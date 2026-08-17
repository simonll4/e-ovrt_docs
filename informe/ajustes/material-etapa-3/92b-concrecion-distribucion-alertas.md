# 92b — Concreción técnica: módulo de distribución de alertas

- **Fecha:** 2026-08-10
- **Qué es esto:** la descripción completa del **módulo de distribución de alertas**
  (`e-ovrt_alert-distribution`) a nivel de concreción técnica — frontera, arquitectura,
  contratos serializados, política, configuración, salidas e integración. Es el material
  del que se escribe **§17.3.10** del informe, en el mismo registro que el `informe/92`
  (contratos y rutas, no cifras).
- **Estado de implementación:** ✎ **2026-08-12 — funcionalmente implementado y
  verificado.** El pipeline completo existe en `e-ovrt_alert-distribution` y cerró los
  seis criterios de spec 45: replay DBE idempotente, consumo EBE desde el publisher real,
  cooldown, deduplicación, MQTT QoS 1 contra broker real e integración en `report.json`.
  Evidencia y salvedades: `operacion/114`. ✎ **2026-08-14:** la vista de outcomes en la
  webconsole, la orquestación integral y el versionado del repo —que este encabezado daba
  por pendientes— se cerraron el 2026-08-13 (`13c801e`, `42529e2`; repo con `c9903cc` y
  `1e6d8fa`). **E-06 sigue excluida.** Las latencias de smoke/loopback no se citan como resultado de desempeño.
  *Decía “diseñado y especificado; implementación pendiente” y luego “trabajo
  comprometido” por ADR-016.*
- **Normativa que lo gobierna** (todos de la **serie del proyecto**, `ADR-001…018` —
  no confundir con la serie interna del control-plane, `ADR-0001…0013` de 4 dígitos):
  **ADR-016** (reapertura acotada: el estatuto vigente del módulo), ADR-005 (recorte,
  canal MQTT, repo propio), ADR-011 (frontera de la política: el motor
  emite siempre, la supresión es de distribución), ADR-004 (`experiment_id`),
  ADR-006/013 (aplicabilidad y relojes), ADR-007 (semántica 1:1), spec 45 (spec
  recortada), `nucleo/06` (anexo de diseño completo, E-06) y **`nucleo/19`** (el cierre
  arquitectónico del ciclo de vida de la alerta, que consolida todo lo anterior).
- **Redlines que alimenta:** **R-02** — su "DEBE DECIR" pide exactamente el párrafo de
  §17.3.10.3 sobre dónde vive la política de notificación y por qué las re-alertas no
  son falsos positivos (desarrollado en §5 de este doc) — y **R-13**, que lista la
  distribución entre los límites que sobreviven y hay que declarar.

---

## 1. Qué es, y sobre todo qué no es

Consumidor **desacoplado** de alertas **ya confirmadas** por el control-plane. Las
recibe (del bus en vivo o de `alerts.jsonl` en diferido), decide **cuáles se convierten
en notificación**, las entrega por **MQTT** y registra el intento y su resultado.

**La frontera es estricta y es la razón de ser del módulo** (§17.3.10.1, DA-13): el
distribuidor **nunca** recalcula severidad, **nunca** muta el estado de un patrón y
**nunca** crea alertas. Solo consume, decide notificación y registra. Que viva en un
**repo hermano propio** —y no dentro del control-plane— materializa esa frontera en la
estructura misma del sistema (ADR-005, que supera la ubicación propuesta en `nucleo/06`
§4).

La cadena conceptual completa, y cada eslabón con su dueño:

| Eslabón | Qué decide | Dónde vive |
|---|---|---|
| **Detección** | qué hay en el frame | media-plane |
| **Patrón** | si la condición se sostiene en el tiempo | control-plane (motor) |
| **Alerta** | que el patrón se confirmó | control-plane (`control.alert.v1`) |
| **Notificación** | si a esta alerta hay que avisarle a alguien, y por dónde | **este módulo** |

El **recorte** respecto del diseño completo del `nucleo/06` (lo excluido queda como
E-06, anexo): **un solo canal** (MQTT; sin Telegram ni webhook), **sin dashboard propio**
(la webconsole muestra los resultados), **retry mínimo** (N intentos fijos, sin backoff
exponencial) y **dead-letter simple** (archivo de agotadas, sin comando de reproceso).

---

## 2. Arquitectura: un pipeline de cinco etapas

