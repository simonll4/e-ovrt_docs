# 72 — Cómo recortar los videos del rodaje, y la ficha de eventos

**Fecha:** 2026-07-26. **Insumo:** las 35 tomas del rodaje del 2026-07-25
(`e-ovrt_datasets/datasets-videos/raw/`, inventario en doc 71 §1).
**Salida:** los ~15 clips del Bloque A del banco, listos para CVAT.
**Para quién:** el que se sienta a recortar y después a anotar. Se lee de arriba hacia
abajo. **§0 explica qué es cada cosa** (pre-roll, onset, evento, cola, episodio,
censura) y es lo único que hay que leer entero: quien ya lo tenga claro, salta a §4,
que son las recetas por escenario, y a §4.10, que es la tabla que se tiene al lado
mientras se recorta.

> **Este documento decide dos cosas y las deja cerradas:**
> 1. **Dónde cortar cada toma** — con números, no con criterio. Cada escenario tiene
>    una fórmula y un piso duro que sale del gate A1 ya implementado; cortar por
>    debajo de ese piso **censura la métrica del clip en silencio** (el clip se ve
>    bien, la métrica no existe).
> 2. **Si hace falta la ficha de eventos** — **sí, y es bloqueante** (§5). Pero no
>    es la que estaba pensada para el día del rodaje: es una ficha **reconstruida
>    por inspección visual**, con un rol distinto y acotado. Nunca es el GT.

> **Actualización (2026-07-26):** este documento se escribió describiendo la
> consola de recorte tal como estaba esa mañana. Esa misma tarde la consola pasó
> a ser **consciente del escenario**: aplica la cola correcta por escenario
> (`SCENARIO_TAIL_S`), valida el piso A1 contra **todos** los escenarios con
> condición (no solo los cinco con objetivo de guion), y acepta las 4 marcas de
> P6/P8, calculando ella misma la fórmula de `D` que §4.6/§4.8 ya traían. Como
> consecuencia, **las recetas de §4 ahora las aplica la consola sola** — siguen
> siendo la referencia de qué números tienen que salir, pero ya no hace falta
> ejecutarlas a mano con el script directo ni compensar con marcas corridas. Los
> párrafos de §2, §4 y §7 de abajo quedan editados en consecuencia; donde no se
> pudo borrar el rastro de la versión vieja sin romper la numeración, queda
> aclarado en línea.

## 0. Qué es cada cosa (leer esto antes que nada)

Recortar bien es fácil **una vez que se entiende qué está haciendo el recorte**. No es
"dejar la parte linda": es **construir el presupuesto de tiempo** que las métricas
necesitan para poder existir. Esta sección define, en orden, todo lo que aparece
después.

### 0.1 La anatomía de un clip

```
   ss                                                                    ss + D
   │                                                                        │
   ▼                                                                        ▼
   ├──── PRE-ROLL ────┬───────────── EVENTO (hold) ─────────────┬─── COLA ───┤
   │      3,5 s       │                                          │    3,0 s   │
   │  en cumplimiento │        INFRACCIÓN sostenida              │ en cumplim.│
   │                  │                                          │            │
   0 s              onset                                       end        D (fin)
                      │                                          │
                      │◀────────── el EPISODIO ─────────────────▶│
                      │
                      ├── confirm 4 s (CR-01) / 7 s (CR-02) ──▶ ALERTA esperada
                      │
                      └── + t_alert_upper 10 s / 20 s ──▶ límite de "alerta lenta pero válida"
```

Un mismo instante tiene **dos nombres según contra qué se mida**, y confundirlos es
el error más común:

| | Referencia | Ejemplo |
|---|---|---|
| **`t1`, `t2`, …** (marcas de la ficha) | segundos sobre el **master** (el archivo crudo del rodaje) | "el casco sale a los 15,4 s de `P6-a-take2.mp4`" |
| **`onset_rel`, `start_ms`, `end_ms`** | milisegundos **dentro del clip recortado** | "el episodio arranca en 3500 ms del clip" |

La conversión es una resta: **`instante_en_el_clip = instante_en_el_master − ss`**.
Todo el GT, todas las alertas y todas las métricas viven en el segundo sistema; la
ficha y el recorte viven en el primero.

### 0.2 Los seis términos

**`ss` (start seek) — dónde empieza el corte en el master.**
Es el argumento `--ss` de `ffmpeg`. Todo lo anterior a `ss` se descarta. Elegir `ss`
**es** recortar: fija cuánto pre-roll hay y, por arrastre, en qué milisegundo del clip
cae el onset.

**`D` (duración) — cuánto dura el clip.**
Es el argumento `--to` del script, que a pesar del nombre **es una duración, no un
instante de fin** (§2.2). El clip abarca `[ss, ss + D]` del master.

**ONSET — el instante en que arranca la infracción.**
No es cuando el actor empieza el gesto: es cuando el EPP **deja de estar puesto**
(el frame exacto lo fija la convención de §5.3). Es el t=0 de todo lo que se mide:
el motor cuenta desde ahí sus 4 s (CR-01) o 7 s (CR-02) para confirmar, y el
evaluador mide desde ahí el TTFD y el `t_alert-system`. **Es el instante más
importante del clip.**

**PRE-ROLL — el tiempo de cumplimiento ANTES del onset.**
Son los 3,5 s en que la persona está en cuadro **con el EPP puesto**. Parece relleno
y es lo contrario:

- **Sin pre-roll no hay TTFD.** El TTFD mide *onset → primera detección*. Si el clip
  arranca ya en infracción, el onset es t=0, el TTFD da 0 ms y **eso no es un
  resultado excelente: es un artefacto de recorte**. Es exactamente lo que pasó con
  `video16_clip10` y lo que motivó el gate A1.
- **Sin pre-roll no hay línea de base.** No se puede distinguir "el sistema detectó
  el cambio" de "el sistema siempre vio lo mismo".
- Tiene respaldo externo triple (i-LIDS descarta warm-up, ODAS mide onset con
  offsets, THUMOS trabaja sobre video *untrimmed*) — doc 57 §3.1 punto 6.

Por eso `MIN_ONSET_MS = 2000`: un clip cuyo primer episodio arranca antes de los 2 s
queda marcado, aunque se vea perfecto.

**EVENTO (o *hold*) — la infracción sostenida.**
Va del onset al fin del episodio. Su largo lo decide **la métrica más lenta que el
clip tiene que permitir**, no la comodidad del actor: el clip debe seguir corriendo
hasta después del momento en que una **alerta lenta pero todavía válida** podría
llegar (10 s para CR-01, 20 s para CR-02). Si el clip termina antes, no se puede
distinguir *"alertó tarde pero dentro del target (pasa)"* de *"no alertó nunca
(falla)"* — y ahí es donde aparece la censura (§0.3).

**COLA — el tiempo de cumplimiento DESPUÉS del fin.**
La persona ya se puso el EPP y el clip sigue. Cumple dos funciones distintas:

- **Observar el cierre por `resolve`** (2 s en CR-01, 3 s en CR-02): que la alerta
  efectivamente se apague, y que no aparezcan alertas tardías espurias.
- **Dar tiempo muerto donde el sistema *pueda* equivocarse.** La precision se mide
  contra el tiempo sin infracción; un clip que corta apenas termina el evento
  **regala una precision alta que no midió nada**.

**EPISODIO — el par (onset, fin) con su condición.**
Es la unidad del GT (`clip_gt.v2`) y la unidad de evaluación: recall, TTFD y
`t_alert-system` se computan **por episodio**. Un clip puede tener 0 (P3, P5), 1
(P1, P2, P4, P7, P9) o 2 (P6, P8) episodios. Los clips de 2 son los que gobiernan el
recorte, porque **el piso se calcula sobre cada episodio por separado** — y el que
manda es el último.

### 0.3 Censura: el modo de falla que este documento existe para evitar

> **Un clip censurado no da error, no se ve mal, y no aporta la métrica.**

Si el clip termina antes de que una alerta lenta-pero-válida hubiera podido ocurrir,
ese episodio **no es medible**, y el sistema lo sabe:

1. `derive_clip_gt.py` escribe un **`dimensioning_warning`** en `provenance` (gate A1)
   y lo avisa en el timeline que imprime.
2. El evaluador del control-plane **censura** ese episodio (A2): lo saca del
   denominador de recall en vez de contarlo como fallo, y no produce `t_alert-system`.

Ninguna de las dos cosas rompe nada: el clip se anota igual, corre igual y produce
artefactos igual. Simplemente **la métrica para la que fue filmado no aparece**, y el
trabajo caro (la pasada humana en CVAT) ya se gastó. Por eso el piso se verifica
**antes** de recortar, con la tabla de §4.10.

El otro lado de la moneda: **la censura es una protección, no un castigo**. Es lo que
impide que un clip mal dimensionado se cuente como "el sistema no alertó" cuando en
realidad el clip no le dio tiempo. Trabajar con ella a favor —dimensionando bien— es
lo único que hace que las métricas del banco sean citables.

### 0.4 El resumen en una línea

