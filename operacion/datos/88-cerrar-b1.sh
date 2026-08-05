#!/bin/bash
# Cierre de la campaña B1 (bare_head como evidencia directa). Agrega las DOS variantes
# que comparten detecciones: `barehead` (la que se reporta) y `eind` (control interno,
# mismo caption). Idempotente.
set -euo pipefail

DATOS=/home/simonll4/projects/docs/operacion/datos/88-b1-barehead-clips
DS=/home/simonll4/projects/e-ovrt_datasets
RES=/home/simonll4/projects/e-ovrt_experimental-setup/results/clip_bench
DEST=$RES/b1_gdinobase560_barehead_scene

for v in barehead eind; do
  n=$(ls "$DATOS/$v"/eval_*.json 2>/dev/null | wc -l)
  echo "[B1] $v: $n/34 evals"
  [ "$n" -eq 34 ] || { echo "[B1] ABORTA: $v incompleto. Reanudar con 88-ciclo-barehead-runner.py"; exit 1; }
done

cd "$DS"
python3 datasets/scripts/bench/aggregate_clip_campaign.py \
  --evals-dir "$DATOS/barehead" --gt-dir datasets-videos/gt \
  --campaign "$DEST/campaign.yaml" --out "$DEST/metrics.json"

echo; echo "===== control interno: E-IND bajo el MISMO caption de 4 clases ====="
python3 datasets/scripts/bench/aggregate_clip_campaign.py \
  --evals-dir "$DATOS/eind" --gt-dir datasets-videos/gt \
  --out "$DEST/metrics_eind_mismo_caption.json"

mkdir -p "$DEST/evals"
cp "$DATOS/barehead"/eval_*.json "$DEST/evals/"
cp "$DATOS/resultados.json" "$DEST/provenance.json"
echo "[B1] artefactos en $DEST"
