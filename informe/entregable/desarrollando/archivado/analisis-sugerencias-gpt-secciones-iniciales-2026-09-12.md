# Análisis de las sugerencias de GPT sobre las Secciones Iniciales (§2–§14) — 2026-09-12

- **Documento revisado:** `desarrollando/E-OVRT-VDP_Secciones_Iniciales_hasta_14_v1.0_sugerencias.docx`
  (bajada de Google Docs del 2026-09-12 03:19; `sha256(word/document.xml)` empieza en `3006b823`).
- **Entregables de esta revisión:**
  1. este documento;
  2. `desarrollando/E-OVRT-VDP_Secciones_Iniciales_hasta_14_v1.1 (sugerencias GPT + Claude, sin aceptar).docx`
     — el mismo archivo con mi veredicto aplicado **como capa de sugerencias y comentarios encima de las de
     GPT**, sin resolver nada (mecánica en §9);
  3. `herramientas/pase_secciones_iniciales_v11.py` — el guion que lo produce y lo verifica.
- **Consigna:** evaluar las sugerencias de GPT, los cambios sobre el glosario y los comentarios; controlar que
  no den de más ni omitan información; **§14 (planificación) y §14.4 (costos) quedan como en la primera
  versión**.
- **Lo que no se pudo ver.** Los comentarios que se resuelven en Google Docs **no viajan en la exportación**
  (ya verificado el 09-07 sobre §17.5): en el archivo sólo están los 36 hilos abiertos. De los comentarios ya
  resueltos no queda rastro, salvo dos párrafos de §12.1 que aparecen editados **sin marca** (sugerencia
  aceptada y comentario resuelto): se revisan igual en §4.

---

## 0. Resumen

1. **La lectura del usuario se sostiene, con un matiz.** De las 30 sugerencias de GPT (22 unidades de texto
   más 8 filas del glosario), **9 son actualizaciones correctas** que el informe necesita (AJ-0.01 sobre el
   alcance, AJ-0.02 sobre el vocabulario, y la baja de promesas que quedaron falsas: «imágenes de
   referencia», «utilidad operativa», «interoperabilidad futura»). Las otras **21 hacen dos cosas que una
   introducción no debería hacer**: traer a §12 la arquitectura y las reglas de lectura de §17 y las
   conclusiones de §18, y **reescribir la hipótesis y los objetivos desde el resultado**.
2. **La hipótesis de GPT es un espejo de §18.1.** Su redacción («es técnicamente factible integrar detección
   open-vocabulary, procesamiento de video y estabilización temporal ... sin requerir ajuste de pesos para
   el núcleo») calca casi palabra por palabra la respuesta del cierre. Una hipótesis escrita después de la
   respuesta deja de ser contrastable. Lo mismo pasa con cuatro de los siete objetivos específicos.
3. **Omisiones concretas de GPT** (todas repuestas en la v1.1): «seguridad laboral» como campo del cruce
   disciplinar (§12.1); el **presupuesto de latencia** y la **arquitectura de transporte de video** entre las
   dimensiones de la hipótesis (§12.3); «bajo condiciones controladas y reproducibles» (§12.3);
   «limitaciones y líneas futuras» como salida del método (§12.5); la **condición por datos y protocolo** de
   la rama de ajuste fino (§12.3, ADR-017); los ejes **normativo, seguimiento multiobjeto y transmisión de
   video** del objetivo 1, que la Etapa 1 sí cubrió (§15.3, §15.4, §16.2.1); los **niveles de severidad** del
   objetivo 2; y las **métricas de seguimiento y la utilidad operativa** del objetivo 5, que §18.6 declara
   expresamente como no cumplidas.
4. **Excesos concretos de GPT** (quitados en la v1.1): asignar cada eslabón a un plano en §12.3; «este último
   nivel representa a la plataforma completa» (regla de lectura de §17.5.1); «el funcionamiento en vivo no
   equivale al cumplimiento del presupuesto de latencia» (conclusión de §18.4) en §12.4; «con registro de
   sus resultados de entrega», «herramientas de orquestación e inspección experimental», «contratos
   explícitos, configuración reproducible y mecanismos de persistencia» en objetivos; el identificador de
   configuración `canonical_v2` en el glosario (cero usos en §15–§19).
5. **Glosario.** Las siete filas nuevas de GPT están **justificadas por el uso real** en las secciones
   vigentes (tabla en §5.2) y recomiendo conservarlas, dos con retoque. Sobre el pedido del colega de sacar
   MOTA/IDF1/HOTA, recomiendo **conservarlas**: §15.3.3, §17.1.7 y §18.6 las nombran. Agrego cinco filas
   que faltan y que el cuerpo usa sin definir (G2A, E-DIR/E-IND, vocabulario activo, episodio, re-alerta).
6. **§14 está intacto**: ninguna marca de GPT desde §14 en adelante (verificado unidad por unidad). Las
   fichas AJ-0.03/0.04/0.05/0.06 siguen pendientes y no las toca nadie, por decisión de congelar el plan.
7. **Vista final si se acepta todo lo de Claude:** §12–§13 pasan de 2.048 palabras (original) a 2.205
   (+7,7 %); la propuesta de GPT daba 2.087. El crecimiento es lo que GPT había recortado y se repone,
   más lo que GPT agrega y vale.

---

## 1. Qué se revisó y cómo

