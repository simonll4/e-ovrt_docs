# Spec 42 — media-plane

> **✎ Enmienda 2026-07-18 (doc 56):** la precondición operativa de abajo ya se cumplió
> (working tree de doc 11 §8 commiteado y pusheado) y la mención "hoy hay REQ/REP" del
> §2 quedó vieja: el publisher PUB del bus está implementado y probado (docs 37/50/51).
> El §3 sigue vigente: **nadie produce `track_id` todavía**. Además el media-plane
> implementó piezas que este spec no pedía: `OakDSource` + prefilter EN-2, ledger de
> descartes, sesiones de preview en vivo, `DELETE /api/runs` — inventario en
> [`operacion/56`](../operacion/56-relevamiento-plataforma-2026-07-18.md) §2.1/§3.2.

- **Fecha:** 2026-07-09
- **Estado:** Escrito (núcleo implementado; tracker/`track_id` pendiente)
- **Repo dueño:** `e-ovrt_media-plane` (base: `feature/inference-service` — servicio
  Fase 1 + two-node Fase 2 + visibilidad; doc 11. **Precondición operativa:
  commitear/pushear el working tree pendiente de doc 11 §8 antes de empezar.**)
- **Decisiones que implementa:** ADR-002 (tracker + `track_id`), ADR-003
  (publisher del bus), ADR-004 (`experiment_id`), ADR-009 (config por payload).
  Normativa transversal: **spec 40** (envelope, seq, lifecycle, G2A, relojes).

## 1. Principio

El pipeline (ingesta → rate-gate → normalización → inferencia → postproceso →
persistencia) no cambia de forma. Este spec agrega **dos sinks/etapas opcionales**
(publisher de bus, tracker) y **trazabilidad** — todo desactivable por config, con
el comportamiento actual como default. Cero cambios a `contracts/` salvo campos
opcionales aditivos.

## 2. `BusPublishingArtifactWriter` (ADR-003; doc 05 §4.1)

- **Costura:** decorador del `RunArtifactWriter`, hermano de
  `EventEmittingArtifactWriter` (`service/events.py`) — publica el
  `DetectionEvent` **completo** tras persistirlo (el WS sigue emitiendo resúmenes
  para la consola; son piezas distintas, doc 11 §3).
- **Wire:** envelope `bus.envelope.v1` (spec 40 §3.1) sobre ZeroMQ **PUB** —
  adaptador nuevo en `transport/` (hoy hay REQ/REP; el patrón base/factory se
  reutiliza). `topic = media.detection.v1.<run_id>`, `key = source_id`, `seq`
  monótono por corrida, `payload` = bytes del evento tal cual va al JSONL.
- **Fin de corrida:** en la finalización del run (donde se estampa
  `summary.json`) publica `run.lifecycle.v1 {event: run_finished, media_run_id,
  status}`. En **two-node**, el writer vive en el Nodo B (`run_node_b`), que ya
  garantiza finalización con status explícito (doc 11 §8.1) — el publisher se
  engancha ahí mismo; el Nodo A no publica nada.
- **Reglas (spec 40 §3.2):** no-bloqueante (HWM finito; drop antes que frenar la
  inferencia — el JSONL es la verdad), habilitado por config de corrida:

```yaml
bus: { enabled: false, endpoint: "tcp://0.0.0.0:5557", hwm: 1000 }
```

## 3. Tracker liviano y `track_id` (ADR-002)

> **Bloqueante para el modo `subject`, verificado el 2026-07-10 (doc 34 §4.1).** Hoy
> **nadie produce `track_id`**: `eovrt_labs/perception/tracking.py:311` escribe el id del
> tracker en `detection_id`, que tras G0 ya no se usa como identidad, y el media-plane no
> emite el campo. Consecuencia: un patrón `granularity: subject` **siempre degrada a escena**
> con causa `no_track_id`, y `generate-detections --track` quedó inerte para el motor. El
> port de esta sección es lo que devuelve la vida al modo `subject` (G1) y a los overlays por
> persona.

