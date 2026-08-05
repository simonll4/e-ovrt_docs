"""Revisión adversarial del doc 96: ¿los hallazgos aguantan el escrutinio?

Tres verificaciones que un tribunal podría exigir y que el doc 96 v1 no traía:

1. RUIDO — bootstrap pareado por clip (cluster bootstrap, 10.000 resamples con
   semilla fija) para los deltas de F1 centrales. El apareo por clip es la
   unidad correcta: los episodios dentro de un clip están correlacionados, y
   las ocho campañas comparten exactamente los mismos 34 clips.
2. SUPERVIVENCIA en t_alert — F-96.5 dice "t_alert casi no se mueve". Pero el
   promedio de t_alert se calcula SOLO sobre episodios que alertaron: si a baja
   densidad los episodios lentos mueren (missed), el promedio puede quedarse
   quieto por composición, no por amortiguación. Se re-compara restringiendo a
   los clips donde ambas campañas igualaron matched (supervivientes comunes,
   aproximación declarada).
3. FRAGMENTACIÓN de tracks — el guard de G1 verifica que toda persona tenga
   track_id, NO que la identidad sea coherente en el tiempo. A stride 26 los
   frames están a ~867 ms y el tracker asocia por IoU entre consecutivos: si la
   identidad se fragmenta, cada fragmento debe sostener los 4 s por su cuenta.
   Se mide tracks-por-clip contra stride 1 (G1).

Uso: 96-critica-verificacion.py
"""
import json
import random
import sys
from pathlib import Path

RES = Path("/home/simonll4/projects/e-ovrt_experimental-setup/results/clip_bench")
DATOS = Path(__file__).parent

CAMP = {
    "T1": "t1_gdinotiny560_v2short_scene",
    "R1": "r1_gdinotiny560_v2short_scene_s7",
    "R3": "r3_gdinotiny560_v2short_scene_s15",
    "R5": "r5_gdinotiny560_v2short_scene_s26",
    "G1": "g1_gdinotiny560_v2short_subject",
    "R2": "r2_gdinotiny560_v2short_subject_s7",
    "R4": "r4_gdinotiny560_v2short_subject_s15",
    "R6": "r6_gdinotiny560_v2short_subject_s26",
}

N_BOOT = 10_000
SEED = 96  # fija: el resultado tiene que ser reproducible


def cargar(camp: str) -> dict:
    """clip_id -> (matched, missed, fp, re_alerts, t_alert_avg, aplicable)."""
    out = {}
    for p in sorted((RES / CAMP[camp] / "evals").glob("eval_*.json")):
        e = json.loads(p.read_text())
        cid = e.get("scenario_id") or p.stem.replace("eval_", "")
        aplicable = e.get("applicability_state") == "computed"
        out[cid] = {
            "matched": e["matched_alerts_count"],
            "missed": e["missed_alerts_count"],
            "fp": e["unexpected_alerts_count"],
            "t_alert": e.get("avg_latency_ms_from_episode_start"),
            "aplicable": aplicable,
        }
    return out


def f1_micro(rows) -> float | None:
    m = sum(r["matched"] for r in rows)
    mi = sum(r["missed"] for r in rows)
    fp = sum(r["fp"] for r in rows)
    if m + mi == 0 or 2 * m + mi + fp == 0:
        return None
    return 2 * m / (2 * m + mi + fp)


def boot_delta(a: dict, b: dict, clips: list[str]) -> tuple[float, float, float, float]:
    """ΔF1 (b−a) observado + IC 95% bootstrap pareado por clip + P(Δ<=0)."""
    rng = random.Random(SEED)
    obs = f1_micro([b[c] for c in clips]) - f1_micro([a[c] for c in clips])
    deltas = []
    for _ in range(N_BOOT):
        sample = [clips[rng.randrange(len(clips))] for _ in clips]
        fa, fb = f1_micro([a[c] for c in sample]), f1_micro([b[c] for c in sample])
        if fa is not None and fb is not None:
            deltas.append(fb - fa)
    deltas.sort()
    lo = deltas[int(0.025 * len(deltas))]
    hi = deltas[int(0.975 * len(deltas))]
    p_le0 = sum(1 for d in deltas if d <= 0) / len(deltas)
    return obs, lo, hi, p_le0


