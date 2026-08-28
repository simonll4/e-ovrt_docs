# Relevamiento técnico — `e-ovrt_control-plane` (2026-08-28)

Auditoría de sólo lectura del repo contra (a) lo que la documentación del proyecto afirma
sobre él y (b) lo que el protocolo del informe (§17.1) prescribe. Toda evidencia es
`ruta:línea` relativa a `/home/simonll4/projects/e-ovrt_control-plane/` salvo indicación.

---

## A) Estado del repo

| Ítem | Valor | Evidencia |
|---|---|---|
| Rama / HEAD | `feature/control-service` · `64cc976` · 2026-08-19 22:13 UTC · "feat(infra): imagen Docker del servicio + limpieza y sincronización de docs" | `git log -1` |
| Working tree | limpio (0 líneas en `git status --short`) | `git status` |
| Remote | `origin git@github.com:Pandulc/e-ovrt_control-plane.git` | `git remote -v` |
| Historia reciente | 30 commits entre 2026-07-02 y 2026-08-19; hitos: `46c855b` G0 (07-10) · `e5415df` bus+live+servicio :8081 (07-10) · `4a504b2`/`853f690`/`b3c6cc8` evaluate-alerts v2 (07-11/07-19) · `ef001ff` live usa v2 (07-23, F-DR9) · `03ee8b0` deprecación v1 + ADRs 0006-0013 (07-29) · `c1cbb56` 3 fixes del evaluador (08-03) · `5327080` direct_evidence (08-04) · `b0ba763` G1 como decorador de fuente (08-05) · `64cc976` Dockerfile (08-19) | `git log -30` |
| Paquete | `eovrt-control-plane` 0.1.0; `requires-python = ">=3.11"`; deps núcleo: pydantic, pyyaml, typer, rich, pyzmq, msgpack, fastapi>=0.110, uvicorn[standard]; extras `dev` (pytest, ruff, httpx) y `labs` (torch, transformers, ultralytics, opencv…) | `pyproject.toml:1-26` |
| Entry points | `eovrt-control` (`eovrt_control.cli:app`), `eovrt-labs` | `pyproject.toml:39-41` |
| pytest | `testpaths=tests`, `addopts=--ignore=tests/labs`, marker `integration` | `pyproject.toml:52-60` |
| venv real | `.venv` → **Python 3.14.4** (`/usr/bin/python3.14`); fastapi 0.139.0, pydantic 2.13.4, pyzmq 27.1.0 | `.venv/pyvenv.cfg` |
| Tests (collect-only) | **312 tests** núcleo en 27 archivos (`--ignore=tests/labs`); `tests/labs/` 22 `def test_` en 2 archivos (requieren extra `[labs]`, no se recolectan) | `pytest --collect-only -q \| grep -c '::'` |
| Tamaño src | 8.430 líneas; núcleo `eovrt_control` (motor 651 líneas `engine/pattern_engine.py`, evaluador temporal 1.307 líneas `evaluation/temporal.py`, bus SUB 375, run_manager 435) + `eovrt_labs` (tracker, generador, visualización) | `wc -l` |
| CLI | `validate-config`, `replay`, `live`, `evaluate-alerts`, `export-alerts-csv`, `serve` (puerto default 8081) | `src/eovrt_control/cli.py:20-137` |
| Servicio HTTP | **12 endpoints**: `GET /healthz`, `GET /readyz`, `POST /api/runs`, `GET /api/runs`, `GET /api/runs/current`, `GET/DELETE /api/runs/{id}`, `GET /api/runs/{id}/{alerts,pattern-progress,pattern-events,received-units}`, `GET /api/config` | `service/routers/{health,runs,config}.py` |
| Dockerfile | `infra/docker/Dockerfile`: `python:3.11-slim`; copia `pyproject.toml`, `src/`, `configs/`; `pip install .` (sólo núcleo, sin `[labs]`/`[dev]`); `ENV EOVRT_CONTROL_RUNS_DIR=/data/runs`; `VOLUME /data/runs`; `EXPOSE 8081 5558`; `HEALTHCHECK` con `urllib` a `/healthz`; `CMD eovrt-control serve --host 0.0.0.0 --port 8081`. `.dockerignore` excluye `runs/ docs/ tests/ fixtures/ .venv/`. **Build nunca ejecutado** (pendiente declarado en CLAUDE.md raíz) | `infra/docker/Dockerfile`, `.dockerignore` |
| ADRs locales | `docs/decisions/ADR-0001…0004` (serie propia del repo) y `ADR-0006…0013` (desde 07-29 adoptan la numeración de la serie del proyecto; **no existe ADR-0005**); nota de serie en `ADR-0006` | `docs/decisions/` |
| Configs activas | `configs/patterns/`: `cr01_cr02_v2` (oficial), `cr01_cr02_v2_subject` (G1), `cr01_cr02_edir_v1`, `cr01_cr02_hyb_or_v1`, `cr01_bare_head_v1`, `cr01_cr02_temporal_eval` (fixture), `cr01_cr02_v1` (**deprecado**). Corridas: `replay_dbe_cr01_cr02`, `live_ebe_cr01_cr02`, `replay_simulated_cr01_cr02_temporal`, `smoke_ebe_{a,b}`, `smoke_claqueta`. Archivo: `configs/_archive/` (13 archivos, README propio) | `find configs` |
| Artefactos locales | `runs/` con 51 corridas (gitignored; 2026-07-18 → 2026-08-18), incl. `smoke_ebe_b` (G1 live) y `control_ebe_oakd_live_20260818*` (alert_bus habilitado) | `ls runs` |
| Deriva declarada | CLAUDE.md raíz indica `python3.11 -m venv`; el venv real es 3.14.4 (tolerado por `>=3.11`; la deriva está declarada en la sección experimental-setup del CLAUDE.md raíz) | — |

---

## B) Afirmaciones verificadas

Leyenda: ✅ coincide · ⚠️ coincide con matiz / imprecisión · ❌ no coincide.

### B.1 `/home/simonll4/projects/CLAUDE.md` — "Acople entre planos" y "e-ovrt_control-plane"

