# Relevamiento técnico — `e-ovrt_experimental-setup` (2026-08-28, solo lectura)

Auditoría del repo contra (i) `CLAUDE.md` del workspace, (ii) `docs/informe/project-kit/00-contexto-base.md`,
(iii) `docs/GUIA-REDACTORES.md`, (iv) `docs/13-glosario-…`, (v) `docs/operacion/128`, (vi)
`docs/decisiones/estado-de-implementacion-adrs.md`, y (vii) el protocolo §17.1 del informe
(`scratchpad/17-1-full.md`). Rutas absolutas bajo `/home/simonll4/projects/` salvo indicación.
Abreviaturas: `ES` = `e-ovrt_experimental-setup`, `DOCS` = `docs`.

---

## A) Estado del repo

| Ítem | Valor | Evidencia |
|---|---|---|
| Rama | `feature/webconsole-consola-tesis` | `git branch --show-current` |
| HEAD | `2bfb268b83b1c0c286b3c2af354a4fdc87e24946` — 2026-08-22 03:34:52 +0000 — `feat(finetuning): constancias del cierre T2 y driver offline reproducible` | `git log -1` |
| Working tree | **limpio** (0 líneas en `git status --short`) | — |
| Remote | `origin git@github.com:simonll4/e-ovrt_experimental-setup.git` | coincide con `CLAUDE.md` |
| `CLAUDE.md` propio | **NO existe** (`wc: CLAUDE.md: No such file`). El README (252 líneas) hace ese papel | — |
| Venv canónico `.venv` | Python **3.11.15** (`.venv/bin/python3.11`) | coincide con `requirements-dev.txt` / CLAUDE.md |
| Venv del BFF `webconsole/backend/.venv` | Python **3.14.4** | coincide con CLAUDE.md ("deriva declarada") |
| Tests `tests/` (collect-only) | **88 collected** | coincide con "88 passed" |
| Tests `finetuning/tests/` | **46 collected** | coincide con "46 passed" |
| Tests `webconsole/backend` | **668 collected** | ✗ los docs dicen **643** (README §3 bis:113-115, `requirements-dev.txt`:18-21, CLAUDE.md) — desfasado desde 08-18/20 (commits `14f9e01`, `288c5dd`) |
| Compose `infra/platform/docker-compose.yml` | YAML válido; **13 servicios** (mosquitto, control-plane, distribution, console + 9 `mp-*` en profile `models`) | `python3 -c "yaml.safe_load…"` → 13 |
| `infra/platform/.env` | existe, gitignorado (`.gitignore`:1); define `EOVRT_WORKSPACE` y `COMPOSE_PROFILES` | — |
| `runs/` en la raíz | 339 directorios `exp_*`/`control_talert_*`, gitignorados (`.gitignore`:2) — son los consolidados ADR-004/014 | `ls runs \| wc -l` |
| `cameras/` | gitignorado (`.gitignore`:6); 3 archivos (`oak_d_lab.yaml`, `rtsp_dvr_1.yaml`, backup bootloader) | — |
| `results/evidence-runs/` | gitignorado (`.gitignore`:16); `evidence-runs.md`/`.yaml` versionados | — |
| `defensa/videos/` | 5 mp4 (V1, V3, VG1, VG1e, VG1_lado_a_lado), gitignorados | — |
| Últimos 40 commits | 2026-07-23 → 2026-08-22; hitos: `3d7dad5` freeze `cr01_cr02_v2_short` (07-23), `159167b` freeze `edir_v1`/`eind_v1` (07-29), `1acd19f`…`ab2d809` campañas clip bench (08-03→05), `86c8793` estrato B (08-09), `42529e2`/`13c801e` distribución (08-13), `14f9e01` HTTP default ADR-019/020 (08-18), `0822413` compose integral (08-20), `2bfb268` cierre T2 (08-22) | `git log -40` |

---

## B) Afirmaciones verificadas

Leyenda: ✅ coincide · ⚠ coincide con matiz · ✗ divergente.

### B.1 `CLAUDE.md` del workspace

| Afirmación | Veredicto | Evidencia (ruta:línea) |
|---|---|---|
| El repo NO es un plano; contiene `prompts/`, `experiments/`, webconsole (React+FastAPI BFF), `cameras/` gitignorado, `infra/` | ✅ | árbol del repo; `.gitignore`:6 |
| `prompts/` incluye `cr01_cr02_v2_short` congelado para rodaje y bench | ✅ | `prompts/cr01_cr02_v2_short.yaml`:9-13 (`status: frozen`, `frozen_sha256: df81fd48…`) |
| Webconsole = cliente HTTP de los TRES servicios, nunca del bus | ✅ | `webconsole/backend/src/eovrt_webconsole/settings.py`:135-142 (defaults :8080/:8081/:8082); `grep zmq backend/src` → 0 archivos |
| Transporte de distribución **HTTP por default**; `subprocess` = fallback | ✅ | `experiment/runner.py`:501-533 (`_resolve_distribution_caller`); `preflight.py`:43-47 |
| Venv canónico 3.11 por pin de alert-distribution; 88 / 46 / 643 | ⚠ | 88 ✅ · 46 ✅ · **643 → 668 collected** |
| Deploy integral: 13 servicios, consola :8090, control :8081, distribución :8082, mosquitto :1883 | ✅ | `docker-compose.yml`:49-52, 74-76, 95, 113; 13 servicios |
| Fleet `mp-mock`, `mp-gdino-tiny-560` (campeón), `mp-gdino-base-560`, `mp-gdino-{tiny,base}`, `mp-yoloe-26{s,m,l,x}`, profile `models`, apagados | ✅ | `docker-compose.yml`:21, 139-184 |
| Dockerfiles en cada repo (`infra/docker/Dockerfile`) | ✅ | `docker-compose.yml`:18-19, 70-71, 91-92; `HEALTHCHECK` presente en los 3 (control-plane:32, alert-distribution:32, media-plane:29) |
| `cp .env.example .env`, única edición `EOVRT_WORKSPACE` | ✅ | `.env.example`:8 (+ `COMPOSE_PROFILES=models`:14, ya seteado) |
| Paridad de rutas `${EOVRT_WORKSPACE}:${EOVRT_WORKSPACE}` en consola/control/distribución | ✅ | `docker-compose.yml`:81, 101, 128-132 |
| Endpoints internos por nombre de servicio (`tcp://control-plane:5558`, `host: mosquitto`) | ✅ | `infra/platform/README.md`:59-61, 131 |
| Fallback `subprocess` **no funciona** en el deploy (imagen sin `eovrt-distribute`) | ✅ | `docker-compose.yml`:120-123; `infra/console/Dockerfile`:22-24 (solo instala `./backend`) |
| `docker compose config` valida 13; **builds + smoke pendientes** | ✅ | `infra/platform/README.md`:156-179 |
| Acople EBE: `sequencing: control_first`; control 201 ⇒ suscripto ⇒ media con `bus.enabled` | ✅ | `runner.py`:1061-1066, 1103-1112; manifiestos `experiments/*/manifest.yaml` (`sequencing: control_first`) |
| Orden con distribución: "**primero** `POST :8082/api/runs`, **después** el control, después el media" | ✗ | `runner.py`:1103-1145: **control primero** (con `alert_bus.enabled=True` + `wait_for_subscriber_ms ≥ 10000`, l.1095-1101), **después** la task de distribución (l.1120-1142), **después** el media (l.1149). La garantía la da el handshake del publicador (`control-plane/src/eovrt_control/transport/alert_bus.py`:85-88), no el orden literal. Ver C.1 |
| `alert_bus.enabled` default `False` en el control | ✅ | `control-plane/src/eovrt_control/config.py`:200 (`wait_for_subscriber_ms` default 0); comentario `docker-compose.yml`:64-66 |
| Runner inyecta `control.input.type=bus` y `media.bus.enabled=true` | ✅ | `runner.py`:1082-1086, 1147 |
| `experiments/` = manifiestos por referencia (ADR-009 rutas absolutas) | ✅ | `experiments/ebe_p1_live/manifest.yaml`:7,11 |
| Backup: `finetuning/weights/finetuned/` (Mendieta), `finetuning/runs/`, `results/`, `defensa/` en capa evidencia | ✅ existen | `finetuning/weights/finetuned/{full-1167640,full-1167864,full-1167982,smoke-1166583}`; `finetuning/runs/*` (7 entradas) |

