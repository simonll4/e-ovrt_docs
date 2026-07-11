# Reporte de estado del tramo plataforma — hecho y pendiente

> **✎ Actualización 2026-07-11 (docs 51–54):** este reporte es el snapshot del
> 2026-07-10; el tablero del §1 quedó superado. Desde entonces: **5b** (doc 51),
> **`evaluate-alerts` v2** (doc 52), **spec 44 completo** backend+frontend (doc 53)
> — hechos, commiteados y **pusheados** — y el **video-gt-lab** (doc 54): el tooling
> del spec 43 implementado + contrato GT↔evaluador reparado, **sin commitear** en
> datasets/media-plane/control-plane. El §7 (inventario de no-commiteado) ya no
> refleja el estado real: lo de docs 37–39/51–53 se pusheó; lo vigente sin commitear
> es lo del doc 54. Pendiente implementable: ítems del doc 54 §5 (SDR/TTFD,
> promoción al banco, `clip_id` en manifiesto) y spec 45 (para lo último, decisión
> del usuario). El dataset con GT (ejecución del spec 43) sigue **pendiente** —
> checklist en doc 54 §5.

- **Fecha:** 2026-07-10
- **Qué es:** el reporte consolidado de todo el trabajo del tramo plataforma (ADR-010,
  orden operativo del handoff 36 derivado de spec 41 §10) al cierre de la sesión del
  2026-07-10: qué se construyó, con qué evidencia, qué defectos atrapó la revisión, y
  qué falta — en orden. **Reemplaza al doc 36 como punto de entrada para implementar.**
- **Numeración:** la serie 30- de `operacion/` se llenó (30–39) y la 40- pertenece a
  `specs/`; operación continúa en la serie **50-** (registrado en el índice).
- **Regla de oro (sin cambios):** las decisiones están cerradas (ADR-001…014). Si algo
  parece ambiguo, la respuesta está en un ADR o un spec — no re-litigar, buscar.
- **Estado de commits: NADA COMMITEADO.** Los tres repos tienen todo el trabajo en el
  working tree/índice (§7). Los HEAD siguen en `docs@cb92c91`,
  `e-ovrt_control-plane@46c855b`, `e-ovrt_media-plane@e12b56a`.

## 1. Tablero del tramo

Orden operativo del handoff 36 §3 (spec 41 §10 con los evaluadores D1 movidos al final
porque los bloquea el acta `edir_v1`, que es del usuario):

| # | Ítem | Estado | Evidencia |
|---|---|---|---|
| 1 | G0 — granularidad de escena | ✅ **commiteado** (2026-07-10, sesión anterior) | docs 34, 35 |
| 2 | `MediaEventSource` (jsonl/memory) | ✅ hecho, **sin commitear** | doc 37 |
| 3 | Bus ZeroMQ + runtime live 1:1 | ✅ hecho, **sin commitear** | doc 37 |
| 4 | Servicio mínimo control-plane :8081 | ✅ hecho, **sin commitear** | doc 38 |
| 5a | Instrumentación `t_capture→alert` — mitad **media-plane** | ✅ hecho, **sin commitear** | doc 39 |
| 5b | Instrumentación — mitad **control-plane** + pattern set `cr01_cr02_v2` + publisher de alertas | ✅ hecho, **sin commitear** (2026-07-11) | doc 51 |
| — | `evaluate-alerts` v2 (spec 41 §8.7) | ⬅️ **LO QUE SIGUE** (plan hermano; extiende `evaluation/temporal.py`) | — |
| 6 | experimental-setup (spec 44): runner, configs por experimento, **consolidación de artefactos (ADR-014)**, `report.json`, webconsole cliente de ambos planos | pendiente (consume el `join` y el publisher de 5b) | — |
| 7 | Evaluadores D1 + fusión E-HYB (spec 41 §6) | pendiente — **bloqueado por el acta `edir_v1`** (doc 12 §2.2) | — |
| — | `evaluate-alerts` v2 (spec 41 §8.7) | pendiente (va con 5b o inmediatamente después) | — |
| — | spec 45 (distribución) y spec 43 (clip bench) | según ADR-010: 45 en paralelo tras el 44; 43 al cierre del 44 | — |

## 2. Qué se construyó (por tramo)

### 2.1 Ítems 2–3 — bus media→control y runtime live (doc 37)

