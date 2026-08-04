#!/bin/bash
# Cierre de la campaña D1 (Fase 2 E-DIR, Nivel B): agrega, copia artefactos a la
# vista comparable y deja los números listos para la fila de results/clip_bench.
# Idempotente: se puede correr de nuevo sin romper nada.
set -euo pipefail

DATOS=/home/simonll4/projects/docs/operacion/datos/85-d1-edir-clips
DS=/home/simonll4/projects/e-ovrt_datasets
DEST=/home/simonll4/projects/e-ovrt_experimental-setup/results/clip_bench/d1_gdinotiny560_edirpair_scene

n=$(ls "$DATOS"/eval_*.json 2>/dev/null | wc -l)
echo "[D1] evals encontrados: $n/34"
if [ "$n" -ne 34 ]; then
  echo "[D1] ABORTA: la campaña no está completa. Reanudar con 85-ciclo-edir-runner.py"
  exit 1
fi

cd "$DS"
python3 datasets/scripts/bench/aggregate_clip_campaign.py \
  --evals-dir "$DATOS" \
  --gt-dir    datasets-videos/gt \
  --campaign  "$DEST/campaign.yaml" \
  --out       "$DEST/metrics.json"

mkdir -p "$DEST/evals"
cp "$DATOS"/eval_*.json "$DEST/evals/"
cp "$DATOS"/resultados.json "$DEST/provenance.json"
echo "[D1] artefactos en $DEST"
