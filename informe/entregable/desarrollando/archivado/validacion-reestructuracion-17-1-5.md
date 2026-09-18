# Validación de la propuesta de reestructuración de §17.1.5 (21 → 4 subsecciones)

> ✅ **CERRADO el 2026-09-03.** La reestructuración de §17.1.5 que este documento validó quedó en la
> v1.10 y sobrevive sin cambios en la **v1.15 final**. El resto del ciclo (§17.1.6, §17.1.7 y el
> tramo final) está en [`relevamiento-17-1-v1-11.md`](relevamiento-17-1-v1-11.md) y
> [`analisis-17-1-8-anexos.md`](analisis-17-1-8-anexos.md). Ya no se edita.

> **Constancia (2026-09-02).** Validación completa de la propuesta de GPT para reestructurar
> §17.1.5 *Condiciones de riesgo, patrones y protocolo de prompts*, cotejada contra el `.docx`
> real, los otros documentos del informe (§15/16 v1.1, §17.3 v1.4, §17.4 v1.6, §17.5 v1.3), el
> pattern set oficial del control-plane y las actas de los pases 3–6. Base cotejada: la copia
> de trabajo `desarrollando/…_v1.7.docx` (modificada 2026-09-02 00:47, con §17.1.2 y §17.1.4 ya
> reestructuradas) y la `v1.8` vigente. Todo lo que sigue se midió; nada se infiere.
>
> ✅ **APLICADA el 2026-09-02 → `E-OVRT-VDP_Seccion_17.1_Consolidacion_Metodologica_v1.10.docx`**
> (base: la v1.9 = rama de GPT con D-E1-11 aplicado). Acta en §G al final. Instrumento:
> `aplicar_1715.py` (edición byte a byte de `word/document.xml`; Tablas 20 y 21, sus captions,
> la nota de la Tabla 21 y los cuatro saltos de sección a página apaisada, intactos).
> **La v1.9 sigue en `desarrollando/` hasta que el usuario acepte la v1.10; entonces pasa a
> `archivado/`.** Los hallazgos A-1…A-4 (rama de GPT) NO se resolvieron en este pase: siguen abiertos.

## 0. Veredicto en tres líneas

1. **El diagnóstico y la estructura de cuatro subsecciones son válidos**: los 21 encabezados,
   los 16 rótulos en negrita, la redefinición de "patrón" (§17.1.5.3.1 ↔ §17.1.3.1/.3.2), la
   síntesis §17.1.5.5 mal ubicada y las cuatro referencias cruzadas internas están **todas
   verificadas**. Los cinco comentarios del revisor anclados en §17.1.5 (v1.8) piden exactamente
   esto.
2. **Cuatro afirmaciones de la propuesta son falsas o están vencidas** (§C): la de §16.2 y las
   severidades ya la corrigió el pase 6; "§15 ya lo fundamenta" es falso para FG-OVD/OVDEval/
   templates/hard negatives (0 ocurrencias en §15/16); §17.3 hoy **no** remite a §17.1.5.x; y
   "composición del vocabulario activo" ya nace en §17.1.5.4.2.
3. **Antes de tocar §17.1.5 hay que resolver el archivo** (§A): la copia de trabajo es un fork
   de la **v1.7**, no de la v1.8 vigente (pierde el cierre D-E1-11), **perdió 26 de los 27
   comentarios resueltos** y tiene un párrafo de cuerpo con estilo Heading 3 en §17.1.4.2.

---

## A. Hallazgos sobre el archivo de trabajo — bloquean antes de aplicar nada

