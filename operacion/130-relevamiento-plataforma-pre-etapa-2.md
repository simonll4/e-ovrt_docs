# 130 — Relevamiento exhaustivo de la plataforma antes de la Etapa 2 (2026-08-28)

> **Qué es.** El relevamiento que pidió el usuario antes de tocar §17.1: los **cinco repos de
> código** leídos contra lo que el set documental afirma de ellos y contra lo que el protocolo
> del informe (§17.1) prescribe, más una auditoría **documento contra documento** del propio
> set. Objetivo: que la alineación de punta a punta, el kit regenerado desde cero y el pase de
> §17.1 partan de una base verificada hoy, no de fotos del 08-05/08-15.
>
> **Cómo se hizo.** Seis agentes de solo lectura en paralelo (uno por repo + uno para `docs/`),
> cada uno con la lista de afirmaciones a verificar y el texto extraído de §17.1. Ningún
> servicio se levantó, ningún test pesado se corrió (WSL con 7,4 GiB); los conteos de tests son
> por `--collect-only` o por `grep "def test_"` según el repo. Los **cinco informes completos**
> (con tabla afirmación → veredicto → `ruta:línea`) están en
> [`datos/130-relevamiento-pre-etapa-2/`](datos/130-relevamiento-pre-etapa-2/) y son la
> evidencia; este documento consolida y decide.
>
> **Qué manda.** Sobre cualquier cifra o afirmación de estado anterior al 2026-08-28, manda
> este documento; donde este documento diga "declarar", el informe declara y no maquilla.
> Reemplaza como foto de plataforma a `operacion/97` (2026-08-05) en todo lo que difieren.

---

## 0. Veredicto en cinco líneas

1. **La plataforma está donde los docs dicen que está, en lo estructural.** Los seis repos
   tienen el árbol limpio (salvo `docs`, con el trabajo 08-25→08-28 sin commitear); los tres
   servicios HTTP + el bus, el pattern set `cr01_cr02_v2` (4.000/7.000 ms, `high`/`medium`,
   histéresis 2.000/3.000), el campeón `gdino-tiny-560` a `box_threshold 0,30`, `bench_v3`
   congelado (sha256 idéntico, `--verify` PASS byte a byte) y **las 26 cifras de los cuatro
   índices verifican contra sus `metrics.json`** (`96-verificar-indices.py` EXIT 0).
2. **Hay una afirmación ancla confundida**: la comparación `gdino-tiny` 800 px vs 560 px **no
   está a umbral igual** (0,35 vs 0,30). El campeón sigue siendo el campeón (0,551 es el dato
   de la combinación 560·0,30, y el par `base`/`base-560` sí está a 0,30 en ambos), pero "560 no
   degrada mAP respecto de 800" no puede afirmarse para tiny sin ese caveat.
3. **Tres desvíos de doc que llegarían al informe si no se corrigen**: el orden de arranque live
   real es **control → distribución → medios** (no "distribución primero"); el fine-tuning
   **excluyó `chv`** (2.203 css + 743 ppe_siabar = 2.946) y varias fichas dicen que entrenó con
   él; y el rango 500–2.000 imágenes de la Tabla 28 de §17.1 **se desvió a 2.946 sin
   justificación escrita**.
4. **Lo que §17.1 prescribió y no se ejerció está identificado, ítem por ítem** (§4): variantes
   template, vocabulario aislado-vs-completo cruzado, español, doble anotación/kappa, MOT17/OVT-B,
   NVDEC, Precision/Recall por severidad en el evaluador, percentiles de `t_alert-system` en
   `evaluate-alerts`, hardware/entorno en el manifiesto de corrida, warm-up de unidades. Nada de
   eso se "corrige" en §17.1: se **declara** donde corresponde (§17.4/§17.5) y §17.1 se ajusta
   sólo en lo que es decisión de protocolo.
5. **Conteos vencidos por todos lados** (tests 643/646/641/668, "39 tests", "16 campañas",
   "19 cifras", "4 estados", "11 endpoints"): ninguno llega al informe, pero todos viven en
   docs que el kit reparte. Se corrigen en este pase (§7).

---

## 1. Estado de los seis repos al 2026-08-28

| Repo | Rama | HEAD | Árbol | Tests medidos hoy | Nota |
|---|---|---|---|---|---|
| `e-ovrt_media-plane` | `feature/inference-service` | `f439db2` (08-22) | limpio | **643** `def test_` (grep; docs decían 646 y 641+5) | venv 3.12.13; Dockerfile CUDA 12.4 con ruedas cu13 pineadas — build nunca ejecutado |
| `e-ovrt_control-plane` | `feature/control-service` | `64cc976` (08-19) | limpio | **312** (collect-only, sin `tests/labs`) + 22 labs | venv 3.14.4 (`requires-python >=3.11`); 12 endpoints en `:8081` |
| `e-ovrt_alert-distribution` | `main` | `f9447a1` (08-19) | limpio | **133** + 1 integración MQTT deseleccionada por default | venv 3.11.15; Dockerfile 3.11-slim |
| `e-ovrt_experimental-setup` | `feature/webconsole-consola-tesis` | `2bfb268` (08-22) | limpio | `tests/` **88** · `finetuning/tests` **46** · BFF **668** (docs decían 643) | compose 13 servicios válido por lectura; `results/finetuning/` no existe (cifras FT en `finetuning/manifests/`) |
| `e-ovrt_datasets` | `feature/datasets-v2-setup` | `6524e21e` (08-20) | limpio | **431 passed** (1,6 s) | `build_bench_strata.py --verify` **PASS ×2**; sha256 `bench_v3.json` = manifiesto |
| `docs` | `main` | `8a0b74a` (08-23) | **57 cambios sin commitear** (08-25→08-28) | `herramientas/tests` 62 + 51 subtests | deuda git del usuario, anotada |

---

## 2. Lo que se confirmó — hechos citables por módulo

*(cada uno con `ruta:línea` en el informe del agente correspondiente)*

