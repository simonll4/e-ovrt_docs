# Relevamiento técnico — `e-ovrt_media-plane` (plano de medios)

Fecha del relevamiento: 2026-08-28 · Modo: SOLO LECTURA (grep/cat/git/python3 sin importar el paquete; ningún test ejecutado).
Rutas relativas a `/home/simonll4/projects/e-ovrt_media-plane/` salvo indicación. `src/` = `src/eovrt_media/`.

---

## A) Estado del repo

| Ítem | Valor | Cómo se verificó |
|---|---|---|
| Rama | `feature/inference-service` | `git branch --show-current` |
| HEAD | `f439db2` = `f439db280495b8e468d1e71a5d15250402649540` | `git rev-parse HEAD` |
| Fecha HEAD | 2026-08-22 03:34:57 +0000 — `feat(configs): catalogo del checkpoint T2 (yoloe-26s-ft-t2)` | `git log -1 --date=iso` |
| Working tree | limpio (`git status --short` vacío) | |
| Remote | `origin git@github.com:simonll4/e-ovrt_media-plane.git` | coincide con `CLAUDE.md` raíz |
| CI | **no hay** (`.github/` no existe) | `ls .github` → No such file |
| Python declarado | `requires-python = ">=3.11"`, `ruff target-version = "py311"` (`pyproject.toml`) | |
| Python real del venv | **3.12.13** (`.venv/bin/python --version`) — coincide con `CLAUDE.md` del repo (`python3.12 -m venv`) | |
| Python del Dockerfile | **3.11** (deadsnakes) sobre `nvidia/cuda:12.4.1-runtime-ubuntu22.04` (`infra/docker/Dockerfile:2,7-14`) | |
| Pins (constraints.txt) | `torch==2.12.1`, `torchvision==0.27.1`, `transformers==5.12.1`, `ultralytics==8.4.86`, `pyzmq==27.1.0`, `msgpack==1.2.1`, `fastapi==0.139.0`, `uvicorn==0.49.0`, `opencv-python==5.0.0.93`, `pydantic==2.13.4`, ruedas `nvidia-*-cu13` (CUDA 13) | `cat constraints.txt` |
| Instalado en `.venv` | torch 2.12.1 · transformers 5.12.1 · ultralytics 8.4.86 · depthai 2.32.0.0 · fastapi 0.139.0 · pyzmq 27.1.0 · msgpack 1.2.1 | `ls .venv/lib/python3.12/site-packages` |
| `pyproject` deps base | pillow, opencv-python, pydantic, pyyaml, rich, pyzmq, msgpack, fastapi>=0.110, uvicorn[standard]. Extras: `edge` (depthai>=2.24,<3, blobconverter), `gpu` (torch, torchvision, transformers, accelerate, huggingface_hub, ultralytics), `dev` (pytest, ruff, httpx, supervision). **Sin `[project.scripts]`** → no existe CLI `eovrt-media` | |
| Tests (grep) | **643** `def test_` en **81** archivos `tests/test_*.py`; 9 archivos usan `pytest.mark.parametrize` (el conteo *collected* es mayor). `tests/fixtures/` único subdir | `grep -rh 'def test_' tests/ \| wc -l` |
| Conteos documentados | `docs/implementation-status.md:196` → **646** (collect-only 2026-07-29) · `docs/operacion/97` (2026-08-05) → **641 passed, 5 skipped** · después de ambos entró `d40b3bd` (2026-08-17) que **agrega tests** (`test_config_refs`, `test_model_factory_runtime`, `test_yoloe_binding`, `test_yoloe_runtime`) ⇒ **ninguna de las tres cifras es actual** | ver C-4 |
| `runs/` local | 472 directorios de corrida (gitignorado) | `ls runs \| wc -l` |

**Últimos 30 commits (2026-07-05 → 2026-08-22), los relevantes para el informe:**

| Commit | Fecha | Qué |
|---|---|---|
| `f439db2` | 08-22 | catálogo `yoloe/yoloe-26s-ft-t2` (T2, serving open-vocabulary vía `set_classes`) |
| `ee7a6af` | 08-19 | archiva MM-GDINO (`configs/_archive/mm-grounding-dino/`), `chv.yaml`/`video_sample.yaml`, `steelbench.py`; `.dockerignore`, `.env.example`, docs sync |
| `d40b3bd` | 08-17 | `fixed_vocabulary` canónico v2 (D-FT-08) + catálogo `yoloe-26s-ft-t1` |
| `716b8af` | 07-29 | implementation-status "646 tests", venv 3.12 |
| `d4f9ef4` | 07-24 | `RunSummary.name` |
| `c78bd16` | 07-23 | `evaluate` restringe `person_gt` al run por default |
| `da44756` | 07-23 | **`image_size` en GDINO + catálogos `gdino-tiny-560` / `gdino-base-560`** |
| `b37d550` | 07-23 | **`prepare_run`** pre-flight por corrida |
| `9ef144c` | 07-23 | run con 0 unidades → `failed` con motivo (F-DR10) |
| `eddeb89`/`cee8832`/`71bf0ac` | 07-18 | sesión de preview en vivo (`/api/preview`) |
| `d9f21fa` | 07-18 | `source.warmup_frames` (warm-up de lente, fuentes vivas) |
| `24522cb` | 07-17 | ledger `dropped_units.jsonl` |
| `9cede10` | 07-17 | **prefilter EN-2 on-device (OAK-D) + `capture_to_host_ms`** |
| `df5f7c7` | 07-13 | **OAK-D Pro PoE como fuente viva** |
| `0133d38` | 07-13 | `track_id` opcional en `Detection` |
| `bfb2f58` | 07-11 | **publisher ZeroMQ (bus) + instrumentación G2A** |
| `774c677` | 07-11 | `experiment_id` en `POST /api/runs` |
| `b8f180b` | 07-06 | split EBE two-node dockerizado (Fase 2) |
| `b7846b8` | 07-05 | deploy movido a `infra/` (`infra/docker/Dockerfile`) |

---

## B) Afirmaciones verificadas

Leyenda: ✅ coincide · ⚠️ parcial/imprecisa · ❌ no coincide.

