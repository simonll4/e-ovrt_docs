# Integración media-plane → control-plane vía bus de eventos

> ⚠️ **2026-08-10 — DOCUMENTO HISTÓRICO.** Diseño del acople por bus, previo a
> implementarlo. **El bus existe y está ejercido** (ADR-003). Para cómo quedó: **`../17`**
> §6, **`../18`** §6 y `../../operacion/37`. Ver el `README.md` de esta carpeta.

- **Fecha:** 2026-07-06
- **Estado:** Ideas / pre-diseño (la tecnología de bus — Kafka u otro broker — se decide más adelante)
- **Referencias:** `01-relevamiento-control-plane.md`,
  `06-diseno-distribucion-alertas.md` (§5 primitivas de bus, §17 evolución a broker)

## 1. Situación actual

```
media-plane (servicio FastAPI)                    control-plane (CLI replay)
POST /api/runs → pipeline → detections.jsonl ──(archivo, offline)──► eovrt-control replay
                          → WS /stream (solo resúmenes: type/unit_id/count)
```

- La integración **por archivo ya funciona**: `replay_dbe_cr01_cr02.yaml` apunta a
  `../../e-ovrt_media-plane/runs/latest/detections.jsonl` y los contratos son
  wire-compatibles (`media.detection.v1` ↔ `contracts/media.py::DetectionEvent`).
- El WS del media-plane **no sirve como bus**: `EventEmittingArtifactWriter` emite
  resúmenes livianos para la webconsole (`{"type":"detection","unit_id":…,"count":…}`),
  no el `DetectionEvent` completo que necesita el motor de patrones.
- El media-plane ya tiene una abstracción de transporte (`transport/`: base, factory,
  memory, network ZeroMQ REQ/REP, msgpack) usada por la topología two-node (EBE).

## 2. Objetivo

Reemplazar el acople por archivo por un **bus de eventos** `media → control`, de modo que:

1. El control-plane consuma `DetectionEvent`s **en vivo** (EBE) además del replay (DBE).
2. Varios consumidores puedan leer el mismo stream (control-plane, webconsole, futuros
   módulos de la plataforma) → semántica **fan-out**, no cola punto a punto.
3. La elección de tecnología (ZeroMQ PUB/SUB vs broker Kafka/RabbitMQ/NATS) quede
   encapsulada detrás de interfaces, decidible más adelante sin reescribir lógica.

## 3. Principio rector: el contrato es el bus

Lo estable es el **evento versionado**, no el transporte. Propuesta de envelope (alineada
con §5 del diseño de distribución de alertas, wire-compatible msgpack):

```
{ schema_version, topic, key, ts_publish_ms, payload }
```

- `payload` = `DetectionEvent` (`media.detection.v1`) serializado tal cual se persiste hoy.
- `topic` = jerárquico, p.ej. `media.detection.v1.<run_id>` (y a futuro
  `control.alert.v1.<severity>` para el tramo de distribución).
- `key` = `unit_id` (o `source_id`) — clave de particionado/dedup si hay broker.
- Regla ya adoptada por el proyecto (ADR propuesto en el diseño de alertas): **el log
  persistido es la fuente de verdad; el bus transporta, no almacena**. `detections.jsonl`
  y `alerts.jsonl` se siguen escribiendo siempre → cualquier corrida en vivo es también
  reproducible offline (paridad DBE/EBE).

## 4. Costuras (seams) en cada repo

### 4.1 Media-plane: publicar (cambio pequeño)

El patrón decorador ya existe. Igual que `EventEmittingArtifactWriter` decora al writer
para el WS, un `BusPublishingArtifactWriter` (o un segundo sink) publica el
`DetectionEvent` **completo** al `BusPublisher` después de persistirlo:

```
RunArtifactWriter (persistencia, verdad)
  └─ EventEmittingArtifactWriter (WS, resúmenes)      ← existe
  └─ BusPublishingArtifactWriter (bus, evento completo) ← nuevo, ~50 líneas
```

- No toca pipeline ni modelos; se habilita por config de corrida (`bus: {type, endpoint, …}`).
- El publish debe ser **no bloqueante** (HWM/drop o cola interna): la inferencia nunca
  espera al bus; la durabilidad la da el JSONL.

### 4.2 Control-plane: consumir (cambio mediano)

