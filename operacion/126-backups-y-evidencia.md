# 126 — Qué se respalda en Drive: evidencia, seguro y descarte (2026-08-19)

- **Antecedente:** el pase de limpieza general del 2026-08-19 (ver §6) dejó los seis
  repos commiteados y pusheados. Este doc responde la pregunta que queda después:
  **el código ya está a salvo en GitHub; ¿qué NO está, y de eso qué hay que subir a Drive?**
- **Estado: cerrado como criterio.** La ejecución de las copias es manual del usuario.

---

## 1. El principio

Todo lo que está versionado y pusheado ya tiene respaldo remoto: los seis repos viven en
GitHub. **Drive no es para el código.** Drive es para lo que git ignora deliberadamente —
que es, justamente, casi toda la evidencia experimental del proyecto.

La pregunta correcta no es "¿esto es grande?" sino **"si esto se pierde, ¿se puede
regenerar con un comando versionado?"**. Tres respuestas, tres capas:

| Capa | Criterio | Si se pierde |
|---|---|---|
| **1. Evidencia** | No se regenera: trabajo humano, corridas de cluster, o el dato que sostiene una afirmación del informe | Se cae una parte del informe o de la defensa |
| **2. Seguro** | Se regenera, pero caro, lento, o dependiendo de terceros que pueden desaparecer | Se pierden semanas, no el argumento |
| **3. Descarte** | Un comando versionado lo reconstruye | Nada: se vuelve a bajar |

---

## 2. Capa 1 — EVIDENCIA (subir sí o sí) · ≈ 2,6 GB

Cabe entero en una cuenta gratuita de Drive. Esto es lo que defiende el informe.

| Ruta | Tamaño | Por qué es irremplazable |
|---|---|---|
| `docs/operacion/datos/` | 1,2 GB | La evidencia cruda de cada doc numerado. Cada afirmación de `operacion/` se verifica acá. Sin esto los docs son aserciones sin respaldo |
| `e-ovrt_experimental-setup/finetuning/weights/finetuned/` | 1,2 GB | Checkpoints de los jobs de Mendieta (T1 `1167640`, T2 `1167864`). **Regenerarlos = re-encolar en el cluster**: días de cola ajena, no un comando |
| `e-ovrt_experimental-setup/finetuning/runs/` | 1,1 GB | Evaluaciones T1 *tuned* vs *baseline* contra `bench_v3` — la medición que firmó el **NO-GO de T1** (doc 123) |
| `e-ovrt_experimental-setup/results/` | 123 MB | Los **4 índices verificables**: la única fuente de cifras del informe (regla de gobierno). Verificables con `docs/operacion/datos/96-verificar-indices.py` |
| `e-ovrt_experimental-setup/defensa/` | 112 MB | Videos de defensa ya renderizados (V1/V3/VG1/VG1e + montaje) |
| `_archived/` (raíz del workspace) | 95 MB | Bandejas originales de CVAT y material de trazabilidad. Es el insumo humano del que salió el banco |
| `e-ovrt_datasets/.../processed/clip_bench/` | 56 MB | **GT de video anotado a mano** (34 clips, 35 episodios). Horas de anotación humana en CVAT: no hay comando que lo rehaga |
| `docs/informe/` | 29 MB | El entregable en curso más los `.docx` con comentarios de los correctores |
| `e-ovrt_datasets/.../processed/coco/bench/` | 21 MB | `bench_v3` congelado (6.477 imgs) + los estratos curados y su manifiesto sha256 |

> **Nota sobre `clip_bench/` y `coco/bench/`:** parte de esto sí está versionado (la
> política del repo versiona `processed/coco/bench/`), pero se sube igual: es barato y es
> el corazón de la medición.

## 3. Capa 2 — SEGURO (subir si hay espacio) · ≈ 9,2 GB