- **Origen:** puerto de `eovrt_labs/perception/tracking.py` (control-plane, rama
  `mati`): IoU greedy + gates de centro/área + ventanas `max_lost` (ms y frames)
  + firma de apariencia del torso. Se porta el algoritmo con sus tests; labs
  sigue existiendo como herramienta de calibración (no se importa entre repos).
- **Ubicación:** etapa opcional de postproceso, **después** de la normalización y
  del NMS, **antes** de persistir — trackea solo la clase `person` (los sujetos;
  el EPP no se trackea). Determinista dado el stream de detecciones.
- **Contrato:** `Detection.track_id: str | None` (default `None`) — campo
  **opcional aditivo** de `media.detection.v1`, sin bump de versión (spec 40 §1).
  Formato `subject_NNN`, ámbito (run, source). Config:

```yaml
tracking:
  enabled: false            # default: comportamiento actual
  iou_threshold: 0.3
  max_lost_ms: 1500         # y/o max_lost_frames
  appearance: { weight: 0.3, min_similarity: 0.2 }
```

- Los parámetros calibrados en labs (p. ej. `video5_gdino.yaml`: `max_lost_ms`
  3000 por oclusiones largas) son los valores de partida documentados.
- **Sin métricas MOT** (E-10): el único indicador emitido es el conteo de tracks
  creados/perdidos por corrida (diagnóstico de fragmentación) — ΔFP_tracker se
  calcula aguas abajo comparando corridas con/sin tracker (Tabla D.2).

## 4. Trazabilidad y config (ADR-004/009)

1. **`experiment_id`**: aceptado en `POST /api/runs`, persistido en `RunSummary`
   (el campo ya existe — pasa a poblarse siempre que venga) y en
   `effective_config`.
2. **Config por payload:** auditar `POST /api/runs` para que la corrida completa
   pueda declararse por payload (ingest config, prompts inline —ya soportado—,
   `tracking`, `bus`, `experiment_id`). Los **catálogos por id se conservan**
   (datasets, plugins, modelos): el payload referencia ids de catálogo para lo
   que es del despliegue, e incluye valores para lo que es del experimento —
   exactamente la frontera del ADR-009 §2.
3. **Timestamps:** verificación puntual (doc 05 §6.4) de que toda fuente puebla
   `timestamp_ms` en EBE (`RtspSource` ya emite wall-clock; `VideoFileSource`
   emite tiempo de media) — test por fuente.

## 5. Instrumentación G2A (doc 08 §1.8 / acción 7)

Las latencias por sub-etapa ya existen (µs, p50/95/99). Se agrega al summary la
**métrica compuesta G2A** = captura/lectura → resultado algorítmico
(t_capture + t_transport + t_preprocess + t_inference), reportada P50/P95/P99
contra el **presupuesto declarado 50–250 ms**, con warm-up excluido y declarado
(`warmup_units` en config/summary). En two-node, los tramos se reportan por nodo
y el G2A end-to-end se mide en el reloj del Nodo B (criterio de relojes,
spec 40 §4). Este número decide H5 (¿GDINO defendible en EBE?) — mini-ADR en su
momento, con datos.

### 5.1 Insumos de `t_capture→alert` (spec 40 §5.2 — obligatorio, no solo agregado)

El agregado del summary no alcanza: la métrica frame→evento se atribuye **por
alerta**, así que estos campos van **por unidad** en `metrics.jsonl`, con
`unit_id` como clave de join:

| Campo | Significado |
|---|---|
| `unit_id` | clave de join con el control-plane (ya existe) |
| `capture_monotonic_ns` | instante de captura, reloj monotónico del nodo de ingesta |
| `capture_wallclock_ms` | instante de captura, reloj de pared (para cruce entre nodos) |
| `g2a_ms` | compuesta de esta unidad (no solo sus componentes) |