### B.2 `00-contexto-base.md` — "Estado vigente que manda sobre el resto" (l.111-189)

| Afirmación | Veredicto | Evidencia |
|---|---|---|
| Banco temporal **47 clips = 32 pos + 15 neg, 37 episodios**; 34 = Bloque A | ✅ | `e-ovrt_datasets/datasets/processed/clip_bench/clip_bench_manifest.json` → `counts`: `clips_total 47`, `positive_clips 32`, `negative_clips 15`; `episodes.total 37` (CR-01 30 / CR-02 7); `by_block A 34 / B 13`; `manifest_yaml_sha256 3f14f50a53c0d6c5…`. Reproducido en `results/clip_bench/index.md`:6-8 |
| FAR/hora se mide y reporta, no sostiene cota (29,2 / 1.850,8 = 3 y 190 FP en 6:09,6, 0,1027 h) | ✅ | `results/index.md`:110-116, 128; `results/clip_bench/index.md`:181-183, 211-214 |
| G1 implementada y medida; MOT fuera de alcance | ✅ | `results/clip_bench/index.md`:30 (G1 F1 0,930); `results/index.md`:133 (L6) |
| Distribución: seis criterios spec 45; vista webconsole + orquestación cerradas 08-13 | ✅ | commits `13c801e`, `42529e2` (2026-08-13) |
| `t_alert-notification` **p95 64,534 ms (n=460)**; sostenido **102,025 ms (n=104)**; primeras 49,869 (n=356) | ✅ | `results/realtime/t_alert_notification/metrics.json`: `primary.latency_ms.p95 = 64.5341796875`, `count 460`; `steady_state.subsequent_deliveries.p95 = 102.025390625`, `count 104`; `first_delivery_per_run.p95 = 49.86865234375`, `count 356` |
| Mide bus de alertas → PUBACK, no sensor → notificación | ✅ | `results/realtime/t_alert_notification/README.md`:7-13 |
| Fine-tuning: T1 NO-GO, T2 NO-GO, T3 causa técnica; ningún checkpoint adoptado | ✅ | `finetuning/manifests/t1_go_no_go_1167640.json` (`verdict: NO-GO`, `checkpoint_not_adopted`); `t2_go_no_go_1167982.json` (`verdict.result: NO-GO`, `checkpoint_adopted: false`); T3: `DOCS/operacion/117`:90-94, 198-200 (D-FT-02/05/06 diferidas) |
| Márgenes D-FT-12 firmados ANTES de baseline y checkpoint | ✅ | `t1_go_no_go_1167640.json.margins_provenance` (`signed_by_user_at 2026-08-15`, `signed_before_baseline true`) |
| D-FT-14 después del veredicto T1; D-FT-15 pre-firmados; D-FT-16 pre-resultado | ✅ | `t2_go_no_go_1167982.json.protocol` (`margins_signed_at 2026-08-17`, `signed_before_any_tuned_result true`, `amendment_applied: D-FT-16 (2026-08-18, pre-resultado)`) |
| T1 gana por recall CR-01, T2 por AP | ✅ | T1: `bare_head` 0→0,0455, recall CR-01 0,0002→0,2089; T2: `bare_head` 0→0,0909, recall 0,0055 (`capacity_retention_curve.points`) |
| Gate de latencia T1 no medido (F-123.1) | ✅ | `t1_go_no_go_1167640.json.latency_gate.status = no_medido`; ídem T2 `gates.latency.measured false` |
| Baseline YOLOE-26s: `bare_head` 0,000; recall CR-01 0,0002; person 0,7843 / helmet 0,6286 / vest 0,2642 | ✅ | `t1_go_no_go_1167640.json.retention_gate.per_class.*.baseline` y `cr01_recall_by_source.count_weighted_aggregate.baseline` |
| Acoples DOS (ADR-020): HTTP en :8080/:8081/:8082 + bus :5557/:5558; subproceso = fallback (`EOVRT_CONSOLE_DISTRIBUTION_TRANSPORT=subprocess`) | ✅ | `runner.py`:501-533; `settings.py`:44-48; `experiments/*/control.yaml` `endpoint: tcp://127.0.0.1:5557`; `t_alert_notification/campaign.yaml`:9 `:5558` |
| Containerización "**diferida con causa**… se va a hacer **después** de cerrar la redacción" | ⚠ **desfasado** | `infra/platform/` ya define la plataforma completa (commit `0822413`, 08-20; `docker-compose.yml` 13 servicios + Dockerfiles en los 3 repos + validación estática `infra/platform/README.md`:160-179). Lo pendiente es **build + smoke** (README:156-158; `operacion/128` §4 fila 2). La regla de redacción ("no describir un despliegue que no corrió") sigue válida; el enunciado "diferida" ya no describe el repo. Ver C.4 |
| `t_alert-system` citable = columna `t_alert` del clip bench (`t_alert_system_ms`) | ✅ | `results/clip_bench/t1_…/metrics.json.positives.t_alert_system_ms = 5326.98`; `results/clip_bench/index.md`:68-90 |
| `precision_alertas`/`recall_alertas`/`F1_alertas` no citables | ✅ | `results/clip_bench/index.md`:88-90 |
| Cifras desde `results/index.md` + 4 índices | ✅ | existen los 4: `bench_imagenes/`, `bench_nivel_a/`, `clip_bench/`, `realtime/`. **No existe `results/finetuning/`** (las cifras FT viven en `finetuning/manifests/*.json`, coherente con "rama comparativa… no van a `results/`", GUIA:268-269) |

