"""Regenera el `provenance.json` de las campañas I1/I2 (estrato B) a la gen. 3.

POR QUÉ EXISTE
--------------
Los `provenance.json` de `i1`/`i2` quedaron con **4 entradas** —las corridas de la
gen. 2 (2026-08-07)— mientras que su `metrics.json` y sus `evals/` son de la **gen. 3**
(13 clips, 2026-08-09, re-evaluados tras la revisión ciega del GT del doc 113 §B).
Es el mismo modo de falla que el del `gt_manifest_yaml_sha256`: la campaña se re-corrió
y se re-evaluó, pero el artefacto de procedencia no se regeneró, así que declaraba
menos corridas de las que sostienen las cifras publicadas. El doc `operacion/111`
lo listaba entre los artefactos del cierre como si estuviera completo.

QUÉ RECUPERA, Y QUÉ NO
----------------------
- `clip_id`, `media_run_id` -> de `110-estrato-b-gen3/runs-map-estratob.json` (los 13).
- `frames`                  -> de `summary.json/units_processed` del run del media-plane.
- `eval`                    -> del `evals/eval_<clip>.json` archivado (post-revisión).
- `seconds`                 -> **null, con causa declarada**: era el wall-clock que medía
  el runner en el momento (`round(dt, 1)`), no un dato derivable de los artefactos.
  Se prefiere `null` explícito antes que inventar una duración plausible.

I2 no corre GPU (reusa las detecciones de I1), así que su `media_run_id` es `null` por
diseño, igual que en el archivo anterior — y se declara con `media_run_id_note`.

Uso:  python3 docs/operacion/datos/113-regenerar-provenance-estrato-b.py [--check]
      --check no escribe: solo reporta si los archivos en disco están al día.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

RAIZ = Path("/home/simonll4/projects")
RES = RAIZ / "e-ovrt_experimental-setup/results/clip_bench"
NIVEL_A = RAIZ / "e-ovrt_experimental-setup/results/bench_nivel_a"
RUNS_MAP = RAIZ / "docs/operacion/datos/110-estrato-b-gen3/runs-map-estratob.json"
RUNS_MAP_NA = RAIZ / "docs/operacion/datos/110-estrato-b-gen3/runs-map-consolidado.json"
MEDIA_RUNS = RAIZ / "e-ovrt_media-plane/runs"
NA1 = "na1_gdinotiny560_v2short_video"

CAMPANAS = {
    "i1_gdinotiny560_v2short_scene_internet": True,    # corre GPU: lleva media_run_id
    "i2_gdinotiny560_v2short_subject_internet": False,  # reusa las detecciones de I1
}

SECONDS_NOTE = (
    "null: el wall-clock por clip lo medía el runner en el momento y no es derivable "
    "de los artefactos; se declara ausente en vez de estimarlo (regeneración 2026-08-09)"
)
RUN_ID_NOTE = (
    "null por diseño: esta campaña no corre inferencia, reusa las detecciones de I1 "
    "(misma granularidad de detección, distinta granularidad del motor)"
)


def frames_de(run_id: str) -> int | None:
    summary = MEDIA_RUNS / run_id / "summary.json"
    if not summary.exists():
        return None
    return json.loads(summary.read_text()).get("units_processed")


def construir(campana: str, con_gpu: bool) -> list[dict]:
    runs = json.loads(RUNS_MAP.read_text())
    filas = []
    for clip_id in sorted(runs):
        eval_p = RES / campana / "evals" / f"eval_{clip_id}.json"
        if not eval_p.exists():
            raise SystemExit(f"falta el eval archivado: {eval_p}")
        run_id = runs[clip_id]
        fila = {
            "clip_id": clip_id,
            "eval": json.loads(eval_p.read_text()),
            "seconds": None,
            "seconds_note": SECONDS_NOTE,
            "media_run_id": run_id if con_gpu else None,
            "frames": frames_de(run_id),
        }
        if not con_gpu:
            fila["media_run_id_note"] = RUN_ID_NOTE
            fila["detections_from"] = run_id
        filas.append(fila)
    return filas


def construir_na1() -> list[dict]:
    """Nivel A sobre video: no hay `eval` por clip (no interviene el motor temporal).

    La unidad de procedencia es la corrida del media-plane que produjo las detecciones
    puntuadas; el detalle por clip ya vive embebido en `metrics.json/por_clip`.
    """
    runs = json.loads(RUNS_MAP_NA.read_text())
    metrics = json.loads((NIVEL_A / NA1 / "metrics.json").read_text())
    filas = []
    for c in sorted(metrics["por_clip"], key=lambda x: x["clip_id"]):
        clip_id = c["clip_id"]
        if clip_id not in runs:
            raise SystemExit(f"{clip_id} no está en {RUNS_MAP_NA.name}")
        run_id = runs[clip_id]
        filas.append({
            "clip_id": clip_id,
            "media_run_id": run_id,
            "frames_puntuados": c["frames_puntuados"],
            "stride": c["stride"],
            "frames": frames_de(run_id),
        })
    return filas


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="no escribe; sale 1 si algún provenance.json está desactualizado")
    args = ap.parse_args()

    objetivos = [(RES / c / "provenance.json", lambda c=c, g=g: construir(c, g), c)
                 for c, g in CAMPANAS.items()]
    objetivos.append((NIVEL_A / NA1 / "provenance.json", construir_na1, NA1))

    desactualizados = 0
    for destino, constructor, campana in objetivos:
        nuevo = constructor()
        actual = json.loads(destino.read_text()) if destino.exists() else None

        if actual == nuevo:
            print(f"  ok   {campana[:44]:44} {len(nuevo)} clips, al día")
            continue

        n_antes = len(actual) if actual else 0
        desactualizados += 1
        if args.check:
            print(f"  DESACTUALIZADO  {campana[:38]:38} disco {n_antes} clips "
                  f"| esperado {len(nuevo)}")
            continue

        destino.write_text(json.dumps(nuevo, ensure_ascii=False, indent=2) + "\n")
        sin_frames = [f["clip_id"] for f in nuevo if f["frames"] is None]
        print(f"  ESCRITO  {campana[:40]:40} {n_antes} -> {len(nuevo)} clips"
              + (f" (sin frames: {sin_frames})" if sin_frames else ""))

    if args.check and desactualizados:
        print(f"\n⚠️  {desactualizados} provenance.json desactualizados "
              f"(correr sin --check para regenerar)")
        return 1
    print("\n✅ provenance del estrato B al día")
    return 0


if __name__ == "__main__":
    sys.exit(main())