| Ruta | Tamaño | Matiz |
|---|---|---|
| `scripts/downloads/` | 7,1 GB | Videos crudos del lote de internet. **Es "regenerable" solo mientras las URLs sigan vivas** — link rot es un riesgo real en YouTube. ⚠ **Hasta que se cierre C1 (las URLs de los 18 `clip.yaml`), esto es evidencia de procedencia, no descarte.** No borrar antes de C1 |
| `e-ovrt_media-plane/runs/` | 1,9 GB | 472 corridas. Regenerables *si* el modelo, el dataset y la config siguen existiendo; caras en GPU. Las que sostienen resultados publicados ya están curadas en `results/evidence-runs/` (capa 1) |
| `e-ovrt_experimental-setup/runs/` | 108 MB | Ídem, del lado del runner |
| `e-ovrt_control-plane/runs/` | 6,7 MB | Barato, subir sin pensarlo |

## 4. Capa 3 — NO subir (se rehace con un comando) · ≈ 23 GB

| Ruta | Tamaño | Cómo se rehace |
|---|---|---|
| `e-ovrt_experimental-setup/finetuning/cache/` | 11 GB | Bundles de envío al cluster: `finetuning/scripts/package_*.py` |
| `e-ovrt_datasets/datasets/raw/` | 6,6 GB | `datasets/scripts/download/*.sh` (requiere `ROBOFLOW_API_KEY`) |
| `e-ovrt_media-plane/models/` | 5,6 GB | `make download-models` |
| `e-ovrt_datasets/datasets/processed/` (salvo `bench/` y `clip_bench/`) | ~130 MB | `convert_datasets.py --views canonical_v2` |
| `finetuning/weights/base/` | 277 MB | Pesos públicos de Ultralytics |
| `.venv*/`, `node_modules/`, `__pycache__/`, `finetuning/data/` | — | Instalación limpia |

## 5. Lo que NO va a Drive por seguridad

- **`e-ovrt_experimental-setup/cameras/`** (16 KB) — presets RTSP/OAK-D con **credenciales
  en claro**. Está gitignorado por eso mismo. Si se respalda, va **cifrado** (o mejor: las
  credenciales a un gestor de contraseñas y el resto del archivo como plantilla sin
  secretos). Nunca a una carpeta de Drive compartida.
- Cualquier `.env` con `HF_TOKEN`, `ROBOFLOW_API_KEY` o credenciales MQTT.

## 6. Estructura sugerida en Drive

```
E-OVRT-VDP/
├── 01-evidencia/          ← capa 1, la que se respalda siempre
│   ├── operacion-datos/   ├── finetuning-checkpoints/   ├── finetuning-runs/
│   ├── results/           ├── defensa/                  ├── archived-cvat/
│   ├── clip-bench-gt/     ├── informe/                  └── bench-v3/
├── 02-seguro/             ← capa 2, si hay espacio
│   ├── videos-internet/   └── runs-*/
└── 00-LEEME.txt           ← copiar acá el §1 de este doc (el criterio de las 3 capas)
```

**Cadencia sugerida:** capa 1 después de cada hito que produzca evidencia nueva (una
campaña, un job de cluster, una tanda de anotación). Capa 2, cuando sobre espacio.

---

## 7. Constancia del pase que originó este doc

El 2026-08-19 se ejecutó una limpieza general de los seis repos: archivado de código y
configs legacy, sincronización de documentación a ADR-019/ADR-020 y `bench_v3`, y el
**deploy integral de la plataforma en Docker Compose**
(`e-ovrt_experimental-setup/infra/platform/`, 13 servicios con paridad de rutas). Detalle
por repo en los mensajes de commit de ese día. Suites al cierre: media-plane 665,
control-plane 312, distribución 133, datasets 418+, experimental-setup 88, webconsole
backend 667, herramientas de docs 36.

Pendiente operativo que sobrevive a este doc: **encender el daemon de Docker y correr
`docker compose build` + el smoke integral** del `infra/platform/README.md` (el daemon
estaba apagado el día del pase).
