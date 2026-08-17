# 100 — T1 (E-04): dimensionamiento MEDIDO del linear probing

- **Fecha:** 2026-08-05.
- **Qué es:** el cierre de la tarea 9 del relevamiento (doc 99): el tier T1 de la
  escalera de `contingencia/20` deja de estar estimado en papel y pasa a tener
  **costo medido**, vía un smoke real del loop completo de entrenamiento.
- **Qué NO es:** T1 ejecutado. Las métricas de acá **no son un resultado** — salen
  de 1 época sobre el 5% de los datos. (✎ 2026-08-11: *decía "E-04 sigue siendo
  condicionada no ejercida"* — desde
  [ADR-017](../decisiones/adr-017-fine-tuning-jornada-experimental.md) E-04 es
  **jornada experimental comprometida**, y este doc es el dimensionamiento y la
  puerta de entrada de esa jornada.) El costo de ejercerla tiene número, no
  adivinanza.
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
>
> ✎ **2026-08-11 — condición CUMPLIDA (el GT del lote cerró el 08-09) y estatuto
> superado por ADR-017:** "el final" llegó — E-04 es **jornada comprometida** y su
> entrada son las puertas del §6 (decisión sobre F-100.1 primero). La secuencia de
> D-100.2 era **orden metodológico** (baseline y evaluaciones primero), no una causa
> de descarte, y así se declara en el informe.

> ## Adenda 2026-08-13 — F-100.1 resuelta; el full vuelve a NO-GO por alcance entrenable
>
> Esta adenda actualiza el estado operativo sin borrar la medición histórica de las secciones
> siguientes:
>
> 1. **F-100.1 quedó resuelta sin tocar `bench_v3`.** El split derivado
>    `finetuning_v1` contiene **2.946 train + 483 val**. Su `val` es disjunto por hash,
>    linaje y componente perceptual, y cubre `person=1.829`, `helmet=759`, `vest=784` y
>    `bare_head=408`. D-FT-01 quedó aprobada: 10 épocas, `best.pt` por máximo
>    `metrics/mAP50-95(B)` agregado sobre las cuatro clases y `last.pt` conservado.
>    F-100.1 se resolvió por una **CUARTA vía** no listada en §4: split propio
>    `finetuning_v1` por grupos (D-FT-11/D-FT-01, aprobadas por el usuario el
>    2026-08-13). Las tres enmiendas originales de §4 quedan históricas; ADR-017 §2d
>    hablaba de “las tres enmiendas”, pero lo ejecutado fue esta cuarta vía superadora.
> 2. **El smoke `1166552` fue técnicamente verde, no metodológicamente válido.** Terminó
>    `COMPLETED 0:0` en una A30, con **1:44** de pared, **45,264 s** dentro del trainer y
>    **7,82 GB** máximos. Produjo y recargó checkpoints, pero la auditoría posterior encontró
>    estado del optimizador para **366/366 tensores**: el freeze upstream pretendido por T1 no
>    fue efectivo. Ese run prueba infraestructura, no el linear probing pre-registrado; su gate
>    de full queda revocado.
> 3. **El smoke corregido `1166583` cerró el gate técnico.** Terminó `COMPLETED 0:0` en A30:
>    3:10 Slurm, 1:51 CPU, 7,64 GB/16 GB, 40,83445 s del script y `GPU_mem=0.543G`. Produjo
>    `best`/`last`/`epoch0`/`results`; confirmó 12 tensores/3.096 parámetros y optimizer con 12
>    parámetros en grupos `[6, 0, 6]` y 12 estados. Gate v2/live verify validó 20 críticos.
>    Es una prueba funcional de 1 época/5 %, no una cifra científica ni una medición full.
> 4. **El contrato de retención se precisa.** Congelar el backbone era la intención de T1,
>    pero el head sí cambia y el checkpoint fusionado usa vocabulario fijo. Esto reduce el
>    alcance del ajuste; no demuestra por sí solo retención open-vocabulary. D-FT-08 y el gate
>    de serving/evaluación deben resolver esa semántica antes del full. ✎ **2026-08-15: D-FT-08
>    firmada.** La semántica quedó resuelta por restricción: vocabulario cerrado, y la retención
>    exigible por D-FT-12 es **in-domain**, no generalista.
> 5. **Costo actualizado: punto central estimado ≈16 min; planificar 30–45 min y conservar
>    walltime 2 h.** Esto no es una medición full. En `1166583`, 19 batches de train tomaron
>    3,9 s (≈4,87 batch/s). Para 2.946 imágenes con batch 8 son ≈369 batches/época; diez épocas
>    proyectan ≈758 s de train. La validación observó 31 batches/5,1 s; repetida diez veces suma
>    ≈51 s. El overhead del job fue ≈149 s (190 s Slurm menos 40,8 s del script). La suma da un
>    punto central cercano a 16 min; aplicar margen 2–3× produce una ventana operativa prudente
>    de **30–45 min**. I/O, contención y variación del nodo pueden cambiarla, por eso se mantiene
>    `1 GPU / 10 CPU / 60 GB / 2 h`. `sbatch --test-only` aceptó ese pedido en `ivb`/`multi` y,
>    con la cola observada, proyectó inicio 2026-08-18: es una estimación del scheduler, no una
>    reserva ni promesa. El full deberá medir y registrar su costo real. Los **60 GB solicitados**
>    son el pedido Slurm dentro del nodo históricamente descrito con 64 GB; no son magnitudes
>    contradictorias.
> 6. **Puertas actuales:** `1166583` cerró el freeze/smoke técnico con 12 tensores/3.096
>    parámetros, optimizer 12/12 y serving real verde. El dual gate T-FT-026 también está
>    cerrado: `technical-smoke-ready.txt` no puede sustituir `full-authorization.json`, que exige
>    T005/023/026/030/031/032/042R, D-FT-08 aprobada y hashes. T023 quedó cerrado con snapshot
>    inmutable y verificado; siguen pendientes D-FT-08/T005, D-FT-12,
>    catálogo/evaluación T031 y baseline
>    YOLOE-26s T032. Hasta entonces
>    T-FT-043 permanece `blocked`; la negativa `RUN` sin auth terminó `exit=1`, con cero full.
>    ✎ **2026-08-15: D-FT-08/T005, D-FT-12 y D-FT-13 firmadas por el usuario.** La puerta ya
>    no espera ninguna decisión humana: restan T031 (ahora `ready`) y T032. T-FT-043 sigue
>    `blocked` y el conteo de jobs full sigue en cero.

