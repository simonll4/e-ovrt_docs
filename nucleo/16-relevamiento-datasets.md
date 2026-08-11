# 16 — Relevamiento: `e-ovrt_datasets`

- **Fecha de relevamiento:** 2026-08-10
- **Método:** relevado **contra git y código**. Los comandos de §2 y la suite de §7 se
  ejecutaron en esta máquina.
- **Regla de este documento:** **no publica ninguna cifra de resultado.** Los tamaños de
  dataset y la composición de los bancos sí están —son hechos de estructura, no
  mediciones—; las métricas viven en los cuatro índices de
  `e-ovrt_experimental-setup/results/`.

---

## 1. Qué es, y qué no es

La **cabecera de la cadena**: adquisición, validación y conversión de datos. Produce tres
cosas que el resto del proyecto consume:

1. El **vocabulario canónico** de clases, que acopla este repo con el media-plane.
2. El **banco de imágenes** (`bench_v3`) para evaluación de detección.
3. El **banco de clips de video** (`clip_bench`) con GT temporal humano, y el material de
   video del que sale.

**Qué NO es:** no es un paquete Python. **No hay `pip install`, no hay Makefile.** Son
scripts sueltos de Python y bash que resuelven rutas relativas a la raíz del repo
(`Path(__file__).resolve().parents[3]`), así que se ejecutan desde cualquier lado pero
esperan que existan `datasets/raw/` y `datasets/processed/`. Dependencias: `Pillow` (y
`kaggle` solo para la descarga de SH17, hoy legacy).

**Tampoco entrena ni evalúa modelos.** Prepara datos y produce GT; medir es del media-plane
y del control-plane.

## 2. Cómo se ejecuta

```bash
# Descarga de datasets crudos (selección v2 activa)
ROBOFLOW_API_KEY=<key> datasets/scripts/download/download_construction_site_safety.sh
datasets/scripts/download/download_chv.sh                    # sin API key
ROBOFLOW_API_KEY=<key> datasets/scripts/download/download_ppe_siabar.sh

# Validación de un dataset crudo (conteos y chequeos de sanidad)
datasets/scripts/validate/summarize_raw_dataset.sh

# Conversión raw -> COCO + YOLO + ODVG, vista canónica
python3 datasets/scripts/convert/convert_datasets.py \
    --datasets construction_site_safety chv ppe_siabar --views canonical_v2

# Manifiestos de rol TRAIN / BENCH / DEMO  -> datasets/splits/v2/
python3 datasets/scripts/curate/build_role_views.py

# GT a nivel persona para la evaluación del BENCH
python3 datasets/scripts/bench/build_person_gt.py

# Banco de imágenes v3 (idempotente, lee las 4 fuentes curadas)
python3 datasets/scripts/curate/build_bench_v3.py

python3 -m pytest datasets/tests/ -q     # 418 passed (2026-08-10) — fixtures sintéticos
```

La suite **no requiere datos crudos**: usa fixtures sintéticos.

## 3. Estructura

```
datasets/
├── scripts/
│   ├── download/    # un script por dataset
│   ├── validate/    # conteos y sanidad del raw
│   ├── convert/     # convert_datasets.py — LA fuente de verdad de las vistas
│   ├── selection/   # scoring de candidatos
│   ├── curate/      # build_role_views.py, build_bench_v3.py
│   ├── bench/       # build_person_gt.py y derivados
│   └── videogt/     # cadena del GT temporal de video (spec 43)
├── raw/             # MOCS · chv · clip_bench · construction_site_safety · ppe_siabar · shel5k
├── processed/       # coco/ · yolo/ · odvg/ · clip_bench/ · reports/ · audit_task43/
├── splits/v2/       # train.txt · bench.txt · demo.txt · manifest.json
└── registry/        # procedencia, licencias, contratos de anotación
datasets-videos/     # material de video (§5.3)
legacy/              # vistas y scripts deprecados, conservados
```

