# 96c — Texto extraído del informe v1.1: §15 Estado del Arte

> **Extracción derivada (2026-07-18)** del `.docx`
> `informe/entregable/E-OVRT-VDP_v1.1_05062026-sin-indice.docx`, **solo para búsqueda y cita**
> (mismo estatuto que el doc 90): al editar, se edita el `.docx`/Google Docs, nunca
> este archivo. Tablas y figuras pueden haber perdido formato; las figuras no se
> extraen. **La §17.3 embebida en el docx NO se incluye en esta serie: está
> desactualizada** — la Etapa 3 vigente es el doc 90 (extracción del standalone).
> Partición completa: 96a (frontmatter+intro+objetivos+plan), 96b (§17.1
> consolidación metodológica — el protocolo), 96c (estado del arte), 96d (marco
> teórico), 96e (cierre+anexos+referencias).

---

## 15. Estado del Arte

El estado del arte reúne los antecedentes técnicos y metodológicos necesarios para contextualizar el desarrollo de una plataforma experimental de detección open-vocabulary en video en tiempo real. Su propósito es revisar los enfoques, modelos y arquitecturas que permiten comprender el alcance actual de la detección visual guiada por lenguaje natural, así como sus limitaciones cuando se la traslada a escenarios dinámicos, con restricciones temporales y requerimientos de seguridad laboral.


### 15.1. Alcance del estado del arte y propósito de la fundamentación teórica

El análisis se organiza en torno a los dominios que condicionan la viabilidad del sistema: la detección open-vocabulary como alternativa frente a los enfoques de vocabulario cerrado, los modelos visión-lenguaje y sus principales familias arquitectónicas, el seguimiento multiobjeto como mecanismo de persistencia temporal, y las tecnologías de transmisión y procesamiento de vídeo necesarias para operar con baja latencia. De manera complementaria, se consideran las brechas que aparecen al aplicar estas tecnologías al dominio de la construcción civil, especialmente en relación con la detección de condiciones de riesgo, la estabilidad temporal de las predicciones, la sensibilidad a los prompts, la disponibilidad de datos y la evaluación de alertas en tiempo real.

Esta revisión no tiene por finalidad elegir de forma aislada un modelo, protocolo o herramienta, sino establecer un marco crítico para distinguir qué capacidades se encuentran suficientemente maduras, qué aspectos requieren validación experimental y qué limitaciones deben ser consideradas durante el diseño e implementación del prototipo. A partir de esta base se derivan criterios para la selección tecnológica, la definición del alcance experimental y la construcción posterior del protocolo de evaluación.


### 15.2. Detección open-vocabulary: modelos, paradigmas y brechas del estado del arte


#### 15.2.1. Paradigmas Arquitectónicos y Modelos Representativos

El estado del arte en OVD no constituye una solución homogénea, sino que se organiza en familias arquitectónicas con compromisos claramente diferenciados entre expresividad semántica, complejidad computacional y eficiencia temporal. A partir de un relevamiento exhaustivo realizado durante la investigación bibliográfica, se identificaron cuatro paradigmas dominantes, de los cuales se presentan a continuación los aspectos y modelos representativos más relevantes para el contexto de sistemas de video en tiempo real.

El primer paradigma extiende arquitecturas end-to-end basadas en Transformers —derivadas de DETR y DINO (Carion et al., 2020; H. Zhang et al., 2022)— incorporando el lenguaje dentro del proceso de predicción mediante mecanismos explícitos de fusión multimodal. El modelo representativo de esta familia es Grounding DINO (Liu et al., 2023), que introduce una fusión multimodal profunda estructurada en tres componentes: un Feature Enhancer que alinea semánticamente regiones visuales con tokens textuales, un Language-guided Query Selection que inicializa las consultas del decoder condicionadas por el texto y un Cross-modality Decoder que refina cajas y asocia predicciones a fragmentos del prompt mediante atención cruzada. Esta arquitectura resulta especialmente efectiva para expresiones referenciales complejas y frases con atributos, reportando 52.5 AP en COCO en configuración zero-shot (Liu et al., 2023).

Desarrollos posteriores como OmDet-Turbo (Zhao et al., 2024) abordan explícitamente la limitación de latencia de este paradigma mediante un módulo de fusión eficiente que permite reutilizar los embeddings textuales entre cuadros consecutivos, amortizando el costo del procesamiento lingüístico cuando el vocabulario de consulta permanece constante. Esta estrategia es directamente relevante para escenarios de monitoreo continuo, donde el conjunto de condiciones de riesgo se define al inicio de la sesión y se mantiene estable a lo largo del flujo de video.

Un segundo paradigma traslada la detección OVD a arquitecturas one-stage de alta eficiencia, derivadas de la familia YOLO, diseñando la integración visión-lenguaje para minimizar el costo adicional en inferencia. El exponente principal es YOLO-World (Cheng et al., 2024), que introduce un mecanismo de Re-Parameterizable Vision-Language Path Aggregation Network (RepVL-PAN) y un módulo de Cross-Modal Late Interaction (CSAM) para alinear características visuales densas con embeddings textuales durante el entrenamiento. En inferencia, los embeddings textuales pueden reparametrizarse como pesos equivalentes a los de un detector YOLO estándar, eliminando el overhead de la fusión multimodal en tiempo de ejecución. Su sucesor, YOLOE (A. Wang et al., 2025), extiende este principio logrando overhead computacional cero tras la reparametrización, reportando 35.9 AP en LVIS-minival con 102.5 FPS en hardware de inferencia optimizado. Este paradigma prioriza tasas de inferencia elevadas y baja latencia, a cambio de una menor expresividad semántica frente a consultas complejas o con atributos relacionales.

Una tercera familia plantea la detección como una extensión del paradigma de clasificación zero-shot de CLIP, utilizando un encoder visual y un encoder textual que proyectan imagen y texto en un espacio semántico compartido. La clasificación abierta se resuelve mediante puntajes de compatibilidad —producto punto entre embeddings visuales locales y embeddings textuales— en lugar de logits de clase fijos. El representante más relevante es OWL-ViT y su evolución OWLv2 (Minderer et al., 2022, 2024), que escala el entrenamiento mediante auto-entrenamiento sobre datos web a gran escala, generando más de mil millones de ejemplos de entrenamiento mediante pseudo-anotaciones. Esta estrategia mejora significativamente el rendimiento en categorías raras del benchmark LVIS (Gupta et al., 2019).

La ventaja principal de este paradigma es su modularidad, donde cambiar el vocabulario de consulta equivale simplemente a cambiar los prompts, sin modificar la arquitectura del modelo. La limitación principal reside en que el cómputo de embeddings textuales por cada nueva consulta introduce latencia variable, aunque esta puede mitigarse mediante caching cuando el vocabulario permanece estable entre cuadros consecutivos.

Un cuarto paradigma reformula la detección como un problema secuencia-a-secuencia condicionado por instrucciones en lenguaje natural, donde el modelo genera salidas estructuradas —texto que codifica cajas delimitadoras, etiquetas y descripciones— mediante decodificación autoregresiva. El modelo representativo es Florence-2 (Xiao et al., 2023), que unifica múltiples tareas de visión —detección, segmentación, captioning y razonamiento visual— bajo un esquema de prompting generalista, sin necesidad de rediseñar cabezales específicos por tarea. La ventaja de este paradigma es su flexibilidad para abordar condiciones de riesgo que requieren descripciones complejas o ricas en contexto.

La limitación crítica para aplicaciones de video en tiempo real es la dependencia de decodificación autoregresiva, que introduce mayor latencia de inferencia y variabilidad temporal respecto a los paradigmas anteriores. La naturaleza secuencial de la generación impide el paralelismo completo de la inferencia, y la inestabilidad frame-to-frame es más pronunciada en este paradigma que en los enfoques de predicción directa, dado que la variabilidad del proceso generativo se acumula entre cuadros consecutivos (Xiao et al., 2023). Esta característica limita su adecuación para sistemas de monitoreo continuo con requisitos estrictos de latencia E2E.

A continuación, se revisan modelos representativos de cada paradigma, enfocando el análisis en: (i) decisiones arquitectónicas, (ii) mecanismo de fusión/compatibilidad visión–lenguaje, (iii) régimen de entrenamiento y tipo de supervisión, y (iv) resultados en benchmarks estándar (COCO, LVIS), junto con consideraciones prácticas de inferencia relevantes para aplicaciones en vídeo.


##### 15.2.1.1. Bloque A — Detectores End-to-End Tipo DETR/DINO con Fusión Visión–Lenguaje en el Decoder


###### 15.2.1.1.1. GLIP y GLIPv2

Arquitectura base. GLIP (Grounded Language-Image Pre-training) unifica detección y phrase grounding bajo una formulación común: el modelo recibe una imagen y un prompt textual con las categorías o frases de interés. Su implementación se construye sobre un detector tipo Dynamic Head y emplea un backbone visual Swin Transformer, junto con un encoder de texto BERT y un módulo de fusión multimodal profunda (Li et al., 2021).

Mecanismo visión–lenguaje. La contribución central de GLIP es reformular la clasificación cerrada como alineamiento región–palabra/región–frase: en lugar de producir logits de clase fijos, reemplaza el clasificador por puntajes de alineamiento entre features visuales de región y features lingüísticas de tokens. A diferencia de enfoques donde visión y texto solo interactúan al final, GLIP enfatiza fusión profunda para integrar señales lingüísticas dentro del pipeline de detección (Li et al., 2021).

Entrenamiento y supervisión. GLIP escala el preentrenamiento mediante datos de grounding a gran escala, combinando 3 millones de anotaciones humanas y 24 millones de pares imagen–texto web con pseudo-cajas generadas mediante self-training, totalizando 27 millones de ejemplos (Li et al., 2021).

Evolución GLIPv2. GLIPv2 extiende el enfoque hacia un modelo unificado que cubre tareas de localización (detección, segmentación por instancias, grounding) y comprensión visión–lenguaje (VQA, captioning). El preentrenamiento unifica tres tareas: phrase grounding, region–word contrastive learning y masked language modeling (Zhang et al., 2022).

Resultados reportados. GLIP alcanza 49.8 AP en COCO y 26.9 AP en LVIS en evaluación directa zero-shot. Con fine-tuning en COCO, reporta 60.8 AP en val y 61.5 AP en test-dev. GLIPv2-H logra 60.6 AP en COCO test-dev y 59.8 AP (caja) en LVIS-minival (Li et al., 2021; Zhang et al., 2022).


###### 15.2.1.1.2. OV-DETR

Arquitectura base. OV-DETR (Zang et al., 2022) representa un enfoque temprano para llevar la detección end-to-end tipo DETR al escenario open-vocabulary. Parte de Deformable DETR como detector base (Zhu et al., 2020) y utiliza CLIP para representar consultas abiertas en forma de texto o imágenes ejemplares.

Mecanismo visión–lenguaje. El obstáculo central al extender DETR a open-vocabulary es que el entrenamiento estándar usa matching bipartito con un costo de clasificación definido sobre clases conocidas. OV-DETR evita este problema reformulando el aprendizaje como matching condicional binario: dado un concepto (texto o imagen), el modelo aprende a decidir si una predicción corresponde o no a esa consulta, en lugar de resolver una clasificación multiclase cerrada (Zang et al., 2022).

Resultados reportados. OV-DETR alcanza 17.4 AP en clases novedosas en el protocolo OV-LVIS y 29.4 AP50 en categorías novedosas en OV-COCO, demostrando que la formulación condicional permite detectar categorías no vistas con un marco end-to-end (Zang et al., 2022).

Licencia. El código se distribuye bajo licencia CC BY-NC-SA 4.0, lo que restringe el uso comercial (Zang, 2022).


###### 15.2.1.1.3. Grounding DINO

Arquitectura base. Grounding DINO propone un detector open-set construido sobre la línea DETR/DINO, con razonamiento global vía Transformer y diseño explícito para integrar lenguaje durante la predicción. El modelo emplea una arquitectura dual-encoder/single-decoder: un backbone visual (frecuentemente Swin Transformer) extrae características multi-escala y un backbone textual (BERT) codifica el prompt (Liu et al., 2023).

Mecanismo visión–lenguaje. La contribución central es una fusión multimodal profunda basada en atención cruzada en distintas etapas. Grounding DINO divide la fusión en tres componentes: Feature Enhancer (interacciones imagen–texto para alinear semántica y regiones), Language-guided Query Selection (inicializa consultas del decoder condicionadas por texto), y Cross-modality Decoder (agrega atención cruzada con texto para refinar cajas y asociar predicciones a fragmentos del prompt). Esto hace que el modelo sea especialmente efectivo con expresiones referenciales o frases con atributos (Liu et al., 2023).

Resultados reportados. En configuración zero-shot, Grounding DINO reporta 52.5 AP en COCO y un récord de 26.1 mAP promedio en ODinW (Liu et al., 2023).

Evolución Grounding DINO 1.5. La versión 1.5 Pro, orientada a máxima generalización, entrena con Grounding-20M (más de 20 millones de imágenes) y logra 54.3 AP en COCO y 55.7 AP en LVIS-minival en zero-shot transfer. La versión 1.5 Edge, orientada a despliegue eficiente, reporta 75.2 FPS y 36.2 AP en LVIS-minival con TensorRT, y despliegue en NVIDIA Orin NX con más de 10 FPS (Ren et al., 2024b).

Licencia. El repositorio oficial se distribuye bajo licencia Apache-2.0 (IDEA-Research, 2024 -a).


###### 15.2.1.1.4. OV-DINO

Arquitectura base. OV-DINO propone un detector open-vocabulary dentro del paradigma DETR/DINO, orientado a robustecer el preentrenamiento a gran escala y reducir el impacto del ruido típico de las pseudo-anotaciones. La receta se organiza alrededor de dos ideas: unificar fuentes de datos heterogéneas en un formato "detection-centric" y mejorar la fusión multimodal durante la predicción (Wang et al., 2024).

Mecanismo visión–lenguaje. OV-DINO introduce Unified Data Integration (UniDI) para integrar múltiples fuentes mitigando ruido de pseudo-labeling, y Language-Aware Selective Fusion (LASF), un módulo de fusión selectiva guiada por lenguaje para alineación visión–lenguaje más efectiva (Wang et al., 2024).

Resultados reportados. En evaluación zero-shot, OV-DINO reporta 50.6 AP en COCO y 40.1 AP en LVIS-minival (Wang et al., 2024).

Licencia. El repositorio oficial está bajo licencia Apache-2.0 (Wang, 2024).


###### 15.2.1.1.5. DINO-X

Arquitectura base. DINO-X es un modelo unificado y object-centric para detección open-world/open-vocabulary, desarrollado como evolución directa de Grounding DINO 1.5, manteniendo un esquema Transformer encoder–decoder orientado a representaciones a nivel objeto. A diferencia de detectores OV que dependen estrictamente de listas de clases, DINO-X soporta múltiples tipos de prompt: texto, prompts visuales y prompts personalizados (Ren et al., 2024a).

Mecanismo visión–lenguaje. La idea distintiva de DINO-X es combinar flexibilidad de entrada con un mecanismo prompt-free mediante un Universal Object Prompt que permite "detectar cualquier cosa" sin definir clases específicas (Ren et al., 2024a).

Entrenamiento. El trabajo construye y utiliza Grounding-100M, un conjunto con más de 100 millones de muestras de grounding de alta calidad para preentrenamiento (Ren et al., 2024a).

Resultados reportados. DINO-X Pro alcanza 56.0 AP en COCO, 59.8 AP en LVIS-minival y 63.3 AP en clases raras de LVIS-minival, estableciendo un nuevo estado del arte en detección abierta (Ren et al., 2024a).

Licencia. El repositorio público indica licencia Apache-2.0 (IDEA-Research, 2024 -c).


###### 15.2.1.1.6. OmDet-Turbo

Arquitectura base. OmDet-Turbo es un detector open-vocabulary basado en Transformers, diseñado explícitamente para tiempo real. El trabajo identifica cuellos de botella típicos en detectores OV tipo DETR y propone un módulo central llamado Efficient Fusion Head (EFH) que incluye ELA-Encoder (Efficient Language-Aware Encoder) para generar consultas eficientemente y ELA-Decoder que evita operaciones lentas tipo ROIAlign (Zhao et al., 2024).

Caching de embeddings textuales. Un punto clave para vídeo es que, si el vocabulario se mantiene constante a lo largo de una secuencia, OmDet-Turbo permite cachear embeddings textuales evitando recomputar el backbone textual en cada frame, ahorrando aproximadamente 40 ms en la variante Tiny (Zhao et al., 2024).

Resultados reportados. OmDet-Turbo-Base alcanza 53.4 AP en COCO y 34.7 AP en LVIS-minival con 18.6 FPS (PyTorch) y 100.2 FPS (TensorRT) en A100. La variante Tiny alcanza 42.5 AP en COCO con 140.0 FPS (TensorRT), posicionándolo como atractivo cuando el requerimiento dominante es latencia (Zhao et al., 2024).

Licencia. El repositorio oficial se publica bajo licencia Apache-2.0 y está integrado en Hugging Face Transformers (om-ai-lab, 2024.; Hugging Face, 2024).


##### 15.2.1.2. Bloque B: Detectores one-stage tipo YOLO con puntuación región–texto


###### 15.2.1.2.1. YOLO-World

Arquitectura base. YOLO-World adapta un detector one-stage de la familia YOLO al escenario open-vocabulary manteniendo predicción densa y diseño orientado a despliegue. Su contribución arquitectónica central es RepVL-PAN (Re-parameterizable Vision-Language Path Aggregation Network), un neck multiescala que incorpora interacción visión–lenguaje sin abandonar la estructura backbone–PAN–head propia de YOLO (Cheng et al., 2024).

Mecanismo visión–lenguaje. El modelo puntúa regiones mediante similitud en un espacio compartido región–texto. RepVL-PAN implementa esta interacción con Text-guided CSPLayer para inyectar guía textual en las features visuales e Image Pooling Attention para enriquecer embeddings textuales con contexto visual. En despliegue, YOLO-World opera con vocabulario offline y habilita una reparametrización que permite prescindir del encoder textual durante inferencia (Cheng et al., 2024).

Resultados reportados. YOLO-World-L reporta 35.4 AP en LVIS-minival con 52.0 FPS en NVIDIA V100 (sin TensorRT), mostrando un punto de operación competitivo para aplicaciones con restricción de latencia (Cheng et al., 2024).

