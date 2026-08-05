# 56 — Relevamiento integral de la plataforma (2026-07-18)

> ## ✎ FOTO HISTÓRICA — REEMPLAZADO POR EL DOC 97 (2026-08-05)
>
> **No citar el cuerpo de este documento como estado actual de la plataforma.** Es la
> foto verificada al **2026-07-18**; desde entonces entraron 85 commits en los 4 repos.
> Lo que quedó superado, en concreto:
>
> - GT de video `gt_preliminary` → **`gt_ready`** con adjudicación humana (doc 80).
> - BENCH v2 (196 imgs) → **`bench_v3`** (6.477 imgs, 3 fuentes independientes).
> - Métrica estrella `cb_b01_p7` (1 clip) → **34 clips, 13 campañas** con GT humano.
> - Solo granularidad de escena → **G1 por sujeto**, verificada en vivo (doc 91).
> - Solo ausencia espacial → **4 estrategias de evidencia, 3 implementadas**.
>
> **Las cifras de §9 están superadas en su totalidad.** La fuente vigente de estado es
> `docs/operacion/97`; la de cifras, `e-ovrt_experimental-setup/results/index.md`.

- **Fecha:** 2026-07-18
- **Tipo:** relevamiento consolidado / memoria de implementación
- **Reemplaza como punto de entrada a:** doc 50 (reporte del tramo) y complementa al doc 55
  (guía de continuación). **Este documento es la foto completa y verificada de la
  plataforma al 2026-07-18** — insumo directo para el informe final (serie 90-).
- **Método:** relevamiento exhaustivo en paralelo de los 4 repos de código + auditoría
  del propio repo `docs` contra la realidad (5 agentes, verificación por lectura de
  código y git, no por memoria).

---

## 0. Resumen ejecutivo

La plataforma está **completa, integrada y probada E2E** en sus dos caminos (DBE offline
por archivo, EBE live por bus ZeroMQ), con el laboratorio de GT temporal de video
operativo y una consola web rediseñada que hoy es la superficie de gestión primaria
(ADR-009). Desde el doc 50 (07-10/11) se sumaron **seis bloques de capacidad** que ningún
doc anterior a este cubre completos:

1. **OAK-D Pro PoE como fuente viva** + **prefilter EN-2 on-device** (opcional,
   fail-open) + métrica `capture_to_host_ms` (media-plane, 07-13/15).
2. **Ledger por-frame de descartes** `media.dropped_unit.v1` + endpoint `/dropped`
   (media-plane, 07-17).
3. **Progreso parcial de patrones** (`control.pattern_progress.v1`) + lookup por
   `media_run_id` + `received-units` (control-plane, 07-17).
4. **Rediseño completo de la webconsole** (tokens + kit UI + shell) y **vista
   correlacionada media↔control** por `unit_id` (detecciones, bboxes, descartes,
   progreso 0-100 % de patrones, alertas) (experimental-setup, 07-17).
5. **Borrado orquestado de runs** (webconsole → control primero, media al final;
   `DELETE /api/runs/{id}` nuevo en el control-plane) (07-18).
6. **Sesiones de preview en vivo** para posicionar cámaras y probar prompts sin corrida
   persistida: `PreviewManager` + `/api/preview` + WS en el media-plane, ventana
   **Cámaras** (CamerasPage + LiveViewer canvas) en la consola (07-18).

Además el laboratorio GT dio su **primera vuelta E2E real con clip nuevo**
(`video16_clip10`: GT preliminar → corrida GDINO/YOLOE/alt-prompts → evaluación
temporal), aunque **ningún GT de video tiene todavía pasada humana**.

**Riesgos operativos hoy:** (a) 18 commits sin pushear en 3 repos (§5); (b) presets de
cámara con **credenciales RTSP en texto plano** que no estaban git-ignoradas (§7 —
mitigado en este relevamiento agregando `cameras/` al `.gitignore`); (c) contradicción
documental EN-2 en informe/93 (corregida, §6).

---

## 1. Estado de los repos (verificado 2026-07-18)

