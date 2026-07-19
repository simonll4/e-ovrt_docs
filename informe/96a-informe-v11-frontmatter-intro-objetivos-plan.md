# 96a — Texto extraído del informe v1.1: frontmatter, introducción, objetivos y plan (§2-14)

> **Extracción derivada (2026-07-18)** del `.docx`
> `informe/E-OVRT-VDP_v1.1_05062026-sin-indice.docx`, **solo para búsqueda y cita**
> (mismo estatuto que el doc 90): al editar, se edita el `.docx`/Google Docs, nunca
> este archivo. Tablas y figuras pueden haber perdido formato; las figuras no se
> extraen. **La §17.3 embebida en el docx NO se incluye en esta serie: está
> desactualizada** — la Etapa 3 vigente es el doc 90 (extracción del standalone).
> Partición completa: 96a (frontmatter+intro+objetivos+plan), 96b (§17.1
> consolidación metodológica — el protocolo), 96c (estado del arte), 96d (marco
> teórico), 96e (cierre+anexos+referencias).

---

CENTRO REGIONAL UNIVERSITARIO CÓRDOBA IUA

FACULTAD DE INGENIERÍA

PROYECTO INTEGRADOR

PLATAFORMA EXPERIMENTAL DE DETECCIÓN OPEN-VOCABULARY EN VIDEO EN TIEMPO REAL PARA MONITOREO ASISTIVO DE RIESGOS EN CONSTRUCCIÓN

INGENIERÍA EN INFORMÁTICA

TUTOR

García Mattio, Mariano

INTEGRANTES

Carrizo, Matías Lautaro

Guillaumet, Gabriel Agustín

Llamosas, Simon


## 2. Hoja de Aceptación del Trabajo Final

[se completará más adelante]


## 3. Dedicatoria

[se completará más adelante]


## 4. Agradecemientos

[se completará más adelante]


## 5. Título del proyecto

Plataforma experimental de detección open-vocabulary en video en tiempo real para monitoreo asistivo de riesgos en construcción.


## 6. Abstract


### Resumen

[se completará más adelante]


### Abstract

[se completará más adelante]


## 7. Palabras Claves

Detección de vocabulario abierto

Modelos visión-lenguaje

Visión por computadora

Procesamiento de video en tiempo real

Streaming de baja latencia

Seguridad laboral en construcción civil

Patrones de riesgo

Arquitectura orientada a eventos

Trazabilidad experimental

Seguimiento multiobjeto


## 11. Glosario, Listado de Símbolos y Convenciones

Tabla 1

Glosario y listado de símbolos y convenciones del proyecto E-OVRT-VDP