**Plano de medios.** Campeón `IDEA-Research/grounding-dino-tiny` a **560×560, `box_threshold`
0,30, `text_threshold` 0,25, NMS IoU 0,50, fp16**, warm-up de modelo al cargar + `prepare_run`
por corrida. G2A se mide **desde el dequeue** (el proceso ya leyó el frame) **hasta el fin de la
inferencia**; presupuesto 50–250 ms evaluado sobre P95; `capture_to_host` (sensor → dequeue)
existe **sólo para OAK-D** — en RTSP ese tramo no se midió. Bus XPUB `:5557`, msgpack
`bus.envelope.v1`, `seq` monótono aunque se descarte, payload byte-idéntico al JSONL, cierre
`run.lifecycle.v1/run_finished`. Un modelo por proceso (`EOVRT_MODEL_REF`), un run activo (409;
**una preview también bloquea**). Fuentes: `image_folder` (no recursivo), `video_file`, `rtsp`,
`oak_d`; preselección EN-2 default off, fail-open, sólo `oak_d`. Artefactos por run:
`effective_config.yaml`, `run_manifest.json`, `detections.jsonl`, `metrics.jsonl`,
`summary.json` (`media.summary.v2`), `run_provenance.json`, `dropped_units.jsonl` — **no existen
`report.json` ni `metrics.json` en este plano** (son del control-plane / experimental-setup).
El campo `run.scenario` **no clasifica nada** (los 472 runs locales dicen `DBE`, incluidos 73
`oak_d` y 21 `rtsp` live): DBE/EBE se distingue por `source_type` + `bus.enabled`.

**Plano de control.** Máquina de **cinco** estados `inactive → candidate → confirmed →
sustained → resolved`; alerta sólo al entrar a `confirmed`; reapertura `resolved → candidate`,
nunca a `inactive`. `cr01_cr02_v2`: CR-01 `high` 4.000/2.000 ms, CR-02 `medium` 7.000/3.000 ms,
escena, **sin cooldown ni memoria** (la capacidad existe en el código, desactivada y no
configurada). Umbrales en ms rigen cuando hay `timestamp_ms`; frames sólo fallback declarado
inerte sobre imágenes (ADR-013). ADR-011 cableado: el motor emite en cada confirmación; el
evaluador cuenta `re_alerts` fuera del denominador de precisión; FP = evento de alerta fuera de
toda ventana de episodio y sub-umbral; ventanas CR-01 [t0+4 s, t0+10 s], CR-02 [t0+7 s, t0+20 s].
Persistencia implementada como **duración desde la primera evidencia con tolerancia a huecos**
(< `resolve_after_ms`), no como proporción de frames positivos. Hitos persistidos **4 de 5**:
`first_evidence_ms` y `alert_registered_ms` monotónicos; candidato/confirmado en
`pattern_events.jsonl` con tiempo de fuente; notificación fuera del repo. `t_alert-system` cierra
en `alert.timestamp_ms` (reloj de fuente del frame que confirmó), no en el registro interno. G1
= `input.track_persons` decora la fuente con un tracker IoU por `source_id`; sin `track_id`
degrada a escena con causa `no_track_id`; verificado en live.

**Distribución.** `t_alert-notification = puback_wall_ms − ts_publish_ms` (**bus de alertas →
PUBACK QoS 1**, dos relojes de pared del mismo host, no monotónico, declarado): p95 **64,534 ms
n=460**; sostenido (2.ª+) **102,025 ms n=104**; 1.ª entrega 49,869 n=356. **No arranca en la
confirmación del patrón** sino en la publicación en el bus. Idempotencia por
**(`notification_id`, `channel`)**, `notification_id = sha1(alert_id)[:16]`; **cinco outcomes**
`delivered / failed / skipped_duplicate / dead_letter / suppressed_cooldown`; `dead_letter` tras 3
intentos con 500 ms fijos. **QoS 1 es el único valor admitido**; topic `eovrt/alerts/<severity>`.
El **cooldown es política de re-notificación del distribuidor** (clave `(condition_id,
source_id)`, 30 s, en memoria; en la campaña 118: 376/836 suprimidas = 44,98 %). Broker de la
**medición** = `amqtt 0.11.3`; Mosquitto es el broker del **despliegue** (compose, sin build).
Runner: HTTP por default; subproceso sólo con `EOVRT_CONSOLE_DISTRIBUTION_TRANSPORT=subprocess`, y
ese fallback no funciona en el compose.

**Orden de arranque live REAL** (runner `runner.py:1095-1149`): **control** (con
`alert_bus.enabled` y `wait_for_subscriber_ms ≥ 10 s`) → **distribución** (necesita
`control_run_id`) → **medios**. La no-pérdida en `:5558` la garantiza el handshake XPUB del
publicador, **no el orden**. El orden "medios ← control ← distribución" que dicen el `CLAUDE.md`
raíz, el README de FIG-A y la nota de `128` §4 **es falso**.

**Datos.** `bench_v3.json`: 6.477 imágenes / 55.165 anotaciones; `stratum` con **cuatro**
valores (`shel5k` 5.000 · `chv` 1.330 · `bench_obra_val` 85 · `bench_obra_test` 62 — el
informe habla de tres estratos fusionando los dos de obra); anotaciones `person` 24.172 ·
`helmet` 22.949 · `bare_head` 6.181 · `vest` 1.863. GT persona CR-01: bench_obra 60 + shel5k
5.248 = **5.308 con el GT vigente**; el **n=5.313** que citan CLAUDE.md, contexto base, los
índices y los docs 64/66 es el del GT del 23-jul (65 en bench_obra, antes del fix del 29-jul):
es el n de aquella medición y se cita así, fechado. CR-02: **142** violadores, sólo en
`bench_obra`. Fine-tuning efectivo (`finetuning_v1`): **`construction_site_safety` 2.203 +
`ppe_siabar` 743 = 2.946 train / 483 val; `chv` excluido** (100 % de sus 1.330 imágenes es
estrato del banco). De los 9 datasets de la Tabla 26 de §17.1, **2 se usaron** (SHEL5K y CHV,
ambos sólo como fuentes del banco), 1 tuvo uso lateral (MOCS, en copia Roboflow de 1.471
imágenes, no el original de 41.668), 6 se descartaron; **los dos datasets que se entrenaron y
la fuente de `bench_obra` no figuran en la Tabla 26** (investigación Roboflow del 06-17).

