# 102 — GT del lote de internet (estrato B) y rescate del piloto de julio

**Fecha:** 2026-08-06. **Insumo:** `anotacionesin-internet/` — 7 exports de CVAT que
entregó el equipo. **Salida:** 3 clips de obra real promovidos al banco con GT humano
(el banco pasa de 34 a 37) + 4 clips piloto procesados y archivados + las dos campañas
del estrato B armadas y listas para correr.

**Estado:** el paso 1 del orden del usuario (doc 95 §fila 2, "CVAT del lote de internet
→ runs/evals que surjan") queda **cumplido del lado del GT**. Faltan los runs: son
GPU y están a un comando.


> ## ⚠️ CORRECCIÓN POSTERIOR — leer antes que nada (2026-08-07, doc 108 §6)
>
> Este documento **publicó el GT original de `v06_c01`, con un episodio CR-02**
> (342.400–355.533 ms). La revisión visual en CVAT determinó que **era un error de
> anotación: la persona SÍ llevaba chaleco** (track 110, 394 cajas, corrección firmada
> con `previous_value`). **El episodio no existe.**
>
> **Qué NO cambia:** la cadena de derivación y sus verificaciones (§1.1 exports a nivel
> TASK y la regla de no aplicar `split_cvat_project.py` por reflejo, guard I2,
> `validate_clip_gt` en 0 errores), el rescate del piloto de julio (§4) y F-102.1 /
> F-102.2. Nada de eso depende del atributo corregido.
>
> **Qué SÍ cambia — cuatro afirmaciones de este doc quedan invertidas:**
>
> 1. **§2 (tabla y cierre):** `v06_c01` es **negativo**, no "1 ep CR-02". De los dos
>    episodios del lote queda **uno** (`v04_c01`), y el cálculo de censura "entra por
>    2,2 s" queda sin objeto.
> 2. **§2.1:** el escenario **P5 era correcto** y el GT no lo desmentía. La lección
>    ("los códigos `scenario` son expectativa de curación, no hechos") sobrevive por
>    `v04_c01`, pero **acá el error estuvo en la anotación, no en la curación**.
> 3. **§2.2 entera, empezando por su título:** `v06_c01` **sí salió negativo**, **sí es
>    soak** (6:09,6 ≥ 5 min) y pasó a ser **el primer y único clip soak del banco** ⇒
>    FAR/hora dejó de ser no computable. **D-90.1 no se deroga, se precisa:** con
>    0,1027 h sigue faltando dos órdenes de magnitud para las 3,0 h de la regla de 3
>    (doc 108 §6.3, doc 111 §6.3).
> 4. **§2.3 (a):** esa adjudicación pendiente se resolvió **en la dirección opuesta a la
>    que este doc anticipaba** — no era oclusión que ampliara el episodio a 24,5 s: no
>    había violación. Es el caso testigo de F-108.4 y del sesgo que el doc 112 §7.2
>    señala (sobre-declarar violaciones donde el estado no es observable).
>
> **§3 (el banco de 37):** la composición cambia — `v06_c01` pasa de positivo a negativo
> y el banco gana su primer soak. Cifras vigentes (banco 47, estrato B cerrado):
> `registry/clip_bench.md` §1 y `results/clip_bench/index.md`; procedencia en el doc 111.
>
> *(Banner agregado el 2026-08-09 — doc 113 §A1; faltaba desde la corrección.)*


---

## 1. Qué llegó, y qué NO era

Siete carpetas, cada una con un `annotations.xml`. Dos grupos distintos:

| grupo | clips | anotador | qué son |
|---|---|---|---|
| **Lote de internet** | `v04_c01`, `v06_c01`, `v10_c01` | `simon` (CVAT tasks 14/18/22) | los que se esperaban (doc 93 §2) |
| **Piloto 2026-07-18** | `video02_clip07`, `video15_clip01`, `video16_clip10`, `video16_clip14` | `pandulc` (tasks 7/2/1/3) | los primeros cuatro que se anotaron, cuando se descubrió que 12 s no alcanzan |

### 1.1 La trampa del doc 80 NO aplicó — verificado, no supuesto

El runbook (doc 93 §2 paso 2) manda pasar `split_cvat_project.py` **siempre**, porque
el export del rodaje fue a nivel PROYECTO y numera los frames en un espacio global: sin
dividir, cada clip sale `negative: true` **en silencio**.

**Estos siete son exports a nivel TASK**, uno por carpeta. Comprobado clip por clip
antes de tocar nada: existe `./meta/task` (no `./meta/project`), el `<name>` de la task
coincide con el nombre de la carpeta, y el rango de frames de las cajas arranca en 0 y
cierra en `size − 1`:

| clip | `size` | rango de frames de las cajas | `n_frames` de `info.json` |
|---|---|---|---|
| `v04_c01` | 572 | 0 … 571 | 572 ✔ |
| `v06_c01` | 11.087 | 0 … 11.086 | 11.087 ✔ |
| `v10_c01` | 1.771 | 0 … 1.770 | 1.771 ✔ |
| los 4 piloto | 360 | 0 … 359 (358 en `video16_clip10`) | — (reconstruido, §4) |

Dividir un export que ya es task-level habría sido el error simétrico. **Regla que
queda:** no aplicar `split_cvat_project.py` por reflejo — mirar si el XML trae
`meta/project` o `meta/task`. El guard I2 de `derive_clip_gt` (que compara `<size>`
contra `n_frames`) cubre la mitad del riesgo, y acá pasó limpio en los tres.

---

## 2. El GT del estrato B (los 3 del lote de internet)

Cadena estándar, sin desvíos: `corrected/` → `derive_clip_gt` (umbrales oficiales
4000/7000) → `validate_clip_gt` → `promote_clip --state gt_ready` → `build_clip_bench`.

| clip | duración | GT humano | dimensionamiento |
|---|---|---|---|
| `v04_c01` | 19,067 s | **1 ep CR-01 `3.967 → 17.967 ms`** (14,0 s, 1 sujeto) | sin avisos |
| `v06_c01` | 6:09,567 | **1 ep CR-02 `342.400 → 355.533 ms`** (13,1 s, 1 sujeto) + 35 sub-umbral | sin avisos |
| `v10_c01` | 59,033 s | **negativo** — 0 episodios, 2 sub-umbral de 233 ms (CR-01 y CR-02 en t = 49,2 s) | n/a |

`validate_clip_gt`: **0 errores** (los dos avisos que imprime son de `a_p3_c01/c02`, los
negativos intencionales del rodaje, y son previos). Contrato con el evaluador
verificado a mano: los tres cargan en `ClipGroundTruthV2` del control-plane con su
`source_id` — que es el modo de falla que la auditoría del 07-11 encontró y arregló.

**Los dos episodios son evaluables SIN censura**, y en `v06_c01` por poco: CR-02 exige
`onset + 20.000 + 3.000 + 2.000` = 367,4 s y el clip dura 369,6 s. **Entra por 2,2 s.**

### 2.1 Dos escenarios estaban mal, y el GT los corrigió

Los códigos `scenario` del lote se fijaron **antes de anotar**: eran expectativa de
curación, no hechos — D-90.1 ya lo había advertido en otro contexto. El GT humano
desmiente dos:

| clip | era | es | por qué |
|---|---|---|---|
| `v04_c01` | P8 | **P1** | P8 = "sale y vuelve a entrar" ⇒ **dos** episodios (doc 72 §4.8). El GT deja uno |
| `v06_c01` | P5 | **P2** | P5 = cumplimiento total. El GT deja un episodio CR-02 sostenido de 13,1 s |
| `v10_c01` | P5 | P5 ✔ | negativo confirmado |

Se corrigieron en el `clip.yaml` (con la expectativa previa anotada al lado, para
trazabilidad) y el GT se volvió a derivar. Dejar `v06_c01` como P5 habría metido un
clip con infracción en la columna de negativos.

### 2.2 `v06_c01` no salió negativo — y eso toca el argumento de FAR/hora

> ✎ **2026-08-07 (doc 108 §6): esta sección quedó invertida, título incluido.** El
> episodio era error de anotación ⇒ `v06_c01` **sí es negativo, sí es soak** y el banco
> pasó de 0 a 1 clip soak. Lo que sigue describe el estado previo a la corrección; el
> argumento de fondo (D-90.1) no se deroga: 0,1027 h contra 3,0 h.

Su propio `clip.yaml` decía *"el GT lo marcará `negative: true` si CVAT no deja ningún
episodio"*. Dejó uno. Consecuencia mecánica: **un clip con episodio no es un clip
negativo**, así que `v06_c01` **no cuenta como soak** (doc 57 §3.2 G1: soak = negativo
de ≥5 min) y no entra al denominador de FAR/hora. Era el único candidato del banco por
duración.

El banco queda con **0 clips soak** y 0,0522 h de clips negativos (eran 0,0358 h).
**L1 no se mueve; si acaso, se confirma:** el denominador alcanzable era el argumento
central de D-90.1 y sigue a dos órdenes de magnitud de las 3,0 h que pide la regla de 3.
Los 5:42 de cumplimiento que sí tiene `v06_c01` son evidencia para el **control de
FP** (tiempo real observado donde no debería haber alerta), no denominador.

### 2.3 Dos adjudicaciones pendientes — decisión humana, NO aplicadas

Auditoría track a track buscando el patrón F-GT1 del doc 80 (violación real partida por
`unknown` cuando el sujeto está en cuadro). Aparecieron dos casos, ninguno adjudicado:
el GT vigente es el conservador.

**(a) `v06_c01`, track 110, `has_vest` — material.** El sujeto del episodio está **en
cuadro de forma continua** desde el frame 9930 (331,0 s) hasta el 10665 (355,5 s) =
24,5 s. El anotador marcó `has_vest = unknown` **explícito** en 336 de esos frames
(9,03 s desde f9935 y 2,17 s desde f10207) y `false` en el resto. La derivación corta en
los `unknown` y deja como episodio solo los últimos 13,1 s.

> Si la revisión visual concluye que era **oclusión y no cambio de estado** (que es
> exactamente lo que se resolvió en el rodaje), el episodio pasa a `331.000 → 355.533 ms`
> y **el onset se adelanta 11,4 s**. Sigue evaluable sin censura. Requiere firma +
> rationale en `annotation.unknown_adjudications` y `apply_adjudications.py`.

**(b) `v04_c01`, track 0, `has_helmet` — cuidado con ésta.** El sujeto entra en el frame
24 y los primeros 95 frames de su presencia (3,17 s) están en `unknown` explícito; el
`false` arranca en el frame 119. Si se adjudicara `false`, **el onset caería a 800 ms y
violaría el pre-roll** `MIN_ONSET_MS = 2000`: el clip pasaría a tener aviso de
dimensionamiento y el TTFD se volvería artefacto. **La anotación conservadora es la que
conviene y además es la defendible** (material nocturno, sujeto entrando lejos).

Ninguna de las dos la decide Claude: van al equipo, con el protocolo del doc 80.

---

## 3. El banco: de 34 a 37, y qué pasa con el freeze

```
clips 37 (A: 34 · B: 3) · positivos 32 / negativos 5 / soak 0
episodios 37 — CR-01 29, CR-02 8
escenarios P1:12 P2:6 P3:2 P4:2 P5:3 P6:2 P7:4 P8:1 P9:5 (sin huecos)
duración total 1.520.403 ms (25 min 20 s) · negativa 187.867 ms (0,0522 h)
✓ banco REPORTABLE: los 37 en gt_ready
```

`build_clip_bench` regeneró `clip_bench_manifest.json` y `clip_bench.sha256`
(149 archivos, `sha256sum -c` verde). Su chequeo extra —que el
`provenance.xml_sha256` de cada GT coincida con el XML promovido— pasó: el GT que está
en el banco se derivó del XML que está en el banco.

**El punto delicado: `manifest.yaml` cambió de sha256.**

| | |
|---|---|
| antes (34 clips) | `cef5082e1eb1981c89251ba1b45d7ff044627f8aa1e428f50e0601abe64260e8` |
| ahora (37 clips) | `6b75ac6e0a8fa5c7a5802b4be1f4b9b01998ef29081180b2eef639e2facbe593` |

(Un detalle de la herramienta, ya corregido y anotado dentro del propio archivo:
**`promote_clip.py` hace round-trip del YAML y borra los comentarios** — se perdió el
bloque que registraba el retiro de `cb_b01_p7`. Se restauró a mano; por eso el sha final
es `6b75ac6e…` y no el que dejó la promoción. Revisarlo la próxima vez que se promueva.)

Ese `cef5082e…` es el que citan **las trece campañas ya corridas** (T1, T2, D1, H1, G1,
B1, R1–R6) en su `campaign.yaml`. No se rompió nada: **el manifest solo creció, las 34
filas del rodaje no cambiaron**, y el archivo con ese hash exacto sigue siendo
recuperable de git —`manifest.yaml` en el commit `f7a27fe6` de `e-ovrt_datasets`—, así
que la procedencia de esas campañas sigue siendo verificable. Queda anotado en el
registry (§Estado) y en los dos `campaign.yaml` nuevos.

---

## 4. El piloto de julio: 4 clips que no se pueden correr, y para qué sirven igual

Los cuatro `videoNN_clipMM` son de otra época: recortes de **12 s** del mismo pool de
videos, anotados el 2026-07-18 para probar el laboratorio. **Su `.mp4` ya no existe** —
se borró en el renombre a `vXX_cXX` (commit `9fdc9f9f`), junto con su pre-anotación. Sin
video no hay corrida, sin corrida no hay alerta y sin alerta no hay nada contra qué
evaluar: **no son promovibles** (y `promote_clip` los rechaza por diseño, exige `mp4` y
`preann`).

Se procesaron igual y quedan en
`datasets/processed/clip_bench/_retired/piloto_2026-07-18/` (layout del banco +
`MOTIVO.md`), con el `info.json` **reconstruido**: `n_frames` y resolución salen del XML;
`fps = 30` por los masters del lote (1920×1080 @ 30) y por la aritmética del doc 57.

**Lo que valen — y es más de lo que parecía:**

| clip | GT humano | avisos A1 |
|---|---|---|
| `video02_clip07` | 1 ep CR-02 `0 → 12.000 ms`, 1 sujeto | onset 0 ms · censura t_alert |
| `video15_clip01` | 1 ep CR-02 `0 → 12.000 ms`, **2 sujetos** | onset 0 ms · censura t_alert |
| `video16_clip10` | 1 ep CR-02 `0 → 11.933 ms`, 1 sujeto, 7 sub-umbral | onset 0 ms · censura t_alert |
| `video16_clip14` | 1 ep CR-02 `2.467 → 12.000 ms`, 1 sujeto | censura t_alert |

**F-102.1 — el gate A1 barre con los cuatro: 4/4 con el episodio censurado, 3/4 sin
pre-roll, 7 avisos en total.** Ningún recorte de 12 s del material sobrevive al
dimensionamiento. La tesis del doc 57 §6.5/§6.7 —que la duración del clip no es estética
sino el presupuesto de tiempo que las métricas necesitan para existir— pasa de apoyarse
en **un** clip con GT preliminar a apoyarse en **cuatro con GT humano**. Es el resultado
que el equipo intuyó en julio ("los videos cortos no servían"), ahora con número.

**F-102.2 — `video16_clip10` cierra dos cosas de paso.** Es el clip testigo del doc 57
(`episodio 0→11933 ms`, `TTFD = 0` por construcción) y contra el que doc 58 verificó el
gate A1, pero aquel GT era **preliminar** (pre-anotación GDINO). El GT **humano**
reproduce el mismo intervalo `0 → 11.933 ms`: **el hallazgo no era un artefacto del
pre-anotador**. Y esa coincidencia exacta valida la reconstrucción del `info.json` (358
frames a 30 fps = 11.933 ms exactos), que era el único número inferido de esta sección.

De yapa: su metadata provisional de julio (commit `52a2d6e4`) lo declaraba `scenario:
P7`, "dos personas, una infringe". El GT humano deja `subjects_in_evidence: 1` —
**P7 no se sostiene**, es P2.

---

## 5. Lo que quedó listo para correr — **corrido el mismo día, ver doc 103**

> ✎ **Esta sección describe el estado ANTES de correr** (por eso dice "nada de esto se
> ejecutó" más abajo). Las dos campañas corrieron el 2026-08-06, mismo día — y el
> resultado no es el número limpio que se esperaba: **`operacion/103`** tiene el
> hallazgo (`v06_c01`, 127 personas GT, rompe `scene` Y `subject` por densidad de
> escena). Se deja el resto de la sección como quedó escrita, de valor histórico para
> entender qué se armó y por qué.

Dos campañas armadas, misma combinación que sus referencias del rodaje y **el estrato
como única variable**:

| código | campaña | analogía | GPU |
|---|---|---|---|
| **I1** | `i1_gdinotiny560_v2short_scene_internet` | T1 (línea de base, escena) | **sí** |
| **I2** | `i2_gdinotiny560_v2short_subject_internet` | G1 (identidad, la mejor del banco) | no — reusa las detecciones de I1 |

I2 es el contraste que más interesa: si la ganancia de la identidad (F1 0,789 → 0,930 en
el rodaje) **se sostiene sobre obra real no guionada**, deja de poder explicarse por el
guion.

```bash
# 0. media-plane sirviendo con el campeón (solo para I1)
cd e-ovrt_media-plane && EOVRT_MODEL_REF=grounding-dino/gdino-tiny-560 make serve

# 1. I1 — escena (~13.400 frames; a los ~5,6 fps agregados del rodaje, ~40 min)
python3 docs/operacion/datos/102-ciclo-internet-runner.py --fase scene

# 2. I2 — sujeto (minutos, sin GPU; guard: aborta el clip si alguna persona
#    quedara sin track_id, que es como se mediría G0 creyendo medir G1)
python3 docs/operacion/datos/102-ciclo-internet-runner.py --fase subject

# 3. agregar las dos y dejar los artefactos con la convención del banco
bash docs/operacion/datos/102-cerrar-campanas-internet.sh
```

El runner es reanudable (saltea lo ya evaluado) e identifica el run del control por
diferencia de directorios, no por mtime — la trampa del doc 81 que cruzaría las alertas
de un clip con el GT de otro en silencio.

**Verificado sin GPU:** sintaxis de runner y script de cierre, existencia de
`track_detections` y del venv del control-plane, y que el evaluador carga los 3 GT.
**No verificado:** la corrida en sí (el media-plane no está levantado).

Después de correr quedan tres cosas a mano: `date` / `duration_note` / `report_doc` en
los dos `campaign.yaml`, la fila nueva en `results/clip_bench/index.md` con su desglose
(L5 / D-90.6), y el doc de campaña.

### 5.1 Cómo se leen esos números cuando salgan

- **Fila aparte, con desglose, nunca fusionada** al agregado del rodaje (D-90.6).
- **n = 2 episodios.** Es el dato de una combinación sobre un material nuevo, no una
  medición con poder estadístico. El intervalo de confianza hay que escribirlo.
- **No es recall comparable clip a clip con T1**: 3 clips contra 34, y el material
  difiere en fuente, iluminación (uno es nocturno) y densidad.
- Lo que sí aporta y nada más lo aporta: **L4** (generalización a obra real) y el
  **control de FP sobre material no guionado**.

---

## 6. Lo que sigue abierto

| # | qué | quién |
|---|---|---|
| 1 | **Correr I1/I2** — §5 | Claude, a un comando |
| 2 | **Las dos adjudicaciones** de §2.3 (`v06_c01` es la que cambia un número; `v04_c01` conviene dejarla como está) | equipo |
| 3 | **URL + fecha de acceso por video** (informe/99 §6 hallazgo 2). Sigue abierto: el mapeo `raw/N.M.mp4` → video de YouTube **no está registrado** y no se pudo recuperar por duración (los 14 son recortes; ningún match exacto contra los 16 `.info.json` de `scripts/downloads/`). Los `clip.yaml` nuevos ya traen la cláusula de licencia con `video_url: TODO` | usuario |
| 4 | Los **11 clips restantes** del lote siguen sin corregir en CVAT. Doc 93 §"Recomendación de alcance" ya los declaraba marginales: con `v06_c01` y `v04_c01` el lote cumple su función | opcional |
| 5 | Doble anotación sigue en **0,0** (objetivo ≥0,2, doc 58 §B.3) — sin cambios | declarado |

**Lo que este doc NO hace:** ningún número de campaña, porque no se corrió ninguna. Las
cifras de arriba son del GT y del banco, y salen de `clip_bench_manifest.json` y de los
`gt/*.json`, todos verificables.
