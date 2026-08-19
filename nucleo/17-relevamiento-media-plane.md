# 17 — Relevamiento: `e-ovrt_media-plane`

- **Fecha de relevamiento:** 2026-08-10
- **Reemplaza a:** `historicos/11-relevamiento-media-plane.md` (foto del 2026-07-09, histórica)
- **Método:** relevado **contra git y código**. Los comandos de §2 y la suite de §7 se
  ejecutaron en esta máquina; la estructura de §3 es el árbol real.
- **Regla de este documento:** **no publica ninguna cifra de resultado.** Las métricas
  viven en los cuatro índices de `e-ovrt_experimental-setup/results/`; la historia de
  capacidades, en `operacion/97`.

---

## 1. Qué es, y qué no es

El **plano de percepción**: un servicio de detección de vocabulario abierto (OVD)
config-driven. Recibe imágenes o video, corre un modelo OVD con un conjunto de prompts, y
emite **detecciones normalizadas** (`media.detection.v1`) que el control-plane consume.

**Desde la Fase 1 (Spec A) ya no es una CLI**: es un **servicio** FastAPI. El modelo se
carga **una vez al arrancar** desde `EOVRT_MODEL_REF`, y una corrida se dispara con
`POST /api/runs`. **Una corrida activa por vez.**

**Qué NO hace:**

- **No evalúa condiciones de riesgo.** No sabe qué es CR-01. Detecta clases; que la
  ausencia de casco sea una violación lo decide el control-plane.
- **No hace tracking.** `Detection` tiene un `track_id` **opcional** en el contrato, pero
  el media-plane no lo produce: la identidad de sujeto se resuelve aguas abajo, como
  decorador de fuente en el control-plane (ver `18` §5.3).
- **No distribuye ni notifica.** Publica detecciones; qué se hace con ellas es de los
  planos siguientes.
- **No entrena.** El fine-tuning (E-04) es una jornada aparte comprometida por ADR-017
  y corre en el clúster (Mendieta), nunca en esta máquina; el media-plane solo
  consumiría los pesos resultantes.

## 2. Cómo se ejecuta

```bash
cd e-ovrt_media-plane
python3.12 -m venv .venv && source .venv/bin/activate && pip install -e ".[gpu,dev]"
make download-models              # pesos: GDINO, MM-GDINO, YOLOE

EOVRT_MODEL_REF=mock make serve   # uvicorn --factory eovrt_media.service.app:create_app :8080
make smoke                        # curl /healthz + /readyz
make test                         # 641 passed, 5 skipped (2026-08-10)
make lint                         # ruff check src tests
```

Las ex-utilidades de CLI viven en `eovrt_media.tools.*` y se invocan con `python -m`
(por ejemplo `python -m eovrt_media.tools.evaluate`).

> **Trampa de entorno:** mover el repo de directorio rompe el `eovrt-media` instalado y los
> imports. Hay que reinstalar en editable, o invocar por `python -m eovrt_media...`.

## 3. Estructura del código

85 archivos bajo `src/eovrt_media/`:

```
src/eovrt_media/
├── config/            # carga y validación de YAML (nada hardcodeado)
├── contracts/         # events.py, detection.py — los contratos versionados
├── sources/           # de dónde entran los fotogramas
│   ├── image_folder_source.py    # NO recursivo: apunta a una carpeta hoja
│   ├── video_file_source.py
│   ├── rtsp_source.py
│   └── oak_d_source.py           # OAK-D Pro PoE + prefilter EN-2
├── preprocessing/     # image_loader.py, normalizer.py
├── models/            # adaptadores: grounding_dino_adapter, yoloe_adapter, mock_detector
├── postprocessing/    # normalización de detecciones (bbox, area_px, ids)
├── runtime/           # orquestación de la corrida
├── service/           # FastAPI :8080 (endpoints en §6.1)
├── transport/         # bus.py — publisher ZeroMQ PUB
├── sinks/             # persistencia de artefactos por corrida
├── metrics/           # instrumentación de tiempos
├── evaluation/        # evaluación contra GT de imágenes
├── debugging/         # utilidades de inspección
└── tools/             # ex-CLI: evaluate, anotación de video, etc.
```

