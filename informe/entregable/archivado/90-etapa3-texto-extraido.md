# 90 — Texto extraído del documento de trabajo: §17.3 Diseño Arquitectónico (v1.12, bajada del 2026-09-08; contenido idéntico a la v1.11, sólo cambió el número. Limpia, sin comentarios. ETAPA 3 CERRADA)

> **Extracción derivada (2026-09-08)** del `.docx`
> `informe/entregable/E-OVRT-VDP_Seccion_17.3_Diseno_Arquitectonico_v1.12.docx`, **solo para búsqueda y cita**
> (mismo estatuto que el doc 90): al editar, se edita el `.docx`/Google Docs, nunca
> este archivo. Tablas y figuras pueden haber perdido formato; las figuras no se
> extraen y las ecuaciones no se convierten — quedan `⟦FIGURA: no extraída — ver el .docx⟧` y
> `⟦ECUACIÓN: no extraída — ver el .docx⟧` donde estaban. Regenerado con
> `herramientas/extraer_informe.py` (regla D-C del manual de aplicación).

---

#### 17.3.1. Propósito y pregunta rectora

El diseño arquitectónico transforma el alcance metodológico, el catálogo de condiciones de riesgo, los escenarios de evaluación, el marco de métricas y los lineamientos ético-legales ya consolidados en una organización técnica capaz de orientar la implementación del prototipo. Esos insumos operan como restricciones, de modo que cada módulo, frontera y flujo del capítulo se derive de una decisión metodológica previa y no de una preferencia técnica aislada.

La plataforma se estructura alrededor de la separación entre el procesamiento visual en tiempo real y la lógica de interpretación posterior, fundamentada en la sección 16.5.3. El plano de medios, la ruta de datos de la sección 16.5.3, produce evidencia perceptiva, y el plano de control, su ruta de control, la interpreta. Esa división protege la ruta crítica de video y sostiene la trazabilidad experimental necesaria para analizar cada corrida.

La pregunta que orienta el capítulo es qué arquitectura permite materializar una plataforma experimental de detección open-vocabulary sobre video en tiempo real conservando modularidad, desacoplamiento, trazabilidad y evaluabilidad dentro del alcance ya definido. El capítulo la responde fijando las responsabilidades de los componentes, los flujos de información, las fronteras entre módulos, los contratos versionados, las interfaces de gobierno y transporte, los escenarios experimentales y los criterios de observabilidad que acompañan la implementación.

#### 17.3.2. Alcance, capacidades y decisiones arquitectónicas

El diseño se formula para un prototipo experimental ejecutado en un entorno local y controlado, y orienta la implementación, la medición y la reconstrucción de resultados sin asumir responsabilidades propias de una solución productiva. Sobre el núcleo validable la plataforma demuestra un flujo completo, medible y trazable desde una fuente visual hasta una alerta asistiva registrada. El objetivo no es ampliar la cantidad de condiciones cubiertas, sino asegurar una base capaz de procesar evidencia visual, publicar eventos, evaluar patrones, registrar alertas y reconstruir resultados experimentales.

El núcleo comprende las capacidades necesarias para operar sobre fuentes controladas, ejecutar inferencia open-vocabulary, versionar prompts, normalizar detecciones, aplicar reglas temporales simples, registrar eventos y producir métricas comparables. El seguimiento multiobjeto formal, las reglas espaciales, las zonas parametrizadas, la preselección liviana en el borde y la adaptación al dominio quedan previstas como extensiones condicionadas que no desplazan la validación inicial ni agregan dependencias al flujo base. La gestión de prompts pertenece al núcleo porque en una plataforma open-vocabulary cada resultado se atribuye a una formulación, una estrategia de detección y un vocabulario activo registrados.

##### 17.3.2.1. Capacidades arquitectónicas requeridas

La arquitectura habilita un conjunto mínimo de capacidades que permiten desarrollar un prototipo medible, trazable y extensible. La enumeración reúne responsabilidades del diseño y no componentes de implementación.

La Tabla 39 declara el régimen de cada capacidad mediante cinco compromisos, cuyo alcance precisa la nota.

**Tabla 39**

*Capacidades arquitectónicas y su tratamiento en el diseño*

| **Capacidad requerida** | **Compromiso** | **Lectura de diseño** |
| --- | --- | --- |
| Gestión y gobierno de la corrida | Núcleo | Debe existir un punto explícito para declarar y congelar la configuración efectiva de cada ejecución, gobernar su ciclo de vida —creación, consulta, cancelación y cierre— y ordenar el disparo entre módulos. |
| Operación sobre fuentes reproducibles | Núcleo | Debe operar sobre imágenes, datasets o videos locales cuya lectura pueda regularse, repetirse y detenerse sin alterar el contenido. Este escenario estabiliza inferencia, contratos, eventos y métricas antes de incorporar captura continua. |
| Operación sobre fuentes en vivo | Complementario previsto | Debe admitir captura o streaming en entorno controlado, donde la fuente continúa evolucionando aunque el procesamiento no sostenga la cadencia, para observar el comportamiento operativo del sistema. |
| Normalización de entrada visual | Núcleo | Cada frame debe incluir metadatos de corrida, fuente, orden temporal, resolución y política de muestreo, para compartir el pipeline sin ocultar las diferencias temporales entre fuentes. |
| Inferencia OVD configurable | Núcleo | Debe integrar modelos OVD mediante adaptadores, de modo que puedan sustituirse o compararse sin rediseñar la cadena. |
| Gestión de prompts y vocabulario activo | Núcleo | Debe versionar formulaciones, aliases, estrategias de detección, vocabulario activo y umbrales asociados. |
| Normalización de detecciones | Núcleo | La salida del plano de medios debe expresarse como un contrato de evento de percepción versionado, única unidad de evidencia compartida para interpretar patrones, persistir y releer corridas. |
| Evaluación de patrones de Nivel 1 | Núcleo | Las detecciones positivas deben asociarse espacialmente por sujeto, convertirse en un estado evaluable de ausencia y estabilizarse mediante persistencia temporal e histéresis. |
| Registro de alertas asistivas | Núcleo | Las alertas deben registrarse al confirmarse un patrón, sin constituir un juicio normativo automático. |
| Publicación y persistencia de eventos | Núcleo | La publicación debe desacoplar productores y consumidores sin bloquear la ruta crítica; la persistencia debe conservar un historial de sólo adición que sobreviva a la corrida y permita su relectura. |
| Observabilidad y métricas | Núcleo | La instrumentación debe integrarse al pipeline: cada tramo emite sus mediciones, sin reconstruirlas después desde artefactos que no las registraron. |
| Reporte experimental | Núcleo | Cada corrida debe persistir una síntesis de configuración, resultados y limitaciones, legible sin acceso al sistema en ejecución. |
| Inspección mínima de resultados | Núcleo | Debe ofrecer una interfaz acotada para revisar corridas, alertas, métricas y evidencia, sin convertirse en un tablero operativo. |
| Gestión de evidencia visual controlada | Complementario previsto | Debe admitir clips, snapshots o recortes justificados para validación, revisión técnica o comunicación académica. |
| Distribución de alertas confirmadas | Capacidad opcional | Debe convertir alertas confirmadas en intentos de entrega registrados, después del registro interno y fuera del razonamiento del patrón, para que una falla externa no se propague al motor de patrones. |
| Preselección liviana en el rol de captura | Capacidad opcional | Debe reducir carga antes de la inferencia con un preselector conservador: ante falla o incertidumbre, la unidad continúa por el flujo principal; el borde no es fuente de verdad y todo descarte queda visible. |
| Identidad temporal de sujeto | Capacidad opcional | Debe admitir granularidad por sujeto mediante identidad temporal válida. Las métricas formales de seguimiento multiobjeto no condicionan la evaluación del núcleo ni deben confundirse con la capacidad de mantener identidad. |
| Capacidades contextuales y relacionales | Extensión condicionada | Debe prever contexto, razonamiento espacial, zonas, proximidad y evaluadores relacionales para las condiciones de Nivel 2 y Nivel 3, sin bloquear CR-01 y CR-02. Su habilitación exige evidencia e instrumentación adecuadas. |
| Adaptación al dominio (fine-tuning) | Rama comparativa condicionada | Sólo corresponde con una línea base preentrenada congelada, datos suficientes, partición disjunta y criterios de escalamiento fijados antes de los resultados. |

**Nota.** El compromiso declara el régimen de cada capacidad. «Núcleo» identifica las capacidades necesarias para el flujo base. «Complementario previsto» agrupa las útiles para la validación, la revisión técnica o la comunicación académica. «Capacidad opcional» identifica las que el diseño contempla pero se declaran en la configuración de cada corrida y permanecen deshabilitadas por defecto, de modo que ninguna opere como comportamiento implícito. «Extensión condicionada» identifica las que exigen evidencia e instrumentación adicionales. «Rama comparativa condicionada» refiere a variantes que sólo se incorporan si se cumplen las condiciones metodológicas correspondientes.

##### 17.3.2.2. Requisitos no funcionales de referencia

Las cualidades no funcionales condicionan la validez experimental del prototipo. No alcanza con detectar una condición de riesgo si el sistema no registra la configuración de la corrida, no mide latencia, no conserva trazabilidad o no controla la evidencia visual generada. La Tabla 40 reúne las cualidades que el diseño trata como condiciones arquitectónicas y no como aspiraciones.

**Tabla 40**

*Requisitos no funcionales de referencia*

| **Dimensión** | **Requisito de diseño** | **Implicación arquitectónica** |
| --- | --- | --- |
| Latencia | Acotar la ruta crítica desde la lectura o captura hasta la publicación de eventos de percepción. | El plano de medios no debe depender de reportes, inspección, persistencia pesada ni notificaciones externas para continuar procesando frames. |
| Reproducibilidad | Registrar la configuración efectiva de cada corrida. | Cada ejecución debe conservar fuente, modelo, prompts, umbrales, entorno, versiones y políticas de muestreo. |
| Modularidad | Permitir la sustitución de fuentes, modelos, prompts, postproceso y motor de patrones. | Los componentes deben comunicarse mediante contratos explícitos y no mediante estructuras internas acopladas. |
| Trazabilidad | Reconstruir una alerta a partir de configuración, detecciones, patrón, métricas y evidencia asociada. | Los eventos, identificadores y relaciones causales deben conservar información suficiente para revisión posterior. |
| Integridad de eventos | Evitar pérdida, duplicación o ambigüedad en eventos relevantes. | Los eventos deben incluir identificadores, versión de esquema, orden lógico y asociación con la corrida correspondiente. |
| Privacidad y minimización | Proteger configuraciones, métricas, eventos y artefactos visuales conservados. | La trazabilidad ordinaria debe apoyarse en eventos y metadatos; los artefactos visuales sólo deben conservarse cuando estén justificados. |
| Observabilidad | Medir tiempos, FPS, errores, descartes y uso de recursos desde las primeras corridas. | La instrumentación debe formar parte del diseño del pipeline y no quedar como una actividad posterior. |
| Robustez experimental | Registrar fallas y anomalías sin ocultar su impacto sobre la corrida. | Los errores de fuente, inferencia, publicación, persistencia o medición deben producir registros interpretables. |

