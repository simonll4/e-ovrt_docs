# 106 — Relevamiento del procesamiento de los clips nuevos, y cómo continuar

**Fecha:** 2026-08-06, cierre de la jornada. **Qué es:** el inventario verificado de
TODO lo que produjo la llegada de las anotaciones (docs 102→105) y la decisión de qué
sigue. Hermano operativo del doc 95 para este frente: **el punto 1 del orden del
usuario del 08-05 ("CVAT del lote → runs/evals que surjan") queda COMPLETO con esta
jornada.**

**Regla de verificación:** nada de lo que sigue está dicho de memoria — la batería
completa corrió al cierre (integridad lab↔banco↔freeze, `validate_clip_gt` en sus dos
modos, freeze 149/149, suite de datasets 283 verde, verificador de índices verde).


> ## ⚠️ CORRECCIÓN POSTERIOR — leer antes que nada (2026-08-07, doc 108 §6)
>
> Este inventario cierra la jornada del 08-06, cuando el GT de **`v06_c01` tenía un
> episodio CR-02**. La revisión visual determinó que **era un error de anotación** (la
> persona sí llevaba chaleco, track 110, 394 cajas). El clip es **negativo** y pasó a
> ser **el primer clip soak del banco**.
>
> **Qué NO cambia:** el inventario de artefactos verificados (§1), los 14 hallazgos
> numerados del día y la **frontera de juzgabilidad de tres ejes** (§2, párrafo final) —
> se midieron sobre las detecciones y sobre el `unknown` del anotador, que no cambiaron.
>
> **Qué SÍ cambia — la "tabla de bolsillo" del §2 quedó stale en sus dos mitades:**
> - **Nivel B:** tras la corrección el estrato tenía **1 episodio evaluable, no 2**
>   (queda `v04_c01`) ⇒ la fila "recall (2 eps)" **no es citable**.
> - **Nivel A:** el "estrato B **0,002**" se puntuó con el XML previo (doc 109 §9.3: la
>   única cifra publicada de esa jornada que estaba incorrecta).
>
> **Y el §3 ya no describe lo que está abierto:** los barridos que ofrecía se ejecutaron
> (doc 107), el lote se cerró (13/14, banco 47) y las campañas se re-corrieron en gen. 3.
> Estado vigente: doc **111**; balance del tramo: doc **112**; cifras: los índices de
> `results/`.
>
> *(Banner agregado el 2026-08-09 — doc 113 §A1; faltaba desde la corrección.)*


---

## 0. El día en una pantalla

| qué llegó | qué salió |
|---|---|
| 7 exports de CVAT (3 del lote + 4 del piloto de julio) | **Banco 34→37** (`gt_ready`, reportable), GT humano validado y promovido (doc 102) |
| — | **I1/I2 corridos** → el doble colapso y su diagnóstico por capas: la **frontera de juzgabilidad** (doc 103) |
| — | **3 ajustes probados solo con configuración**: gate re-calibrado (−32% FP, recall intacto), `base-560` refutado, escena irreparable en denso (doc 104) |
| Los 4 `.mp4` del piloto, recuperados de CVAT por el usuario | **Nivel A sobre video** — primera vez; el derrumbe confirmado con la métrica canónica y dos correcciones al propio encuadre (doc 105) |

**14 hallazgos numerados en un día**: F-102.1/2 · F-103.1/2 · F-104.1/2/3/4 ·
F-105.1/2/3/4, más D-90.1 confirmada y F-81.2(a)/F-89.1 replicadas fuera del guion.

## 1. Inventario de artefactos (verificado al cierre)

### 1.1 GT y banco

- **Banco de clips: 37 filas**, todas `gt_ready`, `manifest.yaml` sha256 `6b75ac6e…`
  (el freeze de 34 de las campañas del rodaje, `cef5082e…`, sigue en el commit
  `f7a27fe6`). Freeze 149/149 OK. `build_clip_bench` reportable.
- **Estrato B** (`v04_c01` P1 · `v06_c01` P2 · `v10_c01` P5): GT humano, 2 episodios
  evaluables sin censura, promovido completo (mp4+meta+preann+annotations+gt).
- **Piloto** (`video02_clip07`, `video15_clip01`, `video16_clip10`, `video16_clip14`):
  **completos otra vez en el laboratorio** (mp4 recuperado + `info.json` real con
  sha256 + yaml + corrected + gt). Masters CVAT en
  `datasets-videos/raw/recuperados-cvat/` (gitignorado); **hashes versionados en
  `datos/105-recuperados-procedencia.json`**. Siguen fuera del banco de Nivel B
  (censura A1); `_retired/piloto_2026-07-18/` queda como registro histórico con nota.
