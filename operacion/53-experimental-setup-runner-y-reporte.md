# Experimental-setup — runner reproducible + consolidación + reporte (spec 44 A1+A2)

- **Fecha:** 2026-07-11
- **Qué es:** el **núcleo reproducible backend** del ítem 6 / spec 44: el runner que orquesta
  los dos planos por HTTP en el orden correcto (A1), más la consolidación de artefactos
  ADR-014 y el generador de reporte `report.json`/`report.md` con estados de aplicabilidad
  ADR-006 (A2). Ejecutado con `subagent-driven-development` (2 planes, 10 tareas, revisor por
  tarea + fixes + 2 revisiones finales de rama). Repo `e-ovrt_experimental-setup`, package
  `eovrt_webconsole` (`webconsole/backend/`).
- **Planes:** `docs/superpowers/plans/2026-07-11-spec44-a1-runner.md` y
  `docs/superpowers/plans/2026-07-11-spec44-a2-consolidation-report.md`.
- **Suite:** `webconsole/backend` **151 → 204 passed** (`.venv/bin/python -m pytest -q`), ruff
  limpio. A1: LISTO CON RESERVAS (reserva cerrada); A2: **LISTO PARA MERGE**.

## 1. A1 — runner reproducible (spec 44 §3, ADR-004)

`eovrt_webconsole/experiment/`:

- **Manifiesto paraguas `experiment.manifest.v1`** (`manifest.py`): `slug`, `runs.{media,control}`
  (service/config/mode), `sequencing`, `frozen`, con `generate_experiment_id(slug, now) =
  exp_<UTC>Z_<slug>` (now inyectable).
- **Cliente HTTP del control-plane** (`control_backend.py`): `ControlPlaneBackend` espejo del
  `RunBackend` del media-plane — `launch(config, mode, experiment_id) → control_run_id`, `current()`
  (incluye `subscribed`), `status`/`alerts`/`config`; + fake service para tests.
- **Runner** (`runner.py`): `run_experiment` orquesta según modo, con dos invariantes duras
  **verificadas discriminantes por mutación** (implementador y revisor):
  - **live (control-first):** POST control (`mode: live`) **primero** → su 201 + `current().subscribed`
    implica suscripto → recién ahí POST media con `bus.enabled`. El check de suscripción es
    **obligatorio** (`SubscriptionNotConfirmed` bloquea el disparo del media si no hay suscripción).
  - **DBE-replay (media-first):** POST media → poll a terminal → **no dispara control si media
    falló** → POST control (`mode: replay`) apuntando al `detections.jsonl` del run.
  - Polling con timeout (`ExperimentTimeout`); `sequencing` reconciliado con `runs.control.mode`
    (ValueError antes de cualquier I/O); `experiment_id` único propagado a ambos planos.

## 2. A2 — consolidación ADR-014 + generador de reporte (spec 44 §4)

- **Aplicabilidad + join** (`applicability.py`): `MetricResult(name, value, unit, status, cause)`,
  el enum ADR-006 exacto, y `join_capture_to_alert` (única recompute del reporte): por alerta,
  `first_evidence_unit_id` → fila `metrics.jsonl` del media (`capture_monotonic_ns`), computa
  `t_capture→alert` y `t_compute-budget` con aplicabilidad por `source_clock`.
- **Consolidación ADR-014** (`consolidation.py`): arma `runs/<experiment_id>/` **copiando** los
  artefactos livianos de ambos planos (`effective_config`, `summary.json`, `metrics.jsonl`,
  `alerts.jsonl`, `pattern_events.jsonl`, `manifest.effective.yaml`) y **referenciando** por
  `run_id` el `detections.jsonl` pesado (`media/detections.ref.json`) — **nunca lo copia**
  (verificado por mutación). El `runs/` de cada plano sigue siendo la fuente de verdad (DA-03).
  `runs/` git-ignored. `sha256_file` streamed para el anti-drift.
- **Generador de reporte** (`report.py`): `report.json` (mapeado a la Tabla D.6: identificación,
  modelo, entrada, parámetros, hardware, temporalidad, eventos, `resultados`, anti_drift,
  observaciones) + `report.md`. **Agrega, no recalcula** (salvo el join). **Todas** las métricas
  del diccionario spec 40 §5.1 figuran en `resultados` con `status`+`cause` — no se omiten.
- **Cableado en el runner** (`runner.py`): paso post-run **protegido** — tras dos corridas OK,
  consolida + genera reporte; no tumba la corrida si falla; no consolida si algún plano falló.

## 3. Aplicabilidad por fuente (ADR-006 / ADR-013), verificada en el gate

