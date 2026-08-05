# 96 — El costo del tiempo real: el banco a la densidad de evidencia del camino live

- **Fecha:** 2026-08-05.
- **Qué es:** la campaña que faltaba para que el eje **DBE ↔ EBE** esté medido en los
  dos escenarios y no en uno solo. Seis campañas nuevas (R1–R6) sobre el mismo banco
  de 34 clips, mismo GT, mismo evaluador: tres densidades de evidencia × dos
  granularidades.
- **Estado:** 6/6 campañas 34/34 clips, cero fallos de guard. ~27 min de GPU.
  **Sin commitear.**
- **Marco de lectura (doc 81 §1):** cada número es el rendimiento medido de UNA
  combinación. El contraste entre combinaciones ES el experimento; nada de esto es
  una nota de aprobación.

---

## 1. El hueco que esta campaña cierra

Las seis campañas del banco del rodaje (T1, T2, D1, H1, B1, G1 — docs 81/84/85/87/88/89)
corrieron **todas** `path: DBE`, `stride: 1`: **30 inferencias por segundo de video**,
32.182 frames sobre 17,9 min de material.

El camino live no puede sostener esa densidad, y está medido:

| Fuente | fps procesados | Descarte |
|---|---|---|
| GDINO live, rodaje 2026-07-25 (doc 71 §2.1) | **1,16 / 1,51 / 1,76** | 92–94% |
| Ídem, mañana vs noche (doc 71 §4) | 2,62 (13:33) → 1,16 (20:10) | degradación térmica 2,4× |
| Techo de esta máquina tras F-RT5 (doc 73) | **3,75–4,42** | — |

O sea: **todo el resultado del banco se midió con ~7 a 25× más evidencia por segundo
de la que el camino en tiempo real entrega.** El propio doc 71 lo señala y lo deja
pasar (*"Acá el fps NO importa: DBE procesa a la velocidad que sea"*). Cuánto de ese
rendimiento sobrevive a la restricción de tiempo real **no estaba medido en ninguna
parte del trabajo** — y es exactamente la diferencia entre haber evaluado el escenario
DBE y haber evaluado el EBE.

Lo que del lado EBE sí estaba medido es **funcional** (paridad replay↔stream
byte-idéntica, `bus_dropped_events: 0` en todas las corridas, humos verdes — docs
37/65/67/91) y **de latencia** (g2a p95, deltas de confirmación — doc 71). Ninguna
métrica de calidad contra GT. Esta campaña la aporta.

## 2. Método: variable única, densidad de evidencia

Tres densidades, cada una anclada a una medición real del camino live, no elegidas
a ojo:

| Campaña | `stride` | fps equivalentes | Ancla |
|---|---|---|---|
| R1 / R2 | 7 | **4,29** | el techo de HOY (3,75–4,42, doc 73) |
| R3 / R4 | 15 | **2,00** | el rango que EFECTIVAMENTE corrió en vivo (1,16–2,62, doc 71) |
| R5 / R6 | 26 | **1,15** | el PEOR caso medido (1,16 fps a las 20:10, doc 71 §4) |

Todo lo demás es idéntico a las referencias: modelo campeón `gdino-tiny-560`, prompt
set congelado `cr01_cr02_v2_short` (`df81fd48…`), pattern set oficial (4000/7000), el
banco `gt_ready` de 34 clips (manifest `cef5082e…`) y el mismo evaluador. Las pares
son T1 (escena, 30 fps) y G1 (sujeto, 30 fps).

**Qué mide y qué no.** Mide el efecto de ver menos frames por segundo sobre la
percepción y sobre el motor temporal. **No** mide latencia operativa ni integridad del
bus: eso vive en los humos EBE y en la caracterización de fps. El decimado es regular
y el descarte live es irregular (jitter) — diferencia declarada, no disimulada.

### Dos guards, porque acá es fácil medir otra cosa sin enterarse

1. **Que el stride efectivamente rija.** Si no se aplicara, la campaña mediría T1
   creyendo medir tiempo real y nada lo delataría (la lección del `no_track_id` de G1).
   Se verifica por partida doble y por clip: `run_descriptor.rate_control.stride` de
   la corrida declara el stride que rigió, y el conteo de unidades procesadas lo
   confirma independientemente contra `ceil(n_frames/stride)`. **34/34 en las seis
   campañas.**
