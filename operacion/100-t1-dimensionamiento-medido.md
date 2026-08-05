# 100 — T1 (E-04): dimensionamiento MEDIDO del linear probing

- **Fecha:** 2026-08-05.
- **Qué es:** el cierre de la tarea 9 del relevamiento (doc 99): el tier T1 de la
  escalera de `contingencia/20` deja de estar estimado en papel y pasa a tener
  **costo medido**, vía un smoke real del loop completo de entrenamiento.
- **Qué NO es:** T1 ejecutado. Las métricas de acá **no son un resultado** — salen
  de 1 época sobre el 5% de los datos. E-04 sigue siendo
  "condicionada no ejercida"; lo único que cambió es que ahora el costo de
  ejercerla tiene número, no adivinanza.
- **Scripts:** `datos/100-t1-preparar-datos.py` (árbol de entrenamiento),
  `datos/100-t1-entrenar-lp.py` (linear probing con `YOLOEPETrainer`).

> ## D-100.1 — El entrenamiento NO se ejecuta en la PC local (decisión del usuario, 2026-08-05)
>
> Ningún tier de la escalera (T1/T2/T3) se corre en esta máquina: el riesgo de
> castigar la GPU del equipo de trabajo no se acepta. **El entrenamiento va al
> clúster administrado — Mendieta (CCAD-UNC), 2×A30 24 GB por nodo, asignación
> mínima 1 GPU + 10 cores + 64 GB RAM, Slurm** (doc 20 §2, Anexo B B.4/B.5), que ya
> era el hardware presupuestado.
>
> Lo que sí se hace local es exactamente lo de este documento: **validar que el loop
> corre y dimensionar**, con un smoke de 1 época sobre 186 imgs. Y el paso previo a
> pedir turno en el clúster es **verificar viabilidad** (datasets, formatos,
> entorno, transporte, licencias) — el §6 es esa checklist.
>
> ## D-100.2 — Secuencia: esto va AL FINAL
>
> El fine-tuning se retoma **después de cerrar todo lo de benchmarking y las
> evaluaciones principales de la plataforma**. No compite con el cierre de
> resultados ni con la redacción. Hoy lo que falta de esa cola es el **GT del lote
> de internet (CVAT, `v06_c01`+`v04_c01`) → soak/FAR** y los **videos de defensa
> V1–V3**; recién con eso cerrado se vuelve acá.

---

## 1. Lo que se corrió

`YOLOE-26s` inicializado desde `yoloe-26s.yaml` + pesos `yoloe-26s-seg.pt`
(gotcha del doc 20 §4.1: los checkpoints son de segmentación), entrenado con
`YOLOEPETrainer` — que **borra SAVPE, pre-computa los text embeddings con
`get_text_pe(names)` y deja entrenables solo las conv finales de las ramas
`cv3`/`one2one_cv3`: ~400 K parámetros**, no los 1,85 M que costaría SAVPE. La
capacidad open-vocabulary del resto del modelo no se toca: **retención por
construcción**, que es el criterio con el que el doc 20 §6 justifica T1 como el
tier de bajo riesgo.

Datos: `css train` (2.603) + `ppe_siabar train` (1.120) = **3.723 imgs**; monitor
`ppe_siabar val` (326). Smoke: 1 época, `fraction=0.05` (186 imgs), `batch=8`,
`workers=2`, `imgsz=640`, `seed=100`, `deterministic=True`.

## 2. Dos verificaciones que había que hacer antes de creer cualquier número

**V1 — las labels son las canónicas, no las del raw.** Ultralytics deriva la ruta
de labels reemplazando `/images/` → `/labels/`, y las `image_lists` de
`canonical_v2` apuntan al **raw**, donde viven las labels originales de Roboflow
(10 clases). Entrenar con las listas directamente habría usado el esquema
equivocado **sin emitir un solo error**. El árbol de symlinks lo evita, y se
verificó: **3.723/3.723 labels resuelven dentro de `canonical_v2`**, con ids
estrictamente en `{0,1,2,3}`.