> Recortar bien = **poner el onset en el segundo 3,5 del clip** y **hacer el clip lo
> bastante largo como para que el último episodio aguante `onset + 14 s` (CR-01) o
> `onset + 25 s` (CR-02)**. Todo §4 es esa frase aplicada a nueve escenarios.

Dicho de otra forma — las tres piezas del clip no tienen el mismo estatus:

| Pieza | Estatus | Regla |
|---|---|---|
| **Pre-roll** | **fijo por convención** | 3,5 s. La consola no da otra cosa; el mínimo duro es 2,0 s y por arriba es decisión con costo (§4.11 caso 1). |
| **Evento** | **dado por la toma** | No se edita: se elige la toma que lo tenga. Mínimo metodológico 8 s (CR-01) / 12 s (CR-02). |
| **Cola / corte final** | **la palanca libre** | Es lo que se ajusta para cerrar la cuenta, y lo que se alarga sin culpa cuando hay dudas. |

Y la cuenta que hay que cerrar, con el pre-roll ya cancelado a los dos lados:
**`evento + cola ≥ 14 s` (CR-01) · `≥ 25 s` (CR-02)** (derivación en §4.11 caso 4).

Y como ninguna toma real da los tiempos exactos del guion, **§4.11 es la sección que
dice qué hacer cuando sobra o falta tiempo** — incluido el único caso donde que sobre
rompe algo (el transitorio de P3).

---

## 1. Las cinco restricciones duras (todo lo demás se deriva de acá)

Estos números **no son del guion, son del código que ya está escrito**. Están
verificados leyendo las fuentes, no la documentación.

| # | Constante | Valor | Dónde vive |
|---|---|---|---|
| 1 | Pre-roll antes del onset | **3,5 s** | `webconsole/.../clips/window.py: PRE_ROLL_S` |
| 2 | Cola después del fin, **por escenario** | **3,0 s** default · **5,0 s** P2 · **10,0 s** P4 | `window.py: SCENARIO_TAIL_S` |
| 3 | Duración objetivo por escenario (guion) | P1 20 · P2 30 · P3 15 · P5 15 · P9 18 s | `window.py: SCENARIO_TARGET_S` |
| 4 | Piso del gate A1 (por episodio), validado en la consola para todo escenario con condición | `start_ms + t_alert_upper + resolve + 2000` | `derive_clip_gt.py: DIMENSIONING_MS`, espejado en `window.py: piso_s()` |
| 5 | Onset mínimo del primer episodio | **2000 ms** | `derive_clip_gt.py: MIN_ONSET_MS` |

> **Desde 2026-07-26 la cola (fila 2) ya no es una sola constante**: `window.py`
> define `SCENARIO_TAIL_S = {"P2": 5.0, "P4": 10.0}` y usa 3,0 s como default para
> el resto. La consola aplica la cola correcta sola, según el escenario del clip
> que se está recortando — ya no hay que compensarla a mano (compárese con §2.1 y
> §4.2/§4.4 más abajo). La fila 3 (objetivo de guion) **no cambió**: sigue cargada
> solo para P1/P2/P3/P5/P9; lo nuevo es que el piso (fila 4) ahora se valida en
> los nueve escenarios, target o no.

Y el gate A1 desplegado por condición:

| Condición | `t_alert_upper` | `resolve` | cola A1 | **Piso = onset + …** |
|---|---|---|---|---|
| **CR-01** (sin casco) | 10 000 ms | 2 000 ms | 2 000 ms | **onset + 14,0 s** |
| **CR-02** (sin chaleco) | 20 000 ms | 3 000 ms | 2 000 ms | **onset + 25,0 s** |

> **Cómo se lee el piso:** un episodio CR-02 que arranca en `t=3,5 s` del clip
> exige que el clip **dure al menos 28,5 s**. Si dura menos, `derive_clip_gt.py`
> escribe un `dimensioning_warning`, y el evaluador (A2) **censura ese episodio**:
> sale del denominador de recall y no produce `t_alert-system`. El clip existe, se
> anota, se corre… y no aporta la métrica para la que fue filmado.
>
> **El piso se calcula sobre el ÚLTIMO episodio del clip, no sobre el primero.**
> `dimensioning_warnings()` itera episodio por episodio. Por eso P6 y P8 —los dos
> clips con más de un episodio— tienen los pisos más altos de todo el banco, y son
> justamente donde el recorte "por sentido común" falla (§4.6 y §4.8).

**Consecuencia de diseño que conviene tener presente:** el pre-roll y la cola no
son estética. Sin pre-roll, TTFD colapsa a 0 y no es una medición sino un
artefacto (doc 57 §3.1 punto 6). Sin cola, no se observa el cierre por `resolve` y
la precision sale alta por falta de tiempo muerto donde equivocarse.

---

## 2. Las dos herramientas, y cuándo usar cada una

### 2.1 La consola (ventana **Clips** → diálogo de recorte)

Reproductor del master, **consciente del escenario** que se le pasa. El diálogo
muestra botones dinámicos según el escenario: para los de un solo episodio son dos
(`Marcar evento` / `Marcar fin`, con las etiquetas propias de cada uno, ver abajo);
para P6 y P8 son cuatro, y cada botón queda **deshabilitado hasta que se marcó el
anterior** (fuerza el orden cronológico). Todos leen `video.currentTime`
(precisión ±0,3 s). Con las marcas, la consola:

1. calcula la ventana: `ss = t_primera_marca − 3,5` y `duración = (t_última_marca +
   cola_escenario) − ss`, con `cola_escenario` saliendo de `SCENARIO_TAIL_S` (3,0 s
   default, 5,0 s en P2, 10,0 s en P4 — ver §1);
2. para P6 y P8, calcula `D` con la misma fórmula que ya trae este documento en
   §4.6/§4.8 (`máx(cobertura, piso del episodio más exigente + 1 s)`), iterando
   todos los episodios del clip;
3. llama a `prepare_clip.sh` con `--ss` y `--to`, **fps 30 fijo, sin `--scale`**
   (el clip queda 1920×1080 CFR 30 sin audio — la OAK-D de 60 fps se re-samplea);
4. asigna el `clip_id` **`a_<escenario>_c<NN>`** (correlativo, nunca pisa uno existente);
5. escribe el `<clip_id>.clip.yaml` con `block: A`, `scenario`, `source_id = clip_id`,
   `level: scene`, `master:` y un **`episode_draft`** en forma de **lista** (una
   entrada para los escenarios de un episodio, dos para P6/P8), cada una con
   `onset_ms`, `end_ms` y `condition`; `warnings` queda como clave de primer nivel
   del YAML, no anidada dentro de `episode_draft` (§6.3);
