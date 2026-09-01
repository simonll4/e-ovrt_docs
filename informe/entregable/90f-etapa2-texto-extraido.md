# 90f — Texto extraído del documento de trabajo: §17.1 Consolidación Metodológica (v1.7, pase 6 de desacople normativo aplicado)

> **Extracción derivada (2026-09-01)** del `.docx`
> `informe/entregable/E-OVRT-VDP_Seccion_17.1_Consolidacion_Metodologica_v1.7.docx`, **solo para búsqueda y cita**
> (mismo estatuto que el doc 90): al editar, se edita el `.docx`/Google Docs, nunca
> este archivo. Tablas y figuras pueden haber perdido formato; las figuras no se
> extraen y las ecuaciones no se convierten — quedan `⟦FIGURA: no extraída — ver el .docx⟧` y
> `⟦ECUACIÓN: no extraída — ver el .docx⟧` donde estaban. Regenerado con
> `herramientas/extraer_informe.py` (regla D-C del manual de aplicación).

---

### 17.1. Consolidación metodológica del protocolo experimental

La consolidación metodológica transforma el marco teórico construido previamente en un protocolo experimental utilizable. Para ello fija decisiones sobre alcance, escenarios, infraestructura, datos, prompts, métricas y criterios de aceptación, integrando los desarrollos metodológicos en una secuencia coherente con el objetivo del prototipo experimental.

El referente experimental resultante delimita qué condiciones de riesgo integran el núcleo del prototipo, cómo se estructuran los escenarios de evaluación, con qué reglas se gestionan los datos, qué métricas deben producirse y cómo debe interpretarse la evidencia obtenida.

Esta instancia no implementa el pipeline ni reporta resultados empíricos. Establece las condiciones de comparabilidad, medición e interpretación necesarias para que el prototipo pueda desarrollarse y evaluarse sobre bases explícitas, trazables y defendibles.

#### 17.1.1. Función y alcance de la consolidación metodológica

El criterio rector prioriza la validez experimental, la trazabilidad y la correspondencia entre alcance, datos disponibles e instrumentación efectiva. El núcleo obligatorio del prototipo se ubica en las condiciones de Nivel 1 —CR-01 y CR-02—, donde convergen observabilidad visual, cobertura de datos, estrategias de evaluación defendibles y métricas aplicables con el hardware disponible; las condiciones de Niveles 2 y 3 se conservan como extensiones condicionadas, debido a brechas de datos, visibilidad y razonamiento contextual.

A partir de ese criterio se fija una secuencia experimental integrada —comparación primaria en Dataset-Based Evaluation (DBE), validación complementaria en Environment-Based Evaluation (EBE), reglas de partición sin leakage, política de formulación y congelamiento de prompts, jerarquía de métricas orientada al valor operativo de alerta y criterios para habilitar una rama comparativa de fine-tuning—, organizada sobre cuatro dimensiones temáticas: el entorno experimental, las condiciones de riesgo y su protocolo de prompts, la estrategia de datos y el framework de métricas.

#### 17.1.2. Alcance experimental consolidado del prototipo

##### 17.1.2.1. Delimitación del catálogo de condiciones de riesgo

El catálogo retenido comprende seis condiciones de riesgo organizadas en tres niveles de complejidad. La decisión principal es distinguir entre el catálogo metodológico completo y el núcleo obligatorio de validación: CR-01 y CR-02 constituyen el plano mínimo del prototipo, porque son condiciones de detección directa de Nivel 1 cuya relevancia preventiva, observabilidad y evaluabilidad están fundamentadas en la sección 16.2.

Esa priorización se justifica porque ambas reúnen observabilidad visual relativa, estrategias de detección directa o indirecta ya definidas, cobertura de datos suficiente y métricas aplicables sin depender de módulos todavía no implementados. CR-03 y CR-04 conservan relevancia, pero dependen de visibilidad fina, ausencia visual y datos complementarios; CR-05 y CR-06 orientan la arquitectura relacional, aunque su evaluación completa requiere persistencia temporal, regiones externas o razonamiento contextual. Esta cautela es consistente con la evidencia sobre dificultades de los modelos OVD ante atributos finos y dominios especializados de construcción (Bianchi et al., 2024; Abdalwhab et al., 2025).

##### 17.1.2.2. Núcleo obligatorio y extensiones condicionadas

La distinción entre núcleo obligatorio y extensión condicionada no elimina condiciones del catálogo. Explicita el nivel de compromiso que esta instancia puede sostener con los datos, la instrumentación y la complejidad disponible. En consecuencia, la aceptación mínima del prototipo no depende de un desempeño uniforme sobre las seis condiciones, sino de demostrar funcionamiento defendible sobre el núcleo obligatorio y de producir evidencia parcial o exploratoria sobre las extensiones condicionadas cuando la arquitectura y los datos lo permitan.

El catálogo completo conserva valor directivo, pero la validación se concentra en aquello que puede medirse con rigor. Esta decisión permite preservar la coherencia entre objetivo experimental, cobertura de datos, complejidad técnica y capacidad real de instrumentación. El catálogo completo, con su tipo de condición, componente evaluador y dificultad estimada, se presenta en la Tabla 20 (Sección 17.1.5.2.3).

#### 17.1.3. Diseño metodológico general y lógica de escenarios

##### 17.1.3.1. Patrón de riesgo como unidad de análisis

El protocolo adopta como unidad de análisis el patrón de riesgo confirmado y no la detección aislada. Esta decisión evita reducir el problema a la mera producción de cajas por cuadro. En el proyecto, la condición de riesgo constituye la unidad semántica de entrada; el patrón de riesgo incorpora severidad, persistencia y, cuando corresponde, relaciones espaciales o temporales; y la alerta constituye la salida operativa trazable del sistema. Esta distinción ordena la relación entre detector, tracker, lógica contextual y backend de eventos.

##### 17.1.3.2. Cadena operativa mínima y motor de patrones

A partir de esa unidad de análisis, el protocolo asume una cadena operativa mínima entre percepción, evaluación y respuesta asistiva. En dicha cadena, las detecciones producidas por el modelo OVD funcionan como evidencia primaria, pero no constituyen por sí mismas una alerta. Para que una alerta sea considerada válida dentro del sistema, la evidencia debe ser agrupada, evaluada y confirmada como patrón de riesgo según los criterios definidos para cada condición.

En términos operativos, esta evaluación corresponde al motor de patrones, entendido como una abstracción lógica del plano de control que aplica criterios de persistencia, severidad, histéresis y lógica espacial o contextual sobre los eventos de detección. Sólo cuando un patrón alcanza el estado confirmado puede registrarse una alerta interna dentro del sistema; su operacionalización se desarrolla en la Sección 17.1.5.3.4.

##### 17.1.3.3. Escenarios de evaluación

Sobre esa base, la evaluación se organiza en dos escenarios complementarios —el Escenario A o Dataset-Based Evaluation (DBE), ámbito primario de comparación controlada y repetible, y el Escenario B o Environment-Based Evaluation (EBE), validación de plausibilidad operativa sobre captura continua—, cuya relación no es de reemplazo; su caracterización completa se desarrolla en la Sección 17.1.4.4.

La secuencia de pruebas se estructura de manera progresiva. Parte de una condición base controlada, continúa con barridos univariados o de baja combinación sobre la configuración retenida y culmina con una prueba de mayor exigencia aplicada a la mejor configuración disponible. Este esquema permite acotar la complejidad experimental, evitar un diseño factorial inmanejable y, al mismo tiempo, conservar capacidad analítica para observar la sensibilidad del sistema frente a variables relevantes.

##### 17.1.3.4. Decisiones estructurales del diseño metodológico

**Tabla 16**

*Decisiones estructurales del diseño metodológico*

| **Decisión** | **Formulación adoptada** | **Implicación para el protocolo** |
| --- | --- | --- |
| Unidad de análisis | Patrón de riesgo confirmado y alerta asociada, no detección aislada. | Obliga a medir persistencia, tiempo de respuesta y estabilidad además de precisión de detección. |
| Cadena operativa mínima | Detección OVD, evento de detección, evaluación de patrón, patrón confirmado, alerta registrada, disponibilidad para consulta o notificación, e interpretación humana. | Conecta la evidencia perceptiva con una salida operativa trazable y evita tratar la alerta como una detección aislada. |
| Motor de patrones | Abstracción lógica del plano de control que evalúa eventos de detección, trayectorias cuando existan y configuración de patrones contra reglas de persistencia, severidad, histéresis y lógica espacial o contextual. | Define dónde se transforma la evidencia perceptiva en patrón candidato, confirmado o resuelto, y evita tratar la alerta como salida directa del detector OVD. |
| Carácter asistivo de la alerta | La alerta informa un patrón de riesgo confirmado según los criterios operativos del prototipo, pero no sustituye la decisión del supervisor humano. | Preserva el alcance experimental, ético y operativo del prototipo. |
| Escenario primario | DBE sobre datasets y benchmarks retenidos. | Asegura comparabilidad, control de variables y repetibilidad de las mediciones. |
| Escenario complementario | EBE en entorno simulado o controlado. | Permite observar el comportamiento del pipeline sobre captura continua y variables visuales realistas. |
| Baseline obligatoria | Toda variante se mide primero en zero-shot. | Protege la comparación entre modelos y evita atribuir al ajuste mejoras que dependen de cambios de evaluación. |
| Comparación entre variantes | Fine-tuning sólo cuando existe soporte metodológico suficiente. | Evita convertir la adaptación al dominio en supuesto previo de viabilidad. |

*Nota.* DBE = Dataset-Based Evaluation. EBE = Environment-Based Evaluation. La baseline zero-shot constituye la referencia mínima a partir de la cual recién puede discutirse el valor de prompts, seguimiento o fine-tuning. La cadena operativa mínima fija el recorrido lógico de la alerta dentro del protocolo experimental. El motor de patrones explicita el componente lógico que transforma evidencia perceptiva en patrón confirmado y opera como criterio de diseño para su instrumentación arquitectónica posterior.

#### 17.1.4. Entorno experimental, infraestructura y escenarios de evaluación

##### 17.1.4.1. Introducción y alcance

El entorno experimental comprende la infraestructura de cómputo disponible para inferencia y entrenamiento, el stack de software asociado, los escenarios de evaluación definidos para el proyecto y las condiciones operativas propias de cada escenario. Su caracterización responde a la pregunta rectora P-E1-04 de la fundamentación teórica: las restricciones del entorno de ejecución —capacidad computacional, protocolos de transmisión y presupuesto de procesamiento— que condicionan las decisiones arquitectónicas del prototipo. Los escenarios de evaluación establecen, además, las condiciones concretas bajo las cuales se ejercita el prototipo.

##### 17.1.4.2. Infraestructura de evaluación

La infraestructura de evaluación se organiza a partir de nodos funcionales. En este trabajo, un nodo representa un rol dentro del entorno experimental: procesamiento central, captura en borde o entrenamiento/adaptación de modelos. Cada rol puede materializarse mediante uno o más dispositivos concretos según la disponibilidad, el escenario de evaluación y la configuración efectiva de la corrida.

Bajo este criterio, el Central Processing Node (CPN) concentra la ejecución del pipeline principal, la inferencia, la evaluación de patrones, la medición de latencia y la consolidación de resultados experimentales. El Edge Node (EN) se ubica próximo a la fuente visual y se orienta a captura, transmisión de video y eventual preprocesamiento liviano. El Training Node (TN), cuando corresponda, se reserva para tareas de ajuste o preparación de variantes de modelo, sin sustituir la evaluación operativa sobre el CPN. Las conclusiones sobre viabilidad operativa —tiempo real, latencia y uso de recursos— se anclan en el CPN.

###### 17.1.4.2.1. Central Processing Node (CPN)

El CPN concentra la lectura o recepción de cuadros, la inferencia open-vocabulary, el postproceso, la evaluación de patrones, el registro de alertas internas y la instrumentación técnica y operativa.

Este rol se materializa sobre una laptop HP Victus 15 Gaming 15-FB2024LA con GPU NVIDIA GeForce RTX 4060 Laptop y 8 GB de VRAM, recurso que delimita el tamaño de modelo, la resolución de inferencia, la precisión numérica y el presupuesto de latencia. El entorno de ejecución adoptado es Linux mediante WSL2 sobre el equipo descrito y contenedores Linux, por compatibilidad con el stack de inferencia y el bus de datos (HP Inc., s. f.).

Las especificaciones completas del CPN y del entorno de software se presentan en las Tablas B.1 y B.3 del Anexo B.

El stack del CPN debe ser compatible con los frameworks oficiales de Grounding DINO y YOLOE, con aceleración sobre GPU NVIDIA y con rutas reproducibles de inferencia. Las librerías, versiones y runtimes candidatos se documentan en la Tabla B.3 del Anexo B (Liu et al., 2023; Wang et al., 2025).

###### 17.1.4.2.2. Implicancias del NVDEC para el pipeline de medios

La decodificación acelerada mediante NVDEC se conserva como alternativa del protocolo para flujos H.264 o H.265 del EBE. Su eventual uso debe declararse por corrida y contrastarse con la decodificación por software, porque modifica el reparto de carga entre CPU y GPU y, por lo tanto, la interpretación del presupuesto temporal (NVIDIA Corporation, s. f.-b).

###### 17.1.4.2.3. Edge Node (EN) y dispositivo de captura candidato

El EN cumple la función de captura, recepción o transmisión de video hacia el CPN, según la topología definida para cada corrida. Dentro del núcleo experimental, su responsabilidad se limita a captura, transmisión y, eventualmente, preprocesamiento liviano. La inferencia open-vocabulary en borde no forma parte del flujo base; su eventual incorporación corresponde a una variante condicionada, sujeta a medición independiente.

El protocolo contempla dos fuentes integrables para este rol: una cámara IP mediante RTSP y la cámara Luxonis OAK-D Pro PoE mediante su interfaz de captura. La vía RTSP se prioriza inicialmente por disponibilidad e interoperabilidad; la OAK-D se incorpora como fuente posterior para capturas controladas y capacidades sensoriales complementarias. Ninguna de las dos decisiones presupone inferencia OVD en el borde (Luxonis, s. f.-a, s. f.-b).

Ambas fuentes deben producir unidades visuales comparables para el CPN y registrar su procedencia, resolución, tasa de captura y temporalidad. La elección entre ellas depende del escenario y no altera la unidad de evaluación del protocolo.

Las especificaciones del dispositivo de captura y su conectividad se detallan en la Tabla B.2 del Anexo B.

##### 17.1.4.3. Adaptación de modelos al dominio

Los modelos OVD candidatos se evalúan tanto en su variante preentrenada (baseline zero-shot) como en una variante ajustada mediante fine-tuning supervisado sobre datos del dominio de construcción o similar. El fine-tuning es un proceso preparatorio previo a la ejecución de los escenarios de evaluación; los pesos resultantes se transfieren al CPN para su evaluación bajo las mismas condiciones de hardware, garantizando una comparación justa.

La incorporación del fine-tuning como experimento comparativo responde a la pregunta rectora P-E1-08. El alcance del prototipo experimental excluye el entrenamiento desde cero; el fine-tuning supervisado sobre un subconjunto acotado de datos del dominio es una forma de adaptación compatible con esta restricción.

El TN se materializa mediante el clúster institucional Mendieta del CCAD-UNC, reservado para preparación y ajuste de variantes. Su capacidad no sustituye la evaluación operativa sobre el CPN; las especificaciones del recurso se presentan en la Tabla B.4 del Anexo B (Centro de Computación de Alto Desempeño, 2026).

El entorno del TN debe permitir preparación de datos, entrenamiento reproducible, conservación de checkpoints y exportación hacia el runtime del CPN. La configuración candidata se resume en la Tabla B.5 del Anexo B.

El TN queda fuera del camino de inferencia evaluado. Prepara variantes sobre particiones previamente definidas, exporta los checkpoints en un formato compatible y entrega esos artefactos al CPN, donde deben compararse con la baseline bajo el mismo material y la misma configuración experimental, salvo la variable aislada.

##### 17.1.4.4. Escenarios de evaluación

Se definen dos escenarios de evaluación complementarios. El primero permite la evaluación controlada y reproducible del pipeline mediante datasets de referencia públicos; el segundo expone el sistema a condiciones visuales representativas del dominio real mediante video en tiempo real captado en un entorno físico. Ambos escenarios son necesarios dado que el primero habilita la comparación cuantitativa entre variantes de modelo y, cuando el dataset y el protocolo lo permitan, el contraste con métricas reportadas en la literatura, mientras que el segundo valida la viabilidad operativa bajo condiciones que ningún dataset puede replicar completamente. En ambos escenarios, la evaluación contempla la ejecución de los modelos preentrenados (baseline) y, cuando una variante ajustada haya sido adoptada conforme a las condiciones de la Sección 17.1.9, de los modelos ajustados mediante fine-tuning en el TN, permitiendo una comparación directa del impacto de la adaptación al dominio.

###### 17.1.4.4.1. Escenario A - Dataset-Based Evaluation (DBE)

En este escenario el pipeline procesa material de imagen o video proveniente de datasets públicos de referencia. La ausencia de condiciones en tiempo real permite reproducibilidad exacta, aislamiento de variables y, cuando el dataset y el protocolo de evaluación coincidan con los de la fuente de referencia, contraste con métricas reportadas en la literatura. Constituye el escenario primario para la evaluación cuantitativa de los componentes OVD y MOT del pipeline, tanto en su variante preentrenada como en la variante ajustada por fine-tuning. Los datasets candidatos se documentan en la estrategia de datos, benchmarks y partición.

**Tabla 17**

*Características del Escenario A - Dataset-Based Evaluation (DBE)*

| **Aspecto** | **Descripción** |
| --- | --- |
| Tipo de entrada | Imágenes y secuencias de video provenientes de datasets anotados |
| Fuente | Colección de datasets candidatos (la estrategia de datos, benchmarks y partición) |
| Nodo de ejecución | CPN para toda la inferencia y evaluación |
| Modelos evaluados | Variante preentrenada (baseline) y variante fine-tuned, cuando aplique, para los modelos candidatos seleccionados |
| Conectividad | No aplica; procesamiento off-line sobre archivos locales |
| Ventaja principal | Reproducibilidad exacta; comparación directa con benchmarks de la literatura; aislamiento del efecto del fine-tuning |
| Limitación principal | Existen datasets públicos de construcción civil para detección, pero no benchmarks del dominio con seguimiento anotado; la evaluación MOT requiere benchmarks generales complementarios y un protocolo propio de transferencia al dominio. |

###### 17.1.4.4.2. Escenario B - Environment-Based Evaluation (EBE)

En este escenario el pipeline opera sobre video en tiempo real captado en un espacio de obra simulado. Este escenario valida la viabilidad operativa del sistema bajo condiciones visuales y de conectividad representativas del dominio real, incluyendo variaciones de iluminación, oclusiones y densidad de personas en escena. A diferencia del Escenario A, el pipeline se ejercita de extremo a extremo, incluyendo las etapas de captura y transporte de video, y permite evaluar el comportamiento del motor de razonamiento temporal bajo condiciones de operación continua. Al igual que en el Escenario A, se ejecuta la variante preentrenada y, cuando haya sido adoptada conforme a la Sección 17.1.9, la variante fine-tuned del modelo candidato seleccionado tras la evaluación del Escenario A. Las variables de sensibilidad candidatas para este escenario se catalogan en la Tabla C.2 del Anexo C.

**Tabla 18**

*Características del Escenario B - Environment-Based Evaluation (EBE)*

