# 105 — Los 4 clips piloto recuperados: Nivel A sobre video, y qué mide realmente la juzgabilidad

**Fecha:** 2026-08-06. **Insumo:** los `.mp4` de los 4 clips piloto, recuperados desde
CVAT por el usuario (se habían perdido en el commit `9fdc9f9f`). **Salida:** los 4
clips vuelven a ser ejecutables, se les midió **Nivel A (estado por persona)** con el
scorer oficial contra su GT humano, y de ahí salió un resultado que **corrige y mejora
la tesis de los docs 103/104**.


> ## ⚠️ CORRECCIÓN POSTERIOR — leer antes que nada (2026-08-07, doc 108 §6)
>
> Este documento se puntuó cuando el GT de atributos de **`v06_c01` marcaba `has_vest =
> false` en el track 110**. La revisión visual determinó que **la persona SÍ llevaba
> chaleco** (394 cajas, corrección firmada). A Nivel A eso cambia **el GT contra el que
> se midió**: `v06_c01` pasa de **37 a 10** person-frames violadoras de CR-02.
>
> **Qué NO cambia — el argumento de §4 y §4.1 se sostiene tal cual.** El `unknown` del
> anotador en `v06_c01` sigue en **6,2%** y su F1 CR-02 sigue en **≈0,002**: el clip con
> el segundo `unknown` más bajo sigue teniendo el peor F1, así que **F-105.4 queda en
> pie** (la monotonía era un artefacto de mirar solo los 4 pilotos). Los tres ejes de
> F-105.2/3 y el derrumbe de precision tampoco dependen del atributo corregido.
> Salvedad honesta: esa celda ahora descansa sobre **10** violaciones, no 37.
>
> **Qué SÍ cambia — dos cifras publicadas acá estaban mal:**
> - **§4.1, fila `v06_c01`:** violadores **37 → 10**, y el recall CR-02 del clip
>   **0,108 → 0,300** (el F1 se mantiene ≈0,002 porque lo domina la precision).
> - **§6, tabla ✎ "estrato B (3)":** su columna CR-02 (0,001 / 0,108 / 0,002) se puntuó
>   con el XML previo a la corrección. **El doc 109 §9.3 la declaró "la única cifra
>   publicada de la jornada que estaba incorrecta"**, no solo desactualizada.
>
> **Cifras vigentes de Nivel A sobre video** (17 clips, gen. 3: CR-01 F1 **0,039** /
> CR-02 **0,020**): `results/bench_nivel_a/index.md` y doc 111 §6.
>
> *(Banner agregado el 2026-08-09 — doc 113 §A1; faltaba desde la corrección.)*


---

## 1. Recuperación y verificación

Los 4 `.mp4` llegaron a `videos-recuperados/`. Antes de usarlos, la verificación que
importaba: **¿corresponden al GT que ya estaba derivado?**

| clip | ffprobe | reconstrucción del doc 102 | ✓ |
|---|---|---|---|
| los 4 | 1920×1080, **30 fps**, **360 frames**, **12,000 s** | 1920×1080, 30 fps, 360 frames, 12.000 ms | **exacto** |

Pasaron por `prepare_clip.sh` (etapa 0), que emitió `info.json` **reales con sha256
verificable**. Y el cierre: al re-derivar el GT con el `info.json` real, los episodios,
los sub-umbral y la duración salieron **idénticos** a los derivados con el `info.json`
reconstruido, en los 4 clips.

> **F-105.1 — la reconstrucción del doc 102 §4 queda validada por vía directa.** El
> `fps = 30` era el único número inferido de aquella sección (por los masters del lote
> y por la aritmética de doc 57: 358 frames → 11.933 ms). El archivo real confirma los
> tres campos. El GT que se derivó sin video era correcto.

Los 4 volvieron al laboratorio (`datasets-videos/`) con su `clip.yaml` actualizado: ya
no dicen "PERDIDO / no ejecutable".

## 2. Por qué Nivel A y no Nivel B

**Nivel B (alerta) no los puede medir**: sus 4 episodios están **censurados por el gate
A1** — 12 s no cubren `onset + t_alert_upper + resolve + cola` (25 s para CR-02), y 3 de
4 tienen el onset en `t=0` (F-102.1). Se corrieron igual, por completitud
(`datos/105-piloto-{scene,subject}-clips`), pero no producen recall citable.

