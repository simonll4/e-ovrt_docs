# Ítem 5b — instrumentación `t_capture→alert` (mitad control-plane), `cr01_cr02_v2` y publisher de alertas

- **Fecha:** 2026-07-11
- **Qué es:** el reporte de resultados del ítem 5b del tramo plataforma (doc 50 §8.1): la
  mitad control-plane de la cadena `t_capture→alert`, el pattern set oficial `cr01_cr02_v2`
  alineado al informe, y el publisher de alertas al bus. Ejecutado con
  `superpowers:subagent-driven-development` (implementador → revisor por tarea → fix →
  re-review, todos con reproducción) y **revisión final de rama**. **SIN COMMITEAR** (regla
  del workspace).
- **Plan:** `e-ovrt_control-plane/docs/superpowers/plans/2026-07-10-5b-instrumentacion-control-plane-y-publisher.md`.
- **Estado de suites:** control-plane **177 passed** (`pytest -q --ignore=tests/labs`), ruff
  limpio. Baseline al arranque: 154. Progresión: T1→156, T2→158, T3→159, T4→160, T5→163,
  T6→165, T7→168 (el fix del review sumó un test de integración), T8→173, T9(gate)→177.
- **Revisión final de rama: LISTO PARA MERGE** (sin defectos Critical ni Important).

## 1. Qué se construyó (9 tareas)

### Insumos de `t_capture→alert` que aporta el control-plane (spec 40 §5.2.4)

Todos son **instantes monotónicos del host de control** (`time.monotonic()*1000`),
comparables con el `capture_monotonic_ns` del media-plane **cuando corren en el mismo host**.

- **`ts_receive_ms`** por unidad en `BusSource`/`JsonlSource` → `metrics.jsonl`
  (`ControlMetricSample`). Requirió ensanchar `SourceItem` a 4-tupla
  `(index, event, error, ts_receive_ms)`; el instante ya se calculaba en `bus.py` para el
  idle-timeout, ahora se propaga hasta la fila de métricas.
- **Hito de primera evidencia por episodio**: `first_evidence_ms`,
  `first_evidence_unit_id` (clave de join **obligatoria**) y `first_evidence_frame_index`,
  capturados **write-once** al abrir el episodio (no se reescriben con unidades posteriores;
  se resetean al resolver/expirar junto a `first_hit_timestamp_ms`). Persisten en
  `PatternStateChanged` **y** en `AlertEvent`. Distinto de `first_hit_timestamp_ms`, que es
  tiempo de medio (`source.timestamp_ms`) — magnitud aparte, no se mezclan.
- **`alert_registered_ms`** (instante monotónico de escritura del `AlertEvent`) en `AlertEvent`.
- **`experiment_id`** (ADR-004) en los tres eventos (`PatternStateChanged`, `AlertEvent`,
  `ControlMetricSample`) — antes sólo estaba en el summary.
- **Percentiles P50/P95/P99 de `processing_ms`** y **TTFA interna** (diagnóstico:
  `alert_registered_ms − first_evidence_ms`, sólo control-plane) en el `RunSummary`, vía un
  helper determinista nuevo `metrics/latency.py::percentiles` (interpolación lineal, sin
  `statistics.quantiles`).

### Join `t_capture→alert` con estado de aplicabilidad (ADR-006, spec 40 §5.2.3)

`metrics/latency.py::join_capture_to_alert` une cada alerta (por `first_evidence_unit_id`)
con el `capture_monotonic_ns` del media-plane y declara:
- `wallclock` single-host → `computed` (valor = `alert_registered_ms − capture_ns/1e6`);
- `media` (DBE video) → `not_interpretable / dbe_media_time`;
- `none` (imágenes) → `not_applicable / non_temporal_source`;
- `two_node` sin sync → `not_interpretable / clock_skew`;
- captura ausente → `applicable_not_computed`.
La precedencia `none`/`media` **antes** de `two_node` está verificada (una fuente no temporal
en two-node sigue siendo `not_applicable`, no `clock_skew`).

### Pattern set oficial `cr01_cr02_v2` (spec 41 §7)