| **Aspecto** | **Descripción** |
| --- | --- |
| Tipo de entrada | Video en vivo desde el EN mediante cámara IP por RTSP o captura directa con OAK-D Pro PoE. La fuente RTSP sintética se reserva para desarrollo y reproducibilidad. |
| Espacio físico | Espacio de obra simulado. |
| Participantes | Personas reales portando EPP (casco, chaleco reflectante, entre otros); configuración de escenas con y sin las condiciones observables objetivo. |
| Condiciones visuales | Variables según la configuración de prueba prevista para la validación experimental, definidas en función del diseño experimental del escenario y de las condiciones operativas que se establezcan para su evaluación. |
| Nodo de ejecución | CPN para inferencia central; EN para captura y, sólo como variante condicionada, preprocesamiento liviano. |
| Modelos evaluados | Variante preentrenada (baseline) y, cuando corresponda conforme a la Sección 17.1.9, variante fine-tuned, sobre el modelo o combinación seleccionada tras el Escenario A. |
| Conectividad | Red LAN. |
| Ventaja principal | Validación operativa bajo condiciones del dominio; ejercita el pipeline completo de extremo a extremo incluyendo transporte de video y motor de razonamiento temporal. |
| Limitación principal | Menor reproducibilidad que el Escenario A; requiere gestión de consentimiento informado e información previa a los participantes, conforme a las salvaguardas de la Sección 17.1.10.1. |

##### 17.1.4.5. Parámetros operativos de referencia

Los parámetros operativos de referencia establecen una base inicial para orientar la evaluación del pipeline experimental. No constituyen valores definitivos de configuración, sino condiciones de partida que permiten delimitar resolución, tasa de cuadros, modalidad de transporte, procesamiento esperado y restricciones generales de ejecución. Su función es ofrecer un marco común para comparar pruebas posteriores y evitar que cada experimento se defina de manera aislada.

Los parámetros operativos se documentan por perfil. En particular, la resolución de inferencia es un parámetro del perfil de modelo y debe fijarse junto con los umbrales recalibrados para ese perfil; no se adopta una resolución única para todas las familias. Los restantes valores orientativos se presentan en la Tabla B.6 del Anexo B.

En el EBE, la captura y el procesamiento pueden ubicarse en nodos distintos. El protocolo exige declarar fuente, transporte, buffering y anclas temporales para distinguir la latencia de adquisición de la latencia algorítmica. La topología de referencia se presenta en la Tabla B.7 del Anexo B.

##### 17.1.4.6. Restricciones y condicionantes del entorno experimental

Las restricciones detalladas en la Tabla 19 condicionan las decisiones del diseño arquitectónico y de la implementación, y deben tenerse presentes al interpretar los resultados experimentales.

**Tabla 19**

*Restricciones y condicionantes del entorno experimental*

| **Restricción** | **Origen** | **Implicación para el diseño** |
| --- | --- | --- |
| VRAM de 8 GB en el CPN | Hardware — RTX 4060 Laptop (8 GB VRAM) | Limita el tamaño de los modelos ejecutables sin cuantización y condiciona la resolución de entrada, el batch efectivo y la elección de runtime en inferencia. |
| Capacidad de inferencia del EN limitada a 1.4 TOPS para AI | Hardware — OAK-D Pro PoE / RVC2 | Restringe la complejidad de los modelos que pueden ejecutarse localmente; el uso del EN debe considerarse, en principio, para captura inteligente, preprocesamiento o inferencia ligera en borde. |
| Linux mediante WSL2 y contenedores Linux en el CPN | Entorno de ejecución — CPN | Las versiones de CUDA, bibliotecas, runtimes y bus deben ser compatibles con el entorno Linux adoptado y quedar congeladas por corrida. |
| Cobertura limitada del dominio para evaluación de seguimiento | Datasets públicos analizados en la estrategia de datos, benchmarks y partición | La evaluación MOT requiere benchmarks generales complementarios y la formalización de un protocolo de transferencia al dominio, dado que la cobertura específica del dominio para seguimiento anotado es insuficiente. |
| Presupuesto de latencia por cuadro, desde la captura hasta la evidencia utilizable para alerta, del orden de 35–250 ms | El framework de métricas (Sección 17.1.7.7) | Condiciona la selección de modelos, la resolución de entrada y la configuración de runtimes. |
| Acceso al clúster sujeto a disponibilidad institucional del recurso | Infraestructura institucional — CCAD-UNC | La planificación del ajuste debe contemplar la cola institucional, sin convertir la disponibilidad de cómputo en criterio metodológico de aceptación o descarte. |
| Necesidad de split train/eval disjunto | Principio metodológico | Los datos utilizados para fine-tuning no pueden formar parte del conjunto de evaluación. La partición debe documentarse explícitamente. |
| Recaudos ético-legales en el Escenario B | Criterios ético-legales de la sección 16.6 | Las pruebas con personas en el campo visual requieren consentimiento informado e información previa, finalidad explícita, minimización, acceso restringido y retención acotada, conforme a la Sección 17.1.10.1. |

*Nota.* Elaboración propia basada en las especificaciones del hardware disponible, la caracterización del TN y del EN en la presente sección, los criterios metodológicos fijados en la estrategia de datos, benchmarks y partición y los criterios ético-legales establecidos en la sección 16.6 y operacionalizados en la Sección 17.1.10.1.

#### 17.1.5. Condiciones de riesgo, patrones y protocolo de prompts

##### 17.1.5.1. Introducción y alcance

La taxonomía de condiciones de riesgo, los patrones asociados y el protocolo de prompts responden a la pregunta rectora P-E1-02, que dejó abierta la brecha entre la identificación de condiciones de riesgo preventivamente relevantes y su traducción en consultas textuales evaluables por modelos de detección open-vocabulary, y señaló que la formulación del prompt no es un detalle accesorio sino una variable capaz de alterar significativamente el desempeño del detector en dominios especializados. En articulación con el framework de métricas, se delimita además cómo estas definiciones deben leerse respecto de la latencia de alerta, las métricas operativas y los criterios de aplicación del framework evaluativo.

El alcance es metodológico: establece qué condiciones deben detectarse, cómo se agrupan en patrones de riesgo, con qué severidad conceptual y criterios analíticos de persistencia se interpretan, y con qué formulaciones textuales se evaluarán. Además, incorpora una operacionalización preliminar del motor de patrones como componente lógico responsable de transformar detecciones y trayectorias en patrones candidatos, confirmados o resueltos. Esta definición no constituye todavía una implementación de software ni fija contratos técnicos finales, pero sí delimita la estructura mínima de ejecución que deberá materializarse en la instancia de análisis y diseño arquitectónico. Los umbrales cuantitativos finales de aceptación y la calibración empírica de ventanas, reglas e histéresis corresponden al framework de métricas y a la validación experimental.

##### 17.1.5.2. Taxonomía de condiciones de riesgo para el prototipo

El primer paso consiste en delimitar el subconjunto de condiciones de riesgo que el prototipo experimental debe ser capaz de detectar. Para ello se explicitan los criterios de selección aplicados sobre el universo relevado en la fundamentación teórica, se presenta la clasificación en tres niveles de complejidad según las capacidades del sistema requeridas para su evaluación y, finalmente, se consolida el catálogo de condiciones seleccionadas junto con sus consideraciones de evaluabilidad. El resultado constituye el insumo directo tanto para la definición de patrones de riesgo como para el diseño de prompts OVD.

###### 17.1.5.2.1. Criterios de selección del subconjunto del prototipo experimental

La fundamentación teórica delimita las condiciones de riesgo observables por su relevancia preventiva, su evidencia visual anotable y su formulación evaluable (sección 16.2), y señala como posibles extensiones situaciones como el trabajo en altura, las zonas restringidas o la interacción con maquinaria. El prototipo experimental no pretende cubrir ese espacio de manera exhaustiva, sino seleccionar un subconjunto acotado que permita demostrar la viabilidad técnica del concepto. Con ese fin se aplican tres criterios de selección, calibrados a las restricciones reales de recursos y al contexto académico del proyecto.

**Representatividad de niveles de complejidad**. El subconjunto debe incluir al menos una condición de cada nivel de complejidad definido en la clasificación de la sección 17.1.5.2.2, de modo que la evaluación ejercite las capacidades del pipeline en sus distintas configuraciones. Este criterio es viable porque los niveles corresponden a capacidades del sistema que deben evaluarse independientemente de la cantidad de condiciones seleccionadas.

**Factibilidad de detección visual**. Las condiciones seleccionadas deben tener correlatos visuales suficientemente diferenciados como para ser evaluables mediante análisis de imagen en las resoluciones y ángulos de cámara típicos de un entorno de laboratorio o simulado. Esto excluye condiciones cuya manifestación visual depende de detalles de difícil resolución (por ejemplo, la distinción entre calzado de seguridad y calzado común), así como condiciones sin correlato visual directo (por ejemplo, “capacitación insuficiente” o “plan de seguridad no elaborado”). La exclusión deliberada de condiciones de baja observabilidad evita comprometer la validez de los resultados experimentales del prototipo con limitaciones ajenas al sistema.

**Viabilidad de evaluación con recursos disponibles**. Las condiciones seleccionadas deben poder evaluarse con alguna combinación de datasets públicos existentes, subconjuntos anotados de los mismos o datos generados en entorno controlado, sin exigir campañas extensivas de recolección o anotación incompatibles con un proyecto académico. Este criterio no presupone cobertura perfecta desde el inicio, pero sí exige que la brecha entre lo disponible y lo necesario sea acotada y metodológicamente manejable.

###### 17.1.5.2.2. Clasificación por niveles de complejidad

La clasificación de las condiciones de riesgo en tres niveles de complejidad responde a una distinción funcional sobre las capacidades que el sistema debe desplegar para evaluarlas. Esta tipología tiene consecuencias directas tanto sobre la arquitectura del pipeline como sobre el protocolo de evaluación aplicable a cada condición.

**Condiciones de Nivel 1: Entidad simple.** Involucran la detección de un único objeto o atributo sobre una entidad. Su evaluación es resoluble, en principio, mediante una única consulta OVD sobre un cuadro individual, sin requerir información temporal ni relacional. Un ejemplo representativo es la detección de casco de seguridad sobre una persona, donde el modelo OVD recibe un prompt como “person with hard hat” o “hard hat” y debe localizar las instancias correspondientes en la imagen. La evaluación de la condición de riesgo asociada (presencia o ausencia del EPP) admite dos estrategias diferenciadas que se analizan en la Sección 17.1.5.4.

**Condiciones de Nivel 2: Entidad con atributo contextual.** Estas involucran entidades sobre las cuales debe verificarse un atributo que depende de información espacial dentro del mismo cuadro. A diferencia del Nivel 1, la condición no se reduce a la detección aislada de un objeto, sino que requiere evaluar la relación espacial entre la entidad y su contexto visual inmediato. Un ejemplo es la presencia de una persona sobre una estructura elevada (andamio, plataforma), donde el modelo OVD puede detectar individualmente a la persona y a la estructura, pero la determinación de que la persona se encuentra sobre la estructura requiere un análisis de las relaciones geométricas entre las detecciones, como la superposición vertical de bounding boxes.

Este análisis puede implementarse mediante lógica de post-detección que opere sobre las salidas del modelo en el mismo cuadro, por ejemplo a través de reglas geométricas de solapamiento, proximidad o posicionamiento relativo entre regiones detectadas. A diferencia del Nivel 3, este tipo de condición no exige aún persistencia temporal ni mantenimiento de identidad entre cuadros, pero sí introduce una capa adicional de razonamiento espacial intracuadro.

**Condiciones de Nivel 3: Relación entre entidades.** Por último, estas condiciones involucran dos o más entidades independientes cuya co-ocurrencia espacial o temporal constituye la condición de riesgo. Estas condiciones exceden la capacidad del detector OVD operando cuadro a cuadro, ya que requieren tanto la detección individual de cada entidad como un módulo de razonamiento que evalúe relaciones geométricas entre ellas (distancia, contención) y las estabilice temporalmente. El tracker MOT interviene en este nivel para preservar la identidad de cada objeto rastreado a lo largo de los cuadros consecutivos que abarca el intervalo de evaluación. Un ejemplo es la co-ocurrencia de maquinaria pesada y peatones por debajo de una distancia de seguridad, donde ambas entidades son detectables individualmente por el OVD, pero la evaluación de proximidad peligrosa requiere calcular distancias entre detecciones y sostener esa evaluación durante un intervalo temporal.

###### 17.1.5.2.3. Catálogo de condiciones de riesgo seleccionadas

La Tabla 20 presenta las seis condiciones de riesgo seleccionadas para el prototipo experimental, organizadas por nivel de complejidad. Para cada condición se indica su código identificador, el tipo de condición, la descripción operativa, el componente del sistema responsable de su evaluación y una estimación cualitativa de la dificultad de detección OVD.

**Tabla 20**

*Catálogo de condiciones de riesgo seleccionadas para el prototipo experimental*

| **Código** | **Nivel** | **Tipo de condición** | **Condición de riesgo** | **Evidencia visual** | **Componente evaluador** | **Dificultad OVD estimada** |
| --- | --- | --- | --- | --- | --- | --- |
| CR-01 | 1 | EPP — casco | Persona sin casco de seguridad en zona de obra | Presencia o ausencia de casco en región cefálica de la persona | OVD cuadro a cuadro | Media |
| CR-02 | 1 | EPP — chaleco | Persona sin chaleco reflectivo en zona de tráfico o maquinaria | Presencia o ausencia de prenda de alta visibilidad en torso | OVD cuadro a cuadro | Media-Baja |
| CR-03 | 2 | Protección contra caídas | Persona en posición elevada sin sistema anticaídas visible | Persona sobre andamio o plataforma sin arnés o línea de vida visible | OVD + contexto espacial intracuadro | Alta |
| CR-04 | 2 | Protección contra caídas | Borde elevado desprotegido con personas próximas | Borde de plataforma o losa sin baranda o red perimetral, con presencia humana | OVD + contexto espacial intracuadro | Alta |
| CR-05 | 3 | Coexistencia peatón-maquinaria | Maquinaria en operación en proximidad a peatones sin separación | Co-ocurrencia de maquinaria pesada y personas por debajo de distancia de seguridad | OVD + MOT + razonamiento contextual | Media |
| CR-06 | 3 | Delimitación de áreas | Persona dentro de zona restringida o delimitada | Presencia de persona en área demarcada como prohibida o restringida | OVD + MOT + razonamiento contextual | Media |

*Nota.* La columna “Componente evaluador” indica qué módulos participan en la evaluación: “OVD cuadro a cuadro” (una o más consultas al detector por cuadro), “OVD + contexto espacial intracuadro” (relaciones geométricas entre detecciones del mismo cuadro) y “OVD + MOT + razonamiento contextual” (persistencia temporal de trayectorias y lógica relacional, cuyo diseño corresponde a la instancia de análisis y diseño arquitectónico). La columna “Dificultad OVD estimada” es una valoración cualitativa basada en la degradación documentada de los modelos OVD ante atributos de granularidad fina, en la discrepancia de distribución y vocabulario en dominios especializados y en el menor desempeño frente a detectores ajustados en entornos de construcción (Bianchi et al., 2024; Jiang et al., 2024; Abdalwhab et al., 2025); no pondera la dificultad del razonamiento contextual. CR-01 y CR-02 constituyen el núcleo obligatorio del prototipo experimental; las restantes condiciones operan como extensiones condicionadas que no bloquean la aceptación del núcleo.

###### 17.1.5.2.4. Consideraciones sobre evaluabilidad y limitaciones

La selección prioriza condiciones con alta observabilidad visual y disponibilidad plausible de datos de evaluación. Aun así, presenta particularidades que conviene explicitar.

La condición CR-04 —borde desprotegido— presenta dos particularidades relevantes. La primera concierne a la naturaleza negativa de la evidencia visual de la condición de riesgo. Dado que esta condición se define por la ausencia de un elemento de protección —baranda o red perimetral—, su evaluación resulta conceptualmente más exigente que en condiciones basadas en la presencia explícita de objetos. En este sentido, la literatura sobre percepción visual humana sugiere asimetrías entre juicios de presencia y ausencia, con respuestas más lentas y menor confianza ante ciertos juicios de ausencia; sin embargo, esta evidencia proviene de tareas perceptuales humanas y no de evaluación automática en visión por computadora, por lo que se invoca aquí únicamente como analogía metodológica (Mazor et al., 2021).

La segunda particularidad es geométrica: la determinación de si un borde es efectivamente elevado depende de información tridimensional que la proyección bidimensional de la cámara no preserva completamente. Por ello, la ambigüedad asociada a altura, profundidad, perspectiva y oclusión debe asumirse desde el diseño experimental.

La condición CR-03 también exige cautela. La evidencia visual relevante no es solo la presencia de una persona en altura, sino la ausencia visible de un sistema anticaídas, lo que depende fuertemente de la escala del objeto en imagen, el ángulo de cámara, la oclusión y la resolución disponible. En consecuencia, su dificultad no proviene únicamente del razonamiento espacial intracuadro, sino también de la visibilidad efectiva del EPP que debería observarse.

Las condiciones de Nivel 3 —CR-05 y CR-06— no son evaluables mediante prompts integrados de OVD, sino mediante la detección de entidades componentes más razonamiento contextual. En CR-06, además, la evaluabilidad presupone cámaras fijas y una parametrización espacial externa al prompt —por ejemplo, un polígono de zona restringida definido por el operador—. Este supuesto debe quedar explícito desde esta etapa, ya que condiciona tanto el diseño experimental como la futura implementación del módulo de razonamiento contextual.

En un escenario real, múltiples condiciones pueden co-ocurrir sobre la misma persona y el sistema las tratará como unidades de detección ortogonales. Esta decisión simplifica el diseño y la evaluación del prototipo experimental, pero también implica que la correlación entre condiciones no se explota como señal de refuerzo. A ello se suman factores contextuales transversales —resolución, ángulo de cámara, iluminación y oclusión— que deberán documentarse como variables experimentales para interpretar correctamente el desempeño observado.

##### 17.1.5.3. Definición conceptual de patrones de riesgo

Los patrones de riesgo constituyen la unidad operativa de análisis del sistema E-OVRT-VDP. Su definición conceptual articula tres componentes: la definición del patrón como abstracción que integra condiciones detectadas con criterios de persistencia y severidad; la delimitación de los niveles de severidad que ordenan la urgencia de respuesta; y los criterios de activación. Todas las definiciones tienen carácter conceptual y analítico; los valores numéricos propuestos son orientativos y quedan sujetos a calibración empírica durante las etapas de implementación y validación.

###### 17.1.5.3.1. El patrón de riesgo como unidad de análisis

En el contexto del proyecto, se define patrón de riesgo como la especificación declarativa de una situación de seguridad relevante que combina una o más condiciones de riesgo detectadas con criterios de persistencia temporal y un nivel de severidad asignado. El patrón opera como unidad de transición entre el plano de medios (que produce detecciones y trayectorias) y el plano de control (que evalúa situaciones y genera alertas). Su función es transformar las detecciones instantáneas —inherentemente ruidosas y variables entre cuadros— en eventos operativamente significativos cuya confirmación justifique la generación de una alerta asistiva.

La distinción entre condición de riesgo y patrón de riesgo es funcional y tiene consecuencias arquitectónicas directas. La condición de riesgo es la unidad semántica que el plano de medios detecta (vía OVD y, cuando corresponde, MOT). El patrón de riesgo es la unidad que el plano de control evalúa, agregando criterios de persistencia temporal, severidad y, en los casos composicionales, lógica de activación combinada. La interfaz entre ambos planos se establece en la publicación de detecciones y trayectorias etiquetadas semánticamente como eventos, según la arquitectura event-driven.

###### 17.1.5.3.2. Niveles de severidad

Cada patrón de riesgo se asocia a un nivel de severidad que refleja el perfil temporal de la condición, entendido como la velocidad con la que la condición observable puede escalar hacia un incidente y la gravedad potencial de sus consecuencias. En articulación con el framework de métricas, la severidad orienta la urgencia operativa del patrón, las ventanas funcionales de persistencia y los objetivos de TTFD y talert-system; no fija por sí sola el costo computacional del pipeline, que debe distinguirse del tramo Glass-to-Algorithm (G2A).

