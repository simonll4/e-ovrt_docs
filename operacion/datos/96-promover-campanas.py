"""Promueve las campañas de tiempo real a `results/clip_bench/` y las agrega.

Por cada densidad × granularidad: crea el directorio de campaña con la
convención del banco (`campaign.yaml` + `evals/` + `provenance.json` +
`metrics.json`) y corre `aggregate_clip_campaign.py`, que es el que aplica las
reglas de agregación con test (negativos fuera de P/R/F1, episodios censurados
fuera del denominador, `re_alerts` que no son FP, desglose por escenario).

Uso: 96-promover-campanas.py
"""
import json
import shutil
import subprocess
import sys
from pathlib import Path

DATOS = Path(__file__).parent
DS = Path("/home/simonll4/projects/e-ovrt_datasets")
RES = Path("/home/simonll4/projects/e-ovrt_experimental-setup/results/clip_bench")
AGG = DS / "datasets/scripts/bench/aggregate_clip_campaign.py"
GT_DIR = DS / "datasets-videos/gt"

FROZEN = "df81fd48b6daf8924b5fb66aa1ce4acc0c880ac6ed8cd1245c6aca1babdb309a"
MANIFEST_SHA = "cef5082e1eb1981c89251ba1b45d7ff044627f8aa1e428f50e0601abe64260e8"

# (código, stride, granularidad, campaña de referencia con stride 1)
PLAN = [
    ("R1", 7, "scene", "t1_gdinotiny560_v2short_scene"),
    ("R2", 7, "subject", "g1_gdinotiny560_v2short_subject"),
    ("R3", 15, "scene", "t1_gdinotiny560_v2short_scene"),
    ("R4", 15, "subject", "g1_gdinotiny560_v2short_subject"),
    ("R5", 26, "scene", "t1_gdinotiny560_v2short_scene"),
    ("R6", 26, "subject", "g1_gdinotiny560_v2short_subject"),
]

# Anclas medidas del camino live, para justificar cada densidad (docs 71/73).
ANCLA = {
    7: ("4,29 fps", "el TECHO de esta máquina hoy: 3,75-4,42 fps con gdino-tiny "
                    "tras la palanca F-RT5 (doc 73)"),
    15: ("2,00 fps", "el rango que EFECTIVAMENTE corrió en vivo durante el rodaje: "
                     "1,16-2,62 fps, 92-94% de frames descartados (doc 71 §2.1)"),
    26: ("1,15 fps", "el PEOR caso medido en vivo: 1,16 fps a las 20:10 del rodaje, "
                     "tras la degradación térmica de 2,4x a lo largo de la jornada "
                     "(doc 71 §4)"),
}


