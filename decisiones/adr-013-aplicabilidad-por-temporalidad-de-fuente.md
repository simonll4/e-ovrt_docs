# ADR-013 — Temporalidad de la fuente: detección automática y aplicabilidad de la evaluación de patrones

- **Fecha:** 2026-07-09
- **Estado:** Aceptada
- **Decisión que atiende:** nueva (decisión del usuario, 2026-07-09). Formaliza qué
  significa correr el plano de control sobre un dataset de imágenes y hace que la
  plataforma lo detecte y lo declare sola, en vez de dejarlo a la disciplina del operador.
- **Decisor:** usuario, 2026-07-09

## El problema

La semántica de patrón del control-plane —episodio, confirmación por persistencia,
histéresis, resolución, expiración, re-alertas— **presupone tiempo**. Un dataset de
imágenes independientes no lo tiene. Evaluar patrones ahí es un error de categoría: lo
que se mide no es el motor sino el evaluador espacial de un solo frame.

El error hoy es silencioso y, peor, mecánicamente garantizado:

1. `ImageFolderSource` emite `source_type: "image"` con **`timestamp_ms: None` y
   `frame_index: None`** (verificado sobre `detections.jsonl` real del BENCH).
2. `source_id` = nombre del archivo ⇒ **cada imagen es su propia clave de estado**
   (bajo G0, `(pattern_id, source_id)`). El estado nunca acumula entre unidades.
3. Por lo tanto `hit_count` nunca supera 1, y **cualquier patrón con persistencia
   (`confirm_after_frames > 1` o `confirm_after_ms`) produce cero alertas por
   construcción** — no por ausencia de riesgo. Medido: el probe del doc 33 §4 dio
   137 eventos de patrón y **0 alertas**.

Nada en la plataforma declara esto. Un operador que corra `cr01_cr02_v2`
(`confirm_after_ms: 4000`) sobre el BENCH obtiene un `summary.json` con
`alerts_count: 0` y `errors_count: 0`, indistinguible de una corrida sin riesgos.

## Decisión

### 1. La temporalidad se detecta de la señal que ya existe en el contrato

`DetectionEventSource.source_type` (campo existente, ya poblado por las tres fuentes):

| `source_type` | Fuentes | Temporalidad | `source_clock` |
|---|---|---|---|
| `image` | `ImageFolderSource` | **unidades independientes, sin tiempo** | `none` |
| `video_frame` | `VideoFileSource` | continua, tiempo de medio | `media` |
| `video_frame` | `RtspSource` | continua, tiempo real | `wallclock` |

**No se agrega ningún campo al contrato para esto.** `source_type` resuelve la
temporalidad; `source_clock` (spec 42 §5) resuelve la interpretabilidad del reloj. Son
dimensiones ortogonales y ambas ya están previstas.

`source_clock` pasa a tener **tres** valores: `wallclock | media | none`. El valor `none`
es el de las fuentes no temporales.

### 2. La evaluación de patrones se declara `not_applicable` sobre fuentes no temporales

Usando el vocabulario de ADR-006 (`computed | applicable_not_computed | not_applicable |
not_interpretable`), el control-plane detecta `source_type: "image"` y estampa en su
`summary.json`:

```json
"pattern_evaluation": { "state": "not_applicable", "causes": ["non_temporal_source"] }
```

`causes` es una **lista** (no un string): una corrida puede acumular más de una causa, y un
string compuesto obligaría al reporte consolidado (spec 44) a parsear separadores en vez de
mapear contra la taxonomía cerrada de ADR-006.

Y si el pattern set configura umbrales temporales, se distinguen **dos trampas
distintas** (medidas empíricamente al implementar, 2026-07-10):

| Config sobre imágenes | Qué pasa realmente | Causa |
|---|---|---|
| `confirm_after_frames > 1` | La corrida **no puede alertar jamás** (cada imagen es su propia clave de estado ⇒ `hit_count` nunca supera 1) | `persistence_unreachable_on_non_temporal_source` |
| `confirm_after_ms`, `resolve_after_*`, `subject_absent_timeout_*` | El umbral se **ignora en silencio**: `_confirmation_met` exige `timestamp_ms` (aquí `None`) y cae al camino por frames, confirmando de inmediato | `inert_temporal_thresholds` |

La distinción importa: declarar "no puede alertar" sobre una corrida que **sí alerta**
—como haría `confirm_after_ms: 4000`, que emite una alerta por imagen— sería metadata de
aplicabilidad falsa para el reporte consolidado (spec 44).

**Los otros dos estados que la detección debe distinguir** (descubiertos al implementar; sin
ellos el campo reintroduce el cero silencioso por otra puerta):

| Situación | Estado | Causa |
|---|---|---|
| Ninguna unidad procesada (input inexistente, vacío, o todas las líneas fallan el parseo) | `applicable_not_computed` | `no_units_processed` |
| La corrida mezcla `image` y `video_frame` | `not_interpretable` | `mixed_source_types` |

Declarar `computed` cuando no se procesó nada sería exactamente el fallo que este ADR
combate: un consumidor automático leería "la evaluación de patrones es válida" sobre una
corrida vacía.