Se distinguen tres niveles de severidad, cuya granularidad se considera suficiente para el alcance del prototipo experimental. Cada nivel se define como una categoría metodológica de prioridad temporal, fundamentada en el perfil temporal de consecuencias asociado a cada tipo de exposición; la relevancia preventiva de las condiciones subyacentes está establecida en la sección 16.2. La severidad ordena prioridades temporales del protocolo y no constituye una calificación normativa de la situación observada.

El nivel crítico corresponde a condiciones con potencial de escalada rápida hacia daño grave o fatal. Es el caso de la exposición en altura sin protección visible y de la interacción próxima entre peatones y maquinaria en operación: en ambos, la exposición observada puede transformarse con rapidez en un incidente severo, lo que justifica asociar estos patrones con ventanas de persistencia más cortas y objetivos más exigentes de TTFD y dentro del framework evaluativo.

El nivel alto corresponde a condiciones cuya exposición sostenida incrementa de forma significativa el riesgo, aunque con mayor margen de intervención que en el nivel crítico. La ausencia de casco en zona activa de obra no produce por sí misma el incidente, pero elimina una barrera de protección frente a eventos plausibles durante la operación. En esa misma lógica, la permanencia en una zona restringida implica una exposición acumulativa a peligros específicos del sector delimitado.

El nivel medio corresponde a condiciones con riesgo latente o de escalada relativamente más lenta, donde puede exigirse mayor evidencia antes de confirmar la alerta. La ausencia de chaleco reflectivo o indumentaria de alta visibilidad reduce la visibilidad del trabajador ante operadores de vehículos o maquinaria, pero la escalada hacia un incidente depende del movimiento efectivo de esos equipos en la zona, lo que justifica ventanas funcionales más largas que en los niveles precedentes.

Si durante la evaluación experimental se identificara la necesidad de niveles adicionales de granularidad, la taxonomía podría extenderse; sin embargo, para el alcance del prototipo experimental, tres niveles proporcionan un balance adecuado entre expresividad y manejabilidad.

###### 17.1.5.3.3. Criterios de persistencia temporal

La persistencia temporal es el mecanismo analítico que define en qué condiciones una detección instantánea se considera un evento confirmado. Su propósito es reducir la tasa de falsas alarmas derivada de la variabilidad inherente a la detección cuadro a cuadro. Como se documentó en el análisis de modelos OVD, el componente OVD introduce variabilidad en los puntajes de confianza y puede producir apariciones espurias entre cuadros consecutivos, por lo que la confirmación temporal constituye una necesidad operativa.

El criterio de persistencia se conceptualiza como una ventana temporal mínima durante la cual la condición debe observarse de manera sostenida —o con una proporción mínima de detecciones positivas dentro de la ventana— antes de que el patrón se considere activo. Estos criterios se definen en términos de duración temporal (segundos) y no de número de cuadros, dado que la conversión depende del throughput efectivo del pipeline, que a su vez está condicionado por el hardware de inferencia. Esta parametrización en unidades temporales permite que la instancia de análisis y diseño arquitectónico realice la conversión una vez conocida la tasa de cuadros real del sistema. En congruencia con el framework de métricas, esta ventana expresa y no debe confundirse ni con —subtramo computacional por cuadro— ni con, que integra además la confirmación operativa del patrón.

Los rangos de persistencia propuestos se derivan del análisis cualitativo de la velocidad de escalada de cada tipo de riesgo y se fijan de modo compatible con los umbrales orientativos del framework de métricas. Para las condiciones de severidad crítica, se proponen ventanas de 2 a 4 segundos, buscando confirmar la exposición con mínima acumulación de evidencia sin sacrificar la capacidad de alerta temprana. Para condiciones de severidad alta, se proponen ventanas de 3 a 5 segundos, que ofrecen mayor evidencia acumulada para reducir falsos positivos sin perder capacidad de respuesta ante una exposición sostenida. Para condiciones de severidad media, se proponen ventanas de 5 a 10 segundos, admitiendo mayor acumulación de evidencia para controlar falsas alarmas en una condición cuya urgencia operativa es relativamente menor.

Estos rangos tienen carácter analítico; los valores definitivos se calibran empíricamente durante la validación experimental, una vez conocido el throughput efectivo.

Un aspecto adicional, que se retoma en la instancia de análisis y diseño arquitectónico, es el comportamiento de histéresis en la activación y desactivación de patrones. En sistemas de alarmas industriales es habitual que el umbral de activación de una alerta difiera del umbral de desactivación, de modo que una interrupción momentánea de la detección —por oclusión parcial, variabilidad del puntaje de confianza o pérdida temporal del track— no desactive prematuramente un patrón recién confirmado. Esta definición queda planteada como criterio de diseño para la etapa arquitectónica.

Existe una tensión inherente entre la severidad del patrón y la confiabilidad de su activación. Algunos patrones críticos requieren ventanas de persistencia más cortas para responder con la urgencia que su perfil de riesgo demanda. Sin embargo, ventanas más cortas implican menos evidencia acumulada, lo que incrementa la probabilidad de falsos positivos. Este trade-off no tiene resolución analítica a priori y constituye uno de los ejes centrales de calibración empírica de la validación experimental, donde deberá evaluarse la curva de tasa de falsos positivos en función de la duración de la ventana de persistencia para cada patrón.

Como valores de protocolo dentro de esos rangos se fijan 4.000 ms de persistencia para la confirmación de PR-01 y 7.000 ms para PR-02, con umbrales de desactivación de 2.000 y 3.000 ms, respectivamente. Los tiempos se expresan en milisegundos para conservar su significado ante distintos ritmos efectivos de cuadro.

###### 17.1.5.3.4. Operacionalización preliminar del motor de patrones

La definición conceptual de patrones de riesgo requiere una traducción operativa mínima que permita explicar cómo una detección aislada puede convertirse, en tiempo de ejecución, en una alerta asistiva trazable. Para ello, se introduce el motor de patrones como abstracción lógica del sistema, responsable de evaluar la evidencia visual producida por el detector y determinar el estado de cada patrón definido.

El motor de patrones no se entiende como un modelo de visión ni como parte del detector OVD. Su función es posterior a la inferencia: recibe detecciones normalizadas, timestamps, configuración de prompts, reglas del patrón y, cuando corresponda, información de seguimiento o de regiones parametrizadas. A partir de esos insumos, aplica criterios de persistencia, severidad, histéresis y relaciones espaciales para decidir si un patrón permanece inactivo, pasa a estado candidato, se confirma o se considera resuelto.

Esta distinción evita tratar una detección puntual como una alerta automática. Una detección indica evidencia visual en un cuadro o instante determinado; un patrón candidato indica que esa evidencia comenzó a sostenerse o a cumplir una condición contextual; un patrón confirmado indica que se alcanzaron los criterios definidos para generar una alerta registrada; y un patrón resuelto indica que la evidencia dejó de sostenerse durante el intervalo de cierre establecido. De este modo, la alerta queda asociada a una evaluación lógica sobre evidencia acumulada y no a una única salida del modelo.

Para los patrones de Nivel 1, como PR-01 y PR-02, la evaluación puede apoyarse en ventanas temporales de evidencia sin requerir obligatoriamente MOT. En ese caso, la persistencia puede estimarse por proporción de cuadros positivos, duración mínima de evidencia o continuidad aproximada de detecciones relevantes. Si se requiere atribuir la condición a una persona individual durante toda la secuencia, será necesario incorporar MOT o un mecanismo equivalente de asociación temporal. Para los patrones de Nivel 2, la evaluación agrega reglas espaciales intracuadro, como proximidad, solapamiento o relación vertical entre entidades. Para los patrones de Nivel 3, la evaluación exige relaciones sostenidas entre entidades o entre una entidad y una zona parametrizada, por lo que el seguimiento temporal adquiere mayor importancia metodológica.

La histéresis forma parte del comportamiento esperado del motor. Un patrón no debería activarse por una detección espuria ni cerrarse por una pérdida momentánea del detector, una oclusión breve o una caída puntual de confianza. Por ello, los criterios de activación y desactivación pueden utilizar ventanas diferentes: la activación exige evidencia suficiente para confirmar el patrón, mientras que la desactivación puede requerir ausencia sostenida de evidencia durante un intervalo mínimo. Esta separación reduce oscilaciones y alertas repetidas dentro de un mismo episodio; la reaparición de la condición después de su resolución constituye un episodio nuevo, y la eventual supresión de notificaciones repetidas se define fuera del motor de patrones.

En esta etapa, el motor de patrones queda definido como una estructura lógica preliminar y no como una implementación cerrada. La instancia de análisis y diseño arquitectónico traduce esta definición en componentes, contratos, eventos y configuraciones concretas; la implementación del prototipo la materializa; y la validación experimental calibra empíricamente sus umbrales, ventanas e histéresis. Con esta delimitación se cierra la brecha entre el patrón conceptual y su evaluación en runtime.

###### 17.1.5.3.5. Catálogo de patrones de riesgo

La Tabla 21 presenta el catálogo de patrones de riesgo asociados a las condiciones seleccionadas. Para cada patrón se especifica la condición o condiciones de activación, el nivel de severidad, el rango de persistencia temporal orientativo, el perfil temporal de la condición que fundamenta la asignación de severidad y el trade-off de falsos positivos asociado.

**Tabla 21**

*Catálogo de patrones de riesgo del prototipo E-OVRT-VDP*

| **Patrón** | **Cond.** | **Severidad** | **Persistencia** | **Criterio de activación** | **Perfil temporal de la condición** | **Trade-off FP** |
| --- | --- | --- | --- | --- | --- | --- |
| PR-01 | CR-01 | Alto | 3–5 s | Persona detectada sin casco durante el intervalo mínimo | Exposición sostenida a caída de objetos o impactos en zona activa de obra; incidente posible ante evento desencadenante. | Moderado |
| PR-02 | CR-02 | Medio | 5–10 s | Persona detectada sin chaleco o indumentaria de alta visibilidad en zona de circulación durante el intervalo | Riesgo de atropello o interferencia operacional por baja visibilidad; escalada dependiente del movimiento efectivo de vehículos o maquinaria. | Bajo |
| PR-03 | CR-03 | Crítico | 2–4 s | Persona en posición elevada sin sistema anticaídas durante el intervalo | Caída a distinto nivel con consecuencia potencialmente fatal; requiere respuesta temprana ante exposición en altura sin protección suficiente. | Elevado |
| PR-04 | CR-04 | Crítico | 2–4 s | Persona próxima a borde desprotegido durante el intervalo | Caída a distinto nivel desde abertura, borde o plataforma sin protección colectiva eficaz. | Elevado |
| PR-05 | CR-05 | Crítico | 2–4 s | Maquinaria y peatón co-detectados por debajo del umbral de distancia mínima durante el intervalo | Atropello, aplastamiento o contacto peligroso por interacción próxima entre peatones, vehículos y maquinaria de obra. | Elevado |
| PR-06 | CR-06 | Alto | 3–5 s | Persona detectada dentro del polígono de zona restringida durante el intervalo | Exposición sostenida a riesgos propios de una zona señalizada, delimitada, de exclusión, de seguridad o de acceso restringido. | Moderado |

*Nota.* Los rangos de persistencia temporal son orientativos y quedan sujetos a calibración empírica durante la validación experimental, una vez conocido el throughput efectivo del pipeline. La columna “Trade-off FP” indica cualitativamente el riesgo de falsos positivos asociado a la brevedad de la ventana de persistencia. La severidad es una clasificación interna del protocolo, fundamentada en el perfil temporal de la condición; no constituye una calificación normativa de la situación observada ni define por sí misma los umbrales computacionales de activación, distancia, persistencia o latencia del sistema. La relevancia preventiva de las condiciones se fundamenta en la sección 16.2. Fuente: elaboración propia.

###### 17.1.5.3.6. Criterios de activación combinada para condiciones de nivel 3

Los patrones PR-05 y PR-06, asociados a condiciones composicionales de Nivel 3, requieren criterios de activación que evalúen relaciones espaciales o de contención entre entidades detectadas independientemente. Los criterios se definen a continuación a nivel conceptual; su materialización en reglas computacionales evaluables corresponde a la instancia de análisis y diseño arquitectónico.

PR-05 — maquinaria en proximidad a peatones. La activación requiere la detección simultánea de al menos una entidad clasificable como maquinaria de obra —por ejemplo, excavadora, retroexcavadora, camión volquete o grúa— y al menos una persona, cuyas detecciones presenten una relación de proximidad inferior a un umbral configurable. Toda métrica de proximidad calculada en coordenadas de imagen debe interpretarse como una medida geométrica 2D aproximada y no como una distancia física real, dado que la perspectiva de cámara altera las distancias aparentes. La evaluación debe sostenerse durante el intervalo de persistencia definido para el patrón, lo que exige trayectorias suficientemente estables de las entidades involucradas. La selección de puntos representativos de las detecciones y de la métrica geométrica concreta corresponde a la instancia de análisis y diseño arquitectónico.

PR-06 — persona en zona restringida. La activación requiere la detección de al menos una persona cuya posición representativa se encuentre contenida dentro de un polígono predefinido que representa la zona restringida. El polígono forma parte de la parametrización del sistema —configurable por el operador, externo al prompt OVD— y presupone una cámara fija, supuesto adoptado para el alcance del prototipo experimental. La permanencia debe sostenerse durante el intervalo de persistencia, lo que implica seguimiento temporal cuando la persistencia se compute por entidad individual. El mecanismo de definición de polígonos y la lógica de contención corresponden a la instancia de análisis y diseño arquitectónico.

Ambos patrones dependen del módulo MOT en la medida en que la evaluación de relaciones sostenidas en el tiempo requiere trayectorias estables de los objetos rastreados durante el intervalo de persistencia. Los ID switches, pérdidas temporales de trayectoria y reasociaciones erróneas pueden generar interrupciones espurias en la evaluación del patrón o reinicios indebidos de la ventana de persistencia. Por ello, estos errores deben contemplarse en el diseño del módulo de razonamiento contextual durante la instancia de análisis y diseño arquitectónico y cuantificarse en la evaluación experimental de la validación experimental.

###### 17.1.5.3.7. Frontera explícita con la instancia de análisis y diseño arquitectónico

Quedan tres insumos directos para la instancia de análisis y diseño arquitectónico: el catálogo de condiciones de riesgo clasificado por niveles de complejidad (Tabla 20), el catálogo de patrones con severidad y persistencia temporal orientativa (Tabla 21), y los criterios conceptuales de activación combinada para PR-05 y PR-06 —con el supuesto de cámara fija, las métricas de proximidad y contención espacial por definir, y la histéresis como criterio de diseño.

Sobre esa base, la instancia de análisis y diseño arquitectónico materializa el esquema declarativo de patrones, el motor de evaluación, la parametrización de zonas restringidas, la lógica de proximidad entre entidades, la lógica de contención punto-en-polígono, los mecanismos computacionales de persistencia temporal y el tratamiento de errores asociados al seguimiento, como pérdidas temporales de trayectoria o cambios de identidad. En particular, allí se define cómo se traducen los criterios conceptuales en reglas operativas configurables, incluyendo la selección de puntos representativos de las detecciones, las métricas geométricas aplicables en coordenadas de imagen y, si correspondiera, mecanismos de calibración o compensación de perspectiva.

La instancia de análisis y diseño arquitectónico podrá establecer valores iniciales configurables para umbrales espaciales, ventanas temporales y criterios de activación/desactivación, con el fin de implementar y ensayar el sistema. Sin embargo, la calibración empírica final de esos umbrales y ventanas corresponde a la validación experimental, bajo el framework cuantitativo definido en el framework de métricas.

##### 17.1.5.4. Protocolo de diseño y evaluación de prompts OVD

El protocolo de prompts establece el marco para el diseño, la variación sistemática y la evaluación empírica de las consultas textuales que operan como interfaz del modelo OVD. Se apoya en la evidencia sobre sensibilidad a la formulación del prompt documentada en el análisis de modelos OVD y en antecedentes de la literatura que muestran que el desempeño de modelos visión-lenguaje y detectores open-vocabulary puede verse afectado por la redacción de la consulta textual y por la forma en que esta se transforma en representaciones textuales para la detección (Du et al., 2022; Zhou et al., 2022).

Asimismo, toma como referencia protocolos de evaluación recientes orientados a examinar limitaciones de los detectores OVD ante atributos de granularidad fina, vocabularios dinámicos, negativos difíciles, comprensión posicional y relaciones entre objetos (Bianchi et al., 2024; Yao et al., 2024). Su objetivo es sistematizar el proceso de selección de prompts, reducir la arbitrariedad y dejar documentadas las decisiones de formulación con evidencia empírica. El protocolo se articula con el framework de métricas, del cual toma las métricas de evaluación y los criterios operativos aplicables al componente OVD.

###### 17.1.5.4.1. Sensibilidad a la formulación del prompt como variable del sistema

El análisis de modelos OVD documentó que los detectores open-vocabulary presentan sensibilidad a variaciones en la formulación de las consultas textuales: cambios leves de redacción pueden alterar significativamente el desempeño de los modelos visión-lenguaje (Zhou et al., 2022); el embedding textual de clase se genera a partir de los prompts ingresados al encoder y su alineación con las representaciones visuales requiere ajuste específico para la tarea de detección (Gu et al., 2021; Du et al., 2022); y la evaluación se vuelve especialmente exigente ante atributos de granularidad fina, vocabularios dinámicos y clases negativas semánticamente cercanas (Bianchi et al., 2024; Yao et al., 2024). De manera complementaria, la incorporación de negativos semánticamente relacionados durante el entrenamiento mejora la discriminación del detector, lo que refuerza —aunque esa técnica exceda el alcance del proyecto— que la composición semántica del vocabulario influye sobre el desempeño (Kim et al., 2024).

En conjunto, estas evidencias justifican tratar el diseño de prompts como una variable de ingeniería del sistema, gestionada con un rigor comparable al de las decisiones de arquitectura, selección de modelos o definición de métricas. El protocolo siguiente ordena ese proceso para el dominio de detección de condiciones de riesgo en construcción civil.

###### 17.1.5.4.2. Estrategia de variación sistemática

Para cada condición de riesgo del catálogo (Tabla 20) se diseñan múltiples variaciones de prompt que difieren a lo largo de ejes controlados. La variación sistemática permite identificar qué formulaciones logran la mejor alineación semántica con las características visuales del dominio y documenta las decisiones de selección con evidencia reproducible. Se definen cuatro ejes principales.

**Estructura sintáctica.** El primer eje comprende variaciones en la organización de los elementos de la consulta, incluyendo frases nominales simples, oraciones descriptivas con contexto y variaciones en el uso de artículos, preposiciones o modificadores. Por ejemplo, para la detección de casco, las formulaciones “hard hat”, “person wearing hard hat” y “safety helmet on worker” difieren en estructura gramatical, aunque refieren a conceptos visualmente relacionados.

Se incluyen además variaciones con template, como “a photo of a [CLASS]”. Esta decisión se fundamenta en el uso habitual de templates en modelos tipo CLIP, donde transformar una etiqueta aislada en una descripción textual breve puede reducir la brecha entre nombres de clase y textos naturales observados durante el preentrenamiento, y mejorar el desempeño frente al uso de la etiqueta sin contexto (Radford et al., 2021). En consecuencia, el protocolo compara prompts con y sin template, sin presuponer a priori cuál formulación resultará superior para el dominio específico de seguridad en construcción.

