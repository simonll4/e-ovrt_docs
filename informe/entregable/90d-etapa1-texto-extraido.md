# 90d — Texto extraído del documento de trabajo: §15 Estado del Arte y §16 Marco Teórico (v1.0)

> **Extracción derivada (2026-08-28)** del `.docx`
> `informe/entregable/desarrollando/E-OVRT-VDP_Secciones_15_y_16_Estado_del_Arte_y_Marco_Teorico_v1.0.docx`, **solo para búsqueda y cita**
> (mismo estatuto que el doc 90): al editar, se edita el `.docx`/Google Docs, nunca
> este archivo. Tablas y figuras pueden haber perdido formato; las figuras no se
> extraen y las ecuaciones no se convierten — quedan `⟦FIGURA: no extraída — ver el .docx⟧` y
> `⟦ECUACIÓN: no extraída — ver el .docx⟧` donde estaban. Regenerado con
> `herramientas/extraer_informe.py` (regla D-C del manual de aplicación).

---

## 15. Estado del arte

El estado del arte reúne los antecedentes técnicos y metodológicos necesarios para contextualizar el desarrollo de una plataforma experimental de detección open-vocabulary en video en tiempo real. Su propósito es revisar los enfoques, modelos y arquitecturas que permiten comprender el alcance actual de la detección visual guiada por lenguaje natural, así como sus limitaciones cuando se la traslada a escenarios dinámicos, con restricciones temporales y requerimientos de seguridad laboral.

### 15.1. Alcance del estado del arte y propósito de la fundamentación teórica

El análisis se organiza en torno a los dominios que condicionan la viabilidad del sistema: la detección open-vocabulary como alternativa frente a los enfoques de vocabulario cerrado, los modelos visión-lenguaje y sus principales familias arquitectónicas, el seguimiento multiobjeto como mecanismo de persistencia temporal, y las tecnologías de transmisión y procesamiento de vídeo necesarias para operar con baja latencia. De manera complementaria, se consideran las brechas que aparecen al aplicar estas tecnologías al dominio de la construcción civil, especialmente en relación con la detección de condiciones de riesgo, la estabilidad temporal de las predicciones, la sensibilidad a los prompts, la disponibilidad de datos y la evaluación de alertas en tiempo real.

Esta revisión no tiene por finalidad elegir de forma aislada un modelo, protocolo o herramienta, sino establecer un marco crítico para distinguir qué capacidades se encuentran suficientemente maduras, qué aspectos requieren validación experimental y qué limitaciones deben ser consideradas durante el diseño e implementación del prototipo. A partir de esta base se derivan criterios para la selección tecnológica, la definición del alcance experimental y la construcción posterior del protocolo de evaluación.

### 15.2. Detección open-vocabulary: modelos, paradigmas y brechas del estado del arte

#### 15.2.1. Paradigmas arquitectónicos y modelos representativos

El estado del arte en OVD no constituye una solución homogénea, sino que se organiza en familias arquitectónicas con compromisos claramente diferenciados entre expresividad semántica, complejidad computacional y eficiencia temporal. A partir de un relevamiento exhaustivo realizado durante la investigación bibliográfica, se identificaron cuatro paradigmas dominantes, de los cuales se presentan a continuación los aspectos y modelos representativos más relevantes para el contexto de sistemas de video en tiempo real.

El primer paradigma extiende arquitecturas end-to-end basadas en Transformers —derivadas de DETR y DINO (Carion et al., 2020; H. Zhang et al., 2022)— e incorpora el lenguaje dentro de la predicción mediante fusión multimodal. Grounding DINO (Liu et al., 2024) organiza esa integración en un Feature Enhancer que alinea representaciones visuales y textuales, una selección de consultas guiada por lenguaje y un decoder de modalidad cruzada que refina cajas y las vincula con fragmentos del prompt. La fusión profunda favorece expresiones referenciales y consultas con atributos, aunque incrementa el costo computacional y la complejidad de despliegue.

El segundo paradigma adapta detectores one-stage de la familia YOLO para puntuar regiones frente a representaciones textuales. YOLO-World (Cheng et al., 2024) incorpora interacción visión-lenguaje en su neck y permite reutilizar un vocabulario precomputado; YOLOE (A. Wang et al., 2025) amplía la reparametrización para admitir prompts textuales, visuales y un modo sin prompt. Esta familia prioriza eficiencia y compatibilidad con pipelines de baja latencia, a cambio de una expresividad más acotada ante consultas relacionales o altamente composicionales.

Una tercera familia deriva la detección del paradigma dual-encoder de CLIP: imagen y texto se proyectan en un espacio compartido y la clase de cada región se obtiene por compatibilidad semántica, no mediante logits fijos. OWL-ViT y OWLv2 (Minderer et al., 2022, 2023) representan este enfoque y muestran cómo el autoentrenamiento puede escalar la supervisión sin alterar el mecanismo de consulta. Su principal ventaja es la modularidad: el vocabulario cambia con los prompts; su costo depende del número de consultas y puede mitigarse mediante el cacheo de embeddings cuando el vocabulario permanece estable.

El cuarto paradigma agrupa modelos guiados por prompts generalistas, generativos e híbridos. Florence-2 (Xiao et al., 2024) formula las tareas como traducción secuencia-a-secuencia y genera representaciones textuales de cajas, etiquetas u otras salidas estructuradas; APE, LLMDet y T-Rex2 adoptan prompting generalista sin compartir necesariamente una decodificación autoregresiva (Shen et al., 2023; Fu et al., 2025; Jiang et al., 2024). Esta flexibilidad amplía la variedad de tareas y modalidades de consulta, pero en los modelos generativos introduce latencia variable y menor paralelismo que la predicción directa.

A continuación, se revisan modelos representativos de cada paradigma, enfocando el análisis en: (i) decisiones arquitectónicas, (ii) mecanismo de fusión/compatibilidad visión–lenguaje, (iii) régimen de entrenamiento y tipo de supervisión, y (iv) resultados en benchmarks estándar (COCO, LVIS), junto con consideraciones prácticas de inferencia relevantes para aplicaciones en vídeo.

**Convención de lectura.** Salvo indicación expresa, las cifras de COCO y LVIS corresponden a AP promediado entre umbrales de intersección sobre unión (IoU) de 0,50 a 0,95; en LVIS se conserva el protocolo Fixed AP cuando así lo informa la fuente. Los resultados de literatura supervisada de EPP se presentan como mAP@0,5 o AP@0,5 en una serie separada y no deben compararse numéricamente con COCO/LVIS AP.

##### 15.2.1.1. Bloque A — Detectores end-to-end tipo DETR/DINO con fusión visión–lenguaje en el decoder

###### 15.2.1.1.1. Grounding DINO

**Arquitectura base.** Grounding DINO extiende la formulación de detección como phrase grounding introducida por GLIP (L. H. Li et al., 2021) y la integra en la línea DETR/DINO. El modelo emplea una arquitectura dual-encoder/single-decoder: un backbone visual —frecuentemente Swin Transformer— extrae características multiescala y un backbone textual BERT codifica el prompt; un Transformer produce predicciones condicionadas por ambas modalidades (Liu et al., 2024).

**Mecanismo visión–lenguaje.** La contribución central es una fusión multimodal profunda basada en atención cruzada en distintas etapas. Grounding DINO divide la fusión en tres componentes: Feature Enhancer (interacciones imagen–texto para alinear semántica y regiones), Language-guided Query Selection (inicializa consultas del decoder condicionadas por texto), y Cross-modality Decoder (agrega atención cruzada con texto para refinar cajas y asociar predicciones a fragmentos del prompt). Esto hace que el modelo sea especialmente efectivo con expresiones referenciales o frases con atributos (Liu et al., 2024).

**Resultados reportados.** En configuración zero-shot, Grounding DINO con backbone Swin-L reporta 52,5 AP en COCO y 26,1 mean AP en ODinW; la variante Swin-T reporta aproximadamente 48,4 AP en COCO bajo el mismo protocolo (Liu et al., 2024).

La variante GroundingDINO-B con backbone Swin-B dispone de pesos públicos, pero su checkpoint declara COCO entre los datos de entrenamiento, junto con O365, GoldG, Cap4M, OpenImages, ODinW-35 y RefCOCO. Por ello, el 56,7 AP publicado en COCO no constituye una cifra zero-shot directamente comparable con la variante Swin-T entrenada sin COCO (IDEA-Research, 2024c).

**Evolución Grounding DINO 1.5.** La versión 1.5 Pro, orientada a máxima generalización, entrena con Grounding-20M (más de 20 millones de imágenes) y logra 54,3 AP en COCO y 55,7 AP en LVIS-minival en zero-shot transfer. La versión 1.5 Edge, orientada a despliegue eficiente, reporta 75,2 FPS y 36,2 AP en LVIS-minival con TensorRT, y despliegue en NVIDIA Orin NX con más de 10 FPS (Ren, Jiang, et al., 2024).

**Licencia y disponibilidad.** El repositorio del Grounding DINO original se distribuye bajo licencia Apache-2.0. Las variantes Grounding DINO 1.5 Pro y Grounding DINO 1.5 Edge se ofrecen mediante API y no publican pesos abiertos; la licencia Apache-2.0 corresponde al SDK de acceso y no al modelo (IDEA-Research, 2024c; Ren, Jiang, et al., 2024).

**Implementación MM-Grounding-DINO.** MM-Grounding-DINO proporciona una tubería unificada de grounding y detección sobre la familia Grounding DINO. Sus variantes Tiny reportan entre 50,4 y 50,6 AP@[0,50:0,95] en COCO zero-shot y entre 35,7 y 41,4 AP@[0,50:0,95] en LVIS-minival, según la configuración y el backbone evaluados (X. Zhao et al., 2024).

###### 15.2.1.1.2. DINO-X

**Arquitectura base.** DINO-X es un modelo unificado y object-centric para detección open-world/open-vocabulary, desarrollado como evolución directa de Grounding DINO 1.5, manteniendo un esquema Transformer encoder–decoder orientado a representaciones a nivel objeto. A diferencia de detectores OV que dependen estrictamente de listas de clases, DINO-X soporta múltiples tipos de prompt: texto, prompts visuales y prompts personalizados (Ren, Chen, et al., 2024).

**Mecanismo visión–lenguaje.** La idea distintiva de DINO-X es combinar flexibilidad de entrada con un mecanismo prompt-free mediante un Universal Object Prompt que permite "detectar cualquier cosa" sin definir clases específicas (Ren, Chen, et al., 2024).

**Entrenamiento.** El trabajo construye y utiliza Grounding-100M, un conjunto con más de 100 millones de muestras de grounding de alta calidad para preentrenamiento (Ren, Chen, et al., 2024).

**Resultados reportados.** DINO-X Pro alcanza 56,0 AP en COCO, 59,8 AP en LVIS-minival y 63,3 AP en clases raras de LVIS-minival, estableciendo un nuevo estado del arte en detección abierta (Ren, Chen, et al., 2024).

**Licencia.** DINO-X se ofrece mediante API y no publica pesos abiertos; la licencia Apache-2.0 corresponde al SDK o cliente de acceso y no a los pesos del modelo (IDEA-Research, 2024a; Ren, Chen, et al., 2024).

##### 15.2.1.2. Bloque B — Detectores one-stage tipo YOLO con puntuación región–texto

###### 15.2.1.2.1. YOLO-World

**Arquitectura base.** YOLO-World adapta un detector one-stage de la familia YOLO al escenario open-vocabulary manteniendo predicción densa y diseño orientado a despliegue. Su contribución arquitectónica central es RepVL-PAN (Re-parameterizable Vision-Language Path Aggregation Network), un neck multiescala que incorpora interacción visión–lenguaje sin abandonar la estructura backbone–PAN–head propia de YOLO (Cheng et al., 2024).

**Mecanismo visión–lenguaje.** El modelo puntúa regiones mediante similitud en un espacio compartido región–texto. RepVL-PAN implementa esta interacción con Text-guided CSPLayer para inyectar guía textual en las features visuales e Image Pooling Attention para enriquecer embeddings textuales con contexto visual. En despliegue, YOLO-World opera con vocabulario offline y habilita una reparametrización que permite prescindir del encoder textual durante inferencia (Cheng et al., 2024).

**Resultados reportados.** YOLO-World-L reporta 35,4 AP en LVIS-minival con 52,0 FPS en NVIDIA V100 (sin TensorRT), mostrando un punto de operación competitivo para aplicaciones con restricción de latencia (Cheng et al., 2024).

**Licencia.** El repositorio declara licencia GPL-3.0, con posibilidad de gestionar licencia alternativa para uso comercial (AILab-CVC, 2024).

###### 15.2.1.2.2. YOLOE

**Arquitectura base.** YOLOE, presentado como "Real-Time Seeing Anything", propone un modelo one-stage que unifica detección y segmentación manteniendo el esquema backbone–PAN–heads típico de YOLO. Sus módulos de alineamiento se diseñan para que, tras reparametrización, el grafo de inferencia quede equivalente al de un YOLO cerrado (A. Wang et al., 2025).

**Mecanismo visión–lenguaje.** YOLOE integra tres modalidades: prompts de texto mediante RepRTA (Re-parameterizable Region-Text Alignment), prompts visuales mediante SAVPE (Semantic-Activated Visual Prompt Encoder), y modo prompt-free mediante LRPC (Lazy Region-Prompt Contrast) que reformula la asignación como retrieval evitando dependencia de modelos de lenguaje en inferencia (A. Wang et al., 2025).

**Resultados reportados.** En LVIS-minival zero-shot, YOLOE-v8-S reporta 27,9 AP con 305,8 FPS (NVIDIA T4, TensorRT) y YOLOE-v8-L alcanza 35,9 AP con 102,5 FPS, superando a YOLO-Worldv2-S por +3,5 AP con mayor velocidad (A. Wang et al., 2025).

Las cifras anteriores corresponden a las variantes YOLOE-v8 evaluadas en el trabajo original, que también publica variantes construidas sobre YOLO11 (YOLOE-11) con resultados equivalentes (Wang et al., 2025). Las variantes sobre YOLO26 (YOLOE-26) son una extensión posterior de Ultralytics, sin evaluación en el trabajo original; por lo tanto, los resultados publicados para YOLOE-v8 no deben utilizarse como si fueran una medición de YOLOE-26 (Ultralytics, 2026).

**Licencia.** El repositorio declara licencia AGPL-3.0, lo que introduce requisitos copyleft que pueden condicionar adopción en integraciones propietarias (THU-MIG, 2025).

##### 15.2.1.3. Bloque C — Detectores basados en dual-encoders (CLIP-like) y matching por similitud

###### 15.2.1.3.1. OWL-ViT y OWLv2

**Arquitectura base.** OWL-ViT propone una receta directa para llevar modelos visión–lenguaje a detección open-vocabulary usando un Vision Transformer (ViT) encoder-only con modificaciones mínimas. Se mantienen los tokens espaciales y se agregan cabezales livianos que predicen, por token, una caja y un embedding de compatibilidad. La clasificación abierta se logra reemplazando un clasificador cerrado por embeddings derivados del texto (Minderer et al., 2022).

**Entrenamiento.** OWLv2 escala mediante self-training (OWL-ST): usa un modelo OWL-ViT como annotator para generar pseudo-cajas sobre datos web a gran escala (WebLI). OWLv2 introduce mejoras de eficiencia de entrenamiento: un objectness head para entrenar pérdidas solo sobre un subconjunto de tokens más plausibles como objeto, y token dropping durante entrenamiento (Minderer et al., 2023).

**Resultados reportados.** OWL-ViT L/14 alcanza 34,6 AP y 31,2 AP en clases raras en LVIS. OWLv2 L/14 con OWL-ST reporta 44,6 AP en clases raras zero-shot en LVIS-val, y la variante G/14 alcanza 47,2 AP en clases raras (Minderer et al., 2022, 2023).

**Licencia.** Los pesos se distribuyen bajo Apache-2.0 (Google, 2022; Google, 2023).

##### 15.2.1.4. Bloque D — Modelos guiados por prompts generalistas: generativos e híbridos

Esta familia reúne modelos que amplían el tipo de consulta o la variedad de tareas sin compartir necesariamente un mecanismo generativo en inferencia. Florence-2 constituye el caso propiamente secuencia-a-secuencia: interpreta instrucciones de tarea y genera una representación textual de cajas, etiquetas u otras salidas estructuradas, con la flexibilidad y el costo temporal propios de la decodificación autoregresiva (Xiao et al., 2024). APE, en cambio, utiliza prompting generalista pero produce predicciones estructuradas de forma directa; LLMDet incorpora conocimiento de un LLM durante el entrenamiento y descarta ese componente en inferencia; T-Rex2 combina prompts textuales y visuales mediante una formulación multimodal (Shen et al., 2023; Fu et al., 2025; Jiang et al., 2024). En conjunto, estos trabajos muestran que el prompting generalista constituye una dimensión transversal y no equivale, por sí mismo, a generación autoregresiva.

###### 15.2.1.4.1. Florence-2

**Arquitectura, entrenamiento y disponibilidad.** Florence-2 utiliza un encoder visual DaViT y un Transformer encoder-decoder multimodal bajo una formulación secuencia-a-secuencia: recibe una imagen y una instrucción de tarea, y genera texto o tokens de localización que representan cajas, regiones y otras salidas estructuradas. El modelo se preentrenó sobre FLD-5B, un banco de 126 millones de imágenes con 5,4 mil millones de anotaciones, y la variante large reporta 37,5 mAP en detección zero-shot sobre COCO. Esta unificación evita cabezales específicos por tarea, pero la generación autoregresiva introduce un costo temporal distinto del de los detectores de predicción directa. Los pesos publicados por Microsoft se distribuyen bajo licencia MIT (Xiao et al., 2024; Microsoft, 2024).

#### 15.2.2. Composición de modelos y pipelines de percepción

Los detectores OVD pueden integrarse en pipelines que combinan capacidades complementarias. Grounded SAM ejemplifica esta composición al encadenar detección condicionada por texto con segmentación universal, mientras que OVTrack formaliza una extensión temporal mediante tracking-by-detection en vocabulario abierto (Ren, Liu, et al., 2024; S. Li et al., 2023). El aporte conceptual de estos enfoques no es un modelo aislado, sino la posibilidad de desacoplar etapas con responsabilidades distintas.

La modularidad permite sustituir componentes y ampliar capacidades, pero también acumula latencia, dependencias de integración y fuentes de variabilidad. Para sistemas de video en tiempo real, la evaluación debe considerar el pipeline completo y no sólo la precisión de cada modelo por separado; este criterio enlaza la detección con el seguimiento temporal y con las etapas posteriores de generación de eventos.

#### 15.2.3. Síntesis comparativa y trade-offs para tiempo real

La Tabla 2 sintetiza las características fundamentales de los cuatro paradigmas arquitectónicos analizados, con énfasis en las dimensiones más relevantes para la viabilidad del sistema E-OVRT-VDP en un contexto de vídeo en tiempo real.

