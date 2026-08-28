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

> ✅ **Nota operativa (no es contenido del informe) — RESUELTA.** El generador del project-kit apuntaba a la
> ruta vieja de `correcciones-etapa-3-4.md` (movida a `archivado/` el 2026-08-20) y `--check --etapa all`
> fallaba. Corregido: hoy el generador toma **ambos pases** —el 1 desde `archivado/` y el 2 desde acá— en
> las etapas 3 y 4, `--check --etapa all` da **OK** y los 36 tests del generador pasan
> (verificado 2026-08-22).

> ✎ **Estado al 2026-08-22.** Al pase original (E3-19…E3-28 · E4-20…E4-22 · C-01…C-04) se agregaron
> **E3-29, E3-30, E3-31, E4-23, E4-24, E4-25** y **E4-26**, las decisiones **D-P2-5** y **D-P2-6**, y una
> **enmienda a E3-28**. Ninguna toca el mapa de tablas de §E (E4-24 y E4-25 agregan **filas** a las Tablas
> 63 y 64, no tablas; E4-26 retitula §17.4.6); sí se agregó a §E el corrimiento de **subsecciones**, que
> faltaba.

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
- **D-P2-5 — Identificadores versionados de contratos (✎ 2026-08-22, extiende D2 sin reabrirla).** §17.3
  nombra los contratos por su **denominación conceptual** (la de la Tabla 50 y de la columna "Contrato del
  diseño" de la Tabla 63: evento de percepción / PerceptionEvent, alerta interna / AlertEvent, referencia
  temporal de evaluación, …). Los **identificadores de cable con sufijo de versión**
  (`media.detection.v1`, `clip_gt.v2`, `bus.envelope.v1`, …) y los literales de protocolo (`run_finished`)
  son **materialización efectiva** y pertenecen a §17.4, cuyo punto de declaración es la Tabla 63. §17.3
  conserva **el compromiso de versionado enunciado en abstracto** (la regla de evolución de §17.3.11.4 y
  "la versión viaja dentro del payload"). Excepción coherente, espejo de la de FIG-E en D2: los **nombres
  de estados** de la máquina de patrones (`inactive`…`resolved`) son vocabulario del diseño y se quedan en
  §17.3.8.2. Fundamento y aplicación: **E3-31** y **E4-23**.
  **Límite de la regla — NO sobre-aplicar.** D-P2-5 alcanza **sólo** al sufijo de versión del esquema y a
  los literales de protocolo. **Se quedan en §17.3**, y quitarlos sería un error: (a) los **nombres de
  campo** que el diseño decide que crucen la frontera —`experiment_id`, `run_id`, `unit_id`, `source_id`,
  `track_id`, `detection_id`, `prompt_set_id`, `clip_id`—, porque *qué información cruza* es diseño;
  verificado que §17.4 no los redeclara (`unit_id`, `source_id`, `track_id`, `detection_id` y `clip_id`
  aparecen **cero veces** en §17.4, de modo que sacarlos de §17.3 los dejaría huérfanos en todo el informe);
  (b) las **tecnologías con su justificación** (ZeroMQ, patrón publicador-suscriptor, msgpack, JSONL de sólo
  adición, HTTP, MQTT con QoS 1), que D2 y E3-04 ya fijaron como diseño; (c) los **nombres de estados** de
  la máquina de patrones. La prueba práctica: si el término nombra *qué* se intercambia o *por qué*, es
  diseño; si nombra *la versión concreta del esquema* o *el literal que viaja por el cable*, es §17.4.
- **D-P2-6 — Un identificador literal se declara una vez; la prosa se lee en castellano** (✎ 2026-08-22;
  completa a D-P2-5, que resolvió *en qué etapa* van, no *cuántas veces*). Fundamento medido: de los 11
  identificadores del par, **9 son `.v1`** — el sufijo varía en dos casos, así que en la enorme mayoría de
  las apariciones no aporta información y sólo quiebra el registro del texto. Reglas:
  1. **La prosa usa siempre la denominación en castellano** ("evento de percepción", "alerta interna",
     "envoltorio del bus", "contrato de ciclo de vida", "referencia temporal de evaluación"). Un
     identificador literal nunca es sujeto gramatical de una oración del informe.
  2. **Cada identificador aparece una sola vez**, y esa vez es la **Tabla 63** de §17.4.2 — el único punto
     de declaración. Sí se mantiene el identificador en prosa cuando **la versión o el literal son el
     argumento del párrafo** (hoy, sólo la glosa de la referencia temporal en §17.4.8, ver E4-23).
  3. **El CamelCase queda como está**: es la denominación de diseño que fijó D1 y aparece **sólo en celdas
     de tabla** (verificado: cero en prosa en ambas secciones). No se persigue.
  Aplicación: **E3-31** deja §17.3 en cero identificadores; **E4-24** aplica las reglas 1 y 2 a §17.4.
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

#### ✎ ENMIENDA 2026-08-22 — rigen las acciones 1, 3 y 4 de este bloque, no las de arriba

**Por qué se enmienda.** Un lector del capítulo llegó a §17.3.14.5, leyó *"…es opcional, deshabilitada por
defecto y fail-open: una falla o incertidumbre del preselector no debe eliminar la unidad del flujo
principal"* y reportó **no poder rastrear de dónde salía el concepto**. Esa es la falla real, y el
diagnóstico de E3-28 la explica: la primera aparición del término está **cruda, dentro de una celda de la
Tabla 43**, y la subsección que sí es dueña del concepto —§17.3.7.5, "Capacidades opcionales sin desplazar
el núcleo validable"— **nunca lo nombra**. El lector recibe una definición pero no encuentra la decisión.

La acción 4 original **agravaba ese recorrido**: quitaba la glosa precisamente en §17.3.14.5, dejando como
única definición del término una celda de tabla. Además contradice D-P2-1: una tabla se consulta, no se lee,
y no es lugar para la única definición de un concepto que reaparece seis veces.

**Criterio de la enmienda:** el término se nombra y se define **en prosa**, en la subsección que ya es dueña
del concepto; las tablas quedan libres de jerga; y el punto de reuso lleva un ancla breve en lugar de una
redefinición o de nada.

**Acciones 2 y 5: sin cambios** (eliminar el párrafo desubicado de §17.3.7.3; erradicar `opt-in` de las dos
celdas restantes).

**Acción 1 enmendada — Tabla 43, DA-11: enunciar la decisión sin el anglicismo.**

> **Decisión:** Permitir preselección liviana en el rol de captura como variante opcional, conservadora y
> deshabilitada por defecto, que conserva la unidad en el flujo principal ante falla o incertidumbre del
> preselector.
> **Justificación:** La variante puede reducir carga sin transformar el borde en fuente de verdad ni ocultar
> descartes, porque el flujo base continúa disponible y comparable.

**Acción 3 enmendada — §17.3.7.5, primer párrafo: acá nace el término.** Absorbe la oración que la acción 3
original rescataba, y agrega la definición:

> El núcleo validable del plano de medios debe poder operar sin exigir seguimiento multiobjeto formal,
> preselección en borde ni adaptación de modelos al dominio. Estas capacidades pueden incorporarse como
> variantes del flujo, pero no deben convertirse en requisitos para demostrar el procesamiento básico de
> CR-01 y CR-02, y su incorporación no modifica el contrato de salida del plano de medios. La preselección
> en borde se adopta además bajo un criterio de degradación segura, denominado fail-open: ante una falla o
> una decisión incierta del preselector, la unidad visual se conserva para el flujo principal. De ese modo
> la variante puede descartar carga, pero nunca convertirse en causa de pérdida de evidencia.

**Acción 4 enmendada — §17.3.14.5: ancla breve, ni redefinición ni vacío.** La segunda oración pasa a:

> La variante de preselección liviana en el borde es opcional, está deshabilitada por defecto y opera con el
> criterio de degradación segura fijado para las capacidades opcionales del plano de medios: una falla o
> incertidumbre del preselector no elimina la unidad del flujo principal.

*(Ancla descriptiva y no numérica a propósito: una referencia "§17.3.7.5" quedaría expuesta a los
corrimientos de numeración de este pase. Si se prefiere la forma explícita, el precedente es E3-07.)*

**Recorrido resultante para el lector**, que es lo que la enmienda arregla:

| Orden | Sección | Qué encuentra |
| --- | --- | --- |
| 1 | §17.3.3.1 | "preselección liviana en borde" como extensión condicionada — sin jerga |
| 2 | §17.3.3.4, DA-11 | la **decisión**, enunciada en castellano — sin jerga |
| 3 | §17.3.7.5 | el **término nombrado y definido en prosa**, con su razón |
| 4 | §17.3.14.5 · Tablas 57, 58 y 59 | usos posteriores, ya anclados |

**Huella final de `fail-open`: cuatro apariciones** — la definitoria de §17.3.7.5 más tres celdas de tabla:
**Tabla 57** (condiciones para interpretar EBE), **Tabla 58** (roles funcionales, fila *EN — modo base de
captura*) y **Tabla 59** (riesgos). Contra las siete actuales: §17.3.7.3 se elimina por la acción 2, DA-11
suelta el término por la acción 1 enmendada, la Tabla 61 desaparece por E3-25 y **§17.3.14.5 también deja de
usar el término** —el texto de la acción 4 enmendada dice "criterio de degradación segura", no `fail-open`—.
`opt-in`: cero (4 de 4).

⚠ **La Tabla 58 no la toca ninguna acción de E3-28, y está bien así.** Su celda dice *"La preselección
liviana es opcional, fail-open y deshabilitada por defecto"*; se deja intacta a propósito, porque con la
enmienda el término ya viene definido en prosa mucho antes (§17.3.7.5 precede a las tres tablas y a
§17.3.14.5). Se deja constancia para que no se lea como omisión ni se "corrija" por las dudas.

**Propiedad verificada:** con el orden resultante —§17.3.7.5 (L387 del texto extraído) antes de §17.3.14.5
(L877) y de las Tablas 57, 58 y 59 (L881, L919, L936)— **ninguna aparición del término precede a su
definición en prosa.** Es exactamente la propiedad que hoy falta y que originó esta enmienda.

---

### E3-29 · §17.3.10.3 "Política, medición y límites de interpretación" — reescritura completa

**Origen:** dos objeciones de lectura sobre el primer párrafo — *"¿por qué nombrar una configuración que no
se utiliza?"* y *"parece que estamos prediciendo el futuro; el diseño va antes que la implementación"*. Al
verificar el párrafo contra el código aparecieron además **dos afirmaciones falsas** en los párrafos
siguientes, y **dos límites de interpretación ausentes** en una subsección que los promete en el título.

**No afecta la numeración de tablas** (no agrega ni elimina tablas): §E queda igual.

#### Verificación (2026-08-22) — qué es cierto y qué no

| Afirmación del texto vigente | Veredicto |
| --- | --- |
| El motor posee capacidad técnica de control de re-confirmación | **Cierto.** Existe control de re-alerta por patrón y sujeto, en ventana temporal o por cuadros. |
| El núcleo no la utiliza | **Cierto.** El conjunto de patrones adoptado lo declara en su propia descripción: el motor emite en cada confirmación. |
| La supresión pertenece a la política del módulo de distribución | **Cierto sólo para el cooldown**, que está implementado y activo por defecto (ventana de 30.000 ms, clave condición + fuente). |
| "…—cooldown, **agrupación o limitación de tasa**—" | **FALSO.** Sólo existe el cooldown. La configuración de política admite exactamente dos parámetros (ventana y clave) y **rechaza claves desconocidas**: los otros dos mecanismos no están apagados, no son expresables. |
| "clave idempotente por evento, canal **y política**" | **FALSO.** La clave es de **dos** componentes: notificación y canal. La política no forma parte de la clave. |
| "distinguir entregas exitosas, supresiones deliberadas, duplicados y fallas de canal" | **Incompleto.** Los resultados posibles son **cinco**, no cuatro. Falta el descarte definitivo por agotamiento de reintentos, que es distinto de la falla de un intento y se registra además en un artefacto aparte. |
| `t_alert-notification` "mide desde la disponibilidad … hasta la confirmación" | **Incompleto.** La métrica se registra en **dos modalidades** y el propio reporte agrega las latencias **separadas por modalidad**. El texto describe una sola y no advierte que no son comparables. |

**Además, ausente y verificable:** el registro de entregas es de **sólo agregado y acumulativo entre
corridas** —ninguna fila se elimina jamás, la generación anterior se archiva íntegra al reutilizar un
directorio, y la deduplicación considera todas las generaciones—. Es un compromiso de trazabilidad que
corresponde exactamente a una subsección titulada "Política, medición y límites de interpretación".

#### Respuesta a la objeción 1 (¿por qué nombrar lo que no se usa?)

Se conserva la mención, con la razón explicitada. La capacidad inactiva no es trivia: es lo que convierte
una limitación aparente en una decisión. El reclamo que depende de ella es el del párrafo siguiente —las
re-alertas no se computan como falsos positivos—. Un lector que observa más alertas que episodios sospecha
un defecto o precisión inflada; nombrar la capacidad que existe y se dejó apagada es lo que responde eso.
El defecto del texto vigente no es mencionarla, es **dar el hecho y dejar el motivo para el párrafo
siguiente**, de modo que en su lugar se lee como dato suelto.

#### Respuesta a la objeción 2 (¿predicción del futuro?)

Correcta, pero apunta media cláusula a la izquierda. Asignar una responsabilidad a un módulo **es** el acto
de diseño, no una predicción — y en este caso ya está realizado: el cooldown existe. Lo que sí predice el
futuro es la **enumeración de tres mecanismos** cuando sólo hay uno. El informe ya tiene un idiom honesto
para eso: la Tabla 48 declara los canales adicionales como *punto de extensión*, no como política vigente.
La reescritura usa el mismo idiom.

#### Qué NO se explica acá porque ya está en Etapa 2 (§17.1)