| # | Afirmación | Veredicto | Evidencia |
|---|---|---|---|
| 1 | Pattern set oficial `cr01_cr02_v2`: CR-01 `high` `confirm_after_ms: 4000`, CR-02 `medium` `7000` | ✅ | `configs/patterns/cr01_cr02_v2.yaml:16,32` (CR-01 high / 4000.0) y `:40,56` (CR-02 medium / 7000.0); `granularity: scene` `:19,43`; resolve 2000/3000 `:33,57` |
| 2 | `v1` deprecado, produce falsos `missed` por umbrales incompatibles con `derive_clip_gt` (F-DR9) | ✅ | Cabecera `configs/patterns/cr01_cr02_v1.yaml:1-13` (DEPRECADO, F-DR9); v1 tiene `confirm_after_frames: 1` sin `confirm_after_ms` (`:33-34,54-55`) y CR-01 `medium` (`:20`) → confirma en el primer frame; el evaluador exige `alert.timestamp_ms >= start_ms + persistencia_min` (`evaluation/temporal.py:308-310`) y trata la alerta anterior al borde como prematura = FP (`:329-333`) ⇒ episodio `missed` + alerta `unexpected` |
| 3 | `alert_bus.enabled` default `False` | ✅ | `config.py:194-201` (`enabled: bool = False`, endpoint `tcp://0.0.0.0:5558`, `wait_for_subscriber_ms` default 0); README `:56`; `docker-compose.yml:64-66` del experimental-setup lo advierte |
| 4 | Orden de suscripción: el consumidor se suscribe ANTES del disparo; el 201 de `POST :8081/api/runs mode: live` implica suscripción | ✅ | `service/run_manager.py:108-114` (construye `BusSource` dentro de `start_run`, antes de devolver); `runtime/live.py:19-27`; `sources/bus.py:3-5,68-77` (construir = `connect`+`SUBSCRIBE`); campo `subscribed` en `run_manager.py:372-379`. El paso "primero `POST :8082`" es del repo de distribución (fuera de alcance); del lado control, `AlertBusPublisher` bindea al arrancar la corrida (`runtime/core.py:196-202`) y puede esperar suscriptor (`transport/alert_bus.py:85-120`) |
| 5 | Huecos de `seq` = `bus_dropped_events`, degradan la corrida, nunca se silencian | ✅ | `sources/bus.py:336-365` (`_check_seq`: primer seq>0 y gaps suman `_dropped`); `runtime/core.py:315-319` (`degradation_causes.add("bus_dropped_events")`); `contracts/metrics.py:62-69`; drenaje acotado avisa pérdidas no contables `bus.py:159-186` |
| 6 | Nunca cerrar un socket ZeroMQ desde otro hilo durante `recv_multipart` (SIGABRT); las fuentes exponen `request_stop()` | ✅ | `sources/bus.py:96-102`; `sources/base.py:40-47`; `service/run_manager.py:329-336` (`shutdown` sólo llama `request_stop`); `sources/tracking.py:45-49,66-67` (el decorador delega) |
| 7 | Servicio en `:8081` (`eovrt-control serve`), bus de alertas `:5558` | ✅ | `cli.py:128-137`; `config.py:198`; `Dockerfile` `EXPOSE 8081 5558` |
| 8 | CLI `replay` / `live` / `evaluate-alerts` conservada para el camino offline | ✅ | `cli.py:27-107` |
| 9 | `python3.11 -m venv .venv` | ⚠️ | venv real 3.14.4; instrucción válida (`requires-python >=3.11`), deriva declarada |
| 10 | `pytest tests/ -q --ignore=tests/labs` — "tests/labs no tiene numpy" | ✅ | `pyproject.toml:52-58` (addopts ya lo ignora); `tests/labs/` usa el extra `[labs]` |
| 11 | Toda corrida live es re-evaluable offline con artefactos idénticos | ✅ (por construcción) | `runtime/core.py:1-6` (un solo bucle para replay y live); `sources/bus.py:8-9,315-317` (misma validación que JSONL); `tests/test_bus_parity.py` (1 test, marker `integration`) |

### B.2 `docs/13-glosario-y-convenciones-de-lectura.md` §3 / §4 / §6

| # | Afirmación | Veredicto | Evidencia |
|---|---|---|---|
| 12 | CR-01 severidad alta, CR-02 media | ✅ | `cr01_cr02_v2.yaml:16,40` |
| 13 | PR-01/PR-02: confirmación 4000/7000 ms, resolución 2000/3000 ms | ✅ | `cr01_cr02_v2.yaml:32-33,56-57` |
| 14 | control-plane: "motor de patrones con histéresis (`inactive→candidate→confirmed→resolved`)" | ⚠️ **omite `sustained`** | Cinco estados: `engine/pattern_engine.py:18` (`inactive`), `:252-262` (`candidate`/`confirmed`/`sustained`), `:355,447` (`resolved`); `docs/contracts.md:23-29`; en 51 corridas locales: 111 `candidate`, 52 `confirmed`, **48 `sustained`**, 59 `resolved`. Mismo texto de 4 estados copiado en `00-contexto-base.md:729`, que contradice `:1155/:1167` (cinco) del mismo kit |
| 15 | DBE = archivo; EBE = bus ZeroMQ `bus.envelope.v1` msgpack, corrida 1:1, cierre por `run_finished` | ✅ | `sources/bus.py:32-35,246,306-312`; `runtime/core.py:334-339` (`media_run_id` None si mezcló runs); `transport/alert_bus.py:24-27,162-172` |
| 16 | G0 escena = núcleo; G1 sujeto con tracker IoU **como decorador en el control-plane** | ✅ | `config.py:147-150` (default `scene`), `:46-51` (`input.track_persons`, opt-in); `engine/evaluators/spatial_absence.py:144-154` (`state_key`); `sources/tracking.py:1-25,37-142` (`TrackingSource`, un tracker por `source_id`); `runtime/{replay,live}.py` (`maybe_track`) |
| 17 | `t_alert`: "desde que la condición se sostiene hasta que el patrón confirma; ideal medido 4000,0 ms" | ⚠️ | Definición operativa real: `alert.timestamp_ms − episode.start_ms` (`temporal.py:1154,1300`, `avg_latency_ms_from_episode_start`), es decir desde el **inicio anotado del episodio GT** (t0, spec 43 §4.1). Con GT derivado por `derive_clip_gt`, 4000,0 exactos es consistente. Redacción del glosario imprecisa, no falsa |
| 18 | TTFD = ms desde inicio del episodio GT hasta la 1ª detección positiva | ✅ | `temporal.py:548-564` (t0 = `start_ms`, t1 = 1ª positiva dentro de `[start,end]`); criterio positivo = evaluador real por estrategia `:534-545` |
| 19 | SDR = fracción del episodio cubierta por detecciones, clamp 0–1 | ✅ | `temporal.py:567-622` (cobertura en ms con fusión de huecos ≤ paso nominal, clamp) |
| 20 | `re_alerts`: el evaluador las cuenta aparte y NO las penaliza como FP | ✅ | `temporal.py:1139-1144` (candidatas no asignadas), `:1201-1208` (repetición con infracción activa, F2), `:1220-1221` (precision = matched/(matched+unexpected)); tests `test_matching_tolerance_and_realerts.py:108-118`, `test_evaluate_alerts_v2_gate.py:112-171` |
| 21 | Estados de aplicabilidad: `not_applicable/non_temporal_source` | ✅ | `runtime/core.py:149-155`; `metrics/latency.py:46-47`; `temporal.py:667-669,1038-1039` |
| 22 | … `not_interpretable/dbe_media_time` | ✅ | `metrics/latency.py:48-49`; test `tests/test_latency.py:32` |
| 23 | … `not_interpretable/cross_node_monotonic_clock` (two-node) | ❌ **nombre no existe en código** | El control-plane emite `not_interpretable/clock_skew` (`metrics/latency.py:50-51`, `tests/test_latency.py:43-46`); el experimental-setup también `clock_skew` (`webconsole/backend/src/eovrt_webconsole/experiment/applicability.py:115`, `report.py:35`). `cross_node_monotonic_clock` sólo aparece en docs: `ADR-0006` local `:68` y `estado-de-implementacion-adrs.md:343` |
| 24 | … `not_applicable/no_ground_truth` | ⚠️ | No lo emite el control-plane (causas reales de `temporal.py`: `non_temporal_source`, `all_episodes_metric_censored`, `negative_clip_no_episodes`, `no_detections_provided`, `non_v2_ground_truth`). Lo emite `report.py:33,360,376,525` del experimental-setup. El `ADR-0006` local `:41-42` lo atribuye falsamente a `evaluation/temporal.py` |
| 25 | Dos series de ADR; el 0005 local no existe | ✅ | `docs/decisions/` (0001-0004, 0006-0013); nota `ADR-0006:3-12` |
| 26 | `track_id` opcional en `Detection`; modo `subject` funciona; `track_id` post-hoc con `SimpleIoUTracker`; `input.track_persons` lo reproduce exacto | ✅ | `contracts/media.py:12-15`; `tools/track_detections.py` (post-hoc, escribe `track_id`, no `detection_id`, `:14-15`); `sources/tracking.py:88-95,130-137`; corrida `runs/smoke_ebe_b_20260805T003713Z_ff0134/summary.json`: `pattern_set_id: cr01_cr02_v2_subject`, 160 unidades, 2 alertas, `degradation_causes: []` (sin `no_track_id`), `subject_key: CR-01:smoke_ebe:subject_001` |
| 27 | `media.detection.v1` evolución aditiva | ✅ | `contracts/media.py:13-15` (`track_id` aditivo), `:87-129` (backport de campos legacy) |
| 28 | `control.alert.v1` persiste-primero | ✅ | `runtime/core.py:258-272` (`alert_sink.write` antes de `publish`); paridad de bytes JSONL↔bus `tests/test_alert_bus.py:94` |
| 29 | `control.pattern_progress.v1`: progreso 0–1 sólo en `candidate`, no toca la máquina | ✅ | `contracts/pattern.py:61-85`; `pattern_engine.py:279-325` (`if state != "candidate": return None`); test `test_progress_does_not_alter_state_machine_or_alerts` |
| 30 | `clip_gt.v2`: episodios en ms, `negative`, `sub_threshold_events`, `provenance` | ✅ | `temporal.py:61-140` |
| 31 | §6 puertos control :8081, entry point `eovrt-control serve` | ✅ | `cli.py:128-137` |

