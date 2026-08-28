# Relevamiento técnico — `e-ovrt_datasets` contra documentación y protocolo §17.1

- **Fecha del relevamiento:** 2026-08-28. Solo lectura (sin edits, sin git write, sin descargas).
- **Objeto:** `/home/simonll4/projects/e-ovrt_datasets` @ `6524e21e` (`feature/datasets-v2-setup`).
- **Documentos contrastados:** `CLAUDE.md` raíz §"e-ovrt_datasets"; `docs/13-glosario…` §4.4 y §5; `docs/informe/project-kit/00-contexto-base.md`; `docs/informe/ajustes/02-…` ficha AJ-2.07 (bloque ✎ 2026-08-18); `material-etapa-3/93-redlines-etapa3.md` R-24; `docs/operacion/99`; protocolo §17.1.6 y §17.1.5.4.5 (`scratchpad/17-1-full.md`).

---

## A) Estado del repo

| Ítem | Valor | Comando |
|---|---|---|
| Rama | `feature/datasets-v2-setup`, en sync con `origin/feature/datasets-v2-setup` (`git@github.com:Pandulc/e-ovrt_datasets.git`) | `git status -sb` |
| HEAD | `6524e21e9837c95eea6aacebd81fabefbfcd9860` — 2026-08-20 01:43:11 +0000 — "feat(bench): generador de los estratos chv/shel5k + sincronización de la documentación" | `git log -1` |
| Working tree | **limpio** (0 líneas en `git status --short`) | |
| Últimos 30 commits | 2026-07-11 → 2026-08-20; hitos: `6a1c3222` (07-23, congela bench_v3) · `0863e637` (07-23, SHEL5K estrato) · `376b438c` (07-23, bench_obra + rechazo ppe-dataset) · `ce415464` (07-29, person_gt sobre núcleo curado, 60 violadores) · `56dcbc05` (08-05, registry al día) · `1d2d9a01` (08-17, archivo roles) · `36ce1798` (08-20, destrackea vistas `original`) · `6524e21e` (08-20, `build_bench_strata.py`) | `git log -30 --format='%h %ad %s' --date=short` |
| Tests | **431 passed in 1.56s** (37 archivos en `datasets/tests/`, fixtures sintéticas; los de artefacto real NO se skippean porque los congelados están en disco) | `python3 -m pytest datasets/tests/ -q` |
| `--verify` | **PASS ×2, exit 0, 0,35 s**: `chv` sha256 `6d15ff9b…` y `shel5k` `bf35f63b…` reproducen byte a byte desde `processed/coco/canonical_v2/` | `python3 datasets/scripts/curate/build_bench_strata.py --verify` |
| Freeze bench_v3 | `sha256sum bench_v3.json` = `4557024ecc4ee497ab1fad01d6819206395c10fd794010ed8c1d9198b19a4462` = `bench_v3_sha256` del manifiesto; las 4 fuentes coinciden con `source_sha256` | `sha256sum datasets/processed/coco/bench/curated/*.json` |
| Sin paquete | No hay `pyproject`/`setup`/`Makefile`; `requirements.txt` = `Pillow`, `PyYAML` | `ls`, `cat requirements.txt` |

**Conteos medidos de `bench_v3.json`** (python sobre el JSON): 6.477 imágenes / 55.165 anotaciones / 4 categorías (`person`=0, `helmet`=1, `vest`=2, `bare_head`=3). Campo `stratum` con **4 valores**: `shel5k` 5.000 · `chv` 1.330 · `bench_obra_val` 85 · `bench_obra_test` 62 (147 = bench_obra).

| Estrato | person | helmet | vest | bare_head | total | imgs con `bare_head` | imgs sin anotaciones |
|---|---:|---:|---:|---:|---:|---:|---:|
| bench_obra_test (62) | 135 | 83 | 38 | 26 | 282 | 14 | 16 |
| bench_obra_val (85) | 127 | 76 | 41 | 35 | 279 | 16 | 26 |
| chv (1.330) | 3.887 | 3.538 | 1.784 | 0 | 9.209 | 0 | 0 |
| shel5k (5.000) | 20.023 | 19.252 | 0 | 6.120 | 45.395 | 1.143 | 0 |
| **Total** | **24.172** | **22.949** | **1.863** | **6.181** | **55.165** | **1.173** | 42 |

GT persona-nivel: `person_gt_bench_obra.json` 262 personas / 60 violadores CR-01 / 0 CR-02 (v1); `person_gt_bench_obra_v2.json` 262 / 60 CR-01 / **142 CR-02** (+15 negativos ambiguos; fuente: `NO-Safety Vest` del raw); `person_gt_shel5k.json` 20.015 personas / **5.248** violadores CR-01, sin `has_vest` a propósito. 0 basenames repetidos entre los 6.477 (chequeo ad hoc). Original histórico `processed/coco/bench/construction_site_safety_bench.json`: 196 imgs / 741 anns, intacto.

---

## B) Afirmaciones verificadas

Leyenda: ✅ verificada · ⚠️ parcial/imprecisa · ❌ divergente.

### B.1 `CLAUDE.md` raíz — sección "e-ovrt_datasets" y bloque de acople