### B.3 "El recorrido del argumento en cuatro números" (`00-contexto-base.md` l.1321-1334; `results/index.md`:68-90)

| Cifra | Veredicto | Artefacto |
|---|---|---|
| mAP50 **0,551** `gdino-tiny-560` sobre 6.477 imgs / 3 fuentes | ⚠ | `results/bench_imagenes/index.md`:82. **Sin `metrics.json` en este repo** (declarado en `results/index.md`:161-162: se verifica contra doc 64). No verificable mecánicamente acá |
| Veto de precisión E-DIR **0,146 < 0,5**; E-DIR F1 0,160 | ✅ | `results/clip_bench/d1_gdinotiny560_edirpair_scene/metrics.json` (verificador: 0,160000); precisión 0,146 en `index.md`:28 |
| E-IND **0,789** (T1) | ✅ | `t1_…/metrics.json.positives.f1_micro = 0.788732`, `precision_micro 0.756757`, `recall_micro 0.823529` |
| Histéresis: CR-02 recall 1,000 con **SDR 0,281** | ✅ | `t1_…/metrics.json.by_condition.CR-02.sdr = 0.281115` (recall por condición vive en doc 81, `index.md`:64-66) |
| G1 **0,930**, detecciones bit a bit idénticas (SDR/TTFD iguales a T1) | ✅ | `g1_…/metrics.json` 0,929577; SDR 0,698 / TTFD 168 ms en ambas filas (`index.md`:26,30) |
| Ganancia de identidad excluye el cero en 4 densidades (+0,141 / +0,072 / +0,137 / +0,096) | ✅ (3 de 4 mecánicos) | verificador §3: G1−T1 +0,141 IC[+0,032,+0,258]; R2−R1 +0,072 [+0,013,+0,145]; R4−R3 +0,137 [+0,032,+0,258]. El +0,096 (R6−R5) no está en `CIFRAS` del verificador (solo en `index.md`:78-79 y doc 96) |

### B.4 `GUIA-REDACTORES.md`

| Sección / afirmación | Veredicto | Evidencia |
|---|---|---|
| §1 experimental-setup = consola web + runner + guarda los resultados | ✅ | árbol: `webconsole/`, `tools/`, `results/` |
| §1 cuarto repo distribución, servicio HTTP :8082, ADR-020 default | ✅ | `settings.py`:48; `runner.py`:501-533 |
| §1 cifra distribución 64,534 / 102,025 / 49,869 | ✅ | B.2 |
| §1 DBE = casi todo lo medido, reproducible; EBE = vivo | ✅ | 14 campañas `path: DBE` (`campaign.yaml` de cada una); EBE en `results/realtime/index.md` |
| §3 formato de cita: G1 0,930 vs 0,789 sobre banco del rodaje; 47 (32/15, 37 ep); 34 evaluables sobre 35 en Bloque A; 3 FP en 6:09,6; asimetría 26 vs 323; mAP50 0,551 por estrato; G2A 14,7 ms desde el dequeue + 202–217 ms captura | ✅ | `results/clip_bench/index.md`:11-15, 26, 30, 182; `results/realtime/index.md`:63, 73-84 |
| §3.1 autocontención (el informe no cita docs/ADRs/rutas) | n/a (regla) | — |
| §4 trampa 1 (34 vs 47), 2 (FAR), 3 (n=2 estrato B), 4 (L4 precisada), 5 (BENCH 196 / `cb_b01_p7` retirados), 6 (FT nunca "falta de tiempo") | ✅ coherentes con `results/` | `results/index.md`:128-135; `results/bench_imagenes/index.md`:33-36 |
| §4 trampa 7 (⛔ superada, DOS acoples) | ✅ | ídem B.2 |
| §4 bloque containerización "diferida con causa" | ⚠ desfasado | ver B.2 / C.4 |
| §6 "Cifras: `results/index.md` + 4 índices" | ✅ | — |
| §7 "verificador… **19 cifras sobre las 16 campañas**" | ✗ desfasado | el verificador cubre **26 cifras / 17 campañas** (salida §G; `results/index.md`:11-12, 145-153) |

### B.5 `13-glosario-y-convenciones-de-lectura.md`

| Afirmación | Veredicto | Evidencia |
|---|---|---|
| §4.2 IDs de campaña T1/T2/D1/H1/G1/B1/R1–R6/I1/I2/NA1 (**16 campañas con artefacto**) | ⚠ | los 16 IDs existen como directorios en `results/clip_bench/` (14) y `results/bench_nivel_a/` (2); el total con artefacto es **17** (falta `t_alert_notification`, `results/index.md`:7-8). Correcto si se lee "16 de video" |
| §4.3 Estrato A = 34 rodaje / B = 13 internet; ≠ estratos de `bench_v3` | ✅ | manifest `by_block A 34 / B 13`; `bench_imagenes/index.md`:26-31 |
| §5 `bench_v3` 6.477 / 3 fuentes / estratos 147+1.330+5.000 | ✅ | `results/bench_imagenes/index.md`:22-31 |
| §5 clip bench 47 clips GT humano, 32/15/37, manifest `3f14f50a…`, en `processed/clip_bench/` | ✅ | manifest (B.2); ruta existe |
| §5 `eind_v1`/`edir_v1` frozen con sha256 desde 07-29 | ✅ | `prompts/eind_v1.yaml`:9-11; `prompts/edir_v1.yaml`:11-15; commit `159167b` |
| §5 pattern set oficial `cr01_cr02_v2` (4000/7000) | ✅ | `experiments/*/control.yaml`:21; `results/clip_bench/t1_…/campaign.yaml` (`pattern_set_note`) |
| §5 TRAIN/BENCH/DEMO 5540/196/1064 | ⚠ histórico | archivados en `e-ovrt_datasets/legacy/` el 08-15 (CLAUDE.md) |
| §6 "Repos de código: media-plane, control-plane, experimental-setup, datasets" | ✗ incompleto | omite `e-ovrt_alert-distribution` (sí aparece en la fila de puertos/entry points) |
| §6 puertos 8080/8081/8082/8090/5173 | ✅ | `settings.py`; `infra/console/Dockerfile`:28; `webconsole/README.md`:44 |

