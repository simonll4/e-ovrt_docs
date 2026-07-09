# Diseño: Módulo de distribución de alertas confirmadas

- **Fecha:** 2026-07-04
- **Estado:** Propuesta (pendiente de revisión)
- **Ámbito:** `e-ovrt_control-plane`
- **Referencia TFG:** §17.3.10 "Distribución de alertas confirmadas" (Tabla 52, tramo arquitectónico de distribución)

## 1. Contexto y motivación

Hoy el plano de control reconoce patrones de riesgo y, cuando un patrón alcanza el
estado `confirmed`, el `PatternEngine` emite un `AlertEvent`. El runtime de replay
recolecta esas alertas y las escribe append-only en `runs/<control_run_id>/alerts.jsonl`.
La vida de una alerta termina como una línea de JSONL: **no existe ninguna distribución
hacia canales externos**.

El TFG especifica (§17.3.10) un tramo de **distribución de alertas confirmadas** que
expone una alerta interna ya registrada hacia consumidores de inspección, reporte o
integración experimental (mensajería asistiva / Telegram, MQTT/IoT, webhook técnico e
interfaz/dashboard de inspección). Este documento diseña ese módulo.

### Estado actual relevante

- `contracts/alerts.py::AlertEvent` (`control.alert.v1`) — alerta interna confirmada.
- `engine/pattern_engine.py` — emite `AlertEvent` al confirmar patrón.
- `runtime/replay.py` — escribe `alerts.jsonl` vía `sinks/jsonl.py::JsonlSink`.
- `cli.py` — comandos `replay`, `validate-config`, `evaluate-alerts`.
- El plano de medios (`e-ovrt_media-plane`) ya usa **ZeroMQ (`pyzmq`) + `msgpack`** con
  una abstracción de transporte en `src/eovrt_media/transport/` (`base`, `factory`,
  `memory`, `network` REQ/REP, `rate_gate`, `serialization`). Este módulo reutiliza ese
  patrón, alineado y compatible en formato de wire.

## 2. Objetivos y no-objetivos

### Objetivos

1. Distribuir alertas **ya confirmadas** hacia canales externos habilitados por
   configuración de corrida: **MQTT**, **Telegram (mensajería asistiva)**, **webhook**
   y **dashboard de inspección (servidor web local en vivo)**.
2. Preservar la **frontera estricta**: primero se confirma el patrón, luego se
   distribuye. La distribución nunca recalcula severidad, muta estado de patrón ni crea
   alertas primarias.
3. Modelar la unidad distribuida como **evento derivado**, separando tres hechos:
   confirmación, intento de entrega, resultado de entrega.
4. Garantizar **idempotencia** ("una misma alerta no se notifica dos veces") mediante un
   ledger de entrega con clave `alert_id + channel`.
5. Garantizar **reintentos con backoff** y **dead-letter** para entregas fallidas, sin
   depender de un broker.
6. Registrar **observabilidad** propia del tramo (intento/resultado por canal) y la
   métrica **`talert-notification`**, medida por separado de la alerta interna.
7. **Una sola implementación para DBE y EBE**: el mismo `Distributor`, adaptadores y
   ledger operan en replay offline y en tiempo real; sólo cambia la fuente/transporte.
8. Introducir **primitivas de bus compartidas** (`transport/`) reutilizables por el bus
   `media → control` en el futuro, alineadas con el plano de medios.

### No-objetivos (fuera de alcance en esta iteración)

- Broker externo (Kafka/RabbitMQ) como capa de fiabilidad. Se documenta el seam para
  incorporarlo en EBE, pero no se construye. Ver §17.
- Acciones automáticas o normativas: ningún canal acciona sin supervisión humana.
- El bus `media → control` en sí (se comparten primitivas, no se implementa aquí).
- Autenticación/roles del dashboard, TLS de producción, alta disponibilidad.

## 3. Principios arquitectónicos

1. **Frontera estricta.** Los adaptadores consumen `AlertEvent`; nunca acceden al estado
   interno de evaluación de patrones (alineado con TFG §17.3.10.1 y contratos).
2. **El log persistido es la fuente de verdad.** `alerts.jsonl` (durable, replayable,
   inspeccionable) es el registro autoritativo. ZeroMQ es **transporte, no almacén**.
3. **ZeroMQ = capa de transporte en vivo**, no capa de fiabilidad. PUB/SUB puede
   descartar mensajes a suscriptores caídos o tardíos; por eso durabilidad, reintentos y
   dedup viven en la aplicación, no en el socket.