| Término / sigla | Definición / uso en el trabajo |
| --- | --- |
| E-OVRT-VDP | Sigla propuesta para Experimental Open-Vocabulary Real-Time Video Detection Platform, nombre abreviado de la plataforma experimental del trabajo. |
| IA | Inteligencia Artificial. Disciplina orientada al desarrollo de sistemas capaces de realizar tareas que normalmente requieren inteligencia humana. |
| CV | Computer Vision o visión por computadora. Área de la inteligencia artificial dedicada al procesamiento e interpretación de imágenes y video. |
| OVD | Open-Vocabulary Detection. Paradigma de detección que permite localizar objetos o condiciones expresadas mediante lenguaje natural, sin depender exclusivamente de clases cerradas predefinidas. |
| Closed-set detection | Detección de vocabulario cerrado. Enfoque en el que el modelo solo reconoce categorías definidas durante su entrenamiento. |
| Open-set | Capacidad de un sistema para operar frente a categorías no vistas o no previstas durante el entrenamiento. |
| Zero-shot | Modalidad de inferencia en la que el modelo intenta reconocer conceptos no observados explícitamente durante el entrenamiento supervisado. |
| Prompt | Consulta o instrucción, generalmente textual, que especifica el concepto o condición que se desea detectar. |
| Prompt visual | Imagen o región de referencia utilizada para especificar visualmente el objeto o condición de interés. |
| Fine-tuning | Ajuste de un modelo preentrenado mediante datos adicionales de un dominio específico. |
| LoRA | Low-Rank Adaptation. Técnica de ajuste eficiente de parámetros usada para adaptar modelos con menor costo computacional. |
| MOT | Multi-Object Tracking. Seguimiento multiobjeto; técnica para mantener identificadores consistentes de personas u objetos a lo largo del video. |
| Tracking-by-detection | Paradigma de seguimiento en el que primero se detectan objetos por fotograma y luego se asocian temporalmente entre cuadros consecutivos. |
| EPP | Equipo de Protección Personal. Elementos destinados a proteger al trabajador, como casco, chaleco, guantes, calzado de seguridad o arnés. |
| PPE | Personal Protective Equipment. Equivalente en inglés de EPP. |
| Patrón de riesgo | Combinación de una o más condiciones observables que, por su presencia, persistencia o relación espacial, representan una situación relevante para la seguridad. |
| Condición de riesgo observable | Situación físicamente visible en imagen o video que puede asociarse a un incumplimiento, peligro o señal preventiva relevante. |
| EDA | Event-Driven Architecture. Arquitectura orientada a eventos, donde los componentes se comunican mediante eventos producidos y consumidos de forma desacoplada. |
| Plano de medios | Parte del sistema dedicada al flujo continuo de video: captura, transporte, decodificación, procesamiento y visualización. |
| Plano de control | Parte del sistema dedicada a eventos, reglas, alertas, configuración, trazabilidad y orquestación de decisiones no multimedia. |
| Streaming | Transmisión continua de datos multimedia, como audio o video, sin requerir descarga completa previa. |
| Latencia end-to-end | Tiempo total transcurrido entre la captura de un evento en la escena y su disponibilidad o visualización en el sistema destino. |
| Latencia de alerta | Tiempo transcurrido entre el inicio observable de una condición de riesgo y la generación efectiva de una alerta por parte del sistema. |
| FPS | Frames per second o cuadros por segundo. Métrica de rendimiento que indica cuántos fotogramas procesa o visualiza el sistema por segundo. |
| Precisión | Proporción de detecciones positivas del sistema que son realmente correctas. |
| Recall | Proporción de instancias relevantes reales que fueron detectadas por el sistema. |
| F1-score | Media armónica entre precisión y recall; se utiliza para evaluar balanceadamente el desempeño de detección. |
| AP | Average Precision. Métrica de precisión promedio utilizada frecuentemente en detección de objetos. |
| mAP | Mean Average Precision. Promedio de AP sobre múltiples clases o umbrales, utilizado en benchmarks de detección. |
| MOTA | Multiple Object Tracking Accuracy. Métrica clásica para evaluar seguimiento multiobjeto. |
| IDF1 | Métrica de seguimiento que evalúa la consistencia de identidad de los objetos rastreados. |
| HOTA | Higher Order Tracking Accuracy. Métrica de tracking que combina detección, asociación e identidad. |
| DBE | Dataset-Based Evaluation. Escenario de evaluación basado en datasets previamente seleccionados y anotados. |
| EBE | Environment-Based Evaluation. Escenario de evaluación basado en un entorno controlado o representativo de obra. |
| CPN | Central Processing Node. Nodo central de procesamiento encargado de ejecutar inferencia, evaluación de patrones o servicios principales. |
| EN | Edge Node. Nodo cercano a la fuente de captura, usado para adquisición, preprocesamiento o transmisión de video. |
| TN | Training Node. Nodo destinado a entrenamiento o adaptación de modelos, cuando corresponda. |
| Dataset | Conjunto de datos utilizado para entrenamiento, validación, prueba o análisis experimental. |
| Benchmark | Conjunto de referencia o procedimiento estandarizado para comparar desempeño entre modelos o configuraciones. |
| API | Application Programming Interface. Interfaz que permite que distintos componentes de software se comuniquen de forma estructurada. |
| Prototipo experimental | Versión funcional acotada de la plataforma, desarrollada con fines de investigación, validación técnica y evaluación controlada. Integra los componentes necesarios para poner a prueba la hipótesis de trabajo, sin constituir un producto final ni una solución lista para despliegue productivo. |
| IoT | Internet of Things. Conjunto de dispositivos y protocolos orientados a la interconexión de objetos físicos mediante redes. |
| MQTT | Protocolo ligero de mensajería publish/subscribe usado habitualmente en sistemas IoT. |
| RTSP | Real Time Streaming Protocol. Protocolo utilizado para controlar transmisiones de medios en tiempo real. |
| RTP | Real-time Transport Protocol. Protocolo de transporte para audio y video en tiempo real. |
| RTMP | Real-Time Messaging Protocol. Protocolo tradicional de transmisión multimedia usado en streaming. |
| WebRTC | Tecnología y conjunto de protocolos para comunicación de audio, video y datos en tiempo real con baja latencia. |
| SRT | Secure Reliable Transport. Protocolo de transporte de video orientado a confiabilidad y baja latencia en redes variables. |
| HLS | HTTP Live Streaming. Protocolo de streaming segmentado sobre HTTP. |
| DASH | Dynamic Adaptive Streaming over HTTP. Técnica de streaming adaptativo basada en segmentos HTTP. |
| GStreamer | Framework multimedia utilizado para construir pipelines de captura, procesamiento y transmisión de audio/video. |
| FFmpeg | Conjunto de herramientas y bibliotecas para procesamiento, conversión, codificación y transmisión multimedia. |
| NVDEC | Decodificador de video por hardware de NVIDIA, utilizado para descargar la decodificación desde CPU hacia GPU. |
| TensorRT | SDK de NVIDIA para optimización y aceleración de inferencia de modelos de aprendizaje profundo. |
| Edge Computing | Paradigma de procesamiento cercano a la fuente de datos, orientado a reducir latencia y carga de red. |
|  | Tiempo entre el inicio observable de una condición de riesgo y el registro interno de la alerta confirmada por el sistema. |
|  | Tiempo entre el registro interno de la alerta confirmada y su entrega por un canal externo de notificación. |
| TTFD | Time To First Detection. Tiempo hasta la primera detección de una condición relevante desde su aparición observable. |
| SDR | Sustained Detection Rate. Tasa de detección sostenida. Indica si una condición se mantiene detectada durante una ventana temporal definida. |
| Latencia de inferencia | Tiempo que tarda el modelo en procesar una entrada visual y producir detecciones. |
| Latencia por tramo | Tiempo medido en una etapa específica del flujo, como ingesta, inferencia, postproceso, publicación o evaluación de patrón. |