| Repo | Rama | HEAD | vs origin | Working tree |
|---|---|---|---|---|
| `e-ovrt_media-plane` | `feature/inference-service` | `eddeb89` (preview en vivo) | **ahead 2** | fix latencia RTSP en preview, terminado con test de regresión, **sin commitear** |
| `e-ovrt_control-plane` | `feature/control-service` | `a53e95e` (DELETE /api/runs) | **ahead 1** | 3 configs replay `video16_clip10*` untracked (experimento comparativo de backends) |
| `e-ovrt_experimental-setup` | `feature/webconsole` | `cb72425` (ventana Cámaras) | **ahead 15** | layout player grande + LiveViewer sin commitear; `cameras/` (presets, ver §7); `experiments/video16_clip10_gt/`; plan/spec borrado-runs |
| `e-ovrt_datasets` | `feature/datasets-v2-setup` | `42cfff37` (stubs de clips) | en sync | fix `stop_frame` job-level CVAT + test; metadata provisional `video16_clip10` |
| `docs` | `main` | `2bc779e` (07-17) | local, sin remote | este relevamiento |

> ⚠️ **Matiz sobre la memoria previa ("consola rediseñada PUSHEADA"):** el rediseño y
> la vista correlacionada (`5a944e2`) sí están pusheados, pero los **15 commits
> posteriores** de experimental-setup (borrado de runs completo + ventana Cámaras +
> fix de preview) están solo en local. Pushear es el pendiente operativo #1.

## 2. Qué se construyó desde el doc 50/55 (07-11 → 07-18), por repo

### 2.1 media-plane (`feature/inference-service`)

| Commit | Fecha | Qué introduce |
|---|---|---|
| `0133d38` | 07-13 | `track_id` **opcional** en el contrato `Detection` (evolución aditiva, spec 40 §1 / 42 §3; pedido del tutor). Nadie lo produce aún (deuda vigente). |
| `df5f7c7` | 07-13 | **`OakDSource`**: OAK-D Pro PoE como fuente viva (DepthAI v2), verificada con hardware real (192.168.1.50). |
| `9cede10` | 07-15 | **Prefilter EN-2 on-device** opcional: gate de personas EN la cámara (blob `person-detection-retail-0013`), fail-open estructural (heartbeat, stall, warm-up), knobs `enabled/confidence/keepalive_window_ms/heartbeat_interval_ms/stall_failopen_ms`. + métrica **`capture_to_host_ms`** (sensor→host). A/B real con GDINO: **87 % de drop on-device**. Solo `source.type=oak_d`. |
| `24522cb` | 07-17 | **Ledger de descartes por-frame**: contrato `media.dropped_unit.v1` (`reason: rate_gate/queue_full/staleness_timeout/channel_closed`), sink JSONL thread-safe de apertura perezosa, endpoint `GET /api/runs/{id}/dropped`. |
| `b36b086` | 07-18 | `preview_max` default `None` (un preview por frame; se escriben tras cerrar G2A). |
| `f16cf8c` | 07-18 | Limpieza: **eliminado el cluster muerto `two_node_local`** (nucleo/11 §4 quedó viejo en esto; `runtime/two_node.py` sigue existiendo). |
| `d9f21fa` | 07-18 | **Warm-up de lente** (`warmup_frames`) en fuentes vivas (oak_d/rtsp) — no confundir con el `warmup_units` de G2A. |
| `71bf0ac` | 07-18 | **Deletterbox** de previews al espacio de coordenadas del frame original. |
| `eddeb89` | 07-18 | **Sesión de preview en vivo**: `PreviewManager`, `POST/GET/DELETE /api/preview`, `WS /api/preview/stream` (binario: header JSON + JPEG), modos `detect`/`raw`, exclusión mutua run↔preview vía `ActivitySlot` (409 con `reason`). |
| *(working tree)* | 07-18 | **Fix de latencia RTSP en preview**: `_LatestUnitBox` + hilo lector `preview-reader` separado del procesamiento — el preview toma siempre el frame más reciente en vez de drenar el buffer interno de `cv2.VideoCapture` en orden (OAK-D no sufría por `maxSize=1/blocking=False` a nivel driver). Test de regresión incluido. **Listo, sin commitear.** |

### 2.2 control-plane (`feature/control-service`)

| Commit | Fecha | Qué introduce |
|---|---|---|
| `5a85d45` | 07-17 | **Pieza A**: progreso parcial de patrones — `pattern_progress.jsonl`, contrato `control.pattern_progress.v1`, `GET /api/runs/{id}/pattern-progress`. Solo en estado `candidate`, `elapsed/umbral` normalizado 0–1, espeja `_confirmation_met`, **no toca la máquina de estados ni las alertas**. **Pieza B**: `GET /api/runs?media_run_id=` (correlación de la consola) y `GET /api/runs/{id}/received-units` (drops del bus por set-difference desde `metrics.jsonl`). |
| `140296b` | 07-18 | Limpieza: `configs/_archive/` (configs y pattern sets sin referencias) y `docs/_archive/superpowers/`. |
| `a53e95e` | 07-18 | **`DELETE /api/runs/{run_id}`** (204) + 22 tests. **Sin pushear.** |