- **Fuente:** hoy `sources/media_jsonl.py` es el único acople. Introducir una interfaz
  `MediaEventSource` (iterador de `(event | error)`) con tres implementaciones espejo de
  `AlertStreamSource` del diseño de alertas:
  - `JsonlSource` — la actual (DBE, replay).
  - `MemorySource` — in-process para tests/DBE determinista.
  - `BusSource` — suscriptor del bus (EBE); mismo motor, otra fuente.
- **Runtime:** `runtime/replay.py` asume corrida finita. Agregar `runtime/live.py`
  (o parametrizar): consume hasta señal de stop / fin de run del media-plane
  (evento `run_finished` en el bus o sentinela END como en el transporte two-node),
  escribe los mismos artefactos JSONL, y emite `summary.json` al cierre.
- El motor (`PatternEngine.process(event)`) **no cambia**: ya es push-based por evento.

## 5. Riesgo de integración nº 1: identidad estable del sujeto

La persistencia temporal del control-plane (confirm/resolve por ms o frames) se apoya en
`subject_key`, que usa el `detection_id` del media-plane. Pero el media-plane genera
`det_{idx:06d}` **por frame** (índice de orden, `detection_normalizer.py`) — no es
identidad: en video real el mismo id puede ser personas distintas frame a frame.