**Índices de resultados.** `96-verificar-indices.py`: ✅ 1.452 enlaces / 0 rotos · 26 cifras
sobre 17 campañas · 3 deltas bootstrap · 35 docs de procedencia. Todas las cifras del "Estado
vigente" del kit y de los "cuatro números" coinciden con los `metrics.json` (47/32/15/37,
manifiesto `3f14f50a…`; 0,789 / 0,930 / 0,146; T1 y T2 con todas sus cifras). Única no
verificable mecánicamente: mAP50 0,551 (sin `metrics.json` en el repo; remite al doc 64).

---

## 3. Divergencias doc ↔ código, consolidadas

Severidad: 🔴 llegaría al informe como afirmación falsa · 🟠 contradicción entre documentos o
cifra vencida que el kit reparte · 🟡 higiene. "Dueño" = dónde se corrige. Estado al cierre de
este pase en §7.

| ID | Sev. | Hallazgo | Dueño / dónde corregir |
|---|---|---|---|
| **R-01** | 🔴 | **Orden de arranque live**: docs dicen distribución → control → medios; el runner hace **control → distribución → medios** y la garantía es el handshake XPUB (≥10 s), no el orden. | `CLAUDE.md` raíz ("Acople entre planos" y párrafo de alert-distribution) · `figuras/README.md` FIG-A (nota + revisar el SVG/PNG) · `128` §4 nota de figuras · `experimental-setup/infra/platform/README.md:69-70` y `docs/experiments.md:93-96` (repo del usuario) · glosario `13:109` ("distribución posterior" → concurrente) |
| **R-02** | 🔴 | **Fine-tuning con `chv`**: AJ-2.07 ✎08-18 (b), R-24 (b), glosario §5, doc 99 §2 y `datasets_metadata.yaml` dicen que se entrenó con css+chv+ppe_siabar; el FT real excluyó `chv` (anti-leakage). Copiarlo al informe violaría la propia Tabla 28. | `ajustes/02` AJ-2.07 · `93` R-24 · glosario `13` §5 · `99` §2 · registry (repo datasets, del usuario) |
| **R-03** | 🔴 | **Tabla 28 de §17.1: rango 500–2.000 imgs** vs 2.946 train, sin justificación en ADR-017 / doc 100 / README de finetuning. | Declarar en §17.4/§17.5 (fila FT) con causa (100 % de linajes elegibles tras dedup y exclusión del banco; F-127.1 muestra que aun así es insuficiente). Anotar en `ajustes/02` AJ-2.11 y `ajustes/05` AJ-5.13. |
| **R-04** | 🔴 | **`gdino-tiny` 800 px corrió a `box_threshold` 0,35 y `gdino-tiny-560` a 0,30** en todas las corridas (07-23 incluidas); doc 64 no lo registra. "560 = igual o mejor mAP que 800" está confundido en el par tiny (el par base sí está a 0,30 en ambos: 0,453 vs 0,401). | `64` ✎ (declarar el umbral por brazo; reescribir como "560 @0,30 ≥ 800 @0,35") · `CLAUDE.md` raíz (párrafo del campeón) · `results/bench_imagenes/index.md` (repo del usuario) · kit: citar siempre el par (resolución, umbral) |
| **R-05** | 🟠 | **`evaluate-alerts` sólo produce promedios** de `t_alert`/TTFD/SDR y no persiste latencias por episodio ⇒ los P50/P95/P99 de §17.1.7.8.1 no salen del evaluador; el kit declara `t_alert-system` citable sin decir que es un promedio por campaña. | kit "Estado vigente" (precisar "promedio por campaña; percentiles sólo del tramo de plataforma en `summary.json`") · §17.4 declara PARCIAL |
| **R-06** | 🟠 | **Precision/Recall por severidad (§17.1.7.5.5) no existe en el evaluador**; sólo el desglose por condición aguas abajo (1:1 con severidad). | §17.4/§17.5: citar P/R por condición y decir que equivale a severidad porque cada CR tiene una sola |
| **R-07** | 🟠 | Glosario `13` §3 y contexto base (`:729`) dicen **4 estados** del motor; son **5** (`sustained`), como el propio kit dice más abajo y FIG-E. | glosario `13` §3 · generador del kit |
| **R-08** | 🟠 | Causa two-node: docs dicen `cross_node_monotonic_clock`; el código emite **`clock_skew`** (control-plane y experimental-setup). ADR-0006 local atribuye `not_applicable:no_ground_truth` al control-plane; lo emite `report.py` del experimental-setup. "11 endpoints" → 12. | glosario `13` · `estado-de-implementacion-adrs.md` (ADR-0006/0008 de la serie de 4 dígitos) · ADRs locales (repo control-plane, del usuario) |
| **R-09** | 🟠 | **Containerización "diferida / fuera de alcance"** en ADR-019 §4, spec 45 §9.8, 124, 125, kit y GUIA — pero Dockerfiles ×3 + compose de 13 servicios existen desde 08-19/20. Lo diferido es **build + smoke**. | ADR-019 ✎ · spec 45 ✎ · `124`/`125` ✎ · generador del kit · GUIA |
| **R-10** | 🟠 | **Broker de la medición 118 = `amqtt`**, no Mosquitto (nucleo/19 §5, spec 45 §5). Además `t_alert-notification` **arranca en `ts_publish_ms` del bus**, no en `confirmed_at_ms` como aún discuten spec 45 §3 y nucleo/19 §6.1. | nucleo/19 ✎ · spec 45 ✎ · kit |
| **R-11** | 🟠 | **`n=5.313`** (CLAUDE.md, contexto base ×4, índices, docs 64/66) es el GT del 23-jul; el vigente da 5.308. | Citar fechado: "n=5.313 (GT del 23-jul; 5.308 con el GT vigente)". `CLAUDE.md` raíz · generador del kit · índice (repo del usuario) |
| **R-12** | 🟠 | **Conteos de tests vencidos**: BFF 643→668; media-plane 646/641→643 (grep); distribución "39"/"37"→133+1; "2.203 tests" (op97) es foto del 08-05. | `CLAUDE.md` raíz · generador del kit · `114` · README/requirements del experimental-setup (usuario) |
| **R-13** | 🟠 | **Tabla 26 de §17.1** vs registry: GDUT-HWD "Apache-2.0" / SHWD "MIT" → "verificar" (nunca descargados); CHV "CC BY 4.0" es del **paper**, el dataset no tiene licencia (L7); MOCS descrito como original (41.668, NC) → lo usado es copia Roboflow 1.471. **Omite** css y ppe_siabar. | Es material del pase de §17.1 (AJ-2.07 / PODA-12): la Tabla 26 se comprime a "utilizados + descartados con causa" y las licencias se escriben como están en el registry |
| **R-14** | 🟠 | **Auditoría humana del GT (Task 4.3)**: `bench_gt_audit.md` §4–6 vacíos y docs 75/78 "sin ejecutar", pero `estado_avance.md` y el README de documentation la dan por ejecutada (sólo se generó el kit). | repo datasets (usuario); en el informe **no afirmar** que hubo auditoría humana del GT de imágenes |
| **R-15** | 🟠 | `CLAUDE.md` raíz: bloque "emits… `train_v2`/`bench_v2`/`demo_v2`" vencido (archivadas 08-15, el propio archivo lo dice más abajo); no lista `download_shel5k.sh`; "las fuentes exponen `request_stop()`" (es `RunControl.request_stop()` en medios; `BusSource.request_stop()` en control). | `CLAUDE.md` raíz |
| **R-16** | 🟠 | `report.json`/`metrics.json` citados como artefactos del media-plane (AJ-2.09) — no existen ahí (`summary.json` + `metrics.jsonl`). `effective_config.yaml` imprime campos inertes de la otra familia (`confidence_threshold 0,25` en GDINO; `box_threshold 0,35` en YOLOE): trampa de cita. | `ajustes/02` AJ-2.09 · glosario `13` §4 (regla de lectura: GDINO = `box`+`text`+`iou`; YOLOE = `confidence`+`iou`) |
| **R-17** | 🟠 | G2A del código **no incluye sensor ni red** (dequeue → fin de inferencia); declarado como F-101.8 para OAK-D, pero para **RTSP el tramo faltante no se midió** (no sólo "sumar 202–217 ms"). | kit / GUIA trampa · §17.4/§17.5 |
| **R-18** | 🟠 | `finetuning/README.md` cierra en T1 (08-17), sin T2 NO-GO; manifiestos de `experiments/` que ya no resuelven (`mock_chv`, `video_annotated*`, 4 `mmgdino`); README raíz con estados de prompt sets vencidos. | repo experimental-setup (usuario) |
| **R-19** | 🟡 | Glosario `13` §6 omite `e-ovrt_alert-distribution` en "Repos de código" (y lista `:8082`); §4.2 "16 campañas" → 17; GUIA §7 "19 cifras / 16 campañas" → 26 / 17. | glosario `13` · GUIA |
| **R-20** | 🟡 | `114` §4 brechas cerradas sin ✎ (ledger por generaciones, venv 3.11, Dockerfile, runner orquesta, layout `runs/exp_<id>/distribution/`); `114`/`118` puertos sin `:8082`; nucleo/19 §4.6 omite `latency_mode`/`experiment_id`; "el ledger es obligatorio porque QoS 1 duplica" mezcla dedup del publicador con re-entregas broker→suscriptor. | `114` · `118` · nucleo/19 |
| **R-21** | 🟡 | Percentiles del media-plane con método mixto (p50 mediana interpolada; p95/p99 por índice), `capture_to_host` sin p99; `run_manifest.json` sin hardware/SO/versiones (§17.1.7.8.1 lo exige); `warmup_units` = 0 en los 472 runs (warm-up de **modelo** sí; de **unidades** no). | §17.4 declara; kit trampa |
| **R-22** | 🟡 | Datasets: "3 estratos" vs `manifest.strata` = 4; shel5k "416×416 uniforme" (real 416×415/416×416/415×416/415×415); `bench_v3.md` no cita `person_gt_bench_obra_v2.json` (CR-02, 142); `ppe_siabar` con dos `source_url`; `construction_ppe_skcet` fuera de `datasets_metadata.yaml`; `bench_v3.py` no chequea duplicados **entre** estratos (verificado ad hoc: 0 basenames repetidos). | repo datasets (usuario) · glosario §4.4 ya explica la fusión |
| **R-23** | 🟡 | Manifiesto del clip bench con `annotator: null` en los 34 clips del Bloque A (los 13 del B: `simon`). No contradice "GT humano"; procedencia por clip incompleta. | repo experimental-setup (usuario) |

