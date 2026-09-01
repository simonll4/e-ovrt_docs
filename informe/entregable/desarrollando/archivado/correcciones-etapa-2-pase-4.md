# Correcciones de la Etapa 2 — §17.1 (pase 4: legibilidad sin pérdida — 2026-08-31)

> ✅ **APLICADO Y VERIFICADO — 2026-08-31 (misma jornada): la entrega de ChatGPT es la v1.5,
> aceptada y limpia** (`desarrollando/…v1.5.docx`). Verificación completa de §D:
> - **Metadiscurso 33 → 11** (target ≤12) · **párrafos >150 palabras 14 → 2** (target ≤2) ·
>   28.418 palabras (target 28.250–28.500) · 109 títulos · 21 tablas 16–36 + 6 de anexo ·
>   **78 ecuaciones** · verificador OK.
> - **Cero pérdida verificada**: "et al." 59 → 59 · años citados idénticos (el −1 aparente era la
>   fecha del banner de extracción, no una cita) · `deberá` 28 y `todavía` 7 intactos · los greps
>   del pase 3 siguen en cero · **41/41 anclas** (viejas en 0, nuevas en 1) · **15/15 cortes de
>   párrafo** aplicados · anti-duplicación limpio (ninguna oración ≥12 palabras repetida).
> - Cambios controlados de la entrega (37 ins / 22 del) **aceptados sobre el XML** (0 fusiones con
>   texto — sin el patrón del defecto del pase 3); los **27 comentarios siguen resueltos e
>   intactos**. Respaldo: `archivado/…v1.5 (entrega GPT, cambios sin aceptar).docx`.
> **La v1.5 es la vigente de la Etapa 2.** Handoff que sigue vivo: §17.3 lleva 11 metadiscursos y
> 2 párrafos gordos a su v1.5; §15/§16 a medir (pase del colega). Vara de voz del informe: §17.5.
>
> ~~**Estado: NO aplicado — es el trabajo a entregar a ChatGPT.**~~ Base:
> `desarrollando/E-OVRT-VDP_Seccion_17.1_Consolidacion_Metodologica_v1.4.docx` (**v1.4 final y
> limpia**: tres pases aplicados, cambios controlados aceptados, 27 comentarios resueltos;
> 28.628 palabras · 109 títulos · 21 tablas 16–36 + 6 de anexo · 78 ecuaciones · verificador OK).
> **Salida esperada: v1.5.**
>
> **Qué es este pase y qué NO es.** El usuario detectó que la sección "pierde al lector". El
> diagnóstico medido (2026-08-31) ubicó la causa: **34 oraciones de metadiscurso** —el texto
> hablando del documento en vez de hablar del sistema: "la presente sección documenta…", "el
> propósito operativo de esta sección es cuádruple"— contra 11 en §17.3, 2 en §17.4 y 1 en §17.5;
> más **14 párrafos de más de 150 palabras**. Este pase corrige **la voz y el ritmo, no el
> contenido**: ninguna decisión, número, criterio, tabla, ecuación ni **cita bibliográfica**
> cambia. **Regla suprema (D-P4-1): cero pérdida de información** — donde una oración de
> metadiscurso lleva contenido, se re-sujeta o se pliega; sólo se elimina el anuncio puro cuyo
> contenido ya está en los títulos o en la oración vecina.
>
> **Lección del pase 3 que rige acá:** los reemplazos son EXACTOS (buscar→reemplazar); si un
> texto no aparece tal cual, se reporta en la entrega en lugar de improvisar. No dejar copias
> viejas al reescribir. Entregar con cambios controlados. **Los 27 comentarios del documento
> están RESUELTOS: no tocarlos, no reabrirlos, no eliminarlos.**

---

## A. Decisiones que gobiernan el pase

⚠ *Serie de IDs propia de la etapa 2 (pase 4); no confundir con otras series D-P*.*

| ID | Decisión | Firma |
|---|---|---|
| **D-P4-1** | **Pase de legibilidad autorizado, con cero pérdida de información**: se comprime el andamiaje metadiscursivo y se parte el párrafo largo; no se recorta contenido ("no reducir por reducir"). La vara de voz es §17.5. | usuario · 2026-08-31 |
| **D-P4-2** | **Intocables**: las invocaciones a las preguntas rectoras `P-E1-xx` (trazabilidad hacia §16.7.3 — pueden re-sujetarse pero el ID y su glosa sobreviven); las fronteras anti-anacronismo ("no implementa…", "corresponde a la instancia de análisis y diseño arquitectónico…"); todas las citas bibliográficas (ninguna se agrega ni se elimina); los señalizadores baratos que orientan ("Se organiza en cinco fases.", "La jerarquía del framework se organiza en tres niveles."). | recomendación adoptada |

