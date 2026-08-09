# 104 — Ajustar la plataforma al estrato B: alternativas probadas y sus resultados

**Fecha:** 2026-08-06. **Insumo:** el diagnóstico por capas del doc 103 §7. **Salida:**
dos ejes de ajuste probados **con configuración existente** (ADR-015 intacto: ninguna
capacidad nueva), con sus números, sus límites y dos hallazgos que no se esperaban.

**La pregunta que responde:** ya sabemos *por qué* se rompe (doc 103). ¿Qué se puede
**hacer al respecto sin salir del alcance**, y hasta dónde alcanza?


> ## ⚠️ CORRECCIÓN POSTERIOR — leer antes que nada (2026-08-07, doc 108 §6)
>
> Este documento se escribió cuando el GT de **`v06_c01` tenía un episodio CR-02**
> (342.400–355.533 ms). La revisión visual en CVAT determinó que **era un error de
> anotación: la persona SÍ llevaba chaleco**. El episodio **no existe**; `v06_c01` es
> **negativo** (P5) y pasó a ser **el primer clip soak del banco**.
>
> **Qué NO cambia (todo el análisis de mecanismo de este doc):** la evidencia perpetua
> del modo escena, la fragmentación del tracker, el colapso de la asociación de `vest`
> con la escala, el acople alucinación↔supresión. Todo eso se midió sobre las
> **detecciones**, que no cambiaron.
>
> **Qué SÍ cambia:** los conteos que tratan a `v06_c01` como clip positivo. Sus alertas
> ya no son "el episodio que el motor no encontró" sino **falsas alarmas sobre un
> negativo**. Cifras vigentes: `results/clip_bench/index.md` y doc 108 §6.


---

## 1. El punto de partida que reencuadra todo: el gate ya existía

El doc 103 §7.3 simuló un "gate de juzgabilidad" filtrando detecciones a mano, y lo
presentó como una mejora *candidata*. Al ir a implementarlo apareció que **no hacía
falta implementar nada**:

```yaml
# configs/patterns/cr01_cr02_v2.yaml — pattern set OFICIAL, ya en producción
evidence:
  min_subject_confidence: 0.35
  min_absent_class_confidence: 0.25
  min_subject_area_px: 400.0      # <-- el gate, y está en 400
```

`spatial_absence.py` (el evaluador de CR-01/CR-02) ya lo aplica:
`(detection.area_px or 0.0) >= pattern.evidence.min_subject_area_px`.

**400 px² son ≈20×20 px: es "prácticamente sin gate".** No es un descuido — es el
valor correcto para el régimen en el que se calibró, el rodaje, donde la mediana de
altura de `person` es 716–839 px (≈100.000 px² de área). Ahí el gate nunca se
activa porque nunca hace falta.

> **F-104.1 — el problema no era una capacidad faltante sino un parámetro sin
> re-calibrar.** La plataforma expone el knob correcto; lo que faltaba era medirlo
> fuera del régimen para el que se eligió. Esto cambia el estatus del ajuste: es
> **configuración**, cabe entero dentro de ADR-015, y no abre ninguna puerta.

## 2. Eje A — barrido del gate (`min_subject_area_px`)

Variable única; todo lo demás intacto (timings 4000/7000, regiones, confianzas,
modelo, prompts). Cero inferencia nueva: reusa las detecciones de I1 y los streams
trackeados de I2. Runner: `datos/104-barrido-gate-runner.py`; salida en
`datos/104-barrido-gate/`.

**Punto de operación declarado ANTES de mirar métricas de alerta:** el gate se fija
donde la curva de percepción medida (doc 103 §7.1) cruza el 50% de asociación de
`vest` — banda 160–220 px ⇒ H=160 px ⇒ con el aspect ratio mediano medido
(w/h = 0,411 en `v06_c01`) ≈ **10.500 px²**. Los valores 6.000 y 16.500 son
sensibilidad a cada lado, no candidatos.

### 2.1 Granularidad `subject` — funciona, y no alcanza

| `min_subject_area_px` | recall | precision | F1 | FP (positivos) | FP (negativo) |
|---|---|---|---|---|---|
| **400** (oficial, = I2) | 1,000 | 0,010 | 0,020 | 196 | 20 |
| 6.000 | 1,000 | — | — | 173 | 14 |
| **10.500** (punto declarado) | **1,000** | **0,015** | **0,029** | **133** | **7** |
| 16.500 (sensibilidad) | 1,000 | 0,025 | 0,049 | 77 | 4 |

**Los 2 episodios reales sobreviven a todos los umbrales** — el gate no cuesta recall.
Y el control de negativos mejora fuerte: `v10_c01` pasa de 20 FP a 7 (declarado) o 4.