Licencia. El repositorio declara licencia GPL-3.0, con posibilidad de gestionar licencia alternativa para uso comercial (AILab-CVC, 2024).


###### 15.2.1.2.2. YOLOE

Arquitectura base. YOLOE, presentado como "Real-Time Seeing Anything", propone un modelo one-stage que unifica detección y segmentación manteniendo el esquema backbone–PAN–heads típico de YOLO. Sus módulos de alineamiento se diseñan para que, tras reparametrización, el grafo de inferencia quede equivalente al de un YOLO cerrado (Wang et al., 2025).

Mecanismo visión–lenguaje. YOLOE integra tres modalidades: prompts de texto mediante RepRTA (Re-parameterizable Region-Text Alignment), prompts visuales mediante SAVPE (Semantic-Activated Visual Prompt Encoder), y modo prompt-free mediante LRPC (Lazy Region-Prompt Contrast) que reformula la asignación como retrieval evitando dependencia de modelos de lenguaje en inferencia (Wang et al., 2025).

Resultados reportados. En LVIS-minival zero-shot, YOLOE-v8-S reporta 27.9 AP con 305.8 FPS (NVIDIA T4, TensorRT) y YOLOE-v8-L alcanza 35.9 AP con 102.5 FPS, superando a YOLO-Worldv2-S por +3.5 AP con mayor velocidad (Wang et al., 2025).

Licencia. El repositorio declara licencia AGPL-3.0, lo que introduce requisitos copyleft que pueden condicionar adopción en integraciones propietarias (THU-MIG, 2025).


##### 15.2.1.3. Bloque C: Detectores Basados en Dual-Encoders (CLIP-like) y Matching por Similitud


###### 15.2.1.3.1. OWL-ViT y OWLv2

Arquitectura base. OWL-ViT propone una receta directa para llevar modelos visión–lenguaje a detección open-vocabulary usando un Vision Transformer (ViT) encoder-only con modificaciones mínimas. Se mantienen los tokens espaciales y se agregan cabezales livianos que predicen, por token, una caja y un embedding de compatibilidad. La clasificación abierta se logra reemplazando un clasificador cerrado por embeddings derivados del texto (Minderer et al., 2022).

Entrenamiento. OWLv2 escala mediante self-training (OWL-ST): usa un modelo OWL-ViT como annotator para generar pseudo-cajas sobre datos web a gran escala (WebLI). OWLv2 introduce mejoras de eficiencia de entrenamiento: un objectness head para entrenar pérdidas solo sobre un subconjunto de tokens más plausibles como objeto, y token dropping durante entrenamiento (Minderer et al., 2023).

Resultados reportados. OWL-ViT L/14 alcanza 34.6 AP y 31.2 AP en clases raras en LVIS. OWLv2 L/14 con OWL-ST reporta 44.6 AP en clases raras zero-shot en LVIS-val, y la variante G/14 alcanza 47.2 AP en clases raras (Minderer et al., 2022, 2023).

Licencia. Los pesos se distribuyen bajo Apache-2.0 (Google, 2022; Google, 2023).


###### 15.2.1.3.2. Detic

Arquitectura base. Detic ("Detecting Twenty-thousand Classes using Image-level Supervision") aborda la detección open-vocabulary desde un enfoque two-stage clásico (RPN y ROI head), planteando que en escenarios de gran vocabulario el cuello de botella no suele ser la generación de propuestas sino la clasificación de regiones (Zhou et al., 2022a).

Mecanismo visión–lenguaje. En configuración open-vocabulary, Detic reemplaza el clasificador cerrado por un esquema de matching: las features de región se puntúan contra embeddings lingüísticos de los nombres de clase usando embeddings de CLIP como pesos del clasificador (Zhou et al., 2022a).

Entrenamiento. El rasgo distintivo es cómo incorpora supervisión débil (labels a nivel imagen) para expandir el vocabulario. Su receta mezcla minibatches de datos con cajas y datos con etiquetas a nivel imagen, donde supervisa la clasificación usando la propuesta de mayor tamaño como proxy de objeto. Utiliza datasets de clasificación a gran escala (ImageNet-21K) para escalar hacia decenas de miles de conceptos (Zhou et al., 2022a).

Resultados reportados. En OV-LVIS, Detic reporta 26.8 mask mAP y 17.8 AP en clases raras. En OV-COCO alcanza 45.0 mAP50 (all) y 27.8 en categorías novel. Detic suele usarse como baseline fuerte para vocabularios grandes, aunque su naturaleza two-stage lo ubica lejos de objetivos de tiempo real (Zhou et al., 2022a).

Licencia. El repositorio indica licencia Apache-2.0 (Zhou, s.f.).


###### 15.2.1.3.3. Familia DetCLIP

Arquitectura base. La familia DetCLIP se centra en escalar el aprendizaje open-vocabulary mediante preentrenamiento que integra datos heterogéneos (detección/grounding/imagen–texto) con mecanismos que refuerzan la semántica lingüística. DetCLIP se apoya en un detector tipo ATSS con backbone Swin y expansión semántica mediante un diccionario de conceptos (Yao et al., 2022).

Evolución. DetCLIPv2 reformula el objetivo hacia alineamiento fino palabra–región aprendido end-to-end directamente desde pares imagen–texto, sin depender de teachers CLIP congelados (Yao et al., 2023). DetCLIPv3 empuja el paradigma hacia detección más generativa incorporando un cabezal de captioning para etiquetas jerárquicas (Yao et al., 2024).

Resultados reportados. DetCLIP reporta 35.9 AP en LVIS (Swin-T). DetCLIPv2 alcanza 40.4 AP (Swin-T) y 44.7 AP (Swin-L) en LVIS-minival. DetCLIPv3 reporta 48.8 AP en LVIS-minival (Swin-L) y 49.9 AP en categorías raras (Yao et al., 2022, 2023, 2024).


##### 15.2.1.4. Bloque D: Modelos generativos guiados por instrucciones


###### 15.2.1.4.1. APE (Aligning and Prompting Everything)

Paradigma y tipo de consulta. APE se ubica en la línea de prompting generalista guiado por lenguaje: el mismo modelo puede ejecutarse como detección/segmentación open-vocabulary y como grounding a partir de listas grandes de categorías y/o descripciones en lenguaje natural. Aunque es guiado por prompts, APE no depende de decodificación autoregresiva, produciendo predicciones estructuradas de manera directa (Shen et al., 2023).

Arquitectura base. APE se construye sobre un pipeline tipo DETR (encoder–decoder Transformer) y combina vision backbone (ViT), modelo de lenguaje para embeddings de prompts, cross-modality encoder para fusionar texto–imagen, y decoder que produce predicciones a nivel objeto. Soporta salidas de detección (cajas) y segmentación (máscaras) (Shen et al., 2023).

Mecanismo visión–lenguaje. El núcleo de APE es alinear instancias con texto mediante una formulación unificada: cada prompt se procesa de forma independiente y el modelo calcula puntajes de alineamiento mediante producto punto. Para escalar a miles de categorías sin costo prohibitivo, APE introduce una interacción cross-modal "gated" que puede simplificarse para vocabularios grandes (Shen et al., 2023).

Resultados reportados. APE-L (D) reporta 59.6 AP (caja) y 53.0 AP (máscara) en LVIS, y 58.3 AP (caja) en COCO con un solo conjunto de pesos. En suites "in the wild", reporta 64.7 en Roboflow100 y 57.9 en ODinW-13 (Shen et al., 2023).

Licencia. El repositorio declara licencia Apache-2.0 (Shen, s.f.).


###### 15.2.1.4.2. Florence-2

Paradigma y tipo de consulta. Florence-2 se enmarca en el paradigma generativo guiado por instrucciones: interpreta un prompt textual de tarea (por ejemplo, "object detection", "dense caption", "OCR") y genera una salida en texto que se post-procesa para recuperar cajas, etiquetas u otras estructuras. Opera con task tokens y puede combinarse con texto adicional (Xiao et al., 2024).

Arquitectura base. Florence-2 adopta una formulación sequence-to-sequence con un Transformer encoder–decoder multimodal. El input combina tokens visuales producidos por un encoder de visión DaViT (Dual Attention Vision Transformer) y embeddings del prompt de tarea. Para representar salida espacial, el modelo amplía el vocabulario con tokens de localización cuantizados usando 1000 bins (Xiao et al., 2023; Ding et al., 2022).

Entrenamiento. El modelo se preentrena sobre FLD-5B, un dataset con 126 millones de imágenes y más de 5 mil millones de anotaciones desglosadas como 500 millones de anotaciones de texto, 1.3 mil millones de anotaciones región–texto y 3.6 mil millones de anotaciones texto–frase–región (Xiao et al., 2023).

Resultados reportados. En zero-shot, Florence-2-L (0.77B parámetros) reporta 37.5 mAP en COCO Det y 135.6 CIDEr en COCO Caption. Tras fine-tuning multitarea, alcanza 43.4 mAP en COCO Det y 93.4 Accuracy@0.5 en RefCOCO (Xiao et al., 2023).

Implicaciones para vídeo. Un solo modelo puede cubrir detección, grounding, captioning y OCR, útil para prototipado rápido. Sin embargo, al ser autoregresivo, el costo de inferencia y la latencia tienden a ser más altos y variables, y en vídeo esa variabilidad suele traducirse en inestabilidad temporal si no se complementa con tracking (Xiao et al., 2023).

Licencia. Los pesos publicados para Florence-2-large indican licencia MIT (Microsoft, 2024).


###### 15.2.1.4.3. LLMDet

Paradigma y tipo de consulta. LLMDet se ubica en una línea híbrida: incorpora señales generativas y conocimiento lingüístico de un LLM durante el entrenamiento, pero en inferencia opera como un detector open-vocabulary convencional sin LLM. El tipo de consulta en despliegue es el habitual: lista de clases y/o frases (Fu et al., 2025).

Arquitectura base. El trabajo toma como detector base MM Grounding DINO y añade un proyector que mapea features visuales al espacio de entrada del LLM, y un LLM que recibe features globales y por región para generar texto durante entrenamiento. El LLM se descarta en inferencia, eliminando overhead en producción (Fu et al., 2025).

Entrenamiento. Se construye el conjunto GroundingCap-1M, en el cual cada muestra incluye una imagen, texto de grounding, cajas asociadas a frases y un caption largo. El entrenamiento combina la pérdida de grounding del detector con pérdidas de language modeling, orientadas tanto a la generación de captions largos a nivel de imagen como de descripciones cortas a nivel de región. La incorporación de captions largos contribuye a mejorar el desempeño en clases raras y escenarios de long-tail (Fu et al., 2025).

Resultados reportados. Con Swin-L, LLMDet reporta 51.1 AP en LVIS-minival y 42.0 AP en LVIS-val, con mejoras marcadas en clases raras. También reportan mejoras en ODinW y robustez ante shift de distribución en COCO-O (Fu et al., 2025).

Licencia. El repositorio indica licencia Apache-2.0 (iSEE-Laboratory, 2025).


###### 15.2.1.4.4. T-Rex2

Paradigma y tipo de consulta. T-Rex2 entra en el Bloque D por su foco en prompting generalista multimodal: soporta prompts de texto, prompts visuales y prompts combinados, distinguiendo flujos interactivos (refinables) y genéricos (visual prompts reutilizables) (Jiang et al., 2024).

Arquitectura base. El paper plantea un modelo práctico de open-set object detection que explota la complementariedad: texto abstrae bien objetos comunes, mientras los prompts visuales representan mejor objetos raros o difíciles de describir. Su contribución de ingeniería clave es una fusión tardía que permite iterar/refinar prompts sin recalcular el encoder de imagen múltiples veces (Jiang et al., 2024).

Entrenamiento. El paper reporta entrenamiento diferenciado para texto y visual prompts con mezcla de datos etiquetados y pseudo-etiquetas, incluyendo self-training sobre SA-1B para visual prompts y cyclical training alternando texto/visual (Jiang et al., 2024).

Resultados reportados. Con Swin-L, T-Rex2 alcanza 46.7 AP en LVIS-minival (texto) y 46.8 AP (visual-genérico), además de números competitivos en ODinW y Roboflow100. El trabajo muestra que el texto gana en categorías frecuentes mientras que el visual gana en muchas categorías raras (Jiang et al., 2024).

Implicación para vídeo. T-Rex2 es interesante por permitir anclar la detección a un ejemplo visual (útil para seguimiento) y por fusión tardía que favorece flujos interactivos sin multiplicar el costo del encoder visual (Jiang et al., 2024).


##### 15.2.1.5. Bloque E — Pipelines, segmentación y despliegue (extensiones prácticas)


###### 15.2.1.5.1. Grounded SAM y Grounded SAM 2

Paradigma. Grounded SAM es representativo de una estrategia de pipeline (ensamblado de modelos foundation) más que de una arquitectura monolítica: resuelve segmentación open-vocabulary descomponiéndola en grounding/detección condicionado por texto y segmentación guiada condicionada por cajas/puntos (Ren et al., 2024c).

Arquitectura base. El pipeline estándar es: 1) Grounding DINO, 2) cajas (condicionadas por prompt textual) y luego 3) SAM con máscaras usando esas cajas como box prompts. SAM por sí solo no "entiende" texto; Grounded SAM lo vuelve text-promptable delegando la parte semántica al detector open-set (Kirillov et al., 2023; Ren et al., 2024c).

Evolución Grounded SAM 2. Grounded SAM 2 actualiza el componente de segmentación a SAM 2 (que soporta imagen y vídeo) y agrega demos de "ground & track". El repositorio soporta varios grounders (Grounding DINO, Florence-2, DINO-X) combinables con SAM 2 para segmentación y tracking (IDEA-Research, 2024 -b; Ravi et al., 2024).

Resultados reportados. Grounded SAM reporta 48.7 mean AP en SegInW con Grounding DINO-Base + SAM-Huge (Ren et al., 2024c).

Valor práctico. El pipeline es ideal para auto-anotación y análisis donde la segmentación precisa vale más que la latencia. En vídeo, Grounded SAM 2 empuja hacia ground & track con SAM 2, aunque el costo de encadenar modelos grandes no es el camino natural al tiempo real estricto (Ren et al., 2024c).

Licencia. Grounded-Segment-Anything se distribuye bajo Apache-2.0; Grounded-SAM-2 incluye componentes bajo Apache-2.0 y BSD-3-Clause (IDEA-Research, 2023; IDEA-Research, 2024 -b).


###### 15.2.1.5.2. OVTrack

Paradigma. OVTrack formaliza open-vocabulary multiple object tracking (MOT) como un problema donde, en test, el sistema recibe una lista de clases de interés (base + novel) y debe detectar y asociar instancias a lo largo del tiempo. La evaluación permite medir precisión/recobrado y calidad de clasificación para clases no vistas durante entrenamiento (Li et al., 2023).

Arquitectura base. OVTrack sigue el paradigma tracking-by-detection: localizador agnóstico a clase basado en Faster R-CNN para proponer cajas por frame, cabezas de embeddings (texto e imagen) para reemplazar el clasificador cerrado por un mecanismo abierto, y head de tracking que produce embedding de apariencia y realiza asociación mediante memoria de tracks (Li et al., 2023).

Entrenamiento. OVTrack entrena el tracker usando sólo imágenes estáticas (LVIS), evitando dependencia de grandes datasets de vídeo etiquetados. Para aprender apariencia útil en tracking sin vídeo real, introduce data hallucination con modelos de difusión (DDPM) para sintetizar pares de instancias positivas/negativas (Li et al., 2023).

Resultados reportados. En TAO open-vocabulary, OVTrack obtiene TETA 35.5 (base) y 27.8 (novel) en validation, y TETA 32.6 (base) y 24.1 (novel) en test (Li et al., 2022, 2023).

Implicaciones para despliegue. El embedding textual del vocabulario puede precalcularse/cachearse si la lista de clases se mantiene fija. Al depender de un detector two-stage por frame más asociación por embeddings, no está pensado como solución real-time end-to-end, sino como baseline fuerte y medible para escenarios abiertos y long-tail (Li et al., 2023).

Licencia. El repositorio reporta licencia Apache-2.0 (SysCV, 2023).


###### 15.2.1.5.3. Roboflow Rapid

Paradigma. Roboflow Rapid no es un modelo OVD en sentido estricto de inferencia con vocabulario abierto, sino un pipeline de operacionalización: parte de una consulta en lenguaje natural y/o ejemplos para auto-etiquetar, entrenar y desplegar rápidamente un detector funcional. El lenguaje se usa principalmente para definir el concepto y generar etiquetas, mientras que el modelo final opera como detector especialista (Deschere, 2025).

Arquitectura del sistema. Rapid implementa un flujo de extremo a extremo: ingesta de imágenes o vídeo, etiquetado asistido por prompt, entrenamiento de un modelo RF-DETR custom, y despliegue automático vía Roboflow Serverless API (Robicheaux et al., 2025; Roboflow, 2025a, 2025b).

Implicaciones prácticas. Rapid es útil para acelerar baselines y datasets, pero no reemplaza un OVD "real" cuando el requisito es cambiar vocabulario en tiempo de ejecución sin reentrenar. El modelo final se comporta más como cerrado/dominio-específico que como vocabulario abierto en tiempo de ejecución (Roboflow, 2025a).

Licencia. Rapid es un producto/plataforma sujeto a condiciones del servicio. RF-DETR (arquitectura base) se publica como open-source bajo Apache-2.0 (Robicheaux et al., 2025; Robinson et al., 2025).


#### 15.2.2. Composición de Modelos y Pipelines de Percepción

Los paradigmas arquitectónicos analizados en la sección 15.2.1 comparten un supuesto implícito: el modelo de detección opera como un componente autosuficiente que recibe una imagen y produce un conjunto de cajas delimitadoras con puntajes de compatibilidad semántica. Sin embargo, la experiencia acumulada en la literatura y en los ecosistemas de despliegue muestra que, en la práctica, los modelos OVD rara vez operan de manera aislada. Del análisis realizado, se identifican enfoques composicionales que integran capacidades complementarias —detección, segmentación de instancias y seguimiento temporal— para abordar tareas que exceden el alcance de un detector individual (Ren et al., 2024). Esta observación es relevante para el marco teórico del proyecto porque introduce una dimensión de diseño que no se reduce a la selección de un modelo, sino a la articulación de capacidades en una arquitectura de percepción.