## B. NO TOCAR

Todo lo del pase 3 sigue vigente: contenido de tablas · rango 500–2.000 · MOT intactos · el
`[[PENDIENTE]]` AAIP · las **78 ecuaciones** · definiciones CPN/EN/TN · los 4.000/7.000 ms.
Además: **los 27 comentarios resueltos** (ni tocarlos ni reabrirlos) · las oraciones que hablan
del **sistema o del proyecto** aunque suenen parecidas al metadiscurso (p. ej. *"la evaluación se
organiza en dos escenarios complementarios"*, *"esta técnica excede el alcance del presente
proyecto"*, *"La presente sección concentra su validación primaria en el tramo Glass-to-Alert"* —
esa habla de qué tramo valida el framework, se queda) · los Anexos C y D completos.

---

## C. Unidades

### E2-51 · §17.1.4.1 — la introducción del entorno, en voz de sistema

**Reemplazar el párrafo completo** que empieza *"La presente sección documenta el entorno
experimental sobre el cual se desarrolla y evalúa la plataforma E-OVRT-VDP."* y termina
*"…delimita el referente experimental de la presente sección."* por:

> *"El entorno experimental comprende la infraestructura de cómputo disponible para inferencia y
> entrenamiento, el stack de software asociado, los escenarios de evaluación definidos para el
> proyecto y las condiciones operativas propias de cada escenario. Su caracterización responde a
> la pregunta rectora P-E1-04 de la fundamentación teórica: las restricciones del entorno de
> ejecución —capacidad computacional, protocolos de transmisión y presupuesto de procesamiento—
> que condicionan las decisiones arquitectónicas del prototipo. Los escenarios de evaluación
> establecen, además, las condiciones concretas bajo las cuales se ejercita el prototipo."*

(Conserva P-E1-04 con su glosa completa y las tres restricciones; sólo cae el envoltorio.)

### E2-52 · §17.1.5 — aperturas en voz de sistema (7 retoques)

1. **§17.1.5.1, primer párrafo** — reemplazar desde *"La presente sección responde a la pregunta
   rectora P-E1-02 definida en la fundamentación teórica, que dejó abierta la brecha"* hasta
   *"…los criterios de aplicación del framework evaluativo."* por:
   > *"La taxonomía de condiciones de riesgo, los patrones asociados y el protocolo de prompts
   > responden a la pregunta rectora P-E1-02, que dejó abierta la brecha entre la identificación
   > normativa de condiciones de riesgo y su traducción en consultas textuales evaluables por
   > modelos de detección open-vocabulary, y señaló que la formulación del prompt no es un
   > detalle accesorio sino una variable capaz de alterar significativamente el desempeño del
   > detector en dominios especializados. En articulación con el framework de métricas, se
   > delimita además cómo estas definiciones deben leerse respecto de la latencia de alerta, las
   > métricas operativas y los criterios de aplicación del framework evaluativo."*
   (Cae sólo la oración-anuncio del medio: su contenido son los títulos de 17.1.5.2/.3/.4.)
2. §17.1.5.1: *"El alcance de la sección es metodológico. Establece qué condiciones"* →
   *"El alcance es metodológico: establece qué condiciones"*.
3. §17.1.5.3, primera oración: *"Esta sección define conceptualmente los patrones de riesgo que
   constituyen la unidad operativa de análisis del sistema E-OVRT-VDP. Para ello articula tres
   componentes:"* → *"Los patrones de riesgo constituyen la unidad operativa de análisis del
   sistema E-OVRT-VDP. Su definición conceptual articula tres componentes:"*.
4. §17.1.5.3.3: *"La presente sección define estos criterios en términos de duración temporal"*
   → *"Estos criterios se definen en términos de duración temporal"*.
5. §17.1.5.3.7: *"El desarrollo de esta sección deja tres insumos directos para la instancia"*
   → *"Quedan tres insumos directos para la instancia"*.
6. **§17.1.5.4, párrafo de apertura** (además es uno de los 14 gordos):
   - *"Esta sección establece el marco metodológico para el diseño, la variación sistemática y la
     evaluación empírica de los prompts textuales que operan como interfaz de consulta del modelo
     OVD."* → *"El protocolo de prompts establece el marco para el diseño, la variación
     sistemática y la evaluación empírica de las consultas textuales que operan como interfaz del
     modelo OVD."*
   - *"El protocolo se articula con el framework definido en el framework de métricas, de la cual
     toma las métricas"* → *"El protocolo se articula con el framework de métricas, del cual toma
     las métricas"* (repara además la concordancia rota).
   - **Partir el párrafo** insertando salto antes de *"Asimismo, toma como referencia protocolos
     de evaluación recientes"*.
