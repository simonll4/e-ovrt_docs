# 84 — Réplica con `gdino-base-560`: Nivel A (Fase D) + campaña T2 de clips

- **Fecha:** 2026-08-04 (madrugada, cadena nocturna encadenada al doc 83).
- **Qué es:** la variante que el pre-registro deja abierta (`nucleo/04` §7: *"modelo
  GDINO-tiny como baseline; **opcional repetir con GDINO-base**"*) más el item 2 del
  doc 82 (campaña de clips con el especialista). Un solo servicio, dos campañas
  secuenciales: `datos/84-cadena-base560.sh`, reanudable.
- **Estado:** **COMPLETO.** Nivel A 18/18 corridas y T2 34/34 clips, ambos con 0
  errores (~2 h de GPU en total). **Sin commitear.**

## 1. La pregunta que responde el Nivel A

El doc 83 dejó abierta una duda que condiciona cómo se lee todo el eje de la tesis:
**¿la debilidad de E-DIR es de la estrategia o de la capacidad del modelo?**
`gdino-base-560` es el candidato ideal para responderla — es el modelo grande y, según
el doc 64, el **especialista en `bare_head`** (recall CR-01 0,599 vs 0,308 del
campeón). Si la formulación directa fallaba por falta de capacidad del text encoder,
acá tenía que mejorar.

## 2. Resultado — F1 en la mitad B, tiny vs base

| Corte | Brazo | tiny-560 | base-560 | Δ |
|---|---|---|---|---|
| `shel5k`/CR-01 | E-IND | 0,546 | 0,496 | −0,050 |
| | `cr01_obs` | 0,188 | 0,167 | −0,020 |
| | `cr01_neg` | 0,123 | 0,162 | +0,039 |
| | `cr01_spec` | 0,097 | 0,096 | −0,001 |
| `bench_obra`/CR-01 | E-IND | 0,408 | 0,400 | −0,008 |
| | mejor E-DIR | 0,189 | 0,189 | 0,000 |
| `bench_obra`/CR-02 | E-IND | 0,479 | **0,583** | **+0,104** |
| | mejor E-DIR | 0,418 | 0,351 | −0,067 |

### El gate, replicado

| Corte | ratio tiny | ratio base | ¿<50%? |
|---|---|---|---|
| `shel5k`/CR-01 | 0,34 | **0,34** | sí |
| `bench_obra`/CR-01 | 0,46 | 0,47 | sí |
| `bench_obra`/CR-02 | 0,87 | 0,60 | no |

**El veredicto no cambia: el gate no se dispara, E-DIR pasa a la Fase 2.**

## 3. Hallazgos

### F-84.1 — La debilidad de E-DIR es estructural, no de capacidad del modelo
En `shel5k` (n grande) el ratio E-DIR/E-IND es **0,34 con los dos modelos, idéntico
hasta el segundo decimal**. El modelo grande y especialista en `bare_head` **no acorta
la brecha**: sus variantes directas se mueven ±0,04 y el mejor E-DIR de `bench_obra`
queda clavado en 0,189. La limitación de la formulación directa **no se compra con
capacidad** — es del modo de expresar la condición, que es exactamente lo que el eje
de la tesis fue a medir. Es el resultado más fuerte del carril: una conclusión que
sobrevive al cambio de modelo.

### F-84.2 — La especialidad del modelo no se transfiere a la estrategia que la usaría
`gdino-base-560` es el especialista `bare_head`, y `cr01_obs` ("person with bare head
on construction site") es la variante que más se le parece — sin embargo **empeora**
(0,188 → 0,167). Detectar mejor la clase `bare_head` con una etiqueta corta no implica
responder mejor a una frase que la describe: son dos regímenes distintos del encoder
de texto. Refuerza F-83.1 (el vocabulario es parte de la inferencia).

### F-84.3 — base-560 sí mueve E-IND, y en la dirección que el doc 64 predecía
E-IND CR-02 sube +0,104 (0,479 → 0,583): base es el especialista `vest` (doc 64,
vest AP 0,582) y E-IND es la estrategia que consume esa evidencia. En CR-01 baja
levemente en los dos estratos. **La elección de modelo mueve a E-IND; la elección de
formulación mueve a E-DIR** — cada palanca actúa sobre su carril.

### F-84.4 — Lo medido con n grande replica; lo medido con n chico, no
| Medición | estrato | tiny | base | ¿replica? |
|---|---|---|---|---|
| ratio del gate | `shel5k` (2487+) | 0,34 | 0,34 | **sí** |
| complementariedad | `shel5k` | 18,5% | 17,6% | **sí** |
| corroboración TP/FP | `shel5k` | 2,4× | **3,0×** | **sí** |
| complementariedad | `bench_obra`/CR-02 (48) | 18,8% | 2,6% | **no** |
| corroboración CR-02 | `bench_obra` (34/26) | invertida | correcta | **no** |

Es la validación empírica del caveat de n del doc 83 §4, y **obliga a la corrección de
F-83.7** (ver abajo).

## 4. Corrección a F-83.7 (doc 83)

La primera versión del hallazgo afirmaba que *"la corroboración se invierte en CR-02"*
y de ahí derivaba que el `corroboration_factor` de -and **tenía** que ser por
condición. **La inversión no replicó**: base-560 da la dirección correcta en CR-02
(50% TP vs 36% FP, contra 71%/88% de tiny). Se midió sobre 34 TP y 26 FP de un solo
estrato.

Lo que queda en pie:
- **CR-01: la corroboración discrimina**, replicado y reforzado (2,4× → **3,0×**).
  Acelerar la confirmación por corroboración es seguro para casco.
- **CR-02: sin evidencia concluyente en ninguna dirección.** La recomendación correcta
  no es "apagar -and en CR-02" sino **medir la corroboración por condición antes de
  fijar el factor**.

## 5. E-HYB-or bajo el otro modelo

| Corte | E-IND | E-HYB-or | Δ |
|---|---|---|---|
| `bench_obra`/CR-01 | 0,400 | 0,338 | −0,062 |
| `bench_obra`/CR-02 | 0,583 | 0,542 | −0,041 |
| `shel5k`/CR-01 | 0,496 | 0,328 | −0,168 |

Igual que con tiny: **-or no supera a E-IND en Nivel A con ningún modelo**. La
predicción registrada (sube recall, baja precisión) se confirma por segunda vez. Su
adopción se decide en Fase 2 sobre F1 de alertas (§8.3), donde la histéresis del motor
puede filtrar parte del ruido — es la única vía que le queda abierta.

## 6. Campaña T2 (clips) — completa

`gdino-base-560` × `cr01_cr02_v2_short` × pattern set v2 × escena, DBE stride=1, los
34 clips del banco. 34/34 sin errores, ~104 min (base-560 es ~2× más lento por frame
que tiny). Mismo evaluador que T1 (`c1cbb56`) → **directamente comparable sin
re-evaluar**.

### Agregado

| Métrica | T1 (tiny-560) | T2 (base-560) |
|---|---|---|
| Recall micro | **0,824** (28/34) | 0,735 (25/34) |
| Precision micro | **0,757** | 0,676 |
| F1 | **0,789** | 0,704 |
| `t_alert-system` | 5.327 ms | **4.899 ms** |
| TTFD | **168 ms** | 221 ms |
| SDR | 0,698 | **0,819** |
| Negativos | 0 FP de 4 | **0 FP de 4** |

### Por escenario y condición

| Esc. | T1 | T2 | | Cond. | T1 SDR | T2 SDR | T1 t_alert | T2 t_alert |
|---|---|---|---|---|---|---|---|---|
| P1 | 1,000 | **0,818** | | CR-01 | 0,805 | 0,804 | 4.314 ms | 4.364 ms |
| P2 | 1,000 | 1,000 | | CR-02 | **0,281** | **0,920** | 8.572 ms | **6.417 ms** |
| P4 | 1,000 | 1,000 |
| P6 | 1,000 | 1,000 |
| P7 | 0,400 | 0,400 |
| P8 | 0,500 | 0,500 |
| P9 | **0,600** | **0,400** |

### F-84.5 — F-81.2b queda refutada **para la palanca "cambiar de modelo bajo `v2_short`"**

La hipótesis del doc 81 era que los missed de P7/P9 venían de **mis-detección de casco
en el pre-roll** y que el especialista CR-01/`bare_head` (doc 64) los recuperaría.
**No los recupera**: P7 clavado en 0,400, P8 en 0,500 y **P9 empeora** (0,600→0,400),
con los FP de CR-01 subiendo de 8 a 11.

**Mecanismo, clasificado contra el GT** con `datos/85-mecanismo-de-fallas.py` (la
taxonomía del doc 81 §5, ahora herramienta reproducible en vez de análisis a mano):

| Tipo | T1 (tiny) | T2 (base) |
|---|---|---|
| `prematura_pre_roll` | 5 | **6** |
| `cruzada_de_condicion` | 4 | 4 |
| `sin_episodio_activo` | 0 | 2 |
| **total inesperadas** | **9** | **12** |
| adelanto de las prematuras (mediana) | **0,5 s** | **1,8 s** |

**Lo que cambia no es tanto el conteo como la magnitud.** Las prematuras pasan de 5 a
6 —un caso— pero su adelanto mediano se **triplica**: de 0,5 s (la mayoría rozando la
tolerancia de 500 ms) a 1,8 s, con cuatro de las seis entre 1,7 y 2,3 s. Con tiny las
alertas caían *al filo* del borde de matching; con base caen claramente adentro del
tramo que el anotador marcó como "cumple". **base-560 no reduce el pre-roll: lo
profundiza** — ve *menos* cascos en esos primeros segundos, coherente con su E-IND
CR-01 más débil en el Nivel A (F-84.3). Los FP cruzados de condición quedan **idénticos
en 4** (la firma de granularidad de F-81.2a no depende del modelo, como corresponde).

La regresión de P1 (1,000→0,818) son 3 alertas: una prematura marginal de +0,2 s
(apenas fuera de la tolerancia) y dos fuera de todo episodio — no un colapso de
percepción.

> **✎ Corrección 2026-08-04.** La primera versión de esta sección decía "en T1 la misma
> taxonomía daba ~3–4 prematuras" y describía 1 tardía; los números salían de una
> inspección a ojo. La clasificación sistemática da **5** prematuras en T1 (no 3–4) y
> reclasifica la "tardía" de `a_p1_c02` como `sin_episodio_activo`. La conclusión
> (base empeora el pre-roll) se sostiene, pero **por la magnitud del adelanto, no por
> el conteo** — que se mueve en un solo caso.

**Alcance de la refutación — el hallazgo de la revisión crítica.** La "especialidad
CR-01" del doc 64 se midió con `evaluate_cr01`, que puntúa **detecciones de
`bare_head`** ("Estrategia E1: detectar bare_head") sobre el prompt set
`cr01_cr02_bench_v2` de 4 clases. **T2 corrió `v2_short` (person/helmet/vest, sin
`bare_head`): nunca ejercitó la capacidad por la que base es especialista.** Lo
refutado es la palanca "cambiar el modelo manteniendo el prompt set desplegado". La
vía **`bare_head` como evidencia positiva de la violación** — donde base tiene recall
0,599 vs 0,308 de tiny, la separación más grande medida entre los dos modelos — sigue
**sin probar a Nivel B**, porque el motor solo tiene `spatial_absence`
(`required_absent_class`): consumir evidencia positiva de condición exige el evaluador
`direct_evidence`. Es la MISMA pieza que necesita la Fase 2 de E-DIR.

Junto con F-81.2a, el déficit de P7–P9 queda fuera del alcance de un cambio de modelo
bajo el prompt set actual. Las palancas restantes: `track_id`/G1 (doc 79) y **evidencia
directa** (frases E-DIR o etiqueta `bare_head`, ambas vía `direct_evidence`).

### F-84.6 — El modelo sí compra percepción de chaleco; la plataforma cobra menos tiempo

CR-02 pasa de SDR **0,281 a 0,920**: la evidencia intermitente que F-81.1 midió (~1 de
cada 6 frames) se vuelve prácticamente continua, y `t_alert` baja **8.572 → 6.417 ms**
(−2,2 s). Como el recall de CR-02 ya era 1,000 en T1 —rescatado por la histéresis— la
mejora **no podía aparecer en el recall**: aparece en calidad de evidencia y latencia.

Es el complemento exacto de F-81.1 y el par de hallazgos se lee junto: **la histéresis
rescata una percepción pobre, y un modelo mejor la elimina como problema — dos
palancas independientes sobre el mismo cuello de botella.** El precio se paga en
CR-01 (recall global 0,824 → 0,735, P1 1,000 → 0,818), coherente con el Nivel A, donde
el E-IND CR-01 de base también salía peor (F-84.3).

**Ninguna campaña gana en todo**: tiny-560 sigue siendo el campeón por F1 agregado y
base-560 es el mejor para CR-02. Eso es el dato, no un empate a desempatar.

## 7. Trampa nueva

11. **Un runner reanudable con salida fija "salta" una réplica entera.** La clave de
    reanudación de `83-fase-d-nivel-a-runner.py` es `(arm, variant, stratum)` y no
    incluye el modelo — que vive en el proceso del servicio (`EOVRT_MODEL_REF`), no en
    el runner. Correr la réplica con el mismo `--out-dir` habría reportado "ya hecho"
    18 veces y devuelto los números de tiny con etiqueta de base. Se agregó
    `--out-dir` y la cadena apunta a `datos/84-*`. Emparenta con D-61.4: **la
    procedencia del modelo no está en los artefactos, hay que declararla.**