Se relevó §17.1 contra esta subsección. Resultado, y criterio de poda aplicado al texto guía:

| Material | Dónde está ya | Consecuencia en §17.3.10.3 |
| --- | --- | --- |
| Qué mide `t_alert-notification` y su alcance | §17.1: *"extiende la medición hacia la disponibilidad de la alerta en el canal definido, pero no forma parte del núcleo evaluativo mínimo"*, más las condiciones para reportarla | **No se redefine.** §17.3 sólo agrega lo que es nuevo: que el registro conserva la modalidad de medición. |
| No mezclar costo computacional, ventana funcional de evidencia y demora de interfaz o distribución | §17.1, delimitación G2A / Glass-to-Alert | **No se reargumenta.** Sólo se declara el corte nuevo: entre modalidades. |
| La unidad de conteo del falso positivo debe declararse previamente y mantenerse constante | §17.1: la regla es explícita | **No se justifica.** Sólo se **declara** la unidad del tramo: la notificación, no la fila. |
| Ventanas de persistencia y trade-off de falsos positivos por severidad | §17.1, Tabla 24 | No se toca. |

**Lo que sí nace en §17.3 y no se recorta:** §17.1 no menciona en ninguna parte la supresión de
re-notificación, el cooldown, las re-alertas, la idempotencia ni el ledger de entregas — cero apariciones
de esos términos en todo el capítulo de Etapa 2. Todo el compromiso de política y trazabilidad del tramo
de distribución se establece por primera vez acá, de modo que no hay repetición que quitar.

#### Texto guía

> El conjunto de patrones adoptado no suprime confirmaciones: cada alerta interna se registra para
> conservar la dinámica real del episodio. La decisión es deliberada —el motor dispone de control de
> re-confirmación por patrón y sujeto y el núcleo lo deja inactivo— porque un motor que suprimiera dejaría
> de reflejar la duración del episodio y no permitiría distinguir una condición que persiste de una que se
> resolvió.
>
> La supresión de re-notificación se reubica en la política del módulo de distribución, y al reubicarse
> cambia de granularidad: el motor la aplicaría por patrón y sujeto, mientras que la política de entrega
> aplica una ventana de silencio por condición y fuente, porque para una notificación asistiva lo relevante
> es que esa condición en esa cámara ya fue avisada. La agrupación de avisos y la limitación de tasa quedan
> como punto de extensión de la política. Una alerta suprimida para comunicación existió y continúa siendo
> medible: las re-alertas de un episodio activo se informan por separado y no se computan como falsos
> positivos, de modo que una decisión de comunicación no altera la precisión del motor.
>
> El ledger de entregas aplica una clave de idempotencia por notificación y canal, es de sólo agregado y
> acumula entre corridas: al reutilizar un directorio de salida la generación anterior se archiva íntegra y
> la deduplicación considera todas las generaciones, por lo que un reprocesamiento no vuelve a entregar lo
> ya entregado. Cada fila conserva número de intento, marca temporal, resultado, motivo de error y
> confirmación del canal, y distingue cinco resultados: entrega exitosa, supresión por política, descarte
> por duplicado, falla de un intento y descarte definitivo por agotamiento de reintentos. La unidad de
> conteo del tramo es la notificación y no la fila: una notificación no entregada deja una fila por cada
> intento más la del descarte definitivo.
>
> Cada fila registra además la modalidad en que se midió `t_alert-notification`, y la latencia del tramo se
> informa siempre separada por modalidad: en relectura DBE el intervalo incorpora el ritmo de reinyección de
> las alertas persistidas, que es propiedad del reprocesamiento y no del canal.

**Balance de extensión:** cuatro párrafos contra seis, y una vez descontada la definición de la métrica y
la justificación de la regla de conteo —ambas de Etapa 2— la subsección queda apenas por encima del texto
vigente, con las dos afirmaciones falsas corregidas y los dos límites presentes.

**Nota de consistencia tipográfica** (no es contenido): en §17.1 la métrica aparece como ecuación de Word y
en §17.3.10.3 como texto corrido. Conviene unificar la forma de escribirla al cerrar las dos secciones.

---

### E3-30 · §17.3.11.1 "Criterios de diseño de contratos" — eliminar la subsección y rescatar una cláusula

**Origen:** pregunta de lectura — *"¿esta sección realmente suma?"*. Se relevó cada afirmación de la
subsección contra el resto de §17.3 y contra §17.1.

**No es solapamiento con Etapa 2.** §17.1 no trata contratos: cero apariciones de "versionado",
"autodescriptivo" o "payload", y delega el asunto de forma explícita —*"la instancia de análisis y diseño
arquitectónico deberá traducir esta definición en componentes, contratos, eventos y configuraciones"*—. El
material pertenece a §17.3. El problema es **redundancia interna del propio capítulo**.

#### Relevamiento afirmación por afirmación

| Afirmación de §17.3.11.1 | Dónde ya está | Veredicto |
| --- | --- | --- |
| Contratos explícitos, autodescriptivos, versionados, estables | En el **párrafo introductorio de §17.3.11, inmediatamente arriba**: *"modelos de datos versionados, serializaciones explícitas e interfaces concretas"*, *"bajo qué versión"* | Reformulación del párrafo anterior como lista normativa. |
| "La versión viaja dentro del payload" | **§17.3.11.4**: *"La versión viaja en el payload persistido y publicado"* | **Duplicado casi literal**, dentro de la misma §17.3.11. |
| "el transporte no sustituye la identificación del esquema" | En ningún otro lugar del capítulo | **ÚNICO aporte real.** Se rescata. |
| Un mismo evento se persiste como JSONL y se transporta en el envoltorio del bus sin volverse dos contratos | Dicho **tres veces antes**: §17.3.5 (*"la persistencia JSONL … no constituye un tercer patrón de acople"*), §17.3.8.4 (*"el payload publicado corresponde al mismo contenido lógico persistido"*), §17.3.10.2 (*"la modalidad de ejecución no modifica la semántica"*) | Cuarta enunciación, y la más débil: las tres anteriores están donde el lector las necesita. |
| Los identificadores delimitan niveles distintos y no son intercambiables | Ver defecto abajo | Defectuoso e innecesario. |

#### El defecto del párrafo de identificadores

Anuncia **cinco** identificadores y define **tres**.

- `run_id` **aparece una única vez en todo §17.3** —exactamente en esa oración— y nunca se define.
- `experiment_id` ya está definido, mejor y mucho antes, en **§17.3.6.2**: *"esta unidad se identifica
  mediante un `experiment_id`, mientras que cada componente conserva su propio identificador de corrida"*.