### B.3 `docs/GUIA-REDACTORES.md` §1

| # | Afirmación | Veredicto | Evidencia |
|---|---|---|---|
| 32 | control-plane "aplica una ventana temporal (no alerta con un solo frame: exige que la condición persista)" | ✅ con matiz | Cierto bajo `cr01_cr02_v2` (4000/7000 ms, `pattern_engine.py:514-521`). **Sobre imágenes o con v1** (`confirm_after_frames: 1`, sin ms) sí confirma en el primer evento; ADR-013 lo declara (`inert_temporal_thresholds`, `runtime/core.py:118-133,149-155`). Redactar "con el pattern set oficial" |
| 33 | alert-distribution "aplica cooldown e idempotencia" (frontera con el motor) | ✅ (lado control) | El motor emite en cada `confirmed` (`pattern_engine.py:197-200`); su `realert_cooldown_*` queda `None` en v2 (`config.py:128-130`; v2.yaml no lo configura) |

### B.4 `docs/informe/project-kit/00-contexto-base.md` (grep)

| # | Línea / afirmación | Veredicto | Evidencia |
|---|---|---|---|
| 34 | `:117` G1 implementada y medida | ✅ (implementación) | ver #16/#26; la cifra 0,930 no es verificable en este repo |
| 35 | `:173-179, :3439-3466` `t_alert-system` citable = `t_alert_system_ms` = passthrough de `avg_latency_ms_from_episode_start` | ✅ | `temporal.py:444,1300`; experimental-setup `report.py:373-409` ("passthrough de `avg_latency_ms_from_episode_start`"). **Matiz clave**: es un **promedio** por corrida; el evaluador no expone percentiles ni las latencias por episodio (v2 no llena `matches`) — ver C.1 |
| 36 | `:242` misma frase que GUIA §1 | ✅ con matiz | ver #32 |
| 37 | `:363` "sin contar `re_alerts`, re-confirmaciones con la infracción todavía activa" | ✅ | `temporal.py:313-341` (`_alert_repeats_matched_episode`: exige posterior al match y ≤ `end_ms + tolerancia`) |
| 38 | `:729` máquina de 4 estados vs `:1155/:1167` cinco estados | ⚠️ **inconsistencia interna del kit** | ver #14 |
| 39 | `:870` pattern set oficial `cr01_cr02_v2` (escena, 4000/7000, sin cooldown ni memoria de cobertura) | ✅ | `cr01_cr02_v2.yaml:6-9`; no hay claves `realert_cooldown_*` ni `coverage_memory_*` |
| 40 | `:1898` ADR-011: "el motor emite todo; el distribuidor aplica cooldown" | ✅ | `pattern_engine.py:197-200,572-586`; ADR-0011 local |
| 41 | `:2510` "el parámetro `realert_cooldown_ms/frames` existe en el motor" (sin uso) | ✅ | `config.py:128-130`; `pattern_engine.py:588-610`; sólo lo configuran `cr01_cr02_temporal_eval.yaml` (fixture) y el archivado `field_v1` |
| 42 | `:2606` "`control.alert.v1` no tiene `confirmed_at_ms`" | ✅ | `contracts/alerts.py:10-41` (tiene `timestamp_ms` de fuente, `alert_registered_ms` monotónico, `first_evidence_ms`) |
| 43 | `:1889-1898` filas ADR (copia de estado-adrs) | ver B.5 | — |

### B.5 `docs/decisiones/estado-de-implementacion-adrs.md` (filas 002, 006, 007, 008, 011, 012, 013)