### 3. Qué SÍ se corre sobre imágenes

La corrida **no se rechaza**. Sobre fuentes no temporales el plano de control conserva
dos usos legítimos, y ambos se ejercen:

- **Smoke de contrato y plumbing**: que los dos planos se entienden (`errors_count: 0`,
  parseo de las N unidades). Es lo que fue la Fase 0 y el Paso 0 (doc 33).
- **Diagnóstico del evaluador espacial por frame**: región, matching 1:1 y asociación
  EPP↔persona sí se ejercitan en una imagen. El BENCH con `person_gt` mide recall CR-01
  por persona contra GT real. Por eso la evidencia de escena conserva los sujetos no
  representantes en `supporting` (bboxes necesarios para el join por persona).

Los `AlertEvent` se siguen emitiendo y persistiendo: sobre imágenes significan
**"condición espacial detectada en este frame"**, no "episodio confirmado". El estado de
aplicabilidad del summary es lo que fija la lectura.

### 4. Qué NO se computa ni se reporta sobre imágenes

El reporte consolidado (spec 44) **omite** —no pone cero, omite y explica— toda métrica
de naturaleza temporal cuando `pattern_evaluation.state == "not_applicable"`:

| Métrica | Estado sobre fuente no temporal |
|---|---|
| `t_capture→alert` | `not_applicable / non_temporal_source` (no hay episodio ni "primera evidencia" en el tiempo) |
| `t_compute-budget` | **`computed`** — es monotónico e independiente de la fuente (spec 40 §5.2.3) |
| TTFA interna, latencias de confirmación | `not_applicable / non_temporal_source` |
| `re_alerts` por episodio, estabilidad | `not_applicable / non_temporal_source` |
| G2A, mAP, AP por clase, recall por persona | `computed` — son métricas de percepción |

### 5. La superficie de selección lo dice antes de correr

Al elegir un data source de imágenes (webconsole o runner, spec 44), la plataforma
**detecta el tipo y lo comunica en el punto de selección**: marca la corrida como
diagnóstico espacial / smoke, deshabilita o esconde los controles de umbrales temporales
(que serían inertes) y las vistas de métricas temporales, y advierte si el pattern set
elegido configura persistencia. La detección ocurre en la config de la fuente
(`type: image_folder`) antes de la corrida, y se re-confirma en el primer evento por
`source_type`.

## Fundamento

1. **La división es la que ya tienen las specs, hecha explícita.** Imágenes → percepción y
   asociación espacial (mAP, AP por clase, recall por persona). Video → patrones con GT
   temporal (clip bench, spec 43: episodios y latencias en tiempo de medio). RTSP/cámara →
   patrones más las métricas end-to-end genuinas (`t_capture→alert` solo es `computed` en
   fuente viva, spec 40 §5.2.3). Este ADR no inventa la división: la detecta y la aplica.
2. **Un cero silencioso es el peor resultado posible de un experimento.** La plataforma ya
   distingue `not_applicable` de `computed` justamente para esto (ADR-006). No usarlo acá
   sería dejar que una corrida estructuralmente incapaz de alertar se lea como evidencia
   de ausencia de riesgo.
3. **Detectar, no configurar.** La señal está en el contrato y la puebla el media-plane.
   Pedirle al operador que declare "esto es una fuente temporal" duplicaría una verdad que
   el sistema ya conoce, y abriría la puerta a que las dos se contradigan.
4. **No rechazar la corrida** preserva el smoke de contrato y el diagnóstico espacial, que
   son la mitad del valor del BENCH y que ya usamos (doc 33). Rechazar convertiría una
   herramienta en un obstáculo.

## Impacto

- **Spec 42 §5:** corregir dos errores de hecho — el `timestamp_ms` de `ImageFolderSource`
  **no** es tiempo de medio, es `None`; y `source_clock` pasa a `wallclock | media | none`,
  con `image_folder` → `none`. La etiqueta `not_interpretable / dbe_media_time` aplica a
  `VideoFileSource`, no a imágenes.
- **Spec 40 §5.2.3:** agregar el tercer caso (fuente no temporal): `t_capture→alert` es
  `not_applicable / non_temporal_source`; `t_compute-budget` sigue `computed`.
- **Spec 41:** el control-plane detecta `source_type` y estampa `pattern_evaluation`
  (estado + causa) en `RunSummary`. Campo aditivo.
- **Spec 44:** la selección de data source detecta el tipo; el reporte omite (no cerea) las
  métricas temporales cuando no aplican; la webconsole lo comunica antes de correr.
- **Plan G0:** el fixture y el gate no cambian (son temporales). Sí queda registrada la
  regla de uso: el BENCH nunca valida el motor.

## Referencias

ADR-002 (G0: la clave de escena es la que hace que cada imagen sea su propia escena),
ADR-006 (vocabulario de aplicabilidad y causas), ADR-012 (qué sostiene G0 sin identidad),
spec 40 §5.2.3, spec 41 §2, spec 42 §5, spec 44, doc 33 §4 y §4.1 (evidencia empírica:
137 eventos / 0 alertas con persistencia sobre imágenes).