```
                    ┌───────────── e-ovrt_alert-distribution ─────────────┐
                    │                                                     │
  control-plane     │  ┌────────┐   ┌────────┐   ┌────────┐   ┌────────┐  │
  ───────────────►  │  │ SOURCE │──►│ POLICY │──►│ LEDGER │──►│ CHANNEL│──┼──► MQTT
   control.alert.v1 │  └────────┘   └────────┘   └────────┘   └────────┘  │    (broker)
   ó alerts.jsonl   │      │            │            │            │       │
                    │      │            │            │            │       │
                    │      └────────────┴────────────┴────────────┘       │
                    │                        │                            │
                    │                   DeliveryRecord                    │
                    │       notifications.jsonl · dead_letter.jsonl       │
                    │              distribution_summary.json              │
                    └─────────────────────────────────────────────────────┘
```

Una alerta atraviesa las etapas **en este orden**, y sale del pipeline en la primera que
la resuelva. Cada salida produce un `DeliveryRecord` — **ninguna alerta desaparece en
silencio**, que es la propiedad de observabilidad que el módulo garantiza:

1. **Source** — entrega la alerta cruda, venga del archivo o del bus.
2. **Policy** — cooldown de notificación (ADR-011). Si suprime → `suppressed_cooldown`.
3. **Ledger** — idempotencia. Si ya se entregó → `skipped_duplicate`.
4. **Channel** — entrega con reintentos. Éxito → `delivered`; cada intento fallido →
   `failed`; agotados → `dead_letter`.
5. **Records** — todo lo anterior se escribe append-only y se agrega en el summary.

**Policy y Ledger son capas distintas y las dos hacen falta** — es la distinción que más
se confunde al leer el módulo: el **ledger deduplica exactos** (la *misma* alerta
reprocesada, p. ej. porque MQTT QoS 1 reentregó o porque se re-corrió el replay); el
**cooldown suprime semánticos** (alertas *distintas*, de la misma condición y cámara,
demasiado seguidas).

---

## 3. Contratos serializados

### 3.1 Entrada: `control.alert.v1` (del control-plane)

El módulo no define este contrato, lo consume. Campos que usa:

| Campo | Uso en distribución |
|---|---|
| `alert_id` | identidad; deriva el `notification_id` |
| `control_run_id`, `media_run_id` | trazabilidad de corrida |
| `pattern_id`, `condition_id` | qué se confirmó |
| `source_id` | qué cámara — **parte de la clave de cooldown** |
| `subject_key` | qué sujeto (bajo G1 incluye `track_id`) |
| `severity` | enruta el topic MQTT |
| `state` | estado del episodio al distribuir |
| `timestamp_ms` | tiempo **de media** — base temporal del cooldown |
| `evidence` | referencias mínimas, se propagan sin interpretarse |
| `experiment_id` | ADR-004; viaja hasta el reporte |

> **Precisión sobre `nucleo/06` §6.1:** aquel diseño preveía un `confirmed_at_ms` en el
> envelope. El `AlertEvent` real **no tiene ese campo**: el tiempo de media es
> `timestamp_ms`, y el instante de pared solo existe en vivo, donde lo aporta el
> `ts_publish_ms` del envelope del bus. El contrato de abajo refleja el evento real.

### 3.2 `NotificationEnvelope` — `control.notification.v1`

Evento **derivado** con contexto mínimo (§17.3.10.1): no reemplaza a la alerta interna,
la referencia.

```python
class NotificationEnvelope(BaseModel):
    schema_version: str = "control.notification.v1"
    event_type: str = "notification_envelope"
    notification_id: str            # sha1(alert_id)[:16] — determinista
    control_run_id: str
    media_run_id: str
    alert_id: str                   # referencia, no reemplazo
    pattern_id: str
    condition_id: str
    source_id: str
    subject_key: str
    severity: str
    episode_state: str
    media_timestamp_ms: float | None = None   # tiempo de media
    confirmed_wall_ms: float | None = None    # ts_publish_ms del bus; None en replay
    evidence_ref: dict | None = None
    summary_text: str               # texto humano breve, para mensajería
    experiment_id: str | None = None
```

**`notification_id` determinista** (`sha1(alert_id)[:16]`) es lo que vuelve la
idempotencia una propiedad *por construcción* y no un cuidado del operador: reprocesar
la misma alerta produce siempre la misma clave, así que el ledger la reconoce.

### 3.3 `DeliveryRecord` — `control.delivery.v1`

Observabilidad del tramo (§17.3.10.3): separa **alerta confirmada**, **intento** y
**resultado**, sin tocar la semántica del evento interno.