Los dos planos, que solo se acoplaban por archivo (DBE/replay), ahora se acoplan **en
vivo** por un bus ZeroMQ PUB/SUB con envelope msgpack `bus.envelope.v1`.

- **Control-plane:** interfaz `MediaEventSource` (iterador `event | error | END`) con
  `JsonlSource`, `MemorySource` y `BusSource` (SUB con detección de huecos de `seq`,
  cierre por `run.lifecycle.v1/run_finished`, fallback por polling, drenaje acotado,
  parada cooperativa); el bucle del motor extraído a `runtime/core.py:execute_over_source`
  (una sola ruta para replay y live); `runtime/live.py` + CLI `live`. `RunSummary` gana
  `media_run_id`, `experiment_id`, `source`, `bus_dropped_events` (aditivos).
- **Media-plane:** `transport/bus.py` (`BusPublisher` sobre XPUB — notifica las
  suscripciones, lo que permite `wait_for_subscriber` en vez de dormir a ciegas — con
  `seq` monótono desde 0 que **se consume aunque el envío se descarte**) y
  `service/bus_writer.py` (`BusPublishingArtifactWriter`: persiste primero, publica
  después; el `payload` es **byte-idéntico a la línea del JSONL**; `run_finished` sale
  pase lo que pase). Config `bus: {enabled, endpoint, hwm, wait_for_subscriber_ms}`
  apagada por default, aceptada también en el `POST /api/runs`.

### 2.2 Ítem 4 — servicio mínimo del control-plane (doc 38)

El control-plane dejó de ser solo CLI: FastAPI en :8081 (`eovrt-control serve`), mismo
patrón que el media-plane, **un run activo por vez**.

| Método | Ruta | Éxito | Errores |
|---|---|---|---|
| `POST` | `/api/runs` (`mode: replay\|live`, config por payload o referencia, `experiment_id`) | 201 `{control_run_id}` | 409 + `active_run_id`; 422 config inválida |
| `GET` | `/api/runs/current` | 200 + `progress` + `subscribed` | 404 |
| `GET` | `/api/runs/{id}` | 200 (+ `summary`, `degraded`, `degradation_causes`) | 404 |
| `GET` | `/api/runs/{id}/alerts` | 200 (fuente de la vista de la webconsole) | 404 |
| `GET` | `/api/config` | 200 `effective_config` | 404 |
| `GET` | `/healthz`, `/readyz` | 200 | — |

La invariante que da sentido al servicio: **el 201 de un `POST mode: live` implica que
el `BusSource` ya está suscripto** (se construye dentro del handler, bajo el lock, antes
de arrancar el hilo). El orquestador dispara el media-plane recién después. La CLI se
conserva completa (camino offline y fallback del orden de sacrificio, ADR-008).

### 2.3 Ítem 5a — instrumentación G2A del media-plane (doc 39)

Los insumos de `t_capture→alert` que aporta el plano de medios (spec 40 §5.2.4):

- **Instante de captura** (`capture_monotonic_ns`, `capture_wallclock_ms`) estampado al
  **leer** la unidad (via `default_factory` en `VisualUnit` — ninguna fuente puede
  olvidarse) y propagado por el canal y el wire de two-node.
- **`source_clock` por fuente** (`wallclock` RTSP / `media` archivo de video / `none`
  imágenes), que decide la aplicabilidad de la métrica aguas abajo (spec 40 §5.2.3).
- **`g2a_ms` por unidad** en `metrics.jsonl` (compuesta captura → resultado algorítmico,
  cerrada al terminar la inferencia), con `unit_id` como clave de join con las alertas.
- **Bloque `g2a` en el summary**: P50/P95/P99 con warm-up excluido y declarado
  (`warmup_units`), contra el presupuesto 50–250 ms.
- **Honestidad en two-node**: los relojes monotónicos de dos hosts no se restan;
  `g2a_ms` vale `null` por fila y el bloque sale
  `not_interpretable / cross_node_monotonic_clock`. Nunca se publica un número sin
  sentido (ADR-006).

### 2.4 Correcciones que no son código

