# Correcciones — pase 2 sobre §17.3 (Diseño Arquitectónico) y §17.4 (Implementación)

**Fecha:** 2026-08-20 · **Insumos:** `E-OVRT-VDP_Seccion_17.3_Diseno_Arquitectonico_v1.1.docx` y
`E-OVRT-VDP_Seccion_17.4_Implementacion_v1.2.docx` (las versiones vigentes, ya con el pase 1 aplicado).
**Verificación:** todos los conteos, duplicaciones y citas de este documento fueron contrastados contra
esos dos `.docx` el 2026-08-20 (ver §D, con el procedimiento para re-verificarlos).

**Relación con el pase 1** (`archivado/correcciones-etapa-3-4.md`, ítems E3-01…E3-18 y E4-01…E4-19):
este pase **continúa la numeración** y **no re-abre** ninguna de sus decisiones. Las decisiones firmadas
del pase 1 (D1 término único, D2 doctrina 17.3-conceptual / 17.4-concreto, D3 códigos de estrategia,
D4 justificación del núcleo-solo, regla de autocontención) **siguen rigiendo**. Dos unidades de este pase
son consecuencia directa de aplicar el criterio del pase 1 donde había quedado sin aplicar (E3-19 y E4-21).

**Numeración de tablas usada acá:** la **vigente en los `.docx`** (§17.3 = Tablas 39–62; §17.4 = Tablas
63–69), es decir la que ya resulta de §E del pase 1. Aplicar este pase la vuelve a mover: el mapa nuevo
está en §E.

> ⚠ **Nota operativa (no es contenido del informe).** El generador del project-kit
> (`herramientas/generar_project_kit.py`, líneas 135 y 153) sigue apuntando a
> `informe/entregable/desarrollando/correcciones-etapa-3-4.md`, que el 2026-08-20 pasó a `archivado/`.
> Hoy `--check --etapa all` falla. Al decidir si este archivo entra al kit, corregir esas dos rutas.

---

## Decisiones que rigen este pase

- **D-P2-1 — Criterio de tabla.** Una tabla se justifica cuando **se consulta, no se lee**: filas
  estrictamente paralelas sobre los mismos atributos, celdas cortas, y el valor está en comparar *entre*
  filas. Corolarios que se aplican de forma mecánica en §A y §B:
  1. **Dos columnas = una lista con bordes.** No es una tabla.
  2. **Dos filas = una oración.**
  3. **Una columna cuyas celdas dicen todas lo mismo = una columna que sobra.**
  4. **Celdas de más de ~120 caracteres = prosa maquetada en grilla.**
- **D-P2-2 — Nada de lo que se elimina se pierde.** Ninguna unidad de este pase elimina un compromiso de
  diseño: cada tabla que sale se reemplaza por texto que en tres casos **ya existe** en el párrafo
  introductorio o en la Nota contigua.
- **D-P2-3 — El momento es ahora.** §17.5 y §17.6 todavía no están redactadas y numerarían desde la
  Tabla 70. Podar después obliga a renumerar dos veces y a corregir referencias ya escritas. Aplicado este
  pase, §17.5 arranca en la Tabla **63**.
- **D-P2-4 — Alcance declarado.** Este pase cubre §17.3 y §17.4. Las secciones cerradas se relevaron y su
  resultado se informa en §F, pero **no se tocan acá**.
- **Heredadas del pase 1:** regla de autocontención (el informe no referencia documentos locales, ADRs,
  fichas ni índices del repositorio — todos los textos guía de este archivo ya la cumplen) y carácter
  orientativo de los "textos guía" (pueden reformularse conservando contenido y registro académico;
  decimales con coma, milisegundos como "4.000 ms").

---

## A. Correcciones a §17.3 — Diseño Arquitectónico

### E3-19 · §17.3.3.4, Tabla 43, fila DA-03 — la columna "Justificación" no justifica

**Problema (tres capas, la primera es dura):**

1. **Contradice al párrafo que introduce la tabla**, dos renglones antes: *"Estas decisiones **no fijan
   tecnologías concretas**, pero establecen reglas estructurales…"*. DA-03 fija tres (HTTP config-driven,
   ZeroMQ PUB/SUB con msgpack, JSONL). Misma página.