6. devuelve **dos tipos de advertencia, separados, que pueden aparecer juntas**:
   la del **objetivo de guion** ("clip de X s, el guion pide ~Y s para este
   escenario", solo para P1/P2/P3/P5/P9) y la del **piso de censura**
   ("clip de X s, el piso de censura pide Y s para este episodio — por debajo,
   `t_alert-system`/recall quedan censurados, doc 57 §6.7"), calculada con
   `piso_s(escenario)` y validada **siempre** que el escenario tenga condición
   (P1/P4/P7/P9 → 17,5 s CR-01; P2 → 28,5 s CR-02; por episodio en P6/P8). P3 y
   P5 no tienen piso porque no tienen episodio.

**Lo que sigue sin hacer la consola:**

- Llamarla con 2 marcas para un escenario que declara 4 (P6, P8) es un **error
  explícito**: la rechaza, no recorta corto en silencio.
- El pre-roll sigue fijo en 3,5 s, sin parámetro (no cambió — §4.11 caso 1).
- No reemplaza la ficha de eventos (§5): las marcas de la consola tienen
  precisión ±0,3 s, que alcanza para recortar pero no para el ±0,1 s que pide el
  GT esperado de la ficha, ni para el transitorio de P3 (§4.11 caso 3), que sigue
  siendo un chequeo manual con la tira de miniaturas.

### 2.2 El script directo (`prepare_clip.sh`)

Sigue existiendo y sigue siendo válido para uso directo (batch, debugging, o
recortar fuera de la webconsole), pero desde que la consola quedó consciente del
escenario **ya no hace falta pasar por acá para ningún escenario del banco** —
ver §2.3.

```bash
cd ~/projects/e-ovrt_datasets
datasets/scripts/videogt/prepare_clip.sh \
    datasets-videos/raw/<master>.mp4 <clip_id> --ss <inicio_s> --to <DURACIÓN_s> --fps 30
```

> ⚠️ **`--to` es DURACIÓN, no instante de fin.** El script pone `-ss` antes de `-i`
> y `-to` después, así que ffmpeg lo interpreta relativo al punto de corte. Pasar un
> instante absoluto **no falla**: produce en silencio un clip más largo con el evento
> descolocado respecto del GT. Es la trampa ya documentada (D3 en `clips/trim.py`).

Emite `clips/<clip_id>.mp4` + `<clip_id>.info.json` (sha256, fps, n_frames,
duration_ms). **No escribe el `.clip.yaml`: hay que escribirlo a mano** (plantilla
en §6.3), y tiene que quedar en la **raíz** de `datasets-videos/` — ahí lo buscan
`promote_clip.py` y la consola, y moverlo rompe las dos cosas.

### 2.3 Regla de decisión

**Los nueve escenarios se recortan desde la consola.** Ya no hay ningún escenario
que dependa del script directo: la consola conoce la cola de cada uno
(`SCENARIO_TAIL_S`) y sabe pedir las 4 marcas de P6/P8 y calcular su `D`.

| Escenario | Marcas que pide la consola | Por qué ya no hace falta el script |
|---|---|---|
| **P1, P3, P7, P9** | 2 (etiquetas propias de cada uno, §5.5) | Cola de 3,0 s (default) alcanza. |
| **P2** | 2 (`chaleco_fuera` / `chaleco_puesto`, marcando el fin **real**) | La consola ya aplica 5,0 s de cola sola (§4.2). |
| **P4** | 2 (`casco_fuera` / `casco_puesto`) | La consola ya aplica 10,0 s de cola sola (§4.4). |
| **P5** | 2 (`tramo_inicio` / `tramo_fin`) | No hay episodio; la consola igual pide un par de marcas. |
| **P6** | 4 (`casco_fuera`, `chaleco_fuera`, `chaleco_puesto`, `casco_puesto`) | La consola calcula `D` con la fórmula de §4.6 sola. |
| **P8** | 4 (`casco_fuera`, `sale_de_cuadro`, `vuelve_a_entrar`, `casco_puesto`) | La consola calcula `D` con la fórmula de §4.8 sola. |

El script directo (§2.2) sigue disponible para uso fuera de la consola, pero
ningún paso del flujo de este documento depende de él.

---

## 3. Qué toma se recorta (selección del material)

Las 35 tomas tienen entre **21,6 s y 71,0 s** — todas tienen margen de sobra para
el recorte que pide su escenario. La duración **no** es el criterio de selección;
el criterio es visual.

### 3.1 Criterio de selección de toma (en orden, primer criterio que discrimina gana)

1. **Cuadro limpio**: 1 o 2 personas, nadie de fondo. Una persona accidental mete un
   sujeto sin GT y arruina el clip para siempre.
2. **La coreografía se ejecutó completa** y en el orden del guion (arranca en
   cumplimiento, la transición se ve, hay cola).
3. **El EPP se ve nítido a la distancia de escena** — acá es donde se caen las tomas
   del DVR (§3.3).
4. **La transición es legible**: se distingue el frame en que el casco deja la cabeza
   / el chaleco deja los hombros. Si la transición ocurre de espaldas o fuera de foco,
   la marca del GT queda a criterio y el clip pierde valor para TTFD.
5. A igualdad de todo lo anterior, **la toma más larga** (más margen para elegir la
   ventana).

### 3.2 Material disponible por escenario

Duraciones medidas de los sidecars `.rec.json`. **La cámara sale del sidecar, no del
nombre** — los `takeN` interlevan OAK-D y DVR bajo la misma numeración (doc 71 §1).

| Escena | OAK-D (60 fps) | DVR (15 fps) |
|---|---|---|
| P1-a | take2 (57,1 s) · take3 (34,7) · take4 (42,0) | take5 (37,9) |
| P1-b | take3 (38,3) · take5 (39,8) | take1 (36,5) |
| P1-c | take5 (40,2) · take6 (35,6) | take2 (36,9) · take4 (37,0) |
| P2-a | take1 (48,5) | take2 (50,8) |
| P2-b | take1 (44,9) | — |
| P2-c | take1 (49,8) · take2 (51,4) | — |
| P3-a | take1 (22,3) · take2 (21,6) | — |
| P4-a | take1 (40,1) | take2 (38,9) |
| P5-a | take1 (41,4) · take2 (55,7) | take3 (57,4) |
| P6-a | take1 (55,4) · take2 (71,0) | — |
| P7-a | take1 (50,1) | — |
| P7-b | take1 (44,7) · take2 (43,5) | take3 (45,8) |
| P8-a | take1 (54,2) | — |
| P9-a | take2 (26,3) · take3 (23,6) | take1 (26,9) |
| P9-b | take1 (24,7) · take2 (23,1) | — |

### 3.3 El subset DVR se verifica ANTES de recortarlo

Las 9 tomas DVR pesan 3–13 MB para 27–57 s: **1,3–2 Mbps a 1920×1080**. Es
compresión pesada y los bloques pueden comerse el casco a distancia (doc 71 §1).

**Protocolo, 5 minutos:** de cada toma DVR candidata, extraer 3 frames —uno en
cumplimiento, uno en plena infracción, uno en la transición— y mirarlos al 100 %:

```bash
cd ~/projects/e-ovrt_datasets/datasets-videos/raw
for t in 5 15 25; do
  ffmpeg -y -v error -ss $t -i P1-a-take5.mp4 -frames:v 1 /tmp/dvr_P1a_$t.png
done
```

Si en esos frames el casco/chaleco **no se distingue con confianza a ojo**, la toma
no entra al banco: un anotador humano no puede fijar un GT que no ve, y un GT dudoso
contamina toda métrica que lo use. Se declara la exclusión y el subset queda con las
que pasen — **no bloquea al resto del banco** (doc 71 §7.1 paso 1).

### 3.4 Orden de trabajo propuesto (y por qué en tres tandas)

El cuello de botella no es recortar (minutos) sino **anotar en CVAT**: cada clip son
600–950 frames a 30 fps. Por eso el banco se arma por tandas, y cada tanda es
autoconsistente — si el tiempo se corta, lo hecho ya sirve.

| Tanda | Clips | Aporte |
|---|---|---|
| **1 — núcleo mínimo defendible** (11) | P1-a, P1-b, P2-a, P2-b, P3-a, P4-a, P5-a, P6-a, P7-a, P8-a, P9-b | Cumple el mínimo de composición de doc 57 §6.4: ≥2 P1, ≥2 P2, 1 P4, 1 P6, 1 P7, 1 P8, 1 P3, 1 P5, 1 P9 |
| **2 — robustez** (4) | P1-c, P2-c, P7-b, P9-a | Oclusión parcial ×2, cruces multi-persona, confusable de vestuario |
| **3 — segunda fuente** (≤3) | `P1-a-take5`, `P2-a-take2`, `P5-a-take3` (DVR) | Evidencia de existencia sobre RTSP comodity — **solo si pasan §3.3** |

**Empezar por P1-a y P2-a** (doc 71 §7.1 paso 3): son las escenas de las dos
condiciones principales, y son las que desbloquean cualquier número citable.

---

## 4. Receta de recorte por escenario

**Notación** (todas las marcas son **segundos sobre el master**, con un decimal):

- `t1, t2, …` = las marcas de la ficha (§5), en orden cronológico.
- `ss` = argumento `--ss` (inicio del corte en el master).
- `D` = argumento `--to` (**duración** del clip).
- `onset_rel` = instante del evento **dentro del clip** = `t_evento − ss`.

Y la regla que gobierna todo: **`ss = t_primer_onset − 3,5`**. Si eso da negativo,
el clip arranca en 0 y el pre-roll queda corto: se anota y se declara TTFD degradado
(la consola avisa; el script no).

---

### 4.1 P1 — Sin casco (CR-01) · 3 clips · **consola**

Marcas: **`t1` = casco fuera de la cabeza**, **`t2` = casco de vuelta puesto**.

```
ss = t1 − 3,5
D  = (t2 − t1) + 6,5          # 3,5 pre-roll + evento + 3,0 cola
onset_rel = 3,5 s
```

| Chequeo | Umbral | Con el evento guionado (14 s) |
|---|---|---|
| Piso A1 (CR-01) | `D ≥ 17,5 s` ⇒ evento **≥ 11,0 s** | D = 20,5 s ✅ |
| Objetivo de escenario | `D ≥ 20 s` ⇒ evento **≥ 13,5 s** | ✅ sin warning |

- **P1-c (oclusión parcial):** la ventana **tiene que contener la oclusión completa**
  (los 2–4 s detrás del objeto). Si el actor pasa detrás del objeto cerca del final
  del hold, alargar `D` hasta que la re-aparición quede dentro del clip con ≥3 s
  después: lo que se mide es la **recuperación** del tracking, y si el clip corta
  durante la oclusión no hay nada que recuperar. Anotar en la ficha el par
  `t_ocl_ini / t_ocl_fin`.
- Si el evento real quedó entre 11,0 y 13,5 s, el clip **sirve** (A1 pasa) pero la
  consola avisa: aceptar el warning y anotarlo, no forzar el recorte.

---

### 4.2 P2 — Sin chaleco (CR-02) · 3 clips · **consola**

Marcas: **`t1` = chaleco fuera de los hombros**, **`t2` = chaleco de vuelta puesto**.

```
ss = t1 − 3,5
D  = (t2 − t1) + 8,5          # 3,5 pre-roll + evento + 5,0 cola
```

| Chequeo | Umbral | Con el evento guionado (22 s) |
|---|---|---|
| Piso A1 (CR-02) | `D ≥ 28,5 s` ⇒ evento **≥ 22,0 s** | con cola 3,0: D = 28,5 s — **justo sobre el piso, margen 0** |
| Objetivo de escenario | `D ≥ 30 s` | con cola 3,0: **warning** |

**Por eso P2 lleva cola de 5 s y no de 3.** Desde 2026-07-26 esto lo resuelve sola
la consola (`SCENARIO_TAIL_S["P2"] = 5.0`): **se marca el fin REAL**, el instante
en que el chaleco vuelve a estar puesto, ni un segundo después. La consola suma
los 5,0 s de cola por su cuenta.

> **Ya no hay que correr la marca de fin.** La versión anterior de este documento
> pedía marcar el fin 2 s después del instante real para simular a mano una cola
> de 5 s con una consola que solo daba 3,0 s fijos. Seguir haciendo eso ahora
> **es activamente contraproducente**: la consola ya suma sus 5,0 s de cola sobre
> la marca, así que correr la marca 2 s más produce 7 s de cola reales y un
> `episode_draft.end_ms` que queda 2 s largo respecto del episodio real. Marcar
> siempre el fin real; el `episode_draft` que escribe la consola queda correcto
> sin necesidad de aclaración ni de comentario compensatorio en el YAML.

- **El chaleco tiene que estar FUERA de cuadro** durante el hold. Si quedó colgado
  del brazo o apoyado a la vista, F-RT1 aplica (GDINO marca `vest` sobre el torso
  descubierto, con picos medidos de **0,73** sobre remera negra lisa) y el clip
  medirá una supresión de vestuario, no una propiedad del motor. Verificarlo en el
  video **antes** de recortar: es criterio de selección de toma, no de recorte.
- **P2-c (oclusión):** mismo agregado que P1-c.

---

### 4.3 P3 — Transitorio sub-umbral (no debe alertar) · 1 clip · **consola**

Marcas: **`t1` = casco fuera**, **`t2` = casco puesto** (≈2 s después).

```
ss = t1 − 3,5
D  = 15,0                     # fijo: 3,5 pre + ~2 transitorio + ~9,5 post
```

- **No hay episodio** ⇒ **no hay piso A1**. Lo que gobierna es otra cosa: después del
  estímulo tiene que caber **al menos una ventana de confirmación completa sin que se
  confirme** (4 s de CR-01 + 2 s de resolve + margen). Con 9,5 s post sobra.
- Con la consola: marcar `t_fin` ≈ `t2 + 6,5` para llegar a los 15 s. Si se marca
  `t2` real, D = 8,5 s y **la consola avisa** ("el guion pide ~15 s"): ese warning es
  correcto, hay que hacerle caso.
- El `episode_draft` de este clip **no es un episodio**: el GT correcto de P3 es
  **cero episodios + un `sub_threshold_event`**. Dejarlo dicho en el YAML.
- ⚠️ **Medir el transitorio antes de recortar.** Si duró **≥ 4,0 s**, el derivador lo
  clasifica como episodio real y P3 deja de existir como control negativo — con el
  agravante de que el clip de 15 s queda censurado. Tabla de decisión y qué hacer con
  cada rango: **§4.11, caso 3**.
- Los dos masters son los más cortos del lote (21,6 y 22,3 s) — igual sobra.

---

### 4.4 P4 — Resolución y permanencia en cuadro · 1 clip · **consola**

Marcas: **`t1` = casco fuera**, **`t2` = casco puesto**.

```
ss = t1 − 3,5
D  = (t2 − t1) + 13,5         # 3,5 pre + evento + 10,0 cola
```

Con el evento guionado (14 s): **D = 27,5 s**.

> **La cola de 10 s ES el escenario.** P4 se filmó para observar que la alerta
> cierre y que la persona se siga siguiendo en cumplimiento. Antes del cambio del
> 2026-07-26, con la cola fija de 3 s de la consola P4 quedaba convertido en una
> copia de P1 y la consola no avisaba nada (P4 no está en `SCENARIO_TARGET_S`, y
> el piso no se validaba para ningún escenario). Ahora `SCENARIO_TAIL_S["P4"] =
> 10.0`: la consola aplica la cola de 10 s sola con las dos marcas de siempre
> (`casco_fuera` / `casco_puesto`), y valida el piso A1 (aunque siga sin target de
> guion, porque `SCENARIO_TARGET_S` no cambió). Ya no hace falta el script.

Piso A1: `D ≥ 17,5 s` — se cumple con enorme margen, y la consola lo confirma.

---

### 4.5 P5 — Cumplimiento total (negativo) · 1 clip · **consola o script**

**No hay evento.** Lo que se busca es una ventana de **15–18 s** con los dos actores
en cuadro, trabajando normal, sin nada raro.

```
ss = t_ambos_en_cuadro − 0,5
D  = 15,0 … 18,0
```

- Elegir el tramo **más representativo**, no el más quieto: movimiento, cruces
  naturales, cambios de escala. Un negativo estático mide menos de lo que parece.
- Desde 2026-07-26 las dos marcas de P5 en la consola se llaman explícitamente
  `tramo_inicio` / `tramo_fin` (no "evento"/"fin", que hubiera sido engañoso para
  un escenario sin infracción). El pre-roll de 3,5 s se sigue aplicando igual
  delante de `tramo_inicio` — la consola no distingue P5 para eso —, así que sigue
  valiendo poner `t_inicio = ss + 3,5` y `t_fin = t_inicio + 8,5` para llegar a los
  15 s. El `episode_draft` resultante **es espurio** — declararlo en el YAML.
- El GT correcto es `negative: true` (cero episodios). `derive_clip_gt.py` lo emite
  solo si la anotación de CVAT no deja ninguna violación; **`--allow-empty` NO va acá**
  (es para clips sin personas en cuadro, y P5 tiene dos).

---

### 4.6 P6 — Las dos condiciones a la vez · 1 clip · **consola (4 marcas)**

Cuatro marcas — desde 2026-07-26, las pide la consola directamente, en botones que
se habilitan en orden: **`casco_fuera`** (`t1`) · **`chaleco_fuera`** (`t2`) ·
**`chaleco_puesto`** (`t3`) · **`casco_puesto`** (`t4`). La consola modela P6 como
dos episodios **anidados** (CR-01 = `[t1, t4]`, CR-02 = `[t2, t3]`).

```
ss = t1 − 3,5
onset_CR01_rel = 3,5
onset_CR02_rel = 3,5 + (t2 − t1)

D = máx(
      (t4 − t1) + 6,5,                    # cubrir los dos eventos + 3 s de cola
      onset_CR02_rel + 25,0 + 1,0         # piso A1 del episodio CR-02 + 1 s de margen
    )
```

Con los tiempos guionados (`t2−t1 = 3 s`, `t4−t1 = 23 s`):

| Candidato | Valor |
|---|---|
| Cobertura de los eventos | 29,5 s |
| **Piso A1 del episodio CR-02** (onset 6,5 + 25,0) | **31,5 s** |
| **D adoptada** | **≈ 32,5 s** |

> **Éste es el caso que el sentido común corta mal.** El recorte "natural" —cubrir
> los cuatro momentos y poner 3 s de cola— daría 29,5 s y **censuraría el episodio
> CR-02**: el clip quedaría 2 s por debajo del piso, `derive_clip_gt.py` escribiría
> el `dimensioning_warning`, el evaluador sacaría ese episodio del denominador, y
> P6 —el único clip de doble condición del banco— dejaría de aportar la mitad de
> lo que fue filmado para aportar. **Desde 2026-07-26 esto ya no depende de que
> quien recorta se acuerde de la cuenta**: la consola aplica esta misma fórmula
> sola —`D = máx(cobertura, piso del episodio más exigente + 1 s)`, iterando los
> dos episodios— y devuelve los ≈32,5 s adoptados sin que haga falta calcularlos a
> mano. La fórmula de abajo sigue siendo la que hay que entender para leer lo que
> la consola hizo; ya no hay que ejecutarla con el script.
>
> **El escalonamiento sigue jugando en contra:** cada segundo que el chaleco sale
> *después* del casco empuja el piso un segundo hacia arriba — la consola lo
> recalcula sola por cada clip, pero conviene tenerlo presente al elegir la toma.

Master disponible: `P6-a-take2` con **71,0 s** — margen de sobra para los 32,5 s.

---

### 4.7 P7 — Dos personas, una infringe · 1–2 clips · **consola**

Marcas: **`t1` casco fuera de ACTOR A**, **`t2` casco puesto**. Mismo cálculo que P1:

```
ss = t1 − 3,5
D  = (t2 − t1) + 6,5
```

- **P7-b (cruces):** los cruces tienen que quedar **enteros dentro del clip** — son
  ~10 s y ocurren durante el hold. Si el recorte parte la secuencia de cruces, se
  pierde justo la señal que P7-b mide (que la infracción no salte de identidad).
  Alargar `D` hasta cubrirla; doc 57 §2 pide 25–30 s para P7 por esta razón.
- **No hay objetivo de guion cargado para P7** ⇒ la consola no avisa por ese lado.
  Sí avisa por **piso A1** (`D ≥ 17,5 s`), desde 2026-07-26. Lo que sigue sin
  validar sola la consola es la **cobertura de los cruces** (~10 s dentro del
  hold): eso se sigue verificando a mano.
- **ACTOR B no genera episodio**: cumple todo el clip. Eso hay que sostenerlo en
  CVAT, no en el recorte.

---

### 4.8 P8 — Sale y vuelve a entrar (dos episodios) · 1 clip · **consola (4 marcas)**

Cuatro marcas — desde 2026-07-26, las pide la consola directamente, en botones que
se habilitan en orden: **`casco_fuera`** (`t1`) · **`sale_de_cuadro`** (`t2`) ·
**`vuelve_a_entrar`** (`t3`, sigue sin casco) · **`casco_puesto`** (`t4`). La
consola modela P8 como dos episodios **secuenciales** (episodio 1 = `[t1, t2]`,
episodio 2 = `[t3, t4]`).

```
ss = t1 − 3,5
onset_ep1_rel = 3,5
onset_ep2_rel = 3,5 + (t3 − t1)

D = máx(
      (t4 − t1) + 6,5,                    # cubrir ambos episodios + 3 s de cola
      onset_ep2_rel + 14,0 + 1,0          # piso A1 del episodio 2 (CR-01) + margen
    )
```

Con los tiempos guionados (`t3−t1 = 13 s`, `t4−t1 = 21 s`):

| Candidato | Valor |
|---|---|
| Cobertura de los eventos | 27,5 s |
| **Piso A1 del episodio 2** (onset 16,5 + 14,0) | **30,5 s** |
| **D adoptada** | **≈ 31,5 s** |

- Mismo modo de falla que P6: recortar por cobertura censuraría el **segundo**
  episodio, que es exactamente el que P8 fue filmado para producir. Coincide con
  el piso que ya había calculado doc 58 §"P8" (30 000 ms). **Desde 2026-07-26 la
  consola aplica esta misma fórmula sola** (mismo mecanismo que P6, §4.6): calcula
  `D` iterando los dos episodios y devuelve los ≈31,5 s adoptados sin que haga
  falta calcularlos a mano.
- **Verificar que la ausencia dure > `resolve` (2 s).** El guion pide ≥5 s; si en la
  toma real fue más corta, los dos episodios se pegan en uno y el clip pasa a medir
  otra cosa — se anota como hallazgo, no se re-recorta para "arreglarlo".
- Master: `P8-a-take1`, 54,2 s. Sobra.

---

### 4.9 P9 — Confusables · 1–2 clips · **consola**

**Es la única escena que arranca ya en infracción** (el actor entra con gorra, o con
el casco en la mano). Y **la gorra sin casco / el casco en la mano SON infracciones
reales** — llevan episodio CR-01 en el GT. Lo que se testea es si el modelo **pierde**
la alerta (falso cumplimiento), no un falso positivo.

Marcas: **`t1` = primer frame con el sujeto completo en cuadro** (= onset del
episodio) · **`t2` = el sujeto sale de cuadro o termina la acción**.

```
ss = t1 − 3,5                 # el pre-roll acá es escena vacía / el sujeto entrando
D  = máx( (t2 − t1) + 6,5 , 18,0 )
```

| Chequeo | Umbral |
|---|---|
| Piso A1 (CR-01) | `D ≥ 17,5 s` |
| Objetivo de escenario | `D ≥ 18 s` |
| `MIN_ONSET_MS` | `onset_rel ≥ 2,0 s` |

> **La trampa de P9:** si el master arranca con el actor **ya dentro del cuadro**, no
> hay de dónde sacar pre-roll: `ss` se va a 0, `onset_rel` cae por debajo de los 2,0 s
> y A1 marca el clip. **No se falsea moviendo el corte** — se declara: el clip sirve
> para recall bajo estrés semántico (que es para lo que se filmó) y **su TTFD no se
> reporta**. Revisar los cuatro masters (`P9-a-take2/take3`, `P9-b-take1/take2`,
> 23–26 s) y elegir el que tenga más segundos de escena antes de la entrada.

---

### 4.10 Tabla de referencia rápida

Desde 2026-07-26 los nueve escenarios se recortan desde la consola, y el aviso de
piso ya no depende de tener un objetivo de guion cargado: la consola valida el
piso A1 en **todo** escenario con condición, y por separado (si lo tiene) el
objetivo de guion. Por eso la tabla desdobla el aviso en dos columnas en vez de
una sola pregunta sí/no.

| Escenario | Herramienta | `ss` | `D` | Piso A1 | ¿Avisa por piso? | ¿Avisa por objetivo de guion? |
|---|---|---|---|---|---|---|
| P1 | consola | `t1 − 3,5` | `(t2−t1) + 6,5` | 17,5 s | ✅ | ✅ (target 20) |
| P2 | consola | `t1 − 3,5` | `(t2−t1) + 8,5` (cola 5,0 s) | 28,5 s | ✅ | ✅ (target 30) |
| P3 | consola | `t1 − 3,5` | `15,0` | — (sin episodio) | — (sin piso) | ✅ (target 15) |
| P4 | consola | `t1 − 3,5` | `(t2−t1) + 13,5` (cola 10,0 s) | 17,5 s | ✅ | — (sin target) |
| P5 | consola | tramo limpio | `15,0–18,0` | — (negativo) | — (sin piso) | ✅ (target 15) |
| P6 | consola (4 marcas) | `t1 − 3,5` | **`máx(cobertura, onset_CR02 + 26)`** ≈ 32,5 s | **onset_CR02 + 25** (episodio CR-02) | ✅ (por episodio) | — (sin target) |
| P7 | consola | `t1 − 3,5` | `(t2−t1) + 6,5`, cubriendo cruces | 17,5 s | ✅ | — (sin target) |
| P8 | consola (4 marcas) | `t1 − 3,5` | **`máx(cobertura, onset_ep2 + 15)`** ≈ 31,5 s | **onset_ep2 + 14** (episodio 2) | ✅ (por episodio) | — (sin target) |
| P9 | consola | `t1 − 3,5` | `máx((t2−t1)+6,5 , 18,0)` | 17,5 s | ✅ | ✅ (target 18) |

**Ya no hay filas donde la consola se quede callada si el clip queda corto.**
Antes del 2026-07-26, P4/P6/P7/P8 no tenían piso validado y P6/P8 ni siquiera
entraban al diálogo (❌ en la versión vieja de esta tabla) — ese agujero se
cerró. Lo que sigue siendo cierto es que **P4, P6, P7 y P8 no tienen objetivo de
guion** (columna derecha en "—"): para esos cuatro, el único número que se
respeta es el piso, no una duración "linda" — no hace falta perseguir más
duración que la que pide la fórmula de §4.6/§4.8, y la fila de piso es la que
hay que mirar con más atención en esos cuatro.

---

### 4.11 Cuando la toma real no coincide con el guion

Ninguna toma va a dar exactamente los tiempos del doc 69: el actor entró antes, el
hold salió de 19 s en vez de 14, el transitorio de P3 duró 3 s y no 2. **Eso es lo
esperado** — se filmó de más (33–71 s por toma) justamente para poder elegir después.

**El principio, y es asimétrico:**

> **El tiempo que sobra se tira o se aprovecha; el que falta no se fabrica.**
> Que sobre nunca rompe nada, pero **casi nunca es gratis**: cuesta duración total,
> cuesta frames de CVAT, y en un caso (pre-roll) **empuja el piso A1 hacia arriba**.
> Que falte tiene remedio solo cambiando de toma.

#### Tabla de decisión

| Qué salió distinto | ¿Rompe? | Qué hacer |
|---|---|---|
| **Pre-roll disponible > 3,5 s** (el actor estuvo mucho en cumplimiento antes) | No | **Por default, ignorarlo**: la consola toma 3,5 s exactos sin importar cuánto haya. Tomar más solo con motivo (abajo). |
| **Pre-roll disponible < 3,5 s** | Degrada | `ss` se clampea a 0 y la consola avisa. Si `onset_rel ≥ 2,0 s` el clip sirve con TTFD algo pobre; **si cae por debajo de 2,0 s, A1 lo marca** → preferir otra toma. |
| **Evento más largo que el guion** | No | **Gratis y bueno**: el piso A1 se calcula sobre el *onset*, no sobre el fin. Más hold = más muestra de SDR. Cubrirlo entero salvo que dispare el clip a >35 s (ver abajo). |
| **Evento más corto que el guion** | Depende de cuánto | El gate mira **`evento + cola`**, no el evento solo: con cola de 3 s el mínimo es **11,0 s (CR-01)** y **22,0 s (CR-02)** de hold, pero un hold corto **se compensa alargando la cola** (caso 4). Lo que no se compensa es el mínimo metodológico del evento: **8 s (CR-01) / 12 s (CR-02)**. |
| **Cola disponible > 3,0 s** | No | Gratis salvo frames de CVAT. **Alargarla es la opción segura por default** cuando hay dudas: da más tiempo muerto donde el sistema puede equivocarse, lo que hace la precision honesta en vez de generosa. |
| **Escalonamiento de P6 > 3 s** (el chaleco salió mucho después del casco) | **Empuja el piso** | Cada segundo extra sube el piso del clip **un segundo** (`onset_CR02` se corre). Recalcular `D` con la fórmula de §4.6 — no reusar los 32,5 s de ejemplo. |
| **Ausencia de P8 más larga** | No | Gratis: cuanto más larga, más limpia la separación en dos episodios. Sube `D` porque corre el onset del episodio 2 (fórmula de §4.8). |
| **Ausencia de P8 < 2 s** | **Sí, cambia lo que mide** | Ver abajo. |
| **Transitorio de P3 ≥ 4 s** | **Sí, deja de ser P3** | El caso más peligroso de todos. Ver abajo. |
| **P9 sin escena previa** (el actor ya está en cuadro en el frame 0 del master) | Degrada | No se puede fabricar pre-roll. Elegir entre las 4 tomas de P9 la que tenga más escena antes de la entrada; si ninguna la tiene, el clip sirve para recall bajo estrés semántico y **su TTFD no se reporta** (§4.9). |

#### Los tres casos que sí hay que pensar

**1. Pre-roll más largo NO es gratis: mueve el piso A1 uno a uno.**

Si se recorta con 5 s de pre-roll en vez de 3,5, el episodio arranca en 5000 ms y el
piso sube exactamente lo mismo:

| Pre-roll | Piso CR-01 (`onset + 14 s`) | Piso CR-02 (`onset + 25 s`) |
|---|---|---|
| 3,5 s (default) | **17,5 s** | **28,5 s** |
| 5,0 s | 19,0 s | 30,0 s |
| 8,0 s | 22,0 s | 33,0 s |

Con masters de 45–70 s hay lugar de sobra, así que **no es una restricción real**;
lo que sí es real es que **hay que rehacer la cuenta**, y que cada segundo de
pre-roll son 30 frames más para anotar sin aportar ninguna métrica nueva. Por eso el
default de 3,5 s se respeta salvo motivo declarado. Motivos válidos:

- **Duda sobre el frame exacto del onset** (transición de espaldas, fuera de foco):
  1–2 s extra de pre-roll dan margen para re-marcar sin volver a cortar.
- **Querer más tiempo de cumplimiento medible** (aporta a precision y FAR igual que
  la cola). Legítimo, pero para eso están los negativos y el soak, que salen más
  baratos por segundo.
- **P5 y soak**, donde el tiempo en cumplimiento *es* el material.

Techo práctico sugerido: **6 s**. Más que eso, conviene un negativo aparte.

**2. Evento muy largo: hasta dónde cubrirlo, y qué pasa si se corta en el medio.**

Si el hold real fue de 40 s, cubrirlo entero da un clip de ~46 s: **1 400 frames de
CVAT para medir lo mismo que miden 25**. Se puede terminar el clip antes del fin del
evento, y el laboratorio lo soporta de forma definida: `violation_intervals()` cierra
la corrida en **el fin del timeline** cuando la violación llega hasta el final. O sea
que el GT sale bien formado, con el episodio terminando en el último frame.

Lo que se pierde al cortar en el medio es concreto y hay que decidirlo a conciencia:

- **No se observa el cierre por `resolve`** — el clip ya no demuestra que la alerta se
  apaga.
- **No hay cola**, así que ese clip **no aporta a precision** (no tiene tiempo muerto).

**Regla:** cubrir el evento entero mientras el clip quede **≤ 35 s**. Si se pasa,
terminar el clip en `onset + 25 s` (CR-01) o `onset + 30 s` (CR-02) —bien por encima
del piso— y **anotar en la ficha que el episodio queda truncado**, para que después
nadie use ese clip como evidencia de cierre. El complemento barato: buscar el
argumento de cierre en P4, que se filmó exactamente para eso.

**3. El transitorio de P3 que se pasó de 4 s deja de ser P3.**

`classify_intervals()` separa episodio de sub-umbral **solo por duración**, contra el
mismo umbral que usa el motor: **≥ 4000 ms es episodio CR-01; < 4000 ms es
`sub_threshold_event`**. No mira la intención del guion.

> Si el actor sostuvo el transitorio 4,2 s en vez de 2, el GT emite un **episodio
> real**, y P3 —el control de "no debe alertar"— **desaparece del banco**. Peor: como
> ahora hay episodio, se activa el piso A1 (17,5 s) y el clip de 15 s de §4.3 queda
> **censurado**. Un clip que era el control negativo pasa a ser un clip de alerta mal
> dimensionado, sin que nadie lo haya decidido.

Por eso el transitorio de P3 **se mide en la ficha antes de recortar**, con la tira de
miniaturas de §5.4 (precisión 0,25 s), no a ojo:

| Transitorio medido | Veredicto |
|---|---|
| **≤ 3,0 s** | ✅ P3 válido. Recortar según §4.3. |
| **3,0 – 4,0 s** | ⚠️ **Filo de cuchillo**: el jitter de anotación (±0,2 s) puede voltearlo a episodio. Preferir la otra toma. |
| **≥ 4,0 s** | ❌ Ya no es P3. O se usa la otra toma, o el clip se re-encuadra como P1 corto (piso 17,5 s) y **se declara que el banco no tiene control sub-umbral**. |

Hay **dos** masters de P3 (`take1` 22,3 s y `take2` 21,6 s): medir el transitorio en
los dos y quedarse con el más corto. Es la única escena del banco donde el criterio
de selección es un número y no la calidad de imagen.

**4. Lo único realmente atado es la SUMA `evento + cola`, no el reparto.**

El piso A1 compara `duration_ms` contra `start_ms + 14 000` (CR-01) o `+ 25 000`
(CR-02). Desarrollando `D = pre-roll + evento + cola` y `start_ms = pre-roll`, el
pre-roll **se cancela de los dos lados**:

```
evento + cola  ≥  14,0 s   (CR-01)
evento + cola  ≥  25,0 s   (CR-02)
```

Es la forma más útil del gate, y aclara qué es libre y qué no:

- **Al gate no le importa si ese tiempo es infracción o cumplimiento.** Un hold de
  9 s con 5 s de cola (14 s) pasa igual que uno de 11 s con 3 s (14 s). Un evento
  corto **se rescata alargando el corte final**, sin cambiar de toma.
- **Pero el evento tiene su propio mínimo, y ese no se compensa con nada:** **8 s
  para CR-01 y 12 s para CR-02** (spec 43 §3.1). Y el ideal metodológico es más
  exigente: que el evento cubra hasta `onset + t_alert_upper` (10 s / 20 s), para que
  una **alerta lenta pero válida caiga dentro de la infracción real** y no después de
  que la persona ya se corrigió.
- **El pre-roll no participa de esta cuenta.** Sube el piso de `D` uno a uno (caso 1)
  porque corre el onset, pero no cambia un segundo lo que hace falta *después* del
  onset. Las dos afirmaciones son la misma cuenta vista desde los dos lados.

**Traducido a la práctica:** de las tres piezas del clip, **una está fijada por
convención** (pre-roll 3,5 s), **una viene dada por la toma y no se puede inventar**
(el evento: se elige toma, no se edita), y **una es la palanca libre** (la cola / el
corte final). La cola es lo que se ajusta para cerrar la desigualdad — y es
exactamente lo que hacen las recetas de P2, P6 y P8.

**Nota hermana, misma lógica, en P8:** la separación en dos episodios la produce la
**ausencia del track** (cuando la persona sale de cuadro no hay atributo que evaluar,
y el intervalo se cierra), así que el GT va a tener 2 episodios casi sin importar
cuánto dure la salida. El que necesita los **2 s de `resolve`** para separarlos es el
**motor**: con una ausencia más corta emite una sola alerta, que matchea un solo
episodio, y **el otro se cuenta como perdido**. Con una ausencia de ≥5 s como pide el
guion no hay problema; si en la toma real salió más corta, el clip mide la
segmentación en contra y **eso se declara como hallazgo, no se arregla re-recortando**.

---

## 5. La ficha de eventos: ¿hace falta?

### 5.1 Veredicto

**Sí, y es bloqueante del recorte** — pero no es la ficha que estaba planeada.

La hoja de registro del doc 69 §8 estaba pensada para llenarse **durante** el rodaje,
con el operador anotando en el momento. Eso no ocurrió: el registro sistemático del
día quedó en los sidecars y en los artefactos de las corridas, y la **verdad de campo
sobre qué EPP estaba puesto y cuándo hubo que reconstruirla preguntándole al actor**
esa misma noche (doc 71 §2.3). Ese camino ya no está disponible para 35 tomas y no
sería confiable si lo estuviera.

Lo que se necesita ahora es una ficha **reconstruida por inspección visual del
material**, con cuatro funciones concretas:

1. **Es literalmente el input de la herramienta de recorte.** Recortar es marcar
   los instantes de transición. No hay forma de cortar sin conocer esos números; la
   única pregunta real es si se anotan o se pierden apenas usados. Desde 2026-07-26
   la consola ya acepta las **cuatro** marcas de P6 y P8 y guarda sus onset/end en
   el `episode_draft` (§6.3), así que el dato ya no vive *solo* en la ficha para
   esos dos — pero la consola marca con precisión ±0,3 s (`video.currentTime`) y
   la ficha con ±0,1 s: para el GT esperado que se compara en el paso 9 de §6.2,
   la ficha sigue siendo la referencia fina.

2. **Sin ella, dos escenarios se recortaban mal y nada avisaba — ya no es así en la
   consola, pero la ficha sigue siendo la referencia de precisión.** Antes del
   2026-07-26, el piso A1 de P6 y P8 se calculaba sobre marcas intermedias (`t2` y
   `t3`) que el `.clip.yaml` no guardaba y la consola no validaba: la ficha era el
   único lugar donde el recorte de esos dos era falsable. Ahora la consola calcula
   y valida el piso sola con sus propias marcas (§4.6, §4.8). Lo que la ficha sigue
   aportando, y que la consola no reemplaza, es la precisión de ±0,1 s de esas
   mismas cuatro marcas, necesaria para construir el episodio esperado contra el
   que se compara el timeline de `derive_clip_gt.py` (punto 3 más abajo).

3. **Es el chequeo cruzado independiente contra CVAT.** El GT sale de CVAT, no de la
   ficha (§5.2). Pero cuando `derive_clip_gt.py` imprima su timeline, comparar
   `start_ms/end_ms` derivados contra la ficha detecta al instante los tres errores
   caros: anotar el clip equivocado, invertir un atributo (`has_helmet` en `true`
   donde va `false`), y dejar un tramo en `unknown` que parte un episodio en dos. Sin
   una expectativa escrita **de antemano**, esos tres errores pasan como GT válido.

4. **Le ahorra al anotador el barrido a ciegas.** Cada clip son 600–950 frames. Con
   las transiciones ubicadas al ±0,5 s, el trabajo en CVAT es corregir alrededor de
   3–4 instantes conocidos; sin ellas, es escanear el clip entero buscando dónde
   cambia el estado.

**Costo real:** ~15 clips × 2–4 marcas. Una tarde de trabajo cuidadoso, en la misma
pasada en que se elige la toma (§3.1) — porque para elegirla ya hay que mirar el
video igual. **No se hace para las 35 tomas: solo para las ~15 seleccionadas.**

### 5.2 Lo que la ficha NO es — y esto no es negociable

> **La ficha no es el ground truth. El GT sale de CVAT, frame por frame.**

El motivo es medible, no doctrinario: **la transición no es instantánea**. En las
corridas del rodaje, sacarse el chaleco tomó **1,07 s** (frames 249→281) y sacarse el
casco **2,5 s** (frames 251→325) — doc 71 §2.3. Una marca de ficha leída con el
reproductor tiene una incertidumbre del mismo orden que la transición que pretende
marcar, y esa diferencia es entre el 25 % y el 60 % del umbral de confirmación de
CR-01 (4 s). Un GT construido sobre marcas de reproductor mediría el reloj del
anotador, no el del sistema.

De ahí se derivan tres reglas:

- La ficha entra al `.clip.yaml` **solo** como `episode_draft`, campo que
  `derive_clip_gt.py` tolera y **no filtra al `clip_gt.v2`**. Es un borrador, y está
  bien que lo sea.
- El `clip_gt.v2` sale **siempre** de `corrected/<clip_id>.xml` (CVAT) vía
  `derive_clip_gt.py`. No hay atajo, y no lo va a haber.
- Discrepancia ficha ↔ GT **por debajo de 0,5 s**: normal, se ignora (es el mismo
  orden que `START_END_TOLERANCE_MS` del laboratorio). **Por encima de 1,0 s**: se
  investiga antes de promover el clip — o la ficha se leyó mal, o la anotación está
  mal, y las dos causas importan.

### 5.3 La convención de marcado (definirla una vez, aplicarla siempre)

Como la transición dura 1–2,5 s, **la convención decide hasta 2,5 s de episodio**.
Fijada acá, y la misma se usa en CVAT al resolver los atributos:

| Marca | Definición operativa |
|---|---|
| **Casco fuera** (onset CR-01) | Primer frame en que el casco **no toca la cabeza**. No cuando arranca el gesto. |
| **Casco puesto** (fin CR-01) | Primer frame en que el casco está **apoyado en la cabeza**, aunque todavía se lo esté acomodando. |
| **Chaleco fuera** (onset CR-02) | Primer frame en que el chaleco **no está sobre ninguno de los dos hombros**. |
| **Chaleco puesto** (fin CR-02) | Primer frame en que el chaleco está **sobre los dos hombros**, aunque esté sin cerrar. |
| **Sale de cuadro** (P8) | Primer frame **sin ninguna parte** del cuerpo en el encuadre. |
| **Vuelve a entrar** (P8) | Primer frame con el cuerpo **suficientemente visible como para anotar una caja**. |
| **Oclusión ini/fin** (P1-c, P2-c) | Primer/último frame en que el objeto tapa cabeza o torso. |

**Asimetría deliberada:** el onset se marca **tarde** (cuando el EPP ya está fuera) y
el fin **temprano** (apenas vuelve a su lugar). Eso hace el episodio **conservador**:
nunca le regala al sistema tiempo de infracción que no existió, que es el error que
inflaría el recall y acortaría el TTFD. Es la misma dirección de prudencia que el
borde inferior de la ventana de matching del evaluador.

### 5.4 Cómo leer las marcas

1. **Marcas de recorte** (`±0,3 s` alcanza): el reproductor del diálogo de recorte
   de la consola, con los botones propios de cada escenario (`casco_fuera` /
   `casco_puesto`, `chaleco_fuera` / `chaleco_puesto`, `tramo_inicio` /
   `tramo_fin`, o las 4 de P6/P8). Lee `video.currentTime`; la precisión la
   limita el seek del navegador, y para elegir `ss` sobra.

2. **Marcas de la ficha** (`±0,1 s`, y las 4 marcas de P6/P8): tira de miniaturas
   alrededor de la transición y refinamiento por frame.

   ```bash
   cd ~/projects/e-ovrt_datasets/datasets-videos/raw
   # 6 s alrededor de la transición, 4 fps, en una sola imagen 6x4
   ffmpeg -y -v error -ss 12 -i P6-a-take2.mp4 -t 6 \
          -vf "fps=4,scale=320:-1,tile=6x4" -frames:v 1 /tmp/tira.png
   # y el frame exacto una vez ubicado
   ffmpeg -y -v error -ss 14.75 -i P6-a-take2.mp4 -frames:v 1 /tmp/f.png
   ```

   Cada celda de la tira son 0,25 s: dos pasadas ubican cualquier transición con
   precisión de frame.

3. **Redondeo:** anotar con **un decimal**. A 30 fps del clip, 0,1 s = 3 frames, muy
   por debajo de la incertidumbre real de la transición. Más decimales es precisión
   inventada.

### 5.5 Formato de la ficha, por escenario

Un archivo único: **`e-ovrt_datasets/datasets-videos/docs/ficha-eventos-rodaje.md`**
(el laboratorio ya tiene ese directorio de docs, y se versiona con el repo — no son
media, son metadatos).

**Índice, una fila por clip del banco:**

```markdown
| clip_id  | master          | cám   | esc | dur master | ss    | D     | estado    |
|----------|-----------------|-------|-----|-----------:|------:|------:|-----------|
| a_p1_c01 | P1-a-take2.mp4  | OAK-D | P1  |     57,1 s | 12,3  | 20,6  | recortado |
| a_p2_c01 | P2-a-take1.mp4  | OAK-D | P2  |     48,5 s |  8,9  | 30,4  | pendiente |
```

**Y un bloque por clip con sus marcas.** La cantidad de marcas la fija el escenario:

| Escenario | Marcas obligatorias | Marcas opcionales |
|---|---|---|
| **P1**, **P7** | `casco_fuera`, `casco_puesto` | — |
| **P1-c**, **P2-c** | las de su escenario base | `ocl_ini`, `ocl_fin` |
| **P2** | `chaleco_fuera`, `chaleco_puesto` | `chaleco_visible_hasta` (si quedó en cuadro un rato) |
| **P3** | `casco_fuera`, `casco_puesto` (≈2 s) | — |
| **P4** | `casco_fuera`, `casco_puesto` | `sale_de_cuadro` (si sale antes del final) |
| **P5** | `ambos_en_cuadro`, `fin_tramo_limpio` | — (no hay evento) |
| **P6** | `casco_fuera`, `chaleco_fuera`, `chaleco_puesto`, `casco_puesto` | — |
| **P8** | `casco_fuera`, `sale_de_cuadro`, `vuelve`, `casco_puesto` | — |
| **P9** | `sujeto_completo_en_cuadro`, `fin_accion` | — |

Formato de cada bloque:

```markdown
### a_p6_c01 — master `P6-a-take2.mp4` (OAK-D, 71,0 s) — escenario P6

| # | marca             | t (s) | condición | nota                              |
|---|-------------------|------:|-----------|-----------------------------------|
| 1 | casco_fuera       |  15,4 | CR-01     | onset ep. casco                   |
| 2 | chaleco_fuera     |  18,6 | CR-02     | onset ep. chaleco (+3,2 s)        |
| 3 | chaleco_puesto    |  39,1 | CR-02     | fin ep. chaleco                   |
| 4 | casco_puesto      |  42,3 | CR-01     | fin ep. casco                     |

Recorte: ss = 15,4 − 3,5 = **11,9** · onset_CR02_rel = 3,5 + 3,2 = **6,7 s**
D = máx( (42,3−15,4)+6,5 = 33,4 ; 6,7+26,0 = 32,7 ) = **33,4 s**
Episodios esperados en el GT: CR-01 [3500, 30400] · CR-02 [6700, 27200] (ms, ±500)
Cuadro limpio: sí · Chaleco fuera de cuadro durante el hold: sí
```

**Las dos últimas líneas son el corazón de la ficha**: los episodios esperados en ms
son la expectativa escrita **antes** de anotar, contra la que se compara el timeline
que imprime `derive_clip_gt.py`. Sin eso, la ficha es un registro; con eso, es un test.

---

## 6. El procedimiento, de punta a punta

### 6.1 Por cada clip (≈20 min sin contar CVAT)

1. **Elegir la toma** con los criterios de §3.1. Si es DVR, pasar antes por §3.3.
2. **Leer las marcas** (§5.4) y **escribir el bloque de ficha** (§5.5), incluidos
   `ss`, `D` y los episodios esperados. **Antes de recortar** — la ficha es el input,
   no el acta.
3. **Recortar desde la consola** (§2.3), leyendo el warning de piso que devuelve
   (y el de objetivo de guion, si el escenario tiene uno cargado — §4.10). El
   piso ya se valida sola para los nueve escenarios; igual conviene tener la
   tabla de §4.10 al lado para entender **por qué** salió el `D` que salió.
4. Si por algún motivo se recorta con el script directo (§2.2), **verificar el
   piso A1 a mano** con la tabla de §4.10: ahí sí nada lo va a avisar hasta
   `derive_clip_gt.py` (paso 8).
5. **Chequear el `info.json`**: `duration_ms` coincide con la `D` planeada (±1 frame),
   `fps: 30`, resolución 1920×1080.
6. **Revisar el `.clip.yaml`**: si se usó el script, escribirlo (§6.3); si se usó la
   consola, verificar `scenario`, `source_id` y anotar los desvíos del
   `episode_draft` que siguen siendo espurios por diseño (P3: no es un episodio
   real; P5: no hay evento). P2 ya no necesita esta salvedad — desde 2026-07-26
   se marca el fin real y el `episode_draft` que escribe la consola es correcto.

### 6.2 Después, por tanda

7. **Pre-anotar** (media-plane, GDINO-base + ByteTrack) y **anotar en CVAT** siguiendo
   el protocolo del laboratorio. Los atributos `has_helmet`/`has_vest` arrancan en
   `unknown` a propósito: **un radio sin tocar nunca debe fabricar una violación**.
8. **Derivar el GT:**
   ```bash
   cd ~/projects/e-ovrt_datasets
   python3 datasets/scripts/videogt/derive_clip_gt.py \
       --xml datasets-videos/corrected/<clip_id>.xml \
       --clip-yaml datasets-videos/<clip_id>.clip.yaml \
       --info datasets-videos/clips/<clip_id>.info.json \
       --out datasets-videos/gt/<clip_id>.json
   ```
   El default de `--pattern-set` (CR-01=4000, CR-02=7000) ya está alineado con
   `cr01_cr02_v2`. **No pasar otro** salvo que la corrida del banco use otro.
9. **Comparar el timeline impreso contra los episodios esperados de la ficha.**
   Δ ≤ 0,5 s se ignora; Δ > 1,0 s se investiga antes de promover (§5.2).
10. **Cero `dimensioning_warnings` en `provenance`.** Si aparece uno, el recorte falló:
    volver a cortar desde el master (que nunca se toca) y **regenerar** el clip con el
    mismo `clip_id` — la consola invalida sola la pre-anotación vieja renombrándola a
    `.stale`, porque son cajas de un video que ya no existe.
11. **Validar y promover:**
    ```bash
    python3 datasets/scripts/bench/validate_clip_gt.py --gt-dir datasets-videos/gt/
    python3 datasets/scripts/bench/promote_clip.py --clip-id <clip_id>
    ```
12. **Correr el banco en DBE** (experimentos `media_first`, replay por ambos planos) y
    `evaluate-alerts`. En DBE el fps no importa: se procesa a la velocidad que haga
    falta y la medición va sobre timestamps de media (doc 71 §7.1 paso 4).

### 6.3 Plantilla del `.clip.yaml`

Desde 2026-07-26 esta es también la forma que escribe la consola sola (P6, P8:
2 entradas en la lista; el resto de los escenarios: 1 entrada). `episode_draft`
es una **lista**, cada elemento con su `condition`; y `warnings` pasó a ser una
clave de **primer nivel** del YAML, ya no anidada dentro de `episode_draft`. Si
se recorta con el script directo (§2.2), hay que escribir el YAML a mano con
esta misma forma:

```yaml
# Recortado con prepare_clip.sh: --ss 11.9 --to 33.4 --fps 30
# Marcas y episodios esperados: docs/ficha-eventos-rodaje.md
# La cola es larga a propósito: el piso A1 del episodio CR-02 (onset 6,7 s + 25 s)
# gobierna la duración.
clip_id: a_p6_c01
block: A               # rodaje propio guionado
scenario: P6
source_id: a_p6_c01    # el evaluador matchea alert.source_id == episode.source_id
level: scene
master: raw/P6-a-take2.mp4
episode_draft:         # BORRADOR — la verdad sale de CVAT — lista, una entrada por episodio
  - condition: CR-01
    onset_ms: 3500
    end_ms: 30400
  - condition: CR-02
    onset_ms: 6700
    end_ms: 27200
warnings: []           # clave de primer nivel, no anidada en episode_draft
```

> **`source_id` es el campo que carga el peso.** El evaluador cruza
> `alert.source_id == episode.source_id`. Si no coincide con el `ingest.config.source_id`
> de la corrida del banco, **ninguna alerta matchea con ningún episodio**: todas
> cuentan como falsos positivos, todos los episodios como perdidos, y los resultados
> salen catastróficos por culpa de un string. Mantener `source_id = clip_id`.

---

## 7. Deuda detectada al escribir esto (no bloquea, va a la lista)

**Resuelto el 2026-07-26** (ver la nota de actualización al principio del doc):
lo que sigue son los cuatro puntos tal como estaban detectados el 07-26 por la
mañana, con la resolución real anotada al lado de cada uno.

1. ~~La consola no tiene parámetro de cola.~~ **Resuelto**: `SCENARIO_TAIL_S`
   (3,0 s default, 5,0 s P2, 10,0 s P4) — la consola ya no fuerza a usar el
   script ni a corromper el `episode_draft` corriendo la marca de fin.
2. ~~`SCENARIO_TARGET_S` no cubre P4, P6, P7 ni P8.~~ **Parcialmente resuelto**:
   el **piso A1** ahora se valida en los nueve escenarios (`piso_s()`), que era
   la parte peligrosa (el silencio leído como validación). El **objetivo de
   guion** sigue sin cargarse para P4/P6/P7/P8 — pero eso ya no es un agujero,
   porque esos cuatro escenarios no tienen un target de guion definido en primer
   lugar: lo único que tienen que cumplir es el piso, y ese ya se avisa.
3. ~~El diálogo de recorte acepta un solo par de marcas.~~ **Resuelto**: P6 y P8
   ahora piden sus 4 marcas directamente en el diálogo, con botones que se
   habilitan en orden cronológico; llamar al camino de 2 marcas con P6/P8 es un
   error explícito.
4. ~~No hay validación del piso A1 en el momento del recorte.~~ **Resuelto**: la
   consola evalúa `piso_s()` (espejo de `DIMENSIONING_MS`) al momento de
   recortar, no recién al derivar el GT. El warning llega antes de gastar el
   trabajo caro de CVAT.
5. **`prepare_clip.sh` no aplica `--scale`** desde la consola: los clips quedan en
   1080p. Correcto para anotar, pesado para mover; a considerar si CVAT se sirve
   desde otra máquina. (Sin cambios — sigue pendiente.)

---

## 8. Los cinco números de este documento

1. **~15 clips** del Bloque A, en 3 tandas — la primera (11 clips) ya cumple el
   mínimo de composición de doc 57 §6.4.
2. **`onset + 14 s` (CR-01) y `onset + 25 s` (CR-02)**: los dos pisos que decide el
   gate A1. Todo el §4 es aritmética sobre esos dos números.
3. **P6 ≈ 32,5 s y P8 ≈ 31,5 s** — los dos clips que el recorte por cobertura
   *cortaría* **2–3 s demasiado corto**, censurando en silencio justo el episodio
   que los justifica. Hasta el 2026-07-25 nada avisaba de esto; desde el
   2026-07-26 la consola calcula estos dos números sola (§4.6, §4.8) y avisa por
   piso si el recorte quedara corto.
4. **1,07 s y 2,5 s**: lo que tardaron, medidos, sacarse el chaleco y el casco en el
   rodaje. Es la razón por la que la ficha **no puede ser** el GT, y por la que la
   convención de marcado (§5.3) hay que fijarla antes de anotar.
5. **±0,5 s**: la tolerancia con la que la ficha y el GT de CVAT tienen que coincidir.
   Por encima de 1,0 s hay un error real, y siempre es uno de los tres caros: clip
   equivocado, atributo invertido, o un tramo en `unknown` partiendo un episodio.