## 12. Introducción


### 12.1. Motivación y contexto del proyecto

La seguridad laboral en la industria de la construcción civil constituye un problema de alta relevancia técnica, social y organizacional. Se trata de un sector caracterizado por entornos dinámicos, tareas simultáneas, circulación de personas y maquinaria, estructuras temporales, cambios frecuentes en la disposición del espacio de trabajo y exposición permanente a condiciones de riesgo. En este contexto, la supervisión visual cumple un papel preventivo relevante, pero también presenta limitaciones cuando depende exclusivamente de la observación humana continua sobre múltiples cámaras o frentes de obra.

El presente Proyecto Integrador surge de la necesidad de explorar una alternativa tecnológica capaz de complementar la supervisión tradicional mediante una plataforma experimental de detección open-vocabulary en video en tiempo real. La motivación central no consiste en reemplazar al supervisor humano ni en automatizar decisiones de cumplimiento normativo, sino en investigar si los modelos actuales de visión-lenguaje pueden contribuir a identificar de manera flexible señales visuales asociadas a condiciones de riesgo en entornos de construcción. De esta forma, el proyecto se ubica en la intersección entre inteligencia artificial, visión por computadora, procesamiento de video en tiempo real, seguridad laboral y diseño responsable de sistemas asistivos.

La elección del tema se fundamenta en una brecha concreta. Los sistemas tradicionales de detección de objetos operan, en general, bajo un paradigma de vocabulario cerrado, es decir, solo reconocen categorías previstas durante su entrenamiento. Esta característica resulta problemática en obras civiles, donde los riesgos no siempre pueden anticiparse como una lista fija de objetos o clases. Una condición como "persona sin casco cerca de una excavación", "material obstruyendo un pasillo de circulación" o "trabajador en zona de tránsito vehicular" combina objetos, atributos, relaciones espaciales, contexto operativo y persistencia temporal. Por ello, un sistema cerrado puede resultar insuficiente si no fue entrenado explícitamente para cada combinación posible.