**Nivel de especificidad del vocabulario.** El segundo eje comprende variaciones en la granularidad de los términos utilizados, desde vocabulario genérico hasta terminología específica del dominio de construcción. Por ejemplo, “person”, “worker” y “construction worker” representan distintos niveles de especificidad semántica para referirse a entidades humanas observables en una escena de obra. La hipótesis metodológica es que términos más específicos pueden mejorar la precisión en el dominio al reducir la ambigüedad de la consulta y aproximarla al contexto visual de obra. Sin embargo, también pueden reducir el recall si la formulación elegida resulta demasiado restrictiva o menos compatible con las representaciones textuales aprendidas por el modelo durante el preentrenamiento. Por ello, la selección entre vocabulario genérico y vocabulario específico no se asume como una decisión evidente, sino como una variable experimental del diseño de prompts.

**Estrategia de detección.** El tercer eje distingue entre formulaciones directas y formulaciones indirectas o descompuestas. En las formulaciones directas, el prompt intenta describir la condición de riesgo completa, incluyendo presencia o ausencia del elemento relevante; en las indirectas, el detector identifica entidades visibles por separado y la evaluación de la condición se reconstruye mediante lógica externa al modelo OVD. Esta distinción no es meramente terminológica: define dos modos de consulta con implicancias diferentes sobre precisión, costo computacional y complejidad de integración en el pipeline. La distinción resulta pertinente porque los modelos OVD permiten consultar categorías o descripciones mediante entradas textuales, pero no necesariamente resuelven de forma robusta todos los atributos, posiciones y relaciones espaciales implicados en una condición compuesta (Gu et al., 2021; Yao et al., 2024).

En este trabajo estas familias se identifican con un código: estrategia directa (E-DIR), cuando el prompt intenta describir la condición de riesgo completa; estrategia indirecta (E-IND), cuando el detector identifica entidades visibles por separado y la condición se reconstruye mediante lógica externa al modelo; y estrategia híbrida (E-HYB), cuando se combinan consultas de ambos tipos bajo una regla de composición explícita. Los códigos identifican las variantes en el diseño arquitectónico y en la evaluación experimental.

La elección entre ambas estrategias está condicionada por la dificultad práctica de evaluar condiciones formuladas en términos de ausencia visible. Mientras la estrategia directa intenta describir de manera íntegra la condición de riesgo, la indirecta opera con prompts de presencia pura —por ejemplo, “person” y “hard hat” como consultas separadas— y traslada al sistema la responsabilidad de asociar detecciones y verificar relaciones geométricas. El beneficio potencial en robustez semántica se compensa, sin embargo, con mayor complejidad de razonamiento y una posible carga adicional de inferencia por cuadro, cuya magnitud deberá verificarse frente al presupuesto de latencia definido en el framework de métricas. La estrategia indirecta resulta especialmente pertinente para condiciones cuya evidencia visual es la ausencia de un EPP —CR-01, CR-02, CR-03— y para condiciones que requieren evaluación de relaciones espaciales intracuadro —CR-03, CR-04—.

El protocolo de evaluación de la Sección 17.1.5.4.5 compara empíricamente ambas estrategias para todas las condiciones en que sean aplicables, sin presuponer la superioridad de ninguna. La instancia de análisis y diseño arquitectónico materializa la lógica de asociación espacial requerida por la estrategia indirecta y determina si su costo computacional adicional es compatible con las restricciones operativas del sistema.

**Composición del vocabulario activo.** El cuarto eje evalúa cómo el conjunto de prompts simultáneamente activos en el vocabulario del detector afecta el desempeño de cada prompt individual. El benchmark FG-OVD muestra que la evaluación de detectores open-vocabulary se vuelve especialmente exigente cuando el vocabulario incluye clases negativas de granularidad fina, es decir, descripciones semánticamente cercanas al prompt objetivo pero referidas a categorías o atributos distintos. En ese escenario, varios modelos OVD presentan dificultades para detectar, distinguir y asignar correctamente descripciones finas en presencia de hard-negative classes (Bianchi et al., 2024).

En el contexto de E-OVRT-VDP, donde el sistema busca simultáneamente múltiples condiciones y entidades —por ejemplo, “hard hat”, “person”, “reflective vest” y “scaffolding”—, se plantea la hipótesis de que prompts semánticamente próximos pueden competir entre sí y generar confusiones de clasificación. Por ello, este eje propone evaluar el desempeño de cada prompt tanto en aislamiento como dentro del vocabulario completo del sistema.

**Implicancias del tamaño del vocabulario activo.** El número de prompts simultáneamente activos puede afectar tanto la latencia de inferencia como la precisión, y su impacto no es uniforme entre arquitecturas: las familias YOLO orientadas a open-vocabulary precomputan o reparametrizan los embeddings textuales fuera del ciclo de inferencia —el paradigma prompt-then-detect de YOLO-World y la alineación reparametrizable RepRTA de YOLOE (Cheng et al., 2024; Wang et al., 2025)—, mientras que Grounding DINO procesa el par imagen-texto en cada consulta, de modo que un vocabulario mayor incrementa la longitud de la entrada textual y el costo de fusión cross-modal (Liu et al., 2024). El detalle arquitectónico se desarrolla en el análisis de modelos OVD; la consecuencia de diseño es que la cantidad de prompts sostenibles dentro del presupuesto de latencia depende del modelo elegido, la sintaxis concreta de los prompts, la resolución de entrada y el hardware de inferencia disponible.

###### 17.1.5.4.3. Consideraciones sobre el idioma de los prompts

Los modelos OVD candidatos —Grounding DINO, YOLO-World, YOLOE, OWL-ViT y Florence-2— se apoyan en arquitecturas visión-lenguaje donde la entrada textual cumple un rol central, con encoders derivados de BERT, CLIP o MobileCLIP según la familia (Liu et al., 2024; Cheng et al., 2024; Wang et al., 2025; Minderer et al., 2022; Xiao et al., 2024).

La decisión de formular los prompts primarios en inglés se fundamenta en la centralidad de ese idioma en varios de los modelos y corpus visión-lenguaje utilizados como base. CLIP, Conceptual Captions y CC12M —los corpus de la línea de preentrenamiento de base— se construyeron sobre material predominantemente en inglés (Radford et al., 2021; Sharma et al., 2018; Changpinyo et al., 2021). Aunque no todos los modelos candidatos publican una caracterización lingüística equivalente de sus datos de entrenamiento, la evidencia disponible justifica utilizar el inglés como idioma primario de consulta para favorecer la compatibilidad con los patrones lingüísticos dominantes del preentrenamiento.

Esta decisión tiene una implicación práctica relevante: la plataforma se desarrolla en un contexto académico argentino y constituye un prototipo experimental, no un sistema productivo. En consecuencia, el idioma natural de trabajo de operadores e investigadores es el español, mientras que la capa de consulta del detector se formulará primariamente en inglés para favorecer la alineación con los modelos candidatos. En el prototipo experimental, la traducción de las descripciones de condiciones de riesgo al inglés se realiza manualmente durante la fase de diseño de prompts.

Como línea complementaria de evaluación, podrá explorarse la ejecución de prompts formulados directamente en español o mediados por traducción automatizada, con el fin de cuantificar la eventual degradación asociada a la brecha lingüística y documentar si alguno de los modelos candidatos ofrece soporte multilingüe funcional para el dominio. De realizarse, estas pruebas corresponderán a la validación experimental y constituirán una contribución adicional al análisis de viabilidad del sistema.

###### 17.1.5.4.4. Catálogo de prompts candidatos

El catálogo de prompts candidatos define las formulaciones previstas para evaluar las condiciones de riesgo seleccionadas. Para las condiciones de Nivel 1 y Nivel 2 se contemplan formulaciones directas, variantes léxicas y estrategias indirectas o descompuestas, según el tipo de evidencia visual que se busca activar en el modelo. Por ejemplo, una condición como ausencia de casco puede evaluarse mediante consultas directas orientadas a identificar una “persona sin casco” o mediante variantes que busquen evidencias positivas de “casco de seguridad” sobre la región cefálica. De forma similar, una condición asociada al chaleco reflectivo puede abordarse mediante prompts como “persona con chaleco de seguridad” o formulaciones equivalentes vinculadas a ropa de alta visibilidad.

En el caso de las condiciones de nivel 3, no se proponen prompts integrados como una única consulta OVD, dado que su evaluación requiere razonamiento contextual sobre múltiples entidades o relaciones espaciales. Por ello, se consideran prompts orientados a detectar las entidades componentes, cuyos resultados podrán ser utilizados posteriormente por el motor de patrones. El conjunto de candidatos se construye a partir del catálogo del Anexo C (Tabla C.1), y las formulaciones finalistas deben quedar seleccionadas y congeladas mediante un acta previa a la evaluación comparativa.

La inclusión de prompts candidatos para CR-03 y CR-04 no implica que ambas condiciones dispongan de soporte completo de evaluación en datasets públicos. En estos casos, los prompts permiten explorar formulaciones posibles y detectar entidades o estados visuales parciales, pero la validación del patrón completo depende de contar con datos que representen la condición operacionalizada. Por ello, los resultados sobre CR-03 y CR-04 deberán distinguir explícitamente entre desempeño del prompt sobre componentes visuales y evaluación integral de la condición de riesgo.

###### 17.1.5.4.5. Protocolo de evaluación de prompts

El protocolo de evaluación tiene por objetivo determinar, para cada condición de riesgo y cada modelo OVD candidato, qué formulación de prompt ofrece el mejor desempeño dentro del framework adoptado para el componente OVD, con lectura prioritaria sobre AP@0.5 y Precision/Recall en el punto operativo declarado. Su diseño se fundamenta en prácticas de evaluación documentadas en la literatura reciente, particularmente FG-OVD y OVDEval (Bianchi et al., 2024; Yao et al., 2024), adaptadas al alcance y los recursos de un proyecto académico. Las métricas, los criterios de reporte y los umbrales orientativos se definen en el framework de métricas; el presente protocolo describe la estructura procedural de las pruebas de prompts dentro de ese marco. Se organiza en cinco fases.

**Fase 1 - Preparación del dataset de evaluación.** Para cada condición de riesgo, se selecciona un subconjunto del inventario de datasets documentado en la estrategia de datos, benchmarks y partición que contenga imágenes o cuadros con anotaciones de verdad fundamental o ground truth relevantes para la condición evaluada. La selección sigue el principio de representatividad, de modo que el subconjunto incluya variación en iluminación, ángulo de cámara, grado de oclusión y escala de los objetos de interés, dentro de lo que los datos disponibles permitan.

Cuando el ground truth existente no cubra directamente la condición —por ejemplo, si el dataset anota “casco” pero no “persona sin casco”—, se generarán anotaciones complementarias sobre un conjunto acotado de imágenes, garantizando acuerdo interanotador mediante doble anotación independiente sobre al menos un 20% del conjunto. Para etiquetas categóricas sobre unidades previamente definidas se calculará el coeficiente kappa de Cohen como indicador de confiabilidad interanotador (Cohen, 1960); cuando la anotación involucre localización espacial mediante bounding boxes, el acuerdo se evaluará además mediante criterios de solapamiento geométrico, como IoU promedio o proporción de coincidencias por encima de un umbral IoU predefinido. El requisito rige para toda anotación producida por el proyecto; cuando la referencia se reutilice de anotaciones de fuente sin reanotación, la doble anotación no aplica y la ausencia de una medida de acuerdo debe declararse como limitación del material.

Como objetivo operativo se procurará contar con al menos 200 instancias positivas anotadas por condición, complementadas con casos negativos cuando resulten necesarios para estimar precisión y falsos positivos. Cuando una condición o un estrato no alcance ese piso, el protocolo exige reportar el n efectivo con intervalos de confianza al 95 % obtenidos por bootstrap sobre las unidades de evaluación y abstenerse de ordenar variantes cuyos intervalos se superpongan.

**Fase 2 - Definición de la matriz experimental.** Se construye la matriz de combinaciones a evaluar, donde cada celda corresponde a una tupla (modelo OVD, condición de riesgo, variación de prompt, contexto de vocabulario). El último término responde al eje de composición de vocabulario definido en la Sección 17.1.5.4.2, y distingue dos condiciones experimentales por prompt: evaluación en aislamiento, donde el prompt —o el conjunto mínimo de prompts requerido por la estrategia indirecta o descompuesta— es el único vocabulario activo del modelo, y evaluación en contexto completo, donde el prompt opera junto con los demás prompts activos del sistema.

Los hiperparámetros del modelo —umbral de confianza, umbral de NMS— se fijan a valores constantes durante toda la evaluación para garantizar comparabilidad entre variaciones de prompt. Si se evalúan múltiples umbrales, estos se documentan como variable adicional de la matriz.

**Fase 3 - Ejecución sistemática.** Para cada combinación de la matriz se ejecuta la inferencia sobre el dataset correspondiente en condiciones controladas —hardware, resolución de entrada y preprocesamiento constantes—, registrando por imagen las detecciones con sus coordenadas, puntaje de confianza y etiqueta, en formato estructurado que permita el cálculo posterior de métricas y la reproducción de los experimentos.

**Fase 4 - Cálculo de métricas.** Para cada tupla (modelo, condición, prompt, contexto de vocabulario), se calculan las métricas definidas en el framework de métricas para el componente OVD. Se registra también el puntaje de confianza medio de las detecciones verdaderas positivas como indicador complementario de la estabilidad de la respuesta del modelo ante cada formulación de prompt.

Para las condiciones evaluadas con estrategia indirecta o descompuesta, se calculan también las métricas de cada entidad componente por separado, de modo que pueda identificarse si la degradación proviene de la detección de las entidades individuales, del atributo visual evaluado o de la lógica de asociación.

**Fase 5 - Análisis comparativo y selección.** Se construye una matriz de resultados que permite identificar, para cada condición, la combinación (modelo, prompt) que maximiza el criterio de selección definido en el framework de métricas. Los resultados se analizan tanto por condición individual como de manera transversal, identificando patrones sistemáticos —por ejemplo, si los prompts con template superan consistentemente a los prompts sin template, o si la estrategia indirecta supera a la directa para condiciones de EPP—. Se documenta también la sensibilidad de cada modelo al contexto de vocabulario, cuantificando la diferencia de desempeño entre aislamiento y contexto completo.

El protocolo produce como salida un registro estructurado de métricas por combinación, que alimenta directamente las decisiones de la instancia de análisis y diseño arquitectónico —selección de prompts primarios para la configuración del sistema— y las conclusiones de la validación experimental —análisis de sensibilidad y robustez frente a variaciones de formulación—. Este registro, junto con los scripts de ejecución y los datasets utilizados, constituye el artefacto de reproducibilidad del protocolo.

##### 17.1.5.5. Síntesis parcial de condiciones, prompts y variantes de prueba

La formulación del prompt se asume como variable experimental del sistema. En OVD, cambios de sintaxis, especificidad o selección léxica pueden modificar el comportamiento del detector, especialmente cuando la condición se formula por ausencia de un elemento, por atributos finos o por composición contextual (Du et al., 2022; Bianchi et al., 2024). Por ello, el contraste entre familias de prompts precede al congelamiento de la configuración comparativa final en la instancia de análisis y diseño arquitectónico.

Para evitar ambigüedades terminológicas se adoptan dos definiciones operativas. La primera es matriz de prompts, entendida como el conjunto acotado de formulaciones alternativas que se ensayan para una misma condición. La segunda es la composición del vocabulario activo, entendida como el conjunto de descripciones, etiquetas o consultas que el modelo evalúa en simultáneo dentro de una corrida determinada. Esta aclaración deja explícito qué variable se mide cuando se habla del “tamaño” o de la “composición” del vocabulario.

El desarrollo completo de las matrices de prompts, sus variantes y los criterios de prueba se presenta en el Anexo C.

#### 17.1.6. Estrategia de datos, benchmarks y partición

##### 17.1.6.1. Introducción y alcance

###### 17.1.6.1.1. Propósito y preguntas rectoras

La estrategia de datos responde a las preguntas rectoras P-E1-03 y P-E1-08 formuladas en la sección 16.7.3 de la fundamentación teórica. En relación con P-E1-03, construye un inventario crítico de datasets públicos potencialmente utilizables para evaluar el prototipo experimental sobre las condiciones de riesgo definidas en la taxonomía de condiciones de riesgo, patrones y prompts, documentando cobertura, formato, acceso, licencia y restricciones operativas. En relación con P-E1-08, analiza qué colecciones pueden funcionar como insumo de un experimento comparativo acotado de fine-tuning, bajo las condiciones metodológicas fijadas por el framework de métricas para preservar la validez de la comparación entre baseline zero-shot y variante ajustada al dominio.

Ese propósito se completa con un mapeo explícito entre cada dataset candidato y las condiciones de riesgo CR-01 a CR-06 de la taxonomía, y con las condiciones metodológicas mínimas que cualquier estrategia de partición deberá satisfacer para sostener una comparación válida entre baseline zero-shot y variante fine-tuned, cuando esa comparación aplique.

El análisis parte del reconocimiento, establecido en la fundamentación teórica, de que los modelos OVD preentrenados en colecciones generalistas presentan una brecha de dominio respecto de la construcción civil. Esa brecha no se resuelve únicamente con mayor volumen: también exige distinguir entre condiciones con evidencia visual directa —como CR-01 y CR-02—, condiciones espaciales o de ausencia visual fina —como CR-03 y CR-04— y condiciones relacionales o dependientes de parametrización externa —como CR-05 y CR-06—. En consecuencia, la aptitud de un dataset no se agota en la presencia de una clase aislada, sino que debe leerse en articulación con la taxonomía y el protocolo de evaluación definidos por la taxonomía de condiciones de riesgo, patrones y prompts y el framework de métricas.

El alcance es metodológico: elabora un inventario de datasets, explicita criterios de inclusión y exclusión, mapea cobertura contra CR-01–CR-06, analiza compatibilidad con los pipelines de ajuste priorizados y fija condiciones mínimas para su eventual partición y uso experimental. No define todavía la combinación definitiva de datasets, no ejecuta particiones ni campañas de curación o anotación complementaria y no implementa mediciones; esas decisiones corresponden a la instancia de análisis y diseño arquitectónico y su validación empírica a la validación experimental.

###### 17.1.6.1.2. Criterios de categorización y exclusión

El inventario se organiza en dos categorías con criterio de pertenencia explícito. La primera agrupa los datasets sobre los cuales se ejecutan operaciones directas (descarga, procesamiento, partición y uso experimental). La segunda comprende benchmarks establecidos cuyas particiones de test se emplean para medir el rendimiento de módulos específicos del sistema en condiciones comparables con la literatura. Toda colección que no satisfaga al menos uno de estos dos criterios queda fuera del alcance de la sección.

**Categoría 1 — Datasets de gestión directa.** Un dataset pertenece a esta categoría si se descarga, procesa y utiliza directamente para evaluación del pipeline OVD en el dominio de construcción civil y/o como insumo del experimento comparativo de fine-tuning. La pertenencia a esta categoría no implica decisión de uso; la confirmación de qué datasets se gestionan efectivamente corresponde a la instancia de análisis y diseño arquitectónico. Los datasets listados en la Sección 17.1.6.2 constituyen el conjunto de candidatos analizados en esta sección.

**Categoría 2 — Benchmarks de evaluación de referencia.** Un dataset pertenece a esta categoría si es un benchmark establecido cuyas particiones de test se emplearán para medir el rendimiento de módulos específicos del sistema bajo condiciones comparables con la literatura. Cada benchmark incluido debe tener una función explícita dentro del protocolo de evaluación, indicando qué módulo se evalúa con él, en qué etapa se utiliza y qué métricas se obtienen.

**Alcance y exclusiones explícitas.** Quedan fuera del inventario las colecciones generalistas de gran escala sobre las cuales los modelos OVD fueron preentrenados por sus autores, tales como Visual Genome, LVIS v1.0, Objects365 v2, Open Images V7, entre otras. Estas colecciones no constituyen datos gestionados por el proyecto: no se descargan, procesan ni particionan, sino que se aprovechan indirectamente a través de los pesos públicos de los modelos candidatos. Su documentación corresponde al análisis de modelos OVD, donde se describe la procedencia de las capacidades open-vocabulary de cada modelo y las restricciones de licencia asociadas.

