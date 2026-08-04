"""Campaña D1 (Fase 2 de E-DIR, Nivel B) sobre el banco de clips del rodaje.

Igual cadena que el runner 81 (media -> replay -> evaluate-alerts), con la ESTRATEGIA
como variable (doc 12 §6.3: estrategia = prompt set + evaluador):

  - prompts: person + las dos variantes E-DIR ganadoras por condicion en la mitad A
    de bench_obra (doc 83): cr01_spec y cr02_obs. `person` NO es evidencia — es el
    sujeto que exige el gating por persona del evaluador direct_evidence (doc 12
    §4.2): sin detecciones de persona, todo hit directo queda ungated y el patron no
    puede disparar nunca.
  - patterns: cr01_cr02_edir_v1 (strategy: edir, mismos timings 4000/7000 que v2).

El brazo E-IND de la Fase 2 NO se corre: es T1 (caption eind_v1 byte-identico a
cr01_cr02_v2_short — doc 83 §5 bis).

Uso: 85-ciclo-edir-runner.py [--clips a_p1_c02,...] [--out-dir DIR]
"""
import argparse, json, subprocess, sys, time, urllib.request
from pathlib import Path

MEDIA = "http://127.0.0.1:8080"
DS = Path("/home/simonll4/projects/e-ovrt_datasets")
MP = Path("/home/simonll4/projects/e-ovrt_media-plane")
CP = Path("/home/simonll4/projects/e-ovrt_control-plane")
PATTERNS = CP / "configs/patterns/cr01_cr02_edir_v1.yaml"

# Frases CONGELADAS de edir_v1 (frozen_sha256 a1278d0c..., acta doc 76) — transcriptas
# literales; una frase mal elegida es un resultado, no un bug.
PROMPTS = {
    "set_inline": {
        "id": "edir_v1_pair_nivel_b",
        "classes": [
            {"id": "person", "phrasings": {"default": ["person"]}},
            {"id": "cr01_spec",
             "phrasings": {"default": ["construction worker without safety helmet"]}},
            {"id": "cr02_obs",
             "phrasings": {"default": ["person without bright colored safety clothing"]}},
        ],
    },
    "active_ids": ["person", "cr01_spec", "cr02_obs"],
}


def _post(path, body):
    req = urllib.request.Request(MEDIA + path, method="POST",
                                data=json.dumps(body).encode(),
                                headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())


def _get(path):
    with urllib.request.urlopen(MEDIA + path, timeout=60) as r:
        return json.loads(r.read())


def media_run(clip_id):
    body = {
        "ingest": {"plugin": "video_file", "config": {
            "path": str(DS / "datasets-videos/clips" / f"{clip_id}.mp4"),
            "source_id": clip_id,
        }},
        "prompts": PROMPTS,
        "run": {"name": f"d1_edir_{clip_id}", "save_previews": False},
    }
    r = _post("/api/runs", body)
    run_id = r.get("run_id") or r.get("id")
    while True:
        time.sleep(2)
        s = _get(f"/api/runs/{run_id}")
        st = (s.get("status") or s.get("state") or "").lower()
        if st in ("completed", "finished", "succeeded", "failed", "error", "stopped", "cancelled"):
            return run_id, st, s


