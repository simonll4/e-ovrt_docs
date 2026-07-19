# ADRs — Estado de implementación (cierre de trazabilidad)

- **Fecha:** 2026-07-18
- **Propósito:** cerrar el loop **decisión → implementación** para cada ADR. Los ADRs
  se escribieron *antes* de implementar y expresan su impacto como trabajo futuro;
  este documento registra, con rutas reales, endpoints y evidencia medida, **cómo
  terminó implementada cada decisión** al 2026-07-18. Los ADRs no se editan (carpeta
  cerrada); este doc es su companion de cierre y se actualiza con causa.
- **Cómo leer:** siglas en el doc 13 (glosario). Para cada ADR: la decisión en una
  frase autocontenida, cómo quedó implementada, la evidencia, y lo pendiente.
  La foto completa de la plataforma es el doc 56.

---

## 0. Tabla resumen

| ADR | Decisión (una frase) | Estado de implementación |
|---|---|---|
| 001 | La estrategia de detección del núcleo es **indirecta** (detectar persona+EPP y razonar la ausencia), no prompts de infracción directa | **Implementada como encuadre**; cierre experimental (D1) pendiente del acta `edir_v1` |
| 002 | El patrón se evalúa **por escena (G0)**, sin identidad de personas; el modo por-sujeto (G1) es solo demostrativo | **G0 implementado y verificado** (gate F1=1.0); G1 **no portado** (deuda) |
| 003 | El acople live media→control es **bus ZeroMQ PUB/SUB + msgpack**, broker diferido | **Implementado y demostrado** (paridad byte-idéntica replay↔stream) |
| 004 | La corrida experimental es un **manifiesto paraguas** con `experiment_id` propagado, orquestada por un runner HTTP | **Implementado** (runner + manifiesto + propagación a ambos planos) |
| 005 | La distribución de alertas se recorta a **un canal MQTT en repo propio** | **NO implementado** (diferido para lo último por decisión del usuario); solo existe la frontera de salida (`control.alert.v1`) |
| 006 | El reporte consolidado junta ambos planos por `experiment_id` y **cada métrica declara su aplicabilidad** con causa | **Implementado** (report.json/md + estados en todos los evaluadores) |
| 007 | En vivo, la corrida del control-plane es **1:1** con el run del media-plane y cierra por `run_finished` | **Implementado y verificado E2E** |
| 008 | El control-plane se expone como **servicio HTTP mínimo** (:8081) | **Implementado y superado** (11 endpoints vs los 3 decididos) |
| 009 | La config experimental se **centraliza** en experimental-setup y la **webconsole es la superficie de gestión primaria** | **Implementado y superado** (consola rediseñada, 10 páginas) |
| 010 | Se ejecuta **la plataforma primero**, la evaluación después; el clip bench se dispara al cierre del spec 44 | **Cumplida** (orden 40→41→42→44 ejecutado; tooling del 43 completo) |
| 011 | El motor **emite en cada confirmación**; cooldown y supresión son política de notificación (módulo de distribución) | **Implementado** en motor y evaluador; la política espera al spec 45 |
| 012 | Bajo G0 la memoria de cobertura EPP **se ignora con causa declarada** (la histéresis subsume el parpadeo) | **Implementado y FALSACIÓN SUPERADA** (los dos tests condición-de-merge pasaron) |
| 013 | La plataforma **detecta la temporalidad de la fuente** y declara sola la no-aplicabilidad de métricas temporales | **Implementado con evidencia medida** (137 eventos / 0 alertas sobre imágenes) |
| 014 | Los resultados de un run global se **consolidan con híbrido selectivo** (liviano copiado, crudo referenciado) | **Implementado** (consolidación + reporte); "sellado" opt-in sin ejercitar |

## 1. Detalle por ADR

### ADR-001 — Estrategia E-IND (encuadre)

- **Decisión:** el núcleo detecta con prompts de **evidencia positiva** (persona,
  casco, chaleco) y razona la ausencia geométricamente (E-IND); los prompts que
  describen la infracción ("persona sin casco", E-DIR) son variante comparativa, y la
  fusión E-HYB se corre siempre en la Fase 2 del experimento D1.