---

## 1. Lo que se corrió

`YOLOE-26s` inicializado desde `yoloe-26s.yaml` + pesos `yoloe-26s-seg.pt`
(gotcha del doc 20 §4.1: los checkpoints son de segmentación), entrenado con
`YOLOEPETrainer` — que **borra SAVPE, pre-computa los text embeddings con
`get_text_pe(names)` y deja entrenables solo las conv finales de las ramas
`cv3`/`one2one_cv3`. **[Corregido 2026-08-14] El alcance entrenable real es de
3.096 parámetros en 12 tensores; “~400 K” era el orden de magnitud del head completo,
no de los tensores habilitados por el manifiesto.** La corrección fortalece el argumento
anti-sobreajuste. Ese alcance congela el backbone y vuelve T1 un tier de bajo riesgo, pero no
garantiza retención open-vocabulary: el head cambia, el checkpoint se fusiona con
vocabulario fijo y el freeze efectivo debe comprobarse sobre el artefacto. La adenda
del 2026-08-13 registra que el primer stack remoto no cumplió esa última condición.

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
   sobre **3.096 parámetros** —los 12 tensores `cv3`/`one2one_cv3` congelados por
   manifiesto—; “400 K” era el orden de magnitud del head completo, no del alcance
   entrenable real). El argumento anti-sobreajuste se fortalece, o
