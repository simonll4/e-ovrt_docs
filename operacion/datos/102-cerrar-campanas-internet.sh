#!/bin/bash
# Cierre de las campañas I1 (scene) e I2 (subject) del estrato B — lote de
# internet. Agrega con las reglas con test (negativos fuera de P/R/F1, episodios
# censurados fuera del denominador, re_alerts que no son FP, desglose por
# escenario) y deja los artefactos con la convención del banco. Idempotente.
#
# Correr DESPUÉS de:
#   102-ciclo-internet-runner.py --fase scene
#   102-ciclo-internet-runner.py --fase subject
set -euo pipefail

DATOS=/home/simonll4/projects/docs/operacion/datos
DS=/home/simonll4/projects/e-ovrt_datasets
RES=/home/simonll4/projects/e-ovrt_experimental-setup/results/clip_bench
N_ESPERADO=3   # v04_c01, v06_c01, v10_c01

cerrar () {
  local codigo="$1" fase="$2" dest="$3"
  local src="$DATOS/102-${codigo,,}-internet-${fase}-clips"
  local n
  n=$(ls "$src"/eval_*.json 2>/dev/null | wc -l)
  echo "[$codigo] $fase: $n/$N_ESPERADO evals"
  [ "$n" -eq "$N_ESPERADO" ] || {
    echo "[$codigo] ABORTA: incompleto. Reanudar con 102-ciclo-internet-runner.py --fase $fase"
    exit 1
  }

  cd "$DS"
  python3 datasets/scripts/bench/aggregate_clip_campaign.py \
    --evals-dir "$src" --gt-dir datasets-videos/gt \
    --campaign "$RES/$dest/campaign.yaml" --out "$RES/$dest/metrics.json"

  mkdir -p "$RES/$dest/evals"
  cp "$src"/eval_*.json "$RES/$dest/evals/"
  cp "$src/resultados.json" "$RES/$dest/provenance.json"
  echo "[$codigo] artefactos en $RES/$dest"
  echo
}

cerrar I1 scene   i1_gdinotiny560_v2short_scene_internet
cerrar I2 subject i2_gdinotiny560_v2short_subject_internet

echo "Falta a mano: la fila nueva en $RES/index.md (estrato B, con desglose — L5/D-90.6),"
echo "y completar date/duration_note/report_doc en los dos campaign.yaml."