Untracked: `configs/replay_video16_clip10{,_yoloe,_altprompts}.yaml` — experimento
comparativo de 3 backends (GDINO-tiny, YOLOE-26l, GDINO+`ppe_alt_v1`
worker/hardhat/reflective_vest) sobre el mismo clip con `cr01_cr02_v2`; sus runs ya
existen en `runs/`. Es además el test de **agnosticismo del GT** frente al prompt set.

### 2.3 experimental-setup (`feature/webconsole`) — 26 commits, 5 líneas

- **Runner real**: `031e10a` (3 fixes de costura al correr la orquestación REAL),
  `f52e242` (`oak_d` habilitado en `SUPPORTED_PLUGINS`).
- **Prompt sets**: `47ad594` + `4420c32` + `5d882b2` — ciclo de vida completo
  (estados, badge `frozen`), catálogo activo: `cr01_cr02_v2_short` y
  `cr01_cr02_bench_v2` (`exploratory`), `eind_v1` (`frozen_pending_review`); 4 sets
  E-DIR en `prompts/_archive/`.
- **Rediseño + vista correlacionada**: `5a944e2` (+`25de358`, `513d395`) — sistema de
  diseño con tokens (`styles/tokens.css`, dark, paleta de status ≥3:1), kit de
  primitivas (`components/ui/`: Badge, Card, DetChip, EmptyState, ErrorBanner, Field,
  StatTile), Shell/Breadcrumbs; **`TraceSection` + `trace.py::compose_trace`** (función
  pura): join por `unit_id` de 4 fuentes (detections + dropped del media;
  pattern-progress + alerts + received-units del control), orden por `frame_index` o
  lexicográfico, paginación y filtro "solo actividad".
- **Borrado de runs** (12 commits, `c1dfea7`…`ecabbf1`): `DELETE /api/runs/{id}` en el
  BFF orquesta **control-plane primero, media-plane al final** (visibilidad de
  reintento), manejo simétrico de fallo parcial, botones en RunsPage/RunDetailPage.
- **Ventana Cámaras**: `cb72425` (+`0d673bd`) — CamerasPage, presets CRUD
  (`/api/cameras` → `camera_store.py`, un YAML por preset en `cameras/`), proxy de
  preview (`/api/preview` REST + WS passthrough), `LivePromptPanel`. En working tree:
  **`LiveViewer`** (canvas: frame+bboxes en un solo paint, descarte de decodificaciones
  fuera de orden, overlay fps/resolución/modo) y layout con player principal grande.

### 2.4 datasets (`feature/datasets-v2-setup`)

- `9867fc50` (07-15) + `65d2a561` (07-17): **protocolo de etiquetado CVAT**
  (`datasets-videos/docs/etiquetado-cvat.md`, §7 reglas del anotador: `unknown` solo en
  tramos sostenidos, sesgo temprano, prioridad identidad>atributos>cajas, pasada
  anti-anclaje) + hoja de sesión `sesion-cvat-cb_b01_p7.md`.
- `0d1c1292`: limpieza — **eliminadas definitivamente las vistas deprecadas
  `canonical_cr01_cr02` y `finetuning_cr01_cr02`** (cualquier referencia quedó
  obsoleta).
- `42cfff37`: **7 stubs `*.clip.yaml`** de clips candidatos al banco (`recorte-1`,
  `video02_clip07`, `video09_clip03`, `video11_clip06`, `video15_clip01`,
  `video16_clip10`, `video16_clip14`).
- *(working tree)*: fix del parser CVAT — `parse_cvat_video_xml` ahora lee `<size>`
  también de `meta/job` (exports a nivel *job*); sin esto `stop_frame` quedaba `None` y
  **el guard I2 de `derive_clip_gt.py` se desactivaba en silencio**. + test. Y metadata
  provisional de `video16_clip10` (`block: B`, `scenario: P7`, marcado PROVISIONAL).

## 3. Arquitectura consolidada (foto 2026-07-18)

### 3.1 Topología de servicios

