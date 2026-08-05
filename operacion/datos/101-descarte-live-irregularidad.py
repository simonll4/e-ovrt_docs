"""¿Qué tan irregular es el descarte del camino live? (doc 101)

El eje de calidad bajo tiempo real (R1-R6, doc 96) se midió con decimado
REGULAR (`rate_control.stride`), y el propio doc 96 declara el hueco: "el
decimado es regular; el live descarta con jitter según lo que el consumidor
tome. Ese efecto no está medido" (results/realtime/index.md §7). Este script
lo mide, desde los artefactos que ya existen: los `detections.jsonl` de las
corridas live reales (source_type == oak_d) del rodaje (doc 71) y de los
humos EBE (docs 65/67/91).

Por cada corrida live: huecos entre frames procesados consecutivos, en ms
(source.timestamp_ms) y en frames equivalentes a 30 fps (la unidad del banco:
gap_frames = dt_ms / 33.33). Estadísticos de irregularidad: CV (std/media),
p5/p50/p95/max y la fracción de huecos "cerca del regular" (dentro de
±50% de la mediana). Un decimado regular perfecto tiene CV = 0 y frac = 1.

Salidas:
  - tabla compacta por corrida y agregado por grupo (modelo × jornada)
  - 101-descarte-live-distribucion.json: los huecos crudos por grupo, para
    alimentar el muestreador del decimado empírico (task 3 del doc 101)

Uso: python3 101-descarte-live-irregularidad.py [--runs-dir DIR]
"""

import argparse
import json
import statistics as st
from pathlib import Path

MP_RUNS = Path("/home/simonll4/projects/e-ovrt_media-plane/runs")
OUT = Path(__file__).parent / "101-descarte-live-distribucion.json"

# Las 6 corridas finales del rodaje (doc 71 §2.1) — para etiquetarlas en la tabla.
DOC71 = {
    "run_20260725_201020_dbe_grounding_dino_0ca90e": "GDINO P1 (doc71)",
    "run_20260725_201145_dbe_grounding_dino_0eb1fd": "GDINO P2 (doc71)",
    "run_20260725_201247_dbe_grounding_dino_12394a": "GDINO P3 (doc71)",
    "run_20260725_201820_dbe_yoloe_210d40": "YOLOE P1 (doc71)",
    "run_20260725_201916_dbe_yoloe_73535e": "YOLOE P2 (doc71)",
    "run_20260725_202012_dbe_yoloe_e2bfe1": "YOLOE P3 (doc71)",
}

FRAME_MS = 1000.0 / 30.0  # la unidad del banco: clips a 30 fps


def gaps_of_run(run_dir: Path):
    """Huecos (ms) entre frames procesados consecutivos, desde detections.jsonl."""
    det = run_dir / "detections.jsonl"
    if not det.exists():
        return None
    ts = []
    with det.open() as fh:
        for line in fh:
            if not line.strip():
                continue
            ev = json.loads(line)
            src = ev.get("source") or {}
            t = src.get("timestamp_ms")
            if t is not None:
                ts.append(float(t))
    ts.sort()
    return [b - a for a, b in zip(ts, ts[1:]) if b - a > 0]


def stats(gaps):
    if len(gaps) < 5:
        return None
    med = st.median(gaps)
    mean = st.mean(gaps)
    sd = st.pstdev(gaps)
    qs = sorted(gaps)

    def pct(p):
        return qs[min(len(qs) - 1, int(p / 100 * len(qs)))]

    near = sum(1 for g in gaps if 0.5 * med <= g <= 1.5 * med) / len(gaps)
    return {
        "n_gaps": len(gaps),
        "mean_ms": round(mean, 1),
        "median_ms": round(med, 1),
        "cv": round(sd / mean, 3) if mean else None,
        "p5_ms": round(pct(5), 1),
        "p95_ms": round(pct(95), 1),
        "max_ms": round(max(gaps), 1),
        "frac_near_regular": round(near, 3),
        "mean_gap_frames30": round(mean / FRAME_MS, 2),
        "fps_eq": round(1000.0 / mean, 2) if mean else None,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs-dir", default=str(MP_RUNS))
    a = ap.parse_args()
    runs_dir = Path(a.runs_dir)

    rows, groups = [], {}
    for run_dir in sorted(runs_dir.iterdir()):
        summ_p = run_dir / "summary.json"
        if not summ_p.exists():
            continue
        try:
            summ = json.loads(summ_p.read_text())
        except json.JSONDecodeError:
            continue
        if summ.get("source_type") != "oak_d":
            continue  # solo el camino live con cámara real
        gaps = gaps_of_run(run_dir)
        if not gaps:
            continue
        s = stats(gaps)
        if s is None:
            continue
        day = (summ.get("started_at") or "")[:10]
        model = summ.get("model_name", "?")
        group = f"{model}@{day}"
        rows.append({
            "run_id": summ["run_id"],
            "label": DOC71.get(summ["run_id"], summ.get("name", "")),
            "group": group,
            "units": summ.get("units_processed"),
            "dropped": summ.get("units_dropped"),
            "fps_eff_summary": summ.get("fps_effective"),
            **s,
        })
        groups.setdefault(group, []).extend(gaps)

    if not rows:
        print("No se encontró ninguna corrida live (source_type=oak_d) con gaps.")
        return 1

    hdr = (f"{'corrida':<44} {'grupo':<24} {'proc':>5} {'drop':>5} "
           f"{'fps_eq':>6} {'gap_med':>8} {'CV':>6} {'p95':>8} {'max':>8} {'frac_reg':>8}")
    print(hdr)
    print("-" * len(hdr))
    for r in rows:
        name = r["label"] or r["run_id"].rsplit("_", 1)[-1]
        print(f"{name:<44} {r['group']:<24} {r['units'] or '?':>5} "
              f"{r['dropped'] if r['dropped'] is not None else '?':>5} "
              f"{r['fps_eq']:>6} {r['median_ms']:>7}m {r['cv']:>6} "
              f"{r['p95_ms']:>7}m {r['max_ms']:>7}m {r['frac_near_regular']:>8}")

    print("\n=== agregado por grupo (huecos agrupados) ===")
    agg = {}
    for g, gaps in sorted(groups.items()):
        s = stats(gaps)
        agg[g] = s
        print(f"{g:<28} n={s['n_gaps']:>5}  media={s['mean_ms']:>7.1f} ms "
              f"(~{s['mean_gap_frames30']:>5.2f} frames@30, {s['fps_eq']} fps)  "
              f"CV={s['cv']}  p5={s['p5_ms']} p95={s['p95_ms']} max={s['max_ms']}  "
              f"frac_reg={s['frac_near_regular']}")

    OUT.write_text(json.dumps({
        "descripcion": "Huecos (ms) entre frames procesados consecutivos en corridas "
                       "live oak_d, por grupo modelo@jornada. Fuente: "
                       "e-ovrt_media-plane/runs/*/detections.jsonl "
                       "(source.timestamp_ms). Generado por "
                       "101-descarte-live-irregularidad.py.",
        "frame_ms_30fps": FRAME_MS,
        "por_corrida": rows,
        "agregado": agg,
        "gaps_ms_por_grupo": {g: [round(x, 2) for x in v] for g, v in groups.items()},
    }, indent=1))
    print(f"\n-> {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