| # | Afirmación | Doc fuente | Veredicto | Evidencia (ruta:línea / valor) |
|---|---|---|---|---|
| B1 | Campeón `grounding-dino/gdino-tiny-560`, variante `image_size: 560` del catálogo existente | CLAUDE.md raíz "Modelo campeón" | ✅ | `configs/models/grounding-dino/gdino-tiny-560.yaml:9,16,21` (`variant: gdino-tiny-560`, `model_id: IDEA-Research/grounding-dino-tiny`, `image_size: 560`) |
| B2 | box_threshold efectivo del campeón = **0,30** (no 0,35) | pase 3 / correcciones-etapa-3-4 (memoria) | ✅ | `gdino-tiny-560.yaml:19` `box_threshold: 0.30`; `gdino-base-560.yaml:16` 0.30; `gdino-base.yaml` 0.30; **`gdino-tiny.yaml:13` = 0.35** (el 800 px). Default de schema/adapter 0.35 (`schemas.py:433`, `grounding_dino_adapter.py:63`). En los 472 runs locales: todas las corridas `gdino-tiny-560` usan 0.3; las `gdino-tiny` (800) usan 0.35 |
| B3 | `confidence_threshold` es del carril YOLOE, no de GDINO | ídem | ✅ | `models/__init__.py:36-45` pasa a `GroundingDinoHFAdapter` solo `box_threshold`, `text_threshold`, `iou_threshold`, `image_size`; `confidence_threshold` sólo va a `YOLOEUltralyticsAdapter` (`:53`). ⚠️ **pero** `effective_config.yaml` de un run GDINO imprime igual `confidence_threshold: 0.25` e `iou_threshold: 0.5` (defaults de `schemas.py:438-439`) — ver C-3 |
| B4 | `image_size: 560` se aplica en la inferencia (letterbox 560) | CLAUDE.md raíz, doc 61/64 | ✅ | `grounding_dino_adapter.py:123-129` (`processor size = {shortest_edge, longest_edge} = image_size`), `models/__init__.py:44` |
| B5 | Catálogo de modelos exacto | CLAUDE.md raíz / compose | ✅ | 11 catálogos activos: `mock`; `grounding-dino/{gdino-tiny, gdino-tiny-560, gdino-base, gdino-base-560}`; `yoloe/{yoloe-26s, yoloe-26m, yoloe-26l, yoloe-26x, yoloe-26s-ft-t1, yoloe-26s-ft-t2}`. Archivados: `configs/_archive/mm-grounding-dino/{tiny,base,large}.yaml` |
| B6 | `make download-models` baja GDINO tiny+base y YOLOE-26 s/m/l/x; MM-GDINO archivado 2026-08-19 | CLAUDE.md raíz + repo | ✅ | `scripts/download_models.sh:17-22` (hf download tiny/base), `:35` (yoloe-26{s,m,l,x}-seg.pt), `:25` comentario del archivado; `models/README.md:52-63` |
| B7 | Servicio FastAPI en `:8080`, `uvicorn --factory eovrt_media.service.app:create_app` | CLAUDE.md raíz, glosario §6, op97 | ✅ | `Makefile:19-21`; `infra/docker/Dockerfile` `EXPOSE 8080` + `CMD uvicorn --factory … --port 8080`; `service/app.py:71` `create_app` |
| B8 | Modelo cargado **una vez** al startup desde `EOVRT_MODEL_REF` (obligatorio) | CLAUDE.md raíz, glosario, op97:148 | ✅ | `service/settings.py:26-30` (ValueError si falta); `service/app.py:29-37` (`resolve_model_ref` → `create_adapter` → `adapter.load` una vez); `/readyz` 503 hasta que cargue (`routers/health.py:15-23`); `POST /api/runs` 503 si no listo (`routers/runs.py:22`) |
| B9 | Un run activo a la vez (segundo POST → 409) | README, op97, ADR-008 (análogo) | ✅ (+ matiz) | `run_manager.py:108-109` (`RunBusyError`), `routers/runs.py:33,47` (409). Matiz: `ActivitySlot` — "un run **o** una preview, nunca ambos" (`service/activity_slot.py:1`, `run_manager.py:118`) |
| B10 | Ya no es CLI; utilitarios en `eovrt_media.tools.*` | CLAUDE.md raíz/repo, README | ✅ | sin `[project.scripts]`; `src/tools/`: `evaluate.py`, `inspect_runs.py`, `preannotate_video.py`, `run_node.py`, `videogt.py` |
| B11 | `evaluate` restringe el GT al run por default | CLAUDE.md raíz | ✅ | `tools/evaluate.py:37` `restrict_gt_to_detections=True`; commit `c78bd16` |
| B12 | Fuentes de ingesta: `image_folder`, `video_file`, `rtsp`, `oak_d`; alias video/video_frame | README, CLAUDE.md | ✅ | `sources/registry.py:34-47`; `LIVE_SOURCE_TYPES = ("rtsp","oak_d")` (`schemas.py:145`); assert de coherencia (`registry.py:53`) |
| B13 | `ImageFolderSource` **no recursivo** | CLAUDE.md raíz | ✅ | `sources/image_folder_source.py:53-54` (`iterdir()` + filtro por sufijo, sin `rglob`) |
| B14 | Preselección EN-2 on-device existe, **default off**, degradación segura (fail-open), sólo `oak_d` | CLAUDE.md raíz, glosario "EN-2", memoria | ✅ | `schemas.py:155-176` (`OakDPrefilterConfig.enabled=False`, blob `person-detection-retail-0013_6shave.blob`, `keepalive/heartbeat/stall_failopen`); `:251-252` rechaza `prefilter` fuera de `oak_d`; `oak_d_source.py:57-58,99-101` (razones `failopen/heartbeat/warmup`), `:193-200` fail-fast si falta el blob; `Makefile:16` `download-prefilter-blob` |
| B15 | `bus.enabled` (default off), XPUB `tcp://0.0.0.0:5557`, msgpack, `bus.envelope.v1`, `seq` monótono que se incrementa aunque se descarte, NOBLOCK, JSONL = verdad | CLAUDE.md raíz, glosario, ADR-003 | ✅ | `schemas.py:361-369` (`BusConfig`: enabled False, endpoint, hwm 1000, `wait_for_subscriber_ms` 0); `transport/bus.py:19-22,69-74,127-128,138`; `service/bus_writer.py:34-40` (persiste primero; payload = `model_dump_json(exclude_none=True)` byte-idéntico al JSONL) |
| B16 | Cierre con `run.lifecycle.v1/run_finished` | CLAUDE.md raíz, ADR-007, glosario EBE | ✅ | `transport/bus.py:21-22`; `service/bus_writer.py:42-52` (`{"schema_version":"run.lifecycle.v1","event":"run_finished","media_run_id","status"}`) |
| B17 | Huecos de `seq` → `bus_dropped_events` (lado consumidor) | CLAUDE.md raíz, glosario, ADR-003 | ✅ | vive en el **control-plane**: `e-ovrt_control-plane/src/eovrt_control/contracts/metrics.py:69`, `runtime/core.py:300,316`. El media-plane sólo cuenta `send_failures` y documenta que **no** detecta pérdidas por HWM (`bus.py:49-57`) |
| B18 | "Las fuentes de red exponen `request_stop()`" | CLAUDE.md raíz "Trampa de concurrencia" | ⚠️ | En el media-plane las fuentes exponen **`stop()`** (`sources/base.py:28`, `rtsp_source.py:71`, `oak_d_source.py:298`); `request_stop()` es de **`RunControl`** (`runtime/pipeline.py:413`) y llama a `source.stop()`. `request_stop()` sí existe en `BusSource` del control-plane (ADR-003 estado). Ver C-7 |
| B19 | `warmup_frames` default 0, sólo fuentes vivas | memoria "Grabación de rodaje" / doc 69 | ✅ | `schemas.py:218` (`Field(default=0, ge=0)`), `:239-246` (422 si no es rtsp/oak_d); se descartan **en la fuente** (`rtsp_source.py:100-102`, `oak_d_source.py:417-427`) |
| B20 | `g2a_ms` = captura → resultado algorítmico, cerrado **al terminar la inferencia**, mismo reloj monotónico; se mide **desde el dequeue** (F-101.8) | glosario "G2A", contexto-base:364, doc 128 §1, op101 | ✅ | `runtime/pipeline.py:237-242` (`time.monotonic_ns() - item.capture_monotonic_ns`, antes del postproceso); `contracts/visual_unit.py:23` (`capture_monotonic_ns` se estampa al construir el `VisualUnit`, i.e. después de `cap.read()` / `queue.tryGet()`: `rtsp_source.py:93-115`, `oak_d_source.py:390,438-450`). Presupuesto 50–250 ms (`metrics/g2a.py:13-14`), veredicto sobre P95 (`:81`) |
| B21 | `capture_to_host` (fotón → dequeue) sólo OAK-D, 202–217 ms en rodaje | memoria/doc 101, results | ✅ (mecanismo) | `oak_d_source.py:432-433` (`dai.Clock.now() - msg.getTimestamp()`); `contracts/metrics.py:24-25` "solo oak_d"; summary con p50/p95/samples (`run_artifact_writer.py:209-218`). Ejemplo local: `run_20260818_002811…` p50 202,11 ms / p95 255,27 |
| B22 | two-node: G2A **no interpretable** (relojes de hosts distintos), no se fabrica cifra | ADR-006 (por docstring), CLAUDE.md repo | ✅ | `pipeline.py:244-254` (`g2a_ms = None`), `run_artifact_writer.py:199-200` (`not_interpretable / cross_node_monotonic_clock`) |
| B23 | Layout de artefactos de un run | usage.md "Leer resultados", ADR-009 | ✅ para usage.md / ❌ para "report.json"/"metrics.json" | `run_artifact_writer.py:76-142,283,307-310`: `run_config.yaml`, `effective_config.yaml`, `run_manifest.json`, `detections.jsonl`, `metrics.jsonl`, `errors.jsonl`, `dropped_units.jsonl` (lazy), `summary.json` (`media.summary.v2`), `run_provenance.json`, `previews/`, `annotated.mp4` (opt), `eval_perception.json` (post-evaluación, `run_manager.py:64`), `debug_events.jsonl` (debug). **No existen `report.json` ni `metrics.json`** en el media-plane (grep en `src/`: sólo `session_report.json` de debugging). Verificado en `runs/run_20260818_002811_dbe_grounding_dino_451265/` |
| B24 | `effective_config` persistido (ADR-009) con secretos redactados | ADR-009 estado, usage.md | ✅ | `run_artifact_writer.py:108`; `schemas.py` sección "Secret redaction" (`:557+`); `tests/test_secret_redaction.py` (10 tests) |
| B25 | `experiment_id` aceptado en `POST /api/runs` (ADR-004) | estado ADRs | ✅ | `service/run_request.py:58,116-117`; `RunSummary.experiment_id` |
| B26 | `source_clock` none/media/wallclock (ADR-013) | estado ADRs | ✅ | `image_folder_source.py:29` none · `video_file_source.py:31` media · `rtsp_source.py:26` / `oak_d_source.py:135` wallclock |
| B27 | Dockerfile presente; imagen usada por el deploy integral | CLAUDE.md raíz "Deploy integral" | ✅ | `infra/docker/Dockerfile`; `e-ovrt_experimental-setup/infra/platform/docker-compose.yml:16-19` (`x-mp-common` build context media-plane); fleet `mp-mock, mp-gdino-tiny-560, mp-gdino-base-560, mp-gdino-tiny, mp-gdino-base, mp-yoloe-26{s,m,l,x}` (`:139-183`), profile `models` (`:21`); bus `:5557` **no** publicado al host en el integral (`:36-38`), sí en el standalone (`infra/docker-compose.yml:22`) |
| B28 | Glosario: media-plane = FastAPI :8080, `EOVRT_MODEL_REF`, emite `media.detection.v1` | glosario §3 l.104 | ✅ | `contracts/events.py:44-47` `schema_version = "media.detection.v1"` |
| B29 | Glosario: `media.dropped_unit.v1` con razones `rate_gate/queue_full/staleness_timeout/channel_closed` | glosario §4 l.144 | ✅ | `contracts/dropped_unit.py:10`; `pipeline.py:88`, `transport/memory.py:59,69,144` |
| B30 | Glosario §6 puertos: media :8080 | glosario l.254 | ✅ | ídem B7 |
| B31 | GUIA §1: "Recibe video (archivo o cámara), corre el modelo OVD y emite detecciones" | GUIA-REDACTORES §1 | ✅ (también imágenes) | B12 |
| B32 | contexto-base l.364: G2A 14,7 ms "desde el dequeue" | project-kit | ✅ mecanismo (cifra no verificable acá) | B20 |
| B33 | ADR-003 estado: `transport/bus.py` `BusPublisher` XPUB, `seq` monótono, persiste-primero, knob `bus.enabled` | estado ADRs | ✅ | B15 |
| B34 | op97 §2.2 lista de commits del media-plane (07-18→07-24) | op97 | ✅ | coinciden hash por hash con `git log` |
| B35 | op97 tabla suites: media-plane 641 passed / 5 skipped | op97:52 | ⚠️ desactualizado | ver A y C-4 |
| B36 | README tabla "Adaptadores soportados": `grounding_dino_hf`, `yoloe_ultralytics` | README.md | ⚠️ | los catálogos usan `adapter: grounding_dino` / `adapter: yoloe`; `create_adapter` acepta ambos alias (`models/__init__.py:33,48`) pero el mensaje de error sólo lista `mock, grounding_dino, yoloe` (`:69`) |
| B37 | Precisión fp16 y warmup del modelo por default | usage.md "Knobs" | ✅ | `schemas.py:375-376` (`half_precision=True`, `warmup=True`); `grounding_dino_adapter.py:150-154` autocast fp16 en cuda; `models/base.py::prepare_run` (pre-flight, `pipeline.py` vía `b37d550`) |
| B38 | Prompt set congelado `cr01_cr02_v2_short`, `language: en`, `status: frozen` con sha | CLAUDE.md raíz, doc 67 | ✅ | `e-ovrt_experimental-setup/prompts/cr01_cr02_v2_short.yaml` (`language: en`, `frozen_sha256: df81fd48…`); schema `PromptSet.language` opcional (`schemas.py:44`) |
| B39 | `active_ids` permite vocabulario parcial (aislamiento) | §17.1.5.4.2 (protocolo) | ✅ mecanismo | `schemas.py:497` (`PromptsSection.active_ids`), `:56-69` (`get_active_classes`, `build_plan`) |

