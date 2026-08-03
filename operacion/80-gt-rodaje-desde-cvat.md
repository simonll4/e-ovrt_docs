# 80 — GT temporal del rodaje derivado desde CVAT (34 clips del Bloque A)

- **Fecha:** 2026-08-03
- **Insumo:** `rodaje-anotado/annotations.xml` — export **a nivel PROYECTO** del
  proyecto CVAT `TFG` (52 tasks, 631 tracks, 235.379 cajas, 56 MB).
- **Alcance:** SOLO los 34 clips del rodaje (`a_pN_cNN`). Los 14 clips de
  internet (`vNN_cNN`) y los 4 pilotos (`videoNN_clipNN`) quedan en el export
  pero **no se derivaron**: la pasada CVAT de internet sigue en curso.
- **Estado:** GT derivado y validado (0 errores), 34 clips promovidos al banco.
  **Sin commitear.**

---

## 1. Resultado

| | |
|---|---|
| Clips con GT | **34 / 34** (`datasets-videos/gt/`) |
| Validación | `✓ validate_clip_gt: 0 error(es)` |
| Episodios | **41** — CR-01: 32, CR-02: 9 |
| Negativos | 4 (`a_p3_c01`, `a_p3_c02`, `a_p5_c01`, `a_p5_c02`) |
| Avisos de dimensionamiento (A1) | 6 |
| Promovidos al banco | 34, todos con `state: gt_ready` (derivado, no impuesto) |
| Banco total | 35 clips (los 34 + el legacy `cb_b01_p7`) |
| Cobertura de escenarios | P1–P9 completa, sin huecos |

Suite de `e-ovrt_datasets`: **197 passed**. Checksums del banco: `OK`.

## 2. Hallazgo bloqueante resuelto: el export de PROYECTO no es un export de task

CVAT exporta un **proyecto** como un único `annotations.xml` donde los tracks se
distinguen por el atributo `task_id`, pero **los frames viven en un espacio
global y continuo**: la task N empieza donde termina la N-1. `a_p1_c02`, un clip
de 1123 frames, trae sus cajas en los frames **30068–31190**.

Todo el laboratorio (`cvat_xml.parse_cvat_video_xml`, `derive_clip_gt`) asume el
contrato de un export **a nivel task**: frames 0-based respecto del clip, y
`<meta><task><size>` para el guard I2.

Alimentar el XML de proyecto directo al pipeline **falla en silencio y en
total**:

1. `root.findall("track")` mete los 631 tracks de los 52 clips en cada clip.
2. `./meta/task/size` no existe (es `./meta/project/tasks/task/size`) →
   `stop_frame = None` → **el guard I2 se desactiva sin avisar**.
3. Todas las cajas caen fuera de `[0, n_frames-1]` → `attribute_states` devuelve
   `None` en todo el timeline → **cada clip sale `negative: true`**.
4. **El guard C2 no lo atrapa**: los tracks con label `person` sí existen, así
   que la derivación no protesta.

El resultado habría sido un banco de 34 negativos falsos, con toda violación
real contada como falso positivo del modelo. No hay ninguna señal de error.

### El fix: `split_cvat_project.py` (nuevo, TDD)

`datasets/scripts/videogt/split_cvat_project.py` — etapa 2b, entre el export de
CVAT y `derive_clip_gt`. Divide el export de proyecto en un XML por task,
rebasando los frames al espacio local y emitiendo `<meta><task><size>` para que
I2 vuelva a estar activo.

```bash
python3 datasets/scripts/videogt/split_cvat_project.py \
    --xml ../rodaje-anotado/annotations.xml \
    --out-dir datasets-videos/corrected \
    --match '^a_p[0-9]+_c[0-9]+$'
```

**El offset de cada task es la suma acumulada de los `<size>` anteriores en
orden de documento.** El modelo se verificó exhaustivamente antes de usarlo:
**0 de 235.379 cajas** caen fuera de la ventana que les corresponde. El script
además valida el invariante caja por caja y **corta** si alguna se sale — si una
versión distinta de CVAT numerara de otra forma, rompe en vez de rebasar mal.

