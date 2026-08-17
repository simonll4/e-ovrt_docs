# 118 — Campaña de medición de `t_alert-notification` en modalidad live

- **Fecha de ejecución:** 2026-08-13
- **Estado:** cerrado; cifra citable y artefactos curados publicados
- **Dependencias:** ADR-016, spec 45, diseño `2026-08-13-campana-t-alert-notification-design`, y docs/operacion/114 y 115.
- **Responsable de configuración/orquestación:** `e-ovrt_experimental-setup`

## 0) Objetivo de la campaña

Producir una cifra citable de:

`t_alert-notification = puback_wall_ms - ts_publish_ms`

para el tramo live real (`control.alert.v1` → `eovrt-distribute` → MQTT QoS 1), con trazabilidad completa por `run_id` y `notification_id`.

## 1) Alcance y corpus

La evidencia canónica de la campaña se toma de:

- `e-ovrt_experimental-setup/results/evidence-runs.md`
- `e-ovrt_experimental-setup/results/evidence-runs/resolved-runs.json`

Consolidado vigente:

- **Primario:** 400 runs DBE + 13 runs EBE históricas no derivadas (total **413** runs; **356** con eventos potenciales).
- **Suplementario:** 544 runs decimado empírico (`control_replay_empirico`), solo para cobertura contractual, **no** incluido en el agregado principal. El mismo conjunto figura en `corpus.json` como `supplemental_derived_ebe`.
- El agregado principal usa exclusivamente `mode=live` y `latency_mode=live`.

## 2) Criterios de salida citable

Para declarar el resultado como citable:

- `413` corridas ejecutadas y cada una finaliza con `run_finished`.
- `bus_dropped_events = 0` y `dead_letter = 0` en resumen de distribución.
- `skipped_malformed = 0` y `skipped_invalid_alerts = 0`.
- Conteo de outcomes coherente con `distribution_summary.json`.
- Cada `notification_id` esperado aparece en el suscriptor testigo y no hay IDs inesperados sin causa.
- `t_alert-notification` calculada solo con registros con `mode=live` y `latency_mode=live`.

Si un gate falla, no se publica cifra agregada. Se registra causa y se repite la corrida completa.

## 3) Checklist operativo previo

1. `cd e-ovrt_experimental-setup && python3 tools/evidence_runs.py --check --archive-only`.
2. Verificar disponibilidad/estado de puertos: `5557`, `5558`, `8080`, `8081` y `1883`.
3. Iniciar broker real de laboratorio:
   - `cd e-ovrt_experimental-setup/infra/platform && amqtt -c mosquitto/amqtt.yaml`
4. Levantar un suscriptor testigo en `eovrt/alerts/#` y confirmar recepción.

## 4) Manifiestos a preparar

Manifiestos reales en `e-ovrt_experimental-setup/experiments/t_alert_notification/`:

- `campaign.yaml`
- `distribution-live.yaml`
- `distribution-replay.yaml`
- `video/manifest.template.yaml`
- `camera/*.template.yaml`

Reglas de manifiesto:

- `runs.media.mode: run`
- `runs.control.mode: live`
- `runs.distribution.mode: live`
- `runs.distribution.config` con `channel.mode: live`; el broker MQTT vive en
  `channel.host`/`channel.port` del YAML del distribuidor (`127.0.0.1:1883`).
- `runs.distribution.endpoint` es el SUB ZeroMQ al bus de alertas del control-plane:
  `tcp://127.0.0.1:5558`. El broker MQTT nunca va en ese campo.

## 5) Secuencia de corrida

### Fase principal (413 runs)

- Correr los 413 runs (400 DBE + 13 EBE no derivado), uno por uno.
- Un `out_dir` y ledger limpio por corrida.
- No compartir cache entre corridas.

### Fase suplementaria (544 runs)

- Ejecutar los 544 runs de `control_replay_empirico` en una secuencia separada.
- Mantener salidas separadas y nunca mezclar con el agregado principal.

### Fase integrada

- 3 corridas E2E de video/clip con ruta completa `media → control → distribution`.
- El smoke con cámara previsto no se ejecutó: ni OAK-D ni RTSP estaban conectadas. Esta
  indisponibilidad física no se interpreta como evidencia negativa del sistema.
- Estas corridas no se agregan al primario.

## 6) Evidencia mínima a persistir

En `results/realtime/t_alert_notification/`:

- `campaign.yaml`
- `corpus.json`
- `provenance.json`
- `metrics.json`
- `outcomes.csv`
- `integrated-runs.json`
- `camera-smoke.json`

Por cada corrida:

- `runs/<run_id>/report.md`
- `runs/<run_id>/report.json`
- `runs/<run_id>/distribution/distribution_summary.json`

## 7) Riesgos y acciones

- Si no hay `run_finished`, repetir corrida completa.
- Si el broker no es real o no publica PUBACK QoS 1, no hay cifra validable.
- Si hay mismatch entre ledger y suscriptor testigo, detener y repetir con causa documentada.
- QoS 1 admite duplicados; validar multiconjunción por `notification_id` y no por igualdad estricta de líneas.