2. **La celda enumera en lugar de justificar.** Las otras doce filas dan una razón (DA-01: *"Protege la
   ruta crítica…"*; DA-05: *"Permite comparar modelos sin rediseñar…"*). DA-03 responde "¿con qué?", no
   "¿por qué?". El porqué existe y está escrito: es §17.3.5 (*"Se adopta HTTP porque… Se adopta ZeroMQ
   porque… msgpack reduce…"*). La tabla se quedó con el "qué" y la prosa con el "porqué", invertido.
3. **Congela como invariante lo que el propio informe declara sustituible.** La tabla se presenta como
   *"reglas estructurales que deberán preservarse"*; §17.3.9.1 dice la doctrina correcta: *"conserva el
   transporte como mecanismo sustituible, pero fija para el prototipo una publicación ZeroMQ…"*. Si el bus
   fuera otro, DA-03 quedaría "incumplida" aunque la regla de diseño se preserve intacta.

Además es la única de trece filas con anglicismo crudo ("HTTP config-driven", "PUB/SUB") cuando el cuerpo
ya normalizó a *"interfaces HTTP gobernadas por configuración"* y *"publicador-suscriptor"*, y duplica casi
textualmente la Tabla 65 de §17.4 (que E4-20 elimina).

**Acción — reescribir sólo la celda de Justificación.** La Decisión no cambia.

> **DA-03 · Decisión:** Separar gobierno de corrida, transporte de datos en ejecución y repositorio
> persistente de hechos.
> **Justificación:** Cada preocupación tiene un régimen propio: el gobierno es puntual y de
> solicitud–respuesta, el transporte es continuo y no debe bloquear la ruta crítica, y la persistencia debe
> sobrevivir a la corrida para habilitar su relectura. Mantenerlas separadas permite sustituir el mecanismo
> de transporte sin alterar el gobierno ni la evidencia, y reevaluar cualquier corrida sin depender de la
> mensajería.

**Verificado:** DA-03 no está referenciada en ningún punto de §17.4 (la única fila del pase citada allí es
DA-13, en §17.4.6), así que el cambio no deja referencias colgadas. Las tecnologías siguen nombradas —con
su fundamento— en §17.3.5 y §17.3.9.1, que es donde D2 las admite.

---

### E3-20 · §17.3.6.6 "Validaciones previas al inicio de la corrida" — eliminar la subsección y reubicar

**Problema.** La subsección promete un mecanismo (un control de admisión) y entrega una lista de buenas
intenciones: ocho "debe/debería" en tres párrafos y sólo uno con consecuente. Nunca dice **quién** valida,
**en qué momento** ni **qué pasa cuando falla**. Párrafo por párrafo:

- **¶1** — el inventario *"fuente visual, modelo OVD, vocabulario activo, umbrales, política de registro"*
  ya está dos veces: es la **Tabla 44** completa y es §17.3.6.1 (*"**Antes de iniciar la ejecución**,
  define qué se evaluará, con qué fuente, con qué modelo, con qué vocabulario activo…"*). La segunda
  oración (*"tampoco debería evaluarse una alerta si no existe al menos un patrón activo"*) es
  tautológica. **Salvable:** la idea de compuerta.
- **¶2** — es un eco débil y anticipado de **§17.3.13.3**, que lo dice con precisión (los cuatro estados
  `computed / applicable_not_computed / not_applicable / not_interpretable`, cada uno con causa, más los
  ejemplos). Además está mal ubicado: declarar aplicabilidad no es una validación previa al inicio, es una
  propiedad del reporte. **Se elimina sin reemplazo.**
- **¶3** — solapa DA-11, §17.3.7.5 y §17.3.12.3. **Lo propio** es el consecuente: que un módulo implícito
  corrompe la interpretación de latencia, cobertura, privacidad y aplicabilidad.

**Acción.**
1. **Eliminar §17.3.6.6 completa.** §17.3.6.7 pasa a ser §17.3.6.6.
2. **Rescate 1 — al final del párrafo del punto de gobierno de §17.3.6.1:**
   > *"Esa función de gobierno sólo se sostiene si la configuración se resuelve y se valida antes de
   > iniciar la ejecución: una corrida cuya declaración esté incompleta debe fallar al crearse y no
   > producir artefactos que luego resulten inatribuibles."*
3. **Rescate 2 — como cierre de §17.3.6.5 (reglas de comparabilidad):**
   > *"Por la misma razón, ningún módulo opcional —evidencia visual, identidad temporal, zonas,
   > preselección en el rol de captura o distribución externa— puede operar como comportamiento implícito:
   > su habilitación se declara en la configuración de la corrida, porque una activación silenciosa
   > alteraría la interpretación de latencia, cobertura temporal, privacidad y aplicabilidad de métricas,
   > es decir, la base misma de la comparación."*

**Verificado:** ninguna prosa de §17.3 ni de §17.4 referencia §17.3.6.6. El hecho no se pierde del informe:
la Tabla 67 de §17.4 ya acredita que *"los endpoints… operan sobre configuraciones validadas"*.
**Saldo:** −1 subsección, ~180 palabras, cero compromisos de diseño perdidos.

---

### E3-21 · §17.3.3.1 y §17.3.3.2, Tablas 40 y 41 — fusionar en una sola tabla

**Problema — es la duplicación más cara del capítulo.** Dos tablas en subsecciones contiguas, con la misma
forma de columnas (`capacidad | tratamiento | justificación`), que asignan valores de **la misma taxonomía
de cinco términos**, con ~8 filas repetidas entre 12 y 16 (DBE, EBE, prompts, Nivel 1, evidencia visual,
inspección, identidad/MOT, adaptación al dominio). La prueba está en las Notas, que son la misma frase
dos veces con distinta redacción:

> **T40:** *"…'complementario previsto' agrupa capacidades útiles pero no obligatorias; 'extensión
> condicionada' identifica capacidades previstas sujetas a disponibilidad de datos y módulos; y 'rama
> comparativa condicionada'…"*
> **T41:** *"…'complementario previsto' agrupa capacidades útiles para validación…; 'extensión
> condicionada' identifica capacidades previstas pero no obligatorias; y 'rama comparativa
> condicionada'…"*

El lector no puede distinguir "alcance" de "capacidades requeridas" porque, operativamente, son lo mismo.

**Acción.**
1. **Una sola tabla**, ubicada en §17.3.3.2, titulada **"Capacidades arquitectónicas y su tratamiento en el
   diseño"**, con las columnas de la Tabla 41 (`Capacidad requerida | Compromiso | Lectura de diseño`).
2. **Base:** las 16 filas de la Tabla 41, que son las más granulares y mejor ordenadas.
3. **Absorber de la Tabla 40** las dos filas que sólo ella tiene, con su texto actual:
   - **Video crudo continuo** — *Fuera del comportamiento ordinario* — *"La trazabilidad principal se apoya
     en eventos, metadatos, métricas y referencias controladas."* (es una declaración de frontera, no puede
     perderse)
   - **Condiciones de riesgo de Nivel 2 y Nivel 3** — *Extensión condicionada* — se mantiene como fila
     propia, separada de "Capacidades contextuales y relacionales": una es el catálogo de condiciones, la
     otra los mecanismos que las habilitarían.
4. **Conservar la redacción de la Tabla 40** en dos celdas donde es más precisa que la de la 41:
   - identidad temporal / métricas MOT: *"La arquitectura admite granularidad por sujeto mediante una
     identidad temporal válida. Las métricas MOT no condicionan la evaluación del núcleo ni deben
     confundirse con la capacidad de mantener identidad."*
   - adaptación al dominio: *"Sólo corresponde bajo una línea base preentrenada congelada, datos
     suficientes, partición disjunta y criterios de escalamiento definidos con anterioridad a los
     resultados."*
5. **Una sola Nota**, con la glosa de los cinco tratamientos (la de la Tabla 41, que es la más completa).
6. **§17.3.3.1 conserva su prosa** —define el alcance del núcleo y las extensiones— y pierde su tabla; la
   frase que la introduce (*"La Tabla 40 detalla…"*) pasa a remitir a la tabla única de §17.3.3.2.

**Resultado:** ~18 filas, una taxonomía, una glosa. **−1 tabla, −10 filas, −1 nota duplicada.**

---

### E3-22 · §17.3.2, Tabla 39 — pasar a viñetas

**Problema.** 6 filas × 3 columnas con celdas de 125 caracteres de mediana (máximo 299): es prosa
maquetada en grilla (D-P2-1.4). Y su columna del medio —"Criterio ya definido"— es un **resumen de §17.1**:
repetición de un capítulo anterior dentro de una tabla. Lo valioso es el vínculo insumo → decisión, que son
seis oraciones. Quitar sólo la columna del medio la dejaría en dos columnas, o sea en una lista (D-P2-1.1);
conviene hacer el paso completo.

**Acción — reemplazar la tabla y su Nota por el siguiente cierre de §17.3.2** (el párrafo que hoy la
introduce se conserva y encadena con esto):

> *"Cada decisión de diseño se vincula con un insumo metodológico ya consolidado:*
> - *del **marco teórico** de detección de vocabulario abierto, seguimiento y procesamiento de video se
>   deriva una arquitectura modular, con separación de planos, ruta crítica medible y modelos sustituibles
>   mediante adaptadores;*
> - *de las **condiciones de riesgo seleccionadas**, priorizar el flujo completo de equipo de protección
>   mediante la estrategia indirecta (E-IND) y mantener zonas, relaciones complejas y métricas de
>   seguimiento como capacidades no bloqueantes;*
> - *de los **escenarios de evaluación**, abstraer las fuentes visuales para que ambos ingresen al pipeline
>   mediante contratos comunes, distinguiendo reproducibilidad, frescura, omisión, descarte y trazabilidad
>   temporal según la naturaleza de la fuente;*
> - *de los **roles funcionales**, definirlos como roles de referencia que organizan el diseño y delimitan
>   responsabilidades sin fijar una distribución obligatoria en hardware, procesos o contenedores;*
> - *del **marco de métricas**, instrumentar marcas temporales, configuración de corrida, métricas por
>   tramo y eventos reconstruibles desde el inicio del diseño;*
> - *de los **lineamientos ético-legales**, priorizar eventos, metadatos y referencias controladas y
>   conservar evidencia visual sólo cuando esté justificada por validación, auditoría o comunicación
>   académica."*

Eliminar también la referencia en prosa *"La Tabla 39 sintetiza esta relación…"*.

---

### E3-23 · §17.3.11.2, Tabla 49 — subsumida por la Tabla 50

**Problema.** Su columna "Contrato principal" **es la columna 1 de la Tabla 50**, una página después; y
"Información que cruza" es la "Información mínima" de la Tabla 50 en grano grueso. Ejemplo textual:

> **T49:** *Salida del plano de medios | Detecciones normalizadas, modelo, prompts, coordenadas, puntajes y
> tiempos | media.detection.v1*
> **T50:** *PerceptionEvent | Publica evidencia perceptiva normalizada | media.detection.v1, run, unidad,
> fuente, modelo, prompts, detecciones y timing*

Lo único que la Tabla 49 aporta y la 50 no es la columna **"Decisión protegida"**, que es justamente lo
valioso: dice *por qué* existe cada frontera.

**Acción.**
1. **Eliminar la Tabla 49** y su Nota. La Tabla 50 queda como la única tabla de contratos del capítulo.
2. **Conservar las siete decisiones protegidas como prosa** en §17.3.11.2, encadenadas al párrafo que hoy
   introduce la tabla. **Texto guía:**
   > *"Cada frontera existe para proteger una decisión. La del gobierno del experimento evita una
   > configuración monolítica y vincula ciclos de vida independientes. La de entrada visual unifica los dos
   > escenarios sin ocultar su temporalidad. La de salida del plano de medios encapsula la heterogeneidad
   > del detector. La de entrada del plano de control obliga a evaluar reglas sobre eventos y no sobre
   > frames crudos. La de salida del plano de control diferencia detección, patrón y alerta. La de
   > distribución mantiene la comunicación y la idempotencia aguas abajo de la alerta interna. Y la de
   > referencia y soporte sostiene la medición y la reconstrucción con estados de aplicabilidad. Las
   > fronteras son lógicas: no prescriben que cada responsabilidad se despliegue en una máquina, proceso o
   > contenedor independiente."*
3. Eliminar la referencia *"La Tabla 49 resume las fronteras que el diseño protege…"*, cuyo contenido pasa
   al texto anterior.

---

### E3-24 · §17.3.11.4, Tabla 51 — pasar a párrafo

**Problema.** Tres de sus cinco filas dicen textualmente *"Extensión prevista; …"* en la columna "Estado de
diseño": densidad informativa nula (D-P2-1.3). Y el contenido es un roadmap de campos opcionales, no una
decisión de diseño. La única fila con carga real —identidad temporal— ya está en DA-06 y se desarrolla en
§17.4.11.

**Acción — reemplazar la tabla por un párrafo** en §17.3.11.4, antes de la Nota (que se conserva porque
enuncia la regla de versionado):

> *"La superficie de crecimiento del evento de percepción se mantiene acotada y separada de las reglas de
> riesgo. La identidad temporal de sujeto es un campo opcional y la única identidad válida entre frames: el
> contrato la admite y el plano de control puede materializarla por configuración, sin que el plano de
> medios necesite emitirla y sin mezclar esa capacidad con las métricas de seguimiento. Velocidad,
> dirección, puntos clave de pose y máscaras de segmentación quedan previstos como campos opcionales que no
> modifican la semántica mínima del evento ni desplazan al bounding box. Las relaciones entre sujeto,
> evidencia de soporte y clase ausente, en cambio, pertenecen al plano de control: el plano de medios
> publica detecciones individuales."*

Eliminar la referencia *"La Tabla 51 explicita la superficie de crecimiento…"*.

---

### E3-25 · §17.3.17, Tabla 61 — eliminar

**Problema.** Tres razones convergentes:
1. Es de dos columnas (D-P2-1.1).
2. Duplica las filas de tratamiento "complementario previsto" y "extensión condicionada" de las Tablas 40 y
   41 (que E3-21 fusiona), y la Tabla 69 de §17.4 la reemplaza con ventaja: agrega el costo técnico y está
   respaldada por implementación.
3. **El párrafo que le sigue ya la sustituye en prosa:** *"La frontera de extensibilidad distingue tres
   clases de cambio. Una condición nueva del tipo «sujeto sin EPP» requiere una definición declarativa de
   patrón y vocabulario… Una familia relacional, zonal o de trayectoria requiere un evaluador nuevo… Un
   modelo, una fuente o un canal nuevos requieren sus respectivos adaptadores…"*.

**Acción.** Eliminar la Tabla 61 y su encabezado. El párrafo siguiente queda solo y basta.

---

### E3-26 · §17.3.18, Tabla 62 — eliminar

**Problema.** Es una **tabla-resumen dentro de una sección-resumen**: sus diez filas recapitulan decisiones
ya tomadas y desarrolladas —"Responsabilidades separadas" = DA-01; "Persistencia y transporte diferenciados"
= DA-03; "Alerta interna protegida" = DA-13; "Trazabilidad y minimización" = DA-08/DA-09; "Plan de
materialización" = Tabla 60—. No agrega un solo compromiso nuevo, y además es de dos columnas.

**Acción.** Eliminar la tabla y su Nota. §17.3.18 conserva su prosa de cierre, que ya declara el paso a la
implementación sin anticipar resultados. Si se quiere conservar la función de checklist, alcanza con una
oración al cierre:

> *"El diseño se considera completo cuando cada una de estas decisiones —separación de responsabilidades,
> estrategia perceptiva, configuración reproducible, contratos versionados, persistencia y transporte
> diferenciados, temporalidad declarada, alerta interna protegida y extensibilidad delimitada— posee un
> criterio verificable en la implementación."*

---

### E3-27 · §17.3.8.3.1, Tabla 46 — podar la tercera columna

**Problema.** Después de E3-09 (pase 1), que le quitó los valores numéricos, la columna **"Función en el
motor" quedó circular** en cuatro de diez filas: *"Identificación del patrón → Identifica la regla y su
configuración"*; *"Severidad configurada → Asigna la prioridad conceptual de la condición"*; *"Evidencia
requerida → Define la evidencia utilizada"*; *"Región de evaluación → Delimita dónde se busca el EPP"*. La
columna repite el nombre de la fila con otras palabras.

**Acción.** Eliminar la columna "Función en el motor". La tabla queda como
`Componente | Contenido esperado` — que es una lista, así que la alternativa equivalente es pasarla a
viñetas con el componente en negrita. **Recomiendo las viñetas**, por coherencia con D-P2-1.1. La Nota se
conserva sin cambios (remite a §17.4.6 por los valores).

---

### E3-28 · Terminología `opt-in` / `fail-open` y el párrafo desubicado de §17.3.7.3

**Problema.** Ninguno de los dos términos viene de etapas anteriores: **cero apariciones** en el
frontmatter/objetivos/plan, en §17.1, en el estado del arte, en el marco teórico y en el cierre/anexos.
Ambos **nacen en §17.3**, y su primera aparición es **DA-11, dentro de una celda de la Tabla 43**, crudos y
sin glosa. Después:

- `fail-open` **se glosa dos veces**, ninguna en su primer uso, y con las mismas palabras:
  > §17.3.7.3: *"…con comportamiento fail-open: ante incertidumbre o falla, la unidad se conserva para el
  > flujo principal."*
  > §17.3.14.5: *"…es opcional, deshabilitada por defecto y fail-open: una falla o incertidumbre del
  > preselector no debe eliminar la unidad del flujo principal."*
- `opt-in` **no se define nunca**, y no hace falta: siempre viene pegado a *"deshabilitada por defecto"*,
  que es su definición. Peor: el propio informe usa "opcional" para lo mismo en §17.3.14.5 y en la Tabla 58,
  con lo cual alterna dos términos para un solo concepto sin criterio.
- El párrafo de §17.3.7.3 está **en la subsección equivocada**: los otros cuatro párrafos de "Control de
  ritmo según tipo de fuente" son todos ritmo (fuentes pulleables vs. vivas, atraso acumulado, descartes,
  FPS vs. cobertura); ése abre con *"Las capacidades opcionales del plano de medios…"*. §17.3.7.5 se titula
  literalmente **"Capacidades opcionales sin desplazar el núcleo validable"**.

**Acción — cinco ediciones puntuales.**

1. **Tabla 43, DA-11 — glosar acá (primer uso) y eliminar el anglicismo:**
   > **Decisión:** Permitir preselección liviana en el EN como variante **opcional**, conservadora y
   > deshabilitada por defecto, con comportamiento fail-open.
   > **Justificación:** El comportamiento fail-open conserva la unidad en el flujo principal ante falla o
   > incertidumbre del preselector, de modo que la variante puede reducir carga sin transformar el borde en
   > fuente de verdad ni ocultar descartes; el flujo base continúa disponible.

2. **§17.3.7.3 — eliminar el cuarto párrafo completo** (el que empieza *"Las capacidades opcionales del
   plano de medios se incorporan sin modificar su contrato de salida…"*). La subsección queda con cuatro
   párrafos, todos sobre ritmo, y cierra donde debe. De sus cuatro oraciones: la de preselección se va
   porque §17.3.14.5 la dice mejor; la de instrumentación también está allá; y la última (*"la identidad
   temporal, las asociaciones y el razonamiento contextual permanecen en el plano de control"*) ya está en
   §17.3.7.4 y en §17.3.7.5.

3. **§17.3.7.5 — rescatar la única oración que no está en otro lado.** Al final del primer párrafo:
   > *"Estas capacidades pueden incorporarse como variantes del flujo, pero no deben convertirse en
   > requisitos para demostrar el procesamiento básico de CR-01 y CR-02, **y su incorporación no modifica el
   > contrato de salida del plano de medios**."*

4. **§17.3.14.5 — quitar la glosa, que ahora es la segunda.** La subsección conserva el párrafo (ahí el rol
   EN *es* el tema: la preselección sólo existe en EBE), pero la segunda oración pasa a
   *"…una falla o incertidumbre del preselector no elimina la unidad del flujo principal"*, sin volver a
   definir el término.

5. **Las dos celdas que quedan con `opt-in`:**
   - Tabla 57, fila *Preselección en el borde*: *"Estado opt-in, criterio, fail-open y ledger de
     decisiones"* → **"Estado de habilitación, criterio, comportamiento fail-open y ledger de decisiones"**.
   - Tabla 59, fila *Preselección en borde descarta evidencia*: *"…como variante opt-in y fail-open, con
     ledger…"* → **"…como variante opcional y fail-open, con ledger…"**.

**Resultado:** `opt-in` desaparece del informe (4 de 4) y `fail-open` queda glosado una sola vez, en su
primera aparición. Ver **E4-22**, que cierra el otro extremo del mismo problema.

---

## B. Correcciones a §17.4 — Implementación

### E4-20 · §17.4.5, Tabla 65 — eliminar

**Problema.** **Dos filas.** Es el caso más claro del informe (D-P2-1.2): su propia Nota las resume
completas en una oración —*"HTTP gobierna configuración y ciclo de vida de los tres servicios; el bus
transporta los hechos de ejecución"*— y el párrafo que la introduce ya anuncia los dos patrones. Es, además,
la tercera formulación del mismo contenido: DA-03 (§17.3.3.4), el párrafo de materialización (§17.3.5) y
esta tabla.

**Acción.** Eliminar la tabla y su encabezado. El texto de la Nota se integra como cierre del párrafo que
hoy la introduce; **los puertos y los participantes ya están en la Tabla 64** (interfaces), que es donde
corresponde por D2. Actualizar la referencia en prosa si la hubiera.

---

### E4-21 · §17.4.9, Tabla 67 — eliminar la columna "Estado"

**Problema.** Las **siete filas dicen "Verificada"**. Es exactamente el defecto que E3-02 del pase 1 ya
eliminó de la Tabla 43 (*"Todas las filas dicen 'Adoptada': la columna no discrimina nada"*), que quedó sin
aplicar en §17.4.

**Acción.**
1. Eliminar la columna "Estado". El párrafo que introduce la tabla ya declara que todo lo listado es
   evidencia de verificación, y la Nota lo reafirma.
2. Sin esa columna la tabla queda en dos columnas, o sea en una lista (D-P2-1.1): **pasarla a viñetas** con
   la propiedad verificada en negrita y su evidencia a continuación. Se conservan íntegras las siete
   evidencias, incluida la de pruebas automatizadas (2.203 aprobadas, sin fallos, en cinco suites, más la
   suite propia del módulo de distribución).
3. Conservar la Nota tal cual (acota que la tabla acredita funcionamiento técnico y no desempeño).

---

### E4-22 · §17.4.10, Tabla 68 — fila nueva: la preselección en el borde no se ejerció

**Problema — es el agujero de rendición de cuentas del capítulo.** La preselección liviana en el rol de
captura aparece **once veces en §17.3** (§17.3.3.1, DA-11, Tabla 44, §17.3.6.6, §17.3.7.3, §17.3.7.5,
§17.3.14.5 y las Tablas 57, 58, 59 y 61: cuatro tablas distintas le dedican una fila). En **§17.4 aparece
cero veces**. Y **no está declarada como exclusión**: la Tabla 68 —que es el lugar del informe donde se
rinden cuentas de capacidades ejercidas, exclusiones y brechas— tiene seis filas (identidad de sujeto,
estrategias E-DIR/E-IND/E-HYB, distribución de alertas, rama comparativa de ajuste fino, condiciones de
Nivel 2 y 3, paridad DBE/EBE) y ninguna es el rol de captura. Mientras tanto §17.4.5 dice que *"los
servicios se ejecutaron co-ubicados en un único host con GPU"*, que implícitamente significa que ese rol
nunca se desplegó.

Un lector que cuenta once menciones de una capacidad en el diseño y no la encuentra en el balance de
implementación se queda con una pregunta que el informe no contesta.

**Acción — agregar una fila a la Tabla 68**, después de *Condiciones de riesgo de nivel 2 y 3*:

> **Preselección liviana en el rol de captura** || *Especificada en el diseño como variante opcional y
> deshabilitada por defecto; no ejercida. Las corridas se ejecutaron con los servicios co-ubicados en un
> único host, sin desplegar el rol de captura como unidad separada.* || *La capacidad no integra los
> resultados: su efecto sobre carga, cobertura temporal y latencia queda fuera de lo medido y no puede
> reclamarse como propiedad verificada del prototipo.*

**Complemento recomendado (no obligatorio):** bajar la huella en §17.3. E3-25 ya elimina una de las cuatro
tablas con fila de preselección (la 61); las unidades opcionales C-01 y C-03 se ocupan de otras dos. Con
DA-11 más el párrafo de §17.3.14.5 alcanza y sobra para dejar la decisión declarada.

---

## C. Unidades opcionales — la regla de las dos columnas

Estas cuatro unidades **no eliminan contenido**: cambian el formato de tablas que, por D-P2-1, son listas.
Aplicarlas baja el conteo sin perder una palabra; no aplicarlas no rompe nada. Van separadas porque son
decisión de estilo, no de contenido.

### C-01 (opc) · Tablas 52, 59 y 60 — pasar a viñetas
Las tres son de dos columnas. **52** (hechos persistibles mínimos, 12 filas) es la más defendible: se
consulta como checklist. **59** (riesgos y mitigaciones, 9 filas) es la más prescindible: tres de sus filas
—pérdida silenciosa en el bus, relojes incompatibles, fuente no temporal— ya están en §17.3.13.3 con más
precisión, incluidos los códigos de causa. **60** (plan de materialización, 10 filas) tiene contenido
propio y es el puente a §17.4. En los tres casos: viñeta con el término en negrita y su explicación a
continuación.

### C-02 (opc) · §17.3.15, Tabla 58 — pasar a items
Cuatro filas, y viene inmediatamente después de una figura que ya muestra los mismos roles. Cuatro párrafos
breves (uno por rol) leen igual o mejor.

### C-03 (opc) · §17.3.14.5, Tabla 57 — pasar a items
Es la expansión de **una celda** de la Tabla 56 (la fila "Instrumentación adicional", que ya enumera
captura, profundidad de cola, descartes, jitter, reemplazo de frames y estado de fuente) y se solapa con la
Tabla 55 en descartes, timestamps y errores. Si se aplica esta unidad, la edición 5 de E3-28 sobre la Tabla
57 se absorbe acá.

### C-04 (opc) · §17.3.13.1, Tabla 53 — revisar contra la Tabla 54
Es la más floja de las que este pase conserva: su tercera columna nombra las métricas que la Tabla 54 define
dos párrafos después con `Métrica | Inicio | Cierre | Unidad`. Y §17.3.13 queda con tres tablas seguidas
(53, 54, 55). La 54 es la mejor tabla del capítulo y no se toca; si hace falta una cuarta baja, es la 53.

---

## D. Hechos verificados (2026-08-20) — NO "corregir" estos valores

Todo lo que sigue se contrastó contra los dos `.docx` vigentes. Procedimiento para re-verificar: los `.docx`
son ZIP; `word/document.xml` contiene el cuerpo, con `w:p` para párrafos y `w:tbl` para tablas. Los conteos
se obtuvieron extrayendo el texto de cada bloque en orden de aparición.

**Sobre `opt-in` y `fail-open`:**
- Apariciones en §17.3: `opt-in` **4** (Tabla 43/DA-11, §17.3.7.3, Tabla 57, Tabla 59) · `fail-open` **7**
  (las cuatro anteriores más §17.3.14.5, Tabla 58 y Tabla 61).
- Apariciones en §17.4: **0** de ambos. Búsqueda ampliada a `preselec`, `borde`, `OAK` y `EN` como rol:
  **0 resultados**.
- Apariciones en las secciones previas del informe (frontmatter/intro/objetivos/plan; §17.1 consolidación
  metodológica; estado del arte; marco teórico; cierre/anexos/referencias): **0 y 0**. Ambos términos nacen
  en §17.3.
- `fail-open` se glosa **dos veces** (§17.3.7.3 y §17.3.14.5); `opt-in`, **ninguna**.
- La preselección en el borde aparece **11 veces** en §17.3, en cuatro tablas distintas.

**Sobre tablas y columnas:**
- Tabla 67 (§17.4): la columna "Estado" dice "Verificada" en **7 de 7** filas.
- Tabla 68 (§17.4): **6 filas**; ninguna corresponde al rol de captura ni a la preselección.
- Tabla 65 (§17.4): **2 filas**.
- Tabla 51 (§17.3): **3 de 5** filas de la columna "Estado de diseño" empiezan con "Extensión prevista".
- Tablas 40 y 41 (§17.3): comparten la taxonomía de cinco tratamientos y sus Notas son la misma glosa
  redactada dos veces.
- Tabla 49 vs. Tabla 50 (§17.3): la columna "Contrato principal" de la 49 es el conjunto de la columna 1 de
  la 50.
- Métricas de forma (filas × columnas, mediana de caracteres por celda) de las tablas citadas: T39 6×3 med
  125 (máx 299) · T47 6×4 med 126 · T66 4×3 med 101 · T56 6×4 med 80 · T54 8×4 med 30 · T63 16×4 med 20 ·
  T55 9×3 med 26 · T45 13×4 med 26.

**Sobre referencias cruzadas (verificado antes de proponer cada eliminación):**
- **DA-03** no está citada en §17.4; la única fila del pase de decisiones citada allí es **DA-13**
  (§17.4.6).
- **§17.3.6.6** no está referenciada en ninguna prosa de §17.3 ni de §17.4.
- Referencias en prosa a tablas que este pase elimina: *"La Tabla 39 sintetiza…"* (§17.3.2), *"La Tabla 49
  resume…"* (§17.3.11.2) y *"La Tabla 51 explicita…"* (§17.3.11.4). Las tres se resuelven dentro de su
  unidad.
- §17.4.5 afirma: *"En los experimentos del presente trabajo, los servicios se ejecutaron co-ubicados en un
  único host con GPU."*

---

## E. Renumeración resultante (consecuencia de aplicar §A y §B)

Aplicando las unidades **no opcionales**: §17.3 pasa de 24 a **18 tablas** (fusión 40+41; bajas 39, 49, 51,
61 y 62) y §17.4 de 7 a **6** (baja 65). La numeración definitiva la fija el maestro al integrar; el mapa
esperado es:

**§17.3 — de 24 a 18 tablas**

| Actual | Contenido | Nuevo |
|---|---|---|
| 40 + 41 | Capacidades arquitectónicas y su tratamiento (fusionadas, §17.3.3.2) | **39** |
| 42 | Requisitos no funcionales de referencia | **40** |
| 43 | Decisiones arquitectónicas iniciales | **41** |
| 44 | Elementos mínimos de la configuración experimental | **42** |
| 45 | Vocabulario inicial de prompts por condición | **43** |
| 46 | Componentes mínimos de una definición de patrón | **44** |
| 47 | Diseño del motor de patrones según condición | **45** |
| 48 | Consumidores y salidas del tramo de distribución | **46** |
| 50 | Contratos mínimos para la ejecución experimental | **47** |
| 52 | Hechos persistibles mínimos | **48** |
| 53 | Métricas y evidencias por tramo | **49** |
| 54 | Diccionario de métricas | **50** |
| 55 | Señales observables del sistema | **51** |
| 56 | Comparación DBE / EBE | **52** |
| 57 | Condiciones observables para interpretar EBE | **53** |
| 58 | Roles funcionales y unidades desplegables | **54** |
| 59 | Riesgos arquitectónicos y mitigaciones | **55** |
| 60 | Plan de materialización del núcleo | **56** |

Bajas: **39** (→ viñetas, E3-22), **49** (→ prosa, E3-23), **51** (→ párrafo, E3-24), **61** (E3-25) y
**62** (E3-26).

**§17.4 — de 7 a 6 tablas**

| Actual | Contenido | Nuevo |
|---|---|---|
| 63 | Correspondencia contratos del diseño ↔ materialización | **57** |
| 64 | Interfaces principales de los servicios | **58** |
| 66 | Artefactos persistidos por componente | **59** |
| 67 | Evidencia de verificación técnica | **60** |
| 68 | Capacidades ejercidas, exclusiones y brechas | **61** |
| 69 | Puntos de extensión y costo técnico | **62** |

Baja: **65** (E4-20).

**Referencias en prosa a actualizar** — §17.3: *"las decisiones enumeradas en la Tabla 43"* (§17.3.4) →
**41**; *"La Tabla 44 resume…"* (§17.3.6.2) → **42**; *"La Tabla 45 organiza…"* (§17.3.6.4) → **43**;
*"…se sintetizan en la Tabla 46"* (§17.3.8.2) → **44**; *"La Tabla 48 distingue…"* (§17.3.10.2) → **46**;
*"La Tabla 56 resume…"* (§17.3.14.4) → **52**. §17.4: *"La Tabla 63 establece…"* (§17.4.2) → **57**;
*"La Tabla 68 evita…"* (§17.4.10) → **61**.

**Consecuencia aguas abajo:** **§17.5 pasa a numerar desde la Tabla 63** (hoy arrancaría en la 70). Por eso
D-P2-3: conviene resolver este pase antes de redactar §17.5 y §17.6. Si además se aplican las unidades
opcionales de §C, el mapa se corre otro tanto y debe recalcularse al integrar.

**Figuras:** este pase no toca ninguna figura. El mapa de §E del pase 1 sigue vigente.

---

## F. Alcance sobre el resto del informe

Para que el criterio D-P2-1 no quede aplicado sólo donde se estaba trabajando, se relevó la forma de
**todas** las tablas del informe. Resultado:

**§17.3 es la anomalía del documento, no la norma.** Las secciones ya cerradas usan matrices densas —de 4 a
7 columnas con celdas de 7 a 47 caracteres de mediana (Tablas 23, 24, 26, 29, 33, 36)—, que es exactamente
el caso en que una tabla se justifica. §17.3, en cambio, usa 3 columnas con medianas de 30 a 126 caracteres:
grillas de prosa. Esa diferencia de forma explica por qué el capítulo se siente sobrecargado de tablas
aunque tenga menos que §17.1.

**Lo que el criterio marcaría fuera de §17.3/§17.4, si se aplicara de manera uniforme** (relevamiento de
forma, **sin** revisión de contenido — no se propone acción):

- **Celdas largas (prosa en grilla):** Tabla 13 (mediana **278** caracteres), Tabla 7 (**196**), Tabla 14
  (**190**), Tabla 12 (**116**), Tabla 5 y Tabla 15 (**122** cada una) — todas en estado del arte y marco
  teórico.
- **Dos columnas:** Tablas 19, 20 y 28 (§17.1), más varias tablas de anexo en el cierre. La Tabla 1 también
  es de dos columnas pero es un glosario de 61 entradas: ahí el formato es correcto.
- **Dos filas:** Tabla 30 (§17.1).

**Por qué no se propone tocarlas acá:** esas secciones están cerradas y su renumeración arrastraría todo el
informe — son **38 tablas numeradas** (Tablas 1 a 38) y **62 apariciones** de "Tabla N" entre rótulos y
referencias en prosa, que habría que recorrer una por una. Si se decide extender el criterio, corresponde un
pase propio y debe hacerse **antes** que este, no después, para renumerar una sola vez. Mi recomendación es
**no abrirlo**: el costo de renumeración supera la ganancia, y ninguna de esas tablas presenta el problema
que sí presenta §17.3 —duplicación entre tablas vecinas y columnas que no discriminan—.

**Lo que este pase sí verificó en todo el informe:** la trazabilidad terminológica de `opt-in` y
`fail-open` (§D), que era la pregunta de origen de E3-28.
