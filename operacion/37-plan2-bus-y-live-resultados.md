# Plan 2 — bus media→control y runtime live: resultados

- **Fecha:** 2026-07-10
- **Qué cubre:** ítems 2 y 3 del orden de implementación de la spec 41 §10
  (`MediaEventSource`; `BusPublishingArtifactWriter` + `BusSource` + runtime live).
- **Plan ejecutado:** `e-ovrt_control-plane/docs/superpowers/plans/2026-07-10-plan2-bus-y-runtime-live.md`
- **Estado:** completo, **sin commitear** (regla del workspace: los commits los pide el usuario).
- **ADRs que implementa:** ADR-003 (bus ZeroMQ), ADR-007 (corrida 1:1). Normativa: spec 40 §3.

## 1. Qué quedó construido

| Repo | Pieza | Archivo |
|---|---|---|
| media-plane | `encode_envelope` + `BusPublisher` (XPUB, HWM, `seq`) | `src/eovrt_media/transport/bus.py` |
| media-plane | `BusPublishingArtifactWriter` (decorador del `RunArtifactWriter`) | `src/eovrt_media/service/bus_writer.py` |
| media-plane | cableado + `run.lifecycle.v1/run_finished` | `runtime/pipeline.py`, `runtime/two_node.py` |
| media-plane | config `bus` (apagada por default) | `config/schemas.py`, `service/run_request.py` |
| control-plane | interfaz `MediaEventSource` + `JsonlSource` + `MemorySource` | `src/eovrt_control/sources/{base,jsonl,memory}.py` |
| control-plane | `BusSource` (SUB, huecos de `seq`, lifecycle, polling, drenaje acotado) | `src/eovrt_control/sources/bus.py` |
| control-plane | bucle del motor, agnóstico de la fuente | `src/eovrt_control/runtime/core.py` |
| control-plane | runtime live 1:1 + CLI `live` | `src/eovrt_control/runtime/live.py`, `cli.py` |
| control-plane | **gate** de paridad replay↔stream | `tests/test_bus_parity.py` |

`RunSummary` del control-plane gana cuatro campos aditivos: `media_run_id`, `experiment_id`,
`source` (`jsonl|memory|bus`) y `bus_dropped_events`. Sin bump de `schema_version`.

## 2. Suites (medidas, no supuestas)

| Repo | Antes | Después | Lint |
|---|---|---|---|
| control-plane (`pytest -q --ignore=tests/labs`) | 57 passed | **89 passed** | `ruff`: limpio |
| media-plane (`pytest -q`) | 440 passed | **456 passed** | `ruff`: limpio |

`tests/labs/` del control-plane sigue rojo por `numpy` ausente en el extra dev (conocido,
no bloqueante). El extra `dev` del control-plane ahora incluye `pyzmq` y `msgpack`.

## 3. Gate de paridad replay↔stream (spec 40 §3.4)

Corriendo el fixture `cr01_cr02_temporal` (12 eventos, `source_type: "video"`) con el pattern
set `cr01_cr02_temporal_eval` por ambas vías: **12 unidades, 8 `pattern_events`, 2 alertas,
`pattern_evaluation: computed`, no degradada, `bus_dropped_events: 0`** — artefactos idénticos
módulo `control_run_id` y `alert_id` (este último deriva del primero).

**El gate fue verificado significativo por mutación** (un gate que no puede fallar no es un gate):

| Mutación | Resultado | Lectura |
|---|---|---|
| El publicador saltea un evento | **falla** | detecta pérdida de eventos |
| 4 frames consecutivos bajo el umbral de confianza | **falla** (contadores) | detecta divergencia de la máquina de estados |
| Un bbox corrido **1 px**, contadores idénticos | **falla** (`pattern_events.jsonl difiere`) | compara **contenido**, no solo contadores |
| Un solo frame bajo el umbral | **pasa** | correcto: `resolve_after_frames: 2` absorbe el dropout. Es la histéresis, no un gate ciego |

## 4. Corrida live end-to-end (criterio de terminado, spec 41 §11)

Servicio real (`EOVRT_MODEL_REF=mock`, `uvicorn` en :8099), fuente
`data/samples/videos/recorte-1.mp4`, `max_units: 40`, `bus.enabled: true`. Orden respetado:
`BusSource` construido y suscripto **antes** del `POST /api/runs`.

```
media_run_id        run_20260710_062654_dbe_mock_757a73   (== run_id devuelto por el POST)
experiment_id       exp-e2e-2026-07-10
source              bus
units_processed     40      == 40 lineas de detections.jsonl   (conservacion exacta)
units_failed        0
errors_count        0       (no hubo BusIdleTimeout: cerro por run_finished)
bus_dropped_events  0
degraded            False
pattern_events      15
alerts              6
pattern_evaluation  computed
status del media    succeeded
```

