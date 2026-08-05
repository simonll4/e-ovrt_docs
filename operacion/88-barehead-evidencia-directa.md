# 88 — `bare_head` como evidencia directa, y el costo medido del caption

- **Fecha:** 2026-08-04.
- **Qué es:** la última palanca de percepción que quedaba sin medir a Nivel B
  (F-84.5): usar `bare_head` —la clase en la que `gdino-base-560` es especialista
  (recall 0,599 vs 0,308 de tiny, doc 64)— como **evidencia directa** de CR-01, en
  lugar de la ausencia espacial de `helmet`.
- **Estado:** 34/34 clips, 0 errores. Y salió **un segundo resultado que no se fue a
  buscar** y que responde una pregunta abierta del pre-registro.

## 1. El diseño: una inferencia, dos evaluadores

Se usa el caption de **4 clases `cr01_cr02_bench_v2`** (`person/helmet/vest/bare_head`)
a propósito: es **el mismo en el que doc 64 midió la especialidad**. Un caption
recortado a `person + bare_head` habría cambiado el régimen de detección y repetido el
error F-83.1 — el vocabulario es parte de la inferencia.

De ahí sale un bonus de diseño: ese caption trae las cuatro clases, así que de **una
sola inferencia** salen dos replays sobre las **mismas detecciones**:

| | Pattern set | Evidencia |
|---|---|---|
| **(a)** | `cr01_cr02_v2` | E-IND: ausencia espacial de `helmet` |
| **(b)** | `cr01_bare_head_v1` | `bare_head` directo, gating `region_center` |

(a) vs (b) es **variable única perfecta**: las detecciones son bit a bit las mismas,
cambia solo el evaluador. Y (a) contra T2 (mismo modelo, caption de 3 clases) **aísla
el efecto del caption**.

`bare_head` se gatea con `match: region_center`, no `person_iou`: es una detección de
**parte** (caja de cabeza), y con IoU contra el cuerpo entero no gatearía nunca. Es el
mismo criterio que `head_region` del `person_gt`.

## 2. Resultado 1 — F-88.1: el caption tiene un costo, y ahora está medido

| Campaña | Modelo | Caption | Evaluador | F1 |
|---|---|---|---|---|
| **T2** | base-560 | 3 clases | E-IND | **0,704** |
| **B1-eind** | base-560 | **4 clases** | E-IND | **0,622** |

Mismo modelo, mismo evaluador, mismo pattern set, mismo GT, mismos timings. **La única
diferencia es una palabra más en el caption** (`bare head`), y cuesta **0,082 de F1**
(recall 0,735 → 0,676; precision 0,676 → 0,575).

Esto **responde una pregunta que el pre-registro dejó abierta**. El doc 12 §4.1 dejó el
pase único de vocabulario unión como *"variante operativa condicionada: si el
sub-experimento aislado-vs-completo muestra interacción despreciable, la plataforma
puede usarlo declarando la equivalencia; si hay interacción, se declara el costo (2
pases) o se descarta"*. **La interacción no es despreciable**: agregar una sola clase
al vocabulario degrada la estrategia desplegada. Consecuencia de plataforma: el atajo
de un solo pase con vocabulario unión **no es gratis**, y la regla dual-run del
pre-registro queda validada empíricamente, no solo por argumento.

Es también la confirmación a Nivel B de F-83.1, que hasta ahora era un argumento sobre
cómo se arma el caption.

## 3. Resultado 2 — F-88.2: `bare_head` directo no supera a la ausencia espacial

Comparación **restringida a los 23 clips cuyo GT es solo CR-01** (25 episodios) — el
agregado completo penalizaría a `bare_head` por episodios CR-02 que su pattern set
estructuralmente no puede detectar:

| Campaña | recall | precision | F1 |
|---|---|---|---|
| **T1** (tiny, 3 clases, E-IND) | **0,760** | **0,704** | **0,731** |
| T2 (base, 3 clases, E-IND) | 0,640 | 0,593 | 0,615 |
| B1-eind (base, 4 clases, E-IND) | 0,640 | 0,533 | 0,582 |
| **B1 `bare_head`** (base, 4 clases, directo) | 0,480 | 0,480 | **0,480** |
| D1 (E-DIR frases) | 0,240 | 0,222 | 0,231 |
| H1 (hyb_or) | 0,200 | 0,185 | 0,192 |

**La palanca no alcanza.** Con el modelo especialista, su vocabulario nativo y el
mismo caption en el que se midió la especialidad, `bare_head` directo rinde **0,480
contra 0,582 de la ausencia espacial sobre las mismas detecciones**. F-84.5 queda
cerrada: la vía que T2 no había probado **tampoco recupera el déficit de CR-01**.

## 4. F-88.3 — La etiqueta corta es mucho mejor que la frase negada, y eso ordena el eje

`bare_head` (0,480) está **muy por encima** de las frases E-DIR (D1: 0,231) aunque las
dos sean "evidencia directa de la condición" consumidas por el mismo evaluador. La
diferencia no es el mecanismo: **es la formulación**.

| Formulación | Tipo | F1 (CR-01 puro) |
|---|---|---|
| `helmet` + ausencia espacial | etiqueta corta + inferencia | **0,582–0,731** |
| `bare head` | **etiqueta corta**, estado observable | **0,480** |
| `"construction worker without safety helmet"` | **frase negada** | 0,231 |

Es el orden que el eje de la tesis predijo y ahora está medido de punta a punta: el
detector responde bien a **etiquetas cortas de objetos y estados**, y mal a **frases
que niegan**. La ventaja de E-IND no es "inferir es mejor que detectar": es que su
vocabulario está hecho de las etiquetas cortas que el modelo entiende. `bare_head`
—que es evidencia directa pero con etiqueta corta— cae **en el medio exacto**, y esa
posición intermedia es la evidencia más limpia de que **lo que manda es cómo se
expresa la condición, no si se infiere o se detecta**.

## 5. Percepción excelente, alertas mediocres — otra vez

`bare_head` tiene **la mejor percepción de todas las campañas**: SDR **0,940**
(vs 0,698 de T1), TTFD **41 ms** (vs 168 ms) y `t_alert` **3.919 ms** — por debajo de
los 4.000 ms de persistencia, o sea que la alerta cae esencialmente en la ventana
mínima contada desde el arranque del clip.

Y ahí está la falla: el mecanismo (`85-mecanismo-de-fallas.py`) da **13 prematuras de
pre-roll** contra 10 de su propio control E-IND, y **3 FP en clips negativos** (el peor
del banco; T1, T2 y B1-eind tienen 0). Con evidencia presente el 94% del episodio
—incluido el pre-roll donde el GT dice "cumple"— el patrón confirma antes de la
ventana. Es F-87.2 otra vez, con otra fuente de evidencia: **percepción casi perfecta y
alertas peores**, porque lo que rompe no es ver poco sino ver *antes*.

## 6. Qué queda cerrado

Con esta campaña se agotaron las palancas medibles sobre el banco del rodaje:

| Palanca | Resultado |
|---|---|
| Formulación (E-DIR frases) | D1 — veto de precisión |
| Fusión (E-HYB-or) | H1 — predicción refutada, F-87.2 |
| Modelo (base-560) | T2 — no recupera el pre-roll |
| **Vocabulario nativo del especialista (`bare_head`)** | **B1 — tampoco (0,480 vs 0,582)** |
| Granularidad (G1/`track_id`) | **pendiente** — requiere el productor (doc 79) |

**E-IND con `cr01_cr02_v2_short` sobre `gdino-tiny-560` (T1, F1 0,789) sigue siendo la
mejor combinación medida**, y ninguna de las cuatro palancas alternativas la superó.
La única que queda sin probar es la granularidad por sujeto, que ataca el mecanismo
(a) de F-81.2 — el único de los diagnosticados que ninguna palanca de percepción o
formulación puede tocar.