### B.6 `operacion/128` §1 y §4

| Fila | Veredicto | Evidencia |
|---|---|---|
| Ejes E-DIR/E-IND congelados acta 07-29; F-83.6 18,5 % | ✅ | prompts frozen; `results/bench_nivel_a/index.md`:64, 95-97 |
| Cadena T→P→D: cifras = SOLO los 4 índices; G1 0,930; E-IND 0,789 | ✅ | B.3 |
| Estrato B: banco 32/15/47, manifest `3f14f50a…`, revisión ciega tumbó 5/7 | ✅ | manifest; `results/clip_bench/index.md`:215-219 |
| R1–R6 F-96.4 | ✅ | `results/clip_bench/index.md`:58-79; verificador §3 |
| Distribución p95 64,534 (n=460); servicio :8082 | ✅ | B.2 |
| FT jornada completa 08-21; curva de 3 puntos; F-127.1 | ✅ | `t2_go_no_go_1167982.json.capacity_retention_curve` (3 puntos: 0 / 3.096 / 10.350.308 params) |
| Deploy integral 13 servicios validado por config; builds+smoke PENDIENTES | ✅ | `infra/platform/README.md`:156-179 |
| §4: informe primero; smoke Docker / C1 / V2 / latencia FT post-entrega; V2 no existe | ✅ | `defensa/README.md`:13 ("V2 NO EXISTE") |

### B.7 `estado-de-implementacion-adrs.md`

| ADR | Afirmación relevante al repo | Veredicto | Evidencia |
|---|---|---|---|
| 009 | config centralizada en ES; prompt sets con ciclo de vida (`prompt_store.py`, `frozen_sha256`); historial durable y promoción `runs/`→`results/` **diferidos** | ✅ | `prompts/*.yaml` con `status`/`frozen_sha256`; `results/` se cura a mano (`clip_bench/README.md`:40-61) |
| 010 | plataforma primero, clip bench al cierre del spec 44 | ✅ (histórico) | fechas de campañas 08-03→08-09 posteriores al tramo plataforma |
| 014 | consolidado en `ES/runs/<experiment_id>/` gitignorado, híbrido selectivo; sellado opt-in no ejercitado | ✅ | `runs/` 339 dirs gitignorados; `.gitignore`:2 |
| 015 | cierre de alcance; §2b/2c/6 derogados por 016 | n/a repo | — |
| 016 | distribución materializada; vista + orquestación integradas | ✅ | commits `13c801e`/`42529e2`; `experiments/t_alert_notification/` |
| 017 | FT jornada: T1 NO-GO 08-17, D-FT-14 reabre T2 exploratorio, T2 NO-GO 08-21 (`1167864` submuestreado → D-FT-16 → `1167982` early stop 16/60 best=ep1) | ✅ | `t1_go_no_go_1167640.json`, `t2_go_no_go_1167982.json.checkpoint.training_caveat`; `weights/finetuned/full-1167864` existe |
| 018 | derogada por 020; subproceso = fallback (`EOVRT_DISTRIBUTION_EXECUTABLE`) | ✅ | `runner.py`:106-125 (`resolve_distribution_executable`), 525-526 |
| 019 | servicio HTTP :8082; cliente opcional vía `…TRANSPORT=http`; "containerización diferida con causa (ADR-019 §4)" | ⚠ | HTTP hoy es default (fila 020 ✅); la containerización **ya está definida** en `infra/platform/` (C.4) |
| 020 | HTTP default; preflight sondea `/healthz`; fallback solo con `=subprocess` | ✅ | `preflight.py`:43-62, 170; `runner.py`:525 (comparación estricta) |

---

## C) Divergencias doc↔repo, por gravedad

### ALTA (puede llegar al informe o rompe la reproducibilidad)

**C.1 Orden de arranque live con distribución — docs vs runner.**
- *Dicen:* CLAUDE.md ("Acople entre planos": "primero `POST :8082/api/runs` (`mode: live`), después el control, después el media"); `ES/infra/platform/README.md`:69-70 ("distribución antes que control, control antes que media"); `ES/docs/experiments.md`:93-96 ("si hay distribución, primero `POST :8082/api/runs`; después el control"). `operacion/128` §4 fija para las figuras "orden de arranque INVERSO al flujo de datos".
- *Hay:* `webconsole/backend/src/eovrt_webconsole/experiment/runner.py`:1095-1149 — el runner lanza **primero el control** (`alert_bus.enabled = True`, `wait_for_subscriber_ms = max(cfg, 10000)`), **después** crea la task de distribución (`POST :8082/api/runs` vía `distribution_http.run_distribution_http`:105) y **al final** el media. La no-pérdida en `:5558` la garantiza el handshake del publicador (`control-plane …/transport/alert_bus.py`:85-88 `wait_for_subscriber`), no la secuencia literal. Tests: `tests/test_runner_distribution.py`:190 asserta `wait_for_subscriber_ms: 10000`; ningún test asserta "distribución antes que control".
- *Corregir:* elegir uno. O bien (a) redactar en CLAUDE.md, `infra/platform/README.md`:69-70, `docs/experiments.md`:93-96 y en la nota de FIG (`operacion/128` §4) que el orden real es **control (con espera de suscriptor ≥10 s) → distribución → media**, o bien (b) cambiar el runner para lanzar la distribución antes del control. Si el informe §17.4 ya describe "distribución primero", hoy describe algo que el código no hace.

**C.2 Rango de entrenamiento del protocolo (Tabla 28: 500–2.000 imgs) vs `finetuning_v1` (2.946 train / 483 val).**
- *Dice el protocolo:* `17-1-full.md`:678 "El split de entrenamiento para fine-tuning se acota a 500–2.000 imágenes".
- *Hay:* `finetuning/manifests/finetuning_v1.summary.json` → `splits.train.images 2946`, `val.images 483`; `configs/t1_yoloe26s_lp.yaml`:18-19.
- *Corregir:* declarar la desviación en §17.4/§17.5 (la fila FT de la Tabla 68 / AJ-5.13) con su causa (D-FT-11), o registrarla en `docs/operacion/116/117` si ya lo está (no lo verifiqué, ver F).

### MEDIA (docs desfasados sobre el estado del repo)

**C.3 Conteo de tests del BFF: 643 → 668.** README §3 bis:115, `requirements-dev.txt`:21, CLAUDE.md dicen "643 passed" (foto 08-15); hoy se recolectan **668** (+25 tras `14f9e01` y `288c5dd`). Corregir los tres.

