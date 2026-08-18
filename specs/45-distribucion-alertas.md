# Spec 45 — Distribución de alertas (repo nuevo)

- **Fecha:** 2026-07-09
- **Estado:** Escrito
- **Repo dueño:** **`e-ovrt_alert-distribution`** (repo hermano NUEVO — local, sin
  remote GitHub, regla del workspace). Se crea con este spec.
- **Decisiones que implementa:** ADR-005 (recorte + MQTT + repo propio), ADR-004
  (`experiment_id`), ADR-006 (métrica separada). Normativa: spec 40 (envelope,
  `t_alert-notification`). **El doc 06 es el anexo de diseño completo** (E-06):
  este spec es su versión recortada y re-ubicada; donde no contradice, el doc 06
  detalla.

## 1. Qué es (y qué no)

Consumidor desacoplado de alertas **ya confirmadas**: las recibe del bus
`control.alert.v1.*` (o de `alerts.jsonl` en modo replay), las envuelve, las
entrega por **MQTT** y registra intento/resultado. **Nunca** recalcula severidad,
muta estado de patrón ni crea alertas (frontera estricta §17.3.10.1 — que el repo
separado materializa en la estructura misma).

**Recorte vs doc 06 (E-06):** un solo canal (MQTT); sin Telegram/webhook; sin
dashboard propio (la webconsole muestra outcomes — spec 44 §8); retry mínimo
(N intentos + registro, sin backoff sofisticado); **dead-letter simple** (archivo
de agotadas, sin comando de reproceso en esta iteración).

## 2. Estructura del repo

```
e-ovrt_alert-distribution/
├── pyproject.toml                # paquete eovrt_distribution; extra [mqtt] → paho-mqtt
├── src/eovrt_distribution/
│   ├── transport/                # PUB/SUB ZeroMQ + envelope — wire-compatible con
│   │                             #   los planos (nace acá; extracción futura mecánica)
│   ├── contracts/
│   │   ├── notification.py       # NotificationEnvelope (control.notification.v1)
│   │   └── delivery.py           # DeliveryRecord (control.delivery.v1)
│   ├── sources.py                # AlertStreamSource: JsonlReplay | Zmq (backfill)
│   ├── ledger.py                 # idempotencia (notification_id, channel)
│   ├── channels/mqtt.py          # único canal; dry_run | live
│   ├── distributor.py            # source → ledger → canal → registros
│   └── cli.py                    # eovrt-distribute (replay y live)
├── configs/
└── tests/
```

## 3. Contratos (según doc 06 §6, con dos ajustes)

- `NotificationEnvelope`: como doc 06 §6.1 **más `experiment_id`** (spec 40 §2).
  `notification_id` determinista desde `alert_id` (idempotencia por construcción).
- `DeliveryRecord`: como doc 06 §6.2 **más `experiment_id`**; `channel` fijo
  `"mqtt"` en esta iteración; `talert_notification_ms` medido desde
  `confirmed_at_ms` hasta el PUBACK — en modo replay-DBE se etiqueta
  `wall_clock_dbe` (política del spec 40 §5, fila t_alert-notification).

## 4. Fuentes y modos

| Modo | Fuente | Uso |
|---|---|---|
| `replay` | `JsonlReplaySource` sobre `runs/<id>/alerts.jsonl` del control-plane | DBE, post-run; idempotente re-ejecutable |
| `live` | `ZmqSource` suscripta a `control.alert.v1.*` (publisher del spec 41 §8.6), con **backfill** desde `alerts.jsonl` al conectar | EBE; mismo distribuidor |

Reglas del bus: las de spec 40 §3.2 aplican (suscripción antes del run — el
runner/spec 44 ordena; huecos de `seq` → registrados; el log es la verdad, por
eso el backfill).

## 5. Canal MQTT