---

## 4. Protocolo §17.1 vs lo construido — la tabla que alimenta el pase de la Etapa 2

Leyenda: **✅ CUMPLIDA** · **◐ PARCIAL** · **⊘ NO EJERCIDA** · **↯ DESVIADA** (se hizo distinto,
con causa). Regla de uso: lo ✅ y lo ↯ que sea *decisión* puede reflejarse en §17.1 como protocolo
ajustado; lo ⊘ y lo ◐ que sea *resultado de ejecución* **se declara en §17.4/§17.5**, nunca se
borra de §17.1 (guardrail `07` §9; mapa regla 5).

### 4.1 Entorno (§17.1.4)

| Prescripción | Estado | Evidencia / qué declarar |
|---|---|---|
| CPN: HP Victus, RTX 4060 Laptop 8 GB, **Windows 11** | ↯ | Corre en **Linux (WSL2)** y Docker Ubuntu; el repo no registra el SO en los artefactos. §17.1.4.2.1 puede seguir describiendo el hardware; el SO se corrige como decisión. |
| NVDEC para decodificar en GPU (§17.1.4.2.2) | ⊘ | `cv2.VideoCapture` software; 0 referencias a nvdec/cudacodec. Declarar en §17.4. |
| EN = OAK-D Pro PoE; inferencia en borde sólo como variante condicionada | ✅ | `oak_d_source.py` (DepthAI v2); EN-2 default off, medida aparte (87 % drop). |
| Contingencia: cámara IP por RTSP (§17.1.4.2.4) | ✅ (y **se ejerció primero**) | `rtsp_source.py`; 21 runs `rtsp`. → AJ-2.10. |
| Stack oficial GDINO/YOLOE, GPU NVIDIA | ✅ | Transformers + Ultralytics; torch 2.12.1. |
| Exportación PyTorch / TensorRT / ONNX (§17.1.4.3.3) | ◐ | Sólo PyTorch nativo. |
| Escenarios A (DBE) y B (EBE) | ✅ | Por fuente + `bus.enabled`; **no por el campo `scenario`**. |
| Parámetros de referencia ≈640 px (Tabla B.6) | ↯ | YOLOE 640; GDINO **560** (campeón) y 800; el propio §17.1.7.7.5 exige recalibrar si difiere de 640 → se cumplió por selección S1/S2 (con el caveat R-04). |
| Restricción VRAM 8 GB | ✅ | `gpu_memory_peak_mb`, fp16 default. |