**Nota.** Los requisitos no funcionales expresan las cualidades necesarias para preservar la validez experimental del prototipo y aseguran comparabilidad entre corridas, trazabilidad de resultados y control de las decisiones que afectan la latencia, la privacidad, la reproducibilidad o la observabilidad.

##### 17.3.2.3. Decisiones arquitectónicas y principios de lectura

Las decisiones arquitectónicas iniciales no fijan tecnologías concretas y establecen reglas estructurales que se preservan durante el desarrollo del prototipo. La Tabla 41 las reúne alrededor de cuatro ejes. La **separación entre ruta crítica y lógica de control** mantiene la inferencia y la publicación de evidencia perceptiva desacopladas de la evaluación de patrones, la persistencia, los reportes y las notificaciones externas (DA-01, DA-02). La **modularidad por contratos** hace que fuentes, modelos, prompts, detecciones, patrones y métricas se intercambien mediante estructuras explícitas, sin dependencias internas que dificulten la sustitución o la evaluación comparativa (DA-05, DA-12). La **trazabilidad experimental** permite reconstruir toda alerta a partir de la configuración de corrida, los eventos de percepción, el patrón evaluado y las métricas registradas (DA-03, DA-04, DA-13). La **medición desde el diseño** instrumenta tiempos, cadencia efectiva, descartes, errores y estados de patrón desde las primeras corridas, porque forman parte de la validez experimental.

**Tabla 41**

*Decisiones arquitectónicas iniciales*

| **ID** | **Decisión** | **Justificación** |
| --- | --- | --- |
| DA-01 | Separar plano de medios y plano de control. | Protege la ruta crítica de video y desacopla la inferencia de la lógica de interpretación. |
| DA-02 | Publicar evidencia perceptiva como eventos de percepción normalizados. | Permite desacoplar detecciones, patrones, métricas, alertas y persistencia. |
| DA-03 | Separar el gobierno de las corridas, el transporte de eventos durante la ejecución y el repositorio persistente de hechos. | Cada preocupación tiene un régimen propio, porque el gobierno es puntual y de solicitud y respuesta, el transporte es continuo y no debe bloquear la ruta crítica, y la persistencia sobrevive a la corrida para habilitar su relectura. |
| DA-04 | Confirmar patrones mediante persistencia temporal e histéresis. | Reduce alertas generadas por detecciones aisladas, inestables o de corta duración. |
| DA-05 | Integrar modelos OVD mediante adaptadores. | Permite comparar modelos o variantes sin rediseñar la arquitectura general. |
| DA-06 | Admitir granularidad por sujeto mediante identidad temporal opcional, sin convertir las métricas MOT en requisito del núcleo. | Permite evaluar persistencia por persona cuando existe identidad válida y conserva la granularidad de escena como configuración independiente. |
| DA-07 | Tratar la adaptación al dominio como rama comparativa separada y condicionada por datos y protocolo. | Preserva una línea base zero-shot congelada y evita mezclar resultados de una variante ajustada con el núcleo sin entrenamiento. |
| DA-08 | Adoptar minimización visual como criterio ordinario de trazabilidad. | Evita que el almacenamiento indiscriminado de video crudo sea parte del comportamiento base. |
| DA-09 | Separar trazabilidad ordinaria de evidencia visual controlada. | Permite conservar clips, capturas o recortes sólo cuando estén justificados por validación, revisión técnica o comunicación académica. |
| DA-10 | Priorizar DBE antes de EBE. | Estabiliza contratos, inferencia, eventos y métricas antes de incorporar captura continua. |
| DA-11 | Permitir preselección liviana en el rol de captura como variante opcional, conservadora, deshabilitada por defecto y fail-open. | La variante puede reducir carga sin transformar el borde en fuente de verdad ni ocultar descartes, porque el flujo base continúa disponible y comparable. |
| DA-12 | Versionar prompts y vocabulario activo por corrida. | Garantiza la reproducibilidad y comparación entre formulaciones. |
| DA-13 | Registrar toda alerta interna antes de aplicar políticas de supresión o entrega externa. | Preserva la semántica y la medición del episodio; el cooldown, la limitación de tasa y la idempotencia pertenecen al tramo de distribución. |

**Nota.** Las decisiones fijan reglas estructurales adoptadas para el diseño del prototipo experimental. Su materialización y su verificación se documentan en conjunto en la sección 17.4.

A esos cuatro ejes se suma un criterio transversal de **evolución incremental**, por el cual las capacidades condicionadas (DA-06, DA-07, DA-11) se incorporan sin desplazar el núcleo ni convertirse en dependencias del flujo base.

#### 17.3.3. Vista general y patrones de acople

La plataforma se organiza como una arquitectura lógica por bloques que procesa fuentes de video, genera evidencia perceptiva, evalúa patrones de riesgo y conserva resultados reconstruibles. La vista separa responsabilidades y no prescribe una distribución obligatoria en procesos, servicios o nodos físicos.

El flujo principal parte de fuentes visuales externas, como datasets, videos locales, cámaras o flujos de streaming, y entra al plano de medios por el adaptador de ingesta visual, que encapsula los distintos orígenes bajo una representación común. Desde ese punto se concentra la ruta crítica, que va de la lectura o la captura hasta la publicación de evidencia perceptiva normalizada. El plano no depende de tareas posteriores para continuar procesando unidades visuales. La configuración experimental atraviesa ese flujo y define las condiciones de cada corrida, entre ellas el escenario, el modelo, los prompts activos, los umbrales, las políticas de evidencia y los parámetros de ejecución, sin intervenir en el procesamiento frame a frame.

A partir de los eventos publicados, el plano de control evalúa patrones, administra estados de corrida y registra alertas asistivas internas cuando confirma una condición de riesgo. Las alertas confirmadas viajan por un bus dedicado hacia el módulo de distribución. El ciclo de vida de los tres módulos se gobierna mediante interfaces independientes, que la interfaz de inspección y el orquestador experimental utilizan sin consumir los buses.

La trazabilidad, la observabilidad y la inspección se agrupan en el bloque de soporte experimental, que es una capacidad transversal y no una etapa del flujo frame a frame. Ese bloque conserva evidencia reconstruible, consolida telemetría técnica y permite revisar corridas, métricas, alertas y resultados sin interferir con la ruta crítica. La Figura 4.1 presenta esa organización en una vista lógica de alto nivel. Las flechas sólidas representan el flujo principal de datos y eventos, y las punteadas, la influencia de la configuración o las capacidades de soporte.

**Figura 4.1**

*Vista conceptual de la arquitectura E-OVRT-VDP*⟦FIGURA: no extraída — ver el .docx⟧

La vista se materializa mediante dos patrones de acople complementarios. El gobierno de las corridas ocurre por interfaces HTTP gobernadas por configuración en los tres módulos ejecutables. Se adopta HTTP porque el ciclo de vida de una corrida, que abarca crear, consultar, cancelar y cerrar, tiene semántica de solicitud y respuesta, admite múltiples clientes sin acoplarlos entre sí y permite disponer los módulos en un mismo host o en hosts distintos sin modificar su lógica. El gobierno por configuración obliga a que cada corrida declare sus parámetros en lugar de heredarlos de constantes ocultas.

El intercambio de datos en ejecución ocurre mediante un bus ZeroMQ con patrón publicador-suscriptor (PUB/SUB) y serialización binaria msgpack, con un canal de detecciones entre los planos y un canal de alertas hacia la distribución. Se adopta ZeroMQ porque ofrece transporte de baja latencia sin requerir un broker como dependencia adicional del prototipo, y porque el patrón publicador-suscriptor desacopla al productor de sus consumidores sin bloquear la ruta crítica. msgpack reduce el costo de serialización respecto del texto plano y conserva estructuras autodescriptivas.

La durabilidad no se le exige al canal. Cada hecho se persiste en archivos JSONL de sólo adición antes de publicarse, de modo que la evidencia se pueda releer y reevaluar sin depender de la mensajería. El gobierno fija la configuración y el ciclo de vida, el bus transporta los hechos de ejecución y la persistencia sostiene la relectura sin constituir un tercer patrón de acople.

Esta organización mantiene separados, y coordinados por contratos explícitos, el procesamiento de video, la interpretación de patrones, la distribución de alertas y el análisis experimental.

#### 17.3.4. Configuración experimental, vocabulario y estrategia del núcleo

La configuración experimental concentra las decisiones que gobiernan una corrida y declara de manera explícita y reproducible el escenario, la fuente visual, el modelo OVD, los prompts activos, los umbrales, la política de muestreo, los módulos habilitados, los criterios de patrón, la política de evidencia y la instrumentación de métricas. Al fijarlas antes de la ejecución, separa la definición de las condiciones del procesamiento efectivo de frames y eventos, y permite que cada detección, transición de patrón, alerta interna, métrica o evidencia conservada se asocie con una configuración efectiva de corrida.

Esa separación protege la ruta crítica, porque el pipeline dispone de la configuración efectiva sin consultas externas bloqueantes para decidir qué modelo ejecuta, qué prompts utiliza o qué política de muestreo aplica. También delimita la interpretación posterior de los resultados, ya que una detección sólo resulta experimentalmente útil si puede relacionarse con su fuente, modelo, prompt, umbral, postproceso y patrón evaluado. Sin esa asociación no es posible atribuir diferencias de desempeño a una variable concreta de la corrida.

El gobierno se sostiene sólo si la configuración se resuelve y se valida antes de iniciar la ejecución, de manera que una corrida con declaración incompleta falle al crearse y no produzca artefactos que no puedan atribuirse a una configuración declarada. La configuración alcanza a tres destinatarios. El plano de medios recibe los parámetros que aplica sin diseñarlos ni versionarlos, el plano de control recibe los criterios con los que evalúa y el soporte experimental la utiliza como clave de reconstrucción, de modo que todo evento, métrica, alerta o evidencia conservada pueda rastrearse hasta la corrida que le dio origen.

##### 17.3.4.1. Configuración de corrida como artefacto de reproducibilidad

La configuración de corrida se materializa como un manifiesto de experimento que referencia y congela las configuraciones efectivas de cada componente. El plano de medios, el plano de control y el tramo de distribución tienen ciclos de vida y destinatarios distintos, y una configuración monolítica no tendría un único consumidor ni permitiría reconstruir con precisión qué versión recibió cada servicio.

Se denomina ejecución experimental a la unidad lógica que agrupa las ejecuciones independientes de los componentes que participan en una misma instancia del experimento. Esa unidad se identifica mediante un identificador de experimento (*experiment_id*), mientras que cada componente conserva su propio identificador de corrida. La separación entre ambos niveles permite correlacionar configuraciones, eventos, métricas, alertas, entregas y artefactos bajo una clave común, sin imponer un ciclo de vida único ni una configuración monolítica a los servicios participantes.