2. armar un val con `bare_head` que no sea estrato de `bench_v3` — hoy no existe:
   `bare_head` nativo solo lo trae `shel5k`, que **es** estrato. Habría que
   particionar `shel5k` y retirar esa partición de `bench_v3`, lo que rompe el
   congelamiento del bench (sha256 en `bench_v3_manifest.json`), o
3. dejar el monitor como está y **medir `bare_head` solo en el eval final** contra
   `bench_v3`, declarando que el entrenamiento corrió a ciegas en esa clase.

La 3 es la única que no toca el bench congelado. La decisión es del usuario y es
previa a correr T1 completo.

[Corregido 2026-08-14] La premisa original de la vía 2 —que `bare_head` nativo sólo
lo trae `shel5k`— resultó FALSA al auditar el corpus: `construction_site_safety`/train
aporta `bare_head` nativo (1.900 instancias en train y 408 en val de `finetuning_v1`;
ver `finetuning_v1.summary.json`). El bloqueo real de F-100.1 era la ausencia de un val
CON GARANTÍAS, sin leakage por linaje, y se resolvió por una cuarta vía: split por
grupos de `finetuning_v1`. Las tres vías anteriores quedan como registro histórico.

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

Esto es lo que había que poder responder **antes** de reservar GPU en Mendieta. No es
un plan de ejecución: es la puerta y conserva la foto del 2026-08-05. La adenda superior
registra qué puntos se cerraron y cuáles se reabrieron después del smoke remoto.

### 6.1 Ya verificado local (no hace falta el clúster para esto)

| Pieza | Estado |
|---|---|
| Árbol de entrenamiento con guards (labels canónicas, stems únicos, conteos exactos) | ✅ listo y verificado |
| Disjunción train ∩ `bench_v3` | ✅ comprobada contra el bench real: **0 intersección** |
| Loop de linear probing end-to-end | ✅ smoke verde, `rc=0` |
| Presupuesto de cómputo | ✅ **≤1 GPU-h en A30** (medido ≈1 h en 4060, cota conservadora) |
| Formatos de datos | ✅ YOLO `canonical_v2` con `data.yaml` + `image_lists`; ODVG listo para el camino T3 |
| Pesos base | ✅ `yoloe-26{s,m,l,x}-seg.pt` cacheados |

### 6.2 Faltaba verificar antes de pedir turno (foto histórica del 2026-08-05)

| Pieza | Por qué importa |
|---|---|
| **Decisión sobre F-100.1** (monitor ciego a `bare_head`) | **Bloquea.** Define si el turno se gasta entrenando algo cuya clase central no se puede monitorear. |
| **Entorno reproducible en el clúster** | Versión de ultralytics (acá 8.4.86), CUDA (Mendieta: 12.x candidato vs `torch 2.12.1+cu130` local), y si se resuelve por venv, container o módulo del sitio. Es el costo dominante según doc 20 §3.2, y para T3 (MMDetection) es el riesgo alto. |
| **Transporte de datos** | 3.723 imgs de train + el árbol de labels. Definir el mecanismo (rsync/scp/almacenamiento del sitio) y la cuota disponible. |
| **Evaluación** | No está armada: falta el puente de detecciones del modelo fine-tuneado a `bench_v3` + el GT de `machinery` del doc 94 como sonda de clase nueva. **[2026-08-14: este ítem no está cerrado ni derogado; su derogación para T1 es la propuesta D-FT-13 del doc 117, pendiente de firma.]** ✎ **[2026-08-15: D-FT-13 FIRMADA. La sonda `machinery` queda derogada para T1 — el vocabulario cerrado de D-FT-08 impide ejercitar una clase externa — y reasignada a T2/T3. Este ítem de la puerta queda cerrado; el puente de detecciones a `bench_v3` sigue siendo T-FT-031, hoy `ready`.]** |
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