`configs/patterns/cr01_cr02_v2.yaml` + run config `configs/replay_cr01_cr02_v2.yaml`.
Valores del informe (Tabla 24/D.4): **CR-01 severity `high`, `confirm_after_ms: 4000`,
resolve 2000; CR-02 severity `medium`, `confirm_after_ms: 7000`, resolve 3000**;
`granularity: scene`; **sin cooldown** (ADR-011, `realert_cooldown_*` sin configurar — el
motor emite en cada confirmación) y **sin memoria de cobertura** (ADR-012,
`coverage_memory_*` sin configurar; el mecanismo `coverage_memory_unsupported_scene` ya
estaba cableado del tramo G0). El motor **no se tocó**.

### Publisher de alertas al bus (spec 41 §8 item 6)

`transport/alert_bus.py::AlertBusPublisher` publica cada `AlertEvent` en
`control.alert.v1.<control_run_id>` — **espejo fiel** del `BusPublisher` del media-plane
(envelope `bus.envelope.v1`, XPUB, `seq` monótono consumido aunque se descarte,
`flags=NOBLOCK`, `wait_for_subscriber`, `close` idempotente, protección de fuga de socket).
Cableado en `runtime/core.py`: **persiste primero, publica después**; `run_finished` sale
pase lo que pase en el `finally`; apagado por default (`AlertBusSection.enabled`). Es el
insumo del repo de distribución (spec 45).

## 2. Verificación (gates por mutación + e2e real)

Regla del tramo: **un gate que no puede fallar no es un gate.** Cada gate se sometió a
mutación (implementador **y** revisor, independiente).

| Gate | Qué prueba | Verificación por mutación |
|---|---|---|
| Flicker escena (ADR-012, `test_pattern_engine.py`) | un EPP que desaparece/reaparece dentro de una ventana menor que `resolve_after_ms` **no** resuelve ni re-alerta | 1er borrador era vacuo (1 solo frame clear ⇒ elapsed siempre 0); se agregó un 2º frame clear. `resolve_after_ms=100` ⇒ **falla** (transiciona a resolved); con 2000 ⇒ pasa. |
| Byte-paridad payload↔JSONL (`test_alert_bus.py`) | el payload publicado es byte-idéntico a la línea de `alerts.jsonl`, con un campo `None` deliberado | usar `model_dump_json(exclude_none=True)` (el sketch del plan) ⇒ **falla** (dropea la clave `None`, el sink escribe `null`). |
| Cadena `t_capture→alert` (`test_capture_to_alert_gate.py`) | corrida real in-process (RunManager replay) ⇒ toda alerta trae `first_evidence_*`/`alert_registered_ms`; el join declara el estado correcto por `source_clock` | borrar `first_evidence_unit_id` en el motor ⇒ **falla** Test A; forzar `computed` en la rama `media` del join ⇒ **falla** Test B (`media`). Ambas revertidas, suite verde. |

**Corrida end-to-end real, dos servicios por bus** (evidencia en `operacion/datos/51-*`):

| Corrida | Números | Evidencia |
|---|---|---|
| **Live por bus** (control-plane `:8181` `mode:live` + media-plane `:8180` mock, `recorte-1.mp4`, 300 unidades, `cr01_cr02_v2`, `alert_bus.enabled`) | 201 con `subscribed:true` **antes** de disparar el media-plane; 300/300 unidades, **0 perdidas**, cierre 1:1 por `run_finished`; **2 alertas** (CR-01 high + CR-02 medium) con `first_evidence_*`/`alert_registered_ms` válidos (`alert_registered_ms ≥ first_evidence_ms`); `degraded:false`, `pattern_evaluation.state: computed`; G2A p95 20.6 ms | `datos/51-2026-07-11-5b-*` |
| **Join sobre esa corrida** | `source_clock: media` (video_file) ⇒ join = `not_interpretable / dbe_media_time` para ambas alertas — el resultado **honesto y correcto** para DBE video (spec 40 §5.2.3), no una falla | `datos/51-2026-07-11-5b-join.json` |

**Hallazgo de la corrida real:** con `max_units: 30` (como las corridas de `cr01_cr02_v1`)
salieron **0 alertas** — `cr01_cr02_v2` confirma a 4000/7000 ms medidos contra los
`timestamp_ms` del video (~33 ms/frame), así que 30 frames ⇒ ~1 s, insuficiente. Con 300
unidades (~10 s) aparecen las alertas. **Esto valida las bandas del informe**: v2 exige
evidencia sostenida, a diferencia de v1 (`confirm_after_frames: 1`).

