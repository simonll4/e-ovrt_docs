# Runbook local — media-plane + webconsole sin Docker

- **Última actualización:** 2026-07-09
- **Propósito:** levantar los dos servicios en local, con hot-reload, para iterar rápido.
  Sin `docker build`. El control-plane queda fuera (se integra más adelante).
- **Topología:** un solo host. La consola es **cliente HTTP/WS** del media-plane; no
  ejecuta el pipeline.

```
navegador  ──►  webconsole (BFF + SPA)  ──►  media-plane (servicio de inferencia)
                :8090                        :8080
```

## Prerrequisitos (una sola vez)

Los dos venvs y `node_modules` ya existen en este workspace. Si arrancás de cero:

```bash
cd e-ovrt_media-plane
python3.11 -m venv .venv && source .venv/bin/activate && pip install -e ".[gpu,dev]"
make download-models        # pesos GDINO / MM-GDINO / YOLOE

cd ../e-ovrt_experimental-setup/webconsole
make install                # venv del backend + npm install
```

## Levantar (dos terminales)

### Terminal 1 — media-plane (`:8080`)

```bash
cd e-ovrt_media-plane
source .venv/bin/activate                     # `make serve` usa el uvicorn del PATH
EOVRT_MODEL_REF=grounding-dino/gdino-tiny make serve
```

El modelo se carga **una vez al arrancar**, no por corrida. Con GDINO-tiny sobre GPU
tarda ~13 s hasta quedar `ready`. Esperá a que `/readyz` conteste antes de lanzar nada.

Refs disponibles (el ref es la ruta bajo `configs/models/`, sin `.yaml`):

| Ref | Cuándo usarlo |
|---|---|
| `mock` | Iterar sobre la consola o el pipeline sin GPU. Arranca instantáneo. |
| `grounding-dino/gdino-tiny` | **Default recomendado.** Mejor mAP del Sprint 2 (0.441). |
| `grounding-dino/gdino-base` | Más lento, más preciso. |
| `yoloe/yoloe-26{s,m,l,x}` | Rápido, pero sin `vest` ni `bare_head`. |
| `mm-grounding-dino/*` | Descartado en Sprint 2 (bboxes rotos). No usar. |

### Terminal 2 — webconsole (`:8090`)

```bash
cd e-ovrt_experimental-setup/webconsole
make serve
```

`make serve` depende del target `build`, así que **recompila la SPA antes de servirla**.
No arranques `uvicorn` a mano salvo que sepas que el `dist/` está fresco (ver la trampa
más abajo).

Apunta a `http://localhost:8080` por defecto. Para otro target:

```bash
EOVRT_CONSOLE_SERVICE_URL=http://otro-host:8080 make serve
```

Abrí **http://localhost:8090**.

## Verificar que quedó bien

```bash
cd e-ovrt_media-plane            && make smoke   # /healthz + /readyz
cd e-ovrt_experimental-setup/webconsole && make smoke   # /api/health + /api/target
```

`/api/target` de la consola debe devolver `"ready": true` y el `ref` del modelo que
cargaste. Si dice `healthy: false`, el media-plane no está arriba.

## Lanzar una corrida RTSP

La URL real de la cámara (con credenciales) **no vive en este doc ni en ningún archivo
versionado** — sigue el mismo criterio que ya está establecido en el media-plane desde
la prueba EZVIZ del 2026-06-21 (`docs/_archive/superpowers/plans/2026-06-21-prueba-rtsp-ezviz-yoloe-single-host.md`):
nunca commitear la URI ni las credenciales. Está guardada, gitignored, en:

```
e-ovrt_media-plane/configs/runs/local/rtsp_camera.env
```

```bash
source e-ovrt_media-plane/configs/runs/local/rtsp_camera.env   # exporta $EZVIZ_RTSP_URL
echo "$EZVIZ_RTSP_URL"                                          # copiar y pegar donde haga falta
```

