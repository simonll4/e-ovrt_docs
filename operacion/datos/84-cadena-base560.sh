#!/bin/bash
# Cadena nocturna gdino-base-560 (2026-08-04): dos campañas secuenciales sobre el
# MISMO servicio (el media-plane carga el modelo una vez, EOVRT_MODEL_REF).
#
#   1. Replica de la Fase D Nivel A (pre-registro nucleo/04 §7: "opcional repetir
#      con GDINO-base") -> ¿la debilidad de E-DIR con la negacion depende de la
#      capacidad del text encoder? base es ademas el especialista CR-01/bare_head
#      (doc 64), o sea el mejor caso posible para cr01_obs.
#   2. Campaña T2 del clip bench (doc 82 item 2): base-560 x v2_short x v2 x escena,
#      contra la linea de base T1. Pone a prueba F-81.2b (pre-roll de P7/P9).
#
# Ambos runners son reanudables: si la maquina duerme, relanzar este script retoma
# donde quedo. Trampa D-61.4: el run_descriptor NO guarda la variante 560 — la
# procedencia del modelo queda declarada ACA y en el campaign.yaml.
set -u
DATOS=/home/simonll4/projects/docs/operacion/datos

echo "[CHAIN] inicio $(date '+%F %T') — servicio esperado: gdino-base-560"

python3 "$DATOS/83-fase-d-nivel-a-runner.py" --out-dir "$DATOS/84-fase-d-nivel-a-base560"
rc=$?
if [ $rc -ne 0 ]; then
  echo "[CHAIN] FALLO fase Nivel A (rc=$rc) — no se lanza T2"
  exit $rc
fi
echo "[CHAIN] Nivel A base-560 COMPLETO $(date '+%F %T')"

python3 "$DATOS/81-ciclo-rodaje-runner.py" --out-dir "$DATOS/84-t2-base560-clips"
rc=$?
if [ $rc -ne 0 ]; then
  echo "[CHAIN] FALLO fase T2 clips (rc=$rc)"
  exit $rc
fi
echo "[CHAIN] T2 base-560 COMPLETO $(date '+%F %T')"
echo "[CHAIN] DONE"