- **Mito desmentido (medido):** el doc 37 afirmaba que la purga de `self._state` del
  motor "pasó de teórica a real" con el live. **Falso.** Bajo `granularity: scene` la
  clave es `(pattern_id, "pattern_id:source_id")`: el estado crece con `source_id`
  **distintos**, no con el tiempo (5000 frames de una fuente única ⇒ 2 entradas;
  RTSP/video emiten `source_id` constante). La fuga real llega con `granularity:
  subject` + `track_id`, que nadie produce aún. Corregido en doc 37 §7.2, handoff 36 y
  la memoria de sesión.
- Docs 37/38/39 escritos con números medidos; handoff 36 actualizado; `CLAUDE.md` del
  workspace y del media-plane al día; este reporte como nuevo punto de entrada.

## 3. Verificación (gates, mutaciones, E2E)

Regla aplicada en todo el tramo: **un gate que no puede fallar no es un gate** — cada
gate se sometió a mutación antes de darlo por bueno.

| Gate | Qué prueba | Verificación por mutación |
|---|---|---|
| Paridad replay↔stream (`test_bus_parity.py`) | mismo fixture por archivo y por bus ⇒ artefactos idénticos módulo `control_run_id`/`alert_id` | saltear 1 evento ⇒ **falla**; bbox corrido 1 px con contadores idénticos ⇒ **falla la comparación de contenido**; dropout de 1 frame ⇒ pasa (la histéresis `resolve_after_frames: 2` lo absorbe — correcto) |
| Orden de suscripción (`test_service_live.py`) | el 201 implica `subscribed: true` (aserción de **orden**, no de timing: PUB/SUB es asincrónico) | mover la suscripción al hilo de fondo ⇒ **falla**. El primer intento de gate era vacuo (§4) y se reemplazó |
| Insumos G2A (`test_g2a_gate.py` + `test_capture_timestamps.py`) | los 3 campos por unidad; G2A ≥ latencia de inferencia; `source_clock` correcto | `default=0` ⇒ **falla el gate** (hubo que endurecerlo); borrar el copiado en `normalize_spatial` ⇒ la caza el test unitario con `sleep(20ms)` (el gate solo no la distingue en mock — documentado) |

Corridas end-to-end reales (evidencia en `operacion/datos/`):

| Corrida | Números | Evidencia |
|---|---|---|
| **Live por bus** (servicio media-plane mock, video real, 40 unidades) | 40/40 unidades, 0 perdidas, cierre solo por `run_finished`, 15 `pattern_events`, 6 alertas; **el mismo run releído offline produce artefactos byte-idénticos** (re-evaluabilidad de ADR-003 demostrada) | `datos/37-*` |
| **Dos servicios hablándose** (orden del spec 44: control-plane primero) | 201 con `subscribed: true` **antes** de disparar el media-plane; 30/30 unidades, 0 perdidas; 409 verificado con `active_run_id`; cierre 1:1; alertas y config por sus endpoints; `experiment_id` de punta a punta | `datos/38-*` |
| **G2A sobre video** (20 unidades) | `source_clock: media`; `g2a: computed`, P50 14.7 ms, P95 31.8 ms, dentro del presupuesto 50–250 ms; 20/20 filas con los tres campos | `datos/39-*` |

Además: fuzz de 10 mensajes de bus malformados ⇒ 10 `ErrorEvent`, 0 excepciones; el
contrato de errores del servicio comprobado a mano (6 entradas inválidas del cliente ⇒
422; bug interno ⇒ 500); parada cooperativa 5/5 corridas sin SIGABRT; path traversal
con 7 nombres hostiles ⇒ 0 escapes de `runs_dir`.

## 4. Defectos que la revisión adversarial atrapó

Los planes traían código de referencia con defectos reales; el proceso de review por
tarea (implementador → revisor → fix → re-review, todos con reproducción) los cazó.
Detalle completo en doc 37 §6 (9), doc 38 §6 (8), doc 39 §6 (5). Los que valen como
lección del dominio:

**Seguridad / disponibilidad:**
1. **Path traversal desde el payload** — `new_control_run_id` devolvía el `run.id` del
   usuario sin validar; `"../../etc/evil"` escapaba de `runs_dir`. Ahora la validez del
   id es postcondición de la función.
2. **Run activo fantasma permanente** — un `BaseException` en el hilo dejaba el slot
   tomado y todo `POST` posterior daba 409 para siempre. Limpieza en `finally`.
