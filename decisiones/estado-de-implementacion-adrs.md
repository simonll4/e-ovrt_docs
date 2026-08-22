# ADRs — Estado de implementación (cierre de trazabilidad)

- **Fecha:** 2026-07-18 · **última actualización:** 2026-08-18
- **Propósito:** cerrar el loop **decisión → implementación** para cada ADR. Los ADRs
  se escribieron *antes* de implementar y expresan su impacto como trabajo futuro;
  este documento registra, con rutas reales, endpoints y evidencia medida, **cómo
  terminó implementada cada decisión** al 2026-07-18. Los ADRs no se editan (carpeta
  cerrada); este doc es su companion de cierre y se actualiza con causa.
- **Cómo leer:** siglas en el doc 13 (glosario). Para cada ADR: la decisión en una
  frase autocontenida, cómo quedó implementada, la evidencia, y lo pendiente.
  La foto de los tres componentes originales es `operacion/97`; el estado ejecutado de
  distribución está en `operacion/114` y sus banners de cierre del 2026-08-11.

---

## 0. Tabla resumen

| ADR | Decisión (una frase) | Estado de implementación |
|---|---|---|
| 001 | La estrategia de detección del núcleo es **indirecta** (detectar persona+EPP y razonar la ausencia), no prompts de infracción directa | **Implementada como encuadre y cerrada experimentalmente** (✎ 2026-08-06; *decía "pendiente del acta `edir_v1`"*): acta firmada 2026-07-29 (doc 76) y **D1 corrió en los dos niveles** — E-DIR vetada por precisión (0,146 < 0,5) |
| 002 | El patrón se evalúa **por escena (G0)**, sin identidad de personas; el modo por-sujeto (G1) es capacidad operativa medida (adenda 08-04 + ADR-015) | **G0 implementado y verificado** (gate F1=1.0); **G1 implementado y medido** (✎ 2026-08-06; *decía "no portado (deuda)"*): decorador de fuente en el control-plane, F1 0,930 en 34 clips — ver §1 (RESUELTO 2026-08-04) |
| 003 | El acople live media→control es **bus ZeroMQ PUB/SUB + msgpack**, broker diferido | **Implementado y demostrado** (paridad byte-idéntica replay↔stream) |
| 004 | La corrida experimental es un **manifiesto paraguas** con `experiment_id` propagado, orquestada por un runner HTTP | **Implementado** (runner + manifiesto + propagación a ambos planos) |
| 005 | La distribución de alertas se recorta a **un canal MQTT en repo propio** | **Funcionalmente implementado** (✎ 2026-08-12): seis criterios de spec 45 verificados, incluidos DBE/EBE, MQTT QoS 1 contra broker real y `report.json`. ✎ 2026-08-14: los pendientes del 08-12 (vista de outcomes en la **webconsole**, **orquestación** integral y versionar el repo) se cerraron el 2026-08-13 — `13c801e`, `42529e2`, y repo con `c9903cc`/`1e6d8fa` |
| 006 | El reporte consolidado junta ambos planos por `experiment_id` y **cada métrica declara su aplicabilidad** con causa | **Implementado** (report.json/md + estados en todos los evaluadores) |
| 007 | En vivo, la corrida del control-plane es **1:1** con el run del media-plane y cierra por `run_finished` | **Implementado y verificado E2E** |
| 008 | El control-plane se expone como **servicio HTTP mínimo** (:8081) | **Implementado y superado** (11 endpoints vs los 3 decididos) |
| 009 | La config experimental se **centraliza** en experimental-setup y la **webconsole es la superficie de gestión primaria** | **Implementación incompleta** [Enmienda 2026-08-14]: la UI está rediseñada, pero el historial durable y la promoción `runs/`→`results/` quedaron diferidos (doc 115 §2.2, frentes C/D, D-115.2). La calificación histórica “superado” describía la UI, no el ciclo de evidencia. |
| 010 | Se ejecuta **la plataforma primero**, la evaluación después; el clip bench se dispara al cierre del spec 44 | **Cumplida** (orden 40→41→42→44 ejecutado; tooling del 43 completo) |
| 011 | El motor **emite en cada confirmación**; cooldown y supresión son política de notificación (módulo de distribución) | **Implementado en ambos lados de la frontera**: el motor emite todo; el distribuidor aplica cooldown por `(condition_id, source_id)` y lo registra |
| 012 | Bajo G0 la memoria de cobertura EPP **se ignora con causa declarada** (la histéresis subsume el parpadeo) | **Implementado y FALSACIÓN SUPERADA** (los dos tests condición-de-merge pasaron) |
| 013 | La plataforma **detecta la temporalidad de la fuente** y declara sola la no-aplicabilidad de métricas temporales | **Implementado con evidencia medida** (137 eventos / 0 alertas sobre imágenes) |
| 014 | Los resultados de un run global se **consolidan con híbrido selectivo** (liviano copiado, crudo referenciado) | **Implementación parcial** [Enmienda 2026-08-14]: consolidación y reporte están ejercitados; el sellado opt-in, el índice durable y la promoción trazable a `results/` siguen diferidos (doc 115 §4, frentes C/D, D-115.2). |
| **015** | **El alcance creció** en E-03/E-07/E-13 y se registra; **no se agrega ninguna capacidad más**; MQTT queda declarada NO implementada | **Aceptada (usuario, 2026-08-05) y APLICADA al doc 10** (ítem 10 + filas E-03/E-04/E-07/E-13). No es un ADR de implementación: es el cierre del registro de alcance. **R-13 y R-21 desbloqueados**. ✎ **2026-08-10: §2b/§2c/§6 DEROGADOS por ADR-016**; §2a/§3/§4/§5 vigentes (la lista L1–L8 se sigue citando desde §3) |
| **016** | **Reapertura acotada de la distribución** para cerrar la arquitectura: recorte exacto de ADR-005, E-06 sigue excluida, nada más se reabre (✎ 2026-08-11: **E-04 sale del freno por ADR-017**; el freno sigue para EN-3/E-10/E-06/CR nuevas) | **Aceptada y materializada**: módulo funcional, reporte integrado y broker MQTT real verificado. La vista de webconsole y la orquestación siguen abiertas; el repo aún no tiene commits |
| **017** | **El fine-tuning (E-04) se ejerce como jornada experimental completa** (escalera T1→T2/T3 con go/no-go pre-registrados, Mendieta, eval contra `bench_v3`), y el encuadre del informe pasa a **rama experimental condicionada por datos y protocolo** — la causa temporal queda prohibida | **Aceptada; implementación en curso, NO-GO T1 full.** F-100.1, freeze/smoke, dual gate, serving real y procedencia T-FT-023 están cerrados (snapshot `639e60df…`). ✎ **2026-08-15: D-FT-08/T-FT-005, D-FT-12 y D-FT-13 firmadas por el usuario, y T-FT-031/T-FT-032 CERRADAS la misma jornada** (doc 120: comando de evaluación congelado + enforcement canónico v2 + **baseline YOLOE-26s one-shot**, `bare_head` AP50 0,000 / recall CR-01 agregado 0,0002). **Las 7 gates del full-authorization están cerradas**; restan emitirla y el `RUN` manual (T-FT-043). Cero full; **no bloquea el informe**. ✎ **2026-08-15 (noche): T-FT-043 CERRADA — autorización emitida y verificada (7 gates) y `RUN` encolado como job `1167640`.** Abierto: la corrida y su evaluación (T-FT-050→052); sin cifra del modelo ajustado. ✎ **2026-08-17: JORNADA CERRADA — T-FT-044/050/051/052 `done`, veredicto D-FT-12 = NO-GO** (doc 123): el job corrió (`COMPLETED`, 10/10 épocas), el checkpoint se promovió por hash y se evaluó una sola vez — `bare_head` AP50 **0,0000 → 0,0455**, recall CR-01 **0,0002 → 0,2089**, pero faltaron **0,0045** al umbral de ganancia y `person` cayó **−11,62 %** (tope 10 %). Checkpoint **no adoptado**. **ADR-017 pasa de "implementación en curso" a EJERCIDO Y CERRADO en su tramo T1**; ✎ misma fecha, la escalera de `contingencia/20` §6 se aplicó: **T2/T3 NO habilitados** (T1 sin ganancia exigible) — rama cerrada con evidencia, **trabajo futuro con causa técnica, no temporal**. ✎ más tarde ese día, **enmienda D-FT-14** (vía D-FT-03): **T2 reabierto como tier exploratorio** con pre-registración propia (D-FT-15 a firmar antes del RUN), T1 intacto, T2 = último brazo contra `bench_v3`; **T3 sigue cerrado**. ✎ **2026-08-21: T2 CERRADO — D-FT-15 = NO-GO; LA JORNADA E-04 ESTÁ COMPLETA EN SUS TRES TIERS** (doc 127): gain PASA (`bare_head` 0 → 0,0909) pero retención in-domain FALLA ×4 (mAP50 −43,4 %) y retención OV FALLA (COCO −71,3 %); las 3 expectativas pre-registradas confirmadas. Secuencia declarable: `1167864` submuestreado (`optimizer=auto`) ⇒ D-FT-16 pre-resultado ⇒ `1167982` (SGD explícito) colapsó en entrenamiento (early stop 16/60, best=ep1). **F-127.1: el fallo de T1 es estructural (datos), no de capacidad** — curva de 3 puntos completa. Checkpoint no adoptado |