Pero la conclusión honesta es la del doc 103 §7.3, ahora por el camino real de
configuración en vez de por simulación: **el gate convierte "inutilizable" en
"malo"**. Precision 0,015 en el punto declarado. Y **no hay margen para subir más**:
el violador real de `v06_c01` mide 216 px de mediana (GT humano) ≈ 19.200 px² — a
16.500 px² ya está a un paso del borde. **El violador vive en la misma escala que el
ruido**, que es exactamente lo que hace a este régimen difícil y no un problema de
umbral.

### 2.2 Granularidad `scene` — el gate EMPEORA los FP, y el porqué es el hallazgo

| `min_subject_area_px` | recall | FP total | FP en `v06_c01` |
|---|---|---|---|
| 400 (oficial, = I1) | 0,000 | 7 | **3** |
| 6.000 | 0,000 | 8 | 3 |
| 10.500 | 0,000 | 13 | **8** |
| 16.500 | 0,000 | 17 | **14** |

Contraintuitivo, así que fui a los `alerts.jsonl` crudos en vez de reportarlo:

```
v06_c01, scene, gate 400   →  3 alertas:  CR-01 4,6s · CR-02 7,0s · CR-01 357,3s
v06_c01, scene, gate 16500 → 14 alertas:  CR-01 6,3s · CR-02 7,0s · CR-01 en
                              27, 111, 137, 163, 207, 216, 229, 250, 295, 318, 331, 341 s
```

> **F-104.2 — el bajo conteo de FP del modo escena era un ARTEFACTO de su propia
> patología, no una virtud.** Sin gate, la evidencia es perpetua (siempre hay alguien
> "sin chaleco" en algún lado del plano): la condición **se engancha en un solo estado
> de violación y nunca resuelve**, así que emite UNA alerta y se calla 6 minutos. Al
> subir el gate, la evidencia se vuelve intermitente ⇒ la condición **resuelve y se
> re-arma** ⇒ cada re-arme emite una alerta nueva. Los 3 FP de I1 no eran "escena
> discrimina mejor": eran el latch tapando la cuenta.

Esto tiene una consecuencia metodológica que va más allá del estrato B: **comparar el
conteo de FP entre `scene` y `subject` es engañoso cuando la escena está capturada.**
En el rodaje la comparación era válida (la evidencia sí se interrumpe, con 1–5
personas); acá no. Es una advertencia de lectura, no una corrección de números
anteriores.

Y CR-02 **sigue emitiendo una sola vez a los 7,0 s incluso con gate 16.500**: siempre
queda al menos una persona grande sin chaleco detectado. Por eso el recall de escena
se queda en 0,000 en todo el barrido: **el gate no rescata al modo escena**. Refuerza
lo que el doc 103 ya decía: en este régimen el fix es `subject`, y no vale invertir en
re-armar escena.

## 3. Eje B — modelo `gdino-base-560` (I3/I4)

En curso al momento de escribir (~70 min de GPU: base es ~2× tiny, T2 midió 104 min
sobre 34 clips). Es la prueba directa de la **capa 1** del doc 103 §7: si el piso de
percepción es del `tiny` o de la familia. T2 ya había medido en el rodaje que base
sube el SDR de CR-02 de 0,281 a 0,920 — y la raíz del desastre acá es exactamente el
recall de `vest`.

Se mide lo mismo que a tiny, para que sea comparable: la **curva de asociación por
altura de sujeto** (el instrumento del doc 103 §7.1) además de las métricas de alerta.
Predicción pre-registrada: la curva sube en la banda 160–320 px; **la incógnita real
es la nocturna** (`v04_c01`, donde tiny da 55% incluso a ≥320 px).

Resultados y su lectura: **§5, cuando termine.**

## 4. Lo que estos ajustes NO pueden arreglar

Queda dicho para que el informe no prometa de más:

- **El piso de percepción.** Ningún parámetro del control-plane inventa un chaleco que
  el detector no vio. El gate solo evita *opinar* sobre sujetos no juzgables.
- **La noche.** Los 9 FP de `v04_c01` **no se mueven con ningún valor del gate** (9 en
  los 4 umbrales): son de iluminación, no de tamaño. El gate es un instrumento de
  escala y la noche es otro eje.
