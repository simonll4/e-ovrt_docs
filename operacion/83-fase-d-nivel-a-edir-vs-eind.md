# 83 — Fase D, Fase 1 (Nivel A): E-DIR vs E-IND sobre el bench de imágenes

- **Fecha:** 2026-08-03 (noche, misma jornada que los docs 80/81).
- **Qué es:** la primera ejecución del **gate pre-registrado** de la Fase D
  (`nucleo/04` §7 Fase 1 / §8): puntuar el estado "sin EPP" **a nivel persona** con
  los dos prompt sets congelados (`eind_v1` / `edir_v1`, doc 76), con umbrales
  calibrados en la mitad A del bench y todo lo reportado saliendo de la mitad B.
- **Estado:** **completo**. 18/18 corridas de inferencia sin errores (~60 min de GPU),
  los dos estratos puntuados. **Sin commitear.**

> **Marco de lectura (doc 81 §1, vigente).** Los números de abajo son el rendimiento
> medido de combinaciones concretas, no una nota. Que E-DIR quede lejos de E-IND en
> CR-01 **es el dato** que el eje de la tesis fue a buscar, no un fracaso.

---

## 1. Tres hallazgos que cambiaron el plan antes de correr nada

El doc 82 daba la Fase D por "lista para correr una campaña". La verificación previa
encontró que no lo estaba, por tres motivos independientes.

### F-83.1 — El atajo del pre-registro no era usable
`nucleo/04` §7 paso 7 autoriza reusar las corridas de Sprint 2 como brazo E-IND "sin
re-inferir". **Las 28 corridas de bench en disco usaron `cr01_cr02_bench_v2`, que
tiene 4 clases** — incluye `bare_head`. Y el adapter arma **un solo caption**
(`grounding_dino_adapter.py:121`, `text = ". ".join(plan.texts()) + "."`), así que
esas corridas vieron `"person. helmet. vest. bare head."` mientras `eind_v1` declara
solo las tres primeras. Peor: en ese set `bare_head` está declarado con
`strategy: observable_state`, **el mismo eje que `cr01_obs` de E-DIR**. Reusarlas
habría metido un prompt de la familia E-DIR dentro del brazo E-IND, rompiendo la
regla de variable única (§17.3.6.5). **Se re-infirió E-IND con `eind_v1` limpio.**

### F-83.2 — CR-02 no tenía GT a nivel persona (y el gate no podía evaluarse)
La Fase 1 puntúa contra `has_helmet`/`has_vest`. `has_vest` **no existía**:

| | personas | sin casco | sin chaleco |
|---|---|---|---|
| `person_gt_bench_obra` | 262 | 60 | **0** |
| `person_gt_shel5k` | 20.015 | 5.248 | **campo ausente** |

