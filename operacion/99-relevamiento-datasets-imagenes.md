# 99 — Relevamiento y organización de los datasets de imágenes

- **Fecha:** 2026-08-05.
- **Qué es:** el relevamiento completo del repo `e-ovrt_datasets` en su parte de
  imágenes — qué hay físicamente, qué alimentó resultados reportables, qué va al
  informe y qué no — más la puesta al día del registry, que había quedado
  desactualizado en puntos que importan (MOCS, shel5k, chv, ppe-dataset).
- **Método:** inventario contra disco (`du`, conteos), registry contra realidad,
  y uso contra los resultados reportables (docs 64/66/83/94, `results/`).

---

## 1. Inventario físico (datasets/raw/, 6,5 GB de imágenes)

| Dataset | Tamaño | Imgs | Licencia | Estado real |
|---|---|---|---|---|
| `shel5k` | 2,5 GB | 5.000 | CC BY 4.0 | **Estrato BENCH de bench_v3** — bare_head nativo, person_gt (5.248 violadores) |
| `ppe-dataset` | 1,2 GB | 5.381 | MIT | **RECHAZADO** (protocolo S0, 4 descalificadores) — **borrable** |
| `chv` | 855 MB | 1.330 | grant informal + cita | **TRAIN + estrato BENCH** — mejor vest AP del proyecto |
| `construction_site_safety` | 314 MB | 2.799 | CC BY 4.0 | **TRAIN + núcleo de bench_obra** + GT de A1 + negativos CR-02 |
| `MOCS` | 228 MB | 1.471 | CC BY 4.0 (uploader) | **Piloto A1** (doc 94) — copia Roboflow, NO el original |
| `ppe_siabar` | 205 MB | 1.607 | CC BY 4.0 | **TRAIN** |
| ~~`construction_safety_hardhat`~~ | — | 0 | CC0 | Dir vacío **eliminado** hoy (URL inválida desde 06-18, registrado) |

(`raw/clip_bench` — 1,1 GB — es el material de VIDEO del banco de clips, fuera de
este relevamiento.)

**Registrados pero SIN raw en disco:** `sh17` (CC BY-NC-SA) y `construction_ppe`
(AGPL-3.0) — sus vistas `processed/original/` apuntan a rutas de otra máquina
(`/home/pandulc/...`): **doblemente muertas**. Nunca entraron al pipeline v2 ni a
ningún resultado. **Registrados y nunca descargados:** `gdut_hwd`, `shwd`, `soda`,
`pictor_ppe` (candidatos evaluados en papel, doc 66).

## 2. Clasificación — qué documenta el informe

### Nivel A — material del informe (los 5 con resultados reportables)

| Dataset | Qué resultado sostiene | Declaración de licencia para el informe |
|---|---|---|
| `construction_site_safety` | TRAIN + origen de `bench_obra` (147 curadas) + **GT de `machinery`/`vehicle` del piloto A1** + negativos explícitos del GT CR-02 Nivel A | CC BY 4.0, atribución a Roboflow Universe Projects |
| `chv` | 2º estrato de bench_v3 (1.330) + TRAIN + mejor vest AP (0,55–0,58) | Grant informal "open for free use"; **cita obligatoria `wang2021ppe`**; imágenes NO redistribuibles (cumplido por construcción: raw gitignorado) |
| `shel5k` | 3er estrato de bench_v3 (5.000) — único con `bare_head` nativo; el n grande que separó al especialista (doc 64 §B5) | CC BY 4.0, Mendeley DOI 10.17632/9rcv8mm682.4 |
| `ppe_siabar` | TRAIN (1.120 imgs de train) | CC BY 4.0 |
| `MOCS` (copia Roboflow) | Piloto A1: amplitud de vocabulario (cualitativa) + ancla person↔Worker (AP 0,610, n=507) | CC BY 4.0 **declarada por el uploader de la copia**; original (anlab340) sin verificar → uso evaluativo, sin redistribución, **citar el paper original de MOCS** |

> **Precisión que el informe debe conservar:** el número duro del piloto A1
> (`machinery` AP 0,662) **no sale de MOCS** — sale del GT de
> `construction_site_safety` (clases `machinery`/`vehicle` que canonical_v2 nunca
> usó). MOCS aporta la evidencia cualitativa y el ancla cross-dataset.

### Nivel B — se documenta como METODOLOGÍA, no como material

El proceso de selección es en sí un resultado del trabajo (el protocolo funcionando):

- **`ppe-dataset` rechazado** (registry `evaluation_ppe_dataset.md`): 4
  descalificadores, cada uno suficiente — sin GT de `person`, dominio e-commerce,
  anotación pobre, integridad rota — más 10% de solapamiento con material de TRAIN.
- **El scoring de candidatos** (`registry/selection_scoring.csv`): MOCS descartado
  para BENCH (solo `Worker`), `construction_ppe_skcet` descartado (55% defectos),
  `construction_safety_hardhat` no disponible.