**Tabla 2**

*Síntesis comparativa de paradigmas arquitectónicos OVD según dimensiones relevantes para sistemas de video en tiempo real*

| **Paradigma** | **Modelo(s) representativos** | **Mecanismo visión-lenguaje** | **Fortaleza principal** | **Limitación para tiempo real** |
| --- | --- | --- | --- | --- |
| DETR/DINO + fusión profunda | Grounding DINO, MM-Grounding-DINO, DINO-X | Fusión multimodal en decoder mediante atención cruzada visión-lenguaje | Alta precisión semántica; manejo de expresiones referenciales complejas | Costo computacional elevado; requiere optimización explícita para tiempo real |
| One-stage YOLO + puntuación región-texto | YOLO-World, YOLOE | Alineamiento región-texto reparametrizable; reducción progresiva del overhead de fusión mediante reparametrización | Alta velocidad de inferencia; compatible con hardware de borde | Menor expresividad semántica frente a consultas complejas o con atributos compuestos |
| Dual-encoder CLIP-like + matching por similitud | OWL-ViT, OWLv2 | Matching por similitud en espacio de embeddings compartido; reutilización directa de preentrenamiento contrastivo | Modularidad; cambio de vocabulario sin modificar el modelo | latencia variable según tamaño del vocabulario; requiere caching para vocabularios estables; requiere cómputo de embeddings por consulta |
| Prompts generalistas: generativo e híbrido | Florence-2, APE, LLMDet, T-Rex2 | Mecanismos heterogéneos: generación autoregresiva en Florence-2; predicción directa o integración híbrida en APE, LLMDet y T-Rex2 | Flexibilidad multitarea; soporte para prompts complejos y multimodales | Florence-2: latencia de inferencia variable e inestabilidad temporal por decodificación autoregresiva; APE: costo de prompting masivo escalable pero sin garantías de tiempo real estricto |

*Nota.* La columna “Limitación para tiempo real” describe el principal factor restrictivo de cada paradigma en escenarios de monitoreo continuo. Los modelos listados son representativos de cada familia; no constituyen una lista exhaustiva. Las métricas de velocidad son contextuales al hardware y configuración de inferencia reportados en la literatura primaria. Fuente: Elaboración propia basada en las fuentes mencionadas (Cheng et al., 2024; Liu et al., 2024; Minderer et al., 2022, 2023; A. Wang et al., 2025; Xiao et al., 2024).

El régimen de disponibilidad constituye una dimensión independiente del rendimiento. YOLO-World y YOLOE se publican bajo GPL-3.0 y AGPL-3.0, respectivamente, mientras que el Grounding DINO original y OWLv2 utilizan licencias permisivas Apache-2.0; por otra parte, Grounding DINO 1.5 y DINO-X se ofrecen mediante API sin pesos abiertos. Estas diferencias afectan la reproducción independiente, la redistribución de artefactos y la continuidad tecnológica, aun en un prototipo académico. Por ello, la comparación de alternativas debe distinguir entre licencia del código, licencia de los pesos y condiciones del servicio de acceso (AILab-CVC, 2024; Google, 2022, 2023; IDEA-Research, 2024a, 2024c; THU-MIG, 2025).

Como complemento a esta síntesis por paradigmas, en la Tabla A.1 del Anexo A se incluye una matriz ampliada orientada a prototipado, donde se comparan modelos representativos según familia arquitectónica, mecanismo visión-lenguaje, métricas reportadas, rendimiento y licenciamiento. Dicha matriz conserva el detalle técnico necesario para respaldar la selección posterior de alternativas, sin sobrecargar el cuerpo principal del estado del arte.

Del análisis comparativo emergen tres tensiones técnicas que deben considerarse como criterios de selección. La primera es la tensión entre precisión semántica y latencia de inferencia: los modelos con fusión visión-lenguaje más profunda suelen ofrecer mayor capacidad frente a consultas complejas, pero con un costo computacional que puede reducir la tasa de procesamiento. La segunda es la tensión entre generalización zero-shot y especialización de dominio: los benchmarks generales no representan por sí mismos las condiciones visuales de una obra civil. Esta tensión se extiende al fine-tuning. La evidencia revisada no permite atribuir la retención open-vocabulary a una familia arquitectónica por sí sola, porque las comparaciones utilizan datos, módulos entrenables y protocolos diferentes. La retención depende de la receta aplicada: qué parámetros se ajustan o congelan, si se conserva supervisión lingüística amplia y si se evalúan categorías no vistas (Cheng et al., 2024; Minderer et al., 2023; X. Zhao et al., 2024). Por ello, debe describirse para cada configuración y no inferirse de la profundidad o removibilidad de la fusión. La tercera es la tensión entre expresividad semántica y simplicidad del prompt: las consultas más precisas exigen mayor control de formulación, introduciendo una variable de diseño ausente en sistemas closed-set.

Una observación transversal es que, en los modelos que permiten reutilizar la representación textual, el cacheo de embeddings entre cuadros reduce el costo recurrente cuando el vocabulario permanece estable (A. Wang et al., 2025; T. Zhao et al., 2024). Dado que las condiciones de riesgo se definen al inicio de la sesión y se mantienen constantes, esta estrategia resulta directamente aplicable al escenario considerado.

Adicionalmente, la tendencia hacia pipelines composicionales descrita en esta sección introduce una cuarta tensión que opera en un plano distinto a las anteriores: la tensión entre modularidad e integrabilidad. Los enfoques que ensamblan múltiples modelos foundation —como la combinación de un detector OVD con un segmentador universal— ofrecen mayor flexibilidad para sustituir componentes y abordar tareas compuestas, pero acumulan latencia de inferencia por la ejecución secuencial de etapas y aumentan la complejidad de integración entre formatos de entrada y salida. Esta tensión no invalida el patrón composicional, pero señala que la evaluación de alternativas en etapas posteriores deberá considerar no solo el rendimiento de cada modelo de forma aislada, sino el costo total del pipeline resultante bajo las restricciones temporales del escenario de aplicación.

##### 15.2.3.1. Análisis de rendimiento para tiempo real

Desde el punto de vista del desempeño temporal, varios de los modelos analizados presentan características compatibles con aplicaciones de análisis de vídeo en tiempo real. La Tabla 3 resume puntos de operación publicados para modelos representativos y calcula, a partir de sus FPS, una latencia teórica por cuadro; estos valores no constituyen mediciones homogéneas de latencia.

**Tabla 3**

*Análisis comparativo de rendimiento de modelos OVD para tiempo real*

| **Modelo** | **Hardware** | **Framework** | **FPS** | **Latencia derivada (ms/cuadro)** | **LVIS-minival AP@[0,50:0,95]** |
| --- | --- | --- | --- | --- | --- |
| YOLOE-v8-S | T4 | TensorRT | 305,8 | 3,3 ms | 27,9 |
| YOLOE-v8-L | T4 | TensorRT | 102,5 | 9,8 ms | 35,9 |
| G-DINO 1.5 Edge | A100 | TensorRT | 75,2 | 13,3 ms | 36,2 |
| YOLO-World-L | V100 | PyTorch | 52,0 | 19,2 ms | 35,4 |

*Nota.* La columna «Latencia derivada» se calculó como 1000/FPS y expresa milisegundos por cuadro inferidos de la tasa publicada; no corresponde a una medición independiente de latencia. Los valores de FPS y AP provienen de trabajos originales con hardware, resolución, batch size y runtime no homogéneos. Por ello, la tabla muestra puntos de operación indicativos, no benchmarks normalizados ni latencia extremo a extremo. Fuente: elaboración propia basada en A. Wang et al. (2025), Ren, Jiang, et al. (2024) y Cheng et al. (2024).

Los puntos de operación de la tabla describen rendimiento publicado sobre benchmarks generales y no constituyen una predicción del desempeño sobre condiciones de EPP en construcción. La brecha entre benchmark general y condición de dominio se desarrolla en la sección 15.2.5.4.

#### 15.2.4. Adaptabilidad mediante fine-tuning y preservación de capacidad open-vocabulary

El ajuste de un modelo preentrenado introduce un compromiso entre especialización de dominio y preservación de las representaciones adquiridas. La literatura muestra que actualizar todos los parámetros puede mejorar el desempeño in-domain y, al mismo tiempo, deteriorar la generalización fuera de distribución frente a estrategias que congelan la mayor parte del modelo; este fenómeno se vincula con el olvido catastrófico (catastrophic forgetting) y exige medir la retención de forma explícita (Kirkpatrick et al., 2017; Kumar et al., 2022). Cuando la evidencia del dominio es limitada, la cantidad y ubicación de los parámetros actualizados también importan: el ajuste selectivo de capas puede preservar mejor información preentrenada que el ajuste completo (Lee et al., 2023).

En Grounding DINO se documentan fine-tuning closed-set, preentrenamiento continuado open-set y ajuste open-vocabulary; MM-Grounding-DINO muestra que la retención depende de mantener supervisión y evaluación sobre categorías no vistas (X. Zhao et al., 2024). La adaptación con LoRA constituye una variante de actualización acotada en la que se conservan congelados los backbones y se entrenan adaptadores de bajo rango (Rasaee et al., 2025). Como referencia de especialización, Grounding DINO con Swin-L reporta 62,6 AP en COCO val y 63,0 AP en test-dev tras fine-tuning closed-set, frente a 52,5 AP en su evaluación zero-shot; los regímenes no son equivalentes y no deben confundirse (Liu et al., 2024).

Para YOLO-World, la documentación distingue el ajuste con MixedGroundingDataset, que conserva textos y tareas de grounding, del ajuste closed-set con MultiModalDataset y vocabulario fijo. La variante reparametrizada elimina RepVL-PAN y el encoder textual, con lo cual prioriza eficiencia a costa de cerrar el vocabulario. El ajuste del encoder textual puede degradar la generalización, mientras que congelarlo o conservar supervisión abierta reduce ese riesgo (AILab-CVC, 2024; Cheng et al., 2024).

YOLOE ofrece linear probing y full tuning para transferencia a un dominio. La receta estándar produce un modelo de vocabulario fijo después del ajuste; los autores no reportan una métrica de retención open-vocabulary para ese camino. Evaluarla exige reinyectar vocabulario abierto y aplicar un protocolo explícito, de modo que especialización in-domain y capacidad abierta permanezcan como dimensiones separadas (A. Wang et al., 2025).

En los dual-encoders, el ajuste de extremo a extremo sobre datasets cerrados requiere estrategias de regularización para evitar el colapso del espacio de embeddings compartido del que depende la capacidad abierta (Minderer et al., 2022). OWLv2 aporta además la receta OWL-ST de autoentrenamiento con pseudoanotaciones; el uso de un vocabulario diverso derivado de n-gramas preserva mejor la generalización que un espacio de etiquetas estrecho (Minderer et al., 2023). En Florence-2, el ajuste mediante LoRA modifica una fracción acotada de parámetros, aunque la retención de clases base se informa como parcial y dependiente de la configuración (Ucar et al., 2025; Xiao et al., 2024).

En síntesis, no existe una jerarquía universal de familias frente al fine-tuning. La comparación defendible se realiza por receta concreta, distinguiendo parámetros actualizados, datos de adaptación y evaluación posterior de generalización. La Tabla 4 resume las estrategias documentadas y sus condiciones de retención.

**Tabla 4**

*Estrategias de fine-tuning documentadas y retención OVD reportada por familia arquitectónica*

| **Familia / Modelo** | **Estrategia de fine-tuning** | **Retención OVD reportada** | **Condición clave** |
| --- | --- | --- | --- |
| Grounding DINO | Fine-tuning closed-set | No | Vocabulario restringido post-ajuste |
| Grounding DINO | Preentrenamiento continuado open-set | Sí | LR reducido; módulos congelados; datos mixtos |
| Grounding DINO | Fine-tuning open-vocabulary (base a novel) | Sí | Evaluación explícita en categorías no vistas |
| Grounding DINO | Adaptación LoRA | Sí | Backbones congelados; solo adapters entrenables |
| YOLO-World | Fine-tuning con MixedGroundingDataset | Parcial | Depende de capas ajustadas; text encoder frágil |
| YOLO-World | Fine-tuning closed-set (MultiModalDataset) | No | Vocabulario fijo en JSON |
| YOLO-World | Reparametrización eficiente (sin RepVL-PAN) | No | Text encoder removido; equivale a YOLOv8 |
| YOLOE | Transferring (linear probing / full tuning) | No evaluada por los autores | La receta estándar produce vocabulario fijo; la retención requiere reinyectar y evaluar vocabulario abierto |
| OWL-ViT / OWLv2 | Fine-tuning de extremo a extremo con regularización | Parcial | Requiere estrategias de regularización |
| OWL-ViT / OWLv2 | Self-training (OWL-ST) con pseudo-anotaciones | Sí | Vocabulario diverso (n-gramas) preserva OVD |
| Florence-2 | Fine-tuning con LoRA | Parcial | Retención parcial de clases base; encoder congelado recomendado |

*Nota.* “Retención OVD reportada” resume el comportamiento informado para la receta y el protocolo indicados; no constituye una propiedad universal de la familia arquitectónica. “Parcial” indica una retención dependiente de la configuración específica —capas congeladas, tasa de aprendizaje, datos de entrenamiento y evaluación sobre categorías no vistas—. Fuente: elaboración propia basada en AILab-CVC (2024), Cheng et al. (2024), Liu et al. (2024), Minderer et al. (2022, 2023), Rasaee et al. (2025), Ucar et al. (2025), A. Wang et al. (2025), Xiao et al. (2024) y X. Zhao et al. (2024).

La evidencia sintetizada en la Tabla 4 permite identificar tres factores recurrentes: qué parámetros se ajustan o congelan, la amplitud y diversidad del vocabulario utilizado durante el entrenamiento, y la existencia de una evaluación explícita sobre categorías no vistas. Estos factores interactúan con la arquitectura, pero los trabajos revisados no aíslan sus efectos mediante un protocolo común. Por ello, no corresponde afirmar que una familia tolere mejor el ajuste completo; corresponde describir qué receta retuvo capacidad OVD, bajo qué datos y con qué protocolo de evaluación.

#### 15.2.5. Brechas identificadas en el dominio de la construcción civil

A partir de la revisión y síntesis de los enfoques presentados, se pone de manifiesto un conjunto de limitaciones estructurales que no quedan plenamente resueltas por los modelos actuales de detección *open-vocabulary*. Estas brechas delinean líneas de trabajo relevantes para etapas posteriores del proyecto y permiten anticipar desafíos técnicos que deberán abordarse durante el diseño arquitectónico y la implementación del prototipo.

##### 15.2.5.1. Contextualización semántica limitada

La mayoría de los detectores OVD actuales resuelven la detección como una combinación de localización espacial y compatibilidad textual evaluada de manera independiente para cada región candidata (Zareian et al., 2021; Liu et al., 2024). Este enfoque, aunque efectivo para identificar objetos individuales, no garantiza consistencia contextual entre múltiples entidades detectadas ni permite razonar sobre relaciones espaciales o semánticas entre ellas.

En entornos industriales y de construcción, muchos conceptos relevantes para la seguridad son inherentemente composicionales y dependen del contexto espacial. Condiciones como "persona sin casco cerca de excavación", "operario en zona de tránsito vehicular" o "escalera bloqueando salida de emergencia" requieren no solo detectar cada elemento de manera aislada, sino también evaluar sus relaciones geométricas y semánticas. Esta limitación impide dar por resueltas las condiciones relacionales a partir de la salida local del detector y exige que cualquier tratamiento adicional se defina y valide de forma explícita.

##### 15.2.5.2. Ausencia de consistencia temporal nativa

Los modelos de detección open-vocabulary operan predominantemente sobre imágenes estáticas, procesando cada cuadro de manera independiente sin mantener memoria de estados previos ni modelar explícitamente la evolución temporal de las detecciones. Esta característica introduce variabilidad entre cuadros consecutivos que puede manifestarse como fluctuaciones en los puntajes de confianza, apariciones y desapariciones espurias de detecciones, e inconsistencias en la asignación de etiquetas entre cuadros consecutivos.

En aplicaciones de vídeo, particularmente aquellas orientadas a monitoreo continuo, esta variabilidad temporal resulta problemática. Los enfoques generativos, como Florence-2, tienden a exhibir mayor inestabilidad debido a la naturaleza autoregresiva de su decodificación (Xiao et al., 2024). La literatura reciente sugiere que la integración con módulos de seguimiento multi-objeto (MOT) constituye una estrategia efectiva para mitigar este problema, permitiendo que el tracker aporte coherencia temporal a las detecciones semánticamente ricas del OVD (S. Li et al., 2023). No obstante, esta integración introduce complejidad arquitectónica adicional y requiere considerar la compatibilidad entre el detector y el método de seguimiento seleccionado.

##### 15.2.5.3. Sensibilidad a la formulación del prompt

La flexibilidad semántica que caracteriza a la detección open-vocabulary introduce una dependencia significativa respecto de la formulación exacta de las consultas textuales. Investigaciones en modelos visión-lenguaje han demostrado que pequeños cambios en la redacción de las consultas pueden producir diferencias significativas en el desempeño, incluso cuando diferentes formulaciones refieren al mismo concepto subyacente (Zhou et al., 2022b). Esta sensibilidad tiene implicancias directas para la usabilidad del sistema: usuarios con diferentes niveles de experiencia o distintas convenciones lingüísticas pueden obtener resultados heterogéneos ante objetivos de detección equivalentes.

Esta observación motivó el desarrollo de técnicas de prompt learning, donde los tokens de contexto se reemplazan por vectores aprendibles que se optimizan con datos etiquetados del dominio objetivo (Zhou et al., 2022b; Khattak et al., 2023). Sin embargo, las estrategias desarrolladas para clasificación de imágenes no se transfieren directamente al contexto de detección. Se demostró que la optimización automática de representaciones de prompts —específicamente diseñada para tareas de detección— supera consistentemente a los prompts elaborados mediante ingeniería manual, evidenciando la necesidad de enfoques especializados para el dominio OVD (Du et al., 2022). Adicionalmente, algunos modelos recientes abordan parcialmente esta limitación mediante el soporte de prompts visuales que permiten anclar la detección a ejemplos concretos en lugar de depender exclusivamente de descripciones textuales (Jiang et al., 2024).

##### 15.2.5.4. Sensibilidad al dominio de aplicación

Los benchmarks estándar utilizados para evaluar modelos OVD —como MS COCO con 80 categorías de objetos cotidianos (Lin et al., 2014) o LVIS con más de 1200 categorías de distribución long-tail (Gupta et al., 2019)— no representan plenamente las condiciones visuales y semánticas de entornos industriales especializados. En el contexto específico de obras de construcción, factores como iluminación extrema, oclusiones frecuentes por maquinaria y estructuras, indumentaria especializada de protección, y presencia de equipamiento industrial introducen distribuciones visuales que difieren significativamente de los datos de preentrenamiento.