En la consola: **Nueva corrida → Plugin de ingesta: `rtsp`** → pegar `$EZVIZ_RTSP_URL`
en el campo de URL (formato esperado: `rtsp://usuario:clave@ip:554/stream`).

Las fuentes vivas generan **runs infinitos**: se cortan a mano con "■ Detener" en la
vista del run. Al guardar un manifiesto, las credenciales se escriben **redactadas**
(`rtsp://***:***@...`); tenés que recompletar usuario y clave al re-lanzar.

`oak_d` está habilitado (implementado 2026-07-13): requiere la cámara OAK-D Pro PoE
en la LAN con IP fija y el SDK DepthAI (`pip install -e ".[edge]"` en el media-plane).
Ver `e-ovrt_media-plane/docs/contexto/oak-d-integration.md`.

Si `configs/runs/local/rtsp_camera.env` no existe (p. ej. clon nuevo del repo),
recrealo con:

```bash
cat > e-ovrt_media-plane/configs/runs/local/rtsp_camera.env << 'EOF'
EZVIZ_RTSP_URL="rtsp://usuario:clave@ip:554/stream"
EOF
```

## Iterar rápido

### Backend de la consola (hot-reload)

```bash
cd e-ovrt_experimental-setup/webconsole
make dev-backend       # uvicorn --reload en :8090
```

### Frontend (Vite, hot-reload real)

```bash
make dev-frontend      # :5173, proxea /api → :8090
```

Con `dev-frontend` trabajás contra `http://localhost:5173` y **no necesitás rebuildear**
el `dist/` en cada cambio. Es el modo recomendado para tocar la SPA.

### Media-plane

Para iterar sobre el pipeline o los routers, usá `EOVRT_MODEL_REF=mock`: `--reload`
recarga el proceso entero en cada guardado, y con un modelo real eso significa volver a
cargar los pesos cada vez.

```bash
source .venv/bin/activate
EOVRT_MODEL_REF=mock uvicorn --factory eovrt_media.service.app:create_app --reload --port 8080
```

## Bajar los servicios

`Ctrl-C` en cada terminal. Si quedó algo colgado:

```bash
ss -ltnp | grep -E ':8080|:8090'    # ver quién ocupa los puertos
```

## Trampas conocidas

**El `dist/` viejo se sirve sin avisar.** Si arrancás el BFF con `uvicorn` directo en vez
de `make serve`, la consola sirve el bundle que haya en `frontend/dist/`, por más viejo
que sea. Síntoma típico: una opción nueva (p. ej. `rtsp`) no aparece en el desplegable
aunque `GET /api/catalog/ingest-plugins` la reporte con `enabled: true`. Solución:
`make build`, y recargar el navegador con `Ctrl-Shift-R`.

**Un run contra una cámara inalcanzable termina como `succeeded`.** El `ConnectionError`
queda en `errors.jsonl` con `recoverable: true` y el run cierra con `units_processed: 0`.
En la consola vas a ver un run "exitoso" con cero frames. Si te pasa, revisá:

```bash
cat e-ovrt_media-plane/runs/<run_id>/errors.jsonl
```

**Un solo run activo por instancia.** Un segundo `POST /api/runs` mientras hay uno vivo
devuelve `409`. Pará el anterior primero.

**Los datasets se resuelven contra el CWD.** `configs/datasets/*.yaml` usa rutas
`../e-ovrt_datasets/...`, así que el media-plane tiene que arrancarse **desde su raíz**
(o setear `EOVRT_DATASETS_ROOT`).

## Qué queda afuera a propósito

- **control-plane**: se integra más adelante (bus de eventos, D3 del doc 03).
- **Docker / two-node**: `infra/twonode/` (media-plane) e `infra/platform/`
  (experimental-setup). Este runbook es explícitamente el camino sin contenedores.
- **oak_d**: implementado; el run real requiere la cámara conectada a la LAN
  (ver `e-ovrt_media-plane/docs/contexto/oak-d-integration.md`).