- **Cómo quedó:** E-IND es lo único cableado end-to-end: el evaluador espacial vive en
  `e-ovrt_control-plane/src/eovrt_control/engine/evaluators/spatial_absence.py`
  (regiones `upper_body`/`torso` del pattern set `cr01_cr02_v2`). Los prompt sets del
  experimento existen con ciclo de vida en `e-ovrt_experimental-setup/prompts/`:
  `eind_v1` está **`frozen_pending_review`** (espera el acta del usuario) y los sets
  E-DIR exploratorios quedaron en `prompts/_archive/`. La bajada operativa completa
  (comparabilidad, calib/test, fusión) es el doc 12.
- **Evidencia:** benchmark de modelos doc 31 (insumo: YOLOE ciego a `bare_head` ⇒
  restringe el espacio de búsqueda de D1); toda la plataforma corre E-IND en los E2E
  de docs 35/37/38/51.
- **Pendiente:** el **experimento D1 no se corrió** (bloqueado por el acta `edir_v1`).
  Este es el único punto que puede revisar el ADR. Insumo nuevo: el comparativo de 3
  backends sobre `video16_clip10` (doc 56 §2.2).

### ADR-002 — Granularidad G0 núcleo + G1 demostrativa

- **Decisión:** el estado del patrón se clava por `(pattern_id, source_id)` — escena,
  sin identidad de personas (G0). El modo por-sujeto (G1, con tracker que emite
  `track_id`) es demostrativo: sin métricas MOT, sin GT de identidades.
- **Cómo quedó:** G0 **implementado el 2026-07-10** (doc 34): la clave de estado es de
  escena en `engine/pattern_engine.py`, y el gate se alcanzó — **F1 = 1.0 en ambas
  granularidades, verificado significativo**; el BENCH bajó de 137 a 77 alertas *por
  diseño* con invariante Σ`subjects_in_evidence_max` = 137 exacto (la re-verificación
  sobre datos frescos del doc 34 §2.3 dio 141→77 con Σ=141 — mismo invariante, corrida
  distinta; la cifra canónica del set es 137). El contrato ya
  acepta la evolución: `track_id` es campo **opcional** de `Detection` desde el
  2026-07-13 (media-plane `0133d38`).
- **Evidencia:** doc 34 completo; corroboración empírica de la limitación D2.2 (un
  riesgo transitorio adelanta el reloj del episodio de escena).
- **Pendiente:** **G1 no está portado**: el `SimpleIoUTracker` existe solo en
  `e-ovrt_control-plane/src/eovrt_labs/perception/tracking.py` (paquete experimental)
  y **nadie produce `track_id`** ⇒ el modo `subject` del motor está inerte (deuda del
  spec 42 §3, vigente).

### ADR-003 — Bus media→control: ZeroMQ PUB/SUB

- **Decisión:** en el escenario offline (DBE) el acople sigue siendo por archivo
  (`detections.jsonl` → replay); en vivo (EBE), bus ZeroMQ PUB/SUB con msgpack y
  envelope versionado; broker (Kafka/RabbitMQ) fuera de alcance con el seam
  documentado.
- **Cómo quedó:** **implementado el 2026-07-10** (doc 37). Publisher del lado media:
  `e-ovrt_media-plane/src/eovrt_media/transport/bus.py` (`BusPublisher`, socket XPUB,
  envelope `bus.envelope.v1`, `seq` monótono, persiste-primero: el JSONL es la
  verdad). Consumidor del lado control:
  `e-ovrt_control-plane/src/eovrt_control/sources/bus.py` (`BusSource`, SUB, cuenta
  `bus_dropped_events` por huecos de `seq`, parada cooperativa `request_stop()`).
  Knob `bus.enabled` en la config del media-plane.
- **Evidencia:** gate de paridad replay↔stream **byte-idéntica**, verificado
  significativo por mutación (bbox 1 px ⇒ falla); E2E real 40/40 unidades, 0
  perdidas, cierre por `run_finished` (doc 37 §4; datos en `operacion/datos/37-*`).
- **Pendiente:** nada del alcance decidido. El broker sigue diferido, como se decidió.

### ADR-004 — Corrida paraguas y `experiment_id`

- **Decisión:** la corrida experimental es un manifiesto paraguas en
  experimental-setup que **referencia** (no fusiona) las configs de ambos planos; un
  `experiment_id` viaja a los dos; un runner CLI orquesta por HTTP.