- **Bandeja de entrada**: `anotacionesin-internet/` archivada por el usuario en
  `_archived/` — las anotaciones están preservadas en git vía el banco y `_retired/`.

### 1.2 Corridas y resultados

| corrida | qué es | dónde |
|---|---|---|
| I1 / I2 | estrato B, tiny, scene/subject — **campañas del banco** | `results/clip_bench/{i1,i2}_…_internet/` (campaign.yaml + metrics.json + evals + provenance) |
| barrido gate | 4 umbrales × 2 granularidades — exploratorio doc 104 | `datos/104-barrido-gate/` |
| I3 / I4 | base-560, scene/subject — exploratorio doc 104 (refutado) | `datos/104-i{3,4}-base-*-clips/` |
| piloto Nivel B | 4 clips, scene/subject — censurado, por completitud | `datos/105-piloto-{scene,subject}-clips/` |
| **Nivel A clips** | piloto + estrato B, scorer oficial | `datos/105-nivel-a-{piloto,estrato-b}.json` |

### 1.3 Herramientas nuevas (todas medición/tooling, ADR-015 intacto)

| herramienta | estado |
|---|---|
| `102-ciclo-internet-runner.py` (+ `--scene-dir`) | probado 4 veces (I1/I2/I3/I4 + piloto) |
| `104-barrido-gate-runner.py` | probado |
| **`datasets/scripts/bench/score_clip_person_state.py`** | probado sobre 7 clips; **⚠ SIN TESTS propios** — es la única pieza nueva que produce números y no tiene suite (la cultura de la casa es TDD para esto: `split_cvat_project` 9 tests, `apply_adjudications` 10) |
| `103-diagnostico-juzgabilidad.py`, `103-gate-sim.py` | diagnósticos, congelados como evidencia |

### 1.4 Dónde quedó escrito qué

- **Docs**: 102 (GT) · 103 (hallazgo + diagnóstico §7) · 104 (ajustes) · 105 (Nivel A)
  — indexados en `00-indice.md`.