| # | Hallazgo | Evidencia |
|---|---|---|
| A-1 | La copia de trabajo `desarrollando/…_v1.7.docx` (sha `91d4a24f…`, 24.911 palabras, 100 títulos) deriva de la **v1.7 archivada** (`3c463696…`), **no de la v1.8** (`684bac34…`). Conserva el marcador `[[PENDIENTE: definir con el equipo la aplicabilidad de esta inscripción…]]` y la oración de anclaje *"Ese régimen contempla, además, requisitos administrativos… (AAIP)… se documentan a continuación."* que la v1.8 eliminó (D-E1-11, 09-01). | `verificar_entregable.py`: "marcadores pendientes: PENDIENTE×1" en la copia; "ninguno" en v1.8. `90f`, generador y kit ya están a **v1.8**. |
| A-2 | **Perdió 26 de 27 comentarios.** Sobrevive sólo el id 0 del colega (anclado en el título 17.1.4). Los 5 anclados en §17.1.5 desaparecieron: **11** (título 17.1.5: *"se me hizo muy repetitivo, antes de llegar a esta sección ya leí mucho sobre esto"*), **12** (intro: *"hacer más breve esta introducción y no ser redundante. Mandar a leer la sección donde se desarrolló"*), **13** (título 17.1.5.3.3: *"se puede hacer más breve sin perder la calidad del desarrollo"*), **14** (párrafo de prompts de nivel 3: *"pendiente a resolver"*), **15** (remisión final al Anexo C: *"pendiente a resolver"*). | `comments.xml`: 1 vs 27. Regla del pase 5 (acta, l. 47): *"Los 27 comentarios resueltos no se tocan"*. Estos cinco **respaldan la propuesta** y la propuesta no los cita. |
| A-3 | **Defecto de formato en §17.1.4.2**: el párrafo *"La relación entre ambos escenarios no es de reemplazo. El DBE sostiene…"* quedó con estilo **Heading 3** (mismo nivel que 17.1.4). Aparece en el índice como título sin número. | Párrafo #62 del XML; `verificar_entregable.py` no lo detecta (sólo busca títulos sin estilo, no cuerpo con estilo de título). |
| A-4 | §17.1.2 quedó con **una sola subsección** (17.1.2.1) — hija única, estructuralmente rara. | Lista de títulos de la copia. |

**Camino recomendado**: rehacer las ediciones de §17.1.2/§17.1.4 **sobre la v1.8** (o re-aplicar
D-E1-11 y reinyectar los 27 comentarios sobre la copia) y corregir A-3/A-4 **antes** de abrir
§17.1.5. Si se sigue sobre la copia actual, el cierre D-E1-11 y la historia de revisión se pierden
en silencio.

---

## B. Lo que la propuesta afirma y se verificó cierto

| Afirmación | Verificación |
|---|---|
| 21 encabezados subordinados | 1 + 1+4 + 1+7 + 1+5 + 1 = **21** ✔ |
| Rótulos en negrita como tercer nivel | **16** (+2 captions de tabla): 3 criterios, 3 niveles, 5 ejes/implicancias, 5 fases ✔ |
| Peso de la sección | **8.092 palabras** = 32 % del documento (7.351 prosa + 556 en tablas). En v1.5 eran 9.242: el pase 5 ya sacó ~1.150. |
| §17.1.5.3.1 redefine lo que §17.1.3.1/.3.2 ya definen | ✔ Texto cotejado: condición = unidad semántica de entrada; patrón = severidad + persistencia + relaciones; alerta = salida operativa; motor = abstracción del plano de control. |
| §17.1.5.5 hace tres cosas (variable experimental · define dos términos · remite al Anexo C) | ✔ |
| Dos referencias formales al Anexo C dentro de §17.1.5 | ✔ (§17.1.5.4.4 y §17.1.5.5) |
| "Los criterios de evaluación están en el cuerpo, no en C.1" | ✔ Anexo C = C.1 catálogo de prompts · C.2 variables EBE · C.3 logística. Ningún criterio. |
| Tabla 20: código, nivel, tipo, condición, evidencia, componente evaluador, dificultad | ✔ |
| Tabla 21: patrón, condición, severidad, persistencia, criterio de activación, perfil temporal, trade-off FP | ✔ |
| Rangos 2–4 / 3–5 / 5–10 s; PR-01 4.000/2.000 ms; PR-02 7.000/3.000 ms | ✔ y **coinciden con el pattern set oficial** `cr01_cr02_v2` (CR-01 `high` 4000/2000 · CR-02 `medium` 7000/3000). |
| Mazor et al. (2021) es analogía de percepción humana | ✔ el propio texto lo declara. Pase 5 (E2-58) la dejó **deliberadamente** en una "casa única" (§17.1.5.2.4). |
| Kim et al. (2024) "excede el alcance" | ✔ literal en §17.1.5.4.1. |
| Histéresis explicada dos veces | ✔ §17.1.5.3.3 párrafo 5 y §17.1.5.3.4 párrafo 5. |
| PR-05/PR-06: contenido no cubierto por la Tabla 21 | ✔ (coordenadas 2D ≠ distancia física, polígono externo, cámara fija, ID switches). |
| Referencias cruzadas **dentro del .docx** a actualizar | **Las cuatro que lista son exactamente todas**: §17.1.3.2 → *17.1.5.3.4* (l. 37) · tabla de §17.1.6.1.3 → *17.1.5.2* (l. 381) · §17.1.7.7.5 → *17.1.5.3.2* (l. 737) · nota de la Tabla C.1 → *17.1.5.4.2* (l. 952). Más 4 autorreferencias internas que desaparecen con la reescritura (.2.1→.2.2 · .2.2→.4 · .4.2→.4.5 · .4.5→.4.2). |
| La nueva §17.1.2.1 ya explica núcleo/extensiones | ✔ (copia de trabajo, l. 21–23). **Además** la última oración de la nota de la Tabla 20 lo repite: candidata adicional. |
| El pre-registro no ejercido no se borra | ✔ Regla vigente: pase 3 (*"lo prescripto y no ejercido no se borra, lo reporta §17.5"*), D-P5-3, `analisis-poda-17-1.md` §6.2. |
| Sin ecuaciones ni figuras en §17.1.5 | ✔ 0 `oMath` en el rango: la reescritura no toca las 76 ecuaciones. Conservar las Tablas 20/21 y no crear tabla nueva mantiene la numeración 16–35. |