3. **`_check_seq` retrocedía el contador** ante un `seq` duplicado, inflando
   `dropped_events` — y ese hueco es la **única** señal de pérdida del sistema (un
   PUB/XPUB dropea en silencio al HWM: medido, 2000 envíos, 0 EAGAIN, 3 entregados).
4. **Config inválida del cliente respondía 500** (endpoint de bus malformado, YAML
   corrupto) en vez de 422 — normalizado en la raíz sin ensanchar el `except` del router.
5. **Reusar un `run.id`** reportaba una corrida fallida como `succeeded` con los
   artefactos truncados de otra corrida debajo — ahora se rechaza (422) sin borrar nada.
6. **Cuatro caminos por los que un mensaje malformado del bus mataba la corrida** en
   vez de salir como `ErrorEvent`.
7. **`run_finished` no garantizado** — la construcción del publicador fuera del `try`,
   `run_node_b` sin `finally` externo, `close()` sin protección: tres rondas de fix
   hasta que "sale pase lo que pase" fue verdad.

**Gates y tests vacuos (los instructivos):**
8. El gate "el 201 implica suscripto" **no podía fallar**: el helper de test absorbía
   cualquier retraso (hasta un `sleep(2 s)` inyectado). La invariante es de *orden*, no
   de timing — se probó estructuralmente.
9. El gate G2A no cazaba `default=0` (`monotonic_ns() − 0` sigue siendo positivo).
10. Un test de `limit=-1` pasaba con y sin el fix (`[x][:-1] == []` con un solo elemento).
11. **La byte-compatibilidad payload↔JSONL no tenía ningún test que la sostuviera** (el
    que existía recomputaba la expresión y se comparaba consigo mismo). Ahora hay uno
    e2e contra el archivo real, probado mutando el sink.

**Otros:** `exclude_none=True` borraba `g2a_ms: null` de las filas (la clave desaparecía
en vez de decir "no medible"); `SUBSCRIBE ""` metido en producción para tapar un test
roto (diagnóstico probado falso: era slow-joiner del helper — se revirtió); `_drain()`
sin cota que anulaba el cierre por polling; `send_failures` que miente por diseño de
PUB/XPUB (documentado, no "arreglado" mal); fuga de socket en caminos de error de
`__init__`; un comentario que justificaba un import perezoso con un ciclo de imports
**inexistente** (comprobado y corregido).

## 5. Reglas duras del dominio (verificadas, no negociables)

1. **Orden de disparo live:** `POST :8081/api/runs` (`mode: live`) **primero** — su 201
   implica suscripción — y `POST :8080/api/runs` con `bus.enabled: true` **después**.
   PUB/SUB no retiene lo publicado antes de la suscripción; el hueco inicial de `seq`
   se cuenta como `bus_dropped_events` y degrada la corrida (no se silencia).
2. **Nunca cerrar un socket ZeroMQ desde otro hilo** mientras el iterador está en
   `recv_multipart`: libzmq aborta el proceso con SIGABRT (`session_base.cpp`). Las
   fuentes exponen `request_stop()` (parada cooperativa); el socket lo cierra el hilo
   que lo creó.
3. **Un PUB/XPUB dropea en silencio al llenarse el HWM** (nunca EAGAIN): el hueco de
   `seq` del lado del consumidor es la única señal de pérdida del sistema entero.
4. **Los relojes monotónicos de dos hosts no se restan** (origen arbitrario por
   máquina): en two-node, G2A es `not_interpretable / cross_node_monotonic_clock` y
   `g2a_ms` es `null` por fila.
5. **El JSONL es la verdad; el bus solo transporta.** Persiste primero, publica después;
   toda corrida live es re-evaluable offline con artefactos idénticos (demostrado).
6. **Los dos repos no se importan entre sí**: el envelope está duplicado a propósito y
   el contrato de wire se pinea con tests en ambos lados (byte-compatibilidad incluida).
7. **Nunca publicar un número que no significa nada**: estados de aplicabilidad
   ADR-006 (`computed | applicable_not_computed | not_applicable | not_interpretable`)
   con causa, en vez de ceros o basura.
8. **Contratos siempre aditivos, sin bump de `schema_version`.**
9. **`default_factory`, no `default=f()`** para timestamps por instancia — y si un
   modelo aguas abajo se reconstruye (p.ej. `normalize_spatial`), el copiado explícito
   necesita su propio test: el re-estampado es **silencioso**.