**C.4 Containerización "diferida con causa".** `00-contexto-base.md`:163-172, GUIA:338-346 y fila ADR-019 dicen que se hará después de la redacción. El repo la tiene **definida y validada estáticamente** desde 08-19/20 (`infra/platform/docker-compose.yml` 13 servicios; Dockerfiles en los 3 repos; `README.md`:160-179). Pendiente real: `docker compose build` + smoke 1–5. Corregir la redacción: "definida y validada por config; build y smoke diferidos post-entrega" (como ya dice `operacion/128` §1 última fila).

**C.5 Manifiestos de `experiments/` que ya no resuelven contra el catálogo del media-plane.** `e-ovrt_media-plane/configs/datasets/` solo tiene `bench_v2_test`, `bench_v2_val`, `demo_v2`; `configs/models/` ya no tiene `mm-grounding-dino/*` (archivado en `configs/_archive/`, commit `ee7a6af`). Quedan sin destino: `experiments/mock_chv.yaml`:9 (`source.ref: chv`), `experiments/video_annotated.yaml`:9 y `video_annotated_gdino.yaml`:9 (`video_sample`), y los 4 `experiments/bench_v2/b2_g_e{5,6}_mmgdino_*.yaml` (`mm-grounding-dino/mm-gdino-{tiny,base}`). `ES/docs/experiments.md`:197-201 sigue listando `mm-grounding-dino/*`, `chv` y `video_sample` como disponibles. Corregir: archivar esos manifiestos o documentar que son registro histórico (como se hizo con `realt-time-safety_vest.yaml`).

**C.6 `finetuning/README.md` no refleja el cierre de T2.** Su encabezado de estado (l.12-20) cierra en "2026-08-17 — JORNADA T1 CERRADA"; el cierre T2 NO-GO (08-21, `t2_go_no_go_1167982.json`, commit `2bfb268`) no aparece. Agregar el bloque T2 (secuencia `1167864` → D-FT-16 → `1167982`, curva de 3 puntos).

### BAJA (inconsistencias internas / metadatos)

**C.7 `README.md` raíz, varias afirmaciones vencidas:** l.39-41 el layout anota `cr01_cr02_v2_short # exploratory` y `eind_v1 # frozen_pending_review` (ambos `frozen`; el mismo README lo dice bien en §5:193-195); l.71 "cliente del servicio media-plane" (hoy tres servicios, como dice §4:134-136); §5:190 "catálogo activo (5)" mientras `prompts/` tiene **7** YAML activos (faltan `clase_nueva_v1`, `coco_val2017_80`); §5:210 "6 modelos (GDINO t/b, MM-GDINO t/b, …)" (MM-GDINO archivado en el media-plane); §9:245 "runs/ … viven en los planos hermanos" cuando el repo tiene su propio `runs/` consolidado (ADR-014, 339 dirs).

**C.8 `prompts/_archive/README.md`:7-9** dice `cr01_cr02_bench_v2` **frozen** y `eind_v1` **frozen_pending_review**; los YAML dicen `exploratory` (`cr01_cr02_bench_v2.yaml`:9) y `frozen` (`eind_v1.yaml`:10). `ES/docs/experiments.md`:121 también llama "congelado" a `cr01_cr02_bench_v2`.

**C.9 `GUIA-REDACTORES.md`:419-421** "19 cifras sobre las 16 campañas" → hoy 26 cifras / 17 campañas (cobertura obligatoria).

**C.10 Glosario §6** omite `e-ovrt_alert-distribution` en "Repos de código"; §4.2 "16 campañas con artefacto" (17 con `t_alert_notification`).

**C.11 Metadato `annotator` del manifest del clip bench:** los 34 clips del Bloque A tienen `annotator: null` (los 13 del B: `simon`). No contradice "GT humano" (doc 80), pero la procedencia por clip está incompleta en el artefacto.

**C.12 `00-contexto-base.md`** (y GUIA §1) sigue diciendo que el tercer repo "no es un tercer plano" y que la webconsole del README raíz es "cliente del servicio media-plane" — coherente entre sí, pero el README raíz l.71 debería alinearse con §4.

---

## D) Protocolo §17.1 vs lo ejecutado

Leyenda: **CUMPLIDA** / **PARCIAL** / **NO EJERCIDA** / **DESVIADA**. Evidencia en `results/`, `experiments/`, `prompts/`, `finetuning/`.