---

## C) Divergencias doc↔código (por gravedad)

### C-1 · ALTA (afecta una cifra ancla del informe) — La comparación 800 px vs 560 px de GDINO-tiny **no está a umbral igual**
- **Qué dice el doc:** CLAUDE.md raíz / doc 61 / doc 64 / contexto-base:1354: "la resolución 560 da −24 % de latencia con **igual o mejor mAP** que 800"; `gdino-tiny-560` es "variante `image_size: 560` de los catálogos existentes".
- **Qué hay en el código:** `configs/models/grounding-dino/gdino-tiny.yaml:13` `box_threshold: 0.35` vs `gdino-tiny-560.yaml:19` `box_threshold: 0.30`. El propio comentario del catálogo 560 dice "mismo checkpoint … catálogo separado para mantener comparabilidad", pero el umbral **cambió**. En los 472 runs locales: **todas** las corridas `gdino-tiny` (800) corrieron a 0.35 y **todas** las `gdino-tiny-560` a 0.30 (p.ej. `run_20260723_023440_dbe_grounding_dino_8819f7` tiny@0.35 vs `run_20260723_023517_dbe_grounding_dino_07105b` tiny-560@0.30, ambos `image_folder` el mismo día). Para `gdino-base` ↔ `gdino-base-560` sí es 0.30 en ambos.
- **Por qué importa:** AP@0.5 es sensible al umbral de score (bajarlo sube recall y típicamente AP). La ganancia "igual o mejor mAP a 560" está **confundida** con −0,05 de umbral en el par tiny. La cifra del campeón (0,551) es válida como dato de la combinación (tiny·560·0,30); lo que no puede afirmarse sin re-verificar es "la resolución sola no degrada".
- **Qué corregir y dónde:** (a) en `docs/operacion/61` y `64` declarar el umbral de cada brazo y, si no se controló, reescribir la conclusión como "560 px @0,30 ≥ 800 px @0,35"; (b) en el informe (§17.4/§17.5) citar siempre el par (resolución, box_threshold) del campeón: **560 / 0,30 / text 0,25 / NMS IoU 0,50 / fp16**; (c) opcional: alinear `gdino-tiny.yaml` a 0.30 o dejar constancia de por qué no.