```
webconsole SPA (Vite :5173) ──proxy /api──► BFF FastAPI :8090
                                              │  ├─► media-plane   :8080 (HTTP+WS)
                                              │  └─► control-plane :8081 (HTTP)
runner CLI (experimental-setup) ──HTTP──► ambos planos (ADR-004/008/009)
media-plane ══ bus ZeroMQ XPUB/SUB, msgpack, bus.envelope.v1 ══► control-plane (EBE)
media-plane ── runs/<id>/detections.jsonl ──► control-plane replay (DBE)
```

El JSONL sigue siendo la verdad en ambos caminos; toda corrida live es re-evaluable
offline con artefactos byte-idénticos (doc 37).

### 3.2 API del media-plane (:8080)

`GET /healthz` · `GET /readyz` · `GET /api/model` ·
`GET /api/catalog/{ingest-plugins,datasets}` ·
`POST/GET /api/runs` · `GET /api/runs/{id}` · `POST /api/runs/{id}/stop` ·
`DELETE /api/runs/{id}` · `GET /api/runs/{id}/detections` ·
`GET /api/runs/{id}/dropped` · `GET /api/runs/{id}/artifacts/{path}` ·
`POST|GET /api/runs/{id}/evaluate` · `WS /api/runs/{id}/stream` ·
`POST/GET/DELETE /api/preview` · `WS /api/preview/stream`

Fuentes: `image_folder`, `video`, `rtsp` (viva, wallclock, reconexión), `oak_d`
(viva, DepthAI, prefilter EN-2 opcional). Vivas = aceptan `warmup_frames`.
Modelos por catálogo `configs/models/`: `mock`, GDINO base/tiny, MM-GDINO
tiny/base/large, YOLOE 26s/26m/26l/26x. Contratos: `media.detection.v1` (con
`track_id` opcional), `media.metric.v2` (`g2a_ms`, `capture_to_host_ms`),
`media.dropped_unit.v1`, `bus.envelope.v1`.

### 3.3 API del control-plane (:8081)

`GET /healthz` · `GET /readyz` · `GET /api/config` ·
`POST /api/runs` (201 ⇒ en live, `BusSource` YA suscripto — invariante doc 38) ·
`GET /api/runs` (+`?media_run_id=`) · `GET /api/runs/current` · `GET /api/runs/{id}` ·
`DELETE /api/runs/{id}` · `GET /api/runs/{id}/alerts` ·
`GET /api/runs/{id}/pattern-progress` · `GET /api/runs/{id}/received-units`

Motor: histéresis `inactive→candidate→confirmed→resolved`, granularidad escena
(ADR-002/012), pattern set oficial **`cr01_cr02_v2`** (CR-01 high `confirm_after_ms:
4000` / CR-02 medium `7000`, resolve 2000/3000, sin cooldown ADR-011). Evaluador
`evaluate-alerts` v2: 5 métricas (P/R/F1, TTFD, SDR) + `re_alerts` +
`sub_threshold_count` + estados de aplicabilidad ADR-006/013; matching por episodio en
ventana `[start+persistencia_min, start+t_alert_max]`, nivel `scene`↔`source_id` /
`subject`↔`subject_key` con fallo ruidoso. Publisher `control.alert.v1` (XPUB,
persiste-primero). Artefactos por run: `pattern_events.jsonl`, `pattern_progress.jsonl`,
`alerts.jsonl/.csv`, `metrics.jsonl`, `errors.jsonl`, `summary.json`,
`effective_config.yaml` (+`evaluation_*.json` si se evaluó).
`eovrt_labs` (rama `mati`, **completamente mergeada**): tracker IoU+distancia,
backend supervisado yolo-ppe, generador de percepción — vive como extra `.[labs]`.

### 3.4 experimental-setup

- **Runner** (spec 44 A1+A2): manifiesto `experiment.manifest.v1` (`slug`,
  `runs.media/control`, `sequencing: control_first|media_first`, `clip_id`,
  `ground_truth`), live⇒control-first con guardián `SubscriptionNotConfirmed`,
  replay⇒media-first; consolidación ADR-014 (crudos referenciados, nunca copiados);
  `report.json`/`report.md`; evaluación temporal inyectable (default CLI
  `eovrt-control evaluate-alerts`).
- **BFF :8090**: proxy a ambos planos, `ExperimentRunManager` (un experimento activo),
  CRUD de cámaras, proxy de preview, borrado orquestado, trace correlado
  (`compose_trace`).