También quedan fuera del inventario las colecciones que no satisfacen los criterios mínimos de selección definidos en la Sección 17.1.6.1.3, en particular aquellas sin disponibilidad pública verificable, sin condiciones de uso suficientemente documentadas, con baja pertinencia respecto del dominio de construcción civil, con cobertura insuficiente de las condiciones de riesgo CR-01 a CR-06, o con anotaciones incompletas que impidan su conversión o evaluación bajo el protocolo del proyecto. De igual modo, se excluyen como fuente principal de evaluación los datasets compuestos exclusivamente por imágenes sintéticas sin validación manual o sin contraste documentado con escenas reales, dado que no permiten caracterizar adecuadamente el sesgo de dominio respecto de entornos reales de construcción y podrían comprometer la validez ecológica del protocolo experimental.

Las condiciones de calzado inadecuado, ausencia de guantes o gafas de protección, y obstrucción de pasillos o materiales inestables, aunque preventivamente relevantes, no integran el alcance experimental definido en la taxonomía de condiciones de riesgo, patrones y prompts para la Etapa 2. Su análisis de cobertura queda fuera del alcance de esta instancia y sólo correspondería si se ampliara el conjunto de condiciones evaluadas.

###### 17.1.6.1.3. Criterios metodológicos de selección y evaluación

La evaluación de cada dataset candidato se realiza sobre siete dimensiones que derivan del análisis teórico de la fundamentación teórica y de las necesidades operativas del proyecto. Estas dimensiones no tienen pesos fijos a priori; su ponderación relativa depende de la función que la instancia de análisis y diseño arquitectónico asigne al dataset dentro de la estrategia combinatoria. Un dataset orientado a ajuste de dominio priorizaría la pertinencia al dominio (C1) y la cobertura del catálogo experimental (C2), mientras que uno orientado a preservar capacidades open-vocabulary priorizaría la compatibilidad semántica (C3) y la posibilidad de conversión o integración en los pipelines efectivamente seleccionados.

**Tabla 22**

*Criterios de evaluación para la selección de datasets candidatos*

| **#** | **Dimensión** | **Descripción operativa** |
| --- | --- | --- |
| C1 | Pertinencia al dominio | Presencia de escenas de construcción, industria o trabajadores con EPP. Se valoran entornos realistas con variaciones de iluminación, ángulo de cámara y condiciones climáticas. |
| C2 | Cobertura del catálogo experimental | Proporción de categorías anotadas que se corresponden con alguna condición de riesgo del catálogo experimental (CR-01 a CR-06) definido en la Sección 17.1.5.2. |
| C3 | Compatibilidad OV | Amplitud del vocabulario, presencia de anotaciones en lenguaje natural o descripciones que permitan consultas semánticas. |
| C4 | Soporte temporal | Existencia de secuencias con entidades persistentes (IDs de trayectoria) o anotaciones cuadro a cuadro, necesarias para la integración con módulos de seguimiento multi-objeto (MOT). |
| C5 | Calidad de anotación | Exhaustividad y consistencia de las anotaciones (cajas delimitadoras, máscaras, relaciones). Se prefieren anotaciones manuales con protocolos de control de calidad documentados. |
| C6 | Condiciones desafiantes | Presencia de oclusiones, escenas nocturnas o de baja iluminación, movimiento, multitudes o cambios de escala que permitan evaluar robustez en condiciones realistas de obra. |
| C7 | Viabilidad técnico-legal | Formato estandarizado o convertible; disponibilidad pública verificada; licencia explícita o declaración pública de uso académico compatible. Cuando la fuente sólo indique “free use” o la licencia no sea visible, el dataset se mantiene como candidato condicional y requiere verificación manual antes de su gestión efectiva. |

*Nota.* Los criterios C1 a C7 no tienen pesos fijos; su ponderación relativa dependerá de la función asignada al dataset en la instancia de análisis y diseño arquitectónico. Elaboración propia basada en el análisis metodológico de la Etapa 2.

##### 17.1.6.2. Datasets de gestión directa (categoría 1)

La selección se concentra en cuatro colecciones retenidas como candidatas de gestión directa por su pertinencia para CR-01 y CR-02, su disponibilidad y su viabilidad de integración. La retención no asigna todavía un rol definitivo: entrenamiento, evaluación y banco deben definirse mediante particiones disjuntas y con trazabilidad de licencia y procedencia.

###### 17.1.6.2.1. Datasets retenidos como candidatos

**Tabla 23**

*Datasets retenidos como candidatos de gestión directa*

| **Dataset** | **Volumen o versión** | **Contenido relevante** | **Formato** | **Licencia** | **Cobertura** | **Lectura metodológica** |
| --- | --- | --- | --- | --- | --- | --- |
| SHEL5K (Otgonbold et al., 2022) | 5.000 imágenes | Casco, cabeza y persona con o sin casco | Pascal VOC | CC BY 4.0 | CR-01 directa | Fuente sólida para evaluar presencia y ausencia de casco; no cubre chaleco ni relaciones contextuales. |
| CHV (Wang et al., 2021) | 1.330 imágenes | Persona, chaleco y cascos por color | Formato nativo a inspeccionar | Sin licencia formal; cita obligatoria | CR-01 y CR-02 | Condicionado a verificar términos de uso y redistribución. |
| construction_site_safety | Versión registrada | Escenas de construcción con anotaciones de EPP | YOLO / Roboflow | CC BY 4.0 | CR-01 y CR-02 | Candidato de dominio; exige separar linajes de entrenamiento y evaluación. |
| ppe_siabar | Versión registrada | Anotaciones de EPP en dominio afín | YOLO / Roboflow | CC BY 4.0 | CR-01 y CR-02 | Candidato para adaptación; aptitud sujeta a curación y partición. |

*Nota.* La retención expresa aptitud metodológica como candidato y no asignación efectiva. El rol de cada fuente debe quedar congelado antes de cualquier entrenamiento, sin solapamiento entre material de ajuste y estratos de evaluación.

###### 17.1.6.2.2. Datasets descartados y causa metodológica

Las colecciones restantes se descartan del núcleo de gestión directa cuando su licencia, acceso, dominio o cobertura no permiten sostener un uso principal dentro del protocolo. El descarte no niega su valor académico; delimita por qué no integran la combinación retenida.

**Tabla 24**

*Datasets descartados y causa metodológica*

| **Dataset** | **Causa principal** | **Consecuencia para el protocolo** | **Estatuto** |
| --- | --- | --- | --- |
| SH17 | Licencia CC BY-NC-SA y dominio predominantemente industrial. | No se adopta como fuente principal del núcleo. | Descartado. |
| Pictor-PPE | Licencia no verificable y versión pública parcial. | No permite asegurar gestión y redistribución reproducibles. | Descartado. |
| Construction-PPE | Licencia AGPL-3.0 y cobertura ya atendida por fuentes retenidas. | Se evita introducir obligaciones adicionales sin aporte diferencial suficiente. | Descartado. |
| GDUT-HWD y SHWD | Licencia del paquete sin verificar y condición principal ya cubierta. | Pueden conservarse como referencia, pero no como insumo gestionado. | Descartados. |
| SODA | Cobertura orientada a contexto y condiciones fuera del núcleo CR-01/CR-02. | No resuelve de forma nativa los patrones priorizados. | Descartado del núcleo. |
| MOCS | Copia pública parcial y utilidad principalmente exploratoria para maquinaria. | No se adopta para evaluación principal ni ajuste de EPP. | Uso exploratorio solamente. |

*Nota.* Las causas de descarte se aplican al uso principal dentro de este protocolo; no constituyen una evaluación general de la calidad científica de cada colección.

###### 17.1.6.2.3. Síntesis de cobertura conjunta y brechas

La cobertura retenida es suficiente para concentrar el núcleo en CR-01 y CR-02. CR-01 dispone de evidencia directa sobre casco y ausencia de casco; CR-02 cuenta con fuentes que combinan persona y chaleco. CR-03 y CR-04 conservan una brecha directa, mientras que CR-05 y CR-06 requieren datos relacionales, regiones externas o material controlado. La presencia de entidades auxiliares no se interpreta como anotación del patrón completo.

###### 17.1.6.2.4. Viabilidad para el ajuste fino

La rama de ajuste fino se limita a CR-01 y CR-02 y utiliza únicamente fuentes cuya cobertura, licencia y formato permitan construir un conjunto curado y disjunto del test. La comparación no presupone que el ajuste deba superar a la baseline: exige observar la ganancia en el dominio y la retención de capacidades fuera de las clases ajustadas bajo el framework de métricas.

El protocolo conserva un máximo de dos familias candidatas y un rango orientativo de 500 a 2.000 imágenes para el split de entrenamiento. La cantidad concreta, la conversión de formato y la selección de capas o parámetros deben quedar predefinidas y justificarse si se apartan de ese rango.

###### 17.1.6.2.5. Transferibilidad y límites de interpretación

La transferibilidad se interpreta de forma cualitativa según proximidad visual al dominio, cobertura de EPP, diversidad de escala y posibilidad de conservar negativos explícitos. Las cuatro fuentes retenidas sostienen el núcleo, pero ninguna habilita por sí sola conclusiones sobre condiciones relacionales, altura, zonas restringidas o desempeño en obra real no controlada.

###### 17.1.6.2.6. Datos complementarios para condiciones brechadas

Cuando una condición brechada permanezca dentro del alcance exploratorio, el orden de preferencia es: curación de fuentes públicas con licencia compatible; anotación complementaria acotada con control de calidad; y producción de material controlado en el EBE bajo las salvaguardas de la Sección 17.1.10.1. La ampliación sólo se justifica si aporta evidencia interpretable sin desplazar la evaluación del núcleo.

###### 17.1.6.2.7. Condiciones para la partición de datos

La evaluación comparativa zero-shot vs. fine-tuned requiere que los conjuntos de entrenamiento y evaluación sean estrictamente disjuntos, tal como exige el framework de métricas para sostener la validez de la comparación. El diseño concreto de la partición —qué proporciones se asignan a entrenamiento, validación y evaluación, qué datasets alimentan el subset de entrenamiento y qué colecciones se reservan para test— corresponde a la instancia de análisis y diseño arquitectónico, una vez definidos los modelos seleccionados y la estrategia de adaptación de dominio. El protocolo fija sólo las condiciones metodológicas que cualquier esquema de partición deberá satisfacer. Una misma fuente no puede utilizarse simultáneamente como material de entrenamiento y como estrato del banco de evaluación; cualquier excepción invalidaría la independencia de la comparación.

**Tabla 25**

*Condiciones metodológicas para la partición de datos*

| **Condición** | **Descripción** |
| --- | --- |
| Disyunción estricta | Ninguna imagen del split de test debe aparecer en el split de entrenamiento, ni directamente ni mediante data augmentation aplicada sobre imágenes de test. El incumplimiento de esta condición invalidaría la comparación pretrained vs. fine-tuned. |
| Test set compartido | El split de evaluación debe ser idéntico para la línea base pretrained y los modelos fine-tuned, a fin de garantizar comparabilidad directa. |
| Semilla reproducible | Cuando la partición sea aleatoria, debe documentarse la semilla utilizada, de modo que el split pueda regenerarse y verificarse independientemente. |
| Splits oficiales | Cuando exista un split publicado por la fuente (p. ej., CHV en el paper o Construction-PPE en Ultralytics), conviene revisarlo antes de redefinirlo. La instancia de análisis y diseño arquitectónico podrá apartarse de ese esquema si justifica la decisión. |
| Rango de entrenamiento | El split de entrenamiento para fine-tuning se acota a 500–2.000 imágenes, conforme al análisis de suficiencia desarrollado en la sección 17.1.6.2.4. La baseline zero-shot se evalúa siempre sobre el test set congelado. |
| No solapamiento cruzado | Si se combinan múltiples datasets para formar un split unificado, debe verificarse la ausencia de imágenes duplicadas entre colecciones, especialmente entre datasets de PPE web-mined o crowd-sourced que podrían compartir fuentes de origen. |
| Congelamiento previo | El test set debe quedar definido y congelado antes del inicio de cualquier entrenamiento, incluida la aplicación de data augmentation sobre el split de entrenamiento, para evitar data leakage inadvertido. |

*Nota.* Estas condiciones son requisitos metodológicos; las proporciones concretas de partición y la composición final del subset de entrenamiento corresponden a la instancia de análisis y diseño arquitectónico. Cuando exista una divergencia entre el split publicado por una fuente y las necesidades experimentales del proyecto, la desviación deberá justificarse explícitamente en la bitácora.

###### 17.1.6.2.8. Evaluación de aptitud por propósito

La Tabla 26 sintetiza la aptitud metodológica de las cuatro fuentes retenidas para ajuste y evaluación, sin asignar todavía un rol efectivo.

La valoración considera cobertura, proximidad de dominio, formato, licencia y necesidad de mantener fuentes independientes para el test.

**Tabla 26**

*Aptitud de cada dataset candidato para fine-tuning y evaluación*

| **Dataset** | **Aptitud FT** | **Aptitud eval.** | **Justificación** |
| --- | --- | --- | --- |
| SHEL5K | Media | Alta para CR-01 | Cobertura sólida de casco y ausencia de casco; alcance limitado fuera de CR-01. |
| CHV | Media condicionada | Alta para CR-01/CR-02 | Pertinencia de dominio, con términos de uso del dataset que deben verificarse. |
| construction_site_safety | Alta potencial | Alta condicionada | Escenas de construcción y anotaciones de EPP; exige disyunción por linaje entre ajuste y evaluación. |
| ppe_siabar | Alta potencial | Media condicionada | Aporta EPP en dominio afín; requiere una fuente independiente para evaluar generalización. |

*Nota.* “Condicionada” indica que el rol depende de la verificación de términos, de la curación y de una partición estrictamente disjunta.

##### 17.1.6.3. Benchmarks de evaluación de referencia (categoría 2)

Tal como establece el framework de métricas, las métricas MOT basadas en identidades persistentes sólo resultan metodológicamente defendibles cuando se dispone de secuencias o benchmarks específicamente anotados con IDs de trayectoria. Por ello, los benchmarks de esta categoría no sustituyen la evaluación del dominio del proyecto: cumplen una función acotada de verificación de implementación y comparación de referencia para el módulo de seguimiento.

**Tabla 27**

*Benchmarks de evaluación de referencia para módulos de seguimiento*

| **Dataset** | **Características** | **Licencia** | **Métricas** | **Aptitud en el proyecto** | **Limitaciones** |
| --- | --- | --- | --- | --- | --- |
| MOT17 | 14 secuencias reales; benchmark operacionalizado como 42 entradas al considerar tres sets públicos de detecciones por secuencia: DPM, Faster R-CNN y SDP. | CC BY-NC-SA 3.0 | MOTA, IDF1, HOTA | Adecuado para verificar que la implementación del tracker reproduce resultados comparables a trackers de referencia bajo un protocolo conocido. | Benchmark centrado en seguimiento de peatones; no representa el dominio construcción. |
| OVT-B | 1.973 videos; 637.608 anotaciones de bounding boxes; 1.048 categorías. | Apache-2.0 visible en el repositorio oficial | TETA como métrica principal; LocA, ClsA y AssA como componentes. | Adecuado para evaluar la integración OVD+MOT bajo vocabulario abierto extenso y múltiples categorías. | No declara cobertura específica del dominio construcción. |

*Nota.* TETA = Track Every Thing Accuracy; LocA = Localization Accuracy; ClsA = Classification Accuracy; AssA = Association Accuracy. MOTA = Multiple Object Tracking Accuracy; IDF1 = ID F1 Score; HOTA = Higher Order Tracking Accuracy. TrackingNet y LaSOT se descartan por corresponder a benchmarks de single-object seguimiento; OV-TAO se descarta porque OVT-B ofrece mayor escala y una adecuación más directa al problema open-vocabulary multi-object seguimiento del proyecto.

###### 17.1.6.3.1. MOT17 — justificación de uso

MOT17 no representa el dominio de construcción civil. Su inclusión responde a una razón de ingeniería específica: constituye un benchmark de referencia ampliamente utilizado para evaluar trackers multiobjeto bajo un protocolo conocido. En particular, permite contrastar la implementación local del módulo de seguimiento con resultados públicos de trackers de referencia, como ByteTrack y OC-SORT, antes de trasladar el análisis al dominio del proyecto. Por lo tanto, la evaluación sobre MOT17 responde a una pregunta de corrección de implementación y reproducibilidad técnica, no de validez operativa en obra.

###### 17.1.6.3.2. OVT-B — justificación de uso

OVT-B es el benchmark más cercano a la arquitectura conceptual del proyecto, porque evalúa explícitamente el seguimiento multiobjeto en régimen open-vocabulary. Su utilidad no reside en representar el dominio de construcción civil, sino en evaluar la integración OVD+MOT bajo un vocabulario extenso y trayectorias de múltiples categorías. Por ello, OVT-B se interpreta como benchmark de referencia para robustez semántica y asociación temporal, mientras que la validación del dominio específico se mantiene separada y se realiza sobre los datos del proyecto o sobre el escenario complementario que se defina en la instancia de análisis y diseño arquitectónico.

##### 17.1.6.4. Consideraciones transversales

Dos dimensiones atraviesan el inventario completo con independencia de la categoría o del propósito asignado a cada dataset: las condiciones éticas y de licencia que enmarcan el uso de los datos, y las restricciones logísticas que condicionan su gestión operativa. Ambas dimensiones son insumos directos para la planificación de la instancia de análisis y diseño arquitectónico.

###### 17.1.6.4.1. Consideraciones éticas sobre los datos

Los datasets retenidos reúnen imágenes procedentes de repositorios públicos y escenas de construcción o dominios afines centrados en EPP. Su uso previsto se limita a investigación académica, sin reconocimiento facial, identificación individual ni tratamiento biométrico. Las anotaciones consideradas son principalmente cajas delimitadoras y etiquetas de objetos, en concordancia con el principio de minimización desarrollado en el marco ético-legal de la fundamentación teórica.

Para cualquier dato generado ad hoc conforme a las alternativas de la Sección 17.1.6.2.6 rigen las salvaguardas de la Sección 17.1.10.1.

Las condiciones de uso no son homogéneas. SHEL5K, construction_site_safety y ppe_siabar se registran bajo CC BY 4.0; CHV no presenta una licencia formal para el paquete de datos, por lo que su eventual utilización exige citar la fuente y verificar los términos aplicables. La licencia del artículo asociado no se transfiere por inferencia al dataset. Las colecciones descartadas conservan el estatuto y la causa resumidos en la Tabla 24, sin atribuirles licencias no verificadas.

En consecuencia, la instancia de análisis y diseño arquitectónico verifica manualmente los términos efectivos de cada fuente antes de descargar, fusionar, redistribuir o publicar derivados de los datos. La gestión del corpus deberá conservar trazabilidad por dataset de origen, registrar licencias y condiciones aplicables, y evitar que la combinación de colecciones con licencias heterogéneas genere obligaciones incompatibles con el alcance académico del proyecto.

###### 17.1.6.4.2. Logística de datos

El pipeline de gestión de datos comprende cinco pasos secuenciales: descarga o solicitud de acceso desde las fuentes de origen, verificación de integridad, inspección del formato nativo y conversión al formato de trabajo requerido por cada pipeline, partición conforme a las condiciones metodológicas definidas anteriormente, y transferencia del subset de entrenamiento y, cuando corresponda, del conjunto de validación al clúster de cómputo de alto rendimiento Mendieta para el experimento de fine-tuning. La evaluación e inferencia operativa se ejecutarán en el hardware local, manteniendo la separación funcional entre entrenamiento y despliegue documentada en la sección de entorno experimental, infraestructura y escenarios de evaluación. La logística de conversión y acceso por fuente se detalla en la Tabla C.3 del Anexo C.