- `paho-mqtt` (extra opcional; sin él, solo `dry_run`). Publica el
  `NotificationEnvelope` (JSON) a topic `eovrt/alerts/<severity>`; QoS 1 —
  **el ledger es obligatorio** porque QoS 1 puede duplicar (doc 07 D5.2).
- `dry_run` (default): construye payload y lo registra sin I/O — CI cubierta.
  `live`: broker Mosquitto (compose de la plataforma en experimental-setup).
- Credenciales/host por env/config; jamás en artefactos.
- Demo de defensa: `mosquitto_sub` en vivo + vista de la webconsole (doc 07 D5.3).

## 6. Política de notificación, ledger, retry y observabilidad

- **Política de notificación (ADR-011 — el cooldown vive ACÁ, no en el motor):**
  el control-plane emite un `AlertEvent` por cada confirmación del patrón; el
  distribuidor decide cuáles se convierten en notificación. Config:

  ```yaml
  notification_policy:
    cooldown_ms: 30000        # no re-notificar la misma clave dentro de la ventana
    key: [condition_id, source_id]   # clave de supresión (default; puede sumar subject_key)
  ```

  Una alerta suprimida genera `DeliveryRecord(outcome="suppressed_cooldown")` —
  trazable, contada en el summary, nunca silenciosa. Valor inicial 30 s
  (declarado, calibrable); la ventana se define sobre `(condition, source)`
  porque para notificación asistiva lo relevante es "esta condición en esta
  cámara ya fue avisada", independiente del sujeto.
- **Ledger:** clave `(notification_id, channel)`; backing = los `DeliveryRecord`
  `delivered` en `notifications.jsonl` (append-only); re-ejecución segura
  (`skipped_duplicate`). El ledger deduplica **exactos** (misma alerta); el
  cooldown suprime **semánticos** (alertas distintas de la misma condición-fuente
  demasiado seguidas) — capas distintas, ambas necesarias.
- **Retry:** `max_attempts` (default 3) con espera fija corta; agotado →
  `outcome: dead_letter` + línea en `dead_letter.jsonl`. Nada más.
- **Salidas por corrida:** `notifications.jsonl`, `dead_letter.jsonl`,
  `distribution_summary.json` (conteos por outcome + agregados
  `t_alert-notification` min/mean/p95). El generador de reporte (spec 44 §4) los
  incorpora al `report.json`.

## 7. Orden de implementación y criterios de terminado

Orden: contratos + ledger + canal en `dry_run` con `DirectSource` de test →
`JsonlReplaySource` (DBE end-to-end contra una corrida real) → `transport/` +
`ZmqSource` (live) → Mosquitto en el compose + modo `live`.

- [ ] `distribute` en replay sobre una corrida real: `notifications.jsonl`
      completo, re-ejecución 100% `skipped_duplicate`.
- [ ] Modo live consumiendo el bus de alertas de una corrida EBE, con backfill
      verificado (alertas previas a la suscripción no se pierden).
- [ ] Entrega MQTT real observada con `mosquitto_sub`;
      `t_alert-notification` p95 en `distribution_summary.json`.
- [ ] QoS 1 duplicado simulado → deduplicado por ledger (test).
- [ ] Ráfaga de re-alertas de la misma condición-fuente → una sola notificación +
      `suppressed_cooldown` registrados (test de la política ADR-011).
- [ ] `experiment_id` presente en envelope y records; el `report.json` de una
      corrida con distribución lo muestra integrado (spec 44).

## 8. Interfaces

- **Spec 41:** consume su publisher `control.alert.v1.*`; no toca el motor.
- **Spec 44:** compose del broker; reporte integra `distribution_summary.json`;
  webconsole muestra outcomes (fase 2 de la vista de alertas).
- **Doc 06:** todo lo excluido (canales extra, backoff, dashboard, reproceso de
  dead-letter) queda diseñado ahí como anexo (E-06) — la incorporación futura no
  altera la semántica de la alerta (DA-13).

---