Los resultados publicados en benchmarks generales no predicen por sí mismos el desempeño sobre una condición de dominio específica. Grounding DINO con backbone Swin-L pasa de 52,5 AP en COCO a 26,1 mean AP sobre los 35 conjuntos de ODinW. En consecuencia, la transferencia al dominio de construcción debe verificarse mediante una línea base zero-shot propia y un conjunto de prueba congelado, sin asumir equivalencia entre COCO o LVIS y la condición objetivo (Liu et al., 2024).

Como referencia supervisada in-domain, YOLOR alcanzó un mAP@0,5 de 0,883 sobre SHEL5K y un AP@0,5 de 0,907 para la clase head; YOLOv5x alcanzó un mAP@0,5 de 0,866 sobre CHV; y YOLOv9-e reportó un mAP@0,5 aproximado de 0,71 sobre SH17, con valores entre 0,58 y 0,69 para las variantes de YOLOv8 (Otgonbold et al., 2022; Wang et al., 2021; Ahmad & Rahimi, 2025).

Estas cifras corresponden a detectores entrenados sobre taxonomías específicas de EPP y no constituyen una comparación directa con los resultados de COCO o LVIS. En particular, el AP@0,5 de 0,907 para la clase *head* muestra que un detector supervisado puede alcanzar un desempeño alto sobre esa categoría en SHEL5K. La cifra no permite inferir una dificultad intrínseca universal, pero sí establece una referencia in-domain para analizar el costo de formular la condición sin entrenamiento específico.

La evidencia ubicada específicamente en el cruce entre vocabulario abierto y EPP es todavía limitada. Choi y Greer (2024) evaluaron OWLv2 zero-shot sobre 5.210 imágenes: obtuvieron AP@IoU>0,5 de 0,6767 para *person* y 0,6493 para detección directa de *hardhat*. Al introducir asociación jerárquica, la clase *head* —cabeza sin casco— alcanzó 0,1024 AP y la cascada multietapa obtuvo 0,2699 AP para detección de casco. Estas cifras no equivalen a una métrica de condición o alerta, pero muestran que la asociación persona–cabeza–EPP agrega dificultad respecto de detectar los componentes por separado.

Como evidencia adyacente, Chen y Zou (2025) evaluaron modelos visión-lenguaje generativos en una tarea de visual grounding y observaron IoU total inferior al 20 % para objetivos con restricciones de atributo, como trabajadores con casco blanco. El resultado no constituye un benchmark de detectores OVD, pero respalda la dificultad de localizar condiciones visuales finamente especificadas mediante lenguaje natural.

El relevamiento de publicaciones entre 2023 y 2026 no identificó evaluaciones de Grounding DINO o YOLO-World zero-shot sobre SHEL5K o CHV, ni un benchmark multi-fuente de EPP bajo protocolo COCO. Esta ausencia constituye una brecha del estado del arte: los benchmarks generales no resuelven la evaluación de una condición de dominio expresada mediante lenguaje natural, por lo que se requiere una línea base zero-shot propia y un conjunto de prueba congelado. La respuesta experimental a esta brecha corresponde a las secciones posteriores.

##### 15.2.5.5. Protocolos de evaluación específicos para seguridad industrial

Las métricas de evaluación predominantes en la literatura OVD —como Average Precision (AP) en COCO o LVIS— constituyen indicadores generales de rendimiento que no capturan adecuadamente el valor operativo de un sistema de detección en el contexto de seguridad industrial (Gupta et al., 2019). Estas métricas evalúan la precisión de localización y clasificación cuadro a cuadro, sin considerar aspectos temporales ni el impacto diferenciado de distintos tipos de error en escenarios de monitoreo de riesgos.

Para validar la plataforma en su dominio de aplicación, resulta necesario diseñar métricas y protocolos de evaluación alineados con los objetivos de seguridad en construcción. Esto incluye considerar la tasa de eventos de riesgo detectados correctamente a lo largo de secuencias de video, el tiempo transcurrido entre el inicio de una condición de riesgo y su detección (latencia de alerta), la tasa de falsas alarmas por unidad de tiempo de monitoreo, y la persistencia mínima requerida para considerar válida una detección.

##### 15.2.5.6. Tabla comparativa de brechas identificadas

La Tabla 5 organiza las brechas identificadas en las subsecciones precedentes con su descripción técnica y su implicación específica para el proyecto.

**Tabla 5**

*Brechas identificadas en la aplicación de modelos OVD al dominio de seguridad en construcción civil*

| **Brecha identificada** | **Descripción** | **Implicación para el proyecto** |
| --- | --- | --- |
| Contextualización semántica limitada | Los modelos OVD detectan entidades localmente pero no infieren relaciones espaciales complejas entre ellas (p. ej., “persona dentro de zona restringida” requiere razonamiento relacional) | Las condiciones composicionales no pueden evaluarse a partir de la salida local del detector sin una estrategia adicional explícitamente definida y validada. |
| Ausencia de consistencia temporal nativa | La detección cuadro a cuadro introduce variabilidad en puntajes de confianza, apariciones y desapariciones espurias entre cuadros consecutivos | Necesidad de integración con módulo MOT para aportar coherencia temporal a las detecciones semánticas (S. Li et al., 2023) |
| Sensibilidad a la formulación del prompt | Pequeños cambios en la redacción producen diferencias significativas en el desempeño, incluso para conceptos equivalentes (Zhou et al., 2022b) | El diseño de prompts para condiciones de riesgo requiere un proceso sistemático; la selección informal puede comprometer la robustez del sistema |
| Brecha de dominio con benchmarks estándar | Los resultados en COCO o LVIS no garantizan transferencia al dominio objetivo. Grounding DINO con backbone Swin-L pasa de 52,5 AP en COCO a 26,1 mean AP en ODinW. | El protocolo debe incorporar una línea base zero-shot propia y un conjunto de prueba de dominio congelado; los benchmarks generales funcionan únicamente como referencia externa. |
| Ausencia de protocolos de evaluación específicos para seguridad industrial | Las métricas AP en COCO/LVIS (Gupta et al., 2019; Lin et al., 2014) no capturan el valor operativo del sistema: no consideran latencia de alerta, persistencia de la detección ni impacto diferenciado de falsos positivos/negativos. | El protocolo experimental debe definir métricas alineadas con el valor operativo de la alerta, incluyendo persistencia temporal, latencia y tratamiento diferenciado de falsos positivos y falsos negativos. |
| Escasez de evaluación OVD × EPP | La literatura ofrece evidencia directa limitada. Choi y Greer (2024) reportan AP@IoU>0,5 de 0,6767 para *person*, 0,6493 para detección directa de *hardhat*, 0,1024 para la clase *head* y 0,2699 para la cascada multietapa. El relevamiento no identificó evaluaciones de Grounding DINO o YOLO-World zero-shot sobre SHEL5K o CHV, ni un benchmark de EPP multi-fuente bajo protocolo COCO. | Se requiere una línea base zero-shot propia y un conjunto de prueba congelado; la respuesta experimental se presenta fuera del estado del arte. |

*Nota.* Las brechas listadas delimitan problemas técnicos que el protocolo y la arquitectura deben abordar; no se presentan como limitaciones insalvables. Fuente: elaboración propia basada en Choi y Greer (2024), Chen y Zou (2025), Gupta et al. (2019), S. Li et al. (2023), Lin et al. (2014), Liu et al. (2024), Zareian et al. (2021) y Zhou et al. (2022b).

#### 15.2.6. Síntesis de la sección y avance al seguimiento multi-objeto

El análisis de los paradigmas OVD evidencia que la viabilidad de su integración en sistemas de monitoreo continuo está condicionada por cuatro factores: balance entre expresividad semántica y eficiencia de inferencia, diseño sistemático de prompts para el dominio específico, mecanismos de compensación de la variabilidad temporal cuadro a cuadro, y evaluación empírica en condiciones visuales de construcción civil. Los dos últimos factores remiten directamente al problema de persistencia temporal: dado que la OVD produce observaciones instantáneas sin identidad ni continuidad, la sección siguiente analiza los métodos de seguimiento multiobjeto como mecanismo para sostener esas detecciones a lo largo del tiempo.

En las secciones posteriores se distinguirá entre calibración operativa y adaptación paramétrica. La primera comprende cambios de resolución de entrada, formulación del vocabulario, umbrales, postproceso y estabilización temporal sin modificar los pesos del modelo; la segunda refiere exclusivamente al ajuste de parámetros mediante fine-tuning u otras técnicas de entrenamiento. Con esta distinción se evita presentar configuraciones de plataforma como si fueran modelos reentrenados.

### 15.3. Seguimiento multiobjeto: métodos, métricas y brechas del estado del arte

El seguimiento multiobjeto (MOT) constituye el mecanismo que transforma las detecciones instantáneas producidas por el sistema OVD en trayectorias persistentes a lo largo del tiempo, habilitando la agregación temporal de evidencias necesaria para la generación de alertas operativas. En esta sección se analizan los métodos representativos del estado del arte en MOT para sistemas de video en tiempo real, las métricas de evaluación relevantes para el contexto del proyecto y las brechas identificadas en la intersección entre MOT y detección open-vocabulary.

#### 15.3.1. Métodos representativos

El estado del arte en MOT para sistemas de video en tiempo real está dominado por la familia SORT extendida, cuya evolución refleja el progreso en el manejo de oclusiones, la explotación de detecciones de baja confianza y la eliminación de dependencias de entrenamiento específico por dominio.

##### 15.3.1.1. SORT

SORT (Simple Online and Realtime Tracking) establece el esquema de referencia del paradigma tracking-by-detection moderno. Combina el filtro de Kalman para el modelado del movimiento con el algoritmo Húngaro para la asignación óptima de detecciones a trayectorias, utilizando IoU como única métrica de similitud. Su diseño minimalista prescinde de cualquier modelado de apariencia, lo que resulta en latencia muy baja —capacidad de operar a tasas superiores a 200 FPS— y ausencia total de dependencias de entrenamiento. La principal limitación de SORT es su baja robustez ante oclusiones: cuando un objeto no es detectado durante varios cuadros consecutivos, la trayectoria se termina y la re-asociación posterior puede producir un cambio de identificador (ID switch), fragmentando la trayectoria en múltiples segmentos (Bewley et al., 2016).

##### 15.3.1.2. Contraste con variantes posteriores

Las extensiones de tracking-by-detection introducen distintos mecanismos para mejorar la continuidad: DeepSORT agrega apariencia mediante ReID (Wojke et al., 2017); ByteTrack reutiliza detecciones de baja confianza para sostener trayectorias (Y. Zhang et al., 2022); y OC-SORT corrige la estimación de movimiento durante oclusiones sin requerir apariencia (Cao et al., 2023). En el extremo de mayor complejidad, BoT-SORT combina movimiento y ReID, mientras que TrackFormer y MOTR aprenden detección y asociación de manera conjunta. Estas variantes permiten contrastar robustez, dependencia de entrenamiento y costo computacional, pero no establecen por sí mismas un método preferente para una plataforma OVD modular; la síntesis comparativa se conserva en la Tabla 6.

#### 15.3.2. Síntesis comparativa de métodos MOT

La Tabla 6 sintetiza las características principales de los métodos MOT analizados, con énfasis en las dimensiones más relevantes para su integración en el sistema E-OVRT-VDP: paradigma, modelo de movimiento, estrategia de asociación, robustez ante oclusiones, latencia y dependencias de entrenamiento.

**Tabla 6**

*Síntesis comparativa de métodos MOT representativos según dimensiones relevantes para sistemas de video en tiempo real con detección open-vocabulary*

| **Método** | **Paradigma** | **Modelo de movimiento** | **Asociación de datos** | **Robustez a oclusiones** | **Latencia / FPS** | **Dependencia de entrenamiento** |
| --- | --- | --- | --- | --- | --- | --- |
| SORT | Tracking-by-detection | Kalman lineal | IoU + Húngaro | Baja | Muy alta (>200 FPS) | Ninguna |
| DeepSORT | Tracking-by-detection | Kalman lineal | Cascada: movimiento + apariencia | Media-Alta | Media | Modelo ReID preentrenado |
| ByteTrack | Tracking-by-detection | Kalman lineal | Jerárquica: alta/baja confianza + IoU | Alta | Muy alta (>170 FPS) | Ninguna |
| OC-SORT | Tracking-by-detection | Kalman + correcciones OC | IoU + consistencia de momento (OCM) | Media-Alta | Muy alta | Ninguna |
| BoT-SORT | Tracking-by-detection | Kalman mejorado + CMC | Fusión IoU-ReID | Alta | Media | Modelo ReID preentrenado |
| TrackFormer / MOTR | End-to-end (Transformer) | Atención temporal aprendida | Mecanismo de atención global | Muy alta | Baja | Entrenamiento conjunto requerido |

*Nota.* CMC = Compensación de Movimiento de Cámara (Camera Motion Compensation). OC = Observation-Centric. La columna 'Dependencia de entrenamiento' refiere a componentes adicionales al detector base que requieren entrenamiento supervisado. FPS estimados corresponden a las configuraciones reportadas en los trabajos originales sobre hardware de referencia; pueden variar significativamente según el hardware y la resolución de entrada. Fuente: Elaboración propia basada en las fuentes citadas (Adžemović, 2025; Aharon et al., 2022; Bewley et al., 2016; Cao et al., 2023; Wojke et al., 2017; Y. Zhang et al., 2022).

##### 15.3.2.1. Observaciones críticas sobre la comparativa

La literatura comparativa muestra que los métodos de seguimiento difieren no sólo en sus resultados agregados, sino también en las dependencias que introducen. Los enfoques geométricos sin modelos de apariencia pueden acoplarse a detectores externos sin requerir entrenamiento adicional de ReID, mientras que las variantes basadas en apariencia o entrenamiento conjunto dependen de datos y componentes específicos (Adžemović, 2025; Wojke et al., 2017). Esta diferencia delimita un compromiso entre simplicidad de integración y robustez de asociación; por sí sola, no determina la elección de un tracker para una plataforma OVD.

#### 15.3.3. Métricas de evaluación para MOT

MOTA resume falsos negativos, falsos positivos y cambios de identidad respecto del ground truth, aunque su lectura está fuertemente condicionada por los errores de detección (Bernardin & Stiefelhagen, 2008). IDF1 enfatiza la consistencia de identidad a lo largo de la secuencia (Ristani et al., 2016), mientras que HOTA separa y combina calidad de detección, asociación y localización (Luiten et al., 2021). Estas métricas caracterizan al tracker, pero no miden el valor temporal de una alerta; la evaluación de un sistema asistivo exige niveles adicionales, cuya definición corresponde al protocolo experimental. Una comparación ampliada de estas métricas y de sus limitaciones se presenta en la Tabla A.2 del Anexo A.

#### 15.3.4. Brechas identificadas y desafíos para el prototipo

El análisis del estado del arte en MOT revela un conjunto de brechas que condicionan el diseño del prototipo y las decisiones metodológicas de la consolidación metodológica posterior. La Tabla 7 organiza estas brechas con su descripción técnica y su implicación específica para el proyecto.

**Tabla 7**

*Brechas identificadas en la aplicación de métodos MOT al contexto de seguridad en construcción civil en combinación con detección open-vocabulary*

| **Brecha identificada** | **Descripción** | **Implicación para el proyecto** |
| --- | --- | --- |
| Dependencia de la calidad del detector subyacente | El rendimiento del MOT está fuertemente acoplado al desempeño del detector. Errores de detección —FP, FN, bounding boxes inestables— se propagan al seguimiento, produciendo fragmentación de trayectorias, pérdidas de identidad y asociaciones erróneas (S. Li et al., 2025) | En el pipeline OVD + MOT, la variabilidad inherente de la detección open-vocabulary puede amplificar errores de asociación; el diseño del sistema debe contemplar estrategias de filtrado y umbralización que reduzcan el ruido de entrada al tracker |
| Fragilidad ante oclusiones prolongadas | Aunque los métodos modernos manejan oclusiones breves, las oclusiones de larga duración producen terminación prematura de trayectorias, re-asociaciones inciertas y aumento de ID switches (Du et al., 2024) | En entornos de obra civil con alta densidad de obstrucciones (andamios, maquinaria, materiales), la robustez ante oclusiones es una restricción de diseño relevante que debe evaluarse empíricamente |
| Métricas estándar no alineadas con objetivos operativos de seguridad | Las métricas MOTA, IDF1 y HOTA evalúan el desempeño del seguimiento cuadro a cuadro sin considerar el impacto operativo diferenciado de distintos tipos de error en el contexto de seguridad laboral (Luiten et al., 2021) | Se deben definir criterios de evaluación del componente MOT alineados con el dominio: persistencia mínima para disparar alertas, penalización diferenciada de ID switches en condiciones de riesgo, y tolerancia ante falsos positivos por oclusión |
| Ausencia de datasets de construcción con anotaciones de seguimiento | Los benchmarks estándar de MOT (MOT17, MOT20, DanceTrack) no contemplan el dominio de obras civiles; la evaluación del tracker en condiciones representativas requiere datos del dominio específico (Dendorfer et al., 2020; Milan et al., 2016) | La validación del componente MOT en el prototipo no puede apoyarse en benchmarks estándar; se requiere la definición de un protocolo de evaluación propio con datos recopilados en el contexto del proyecto |

*Nota.* Las brechas listadas definen el espacio de problemas abiertos que deben abordarse en el diseño experimental (etapa 2) y en la implementación del prototipo (etapa 4). Fuente: Elaboración propia basada en las fuentes citadas (Adžemović, 2025; Dendorfer et al., 2020; Du et al., 2024; S. Li et al., 2025; Luiten et al., 2021; Milan et al., 2016).

La brecha de ausencia de datasets de construcción con anotaciones de seguimiento merece una consideración adicional. Los benchmarks estándar de MOT —MOT17, MOT20, DanceTrack— fueron diseñados para escenarios de peatones en entornos urbanos y eventos de danza respectivamente, con distribuciones visuales que difieren significativamente de una obra civil: densidad de cámara fija en planos elevados, entidades heterogéneas (personas, maquinaria, materiales), indumentaria de protección que puede confundir a los modelos de apariencia, y configuraciones de oclusión determinadas por la geometría de la obra. Esta brecha no puede resolverse mediante adaptación de los benchmarks existentes; requiere la definición de un protocolo de evaluación propio que se apoyará en los datos recopilados durante la fase experimental del proyecto.

### 15.4. Video en tiempo real y streaming: protocolos, servidores y brechas del estado del arte

#### 15.4.1. Protocolos de transmisión de video de baja latencia

Los protocolos de transmisión de vídeo constituyen un componente relevante dentro del análisis de sistemas de vídeo en tiempo real, debido a que condicionan la forma en que los flujos provenientes de cámaras o fuentes de vídeo son transportados hacia los módulos de procesamiento, visualización o almacenamiento. En el contexto del presente proyecto, su estudio resulta necesario porque la detección open-vocabulary no opera sobre imágenes aisladas, sino sobre secuencias continuas que deben ser recibidas, decodificadas y procesadas con una latencia compatible con la generación oportuna de alertas.