2. **Que las referencias sean comparables.** T1 (08-03 23:02) y G1 (08-04 19:08) se
   evaluaron antes de `5327080` (08-04 16:38), que cambió el despacho de evaluadores y
   toca `_positive_flags_for_source` — el que deriva SDR/TTFD. Contrastar contra
   números producidos por otro evaluador mezclaría densidad con versión del código.
   **Verificado que no ocurre**: re-correr replay + `evaluate-alerts` con el código de
   hoy sobre las mismas detecciones de T1 reprodujo sus **34 evals idénticos campo a
   campo** (`datos/96-verificar-comparabilidad-t1.py`). De paso queda demostrado que
   el camino de replay es determinista a través de una semana de cambios del motor.

## 3. Resultados

| Campaña | Gran. | fps ev. | Recall | Prec. | **F1** | t_alert | TTFD | SDR | FP neg. |
|---|---|---|---|---|---|---|---|---|---|
| **T1** | escena | 30,00 | 0,824 | 0,757 | **0,789** | 5.327 ms | 168 ms | 0,698 | 0/4 |
| **R1** | escena | 4,29 | 0,794 | 0,794 | **0,794** | 5.623 ms | 572 ms | 0,718 | 0/4 |
| **R3** | escena | 2,00 | 0,706 | 0,774 | **0,738** | 4.846 ms | 870 ms | 0,736 | 0/4 |
| **R5** | escena | 1,15 | 0,618 | 0,677 | **0,646** | 5.360 ms | 1.463 ms | 0,719 | 0/4 |
| **G1** | sujeto | 30,00 | 0,971 | 0,892 | **0,930** | 5.236 ms | 168 ms | 0,698 | 0/4 |
| **R2** | sujeto | 4,29 | 0,853 | 0,879 | **0,866** | 5.635 ms | 572 ms | 0,718 | 0/4 |
| **R4** | sujeto | 2,00 | 0,824 | 0,933 | **0,875** | 4.981 ms | 870 ms | 0,736 | 0/4 |
| **R6** | sujeto | 1,15 | 0,676 | 0,821 | **0,742** | 5.577 ms | 1.463 ms | 0,719 | 0/4 |

### Por escenario (regla L5: nunca solo el agregado)

| esc. | T1 | R1 | R3 | R5 | G1 | R2 | R4 | R6 |
|---|---|---|---|---|---|---|---|---|
| P1 | 1,00 | 1,00 | 1,00 | 0,73 | 1,00 | 1,00 | 1,00 | 0,73 |
| **P2** | 1,00 | **0,60** | **0,20** | **0,20** | 1,00 | **0,60** | **0,20** | **0,20** |
| P4 | 1,00 | 1,00 | 1,00 | 1,00 | 1,00 | 1,00 | 1,00 | 1,00 |
| **P6** | 1,00 | **0,50** | 0,50 | 0,50 | 1,00 | **0,50** | 0,50 | 0,50 |
| P7 | 0,40 | 0,60 | 0,40 | 0,40 | 1,00 | 0,80 | 1,00 | 0,80 |
| P8 | 0,50 | 0,50 | 0,50 | 0,50 | 1,00 | 1,00 | 1,00 | 0,50 |
| **P9** | 0,60 | **1,00** | **1,00** | **1,00** | 0,80 | **1,00** | **1,00** | **1,00** |

(P3 y P5 son negativos: **0 FP en las ocho campañas**.)

## 4. Hallazgos

### F-96.1 — El costo del tiempo real es bajo hasta ~4 fps, y no es uniforme

A **4,29 fps —el techo real de hoy— el agregado de escena no se degrada de forma
detectable**: F1 0,794 contra 0,789 de T1 a 30 fps (+0,005; IC 95% bootstrap
[−0,120, +0,132] — ver §4.1). Pero el agregado plano **esconde una redistribución**,
no una ausencia de efecto: P2 se derrumba de 1,000 a 0,600 y P6 de 1,000 a 0,500,
mientras P9 sube de 0,600 a **1,000 con 2 FP menos** y P7 de 0,400 a 0,600. Es el
caso de manual para la regla L5.

