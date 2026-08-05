# 98 — Conclusiones transversales: qué quedó demostrado, con qué respaldo

- **Fecha:** 2026-08-05.
- **Qué es:** el cierre del tramo de resultados. Cruza los **tres materiales**
  (imágenes, video, tiempo real) y los **dos escenarios** (DBE, EBE) para responder la
  pregunta del trabajo con el respaldo de cada afirmación explícito. **Es la conclusión
  de los resultados, no el informe** — el informe traduce esto a prosa.
- **Qué NO es:** un resumen. El doc 92 responde Q1–Q4 del plan maestro; los índices de
  `results/` traen las tablas. Acá se decide **qué se puede afirmar y con qué fuerza**,
  que es lo que un tribunal va a apretar.
- **Insumos:** `results/index.md` y sus 4 índices, docs 92 (Q1–Q4), 96 (tiempo real),
  97 (implementación), 83–89 (campañas), 71/73/91 (live).

---

## 1. La pregunta, y la respuesta en una línea

> *¿Qué rendimiento se obtiene hoy, en construcción civil, con detección
> open-vocabulary **sin entrenar**, expresando las condiciones de riesgo en lenguaje —
> y qué aporta la plataforma alrededor del modelo?*

**Respuesta corta:** la detección zero-shot alcanza para sostener una condición de
riesgo (CR-01) y no alcanza para la otra (CR-02), pero **la plataforma alrededor del
modelo cambia el resultado más que cualquier elección de modelo o de prompt** — y esa
ganancia sobrevive a la restricción del tiempo real.

**La cifra que lo condensa:** sobre el mismo banco, con **las mismas detecciones bit a
bit**, cambiar la granularidad del motor de escena a sujeto lleva el F1 de alertas de
**0,789 a 0,930**. Ninguna de las cuatro palancas de percepción o formulación probadas
(modelo, prompts, fusión, vocabulario nativo) se acercó.

## 2. Escala de afirmación — qué respaldo tiene cada cosa

La distinción que hay que sostener en la defensa. **No todo lo medido tiene el mismo
estatuto**, y decirlo es más fuerte que aplanarlo.

| # | Afirmación | Respaldo | Fuerza |
|---|---|---|---|
| AF-1 | La granularidad por sujeto mejora el F1 de alertas | ΔF1 +0,141, IC 95% [+0,032, +0,258]; y **excluye el cero en las 4 densidades** medidas | **Establecida** |
| AF-2 | E-DIR no sirve como núcleo | Veto pre-registrado de precisión (0,146 < 0,5); brecha F1 0,63; mecanismo identificado (ceguera al atributo, 54% de los FP) | **Establecida** (criterio fijado antes de correr) |
| AF-3 | `gdino-tiny-560` es el campeón | mAP50 1º en las dos escalas (147 y 6.477 imgs, 3 fuentes) | **Establecida** (robusta a la fuente) |
| AF-4 | Agregar una condición nueva no cuesta entrenar | 0 entrenamientos, 48 líneas, 9 min, `machinery` AP 0,662 zero-shot | **Establecida** (medida, no afirmada) |
| AF-5 | `gdino-base-560` es el especialista de CR-02/`bare_head` | recall CR-01 0,599 vs 0,308 (n=5.313); CR-02 SDR 0,281→0,920 | **Establecida** |
| AF-6 | La histéresis temporal rescata percepción intermitente | CR-02 recall 1,000 con SDR 0,281, pagando t_alert | **Establecida**, con límite (AF-7) |
| AF-7 | Ese rescate tiene un límite de cadencia | P2 cae 1,00 → 0,60 → 0,20 al bajar la densidad | **Establecida** direccionalmente (n=5 episodios) |
| AF-8 | El costo del tiempo real sobre el agregado | Estimaciones puntuales +0,005 / −0,050 / −0,143 — decrecientes a partir del techo de hoy, **pero ningún IC excluye el cero** | **Tendencia con mecanismo**, no efecto establecido |
| AF-9 | La fusión E-HYB-or no ayuda | Predicción pre-registrada refutada (recall 0,824→0,353), mecanismo F-87.2 | **Establecida** (refutación de predicción propia) |
| AF-10 | CR-02 a Nivel A | Un solo estrato, **IC solapados** | **No cerrada** — declarado |
| AF-11 | FAR/hora | Ninguna cota alcanzable sostiene afirmación | **Limitación**, no métrica (D-90.1) |

> **Regla que se aplicó y conviene decir en voz alta:** cuando la estimación puntual
> era vistosa pero el IC no excluía el cero, **se degradó la afirmación** en vez de
> reportarla como hallazgo. El caso testigo: "G1 a 4,29 fps supera a T1 con 30 fps"
> (0,866 vs 0,789) es una observación consistente, no un hallazgo — su IC es
> [−0,071, +0,229].

## 3. Los tres materiales, y qué aporta cada uno

Ninguno responde solo; el argumento vive en el cruce.

### Imágenes — el piso de percepción, y su asimetría