**V2 — no hay leakage con `bench_v3`.** El rol TRAIN (`train_v2`, 5.540) incluye
**todo `chv`**, y `chv` es estrato de `bench_v3` desde el 07-23: entrenar con
`train_v2` y evaluar en `bench_v3` sería circular justo en el estrato estrella de
`vest`. Enmienda: el entrenamiento excluye `chv` y `shel5k`. Y no se dio por
supuesto — se comprobó contra el bench real: **intersección 0** en basename y en
stem, para train y para val, contra las 6.477 imgs de `bench_v3`. De paso confirma
que los splits internos de `construction_site_safety` son disjuntos, que es de
donde salen las 147 de `bench_obra`.

## 3. El costo medido

| Magnitud | Medición | Contra lo pre-registrado (doc 20) |
|---|---|---|
| Época de 186 imgs (24 batches de 8) | **16,0 s** de train; 21,6 s con val | — |
| **Extrapolación a T1 completo** (3.723 imgs × 10 épocas) | **≈ 53 min de train + ~30 s de val por época ≈ 1 h** | Cae dentro del rango estimado **1–3 GPU-h**: confirmado |
| VRAM en entrenamiento | **2,42–2,61 GB** de 8.188 MiB | Holgado; el doc 20 daba la RTX 4060 como "marginal" — con `batch=8` no lo es |
| RAM del VM (pico) | **5.760 MB de 7.565** | **Ajustado: 1,8 GB de headroom** (ver §5) |
| Inferencia | 3,8 ms/img (0,2 pre + 0,2 post) | — |
| Modelo fusionado | 9.466.728 params, 20,5 GFLOPs | — |

**Salvedades de la extrapolación, explícitas:** el 5% muestreado puede no
representar la distribución de tamaños de imagen del conjunto completo, y la
primera época incluye chequeos de AMP y construcción de caches. El número honesto
es **≈1 h ± algo**, no 53 min exactos.

**Para qué sirve este número, dado D-100.1.** No es "lo que costaría correr T1 acá"
—acá no se corre— sino **el presupuesto con el que se pide turno en el clúster, y es
conservador por construcción**: está medido en una RTX 4060 Laptop (8 GB, `batch=8`),
y la A30 tiene 24 GB y ~3× el ancho de banda de memoria, así que en Mendieta el
mismo trabajo debería costar **menos** de 1 GPU-h, con margen para subir el batch.
La otra cosa que el número prueba es la que no se puede pedir por Slurm: que **el
loop de linear probing corre de punta a punta con estos datos y estos guards**, así
que el turno de clúster no se gasta descubriendo que el árbol de labels estaba mal.

## 4. F-100.1 — el val de monitoreo es CIEGO a `bare_head` (enmienda obligatoria)

El smoke reportó tres clases, no cuatro:

```
              Class   Images  Instances    Box(P)      R    mAP50
                all      326        973     0.400  0.377    0.326
             person      246        302     0.227  0.785    0.445
             helmet      232        273     0.618  0.341    0.427
               vest      307        398     0.355  0.007    0.106
```

`302 + 273 + 398 = 973` = el total. **`ppe_siabar val` no tiene una sola instancia
de `bare_head`** (train sí: 2.318). El split de monitoreo se eligió por una razón
correcta — es el único candidato que no es estrato de `bench_v3`, así que no
contamina el eval — pero tiene una consecuencia que invalidaría T1 si no se
corrige: **la hipótesis central de T1 es justamente si el ajuste de embeddings
rescata `vest` y `bare_head`, y el monitor no puede ver `bare_head`**. Peor: con
`val=True`, `best.pt` se elegiría por un mAP que ignora la clase de interés.