| Paso | Cómo | Resultado |
|---|---|---|
| Extracción con marcado | guion propio sobre `word/document.xml`: `{+inserción+}`, `[-borrado-]`, anclas de comentario, filas de tabla envueltas en `w:sdt` | 181 unidades; 114 cambios controlados (68 `w:ins`, 46 `w:del`), todos del autor **ChatGPT** con una sola marca de tiempo (2026-09-11 03:59 Z) |
| Comentarios | `comments.xml` + `commentsExtended.xml` | 36 hilos abiertos, `done=0` en todos: **29 de ChatGPT** y **7 de «Matias Lautaro Carrizo»** (12-09, 02:17 a 03:13), 3 de ellos respuestas a hilos de GPT |
| Base de comparación | vista rechazada del documento contra la foto del maestro v1.1 (`96a`) | §12–§14 idénticos al maestro salvo **dos párrafos de §12.1 ya editados sin marca** (§4); el glosario **ya venía modernizado** en la v1.0 (§5.1) |
| Coherencia hacia adelante | extracción de las versiones vigentes de §15/16 v1.4, §17.1 v1.21, §17.3 v1.12, §17.4 v1.15, §17.5 v1.5 y Etapa 6 v1.1; conteo de uso de cada término del glosario y de las siglas frecuentes | tablas de §5; verificación de que §18.1 y §18.6 siguen respondiendo a §12.3 y §13 |
| Remisiones de GPT | todas las subsecciones que citan sus comentarios (§17.1.2, §17.1.7, §17.3.4, §17.3.6, §17.3.7, §17.4.1, §17.4.2, §17.4.7, §17.4.8, §17.5.4, §17.5.6, §17.5.7, §17.6.4, §18.1, §18.2, §18.4, §18.5, §18.6, §16.2, §16.3, §16.6) | existen en las versiones vigentes |

Autoría: las marcas dicen «ChatGPT» porque el documento se editó desde el Project; los siete comentarios
humanos llevan el nombre de la cuenta de Google con la que se hicieron. Acá se los llama «del colega».

---

## 2. Foto del documento

- **§2–§7** (portada, hoja de aceptación, dedicatoria, agradecimientos, título, resumen, palabras clave):
  un solo cambio, en la última palabra clave (§4, u044).
- **§11 Glosario** (Tabla 1, 60 filas en el maestro): GPT cambia la definición de **Zero-shot** y agrega
  **7 filas**; el colega comenta 3 filas existentes y 1 nueva.
- **§12 Introducción**: GPT reescribe **13 de los 18 párrafos**; dos más ya venían editados y aceptados.
- **§13 Objetivos**: GPT reescribe el título, el objetivo general y **5 de los 7** específicos.
- **§14 Plan de trabajo, §14.3 Cronograma, §14.4 Costos**: **sin ninguna marca**. La Figura 1 (Gantt) y el
  placeholder de §14.4 están como en el maestro. (El borrador v0.1 de §14.4 vive en otro documento y no
  entra acá.)

---

## 3. Diagnóstico general: tres patrones en las sugerencias de GPT

### 3.1. Actualizaciones legítimas (conservar)

- **AJ-0.01, alcance (§12.4).** El maestro sugería cobertura de zonas, maquinaria y obstrucciones; GPT
  declara el núcleo CR-01/CR-02 y deja el resto como catálogo conceptual. Coincide con §17.1.2.1 y §18.6.
- **Identidad temporal ≠ identidad personal**, y la **distribución MQTT existe** (ADR-016): el maestro
  hablaba de «interoperabilidad futura». Correcto, aunque la voz («se implementó e integró») se corrige.
- **Baja de promesas falsas**: «imágenes de referencia» como modalidad de consulta (la modalidad visual no
  se ejerció; sólo aparece en §15), «utilidad operativa de las alertas» como propiedad evaluada (no hubo
  estudio de respuesta de operadores), «maquinaria cerca de peatones» como ejemplo del núcleo.
- **Voz en presente** para lo que existe (§12.4 último párrafo, D-P3-9).
- **Glosario**: las siete filas nuevas responden a AJ-0.02 y a términos que el cuerpo usa sin definir.
- **Sus comentarios** están bien fundados: cada uno remite a la subsección que lo respalda, y en el
  objetivo 5 GPT mismo avisa «cambio sustantivo para revisión». Una inconsistencia: el comentario c9 dice
  «no se reinstala el nombre de configuración deprecado ni los códigos internos», pero la fila introduce
  `canonical_v2`, que es un identificador interno (§5.2).

### 3.2. Adelanto de la arquitectura y del cierre a la introducción (quitar)

Es el patrón que el usuario percibió, y se verifica en el texto:

| Dónde | Frase de GPT | De dónde viene |
|---|---|---|
| §12.1 u055 | «estas consultas se articulan con estrategias de detección y reglas explícitas de asociación y persistencia temporal ... producir evidencia perceptiva, evaluar patrones de riesgo y registrar y distribuir alertas» | §17.3.4/§17.3.6 (lo señala el colega: «acá ya se pone a explicar lo que hace la plataforma») |
| §12.3 u064 | «inferencia open-vocabulary en el plano de medios, evaluación ... en el plano de control»; «este último nivel representa a la plataforma completa» | §17.3 y la regla de lectura de §17.5.1 |
| §12.4 u070 | «el funcionamiento en vivo no equivale por sí mismo al cumplimiento del presupuesto de latencia ni a una validación operativa general»; «estrato de obra real» | conclusión de §18.4; jerga de §17.5 |
| §12.4 u069 | «con registro de sus resultados de entrega» | detalle del módulo de distribución (§17.4) |
| §12.2 u059 | «No se evalúa la reducción de la carga cognitiva del supervisor ni el efecto ... sobre la incidencia de accidentes» | límite de §18.6, puesto en el planteo del problema |
| §13.2 u084 | «herramientas de orquestación e inspección experimental» | la consola y el runner (§17.4) |
| §13.2 u083 | «contratos explícitos, configuración reproducible y mecanismos de persistencia e inspección de la evidencia» | propiedades de la implementación (§17.4) |

Los planos de medios y de control **ya estaban** en el maestro (§12.5 y objetivo 3): eso no es de GPT.