**Semántica de la captura por fuente** (importa para la aplicabilidad, spec 40
§5.2.3, y para ADR-013). Tres regímenes, no dos:

| Fuente | `source_type` | `timestamp_ms` | `source_clock` | `t_capture→alert` |
|---|---|---|---|---|
| `RtspSource` | `video_frame` | wall-clock de llegada del frame | `wallclock` | latencia genuina → `computed` |
| `VideoFileSource` | `video_frame` | **tiempo de medio** | `media` | `not_interpretable / dbe_media_time` |
| `ImageFolderSource` | `image` | **`None`** (unidades independientes, sin tiempo) | `none` | `not_applicable / non_temporal_source` |

En los tres casos `capture_monotonic_ns` marca cuándo el proceso leyó la unidad, de
modo que `t_compute-budget` es siempre `computed`.

El media-plane **declara qué tipo de reloj emite cada fuente** en el summary
(`source_clock: wallclock | media | none`) — sin ese campo el reporte no puede
decidir el estado de aplicabilidad. `none` es la declaración de fuente **no
temporal**: sobre ella la evaluación de patrones es `not_applicable` (ADR-013), y
`source_type: "image"` es la señal que ya viaja en cada `DetectionEvent` para que el
control-plane lo detecte sin configuración adicional.

## 6. Orden de implementación sugerido

1. Commit/push del working tree pendiente (doc 11 §8) — precondición.
2. `experiment_id` + auditoría de config por payload (§4) — gate: corrida por API
   con payload completo y summary poblado.
3. Adaptador PUB en `transport/` + `BusPublishingArtifactWriter` + lifecycle (§2)
   — gate: consumidor de prueba recibe N eventos = N líneas del JSONL + END
   (insumo directo del test de paridad del spec 41).
4. Tracker + `track_id` (§3) — gate: tests del algoritmo portados + corrida sobre
   video de prueba con `track_id` estable visible en `detections.jsonl`.
5. G2A en summary + insumos por unidad de `t_capture→alert` (§5, §5.1) — gate:
   summary con G2A P50/95/99, warm-up y `source_clock` declarados; `metrics.jsonl`
   con los tres campos por `unit_id`.

## 7. Criterios de terminado (evidencia)

- [ ] Corrida con `bus.enabled: true` publicando eventos completos + lifecycle;
      verificada contra el `BusSource` del control-plane (integración spec 41).
- [ ] Corrida con `tracking.enabled: true` sobre video real: `track_id` presente,
      estable a lo largo de frames, `None` cuando está deshabilitado (contrato
      intacto para consumidores viejos).
- [ ] `experiment_id` de un `POST /api/runs` recuperable en `RunSummary` y
      `effective_config` (eslabón de la cadena de reconstrucción, spec 40 §2).
- [ ] G2A P50/P95/P99 en el summary de una corrida RTSP, contra presupuesto.
- [ ] `metrics.jsonl` con `capture_monotonic_ns`, `capture_wallclock_ms` y
      `g2a_ms` por `unit_id`, y `source_clock` declarado en el summary — los
      insumos de `t_capture→alert` (spec 40 §5.2.4) verificados con un join
      manual contra una alerta del control-plane.
- [ ] Two-node: run con publisher activo en Nodo B finaliza con `run_finished`
      publicado y summary estampado (los 3 escenarios de doc 11 §8.4 siguen
      pasando).

## 8. Interfaces

- **Spec 41:** el control-plane consume este bus (envelope común) y prefiere
  `track_id` como `subject_id` en patrones G1.
- **Spec 44:** el runner/webconsole disparan con `experiment_id` y config por
  payload; la consola sigue leyendo WS/artefactos por HTTP (no el bus).
- **Spec 43 (diferido):** los clips se consumen por `VideoFileSource` (DBE) y
  como RTSP loop (EBE) sin cambios adicionales aquí.