Frente a esta limitación, los enfoques de detección de vocabulario abierto permiten formular consultas mediante lenguaje natural o, eventualmente, imágenes de referencia. Esta capacidad habilita un modo de interacción más flexible: el usuario puede definir condiciones de interés sin depender exclusivamente de un conjunto rígido de etiquetas preestablecidas. En consecuencia, el proyecto propone evaluar la factibilidad técnica y académica de una plataforma que procese video, interprete consultas open-vocabulary, detecte entidades o condiciones observables, aplique criterios de persistencia o patrones de riesgo y genere alertas asistivas trazables.


### 12.2. Problema identificado

El problema que orienta el trabajo puede expresarse como una discontinuidad entre la naturaleza dinámica y semánticamente abierta de los riesgos en obra y la naturaleza estática de los sistemas de detección visual basados en vocabularios cerrados. Mientras que el entorno de construcción introduce situaciones variables, dependientes del contexto y difíciles de reducir a categorías fijas, muchos sistemas de visión computacional requieren que las clases detectables hayan sido definidas, anotadas y entrenadas previamente.

Esta restricción genera consecuencias prácticas. En primer lugar, una condición no contemplada durante el diseño del sistema puede quedar fuera de su capacidad de detección, aunque sea relevante para la seguridad. En segundo lugar, incorporar nuevas clases o combinaciones suele exigir procesos de recolección de datos, anotación, entrenamiento y validación que pueden ser costosos en tiempo y recursos. En tercer lugar, la detección por fotograma aislado no basta para representar situaciones de riesgo que dependen de duración, reiteración o trayectoria, por lo que el análisis de video requiere además mecanismos de persistencia temporal y criterios operativos para distinguir detecciones aisladas de eventos significativos.

A esta problemática técnica se suma una dimensión operativa: el monitoreo de múltiples cámaras o zonas de trabajo impone una carga cognitiva elevada sobre los responsables de seguridad. La observación humana continua puede verse afectada por fatiga, distracciones, simultaneidad de eventos o limitaciones propias de la atención sostenida. Por ello, una herramienta de detección asistiva puede funcionar como una capa adicional de apoyo, siempre que se mantenga dentro de un marco responsable, trazable y no vinculante.

El proyecto no parte de la premisa de que la inteligencia artificial pueda resolver por sí sola la seguridad en obra. Por el contrario, reconoce que una alerta visual no equivale a una determinación jurídica ni técnica de incumplimiento. La función del sistema propuesto es detectar indicios observables, registrar evidencia, activar patrones previamente definidos y asistir a la supervisión humana. Esta delimitación resulta central para sostener el carácter experimental del trabajo y evitar una interpretación excesiva de las capacidades del prototipo.


### 12.3. Enfoque propuesto e hipótesis de trabajo

La hipótesis de trabajo sostiene que los modelos de detección open-vocabulary, al permitir expresar condiciones de interés mediante lenguaje natural en tiempo de inferencia, constituyen un habilitador tecnológico viable para superar parte de la rigidez de los sistemas closed-set en el contexto del monitoreo visual de seguridad en construcción. Bajo esta hipótesis, una plataforma experimental podría recibir consultas o patrones como "persona sin casco", "persona sin chaleco reflectivo" o "maquinaria cerca de peatones" y transformarlos en eventos analizables dentro de un flujo de video.

