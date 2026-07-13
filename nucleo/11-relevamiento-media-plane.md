# Relevamiento: e-ovrt_media-plane (estado 2026-07-09)

- **Fecha:** 2026-07-09
- **Repo:** `e-ovrt_media-plane` (remote `simonll4/e-ovrt_media-plane`)
- **Rama actual:** `feature/inference-service` — 2 commits adelante de origin
  (Fase 2 two-node) **+ 13 archivos modificados sin commitear** (la novedad de este
  relevamiento, ver §8).
- **Tamaño:** ~7.5k líneas en `src/`, 63 archivos de test (~380 tests al merge de Fase 1).
- **Rol en el set:** completa el hueco del set 00–10 (solo existía relevamiento del
  control-plane, doc 01).

## 1. Qué es hoy

Servicio de inferencia OVD **config-driven** (FastAPI, HTTP/WS). Desde el pivote de
Fase 1 (Spec A, 2026-07-01) **no es un CLI**: el modelo se carga una vez al arranque
(`EOVRT_MODEL_REF`), una corrida se dispara por `POST /api/runs` (un run activo por
vez) y los ex-subcomandos viven en `eovrt_media.tools.*`. Materializa el "Pipeline de
Medios" de Etapa 3: ingesta → rate-gate → normalización → inferencia → postproceso →
persistencia, sin lógica de riesgo (los patrones son del control-plane).

## 2. Historia de ramas (para leer el repo)

```
main ← feat/ebe-fuente-viva (PR#1: RTSP fuente viva, gates fp16, validación two-node JPEG)
     ← feat/infra-deploy (organización infra, edge sin torch)
     ← feature/inference-service (ACTUAL: servicio Fase 1 + two-node Fase 2 + visibilidad)
```

Todo el contenido de las ramas anteriores está incluido en `feature/inference-service`.

## 3. Superficie de API (relevada de `service/routers/`)

| Endpoint | Función |
|---|---|
| `GET /healthz` · `GET /readyz` | Salud / modelo cargado. |
| `GET /api/ingest-plugins` · `GET /api/datasets` | Catálogos de plugins de ingesta y datasets. |
| `GET /api/model` | Modelo activo del servicio. |
| `POST /api/runs` | Dispara corrida (manifiesto: ingest plugin + prompts ref/inline). |
| `GET /api/runs` · `GET /api/runs/{id}` | Listado / estado+summary (con `live`, ver §8). |
| `POST /api/runs/{id}/stop` · `DELETE /api/runs/{id}` | Stop / borrado. |
| `WS /api/runs/{id}/stream` | Eventos en vivo (resúmenes coalescidos, no eventos completos — por eso el bus del doc 05 es otra pieza). |
| `GET /api/runs/{id}/detections` | Detecciones del run por HTTP. |
| `GET /api/runs/{id}/artifacts/{path}` | Sirve artefactos del run (la webconsole lee por acá). |
| `POST/GET /api/runs/{id}/evaluate` | Evaluación BENCH (AP@0.5 / recall CR-01 / mAP50) por HTTP. |

## 4. Módulos (mapa actual)

- `config/` — loader de dos raíces (catálogos del plano + experimento en
  `e-ovrt_experimental-setup`), `PromptPlan`, schemas. Novedad menor: el override del
  catálogo es solo `EOVRT_MEDIA_CATALOG_ROOT`/parámetro (el flag `--catalog-root`
  murió con el CLI).
- `contracts/` — `VisualUnit` → `RawDetection` → `Detection` → `DetectionEvent`
  (`media.detection.v1`) / `MetricSample` (sin cambios: la compatibilidad con el
  control-plane verificada el 2026-07-06 sigue vigente).
- `sources/` — `ImageFolderSource`, `VideoFileSource` (decodificación secuencial,
  commit `a2672ef`), `RtspSource` (wall-clock + reconexión), `OakDSource` (implementada 2026-07-13: DepthAI v2, IP fija, wall-clock,
  reconexión, stop cooperativo).
- `models/` — adaptadores GDINO / YOLOE / mock vía `BaseDetectorAdapter`; device auto.
- `runtime/` — `pipeline.py` (single-host: productor+consumidor sobre
  `MemoryTransportAdapter`), `two_node.py` (nodo A edge / nodo B GPU sobre ZeroMQ
  REQ/REP + heartbeat), `two_node_local.py` (**deshabilitado permanente**; conserva
  solo los helpers de generación de config por decisión de spec de Fase 2).
- `transport/` — base/factory/memory/network (ZeroMQ REQ/REP, msgpack, rate_gate).
  Sigue siendo el patrón a espejar para el bus PUB/SUB del doc 05.
- `service/` — app, routers, `RunManager`, `retention.py` (GC + reconciliación de
  huérfanos), `events.py` (`EventBroadcaster` + `EventEmittingArtifactWriter` para el
  WS — el seam donde se decora el `BusPublishingArtifactWriter` del doc 05).
- `sinks/` — `RunArtifactWriter` (detections/metrics/errors/summary/previews +
  provenance + manifest), `jsonl_sink` (con `atomic_write_json`), y
  **`video_annotation_writer.py`** (ver §7 — hallazgo relevante).
- `tools/` — `evaluate`, `inspect_runs`, `debug_run` (ruta two-node local
  deshabilitada), y **`run_node.py`**: entrypoint two-node
  (`python -m eovrt_media.tools.run_node --role {a|b} --config <run.yaml>`, exit
  codes 0/1) — ENTRYPOINT de los contenedores de `infra/twonode/` y el punto de
  enganche natural para el runner paraguas de experimental-setup (decisión D4).
- `infra/` — deploy standalone (`infra/docker/`) y split two-node (`infra/twonode/`,
  Fase 2 completada; imágenes separadas edge-sin-torch / GPU).

