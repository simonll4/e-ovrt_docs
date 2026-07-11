# `evaluate-alerts` v2 — matching episodio en ms, `re_alerts` y aplicabilidad

> **✎ Actualización 2026-07-11 (más tarde, doc 54):** el video-gt-lab generó el primer
> GT real y la auditoría del contrato encontró que este evaluador **lo rechazaba**
> (episodios sin `source_id`/`subject_key` — reparado del lado del productor) y que
> ignoraba `provenance.pattern_set_ms`. `temporal.py` cambió **sin commitear**:
> ventanas con prioridad caller > provenance > defaults + `effective_matching_windows`
> (199 passed). Además, el "listo para su GT" del §5 es parcial: **SDR y TTFD no están
> implementados** (faltan `detections_path` y la lógica) — v2 cubre 2 de las 5 métricas
> del spec 43 §10. Detalle y pendientes: **doc 54 §4–§5**.

- **Fecha:** 2026-07-11
- **Qué es:** resultados del evaluador temporal v2 del control-plane (spec 41 §8 item 7):
  matching alerta↔episodio por ventana en ms (spec 43 §4.1), `re_alerts` (ADR-011),
  `sub_threshold_events`, y estados de aplicabilidad (ADR-006). Ejecutado con
  `subagent-driven-development` (5 tareas + 1 fix, revisor por tarea + revisión final).
  **SIN COMMITEAR.**
- **Plan:** `e-ovrt_control-plane/docs/superpowers/plans/2026-07-11-evaluate-alerts-v2.md`.
- **Suite:** control-plane **192 passed** (`pytest -q --ignore=tests/labs`), ruff limpio.
  Baseline 177 → 192. **Revisión final de rama: LISTO CON RESERVAS** (sin Critical/Important
  bloqueante).

## 1. Qué se construyó

`src/eovrt_control/evaluation/temporal.py` pasó de un scaffold **frame-index** (que contaba
las alertas extra como `duplicate`) al evaluador **ms** real de spec 43:

- **Schema `clip_gt.v2` en ms** (`ClipEpisodeV2` con `start_ms`/`end_ms`, `SubThresholdEvent`,
  `ClipGroundTruthV2` con metadata + validación de consistencia interna: episodios dentro de
  `duration_ms`, `negative` ⇔ sin episodios, `level` exige su clave, `end_ms ≥ start_ms`).
- **Matching por ventana en ms** `[start_ms + persistencia_min, start_ms + t_alert_max]`,
  parametrizable por corrida/pattern set. Default Tabla D.4: **CR-01 3s/10s, CR-02 5s/20s**.
- **Evaluación a nivel episodio (ADR-011):** episodio detectado si ≥1 alerta cae en su ventana;
  las alertas extra del mismo episodio son **`re_alerts`** (estabilidad de percepción), **NO**
  falsos positivos — `precision = matched/(matched+unexpected)` las excluye del denominador.
- **`sub_threshold_events`:** una alerta que cae en un evento sub-umbral no es FP verdadero
  (insumo del análisis de errores, R3).
- **FP** = alerta fuera de todo episodio y todo sub-threshold; **`missed`** = episodio sin alerta.
- **Estados de aplicabilidad (ADR-006):** `computed` normal; `not_applicable / non_temporal_source`
  cuando **todas** las alertas carecen de `timestamp_ms` (fuente no temporal).
- **Path v1 intacto** (`TemporalGroundTruth`, frame-based): mismo resultado, tests sin cambios.

## 2. Verificación (gate por mutación)

| Gate | Qué prueba | Verificación por mutación |
|---|---|---|
| `test_evaluate_alerts_v2_gate.py` | v1 en verde (F1=1.0) + v2 escena-condición (recall 1.0, `re_alerts`, FP, alerta en el borde inferior de la ventana) | contar las extra del episodio como FP en vez de `re_alerts` ⇒ **falla** (ADR-011 roto); sacar el borde inferior de `_alert_in_episode_window` ⇒ **falla** (una alerta pre-persistencia matchearía). Ambas reproducidas por implementador y revisor, revert por checksum. |

Fixtures migrados a ms con timestamps de replay **verificados** (no adivinados): escena
CR-01@2000ms/CR-02@2500ms; tracked worker_a@2500ms/worker_c@3500ms.

## 3. Defectos que la revisión atrapó

1. **Doble-conteo entre episodios (Critical)** — `_evaluate_v2` no excluía las alertas ya
   consumidas: dos episodios de la misma condición+clave con ventanas solapadas (spec 43 P8,
   entrada/salida) hacían que **una** alerta matcheara **ambos**, inflando `matched`/`recall`
   en silencio. Fix: `consumed_alert_ids` (espejo de v1) + test de regresión discriminante.
2. Placeholder de `evidence` inválido en el plan (el `PatternEvidence` real exige
   pattern_id/condition_id/subject_key/subject/missing_class/score/rationale) — el implementador
   construyó un `_mk_alert` con evidencia válida.
3. Shims temporales `_LegacyClip*` de la Task 1 borrados al reescribir `_load_ground_truth`.

## 4. Deuda registrada (todas muerden sólo sobre datos GT reales, hoy bloqueados)

| # | Deuda | Cuándo duele |
|---|---|---|
| A | **Asignación greedy por episodio puede DEFLACIONAR recall** con 2 episodios de misma condición+clave, ventanas solapadas (P8) y ≥2 alertas: greedy toma la temprana y consume la otra como `re_alert`, dejando el 2º episodio como `missed`. Reverso del Critical de inflación ya corregido. Fix correcto = **matching bipartito óptimo** (o min-window-width-first). | Al scorear clips P8 reales |
| B | `_evaluate_v2` deja `matches`/`missed_alerts` (listas de detalle) vacías aunque los counts se poblan (v1 las llena) — contrato asimétrico, diagnóstico | Consumidor que itere `evaluation.matches` en v2 |
| C | Alertas mezcladas con/sin `timestamp_ms`: las sin timestamp caen a FP con causa engañosa (anómalo: una fuente temporal estampa todas) | Fuente que emita alertas sin timestamp |

## 5. La frontera GT

`evaluate-alerts` v2 queda **listo para su GT** (spec 41 §8 item 7). Los números **reales**
(P/R/F1, `t_alert-system`, TTFD, SDR) siguen **diferidos**: necesitan el dataset de clips
etiquetados `clip_gt.v2` sobre video real (spec 43), bloqueado por grabación + anotación +
consentimiento (Ley 25.326). El validador `validate_clip_gt.py` es un deliverable del repo
`e-ovrt_datasets`, no de acá. Esta rama entrega el evaluador + la cobertura por fixtures
sintéticos, que es exactamente lo implementable sin el dataset.