Sin embargo, esta hipótesis se formula de manera condicionada. La viabilidad de la solución no depende únicamente de que un modelo pueda detectar objetos en imágenes estáticas, sino de la integración de múltiples dimensiones: selección de modelos visión-lenguaje, rendimiento en hardware disponible, estabilidad temporal de las detecciones, estrategia de prompts, disponibilidad de datasets, presupuesto de latencia, arquitectura de streaming, trazabilidad de eventos y restricciones ético-legales asociadas al tratamiento de vídeo en contextos laborales.

Por este motivo, el proyecto se estructura como una plataforma experimental y no como un producto industrial terminado. El objetivo es construir un prototipo experimental que permita evaluar el comportamiento del enfoque bajo condiciones controladas y reproducibles. La solución esperada se organiza alrededor de una cadena operativa mínima: ingesta o lectura de video, inferencia open-vocabulary, eventual seguimiento temporal, evaluación de patrones de riesgo, registro de eventos y generación de alertas asistivas. Esta cadena permite analizar no sólo la precisión de detección, sino también la oportunidad, estabilidad y utilidad operativa de las alertas generadas.

La propuesta también contempla la comparación entre una línea base zero-shot y eventuales estrategias de adaptación al dominio únicamente cuando existan datos, soporte metodológico e infraestructura suficientes. De esta forma, el ajuste de modelos no se asume como punto de partida, sino como posibilidad condicionada a la evidencia disponible. Esta decisión preserva el sentido open-vocabulary del proyecto y evita convertir la adaptación al dominio en un requisito previo de factibilidad.


### 12.4. Alcance, límites y condiciones de trabajo

El alcance del trabajo se circunscribe al desarrollo y evaluación de una plataforma experimental de detección open-vocabulary en video en tiempo real aplicada al dominio de seguridad en construcción civil. El prototipo se orienta a condiciones observables visualmente, especialmente aquellas vinculadas con uso de elementos de protección personal, presencia de personas en zonas de riesgo, interacción entre peatones y maquinaria, obstrucciones del entorno y otros patrones que puedan formularse como consultas o reglas evaluables.

No se busca construir un sistema de fiscalización automática ni una herramienta de certificación normativa. Las alertas generadas por el prototipo se interpretan como señales asistivas destinadas a apoyar la supervisión humana. En consecuencia, el sistema no sustituye la evaluación técnica en terreno, no define responsabilidades legales, no toma decisiones operativas autónomas y no activa medidas físicas de control. Su valor se analiza como instrumento de apoyo, trazabilidad y experimentación académica.

El prototipo no incluirá reconocimiento de identidad personal. La detección se limitará a entidades y condiciones observables, tales como "persona", "casco", "chaleco", "maquinaria" o "zona restringida", sin asociar individuos a nombres, credenciales o perfiles personales. Esta restricción responde tanto a criterios ético-legales como al alcance técnico del trabajo. Del mismo modo, la versión experimental no contempla integración completa con sistemas externos de gestión de seguridad ni con infraestructura física de alarmas, aunque podrá prever mecanismos básicos de notificación o registro para demostrar interoperabilidad futura.

También se asumen condiciones experimentales controladas. El trabajo prioriza escenarios reproducibles, datasets de referencia y, cuando corresponda, un entorno simulado o representativo de obra. La evaluación se organizará en dos planos complementarios: una evaluación basada en datasets, orientada a comparabilidad, control de variables y repetibilidad; y una evaluación basada en entorno, orientada a observar el comportamiento del pipeline sobre captura continua y variables visuales realistas. La disponibilidad de datos, hardware y tiempo de desarrollo condicionará el grado de profundidad de cada escenario.

