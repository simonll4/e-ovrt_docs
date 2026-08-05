"""Contraste del costo del tiempo real: densidad de evidencia vs rendimiento.

Lee los `metrics.json` de las campañas de referencia (T1 escena / G1 sujeto, ambas
stride 1 = 30 fps) y los de las campañas de densidad reducida, y arma la tabla que
va al informe. No recalcula nada: solo alinea campos del MISMO schema
(`clip_campaign_metrics.v1`) para que el contraste sea leer archivos y no rehacer
aritmética a mano (la trampa que el doc 81 §3 documenta).

Uso: 96-contraste-tiempo-real.py
"""
import json
import sys
from pathlib import Path

RES = Path("/home/simonll4/projects/e-ovrt_experimental-setup/results/clip_bench")
DATOS = Path(__file__).parent

# (etiqueta, ruta de metrics.json, stride, granularidad)
FILAS = [
    ("T1  escena", RES / "t1_gdinotiny560_v2short_scene/metrics.json", 1, "scene"),
    ("R1  escena", RES / "r1_gdinotiny560_v2short_scene_s7/metrics.json", 7, "scene"),
    ("R3  escena", RES / "r3_gdinotiny560_v2short_scene_s15/metrics.json", 15, "scene"),
    ("R5  escena", RES / "r5_gdinotiny560_v2short_scene_s26/metrics.json", 26, "scene"),
    ("G1  sujeto", RES / "g1_gdinotiny560_v2short_subject/metrics.json", 1, "subject"),
    ("R2  sujeto", RES / "r2_gdinotiny560_v2short_subject_s7/metrics.json", 7, "subject"),
    ("R4  sujeto", RES / "r4_gdinotiny560_v2short_subject_s15/metrics.json", 15, "subject"),
    ("R6  sujeto", RES / "r6_gdinotiny560_v2short_subject_s26/metrics.json", 26, "subject"),
]


def f(v, p=3):
    return "—" if v is None else f"{v:.{p}f}".replace(".", ",")


def ms(v):
    return "—" if v is None else f"{v:,.0f}".replace(",", ".")


def main():
    filas = []
    for etiqueta, path, stride, gran in FILAS:
        if not path.exists():
            print(f"(falta {path} — se omite {etiqueta})", file=sys.stderr)
            continue
        m = json.loads(path.read_text())
        p, n = m["positives"], m["negatives"]
        filas.append({
            "etiqueta": etiqueta, "stride": stride, "gran": gran,
            "fps": 30.0 / stride,
            "recall": p["recall_micro"], "prec": p["precision_micro"],
            "f1": p["f1_micro"], "t_alert": p["t_alert_system_ms"],
            "ttfd": p["ttfd_ms"], "sdr": p["sdr"],
            "matched": p["matched"], "missed": p["missed"],
            "fp_pos": p["false_positives"], "fp_neg": n["false_positives"],
            "neg_clips": n["clips"],
        })

    print("\n| campaña | stride | fps ev. | recall | prec. | F1 | t_alert | TTFD | SDR | FP neg |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    for r in filas:
        print(f"| {r['etiqueta']} | {r['stride']} | {r['fps']:.2f}".replace(".", ",")
              + f" | {f(r['recall'])} | {f(r['prec'])} | **{f(r['f1'])}** "
                f"| {ms(r['t_alert'])} ms | {ms(r['ttfd'])} ms | {f(r['sdr'])} "
                f"| {r['fp_neg']}/{r['neg_clips']} |")

    # Deltas contra la referencia de cada granularidad (stride 1)
    print("\n### Costo del tiempo real (delta contra stride 1 de la misma granularidad)\n")
    print("| campaña | ΔF1 | Δrecall | Δprec. | ΔSDR | ΔTTFD | matched | missed |")
    print("|---|---|---|---|---|---|---|---|")
    for gran in ("scene", "subject"):
        base = next((r for r in filas if r["gran"] == gran and r["stride"] == 1), None)
        if not base:
            continue
        for r in [x for x in filas if x["gran"] == gran]:
            if r["stride"] == 1:
                print(f"| {r['etiqueta']} (referencia) | — | — | — | — | — "
                      f"| {r['matched']} | {r['missed']} |")
                continue
            d = lambda k, p=3: ("%+.*f" % (p, r[k] - base[k])).replace(".", ",")  # noqa: E731
            print(f"| {r['etiqueta']} | **{d('f1')}** | {d('recall')} | {d('prec')} "
                  f"| {d('sdr')} | {('%+.0f' % (r['ttfd'] - base['ttfd']))} ms "
                  f"| {r['matched']} | {r['missed']} |")

    out = DATOS / "96-contraste-tiempo-real.json"
    out.write_text(json.dumps(filas, indent=2, ensure_ascii=False))
    print(f"\n-> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