| **018** | **El tercer módulo se acopla por subproceso local, no por servicio HTTP**: el runner del BFF lanza `eovrt-distribute` como proceso hijo (el repo de distribución es CLI, sin FastAPI/uvicorn); el dato sigue viajando por el bus (`:5558`), lo nuevo es el control del ciclo de vida | **Aceptada (usuario, 2026-08-15) y ya implementada** — documenta código verificado, no agrega capacidad. Requisito de despliegue vinculante: la consola dockerizada exige `EOVRT_DISTRIBUTION_EXECUTABLE`. Preflight de binario + drenaje de `stderr` con cap de 1 MiB son propios de este patrón. ✎ **2026-08-18** (*esta fila decía "el repo de distribución es CLI, sin FastAPI/uvicorn"*): eso quedó **superado por ADR-019** — el repo SÍ expone servicio HTTP además del CLI (ver fila 019). Este patrón de subproceso **sigue vigente y sigue siendo el default** del runner de la webconsole; ADR-018 no queda derogada ⛔ **✎ 2026-08-18: DEROGADA por ADR-020** — el subproceso dejó de ser patrón de acople y bajó a fallback operativo; esta fila queda como registro histórico y **no se cita como arquitectura vigente** |
| **019** | **El distribuidor suma un servicio HTTP** (`eovrt-distribute serve`, FastAPI/uvicorn en `:8082`), espejo del control-plane, para ser una unidad desplegable propia; no deroga ADR-018 — el subproceso local sigue siendo el camino default del runner del BFF | **Aceptada (usuario, 2026-08-17) e implementada y verificada (2026-08-18)**, incluida una corrida en vivo con cámara real: `POST /api/runs` (201 + id, 409 si hay una activa), `GET /api/runs/{id}` (sirve el mismo `distribution_summary.json` del CLI), `POST /api/runs/{id}/cancel` (parada cooperativa vía `ZmqSource.request_stop()`), `GET /healthz`\/`readyz`\/`config` (spec 45 §9.2/9.3). El runner del BFF es cliente HTTP opcional vía `EOVRT_CONSOLE_DISTRIBUTION_TRANSPORT=http`, con preflight que sondea `/healthz` en vez de exigir el binario local en ese camino. Containerización (Dockerfile, `docker-compose.yml`) queda diferida con causa (ADR-019 §4), no es deuda de esta fila ✎ **2026-08-18: el default pasó a HTTP por ADR-020**; ya no es opt-in — el opt-in ahora es el fallback por subproceso |
| **020** | **HTTP es el acople de la distribución; el subproceso baja a fallback operativo** y deja de ser patrón. Deroga ADR-018 | **Aceptada (usuario, 2026-08-18) e implementada**: el runner del BFF habla por HTTP **por default**; `EOVRT_CONSOLE_DISTRIBUTION_TRANSPORT=subprocess` conserva el camino viejo como red de seguridad (sigue implementado y probado). Preflight: sondea `GET /healthz` del servicio por default; el chequeo de binario local sólo corre en el fallback. **Consecuencia para el informe: DOS patrones de acople** — (a) HTTP config-driven en los tres módulos (`:8080`/`:8081`/`:8082`), (b) bus ZeroMQ (`:5557` detecciones, `:5558` alertas). El fallback **no se describe**: es operación, no arquitectura. Costo declarado: la webconsole exige el servicio arriba cuando la distribución está habilitada |