El proyecto utilizará, prioritariamente, modelos preentrenados y herramientas disponibles, evitando el entrenamiento desde cero por exceder el alcance académico y computacional previsto. Las decisiones sobre fine-tuning, prompts, tracking, servidores de medios o frameworks de inferencia deberán justificarse según criterios de viabilidad técnica, reproducibilidad, licenciamiento, desempeño y compatibilidad con el hardware disponible. En este sentido, el trabajo no se mide por alcanzar una solución industrial completa, sino por construir evidencia suficiente para evaluar la factibilidad del enfoque.


### 12.5. Enfoque metodológico general

El desarrollo del proyecto adopta un enfoque progresivo e iterativo. En primer lugar, se construye una fundamentación teórica orientada a delimitar el problema, revisar el estado del arte y establecer criterios conceptuales. Esta instancia permite responder qué debe detectar el sistema, cómo pueden interpretarse consultas de lenguaje natural, qué restricciones impone el video en tiempo real, qué papel cumple el seguimiento temporal y bajo qué condiciones ético-legales puede analizarse video en contextos laborales.

En segundo lugar, la fundamentación se traduce en una consolidación metodológica que define condiciones de riesgo, patrones, escenarios de evaluación, infraestructura disponible, estrategia de datos, protocolo de prompts, métricas y presupuesto de latencia. Esta etapa cumple una función de puente entre el análisis conceptual y la implementación, ya que transforma criterios generales en decisiones operativas evaluables.

Posteriormente, el trabajo avanza hacia el diseño arquitectónico de la plataforma, donde se definirán los módulos, flujos de datos, contratos de interfaz, separación entre plano de medios y plano de control, mecanismos de registro y criterios de integración. La implementación del prototipo materializará esas decisiones en una versión mínima reproducible. Finalmente, la validación experimental permitirá medir el comportamiento del sistema, identificar dificultades, discutir limitaciones y proponer líneas futuras.

La metodología se orienta a la trazabilidad. Cada decisión técnica relevante deberá poder vincularse con una necesidad del problema, un criterio derivado del marco teórico, una restricción metodológica o una condición experimental. Por ello, las matrices comparativas extensas, catálogos completos de prompts, inventarios de datasets, detalles de infraestructura y registros de medición se conservarán como anexos o evidencia complementaria, mientras que el cuerpo principal mantendrá únicamente la información relevante para sostener la argumentación central del proyecto.


## 13. Objetivo Del Proyecto


### 13.1. Objetivo general

Diseñar, implementar y evaluar la factibilidad técnica de una plataforma experimental de detección open-vocabulary en video en tiempo real, orientada a la identificación asistiva de condiciones de riesgo en obras de construcción civil, mediante la integración de modelos de visión-lenguaje, procesamiento de video de baja latencia, seguimiento temporal, patrones de riesgo y mecanismos de alerta evaluables bajo condiciones controladas.


### 13.2. Objetivos específicos

Analizar el estado del arte y los fundamentos técnicos, metodológicos, normativos y ético-legales vinculados con la detección open-vocabulary, el seguimiento multiobjeto, la transmisión de video en tiempo real y la seguridad laboral en construcción civil, a fin de establecer criterios de diseño y evaluación para la plataforma experimental.

Definir y operacionalizar un conjunto de condiciones de riesgo visualmente observables en entornos de obra, vinculándolas con patrones de riesgo, niveles de severidad, criterios de persistencia temporal y formulaciones de consulta compatibles con modelos de detección open-vocabulary.

Diseñar una arquitectura modular de procesamiento de video en tiempo real que distinga el plano de medios y el plano de control, permitiendo integrar de manera desacoplada componentes de ingesta, inferencia, seguimiento temporal, evaluación de patrones, registro de eventos y generación de alertas.

Implementar un prototipo experimental capaz de ejecutar el flujo experimental previsto, incorporando ingesta o lectura de video, inferencia open-vocabulary, evaluación de patrones de riesgo, registro de eventos, alertas internas e instrumentación de métricas técnicas y operativas.