**Nivel A sí**: mide, por persona y por frame, si el sistema determina bien el estado —
y **no depende de la duración del clip**. Es exactamente la capa que el doc 103 §7
identificó como raíz del problema del estrato B, medida hasta ahora con un proxy
ad-hoc (centro-en-caja). Acá se mide con el **scorer oficial** y las **mismas regiones
del pattern set desplegado**.

Herramienta nueva: `datasets/scripts/bench/score_clip_person_state.py` — hermano de
`run_fase_d_nivel_a.py` (que puntúa imágenes) para clips. Es **tooling de medición, no
capacidad de plataforma**: sigue el precedente de `build_person_gt_shel5k.py` y ADR-015
no lo alcanza. Tres decisiones metodológicas, todas explícitas en su salida:

1. **`unknown` se EXCLUYE del denominador.** Contarlo como `True` inventaría
   cumplimiento; como `False`, violaciones. Es el principio de `derive_clip_gt` y el
   que el runtime no tiene (F-104.4). **El ratio de exclusión se reporta — y resultó
   ser el hallazgo.**
2. **Sub-muestreo temporal** 1 de cada 15 frames (2 Hz): frames contiguos son casi
   idénticos y puntuar los 360 inflaría `n`.
3. **Sin barrido de umbrales**: se puntúa en el **punto de operación desplegado**
   (`person ≥ 0,35`, `evidencia ≥ 0,25`, los valores del pattern set). Con 4 clips,
   barrer sería ajuste in-sample.

## 3. Resultados

`gdino-tiny-560`, prompt set congelado, E-IND, punto de operación desplegado.

| clip | cond | n eval | unknown | violadores | TP | FP | FN | P | R | F1 |
|---|---|---|---|---|---|---|---|---|---|---|
| `video02_clip07` | CR-01 | 256 | 23,8% | 0 | 0 | 110 | 0 | 0,000 | — | 0,000 |
| | CR-02 | 263 | 21,7% | 24 | 8 | 159 | 16 | 0,048 | 0,333 | 0,084 |
| `video15_clip01` | CR-01 | 93 | 3,1% | 0 | 0 | 15 | 0 | 0,000 | — | 0,000 |
| | **CR-02** | 96 | **0,0%** | 49 | 24 | 53 | 25 | **0,312** | **0,490** | **0,381** |
| `video16_clip10` | CR-01 | 185 | 19,6% | 3 | 1 | 22 | 2 | 0,043 | 0,333 | 0,077 |
| | CR-02 | 185 | 19,6% | 26 | 3 | 46 | 23 | 0,061 | 0,115 | 0,080 |
| `video16_clip14` | CR-01 | 172 | 10,9% | 0 | 0 | 43 | 0 | 0,000 | — | 0,000 |
| | CR-02 | 135 | 30,0% | 21 | 4 | 88 | 17 | 0,043 | 0,190 | 0,071 |
| **AGREGADO** | **CR-01** | 706 | 17,4% | 3 | 1 | **190** | 2 | 0,005 | 0,333 | 0,010 |
| **AGREGADO** | **CR-02** | 679 | 20,6% | 120 | 39 | **346** | 81 | 0,101 | 0,325 | 0,154 |

**Contra la referencia del bench de imágenes** (Nivel A, E-IND, mismo modelo y mismas
regiones — `results/bench_nivel_a/index.md`):

| material | P | R | F1 |
|---|---|---|---|
| `bench_obra` (imágenes) | 0,476 | 0,357 | **0,408** |
| `shel5k` (imágenes) | 0,464 | 0,662 | **0,546** |
| **clips piloto, CR-02** | 0,101 | 0,325 | **0,154** |
| **clips piloto, CR-01** | 0,005 | 0,333 | **0,010** |

> **F-105.2 — la caída del estrato B queda confirmada a nivel PERSONA, con el scorer
> oficial.** El mismo E-IND, el mismo modelo y las mismas regiones pasan de F1
> **0,41–0,55 en imágenes** a **0,15 (CR-02) y 0,01 (CR-01)** en estos clips. Ya no es
> una inferencia desde un proxy de asociación (doc 103 §7.1): es la métrica canónica de
> Nivel A. **El recall se sostiene (~0,33); lo que se derrumba es la precision** — el
> sistema declara violaciones sobre gente que cumple, que es exactamente el mecanismo
> de "ausencia de evidencia = evidencia de ausencia".