4. **Misma API para in-process y red.** `inproc://` / `ipc://` (DBE, tests) y `tcp://`
   (EBE) usan el mismo código de socket; DBE y EBE difieren en cadena de conexión, no en
   ruta de código.
5. **Backfill al conectar.** Todo consumidor en vivo (dashboard) rehidrata desde el log
   persistido al suscribirse, para no perder alertas publicadas antes de unirse.

## 4. Ubicación y layout de módulos

```
e-ovrt_control-plane/src/eovrt_control/
├── transport/                 # PRIMITIVAS DE BUS COMPARTIDAS (espeja eovrt_media/transport/)
│   ├── base.py                # BusPublisher / BusSubscriber (ABC) + END sentinel
│   ├── envelope.py            # sobre de mensaje versionado + msgpack (wire-compatible)
│   ├── serialization.py       # encode/decode msgpack
│   ├── memory.py              # adaptador in-process (inproc / cola en memoria)
│   ├── network.py             # adaptador ZeroMQ PUB/SUB (tcp/ipc/inproc)
│   └── factory.py             # construye transporte desde config
├── distribution/
│   ├── sources.py             # AlertStreamSource: Direct / JsonlReplay / Zmq
│   ├── ledger.py              # DeliveryLedger (idempotencia + registro de entrega)
│   ├── retry.py               # política de reintento con backoff + dead-letter
│   ├── distributor.py         # orquestación: source → ledger → adaptadores → registros
│   └── channels/
│       ├── base.py            # ChannelAdapter (ABC): build_payload + deliver
│       ├── mqtt.py            # publica a broker MQTT (paho-mqtt, opcional)
│       ├── telegram.py        # Bot API (HTTP, opcional)
│       └── webhook.py         # POST HTTP genérico (opcional)
├── dashboard/
│   └── server.py              # servidor web local (SUB en vivo + backfill del log)
├── contracts/
│   ├── notification.py        # NotificationEnvelope (alerta distribuida, contexto mínimo)
│   └── delivery.py            # DeliveryRecord (intento + resultado por canal)
└── cli.py                     # + comandos `distribute`, `dashboard`
```

**Decisión de ubicación de `transport/`:** vive dentro de `eovrt_control` (no en un
paquete compartido nuevo) porque los planos son repos git separados y un tercer paquete
sería prematuro. Se mantiene **plane-agnostic** (sin imports específicos de control) y
**wire-compatible** con `eovrt_media/transport/`, de modo que una extracción futura a
`eovrt-transport` sea mecánica. Se registrará en un ADR.

## 5. Primitivas de bus compartidas (`transport/`)

Espejan el patrón del plano de medios, con una diferencia clave: el bus `control → alertas`
requiere **fan-out** (distribuidor y dashboard consumen en paralelo), por lo que se añade
un adaptador **PUB/SUB** a la familia (el plano de medios usa REQ/REP para su pipeline
acoplado productor→consumidor).

- **`base.py`** — `BusPublisher.publish(topic, envelope)`, `BusSubscriber.subscribe(topics)`
  / `poll(timeout)` → `Envelope | END`, `close()`. Sentinela `END` como en el plano de
  medios.
- **`envelope.py`** — sobre versionado `{schema_version, topic, key, ts_publish_ms,
  payload}` serializado con msgpack. `key` porta la clave de idempotencia. Formato
  alineado con el plano de medios.
- **`memory.py`** — implementación in-process (cola) para DBE/tests: determinista, sin
  sockets.
- **`network.py`** — ZeroMQ PUB/SUB. Topics por prefijo (p.ej. severidad/condición). HWM
  configurable; el productor no bloquea la confirmación de patrones (la durabilidad la da
  el log, no el socket).
- **`factory.py`** — construye `memory` o `network` desde config (`type`, `endpoint`,
  `hwm`, `topics`).

## 6. Contratos de datos

### 6.1 `NotificationEnvelope` (`contracts/notification.py`)

Alerta distribuida = **evento derivado** de `AlertEvent` con **contexto mínimo** (TFG
§17.3.10.1): corrida, patrón, condición, severidad, instante de confirmación, estado del
episodio y referencias de evidencia cuando existan.

```python
class NotificationEnvelope(BaseModel):
    schema_version: str = "control.notification.v1"
    event_type: str = "notification_envelope"
    notification_id: str        # derivado determinista de alert_id (idempotencia)
    control_run_id: str
    media_run_id: str
    alert_id: str               # referencia a la alerta interna (no la reemplaza)
    pattern_id: str
    condition_id: str
    subject_key: str
    severity: str
    episode_state: str          # estado del episodio al momento de distribuir
    confirmed_at_ms: float | None
    evidence_ref: dict | None   # referencias mínimas, no evidencia completa
    summary_text: str           # texto humano breve (para mensajería)
```