```python
Outcome = Literal["delivered", "failed", "skipped_duplicate",
                  "dead_letter", "suppressed_cooldown"]

class DeliveryRecord(BaseModel):
    schema_version: str = "control.delivery.v1"
    event_type: str = "delivery_record"
    control_run_id: str
    notification_id: str
    alert_id: str
    channel: str                    # "mqtt" en esta iteración
    mode: Literal["dry_run", "live"]
    attempt: int                    # 0 para supresiones/duplicados; 1..N para envíos
    outcome: Outcome
    error: str | None = None
    talert_notification_ms: float | None = None
    latency_mode: Literal["live", "wall_clock_dbe"] | None = None
    attempted_at: str               # ISO-8601 UTC
    delivered_at: str | None = None
    experiment_id: str | None = None
```

Los cinco `outcome` y qué significa cada uno:

| Outcome | Significa | ¿Es un error? |
|---|---|---|
| `delivered` | entregada y confirmada por el broker | no |
| `suppressed_cooldown` | la condición en esa cámara ya se avisó dentro de la ventana | **no** — es la política funcionando |
| `skipped_duplicate` | esa alerta exacta ya se había entregado | **no** — es la idempotencia funcionando |
| `failed` | un intento falló; quedan reintentos | parcial |
| `dead_letter` | se agotaron los intentos | sí |

---

## 4. Fuentes: el mismo distribuidor para DBE y EBE

| Fuente | Camino | Uso |
|---|---|---|
| `JsonlReplaySource` | **DBE** | relee `runs/<id>/alerts.jsonl` de una corrida del control-plane. Post-run, idempotente, re-ejecutable |
| `ZmqSource` | **EBE** | suscripta a `control.alert.v1.*` en el bus, **con backfill** desde `alerts.jsonl` al conectar |
| `DirectSource` | tests | iterable en memoria, sin sockets |

Las tres entregan `SourcedAlert(alert: dict, ts_publish_ms: float | None)` y alimentan
**el mismo `Distributor`**: el camino de distribución es idéntico en los dos escenarios,
y lo único que cambia es de dónde llegan las alertas. Es la misma propiedad de paridad
DBE↔EBE que sostiene el resto de la plataforma.

**El backfill no es un detalle de implementación, es la corrección de un defecto
estructural del bus**: PUB/SUB pierde todo lo publicado antes de que el consumidor se
suscriba. Como el JSONL del control-plane es la verdad, `ZmqSource` lo lee al conectar y
deduplica por `alert_id` contra lo que después llegue por el stream — de modo que una
alerta emitida antes de la suscripción se notifica igual.

Reglas del bus que el módulo respeta (spec 40 §3.2):

- Envelope `bus.envelope.v1`, dos frames: `[topic-utf8, msgpack{...}]`, con el
  `AlertEvent` serializado como `payload`.
- Suscripción a los prefijos `control.alert.v1.` y `run.lifecycle.v1.`; el
  `run_finished` del lifecycle **cierra la corrida de distribución** (semántica 1:1,
  ADR-007).
- **Los huecos de `seq` se cuentan** (`bus_dropped_events`) y degradan la corrida;
  nunca se silencian.
- **Parada cooperativa**, no cierre desde otro hilo: `request_stop()` levanta un flag y
  el socket se cierra en el mismo hilo que hace `recv` — cerrarlo desde afuera con un
  `recv` en curso aborta el proceso con `SIGABRT` (trampa de libzmq, no negociable en
  todo el workspace).

---

## 5. Política de notificación: dónde vive el cooldown, y por qué

**ADR-011 es la decisión que da forma a este módulo.** El control-plane emite un
`AlertEvent` **cada vez** que un patrón se confirma, sin supresión: `alerts.jsonl` es el
registro fiel de la dinámica del patrón. Quién decide cuántas veces molestar a un
consumidor es el distribuidor.

```yaml
notification_policy:
  cooldown_ms: 30000                 # ventana de supresión
  key: [condition_id, source_id]     # sobre qué se suprime
```

La clave es `(condition_id, source_id)` —no el sujeto— porque para notificación
asistiva lo relevante es *"esta condición en esta cámara ya fue avisada"*. Una ráfaga de
tres personas sin casco en la misma cámara en diez segundos es **un aviso**, no tres.
La base temporal es `media_timestamp_ms` (coherente entre replay y vivo), con fallback a
reloj de pared si la alerta no trae tiempo de media.

Esta ubicación tiene tres consecuencias que el informe declara:

1. **Frontera limpia:** detección ≠ patrón ≠ alerta ≠ notificación.
2. **Métricas más honestas:** con la supresión en el motor, la tasa de re-alertas
   —que es señal de estabilidad perceptual— quedaba oculta. Emitiendo siempre, esa señal
   se mide; suprimirla es decisión del consumidor. Es también la razón por la que
   **`re_alerts` no se cuentan como falsos positivos** en la evaluación.
3. **Corrige dos defectos** detectados al revisar el cooldown del motor: quedaba inerte
   frente a las ventanas del informe (ciclo de re-alerta 6–10 s > cooldown de 5 s), y
   bajo granularidad de escena cambiaba de significado por accidente de la clave de
   estado (*"mismo trabajador"* pasaba a *"misma cámara"*). Acá la ventana se define
   explícitamente sobre `(condición, fuente)`, que es lo correcto.

Toda supresión **queda registrada** (`suppressed_cooldown`) y contada en el summary: la
política es auditable, no invisible.

---

## 6. Ledger de idempotencia

Clave `(notification_id, channel)`. El respaldo es el propio `notifications.jsonl`
append-only: al construirse, el ledger se rehidrata leyendo los registros `delivered`
previos. **Solo `delivered` marca como visto** — un `failed` o un `suppressed_cooldown`
no bloquean un intento posterior.

[Enmienda 2026-08-14] Al reabrir un directorio ya usado, la generación anterior se
conserva íntegra como `notifications.<n>.jsonl` (y `dead_letter.<n>.jsonl`): el archivo
vigente corresponde a la ejecución en curso y ninguna fila se pierde.

Esto da dos garantías operativas:

- **Re-ejecutar el replay es seguro:** la segunda corrida sobre la misma entrada produce
  `skipped_duplicate` en el 100% de los casos, sin re-entregar nada.
- **MQTT QoS 1 puede duplicar** (garantiza *al menos una* entrega): el ledger no es
  opcional, es la contraparte obligatoria de haber elegido QoS 1.

---

## 7. Canal MQTT

Único canal de esta iteración (ADR-005). Elegido por tres razones defendibles: peso
mínimo (Mosquitto en el compose de la plataforma), es **estándar de integración IoT**, y
permite medir `t_alert-notification` limpio, sin la variabilidad de una API externa
ajena al sistema.

| Aspecto | Definición |
|---|---|
| Topic | `eovrt/alerts/<severity>` |
| Payload | el `NotificationEnvelope` serializado a JSON |
| QoS | **1** (al menos una entrega) ⇒ el ledger deduplica |
| Modo `dry_run` | **default**: construye el payload y lo registra **sin I/O** — la CI cubre el pipeline entero sin broker |
| Modo `live` | `paho-mqtt` (extra opcional `[mqtt]`), conexión lazy, `publish` + espera de PUBACK |
| Credenciales | **solo por entorno** (`EOVRT_MQTT_USERNAME` / `EOVRT_MQTT_PASSWORD`) — jamás en configs versionadas ni en artefactos |

Que `dry_run` sea el default no es comodidad: es lo que permite que el módulo completo
sea testeable y reproducible sin infraestructura, igual que el resto de la plataforma.

**Retry:** `max_attempts: 3` con espera fija (`wait_ms: 500`). Agotados los intentos, la
notificación va a `dead_letter.jsonl` con `outcome: dead_letter`. Sin backoff
exponencial ni reproceso automático — eso queda en E-06.

---

## 8. Salidas por corrida, y la métrica

```
runs/<experiment_id>/distribution/
├── notifications.jsonl        # un DeliveryRecord por evento (append-only); generaciones previas como notifications.<n>.jsonl
├── dead_letter.jsonl          # solo las agotadas; generaciones previas como dead_letter.<n>.jsonl
└── distribution_summary.json  # agregado de la corrida
```

> Ejemplo ILUSTRATIVO con valores ficticios: no constituye una medición. La cifra real
> vive en `results/realtime/t_alert_notification/metrics.json` y en el doc 118
> (p95 = 64,534 ms).

```json
{
  "schema_version": "control.distribution_summary.v1",
  "channel": "mqtt",
  "mode": "live",
  "counts": {"delivered": 3, "suppressed_cooldown": 2},
  "skipped_invalid_alerts": 0,
  "source_stats": {"...": "..."},
  "talert_notification_ms": {
    "live": {"count": 3, "min": 31.2, "mean": 41.0, "p95": 58.7}
  }
}
```