### C-2 · MEDIA — El campo `run.scenario` **no clasifica nada**: los 472 runs dicen `DBE`, incluidos los live OAK-D/RTSP
- **Qué dice el doc:** glosario §3 define DBE/EBE por el acople (archivo vs bus) y la fuente (dataset vs cámara); `README` habla de "las cuatro combinaciones escenario × topología"; op97/doc 71 hablan de "6 corridas live" del rodaje.
- **Qué hay en el código:** `schemas.py:126` `scenario: str = "DBE"` — texto libre, sin validación ni derivación desde `source.kind`/`bus.enabled` (grep `scenario` en `schemas.py` y `run_request.py`: sólo el default). El `RunRequest` (`run_request.py:49-58`) ni siquiera expone `scenario`. Resultado: **100 % de los runs locales** tienen `scenario: DBE` en `effective_config.yaml` y `dbe` en el `run_id`, incluidas 73 corridas `oak_d` y 21 `rtsp` (p.ej. `run_20260818_002811_dbe_grounding_dino_451265`, `name: ebe_oakd_live`, `bus.enabled: true`, `source.type: oak_d`).
- **Qué corregir y dónde:** el informe y los índices **no deben** clasificar corridas por `scenario`/`run_id`; usar `source_type` (`run_descriptor.source_kind`) + `bus.enabled`. Dejarlo dicho en `docs/13-glosario` (DBE/EBE) y en el README del repo (o derivar `scenario` en `RunSection` — cambio de código, fuera de este relevamiento).