`bench_v3`, 6.477 imgs, 3 fuentes independientes. **mAP50 0,551** con el campeón. La
estructura del resultado importa más que el número: `person` y `helmet` sólidas
(0,77–0,89), `vest` la más débil de las positivas (0,55), `bare_head` fuerte **solo en
el especialista** (0,399 vs 0,133).

**Lo que este material demuestra:** que hay señal utilizable sin entrenar, y que la
señal **no es uniforme por clase** — lo cual predice exactamente dónde va a fallar la
cadena completa. Y lo predijo: CR-02 (que depende de `vest`) es la condición que se
rompe en video y la primera que muere bajo tiempo real.

**Lo que NO demuestra:** nada temporal. Un AP por imagen no dice si el sistema alerta.

### Video — dónde la plataforma se separa del detector

34 clips, 35 episodios, GT humano `gt_ready`. **13 campañas comparables.** Es el único
material donde se puede medir lo que el trabajo defiende, porque una alerta es un
fenómeno temporal.

**Lo que este material demuestra:** las tres capas del aporte de plataforma —
(1) la histéresis rescata percepción intermitente pero correcta; (2) es palanca de
doble filo, y se midió en los dos sentidos (D1 amplifica evidencia equivocada; F-87.2:
la unión de evidencia **no es monótona** en un motor temporal); (3) **la identidad es
la capa que más agrega**, y su ganancia es 100% del motor (SDR y TTFD idénticos hasta
el decimal).

### Tiempo real — la prueba de que no es un resultado de laboratorio

El plano que faltaba hasta el 2026-08-05. Cuatro sub-planos, medidos por separado:
integridad del acople (cerrado: `bus_dropped_events=0` siempre), latencia operativa
(GDINO fuera de presupuesto con causa, YOLOE dentro), techo de throughput
(diagnosticado: contención de GIL, F-RT3; una palanca aplicada, +18%) y **calidad bajo
restricción** (R1–R6).

**Lo que este material demuestra:** que la ganancia de la plataforma **no es un
artefacto de procesar 30 fps offline**. Es la respuesta a la objeción más obvia de una
defensa.

## 4. Las cuatro conclusiones transversales

### C1 — El margen del sistema está alrededor del modelo, no en el modelo

Es la tesis, y quedó medida. Sobre el mismo banco y las mismas detecciones:

| Palanca | Naturaleza | ΔF1 vs línea de base |
|---|---|---|
| **Granularidad (G1)** | **motor, CPU, un flag** | **+0,141** |
| Modelo (T2, base-560) | percepción, más GPU | −0,085 |
| Vocabulario nativo (B1) | percepción | −0,412 |
| Fusión (H1, hyb_or) | motor | −0,492 |
| Formulación (D1, E-DIR) | prompts | −0,629 |

La única palanca que mejoró la línea de base **no toca el detector**. Y las que sí lo
tocan, o no mejoran, o empeoran. Esto no dice que el detector sea irrelevante — dice
que **con el detector dado, lo que queda por ganar está en la capa que lo rodea**, que
es exactamente lo que una plataforma aporta.

### C2 — Especificar en lenguaje tiene un costo medido, y un modo de falla propio

**El costo:** 0 entrenamientos, 48 líneas de configuración, 9 minutos, 0 GT nuevo — y
la clase nunca configurada (`machinery`) da AP 0,662, **por encima del mAP agregado del
campeón sobre las clases que sí estaban configuradas**.

**El modo de falla, que es el aporte honesto:** la palabra tiene que alinear con la
taxonomía del despliegue. `vehicle` junto a `machinery` en el mismo caption da **0
detecciones** (inanición por solapamiento semántico); aislada da 118 cajas con AP 0,026
porque el 67% cae sobre lo que ese GT llama `machinery`.

La versión fuerte de A1 (`nucleo/09`) no es *"agregar una clase es gratis"* sino:
**agregar una clase cuesta minutos, y validar la palabra también** — con la diferencia
de que el bench lo expone en ~3 minutos, mientras que con un detector cerrado ese error
se descubre después de anotar y entrenar.

### C3 — El motor temporal es una palanca de doble filo, medida en los dos sentidos

Lo que le da valor a este hallazgo es que **no se reportó solo el lado favorable**:

- **A favor:** CR-02 llega a recall 1,000 con SDR 0,281. El detector solo no la
  sostendría; el patrón encima sí (F-81.1).
- **En contra:** la misma persistencia amplifica evidencia persistente-pero-equivocada
  (D1: 35 FP), y la evidencia equivocada **temprana canibaliza alertas correctas** —
  P1 pasa de recall 1,000/0 FP a 0,000/12 FP **con la percepción mejorada** (F-87.2).
- **El límite:** el rescate depende de que la cadencia alcance para muestrear la
  evidencia escasa. Bajo tiempo real, CR-02 es lo primero que se rompe (F-96.2).

**El motor mide persistencia, no corrección.** Dicho así, es una condición de validez
descubierta, no una queja.

### C4 — El método produjo más hallazgos que el resultado

