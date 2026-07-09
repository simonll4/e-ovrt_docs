# Spec 41 — control-plane

- **Fecha:** 2026-07-09
- **Estado:** Escrito
- **Repo dueño:** `e-ovrt_control-plane` (base: rama `mati` — motor con matching
  1:1, región por pose, memoria de cobertura, expiración, cooldown; doc 01 §12.
  El cooldown no se usa en la plataforma — ADR-011, ver §7)
- **Decisiones que implementa:** ADR-001/doc 12 (evaluadores D1 + fusión),
  ADR-002 (G0 + G1 demostrativa), ADR-003 (BusSource), ADR-006 (aplicabilidad),
  ADR-007 (corrida 1:1), ADR-008 (servicio mínimo), ADR-009 (config por payload).
  Normativa transversal: **spec 40** (envelope, `experiment_id`, relojes,
  diccionario de métricas).
- **Fase del protocolo del informe que habilita:** "Pipeline y tracking" y
  "Sensibilidad de prompts" (Tabla 36).

## 1. Estado de partida y principio

El motor (`engine/pattern_engine.py` + `evaluators/spatial_absence.py`) NO se
re-arquitectura: ya es push-based por evento y la rama `mati` cubrió los modos de
falla perceptuales. Este spec agrega **granularidad, fuentes, runtime live,
servicio, evaluadores D1 e instrumentación** — todo aditivo. `eovrt_labs` no se
toca (sigue siendo herramienta de calibración; la percepción canónica es el
media-plane — encuadre del doc 01 §12.4.5).

## 2. Granularidad del patrón (ADR-002)

### 2.1 Clave de estado configurable por patrón

Campo nuevo en `PatternDefinition`: `granularity: scene | subject`
(default **`scene`** = G0, el núcleo).

- **`scene` (G0):** clave de estado `(pattern_id, source_id)`. La evidencia por
  unidad se computa igual que hoy (por persona: matching 1:1, región, memoria de
  cobertura) y luego se **agrega**: la escena está "en evidencia" si ≥1 sujeto la
  aporta. El episodio registra `subjects_in_evidence` (máximo y por unidad) como
  metadato — insumo del GT `clip_gt.v2` y de la limitación declarada (doc 07
  D2.2: alternancia de personas dentro de un episodio de escena).
- **`subject` (G1, demostrativa):** clave `(pattern_id, source_id, subject_id)`
  donde `subject_id` = `track_id` del evento **si está presente**. Si un patrón
  `subject` recibe eventos sin `track_id`, el motor cae a G0 para esa fuente y lo
  reporta como **degradación con causa** (`no_track_id`) — reemplaza el warning
  actual de `det_NNN` por un fallback semántico definido. `detection_id` deja de
  usarse como identidad, siempre.

### 2.2 Migración de fixture y tests (costo presupuestado, doc 07 D2.3)

- Regenerar `fixtures/simulated_media/cr01_cr02_temporal/` + `ground_truth.json`
  a nivel escena-condición (formato `clip_gt.v2`, spec 43 §4) manteniendo el
  escenario (persistente / transitorio-no-alertable / segunda condición).
- Conservar una variante del fixture **con `track_id`** para testear G1 y el
  fallback. **Gate de regresión: F1 = 1.0 en ambas granularidades** sobre el
  fixture — condición para cualquier merge del motor (regla de la rama `mati`).

## 3. Fuentes: `MediaEventSource` (doc 05 §4.2)

Interfaz única (iterador de `event | error | END`) con tres implementaciones:

| Impl | Uso | Nota |
|---|---|---|
| `JsonlSource` | DBE / replay | renombre de `sources/media_jsonl.py` (compat: alias) |
| `MemorySource` | tests deterministas | lista en memoria |
| `BusSource` | EBE / live | ZeroMQ SUB, envelope `bus.envelope.v1` (spec 40 §3.1) |

`BusSource` obligaciones (spec 40 §3.2): suscripción previa al disparo del run
(el servicio la establece al aceptar la corrida, antes de devolver 200);
verificación de huecos en `seq` → contador `bus_dropped_events` en métricas y
corrida marcada degradada si > 0; cierre por `run.lifecycle.v1/run_finished` con
**fallback por polling** de `GET /api/runs/{id}` del media-plane (intervalo
configurable); deserialización = misma ruta de validación que la línea JSONL
(paridad por construcción).

## 4. Runtime live (ADR-007)

`runtime/live.py` (o parametrización de `replay.py` — decisión de implementación;
lo normativo es el comportamiento):

- Corrida **1:1** con el run del media-plane: nace suscripta, consume hasta
  `run_finished`/END, escribe **los mismos artefactos** (`pattern_events.jsonl`,
  `alerts.jsonl`, `metrics.jsonl`, `errors.jsonl`, `summary.json`) y cierra.
- `summary.json` agrega: `media_run_id`, `experiment_id`, `source: bus|jsonl`,
  `bus_dropped_events`, `degraded: bool` + `degradation_causes[]`.