def campaign_yaml(codigo, stride, gran, ref, n_ok, minutos):
    fps, ancla = ANCLA[stride]
    subject = gran == "subject"
    return f"""schema_version: clip_campaign.v1
campaign_id: {campaign_id(codigo, stride, gran)}
date: '2026-08-05'
phase: R
description: >
  El costo del tiempo real ({codigo}). Las seis campañas previas del banco corrieron
  todas `stride: 1` — 30 inferencias por segundo de video — pero el camino live no
  puede sostener esa densidad: durante el rodaje GDINO rindió 1,16-2,62 fps con
  92-94% de frames descartados (doc 71) y el techo de esta máquina tras F-RT5 es
  3,75-4,42 fps (doc 73). O sea que todo el resultado del banco se midió con ~7 a
  25x más evidencia por segundo de la que el tiempo real entrega, y cuánto de ese
  rendimiento sobrevive a la restricción no estaba medido.

  Esta campaña lo mide a densidad {fps}, que es {ancla}.

# --- LA COMBINACIÓN ---
model: grounding-dino/gdino-tiny-560
model_note: 'Idéntico a {ref}. Campeón S1/S2 (doc 64).'
prompt_set: cr01_cr02_v2_short
prompt_set_frozen_sha256: {FROZEN}
prompt_set_note: 'Idéntico a {ref}.'
pattern_set: {'cr01_cr02_v2_subject' if subject else 'cr01_cr02_v2'}
pattern_set_note: 'Idéntico a {ref}. Mismos timings 4000/7000.'
granularity: {gran}
granularity_note: >
  {'G1 — track_id post-hoc con SimpleIoUTracker sobre las detecciones de esta misma densidad. OJO: el tracker asocia por IoU entre frames consecutivos, y acá los frames están a ' + str(round(1000 / (30 / stride))) + ' ms en vez de 33 ms. La degradación de la identidad es PARTE del costo del tiempo real que se está midiendo, no un defecto del montaje.' if subject else 'G0 — sin track_id; el motor acumula ausencia a nivel escena.'}
path: DBE
stride: {stride}
path_note: >
  Camino DBE por archivo, pero con la DENSIDAD DE EVIDENCIA del camino live. La
  variable única contra {ref} es el stride; modelo, prompts, patrones, GT y
  evaluador son los mismos.

  Qué mide y qué NO: mide el efecto de ver menos frames por segundo sobre la
  percepción y sobre el motor temporal. NO mide latencia operativa ni integridad
  del bus — eso vive en los humos EBE (docs 65/67/91) y en la caracterización de
  fps (docs 73/74). El decimado es regular; el descarte live es irregular
  (jitter), diferencia declarada.

# --- GUARD ---
guard_note: >
  Si el stride no se aplicara, la campaña mediría {ref} creyendo medir tiempo real
  y el error no se vería en ningún lado (la lección del `no_track_id` de G1). Se
  verifica por clip y por partida doble: `run_descriptor.rate_control.stride` de la
  corrida declara el stride que rigió, y el conteo de unidades procesadas lo
  confirma independientemente contra ceil(n_frames/stride). {n_ok}/34 pasaron.
{'' if not subject else '''
  Además, el guard de identidad de G1: si una persona quedara sin `track_id`, el
  motor degrada a escena en silencio y esto mediría G0.
'''}
# --- COMPARABILIDAD ---
comparabilidad_note: >
  Las referencias (T1 08-03, G1 08-04) se evaluaron con el control-plane de esas
  fechas, y después vino `5327080` (08-04 16:38), que cambió el despacho de
  evaluadores y toca `_positive_flags_for_source` — el que deriva SDR/TTFD.
  Contrastar contra números producidos por otro evaluador mezclaría densidad de
  evidencia con versión del código. VERIFICADO que no: re-correr replay +
  evaluate-alerts con el código de hoy sobre las mismas detecciones de T1
  reprodujo sus 34 evals **idénticos campo a campo**
  (`96-verificar-comparabilidad-t1.py`). La comparación es limpia.

# --- PROCEDENCIA ---
gt_bank: clip_bench (34 clips, Bloque A rodaje 2026-07-25)
gt_manifest_yaml_sha256: {MANIFEST_SHA}
gt_doc: docs/operacion/80-gt-rodaje-desde-cvat.md
evaluator_note: 'Mismo control-plane y mismo pattern set que {ref}.'
hardware: '{"CPU (tracking post-hoc + replay; sin GPU)" if subject else "NVIDIA RTX 4060 Laptop 8 GB (WSL2)"}'
duration_note: '{n_ok}/34 clips en {minutos}'

report_doc: docs/operacion/96-costo-tiempo-real.md
raw_evidence: docs/operacion/datos/96-rt-stride{stride}{'-subject' if subject else ''}/
"""


def campaign_id(codigo, stride, gran):
    return f"{codigo.lower()}_gdinotiny560_v2short_{gran}_s{stride}"


def main():
    hechas = []
    for codigo, stride, gran, ref in PLAN:
        src = DATOS / f"96-rt-stride{stride}{'-subject' if gran == 'subject' else ''}"
        res_json = src / "resultados.json"
        if not res_json.exists():
            print(f"(falta {res_json} — se omite {codigo})")
            continue
        rows = json.loads(res_json.read_text())
        ok = [r for r in rows if "eval" in r]
        if not ok:
            print(f"({codigo} sin evals — se omite)")
            continue
        segs = sum(r.get("seconds") or 0 for r in ok)
        minutos = f"{segs / 60:.1f} min" if segs else "CPU, < 1 min"

        dest = RES / campaign_id(codigo, stride, gran)
        (dest / "evals").mkdir(parents=True, exist_ok=True)
        for p in src.glob("eval_*.json"):
            shutil.copy2(p, dest / "evals" / p.name)
        (dest / "provenance.json").write_text(json.dumps(
            [{"clip_id": r["clip_id"], "media_run_id": r.get("media_run_id"),
              "stride": stride, "frames": r.get("frames"),
              "frames_totales": r.get("frames_totales")} for r in ok],
            indent=2, ensure_ascii=False))
        (dest / "campaign.yaml").write_text(
            campaign_yaml(codigo, stride, gran, ref, len(ok), minutos))

        r = subprocess.run(
            [sys.executable, str(AGG), "--evals-dir", str(dest / "evals"),
             "--gt-dir", str(GT_DIR), "--out", str(dest / "metrics.json"),
             "--campaign", str(dest / "campaign.yaml")],
            capture_output=True, text=True)
        if r.returncode != 0:
            print(f"{codigo}: AGREGACION FALLO\n{(r.stderr or r.stdout)[-500:]}")
            continue
        # copia para el script de contraste, que lee desde datos/
        shutil.copy2(dest / "metrics.json", src / "metrics.json")
        m = json.loads((dest / "metrics.json").read_text())["positives"]
        print(f"{codigo} s{stride} {gran:8} -> F1 {m['f1_micro']:.3f} "
              f"R {m['recall_micro']:.3f} P {m['precision_micro']:.3f} "
              f"SDR {m['sdr']:.3f}  ({len(ok)}/34)")
        hechas.append(campaign_id(codigo, stride, gran))

    print(f"\n{len(hechas)} campañas promovidas a {RES}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