def main():
    data = {k: cargar(k) for k in CAMP}
    # solo clips positivos aplicables en TODAS las campañas (los 30 positivos)
    clips = sorted(c for c in data["T1"]
                   if all(data[k][c]["aplicable"] for k in CAMP))
    print(f"clips positivos apareados: {len(clips)}\n")

    print("## 1. Bootstrap pareado por clip (ΔF1, IC 95%, 10k resamples, semilla 96)\n")
    print("| contraste | ΔF1 obs. | IC 95% | P(Δ≤0) | ¿excluye 0? |")
    print("|---|---|---|---|---|")
    contrastes = [
        ("R1 − T1 (escena, 4,29 vs 30 fps)", "T1", "R1"),
        ("R3 − T1 (escena, 2,00 vs 30 fps)", "T1", "R3"),
        ("R5 − T1 (escena, 1,15 vs 30 fps)", "T1", "R5"),
        ("R2 − G1 (sujeto, 4,29 vs 30 fps)", "G1", "R2"),
        ("R4 − G1 (sujeto, 2,00 vs 30 fps)", "G1", "R4"),
        ("R6 − G1 (sujeto, 1,15 vs 30 fps)", "G1", "R6"),
        ("R2 − T1 (cruzada: sujeto@4,29 vs escena@30)", "T1", "R2"),
        # El eje que SÍ resulta significativo: granularidad a densidad fija.
        ("G1 − T1 (la de referencia del doc 89)", "T1", "G1"),
        ("R2 − R1 (sujeto vs escena, ambas 4,29 fps)", "R1", "R2"),
        ("R4 − R3 (sujeto vs escena, ambas 2 fps)", "R3", "R4"),
        ("R6 − R5 (sujeto vs escena, ambas 1,15 fps)", "R5", "R6"),
    ]
    resultados = {}
    for nombre, a, b in contrastes:
        obs, lo, hi, p = boot_delta(data[a], data[b], clips)
        resultados[nombre] = (obs, lo, hi, p)
        excl = "SÍ" if (lo > 0 or hi < 0) else "no"
        print(f"| {nombre} | {obs:+.3f} | [{lo:+.3f}, {hi:+.3f}] | {p:.3f} | {excl} |")

    print("\n## 2. Supervivencia en t_alert (F-96.5)\n")
    for a, b in [("T1", "R1"), ("T1", "R3"), ("T1", "R5")]:
        comunes = [c for c in clips
                   if data[a][c]["matched"] == data[b][c]["matched"]
                   and data[a][c]["matched"] > 0
                   and data[a][c]["t_alert"] and data[b][c]["t_alert"]]
        ta = sum(data[a][c]["t_alert"] for c in comunes) / len(comunes)
        tb = sum(data[b][c]["t_alert"] for c in comunes) / len(comunes)
        print(f"{a} vs {b}: {len(comunes)} clips con matched idéntico >0 — "
              f"t_alert {ta:.0f} -> {tb:.0f} ms (Δ {tb-ta:+.0f} ms)")

    print("\n## 3. Fragmentación de tracks por stride\n")
    fuentes = {
        1: DATOS.parent / "datos/89-g1-subject-clips/resultados.json",
        7: DATOS / "96-rt-stride7-subject/resultados.json",
        15: DATOS / "96-rt-stride15-subject/resultados.json",
        26: DATOS / "96-rt-stride26-subject/resultados.json",
    }
    print("| stride | gap entre frames | tracks totales | personas | dets/track (mediana por clip) |")
    print("|---|---|---|---|---|")
    frag = {}
    for s, path in fuentes.items():
        if not path.exists():
            print(f"| {s} | — | (falta {path.name}) | | |")
            continue
        rows = [r for r in json.loads(path.read_text()) if "eval" in r]
        tt = sum(r["tracks"] for r in rows)
        pp = sum(r["person_detections"] for r in rows)
        ratios = sorted(r["person_detections"] / r["tracks"]
                        for r in rows if r.get("tracks"))
        med = ratios[len(ratios) // 2]
        frag[s] = tt
        print(f"| {s} | {33*s} ms | {tt} | {pp} | {med:.1f} |")

    out = DATOS / "96-critica-verificacion.json"
    out.write_text(json.dumps({
        "bootstrap": {k: {"obs": v[0], "ic95": [v[1], v[2]], "p_le0": v[3]}
                      for k, v in resultados.items()},
        "tracks_totales_por_stride": frag,
        "n_boot": N_BOOT, "seed": SEED, "clips": len(clips),
    }, indent=2, ensure_ascii=False))
    print(f"\n-> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