`notification_id` es determinista: `sha1(alert_id)[:16]` (o similar), de modo que
reprocesar la misma alerta produce la misma clave y el ledger la deduplica.

### 6.2 `DeliveryRecord` (`contracts/delivery.py`)

Observabilidad del tramo (TFG §17.3.10.3): diferencia alerta confirmada, intento y
resultado, sin alterar la semántica del evento interno.

```python
class DeliveryRecord(BaseModel):
    schema_version: str = "control.delivery.v1"
    event_type: str = "delivery_record"
    control_run_id: str
    notification_id: str
    alert_id: str
    channel: str                # "mqtt" | "telegram" | "webhook"
    mode: str                   # "dry_run" | "live"
    attempt: int                # 1..N
    outcome: str                # "delivered" | "failed" | "skipped_duplicate" | "dead_letter"
    error: str | None
    talert_notification_ms: float | None  # confirmación → entrega efectiva
    attempted_at: str           # ISO-8601
    delivered_at: str | None
```

### 6.3 Métrica `talert-notification`

Latencia desde `confirmed_at_ms` (alerta interna) hasta la entrega efectiva por canal.
Se registra en cada `DeliveryRecord` y se agrega en el `RunSummary` de distribución
(min/mean/p95 por canal). Se mide **por separado** de la alerta interna: un fallo o demora
de distribución no altera la métrica principal de alerta.

## 7. `AlertStreamSource` (el seam DBE/EBE)

Interfaz que entrega `AlertEvent`s a distribuir. Tres implementaciones, mismo
`Distributor`:

- **`DirectSource`** — iterable en memoria (síncrono, sin sockets). Para **tests unitarios
  deterministas** y para acoplar el distribuidor al engine en un solo proceso.
- **`JsonlReplaySource`** — lee `alerts.jsonl` de una corrida. Camino **DBE** por defecto
  (post-run: `distribute` consume una corrida ya persistida).
- **`ZmqSource`** — suscribe al bus ZeroMQ (`transport/network.py`). Paridad **DBE↔EBE**:
  en DBE puede correr sobre `inproc`/`tcp://localhost`; en EBE sobre `tcp://` entre
  procesos. Al conectar hace **backfill** desde `alerts.jsonl` si se indica una corrida.

```python
class AlertStreamSource(ABC):
    @abstractmethod
    def __iter__(self) -> Iterator[AlertEvent]: ...
```

## 8. Ledger de idempotencia (`distribution/ledger.py`)

Garantiza "no notificar dos veces", incluso ante reintentos, re-ejecución del comando
`distribute`, o redelivery de un futuro broker.

- **Clave:** `(notification_id, channel)`.
- **Backing store:** append-only `runs/<run_id>/notifications.jsonl` (los `DeliveryRecord`
  con `outcome="delivered"` conforman el ledger). Al iniciar, el distribuidor carga las
  claves ya entregadas.
- **Comportamiento:** antes de despachar a un canal, si `(notification_id, channel)` ya
  tiene un `delivered`, se emite `DeliveryRecord(outcome="skipped_duplicate")` y no se
  envía. Re-correr `distribute` sobre la misma corrida es seguro e idempotente.
- Índice en memoria (`set`) para O(1); el archivo es la verdad persistida.

## 9. Reintentos y dead-letter (`distribution/retry.py`)

- Política configurable: `max_attempts`, `backoff_base_ms`, `backoff_factor`,
  `max_backoff_ms`. Backoff exponencial con tope.
- Cada intento genera un `DeliveryRecord`. Éxito → `delivered`. Fallo no terminal → espera
  y reintenta. Agotados los intentos → `DeliveryRecord(outcome="dead_letter")` y la
  notificación se escribe en `runs/<run_id>/dead_letter.jsonl`.
- El dead-letter es un archivo (equivalente app-level a una DLQ de RabbitMQ), reproducible
  y reprocesable con `distribute --retry-dead-letter`.

## 10. Adaptadores de canal (`distribution/channels/`)

Interfaz común, transporte-agnóstica:

```python
class ChannelAdapter(ABC):
    name: str
    @abstractmethod
    def build_payload(self, note: NotificationEnvelope) -> Any: ...
    @abstractmethod
    def deliver(self, payload: Any, *, mode: str) -> None:  # lanza en fallo
        ...
```