### C-3 · MEDIA — `effective_config.yaml` de un run GDINO imprime `confidence_threshold: 0.25` e `iou_threshold: 0.5` (y uno YOLOE imprime `box_threshold: 0.35`)
- **Qué dice el doc:** pase 3: "box_threshold real del campeón = 0,30; `confidence_threshold` es del carril YOLOE".
- **Qué hay en el código:** `ModelSection` es un schema **plano** con los campos de ambas familias (`schemas.py:431-440`), así que el dump efectivo lleva los defaults inertes de la otra familia. Un lector del artefacto puede citar 0,25 para GDINO o 0,35 para YOLOE. Confirmado: run campeón → `box_threshold 0.3, text 0.25, image_size 560, confidence_threshold 0.25, iou_threshold 0.5`; runs YOLOE → `box_threshold 0.35` (inerte), `confidence_threshold 0.25` (el real, `models/__init__.py:53`). Nota: `iou_threshold` **sí** es real para GDINO (NMS por clase canónica, `grounding_dino_adapter.py:23-47`).
- **Qué corregir y dónde:** regla de lectura en `docs/13-glosario` §4 o en el kit: "GDINO: `box_threshold`+`text_threshold`+`iou_threshold`; YOLOE: `confidence_threshold`+`iou_threshold`; el resto es default inerte".

### C-4 · MEDIA — Tres conteos de tests distintos y ninguno vigente
- **Docs:** `docs/implementation-status.md:196` "646 pruebas (collect-only 2026-07-29)"; `docs/operacion/97:52` "641 passed, 5 skipped" (2026-08-05); CLAUDE.md raíz no cita cifra para este repo (bien).
- **Código:** 643 `def test_` por grep al HEAD; `d40b3bd` (08-17) agregó tests después de ambas cifras. El total colectado hoy es desconocido sin correr pytest (prohibido acá).
- **Corregir:** si el informe cita "2.203 tests" (op97, memoria) debe fecharlo (2026-08-05) o re-medir; no citar 646 como actual.

### C-5 · MEDIA — "`report.json`" y "`metrics.json`" no existen en el media-plane
- **Doc:** `docs/informe/ajustes` AJ-2.09: "Bitácora mínima por corrida ≈ `report.json` consolidado + `effective_config`, ya cubierta"; contexto-base FIG-B cita `results/clip_bench/r*/metrics.json` (eso es experimental-setup, correcto).
- **Código:** los artefactos del plano son `summary.json` (`media.summary.v2`) + `metrics.jsonl` (`media.metric.v2`) + `run_manifest.json` (B23). `report.json` es del control-plane/experimental-setup.
- **Corregir:** en §17.4 (qué se instrumentó) nombrar `summary.json`/`metrics.jsonl` para el plano de medios; reservar `report.json` para el consolidado del experimento.

### C-6 · MEDIA — G2A del código ≠ G2A del protocolo (§17.1.7.7): no incluye captura de sensor ni transporte de red
- **Protocolo:** G2A = t_capture + t_transport + t_preprocess + t_inference (Tabla 33, los cuatro "Obligatorio").
- **Código:** `g2a_ms` arranca en `capture_monotonic_ns`, estampado **cuando el proceso ya leyó el frame** (`visual_unit.py:19-23`: "Instante en que el PROCESO leyó la unidad"), y cierra al fin de la inferencia (`pipeline.py:242`). Cubre: espera en cola productor→consumidor (transport in-process), normalización, inferencia. **No** cubre: exposición/lectura del sensor, RTP/red, decodificación (ocurren antes del `cap.read()`/`tryGet()`). El tramo sensor→dequeue sólo existe para OAK-D (`capture_to_host_ms`); **RTSP no tiene medida equivalente**.
- **Estado en docs:** ya declarado como F-101.8 (doc 101, contexto-base:364, doc 128) — la divergencia está **reconocida**, pero el informe debe decir además que para RTSP el tramo faltante **no se midió** (no sólo "hay que sumar 202–217 ms", que es OAK-D).

### C-7 · BAJA — Nomenclatura `request_stop()`
- **Doc:** CLAUDE.md raíz: "Las fuentes de red exponen `request_stop()`".
- **Código:** fuentes → `stop()` (`sources/base.py:28`; `rtsp_source.py:71`; `oak_d_source.py:298`); `request_stop()` → `RunControl` (`pipeline.py:413`), que delega en `source.stop()`. En el control-plane `BusSource.request_stop()` sí existe.
- **Corregir:** CLAUDE.md raíz "Trampa de concurrencia": "… `RunControl.request_stop()` en el media-plane / `BusSource.request_stop()` en el control-plane; ambas terminan en `source.stop()` cooperativo".

### C-8 · BAJA — README lista alias de adaptadores en vez de los ids canónicos
- `README.md` "Adaptadores soportados": `grounding_dino_hf`, `yoloe_ultralytics`. Catálogos y mensaje de error usan `grounding_dino`, `yoloe` (`models/__init__.py:33,48,69`). Corregir la tabla del README.

### C-9 · BAJA — `run_manifest.json` no registra hardware ni entorno de software
- Protocolo §17.1.7.8.1 exige declarar hardware y entorno. El manifest sólo tiene `code_version` (git short hash), fechas, archivos (`run_artifact_writer.py:290-310`); `summary.json` agrega `device` y `gpu_memory_peak_mb`. No hay nombre de GPU, versión de torch/transformers/driver, hostname. Ver D.

### C-10 · BAJA — Dockerfile CUDA 12.4 + ruedas cu13 pineadas; builds sin ejecutar
- `infra/docker/Dockerfile:2` `nvidia/cuda:12.4.1-runtime-ubuntu22.04`; `constraints.txt` pinea `torch==2.12.1` con `nvidia-cuda-runtime==13.0.96`, `nvidia-cudnn-cu13`, etc. Funciona sólo si el driver del host soporta CUDA 13 (las ruedas traen su runtime). Doc 128 §1 ya marca "builds + smoke integral PENDIENTES". No es contradicción, es riesgo no verificado.