Desde una perspectiva general, los protocolos de streaming pueden diferenciarse por dimensiones como el modelo de entrega, el esquema de distribución, la tolerancia a pérdidas, los mecanismos de buffering y el orden de magnitud de latencia que suelen alcanzar bajo determinadas condiciones de red y configuración. Sin embargo, estos valores no deben interpretarse como propiedades absolutas de cada protocolo, ya que la latencia final depende del pipeline completo: captura, codificación, transporte, decodificación, inferencia, evaluación de patrones y comunicación de resultados. Estos componentes serán retomados con mayor detalle en el marco teórico y en la descripción técnica del sistema, donde se analizará su impacto dentro de la arquitectura experimental.

En esta sección, el análisis se limita a revisar los protocolos y familias de transmisión más relevantes para aplicaciones de baja latencia, identificando sus características principales, sus restricciones prácticas y su grado de compatibilidad con un sistema de análisis automatizado de vídeo. Esta revisión permite establecer criterios preliminares para la selección posterior del stack de medios, sin definir todavía una implementación definitiva.

##### 15.4.1.1. Criterios de clasificación de protocolos

**Modelo de entrega push.** En el modelo push, una vez establecida la sesión, el emisor entrega el flujo de manera continua hacia el receptor (típicamente sobre UDP o sobre una sesión persistente), minimizando esperas asociadas a la solicitud de unidades discretas de contenido. Protocolos de tiempo real, como RTP y flujos interactivos como WebRTC, se alinean más naturalmente con push (ISO/IEC, 2022; May, 2017).

**Modelo de entrega pull.** En el modelo pull, el control de la entrega reside principalmente en el cliente: el receptor solicita (por HTTP) segmentos o partes de segmentos en forma sucesiva, habilitando escalabilidad y cacheo, pero introduciendo buffering y latencias asociadas a segmentación y recarga. Los esquemas adaptativos sobre HTTP, como HLS y MPEG-DASH, responden al patrón pull (cliente-driven).

**Esquema de distribución unicast.** En unicast, cada cliente mantiene una conexión individual y recibe un flujo dedicado, lo que simplifica control por receptor (adaptación, seguridad, métricas), pero escala el consumo de ancho de banda en el emisor.

**Esquema de distribución multicast.** En multicast, el emisor envía un único flujo a un grupo multicast y la red replica hacia múltiples receptores, siendo eficiente en redes administradas. Protocolos basados en RTP pueden operar sobre unicast o multicast; sin embargo, el multicast IP no es viable en Internet abierta (en general no es ruteable extremo-a-extremo y complica control de congestión por receptor).

**Orden de magnitud de latencia.** Otra forma práctica de categorizar protocolos es por la latencia extremo a extremo típica que habilitan bajo configuraciones habituales. En términos operativos pueden distinguirse tres rangos:

**Alta latencia (>~3 s).** Protocolos orientados a distribución masiva y robustez. Aquí se ubican implementaciones “clásicas” de HLS y MPEG-DASH con segmentos de varios segundos. Al apoyarse en HTTP/HTTPS y CDN, priorizan escalabilidad y tolerancia a fallos, usualmente con latencias del orden de varios segundos a decenas de segundos (ISO/IEC, 2022; May, 2017).

**Latencia media (~0,5 a 3 s).** Incluye protocolos como RTMP (en ingesta), RTSP cuando se opera con buffers conservadores o sobre TCP, y variantes de baja latencia de HLS/DASH basadas en segmentación fina y entrega parcial.

**Baja latencia (<~500 ms).** Protocolos diseñados para interactividad estricta y respuesta casi en tiempo real: WebRTC, SRT, RIST y flujos RTP con mínima capa de sesión. En general emplean UDP para evitar la penalidad de retransmisiones fuera de plazo y operan con buffers pequeños, compensando la pérdida con estrategias específicas (p. ej., ARQ “dentro de un presupuesto de tiempo” en SRT/ RIST). En WebRTC, además, la conectividad extremo-a-extremo depende de mecanismos de traversal NAT como ICE, que influyen en la latencia efectiva según el tipo de red (Keranen et al., 2018; Nakagawa et al., 2021; Schulzrinne et al., 2003; Sharabayko et al., 2024; Video Services Forum, 2020).

##### 15.4.1.2. Mapa de familias de protocolos según los criterios de clasificación

En esta sección, se analizan los protocolos más relevantes aplicando sistemáticamente (i) modelo de entrega, (ii) esquema de distribución y (iii) latencia típica, además de consideraciones prácticas pertinentes a cada protocolo (NAT, resiliencia, seguridad, tooling).

RTSP/RTP: el estándar de cámaras IP industriales. El Real-Time Streaming Protocol (RTSP) es un protocolo de capa de aplicación orientado al control de sesiones de streaming. Fue especificado inicialmente en el RFC 2326 (Schulzrinne et al., 1998) y posteriormente revisado en RTSP 2.0 mediante el RFC 7826 (Schulzrinne et al., 2016). RTSP opera como plano de control: el cliente describe la sesión, negocia parámetros y ejecuta acciones de control, mientras que el audio y el video suelen transportarse mediante un protocolo de medios separado.

En este esquema, el transporte de medios suele realizarse con Real-time Transport Protocol (RTP), definido en el RFC 3550, acompañado por RTCP para informar pérdida y jitter (Schulzrinne et al., 2003). RTP se encapsula típicamente sobre UDP e incorpora timestamps y números de secuencia para facilitar la reconstrucción temporal y el manejo del jitter. RTSP/RTP se adoptó ampliamente en videovigilancia y cámaras IP por su madurez y compatibilidad; ONVIF Profile S lo utiliza como mecanismo central de consumo y control de streams (ONVIF, 2019). En redes controladas puede utilizar UDP para el transporte, mientras que RTP/RTCP interleaved sobre la conexión TCP de RTSP simplifica el cruce de firewalls a costa de los compromisos propios de TCP (Schulzrinne et al., 1998, 2016).

En cuanto a latencia, los valores reportados para un protocolo son rangos típicos y no compromisos del estándar. La latencia extremo a extremo depende de captura, codificación, red, decodificación y, de manera marcada, del buffer del receptor. Axis Communications AB (2015) identifica el play-out buffer como un componente que puede dominar el retardo cuando se prioriza estabilidad frente a jitter. Bajo condiciones favorables, RTSP/RTP puede operar en el orden de cientos de milisegundos —aproximadamente 200–800 ms—; configuraciones de videovigilancia con buffering conservador pueden elevar ese valor a 1.000–2.000 ms o más (Axis Communications AB, 2015).

#### 15.4.2. Alternativas complementarias de ingesta, transporte y distribución

Además de RTSP/RTP, la literatura de transmisión de baja latencia comprende familias con compromisos diferentes. Los esquemas HTTP adaptativos —HLS y MPEG-DASH, incluidas sus extensiones de baja latencia— priorizan escalabilidad y robustez mediante segmentación; WebRTC integra negociación, transporte y control de congestión para interacción sub-segundo; y SRT/RIST agregan recuperación selectiva de pérdidas sobre UDP para enlaces variables. Estas alternativas no son directamente equivalentes: la latencia observada depende del códec, los buffers, la red y la implementación, por lo que su comparación debe interpretarse como un mapa de propiedades y no como un ranking universal. La Tabla 8 resume estas diferencias.

La captura mediante SDK constituye una alternativa distinta del consumo de un stream ya codificado. En cámaras inteligentes, el host puede gobernar un pipeline ejecutado en el dispositivo y recibir las unidades visuales o salidas requeridas para el procesamiento posterior. Esta modalidad permite desplazar operaciones acotadas de adquisición o preprocesamiento hacia la fuente sin equipararla a inferencia OVD en el borde (Luxonis, s. f.-b).

Los servidores de medios implementan combinaciones de retransmisión, pasarela, reempaquetamiento o transcodificación. Su aporte a la latencia depende de si transforman el contenido o sólo lo reenvían: la transcodificación incorpora decodificación y recodificación, mientras que un relay agrega principalmente un salto de red y gestión de colas. Para un pipeline de analítica visual, esta distinción resulta más relevante que un catálogo extenso de productos, porque permite separar el costo del transporte del costo de transformación multimedia (Ahmad et al., 2005; Amirante et al., 2014, 2015).

En la salida del pipeline, los patrones publicador-suscriptor permiten desacoplar la generación de eventos de sus consumidores. MQTT formaliza distintos niveles de calidad de servicio; QoS 1 garantiza entrega al menos una vez mediante confirmación PUBACK, por lo que una aplicación debe tolerar posibles reentregas y controlar idempotencia cuando un mismo evento no deba producir efectos duplicados (OASIS, 2019). Esta propiedad permite distinguir la generación interna de una alerta de su distribución posterior.

#### 15.4.3. Brechas del estado del arte en el streaming/OVD

Las tecnologías y arquitecturas actuales de streaming presentan un conjunto de limitaciones que condicionan directamente el diseño del pipeline experimental.

##### 15.4.3.1. Ausencia de benchmarks extremo a extremo integrados para pipelines OVD

La literatura revisada evidencia una fragmentación sistemática en la evaluación de desempeño: los benchmarks de inferencia de modelos OVD (p. ej., AP en COCO/LVIS, FPS en GPU aislada) operan de forma independiente respecto de los benchmarks de streaming (latencia de transporte, throughput de protocolo) y de las métricas de plataformas de edge computing (TOPS, FPS bajo carga térmica). Para una plataforma como E-OVRT-VDP el criterio de selección debe basarse en mediciones reproducibles del pipeline completo, y no extrapolarse directamente de métricas parciales o aisladas.

Esta brecha implica que no existen referentes directos en la literatura que permitan predecir con confianza el desempeño de un sistema que combina ingesta de video, inferencia OVD y emisión de eventos bajo restricciones de latencia propias de operación en tiempo real. En consecuencia, la validación empírica del pipeline completo constituye una contribución necesaria del proyecto, y la definición de protocolos de medición reproducibles deberá abordarse como parte del diseño experimental en la etapa 2.

##### 15.4.3.2. Integración de modelos OVD dentro de pipelines de streaming optimizados

Los frameworks de streaming más maduros para video analytics en tiempo real, como NVIDIA DeepStream, han sido históricamente diseñados y optimizados para detectores de clases fijas con arquitecturas convolucionales estándar, cuyos patrones de integración asumen una entrada de imagen y un conjunto predefinido de clases de salida (NVIDIA, 2024). Si bien el ecosistema ha comenzado a incorporar soporte para modelos open-vocabulary —por ejemplo, NVIDIA TAO Toolkit incluye flujos de exportación y despliegue para Grounding DINO (NVIDIA, s. f.-g)—, la integración de estos modelos en pipelines de streaming presenta desafíos técnicos que no se resuelven con la misma inmediatez que los detectores convencionales.

En particular, la conversión de modelos OVD a formatos optimizados como TensorRT puede requerir adaptaciones no triviales cuando la arquitectura incluye operadores no soportados nativamente o componentes dinámicos asociados a la codificación de prompts textuales. Dado que TensorRT no admite entradas de tipo texto, la etapa de tokenización debe separarse del grafo del modelo y gestionarse externamente (NVIDIA, s. f.-g), lo que introduce complejidad adicional en el diseño del pipeline. Más ampliamente, la arquitectura multi-modal que caracteriza a los modelos OVD —con un encoder visual y un encoder textual que interactúan mediante mecanismos de fusión— no se alinea directamente con los patrones de integración nativos de los plugins de inferencia estándar de estos frameworks, aunque rutas alternativas como la integración con Triton Inference Server ofrecen mayor flexibilidad al soportar modelos en múltiples formatos y frameworks (NVIDIA, s. f.-h). Esta brecha, si bien se está reduciendo, sugiere que la integración de modelos OVD dentro del pipeline de streaming requerirá capas de adaptación específicas cuya complejidad y costo deberán evaluarse empíricamente.

##### 15.4.3.3. Interoperabilidad efectiva entre protocolos heterogéneos

Aun cuando la literatura describe los roles del servidor de medios y las funciones de pasarela, reempaquetamiento y transcodificación (§15.4.2), no ofrece evidencia consolidada sobre el overhead real introducido por las conversiones entre protocolos —por ejemplo, de RTSP a WebRTC o de RTMP a SRT— en condiciones de operación representativas. La transcodificación, el reempaquetamiento entre contenedores de medios —como MPEG-TS, FLV o fMP4— y la adaptación entre pilas de transporte pueden agregar latencia y puntos de fallo que no quedan reflejados en las especificaciones de cada protocolo por separado.

Esta brecha resulta relevante en el contexto de E-OVRT-VDP, dado que en entornos reales de obra el parque de cámaras puede exponer flujos mediante protocolos diversos. Si bien el prototipo experimental operará previsiblemente con un conjunto acotado de fuentes y protocolos, la identificación de este vacío en la literatura permite anticipar un factor de complejidad para escenarios de despliegue más amplios y orienta el diseño hacia soluciones que no introduzcan dependencias rígidas con un único protocolo de ingesta.

##### 15.4.3.4. Métricas de evaluación alineadas con objetivos de seguridad laboral

Las métricas estándar de evaluación de sistemas de streaming, tales como latencia media, throughput, tasa de pérdida de paquetes y calidad visual (PSNR/SSIM), no capturan adecuadamente el valor operativo de un sistema orientado a la detección asistiva de riesgos en obra. De manera análoga a lo identificado en la sección de OVD respecto de las métricas de detección, las métricas de streaming convencionales no consideran aspectos como el tiempo transcurrido entre el inicio de una condición de riesgo y la notificación al operador, la continuidad de detección bajo variaciones de calidad del stream, o el impacto diferenciado de artefactos de compresión sobre la detectabilidad de elementos de protección personal.

#### 15.4.4. Síntesis comparativa de protocolos

La Tabla 8 sintetiza las características principales de los protocolos analizados, con énfasis en las dimensiones de mayor relevancia para el diseño del sistema E-OVRT-VDP.

**Tabla 8**

*Comparativa de protocolos de transmisión de video de baja latencia para sistemas de video analítico en tiempo real*

| **Protocolo** | **Latencia típica extremo a extremo** | **Transporte base** | **Modelo de entrega** | **Resiliencia a pérdida** | **Cifrado nativo** | **Caso de uso principal** |
| --- | --- | --- | --- | --- | --- | --- |
| RTSP/RTP | ~200–800 ms | UDP (o TCP) | RTSP controla la sesión; RTP transporta el flujo | Media (con RTCP) | Opcional (RTSPS) | Cámaras IP industriales, CCTV, entornos LAN controlados |
| RTMP | ~2–5 s | TCP | Push | Alta (TCP garantiza entrega) | Sí (RTMPS/TLS) | Ingesta a plataformas de streaming; encoders hacia servidores |
| HLS / MPEG-DASH | ~5–45 s (LL: ~2–10 s) | HTTP/TCP | Pull (segmentado) | Alta (CDN + HTTP) | Sí (HTTPS) | Distribución masiva de contenido; viewers simultáneos elevados |
| WebRTC | < 500 ms | UDP (SRTP sobre DTLS) | Push/Pull (P2P o SFU) | Media (con NACK/FEC) | Sí (DTLS-SRTP, obligatorio) | Interactividad ultra-baja latencia; videoconferencia; monitoreo P2P |
| SRT | ~120–500 ms (configurable) | UDP + ARQ selectivo | Push o Pull | Alta (ARQ con presupuesto de tiempo) | Sí (AES-128/256) | Contribución broadcast; enlaces WAN no confiables; 4G/5G |
| RIST | ~120–500 ms | RTP + ARQ (RTCP FB) | Push o Pull (multicast posible) | Alta (ARQ + FEC) | Sí (DTLS) | Broadcast profesional; distribución multicast en redes gestionadas |

*Nota.* Los rangos de latencia extremo a extremo reportados son valores típicos dependientes de configuración, no compromisos de los estándares. La latencia final está determinada por el pipeline completo (captura, codificación, transporte, decodificación, inferencia), no únicamente por el protocolo. HLS/DASH LL = Low-Latency HLS / DASH. DTLS-SRTP = combinación de Datagram TLS y Secure RTP (cifrado obligatorio en WebRTC). ARQ = Automatic Repeat reQuest. FEC = Forward Error Correction. SFU = Selective Forwarding Unit. NACK = Negative Acknowledgement. Fuente: Elaboración propia basada en Axis Communications AB (2015), DASH Industry Forum (2020), ISO/IEC (2022), Keranen et al. (2018), May (2017), Pantos (2025), Parmar y Thornburgh (2012), Roy (2024), Schulzrinne et al. (1998, 2003, 2016), Sharabayko et al. (2024), Sonono (2019), Video Services Forum (2020, 2024) y World Wide Web Consortium (2025).

La tabla muestra que no existe un protocolo que maximice simultáneamente latencia mínima, alta resiliencia a pérdidas y escalabilidad, lo cual es coherente con el enfoque de diseño de cada estándar, orientado a prioridades diferentes según el contexto de aplicación. En arquitecturas comúnmente adoptadas, esta situación suele abordarse mediante esquemas híbridos que emplean protocolos distintos por tramo del flujo de video: uno para ingesta y transporte desde el origen hacia un servidor o plataforma de medios (en entornos LAN o WAN con distintos niveles de control), y otro para distribución/visualización hacia clientes finales, donde los requerimientos de interactividad, número de usuarios y compatibilidad con navegadores influyen de manera determinante. De forma complementaria, también es habitual que los protocolos HTTP adaptativos (HLS/DASH) se reserven para consumo masivo, reproducción diferida o escenarios donde la prioridad sea la escalabilidad y la tolerancia a variaciones de red, más que la inmediatez. En consecuencia, la evidencia comparativa respalda que la selección de protocolos debe abordarse como una decisión dependiente del escenario y de la infraestructura, y suele validarse mediante pruebas empíricas sobre el pipeline completo (captura, codificación, transporte, decodificación e integración con analítica), antes de su adopción en un sistema específico.

## 16. Marco teórico

El marco teórico concentra los conceptos, categorías normativas y fundamentos técnicos que sostienen el diseño posterior del prototipo. A diferencia del Estado del arte, no funciona como un inventario exhaustivo de modelos o herramientas, sino como base conceptual para justificar qué se detecta, cómo se interpreta, bajo qué restricciones opera el sistema y qué condiciones ético-legales delimitan su uso.

### 16.1. Organización interna del marco teórico

El marco teórico se organiza a partir de los dominios conceptuales que sustentan el diseño y la evaluación de la plataforma experimental. Cada dominio responde a una pregunta central del proyecto y permite delimitar, desde una perspectiva técnica o normativa, las condiciones bajo las cuales resulta posible construir un sistema de detección open-vocabulary aplicado al monitoreo de seguridad en construcción civil.