- **Cómo quedó:** **implementado el 2026-07-11** (doc 53). Manifiesto
  `experiment.manifest.v1` y runner en
  `e-ovrt_experimental-setup/webconsole/backend/src/eovrt_webconsole/experiment/runner.py`
  (secuencia live=control-first con guardián `SubscriptionNotConfirmed`,
  replay=media-first). `experiment_id` aceptado por `POST /api/runs` del media-plane
  (spec 42 §4.1) y presente en los tres eventos del control-plane (doc 51). La
  webconsole dispara orquestado vía `ExperimentRunManager` (un experimento activo).
- **Evidencia:** corridas orquestadas reales (doc 53; primera con GT:
  `experiments/video16_clip10_gt/`, doc 56 §2.3).
- **Pendiente:** nada del alcance decidido (la ampliación del rol de la webconsole la
  cerró ADR-009, ver abajo).

### ADR-005 — Distribución: MQTT en repo propio

- **Decisión:** el módulo de distribución se recorta a un canal demo MQTT con ledger
  de idempotencia, en un **repo hermano propio**, consumiendo las alertas confirmadas
  por bus.
- **Cómo quedó:** **NO implementado, a propósito**: el spec 45 está escrito y su
  ejecución quedó **para lo último** por decisión del usuario (registrada en
  ADR-010/doc 55). Lo único construido es la **frontera de salida** del control-plane
  que el módulo consumirá: el publisher `control.alert.v1`
  (`e-ovrt_control-plane/src/eovrt_control/transport/alert_bus.py`, XPUB,
  persiste-primero, apagado por default) — doc 51.
- **Pendiente:** todo el módulo (repo, canal MQTT, `NotificationEnvelope`, ledger,
  vista en consola). No bloquea al clip bench (ADR-010).

### ADR-006 — Reporte consolidado y aplicabilidad de métricas

- **Decisión:** un generador en experimental-setup junta los artefactos de ambos
  planos por `experiment_id` en `report.json` + `report.md`, y **toda métrica declara
  su estado de aplicabilidad** (`computed | applicable_not_computed | not_applicable |
  not_interpretable`) con causa.
- **Cómo quedó:** **implementado el 2026-07-11** (doc 53): generador en
  `experiment/report.py` + `experiment/applicability.py`. Los estados están cableados
  en toda la cadena: el join `t_capture→alert` del control-plane (doc 51), el
  evaluador temporal v2 (`evaluation/temporal.py`, doc 52: causas
  `not_applicable:non_temporal_source`, `not_applicable:no_ground_truth`, etc.) y el
  bloque G2A del media-plane (doc 39).
- **Evidencia:** E2E reales con los tres veredictos correctos por tipo de fuente:
  video DBE → `not_interpretable/dbe_media_time`, imágenes → `non_temporal_source`,
  sin GT → `no_ground_truth` (docs 51/53).
- **Cierre de condicional:** el ADR dejaba dos opciones para los relojes en two-node;
  quedó resuelta con la **opción declarativa**: `g2a_ms = null` y bloque
  `not_interpretable / cross_node_monotonic_clock` (doc 39) — no se implementó
  sincronización NTP/chrony.

### ADR-007 — Corrida 1:1 en vivo

- **Decisión:** una corrida live del control-plane consume exactamente un run del
  media-plane: nace suscripta antes del run, y cierra cuando llega
  `run.lifecycle.v1/run_finished`.
- **Cómo quedó:** **implementado el 2026-07-10** (docs 37/38): runtime live en
  `runtime/live.py`, `control_run_id` referencia `media_run_id` en el summary, y el
  invariante operativo quedó **estructural**: el 201 de `POST :8081/api/runs`
  (`mode: live`) implica `BusSource` ya suscripto (el gate anterior era vacuo y se
  reemplazó, doc 38). Desde el 07-17 además `GET /api/runs?media_run_id=` permite la
  correlación inversa (consola).
- **Evidencia:** E2E 30/30 unidades con los dos servicios hablándose (doc 38 §4).
- **Pendiente:** las "ventanas de evaluación propias" que el ADR difirió siguen
  difereridas (no hicieron falta: la evaluación temporal las cubrió por otro camino,
  doc 52).

### ADR-008 — Control-plane como servicio mínimo

- **Decisión:** el control-plane se expone como servicio FastAPI mínimo (disparar
  corrida, estado, config), un run activo por vez; la webconsole es cliente de ambos
  planos.