### C-11 · BAJA — Glosario §6 "Repos de código" lista 4 repos y omite `e-ovrt_alert-distribution`
- `docs/13-glosario…:252` vs la misma tabla `:254` que sí lista el puerto `:8082`. No es del media-plane, se anota porque salió en la verificación del §6.

### C-12 · BAJA — Percentiles con método mixto y `capture_to_host` sin p99/avg
- `metrics/g2a.py:77-80`: `p50 = statistics.median` (interpola) mientras p95/p99 son por índice `int(n·p)`; `capture_to_host` sólo p50/p95 (`run_artifact_writer.py:214-218`). Con n chico (15 muestras en el run del 08-18) p95 = p99 = 1614,3 ms. El informe debería declarar el método (percentil por índice, sin interpolación) cuando cite P95/P99.

### C-13 · BAJA — "Un run activo" omite que una **preview** también bloquea
- `service/activity_slot.py:1`, `run_manager.py:118`: `SlotBusyError` si hay preview → 409. Docs (README, glosario) sólo dicen "un run activo a la vez". Agregar el matiz donde se describa la operación desde la consola.

---

## D) Protocolo §17.1 vs construido (sólo lo que toca al media-plane)

| § | Prescripción | Veredicto | Evidencia / qué falta |
|---|---|---|---|
| 17.1.4.2.1 | CPN: HP Victus RTX 4060 8 GB, **Windows 11** | **DESVIADA** | El código corre en Linux (WSL2) y Docker Ubuntu (`Dockerfile`); no hay rama Windows. El repo no registra el SO en los artefactos (C-9); la evidencia de WSL está en memoria/ops, no en el repo |
| 17.1.4.2.2 | NVDEC para decodificar H.264/H.265 en GPU | **NO EJERCIDA** | RTSP/video por `cv2.VideoCapture` (software) — `rtsp_source.py:45-47`, `video_file_source.py`; grep `nvdec|cudacodec|hwaccel|CAP_PROP_HW` en `src/` = 0 resultados |
| 17.1.4.2.3 | EN = OAK-D Pro PoE candidata; captura + preprocesamiento liviano; inferencia en borde sólo como variante condicionada | **CUMPLIDA** | `sources/oak_d_source.py` (DepthAI v2, extra `edge`), `df5f7c7`; variante EN-2 opcional default off (`schemas.py:161`) medida por separado (87 % drop, doc 10 E-07) |
| 17.1.4.2.4 | Contingencia: cámara IP CCTV por RTSP | **CUMPLIDA** (implementada, y usada: 21 runs `rtsp` locales) | `sources/rtsp_source.py`, plugin `rtsp` (`registry.py:36`), `reconnect_retries=5`/`reconnect_delay_ms=1000` (`schemas.py:209-210`) |
| 17.1.4.2.5 | Stack: Grounding DINO y YOLOE con frameworks oficiales, GPU NVIDIA | **CUMPLIDA** | Transformers (`grounding_dino_adapter.py:85`) y Ultralytics (`yoloe_adapter.py`); `constraints.txt` torch 2.12.1 cu13 |
| 17.1.4.3.3 | Checkpoints exportados a "PyTorch nativo, TensorRT u ONNX" | **PARCIAL** (sólo PyTorch nativo) | catálogos FT `yoloe-26s-ft-t1/t2.yaml` → `weights: models/yoloe/finetuned/t{1,2}/best.pt`; sin ONNX/TensorRT en el repo |
| 17.1.4.4 | Escenario A (DBE, archivos) y B (EBE, live LAN) | **CUMPLIDA** (con C-2) | fuentes `image_folder`/`video_file` vs `rtsp`/`oak_d`; bus para EBE (`bus.enabled`). Pero el campo `scenario` no lo refleja (C-2) |
| 17.1.4.5 / Tabla B.6 | Parámetros de referencia (≈640 px, fps, transporte) | **PARCIAL / DESVIADA en resolución** | YOLOE `image_size: 640` ✅; GDINO 800 (default HF) y **560** (campeón) — el propio protocolo (§17.1.7.7.5) exige recalibrar umbrales si la resolución difiere de 640; `rate_control.stride` y `source.fps` (OAK-D default 10, `schemas.py:224`) configurables |
| 17.1.4.6 | Restricción VRAM 8 GB | **CUMPLIDA** (instrumentada) | `gpu_memory_peak_mb` en summary (`pipeline.py:615`), fp16 default (`schemas.py:375`) |
| 17.1.5.4.2 | Eje "composición del vocabulario": evaluar cada prompt **en aislamiento y en contexto completo** | **PARCIAL** | El mecanismo existe (`active_ids`, B39); la matriz aislado-vs-completo como tal no está en el repo (vive en experimental-setup/results si se ejecutó). No verificable acá |
| 17.1.5.4.2 | Variantes con template ("a photo of a [CLASS]") | **NO EJERCIDA** (en este repo) | `PromptClass.phrasings` por backend (`schemas.py:30`) permite frases arbitrarias, pero no hay mecanismo de template ni set con template; el congelado `cr01_cr02_v2_short` usa etiquetas cortas (`person`, `helmet`, `vest`) |
| 17.1.5.4.2 | Estrategias directa vs indirecta | **CUMPLIDA** (soporte) | `PromptClass.strategy`, `condition_id`, `role` (`schemas.py:26-28`); `PromptPhrase.strategy/condition_id` (`prompt_plan.py:21-22`); sets `edir_v1`/`eind_v1` en experimental-setup |
| 17.1.5.4.2 Fase 2 | Hiperparámetros (umbral, NMS) **constantes** entre variantes de prompt | **CUMPLIDA dentro de un catálogo / DESVIADA entre 800 y 560 de tiny** | catálogo fijo por modelo; overrides quedan en `effective_config`; **C-1** |
| 17.1.5.4.3 | Prompts primarios en **inglés** | **CUMPLIDA** | `PromptSet.language` (`schemas.py:44`); `cr01_cr02_v2_short.yaml` `language: en`; GDINO caption `". ".join(texts) + "."` (`grounding_dino_adapter.py:121`) |
| 17.1.5.4.3 | Línea complementaria en español / traducción automática | **NO EJERCIDA** | sin mecanismo ni set en español |
| 17.1.7.7.1–4 | G2A = t_capture + t_transport + t_preprocess + t_inference | **DESVIADA (declarada)** | C-6: G2A del código = dequeue → fin de inferencia; `capture_to_host_ms` cubre sensor→dequeue **sólo OAK-D**; RTSP sin ese tramo. `DetectionEventTiming` desglosa `normalize_ms/inference_ms/postprocess_ms/write_ms/total_ms` (`events.py:34-42`) — no hay `t_transport` de red explícito |
| 17.1.7.7.5 | Presupuesto 50–250 ms; veredicto | **CUMPLIDA** (instrumentado) | `g2a.py:13-14,81` (`p95_within_budget`); ejemplo live: p95 1614 ms → `False` |
| 17.1.7.8.1 | Declarar modelo, versión, checkpoint, resolución, **hardware, entorno de software**, suministro de video, umbral, NMS, vocabulario activo | **PARCIAL** | ✅ `effective_config.yaml` (modelo ref, device, thresholds, image_size, fp16, source, prompts resueltos), `run_provenance.json` (dataset/vocabulario/fingerprint), `code_version`; ❌ **hardware/GPU, versiones de torch/driver/SO, hostname** no se registran (C-9) |
| 17.1.7.8.1 | Timestamps monotónicos, fuente temporal declarada | **CUMPLIDA** | `time.monotonic_ns` / `perf_counter` (`visual_unit.py:23`, `timers.py:38-71`); `source_clock` por fuente (B26); two-node declarado no interpretable (B22) |
| 17.1.7.8.1 | Cinco hitos por alerta (primera evidencia, candidato, confirmado, alerta, notificación) | **N/A al media-plane** (aporta el 1º) | el plano emite `capture_monotonic_ns`/`capture_wallclock_ms` por unidad (`metrics.py:18-19`) para el join por `unit_id`; los hitos de patrón/alerta son del control-plane |
| 17.1.7.8.1 | **Período de calentamiento previo** | **PARCIAL** | Tres mecanismos: (1) `runtime.warmup=True` inferencia dummy al cargar (`schemas.py:376`, `grounding_dino_adapter.py:97-99`); (2) `prepare_run` pre-flight por corrida (`b37d550`); (3) `run.warmup_units` excluye unidades de los percentiles G2A y **se declara** en `summary.g2a.warmup_units` (`schemas.py:133`, `g2a.py:61`). **Pero** `warmup_units` default 0 y **= 0 en los 472 runs locales**; `source.warmup_frames` (lente) sí se usó (5 en el run live del 08-18). El informe debe decir: warm-up de modelo sí (carga + pre-flight), exclusión de muestras iniciales **no** |
| 17.1.7.8.1 | P50/P95/P99 + promedio | **CUMPLIDA** (con C-12) | `summary.json`: `avg/p50/p95/p99_latency_ms` y `g2a.{avg,p50,p95,p99}_ms` (`run_artifact_writer.py:255-258`, `g2a.py:77-80`); `capture_to_host` sólo p50/p95 |
| 17.1.7.8.2 | Sobre imágenes estáticas no medir métricas temporales; declarar no aplicable | **CUMPLIDA** | `source_clock="none"` en `image_folder` (ADR-013); `G2ASummary.state` ∈ {computed, applicable_not_computed, not_interpretable} con `causes` (`g2a.py:45-68`) |
| 17.1.7.8.4 | Bitácora mínima: identificación, modelo, entrada, parámetros, hardware, entorno, temporalidad, logs | **PARCIAL** | todo salvo hardware/entorno (C-9); logs crudos = `detections.jsonl`, `metrics.jsonl`, `errors.jsonl`, `dropped_units.jsonl` |

