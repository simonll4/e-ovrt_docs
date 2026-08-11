# Relevamiento: e-ovrt_control-plane

> ⚠️ **2026-08-10 — DOCUMENTO HISTÓRICO. No usar como estado del control-plane.**
> Reemplazado por **`../18-relevamiento-control-plane.md`**. Es la foto del 2026-07-06 con una
> actualización del 07-09; auditado contra el código el 2026-08-10, **siete de sus once
> secciones están vencidas**. Vale como registro de lo que se sabía ese día, y su banner
> manda sobre su cuerpo.
>
> **Tres trampas activas, por si igual lo leés:**
> - **§8 dice que los pattern sets son `cr01_cr02_v1` y `cr01_cr02_temporal_eval`.**
>   **`v1` está DEPRECADO** en el propio YAML (hallazgo F-DR9: con timing por frames los
>   episodios nunca confirman y aparecen falsos `missed`). El oficial es **`cr01_cr02_v2`**
>   (scene, CR-01 high 4000 ms / CR-02 medium 7000 ms). Hoy hay 7 sets.
> - **§2 dice "sin servicio HTTP, sin broker".** Falso desde julio: hay servicio FastAPI
>   en `:8081` (ADR-0008 local) y fuente bus ZeroMQ live (ADR-0007), con `runtime/live.py`.
> - **§6 presenta `subject_key` como el punto débil sin resolver.** Superado: el default es
>   **G0 por escena** (ADR-002 del proyecto / ADR-0013 local) y la identidad existe como
>   decorador de fuente opt-in en `sources/tracking.py`. **§10 (los 5 pendientes) está
>   superado** desde el 2026-07-29 — lo declara el propio `progress.md` del repo.
>
> **Qué conserva vigencia:** **§1** (qué es el plano y la cadena `condición → patrón →
> evidencia → estado → alerta`, incluido *"una detección no es una alerta"*), **§4** (el
> contrato de entrada, wire-compatible con `media.detection.v1`) y **§12** como registro
> histórico de la rama `mati`.

- **Fecha:** 2026-07-06 · **ACTUALIZADO 2026-07-09 con la rama `mati` — ver §12**,
  que corrige varios puntos de este documento (el motor, el evaluador, el punto
  débil de identidad §6 y el pendiente de cooldown ya evolucionaron).
- **Repo:** `e-ovrt_control-plane` (remote `git@github.com:Pandulc/e-ovrt_control-plane.git`)
- **Estado del repo (al 2026-07-06, rama main):** 3 commits (`Implement initial control plane` → `Add temporal eval` → `Add time-based persistence`), tests 9/9 en verde, ~1.9k líneas Python. **Al 2026-07-09 la rama activa es `mati`** (11 commits nuevos, 2026-07-01→07, pusheada a origin): +5k líneas.

## 1. Qué es

Plano de control experimental de E-OVRT-VDP. Consume la **evidencia perceptual** que
produce el plano de medios (detecciones normalizadas), evalúa **patrones de riesgo**
configurables (hoy CR-01 "persona sin casco" y CR-02 "persona sin chaleco") y emite
**alertas internas trazables**. No ejecuta inferencia visual, no hace tracking, no
distribuye alertas hacia afuera (eso está diseñado aparte, ver
`06-diseno-distribucion-alertas.md`).

Cadena conceptual: `condición → patrón → evidencia perceptual → estado de patrón → alerta interna`.
**Una detección no es una alerta**: la alerta sólo se emite cuando el motor confirma
persistencia temporal de la condición.

## 2. Stack y forma de ejecución

- Python 3.11+, Pydantic, PyYAML, Typer/Rich. Dev: pytest, ruff. Package `eovrt_control`,
  entry point `eovrt-control`.
- **Modo único actual: replay offline DBE** sobre `detections.jsonl` del plano de medios
  (ADR-0004, serie del control-plane). Sin servicio HTTP, sin broker, sin DB (JSONL
  append-only por corrida, ADR-0003 del control-plane — serie de 4 dígitos, no
  confundir con los ADR-00X del proyecto en `docs/decisiones/`).
- CLI: `eovrt-control replay <config.yaml>`, `validate-config`, `evaluate-alerts`.
- Una corrida escribe `runs/<control_run_id>/`: `effective_config.yaml`,
  `pattern_events.jsonl`, `alerts.jsonl`, `metrics.jsonl`, `errors.jsonl`, `summary.json`.