### 3.3. Reescritura de hipótesis y objetivos desde el resultado (rechazar)

- **Hipótesis (u062).** Original: OVD como «habilitador tecnológico viable para superar parte de la rigidez
  de los sistemas closed-set». GPT: «es técnicamente factible integrar detección open-vocabulary,
  procesamiento de video y estabilización temporal en una plataforma configurable ... sin requerir ajuste
  de pesos para el núcleo». Compárese con §18.1: «El proyecto mostró la factibilidad técnica de integrar
  detección open-vocabulary, procesamiento de video, estabilización temporal y distribución de alertas en
  una plataforma experimental trazable ... sin ajustar los pesos del núcleo». La hipótesis pasa a ser la
  respuesta en futuro.
- **Objetivos (u079, u081, u082, u085).** El kit de la Etapa 6 fija la regla: *«§12 Introducción (hipótesis
  de trabajo, alcance) y §13 Objetivos del informe v1.1: §18 tiene que responderlos uno por uno; se citan,
  no se reescriben (son Etapa 0)»*. §18.6 ya está escrito contra los objetivos del maestro y declara lo que
  no se cumplió («la evaluación MOT ... mantiene los límites ya expuestos»; «no prueba ... utilidad
  percibida por responsables de seguridad»). Si el objetivo 5 deja de nombrar seguimiento y utilidad
  operativa, esas dos frases de §18.6 pierden su referente y el informe **oculta una reducción de alcance en
  vez de declararla**. Además, **§14 queda congelado**: el plan (§14.2.5: «métricas: precisión, recall, F1,
  FPS, latencia»; §14.2.1: MOT y protocolos de transmisión) y los objetivos son la misma capa; si uno se
  reescribe desde el resultado y el otro no, el documento se contradice a sí mismo.
- **Consecuencia práctica:** conservar el objetivo general y los objetivos 1, 2 y 5 tal como estaban;
  sumar sólo la distribución de alertas en 3 y 4 (única capacidad nueva respecto del plan, ADR-016).

---

## 4. Veredicto unidad por unidad

Leyenda: **A** aceptar · **AC** aceptar con cambios (Claude tacha la propuesta de GPT e inserta la
alternativa) · **R+** rechazar la de GPT y retocar el original (misma mecánica) · **R** rechazar (sólo
comentario; basta rechazar la sugerencia de GPT). «c##» es el comentario de Claude en la v1.1.