A partir del techo de hoy, las estimaciones puntuales del agregado degradan
monótonamente con la densidad (0,794 → 0,738 → 0,646; desde T1 el primer paso es
+0,005, no una caída), pero **con n = 34 episodios ninguno de esos deltas de escena
excluye el cero por sí solo** (§4.1); el único costo
individualmente significativo es el del peor caso bajo sujeto (R6−G1: −0,188,
IC [−0,334, −0,040]). La señal firme del costo no está en el agregado: está en el
mecanismo por escenario — el derrumbe de P2 (1,000 → 0,600 → 0,200) es consistente,
direccional y tiene causa identificada (F-96.2).

### F-96.2 — Lo primero que se rompe es el rescate de la histéresis (F-81.1)

CR-02 es la condición que vive de que el patrón temporal acumule una percepción
intermitente: SDR 0,281 y recall 1,000 a 30 fps, el argumento pro-plataforma del
doc 81. **Es lo primero que cae**: P2 pasa de 1,000 a 0,600 a 0,200. Con menos
muestras de una evidencia que ya era escasa, el patrón deja de llegar al umbral.

Es un límite preciso de F-81.1, no su refutación: **la histéresis rescata percepción
intermitente sólo mientras la cadencia alcance para muestrearla.** Y no lo arregla la
identidad — P2 se comporta igual bajo escena y bajo sujeto, porque es un problema de
percepción, no de atribución.

### F-96.3 — La densidad reducida filtra evidencia espuria temprana

P9 (confusables) **mejora** de 0,600 a 1,000 y sus FP caen de 2 a 0; los FP de CR-01
bajan de 8 a 6. Coherente con F-87.2 (la evidencia temprana equivocada corre las
alertas correctas fuera de su ventana): ver menos frames es ver también menos de los
frames que engañan. Es un efecto real, medido en los dos sentidos.

### F-96.4 — La ganancia de la identidad sobrevive al tiempo real, y es significativa a TODA densidad

El resultado central del tramo, en su forma que aguanta escrutinio: **la ventaja de
la granularidad por sujeto sobre la de escena, a la MISMA densidad, excluye el cero
en las cuatro densidades medidas** (bootstrap pareado por clip, IC 95% — §4.1):

| densidad | Δ F1 (sujeto − escena) | IC 95% |
|---|---|---|
| 30,00 fps (G1−T1) | +0,141 | [+0,032, +0,258] |
| 4,29 fps (R2−R1) | +0,072 | [+0,013, +0,145] |
| 2,00 fps (R4−R3) | +0,137 | [+0,032, +0,258] |
| 1,15 fps (R6−R5) | +0,096 | [+0,011, +0,202] |

Es la única palanca del banco cuya ganancia es estadísticamente distinguible a la
densidad que el camino live entrega hoy. Y el mecanismo se verificó, no se supuso:
la sospecha era que el tracker IoU se fragmentara con frames a 231–858 ms (cada
fragmento tendría que sostener los 4 s por su cuenta), pero **los tracks totales no
explotan** (154 a stride 1 → 103/91/105 a strides 7/15/26). La identidad se
mantiene coherente; la caída de R6 es densidad, no fragmentación. (Matiz: la
tolerancia del tracker se mide en frames, así que en tiempo de pared se vuelve MÁS
tolerante a stride alto — juega a favor.)

La comparación vistosa —**G1 a 4,29 fps (0,866) rinde mejor que T1 con las 30 fps
completas (0,789)**— queda como **estimación puntual**: +0,077 con IC [−0,071,
+0,229], que no excluye el cero con n = 34. Se reporta como observación consistente
con el hallazgo, no como hallazgo.

La lectura de tesis no cambia: **una palanca de motor gratis (CPU, un flag de
configuración) rinde una mejora significativa a toda densidad, mientras que 7× más
frames —que exigen hardware que esta máquina no tiene— no producen un delta
distinguible en el agregado.** El margen del sistema no estaba en el modelo, estaba
alrededor del modelo.

### F-96.5 — El `t_alert` agregado que "no se mueve" es un artefacto de composición (✎ corregido en revisión adversarial)

TTFD crece linealmente con el paso de muestreo (168 → 572 → 870 → 1.463 ms): en
tiempo real se detecta hasta 1,3 s más tarde, y es inevitable — no se puede detectar
más rápido que la propia cadencia. El `t_alert` agregado, en cambio, parece quieto
(5.327 → 5.623 → 4.846 → 5.360 ms) — y la primera versión de este doc lo leyó como
"la histéresis amortigua el costo". **Esa lectura era un artefacto de supervivencia,
y la revisión adversarial lo midió**: el promedio de `t_alert` solo cuenta episodios
que alertaron, y a baja densidad los episodios lentos (los CR-02 difíciles, con
t_alert 8,6 s) mueren como `missed` — su salida del denominador tira el promedio
hacia abajo justo cuando el costo real sube.