10. **Nunca commitear sin pedido explícito del usuario en ese turno**; nada en GitHub;
    nunca `Co-Authored-By`.

## 6. Suites y lint (medidos)

| Repo | Inicio de sesión | Ahora | Lint |
|---|---|---|---|
| `e-ovrt_control-plane` (`pytest -q --ignore=tests/labs`) | 57 passed | **154 passed** | `ruff` limpio |
| `e-ovrt_media-plane` (`pytest -q`) | 440 passed | **480 passed** | `ruff` limpio |

Progresión por tramo: plan 2 llevó CP 57→89 y MP 440→456; el servicio llevó CP 89→154;
G2A llevó MP 456→480. `tests/labs/` del control-plane sigue rojo por `numpy` ausente
(conocido, no bloqueante): correr siempre con `--ignore=tests/labs`.

## 7. Estado de los repos — inventario de lo NO commiteado

**`docs` (HEAD `cb92c91`)** — 14 rutas:
`operacion/36` (modificado: banners de superado + tablero), `operacion/37`, `38`, `39` y
`50` (nuevos), `00-indice.md` (actualizado: docs 37–50, serie 50-, punto de entrada,
recordatorio de git corregido), y 8 archivos de evidencia en `operacion/datos/`
(`37-*` ×4, `38-*` ×3, `39-*` ×1).

**`e-ovrt_control-plane` (HEAD `46c855b`, rama `feature/control-service`)** — 35 rutas:

- *Fuentes:* `sources/{base,jsonl,memory,bus}.py` (nuevos), `sources/media_jsonl.py`
  (alias de compat).
- *Runtime:* `runtime/{core,live}.py` (nuevos), `runtime/replay.py` (delegador),
  `contracts/metrics.py` (campos aditivos del summary), `config.py` (`input.type: bus`,
  `experiment_id`, `load_replay_config_data`).
- *Servicio:* `service/{__init__,app,settings,run_ids,run_request,run_manager}.py` y
  `service/routers/{__init__,health,runs,config}.py` (todos nuevos), `cli.py` (`live`,
  `serve`), `pyproject.toml` (deps `pyzmq`, `msgpack`, `fastapi`, `uvicorn`, `httpx`).
- *Config:* `configs/live_ebe_cr01_cr02.yaml` (nueva).
- *Tests (10 archivos):* `test_sources`, `test_bus_source`, `test_bus_parity` (gate),
  `test_live`, `test_runtime_progress`, `test_service_request`, `test_run_manager`,
  `test_service_api`, `test_service_live` (gate), `test_replay` (ampliado).
- *Planes:* `docs/superpowers/plans/2026-07-10-{plan2-bus-y-runtime-live,servicio-minimo-control-plane}.md`.

**`e-ovrt_media-plane` (HEAD `e12b56a`, rama `feature/inference-service`)** — 30 rutas:

- *Bus:* `transport/bus.py`, `service/bus_writer.py` (nuevos), `runtime/pipeline.py` y
  `runtime/two_node.py` (cableado + `run_finished` garantizado),
  `service/run_request.py` (`BusSpec`), `config/schemas.py` (`BusConfig`,
  `warmup_units`).
- *G2A:* `contracts/{visual_unit,normalized_unit,metrics,events}.py`,
  `preprocessing/normalizer.py`, `transport/serialization.py`, `sources/*.py`
  (`SOURCE_CLOCK`), `metrics/g2a.py` (nuevo), `runtime/run_context.py`,
  `sinks/{jsonl_sink,run_artifact_writer}.py`.
- *Tests (7 archivos):* `test_bus_publisher`, `test_bus_writer`,
  `test_capture_timestamps`, `test_g2a_metric`, `test_g2a_summary`, `test_g2a_gate`
  (gate), `test_two_node` (ampliado).
- *Docs:* `CLAUDE.md` (bus + instrumentación),
  `docs/superpowers/plans/2026-07-10-instrumentacion-g2a-y-captura.md`.

> Los tres planes ejecutados llevan un banner que advierte **no copiar su código de
> referencia verbatim**: los defectos que traían están corregidos solo en el working
> tree (docs 37 §6, 38 §6, 39 §6).