### 4.2 Condiciones, patrones y prompts (§17.1.5)

| Prescripción | Estado | Evidencia / qué declarar |
|---|---|---|
| Tres niveles de severidad | ◐ | `high`/`medium` ejercidos; `critical` no (PR-03…06 excluidos, E-01/E-02). |
| Persistencia en segundos (3–5 / 5–10) | ✅ | 4.000 / 7.000 ms dentro del rango. → AJ-2.01 como **decisión dentro del rango**. |
| "Sostenida o con proporción mínima de positivos" | ↯ (variante declarada) | Duración desde primera evidencia con tolerancia a huecos < `resolve_after_ms`. Declarar en §17.3/§17.4. |
| Histéresis activación ≠ desactivación | ✅ | 4.000/2.000 y 7.000/3.000. Ya pedida por §17.1.5.3.3 — no es agregado. |
| Calibración empírica FP vs ventana | ⊘ | Umbrales fijados por Tabla 24/D.4; sin barrido. Declarar en §17.5. |
| Estados inactivo/candidato/confirmado/resuelto | ✅ (+`sustained`) | Cinco estados; FIG-E. |
| "Evita alertas repetidas sobre una misma situación" | ↯ deliberada (ADR-011) | El motor re-alerta tras resolver (`re_alerts`); la supresión es del distribuidor. → AJ-2.02 se resuelve como **regla de conteo** (D-E2-3), no como "el §17.1 arrastra el cooldown" (no lo menciona). |
| Estrategias directa vs indirecta comparadas | ✅ | D1 Nivel A (2 estratos) + Nivel B con veto pre-registrado. → **D-E2-2: bautismo E-DIR/E-IND/E-HYB en §17.1.5.4.2**. |
| Eje "contexto de vocabulario": cada prompt **aislado y en vocabulario completo** | ↯ | Régimen asimétrico declarado (E-DIR aislada, E-IND conjunta); ningún prompt en ambos; sustituido por un control único (B1 vs T2: +1 palabra = −0,082 F1). → AJ-2.04.1 se escribe como **decisión de protocolo** y §17.5 reporta el control. |
| Variantes con template ("a photo of a [CLASS]") | ⊘ (definidas, no medidas) | `cr01_template`/`cr02_template` con `enabled_by_default: false`, excluidas de D1. → AJ-2.04.2: §17.1 las mantiene como eje; §17.5 declara no ejercidas. |
| Hiperparámetros congelados entre variantes | ✅ (con matiz) | `box 0,30 / text 0,25` idénticos en todos los brazos; umbrales operativos calibrados por brazo con grid idéntico y reportados como variable (permitido). |
| Especificidad / estructura sintáctica | ◐ | Sólo dentro de E-DIR (`cr01_spec`); E-IND siempre `person`. |
| Idioma inglés; español complementario | ✅ / ⊘ | Todos los sets `language: en`; español = E-09 excluida. |
| Catálogo de candidatos (Tabla C.1) | ✅ | `prompts/_archive/*candidates.yaml` → finalistas `edir_v1` (8 formulaciones, acta doc 76). → AJ-2.07. |
| Piso ~200 positivos por condición o n + IC | ◐ | CR-01 shel5k 2.487 ✅; CR-01 bench_obra 28 y CR-02 82 ✗ → IC95 bootstrap (vía prevista) → **L8**. → AJ-2.05 (la vía se declara en §17.1; el n en §17.5). |
| Doble anotación ≥20 % + kappa + IoU | ⊘ (declarada **L2**) | `double_annotation_ratio 0.0`; en imágenes se reutilizó GT existente; la auditoría humana Task 4.3 **no se ejecutó** (R-14). → AJ-2.06. |
| Matriz (modelo × condición × prompt × contexto) | ◐ | `tiny-560` + réplica `base-560`; CR-01/CR-02; 6 variantes E-DIR + E-IND; **un régimen por brazo**. |
| Confianza media de los TP por formulación | ⊘ | No figura en `metrics.json`. → AJ-2.07 la pide: queda como criterio en §17.1, no ejercido en §17.5. |
| Métricas por entidad componente (indirecta) | ✅ | AP por clase/estrato + Nivel A por persona. |

### 4.3 Datos (§17.1.6)

| Prescripción | Estado | Evidencia / qué declarar |
|---|---|---|
| Inventario Tabla 26 (SH17, SHEL5K, CHV, Pictor-PPE, Construction-PPE, GDUT-HWD, SHWD, SODA, MOCS) | ↯ | Usados: SHEL5K y CHV (sólo banco); lateral: MOCS (copia Roboflow, piloto A1); descartados: 6. **Entrenaron css + ppe_siabar, ausentes de la tabla.** → PODA-12 + AJ-2.07: comprimir a utilizados + descartados con causa; licencias como en el registry (R-13). |
| Tabla 28: disyunción · test compartido · semilla · splits oficiales · congelamiento previo | ✅ | `finetuning_v1.summary.json` (overlap 0, seed 42, `bench_v3_sha256`); bench congelado 07-23, FT 08-15+. |
| Tabla 28: **rango 500–2.000** | ↯ **sin justificar** | 2.946 train. → R-03: declarar en §17.4/§17.5. |
| Tabla 28: no solapamiento cruzado | ✅ train / ◐ bench | Dedup perceptual en train; sin chequeo inter-estrato en bench (ad hoc: 0 repetidos). |
| MOT17 / OVT-B (Tabla 30) | ⊘ (E-10, ADR-015) | 0 menciones en el repo. → **D-E2-6: intacto con ⊘ explícito**. |
| Contraste con métricas de la literatura sobre el mismo dataset (§17.1.4.4.1) | ⊘ | Ningún índice compara con cifras publicadas de SHEL5K/CHV; `bench_v3` es composición propia. |
| Consideraciones éticas / AAIP | — | `[[PENDIENTE]]` de D-E1-11 viaja en espejo a §17.1.11 (D-E2-7). |