| Fuente (`source_clock`) | `t_capture→alert` | `t_compute-budget` | Métricas GT |
|---|---|---|---|
| video (`media`) | `not_interpretable / dbe_media_time` | `computed` | `not_applicable / no_ground_truth` |
| imágenes (`none`) | `not_applicable / non_temporal_source` (+ `re_alerts`, TTFA) | `computed` (+ G2A, percepción) | `not_applicable / no_ground_truth` |
| viva single-host (`wallclock`) | `computed` | `computed` | `not_applicable / no_ground_truth` |

Las métricas que exigen GT **figuran** con `not_applicable / no_ground_truth` (no se omiten): eso
demuestra que la instrumentación está lista **antes** que el GT. Los números reales de percepción
y temporales llegan con el dataset de clips etiquetados (spec 43, diferido).

## 4. Defectos que la revisión atrapó

- **A1:** el gate `SubscriptionNotConfirmed` no era mutation-resistant (borrar el guard pasaba la
  suite) — se agregó el test negativo (fuerza `subscribed=False`, asserta que el media NO se
  dispara). Missing plane keys → `ValueError` claro. Placeholder de config inválido.
- **A2:** doble-conteo de aplicabilidad evitado; `re_alerts` en fuente no-temporal corregido a
  `non_temporal_source` (spec 40 §5.2.3.3), no `no_ground_truth`.

## 5. Deuda registrada (toda en superficie diferida)

- `two_node`: `t_compute-budget` inconsistente entre `two_node` puro y `two_node`+`none` (mismos
  inputs cross-host). Reconciliar al retomar EBE two-node (sin productor hoy).
- `_aggregate_t_capture_to_alert` colapsa si CUALQUIER alerta no joinea (conservador; baja prob.).
- anti-drift inerte hasta que un productor popule `sent_config` en el manifiesto efectivo.
- `_g2a_metric` pasa `g2a.state` sin guardar el enum (seguro hoy; hardening de 1 línea).
- `GET /api/config` del control-plane real devuelve el dict crudo (el fake lo envuelve).

## 7. Plan B — webconsole backend (spec 44 §5) — HECHO (2026-07-11)

El BFF de la webconsole pasó de mono-plano (sólo media-plane :8080) a **superficie de gestión
de la plataforma** (`webconsole/backend`, **151→236 passed**, LISTO PARA MERGE), aditivo (los
204 tests de A1+A2 intactos):

- **Segundo backend** hacia el control-plane :8081 (`app.state.control_backend`, reusa el
  `ControlPlaneBackend` de A1); `control_service_url` por config.
- **CRUD del manifiesto paraguas** `experiment.manifest.v1` (`POST/GET /api/experiments/manifests`),
  reusa `write_manifest` + el schema de A1; el listado tolera YAML roto (no 500).
- **Disparo orquestado** `POST /api/experiments/run`: un `ExperimentRunManager` (un experimento
  activo por vez, 409 si hay otro) corre `run_experiment` de A1 en una **tarea de fondo** (asyncio,
  no bloquea el event loop; el slot se libera pase lo que pase, incluso ante crash del task);
  `GET /api/experiments/current` / `{id}` para el estado.
- **Vista de alertas** `GET /api/experiments/{id}/alerts`: proxy a `GET /api/runs/{id}/alerts` del
  control-plane (polling, sin ZeroMQ en la consola).
- **Lectura del reporte** `GET /api/experiments/{id}/report`: lee el `report.json` del dir
  consolidado, con flag `non_temporal` (ADR-013) para que el frontend deshabilite controles
  temporales.

**Defectos que la revisión atrapó** (con test de regresión): YAMLError→500 en el listado; el
test de slot-free-on-crash faltaba (la lógica era correcta, el guard no era mutation-resistant);
**path traversal HIGH** en `/report` (`repo_root/runs/<experiment_id>` con `%2e%2e` percent-encoded
escapaba un nivel) — cerrado con validación del id + containment `is_relative_to(runs/)`.

**Deuda B:** `poll_interval_s=0.0` en producción (busy-loop, poner ~0.25s); `report.json` corrupto
→ 500 (no client-triggerable); el env de fakes no produce `consolidated_dir` real (limitación de
test, no bug: los planos reales escriben `runs/`).

## 8. Lo que sigue

- **Plan C — frontend React (spec 44 §5.2, declarado sacrificable):** navegación por experimento,
  vista de alertas, disparo orquestado desde la UI, detección no-temporal. Consume las rutas de B.
- **Spec 45 — distribución (repo nuevo):** consume el publisher `control.alert.v1`, MQTT, cooldown
  de notificación (ADR-011), ledger.