---

## C. Afirmaciones falsas o vencidas

| # | La propuesta dice | Lo medido |
|---|---|---|
| C-1 | *"corregiría el problema que vimos antes: no diría que §16.2 fundamenta las seis severidades"* | **Ya corregido en el pase 6** (E2-76…79): la cabecera de §17.1.5.3.2 dice *"categoría metodológica de prioridad temporal… la relevancia preventiva de las condiciones subyacentes está establecida en la sección 16.2. La severidad… no constituye una calificación normativa"*; la nota de la Tabla 21 ídem. La instrucción operativa es **no perder esa redacción al comprimir**, no corregirla. |
| C-2 | *"§15 ya estableció esta brecha"*, *"hard negatives… pertenece al estado del arte"*, *"Eso ya fue tratado en §15"* (tamaño del vocabulario) | §15.2.5.3 sí trata la sensibilidad al prompt (Zhou 2022b, Du 2022). Pero **§15/§16 (v1.0 y v1.1) tienen 0 ocurrencias** de FG-OVD/Bianchi, OVDEval/Yao, Gu (ViLD), *template*, *"a photo of"* y *hard negatives*. §17.1.5.4 es **la única casa en todo el informe** del fundamento del eje "aislado vs completo" y de las métricas por entidad. Comprimir a un párrafo ancla está bien; **remitir a §15 sería una remisión falsa** (el mismo defecto que E3-42 corrigió en §17.3). Esto también corrige la premisa de `archivado/analisis-poda-17-1.md` §4.5 (*"YA vive en §15/§16"*), que era cierta para Zhou/Du y falsa para Bianchi/Yao/Gu. |
| C-3 | *"§17.3, donde E-DIR/E-IND/E-HYB se remiten al lugar en que nacen → nueva §17.1.5.3"* | **§17.3 v1.4 no contiene ninguna referencia a §17.1.5.x** (E3-42 la dejó autosuficiente); §17.4 v1.6 y §17.5 v1.3 tampoco. Hoy no hay nada que actualizar en §17.3. Lo que sí cambia es el **handoff pendiente D-E2-2** (*"§17.3.6.4 recorta su glosa a una remisión a §17.1.5.4.2"*, en el generador del kit l. 514 y en el tablero l. 334): debe apuntar a la nueva §17.1.5.3. |
| C-4 | *"dos términos que hoy aparecen demasiado tarde, recién en 17.1.5.5"* | Cierto sólo para **"matriz de prompts"** (l. 338 y Anexo C). **"Composición del vocabulario activo" ya nace como cuarto eje en §17.1.5.4.2** (l. 286, con definición). Lo que corresponde subir es una sola definición. |