El exponente más representativo de este enfoque composicional es Grounded SAM (Ren et al., 2024), un pipeline que descompone la segmentación open-vocabulary en dos etapas encadenadas: primero, un detector condicionado por texto —típicamente Grounding DINO (Liu et al., 2023)— genera cajas delimitadoras asociadas a las descripciones del prompt; luego, un modelo de segmentación universal —SAM, Segment Anything Model (Kirillov et al., 2023)— produce máscaras de instancia precisas utilizando esas cajas como señal de localización. El diseño es deliberadamente modular: SAM por sí solo carece de comprensión semántica, y Grounding DINO por sí solo no produce segmentación; es la composición la que habilita una capacidad que ninguno de los componentes posee individualmente. Esta arquitectura composicional introduce un compromiso explícito. Por un lado, la modularidad permite sustituir componentes de manera independiente —reemplazar el detector, actualizar el segmentador o intercalar etapas de procesamiento— sin rediseñar el pipeline completo. Por otro lado, la ejecución secuencial de múltiples modelos foundation acumula latencia y consumo de recursos, lo que limita su aplicabilidad directa en escenarios de video en tiempo real con requisitos estrictos de latencia extremo a extremo. Esta tensión entre modularidad y eficiencia es inherente al patrón composicional y debe considerarse como un factor de diseño en la evaluación de alternativas para etapas posteriores.

La evolución hacia Grounded SAM 2 (Ravi et al., 2024) extiende el pipeline al dominio temporal, incorporando SAM 2 como componente de segmentación capaz de operar tanto sobre imágenes estáticas como sobre secuencias de video, habilitando funcionalidades de segmentación y seguimiento combinados (ground and track).

Paralelamente, trabajos como OVTrack (S. Li et al., 2023) formalizan el problema del seguimiento multi-objeto en vocabulario abierto (open-vocabulary MOT), donde el sistema debe detectar y asociar temporalmente instancias de clases tanto conocidas como no vistas durante el entrenamiento. OVTrack adopta el paradigma tracking-by-detection con un localizador agnóstico a clase y cabezas de embeddings textuales y visuales para clasificación abierta, entrenando exclusivamente sobre imágenes estáticas mediante técnicas de data hallucination con modelos de difusión para sintetizar pares de apariencia (S. Li et al., 2023). Si bien el análisis detallado de los mecanismos de seguimiento temporal se desarrolla en la sección 15.3, la existencia de OVTrack como marco formalizado refuerza la observación de que la OVD se concibe cada vez más como un componente dentro de un sistema de percepción más amplio, no como una solución terminal.

La implicación de esta tendencia es que, en la práctica industrial y en la literatura reciente, los sistemas de percepción basados en OVD no se despliegan como detectores aislados, sino como cadenas de procesamiento donde la detección semántica constituye una etapa dentro de un flujo más amplio que típicamente incluye preprocesamiento de la señal visual, segmentación, seguimiento temporal y generación de eventos o alertas (S. Li et al., 2023; Ren et al., 2024). Esta observación refuerza que la evaluación de modelos OVD no puede limitarse a métricas de precisión aisladas, sino que debe considerar la integrabilidad de cada componente dentro de pipelines compuestos, incluyendo factores como la compatibilidad de formatos de entrada y salida entre etapas, el overhead acumulado por la ejecución secuencial de modelos y la estabilidad temporal de las predicciones a lo largo del flujo.


#### 15.2.3. Síntesis Comparativa y Trade-Offs para Tiempo Real

La Tabla 2 sintetiza las características fundamentales de los cuatro paradigmas arquitectónicos analizados, con énfasis en las dimensiones más relevantes para la viabilidad del sistema E-OVRT-VDP en un contexto de vídeo en tiempo real.

Tabla 2

Síntesis comparativa de paradigmas arquitectónicos OVD según dimensiones relevantes para sistemas de video en tiempo real


| Paradigma | Modelo(s) representativos | Mecanismo visión-lenguaje | Fortaleza principal | Limitación para tiempo real |
| --- | --- | --- | --- | --- |
| DETR/DINO + fusión profunda | Grounding DINO, OV-DINO, OmDet-Turbo, DINO-X | Fusión multimodal en decoder mediante atención cruzada visión-lenguaje | Alta precisión semántica; manejo de expresiones referenciales complejas | Costo computacional elevado; requiere optimización explícita para tiempo real |
| One-stage YOLO + puntuación región-texto | YOLO-World, YOLOE | Alineamiento región-texto reparametrizable; reducción progresiva del overhead de fusión mediante reparametrización | Alta velocidad de inferencia; compatible con hardware de borde | Menor expresividad semántica frente a consultas complejas o con atributos compuestos |
| Dual-encoder CLIP-like + matching por similitud | OWL-ViT, OWLv2, DetCLIP | Matching por similitud en espacio de embeddings compartido; reutilización directa de preentrenamiento contrastivo | Modularidad; cambio de vocabulario sin modificar el modelo | latencia variable según tamaño del vocabulario; requiere caching para vocabularios estables; requiere cómputo de embeddings por consulta |
| Generativo guiado por instrucciones | Florence-2, APE | Florence-2: decodificación autoregresiva seq2seq condicionada por instrucciones; APE: predicción directa con alineamiento por producto punto (Xiao et al., 2023; Shen et al., 2023) | Flexibilidad multitarea; soporte para prompts complejos y multimodales | Florence-2: latencia de inferencia variable e inestabilidad temporal por decodificación autoregresiva; APE: costo de prompting masivo escalable pero sin garantías de tiempo real estricto |

Nota. La columna “Limitación para tiempo real” describe el principal factor restrictivo de cada paradigma en escenarios de monitoreo continuo. Los modelos listados son representativos de cada familia; no constituyen una lista exhaustiva. Las métricas de velocidad son contextuales al hardware y configuración de inferencia reportados en la literatura primaria. Fuente: Elaboración propia basada en las fuentes mencionadas (Cheng et al., 2024; Liu et al., 2023; Minderer et al., 2022, 2024; A. Wang et al., 2025; Xiao et al., 2023).

Como complemento a esta síntesis por paradigmas, en la Tabla A.1 del Anexo A se incluye una matriz ampliada orientada a prototipado, donde se comparan modelos representativos según familia arquitectónica, mecanismo visión-lenguaje, métricas reportadas, rendimiento y licenciamiento. Dicha matriz conserva el detalle técnico necesario para respaldar la selección posterior de alternativas, sin sobrecargar el cuerpo principal del estado del arte.

Del análisis comparativo emergen tres tensiones técnicas que deben considerarse explícitamente como criterios orientadores para la selección tecnológica en etapas posteriores. La primera es la tensión entre precisión semántica y latencia de inferencia, ya que los modelos con fusión visión-lenguaje más profunda logran mayor robustez frente a consultas complejas, pero a un costo computacional que puede comprometer la tasa de frames procesados. La segunda es la tensión entre generalización zero-shot y especialización de dominio, cuya cuestión principal reside en que los benchmarks estándar sobre los que se reportan los resultados no representan las condiciones visuales de una obra civil, por lo que el desempeño reportado en la literatura no es directamente transferible al dominio objetivo. Esta tensión adquiere una dimensión adicional cuando se considera la posibilidad de adaptación de dominio mediante fine-tuning. El análisis detallado realizado anteriormente refleja que la capacidad de preservar la generalización open-vocabulary durante el ajuste de pesos varía sustancialmente entre familias arquitectónicas. Los detectores con fusión visión-lenguaje profunda y no removible, como Grounding DINO, exhiben mayor resiliencia, mientras que los detectores con módulos de texto reparametrizables, como YOLO-World y YOLOE, tienden a converger hacia un comportamiento closed-set bajo las configuraciones estándar de fine-tuning (Cheng et al., 2024; X. Zhao et al., 2024). Esta diferenciación entre arquitecturas constituye un factor relevante para la selección de modelos cuando se anticipa la necesidad de adaptación al dominio de la construcción civil. La tercera es la tensión entre expresividad semántica y simplicidad del prompt: consultas más precisas requieren mayor cuidado en la formulación, introduciendo una variable de diseño que no existe en sistemas closed-set.

Una observación transversal del análisis es que la reutilización de embeddings textuales entre cuadros consecutivos —cuando el vocabulario de consulta permanece estable— constituye la estrategia más relevante para aproximar la inferencia OVD a los requisitos de tiempo real, independientemente del paradigma arquitectónico adoptado (A. Wang et al., 2025; Zhao et al., 2024). Es en este contexto donde el conjunto de condiciones de riesgo se define al inicio de la sesión y se mantiene constante, esta estrategia es directamente aplicable y puede reducir significativamente el overhead de la fusión multimodal.

Adicionalmente, la tendencia hacia pipelines composicionales descrita en esta sección introduce una cuarta tensión que opera en un plano distinto a las anteriores: la tensión entre modularidad e integrabilidad. Los enfoques que ensamblan múltiples modelos foundation —como la combinación de un detector OVD con un segmentador universal— ofrecen mayor flexibilidad para sustituir componentes y abordar tareas compuestas, pero acumulan latencia de inferencia por la ejecución secuencial de etapas y aumentan la complejidad de integración entre formatos de entrada y salida. Esta tensión no invalida el patrón composicional, pero señala que la evaluación de alternativas en etapas posteriores deberá considerar no solo el rendimiento de cada modelo de forma aislada, sino el costo total del pipeline resultante bajo las restricciones temporales del escenario de aplicación.


##### 15.2.3.1. Análisis de Rendimiento para Tiempo Real

Desde el punto de vista del desempeño temporal, varios de los modelos analizados presentan características compatibles con aplicaciones de análisis de vídeo en tiempo real. La Tabla 3 resume el rendimiento reportado por los modelos más representativos, considerando distintos compromisos entre velocidad de inferencia, precisión en benchmarks open-vocabulary y viabilidad de despliegue sobre hardware acelerado.

Tabla 3

Análisis comparativo de rendimiento de modelos OVD para tiempo real


| Modelo | Hardware | Framework | FPS | Latencia | LVIS AP |
| --- | --- | --- | --- | --- | --- |
| YOLOE-v8-S | T4 | TensorRT | 305.8 | 3.3 ms | 27.9 |
| OmDet-Turbo-Tiny | A100 | TensorRT | 140.0 | 7.1 ms | 30.3 |
| YOLOE-v8-L | T4 | TensorRT | 102.5 | 9.8 ms | 35.9 |
| OmDet-Turbo-Base | A100 | TensorRT | 100.2 | 10 ms | 34.7 |
| G-DINO 1.5 Edge | A100 | TensorRT | 75.2 | 13.3 ms | 36.2 |
| YOLO-World-L | V100 | PyTorch | 52.0 | 19.2 ms | 35.4 |

Nota: Los valores de FPS, latencia y AP reportados provienen de los trabajos originales y no siempre fueron obtenidos bajo condiciones idénticas de hardware, resolución, batch size o framework. En consecuencia, deben interpretarse como indicativos y comparativos, no como benchmarks estrictamente normalizados. Fuente: elaboración propia basada en Wang et al. (2025), Zhao et al. (2024), Ren et al. (2024b) y Cheng et al. (2024).


#### 15.2.4. Ventajas, Limitaciones y Trade-Offs Observables

El análisis de arquitecturas y modelos de detección open-vocabulary pone de manifiesto que no existe una solución dominante que optimice simultáneamente precisión semántica, latencia, robustez open-set y facilidad de despliegue. En la práctica, cada enfoque introduce compromisos específicos que deben evaluarse en función del contexto de aplicación, particularmente cuando el objetivo es el análisis de video en tiempo real.


##### 15.2.4.1. Eficiencia y Latencia

Los modelos que declaran soporte para escenarios de tiempo real suelen apoyarse en dos estrategias principales. La primera consiste en reducir el costo de la fusión multimodal, ya sea limitando el uso de atención cruzada profunda o reparametrizando la influencia del lenguaje para preservar el paralelismo de la inferencia (Zhao et al., 2024). La segunda se basa en el caching de embeddings textuales, especialmente relevante en flujos de video donde el vocabulario permanece constante durante intervalos prolongados.

En este sentido, enfoques como OmDet-Turbo hacen explícita esta línea de diseño, permitiendo amortizar el costo del procesamiento lingüístico a lo largo de múltiples cuadros (T. Zhao et al., 2024). De forma complementaria, variantes optimizadas como Grounding DINO 1.5 Edge formalizan una orientación específica a despliegues acelerados, reportando métricas concretas de FPS bajo inferencia optimizada con TensorRT (Ren et al., 2024b). YOLOE representa el avance más significativo al lograr overhead cero después de reparametrización, igualando exactamente la velocidad de detectores YOLO estándar (Wang et al., 2025).


##### 15.2.4.2. Generalización Semántica y Robustez Open-Set

Desde el punto de vista de la generalización, los modelos con fusión visión-lenguaje profunda tienden a mostrar mayor robustez frente a conceptos no vistos y descripciones complejas. Grounding DINO enfatiza una integración estrecha entre lenguaje y visión, con evaluaciones explícitas en benchmarks como COCO, LVIS y ODinW (Liu et al., 2023). DINO-X alcanza 63.3 AP en categorías raras de LVIS, demostrando capacidad excepcional para el long-tail semántico (Ren et al., 2024a).

Enfoques como OV-DINO introducen mecanismos adicionales para reducir el ruido asociado al pseudo-etiquetado y mejorar la alineación selectiva guiada por lenguaje (Wang et al., 2024). LLMDet demuestra que la integración de conocimiento lingüístico externo vía un LLM puede llevar la detección open-vocab a niveles de precisión sin precedentes, aunque con arquitectura compleja y alta demanda computacional (Fu et al., 2025).


##### 15.2.4.3. Licencias y Riesgo de Adopción

Un aspecto frecuentemente subestimado en el análisis técnico, pero crucial para prototipos con proyección, es el régimen de licenciamiento. YOLO-World y YOLOE presentan casos paradigmáticos: ofrecen combinaciones muy competitivas de velocidad y precisión open-vocabulary, pero sus licencias GPLv3 y AGPL-3.0 respectivamente introducen restricciones relevantes para usos comerciales o integraciones cerradas (Cheng et al., 2024; Wang et al., 2025). De forma similar, OV-DETR bajo CC BY-NC-SA 4.0 limita explícitamente su uso fuera del ámbito académico (Zang et al., 2022). En contraste, modelos como Grounding DINO, OmDet-Turbo, LLMDet y varios checkpoints modernos se alinean con licencias permisivas como Apache-2.0 o MIT, reduciendo la fricción legal y simplificando su incorporación en prototipos experimentales con potencial de evolución futura.

En el contexto del presente trabajo, las consideraciones de licenciamiento no constituyen un condicionante operativo. El proyecto se desarrolla con fines estrictamente académicos y experimentales, sin orientación a explotación comercial ni a integración en productos cerrados.


##### 15.2.4.4. Integración de Segmentación y Seguimiento

Una tendencia emergente es combinar detección OVD con segmentación de instancias y seguimiento temporal. Grounded SAM ilustra esta integración: al acoplar un detector open-vocabulary con un segmentador universal, es posible localizar y segmentar cualquier región indicada por texto (Ren et al., 2024c). La extensión Grounded SAM 2 demuestra que es factible incorporar un módulo de tracking para seguir objetos segmentados a lo largo de un vídeo.

X-Decoder (Zou et al., 2023) explora un enfoque unificado con un decodificador capaz de producir tanto máscaras píxel a píxel como descripciones textuales, logrando estado del arte en segmentación open-vocabulary y segmentación referencial. YOLOE integra capacidad de segmentación directamente en la arquitectura, añadiendo una rama de máscara con mínima sobrecarga (Wang et al., 2025).


##### 15.2.4.5. Adaptabilidad Mediante Fine-Tuning y Preservación de Capacidad Open-Vocabulary

Las secciones precedentes evaluaron los modelos OVD en su modalidad zero-shot, es decir, utilizando exclusivamente los pesos obtenidos durante el preentrenamiento a gran escala. Sin embargo, la literatura reciente documenta de manera creciente el comportamiento de estas arquitecturas cuando se someten a fine-tuning sobre datasets de dominio específico, revelando un compromiso fundamental que no se manifiesta en los detectores closed-set convencionales. En un detector tradicional, el fine-tuning mejora el rendimiento en las categorías del dataset objetivo sin costo conceptual adicional. En un modelo OVD, el ajuste de los pesos puede degradar la capacidad de generalización semántica que constituye la propiedad distintiva de estos sistemas, fenómeno conocido en la literatura de modelos foundation como olvido catastrófico o catastrophic forgetting (Kirkpatrick et al., 2017). La intensidad de esta degradación varía significativamente según la profundidad de la fusión visión-lenguaje en la arquitectura, las capas que se ajustan y la estrategia de entrenamiento empleada.

Es por ello que a continuación se analizará la evidencia disponible para cada familia arquitectónica identificada anteriormente, con foco en las estrategias de fine-tuning documentadas, su efecto sobre la capacidad OVD residual y las implicancias para la selección de modelos en el proyecto.

Bloque A: Detectores end-to-end tipo DETR/DINO con fusión profunda. Grounding DINO (Liu et al., 2023) presenta la arquitectura más favorable para preservar capacidad OVD durante el fine-tuning, debido a que la integración del lenguaje ocurre en múltiples etapas del detector (Feature Enhancer, Language-guided Query Selection y Cross-modality Decoder) y no puede removerse sin destruir la funcionalidad del modelo. Los estudios de ablación muestran que la eliminación de cualquier componente de fusión reduce el AP zero-shot en más de 12 puntos, mientras que el impacto sobre el rendimiento en fine-tuning closed-set es mínimo, lo que indica que la maquinaria de fusión multimodal es esencial específicamente para la generalización open-set (Liu et al., 2023).

El proyecto MM-Grounding-DINO (X. Zhao et al., 2024) implementó y comparó tres estrategias de fine-tuning sobre la arquitectura Grounding DINO, ofreciendo la evaluación más completa disponible hasta el momento. La primera estrategia, denominada fine-tuning closed-set, optimiza el modelo directamente sobre el dataset objetivo y restringe el vocabulario textual a las categorías del dataset tras el ajuste, eliminando la capacidad OVD. La segunda, denominada preentrenamiento continuado open-set, reduce el learning rate y congela módulos específicos mientras continúa el entrenamiento sobre el dataset objetivo, o combina el dataset objetivo con datos de preentrenamiento originales, preservando la generalización. La tercera, fine-tuning open-vocabulary, entrena sobre categorías base y evalúa sobre categorías novedosas no vistas, midiendo explícitamente la retención de capacidad OVD (X. Zhao et al., 2024). Las dos últimas estrategias fueron diseñadas específicamente para mantener la generalizabilidad del modelo mientras mejoran el rendimiento en el dataset objetivo.