El manifiesto declara un *experiment_id*, las referencias a las configuraciones de cada plano, el orden de disparo y los artefactos congelados, entre ellos el modelo, el conjunto de prompts, el conjunto de patrones y la política de distribución. Dos corridas sólo son comparables cuando se conoce qué variable cambió y cuáles permanecieron constantes. La Tabla 42 reúne los elementos mínimos de ese gobierno reproducible.

**Tabla 42**

*Elementos mínimos de la configuración experimental*

| **Elemento configurable** | **Contenido esperado** | **Función arquitectónica** |
| --- | --- | --- |
| Manifiesto de experimento | Versión del manifiesto, fecha, objetivo y referencias a las configuraciones efectivas del plano de medios, del plano de control y del módulo de distribución cuando se habilita. | Gobierna una ejecución experimental sin imponer una configuración monolítica a servicios con ciclos de vida independientes. |
| Identificador de experimento | experiment_id, junto con los identificadores de corrida de cada componente. | Vincula eventos, métricas, errores, alertas, entregas y artefactos de todos los componentes bajo una clave común. |
| Escenario y fuente visual | DBE o EBE; dataset, video local, imagen, cámara o stream; naturaleza temporal; resolución, ritmo esperado, duración y restricciones conocidas. | Distingue fuentes reproducibles, fuentes temporales y fuentes en vivo sin confundir escenario con topología física. |
| Parámetros del pipeline | Resolución de procesamiento, selección o muestreo, criterios de omisión o descarte, tamaño de cola, ritmo esperado y calentamiento. | Condiciona latencia, cobertura temporal, unidades procesadas y lectura de descartes. |
| Modelo OVD | Modelo, versión, checkpoint, backend, precisión numérica, dispositivo y adaptador. | Permite sustituir o comparar modelos sin acoplar el resto de la arquitectura. |
| Prompts y vocabulario activo | Conjunto versionado, condición asociada, rol de cada clase, estrategia de formulación y umbral vinculado. | Garantiza trazabilidad entre consulta textual, evidencia producida y configuración. |
| Umbrales y postproceso | Confianza mínima, IoU/NMS, filtros por clase, tamaño, región y normalización de coordenadas. | Define qué salidas crudas se transforman en evidencia perceptiva normalizada. |
| Patrones activos | Condición, severidad, granularidad scene\|subject, ventana de confirmación, histéresis de resolución y criterio de evidencia. | Transforma evidencia puntual en estados y alertas internas por episodio. El cooldown no integra este contrato. |
| Capacidades habilitadas y evidencia | Identidad de sujeto, zonas, preselección en borde, inspección, distribución y política de evidencia visual. | Evita capacidades implícitas y preserva la comparabilidad entre corridas. |
| Política de distribución | Canal, calidad de servicio, idempotencia, supresión de re-notificación, limitación de tasa y retención del ledger. | Concentra los controles de comunicación aguas abajo de la alerta interna. |
| Instrumentación y entorno | Timestamps por tramo, métricas esperadas, estado de aplicabilidad, causa, entorno, librerías y runtime. | Permite calcular o rechazar métricas de forma explícita y reconstruir condiciones de ejecución. |

**Nota.** La tabla presenta los elementos mínimos del manifiesto y de las configuraciones referenciadas. Los contratos concretos se desarrollan en la sección 17.3.8.

##### 17.3.4.2. Diseño de prompts y vocabulario activo

El diseño de prompts expresa las condiciones de riesgo como consultas consumibles por un modelo OVD. La sección 17.1.5.3 estableció la sensibilidad de estos modelos a la formulación de la consulta y fijó el inglés como idioma primario del vocabulario, de modo que aquí sólo se fija la consecuencia arquitectónica. La consulta textual incide sobre la evidencia perceptiva generada, y por eso se registra, se versiona y se mantiene trazable hasta los resultados que contribuye a producir.

Cada prompt se asocia a una condición de riesgo, un texto de consulta, una estrategia de formulación, una versión y un conjunto de prompts activos. Una modificación de redacción se registra como variante experimental y no como reemplazo informal, de manera que pueda explicarse qué formulación produjo una detección y compararse resultados sin perder el vínculo con la condición original.

El vocabulario activo es el conjunto de prompts habilitados en una corrida. Su tamaño y su composición afectan el comportamiento semántico del detector y, según el modelo, el costo de inferencia. Por eso el núcleo validable trabaja con un vocabulario reducido y controlado, suficiente para evaluar la sensibilidad de formulación y sin listas amplias que dificulten atribuir resultados.

Un prompt y una estrategia de detección no son lo mismo. Un prompt es una consulta semántica, mientras que una estrategia puede combinar prompts, postproceso, evidencia indirecta o reglas espaciales.

##### 17.3.4.3. Vocabulario y estrategia del núcleo validable

El diseño inicial distingue el vocabulario positivo del núcleo, los conjuntos de las ramas comparativas y el vocabulario condicionado de las condiciones de mayor complejidad. Para CR-01 y CR-02 el núcleo utiliza person, helmet y vest, donde la primera categoría identifica la entidad sujeto y las restantes representan los elementos de protección cuya presencia se evalúa espacialmente respecto de cada persona.

La ausencia de casco o chaleco no se formula como consulta principal del núcleo. Se infiere en el plano de control cuando existe evidencia suficiente de una persona y no se encuentra evidencia del EPP correspondiente dentro de la región configurada. Las consultas negativas o de estado observable se mantienen en conjuntos separados para las estrategias directa (E-DIR) e híbrida (E-HYB) definidas en la consolidación metodológica, de modo que sus resultados sean atribuibles a una estrategia explícita y no a una mezcla informal de vocabularios.

Para el núcleo validable se adopta la estrategia indirecta con inferencia espacial de ausencia (E-IND). La frontera que esa elección fija es explícita. El plano de medios informa qué entidades observó, dónde y con qué confianza. El plano de control decide si la evidencia del elemento de protección se asocia al sujeto, construye el estado evaluable de la condición y lo estabiliza antes de registrar una alerta.

La estrategia se adopta por auditabilidad, porque cada evaluación puede reconstruirse a partir de la caja del sujeto, la región analizada, las detecciones de protección, los umbrales y la regla aplicada, y así la ausencia no se presenta como una conclusión opaca del modelo. La detección directa (E-DIR) y las variantes híbridas (E-HYB) se conservan como ramas comparativas configurables, con conjuntos de prompts y reglas identificados por separado, y comparten los contratos de publicación, evaluación temporal y registro, de modo que la comparación no requiera alterar la arquitectura central.

CR-03 y CR-04 conservan consultas compuestas y descompuestas de carácter condicionado, porque su confirmación requiere contexto espacial adicional. CR-05 y CR-06 se expresan mediante entidades componentes, ya que la condición completa depende de proximidad, seguimiento o zonas declaradas externamente. La Tabla 43 organiza el vocabulario del núcleo y de las ramas comparativas, y el catálogo completo de formulaciones candidatas por condición y estrategia se consolida en el Anexo C.

**Tabla 43**

*Vocabulario de prompts en inglés del núcleo validable y de las ramas comparativas*

| **Condición y estrategia** | **Rol de la consulta** | **Consulta o categoría candidata** | **Uso previsto** |
| --- | --- | --- | --- |
| CR-01 y CR-02 — núcleo E-IND | Entidad sujeto | person | Localizar las personas sobre las cuales se evalúa la presencia o ausencia espacial del EPP. |
| CR-01 — núcleo E-IND | Evidencia positiva de EPP | helmet | Detectar casco asociable a una persona. La ausencia se infiere en el plano de control. |
| CR-02 — núcleo E-IND | Evidencia positiva de EPP | vest | Detectar chaleco asociable a una persona. La ausencia se infiere en el plano de control. |
| CR-01 — rama E-DIR | Ausencia o estado observable | bare_head; “person without hard hat”; “construction worker without safety helmet”; “person with bare head on construction site” | Comparar formulaciones directas bajo una configuración independiente del núcleo. |
| CR-02 — rama E-DIR | Ausencia o descripción visual | “person without reflective vest”; “worker without high-visibility vest”; “person without bright colored safety clothing” | Comparar formulaciones directas o atributivas bajo una configuración independiente del núcleo. |

**Nota.** El vocabulario del núcleo validable está compuesto por person, helmet y vest. Las formulaciones directas pertenecen a ramas comparativas independientes y el vocabulario condicionado de CR-03 a CR-06 se consolida en el Anexo C. Cada corrida conserva *prompt_set_id*, de modo que toda detección pueda atribuirse al conjunto que la produjo.

##### 17.3.4.4. Reglas de comparabilidad entre configuraciones

La configuración permite comparar variantes sin producir conclusiones ambiguas. Al comparar prompts se mantienen constantes el modelo, la fuente visual, la resolución, la política de muestreo, los umbrales, el postproceso y los criterios de patrón, de modo que una variación de desempeño pueda atribuirse a la formulación evaluada. Al comparar modelos OVD se conserva el mismo conjunto de prompts y condiciones equivalentes de fuente, resolución y postproceso, y si un modelo requiere umbrales distintos por la escala de sus puntajes, esa diferencia se declara como parte de la configuración y no se oculta como detalle de implementación.

Al comparar DBE y EBE se declara que cambia la naturaleza temporal de la fuente. En EBE intervienen la captura continua, la variabilidad de iluminación, la codificación o decodificación cuando corresponda, la continuidad temporal, las omisiones, los descartes y la disponibilidad efectiva de frames, de modo que las diferencias observadas no se atribuyan automáticamente al detector OVD.

Por la misma razón, ningún módulo opcional opera como comportamiento implícito. La evidencia visual, la identidad temporal, las zonas, la preselección en el rol de captura y la distribución externa se habilitan en la configuración de la corrida, porque una activación silenciosa alteraría la interpretación de la latencia, la cobertura temporal, la privacidad y la aplicabilidad de las métricas. Es esa referencia declarada, y no una reinterpretación posterior de los artefactos, la que permite atribuir una diferencia de resultados a la variante evaluada y no a un cambio no declarado en la cadena.

#### 17.3.5. Diseño conceptual del plano de medios

El plano de medios se materializa en el componente lógico Pipeline de Medios, que concentra la ruta sensible a la latencia. Comienza cuando el adaptador de ingesta visual recibe, lee o decodifica una unidad visual proveniente de una fuente externa y termina cuando publica evidencia perceptiva normalizada hacia la frontera de integración. Su alcance abarca ingesta, decodificación cuando corresponda, control de ritmo, normalización visual, inferencia open-vocabulary, postproceso y publicación no bloqueante.

El límite del componente es estricto. El Pipeline de Medios no confirma condiciones de riesgo, no asigna severidad, no ejecuta reglas de patrón, no genera alertas y no depende de persistencia pesada para continuar procesando frames. Su salida es evidencia perceptiva primaria asociada a una corrida, una fuente, una referencia temporal, un modelo y una configuración de procesamiento, y su interpretación corresponde al plano de control.

