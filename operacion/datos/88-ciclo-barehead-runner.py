"""Campaña B1: `bare_head` como evidencia directa vs ausencia espacial, mismo caption.

Cierra F-84.5 (doc 84): la especialidad CR-01 de `gdino-base-560` (recall 0.599 vs
0.308 de tiny, doc 64) se midio DETECTANDO `bare_head`, y el prompt set desplegado
`cr01_cr02_v2_short` no incluye esa clase — T2 nunca la ejercito. Es la ultima
palanca de percepcion sin medir a Nivel B.

Diseño: UNA inferencia por clip con el prompt set `cr01_cr02_bench_v2` (4 clases,
el MISMO caption en el que se midio la especialidad) y DOS replays sobre las MISMAS
detecciones:

  (a) cr01_cr02_v2       -> E-IND (spatial_absence sobre person/helmet)
  (b) cr01_bare_head_v1  -> bare_head como evidencia directa (region_center)

Como (a) y (b) comparten las detecciones bit a bit, la comparacion entre ambas es de
variable unica: cambia SOLO el evaluador. Y (a) contra T2 (mismo modelo, caption de
3 clases) aisla el efecto del caption.

Uso: 88-ciclo-barehead-runner.py [--clips ...] [--out-dir DIR]
"""
import argparse, json, subprocess, sys, time, urllib.request
from pathlib import Path

MEDIA = "http://127.0.0.1:8080"
DS = Path("/home/simonll4/projects/e-ovrt_datasets")
MP = Path("/home/simonll4/projects/e-ovrt_media-plane")
CP = Path("/home/simonll4/projects/e-ovrt_control-plane")

VARIANTES = {
    "eind": CP / "configs/patterns/cr01_cr02_v2.yaml",
    "barehead": CP / "configs/patterns/cr01_bare_head_v1.yaml",
}
ACTIVOS = {"eind": ["CR-01", "CR-02"], "barehead": ["CR-01"]}

# Prompt set cr01_cr02_bench_v2 transcripto literal (4 clases) — el caption en el que
# doc 64 midio la especialidad bare_head de base-560.
PROMPTS = {
    "set_inline": {
        "id": "cr01_cr02_bench_v2",
        "classes": [
            {"id": "person", "phrasings": {"default": ["person"]}},
            {"id": "helmet", "phrasings": {"default": ["helmet"]}},
            {"id": "vest", "phrasings": {"default": ["vest"]}},
            {"id": "bare_head", "phrasings": {"default": ["bare head"]}},
        ],
    },
    "active_ids": ["person", "helmet", "vest", "bare_head"],
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
        "run": {"name": f"b1_barehead_{clip_id}", "save_previews": False},
    }
    r = _post("/api/runs", body)
    run_id = r.get("run_id") or r.get("id")
    while True:
        time.sleep(2)
        s = _get(f"/api/runs/{run_id}")
        st = (s.get("status") or s.get("state") or "").lower()
        if st in ("completed", "finished", "succeeded", "failed", "error", "stopped", "cancelled"):
            return run_id, st