- **Índices de resultados**: `clip_bench/index.md` (sección estrato B + tabla de
  ajustes + advertencias F-104.x) · `bench_nivel_a/index.md` (sección nueva "Nivel A
  sobre clips") · `results/index.md` (L4 anotada). Verificador mecánico: **verde**.
- **Registry**: `clip_bench.md` (37 clips, L4 parcial, L5 por bloque) ·
  `license_registry.md` (fila del lote con GT 3/14 y escenarios corregidos).
- **Memoria del proyecto** (kit): `sintesis/resultados-y-conclusiones.md` con el arco
  completo del día en el estado.

## 2. Los números que quedan (la tabla de bolsillo)

**Nivel B (alerta), estrato B** — fila aparte, jamás fusionada (D-90.6):

| | scene | subject | subject+gate 10.500 |
|---|---|---|---|
| recall (2 eps) | 0,000 | 1,000 | 1,000 |
| precision | 0,000 | 0,010 | 0,015 |

**Nivel A (persona), CR-02 F1**: imágenes 0,41–0,55 → piloto **0,154** → estrato B
**0,002**. Cae la precision; el recall (~0,33) se sostiene.

> ✎ **Esta tabla de bolsillo NO es citable (2026-08-07, doc 108 §6).** Se armó con
> `v06_c01` como positivo: tras la corrección el estrato tenía 1 episodio evaluable (no
> los 2 del recall) y la celda de Nivel A se puntuó con el XML previo. La lectura
> cualitativa —cae la precision, el recall se sostiene— es la que sobrevivió a la gen. 3.
> Cifras vigentes: `results/clip_bench/index.md` y `results/bench_nivel_a/index.md`.

**La frontera de juzgabilidad tiene tres ejes medidos**: escala (asociación de vest
96–100% a ≥320 px diurno vs 0–17% bajo 160 px) × iluminación (nocturno 55% incluso
grande; insensible al gate y al modelo) × **oclusión** (sujetos de 370 px con 58,5% de
solape → F1 0,084). Y **no hay índice escalar barato que la prediga** (F-105.4): la
brecha humano/modelo es el contexto temporal.

## 3. Qué está abierto — con dueño

### Míos, baratos, listos para disparar (los 3 barridos ya ofrecidos + 2 nuevos)

> ✎ **EJECUTADOS los 5 la misma noche — resultados en el doc `operacion/107`.**
> Titulares: `min_subject_confidence` 0,50 = la mejor palanca individual (FP −48%,
> recall intacto, F-107.1); `min_absent_class_confidence` NO accionable (F-107.2, y
> midió el acople alucinación↔supresión); persistencia 12 s = −32% FP a costo t_alert
> 8,4→15,7 s (F-107.3); taxonomía de mecanismos satura en clips largos (F-107.4,
> columnas I1/I2 agregadas al índice con nota); tests del scorer: 8, suite 291 verde.
> **La celda combinada NO se corrió** (sobre-ajuste in-sample) — queda como validación
> out-of-sample si llega material nuevo. Con esto, §4.1 queda cumplido.

| # | experimento | qué cierra | costo |
|---|---|---|---|
| ~~1~~ | ~~Barrido `min_subject_confidence` (0,35→0,5)~~ | **HECHO — F-107.1** | — |
| ~~2~~ | ~~Barrido `min_absent_class_confidence` (0,25→↓)~~ | **HECHO — F-107.2** (no accionable) | — |
| ~~3~~ | ~~Barrido `confirm_after_ms` CR-02 (7→10–12 s)~~ | **HECHO — F-107.3** | — |
| ~~4~~ | ~~Clasificación de mecanismo de FP~~ | **HECHO — F-107.4** | — |
| ~~5~~ | ~~**Tests para `score_clip_person_state.py`**~~ | **HECHO** — 8 tests, 291 verdes | — |

### Del equipo / del usuario

| # | qué | consecuencia |
|---|---|---|
| 6 | Adjudicación del hueco `unknown` de `v06_c01` (doc 102 §2.3) | adelanta el onset 11,4 s ⇒ el t_alert del match pasa de 8,4 s a ~19,8 s, **al borde de la ventana de 20 s** — decidir sabiendo eso; la de `v04_c01` conviene NO tocarla |
| 7 | URL + fecha de acceso por video del lote (informe/99 §6) | evidencia perecedera; los yaml ya tienen la cláusula con `video_url: TODO` |
| 8 | Anotar más clips — solo si se quiere reforzar un eje: `v04_c02/c03` (nocturno, ~60 s) o densidad intermedia (elegir con escaneo GT-free de los 11) | opcional; doc 93 los daba marginales y sigue válido |
| 9 | Decisiones de encuadre para el informe: nombre de la limitación (¿nueva o L4/L6 ampliada?), los 3 ejes, F-105.4 como trabajo futuro principal | van al pase de redlines |

### Lo que NO está abierto (para no re-litigar)

FAR/hora (D-90.1 confirmada) · re-rodar EBE (doc 101) · `hyb_and` (D-90.4) · promover
el gate como config de producción (calibración in-sample declarada) · fusionar estrato
B con el agregado del rodaje (D-90.6) · el modo escena en escenas densas (F-104.2).

## 4. Cómo continuar — el orden recomendado

1. **(opcional, una tarde)** Los ítems 1–5 de arriba. Cierran la matriz de knobs y la
   deuda de tests. Es lo único que este frente tiene pendiente de MI lado.
2. **Retomar TU orden del 08-05**: el paso 1 está completo → siguen los **videos
   V1–V3 de la defensa** (V2 pendiente — el intento con `gloves` era falso) →
   **recién ahí** la redacción §17.x + regenerar `informe-project-kit`.
3. Cuando el kit se regenere, **los docs 102–105 aportan material nuevo al inventario
   de `informe/99`**: la curva de asociación por altura (figura candidata), la tabla
   del barrido del gate, la comparación Nivel A imágenes/video, y los hallazgos
   F-102.1→F-105.4 para el capítulo de limitaciones y trabajo futuro. **No tocar el
   kit antes** (orden del 08-05).

## 5. Deuda git (foto al cierre, sin acción — la maneja el usuario)

| repo | estado |
|---|---|
| `docs` | docs 102–106 + datos/10{2,3,4,5}-* + índice + sintesis + informe/99 ✎ + operacion/93/95/98 ✎ — sin commitear |
| `e-ovrt_datasets` | banco 37 (manifest+freeze+gt+annotations+meta), registry ×2, `score_clip_person_state.py`, 7 clip.yaml del lab, README ✎, `_retired/piloto` — sin commitear |
| `e-ovrt_experimental-setup` | `results/clip_bench/{i1,i2}` nuevos + 3 índices tocados — sin commitear |
| `e-ovrt_control-plane` / `e-ovrt_media-plane` | **sin cambios** (todo lo probado fue config efímera en `datos/`) |

GPU libre, ningún servicio colgado, scratchpad limpio de fixtures.