| ADR | Dice el doc | Veredicto | Evidencia |
|---|---|---|---|
| 002 | G0 implementado (gate F1=1.0); G1 implementado como decorador de fuente, medido F1 0,930 | ✅ impl. / cifra no verificable acá | `config.py:150`; `spatial_absence.py:144-154,191-205` (fallback a escena con causa `no_track_id`); `sources/tracking.py`; tests `test_tracking_source.py` (18), `test_track_detections.py` (8) |
| 006 | Cada métrica declara aplicabilidad con causa; two-node resuelto "declarativa (`not_interpretable/cross_node_monotonic_clock`, doc 39)" (`:343`) | ✅ vocabulario / ❌ **nombre de causa** | `contracts/metrics.py:10-15` (4 estados cerrados); `runtime/core.py:136-156`; `temporal.py:1231-1257`; `metrics/latency.py:29-60`. La causa real es `clock_skew` (`latency.py:51`) |
| 007 | Corrida live 1:1, cierra por `run_finished`; verificado E2E | ✅ | `sources/bus.py:306-312`; `runtime/core.py:337-339`; `transport/alert_bus.py:162-172` (END en `finally`, `core.py:307-312`); `tests/test_service_live.py` (3), `test_live.py` (5) |
| 008 | Servicio HTTP mínimo :8081, "11 endpoints vs los 3 decididos" | ⚠️ **son 12** | `grep @router` → 12 decoradores (`health.py:10,15`; `runs.py:21,36,42,50,59,74,84,96,110`; `config.py:12`). El ADR-0008 local `:47-49` también dice 11 |
| 011 | Motor emite en cada confirmación; cooldown/supresión en distribución | ✅ | `pattern_engine.py:197-200`; único gate `_maybe_alert/_cooldown_ok` (`:572-610`) inactivo con `None` (default `config.py:129-130`); v2 sin cooldown; evaluador `re_alerts` (`temporal.py:1139-1144,1201-1208`) |
| 012 | Memoria de cobertura ignorada bajo G0 con causa; falsación superada | ✅ | `pattern_engine.py:45-49` (`_memory_applicable` exige `subject`), `:156-158` (causa `coverage_memory_unsupported_scene`); tests `test_pattern_engine.py:295,312,326,516` |
| 013 | Detecta temporalidad de la fuente y declara no-aplicabilidad; "137 eventos / 0 alertas sobre imágenes" | ✅ impl. / cifra no verificable | `runtime/core.py:103-156`: causas `non_temporal_source`, `persistence_unreachable_on_non_temporal_source` (frames>1), `inert_temporal_thresholds` (ms ignorados), `mixed_source_types`, `no_units_processed`; el input original de 137 eventos fue podado (`configs/_archive/fase0_dbe_gdino_bench_rerun.yaml:8-13`) |

### B.6 `docs/informe/figuras/README.md` — FIG-E (máquina de estados)

| # | Afirmación | Veredicto | Evidencia |
|---|---|---|---|
| 44 | Cinco estados `inactive → candidate → confirmed → sustained → resolved` | ✅ | `pattern_engine.py:18,252-262,355,447`; `docs/contracts.md:23-29`; transiciones medidas en `runs/*/pattern_events.jsonl`: inactive→candidate 71, candidate→confirmed 52, confirmed→sustained 48, candidate→resolved 41, **resolved→candidate 40**, sustained→resolved 14, confirmed→resolved 4; **inactive→confirmed 0, resolved→inactive 0** |
| 45 | La alerta se emite en la transición de entrada a `confirmed`; `sustained` no produce cambio nuevo ni multiplica alertas | ✅ | `pattern_engine.py:197-200` (alerta sólo si `change.state == "confirmed"`); `:261-265` (sustained→sustained devuelve `None`) |
| 46 | Reapertura `resolved → candidate` (no a `inactive`; `inactive` sólo inicial) | ✅ | `pattern_engine.py:229-233,252-257` (desde `resolved` reinicia `hit_count`/`first_hit` y pasa a `candidate` porque `elapsed=0 < confirm_after_ms`); ningún camino asigna `"inactive"` |
| 47 | Salto directo `inactive/resolved → confirmed` "si la condición ya se cumple en el primer evento" | ✅ con matiz | `pattern_engine.py:252-257` — sólo cuando rige el camino por frames (`confirm_after_ms` None o `timestamp_ms` None, i.e. imágenes/v1); con v2 sobre video **nunca ocurre** (0 casos en 51 corridas) |
| 48 | A `resolved` por dos caminos (despeje sostenido o expiración por ausencia) | ✅ | `_advance_clear` `:327-388` (≥ `resolve_after_ms` de despeje) y `_expire_absent_subjects` `:416-485` (`subject_absent_timeout_*`, reinterpretado a escena, ADR-012 §3). Nota: también desde `candidate` (41 casos), lo que el script de la figura dibuja (`docs/informe/figuras/scripts/fig_e_maquina_de_estados.py`, flechas desde candidate/confirmed/sustained a resolved) |

### B.7 Hechos puntuales