No daba cero por medición: `has_vest=True` era un **placeholder declarado**
(`note_cr02`: *"NO-Safety Vest no es clase canonical_v2"*) y SHEL5K no anota chaleco.
Con CR-02 inmedible, el gate del §8 (*"F1 de E-DIR < 50% del de E-IND en **ambas**
condiciones"*) no podía dispararse nunca: E-DIR pasaba a Fase 2 por defecto, sin que
nadie lo hubiera decidido.

### F-83.3 — La vía obvia para arreglarlo era circular; la válida estaba en el raw
La tentación era derivar `has_vest` del estrato **CHV** (3.887 `person` + 1.784
`vest` a nivel caja): "ninguna caja `vest` cae dentro de la persona" ⇒ sin chaleco.
Daba n grande y números plausibles (54,6% sin chaleco, contra 12,9% sin casco como
control). **Es circular**: esa es exactamente la operación de `spatial_absence`, o
sea la de E-IND. Construir el GT con la lógica de E-IND y después usarlo para
comparar E-DIR contra E-IND le regala la comparación a E-IND, justo en el eje
central de la tesis. Es además lo que `build_person_gt.py` prohíbe explícitamente
en su docstring (anti-circularidad **D10**).

La vía válida estaba donde el propio `note_cr02` apuntaba (*"ver raw annotations"*):
`construction_site_safety` tiene **`NO-Safety Vest` como clase negativa explícita**
(índice 4), marcada por un humano; solo se pierde al mapear a `canonical_v2`. En las
147 imágenes curadas de `bench_obra` hay **147 anotaciones `NO-Safety Vest`** (en 56
imágenes). Se recuperan y se hacen pasar por la maquinaria que `build_person_gt.py`
ya tenía para `no_vest`.

**Resultado**: `person_gt_bench_obra_v2.json` — 262 personas, **60 sin casco (idéntico
al builder vigente, sin regresión) y 142 sin chaleco**.

#### Sub-hallazgo: atribución 1:1 de los negativos
La primera versión daba **148 violadores contra 147 negativos**: 15 cajas
`NO-Safety Vest` caen dentro de **dos** personas superpuestas y el matching las
marcaba a las dos. Hasta un 10% de la clase positiva de CR-02 habría sido gente que
sí llevaba chaleco, marcada por la caja del vecino — contaminación justo donde se
mide precision. Cada negativo se atribuye ahora a **una sola** persona (la que mejor
lo contiene; ante contención total, la de menor área) y las 27 personas candidatas
en casos ambiguos quedan marcadas con `vest_attribution_ambiguous` para poder
reportar CR-02 con y sin ellas.

---

## 2. Qué se corrió

| Componente | Valor |
|---|---|
| Modelo | `grounding-dino/gdino-tiny-560` (campeón S1/S2, doc 64), `box_threshold` 0.30 |
| Brazo E-IND | `eind_v1` congelado (`7a0126f4…`), 3 clases en UN caption (su forma desplegada) |
| Brazo E-DIR | `edir_v1` congelado (`a1278d0c…`), 6 formulaciones, **una corrida por variante** |
| Regiones | las del pattern set desplegado `cr01_cr02_v2` (upper_body 0–0.45 / torso 0.25–0.85) |
| Partición | mitades A/B estratificadas por presencia de violador, semilla 20260803 |
| Calibración | grid de umbrales **idéntico para ambos brazos**, solo en la mitad A |
| Reporte | solo mitad B, con IC95 bootstrap por remuestreo de **imágenes** |

**Las 6 variantes E-DIR corren aisladas** (una frase por caption). Con las seis
juntas, el phrase grounding tendría que atribuir cajas entre frases que comparten
casi todo el vocabulario, y el resultado mediría formulación **+ amontonamiento**.
Aislarlas mide la formulación; el caveat de régimen asimétrico frente a E-IND (que
corre con sus 3 clases juntas, su forma desplegada) queda declarado acá.

Los dos `diagnostic_template` (`enabled_by_default: false`) no entran: son sondas del
eje de presencia, no candidatas a evidencia de ausencia.

### Trampa de calibración que mordió
Con el grid cortado en 0.50 (E-IND) y 0.60 (E-DIR), **los dos brazos elegían su valor
máximo**: el óptimo estaba en el borde y la comparación medía el techo del grid, no
la estrategia. Los grids se ampliaron hasta 0.80/0.85 y se re-puntuó. Ningún brazo
toca el borde ahora. Re-puntuar es CPU y segundos: las detecciones quedan en disco.

---

## 3. Resultados — estrato `bench_obra` (147 imgs, 74 en la mitad B)

### CR-01 (casco) — 28 personas violadoras en la mitad B

| Brazo | P | R | F1 | IC95 recall | TP | FP | FN | umbral |
|---|---|---|---|---|---|---|---|---|
| **E-IND** | 0,476 | 0,357 | **0,408** | [0,179–0,556] | 10 | 11 | 18 | p0,60 / e0,35 |
| `cr01_spec` | 0,200 | 0,179 | 0,189 | [0,043–0,370] | 5 | 20 | 23 | 0,70 |
| `cr01_neg` | 0,160 | 0,143 | 0,151 | [0,028–0,333] | 4 | 21 | 24 | 0,60 |
| `cr01_obs` | 0,097 | 0,250 | 0,140 | [0,100–0,471] | 7 | 65 | 21 | 0,45 |

### CR-02 (chaleco) — 82 personas violadoras en la mitad B

| Brazo | P | R | F1 | IC95 recall | TP | FP | FN | umbral |
|---|---|---|---|---|---|---|---|---|
| **E-IND** | 0,567 | 0,415 | **0,479** | [0,243–0,644] | 34 | 26 | 48 | p0,60 / e0,70 |
| `cr02_obs` | 0,434 | 0,402 | 0,418 | [0,259–0,592] | 33 | 43 | 49 | 0,40 |
| `cr02_neg` | 0,359 | 0,451 | 0,400 | [0,311–0,646] | 37 | 66 | 45 | 0,30 |
| `cr02_spec` | 0,298 | 0,341 | 0,318 | [0,220–0,568] | 28 | 66 | 54 | 0,40 |

---

## 3 bis. Resultados — estrato `shel5k` (5.000 imgs, 2.500 en la mitad B)

Es el estrato que **cierra CR-01**: 2.487 personas violadoras en la mitad de test,
contra 28 en `bench_obra`.

| Brazo | P | R | F1 | IC95 recall | TP | FP | FN | umbral |
|---|---|---|---|---|---|---|---|---|
| **E-IND** | 0,464 | 0,662 | **0,546** | **[0,628–0,697]** | 1647 | 1899 | 840 | p0,35 / e0,35 |
| `cr01_obs` | 0,119 | 0,445 | 0,188 | **[0,420–0,472]** | 1107 | 8212 | 1380 | 0,35 |
| `cr01_spec` | 0,061 | 0,234 | 0,097 | [0,215–0,255] | 583 | 8944 | 1904 | 0,30 |
| `cr01_neg` | 0,083 | 0,232 | 0,123 | [0,211–0,255] | 578 | 6351 | 1909 | 0,30 |

**Los IC95 de E-IND y del mejor E-DIR no se solapan** ([0,628–0,697] vs
[0,420–0,472]). Con este n, la diferencia en CR-01 no es ruido.

## 3 ter. El gate del §8

| Estrato / condición | F1 E-IND | mejor E-DIR | F1 | ratio | ¿< 50%? |
|---|---|---|---|---|---|
| `bench_obra` / CR-01 | 0,408 | `cr01_spec` | 0,189 | 0,46 | **sí** |
| `shel5k` / CR-01 | 0,546 | `cr01_obs` | 0,188 | **0,34** | **sí** |
| `bench_obra` / CR-02 | 0,479 | `cr02_obs` | 0,418 | **0,87** | no |

**El gate NO se dispara. E-DIR pasa a la Fase 2.** El criterio exige estar por debajo
del 50% **en ambas condiciones**: CR-01 lo cumple en los dos estratos independientes
(0,46 y 0,34) pero CR-02 está en 0,87. La decisión pre-registrada no se re-litiga por
el resultado.

### Complementariedad (predicción pre-registrada: >15% ⇒ margen para E-HYB)

| Estrato / condición | E-IND falla | mejor E-DIR falla | recupera | fracción |
|---|---|---|---|---|
| `bench_obra` / CR-01 | 18 | 23 | 1 | 5,6% |
| `shel5k` / CR-01 | 840 | 1380 | **155** | **18,5%** |
| `bench_obra` / CR-02 | 48 | 49 | 9 | **18,8%** |

Con n adecuado la predicción queda **contrastada en las dos condiciones**. El 5,6% de
`bench_obra`/CR-01 se explica por su n (18 fallos): el mismo experimento con 840
fallos da 18,5%.

---

## 3 quater. E-HYB Fase 1 offline (doc 12 §4 — dual-run, sin inferencia nueva)

El pre-registro manda correr la fusión de Fase 1 sobre las corridas ya hechas
(§6.2: *"Fase 1 E-HYB offline (gratis)"*). Sin parámetros libres propios: hereda los
umbrales calibrados en la mitad A de cada brazo; gating por persona (§4.2) con el
mismo IoU 0,5. La variante que entra a la fusión se elige por F1 **de calibración**
(mitad A), no de test.

**Diagnóstico previo — dónde caen los FP de E-DIR** (shel5k, mitad B, umbrales
calibrados): los FP de `cr01_obs` son **54% ceguera al atributo** (la frase dispara
sobre personas CON casco — el gating no filtra eso) y 46% alucinación sin persona
(eso sí lo filtra: el gating descarta el 40% de sus predicciones). Los FP de E-IND
son 44%/56%.

### E-HYB-or (unión gateada) — mitad B

| Corte | E-IND F1 | variante F1 | **E-HYB-or F1** | ΔR vs E-IND | ΔP vs E-IND |
|---|---|---|---|---|---|
| `bench_obra`/CR-01 (`cr01_obs`) | 0,408 | 0,140 | 0,293 | +0,036 | −0,242 |
| `bench_obra`/CR-02 (`cr02_obs`) | 0,479 | 0,418 | **0,473** | +0,012 | −0,037 |
| `shel5k`/CR-01 (`cr01_obs`) | 0,546 | 0,188 | 0,333 | +0,022 | −0,244 |

La predicción registrada (*"sube recall, baja precisión"*) se confirma con el signo
exacto: el recall sube poco (+0,01–0,04) y la precisión paga mucho. **-or no supera a
E-IND en ningún corte de Nivel A** — aunque en CR-02 queda a 0,006, prácticamente
empate. La adopción se decide igual en Fase 2 (§8.3 es sobre F1 de **alertas**, y la
histéresis temporal filtra parte del ruido extra — F-81.1 ya mostró que el motor
rescata señal intermitente).

### La parte de -and medible en Fase 1: ¿a quién corrobora E-DIR?

-and no cambia el estado por persona (E-IND es la señal primaria; su efecto — acelerar
la confirmación — se ve recién en Nivel B). Lo que sí se mide: la tasa de
corroboración sobre los TP vs los FP de E-IND.

| Corte | TPs corroborados | FPs corroborados | ¿Discrimina? |
|---|---|---|---|
| `shel5k`/CR-01 | **58%** (956/1647) | **24%** (463/1899) | **sí, 2,4×** |
| `bench_obra`/CR-01 | 50% (5/10) | 64% (7/11) | invertido (n mínimo) |
| `bench_obra`/CR-02 | 71% (24/34) | **88%** (23/26) | **invertido** |

**F-83.7 — la corroboración discrimina en CR-01.** En casco con n grande E-DIR
corrobora a los aciertos 2,4 veces más que a los errores: acelerar la confirmación por
corroboración es seguro para CR-01. **Replicado y reforzado con `gdino-base-560`
(3,0×: 51% vs 17%, doc 84)** — es un efecto del método de fusión, no del modelo.

> **✎ Corrección 2026-08-04 (réplica base-560, doc 84).** La primera versión de este
> hallazgo afirmaba además que *"la corroboración se invierte en CR-02"* (71% TP vs
> 88% FP) y de ahí derivaba que el `corroboration_factor` **tenía** que ser por
> condición. **Esa parte no replicó**: con `gdino-base-560` la dirección en CR-02 es
> la correcta (50% TP vs 36% FP). La inversión se midió sobre 34 TP y 26 FP de un
> solo estrato — n insuficiente, exactamente el límite que este mismo doc declara en
> §4. Lo que queda en pie: la discriminación de CR-01 (replicada con n grande) y que
> **CR-02 no tiene evidencia concluyente en ninguna dirección**. La recomendación
> correcta no es "apagar -and en CR-02" sino **medir la corroboración por condición
> antes de fijar el factor**, porque hoy CR-02 no está determinado.

---

## 4. Lectura — y hasta dónde llega

- **La asimetría CR-01 / CR-02 es el hallazgo.** E-DIR queda en 0,34–0,46 del F1 de
  E-IND en casco (dos estratos independientes) y en 0,87 en chaleco. Es coherente con
  el caveat C1 del acta (doc 76): la debilidad del text encoder con la negación **es
  la hipótesis del eje**, no un defecto del set. En chaleco, donde la evidencia
  positiva (`vest`) es la más débil de la plataforma (F-81.1: SDR 0,16), la
  formulación directa casi alcanza a la inferencia espacial. **La formulación en
  lenguaje mueve el rendimiento, y cuánto lo mueve depende de la condición.**
- **El eje que gana cambia según la condición.** En casco `specificity` en
  `bench_obra` y `observable_state` en `shel5k` (ambos ≈0,19); en chaleco gana
  `observable_state` ("person without bright colored safety clothing"). **La negación
  sintáctica pura no gana en ninguna** — es el eje más débil de los tres.
- **E-DIR no es un detector, pero sí un recuperador.** `cr01_obs` en `shel5k` tiene
  recall 0,445 con precision 0,119 (8.212 FP): como estrategia sola es inviable, y aun
  así **recupera el 18,5% de lo que E-IND no ve**. Ese es exactamente el argumento
  de E-HYB, ahora medido en vez de supuesto.
- **El costo de E-DIR es precision, no recall.** En los tres cortes su recall es
  comparable o mayor al de E-IND en el mismo umbral calibrado; lo que se derrumba es
  la precision (0,06–0,43). Dispara mucho y acierta poco.

**Hasta dónde llegan estos números.** CR-01 está cerrado: los IC95 de `shel5k` **no se
solapan** (E-IND [0,628–0,697] vs `cr01_obs` [0,420–0,472]) sobre 2.487 positivos, y
los dos estratos coinciden en dirección y magnitud. **CR-02 no está cerrado**: vive
solo en `bench_obra`, con 82 positivos y IC que **sí se solapan** (E-IND [0,243–0,644]
vs `cr02_neg` [0,311–0,646]). Que el ratio de CR-02 sea 0,87 alcanza para que el gate
no se dispare —el criterio es un umbral, no una prueba de significancia— pero **no
alcanza para afirmar que E-DIR y E-IND empatan en chaleco**. Cerrar CR-02 requiere
otra fuente con negativos de chaleco explícitos; hoy no la hay en el bench.

---

## 5. Qué quedó construido

| Artefacto | Qué es |
|---|---|
| `datasets/scripts/bench/person_gt_cr02.py` | GT de CR-02 a nivel persona desde negativos explícitos del raw + atribución 1:1 |
| `datasets/tests/test_person_gt_cr02.py` | 19 tests, incluido el que **fija D10** (ausencia de caja `vest` positiva NO marca violación) |
| `datasets/scripts/bench/score_person_state.py` | scoring de estado por persona: E-IND offline, E-DIR por variante, matching 1:1, P/R/F1, mitades A/B, bootstrap |
| `datasets/tests/test_score_person_state.py` | 27 tests |
| `datasets/scripts/bench/run_fase_d_nivel_a.py` | driver del protocolo: calibra en A, reporta en B, evalúa el gate, la complementariedad y E-HYB Fase 1 |
| `datasets/scripts/bench/fuse_ehyb.py` + `test_fuse_ehyb.py` | fusión pre-registrada (doc 12 §4): gating por persona, -or con dedupe, split de corroboración; 10 tests |
| `docs/operacion/datos/83-fase-d-nivel-a-runner.py` | runner de inferencia de los dos brazos |
| `.../curated/person_gt_bench_obra_v2.json` | 262 personas, 60 sin casco, 142 sin chaleco |

Suite de `e-ovrt_datasets`: **272 passed** (era 216; +56 tests, sin regresiones).

## 5 bis. Qué sigue (el orden lo fija el pre-registro, doc 12 §6.2)

1. **Fase 2 E-DIR = el evaluador `direct_evidence` en el control-plane** (doc 12
   §4.3: evaluador + marca de corroboración + factor de ventana, "1–2 días, firme en
   el spec 41") + pattern set E-DIR. Es el único código que falta del eje de la
   tesis. El brazo E-IND de Fase 2 **no se re-corre: es T1** — el caption de
   `eind_v1` es byte-idéntico al de `cr01_cr02_v2_short` ("person. helmet. vest."),
   así que la corrida sería la misma inferencia; se declara la equivalencia.
2. **Fase 2 fusiones** (-or directo; -and con `corroboration_factor` **por
   condición**, F-83.7).
3. **Réplica base-560** (Nivel A + T2 clips): lanzada 2026-08-04 de madrugada como
   cadena nocturna (`datos/84-cadena-base560.sh`, reanudable). Responde si la
   debilidad con la negación es de capacidad del encoder, y F-81.2b en los clips.

## 6. Trampas nuevas (además de las 6 del doc 82)

7. **Reusar corridas viejas como brazo de un experimento de prompts es casi siempre
   inválido.** El caption de GDINO se arma con TODAS las frases activas: dos corridas
   con distinto vocabulario no son comparables aunque compartan las clases que a uno
   le interesan. Chequear `prompt_set_id` del `summary.json`, no el nombre del run.
8. **Un grid de calibración cuyo óptimo cae en el borde no calibró nada.** Si el
   argmax es el valor máximo del grid, ampliarlo y re-puntuar antes de leer el
   resultado.
9. **El universo de imágenes del scoring es el estrato, no las imágenes con GT de
   persona.** Si se toman solo las que tienen personas anotadas (104 de 147 en
   `bench_obra`), las alucinaciones sobre imágenes vacías no pagan ningún costo.
10. **`run_descriptor` no guarda la variante del modelo** (dice `grounding_dino`, no
    `gdino-tiny-560`): de un run viejo no se puede saber qué pesos lo produjeron sin
    cruzar métricas contra el doc 64. Ya anotado como D-61.4 en el doc 62 §8; sigue
    abierto.