## 9. Servicio HTTP (ADR-019, 2026-08-17)

Extensión **aditiva** (regla 2 del `specs/README.md`): el módulo suma una interfaz de red
para ser una unidad desplegable propia. **El CLI de §8 no cambia** y sigue siendo el
camino offline; el subproceso de ADR-018 sigue disponible. Análisis y alternativas están
en [ADR-019](../decisiones/adr-019-servicio-http-distribucion.md); acá van contratos,
módulos y criterios de terminado.

### 9.1 Módulos

Espejo del control-plane, para que no haya un tercer estilo de servicio que aprender:

```
src/eovrt_distribution/
├── service/
│   ├── app.py           # create_app(): factory FastAPI + lifespan
│   ├── settings.py      # ServiceSettings.from_env() (runs_dir, config por defecto)
│   ├── run_request.py   # DistributionRunRequest (pydantic, extra="forbid")
│   ├── run_ids.py       # validación de run_id (evita traversal en la ruta)
│   ├── run_manager.py   # una corrida activa; hilo + estado + summary
│   └── routers/{health,runs,config}.py
└── cli.py               # + subcomando `serve` (replay/live intactos)
```

### 9.2 Contrato de corrida

`POST /api/runs` → **201** `{"distribution_run_id": "..."}`. Cuerpo
`DistributionRunRequest` con `extra="forbid"` (campo desconocido → **422**, nunca se
ignora en silencio):

| Campo | Modo | Notas |
|---|---|---|
| `mode` | ambos | `"replay"` \| `"live"` |
| `out_dir` | ambos | destino de los artefactos de §6 |
| `config_path` \| `config` | ambos | **exactamente uno** (ADR-009: por referencia o por payload) |
| `alerts_path` | replay | el `alerts.jsonl` a releer |
| `endpoint` | live | endpoint del bus de alertas |
| `control_run_id` | live | opcional; filtra la corrida del control-plane |
| `backfill` | live | opcional; alertas previas a la suscripción |
| `idle_timeout_ms` | live | opcional; > 0 y finito |

Los campos son los mismos argumentos del CLI: el servicio no inventa semántica, solo la
expone por red.

**Asíncrono.** Una corrida live dura minutos; `POST` no la espera. El estado se lee por
`GET /api/runs/{id}`, que sirve el `distribution_summary.json` que `Distributor.run()`
**ya escribe** en `out_dir` (§6) — el servicio no duplica el artefacto, lo publica.

### 9.3 Superficie

| Endpoint | Semántica |
|---|---|
| `GET /healthz` · `GET /readyz` | vivo / listo |
| `POST /api/runs` | 201 + id · **409** si ya hay una activa (con `active_run_id`) · 422 config inválida |
| `GET /api/runs` · `GET /api/runs/current` | listado · corrida activa (404 si no hay) |
| `GET /api/runs/{id}` | estado + summary · 404 si desconocida |
| `DELETE /api/runs/{id}` | **olvida la corrida del registro** · 204 · **409** si está activa (cancelar es `/cancel`, no borrar) |
| `POST /api/runs/{id}/cancel` | parada cooperativa (§9.4) |
| `GET /api/config` | config efectiva |

### 9.4 Ciclo de vida y la trampa de ZeroMQ

Una corrida activa por vez. Termina sola cuando la fuente se agota: en `replay` al fin del
archivo, en `live` por `idle_timeout_ms` o por el cierre de la corrida del control-plane.

La cancelación y el apagado usan **`ZmqSource.request_stop()`**, que ya implementa la
parada cooperativa (flag + `RCVTIMEO`, con el `sock.close(0)` dentro del mismo hilo del
loop). **Ningún socket se cierra desde un hilo distinto del que lo creó**: hacerlo aborta
el proceso con `SIGABRT`. El `lifespan` cierra con `shutdown()` + `join_active(timeout)`,
igual que el control-plane.