| Hecho | Veredicto | Evidencia |
|---|---|---|
| ADR-011: el motor emite en cada confirmación y NO tiene cooldown | ✅ como "capacidad desactivada" | Sí existe código de cooldown (`pattern_engine.py:578-610`, `config.py:128-130`) pero es opt-in y `cr01_cr02_v2` no lo configura; no hay otra supresión (`_maybe_alert` es el único gate). Redactar: "el motor no aplica cooldown" (no "no tiene") |
| `re_alerts` existen y no cuentan como FP | ✅ | `temporal.py:429,1139-1144,1201-1221`; 3 tests dedicados |
| Cinco hitos por alerta: cuáles persiste el control-plane | 4 de 5, con dos relojes | (1) primera evidencia: `first_evidence_ms` monotónico + `first_evidence_unit_id/frame_index` (`pattern_engine.py:238-241`, `alerts.py:36-38`) ✅ · (2) candidato: `pattern_events.jsonl` `state=candidate` con `timestamp_ms`/`frame_index` **de fuente** + `unit_id` (`pattern.py:31-58`); el instante de recepción monotónico se reconstruye por join `unit_id → metrics.jsonl.ts_receive_ms` (`core.py:279-294`) ⚠️ indirecto · (3) confirmado: idem `state=confirmed` ⚠️ indirecto · (4) alerta registrada: `alert_registered_ms` monotónico (`pattern_engine.py:638`) ✅ · (5) notificación: ❌ no en este repo (módulo de distribución). Derivado: `ttfa_internal_ms_percentiles` = registrada − 1ª evidencia, P50/P95/P99 (`core.py:273-277,353`), etiquetado "diagnóstico" (`metrics.py:55-57`) |
| Percentiles P50/P95/P99 vs promedio | ⚠️ mixto | `summary.json`: `processing_ms_percentiles` y `ttfa_internal_ms_percentiles` P50/P95/P99 (`metrics/latency.py:5-26`), `avg_processing_ms` ✅; `ttfa_internal` **sin promedio**. `evaluate-alerts`: **sólo promedios** (`avg_latency_ms_from_episode_start`, `avg_ttfd_ms`, `avg_sdr`, `temporal.py:745-746,1300`); por-episodio sólo para TTFD/SDR (`ttfd_by_episode`, `sdr_by_episode`), **no para t_alert** (la lista `latencies` no se persiste; `matches` sólo se llena en v1) |
| Aplicabilidad `not_applicable:<causa>` (ADR-006/013) | ✅ | Vocabulario cerrado `contracts/metrics.py:14`; formato `"<estado>:<causa>"` en `ttfd_sdr_applicability` (`temporal.py:463-467`), pareja `applicability_state/cause` para la evaluación (`:442-443`); `RunSummary.pattern_evaluation` (`metrics.py:70-73`) |
| Severidades `high`/`medium` | ✅ / ⚠️ | v2: CR-01 `high`, CR-02 `medium`; v1 tenía CR-01 `medium` (deprecado). `PatternDefinition.severity: str = "medium"` (`config.py:144`) **sin vocabulario cerrado** (no valida los 3 niveles del protocolo) |
| Persistencia en ms; `confirm_after_frames` como fallback/diagnóstico | ✅ | `pattern_engine.py:508-521` (ms si hay `timestamp_ms`, si no frames); `runtime/core.py:103-133` declara frames>1 como inalcanzable y ms como inertes sobre imágenes (ADR-013) |
| Unidad de conteo del FP | ✅ declarada | **Evento de alerta** (`AlertEvent`) fuera de toda ventana de matching de episodio, fuera de `sub_threshold_events` y que no repite un episodio matcheado (`temporal.py:1173-1221`); `far_per_hour` = FP con timestamp / horas observadas (`:1268-1280`); alertas sin timestamp cuentan en `unexpected` pero no en FAR (`:1183-1193`) |
| Modo `subject` (G1) funciona | ✅ | ver #26; `smoke_ebe_b` live sin `no_track_id` |
| Puertos 8081 y 5558 | ✅ | `cli.py:130`; `config.py:198`; Dockerfile |

---

## C) Divergencias doc↔código, por gravedad

### Alta (afectan cifras o afirmaciones metodológicas del informe)

| # | Qué dice el doc | Qué hay | Corregir y dónde |
|---|---|---|---|
| C.1 | Protocolo §17.1.7.8.1: métricas temporales "como mínimo P50, P95 y P99, además del promedio". El kit (`00-contexto-base.md:173-179`) declara `t_alert-system` citable | `evaluate-alerts` produce **sólo promedios**: `avg_latency_ms_from_episode_start` (`temporal.py:1300`), `avg_ttfd_ms`/`avg_sdr` (`:745-746`); no persiste las latencias por episodio de t_alert (v2 deja `matches=[]`) ⇒ los percentiles no se pueden recomputar desde la salida del evaluador. El experimental-setup lo pasa tal cual (`report.py:389-409`) | O bien (a) extender `TemporalAlertEvaluation` con `latency_ms_by_episode` + percentiles (cambio aditivo en `temporal.py`), o (b) el informe cita `t_alert-system` explícitamente como **promedio por campaña con n** y declara la ausencia de percentiles como desvío del protocolo. `summary.json` sí cumple (P50/P95/P99) pero para `processing_ms`/`ttfa_internal`, no para t_alert-system |
| C.2 | Protocolo §17.1.7.5.5 / §17.1.7.8.3: Precision/Recall **por severidad** con n, criterio de agrupamiento y punto operativo | `evaluation/temporal.py` no usa `severity` en ningún lugar (grep vacío); precision/recall/F1 son agregados por clip sobre CR-01+CR-02 juntos. El desglose por condición (≡ severidad, 1:1) existe sólo aguas abajo (tablas CR-01/CR-02 del índice de resultados del experimental-setup) | Informe: citar P/R por severidad desde el desglose por condición del experimental-setup (`results/clip_bench/`), no del control-plane; declarar que el evaluador del plano agrega por clip. Opcional: agregar `by_condition` a `TemporalAlertEvaluation` |

### Media (contradicciones entre documentos o doc↔código en nombres)

| # | Qué dice el doc | Qué hay | Corregir y dónde |
|---|---|---|---|
| C.3 | Glosario `13` §3 fila control-plane y `00-contexto-base.md:729`: histéresis `inactive→candidate→confirmed→resolved` (4 estados) | 5 estados con `sustained` (`pattern_engine.py:261-262`, `contracts.md:28`; 48 eventos `sustained` en corridas locales). El propio kit dice cinco en `:1155/:1167` y `figuras/README.md:115` | Actualizar la fila del glosario 13 §3 (`docs/13-glosario…md`) y regenerar el kit (`herramientas/generar_project_kit.py`) para que `:729` diga los cinco |
| C.4 | `ADR-0006` local `:68`, `estado-de-implementacion-adrs.md:343`, glosario §3: causa two-node `not_interpretable/cross_node_monotonic_clock` | Código: `not_interpretable/clock_skew` (`metrics/latency.py:50-51`; `tests/test_latency.py:43-46`; experimental-setup `applicability.py:115`, `report.py:35`) | Corregir el nombre en los tres docs (o documentar `cross_node_monotonic_clock` como sinónimo del doc 39 no materializado). En el informe usar `clock_skew` |
| C.5 | `ADR-0006` local `:41-42`: "`evaluation/temporal.py` declara `not_applicable:no_ground_truth` sin GT" | `temporal.py` no emite esa causa; la emite `report.py:33,360,376,525,698-700` del experimental-setup | Corregir "Cableado en este repo" del `ADR-0006` local |
| C.6 | Protocolo §17.1.7.8.3: hito de cierre de t_alert-system = "registro interno de la alerta" | El evaluador usa `alert.timestamp_ms` (tiempo de **fuente** del frame que confirmó, `temporal.py:1154`), no `alert_registered_ms` (monotónico del host, no comparable con el GT en ms de video). En DBE la diferencia es `processing_ms` (~0,2 ms, `summary.json`); en EBE incluye la cola del bus (no medida por esta métrica) | Declarar en el informe: t_alert-system se mide en el reloj del material (frame de confirmación); el registro interno queda en `alert_registered_ms` y se reporta aparte como `ttfa_internal` (P50/P95/P99) |
| C.7 | `ADR-0008` local `:47-49` y `estado-adrs:27`: "11 endpoints" | 12 decoradores (`health.py:10,15`; `runs.py` ×9; `config.py:12`) | Corregir a 12 (o "12 rutas / 11 recursos" si se cuenta GET+DELETE de `/runs/{id}` como uno) |

### Baja (precisión, higiene documental)