**`configs()` dentro de `convert_datasets.py` es la fuente de verdad** para agregar un
dataset: ahí viven las particularidades de formato, la lista de clases y el mapeo a
`canonical_v2` de cada fuente.

## 4. El vocabulario canónico — el acople con el media-plane

Desde el 2026-06-17 el repo emite **varias vistas por dataset**:

| Vista | Qué es |
|---|---|
| `original` | Las clases de la fuente, sin tocar |
| **`canonical_v2`** | **El vocabulario canónico**: `person`, `helmet`, `vest`, `bare_head` (más los atributos `has_helmet` / `has_vest`, solo en la vista BENCH) |
| `train_v2`, `bench_v2`, `demo_v2` | Splits por tarea, derivados de `canonical_v2` |
| ⚠️ `canonical_cr01_cr02`, `finetuning_cr01_cr02` | **DEPRECADAS**. Reemplazadas por las v2; los scripts viven en `legacy/` |

**Este es el punto de acople duro con el media-plane**: sus catálogos y prompts hablan este
vocabulario. **Cambiar un nombre de clase o una condición obliga a mover los dos repos a
la vez.**

**Flujo del dato:**

```
raw/<dataset_id>/ → convert_datasets.py --views canonical_v2
   → processed/{coco,yolo,odvg}/canonical_v2/<dataset_id>/
      → build_role_views.py → splits/v2/{train,bench,demo}.txt
```

Los tres datasets con rol TRAIN son `construction_site_safety`, `chv` y `ppe_siabar`.

## 5. Los bancos de evaluación

### 5.1 `bench_v3` — el banco de imágenes

Vive en `datasets/processed/coco/bench/curated/bench_v3.json`. **Estratifica 6.477
imágenes sobre tres fuentes independientes**, y cada imagen lleva su `stratum`:

| Estrato | Imágenes | Qué aporta |
|---|---|---|
| `bench_obra` | 147 | Núcleo curado, revisado visualmente |
| `chv` | 1.330 | Mejor AP de chaleco medido |
| `shel5k` | 5.000 | GT nativo de `bare_head` (vía clase `head`), con `person_gt_shel5k.json` para los atributos de CR-01 |

`bench_v3_manifest.json` lleva un sha256 por fuente para verificar el congelamiento.
Procedencia y salvedades por estrato: `datasets/registry/bench_v3.md`.

> **Regla de reporte, no negociable: siempre por estrato Y agregado. Nunca solo el
> agregado.**

> **El BENCH viejo de 196 imágenes NO es este.** El split BENCH original de
> `construction_site_safety` resultó ~20-25% fuera de dominio (selfies de COVID, PASCAL
> VOC, aeropuerto, casino — auditado en `operacion/63`). Se conserva **sin modificar** como
> artefacto histórico; el derivado curado es `bench_v3`.

### 5.2 `clip_bench` — el banco de video

En `datasets/processed/clip_bench/`: `meta/<clip_id>.clip.yaml` (un archivo por clip, con
escenario, master, licencia y las correcciones firmadas del GT), `annotations/`, `gt/`,
`manifest.yaml`, `clip_bench.sha256` y `_retired/` para los clips retirados **con causa
escrita** (no se borran).

Dos bloques: **A** el rodaje propio guionado, **B** el lote de internet (obra real, no
guionada). Los conteos vigentes de clips, episodios y evaluables **no van acá**: salen de
`e-ovrt_experimental-setup/results/clip_bench/index.md`, que es la referencia citable.

**Las anotaciones del repo son la fuente de verdad, por encima de CVAT.** Hay un guard
`--check` en la cadena para verificarlo.

**Cadena del GT de video** (`scripts/videogt/`): `split_cvat_project.py` → `derive` →
`validate` → `promote` → `aggregate`.

### 5.3 `datasets-videos/` — el material de video

**8,4 G**, la fuente única del material de video desde la reorganización de `operacion/109`:
`raw/` (los masters), `clips/`, `preann/`, `corrected/`, `review/`, `gt/`, más un
`.clip.yaml` por clip en la raíz, `README.md` y `GUIA-CVAT.md`.