| Sección · unidad | Qué hizo GPT | Veredicto | Por qué | v1.1 |
|---|---|---|---|---|
| §7 Palabras clave · u044 | «Seguimiento multiobjeto» → «Identidad temporal por sujeto» | **R** | Lo no ejercido son las **métricas** MOT, no el seguimiento: el tracker existe y su aporte se mide (F1 0,930 por sujeto vs 0,789 por escena, §18.1). §15.3 y §16.4 usan «seguimiento multiobjeto». Una palabra clave debe ser buscable. Alternativa si molesta MOT: «Seguimiento temporal de personas» | c36 |
| §12.1 ¶2 · u053 | **Ya aceptado sin marca.** «aborda esta necesidad mediante el estudio, diseño, implementación y evaluación...»; la lista de campos quedó con 4 en vez de 5 | edición propia | Se cayó «seguridad laboral», el dominio del trabajo | repuesto; c42 |
| §12.1 ¶3 · u054 | **Ya aceptado sin marca.** «Los detectores de vocabulario cerrado reconocen... "persona sin casco" no equivale a localizar una persona y un casco» | — | Buen párrafo puente: introduce el problema de a poco | sin cambios |
| §12.1 ¶4 · u055 | Quita «imágenes de referencia»; explica cómo se articulan consultas, estrategias y reglas; «registrar y distribuir alertas» | **R+** | El colega tiene razón (c16). Se conserva el original, se quita «imágenes de referencia», se agrega la advertencia de GPT («una consulta válida no garantiza una detección correcta»), presente y sin «y académica» | c43 |
| §12.2 ¶1 · u057 | Sustituye el planteo del problema (riesgos abiertos vs. vocabularios cerrados) por la pregunta de ingeniería | **R+** | Primero el problema del dominio, después la pregunta. Se toma la pregunta de GPT como cierre del párrafo y «estática» pasa a «vocabulario fijo» | c44 |
| §12.2 ¶2 · u058 | Reescribe las tres consecuencias con más cautela (la extensibilidad no elimina el costo de validar) | **AC** | El fondo mejora (§16.3, §18.2); se repone «relevante para la seguridad», el costo en datos y recursos, y la enumeración en tres pasos | c45 |
| §12.2 ¶3 · u059 | Comprime la dimensión operativa y agrega «no se evalúa la reducción de la carga cognitiva...» | **R** | La fatiga y la atención sostenida son motivación legítima; la advertencia es un límite y va a §12.4 | c46; frase movida a u068 (c52) |
| §12.3 ¶1 · u062 | Hipótesis reescrita como espejo de §18.1 | **R+** | Ver §3.3. Se conserva la original con tres retoques: «sin ajustar los pesos del modelo» (premisa desde el inicio, §17.1.9), sale «maquinaria cerca de peatones», entra «no presupone que un detector open-vocabulary supere a un detector supervisado» | c47 |
| §12.3 ¶2 · u063 | Nueva lista de dimensiones; pierde «presupuesto de latencia» (→ «instrumentación de latencia») y «arquitectura de streaming»; agrega frase metodológica | **AC** | Se reponen presupuesto de latencia (§17.1.7, §18.4) y arquitectura de transporte de video (§15.4, §17.3.5); se quita la frase final, que es §12.5 | c48 |
| §12.3 ¶3 · u064 | Cadena con planos, jerarquía de evidencia de §17.5, sin «utilidad operativa» ni «condiciones controladas» | **AC** | Se conservan la distribución en la cadena y la baja de «utilidad operativa»; se quitan los planos y «representa a la plataforma completa»; se repone «bajo condiciones controladas y reproducibles»; los tres niveles quedan nombrados en una frase | c49 |
| §12.3 ¶4 · u065 | Rama de ajuste fino como rama comparativa con criterios previos | **AC** | Correcto; se repone la condición «por datos y protocolo» (ADR-017, §17.1.9), única pérdida | c50 |
| §12.4 ¶1 · u067 | Núcleo CR-01/CR-02; resto como catálogo | **A** | Es AJ-0.01 (§17.1.2.1, §18.6) | c51 |
| §12.4 ¶2 · u068 | (sin cambio de GPT) | — | Recibe la frase movida desde u059 | c52 |
| §12.4 ¶3 · u069 | Identidad temporal sin biometría; «se implementó e integró la distribución... con registro de sus resultados de entrega» | **AC** | Contenido correcto (AJ-0.01, ADR-016); voz a presente; sale el detalle del registro | c53 |
| §12.4 ¶4 · u070 | DBE/EBE; rodaje vs «estrato de obra real»; «el funcionamiento en vivo no equivale al cumplimiento del presupuesto de latencia» | **AC** | Escenarios y separación rodaje/obra real se conservan; sale la conclusión de §18.4 y la palabra «estrato» | c54 |
| §12.4 ¶5 · u071 | Presente; entrenamiento desde cero fuera de alcance | **A** | Voz del informe | c55 |
| §12.5 ¶3 · u075 | Mapa de lectura actualizado (§17.3–§17.5); pierde «identificar dificultades, discutir limitaciones y proponer líneas futuras» | **AC** | Se reponen «limitaciones y líneas de continuidad» (= §18.6) | c56 |
| §12.5 ¶4 · u076 | Cuerpo / anexos / artefactos | **A** | Coincide con §17.6 y §19; sin rutas internas | c57 |
| §13 título · u077 | «Objetivo Del Proyecto» → «Objetivos del proyecto» | **A** | Gramática. Nota: §14 sigue en Title Case («Plan De Trabajo De...»); se unifica en la integración | — |
| §13.1 · u079 | Objetivo general reescrito («sustentada en el análisis crítico...») | **R** | Ver §3.3. El original ya nombra todo lo que se hizo; GPT agrega el objetivo 1 y quita «bajo condiciones controladas» | c58 |
| §13.2 obj. 1 · u081 | Quita «normativos», «seguimiento multiobjeto», «transmisión de video» | **R** | La Etapa 1 cubrió los tres (§16.2.1, §15.3/§16.4, §15.4) y §14.2.1 los lista | c59 |
| §13.2 obj. 2 · u082 | Reduce a CR-01/CR-02; quita «niveles de severidad» | **R** | Ajusta el objetivo al resultado; la severidad existe (PR-01 alto, PR-02 medio); §18.6 ya dice que el núcleo se concretó en CR-01/CR-02 | c60 |
| §13.2 obj. 3 · u083 | Planos + distribución + propiedades de implementación; recorta componentes | **AC** | Original + «y su distribución hacia canales externos» | c61 |
| §13.2 obj. 4 · u084 | Inventario de lo construido (identidad por sujeto, orquestación e inspección); pierde «métricas operativas» | **AC** | Original + «y su distribución» | c62 |
| §13.2 obj. 5 · u085 | Quita «métricas de seguimiento» y «utilidad operativa»; describe §17.5 | **R** | GPT lo marca «cambio sustantivo». §18.6 declara esas dos faltas: el objetivo debe seguir nombrándolas | c63 |
| §13.2 obj. 6 y 7 | (sin cambios) | — | — | — |
| §14 completo | (sin cambios) | — | Congelado por decisión del usuario | — |

---

## 5. Glosario (Tabla 1)

### 5.1. Lo que ya venía cambiado en la v1.0 (antes del pase de GPT)

La v1.0 no es el glosario del maestro: **15 definiciones ya estaban modernizadas** sin marca (E-OVRT-VDP,
OVD, Patrón de riesgo, Condición de riesgo observable, Plano de medios, Plano de control, Latencia
end-to-end, Latencia de alerta, MOTA, IDF1, HOTA, DBE, EBE, MQTT, SDR) y las dos filas con ecuación
(t_alert-system, t_alert-notification) reemplazan una fila sin término del maestro. Son coherentes con
§17.1.7 y §17.3 y no se tocan; se anota para que nadie las atribuya a este pase.

### 5.2. Los cambios de GPT

Criterio aplicado a cada fila: **una fila se justifica si el cuerpo del informe usa el término y no lo
define donde aparece**. Conteo de apariciones en las versiones vigentes (columnas: §15–16 · §17.1 · §17.3 ·
§17.4 · §17.5 · §17.6–§19):