- **Cómo quedó:** **implementado el 2026-07-10** (doc 38) y **superado después**:
  `eovrt-control serve` en :8081; hoy **11 endpoints** (`/healthz`, `/readyz`,
  `GET /api/config`, `POST/GET /api/runs`, `/runs/current`, `/runs/{id}`,
  `DELETE /runs/{id}`, `/runs/{id}/alerts`, `/runs/{id}/pattern-progress`,
  `/runs/{id}/received-units`) — doc 56 §3.3. Un run activo (409). La "cáscara
  sacrificable" no solo no se sacrificó: creció con la observabilidad de la consola.
- **Evidencia:** docs 38/51/56; suite `test_service_api.py` (29 tests).

### ADR-009 — Config centralizada + webconsole superficie de gestión

- **Decisión:** la config experimental (manifiestos, prompts, pattern sets activos)
  vive centralizada en experimental-setup; los servicios la reciben al disparar y
  persisten `effective_config`; la webconsole es la superficie de gestión primaria y
  el runner CLI queda como camino headless con las mismas APIs.
- **Cómo quedó:** **implementado el 2026-07-11 y ampliado el 07-17/18**: ambos planos
  aceptan config por payload y escriben `effective_config.yaml`; los prompt sets
  tienen ciclo de vida gestionado desde la consola (`prompt_store.py`, estados
  `exploratory`/`frozen` con `frozen_sha256`); la consola es hoy 10 páginas con
  sistema de diseño propio, vista correlacionada media↔control, gestión de cámaras
  con preview en vivo y borrado orquestado de runs (doc 56 §2.3/§3.4). El runner CLI
  usa las mismas APIs (doc 53).
- **Evidencia:** docs 53/56; suites BFF 310 / SPA 157.
- **Nota de vigencia:** este ADR es el que **rige** el rol de la webconsole (amplía
  ADR-004 y ADR-008); ver §2 "vista por tema".

### ADR-010 — Secuenciación: plataforma primero

- **Decisión:** primero el tramo plataforma (servicios, bus, config, trazabilidad,
  instrumentación), después la evaluación; el clip bench (spec 43) se dispara al
  cierre del spec 44; la distribución (spec 45) no bloquea; el material crudo de
  videos se arma en paralelo.
- **Cómo quedó:** **cumplida tal cual**: la cola 40→41→42→44 se ejecutó completa
  (docs 37/38/39/51/52/53), el tooling del 43 se construyó al cierre del 44 (doc 54:
  video-gt-lab completo) y el material crudo avanzó en paralelo (7 clips normalizados
  + preanotados en `e-ovrt_datasets/datasets-videos/`). El 45 sigue al final, como se
  decidió.
- **Pendiente del tramo evaluación:** pasada humana del GT, grabación del banco A+C,
  corridas del banco, experimento D1 (doc 55 pasos 1–5).

### ADR-011 — Frontera de política de alertas

- **Decisión:** el motor emite un `AlertEvent` en **cada confirmación** del patrón
  (sin supresión); el cooldown/re-notificación es política del módulo de
  distribución; el evaluador cuenta `re_alerts` sin penalizarlas como falsos
  positivos.
- **Cómo quedó:** **implementado del lado motor y evaluador**: el pattern set oficial
  `cr01_cr02_v2` va **sin cooldown** (`configs/patterns/cr01_cr02_v2.yaml`; el campo
  `realert_cooldown` del motor existe y queda en `None` — capacidad no usada, como se
  decidió); `evaluate-alerts` v2 reporta `re_alerts_count` aparte (doc 52,
  `evaluation/temporal.py`).
- **Pendiente:** la `notification_policy` con cooldown vive en el spec 45 (no
  implementado, ver ADR-005).

### ADR-012 — Memoria de cobertura bajo G0

- **Decisión:** con granularidad de escena no hay identidad de sujeto, así que la
  memoria de cobertura EPP **es inaplicable**: el motor la ignora declarando la causa
  `coverage_memory_unsupported_scene` (la histéresis `resolve_after_ms` subsume el
  parpadeo); la memoria sobrevive solo bajo G1. El ADR se aceptó **sujeto a falsación
  por dos tests** condición-de-merge.
- **Cómo quedó:** **implementado y falsación SUPERADA el 2026-07-10** (doc 34): los
  dos tests pasaron — gate F1 = 1.0 (verificado significativo) y el test de parpadeo;
  además un **par discriminante** confirmó empíricamente la decisión. En código:
  `_memory_applicable` en `engine/pattern_engine.py` (solo `granularity: subject`),
  causa de degradación declarada en el summary.
