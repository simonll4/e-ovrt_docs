"""Contraste del decimado empírico (doc 101): ¿el jitter cambia las conclusiones?

Lee los metrics.json/evals de las variantes 101 (j7/s12/j12 × escena/sujeto) y de
las referencias del doc 96 (R1/R2, decimado regular stride 7), y responde tres
preguntas con bootstrap pareado por clip (mismo método y semilla-fija que
`96-critica-verificacion.py`):

  1. EFECTO DEL JITTER a la densidad de HOY (4,1-4,3 fps): j7 − R1 (escena) y
     j7subj − R2 (sujeto). Si el IC cruza el cero, el decimado regular de R1-R6
     es proxy válido del descarte irregular del live a esa densidad.
  2. EFECTO DEL JITTER a la densidad del RODAJE (2,5 fps, CV 0,357): j12 − s12,
     en ambas granularidades (control regular propio, misma densidad media).
  3. F-96.4 BAJO JITTER: ¿la ganancia de la identidad (sujeto − escena) sigue
     excluyendo el cero con muestreo irregular? (la conclusión central del eje)

Además: fragmentación de tracks (j7 vs R2), FP en negativos por variante, y
t_alert entre supervivientes comunes (la lección F-96.5: sin control de
supervivencia el promedio miente).

Uso: 101-decimado-empirico-contraste.py
"""

import json
import random
import sys
from pathlib import Path

DATOS = Path(__file__).parent
RES = Path("/home/simonll4/projects/e-ovrt_experimental-setup/results/clip_bench")

CAMP = {
    "R1 (regular s7)": RES / "r1_gdinotiny560_v2short_scene_s7",
    "j7 (jitter 08-05)": DATOS / "101-rt-j7",
    "s12 (regular 12)": DATOS / "101-rt-s12",
    "j12 (jitter rodaje)": DATOS / "101-rt-j12",
    "R2 subj (regular s7)": RES / "r2_gdinotiny560_v2short_subject_s7",
    "j7 subj": DATOS / "101-rt-j7-subject",
    "s12 subj": DATOS / "101-rt-s12-subject",
    "j12 subj": DATOS / "101-rt-j12-subject",
}

N_BOOT = 10_000
SEED = 101


def cargar_dir(base: Path) -> dict:
    evdir = base / "evals" if (base / "evals").exists() else base
    out = {}
    for p in sorted(evdir.glob("eval_*.json")):
        e = json.loads(p.read_text())
        cid = e.get("scenario_id") or p.stem.replace("eval_", "")
        out[cid] = {
            "matched": e["matched_alerts_count"],
            "missed": e["missed_alerts_count"],
            "fp": e["unexpected_alerts_count"],
            "t_alert": e.get("avg_latency_ms_from_episode_start"),
            "aplicable": e.get("applicability_state") == "computed",
        }
    return out


def cargar(nombre: str) -> dict:
    return cargar_dir(CAMP[nombre])


def f1_micro(rows):
    m = sum(r["matched"] for r in rows)
    mi = sum(r["missed"] for r in rows)
    fp = sum(r["fp"] for r in rows)
    if m + mi == 0 or 2 * m + mi + fp == 0:
        return None
    return 2 * m / (2 * m + mi + fp)


def boot_delta(a, b, clips):
    """ΔF1 (b−a) observado, IC 95% pareado por clip, P(Δ<=0)."""
    rng = random.Random(SEED)
    obs = f1_micro([b[c] for c in clips]) - f1_micro([a[c] for c in clips])
    deltas = []
    for _ in range(N_BOOT):
        s = [clips[rng.randrange(len(clips))] for _ in clips]
        fa, fb = f1_micro([a[c] for c in s]), f1_micro([b[c] for c in s])
        if fa is not None and fb is not None:
            deltas.append(fb - fa)
    deltas.sort()
    return (obs, deltas[int(0.025 * len(deltas))],
            deltas[int(0.975 * len(deltas))],
            sum(1 for d in deltas if d <= 0) / len(deltas))