## 3. Estructura del código

```
src/eovrt_control/
├── cli.py                  # Typer: replay / validate-config / evaluate-alerts
├── config.py               # ReplayConfig + PatternDefinition (region/evidence/timing)
├── contracts/
│   ├── media.py            # DetectionEvent espejo de media.detection.v1 + backport de campos planos
│   ├── pattern.py          # PatternEvidence, PatternStateChanged (control.pattern_state.v1)
│   ├── alerts.py           # AlertEvent (control.alert.v1)
│   ├── metrics.py          # ControlMetricSample, RunSummary
│   └── errors.py           # ErrorEvent
├── engine/
│   ├── pattern_engine.py   # máquina de estados por (pattern_id, subject_key)
│   └── evaluators/spatial_absence.py  # inferencia de ausencia de EPP por región
├── sources/media_jsonl.py  # iterador línea a línea con manejo de errores por línea
├── sinks/                  # JsonlSink + RunArtifacts
├── runtime/replay.py       # orquestación de la corrida completa
└── evaluation/temporal.py  # eval de alerts.jsonl vs ground truth temporal débil
```

## 4. Contrato de entrada

`contracts/media.py::DetectionEvent` replica `media.detection.v1` del media-plane:
`run_id`, `unit_id`, `source{source_id,source_type,frame_index,timestamp_ms,width,height}`,
`model`, `prompts`, `detections[]`, `timing`. Un `model_validator(mode="before")`
retro-porta campos planos históricos (`source_path`, `model_adapter`, `prompt_version`,
`timing_ms`) para poder reproducir artefactos viejos.

Compatibilidad verificada contra el contrato real del media-plane
(`eovrt_media/contracts/events.py` + `detection.py`):

- Campos extra del media-plane (`source_prompt`, `strategy`, `condition_id` en Detection;
  `normalize_ms` en timing) se ignoran sin error (Pydantic default). ✔
- Todos los campos que el control-plane exige existen en lo que emite el media-plane. ✔
- `configs/replay_dbe_cr01_cr02.yaml` ya apunta a
  `../../e-ovrt_media-plane/runs/latest/detections.jsonl` — el replay cross-repo funciona hoy.

## 5. Evaluador espacial (spatial_absence)

Para cada patrón (ej. CR-01: `subject_class=person`, `required_absent_class=helmet`):

1. Filtra sujetos `person` por `min_subject_confidence` (0.35) y `min_subject_area_px` (400).
2. Define una **región esperada** dentro del bbox de la persona por ratios
   (CR-01 `upper_body`: y 0–0.45, margen x 0.12; CR-02 `torso`: y 0.25–0.85, margen x 0.08).
3. Busca detecciones del EPP requerido (≥ `min_absent_class_confidence` 0.25) cuyo
   **centro** caiga dentro de la región.
4. Si no hay ninguna → emite `PatternEvidence` (evidencia positiva de ausencia).

Alias de labels: `person|worker|human|people`, `helmet|hardhat|safety helmet|…`,
`vest|reflective vest|safety vest|…` — matching por `label` o `prompt_id` normalizados.
Nota: **no usa `bare_head`** (clase del vocabulario canonical_v2) como evidencia positiva.

## 6. Máquina de estados y persistencia temporal

Estado por clave `(pattern_id, subject_key)`:
`inactive → candidate → confirmed → sustained → resolved`.

- **Hit** (evidencia presente): acumula; pasa a `confirmed` cuando se cumple
  `confirm_after_ms` (preferido, por `timestamp_ms` del evento) o
  `confirm_after_frames` (fallback). `confirmed → sustained` en el siguiente hit.
- **Clear** (sujeto observado sin evidencia): pasa a `resolved` tras `resolve_after_ms`
  o `resolve_after_frames`.
- **AlertEvent se emite sólo en la transición a `confirmed`**, con `alert_id` determinista:
  `uuid5(control_run_id:media_run_id:unit_id:pattern_id:subject_key)` → idempotente por
  construcción (re-procesar el mismo evento produce el mismo id).

### subject_key — el punto débil conocido