Esto ya está reconocido como pendiente en ambos lados ("el plano de control no realiza
tracking; la identidad estable debe venir del plano de medios"). Para la integración EBE
hay que resolverlo **antes o junto con** el bus:

- **Opción A (recomendada como primer paso):** tracking liviano en el media-plane
  (IoU/centroid tracker post-normalización, p.ej. ByteTrack-lite sin apariencia) que
  emita `track_id` en `Detection`. Extensión de contrato aditiva → `media.detection.v2`
  o campo opcional en v1.
- **Opción B:** asociación por solapamiento en el control-plane (matching greedy del
  bbox del sujeto entre frames consecutivos). Menos invasiva pero contradice el ADR de
  que la identidad viene del plano de medios, y duplica trabajo si la webconsole también
  la necesita.
- Mientras tanto, con `confirm_after_frames: 1` (config `cr01_cr02_v1` actual) el
  problema no bloquea las primeras corridas DBE reales — sólo bloquea la persistencia
  temporal real.

## 6. Otras alineaciones de contrato a resolver

1. **Vocabulario:** canonical_v2 = `person, helmet, vest, bare_head`. El evaluador cubre
   los tres primeros con alias; **`bare_head` no se usa**. Idea: usarlo como **evidencia
   positiva directa** de CR-01 (persona con cabeza descubierta), combinable con la
   inferencia espacial de ausencia (OR o votación). Ojo: Sprint 2 mostró `bare_head`
   débil en zero-shot en todos los modelos — calibrar antes de dársela como señal fuerte.
2. **`run_id` vs stream continuo:** el control-plane etiqueta todo con `media_run_id`.
   En EBE con RTSP el "run" del media-plane puede ser largo/continuo; definir semántica
   de corrida del control-plane (¿1:1 con run de media? ¿ventanas temporales?).
3. **Evento de fin de corrida:** el bus necesita señal `run_finished` (o el control-plane
   la infiere por timeout) para cerrar `summary.json`.
   *Actualización 2026-07-09 (doc 11 §8):* el media-plane ya garantiza `summary.json`
   con `status: succeeded|failed` explícito también en two-node, y `GET /api/runs/{id}`
   reporta `running`/`live` para corridas en curso de otros procesos — el `BusSource`
   puede cerrar por señal del bus con **polling de estado como fallback** sin diseño extra.
4. **Timestamps:** `timestamp_ms` es la base de la persistencia temporal preferida.
   `RtspSource` ya emite wall-clock; verificar que todas las fuentes lo pueblen en EBE.
5. **Backpressure:** el control-plane procesa en sub-ms por evento (motor trivial hoy),
   pero si crece, definir política (drop-oldest en el suscriptor, como el rate_gate del
   media-plane).

## 7. ZeroMQ vs broker (Kafka) — criterios para decidir después

La decisión se difiere, pero las interfaces (§3–4) hacen que sea intercambiable. Criterios:

| Criterio | ZeroMQ PUB/SUB | Broker (Kafka/Redpanda/NATS JetStream) |
|---|---|---|
| Peso operacional (WSL/Docker de la plataforma) | Mínimo (lib embebida; ya es dependencia) | Un servicio más en `infra/platform/` (Redpanda/NATS son livianos; Kafka clásico no) |
| Fan-out multi-consumidor | Sí (PUB/SUB) | Sí (consumer groups) |
| Durabilidad / replay desde el bus | No (si no estás suscripto, lo perdiste; mitigado porque el JSONL es la verdad) | Sí — offsets = replay DBE natural desde el propio bus |
| Redelivery / at-least-once | No aplica | Sí → exige idempotencia (ya la hay: `alert_id` uuid5 determinista; ledger del módulo de distribución) |
| Alineación con lo ya construido | Alta (transport/ two-node, diseño de alertas) | Nueva pieza |
| Valor para el TFG | Simplicidad, foco en la lógica | Argumento arquitectónico "plataforma de eventos" más fuerte |

Lectura pragmática: **empezar con ZeroMQ PUB/SUB** (paridad total con lo existente, cero
infraestructura nueva) y dejar `BrokerSource`/`BrokerPublisher` como implementación
adicional si el TFG o la plataforma piden durabilidad/replay en el bus. Es exactamente el
seam que el diseño de distribución de alertas ya documenta en §17. Si se elige broker,
preferir **Redpanda o NATS JetStream** sobre Kafka clásico por el costo operacional en
WSL (memoria del ecosistema Docker ya es un tema sensible en este entorno).

## 8. Fases propuestas

- **Fase 0 — hoy mismo, sin bus:** correr `eovrt-control replay` sobre un
  `detections.jsonl` real (pendiente nº1 del control-plane). Valida contratos y calibra
  thresholds con datos reales. No requiere código nuevo.
- **Fase A — contrato + fuente abstracta (DBE):** `MediaEventSource` en control-plane
  (`jsonl` + `memory`), envelope versionado compartido, tests de paridad
  replay-vs-stream con el fixture temporal. Resultado: el motor es agnóstico de la fuente.
- **Fase B — bus ZeroMQ (EBE local):** `BusPublishingArtifactWriter` en media-plane +
  `BusSource` en control-plane sobre PUB/SUB; ambos en la plataforma Docker
  (`e-ovrt_experimental-setup/infra/platform/`), encajando con la topología two-node ya
  verificada. Señal de fin de run. Demo en vivo: RTSP → detecciones → alertas.
- **Fase B' — identidad estable (paralelo a B):** `track_id` en media-plane (§5 opción A)
  y `subject_key` del control-plane preferiéndolo. Habilita `confirm_after_ms` real.
- **Fase C — broker (opcional/diferido):** implementación `Broker*` del mismo contrato si
  se decide Kafka/Redpanda/NATS; el resto del código no cambia.

## 9. Panorama de la plataforma resultante

```
                         ┌────────────────────────────────────────────┐
 RTSP / video / imgs ──► │ media-plane (GPU)                          │
                         │  ingest → inferencia → normalize → persist │
                         └───────┬───────────────────────┬────────────┘
                                 │ detections.jsonl      │ bus: media.detection.v1
                                 ▼ (verdad, replay DBE)  ▼ (fan-out)
                    ┌────────────────────┐   ┌──────────────────────────┐
                    │ webconsole (live)  │◄──┤ control-plane            │
                    └────────────────────┘   │  PatternEngine → alerts  │
                                             └──────┬───────────────────┘
                                                    │ bus: control.alert.v1
                                                    ▼
                                     módulo de distribución de alertas
                                     (MQTT / Telegram / webhook / dashboard,
                                      diseño 2026-07-04)
```

Un solo patrón de bus (envelope + publisher/subscriber) sirve para los dos tramos:
`media → control` (este documento) y `control → distribución` (diseño ya escrito). Las
primitivas `transport/` deberían terminar extraídas a un paquete compartido o duplicadas
wire-compatible, como ya propone el diseño de alertas.

## 10. Preguntas abiertas

1. ¿Semántica de corrida del control-plane en streams continuos (RTSP): 1:1 con run de
   media, o ventanas propias?
2. ¿`track_id` como campo nuevo opcional de `media.detection.v1` o bump a `v2`?
3. ¿El control-plane pasa a servicio (FastAPI, espejo del media-plane) en Fase B, o sigue
   siendo proceso CLI de larga vida suscripto al bus? (El diseño de distribución sugiere
   CLI primero.)
4. ¿La webconsole consume el bus directamente o sigue con el WS del media-plane?