## 8. Lo que falta

### 8.1 Siguiente paso inmediato — ítem 5b (control-plane)

Es lo que convierte los insumos del doc 39 en la métrica. Alcance (spec 41 §7–§8,
spec 40 §5.2.4/§5.4):

1. **`ts_receive_ms`** por unidad en `BusSource` → `metrics.jsonl` del control-plane.
2. **Hitos de primera evidencia por episodio**: `first_evidence_ms`,
   `first_evidence_frame_index` y **`first_evidence_unit_id`** (obligatorio: es la
   clave de join con las métricas del media-plane) en `PatternStateChanged` y
   `AlertEvent`. El motor ya guarda `first_hit_timestamp_ms` en `PatternRuntimeState`;
   hay que extenderlo con el `unit_id` y exponerlo.
3. **`alert_registered_ms`** (instante monotónico de escritura del `AlertEvent`).
4. **`experiment_id`** en los eventos (`PatternStateChanged`, `AlertEvent`,
   `ControlMetricSample`) — hoy solo está en el summary.
5. **Percentiles P50/P95/P99 de `processing_ms`** (hoy solo promedio) y **TTFA
   interna** en el summary (etiquetada diagnóstico).
6. **Pattern set `cr01_cr02_v2` oficial** (spec 41 §7) — la desalineación más
   importante con el informe: partir de `cr01_cr02_field_v1`; PR-01/CR-01 severidad
   **high**, `confirm_after_ms: 4000`, resolve 2000; PR-02/CR-02 severidad medium,
   `confirm_after_ms: 7000`, resolve 3000; `granularity: scene`; **sin cooldown**
   (ADR-011: el motor emite en cada confirmación, la supresión es de distribución);
   **sin memoria de cobertura** (ADR-012: no aplica bajo escena). La `field_v1` actual
   confirma a 1000 ms — fuera de las bandas del informe (PR-01 3–5 s, PR-02 5–10 s).
7. **Publisher de alertas al bus** `control.alert.v1.<control_run_id>` (spec 41 §8.6):
   mismo envelope y primitivas que el bus de detecciones; habilitado por config; el
   JSONL sigue siendo la verdad. Es el insumo del repo de distribución (spec 45).
8. **El join `t_capture→alert`** de punta a punta, con su estado de aplicabilidad por
   fuente (`computed` en RTSP; `not_interpretable / dbe_media_time` en video;
   `not_applicable / non_temporal_source` en imágenes) y verificación e2e real.

Luego (o dentro del mismo plan si el tamaño lo permite): **`evaluate-alerts` v2**
(spec 41 §8.7: consume `clip_gt.v2`, evaluación a nivel episodio, `re_alerts` no son
FP, estados de aplicabilidad).

### 8.2 Después, en orden

- **Ítem 6 — experimental-setup (spec 44):** estructura de configs por experimento
  (ADR-009), runner que orquesta los dos servicios por HTTP **en el orden correcto**
  (control-plane primero), manifiesto paraguas con `experiment_id` (ADR-004),
  **consolidación de artefactos por experimento (ADR-014, ver más abajo)**,
  `report.json`/`report.md` consolidado (mapear contra la Tabla D.6, métricas con
  estados de aplicabilidad — las que exigen GT figuran `not_applicable /
  no_ground_truth`, no se omiten), y la webconsole como cliente de ambos planos
  (segundo `RunBackend` → :8081; vista de alertas leyendo `GET /api/runs/{id}/alerts`).

  **Layout de resultados (ADR-014, decidido 2026-07-10 — hoy la webconsole es un BFF
  stateless sin nada de esto).** Dos clases de corrida, dos destinos:
  - **Run global (experimento, con `experiment_id`)** — lanzado desde la webconsole o el
    runner, involucra ≥ 2 planos. Sus resultados se **consolidan** en
    `experimental-setup/runs/<experiment_id>/` (git-ignored), con **híbrido selectivo**:
    copia lo liviano y decisivo (manifiesto efectivo, `effective_config` de cada plano,
    `summary.json`, `metrics.jsonl`, `alerts.jsonl`, `pattern_events.jsonl`, `report`) y
    **referencia por `run_id`** los `detections.jsonl` pesados, que quedan en el `runs/`
    del plano como fuente de verdad (DA-03). Es la config + los resultados de la
    plataforma centralizados en un lugar ordenado por `experiment_id`, sin duplicar los
    GB crudos. Un "sellado" opt-in materializa los crudos para archivado permanente
    (campañas R1–R4, D1).
  - **Run de test sobre un solo módulo (corrida suelta, sin `experiment_id`)** — sobre un
    solo plano, se configura y se lee en su propio repo, cae en el `runs/` **local** de
    ese plano y **no se consolida** (diagnóstico/smoke; spec 44 §5.2). Ninguna ceremonia
    de experimento para probar un módulo aislado.

  El detalle (layout completo, fuente de verdad, sellado) está en **ADR-014**; el spec 44
  quedó ajustado en consecuencia (§1.1, §2, §4, §5, §6).