| # | Afirmación | Veredicto | Evidencia |
|---|---|---|---|
| 1 | Scripts sueltos, sin paquete, sin `pip install`, sin Makefile | ✅ | `ls` raíz: sin `pyproject`/`Makefile`; `README.md` §Requisitos |
| 2 | "Scripts resolve paths relative to the repo root (`parents[3]`)" | ⚠️ | Solo `convert/convert_datasets.py:18` y `bench/build_audit_kit.py:26` usan `parents[3]`; `curate/build_bench_{obra,strata,v3}.py`, `bench/build_person_gt_shel5k.py`, `bench/build_clip_bench.py` usan `parents[2]` (= `datasets/`). Resuelven igual desde cualquier CWD, pero la raíz que asumen es `datasets/`, no la del repo |
| 3 | Requiere `Pillow` y `PyYAML`; `ffmpeg` para video; sin Kaggle CLI (urllib) | ✅ | `requirements.txt`; `README.md`; `legacy/scripts/download/download_sh17_kaggle.py:7-8` (`urllib.request`) |
| 4 | Descargas: `download_construction_site_safety.sh`, `download_chv.sh`, `download_ppe_siabar.sh`; hardhat descartado; legacy `download_construction_ppe.sh`, `download_sh17_kaggle.py` | ⚠️ | Los 3 existen + **`download_shel5k.sh`** (volvió a activo el 08-19, `download/README.md`) que `CLAUDE.md` no lista. Legacy verificado en `legacy/README.md` |
| 5 | Vistas emitidas: `original`, `canonical_v2`, **`train_v2`, `bench_v2`, `demo_v2`** (bloque "coupled by canonical vocabulary") | ❌ | Las vistas por rol fueron **archivadas el 2026-08-15** (`datasets/splits/DEPRECATED.md`; `legacy/splits/v2/`; `legacy/scripts/curate/build_role_views.py`). El propio `CLAUDE.md` lo dice más abajo ("ARCHIVADO 2026-08-15") → el bloque de arriba quedó viejo |
| 6 | Deprecados `canonical_cr01_cr02`, `finetuning_cr01_cr02` | ✅ | `class_mapping.yaml` §deprecated; `legacy/scripts/split/`, `legacy/scripts/curate/generate_finetuning_cr01_cr02.py`; `convert_datasets.py:503-505` |
| 7 | Los 3 TRAIN: `construction_site_safety`, `chv`, `ppe_siabar` | ⚠️ | Cierto **como rol histórico** (`datasets_metadata.yaml` `role_v2`; `selection_scoring.csv` col. `rol`; `conversion_report.md` TRAIN=5.540). El **entrenamiento efectivo** (`finetuning_v1`) usó solo `construction_site_safety` (2.203 train / 375 val) + `ppe_siabar` (743 / 108); **`chv` excluido** por anti-leakage (100 % de chv está en bench_v3) — `e-ovrt_experimental-setup/finetuning/manifests/finetuning_v1.summary.json` `.splits`; `docs/operacion/100` §V2 |
| 8 | `shel5k` no es TRAIN: fuente canonical_v2 y estrato de bench_v3 (5.000) | ✅ | `datasets_metadata.yaml` shel5k `role_v2: [BENCH]`, `status: bench_v3_stratum`; `conversion_report.md` (3500/750/750) |
| 9 | Comando `convert_datasets.py --datasets construction_site_safety chv ppe_siabar shel5k --views canonical_v2` | ✅ | `configs()` tiene los 4 + `construction_safety_hardhat`, `construction_ppe`, `sh17` (legacy); `conversion_report.md` |
| 10 | `build_person_gt.py` (comando pelado) | ⚠️ | Exige `--coco` (nargs+) y `--out` (`build_person_gt.py:156-158`); el comando completo está en `bench_v3.md` |
| 11 | bench_v3: 6.477 = 147 + 1.330 + 5.000, 3 fuentes, `stratum` por imagen | ✅/⚠️ | Conteos exactos (tabla A). El campo `stratum` tiene **4** valores (`bench_obra_test`/`_val` separados); "3 estratos" requiere fusionar los dos de obra (glosario §4.4 lo aclara; el manifiesto dice `strata: 4`) |
| 12 | Manifiesto con sha256 por fuente para verificar el freeze | ✅ | `bench_v3_manifest.json` (`source_sha256` ×4 + `bench_v3_sha256`); `test_bench_v3_freeze.py` pinnea conteos y hashes |
| 13 | `bench_obra` 147 curado, spot-check visual; `chv` 1.330 mejor vest AP; `shel5k` 5.000 CC BY 4.0, `bare_head` nativo vía `head`, `person_gt_shel5k.json` | ✅ | `bench_v3.md` §Composición (spot-check **muestral 36/147**); `convert_datasets.py:229-252` (`head`→`bare_head` con `bare_head_explicit_sources`); `license_registry.md` fila SHEL5K |
| 14 | Cadena de regeneración: raw → convert → `build_bench_obra.py` / `build_bench_strata.py` → `build_bench_v3.py`; `--verify` byte a byte | ✅ | `--verify` PASS hoy; `bench_v3.md` §Cadena completa; `build_bench_v3.py:43-47` `STRATUM_SOURCES` |
| 15 | Trampa de serialización (estratos `json.dumps` pelado; bench_v3 `sort_keys=True`) | ✅ | Estratos: 0 newlines, sin newline final, empiezan `{"images": …`; `bench_v3.json` empieza `{"annotations": …` (claves ordenadas); `build_bench_strata.py:97`, `build_bench_v3.py:62` |
| 16 | Política de versionado: raw gitignorado; se commitea registry, scripts, processed necesarios | ✅ | `.gitignore:37-75` + excepción `processed/coco/bench/`; commit `36ce1798` destrackeó ~6.352 archivos de vistas `original` |
| 17 | BENCH-196 histórico ~20–25 % fuera de dominio, intacto; curado en `curated/` | ✅ | `curation_bench_obra.md`: 49/196 excluidas = **25,0 %** (doc 63 estimaba 20–25 %); original 196/741 intacto en disco |
| 18 | "Report metrics both per-stratum and aggregated" | ✅ | `bench_v3.md` §Uso |
| 19 | Campeón/especialista: "recall CR-01 0.599 vs 0.308 del campeón, **n=5.313**" | ❌ | Con el GT vigente el denominador es **60 + 5.248 = 5.308**. 5.313 = 65 + 5.248: se calculó el 07-23 con `person_gt` previo al fix `ce415464` (07-29) que removió 4 `bare_head` sub-píxel (65→60; `bench_v3.md` nota final; doc 66 l.206 "n=65"). Misma cifra en `00-contexto-base.md` l.1347/1727/3037/3075, `results/bench_imagenes/index.md` l.80/118, docs 64/66 |
| 20 | Registry: `datasets_metadata.yaml`, `license_registry.md`, `download_log.md`, `class_mapping.yaml`, `conversion_report.md` | ✅ | 13 archivos en `datasets/registry/` (además `bench_v3.md`, `curation_bench_obra.md`, `evaluation_ppe_dataset.md`, `selection_scoring.csv`, `annotation_contract_v2.yaml`, `bench_gt_audit.md`, `clip_bench.md`, `plantilla-consentimiento…`) |

