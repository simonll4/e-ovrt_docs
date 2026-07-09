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
