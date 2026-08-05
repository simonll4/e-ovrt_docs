"""Campaña R (sujeto) — el costo del tiempo real bajo granularidad G1.

Contraparte por sujeto de `96-costo-tiempo-real-runner.py`. G1 (doc 89) es el
mejor resultado del banco (F1 0,930) y su ganancia es 100% del motor: las
detecciones son bit a bit las de T1. La pregunta acá es si esa ganancia
SOBREVIVE a la densidad de evidencia del tiempo real — y hay motivo para dudar:
el tracker es IoU sobre frames consecutivos, y a stride 7 los frames pasan de
estar a 33 ms a estar a 233 ms. Si la identidad se rompe, G1 se degrada a G0
y la mejor combinación del banco deja de serlo en vivo. Eso es exactamente lo
que hay que medir, no suponer.

Por clip:  track_detections(detecciones del stride N) -> tracked.jsonl
        -> eovrt-control replay (cr01_cr02_v2_subject)
        -> evaluate-alerts vs gt/<clip>.json
        -> eval_<clip>.json

Variable única contra la campaña de escena del MISMO stride: la granularidad.
Variable única contra G1 (stride 1): la densidad de evidencia.

GUARD (doc 89): si una persona queda sin `track_id`, el motor degrada a escena
EN SILENCIO (causa `no_track_id`) y esto mediría G0 creyendo medir G1. Se
verifica por clip. A densidad reducida el guard es MÁS relevante, no menos.

Uso: 96-costo-tiempo-real-sujeto.py --stride N [--clips ...]
"""
import argparse, json, subprocess, sys, time
from pathlib import Path

DS = Path("/home/simonll4/projects/e-ovrt_datasets")
MP = Path("/home/simonll4/projects/e-ovrt_media-plane")
CP = Path("/home/simonll4/projects/e-ovrt_control-plane")
PATTERNS = CP / "configs/patterns/cr01_cr02_v2_subject.yaml"

sys.path.insert(0, str(CP / "src"))
from eovrt_control.tools.track_detections import track_event_stream  # noqa: E402


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


def replay_and_eval(clip_id, det_path, out_dir, stride):
    cfg = out_dir / f"replay_{clip_id}.yaml"
    cfg.write_text(
        "run:\n  id: null\n  scenario: DBE\n"
        f"  name: control_rt_s{stride}_subject_{clip_id}\n"
        f'  description: "Costo del tiempo real (sujeto) — {clip_id}, stride {stride}."\n'
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
    ap.add_argument("--stride", type=int, required=True)
    ap.add_argument("--clips", default="")
    a = ap.parse_args()

    base = Path(__file__).parent
    escena = base / f"96-rt-stride{a.stride}" / "resultados.json"
    if not escena.exists():
        print(f"FALTA la campaña de escena del stride {a.stride}: {escena}")
        return 2
    proc = {r["clip_id"]: r["media_run_id"]
            for r in json.loads(escena.read_text())
            if r.get("media_run_id") and "eval" in r}

    clips = [c.strip() for c in a.clips.split(",") if c.strip()] or sorted(proc)
    out_dir = base / f"96-rt-stride{a.stride}-subject"
    (out_dir / "control_runs").mkdir(parents=True, exist_ok=True)
    (out_dir / "tracked").mkdir(parents=True, exist_ok=True)

    res_path = out_dir / "resultados.json"
    results = json.loads(res_path.read_text()) if res_path.exists() else []
    hechos = {r["clip_id"] for r in results if "eval" in r}

    print(f"=== stride {a.stride} · granularidad SUJETO — {len(clips)} clips ===", flush=True)
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
                MP / "runs" / proc[cid] / "detections.jsonl", tracked)
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

        ev, err = replay_and_eval(cid, tracked, out_dir, a.stride)
        if err:
            print(f"    CONTROL FALLO: {err}", flush=True)
            results.append({"clip_id": cid, "error": err})
            res_path.write_text(json.dumps(results, indent=2, ensure_ascii=False)); continue

        e = json.loads(ev.read_text())
        results.append({"clip_id": cid, "eval": e, "media_run_id": proc[cid],
                        "stride": a.stride,
                        "frames": stats["frames"],
                        "person_detections": stats["person_detections"],
                        "tracks": stats["tracks"]})
        res_path.write_text(json.dumps(results, indent=2, ensure_ascii=False))
        print(f"    OK — {stats['tracks']} tracks sobre {stats['person_detections']} personas",
              flush=True)

    ok = len([r for r in results if "eval" in r])
    print(f"\n{ok}/{len(clips)} clips OK en {(time.time()-t0)/60:.1f} min -> {res_path}")
    return 0 if ok == len(clips) else 1


if __name__ == "__main__":
    sys.exit(main())