- **Frontend**: páginas Runs/RunDetail/Compose/Experiments/ExperimentDetail/Compare/
  PromptSets/Catalog/Platform/**Cameras**; sistema de tokens + kit UI + Shell.
- **Experimentos**: muestras single-host, matriz `bench_v2/` (6 modelos × 2 splits) y
  `video16_clip10_gt/` (primera corrida orquestada con `clip_id → source_id` y
  evaluación contra GT del video-gt-lab).

### 3.5 datasets / video-gt-lab

Flujo GT: `prepare_clip.sh` (CFR 30fps+sha256) → `preannotate_video` (en media-plane:
GDINO-base anti-circularidad + ByteTrack + NMS) → CVAT (atributos
`unknown/true/false`; la incertidumbre nunca fabrica infracción) → `derive_clip_gt.py`
(guards I1/I2, umbrales `{CR-01: 4000, CR-02: 7000}`) → `validate_clip_gt.py` →
`promote_clip.py` → banco `processed/clip_bench/`.

**Estado del banco**: 1 clip promovido (`cb_b01_p7`, `state: gt_preliminary`,
anotador `claude-vision-preliminary`, 1 episodio CR-01 0→24433 ms, track 11). En
staging: 7 clips normalizados + preanotaciones; `video16_clip10` con GT preliminar
untracked (1 episodio CR-02 + 2 sub-umbrales) usado como **test de mecánica E2E**.
**Ningún GT tiene pasada humana todavía.** Pipeline v2 de imágenes sin cambios
(TRAIN=5540 / BENCH=196 / DEMO=1064).

## 4. Suites de test (conteos verificados 2026-07-18)

| Repo | Tests | Nota |
|---|---|---|
| media-plane | 79 archivos (626 passed + 5 skipped en la última corrida completa) | incluye regresión RTSP-backlog nueva |
| control-plane | 251 colectados (246 passed reportados en `5a85d45`; 1 fallo preexistente ajeno en `tests/labs`) | |
| experimental-setup backend | 37 archivos / 310 funciones | fakes de ambos planos con DELETE |
| experimental-setup frontend | 31 archivos / 157 casos (Vitest) | el plan de borrado-runs que dice "no hay tests de frontend" está equivocado |
| datasets | 103 funciones en 13 archivos | fixtures sintéticos, sin datos raw |

## 5. Inventario de trabajo NO persistido (pendiente operativo #1)

> **✎ Cierre del mismo día:** los cuatro working trees de abajo se **commitearon el
> 2026-07-18** a pedido del usuario (media `cee8832`; control `ed1f19f`; exp-setup
> `00fa4aa`+`14d202b`+`545321c`+`efbea3c`; datasets `223ab953`+`52a2d6e4`). El único
> pendiente operativo que queda es **pushear** (26 commits en total tras el cierre).

**Sin pushear al momento del relevamiento (18 commits):** media-plane 2 (`71bf0ac`
deletterbox, `eddeb89` preview en vivo), control-plane 1 (`a53e95e` DELETE),
experimental-setup 15 (bloque borrado de runs — 12 commits `85d31a9`…`ecabbf1` — +
ventana Cámaras `0d673bd`/`cb72425` + fix de preview `513d395`; el rediseño y la vista
correlacionada `5a944e2` sí están pusheados).

**Sin commitear al momento del relevamiento** (ya resuelto, ver el cierre de arriba):
- media-plane: fix latencia RTSP (`preview_manager.py` + test) — terminado.
- control-plane: 3 configs `replay_video16_clip10*.yaml` (experimento comparativo).
- experimental-setup: LiveViewer + layout player grande (+ test), `cameras/` (ver §7),
  `experiments/video16_clip10_gt/`, plan/spec borrado-runs sin archivar.
- datasets: fix `stop_frame` job-level + test, metadata provisional `video16_clip10`.

## 6. Inconsistencias detectadas y su resolución (auditoría docs vs realidad)

| # | Inconsistencia | Resolución (2026-07-18) |
|---|---|---|
| 1 | `informe/93` R-fila EN-2: "sigue fuera de alcance" contradice nucleo/10 E-07 (implementada 07-15) | **Corregido en informe/93** |
| 2 | `nucleo/11` §8: "trabajo sin commitear, riesgo de pérdida" — ya pusheado; `two_node_local` "deshabilitado" — ya eliminado; "~380 tests" — hoy 626+ | **Banner de actualización agregado**; el detalle vive acá (§2.1) |
| 3 | `operacion/50` §7/§8.4: "79 rutas sin commitear" / deuda #5 "el control-plane no tiene gestión de runs" | **Banner ampliado**; superado por §2.2 |
| 4 | `operacion/55` HEADs viejos (07-11/13) y consola descrita pre-rediseño | **Actualizado** con puntero a este doc |
| 5 | `specs/42` precondición "commitear working tree doc 11 §8" (hecha) y bus "hoy REQ/REP" (ya PUB) | **Enmienda al frente del spec** |
| 6 | `specs/44` §5.2 "rediseño UX sacrificable" — se implementó y amplió | **Enmienda al frente del spec** |
| 7 | Memoria del proyecto: "consola rediseñada PUSHEADA" | Falso — ahead 15. Corregido en la memoria de sesión y registrado en §1 |
| 8 | `docs/architecture.md` y `docs/progress.md` internos del control-plane cortan en 07-02 | Registrado; son docs del repo de código, no de este repo (deuda menor) |
| 9 | Plan borrado-runs afirma "no hay tests de frontend" | Falso (157 casos Vitest); registrado |

Lo que **sigue vigente y correcto**: nucleo/10 (alcance, doc más al día), nucleo/12
(enmienda 07-17 presente), operacion/54 (GT-lab), ADRs 001-014 (ninguno contradicho
por la implementación).

## 7. ⚠️ Seguridad: credenciales de cámara en texto plano

`e-ovrt_experimental-setup/cameras/rtsp_dvr_1.yaml` contiene la URL RTSP con
usuario:clave en claro, y `camera_store.py` persiste los presets tal cual (por diseño:
"el media-plane es el validador final"). El directorio **no estaba git-ignorado**: un
`git add -A` habría commiteado la credencial.

**Mitigación aplicada en este relevamiento:** se agregó `cameras/` al `.gitignore` del
repo. Pendiente de decisión: mover credenciales a env/secret store o aceptar el
YAML-local-ignorado como mecanismo definitivo (documentarlo en el spec 44 si se acepta).

## 8. Pendientes reales (qué falta, en orden)

1. **Pushear los 18 commits** y commitear los 4 working trees (§5) — pedir al usuario.
2. **Pasada humana en CVAT** sobre `cb_b01_p7` (y `video16_clip10`): hoy TODO GT es
   `gt_preliminary` por visión de Claude; las 5 métricas del spec 43 no son citables
   como resultado hasta reemplazarlo (doc 55 PASO 1-3).
3. **Grabación del banco A+C** (guiones spec 43 §3) + consentimientos; completar
   metadata real de los 7 stubs de clips.
4. **EBE-desde-clip** (correr el banco por el camino live, hoy solo DBE-replay).
5. **Spec 45 (distribución MQTT)** — para lo último por decisión registrada.
6. **D1** — bloqueado por acta `edir_v1` (nucleo/12); insumo nuevo: el experimento
   comparativo `video16_clip10` de 3 backends (§2.2) alimenta la discusión.
7. Deuda técnica vigente: nadie produce `track_id` (modo `subject` inerte); matching
   greedy de `evaluate-alerts` puede deflacionar recall con ≥2 alertas por episodio
   (fix = bipartito, doc 52); purga de estado del motor (no bloquea live, doc 37 §7.2);
   SDR+TTFD sobre GT humano pendiente de números reales.

## 9. Números clave ya medidos (citables en el informe, con artefacto)

- **Benchmark del clip `cb_b01_p7`** (GDINO-tiny, GT preliminar):
  P 0,50 · R 1,00 · F1 0,667 · t_alert 4000,0 ms exactos · TTFD 0 ms · **SDR 0,9986**
  (`operacion/datos/95-2026-07-12-bench-cb_b01_p7-gdino-*`). El FP de CR-02 es
  hallazgo del modelo, no del evaluador.
- **G2A** single-host: P50 14,7 ms / P95 31,8 ms (presupuesto 50-250 ms, doc 39).
- **Prefilter EN-2** A/B real con GDINO: **87 % de drop on-device** (07-15).
- **Paridad replay↔stream**: byte-idéntica, verificada por mutación (doc 37).
- **BENCH v2 imágenes**: GDINO-tiny mAP 0,441; YOLOE ciego a `bare_head` (doc 31).