Adicionalmente, la adaptación mediante técnicas de ajuste eficiente de parámetros (PEFT) ha mostrado resultados prometedores. Grounding DINO puede adaptarse al dominio de imagen médica por ultrasonido mediante adaptadores LoRA (Low-Rank Adaptation) aplicados sobre backbones ViT y BERT congelados, habilitando segmentación guiada por prompts textuales sin reentrenar las redes subyacentes (Rasaee et al., 2025). Este enfoque resulta especialmente relevante para contextos con datasets de dominio reducidos, dado que minimiza tanto el costo computacional como el riesgo de degradación de la capacidad OVD. Grounding DINO alcanza 63.0 AP en COCO con fine-tuning closed-set frente a 52.5 AP en zero-shot (Liu et al., 2023), evidenciando un margen sustancial de mejora disponible mediante adaptación de dominio.

Bloque B: Detectores one-stage tipo YOLO con alineamiento visión-lenguaje. YOLO-World (Cheng et al., 2024) presenta un comportamiento frente al fine-tuning cualitativamente distinto al de Grounding DINO, debido a que su mecanismo de fusión visión-lenguaje (RepVL-PAN) fue diseñado para ser reparametrizable, es decir, los embeddings textuales pueden incorporarse como pesos fijos del modelo, permitiendo remover el text encoder durante la inferencia. Esta decisión arquitectónica, orientada a maximizar la velocidad de despliegue, implica que el módulo de lenguaje es estructuralmente desacoplable del detector visual.

Su documentación oficial documenta tres recetas de fine-tuning (AILab-CVC, 2024). La primera, fine-tuning normal, utiliza MixedGroundingDataset con textos ricos y tareas de grounding, orientada a preservar la capacidad open-vocabulary. La segunda, fine-tuning closed-set, utiliza MultiModalDataset con un JSON de vocabulario fijo, restringiendo las clases detectables al dataset objetivo. La tercera, fine-tuning reparametrizado, remueve el RepVL-PAN y el text encoder, produciendo un modelo con arquitectura equivalente a YOLOv8 pero inicializado con pesos preentrenados a gran escala; esta variante ofrece mayor velocidad pero elimina completamente la capacidad OVD.

Un hallazgo crítico es la fragilidad del text encoder CLIP frente al fine-tuning (Cheng et al., 2024). Se observó que el ajuste del encoder textual CLIP durante el entrenamiento sobre Objects365 produce una caída severa del rendimiento, atribuyendo esta degradación a que el fine-tuning sobre un vocabulario cerrado destruye la capacidad de generalización del encoder. Este resultado sugiere que, en la familia YOLO-World, la preservación de capacidad OVD post-fine-tuning requiere congelar o ajustar con learning rate muy reducido el text encoder, concentrando la adaptación en las capas visuales y en el RepVL-PAN. La evaluación de segmentación open-vocabulary confirma este patrón. Cuando solo se ajusta el head de segmentación, el modelo retiene las capacidades zero-shot adquiridas durante el preentrenamiento; cuando se ajustan todos los módulos, el modelo se adapta mejor al dataset pero puede exhibir degradación de las capacidades zero-shot (Cheng et al., 2024).

YOLOE (Wang et al., 2025) comparte la filosofía de reparametrización y la amplía. Su estrategia RepRTA (Re-parameterizable Region-Text Alignment) permite que, tras el entrenamiento, los parámetros del modelo se reparametricen en un head YOLO estándar, preservando FLOPs y velocidad idénticos a los de YOLOv8 o YOLO11 (Wang et al., 2025). El pipeline de transferencia a datasets de dominio (denominado transferring en la documentación oficial) soporta tanto linear probing (es decir, solo la última convolución del head de clasificación es entrenable) como full tuning (todos los parámetros son entrenables). En ambos casos, el modelo resultante opera como un detector closed-set convencional. La capacidad OVD se preserva únicamente si se mantiene la rama de text prompts o visual prompts activa, lo que requiere configuración específica fuera del pipeline estándar de Ultralytics.

Bloque C: Detectores basados en dual-encoders CLIP-like. OWL-ViT (Minderer et al., 2022) y su sucesor OWLv2 (Minderer et al., 2023) ofrecen una perspectiva diferente sobre la relación entre fine-tuning y capacidad OVD. Estos modelos utilizan encoders de visión y texto preentrenados contrastivamente (CLIP o SigLIP) con heads ligeros de clasificación y localización adjuntos directamente a los tokens de salida del encoder visual. La detección open-vocabulary se habilita reemplazando los pesos fijos de clasificación por los embeddings de texto derivados del encoder lingüístico (Minderer et al., 2022). Dado que la capacidad OVD depende enteramente de la calidad del espacio de embeddings compartido, el fine-tuning sobre datasets cerrados requiere estrategias de regularización para evitar el colapso de dicho espacio. Dichas estrategias ya son proporcionadas por los mismos autores, sobre todo para lograr rendimiento competitivo tanto en detección zero-shot condicionada por texto como en detección one-shot condicionada por imagen (Minderer et al., 2022).

OWLv2 introduce una innovación relevante para el problema de la adaptación de dominio sin fine-tuning manual. Mediante la receta OWL-ST (OWL Self-Training), el modelo utiliza un detector existente para generar pseudo-anotaciones de cajas sobre pares imagen-texto a escala web, entrenándose sobre más de mil millones de ejemplos sin anotaciones humanas adicionales. Este enfoque mejora el AP en categorías raras de LVIS de 31.2% a 44.6% con arquitectura L/14 (Minderer et al., 2023). La selección del espacio de etiquetas para las pseudo-anotaciones resulta determinante. El uso de un vocabulario curado produce buen rendimiento en las clases del vocabulario pero generaliza pobremente a clases y datasets no vistos, mientras que la supervisión débil pero diversa derivada de n-gramas del texto asociado a cada imagen preserva la generalización open-vocabulary (Minderer et al., 2023). Esta evidencia refuerza la observación transversal de que la amplitud y diversidad del vocabulario de entrenamiento es un factor protector de la capacidad OVD.

Bloque D: Modelos generativos guiados por instrucciones. Florence-2 (Xiao et al., 2023) formula todas las tareas de visión como problemas de secuencia a secuencia, utilizando un encoder visual DaViT y un decoder Transformer estándar. Esta arquitectura unificada implica que el fine-tuning afecta al pipeline generativo completo, no a un módulo de fusión localizado. Florence-2 puede fine-tunearse para detección de objetos en entornos no estructurados y desordenados, alcanzando valores de mAP comparables a los de YOLOv8, YOLOv9 y YOLOv10 mediante LoRA y ajuste cuidadoso de capas Transformer (Ucar et al., 2025). La guía de Roboflow para fine-tuning de Florence-2 en detección (Skalski, 2025) reporta que el modelo fine-tuneado retiene parcialmente la capacidad de detectar clases base del preentrenamiento, aunque con rendimiento degradado respecto al modelo original. Los autores de Florence-2 reportan además que el fine-tuning con el encoder de imagen descongelado produce mejoras respecto al enfoque con encoder congelado (Xiao et al., 2023), pero esta estrategia maximiza el riesgo de degradación en categorías no vistas.

Síntesis y tabla comparativa. El análisis transversal revela un patrón consistente. La preservación de la capacidad OVD post-fine-tuning está directamente correlacionada con la profundidad e inextricabilidad de la fusión visión-lenguaje en la arquitectura. Los modelos con fusión profunda y no removible (Grounding DINO) ofrecen mayor resiliencia, dado que el fine-tuning necesariamente opera sobre una arquitectura que integra lenguaje en cada etapa de predicción. Los modelos con módulos de lenguaje removibles o reparametrizables (YOLO-World, YOLOE) tienden a perder capacidad OVD durante el fine-tuning estándar, salvo que se adopten configuraciones específicas de preservación. Los detectores dual-encoder (OWL-ViT/v2) dependen de la integridad del espacio de embeddings compartido y requieren regularización explícita o estrategias de self-training para mantener la generalización. Los modelos generativos (Florence-2) pueden adaptarse a dominios específicos mediante PEFT, pero el impacto sobre categorías no vistas requiere evaluación caso a caso.

La Tabla 4 sintetiza las estrategias de fine-tuning documentadas para los modelos representativos, indicando si preservan la capacidad OVD y las condiciones bajo las cuales lo hacen.

Tabla 4

Estrategias de fine-tuning documentadas y preservación de capacidad OVD por familia arquitectónica


| Familia / Modelo | Estrategia de fine-tuning | Preserva OVD | Condición clave |
| --- | --- | --- | --- |
| Grounding DINO | Fine-tuning closed-set | No | Vocabulario restringido post-ajuste |
| Grounding DINO | Preentrenamiento continuado open-set | Sí | LR reducido; módulos congelados; datos mixtos |
| Grounding DINO | Fine-tuning open-vocabulary (base→novel) | Sí | Evaluación explícita en categorías no vistas |
| Grounding DINO | Adaptación LoRA | Sí | Backbones congelados; solo adapters entrenables |
| YOLO-World | Fine-tuning con MixedGroundingDataset | Parcial | Depende de capas ajustadas; text encoder frágil |
| YOLO-World | Fine-tuning closed-set (MultiModalDataset) | No | Vocabulario fijo en JSON |
| YOLO-World | Reparametrización eficiente (sin RepVL-PAN) | No | Text encoder removido; equivale a YOLOv8 |
| YOLOE | Transferring (linear probing / full tuning) | No | Modelo reparametrizado como YOLO estándar |
| OWL-ViT / OWLv2 | Fine-tuning end-to-end con regularización | Parcial | Requiere estrategias de regularización |
| OWL-ViT / OWLv2 | Self-training (OWL-ST) con pseudo-anotaciones | Sí | Vocabulario diverso (n-gramas) preserva OVD |
| Florence-2 | Fine-tuning con LoRA | Parcial | Retención parcial de clases base; encoder congelado recomendado |

Nota. "Preserva OVD" indica si el modelo resultante puede recibir prompts textuales arbitrarios en inferencia y detectar categorías no vistas durante el fine-tuning. "Parcial" indica preservación dependiente de la configuración específica (capas congeladas, learning rate, datos de entrenamiento). Fuente: Elaboración propia basada en AILab-CVC (2024), Cheng et al. (2024), Liu et al. (2023), Minderer et al. (2022, 2023), Rasaee et al. (2025), Ucar et al. (2025), Wang et al. (2025), Xiao et al. (2023) y Zhao et al. (2024b).

La evidencia sintetizada en la Tabla 4 permite identificar una regularidad en la literatura. La preservación de la capacidad OVD post-fine-tuning depende de tres factores que operan conjuntamente. El primero es la profundidad de la integración visión-lenguaje en la arquitectura, donde los modelos con fusión profunda y no removible exhiben mayor resiliencia que aquellos con módulos de texto desacoplables. El segundo es la estrategia de congelamiento de parámetros, donde las técnicas de ajuste eficiente (LoRA, linear probing, congelamiento selectivo de capas) reducen el riesgo de degradación respecto del ajuste completo de todos los módulos. El tercero es la amplitud y diversidad del vocabulario utilizado durante el fine-tuning, donde los enfoques que mantienen vocabularios ricos o mixtos preservan mejor la generalización que aquellos que restringen el entrenamiento a un conjunto cerrado de categorías. Estos factores no son independientes entre sí, sino que interactúan de manera que las arquitecturas con fusión profunda toleran mejor el ajuste completo, mientras que las arquitecturas con módulos removibles requieren estrategias de preservación más conservadoras para retener capacidad OVD.


#### 15.2.5. Brechas identificadas en el dominio de la construcción civil

A partir de la revisión y síntesis de los enfoques presentados, se pone de manifiesto un conjunto de limitaciones estructurales que no quedan plenamente resueltas por los modelos actuales de detección open-vocabulary. Estas brechas delinean líneas de trabajo relevantes para etapas posteriores del proyecto y permiten anticipar desafíos técnicos que deberán abordarse durante el diseño arquitectónico y la implementación del prototipo.


##### 15.2.5.1. Contextualización semántica limitada

La mayoría de los detectores OVD actuales resuelven la detección como una combinación de localización espacial y compatibilidad textual evaluada de manera independiente para cada región candidata (Zareian et al., 2021; Liu et al., 2023). Este enfoque, aunque efectivo para identificar objetos individuales, no garantiza consistencia contextual entre múltiples entidades detectadas ni permite razonar sobre relaciones espaciales o semánticas entre ellas.

En entornos industriales y de construcción, muchos conceptos relevantes para la seguridad son inherentemente composicionales y dependen del contexto espacial. Condiciones como "persona sin casco cerca de excavación", "operario en zona de tránsito vehicular" o "escalera bloqueando salida de emergencia" requieren no solo detectar cada elemento de manera aislada, sino también evaluar sus relaciones geométricas y semánticas. Los modelos OVD actuales carecen de mecanismos nativos para este tipo de razonamiento relacional, lo que sugiere la necesidad de incorporar módulos adicionales de inferencia contextual o reglas de negocio que operen sobre las detecciones primarias.


##### 15.2.5.2. Ausencia de consistencia temporal nativa

Los modelos de detección open-vocabulary operan predominantemente sobre imágenes estáticas, procesando cada fotograma de manera independiente sin mantener memoria de estados previos ni modelar explícitamente la evolución temporal de las detecciones. Esta característica introduce variabilidad frame-to-frame que puede manifestarse como fluctuaciones en los puntajes de confianza, apariciones y desapariciones espurias de detecciones, e inconsistencias en la asignación de etiquetas entre cuadros consecutivos.

En aplicaciones de vídeo, particularmente aquellas orientadas a monitoreo continuo, esta variabilidad temporal resulta problemática. Los enfoques generativos, como Florence-2, tienden a exhibir mayor inestabilidad debido a la naturaleza autoregresiva de su decodificación (Xiao et al., 2023). La literatura reciente sugiere que la integración con módulos de seguimiento multi-objeto (MOT) constituye una estrategia efectiva para mitigar este problema, permitiendo que el tracker aporte coherencia temporal a las detecciones semánticamente ricas del OVD (Li et al., 2023). No obstante, esta integración introduce complejidad arquitectónica adicional y requiere considerar la compatibilidad entre el detector y el método de tracking seleccionado.


##### 15.2.5.3. Sensibilidad a la formulación del prompt

La flexibilidad semántica que caracteriza a la detección open-vocabulary introduce una dependencia significativa respecto de la formulación exacta de las consultas textuales. Investigaciones en modelos visión-lenguaje han demostrado que pequeños cambios en la redacción de las consultas pueden producir diferencias significativas en el desempeño, incluso cuando diferentes formulaciones refieren al mismo concepto subyacente (Zhou et al., 2022b). Esta sensibilidad tiene implicancias directas para la usabilidad del sistema: usuarios con diferentes niveles de experiencia o distintas convenciones lingüísticas pueden obtener resultados heterogéneos ante objetivos de detección equivalentes.

Esta observación motivó el desarrollo de técnicas de prompt learning, donde los tokens de contexto se reemplazan por vectores aprendibles que se optimizan con datos etiquetados del dominio objetivo (Zhou et al., 2022b; Khattak et al., 2023). Sin embargo, las estrategias desarrolladas para clasificación de imágenes no se transfieren directamente al contexto de detección. Se demostró que la optimización automática de representaciones de prompts —específicamente diseñada para tareas de detección— supera consistentemente a los prompts elaborados mediante ingeniería manual, evidenciando la necesidad de enfoques especializados para el dominio OVD (Du et al., 2022) . Adicionalmente, algunos modelos recientes abordan parcialmente esta limitación mediante el soporte de prompts visuales que permiten anclar la detección a ejemplos concretos en lugar de depender exclusivamente de descripciones textuales (Jiang et al., 2024).


##### 15.2.5.4. Sensibilidad al dominio de aplicación

Los benchmarks estándar utilizados para evaluar modelos OVD —como MS COCO con 80 categorías de objetos cotidianos (Lin et al., 2014) o LVIS con más de 1200 categorías de distribución long-tail (Gupta et al., 2019)— no representan plenamente las condiciones visuales y semánticas de entornos industriales especializados. En el contexto específico de obras de construcción, factores como iluminación extrema, oclusiones frecuentes por maquinaria y estructuras, indumentaria especializada de protección, y presencia de equipamiento industrial introducen distribuciones visuales que difieren significativamente de los datos de preentrenamiento.

Esta brecha de dominio sugiere que, incluso con la capacidad de generalización zero-shot que caracteriza a los modelos OVD, será necesario algún grado de adaptación o calibración para optimizar el rendimiento en el dominio objetivo. Las estrategias potenciales incluyen el ajuste de umbrales de confianza por tipo de escena, la incorporación de filtros de post-procesamiento para falsos positivos recurrentes, y eventualmente el refinamiento ligero (fine-tuning) sobre conjuntos reducidos de imágenes representativas del entorno de obra. No obstante, el fine-tuning en modelos OVD introduce un compromiso entre mejora de rendimiento en categorías vistas y potencial degradación de la capacidad open-vocabulary, cuya intensidad depende de la arquitectura del modelo y de la estrategia de ajuste empleada.


##### 15.2.5.5. Protocolos de evaluación específicos para seguridad industrial

Las métricas de evaluación predominantes en la literatura OVD —como Average Precision (AP) en COCO o LVIS— constituyen indicadores generales de rendimiento que no capturan adecuadamente el valor operativo de un sistema de detección en el contexto de seguridad industrial (Gupta et al., 2019). Estas métricas evalúan la precisión de localización y clasificación frame-by-frame, sin considerar aspectos temporales ni el impacto diferenciado de distintos tipos de error en escenarios de monitoreo de riesgos.

Para validar la plataforma en su dominio de aplicación, resulta necesario diseñar métricas y protocolos de evaluación alineados con los objetivos de seguridad en construcción. Esto incluye considerar la tasa de eventos de riesgo detectados correctamente a lo largo de secuencias de video, el tiempo transcurrido entre el inicio de una condición de riesgo y su detección (latencia de alerta), la tasa de falsas alarmas por unidad de tiempo de monitoreo, y la persistencia mínima requerida para considerar válida una detección.