7. §17.1.5.5: *"Para evitar ambigüedades terminológicas, esta sección adopta dos definiciones
   operativas."* → *"Para evitar ambigüedades terminológicas se adoptan dos definiciones
   operativas."*

### E2-53 · §17.1.6 — la estrategia de datos deja de presentarse a sí misma (6 retoques)

1. **§17.1.6.1.1, primer párrafo**: *"La presente sección responde a las preguntas rectoras
   P-E1-03 y P-E1-08 formuladas en la sección 16.7.3 de la fundamentación teórica. En relación
   con P-E1-03, construye"* → *"La estrategia de datos responde a las preguntas rectoras P-E1-03
   y P-E1-08 formuladas en la sección 16.7.3 de la fundamentación teórica. En relación con
   P-E1-03, construye"* (el resto del párrafo queda tal cual).
2. **§17.1.6.1.1, segundo párrafo** ("El propósito operativo de esta sección es cuádruple.
   Primero, … Cuarto, …") — **reemplazar el párrafo completo** por:
   > *"Ese propósito se completa con un mapeo explícito entre cada dataset candidato y las
   > condiciones de riesgo CR-01 a CR-06 de la taxonomía, y con las condiciones metodológicas
   > mínimas que cualquier estrategia de partición deberá satisfacer para sostener una comparación
   > válida entre baseline zero-shot y variante fine-tuned, cuando esa comparación aplique."*
   (Los puntos "Primero" y "Tercero" ya están, palabra por palabra, en el párrafo anterior — el
   inventario con atributos y la aptitud para fine-tuning; sólo "Segundo" y "Cuarto" agregan
   información y ésa se conserva entera.)
3. §17.1.6.1.1: *"El alcance de la sección es metodológico. Elabora un inventario"* →
   *"El alcance es metodológico: elabora un inventario"*.
4. §17.1.6.1.2: *"El inventario de esta sección se organiza en dos categorías"* →
   *"El inventario se organiza en dos categorías"*; y *"Quedan fuera del alcance de la presente
   sección las colecciones generalistas"* → *"Quedan fuera del inventario las colecciones
   generalistas"*.
5. §17.1.6.2.7: *"La presente sección documenta sólo las condiciones metodológicas que cualquier
   esquema de partición deberá satisfacer."* → *"El protocolo fija sólo las condiciones
   metodológicas que cualquier esquema de partición deberá satisfacer."*
6. **§17.1.6.4, apertura** — reemplazar *"Las secciones precedentes analizaron los datasets desde
   una perspectiva técnica y metodológica. La presente sección documenta dos dimensiones que
   atraviesan el inventario completo"* por *"Dos dimensiones atraviesan el inventario completo"*
   (el resto del párrafo queda tal cual, incluida la frase final de insumos para la instancia de
   análisis y diseño arquitectónico).

### E2-54 · §17.1.7 — el framework habla de métricas, no de sí mismo (6 retoques)

1. **§17.1.7.1.1, segundo párrafo**: *"En ese marco, la presente sección responde a dos de las
   preguntas rectoras formuladas en la fundamentación teórica. En relación con P-E1-06, define el
   framework de métricas para evaluar"* → *"En ese marco, el framework responde a dos preguntas
   rectoras de la fundamentación teórica. En relación con P-E1-06, define las métricas para
   evaluar"* (el resto del párrafo, incluida la glosa de P-E1-01, queda tal cual).
2. §17.1.7.1.1: *"El alcance de la sección es metodológico. Define métricas"* →
   *"El alcance es metodológico: define métricas"*.
3. §17.1.7.3.2: *"No todas las métricas definidas en esta sección asumen el mismo nivel de
   compromiso."* → *"No todas las métricas del framework asumen el mismo nivel de compromiso."*
4. §17.1.7.4: *"Las secciones siguientes presentan las familias de métricas seleccionadas para
   los tres planos del sistema evaluable: detección OVD, seguimiento multiobjeto (MOT) y
   rendimiento del pipeline."* → *"Las métricas adoptadas cubren los tres planos del sistema
   evaluable: detección OVD, seguimiento multiobjeto (MOT) y rendimiento del pipeline."*
5. §17.1.7.5: *"Por ello, esta sección incorpora métricas operativas específicas del dominio:"*
   → *"Por ello, el framework incorpora métricas operativas específicas del dominio:"*
6. §17.1.7.8: *"Para que el framework sea ejecutable y no meramente declarativo, la presente
   sección traduce las métricas anteriores a requisitos mínimos de instrumentación, preparación y
   registro. Su propósito no es redefinir las métricas, sino fijar las condiciones bajo las
   cuales su medición resulta metodológicamente defendible."* → *"Para que el framework sea
   ejecutable y no meramente declarativo, las métricas anteriores se traducen a requisitos
   mínimos de instrumentación, preparación y registro. No se redefinen las métricas: se fijan las
   condiciones bajo las cuales su medición resulta metodológicamente defendible."*

### E2-55 · Partir los párrafos de más de 150 palabras · ⚠ SOLO saltos de párrafo, ni una palabra cambia

Insertar un salto de párrafo **antes de** cada una de estas oraciones (la oración citada abre el
párrafo nuevo). La nota de la Tabla 21 (§17.1.5.2.3) **NO se parte** — las notas de tabla van en
un solo párrafo. El párrafo de apertura de §17.1.5.4 ya se parte en E2-52.6.

| # | § | El párrafo nuevo empieza en… |
|---|---|---|
| 1 | 17.1.5.2.1 | "La pertinencia de este criterio se ve reforzada por evidencia empírica reciente" |
| 2 | 17.1.5.2.2 | "Este análisis puede implementarse mediante lógica de post-detección" |
| 3 | 17.1.5.2.4 | "La segunda particularidad es geométrica:" |
| 4 | 17.1.5.4.1 | "En este marco, la formulación del prompt no constituye un detalle accesorio:" |
| 5 | 17.1.5.4.1 | "De manera complementaria, trabajos recientes muestran que la incorporación" |
| 6 | 17.1.5.4.2 | "Los encoders textuales utilizados por modelos visión-lenguaje" |
| 7 | 17.1.5.4.2 | "Esta expectativa se fundamenta en que, en los modelos OVD," |
| 8 | 17.1.5.4.2 | "Esto no implica necesariamente que el costo total de inferencia" |
| 9 | 17.1.5.4.2 | "Por otro lado, Grounding DINO recibe como entrada" |
| 10 | 17.1.5.4.3 | "Esta decisión tiene una implicación práctica relevante:" |
| 11 | 17.1.7.6 | "La separación estricta entre datos de entrenamiento y evaluación" |
| 12 | 17.1.7.6 | "Cuando exista una variante ajustada y soporte de datos suficiente" ⚠ el tramo lleva ecuaciones: no tocarlas |
| 13 | 17.1.7.7.4 | "En este punto, la mención de YOLO-World debe leerse" ⚠ ídem |
| 14 | 17.1.10.2 | "Quinto, la disyunción entre datos de entrenamiento" |

---

## D. Verificación de cierre (targets de la v1.5)

| Métrica | v1.4 | Target | Cómo |
|---|---|---|---|
| Palabras | 28.628 | **~28.250–28.500** (baja sólo el andamiaje; sin cuota) | verificador |
| Títulos numerados | 109 | **109** (ninguno cambia) | verificador |
| Tablas | 21 (16–36) + 6 anexo | **idéntico** | grep de rótulos |
| Ecuaciones OMML | 78 | **78** (ninguna unidad las toca) | XML |
| Comentarios | 27 resueltos | **27 resueltos, intactos** | XML |
| Metadiscurso (patrón: "la presente sección\|esta sección\|el presente\|se organiza en\|el alcance de la sección\|las secciones siguientes\|las secciones precedentes\|de esta sección") | 34 oraciones | **≤ 12** (los que quedan hablan del sistema o son señalizadores de D-P4-2) | grep |
| Párrafos >150 palabras | 14 | **≤ 2** (la nota de la Tabla 21; cualquier otro, declarado) | script |
| Citas bibliográficas | — | conteo de "et al." y de años entre paréntesis **idéntico** a la v1.4 | grep |
| Voz | `deberá` 28 · `todavía` 7 | **idéntico** | grep |
| Greps del pase 3 | todos en cero | **siguen en cero** | extracción |
| Diff | — | párrafo a párrafo contra `90f` v1.4: cada bloque atribuido a E2-51…E2-55; **chequeo anti-duplicación**: ninguna oración ≥12 palabras repetida | script |

## E. Handoff

La misma medición que originó este pase da para el resto del informe: **§17.3 = 11 oraciones de
metadiscurso y 2 párrafos gordos** (para su v1.5, junto con E3-42 y los 3 sitios de voz D-P3-9) ·
**§15+§16 = a medir** (pase del colega) · §17.4 (2) y §17.5 (1) no lo necesitan. La vara de voz
del informe queda fijada: **§17.5**.
