# Correcciones — pase 3 sobre §17.3 (Diseño), §17.4 (Implementación) y restricciones para §17.5

**Fecha:** 2026-08-22 · **Insumos:** los **40 comentarios en 29 hilos** que quedaron en
`E-OVRT-VDP_Seccion_17.3_Diseno_Arquitectonico_v1.1.docx` (37 comentarios) y
`E-OVRT-VDP_Seccion_17.4_Implementacion_v1.2.docx` (3), extraídos de `word/comments.xml` con sus hilos,
anclajes y respuestas.
**Verificación:** cada afirmación de repetición, cada referencia cruzada y cada hecho técnico de este
documento fue contrastado el 2026-08-22 contra el texto extraído de ambos `.docx`, contra las secciones
cerradas del informe (`E-OVRT-VDP_v1.1_05062026-sin-etapa3.docx`) y contra el código de los cinco
repositorios. El procedimiento de re-verificación está en §E.

**Relación con los pases 1 y 2.** Este pase **continúa la numeración** (§17.3 desde **E3-32**, §17.4 desde
**E4-27**; con las adiciones del mismo día llega a **E3-42** y **E4-30**) y **no reabre** ninguna decisión
firmada. Siguen rigiendo D1–D4 y la regla de autocontención del
pase 1, y D-P2-1…D-P2-6 del pase 2. **Dos unidades del pase 2 se enmiendan** por hechos verificados en
este pase, no por cambio de criterio: **E3-22** (produciría una duplicación) y **E4-22** (afirma algo falso).
Las enmiendas están en §A y son parte de este pase; el texto del pase 2 no se reescribe.

**Numeración de tablas usada acá:** la **vigente en los `.docx`** (§17.3 = Tablas 39–62; §17.4 = 63–69).
El mapa resultante de aplicar los tres pases está en §G.

> ✎ **Dos defectos del propio kit, corregidos al abrir este pase (2026-08-22).**
> 1. `entregable/90-etapa3-texto-extraido.md` —el texto base de §17.3 que el generador entrega a la etapa 3—
>    era la extracción **v0.1**: 24.389 palabras contra las 20.622 de la v1.1 vigente, y decía "contratos
>    preliminares" donde el informe hoy dice "contratos versionados". **Regenerado** desde el `.docx` vigente
>    (regla D-C). Diferencia: 728 líneas fuera, 517 dentro.
> 2. La etapa 4 no tenía texto base extraído: el generador entregaba `borradores/17-4.md`, el borrador previo
>    al pegado y **anterior al pase 2**. Se agregó **`entregable/90b-etapa4-texto-extraido.md`** con la
>    extracción de la v1.2 vigente; el borrador se conserva como material, ya no como base.

---

## Decisiones que rigen este pase

- **D-P3-1 — Propósito por sección, y alineación entre secciones.** *(directiva del usuario, 2026-08-22)*
  Una subsección se justifica cuando **sostiene algo que ninguna otra sostiene**. El criterio se aplica en
  tres preguntas, en este orden:
  1. **¿Qué afirma que no esté afirmado antes?** Si la respuesta es "nada", la subsección se elimina y su
     aporte —si lo tiene— se reubica en la sección que ya es dueña del concepto.
  2. **¿Se pisa con otra?** Dos subsecciones que responden la misma pregunta desde ángulos distintos se
     funden o se reparten explícitamente el terreno.
  3. **¿Su título anuncia lo que hace?** Si no, se retitula. Un título que promete lo que la sección no
     entrega es una repetición encubierta.
- **D-P3-2 — Poda quirúrgica, no estructural.** *(decisión del usuario, 2026-08-22)* Se eliminan párrafos
  verificados como duplicado y se resumen las subsecciones huecas. **No** se colapsan bloques enteros de
  subsecciones para ahorrar numeración. Dos subsecciones desaparecen en este pase (§17.3.6.7 y §17.3.7.4)
  y lo hacen porque quedaron sin contenido propio, no por presupuesto de páginas.
- **D-P3-3 — Alcance: etapas 3, 4 y 5. Las etapas 1 y 2 al final.** *(decisión del usuario, 2026-08-22)*
  §17.5 todavía no está redactada: para ella este pase **no corrige, restringe** (§D). Corolario duro:
  **§17.3 y §17.4 no pueden depender de una edición futura en §17.1**. Donde el pase 1 había resuelto un
  problema de §17.3 mediante un ajuste en etapa 2, este pase lo resuelve **dentro de §17.3**, y el ajuste de
  etapa 2 pasa de obligatorio a armonizador (ver **E3-42**).
- **D-P3-4 — Un concepto se define donde se decide.** Extiende el criterio ya usado en la enmienda a E3-28:
  el término se nombra y se glosa **en prosa**, **en la subsección que es dueña de la decisión**, y los usos
  posteriores lo referencian sin redefinirlo. Nunca en una celda de tabla, nunca dos veces.
- **D-P3-5 — Un calco no es un término técnico.** Se normalizan (a) los calcos del inglés que tienen un
  equivalente castellano corriente y (b) los anglicismos crudos **que el propio informe ya normalizó en otro
  pasaje** —el defecto no es el anglicismo, es la inconsistencia—. **No** se persiguen los términos técnicos
  sin equivalente establecido ni los literales de configuración (ver la lista cerrada en **E3-33**).
- **D-P3-6 — §17.5 se organiza por pregunta de medición, no por cronología de campañas.** *(decisión del
  usuario, 2026-08-22.)* La sección es un **resumen de resultados**: reporta qué se midió y cuánto dio,
  organizado por la pregunta que cada medición responde — **nunca por el orden en que se experimentó**. Los
  identificadores de campaña (T1/G1/R1–R6/B1/D1/H1/I1/I2…) aparecen como **procedencia del dato**, jamás
  como estructura del texto: ningún título de subsección lleva nombre de campaña. La sección justifica
  **todos los caminos**: los adoptados (con su criterio pre-registrado), los probados y no adoptados (con
  el veredicto que los descartó) y los **no ejecutados o no implementados, con su factor de justificación**
  — la exclusión se lee como alcance declarado, no como omisión. El esquema concreto está en §D.0.
  ⚠ Trampa que la reorganización temática vuelve más peligrosa: la campaña "T1" del banco de clips y el
  tramo "T1" del ajuste fino **no son lo mismo** — al convivir en una sola sección, cada mención dice de
  cuál habla.
- **Heredadas:** regla de autocontención (el informe no referencia documentos locales, ADRs, fichas ni
  índices del repositorio; **sí** referencia sus propias secciones), carácter orientativo de los textos guía
  (reformulables conservando contenido y registro académico; decimales con coma, milisegundos como
  "4.000 ms"), y D-P2-1 (criterio de tabla), D-P2-5 y D-P2-6 (identificadores versionados).

---

## A. Enmiendas a dos unidades del pase 2

### ✎ ENMIENDA a E3-22 · §17.3.2 — las viñetas propuestas ya existen como prosa

**Por qué se enmienda.** E3-22 propone reemplazar la Tabla 39 por seis viñetas insumo → decisión. Verificado
contra el `.docx` v1.1: **esas seis viñetas ya están escritas**, como los seis párrafos que arrancan en
*"La arquitectura propuesta se deriva de las definiciones metodológicas consolidadas en las secciones
anteriores…"* y desarrollan uno por uno el marco teórico, el núcleo CR-01/CR-02, los escenarios, los roles,
el marco de métricas y los lineamientos ético-legales. Aplicar E3-22 tal cual dejaría **dos** enunciados del
mismo contenido donde hoy hay tres.

**El estado real de §17.3.2 (1.197 palabras) es una triplicación:**

| Bloque | Qué dice | Veredicto |
| --- | --- | --- |
| Cuatro párrafos introductorios | insumos, prioridad CR-01/CR-02, DBE/EBE, y el puente a la tabla | duplican tres de los seis párrafos de abajo, uno casi palabra por palabra |
| Tabla 39 (6 × 3) | insumo → criterio → decisión | mediana de 125 caracteres por celda; su columna del medio resume §17.1 |
| Seis párrafos desarrollados | el vínculo insumo → decisión, uno por insumo | **es el texto que se queda** |

La duplicación literal: ¶1 dice *"La arquitectura propuesta **se construye a partir de** las definiciones
metodológicas consolidadas en las secciones anteriores. En particular, toma como insumos el alcance
experimental…"* y ¶5 dice *"La arquitectura propuesta **se deriva de** las definiciones metodológicas
consolidadas en las secciones anteriores. El alcance experimental, las condiciones de riesgo…"*.

**Acción — tres ediciones.**