Las fuentes utilizadas en DBE y EBE ingresan por una misma frontera conceptual, el adaptador de ingesta visual, y la diferencia entre escenarios se resuelve en la forma de lectura, la disponibilidad del frame, los metadatos temporales y el control de ritmo, no en la salida del plano. En DBE predomina la lectura reproducible. En EBE pueden aparecer irregularidades temporales, atraso acumulado, variabilidad de captura o disponibilidad de frames recientes. En ambos casos la salida conserva trazabilidad suficiente para reconstruir qué se procesó, bajo qué configuración y con qué resultado. La Figura 4.2 representa ese flujo interno. Las fuentes visuales son externas al plano, que comienza en el adaptador de ingesta visual, responsable de recibir, leer o decodificar la fuente y transformarla en una unidad visual procesable. La configuración de corrida parametriza la ejecución como entrada transversal, sin formar parte del procesamiento frame a frame. El evento de percepción normalizado se ubica por fuera del recuadro para señalar la frontera de salida hacia el bus interno de eventos y el plano de control.

**Figura 4.2**

*Flujo conceptual del Pipeline de Medios*⟦FIGURA: no extraída — ver el .docx⟧

##### 17.3.5.1. Flujo operativo del Pipeline de Medios

El flujo interno se organiza como una cadena de transformación progresiva. Cada etapa recibe una representación visual o perceptiva, aplica una operación acotada y entrega una salida que mantiene relación con la corrida y con la referencia temporal original, de modo que fuentes, modelos o políticas de procesamiento puedan sustituirse sin modificar la responsabilidad general del plano.

**Ingesta y decodificación.** La primera responsabilidad interna del plano es recibir la entrada visual desde fuentes externas, como datasets, imágenes, videos locales, cámaras o streams. La fuente queda encapsulada por un adaptador de ingesta visual que oculta diferencias de formato sin eliminar información relevante para la evaluación. Cuando la entrada proviene de video codificado o de streaming, la decodificación convierte el flujo en frames procesables y registra la información necesaria para distinguir disponibilidad, recepción, orden lógico y referencia temporal. En DBE suele alcanzar con conservar el índice de secuencia y el orden de lectura. En EBE puede ser necesario registrar además timestamps de captura o recepción, irregularidad temporal y descartes por atraso.

**Control de ritmo y selección de unidades visuales.** Antes de ingresar a inferencia, el pipeline decide qué unidades visuales se procesan. La decisión puede aceptar todos los frames, aplicar una selección determinista, reducir la frecuencia de procesamiento o priorizar unidades recientes cuando existe captura continua. La política se declara por corrida, porque cambiar la selección de unidades, la frecuencia de procesamiento o el criterio de omisión equivale a cambiar la variante experimental evaluada. Lo que el diseño exige no es una política concreta sino la ausencia de decisiones invisibles, de manera que toda unidad omitida, reemplazada o descartada quede asociada a una causa y a una política declarada.

En corridas DBE, o con fuentes cuya lectura puede regularse, la prioridad es preservar reproducibilidad, orden lógico y trazabilidad de las unidades procesadas, y si no se procesan todos los frames la selección es determinista y se mantiene constante entre corridas comparables. En corridas EBE, o con fuentes en vivo, la prioridad es que el atraso acumulado no crezca indefinidamente y que toda omisión, irregularidad temporal o descarte quede registrada. El resultado esperado no es maximizar la cadencia de forma aislada sino hacer interpretable el comportamiento del pipeline, porque un sistema que procesa menos frames puede ser válido para una corrida exploratoria y esa reducción debe ser visible para no confundir rendimiento con cobertura temporal.

**Normalización visual**. El frame aceptado se adapta a los requisitos del modelo seleccionado. Esta etapa puede modificar resolución, formato, espacio de color, disposición de tensores o escala de entrada. El diseño preserva la relación entre coordenadas originales y coordenadas de inferencia, porque esa relación permite interpretar cajas delimitadoras, revisar evidencia visual y comparar resultados entre configuraciones con distinta resolución. Reescalado, recortes o relleno de bordes no deben tratarse como operaciones invisibles.

**Inferencia open-vocabulary.** La inferencia ejecuta el detector configurado sobre la entrada normalizada y el conjunto de prompts activos. El modelo se integra mediante un adaptador para evitar que el resto del plano dependa de la salida particular de un detector concreto. Esta etapa produce resultados crudos, como cajas, puntajes, etiquetas o frases asociadas, según el formato propio del detector utilizado. Cuando el modelo lo permita, el adaptador puede reutilizar representaciones textuales precalculadas o mecanismos equivalentes para reducir el costo de inferencia, siempre que esa optimización no altere la trazabilidad de la corrida.

**Postproceso y normalización de detecciones.** Luego de la inferencia, el pipeline aplica los filtros definidos por la configuración de corrida, entre ellos umbrales, supresión de detecciones redundantes, normalización de etiquetas y remapeo de coordenadas, para convertir las salidas del modelo en evidencia perceptiva común. Esa salida queda asociada al frame, al prompt, a la condición y al nivel de confianza correspondiente. No interpreta riesgo ni genera alertas, y sólo entrega evidencia normalizada al plano de control.

**Publicación de evidencia perceptiva.** La publicación cierra el plano de medios. La evidencia normalizada se entrega como evento liviano hacia la frontera de integración, asociada a la corrida, la fuente, la referencia temporal, el modelo, los prompts y los timestamps relevantes. A partir de ese punto la evidencia puede evaluarse en el plano de control, persistirse de manera reconstruible o inspeccionarse desde el soporte experimental, y ninguna de esas tareas es requisito para que el pipeline continúe con la siguiente unidad visual.

En consecuencia, la salida del plano de medios no se reduce a cajas y puntajes sin contexto y tampoco incorpora severidad, confirmación de patrón ni decisión de alerta. Su producto es evidencia visual primaria, normalizada y trazable, cuya interpretación corresponde al plano de control.

Sobre esa cadena el diseño mantiene una ruta no bloqueante. Si el bus interno, la persistencia, la inspección o una salida externa fallan o se saturan, esa condición se registra como parte de la ejecución y no convierte a esos consumidores en dependencia directa del procesamiento visual. El plano hace visible además la variabilidad temporal, porque una latencia aparentemente baja puede ocultar pérdida de frames, colas saturadas o reemplazo de frames antiguos por frames recientes, y por eso registra timestamps por tramo, profundidad de cola cuando corresponde, frames aceptados, frames omitidos y descartes.

Los adaptadores absorben la heterogeneidad de los detectores OVD, que difieren en formato de entrada, tipo de prompt, estructura de salida, semántica de puntajes y costo de inferencia, y entregan una evidencia perceptiva estable que no acopla al plano de control con un modelo específico ni con los detalles internos de su implementación. La persistencia temporal de un patrón, la histéresis, la severidad y el registro interno de la alerta pertenecen al motor de patrones, de modo que el plano de medios pueda mejorar la calidad de la evidencia perceptiva sin decidir si una condición observada se convirtió en una situación de riesgo confirmada.

##### 17.3.5.2. Capacidades opcionales y degradación segura

El núcleo validable del plano de medios opera sin seguimiento multiobjeto formal, sin preselección en borde y sin adaptación de modelos al dominio. Estas capacidades se incorporan como variantes del flujo, no son requisito para demostrar el procesamiento de CR-01 y CR-02 y no modifican el contrato de salida. La preselección en borde se adopta bajo un criterio de degradación segura, denominado fail-open, por el cual una falla o una decisión incierta del preselector conserva la unidad visual para el flujo principal. La variante puede descartar carga y nunca ser causa de pérdida de evidencia.

El seguimiento puede ubicarse después del postproceso cuando resulte necesario estabilizar entidades, reducir oscilaciones entre frames o entregar identificadores temporales al plano de control. Un identificador temporal no equivale a una condición de riesgo sostenida.

Las variantes orientadas a eficiencia reciben el mismo tratamiento. Las reducciones de resolución, los cambios de modo de inferencia o las exportaciones a motores optimizados corresponden a la implementación, y cualquier variante que altere la ruta frame-evento se declara en la configuración de corrida.

#### 17.3.6. Diseño conceptual del plano de control

El plano de control interpreta la evidencia perceptiva producida por el plano de medios. Su responsabilidad comienza cuando ingresa un evento de percepción normalizado y termina cuando el sistema registra estados de patrón, alertas internas, eventos persistibles, métricas y salidas de inspección o distribución desacopladas. A diferencia del Pipeline de Medios no procesa frames crudos ni opera al ritmo constante de captura, porque trabaja sobre eventos y sobre cambios de estado derivados de reglas configuradas.

La separación entre detección, patrón y alerta es su decisión arquitectónica central. Una detección puntual expresa una observación del modelo sobre una unidad visual. Un patrón confirmado expresa que esa evidencia fue evaluada durante una ventana temporal bajo criterios explícitos de persistencia, umbral e histéresis. Una alerta interna registra un episodio asistivo generado por una transición válida del patrón. El plano no transforma cada detección en una alerta, sino que estabiliza la evidencia antes de producir salidas operativas.

Esa organización evita que la variabilidad propia de la inferencia OVD, con sus falsos positivos, falsos negativos, fluctuación de puntajes, sensibilidad al prompt u oclusiones parciales, se traslade directamente al sistema de alertas. También mantiene al plano de medios aislado de consumidores lentos, persistencia histórica, reportes, notificaciones externas o interfaces de inspección, que el plano de control ejecuta de forma asíncrona.

En el alcance del prototipo el plano de control se orienta al núcleo validable. Para CR-01 y CR-02 la evaluación se resuelve mediante persistencia temporal simple y estados de patrón, sin exigir seguimiento multiobjeto formal. El seguimiento, las zonas espaciales y las reglas relacionales enriquecen escenarios posteriores y no son dependientes del núcleo validable.

El plano recibe evidencia perceptiva normalizada, selecciona los patrones activos, evalúa la evidencia espacial y temporal, administra el estado de cada patrón y registra una alerta interna cuando confirma un episodio, mientras persiste transiciones, métricas y errores. La evaluación no ejecuta inferencia visual, no asigna identidad personal y no determina cumplimiento normativo, porque aplica reglas declaradas de asociación espacial, persistencia, granularidad e histéresis. La alerta interna que sigue a la confirmación es el hecho principal del sistema y precede a cualquier notificación.

##### 17.3.6.1. Máquina de estados y ciclo del episodio

La máquina de estados distingue inactivo (*inactive*), candidato (*candidate*), confirmado (*confirmed*), sostenido (*sustained*) y resuelto (*resolved*). Una evidencia inicial abre el estado candidato. La confirmación ocurre cuando la condición satisface la ventana temporal y los umbrales declarados. La continuidad mantiene el episodio y la ausencia sostenida durante la histéresis lo resuelve.

La transición a confirmed registra una alerta interna por episodio. El estado sostenido actualiza duración y evidencia sin convertir cada frame positivo en una alerta nueva. Una nueva confirmación posterior se conserva como re-alerta y se evalúa por separado de los falsos positivos.

Las ventanas se expresan en milisegundos y no en frames, de modo que la semántica temporal no cambie con la cadencia de procesamiento. Los valores adoptados para los patrones del núcleo se documentan junto con la configuración efectiva en la sección 17.4.4.

