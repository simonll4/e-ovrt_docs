#!/bin/bash
# Levanta media-plane (:8080) y control-plane (:8081) y espera a que ambos esten ready.
# Cada uno DESDE LA RAIZ DE SU REPO (doc 82 trampa 5: si no, los artefactos caen en
# projects/runs/ y la config relativa no resuelve).
#
# Uso:  bash 91-arrancar-servicios.sh          # gdino-tiny-560 (campeon)
#       EOVRT_MODEL_REF=... bash 91-arrancar-servicios.sh
set -u
MODEL="${EOVRT_MODEL_REF:-grounding-dino/gdino-tiny-560}"
LOGS="${LOGS_DIR:-/tmp/eovrt-smoke-logs}"
mkdir -p "$LOGS"

echo "[*] limpiando servicios previos"
ps -eo pid,cmd | grep -E "[u]vicorn --factory eovrt|[e]ovrt-control serve" | awk '{print $1}' | xargs -r kill -9
sleep 2

echo "[*] media-plane :8080  (EOVRT_MODEL_REF=$MODEL)"
cd /home/simonll4/projects/e-ovrt_media-plane || exit 1
EOVRT_MODEL_REF="$MODEL" nohup .venv/bin/uvicorn --factory \
  eovrt_media.service.app:create_app --host 127.0.0.1 --port 8080 \
  > "$LOGS/media.log" 2>&1 &

echo "[*] control-plane :8081"
cd /home/simonll4/projects/e-ovrt_control-plane || exit 1
nohup .venv/bin/eovrt-control serve --port 8081 > "$LOGS/control.log" 2>&1 &

echo "[*] esperando ready (el modelo tarda ~20-40 s en cargar)"
for i in $(seq 1 90); do
  m=$(python3 -c "
import urllib.request
try: print('ok' if b'ready' in urllib.request.urlopen('http://127.0.0.1:8080/readyz', timeout=2).read() else 'no')
except Exception: print('no')" 2>/dev/null)
  c=$(python3 -c "
import urllib.request
try:
    urllib.request.urlopen('http://127.0.0.1:8081/healthz', timeout=2); print('ok')
except Exception: print('no')" 2>/dev/null)
  if [ "$m" = "ok" ] && [ "$c" = "ok" ]; then
    echo "[OK] ambos servicios arriba"
    python3 -c "
import urllib.request; print('     media:', urllib.request.urlopen('http://127.0.0.1:8080/readyz', timeout=5).read().decode())"
    echo "     logs: $LOGS/{media,control}.log"
    exit 0
  fi
  sleep 2
done
echo "[FALLO] no quedaron ready. Ultimas lineas:"
tail -5 "$LOGS/media.log" "$LOGS/control.log"
exit 1