### B.2 Glosario `13` §4.4 y §5

| Afirmación | Veredicto | Evidencia |
|---|---|---|
| Tabla fuente→estrato: css CC BY 4.0→`bench_obra` 147; chv sin licencia formal→`chv` 1.330; shel5k CC BY 4.0→`shel5k` 5.000 | ✅ | `license_registry.md`; manifiesto |
| `bench_obra` = valid 114 + test 82 = 196 → −49 imgs (12 prefijos) − 4 cajas `bare_head` < 9 px² → 147 (85 val + 62 test) | ✅ | `datasets_metadata.yaml` css `splits: {val: 114, test: 82}`; `build_bench_obra.py:31-47` (`EXCLUDED_PREFIXES` ×12, `MIN_BBOX_AREA_PX = 9.0`); `bench_obra_manifest.json` (`excluded_images` 49, `excluded_annotations_min_area` 4) |
| "bench_obra_val y bench_obra_test cuentan como un solo estrato" | ✅ (convención) | El manifiesto los lista separados (`strata` ×4); la fusión es regla de lectura, no del artefacto |
| §5 TRAIN/BENCH/DEMO 5540/196/1064 | ✅ histórico | `conversion_report.md` §Manifests de rol (ARCHIVADO); el glosario no dice que los roles fueron archivados el 08-15 (dice solo que el BENCH-196 no se cita) |
| §5 "agregado dominado por shel5k (77 %)" | ✅ | 5.000/6.477 = 77,2 % |
| §5 canonical_v2 = 4 clases + atributos `has_helmet`/`has_vest` solo en BENCH | ✅ | `class_mapping.yaml` §bench_attributes; `person_gt_*` |

### B.3 `00-contexto-base.md` (grep)

| Línea(s) | Afirmación | Veredicto |
|---|---|---|
| 360, 828-855 | Trampa fuente≠estrato; frase apta | ✅ coherente con glosario y con el repo |
| 1337-1341, 2979-2988 | 6.477 imgs / 55.165 anns / 3 estratos; 196 histórico 20–25 % OOD | ✅ |
| 2740 | L7 = licencia parcial de `chv`, **20,5 %** del bench | ✅ 1.330/6.477 = 20,53 % |
| 29, 489, 2142, 2175 | 2.946 imágenes de train (fine-tuning) | ✅ `finetuning_v1.summary.json` `.splits.train.images = 2946` (+ 483 val); `configs/t1_yoloe26s_lp.yaml:18-19` |
| 1347, 1727, 3037, 3075 | recall CR-01 n=5.313 | ❌ ver B.1 #19 (5.308 con GT vigente) |
| 1591, 1626-1628 | SHEL5K/CHV/SH17 techos supervisados (0,883 / 0,866 / ≈0,71) | no verificable acá (literatura) |
| 1842, 2908-2916 | Licencias de pesos en `license_registry.md` §PESOS DE MODELO | ✅ sección existe (GDINO/MM-GDINO Apache-2.0, YOLOE AGPL-3.0) |

### B.4 AJ-2.07 (✎ 2026-08-18) y R-24