El ciclo de evaluación selecciona evidencias, actualiza la memoria, aplica la ventana de confirmación y la histéresis, registra la transición y conserva la causa. Los descartes de fuente, los huecos temporales y la pérdida de identidad se distinguen de la ausencia real de evidencia. La confirmación representa el cumplimiento de una regla interna bajo la configuración de la corrida y no constituye certificación normativa ni decisión automática de intervención. La Figura 4.3 representa el ciclo de vida temporal de un patrón de riesgo en el plano de control. La condición observada abre el estado candidate y, cuando la evidencia satisface la ventana de confirmación configurada, el patrón pasa a confirmed y se registra la alerta interna correspondiente. Mientras la condición permanece activa el patrón evoluciona a sustained. Cumplida la ventana de resolución, el episodio pasa a resolved y retorna a inactive. Si la evidencia inicial resulta insuficiente o no persiste durante la ventana de confirmación, el patrón vuelve a inactive sin generar una alerta.

**Figura 4.3**

*Máquina de estados del motor de patrones*

⟦FIGURA: no extraída — ver el .docx⟧

##### 17.3.6.2. Motor de evaluación y definición de patrón

El motor de evaluación es el componente lógico del plano de control que transforma evidencia perceptiva normalizada en estados de patrón, episodios y alertas internas. No procesa imágenes ni ejecuta inferencia OVD. Consume los eventos publicados por el plano de medios, consulta las definiciones activas de patrón declaradas en la configuración experimental y actualiza el estado correspondiente dentro de la corrida.

El motor admite el catálogo completo de patrones del prototipo y su activación efectiva depende de la configuración de corrida, los módulos habilitados y la disponibilidad de evidencia suficiente, de modo que la arquitectura pueda incorporar patrones de mayor complejidad sin modificar la lógica central del plano de control.

El motor no evalúa condiciones de riesgo aisladas, sino patrones activos que las operacionalizan durante una corrida. La condición identificada mediante CR-01 a CR-06 conserva el significado semántico del fenómeno observable, y el patrón correspondiente, identificado mediante PR-01 a PR-06, establece la regla con la que ese fenómeno se convierte en un estado evaluable. La separación permite modificar la estrategia de evidencia, la granularidad o el comportamiento temporal sin alterar el catálogo de condiciones de riesgo.

Cada patrón se declara mediante configuración y reúne, como una única definición evaluable, los criterios necesarios para admitir evidencia, mantener estado y producir una salida trazable, de modo que la lógica del motor no dependa de reglas particulares incorporadas de manera rígida en el código. La definición comprende siete elementos.

**Identidad y vínculo semántico**. El código y la versión del patrón lo relacionan con una condición de riesgo determinada. Esta asociación permite reconstruir qué regla evaluó la evidencia y bajo qué definición, sin confundir el fenómeno observable con su tratamiento operativo.

**Evidencia admisible.** El patrón especifica qué detecciones o relaciones pueden intervenir en la evaluación. En el núcleo, el motor utiliza detecciones positivas de person y del elemento de protección correspondiente, helmet o vest, y determina su presencia o ausencia mediante asociación espacial. La condición de riesgo no se deriva de una detección negativa opaca.

**Granularidad y región de evaluación.** La granularidad scene mantiene el estado por patrón y fuente, mientras que subject lo mantiene además por identidad temporal de sujeto. Cuando la condición depende de un elemento asociado a la persona, el patrón también declara la región relativa de la caja donde se busca la evidencia, que es la región cefálica para PR-01 y el torso para PR-02.

**Precondiciones de evidencia**. La definición establece los requisitos mínimos que deben satisfacer el sujeto y el elemento de protección para contribuir al patrón, como confianza y área del sujeto. Estos criterios se aplican sobre la evidencia ya normalizada por el plano de medios y evitan que detecciones insuficientes modifiquen el estado temporal.

**Regla temporal e histéresis**. El patrón declara una ventana de confirmación que exige evidencia sostenida antes de registrar la condición y una ventana de resolución que impide cerrar el episodio ante pérdidas breves, oclusiones o fluctuaciones del detector. Ambas se expresan en milisegundos para que su significado no dependa de la cadencia de procesamiento.

**Severidad y dependencias opcionales**. La severidad proviene del catálogo metodológico y permanece asociada al patrón durante la corrida. Las capacidades adicionales —identidad temporal, zonas o relaciones entre entidades— sólo intervienen cuando fueron habilitadas explícitamente y existe evidencia suficiente para utilizarlas.

**Estado y salida observable.** A partir de los criterios anteriores, el motor actualiza el estado del patrón y registra las transiciones correspondientes. Cuando la evidencia satisface la regla de confirmación, produce la alerta interna y los eventos necesarios para reconstruir posteriormente la evaluación.

La granularidad de la memoria temporal es un parámetro explícito de la definición de patrón. Bajo granularidad de escena el estado se indexa por (patrón, fuente) y evalúa la continuidad de la condición en la escena. Bajo granularidad de sujeto se indexa por (patrón, fuente, identidad) y exige una identidad temporal válida.

La granularidad de sujeto sólo puede utilizar una identidad producida por un componente de seguimiento o por un decorador equivalente del plano de control, porque el identificador de detección no vale entre frames. La capacidad se habilita por configuración sin modificar el contrato de percepción, y la identidad resultante se conserva en los artefactos del control y no en el registro ordinario del plano de medios.

La granularidad de escena sostiene una afirmación precisa, que es la persistencia de la condición en la escena. No permite concluir que el mismo sujeto sostuvo el riesgo durante toda la ventana, porque una rotación de personas podría mantener la condición de forma continua. Esa segunda afirmación requiere granularidad de sujeto.

La exclusión de las métricas formales de seguimiento multiobjeto no elimina esta capacidad, porque la arquitectura separa la identidad necesaria para indexar el estado del patrón de la evaluación formal del desempeño de seguimiento.

El motor respeta la clasificación metodológica de condiciones por nivel de complejidad. Desde el diseño arquitectónico, esa clasificación se traduce en requisitos de evaluación distintos, porque algunos patrones se resuelven con evidencia perceptiva y persistencia temporal simple y otros sólo se activan cuando la corrida habilita insumos adicionales como seguimiento, zonas parametrizadas o reglas espaciales.

Esa diferenciación permite diseñar un motor único sin sobredimensionar el prototipo experimental, con una lógica común de evaluación que adapta sus entradas y criterios según el patrón activo y la configuración de corrida. La Tabla 44 reúne las dependencias arquitectónicas de cada patrón y su tratamiento en el prototipo.

**Tabla 44**

*Diseño del motor de patrones según condición de riesgo*

| **Patrón y condición asociada** | **Evidencia y regla de evaluación** | **Dependencias arquitectónicas** | **Tratamiento en el prototipo** |
| --- | --- | --- | --- |
| PR-01 / CR-01 — Persona sin casco | Detecciones positivas de person y helmet, con evaluación de la región cefálica por sujeto. | Eventos de percepción, coordenadas comparables y referencia temporal. La granularidad de sujeto requiere identidad temporal válida; la de escena no. | Núcleo validable. Produce estados candidato, confirmado, sostenido y resuelto, además de una alerta interna trazable por episodio. |
| PR-02 / CR-02 — Persona sin chaleco reflectivo | Detecciones positivas de person y vest, con evaluación de la región del torso por sujeto. | Eventos de percepción, coordenadas comparables y referencia temporal. Comparte la misma frontera contractual que PR-01. | Núcleo validable. Se evalúa mediante la misma cadena arquitectónica, con severidad y ventanas propias. |
| PR-03 / CR-03 — Trabajo en altura sin anticaídas visible | Persona en altura o sobre estructura elevada junto con ausencia o baja evidencia de sistema anticaídas visible. | OVD sobre entidades o atributos, reglas espaciales intra-frame y evidencia visual suficiente del escenario. | Extensión condicionada. No bloquea el núcleo; sólo debe activarse si existen datos o escenas que permitan evaluar la condición completa. |
| PR-04 / CR-04 — Borde elevado desprotegido con personas próximas | Borde, plataforma o zona elevada sin protección colectiva, con personas próximas. | OVD de entidades del entorno, reglas espaciales, posible parametrización de regiones y cámara con perspectiva adecuada. | Extensión condicionada. Puede reportarse parcialmente si sólo se detectan componentes visuales sin validar la condición completa. |
| PR-05 / CR-05 — Maquinaria cerca de peatones | Maquinaria y personas con relación de proximidad sostenida. | OVD de entidades, seguimiento temporal o asociación equivalente, reglas de proximidad y métricas de continuidad. | Condicionado a módulo contextual. No pertenece al núcleo; requiere instrumentación temporal y control de falsos positivos relacionales. |
| PR-06 / CR-06 — Persona en zona restringida | Persona dentro de un polígono o zona definida externamente. | Cámara fija o geometría controlada, polígono de zona, OVD de persona y, preferentemente, tracking o asociación temporal. | Condicionado a escenario EBE controlado o fuente fija. Requiere parametrización explícita de zona en la configuración de corrida. |

**Nota.** La tabla declara las dependencias arquitectónicas de cada patrón y el tratamiento que recibe en el prototipo. El tratamiento «núcleo validable» identifica los patrones obligatorios del prototipo experimental. El tratamiento «extensión condicionada» indica capacidades previstas que sólo deben habilitarse cuando existan datos, módulos e instrumentación suficientes. Las reglas de evidencia, la severidad y los rangos de persistencia de cada patrón se establecen en la sección 17.1.5.2.

La salida principal del motor no es una alerta aislada, sino una secuencia de eventos derivados que describen el ciclo de vida del patrón, desde el inicio del candidato hasta la confirmación, el sostenimiento y la resolución o el descarte por evidencia insuficiente. La alerta interna se registra sólo cuando una transición válida confirma el patrón, lo que evita emitir alertas por cada frame positivo y permite analizar episodios con inicio, duración, evidencia causal y cierre.

Cada transición conserva trazabilidad suficiente para explicar su origen, con la configuración de corrida, el patrón evaluado, la condición asociada, la evidencia considerada, la ventana temporal, los umbrales aplicados, el estado previo, el estado nuevo y la referencia temporal. Esa información permite reconstruir por qué se generó una alerta, por qué se resolvió un episodio, qué evidencia se descartó y qué parámetros condicionaron el resultado.

##### 17.3.6.3. Transporte, persistencia y trazabilidad experimental

La arquitectura diferencia el canal de transporte del repositorio persistente, de modo que la durabilidad no se atribuya a un mecanismo de mensajería diseñado para baja latencia. El repositorio es la fuente de verdad. Cada evento de percepción se escribe en un archivo JSONL de sólo adición antes de publicarse, y los cambios de estado, las alertas, las métricas y los errores siguen la misma regla en sus componentes respectivos. Si el canal falla, el hecho persistido permanece disponible para relectura.

En el camino de ejecución en vivo el canal adopta ZeroMQ con patrón publicador-suscriptor, msgpack, tópicos por tipo de evento y un número de secuencia monótono dentro del envoltorio versionado del bus. El plano de control consume ese contrato por el canal de detecciones y no interpreta formatos propios de un detector ni recibe frames crudos. El payload publicado corresponde al mismo contenido lógico persistido, de manera que la corrida pueda releerse por el camino diferido sin redefinir la evidencia.