La corrida del control-plane **cerró sola** al llegar el `run_finished` (el hilo terminó sin
timeout). Las 6 alertas referencian unidades que existen en el `detections.jsonl` del
media-plane y llevan el `media_run_id` correcto: la cadena de reconstrucción (spec 40 §2)
funciona sobre datos reales.

**Re-evaluabilidad (ADR-003, mitigación 3):** el mismo run, releído offline desde su
`detections.jsonl`, produce **artefactos byte-idénticos** a la corrida live (15 `pattern_events`,
6 alertas, iguales módulo `control_run_id`/`alert_id`). Es la paridad live↔replay demostrada
sobre datos reales atravesando el servicio HTTP, no solo sobre un fixture.

Evidencia archivada en `datos/` (`runs/` es git-ignored en ambos planos):
`37-2026-07-10-live-e2e-{media,control,replay}-summary.json` y
`37-2026-07-10-live-e2e-control-alerts.jsonl`.

## 5. Decisiones de implementación que se apartan de la letra del spec

1. **XPUB en vez de PUB** (spec 42 §2 dice "ZeroMQ **PUB**"). Del lado del envío son
   equivalentes y el consumidor no nota la diferencia; XPUB además **notifica cuando un SUB se
   suscribe**, lo que permite implementar la regla 1 de spec 40 §3.2 ("el consumidor suscripto
   antes del disparo") de forma verificable (`wait_for_subscriber`) en vez de dormir a ciegas.
   No amerita ADR: es una elección de implementación dentro de la misma primitiva.
2. **`run_finished` se publica desde `execute_run`/`run_node_b`, no desde el `RunManager`.** Es
   donde vive el writer y donde termina el ciclo de vida del publicador. El status que emite
   (`succeeded`/`stopped`/`failed`) no distingue `stalled` como sí lo hace el `RunManager`; el
   consumidor solo necesita **una** señal terminal.
3. **El `key` del envelope de lifecycle es el `run_id`**, no un `source_id` (spec 40 §3.1 define
   `key = source_id`). El evento de lifecycle no tiene fuente; el consumidor nunca lee `key`.

## 6. Defectos encontrados y corregidos durante la implementación

El plan traía código de referencia con defectos reales, todos hallados por la revisión adversarial
por tarea y corregidos con test de regresión. Se registran porque son las trampas del dominio:

1. **`publish()` podía matar la corrida.** Sobre un publicador cerrado, `send_multipart` levanta
   `ZMQError` (ENOTSOCK), no `zmq.Again`; y `encode_envelope` corría fuera del `try`. Violaba
   "el bus nunca propaga una excepción al pipeline". → no-op seguro + cadena de `except`.
2. **`BusPublisher(...)` se construía fuera del `try`.** Un `bind()` fallido (EADDRINUSE, muy
   plausible) mataba el run, filtraba los descriptores del `RunArtifactWriter` y **nunca publicaba
   el `run_finished`** — el modo de falla exacto que esa garantía existe para cubrir. → degrada a
   corrida sin bus.
3. **`run_node_b` (camino EBE dockerizado) no tenía `try/finally` externo.** Un fallo temprano
   (`create_adapter`, `create_transport`) escapaba sin `run_finished` ni `close()`. Un comentario
   en el código *prometía* la garantía que no cumplía. → espeja a `execute_run`.
4. **`close()` era el único punto del bus sin protección**, invocado desde 4 sitios (uno de ellos
   antes del `try` externo); podía enmascarar la excepción real de la corrida. → `close()` nunca
   levanta, es idempotente.
5. **`_check_seq` retrocedía el contador ante un `seq` duplicado**, inflando `dropped_events` en el
   siguiente mensaje legítimo. Como el hueco de `seq` es la **única** señal de pérdida del sistema
   (un PUB/XPUB dropea en silencio al HWM — medido: 2000 envíos, 0 EAGAIN, 3 entregados), el
   mecanismo de detección de pérdidas daba números falsos. → solo avanza si `seq >= expected`.
6. **Cuatro caminos por los que un mensaje malformado mataba la corrida** en vez de salir como
   `ErrorEvent`: `envelope["topic"]` sin guarda, `json.loads` del lifecycle sin `try`,
   `recv_multipart` asumiendo 2 frames, `TypeError` no atrapado en la rama de detección.
   → verificado con un fuzz de 10 mensajes malformados: 10 `ErrorEvent`, cero excepciones.
7. **`_drain()` sin cota** podía no terminar nunca con un publicador rápido, anulando el cierre por
   polling (cuyo propósito es *garantizar* el cierre). → deadline + tope de items.
8. **La byte-compatibilidad no tenía ningún test que la sostuviera.** Se cumplía solo porque
   `bus_writer.py` y `jsonl_sink.py` contenían la misma expresión por casualidad; el test que decía
   verificarla recomputaba esa expresión y se comparaba consigo mismo. → test end-to-end contra el
   `detections.jsonl` real, verificado por mutación (mutando el sink, el test viejo pasa ciego y el
   nuevo falla).
9. **`SUBSCRIBE ""` en vez de los dos prefijos**: un implementador cambió código de producción para
   hacer pasar un test, culpando a `XPUB_VERBOSE`. Se probó falso — la causa era el helper de test,
   que drenaba una sola notificación de suscripción y dejaba una colgada (slow-joiner). Revertido.

## 7. Deuda que este plan NO absorbió

1. **Nadie produce `track_id`** (spec 42 §3). `granularity: subject` sigue viviendo solo en
   fixtures. Es el próximo bloqueante para G1 y para los overlays por persona.
2. **Purga del estado del motor** (`self._state` sin `subject_absent_timeout`). **CORRECCIÓN
   (medida el 2026-07-10):** una versión previa de este doc afirmaba que la purga "ahora importa
   de verdad porque una corrida live sobre RTSP es de duración indefinida". **Es falso.** Bajo
   `granularity: scene` la clave de estado es `(pattern_id, "pattern_id:source_id")`, así que el
   estado crece con la cantidad de **`source_id` distintos**, no con el tiempo. Medido: 5000
   frames de una fuente única ⇒ `len(_state) == 2` (una entrada por patrón activo). Y
   `RtspSource`/`VideoFileSource` emiten un `source_id` **constante** (derivado de la URL o del
   nombre de archivo), verificado en la corrida E2E de §4: 40 frames de video ⇒ 1 `source_id`.

   La fuga real existe pero en otros dos casos: (a) `source_id` por unidad — `ImageFolderSource`,
   donde cada imagen es su propia escena: 5000 imágenes ⇒ `len(_state) == 10000`; es una corrida
   finita, así que el estado muere con el proceso; (b) `granularity: subject` con `track_id`, que
   **nadie produce todavía**. Conclusión: **no bloquea el ítem 4 ni las corridas live**. Se vuelve
   necesario cuando aterrice el tracker (spec 42 §3), y ahí sí una corrida RTSP larga acumula un
   estado por track. Reagendado con esa deuda, no con el servicio mínimo.
3. **`experiment_id` no viaja en el `POST /api/runs` del media-plane** (spec 42 §4.1). El summary
   del control-plane lo tiene desde su config; el del media-plane, no. La cadena de reconstrucción
   queda a medias hasta el ítem 5.
4. **`BusSource` no expone `ts_receive_ms` por unidad** (spec 41 §8.3) — insumo de
   `t_capture→alert`, que se implementa en el ítem 5.
5. **El cierre por idle timeout no marca la corrida `degraded`.** Emite un `ErrorEvent`
   `BusIdleTimeout` (queda en `errors.jsonl` y en `errors_count`, no es silencioso), pero
   `degraded` queda en `False`. Decisión de producto pendiente: ¿una corrida que no cerró limpio
   es una corrida degradada?
6. **`run_live` no valida `input.type == "bus"` cuando se le inyecta la fuente.** La fuente
   inyectada es autoritativa por diseño (es lo que permite suscribirse antes del disparo), pero una
   config `media_jsonl` + fuente inyectada corre sin aviso.
7. **`wait_for_subscriber` del media-plane** ahora drena `expected` notificaciones (default 2, que
   es lo que emite un `BusSource` con sus dos prefijos). Si el consumidor cambia su cantidad de
   `SUBSCRIBE`, hay que actualizar ese default.

## 8. Cómo correr una corrida live

Levantar **primero** el consumidor (se suscribe al construirse), después disparar el run:

```bash
# Terminal 1 — media-plane
cd e-ovrt_media-plane && source .venv/bin/activate
EOVRT_MODEL_REF=grounding-dino/gdino-tiny uvicorn --factory eovrt_media.service.app:create_app

# Terminal 2 — control-plane (ANTES del POST)
cd e-ovrt_control-plane && source .venv/bin/activate
python -m eovrt_control.cli live configs/live_ebe_cr01_cr02.yaml

# Terminal 3 — disparo, con "bus": {"enabled": true, "endpoint": "tcp://127.0.0.1:5557"}
# en el body de POST /api/runs (ver §4 de este doc para el body completo)
```

Si el run ya está corriendo cuando arranca `live`, se pierden los eventos previos y el hueco
inicial de `seq` se cuenta como `bus_dropped_events` (la corrida se marca degradada, no se
silencia). Para despliegues donde no se puede garantizar el orden, el publicador acepta
`wait_for_subscriber_ms > 0` y espera al consumidor antes de emitir.