##### 15.2.5.6. Tabla comparativa de brechas identificadas

Tabla 5

Brechas identificadas en la aplicación de modelos OVD al dominio de seguridad en construcción civil


| Brecha identificada | Descripción | Implicación para el proyecto |
| --- | --- | --- |
| Contextualización semántica limitada | Los modelos OVD detectan entidades localmente pero no infieren relaciones espaciales complejas entre ellas (p. ej., “persona dentro de zona restringida” requiere razonamiento relacional) | El sistema no puede depender exclusivamente del detector para condiciones composicionales; se requieren módulos adicionales de razonamiento contextual |
| Ausencia de consistencia temporal nativa | La detección frame-a-frame introduce variabilidad en puntajes de confianza, apariciones y desapariciones espurias entre cuadros consecutivos | Necesidad de integración con módulo MOT para aportar coherencia temporal a las detecciones semánticas (S. Li et al., 2023) |
| Sensibilidad a la formulación del prompt | Pequeños cambios en la redacción producen diferencias significativas en el desempeño, incluso para conceptos equivalentes (Zhou et al., 2022b) | El diseño de prompts para condiciones de riesgo requiere un proceso sistemático; la selección informal puede comprometer la robustez del sistema |
| Brecha de dominio con benchmarks estándar | MS COCO (80 categorías) y LVIS (1200+ categorías) no representan las condiciones visuales de obras civiles: iluminación extrema, oclusiones por maquinaria, indumentaria especializada (Gupta et al., 2019; Lin et al., 2015) | El desempeño reportado en benchmarks no es directamente transferible al dominio objetivo; se requiere evaluación empírica en condiciones representativas |
| Ausencia de protocolos de evaluación específicos para seguridad industrial | Las métricas AP en COCO/LVIS (Gupta et al., 2019; Lin et al., 2015) no capturan el valor operativo del sistema: no consideran latencia de alerta, persistencia de la detección ni impacto diferenciado de falsos positivos/negativos. | La Etapa 2 del proyecto debe diseñar métricas y protocolos de evaluación alineados con los objetivos de seguridad laboral |

Nota. Las brechas listadas no constituyen limitaciones insalvables, sino desafíos técnicos que definen el espacio de problemas a abordar en las Etapas 2 y 3 del proyecto. Fuente: Elaboración propia basada en las fuentes mencionadas (Gupta et al., 2019; S. Li et al., 2023; Lin et al., 2015; Liu et al., 2023; Zareian et al., 2021; Zhou et al., 2022a, 2022b).


#### 15.2.6. Síntesis de la sección y avance al seguimiento multi-objeto

El análisis de los paradigmas OVD evidencia que la viabilidad de su integración en sistemas de monitoreo continuo está condicionada por cuatro factores: balance entre expresividad semántica y eficiencia de inferencia, diseño sistemático de prompts para el dominio específico, mecanismos de compensación de la variabilidad temporal frame-a-frame, y evaluación empírica en condiciones visuales de construcción civil. Los dos últimos factores remiten directamente al problema de persistencia temporal: dado que la OVD produce observaciones instantáneas sin identidad ni continuidad, la sección siguiente analiza los métodos de seguimiento multiobjeto como mecanismo para sostener esas detecciones a lo largo del tiempo


### 15.3. Seguimiento multiobjeto: métodos, métricas y brechas del estado del arte

El seguimiento multiobjeto (MOT) constituye el mecanismo que transforma las detecciones instantáneas producidas por el sistema OVD en trayectorias persistentes a lo largo del tiempo, habilitando la agregación temporal de evidencias necesaria para la generación de alertas operativas. En esta sección se analizan los métodos representativos del estado del arte en MOT para sistemas de video en tiempo real, las métricas de evaluación relevantes para el contexto del proyecto y las brechas identificadas en la intersección entre MOT y detección open-vocabulary.


#### 15.3.1. Métodos Representativos

El estado del arte en MOT para sistemas de video en tiempo real está dominado por la familia SORT extendida, cuya evolución refleja el progreso en el manejo de oclusiones, la explotación de detecciones de baja confianza y la eliminación de dependencias de entrenamiento específico por dominio.


##### 15.3.1.1. SORT

SORT (Simple Online and Realtime Tracking) establece el esquema de referencia del paradigma tracking-by-detection moderno. Combina el filtro de Kalman para el modelado del movimiento con el algoritmo Húngaro para la asignación óptima de detecciones a trayectorias, utilizando IoU como única métrica de similitud. Su diseño minimalista prescinde de cualquier modelado de apariencia, lo que resulta en latencia muy baja —capacidad de operar a tasas superiores a 200 FPS— y ausencia total de dependencias de entrenamiento. La principal limitación de SORT es su baja robustez ante oclusiones: cuando un objeto no es detectado durante varios cuadros consecutivos, la trayectoria se termina y la re-asociación posterior puede producir un cambio de identificador (ID switch), fragmentando la trayectoria en múltiples segmentos (Bewley et al., 2016).


##### 15.3.1.2. DeepSORT

DeepSORT extiende SORT incorporando el modelado de apariencia descrito en el análisis del modelado de apariencia, con el objetivo de mitigar las ambigüedades de asociación en presencia de oclusiones y cruces (Wojke et al., 2017). En términos operativos, mantiene el marco de predicción de movimiento y validación cinemático-estadística, pero introduce un término adicional de similitud visual basado en embeddings extraídos por una red neuronal, integrando la evidencia de movimiento y apariencia en la función de costo de asociación (Wojke et al., 2017).

La consecuencia directa es una reducción significativa de cambios de identidad y una mayor capacidad de re-asociación tras desapariciones temporales, particularmente en secuencias con oclusiones parciales o alta densidad de objetos. Sin embargo, este aumento de robustez implica mayores requerimientos computacionales y dependencia de un modelo de re-identificación entrenado. En aplicaciones estrictamente en tiempo real, esta dependencia puede degradar el rendimiento si no se optimiza adecuadamente el extractor de características. Asimismo, en entornos open-vocabulary dinámicos, la dependencia de embeddings entrenados con dominios específicos puede introducir restricciones adicionales o degradaciones cuando el dominio visual o las categorías observadas se alejan del régimen de entrenamiento (Wojke et al., 2017).


##### 15.3.1.3. ByteTrack

ByteTrack introduce una innovación conceptualmente simple pero con impacto significativo sobre la robustez del tracker: en lugar de descartar las detecciones por debajo de un umbral de confianza del detector —como hace SORT—, las utiliza en una segunda etapa de asociación para mantener la continuidad de trayectorias existentes. La idea central es que una detección de baja confianza en el cuadro t puede corresponder a un objeto parcialmente ocluso cuya trayectoria fue establecida en cuadros anteriores; descartarla produce una fragmentación innecesaria. La asociación se estructura en dos pasos jerárquicos: primero se asocian las detecciones de alta confianza con las trayectorias activas; luego, las trayectorias no asociadas se intentan conectar con las detecciones de baja confianza. ByteTrack mantiene la ausencia de modelos de apariencia y logra tasas de inferencia superiores a 170 FPS, siendo directamente compatible con detectores one-stage como YOLO-World (Adžemović, 2025; Y. Zhang et al., 2022).


##### 15.3.1.4. OC-SORT

OC-SORT (Observation-Centric SORT) aborda una limitación distinta de SORT: la degradación del modelo de movimiento durante los períodos de oclusión. En SORT, cuando un objeto no es detectado durante varios cuadros, el filtro de Kalman continúa actualizando el estado interno basándose únicamente en predicciones del modelo dinámico, acumulando error de estimación que se manifiesta en asociaciones incorrectas cuando el objeto reaparece. OC-SORT introduce dos correcciones principales: el Observation-Centric Momentum (OCM), que estima la dirección y magnitud del movimiento del objeto a partir de sus observaciones históricas en lugar de basarse en las predicciones del filtro, y el Observation-Centric Re-Update (OCR), que reajusta las estimaciones del filtro utilizando las observaciones reales durante los períodos de oclusión. Estas correcciones reducen los ID switches sin incorporar modelos de apariencia ni incrementar significativamente el costo computacional (Cao et al., 2023).


##### 15.3.1.5. BoT-SORT y métodos end-to-end

BoT-SORT (Aharon et al., 2022) representa un punto de convergencia entre la eficiencia de ByteTrack y la robustez de DeepSORT: incorpora embeddings de apariencia, compensación de movimiento de cámara (CMC) mediante homografía, y la estrategia de asociación jerárquica de ByteTrack. Este diseño maximiza la precisión en benchmarks a costa de una mayor complejidad computacional y la dependencia de un modelo ReID preentrenado, posicionándolo como una opción de alta precisión cuando la robustez prima sobre la latencia.

En el extremo opuesto del espectro de complejidad, los enfoques end-to-end basados en Transformers —como TrackFormer (Meinhardt et al., 2022) y MOTR— formulan el tracking como un problema de predicción conjunta de detecciones y asociaciones en una única red entrenada conjuntamente. Si bien estas arquitecturas ofrecen ventajas teóricas en términos de coherencia global del pipeline, sus altos requisitos computacionales, la complejidad del entrenamiento conjunto y la limitada flexibilidad para integrar detectores OVD externos hacen que su adopción en sistemas experimentales de tiempo real sea actualmente limitada (Adžemović, 2025).


#### 15.3.2. Síntesis comparativa de métodos MOT

La Tabla 6 sintetiza las características principales de los métodos MOT analizados, con énfasis en las dimensiones más relevantes para su integración en el sistema E-OVRT-VDP: paradigma, modelo de movimiento, estrategia de asociación, robustez ante oclusiones, latencia y dependencias de entrenamiento.

Tabla 6

Síntesis comparativa de métodos MOT representativos según dimensiones relevantes para sistemas de video en tiempo real con detección open-vocabulary


| Método | Paradigma | Modelo de movimiento | Asociación de datos | Robustez a oclusiones | Latencia / FPS | Dependencia de entrenamiento |
| --- | --- | --- | --- | --- | --- | --- |
| SORT | Tracking-by- detection | Kalman lineal | IoU + Húngaro | Baja | Muy alta (>200 FPS) | Ninguna |
| DeepSORT | Tracking-by- detection | Kalman lineal | Cascada: movimiento + apariencia | Media-Alta | Media | Modelo ReID preentrenado |
| ByteTrack | Tracking-by- detection | Kalman lineal | Jerárquica: alta/baja confianza + IoU | Alta | Muy alta (>170 FPS) | Ninguna |
| OC-SORT | Tracking-by- detection | Kalman + correcciones OC | IoU + consistencia de momento (OCM) | Media-Alta | Muy alta | Ninguna |
| BoT-SORT | Tracking-by- detection | Kalman mejorado + CMC | Fusión IoU-ReID | Alta | Media | Modelo ReID preentrenado |
| TrackFormer / MOTR | End-to-end (Transformer) | Atención temporal aprendida | Mecanismo de atención global | Muy alta | Baja | Entrenamiento conjunto requerido |

Nota. CMC = Compensación de Movimiento de Cámara (Camera Motion Compensation). OC = Observation-Centric. La columna 'Dependencia de entrenamiento' refiere a componentes adicionales al detector base que requieren entrenamiento supervisado. FPS estimados corresponden a las configuraciones reportadas en los trabajos originales sobre hardware de referencia; pueden variar significativamente según el hardware y la resolución de entrada. Fuente: Elaboración propia basada en las fuentes citadas (Adžemović, 2025; Aharon et al., 2022; Bewley et al., 2016; Cao et al., 2023; Wojke et al., 2017; Y. Zhang et al., 2022).


##### 15.3.2.1. Observaciones críticas sobre la comparativa

La comparativa evidencia que los métodos de tracking-by-detection puramente geométricos, como SORT, ByteTrack y OC-SORT, presentan una mayor compatibilidad con detectores open-vocabulary, ya que no dependen de modelos de apariencia entrenados en dominios específicos y permiten desacoplar el detector del módulo de seguimiento. Esta propiedad resulta especialmente relevante en sistemas donde las clases de interés pueden variar dinámicamente según las consultas del usuario y donde se requiere sustituir modelos sin reentrenamiento. En términos operativos, se observa un trade-off entre velocidad y robustez: los métodos geométricos alcanzan altas tasas de procesamiento y menor latencia, aunque son más sensibles a oclusiones prolongadas, mientras que enfoques como DeepSORT o BoT-SORT mejoran la estabilidad de identidades mediante embeddings visuales, a costa de mayor carga computacional. Por su parte, los métodos end-to-end como FairMOT o TrackFormer ofrecen integración profunda entre detección y seguimiento, pero su necesidad de entrenamiento conjunto limita la flexibilidad requerida por pipelines OVD modulares. En este marco, ByteTrack y OC-SORT representan alternativas particularmente equilibradas, al introducir mejoras sobre SORT —asociación de detecciones de baja confianza y correcciones observation-centric— sin perder eficiencia computacional. Por ello, para una plataforma experimental de detección open-vocabulary en tiempo real, la familia SORT extendida se presenta como la opción más adecuada, al combinar independencia del detector, bajo costo computacional, robustez suficiente y mayor transparencia para la iteración, auditoría y diagnóstico de fallos.


#### 15.3.3. Métricas de evaluación para MOT

La evaluación del desempeño de algoritmos MOT requiere métricas estandarizadas que capturen diferentes aspectos del problema: precisión de detección, consistencia de identidad y localización espacial. Las tres métricas principales en la literatura son MOTA, IDF1 y HOTA, cada una con sesgos y alcances distintos que hacen necesaria su interpretación conjunta (Luiten et al., 2021).


##### 15.3.3.1. MOTA (Multiple Object Tracking Accuracy)

MOTA es la métrica clásica de evaluación MOT. Se define como: MOTA = 1 − (FN + FP + IDSW) / GT, donde FN son falsos negativos, FP son falsos positivos, IDSW son cambios de identidad, y GT es el total de objetos ground truth. MOTA está sesgada hacia medir la precisión de detección, penalizando fuertemente los errores de detección sobre los errores de asociación (Bernardin & Stiefelhagen, 2008).


##### 15.3.3.2. IDF1 (Identification F1-Score)

IDF1 se enfoca en la consistencia de identidad a largo plazo. Calcula el F1-score entre detecciones verdaderas positivas que mantienen la identidad correcta. IDF1 está sesgada hacia medir la asociación, a expensas de ignorar mejoras en la detección (Ristani et al., 2016).


##### 15.3.3.3. HOTA (Higher Order Tracking Accuracy)

HOTA surge como respuesta a las limitaciones de MOTA e IDF1. HOTA balancea explícitamente la precisión de detección y asociación mediante la fórmula:


|  | (1) |
| --- | --- |

donde DetA es la precisión de detección y AssA es la precisión de asociación (Luiten et al., 2021). HOTA también incorpora la precisión de localización, ausente en MOTA e IDF1. La métrica ha sido adoptada por los principales benchmarks como MOTChallenge y se recomienda para evaluaciones comprehensivas de trackers modernos.

Sin embargo, las tres métricas presentan una limitación común para el dominio de seguridad laboral: evalúan el desempeño del tracker de manera agnóstica al valor operativo de cada tipo de error. Un ID switch en una trayectoria de persona dentro de zona restringida tiene un impacto operativo muy diferente a un ID switch en una trayectoria de maquinaria estacionaria, pero ambos contribuyen de manera idéntica al cómputo de MOTA o HOTA. Esta homogeneización del error es incompatible con los requisitos de un sistema de alerta cuya efectividad depende de distinguir entre tipos de error con consecuencias asimétricas. La consolidación metodológica posterior del proyecto deberá abordar el diseño de criterios de evaluación complementarios alineados con los objetivos de seguridad laboral.


#### 15.3.4. Brechas identificadas y desafíos para el prototipo

El análisis del estado del arte en MOT revela un conjunto de brechas que condicionan el diseño del prototipo y las decisiones metodológicas de la consolidación metodológica posterior. La Tabla 7 organiza estas brechas con su descripción técnica y su implicación específica para el proyecto.

Tabla 7

Brechas identificadas en la aplicación de métodos MOT al contexto de seguridad en construcción civil en combinación con detección open-vocabulary


| Brecha identificada | Descripción | Implicación para el proyecto |
| --- | --- | --- |
| Dependencia de la calidad del detector subyacente | El rendimiento del MOT está fuertemente acoplado al desempeño del detector. Errores de detección —FP, FN, bounding boxes inestables— se propagan al tracking, produciendo fragmentación de trayectorias, pérdidas de identidad y asociaciones erróneas (S. Li et al., 2025) | En el pipeline OVD + MOT, la variabilidad inherente de la detección open-vocabulary puede amplificar errores de asociación; el diseño del sistema debe contemplar estrategias de filtrado y umbralización que reduzcan el ruido de entrada al tracker |
| Fragilidad ante oclusiones prolongadas | Aunque los métodos modernos manejan oclusiones breves, las oclusiones de larga duración producen terminación prematura de trayectorias, re-asociaciones inciertas y aumento de ID switches (Du et al., 2024) | En entornos de obra civil con alta densidad de obstrucciones (andamios, maquinaria, materiales), la robustez ante oclusiones es una restricción de diseño relevante que debe evaluarse empíricamente |
| Ausencia de semántica en los identificadores de tracking | Los identificadores asignados por MOT son puramente internos y efímeros: no persisten entre sesiones, cámaras ni reinicios del sistema (Du et al., 2024) | El sistema no puede utilizar el tracking para correlación inter-cámara sin mecanismos adicionales; las alertas basadas en persistencia de identidad quedan limitadas al contexto temporal inmediato de cada flujo de video |
| Métricas estándar no alineadas con objetivos operativos de seguridad | Las métricas MOTA, IDF1 y HOTA evalúan el desempeño del tracking frame-a-frame sin considerar el impacto operativo diferenciado de distintos tipos de error en el contexto de seguridad laboral (Luiten et al., 2021) | Se deben definir criterios de evaluación del componente MOT alineados con el dominio: persistencia mínima para disparar alertas, penalización diferenciada de ID switches en condiciones de riesgo, y tolerancia ante falsos positivos por oclusión |
| Ausencia de datasets de construcción con anotaciones de tracking | Los benchmarks estándar de MOT (MOT17, MOT20, DanceTrack) no contemplan el dominio de obras civiles; la evaluación del tracker en condiciones representativas requiere datos del dominio específico (Dendorfer et al., 2020; Milan et al., 2016) | La validación del componente MOT en el prototipo no puede apoyarse en benchmarks estándar; se requiere la definición de un protocolo de evaluación propio con datos recopilados en el contexto del proyecto |