def replay_and_eval(clip_id, det_path, out_dir, variante):
    patterns = VARIANTES[variante]
    sub = out_dir / variante
    (sub / "control_runs").mkdir(parents=True, exist_ok=True)
    cfg = sub / f"replay_{clip_id}.yaml"
    activos = "".join(f"    - {c}\n" for c in ACTIVOS[variante])
    cfg.write_text(
        "run:\n  id: null\n  scenario: DBE\n"
        f"  name: control_b1_{variante}_{clip_id}\n"
        f'  description: "B1 {variante} — {clip_id}, caption cr01_cr02_bench_v2."\n'
        f"input:\n  type: media_jsonl\n  path: {det_path}\n"
        f"patterns:\n  file: {patterns}\n  active_ids:\n{activos}"
        f"outputs:\n  base_dir: {sub / 'control_runs'}\n"
        "  save_pattern_events_jsonl: true\n  save_alerts_jsonl: true\n"
        "  save_metrics_jsonl: true\n  save_errors_jsonl: true\n  save_summary_json: true\n"
        "logging:\n  level: WARNING\n")
    before = {p.name for p in (sub / "control_runs").glob("*") if p.is_dir()}
    r = subprocess.run([str(CP / ".venv/bin/eovrt-control"), "replay", str(cfg)],
                       capture_output=True, text=True, cwd=str(CP))
    if r.returncode != 0:
        return None, f"replay rc={r.returncode}: {(r.stderr or r.stdout)[-300:]}"
    nuevos = [p for p in (sub / "control_runs").glob("*")
              if p.is_dir() and p.name not in before]
    if len(nuevos) != 1:
        return None, f"el replay creo {len(nuevos)} directorios nuevos (esperaba 1)"
    alerts = nuevos[0] / "alerts.jsonl"
    if not alerts.exists():
        return None, f"no se encontro {alerts}"
    ev = sub / f"eval_{clip_id}.json"
    r2 = subprocess.run(
        [str(CP / ".venv/bin/eovrt-control"), "evaluate-alerts", str(alerts),
         str(DS / "datasets-videos/gt" / f"{clip_id}.json"),
         "--detections", str(det_path), "--patterns", str(patterns), "-o", str(ev)],
        capture_output=True, text=True, cwd=str(CP))
    if r2.returncode != 0:
        return None, f"evaluate rc={r2.returncode}: {(r2.stderr or r2.stdout)[-300:]}"
    return ev, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--clips", default="")
    ap.add_argument("--out-dir", default=str(Path(__file__).parent / "88-b1-barehead-clips"))
    a = ap.parse_args()

    clips = ([c.strip() for c in a.clips.split(",") if c.strip()]
             or sorted(p.stem for p in (DS / "datasets-videos/gt").glob("a_p*.json")))
    out_dir = Path(a.out_dir); out_dir.mkdir(parents=True, exist_ok=True)

    res_path = out_dir / "resultados.json"
    results = json.loads(res_path.read_text()) if res_path.exists() else []
    hechos = {r["clip_id"] for r in results if r.get("evals")}

    t0 = time.time()
    for i, cid in enumerate(clips, 1):
        if cid in hechos:
            print(f"[{i}/{len(clips)}] {cid} — ya evaluado, se saltea", flush=True)
            continue
        results = [r for r in results if r["clip_id"] != cid]
        t1 = time.time()
        print(f"[{i}/{len(clips)}] {cid} ...", flush=True)
        try:
            run_id, st = media_run(cid)
        except Exception as e:
            print(f"    MEDIA FALLO: {e}", flush=True)
            results.append({"clip_id": cid, "error": f"media: {e}"})
            res_path.write_text(json.dumps(results, indent=2, ensure_ascii=False)); continue
        if st not in ("completed", "finished", "succeeded"):
            results.append({"clip_id": cid, "error": f"media estado {st}"})
            res_path.write_text(json.dumps(results, indent=2, ensure_ascii=False)); continue
        det = MP / "runs" / run_id / "detections.jsonl"
        if not det.exists():
            results.append({"clip_id": cid, "error": "sin detections.jsonl"})
            res_path.write_text(json.dumps(results, indent=2, ensure_ascii=False)); continue

        evals, errores = {}, {}
        for variante in VARIANTES:
            ev, err = replay_and_eval(cid, det, out_dir, variante)
            if err:
                errores[variante] = err
            else:
                evals[variante] = json.loads(ev.read_text())
        if errores:
            print(f"    CONTROL FALLO: {errores}", flush=True)
            results.append({"clip_id": cid, "media_run_id": run_id, "error": str(errores)})
        else:
            results.append({"clip_id": cid, "media_run_id": run_id, "evals": evals,
                            "seconds": round(time.time() - t1, 1)})
            print(f"    OK en {time.time()-t1:.0f}s   "
                  f"[{len([r for r in results if r.get('evals')])} listos, "
                  f"{(time.time()-t0)/60:.0f} min]", flush=True)
        res_path.write_text(json.dumps(results, indent=2, ensure_ascii=False))

    ok = len([r for r in results if r.get("evals")])
    print(f"\n{ok}/{len(clips)} clips OK -> {res_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
