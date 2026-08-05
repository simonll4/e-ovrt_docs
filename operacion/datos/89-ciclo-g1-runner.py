"""Campaña G1 (granularidad por sujeto, Nivel B) — SIN GPU.

Cierra la última palanca abierta del banco: el mecanismo (a) de F-81.2 (doc 81), el
único que ninguna palanca de percepción ni de formulación puede tocar. Bajo escena el
motor acumula "alguien sin casco", pero el GT exige que UN SUJETO sostenga la violación
4 s (regla C1 de `derive_clip_gt`); en multitud los sujetos se relevan y la alerta cae
fuera de la ventana.

Por clip:  track_detections(T1) -> tracked.jsonl (track_id post-hoc sobre las MISMAS cajas)
        -> eovrt-control replay (cr01_cr02_v2_subject, granularity: subject)
        -> evaluate-alerts vs gt/<clip>.json

Variable única contra T1: cambia SOLO la granularidad del motor. Las detecciones son
bit a bit las de T1 — no hay inferencia nueva.

Guard: si alguna persona quedara sin `track_id`, el motor degrada a escena EN SILENCIO
(causa `no_track_id`) y la campaña mediría G0 creyendo medir G1. Se verifica por clip.

Uso: 89-ciclo-g1-runner.py [--clips ...] [--out-dir DIR]
"""
import argparse, json, subprocess, sys, time
from pathlib import Path

DS = Path("/home/simonll4/projects/e-ovrt_datasets")
MP = Path("/home/simonll4/projects/e-ovrt_media-plane")
CP = Path("/home/simonll4/projects/e-ovrt_control-plane")
RES = Path("/home/simonll4/projects/e-ovrt_experimental-setup/results/clip_bench")
PATTERNS = CP / "configs/patterns/cr01_cr02_v2_subject.yaml"

sys.path.insert(0, str(CP / "src"))
from eovrt_control.tools.track_detections import track_event_stream  # noqa: E402


def _procedencia(campaign: str) -> dict:
    data = json.loads((RES / campaign / "provenance.json").read_text())
    return {x["clip_id"]: x["media_run_id"] for x in data if x.get("media_run_id")}


def _verificar_track_ids(path: Path) -> tuple[int, int]:
    """(personas, personas sin track_id) — el guard contra medir G0 en silencio."""
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


def replay_and_eval(clip_id, det_path, out_dir):
    cfg = out_dir / f"replay_{clip_id}.yaml"
    cfg.write_text(
        "run:\n  id: null\n  scenario: DBE\n"
        f"  name: control_g1_subject_{clip_id}\n"
        f'  description: "G1 granularidad subject — {clip_id}, track_id post-hoc sobre T1."\n'
        f"input:\n  type: media_jsonl\n  path: {det_path}\n"
        f"patterns:\n  file: {PATTERNS}\n  active_ids:\n    - CR-01\n    - CR-02\n"
        f"outputs:\n  base_dir: {out_dir / 'control_runs'}\n"
        "  save_pattern_events_jsonl: true\n  save_alerts_jsonl: true\n"
        "  save_metrics_jsonl: true\n  save_errors_jsonl: true\n  save_summary_json: true\n"
        "logging:\n  level: WARNING\n")
    before = {p.name for p in (out_dir / "control_runs").glob("*") if p.is_dir()}
    r = subprocess.run([str(CP / ".venv/bin/eovrt-control"), "replay", str(cfg)],
                       capture_output=True, text=True, cwd=str(CP))
    if r.returncode != 0:
        return None, f"replay rc={r.returncode}: {(r.stderr or r.stdout)[-300:]}"
    nuevos = [p for p in (out_dir / "control_runs").glob("*")
              if p.is_dir() and p.name not in before]
    if len(nuevos) != 1:
        return None, f"el replay creo {len(nuevos)} directorios nuevos (esperaba 1)"
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
    ap.add_argument("--out-dir", default=str(Path(__file__).parent / "89-g1-subject-clips"))
    a = ap.parse_args()

    eind = _procedencia("t1_gdinotiny560_v2short_scene")
    clips = [c.strip() for c in a.clips.split(",") if c.strip()] or sorted(eind)

    out_dir = Path(a.out_dir)
    (out_dir / "control_runs").mkdir(parents=True, exist_ok=True)
    (out_dir / "tracked").mkdir(parents=True, exist_ok=True)

    res_path = out_dir / "resultados.json"
    results = json.loads(res_path.read_text()) if res_path.exists() else []
    hechos = {r["clip_id"] for r in results if "eval" in r}

    t0 = time.time()
    for i, cid in enumerate(clips, 1):
        if cid in hechos:
            print(f"[{i}/{len(clips)}] {cid} — ya evaluado, se saltea", flush=True)
            continue
        results = [r for r in results if r["clip_id"] != cid]
        print(f"[{i}/{len(clips)}] {cid} ...", flush=True)
        tracked = out_dir / "tracked" / f"{cid}.jsonl"
        try:
            stats = track_event_stream(
                MP / "runs" / eind[cid] / "detections.jsonl", tracked)
        except Exception as e:
            print(f"    TRACKING FALLO: {e}", flush=True)
            results.append({"clip_id": cid, "error": f"tracking: {e}"})
            res_path.write_text(json.dumps(results, indent=2, ensure_ascii=False)); continue

        personas, sin_id = _verificar_track_ids(tracked)
        if sin_id:
            print(f"    GUARD: {sin_id}/{personas} personas sin track_id — "
                  f"el motor degradaría a escena y esto mediría G0", flush=True)
            results.append({"clip_id": cid, "error": f"{sin_id} personas sin track_id"})
            res_path.write_text(json.dumps(results, indent=2, ensure_ascii=False)); continue

        ev, err = replay_and_eval(cid, tracked, out_dir)
        if err:
            print(f"    CONTROL FALLO: {err}", flush=True)
            results.append({"clip_id": cid, "error": err})
            res_path.write_text(json.dumps(results, indent=2, ensure_ascii=False)); continue

        e = json.loads(ev.read_text())
        results.append({"clip_id": cid, "eval": e, "eind_run_id": eind[cid],
                        "frames": stats["frames"], "person_detections": stats["person_detections"],
                        "tracks": stats["tracks"]})
        res_path.write_text(json.dumps(results, indent=2, ensure_ascii=False))
        print(f"    OK — {stats['tracks']} tracks sobre {stats['person_detections']} personas",
              flush=True)

    ok = len([r for r in results if "eval" in r])
    print(f"\n{ok}/{len(clips)} clips OK en {(time.time()-t0)/60:.1f} min -> {res_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