## 4. El hallazgo: el `unknown` del anotador predice el rendimiento del sistema

Ordenando los 4 clips por el ratio de `unknown` que produjo el **humano** — un número
que se calcula **sin el modelo, sin correr nada**:

| clip | personas/frame | altura mediana | % personas solapadas | **unknown (humano)** | **F1 CR-02 (sistema)** |
|---|---|---|---|---|---|
| `video15_clip01` | 4,0 | 173 px | **0,0%** | **0,0%** | **0,381** |
| `video16_clip10` | 9,5 | 178 px | 14,4% | 19,6% | 0,080 |
| `video02_clip07` | 14,0 | **370 px** | **58,5%** | 21,7% | 0,084 |
| `video16_clip14` | 8,0 | 138 px | 19,7% | **30,0%** | 0,071 |

Dentro de estos 4 clips la relación es **monótona**: a más `unknown` del humano, peor
F1 del sistema. Fue tentador leerlo como un índice de juzgabilidad medible sin modelo.
**No se sostiene: al agregar los 3 clips del estrato B con la misma métrica (§4.1), se
rompe.** Lo que sí sobrevive es otra cosa, y es lo que importa:

> **F-105.3 — la juzgabilidad NO se reduce a la escala, y esto corrige el encuadre de
> los docs 103/104.** `video02_clip07` tiene los **sujetos más grandes del conjunto**
> (370 px de mediana, por encima del umbral de ~320 px donde la asociación era 96–100%
> en el rodaje) y aun así rinde F1 0,084. La razón, verificada visualmente: es una
> cuadrilla **apiñada, con 58,5% de las personas solapadas** entre sí. Todos llevan
> chaleco; el problema es la **oclusión mutua**. La juzgabilidad tiene al menos **tres
> ejes: escala × iluminación × oclusión/apiñamiento.** El encuadre de los docs 103/104
> ("escala × iluminación") era incompleto.

### 4.1 Por qué el `unknown` del humano NO es un índice de juzgabilidad del modelo

Con los 7 clips que hoy tienen GT humano y Nivel A medido:

| clip | grupo | unknown (humano) | altura mediana | F1 CR-02 | violadores |
|---|---|---|---|---|---|
| `video15_clip01` | piloto | 0,0% | 173 px | **0,381** | 49 |
| **`v06_c01`** | estrato B | **6,2%** | 211 px | **0,002** | 37 |
| `v04_c01` | estrato B | 19,2% | 327 px | — | 0 |
| `video16_clip10` | piloto | 19,6% | 178 px | 0,080 | 26 |
| `video02_clip07` | piloto | 21,7% | 370 px | 0,084 | 24 |
| `video16_clip14` | piloto | 30,0% | 138 px | 0,071 | 21 |
| `v10_c01` | estrato B | 50,6% | 192 px | — | 0 |

> ✎ **La fila de `v06_c01` quedó stale (2026-08-07, doc 108 §6):** sus violadores son
> **10**, no 37, y su recall CR-02 es **0,300**, no 0,108 — se puntuó contra el XML
> previo a la corrección firmada. Las dos columnas que sostienen el argumento de abajo
> (`unknown` 6,2% y F1 0,002) **no cambian**.

**`v06_c01` rompe la relación**: segundo `unknown` más bajo (6,2%) y el peor F1 con
violadores reales (0,002). La monotonía era un artefacto de mirar solo los 4 pilotos.

> **F-105.4 — el `unknown` del anotador mide la juzgabilidad HUMANA, no la del modelo,
> y las dos divergen donde el humano tiene ventajas que el modelo no tiene.** En
> `v06_c01` el anotador siguió a cada persona **a lo largo de 6 minutos**: con
> continuidad temporal, cambios de ángulo y la posibilidad de mirar dos veces, pudo
> determinar el estado del 94% de las persona-frames visibles. El modelo decide
> **frame a frame, sin memoria**, y ahí fracasa. La brecha entre ambos no es ruido:
> **es la ventaja del contexto temporal**, y señala que la vía de mejora no es solo
> mejor percepción por frame sino **agregación temporal de evidencia por sujeto** —
> algo que la plataforma hoy hace para *confirmar* violaciones (`confirm_after_ms`)
> pero no para *determinar el estado*.