Nota. Las brechas listadas definen el espacio de problemas abiertos que deben abordarse en el diseño experimental (etapa 2) y en la implementación del prototipo (etapa 4). Fuente: Elaboración propia basada en las fuentes citadas (Adžemović, 2025; Dendorfer et al., 2020; Du et al., 2024; S. Li et al., 2025; Luiten et al., 2021; Milan et al., 2016).

La brecha de ausencia de datasets de construcción con anotaciones de tracking merece una consideración adicional. Los benchmarks estándar de MOT —MOT17, MOT20, DanceTrack— fueron diseñados para escenarios de peatones en entornos urbanos y eventos de danza respectivamente, con distribuciones visuales que difieren significativamente de una obra civil: densidad de cámara fija en planos elevados, entidades heterogéneas (personas, maquinaria, materiales), indumentaria de protección que puede confundir a los modelos de apariencia, y configuraciones de oclusión determinadas por la geometría de la obra. Esta brecha no puede resolverse mediante adaptación de los benchmarks existentes; requiere la definición de un protocolo de evaluación propio que se apoyará en los datos recopilados durante la fase experimental del proyecto.


### 15.4. Video en tiempo real y streaming: protocolos, servidores y brechas del estado del arte


#### 15.4.1. Protocolos de transmisión de video de baja latencia

Los protocolos de transmisión de vídeo constituyen un componente relevante dentro del análisis de sistemas de vídeo en tiempo real, debido a que condicionan la forma en que los flujos provenientes de cámaras o fuentes de vídeo son transportados hacia los módulos de procesamiento, visualización o almacenamiento. En el contexto del presente proyecto, su estudio resulta necesario porque la detección open-vocabulary no opera sobre imágenes aisladas, sino sobre secuencias continuas que deben ser recibidas, decodificadas y procesadas con una latencia compatible con la generación oportuna de alertas.

Desde una perspectiva general, los protocolos de streaming pueden diferenciarse por dimensiones como el modelo de entrega, el esquema de distribución, la tolerancia a pérdidas, los mecanismos de buffering y el orden de magnitud de latencia que suelen alcanzar bajo determinadas condiciones de red y configuración. Sin embargo, estos valores no deben interpretarse como propiedades absolutas de cada protocolo, ya que la latencia final depende del pipeline completo: captura, codificación, transporte, decodificación, inferencia, evaluación de patrones y comunicación de resultados. Estos componentes serán retomados con mayor detalle en el marco teórico y en la descripción técnica del sistema, donde se analizará su impacto dentro de la arquitectura experimental.

En esta sección, el análisis se limita a revisar los protocolos y familias de transmisión más relevantes para aplicaciones de baja latencia, identificando sus características principales, sus restricciones prácticas y su grado de compatibilidad con un sistema de análisis automatizado de vídeo. Esta revisión permite establecer criterios preliminares para la selección posterior del stack de medios, sin definir todavía una implementación definitiva.


##### 15.4.1.1. Criterios de clasificación de protocolos

Modelo de entrega push. En el modelo push, una vez establecida la sesión, el emisor entrega el flujo de manera continua hacia el receptor (típicamente sobre UDP o sobre una sesión persistente), minimizando esperas asociadas a la solicitud de unidades discretas de contenido. Protocolos de tiempo real, como RTP y flujos interactivos como WebRTC, se alinean más naturalmente con push (ISO/IEC, 2022; May, 2017a).

Modelo de entrega pull. En el modelo pull, el control de la entrega reside principalmente en el cliente: el receptor solicita (por HTTP) segmentos o partes de segmentos en forma sucesiva, habilitando escalabilidad y cacheo, pero introduciendo buffering y latencias asociadas a segmentación y recarga. Los esquemas adaptativos sobre HTTP, como HLS y MPEG-DASH, responden al patrón pull (cliente-driven).

Esquema de distribución unicast. En unicast, cada cliente mantiene una conexión individual y recibe un flujo dedicado, lo que simplifica control por receptor (adaptación, seguridad, métricas), pero escala el consumo de ancho de banda en el emisor.

Esquema de distribución multicast. En multicast, el emisor envía un único flujo a un grupo multicast y la red replica hacia múltiples receptores, siendo eficiente en redes administradas. Protocolos basados en RTP pueden operar sobre unicast o multicast; sin embargo, el multicast IP no es viable en Internet abierta (en general no es ruteable extremo-a-extremo y complica control de congestión por receptor).

Orden de magnitud de latencia. Otra forma práctica de categorizar protocolos es por la latencia end-to-end típica que habilitan bajo configuraciones habituales. En términos operativos pueden distinguirse tres rangos:

Alta latencia (>~3 s). Protocolos orientados a distribución masiva y robustez. Aquí se ubican implementaciones “clásicas” de HLS y MPEG-DASH con segmentos de varios segundos. Al apoyarse en HTTP/HTTPS y CDN, priorizan escalabilidad y tolerancia a fallos, usualmente con latencias del orden de varios segundos a decenas de segundos (ISO/IEC, 2022; May, 2017a).

Latencia media (~0,5 a 3 s). Incluye protocolos como RTMP (en ingesta), RTSP cuando se opera con buffers conservadores o sobre TCP, y variantes de baja latencia de HLS/DASH basadas en segmentación fina y entrega parcial.

Baja latencia (<~500 ms). Protocolos diseñados para interactividad estricta y respuesta casi en tiempo real: WebRTC, SRT, RIST y flujos RTP con mínima capa de sesión. En general emplean UDP para evitar la penalidad de retransmisiones fuera de plazo y operan con buffers pequeños, compensando la pérdida con estrategias específicas (p. ej., ARQ “dentro de un presupuesto de tiempo” en SRT/ RIST). En WebRTC, además, la conectividad extremo-a-extremo depende de mecanismos de traversal NAT como ICE, que influyen en la latencia efectiva según el tipo de red (Keranen et al., 2018; Nakagawa et al., 2021; Schulzrinne et al., 2003b; M. P. Sharabayko et al., 2024; Video Services Forum, 2020).


##### 15.4.1.2. Mapa de familias de protocolos según los criterios de clasificación

En esta sección, se analizan los protocolos más relevantes aplicando sistemáticamente (i) modelo de entrega, (ii) esquema de distribución y (iii) latencia típica, además de consideraciones prácticas pertinentes a cada protocolo (NAT, resiliencia, seguridad, tooling).

RTSP/RTP: El estándar de cámaras IP industriales. El Real-Time Streaming Protocol (RTSP) es un protocolo de capa de aplicación orientado al control de sesiones de streaming. Fue especificado inicialmente en el RFC 2326 (Schulzrinne et al., 1998a) y posteriormente revisado en RTSP 2.0 mediante el RFC 7826, dejando obsoleta la versión original (Schulzrinne et al., 2016). En términos funcionales, RTSP opera como plano de control: define cómo un cliente describe una sesión, negocia parámetros y ejecuta acciones de control, mientras que el transporte del audio y el video no suele ocurrir en RTSP sino en un protocolo de medios separado. RTSP mantiene estado de sesión y utiliza comandos bidireccionales con sintaxis similar a HTTP.

En este esquema, el transporte de medios suele realizarse con el Real-time Transport Protocol (RTP), definido en el RFC 3550, acompañado por RTCP que informa métricas como pérdida y jitter, útiles para diagnóstico y sincronización (Schulzrinne et al., 2003b). RTP se encapsula típicamente sobre UDP e incorpora cabeceras con timestamps y números de secuencia para facilitar la reconstrucción temporal del flujo, la sincronización entre medios y el manejo del jitter en el receptor..

RTSP/RTP se adoptó ampliamente en entornos industriales y de videovigilancia por su compatibilidad y madurez, y su uso se encuentra alineado con especificaciones del ecosistema IP de seguridad, como ONVIF Profile S, donde RTSP aparece como componente central para consumo/control de streams (ONVIF, 2019). Operativamente, la combinación RTSP/RTP es particularmente conveniente en redes controladas (LAN) por su eficiencia cuando se usa UDP; no obstante, en escenarios con NAT y firewalls puede aparecer fricción por la necesidad de múltiples flujos/puertos para RTP/RTCP. Para mitigar este problema, RTSP contempla la posibilidad de transportar RTP/RTCP interleaved sobre la misma conexión TCP, simplificando el cruce de firewalls, aunque introduciendo trade-offs propios de TCP (por ejemplo, mayor sensibilidad a variaciones y efectos de bloqueo por orden) (Schulzrinne et al., 1998a, 2016). En términos de puertos, el registro de IANA asocia comúnmente rtsp con 554/TCP y 554/UDP, y rtsps con 322/TCP y 322/UDP, aunque en la práctica los vendors pueden operar con puertos alternativos por configuración (Internet Assigned Numbers Authority, s/f).

En cuanto a latencia, es importante explicitar un criterio: los valores reportados para un protocolo son rangos típicos observados y no compromisos del estándar. Ni RTSP ni RTP garantizan un valor en específico. La latencia end-to-end (glass-to-glass) se ve dominada por el pipeline completo (captura, codificación, red, decodificación) y, de manera muy marcada, por el buffer del receptor y las políticas del cliente de reproducción. En literatura técnica de videovigilancia se describe explícitamente que múltiples etapas suman retardo y que el play-out buffer puede convertirse en un componente dominante, elevando la latencia para priorizar estabilidad ante jitter (Axis Communications AB, 2015). Bajo condiciones favorables, RTSP/RTP puede operar con latencias del orden de cientos de milisegundos (por ejemplo, ~200–800 ms). En despliegues reales con Video Management Software (VMS), donde se prioriza continuidad y tolerancia a variaciones de red, es frecuente observar valores que suben a 1.000–2.000 ms o más, configurados explícitamente por buffering y por el comportamiento del cliente (Axis Communications AB, 2015).

RTMP: El protocolo de ingesta dominante de la era Flash. El Real-Time Messaging Protocol (RTMP) fue impulsado históricamente por el ecosistema Flash y, aunque Flash Player quedó oficialmente descontinuado (fin de soporte el 31/12/2020 y bloqueo de contenido desde el 12/01/2021), RTMP sigue teniendo un rol vigente como protocolo de ingesta hacia plataformas y servidores de streaming (Adobe, 2021; Twitch Developers, s/f). Conceptualmente, RTMP se apoya sobre TCP y establece una conexión persistente en la que viajan audio, video y datos de control multiplexados; el diseño incorpora un mecanismo de “chunking” para intercalar flujos y sostener continuidad de entrega: el tamaño máximo de chunk por defecto es 128 bytes, aunque puede renegociarse mediante mensajes de control (Parmar & Thornburgh, 2012). En la práctica operativa, suele utilizar el puerto 1935 (por defecto), y existen variantes para atravesar restricciones de red, como RTMPS (RTMP sobre TLS) o tunelado por HTTP (The FFmpeg developers, s/f-b).

Desde el punto de vista de arquitectura, RTMP se comporta como un canal “siempre abierto” entre codificador (OBS/encoder/cámara) y servidor/plataforma, en el que la sesión intercambia comandos y metadatos además de los paquetes de medios (Parmar & Thornburgh, 2012). Esa persistencia simplifica la ingesta en escenarios clásicos de broadcasting, y explica por qué muchas plataformas todavía aceptan RTMP como entrada aunque distribuyan al público con otros formatos; por ejemplo, Twitch describe explícitamente que el envío hacia su infraestructura se realiza usando RTMP (Twitch Developers, s/f).

En latencia, RTMP suele ubicarse en un rango “bajo” comparado con protocolos segmentados, pero no es ultra-bajo en sentido estricto: en implementaciones reales, es común observar ~2–5 s (2000–5000 ms) de glass-to-glass en configuraciones típicas, muy influido por el buffering del reproductor y por la estabilidad de la red (Roy (Whalen), 2024).

Además, varios stacks incorporan buffers explícitos del lado cliente/encoder: por ejemplo, en tooling común se expone un “client buffer time” configurable y con valores por defecto del orden de 3000 ms (The FFmpeg developers, s/f-b). Esto es clave para la plantilla: cuando el documento menciona latencias, debe quedar claro que el número final no es una propiedad “fija” del protocolo, sino la resultante del buffering + RTT/jitter + códec + política de retransmisión de TCP.

En cuanto a vigencia y compatibilidad, el motivo principal por el que RTMP persiste es pragmático: es un “idioma común” de ingesta para encoders y plataformas. Sin embargo, para un diseño nuevo orientado a tiempo real, sus límites aparecen rápido ya que, al estar sobre TCP, en presencia de pérdida/jitter el comportamiento de retransmisión puede traducirse en demoras variables (latencia “elástica”), y en general no ofrece, por sí mismo, garantías modernas de resiliencia/recuperación orientadas a tiempo real como las que hoy se buscan con alternativas basadas en UDP (p. ej., SRT/WebRTC en otras secciones). En paralelo, también hay un punto de “futuro del ecosistema”: RTMP tiene una especificación publicada y ampliamente implementada, pero su evolución no siguió una trayectoria de estandarización comparable a los RFCs, y buena parte de su protagonismo histórico estuvo atado a Flash (Adobe, 2021; Parmar & Thornburgh, 2012).

Respecto de códecs, el RTMP “clásico” se consolidó como baseline interoperable en FLV con H.264/AAC, y plataformas documentan RTMP/RTMPS con soporte típico de H.264 como opción compatible (Parmar & Thornburgh, 2012). Aun así, el estado del arte se está moviendo: especificaciones como Enhanced RTMP/Enhanced FLV proponen extensiones (incluida señalización por FOURCC) para habilitar códecs modernos como HEVC y AV1, y tooling ampliamente usado ya lo implementa en escenarios acotados (p. ej., OBS con Enhanced RTMP en beta para YouTube). Por lo tanto, es más preciso afirmar que la limitación es principalmente de interoperabilidad y soporte homogéneo (encoder + servidor + plataforma) que una imposibilidad conceptual absoluta.

Protocolos HTTP adaptativos: HLS, MPEG-DASH y CMAF. Las tecnologías de streaming adaptativo sobre HTTP se consolidaron como estándar para distribuir vídeo a grandes audiencias por su escalabilidad y porque reutilizan infraestructura web existente (CDN, proxies, cachés y firewalls “amigables” con HTTP). En esta familia, HLS y MPEG-DASH comparten la idea central de “segmentar + describir en un manifiesto + descargar por HTTP”, y CMAF aparece como pieza clave para reducir duplicación de contenedores y habilitar variantes de baja latencia. Sin embargo, incluso en sus modos “low latency”, suelen ubicarse en el rango de latencia de pocos segundos, muy por encima de los protocolos de ultra-baja latencia orientados a interactividad estricta.

HTTP Live Streaming (HLS). Define un esquema en el cual el contenido se publica como una secuencia de segmentos (históricamente MPEG-TS, y en implementaciones modernas también fMP4/CMAF) y se expone un manifiesto (playlist M3U8) para que el cliente los descargue y reproduzca en orden (May, 2017a). En su configuración “clásica”, la latencia tiende a ser elevada porque el cliente suele mantener un buffer de seguridad y porque los segmentos suelen tener duraciones de varios segundos; el propio RFC 8216 describe el modelo de “segmentos + playlist” y un comportamiento típico de segmentación que, en la práctica, deriva en latencias del orden de decenas de segundos dependiendo del empaquetado y del reproductor (May, 2017a).

Con Low-Latency HLS (LL-HLS) el objetivo es reducir la latencia sin abandonar HTTP/CDN, principalmente habilitando la entrega “temprana” de contenido antes de que el segmento completo esté terminado. Este comportamiento está especificado en la evolución del estándar, incorporando mecanismos como partial segments (PART), recargas bloqueantes del playlist y señales para “preanunciar” contenido próximo (Pantos, 2025). En términos prácticos, LL-HLS puede configurarse para emitir “partes” muy cortas —por ejemplo, del orden de ~200 ms— que el cliente puede comenzar a consumir apenas se codifican, sin esperar el cierre del segmento completo (Apple Developer, s/f). Importante: esos 200 ms son un tamaño de “parte/chunk” (granularidad de publicación), no la latencia end-to-end total; la latencia final depende también de parámetros como el hold-back del reproductor, el buffer mínimo, la cadencia de actualización del playlist, la latencia de codificación (GOP), y la red. En presentaciones técnicas de Apple sobre LL-HLS se reporta la posibilidad de lograr streaming “casi en vivo” con latencias sub-2s en escenarios optimizados, precisamente gracias a este enfoque de entrega incremental sobre HTTP (Apple Developer, 2019).

MPEG-DASH (ISO/IEC 23009-1). Cuenta con un manifiesto (MPD) que describe representaciones (bitrate/resolución) y el cliente descarga segmentos por HTTP, permitiendo adaptación dinámica. Su modo de baja latencia se apoya en CMAF y en técnicas de entrega temprana (por ejemplo, HTTP chunked transfer) para que el reproductor pueda empezar a consumir el segmento mientras se produce. Documentos de la industria (DASH-IF) definen explícitamente el objetivo de “low-latency service offering” con una latencia objetivo típicamente entre 2 y 10 segundos, manteniendo compatibilidad con CDN y con clientes legacy que seguirían reproduciendo con más delay si no soportan el modo LL (DASH Industry Forum, 2020). Esto vuelve a reforzar la idea clave: en HTTP adaptativo, la baja latencia es “baja” en términos OTT (segundos), no en términos de interactividad estricta (centenas de ms).

CMAF (ISO/IEC 23000-19). No es un protocolo sino un formato contenedor y de segmentación basado en fragmented MP4, pensado para que un mismo set de fragmentos/segmentos sea utilizable tanto por HLS como por DASH, reduciendo duplicaciones y facilitando interoperabilidad. En el contexto de baja latencia, CMAF permite estructurar el contenido en unidades más pequeñas (chunks/fragments) que pueden ser decodificables progresivamente; por ejemplo, en materiales técnicos vinculados a perfiles DVB/DASH se ven parámetros que acotan la duración máxima de un “chunk” a ~500 ms en ciertos esquemas de señalización, nuevamente como granularidad de entrega y no como garantía de latencia end-to-end (Law, 2020). En otras palabras: que el sistema “empaquete” en 200 ms o 500 ms ayuda, pero la latencia total sigue estando dominada por decisiones de pipeline y buffers de reproducción.