Los `.mp4` están gitignoreados. El propio README (línea 197) declara la convención:
`datasets/raw/clip_bench/clips/<clip_id>.mp4  # GIT-IGNORED (sube a Drive a mano)`.

## 6. Política de versionado y registry

**Se versiona:** documentación, scripts, metadatos del registry y las salidas procesadas
necesarias para reproducir. **No se versiona:** imágenes, videos y archivos crudos.

Verificado el 2026-08-10: de los 13.161 archivos versionados, lo que hay bajo `raw/` son
**anotaciones, no medios** — `raw/shel5k` son 5.000 `.xml` y `raw/chv` 1.333 `.txt`. **Cero
imágenes versionadas.** La política se cumple, y es lo que sostiene la declaración de
"sin redistribución" de las licencias de terceros.

**`datasets/registry/`** es donde vive la procedencia: `datasets_metadata.yaml`,
`license_registry.md`, `download_log.md`, `class_mapping.yaml`, `conversion_report.md`,
`bench_v3.md`, `clip_bench.md`, `annotation_contract_v2.yaml`, `curation_bench_obra.md`,
`bench_gt_audit.md`, `selection_scoring.csv` y la
`plantilla-consentimiento-audiovisual.md`.

## 7. Estado de implementación y límites

**Construido:** la cadena completa de descarga → validación → conversión → vistas →
splits; los dos bancos; la cadena de GT temporal de video. Suite: **418 passed**.

**Límites y huecos declarados:**

- **Licencia de `chv` parcial** — sin licencia formal (SPDX: none), con grant informal de
  los autores. Uso con **cita obligatoria** y sin redistribución de imágenes.
- **MOCS** — se usó una copia de terceros; el original nunca se descargó ni se verificó.
  Citar el paper original.
- **Lote de internet** — *Standard YouTube License*, **no** Creative Commons. Uso
  académico con cita, sin redistribución.
- **URL por video: pendiente.** Los `.clip.yaml` del lote llevan `master: raw/N.M.mp4` y
  `license.video_url: TODO`. **No es recuperable desde el disco**: no hay registro del
  origen de cada master. Es tarea manual, y es evidencia perecedera — si el canal baja los
  videos, se pierde la referencia.
- **Vistas deprecadas** — `canonical_cr01_cr02` y `finetuning_cr01_cr02` siguen en
  `legacy/`, no se usan.
- **La vista YOLO** (6.338 archivos versionados) existe para soportar fine-tuning, que no
  se ejerció (E-04). Se conserva porque es parte del fundamento de que E-04 fue **decisión
  de secuenciación** y no falta de preparación.

## 8. Trampas conocidas

1. **El export de CVAT es a nivel PROYECTO.** Sin `split_cvat_project.py`, el GT sale
   **negativo en silencio** — el modo de falla más caro de esta cadena.
2. **Editar el yaml de un clip ya promovido obliga a re-derivar su GT.** Si no, el GT deja
   de ser re-derivable y queda desalineado.
3. **Los "person N" de la interfaz de CVAT no coinciden con los `track_id` del XML
   exportado.** Verificar dibujando la caja del track sobre el frame; asumir la
   correspondencia ya produjo declaraciones de episodio erróneas.
4. **`datasets_videos_dir` custom rompe `prepare_clip.sh`.**
5. Los scripts asumen que `datasets/raw/` y `datasets/processed/` existen.

## Referencias

`14` (mapa de la cadena) · `17` (media-plane, el consumidor del vocabulario) ·
`specs/43-clip-bench-gt-temporal.md` · `datasets/registry/bench_v3.md` y `clip_bench.md` ·
`operacion/63` (auditoría del BENCH viejo) · `operacion/99` (relevamiento de datasets de
imágenes) · `operacion/109` (fuente única del material de video) ·
`informe/ajustes/gobierno/99-materiales-de-cierre.md` §3 (licencias y citas obligatorias).