Restringiendo a los clips donde ambas campañas igualaron `matched` (supervivientes
comunes, aproximación declarada): **t_alert crece +1.251 ms a 4,29 fps, +685 a
2 fps, +1.175 a 1,15 fps.** El costo del tiempo real en el tiempo de alerta es
real, del orden de +0,7 a +1,3 s — consistente con F-81.3 (`t_alert ≈ persistencia
+ TTFD`) más la cuantización de la confirmación al paso de muestreo.

El hallazgo que queda es doble: (a) el costo operativo en tiempo de alerta a la
densidad de hoy es ~1 s sobre una política de 4–7 s — acotado y declarable; (b) el
`t_alert` agregado **no es comparable entre densidades sin control de
supervivencia**, hermano del F-96.6. Dos artefactos de instrumento cazados en la
misma campaña, ambos antes de reportar al informe.

### F-96.6 — El SDR no es comparable entre cadencias (artefacto de medición)

El SDR **sube** al bajar la densidad (0,698 → 0,718 → 0,736), lo que leído ingenuamente
diría "el detector mejora cuando mira menos". Es falso, y se midió por qué:
`_sdr_for_episode` funde tramos separados por un hueco ≤ paso nominal, y el paso
nominal es la mediana de gaps de la fuente. A 30 fps el paso es 33 ms y un parpadeo de
100 ms deja hueco visible; a 2 fps el paso es 500 ms y ese mismo parpadeo desaparece
dentro de la tolerancia.

Decimando **las mismas detecciones de T1** (`datos/96-sdr-efecto-instrumento.py`), sin
cambiar una sola caja:

| stride | SDR sólo por el instrumento | SDR medido en campaña | Residual = percepción |
|---|---|---|---|
| 7 | +0,019 | +0,020 | **+0,001** |
| 15 | +0,039 | +0,038 | **−0,001** |
| 26 | +0,022 | +0,021 | **−0,001** |

**La subida es ~100% instrumento y ~0% percepción.** El SDR es válido *dentro* de una
cadencia y deriva por construcción *entre* cadencias. Familia F-EV1/2/3 (doc 81 §3):
un artefacto de medición hallado antes de reportar, no después.

Corolario para el informe: **las comparaciones de SDR del banco entre campañas de
distinto stride deben llevar esta corrección o no hacerse.** Las seis campañas
previas comparten `stride: 1`, así que **ninguna conclusión anterior se ve afectada**.

### F-96.7 — El control de negativos aguanta a toda densidad

**0 FP sobre los 4 clips negativos en las ocho campañas.** Con 4 clips esto es un
control comparativo, no una cota (D-90.1) — pero el dato direccional es limpio: la
restricción de tiempo real no introduce falsas alarmas en material de cumplimiento
(y a menos frames, menos oportunidades de FP: el control es más fácil a baja
densidad, se declara).

### 4.1 Verificación adversarial de los hallazgos (bootstrap pareado)

Los cuatro hallazgos de arriba se sometieron a revisión adversarial ANTES de pasar
al informe (`datos/96-critica-verificacion.py`): bootstrap pareado por clip
(la unidad correcta — los episodios dentro de un clip están correlacionados y las
ocho campañas comparten los mismos 34 clips), 10.000 resamples, semilla fija 96.

| contraste | ΔF1 obs. | IC 95% | ¿excluye 0? |
|---|---|---|---|
| R1 − T1 (escena, 4,29 vs 30 fps) | +0,005 | [−0,120, +0,132] | no |
| R3 − T1 (escena, 2,00 vs 30 fps) | −0,050 | [−0,174, +0,077] | no |
| R5 − T1 (escena, 1,15 vs 30 fps) | −0,143 | [−0,309, +0,033] | no |
| R2 − G1 (sujeto, 4,29 vs 30 fps) | −0,064 | [−0,163, +0,039] | no |
| R6 − G1 (sujeto, 1,15 vs 30 fps) | **−0,188** | **[−0,334, −0,040]** | **SÍ** |
| G1 − T1 (sujeto vs escena, 30 fps) | **+0,141** | **[+0,032, +0,258]** | **SÍ** |
| R2 − R1 (sujeto vs escena, 4,29 fps) | **+0,072** | **[+0,013, +0,145]** | **SÍ** |
| R4 − R3 (sujeto vs escena, 2,00 fps) | **+0,137** | **[+0,032, +0,258]** | **SÍ** |
| R6 − R5 (sujeto vs escena, 1,15 fps) | **+0,096** | **[+0,011, +0,202]** | **SÍ** |
| R2 − T1 (cruzada: sujeto@4,29 vs escena@30) | +0,077 | [−0,071, +0,229] | no |