Enmiendas posibles, ninguna ejecutada todavía:
1. Seleccionar el checkpoint por **`last.pt`** en vez de `best.pt` (10 épocas de LP
   sobre 400 K params no sobreajustan de forma peligrosa), o
2. armar un val con `bare_head` que no sea estrato de `bench_v3` — hoy no existe:
   `bare_head` nativo solo lo trae `shel5k`, que **es** estrato. Habría que
   particionar `shel5k` y retirar esa partición de `bench_v3`, lo que rompe el
   congelamiento del bench (sha256 en `bench_v3_manifest.json`), o
3. dejar el monitor como está y **medir `bare_head` solo en el eval final** contra
   `bench_v3`, declarando que el entrenamiento corrió a ciegas en esa clase.

La 3 es la única que no toca el bench congelado. La decisión es del usuario y es
previa a correr T1 completo.

> Las métricas de arriba **no dicen nada** sobre si T1 funciona: 1 época sobre 186
> imágenes. `vest` con recall 0,007 es ruido de arranque, no un hallazgo.

## 5. F-100.2 — los defaults de ultralytics tiran WSL abajo (`global_oom`)

Dos caídas de WSL durante esta jornada (05:12:33 y 05:20:38) **no fueron de la GPU
ni de disco**: fueron `global_oom` del VM. Mecanismo verificado en `journalctl`
(journald es persistente acá, así que los boots previos sobreviven a la caída):

```
pt_data_worker invoked oom-killer: ... global_oom
Out of memory: Killed process 5807 (python)
  total-vm:33137296kB  anon-rss:1117832kB  shmem-rss:2928008kB
misc dxg: dxgk: create_existing_sysmem: get_user_pages_fast failed: 3549
systemd[1]: init.scope: The kernel OOM killer killed some processes in this unit.
```

El host tiene 15,25 GiB y el `.wslconfig` **no declara memoria** (solo
`networkingMode=mirrored`, que sostiene las cámaras link-local del doc 68), así que
WSL corre en el default: **7,4 GiB de cap, con `/dev/shm` tomando 3,7 GiB de ese
mismo total**. Con `nproc` = 16, ultralytics elige **`workers=8`**: ocho DataLoader
workers a 640px + 2,9 GiB de shmem + ~1,3 GiB del tooling de la sesión agotan el
VM. El OOM killer entonces siega procesos de `init.scope` —donde en WSL vive el
init de la distro— y **cae la distro entera, no solo el entrenamiento**.

Trampa de lectura: los `misc dxg: … Ioctl failed: -12` que aparecen justo después
son **consecuencia** (`get_user_pages_fast failed`: ya no había páginas), no causa.
Hacen parecer que fue el driver de GPU. Hay un tercer episodio idéntico el Jul 27
04:51 (víctima: `uvicorn`), así que es una condición crónica del host, no de T1.

**Mitigación aplicada y verificada:** `workers=2` y `batch=8` como defaults del
script, más correr el entrenamiento acotado por cgroup (cgroup v2 está con el
controlador `memory` delegado al user slice):

```bash
systemd-run --user --scope -p MemoryMax=4G -p MemorySwapMax=2G <venv>/bin/python …
```

Así una explosión mata al proceso con error claro dentro de su cgroup en vez de
disparar `global_oom`. El smoke corrió así y **WSL sobrevivió** (pico 5.760 MB).

**Nota de alcance tras D-100.1:** la recomendación de subir la RAM del VM **ya no es
un requisito de T1** (T1 no se corre acá). Pero sigue valiendo por otra razón: la
condición es del host, no del entrenamiento — el episodio del Jul 27 04:51 se llevó
un **`uvicorn`**, es decir un servicio de la plataforma. Con 1,8 GB de headroom,
cualquier corrida larga de los dos planos convive con el mismo riesgo. Si se quiere
cerrar esa exposición: `memory=10GB` + `swap=8GB` en el `.wslconfig` **sin tocar
`networkingMode=mirrored`** (es lo que sostiene las cámaras link-local del doc 68) y
`wsl --shutdown`. Queda como decisión de higiene del host, desacoplada de E-04.