> **Desvío deliberado del espejo:** el control-plane **no** expone cancelación —su corrida
> live no se puede cancelar, y eso está registrado como trampa operativa—. El distribuidor
> sí la expone porque `request_stop()` ya existe y hace la parada segura: heredar la
> limitación sería copiar el molde en lo que tiene de defecto. Es la única diferencia
> intencional de superficie respecto del control-plane.

> **Qué borra `DELETE`, y qué no** *(✎ corrección 2026-08-17, hallazgo de revisión)*: borra
> **el registro en memoria** de la corrida, nada más. A diferencia del control-plane —cuyo
> `DELETE` limpia `runs_dir/<run_id>`— acá el servicio **no es dueño de ningún artefacto**:
> los escribe en `out_dir`, una ruta que elige el cliente (§9.2). Borrar `out_dir` desde un
> endpoint HTTP sería **borrado arbitrario de directorios por pedido del cliente**, así que
> no se hace: el que crea el directorio es quien lo limpia. Sin esta precisión el endpoint
> queda decorativo —devuelve 204 sin borrar nada— que es exactamente como se implementó la
> primera vez. Su valor real es acotar el crecimiento del registro en un servicio de vida
> larga.

### 9.5 Restricción declarada

`out_dir` se comparte entre el BFF y el servicio **por sistema de archivos**. Hoy es
gratis (mismo host); al containerizar es un volumen compartido. Misma condición que los
`runs_dir` de los otros dos planos — no es deuda nueva, pero es lo primero a resolver en
el paso de Docker.

### 9.6 Cliente: el runner del BFF

Gana un cliente HTTP con el mismo patrón de polling que ya usa con media y control.
**El default sigue siendo el subproceso (spec 44 §B4, ADR-018)**: el camino HTTP se
activa sólo con `EOVRT_CONSOLE_DISTRIBUTION_TRANSPORT=http`. *(✎ 2026-08-18 — en la
implementación quedó como loop propio y no como reuso de `_poll_until_terminal`: el
vocabulario terminal de ese helper no incluye `cancelled`, el estado propio de este
servicio.)*

### 9.7 Criterios de terminado

- [ ] `POST /api/runs` en `replay` sobre un `alerts.jsonl` real: 201, la corrida llega a
      estado terminal y `GET /api/runs/{id}` devuelve el mismo summary que imprime el CLI.
- [ ] Segunda corrida con una activa → **409** con `active_run_id`.
- [ ] Campo desconocido en el body → **422**; `config_path` y `config` juntos (o ninguno)
      → **422**.
- [ ] `GET /api/runs/{id}` con id inexistente → **404**; id con `../` → rechazado. *(El
      test debe usar una forma que **llegue al handler**, p. ej. `%2e%2e`: con `%2f` el
      router de Starlette responde 404 antes, y el test pasaría igual sin la validación.)*
- [ ] `DELETE` de una corrida terminada → **204**, y el `GET` siguiente → **404**; `DELETE`
      de una activa → **409**. `out_dir` **no se toca** en ninguno de los dos casos.
- [ ] Corrida `live` cancelada por `POST /cancel`: termina con
      `termination_reason = "requested_stop"`, sin `SIGABRT` y sin proceso huérfano.
- [ ] Apagado del servicio con una corrida live activa: `lifespan` la cierra y cosecha.
- [ ] **La suite del CLI pasa sin tocar** — es la prueba de que el cambio es aditivo.
- [ ] El runner del BFF dispara por HTTP y obtiene el mismo `distribution_summary.json`
      que obtenía por subproceso, sobre la misma corrida.

### 9.8 Fuera de alcance (diferido con causa, ADR-019 §4)

Dockerfile del distribuidor, su servicio en `infra/platform/docker-compose.yml` y la
containerización del control-plane. **El despliegue no es un resultado del informe**: es
evidencia de lo implementado y de portabilidad, y se reporta con su estado a la entrega.