- **Test de paridad replay↔stream** (spec 40 §3.4): mismo fixture por
  `JsonlSource` y por `BusSource`+publicador local → `pattern_events` y `alerts`
  idénticos módulo timestamps de procesamiento. Entra al CI (ZeroMQ sobre
  `inproc`/`tcp://localhost`, marcado como test de integración).

## 5. Servicio mínimo (ADR-008)

FastAPI, mismo patrón que el media-plane (`create_app`), **un run activo por vez**:

| Endpoint | Semántica |
|---|---|
| `POST /api/runs` | Dispara corrida. Body: config **por payload completo o por referencia** (path/id — ADR-009); `mode: replay | live`; `experiment_id`. En `live`: suscribe el `BusSource` ANTES de responder 200. 409 si hay run activo. |
| `GET /api/runs/current` | Estado del run activo (`running/succeeded/failed` + contadores en vivo: unidades, alertas, drops). |
| `GET /api/runs/{id}` | Estado + rutas de artefactos de una corrida (activa o histórica). |
| `GET /api/runs/{id}/alerts` | Lista de `AlertEvent`s de la corrida (lee `alerts.jsonl`) — **la fuente de la vista de alertas de la webconsole** (spec 44; la consola NO consume el bus, spec 40 §3.3). Polling; WS/SSE diferido. |
| `GET /api/config` | Config efectiva del run activo (o la última). |
| `GET /healthz` / `GET /readyz` | Estándar de la plataforma. |

- Explícitamente fuera (E-12/ADR-008): sesiones, auth, concurrencia, retención,
  gestión de modelos. La **CLI se conserva completa** (`replay`,
  `validate-config`, `evaluate-alerts`, `export-alerts-csv`) — es el camino
  offline/tests y el fallback declarado del orden de sacrificio (doc 10 ítem 9).
- Arranque: `eovrt-control serve` (o `make serve`), puerto configurable
  (default :8081 — el media-plane usa :8080).

## 6. Evaluadores D1 y fusión E-HYB (ADR-001, doc 12 §4)

### 6.1 `evaluators/direct_evidence.py` (nuevo, ~50 líneas)

Config por patrón: lista de `prompt_id`/labels E-DIR aceptados + umbral por
frase. Produce `PatternEvidence` si una detección directa supera el umbral **y
pasa el gating por persona** (doc 12 §4.2): IoU ≥ 0.5 contra un bbox de persona
para frases persona-céntricas; centro-en-región-superior para detecciones de
parte (`bare_head`). Sin persona matcheada → la detección no aporta evidencia
(se cuenta en métricas como `ungated_direct_hits`, diagnóstico).

### 6.2 Fusión (config del patrón, no evaluador nuevo)

```yaml
evidence:
  strategy: eind | edir | hyb_or | hyb_and     # default: eind
  hyb_and:
    corroboration_factor: 0.5    # multiplica confirm_after_ms
    corroboration_ratio: 0.5     # fracción de hits corroborados requerida
```

- `hyb_or`: evidencia de la unidad = `spatial_absence` OR `direct_evidence`.
- `hyb_and`: `spatial_absence` es la primaria (sin ella no hay episodio); un hit
  con `direct_evidence` concordante en la misma unidad se marca `corroborated`;
  cuando la fracción de hits corroborados del episodio ≥ `corroboration_ratio`,
  la ventana efectiva de confirmación = `confirm_after_ms × corroboration_factor`.
- Los hits persisten su marca en `pattern_events.jsonl` (auditoría: se puede
  reconstruir qué frase aceleró qué alerta — doc 12 §6.4). Parámetros congelados
  por corrida en `effective_config`.

## 7. Pattern set `cr01_cr02_v2` (doc 08 §2.1 — desalineación más importante)

Partir de `cr01_cr02_field_v1` (perfil de campo de `mati`: memoria de cobertura y
expiración de sujetos — semántica de patrón que SE CONSERVA) y alinear al informe
(Tabla 24/D.4). **Sin cooldown (ADR-011):** `realert_cooldown_ms/frames` quedan
sin configurar — el motor emite un `AlertEvent` en cada transición a `confirmed`;
la supresión de re-notificación es política del tramo de distribución (spec 45).
La capacidad queda en el motor sin usar por la plataforma; `field_v1` la conserva
como perfil de diagnóstico/labs.

| Patrón | Severidad | confirm_after_ms | resolve (histéresis) | granularity | cooldown |
|---|---|---|---|---|---|
| PR-01 (CR-01) | **high** | **4000** (banda 3–5 s) | 2000 | scene | — (ADR-011) |
| PR-02 (CR-02) | **medium** | **7000** (banda 5–10 s) | 3000 | scene | — (ADR-011) |

Valores iniciales declarados dentro de las bandas; calibrables en el tramo de
evaluación (ADR-010), nunca entre corridas de una misma comparación. `v1` y
`field_v1` quedan como configs de diagnóstico, documentadas como tales.

## 8. Instrumentación y contratos (spec 40 §5.4/§5.2/§2)

1. **`experiment_id`** (opcional, aditivo) en `PatternStateChanged`, `AlertEvent`,
   `ControlMetricSample`, `RunSummary` — poblado desde la config de corrida.