---

## D. Lo que la propuesta no contempla

| # | Hueco | Detalle |
|---|---|---|
| D-1 | **Bajas de referencias.** Mazor (2021) y Kim (2024) se citan **únicamente en §17.1.5** (0 en §15/16, §17.3, §17.4, §17.5). Eliminarlas = dos referencias menos en el informe. | El pase 5 corrió con regla "cero bajas de referencias" y E2-58 conservó Mazor a propósito. Es **decisión nueva del usuario**, no default de la poda. Ninguna de las dos está hoy en la lista de referencias (`90e`), así que no quedan huérfanas; la integración las agrega sólo si sobreviven. Sharma y Changpinyo también se citan en §17.3: seguras. |
| D-2 | **Huecos textuales preexistentes** (desde la v1.0) en los párrafos que la propuesta reescribe: §17.1.5.3.2 *"objetivos más exigentes de TTFD y ⟨ ⟩ dentro del framework evaluativo"*; §17.1.5.3.3 *"esta ventana expresa ⟨ ⟩ y no debe confundirse ni con ⟨ ⟩ —subtramo computacional por cuadro— ni con ⟨ ⟩, que integra además la confirmación operativa"*; y *"talert-system"* aplanado. | **No son objetos de ecuación** (XML sin `oMath`, `sym` ni campos — el guardrail "los nombres vacíos son ecuaciones" no aplica acá). La reescritura es el momento de restituir los símbolos (t_alert, ventana de persistencia, G2A, t_alert-system) o de suprimir la oración. |
| D-3 | **Guardrails de pases previos que deben sobrevivir explícitamente.** | E2-74: la oración *"La fundamentación teórica delimita las condiciones… (sección 16.2), y señala como posibles extensiones…"* repara una referencia colgante — la compresión de los criterios a un párrafo debe conservar esa remisión. D-P3-1: prohibido tocar definiciones, umbrales y contenido de tablas. D-P5-3 y pase 6 §4: CR/PR completos, ventanas intactas. |
| D-4 | **Reabre un veredicto 🟢.** `archivado/analisis-poda-17-1.md` §4.6 marcó §17.1.5.3 *"dejar (ya trabajada tres veces)"*; la propuesta elimina .3.1, comprime severidad/persistencia/motor y funde .3.6/.3.7. | Es coherente (la fragmentación sí es el problema), pero es **decisión nueva a firmar**, no continuación del pase 5. |
| D-5 | **Cadena fuera del .docx.** | Re-extraer `90f` · regenerar el kit (`generar_project_kit.py --check`; `01-etapa-2-activa.md` trae 153 referencias a `17.1.5.`) · actualizar la nota D-E2-2 del generador (l. 514) · tablero `00-el-informe-hoy.md` (l. 334, 443–444) · `INSTRUCCIONES-PROJECT`. **No** se reescriben actas, `ajustes/02` ni `operacion/*` (archivado lógico). |
| D-6 | **Comentarios anclados** (en la v1.8): al borrar la intro (12), el título .3.3 (13) y la oración final al Anexo C (15) se borran sus comentarios; 14 depende de cómo se funda el párrafo. | Están resueltos; la política vigente es que "viajan" y el usuario decide. Debe decidirse **antes**, no descubrirse después. |
| D-7 | **Tercera representación de las severidades.** §17.1.7.7.5 re-describe crítica/alta/media en tres párrafos con rótulo. | Al comprimir §17.1.5.3.2 a un párrafo, §17.1.7.7.5 pasa a ser la descripción más larga; no hay contradicción, pero conviene revisarla en el mismo pase. |
| D-8 | **Estados del motor.** §17.1.5.3.4 nombra 4 estados (inactivo/candidato/confirmado/resuelto); §17.3 define 5 con reapertura a *candidate*. | Reducir el motor a "requisitos metodológicos" (propuesta §6) **elimina** esta inconsistencia latente: punto a favor, vale nombrarlo. |
| D-9 | **Numeración de la nueva §17.1.5.** | Con 4 hijas y sin nietas, Word renumera solo. Verificar tras aplicar: `verificar_entregable.py` (huecos de numeración) + conteo de títulos esperado **100 − 17 = 83** sobre la copia actual, o **109 − 17 = 92** sobre la v1.8. |