##### 17.1.6.5. Síntesis parcial de la estrategia de datos, benchmarks y partición

La estrategia de datos, benchmarks y partición muestra una cobertura desigual respecto del catálogo retenido. Las condiciones de EPP poseen el soporte más sólido: CR-01 cuenta con múltiples fuentes centradas en casco o ausencia de casco, y CR-02 dispone de cobertura adecuada para chaleco, aunque menos redundante. En cambio, CR-03 y CR-04 mantienen brechas directas de cobertura, mientras que CR-05 y CR-06 dependen de entidades auxiliares y contexto parcial, no de etiquetas nativas del patrón de riesgo completo.

**Tabla 28**

*Cobertura de datos por condición y consecuencia metodológica*

| **Condición** | **Nivel de cobertura** | **Fuentes retenidas o apoyo** | **Uso metodológico definido** |
| --- | --- | --- | --- |
| CR-01 - Persona sin casco | Sólida | SHEL5K, CHV, construction_site_safety y ppe_siabar. | Integra el núcleo obligatorio y admite evaluación directa o composición por persona. |
| CR-02 - Persona sin chaleco reflectivo | Adecuada | CHV, construction_site_safety y ppe_siabar. | Integra el núcleo obligatorio, con menor redundancia que CR-01. |
| CR-03 - Trabajo en altura sin anticaídas | Brecha directa | Sin fuente retenida con la condición completa. | Sólo admite evidencia exploratoria sobre componentes o material complementario controlado. |
| CR-04 - Borde elevado desprotegido | Brecha directa | Sin fuente retenida con la condición completa. | Se mantiene como extensión condicionada y no bloquea la aceptación del núcleo. |
| CR-05 - Maquinaria cerca de peatones | Sin cobertura directa retenida | Requiere entidades relacionales y temporalidad. | Su evaluación depende de material específico y lógica contextual. |
| CR-06 - Persona en zona restringida | Sin cobertura directa retenida | Requiere polígono externo y cámara fija. | Su evaluación depende de parametrización espacial externa al prompt. |

*Nota.* La cobertura se refiere a la posibilidad de evaluar la condición operativa completa y no sólo a la presencia de algunas de sus entidades en una colección de imágenes.

Los benchmarks de referencia cumplen un papel más acotado. MOT17 puede utilizarse para verificar instrumentación y cálculo de métricas de seguimiento bajo un protocolo ampliamente conocido; OVT-B puede servir para observar integración entre open vocabulary y seguimiento. Ninguno de los dos se interpretará como evidencia directa de desempeño en construcción civil. Su valor es instrumental: permiten auditar módulos del sistema antes de reinsertarlos en el dominio objetivo.

Esta clasificación evita una sobre-declaración del alcance experimental. En particular, la presencia de entidades relacionadas con CR-03 o CR-04 en una colección de imágenes no habilita por sí sola la validación de la condición completa. Para esas condiciones, el protocolo sólo podrá reportar resultados completos cuando exista evidencia anotada sobre la combinación operativa requerida; de lo contrario, deberá distinguir entre detección de componentes visuales, prueba exploratoria de reglas espaciales y validación efectiva del patrón de riesgo.

La partición de datos se rige por las condiciones metodológicas obligatorias de la Tabla 25.

#### 17.1.7. Framework de métricas, viabilidad operativa y presupuesto de latencia

##### 17.1.7.1. Introducción y alcance

###### 17.1.7.1.1. Propósito y preguntas rectoras

La fundamentación teórica del proyecto E-OVRT-VDP identificó una brecha persistente entre las métricas académicas estándar y la evidencia operativa que debe ofrecer un sistema de alerta asistiva orientado a seguridad laboral. Aunque métricas como AP, HOTA y los indicadores convencionales de rendimiento del pipeline resultan necesarias para la comparabilidad técnica, por sí solas no permiten establecer si el sistema detecta, sostiene y transforma una condición de riesgo en una alerta con la oportunidad, la estabilidad y la trazabilidad requeridas por el dominio.

En ese marco, el framework responde a dos preguntas rectoras de la fundamentación teórica. En relación con P-E1-06, define las métricas para evaluar de manera integral detección OVD, seguimiento multiobjeto, rendimiento del pipeline y desempeño operativo de alerta, junto con umbrales orientativos diferenciados por severidad. En relación con P-E1-01, operacionaliza el presupuesto de latencia admisible mediante una descomposición en componentes medibles y una estimación orientativa compatible con el perfil de hardware de referencia.

El alcance es metodológico: define métricas, niveles de compromiso, criterios de aplicación, umbrales orientativos y requisitos mínimos de instrumentación y reporte, pero no implementa la medición en código ni ejecuta campañas experimentales. Esas tareas corresponden, respectivamente, a la instancia de análisis y diseño arquitectónico y a la validación experimental. Las definiciones formales de las métricas estándar pueden consultarse en las secciones correspondientes de la fundamentación teórica.

En consecuencia, el framework no debe interpretarse como una promesa de ejecución uniforme de todas las métricas definidas, sino como una matriz metodológica de aplicación condicionada. Cada métrica sólo será exigible cuando existan los datos, módulos, referencias de evaluación e instrumentación necesarios para calcularla de manera trazable. Cuando esas condiciones no se cumplan, la salida metodológicamente correcta será declararla como no ejecutada o no aplicable, indicando la causa.

##### 17.1.7.2. Alcance evaluativo y definición operativa de la latencia de alerta

A efectos evaluativos, se distinguen tres tramos temporales que no deben confundirse. El primero es Glass-to-Algorithm (G2A), que mide el intervalo entre la captura o lectura de un cuadro y la disponibilidad del resultado algorítmico asociado a ese cuadro. El segundo es Glass-to-Alert, que mide el intervalo entre el inicio anotado de una condición de riesgo y la generación de una alerta confirmada y registrada dentro del sistema. El tercero es glass-to-glass, que extiende la cadena hasta la visualización remota del video procesado (Axis Communications AB, s. f.; Bachhuber et al., 2018).

La presente sección concentra su validación primaria en el tramo Glass-to-Alert hasta la alerta confirmada y registrada dentro del sistema. En consecuencia, la métrica operativa principal es ⟦ECUACIÓN: no extraída — ver el .docx⟧, entendida como el tiempo entre el inicio anotado del evento y la generación de una alerta registrada luego de la evaluación del patrón correspondiente. Esta definición distingue la alerta de una detección aislada y la ubica como salida operativa trazable del sistema.

En las configuraciones que incluyan un trayecto instrumentado de consulta o notificación, se reportará adicionalmente ⟦ECUACIÓN: no extraída — ver el .docx⟧ como medida complementaria. Esta métrica extiende la medición hacia la disponibilidad de la alerta en el canal definido, pero no forma parte del núcleo evaluativo mínimo.

En este trabajo, la latencia interna hasta el registro de la alerta se identifica como t_alert-system; la extensión hasta un canal instrumentado se identifica como t_alert-notification. Ambas denominaciones deben conservarse sin intercambiar sus hitos de inicio y cierre.

##### 17.1.7.3. Estructura del framework y criterios de viabilidad

El framework se organiza en torno a una jerarquía de métricas y a niveles de compromiso que permiten priorizar evidencia sin sobredimensionar el alcance experimental. La combinación de ambos ejes preserva el rigor metodológico y, al mismo tiempo, reconoce que no todas las métricas útiles son igualmente ejecutables dentro del prototipo experimental.

###### 17.1.7.3.1. Jerarquía de métricas

El framework distingue tres niveles de análisis, cada uno con su unidad de evaluación. El nivel de percepción evalúa detecciones por imagen contra las anotaciones de referencia. El nivel de estado observable por persona determina, para cada persona detectada, si el estado derivado —presencia o ausencia del elemento de protección— coincide con la referencia, componiendo geométricamente las entidades sin requerir identidades persistentes. El nivel de alerta temporal evalúa la alerta confirmada por episodio contra una referencia temporal anotada. Las métricas de detección alimentan el primer nivel; precision y recall por persona, el segundo; y las métricas operativas del apartado 17.1.7.5, el tercero.

La jerarquía del framework se organiza en tres niveles. El nivel primario reúne las métricas que capturan valor operativo directo para el prototipo: ⟦ECUACIÓN: no extraída — ver el .docx⟧, Tiempo a la Primera Detección (TTFD), Tasa de Detección Sostenida (SDR) y Precision/Recall por severidad. El nivel secundario reúne las métricas que explican el comportamiento del detector, del tracker y del pipeline sin constituir por sí mismas evidencia suficiente de valor operativo: AP@0.5, AP@[0.5:0.95], HOTA y los indicadores complementarios de MOT y desempeño computacional. El nivel transversal reúne las métricas de comparación entre variantes zero-shot y fine-tuned, siempre que existan baseline explícita, particiones disjuntas y soporte de datos suficiente.

La pertenencia de una métrica al nivel primario expresa su prioridad interpretativa, no su aplicabilidad automática. Una métrica primaria puede no ejecutarse si el escenario evaluado no dispone de eventos anotados, persistencia temporal, motor de patrones, severidad asignada o logs suficientes. En esos casos, la métrica conserva su rol dentro del framework, pero debe reportarse como no aplicable para esa corrida o condición específica.

Esta jerarquía tiene una consecuencia práctica: si los recursos experimentales no permitieran ejecutar todo el repertorio con la misma profundidad, el núcleo evaluativo del prototipo estará dado por las métricas primarias y por los diagnósticos mínimos del pipeline. Las métricas deseables o conceptuales conservan valor analítico y comparativo, pero no deben desplazar la evidencia central sobre capacidad de alerta.

###### 17.1.7.3.2. Niveles de compromiso

No todas las métricas del framework asumen el mismo nivel de compromiso. Obligatorio designa métricas que el núcleo del prototipo experimental debe reportar para sostener sus conclusiones; deseable designa métricas que enriquecen el análisis, pero cuya omisión no invalida el experimento si se explicita la razón; conceptual designa tratamientos o extensiones metodológicas cuya formulación analítica es pertinente, aunque su evaluación empírica completa exceda el alcance experimental del prototipo.

El nivel de compromiso también depende del alcance efectivamente implementado. Una métrica puede ser obligatoria para condiciones evaluables mediante detección directa o indirecta ya instrumentada, y no resultar exigible allí donde todavía falten módulos de razonamiento contextual, anotación especializada o trayectos completos de notificación.

###### 17.1.7.3.3. Criterios de factibilidad experimental

Una métrica sólo se asumirá como obligatoria cuando cumpla simultáneamente cinco condiciones: necesidad operativa para responder la pregunta de validación del prototipo experimental; disponibilidad de ground truth o referencia verificable; existencia del módulo que produce la señal evaluada; instrumentación suficiente mediante timestamps, logs o exportación de resultados; y costo de anotación o procesamiento compatible con el proyecto. Bajo estos criterios, una métrica puede estar correctamente definida en el framework y, aun así, no corresponder en una corrida concreta. Esta distinción evita validar el prototipo con indicadores que los datos, el entorno o la implementación no permiten sostener.

##### 17.1.7.4. Métricas adoptadas

Las métricas adoptadas cubren los tres planos del sistema evaluable: detección OVD, seguimiento multiobjeto (MOT) y rendimiento del pipeline. La selección no pretende agotar la literatura, sino establecer un conjunto defendible de métricas candidatas y niveles de compromiso coherentes con el alcance del prototipo.

###### 17.1.7.4.1. Métricas de detección OVD

La evaluación del componente de detección open-vocabulary adopta un subconjunto de las métricas estándar revisadas en el análisis de modelos OVD. AP@0.5 y Precision/Recall constituyen el núcleo mínimo por su interpretabilidad, su disponibilidad en herramientas de evaluación consolidadas y su utilidad para contrastar variantes zero-shot y fine-tuned. AP@[0.5:0.95] se conserva como métrica deseable de comparabilidad académica, mientras que NMS-AP permanece en plano conceptual por su valor analítico sobre vocabularios extensos y su menor prioridad operativa en el prototipo experimental.

###### 17.1.7.4.2. Métricas de seguimiento multiobjeto

La evaluación MOT recupera como base las métricas estándar desarrolladas en el análisis de seguimiento multiobjeto, pero recalibra su nivel de compromiso según el alcance efectivo del prototipo experimental. En ese marco, HOTA se conserva como métrica de referencia académica, aunque su cálculo riguroso —al igual que DetA, AssA e IDF1— exige anotaciones cuadro a cuadro con identidades persistentes, por lo que estas métricas quedan como deseables sobre subsets específicamente preparados para MOT. MOTA, IDSW y fragmentación conservan valor diagnóstico complementario en esos mismos subsets.

Para el núcleo del prototipo experimental, la métrica más útil es ⟦ECUACIÓN: no extraída — ver el .docx⟧, incorporada en esta etapa como operacionalización propia y entendida como la diferencia de falsos positivos observada entre corridas equivalentes con y sin tracker habilitado. Su valor metodológico reside en estimar si el seguimiento reduce detecciones espurias o falsas alertas sin exigir ground truth de identidades. No obstante, su interpretación sólo es válida si la unidad de conteo del falso positivo se declara previamente y se mantiene constante durante la comparación.

###### 17.1.7.4.3. Métricas de rendimiento del pipeline

El rendimiento del pipeline integrado constituye una familia de métricas propia, porque la utilidad del sistema no depende sólo de la calidad semántica de detección o seguimiento, sino también del comportamiento sostenido de la cadena completa. FPS efectivos, latencia G2A y consumo de recursos permiten interpretar cuellos de botella, estabilidad temporal y margen operativo del hardware disponible. El análisis de las métricas de rendimiento del pipeline queda desarrollado en la Tabla D.1 del Anexo D.

##### 17.1.7.5. Métricas operativas específicas del dominio

Las métricas estándar de detección, seguimiento y rendimiento aportan comparabilidad técnica, pero no alcanzan por sí solas para describir el valor operativo del sistema en seguridad laboral. En este dominio, no interesa únicamente si el modelo detecta objetos o atributos en un cuadro, sino si el prototipo puede reaccionar frente a una condición de riesgo, sostener evidencia temporal suficiente y transformar esa evidencia en una alerta trazable cuando corresponda.

Por ello, el framework incorpora métricas operativas específicas del dominio: latencia de alerta, tiempo a la primera detección, tasa de detección sostenida y evaluación diferenciada por severidad. Su aplicación queda condicionada por la disponibilidad de secuencias temporales, eventos anotados, criterios de detección positivos previamente definidos e instrumentación suficiente. En consecuencia, estas métricas no deben interpretarse como aplicables a toda corrida experimental, sino como métricas ejecutables sólo cuando los datos y el alcance implementado permiten calcularlas de manera válida.

###### 17.1.7.5.1. Latencia de alerta (⟦ECUACIÓN: no extraída — ver el .docx⟧)

La latencia de alerta se evalúa principalmente mediante ⟦ECUACIÓN: no extraída — ver el .docx⟧. Esta métrica no mide una detección aislada, sino la capacidad del prototipo para transformar evidencia visual en una alerta confirmada y registrada dentro del sistema.

Por lo tanto, ⟦ECUACIÓN: no extraída — ver el .docx⟧ sólo corresponde cuando la corrida incluye, como mínimo, detección OVD, evaluación de patrón, confirmación del patrón y registro interno de la alerta. Una detección temprana puede contribuir a la alerta, pero no la constituye por sí misma si no satisface los criterios de persistencia, severidad o activación definidos para el patrón evaluado.

Cuando la configuración evaluada incluya un trayecto instrumentado de consulta, exposición o notificación, se reportará adicionalmente ⟦ECUACIÓN: no extraída — ver el .docx⟧ como medida complementaria. Esta métrica no forma parte del núcleo mínimo de validación de la alerta, porque depende de componentes de interfaz o comunicación que pueden variar según el diseño arquitectónico adoptado.

###### 17.1.7.5.2. Tiempo a la primera detección (TTFD)

El Tiempo a la Primera Detección, o TTFD, mide el tiempo transcurrido entre el inicio anotado de una condición de riesgo y la primera detección positiva válida producida por el sistema, según el criterio declarado para la corrida. A diferencia de ⟦ECUACIÓN: no extraída — ver el .docx⟧, esta métrica no requiere confirmación por persistencia, evaluación completa del patrón ni generación de alerta. Su función es medir la rapidez con la que el sistema produce la primera evidencia perceptiva asociada a una condición nueva.

TTFD debe interpretarse como una métrica de reacción inicial y no como una métrica de alerta. Una primera detección temprana puede ser útil para reducir la latencia operativa posterior, pero no implica por sí sola que exista un patrón de riesgo confirmado ni una alerta válida dentro del sistema. La transición desde TTFD hacia ⟦ECUACIÓN: no extraída — ver el .docx⟧ depende de que las detecciones posteriores satisfagan los criterios de persistencia, severidad o activación definidos para la condición evaluada.

Esta métrica resulta especialmente informativa en eventos de severidad crítica o alta, donde interesa conocer cuánto tarda el sistema en producir la primera señal visual relevante.

###### 17.1.7.5.3. Tasa de detección sostenida (SDR)

La Tasa de Detección Sostenida, o SDR, mide la proporción del intervalo anotado de una condición de riesgo durante la cual el sistema mantiene detecciones positivas, según el criterio definido para la corrida. Su función es evaluar la estabilidad temporal de la evidencia, no la generación de una alerta.

En el protocolo, SDR permite distinguir entre una detección puntual y una condición sostenida. Una detección aislada puede no ser suficiente para confirmar un patrón de riesgo; por eso, esta métrica aporta evidencia sobre la persistencia necesaria para alimentar la lógica de confirmación del patrón.

###### 17.1.7.5.4. Evaluación diferenciada por severidad

No todos los errores del sistema tienen el mismo impacto operativo. Por ello, el framework adopta como obligación mínima el reporte de Precision y Recall por severidad, o por grupos de condiciones con severidad homogénea, acompañado por el tamaño muestral correspondiente.

Esta evaluación sólo corresponde cuando la severidad haya sido asignada previamente a la condición, patrón o evento evaluado. Si la severidad no fue definida de forma explícita, Precision y Recall podrán reportarse por condición de riesgo, pero no como métricas diferenciadas por severidad.

La asignación formal de pesos distintos a falsos positivos y falsos negativos se mantiene en plano conceptual. Aunque puede ser metodológicamente útil para reflejar diferencias de impacto operativo, depende de criterios de política de riesgo que exceden el alcance del prototipo experimental.

##### 17.1.7.6. Protocolo comparativo entre variantes preentrenada y ajustada al dominio

La comparación entre la variante preentrenada y la variante ajustada al dominio (fine-tuned) debe entenderse como un protocolo evaluativo condicionado, no como un resultado garantizado. Su finalidad es determinar si el ajuste al dominio aporta mejoras medibles sin comprometer la validez experimental ni degradar de manera no controlada la capacidad open-vocabulary del modelo. En ese marco, toda variante ajustada al dominio requiere una baseline zero-shot explícita, evaluada previamente sobre el conjunto de evaluación reservado. Esa baseline constituye el punto de referencia mínimo de toda comparación. En ausencia de baseline zero-shot, soporte de datos suficiente o separación estricta entre entrenamiento y evaluación, el contraste entre variantes no corresponde como evidencia metodológicamente válida.

La separación estricta entre datos de entrenamiento y evaluación es condición de validez experimental y deberá quedar formalizada en la estrategia de datos, benchmarks y partición. Asimismo, la selección de checkpoints no debe hacerse sobre el conjunto de evaluación ni sobre clips o cuadros reutilizados en la línea base o baseline. Toda corrida comparativa deberá conservar el mismo conjunto de evaluación y la misma configuración experimental, salvo la variable que se busque aislar.