| Afirmación | Veredicto | Evidencia |
|---|---|---|
| Separar candidatos evaluados (SH17, Pictor-PPE, GDUT-HWD, SHWD, SODA, MOCS…) de utilizados | ✅ el registry lo permite | `datasets_metadata.yaml` con status `legacy_archived` / `pending_download` / `pending_license_review` / `rejected_s0` y notas "POR QUÉ NUNCA SE DESCARGÓ" (✎ 08-15) |
| (b) Utilizados para **entrenamiento**: `construction_site_safety`, `chv`, `ppe_siabar` | ❌ | Rol TRAIN histórico sí; el fine-tuning real (única adaptación ejecutada, T1/T2) entrenó con `construction_site_safety` + `ppe_siabar` **sin `chv`** (`finetuning_v1.summary.json` `.splits.train.datasets`; doc 100 §V2 "Enmienda: el entrenamiento excluye `chv` y `shel5k`"; `DEPRECATED.md` "CHV no puede entrar al fine-tuning (gate invariante 2)") |
| (c) Fuentes del banco: css, chv, shel5k; `ppe_siabar` no aporta al banco; `shel5k` no entrena | ✅ | manifiesto; `finetuning_v1.summary.json` `.sources` (solo css y ppe_siabar) |
| `bench_obra` no es dataset; cadena 196→147; `bare_head` 110→61 | ✅ | `curation_bench_obra.md` tabla (person 340→262, helmet 189→159, vest 102→79, bare_head 110→61) |
| R-24: inventario del informe anterior a la selección efectiva | ✅ | Tabla 26 no contiene `construction_site_safety` ni `ppe_siabar` (ver D) |

### B.5 `docs/operacion/99` (2026-08-05)

| Afirmación | Veredicto | Evidencia |
|---|---|---|
| Inventario físico: shel5k 5.000 / ppe-dataset 5.381 (rechazado) / chv 1.330 / css 2.799 / MOCS 1.471 / ppe_siabar 1.607 | ✅ registry | `datasets_metadata.yaml` `image_count`; `download_log.md`. (No conté imágenes en `raw/` — ver F) |
| "chv: TRAIN + estrato BENCH" | ⚠️ | Rol histórico; en el entrenamiento efectivo chv NO participa (B.4). El doc es del 08-05, anterior a `finetuning_v1` (08-13); la frase sobrevive sin matiz en el registry (`role_v2: [TRAIN, DEMO, BENCH]`) |
| sh17/construction_ppe `raw_absent_views_stale`; vistas muertas borradas | ✅ (superado) | Hoy `status: legacy_archived` (✎ 08-15); reportes en `legacy/processed_reports/` |
| Candidatos nunca descargados: gdut_hwd, shwd, soda, pictor_ppe | ✅ | `datasets_metadata.yaml` (`downloaded_at: null`) |
| `construction_ppe_skcet` descartado (55 % defectos) | ⚠️ | Está en `selection_scoring.csv`, `class_mapping.yaml`, `annotation_contract_v2.yaml`, pero **no tiene entrada en `datasets_metadata.yaml`** |
| MOCS = copia Roboflow, no el original | ✅ | `datasets_metadata.yaml` id `mocs` (✎ 08-05); `license_registry.md` |

### B.6 Licencias registradas (`license_registry.md`, `datasets_metadata.yaml`)

| Dataset | Licencia registrada | Estado | Uso real |
|---|---|---|---|
| construction_site_safety (Roboflow v27) | CC BY 4.0 | Aprobado | TRAIN efectivo + fuente de `bench_obra` |
| ppe_siabar (Roboflow v1) | CC BY 4.0 | Aprobado | TRAIN efectivo; no bench |
| chv (GitHub ZijianWang) | **sin SPDX**; grant "open for free use" + cita `wang2021ppe`; verificación 2026-07-29 (GitHub API `license: None`) | Aprobado uso académico, SIN redistribución → **L7** | Estrato `chv` (100 %); rol TRAIN histórico; excluido del FT |
| shel5k (Mendeley 9rcv8mm682 v4) | CC BY 4.0 | Aprobado | Estrato `shel5k` (100 %); no TRAIN |
| MOCS (copia `mocs-bowib`) | CC BY 4.0 declarada por uploader; original anlab340 sin verificar | Aprobado evaluativo, sin redistribución | Piloto A1 (doc 94); descartado para BENCH |
| ppe_dataset_rbyz | MIT | **Rechazado S0** (4 descalificadores + 10 % solapamiento con ppe_siabar) | ninguno; raw borrado 08-05 |
| SH17 | CC BY-NC-SA 4.0 | legacy_archived | ninguno en v2 |
| Construction-PPE (Ultralytics) | AGPL-3.0 | legacy_archived | ninguno en v2 |
| construction_safety_hardhat (Kaggle) | CC0 | No disponible (URL inválida 06-18) | ninguno |
| GDUT-HWD / SHWD / SODA | "Verificar" | Pendiente (inventario, no pendiente de trabajo) | ninguno |
| Pictor-PPE | "Verificar" | Bloqueado | ninguno |
| coco_val2017 | anns CC BY 4.0; imgs Flickr | Aprobado solo local | arnés de retención OV (T2) |

---

## C) Divergencias doc↔repo por gravedad

### 🔴 ALTA

**C1. "Utilizados para entrenamiento: css, chv, ppe_siabar" (AJ-2.07 ✎08-18 (b); R-24 (b); glosario §5; doc 99 §2; `datasets_metadata.yaml` chv `role_v2`).**
- *Qué hay:* la única adaptación ejecutada (`finetuning_v1`, T1 job 1167640 y T2 job 1167982) entrenó con `construction_site_safety` (2.203) + `ppe_siabar` (743) = **2.946**; `chv` fue excluido explícitamente porque el 100 % de sus 1.330 imágenes es estrato de `bench_v3` (`docs/operacion/100` §V2; `finetuning_v1.summary.json` `.sources` sin chv; `DEPRECATED.md` "gate invariante 2").
- *Riesgo:* si el informe copia (b) tal cual, declara haber entrenado con una fuente del banco → viola su propia Tabla 28 "Disyunción estricta" y contradice el manifiesto.
- *Corregir:* R-24 (b) y la nota de AJ-2.07 → "rol TRAIN histórico (train_v2): css, chv, ppe_siabar — **archivado**; entrenamiento efectivo (`finetuning_v1`): css + ppe_siabar, chv excluido por anti-leakage"; glosario §5 fila TRAIN/BENCH/DEMO; `datasets_metadata.yaml` chv (anotar que TRAIN es histórico y que el FT lo excluye); doc 99 §2 fila chv.