## 4. Contratos

| Contrato | Qué es |
|---|---|
| `media.detection.v1` | **El contrato central.** Detecciones normalizadas de una unidad visual |
| `media.dropped_unit.v1` | Ledger de descartes: qué unidad se tiró y por qué. Nunca silencioso |
| `media.metric.v2` | Tiempos y conteos por unidad |
| `media.summary.v2` | Agregados de la corrida |
| `media.error.v1` | Errores por unidad |

`media.detection.v1` lleva `run_id`, `unit_id`, `source{source_id, source_type,
frame_index, timestamp_ms, width, height}`, `model`, `prompts`, `detections[]` y `timing`.
Cada `Detection` incluye bbox normalizado, `area_px`, `label`, score, y opcionalmente
`source_prompt`, `strategy`, `condition_id` y `track_id`.

**El `detection_id` es por frame** (`det_NNNNNN`, índice de orden dentro del fotograma), no
un identificador de sujeto persistente. Confundirlos fue un modo de falla histórico: por
eso la identidad se resuelve aguas abajo y con verificación explícita (`18` §8.6).

Una corrida escribe `runs/<run_id>/`: `detections.jsonl`, `effective_config.yaml`,
`metrics.jsonl`, `errors.jsonl`, `summary.json`, `run_manifest.json`,
`run_provenance.json` y `previews/`.

## 5. Configuración y catálogos

Todo por YAML: **ni rutas ni umbrales hardcodeados**.

### 5.1 Catálogos de modelos (`configs/models/`)

| Familia | Variantes |
|---|---|
| `grounding-dino` | `gdino-tiny`, `gdino-base`, **`gdino-tiny-560`**, `gdino-base-560` |
| `yoloe` | `yoloe-26s`, `-26m`, `-26l`, `-26x` |
| `mock` | detector de mentira, para smoke sin GPU |
| ⚠️ `mm-grounding-dino` | `mm-gdino-tiny`, `-base`, `-large`. **Catálogo conservado pero descartado** en el bench (bboxes rotos en la variante tiny) — no usar sin releer el motivo |

Las variantes `-560` difieren solo en `image_size: 560`.

> **Hueco declarado:** los catálogos de modelos **no registran la licencia** del peso que
> descargan. Es uno de los hallazgos abiertos de `informe/99` §6.

### 5.2 Datasets (`configs/datasets/`)

`bench_v2_test`, `bench_v2_val`, `chv`, `demo_v2`, `video_sample`. Usan **paths relativos
cross-repo** del tipo `../e-ovrt_datasets/datasets/raw/...`, lo que asume dos cosas: que los
repos son hermanos en disco, y que `eovrt-media` se ejecuta **desde la raíz del
media-plane** (los paths resuelven contra el CWD).

> ✎ **2026-08-19:** `chv` y `video_sample` fueron **archivados a `configs/_archive/`**
> del media-plane (huérfanos: nadie los consumía) — el inventario vivo es
> `bench_v2_test`, `bench_v2_val`, `demo_v2`. El benchmark de imágenes **vigente** es
> **`bench_v3`** (definido en el registry del repo datasets, no en estos configs); los
> `bench_v2_*` son los configs de los splits v2 **históricos**.

> **Trampa:** `ImageFolderSource` **no es recursivo**. Un config de dataset apunta a una
> carpeta hoja de imágenes, no a la raíz del dataset.

### 5.3 Prompts

Los conjuntos de prompts **no viven acá**: viven en `e-ovrt_experimental-setup/prompts/`
(ver `15`). El media-plane conserva el **contrato** y los catálogos por id. Es la separación
que permite cambiar el vocabulario sin tocar el plano.

## 6. Acople con los vecinos

**Aguas arriba:** `e-ovrt_datasets` por path relativo (imágenes y video), y hardware real
por RTSP u OAK-D.

**Aguas abajo — control-plane**, por dos caminos:

- **DBE:** escribe `runs/<id>/detections.jsonl`; el control-plane lo relee. El repositorio
  es la fuente de verdad.
