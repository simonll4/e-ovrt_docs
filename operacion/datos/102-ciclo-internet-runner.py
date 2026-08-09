"""Campañas I1 / I2 — estrato B (lote de internet) sobre el banco de clips.

Es el runner del doc 81 apuntado a los clips `v*` del lote de internet, más la
fase de sujeto del doc 89. Dos campañas, misma combinación que las de referencia
del rodaje, cambiando SOLO el estrato de material:

  I1  scene    = T1 sobre estrato B   (necesita GPU: hay inferencia)
  I2  subject  = G1 sobre estrato B   (SIN GPU: reusa las detecciones de I1)

Fase `scene` (I1), por clip:
    media-plane POST /api/runs (video_file, source_id=clip_id)
      -> detections.jsonl
      -> eovrt-control replay (pattern set OFICIAL cr01_cr02_v2)
      -> evaluate-alerts vs gt/<clip>.json (+SDR/TTFD con --detections)
      -> eval_<clip>.json

Fase `subject` (I2), por clip:
    track_detections sobre las detecciones de I1 -> tracked.jsonl
      -> eovrt-control replay (cr01_cr02_v2_subject, granularity: subject)
      -> evaluate-alerts vs el MISMO gt/<clip>.json
      -> eval_<clip>.json

Variable única entre I1 e I2: la granularidad del motor. Las cajas son bit a bit
las mismas (no hay inferencia nueva en la fase subject) — el mismo contraste de
variable única que T1 vs G1.

Requisito de la fase scene: el media-plane sirviendo en :8080 con el modelo
campeón cargado —
    cd e-ovrt_media-plane && EOVRT_MODEL_REF=grounding-dino/gdino-tiny-560 make serve
(o `docs/operacion/datos/91-arrancar-servicios.sh`).

Uso:
    102-ciclo-internet-runner.py --fase scene
    102-ciclo-internet-runner.py --fase subject
    102-ciclo-internet-runner.py --fase scene --clips v04_c01      # uno solo

Reanudable: si `resultados.json` ya tiene el clip evaluado, lo saltea.
"""
import argparse, json, subprocess, sys, time, urllib.request
from pathlib import Path

MEDIA = "http://127.0.0.1:8080"
DS = Path("/home/simonll4/projects/e-ovrt_datasets")
MP = Path("/home/simonll4/projects/e-ovrt_media-plane")
CP = Path("/home/simonll4/projects/e-ovrt_control-plane")
DATOS = Path(__file__).parent

# Los 3 clips del lote de internet con GT humano (doc 102). El resto del lote
# sigue sin corregir en CVAT y NO entra: sin GT no hay nada contra qué evaluar.
CLIPS = ["v04_c01", "v06_c01", "v10_c01"]

PATTERNS = {
    "scene": CP / "configs/patterns/cr01_cr02_v2.yaml",
    "subject": CP / "configs/patterns/cr01_cr02_v2_subject.yaml",
}
OUT_DIRS = {
    "scene": DATOS / "102-i1-internet-scene-clips",
    "subject": DATOS / "102-i2-internet-subject-clips",
}

# Prompt set CONGELADO cr01_cr02_v2_short (frozen_sha256 df81fd48...) — el mismo
# de T1/G1 y de toda evaluación de bench. Espejo inline, idéntico al del doc 81.
PROMPTS = {
    "set_inline": {
        "id": "cr01_cr02_v2_short",
        "classes": [
            {"id": "person", "phrasings": {"default": ["person"]}},
            {"id": "helmet", "phrasings": {"default": ["helmet"]}},
            {"id": "vest", "phrasings": {"default": ["vest"]}},
        ],
    },
    "active_ids": ["person", "helmet", "vest"],
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
        "run": {"name": f"bench_internet_{clip_id}", "save_previews": False},
    }
    r = _post("/api/runs", body)
    run_id = r.get("run_id") or r.get("id")
    while True:
        time.sleep(2)
        s = _get(f"/api/runs/{run_id}")
        st = (s.get("status") or s.get("state") or "").lower()
        if st in ("completed", "finished", "succeeded", "failed", "error", "stopped", "cancelled"):
            return run_id, st, s


def _verificar_track_ids(path: Path):
    """(personas, personas sin track_id) — guard del doc 89.

    Si alguna persona queda sin `track_id` el motor degrada a escena EN SILENCIO
    (causa `no_track_id`) y la campaña mediría G0 creyendo medir G1.
    """
    total = sin_id = 0
    with path.open() as fh:
        for line in fh:
            if not line.strip():
                continue
            for d in json.loads(line).get("detections") or []:
                if d.get("label") == "person":
                    total += 1
                    if not d.get("track_id"):
                        sin_id += 1
    return total, sin_id


