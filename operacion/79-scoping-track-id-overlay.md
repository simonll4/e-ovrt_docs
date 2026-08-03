# 79 — Scoping: `track_id` + overlay por persona (videos V1–V3)

- **Última actualización:** 2026-07-29
- **Propósito:** relevamiento de solo lectura previo al brainstorming del bloque que
  desbloquea los videos de la defensa (docs 09 §6, 75 §4): hoy nadie produce `track_id`,
  `granularity: subject` solo vive en fixtures y el overlay pinta una caja por escena.
- **Basado en:** código actual de los 4 repos (control-plane `feature/control-service`,
  media-plane `feature/inference-service`); docs 09 §6.2–6.3, 34 §4, 37 §7.2; spec 42 §3.

## 1. Estado real de cada pieza

**Tracker de labs (candidato a port, spec 42 §3).**
`e-ovrt_control-plane/src/eovrt_labs/perception/tracking.py` — `SimpleIoUTracker`
(línea 66): IoU greedy + gates de centro/área + ventanas `max_lost_ms/frames` + firma
de apariencia del torso (EMA). Interfaz `assign(person_boxes, confidences,
appearance_features, frame_index, timestamp_ms) -> list[str]` con ids `subject_NNN`.
Python puro, sin numpy. **Bug conocido**: `apply_person_tracking` (línea 274) escribe el
id en `detection_id` (línea ~311), campo que G0 prohibió como identidad (doc 34 §4.1) —
por eso `generate-detections --track` es inerte para el motor. Tests directos en
`tests/labs/test_perception_generator.py:230-278`, pero `tests/labs` está **excluido de
la corrida estándar** (`--ignore=tests/labs`, sin numpy): el port debe llevar sus tests.

**ByteTrack en la pre-anotación (media-plane).**
`e-ovrt_media-plane/src/eovrt_media/tools/preannotate_video.py::track_persons` usa
`sv.ByteTrack` (supervision 0.29.1, **deprecada desde 0.28**) sobre cajas de persona,
con la trampa `det_thresh = activation + 0.1` documentada en el docstring. Es una tool
batch offline (import lazy, atributos vía hack de `class_id`), no un componente del
pipeline — pero el algoritmo es online frame a frame: **es reusable tal cual para un
render post-hoc** que trackee sobre `detections.jsonl` agrupado por frame.

**El contrato ya está cableado de punta a punta — falta solo el productor.**
Media-plane: `contracts/detection.py:38` (`Detection.track_id: str | None`, aditivo,
`exclude_none`); `sinks/jsonl_sink.py::write_event` serializa con `exclude_none=True`
→ si alguien lo puebla, viaja gratis a `detections.jsonl` y al bus. Control-plane:
espejo en `contracts/media.py:15`; el motor lo consume en
`engine/evaluators/spatial_absence.py:141-150` (`state_key` →
`pattern_id:source_id:track_id`), degradando a escena con causa `no_track_id` si
cualquier sujeto viene sin él (líneas 189-198); memoria de cobertura ADR-012 solo bajo
`subject` (`pattern_engine.py:49`). Fixtures que lo simulan:
`tests/test_pattern_engine.py:66-320` (`subject_006`, `subject_001`). Lo que falta para
producirlo (spec 42 §3): (1) portar el tracker a `eovrt_media` con sus tests, (2) config
`tracking.enabled` (default false), (3) etapa post-`normalizer.normalize` en
`runtime/pipeline.py` (~línea 298) que escriba `track_id` (no `detection_id`), solo
clase `person`, (4) conteo de tracks creados/perdidos en el summary.

**El overlay: dos mitades que nadie compuso.**
Media-plane: `sinks/video_annotation_writer.py` (`annotated.mp4`, enganchado en
`runtime/pipeline.py:177` bajo `outputs.save_annotated_video`) pinta vía
`visualize.py::_draw_annotations` **todas las detecciones** (color por label) — no
conoce alertas, estados ni `track_id`. Control-plane:
`eovrt_labs/visualization/frame_drawing.py:125` (`draw_annotations`) pinta las cajas de
las **alertas** desde `sinks/alerts_csv.py`, pero **solo el bbox del representante** con
la clave de escena — un frame con N descubiertos pinta una caja (doc 34 §4.2). Dato
clave: `supporting_labels`/`supporting_bboxes` (alerts_csv.py:35-36) **ya persisten a
las demás personas** — la información para pintar a todos existe en los artefactos;
falta un renderer que la consuma. Nadie compone detecciones + `pattern_events.jsonl` +
`alerts.jsonl` + timeline (doc 09 §6.3 lo estimó "horas, no días").

