# 87 — E-HYB-or a Nivel B: la fusión refutada, y por qué

- **Fecha:** 2026-08-04.
- **Qué es:** la última rama del pre-registro que quedaba viva sobre el banco del
  rodaje. ADR-001 la fijó como **rama experimental de primera clase** ("E-HYB-or/and
  se corren en la Fase 2 **siempre**"), y el doc 12 §4.3 registró la predicción a
  contrastar: *"sube recall de alertas, baja precisión; la histéresis temporal filtra
  parte del ruido extra"*.
- **Estado:** 34/34 clips, **sin GPU**, 0,4 min. Suites verdes.

## 1. Cómo se corrió: dual-run, y por qué eso importa

El pre-registro (doc 12 §4.1) **prohíbe** el pase único de vocabulario unión: en GDINO
el vocabulario es parte de la inferencia, así que un caption con las 5 clases daría
señales distintas de las de T1 y D1 y la comparación dejaría de ser de variable única.
La fusión se hace sobre las corridas **ya existentes** — corolario operativo: **E-HYB
a Nivel B no consume GPU**, solo replay.

Que el fundamento no es teórico está **medido**: `person`, con la frase idéntica
`"person"`, produce **729 cajas en T1 y 731 en D1** para `a_p1_c09` (1.095 vs 1.317 en
`a_p2_c01`) — el resto del caption cambia la inferencia del sujeto.

`merge_dual_run.py` (11 tests) fusiona frame a frame: del stream E-IND entra todo (así
`spatial_absence` ve exactamente lo de T1 y su evidencia es bit a bit la misma), del
E-DIR solo las clases de evidencia directa — sus `person` se descartan para no duplicar
sujetos. Falla fuerte ante desalineación de frames, timestamps o `source_id`: alinear a
ciegas cruzaría evidencia de clips distintos en silencio, la misma familia de trampa
que el mtime del doc 82 y el export de CVAT.

**Desviación declarada y medida.** El gating por persona usa entonces los sujetos del
stream E-IND, no los del E-DIR con los que se gatearon en D1 (en el sistema fusionado
hay una sola fuente de sujetos, coherente con §4.3: E-IND es la señal primaria). Sobre
los 34 clips: de **5.943** hits directos gateados en D1, **5.897 siguen gateando** con
las personas de T1 = **99,2%**. La desviación afecta al **0,8%** de los hits. Medida,
no supuesta.

## 2. Resultados

| Métrica | T1 (E-IND) | D1 (E-DIR) | **H1 (hyb_or)** |
|---|---|---|---|
| Recall micro | **0,824** | 0,176 | **0,353** |
| Precision micro | **0,757** | 0,146 | 0,255 |
| F1 | **0,789** | 0,160 | **0,296** |
| SDR | 0,698 | 0,210 | **0,738** |
| TTFD | 168 ms | 847 ms | **113 ms** |
| FP | 9 | 35 | 35 |
| Negativos | **0/4** | 2/4 | 2/4 |

| Esc. | T1 | D1 | H1 |
|---|---|---|---|
| **P1** | **1,000** | 0,091 | **0,000** |
| P2 | 1,000 | 0,000 | **1,000** |
| P4 | 1,000 | 0,500 | 0,000 |
| P6 | 1,000 | 0,000 | 0,500 |
| P7 | 0,400 | 0,000 | 0,400 |
| P8 | 0,500 | 0,000 | 0,000 |
| P9 | 0,600 | 0,800 | 0,600 |

## 3. F-87.1 — La predicción pre-registrada queda REFUTADA

La predicción decía **"sube recall, baja precisión"**. La precisión bajó, como se
esperaba (0,757 → 0,255). Pero **el recall NO subió: se derrumbó** (0,824 → 0,353).
La fusión no se comporta como una unión.

El criterio de adopción del §8.3 (superar a la mejor individual por ≥0,05 de F1) no
está ni cerca: 0,296 contra 0,789. **E-HYB no es núcleo**, y queda documentada como
variante comparativa con sus números (§8 criterio 4: nada se tira).

## 4. F-87.2 — Por qué: la unión de evidencia NO es monótona en un motor temporal

Este es el hallazgo, y explica el resultado entero.

En una clasificación por frame, un OR solo puede **agregar** positivos: el recall no
puede bajar. Pero la plataforma no clasifica frames, **confirma episodios**: hay una
ventana de persistencia y una ventana de matching. Agregar evidencia **más temprana**
no agrega una alerta: **corre la que ya existía**. Y una alerta que se adelanta fuera
de la ventana cuenta doble mal — el episodio va a `missed` **y** la alerta a
`unexpected`.

La firma es inequívoca. Los **11 clips de P1** confirman en H1 a **~4,0 s exactos**
(4,0 / 4,0 / 4,1 / 4,1 / 4,0 / 4,5 / 4,0 / 4,0 / 4,0 / 4,0 / 4,0): eso es
`confirm_after_ms = 4000` contado **desde el frame 0**, porque la evidencia directa
está presente desde el primer frame. Con E-IND sola, esos mismos clips confirmaban a
`onset + 4,0 s` ≈ 7,6 s absolutos, **dentro** de la ventana. Resultado: P1 pasa de
**recall 1,000 con 0 FP** a **0,000 con 12 FP**, sin que la percepción haya empeorado.

De hecho **la percepción mejoró**: SDR sube (0,698 → 0,738) y TTFD baja (168 → 113 ms).
La fusión gana en las métricas de percepción y pierde en las de alerta con los mismos
datos — otra confirmación de F-85.4 (el Nivel A no predice el Nivel B), ahora dentro de
una sola campaña.

**Es el tercer filo de F-85.3.** La histéresis rescata evidencia débil pero correcta
(F-81.1), amplifica evidencia fuerte pero equivocada (D1), y ahora se ve que evidencia
equivocada **temprana** no solo agrega falsas alarmas: **canibaliza las alertas
correctas**, adelantándolas fuera de su ventana.

## 5. F-87.3 — Predicción sobre `hyb_and`, antes de implementarla

`hyb_and` no cambia *quién* dispara: su único efecto declarado (doc 12 §4.3) es
**acelerar la confirmación** — reducir la ventana por `corroboration_factor` cuando la
mayoría de los hits están corroborados. Pero F-87.2 acaba de mostrar que **adelantar la
confirmación es exactamente el mecanismo de falla** en este banco.

**Predicción registrada aquí, antes de gastar el esfuerzo:** sobre el banco del rodaje,
`hyb_and` empeoraría el recall respecto de E-IND sola, y más cuanto mayor sea la
corroboración — porque los clips tienen pre-roll guionado de ~3 s y la corroboración de
CR-01 es alta (58% de los TP, F-83.7). Con `corroboration_factor: 0.5` la ventana de
CR-01 caería a 2.000 ms y las alertas se adelantarían otros 2 s dentro del pre-roll.

### ✎ 2026-08-05 — el argumento es más fuerte: el experimento sería un artefacto de medición

Al cerrar D-90.4 se verificó cómo el evaluador deriva la ventana de matching, y eso
convierte la predicción en algo más duro que "saldría peor".

El borde inferior de la ventana es **`persistencia_min_ms` con `origin:
gt_provenance`** — o sea, la persistencia **nominal** del pattern set (4.000 ms CR-01 /
7.000 ms CR-02) con la que `derive_clip_gt` construyó los episodios. El evaluador **no
sabe** que `hyb_and` acorta la ventana en runtime.

Consecuencia: con `corroboration_factor: 0.5`, el motor confirmaría a `onset + 2.000 ms`
mientras la ventana recién abre en `onset + 4.000 ms`. La alerta cae **antes** del borde
⇒ el episodio cuenta `missed` **y** la alerta `unexpected`: el doble castigo de F-EV2,
ahora por construcción. Y el efecto es perverso: **cuanto mejor funcione la
corroboración —cuanto más acelere— peor puntúa**. Eso no mide la fusión, mide el
desacople entre el motor y el GT.

Para medirla de verdad harían falta una de dos cosas, y **las dos rompen la
comparabilidad** que sostiene toda la serie:

- **regenerar el GT** con la persistencia acortada → deja de ser el mismo GT que las 6
  campañas ya corridas;
- **hacer al evaluador consciente de la corroboración** (ventana efectiva por episodio)
  → cambia el evaluador con el que se midieron T1, T2, D1, H1, B1 y G1.

Ambas cuestan más que el cambio del motor. **`hyb_and` no se ejecuta**: no por falta de
tiempo, sino porque **el experimento tal como está pre-registrado no es medible contra
este banco sin invalidar el resto de la serie**. Sigue siendo una idea viva para
material sin pre-roll guionado o con un evaluador corroboration-aware — queda como
trabajo futuro con su predicción y su condición de medición escritas, que es la salida
que el pre-registro contempla (§6.2: *"lo no corrido se reporta no ejecutada con
causa"*).

**Decisión del usuario 2026-08-05 (D-90.4): aceptada.**

## 6. Mecanismo de las alertas inesperadas

| Tipo | T1 | D1 | H1 |
|---|---|---|---|
| `prematura_pre_roll` | 5 | 14 | **20** |
| `cruzada_de_condicion` | 4 | 8 | **14** |
| `sin_episodio_activo` | 0 | 12 | 3 |
| adelanto mediano | 0,5 s | 2,5 s | 2,6 s |

## 7. Con esto, el eje de la tesis queda cerrado

Las tres estrategias del pre-registro corridas de punta a punta, sobre el mismo banco,
mismo GT, mismo motor y mismos timings:

| Estrategia | F1 de alertas | Veredicto |
|---|---|---|
| **E-IND** | **0,789** | **Núcleo** (ADR-001, confirmado por medición) |
| E-DIR | 0,160 | Descartada — veto de precisión del §8 (0,146 < 0,5) |
| E-HYB-or | 0,296 | No supera a la mejor individual (§8.3) |

Y las tres fallas están **explicadas por mecanismo**, no solo cuantificadas: ceguera al
atributo de la formulación directa (Nivel A, 54% de sus FP sobre gente que cumple), su
amplificación por la histéresis (D1), y la no-monotonía de la unión en un motor temporal
(H1). Eso es lo que convierte los números en conclusiones.