Tests: `datasets/tests/test_split_cvat_project.py`, **9 casos** (rebase,
aislamiento por task, `<size>` para I2, integración con `attribute_states`,
filtros, rechazo de export a nivel task, rechazo de cajas fuera de ventana).

### Verificación independiente de que no se cruzaron clips

- **I2 activo en los 34**: `stop_frame` coincide con `n_frames` del `.info.json`
  en 34/34 (tolerancia 1 frame). Ninguno quedó en `None`.
- **`<source>` de cada task == `<clip_id>.mp4`** en 34/34.
- **Concordancia con la ficha del rodaje** (`docs/ficha-eventos-rodaje.md`,
  registrada el 25/07, independiente de la anotación): en 27 de 34 clips los
  onsets del GT caen a menos de ~1 s de los de la ficha. Un cruce de clips sería
  imposible de reconciliar con esa coincidencia.

## 3. F-GT1 — Huecos `unknown` que parten episodios (6 clips) — **RESUELTO 2026-08-03**

**Cierre (misma fecha, tras revisión visual del usuario sobre el material de
`review/fgt1/`):** en los 6 clips el `unknown` era **oclusión, no cambio de
estado** — en P1 (c09–c12) el actor mete la cabeza detrás de una caja; en P2
(c04–c05) la caja que carga le tapa el torso. Por la imagen sola no se
determina (el `unknown` del anotador fue correcto frame a frame), pero el
estado real del mundo es "sin casco/chaleco" con certeza: continuidad temporal
+ rodaje dirigido. **Adjudicado `false` en los 6** vía
`annotation.unknown_adjudications` en cada `clip.yaml` (firmadas
`simonll4`, con rationale), aplicado con `apply_adjudications.py` y
re-derivado. Resultado real = el predicho por el sandbox: 6 clips 2→1
episodios, **rodaje 41→35** (CR-01 28, CR-02 7), **banco 42→36**, avisos de
dimensionamiento de estos clips 5→0, `validate_clip_gt` 0 errores, checksums
OK, los 6 GT del banco llevan la adjudicación auditable. La distinción
metodológica que queda declarada: el atributo por frame responde "¿qué muestra
la imagen?"; el GT del banco responde "¿cuál era el estado real?" — la
adjudicación es el puente firmado entre ambos, y nunca pisa un valor explícito
del anotador.

### Detalle original del hallazgo (previo al cierre)

En 7 clips el GT parte en **dos** episodios lo que la ficha del rodaje anotó
como **uno**. Al caracterizar el hueco caja por caja:

| Clip | Condición | Hueco | Qué hay en el hueco |
|---|---|---|---|
| `a_p1_c09` | CR-01 | 12,1–15,5 s (3,4 s) | **visible**, `has_helmet=unknown` |
| `a_p1_c10` | CR-01 | 11,1–17,0 s (5,9 s) | **visible**, `has_helmet=unknown` |
| `a_p1_c11` | CR-01 | 10,1–15,7 s (5,6 s) | **visible**, `has_helmet=unknown` |
| `a_p1_c12` | CR-01 | 10,1–15,8 s (5,7 s) | **visible**, `has_helmet=unknown` |
| `a_p2_c04` | CR-02 | 12,3–17,0 s (4,8 s) | **visible**, `has_vest=unknown` |
| `a_p2_c05` | CR-02 | 14,2–18,2 s (4,0 s) | **visible**, `has_vest=unknown` |
| `a_p1_c05` | CR-01 | 12,7–13,3 s (0,6 s) | `has_helmet=true` real (cumplimiento de 0,6 s) |
| `a_p7_c03` | CR-01 | 8,1–11,6 s | legítimo: escena multi-persona, un sujeto cumple y otros salen de cuadro |

**El caso que importa son los 6 primeros**: son clips P1/P2 de **un solo actor**,
que **no sale de cuadro** — sigue visible, con el atributo marcado `unknown`
durante 3,4–5,9 s.