## 2. Las dos rutas para V1–V3

Doc 09 §6.2 define V1–V3 como videos **pre-renderizados** y §6.3 decide la herramienta
como **renderizador post-hoc offline** — la defensa no exige `track_id` en vivo.

**(a) Port del tracker al pipeline online** (spec 42 §3 completo). Esfuerzo: 1-2 días
(port + config + etapa + tests) **más** la purga de estado del motor que se reagendó
justo para este momento (doc 37 §7.2: bajo `subject` una corrida RTSP larga acumula
estado por track; doc 34 §4.3) **más** revalidar el pattern set v2: los umbrales
4000/7000 se calibraron bajo escena y la semántica episódica cambia (doc 34 §3, el
reloj por relevo de sujetos). Riesgo medio-alto: toca el pipeline congelado del cierre
y las corridas ya hechas no se benefician. Es lo único que revive G1/`subject` real.

**(b) Renderer offline post-hoc** (sin tocar el pipeline). Script en control-plane o
experimental-setup (doc 09 §6.3 lo deja abierto) que lee video fuente +
`detections.jsonl` + `pattern_events.jsonl` + `alerts.jsonl` de una corrida ya hecha,
pinta todas las cajas + estado del patrón + banner de alerta + timeline TTFD/t_alert, y
para identidad por persona corre tracking **post-hoc** sobre las cajas `person` del
JSONL (ByteTrack de `preannotate_video` reusado, o `SimpleIoUTracker` que es Python
puro sin dependencias). Pinta `supporting_bboxes` para no perder N>1. Esfuerzo:
horas-1 día. Riesgo bajo; re-renderizable sin re-correr. Limitación honesta: la alerta
sigue siendo de escena — el "por persona" es identidad visual, no semántica del motor.

## 3. Riesgos

1. **Fuga de estado del motor** bajo `subject` (doc 37 §7.2): sin política de purga,
   se activa exactamente cuando aterrice el tracker. Solo aplica a la ruta (a).
2. **Cambio de semántica escena→subject** (doc 34 §3): resultados no comparables con
   las corridas/GT existentes; ojo con reusar métricas ya reportadas.
3. **Reuso ingenuo del código de labs** repite el bug `detection_id` (doc 34 §4.1).
4. **`sv.ByteTrack` deprecada** (funcional hasta supervision 0.30) + trampa del
   `det_thresh` +0.1 — si el renderer la usa, fijar versión o preferir el tracker de labs.
5. **Alineación de frames en el render offline**: `detections.jsonl` trae
   `frame_index/timestamp_ms` de los frames muestreados (stride/rate-gate); el renderer
   sobre el video original a fps completo debe decidir hold/interpolación en los huecos.

## 4. Recomendación y preguntas de alcance

**Recomendación: ruta (b) ahora** — desbloquea V1–V3 con lo que ya existe (los
artefactos tienen todo, incluido `supporting_bboxes`) sin tocar el pipeline en pleno
cierre; coincide con lo ya decidido en doc 09 §6.3. La ruta (a) queda como bloque
separado post-videos, solo si se quiere defender G1 vivo, y arrastra la purga de estado.

Preguntas a decidir en el brainstorming:
1. **¿V1–V3 con una persona o con N>1 en escena?** Con una, escena pinta perfecto; con
   N>1 el renderer debe consumir `supporting_*`, y si además se quiere *alerta* por
   sujeto (no solo caja), eso es ruta (a).
2. **¿El video necesita identidad estable visible (`subject_001`, color por persona) o
   alcanza cajas + estado de escena?** Define si el render post-hoc incluye tracking o
   solo composición — la mitad del esfuerzo de (b).
3. **¿G1/`subject` se defiende como capacidad ejecutable o como diseño con fixtures?**
   Decide si spec 42 §3 entra al alcance del cierre o queda deuda declarada (ADR-002 ya
   la enmarca como demostrativa).