Ventajas y limitaciones. HLS/DASH (y sus variantes LL sobre CMAF) siguen siendo imbatibles para distribución masiva y robusta —aprovechan CDNs, se comportan bien con firewalls y permiten bitrate adaptativo—, pero pagan el costo de una latencia que, aún optimizada, suele quedar en pocos segundos.

WebRTC: Ultra-baja latencia para aplicaciones interactivas. Web Real-Time Communication (WebRTC) no es un protocolo único, sino una pila completa de estándares y APIs orientada a comunicación de audio/video en tiempo real, nacida en el contexto del navegador pero extendida hoy a SDKs móviles y servidores. A nivel de estandarización, WebRTC se apoya en un conjunto de especificaciones IETF (por ejemplo, el documento de visión general y la definición de transportes) y en la API JavaScript normalizada por W3C, que expone primitivas como RTCPeerConnection para establecer sesiones de comunicación con latencias típicamente sub-segundo cuando la red lo permite (World Wide Web Consortium, 2025).

En términos funcionales, WebRTC resuelve “de punta a punta” (en el sentido de la pila de comunicación) tres problemas que otros enfoques suelen delegar a componentes externos: (1) negociación de conectividad en presencia de NAT/firewalls, (2) transporte de medios en tiempo real sobre UDP con control de congestión y métricas de calidad, y (3) cifrado obligatorio del canal de medios. Esta integración es relevante para casos donde la latencia es prioritaria y donde la operación ocurre en redes variables (obra, 4G/5G, Wi-Fi corporativo), porque evita depender de segmentación HTTP y reduce buffering estructural.

La arquitectura base combina señalización (fuera de banda) con transporte de medios. WebRTC utiliza SDP con el modelo offer/answer para describir capacidades (códecs, direcciones, parámetros), pero el “plano de señalización” no está fijado por WebRTC y queda en manos de la aplicación (HTTP, WebSocket, MQTT, etc.). En la práctica, el estándar JSEP define cómo una aplicación JavaScript controla esa máquina de estados de establecimiento y aplica las descripciones SDP a la conexión, manteniendo la flexibilidad de integrar WebRTC en arquitecturas más grandes sin imponer un protocolo de señalización único.

En la capa de conectividad, WebRTC se apoya en ICE para atravesar NAT, usando STUN para descubrir direcciones públicas y TURN como relé cuando no hay ruta directa viable. ICE está estandarizado en RFC 8445 y, además, la especificación de transportes de WebRTC explicita requerimientos de soporte (incluyendo el uso de TURN para escenarios de NATs restrictivos), lo que lo vuelve un “supuesto operativo” del stack y no un agregado opcional.

Respecto de la latencia —bajo el marco conceptual desarrollado en la sección 16.5.1— conviene distinguir dos métricas que suelen confundirse: el RTT de red (ida y vuelta de paquetes, útil para caracterizar conectividad) y la latencia glass-to-glass (captura → codificación → transporte → decodificación → render). En WebRTC pueden observarse RTTs muy bajos en rutas P2P favorables; sin embargo, el desempeño “glass-to-glass” depende principalmente del pipeline extremo a extremo (códec, parámetros del encoder como GOP/B-frames/rate control, jitter buffer y render del receptor). En mediciones experimentales sobre escenarios WebRTC se reportan latencias extremo a extremo del orden de centenas de milisegundos cuando el pipeline está optimizado. Asimismo, en estudios con usuarios reales, una fracción relevante de conexiones P2P alcanza RTTs compatibles con aplicaciones altamente sensibles a sincronización, aunque no es un comportamiento universal porque depende del acceso y de las condiciones de NAT.

En seguridad, WebRTC impone cifrado en el plano de medios como requisito: el establecimiento de claves se hace mediante DTLS y luego el contenido viaja cifrado con SRTP (DTLS-SRTP), lo que elimina configuraciones “sin cifrar” a nivel de medios. La arquitectura y el modelo de amenazas de WebRTC están desarrollados en documentos específicos de seguridad, que además aclaran implicancias prácticas (por ejemplo, exposición de direcciones, consideraciones de privacidad y superficie de ataque). Un matiz relevante para arquitectura: cuando se introduce un servidor intermedio (p. ej., SFU), el cifrado sigue existiendo en los enlaces WebRTC, pero el “extremo” criptográfico puede ser el servidor (no necesariamente un cifrado E2E entre productor y consumidor final), salvo que se implementen mecanismos adicionales a nivel aplicación.

Para simplificar su uso en streaming (ingesta/egreso) sin implementar señalización compleja, surgen perfiles HTTP. WHIP ya está estandarizado como RFC 9725 y define un mecanismo de ingesta WebRTC basado en HTTP que reduce fricción operativa (publicación vía HTTP y negociación asociada).

SRT: Transporte confiable de baja latencia sobre UDP. Secure Reliable Transport (SRT) es un protocolo de transporte para video en vivo diseñado para mantener baja latencia tolerando pérdida, jitter y variaciones de ancho de banda en redes no confiables. Desarrollado por Haivision y liberado como código abierto en 2017, actualmente es mantenido por la SRT Alliance. Su especificación técnica fue documentada como Internet-Draft en IETF, lo que formaliza su comportamiento y terminología (M. P. Sharabayko et al., 2024).

SRT utiliza UDP como transporte base y agrega una capa de control a nivel de usuario para lograr confiabilidad selectiva. El receptor detecta huecos en la secuencia de paquetes y solicita retransmisiones puntuales mediante NACK (Negative Acknowledgements), un esquema conocido como ARQ selectivo. La diferencia fundamental con TCP radica en que SRT opera con un presupuesto de tiempo configurable, denominado SRT Latency: dentro de esa ventana, el protocolo intenta recuperar paquetes perdidos; si un paquete no puede recuperarse a tiempo, se descarta mediante el mecanismo TLPKTDROP (Too-Late Packet Drop) para mantener la continuidad del flujo. De este modo, la latencia no es un valor fijo universal sino una configuración que se ajusta según las condiciones del enlace, permitiendo latencia acotada y predecible (M. Sharabayko, 2022; M. P. Sharabayko et al., 2024).

En condiciones prácticas, SRT opera con latencias configuradas típicamente entre 120 y 500 ms, pudiendo incrementarse si el RTT es alto o la pérdida significativa. En redes locales de muy baja pérdida puede configurarse más agresivamente, respetando el piso operativo recomendado de aproximadamente 120 ms (M. P. Sharabayko et al., 2024).

En cuanto a conectividad, SRT soporta modos Caller, Listener y Rendezvous, lo que facilita escenarios de despliegue detrás de NAT o firewalls sin requerir aperturas permanentes de puertos entrantes en todos los extremos. Esto resulta relevante para entornos donde la conectividad depende de routers 4G/5G o redes con reglas de acceso restrictivas (M. P. Sharabayko et al., 2024). Además, SRT incorpora cifrado opcional con AES (128, 192 o 256 bits), proporcionando confidencialidad del contenido en tránsito cuando se habilita (M. P. Sharabayko et al., 2024).

RIST: Estándar abierto para transporte resiliente de video. Reliable Internet Stream Transport (RIST) es una especificación para transporte confiable de video en tiempo real sobre redes IP no administradas, desarrollada por el Video Services Forum (VSF) con un foco explícito en interoperabilidad multivendor. El protocolo se publica como Recomendaciones Técnicas (TR) de acceso público, organizadas en perfiles incrementales: Simple Profile (TR-06-1), Main Profile (TR-06-2) y Advanced Profile (TR-06-3), donde cada perfil agrega capacidades sobre el anterior (Video Services Forum, 2020, 2024).

El punto diferencial de RIST es su elección de base protocolar: se apoya en el ecosistema existente de RTP/RTCP (Schulzrinne et al., 2003b) y añade mecanismos de recuperación de pérdidas de forma interoperable. En el Simple Profile, el enfoque central es un esquema ARQ impulsado por el receptor, donde la pérdida se detecta por discontinuidades en los números de secuencia RTP y se solicitan retransmisiones mediante mensajes NACK a través de RTCP, conforme al perfil de retroalimentación extendido RTP/AVPF (Video Services Forum, 2020, 2024). Esto permite recuperar paquetes perdidos dentro de una ventana temporal definida, evitando convertir el transporte en un flujo perfecto pero excesivamente tardío para reproducción en tiempo real. Al igual que SRT, el diseño busca un equilibrio práctico: recuperar lo recuperable a tiempo y descartar lo que llegue demasiado tarde.

La latencia en RIST, al igual que en SRT, no es una propiedad fija del protocolo sino resultado del presupuesto de buffering y de las condiciones del enlace. La ventana disponible para retransmisión está acotada por la latencia objetivo del pipeline; cuanto mayor es el RTT y la variabilidad, mayor debe ser el buffer para mantener alta tasa de recuperación. En evaluaciones empíricas comparando RIST Simple Profile y SRT bajo condiciones controladas de laboratorio, se observó que ambos protocolos pueden comportarse de manera comparable en recuperación de pérdida y latencia cuando se configuran con presupuestos equivalentes, y que las diferencias prácticas aparecen más por implementación y parametrización que por el mecanismo ARQ en sí (Sonono, 2019).

En comparación con SRT, la discusión práctica se organiza en torno a tres ejes. Primero, la base protocolar: RIST prioriza RTP/RTCP y un modelo de extensiones alineado con estándares del broadcast, mientras que SRT utiliza un stack propio sobre UDP derivado de UDT (M. P. Sharabayko et al., 2024). Segundo, la distribución: RIST incluye soporte explícito para IP multicast y escenarios uno-a-muchos desde su Simple Profile (Video Services Forum, 2020), mientras que SRT se utiliza predominantemente en contribución unicast. Tercero, la seguridad: SRT incorpora cifrado AES integrado a nivel de protocolo, mientras que RIST Main Profile emplea DTLS con autenticación basada en certificados, un enfoque que ofrece mayor granularidad en la gestión de identidades (Video Services Forum, 2024).


#### 15.4.2. Servidores de medios de código abierto para transmisión en baja latencia


##### 15.4.2.1. Roles funcionales del servidor de medios

Un servidor de medios puede desempeñar diferentes funciones según los requisitos del sistema. La literatura y las especificaciones técnicas distinguen roles que afectan tanto la latencia end-to-end como la complejidad computacional.

En particular, clasificaremos estos roles entre (i) aquellos que no requieren decodificar/recodificar y (ii) aquellos que sí implican procesamiento multimedia. Adicionalmente, se considera el rol de gateway como función de interoperabilidad entre protocolos y ecosistemas heterogéneos.


###### 15.4.2.1.1. Roles que no requieren decodificar/recodificar

Relay (retransmisión). En este modo, el servidor actúa como punto de paso que recibe paquetes desde un origen y los reenvía a uno o más destinos sin modificar el contenido multimedia. En arquitecturas WebRTC, este rol se implementa típicamente mediante servidores TURN (Traversal Using Relays around NAT), especificados en el RFC 5766, para habilitar conectividad cuando no existe una ruta directa viable entre extremos (Mahy et al., 2010).

Un relay no introduce retardo por procesamiento de medios (no hay decodificación/recodificación). Sin embargo, puede aumentar la latencia efectiva al agregar un salto adicional en la ruta (tráfico vía relé), sumando tiempo de propagación y overhead de entrada/salida. Por lo tanto, su contribución típica a la latencia es baja en comparación con roles que procesan contenido, aunque queda condicionada por ubicación del relé, congestión y buffering del receptor, factores vinculados con los componentes de transporte y renderizado desarrollados en las secciones 16.5.2.3 y 16.5.2.5.

Selective Forwarding Unit (SFU). SFU es uno de los patrones más utilizados en arquitecturas WebRTC multiparte. Cada cliente publica uno (o pocos) flujos hacia el servidor y la SFU reenvía selectivamente esos flujos a los receptores correspondientes sin decodificar ni transcodificar. En términos de latencia, esto es relevante porque, evitar procesamiento pesado sobre el contenido multimedia, la SFU tiende a no sumar retardos comparables a los de una transcodificación; su impacto se concentra en el salto adicional, el enrutamiento, el manejo de colas y el comportamiento bajo carga.

En el caso de Janus, su concepción como gateway WebRTC modular y extensible habilita el uso en configuraciones tipo SFU mediante plugins (Amirante et al., 2014), y su análisis de performance reporta escenarios de videoconferencia y “webinar” donde el cuello de botella pasa a estar dominado por recursos del servidor y número de conexiones simultáneas (Amirante et al., 2015).

Ahora bien, la performance real de una SFU depende del setup y del perfil de carga. En estudios comparativos realizados con el framework KITE se observaron diferencias claras entre implementaciones bajo campañas controladas: algunas SFU mantienen el RTT bajo durante la rampa de carga y degradan de forma gradual, mientras que otras exhiben incrementos mayores de RTT y/o inestabilidad al alcanzar la carga objetivo (Andre et al., 2018). Asimismo, se ha señalado que métricas como RTT o bitrate constituyen indicadores útiles de estrés y degradación, pero no son equivalentes por sí mismas a la latencia glass-to-glass ni agotan la caracterización de la calidad percibida, la cual puede deteriorarse de forma marcada cuando el bitrate desciende por debajo de ciertos umbrales (Andre et al., 2018).

Transmux (re-empaquetamiento). La operación de transmuxing consiste en cambiar el contenedor o el protocolo de entrega sin modificar los flujos ya codificados de audio y video (es decir, sin decodificar ni recodificar). Por ejemplo, al convertir una ingesta RTMP hacia una salida HLS, el sistema puede re-empaquetar el flujo comprimido en segmentos y manifiestos HLS, manteniendo el códec original (May, 2017; Parmar & Thornburgh, 2012).

Aunque el transmux suele agregar poca sobrecarga computacional por no transcodificar, el paso desde un esquema persistente a uno segmentado puede introducir latencia principalmente por segmentación y buffering del reproductor (May, 2017). En streaming adaptativo, el empaquetamiento dinámico se utiliza para flexibilizar la entrega sin duplicar el costo de codificación y para evitar mantener representaciones pre-empaquetadas en múltiples formatos, con beneficios operativos en escenarios a escala (Bentaleb et al., 2019).


###### 15.4.2.1.2. Roles que sí implican procesamiento multimedia

Transcode (transcodificación). La transcodificación implica la decodificación completa del flujo entrante y su posterior recodificación con parámetros distintos (códec, resolución, tasa de bits o frecuencia de cuadros). En sistemas de tiempo real, introduce procesamiento directo sobre el contenido, con impacto material en el retardo. La transcodificación tiene como objetivos centrales: (i) aprovechar información del bitstream original, (ii) preservar calidad visual cerca a una codificación directa desde la fuente y (iii) minimizar retardo y memoria para cumplir requisitos de tiempo real (Ahmad et al., 2005).

En cuanto a latencia, la transcodificación suele convertirse en uno de los aportes dominantes cuando el pipeline exige recodificar en línea. El retardo agregado depende de la complejidad del códec, la resolución, la estructura del GOP y los recursos de hardware. Algunos documentos muestran que la aceleración por hardware permite sostener altas tasas de procesamiento con latencias más controladas que implementaciones puramente en software, y que decisiones de codificación como el uso de B-frames tienden a aumentar la latencia, mientras GOPs más cortos pueden reducir retardo a costa de menor eficiencia de compresión.


###### 15.4.2.1.3. Interoperabilidad

Gateway (pasarela). Un gateway de medios actúa como puente entre distintos protocolos, redes o tecnologías, habilitando interoperabilidad cuando fuentes y consumidores no comparten el mismo transporte o señalización. En WebRTC, Janus fue concebido explícitamente como gateway de propósito general para interconectar clientes WebRTC con tecnologías de tiempo real heredadas mediante una arquitectura modular basada en plugins (Amirante et al., 2014).

Este rol es particularmente relevante cuando se integran fuentes legacy —por ejemplo, cámaras IP que exponen RTSP en ecosistemas ONVIF— con consumidores modernos en navegador, donde WebRTC suele ser el mecanismo natural para interacción en tiempo real (ONVIF, 2019; Schulzrinne et al., 1998b). Desde la perspectiva de latencia end-to-end, el impacto del gateway depende de qué transformación realice: puede limitarse a señalización y reenvío, o incorporar transmux/transcodificación según el caso, alterando sustancialmente su contribución al retardo total.


##### 15.4.2.2. Capacidades transversales y operación

Además de los roles funcionales, en sistemas de transmisión de baja latencia la operación diaria del servidor de medios exige capacidades transversales para diagnosticar degradaciones, validar supuestos de configuración y sostener objetivos bajo carga. Entre ellas, la observabilidad resulta clave porque vincula métricas del servidor y de la red con el comportamiento de protocolos y topologías discutidos en las secciones anteriores.


###### 15.4.2.2.1. Observabilidad y monitoreo

Los servidores de medios contemporáneos suelen incorporar capacidades de observabilidad para monitorear el estado del sistema en tiempo real y facilitar diagnóstico operativo.

Un ejemplo representativo de esto es Kurento, el cual expone métricas y estadísticas mediante APIs programables, facilitando integración con sistemas de monitoreo externos. Entre las señales típicas se incluyen: flujos/sesiones activas, utilización de CPU/memoria, indicadores de desempeño del pipeline y eventos de error. Esta información es clave para detectar cuellos de botella, validar configuraciones de buffers y sostener objetivos de latencia bajo distintas condiciones de carga (Garcia et al., 2017).


##### 15.4.2.3. Patrones de despliegue

La ubicación física del servidor de medios respecto a las fuentes de video y a los consumidores finales tiene un impacto directo sobre la latencia end-to-end del sistema . En particular, el emplazamiento condiciona el componente de red (propagación + jitter + pérdida), la necesidad de buffers para estabilizar la reproducción/análisis y, por ende, el grado en que resulta viable sostener perfiles de ultra-baja latencia con los protocolos discutidos anteriormente. Con base en la literatura de edge computing, es útil organizar el análisis en tres patrones: despliegue en el borde, centralizado en nube y un enfoque híbrido edge-cloud.