### `t_alert-notification`: la métrica del tramo, y su caveat

Latencia desde la confirmación de la alerta hasta la entrega efectiva por el canal. Se
registra por notificación y se agrega (min / mean / p95). **Se mide por separado de la
alerta interna**: una demora o un fallo de distribución no contamina la métrica
principal de alerta.

**El caveat va declarado siempre, porque la métrica no significa lo mismo en los dos
caminos** (política de spec 40 §5):

| `latency_mode` | Cómo se calcula | Qué mide de verdad |
|---|---|---|
| `live` | `puback_wall_ms − ts_publish_ms` | latencia real del tramo de distribución |
| `wall_clock_dbe` | duración del envío en replay | **reloj de pared de un reproceso**, no el tiempo del episodio |

Reportar un `wall_clock_dbe` como si fuera latencia operativa sería un error de la misma
familia que el ya declarado para G2A (que se mide desde el *dequeue*, no desde el
fotón): el número existe, pero no dice lo que parece decir.

---

## 9. Configuración y operación

```yaml
# configs/example.yaml — sin credenciales: van por entorno
notification_policy:
  cooldown_ms: 30000
  key: [condition_id, source_id]
channel:
  mode: dry_run          # live requiere el extra [mqtt] y un broker Mosquitto
  host: 127.0.0.1
  port: 1883
  topic_prefix: eovrt/alerts
  qos: 1
retry:
  max_attempts: 3
  wait_ms: 500
```

```bash
# DBE — sobre una corrida ya persistida del control-plane
eovrt-distribute replay --alerts <control-run>/alerts.jsonl --out-dir runs/d1

# EBE — consumiendo el bus, con backfill de lo publicado antes de suscribirse
eovrt-distribute live --endpoint tcp://127.0.0.1:5558 \
                      --backfill <control-run>/alerts.jsonl --out-dir runs/d2
```

En EBE rige el **mismo orden no negociable** que el resto de la plataforma: el
consumidor se suscribe **antes** de que se dispare la corrida; el backfill cubre lo que
aun así se haya perdido.

---

## 10. Integración con el resto de la plataforma

| Con | Interfaz |
|---|---|
| **control-plane** (spec 41) | consume su publisher `control.alert.v1.*` y su `alerts.jsonl`. **No toca el motor**: el control-plane no conoce canales ni ledger |
| **experimental-setup** (spec 44) | el broker Mosquitto va en el compose; el generador de reporte incorpora `distribution_summary.json` al `report.json` de la corrida |
| **webconsole** | muestra los `outcome` de entrega en la vista de alertas — **no hay dashboard propio** (recorte de ADR-005) |
| **`experiment_id`** (ADR-004) | viaja desde el `AlertEvent` hasta el `DeliveryRecord` y el summary, de modo que la distribución queda atada a la corrida paraguas |

Para la **demostración de defensa**: `mosquitto_sub` suscrito en vivo mostrando las
notificaciones llegar, más la vista de la webconsole. Sin canal externo, justamente para
no exhibir la latencia de una API de terceros como si fuera del sistema.

---

## 11. Criterios de terminado

Lo que hay que poder mostrar para dar el módulo por cerrado (spec 45 §7):

- [x] `replay` sobre una corrida real y re-ejecución idempotente — ver `operacion/114`
      y regresiones `test_cli.py`/`test_ledger.py`.
- [x] Modo `live` con backfill de alertas previas — ver `operacion/114` y
      `test_zmq_source.py`.
- [x] Entrega MQTT real y p95 en summary — campaña doc 118: **64,534 ms (n = 460)**,
      testigo MQTT 100 %.
- [x] Duplicado QoS 1 deduplicado — `notification_id = sha1(alert_id)[:16]` y
      regresiones de `test_ledger.py`.
- [x] Ráfaga condición-fuente suprimida — clave `(condition_id, source_id)` y **376
      `suppressed_cooldown`** en la campaña del doc 118.
- [x] `experiment_id` presente en envelope, records y `report.json` — ver
      `operacion/114` y tests de consolidación/reporte del backend.

---

## 12. Qué queda fuera, y con qué causa

Excluido en **E-06** (`nucleo/10`), diseñado en `nucleo/06` como anexo: canales
adicionales (Telegram, webhook), dashboard dedicado, backoff exponencial y reproceso de
la dead-letter. La incorporación futura de cualquiera de ellos **no altera la semántica
de la alerta** (DA-13) — entra como un canal más detrás de la misma interfaz, que es
precisamente lo que la frontera del §1 protege.
