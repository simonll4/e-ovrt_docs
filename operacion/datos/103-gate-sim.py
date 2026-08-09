"""Simulación post-hoc del gate de juzgabilidad (hallazgo 103) — EXPLORATORIO.

¿Un umbral mínimo de tamaño de sujeto para la evidencia de AUSENCIA arreglaría
la precision de I2 sin perder los 2 episodios reales? Se filtran las detecciones
person con altura < H px del stream YA TRACKEADO de I2 (mismas cajas, cero
inferencia nueva) y se re-corre replay(subject) + evaluate-alerts.

ADVERTENCIA METODOLÓGICA (va también en el doc): esto es ajuste IN-SAMPLE sobre
el mismo clip que motivó la hipótesis. Sirve para atribuir el mecanismo
(¿plataforma ajustable o piso del modelo?), NO para elegir un umbral de
producción ni para producir métricas de campaña. Cualquier umbral real
necesitaría clips frescos.
"""
import json
import subprocess
import sys
from pathlib import Path

DATOS = Path(__file__).parent
DS = Path("/home/simonll4/projects/e-ovrt_datasets")
CP = Path("/home/simonll4/projects/e-ovrt_control-plane")
PATTERNS = CP / "configs/patterns/cr01_cr02_v2_subject.yaml"
TRACKED = DATOS / "102-i2-internet-subject-clips/tracked"
OUT = DATOS / "103-gate-sim"

CLIPS = ["v04_c01", "v06_c01", "v10_c01"]
THRESHOLDS = [0, 120, 160, 200]   # 0 = control (debe reproducir I2)


def filter_stream(src: Path, dst: Path, h_min: int) -> tuple[int, int]:
    kept = dropped = 0
    with src.open() as fi, dst.open("w") as fo:
        for line in fi:
            if not line.strip():
                continue
            ev = json.loads(line)
            dets = ev.get("detections") or []
            out = []
            for d in dets:
                if d["label"] == "person":
                    h = d["bbox_xyxy"][3] - d["bbox_xyxy"][1]
                    if h < h_min:
                        dropped += 1
                        continue
                    kept += 1
                out.append(d)
            ev["detections"] = out
            fo.write(json.dumps(ev) + "\n")
    return kept, dropped


def replay_and_eval(cid, det_path, out_dir, tag):
    cfg = out_dir / f"replay_{tag}_{cid}.yaml"
    cfg.write_text(
        "run:\n  id: null\n  scenario: DBE\n"
        f"  name: gatesim_{tag}_{cid}\n"
        f'  description: "simulacion gate juzgabilidad {tag} — exploratorio doc 103"\n'
        f"input:\n  type: media_jsonl\n  path: {det_path}\n"
        f"patterns:\n  file: {PATTERNS}\n  active_ids:\n    - CR-01\n    - CR-02\n"
        f"outputs:\n  base_dir: {out_dir / 'control_runs'}\n"
        "  save_alerts_jsonl: true\n  save_summary_json: true\n"
        "logging:\n  level: ERROR\n")
    before = {p.name for p in (out_dir / "control_runs").glob("*") if p.is_dir()}
    r = subprocess.run([str(CP / ".venv/bin/eovrt-control"), "replay", str(cfg)],
                       capture_output=True, text=True, cwd=str(CP))
    if r.returncode != 0:
        return None, f"replay rc={r.returncode}: {(r.stderr or r.stdout)[-200:]}"
    nuevos = [p for p in (out_dir / "control_runs").glob("*")
              if p.is_dir() and p.name not in before]
    alerts = nuevos[0] / "alerts.jsonl"
    ev = out_dir / f"eval_{tag}_{cid}.json"
    r2 = subprocess.run(
        [str(CP / ".venv/bin/eovrt-control"), "evaluate-alerts", str(alerts),
         str(DS / "datasets-videos/gt" / f"{cid}.json"),
         "--detections", str(det_path), "--patterns", str(PATTERNS), "-o", str(ev)],
        capture_output=True, text=True, cwd=str(CP))
    if r2.returncode != 0:
        return None, f"evaluate rc={r2.returncode}: {(r2.stderr or r2.stdout)[-200:]}"
    return json.loads(ev.read_text()), None


def main():
    (OUT / "control_runs").mkdir(parents=True, exist_ok=True)
    print(f"{'H(px)':>6} {'clip':>9} {'matched':>8} {'missed':>7} {'FP':>5} "
          f"{'re_al':>6} {'person kept/dropped':>20}")
    rows = []
    for h in THRESHOLDS:
        tot_fp = tot_matched = tot_missed = 0
        for cid in CLIPS:
            src = TRACKED / f"{cid}.jsonl"
            det = OUT / f"{cid}.h{h}.jsonl"
            kept, dropped = filter_stream(src, det, h)
            ev, err = replay_and_eval(cid, det, OUT, f"h{h}")
            if err:
                print(f"{h:>6} {cid:>9}  ERROR: {err}")
                continue
            m, mi = ev["matched_alerts_count"], ev["missed_alerts_count"]
            fp, re_ = ev["unexpected_alerts_count"], ev["re_alerts_count"]
            print(f"{h:>6} {cid:>9} {m:>8} {mi:>7} {fp:>5} {re_:>6} {kept:>11}/{dropped}")
            tot_fp += fp; tot_matched += m; tot_missed += mi
            rows.append({"h": h, "clip": cid, "matched": m, "missed": mi,
                         "fp": fp, "re_alerts": re_, "kept": kept, "dropped": dropped})
        print(f"{h:>6} {'TOTAL':>9} {tot_matched:>8} {tot_missed:>7} {tot_fp:>5}")
        print()
    (OUT / "resumen.json").write_text(json.dumps(rows, indent=2))
    print(f"-> {OUT}/resumen.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