`subject_key = f"{pattern.id}:{source_id}:{detection_id o unit_id:person:index}"`.
El control-plane **no hace tracking** (declarado en `docs/architecture.md`): asume que el
media-plane provee identidad estable. Pero el media-plane real genera
`detection_id = f"det_{idx:06d}"` **por frame** (índice de orden en el frame, en
`postprocessing/detection_normalizer.py`), no un track id. Consecuencia: con video real,
el mismo `det_000001` puede ser personas distintas en frames distintos (aliasing de
identidad) y la persistencia temporal acumula hits sobre identidades incorrectas. Los
fixtures sintéticos evitan esto poniendo `detection_id` estables (`worker_a`, …). Está
listado como pendiente explícito: "definir el contrato de identificador estable de sujeto
emitido por el plano de medios antes de pasar a escenarios EBE".

## 7. Contratos de salida

- `PatternStateChanged` (`control.pattern_state.v1`): cambio de estado por sujeto, con
  `control_run_id`, `media_run_id`, `unit_id`, `source_id`, `pattern_id`, `condition_id`,
  `subject_key`, `previous_state/state`, `severity`, `evidence`, `frame_index`, `timestamp_ms`.
- `AlertEvent` (`control.alert.v1`): igual + `alert_id`, `state="open"`. No implica acción
  externa automática.
- `ControlMetricSample` (`control.metric.v1`): por unidad visual — conteos y `processing_ms`.
- `RunSummary` (`control.summary.v1`): agregados + rutas de artefactos.
- `ErrorEvent` (`control.error.v1`): errores por línea/unidad; una línea inválida no
  aborta la corrida.

## 8. Configuración

- **Config de replay** (`configs/replay_*.yaml`): `run{scenario,name}`, `input{type=media_jsonl,path}`,
  `patterns{file,active_ids}`, `outputs`, `logging`. Paths relativos al YAML.
- **Pattern sets** (`configs/patterns/*.yaml`): `cr01_cr02_v1` (confirm/resolve = 1 frame,
  para primeras corridas DBE) y `cr01_cr02_temporal_eval` (confirm 3 / resolve 2 frames,
  para el fixture temporal). Cada patrón: `id`, `condition_id`, `severity`, `subject_class`,
  `required_absent_class`, `region{ratios}`, `evidence{umbrales}`, `timing{frames|ms}`.

## 9. Evaluación temporal

Fixture sintético `fixtures/simulated_media/cr01_cr02_temporal/` (12 unidades,
`worker_a` CR-01 persistente, `worker_b` transitorio que NO debe alertar, `worker_c`
CR-02 persistente) + `ground_truth.json` débil. `eovrt-control evaluate-alerts` calcula
expected/observed/matched/missed/unexpected/duplicates, precision/recall/F1 y latencia
primera-evidencia→alerta (frames y ms). Caso feliz validado: P/R/F1 = 1.0.

## 10. Pendientes declarados por el repo (docs/progress.md)

1. Ejecutar replay con artefactos reales del plano de medios.
2. Fixtures desde clips reales.
3. Calibrar thresholds de región/confianza con salidas DBE reales.
4. Extender ground truth temporal (ventanas, FP/min, tiempo máx. hasta alerta).
5. **Contrato de id estable de sujeto desde el plano de medios** (bloqueante para EBE).

## 11. Observaciones para la integración (resumen)

- El contrato de entrada ya es wire-compatible con lo que persiste el media-plane; la
  integración por archivo funciona hoy. El salto a bus de eventos es un cambio de
  **fuente**, no de contrato (ver doc de integración).
- La fuente está bien aislada (`sources/media_jsonl.py` es el único acople a la forma de
  entrada) y el motor es push-based (`engine.process(event)` por evento) → apto para
  consumir un stream sin re-arquitectura.
- `runtime/replay.py` asume corrida finita (resumen al agotar el archivo); un modo
  streaming necesita un runtime nuevo con cortes de resumen periódicos o por señal.
- El diseño de distribución de alertas (2026-07-04) ya propone primitivas de bus
  (`transport/` espejo del media-plane, ZeroMQ PUB/SUB + msgpack, envelope versionado)
  pensadas para reutilizarse en el bus `media → control`.

## 12. ACTUALIZACIÓN 2026-07-09 — rama `mati` (11 commits, 2026-07-01→07)

Desarrollo sustancial de otro integrante del equipo, pusheado a `origin/mati`
(+5k líneas). Reorganiza el repo en **núcleo `eovrt_control` liviano** (sin
torch/OpenCV) **+ paquete experimental `eovrt_labs`** (extra `.[labs]`).