| § | Prescripción | Estado | Dónde / evidencia |
|---|---|---|---|
| 17.1.3.3 | DBE primario (controlado, repetible) + EBE complementario | **CUMPLIDA** | 14 campañas `path: DBE` en `results/clip_bench/*/campaign.yaml`; EBE: rodaje 6 corridas live (`results/realtime/index.md`:88-97), doc 91/101 |
| 17.1.3.3 | Secuencia progresiva: base → barridos univariados → prueba exigente | **CUMPLIDA** | T1 base (08-03) → variable única por campaña (T2 modelo, D1 prompts, H1 fusión, B1 vocabulario, G1 granularidad, R1–R6 densidad) → estrato B obra real (I1/I2). `clip_bench/index.md`:24-31, 58-67, 149-219 |
| 17.1.3.4 | Baseline obligatoria zero-shot para toda variante | **CUMPLIDA** | S1/S2 doc 64; baseline YOLOE-26s one-shot 08-15 antes de T1 (`t1_go_no_go…margins_provenance`) |
| 17.1.4.4 | Ambos escenarios evalúan preentrenado **y** ajustado | **PARCIAL** | Ajustados solo en DBE-imágenes (`bench_v3`); **ningún checkpoint FT corrió sobre clips ni en EBE** (no hay campaña `results/clip_bench/*ft*`; `t1/t2_go_no_go` solo brazos de imágenes) |
| 17.1.4.4.1 | DBE: contraste con métricas de la literatura cuando dataset/protocolo coincidan | **NO EJERCIDA** | ningún índice reporta comparación con cifras publicadas de SHEL5K/CHV; `bench_v3` es composición propia |
| 17.1.4.4.2 | EBE en obra simulada con participantes, escenas con/sin infracción, OAK-D | **CUMPLIDA** | `experiments/ebe_p{1,2,3}_live/`, `yoloe_p{1,2,3}_live/` (`ingest.plugin: oak_d`); P3 = sin infracción; `results/realtime/index.md`:88-97, 172-192 |
| 17.1.5.4.2 eje 1 | Estructura sintáctica: nominal vs descriptiva | **PARCIAL** | E-IND = etiquetas nominales (`person/helmet/vest`); E-DIR = oraciones descriptivas (`edir_v1.yaml`:27,32,37,52,57,62). No hubo variantes de artículos/preposiciones para una misma clase; F-88.3 ordena "etiqueta corta > frase negada" (`clip_bench/index.md`:185-191) |
| 17.1.5.4.2 eje 1 | Variantes con **template** ("a photo of a [CLASS]"), con y sin | **NO EJERCIDA** (definida, no medida) | `edir_v1.yaml`:41-46, 63-68 (`cr01_template`/`cr02_template`, `enabled_by_default: false`); excluidas de D1: `bench_nivel_a/d1_…/campaign.yaml`:47 `variants_excluded: [cr01_template, cr02_template]`; ninguna campaña las puntúa |
| 17.1.5.4.2 eje 2 | Especificidad (`person`/`worker`/`construction worker`) | **PARCIAL** | solo dentro de E-DIR (`cr01_spec`/`cr02_spec` = "construction worker without …"); caveat C2 doc 76 (cambia sujeto y objeto a la vez). E-IND siempre `person` (`cr01_cr02_v2_short`; A/B `cr01_cr02_v2_safety_vest` solo cambió `vest`, sin campaña en `results/`) |
| 17.1.5.4.2 eje 3 | Directa vs indirecta comparadas para todas las condiciones aplicables | **CUMPLIDA** | Nivel A: D1 CR-01 (2 estratos) y CR-02 (`bench_obra`) (`bench_nivel_a/index.md`:24-58); Nivel B: D1/H1/B1 vs T1 (`clip_bench/index.md`:19-35 veredicto) |
| 17.1.5.4.2 eje 4 | Cada prompt evaluado **en aislamiento y en contexto completo** | **DESVIADA** | régimen asimétrico declarado: E-DIR una frase por caption (`caption_regime: isolated`), E-IND las 3 juntas (`caption_regime: joint`) — `d1_…/campaign.yaml`:33-52; doc 83:91-96. **Ningún prompt se midió en ambos regímenes.** El sub-experimento aislado-vs-completo se sustituyó por un único control: B1 vs T2 (+1 palabra en el caption = −0,082 F1, F-88.1, `clip_bench/index.md`:178-184) |
| 17.1.5.4.2 | Tamaño del vocabulario activo vs latencia por arquitectura | **PARCIAL** | costo del caption medido en calidad (F-88.1), no en latencia por nº de prompts; latencia por modelo en `realtime/index.md`:59-65 |
| 17.1.5.4.3 | Prompts en inglés; español como línea complementaria | **CUMPLIDA / NO EJERCIDA** | todos los sets `language: en`; español = E-09 excluida (`DOCS/nucleo/10`) |
| 17.1.5.4.4 | Catálogo de candidatos (Tabla C.1) | **CUMPLIDA** | `prompts/_archive/edir_exp_cr01_candidates.yaml`, `…cr02_candidates.yaml`, `edir_exp_weak_classes.yaml` → finalistas `edir_v1` (8 formulaciones) por acta doc 76 |
| 17.1.5.4.5 F1 | Dataset con GT relevante; anotación complementaria con **doble anotación ≥20 % + kappa** | **NO EJERCIDA (declarada L2)** | imágenes: se reutilizó GT existente (`has_vest` de negativos explícitos del raw, `d1_…/campaign.yaml` `cr02_gt_provenance`) — sin anotación nueva; video: `clip_bench_manifest.json.counts.double_annotation_ratio = 0.0`, `double_annotated_clips 0`; L2 en `results/index.md`:129; doc 80:211-220 |
| 17.1.5.4.5 F1 | Piso ~200 positivos por condición, o n efectivo + IC | **PARCIAL** | CR-01 `shel5k` n+=2.487 ✅; CR-01 `bench_obra` n+=28 ✗; CR-02 n+=82 ✗ (un solo estrato) → **IC95 bootstrap reportados** (`bench_nivel_a/index.md`:26-44), limitación L8. Doc 92:129-132 lo declara "cumplido por la vía correcta" (espacial) |
| 17.1.5.4.5 F2 | Matriz (modelo × condición × prompt × contexto) | **PARCIAL** | modelo: `tiny-560` + réplica `base-560` (`metrics_base560_replica.json`, doc 84); condición: CR-01/CR-02; prompt: 6 variantes E-DIR + E-IND; contexto: **un régimen por brazo** (no cruzado) |
| 17.1.5.4.5 F2 | Hiperparámetros congelados entre variantes | **CUMPLIDA (con matiz declarado)** | `box_threshold 0.30 / text_threshold 0.25` idénticos (`d1_…/campaign.yaml`:57-59, T1/D1/H1 `model_note`); umbrales operativos calibrados por brazo en mitad A con **grid idéntico** (`threshold_grids`), reportado como variable adicional — permitido por el texto ("se documentan como variable adicional") |
| 17.1.5.4.5 F3 | Ejecución sistemática, formato estructurado | **CUMPLIDA** | `provenance_runs.json` (18 corridas), `detections.jsonl` en media-plane, `evidence-runs/` |
| 17.1.5.4.5 F4 | Métricas por (modelo, condición, prompt, contexto) + **confianza media de TP** | **PARCIAL** | P/R/F1/IC por variante ✅ (`metrics.json.strata.*.conditions.*.arms`); la confianza media de TP no figura en `metrics.json` (ver F) |
| 17.1.5.4.5 F4 | Indirecta: métricas por entidad componente | **CUMPLIDA** | AP por clase/estrato (`bench_imagenes/index.md`:95-102) + Nivel A por persona |
| 17.1.5.4.5 F5 | Selección + patrones transversales (template vs no; indirecta vs directa); sensibilidad al contexto cuantificada | **PARCIAL** | indirecta vs directa ✅ (veredicto pre-registrado `nucleo/04` §8); template ✗; sensibilidad al contexto solo F-88.1 (un punto) |
| 17.1.6.2.7 T28 | Disyunción estricta / test compartido / semilla / no solapamiento / congelamiento previo | **CUMPLIDA** | `finetuning_v1.summary.json`: `gates.bench_overlap_selected 0`, `shared_components_train_val 0`, `seed 42`, `deduplicated_ppe_lineage 700`, `bench_v3_sha256 4557024e…`; `bench_v3` congelado 07-23, FT 08-15+ |
| 17.1.6.2.7 T28 | Rango de entrenamiento **500–2.000** imgs | **DESVIADA** | train **2.946** / val 483 (`finetuning_v1.summary.json`, `t1_yoloe26s_lp.yaml`:18-19) |
| 17.1.6 T31 | CR-01/CR-02 núcleo; CR-03…06 condicionadas | **CUMPLIDA** | solo CR-01/CR-02 en `configs/patterns/cr01_cr02_v2`; E-01/E-02 excluidas |
| 17.1.7.6 | Baseline zero-shot explícita, mismo test, checkpoint no elegido sobre test | **CUMPLIDA** | baseline one-shot 08-15; `bench_v3` en ambos brazos; `checkpoint_policy: best_metrics_mAP50-95_B_all_four_val_classes` sobre val (`t1_yoloe26s_lp.yaml`:51) |
| 17.1.7.6 | ΔAP, ΔRecall, ΔPrecision, ΔSDR por CR | **PARCIAL** | ΔAP ✅ (`bare_head` 0→0,0455 / 0,0909), ΔRecall CR-01 ✅ (0,0002→0,2089 / 0,0055); **ΔPrecision y ΔSDR no reportados** (sin brazo de video) |
| 17.1.7.6 | Δt_alert, ΔTTFD (deseable) | **NO EJERCIDA** | sin corrida FT sobre clips |
| 17.1.7.6 | Retención OV sobre subset generalista (deseable) | **CUMPLIDA (T2) / NO MEDIBLE (T1)** | T2: COCO val2017 80 clases, 0,4347→0,1247 (`t2_go_no_go…retention_open_vocabulary`; `prompts/coco_val2017_80.yaml`); T1: `coco_ov_note: no medible (head fusionado D-FT-08)` |
| 17.1.7.6 | Costo: horas-GPU, tiempo, horas-persona, imágenes, criterio de checkpoint | **PARCIAL** | `elapsed 00:13:08` (T1, `t1_promotion_1167640.json`:11), `00:26:10` (T2); imágenes 2.946/483; checkpoint policy ✅; **horas-persona no registradas** |
| 17.1.8 T36 | Preparación (congelar entorno/checkpoints/datasets/bitácora) | **CUMPLIDA** | `bench_v3` 07-23; prompts `frozen_sha256` 07-23/07-29; `evidence-runs/` + `files.sha256`; `finetuning/manifests/t1_source_snapshot.json` |
| 17.1.8 T36 | Baseline DBE zero-shot por modelo sobre test congelado | **CUMPLIDA** | S1/S2 (07-23) + B5 (`bench_imagenes/index.md`:78-84) |
| 17.1.8 T36 | Sensibilidad de prompts → matriz y formulación primaria congelada | **CUMPLIDA (orden invertido)** | la formulación primaria (`cr01_cr02_v2_short`) se congeló **07-23 antes** del estudio de sensibilidad (D1 08-03/04); la sensibilidad confirmó la elección a posteriori |
| 17.1.8 T36 | Pipeline y tracking: tG2A, FPS, recursos, aporte del tracker | **CUMPLIDA (sin MOT)** | G2A/FPS/GIL: `realtime/index.md`:59-130; tracker = G1 F1 (`clip_bench/index.md`:30), sin métricas MOT (E-10) |
| 17.1.8 T36 | Fine-tuning condicionado | **CUMPLIDA** | T1/T2 08-15→08-21, gates pre-registrados |
| 17.1.8 T36 | EBE complementario | **CUMPLIDA** | rodaje 07-25 (doc 71), humos 08-05 (doc 101), G1 live (doc 91) |
| 17.1.8 T36 | Reporte con métricas no aplicables y causas | **CUMPLIDA** | estados `not_applicable:<causa>` (ADR-006/013), `results/index.md`:117-118 |
| 17.1.8 T36 | **Orden real** de las fases | **DESVIADA (declarable)** | Preparación → Baseline DBE imágenes (07-23) → **EBE rodaje (07-25)** → GT video (08-03) → baseline Nivel B T1 (08-03) → sensibilidad de prompts (08-03/04) → pipeline/tracking G1 + densidad (08-04/05) → EBE blindado (08-05) → **Reporte** (índices 08-05→08-14) → estrato B (08-09) → distribución (08-13) → **fine-tuning (08-15→08-21, después del cierre del tramo y con la redacción iniciada)**. El EBE precedió a la sensibilidad de prompts porque fue la fuente del banco de clips; el FT fue la última fase |
| 17.1.9.2 | Máx. 2 candidatos: Grounding DINO y YOLOE | **PARCIAL** | solo **YOLOE-26s** ajustado (T1 linear probing 3.096 params; T2 full 10,35 M); GDINO no ajustado (T3 planificado como MM-GDINO, diferido con causa técnica — D-FT-02/05/06) |
| 17.1.9 T37 | Baseline / datos CR-01-02 / integridad / ganancia exigible / costo operativo | **CUMPLIDA salvo costo** | gates `gain`/`retention` pre-registrados (T1 falla gain por 0,0045; T2 pasa gain, falla retención ×4 y OV −71,3 %); **latencia no medida** en T1 ni T2 (`latency_gate.status no_medido`) |