En primer lugar, se aborda el dominio de aplicación, vinculado con la seguridad laboral en obras y con la identificación de condiciones de riesgo observables mediante análisis visual. Luego se desarrollan los fundamentos de la detección open-vocabulary, el seguimiento multiobjeto, la transmisión de video en tiempo real y las restricciones ético-legales asociadas al uso de sistemas de visión por computadora en contextos laborales. Esta organización permite que las decisiones posteriores de diseño, implementación y evaluación no aparezcan como elecciones aisladas, sino como consecuencia de un conjunto articulado de criterios técnicos, metodológicos y normativos.

La Tabla 9 resume la relación entre cada dominio del marco teórico, la pregunta que orienta su desarrollo y su contribución dentro del proyecto.

**Tabla 9**

*Correspondencia entre dominios del marco teórico, preguntas articuladoras y contribución al proyecto*

| **Dominio del marco teórico** | **Pregunta articuladora** | **Contribución al proyecto** |
| --- | --- | --- |
| Seguridad laboral y condiciones de riesgo observables | ¿Qué condiciones debe poder identificar el sistema? | Define el dominio de aplicación y traduce obligaciones preventivas en evidencias visuales detectables. |
| Detección open-vocabulary y modelos visión-lenguaje | ¿Cómo puede el sistema interpretar descripciones abiertas en lenguaje natural? | Fundamenta el uso de modelos capaces de detectar conceptos no restringidos a un vocabulario cerrado. |
| Seguimiento multiobjeto | ¿Cómo se mantiene la continuidad temporal de las detecciones? | Justifica la incorporación de mecanismos de seguimiento para reducir inestabilidad entre cuadros consecutivos y evaluar persistencia. |
| Video en tiempo real, streaming y latencia | ¿Qué restricciones impone el procesamiento continuo de video? | Delimita los componentes del pipeline, las fuentes de latencia y los criterios para operar en tiempo real. |
| Marco ético-legal y privacidad | ¿Bajo qué condiciones es legítimo aplicar visión computacional en entornos laborales? | Establece límites de uso responsable, minimización de datos, carácter asistivo y ausencia de identificación personal. |
| Convergencias y preguntas rectoras | ¿Qué brechas atraviesan los dominios y qué debe definir el protocolo experimental? | Integra restricciones, explicita límites y formula las preguntas que guían la consolidación metodológica. |

*Nota.* Cada dominio se corresponde con una sección de este capítulo; la columna «Contribución al proyecto» indica qué aporta al desarrollo posterior, no un resultado alcanzado. Fuente: elaboración propia.

El punto de partida del análisis es el dominio de aplicación. Antes de evaluar qué puede detectar el sistema, es necesario precisar qué debe detectar y por qué, definiendo así qué condiciones de riesgo son relevantes en una obra de construcción, qué las hace observables visualmente y qué obligación normativa impone su prevención. Sin esa delimitación, cualquier evaluación del desempeño técnico del sistema carecería de criterio de referencia.

### 16.2. Condiciones de riesgo observables

La viabilidad técnica de un sistema de detección visual depende, en primer lugar, de una definición precisa de su objeto: qué condiciones deben ser detectadas, bajo qué criterio se las considera riesgosas y por qué son observables mediante visión por computadora. En el contexto de la construcción civil, esa definición no es arbitraria. Emerge de un marco normativo consolidado que establece, con carácter obligatorio, cuáles son las obligaciones del empleador en materia de prevención y qué condiciones físicas en la obra constituyen incumplimiento de esas obligaciones. Las siguientes secciones sistematizan ese marco y lo traducen al plano de los observables visuales que el sistema deberá identificar.

El sector de la construcción combina tareas simultáneas, entornos cambiantes y una elevada interacción entre personas, maquinaria y estructuras temporales. En este contexto, la regulación en materia de seguridad y salud en el trabajo cumple un rol ordenatorio: define obligaciones mínimas y mecanismos de control que orientan la prevención, y establece un lenguaje común para evaluar condiciones de riesgo.

Para un proyecto que analiza video en obra y emite alertas asistivas, la normativa no debe interpretarse como una lista de verificación aislada, sino como el fundamento que permite traducir riesgos típicos (por ejemplo, trabajo en altura sin protección colectiva o sin anclaje, presencia de personas en zonas de exclusión de equipos móviles o izajes, o interacción peatón-vehículo fuera de circuitos señalizados) en criterios observables y verificables. Esta sección desarrolla el marco normativo argentino aplicable y propone una articulación conceptual entre las obligaciones legales y las evidencias susceptibles de detección automatizada.

#### 16.2.1. La normativa como fuente de condiciones de riesgo

La seguridad laboral en la industria de la construcción civil se organiza a partir de un conjunto de instrumentos normativos que prescriben obligaciones concretas para empleadores, trabajadores y empresas. Una distinción metodológica relevante separa la normativa de cumplimiento obligatorio —leyes, decretos reglamentarios y resoluciones técnicas con fuerza vinculante— de los estándares voluntarios de gestión, que no generan exigibilidad legal por sí mismos, pero aportan marcos conceptuales útiles para organizar la prevención de manera sistemática. Ambos tipos de instrumentos resultan pertinentes para este análisis, siendo la normativa obligatoria la que define qué condiciones deben cumplirse y en consecuencia qué incumplimientos constituyen riesgo, y los estándares de gestión, en cambio, ofrecen un marco para comprender cómo se monitorea y verifica ese cumplimiento en la práctica operativa.

##### 16.2.1.1. Normativa de cumplimiento obligatorio

En Argentina, el sistema normativo de higiene y seguridad laboral se estructura jerárquicamente a partir de la Ley 19.587, reglamentada con carácter general por el Decreto 351/79 y con especificidad sectorial por el Decreto 911/96 para la industria de la construcción. Este cuerpo normativo se complementa con resoluciones técnicas emitidas por la Superintendencia de Riesgos del Trabajo, que operacionalizan los mecanismos de control y coordinación preventiva.

##### 16.2.1.2. Ley 19.587 y el principio de prevención

La Ley 19.587 de Higiene y Seguridad en el Trabajo establece el marco general aplicable a todo el territorio nacional y fija como eje conceptual el principio de prevención: las condiciones laborales deben ajustarse a normas técnicas destinadas a prevenir daños a la salud y a la integridad de las personas (Ley 19.587, 1972). Su alcance no se limita a un sector específico, sino que delimita obligaciones generales vinculadas al ambiente de trabajo, las instalaciones, los procesos productivos y la organización preventiva.

La contribución conceptual de esta ley para el presente análisis reside en instalar el deber de anticipación como componente central de la gestión de seguridad. La prevención no se concibe como respuesta reactiva a incidentes, sino como identificación y control sistemático de condiciones que preceden al daño. En una obra civil, por ejemplo, donde el riesgo se reconfigura constantemente con el avance de los trabajos, este principio implica que el sistema de monitoreo debe orientarse a detectar condiciones de riesgo antes de que se materialicen en accidentes, y no únicamente a registrar eventos ya ocurridos.

##### 16.2.1.3. Decreto 351/79: reglamentación general

El Decreto 351/79 aprueba la reglamentación de la Ley 19.587 y desarrolla un conjunto de exigencias técnicas que permiten trasladar el deber general de prevención a requisitos operativos verificables (Decreto 351/79, 1979). Organiza aspectos como condiciones edilicias, instalaciones, señalización, iluminación, ventilación, protecciones de máquinas, orden y limpieza, y la estructuración de servicios especializados en higiene y seguridad.

El aporte conceptual de este decreto para el análisis es la noción de condición controlable, ya que muchos riesgos se expresan como estados observables del entorno —ausencia de resguardos, obstrucciones en vías de circulación, falta de señalización, desorden en zonas de trabajo—, lo que habilita estrategias de verificación sistemática basadas en la observación del espacio físico. El decreto consolida la idea de que la seguridad puede monitorearse a partir de indicadores verificables en el lugar de trabajo, idea que resulta directamente relevante para un sistema de monitoreo visual.

##### 16.2.1.4. Decreto 911/96: reglamento específico de construcción

El Decreto 911/96 aprueba el Reglamento de Higiene y Seguridad específico para la industria de la construcción, atendiendo a particularidades que distinguen a este sector de otros entornos laborales, definiendo cuestiones del contexto de la obra como establecimiento temporal con geometría cambiante, la coexistencia simultánea de múltiples contratistas y subcontratistas, la presencia de estructuras provisorias en permanente transformación, y la exposición a riesgos que varían día a día con el avance de los trabajos (Decreto 911/96, 1996).

Este reglamento aborda de manera específica los riesgos más frecuentes y graves de la actividad: trabajos en altura con andamios y plataformas, excavaciones, instalaciones eléctricas provisorias, movimiento de materiales y operación de equipos pesados. Su contribución conceptual es doble. Por un lado, explicita que el riesgo en construcción no depende únicamente del comportamiento individual del trabajador, sino también del diseño del entorno físico —protecciones colectivas, delimitación de áreas, condiciones de acceso y circulación—. Por otro lado, vincula la seguridad a la gestión integral de la obra como sistema, donde la coordinación entre empleadores concurrentes y la planificación preventiva son tan relevantes como las medidas individuales de protección.

##### 16.2.1.5. Resoluciones SRT: programas y coordinación preventiva

La Resolución SRT 51/97 y la Resolución SRT 35/98 completan el marco normativo estableciendo la dimensión organizacional de la prevención. La primera fija la obligación de comunicar el inicio de obra y de elaborar programas de seguridad específicos para cada proyecto, con intervención verificadora de las ART mediante visitas sistemáticas (SRT, 1997). La segunda regula los casos de concurrencia de múltiples empleadores imponiendo la coordinación de esos programas y su verificación conjunta (SRT, 1998).

En el ámbito de la construcción, el cumplimiento normativo se articula con instrumentos operativos impulsados por la Superintendencia de Riesgos del Trabajo (SRT) y por las Aseguradoras de Riesgos del Trabajo (ART). De forma complementaria, el Programa de Construcción difundido por la SRT explicita como objetivo el establecimiento de mecanismos de adopción de medidas preventivas, correctivas y de control, incluyendo la verificación de avisos de obra y la coordinación de programas (SRT, s. f.).

Estas resoluciones refuerzan la concepción de la prevención como proceso continuo y organizado, no como conjunto de medidas puntuales. En este contexto, su relevancia conceptual reside en que sitúan la detección de condiciones de riesgo en un marco institucional más amplio, dado que las alertas generadas por un sistema de monitoreo asistivo no son decisiones autónomas, sino insumos para los mecanismos de supervisión humana y gestión preventiva previstos por la normativa vigente.

##### 16.2.1.6. Estándares voluntarios de gestión

Los estándares internacionales de gestión constituyen herramientas complementarias al marco legal. Si bien su adopción no es obligatoria, proporcionan estructuras sistemáticas para organizar la prevención de riesgos en torno a procesos definidos, responsabilidades asignadas y ciclos de mejora continua. En proyectos que integran tecnología al monitoreo de seguridad, estos estándares ofrecen un marco conceptual para situar las herramientas dentro de un sistema de gestión más amplio.

##### 16.2.1.7. ISO 45001 y sistemas de gestión de SST

La norma ISO 45001:2018 constituye el estándar internacional de referencia para sistemas de gestión de seguridad y salud en el trabajo. Si bien su adopción no es obligatoria bajo la normativa argentina, su marco conceptual resulta relevante para comprender cómo se organiza la prevención como sistema gestionable y auditable (ISO, 2018). El estándar integra identificación de peligros, evaluación de riesgos, control operacional, preparación ante emergencias y revisión del desempeño mediante auditorías y acciones correctivas, todo ello estructurado en el ciclo Planificar-Hacer-Verificar-Actuar (PDCA).

Su valor para el presente análisis reside en que convierte el cumplimiento normativo en una práctica gestionable y verificable: la organización no solo debe cumplir las obligaciones legales, sino demostrar que identifica peligros, implementa controles, verifica resultados y mejora sistemáticamente. Esta perspectiva permite ubicar un sistema de monitoreo asistivo como componente de un sistema de gestión más amplio, evitando interpretarlo como sustituto de la supervisión humana o del control institucional. Las alertas generadas por el sistema son insumos para ese ciclo de gestión, no reemplazos de ninguna de sus etapas.

#### 16.2.2. Operacionalización: prescripción normativa y observable visual

El propósito de las secciones anteriores fue establecer el marco legal y conceptual que define qué condiciones deben cumplirse en una obra civil. Sin embargo, para que este marco resulte operativo en un sistema de monitoreo visual, es necesario traducir las obligaciones normativas a condiciones físicamente observables que puedan ser identificadas en imágenes o video. Este proceso constituye lo que en metodología de investigación se denomina operacionalización, es decir, el proceso de traducción de un concepto abstracto o normativo en indicadores concretos y verificables (Decreto 351/79, 1979; Decreto 911/96, 1996).

La operacionalización aplicada en este capítulo parte de las obligaciones tipificadas en el marco normativo y las transforma en evidencias visuales que manifiestan, de manera observable, el cumplimiento o incumplimiento de cada obligación. Una prescripción como “el empleador debe proveer elementos de protección personal adecuados” (Ley 19.587, 1972) se traduce, por ejemplo, en la evidencia observable “presencia de casco en la región cefálica del trabajador”. Esta traducción no implica equiparar la observación visual con la certificación del cumplimiento normativo —una cuestión que requiere evaluación técnica en terreno y decisión humana—, sino construir un conjunto de señales de atención alineadas con categorías regulatorias reconocidas, que un sistema asistivo puede detectar y reportar para su posterior evaluación por los responsables.

Es importante señalar que esta operacionalización tiene limitaciones inherentes. La visión por computadora captura información visual bidimensional proyectada desde ángulos específicos, lo que puede generar ambigüedades de interpretación. Por ejemplo, un casco que en realidad está siendo transportado en la mano puede proyectarse de manera similar a uno que está siendo usado correctamente desde ciertos ángulos de cámara. Estas ambigüedades no invalidan el valor asistivo del sistema, pero refuerzan la necesidad de que las alertas generadas sean interpretadas por supervisores humanos con capacidad de contextualización, y no como determinaciones definitivas de cumplimiento o incumplimiento normativo.

##### 16.2.2.1. Taxonomía de categorías de riesgo

Para que la operacionalización sea sistemática y trazable al marco normativo, es necesario organizar el análisis en categorías de riesgo que agrupen obligaciones de naturaleza similar. En la construcción civil, las categorías de riesgo más relevantes para este proyecto son aquellas que combinan tres condiciones: presencia normativa, criticidad preventiva y posibilidad de observación visual.

Bajo ese criterio, se consideran principalmente las siguientes categorías: incumplimiento en el uso de equipos de protección personal (EPP), condiciones inseguras en trabajos en altura, acceso no autorizado o desprotegido a zonas restringidas, coexistencia riesgosa entre peatones y maquinaria, y condiciones inadecuadas del entorno físico de trabajo, como desorden, obstrucciones, instalaciones provisorias o ausencia de señalización.

Esta taxonomía no pretende agotar el universo de riesgos en obra. Su función es construir un puente entre obligaciones legales y evidencias verificables en video, de modo que las condiciones priorizadas puedan justificarse tanto desde el marco normativo como desde su factibilidad técnica de detección visual.

##### 16.2.2.2. Matriz de evidencias visuales

La Tabla 10 presenta la operacionalización del marco normativo en términos de evidencias visuales y condiciones detectables en video. Cada fila articula una obligación normativa tipificada, la evidencia física que la materializa, y la condición de riesgo observable que correspondería a su incumplimiento o ausencia. Esta tabla constituye el artefacto analítico central de este capítulo y funciona como insumo conceptual para las etapas posteriores del proyecto en las que se definirán los patrones de consulta del sistema.

**Tabla 10**

*Correspondencia entre obligaciones normativas, evidencias visuales y condiciones de riesgo detectables en video*

| **Categoría de riesgo** | **Prescripción normativa** | **Evidencia operativa / visual** | **Condición detectable en video** |
| --- | --- | --- | --- |
| Uso de EPP — casco | Ley 19.587, arts. 8-9; Dec. 911/96, arts. 98-115 | Casco de seguridad en región cefálica | Persona sin casco; persona en borde elevado sin protección cefálica visible |
| Uso de EPP — chaleco reflectivo | Ley 19.587, arts. 8-9; Dec. 911/96, arts. 98-115 | Chaleco de alta visibilidad en torso | Persona sin chaleco reflectivo en zona de tráfico o maquinaria |
| Uso de EPP — calzado de seguridad | Ley 19.587, arts. 8-9; Dec. 911/96, arts. 98-115 | Calzado con puntera reforzada o bota de seguridad | Persona con calzado inadecuado visible en zonas de riesgo de aplastamiento |
| Protección contra caídas en altura | Ley 19.587, arts. 8-9; Dec. 911/96, arts. 52-57, 98-115 | Arnés con línea de vida; barandas, redes y protecciones perimetrales | Trabajo en altura sin sistema anticaídas visible; borde desprotegido con personas próximas |
| Delimitación de áreas de riesgo | Dec. 351/79, cap. 12; Dec. 911/96, arts. 47, 61-62, 66-69 | Cintas, vallados, cartelería, zonas restringidas demarcadas | Persona dentro de zona restringida; cruce peligroso peatón-maquinaria; ausencia de segregación visible |
| Control de circulación y coexistencia con maquinaria | Dec. 911/96, arts. 47, 70-71 | Rutas separadas, balizamiento, señalero presente | Maquinaria circulando cerca de peatones; ausencia de separación; maniobras en zonas congestionadas |
| Orden, limpieza y gestión de obstáculos | Dec. 351/79, cap. 5; Dec. 911/96, arts. 46-47 | Superficies libres; materiales apilados; escombros contenidos | Pasillos obstruidos; materiales inestables; riesgo de tropiezo por desorden visible |
| Instalaciones eléctricas provisorias | Dec. 911/96, arts. 74-87 | Tableros protegidos; cables con doble aislación; disyuntores | Cableado expuesto en zonas de tránsito; conexiones improvisadas visibles |

*Nota.* La columna “Condición detectable en video” describe situaciones susceptibles de ser identificadas por análisis visual, no determinaciones de cumplimiento normativo. La tabla no constituye selección de prompts ni especificación de sistema; es un artefacto analítico conceptual cuya elaboración es independiente de la tecnología de detección que se adopte en etapas posteriores. Fuente: Elaboración propia basada en las fuentes citadas (Decreto 351/79, 1979; Decreto 911/96, 1996; Ley 19.587, 1972).

Para que las evidencias visuales sistematizadas en la tabla precedente resulten operativas en el contexto del sistema propuesto, es necesario establecer criterios de evaluabilidad que permitan valorar su detección de manera objetiva y reproducible. En este sentido, cada condición observable debe poder vincularse a métricas de desempeño del modelo —tales como precisión, exhaustividad (recall) y tasa de falsos positivos— así como a indicadores de rendimiento en tiempo real, entre los que se incluyen la latencia de inferencia y la tasa de cuadros procesados por segundo. Esta formalización permite no solo validar el comportamiento del sistema en escenarios controlados, sino también comparar configuraciones y arquitecturas de detección alternativas, asegurando coherencia con el marco de evaluación que se define en el protocolo experimental. Cabe señalar que los umbrales específicos y las expresiones formales de estos criterios constituyen decisiones de implementación que se abordarán en etapas posteriores del trabajo.