**C2. Tabla 28 "Rango de entrenamiento 500–2.000 imágenes" vs 2.946 train.**
- *Qué hay:* 2.946 (+47 % sobre el techo). Ni ADR-017, ni doc 100, ni `finetuning/README.md`/`configs/README.md` mencionan el rango 500–2.000 ni justifican la desviación (grep `2\.000|500–2|rango` sin hits). La nota de la Tabla 28 exige "justificarse explícitamente en la bitácora".
- *Corregir:* §17.4/§17.5 (o D-FT-11) debe declarar la desviación y su causa (se tomó el 100 % de linajes elegibles tras dedup y exclusión de bench; F-127.1 "estructural: 2.946 imgs vs 10,35M params" es justamente el argumento de que incluso ese volumen es insuficiente).

### 🟠 MEDIA

**C3. `n=5.313` (CLAUDE.md l.84; `00-contexto-base.md` ×4; `results/bench_imagenes/index.md` ×2; docs 64/66).** Con el GT vigente (`person_gt_bench_obra.json` 60 + `person_gt_shel5k.json` 5.248) el denominador es **5.308**. 5.313 corresponde al GT del 23-jul (65 violadores en bench_obra, antes del fix `ce415464` del 29-jul). *Corregir:* citar "n=5.313 (GT del 23-jul; 5.308 con el GT vigente)" o recalcular; tocar `CLAUDE.md`, `00-contexto-base.md`, `results/bench_imagenes/index.md`.

**C4. Auditoría humana del GT (Task 4.3) — estado contradictorio.** `bench_gt_audit.md` §4 (checklist 24 imgs) y §5/§6 están **vacíos** ("Completar tras la revisión manual"); `estado_avance.md` l.23 dice "4.3 auditoría manual pendiente" y l.110 "Task 4.3 (✎ ya ejecutada)"; `documentation/README.md` dice "Task 4.3 ya ejecutada — kit en…"; docs 75 §6 y 78 A2 la listan como **sin ejecutar**. Lo ejecutado es el **kit** (`build_audit_kit.py`, 24 PNG), no la auditoría. *Corregir:* `estado_avance.md` l.110 y `documentation/README.md` → "kit generado; checklist pendiente"; el informe no puede declarar "precisión del GT ≥ 95 %" ni doble anotación (ver D.3).

**C5. `CLAUDE.md` raíz desincronizado en dos puntos:** (i) bloque "the datasets repo emits multiple views… `train_v2`, `bench_v2`, `demo_v2`" — archivadas el 08-15 (contradice su propio bloque "ARCHIVADO 2026-08-15"); (ii) no lista `download_shel5k.sh` (activo desde 08-19). *Corregir:* `CLAUDE.md` raíz.

**C6. Tabla 26 del informe vs registry, en licencias y alcance:** GDUT-HWD "Apache-2.0 visible" y SHWD "MIT" — el registry dice **"Verificar / Pendiente"** para ambos (nunca se descargaron); CHV "paper CC BY 4.0" — el dataset **no tiene licencia** (L7; la CC BY es del paper, no de los datos); MOCS "41.668 imgs, CC BY-NC 4.0, acceso por solicitud" — lo que existe es la **copia Roboflow** de 1.471 imgs (solo `Worker`, CC BY 4.0 del uploader). *Corregir:* al transcribir la Tabla 26 a §17.4/§17.5, declarar que las licencias de GDUT/SHWD no se verificaron (no se descargaron) y que MOCS-usado ≠ MOCS-original.

**C7. Tabla 26 omite los dos datasets efectivamente usados para entrenar y para `bench_obra`:** `construction_site_safety` y `ppe_siabar` provienen de una investigación posterior al protocolo (`documentation/investigacion-roboflow-universe.md`, 2026-06-17; `selection_scoring.csv`). R-24 lo señala en general; el informe debe decir explícitamente que la selección efectiva agregó candidatos fuera del inventario de §17.1.6.2.

### 🟡 BAJA