✎ **2026-08-15 — una excepción ratificada a esta política, acotada y retroactiva.** La
regla *"al clúster sube solo material CC BY 4.0"* se enunció **para datos** y sigue
vigente tal cual para el payload de entrenamiento. Un **asset de modelo** no la cumplió:
`mobileclip2_b.ts` (253 MB, `NOASSERTION`, text-encoder de YOLOE) viajó dentro del bundle
r20 el 2026-08-13, dos días antes de la firma. El usuario **ratificó la excepción el
2026-08-15**, limitada a ese asset, sin redistribución, y sin relajar el criterio para
datos. Constancia y límites completos:
`e-ovrt_datasets/datasets/registry/license_registry.md`, sección `mobileclip2_b.ts`.
**Al citarla en el informe: excepción ratificada *después* del hecho, no autorización previa.**

### 6.4 Lo que no se negocia

El go/no-go pre-registrado de la Tabla 37 (ΔAP ≥ +0,05 absoluto en la clase objetivo
**o** rescate de recall <0,1 → >0,5; retención ≤10% de caída relativa; sin
degradación de latencia) sigue vigente y **no se negocia después de ver resultados**.

La retención no puede darse por garantizada para T1: aunque el backbone deba quedar
congelado, el head se ajusta y se fusiona con vocabulario fijo. D-FT-08 debe precisar qué
planes acepta el checkpoint [✎ 2026-08-15: **aprobada** — ids `[person, helmet, vest,
bare_head]` fijos y ordenados, `set_classes()` prohibido] y la baseline YOLOE-26s debe quedar congelada sobre el mismo
`bench_v3` antes de observar el resultado ajustado. Hasta ese cierre no corresponde afirmar
retención generalista ni usarla como hecho para habilitar el escalamiento.

### 6.5 F-100.3 — límite de walltime por corrida en Mendieta (limitación potencial)

✎ **2026-08-12 — precisión operativa del usuario.** En Mendieta hay que separar tres
recursos que no tienen el mismo límite:

1. **Tiempo de conexión:** no constituye la restricción; la preparación, transferencia,
   inspección y armado de jobs pueden hacerse sin consumir el walltime de entrenamiento.
2. **Tiempo de corrida:** cada job tiene un máximo de **2 días (48 h)**.
3. **Ancho de la asignación:** no está limitado a un nodo o una GPU. Se pueden solicitar
   varios nodos durante esas 48 h; por ejemplo, **8 nodos × 2 GPU = 16 GPU**. El TN de
   esta jornada es Mendieta; otros clusters o grupos de nodos no se presuponen.

El máximo de 48 h es una **limitación potencial del experimento**, no una limitación
efectiva por definición. Al cierre de cada tier se registra una de estas dos lecturas:

- **`walltime_not_binding`:** la corrida terminó normalmente, sin reducir épocas, datos,
  evaluación ni alcance por el máximo de 48 h. El informe declara la restricción y explica
  que no fue vinculante, con la duración y la asignación reales.
- **`walltime_binding`:** el scheduler interrumpió la corrida, obligó a reanudarla, impidió
  completar el schedule pre-registrado o condicionó el tier alcanzado. El informe lo
  declara como **limitación técnica de E-04**, indicando el efecto concreto.

Esto **no rehabilita** la causa "falta de tiempo del proyecto" prohibida por ADR-017. Un
walltime duro del scheduler es una condición técnica medible; el cronograma general del
proyecto es otra cosa. Para poder distinguirlas, cada job debe conservar:

- nodos y GPU solicitados y efectivamente asignados;
- partición, límite pedido y duración real;
- timestamps de inicio y cierre;
- estado y motivo de terminación de Slurm;
- último checkpoint durable;
- cantidad de reanudaciones y cualquier cambio de alcance que hayan provocado.

La proyección histórica ubicó T1 cerca de una hora en una GPU menos capaz; el envelope vigente
de 2 h se justifica con margen en la adenda, pero sólo la corrida válida permitirá clasificar
si el walltime fue vinculante. Para T3 la disponibilidad de muchos nodos evita forzar a una
GPU los recipes distribuidos, pero no elimina el walltime: el job debe guardar checkpoints
periódicos y ser reanudable antes de solicitar la corrida larga.