Esto **no invalida** la conclusión práctica de los docs 103/104 (hay una frontera de
operación y hay que declararla); la vuelve más precisa: **no existe un índice escalar
barato que la prediga**. Un criterio de emplazamiento tendría que medirse contra el
modelo, no contra un anotador.

## 5. Lo que NO se puede concluir de acá

- **No es "el sistema no sirve".** Recall ~0,33 con precision baja significa que hay
  señal; lo que falta es la capacidad de abstenerse (F-104.4).
- **CR-01 tiene 3 violadores en total** en los 4 clips: su precision (0,005) está
  dominada por los 190 FP contra un puñado de positivos. Es un número válido para
  hablar de **tasa de falsas alarmas**, no para hablar de la calidad del recall de
  CR-01, que es prácticamente inobservable con este material.

  > ✎ **Regla declarada (2026-08-09, decisión D-113.2, doc `operacion/113` §D):**
  > **48% de estos 190 FP (91) son predicciones sobre personas `unknown`** — la persona
  > sale del denominador pero su predicción sí cuenta como FP, por decisión deliberada
  > ("la alerta sobre una persona no juzgable suena igual"). No se recalculó nada: la
  > cifra 0,005/190 sigue siendo la vigente con la regla declarada. Detalle:
  > `results/bench_nivel_a/index.md`.
- **Nada de esto entra al banco de Nivel B.** Los 4 clips siguen censurados por A1 y
  no producen recall temporal citable. Su lugar es Nivel A.
- **No se re-calibró nada acá.** El punto de operación es el desplegado, a propósito.

## 6. Estado y qué queda

Artefactos: `datos/105-nivel-a-piloto.json` (por clip y agregado, con los conteos de
exclusión), `datos/105-piloto-{scene,subject}-clips` (Nivel B, censurado), y los 4
clips otra vez completos en `datasets-videos/` (mp4 + info.json real + clip.yaml +
corrected + gt). El área `_retired/piloto_2026-07-18/` queda como registro histórico;
su `MOTIVO.md` necesita una nota de que los videos volvieron.

✎ El paso 1 que este doc dejaba abierto (**Nivel A sobre el estrato B**) **se ejecutó
en la misma sesión** — es lo que produjo §4.1 y refutó la lectura del `unknown` como
índice. Resultados en `datos/105-nivel-a-estrato-b.json`:

| material | CR-01 P / R / F1 | CR-02 P / R / F1 |
|---|---|---|
| clips piloto (4) | 0,005 / 0,333 / 0,010 | 0,101 / 0,325 / **0,154** |
| **estrato B (3)** | 0,019 / **0,595** / 0,037 | 0,001 / 0,108 / **0,002** |
| `bench_obra` (imágenes, referencia) | — | 0,476 / 0,357 / **0,408** |

**El estrato B es aún peor que el piloto a nivel persona** (CR-02 F1 0,002 vs 0,154):
`v06_c01` solo genera 3.172 FP sobre 6.442 persona-frames evaluadas — **casi una falsa
violación cada dos personas observadas**. La única celda decente de todo el conjunto es
`v04_c01` CR-01 (**recall 0,714**, F1 0,223): el violador nocturno es grande y el
modelo lo encuentra — pero con 55% de `unknown` en el GT y 131 FP.

**Abierto, a decisión del equipo:**
1. Si el eje de **oclusión/apiñamiento** (F-105.3) se suma explícitamente a la
   caracterización de la frontera en el informe, junto a escala e iluminación.
2. Si **F-105.4** (agregación temporal de evidencia por sujeto para *determinar
   estado*, no solo para confirmar) se declara como la vía de trabajo futuro
   principal — es más específica que "sumar el estado `unknown`" del doc 104 y sale
   de una brecha medida contra un anotador humano.
3. Si `video15_clip01` (0% unknown, F1 0,381 — el mejor del conjunto) merece leerse
   como el **punto de referencia de "material juzgable"** no guionado.
