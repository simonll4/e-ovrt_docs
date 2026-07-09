"""Benchmark de modelos OVD en el host local.

Para cada ref de modelo levanta el servicio media-plane en un proceso propio
(VRAM y tiempo de carga limpios), corre dos suites y baja el servicio:

  A) BENCH v2 val (114 imgs, determinista) -> mAP@0.5, AP por clase, latencias
  B) Cámara RTSP en vivo                    -> capacidad de tiempo real (keep-up)

Escribe resultados crudos a bench_results.json. No versiona credenciales:
la URL sale de configs/runs/local/rtsp_camera.env.
"""
from __future__ import annotations

import json
import os
import re
import signal
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

import yaml

REPO = Path("/home/simonll4/projects/e-ovrt_media-plane")
SCRATCH = Path("/tmp/claude-1000/-home-simonll4-projects/5bd0dd53-f0ed-4add-9710-a38d67c1d5df/scratchpad")
BASE = "http://127.0.0.1:8080"
PORT = 8080

MODELS = [
    "grounding-dino/gdino-tiny",
    "grounding-dino/gdino-base",
    "yoloe/yoloe-26s",
    "yoloe/yoloe-26m",
    "yoloe/yoloe-26l",
    "yoloe/yoloe-26x",
]

BENCH_DATASET = "bench_v2_val"
RTSP_MAX_UNITS = 100
ACTIVE_IDS = ["person", "helmet", "vest", "bare_head"]


def prompt_set() -> dict:
    path = REPO.parent / "e-ovrt_experimental-setup/prompts/cr01_cr02_bench_v2.yaml"
    return yaml.safe_load(path.read_text())["prompt_set"]


def rtsp_url() -> str:
    env = (REPO / "configs/runs/local/rtsp_camera.env").read_text()
    m = re.search(r'EZVIZ_RTSP_URL="([^"]+)"', env)
    if not m:
        raise RuntimeError("no se pudo leer EZVIZ_RTSP_URL")
    return m.group(1)


def redact(url: str) -> str:
    return re.sub(r"//[^/@]+@", "//***:***@", url)


def http(method: str, path: str, payload: dict | None = None, timeout: float = 30.0):
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(BASE + path, data=data, method=method)
    if data:
        req.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(req, timeout=timeout) as r:
        body = r.read().decode()
    return r.status, (json.loads(body) if body else None)


def http_safe(method: str, path: str, payload: dict | None = None, timeout: float = 30.0):
    try:
        return http(method, path, payload, timeout)
    except urllib.error.HTTPError as e:
        return e.code, {"detail": e.read().decode()[:400]}
    except Exception as e:  # noqa: BLE001
        return 0, {"detail": f"{type(e).__name__}: {e}"}


def wait_ready(proc: subprocess.Popen, limit: float = 300.0) -> float | None:
    """Devuelve segundos hasta /readyz OK, o None si murió/timeout."""
    started = time.perf_counter()
    while time.perf_counter() - started < limit:
        if proc.poll() is not None:
            return None
        status, _ = http_safe("GET", "/readyz", timeout=3)
        if status == 200:
            return time.perf_counter() - started
        time.sleep(1)
    return None


def start_service(model_ref: str, log_path: Path) -> subprocess.Popen:
    env = {**os.environ, "EOVRT_MODEL_REF": model_ref}
    return subprocess.Popen(
        [
            str(REPO / ".venv/bin/python"), "-m", "uvicorn", "--factory",
            "eovrt_media.service.app:create_app",
            "--host", "127.0.0.1", "--port", str(PORT), "--log-level", "warning",
        ],
        cwd=REPO, env=env,
        stdout=log_path.open("w"), stderr=subprocess.STDOUT,
        start_new_session=True,
    )


def stop_service(proc: subprocess.Popen) -> None:
    if proc.poll() is not None:
        return
    os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
    try:
        proc.wait(timeout=40)
    except subprocess.TimeoutExpired:
        os.killpg(os.getpgid(proc.pid), signal.SIGKILL)
        proc.wait(timeout=10)
    time.sleep(2)  # que el puerto quede libre


def await_run(run_id: str, limit: float = 900.0) -> dict:
    started = time.perf_counter()
    while time.perf_counter() - started < limit:
        status, info = http_safe("GET", f"/api/runs/{run_id}", timeout=10)
        if status == 200 and info["status"] in ("succeeded", "failed", "error", "stopped"):
            return info
        time.sleep(2)
    return {"status": "timeout"}


def launch(ingest: dict, run_params: dict, pset: dict) -> tuple[int, dict]:
    return http_safe("POST", "/api/runs", {
        "ingest": ingest,
        "prompts": {"set_inline": pset, "active_ids": ACTIVE_IDS},
        "run": run_params,
    }, timeout=60)


def suite_bench(pset: dict) -> dict:
    code, resp = launch(
        {"plugin": "image_folder", "config": {"dataset": BENCH_DATASET}},
        {"name": "bench_v2_val", "save_previews": False},
        pset,
    )
    if code != 201:
        return {"error": f"launch {code}: {resp}"}
    run_id = resp["run_id"]
    info = await_run(run_id)
    out = {"run_id": run_id, "status": info.get("status"), "summary": info.get("summary")}
    if info.get("status") == "succeeded":
        ec, ev = http_safe("POST", f"/api/runs/{run_id}/evaluate", timeout=300)
        out["eval_status"] = ec
        out["eval"] = ev
    return out


def suite_rtsp(pset: dict, url: str) -> dict:
    code, resp = launch(
        {"plugin": "rtsp", "config": {"url": url, "reconnect_retries": 3, "reconnect_delay_ms": 1000}},
        {"name": "camera_live", "max_units": RTSP_MAX_UNITS, "save_previews": False},
        pset,
    )
    if code != 201:
        return {"error": f"launch {code}: {resp}"}
    run_id = resp["run_id"]
    info = await_run(run_id, limit=300)
    return {"run_id": run_id, "status": info.get("status"), "summary": info.get("summary")}


def main() -> int:
    pset = prompt_set()
    url = rtsp_url()
    print(f"cámara: {redact(url)}", flush=True)

    results = []
    for ref in MODELS:
        print(f"\n===== {ref} =====", flush=True)
        entry: dict = {"model_ref": ref}
        log = SCRATCH / f"svc_{ref.replace('/', '_')}.log"
        proc = start_service(ref, log)
        try:
            load_s = wait_ready(proc)
            if load_s is None:
                entry["error"] = "no llegó a ready"
                entry["log_tail"] = log.read_text()[-800:]
                print("  FALLÓ el arranque", flush=True)
                results.append(entry)
                continue
            entry["load_seconds"] = round(load_s, 2)
            _, model_info = http_safe("GET", "/api/model")
            entry["model_info"] = model_info
            print(f"  ready en {load_s:.1f}s (device={model_info.get('device')})", flush=True)

            t0 = time.perf_counter()
            entry["bench"] = suite_bench(pset)
            print(f"  BENCH ok en {time.perf_counter() - t0:.1f}s "
                  f"(mAP50={((entry['bench'].get('eval') or {}).get('mAP50'))})", flush=True)

            entry["rtsp"] = suite_rtsp(pset, url)
            s = entry["rtsp"].get("summary") or {}
            print(f"  RTSP: procesados={s.get('units_processed')} "
                  f"descartados={s.get('units_dropped')}", flush=True)
        finally:
            stop_service(proc)
        results.append(entry)

    out = SCRATCH / "bench_results.json"
    out.write_text(json.dumps(results, indent=2))
    print(f"\nresultados -> {out}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