---

## E. Sobre la estimación de reducción

Prosa actual de §17.1.5: **7.351 palabras** (sin tablas). Las eliminaciones puras de la propuesta
(intro 220, .2 intro 92, .3 intro 80, .3.1 181, .3.7 227→~30, .5 174, .4.1 198→~80) suman ya
**~−1.050**; las compresiones de .2.1/.2.2/.2.4, .3.2/.3.3/.3.4, .4.2/.4.3/.4.5 aportan
razonablemente otras −1.500 a −2.000. El rango **35–45 %** (≈ −2.600 a −3.300 palabras; prosa
final ~4.000–4.800) es realista, y el criterio que fija la propuesta ("cada párrafo restante
sostiene una decisión, una definición o una regla") es el correcto: no fijar el porcentaje como
objetivo.

Pesos por bloque (prosa / tabla), para dimensionar cada compresión:

| Bloque | Prosa | Tabla |
|---|---:|---:|
| 17.1.5.1 Introducción | 220 | — |
| 17.1.5.2 (+ .2.1–.2.4) | 92 + 318 + 468 + 214 + 408 = 1.500 | 268 |
| 17.1.5.3 (+ .3.1–.3.7) | 80 + 181 + 415 + 593 + 529 + 167 + 373 + 227 = 2.565 | 288 |
| 17.1.5.4 (+ .4.1–.4.5) | 183 + 198 + 1.041 + 308 + 279 + 883 = 2.892 | — |
| 17.1.5.5 Síntesis | 174 | — |

---

## F. Orden de aplicación recomendado

1. Resolver **A-1…A-4** (base v1.8, comentarios, Heading 3, hija única).
2. Firmar las decisiones nuevas: **D-1** (Mazor/Kim), **D-4** (reabrir §17.1.5.3), **D-6**
   (comentarios 12/13/14/15).
3. Aplicar la reestructuración con las correcciones **C-1…C-4** incorporadas al instrumento
   (la cabecera de severidad del pase 6 se conserva literal; el párrafo ancla de FG-OVD/OVDEval
   se queda; el handoff D-E2-2 apunta a la nueva §17.1.5.3; una sola definición sube).
4. En el mismo pase: **D-2** (huecos), **D-3** (E2-74), las 4 referencias cruzadas de §B y
   la oración final de la nota de la Tabla 20.
5. Cierre: `verificar_entregable.py` · conteo de títulos · 76 ecuaciones · comentarios ·
   `90f` → kit `--check` → tablero.

---

## G. Acta de aplicación (2026-09-02) — v1.9 → v1.10

**Qué se aplicó.** La estructura de cuatro subsecciones propuesta por GPT (§2 de la propuesta),
con las correcciones C-1…C-4 y los huecos D-2, D-3, D-7 y D-8 incorporados. Prioridades del
usuario para la redacción: sin redundancia con §17.1.2, §17.1.3 y §15; prosa narrativa continua
de TFG; sin dos puntos ni punto y coma en la prosa nueva (medido: **0 y 0**, fuera de las citas
APA entre paréntesis, que conservan su punto y coma normativo).

| Bloque viejo | Destino | Qué se hizo |
|---|---|---|
| 17.1.5.1 Introducción | párrafo bajo 17.1.5 | Un párrafo. Cae el metadiscurso ("no constituye implementación", "la validación calibrará"). |
| 17.1.5.2 + .2.1–.2.4 | **17.1.5.1** | Criterios en un párrafo (conserva la oración de E2-74 con su remisión a §16.2). Niveles en un párrafo con un ejemplo cada uno. Tabla 20 intacta. Nota de la Tabla 20 sin su última oración (duplicaba §17.1.2.1). CR-03/CR-04 juntas, Nivel 3 + ortogonalidad + transversales en otro. **Mazor (2021) cae.** |
| 17.1.5.3 + .3.1–.3.7 | **17.1.5.2** | .3.1 eliminada (remite a §17.1.3). Severidad en dos párrafos que **conservan literal la doctrina del pase 6** ("categoría metodológica de prioridad temporal… no constituye una calificación normativa"). Persistencia en tres párrafos con los rangos, el trade-off, la histéresis y los 4.000/2.000 y 7.000/3.000 ms. Motor reducido a requisitos, **sin nombrar estados** (cierra la inconsistencia 4 vs 5 con §17.3). Tabla 21 y su nota intactas. PR-05/PR-06 en dos párrafos, con la oración puente al diseño. **Se restituyen los huecos de símbolos** de .3.2/.3.3 escribiendo "TTFD y latencia de alerta del sistema" y "tramo computacional por cuadro" como texto. |
| 17.1.5.4 + .4.1–.4.4 | **17.1.5.3** | Un párrafo ancla que remite al análisis de modelos OVD para Zhou/Du/Gu y **conserva FG-OVD/OVDEval con el fundamento de los hard negatives** (no está en §15/§16). Las dos definiciones (matriz de prompts, composición del vocabulario activo) suben acá. Cuatro ejes en cuatro párrafos sin rótulos. E-DIR/E-IND/E-HYB nacen acá. Tamaño del vocabulario reducido a consecuencia + cita agrupada. Idioma en un párrafo sin el recorrido por los cinco modelos. Una sola remisión a la Tabla C.1 con el acta de congelamiento y la salvedad CR-03/CR-04. **Kim (2024) cae.** |
| 17.1.5.4.5 | **17.1.5.4** | Cinco fases con rótulo corto en negrita (formato ya usado por el documento), cada una en un párrafo. Todo el pre-registro intacto (20 %, kappa, IoU, 200 positivos, n efectivo + IC 95 % bootstrap, hiperparámetros congelados, métricas por entidad componente, congelamiento previo). Cierre con el artefacto de reproducibilidad. |
| 17.1.5.5 Síntesis | eliminada | Sus dos definiciones subieron a 17.1.5.3. |

**Referencias cruzadas actualizadas (las cuatro de §B):** §17.1.3.2 → 17.1.5.2 · tabla de
§17.1.6.1.3 → 17.1.5.1 · §17.1.7.7.5 → 17.1.5.2 · nota de la Tabla C.1 → 17.1.5.3. Ninguna
referencia a numeración de tercer nivel (`17.1.5.x.y`) sobrevive en el documento.

**Medición v1.9 → v1.10:** 24.851 → **21.779 palabras** (−3.072) · 100 → **83 títulos** (−17 =
21 − 4) · §17.1.5: 7.351 → **4.421 palabras de prosa** (−40 %, dentro del 35–45 % estimado) ·
76 ecuaciones · 24 tablas · 45 saltos de sección · 1 comentario (el del colega) · 0 marcas de
revisión · `verificar_entregable.py` OK sin marcadores. El diff de texto contra la v1.9 es
exactamente el tramo §17.1.5 más las cuatro referencias.

**Decisiones tomadas en este pase que el usuario puede revertir con una oración cada una:**
Mazor et al. (2021) y Kim et al. (2024) ya no se citan en el informe (D-1). La v1.8 archivada
conserva ambas oraciones.

**Pendiente (no es de este pase):** los hallazgos A-1…A-4 de la rama de GPT (26 comentarios,
Tablas 18/19, contenido de §17.1.4, celdas de la Tabla C.3, Heading 3 en §17.1.4.2) · la cadena
fuera del `.docx` (D-5: re-extraer `90f`, regenerar el kit, nota D-E2-2 del generador → §17.1.5.3,
tablero) · §17.1.7.7.5 sigue con sus tres párrafos de severidad (D-7, revisar en la integración).