Cinco artefactos de medición cazados **antes** de reportar, todos en la dirección de
*subestimar* o *distorsionar* la plataforma:

| Artefacto | Qué habría pasado |
|---|---|
| F-EV1 — clip negativo con F1=0 "computed" | 4 aciertos perfectos contados como catástrofes en el agregado |
| F-EV2 — tolerancia de bordes del GT ignorada | Doble castigo (missed + unexpected) a detecciones correctas |
| F-EV3 — re-confirmación contada como FP | Violación de ADR-011 |
| F-96.6 — SDR entre cadencias | "El detector mejora cuando mira menos": ~100% instrumento |
| F-96.5 — `t_alert` sin control de supervivencia | "La histéresis amortigua el costo": era composición del denominador |

Más dos guards que evitaron medir otra cosa creyendo medir lo correcto: el
`no_track_id` de G1 (habría medido G0 en silencio) y el doble guard de stride de R1–R6
(habría medido T1 creyendo medir tiempo real).

**Esto es reportable como resultado metodológico**, y probablemente sea lo más
transferible del trabajo: la infraestructura de evaluación necesita sus propios tests,
porque sus errores producen números plausibles.

## 5. Los dos escenarios, en una tabla

| Dimensión | DBE (offline, por archivo) | EBE (live, por bus) |
|---|---|---|
| Integridad | repositorio = fuente de verdad | **`bus_dropped_events = 0`** en todas las corridas |
| Paridad | — | **byte-idéntica** con replay (verificada por mutación) |
| Calidad contra GT | 13 campañas, 34 clips | por **proxy de densidad** (R1–R6) + confirmaciones live |
| Latencia | no aplica (ADR-013) | G2A p95 630–890 ms GDINO ✗ / 225–249 ms YOLOE ✓ |
| Throughput | irrelevante por diseño | 1,16–4,42 fps, causa diagnosticada (GIL) |
| Confirmaciones de patrón en vivo | — | **7 CR-01** (4,1–4,6 s) + **3 CR-02** (≥7,1 s) |

**Lo que cierra el eje:** toda corrida live es re-evaluable offline y produce artefactos
idénticos. El JSONL es la verdad en los dos caminos, así que **el escenario no cambia
el resultado, solo la densidad de evidencia** — y esa densidad ya está medida.

**Lo que queda abierto y se declara:** no hay campaña EBE de punta a punta por el bus
sobre los 34 clips (falta el ancla de sincronización); el decimado de R1–R6 es regular
y el descarte live es irregular.

## 6. Limitaciones, ordenadas por cuánto duelen

1. **L4 — un solo bloque guionado, sin obra real en video.** La más citable. Mismos
   actores, misma locación, escenarios guionados. La levanta el lote de internet
   cuando tenga GT; hoy el capítulo se sostiene sin él, pero con la limitación dicha.
2. **L1 — FAR/hora no reportable.** Harían falta 3 h de cumplimiento anotado; el banco
   llega a 0,10–0,26 h. Se reemplaza por el control de negativos, que discrimina
   (T1/T2/G1 dan 0 FP de 4; D1/H1/B1 dan 2–3).
3. **CR-02 a Nivel A no cerrada** — un solo estrato, IC solapados.
4. **L5 — escenarios desbalanceados**: obliga a reportar siempre por escenario.
5. **L2 — sin doble anotación ni kappa** (decisión declarada, no omisión).
6. **El tracker no está medido en obra real con multitud** — G1 se verificó en vivo con
   pocos sujetos.
7. **Licencia de `chv` parcial** (20,5% del bench de imágenes).

## 7. Qué se puede escribir ya, y qué espera

**Se puede escribir el capítulo de resultados completo.** Los tres materiales tienen
índice con procedencia verificada mecánicamente, las afirmaciones tienen su escala de
respaldo (§2) y las limitaciones están declaradas.

**Espera material, no análisis:**

| Ítem | Qué agrega | Quién |
|---|---|---|
| Lote de internet (CVAT) | Levanta **L4** + control de FP en material real | usuario |
| Videos V1–V3 de la defensa | Material de defensa, no resultado | usuario decide alcance |

Ninguno de los dos cambia una conclusión de este documento: el primero **agrega** una
sección de generalización, el segundo es soporte visual. Si no llegaran, el capítulo se
sostiene con L4 declarada — que es la regla del §7.6 del doc 57 (*el cierre lo decide
la cobertura del material; lo no cubierto se declara con causa, nunca se fabrica*).

## 8. Dónde está cada número

- **Punto de entrada:** `e-ovrt_experimental-setup/results/index.md` (4 índices por
  material, verificados con `datos/96-verificar-indices.py`).
- **Q1–Q4 del plan maestro:** doc 92 (con adenda ✎ del eje de tiempo real).
- **Estado de implementación:** doc 97 (reemplaza al 56).
- **Campañas:** docs 81 (T1), 83/84 (Nivel A + T2), 85 (D1), 87 (H1), 88 (B1),
  89 (G1), 96 (R1–R6).
- **Live:** docs 37, 65, 67, 71, 73, 74, 91.