1. **Eliminar la Tabla 39, su Nota y la oración que la introduce** (*"La Tabla 39 sintetiza esta relación
   entre definiciones previas y decisiones arquitectónicas derivadas."*).
2. **No crear las viñetas de E3-22.** Esa acción queda derogada por esta enmienda.
3. **Reemplazar los cuatro párrafos introductorios por un párrafo de entrada.** Texto guía:

   > *"La arquitectura propuesta se deriva de las definiciones metodológicas ya consolidadas: el alcance
   > experimental del prototipo, el catálogo de condiciones de riesgo, los escenarios de evaluación, los
   > roles funcionales del entorno, el marco de métricas y los lineamientos ético-legales actúan como
   > restricciones de diseño. Lo que sigue no reitera el protocolo experimental: explicita qué consecuencia
   > arquitectónica se deriva de cada uno de esos insumos, de modo que ningún módulo, frontera o flujo del
   > sistema aparezca como una decisión aislada."*

4. Los seis párrafos desarrollados se conservan **menos el de CPN, EN y TN**, que pasa a **E3-34**.

**Resultado:** 1.197 → ~600 palabras. **−1 tabla, −4 párrafos, un solo enunciado del vínculo insumo → decisión.**

*Origen: hilo C0 de §17.3 (vos: "como para sacar la tabla y acortar" · "sí tiene sentido la sección…, lo que
quería sacar es la tabla") y las dos respuestas de Gabriel ("podría ser más resumido" · "lo que está después
va, esto lo volaría").*

---

### ✎ ENMIENDA a E4-22 · §17.4.10, Tabla 68 — la preselección en el borde **sí se ejerció**

**Por qué se enmienda.** E4-22 propone una fila que dice *"no ejercida"* y *"no puede reclamarse como
propiedad verificada del prototipo"*. **Ambas afirmaciones son falsas.** Verificado contra el código y contra
el registro operativo:

| Hecho | Evidencia |
| --- | --- |
| La preselección está **implementada** | Filtro de personas ejecutado en el propio dispositivo de captura, con umbral, ventana de evidencia, latido incondicional y apertura total ante silencio de la red neuronal; validación que impide configurar una apertura posterior al vencimiento de la evidencia. Deshabilitada por defecto. |
| Está implementada **sólo para la cámara propia** | El esquema de configuración la rechaza para cualquier otro tipo de fuente. Para las fuentes por red no existe. |
| Su efecto está **medido** | Comparación pareada contra el flujo completo con el mismo detector: **87 % de unidades descartadas en el dispositivo**. |
| Estuvo **apagada en todo lo evaluativo**, por decisión previa a los resultados | Un filtro de fotogramas sin persona suprime justamente las detecciones sostenidas que la tasa de falsos positivos por hora existe para medir; y agrega el error multiplicativo de un detector más débil sobre la cadena que se quiere caracterizar. |

Es decir: no es una brecha, es **una capacidad implementada y medida cuya exclusión de lo evaluativo es un
resultado metodológico**. La versión de E4-22 convierte un acierto del trabajo en un agujero.

**Acción — reemplazar la fila propuesta por E4-22 por ésta** (misma posición: después de *Condiciones de
riesgo de nivel 2 y 3*):

> **Preselección liviana en el rol de captura** ||
> *Implementada para la fuente de captura propia como filtro de personas ejecutado en el dispositivo, con
> criterio de degradación segura y deshabilitada por defecto; su reducción de carga se midió en una
> comparación pareada contra el flujo completo, con un 87 % de unidades descartadas antes de salir de la
> cámara. No existe para las fuentes por red. Permaneció deshabilitada en todas las corridas evaluativas.* ||
> *La exclusión de lo evaluativo es deliberada y anterior a los resultados: un filtro de fotogramas sin
> persona suprimiría las detecciones sostenidas que la tasa de falsos positivos por hora existe para medir, y
> superpondría el error de un detector auxiliar más débil sobre la cadena que se busca caracterizar.
> Habilitarlo cambiaría la procedencia de esas métricas en lugar de mejorarlas. La capacidad se reporta,
> entonces, como implementada y caracterizada fuera del régimen evaluativo.*

**Se conserva de E4-22:** el diagnóstico (once menciones en §17.3 contra cero en §17.4 era, efectivamente, un
agujero de rendición de cuentas) y el complemento recomendado de bajar la huella en §17.3.

**Consecuencia para §17.5:** si §17.5 vuelve a citar el 87 %, debe hacerlo con su denominador y su condición
de medición. Si no lo hace, esta celda es su único lugar en el informe y así queda declarado en §D.

*Origen: C20 de §17.3 ("esto en oakd lo hicimos. asegurarse que esté claro en etapa 4. RTSP no lo hicimos").*

---

## B. Correcciones nuevas a §17.3 — Diseño Arquitectónico

> **Dato que ordena todo este bloque:** §17.3 pesa **20.622 palabras** contra **5.477** de §17.4 — 3,8 a 1
> entre el diseño y su materialización. Las quince repeticiones que siguen fueron verificadas una por una
> contra el texto; ninguna se corrige por impresión de extensión.

### E3-33 · Calcos del inglés y anglicismos que el informe ya normalizó en otro pasaje

**Problema.** Dos comentarios apuntan a traducciones malas (*"traducción chotísima, mejorar o cambiar esa
palabra"* sobre **frescura**; *"otra traducción muy chota"* sobre **fuentes vivas**). Relevado el capítulo
completo, el defecto es más amplio y tiene dos formas distintas, que se tratan distinto.

**(a) Calcos con equivalente castellano corriente — se reemplazan.**

| Término | Apariciones | Reemplazo único | Nota |
| --- | --- | --- | --- |
| `frescura` | 5 | **actualidad** (en enumeraciones) · **actualidad de la unidad visual** (donde nombra la política) | Calco de *freshness*. La política que nombra es "preferir la unidad más reciente"; "frescura" no dice eso en castellano técnico. |
| `fuente viva` / `fuentes vivas` | 9, más una forma verbal (*"la fuente es viva"*) | **fuente en vivo** / **fuentes en vivo** | Calco de *live source*. El informe **ya dice "en vivo"** en §17.3.8.4 (*"una corrida viva"* → también se normaliza), en §17.4.4 y en §17.4.5 (*"corrida en vivo"*, *"camino de ejecución en vivo"*): el reemplazo alinea, no innova. Alcanza al título de §17.3.14.2, que pasa a **"EBE como escenario de fuente en vivo controlada"**. |
| `pulleable` | 1 (§17.3.7.3) | perífrasis | *"…o en general con **fuentes cuya lectura puede regularse** —conjuntos de imágenes, videos locales o archivos—"*. Nadie lo marcó, pero es el peor de los tres. |

**(b) Anglicismos crudos que el propio informe ya tradujo en otro lugar — se alinean.** El defecto acá no es
el anglicismo: es que el mismo capítulo usa las dos formas.

| Término | Dónde sobrevive tras los pases 1 y 2 | Forma ya usada en el informe |
| --- | --- | --- |
| `PUB/SUB` | §17.3.8.1, §17.3.8.4 | **publicador-suscriptor** (§17.3.5, §17.3.18) |
| `config-driven` | §17.3.18 | **gobernado por configuración** (§17.3.5, §17.4.4) — E3-19 ya lo saca de DA-03 |
| `outcome` | §17.3.10.2 (Tabla 48), §17.3.13.1 (Tabla 53), §17.3.13.3 (Tabla 55) | **resultado de entrega** / **resultado del canal** (§17.3.10.1, §17.3.10.3) |
| `backpressure` | §17.3.14.5 (Tabla 57) | **acumulación de atraso** (§17.3.7.3, §17.3.14.4) |
| `keep-up` | §17.3.16 (Tabla 59) | **capacidad de sostener el ritmo** |
| `letterbox` | §17.3.7.1 | **relleno de bordes** |

**(c) Lista cerrada de lo que NO se toca, con su razón** — para que no se "corrija" por las dudas en un pase
posterior: `checkpoint`, `ledger`, `frame`, `buffer`, `tracker`, `streaming`, `snapshot`, `bounding box`,
`jitter` (términos técnicos sin equivalente castellano establecido en la literatura del dominio);
`fail-open` (queda glosado una sola vez por la enmienda a E3-28, que es la doctrina D-P3-4 aplicada); y
`scene` / `subject` (son **valores literales de configuración**, no prosa: nombran lo que se escribe en el
archivo de patrones).

*Origen: C5 y C6 de §17.3.*

---

### E3-34 · CPN, EN y TN se explican **tres veces** en el informe

**Problema — verificado sobre el `.docx` maestro.** Los tres roles quedan definidos en la consolidación
metodológica (§17.1.4.2 y sus tres sub-apartados), con este texto:

> *"…el Central Processing Node (CPN) concentra la ejecución del pipeline principal, la inferencia, la
> evaluación de patrones, la medición de latencia y la consolidación de resultados experimentales. El Edge
> Node (EN) se ubica próximo a la fuente visual y se orienta a captura, transmisión de video y eventual
> preprocesamiento liviano. El Training Node (TN), cuando corresponda, se reserva para tareas de ajuste o
> preparación de variantes de modelo, sin sustituir la evaluación operativa sobre el CPN."*

§17.3 lo vuelve a decir **dos veces más**, casi con las mismas palabras: en §17.3.2 (*"El CPN concentra las
capacidades centrales de procesamiento y evaluación; el EN representa la captura o el procesamiento próximo
a la fuente; y el TN delimita las tareas de entrenamiento o adaptación cuando corresponden"*) y en la
apertura de §17.3.15. Es el mismo párrafo tres veces en el mismo documento.

**Acción — dos ediciones. En ninguna de las dos §17.3 redefine los roles.**

1. **§17.3.2 — reemplazar el párrafo de roles por su consecuencia arquitectónica**, que es lo único que
   corresponde a esta sección (la sección trata de qué se *deriva* de cada insumo, no de qué *es* cada insumo):

   > *"De los roles funcionales ya establecidos se deriva una restricción de diseño y no una nueva
   > definición: se adoptan como responsabilidades de referencia que permiten declarar dónde se captura,
   > dónde se ejecuta la inferencia y dónde se prepara una variante ajustada, sin que la distribución física
   > de componentes pase a formar parte de la semántica de los contratos."*

2. **§17.3.15 — reemplazar el primer párrafo por una entrada que remita y no repita.** El resto de la
   sección (topología de referencia, el TN fuera del camino de inferencia, el módulo de distribución como
   unidad desplegable) es contenido propio y se conserva:

   > *"Esta sección no redefine los roles funcionales ya establecidos en la consolidación metodológica: fija
   > la topología de referencia con la que se materializan en el prototipo y ubica en ella al módulo de
   > distribución. La única precisión que el diseño agrega es que ninguno de los tres roles equivale
   > necesariamente a una máquina dedicada."*

*Origen: C7 y el hilo C35/C36 de §17.3 ("esto ya está claro en etapa 2, no volver a explicar acá" · "o
introducir brevemente haciendo referencia a la sección de la etapa 2"). La remisión a una sección **propia**
del informe no viola la autocontención, que alcanza a documentos del repositorio.*

---

### E3-35 · §17.3.6.7 "Frontera con los planos de ejecución y el soporte experimental" — eliminar y reubicar

**Problema.** La subsección tiene tres párrafos y **dos de ellos ya están dichos**:

| Párrafo | Qué dice | Dónde ya está |
| --- | --- | --- |
| 1 | La configuración define los parámetros del plano de medios; el plano de medios los aplica pero no los diseña ni versiona. | §17.3.7, párrafo de apertura, con más precisión; y otra vez en §17.3.7.4 (que **E3-36** elimina por lo mismo). |
| 2 | Para el plano de control, la configuración define patrones, severidad, ventanas, histéresis. | Tabla 44, fila *Patrones activos*; y §17.3.8.3.1 completo. |
| 3 | Para el soporte experimental, la configuración es la clave de reconstrucción. | Es lo único propio, y aun así §17.3.12.1 lo repite (*"Toda alerta puede reconstruirse hasta la configuración efectiva…"*). |

Es exactamente el caso de §17.3.6.6, que **E3-20** ya resolvió con poda y reubicación, y por eso Gabriel pide
el mismo tratamiento.

**Acción — eliminar la subsección y rescatar una oración**, al cierre de §17.3.6.1 (*"Función arquitectónica
de la configuración experimental"*, que es la dueña del concepto):

> *"Esa función de gobierno se proyecta sobre los tres destinatarios de la configuración: el plano de medios
> recibe los parámetros que aplica sin diseñarlos ni versionarlos, el plano de control recibe los criterios
> con los que evalúa, y el soporte experimental la utiliza como clave de reconstrucción, de modo que todo
> evento, métrica, alerta o evidencia conservada pueda rastrearse hasta la corrida que le dio origen."*

⚠ **Consecuencia de numeración, encadenada con E3-20.** E3-20 elimina §17.3.6.6 y corre §17.3.6.7 → §17.3.6.6.
Con E3-35 esa subsección también desaparece: **§17.3.6 queda con cinco subsecciones (6.1 a 6.5)**, sin
renumeración adicional respecto de lo que ya fija E3-20.

*Origen: C15 de §17.3 ("ídem a lo anterior… es una sección que no tiene tanto propósito en sí misma, podría
rescatarse mucho más resumida entre 17.3.6.1 y 6.2").*

---

### E3-36 · §17.3.7.4 "Relación con configuración, modelos y prompts" — eliminar, salvo su último párrafo

**Problema — la subsección entera es eco, con una sola excepción.** Cuatro párrafos, 263 palabras:

| Párrafo | Veredicto |
| --- | --- |
| 1 — *"El Pipeline de Medios consume la configuración experimental definida para la corrida, pero no la gobierna…"* | **Duplicado casi literal** del párrafo de apertura de §17.3.7: *"La configuración experimental actúa como entrada transversal del Pipeline de Medios, pero no es una responsabilidad interna de este plano… sin convertirse en el módulo encargado de gobernarla o versionarla."* |
| 2 — prompts como contexto semántico | Ya está en §17.3.6.3 y en §17.3.7 (apertura). **Excepción:** la oración sobre reutilizar representaciones textuales precalculadas es un compromiso de diseño que no aparece en ningún otro lado — se rescata. |
| 3 — la salida debe incluir referencias suficientes para reconstruir el origen | Es el cuarto criterio de §17.3.7.2 (*"conservar la trazabilidad mínima del resultado perceptivo"*) y el cierre de §17.3.7.1. |
| 4 — la salida no se reduce a cajas y puntajes, pero tampoco incorpora severidad ni decisión de alerta | **Es el único aporte propio de la subsección.** |

**Acción — eliminar §17.3.7.4** y reubicar sus dos rescates:

1. **El párrafo 4 pasa a cerrar §17.3.7.1** (*"Flujo operativo del Pipeline de Medios"*), inmediatamente
   después del bloque **Publicación de evidencia perceptiva**, que es donde el tema es la salida:

   > *"En consecuencia, la salida del plano de medios no se reduce a cajas y puntajes sin contexto, pero
   > tampoco incorpora severidad, confirmación de patrón ni decisión de alerta. Su producto es evidencia
   > visual primaria, normalizada y trazable: la interpretación de esa evidencia corresponde al plano de
   > control, y la comparación entre configuraciones, modelos y prompts, al análisis experimental posterior."*

2. **La oración sobre representaciones precalculadas se anexa al bloque Inferencia open-vocabulary** de
   §17.3.7.1:

   > *"…según el formato propio del detector utilizado. Cuando el modelo lo permita, el adaptador puede
   > reutilizar representaciones textuales precalculadas o mecanismos equivalentes para reducir el costo de
   > inferencia, siempre que esa optimización no altere la trazabilidad de la corrida."*

⚠ **Consecuencia de numeración:** §17.3.7.5 pasa a **§17.3.7.4**. §17.3.7 queda con cuatro subsecciones.
Esto **afecta a la enmienda de E3-28**, cuya acción 3 reescribe el primer párrafo de "§17.3.7.5": la unidad
sigue siendo la misma —*"Capacidades opcionales sin desplazar el núcleo validable"*— y pasa a numerarse 7.4.
La enmienda a E3-28 ya previó este riesgo y por eso su ancla en §17.3.14.5 es descriptiva y no numérica.

*Origen: C18 y C19 de §17.3 ("esta sección es repetitiva, lo único rescatable es el último párrafo, reducir"
· "ya se dijo 20 veces").*

---

### E3-37 · §17.3.7.5 — los dos cierres que repiten la apertura del plano de medios

**Problema.** Dos pasajes concretos, ambos verificados:

1. **Última oración del segundo párrafo:** *"La decisión de que una detección persistió durante una ventana
   temporal sigue perteneciendo al motor de patrones."* Es el **quinto criterio de §17.3.7.2**, dos
   subsecciones antes: *"La persistencia temporal de un patrón, la histéresis, la severidad y el registro
   interno de alerta pertenecen al motor de patrones. El plano de medios… no debe decidir si una condición
   observada se convirtió en una situación de riesgo confirmada."*
2. **El párrafo de cierre completo** (*"Con esta delimitación, el Pipeline de Medios queda definido como una
   ruta de transformación acotada y medible: recibe entrada visual, controla el ritmo…"*) es la enumeración
   del **párrafo de apertura de §17.3.7**, que ya dijo *"Su alcance incluye ingesta, decodificación cuando
   corresponda, control de ritmo, normalización visual, inferencia open-vocabulary, postproceso y publicación
   no bloqueante"* y *"El Pipeline de Medios no confirma condiciones de riesgo, no asigna severidad, no
   ejecuta reglas de patrón, no genera alertas"*. Un cierre que repite la apertura no cierra: reinicia.

**Acción.**

1. Eliminar la oración del punto 1. El párrafo termina en *"…un identificador temporal no equivale a una
   condición de riesgo sostenida."*
2. Eliminar el párrafo de cierre completo. La subsección termina en el párrafo de variantes de eficiencia,
   cuya última oración ya cierra bien (*"…cualquier variante que altere la ruta frame-evento debe quedar
   declarada en la configuración de corrida"*).

⚠ **El primer párrafo de esta subsección lo reescribe la enmienda a E3-28** (ahí nace `fail-open`): esa
reescritura manda, y E3-37 no la toca. Resultado combinado: tres párrafos —el de E3-28, el de tracking sin
la oración repetida, y el de variantes de eficiencia—.

*Origen: C21 ("este tipo de aclaraciones repetitivas son una pija") y C22 ("esto ya se dijo antessss").*

---

### E3-38 · §17.3.8.3.1 — el mismo párrafo, dos párrafos después

**Problema.** La subsección dice lo mismo en el primer par de párrafos y en el tercero:

> **¶1:** *"Cada patrón referencia una condición del catálogo y define cómo esa condición debe ser evaluada
> durante la corrida."*
> **¶2:** *"…indica qué evidencia acepta, durante cuánto tiempo debe sostenerse, qué severidad tiene, qué
> histéresis aplica y qué evento debe emitirse cuando cambia de estado."*
> **¶3:** *"Cada patrón referencia una condición observable del catálogo CR-01 a CR-06 y define cómo esa
> condición será evaluada dentro del plano de control: evidencia requerida, ventana temporal, umbrales,
> histéresis, severidad y dependencias opcionales."*

Lo único que ¶3 agrega y no está en ningún otro lado es **la codificación PR-01 a PR-06** y su razón de ser.

**Acción — eliminar ¶3 y anexar su aporte al final de ¶2:**

> *"…y qué evento debe emitirse cuando cambia de estado. La codificación PR-01 a PR-06 identifica cada patrón
> y lo mantiene distinguible de la condición observable que evalúa (CR-01 a CR-06): una nombra el fenómeno,
> la otra la regla operativa que decide cuándo se lo considera sostenido."*

*Origen: C24 ("lo dijo literalmente en el párrafo anterior").*

---

### E3-39 · §17.3.8.3.4 — usar las siglas de métricas que la etapa 2 ya definió

**Problema.** El párrafo que vincula transiciones con métricas las nombra en castellano largo y no usa las
siglas, aunque **las tres están definidas con su sigla en la consolidación metodológica**: verificado en
§17.1.7.5.1 *Latencia de Alerta (t_alert-system)* —la sigla viaja como ecuación de Word, por eso no aparece
en las extracciones planas—, §17.1.7.5.2 *Tiempo a la Primera Detección (TTFD)* y §17.1.7.5.3 *Tasa de
Detección Sostenida (SDR)*. El resultado es que el lector no puede conectar este párrafo con la Tabla 54, que
las nombra por sigla cinco subsecciones más adelante.

**Acción — reescribir el tercer párrafo:**

> *"Las métricas operativas del plano de control se apoyan en estas transiciones: el tiempo hasta la primera
> detección (TTFD) se ancla en la primera evidencia perceptiva relevante; la latencia de alerta
> (t_alert-system) se cierra con el registro de la alerta interna que sigue a la transición a confirmado; la
> tasa de detección sostenida (SDR) se calcula sobre la continuidad del episodio; y los errores o descartes
> permiten distinguir una ausencia real de evidencia de una falla técnica o de una pérdida por muestreo."*

**No hay referencia hacia adelante:** las tres siglas nacen en §17.1, no en la Tabla 54. Al usarlas acá por
primera vez dentro de §17.3 se escribe el nombre completo delante, como en el texto guía; a partir de la
Tabla 53 el capítulo ya las usa solas.

*Origen: C26 ("usar siglas de las métricas que ya definimos").*

---

### E3-40 · §17.3.9 — la cadena condición → alerta se explica por cuarta vez

**Problema.** §17.3.9 llega después de que §17.3.7 y §17.3.8 ya recorrieron la cadena completa, y en vez de
aportar lo suyo —el **vínculo** entre condición metodológica y materialización, que sí es propio— vuelve a
narrar el funcionamiento del plano de control. Tres puntos verificados:

- **§17.3.9.1**, tercer párrafo: *"Allí se aplican criterios de persistencia, histéresis, severidad
  configurada… Sólo cuando el patrón alcanza una transición válida a confirmado se registra una alerta
  interna por episodio."* Ya dicho en §17.3.8 (apertura), §17.3.8.1, §17.3.8.2 y §17.3.8.3.
- **§17.3.9.2** repite dos veces dentro de sí misma: el primer párrafo dice *"El plano de medios consulta
  person, helmet y vest; el plano de control relaciona cada sujeto con la evidencia…"* y el segundo lo
  reformula como *"El plano de medios informa qué entidades observó… El plano de control decide si la
  evidencia de casco o chaleco se asocia al sujeto"*. Además el primero duplica §17.3.6.4.
- **§17.3.9.3**, segundo párrafo: *"La confirmación no es un hecho aislado: depende de detecciones
  acumuladas, criterios de persistencia, histéresis, severidad configurada y reglas activas. Por ello, la
  alerta interna debe poder reconstruirse desde la cadena completa…"* es §17.3.8.3.4, segundo párrafo.

**Decisión sobre §17.3.9.2 (era pregunta abierta en el hilo C28/C29).** **Se conserva**, podada. Es el único
lugar del informe donde la estrategia del núcleo está enunciada como **decisión adoptada** con su frontera
medios/control; borrarla dejaría a E-IND existiendo sólo dentro de celdas de tabla y de párrafos que la
mencionan de paso. Lo que se elimina es la reexplicación, no la decisión.

**Acción — tres ediciones.**

1. **§17.3.9.1 — reescribir el tercer párrafo** para que sea el eslabón y no el resumen del motor:

   > *"El plano de control evalúa esa evidencia mediante el patrón correspondiente y, cuando la evaluación
   > confirma el episodio, registra una alerta interna. Esa alerta es una salida asistiva del sistema: no
   > equivale a una notificación externa ni a una certificación normativa."*

2. **§17.3.9.2 — de cuatro párrafos a dos.** El primero enuncia la decisión y la frontera; el segundo, la
   razón y las ramas comparativas:

   > *"Para el núcleo validable se adopta la estrategia indirecta con inferencia espacial de ausencia
   > (E-IND). La frontera que esa elección fija es explícita: el plano de medios informa qué entidades
   > observó, dónde y con qué confianza; el plano de control decide si la evidencia del elemento de
   > protección se asocia al sujeto, construye el estado evaluable de la condición y lo estabiliza antes de
   > registrar una alerta."*
   >
   > *"La estrategia se adopta por auditabilidad: cada evaluación puede reconstruirse a partir de la caja del
   > sujeto, la región analizada, las detecciones de protección, los umbrales y la regla aplicada, de modo
   > que la ausencia no se presenta como una conclusión opaca del modelo. La detección directa (E-DIR) y las
   > variantes híbridas (E-HYB) se conservan como ramas comparativas configurables, con conjuntos de prompts
   > y reglas identificados por separado; comparten los contratos de publicación, evaluación temporal y
   > registro, de modo que la comparación no requiera alterar la arquitectura central."*

3. **§17.3.9.3 — retitular y reescribir.** Hoy se titula *"Trazabilidad de la cadena causal"* y se pisa con
   §17.3.8.3.4 y con §17.3.12 entera. Lo que **sólo ella** sostiene es otra cosa: que la variante de
   estrategia quede registrada en los eventos es lo que hace comparables dos corridas. El nuevo título es
   **"Comparabilidad entre estrategias"** y el cuerpo:

   > *"Para que la comparación entre variantes sea posible, cada evidencia publicada conserva el vínculo con
   > la condición que representa, la estrategia de detección utilizada y la configuración efectiva de la
   > corrida. Una misma condición puede evaluarse con distintas estrategias sin alterar la semántica del
   > sistema, siempre que la corrida declare la variante utilizada y los eventos resultantes conserven esa
   > referencia. Es esa referencia declarada, y no una reinterpretación posterior de los artefactos, la que
   > permite atribuir una diferencia de resultados a la estrategia evaluada y no a un cambio no declarado en
   > la cadena."*

**Resultado:** §17.3.9 pasa de 678 a ~400 palabras, conserva sus tres subsecciones y cada una responde una
pregunta distinta (cómo se traduce · qué se adoptó · por qué se puede comparar).

*Origen: C27 ("ya se dijo antes, no repetir huevadas"), el hilo C28/C29 ("¿la dejamos como constitución o la
borramos?" · "el fabio decide"), C30 y C31 ("esto ya está claro" · "esto también").*

---

### E3-41 · §17.3.10 — la sección no tiene entrada y su primera subsección la suple mal

**Problema.** §17.3.10 *"Distribución de alertas confirmadas"* es la **única sección de §17.3 con cero
palabras propias**: el título va directo a §17.3.10.1. Esa subsección termina haciendo dos trabajos y no hace
bien ninguno. Su arranque —*"La cadena descrita hasta aquí termina en un hecho interno… Falta el último
tramo: hacer llegar esa alerta a un canal externo sin comprometer al motor que la produjo"*— es narrativo,
está fuera del registro del resto del capítulo (*"falta el último tramo"*) y, sobre todo, **no enuncia la
función arquitectónica**, que es exactamente lo que su título promete.

**Acción — dos ediciones.**

1. **§17.3.10 recupera su párrafo de entrada** (dos oraciones, antes de la primera subsección):

   > *"La alerta interna es el hecho terminal del plano de control, pero todavía no es un aviso. Esta sección
   > define el tramo que la convierte en entregas observables sin incorporar la comunicación a la ruta que la
   > produjo."*

2. **§17.3.10.1 arranca por la función**, que es lo que su título anuncia:

   > *"La función arquitectónica de la distribución es transformar una alerta ya confirmada en intentos de
   > entrega registrados, sin participar del razonamiento que la produjo. El plano de control publica cada
   > alerta confirmada en un bus de alertas dedicado; el módulo de distribución la consume desde allí, aplica
   > la política de notificación y registra el resultado de cada intento. No constituye un tercer plano ni un
   > cuarto rol funcional: es un módulo desacoplado, y esa condición es la que impide que la indisponibilidad
   > de un canal externo se propague al motor de patrones."*

Los otros dos párrafos de §17.3.10.1 (pipeline de distribución; política ordinaria) se conservan.

*Origen: C32 ("malísima esta intro").*

---

### E3-42 · §17.3.6.4 — la remisión a §17.1.5.4.2 **es falsa hoy**, y §17.3 debe dejar de depender de ella

**Problema — es el único defecto duro de referencia cruzada del capítulo.** §17.3.6.4 dice:

> *"…se mantienen en conjuntos separados para las estrategias directa (E-DIR) e híbrida (E-HYB) **definidas
> en la consolidación metodológica (sección 17.1.5.4.2)**…"*

Verificado sobre el `.docx` maestro de las secciones cerradas: **`E-DIR`, `E-IND` y `E-HYB` aparecen cero
veces en todo el informe fuera de §17.3 y §17.4.** §17.1.5.4 sí distingue las familias en prosa ("estrategia
directa", 3 apariciones; "estrategia indirecta", 5; "híbrida", 4), pero **no las bautiza con esos códigos**,
y §17.1.5.4.2 se titula *"Estrategia de Variación Sistemática"*, que es otra cosa. La remisión envía al
lector a un lugar donde no está lo que se le promete.

**Por qué no alcanza con lo ya decidido.** El pase 1 previó exactamente esto (decisión D3 y ajuste C-1:
bautizar los tres códigos en §17.1.5.4.2). Pero C-1 es una edición de **etapa 2**, y por D-P3-3 la etapa 2 se
trabaja al final. §17.3 no puede quedar colgada de una edición futura.

**Acción — §17.3 se hace autosuficiente, en tres ediciones.**

1. **§17.3.2 — quitar el código del párrafo de condiciones de riesgo.** Hoy dice *"el flujo base prioriza la
   estrategia indirecta E-IND"*; pasa a *"el flujo base prioriza la estrategia indirecta"*. Motivo: tras la
   enmienda a E3-22 ésa sería la primera aparición del código en el informe, y §17.3.2 no es la sección
   dueña del concepto (D-P3-4).
2. **§17.3.6.4 — acá nacen los tres códigos**, en el párrafo que hoy hace la remisión falsa:

   > *"Las consultas negativas o de estado observable se mantienen en conjuntos separados para las
   > estrategias directa e híbrida ya distinguidas en la consolidación metodológica, de modo que sus
   > resultados sean atribuibles a una estrategia explícita y no a una mezcla informal de vocabularios. En el
   > diseño arquitectónico y en lo que sigue del trabajo, estas familias se identifican mediante un código:
   > estrategia directa (E-DIR), cuando el prompt intenta describir la condición de riesgo completa;
   > estrategia indirecta (E-IND), cuando el detector identifica entidades visibles por separado y la
   > condición se reconstruye mediante lógica externa al modelo; y estrategia híbrida (E-HYB), cuando se
   > combinan consultas de ambos tipos bajo una regla de composición explícita."*

3. **Verificar el orden al aplicar:** con estas dos ediciones, la primera aparición de cualquiera de los tres
   códigos en el informe es la glosa de §17.3.6.4, que **precede** a la Tabla 45 (dentro de la misma
   subsección), a §17.3.9.2, a la Tabla 60 y a §17.3.18. Ninguna aparición queda antes de su definición.

**Qué pasa con C-1 del pase 1.** Deja de ser obligatorio y **pasa a ser armonizador**: si al trabajar la
etapa 2 se aplica el bautismo en §17.1.5.4.2, entonces §17.3.6.4 recorta su glosa a la remisión (*"…para las
estrategias directa (E-DIR) e híbrida (E-HYB) definidas en la consolidación metodológica"*). Si no se aplica,
el informe queda igualmente correcto y autoconsistente. **Se anota en §I como dependencia inversa**, para que
al tocar etapa 2 no se dupliquen las dos glosas.

*Origen: C11 de §17.3 ("tienen que estar definidas. revisar esto en etapa 2").*

---

## C. Correcciones nuevas a §17.4 — Implementación

### E4-27 · §17.4.10, Tabla 68 — la fila de ajuste fino afirma algo **falso hoy**, y su marcador está vencido

**Nadie lo comentó; es un hallazgo de este pase y es el defecto más grave de §17.4.** La celda de estado dice:

> *"…El tramo exploratorio adicional **fue enviado y permanece en cola, sin haber iniciado**."*

y arrastra el marcador *[[PENDIENTE: resultado y veredicto del tramo exploratorio adicional · depende de
completar su ejecución y evaluación predefinidas]]*, más una oración en la Nota de la tabla que lo sostiene
(*"El marcador del tramo exploratorio adicional permanece visible hasta que exista un artefacto evaluado; su
envío y permanencia en cola no constituyen por sí mismos un resultado"*).

**Verificado: la escalera está completa y cerrada.** El tramo adicional dejó de estar en cola, corrió, se
evaluó una sola vez contra el banco congelado y produjo veredicto negativo; y el tercer tramo se cerró con
causa técnica. Los tres puntos de la escalera están cerrados, y el hallazgo de conjunto es más fuerte que
cualquiera de ellos por separado: el límite no es de capacidad del modelo sino **estructural**, porque el
corpus de ajuste disponible es de un orden que no alcanza a sostener el número de parámetros que se ajustan.
La causa técnica del tercer tramo también es declarable sin citar nada del repositorio: el único corpus
histórico de ese volumen **comparte fuentes con el banco de evaluación congelado** y, además, derivaba la
clase de cabeza descubierta de un modo que el vocabulario canónico vigente prohíbe.

**Acción — tres ediciones.**

1. **Reemplazar la celda de estado:**

   > *"Protocolo, procedencia, servicio de inferencia, evaluación y línea base quedaron congelados, y la
   > escalera de tramos pre-registrada se ejecutó completa. Los dos tramos entrenados se evaluaron una única
   > vez contra el banco congelado y ninguno superó los criterios de incorporación, firmados antes de que
   > existiera el checkpoint que se les aplicaría. El tercer tramo se cerró con causa técnica: el único
   > corpus disponible de ese volumen comparte fuentes con el banco de evaluación y deriva la clase de cabeza
   > descubierta de una forma que el vocabulario canónico vigente no admite."*

2. **Reemplazar la celda de consecuencia, eliminando el marcador `[[PENDIENTE]]`:**

   > *"Ningún checkpoint se incorporó como modelo de servicio. El resultado es un veredicto negativo
   > pre-registrado y no un tramo abierto: los criterios y los márgenes se firmaron antes de la evaluación, y
   > las tres expectativas registradas de antemano se confirmaron. Los valores por tramo y la lectura de la
   > curva se informan en la sección 17.5."*

3. **Eliminar de la Nota de la Tabla 68** la oración sobre el marcador. El resto de la Nota se conserva.

⚠ **El otro marcador de §17.4 no se toca.** El `[[PENDIENTE]]` de §17.4.8.1 —dirección de origen y fecha de
acceso por clip del lote de obra real— **sigue vigente y sigue siendo bloqueante para la versión final**. No
se elimina ni se relaja.

---

### E4-28 · §17.4.3 "Contratos de datos materializados" — la sección más densa del capítulo

**Problema.** 197 palabras y tres párrafos para cinco contratos, con estos defectos verificados:

1. **Anuncia cinco y no los enumera.** *"Cinco contratos concentran los hechos principales de la ejecución"*
   y arranca directo con el primero; el lector cuenta hacia atrás para saber cuáles fueron.
2. **La primera oración encadena nueve complementos** (*"…incluye identificación de corrida y unidad visual,
   descripción de la fuente, perfil de modelo, conjunto de prompts, detecciones con coordenadas en píxeles y
   normalizadas, y tiempos por unidad"*). Es un inventario disfrazado de oración.
3. **Reparto desparejo:** dos contratos en el primer párrafo, tres apretados en el segundo.
4. **Las propiedades técnicas —que son el aporte de la sección— quedan escondidas** al final de subordinadas:
   la secuencia monótona que vuelve detectable el hueco, el identificador determinista que permite deduplicar
   sin estado compartido, la evidencia que hace reconstruible la ausencia.

**Cuál es el propósito que sólo esta sección tiene** (D-P3-1): la Tabla 63 de §17.4.2 ya da la
correspondencia diseño → materialización, y §17.3.11.3 ya dio la información mínima de cada contrato. Lo que
falta y sólo acá cabe es **qué propiedad técnica habilita cada contrato materializado**. La reorganización se
hace alrededor de eso.

**Acción — cuatro párrafos, uno por función, cada uno cerrando en su propiedad.** Texto guía:

> *"Cinco contratos concentran los hechos principales de la ejecución: el evento de percepción, el envoltorio
> del bus, el contrato de ciclo de vida, el evento de transición de patrón y la alerta interna. Los cinco
> están declarados con su identificador en la tabla anterior; lo que sigue precisa qué lleva cada uno y qué
> propiedad técnica habilita."*
>
> *"El evento de percepción normaliza la salida del detector. Identifica la corrida y la unidad visual;
> describe la fuente, el perfil de modelo y el conjunto de prompts efectivos; y transporta las detecciones
> con sus coordenadas en píxeles y normalizadas, sus puntajes y los tiempos medidos por unidad. Esa
> composición es la que permite que una detección se atribuya después a una variable concreta de la corrida y
> no a una combinación desconocida."*
>
> *"El envoltorio del bus encapsula ese mismo contenido para transmitirlo y le agrega un número de secuencia
> monótono; el contrato de ciclo de vida delimita el inicio y el cierre de la corrida. Juntos habilitan dos
> propiedades que la persistencia sola no da: cualquier pérdida en el transporte se vuelve detectable como un
> hueco de secuencia en lugar de pasar por ausencia de evidencia, y el final lógico de la corrida se
> distingue de una interrupción, de modo que los consumidores puedan cerrarse y los artefactos consolidarse."*
>
> *"El evento de transición registra los cambios entre los estados del patrón —los mismos que fija la máquina
> de estados del diseño— junto con la evidencia y los hitos temporales que los motivaron; la alerta interna
> registra la confirmación del episodio con un identificador determinista, de modo que reprocesar la misma
> corrida produzca la misma identidad de alerta y la deduplicación no requiera estado compartido entre
> componentes. La alerta conserva además evidencia auditable: sujeto observado, detecciones de soporte, clase
> de protección ausente, región evaluada, puntaje y justificación legible. Por eso la ausencia no se presenta
> como una afirmación opaca del detector, sino como una inferencia del plano de control reconstruible sobre
> evidencia positiva."*

⚠ **Respeta E4-24 y D-P2-6:** ningún identificador literal aparece en esta prosa; los cinco quedan declarados
en la Tabla 63, que es su único punto de declaración. La referencia a la figura de la máquina de estados se
mantiene descriptiva, como pide la enmienda a E3-28.

*Origen: C0 de §17.4 ("difícil de leer, hay que mejorar la organización del desarrollo de esta sección").*

---

### E4-29 · §17.4.7 — el árbol de artefactos no muestra la plataforma completa

**Problema.** El árbol de la ejecución experimental lista `manifest.effective.yaml`, `media/`, `control/` y
`report/`, y deja la distribución fuera, en una oración suelta al pie: *"Cuando el tramo de distribución está
habilitado, su ledger y su reporte se consolidan del mismo modo."* Pero **esta es justamente la sección donde
se muestra cómo se consolida la evidencia de una corrida**: dejar un componente fuera del árbol sugiere que
se consolida distinto, cuando el argumento es el contrario. La condicionalidad es correcta —la plataforma es
modular y un tramo puede no estar habilitado—, pero ya hay una forma en el propio árbol de expresarla: dentro
de `control/` la evaluación temporal aparece con su condición entre paréntesis.

Defecto asociado, misma sección: la fila *Distribución* de la **Tabla 66** es la única de las cuatro que **no
nombra archivos** (*"Ledger de intentos y entregas; resultados de canal; reporte de distribución"*), mientras
las otras tres los nombran uno por uno. Verificado contra el módulo: los artefactos reales son
`notifications.jsonl` —el ledger de sólo agregado—, `distribution_summary.json` y `dead_letter.jsonl`, este
último el registro de los descartes definitivos por agotamiento de reintentos. **No** produce
`effective_config.yaml` por corrida: expone su configuración efectiva por interfaz, y esa asimetría con los
dos planos no debe insinuarse resuelta.

**Acción — tres ediciones.**

1. **Incorporar la distribución al árbol**, con su condición entre paréntesis, igual que la evaluación temporal:

   ```
   runs/<experiment_id>/                (repositorio del soporte experimental)
     manifest.effective.yaml
     media/           summary.json · metrics.jsonl · effective_config.yaml ·
                      detections.ref.json  (referencia al detections.jsonl del plano de medios)
     control/         alerts.jsonl · pattern_events.jsonl · metrics.jsonl ·
                      summary.json · effective_config.yaml
                      (y la evaluación temporal, cuando la corrida la habilita)
     distribution/    notifications.jsonl · distribution_summary.json · dead_letter.jsonl
                      (cuando la corrida habilita el tramo de distribución)
     report/          report.json · report.md
   ```

2. **Reemplazar la oración suelta** por una que cierre el argumento en lugar de excusarlo:

   > *"La ejecución experimental consolida así los cuatro componentes bajo una misma clave. La modularidad de
   > la plataforma se expresa en que un tramo pueda no estar habilitado, no en que su evidencia se consolide
   > de otro modo cuando lo está."*

3. **Tabla 66, fila *Distribución* — nombrar los artefactos** como en las otras tres filas:

   > *"notifications.jsonl (ledger de intentos y entregas, de sólo agregado); dead_letter.jsonl;
   > distribution_summary.json"* || *"Relaciona cada intento y resultado de entrega con la alerta interna
   > original sin reescribirla, y conserva por separado los descartes definitivos por agotamiento de
   > reintentos."*

*Origen: C2 de §17.4 ("agregar el módulo de distribución… la idea es mostrar la plataforma como un todo, y
más en esta parte que se habla de la consolidación de la evidencia de las corridas").*

---

### E4-30 · `PUB/SUB` en §17.4 — alinear con la normalización de E3-33 (✎ agregada el mismo día)

**Problema — desalineado entre secciones detectado en la verificación cruzada (§I).** E3-33 (b) alinea
§17.3 a la forma que el propio informe ya normalizó: **publicador-suscriptor** (§17.3.5, §17.3.18). Pero
§17.4 usa `PUB/SUB` crudo **cuatro veces**, y ninguna unidad lo tocaba. Aplicar E3-33 sin esto dejaría a
las dos secciones en formas distintas del mismo término — exactamente el defecto que D-P3-5 (b) corrige.

**Acción — tres ediciones (la cuarta aparición desaparece sola con E4-20, que elimina la Tabla 65):**

1. **Nota de la figura de §17.4.1** (*"…mediante buses ZeroMQ PUB/SUB con serialización msgpack…"*) →
   *"…mediante buses ZeroMQ de patrón publicador-suscriptor con serialización msgpack…"*.
2. **Tabla 64, fila del canal de detecciones:** celda de operación *"ZeroMQ PUB/SUB + msgpack"* →
   **"Bus ZeroMQ publicador-suscriptor (msgpack)"**.
3. **Tabla 64, fila del canal de alertas:** ídem.

**Verificación al aplicar:** `PUB/SUB` queda en **cero** apariciones en §17.4 (y en las dos que E3-33
conserva glosadas en §17.3 si las hubiera — el conteo final del par es el de E3-33).

---

## D. §17.5 — restricciones que este pase deja fijadas (no es corrección: §17.5 no está redactada)

Por D-P3-3 la etapa 5 entra en alcance. Como no hay texto que corregir, lo que se fija es el terreno, para
que §17.5 no repita §17.3/§17.4 ni contradiga lo que este pase acaba de resolver.

### D.0 — La organización de la sección (aplica D-P3-6; ✎ decisión del usuario, 2026-08-22)

**La sección se organiza por pregunta de medición, no por cronología.** El modelo estructural es el de la
síntesis de resultados vigente (pregunta → niveles de medición → tiempo real → caminos → limitaciones), que
ya demostró sostener el argumento sin narrar campañas. Esquema de referencia — los títulos definitivos los
fija la redacción, la **secuencia y el reparto** son lo decidido:

1. **Encuadre y reglas de lectura.** La pregunta de la sección, los **tres niveles de medición** (percepción
   por imagen · estado por sujeto · alerta por episodio), los estados de aplicabilidad, y de dónde sale cada
   cifra. Acá viven las reglas transversales: reportar por estrato además del agregado, no sumar percentiles
   entre tramos, re-alertas no son falsos positivos.
2. **Percepción sobre imágenes.** El banco de imágenes congelado: resultados **por modelo y por familia**,
   por estrato, con veredictos **por combinación** (rige E4-26: prohibida la fórmula "el mejor modelo"; la
   selección del perfil operativo se enuncia como criterio pre-registrado). Cierra con el costo medido de
   incorporar vocabulario nuevo (el piloto de clase nueva).
3. **Estado por sujeto (nivel intermedio).** La comparación de estrategias de detección sobre el estado
   "sin protección" por persona: la indirecta adoptada, la directa y la híbrida como ramas comparativas —
   los resultados que fundamentan el veredicto van acá, no en la narración de campañas.
4. **Alerta por episodio contra la referencia temporal humana — el resultado principal.** El banco temporal
   completo (47 clips: 32 positivos + 15 negativos), por estrato y por condición; la granularidad por
   sujeto como capacidad medida; la tasa de falsos positivos por hora (se reporta, no sostiene cota); la
   frontera de juzgabilidad del material de obra real (sin ranking sobre n = 2).
5. **Tiempo real.** Qué sobrevive a la restricción del camino en vivo: el costo de la densidad de
   procesamiento, la cadena de latencias **por tramos** (con la regla de relojes), y la latencia del tramo
   de distribución con su denominador.
6. **Caminos probados y no adoptados — con el veredicto que los descartó.** Una subsección propia, no notas
   dispersas: la estrategia directa (vetada por precisión), la híbrida (una variante ejecutada y refutada,
   una no ejecutable), la familia de modelos descartada en la comparación, y la **rama de ajuste fino como
   curva de capacidad de tres puntos** (dos veredictos negativos pre-registrados + un tramo cerrado con
   causa técnica; rige el punto 4 de abajo). El criterio de cada descarte precede al resultado que lo aplicó.
7. **Lo no ejecutado y lo no implementado — con su factor de justificación.** También subsección propia:
   condiciones de Nivel 2/3 (evaluabilidad: sin verdad de terreno ni evaluadores validables), métricas MOT
   (sin anotación de identidad), preselección en el borde (implementada y medida, excluida de lo evaluativo
   por decisión pre-registrada — rige la enmienda a E4-22), cota operativa de FAR (exposición insuficiente),
   y el ancla temporal para comparar EBE-desde-clip. Cada ítem con su justificación, nunca como lista de
   faltantes.
8. **Síntesis de la sección.** Qué queda afirmado con qué fuerza, y la remisión a las limitaciones
   declaradas. La **interpretación** (qué significa para la pregunta de la tesis) no vive acá: pertenece a
   las conclusiones.

**Reparto con las secciones vecinas, para no volver a pisarse:** §17.4 acredita que las capacidades
funcionan (verificación técnica); §17.5 reporta **cuánto dan** (medición); §18 dice **qué significa**
(interpretación y conclusiones). Un contenido que acredite funcionamiento no se repite en §17.5; un juicio
de valor no se adelanta desde §18.

### Restricciones puntuales

1. **Lo que §17.5 no vuelve a explicar.** La arquitectura, los contratos, los patrones de acople, los
   artefactos por corrida y el criterio de aplicabilidad de métricas ya están en §17.3 y §17.4. §17.5 los
   **usa**; no los reintroduce. Si un resultado necesita una condición de medición, se enuncia en una oración
   y se remite a la sección que la fijó.
2. **Herencia de E4-26 — no hay "mejor modelo".** Los resultados se presentan por modelo y por familia; la
   selección se enuncia como criterio operativo con base pre-registrada, y el veredicto es **por combinación**
   (un perfil puede ganar en precisión y otro en exhaustividad de una condición). Está prohibida la fórmula
   "el mejor modelo".
3. **Herencia de la enmienda a E4-22 — el 87 % de la preselección.** Si §17.5 lo cita, va con su denominador
   y su condición de medición, y aclarando que la capacidad estuvo deshabilitada en todo lo evaluativo. Si no
   lo cita, la celda de la Tabla 68 es su único lugar en el informe.
4. **Herencia de E4-27 — la rama de ajuste fino cierra en §17.5.** Los tres tramos y su lectura de conjunto
   (el límite es estructural, no de capacidad) se informan acá, con los márgenes firmados de antemano. Ningún
   pasaje del informe puede seguir describiendo el tramo adicional como pendiente.
5. **Las tres piezas de "listo para pegar" con contenido vencido** que ya identificó la revisión de cierre
   —la fila de ajuste fino que dice que resta la corrida (resuelta acá por **E4-27**), el identificador de un
   clip retirado del banco, y el redline de alcance sin anclar a su unidad— **se revisan antes de pegar
   §17.5**, no después.
6. **Criterio de tablas heredado.** Rige D-P2-1 y el resultado de la revisión de cierre para §17.5: siete
   tablas, seis a prosa, tres al Anexo D, una eliminada; y la tabla principal baja de trece a ocho columnas.
   Con los tres pases aplicados, **§17.5 arranca en la Tabla 61** (ver §G).
7. **Autocontención.** Igual que en §17.3 y §17.4: sin referencias a documentos del repositorio, decisiones
   internas, fichas ni índices. Las referencias a otras secciones del informe sí valen.

---

## E. Hechos verificados en este pase — NO "corregir" estos valores

| Hecho | Valor verificado | Cómo se re-verifica |
| --- | --- | --- |
| Peso de las dos secciones | §17.3 = **20.622** palabras · §17.4 = **5.477** (cuerpo extraído, sin el banner de la extracción) | `herramientas/extraer_informe.py` sobre cada `.docx`, después `wc -w` descartando el bloque anterior al primer `---` |
| Comentarios traídos | **40** en **29 hilos**: 37 en §17.3, 3 en §17.4 | `word/comments.xml` + `word/commentsExtended.xml` (hilos por `paraIdParent`) |
| CPN/EN/TN definidos en etapa 2 | §17.1.4.2 y sus tres sub-apartados | búsqueda de `CPN` en `entregable/96b-…-17-1-…md` |
| `E-DIR`/`E-IND`/`E-HYB` en secciones cerradas | **cero apariciones** | búsqueda sobre el XML de `entregable/E-OVRT-VDP_v1.1_05062026-sin-etapa3.docx` |
| Siglas de métricas definidas en etapa 2 | `t_alert-system` §17.1.7.5.1 (como ecuación OMML) · `TTFD` §17.1.7.5.2 · `SDR` §17.1.7.5.3 | ídem; la sigla de latencia **no** aparece en extracciones planas |
| Preselección en el borde: implementada | sólo para la cámara propia; deshabilitada por defecto; degradación segura con latido y apertura ante silencio | esquema de configuración del plano de medios (`config/schemas.py`) y la fuente del dispositivo |
| Preselección: efecto medido | **87 %** de unidades descartadas en el dispositivo, comparación pareada contra el flujo completo | registro de relevamiento de plataforma |
| Preselección: apagada en lo evaluativo | decisión previa a los resultados, con dos causas declaradas | registro de decisiones del banco en tiempo real |
| Ajuste fino: escalera completa | dos tramos entrenados y evaluados (ambos negativos) + tercero cerrado con causa técnica | cierres de jornada de los tres tramos |
| Artefactos del módulo de distribución | `notifications.jsonl`, `distribution_summary.json`, `dead_letter.jsonl`; **no** escribe `effective_config.yaml` por corrida | `out_dir / "…"` en `eovrt_distribution` |
| Valores del núcleo referenciados desde §17.3 | §17.4.6 **sí** los documenta (4.000/7.000 ms, 0,35, 400 px², 0,25, regiones 0–45 % y 25–85 %) | §17.4.6, primer párrafo |

---

## F. Mapa comentario → unidad — los 29 hilos, ninguno sin destino

**§17.3 (26 hilos)**

| Hilo | Sección | Destino |
| --- | --- | --- |
| C0 (+C1, C2, C3, C4) | 17.3.2 | **enmienda a E3-22** (§A) |
| C5 | 17.3.2 | **E3-33** (a) |
| C6 | 17.3.2 | **E3-33** (a) |
| C7 | 17.3.2 | **E3-34** |
| C8 (+C9) | 17.3.3.2 | **E3-21** (pase 2) fusiona las Tablas 40 y 41 — resuelve la duplicación medible. Lo que Gabriel además insinúa (que §17.3.3.1 y §17.3.3.2 comparten terreno en prosa) queda **diferido a la etapa 2** por decisión tuya en el hilo ("cuando se termine ahí vemos cómo enganchamos"). Ver §H. |
| C10 | 17.3.5 | **checkpoint de cierre, no unidad.** Dos de las siete figuras están producidas (la vista de procesos de §17.4.1 y la máquina de estados de §17.3.8.2, PNG 300 dpi y SVG, ancho 16 cm). Las cinco restantes de §17.3 son las tuyas y entran en el pase final de figuras. Ver §H. |
| C11 | 17.3.6.4 | **E3-42** |
| C12 (+C13, C14) | 17.3.6.6 | **E3-20** (pase 2) — sin cambios; es tu propio texto |
| C15 | 17.3.6.7 | **E3-35** |
| C16 (+C17) | 17.3.7.3 | **E3-28 + enmienda** (pase 2) — sin cambios |
| C18 | 17.3.7.4 | **E3-36** |
| C19 | 17.3.7.4 | **E3-36** |
| C20 | 17.3.7.5 | **enmienda a E4-22** (§A) |
| C21 | 17.3.7.5 | **E3-37** |
| C22 | 17.3.7.5 | **E3-37** |
| C23 | 17.3.8.2 | **verificado, sin cambio.** §17.4.6 sí documenta los valores del núcleo. La sección se retitula por E4-26 (*"…y catálogo de modelos"*) pero **no cambia de número**, así que la remisión sigue siendo válida. |
| C24 | 17.3.8.3.1 | **E3-38** |
| C25 | 17.3.8.3.1 | ídem C23 — verificado, sin cambio |
| C26 | 17.3.8.3.4 | **E3-39** |
| C27 | 17.3.9.1 | **E3-40** (1) |
| C28 (+C29) | 17.3.9.2 | **E3-40** (2) — decisión tomada: se conserva podada |
| C30 | 17.3.9.3 | **E3-40** (3) |
| C31 | 17.3.9.3 | **E3-40** (3) |
| C32 | 17.3.10.1 | **E3-41** |
| C33 (+C34) | 17.3.11.1 | **E3-30** (pase 2) — sin cambios; es tu propio texto |
| C35 (+C36) | 17.3.15 | **E3-34** (2) |

**§17.4 (3 hilos)**

| Hilo | Sección | Destino |
| --- | --- | --- |
| C0 | 17.4.3 | **E4-28** |
| C1 | 17.4.4 | **E4-25** (pase 2) — cubierto entero: propósito por endpoint, la asimetría de detención declarada y el orden de disparo derivado |
| C2 | 17.4.7 | **E4-29** |

**Sin comentario asociado, hallazgos de este pase:** **E4-27** (la fila de ajuste fino afirma algo falso),
**E3-33 (b) y (c)** (los anglicismos inconsistentes más allá de los dos marcados), y los dos defectos del kit
anotados en la cabecera.

---

## G. Numeración resultante, con los tres pases aplicados

**Subsecciones de §17.3**

| Cambio | Unidad | Efecto |
| --- | --- | --- |
| §17.3.6.6 eliminada | E3-20 (pase 2) | 6.7 → 6.6 |
| §17.3.6.6 (ex 6.7) eliminada | **E3-35** | §17.3.6 queda con **6.1 a 6.5** |
| §17.3.7.4 eliminada | **E3-36** | 7.5 → **7.4**; §17.3.7 queda con **7.1 a 7.4** |
| §17.3.9.3 retitulada | **E3-40** (3) | mismo número, nuevo título *"Comparabilidad entre estrategias"* |
| §17.3.11.1 eliminada | E3-30 (pase 2) | 11.2 → 11.1, 11.3 → 11.2, 11.4 → 11.3 |
| §17.3.14.2 retitulada | **E3-33** (a) | *"EBE como escenario de fuente en vivo controlada"* |

⚠ **Dependencia cruzada a respetar al aplicar:** la acción 3 de la enmienda a E3-28 apunta a "§17.3.7.5"; tras
E3-36 esa subsección es **§17.3.7.4**. Es la misma unidad (*"Capacidades opcionales sin desplazar el núcleo
validable"*) y sigue siendo donde nace `fail-open`.

**Tablas.** Este pase elimina **una** tabla más que el pase 2: la **Tabla 39**, que E3-22 ya sacaba —la
enmienda no cambia el conteo, sólo qué la reemplaza—. Las Tablas 64, 66, 68 y 69 reciben ediciones de celda o
de fila, no cambian de posición. ✎ **Mapa computado (2026-08-23; segunda corrección el mismo día — al aplicarse E3-27 la
Tabla 46 pasó a viñetas, así que §17.3 pierde SIETE tablas, no seis):** §17.3 pierde 39, 40, 46, 49, 51,
61 y 62, y queda con **17 = Tablas 39–55** (41→39, 42→40, 43→41, 44→42, 45→43, 47→44, 48→45, 50→46,
52→47, 53→48, 54→49, 55→50, 56→51, 57→52, 58→53, 59→54, 60→55); §17.4 pierde la 65 y queda con **6 =
Tablas 56–61** (63→56, 64→57, 66→58, 67→59, 68→60, 69→61); **§17.5 arranca en la Tabla 62**. ⚠ El mapa
vale si las opcionales C-01 a C-04 del pase 2 **no** se aplican (siguen sin decidirse); si alguna se
aplica, se recorre desde su posición.

---

## H. Verificación cruzada de alineación entre §17.3 y §17.4 (✎ 2026-08-22, directiva del usuario)

Cada tema que cruza la frontera diseño → implementación, con la unidad que lo fija de cada lado y el estado
verificado. **Esta tabla es la prueba de que las correcciones de ambas etapas no se contradicen**; si una
unidad futura toca uno de estos temas, tiene que actualizar la fila.

| Tema compartido | Lado §17.3 | Lado §17.4 | Verificado |
| --- | --- | --- | --- |
| Identificadores versionados (`.vN`, literales) | E3-31 (cero en §17.3) bajo D-P2-5 | E4-23 + E4-24 (Tabla 63 único punto de declaración; 1 glosa) bajo D-P2-6 | ✅ contrapartes explícitas; la fila *Cierre de corrida* de E4-24 recibe lo que E3-31 suelta |
| `fail-open` / `opt-in` | E3-28 + enmienda: nace y se glosa en "Capacidades opcionales…" (§17.3.7.4 tras E3-36); `opt-in` erradicado | Enmienda a E4-22: la fila de la Tabla 68 dice **"criterio de degradación segura"** — usa el término ya definido, no lo redefine | ✅ definición precede a todo uso |
| Preselección en el borde | Huella declarativa: DA-11, §17.3.7.4, §17.3.14.5, Tablas 57/58/59 | Enmienda a E4-22: implementada y medida (87 %), excluida de lo evaluativo con causa pre-registrada | ✅ el diseño la declara, la implementación rinde cuentas |
| Rama de ajuste fino | DA-07 y fila "Adaptación al dominio" (E3-21): condiciones de la rama (línea base congelada, partición disjunta, criterios previos) | E4-27: jornada completa, tres tramos cerrados, sin marcador | ✅ las condiciones del diseño son exactamente las que la jornada cumplió (pre-registración) |
| Duplicación DA-03 ↔ patrones de acople | E3-19 (la celda de DA-03 deja de enumerar tecnologías) | E4-20 (Tabla 65 eliminada: era el duplicado) | ✅ el par se resolvió de los dos lados |
| Anglicismos ya normalizados | E3-33 (a)(b)(c) — con lista cerrada de lo que NO se toca | **E4-30** — las 3 apariciones sobrevivientes de `PUB/SUB` | ✅ misma forma en ambas secciones |
| Códigos E-DIR / E-IND / E-HYB | E3-42: nacen glosados en §17.3.6.4 | §17.4.10 (Tabla 68) los usa después de esa definición | ✅ orden definición → uso verificado; §17.5 los hereda (D.0) |
| Valores efectivos del núcleo | §17.3.8.2 y Tabla 46 remiten a §17.4.6 (verificado en C23/C25) | E4-26 retitula §17.4.6 **sin cambiar su número** | ✅ la remisión sigue válida |
| Máquina de estados (FIG-E) | Vive en §17.3.8.2 (D2, excepción declarada) | §17.4.3 la referencia sin repetirla (texto guía de E4-28 mantiene la referencia descriptiva) | ✅ una sola figura, un solo dueño |
| Consolidación de evidencia por corrida | §17.3.10.2 / Tabla 48 (consumidores) y §17.3.12.1 (repositorio por `experiment_id`) | E4-29: `distribution/` entra al árbol con su condición entre paréntesis | ✅ el árbol muestra los cuatro componentes que el diseño promete |
| Cierre de corrida (`run_finished`) | §17.3.8.4 lo enuncia en abstracto (E3-31 suelta el literal) | Tabla 63, fila nueva de E4-24, lo declara | ✅ sin huérfanos |

---

## I. Diferidos y dependencias inversas

| Ítem | Por qué se difiere | Cuándo se retoma |
| --- | --- | --- |
| **C-1 del pase 1** — bautizar E-DIR/E-IND/E-HYB en §17.1.5.4.2 | Es edición de etapa 2, y **E3-42** ya dejó §17.3 autosuficiente | Al trabajar etapa 2. **Dependencia inversa:** si se aplica, hay que recortar la glosa de §17.3.6.4 a una remisión, o el informe la dirá dos veces |
| **Solape §17.3.3.1 ↔ §17.3.3.2 en prosa** (hilo C8/C9) | Depende de qué quede en §17.1 tras la etapa 2 | Al cerrar etapa 2, con E3-21 ya aplicada |
| **Pase de figuras** (C10) | Las cinco figuras de §17.3 son originales del autor | Pase final de figuras, junto con la inserción de las dos producidas |
| **`[[PENDIENTE]]` de §17.4.8.1** — origen y fecha de acceso por clip del lote de obra real | Insumo del usuario, sigue abierto | **Bloqueante para la versión final**; no se relaja |
| **Unidades opcionales C-01 a C-04 del pase 2** | Decisión no tomada | Antes de fijar la numeración final de tablas (§G) |
| **Anomalía observada en §17.1.7.5.1** (fuera de alcance) | La sigla de la latencia de alerta viaja como ecuación de Word y desaparece en toda extracción plana: los títulos quedan como *"Latencia de Alerta ()"* | Al trabajar etapa 2, verificar que la sigla se lea bien en el `.docx` final y no sólo en pantalla |