Todo consumidor se suscribe antes de que su productor publique, y el orquestador verifica esa precondición al crear la corrida, porque la respuesta de creación de un consumidor implica su disponibilidad, y cuando un consumidor se crea después de su productor, como ocurre con el módulo de distribución, es el publicador el que retiene la emisión hasta que exista un suscriptor. El orden efectivo de arranque de los módulos se documenta en la sección 17.4.

La pérdida se detecta mediante huecos de secuencia. Un hueco incrementa *bus_dropped_events*, degrada la corrida y queda expuesto en el reporte, y nunca se interpreta como ausencia de evidencia en la escena.

El cierre de la corrida se propaga mediante un evento de ciclo de vida cuyo hito de finalización delimita el final lógico y permite cerrar consumidores, consolidar artefactos y distinguir un fin normal de una interrupción.

La frontera contractual no depende de que el transporte utilice o no un broker, porque la durabilidad, la reevaluación y la causalidad se sostienen en la regla de persistir antes de publicar y en los esquemas versionados.

##### 17.3.6.4. Cadena de traducción entre condición, evidencia, patrón y alerta

La cadena que va de la condición observable hasta la alerta atraviesa los dos planos. La condición del catálogo metodológico define qué fenómeno se monitorea, la estrategia de detección establece si la evidencia se busca mediante un prompt directo, una combinación de consultas, evidencia auxiliar o reglas contextuales, el plano de medios publica evidencia perceptiva normalizada y el plano de control la evalúa mediante el patrón correspondiente. Cuando la evaluación confirma el episodio, registra una alerta interna, que es una salida asistiva del sistema y no equivale a una notificación externa ni a una certificación normativa. La Figura 4.4 muestra cómo una condición definida metodológicamente se materializa en la arquitectura. La estrategia orienta la producción de evidencia en el plano de medios, el patrón la evalúa en el plano de control y la alerta interna registra el episodio confirmado.

**Figura 4.4**

*Cadena de traducción entre condición, estrategia, evidencia, patrón y alerta*

⟦FIGURA: no extraída — ver el .docx⟧

#### 17.3.7. Distribución de alertas confirmadas

La alerta interna es el hecho terminal del plano de control y todavía no es un aviso. El tramo de distribución la convierte en intentos de entrega registrados sin participar del razonamiento que la produjo.

El plano de control publica cada alerta confirmada en un bus de alertas dedicado, y el módulo de distribución la consume desde allí, aplica la política de notificación y registra el resultado de cada intento. No constituye un tercer plano ni un cuarto rol funcional, sino un módulo desacoplado, y esa condición es la que impide que la indisponibilidad de un canal externo se propague al motor de patrones.

El pipeline de distribución comprende una fuente de alertas, una política de notificación, un sobre versionado, un adaptador de canal y un ledger de entregas. La misma lógica admite la relectura desde artefactos persistidos y el consumo en vivo desde el bus de alertas, sin modificar la semántica de la alerta de entrada.

La política ordinaria prioriza trazabilidad, idempotencia y operación no bloqueante. Una falla del canal genera un resultado de entrega y un error interpretable, y no invalida ni elimina la alerta interna. Toda notificación externa es una salida derivada de la alerta interna y se mide por separado.

El tramo separa el dato del gobierno. Las alertas confirmadas llegan por el bus de alertas en sentido único desde el plano de control, mientras que las órdenes de ciclo de vida llegan por una interfaz de gobierno propia del módulo, que permite crear, consultar, cancelar y descartar corridas de entrega. Para la relectura diferida el módulo conserva una entrada offline sobre alertas persistidas, y ambos caminos utilizan los mismos contratos de alerta interna, sobre de notificación y registro de entrega, por lo que la modalidad de ejecución no modifica la semántica de la alerta ni la del resultado.

La Tabla 45 distingue los consumidores del evento confirmado. Ninguno puede modificar retrospectivamente el patrón, la alerta interna o su referencia temporal.

**Tabla 45**

*Consumidores y salidas del tramo de distribución*

| **Consumidor o salida** | **Uso previsto** | **Tratamiento arquitectónico** |
| --- | --- | --- |
| MQTT QoS 1 | Publicar el sobre de notificación y esperar confirmación de entrega del broker. | Canal de entrega mediante adaptador; el resultado queda asentado como registro de entrega. |
| Interfaz de inspección | Mostrar alerta, política aplicada, intento y resultado de entrega. | Proyección de consulta; no consume el bus de percepción ni confirma patrones. |
| Reporte experimental | Consolidar conteos por resultado de entrega, errores y latencia del tramo. | Se calcula desde el ledger y se mantiene separado de las métricas de alerta interna. |
| Relectura DBE | Distribuir alertas ya persistidas de una corrida. | Debe ser idempotente: reprocesar el mismo evento no duplica entregas. |
| Canales adicionales | Correo, webhook u otras integraciones futuras. | Punto de extensión por adaptador; no forma parte del núcleo ni altera los contratos existentes. |

**Nota.** El módulo de distribución conserva su propio estado operativo y su ledger, y no utiliza el almacenamiento continuo de video ni requiere acceso a frames crudos.

El conjunto de patrones adoptado no suprime confirmaciones, porque cada alerta interna se registra para conservar la dinámica real del episodio. La decisión es deliberada. El motor dispone de control de re-confirmación por patrón y sujeto y el núcleo lo deja inactivo, ya que un motor que suprimiera dejaría de reflejar la duración del episodio y no permitiría distinguir una condición que persiste de una que se resolvió.

La supresión de re-notificación se reubica en la política del módulo de distribución y, al reubicarse, cambia de granularidad. El motor la aplicaría por patrón y sujeto, mientras que la política de entrega aplica una ventana de silencio por condición y fuente, porque para una notificación asistiva lo relevante es que esa condición en esa cámara ya fue avisada. La agrupación de avisos y la limitación de tasa quedan como punto de extensión de la política. Una alerta suprimida para comunicación existió y continúa siendo medible, y las re-alertas de un episodio activo se informan por separado y no se computan como falsos positivos, de modo que una decisión de comunicación no altere la precisión del motor.

El ledger de entregas es de sólo agregado, aplica una clave de idempotencia por notificación y canal y acumula entre corridas, de manera que un reprocesamiento no vuelva a entregar lo ya entregado. Cada fila conserva el número de intento, la marca temporal, el resultado, el motivo de error y la confirmación del canal, y distingue entrega exitosa, supresión por política, descarte por duplicado, falla de un intento y descarte definitivo por agotamiento de reintentos. Cada fila registra además la modalidad en que se midió la latencia del tramo, que se informa siempre separada por modalidad, porque en relectura diferida el intervalo incorpora el ritmo de reinyección de las alertas persistidas, que es propiedad del reprocesamiento y no del canal. El detalle operativo del ledger, incluida la unidad de conteo del tramo, se documenta en la sección 17.4.

#### 17.3.8. Contratos, trazabilidad y evidencia visual

Los contratos estabilizan la semántica de intercambio entre componentes y definen qué información cruza cada frontera y bajo qué versión. En la arquitectura consolidada del núcleo se expresan como modelos de datos versionados, con serializaciones explícitas e interfaces concretas, y cada uno queda asociado a una corrida para que productores y consumidores evolucionen de forma independiente. La versión viaja dentro del payload y no en el envoltorio de transporte, de manera que el canal pueda cambiar sin que el hecho persistido pierda la identificación de su esquema. Las capacidades futuras evolucionan de forma aditiva sin romper la lectura de corridas históricas.

Las fronteras son lógicas y no prescriben que cada responsabilidad se despliegue en una máquina, un proceso o un contenedor independiente.

##### 17.3.8.1. Contratos mínimos e interfaces

Todo contrato declara su identidad de esquema y su versión como primer elemento del payload. La Tabla 46 reúne los contratos mínimos de la ejecución experimental.

**Tabla 46**

*Contratos mínimos para la ejecución experimental*

| **Contrato** | **Función arquitectónica** | **Información mínima** |
| --- | --- | --- |
| Manifiesto de experimento | Gobierna la ejecución experimental. | experiment_id, referencias de configuración, runs por componente, orden de inicio, modelo, prompt set, pattern set y versión. |
| SourceDefinition | Describe la fuente visual. | source_id, tipo, naturaleza temporal, ubicación o dispositivo, resolución, ritmo y restricciones. |
| ModelProfile | Define el adaptador y perfil de inferencia. | Modelo, checkpoint, backend, dispositivo, precisión y parámetros de entrada. |
| PromptDefinition | Versiona el vocabulario. | prompt_set_id, clase, texto, rol, estrategia y umbrales asociados. |
| FrameMetadata | Identifica la unidad visual. | unit_id, source_id, índice, timestamp, tamaño y transformaciones. |
| PerceptionEvent | Publica evidencia perceptiva normalizada. | run, unidad, fuente, modelo, prompts, detecciones y timing. |
| PatternDefinition | Declara la condición evaluable. | Patrón, condición, sujeto, EPP requerido, granularidad, región, umbrales, confirmación, resolución y severidad. |
| PatternStateChanged | Registra la transición del motor. | Estado anterior y nuevo, evidencia, sujeto o escena y tiempos. |
| AlertEvent | Registra la confirmación de un episodio. | Identificador determinista, patrón, fuente, evidencia, severidad y hito de registro. |
| MetricSample / ErrorEvent | Conserva observabilidad y fallas. | Nombre, valor, unidad, tramo, reloj, status, cause, error y contexto. |
| Referencia temporal de evaluación | Anota episodios por clip. | clip_id, condición, inicio y fin en ms, eventos subumbral, tolerancia, condición negativa y procedencia. |
| NotificationEnvelope | Prepara una alerta para entrega. | Alerta, política, canal, intento y clave de idempotencia. |
| DeliveryRecord | Registra el resultado del canal. | Resultado de entrega, timestamp, confirmación, error y latencia del tramo. |

**Nota.** Los contratos de referencia temporal y distribución tienen el mismo estatuto formal que los eventos de percepción y control, porque una medición o una entrega no es reproducible si su entrada carece de versión y procedencia.

El evento central del sistema es el evento de percepción, que agrupa la identidad de esquema versionada, la corrida, la unidad visual, la fuente, el modelo, los prompts, las detecciones y los tiempos. Cada detección conserva etiqueta, prompt, confianza, caja en píxeles y normalizada, y área. El *detection_id* sólo identifica una detección dentro de la unidad visual y no constituye identidad entre frames. Los campos opcionales se incorporan de forma aditiva y se omiten cuando no están disponibles.

La referencia temporal de evaluación impone dos invariantes de validez. La identidad de la fuente de la corrida y la del clip anotado deben coincidir, y para el banco temporal se utiliza *source_id = clip_id*. Y la incertidumbre no fabrica una infracción, de modo que cuando el estado del EPP no es juzgable el episodio no se extiende como violación.