| # | Qué dice / qué hay | Corregir |
|---|---|---|
| C.8 | `temporal.py:679` etiqueta `positive_criterion = "spatial_absence(<set>) >=1 evidencia"` **hardcodeada**, pero el criterio despacha por estrategia (`evaluate_pattern`, `:545`) — en evals de `edir_v1`/`hyb_or_v1` la etiqueta es engañosa | Derivar la etiqueta de `pattern.evidence.strategy` |
| C.9 | `PatternDefinition.severity: str` sin enum (`config.py:144`); el protocolo define crítico/alto/medio | Restringir a `Literal["critical","high","medium"]` o documentar la libertad |
| C.10 | README `:74` "pattern set oficial y ÚNICO vigente es `cr01_cr02_v2`… `v1` se conserva sólo como fixture" no menciona los 4 sets de campaña (`v2_subject`, `edir_v1`, `hyb_or_v1`, `bare_head_v1`) ni `input.track_persons`; `configs/_archive/README.md` §"Activos" también los omite | Añadir párrafo "pattern sets de campaña (variable única vs v2)" al README y a `_archive/README.md` |
| C.11 | `docs/architecture.md:53` describe el cooldown como mecanismo del ciclo sin remitir a ADR-0011 en esa línea (README y v2.yaml sí lo hacen) | Añadir "no usado por la plataforma (ADR-0011)" |
| C.12 | Memoria de sesión (`project_control_plane.md`): "el motor NO tiene cooldown" | Precisar: capacidad presente, desactivada por default y no configurada en v2 |
| C.13 | `RunSummary.ttfa_internal_ms_percentiles` sin promedio (`core.py:353`), mientras el protocolo pide promedio + percentiles | Aditivo: `avg_ttfa_internal_ms` |
| C.14 | Glosario §6 "Repos de código" omite `e-ovrt_alert-distribution` (fuera de este repo) | Añadir |
| C.15 | `alert_bus.wait_for_subscriber_ms` default 0 (`config.py:200`): con `alert_bus.enabled: true` y sin espera, las primeras alertas pueden perderse si el distribuidor se suscribe tarde (XPUB no reintenta). Los templates `experiments/t_alert_notification/*/control.template.yaml` habilitan el bus; la corrida `control_ebe_oakd_live_20260818T002810Z` usó 500 ms | Documentar el valor recomendado en README/plataforma |

---

## D) Protocolo §17.1 vs construido

Fuente del protocolo: `scratchpad/17-1-full.md` (§17.1.3.2, §17.1.5.3, §17.1.7.2, §17.1.7.5, §17.1.7.7.6, §17.1.7.8).