- **La auditoría del BENCH original** (doc 63): 196 imgs con ~20–25% fuera de
  dominio → nace `bench_v3`. El original se conserva **sin modificar** como
  artefacto histórico.
- **Los 8 candidatos** de la ampliación (doc 66) con licencia/dominio/GT verificados
  → SHEL5K adoptado, CHV promovido.

### Nivel C — fuera del informe (sin uso en v2)

| Qué | Por qué queda afuera | Acción |
|---|---|---|
| `sh17` | CC BY-**NC-SA**; nunca en v2; raw ausente, vistas muertas | Registry actualizado (`raw_absent_views_stale`); vistas `processed/*/original/sh17` **borrables** |
| `construction_ppe` | AGPL-3.0; nunca en v2; raw ausente | Ídem (`processed/*/original/construction_ppe` borrables) |
| `gdut_hwd`/`shwd`/`soda`/`pictor_ppe` | Nunca descargados | Quedan como candidatos registrados |
| `legacy/` (splits y scripts cr01_cr02) | Deprecados con el reinicio v2 (2026-06-17) | Ya movidos y documentados — sin acción |

## 3. Lo que se corrigió hoy en el registry

1. **`mocs`**: la entrada describía el original de anlab340 como "bloqueado
   pendiente de acceso" — pero lo que está en disco (y se usó en el doc 94) es la
   **copia Roboflow `mocs-bowib`** (CC BY 4.0 del uploader, solo `Worker`).
   Entrada reescrita con la procedencia real y el caveat de licencia.
2. **`shel5k`**: figuraba `downloaded_basic_validated` sin rol — es estrato BENCH
   de bench_v3 desde el 07-23. Ahora `bench_v3_stratum`, con sus artefactos.
3. **`chv`**: le faltaba el rol BENCH.
4. **`sh17` / `construction_ppe`**: figuraban como descargados y convertidos — el
   raw no está y las vistas apuntan a otra máquina. Ahora `raw_absent_views_stale`.
5. **`ppe_dataset_rbyz`**: 1,2 GB en disco y **no figuraba en el metadata yaml**
   (solo el doc de evaluación). Entrada agregada con `rejected_s0`.
6. **`license_registry.md`**: fila MOCS actualizada (procedencia de la copia) y
   fila nueva para ppe-dataset.
7. Dir vacío `raw/construction_safety_hardhat` eliminado.

## 4. Limpieza — EJECUTADA (2026-08-05, autorizada por el usuario)

| Qué | Liberó | Verificación previa al borrado |
|---|---|---|
| `raw/ppe-dataset/` | **1,2 GB** | Rechazado por S0, re-descargable de Roboflow, sin artefactos dependientes |
| `processed/{coco,yolo,odvg}/original/{sh17,construction_ppe}` | **~71 MB** | `image_lists` apuntando a `/home/pandulc/Descargas/e4/…` (otra máquina) → doblemente muertas |

`datasets/` pasó de **6,5 GB a 5,3 GB**. Se conservaron a propósito los
`processed/reports/{sh17,construction_ppe}_conversion_report.json` (procedencia de
conversión: metadata, no vista) y todas las referencias en documentación y registry
— registrar un dataset muerto es justamente el punto del registry. Los raw de los 5
datasets del Nivel A **no se tocaron** (y siguen gitignorados por política).

> Corrección al estimado original: las vistas muertas eran ~71 MB, no ~35 MB
> (sh17 60,7 MB + construction_ppe 10 MB).

## 5. La conexión con E-04 (fine-tuning)

El relevamiento confirma lo que la exclusión E-04 declara como "preparación
materializada": vistas YOLO canonical_v2 con `data.yaml` + `image_lists` listas
para Ultralytics, vistas **ODVG** (el formato de entrenamiento de MM-GDINO) para
los 3 datasets TRAIN + shel5k, split `train_v2` (5.540 imgs) congelado y disjunto
del bench, pesos base YOLOE en el media-plane y el slot `models/yoloe/finetuned/`
**vacío esperando**. La contingencia (doc `contingencia/20`) tiene la escalera
T1–T3 con go/no-go pre-registrados; la enmienda natural es que la evaluación use
`bench_v3` (el sucesor congelado del BENCH de 196 que el doc 20 cita) más el GT de
`machinery` del doc 94 como sonda de clase nueva.

## 6. Dónde está cada cosa

| Qué | Dónde |
|---|---|
| Metadata por dataset (fuente de verdad) | `datasets/registry/datasets_metadata.yaml` |
| Licencias y estados de uso | `datasets/registry/license_registry.md` |
| Rechazo de ppe-dataset | `datasets/registry/evaluation_ppe_dataset.md` |
| Scoring de candidatos | `datasets/registry/selection_scoring.csv` |
| Composición y salvedades de bench_v3 | `datasets/registry/bench_v3.md` |
| Conversiones y conteos por clase | `datasets/registry/conversion_report.md` |
| Índice de resultados de imágenes | `e-ovrt_experimental-setup/results/bench_imagenes/index.md` |