### 4.4 Métricas e instrumentación (§17.1.7)

| Prescripción | Estado | Evidencia / qué declarar |
|---|---|---|
| G2A = t_capture + t_transport + t_preprocess + t_inference | ↯ (declarada) | Código: dequeue → fin de inferencia; sensor→dequeue sólo OAK-D (`capture_to_host` 202–217 ms); **RTSP sin ese tramo**. §17.1.7.7 conserva la descomposición (§16.5 la cita); §17.4 declara qué tramo se midió. |
| Presupuesto 50–250 ms sobre P95 | ✅ instrumentado | `p95_within_budget`; live GDINO fuera de presupuesto (630–890 ms). |
| `t_alert-system` = inicio anotado → alerta registrada | ✅ (reloj de fuente) | Cierra en `alert.timestamp_ms`, no en `alert_registered_ms`. Declarar. |
| `t_alert-notification` complementaria, sólo con trayecto instrumentado | ✅ | Tramo bus→PUBACK; **no arranca en la confirmación**; no llega a interfaz/cliente (◐ Tabla 33). |
| TTFD y SDR | ✅ | En tiempo (ms); criterio declarado; no aplicable declarado. |
| Métricas temporales sólo sobre secuencias | ✅ | ADR-013; `not_applicable:non_temporal_source`. |
| **P/R por severidad** | ◐ | No en el evaluador; por condición aguas abajo (1:1). → R-06. |
| Cinco hitos por alerta | ◐ 4/5 | Notificación fuera del control-plane; candidato/confirmado con reloj de fuente. → AJ-2.09: §17.1 no cambia; §17.4 lo dice. |
| **P50/P95/P99 + promedio** | ◐ | Media: `summary.json` ✅ (método por índice, p50 interpolada). Control: `summary.json` ✅ / `evaluate-alerts` **sólo promedios**. Distribución: `metrics.json` ✅ / summary por corrida sólo min/mean/p95. → R-05. |
| Warm-up previo declarado | ◐ | Modelo sí (carga + `prepare_run`); `warmup_units` = 0 en todos los runs; control sin warm-up (0,2 ms/unidad, irrelevante); distribución no declarado (1.ª entrega más rápida, no infla). |
| Timestamps monotónicos con fuente declarada | ✅ / ↯ distribución | Medios y control monotónicos + `source_clock`; distribución con dos wall-clocks del mismo host (declarado). |
| Declarar hardware y entorno por corrida | ◐ | `effective_config` + `run_provenance` ✅; **GPU/torch/driver/SO/hostname no se registran**. |
| Unidad de conteo del FP declarada e invariante | ✅ | Evento de alerta fuera de ventanas; `re_alerts` fuera del denominador. → D-E2-3 escribe la regla en §17.1.7.8.3. |
| GT inexistente ⇒ no aproximar | ✅ | `not_applicable:*`, censura, clip negativo no evaluable. → AJ-2.12. |
| Métricas MOT (HOTA, IDF1…) | ⊘ (E-10) | Sin GT de identidades. → D-E2-6. |
| Protocolo comparativo preentrenada vs ajustada (§17.1.7.6): ΔAP, ΔRecall ✅ · ΔPrecision, ΔSDR, Δt_alert, ΔTTFD ⊘ · retención OV ✅ T2 / no medible T1 · latencia ⊘ · horas-persona ⊘ | ◐ | Los checkpoints ajustados **sólo se evaluaron en DBE-imágenes**, nunca en clips ni EBE. §17.1 conserva el protocolo; §17.5 fila FT lo declara. |
| Fases de la Tabla 36 | ✅ (orden ↯ declarable) | Orden real: Preparación → Baseline DBE imágenes (07-23) → **EBE rodaje (07-25)** → GT video → Nivel B base → sensibilidad de prompts (08-03/04) → tracking/densidad → EBE blindado → Reporte → estrato B → distribución → **fine-tuning último (08-15→21)**. La formulación primaria se congeló **antes** del estudio de sensibilidad. → AJ-2.08: nombres de fase sí; el orden se declara en §17.4. |
| Adaptación: máx. 2 candidatos GDINO y YOLOE (§17.1.9.2) | ◐ | Sólo YOLOE-26s ajustado (T1 lineal, T2 completo); GDINO no (T3 diferido con causa técnica). → AJ-2.11: regla y criterio en §17.1; la jornada en §17.4/§17.5. |

---

## 5. Set documental — auditoría documento contra documento

Informe completo: [`datos/130-relevamiento-pre-etapa-2/docs-set.md`](datos/130-relevamiento-pre-etapa-2/docs-set.md)
(37 hallazgos nuevos además de los 12 de `revision-previa-etapa-2.md` §3: **6 🔴 · 13 🟠 · 18 🟡**;
26 llegan al kit porque su archivo es fuente del generador). Los 🔴:

| # | Dónde | Qué decía | Qué manda |
|---|---|---|---|
| 1 | `sintesis/fundamentos-teoricos.md` ~L605-616 | E-04 "NO-GO T1… último eslabón: full-authorization + RUN manual" | jornada cerrada (`123`/`127`/`128`) |
| 2 | `operacion/97` (foto 08-05) vendido como "ESTADO VIGENTE" por `00-indice` y GUIA | "4 repos", "dos servicios HTTP", "distribución MQTT no implementada"; sin un solo ✎ | 5 repos, tres servicios, distribución implementada y medida (118); superado por este doc |
| 3 | `informe/project-kit/README.md` | cuarto archivo de knowledge = `…17.3…v1.1.docx` / `…17.4…v1.2.docx` (no existen); tabla de estado con §17.4 v1.5; orden 6→1→2→0 | knowledge = contexto base + paquete de etapa + DOCX base de formato + `.docx` vigente de la sección (v1.0 / v1.0 / v1.4 / v1.6 / v1.3) |
| 4 | `generar_project_kit.py` L183 vs L143/`STAGE_CONTRACTS[1]` | "podas 01 a 11: NINGUNA aplicada" y "podas 01-11 aplicadas" en el mismo paquete | aplicadas (Etapa 1 cerrada) |
| 5 | `GUIA-REDACTORES.md` ~L117, ~L397 | "§17.4, §17.5 y §17.6 están vacías / desde cero" | 17.4 v1.6 y 17.5 v1.3 existen; falta 17.6 |
| 6 | `informe/ajustes/08-manual` L13 + tablero §5 + L26 + L129 | "109 unidades. Cero aplicadas", 100 % `[ ]`, "no existe script de extracción", "la vara no existe" | Etapa 1 cerrada con 16 AJ-1 + podas 01–11; 17.3/17.4/17.5 con pases aplicados; extractor y verificador existen; la vara está escrita |