Cuando exista una variante ajustada y soporte de datos suficiente para una condición de riesgo determinada, se reportarán los deltas ΔAP, ΔRecall, ΔPrecision y ΔSDR respecto de la baseline zero-shot. Los deltas sobre ⟦ECUACIÓN: no extraída — ver el .docx⟧ y TTFD se consideran deseables cuando la condición evaluada permita medirlos con trazabilidad suficiente. Del mismo modo, resulta deseable verificar si el ajuste al dominio degrada la capacidad open-vocabulary sobre categorías externas al entrenamiento mediante un subset generalista separado del dominio específico.

Toda ejecución de ajuste al dominio debe documentar horas-GPU, tiempo total, horas-persona, cantidad de imágenes y criterios de selección del checkpoint. Sin ese contexto, la ganancia observada pierde interpretabilidad como insumo para decisiones metodológicas.

**Tabla 29**

*Métricas y criterios de reporte para la comparación entre variantes*

| **Métrica** | **Qué captura** | **Relación con métricas estándar** | **Compromiso** | **Nivel** |
| --- | --- | --- | --- | --- |
| ΔAP, ΔRecall, ΔPrecision, ΔSDR por CR-XX | Ganancia del fine-tuning respecto de la baseline zero-shot. | Diferencia entre variantes | Obligatorio si aplica | Transversal |
| Δtalert, ΔTTFD | Verifica que el ajuste al dominio no degrade ⟦ECUACIÓN: no extraída — ver el .docx⟧ ni la respuesta inicial. | Diferencia entre variantes | Deseable | Transversal |
| AP generalista post fine-tuning | Retención de capacidad abierta fuera del dominio de entrenamiento. | Comparación sobre subset generalista | Deseable | Transversal |
| Costo de entrenamiento | Horas-GPU, tiempo total, horas-persona e imágenes utilizadas. | Registro documental | Obligatorio si hay fine-tuning | Transversal |

*Nota.* Δ = diferencia respecto de la baseline zero-shot. La expresión «si aplica» indica que la métrica sólo se exige cuando existe una variante ajustada al dominio, una baseline zero-shot explícita, soporte de datos suficiente y partición estrictamente disjunta entre entrenamiento y evaluación. AP generalista post fine-tuning refiere a la retención de capacidad open-vocabulary fuera del dominio de ajuste.

##### 17.1.7.7. Presupuesto de latencia y componentes medibles

La latencia de alerta se trata aquí como un presupuesto descomponible en componentes observables. En este marco, G2A representa el subtramo instrumental del pipeline por cuadro, mientras que ⟦ECUACIÓN: no extraída — ver el .docx⟧ operacionaliza la latencia de alerta hasta su confirmación interna. En las configuraciones que incluyan un trayecto instrumentado de notificación, se considerará además ⟦ECUACIÓN: no extraída — ver el .docx⟧.

###### 17.1.7.7.1. Descomposición operativa

La descomposición temporal adoptada es la siguiente:

⟦ECUACIÓN: no extraída — ver el .docx⟧

⟦ECUACIÓN: no extraída — ver el .docx⟧

⟦ECUACIÓN: no extraída — ver el .docx⟧

Aquí, ⟦ECUACIÓN: no extraída — ver el .docx⟧ representa la ventana funcional de persistencia necesaria para confirmar el evento, no un costo de cómputo en sentido estricto. El modelo es deliberadamente aditivo y conservador: aunque en una implementación real pueden existir solapamientos, buffering o paralelismo, la descomposición lineal sigue siendo útil para instrumentar mediciones, detectar cuellos de botella y comparar configuraciones.

###### 17.1.7.7.2. Componentes medibles y adscripción por tramo

La descomposición temporal presentada en la subsección anterior sólo resulta metodológicamente útil si cada componente queda adscrito a un tramo evaluativo preciso. En ese marco, la presente tabla no fija valores cerrados por componente, sino que organiza qué partes del retardo pertenecen al subtramo instrumental G2A, cuáles integran la confirmación interna de la alerta operacionalizada como ⟦ECUACIÓN: no extraída — ver el .docx⟧ y cuál corresponde, cuando exista, al trayecto adicional de notificación expresado por ⟦ECUACIÓN: no extraída — ver el .docx⟧. Su función es guiar la instrumentación mínima del sistema efectivamente implementado y evitar que se mezclen costos computacionales, ventanas funcionales de evidencia y demoras externas de interfaz o distribución.

**Tabla 30**

*Componentes del presupuesto de latencia y adscripción a G2A,* ⟦ECUACIÓN: no extraída — ver el .docx⟧ *y* ⟦ECUACIÓN: no extraída — ver el .docx⟧

| **Componente** | **Criterio orientativo** | **Variables dominantes** | **Tramo** | **Compromiso** |
| --- | --- | --- | --- | --- |
| ⟦ECUACIÓN: no extraída — ver el .docx⟧ | Debe medirse como parte del origen temporal de la corrida. | Sensor, buffer de captura, FPS de origen. | G2A | Obligatorio |
| ⟦ECUACIÓN: no extraída — ver el .docx⟧ | Debe medirse sobre el mecanismo de suministro efectivamente utilizado, ya sea red, stream o lectura local instrumentada. | RTSP/WebRTC, RTT, buffering, codificación/decodificación e I/O de lectura. | G2A | Obligatorio |
| ⟦ECUACIÓN: no extraída — ver el .docx⟧ | Incluye transformaciones de entrada y, cuando corresponda, transferencias entre CPU y GPU. | Resize, normalización y movimiento CPU-GPU. | G2A | Obligatorio |
| ⟦ECUACIÓN: no extraída — ver el .docx⟧ | Debe medirse por modelo y resolución; suele concentrar la mayor carga computacional. | Arquitectura OVD, resolución, caching de embeddings. | G2A | Obligatorio |
| ⟦ECUACIÓN: no extraída — ver el .docx⟧ | Corresponde a la ventana funcional de persistencia necesaria para confirmar el evento; no debe confundirse con un costo de cómputo. | Severidad, regla de persistencia, duración mínima del evento y frecuencia de muestreo. | ⟦ECUACIÓN: no extraída — ver el .docx⟧ | Obligatorio cuando exista confirmación por persistencia |
| ⟦ECUACIÓN: no extraída — ver el .docx⟧ | Sólo corresponde si hay tracker. | Método MOT, matching, cantidad de objetos. | ⟦ECUACIÓN: no extraída — ver el .docx⟧ | Obligatorio si hay tracker |
| ⟦ECUACIÓN: no extraída — ver el .docx⟧ | Debe distinguirse de ⟦ECUACIÓN: no extraída — ver el .docx⟧ y medirse como costo computacional de las reglas aplicadas. | Reglas de persistencia, lógica espacial, patrones activos. | ⟦ECUACIÓN: no extraída — ver el .docx⟧ | Obligatorio si existe |
| ⟦ECUACIÓN: no extraída — ver el .docx⟧ | Sólo aplica en configuraciones que incluyan un trayecto instrumentado de notificación hacia interfaz, cliente o canal externo. | MQTT/HTTP/WebSocket, cola de eventos, cliente e interfaz. | ⟦ECUACIÓN: no extraída — ver el .docx⟧ | Deseable |

*Nota.* La tabla organiza los componentes del presupuesto y explicita a qué tramo pertenece cada uno: G2A, ⟦ECUACIÓN: no extraída — ver el .docx⟧ o ⟦ECUACIÓN: no extraída — ver el .docx⟧. No fija valores cerrados por componente; su función es guiar la instrumentación y la interpretación del retardo sobre el sistema efectivamente implementado.

###### 17.1.7.7.3. Cierre operativo del presupuesto

En términos operativos, G2A abarca ⟦ECUACIÓN: no extraída — ver el .docx⟧, ⟦ECUACIÓN: no extraída — ver el .docx⟧, ⟦ECUACIÓN: no extraída — ver el .docx⟧ y ⟦ECUACIÓN: no extraída — ver el .docx⟧. La latencia de alerta hasta su confirmación interna, operacionalizada mediante ⟦ECUACIÓN: no extraída — ver el .docx⟧, agrega, según la configuración evaluada, ⟦ECUACIÓN: no extraída — ver el .docx⟧, ⟦ECUACIÓN: no extraída — ver el .docx⟧ y la ventana funcional ⟦ECUACIÓN: no extraída — ver el .docx⟧. El trayecto de notificación hacia interfaz, cliente o canal externo debe tratarse como una extensión adicional del sistema, expresada mediante ⟦ECUACIÓN: no extraída — ver el .docx⟧, y no como condición para validar el núcleo del prototipo experimental.

###### 17.1.7.7.4. Estimación orientativa del presupuesto de latencia

La descomposición presentada permite construir una estimación orientativa del presupuesto de latencia sin confundir el rendimiento por cuadro del subtramo G2A con la latencia de alerta confirmada expresada por ⟦ECUACIÓN: no extraída — ver el .docx⟧. Esta estimación no reemplaza la calibración empírica de la validación experimental, sino que funciona como referencia de plausibilidad para interpretar los umbrales de la Sección 17.1.7.7.5 y verificar que las metas de ⟦ECUACIÓN: no extraída — ver el .docx⟧ resulten consistentes con el hardware de referencia.

Tomando como perfil de referencia el hardware de inferencia documentado en el entorno experimental, infraestructura y escenarios de evaluación, puede asumirse como orientación inicial un rango de 10 a 50 ms para ⟦ECUACIÓN: no extraída — ver el .docx⟧ + ⟦ECUACIÓN: no extraída — ver el .docx⟧ en una LAN controlada y configurada para baja latencia. Ese orden de magnitud es consistente con la literatura relevada en el análisis de operación en tiempo real, donde la captura a 30 fps impone un piso del orden de un período de cuadro y los protocolos orientados a entornos IP controlados —en particular RTSP/RTP— se presentan como alternativas operativamente convenientes en redes locales cuando el buffering se mantiene acotado (Axis Communications AB, s. f.; Bachhuber et al., 2018).

Para ⟦ECUACIÓN: no extraída — ver el .docx⟧, un rango de 5 a 20 ms constituye una estimación de ingeniería razonable para operaciones de redimensionado, normalización y, cuando corresponda, transferencia entre CPU y GPU sobre cuadros de 640 px; no debe interpretarse como una banda cerrada directamente respaldada por un benchmark único, sino como una aproximación plausible para el perfil experimental adoptado.

Para ⟦ECUACIÓN: no extraída — ver el .docx⟧, conviene tratar el rango de 15 a 150 ms como una banda orientativa de ingeniería para inferencia local acelerada, apoyada en dos referencias complementarias. Por un lado, el análisis de operación en tiempo real identifica un rango de 10–30 ms por cuadro asociado a modelos ligeros optimizados y otro de 50–150 ms característico de arquitecturas transformer sin optimización específica para edge; por otro, el análisis de modelos OVD documenta ejemplos concretos dentro de la familia OVD eficiente, como YOLOE-v8-S (3,3 ms) y YOLOE-v8-L (9,8 ms) sobre T4 con TensorRT, YOLO-World-L (19,2 ms) sobre V100 sin TensorRT, y variantes optimizadas como OmDet-Turbo-Base (10 ms) y G-DINO 1.5 Edge (13,3 ms) sobre A100 con TensorRT (Cheng et al., 2024; Wang et al., 2025).

En este punto, la mención de YOLO-World debe leerse únicamente como referencia comparativa dentro de la subfamilia eficiente de detectores OVD, no como modelo priorizado del protocolo experimental de E2, cuyos candidatos de trabajo siguen siendo YOLOE y Grounding DINO.

Para ⟦ECUACIÓN: no extraída — ver el .docx⟧, un rango de 5 a 20 ms constituye una estimación conservadora y plausible para trackers ligeros de familia tracking-by-detection. En la literatura de referencia del proyecto, SORT se presenta como un método orientado a muy baja carga computacional y ByteTrack como una alternativa que preserva viabilidad en tiempo real dentro de sistemas de seguimiento más completos (Bewley et al., 2016; Zhang et al., 2022); sin embargo, esos valores no deben interpretarse como una cota universal del tracker aislado, sino como órdenes de magnitud útiles para un presupuesto experimental favorable. Para ⟦ECUACIÓN: no extraída — ver el .docx⟧ con reglas simples de persistencia y lógica espacial, un valor menor a 10 ms sigue siendo una estimación de ingeniería plausible, sujeta a verificación empírica.

Bajo estos supuestos, el tramo estrictamente computacional desde la captura hasta la disponibilidad de evidencia utilizable para alerta puede ubicarse orientativamente en el orden de 35 a 250 ms por cuadro cuando se emplean OVD eficientes, red local de baja latencia, tracker ligero y reglas simples. ⟦ECUACIÓN: no extraída — ver el .docx⟧, sin embargo, incorpora además ⟦ECUACIÓN: no extraída — ver el .docx⟧: para severidad crítica, una persistencia orientativa de 2 a 4 s combinada con ese presupuesto computacional vuelve metodológicamente coherente el objetivo de 3 a 5 s; para severidad alta y media, ventanas funcionales más largas hacen igualmente plausibles objetivos orientativos de 5 a 10 s y 10 a 20 s, respectivamente.

El presupuesto precedente corresponde, por tanto, a un escenario favorable de inferencia local sin cuello de botella severo de red y con una familia de modelos optimizada para tiempo real. En este marco, los rangos asignados a ⟦ECUACIÓN: no extraída — ver el .docx⟧ y ⟦ECUACIÓN: no extraída — ver el .docx⟧ deben interpretarse como estimaciones de ingeniería plausibles, pero no como bandas cerradas directamente respaldadas por la bibliografía citada; su validación definitiva corresponde a la calibración empírica de la validación experimental. Si el hardware efectivo difiriera significativamente del perfil de referencia —por ejemplo, por el uso de modelos más pesados, resolución de entrada superior a 640 px o protocolos de transporte con mayor latencia—, los umbrales de la siguiente sección deberán recalibrarse antes de operar como criterio de aceptación.

###### 17.1.7.7.5. Umbrales orientativos por nivel de severidad

La clasificación de severidad definida en la Sección 17.1.5.3.2 exige interpretar los umbrales de aceptación de manera diferenciada según la urgencia de la condición, la persistencia requerida para confirmarla y la tolerancia relativa a falsos positivos y falsos negativos. Los valores que siguen son orientativos: ordenan la evaluación del prototipo y deberán recalibrarse en la validación experimental con el throughput efectivo del pipeline. Los umbrales de TTFD se fijan por debajo de las ventanas orientativas de persistencia para preservar su función como métrica de responsividad inicial y evitar que quede absorbida por el tiempo total de confirmación de la alerta.

**Severidad crítica.** Corresponde a condiciones con potencial de escalada rápida hacia daño grave. Se prioriza minimizar falsos negativos y, por lo tanto, sostener ventanas cortas de confirmación y tiempos exigentes tanto para TTFD como para ⟦ECUACIÓN: no extraída — ver el .docx⟧.

**Severidad alta.** Corresponde a condiciones donde la exposición sostenida incrementa de forma significativa el riesgo, aunque con un margen de intervención algo mayor. Se admite un compromiso intermedio entre rapidez, estabilidad y control de falsas alarmas.

**Severidad media**. Corresponde a condiciones con riesgo latente o de escalada más lenta. En este nivel puede exigirse mayor evidencia antes de confirmar la alerta, con menor tolerancia a falsos positivos y ventanas funcionales de persistencia más largas.

Los umbrales orientativos consolidados se presentan en la Tabla 32 (Sección 17.1.7.9).

##### 17.1.7.8. Operacionalización de la medición y condiciones de no aplicación

Para que el framework sea ejecutable y no meramente declarativo, las métricas anteriores se traducen a requisitos mínimos de instrumentación, preparación y registro. No se redefinen las métricas: se fijan las condiciones bajo las cuales su medición resulta metodológicamente defendible.

###### 17.1.7.8.1. Reglas generales de instrumentación

Toda corrida debe declarar, como mínimo, modelo, versión, checkpoint, variante, resolución de entrada, hardware, entorno de software, protocolo o mecanismo de suministro de video, umbral de confianza, configuración de NMS, vocabulario activo, ventana de persistencia y presencia o ausencia de tracker. Las corridas comparativas deben ejecutarse sobre el mismo conjunto de clips o cuadros y con igual configuración experimental, salvo la variable que se busque aislar. En las corridas que involucren fine-tuning, la semilla de partición, el identificador del split y la composición del corpus deberán quedar registrados de manera explícita para permitir regeneración y auditoría del contraste experimental. Las métricas temporales deben usar timestamps monotónicos, consistentes a lo largo del pipeline y con fuente temporal explícitamente declarada.

En las corridas integradas que reporten métricas de alerta, la instrumentación deberá registrar además los hitos temporales asociados a la evaluación del patrón. Como mínimo, deberán conservarse el timestamp de la detección o evidencia positiva inicial, el timestamp de inicio del patrón candidato cuando corresponda, el timestamp de confirmación del patrón, el timestamp de registro interno de la alerta y, si aplica, el timestamp de disponibilidad, consulta o notificación externa. Estos hitos deben provenir de logs trazables y utilizar una fuente temporal coherente con el resto del pipeline. Sin estos registros, no corresponde reportar ⟦ECUACIÓN: no extraída — ver el .docx⟧ ni ⟦ECUACIÓN: no extraída — ver el .docx⟧; sólo podrán reportarse métricas de detección, rendimiento o reacción inicial, según corresponda.

Toda medición debe incluir un período de calentamiento previo. Las métricas temporales se reportarán, como mínimo, con P50, P95 y P99, además del promedio, salvo que el tamaño muestral no lo permita. Si una métrica depende de ground truth específico inexistente o insuficiente, la salida correcta es declararla no ejecutada, no improvisar una aproximación. Los insumos mínimos por familia de métricas se consolidan en la Tabla D.2 del Anexo D.

###### 17.1.7.8.2. Alcance efectivo y casos en los que no corresponde medir

El compromiso efectivo de cada métrica depende de la condición de riesgo, del escenario de evaluación y de los módulos realmente implementados e instrumentados. En el alcance metodológico ya consolidado del prototipo experimental, CR-01 y CR-02 constituyen el núcleo evaluativo obligatorio por su cobertura de datos y operacionalización directa, mientras que CR-03 a CR-06 permanecen condicionadas a la disponibilidad de evidencia visual, razonamiento contextual e instrumentación suficiente. En consecuencia, las métricas asociadas a condiciones condicionadas podrán ejecutarse de manera parcial o declararse no aplicables sin comprometer la validez del núcleo del prototipo experimental, siempre que esa decisión quede explícitamente justificada en el reporte.

No corresponde medir HOTA, DetA / AssA, IDF1, MOTA, IDSW ni fragmentación sin ground truth con identidades persistentes. Tampoco corresponde comparar variantes zero-shot y fine-tuned si no existe baseline zero-shot explícita o si la partición train/eval no es estrictamente disjunta. En esos casos, la métrica o comparación debe declararse como no aplicable, no como resultado omitido.

En el caso de las métricas de alerta, no corresponde medir ⟦ECUACIÓN: no extraída — ver el .docx⟧ si la configuración evaluada no incluye evaluación de patrón ni registro interno de alerta confirmada. En pruebas puramente cuadro a cuadro, donde sólo se evalúa la salida del detector OVD, las métricas aplicables son las de detección, rendimiento del pipeline o latencia algorítmica. La ausencia de una cadena operativa instrumentada debe declararse explícitamente como condición de no aplicación de las métricas de alerta.

Del mismo modo, no corresponde medir ⟦ECUACIÓN: no extraída — ver el .docx⟧ si la configuración evaluada no incluye un trayecto instrumentado de consulta o notificación, o si dicho trayecto no genera timestamps confiables. Esta métrica sólo debe reportarse cuando la alerta registrada pueda vincularse con un hito posterior verificable de disponibilidad, entrega o consulta en el canal definido.