Evaluar el desempeño del prototipo mediante un protocolo experimental reproducible, considerando escenarios basados en datasets y escenarios controlados representativos, con métricas de detección, seguimiento, rendimiento del pipeline, latencia de alerta y utilidad operativa de las notificaciones generadas.

Incorporar lineamientos de ética, privacidad y seguridad de la información acordes con el uso responsable de sistemas de análisis automatizado de video en contextos laborales, manteniendo el carácter asistivo de las alertas y evitando mecanismos de reconocimiento de identidad personal.

Documentar las decisiones técnicas, metodológicas y experimentales adoptadas durante el desarrollo del proyecto, junto con sus resultados, limitaciones, evidencias generadas y posibles líneas de continuidad o mejora futura.


## 14. Plan De Trabajo De Proyecto Integrador


### 14.1. Enfoque general de trabajo

Se adopta un proceso iterativo-incremental, de inspiración ágil, orientado a construir progresivamente la plataforma experimental y la evidencia académica asociada. El avance se organiza en ciclos de planificación, ejecución, verificación y ajuste, priorizando las tareas según su aporte directo a los objetivos del proyecto. Esta metodología permite incorporar hallazgos de investigación, restricciones técnicas emergentes y resultados preliminares sin alterar el propósito general del trabajo.

La documentación acompaña cada etapa del proceso. Las decisiones técnicas, configuraciones, supuestos, limitaciones, pruebas y resultados parciales se registran a medida que se producen, favoreciendo la reproducibilidad del prototipo y la trazabilidad de las decisiones adoptadas. Esta forma de trabajo permite distinguir qué decisiones derivan del análisis teórico, cuáles responden a restricciones metodológicas y cuáles surgen de la implementación concreta del sistema.


### 14.2. Etapas del proyecto


#### 14.2.1. Etapa 1 - Investigación bibliográfica y fundamentación teórica

Duración estimada: 4–5 semanas Propósito: construir un marco teórico, técnico, ético y normativo que sustente el proyecto, comprendiendo en profundidad las tecnologías involucradas sin tomar decisiones de diseño ni selección definitiva.

Actividades:

Revisión sistemática de literatura y documentación técnica sobre:

Modelos open-vocabulary detection (OVD)

Técnicas de multi-object tracking (MOT)

Protocolos y arquitecturas de transmisión de medios en baja latencia

Enfoques ético-legales y de privacidad en visión por computadora

Normativa de seguridad laboral en la construcción

Elaboración de fichas de lectura, matrices comparativas y síntesis crítica.

Integración de los resultados en un informe académico estructurado.

Resultado esperado:

Informe “Fundamentación teórica y estado del arte”.

Criterios conceptuales para orientar las decisiones metodológicas de la Etapa 2.


#### 14.2.2. Etapa 2 - Análisis metodológico y estrategia de evaluación

Duración estimada: 5–6 semanas Propósito: definir los criterios experimentales, métricas, datasets y condiciones de prueba que permitirán evaluar la factibilidad del sistema en laboratorio y entorno simulado.

Actividades:

Determinar supuestos y restricciones técnicas (hardware, cámaras, entornos controlados).

Definir métricas de evaluación: precisión, recall, F1-score, FPS, latencia.

Explorar, seleccionar y documentar datasets de referencia y del dominio construcción.

Diseñar un protocolo de evaluación reproducible y escalable a futuro.

Elaborar matriz de riesgos técnicos y operativos con mitigaciones básicas.

Resultado esperado:

Documento “Plan metodológico y protocolo de evaluación”.

Inventario de datasets validados y criterios de evaluación.

Matriz de riesgos y supuestos experimentales.


#### 14.2.3. Etapa 3 - Diseño arquitectónico de la plataforma experimental

Duración estimada: 7–9 semanas Propósito: definir una arquitectura conceptual y modular, lo suficientemente clara para implementar un prototipo funcional, sin buscar una ingeniería de producto completa.