| § | Prescripción | Estado | Evidencia / qué falta |
|---|---|---|---|
| 17.1.3.2 | Cadena detección → evento → motor → confirmación → registro de alerta → disponibilidad → humano; sólo `confirmed` registra alerta | **CUMPLIDA** | `runtime/core.py:217-300` (bucle), `pattern_engine.py:197-200` (alerta sólo en `confirmed`), `sinks/jsonl` + `GET /api/runs/{id}/alerts` + bus `:5558` (disponibilidad) |
| 17.1.5.3.1 | Patrón = condición + persistencia + severidad, declarativo; motor separado del detector | **CUMPLIDA** | `config.py:138-153` (`PatternDefinition` YAML: `condition_id`, `severity`, `timing`, `region`, `evidence.strategy`); el motor no infiere (`ADR-0001`) |
| 17.1.5.3.2 | Tres niveles de severidad (crítico/alto/medio) | **CUMPLIDA (parcial)** | `high` (CR-01) y `medium` (CR-02) en v2; `critical` **NO EJERCIDA** (sin PR-03…06, exclusiones E-xx); campo `severity` sin enum (C.9) |
| 17.1.5.3.3 | Persistencia en **segundos**, no frames; alto 3–5 s, medio 5–10 s | **CUMPLIDA** | `confirm_after_ms` 4000 (∈ 3–5 s) / 7000 (∈ 5–10 s) rige cuando hay `timestamp_ms` (`pattern_engine.py:514-520`); frames sólo fallback (`:521`) y declarado inerte/inalcanzable sobre imágenes (`core.py:103-133`) |
| 17.1.5.3.3 | "Sostenida — o con una proporción mínima de detecciones positivas dentro de la ventana" | **DESVIADA (variante declarada)** | El motor implementa **duración desde la primera evidencia con tolerancia a huecos** < `resolve_after_ms` (un frame limpio no reinicia `first_hit_timestamp_ms`; sólo `resolve_after_ms` de despeje continuo resuelve, `pattern_engine.py:327-348,523-536`), no una proporción de frames positivos. Equivale a "sostenida con histéresis"; conviene declararlo así en §17.3/17.4 |
| 17.1.5.3.3 | Histéresis: umbral de activación ≠ desactivación | **CUMPLIDA** | 4000/2000 y 7000/3000 (`cr01_cr02_v2.yaml:32-33,56-57`); `_confirmation_met` vs `_resolution_met` (`pattern_engine.py:508-536`); test `test_hysteresis_absorbs_epp_flicker_without_coverage_memory`, `test_cr01_cr02_v2_scene_flicker_within_resolve_window_does_not_realert` |
| 17.1.5.3.3 | Calibración empírica de la curva FP vs duración de ventana | **NO EJERCIDA (en este repo)** | Umbrales fijados por Tabla 24/D.4 (ADR-0010 "plataforma primero"); no hay barrido de `confirm_after_ms` en configs activas (los probes con otros timings están en `configs/_archive/`) |
| 17.1.5.3.4 | Estados inactivo / candidato / confirmado / resuelto | **CUMPLIDA (+ `sustained` aditivo)** | `pattern_engine.py:18,252-262,355`; `contracts.md:23-29` |
| 17.1.5.3.4 | Nivel 1 sin MOT obligatorio; MOT si se atribuye a persona individual | **CUMPLIDA** | G0 escena por default (`config.py:150`); G1 opt-in con tracker IoU (`sources/tracking.py`) |
| 17.1.5.3.4 | Histéresis "evita alertas repetidas sobre una misma situación" | **DESVIADA (deliberada, ADR-011)** | El motor **sí** re-alerta en cada re-confirmación tras resolver (`re_alerts`); la supresión se movió a distribución. Dentro de un episodio no hay repetición (`sustained` no emite). Declarar en el informe |
| 17.1.5.3.5 | Tabla 24: PR-01 alto 3–5 s, PR-02 medio 5–10 s | **CUMPLIDA** | ver arriba; PR-03…PR-06 **NO EJERCIDOS** |
| 17.1.5.3.7 | Criterios de activación/desactivación configurables; tratamiento de pérdidas de track | **CUMPLIDA** | timing por YAML; `subject_absent_timeout_*` (`pattern_engine.py:416-506`); degradación `no_track_id` a escena (`spatial_absence.py:191-197`) |
| 17.1.7.2 | t_alert-system = inicio anotado del evento → alerta registrada tras evaluación del patrón | **CUMPLIDA (reloj de fuente)** | `temporal.py:1154` (`alert.timestamp_ms − episode.start_ms`); ver C.6 |
| 17.1.7.5.1 | t_alert-system sólo con detección + evaluación + confirmación + registro interno; en frame-a-frame declarar no aplicación | **CUMPLIDA** | El evaluador sólo lee `alerts.jsonl` (registro interno); `not_applicable:non_temporal_source` (`temporal.py:1022-1046`); `RunSummary.pattern_evaluation` (`core.py:136-156`) |
| 17.1.7.5.1 | t_alert-notification complementaria si hay trayecto instrumentado | **FUERA DE ESTE REPO** | Módulo de distribución (`:5558` → MQTT); el control-plane sólo publica (`transport/alert_bus.py`) |
| 17.1.7.5.2 | TTFD: inicio anotado → 1ª detección positiva válida; criterio declarado | **CUMPLIDA** | `temporal.py:548-564`; criterio = evaluador real de la estrategia del patrón (`:534-545`), campo `positive_criterion` (`:468-470`; etiqueta con bug C.8); no aplicable declarado (`:632-673`) |
| 17.1.7.5.3 | SDR: proporción del intervalo anotado con detecciones positivas; criterio tiempo vs frames declarado | **CUMPLIDA** | `temporal.py:567-622` (en **tiempo**, ms; fusión de huecos ≤ paso nominal, documentado en docstring) |
| 17.1.7.5.4 | Métricas temporales sólo sobre secuencias; no sobre imágenes | **CUMPLIDA** | ADR-013 `core.py:149-155`; `temporal.py:667-669,1022-1046` |
| 17.1.7.5.5 | Precision/Recall **por severidad** con n | **PARCIAL (no en este repo)** | `temporal.py` no usa `severity`; agregado por clip. Desglose por condición sólo en el experimental-setup (C.2) |
| 17.1.7.7.6 | Umbrales por severidad (Tabla D.4) | **CUMPLIDA (no verificable la tabla)** | `DEFAULT_MATCHING_WINDOWS` CR-01 4000/10000, CR-02 7000/20000 (`temporal.py:151-160`) dice citar Tabla D.4; el Anexo D no está en `17-1-full.md` |
| 17.1.7.8.1 | Declarar modelo, checkpoint, resolución, umbrales, ventana de persistencia, tracker | **CUMPLIDA (su parte)** | `effective_config.yaml` por corrida (`sinks/artifacts.py:51-54`: pattern set, timings, `track_persons`, `alert_bus`); modelo/resolución/NMS son del media-plane (`media.detection.v1` trae `model.name`, `prompts.prompt_set_id`) |
| 17.1.7.8.1 | Timestamps monotónicos, fuente declarada | **CUMPLIDA** | `alert_registered_ms`, `first_evidence_ms`, `ts_receive_ms` = `time.monotonic()` (`pattern_engine.py:638`, `bus.py:333`); `timestamp_ms` = reloj de fuente; join con `source_clock` en `metrics/latency.py:29-60` |
| 17.1.7.8.1 | Cinco hitos: 1ª evidencia, candidato, confirmado, registro, notificación | **PARCIAL (4/5)** | 1ª evidencia ✅ y registro ✅ directos y monotónicos; candidato y confirmado ⚠️ en `pattern_events.jsonl` con tiempo de fuente (monotónico reconstruible vía `unit_id`→`metrics.jsonl.ts_receive_ms`); notificación ❌ fuera del repo |
| 17.1.7.8.1 | Período de calentamiento previo | **NO EJERCIDA (en este repo)** | Sin warm-up en el control-plane (grep `warm` vacío); el motor cuesta ~0,2 ms/unidad (`summary.json` `processing_ms_percentiles` p95 0,36 ms). El warm-up relevante es del media-plane |
| 17.1.7.8.1 | P50/P95/P99 + promedio | **PARCIAL** | `summary.json` ✅ (processing, ttfa_internal; ttfa sin promedio); `evaluate-alerts` ❌ sólo promedios (C.1) |
| 17.1.7.8.1 | GT inexistente ⇒ declarar no ejecutada, no aproximar | **CUMPLIDA** | `not_applicable:*`, censura `metric_censored` (`temporal.py:249-268,1157-1170,1231-1263`), clip negativo declarado no evaluable (`:1238-1257`) |
| 17.1.7.8.2 | No medir MOT sin GT de identidades | **CUMPLIDA** | No hay métricas MOT en el repo (E-10); tracker sólo produce `track_id` |
| 17.1.7.8.2 | No medir t_alert-system sin evaluación de patrón ni registro | **CUMPLIDA** | ídem 17.1.7.5.1 |
| 17.1.7.8.3 | Unidad de conteo del FP declarada antes de medir e idéntica entre corridas comparativas | **CUMPLIDA** | Unidad = evento de alerta fuera de ventanas/sub-umbral/re-alert (`temporal.py:1173-1221`), fijada por spec 43/ADR-0011, invariante entre campañas |
| 17.1.7.8.3 | TTFD: 1ª evidencia ≠ alerta confirmada; criterio estable y registrado | **CUMPLIDA** | `positive_criterion` en la salida (`temporal.py:468-470,679`); TTFD independiente de alertas |
| 17.1.7.8.3 | Hito de cierre de t_alert definido antes; logs que reconstruyan 1ª evidencia → candidato → confirmado → registro | **CUMPLIDA (con C.6)** | `alerts.jsonl` (registro + `first_evidence_*`), `pattern_events.jsonl` (candidate/confirmed/sustained/resolved), `metrics.jsonl` (`ts_receive_ms` por unidad) |
| 17.1.7.8.3 | SDR: criterio tiempo vs frames declarado; privilegiar tiempo si el throughput es inestable | **CUMPLIDA** | En tiempo (ms), `temporal.py:573-584` |
| 17.1.7.8.3 | P/R por severidad con n, agrupamiento y punto operativo | **PARCIAL (no en este repo)** | C.2 |
| 17.1.7.8.4 | Bitácora mínima por corrida; logs crudos y trazabilidad | **CUMPLIDA** | `effective_config.yaml`, `summary.json` (`started_at/finished_at`, `warnings`, `degraded`, `degradation_causes`, `pattern_evaluation`), JSONL append-only (`ADR-0003`) |

---

## E) Hechos citables (con comando de re-verificación)

Todos los comandos desde `/home/simonll4/projects/e-ovrt_control-plane`.