---

## E) Hechos citables sobre este repo (con comando de re-verificación)

1. **Campeón:** `grounding-dino/gdino-tiny-560` = checkpoint `IDEA-Research/grounding-dino-tiny`, letterbox **560×560**, `box_threshold 0,30`, `text_threshold 0,25`, NMS por clase canónica IoU 0,50, fp16 autocast en CUDA, warm-up al cargar.
   `grep -E '^(model_id|box_threshold|text_threshold|image_size):' configs/models/grounding-dino/gdino-tiny-560.yaml; grep -n 'half_precision: bool\|warmup: bool\|iou_threshold: float' src/eovrt_media/config/schemas.py`
2. **El 800 px de tiny usa otro umbral (0,35):** `grep box_threshold configs/models/grounding-dino/gdino-tiny.yaml configs/models/grounding-dino/gdino-tiny-560.yaml`
3. **Catálogo activo = 11 refs** (1 mock, 4 GDINO, 4 YOLOE originales, 2 YOLOE fine-tuned T1/T2); MM-GDINO archivado 2026-08-19.
   `find configs/models -name '*.yaml' | sort; ls configs/_archive/mm-grounding-dino/`
4. **Servicio :8080, un modelo por proceso (`EOVRT_MODEL_REF` obligatorio), un run activo (409), preview y run excluyentes.**
   `grep -n 'EOVRT_MODEL_REF es obligatorio' src/eovrt_media/service/settings.py; grep -n 'status_code=409' src/eovrt_media/service/routers/runs.py; head -1 src/eovrt_media/service/activity_slot.py`
5. **Endpoints:** `GET /healthz`, `GET /readyz`, `GET /api/model`, `POST/GET /api/runs`, `GET/DELETE /api/runs/{id}`, `POST …/stop`, `GET …/detections`, `GET …/dropped`, `GET …/artifacts/{path}`, `POST/GET …/evaluate`, `WS /api/runs/{id}/stream`, `POST/GET/DELETE /api/preview`, `WS /api/preview/stream`, `GET /api/catalog/ingest-plugins`, `GET /api/catalog/datasets`.
   `grep -rn '@router\.' src/eovrt_media/service/routers/`
6. **Fuentes:** `image_folder` (no recursivo), `video_file` (alias `video`, `video_frame`), `rtsp`, `oak_d`; vivas = rtsp, oak_d.
   `sed -n '34,47p' src/eovrt_media/sources/registry.py; sed -n '53,54p' src/eovrt_media/sources/image_folder_source.py`