Actividades:

Diseño del plano de medios (captura, normalización, transporte de video).

Diseño del plano de control (detección, eventos, alertas, almacenamiento).

Definición de módulos principales.

Elaboración de diagramas de arquitectura y flujo de datos.

Definición preliminar de APIs internas y contratos de comunicación.

Planificación del backlog de desarrollo incremental (sprints o hitos).

Redacción del documento técnico de arquitectura.

Resultado esperado:

Documento “Diseño de arquitectura modular”.

Diagramas de flujo, componentes y contratos de interfaz.

Backlog inicial priorizado para la implementación.


#### 14.2.4. Etapa 4 - Implementación del prototipo experimental

Duración estimada: 10–12 semanas Propósito: construir el prototipo experimental que materializa la arquitectura definida, integrando los módulos esenciales en un flujo funcional de extremo a extremo.

Actividades:

Implementar el módulo de ingesta y transmisión de video de baja latencia, conforme al diseño del plano de medios.

Integrar un modelo OV pre entrenado capaz de procesar secuencias de video en tiempo real.

Incorporar, en la medida en que resulte viable, componentes complementarios como:

Módulo de seguimiento temporal (MOT),

Lógica básica de patrones de riesgo,

Sistema simplificado de alertas o registro de eventos,

Interfaz de prueba (API o panel web básico).

Documentar de manera continua las configuraciones, dependencias, decisiones técnicas y limitaciones observadas durante la implementación.

Realizar una validación técnica preliminar del flujo mínimo en entorno controlado, midiendo latencia, FPS y estabilidad general.

Resultado esperado:

Prototipo funcional reproducible con documentación técnica.

Video o demo funcional end-to-end.

Log de pruebas iniciales (latencia, FPS).

Registro de decisiones técnicas y limitaciones.


#### 14.2.5. Etapa 5 - Evaluación y validación de desempeño

Duración estimada: 4–5 semanas Propósito: medir cuantitativa y cualitativamente el desempeño del prototipo en laboratorio y en entorno simulado de obra civil.

Actividades:

Ejecución de pruebas en dataset controlado (laboratorio).

Ejecución en escenario representativo de obra simulada.

Registro de métricas: precisión, recall, F1, FPS, latencia.

Evaluación de robustez frente a condiciones reales (iluminación, oclusión, movimiento).

Análisis comparativo con resultados del estado del arte.

Elaborar el informe de resultados y análisis crítico.

Resultado esperado:

Informe “Evaluación de desempeño y validación experimental”.

Tablas de métricas y gráficos analíticos.

Discusión de fortalezas, debilidades y limitaciones del sistema.


#### 14.2.6. Etapa 6 - Documentación final, revisión y presentación

Duración estimada: 5–6 semanas Propósito: consolidar los resultados técnicos y académicos del proyecto, garantizando una entrega completa, reproducible y lista para defensa.

Actividades:

Redactar el Informe Final estructurado.

Incorporar anexos técnicos (APIs, diagramas, logs, parámetros).

Compilar manual de despliegue y documentación del repositorio.

Preparar presentación oral y material multimedia (slides, video demo).

Validar y etiquetar el repositorio final (versión definitiva).

Resultado esperado:

Entrega académica completa: informe PDF, anexos, repositorio y presentación.

Defensa lista ante tribunal con documentación de respaldo.


### 14.3. Cronograma y esquema gráfico

El cronograma del proyecto se organiza en torno a las seis etapas descritas. La secuencia general mantiene una progresión desde la investigación y fundamentación inicial hasta la validación experimental y el cierre documental. El esquema gráfico permite distinguir la duración estimada de cada etapa, su relación temporal con las demás y el estado de avance correspondiente.

Figura 1

Diagrama de Gantt de las etapas previstas del proyecto.


### 14.4. Costos asociados al proyecto

[Se completará más adelante.]