La derivación hace lo correcto y lo documentado (`cvat_xml.py`: *"None = … no
evaluable — nunca fabricar violación"*). El problema es aguas abajo: el motor de
patrones ve una persona detectada de forma continua y **sostendría una sola
alerta**, mientras el GT declara dos episodios. El evaluador matchea el primero
y **el segundo se cuenta como `missed`** → recall de CR-01/CR-02 deprimido por
un artefacto de anotación, no por el sistema. Es la misma clase de falla que
F-DR9 (umbrales incompatibles con `derive_clip_gt`).

**Decisión pendiente del usuario** — solo se resuelve mirando el video:

- Si en esos tramos el casco/chaleco **sí es determinable** → corregir el
  atributo en CVAT (`unknown` → `false`) y re-derivar: el episodio se une solo.
- Si **genuinamente no es determinable** (el actor se dio vuelta, oclusión) →
  el `unknown` es correcto y hay que **declarar la limitación** al reportar
  recall, o marcar esos episodios como censurados.

Re-correr después de corregir es un comando: el pipeline es idempotente.

**Actualización (misma fecha): tooling y material de decisión listos.**
- **Indicios que apuntan a "visibilidad, no cambio de estado"** (sin reemplazar la
  mirada humana): (a) los 6 huecos están encerrados entre `false` a ambos lados,
  sin ningún `true` en medio — un cambio real de estado exigiría ponerse Y sacarse
  el EPP dentro de 3,4–5,9 s; (b) verificado en sandbox: al adjudicar `false`, el
  episodio resultante coincide con el de la ficha del rodaje (independiente,
  25/07) con Δ ≤ 0,7 s en 5 de 6 clips (2,7 s en `a_p2_c05`).
- **Material visual**: `datasets-videos/review/fgt1/` — hoja de contactos
  (3 frames antes / 9 dentro / 3 después, caja coloreada por estado) + mp4 de la
  ventana por clip, generador incluido; gitignorado (frames de personas reales).
- **Herramienta**: `datasets/scripts/videogt/apply_adjudications.py` (TDD, 10
  tests). La decisión se declara en `clip.yaml` bajo
  `annotation.unknown_adjudications` (con `decided_by` y `rationale`
  obligatorios) — NO se parchea el XML a mano: `corrected/` es gitignorado y un
  parche ahí se perdería en silencio en el próximo split. La herramienta solo
  convierte `unknown` (se niega a pisar un valor explícito del anotador), corta si
  el rango no matchea nada, y es idempotente. Flujo: split → apply → derive.
- **Efecto verificado en sandbox** (`validate_clip_gt` rc=0): cada clip 2→1
  episodios; rodaje 41→35 (CR-01 32→28, CR-02 9→7); banco completo 42→36; los
  avisos de dimensionamiento de estos 6 clips 5→0 (el tramo censurado desaparece
  al unirse el episodio). Instrucciones paso a paso: `review/fgt1/LEEME.md`.

## 4. Los 4 negativos son intencionales (no son un C2 encubierto)

`validate_clip_gt` avisa que `a_p3_c01`/`a_p3_c02` son negativos con escenario
P3, y su heurística espera negativos solo en P5/V3. **No es un defecto**: la
ficha del rodaje declara `condition: None` para los cuatro (`a_p3_c01`,
`a_p3_c02`, `a_p5_c01`, `a_p5_c02`), es decir el rodaje los filmó como
cumplimiento. GT y ficha **coinciden**. Lo que está desactualizado es la
expectativa de escenarios del validador (P3 también es negativo), no el dato.

## 5. Estado del banco de clips

`datasets/processed/clip_bench/` — 35 clips, `clip_bench_manifest.json` +
`clip_bench.sha256` escritos.

```
por escenario: P1:11 P2:5 P3:2 P4:2 P5:2 P6:2 P7:5 P8:1 P9:5   (P1–P9 completo)
positivos: 31   negativos: 4   soak: 0
episodios: CR-01 33, CR-02 9        (33 = 32 del rodaje + 1 de cb_b01_p7)
```

**Cierre del banco (2026-08-03): ✓ REPORTABLE, 34 clips.**

`cb_b01_p7` —el clip de bring-up del spec 43, único no-rodaje— fue **retirado**.
Era la única fila que disparaba el gate, y el motivo vinculante no era su estado
de GT sino la **licencia/consentimiento sin registrar**: es obra real con ~10-12
operarios identificables, y su propio `clip.yaml` lo condicionaba a registrarla
antes de usarlo en resultados reportables (spec 43 §7). Eso no se arregla con una
pasada de CVAT, así que anotarlo no habría desbloqueado nada. Se suman: GT
producido por IA (`annotator: claude-vision-preliminary`) y un GT que no
discrimina (un episodio de escena que cubre el 100% del clip, onset en 0 ms → el
TTFD colapsa a 0 por recorte). Retiro **no destructivo** a
`clip_bench/_retired/cb_b01_p7/` (layout del banco preservado, `.mp4` intacto y
todavía usable como clip de humo); motivo completo en su `MOTIVO.md`.

Composición final: **34 clips, todos `gt_ready`**, P1–P9 sin huecos,
30 positivos / 4 negativos, **35 episodios** (CR-01 28, CR-02 7), 17 min 53 s de
material. `manifest.yaml` sha256 `cef5082e…`, checksums OK.

**Limitaciones declaradas** (nuevas en `datasets/registry/clip_bench.md`, el
análogo de `bench_v3.md` para video — se declaran ANTES de reportar números):

- **L1 — sin clips soak** → FAR/hora **no computable** (doc 57 §3.2 G1 exige un
  negativo de ≥5 min; los 4 negativos suman 0,0358 h y no entran al denominador).
  Llega con el lote de internet.
- **L2 — sin doble anotación: DECISIÓN, no pendiente.** `ratio 0.0` vs objetivo
  ≥0,2 (doc 58 §B.3). **El equipo decidió el 2026-08-03 no ejecutarla**: 3
  personas y el tiempo hasta la defensa no lo admiten. Consecuencia que va al
  informe: **no hay kappa, la confiabilidad de la anotación no está
  cuantificada** — los números se leen "contra el criterio de un anotador".
  Mitigaciones parciales citables: el GT sale de pre-anotación corregida (no de
  trazado libre), las fichas del rodaje del 25/07 concuerdan dentro de ~1 s, y el
  rodaje es guionado (la identidad de los episodios no depende del anotador,
  solo sus bordes).
- **L3 — 6 episodios (17%) con bordes adjudicados** sobre tramos no observables
  (F-GT1, §3).
- **L4 — un solo bloque, material guionado**: sin obra real. La generalización no
  la mide este banco.
- **L5 — escenarios desbalanceados** (P1=11, P8=1): reportar por escenario además
  del agregado, igual que la regla de estratos de `bench_v3`.

## 6. Comandos para reproducir

```bash
cd e-ovrt_datasets
# 1. dividir el export de proyecto (solo rodaje)
python3 datasets/scripts/videogt/split_cvat_project.py \
    --xml ../rodaje-anotado/annotations.xml \
    --out-dir datasets-videos/corrected --match '^a_p[0-9]+_c[0-9]+$'
# 2. derivar GT (pattern set por default = cr01_cr02_v2, 4000/7000)
for x in datasets-videos/corrected/a_p*.xml; do id=$(basename "$x" .xml)
  python3 datasets/scripts/videogt/derive_clip_gt.py --xml "$x" \
    --clip-yaml "datasets-videos/$id.clip.yaml" \
    --info "datasets-videos/clips/$id.info.json" \
    --out "datasets-videos/gt/$id.json"; done
# 3. validar, promover, ensamblar
python3 datasets/scripts/bench/validate_clip_gt.py --gt-dir datasets-videos/gt
for y in datasets-videos/a_p*.clip.yaml; do
  python3 datasets/scripts/bench/promote_clip.py --clip-id $(basename "$y" .clip.yaml); done
python3 datasets/scripts/bench/build_clip_bench.py --allow-preliminary
```

## 7. Qué habilita esto

Con GT temporal humano en 34 clips y P1–P9 cubierto, el **tramo T→P→D** del plan
maestro (doc 62) queda desbloqueado para el material del rodaje: ya se puede
correr la evaluación de alertas (`evaluate-alerts`, 5 métricas) contra GT real,
que hasta ahora solo se había ejercitado con el `gt_preliminary` de `cb_b01_p7`.

Queda fuera y sigue esperando a CVAT: los 14 clips de internet — que son los que
aportan el **soak** y, con él, el FAR/hora.