| Fila | Uso en el cuerpo | Veredicto |
|---|---|---|
| **Zero-shot** (redefinida) | «zero-shot» en sentido de la literatura: 17 · 12 · 1 · 0 · 0 · 5 | **AC** — la definición de GPT es sólo la operativa del proyecto y choca con el uso de §15/§16; se funden las dos (c37) |
| **CR-01 / CR-02** (nueva) | desde §16.2.2 hasta §18.6, y ahora §12.4 y §13.2 | **AC** — se agregan los códigos de patrón **PR-01/PR-02**, que §17.1.5 y §17.3.6 usan y nadie define (c39) |
| **Vocabulario canónico** (nueva) | `bare_head`: 0 · 0 · 1 · 0 · 5 · 0; `canonical_v2`: **0 en todo el informe** | **AC** — se conservan las cuatro etiquetas (AJ-0.02) y sale el identificador de configuración (c40) |
| **Evento de percepción** (nueva) | 0 · 0 · 14 · 7 · 0 · 2; `media.detection.v1` 3 veces en §17.4 | **A** |
| **Identidad temporal por sujeto** (nueva) | «identidad temporal»: 0 · 7 · 9 · 0 · 2 · 2; «por sujeto»: 0 · 1 · 5 · 4 · 6 · 7 | **A** |
| **Granularidad** (nueva) | scene/subject: §17.3 (2/3), §17.4, §17.6–19; «granularidad por sujeto/escena» en §17.5.4 y §18.1 | **A** |
| **Distribución de alertas** (nueva) | §17.3.7 completa; §17.4, §18 | **A** |
| **FAR** (nueva) | 0 · 3 · 0 · 0 · 0 · 1 | **A** — y su advertencia («una tasa derivada no establece una cota operativa») es la trampa P3 del manual |

Sobre el comentario del colega «todas las que agregó a partir de acá me parecen al vicio» (c7): con el
criterio de uso, **ninguna de las siete sobra**. La respuesta con los conteos está en c39.

### 5.3. MOTA / IDF1 / HOTA (pedido del colega: quitarlas)

Recomiendo **conservarlas** (c38). Uso: MOTA 3 · 4 · 0 · 0 · 0 · 3; IDF1 3 · 4 · 0 · 0 · 0 · 2; HOTA 4 · 4 ·
0 · 0 · 0 · 2. Están en §15.3.3 («Métricas de evaluación para MOT»), en §17.1.7 (declaradas condicionadas)
y en §18.6 («la evaluación MOT ... mantiene los límites ya expuestos»). Un lector que llega a §16 o §18
necesita la definición, y las tres filas ya dicen lo correcto («no se utilizó para evaluar el prototipo»).
Si igual se quitan, hay que definirlas en §15.3.3 en la primera aparición (criterio F6 del manual), y §15/16
está cerrada.

### 5.4. Filas que agrego (sugerencia de Claude, c41)

Mismo criterio, sobre siglas y términos que el cuerpo usa sin definir:

| Fila nueva | Uso en el cuerpo | Fuente de la definición |
|---|---|---|
| **Vocabulario activo** | 20 (0 · 8 · 6 · 1 · 2 · 3) | §17.1.5 «cuarto eje» |
| **Estrategia de detección** (E-DIR / E-IND / E-HYB) | E-IND 17, E-DIR 10, E-HYB 5 | §17.1.5 «tercer eje» |
| **G2A** | 26 (5 · 10 · 2 · 0 · 0 · 5) | Tabla 29 de §17.1.7: «dequeue → fin de inferencia»; nota «G2A = Glass-to-Algorithm» |
| **Episodio** | 127 (4 · 35 · 26 · 11 · 31 · 20) | §17.4.6 (clip_gt.v2: episodios a nivel de escena y condición) |
| **Re-alerta** | 11 (0 · 4 · 5 · 0 · 2 · 0) | §17.1.7 nota: «una re-alerta asociada al mismo episodio no es un falso positivo» |

Si el criterio es un glosario mínimo, las dos imprescindibles son **G2A** y **Estrategia de detección**:
son siglas opacas para el tribunal. Las filas se insertan después de «Latencia por tramo» (última fila
original) y antes de las de GPT, para no anidarlas en los envoltorios de Google Docs de aquéllas.

### 5.5. Filas sin uso en ninguna sección (decisión del usuario; no las toqué)

IA, CV, IoT, GStreamer, FFmpeg y «Latencia end-to-end» no aparecen en §12–§19. Son candidatas a poda si
se quiere acortar la tabla; ninguna es de GPT.

### 5.6. Siglas frecuentes que quedan sin definir (para la integración)

COCO (48), LVIS (34), GPU/CPU/VRAM/RAM, YOLOE/YOLO (48), DINO (57, por Grounding DINO), CLIP (12), ODVG
(14), OAK-D (11), NMS (5), AP50 (10), CHV/SHEL5K/MOCS (nombres de datasets). Son o nombres propios o
siglas que el texto define en su primera aparición (criterio F6). No agregué filas por ellas.

---

## 6. Los comentarios

### 6.1. Los siete del colega

| Hilo | Sobre | Dice | Mi posición |
|---|---|---|---|
| c1 (respuesta a c0) | palabra clave | «ver» | R a GPT: conservar «Seguimiento multiobjeto» (c36) |
| c3 (respuesta a c2) | Zero-shot | «ver» | AC: fundir definición general y operativa (c37) |
| c4, c5, c6 | MOTA, IDF1, HOTA | «no usamos ninguna de las 3 ... Las sacaría de acá» | Conservar, por uso en §15.3.3, §17.1.7 y §18.6 (c38) |
| c7 | filas nuevas | «todas las que agregó a partir de acá me parecen al vicio» | Ninguna sobra por criterio de uso; una se retoca de fondo (c39) |
| c16 (respuesta a c15) | §12.1 u055 | «acá ya se pone a explicar lo que hace la plataforma, lo cual mucho sentido no tiene porque es una introducción» | De acuerdo; la alternativa de u055 lo resuelve (c43) |

### 6.2. Los 29 de GPT

Son justificaciones de cada cambio, bien ancladas y con remisiones que existen (§1). Tres observaciones:
c35 avisa honestamente que el objetivo 5 es un «cambio sustantivo para revisión» (lo es, y se rechaza por
lo dicho en §3.3); c9 promete no instalar «el nombre de configuración deprecado ni los códigos internos»
pero la fila trae `canonical_v2` (se retoca); c29 declara que «no se incorporan rutas ni referencias a
documentación interna en el texto propuesto», y es cierto en todo el pase: **la autocontención se
respeta** (ninguna sugerencia cita docs, ADR ni fichas).