La estructura que emerge es nítida y es la que el doc reporta: **los deltas de
densidad dentro de una granularidad no se distinguen del cero** (salvo el peor caso
bajo sujeto), **y los deltas de granularidad a densidad fija se distinguen del cero
en las cuatro densidades.** Lo que esta campaña puede afirmar con respaldo es lo
segundo; lo primero se reporta como estimación puntual con su mecanismo por
escenario. La verificación también corrigió F-96.5 (supervivencia) y confirmó la
coherencia del tracker (F-96.4).

## 5. Qué NO dice esta campaña

- **No es una corrida por el bus.** Mide la densidad de evidencia del camino live
  sobre el camino DBE. La integridad del acople (`bus_dropped_events`, cierre 1:1) y
  la latencia operativa siguen viniendo de los humos EBE (docs 37/65/67/91), que están
  verdes. Una campaña EBE de punta a punta sobre los 34 clips queda como trabajo
  ubicado, no ejecutado.
- **El decimado es regular; el descarte live es irregular.** El live descarta según lo
  que el consumidor pueda tomar, con jitter. El efecto de esa irregularidad no está
  medido.
- **R4 supera a R2** (0,875 vs 0,866) pese a tener la mitad de densidad. Con IC de
  ±0,10–0,15 sobre estos deltas (§4.1), eso es ruido, no una inversión: se declara,
  no se explica.
- **n chico por escenario.** P2 son 5 episodios, P6 son 2: los saltos de esos
  escenarios son direccionales, no cuantitativos.
- **Los deltas de densidad del agregado no excluyen el cero** (§4.1) — ni siquiera
  R5−T1 (−0,143). El costo del tiempo real sobre el agregado de escena queda como
  tendencia monótona de estimaciones puntuales con mecanismo identificado (P2), no
  como efecto establecido. Lo establecido es la ganancia de la identidad a densidad
  fija.

## 6. Qué cambia en el estado del trabajo

- El eje **DBE ↔ EBE pasa de estar medido en un escenario a estarlo en dos** en lo
  que respecta a calidad contra GT — vía proxy de densidad sobre DBE, con las
  diferencias contra el live declaradas (§5).
- La afirmación **"G1 es la mejor combinación del banco" sobrevive al tiempo real**,
  en su forma verificada: su ventaja sobre escena excluye el cero en las cuatro
  densidades (§4.1) y el tracker no se fragmenta. La comparación cruzada (R2 > T1)
  queda como estimación puntual consistente.
- La conclusión de **F-81.1 gana un límite declarado**: la histéresis rescata
  percepción intermitente mientras la cadencia alcance para muestrearla.
- Aparecen **dos correcciones de lectura** que el informe debe llevar: el SDR no se
  compara entre cadencias (F-96.6) y el `t_alert` agregado no se compara entre
  densidades sin control de supervivencia (F-96.5).

## 7. Dónde está cada número

- Campañas: `e-ovrt_experimental-setup/results/clip_bench/r{1..6}_gdinotiny560_v2short_*`
  (`campaign.yaml` + `metrics.json` + `evals/` + `provenance.json`).
- Runners y evidencia cruda: `datos/96-costo-tiempo-real-runner.py`,
  `96-costo-tiempo-real-sujeto.py`, `96-rt-stride{7,15,26}[-subject]/`.
- Guards y contrastes: `96-verificar-comparabilidad-t1.py`,
  `96-sdr-efecto-instrumento.py`, `96-contraste-tiempo-real.py` (+ `.json`).
- Revisión adversarial (bootstrap, supervivencia, fragmentación):
  `96-critica-verificacion.py` (+ `.json`).
- Tabla comparativa del banco: `results/clip_bench/index.md`.