La cadena temporal conserva cinco hitos por alerta, que son la primera evidencia positiva identificada por *unit_id*, la transición a candidato, la transición a confirmado, el registro de la alerta interna y, cuando existe distribución, la confirmación de entrega. Esos hitos permiten medir cada tramo sin mezclar relojes ni poblaciones.

La superficie de crecimiento del evento de percepción se mantiene acotada y separada de las reglas de riesgo. La identidad temporal de sujeto es un campo opcional y la única identidad válida entre frames, que el plano de control puede materializar por configuración sin que el plano de medios necesite emitirla. La velocidad, la dirección, los puntos clave de pose y las máscaras de segmentación quedan previstos como campos opcionales que no modifican la semántica mínima del evento ni desplazan al bounding box. Las relaciones entre sujeto, evidencia de soporte y clase ausente pertenecen al plano de control, porque el plano de medios publica detecciones individuales.

##### 17.3.8.2. Repositorio de hechos y reconstrucción experimental

La trazabilidad experimental permite reconstruir cómo una corrida produjo una alerta interna. La arquitectura conserva la relación entre la configuración de corrida, la fuente visual, el modelo utilizado, los prompts activos, la evidencia perceptiva, la transición de estado del patrón, la alerta registrada y las métricas o errores asociados. Sin esa relación una alerta pierde valor experimental, porque no puede auditarse, compararse ni analizarse con suficiente rigor.

El repositorio utiliza archivos JSONL de sólo adición por corrida y por tipo de hecho. La regla impide la sobrescritura silenciosa y ofrece una representación simple, inspeccionable y re-evaluable sin introducir una base de datos como dependencia del núcleo.

Cada corrida conserva configuración efectiva, manifiesto, procedencia y versión de código junto a detecciones, métricas, errores, transiciones y alertas. El soporte experimental agrupa los runs de los componentes bajo *experiment_id*, copia los artefactos livianos y referencia los de mayor volumen.

Toda alerta puede reconstruirse hasta la configuración efectiva, el conjunto de prompts, el modelo, la fuente y la versión de código que la produjeron. La persistencia no requiere video crudo continuo y mantiene separados los hechos originales de sus proyecciones tabulares o reportes.

Los hechos que la reconstrucción exige exceden a los contratos de intercambio. Junto al inicio y cierre de corrida, al manifiesto con las configuraciones efectivas y a la procedencia e identidad de la fuente, el repositorio conserva los eventos de percepción, las unidades omitidas o descartadas con su causa, los cambios de estado del patrón, la primera evidencia positiva, las alertas internas, las entregas cuando el tramo está habilitado, las métricas con su estado de aplicabilidad y los errores y anomalías. Los hechos asociados a seguimiento temporal, zonas, distribución externa, adaptación de modelos o evidencia visual controlada se incorporan sólo cuando la corrida habilita esas capacidades y no forman parte del conjunto mínimo para CR-01 y CR-02.

Esta selección prioriza la reconstrucción de la cadena causal de la alerta. Una detección aislada no explica un episodio, porque debe relacionarse con la configuración que la produjo, el patrón que la evaluó, la transición que confirmó la condición y las métricas o anomalías que condicionaron el resultado. Por esa razón los errores y descartes relevantes tienen el mismo valor interpretativo que los eventos funcionales, ya que permiten distinguir una ausencia real de evidencia de una falla técnica, un descarte por muestreo o una limitación de la fuente.

Las extensiones condicionadas mantienen esta lógica. Si se incorpora seguimiento temporal, zonas, reglas espaciales, notificaciones externas o adaptación de modelos, esos hechos se persisten como información adicional de la corrida, sin desplazar la cadena mínima de reconstrucción ni convertir capacidades exploratorias en requisitos del núcleo experimental.

##### 17.3.8.3. Política de evidencia visual mínima

La arquitectura adopta una política de minimización de evidencia visual. En el comportamiento ordinario del prototipo la trazabilidad se apoya en identificadores, metadatos, eventos, métricas, coordenadas, referencias temporales y relaciones causales entre hechos persistidos. El almacenamiento continuo de video crudo no forma parte del flujo base, porque aumenta volumen, complejidad y riesgo de privacidad sin ser necesario para reconstruir las decisiones experimentales.

Cuando la revisión técnica, la validación o la comunicación académica requieren evidencia visual, ésta se conserva como artefacto controlado, en forma de snapshot, recorte anotado, clip breve, huella criptográfica, referencia a archivo o vínculo asociado a una alerta o corrida específica. Su uso se justifica por la finalidad experimental, cuenta con criterios explícitos de acceso, retención y anonimización, y no reemplaza métricas, eventos persistidos ni criterios de evaluación.

La política preserva el carácter asistivo y no identificatorio de la plataforma. El sistema no realiza reconocimiento facial, no identifica nominalmente a trabajadores, no extrae biometría y no emite decisiones normativas autónomas. La alerta interna orienta la atención humana sobre una condición visualmente observable, y la interpretación final y cualquier acción preventiva permanecen fuera del sistema automatizado.

#### 17.3.9. Observabilidad y aplicabilidad de métricas

La observabilidad forma parte del contrato experimental. Cada métrica declara la señal que utiliza, el inicio y el cierre del reloj, la unidad, la población y la condición de aplicabilidad. Cuando una medición no tiene significado, la plataforma conserva la causa en lugar de publicar cero u omitir el campo.

La instrumentación se ancla en los puntos donde la arquitectura ya produce hechos. Las transiciones del motor sostienen las métricas del plano de control, porque el tiempo hasta la primera detección se ancla en la primera evidencia perceptiva relevante, la latencia de alerta del sistema se cierra con el registro de la alerta interna que sigue a la transición a confirmado y la tasa de detección sostenida se calcula sobre la continuidad del episodio. Las definiciones operacionales de cada métrica, sus hitos y sus reglas de lectura se establecen en las secciones 17.1.7.3 y 17.1.7.5 y en el Anexo D. La Tabla 47 ubica cada medición en el tramo arquitectónico que la produce.

**Tabla 47**

*Métricas y evidencias por tramo arquitectónico*

| **Tramo** | **Punto de medición** | **Métricas o evidencias** |
| --- | --- | --- |
| Captura y host | Captura física, timestamp de fuente y dequeue en el host. | capture_to_host, jitter y disponibilidad temporal, cuando existe ancla compatible. |
| Plano de medios | Dequeue, normalización, inferencia, postproceso y publicación. | G2A, latencia de inferencia, FPS efectivo, throughput y descartes. |
| Bus media-control | Publicación, secuencia y recepción. | Huecos de seq, integridad, atraso y correlación por unit_id. |
| Plano de control | Primera evidencia, candidato, confirmado, alerta y resolución. | TTFD, t_alert-system, latencia interna, SDR, transiciones y re-alertas. |
| Distribución | Disponibilidad de alerta, intento y confirmación del canal. | t_alert-notification, resultados de entrega, supresiones, duplicados y errores. |
| Soporte experimental | Consolidación por corrida y entorno. | Recursos, estados de aplicabilidad, causas, robustez y reporte reconstruible. |

**Nota.** La cadena temporal completa se informa por tramos, y cada tramo declara su hito inicial, su hito final y su dominio de reloj. Los percentiles de tramos diferentes no son aditivos y no deben sumarse para fabricar una latencia de extremo a extremo. La medición del plano de medios comienza en el ingreso de la unidad al host de procesamiento y no en la captura física, que constituye un tramo propio.

Las latencias dentro de un mismo host utilizan reloj monotónico local, y los monotónicos de hosts distintos no se restan. Cuando un trayecto cruza dominios de reloj sin una sincronización válida, la métrica se declara no interpretable con su causa.

El criterio de detección positiva se comparte con el motor de patrones, de modo que la evaluación no reimplemente una segunda definición de evidencia y no aparezcan divergencias silenciosas entre el sistema que decide y el sistema que mide. La Tabla 48 reúne las señales observables sobre las que se apoyan estas mediciones.

**Tabla 48**

*Señales observables del sistema*

| **Señal observable** | **Origen** | **Uso experimental** |
| --- | --- | --- |
| Timestamps por tramo | Fuente, media, control y distribución. | Calculan latencias y verifican el dominio de reloj. |
| Unidades aceptadas, omitidas o descartadas | Control de ritmo, cola y fuente. | Interpretan cobertura temporal y pérdida de evidencia. |
| Eventos de percepción | Plano de medios. | Correlacionan percepción con fuente, modelo, prompt y unidad. |
| Huecos de secuencia | Bus ZeroMQ. | Detectan pérdida silenciosa y degradan la corrida. |
| Transiciones de patrón | Plano de control. | Reconstruyen persistencia, confirmación y resolución. |
| Alertas y re-alertas | Plano de control. | Delimitan episodios y estabilidad sin confundir repetición con FP. |
| Entregas y resultados de entrega | Distribución. | Separan entrega exitosa, supresión, duplicado y error. |
| Muestras de recursos | Entorno y soporte. | Explican cuellos de botella y diferencias entre corridas. |
| Errores y causas | Instrumentación transversal. | Evitan interpretar una corrida degradada como ausencia de riesgo. |

Cada métrica incluye un estado y una causa. Los estados admitidos son *computed*, *applicable_not_computed*, *not_applicable* y *not_interpretable*, y la plataforma no publica un cero cuando lo correcto es declarar una causa.

Una fuente de imágenes independientes produce not_applicable con causa *non_temporal_source* para los patrones temporales. Un trayecto con monotónicos de dos hosts produce not_interpretable con causa cross_node_monotonic_clock. Una corrida sin referencia anotada produce not_applicable con causa *no_ground_truth*. Y un tiempo hasta la primera detección sin evidencia positiva permanece nulo con su causa.

El reporte consolida el manifiesto, las configuraciones efectivas, las métricas por tramo, el estado de aplicabilidad, las alertas, las re-alertas, los descartes, los errores, los recursos y las limitaciones de interpretación, y cada valor mantiene la condición, el escenario y la población sobre la que se calculó.

El reporte constituye una proyección de hechos persistidos. Puede regenerarse sin modificar los eventos originales y no se utiliza como fuente de verdad cuando existe el artefacto primario.

#### 17.3.10. Escenarios experimentales y topología de referencia

La definición metodológica de ambos escenarios corresponde a la sección 17.1.4.2, y aquí se conservan únicamente sus consecuencias arquitectónicas. En DBE la fuente es regulable y puede releerse bajo la misma configuración, de modo que la arquitectura priorice identidad estable de unidades, orden lógico, persistencia previa y reconstrucción determinista de eventos, patrones y alertas. En EBE la fuente opera en vivo y la escena continúa evolucionando aunque el pipeline se retrase, de modo que la arquitectura instrumente captura o recepción, colas, descartes, jitter, actualidad y dominio de reloj. Ninguno de los dos es una topología física.

##### 17.3.10.1. Equivalencia arquitectónica y alcance de EBE

DBE y EBE convergen en la misma arquitectura una vez normalizada la entrada visual. La diferencia entre escenarios se ubica antes y alrededor de la disponibilidad del frame, en el origen de la fuente, la referencia temporal, la política de muestreo, el control de ritmo y la instrumentación de omisiones o descartes. Después de esa frontera, la inferencia OVD, el postproceso, la publicación de evidencia perceptiva, la evaluación de patrones y el registro de alertas internas mantienen la misma semántica.