### 6.3. Los resueltos

No hay forma de evaluarlos desde el archivo: Google Docs los elimina de la exportación. Sólo se infiere
que las sugerencias de u053 y u054 se aceptaron (§4). Si hace falta revisarlos, hay que hacerlo en el
historial de comentarios de Google Docs.

---

## 7. Dar de más / omitir — listas cerradas

**Omisiones de GPT** (todas repuestas en la v1.1):

1. «seguridad laboral» en el cruce de disciplinas (§12.1 u053, edición ya aceptada).
2. «relevante para la seguridad» y el costo en datos, anotación y recursos (§12.2 u058).
3. Presupuesto de latencia y arquitectura de transporte de video entre las dimensiones (§12.3 u063).
4. «bajo condiciones controladas y reproducibles» (§12.3 u064).
5. Condición «por datos y protocolo» de la rama de ajuste fino (§12.3 u065, ADR-017).
6. «limitaciones y líneas futuras» como salida del método (§12.5 u075).
7. Ejes normativo, seguimiento multiobjeto y transmisión de video del objetivo 1 (u081).
8. Niveles de severidad en el objetivo 2 (u082).
9. Métricas de seguimiento y utilidad operativa en el objetivo 5 (u085): su ausencia debe declararla §18.6,
   no borrarla el objetivo.
10. El planteo del problema del dominio antes de la pregunta de ingeniería (§12.2 u057).

**Excesos de GPT** (todos quitados en la v1.1):

1. Articulación interna consultas/estrategias/reglas en la motivación (§12.1 u055).
2. Planos asignados a cada eslabón y «este último nivel representa a la plataforma completa» (§12.3 u064).
3. Frase metodológica de cierre en las dimensiones de la hipótesis (§12.3 u063).
4. «con registro de sus resultados de entrega» (§12.4 u069).
5. «el funcionamiento en vivo no equivale al cumplimiento del presupuesto de latencia...» y «estrato»
   (§12.4 u070).
6. Advertencia de §18.6 sobre carga cognitiva y accidentes dentro del planteo del problema (§12.2 u059);
   se mueve a §12.4.
7. «herramientas de orquestación e inspección experimental» y «contratos explícitos, configuración
   reproducible y mecanismos de persistencia e inspección» en objetivos (u083, u084).
8. `canonical_v2` en el glosario.
9. Hipótesis y objetivo general reescritos desde §18 (u062, u079).

---

## 8. Coherencia con §14 y con el cierre

- **§14 congelado ⇒ §13 no se aleja del plan.** Los objetivos y el plan son la misma capa del documento.
  Con §14.2.5 diciendo «Registro de métricas: precisión, recall, F1, FPS, latencia» y §14.2.1 listando MOT y
  protocolos de transmisión, reescribir §13 desde el resultado deja el plan y los objetivos en
  contradicción. Por eso el veredicto de §13 es conservar y sumar sólo la distribución.
- **§18.1** responde «la hipótesis de la sección 12.3» con «afirmativa en ese alcance y condicionada». Con
  la hipótesis original retocada esa respuesta sigue teniendo sentido; con la de GPT, §18.1 respondería a
  su propia paráfrasis.
- **§18.6** balancea objetivos y declara dos incumplimientos (evaluación MOT, utilidad percibida). Sólo
  tienen referente si el objetivo 5 sigue nombrando seguimiento y utilidad operativa.
- **Fichas de la Etapa 0 que siguen pendientes** y que nadie toca por el congelamiento: **AJ-0.03** (Gantt
  vencido), **AJ-0.04** (semanas no literales; correspondencia con las fases), **AJ-0.05** (costos; el
  borrador v0.1 de §14.4 vive aparte), **AJ-0.06** (tabla etapa → sección). AJ-0.01 y AJ-0.02 quedan
  cubiertas por este pase si se aceptan u067/u069 y las filas del glosario.

---

## 9. La v1.1: cómo leerla y cómo se verificó

**Mecánica de capas.** Las sugerencias de GPT quedan intactas; rechazarlas devuelve el original de la v1.0.
Encima:

- En las unidades **AC** y **R+**, Claude **tacha la inserción de GPT** (borrado anidado dentro de la
  inserción pendiente, que es como Word representa que un revisor edita la inserción de otro) e **inserta
  su alternativa a continuación** como sugerencia propia. Aceptar todo lo del párrafo deja la alternativa
  de Claude; rechazar sólo lo de Claude deja la propuesta de GPT; rechazar todo deja el original.
- En las unidades **R**, sólo hay un comentario: basta rechazar la sugerencia de GPT.
- En las **A**, no hay marca (a veces un comentario).
- Dos ediciones sobre texto sin marca de GPT: «seguridad laboral» en §12.1 y la frase sobre carga cognitiva
  al final de §12.4 ¶2.
- En el glosario: dos celdas de GPT tachadas y reemplazadas (Zero-shot, Vocabulario canónico), una ampliada
  (CR-01/CR-02), cinco filas nuevas de Claude.
- Los 36 hilos previos se conservan con sus anclas; no se resuelve ni se borra ninguno.

**Cifras.** 68 `w:ins` / 46 `w:del` de GPT (sin cambios) · 32 `w:ins` / 26 `w:del` de Claude · 28
comentarios de Claude (ids 36–63) · 36 → 64 anclas de comentario.

**Verificación ejecutada** (`pase_secciones_iniciales_v11.py`, al final de la corrida):

- quitar sólo las marcas de Claude devuelve el documento de origen (secuencia completa de texto vivo y
  tachado, incluidas las marcas de GPT): **SÍ**;
- anclas de comentario del origen conservadas: **SÍ** (36 de 36);
- `verificar_paquete.py`: **paquete íntegro**; XML de `document.xml`, `comments.xml`,
  `commentsExtended.xml`, `[Content_Types].xml` y `document.xml.rels` parseados antes de escribir;