#### 16.2.3. Integración con sistemas de monitoreo asistivo

De las secciones anteriores, es posible apreciar que el marco normativo de la construcción civil genera un conjunto definido y justificado de condiciones de riesgo que son, en principio, observables en el espacio físico de la obra. Esta observabilidad no es un hallazgo trivial, sino que implica la existencia de una correspondencia estructural entre las obligaciones legales y las señales visuales que un sistema de monitoreo puede capturar, lo que fundamenta la viabilidad conceptual del proyecto como herramienta de apoyo a la prevención.

Sin embargo, esta correspondencia tiene límites que deben quedar explícitos. En primer lugar, no todas las obligaciones normativas tienen correlatos visuales directos. Por ejemplo, prescripciones como la correcta certificación de los EPP según norma IRAM, el ajuste técnico de un arnés o la altura reglamentaria de una baranda son condiciones que, aun manifestándose en el espacio físico, no pueden determinarse con certeza a partir de la imagen. El sistema puede señalar la presencia o ausencia de un elemento, pero no verificar su conformidad técnica. En segundo lugar, la observabilidad visual de una condición no garantiza que el sistema la detecte con precisión en todas las circunstancias, ya que elementos como la iluminación, los ángulos de cámara y las oclusiones introducen variabilidad que el análisis conceptual no puede anticipar completamente.

La integración de estas condiciones en un sistema de este tipo tiene coherencia con el enfoque de la normativa vigente, que concibe la prevención como un proceso continuo de verificación y corrección (ISO, 2018; SRT, 1997, 1998). Un sistema que detecta señales de riesgo a modo de asistencia puede contribuir a sostener la continuidad del control en entornos con múltiples frentes de trabajo simultáneos, complementando la capacidad de observación de los supervisores humanos sin desplazar sus responsabilidades legales ni sustituir los mecanismos institucionales de fiscalización.

Esta lectura es coherente con el enfoque de las resoluciones de la SRT relativas a programas de seguridad, coordinación entre empleadores y verificación en obra, que conciben la prevención como un proceso continuo y organizado (SRT, 1997, 1998). La tecnología no sustituye la evaluación técnica en terreno ni el rol de las ART o de los responsables de seguridad, sino que puede integrarse como un soporte instrumental para fortalecer la detección, la trazabilidad y la respuesta ante condiciones de riesgo observables.

### 16.3. Percepción visión-lenguaje: fundamentos conceptuales de la detección open-vocabulary

Como se mencionó anteriormente, la detección de objetos en imágenes ha sido históricamente un problema de clasificación cerrada, donde los sistemas reconocen únicamente las categorías para las que fueron entrenados. Este supuesto es incompatible con el dominio de seguridad laboral, donde las condiciones de riesgo son heterogéneas, cambian según la etapa de la obra y pueden formularse con precisión en lenguaje natural pero difícilmente acotarse en un conjunto fijo de clases predefinidas. El paradigma de detección de vocabulario abierto (OVD) rompe esa restricción al incorporar un encoder de lenguaje que permite guiar la detección mediante descripciones textuales arbitrarias.

La presente sección caracteriza los fundamentos conceptuales de la detección open-vocabulary, con énfasis en la transición desde los enfoques de vocabulario cerrado hacia modelos capaces de vincular información visual y lenguaje natural. En particular, se desarrollan los principios de alineación visión-lenguaje, el rol del prompt como mecanismo de especificación dinámica y las condiciones que hacen posible formular consultas abiertas sobre escenas visuales.

#### 16.3.1. Del closed-set al open-vocabulary

En la detección de objetos tradicional, el modelo aprende a localizar instancias en una imagen y a clasificarlas dentro de un vocabulario fijo, establecido de antemano y sin posibilidad de expansión en tiempo de inferencia. Esta formulación permite optimizar el rendimiento sobre benchmarks bien delimitados, como MS COCO con 80 categorías (Lin et al., 2014) o PASCAL VOC (Everingham et al., 2010), pero introduce una dependencia estructural entre el dominio de entrenamiento y el dominio de aplicación, siendo que el sistema solo puede detectar lo que fue explícitamente contemplado en el diseño.

La detección open-vocabulary supera esta restricción al separar el espacio semántico del conjunto de categorías de entrenamiento. En lugar de aprender representaciones para clases discretas y fijas, los modelos OVD aprenden a alinear regiones visuales con descripciones lingüísticas en un espacio de embeddings compartido. La noción de clase deja de ser un identificador discreto y pasa a representarse como una entidad semántica continua, definida dinámicamente por el contenido de la consulta (Zareian et al., 2021). En consecuencia, una categoría expresada en lenguaje natural durante la inferencia puede ser reconocida aunque el modelo nunca la haya visto etiquetada durante el entrenamiento, siempre que su representación semántica sea coherente con el espacio aprendido.

Esta capacidad no es absoluta. La calidad de la generalización zero-shot —ampliada en la sección 16.3.5— depende de la calidad y amplitud del preentrenamiento multimodal, y el desempeño sobre categorías muy específicas o visualmente inusuales puede ser significativamente inferior al observado sobre categorías cotidianas bien representadas en los datos de entrenamiento. Reconocer la potencia del paradigma OVD sin ignorar sus condiciones y límites es el propósito de las secciones que siguen.

#### 16.3.2. Mecanismos de alineación visión-lenguaje

El pilar técnico central de OVD es el uso de representaciones conjuntas de visión y lenguaje. Estas representaciones se obtienen mediante modelos multimodales entrenados para proyectar imágenes, regiones visuales y textos en un espacio latente compartido, donde la proximidad geométrica refleja afinidad semántica. El trabajo seminal en esta dirección es CLIP (Contrastive Language–Image Pre-training), que demostró la viabilidad de entrenar modelos con cientos de millones de pares imagen-texto recopilados de la web para aprender representaciones visuales altamente transferibles, alineadas con descripciones en lenguaje natural (Radford et al., 2021).

El entrenamiento contrastivo opera sobre la base de maximizar la compatibilidad entre pares imagen-texto correctos y minimizar entre pares incorrectos, produciendo un encoder visual y un encoder textual que proyectan imagen y texto a un espacio semántico compartido (Minderer et al., 2022, 2023; Radford et al., 2021). El proceso de detección resultante puede describirse en tres etapas conceptuales, donde 1) a partir de una imagen, el backbone visual genera representaciones asociadas a regiones candidatas, 2) a partir de una consulta textual (prompt), el encoder de lenguaje obtiene una representación semántica y finalmente, 3) la detección se resuelve evaluando la compatibilidad entre ambas representaciones mediante funciones de similitud, atención cruzada u otros mecanismos de alineación, aplicando non-maximum suppression sobre las regiones con mayor compatibilidad semántica. Este esquema introduce una separación conceptual entre localización espacial y reconocimiento semántico, lo que permite evaluar nuevas descripciones en tiempo de inferencia sin modificar los parámetros del modelo (Minderer et al., 2022).

#### 16.3.3. Rol del lenguaje natural como especificación dinámica

En detección open-vocabulary, el lenguaje funciona como una especificación de inferencia: la consulta textual define qué concepto debe localizarse sin modificar el clasificador ni volver a entrenar el modelo. Esta propiedad permite expresar entidades, atributos y relaciones mediante vocabulario natural, pero introduce una variable ausente en los detectores closed-set: formulaciones semánticamente cercanas no necesariamente producen representaciones equivalentes. La sensibilidad depende del encoder textual, del contexto léxico y del régimen de alineación empleado durante el preentrenamiento (Zhou et al., 2022b).

La literatura aborda este problema mediante ingeniería sistemática de prompts, prompt learning con tokens de contexto aprendibles y, en algunas arquitecturas, prompts visuales que anclan la consulta a un ejemplo (Du et al., 2022; Jiang et al., 2024; Khattak et al., 2023). Estas alternativas son modalidades de consulta documentadas, no requisitos universales. Para evaluar una condición de dominio, la formulación textual debe tratarse como parte del protocolo experimental: deben compararse variantes bajo los mismos datos, umbrales y métricas, evitando atribuir al modelo diferencias producidas únicamente por la redacción.

#### 16.3.4. Composicionalidad, negación y condiciones definidas por ausencia

El aprendizaje contrastivo aproxima representaciones globales de imágenes y textos al recompensar la compatibilidad entre pares correctos y separar pares incorrectos. Ese objetivo no obliga a codificar de manera explícita quién realiza una acción, qué atributo modifica a cada entidad ni en qué orden aparecen los términos. Esto no significa que los modelos ignoren las palabras, sino que un buen desempeño de recuperación puede coexistir con baja sensibilidad a la estructura relacional de la frase.

Yuksekgonul et al. (2023) estudian esta limitación mediante ARO, un benchmark con más de 50.000 casos organizados en atribución, relación y orden. Los resultados muestran que modelos visión-lenguaje de referencia pueden apoyarse fuertemente en el inventario léxico y resolver coincidencias globales sin representar con igual robustez los vínculos entre sustantivos, atributos y relaciones. El comportamiento se aproxima así a una bolsa de palabras: los conceptos dominantes conservan gran peso aunque se intercambien modificadores o cambie la estructura que determina el significado.

Winoground aísla la composicionalidad con pares de captions que contienen exactamente las mismas palabras en distinto orden y se asocian con dos imágenes diferentes. Los modelos evaluados no superaron de manera consistente el azar al vincular cada caption con la imagen correcta (Thrush et al., 2022). La prueba elimina la ventaja del contenido léxico compartido y muestra que la alineación global no garantiza razonamiento visio-lingüístico sobre roles y relaciones.

En detección y phrase grounding, la asociación entre tokens y regiones aporta localización más fina que la recuperación global, pero la negación mantiene una dificultad conceptual. Una frase como «persona sin casco» contiene el concepto positivo casco; sin embargo, la ausencia no constituye una región visible que pueda recibir una caja. Además, el solapamiento léxico puede hacer que el sustantivo positivo conserve influencia aun cuando el modificador cambie la condición solicitada (Liu et al., 2024). Evaluar ausencia exige definir qué región de la persona resulta pertinente, qué evidencia positiva debería encontrarse y bajo qué relación espacial se considera asociada.

Por ello, una condición definida por ausencia admite al menos dos formulaciones conceptuales: solicitar directamente al modelo que localice la infracción completa, o solicitar evidencia positiva —persona y elemento de protección— y derivar la ausencia mediante razonamiento sobre las detecciones. La primera delega composición y negación al modelo; la segunda separa percepción y relación, pero introduce reglas y posibles errores de asociación. La literatura no establece una alternativa universalmente superior. Su desempeño depende del modelo, del prompt, de la granularidad espacial y del dominio, por lo que la comparación debe permanecer como pregunta empírica. Esta limitación enlaza con la brecha de contextualización semántica de la sección 15.2.5.1 sin anticipar la estrategia que adopte el diseño.

#### 16.3.5. Generalización zero-shot y el problema del long-tail semántico

Un concepto estrechamente vinculado a la OVD es la generalización zero-shot, siendo esta la capacidad de reconocer conceptos no observados explícitamente durante el entrenamiento supervisado. Esta propiedad resulta especialmente relevante en dominios caracterizados por distribuciones de clases desbalanceadas o por una fuerte presencia de categorías poco frecuentes, denominadas en la literatura como long-tail semántico.

Los modelos OVD no eliminan por completo las limitaciones impuestas por los datos de preentrenamiento: categorías visualmente inusuales o semánticamente distantes de los conceptos mejor representados pueden exhibir un desempeño inferior al observado en categorías frecuentes. En construcción civil, esto afecta especialmente a categorías especializadas del dominio —incluidos determinados EPP y roles operativos— cuya representación en los datos generalistas puede ser limitada. Por ello, su desempeño zero-shot debe verificarse en material de dominio y no inferirse desde benchmarks generales.

La ampliación de datos y el autoentrenamiento mejoran la cobertura de categorías raras, pero no eliminan la brecha entre benchmarks generalistas y dominios especializados (Minderer et al., 2023).

#### 16.3.6. Dimensiones de comparación de modelos OVD

La literatura permite comparar modelos OVD a lo largo de dimensiones distintas: capacidad de generalización zero-shot y transferencia de dominio; expresividad frente a atributos y relaciones; latencia y dependencia del hardware; modalidad de consulta; disponibilidad de código y pesos; y posibilidades de adaptación paramétrica. Ninguna dimensión determina por sí sola la adecuación de una alternativa, y los resultados de benchmarks no son directamente transferibles entre hardware, resoluciones y regímenes de evaluación diferentes (Cheng et al., 2024; Liu et al., 2024; Minderer et al., 2022, 2023).

La retención open-vocabulary después del fine-tuning tampoco puede atribuirse a la familia arquitectónica. Como se sintetiza en la sección 15.2.4, depende de la receta concreta: qué parámetros se actualizan o congelan, si se conserva supervisión lingüística amplia y si el protocolo evalúa categorías no vistas (A. Wang et al., 2025; X. Zhao et al., 2024). Los prompts visuales, la segmentación o la ejecución híbrida entre modelos pueden describirse como capacidades presentes en parte de la literatura, pero no constituyen requisitos generales. El peso asignado a cada dimensión pertenece a la metodología y al diseño posterior, donde debe justificarse con relación al alcance experimental.

### 16.4. Persistencia temporal de entidades y fundamentos conceptuales del seguimiento multiobjeto

Una detección aislada no basta para sustentar una alerta temporal. Para distinguir entre una aparición breve y una condición que permanece, se requiere continuidad entre cuadros, una propiedad que la detección por cuadro no provee. El seguimiento multiobjeto (MOT) cumple esa función al asignar identificadores temporales internos a las entidades detectadas, estimar sus trayectorias cuadro a cuadro y sostener la continuidad ante omisiones breves. La presente sección caracteriza los fundamentos técnicos de ese mecanismo, sus métodos representativos y los compromisos relevantes para integrarlo en un sistema de monitoreo.

#### 16.4.1. La limitación temporal de la detección por cuadro

Un detector de objetos —incluyendo los modelos OVD— opera de manera fundamentalmente estática: dada una imagen, produce un conjunto de regiones detectadas con sus etiquetas semánticas y puntajes de confianza. Esta operación se realiza de manera independiente para cada cuadro del flujo de video, sin memoria ni referencia a los cuadros anteriores. En consecuencia, el mismo objeto físico presente en dos cuadros consecutivos es tratado como dos entidades sin relación; no existe ningún mecanismo que les asigne una identidad común ni que modele su trayectoria a lo largo del tiempo (Bewley et al., 2016; Luo et al., 2021).

Esta limitación tiene consecuencias operativas directas para el sistema de monitoreo. En primer lugar, la variabilidad cuadro a cuadro que caracteriza a los modelos OVD —fluctuaciones en puntajes de confianza, apariciones y desapariciones espurias e inconsistencias entre cuadros consecutivos (Xiao et al., 2024)— no puede filtrarse ni estabilizarse sin una capa que integre información temporal. En segundo lugar, muchas condiciones de riesgo no son eventos instantáneos, sino estados que deben persistir durante un intervalo mínimo para resultar operativamente significativos: una presencia sostenida en una zona restringida no equivale a una detección espuria de un único cuadro (Du et al., 2024). En tercer lugar, las alertas basadas en evidencia sostenida —y no en detecciones aisladas— pueden reducir la carga cognitiva y la fatiga de alerta asociada con falsos positivos frecuentes (Du et al., 2024).

El seguimiento multiobjeto aporta la capa de integración temporal que la detección por cuadro no ofrece: asigna identificadores temporales internos a las entidades detectadas, modela su estado y trayectoria a lo largo de la secuencia y produce trayectorias estructuradas sobre las que puede agregarse evidencia temporal (Du et al., 2024; Milan et al., 2016).

#### 16.4.2. Fundamentos del MOT y del paradigma tracking-by-detection

El seguimiento multiobjeto estima trayectorias a partir de detecciones ruidosas e incompletas. En el paradigma tracking-by-detection, un detector externo localiza objetos en cada cuadro y el tracker mantiene un estado temporal para cada trayectoria activa. Este desacoplamiento permite integrar detectores con vocabularios y arquitecturas diferentes sin reentrenar necesariamente el componente temporal, aunque conserva una dependencia inevitable: toda trayectoria se origina en las observaciones entregadas por el detector (Adžemović, 2025; Bewley et al., 2016).

El estado de una trayectoria resume información acumulada dentro de la secuencia: identificador temporal, última caja observada, antigüedad y número de cuadros sin asociación, entre otros atributos posibles. Ese identificador sólo organiza observaciones dentro del flujo; no representa identidad personal ni garantiza continuidad entre cámaras, sesiones o reinicios. Una trayectoria puede encontrarse en estado tentativo, activo o perdido según la evidencia disponible, pero la terminología concreta depende del método y no constituye un requisito universal (Milan et al., 2016).

El ciclo de seguimiento comprende tres operaciones conceptuales. La predicción estima dónde debería encontrarse una trayectoria en el cuadro siguiente; puede utilizar el último estado observado o un modelo de movimiento. La similitud cuantifica la compatibilidad entre una predicción y una detección. La intersección sobre unión (IoU) divide el área de intersección de dos cajas por el área de su unión y ofrece una señal geométrica interpretable, sin parámetros aprendidos. Su principal límite aparece cuando el desplazamiento, la oclusión o la inestabilidad de las cajas reducen la superposición aun cuando ambas observaciones correspondan a la misma entidad (Bewley et al., 2016).

La asignación convierte la matriz de similitudes en correspondencias globales. Habitualmente se formula como un problema bipartito entre trayectorias y detecciones y se resuelve con el algoritmo húngaro. Los mecanismos de gating descartan pares incompatibles antes de asignar; los umbrales controlan qué costo resulta aceptable. Las detecciones no asignadas pueden iniciar trayectorias nuevas y las trayectorias sin observación pueden conservarse durante una ventana limitada. Esta memoria tolera omisiones breves, pero incrementarla también aumenta el riesgo de reasociar una detección a la trayectoria equivocada.

La apariencia agrega embeddings de reidentificación a la evidencia geométrica y puede mejorar la reasociación durante cruces u oclusiones. A cambio, introduce cómputo, parámetros entrenados y sensibilidad al dominio visual (Wojke et al., 2017). Los métodos puramente geométricos reducen esas dependencias, pero son más frágiles cuando varias personas ocupan posiciones cercanas o desaparecen por intervalos prolongados. Ningún mecanismo recupera información que el detector nunca observó: falsos negativos, cajas inestables y detecciones espurias pueden fragmentar trayectorias o producir cambios de identificador.