7. **Bus media→control:** off por default; XPUB `tcp://0.0.0.0:5557`, HWM 1000, msgpack `bus.envelope.v1`, topics `media.detection.v1.<run_id>` / `run.lifecycle.v1.<run_id>`, `seq` monótono incrementado aunque se descarte, `NOBLOCK`, payload byte-idéntico al JSONL, `run_finished` al cierre.
   `sed -n '361,369p' src/eovrt_media/config/schemas.py; sed -n '19,22p;127,138p' src/eovrt_media/transport/bus.py; sed -n '42,52p' src/eovrt_media/service/bus_writer.py`
8. **G2A:** `g2a_ms = monotonic_ns(fin de inferencia) − capture_monotonic_ns(construcción del VisualUnit tras el dequeue)`; presupuesto 50–250 ms sobre P95; `None` en two-node; `capture_to_host_ms` (sensor→host) sólo OAK-D vía `dai.Clock.now() − msg.getTimestamp()`.
   `sed -n '237,254p' src/eovrt_media/runtime/pipeline.py; sed -n '19,27p' src/eovrt_media/contracts/visual_unit.py; sed -n '430,434p' src/eovrt_media/sources/oak_d_source.py`
9. **Warm-up:** `runtime.warmup=True` (dummy al cargar) + `prepare_run` pre-flight; `run.warmup_units` default 0 (y 0 en todos los runs locales); `source.warmup_frames` default 0, sólo fuentes vivas, descarta en la fuente.
   `grep -n 'warmup' src/eovrt_media/config/schemas.py`
10. **EN-2 prefilter:** `OakDPrefilterConfig.enabled=False`, blob `person-detection-retail-0013_6shave.blob`, confidence 0,25, keepalive 1500 ms, heartbeat 2000 ms, fail-open a 3000 ms de silencio; fail-fast si falta el blob; sólo `oak_d`.
   `sed -n '155,176p;251,252p' src/eovrt_media/config/schemas.py`
11. **Artefactos por run:** `run_config.yaml`, `effective_config.yaml`, `run_manifest.json`, `detections.jsonl` (`media.detection.v1`), `metrics.jsonl` (`media.metric.v2`), `errors.jsonl`, `dropped_units.jsonl` (lazy), `summary.json` (`media.summary.v2`), `run_provenance.json`, `previews/`, `annotated.mp4` (opt), `eval_perception.json` (post-eval). **No** `report.json`/`metrics.json`.
   `grep -rn -o -E '"[a-z_]+\.(jsonl|json|yaml|mp4)"' src/eovrt_media/sinks src/eovrt_media/service | sort -u`
12. **Herramientas:** `python -m eovrt_media.tools.{evaluate,inspect_runs,preannotate_video,run_node,videogt}`; `evaluate` restringe GT al run por default.
    `ls src/eovrt_media/tools/; grep -n restrict_gt_to_detections src/eovrt_media/tools/evaluate.py`
13. **Docker:** `infra/docker/Dockerfile` (CUDA 12.4 runtime + Python 3.11, `EXPOSE 8080`, healthcheck `/readyz`, `EOVRT_MODEL_REF=mock` default); standalone `infra/docker-compose.yml` publica 8080 y 5557; el integral (`experimental-setup/infra/platform`) levanta 9 instancias `mp-*` bajo profile `models` sin publicar 5557.
    `sed -n '1,3p' infra/docker/Dockerfile; grep -n '^  mp-' ../e-ovrt_experimental-setup/infra/platform/docker-compose.yml`
14. **Versiones:** torch 2.12.1 · transformers 5.12.1 · ultralytics 8.4.86 · pyzmq 27.1.0 · msgpack 1.2.1 · fastapi 0.139.0 · depthai 2.32.0 (venv) · Python 3.12.13 (venv) / 3.11 (Docker).
    `grep -E '^(torch|transformers|ultralytics|pyzmq|msgpack|fastapi)==' constraints.txt; .venv/bin/python --version`
15. **Tests:** 643 funciones `def test_` en 81 archivos al HEAD `f439db2` (conteo estático; el colectado incluye parametrizaciones).
    `grep -rh 'def test_' tests/ | wc -l; ls tests/test_*.py | wc -l`
16. **Estado git:** `feature/inference-service` @ `f439db2` (2026-08-22), árbol limpio, sin CI.
    `git -C e-ovrt_media-plane status --short; git -C e-ovrt_media-plane log -1 --format='%h %ad' --date=short`

---

## F) No pude verificar (restricciones de lectura / fuera del repo)

- **Conteo real de tests colectados/pasados hoy** (pytest prohibido). Sólo el conteo estático (643).
- **Que la comparación 800↔560 de doc 61/64 haya controlado el umbral** (C-1): sólo verifiqué que los catálogos y los runs locales del 07-23 difieren en `box_threshold`; no leí doc 61/64 para ver si se aplicó un override o si la conclusión ya lo declara.
- **Cifras numéricas de latencia del informe** (14,7 ms p50, 31,8 p95, 630–890 ms live, 202–217 ms `capture_to_host`): vienen de `experimental-setup/results/`; acá sólo confirmé el mecanismo y un run local de ejemplo (`run_20260818_002811…`: g2a p50 723,6 / p95 1614,3 ms; capture_to_host p50 202,1 / p95 255,3 ms, n=15).
- **`bus_dropped_events = 0` en las 6 corridas del rodaje** (doc 128 §1): es un contador del control-plane; no revisé sus artefactos.
- **Build de la imagen Docker y compatibilidad CUDA 12.4 (imagen) vs ruedas cu13** (C-10): doc 128 ya lo marca pendiente; no se puede construir acá.
- **Que el SO del CPN haya sido WSL2 en todas las corridas** (D, §17.1.4.2.1): el repo no registra SO/hardware por run (C-9); la evidencia está en memoria/ops.
- **Matriz aislado-vs-contexto-completo y variantes con template** (§17.1.5.4): si se ejecutaron, están en experimental-setup/results, no en este repo.
- **`docs/operacion/97` §3–§4 y `128` §2–§5** más allá de lo citado: sólo leí lo pedido (tabla de suites, §2.2, §1 del acta).
