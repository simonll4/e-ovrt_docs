"""Campaña H1 (E-HYB-or, Nivel B) sobre el banco de clips — SIN GPU.

La fusion es dual-run (doc 12 §4.1): se fusionan las detecciones YA EXISTENTES de la
corrida E-IND (T1) y la E-DIR (D1) de cada clip, y se re-corre solo el control-plane.
No hay inferencia nueva: toda diferencia observada es atribuible a la funcion de
fusion y no a un caption distinto.

Por clip:  merge_dual_run(T1, D1) -> fusion.jsonl
        -> eovrt-control replay (cr01_cr02_hyb_or_v1)
        -> evaluate-alerts vs gt/<clip>.json
        -> eval_<clip>.json

Uso: 87-ciclo-hybor-runner.py [--clips ...] [--out-dir DIR]
"""
import argparse, json, subprocess, sys, time
from pathlib import Path

DS = Path("/home/simonll4/projects/e-ovrt_datasets")
MP = Path("/home/simonll4/projects/e-ovrt_media-plane")
CP = Path("/home/simonll4/projects/e-ovrt_control-plane")
RES = Path("/home/simonll4/projects/e-ovrt_experimental-setup/results/clip_bench")
PATTERNS = CP / "configs/patterns/cr01_cr02_hyb_or_v1.yaml"
DIRECT_CLASSES = ("cr01_spec", "cr02_obs")

sys.path.insert(0, str(DS / "datasets/scripts"))
from bench.merge_dual_run import merge_detection_streams  # noqa: E402


def _procedencia(campaign: str) -> dict:
    data = json.loads((RES / campaign / "provenance.json").read_text())
    return {x["clip_id"]: x["media_run_id"] for x in data if x.get("media_run_id")}


def replay_and_eval(clip_id, det_path, out_dir):
    cfg = out_dir / f"replay_{clip_id}.yaml"
    cfg.write_text(
        "run:\n  id: null\n  scenario: DBE\n"
        f"  name: control_h1_hybor_{clip_id}\n"
        f'  description: "H1 E-HYB-or Nivel B — {clip_id}, fusion dual-run T1+D1."\n'
        f"input:\n  type: media_jsonl\n  path: {det_path}\n"
        f"patterns:\n  file: {PATTERNS}\n  active_ids:\n    - CR-01\n    - CR-02\n"
        f"outputs:\n  base_dir: {out_dir / 'control_runs'}\n"
        "  save_pattern_events_jsonl: true\n  save_alerts_jsonl: true\n"
        "  save_metrics_jsonl: true\n  save_errors_jsonl: true\n  save_summary_json: true\n"
        "logging:\n  level: WARNING\n")
    # Identificacion por DIFERENCIA de directorios (trampa 4 del doc 82).
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
    ap.add_argument("--out-dir", default=str(Path(__file__).parent / "87-h1-hybor-clips"))
    a = ap.parse_args()

    eind = _procedencia("t1_gdinotiny560_v2short_scene")
    edir = _procedencia("d1_gdinotiny560_edirpair_scene")
    clips = [c.strip() for c in a.clips.split(",") if c.strip()] or sorted(set(eind) & set(edir))
    faltan = sorted(set(edir) - set(eind))
    if faltan:
        print(f"AVISO: {len(faltan)} clips de D1 sin par en T1, se omiten: {faltan[:5]}")

    out_dir = Path(a.out_dir)
    (out_dir / "control_runs").mkdir(parents=True, exist_ok=True)
    (out_dir / "fusion").mkdir(parents=True, exist_ok=True)

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
        fusion = out_dir / "fusion" / f"{cid}.jsonl"
        try:
            stats = merge_detection_streams(
                MP / "runs" / eind[cid] / "detections.jsonl",
                MP / "runs" / edir[cid] / "detections.jsonl",
                fusion, DIRECT_CLASSES)
        except Exception as e:
            print(f"    FUSION FALLO: {e}", flush=True)
            results.append({"clip_id": cid, "error": f"fusion: {e}"})
            res_path.write_text(json.dumps(results, indent=2, ensure_ascii=False)); continue
        ev, err = replay_and_eval(cid, fusion, out_dir)
        if err:
            print(f"    CONTROL FALLO: {err}", flush=True)
            results.append({"clip_id": cid, "error": err})
            res_path.write_text(json.dumps(results, indent=2, ensure_ascii=False)); continue
        results.append({
            "clip_id": cid, "eval": json.loads(ev.read_text()),
            "eind_run_id": eind[cid], "edir_run_id": edir[cid],
            "frames": stats["frames"], "direct_hits": stats["direct_hits"],
        })
        res_path.write_text(json.dumps(results, indent=2, ensure_ascii=False))
        print(f"    OK — {stats['frames']} frames, {stats['direct_hits']} hits directos", flush=True)

    ok = len([r for r in results if "eval" in r])
    print(f"\n{ok}/{len(clips)} clips OK en {(time.time()-t0)/60:.1f} min -> {res_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