Por ello, el aporte del tracker debe interpretarse como organización temporal de evidencia, no como corrección semántica automática. La evaluación del seguimiento distingue localización, asociación y continuidad; la evaluación de una alerta agrega otras decisiones —persistencia mínima, reglas de estado y tratamiento de episodios— que pertenecen al protocolo experimental. Esta separación evita trasladar métricas MOT a la plataforma completa cuando no existen anotaciones ni objetivos específicos para ese problema.

#### 16.4.3. Integración conceptual entre OVD y MOT

Un detector OVD produce cajas, etiquetas abiertas y puntajes condicionados por el prompt; un tracker opera principalmente sobre geometría, movimiento y continuidad temporal. La identidad de seguimiento es, por lo tanto, un identificador interno y efímero dentro de un flujo, no una identidad personal ni un mecanismo de reconocimiento. Esta separación permite agregar evidencia por entidad a lo largo de una secuencia sin atribuir nombre o identidad civil a la persona observada.

La integración básica encadena percepción y asociación: las detecciones de cada cuadro alimentan al tracker, que actualiza trayectorias; sobre esas trayectorias pueden agregarse puntajes, evaluar persistencia y reconocer cambios de estado. El tracker aporta continuidad, pero no resuelve por sí mismo la incertidumbre semántica. Si la etiqueta o el puntaje del detector fluctúan, el sistema necesita una regla separada de agregación temporal para decidir qué evidencia conserva y durante cuánto tiempo.

La literatura muestra que el seguimiento puede reducir la sensibilidad a detecciones aisladas y sostener evidencia durante omisiones breves, aunque su calidad continúa limitada por la estabilidad del detector y por las oclusiones (S. Li et al., 2023, 2025). Una asociación geométricamente correcta no implica que la condición semántica esté bien interpretada; de manera inversa, una detección semánticamente correcta puede asignarse a una trayectoria equivocada. Esta distinción justifica evaluar percepción y persistencia como niveles relacionados pero no equivalentes.

Los métodos sin apariencia reducen dependencias de entrenamiento, mientras que los métodos con ReID pueden mejorar la reasociación a costa de modelos y datos adicionales (Adžemović, 2025; Wojke et al., 2017). La selección del mecanismo, las ventanas de vida de las trayectorias y las reglas de estabilización pertenecen al protocolo y al diseño posterior.

### 16.5. Operación en tiempo real, transmisión y procesamiento cercano a la fuente

Un sistema de percepción puede ser preciso y, aun así, resultar operativamente inadecuado si la evidencia llega después del margen disponible para interpretarla. La latencia es una propiedad acumulativa del pipeline completo y no del modelo o del protocolo por separado. Esta sección delimita los tramos temporales relevantes, una descomposición instrumental de Glass-to-Algorithm y los patrones arquitectónicos que permiten sostener flujos continuos sin confundir transporte, inferencia, confirmación temporal y notificación.

#### 16.5.1. La latencia extremo a extremo como restricción de diseño

En sistemas de video analítico, la expresión latencia extremo a extremo sólo resulta interpretable cuando se declara el punto inicial y el punto final. Glass-to-Glass (G2G) abarca desde la captura hasta la presentación del contenido en una interfaz; Glass-to-Algorithm (G2A) termina cuando el resultado algorítmico asociado a un cuadro queda disponible (Axis Communications AB, 2015; Bachhuber et al., 2018). En una plataforma de alertas, G2A caracteriza un subtramo instrumental por cuadro: no incluye por sí solo la asociación temporal, la ventana necesaria para confirmar una condición, el registro de la alerta ni su distribución.

La percepción humana aporta una referencia, no una cota universal. Retardos alrededor de 100 ms comienzan a afectar la sensación de inmediatez en tareas interactivas, y diferencias de decenas de milisegundos pueden percibirse en tareas de manipulación directa (Card et al., 2008; Deber et al., 2015). Un sistema de supervisión puede admitir presupuestos mayores según el perfil temporal del riesgo, el tipo de intervención y el papel del operador. La magnitud admisible debe fijarse en el protocolo experimental y relacionarse con la condición evaluada.

La latencia total es acumulativa. Captura, suministro de la fuente, transformaciones, copias de memoria e inferencia aportan retardos de naturaleza diferente. Optimizar un componente no garantiza una reducción equivalente del total si otro domina la ruta crítica. Además, una tasa media compatible con tiempo real puede ocultar colas crecientes o episodios de saturación; por eso la medición debe considerar percentiles, backlog y comportamiento sostenido, no sólo el promedio.

El buffering ilustra el compromiso central. Una cola o jitter buffer absorbe variaciones y desacopla ritmos entre productor y consumidor, pero cada unidad retenida incrementa el retardo. El diseño debe presupuestar los buffers y declarar sus políticas: eliminarlos indiscriminadamente puede producir pérdidas e inestabilidad, mientras sobredimensionarlos convierte un déficit de throughput en latencia acumulada (Axis Communications AB, 2015; Gettys & Nichols, 2012).

#### 16.5.2. Descomposición instrumental de Glass-to-Algorithm

Para mantener una notación consistente con el protocolo experimental, el subtramo G2A se descompone en cuatro componentes observables:

t_G2A = t_capture + t_transport + t_preprocess + t_inference (1)

t_capture representa la adquisición o lectura del cuadro hasta su disponibilidad para el host o consumidor instrumentado. t_transport comprende el suministro efectivo de la fuente —red, stream o lectura local—, incluidos los buffers y operaciones de entrada/salida que correspondan. t_preprocess agrupa decodificación cuando aplique, conversión de formato, redimensionado, normalización y transferencias de memoria. t_inference mide la ejecución del modelo hasta producir su salida algorítmica. La separación evita introducir renderizado o notificación en una métrica que termina antes de la interfaz (Bachhuber et al., 2018; H. Wang et al., 2022).

La Tabla 11 sintetiza los cuatro componentes instrumentales y los criterios necesarios para interpretar cada uno.

**Tabla 11**

*Componentes instrumentales del subtramo Glass-to-Algorithm*

| **Componente** | **Definición operativa** | **Fuentes principales de variabilidad** | **Criterio de interpretación** |
| --- | --- | --- | --- |
| t_capture | Captura, lectura o dequeue del cuadro en el punto temporal definido por la instrumentación | Período de cuadro, exposición, ISP y buffering de la fuente | Debe declararse el origen exacto del timestamp; a 30 fps, un período de cuadro es ≈33,3 ms |
| t_transport | Entrega del cuadro desde la fuente al consumidor del pipeline, por red, stream o I/O local | Jitter, colas, pérdida, retransmisiones, buffers y ritmo de lectura | La cola y los percentiles describen mejor la estabilidad que la media aislada |
| t_preprocess | Preparación de la entrada del modelo | Decodificación, formato de píxel, resize, normalización y movimiento CPU–GPU | Debe medirse por configuración porque las copias de memoria pueden dominar en pipelines acelerados |
| t_inference | Ejecución del modelo hasta obtener detecciones o resultados equivalentes | Arquitectura, resolución, vocabulario, runtime y hardware | La literatura reporta órdenes de 10–30 ms para alternativas one-stage optimizadas y 50–150 ms para Transformers sin optimización equivalente |

*Nota.* Los rangos son referencias contextuales y no garantías. G2A no equivale a latencia de alerta: el seguimiento, el razonamiento, la ventana de persistencia y la distribución pertenecen a tramos posteriores. Fuente: elaboración propia basada en Axis Communications AB (2015), Bachhuber et al. (2018), Cheng et al. (2024), H. Wang et al. (2022) y Ren, Jiang, et al. (2024).

La captura está condicionada por el ritmo de origen. A 30 fps, el período entre cuadros es de aproximadamente 33,3 ms, aunque el punto de observación puede encontrarse después de exposición, procesamiento interno o buffers de cámara. Por ello, “captura” no debe suponerse equivalente al instante físico en que la luz alcanza el sensor: la instrumentación debe declarar si comienza en el sensor, en la recepción, en la lectura o en el dequeue de la aplicación.

El transporte es el componente más expuesto a variación externa. Propagación y procesamiento de red suelen ser relativamente estables; el encolado, el jitter y las retransmisiones dependen de la carga. En una fuente local, el término sigue existiendo como costo de lectura, demultiplexado o buffering. Lo que compromete el tiempo real no es sólo un valor medio elevado, sino una cola que crece porque el consumidor procesa por debajo del ritmo de entrada. Percentiles y ocupación de cola permiten distinguir un episodio aislado de un déficit sostenido (Gettys & Nichols, 2012; Kurose & Ross, 2021).

El preprocesamiento debe incluir todas las transformaciones efectivamente ejecutadas antes del modelo. La decodificación, la conversión de color, el redimensionado, la normalización y las transferencias CPU–GPU pueden constituir una fracción relevante, especialmente cuando se introducen copias intermedias. Agruparlas bajo un término explícito evita atribuir a la inferencia demoras que pertenecen a la preparación de datos.

La inferencia depende de arquitectura, resolución, número de consultas, runtime y hardware. Los rangos publicados para alternativas one-stage optimizadas y Transformers no optimizados son órdenes de magnitud obtenidos en configuraciones heterogéneas; no deben trasladarse como predicción. La medición por componentes permite identificar si una configuración está limitada por el modelo, por la fuente o por el movimiento de datos, y separa el costo por cuadro de la confirmación temporal de una alerta.

La instrumentación debe fijar límites observables y utilizar un dominio temporal coherente. Cuando el origen no expone el instante físico de captura —situación habitual en streams, archivos o SDK de cámara—, t_capture comienza en el punto más temprano que la aplicación puede medir y esa convención debe declararse. Los timestamps de CPU y acelerador tampoco son intercambiables sin sincronización: una operación asíncrona puede parecer concluida antes de que el dispositivo haya terminado el trabajo. Por ello, los límites de t_preprocess y t_inference deben definirse con las barreras o sincronizaciones que correspondan al runtime (H. Wang et al., 2022).

La ecuación expresa el recorrido temporal de una unidad, pero no implica que la tasa de procesamiento sea el inverso de esa latencia. En un pipeline, distintas etapas pueden solaparse: mientras un cuadro se infiere, otro puede estar siendo capturado o preparado. El throughput describe cuántas unidades se completan por unidad de tiempo; la latencia describe cuánto tarda una unidad desde su origen hasta su salida. Para localizar cuellos de botella deben medirse ambos y evitarse sumas de promedios obtenidos sobre corridas o poblaciones diferentes (Bachhuber et al., 2018; Bass et al., 2022).

Un reporte reproducible debe declarar período de calentamiento, tamaño de lote, resolución, vocabulario o número de consultas, precisión numérica, runtime, fuente de video y política de colas. Además del tamaño muestral y la tendencia central, conviene informar percentiles de latencia, cuadros descartados, ocupación máxima de cola y throughput sostenido. Estas variables permiten distinguir variación ocasional de saturación sistemática y vincular el resultado global con el componente que la produce (Gettys & Nichols, 2012).

#### 16.5.3. Separación de planos y flujo productor-consumidor

En sistemas de análisis continuo resulta útil distinguir una ruta de datos —captura, transformación e inferencia— de una ruta de control que administra configuración, eventos y coordinación. La separación deriva de patrones de planos de datos y control y permite optimizar el flujo continuo sin bloquearlo con operaciones discretas de gobierno o notificación (Kreutz et al., 2015). No prescribe una distribución física ni una tecnología particular: ambos planos pueden coexistir en un host o distribuirse cuando el diseño lo justifique.

La ruta de datos prioriza throughput sostenido, latencia acotada y un orden definido de transformaciones. La ruta de control procesa comandos, cambios de configuración y eventos a ritmos no necesariamente ligados a la tasa de cuadros. Mantener responsabilidades diferenciadas facilita aislar cuellos de botella y evita que una operación de registro o notificación bloquee la recepción del siguiente cuadro (Bass et al., 2022). Esta separación es conceptual: no convierte por sí sola al sistema en distribuido ni exige una nube.

La ruta crítica puede modelarse como una cadena productor-consumidor. Cada etapa produce unidades que la siguiente consume; cuando el productor supera sostenidamente la capacidad del consumidor, una cola sin límite convierte el déficit de throughput en latencia creciente. Las colas acotadas, la contrapresión y las políticas explícitas de descarte, muestreo o sustitución permiten mantener el sistema observable. La política adecuada depende de la semántica: conservar todas las unidades puede ser necesario para relectura reproducible, mientras que una ruta viva puede priorizar evidencia reciente para evitar procesar cuadros obsoletos.

El desacoplamiento no elimina la necesidad de medir. Deben observarse ritmo de producción, ritmo de consumo, ocupación de cola, unidades descartadas y tiempo de residencia. Un sistema que reporta FPS aceptables pero acumula backlog no opera en tiempo real; simplemente procesa con retraso.

Para eventos discretos, el patrón publish/subscribe separa productores y consumidores: el emisor publica sin conocer todos los destinos y cada suscriptor procesa los tipos de evento pertinentes. Conviene distinguir tres responsabilidades: el transporte en ejecución entrega eventos a consumidores activos; la persistencia conserva hechos para relectura o auditoría; y la distribución externa comunica una alerta. Un bus puede desacoplar componentes, pero no garantiza por sí mismo que los eventos sobrevivan a una desconexión; la durabilidad requiere un repositorio o una política de retención independiente de la mensajería en vivo (Cugola & Margara, 2012).

Las garantías de entrega también forman parte del contrato conceptual. Una entrega al menos una vez puede producir reenvíos y, por lo tanto, duplicados; una entrega como máximo una vez puede perder mensajes; y exactamente una vez exige coordinación adicional. Cuando una alerta no debe producir efectos repetidos, el evento necesita una identidad estable y el consumidor debe procesarlo de manera idempotente. MQTT QoS 1 ejemplifica la primera semántica mediante confirmación, sin convertirla en una garantía de ausencia de duplicados (OASIS, 2019). Estas propiedades fundamentan la evaluación de mensajería sin prescribir una tecnología arquitectónica concreta.

#### 16.5.4. Computación en el borde y filtrado cercano al origen

La literatura utiliza edge, fog y cloud con fronteras variables. En este trabajo, edge designa cómputo en el dispositivo, gateway inmediato o servidor próximo a la fuente; fog, una capa intermedia de agregación cercana o regional; y cloud, centros de datos centralizados (Iorga et al., 2018; Yousefpour et al., 2019). La convención permite describir tres patrones: procesamiento en el dispositivo, procesamiento en un nodo cercano y partición colaborativa entre niveles (Chen & Ran, 2019).

Acercar cómputo al origen puede reducir ida y vuelta de red, ancho de banda y exposición de video crudo, pero introduce límites de memoria, energía y temperatura (Satyanarayanan, 2017; Shi et al., 2016). La nube ofrece elasticidad y recursos centralizados, aunque depende de conectividad y amplía el recorrido del dato. Una capa fog puede agregar varias fuentes, aplicar políticas o resumir información antes de enviarla a niveles superiores. Ningún nivel es intrínsecamente superior: su conveniencia depende del tramo que se desplace y de la carga sostenida.

No toda operación cercana al sensor equivale a inferencia completa en el borde. Una cámara inteligente puede ejecutar adquisición, filtrado, selección de cuadros, conversión o preprocesamiento y enviar sólo las unidades necesarias al consumidor principal. Este reparto reduce el consumo aguas abajo sin atribuir al dispositivo capacidades de detección que no ejecuta. La distinción es importante para analizar gateways y cámaras programables sin confundir prefiltrado con despliegue integral del modelo.

En video analytics, filtrar o resumir cerca del origen disminuye tráfico y carga posterior. Ananthanarayanan et al. (2017) muestran que procesar cerca de las cámaras permite reducir ancho de banda y distribuir recursos en cargas de video a escala. En un prototipo, el mismo principio puede evaluarse de forma acotada: cuánto trabajo se ejecuta antes del host, qué evidencia se descarta y qué impacto tiene esa decisión sobre calidad y latencia.

El punto de partición debe evaluarse por latencia, throughput, privacidad, capacidad sostenida y reproducibilidad. Métricas nominales como TOPS no bastan para anticipar el comportamiento de una aplicación. Bajo carga prolongada, límites térmicos, memoria compartida y variaciones del runtime pueden degradar el ritmo; por ello, los percentiles de latencia, el uso de memoria, el throughput efectivo y los eventos de saturación resultan más informativos que un máximo instantáneo (Satyanarayanan, 2017; Shi et al., 2016). La decisión de ejecutar inferencia en el borde, en un host cercano o en infraestructura remota debe mantenerse separada de la decisión de filtrar cerca del origen.

El filtrado cercano al origen introduce, a su vez, un compromiso metodológico. Seleccionar cuadros, reducir resolución, limitar regiones o descartar unidades disminuye carga y ancho de banda, pero modifica la evidencia que recibe el detector y puede afectar la continuidad temporal. Por ello, la política de prefiltrado debe declararse junto con la fuente y conservar parámetros suficientes para reproducirla; dos configuraciones sólo son comparables si procesan materiales y reglas de selección equivalentes.

Desplazar procesamiento hacia la fuente puede reducir la transmisión de video crudo, pero no elimina por sí mismo el tratamiento de datos personales. Metadatos temporales, zonas, trayectorias y recortes pueden mantener capacidad de identificación indirecta, por lo que la minimización debe evaluarse sobre el conjunto de datos producido y no únicamente sobre la ubicación física del cómputo (European Data Protection Board, 2020).

#### 16.5.5. Brecha de evaluación integrada

La literatura caracteriza por separado protocolos, códecs, hardware y modelos de inferencia, pero no ofrece un marco universal para presupuestar la latencia extremo a extremo de un pipeline que integra detección open-vocabulary. Los resultados aislados sólo funcionan como referencias externas; la adecuación debe verificarse mediante instrumentación del sistema completo y una definición explícita del tramo medido. Esta brecha se corresponde con la identificada en la sección 15.4.3.1 y fundamenta la necesidad de un protocolo reproducible sin anticipar la selección del stack.

### 16.6. Marco ético-legal para el análisis automatizado de video en entornos laborales

#### 16.6.1. Encuadre ético-legal y carácter asistivo

El análisis automatizado de video en el trabajo involucra una asimetría entre quienes controlan el sistema y las personas captadas. El propósito preventivo no basta para legitimar el tratamiento: deben delimitarse finalidad, proporcionalidad, seguridad, transparencia, supervisión humana y responsabilidades sobre el ciclo de vida de los datos (Organisation for Economic Co-operation and Development, 2019; UNESCO, 2021). Esta sección caracteriza el régimen aplicable y las restricciones que impone al diseño, sin convertir observaciones visuales en determinaciones normativas ni habilitar identificación personal.

#### 16.6.2. Delimitación del tratamiento de datos en sistemas de visión por computadora