- **EBE:** publica en el bus ZeroMQ PUB con envelope `bus.envelope.v1` cuando
  `bus.enabled: true` (ADR-003).

**Orden de disparo en live:** el consumidor **debe suscribirse antes** de que arranque el
run — primero `POST :8081/api/runs` en el control-plane, después `POST :8080/api/runs` acá.
Detalle en `18` §6.

**Clientes HTTP:** la webconsole y el runner (`15`).

### 6.1 Endpoints

`GET /healthz` · `GET /readyz` · `GET /model` · `GET /datasets` · `GET /ingest-plugins` ·
`POST /api/runs` · `GET /api/runs` · `GET /api/runs/{id}` · `DELETE /api/runs/{id}` ·
`POST /api/runs/{id}/stop` · `GET /api/runs/{id}/detections` · `GET /api/runs/{id}/dropped` ·
`GET /api/runs/{id}/artifacts/{path}` · `POST|GET /api/runs/{id}/evaluate` ·
`GET /api/runs/{id}/stream` · sesiones de **preview en vivo** (`/preview`,
`/preview/stream`).

## 7. Estado de implementación y límites

**Construido y ejercido:** el servicio con carga única de modelo · las cuatro fuentes
(carpeta de imágenes, archivo de video, RTSP, OAK-D) · adaptadores GDINO / YOLOE / mock ·
el ledger de descartes · el bus de salida · preview en vivo · evaluación contra GT de
imágenes. Suite: **641 passed, 5 skipped**.

**Lo que no está:**

- **Productor de `track_id`.** El campo existe en el contrato; nadie lo llena acá. Resuelto
  aguas abajo (ADR-002 del proyecto, adenda ratificada).
- **Fine-tuning (E-04).** Los splits están materializados y el camino operacionalizado;
  ✎ 2026-08-11: **jornada comprometida por ADR-017** (*decía "no se ejerce por
  secuenciación"*). Corre en el clúster, nunca local; acá solo aterrizarían los pesos
  ajustados como variante de catálogo.
- **Inferencia en borde (EN-3).** Excluida. Lo que sí se ejerció es la **OAK-D como fuente**
  y el **prefilter EN-2**, opcional y apagado por default (E-07 parcial).
- **Licencia en los catálogos de modelos.** Hueco abierto, §5.1.

**Runs no citados:** al 2026-08-10, de 462 runs en `runs/` hay 34 que no cita ningún
documento ni índice. Todos conservan `effective_config.yaml` y `run_provenance.json`.
`runs/`, `models/` y `.venv/` están gitignoreados: el repo versionado son 333 archivos.

## 8. Trampas conocidas

1. **Mover el repo rompe el entorno** — reinstalar editable o usar `python -m`.
2. **`ImageFolderSource` no es recursivo** — apuntar a la carpeta hoja.
3. **Los paths cross-repo resuelven contra el CWD** — ejecutar desde la raíz del repo.
4. **`outputs.base_dir` en las configs de corrida resuelve relativo al archivo de config.**
5. **`ingest.config` de la OAK-D usa `url`, no `ip`** — con `ip` devuelve 422.
6. **`warmup_frames` viene en 0 por default**, lo que sesga la primera medición de latencia.
7. **El `ping` a cámaras link-local desde WSL miente** si WSL está en NAT: responde el
   gateway de Windows con `ttl=63`. Verificar con `ip route get` (sin `via`), `ttl=64` y
   `dai.Device()`. Requiere `networkingMode=mirrored`; `wsl --shutdown` **no alcanza**.
8. **WSL se cae por `global_oom`, no por la GPU** — `workers=8` de ultralytics revienta un
   VM de 7,4 GiB; los `dxg Ioctl failed: -12` son consecuencia, no causa.

## Referencias

`historicos/11` (relevamiento histórico) · `14` (mapa de la cadena) · `16` (datasets, aguas arriba) ·
`18` (control-plane, aguas abajo) · `specs/42-media-plane.md` · `e-ovrt_media-plane/CLAUDE.md` ·
`operacion/97` (capacidades y evidencia medida) · ADR-003 (bus) · `operacion/61` (dry-run de
cámaras) · `operacion/68` y `91` (red de WSL y OAK-D).