## 8) Criterio de entrega para informe

- Reportar `t_alert-notification.p95`, `median`, `min/max`, conteo de outcomes y tasa de cooldown.
- Dejar explícito que solo se agregó el tramo con `latency_mode=live`.
- Conservar log de corridas excluidas y motivo de exclusión.

## 9) Resultado ejecutado

La cifra aceptada para el informe es:

> **F-118.1 — `t_alert-notification` p95 = 64,534 ms (n = 460 entregas live)**

Estadísticos del agregado principal, en milisegundos: mínimo **27,766**, media **42,577**,
p50 **41,434**, p95 **64,534**, p99 **105,926** y máximo **119,443**. El cálculo usa
nearest-rank sobre cada `DeliveryRecord` elegible; no promedia percentiles por run.

El corpus principal se ejecutó completo: **413 runs**, **356** con alertas y **836** eventos.
**F-118.2.** Los outcomes fueron **460 `delivered`** y **376 `suppressed_cooldown`** (44,976 % del total de
eventos). Las 460 entregas fueron observadas por el testigo MQTT, sin duplicados ni IDs
inesperados. Todos los runs cerraron por `run_finished`; los contadores de drops, dead letters,
eventos malformados y alertas inválidas fueron cero.

Como análisis de sensibilidad por procedencia histórica, el p95 fue **61,770 ms** en DBE
(n=447) y **71,808 ms** en EBE no derivada (n=13). No se interpreta la diferencia entre estos
subgrupos como contraste inferencial: el tramo se republicó live y la muestra EBE es pequeña.

La validación integrada usó `a_p1_c08` y completó tres repeticiones desde video hasta el reporte,
con una entrega por repetición y valores de **116,839**, **152,901** y **91,588 ms**. En las tres,
`report.json` publicó `t_alert-notification` como `computed`; no hubo drops, entradas inválidas ni
divergencias con el testigo MQTT. Estas cuatro observaciones integradas —admisión más tres
repeticiones— permanecen separadas del agregado principal.

**F-118.3.** El smoke de cámara se registra como **`not_executed: hardware_source_not_connected`**. Los
intentos de admisión que no procesaron unidades quedan excluidos y no se presentan como un
resultado negativo. La cámara era una validación suplementaria y nunca una fuente de muestras
para el p95 principal; por ello su indisponibilidad no altera la validez de la cifra del tramo
`alert bus -> PUBACK`, cuyo acople completo quedó además validado desde video.

### Análisis steady-state (agregado 2026-08-14)

El mismo `outcomes.csv`, sin re-corrida, se particionó por la primera entrega de cada
corrida. Las primeras entregas representan el **77,4 %** de la muestra y son las más
rápidas: **p95 = 49,869 ms (n = 356)**. Para las entregas 2.ª en adelante, la lectura
honesta de operación continua es **p95 = 102,025 ms (n = 104)**. El p95 principal
de 64,534 ms continúa siendo el agregado citable de todas las entregas.

El payload MQTT observado por el testigo fue de **1.078 bytes en p95** (n = 460;
mínimo 1.022, p50 1.037 y máximo 1.835), según el bloque `payload_bytes` regenerado
por el agregador en `metrics.json`.

**Enmienda de procedencia (2026-08-14).** Los bloques `steady_state` y `payload_bytes` se
habían insertado a mano sobre el `metrics.json` publicado: el `candidate-metrics.json` del
intento no los contenía, el agregador rechazaba re-agregar un intento ya publicado y la
plantilla del README no los emitía, de modo que regenerar la publicación los habría borrado
en silencio. Se cerró la brecha en el pipeline (`verify --allow-completed` para re-agregar
desde las fases inmutables y `rebuild-curated` para re-derivar `metrics.json` y `README.md`
del candidato) y se regeneró el artefacto: **ningún valor publicado cambió** y la única
adición fue la clave derivada `primary.cooldown_rate` (376/836 = 0,44976, la tasa que este
documento ya citaba). El máximo del régimen sostenido pasó de `119,442` a **119,443** ms
porque la plantilla redondea en lugar de truncar. `provenance.json` conserva su
`accepted_at` y su `publication_tooling_sha256` del 2026-08-13 y registra la enmienda con el
hash del utillaje posterior en su bloque `amendments`. Constancia: `operacion/119`.

## 10) Evidencia y formulación citable

Los artefactos están en
`e-ovrt_experimental-setup/results/realtime/t_alert_notification/`. `metrics.json` contiene la
cifra y los gates; `outcomes.csv` permite recomputar las 1.410 decisiones de las series principal
y suplementaria; `integrated-runs.json` conserva los IDs de las repeticiones E2E; y
`provenance.json` registra versiones, commits, hashes, árbol dirty y exclusiones.

Formulación recomendada: *La latencia de distribución de alertas, definida desde la publicación
en el bus del control-plane hasta el PUBACK del broker MQTT QoS 1, presentó un p95 de 64,534 ms
sobre 460 entregas live. Esta cifra no incluye captura, inferencia ni evaluación del patrón.*