### 12.1 Evolución del motor (núcleo)

Las cinco mejoras atacan exactamente los modos de falla señalados en este
relevamiento y en el doc 04 §3.3:

1. **Asociación EPP↔persona 1:1 por matching bipartito de cardinalidad máxima**
   (caminos aumentantes, adyacencia ordenada por cercanía al centro de región) —
   elimina el "robo" de casco entre cajas de persona superpuestas del matching por
   contención simple.
2. **Región adaptativa por pose** (`region.full_height_aspect_ratio`): si la caja
   del sujeto es más ancha que alta (agachado/inclinado), la banda vertical se
   expande a la altura completa — mitiga el modo de falla por postura.
3. **Memoria de cobertura EPP** (`timing.coverage_memory_ms/frames`): sujeto con
   EPP visto hace menos de la ventana sigue tratándose como cubierto — amortigua el
   parpadeo del detector y oclusiones breves (histéresis de cobertura).
4. **Expiración de sujetos ausentes** (`timing.subject_absent_timeout_ms/frames`):
   resuelve y purga sujetos que salen de escena — acota el estado y cierra episodios.
5. **Cooldown de re-alerta** (`timing.realert_cooldown_ms/frames`) por
   (patrón, sujeto) — cierra el gap señalado en docs 02 §4.8 / 08 §4.1.

Además: **warning explícito cuando la persistencia temporal no puede operar por
falta de ids estables** (`replay.py` detecta el fallback `det_NNN` y lo reporta) —
reconoce formalmente el riesgo nº1 de §6; export **`alerts.csv`** en el núcleo; y
**contrato de timing migrado** (fuera `read_ms/preprocess_ms`, entra `normalize_ms`)
→ ahora espejo exacto del media-plane. Nuevo pattern set **`cr01_cr02_field_v1`**
("perfil de campo": todo lo anterior activado; ojo: severity sigue `medium` y
confirm 1000 ms — la alineación al informe del doc 08 §2.1 sigue pendiente).

### 12.2 `eovrt_labs`: generador de percepción propio + tracking + visualización

- **Generador de detecciones** desde video/imágenes → `detections.jsonl`
  (`media.detection.v1` compatible) con tres backends: `gdino` (default),
  **`yolo-ppe` (modelo supervisado construction-site-safety — una baseline cerrada
  lista para comparar)** y `yoloe`; tuning fino por YAML.
- **`SimpleIoUTracker`** con apariencia: `--track` produce ids de sujeto estables
  (`subject_001`, …) — la identidad que el motor necesita para persistencia real.
- **Visualización de alertas sobre video** (`frame_drawing.py` + `alerts_csv`).
- **Evidencia real ya producida:** `docs/reportes/REPORTE_HF_VIDEO_INTEL_20260626.md`
  — primera corrida end-to-end video→percepción→control→alertas (video de obra,
  yolo-ppe + tracking IoU, RTX 4060/WSL) — anterior incluso a la Fase 0 que corrimos
  el 07-06; y un runbook de comparativa gdino antes/después de las mejoras del motor.

### 12.3 Cómo se probó y ajustó el motor (herramientas + experimentos ya corridos)

**Toolchain de calibración** (todo en la rama `mati`):

- **`eovrt-labs generate-detections`**: video/carpeta → `detections.jsonl`
  (`media.detection.v1` estricto: bbox_norm, area_px, timing, `exclude_none`).
  Backends con vocabulario **positivo canónico** (person/helmet/vest — labs es
  E-IND puro): `gdino` usa prompts `person / helmet / safety vest`; `yolo-ppe`
  (supervisado, pesos `construction-site-safety.pt` auto-descargados) **descarta
  deliberadamente las clases negativas del modelo** (`no_helmet`→ descartada) para
  mantener la inferencia de ausencia en el motor; `yoloe` con prompt set propio.
- **Tuning por YAML** (`--tuning`, `configs/tuning/`): umbrales de confianza **por
  clase** (person/helmet/vest), NMS separado persona vs EPP, área mínima, tamaño de
  inferencia; tracking con IoU threshold, ventanas `max_lost` (ms y frames), gates
  de centro/área y **firma de apariencia del torso** (peso + similitud mínima) para
  sostener IDs. Fix incluido: el piso de confianza del backend sigue al menor umbral
  por clase.