1. **Pattern set oficial** `cr01_cr02_v2`: CR-01 `high`, `confirm_after_ms 4000`, `resolve_after_ms 2000`; CR-02 `medium`, `7000`/`3000`; `granularity: scene`; sin cooldown ni memoria de cobertura.
   `grep -n -E 'severity|confirm_after_ms|resolve_after_ms|granularity|cooldown|memoria' configs/patterns/cr01_cr02_v2.yaml`
2. **Máquina de estados de cinco estados** `inactive → candidate → confirmed → sustained → resolved`, reapertura `resolved → candidate`, alerta sólo al entrar a `confirmed`.
   `grep -n -E '"(inactive|candidate|confirmed|sustained|resolved)"' src/eovrt_control/engine/pattern_engine.py` · transiciones observadas: `cat runs/*/pattern_events.jsonl | python3 -c "import sys,json,collections;c=collections.Counter((json.loads(l)['previous_state'],json.loads(l)['state']) for l in sys.stdin if l.strip());print(dict(c))"`
3. **ADR-011 materializado**: el motor emite `AlertEvent` en cada transición a `confirmed`; el cooldown `realert_cooldown_*` es opt-in (`None` por default) y v2 no lo configura.
   `grep -n -E 'state == "confirmed"|realert_cooldown' src/eovrt_control/engine/pattern_engine.py src/eovrt_control/config.py configs/patterns/cr01_cr02_v2.yaml`
4. **`re_alerts` no son FP**: `precision = matched / (matched + unexpected)`; re-alerts y sub-umbral fuera del denominador; FP = evento de alerta fuera de toda ventana de episodio.
   `sed -n '1139,1144p;1201,1221p' src/eovrt_control/evaluation/temporal.py`
5. **Ventanas de matching** (spec 43 / Tabla D.4): CR-01 `[start+4000, start+10000]`, CR-02 `[start+7000, start+20000]`, con prioridad caller > `provenance.pattern_set_ms` del GT > defaults.
   `sed -n '151,160p;175,197p' src/eovrt_control/evaluation/temporal.py`
6. **t_alert-system** (`avg_latency_ms_from_episode_start`) = `alert.timestamp_ms − episode.start_ms`, **promedio** por corrida, sin percentiles.
   `grep -n -E 'latencies|avg_latency_ms_from_episode_start' src/eovrt_control/evaluation/temporal.py`
7. **Aplicabilidad**: vocabulario cerrado `computed | applicable_not_computed | not_applicable | not_interpretable`; causas del motor sobre imágenes `non_temporal_source`, `persistence_unreachable_on_non_temporal_source`, `inert_temporal_thresholds`; two-node = `clock_skew`.
   `sed -n '10,15p' src/eovrt_control/contracts/metrics.py; sed -n '136,156p' src/eovrt_control/runtime/core.py; sed -n '46,51p' src/eovrt_control/metrics/latency.py`
8. **Hitos persistidos por alerta**: `first_evidence_ms`/`first_evidence_unit_id`/`first_evidence_frame_index` y `alert_registered_ms` (monotónicos), `timestamp_ms`/`frame_index` (fuente); `ttfa_internal_ms_percentiles` P50/P95/P99 en `summary.json`.
   `sed -n '10,41p' src/eovrt_control/contracts/alerts.py; grep -n ttfa_internal src/eovrt_control/runtime/core.py`
9. **Bus**: SUB `:5557` (`media.detection.v1.`, `run.lifecycle.v1.`), huecos de `seq` → `bus_dropped_events` → `degraded`; XPUB `:5558` `control.alert.v1` apagado por default; END `run_finished` en `finally`.
   `sed -n '336,365p' src/eovrt_control/sources/bus.py; sed -n '194,201p' src/eovrt_control/config.py; sed -n '307,319p' src/eovrt_control/runtime/core.py`
10. **G1 como decorador de fuente** (`input.track_persons`), un tracker por `source_id`, DBE y EBE por igual; degradación `no_track_id` a escena si falta identidad.
    `sed -n '46,51p' src/eovrt_control/config.py; sed -n '144,154p;191,197p' src/eovrt_control/engine/evaluators/spatial_absence.py; python3 -c "import json;print(json.load(open('runs/smoke_ebe_b_20260805T003713Z_ff0134/summary.json'))['degradation_causes'])"`
11. **Servicio HTTP**: 12 endpoints, un run activo por vez (409), 201 de `live` implica `BusSource` suscripto.
    `grep -n -E '@router\.' src/eovrt_control/service/routers/*.py; sed -n '108,114p' src/eovrt_control/service/run_manager.py`
12. **Tests**: 312 recolectados (núcleo).
    `.venv/bin/python -m pytest tests/ --ignore=tests/labs --collect-only -q 2>/dev/null | grep -c '::'`
13. **Estado git**: `feature/control-service` @ `64cc976` (2026-08-19), limpio.
    `git status --short | wc -l; git log -1 --format='%h %ci %s'`
14. **Imagen Docker**: `python:3.11-slim`, sólo núcleo, `EXPOSE 8081 5558`, healthcheck `/healthz`.
    `sed -n '13,36p' infra/docker/Dockerfile`

---

## F) No pude verificar (fuera de alcance, sólo lectura, o sin insumo)

- **Cifras experimentales** citadas en los docs (F1 0,930 G1 / 0,789 T1; t_alert 5.236/5.327 ms; confirmaciones live 4,1–4,6 s del doc 91; "137 eventos / 0 alertas" del doc 33): viven en `e-ovrt_experimental-setup/results/` y `docs/operacion/`; el input del doc 33 fue podado (`configs/_archive/fase0_dbe_gdino_bench_rerun.yaml:8-13`).
- **Tabla D.4 del Anexo D** (techos `t_alert_max_ms` 10 s / 20 s y umbrales TTFD por severidad): no está en `17-1-full.md`; sólo verificado que el código dice citarla (`temporal.py:151-160`).
- **Suite completa**: no ejecutada (restricción); sólo `--collect-only` (312). Los tests `integration` (`test_bus_parity`, `test_alert_bus_integration`) usan ZeroMQ real en localhost.
- **Build y smoke Docker**: nunca ejecutados (pendiente declarado en CLAUDE.md raíz y `docs/progress.md`).
- **Lado distribución del orden de arranque** (`POST :8082` primero) y `t_alert-notification` p95 64,534 ms: repo `e-ovrt_alert-distribution`.
- **Desglose P/R por condición/severidad aguas abajo**: no leí el agregador del clip bench del experimental-setup; sólo confirmé que el control-plane no lo produce.
- **Paridad replay↔live byte a byte** sobre corridas reales: sólo verificada por construcción y por el test `test_bus_parity.py` (no ejecutado).
- **Rendering de FIG-E**: leí el script generador (flechas desde candidate/confirmed/sustained a resolved, reapertura a candidate, salto inactive→confirmed), no el PNG/SVG.