- **La asimetría epistémica de fondo.** El gate es un *proxy* del estado `unknown`:
  descarta al sujeto no juzgable en vez de representar "no sé". El GT humano sí tiene
  `unknown` y `derive_clip_gt` lo respeta ("la incertidumbre nunca fabrica una
  violación"); el runtime lo aproxima por tamaño. Cerrar esa brecha de verdad **sería
  capacidad nueva y ADR-015 la deja fuera** — se declara como trabajo futuro con la
  evidencia de dirección que dan estos números.
- **La calibración es IN-SAMPLE.** El punto de operación se fijó con la curva del mismo
  estrato que motivó la hipótesis. Sirve para caracterizar mecanismo y sensibilidad,
  **no para declarar un umbral de producción** — eso exige clips frescos. Los 11 clips
  sin anotar del lote podrían darlos.

## 5. Resultados del Eje B — la predicción pre-registrada quedó REFUTADA

I3 (base-560, escena) corrió en 40,0 min (2,07× tiny, calza con el ~2× de T2); I4
(sujeto sobre las detecciones de I3) en 25 s. Artefactos en
`datos/104-i3-base-scene-clips` y `datos/104-i4-base-subject-clips`.

### 5.1 A nivel alerta: base NO rescata el estrato B

| campaña | recall | precision | F1 | FP pos. | FP neg. | SDR |
|---|---|---|---|---|---|---|
| I1 tiny · scene | 0,000 | 0,000 | — | 5 | 2 | **0,997** |
| **I3 base · scene** | **0,000** | 0,000 | — | 6 | 4 | **0,924** |
| I2 tiny · subject | 1,000 | 0,010 | 0,020 | 196 | 20 | 0,997 |
| **I4 base · subject** | **1,000** | **0,011** | **0,021** | 186 | 14 | 0,924 |

**El patrón de recall es idéntico** (escena 0/2, sujeto 2/2) y la precision no se
mueve (0,010 → 0,011). **El modelo más fuerte no cambia el resultado.**

> **F-104.3 — el piso de percepción del estrato B no es un problema de `tiny` vs
> `base`.** La predicción pre-registrada (§3) decía que la curva subiría en 160–320 px
> y que la incógnita era la nocturna. Salió peor que eso: **la curva no sube en la
> banda que importa en NINGÚN clip**, y en `v06_c01` el **SDR baja de 0,995 a 0,848**
> — base sostiene PEOR la detección del violador real. Esto no contradice a T2 (que
> midió base mejor en el rodaje, SDR CR-02 0,281→0,920): dice que **esa ventaja es
> específica del régimen del rodaje** y no transfiere a sujetos chicos.

Curva de asociación de `vest`, tiny → base, en las bandas que deciden:

| clip | 160–220 px | 220–320 px | ≥320 px |
|---|---|---|---|
| `v04_c01` (nocturno) | 8,7% → **9,1%** | 13,2% → **12,9%** | 55,1% → 70,8% |
| `v06_c01` (denso) | 57,0% → **42,8%** | 73,2% → **62,5%** | — |
| `v10_c01` | 51,9% → **0,2%** | 62,9% → **1,5%** | — |

Base solo mejora donde ya se veía bien (≥320 px en v04: +15,7 pts). **En v06 EMPEORA**
(−14 pts). Lo de v10 es otra cosa y se explica abajo.

### 5.2 `v10_c01` cambió de significado — y es el mejor caso del banco para el argumento epistémico

El derrumbe de v10 (tiny 3.376 detecciones `vest` → base **48**, 70×) obligó a mirar
el video, no el número. **`v10_c01` no es la misma clase de escena que v06**: es
instalación de fachada en altura, y los operarios llevan **arnés de seguridad y ropa
de trabajo común, no chalecos reflectantes** (verificado visualmente en frame).

Y lo que dice el GT humano de ese clip es lo más interesante de toda la jornada:

```
v10_c01 — has_vest por track (1.771 frames)
  track 0:  T=0     F=7     unknown=1764
  track 1:  T=0     F=0     unknown=1771
  track 2:  T=0     F=0     unknown=1771
  track 3:  T=1771  F=0     unknown=0
  track 4:  T=1683  F=0     unknown=88
  track 5:  T=0     F=0     unknown=1771
```

**El anotador humano, frente a las mismas imágenes, dijo "no sé" en ~85% de los
frames-sujeto.** El motor, frente a las mismas imágenes, emitió **20 alertas** (tiny,
sujeto). No es que el humano y la máquina discrepen sobre un hecho: **el humano tiene
un estado que la máquina no tiene.**

> **F-104.4 — `v10_c01` es la demostración limpia de la asimetría epistémica.** El
> doc 103 §7.4 la había inferido del mecanismo; acá está medida contra un GT humano
> que ejerció masivamente el `unknown`. Es el caso más citable del argumento, y no
> depende de la densidad (v10 tiene 6 personas) ni de la noche (es diurno):
> **depende sólo de la juzgabilidad.**

Y explica por qué comparar FP entre modelos acá es traicionero: tiny detecta 3.376
chalecos donde el humano no puede afirmar que los haya — es decir, **tiny probablemente
alucina chalecos, y esa alucinación le SUPRIME alertas CR-02** (un chaleco detectado
cancela la violación). Base casi no detecta ninguno y por eso emite el doble de FP a
escena (2→4). **El conteo de FP se movió por una razón que no tiene nada que ver con
acertar.** Corolario metodológico, hermano de F-104.2: comparar FP entre dos
configuraciones que fallan de maneras distintas no ordena calidad.

### 5.3 Qué queda de la tabla de alternativas

| alternativa | ¿qué prometía? | resultado medido |
|---|---|---|
| **Gate `min_subject_area_px`** (config existente) | filtrar sujetos no juzgables | **La mejor de las tres.** Sujeto: FP 196→133 (−32%) en el punto declarado, −61% en sensibilidad, **recall intacto**. Escena: la empeora (F-104.2) |
| **Modelo `base-560`** (config existente) | subir el recall de `vest` | **Refutada (F-104.3).** Recall idéntico, precision +0,001, SDR de v06 −0,147. Cuesta 2× de GPU |
| **Granularidad `subject`** (ya medida en I2) | recuperar el recall que escena pierde | **Confirmada**: 2/2 vs 0/2, replica F-89.1 sobre material real. Pero su precision es el problema, no la solución |

**La combinación menos mala del estrato B es `tiny` + `subject` + gate re-calibrado:**
recall 1,000, precision 0,015, FP negativos 20→7. Sigue sin ser operable, y el techo
está donde el doc 103 §7.3 lo puso: el violador real vive en la escala del ruido.

**✎ Composición de los FP contra los sub-umbral del GT** (cruce posterior, mismo día):
de los 187 FP de I2 en `v06_c01`, solo **28 (15%) coinciden con un transitorio real**
del GT (violación corta que el motor amplificó más allá de su duración real); **159
(85%) no tienen ninguna violación real cerca, ni siquiera sub-umbral** — son ausencia
fabricada por percepción pura. En `v10_c01`: 19/20 puros. Confirma que el flood no es
"el motor sobre-reaccionando a violaciones cortas reales" sino evidencia inventada.

## 6. Qué aporta esto a la tesis

1. **Convierte un resultado malo en un capítulo de ingeniería medida.** No es "la
   plataforma falló en obra real": es *detectamos el mecanismo, identificamos el knob
   que ya existía, lo re-calibramos con criterio declarado, medimos cuánto rinde
   (−32% FP en el punto declarado, −61% en sensibilidad, recall intacto), probamos la
   alternativa de modelo y la refutamos con número, y dijimos dónde topa*. Eso es
   exactamente el tipo de evidencia que el eje A1–A5 pide.
2. **F-104.1 es una lección de diseño citable**: los parámetros de una plataforma
   config-driven llevan implícito el régimen en el que se calibraron; mudar de régimen
   sin re-calibrar es un modo de falla silencioso. Y su corolario positivo: **la
   plataforma tenía la palanca correcta**, lo que valida el diseño config-driven.
3. **Dos correcciones de lectura que valen para todo el banco.** F-104.2 (el conteo de
   FP de escena está deprimido por su propio latch) y §5.2 (el conteo de FP se mueve
   por alucinación de la clase ausente, no por acertar): **el conteo de FP no ordena
   calidad entre configuraciones que fallan distinto**. Es una advertencia de lectura
   para la tabla del banco, no una corrección de números anteriores.
4. **F-104.3 acota una conclusión previa sin contradecirla.** T2 midió que base-560 es
   el especialista de CR-02 en el rodaje; acá se ve que **esa ventaja es específica del
   régimen** y no transfiere a sujetos chicos. El informe gana precisión: la
   recomendación de modelo va con su sobre de validez.
5. **F-104.4 le da al argumento epistémico su mejor evidencia.** `v10_c01`: el
   anotador humano dijo `unknown` en ~85% de los frames-sujeto y el motor emitió 20
   alertas sobre el mismo material. La brecha entre el GT (que honra la incertidumbre
   por diseño) y el runtime (que no la representa) deja de ser un argumento de
   arquitectura y pasa a ser **un número contra un GT humano**.
6. **Cierra el arco del estrato B sin ampliar alcance**: problema → diagnóstico por
   capas → tres alternativas probadas con configuración existente (una útil, una
   refutada, una confirmada-pero-insuficiente) → límite declarado → trabajo futuro
   nombrado con evidencia de dirección.