## 5. Flujo de ejecución

- **Single-host:** `POST /api/runs` → `RunManager` → `execute_run()`: hilo productor
  (read → rate-gate → normalize) + hilo consumidor (inferencia → postproceso →
  write), acoplados por transporte en memoria.
- **Two-node (EBE):** Nodo A (`run_node_a`: ingesta + rate + normalización + servidor
  ZeroMQ REP) → red → Nodo B (`run_node_b`: cliente REQ + inferencia + artefactos).
  El run config declara `topology.mode: two_node`. **Nodo B comparte `runs_dir` con
  el servicio**, lo que motivó la reconciliación de ownership de §8.

## 6. Estado de verificación

- Fase 1 (servicio): merge con 380 tests + review whole-branch (hardening: redacción
  de credenciales RTSP, run_id sanitizado, etc.).
- Fase 2 (two-node Docker): verificada 2026-07-06 con mock; run GPU real pendiente
  (sin GPU/pesos en el entorno de build).
- Validaciones previas en ramas: BENCH gate fp16 (GDINO + YOLOE) y transporte
  two-node JPEG (ZeroMQ transparente; efecto JPEG en marginales) — commits
  `a3f3352`/`db9d563`.
- **Visibilidad two-node end-to-end validada 2026-07-06** (3 escenarios, §8).

## 7. Hallazgo para el doc 09: el overlay renderer ya está a medio construir

`sinks/video_annotation_writer.py` + `visualize.py` ya implementan: anotación de
frames con detecciones (`annotate_payload_bgr`), ensamblado a `.mp4` (cv2 `mp4v`) y
**transcodificación a H.264 yuv420p vía ffmpeg** para reproducción en navegador, con
FPS inferido de `timestamp_ms`. Lo que falta para los videos V1–V3 de la defensa es
la capa de composición del control-plane: estados de patrón (`pattern_events.jsonl`),
alertas (`alerts.jsonl`) y timeline TTFD/t_alert. **La estimación del doc 09 §6.3
(1–2 días desde cero) baja a ~1 día de extensión** reutilizando esta pieza.

## 8. Novedades sin commitear (2026-07-06/09) — el motivo de este relevamiento

Implementan la spec `2026-07-06-webconsole-twonode-visibility-design.md` (vive en
`e-ovrt_experimental-setup/docs/superpowers/specs/`): hasta ahora, un run two-node
era invisible o quedaba corrupto para el servicio/webconsole. Cambios:

1. **Finalización garantizada de `run_node_b`** (`runtime/two_node.py`): toda corrida
   two-node termina con `summary.json` estampado con `status: succeeded|failed` y
   `error` explícitos (read-modify-write atómico, mismo patrón que
   `RunManager._finalize`), incluso ante excepción — que se re-lanza tras finalizar.
2. **Runs de otros procesos visibles en la API** (`service/run_manager.py`): campo
   `live: true|false` en get/list (distingue el run activo del servicio de los
   leídos de disco); un directorio con `effective_config.yaml` pero sin
   `summary.json` se reporta `status: "running"` en vez de 404 — así el servicio
   expone corridas two-node en curso lanzadas por `run_node_b` externo.
3. **Ownership en la reconciliación de huérfanos** (`service/retention.py`): al
   arrancar, el servicio reconcilia runs huérfanos (proceso muerto sin finalizar),
   pero ahora **excluye** los runs cuyo `effective_config.yaml` declara
   `topology.mode: two_node` — pueden estar vivos en otro proceso y estampárselos
   como `interrupted` los corrompería.
4. **Validación E2E de los 3 escenarios** (documentada en `infra/twonode/README.md`)
   contra servicio real + BFF de la webconsole: (a) run mock exitoso → `succeeded`,
   `live: false`, `topology: two_node` en la consola; (b) kill de `node-a` a mitad de
   corrida → transición en vivo `running` → `failed` con error legible ("Nodo A no
   respondió en 10000 ms…", **sin reintento automático**); (c) restart del servicio
   con un run two-node en vuelo (congelado con `docker compose pause`) → NO fue
   estampado como interrumpido y la consola lo mostró `running`; al despausar terminó
   `succeeded` solo.
5. Limpiezas documentales: `two_node_local` declarado deshabilitado permanente (sin
   puente al despliegue Docker); referencias `--catalog-root` eliminadas.

**Estado git:** todo esto está en el working tree de `feature/inference-service`
(ahead 2 de origin, sin push). Riesgo operativo: trabajo valioso sin commitear ni
respaldar — mismo señalamiento que H10 del doc 07 para `/docs`.

## 9. Impacto sobre el set de documentos (aplicado en esta actualización)

1. **Doc 05 (bus media→control):** la semántica de fin/estado de corrida que el bus
   necesitaba (`run_finished`, pregunta abierta §10.3) ahora tiene soporte concreto:
   `summary.json` con `status` garantizado (también en two-node) + `GET /api/runs/{id}`
   con `running`/`live`. El `BusSource` del control-plane puede cerrar corrida por
   señal del bus **o** por polling de estado como fallback. ✎ Nota agregada.
2. **Doc 09 (defensa):** overlay renderer re-estimado como extensión de
   `VideoAnnotationWriter` (§7). ✎ Nota agregada.
3. **Doc 02 §3 (estado real):** la fila de webconsole/EBE queda más fuerte — la
   consola ya muestra corridas two-node con ciclo de vida correcto, validado E2E.
   ✎ Nota agregada.
4. **D4 (runner paraguas):** `tools/run_node.py` es el entrypoint que el runner de
   experimental-setup debe orquestar junto con `POST /api/runs` — el spec de D4 ya
   tiene sus dos puntos de enganche concretos.