> **✎ 2026-08-15 — la nota del 2026-08-14 sobre el patrón BFF-subprocess quedó
> promovida a [ADR-018](adr-018-acople-bff-subproceso-distribucion.md)**, firmada por el
> usuario. *Decía: "Si el patrón se consolida merece ADR propia; queda como propuesta
> abierta, no ejercida."* El informe debe describir **tres** patrones de acople, no dos.
>
> ⛔ **✎ 2026-08-18 — la frase anterior quedó superada: son DOS.**
> [ADR-020](adr-020-http-como-unico-acople-de-distribucion.md) derogó a la 018. Tras
> [ADR-019](adr-019-servicio-http-distribucion.md) el distribuidor tiene servicio HTTP
> propio (`:8082`) y la 020 invirtió el default: **HTTP es el acople**, el subproceso bajó
> a **fallback operativo** (`EOVRT_CONSOLE_DISTRIBUTION_TRANSPORT=subprocess`) y dejó de
> ser un patrón. El informe describe **(a)** HTTP config-driven en los **tres** módulos y
> **(b)** bus ZeroMQ. El fallback no se cuenta: es operación, no arquitectura.

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
  `eind_v1` y `edir_v1` quedaron **congelados con acta firmada** (2026-07-29, doc 76,
  sha256 registrados; ✎ *decía "`frozen_pending_review`, espera el acta del
  usuario"*) y los sets E-DIR exploratorios quedaron en `prompts/_archive/`. La bajada operativa completa
  (comparabilidad, calib/test, fusión) es el doc 12.
- **Evidencia:** benchmark de modelos doc 31 (insumo: YOLOE ciego a `bare_head` ⇒
  restringe el espacio de búsqueda de D1); toda la plataforma corre E-IND en los E2E
  de docs 35/37/38/51.
- **Pendiente:** ninguno. (✎ 2026-08-06; *decía "el experimento D1 no se corrió
  (bloqueado por el acta `edir_v1`)" y "`eind_v1` está `frozen_pending_review`"*):
  el acta se firmó el 2026-07-29 (doc 76, ambos sets congelados con sha256) y **D1
  corrió en los dos niveles** — a Nivel A E-IND gana por el criterio pre-registrado
  y a Nivel B E-DIR quedó **vetada por precisión** (0,146 < 0,5, campaña D1 del clip
  bench). El único punto que podía revisar el ADR se ejerció y lo confirmó.

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
- ~~**Pendiente:** G1 no está portado, nadie produce `track_id`, el modo `subject` está
  inerte~~ → **RESUELTO 2026-08-04 por otra vía (adenda del ADR, pendiente de
  ratificación).** El productor de `track_id` se implementó **en el control-plane como
  decorador de fuente** (`sources/tracking.py`, `input.track_persons`, opt-in) en vez
  de portarlo al media-plane. Cubre **DBE y EBE/live** por igual porque decora
  cualquier `MediaEventSource`, y no toca el pipeline congelado del media-plane. El
  modo `subject` dejó de estar inerte: **campaña G1 sobre los 34 clips, F1 0,789 →
  0,930** con las mismas detecciones (doc 89). Verificado que el camino config-driven
  reproduce la campaña **exacto**. La deuda del spec 42 §3 (tracker en el media-plane,
  `track_id` embebido en `detections.jsonl`) queda **abierta pero ya no bloqueante**:
  es una cuestión de dónde vive la identidad, no de si existe.

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
- **Cómo quedó:** **funcionalmente implementado y verificado el 2026-08-11** (doc 114).
  El pipeline source → policy → ledger → channel → records existe en el repo propio;
  soporta replay DBE y fuente ZeroMQ EBE, cooldown, idempotencia, retry, dead-letter y
  MQTT QoS 1. Sobre `v06_c01`, DBE y EBE produjeron el mismo reparto 23 entregadas / 170
  suprimidas; la entrega real recibió 23/23 mensajes. `experimental-setup` integra el
  summary y declara la aplicabilidad de `t_alert-notification` según `latency_mode`.
- **Pendiente:** el cierre de robustez/operación registrado en doc 114. **E-06** (canales
  extra y dashboard propio) sigue excluida y ninguna latencia de smoke se promueve a
  resultado experimental. ✎ **2026-08-14:** la vista de outcomes en la **webconsole**, el
  lanzamiento por la **orquestación** integral y el versionado del repo —los tres listados
  acá como pendientes— quedaron cerrados el 2026-08-13 (`13c801e`, `42529e2`; repo con
  `c9903cc` y `1e6d8fa`).

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

### ADR-015 — Cierre de alcance al final del tramo experimental (✅ Aceptada 2026-08-05, ✎ parcialmente derogada 2026-08-10)

> **✎ 2026-08-10 — ADR-016 deroga §2b, §2c y §6.** Lo que sigue abajo describe el ADR
> como fue aceptado el 08-05. **Sus §2a, §3, §4 y §5 siguen vigentes y ratificados** (la
> tabla del alcance que creció y la lista de límites L1–L8 que reemplaza a R-13). Lo que
> cayó es el cierre de puerta y la declaración de MQTT como no implementada.

- **Decisión:** registrar que el alcance **creció** respecto del doc 10 en E-03 (G1 pasa
  de demostrativa a capacidad operativa medida), E-07 (OAK-D + EN-2, parcial) y E-13
  (E-HYB-or ejecutada y refutada; `hyb_and` no ejecutada con causa); **cerrar la puerta**
  (ninguna capacidad nueva de acá a la defensa) y declarar la distribución MQTT como NO
  implementada, resolviendo el condicional del ADR-005. ✎ **Estas dos últimas cláusulas
  (§2b y §2c) fueron derogadas por ADR-016 el 2026-08-10.**
- **Cómo quedó:** **es el único ADR que no describe implementación** — no toca código ni
  cambia una sola cifra medida. Reordena qué se declara como alcance y qué como límite.
- **Por qué existe:** el doc 95 §5.1 lo pidió como *"recorte final de alcance"* porque los
  docs 91/94 declaraban el tracker/G1 como no implementado. **La premisa se invirtió**: G1
  terminó siendo el mejor resultado del banco (F1 0,930). Cumplir el pedido literal habría
  obligado a esconder ese resultado o declararlo fuera de alcance.
- **Qué desbloquea:** **R-13** (la lista de límites: de sus 8 ítems, 5 estaban resueltos —
  auditados uno por uno en el ADR §3) y **R-21** (la tabla de estado del backlog, que
  afirma "MOT ✗ tracker no implementado" y es falso al cierre: lo excluido son las
  métricas MOT, E-10, no la capacidad).
- **Cerrado:** aceptado por el usuario el **2026-08-05** y **aplicado al doc 10** — su
  encabezado apunta a este ADR, el **ítem 10** de la lista de alcance quedó reescrito y las
  filas **E-03/E-04/E-07/E-13** de la tabla de exclusiones llevan su estado real con
  evidencia. Registro de alcance y resultados ya dicen lo mismo.

## 2. Vista por tema (resuelve la superposición de ADRs)

Para saber **qué rige hoy** cuando varios ADRs tocan lo mismo:

| Tema | Cadena de ADRs | Estado vigente |
|---|---|---|
| **Rol de la webconsole** | 004 ("muestra") → 008 ("cliente de ambos planos") → **009 (rige: superficie de gestión primaria)** | Consola = gestión primaria (configs, prompts, cámaras, runs, experimentos); runner CLI = camino headless con las mismas APIs |
| **Config** | 004 (manifiesto referencia) + **009 (rige: centralizada en experimental-setup)** | Config experimental centralizada, entregada por payload, `effective_config` persistido por cada plano |
| **Artefactos/resultados** | 004 (`experiment_id`) + 006 (reporte) + **014 (rige: layout híbrido selectivo)** | Consolidado liviano + crudos referenciados; reporte con estados de aplicabilidad |
| **Alertas y su política** | **011 (rige: motor emite todo)** + 005/**016** (la política vive en distribución, hoy funcional) | Motor sin supresión; distribuidor con cooldown e idempotencia; `re_alerts` contadas, no penalizadas |
| **Qué mide cada corrida** | 006 (vocabulario de aplicabilidad) + **013 (rige: por temporalidad de fuente)** + 012 (causa específica de G0) | La plataforma declara sola qué aplica, con causa, sin rechazar corridas |

## 3. Condicionales de los ADRs: resolución registrada

| ADR | Condicional que dejaba abierto | Resolución |
|---|---|---|
| 001 | "el cierre definitivo lo da el experimento D1" | ✎ **RESUELTO (corregido 2026-08-05; esta fila decía "sigue abierto")**: el acta se firmó el 2026-07-29 (doc 76 — `edir_v1` `a1278d0c…` y `eind_v1` `7a0126f4…` congelados con sha256) y **D1 corrió en los dos niveles**: Nivel A pasó el gate parcialmente (doc 83) y **Nivel B descartó E-DIR por veto de precisión** (0,146 < 0,5 — doc 85). El encuadre E-IND queda confirmado con número, no por defecto |
| 006 | dos opciones para relojes two-node | Resuelto: **declarativa** (`not_interpretable/cross_node_monotonic_clock`, doc 39) |
| 007 | ventanas de evaluación propias "trabajo futuro" | No hicieron falta: la evaluación temporal v2 (doc 52) cubre el caso |
| 005 | "¿MQTT sí o no?" (canal de distribución, spec 45) | ✎ **RESUELTO: SÍ e implementado** (ADR-016; verificación 2026-08-11, doc 114). E-06 sigue excluida. Quedan la vista de webconsole, la orquestación y versionar el repo; no bloquea la redacción |
| 012 | "sujeta a falsación por test" | **Falsación superada** (doc 34); la reversión no se activó |
| 002/008/009 | recortes "si la agenda aprieta" (G1-demo, cáscara HTTP, mejora UX) | Ninguno se ejerció; al revés: servicio y UX se ampliaron. (✎ 2026-08-06; *decía "G1 sigue sin portar pero por orden de prioridad"*): G1 terminó **implementada y medida** — decorador en el control-plane, F1 0,930 en 34 clips (adenda ADR-002 ratificada + ADR-015 E-03) |