La equivalencia evita construir dos flujos incompatibles, cuyos resultados dejarían de ser comparables. Al conservar la misma estructura de eventos, métricas y hechos persistibles, la arquitectura permite distinguir qué parte de la variación proviene de la fuente continua y qué parte del detector o de la evaluación de patrones.

La comparación entre escenarios declara explícitamente qué variables cambiaron. Una corrida DBE y una corrida EBE pueden compartir modelo, prompts, umbrales y reglas de patrón y diferir en fuente, temporización, iluminación, compresión o criterio de descarte, y esas diferencias se registran como parte de la configuración y de la observabilidad.

EBE admite cámaras IP por RTSP, la OAK-D Pro PoE y otras fuentes continuas declaradas mediante el mismo adaptador conceptual. La arquitectura contempla tanto el dispositivo candidato como la contingencia con cámara IP convencional, y ninguna alternativa modifica los contratos de percepción y control.

El rol de captura puede operar como ingesta, preprocesamiento no semántico o preselección conservadora. La variante de preselección liviana en el borde es opcional, está deshabilitada por defecto y opera con el criterio de degradación segura fijado para las capacidades opcionales del plano de medios, de modo que una falla o una incertidumbre del preselector no elimine la unidad del flujo principal. Toda transformación, descarte o cambio de resolución se registra.

La comparación entre una corrida DBE sobre archivo y una corrida EBE del mismo contenido exige un ancla común entre el tiempo de medio y el reloj de pared. Sin ese ancla, el matching temporal contra la referencia anotada se declara no interpretable, mientras que la integridad del bus y la relectura offline continúan siendo evaluables por separado. La Tabla 49 reúne las condiciones que cada corrida EBE debe registrar para que sus resultados sean interpretables.

**Tabla 49**

*Condiciones observables para interpretar EBE*

| **Condición** | **Registro mínimo** | **Impacto** |
| --- | --- | --- |
| Fuente continua | Tipo de cámara o stream, adaptador, source_id y naturaleza temporal. | Distingue captura local, red y participación del EN. |
| Conectividad y transporte | LAN, RTSP u otro mecanismo, codificación y buffering. | Condiciona jitter, atraso y disponibilidad de frames. |
| Timestamps y reloj | Captura, recepción, dequeue y dominio de reloj. | Determina qué latencias son calculables o interpretables. |
| Colas y control de ritmo | Tamaño, profundidad, reemplazos y política de actualidad. | Explica acumulación de atraso, pérdida de continuidad y capacidad de sostener el ritmo. |
| Descartes | Cantidad, causa y unidad afectada. | Evita confundir omisión del pipeline con ausencia de evidencia. |
| Preselección en el borde | Estado de habilitación, criterio, comportamiento fail-open y ledger de decisiones. | Permite comparar preselección contra flujo completo sin ocultar falsos negativos. |
| Degradación | Cortes, jitter, saturación, reloj inválido o fuente irregular. | Obliga a marcar métricas limitadas o no interpretables. |

##### 17.3.10.2. Naturaleza temporal de la fuente y aplicabilidad

La procedencia DBE o EBE no determina por sí sola si una fuente sostiene razonamiento temporal. Un video de archivo y un stream en vivo son temporales, mientras que un conjunto de imágenes independientes no lo es. La configuración deriva esta propiedad del tipo de fuente y no permite que el operador la contradiga.

Aplicar una ventana de persistencia sobre imágenes independientes produciría cero alertas por construcción, un resultado indistinguible de la ausencia real de riesgo. Para evitar ese cero silencioso, la evaluación de patrones se declara not_applicable/non_temporal_source. La corrida conserva valor para percepción y asociación espacial, pero no para continuidad o alerta temporal.

Las imágenes permiten afirmar sobre percepción. Los clips temporales permiten afirmar además sobre estado y episodios. Las fuentes en vivo permiten afirmar también sobre transporte, actualidad y comportamiento operativo. Cada reporte limita sus conclusiones al régimen que la fuente permite observar.

##### 17.3.10.3. Roles funcionales y unidades desplegables de referencia

La topología de referencia materializa los roles funcionales establecidos en la sección 17.1.4.1 y ubica en ella al módulo de distribución. Ninguno de los roles equivale necesariamente a una máquina dedicada, y la distribución física de los componentes no forma parte del compromiso conceptual del diseño.

La topología dispone un nodo de borde para captura y un nodo central con GPU para procesamiento. El nodo de entrenamiento permanece fuera del camino operativo de inferencia, porque cualquier adaptación produce un checkpoint candidato que se evalúa después sobre el nodo central y se mantiene como rama comparativa separada. El módulo de distribución se modela como una unidad desplegable propia, gobernada por su propia interfaz de gobierno y consumidora del bus de alertas, y puede co-ubicarse con el nodo central o separarse sin modificar los contratos de alerta interna, notificación y entrega. La Tabla 50 fija la correspondencia entre roles y unidades desplegables. Las métricas se atribuyen al rol y al despliegue efectivamente declarados en la corrida, y no se extrapolan entre unidades desplegables distintas.

**Tabla 50**

*Correspondencia de diseño entre roles funcionales y unidades desplegables de referencia*

| **Rol o unidad desplegable** | **Materialización de referencia** | **Responsabilidades** |
| --- | --- | --- |
| EN (modo base de captura) | Nodo de captura o unidad de ejecución de borde, sin GPU requerida. | Ingesta, control de ritmo, timestamps, healthcheck y normalización no semántica. La preselección liviana es opcional, fail-open y deshabilitada por defecto. |
| CPN | Nodo central o unidad de ejecución con GPU. | Inferencia OVD, postproceso, publicación, evaluación de patrones, alertas internas, persistencia, observabilidad y reporte. |
| TN | Clúster Mendieta u otro recurso de entrenamiento separado. | Preparación de checkpoints de una rama comparativa bajo datos, protocolo y criterios de escalamiento predefinidos; no sustituye la evaluación sobre el CPN. |
| Módulo de distribución | Servicio gobernado por configuración con interfaz HTTP propia, co-ubicable con el CPN o desplegable por separado. | Consumo de la alerta interna desde el bus de alertas, política de notificación, ledger de idempotencia, entrega MQTT y registro del sobre de notificación y del resultado de entrega. |

#### 17.3.11. Riesgos, plan de materialización y cierre

Los riesgos arquitectónicos se formulan como modos de falla observables y se vinculan con una mitigación concreta. La arquitectura no presupone que una mitigación elimina el riesgo, sino que exige instrumentarlo y declarar su efecto sobre la interpretación de la corrida. La Tabla 51 reúne esos riesgos y sus mitigaciones de diseño.

**Tabla 51**

*Riesgos arquitectónicos y mitigaciones de diseño*

| **Riesgo arquitectónico** | **Mitigación de diseño** |
| --- | --- |
| Conflicto entre calidad perceptiva y cadencia. | Separar selección de modelo, densidad de procesamiento y patrón; medir percepción, G2A y capacidad de sostener el ritmo por configuración sin asumir que un único modelo satisface todos los objetivos. |
| Identidad de detección interpretada como identidad temporal. | Declarar detection_id local al frame; utilizar granularidad de escena o una identidad temporal válida para subject. |
| Pérdida silenciosa en publicador-suscriptor. | Persistir antes de publicar, transportar seq, contar huecos y degradar explícitamente la corrida. |
| Relojes incompatibles entre hosts. | Medir cada tramo en un único dominio o declarar not_interpretable/cross_node_monotonic_clock. |
| Fuente no temporal evaluada con patrones. | Derivar naturaleza temporal y declarar not_applicable/non_temporal_source en lugar de cero alertas. |
| Preselección en borde descarta evidencia. | Mantener la preselección liviana como variante opcional y fail-open, con ledger por unidad y comparación contra el flujo completo. |
| Notificación externa altera la métrica del sistema. | Registrar primero la alerta interna; ubicar cooldown, idempotencia y fallas en distribución. |
| Trazabilidad o privacidad insuficientes. | Conservar manifiesto, JSONL y procedencia; minimizar evidencia visual y controlar acceso y retención. |
| Extensiones desplazan el núcleo. | Separar condiciones configurables de nuevas familias de evaluadores y exigir que cada capacidad opcional se declare por corrida. |

El plan de materialización ordena dependencias de diseño y no reemplaza el registro de implementación. El núcleo se construye primero sobre DBE para estabilizar contratos, evidencia, patrones y reporte, y luego se incorporan EBE y las capacidades opcionales sin modificar la semántica del flujo base. La Tabla 52 fija el entregable arquitectónico de cada incremento y el criterio que permite decidir si es verificable. El estado alcanzado por el conjunto de los incrementos corresponde a la sección 17.4.

**Tabla 52**

*Plan de materialización del núcleo*

| **Incremento** | **Criterio de avance** |
| --- | --- |
| Manifiesto y configuración | Una corrida puede reconstruirse mediante experiment_id, configs efectivas y versiones. |
| Fuentes DBE | Imágenes y videos ingresan con identidad, orden y naturaleza temporal declarados. |
| Vocabulario E-IND | Cada detección se atribuye a prompt_set_id y al rol de la clase. |
| Adaptador OVD | El modelo puede sustituirse sin modificar el contrato de percepción. |
| Normalización y postproceso | Las detecciones conservan coordenadas originales, normalizadas y filtros declarados. |
| Persistencia y bus | El hecho se persiste antes de publicarse y toda pérdida resulta detectable. |
| Patrones CR-01/CR-02 | La configuración fija región, granularidad, severidad y ventanas en milisegundos. |
| Alertas internas | Cada episodio confirmado produce una alerta idempotente y auditable. |
| Observabilidad | Cada métrica declara tramo, reloj, unidad, status y cause. |
| Reporte | La salida puede regenerarse desde los artefactos primarios. |

La frontera de extensibilidad distingue tres clases de cambio. Una condición nueva del tipo «sujeto sin EPP» requiere una definición declarativa de patrón y vocabulario, sin modificar contratos ni reentrenar el modelo. Una familia relacional, zonal o de trayectoria requiere un evaluador nuevo en el plano de control. Un modelo, una fuente o un canal nuevos requieren sus respectivos adaptadores y mantienen estables los contratos centrales. Esa frontera evita presentar la extensibilidad open-vocabulary como una capacidad ilimitada, y el costo medido de incorporar extensiones se documenta en las secciones de implementación y evaluación.

El diseño define una plataforma experimental compuesta por el plano de medios, el plano de control, el soporte experimental y un tramo desacoplado de distribución, que protege la ruta crítica, separa la evidencia de su interpretación y conserva una cadena causal reconstruible desde la fuente hasta la entrega. La granularidad de escena y la granularidad de sujeto se tratan como configuraciones semánticamente distintas, y la identidad personal permanece fuera del alcance.

El capítulo deja preparado el paso a la implementación. La sección 17.4 documenta qué componentes se materializaron y cómo se verificaron, y la sección 17.5 concentra las mediciones y su interpretación experimental.
