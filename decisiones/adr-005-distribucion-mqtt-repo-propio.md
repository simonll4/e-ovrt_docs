# ADR-005 — Distribución de alertas: recorte, canal MQTT y repo propio

> **✎ Estado de implementación (act. 2026-08-10):** **implementación COMPROMETIDA** por
> [ADR-016](adr-016-reapertura-acotada-distribucion.md), con el recorte de §1 de este
> documento y nada más (E-06 sigue excluida). *Decía "NO implementado, a propósito", y
> entre el 2026-08-05 y el 2026-08-10 estuvo declarado como exclusión cerrada por
> ADR-015 §2c — cláusula hoy derogada.*
>
> Construido a la fecha: **solo la frontera de salida** (`control.alert.v1`, publisher del
> control-plane, apagado por default). El repo `e-ovrt_alert-distribution` existe con su
> estructura pero **sin implementación** (cero commits; `src/eovrt_distribution/` son
> paquetes vacíos). Estado detallado y ciclo de vida completo de la alerta:
> [`../nucleo/19-cierre-arquitectura-ciclo-de-vida-alerta.md`](../nucleo/19-cierre-arquitectura-ciclo-de-vida-alerta.md).
> Detalle por ADR: [`estado-de-implementacion-adrs.md`](estado-de-implementacion-adrs.md).

- **Fecha:** 2026-07-09 (canal decidido 2026-07-06)
- **Estado:** Aceptada
- **Dimensión que atiende:** D5 (doc 03 §6) + ubicación del módulo (doc 06 §4)
- **Decisor:** usuario (canal: 2026-07-06; repo propio: 2026-07-09)

## Decisión

1. **Alcance recortado** (sobre el diseño completo del doc 06): un canal
   demostrativo + `NotificationEnvelope` + ledger de idempotencia
   (`notification_id` determinista, clave `(notification_id, channel)`) + retry
   mínimo (N intentos, registro) + **vista de alertas en la webconsole existente**
   (no dashboard nuevo). El diseño completo (4 canales, dead-letter, dashboard)
   queda como anexo (E-06).
2. **Canal: MQTT.** Fundamento defendible (doc 07 D5): peso mínimo (Mosquitto en el
   compose), estándar de integración IoT (Tabla 48), y medición limpia de
   `t_alert-notification` sin la variabilidad de una API externa. MQTT QoS 1 puede
   duplicar entregas → el ledger no es opcional.
3. **El módulo vive en un repo propio** (hermano, p. ej. `e-ovrt_alert-distribution`),
   **no dentro de `e-ovrt_control-plane`** — supera la decisión de ubicación del
   doc 06 §4. Consume `AlertEvent`s por el **bus control→distribución** (ZeroMQ
   PUB/SUB, mismo patrón `transport/` wire-compatible) con backfill desde
   `alerts.jsonl`. El control-plane no conoce canales ni ledger: publica alertas
   confirmadas y nada más.

## Alternativas consideradas

- **Módulo dentro del control-plane** (doc 06 §4, "un tercer paquete sería
  prematuro"): descartada — el repo propio materializa la frontera estricta de
  §17.3.10.1/DA-13 en la estructura misma del sistema y el seam ya estaba diseñado
  (`AlertStreamSource`/`ZmqSource`); el costo es solo empaquetado.
- **Telegram como canal:** efecto de demo, pero mide la latencia de una API externa
  ajena al sistema; para la defensa, `mosquitto_sub` en vivo + webconsole basta.

## Impacto

- Repo nuevo con `transport/` propio (nace ahí; extracción a paquete compartido
  sigue siendo futura y mecánica).
- El control-plane suma el publisher de alertas al bus (pieza chica, junto al sink).
- Doc 06 se conserva como diseño original; su §4 (ubicación) queda superado por
  este ADR. E-06 (canales extra + dashboard) no cambia.
- Preguntas abiertas del doc 06 §20 ya cerradas en doc 07 H11 (plantilla fija en
  código; una corrida por vista; `t_alert-notification` DBE = wall-clock etiquetado).

## Referencias

Doc 02 §4.7, doc 03 §6, doc 06, doc 07 D5/H11, doc 10 E-06.