2. **Hito "primera evidencia positiva"**: `first_evidence_ms`, `frame_index` y
   **`first_evidence_unit_id`** como campos del episodio (persistidos en el evento
   de transición y en `alerts.jsonl`) — completan los hitos obligatorios
   (Tabla D.5). El `unit_id` es **obligatorio**: es la clave de join con las
   métricas del media-plane para `t_capture→alert` (spec 40 §5.2.4); sin él la
   métrica no se puede atribuir.
3. **`alert_registered_ms`** (instante monotónico de escritura del `AlertEvent`) y
   **`ts_receive_ms`** por unidad en `BusSource` — los otros dos insumos de
   `t_capture→alert` que aporta este plano (spec 40 §5.2.4).
4. **TTFA interna** (primera evidencia → alerta) en `summary.json` — etiquetada
   diagnóstico, no sustituye `t_alert-system` (spec 40 §5).
5. **Percentiles P50/P95/P99** de `processing_ms` (hoy solo promedio).
6. **Publisher de alertas al bus** `control.alert.v1.<control_run_id>` (envelope
   spec 40 §3.1, no-bloqueante, mismo patrón que el media-plane): el insumo del
   repo de distribución (spec 45). Habilitado por config; el JSONL sigue siendo
   la verdad.
7. `evaluate-alerts` v2: consume `clip_gt.v2` (episodios escena-condición,
   matching y tolerancias de spec 43 §4.1) además del formato v1 del fixture.
   **Evaluación a nivel episodio (ADR-011):** episodio detectado si ≥1 alerta en
   su ventana; las alertas adicionales del mismo episodio se cuentan como
   `re_alerts` (métrica de estabilidad de percepción), NO como falsos positivos;
   FP = alerta fuera de todo episodio. Resultados con **estados de aplicabilidad
   + causa** (ADR-006).

## 9. Config de corrida (extensión del schema YAML)

```yaml
run: { scenario: ..., name: ..., experiment_id: ... }      # experiment_id nuevo
input:
  type: media_jsonl | bus                                   # bus nuevo
  path: ...                                                 # si media_jsonl
  bus: { endpoint: "tcp://...", topics: ["media.detection.v1."], hwm: 1000,
         finish: { signal: run_lifecycle, poll_url: null, poll_interval_s: 5 } }
patterns: { file: configs/patterns/cr01_cr02_v2.yaml, active_ids: [...] }
alert_bus: { enabled: false, endpoint: ..., hwm: 1000 }     # nuevo (→ spec 45)
outputs: { ... }                                            # sin cambios
```

El servicio acepta este mismo schema por payload (ADR-009); `validate-config`
lo cubre. Paths relativos: al YAML si viene por referencia; prohibidos si viene
por payload (todo absoluto o por id de catálogo) — regla anti-ambigüedad.

## 10. Orden de implementación sugerido (fases con gate propio)

1. **G0 + fixture regenerado** (§2) — gate: F1 = 1.0 ambas granularidades.
2. **`MediaEventSource` (jsonl/memory)** (§3) — gate: replay actual intacto.
3. **BusSource + runtime live** (§3–4) — gate: test de paridad replay↔stream.
4. **Servicio mínimo** (§5) — gate: smoke `serve` + corrida por API + 409.
5. **Evaluadores D1 + fusión** (§6) — gate: tests unitarios de gating y
   corroboración sobre fixture sintético.
6. **Pattern set v2 + instrumentación + publisher de alertas** (§7–8) — gate:
   summary con hitos/percentiles/`experiment_id`; envelope de alerta validado.
7. **evaluate-alerts v2** (§8.7) — gate: fixture v1 sigue en verde + fixture v2
   escena-condición en verde.

## 11. Criterios de terminado (evidencia)

- [ ] Corrida **live** end-to-end: media-plane publica → `BusSource` consume →
      alertas emitidas → summary 1:1 cerrado por `run_finished`, con
      `experiment_id` y contadores de drops en el summary.
- [ ] Test de paridad replay↔stream en verde en CI.
- [ ] Gate de regresión F1 = 1.0 (fixture v2, granularidades scene y subject).
- [ ] Servicio respondiendo los 6 endpoints; corrida disparada por API con config
      por payload; vista de alertas de la webconsole leyendo
      `GET /api/runs/{id}/alerts` (integración en spec 44).
- [ ] Una corrida con `strategy: hyb_and` sobre el fixture, con hits
      `corroborated` visibles en `pattern_events.jsonl`.
- [ ] `report.json` (spec 44) consumiendo este summary sin transformación manual.

## 12. Interfaces

- **Spec 42:** consume `media.detection.v1` con `track_id` opcional; el bus lo
  publica el media-plane (envelope común).
- **Spec 44:** el runner/webconsole disparan por `POST /api/runs`; la vista de
  alertas lee del servicio; el manifiesto provee config y `experiment_id`.
- **Spec 45:** consume `control.alert.v1.*` del publisher de §8.6.
- **Spec 43 (diferido):** `evaluate-alerts` v2 ya queda listo para su GT; al
  ejecutarse el banco, no hay código nuevo aquí.