- `unit_id` y `source_id` se usan ya definidos en §17.3.11.3, §17.3.12.2 y §17.3.13.
- **Falta `detection_id`**, que es el identificador cuya confusión sí importa: §17.3.11.3 aclara que *"sólo
  identifica una detección dentro de la unidad visual; no constituye identidad entre frames"*, §17.3.8.3.2
  lo repite, y **§17.3.16 lo lista como riesgo arquitectónico** (*"identidad de detección interpretada como
  identidad temporal"*). El párrafo que promete decir cuáles identificadores no son intercambiables omite
  el único caso que el capítulo trata como trampa.

#### Corrección: eliminar la subsección, reforzar el párrafo introductorio de §17.3.11

**Texto guía** (reemplaza el párrafo introductorio de §17.3.11 y absorbe lo rescatable de §17.3.11.1):

> Los contratos estabilizan la semántica de intercambio entre componentes: definen qué información cruza
> cada frontera y bajo qué versión. En la arquitectura consolidada del núcleo se expresan como modelos de
> datos versionados, con serializaciones explícitas e interfaces concretas, y cada uno queda asociado a una
> corrida para que productores y consumidores puedan evolucionar de forma independiente. La versión viaja
> dentro del payload y no en el envoltorio de transporte: el canal puede cambiar sin que el hecho
> persistido pierda la identificación de su esquema. Las capacidades futuras deben evolucionar de forma
> aditiva sin romper la lectura de corridas históricas.

**Lo que se elimina y no se pierde:** la tesis de un contrato con dos transportes queda en sus tres
enunciaciones existentes; los niveles de identidad quedan definidos en los lugares donde cada identificador
se usa. Nada de esto es un compromiso de diseño que desaparezca (D-P2-2).

**Variante si se quiere conservar los niveles de identidad reunidos:** agregar una oración al final de
§17.3.11.3 —que ya trata `detection_id`— en lugar de una subsección propia, y ahí sí nombrar los cinco
identificadores **más** `detection_id`, definiendo los seis. No se recomienda: duplicaría definiciones que
ya funcionan en su lugar de uso.

#### ⚠ Consecuencia de numeración — afecta a E3-23 y E3-24

Eliminar el encabezado §17.3.11.1 corre las tres subsecciones siguientes:

| Hoy | Después de E3-30 |
| --- | --- |
| 17.3.11.1 Criterios de diseño de contratos | *(eliminada; absorbida en el intro de §17.3.11)* |
| 17.3.11.2 Fronteras informacionales de intercambio | **17.3.11.1** |
| 17.3.11.3 Contratos mínimos e interfaces | **17.3.11.2** |
| 17.3.11.4 Criterios de evolución durante la implementación experimental | **17.3.11.3** |

**E3-23** está redactada contra "§17.3.11.2, Tabla 49" y **E3-24** contra "§17.3.11.4, Tabla 51". Si se
aplica E3-30, esas dos unidades pasan a apuntar a **§17.3.11.1** y **§17.3.11.3** respectivamente. Aplicar
E3-30 **primero** y leer E3-23/E3-24 con el mapa nuevo, o aplicarlas antes y renumerar una sola vez al
final. No afecta la numeración de **tablas**: §E queda igual.

---

### E3-31 · Identificadores versionados en §17.3 — migran TODOS a §17.4 (aplica D-P2-5) ✎ REVISADA 2026-08-22

**Origen:** pregunta de lectura — *"§17.3 nombra versiones de contratos (`media.detection.v1`) porque ya
tenemos la plataforma implementada; ¿no debería eso ir a Etapa 4?"*.

> ⚠ **Esta unidad reemplaza a su primera versión (mismo día).** La primera versión proponía un criterio
> estrecho —"`.v1` se queda porque es declarable ex-ante; sólo `.v2` delata historia"— y desestimaba la
> variante estricta. La verificación contra el `.docx` de §17.4 v1.2 la refutó. Rige la versión estricta,
> formalizada como **D-P2-5**.

#### Los tres hechos que refutan el criterio estrecho (verificados 2026-08-22)

1. **§17.4 ya está escrito bajo el criterio estricto, y el par se contradice.** §17.4.2 abre con *"los
   contratos preliminares definidos durante el diseño se materializaron como…"* y su **Tabla 63** titula la
   primera columna **"Contrato del diseño"** con las denominaciones conceptuales (PerceptionEvent,
   AlertEvent, Referencia temporal…) y la segunda **"Materialización efectiva"** con los identificadores
   versionados. Bajo la lógica del propio informe, `media.detection.v1` **es** materialización. Si §17.3
   dice nueve veces `media.detection.v1`, la fila *PerceptionEvent → media.detection.v1* de la Tabla 63
   queda tautológica y la narrativa diseño→implementación se contradice a sí misma.

2. **El pase 1 ya venía moviéndose en esta dirección.** El texto guía de E3-04 (aplicado en la v1.1
   vigente) reescribió el párrafo de acople de §17.3.5 nombrando ZeroMQ, msgpack y JSONL **sin ningún
   identificador versionado**. La tecnología con su justificación es diseño (D2); el nombre de cable no lo
   acompañó.

3. **La asimetría existente prueba que el corte `.v1`/`.v2` era casualidad, no principio.** §17.3 nunca
   nombra `media.metric.v2` ni `control.metric.v1` — dice "contratos de métricas", genérico — y §17.4 los
   declara en la Tabla 63. Las métricas ya siguen el patrón correcto. Y los dos únicos `.v2` del par
   (`clip_gt.v2`, `media.metric.v2`) son exactamente los contratos que **iteraron durante la
   construcción**: el corte "los `.v1` pueden quedarse" sobrevivía sólo porque los demás contratos no
   alcanzaron a romperse. Si el evento de percepción hubiera iterado, §17.3 filtraría `media.detection.v2`
   con el mismo mecanismo.

**Qué conserva §17.3 (esto no cambia):** las decisiones de versionado como propiedades de diseño —"la
versión viaja dentro del payload", la regla de evolución aditiva de §17.3.11.4— enunciadas **en
abstracto**; las tecnologías con su justificación (D2/E3-04); las denominaciones conceptuales de la Tabla
50; y los nombres de estados `inactive`…`resolved` de §17.3.8.2 (vocabulario de la máquina de estados, que
es diseño por la excepción de D2 — se deja constancia para que no parezca omisión).

#### Inventario de aplicación — §17.3 queda con CERO identificadores `.vN`

Recuento sobre la v1.1 vigente: **42 menciones de 9 identificadores**. **11 mueren solas** con unidades ya
firmadas — 8 en la Tabla 49 (E3-23; son 7 filas pero 8 menciones), 2 en la Tabla 61 (E3-25) y 1 en
§17.3.11.1 (E3-30). Quedan **31 menciones en 19 puntos de edición**, todos mecánicos: el reemplazo usa
denominaciones que §17.3 ya definió. Números de tabla según la numeración **vigente** en el `.docx` v1.1
(el mapa post-pase está en §E).

| # | Ubicación | Vigente | Reemplazo |
| --- | --- | --- | --- |
| 1 | §17.3.8.1, párrafo del bus | "…serialización msgpack y envoltorio `bus.envelope.v1`" | "…serialización msgpack y un envoltorio versionado" |
| 2 | §17.3.8.1, párrafo siguiente | "Cuando un patrón alcanza el estado confirmado se registra `control.alert.v1`. La alerta interna es el hecho principal…" | "Cuando un patrón alcanza el estado confirmado se registra la alerta interna: es el hecho principal del sistema y precede a cualquier notificación." |
| 3–4 | §17.3.8.3.3, **Tabla 47**, filas PR-01 y PR-02, columna de insumos | "Eventos `media.detection.v1`, coordenadas…" (×2) | "Eventos de percepción, coordenadas…" (×2) |
| 5 | §17.3.8.4, camino EBE | "un seq monótono dentro de `bus.envelope.v1`" | "un número de secuencia monótono dentro del envoltorio versionado del bus" |
| 6 | §17.3.8.4, cierre | "El cierre se propaga mediante `run.lifecycle.v1`. El evento `run_finished` delimita el final lógico…" | "El cierre de la corrida se propaga mediante un evento de ciclo de vida cuyo hito de finalización delimita el final lógico…" (los DOS literales migran; quedan declarados en la fila *Cierre de corrida* que **E4-24** agrega a la Tabla 63) |
| 7 | §17.3.10.2, prosa | "Ambos caminos utilizan `control.alert.v1`, `control.notification.v1` y `control.delivery.v1`, por lo que…" | "Ambos caminos utilizan los mismos contratos de alerta interna, sobre de notificación y registro de entrega, por lo que…" |
| 8 | §17.3.10.2, **Tabla 48**, fila MQTT QoS 1 | "Publicar `control.notification.v1` y esperar…" · "…queda registrado en `control.delivery.v1`" | "Publicar el sobre de notificación y esperar…" · "…queda asentado como registro de entrega" |
| 9 | §17.3.11.3, **Tabla 50**, columna "Información mínima" — 6 celdas: PerceptionEvent, PatternStateChanged, AlertEvent, Referencia temporal de evaluación, NotificationEnvelope y DeliveryRecord | cada celda abre con su identificador (`media.detection.v1, run, unidad…`) | **quitar el identificador inicial de las 6 celdas** y habilitarlo con una oración única antes de la tabla: **"Todo contrato declara su identidad de esquema y su versión como primer elemento del payload."** El resto de cada celda queda igual. |
| 10 | §17.3.11.3, prosa | "El evento central del sistema es `media.detection.v1`. Agrupa la identidad de esquema, la corrida…" | "El evento central del sistema es el evento de percepción. Agrupa la identidad de esquema versionada, la corrida…" |
| 11 | §17.3.11.3, prosa | "La referencia `clip_gt.v2` impone dos invariantes…" | "La referencia temporal de evaluación impone dos invariantes…" (las invariantes quedan íntegras: son diseño) |
| 12 | §17.3.11.4 | "Un cambio aditivo conserva `media.detection.v1` porque no invalida consumidores existentes." | "Un cambio aditivo conserva la versión vigente del contrato porque no invalida consumidores existentes." (el resto de la subsección no se toca: la regla es diseño) |
| 13 | §17.3.13.2, **Tabla 54** (diccionario de métricas), fila TTFD | "requiere `clip_gt.v2`" | "requiere referencia temporal anotada" |
| 14 | §17.3.13.3, **Tabla 55** (señales observables), primera fila | "Eventos `media.detection.v1`" | "Eventos de percepción" |
| 15 | §17.3.14.5, prosa | "el matching temporal contra `clip_gt.v2` se declara no interpretable" | "el matching temporal contra la referencia temporal se declara no interpretable" |
| 16 | §17.3.15, **prosa** (cierre del párrafo del módulo de distribución) | "Puede co-ubicarse con el CPN o separarse sin modificar `control.alert.v1`, `control.notification.v1` ni `control.delivery.v1`." | "…sin modificar los contratos de alerta interna, notificación y entrega." |
| 17 | §17.3.15, **Tabla 58** (roles funcionales), fila *Módulo de distribución* | "Consumo de `control.alert.v1` desde el bus de alertas, política de notificación, ledger de idempotencia, entrega MQTT y registro de `control.notification.v1` y `control.delivery.v1`." | "Consumo de la alerta interna desde el bus de alertas, política de notificación, ledger de idempotencia, entrega MQTT y registro del sobre de notificación y del resultado de entrega." |
| 18 | §17.3.16, **Tabla 59** (riesgos y mitigaciones), fila *Notificación externa altera la métrica* | "Registrar primero `control.alert.v1`; ubicar cooldown…" | "Registrar primero la alerta interna; ubicar cooldown…" |
| 19 | §17.3.17, **Tabla 60** (plan de materialización), fila *Adaptador OVD* | "El modelo puede sustituirse sin modificar el contrato `media.detection.v1`." | "El modelo puede sustituirse sin modificar el contrato del evento de percepción." |

**No inventar un `clip_gt.v1` en §17.3.** El diseño no fija números de versión de ningún contrato; la
historia real de la referencia temporal se declara en §17.4 (ver E4-23).

**Verificación al aplicar:** buscar "`.v1`", "`.v2`" y "`run_finished`" en §17.3 → **cero resultados**.
Aritmética de control: 42 = 11 que mueren con E3-23/E3-25/E3-30 + 31 en los 19 puntos de arriba.
Todos los identificadores quedan declarados en la **Tabla 63** de §17.4.2 —incluida la fila *Cierre de
corrida* que agrega **E4-24**— más la excepción glosada de §17.4.8 (E4-23). Verificado contra el `.docx`
v1.2: el traspaso no deja ningún identificador huérfano.

**Ojo con los puntos 16–19: son cuatro ubicaciones distintas, no una.** Están en cuatro subsecciones y tres
tablas diferentes; tratarlas como un solo reemplazo global deja menciones vivas. En particular el punto 19
está en la **Tabla 60, que SOBREVIVE** (E3-25 elimina la 61, no la 60): es el punto que más fácil se pasa
por alto y sin él la verificación de "cero identificadores" falla.

**Interacciones:** los textos guía de E3-29 y E3-30 ya cumplen D-P2-5 (no nombran identificadores). E3-23 y
E3-25/E3-26 eliminan tablas que contenían menciones — aplicarlas no genera conflicto en ningún orden. La
fila 9 convive con la renumeración de E3-30 (§17.3.11.3 pasa a ser §17.3.11.2). Si se aplican las
opcionales, C-01 pasa a viñetas las Tablas 59 y 60 (puntos 18 y 19): el texto del reemplazo es el mismo.

**Decisión aceptada 2026-08-22 — la Tabla 50 conserva el CamelCase, NO se castellaniza.** Tras aplicar esta
unidad, la primera columna de la Tabla 50 (PerceptionEvent, AlertEvent, …) queda como único "identificador"
visible en §17.3. Es deliberado: ese CamelCase es la denominación de diseño que fijó D1 y es la **clave de
join** con la columna "Contrato del diseño" de la Tabla 63 — el lector que quiere el id de cable recorre
Tabla 50 → Tabla 63 y lo encuentra declarado una sola vez. Castellanizar la Tabla 50 rompería ese join.
No "corregirla" al aplicar el pase.

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

### E4-23 · §17.4 como único punto de declaración de identificadores versionados (contraparte de E3-31)

**Qué verifica y qué agrega.** Con E3-31 aplicada, §17.4 pasa a ser el primer lugar del informe donde el
lector ve un identificador `.vN`. Se verificó contra el `.docx` v1.2 que el traspaso está completo — **no
hay que agregar ninguna declaración**: la Tabla 63 ya declara `experiment.manifest.v1`,
`media.detection.v1`, `control.pattern_state.v1`, `control.alert.v1`, `media.metric.v2` /
`control.metric.v1`, `bus.envelope.v1`, `clip_gt.v2` y `control.notification.v1` / `control.delivery.v1`.
`run.lifecycle.v1` y el literal `run_finished` aparecen hoy en la prosa de §17.4.3 y §17.4.5; con **E4-24**
esa prosa pasa al castellano y ambos quedan declarados en la fila *Cierre de corrida* que E4-24 agrega a la
Tabla 63 — así el punto 6 de E3-31 los suelta sin dejarlos huérfanos. La Tabla 63 deja de ser parcialmente
tautológica y pasa a hacer el trabajo para el que existe.

**Única edición requerida — glosar por qué la referencia temporal es v2.** Tras E3-31, `clip_gt.v2` y
`media.metric.v2` quedan como los únicos sufijos "2" del informe, sin que ninguna v1 se mencione jamás. Para
la referencia temporal la pregunta es esperable (es el esquema del que dependen los resultados temporales de
§17.5) y la historia es real y honesta: la primera generación de la referencia registraba alertas esperadas
por sujeto, y fue reemplazada por episodios a nivel escena-condición con tiempos en milisegundos. En
§17.4.8, donde dice:

> *"…materializada mediante el esquema clip_gt.v2."*

pasa a:

> *"…materializada mediante el esquema clip_gt.v2, segunda versión de la referencia: la primera
> generación registraba alertas esperadas por sujeto y fue reemplazada por episodios a nivel de escena y
> condición con tiempos en milisegundos, junto con estados de aplicabilidad por clip."*

(Autocontenido: enuncia el hecho sin citar documentos del repositorio. Para `media.metric.v2` no se
propone glosa: es una fila de la Tabla 63 sin peso argumental en §17.5.)

**Qué NO hacer en §17.4:** no "corregir" la Tabla 63 reemplazando su columna "Contrato del diseño" por los
identificadores versionados — esa columna es el ancla hacia §17.3 y con D-P2-5 quedó exactamente bien como
está.

---

### E4-24 · §17.4 — sacar los identificadores literales de la prosa y sanear la Tabla 63 (aplica D-P2-6)

**Medición.** §17.4 tiene **22 menciones** de identificadores versionados: **14 en celdas de tabla** y
**8 en prosa**. Las 8 de prosa son el ruido; se reducen a **1**. Total resultante: **15**.

#### 1. §17.4.3 "Contratos de datos materializados" — el punto más denso (5 de las 8)

Hoy tres oraciones consecutivas usan un identificador como sujeto. **Texto guía** para los dos primeros
párrafos (el tercero, sobre evidencia auditable de la alerta, no se toca):

> Cinco contratos concentran los hechos principales de la ejecución; la Tabla 63 los identifica por su
> esquema y versión. El evento de percepción normaliza la salida del detector e incluye identificación de
> corrida y unidad visual, descripción de la fuente, perfil de modelo, conjunto de prompts, detecciones con
> coordenadas en píxeles y normalizadas, y tiempos por unidad. El envoltorio del bus encapsula el mismo
> payload para su transmisión e incorpora un número de secuencia monótono que vuelve detectable cualquier
> hueco.
>
> El contrato de ciclo de vida delimita la corrida y la cierra mediante un evento de finalización. El
> registro de transiciones del patrón recorre los estados inactive, candidate, confirmed, sustained y
> resolved (figura de la sección 17.3.8.2), junto con la evidencia y los hitos temporales que las motivaron.
> La alerta interna registra la confirmación de un episodio mediante un identificador determinista, de modo
> que reprocesar la misma corrida produce la misma identidad de alerta y permite deduplicar sin estado
> compartido.

Se conservan íntegros el contenido, los nombres de estados (D-P2-5) y la referencia a la figura.

#### 2. Las tres menciones de prosa restantes

| Ubicación | Vigente | Acción |
| --- | --- | --- |
| §17.4.5, camino EBE | "la evidencia se transmite por el bus ZeroMQ dentro de `bus.envelope.v1`; … el cierre se comunica mediante `run_finished`" | "…dentro del envoltorio versionado del bus; … el cierre se comunica mediante el evento de finalización de la corrida". **Ambos literales ya están declarados** (`bus.envelope.v1` en la Tabla 63; para el evento de finalización, agregar la fila de la regla 3 abajo). |
| §17.4.8, referencia temporal | "materializada mediante el esquema `clip_gt.v2`" | **SE CONSERVA**, con la glosa de E4-23: acá la versión *es* el argumento del párrafo (excepción de la regla 2). |
| §17.4.11, identidad de sujeto | mención en el párrafo de extensiones | Reemplazar por la denominación en castellano; el contrato ya está en la Tabla 63. |

#### 3. Tabla 63 — que cada columna haga un solo trabajo

Auditada fila por fila, la columna **"Versionado y trazabilidad"** mezcla **8 celdas que son un
identificador literal** con **8 que son una oración en prosa** ("Catálogo versionado; un archivo por
variante", "Contrato interno; viaja dentro del evento publicado", "Esquema por componente, registrado por
corrida"…). El lector no puede escanearla para saber si un contrato tiene esquema versionado propio o no.

**Acción mínima y suficiente — ampliar la Nota al pie**, sin tocar las 16 filas:

> **Nota.** La tabla documenta la correspondencia semántica entre el diseño y la implementación. Nueve
> contratos se materializan como **esquema versionado con identificador propio**, que es el que viaja en el
> payload y queda registrado en los artefactos de cada corrida; los restantes se versionan por **catálogo,
> configuración congelada o por el manifiesto de la ejecución experimental**, sin esquema propio. Esta tabla
> es el único punto del informe donde se declaran esos identificadores: el resto del capítulo se refiere a
> cada contrato por su denominación.

**Fila nueva** (para que el evento de finalización quede declarado al soltarlo §17.3 y §17.4.5):

> **Cierre de corrida** || *Evento de finalización publicado al cerrar la corrida* || `run.lifecycle.v1`
> (evento `run_finished`) || *Ambos planos*

*(Con esta fila la tabla pasa de 16 a 17 filas y de 9 a 10 contratos con esquema propio — ajustar el "nueve"
de la Nota a **diez** al aplicar.)*

**Lo que NO se hace:** reemplazar la columna 1 por identificadores. Es el ancla hacia §17.3 (D-P2-5) y su
mezcla de CamelCase y castellano es la que fijó D1 — se deja.

**Verificación al aplicar:** en §17.4, identificadores `.vN` fuera de la Tabla 63 → **una sola** ocurrencia,
la de §17.4.8 con su glosa. Y ningún identificador literal como sujeto gramatical en todo el capítulo.

### E4-25 · §17.4.4, Tabla 64 — el propósito de cada interfaz, cerrado y sin asimetrías falsas

**Origen:** directiva del usuario — *"el propósito de cada interfaz relevante que mostramos en el informe
tiene que estar súper claro y justificado, para no dejar dudas para el tribunal"*. Auditada la Tabla 64
contra las rutas reales de los tres servicios (2026-08-22), aparecen tres defectos y un remanente de E4-24.

#### Defectos verificados

1. **Asimetría de detención FALSA por omisión — el peor de los tres.** La tabla muestra `cancel` sólo en la
   distribución. Verificado contra el código: **el plano de medios SÍ expone detención**
   (`POST /api/runs/{id}/stop`, 202, cooperativa) y no figura; **el plano de control es el ÚNICO que no la
   expone**, y eso no se señala ni se justifica. Un tribunal que escanee la tabla concluye exactamente lo
   contrario de la realidad. La Nota agrava: *"las interfaces de administración y detención conservan…"*
   insinúa endpoints sin decir cuáles existen y cuáles no.
2. **Celdas que parafrasean el verbo HTTP** en lugar de decir para qué está la operación ("Consulta el
   estado de la corrida de entrega" no informa nada que el nombre del endpoint no diga).
3. **La garantía de suscripción está enunciada sólo para el control.** El párrafo final dice *"la respuesta
   afirmativa del plano de control implica que su consumidor ya está suscripto"* — pero la misma garantía
   del 201 de la distribución (bus de alertas) no está, y el **orden de disparo inverso al flujo de datos**
   (distribución → control → medios), que es la doctrina que justifica la existencia misma del
   `POST /api/runs` de la distribución, no se deriva en ninguna parte.
4. **Remanente de E4-24:** quedan 4 identificadores en celdas fuera de la Tabla 63 — 3 en la Tabla 64
   (fila `:5557` y fila `:5558`) y 1 en la Tabla 69.

**Hecho verificado que habilita la justificación:** los tres servicios implementan el mismo contrato de
gobierno — una corrida activa por vez, rechazo de solicitudes concurrentes señalando la corrida activa
(`RunBusyError` existe en los tres), configuración efectiva persistida por corrida.

#### Acciones

**A. Tabla 64 — filas.** Celdas cortas (D-P2-1); la justificación profunda va a la prosa de la acción C.

| Fila | Acción |
| --- | --- |
| Plano de medios — **fila nueva** tras `POST /api/runs` | `POST /api/runs/{id}/stop` → *"Detiene cooperativamente la corrida en curso; el cierre se propaga a los consumidores por el bus."* |
| Distribución `GET /api/runs/{id}` | → *"Consulta estado y conteos de entrega; determina cuándo consolidar artefactos."* |
| Distribución `POST /api/runs/{id}/cancel` | → *"Detiene cooperativamente una corrida de entrega en curso."* (mismo verbo que el stop de medios: es el mismo mecanismo) |
| Fila `Medios → control (:5557)` | → *"Transporta los eventos de percepción y el ciclo de vida de la corrida dentro del envoltorio versionado del bus."* |
| Fila `Control → distribución (:5558)` | → *"Transporta las alertas internas confirmadas hacia el módulo de distribución."* |
| Las demás filas | Sin cambios — `POST /api/runs` de los tres ya dice qué cruza; los `GET /api/config` y `GET /api/model` quedan, su propósito lo da la prosa. |

**B. Nota de la tabla — decir la verdad en vez de insinuarla:**

> **Nota.** La tabla resume las operaciones de gobierno principales; no es un inventario exhaustivo
> (listados, corrida actual, artefactos por corrida, comprobaciones de salud y limpieza del registro se
> omiten). La detención figura únicamente donde el servicio la expone: el plano de control no ofrece
> detención de una corrida en curso, y esa asimetría es deliberada (ver el texto).

**C. Prosa — reemplazar el párrafo final** (*"En una corrida live, la respuesta afirmativa del plano de
control implica que su consumidor ya está suscripto."*) por tres párrafos que justifican lo que la tabla
declara:

> Los tres servicios implementan el mismo contrato de gobierno: admiten una corrida activa por vez y
> rechazan solicitudes concurrentes señalando la corrida en curso; cada corrida declara su configuración al
> crearse y el servicio persiste la configuración efectiva utilizada. Las operaciones de consulta de
> configuración y de perfil de modelo permiten verificar, antes de disparar, que el servicio cargó lo que el
> experimento requiere: sin ellas, una discrepancia entre lo configurado y lo desplegado sólo se descubriría
> en los resultados.
>
> En una corrida en vivo, la respuesta afirmativa de cada consumidor del bus implica que su suscripción ya
> está establecida: la del plano de control sobre el canal de detecciones y la del módulo de distribución
> sobre el canal de alertas. De esa garantía se deriva el orden de disparo, inverso al flujo de datos:
> primero la distribución, después el control, por último el plano de medios. Un consumidor suscripto tarde
> perdería los eventos ya publicados sin ningún error observable; el orden de disparo excluye esa pérdida
> por construcción.
>
> La detención de corridas es cooperativa en los dos servicios que la exponen: la solicitud marca la corrida
> y el hilo de ejecución la observa entre unidades, sin cortes abruptos que dejarían artefactos a medio
> escribir. El plano de control no expone detención, y la asimetría es deliberada: su corrida en vivo se
> cierra con el evento de finalización que publica el plano de medios —la relación entre ambas corridas es
> uno a uno—, de modo que la intervención del operador se ejerce aguas arriba y el cierre llega por el mismo
> canal que los datos. El módulo de distribución, en cambio, requiere cancelación propia: una corrida de
> entrega puede permanecer a la espera de alertas y debe poder abortarse sin reiniciar el servicio.

**D. Tabla 69, fila "Dato adicional en la detección":** *"Evolución aditiva sin ruptura de
`media.detection.v1`"* → **"Evolución aditiva sin ruptura del contrato de percepción."**

**Corrección aritmética a E4-24:** su "Total resultante: 15" no contaba el identificador de su propia fila
nueva (*Cierre de corrida*); con ella son 16. Tras esta unidad quedan **12**: los 11 de la Tabla 63
(10 filas actuales + la nueva) y la glosa de §17.4.8 (E4-23). Con esto, la regla 2 de D-P2-6 pasa a
cumplirse literalmente: **ningún identificador vive fuera de la Tabla 63, salvo la excepción glosada.**

**Verificación al aplicar:** (a) en §17.4, ids `.vN` fuera de la Tabla 63 → sólo la glosa de §17.4.8;
(b) la Tabla 64 muestra detención en medios y distribución, y la Nota + prosa explican por qué el control
no; (c) el orden distribución → control → medios queda derivado en la prosa — es la misma advertencia de
cita que acompaña a la figura de arranque ("orden de arranque inverso al flujo de datos"), ahora con su
porqué en el cuerpo del informe.

### E4-26 · §17.4.6 — el núcleo no tiene UN modelo: tiene un catálogo que se ejerce entero

**Origen:** objeción del usuario sobre el tercer párrafo de §17.4.6 — *"no tenemos un solo modelo para el
núcleo; el perfil de modelo para el núcleo son todos los que probamos. Esto es experimental"*. La objeción
es doctrinaria y es correcta: la tesis no corona un modelo, muestra una plataforma que mide modelos de dos
familias bajo condiciones idénticas y da veredictos POR MODELO en §17.5. El texto vigente
—*"El perfil desplegado para el núcleo es grounding-dino/gdino-tiny-560, seleccionado en la comparación…"*—
promueve una decisión operativa de una corrida a identidad del sistema, que es exactamente el encuadre que
la defensa debe evitar (la plataforma es la tesis; el detector es la variable).

#### Hechos verificados (2026-08-22, contra el repositorio del plano de medios)

- **El catálogo vigente tiene NUEVE perfiles** más el mock: Grounding DINO tiny y base, cada uno en 800 y
  en 560 píxeles (4), y YOLOE en tamaños s/m/l/x (4). Cada perfil es un archivo del catálogo con su
  adaptador, umbrales y licencia.
- **MM-Grounding DINO NO está en el catálogo vigente**: sus tres perfiles están **archivados**
  (`configs/_archive/`, 2026-08-19), tras su descarte experimental. La frase del informe "incluye variantes
  … de MM-Grounding DINO" es **falsa en presente**; la familia se integró y se descartó — ese descarte es
  un RESULTADO que se informa en §17.5, no una fila del catálogo actual.
- **El despliegue integral materializa el catálogo entero como flota**: una instancia de servicio por
  perfil, orquestadas por la consola. "Comparar perfiles = disponer procesos con perfiles distintos"
  (§17.4.4) está implementado literalmente.
- Los valores citados del perfil `gdino-tiny-560` (umbral de caja 0,30, de texto 0,25, entrada 560) están
  confirmados contra su archivo de catálogo. No se cuestionan — se re-encuadran.
- Existen además dos perfiles de checkpoints de ajuste fino **no adoptados** (rama comparativa): no se
  enumeran en el catálogo del núcleo; su lugar es la fila de la Tabla 68 y §17.5.

#### Acciones

**A. Retitular §17.4.6:** "Configuración efectiva y modelo desplegado" → **"Configuración efectiva y
catálogo de modelos"**. El título vigente lleva el encuadre de modelo único. (Sin impacto: ninguna otra
sección referencia "17.4.6" por número.)

**B. Reemplazar el tercer párrafo** (los dos primeros —pattern set y estrategia perceptiva— no se tocan).
**Texto guía:**

> El catálogo de perfiles de modelo materializa la sustituibilidad prevista en el diseño: variantes de
> Grounding DINO —tiny y base, cada una con resolución de entrada de 800 y de 560 píxeles— y de YOLOE en
> cuatro tamaños, todas integradas mediante adaptadores sobre el mismo contrato de salida. Una tercera
> familia, MM-Grounding DINO, se integró por el mismo mecanismo y fue descartada durante la evaluación; su
> descarte se informa con los resultados y sus perfiles quedaron archivados fuera del catálogo activo.
>
> El núcleo no fija un modelo único. Cada instancia del servicio de medios carga un perfil al iniciarse, la
> comparación entre perfiles se materializa disponiendo instancias con perfiles distintos bajo la misma
> configuración de corrida, y el despliegue integral de la plataforma instancia un servicio por perfil del
> catálogo, orquestados desde la consola. Los perfiles vigentes se compararon sobre el banco de imágenes
> congelado; las campañas temporales y en vivo fijan un perfil por corrida, declarado en el manifiesto. Los
> resultados por modelo y por familia, y los criterios pre-registrados con que se seleccionó el perfil de
> cada campaña, se presentan en la sección 17.5.
>
> Cada perfil declara sus umbrales y su postproceso en el catálogo, y cada corrida persiste la configuración
> efectiva utilizada, sin constantes ocultas en el código. A título de ejemplo, el perfil fijado por
> criterio pre-registrado para las corridas en vivo declara umbral de caja de 0,30 y de texto de 0,25; su
> postproceso aplica confianza mínima de 0,25, supresión de solapamientos con IoU de 0,50 y área mínima de
> caja de 100 píxeles cuadrados; y el control de ritmo opera con selección determinista de paso 1 y una cola
> máxima de ocho unidades.

Qué cambia y por qué: (1) **MM-GDINO pasa de fila del catálogo a hecho histórico con remisión a §17.5** —
deja de ser falso y se vuelve evidencia de sustituibilidad (la familia entró y salió sin tocar el contrato);
(2) **"el perfil desplegado para el núcleo es X" desaparece** — lo reemplaza la regla general (un perfil por
instancia, un perfil por corrida, declarado en el manifiesto) y la flota que materializa el catálogo entero;
(3) los valores efectivos **se conservan todos** pero como *ejemplo* de la propiedad que importa (config
efectiva persistida), y el identificador `gdino-tiny-560` sale de la prosa — coherente con D-P2-6, el
manifiesto de cada corrida es quien lo declara; (4) la selección queda como **decisión operativa
pre-registrada por campaña**, con su criterio en §17.5, no como veredicto.

**C. Nota para la redacción de §17.5 (fuera del alcance de este pase, dejar constancia):** presentar los
resultados **por modelo y por familia**, cada combinación con su dato; la selección del perfil live se
presenta como decisión operativa con criterio pre-registrado sobre el banco de imágenes, incluyendo que la
misma comparación identificó a un perfil distinto como más fuerte en otra dimensión (recall de la condición
CR-01) — la evidencia de que el veredicto es por combinación, no único. Nunca la fórmula "el mejor modelo".

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

**Subsecciones** (✎ agregado 2026-08-22 — faltaba: dos unidades de este pase eliminan encabezados y §E sólo
cubría tablas). Dos corrimientos, en ramas distintas y por lo tanto independientes:

| Unidad | Encabezado que se elimina | Corrimiento |
|---|---|---|
| **E3-20** | §17.3.6.6 *Validaciones previas al inicio de la corrida* | §17.3.6.7 → **§17.3.6.6** |
| **E3-30** | §17.3.11.1 *Criterios de diseño de contratos* | §17.3.11.2 → **.1** · §17.3.11.3 → **.2** · §17.3.11.4 → **.3** |

**No hay referencias que se rompan** — verificado sobre ambos `.docx`: el par entero contiene sólo tres
referencias a subsecciones de §17.3 (§17.3.11 como padre, y "sección 17.3.8.2" y "sección 17.3.8.4" desde
§17.4), y **ninguna** apunta a un encabezado que se mueva. Sí quedan afectadas las referencias *internas de
este documento de correcciones*: **E3-23** apunta a "§17.3.11.2, Tabla 49" y **E3-24** a "§17.3.11.4,
Tabla 51"; con E3-30 aplicada pasan a §17.3.11.1 y §17.3.11.3. La enmienda de E3-28 usa ancla descriptiva y
no numérica justamente para no depender de este mapa.

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