- **C8.** "3 estratos" vs `manifest.strata` = 4 (`bench_obra_test`, `bench_obra_val`, `chv`, `shel5k`). Cualquier agrupación por `stratum` da 4 filas; el informe debe explicitar la fusión (glosario §4.4 ya lo hace).
- **C9.** `bench_v3.md`: "resolución uniforme 416×416" en shel5k — medido: 416×415 (2.461), 416×416 (2.192), 415×416 (324), 415×415 (23). Aproximación válida, no literal.
- **C10.** `bench_v3.md` dice `test_bench_strata.py` "13 tests"; el archivo tiene 11 `def test_` (puede haber parametrize; no afecta).
- **C11.** `CLAUDE.md`: `parents[3]` no es la regla general (B.1 #2); `build_person_gt.py` requiere `--coco/--out` (B.1 #10).
- **C12.** `construction_ppe_skcet` (descartado, 55 % defectos) figura en `selection_scoring.csv`, `class_mapping.yaml` y `annotation_contract_v2.yaml` pero **no en `datasets_metadata.yaml`** (fuente de verdad declarada).
- **C13.** `ppe_siabar` con dos `source_url` distintas: registry `siabar/ppe-dataset-for-workplace-safety` vs `finetuning_v1.summary.json` `siabar/ppe-plsuk`.
- **C14.** `bench_v3.md` §Uso cita solo `person_gt_bench_obra.json` (CR-01, `has_vest=True` para todos) y no menciona `person_gt_bench_obra_v2.json` (CR-02 desde negativos explícitos, 142 violadores) que sostiene los resultados CR-02 de Nivel A.
- **C15.** Glosario §5 mantiene la fila TRAIN/BENCH/DEMO 5540/196/1064 sin la nota de archivo del 08-15 (solo dice que el 196 no se cita).

---

## D) Protocolo §17.1.6 vs construido

### D.1 Por dataset (Tabla 26/27/29 + los que el protocolo no nombra)

| Dataset nombrado en §17.1 | Prescripción del informe (Tabla 26/29) | Destino real | Estado | Evidencia |
|---|---|---|---|---|
| **SH17** | FT Alta / eval Alta; CC BY-NC-SA | Descargado 06-05 (14 GB), convertido v1; **nunca v2**; licencia NC-SA inelegible (rúbrica §7); raw borrado; `legacy_archived` | **DESCARTADO** (licencia + reinicio v2) | `datasets_metadata.yaml` sh17; `download_log.md`; `legacy/processed_reports/sh17_…json` |
| **SHEL5K** | FT Media-Alta / eval Alta; CC BY 4.0 | **Fuente del banco**: estrato `shel5k` = 100 % (5.000; splits `custom_seeded` seed 42 concatenados train,val,test); `bare_head` nativo (`head`); `person_gt_shel5k.json`; **no entrena** | **UTILIZADO (eval)** | manifiesto; `convert_datasets.py:209-254`; `build_bench_strata.py` |
| **CHV** | FT Media-Alta / eval Alta; "uso libre, verificar redistribución" | **Fuente del banco**: estrato `chv` = 100 % (1.330, splits oficiales `data split/*.txt`); rol TRAIN histórico (`train_v2`, archivado); **excluido del FT efectivo** (anti-leakage); DEMO = catálogo media-plane apunta al raw; licencia sin SPDX → L7 | **UTILIZADO (eval); NO entrenado** | `finetuning_v1.summary.json`; doc 100 §V2; `license_registry.md` |
| **Pictor-PPE** | Media/Condicionada | Nunca descargado; `pending_license_review`, Bloqueado | **DESCARTADO** (licencia no verificable) | `datasets_metadata.yaml` pictor_ppe |
| **Construction-PPE (Ultralytics)** | FT Media-Alta / eval Alta; AGPL-3.0 | Descargado 06-05, convertido v1; nunca v2; AGPL inelegible; raw ausente; `legacy_archived` | **DESCARTADO** (licencia + v2) | `datasets_metadata.yaml` construction_ppe |
| **GDUT-HWD** | FT Media-Alta / eval Alta; "Apache-2.0 visible" | Nunca descargado; licencia "verificar"; CR-01 ya cubierta; alcance cerrado (ADR-015/016) | **DESCARTADO** (inventario) | `datasets_metadata.yaml` gdut_hwd (✎ 08-15) |
| **SHWD** | FT Media-Alta / eval Alta; MIT | Ídem GDUT-HWD | **DESCARTADO** (inventario) | `datasets_metadata.yaml` shwd |
| **SODA** | Media / Media-Alta; CR-05/06 | Nunca descargado; cubre CR-05/06 **excluidas** (E-02, `nucleo/10`) | **DESCARTADO** (fuera de alcance) | `datasets_metadata.yaml` soda |
| **MOCS** | Baja/Condicionada; 41.668 imgs; CC BY-NC + solicitud | Original **nunca** solicitado; lo que hay es la copia Roboflow `mocs-bowib` (1.471 imgs, solo `Worker`, CC BY 4.0 uploader). Descartado para BENCH (scoring); usado en **piloto A1** (doc 94): cualitativo + ancla person↔Worker AP 0,610 n=507 | **USO LATERAL** (piloto A1), no bench ni train | `datasets_metadata.yaml` mocs; `selection_scoring.csv`; `license_registry.md` |
| **MOT17 / OVT-B** (Tabla 30) | Verificar tracker / integración OVD+MOT | Ninguna mención en el repo; exclusión **E-10** (`nucleo/10` §E-10; ADR-015): métricas MOT "no aplicables" con fundamento medido | **NO EJERCIDA** (exclusión registrada) | `grep -ri "MOT17\|OVT-B" e-ovrt_datasets` → 0 hits |
| — *no en Tabla 26* — **construction_site_safety** (Roboflow v27) | — | 2.799 imgs CC BY 4.0; **TRAIN efectivo** (2.203/375) + fuente de `bench_obra` (val+test 196 → 147); negativos explícitos NO-Hardhat/NO-Safety Vest → GT CR-01/CR-02 | **UTILIZADO (train + eval)** | `datasets_metadata.yaml`; `build_bench_obra.py` |
| — *no en Tabla 26* — **ppe_siabar** (Roboflow v1) | — | 1.607 imgs CC BY 4.0; **TRAIN efectivo** (743/108); no bench | **UTILIZADO (train)** | `finetuning_v1.summary.json` |
| — *no en Tabla 26* — construction_safety_hardhat (Kaggle) | — | URL inválida 06-18, nunca descargado | DESCARTADO | `download_log.md` |
| — *no en Tabla 26* — construction_ppe_skcet (Roboflow) | — | 55 % defectos | DESCARTADO | `selection_scoring.csv` |
| — *no en Tabla 26* — ppe_dataset_rbyz (Roboflow) | — | Rechazado S0 07-23 (sin GT person, dominio e-commerce, anotación pobre, integridad rota; 10 % solapa ppe_siabar) | RECHAZADO | `evaluation_ppe_dataset.md` |
| — *no en Tabla 26* — coco_val2017 | — | Arnés de retención OV para T2 (5.000 imgs, 80 clases); local, no redistribuido | UTILIZADO (eval OV, rama FT) | `download_log.md`; `t2_coco_retention_base_frozen.json` |

**Lectura:** de los 9 datasets de la Tabla 26, **2 se usaron** (SHEL5K y CHV, ambos solo como fuentes del banco), **1 tuvo uso lateral** (MOCS, en copia distinta a la descrita), **6 se descartaron**. Los **dos datasets de entrenamiento y la fuente del núcleo del banco no figuran en el protocolo**. Los benchmarks de Categoría 2 no se ejercieron (E-10).

### D.2 Por condición de partición (Tabla 28)

| Condición (Tabla 28) | Estado | Evidencia (dónde se cumple) |
|---|---|---|
| **Disyunción estricta** train ∩ test = ∅ | **CUMPLIDA** (en `finetuning_v1`) | `finetuning_v1.summary.json` `.gates.bench_overlap_selected = 0`, `.exclusions.bench_source_lineage = 25`, `.bench_perceptual_component = 56`; chv y shel5k excluidos enteros; doc 100 §V2 "intersección 0 en basename y stem contra las 6.477". ⚠️ El rol TRAIN histórico (`train_v2`, 5.540) **sí** solapaba 100 % con el estrato `chv` → por eso se archivó (`DEPRECATED.md`); `leakage_check.py` solo controlaba TRAIN vs BENCH-196 |
| **Test set compartido** | **CUMPLIDA** | Baseline `run_20260815_193750`, T1 tuned `run_20260817_015315`, T2 tuned `run_20260821_150015`: 6.477/6.477 sobre `bench_v3`; `bench_v3_sha256` pinneado en `finetuning_v1.summary.json` y `t1_yoloe26s_bench_v3_protocol.json` |
| **Semilla reproducible** | **CUMPLIDA** | `convert_datasets.py:345` `custom_splits(seed=42)` (shel5k); `finetuning_v1` `seed: 42`; entrenamiento `seed 100, deterministic` (`t2_yoloe26s_protocol.json`); `build_bench_strata.py` sin muestreo (100 %) |
| **Splits oficiales** | **CUMPLIDA** | chv: `data split/{train,valid,test}.txt` oficiales (`convert_datasets.py:76-80`); css/ppe_siabar: subdirs Roboflow; shel5k: sin split oficial → `custom_seeded` documentado (`download_log.md`) |
| **Rango de entrenamiento 500–2.000** | **DESVIADA** | 2.946 train (+47 %); sin justificación explícita contra el rango en ADR-017 / doc 100 / `finetuning/README.md` (ver C2) |
| **No solapamiento cruzado** entre colecciones | **CUMPLIDA** (train) / **PARCIAL** (bench) | Train: dedup perceptual `ahash64`/`dhash64` por linaje (`finetuning_v1.split.csv`), 700 linajes ppe deduplicados; ppe_dataset_rbyz rechazado por 10 % solapamiento con ppe_siabar. Bench: `build_bench_strata.py:138` asserta basenames únicos **intra**-estrato; `build_bench_v3.py` no chequea duplicados **entre** estratos (verificado ad hoc hoy: 0 basenames repetidos entre los 6.477; sin chequeo perceptual entre css/chv/shel5k) |
| **Congelamiento previo** | **CUMPLIDA** | bench_v3 congelado 2026-07-23 (`6a1c3222`, sha en manifiesto) → T1 entrena 2026-08-15/17, T2 2026-08-21; `test_bench_v3_freeze.py` pinnea conteos y hashes; `--verify` reproduce estratos |

### D.3 §17.1.5.4.5 (anotación complementaria, acuerdo, piso de positivos)

| Prescripción | Estado | Evidencia |
|---|---|---|
| Doble anotación independiente ≥ 20 % + kappa de Cohen + IoU/umbral para cajas | **NO EJERCIDA** (imágenes) | El GT del banco reutiliza anotaciones de las fuentes (D9/D10: negativos explícitos, no se anotó de nuevo); auditoría humana Task 4.3 diseñada sobre 24/147 imgs (16 %) con **checklist vacío** (`bench_gt_audit.md` §4–6); `clip_bench.md` §L2 declara "Sin doble anotación: no hay kappa (DECISIÓN)"; `grep -ri kappa datasets/registry` → solo esa limitación |
| ≥ 200 instancias positivas por condición (o documentar n + IC) | **CUMPLIDA CR-01 / NO CR-02** | CR-01: 5.308 violadores (5.248 shel5k + 60 bench_obra); CR-02: **142** violadores, solo en `bench_obra` (`person_gt_bench_obra_v2.json`, +15 ambiguos); bench_obra CR-01 = 60 < 150 (spec §6.5) < 200 (informe) — documentado en `bench_gt_audit.md` §7 |
| Subconjunto representativo (iluminación, ángulo, oclusión, escala) | PARCIAL | Salvedades por estrato declaradas (`bench_v3.md`: shel5k 416×416 uniforme, mirror-padding; chv dominio mixto/stock) — no hay estratificación por esas variables |

---

## E) Hechos citables con comando (desde `/home/simonll4/projects/e-ovrt_datasets`)

```bash
git rev-parse HEAD                      # 6524e21e9837c95eea6aacebd81fabefbfcd9860
git status --short | wc -l              # 0
python3 -m pytest datasets/tests/ -q | tail -1     # 431 passed in 1.56s
python3 datasets/scripts/curate/build_bench_strata.py --verify   # [PASS] chv 6d15ff9b… · [PASS] shel5k bf35f63b…
sha256sum datasets/processed/coco/bench/curated/bench_v3.json    # 4557024ecc4ee497ab1fad01d6819206395c10fd794010ed8c1d9198b19a4462
python3 - <<'EOF'
import json,collections
d=json.load(open('datasets/processed/coco/bench/curated/bench_v3.json'))
print(len(d['images']),len(d['annotations']))                      # 6477 55165
print(collections.Counter(i['stratum'] for i in d['images']))      # shel5k 5000, chv 1330, bench_obra_val 85, bench_obra_test 62
c={x['id']:x['name'] for x in d['categories']}
print(collections.Counter(c[a['category_id']] for a in d['annotations']))  # person 24172, helmet 22949, bare_head 6181, vest 1863
EOF
python3 -c "import json;d=json.load(open('datasets/processed/coco/bench/curated/person_gt_shel5k.json'));print(d['total_persons'],d['violators_cr01'])"      # 20015 5248
python3 -c "import json;d=json.load(open('datasets/processed/coco/bench/curated/person_gt_bench_obra_v2.json'));print(d['total_persons'],d['violators_cr01'],d['violators_cr02'])"  # 262 60 142
python3 -c "import json;print(len(json.load(open('datasets/processed/coco/bench/construction_site_safety_bench.json'))['images']))"   # 196 (histórico, intacto)
python3 -c "import json;m=json.load(open('datasets/processed/coco/bench/curated/bench_obra_manifest.json'));print(len(m['excluded_images']),m['excluded_annotations_min_area'],m['class_counts'])"  # 49 4 {original…, obra…}
python3 -c "import json;d=json.load(open('../e-ovrt_experimental-setup/finetuning/manifests/finetuning_v1.summary.json'));print(d['splits']['train']['images'],d['splits']['train']['datasets'],d['gates'])"  # 2946 {'construction_site_safety': 2203, 'ppe_siabar': 743} bench_overlap_selected 0
grep -n "role_v2" -A2 datasets/registry/datasets_metadata.yaml | grep -B2 "BENCH\|TRAIN"    # roles históricos por dataset
grep -c "^def test_" datasets/tests/test_bench_strata.py           # 11
```

Otros hechos: 49/196 = 25,0 % excluido del BENCH histórico · chv = 20,53 % del bench (L7) · shel5k = 77,2 % · `person_gt_shel5k` 20.015 personas = 20.023 cajas `person` − 8 labels `person` sueltos descartados · 42 imágenes de bench_obra sin anotaciones (16 test + 26 val) · 1.173 imágenes con GT `bare_head` (1.143 shel5k + 30 bench_obra) · 0 basenames repetidos entre estratos · estratos serializados sin newline final (`bench_stratum_chv.json` 1.565.965 B; `_shel5k` 6.937.054 B; `bench_v3.json` 8.760.679 B).

---

## F) No pude verificar

1. **Licencias contra las fuentes externas** (Roboflow, Mendeley, GitHub CHV, Kaggle): sin red; me apoyé en `license_registry.md` (verificación CHV del 2026-07-29 documentada con la respuesta de la GitHub API).
2. **Conteos de imágenes en `datasets/raw/`** (2.799 / 1.607 / 1.330 / 5.000 / 1.471): no los recontabilicé en disco; `--verify` PASS implica que `processed/coco/canonical_v2/{chv,shel5k}` están y coinciden.
3. **Origen exacto de n=5.313**: inferido como 65 + 5.248 (doc 66 l.206 cita n=65 para bench_obra); no re-ejecuté la evaluación de doc 64/66.
4. **Cifras de literatura** de `00-contexto-base.md` (techos supervisados SHEL5K 0,883 / CHV 0,866 / SH17 ≈0,71) y de la Tabla 26 del informe (volúmenes de GDUT-HWD, SHWD, SODA, MOCS original, Pictor).
5. **Si la auditoría Task 4.3 se hizo fuera de registro**: en el repo y en docs 75/78 consta como no ejecutada; `estado_avance.md` l.110 y `documentation/README.md` la dan por ejecutada sin evidencia.
6. **Solapamiento perceptual entre fuentes del bench** (css ↔ chv ↔ shel5k): solo verifiqué basenames (0 repetidos); no corrí hashing perceptual.
7. **Si `chv` fue usado en alguna adaptación previa al reinicio v2** (legacy `finetuning_cr01_cr02`): fuera del alcance de resultados reportables.