def replay_and_eval(clip_id, det_path, out_dir, fase):
    patterns = PATTERNS[fase]
    cfg = out_dir / f"replay_{clip_id}.yaml"
    cfg.write_text(
        "run:\n  id: null\n  scenario: DBE\n"
        f"  name: control_internet_{fase}_{clip_id}\n"
        f'  description: "Estrato B (lote de internet) — {clip_id}, granularidad {fase}."\n'
        f"input:\n  type: media_jsonl\n  path: {det_path}\n"
        f"patterns:\n  file: {patterns}\n  active_ids:\n    - CR-01\n    - CR-02\n"
        f"outputs:\n  base_dir: {out_dir / 'control_runs'}\n"
        "  save_pattern_events_jsonl: true\n  save_alerts_jsonl: true\n"
        "  save_metrics_jsonl: true\n  save_errors_jsonl: true\n  save_summary_json: true\n"
        "logging:\n  level: WARNING\n")
    # Identificar el run del control por DIFERENCIA de directorios, no por mtime:
    # tomar "el más nuevo" cruzaría las alertas de un clip con el GT de otro en
    # silencio, y el error no se vería en ningún lado (doc 81).
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
         "--detections", str(det_path), "--patterns", str(patterns), "-o", str(ev)],
        capture_output=True, text=True, cwd=str(CP))
    if r2.returncode != 0:
        return None, f"evaluate rc={r2.returncode}: {(r2.stderr or r2.stdout)[-300:]}"
    return ev, None


def detecciones_de_i1(clip_id, scene_dir=None):
    """media_run_id de la fase scene, leído de su resultados.json.

    `scene_dir` permite encadenar la fase subject sobre OTRA corrida de escena
    (p.ej. la de `gdino-base-560` del doc 104) sin tocar la de I1.
    """
    res = (Path(scene_dir) if scene_dir else OUT_DIRS["scene"]) / "resultados.json"
    if not res.exists():
        raise RuntimeError(
            "la fase subject reusa las detecciones de la fase scene y todavía no "
            f"existe {res} — correr primero: 102-ciclo-internet-runner.py --fase scene")
    por_clip = {r["clip_id"]: r.get("media_run_id")
                for r in json.loads(res.read_text()) if r.get("media_run_id")}
    if clip_id not in por_clip:
        raise RuntimeError(f"{clip_id} no tiene corrida de la fase scene todavía")
    return MP / "runs" / por_clip[clip_id] / "detections.jsonl"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fase", choices=["scene", "subject"], required=True)
    ap.add_argument("--clips", default="")
    ap.add_argument("--out-dir", default="")
    ap.add_argument("--scene-dir", default="",
                    help="fase subject: dir de la corrida de escena cuyas detecciones reusar")
    a = ap.parse_args()

    clips = [c.strip() for c in a.clips.split(",") if c.strip()] or CLIPS
    out_dir = Path(a.out_dir) if a.out_dir else OUT_DIRS[a.fase]
    (out_dir / "control_runs").mkdir(parents=True, exist_ok=True)
    if a.fase == "subject":
        (out_dir / "tracked").mkdir(parents=True, exist_ok=True)
        sys.path.insert(0, str(CP / "src"))
        from eovrt_control.tools.track_detections import track_event_stream

    res_path = out_dir / "resultados.json"
    results = json.loads(res_path.read_text()) if res_path.exists() else []
    hechos = {r["clip_id"] for r in results if "eval" in r}

    def guardar():
        # Incremental: v06_c01 solo son 11.087 frames; no perder todo por un fallo tardío.
        res_path.write_text(json.dumps(results, indent=2, ensure_ascii=False))

    t_camp = time.time()
    for i, cid in enumerate(clips, 1):
        if cid in hechos:
            print(f"[{i}/{len(clips)}] {cid} — ya evaluado, se saltea", flush=True)
            continue
        results = [r for r in results if r["clip_id"] != cid]   # limpia intentos fallidos
        t0 = time.time()
        print(f"[{i}/{len(clips)}] {cid} ({a.fase}) ...", flush=True)
        extra = {}

        if a.fase == "scene":
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
            extra = {"media_run_id": run_id,
                     "frames": summary.get("units_processed") or summary.get("frames")}
        else:
            try:
                origen = detecciones_de_i1(cid, a.scene_dir or None)
                det = out_dir / "tracked" / f"{cid}.jsonl"
                stats = track_event_stream(origen, det)
            except Exception as e:
                print(f"    TRACKING FALLO: {e}", flush=True)
                results.append({"clip_id": cid, "error": f"tracking: {e}"}); guardar(); continue
            personas, sin_id = _verificar_track_ids(det)
            if sin_id:
                print(f"    GUARD: {sin_id}/{personas} personas sin track_id — "
                      f"el motor degradaría a escena y esto mediría G0", flush=True)
                results.append({"clip_id": cid, "error": f"{sin_id} personas sin track_id"})
                guardar(); continue
            extra = {"frames": stats["frames"], "tracks": stats["tracks"],
                     "person_detections": stats["person_detections"]}

        ev, err = replay_and_eval(cid, det, out_dir, a.fase)
        dt = time.time() - t0
        if err:
            print(f"    CONTROL FALLO: {err}", flush=True)
            results.append({"clip_id": cid, "error": err}); guardar(); continue
        results.append({"clip_id": cid, "eval": json.loads(ev.read_text()),
                        "seconds": round(dt, 1), **extra})
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