- conteo de tablas y de saltos de sección igual al origen;
- lectura de la vista «aceptar todo» de §12–§13 de corrido: coherente (archivo de trabajo
  `vista_aceptada_12_13.txt`).

**Lo que no se pudo probar:** la importación a Google Docs de un borrado anidado en una inserción ajena. Es
la representación estándar de Word y Google la exporta así, pero no la importé de vuelta. Si al subir el
archivo la capa se viera rara, todos los textos alternativos están en el Anexo A de este documento y cada
comentario de Claude dice el veredicto: se puede aplicar a mano.

**Trampas de esta exportación, para la memoria del set:** Google Docs envuelve cada tramo de sugerencia,
cada fila insertada y cada párrafo de celda insertado en `w:sdt` con `w:tag goog_rdk_N` (120 en este
archivo); un extractor que busque `w:tr` y `w:p` sólo como hijos directos **no ve** las filas ni las celdas
nuevas. `comments.xml` no declara el prefijo `w14` que el motor usa para `paraId`; el guion lo agrega.

---

## 10. Notas menores

- **Comillas.** GPT escribe «persona sin casco»; el maestro y mis alternativas usan comillas rectas. En las
  secciones vigentes las angulares aparecen sólo en §17.3 (8) y §15/16 (2). Se unifica en la integración.
- **Título de §13** pasa a minúsculas; **§14** sigue en Title Case («Plan De Trabajo De Proyecto
  Integrador»). Integración.
- **Palabras clave**: la última lleva el salto de sección; el cambio de GPT es de texto, no de párrafo, así
  que no hay riesgo de título fantasma.
- **Prompt visual** sigue en el glosario aunque el texto ya no la nombra como modalidad de la plataforma:
  correcto, porque §15 la trata (4 apariciones).
- El total de palabras de §12–§13 en la vista «aceptar todo» (2.205) incluye todavía las versiones de GPT
  de las unidades **R**; si el usuario las rechaza, la cifra baja unas 60 palabras.

---

## Anexo A. Textos alternativos completos de la v1.1

Se listan para poder aplicarlos a mano si hiciera falta. Cada uno reemplaza la propuesta de GPT en la
unidad indicada.

**§12.1 ¶4 (u055, R+)**
> Frente a esta limitación, los enfoques de detección de vocabulario abierto permiten formular consultas mediante lenguaje natural. Esta capacidad habilita un modo de especificación más flexible: el usuario puede definir las entidades de interés sin depender de un conjunto rígido de etiquetas preestablecidas, aunque una consulta lingüísticamente válida no garantiza por sí sola una detección correcta. Sobre esa base, el proyecto evalúa la factibilidad técnica de una plataforma que procese video, interprete consultas open-vocabulary, detecte entidades y condiciones observables, aplique criterios de persistencia temporal y genere alertas asistivas trazables.

**§12.2 ¶1 (u057, R+)**
> El problema que orienta el trabajo puede expresarse como una discontinuidad entre la naturaleza dinámica y semánticamente abierta de los riesgos en obra y el vocabulario fijo de los sistemas de detección visual closed-set. Mientras que el entorno de construcción introduce situaciones variables, dependientes del contexto y difíciles de reducir a categorías fijas, muchos sistemas de visión computacional requieren que las clases detectables hayan sido definidas, anotadas y entrenadas previamente. De ahí la pregunta que orienta el desarrollo: cómo transformar condiciones de riesgo expresadas en lenguaje natural en alertas trazables sobre un flujo de video, y con qué desempeño y limitaciones puede sostenerse esa transformación.

**§12.2 ¶2 (u058, AC)**
> Esta problemática tiene consecuencias prácticas. En primer lugar, una condición no contemplada por un detector de vocabulario cerrado queda fuera de su capacidad de detección aunque sea relevante para la seguridad, e incorporarla exige recolectar datos, anotar y adaptar el modelo, con un costo en tiempo y recursos. En segundo lugar, en un enfoque open-vocabulary, incorporar o reformular una consulta no elimina la necesidad de validar sus detecciones ni las asociaciones que sustentan la condición de riesgo. En tercer lugar, la detección por fotograma aislado no representa por sí sola situaciones que dependen de duración o reiteración; el análisis de video requiere mecanismos de persistencia temporal y criterios explícitos para distinguir evidencia aislada de episodios que justifican una alerta.

**§12.3 ¶1 (u062, R+)**
> La hipótesis de trabajo sostiene que los modelos de detección open-vocabulary, al permitir expresar condiciones de interés mediante lenguaje natural en tiempo de inferencia y sin ajustar los pesos del modelo, constituyen un habilitador tecnológico viable para superar parte de la rigidez de los sistemas closed-set en el monitoreo visual de seguridad en construcción. Bajo esta hipótesis, una plataforma experimental podría recibir consultas o patrones como "persona sin casco" o "persona sin chaleco reflectivo" y transformarlos en alertas evaluables dentro de un flujo de video. La hipótesis no presupone que un detector open-vocabulary supere a un detector supervisado ni que la plataforma resulte apta para cualquier escenario de obra.

**§12.3 ¶2 (u063, AC)**
> Sin embargo, esta hipótesis se formula de manera condicionada. La viabilidad no depende únicamente de detectar objetos en imágenes estáticas, sino de integrar la selección de modelos visión-lenguaje, la formulación de consultas, la asociación de evidencia, la estabilidad temporal, los datos de evaluación, el rendimiento en el hardware disponible, la arquitectura de transporte de video, el presupuesto de latencia, la trazabilidad de eventos y las salvaguardas de privacidad en el tratamiento de video en contextos laborales.