---

## E) Hechos citables con comando

```bash
# Estado
cd /home/simonll4/projects/e-ovrt_experimental-setup && git branch --show-current && git log -1 --format='%h %ci %s' && git status --short | wc -l
# → feature/webconsole-consola-tesis · 2bfb268 2026-08-22 · 0

# Tests recolectados (88 / 46 / 668)
.venv/bin/python -m pytest tests/ --collect-only -q | tail -1
.venv/bin/python -m pytest finetuning/tests/ --collect-only -q | tail -1
(cd webconsole/backend && ../../.venv/bin/python -m pytest --collect-only -q | tail -1)

# Compose: 13 servicios, 9 en profile models
python3 -c "import yaml;s=yaml.safe_load(open('infra/platform/docker-compose.yml'))['services'];print(len(s),sum(1 for v in s.values() if v.get('profiles')==['models']))"

# Prompt sets congelados y sus sha
grep -H -E "status:|frozen_sha256" prompts/*.yaml

# Frases exactas E-DIR / E-IND
grep -n "phrasings" prompts/edir_v1.yaml prompts/eind_v1.yaml prompts/cr01_cr02_v2_short.yaml

# Transporte de distribución (default HTTP, fallback subprocess)
grep -n "EOVRT_CONSOLE_DISTRIBUTION_TRANSPORT" webconsole/backend/src/eovrt_webconsole/experiment/runner.py webconsole/backend/src/eovrt_webconsole/preflight.py
# Orden real live: control → distribución → media
sed -n '1095,1150p' webconsole/backend/src/eovrt_webconsole/experiment/runner.py

# Banco de clips 47/32/15/37 y manifest 3f14f50a…
python3 -c "import json;d=json.load(open('/home/simonll4/projects/e-ovrt_datasets/datasets/processed/clip_bench/clip_bench_manifest.json'));print(d['counts']['clips_total'],d['counts']['positive_clips'],d['counts']['negative_clips'],d['episodes']['total'],d['manifest_yaml_sha256'][:8],d['counts']['double_annotation_ratio'])"

# Cifras estrella
python3 -c "import json;p='results/clip_bench/%s/metrics.json';print(json.load(open(p%'t1_gdinotiny560_v2short_scene'))['positives']['f1_micro'],json.load(open(p%'g1_gdinotiny560_v2short_subject'))['positives']['f1_micro'],json.load(open(p%'d1_gdinotiny560_edirpair_scene'))['positives']['precision_micro'])"
# → 0.788732 0.929577 0.146…
python3 -c "import json;d=json.load(open('results/realtime/t_alert_notification/metrics.json'));print(d['primary']['latency_ms']['p95'],d['primary']['latency_ms']['count'],d['steady_state']['subsequent_deliveries']['p95'],d['steady_state']['subsequent_deliveries']['count'])"
# → 64.534 460 102.025 104

# Fine-tuning: veredictos y split
python3 -c "import json;print(json.load(open('finetuning/manifests/t1_go_no_go_1167640.json'))['verdict'],json.load(open('finetuning/manifests/t2_go_no_go_1167982.json'))['verdict']['result'])"
python3 -c "import json;d=json.load(open('finetuning/manifests/finetuning_v1.summary.json'));print(d['splits']['train']['images'],d['splits']['val']['images'],d['gates'])"
grep -n "SLURM_JOB_ID" finetuning/scripts/train_t2.py   # l.317: exige SLURM_JOB_ID

# Verificador de índices
python3 /home/simonll4/projects/docs/operacion/datos/96-verificar-indices.py
```