- **Estado vigente:** la reversión prevista ("memoria a nivel escena") **no se
  activó** y no hay causa para activarla.

### ADR-013 — Aplicabilidad por temporalidad de fuente

- **Decisión:** la plataforma detecta la temporalidad por `source_type` y declara
  sola qué mide cada fuente: imágenes → percepción/asociación espacial (los patrones
  con persistencia **no pueden alertar**), video → patrones con GT temporal, RTSP →
  patrones + métricas end-to-end. La corrida sobre imágenes no se rechaza: se degrada
  con causa (`not_applicable / non_temporal_source`).
- **Cómo quedó:** **implementado con la evidencia medida que el propio ADR cita**: el
  probe del doc 33 §4 (137 eventos de patrón, **0 alertas** sobre el BENCH de
  imágenes) es el comportamiento hoy cableado en los evaluadores y el reporte
  (docs 51/52/53); `source_clock` soporta `none`; la consola marca las corridas
  no-temporales (badge ADR-013 en la vista de reporte).
- **Evidencia:** doc 33 §4 (medición), doc 53 (estados en reporte E2E real).

### ADR-014 — Layout de artefactos por experimento

- **Decisión:** run global → consolidado en
  `experimental-setup/runs/<experiment_id>/` (git-ignored) con **híbrido selectivo**:
  configs/summaries/metrics/alerts/report se copian; los `detections.jsonl` pesados
  se **referencian** por `run_id` (fuente de verdad = `runs/` del plano). Run de test
  de módulo → local, sin consolidar. "Sellado" opt-in materializa crudos.
- **Cómo quedó:** **implementado el 2026-07-11** (doc 53):
  `experiment/consolidation.py` arma el layout exacto y **nunca copia** los crudos;
  el reporte agrega desde el consolidado.
- **Pendiente:** el "sellado" opt-in quedó previsto pero **no se ejercitó** en ninguna
  corrida real (sin evidencia de uso; verificar su cableado cuando se archive el
  primer experimento definitivo).

## 2. Vista por tema (resuelve la superposición de ADRs)

Para saber **qué rige hoy** cuando varios ADRs tocan lo mismo:

| Tema | Cadena de ADRs | Estado vigente |
|---|---|---|
| **Rol de la webconsole** | 004 ("muestra") → 008 ("cliente de ambos planos") → **009 (rige: superficie de gestión primaria)** | Consola = gestión primaria (configs, prompts, cámaras, runs, experimentos); runner CLI = camino headless con las mismas APIs |
| **Config** | 004 (manifiesto referencia) + **009 (rige: centralizada en experimental-setup)** | Config experimental centralizada, entregada por payload, `effective_config` persistido por cada plano |
| **Artefactos/resultados** | 004 (`experiment_id`) + 006 (reporte) + **014 (rige: layout híbrido selectivo)** | Consolidado liviano + crudos referenciados; reporte con estados de aplicabilidad |
| **Alertas y su política** | **011 (rige: motor emite todo)** + 005 (la política vive en distribución, no implementada) | Sin cooldown en plataforma; `re_alerts` contadas, no penalizadas |
| **Qué mide cada corrida** | 006 (vocabulario de aplicabilidad) + **013 (rige: por temporalidad de fuente)** + 012 (causa específica de G0) | La plataforma declara sola qué aplica, con causa, sin rechazar corridas |

## 3. Condicionales de los ADRs: resolución registrada

| ADR | Condicional que dejaba abierto | Resolución |
|---|---|---|
| 001 | "el cierre definitivo lo da el experimento D1" | **Sigue abierto** (acta `edir_v1` pendiente); el encuadre E-IND rige mientras tanto |
| 006 | dos opciones para relojes two-node | Resuelto: **declarativa** (`not_interpretable/cross_node_monotonic_clock`, doc 39) |
| 007 | ventanas de evaluación propias "trabajo futuro" | No hicieron falta: la evaluación temporal v2 (doc 52) cubre el caso |
| 012 | "sujeta a falsación por test" | **Falsación superada** (doc 34); la reversión no se activó |
| 002/008/009 | recortes "si la agenda aprieta" (G1-demo, cáscara HTTP, mejora UX) | Ninguno se ejerció; al revés: servicio y UX se ampliaron. G1 sigue sin portar pero por orden de prioridad, no por recorte |
