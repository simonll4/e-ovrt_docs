# Instrumentación G2A y timestamps de captura (media-plane) — resultados

- **Fecha:** 2026-07-10
- **Qué cubre:** la **mitad media-plane** del ítem 5 del orden de la spec 41 §10: los insumos de
  `t_capture→alert` que produce el plano de medios (spec 40 §5.2.4, spec 42 §5/§5.1).
- **Plan ejecutado:** `e-ovrt_media-plane/docs/superpowers/plans/2026-07-10-instrumentacion-g2a-y-captura.md`
- **Estado:** completo, **sin commitear**.
- **Falta la otra mitad** (plano de control): `ts_receive_ms`, `first_evidence_unit_id`,
  `alert_registered_ms`, percentiles de `processing_ms`, y el pattern set `cr01_cr02_v2`. Hasta que
  esté, **`t_capture→alert` todavía no se puede calcular**: este tramo deja los insumos, no la métrica.

## 1. Qué quedó construido

| Pieza | Archivo |
|---|---|
| Instante de captura por unidad (`capture_monotonic_ns`, `capture_wallclock_ms`) | `contracts/visual_unit.py` |
| Tipo de reloj de cada fuente (`source_clock`) | `sources/*.py` (constante `SOURCE_CLOCK`) |
| Los tres campos cruzan el canal y el wire de two-node | `contracts/normalized_unit.py`, `preprocessing/normalizer.py`, `transport/serialization.py` |
| `g2a_ms` por unidad en `metrics.jsonl` | `contracts/metrics.py`, `runtime/pipeline.py` |
| Percentiles, warm-up, presupuesto y aplicabilidad | `metrics/g2a.py`, `contracts/events.py` |
| `warmup_units` declarado en la config | `config/schemas.py` |

**El instante de captura se estampa donde se lee la unidad**, con un `default_factory` en el
`VisualUnit`: se evalúa al construirlo, que es exactamente el momento de lectura. Ninguna fuente
puede olvidarse, y las fuentes futuras lo heredan gratis.

`metrics.jsonl` gana, por `unit_id` (que es la clave de join con las alertas del control-plane):
`capture_monotonic_ns`, `capture_wallclock_ms`, `g2a_ms`. `summary.json` gana `source_clock` y el
bloque `g2a`.

## 2. Suites (medidas)

| Repo | Antes | Después | Lint |
|---|---|---|---|
| media-plane (`pytest -q`) | 456 passed | **480 passed** | `ruff`: limpio |
| control-plane (`--ignore=tests/labs`) | 154 passed | **154 passed** (sin cambios) | `ruff`: limpio |

## 3. Corrida real sobre video

Servicio con `EOVRT_MODEL_REF=mock` sobre `data/samples/videos/recorte-1.mp4`, 20 unidades:

```
source_clock : media          <-- archivo de video: los timestamp_ms son tiempo de MEDIO
g2a          : state=computed  count=20  warmup_units=0
               p50_ms=14.656   p95_ms=31.819
               presupuesto 50-250 ms -> p95_within_budget=True
metrics.jsonl: 20/20 filas con capture_monotonic_ns, capture_wallclock_ms y g2a_ms
```

Evidencia: `datos/39-2026-07-10-g2a-video-summary.json`.

## 4. Lo que NO se publica, y por qué

Dos declaraciones de aplicabilidad, en el vocabulario de ADR-006. **Nunca se publica un número que
no significa nada.**

**`source_clock`** decide, aguas abajo, si `t_capture→alert` es interpretable (spec 40 §5.2.3):

| Fuente | `source_clock` | Lectura de `t_capture→alert` |
|---|---|---|
| `RtspSource` | `wallclock` | latencia genuina ⇒ `computed` |
| `VideoFileSource` | `media` | `not_interpretable / dbe_media_time` (el replay consume el archivo más rápido que tiempo real) |
| `ImageFolderSource` | `none` | `not_applicable / non_temporal_source` (no hay tiempo) |

**Two-node.** En `topology.mode: two_node`, `capture_monotonic_ns` lo estampa el **Nodo A** y el
G2A lo cerraría el **Nodo B**. `CLOCK_MONOTONIC` tiene un origen arbitrario por máquina: la resta
puede dar negativo, gigantesco, o "razonable" por casualidad. Por eso:

- cada fila de `metrics.jsonl` escribe **`g2a_ms: null`** (la clave existe: `null` significa "no
  medible", y es distinguible de un artefacto viejo sin el campo);
- el summary declara `state: "not_interpretable", causes: ["cross_node_monotonic_clock"]`, con
  `count: 0` y **sin percentiles**.

Esto último costó un hallazgo de review: declararlo solo en el summary **no alcanzaba**, porque el
plano de control joinea las **filas** de `metrics.jsonl`, no el summary.

**Warm-up.** Las primeras `warmup_units` unidades (cronológicas, no las más lentas) se excluyen de
los percentiles y el número se **declara** en el summary. Con `warmup_units` ≥ la cantidad de
muestras, el estado es `applicable_not_computed / all_units_in_warmup`, no un cero silencioso.

## 5. El gate, y hasta dónde llega

`tests/test_g2a_gate.py` verifica los tres campos por unidad, el `source_clock`, y que el bloque
G2A no mienta sobre el conteo. Se lo sometió a **dos mutaciones**:

| Mutación | Gate solo | Suite completa |
|---|---|---|
| A — `default_factory=time.monotonic_ns` → `default=0` (todas las unidades comparten instante) | **falla** (2 failed) | falla |
| B — borrar el copiado de `capture_monotonic_ns` en `normalize_spatial` | **pasa** | **falla** |

**La mutación A hizo falta endurecer el gate**: tal como lo escribí en el plan, no fallaba, porque
`monotonic_ns() - 0` sigue siendo un número enorme y positivo, y las aserciones `g2a_ms > 0` y
`g2a_ms >= latency_inference_ms` sobrevivían. Se agregó `capture_monotonic_ns > 0`.

**La mutación B es la peligrosa** y el gate **no la caza solo**: si alguien borra el copiado, el
`default_factory` del `NormalizedUnit` re-estampa **en silencio** con el instante de la
normalización, y el G2A colapsa a casi cero sin que nada explote. En el pipeline mock, captura y
normalización ocurren en microsegundos, así que el gate no lo distingue. La caza
`tests/test_capture_timestamps.py::test_normalize_spatial_preserves_the_read_instant_and_does_not_restamp`,
que duerme 20 ms entre la lectura y la normalización para volver visible el re-estampado. Ese test
se agregó a raíz de una code review: no estaba en el plan.

## 6. Defectos encontrados durante la implementación

1. **`exclude_none=True` borraba el campo (Important).** `JSONLSink.write_metric` serializaba con
   `exclude_none=True`, así que `g2a_ms=None` **desaparecía** de la fila en vez de escribirse como
   `null`. Un consumidor no podría distinguir "no interpretable en esta topología" de "artefacto de
   un schema anterior". Ahora `g2a_ms` nunca se omite. **La misma trampa sigue latente** en
   `write_event` y en el sink del summary: hoy no muerde, pero morderá cuando se agregue otro campo
   opcional cuyo `None` sea informativo.
2. **`not_interpretable` perdía contra "sin muestras" (Important).** En two-node el acumulador queda
   vacío, así que el summary reportaba `applicable_not_computed / no_units_processed` — falso: sí
   hubo unidades, lo que no se puede es interpretarlas. Se reordenó `summarize()`.
3. **Hueco de cobertura del re-estampado silencioso (Important).** Ver §5, mutación B.
4. **Gate vacuo para la mutación A.** Ver §5.
5. **Un comentario falso (Minor).** El import de `G2AAccumulator` en `run_context.py` se justificaba
   con "produce un ciclo de import". Se comprobó que no hay ciclo (`contracts/events.py` no importa
   nada de `runtime/` ni `metrics/`); el import se subió al tope. Un comentario que justifica algo
   con una razón falsa es peor que no tenerlo.

## 7. Deuda

1. **`experiment_id` sigue sin viajar en el `POST /api/runs`** del media-plane (spec 42 §4.1). El
   `RunSummary` tiene el campo y el writer lo puebla desde `config.experiment.id`, pero el request no
   lo acepta. La cadena de reconstrucción (spec 40 §2) queda a medias.
2. **En two-node, G2A no se puede computar** con este diseño. Habría que declarar la sincronización
   de relojes (chrony/NTP) con su error estimado, o re-estampar la captura en el Nodo B (que mediría
   otra cosa). Decisión pendiente, spec 40 §4.
3. **`t_capture→alert` todavía no existe**: falta la mitad del control-plane.
4. **`exclude_none=True` latente** en `write_event` y en el sink del summary (§6.1).