- **Modo `dry_run` (por defecto):** `build_payload` se ejecuta y el payload se registra
  en el `DeliveryRecord`; `deliver` **no hace I/O de red**. Reproducible, testeable, sin
  dependencias externas.
- **Modo `live`:** `deliver` ejecuta I/O real. Se activa sólo con configuración explícita
  (endpoint/credenciales presentes).

Adaptadores:

- **`mqtt.py`** — publica el payload (JSON) a un topic del broker MQTT. Dep opcional
  `paho-mqtt`. Import perezoso. No acciona nada; sólo publica para consumidores externos.
- **`telegram.py`** — mensajería asistiva: `sendMessage` vía Bot API (HTTP). Texto breve
  (`summary_text`). Dep: `httpx` (opcional) o `urllib` stdlib.
- **`webhook.py`** — POST HTTP genérico del `NotificationEnvelope` (JSON) a una URL
  configurada. Para validación/integración experimental.

Credenciales/endpoints se leen de config + variables de entorno; nunca se hardcodean ni
se persisten en artefactos.

## 11. Orquestación (`distribution/distributor.py`)

```
for alert in source:                       # AlertStreamSource
    note = NotificationEnvelope.from_alert(alert)
    for channel in enabled_channels:
        if ledger.already_delivered(note.notification_id, channel.name):
            record(skipped_duplicate); continue
        try:
            retry.run(lambda: channel.deliver(channel.build_payload(note), mode=mode))
            record(delivered, talert_notification_ms=now - alert.confirmed_at)
            ledger.mark(note.notification_id, channel.name)
        except PermanentFailure:
            record(dead_letter); dead_letter_sink.write(note)
```

- Despacho **concurrente opcional** por canal (`ThreadPoolExecutor`) para que
  `talert-notification` total ≈ `max(canales)` en vez de `sum(canales)`. Por defecto
  secuencial (determinista); concurrencia habilitable por config.
- Al terminar, escribe `distribution_summary.json` (conteos por canal, outcomes,
  agregados de `talert-notification`).

## 12. Dashboard de inspección (`dashboard/server.py`)

Servidor web local **en vivo**, modelado como *consumidor* (no como adaptador push):
"proyección posterior basada en eventos persistidos" (TFG), pero con actualización en
vivo.

- **Fuente doble:** al arrancar, **backfill** leyendo `alerts.jsonl` +
  `notifications.jsonl` de la corrida; luego **suscribe** al bus ZeroMQ (`ZmqSource`) para
  updates en vivo (o hace *tail* del log si el bus no está habilitado).
- **Transporte al navegador:** `http.server` de stdlib + endpoint **SSE** (`text/event-stream`).
  Cero dependencias nuevas obligatorias. (Alternativa evaluada: FastAPI/uvicorn como extra
  `[dashboard]`; se descarta por peso salvo que se pida.)
- **Vista:** tabla de alertas confirmadas con severidad/condición/patrón/instante y el
  outcome de entrega por canal (delivered/failed/dead-letter). Sólo lectura; no acciona
  ni reevalúa nada.
- Comando: `eovrt-control dashboard --run runs/<id> [--port 8080] [--bus <endpoint>]`.

## 13. Configuración (`config.py`)

Nueva sección opcional; ausente ⇒ distribución deshabilitada (comportamiento actual
intacto).

```yaml
distribution:
  enabled: true
  concurrency: false          # despacho concurrente por canal
  bus:                        # opcional; si ausente, source = jsonl replay
    type: memory | zmq
    endpoint: "tcp://127.0.0.1:5556"
    hwm: 1000
  retry:
    max_attempts: 3
    backoff_base_ms: 200
    backoff_factor: 2.0
    max_backoff_ms: 5000
  channels:
    telegram:
      enabled: true
      mode: dry_run           # dry_run | live
      bot_token_env: TELEGRAM_BOT_TOKEN
      chat_id: "..."
    mqtt:
      enabled: true
      mode: dry_run
      host: "localhost"
      port: 1883
      topic: "eovrt/alerts"
    webhook:
      enabled: false
      mode: dry_run
      url: "https://..."
```

Modelos Pydantic: `DistributionSection`, `BusConfig`, `RetryConfig`, `ChannelConfig`.
`OutputsSection` gana toggles `save_notifications_jsonl`, `save_dead_letter_jsonl`,
`save_distribution_summary_json`.

## 14. Interfaz CLI (`cli.py`)