---

## F) No pude verificar (solo lectura / fuera de alcance)

1. **Que los tests pasen** (solo `--collect-only`): 88 / 46 / 668 recolectados; no ejecutados. Tampoco `vitest` del frontend (55 archivos `*.test.*`, sin correr).
2. **Builds e imágenes Docker** (daemon apagado): compose válido por lectura; `HEALTHCHECK` presentes en los 3 Dockerfiles hermanos; no verifiqué que compilen.
3. **Cifras de `bench_imagenes/`** (mAP50 0,551, 0,503, 0,525, 0,442, recall CR-01 0,308/0,599): sin `metrics.json` en este repo; el propio índice remite a `docs/operacion/64` (`results/index.md`:161-162). El verificador no las cubre.
4. **`frozen_sha256`** de los tres sets congelados: no recomputé el hash (fórmula en `docs/prompt-strategy.md`:78-85); solo constaté presencia y coincidencia con doc 76 y `campaign.yaml`.
5. **Confianza media de TP por formulación** (§17.1.5.4.5 F4): no la encontré en `bench_nivel_a/d1_…/metrics.json` (claves `precision/recall/f1/tp/fp/fn`); podría vivir en `docs/operacion/datos/83-*`.
6. **Horas-persona del fine-tuning** (§17.1.7.6): no registradas en `finetuning/manifests/`.
7. **Si la desviación 2.946 > 2.000 imgs (Tabla 28) está declarada** en `docs/operacion/116`/`117` o en la fila FT del informe: no lo revisé.
8. **Delta +0,096 (R6−R5)**: citado en `clip_bench/index.md`:78-79 y doc 96, no está en `CIFRAS` del verificador (solo los otros tres deltas).
9. **Contenido de `runs/` (339 consolidados)**: no auditado; la mayoría son `exp_*_orq*` de campañas t_alert (2026-08-13).

---

## G) Salida completa de `96-verificar-indices.py` (2026-08-28, EXIT=0)

```
## 1. Enlaces relativos en results/

  1452 enlaces ok, 0 rotos

## 2. Cifras citadas vs metrics.json en disco

  ok   t1_gdinotiny560_v2short_scene          citado 0.789 | disco 0.788732 x5
  ok   t2_gdinobase560_v2short_scene          citado 0.704 | disco 0.704225 x6
  ok   d1_gdinotiny560_edirpair_scene         citado 0.160 | disco 0.160000 x4
  ok   h1_gdinotiny560_hybor_scene            citado 0.296 | disco 0.296296 x3
  ok   g1_gdinotiny560_v2short_subject        citado 0.930 | disco 0.929577 x4
  ok   b1_gdinobase560_barehead_scene         citado 0.377 | disco 0.376812 x3
  ok   r1_gdinotiny560_v2short_scene_s7       citado 0.794 | disco 0.794118 x3
  ok   r2_gdinotiny560_v2short_subject_s7     citado 0.866 | disco 0.865672 x3
  ok   r3_gdinotiny560_v2short_scene_s15      citado 0.738 | disco 0.738462 x4
  ok   r4_gdinotiny560_v2short_subject_s15    citado 0.875 | disco 0.875000 x2
  ok   r5_gdinotiny560_v2short_scene_s26      citado 0.646 | disco 0.646154
  ok   r6_gdinotiny560_v2short_subject_s26    citado 0.742 | disco 0.741936
  ok   i1_gdinotiny560_v2short_scene_internet citado 0.333 | disco 0.333333
  ok   i2_gdinotiny560_v2short_subject_intern citado 0.190 | disco 0.190476
  ok   d1_gdinotiny560_edir_vs_eind           citado 0.546 | disco 0.545997 x2
  ok   d1_gdinotiny560_edir_vs_eind           citado 0.408 | disco 0.408163 x3
  ok   d1_gdinotiny560_edir_vs_eind           citado 0.479 | disco 0.478873 x3
  ok   na1_gdinotiny560_v2short_video         citado 0.031 | disco 0.030649
  ok   na1_gdinotiny560_v2short_video         citado 0.018 | disco 0.018042
  ok   t_alert_notification                   citado 64.534 | disco 64.534180
  ok   t_alert_notification                   citado 64.534 | disco 64.534180 x2
  ok   t_alert_notification                   citado 460.000 | disco 460.000000 x2
  ok   t_alert_notification                   citado 356.000 | disco 356.000000
  ok   t_alert_notification                   citado 104.000 | disco 104.000000
  ok   t_alert_notification                   citado 49.869 | disco 49.868652
  ok   t_alert_notification                   citado 102.025 | disco 102.025391

## 2.1 Cobertura: ¿toda campaña con artefacto tiene cifra verificada?

  17 campañas con metrics.json en disco, 17 cubiertas por CIFRAS
  ok   cobertura completa

## 3. Deltas del bootstrap citados vs 96-critica-verificacion.json

  ok   G1 − T1 (la de referencia del doc 89)        citado +0.141 | obs +0.141 IC[+0.032,+0.258]
  ok   R2 − R1 (sujeto vs escena, ambas 4,29 fps)   citado +0.072 | obs +0.072 IC[+0.013,+0.145]
  ok   R4 − R3 (sujeto vs escena, ambas 2 fps)      citado +0.137 | obs +0.137 IC[+0.032,+0.258]

## 4. Docs de procedencia referenciados

  35 docs referenciados; sin archivo en operacion/ ni nucleo/(+historicos/): ninguno

✅ Todo verificado
EXIT=0
```