def fmt(x, p=3):
    return f"{x:+.{p}f}".replace(".", ",")


def metrics_de(nombre):
    m = json.loads((CAMP[nombre] / "metrics.json").read_text())
    p, n = m["positives"], m["negatives"]
    return p, n


def main():
    faltan = [k for k, v in CAMP.items()
              if not (v / "metrics.json").exists() and not (v / "evals").exists()]
    if faltan:
        print(f"Faltan campañas: {faltan}")
        return 2

    data = {k: cargar(k) for k in CAMP}
    clips = sorted(set.intersection(*(set(v) for v in data.values())))
    # solo clips aplicables en todas (los 4 negativos quedan fuera de F1, como siempre)
    aplicables = [c for c in clips if all(data[k][c]["aplicable"] for k in data)]
    print(f"{len(clips)} clips comunes, {len(aplicables)} aplicables (positivos)\n")

    print("| variante | fps ev. | muestreo | recall | prec. | F1 | FP neg |")
    print("|---|---|---|---|---|---|---|")
    for nombre, fps, muestreo in [
        ("R1 (regular s7)", "4,29", "regular"),
        ("j7 (jitter 08-05)", "4,23", "empírico CV 0,22"),
        ("s12 (regular 12)", "2,52", "regular"),
        ("j12 (jitter rodaje)", "2,53", "empírico CV 0,36"),
        ("R2 subj (regular s7)", "4,29", "regular"),
        ("j7 subj", "4,23", "empírico CV 0,22"),
        ("s12 subj", "2,52", "regular"),
        ("j12 subj", "2,53", "empírico CV 0,36"),
    ]:
        p, n = metrics_de(nombre)
        print(f"| {nombre} | {fps} | {muestreo} | {p['recall_micro']:.3f} "
              f"| {p['precision_micro']:.3f} | **{p['f1_micro']:.3f}** "
              f"| {n['false_positives']}/{n['clips']} |".replace(".", ","))

    print("\n### 1-2. Efecto del jitter (bootstrap pareado, 10k, semilla 101)\n")
    print("| contraste | ΔF1 obs | IC 95% | P(Δ<=0) |")
    print("|---|---|---|---|")
    pares = [
        ("j7 − R1 (escena, hoy)", "R1 (regular s7)", "j7 (jitter 08-05)"),
        ("j7subj − R2 (sujeto, hoy)", "R2 subj (regular s7)", "j7 subj"),
        ("j12 − s12 (escena, rodaje)", "s12 (regular 12)", "j12 (jitter rodaje)"),
        ("j12subj − s12subj (sujeto, rodaje)", "s12 subj", "j12 subj"),
    ]
    for etiqueta, a, b in pares:
        obs, lo, hi, p0 = boot_delta(data[a], data[b], aplicables)
        cruza = "cruza el 0" if lo <= 0 <= hi else "EXCLUYE el 0"
        print(f"| {etiqueta} | {fmt(obs)} | [{fmt(lo)}, {fmt(hi)}] ({cruza}) | {p0:.3f} |")

    print("\n### 3. F-96.4 bajo jitter: ganancia de la identidad (sujeto − escena)\n")
    print("| densidad | muestreo | Δ obs | IC 95% |")
    print("|---|---|---|---|")
    for etiqueta, muestreo, esc, subj in [
        ("4,29 fps", "regular (=R2−R1, doc 96)", "R1 (regular s7)", "R2 subj (regular s7)"),
        ("4,23 fps", "empírico seed 101", "j7 (jitter 08-05)", "j7 subj"),
        ("2,52 fps", "regular (control nuevo)", "s12 (regular 12)", "s12 subj"),
        ("2,53 fps", "empírico seed 101", "j12 (jitter rodaje)", "j12 subj"),
    ]:
        obs, lo, hi, _ = boot_delta(data[esc], data[subj], aplicables)
        v = "EXCLUYE el 0" if lo > 0 else "cruza el 0"
        print(f"| {etiqueta} | {muestreo} | {fmt(obs)} | [{fmt(lo)}, {fmt(hi)}] ({v}) |")

    # robustez multi-semilla: mismas comparaciones con las semillas extra que existan
    seeds_extra = sorted({p.name.split("-seed")[1].split("-")[0]
                          for p in DATOS.glob("101-rt-j7-seed*")})
    if seeds_extra:
        print("\n### 3b. Robustez multi-semilla (identidad y efecto del jitter)\n")
        print("| semilla | j7: Δident | j12: Δident | j7−R1 | j12−s12 |")
        print("|---|---|---|---|---|")
        for s in ["101"] + seeds_extra:
            suf = "" if s == "101" else f"-seed{s}"
            dj7 = cargar_dir(DATOS / f"101-rt-j7{suf}")
            dj7s = cargar_dir(DATOS / f"101-rt-j7{suf}-subject")
            dj12 = cargar_dir(DATOS / f"101-rt-j12{suf}")
            dj12s = cargar_dir(DATOS / f"101-rt-j12{suf}-subject")
            i7 = boot_delta(dj7, dj7s, aplicables)
            i12 = boot_delta(dj12, dj12s, aplicables)
            e7 = boot_delta(data["R1 (regular s7)"], dj7, aplicables)
            e12 = boot_delta(data["s12 (regular 12)"], dj12, aplicables)
            cell = lambda r: f"{fmt(r[0])} [{fmt(r[1])},{fmt(r[2])}]"  # noqa: E731
            print(f"| {s} | {cell(i7)} | {cell(i12)} | {cell(e7)} | {cell(e12)} |")

    # t_alert entre supervivientes comunes (control de supervivencia, F-96.5)
    print("\n### t_alert entre supervivientes comunes (j7 vs R1)\n")
    a, b = data["R1 (regular s7)"], data["j7 (jitter 08-05)"]
    comunes = [c for c in aplicables
               if a[c]["matched"] == b[c]["matched"] and a[c]["matched"] > 0
               and a[c]["t_alert"] and b[c]["t_alert"]]
    if comunes:
        ta = sum(a[c]["t_alert"] for c in comunes) / len(comunes)
        tb = sum(b[c]["t_alert"] for c in comunes) / len(comunes)
        print(f"{len(comunes)} clips con matched igual y >0: "
              f"R1 {ta:,.0f} ms vs j7 {tb:,.0f} ms (Δ {tb - ta:+,.0f} ms)")

    # fragmentación de tracks: j7 vs R2 (desde resultados.json)
    print("\n### Tracks (fragmentación de identidad)\n")
    for nombre, d in [("R2 (regular s7)", DATOS / "96-rt-stride7-subject"),
                      ("j7 subj", DATOS / "101-rt-j7-subject"),
                      ("j12 subj", DATOS / "101-rt-j12-subject")]:
        rj = d / "resultados.json"
        if rj.exists():
            rows = [r for r in json.loads(rj.read_text()) if "tracks" in r]
            print(f"{nombre}: {sum(r['tracks'] for r in rows)} tracks "
                  f"en {len(rows)} clips")

    out = DATOS / "101-decimado-empirico-contraste.json"
    resumen = {}
    for etiqueta, a, b in pares:
        obs, lo, hi, p0 = boot_delta(data[a], data[b], aplicables)
        resumen[etiqueta] = {"delta_f1": obs, "ic95": [lo, hi], "p_le0": p0}
    for etiqueta, esc, subj in [("identidad@hoy_jitter", "j7 (jitter 08-05)", "j7 subj"),
                                ("identidad@rodaje_jitter", "j12 (jitter rodaje)", "j12 subj")]:
        obs, lo, hi, p0 = boot_delta(data[esc], data[subj], aplicables)
        resumen[etiqueta] = {"delta_f1": obs, "ic95": [lo, hi], "p_le0": p0}
    out.write_text(json.dumps(resumen, indent=2, ensure_ascii=False))
    print(f"\n-> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