- **Ítem 7 — evaluadores D1** (`evaluators/direct_evidence.py` + fusión
  `eind|edir|hyb_or|hyb_and`): **bloqueado por el acta de revisión de `edir_v1`**.
- **Spec 45** (distribución MQTT, repo propio): consume el publisher de 5b.7. En
  paralelo tras el 44 (ADR-010).
- **Spec 43** (clip bench + GT temporal): se dispara al cierre del 44; `evaluate-alerts`
  v2 ya queda listo para su GT.

### 8.3 Deuda técnica registrada (docs 37 §7, 38 §8, 39 §7)

| # | Deuda | Impacto | Cuándo duele |
|---|---|---|---|
| 1 | **Nadie produce `track_id`** (port del tracker, spec 42 §3) | `granularity: subject` (G1) solo vive en fixtures; overlays por persona imposibles | Videos V1–V3 de la defensa |
| 2 | **`experiment_id` no viaja en el `POST /api/runs` del media-plane** (spec 42 §4.1) | La cadena de reconstrucción (spec 40 §2) queda a medias | Ítem 6 (el runner lo necesita) |
| 3 | **Corrida fallida del control-plane = 404** (el `RunSummary` no tiene campo `status`; el `failed` solo se ve en `current()` antes de soltar el slot) | La webconsole no puede mostrar un `failed` histórico | Decisión de contrato pendiente (campo aditivo) |
| 4 | Corrida detenida por `request_stop()` escribe summary sin marca "stopped" (solo el `ErrorEvent` `BusStopRequested`) | Mismo origen que #3 | Ídem |
| 5 | No hay `POST /runs/{id}/stop` ni `GET /runs` (listado) en el control-plane | Una live sin `run_finished` solo muere por idle timeout (default 300 s) o polling; mientras, 409 | Operación con la webconsole |
| 6 | Sin retención de `runs/` en el control-plane + dirs huérfanos por `POST` con bus inválido (`prepare_run` corre antes de `build_bus_source`) | Disco crece sin límite | Corridas largas / demo |
| 7 | `exclude_none=True` latente en `write_event` y el sink del summary del media-plane | El próximo campo opcional cuyo `None` sea informativo desaparecerá en silencio | Al agregar ese campo |
| 8 | G2A en two-node no computable (relojes de dos hosts); para computarlo: chrony/NTP con error declarado, o re-estampar en Nodo B (mediría otra cosa) | Declarado `not_interpretable`, no medido | H5 / EBE two-node (spec 40 §4) |
| 9 | El cierre por idle timeout no marca la corrida `degraded` (queda en `errors.jsonl`, no es silencioso) | Decisión de producto pendiente | Evaluación |
| 10 | Purga de `self._state` del motor — **no urgente** (medido: acotado bajo `scene`, §2.4) | Se vuelve real con el tracker (#1) | Junto al port del tracker |
| 11 | Overlay pinta una caja por escena (deuda de G0, doc 34) | Videos V1–V3 necesitan renderer que consuma `supporting` o modo `subject` (depende de #1) | Material de la defensa |
| 12 | Hallazgos menores de la review de G0 no aplicados (doc 34 §4.4: eficiencia de `supporting`, causas como strings dispersas, helpers de test triplicados, `state_key` no escapa `:`, README/architecture del control-plane desactualizados) | Limpieza | Cuando aparezca el segundo evaluador |
| 13 | El README del media-plane documenta un request shape viejo (el real: `{ingest, prompts:{set_inline, active_ids}, run, bus}`; el modelo va por `EOVRT_MODEL_REF`) | Confunde a quien integre | Ítem 6 |

### 8.4 Pendiente del usuario (no se avanza solo)

1. **Commitear el trabajo de esta sesión** — 79 rutas en 3 repos (§7: 14 en `docs`,
   35 en el control-plane, 30 en el media-plane), todo listo para `git commit` cuando
   lo pida. Sugerencia: un commit por tramo y repo (plan 2 / servicio / G2A / docs),
   o uno por repo.
2. Integrar `mati` → `main` en el control-plane (coordinación con el compañero).
3. Push del media-plane (3 commits viejos sin pushear + todo lo local). *(Recordar:
   nada en GitHub para `docs`; el media-plane sí tiene remote.)*
4. **Acta de revisión de `edir_v1`** (doc 12 §2.2) — lo único que bloquea el ítem 7.
5. `sudo rm` de los 14 dirs de root en `media-plane/runs/` (los escribió Docker
   two-node), si quiere completar la poda.

## 9. Cómo continuar desde otra sesión de Claude Code

Guía autocontenida para arrancar una sesión nueva (o retomar una con `claude --resume
<session-id>`, como en `projects/notas.txt`). El trabajo continúa igual con una sesión
nueva: **este doc y la memoria de Claude son el punto de entrada, no la conversación
anterior.**

**Paso 1 — ubicarse (≈15 min de lectura).**
- Leer **este doc (50)** entero: es el punto de entrada. Para el detalle de cada tramo:
  doc 39 (G2A) → 38 (servicio) → 37 (bus/live). Docs 32/36 son registro histórico.
- La memoria de Claude (`~/.claude/.../memory/MEMORY.md` → `project_arranque_tramo_plataforma.md`)
  ya apunta acá y resume el estado; se carga sola al arrancar.
- Decisiones cerradas: **ADR-001…014** en `docs/decisiones/`. Si algo parece ambiguo, la
  respuesta está en un ADR o un spec (serie 40–45) — **no re-litigar, buscar**. Una
  decisión nueva se registra como ADR (así nacieron 012, 013, 014).

**Paso 2 — verificar que el estado es el esperado** (debe dar 154 / 480, ruff limpio):

```bash
cd ~/projects/e-ovrt_control-plane && .venv/bin/python -m pytest -q --ignore=tests/labs && .venv/bin/python -m ruff check src tests
cd ~/projects/e-ovrt_media-plane  && .venv/bin/python -m pytest -q && .venv/bin/python -m ruff check src tests
```

Si los números coinciden, el working tree es el que este doc describe (nada commiteado:
HEAD `docs@cb92c91`, `control-plane@46c855b`, `media-plane@e12b56a`). Si no coinciden,
alguien commiteó o cambió algo entre sesiones — reconciliar con `git status` antes de seguir.

**Paso 3 — reglas del workspace, no negociables** (§5.10 + `projects/CLAUDE.md`):
nunca commitear sin pedido explícito del usuario en ese turno; nada en GitHub para `docs`
ni `control-plane` (local; el `media-plane` sí tiene remote pero tampoco se pushea solo);
nunca `Co-Authored-By`; cuidado con Docker/WSL (la Capa 3 de los scripts mata WSL — nunca
correr autónomo).

**Paso 4 — el próximo trabajo: ítem 5b** (mitad control-plane de `t_capture→alert` +
`cr01_cr02_v2` + publisher de alertas; alcance completo en §8.1). Escribir el plan con
`superpowers:writing-plans` antes de codear (modelo:
`e-ovrt_control-plane/docs/superpowers/plans/2026-07-09-g0-granularidad-escena.md`; los
tres planes de esta sesión muestran además el patrón de **gates verificados por mutación**).
Ejecutar con `superpowers:subagent-driven-development`, snapshots `git write-tree`, sin
commits. El ítem 6 (experimental-setup + consolidación ADR-014) viene después.

**Trampas operativas vigentes:** cada repo usa su `.venv` (`python3` del sistema no tiene
las deps); `curl` está bloqueado en este entorno (usar `urllib`); `tests/labs` sin numpy
(`--ignore=tests/labs`); `configs/replay_hf_*` apuntan a `runs/latest` inexistente; `runs/`
se poda — archivar la evidencia que un doc cite en `operacion/datos/`.