- **`distribute`** — distribuye alertas de una corrida ya persistida (camino DBE
  post-run):
  ```
  eovrt-control distribute --run runs/<id> --config <run.yaml> \
      [--retry-dead-letter] [--dry-run/--live]
  ```
  Lee `alerts.jsonl` (o suscribe al bus si `distribution.bus` está configurado), despacha,
  escribe `notifications.jsonl`, `dead_letter.jsonl`, `distribution_summary.json`.
- **`dashboard`** — levanta el servidor web local (§12).
- `replay` permanece intacto. (Opción futura: flag `replay --distribute` para publicar al
  bus in-process en EBE; no requerido ahora.)

## 15. Observabilidad y métricas

- `notifications.jsonl` — todos los `DeliveryRecord` (intento/resultado/skip/dead-letter).
- `dead_letter.jsonl` — notificaciones agotadas para reproceso.
- `distribution_summary.json` — por canal: intentos, delivered, failed, duplicates,
  dead-letter; agregados de `talert-notification` (min/mean/p95).
- El `evaluate-alerts` existente no cambia: mide la alerta interna. La distribución se mide
  aparte, como exige el TFG.

## 16. Estrategia de pruebas

- **Unitarias (deterministas, sin red):**
  - `NotificationEnvelope.from_alert` (contexto mínimo, `notification_id` determinista).
  - Ledger: dedup de `(notification_id, channel)`; re-run idempotente.
  - Retry: backoff, transición a dead-letter tras `max_attempts`.
  - Adaptadores en `dry_run`: `build_payload` correcto, `deliver` sin I/O.
  - `DirectSource` + `Distributor` end-to-end con canal *fake* (registra llamadas).
- **Transporte:** `memory` bus (in-process) publish/subscribe + END; envelope msgpack
  round-trip.
- **Integración ZeroMQ:** `ZmqSource` sobre `inproc`/`tcp://localhost` publica→suscribe
  (marcado, tolerante a timing; fuera del set determinista).
- **Dashboard:** arranque, backfill desde artefactos, endpoint SSE responde; smoke test.
- **Live channels:** no en CI; scripts manuales con broker/bot reales. `dry_run` cubre CI.
- `ruff` + `pytest` como en el resto del repo.

## 17. Paridad DBE/EBE y evolución a broker

- **DBE:** `distribute` post-run con `JsonlReplaySource` (o bus `memory`/`inproc`). 100%
  reproducible.
- **EBE:** el plano de control publica cada `AlertEvent` confirmado al bus ZeroMQ; el
  mismo `Distributor` lo consume vía `ZmqSource` en otro proceso. Cambia la cadena de
  conexión, no el código.
- **Broker futuro (Kafka/RabbitMQ):** si EBE lo requiere, se añade una implementación
  `BrokerSource` a `AlertStreamSource` y/o un `BusPublisher`/`BusSubscriber` de broker en
  `transport/`. **Cero cambios en adaptadores, ledger o distribuidor.** El broker aporta
  transporte y colas; durabilidad/dedup/reintentos siguen en la app (un broker at-least-once
  puede *duplicar* entregas, por eso el ledger es imprescindible independientemente del
  transporte).

## 18. Dependencias

- **Núcleo:** `pyzmq`, `msgpack` (ya usados por el plano de medios; se agregan a
  `dependencies` del control plane).
- **Extras opcionales** en `pyproject.toml`: `[mqtt]` → `paho-mqtt`; `[http]` → `httpx`
  (Telegram/webhook; fallback stdlib `urllib`). Dashboard usa stdlib.
- Imports perezosos: sin el extra, el canal correspondiente sólo funciona en `dry_run` o
  informa dependencia faltante; el núcleo permanece liviano.

## 19. Decisiones y ADRs a registrar

- ADR: **ZeroMQ como transporte del bus** (brokerless; misma API in-process/red; paridad
  DBE/EBE; alineado con el plano de medios). Broker diferido a EBE.
- ADR: **Log persistido como fuente de verdad**; ZeroMQ transporta, no almacena.
- ADR: **`transport/` mirror del plano de medios**, wire-compatible, extraíble a paquete
  compartido a futuro.

## 20. Preguntas abiertas

1. ¿`summary_text` de la notificación se plantilla por config (idioma/campos) o se fija en
   código por ahora?
2. ¿El dashboard debe listar varias corridas o sólo la corrida indicada? (Propuesta: una
   corrida en esta iteración.)
3. ¿`talert-notification` en DBE debe medirse contra tiempo de wall-clock del `distribute`
   o marcarse como N/A (no hay tiempo real)? (Propuesta: registrar wall-clock del despacho
   y etiquetar el escenario como DBE para no confundir con latencia real EBE.)
