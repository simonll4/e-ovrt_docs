# ADR-011 — Frontera de la política de alertas: el motor emite siempre; la supresión es de distribución

- **Fecha:** 2026-07-09
- **Estado:** Aceptada
- **Decisión que atiende:** nueva (decisión del usuario, a raíz de revisar el
  cooldown de la rama `mati` en el spec 41). Ajusta specs 41/43/45.
- **Decisor:** usuario, 2026-07-09

## Decisión

1. **El control-plane emite un `AlertEvent` cada vez que un patrón declarado
   cumple sus reglas** (transición a `confirmed`), sin supresión posterior:
   `alerts.jsonl` es el **registro fiel de la dinámica del patrón**. Lo que SÍ es
   semántica de patrón —y se queda en el motor— es la evidencia y la persistencia
   temporal: umbrales, región, matching 1:1, **memoria de cobertura, histéresis
   confirm/resolve, expiración de sujetos** (absorben el ruido perceptual, no la
   política de notificación).
2. **El cooldown de re-alerta y toda política de notificación** (supresión por
   ventana, agrupación, rate-limiting) **pertenecen al módulo de distribución**
   (`e-ovrt_alert-distribution`, ADR-005): es el que decide cuántas veces
   molestar a un consumidor con una condición ya notificada. Config
   `notification_policy.cooldown_ms` por `(condition_id, source_id/subject_key)`,
   con outcome trazable `suppressed_cooldown` en el `DeliveryRecord`.
3. El parámetro `realert_cooldown_ms/frames` del motor (rama `mati`) **queda como
   capacidad no usada por la plataforma**: los pattern sets de plataforma
   (`cr01_cr02_v2`) lo dejan sin configurar (None = desactivado, que es el
   default del motor). No se elimina código; `field_v1` lo conserva como perfil
   de diagnóstico/labs, documentado como tal.

## Fundamento

1. **Frontera limpia y defendible:** detección ≠ patrón ≠ alerta ≠ notificación.
   El propio diseño de distribución (doc 06 §2) ya separa "confirmación, intento
   de entrega, resultado"; la supresión es política del tramo de entrega, igual
   que la idempotencia del ledger.
2. **Métricas más honestas:** con supresión en el motor, la tasa de re-alertas
   (señal de estabilidad de la percepción, hallazgo del experimento Intel
   2026-06-26) quedaba oculta. Emitiendo siempre, esa señal se mide; suprimirla
   es decisión del consumidor.
3. **Elimina dos defectos detectados en la revisión del spec 41:** (a) el
   cooldown de `field_v1` (5000 ms) quedaba inerte con las ventanas del informe
   (ciclo mínimo de re-alerta 6–10 s > cooldown); (b) bajo G0 el cooldown del
   motor cambiaba de significado ("mismo trabajador" → "misma cámara") por
   accidente de la clave de estado. En distribución, la ventana se define
   explícitamente sobre `(condition, source)` — que es lo correcto para
   notificaciones asistivas — con valor inicial declarado y calibrable (30 s).

## Consecuencia para la evaluación (specs 41/43)

`evaluate-alerts` evalúa **a nivel episodio**: un episodio GT está detectado si
≥1 alerta cae en su ventana de matching; las alertas adicionales del mismo
episodio se reportan como `re_alerts` (métrica de estabilidad), **no** como
falsos positivos. FP = alerta fuera de todo episodio. La métrica de "no molestar
dos veces" se mide en el tramo de distribución (`suppressed_cooldown` en los
DeliveryRecords), separada de la alerta interna — exactamente DA-13.

## Impacto

- **Spec 41:** pattern set v2 sin cooldown; evaluador por episodio (§8.6).
- **Spec 45:** sección `notification_policy` (cooldown por condición-fuente).
- **Spec 43 §4.1:** matching ajustado (re-alertas del episodio ≠ duplicadas FP).
- **Informe:** el `cooldown` que la Tabla 44 lista como parámetro de RunConfig se
  redline-a como parámetro del tramo de distribución (agenda doc 02 §4.8).

## Referencias

Doc 01 §12.1.5 (origen del cooldown en `mati`), doc 06 §2/§6, doc 02 §2.3 (DA-13),
specs 41/43/45, conversación de revisión 2026-07-09.
