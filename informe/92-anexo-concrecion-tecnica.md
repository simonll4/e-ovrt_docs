# Anexo de concreción técnica — material listo para inyectar en el capítulo

- **Fecha:** 2026-07-12
- **Para qué sirve:** es la respuesta material a la observación del tutor técnico
  ("se definen contratos y módulos pero no siempre se evidencia cómo se implementan concretamente:
  clases, APIs, servicios"). Todo lo de acá está **verificado contra el código y contra artefactos
  reales en disco**, con ruta y línea. Nada está inventado ni idealizado.
- **Cómo usarlo:** cada sección corresponde a un redline del plan de `91-relevamiento-etapa3-vs-implementacion.md`
  (bloque B). El texto está escrito para poder pasarse al `.docx` con edición mínima.
- **Regla de oro al copiar:** si un campo no está en el código, **no va al informe**. La única forma de
  que este anexo envejezca mal es que alguien "mejore" un esquema al transcribirlo.

---

## 1. Tabla de correspondencia: contrato preliminar (Etapa 3) ↔ artefacto real

Esta tabla es la bisagra del capítulo. Convierte los diez nombres conceptuales de la Tabla 50 en
artefactos verificables, sin traicionar la lógica del diseño original.

| Contrato preliminar (Tabla 49/50) | Artefacto real | Tipo / esquema | Dónde vive |
|---|---|---|---|
| `RunConfig` | **Manifiesto de experimento** + configs por plano (referenciadas) | `experiment.manifest.v1` | `e-ovrt_experimental-setup/experiments/` |
| `SourceDefinition` | Sección `source` de la run config + **registro de plugins de ingesta** | `SourceSection` | `media-plane/config/schemas.py:141` |
| `ModelProfile` | Catálogo de modelos por archivo + `EOVRT_MODEL_REF` | `ModelSection` | `media-plane/configs/models/<familia>/<variante>.yaml` |
| `PromptDefinition` | Prompt set versionado | `PromptSet` / `PromptClass` | `experimental-setup/prompts/cr01_cr02_v2_short.yaml` |
| `FrameMetadata` | `VisualUnit` (interno) + bloque `source` del evento publicado | `VisualUnit` | `media-plane/contracts/visual_unit.py:11` |
| **`PerceptionEvent`** | **`DetectionEvent`** | **`media.detection.v1`** | `media-plane/contracts/events.py:44` |
| `PatternDefinition` | Definición declarativa dentro del pattern set | `PatternDefinition` | `control-plane/config.py:91` |
| `PatternStateChanged` | `PatternStateChanged` | `control.pattern_state.v1` | `control-plane/contracts/pattern.py:31` |
| `AlertEvent` | `AlertEvent` (`alert_id` uuid5 determinista ⇒ idempotente) | `control.alert.v1` | `control-plane/contracts/alerts.py:10` |
| `MetricSample` | `MetricSample` (medios) / `ControlMetricSample` (control) | `media.metric.v2` / `control.metric.v1` | `media-plane/contracts/metrics.py:8` · `control-plane/contracts/metrics.py:18` |
| `ErrorEvent` | `errors.jsonl` por corrida | — | ambos planos |
| Repositorio de eventos (§17.3.12) | **JSONL append-only por corrida** | `runs/<run_id>/*.jsonl` | cada plano |
| Bus interno de eventos (§17.3.8.4) | **ZeroMQ XPUB/SUB + msgpack** | `bus.envelope.v1` | `media-plane/transport/bus.py:19` |
| Reporte experimental (§17.3.13.4) | Reporte consolidado | `report.json` / `report.md` | `experimental-setup/runs/<experiment_id>/report/` |
| Alerta distribuida (§17.3.10) | `NotificationEnvelope` / `DeliveryRecord` | `control.notification.v1` / `control.delivery.v1` | **spec 45 — no implementado; sigue preliminar** |

> **Frase para el capítulo:** *"Los contratos definidos en la Etapa 3 dejaron de ser denominaciones
> preliminares para el núcleo validable: se materializaron como modelos de datos versionados, con
> serialización explícita y esquema verificable. La tabla siguiente establece la correspondencia. Los
> contratos del tramo de distribución, no implementado, conservan su carácter preliminar y así se declaran."*

---

## 2. El evento de detección: clase, esquema y serialización

Es el contrato central del sistema (el `PerceptionEvent` del capítulo). El tutor pidió literalmente ver
"una clase" y "un DTO". Acá están las dos cosas.

### 2.1 La clase (Python / Pydantic)

`e-ovrt_media-plane/src/eovrt_media/contracts/events.py:44`

```python
class DetectionEvent(BaseModel):
    schema_version: str = "media.detection.v1"
    event_type: str = "detection_event"
    run_id: str
    unit_id: str                      # identificador de la unidad visual (frame)
    source: DetectionEventSource      # source_id, source_type, frame_index, timestamp_ms, width, height
    model: DetectionEventModel        # name, model_id, device
    prompts: DetectionEventPrompts    # prompt_set_id
    detections: list[Detection]
    timing: DetectionEventTiming      # normalize_ms, inference_ms, postprocess_ms, write_ms, total_ms


class Detection(BaseModel):           # contracts/detection.py:28
    detection_id: str | None = None
    label: str
    prompt_id: str | None = None
    source_prompt: str | None = None
    strategy: str | None = None       # declarado en el modelo; NO se serializa hoy (vale None)
    condition_id: str | None = None   # ídem
    confidence: float
    bbox_xyxy: list[float]            # píxeles, sistema de la imagen original
    bbox_norm_xyxy: list[float]       # normalizado [0,1]
    area_px: float | None = None
    model_name: str | None = None
```

> ⚠️ **Corregido tras auditoría (2026-07-12).** Los campos opcionales son opcionales **de verdad**: no
> los muestres como requeridos. Y `strategy` / `condition_id` **existen en el modelo pero valen `None` y
> no aparecen en el JSONL** de las corridas actuales (el escritor omite los nulos). Si querés mostrarlos
> en el informe, hay que **poblarlos primero**; hasta entonces, no van al DTO de ejemplo.

### 2.2 El DTO serializado — **línea literal**, verificada carácter por carácter

> ⚠️ **La versión anterior de este bloque estaba fabricada** (una detección `helmet` que no existía en esa
> línea, y tiempos de postproceso/escritura inventados). Lo que sigue es la **transcripción literal** de
> `e-ovrt_media-plane/runs/run_20260711_211647_dbe_grounding_dino_6114c6/detections.jsonl`, unidad
> `frame_000120` — la unidad en la que el sistema confirma la alerta de CR-01, a los 4000 ms exactos.
> **Único recorte:** de las 22 detecciones de esa unidad se muestran 2, y se indica el recorte.
> **Regla: no se agrega, no se mejora, no se completa nada.**

```json
{
  "schema_version": "media.detection.v1",
  "event_type": "detection_event",
  "run_id": "run_20260711_211647_dbe_grounding_dino_6114c6",
  "unit_id": "frame_000120",
  "source":  { "source_id": "cb_b01_p7", "source_type": "video_frame",
               "frame_index": 120, "timestamp_ms": 4000.0,
               "width": 1920, "height": 1080 },
  "model":   { "name": "grounding_dino",
               "model_id": "IDEA-Research/grounding-dino-tiny", "device": "cuda" },
  "prompts": { "prompt_set_id": "cr01_cr02_v2_short_inline" },
  "detections": [
    { "detection_id": "det_000001", "label": "person",
      "prompt_id": "person", "source_prompt": "person", "confidence": 0.8257,
      "bbox_xyxy": [1734.6, 300.9, 1838.2, 525.8],
      "bbox_norm_xyxy": [0.9034, 0.2786, 0.9574, 0.4869],
      "area_px": 23291.6, "model_name": "grounding_dino" },
    { "detection_id": "det_000002", "label": "person",
      "prompt_id": "person", "source_prompt": "person", "confidence": 0.837,
      "bbox_xyxy": [159.5, 402.2, 253.4, 639.8],
      "bbox_norm_xyxy": [0.0831, 0.3724, 0.132, 0.5924],
      "area_px": 22312.3, "model_name": "grounding_dino" }
    // … 20 detecciones más (person / helmet / vest) omitidas por legibilidad
  ],
  "timing": { "normalize_ms": 8.25, "inference_ms": 214.37,
              "postprocess_ms": 0.2, "write_ms": 0.0, "total_ms": 214.59 }
}
```

**Dos cosas que esta línea literal enseña, y que el ejemplo fabricado ocultaba:**

1. **`strategy` y `condition_id` no aparecen.** Existen en el modelo Pydantic, pero valen `None` y el
   escritor omite los nulos. El evento **no lleva hoy la condición de riesgo asociada**: la asociación
   condición ↔ evidencia la hace el plano de control. Si se quiere que el evento la lleve, hay que
   poblarla (es aditivo y barato) — pero **no se puede escribir en el informe que ya la lleva**.
2. **El identificador del conjunto de prompts es `cr01_cr02_v2_short_inline`**, no `cr01_cr02_v2_short`:
   el sufijo `_inline` registra que el conjunto viajó embebido en el disparo de la corrida, no por
   referencia a catálogo. Es trazabilidad real, y conviene no "limpiarla" al transcribir.

### 2.3 Dónde se publica

El mismo payload viaja por dos caminos, **byte-idénticos**:

- **DBE (offline):** se escribe append-only en `runs/<run_id>/detections.jsonl`. El control-plane lo relee.
- **EBE (live):** se publica en el bus dentro de un envelope msgpack.

```python
# media-plane/transport/bus.py:19
ENVELOPE_SCHEMA_VERSION  = "bus.envelope.v1"
DETECTION_TOPIC_PREFIX   = "media.detection.v1."      # topic: media.detection.v1.<media_run_id>
LIFECYCLE_TOPIC_PREFIX   = "run.lifecycle.v1."
```
```jsonc
// envelope (msgpack) — el payload es la MISMA línea que va al JSONL
{ "schema_version": "bus.envelope.v1",
  "topic": "media.detection.v1.run_20260711_211647_...",
  "key": "cb_b01_p7",          // source_id
  "seq": 41,                   // monótono: el hueco de seq es la ÚNICA señal de pérdida
  "ts_publish_ms": 1783804607379.2,
  "payload": <bytes de la línea JSONL> }
```

> **Frase para el capítulo:** *"El evento de percepción se persiste primero y se publica después. El
> payload publicado en el bus es byte-idéntico a la línea persistida, de modo que toda corrida en vivo es
> re-evaluable offline y produce artefactos idénticos (verificado)."*

---

## 3. Las APIs: el sistema es ejecutable por HTTP

El capítulo no tiene una sola interfaz. El sistema tiene dos servicios HTTP config-driven. Esta es la
tabla mínima que responde al "una API: `POST /events/detection`" del tutor.

### 3.1 Plano de medios — `:8080` (FastAPI; `service/app.py:64`)

| Método | Path | Request | Respuesta |
|---|---|---|---|
| `GET` | `/healthz` · `/readyz` | — | `{"status":"ok"}` · `{"status":"ready","model":"<ref>"}` o 503 |
| `GET` | `/api/model` | — | modelo cargado, device, umbrales |
| **`POST`** | **`/api/runs`** | **`RunRequest`** | **201 `{"run_id": "..."}`** · 409 si hay corrida activa · 422 config inválida |
| `GET` | `/api/runs/{run_id}` | — | estado + `summary` |
| `POST` | `/api/runs/{run_id}/stop` | — | 202 |
| `GET` | `/api/runs/{run_id}/detections` | `page`, `page_size` | página de `DetectionEvent` |
| `POST` | `/api/runs/{run_id}/evaluate` | — | `EvalPerceptionResults` (AP@0.5 por clase, `mAP50`, recall CR-01) |
| `WS` | `/api/runs/{run_id}/stream` | — | eventos de la corrida en curso |

```python
# service/run_request.py:49 — el contrato de disparo de una corrida
class RunRequest(BaseModel, extra="forbid"):
    ingest:  IngestSpec           # {plugin: "video_file"|"image_folder"|"rtsp", config: {...}}
    prompts: PromptsSpec          # {set_inline: {...}, active_ids: [...]}
    run:     RunParams            # {stride, max_units, save_annotated_video, save_previews, name}
    bus:     BusSpec | None       # {enabled, endpoint, hwm, wait_for_subscriber_ms}
    experiment_id: str | None     # clave de trazabilidad de la corrida paraguas
```

**Decisión de diseño citable:** el modelo **nunca viaja en el request**. Se carga una vez al arranque del
servicio desde `EOVRT_MODEL_REF`. Un servicio = un modelo cargado; comparar modelos = levantar servicios
distintos. Esto mantiene la ruta crítica libre del costo de carga de pesos (que es de decenas de segundos).

### 3.2 Plano de control — `:8081` (FastAPI; `service/app.py:30`)

| Método | Path | Request | Respuesta |
|---|---|---|---|
| `GET` | `/healthz` · `/readyz` | — | `{"status":"ok"}` |
| **`POST`** | **`/api/runs`** | **`ControlRunRequest`** | **201 `{"control_run_id": "..."}`** · 409 busy |
| `GET` | `/api/runs/current` · `/api/runs/{id}` | — | estado + `summary` |
| `GET` | `/api/runs/{id}/alerts` | `limit` | lista de `AlertEvent` |
| `GET` | `/api/config` | — | config efectiva de la corrida |

```python
# control-plane/service/run_request.py:10
class ControlRunRequest(BaseModel):
    mode: Literal["replay", "live"]
    config_path: str | None       # por referencia
    config: dict | None           # por payload (ADR-009) — exactamente uno de los dos
    experiment_id: str | None
```

**Invariante no negociable, y hay que escribirlo:** el `201` de un `POST` con `mode: live` **implica que el
consumidor del bus ya está suscripto**. ZeroMQ PUB/SUB **pierde todo lo publicado antes de la
suscripción**; por eso el orden de disparo es **control primero, medios después**. El runner lo verifica
antes de disparar el media-plane (`SubscriptionNotConfirmed` bloquea la corrida).

### 3.3 Orquestación

Un tercer componente (runner CLI / webconsole, en `e-ovrt_experimental-setup`) dispara la corrida paraguas
por HTTP contra ambos servicios, propaga el `experiment_id` y consolida los resultados. **La webconsole no
consume el bus**: habla con las APIs (patrón BFF). El bus es interno de la plataforma.

---

## 4. Extensibilidad del evento de inferencia — la respuesta a T3

Este es el punto más sustantivo de la observación del tutor:

> *"Es muy importante ser muy claro en la definición de eventos tipo inferencias para que den soporte a
> datos que a lo mejor hoy no están, pero mañana sí: agregar a las detecciones detecciones asociadas,
> datos de tracking, velocidad, dirección, eventualmente pose o segmentación."*

### 4.1 La regla de evolución (adoptada, spec 40 §1)

1. **Los cambios son siempre aditivos.** Un campo nuevo entra como **opcional con default**, nunca como
   requerido.
2. **Un cambio aditivo no bumpea `schema_version`.** `media.detection.v1` sigue siendo `v1` cuando gana
   `track_id`. Un consumidor viejo ignora el campo nuevo; un consumidor nuevo lo encuentra ausente y usa
   su default.
3. **Cambiar el significado de un campo, o eliminarlo, es ruptura contractual** ⇒ obliga a `v2`.
4. **La versión viaja en el payload**, no en el transporte (`schema_version` es un campo del evento, tanto
   en la línea JSONL como dentro del envelope msgpack). Un artefacto guardado es autodescriptivo: se puede
   releer años después sin conocer el canal por el que viajó.
5. El consumidor tolera artefactos viejos: `DetectionEvent` del control-plane tiene un
   `model_validator(mode="before")` (`contracts/media.py:87`) que absorbe eventos con campos planos legacy.

### 4.2 El camino concreto de cada extensión que el tutor nombró

| Extensión | Camino en el contrato | Estado hoy |
|---|---|---|
| **Tracking (`track_id`)** | Campo opcional de `Detection`. **Ya existe del lado consumidor**: `track_id: str \| None = None` en `control-plane/contracts/media.py:11`, y el motor ya lo usa como identidad (`state_key()`). | **Contrato listo, productor pendiente.** El media-plane no lo emite todavía (spec 42 §3). Por eso `granularity: subject` degrada a escena con causa `no_track_id`. |
| **Velocidad y dirección** | Campos opcionales derivados (`velocity_px_s`, `heading_deg`). No requieren cambiar el evento: requieren `track_id` + los timestamps **que ya viajan** (`source.timestamp_ms`, `capture_monotonic_ns`, `capture_wallclock_ms`). | Especificado; no implementado. |
| **Pose** | Campo opcional (`keypoints`). ⚠️ **Corregido:** el motor **no tiene soporte de pose**. Lo que tiene es una **heurística geométrica**: la región de búsqueda de EPP se ensancha a altura completa cuando la relación de aspecto del bbox sugiere un sujeto no erguido (`full_height_aspect_ratio`, `PatternRegionConfig`, usado en `spatial_absence.py:58`). Decirle "costura de pose" invita a que te pidan el keypoint. | Heurística de aspecto en el evaluador; el evento no lleva keypoints. |
| **Segmentación** | Campo opcional (`mask_rle` / `polygon`), junto al bbox, no en lugar de él. | Especificado; no implementado. |
| **Detecciones asociadas** | Ya modelado, pero **en el plano de control, no en el evento de percepción**: `PatternEvidence` liga el sujeto con sus detecciones de soporte (`supporting[]`) y la clase ausente (`missing_class`). Esa es, por diseño, la capa que asocia detecciones entre sí. | **Implementado.** |

### 4.3 El evento, mostrado con su superficie de crecimiento

> ⚠️ **Corregido tras auditoría.** La versión anterior de este bloque mezclaba valores de tres artefactos
> distintos. Ahora la detección **emitida hoy** es la línea literal de `frame_000120` (la misma de §2.2),
> y lo **previsto** va claramente separado, en comentarios, sin fingir que existe.

```jsonc
{
  "schema_version": "media.detection.v1",     // aditivo ⇒ NO cambia al agregar campos nuevos
  "run_id": "run_20260711_211647_dbe_grounding_dino_6114c6",
  "unit_id": "frame_000120",
  "source":  { "source_id": "cb_b01_p7", "source_type": "video_frame",
               "frame_index": 120, "timestamp_ms": 4000.0, "width": 1920, "height": 1080 },
  "model":   { "name": "grounding_dino",
               "model_id": "IDEA-Research/grounding-dino-tiny", "device": "cuda" },
  "prompts": { "prompt_set_id": "cr01_cr02_v2_short_inline" },
  "detections": [
    {
      // ================= EMITIDO HOY (línea literal del artefacto) =================
      "detection_id": "det_000002",           // índice por frame: NO es identidad entre frames
      "label": "person", "confidence": 0.837,
      "bbox_xyxy":      [159.5, 402.2, 253.4, 639.8],
      "bbox_norm_xyxy": [0.0831, 0.3724, 0.132, 0.5924],
      "prompt_id": "person", "source_prompt": "person",
      "area_px": 22312.3, "model_name": "grounding_dino"

      // ============ PREVISTO: aditivo, opcional, sin bump de versión ==============
      // "track_id":      "trk_017",      // única identidad válida entre frames (spec 42 §3)
      // "velocity_px_s": [12.4, -3.1],   // derivable de track_id + timestamps ya presentes
      // "heading_deg":   104.2,
      // "keypoints":     [ ... ],        // pose
      // "mask_rle":      "...",          // segmentación
      //
      // "strategy" y "condition_id" existen en el modelo pero hoy valen null y no se
      // serializan. Poblarlos es aditivo y barato — pero HOY NO ESTÁN EN EL EVENTO.
    }
  ],
  "timing": { "normalize_ms": 8.25, "inference_ms": 214.37,
              "postprocess_ms": 0.2, "write_ms": 0.0, "total_ms": 214.59 }
}
```

> **Frase para el capítulo (la que responde al tutor):** *"El contrato del evento de percepción está
> diseñado para crecer sin romperse: los campos nuevos entran como opcionales con valor por defecto y no
> bumpean la versión del esquema, de modo que un consumidor escrito contra `media.detection.v1` sigue
> siendo válido cuando el evento incorpora identidad de sujeto, cinemática, pose o segmentación. La
> identidad de sujeto (`track_id`) ya está prevista en el contrato y consumida por el motor de patrones;
> el productor no la emite en la versión evaluada, y por esa razón el núcleo opera sobre granularidad de
> escena. Se declara explícitamente: `detection_id` es un índice por frame y **no** una identidad entre
> frames — usarlo como identidad produce aliasing medible: sobre una corrida de vídeo real, la etiqueta
> `det_000001` recorre 1831 px del ancho del cuadro (de 1920 px) a lo largo de la corrida, con saltos de
> hasta ~1750 px entre cuadros consecutivos."*

> ⚠️ **Corregido tras auditoría.** La formulación anterior decía "recorre 1831 px **entre frames
> consecutivos**", y eso es **falso**: los 1831 px son el **rango total** recorrido a lo largo de la
> corrida; el **salto máximo entre cuadros consecutivos es ~1749 px**. Ambos números destruyen la
> hipótesis de identidad, así que el argumento no se debilita — pero la afirmación original era
> verificable y falsa, que es la peor combinación posible en una defensa.

Ese dato es el que convierte una limitación en un argumento: no elegimos escena por comodidad,
elegimos escena porque **medimos** que la alternativa disponible era identidad falsa.

---

## 5. El plano de control: los otros dos eventos

### 5.1 `PatternStateChanged` — `control.pattern_state.v1`

```python
# control-plane/contracts/pattern.py:31
class PatternStateChanged(BaseModel):
    schema_version: str = "control.pattern_state.v1"
    control_run_id: str
    media_run_id: str
    unit_id: str
    source_id: str
    pattern_id: str
    condition_id: str
    subject_key: str                  # "CR-01:cb_b01_p7" bajo escena
    previous_state: str               # inactive | candidate | confirmed | sustained | resolved
    state: str
    severity: str                     # high | medium
    evidence: PatternEvidence
    first_evidence_ms: float          # hito 1 de los cinco obligatorios
    first_evidence_unit_id: str       # clave de join con las métricas del plano de medios
    experiment_id: str | None
```

`subject_key` merece una línea en el capítulo, porque materializa ADR-002:
`f"{pattern_id}:{source_id}"` bajo `granularity: scene`, `f"{pattern_id}:{source_id}:{track_id}"` bajo
`subject`. El docstring del evaluador lo dice sin ambigüedad: *"`detection_id` NO se usa como identidad,
nunca"*.

### 5.2 `AlertEvent` — `control.alert.v1` (la alerta del **benchmark**, no de un smoke)

> ⚠️ **Corregido tras auditoría.** La versión anterior mostraba la alerta de la corrida **mock** (el smoke
> de plomería de `clip_id`), que confirma en 4033,33 ms. La alerta de abajo es la del **benchmark real con
> GDINO-tiny** sobre `cb_b01_p7`, reproducido y archivado el 2026-07-12 en
> `operacion/datos/95-2026-07-12-bench-cb_b01_p7-gdino-alerts.jsonl`. Confirma en **4000,0 ms exactos**.
> Si vas a poner un JSON al lado del número `t_alert-system = 4000 ms`, tiene que ser **este**.

```json
{ "schema_version": "control.alert.v1", "event_type": "alert_event",
  "control_run_id": "bench_cb_b01_p7_gdino_20260712_20260712T232146Z",
  "media_run_id":   "run_20260711_211647_dbe_grounding_dino_6114c6",
  "alert_id": "ff1ffb62-60a9-5e19-a7b8-42d076864f14",
  "pattern_id": "CR-01", "condition_id": "CR-01",
  "subject_key": "CR-01:cb_b01_p7", "source_id": "cb_b01_p7",
  "severity": "high", "state": "open",
  "unit_id": "frame_000120", "frame_index": 120, "timestamp_ms": 4000.0,
  "evidence": {
    "subject": { "detection_id": "det_000013", "label": "person", "confidence": 0.502,
                 "bbox_xyxy": [1065.4, 1005.4, 1185.9, 1081.2] },
    "missing_class": "helmet",
    "supporting": [ { "detection_id": "det_000021", "label": "person", "confidence": 0.4016 },
                    { "detection_id": "det_000022", "label": "person", "confidence": 0.4147 } ],
    "score": 0.502, "subjects_in_evidence": 3,
    "rationale": "No se encontro evidencia 'helmet' en region 'upper_body' de 3 sujeto(s)." },
  "frame_index": 120, "timestamp_ms": 4000.0, "subjects_in_evidence_max": 6,
  "first_evidence_ms": 230525124.622, "first_evidence_unit_id": "frame_000000",
  "alert_registered_ms": 230525159.420,
  "experiment_id": null }
```

Cuatro cosas para señalar en el texto:

1. **`alert_id` es un uuid5 determinista** (`pattern_engine.py:517`) ⇒ la alerta es **idempotente**:
   reprocesar la misma corrida produce el mismo identificador, y un consumidor aguas abajo puede
   deduplicar sin estado compartido.
2. **`rationale` en lenguaje natural + `subject` + `supporting[]` + `missing_class`**: la evidencia de la
   ausencia es **auditable**. Es el argumento a favor de E-IND frente al prompt de negación, hecho
   artefacto. Esto es lo que un prompt de negación **no puede darte**.
3. **La alerta confirma en `timestamp_ms: 4000.0`** — exactamente la ventana de persistencia configurada
   para CR-01. El sistema hace lo que su configuración declara, al milisegundo.
4. **`experiment_id: null`**: esta corrida se disparó por CLI, sin manifiesto paraguas. Es honesto y vale
   la pena verlo — el campo existe y viaja; en esta corrida puntual no se lo pobló.

---

## 6. Configuración: los valores efectivos (que el capítulo nunca da)

El capítulo no contiene **una sola cifra**. Estos son los valores que gobiernan el núcleo validable hoy.

### 6.1 Pattern set oficial — `control-plane/configs/patterns/cr01_cr02_v2.yaml`

```yaml
pattern_set:
  id: cr01_cr02_v2
  patterns:
    - id: CR-01                       # persona sin casco
      severity: high
      subject_class: person
      required_absent_class: helmet
      granularity: scene              # ADR-002 — G0 es el núcleo
      region:   { type: upper_body, y_min_ratio: 0.0, y_max_ratio: 0.45, x_margin_ratio: 0.12 }
      evidence: { min_subject_confidence: 0.35, min_absent_class_confidence: 0.25,
                  min_subject_area_px: 400.0 }
      timing:   { confirm_after_ms: 4000.0, resolve_after_ms: 2000.0 }

    - id: CR-02                       # persona sin chaleco
      severity: medium
      required_absent_class: vest
      granularity: scene
      region:   { type: torso, y_min_ratio: 0.25, y_max_ratio: 0.85, x_margin_ratio: 0.08 }
      timing:   { confirm_after_ms: 7000.0, resolve_after_ms: 3000.0 }
```

**El pattern set oficial no configura `cooldown`** ni memoria de cobertura.

> ⚠️ **Matiz obligatorio (corregido tras auditoría).** No escribas "el cooldown no existe en el motor":
> **sí existe** — `PatternTimingConfig.realert_cooldown_ms` / `realert_cooldown_frames`
> (`control-plane/config.py:82-83`) y `PatternEngine._cooldown_ok()` (`engine/pattern_engine.py:477-499`).
> Lo que ocurre es que **el pattern set oficial lo deja sin configurar (`None` ⇒ desactivado)**, y ADR-011
> §3 lo declara literalmente *"capacidad no usada por la plataforma"*: la política de supresión vive en el
> tramo de distribución. La formulación correcta para el informe es **"el motor no suprime: emite en cada
> confirmación, porque el conjunto de patrones adoptado no configura supresión"**, no "el motor no puede
> suprimir". Si alguien abre `pattern_engine.py` y encuentra un cooldown que el informe negaba, el daño es
> mayor que el beneficio de la frase simple.

Y **sin memoria de cobertura** (ADR-012: inaplicable bajo escena — la histéresis subsume el parpadeo del
detector).

**Alineación con el informe:** CR-01 → `high`, persistencia 4000 ms (banda del informe: alto, 3–5 s ✓).
CR-02 → `medium`, persistencia 7000 ms (banda: medio, 5–10 s ✓). La persistencia se expresa **en
milisegundos, no en frames**, como exige §17.1.5.3.3.

### 6.2 Umbrales del plano de medios (`config/schemas.py`)

`box_threshold 0.35` · `text_threshold 0.25` · `confidence_threshold 0.25` · `iou_threshold 0.50` ·
postproceso `min_confidence 0.25`, `min_box_area_px 100.0` · `rate_control.stride 1`, `max_queue_size 8`.

### 6.3 Prompt set del núcleo (E-IND) — `experimental-setup/prompts/cr01_cr02_v2_short.yaml`

`person` (rol: entidad) · `helmet`, `vest` (rol: EPP). Evidencia **positiva**: la ausencia no se pregunta
al modelo, se **infiere** en el plano de control. Es la materialización de ADR-001.

---

## 7. Cómo se mide (definiciones operacionales)

El tutor pidió "cómo se mide para saber si funciona bien". Estas son las definiciones **implementadas**,
no las deseadas. Cada una tiene t0, t1 y su condición de aplicabilidad.

| Métrica | t0 | t1 | Implementación |
|---|---|---|---|
| **G2A** | captura de la unidad (`capture_monotonic_ns`) | fin de la inferencia | `MetricSample.g2a_ms` por unidad + `G2ASummary` p50/p95/p99 + `p95_within_budget: bool`. Presupuesto declarado: **50–250 ms**. |

> 🔴 **HALLAZGO CORREGIDO — leer antes de escribir una sola línea sobre G2A.**
> El número que veníamos citando (**p50 14,7 ms / p95 31,8 ms, "dentro de presupuesto"**) es de una corrida
> con **detector `mock`** (doc 39: `EOVRT_MODEL_REF=mock`, 20 unidades). **No es evidencia de que el sistema
> cumpla el presupuesto.**
>
> La corrida **real** con GDINO-tiny sobre `cb_b01_p7` (`summary.json` archivado) dice:
> **`g2a: p50 2214,2 ms · p95 2604,1 ms · p95_within_budget: false`** — un orden de magnitud **por encima**
> del presupuesto 50–250 ms.
>
> **No lo escondas: convertilo en hallazgo.** Es exactamente el mismo resultado que el conflicto
> CR-01 ↔ tiempo real del doc 31 (GDINO sostiene CR-01 pero sólo sigue el 14–22 % del ritmo de cámara), y
> refuerza la tesis en vez de debilitarla: *la instrumentación **funciona** — mide, compara contra el
> presupuesto y **declara el incumplimiento sola** (`p95_within_budget: false`)*. Un instrumento que sólo
> devuelve verdes no es un instrumento.
>
> Formulación correcta para el informe: *"la instrumentación de G2A opera y detecta el incumplimiento: con
> detector de referencia el p95 es de 31,8 ms (dentro del presupuesto), mientras que con el detector
> open-vocabulary evaluado el p95 asciende a 2604 ms y el sistema lo declara fuera de presupuesto. La
> latencia del detector, y no la instrumentación, es la restricción operativa."*
| **TTFD** | inicio del episodio en el GT | primera detección positiva dentro del episodio | `_ttfd_for_episode` (`evaluation/temporal.py:438`). Si no hay ninguna: **`None` + `no_positive_detected`** — nunca 0.0 por defecto. |
| **`t_alert-system`** | inicio anotado del episodio | alerta interna registrada | `avg_latency_ms_from_episode_start`. |
| **TTFA interna** | `first_evidence_ms` | `alert_registered_ms` | percentiles en `RunSummary.ttfa_internal_ms_percentiles`. |
| **SDR** | — | — | fracción del episodio `[start,end]` cubierta por detección positiva continua; tramos con hueco ≤ paso nominal se fusionan; clampeado a `[0,1]` (`_sdr_for_episode`, `:457`). |
| **Precision / Recall / F1** | — | — | a **nivel episodio**, con ventana de matching en ms. `precision = matched / (matched + unexpected)`: las **re-alertas no entran al denominador** (ADR-011), y los `sub_threshold_events` tampoco. |
| **`t_capture→alert`** *(derivada propia)* | captura del frame de primera evidencia | alerta registrada | Join entre planos por `first_evidence_unit_id`. **Identidad declarada:** `t_alert-system = TTFD + t_capture→alert`. |

**Criterio de detección positiva** (y esto es importante, porque cierra el círculo): el evaluador **no
reimplementa** el criterio — reusa el evaluador real del motor
(`evaluate_spatial_absence(event, pattern).evidences != []`). El artefacto lo declara literalmente:
`"positive_criterion": "spatial_absence(cr01_cr02_v2) >=1 evidencia"`. No hay dos definiciones de "positivo"
que puedan divergir en silencio.

**Criterio de relojes** (el hueco de la Etapa 3): las latencias intra-nodo usan reloj monotónico local; las
end-to-end se miden **en un solo reloj**. **Los monotónicos de dos hosts no se restan** — en two-node, G2A
se declara `not_interpretable / cross_node_monotonic_clock` y `g2a_ms` va `null`. No se publica un número
que no significa nada.

**Estados de aplicabilidad** (§17.3.13.3, hecho campo literal):
`computed | applicable_not_computed | not_applicable | not_interpretable`, siempre con `cause`. Ejemplos
reales del `report.json`: `t_alert→notification` → `not_applicable / no_distribution` (no hay canal);
`t_capture→alert` → `not_interpretable / dbe_media_time` (reloj de medio, no de pared).

---

## 8. Artefactos de una corrida (el "sistema ejecutable y verificable")

```
media-plane   runs/<run_id>/
              ├── detections.jsonl        # media.detection.v1, append-only
              ├── metrics.jsonl           # media.metric.v2 (incluye g2a_ms por unidad)
              ├── errors.jsonl
              ├── summary.json            # media.summary.v2
              ├── effective_config.yaml   # config efectiva (credenciales redactadas)
              ├── run_manifest.json       # incluye code_version: "<git sha>"
              └── run_provenance.json     # dataset, split, vocabulario, fingerprint de la fuente

control-plane runs/<control_run_id>/
              ├── pattern_events.jsonl    # control.pattern_state.v1
              ├── alerts.jsonl            # control.alert.v1
              ├── alerts.csv              # proyección tabular de las alertas
              └── metrics.jsonl · errors.jsonl · summary.json · effective_config.yaml
              #  temporal_evaluation.json NO vive acá por defecto: lo escribe `evaluate-alerts`
              #  donde apunte su flag -o (normalmente, bajo el run de experimental-setup).

experimental- runs/<experiment_id>/       # la corrida paraguas (ADR-014)
setup         ├── manifest.effective.yaml    # experiment.manifest.v1 (+ clip_id, ground_truth)
              ├── media/    …  control/   …  # lo liviano se copia
              ├── media/detections.ref.json  # lo pesado se REFERENCIA: {run_id, path}
              └── report/{report.json, report.md}
```

**`run_manifest.json` lleva el `code_version` (SHA de git).** Junto con `effective_config.yaml` y el
`run_provenance.json`, cierra la promesa de trazabilidad del §17.3.11.1: **toda alerta se reconstruye hasta
la configuración, el prompt set, el modelo y el commit que la produjeron.**

---

## 9. Puntos de extensión del sistema (el "cómo agrego X")

| Extender con… | Qué hay que tocar |
|---|---|
| **Una fuente nueva** | Implementar `BaseSource` (yield de `VisualUnit`) + una entrada en `PLUGINS` (`sources/registry.py:25`). Hoy: `image_folder`, `video_file`, `rtsp`, `oak_d` (declarado **no disponible** ⇒ 422 explícito, no 500). |
| **Un modelo nuevo** | Subclase de `BaseDetectorAdapter` + rama en `create_adapter()` + un YAML en `configs/models/`. Hoy: `grounding_dino`, `yoloe`, `mock`. |
| **Una condición de riesgo nueva** | **Sólo configuración**, si la condición es del tipo "sujeto sin EPP": una entrada declarativa en el pattern set (clase sujeto, clase ausente, región, umbrales, tiempos) + los prompts. **Cero código.** Este es el mini-experimento A1 (costo marginal de una condición nueva) y es un resultado de tesis en sí mismo. |
| **Un tipo de patrón nuevo** (p. ej. relacional o zonal) | Un evaluador nuevo en `engine/evaluators/`. Hoy sólo existe `spatial_absence`. |
| **Un canal de notificación** | Repo de distribución (spec 45): implementar el canal contra `NotificationEnvelope`. **No implementado.** |

El contraste entre las filas 3 y 4 es, en sí, un argumento de la tesis: **agregar una condición del núcleo
cuesta configuración; agregar una familia nueva de condiciones cuesta un evaluador.** Esa es la frontera
real de la extensibilidad por lenguaje, y conviene medirla y declararla en vez de prometer que "todo es
configurable".

---

## 10. Números canónicos — **la única fuente de verdad para citar cifras**

> **Regla, tras la auditoría del 2026-07-12:** ninguna cifra entra a los docs 91/93/94 —ni al `.docx`— si
> no está en esta tabla. Cada fila dice **qué corrida** la produjo y **con qué detector**, porque la mitad
> de los errores encontrados venían de citar un número de una corrida y atribuirlo a otra.

| Cifra | Valor | Corrida / detector | Artefacto |
|---|---|---|---|
| **Benchmark contra GT temporal** (el número estrella) | **P 0,50 · R 1,00 · F1 0,667 · t_alert-system 4000,0 ms · TTFD 0,0 ms · SDR 0,9986** | `cb_b01_p7`, **GDINO-tiny**, DBE replay, GT **preliminar** | `operacion/datos/95-2026-07-12-bench-cb_b01_p7-gdino-temporal_evaluation.json` ✅ **reproducido y archivado el 2026-07-12** |
| Alertas del benchmark | 2 (CR-01 `high` @ 4000,0 ms · CR-02 `medium` @ 7000,0 ms). 1 TP + 1 FP; `re_alerts: 0` | ídem | `…-gdino-alerts.jsonl` |
| Percepción sobre vídeo real | 733 unidades · **0 fallos** · 15.914 detecciones · p50 220,2 ms · p95 266,8 ms · **4,39 fps** · VRAM 1745 MB | `run_20260711_211647`, **GDINO-tiny**, clip `cb_b01_p7` | `…-gdino-media-summary.json` |
| **G2A con detector real** | **p50 2214,2 ms · p95 2604,1 ms · `p95_within_budget: false`** | ídem (**GDINO-tiny**) | ídem |
| G2A con detector de referencia | p50 14,7 ms · p95 31,8 ms (dentro de 50–250 ms) | doc 39, **mock**, 20 unidades | `operacion/datos/39-…-g2a-video-summary.json` |
| Byte-identidad replay ≡ live | artefactos idénticos; **40/40** unidades, 0 pérdidas | doc 37, **mock** | `operacion/datos/37-…` |
| Cadena live completa por bus | **300/300** unidades, 0 pérdidas, 2 alertas, cierre por `run_finished` | doc 51, **mock** | `operacion/datos/51-…` |
| Gate de granularidad | **F1 = 1,0** en escena y sujeto; 141 personas ⇒ 77 alertas, Σ`subjects_in_evidence_max` = 141 | doc 34, BENCH imágenes | doc 34 |
| "Cero silencioso" sobre imágenes | **77 pattern_events · 0 alertas**, `not_applicable / non_temporal_source` | `bench_images_persistence_probe_20260710` | run del control-plane |
| Aliasing de `detection_id` | rango total **1831 px** de 1920; salto máx. entre cuadros consecutivos **~1749 px** | `run_20260710_011320` | doc 35 |
| Benchmark de modelos OVD | **6 modelos**. GDINO-tiny mAP@0.5 **0,4577**; GDINO-base recall CR-01 **0,586**; YOLOE recall CR-01 **0,000–0,014** (0–1 `bare_head` sobre 69 de GT) | doc 31 | doc 31 (⚠️ sin artefacto primario) |
| Keep-up RTSP | GDINO **14–22 %** · YOLOE **58–69 %** | doc 31 | ídem |
| Suites de test | datasets 102 · media-plane 520 · control-plane 212 · exp-setup 247 | 2026-07-12 | recolectadas |

**Cifras retiradas por la auditoría (NO usar):**
- ~~"137 eventos de patrón / 0 alertas"~~ → el run fue podado. El equivalente vivo da **77 / 0**.
- ~~"G2A p95 31,8 ms ⇒ el sistema cumple el presupuesto"~~ → era **mock**. Con GDINO **no cumple**.
- ~~"1831 px entre frames consecutivos"~~ → 1831 px es el **rango total**.
- ~~"los 5 modelos evaluados"~~ → son **6**.
- ~~SDR 0,803~~ → ese es el **smoke con mock**, no el benchmark. El benchmark da **0,999**.

---

## 11. Checklist de transcripción al `.docx`

- [ ] §17.3.11 — reemplazar el hedge por la tabla de correspondencia (§1) y los tres contratos concretos (§2, §5).
- [ ] §17.3.11.4 — regla de evolución aditiva + evento con superficie de crecimiento (§4). **Es el pedido T3 del tutor.**
- [ ] §17.3.5 — figura nueva: vista de procesos (dos servicios HTTP + bus + orquestador + webconsole).
- [ ] §17.3.8.1 y §17.3.8.4 / §17.3.12 — bus concreto (§2.3) y layout del repositorio (§8).
- [ ] §17.3.6 / Tabla 44 — configuración con **valores efectivos** (§6), y el matiz correcto del `cooldown`.
- [ ] §17.3.13 — diccionario de métricas con t0/t1 (§7), criterio de relojes y estados de aplicabilidad.
- [ ] §17.3.15 — tabla rol → contenedor (Nodo A ≈ EN-1, Nodo B ≈ CPN).
- [ ] §17.3.17/18 — puntos de extensión (§9): **el costo marginal de una condición nueva es configuración**.
- [ ] Sección de verificación — números de la §10 (y sólo esos) + registro de lo no hecho.