Los sistemas de visión por computadora aplicados a entornos laborales suelen apoyarse en flujos continuos de imágenes para identificar objetos, personas y condiciones de trabajo. Desde una perspectiva jurídico-técnica, este tipo de información no se agota en su dimensión “visual”: en muchos escenarios, una imagen constituye un dato personal en la medida en que permite identificar, directa o indirectamente, a una persona o hacerla identificable a partir de asociaciones razonables con otros datos disponibles (Agencia de Acceso a la Información Pública, s. f.-a; Argentina, 2000). En consecuencia, aun cuando el objetivo operativo del sistema sea la prevención de riesgos, la captación y el análisis de video pueden configurar un tratamiento de datos personales sujeto a obligaciones específicas.

En un caso de uso típico de obra —videovigilancia con analítica basada en IA— el tratamiento involucra, como mínimo, (i) la recolección (captura por cámaras), (ii) el almacenamiento o transmisión del flujo, (iii) el análisis automatizado (inferencia) y (iv) la generación de salidas (alertas, registros, reportes). Cada una de estas etapas puede incrementar o reducir el impacto sobre la privacidad, según se adopten medidas de minimización, segmentación funcional y control de acceso. Este encuadre es relevante porque la protección de datos personales se estructura en torno a la finalidad y a la proporcionalidad del tratamiento: no basta con que el objetivo sea legítimo, sino que el diseño del sistema debe evitar captaciones y usos innecesarios o excesivos para el fin perseguido (Argentina, 2000; European Data Protection Board, 2020).

En el plano organizacional, el régimen de protección de datos distingue roles con responsabilidades diferenciadas. Quien determina los fines y medios del tratamiento asume el carácter de responsable del banco de datos, mientras que terceros que procesan información por cuenta del responsable actúan como encargados o prestadores de servicios. Esta distinción resulta central en soluciones tecnológicas que integran proveedores de infraestructura, plataformas de análisis o servicios en la nube, ya que exige definir obligaciones contractuales, medidas de seguridad y límites de uso coherentes con la finalidad declarada (Argentina, 2000, 2001).

##### 16.6.2.1. Régimen argentino de protección de datos aplicable a imágenes y videovigilancia

En Argentina, el tratamiento de datos personales se rige por la Ley 25.326 de Protección de los Datos Personales y su reglamentación mediante el Decreto 1558/2001 (Argentina, 2000, 2001). El marco establece que los datos deben ser recolectados para fines determinados, explícitos y legítimos, y que su tratamiento no puede desviarse de esos fines. Los principios de calidad y proporcionalidad imponen que la información sea adecuada, pertinente y no excesiva en relación con la finalidad declarada (Argentina, 2000).

La Ley 25.326 define como dato personal toda información referida a personas determinadas o determinables (Argentina, 2000). Esta definición tiene implicaciones operativas directas: una imagen puede identificar a una persona de manera directa por sus rasgos físicos, o de manera indirecta por la combinación con metadatos como hora, zona de obra, turno de trabajo o secuencia de posiciones. De allí que, aun cuando el sistema excluya explícitamente el reconocimiento facial, el análisis de impacto sobre la privacidad no puede limitarse a las salidas directas del modelo: debe considerar la identificabilidad global que emerge del ecosistema de datos que el sistema genera y almacena (Agencia de Acceso a la Información Pública, s. f.-a; Argentina, 2000).

El régimen también garantiza derechos de los titulares —como acceso, rectificación, actualización y supresión— y prevé la vía constitucional del habeas data para proteger la intimidad y controlar el uso de la información personal. Estas garantías son relevantes en escenarios de videovigilancia, donde el titular puede desconocer el alcance de la captación, la duración de conservación o los destinatarios de la información. Por ello, la transparencia y la trazabilidad del tratamiento se vuelven condiciones prácticas para que los derechos no queden meramente formales (Agencia de Acceso a la Información Pública, s. f.-a; Argentina, 2000).

##### 16.6.2.2. Disposición 10/2015

La Disposición 10/2015 de la Dirección Nacional de Protección de Datos Personales —hoy bajo la órbita de la Agencia de Acceso a la Información Pública (AAIP)— constituye el principal instrumento reglamentario específico para sistemas de videovigilancia en Argentina. Su función es operacionalizar los principios generales de la Ley 25.326 en el contexto de la captación sistemática de imágenes, traduciendo los principios de licitud, finalidad, proporcionalidad, transparencia y seguridad en criterios prácticos de diseño e implementación (Argentina, 2015).

Las condiciones de licitud más relevantes que establece la Disposición 10/2015 se organizan en tres ejes. El primero es el requisito de información previa al titular del dato, que puede cumplirse mediante cartelería visible que informe la existencia de dispositivos de captación, la finalidad del tratamiento y los datos de contacto del responsable para el ejercicio de derechos (Argentina, 2015). El segundo es la exigencia de contar con un manual o política de tratamiento de datos personales que defina finalidades, responsables, procedimientos de gestión, mecanismos de seguridad, criterios de conservación y pautas de acceso y divulgación (Argentina, 2015); este manual opera como el instrumento que vincula el diseño técnico del sistema con el cumplimiento normativo. El tercero es la obligación de inscribir las bases de datos de videovigilancia ante la AAIP, acompañando la solicitud con el manual de tratamiento (Agencia de Acceso a la Información Pública, s. f.-b).

[[PENDIENTE: definir con el equipo la aplicabilidad de esta inscripción al contexto experimental y documentar el recaudo adoptado en §17.1 y §17.4.]]

Este requerimiento no se reduce a una formalidad administrativa: contribuye a que la videovigilancia sea gestionada como un tratamiento regulado, con trazabilidad, y no como un recurso técnico difuso susceptible de ampliarse por inercia a nuevos fines.

#### 16.6.3. Medidas de seguridad y protección de la información

Una vez establecidos los requisitos de licitud, transparencia y delimitación de finalidades en el tratamiento de imágenes, adquiere centralidad el plano de la protección efectiva de la información. En los sistemas de videovigilancia —y, en particular, en aquellos que incorporan procesamiento automatizado—, el cumplimiento normativo no se agota en la legitimidad de la captación, sino que exige la adopción de medidas técnicas y organizativas orientadas a prevenir accesos indebidos, usos no autorizados y pérdidas de información. La seguridad de los datos visuales se convierte así en un componente estructural del tratamiento, en tanto condiciona la posibilidad real de garantizar la confidencialidad, la integridad y la disponibilidad de la información, y de sostener en la práctica los principios de protección de datos personales frente a riesgos operativos y de privacidad.

La Disposición 11/2006 establece medidas de seguridad aplicables a archivos y bases de datos de carácter privado, orientadas a preservar la confidencialidad, integridad y disponibilidad de la información (Argentina, 2006). Si bien no prescribe una arquitectura tecnológica específica, fija un estándar de diligencia: el responsable debe adoptar controles proporcionales a la naturaleza de los datos y a los riesgos del tratamiento.

En el contexto de un sistema de análisis de video con inferencia por IA, este estándar se traduce en cuatro dimensiones de control: gestión de accesos bajo el principio de mínimo privilegio, registros de auditoría que permitan reconstruir quién accedió a qué información y cuándo, cifrado en tránsito para los flujos de video y las alertas generadas, y segregación de entornos que impida el acceso lateral desde componentes no críticos hacia el repositorio de video o el historial de alertas (Argentina, 2000, 2006). En sistemas con componente de IA, estos controles deben complementarse con mecanismos de trazabilidad del modelo: versiones, configuraciones de prompts, umbrales de decisión y criterios de actualización deben estar documentados para permitir la auditoría del comportamiento del sistema ante resultados inesperados (ISO, 2023).

La seguridad también se vincula con la temporalidad del tratamiento. En contextos preventivos, la conservación indefinida de video suele resultar difícil de justificar bajo parámetros de proporcionalidad. Por ello, los criterios de retención, borrado seguro y gestión de copias se integran naturalmente a la estrategia de minimización: conservar lo estrictamente necesario para el fin de seguridad y por el tiempo necesario para cumplirlo, evitando acumulaciones que aumenten el impacto ante incidentes o accesos indebidos (European Data Protection Board, 2020).

#### 16.6.4. Referentes comparados y distinción respecto de la biometría

Los marcos comparados sobre videovigilancia refuerzan los principios de finalidad, minimización, transparencia y retención limitada. Las Directrices 3/2019 del EDPB distinguen la captación de video del tratamiento biométrico: una imagen puede ser dato personal sin que exista reconocimiento facial, y el tratamiento se vuelve biométrico cuando se procesan rasgos con la finalidad de identificar de manera unívoca (European Data Protection Board, 2020). Esta distinción fundamenta separar analítica orientada a condiciones observables de mecanismos de identificación personal.

#### 16.6.5. Gobernanza de IA y carácter asistivo

Los principios de gobernanza de IA agregan obligaciones de supervisión humana, trazabilidad, rendición de cuentas y comunicación comprensible de limitaciones. En un sistema asistivo, la salida algorítmica funciona como señal para revisión humana y no como decisión autónoma sobre una persona. El versionado de modelos y configuraciones, la documentación de errores y la posibilidad de reconstruir el comportamiento del sistema son condiciones de auditabilidad, no garantías de corrección (ISO, 2023; Organisation for Economic Co-operation and Development, 2019; UNESCO, 2021).

#### 16.6.6. Implicaciones para el diseño responsable del sistema

El marco normativo y ético opera como condición de contorno sobre la arquitectura y los procedimientos. La Tabla 12 organiza los principios aplicables y los expresa como restricciones que deben considerarse; no afirma que todos los controles se encuentren implementados en el prototipo.

**Tabla 12**

*Principios normativos y éticos y restricciones aplicables al diseño de sistemas de análisis automatizado de video*

| **Principio normativo / ético** | **Fuente** | **Aplicación** | **Restricción que impone al diseño** |
| --- | --- | --- | --- |
| Licitud y finalidad determinada | Ley 25.326 (Argentina, 2000); Disposición 10/2015 (Argentina, 2015) | El tratamiento de imágenes debe limitarse a la detección de condiciones de riesgo laboral y no desviarse hacia control de desempeño, disciplina o vigilancia generalizada | Excluir mecanismos orientados a la identificación individual y documentar la finalidad de cada tratamiento |
| Proporcionalidad y minimización | Ley 25.326 (Argentina, 2000); Directrices 3/2019 (European Data Protection Board, 2020) | La captación y el procesamiento deben limitarse a lo necesario para el fin preventivo | Reducir datos, metadatos y evidencias visuales; no incorporar reconocimiento facial o biométrico |
| Transparencia e información al titular | Ley 25.326 (Argentina, 2000); Disposición 10/2015 (Argentina, 2015) | Las personas captadas deben conocer la existencia, finalidad y responsable del tratamiento | Prever información accesible, señalización y un canal para ejercer derechos |
| Seguridad de la información | Disposición 11/2006 (Argentina, 2006); Ley 25.326 (Argentina, 2000) | Los controles técnicos deben ser proporcionales al riesgo | Aplicar control de acceso, protección en tránsito, segregación de entornos y registro de accesos cuando correspondan |
| Supervisión humana | UNESCO (2021); OECD (Organisation for Economic Co-operation and Development, 2019) | Las alertas son insumos y no determinaciones definitivas | Mantener revisión humana antes de cualquier intervención y evitar acciones autónomas sobre personas |
| Rendición de cuentas y trazabilidad | ISO/IEC 42001:2023 (ISO, 2023); OECD (Organisation for Economic Co-operation and Development, 2019) | El comportamiento del sistema debe ser documentable y revisable | Conservar versiones, configuraciones, métricas y registros suficientes para reconstruir decisiones técnicas |
| Temporalidad y retención mínima | Directrices 3/2019 (European Data Protection Board, 2020); Ley 25.326 (Argentina, 2000) | La conservación debe limitarse al tiempo necesario | Definir retención y borrado seguro conforme a finalidad, proporcionalidad y contexto del tratamiento |

*Nota.* Las normas argentinas citadas tienen carácter obligatorio; los marcos internacionales aportan buenas prácticas de gobernanza. La tabla expresa restricciones, no un inventario de controles implementados. Fuente: elaboración propia basada en Argentina (2000, 2006, 2015), European Data Protection Board (2020), ISO (2023), Organisation for Economic Co-operation and Development (2019) y UNESCO (2021).

#### 16.6.7. Brechas identificadas y tensiones no resueltas

El derecho argentino regula datos personales y videovigilancia, pero no desarrolla de manera específica la analítica visual basada en IA en entornos laborales. Los marcos de gobernanza amplían la discusión hacia supervisión y rendición de cuentas, sin reemplazar las obligaciones legales vigentes (ISO, 2023; Organisation for Economic Co-operation and Development, 2019; UNESCO, 2021).

Persisten tres tensiones principales. Primero, una persona puede resultar indirectamente identificable mediante la combinación de imágenes, tiempo, zona y trayectoria aun sin reconocimiento facial (Agencia de Acceso a la Información Pública, s. f.-a; Argentina, 2000). Segundo, la utilidad de conservar evidencias para analizar riesgos entra en tensión con la minimización y la retención limitada (Argentina, 2000; European Data Protection Board, 2020). Tercero, no existen criterios operativos estandarizados para comunicar la incertidumbre de las alertas a operadores no especializados, por lo que la transparencia debe incluir límites y posibilidad de error.

A estas tensiones se agrega la ausencia de pautas sectoriales específicas para sistemas de IA que analizan video en relaciones laborales. La frontera entre asistencia preventiva y vigilancia de las personas no depende sólo de la capacidad técnica, sino de la finalidad declarada, la información brindada, la posibilidad de revisión humana y la prohibición de convertir una alerta probabilística en una determinación automática sobre un trabajador. La gobernanza debe contemplar además mecanismos para impugnar resultados, documentar límites y revisar usos secundarios que puedan emerger durante la operación (Organisation for Economic Co-operation and Development, 2019; UNESCO, 2021).

### 16.7. Convergencias, brecha transversal y preguntas rectoras

#### 16.7.1. Interdependencia de los dominios

La viabilidad no depende de un detector aislado. La calidad de la percepción condiciona la asociación temporal; la fuente y el transporte delimitan el presupuesto disponible para el cómputo; y el tratamiento de imágenes impone restricciones sobre qué se conserva y cómo se comunica. Por ello, las métricas parciales deben interpretarse dentro de la cadena completa y bajo las condiciones del dominio. Esta interdependencia no determina una arquitectura concreta, pero explica por qué precisión, latencia, persistencia y trazabilidad no pueden evaluarse como problemas independientes (Bass et al., 2022; Cugola & Margara, 2012).

#### 16.7.2. Restricción ético-normativa como brecha transversal

Las brechas técnicas de datasets, prompts, integración y métricas ya fueron sistematizadas en el estado del arte. La brecha genuinamente transversal que agrega este marco es que la legitimidad del tratamiento condiciona simultáneamente percepción, persistencia, almacenamiento y distribución. Una mejora técnica que incremente la identificabilidad o la retención puede ser incompatible con los principios de finalidad y minimización; del mismo modo, una alerta operativamente útil debe conservar revisión humana y trazabilidad. El marco ético-legal actúa así como restricción arquitectónica y procedimental, no como módulo agregado al final (Argentina, 2000, 2015; European Data Protection Board, 2020).

#### 16.7.3. Preguntas rectoras para la consolidación metodológica

El marco teórico delimita las siguientes preguntas, que requieren definición metodológica y evidencia experimental. Los códigos se conservan para mantener la trazabilidad con las secciones posteriores.

**P-E1-01. Presupuesto temporal.** ¿Qué presupuesto de latencia es admisible para el subtramo G2A y para la confirmación de una alerta, sin confundir el cómputo por cuadro con la persistencia temporal? La respuesta debe declarar el origen y el final de cada timestamp, el comportamiento por percentiles y el margen asignado a seguimiento y razonamiento.

**P-E1-02. Condiciones nucleares.** ¿Qué conjunto mínimo de condiciones de riesgo permite evaluar la factibilidad de expresar observables en lenguaje natural, estabilizar evidencia y producir alertas trazables, sin pretender cubrir el catálogo normativo completo? La selección debe distinguir complejidad semántica, evidencia disponible y perfil temporal, pero no asumir que una condición multi-entidad sea obligatoria para demostrar factibilidad.

**P-E1-03. Materiales y anotaciones.** ¿Qué datos públicos y propios ofrecen anotaciones suficientes para evaluar percepción, continuidad temporal y episodios, y cuáles son además aptos para adaptación paramétrica? La respuesta debe separar material de entrenamiento, validación y prueba y evitar reutilizaciones que comprometan la independencia del protocolo.

**P-E1-04. Restricciones de ejecución.** ¿Qué hardware, fuentes de video, resolución, runtime y presupuesto de procesamiento condicionan las configuraciones comparables? La caracterización debe incluir memoria, ritmo efectivo, latencia sostenida y límites de los entornos de inferencia y entrenamiento, que no necesariamente coinciden.

**P-E1-06. Framework de métricas.** ¿Qué métricas y niveles de análisis permiten separar calidad de detección, estado por entidad y comportamiento de la alerta temporal, y qué umbrales se fijan antes de medir? Las métricas de seguimiento sólo resultan aplicables si existen anotaciones y objetivos MOT explícitos; no deben trasladarse automáticamente a la evaluación de alertas.

**P-E1-08. Adaptación paramétrica.** ¿En qué condiciones un ajuste fino ligero mejora el dominio objetivo sin degradar la capacidad open-vocabulary, y cómo se mide esa retención con categorías no vistas? La respuesta exige una receta reproducible, datos diferenciados y una comparación que mantenga separadas especialización y generalización.

Las preguntas se condicionan mutuamente: las condiciones evaluables determinan los datos; el hardware limita configuraciones; y las métricas deben distinguir calidad semántica, rendimiento y confirmación temporal. Su resolución corresponde al protocolo experimental y no se anticipa en esta sección.

### 16.8. Conclusiones parciales de la fundamentación teórica

El marco teórico sostiene la factibilidad conceptual de una plataforma asistiva que recibe video, interpreta observables expresados mediante lenguaje, mantiene continuidad temporal y produce alertas para revisión humana. Esa factibilidad no implica superioridad de OVD frente a detectores supervisados ni capacidad para fiscalizar cumplimiento. Depende de la formulación de las condiciones, del comportamiento en el dominio, de la latencia acumulada y de las restricciones ético-legales.

La revisión también delimita qué no puede inferirse desde la teoría. Los benchmarks generales no predicen por sí solos el rendimiento en construcción; una detección por cuadro no equivale a una alerta; un identificador de seguimiento no es identidad personal; y una capacidad descrita en la literatura no constituye una función implementada. Estas separaciones permiten que el diseño posterior declare alcance y evidencia sin convertir objetivos en resultados.

Se reconocen tres limitaciones del propio marco. El campo OVD evoluciona con rapidez y puede modificar el conjunto de alternativas disponibles; los datos de rendimiento publicados provienen de hardware y condiciones que no representan por sí mismos una obra; y el marco regulatorio de IA y protección de datos puede incorporar nuevas exigencias durante el ciclo de vida del sistema. Estas limitaciones refuerzan la necesidad de decisiones trazables y de validación empírica, sin invalidar la base conceptual desarrollada.