Tampoco corresponde medir TTFD, SDR ni ⟦ECUACIÓN: no extraída — ver el .docx⟧ sobre imágenes estáticas, datasets sin continuidad temporal o corridas donde no se haya anotado el inicio y fin del evento. No corresponde medir Precision/Recall por severidad si la severidad no fue asignada previamente por condición o evento. No corresponde reportar deltas de fine-tuning si la baseline zero-shot no fue ejecutada sobre el mismo conjunto de evaluación o si existe filtración entre entrenamiento y test. Estas restricciones no reducen el valor del framework; delimitan su aplicación válida.

Una métrica que no corresponde medir se reporta con su estado y su causa —por ausencia de referencia, por fuente sin temporalidad o por trayecto no instrumentado—, nunca como cero ni por omisión.

###### 17.1.7.8.3. Precisiones operativas sobre métricas críticas

En ⟦ECUACIÓN: no extraída — ver el .docx⟧, la unidad de conteo del falso positivo deberá declararse antes de medir —detección por cuadro, evento de alerta o sesión consolidada— y mantenerse idéntica en ambas corridas comparativas. Además, ambas corridas deberán conservar igual configuración experimental, salvo la activación o desactivación del tracker.

Una re-alerta o reconfirmación asociada al mismo episodio no se computa como falso positivo; se registra y se reporta por separado para no confundir repetición de salida con una detección espuria.

En TTFD, la primera evidencia positiva no se confunde con la alerta confirmada. Debe declararse explícitamente qué cuenta como primera evidencia positiva —umbral de confianza, criterio de matching y cualquier filtro previo aplicado—. La definición elegida para la corrida debe permanecer estable y quedar registrada en la bitácora.

En ⟦ECUACIÓN: no extraída — ver el .docx⟧ y ⟦ECUACIÓN: no extraída — ver el .docx⟧, el hito temporal de cierre debe quedar definido antes de medir. En el primer caso, corresponde al registro interno de la alerta generado luego de la confirmación del patrón evaluado; en el segundo, a la emisión, disponibilidad o consulta verificable de la notificación en el trayecto instrumentado. Para que la medición sea válida, los logs deben permitir reconstruir la secuencia mínima entre primera evidencia positiva, patrón candidato si corresponde, patrón confirmado y alerta registrada. Si alguno de estos hitos no se instrumenta de manera confiable, la métrica de alerta debe declararse no aplicable.

En SDR, el criterio de cálculo —tiempo o cuadros válidos— debe declararse explícitamente. Si el throughput resulta inestable, conviene privilegiar el cálculo en tiempo por sobre el conteo puro de cuadros.

En Precision/Recall por severidad, los resultados deben acompañarse del tamaño muestral utilizado, del criterio de agrupamiento aplicado y del punto operativo o umbral con el que fueron calculados, evitando mezclar severidades en una misma lectura agregada.

Los resultados se reportan por estrato y escenario, nunca únicamente como agregado. Los materiales sin la condición objetivo no ingresan en precision, recall ni F1; su métrica es el conteo de falsos positivos. La SDR sólo se compara entre corridas con la misma cadencia de muestreo. La latencia de alerta no se compara entre densidades de evidencia distintas sin controlar qué episodios continúan siendo evaluables.

###### 17.1.7.8.4. Registro mínimo por corrida y reporte

Todo reporte deberá conservar contexto experimental suficiente para reproducir e interpretar la corrida. Como mínimo, la bitácora debe registrar identificación, modelo, entrada, parámetros, hardware y entorno de software, temporalidad y logs, resultados y observaciones. El detalle de campos recomendados se consolida en la Tabla D.3 del Anexo D.

Antes del reporte final debe verificarse que cada métrica corresponda al alcance implementado, que las corridas comparativas usen el mismo conjunto de evaluación y que la instrumentación incluya período de calentamiento previo, duración suficiente y conservación y trazabilidad de logs crudos y artefactos de evaluación. Asimismo, toda métrica no ejecutada deberá declararse junto con la razón metodológica o instrumental de su omisión.

##### 17.1.7.9. Síntesis parcial del framework de métricas

La evidencia central del prototipo no puede reducirse a métricas académicas de detección o seguimiento. Debe mostrar si el sistema detecta una condición relevante, la sostiene durante el tiempo requerido y la transforma en una alerta dentro de un margen compatible con su severidad. Por eso el protocolo diferencia métricas obligatorias, deseables y conceptuales: AP y Precision/Recall se conservan como base de detección, HOTA, IDF1 y CLEAR MOT como métricas de seguimiento cuando exista anotación suficiente, y NMS-AP como referencia conceptual para evaluaciones OVD de vocabulario fino (Everingham et al., 2010; Lin et al., 2014; Bernardin & Stiefelhagen, 2008; Ristani et al., 2016; Luiten et al., 2021; Yao et al., 2024).

La jerarquía no implica ejecución universal: cada métrica queda subordinada a los criterios de ejecutabilidad de la Sección 17.1.7.3.3, por lo que el protocolo distingue entre métricas definidas, métricas efectivamente medibles y métricas no aplicables.

**Tabla 31**

*Jerarquía de métricas adoptadas para el prototipo experimental*

| **Plano** | **Métricas obligatorias** | **Métricas deseables o conceptuales** | **Condición de aplicación** |
| --- | --- | --- | --- |
| OVD | AP@0.5; Precision/Recall con criterio de reporte explícito. | AP@[0.5:0.95] como deseable; NMS-AP como conceptual. | Aplicable a toda condición efectivamente evaluada con ground truth de detección. |
| MOT | ⟦ECUACIÓN: no extraída — ver el .docx⟧ cuando el tracker esté integrado. | HOTA, DetA, AssA, IDF1, MOTA, IDSW y Frag sobre subsets anotados. | Sólo aplica cuando exista tracker y, para las métricas estándar, anotación temporal suficiente. |
| Pipeline | FPS efectivos; ⟦ECUACIÓN: no extraída — ver el .docx⟧; uso de VRAM. | Jitter; uso de GPU, RAM y CPU. | Obligatorio en toda corrida integrada. |
| Alerta | ⟦ECUACIÓN: no extraída — ver el .docx⟧; TTFD; SDR; Precision/Recall por severidad cuando exista evento anotado. | ⟦ECUACIÓN: no extraída — ver el .docx⟧, si existe trayecto instrumentado de consulta o notificación. | Obligatorio cuando exista evento anotado, criterio de activación definido, evaluación de patrón y alerta registrada dentro del sistema. |

*Nota.* ⟦ECUACIÓN: no extraída — ver el .docx⟧= Glass-to-Algorithm. TTFD = Time to First Detection. SDR = Sustained Detection Rate. Lo no implementado o no instrumentado debe declararse como no aplicable y no quedar implícitamente omitido.

La latencia operativa principal es ⟦ECUACIÓN: no extraída — ver el .docx⟧, definida como el intervalo entre el inicio anotado de la condición de riesgo y la generación de una alerta confirmada y registrada dentro del sistema.

**Tabla 32**

*Umbrales orientativos por severidad para la lectura operativa de la alerta*

| **Severidad** | ⟦ECUACIÓN: no extraída — ver el .docx⟧ **máximo orientativo** | **TTFD máximo** | **SDR mínima orientativa** | **Lectura operativa** |
| --- | --- | --- | --- | --- |
| Crítica | 3-5 s | < 1 s | >= 0.50 | Se prioriza no omitir eventos críticos y se admite menor estabilidad inicial. |
| Alta | 5-10 s | < 3 s | >= 0.60 | Se busca equilibrio entre rapidez de respuesta y estabilidad. |
| Media | 10-20 s | < 10 s | >= 0.70 | Puede exigirse mayor evidencia antes de confirmar la alerta, con mayor tolerancia temporal. |

*Nota.* Los valores son orientativos y deberán calibrarse con la evidencia de validación experimental. En consolidación metodológica su función es ordenar prioridades y criterios de lectura, no fijar universales del dominio.

Finalmente, todo reporte experimental deberá conservar trazabilidad mínima de la corrida: modelo, prompts, dataset o fuente de video, parámetros, módulos habilitados, hardware, timestamps, métricas calculadas y métricas no aplicadas con su causa. Esto permite distinguir entre resultado negativo, falta de instrumentación y no aplicabilidad por alcance experimental.

#### 17.1.8. Protocolo experimental integrado

##### 17.1.8.1. Secuencia general del protocolo

La secuencia experimental busca evitar que decisiones tardías alteren la validez comparativa del estudio. Ninguna fase que modifique el estado del modelo o del conjunto de datos debe ejecutarse antes de congelar el software relevante, los checkpoints retenidos, el test set y la estructura mínima de bitácora. Sobre esa base, el protocolo se ordena en fases sucesivas y no como un conjunto abierto de ensayos sin jerarquía.

En cada corrida, el conjunto de métricas aplicables deberá definirse antes de la ejecución según el tipo de evidencia disponible. En DBE sobre imágenes estáticas se priorizarán métricas de detección por imagen o cuadro; las métricas temporales —TTFD, SDR y talert-system— quedarán reservadas para secuencias o corridas con eventos anotados e instrumentación suficiente. Del mismo modo, las métricas de seguimiento sólo serán exigibles sobre subconjuntos con identidades persistentes o en análisis ablativos previamente definidos.

**Tabla 33**

*Fases del protocolo experimental integrado*

| **Fase** | **Objetivo** | **Salida esperada** | **Criterio de cierre** |
| --- | --- | --- | --- |
| Preparación | Congelar entorno, versiones, checkpoints, datasets retenidos y estructura mínima de bitácora. | Artefactos y configuración de corrida documentados. | Reproducibilidad básica garantizada. |
| Baseline DBE | Medir cada modelo candidato en zero-shot sobre el test set congelado. | Línea base por condición, prompt y métrica obligatoria. | Predicciones exportadas y métricas primarias calculadas. |
| Sensibilidad de prompts | Comparar familias de prompts y congelar la formulación primaria por condición. | Matriz comparativa y selección justificada. | Prompt principal y variantes de contraste definidos. |
| Pipeline y seguimiento | Medir tG2A, FPS, recursos y aporte del tracker. | Diagnóstico del comportamiento integrado. | Logs temporales y métricas de estabilidad disponibles. |
| Fine-tuning condicionado | Ejecutar adaptación al dominio sólo si se cumplen las condiciones metodológicas fijadas. | Variante comparativa exportada al CPN. | Comparación válida respecto de baseline y test compartido. |
| EBE complementario | Ejecutar captura continua en entorno controlado o simulado. | Evidencia de plausibilidad operativa y latencia integrada. | Eventos, timestamps y alertas registradas. |
| Reporte | Integrar métricas aplicadas, métricas no aplicables y causas de exclusión. | Informe de resultados trazable y replicable. | Se explicitan alcance, límites y condiciones de interpretación. |

*Nota.* La baseline zero-shot y el test congelado constituyen la base sobre la que recién puede discutirse el valor de prompts, seguimiento o ajuste al dominio. La secuencia expresa dependencias entre fases, no un calendario; el orden y las fechas efectivas de ejecución se documentan en la implementación.

#### 17.1.9. Estrategia de adaptación al dominio

##### 17.1.9.1. Criterio metodológico general

La adaptación al dominio se mantiene como una rama comparativa progresiva y condicionada. No se adopta como requisito previo para demostrar la viabilidad del enfoque OVD, porque eso convertiría una hipótesis todavía no probada en un supuesto metodológico. La baseline zero-shot es el punto de partida obligatorio; el fine-tuning sólo se habilita cuando existe soporte de datos suficiente y cuando la comparación puede sostenerse sin romper la integridad del protocolo.

##### 17.1.9.2. Candidatos de comparación y condiciones de decisión

En términos operativos, la comparación se concentrará como máximo en dos candidatos principales —Grounding DINO y YOLOE— por representar compromisos distintos entre expresividad semántica y eficiencia de inferencia (Liu et al., 2024; Wang et al., 2025). La decisión final sobre cuál o cuáles serán ajustados dependerá de la factibilidad real de integración, exportación y ejecución sobre el CPN, y no sólo de su rendimiento reportado en benchmarks generales.

La rama se define para su ejecución como una jornada experimental completa con criterios prerregistrados: una única baseline, márgenes fijados antes de evaluar y un veredicto determinado por reglas de aceptación previamente declaradas. Sus condiciones de habilitación son de datos y de protocolo, no de disponibilidad de cómputo; el TN constituye el recurso de entrenamiento y el CPN conserva la referencia operativa.

**Tabla 34**

*Regla metodológica de decisión para la adaptación al dominio*

| **Regla** | **Decisión adoptada** | **Sentido metodológico** |
| --- | --- | --- |
| Existencia de baseline | Ningún ajuste se evalúa sin baseline zero-shot previa sobre el mismo test. | Sin baseline explícita no existe comparación defendible. |
| Disponibilidad de datos | Se priorizan CR-01 y CR-02; CR-03 y CR-04 quedan fuera del camino ordinario mientras no exista cobertura suficiente. | El ajuste debe concentrarse donde puede producir evidencia útil y comparaciones metodológicamente válidas. |
| Integridad comparativa | El test set debe ser compartido y permanecer congelado. | Evita leakage y falsas mejoras por cambio de evaluación. |
| Ganancia exigible | La variante ajustada debe mostrar una mejora operativamente significativa y no una ventaja marginal difícil de sostener. | Protege al protocolo de ciclos costosos de ajuste con retorno metodológico débil. |
| Costo operativo | La variante ajustada no debe comprometer materialmente la latencia ni el presupuesto de recursos del CPN. | Una mejora semántica que destruye la viabilidad operativa no fortalece al prototipo. |

*Nota.* La regla no prescribe que el fine-tuning deba ejecutarse; define cuándo vale la pena hacerlo sin distorsionar el objetivo principal del prototipo experimental.

#### 17.1.10. Supuestos, riesgos de validez y consideraciones ético-legales

##### 17.1.10.1. Política de minimización y uso asistivo

El marco ético-legal del proyecto se apoya en una política de minimización de datos y de uso asistivo del sistema. Cuando la evaluación utilice datasets públicos o material pregrabado sin nuevas capturas, el requisito central será respetar licencias, condiciones de acceso y límites de uso académico. Cuando el proyecto genere material propio para el EBE, deberán adoptarse salvaguardas de finalidad explícita, acceso restringido, retención acotada y ausencia de reconocimiento de identidad personal o tratamiento biométrico, conforme al régimen argentino de protección de datos personales y videovigilancia (Argentina, 2000; Disposición 10/2015, 2015). Ese régimen contempla, además, requisitos administrativos asociados a las bases de datos con datos personales ante la autoridad de aplicación (AAIP), cuya aplicabilidad al contexto experimental debe determinarse; la decisión y el recaudo adoptado se documentan a continuación.

[[PENDIENTE: definir con el equipo la aplicabilidad de esta inscripción al contexto experimental y documentar el recaudo adoptado en §17.1 y §17.4.]]

##### 17.1.10.2. Supuestos de interpretación

También conviene fijar con claridad los supuestos de interpretación. Primero, el prototipo es un sistema asistivo: una alerta no equivale a una sanción ni a una determinación automática de incumplimiento normativo. Segundo, la evaluabilidad de varias condiciones depende de variables no controlables del todo por el detector, como escala aparente, ángulo de cámara, oclusión o iluminación. Tercero, CR-06 presupone una parametrización espacial externa al prompt y no debe evaluarse como si el lenguaje por sí solo definiera la zona restringida. Cuarto, el EBE constituye una validación en entorno simulado o controlado, no un despliegue real en obra.

Quinto, la disyunción entre datos de entrenamiento y conjunto de evaluación sólo es verificable sobre el ajuste propio del trabajo: los modelos preentrenados de vocabulario abierto provienen de corpus de terceros no inspeccionables, por lo que no puede descartarse que imágenes del conjunto de evaluación hayan participado de ese preentrenamiento. Es una condición estructural de toda evaluación de modelos preentrenados y no una particularidad de este protocolo; acota las cifras zero-shot a una comparación entre combinaciones bajo condiciones idénticas, sin sostener afirmaciones sobre generalización a material inédito.

**Tabla 35**

*Riesgos metodológicos y operativos relevantes para las instancias siguientes*

| **Riesgo** | **Impacto probable** | **Mitigación adoptada** |
| --- | --- | --- |
| La configuración retenida excede el presupuesto de VRAM o rompe la latencia esperada del CPN. | Alto | Priorizar variantes ejecutables en la laptop, ajustar resolución y composición del vocabulario activo y justificar toda optimización sobre el CPN. |
| Persisten brechas de datos para condiciones de Niveles 2 y 3. | Alto | Mantener esas condiciones como extensiones condicionadas y producir datos complementarios sólo si no desplazan el núcleo del prototipo experimental. |
| El tracker agrega complejidad sin reducir falsas alarmas. | Medio | Medir primero ΔFPtracking y sólo exigir métricas MOT completas en subsets donde el costo de anotación esté justificado. |
| El diseño experimental se vuelve inmanejable por exceso de variables combinadas. | Alto | Sostener un diseño reducido con condición base, barridos acotados y prueba de mayor exigencia sólo sobre la configuración retenida. |
| La generación de material propio introduce dudas de privacidad o de consentimiento. | Medio | Aplicar las salvaguardas de la Sección 17.1.10.1, con registro explícito de finalidad y condiciones de captura. |

*Nota.* La mitigación forma parte del diseño metodológico. En varios casos, preservar validez implica acotar el alcance antes que incrementar complejidad sin evidencia suficiente.

#### 17.1.11. Conclusiones parciales de la consolidación metodológica

##### 17.1.11.1. Cierre del alcance metodológico

La consolidación metodológica queda cerrada con un protocolo experimental integrado, consistente con las dimensiones desarrolladas y ajustado al alcance real del prototipo. Ese cierre se expresa en seis definiciones principales: núcleo obligatorio centrado en condiciones de detección directa de Nivel 1; separación entre comparación controlada en DBE y plausibilidad operativa en EBE; estrategia de datos y partición orientada a evitar leakage; framework de métricas centrado en valor operativo de alerta; regla explícita para habilitar o descartar adaptación al dominio; y proyección metodológica que ordena el pasaje hacia diseño, implementación y validación.

##### 17.1.11.2. Articulación con las instancias de diseño e implementación

Las definiciones consolidadas en esta instancia orientan directamente las etapas siguientes del trabajo. El análisis y diseño arquitectónico transforma el protocolo metodológico en una organización técnica consistente, mientras que la validación experimental produce resultados sobre las condiciones, escenarios y métricas fijadas. En todos los casos, deberá declararse qué elementos del catálogo fueron implementados, cuáles no aplicaron y cuáles permanecieron condicionados. Esa trazabilidad entre definición metodológica, diseño, implementación y validación constituye el principal resultado de esta parte del proyecto.

Esta consolidación distribuye sus salidas hacia las instancias siguientes sin anticipar resultados: la caracterización del entorno restringe la arquitectura y sus perfiles de ejecución; las condiciones de riesgo y el protocolo de prompts determinan configuraciones y comparaciones; la estrategia de datos gobierna la curación, la partición y la trazabilidad durante la implementación; y el framework de métricas define la instrumentación de ⟦ECUACIÓN: no extraída — ver el .docx⟧, ⟦ECUACIÓN: no extraída — ver el .docx⟧ y los criterios con los que se interpreta la evaluación.

Estas definiciones preservan el carácter experimental del trabajo y mantienen la orientación central del proyecto: evaluar si la detección open-vocabulary puede integrarse como herramienta asistiva útil para el monitoreo de condiciones de riesgo en construcción civil, sin reemplazar la supervisión humana ni asumir decisiones operativas automáticas.