def replay_and_eval(clip_id, det_path, out_dir):
    cfg = out_dir / f"replay_{clip_id}.yaml"
    cfg.write_text(
        "run:\n  id: null\n  scenario: DBE\n"
        f"  name: control_d1_edir_{clip_id}\n"
        f'  description: "D1 E-DIR Nivel B — {clip_id}, pattern set cr01_cr02_edir_v1."\n'
        f"input:\n  type: media_jsonl\n  path: {det_path}\n"
        f"patterns:\n  file: {PATTERNS}\n  active_ids:\n    - CR-01\n    - CR-02\n"
        f"outputs:\n  base_dir: {out_dir / 'control_runs'}\n"
        "  save_pattern_events_jsonl: true\n  save_alerts_jsonl: true\n"
        "  save_metrics_jsonl: true\n  save_errors_jsonl: true\n  save_summary_json: true\n"
        "logging:\n  level: WARNING\n")
    # Identificacion por DIFERENCIA de directorios (trampa 4 del doc 82): por mtime
    # cruzaria alertas de un clip con el GT de otro en silencio.
    before = {p.name for p in (out_dir / "control_runs").glob("*") if p.is_dir()}
    r = subprocess.run([str(CP / ".venv/bin/eovrt-control"), "replay", str(cfg)],
                       capture_output=True, text=True, cwd=str(CP))
    if r.returncode != 0:
        return None, f"replay rc={r.returncode}: {(r.stderr or r.stdout)[-300:]}"
    nuevos = [p for p in (out_dir / "control_runs").glob("*")
              if p.is_dir() and p.name not in before]
    if len(nuevos) != 1:
        return None, (f"el replay creo {len(nuevos)} directorios nuevos (esperaba 1): "
                      f"{[p.name for p in nuevos]}")
    alerts = nuevos[0] / "alerts.jsonl"
    if not alerts.exists():
        return None, f"no se encontro {alerts}"
    ev = out_dir / f"eval_{clip_id}.json"
    r2 = subprocess.run(
        [str(CP / ".venv/bin/eovrt-control"), "evaluate-alerts", str(alerts),
         str(DS / "datasets-videos/gt" / f"{clip_id}.json"),
         "--detections", str(det_path), "--patterns", str(PATTERNS), "-o", str(ev)],
        capture_output=True, text=True, cwd=str(CP))
    if r2.returncode != 0:
        return None, f"evaluate rc={r2.returncode}: {(r2.stderr or r2.stdout)[-300:]}"
    return ev, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--clips", default="")
    ap.add_argument("--out-dir", default=str(Path(__file__).parent / "85-d1-edir-clips"))
    a = ap.parse_args()

    clips = ([c.strip() for c in a.clips.split(",") if c.strip()]
             or sorted(p.stem for p in (DS / "datasets-videos/gt").glob("a_p*.json")))
    out_dir = Path(a.out_dir); (out_dir / "control_runs").mkdir(parents=True, exist_ok=True)

    res_path = out_dir / "resultados.json"
    results = json.loads(res_path.read_text()) if res_path.exists() else []
    hechos = {r["clip_id"] for r in results if "eval" in r}

    def guardar():
        res_path.write_text(json.dumps(results, indent=2, ensure_ascii=False))

    t_camp = time.time()
    for i, cid in enumerate(clips, 1):
        if cid in hechos:
            print(f"[{i}/{len(clips)}] {cid} — ya evaluado, se saltea", flush=True)
            continue
        results = [r for r in results if r["clip_id"] != cid]
        t0 = time.time()
        print(f"[{i}/{len(clips)}] {cid} ...", flush=True)
        try:
            run_id, st, summary = media_run(cid)
        except Exception as e:
            print(f"    MEDIA FALLO: {e}", flush=True)
            results.append({"clip_id": cid, "error": f"media: {e}"}); guardar(); continue
        if st not in ("completed", "finished", "succeeded"):
            print(f"    MEDIA estado={st}", flush=True)
            results.append({"clip_id": cid, "error": f"media estado {st}"}); guardar(); continue
        det = MP / "runs" / run_id / "detections.jsonl"
        if not det.exists():
            results.append({"clip_id": cid, "error": "sin detections.jsonl"}); guardar(); continue
        ev, err = replay_and_eval(cid, det, out_dir)
        dt = time.time() - t0
        if err:
            print(f"    CONTROL FALLO: {err}", flush=True)
            results.append({"clip_id": cid, "error": err}); guardar(); continue
        e = json.loads(ev.read_text())
        results.append({"clip_id": cid, "media_run_id": run_id, "eval": e,
                        "seconds": round(dt, 1)})
        guardar()
        ok = len([r for r in results if "eval" in r])
        print(f"    OK en {dt:.1f}s -> {ev.name}   "
              f"[{ok} listos, {(time.time()-t_camp)/60:.0f} min transcurridos]", flush=True)

    guardar()
    print(f"\n{len([r for r in results if 'eval' in r])}/{len(clips)} clips OK")
    print(f"-> {res_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