- **`scripts/analyze_alerts.py`**: resumen y **comparación antes/después** de dos
  corridas (total, por condición, pares condición-sujeto únicos, frames con alerta,
  re-alertas por sujeto).
- **Runbook** (`docs/evaluaciones/comparativa-gdino.md`): generar con `--track` →
  replay temporal → comparar; con **gate de regresión**: el fixture sintético debe
  seguir dando F1 = 1.0 (cubierto por tests).
- Visualización de frames de alerta (`frame_drawing` + `alerts.csv` + util
  `draw_alert_frames`) para inspección visual dirigida.

**Experimento 1 — REPORTE_HF_VIDEO_INTEL (2026-06-26, motor viejo):** video real de
obra (`video1.avi`, dataset Intel), `yolo-ppe`+track, stride 2 → 976 unidades, 0
errores, 82 alertas (17 CR-01 / 65 CR-02), 44 sujetos, replay en ~92 ms. Hallazgos
que **motivaron directamente las mejoras del motor**: (a) CR-02 dominada por fallas
de percepción/asociación — trabajadores CON chaleco alertados porque `vest` no se
detecta o no se asocia (⇒ matching 1:1 + memoria de cobertura); (b) re-alertas del
mismo sujeto por ciclos resolved→confirmed, 5–11 alertas por sujeto (⇒ cooldown);
(c) fragmentación de IDs — 44 subjects para pocos trabajadores reales (⇒ apariencia
en el tracker + `max_lost`); (d) veredicto honesto: "sirve como smoke de
integración, no como benchmark — requiere GT y patrón temporal más estricto".

**Experimento 2 — video5 con gdino (run `replay_hf_temporal_20260707T233019Z`,
2026-07-07, motor nuevo):** inspección visual → tuning documentado con causa
(`configs/tuning/video5_gdino.yaml`): NMS de persona más estricto (0.50) por cajas
duplicadas en clusters que generaban CR-01 falsos; `vest_confidence` 0.20 porque un
chaleco amarillo desteñido oscila en conf 0.25–0.35; `track_max_lost_ms` 3000 por
oclusiones largas (manguera de hormigón) que fragmentaban IDs e impedían actuar al
cooldown. **Este es conocimiento de calibración real con trazabilidad frame a frame.**

**Dato de sourcing:** los videos usados (`video1.avi`…`video5`) viven en
`e-ovrt_datasets/datasets/video/` **en el entorno del compañero** (git-ignorados por
la política de raw media; no están en esta copia). Existe además una estrategia
legacy de video stock en el repo datasets. Relevante para el clip bench (H2).

### 12.4 Implicancias sobre el set de documentos (aplicadas)

1. **D2 (G0/G1) queda en revisión:** la rama mati tomó el camino **G1 con tracker en
   el generador** (labs) — funciona hoy para experimentos, pero el flujo de
   plataforma (media-plane, sin tracker) sigue necesitando G0 o portar el tracker.
   No son excluyentes: G1 en labs para calibrar el motor, G0/G1 por decidir para la
   plataforma. Tablero actualizado (doc 03).
2. **E-03 reescrita** (doc 10): "tracker no implementado" ya no es cierto — existe
   como herramienta de labs; lo excluido pasa a ser su incorporación al flujo de
   plataforma y las métricas MOT.
3. **La pregunta del supervisado (doc 09 Q&A) ahora tiene respuesta empírica
   barata:** el backend `yolo-ppe` permite la comparación OVD vs cerrado con el
   mismo motor y el mismo video — refuerza R2 sin romper el won't de fine-tuning.
4. **Overlay renderer (doc 09 §6.3) casi completo entre ambos repos:**
   `frame_drawing`+`alerts_csv` (control) + `VideoAnnotationWriter` (media) — falta
   solo la composición de estados/timeline.
5. **Tensión arquitectónica a administrar en el informe:** labs es un segundo
   pipeline de percepción dentro del repo del control-plane. Encuadre correcto (ya
   sugerido por el propio split core/labs): **labs = herramienta experimental de
   calibración y generación de fixtures; la percepción canónica de la plataforma es
   el media-plane**. Si no se declara así, el tribunal ve dos pipelines compitiendo.
6. La Fase 0 del 07-06 corrió con el motor viejo (matching por contención):
   re-ejecutarla con el motor nuevo cambiará los números (precisión esperablemente
   mejor) — hacerlo antes de calibrar umbrales.