**Contradicciones doc↔doc (mismo hecho, dos versiones)** — resueltas en §7: qué son los "cuatro
archivos" de knowledge · dónde nacen E-DIR/E-IND/E-HYB (D3/C-1 vs E3-42 → cerrado por D-E2-2) ·
estado del kit vs sus fuentes (generador "aplicado" vs tableros "cero") · podas 01–11 · containerización
"diferida" vs "definida" · verificador "19 cifras/16 campañas" vs 26/17 · acople de la distribución
(ADR-018 vs ADR-020 en `ajustes/04`) · plan de tablas de §17.5 (7 vs 6) · alcance de la Etapa 1 ("con
Anexo A" vs "sólo desarrollo") · banco "34 clips = resultado principal" vs 47/Bloque A. Enlaces
rotos: `00-el-informe-hoy` L223 (pase 5 → `archivado/`), `08-manual` L271, `project-kit/README`.

**Coinciden sin fisuras (no tocar):** campeón y `bench_v3`; 47/32/15/37; jornada E-04 cerrada (salvo
los dos ecos); cifras sólo de los 4 índices; L1–L8; G1 medida / MOT excluida; dos patrones / tres
servicios (salvo `operacion/97`); distribución verificada (p95 64,534 ms); autocontención y
marcadores; 17 tablas + 6 figuras; versiones vigentes v1.0/v1.4/v1.6/v1.3.

---

## 6. Decisiones firmadas hoy para la Etapa 2

| ID | Decisión | Firma |
|---|---|---|
| **D-E2-1** | El documento de trabajo de la etapa es **sólo §17.1**; los Anexos C y D se corrigen aparte y quedan en `90g` para el equipo (como el Anexo A en `90e`). | usuario, 2026-08-28 |
| **D-E2-2** | **Bautismo E-DIR / E-IND / E-HYB en §17.1.5.4.2** (C-1 del pase 1) y **recorte de la glosa de §17.3.6.4 a una remisión** (dependencia inversa de E3-42; §17.3 v1.4 → v1.5). | usuario, 2026-08-28 |
| **D-E2-5** | **Ficha nueva AJ-2.13**: el nivel intermedio "estado observable por persona" se declara en §17.1.7.3.1 como nivel de análisis (criterio de diseño, sin cifras), para que §17.5 tenga de dónde colgarlo. | usuario, 2026-08-28 |
| **D-E2-6** | MOT17/OVT-B (§17.1.6.3) y métricas MOT (§17.1.7.4.2) **intactos, con ⊘ explícito** en el pase; lo no ejercido se reporta en §17.5 bloque 7. | usuario, 2026-08-28 |
| D-E2-3 | AJ-2.02 se resuelve como **regla de conteo** en §17.1.7.8.3 (la re-emisión por confirmación repetida no cuenta como FP); §17.1 no menciona cooldown, la ficha tenía premisa falsa. | recomendación adoptada |
| D-E2-4 | AJ-2.01: los 4.000/7.000 ms entran en §17.1.5.3.3 como **decisión de protocolo dentro del rango de la Tabla 24**, sin tocar la tabla y sin la palabra "efectivos" (casa única de los valores efectivos: §17.4). | recomendación adoptada |
| D-E2-7 | AAIP: `[[PENDIENTE]]` espejo en §17.1.11.1 con el mismo texto de D-E1-11. | recomendación adoptada |
| D-E2-8 | PODA-14 sólo recorta §17.1.4 y verifica que lo recortado esté en B.1–B.7; lo que falte se lista como alta al Anexo B para el equipo. | recomendación adoptada |

---

## 7. Qué cambió en el set a partir de este relevamiento (misma jornada, 2026-08-28)

Todo con bloques o notas `✎ 2026-08-28` y sin borrar texto histórico. **Nada commiteado** (los
commits los hace el usuario). Verificación al cierre: `herramientas/tests` **62 passed + 51
subtests** · `generar_project_kit.py --check --etapa all` **OK** · `96-verificar-indices.py` **EXIT 0**
· `datasets/tests` **431 passed** · FIG-A regenerada y revisada a ojo (① control · ② distribución ·
③ medios).

**Kit y sus fuentes directas (este proceso).** `herramientas/generar_project_kit.py`: etapa 2
redacta desde **`90f`** (nuevo, extraído de
`desarrollando/E-OVRT-VDP_Seccion_17.1_Consolidacion_Metodologica_v1.0.docx`, antes `17.1.docx`);
paquete 2 = `correcciones-etapa-2.md` + `90f` + Anexos C/D (`96e`) + este doc §4–§6 + pase 3 §E/§I +
`ajustes/02` + podas 12–14; `STAGE_CONTRACTS[2]` nuevo; `BASE_PREAMBLE` reescrito (Etapa 1 CERRADA,
17.4 v1.6, containerización "definida", orden de arranque real, campeón con umbral y n fechado,
cinco estados, `chv` excluido, G2A/RTSP, `t_alert-system` = promedio); notas D1–D4 con la excepción
D-E2-2; podas 01–11 "aplicadas"; etapa 4 recibe este doc §0–§4 y `97` degradado a histórico;
`STAGE_DESCRIPTIONS` 1/2. `90b` **re-extraído de v1.6**. `informe/project-kit/*` regenerado (8
archivos). `INSTRUCCIONES-PROJECT.md` (lista de `.docx` vigentes, `E2-`; 7.993 caracteres).
`informe/ajustes/02` (banner de arranque + ✎ en AJ-2.01/02/03/04/06/07/09/11/12, AJ-2.13 nueva, §3
ítems 4–5). `informe/entregable/00-el-informe-hoy.md` (entradas 🔎 y ✅ del 08-28, tabla de textos
base, banner de "Lo que está vacío", enlace del pase 5 reparado).
`desarrollando/archivado/{revision-previa-etapa-2,correcciones-etapa-2}.md` (nuevos).
`/home/simonll4/projects/CLAUDE.md` raíz: orden de arranque (R-01), campeón/umbral/n (R-04, R-11),
vistas `train_v2…` archivadas y `download_shel5k.sh` (R-15), `request_stop` (R-15), BFF 668 (R-12),
FT sin `chv` (R-02).

**Set de gobierno (agente editor, 40 archivos).** `informe/figuras/README.md` + `scripts/fig_a_*.py`
+ `fig-a-vista-de-procesos.{png,svg}` regenerados (R-01) · `128` §4 · `13-glosario` (runner
concurrente y orden real; 5 estados; `clock_skew`; 17 campañas; TRAIN/BENCH/DEMO archivados y FT
sin `chv`; quinto repo `:8082`; filas nuevas §4: umbrales por familia y `run.scenario`/artefactos) ·
`93` R-24 (b) + banner de casillas superadas · `94` §4 · `99` §2 · `64` y `61` (umbral tiny 800 @0,35
vs 560 @0,30; conclusión reescrita) · `estado-de-implementacion-adrs.md` (`clock_skew` ×2, 12 rutas
×2, `no_ground_truth` → `report.py`) · `adr-019` §4, `specs/45` §3/§5/§9.8, `124` §1/§5, `125` §7,
`GUIA` ~L337, `ajustes/04` ~L293 (containerización definida; diferido = build+smoke) · `nucleo/19`
(banner, §4.6, §5 amqtt/ledger, §6, §6.1 resuelto) · `114` §2/§4, `118` §3 · `GUIA` L117/L397/L143/
L390/§7 · `gobierno/97` L24, `98` L6, `99` L234/L320 · `operacion/97` banner SUPERADO · `00-indice.md`
(cabecera 08-28, fila 130, 97 superado) · `ajustes/08` (L13, L26, L129, tablero `[x]` AJ-1.01…16 y
PODA-01…11, nota de casillas 3/4/5, L275) · `ajustes/00-mapa` (título, banner, ✎) · `ajustes/01`,
`03` (banners de cierre) · `ajustes/04` (v1.6; ADR-018→020) · `ajustes/07` (banner; 11 casillas) ·
`ajustes/09` (§1, §2.1 seis tablas 62–67, DECISIÓN §2 `[x]`, §4 → pase etapa 2) · `92` L199/L695 ·
`informe/00-indice-informe.md` · `informe/project-kit/README.md` (knowledge vigente; nombres v1.1/v1.2
sólo como históricos) · `sintesis/fundamentos-teoricos.md` L616 · `nucleo/10` L288 y fila E-04 ·
`sintesis/resultados-y-conclusiones.md` (§5, §11, 26/17) · `122` banner de vigencia · `CRONOLOGIA.md`
(jornadas 08-25/27/28).

**Repos hermanos (agente editor, sólo `.md`/`.txt`).** `experimental-setup`: `infra/platform/README.md`
y `docs/experiments.md` (orden real; manifiestos huérfanos; `bench_v2` exploratory), `README.md`
(layout de prompts, tres servicios, 668, catálogo 7, MM-GDINO archivado, `runs/`),
`requirements-dev.txt` (668), `finetuning/README.md` (T2 NO-GO + desviación Tabla 28),
`prompts/_archive/README.md`, `results/bench_imagenes/index.md` (n fechado; caveat del umbral; tablas
y enlaces intactos, verificador EXIT 0). `datasets`: `documentation/estado_avance.md` y `README.md`
(Task 4.3 no ejecutada), `registry/bench_v3.md` (4 estratos; resolución shel5k; `person_gt_…_v2`;
11 tests; `chv` excluido del FT). `control-plane`: `docs/decisions/ADR-0006` (`clock_skew`,
`no_ground_truth`), `ADR-0008` (12 rutas), `README.md` (pattern sets de campaña),
`docs/architecture.md` (cooldown). `media-plane`: `README.md` (ids canónicos; preview ocupa el slot),
`docs/implementation-status.md` (643 por grep). `alert-distribution`: sin cambios.

**Quedó para los dueños (no es documentación):** R-14 completar o cerrar la auditoría humana del GT
(repo datasets); R-18 manifiestos huérfanos de `experiments/` (borrar o marcar); C.8/C.9/C.13/C.15
del control-plane (etiqueta `positive_criterion`, enum de severidad, `avg_ttfa_internal_ms`,
`wait_for_subscriber_ms` recomendado); `run.scenario` derivado en el media-plane; `annotator: null`
del Bloque A; los §17.4 (orden de disparo) y §17.3 (recorte de §17.3.6.4) se corrigen en sus etapas.

---

## 8. Cómo se re-verifica

```
# repos
for r in e-ovrt_media-plane e-ovrt_control-plane e-ovrt_alert-distribution e-ovrt_experimental-setup e-ovrt_datasets docs; do git -C $r log -1 --format="$r %h %cs"; git -C $r status --short | wc -l; done
# índices y banco
python3 docs/operacion/datos/96-verificar-indices.py                          # EXIT 0
cd e-ovrt_datasets && python3 datasets/scripts/curate/build_bench_strata.py --verify && python3 -m pytest datasets/tests -q
# los hechos de §2, por ruta:línea → datos/130-relevamiento-pre-etapa-2/<repo>.md §B y §E
# umbrales del campeón
grep -nE 'box_threshold|image_size' e-ovrt_media-plane/configs/models/grounding-dino/gdino-tiny*.yaml
# orden de arranque live
sed -n '1085,1150p' e-ovrt_experimental-setup/webconsole/backend/src/eovrt_webconsole/experiment/runner.py
```