**Trampa colateral:** `/tmp` se limpia en el reboot, así que el árbol de symlinks
desapareció con la caída y hay que regenerarlo (segundos) antes de reintentar.

## 6. Checklist de viabilidad para pedir turno en el clúster

Esto es lo que hay que poder responder **antes** de reservar GPU en Mendieta. No es
un plan de ejecución: es la puerta.

### 6.1 Ya verificado local (no hace falta el clúster para esto)

| Pieza | Estado |
|---|---|
| Árbol de entrenamiento con guards (labels canónicas, stems únicos, conteos exactos) | ✅ listo y verificado |
| Disjunción train ∩ `bench_v3` | ✅ comprobada contra el bench real: **0 intersección** |
| Loop de linear probing end-to-end | ✅ smoke verde, `rc=0` |
| Presupuesto de cómputo | ✅ **≤1 GPU-h en A30** (medido ≈1 h en 4060, cota conservadora) |
| Formatos de datos | ✅ YOLO `canonical_v2` con `data.yaml` + `image_lists`; ODVG listo para el camino T3 |
| Pesos base | ✅ `yoloe-26{s,m,l,x}-seg.pt` cacheados |

### 6.2 Falta verificar antes de pedir turno

| Pieza | Por qué importa |
|---|---|
| **Decisión sobre F-100.1** (monitor ciego a `bare_head`) | **Bloquea.** Define si el turno se gasta entrenando algo cuya clase central no se puede monitorear. |
| **Entorno reproducible en el clúster** | Versión de ultralytics (acá 8.4.86), CUDA (Mendieta: 12.x candidato vs `torch 2.12.1+cu130` local), y si se resuelve por venv, container o módulo del sitio. Es el costo dominante según doc 20 §3.2, y para T3 (MMDetection) es el riesgo alto. |
| **Transporte de datos** | 3.723 imgs de train + el árbol de labels. Definir el mecanismo (rsync/scp/almacenamiento del sitio) y la cuota disponible. |
| **Evaluación** | No está armada: falta el puente de detecciones del modelo fine-tuneado a `bench_v3` + el GT de `machinery` del doc 94 como sonda de clase nueva. |
| `pycocotools` | Ausente del entorno local. No bloquea T1; sí las métricas COCO de la Tabla 32 que pide T2. |
| **Política de datos del clúster** | Ver 6.3. |

### 6.3 Hallazgo de licencias: la enmienda anti-leakage dejó el payload limpio

Un efecto lateral afortunado de excluir `chv` del entrenamiento (§2, V2): los dos
datasets que **sí** viajan al clúster son `construction_site_safety` y `ppe_siabar`,
**ambos CC BY 4.0, con redistribución permitida con atribución**. Los que tienen
restricción — `chv` ("open for free use", **imágenes NO redistribuibles**, cita
obligatoria `wang2021ppe`) y la copia Roboflow de `MOCS` (uso evaluativo, sin
redistribución) — **no forman parte del conjunto de entrenamiento**.

De ahí la arquitectura recomendada, que además es la más barata:

> **Entrenar en el clúster, evaluar local.** La inferencia es baratísima (3,8 ms/img
> medidos), así que el eval contra `bench_v3` corre acá sin turno de GPU, y las
> imágenes con restricción de redistribución (`chv`, y `shel5k` por volumen: 2,5 GB)
> **nunca salen de esta máquina**. Al clúster sube solo material CC BY 4.0 y bajan
> solo pesos.

### 6.4 Lo que no se negocia

El go/no-go pre-registrado de la Tabla 37 (ΔAP ≥ +0,05 absoluto en la clase objetivo
**o** rescate de recall <0,1 → >0,5; retención ≤10% de caída relativa; sin
degradación de latencia) sigue vigente y **no se negocia después de ver resultados**.