**§12.3 ¶3 (u064, AC)**
> Por este motivo, el proyecto se estructura como una plataforma experimental y no como un producto industrial terminado. El objetivo es construir un prototipo que permita evaluar el comportamiento del enfoque bajo condiciones controladas y reproducibles. La solución se organiza alrededor de una cadena operativa mínima: ingesta o lectura de video, inferencia open-vocabulary, seguimiento temporal, evaluación de patrones de riesgo, registro de alertas y su distribución. Esta cadena permite analizar no sólo la precisión de detección, sino también la oportunidad y la estabilidad de las alertas generadas, en tres niveles de evidencia: la percepción por imagen, el estado por persona y la alerta por episodio.

**§12.3 ¶4 (u065, AC)**
> La propuesta incluye una rama comparativa de ajuste fino al dominio, separada del núcleo sin ajuste de pesos y condicionada a la disponibilidad de datos y a la integridad del protocolo de comparación. Esta rama contrasta variantes adaptadas con una línea base sobre un banco común y considera tanto la ganancia en el dominio como la retención de capacidad open-vocabulary, mediante criterios de adopción definidos antes de la evaluación. La adaptación no se presupone beneficiosa ni se establece como requisito para construir la plataforma; su valor se determina a partir de la evidencia experimental.

**§12.4 ¶2 (u068, frase agregada al final)**
> El trabajo tampoco evalúa el efecto del sistema sobre la carga cognitiva del supervisor ni sobre la incidencia de accidentes; esos beneficios potenciales no forman parte de sus resultados.

**§12.4 ¶3 (u069, AC)**
> El prototipo no realiza reconocimiento de identidad personal ni asocia individuos a nombres, credenciales o perfiles. La identidad temporal por sujeto mantiene estados independientes por persona durante una secuencia, sin identificación biométrica. La plataforma incluye además la distribución de alertas confirmadas hacia un canal externo mediante MQTT. Permanecen fuera de alcance la integración completa con sistemas externos de gestión de seguridad, los canales adicionales de notificación y la activación de infraestructura física de alarmas.

**§12.4 ¶4 (u070, AC)**
> La evaluación distingue dos escenarios complementarios: el Escenario A o DBE, evaluación diferida y reproducible sobre archivos, y el Escenario B o EBE, evaluación en vivo con captura continua e intercambio de eventos entre componentes. El material de video comprende un rodaje controlado y material de obra real, cuyos resultados se interpretan por separado. La procedencia, la referencia humana y las condiciones de observabilidad de los datos delimitan qué conclusiones pueden sostenerse en cada escenario.

**§12.5 ¶3 (u075, AC)**
> El diseño arquitectónico define los módulos, los flujos de datos, los contratos de interfaz y la separación entre el plano de medios, el plano de control y la distribución de alertas. La implementación materializa esas decisiones en un prototipo reproducible e incorpora el soporte experimental y los bancos de evaluación. La evaluación experimental mide percepción, estado por persona, alertas por episodio y rendimiento de ejecución; el análisis de esos resultados delimita el alcance de la factibilidad, sus limitaciones y las líneas de continuidad.

**§13.2 objetivo 3 (u083, AC)**
> Diseñar una arquitectura modular de procesamiento de video en tiempo real que distinga el plano de medios y el plano de control, permitiendo integrar de manera desacoplada componentes de ingesta, inferencia, seguimiento temporal, evaluación de patrones, registro de eventos, generación de alertas y su distribución hacia canales externos.

**§13.2 objetivo 4 (u084, AC)**
> Implementar un prototipo experimental capaz de ejecutar el flujo experimental previsto, incorporando ingesta o lectura de video, inferencia open-vocabulary, evaluación de patrones de riesgo, registro de eventos, alertas internas y su distribución, e instrumentación de métricas técnicas y operativas.

**Glosario · Zero-shot (AC)**
> Modalidad de inferencia en la que el modelo reconoce conceptos que no fueron objeto de un entrenamiento supervisado específico. En este trabajo designa el uso de modelos preentrenados sin ajuste de pesos con datos del dominio; la selección de consultas, umbrales y resolución es calibración operativa, no entrenamiento.

**Glosario · CR-01 / CR-02 (AC)**
> Condiciones nucleares de evaluación: persona sin casco (CR-01) y persona sin chaleco reflectivo (CR-02). Los patrones que las operacionalizan se identifican como PR-01 y PR-02.

**Glosario · Vocabulario canónico (AC)**
> Conjunto de etiquetas de evidencia perceptiva compartido por los componentes de la plataforma: person, helmet, vest y bare_head. Una etiqueta expresa lo que el detector localiza y no equivale a una alerta.

**Glosario · filas nuevas de Claude**
> **Vocabulario activo** — Conjunto de consultas (prompts) simultáneamente activas en una corrida. Su composición condiciona el desempeño del detector, por lo que se declara en cada configuración.
> **Estrategia de detección** — Forma de formular una condición ante el detector. La estrategia directa (E-DIR) describe la condición completa en un prompt; la indirecta (E-IND) consulta las entidades por separado y reconstruye la condición con reglas de asociación externas al modelo; la híbrida (E-HYB) combina ambas bajo una regla explícita.
> **G2A** — Glass-to-Algorithm. Latencia entre el dequeue de la unidad visual y la disponibilidad del resultado de inferencia. No incluye la captura ni el transporte hasta el host, que se informan aparte cuando la fuente aporta una marca de tiempo confiable.
> **Episodio** — Unidad de la evaluación temporal: intervalo anotado por la referencia humana durante el cual una condición de riesgo está presente en un clip. Las alertas se juzgan por episodio, no por cuadro.
> **Re-alerta** — Nueva confirmación de un patrón sobre el mismo episodio después de su resolución. Se contabiliza por separado y no se computa como falsa alerta.