## 3. Defectos que la revisión adversarial atrapó

1. **Byte-paridad rota en el sketch del plan** — el plan proponía
   `model_dump_json(exclude_none=True)` para el payload del bus, pero el `JsonlSink` del
   control-plane escribe `json.dumps(model_dump(mode="json"), ensure_ascii=True)`: con un
   campo opcional en `None`, `exclude_none` **borra la clave** mientras el JSONL escribe
   `null` ⇒ no byte-idénticos. El implementador igualó la serialización del sink y escribió
   un test discriminante con `experiment_id=None`. (La misma trampa `exclude_none` que ya
   mordió al media-plane en el G2A.)
2. **Gate de cadena sin cobertura del cableado real** (T7) — los tests probaban el
   `AlertBusPublisher` aislado (socket falso) pero nada ejercitaba `execute_over_source` con
   `alert_bus.enabled`. Fix: test de integración que corre por `RunManager` real, asserta
   byte-paridad e2e y el sentinela `run_finished` (no-flaky verificado 3×).
3. **Flicker test vacuo** (T6, autodetectado) — con un solo frame clear el `elapsed` es
   siempre 0; el test pasaba con cualquier `resolve_after_ms`. Se corrigió con un 2º frame y
   se verificó discriminante por mutación.

Detalle por tarea en `.superpowers/sdd/progress.md` y los `task-N-report.md` del repo.

## 4. Reglas duras confirmadas

- **`ts_receive_ms` no va en `_VOLATILE` del gate de paridad**: el gate compara
  `pattern_events.jsonl` y `alerts.jsonl`, no `metrics.jsonl`. `first_evidence_ms` y
  `alert_registered_ms` (monotónicos, aparecen en esos dos archivos) **sí** van; los campos
  derivados del contenido (`first_evidence_unit_id`/`frame_index`, `experiment_id`) **no**
  van — siguen comparándose (el gate no se debilita).
- **El publisher nunca muere la corrida**: `publish` traga y cuenta (`send_failures`), nunca
  propaga; `run_status` degrada a `failed` pero **re-lanza** la excepción real (no la traga);
  socket cerrado por el hilo que lo creó (regla SIGABRT).
- **Nunca publicar un número sin sentido**: en DBE video el join sale
  `not_interpretable / dbe_media_time`, no un cero.

## 5. Deuda registrada

| # | Deuda | Cuándo duele |
|---|---|---|
| A | **`join_capture_to_alert` no está cableado a ningún artefacto de corrida** — es un helper de reporte, listo para el ítem 6/spec 43. Nadie asuma que `t_capture→alert` se registra vivo todavía. | Ítem 6 (reporte consolidado) lo consume |
| B | `join_capture_to_alert` sin type hints; rama de instancia `AlertEvent` sin test (solo dicts); sin test del caso combinado `media`+`two_node` | Al cablearlo (ítem 6/spec 43) |
| C | `AlertBusPublisher.wait_for_subscriber(expected=1)` vs `expected=2` del media-plane; `wait` apagado por default | Cuando exista el consumidor de distribución (spec 45, 2 prefijos) |
| D | Constantes de envelope duplicadas entre `sources/bus.py` (consumer) y `transport/alert_bus.py` (producer) — roles de bus distintos, posible por diseño | Rename de prefijo |
| — | (Se mantiene) toda la deuda de doc 50 §8.3 (track_id, `experiment_id` en el `POST` del media-plane, `status`/`stop`/`GET /runs`, retención de `runs/`, etc.) | — |

## 6. Lo que sigue

Ítem 5b **cerrado**. Falta (doc 50 §8.1, "luego"): **`evaluate-alerts` v2** (spec 41 §8 item 7:
consume `clip_gt.v2`, evaluación a nivel episodio, `re_alerts` no son FP, estados de
aplicabilidad) — es un subsistema distinto que extiende `evaluation/temporal.py`, va en un
**plan hermano**. Después, el **ítem 6** (experimental-setup, spec 44 + consolidación ADR-014),
que consume el `join` (deuda A) y el publisher de alertas (spec 45).

**Pendiente del usuario:** commitear (ahora 88 rutas en 3 repos: las 79 previas de doc 50 +
el trabajo de 5b sin commitear + doc 51 y su evidencia). Todo listo para `git commit` cuando
lo pida.