Despliegue en el borde (Edge). El paradigma de Multi-access Edge Computing (MEC) propone ubicar cómputo y almacenamiento en proximidad a usuarios/dispositivos, reduciendo la distancia física del tramo crítico y, por lo tanto, la latencia asociada al transporte hacia un centro remoto (Filali et al., 2020). En surveys de MEC y offloading se destaca que la reducción de latencia es uno de los objetivos de QoS más recurrentes en la literatura, precisamente por la sensibilidad de aplicaciones interactivas y “casi en tiempo real” a demoras y variabilidad de red (Mach & Becvar, 2017).

En el caso de streaming, esta proximidad se vuelve particularmente relevante por la intensidad de tráfico. Los requisitos de bitrate para video de muy alta resolución pueden escalar a órdenes elevados (por ejemplo, rangos típicos reportados de ~20–50 Mbps para 4K y ~50–200 Mbps para 8K, según supuestos y configuraciones), lo que refuerza el valor de procesar cerca de la fuente para evitar que enlaces WAN se conviertan en cuello de botella (Khan et al., 2022). Para videovigilancia/visión por computadora en tiempo real, un nodo edge también reduce la dependencia de conectividad hacia la nube central en el tramo donde se requieren decisiones rápidas, ayudando a sostener objetivos estrictos de latencia operacional.

Adicionalmente, la literatura muestra estrategias específicas para “hacer viable” edge cuando hay restricciones de recursos. Existe un enfoque de transcodificación liviana en el borde, orientado a reducir costo computacional y tráfico de red asociado, lo que es consistente con el objetivo de reservar el presupuesto de latencia para el pipeline crítico (captura-codificación-red-procesamiento-alerta) y no consumir innecesariamente en transporte a un cloud remoto (Erfanian et al., 2021).

Despliegue centralizado (Cloud). En el modelo centralizado, los servidores de medios residen en centros de datos remotos operados por proveedores cloud. Este enfoque simplifica operación (consolidación, elasticidad y administración), pero agrega latencia por distancia geográfica y por la variabilidad típica de enlaces de acceso hacia la nube. En consecuencia, para requerimientos de ultra-baja latencia, la literatura de MEC suele contrastar este patrón con edge indicando que el acceso a nubes centralizadas introduce retardos estructurales que pueden ser problemáticos para cargas altamente sensibles a la latencia (Filali et al., 2020).

Dicho esto, el modelo centralizado sigue siendo apropiado cuando el caso de uso tolera mayor latencia: almacenamiento de grabaciones, analítica diferida, enriquecimiento histórico, o distribución a audiencias amplias mediante mecanismos tolerantes a segundos. En un diseño modular, esto permite separar explícitamente el “plano crítico” de detección/alerta (sensitivo a ms) de funciones cloud que priorizan escala y persistencia.

Despliegue híbrido (Edge-Cloud). Las arquitecturas híbridas combinan nodos edge para el procesamiento sensible a la latencia con recursos cloud para funciones que requieren mayor capacidad elástica o almacenamiento a largo plazo. En la práctica, propuestas de edge-assisted para tareas de visión por computadora buscan precisamente repartir el pipeline para cumplir restricciones de “tiempo real” en el borde, dejando al cloud tareas menos urgentes o más pesadas (L. Liu et al., 2019).


##### 15.4.2.4. Impacto en latencia y gestión de buffers

Como se mencionó anteriormente, la latencia end-to-end resulta de la suma de contribuciones de las etapas a lo largo de todo el pipeline. En consecuencia, cuando en esta sección se discuten “latencias” asociadas a un componente (p. ej., el servidor), deben interpretarse como una porción del retardo total.

En roles que no procesan el contenido multimedia, la contribución del servidor tiende a ser baja en comparación con etapas como codificación/decodificación, porque el servidor se limita a recibir y reenviar paquetes sin recodificar (Amirante et al., 2015). Aun así, el retardo efectivo puede aumentar por factores “sistémicos” como un salto adicional en la ruta o colas internas bajo carga.

Cuando el servidor asume roles de procesamiento o adaptación del flujo, la contribución a la latencia puede volverse material. En particular, en escenarios donde el sistema pasa de un esquema continuo a uno segmentado, la latencia final suele quedar dominada por la segmentación y por las políticas de buffering del reproductor, más que por el costo computacional del servidor (Bentaleb et al., 2019; May, 2017b). La transcodificación, por su parte, requiere decodificación completa y recodificación, por lo que suele ser la operación más demandante del pipeline y puede agregar desde cientos de milisegundos hasta varios segundos según códec, resolución, estructura de GOP y hardware disponible (Ahmad et al., 2005; Li et al., 2019; Žádník et al., 2022).

La gestión de buffers es el otro factor crítico que condiciona la latencia percibida. Cada milisegundo de buffer “comprado” para estabilidad incrementa la latencia end-to-end. Por eso, si el caso de uso exige respuesta humana rápida, el problema no es “eliminar buffers”, sino presupuestarlos: definir un presupuesto de latencia total y repartirlo explícitamente entre codificación, red/recuperación y reproducción, validándolo con mediciones glass-to-glass y no solo con métricas de red como RTT.

En términos de orden de magnitud, como referencia para sistemas human-in-the-loop, se reporta que latencias constantes por debajo de ~300 ms pueden ser manejables, mientras que a partir de ese umbral se vuelve significativamente más difícil mantener operación en tiempo real en tareas de control remoto.


##### 15.4.2.5. Servidores de medios de código abierto

El ecosistema de servidores de medios de código abierto reúne herramientas con perfiles técnicos distintos: (a) gateways/SFUs WebRTC orientados a interactividad y baja latencia, (b) servidores con pipelines de procesamiento multimedia integrables (útiles cuando se evalúa procesamiento “en el plano de medios”), y (c) routers/gateways multiprotocolo pensados para compatibilidad y operación liviana, además de alternativas enfocadas en broadcasting con salidas WebRTC y/o LL-HLS. Estas opciones se presentan como posibles candidatos a evaluar en etapas posteriores.

Janus WebRTC Gateway. Janus es un gateway WebRTC modular que, en configuraciones típicas de videoconferencia y distribución interna, implementa un patrón publish/subscribe mediante su plugin VideoRoom, operando como una SFU (Meetecho, s/f). Su diseño por plugins lo vuelve relevante cuando se requiere separar un núcleo de señalización/gestión WebRTC de funcionalidades específicas (p. ej., videoroom, streaming), y su comportamiento bajo carga fue estudiado en distintos escenarios de publicación/suscripción (Ahmad et al., 2005; Amirante et al., 2014, 2015).

Kurento Media Server. Kurento se caracteriza por un enfoque orientado a media pipelines: además de endpoints (p. ej., WebRTC), define “media elements” encadenables para construir grafos de procesamiento. Esta arquitectura resulta pertinente cuando se analiza la alternativa de integrar procesamiento multimedia (p. ej., módulos basados en OpenCV) dentro del pipeline del servidor, en lugar de tratar al servidor como un componente de transporte puro (Garcia et al., 2017; López et al., 2016). Para E-OVRT-VDP, Kurento se ubica naturalmente en el grupo de servidores donde la evaluación debe considerar explícitamente el trade-off entre capacidad de procesamiento y latencia agregada.

MediaMTX. MediaMTX se presenta como un servidor/proxy “zero-dependency” concebido como media router, con capacidad de publicar/leer/proxy/record/playback y de convertir entre protocolos de manera directa (bluenviron, s/f). De acuerdo con su documentación, soporta un conjunto amplio de entradas/salidas típicas para integración (incluyendo RTSP, RTMP, WebRTC, SRT, HLS/LL-HLS, MPEG-TS y RTP), lo que lo posiciona como candidato cuando el objetivo principal es compatibilidad multiprotocolo y operación liviana en escenarios cercanos a las fuentes (bluenviron, s/f; Go Packages, s/f).

OvenMediaEngine. OvenMediaEngine (OME) se presenta como un servidor orientado a baja latencia y escala, con soporte de ingesta multiprotocolo (p. ej., WebRTC, SRT, RTMP, RTSP, MPEG-2 TS) y salidas centradas en WebRTC y LL-HLS (AirenSoft, s/f-a, s/f-b). En su documentación se explicita que LL-HLS apunta a latencias end-to-end del orden de segundos (≈2–5 s) y que el soporte oficial está disponible desde versiones específicas del proyecto (AirenSoft, s/f-a, s/f-b). En un marco de evaluación, OME es relevante cuando se desea comparar un enfoque “broadcast-oriented” que combine una salida ultra-baja latencia (WebRTC) con una salida HTTP de baja latencia (LL-HLS) para compatibilidad.

SRS (Simple Realtime Server). SRS se describe como un servidor de medios de alta eficiencia con soporte para múltiples protocolos de ingestión/entrega (p. ej., RTMP, WebRTC, HLS, HTTP-FLV, SRT, MPEG-DASH, entre otros) y con un rol explícito de media gateway, facilitando conversiones entre protocolos en un modelo publish/subscribe (OSSRS, s/f). Esto lo vuelve candidato cuando se busca evaluar compatibilidad y comparar un “gateway multiprotocolo” frente a alternativas más especializadas (SFU pura, procesamiento embebido, etc.).

Puede verse un análisis comparativo de estos servidores en la Tabla A.3 del Anexo A.


#### 15.4.3. Brechas del estado del arte en el streaming/OVD

Las tecnologías y arquitecturas actuales de streaming presentan un conjunto de limitaciones que condicionan directamente el diseño del pipeline experimental.


##### 15.4.3.1. Ausencia de benchmarks end-to-end integrados para pipelines OVD

La literatura revisada evidencia una fragmentación sistemática en la evaluación de desempeño: los benchmarks de inferencia de modelos OVD (p. ej., AP en COCO/LVIS, FPS en GPU aislada) operan de forma independiente respecto de los benchmarks de streaming (latencia de transporte, throughput de protocolo) y de las métricas de plataformas de edge computing (TOPS, FPS bajo carga térmica). Para una plataforma como E-OVRT-VDP el criterio de selección debe basarse en mediciones reproducibles del pipeline completo, y no extrapolarse directamente de métricas parciales o aisladas.

Esta brecha implica que no existen referentes directos en la literatura que permitan predecir con confianza el desempeño de un sistema que combina ingesta multi-protocolo, decodificación acelerada, inferencia OVD y emisión de eventos bajo restricciones de latencia propias de operación en tiempo real. En consecuencia, la validación empírica del pipeline completo constituye una contribución necesaria del proyecto, y la definición de protocolos de medición reproducibles deberá abordarse como parte del diseño experimental en la etapa 2.


##### 15.4.3.2. Integración de modelos OVD dentro de pipelines de streaming optimizados

Los frameworks de streaming más maduros para video analytics en tiempo real, como NVIDIA DeepStream, han sido históricamente diseñados y optimizados para detectores de clases fijas con arquitecturas convolucionales estándar, cuyos patrones de integración asumen una entrada de imagen y un conjunto predefinido de clases de salida (NVIDIA, 2024). Si bien el ecosistema ha comenzado a incorporar soporte para modelos open-vocabulary —por ejemplo, NVIDIA TAO Toolkit incluye flujos de exportación y despliegue para Grounding DINO (NVIDIA, s/f-g)—, la integración de estos modelos en pipelines de streaming presenta desafíos técnicos que no se resuelven con la misma inmediatez que los detectores convencionales.

En particular, la conversión de modelos OVD a formatos optimizados como TensorRT puede requerir adaptaciones no triviales cuando la arquitectura incluye operadores no soportados nativamente o componentes dinámicos asociados a la codificación de prompts textuales. Dado que TensorRT no admite entradas de tipo texto, la etapa de tokenización debe separarse del grafo del modelo y gestionarse externamente (NVIDIA, s/f-g), lo que introduce complejidad adicional en el diseño del pipeline. Más ampliamente, la arquitectura multi-modal que caracteriza a los modelos OVD —con un encoder visual y un encoder textual que interactúan mediante mecanismos de fusión— no se alinea directamente con los patrones de integración nativos de los plugins de inferencia estándar de estos frameworks, aunque rutas alternativas como la integración con Triton Inference Server ofrecen mayor flexibilidad al soportar modelos en múltiples formatos y frameworks (NVIDIA, s/f-h). Esta brecha, si bien se está reduciendo, sugiere que la integración de modelos OVD dentro del pipeline de streaming requerirá capas de adaptación específicas cuya complejidad y costo deberán evaluarse empíricamente.


##### 15.4.3.3. Interoperabilidad efectiva entre protocolos heterogéneos

Si bien se estableció un mapa de roles potenciales por familia de protocolos y se analizaron las capacidades de interoperabilidad de servidores de medios de código abierto, la literatura no ofrece evidencia consolidada sobre el overhead real introducido por las pasarelas de protocolo (p. ej., RTSP a WebRTC, RTMP a SRT) en condiciones de operación representativas del caso de uso. La transcodificación, el re-empaquetamiento entre formatos contenedores de medios (p. ej., MPEG-TS, FLV, fMP4) y la adaptación entre pilas de transporte pueden introducir latencias adicionales y puntos de fallo que no se capturan en las especificaciones de protocolo individuales.

Esta brecha resulta relevante en el contexto de E-OVRT-VDP, dado que en entornos reales de obra el parque de cámaras puede exponer flujos mediante protocolos diversos. Si bien el prototipo experimental operará previsiblemente con un conjunto acotado de fuentes y protocolos, la identificación de este vacío en la literatura permite anticipar un factor de complejidad para escenarios de despliegue más amplios y orienta el diseño hacia soluciones que no introduzcan dependencias rígidas con un único protocolo de ingesta.


##### 15.4.3.4. Métricas de evaluación alineadas con objetivos de seguridad laboral

Las métricas estándar de evaluación de sistemas de streaming, tales como latencia media, throughput, tasa de pérdida de paquetes y calidad visual (PSNR/SSIM), no capturan adecuadamente el valor operativo de un sistema orientado a la detección asistiva de riesgos en obra. De manera análoga a lo identificado en la sección de OVD respecto de las métricas de detección, las métricas de streaming convencionales no consideran aspectos como el tiempo transcurrido entre el inicio de una condición de riesgo y la notificación al operador, la continuidad de detección bajo variaciones de calidad del stream, o el impacto diferenciado de artefactos de compresión sobre la detectabilidad de elementos de protección personal.


#### 15.4.4. Síntesis comparativa de protocolos

La Tabla 8 sintetiza las características principales de los protocolos analizados, con énfasis en las dimensiones de mayor relevancia para el diseño del sistema E-OVRT-VDP.

Tabla 8

Comparativa de protocolos de transmisión de video de baja latencia para sistemas de video analítico en tiempo real


| Protocolo | Latencia típica E2E | Transporte base | Modelo de entrega | Resiliencia a pérdida | Cifrado nativo | Caso de uso principal |
| --- | --- | --- | --- | --- | --- | --- |
| RTSP/RTP | ~200–800 ms | UDP (o TCP) | Pull (sesión controlada) | Media (con RTCP) | Opcional (RTSPS) | Cámaras IP industriales, CCTV, entornos LAN controlados |
| RTMP | ~2–5 s | TCP | Push | Alta (TCP garantiza entrega) | Sí (RTMPS/TLS) | Ingesta a plataformas de streaming; encoders hacia servidores |
| HLS / MPEG-DASH | ~5–45 s (LL: ~2–10 s) | HTTP/TCP | Pull (segmentado) | Alta (CDN + HTTP) | Sí (HTTPS) | Distribución masiva de contenido; viewers simultáneos elevados |
| WebRTC | < 500 ms | UDP (SRTP sobre DTLS) | Push/Pull (P2P o SFU) | Media (con NACK/FEC) | Sí (DTLS-SRTP, obligatorio) | Interactividad ultra-baja latencia; videoconferencia; monitoreo P2P |
| SRT | ~120–500 ms (configurable) | UDP + ARQ selectivo | Push o Pull | Alta (ARQ con presupuesto de tiempo) | Sí (AES-128/256) | Contribución broadcast; enlaces WAN no confiables; 4G/5G |
| RIST | ~120–500 ms | RTP + ARQ (RTCP FB) | Push o Pull (multicast posible) | Alta (ARQ + FEC) | Sí (DTLS) | Broadcast profesional; distribución multicast en redes gestionadas |

Nota. Los rangos de latencia E2E reportados son valores típicos dependientes de configuración, no compromisos de los estándares. La latencia final está determinada por el pipeline completo (captura, codificación, transporte, decodificación, inferencia), no únicamente por el protocolo. HLS/DASH LL = Low-Latency HLS / DASH. DTLS-SRTP = combinación de Datagram TLS y Secure RTP (cifrado obligatorio en WebRTC). ARQ = Automatic Repeat reQuest. FEC = Forward Error Correction. Fuente: Elaboración propia basada en Axis Communications AB (2015), DASH Industry Forum (2020), ISO/IEC (2022), Keranen et al. (2018), May (2017), Pantos (2025), Parmar y Thornburgh (2012), Roy (2024), Schulzrinne et al. (1998, 2003, 2016), Sharabayko et al. (2024), Sonono (2019), Video Services Forum (2020, 2024) y World Wide Web Consortium (2025).

La tabla muestra que no existe un protocolo que maximice simultáneamente latencia mínima, alta resiliencia a pérdidas y escalabilidad, lo cual es coherente con el enfoque de diseño de cada estándar, orientado a prioridades diferentes según el contexto de aplicación. En arquitecturas comúnmente adoptadas, esta situación suele abordarse mediante esquemas híbridos que emplean protocolos distintos por tramo del flujo de video: uno para ingesta y transporte desde el origen hacia un servidor o plataforma de medios (en entornos LAN o WAN con distintos niveles de control), y otro para distribución/visualización hacia clientes finales, donde los requerimientos de interactividad, número de usuarios y compatibilidad con navegadores influyen de manera determinante. De forma complementaria, también es habitual que los protocolos HTTP adaptativos (HLS/DASH) se reserven para consumo masivo, reproducción diferida o escenarios donde la prioridad sea la escalabilidad y la tolerancia a variaciones de red, más que la inmediatez. En consecuencia, la evidencia comparativa respalda que la selección de protocolos debe abordarse como una decisión dependiente del escenario y de la infraestructura, y suele validarse mediante pruebas empíricas sobre el pipeline completo (captura, codificación, transporte, decodificación e integración con analítica), antes de su adopción en un sistema específico.


