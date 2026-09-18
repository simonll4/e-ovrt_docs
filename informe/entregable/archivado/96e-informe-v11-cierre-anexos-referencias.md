# 96e — Texto extraído del informe v1.1: §17.4-17.6, cierre, anexos y referencias

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

### 17.4. Implementación del prototipo experimental

[Agregado futuro correspondiente a la Etapa 4]


### 17.5. Evaluación y validación del prototipo

[Agregado futuro correspondiente a la Etapa 5]


### 17.6. Documentación técnica, repositorio y evidencias de cierre

[Agregado futuro correspondiente a la Etapa 6]


## 18. Cierre del Proyecto

[Agregado futuro]


## 19. Anexos


### 19.1. Anexo A - Comparativas técnicas y estado del arte complementario

Tabla A. 1

Síntesis de modelos OVD orientada a prototipado


| Modelo | Familia | Mecanismo V-L | AP Zero-shot | FPS | Licencia |
| --- | --- | --- | --- | --- | --- |
| DINO-X | Transformer | Universal Object Prompt | 59.8 (LVIS) | N/D | Apache-2.0 |
| G-DINO 1.5 Pro | Transformer | Fusión cross-modal profunda | 55.7 (LVIS) | N/D | Apache-2.0 |
| G-DINO 1.5 Edge | Transformer | Fusión cross-modal optimizada | 36.2 (LVIS) | 75.2 (TRT) | Apache-2.0 |
| LLMDet | Transformer+LLM | Co-entrenamiento con LLM | 51.1–52.4 (LVIS) | N/D | Apache-2.0 |
| OV-DINO | Transformer | LASF + UniDI | 50.6 (COCO) | N/D | Apache-2.0 |
| DetCLIPv3 | Transformer | Generativo + VLLM | 48.8 (LVIS) | N/D | N/D |
| OWLv2 L/14 | ViT | Self-training escalable | 44.6 (LVIS rare) | N/D | Apache-2.0 |
| YOLOE-v8-L | One-stage | RepRTA + SAVPE + LRPC | 35.9 (LVIS) | 102.5 (TRT) | AGPL-3.0 |
| YOLO-World-L | One-stage | RepVL-PAN contrastivo | 35.4 (LVIS) | 52.0 (V100) | GPLv3 |
| OmDet-Turbo | Transformer RT | EFH + caching texto | 34.0 (LVIS) | 100.2 (TRT) | Apache-2.0 |
| YOLOE-v8-S | One-stage | RepRTA reparametrizable | 27.9 (LVIS) | 305.8 (TRT) | AGPL-3.0 |
| Florence-2-L | Seq2Seq | Generación condicionada | 37.5 (COCO) | Variable | MIT |

Nota: Las velocidades citadas indican condiciones específicas (hardware GPU: V100, T4 o A100; uso de TensorRT; batch size 1; FP16 y/o caching de texto). Las licencias GPL/AGPL requieren derivar código abierto, limitando la adopción industrial. N/D indica no reportado o no optimizado para tiempo real. Fuente: elaboración propia basada en Ren et al. (2024a, 2024b), Fu et al. (2025), Wang et al. (2024, 2025), Yao et al. (2024), Minderer et al. (2023), Cheng et al. (2024), Zhao et al. (2024) y Xiao et al. (2023).

Tabla A. 2

Métricas de evaluación estándar en seguimiento multi-objeto: características y limitaciones


| Métrica | Qué mide | Fortaleza principal | Limitación principal |
| --- | --- | --- | --- |
| MOTA | Precisión global: penaliza FP, FN e ID switches ponderados sobre el total de ground truth (Bernardin & Stiefelhagen, 2008) | Métrica clásica, simple y ampliamente adoptada para medir el desempeño de detección | Sesgada hacia errores de detección; subestima errores de asociación |
| IDF1 | Consistencia de identidad: F1-score sobre detecciones que mantienen el identificador correcto a lo largo del tiempo (Ristani et al., 2016) | Captura la estabilidad de las identidades asignadas | Ignora mejoras en detección (Ristani et al., 2016); no considera localización espacial (Luiten et al., 2021) |
| HOTA | Balance explícito entre precisión de detección (DetA) y precisión de asociación (AssA), con componente de localización (Luiten et al., 2021) | Métrica integral adoptada por MOTChallenge como estándar de referencia | Mayor complejidad conceptual respecto a MOTA/IDF1, al requerir la interpretación conjunta de sus componentes DetA, AssA y LocA para el diagnóstico de fallos (Luiten et al., 2021) |

Nota. MOTA = Multiple Object Tracking Accuracy. IDF1 = Identification F1-Score. HOTA = Higher Order Tracking Accuracy. DetA = Detection Accuracy. AssA = Association Accuracy. FP = Falsos Positivos. FN = Falsos Negativos. IDSW = ID Switches. GT = Ground Truth. Fuente: Elaboración propia basada en las fuentes citadas (Bernardin & Stiefelhagen, 2008; Luiten et al., 2021; Ristani et al., 2016).

Tabla A. 3

Comparativa de servidores de medios de código abierto


| Servidor | Lenguaje | Rol principal | Protocolos | Transcode | Fortaleza |
| --- | --- | --- | --- | --- | --- |
| Janus | C | SFU/Gateway | WebRTC, SIP | Plugins | Modularidad, documentación académica |
| Kurento | C++ | MCU/ Procesamiento | WebRTC, RTSP, RTP | Sí (integrado) | Integración OpenCV, pipelines |
| MediaMTX | Go | Router/Proxy | RTSP, RTMP, WebRTC, SRT, HLS | No | Ligereza, multi-protocolo |
| OvenMediaEngine | C++ | Origin-Edge | WebRTC, LL-HLS, RTMP | Sí (GPU) | Escalabilidad, baja latencia |
| SRS | C++ | Streaming | RTMP, WebRTC, SRT, HLS | Limitado | Eficiencia, cloud-native |

Nota. Elaboración propia basada en las fuentes tratadas en la sección (Ahmad et al., 2005; AirenSoft, s/f-a, s/f-b; Amirante et al., 2014, 2015; bluenviron, s/f; Garcia et al., 2017; Li et al., 2019; López et al., 2016; Meetecho, s/f; OSSRS, s/f; Žádník et al., 2022).


### 19.2. Anexo B - Infraestructura, nodos y parámetros experimentales

Tabla B. 1

Especificaciones técnicas del Central Processing Node (CPN)


| Componente | Especificación |
| --- | --- |
| Modelo | HP Victus 15 Gaming Laptop 15-FB2024LA (2024) |
| CPU | AMD Ryzen 5 8645HS — arquitectura Zen 4; 6 núcleos / 12 hilos; frecuencia base 4.3 GHz, turbo 5.0 GHz |
| GPU dedicada | NVIDIA GeForce RTX 4060 Laptop — chip AD107; 3072 núcleos CUDA; 96 Tensor Cores (4.ª gen.); 8 GB GDDR6; 128-bit; TGP estimado 75 W |
| Decodificación de video | NVIDIA NVDEC de 5.ª generación integrado en la RTX 4060; soporte por hardware para H.264, H.265/HEVC y AV1 |
| Memoria RAM | 32 GB DDR5-5600 (2 × 16 GB SO-DIMM, Dual Channel) |
| Almacenamiento | 1 TB M.2 PCIe NVMe SSD |
| Sistema operativo | Windows 11 Home Single Language |

Nota. Basado en HP Inc. para la identificación del modelo del equipo, y en Advanced Micro Devices, Inc. y NVIDIA Corporation para las especificaciones de CPU y GPU (Advanced Micro Devices, Inc., s. f.; HP Inc., s. f.; NVIDIA Corporation, s. f.-a, s. f.-b).

Tabla B. 2

Especificaciones técnicas del Edge Node candidato (Luxonis OAK-D Pro PoE)


| Componente | Especificación |
| --- | --- |
| Modelo | Luxonis OAK-D Pro PoE (Series 2) |
| Procesador de visión | RVC2 — 4 TOPS totales de procesamiento (1.4 TOPS para AI) |
| Sensor RGB | Sony IMX378, hasta 12 MP (4056 × 3040), rolling shutter, 78° DFOV / 66° HFOV / 54° VFOV, auto-focus, hasta 60 FPS |
| Sensores estéreo | 2 × OV9282, 1 MP (1280 × 800), global shutter, 89.5° DFOV / 80° HFOV / 55° VFOV, hasta 255 FPS |
| Codificación de video | H.264, H.265 y MJPEG por hardware — hasta 4K/30 FPS y 1080p/60 FPS |
| Percepción IR | IR dot projector para estéreo activo + IR illumination LED para operación en baja o nula iluminación |
| IMU | BNO085, 9 ejes, integrada |
| Conectividad | PoE 802.3af Class 3, 1000BASE-T (1 Gbps); conector M12 para alimentación/datos y M8 para IO auxiliar |
| Consumo máximo | Base + streaming 2.5–3 W, más 0.5 W de circuito PoE; consumo total hasta aproximadamente 7.5 W según carga y subsistemas activos |
| Framework de desarrollo | DepthAI |
| Rango de profundidad | Rango ideal 70 cm–12 m; MinZ ~20 cm en 400P + extended disparity; error absoluto < 2 % por debajo de 4 m, < 4 % entre 4 m y 7 m y < 6 % entre 7 m y 10 m |

Nota. Basado en la página oficial del producto y en la documentación de hardware de OAK-D Pro PoE (Luxonis, s. f.-a, s. f.-b). La cámara utiliza PoE para alimentación y conectividad Gigabit Ethernet, dispone de percepción estéreo activa, iluminación IR y capacidades de procesamiento embebido sobre RVC2. La definición del rol exacto del EN en la topología del Escenario B —captura exclusiva, preprocesamiento o captura con inferencia ligera— se determinará en la Et apa 3.

Tabla B. 3

Stack de software candidato del CPN


| Componente | Especificación | Justificación |
| --- | --- | --- |
| Sistema operativo | Windows 11 Home | Plataforma nativa del CPN; compatibilidad con drivers NVIDIA para arquitectura Ada Lovelace. |
| CUDA / cuDNN | CUDA 12.x — cuDNN 9.x (stack candidato, a confirmar) | Combinación compatible con GPUs NVIDIA Ada Lovelace y con los frameworks de inferencia previstos; las versiones exactas se fijarán durante el setup del entorno. |
| Framework de deep learning | PyTorch | Framework oficial de referencia para Grounding DINO y YOLOE; compatibilidad directa con checkpoints preentrenados y ajustados al dominio. |
| Runtime de optimización (primario) | TensorRT | Runtime candidato de optimización para GPU NVIDIA, pertinente para evaluar configuraciones de baja latencia en el CPN. |
| Runtime de optimización (alternativo) | ONNX Runtime (proveedor CUDA) | Alternativa portable para exportar modelos en formato ONNX y contrastar su desempeño frente a TensorRT. |
| Framework de pipeline (a evaluar) | NVIDIA DeepStream vía WSL2 | Framework candidato, basado en GStreamer y documentado por NVIDIA para ejecución sobre Windows 11 mediante WSL2 con GPUs GeForce/Quadro en modo WDDM; su adopción efectiva se evaluará en la instancia de análisis y diseño arquitectónico frente a otras alternativas del plano de medios. |
| Gestión de entorno | conda o venv (a definir) | Aislamiento de dependencias entre modelos con distintos requisitos de versión. |

Nota. La configuración propuesta debe interpretarse como stack candidato del CPN y no como decisión de implementación ya cerrada. La selección final de versiones, runtimes y framework de pipeline corresponde a la instancia de análisis y diseño arquitectónico, en tanto forma parte del diseño arquitectónico del sistema. La instalación efectiva, integración y verificación de funcionamiento del stack sobre el hardware del CPN corresponden a la implementación del prototipo experimental. La selección de Grounding DINO y YOLOE como modelos candidatos se encuentra alineada con el análisis de modelos OVD, que los ubica como alternativas representativas de distintos compromisos entre expresividad semántica y eficiencia computacional. Asimismo, la separación entre PyTorch nativo, TensorRT y ONNX Runtime resulta consistente con el flujo de transferencia previsto entre el TN y el CPN, donde los checkpoints ajustados se exportan al formato requerido por el runtime de inferencia finalmente adoptado. La mención de DeepStream vía WSL2, TensorRT y ONNX Runtime se apoya en la documentación oficial correspondiente (NVIDIA Corporation, 2026a, 2026b; ONNX Runtime, s. f.).

Tabla B. 4

Especificaciones técnicas del Training Node (TN)


| Componente | Especificación |
| --- | --- |
| Tipo de recurso | Cluster de cómputo institucional (Mendieta, CCAD-UNC) |
| Nodos disponibles | 19 nodos de cómputo con GPU |
| GPU por nodo | 2 × NVIDIA A30 — 24 GB HBM2 cada una; arquitectura Ampere; soporte TF32, FP16, BF16 e INT8 |
| CPU por nodo | 20 núcleos / 20 hilos — Intel Xeon E5-2680 v2 |
| Memoria RAM por nodo | 64 GB |
| Almacenamiento local | 400 GB SSD SATA por nodo |
| Interconexión | 40 Gbps Infiniband QDR |
| Asignación mínima | 1/2 nodo (10 cores, 1 GPU) |
| Rol en el proyecto | Fine-tuning de modelos OVD candidatos sobre datos del dominio de construcción civil |
| Disponibilidad | Acceso institucional asignado al proyecto |

Nota. Especificaciones verificadas para el clúster Mendieta en la tabla oficial de infraestructura de CCAD-UNC, y complementadas con la ficha técnica oficial de NVIDIA A30 para las características de la GPU (Centro de Computación de Alto Desempeño, 2026; NVIDIA Corporation, 2022). La asignación mínima validada explícitamente por la fuente institucional es 1/2 nodo (10 cores, 1 GPU). Los clústeres Mulatona, Eulogia, Serafín y Boogie no presentan GPUs en la tabla comparativa oficial del CCAD, por lo que no son considerados para utilizar en el proyecto.

Tabla B. 5

Stack de software candidato del TN


| Componente | Especificación | Justificación |
| --- | --- | --- |
| Sistema operativo | Linux (distribución del cluster) | Entorno estándar para entrenamiento de modelos sobre GPU en infraestructura HPC. |
| CUDA / cuDNN | CUDA 12.x — cuDNN 9.x (stack candidato, a confirmar) | Combinación compatible con la arquitectura Ampere de las NVIDIA A30 y con frameworks de entrenamiento basados en PyTorch. |
| Framework de entrenamiento | PyTorch + bibliotecas de fine-tuning de cada modelo | Grounding DINO y YOLOE publican sus implementaciones oficiales en PyTorch, lo que favorece compatibilidad con checkpoints y rutinas de ajuste fino. |
| Multi-GPU | DistributedDataParallel (DDP) o equivalente (si la asignación efectiva lo permite) | Las 2 A30 por nodo habilitan entrenamiento distribuido para reducir tiempos de convergencia |

Nota. La configuración consignada debe interpretarse como stack candidato del TN y no como entorno de entrenamiento ya validado. La definición del procedimiento de fine-tuning —incluyendo esquema de ajuste, congelamiento de capas, tasa de aprendizaje, número de épocas y uso o no de entrenamiento distribuido— corresponde a la instancia de análisis y diseño arquitectónico como parte del diseño experimental. La instalación efectiva, integración y verificación de funcionamiento del entorno sobre el clúster corresponden a la implementación del prototipo experimental. Asimismo, cualquier comparación entre variantes zero-shot y fine-tuned exige mantener una baseline explícita y una partición train/eval estrictamente disjunta. Fuentes: Liu et al. (2023); Wang et al. (2025); NVIDIA Corporation (2022); Meta AI (2019).

Tabla B. 6

Parámetros de referencia orientativos del pipeline


| Parámetro | Valor de referencia |
| --- | --- |
| Resolución de captura | 1280 × 720 px (HD). Resolución de referencia del sensor o fuente de video. El pipeline incluye una etapa de preprocesamiento que adapta los frames a la resolución de entrada requerida por el modelo seleccionado; para los modelos actualmente priorizados, ello puede implicar configuraciones del orden de 640 × 640 px en variantes tipo YOLOE y 800 × 1333 px en variantes tipo Grounding DINO. |
| Framerate de captura de referencia | 30 FPS (estimativo). Valor orientativo para la fuente de video; no equivale a los FPS efectivos del pipeline, que dependerán de la latencia de inferencia, del presupuesto G2A y de la configuración de ejecución. |
| Presupuesto de latencia G2A | 50 ms - 250 ms. Presupuesto de referencia definido en el framework de métricas; véase allí su formalización y descomposición operativa. |

Nota. Valores orientativos sujetos a validación experimental en la validación experimental. La distinción entre resolución de captura y resolución de entrada del modelo es relevante: el pipeline incluye una etapa de redimensionamiento que adapta los frames al formato esperado por cada modelo OVD candidato. Elaboración propia.

Tabla B. 7

Topología de red del Escenario B


| Aspecto | Descripción |
| --- | --- |
| Topología | LAN. |
| Protocolo de transmisión | RTSP/RTP sobre UDP como protocolo de referencia para cámaras IP y flujos de video sobre red local; la decisión definitiva de transporte y topología interna corresponde a la instancia de análisis y diseño arquitectónico. |
| Acceso a internet | No disponible durante las pruebas. |
| Restricciones de red | Sin restricciones externas previstas; la configuración efectiva de buffering, transporte y eventual intermediación se definirá en la etapa de diseño. |

Nota. En el marco del proyecto, RTSP/RTP se adopta como referencia por su amplia compatibilidad con cámaras IP y por su adecuación a entornos LAN de videovigilancia y streaming controlado. Esta elección no implica fijar de manera anticipada la topología interna definitiva del pipeline ni descartar otras alternativas de transporte que pudieran resultar pertinentes según la arquitectura que se defina en la instancia de análisis y diseño arquitectónico.


### 19.3. Anexo C - Prompts, datos, datasets, benchmarks y logística

Tabla C. 1

Catálogo de prompts candidatos por condición de riesgo


| Código | Eje de variación | Prompt candidato (inglés) | Estrategia |
| --- | --- | --- | --- |
| CR-01 | Sintáctica | person without hard hat | Frase nominal con negación explícita |
| CR-01 | Especificidad | construction worker without safety helmet | Términos específicos del dominio |
| CR-01 | Estado observable | person with bare head on construction site | Estado resultante, sin negación directa |
| CR-01 | Template | a photo of a hard hat | Template estándar CLIP para detección de presencia |
| CR-01 | Indirecta | hard hat ; person | Detección separada de entidades; relación evaluada externamente |
| CR-02 | Sintáctica | person without reflective vest | Frase nominal con negación |
| CR-02 | Especificidad | worker without high-visibility vest | Vocabulario técnico de seguridad |
| CR-02 | Descripción visual | person without bright colored safety clothing | Descripción visual del atributo ausente |
| CR-02 | Template | a photo of a reflective safety vest | Template estándar CLIP |
| CR-02 | Indirecta | reflective vest ; person | Detección separada de entidades |
| CR-03 | Sintáctica | person on scaffolding without harness | Contexto espacial + negación |
| CR-03 | Especificidad | worker at height without fall protection equipment | Vocabulario técnico ampliado |
| CR-03 | Descompuesta | person on scaffolding ; safety harness ; fall arrest harness | Detección separada de persona en altura y elementos de protección |
| CR-03 | Estado observable | unprotected worker on elevated platform | Estado resultante sin negación explícita del EPP |
| CR-04 | Sintáctica | unprotected edge with person nearby | Entidad compuesta: borde + persona |
| CR-04 | Especificidad | elevated platform without guardrail near workers | Términos de protección colectiva |
| CR-04 | Descompuesta | platform edge ; guardrail ; safety railing ; person at height | Detección de borde, protección colectiva y persona |
| CR-05 (a) | Entidades maquinaria | excavator ; backhoe loader ; dump truck ; crane ; heavy machinery | Entidades de maquinaria a detectar individualmente |
| CR-05 (b) | Entidades humanas | person ; construction worker ; pedestrian | Entidades humanas a detectar individualmente |
| CR-06 (a) | Entidad persona | person ; worker ; pedestrian | Entidad cuya posición se evalúa contra el polígono |
| CR-06 (b) | Elementos auxiliares | restricted area sign ; caution tape ; warning tape ; barrier ; safety cone | Elementos delimitadores de referencia visual |

Nota. Las estrategias “Indirecta” y “Descompuesta” utilizan el separador “;” como notación analítica para indicar consultas independientes al modelo OVD; su materialización concreta depende de la sintaxis admitida por cada detector. Las variaciones “Template” utilizan formulaciones tipo “a photo of a [CLASS]”, alineadas con prácticas habituales de uso de modelos visión-lenguaje preentrenados como CLIP. Para CR-05 y CR-06, al tratarse de condiciones de Nivel 3, no se formulan prompts integrados sino prompts de entidades componentes; la evaluación de la condición completa se realiza en el módulo de razonamiento contextual. En particular, los elementos auxiliares de CR-06 no reemplazan la definición externa del polígono de zona restringida, sino que pueden funcionar como referencias visuales complementarias para experimentos o análisis cualitativo. Fuente: Elaboración propia basada en los ejes de variación de la Sección 17.1.5.4.2 y en los hallazgos de Zhou et al. (2022), Du et al. (2022), Gu et al. (2021) y Radford et al. (2021).

Tabla C. 2 Variables de sensibilidad candidatas para el Environment-Based Evaluation


| Variable | Niveles o condiciones retenidas | Uso dentro del protocolo |
| --- | --- | --- |
| Iluminación | Controlada; mixta; natural cuando el entorno lo permita. | Define condición base y barridos univariados de sensibilidad. |
| Resolución de fuente | 1280 × 720 como base; 1920 × 1080 como variante de sensibilidad si la configuración lo permite. | Estima el costo-beneficio entre visibilidad, carga computacional y estabilidad del pipeline. |
| Distancia cámara-sujeto | Rangos a cerrar en instancia de análisis y diseño arquitectónico según campo visual y tamaño aparente; guía inicial: 5-10 m y 10-20 m. | Permite observar el efecto de escala de objeto sin fijar una geometría de cámara antes del diseño del EBE. |
| Oclusión | Baja y media; la oclusión severa no se adopta como obligación de aceptación. | Tensiona la robustez sin convertir la campaña en irreproducible. |
| Tracker | Deshabilitado y habilitado cuando aplique. | Permite medir el aporte del tracking a estabilidad, persistencia y reducción de falsas alarmas. |
| Matriz de prompts | Conjunto acotado de variantes por condición. | Permite seleccionar y congelar el prompt primario antes de las corridas comparativas finales. |
| Composición del vocabulario activo | Configuraciones pequeñas y medianas, explícitamente documentadas. | Permite medir si la cantidad y tipo de consultas activas impacta precisión, latencia o ambas. |

Nota. El EBE se organiza de manera secuencial: condición base, barridos de sensibilidad y prueba de mayor exigencia sobre la mejor configuración retenida. Los niveles consignados son candidatos de diseño y deberán cerrarse al definir la topología y el espacio físico de prueba.

Tabla C. 3

Síntesis de cobertura conjunta por condición de riesgo


| Condición de riesgo | Nivel de cobertura | N.º de fuentes | Observación |
| --- | --- | --- | --- |
| CR-01 — Persona sin casco | Sólida | 7 | Redundancia alta para casco y ausencia de casco. La cobertura proviene de SH17, SHEL5K, CHV, Pictor-PPE, Construction-PPE, GDUT-HWD y SHWD. |
| CR-02 — Persona sin chaleco | Adecuada | 4 | Cobertura suficiente para evaluación, aunque menos redundante que CR-01. La cobertura principal proviene de SH17, CHV, Pictor-PPE y Construction-PPE. |
| CR-03 — Trabajo en altura sin anticaídas | BRECHA | 0 directas | No se identificó una fuente que combine persona en altura, ausencia de sistema anticaídas y anotación aprovechable de la condición completa. |
| CR-04 — Borde elevado desprotegido | BRECHA | 0 directas | No se identificó una fuente con anotaciones de borde elevado, ausencia de protección colectiva y proximidad de personas. |
| CR-05 — Maquinaria cerca de peatones | Parcial | 1 confirmada + 1 condicionada | SODA aporta entidades y contexto de obra. MOCS también aportaría trabajadores, maquinaria y vehículos. La condición completa requiere razonamiento espacial y, eventualmente, temporal. |
| CR-06 — Persona en zona restringida | Parcial | 1 | SODA aporta elementos contextuales útiles para delimitar zonas o barreras. MOCS podría aportar trabajadores y contexto dinámico. La condición requiere polígono externo y regla espacial. |

Nota. Elaboración propia basada en el mapeo de la Tabla 27. El nivel de cobertura refleja la disponibilidad de clases, entidades o contexto útil dentro del inventario, no la dificultad intrínseca de detección ni la complejidad del razonamiento posterior. El conteo de fuentes distingue entre cobertura directa de la condición, cobertura parcial de entidades o contexto, y apoyo contextual insuficiente para constituir por sí solo una etiqueta nativa del patrón de riesgo.

Tabla C. 4

Compatibilidad de formato de anotación entre datasets candidatos y modelos OVD priorizados


| Dataset | Formato nativo | Grounding DINO (ODVG) | YOLOE / pipeline Ultralytics |
| --- | --- | --- | --- |
| SH17 | YOLO; Pascal VOC a verificar | Medio. Desde YOLO requiere conversión YOLO→COCO→ODVG. Si se confirma Pascal VOC, la ruta alternativa sería VOC→COCO→ODVG.. | Nulo/Bajo. Nulo si se usa el formato YOLO disponible; Bajo sólo si se parte de una versión Pascal VOC verificada. |
| SHEL5K | Pascal VOC | Medio. Requiere conversión VOC→COCO→ODVG. | Bajo. Requiere conversión directa VOC→YOLO. |
| CHV | Formato nativo no validado | Medio. Requiere inspección del paquete y normalización previa a COCO/ODVG. | Medio. Requiere inspección del paquete y eventual conversión a YOLO. |
| Pictor-PPE | Formato nativo no validado | Medio. Requiere inspección de la versión pública disponible y normalización a COCO/ODVG. | Medio. Requiere inspección previa y eventual conversión a YOLO. |
| Construction-PPE | YOLO | Medio. Requiere conversión YOLO→COCO→ODVG. | Nulo. Ya se encuentra en formato nativo del pipeline Ultralytics. |
| GDUT-HWD | Formato nativo a verificar; cajas + label en benchmark SSD/Caffe | Medio. Requiere verificar la estructura efectiva de cajas/labels y normalizar a COCO/ODVG. | Medio. Requiere verificar la estructura efectiva de cajas/labels y convertir a YOLO. |
| SHWD | Pascal VOC | Medio. Requiere conversión VOC→COCO→ODVG. | Bajo. Requiere conversión directa VOC→YOLO. |
| SODA | Pascal VOC | Medio. Requiere conversión VOC→COCO→ODVG. | Bajo. Requiere conversión directa VOC→YOLO. |
| MOCS | Multi-type annotation / formato a verificar | Medio condicionado. Requiere acceso efectivo, inspección del paquete y normalización a COCO/ODVG. | Medio condicionado. Requiere acceso efectivo, inspección del paquete y eventual conversión a YOLO. |

Nota. El esfuerzo se clasifica como Nulo —sin conversión—, Bajo —conversión directa o adaptación menor— o Medio —inspección previa del paquete y/o conversión en dos pasos—. La categoría “Medio condicionado” indica que el esfuerzo técnico no puede cerrarse hasta verificar acceso efectivo, estructura del paquete y términos de uso. Cuando la fuente visible no permite confirmar el formato nativo del dataset, el esfuerzo incluye una etapa previa de inspección antes de la normalización al formato de trabajo.

Tabla C. 5

Estimación de volumen de almacenamiento por dataset candidato


| Dataset | Imágenes | Vol. est. (GB) | Formato destino | Observación |
| --- | --- | --- | --- | --- |
| SH17 | 8.099 | ~3–5 | Nativo: YOLO; Pascal VOC a verificar. Destino: COCO/ODVG y/o YOLO. | Descarga desde repositorio/Kaggle del autor. |
| SHEL5K | 5.000 | ~0,5–1 | Nativo: Pascal VOC. Destino: COCO/ODVG y/o YOLO. | Disponible en Mendeley Data. |
| CHV | 1.330 | ~0,5–1 | Formato nativo a verificar. Destino: COCO/ODVG y/o YOLO. | Revisar estructura del paquete y términos de uso al descargar. |
| Pictor-PPE | 1.472 nominales; ~770–780 públicas | ~0,2–0,5 | Formato nativo a verificar. Destino: COCO/ODVG y/o YOLO. | Verificar alcance exacto de la versión pública antes de descargar. |
| Construction-PPE | 1.416 | ~0,18–0,3 | Nativo: YOLO. Destino: YOLO y, si corresponde, COCO/ODVG. | Disponible vía Ultralytics. |
| GDUT-HWD | 3.174 | ~0,5–1,5 | Formato nativo a verificar. Destino: COCO/ODVG y/o YOLO. | Confirmar estructura efectiva de cajas/labels y alcance de licencia sobre datos descargables. |
| SHWD | 7.581 | ~1–3 | Nativo: Pascal VOC. Destino: COCO/ODVG y/o YOLO. | Requiere conversión para ambos pipelines priorizados. |
| SODA | 19.846 | ~8–12 | Nativo: Pascal VOC. Destino: COCO/ODVG y/o YOLO. | Mayor volumen entre los datasets de acceso directo; filtrar según condición objetivo. |
| MOCS | 41.668 | ~15–25 | Multi-type annotation / formato a verificar. Destino condicionado a inspección del paquete. | Acceso por solicitud previa; no debe computarse como volumen operativo automático hasta confirmar acceso y términos. |
| Total estimado | ~88,9–89,6 mil | ~35–55 | — | Escenario condicionado por acceso efectivo, licencia y tamaño real del paquete entregado. |

Nota. Las estimaciones de almacenamiento son aproximadas y dependen de la resolución de las imágenes, la estructura del paquete descargado, la presencia de máscaras u otros tipos de anotación, y los formatos derivados que se generen en la instancia de análisis y diseño arquitectónico. La columna de imágenes se conserva con finalidad logística, ya que permite dimensionar almacenamiento, descarga, conversión y transferencia, sin reemplazar el análisis de cobertura y aptitud desarrollado en las secciones anteriores.


### 19.4. Anexo D - Métricas, instrumentación y bitácora experimental

Tabla D. 1

Métricas de detección OVD adoptadas para el prototipo experimental


| Métrica | Justificación de adopción | Fuente de referencia | Compromiso |
| --- | --- | --- | --- |
| AP@0.5 | Métrica base e interpretable para comparar variantes zero-shot y ajustadas al dominio; tolera errores moderados de localización y cuenta con soporte extendido en herramientas de evaluación. | Everingham et al. (2010) | Obligatorio |
| AP@[0.5:0.95] | Mantiene comparabilidad con el protocolo COCO-style al promediar AP sobre múltiples umbrales de IoU entre 0.50 y 0.95, pero no condiciona por sí sola las decisiones del prototipo experimental. | Lin et al. (2014) | Deseable |
| NMS-AP | Útil como referencia metodológica para análisis fino de OVD con etiquetas o prompts detallados y negativos duros, donde el AP convencional puede inflarse; excede el alcance operativo del prototipo experimental. | Yao et al. (2024) | Conceptual |
| Precision / Recall | Permite analizar el balance entre falsos positivos y falsos negativos con lectura operativa y desagregación por severidad, siempre que se declare explícitamente el punto operativo o criterio de reporte. | Everingham et al. (2010) | Obligatorio |

Nota. AP = Average Precision. NMS = Non-Maximum Suppression. AP@0.5 y Precision/Recall deben reportarse, como mínimo, para la baseline zero-shot y, cuando exista una variante ajustada al dominio metodológicamente comparable, para dicha variante. Precision/Recall deberá reportarse con el punto operativo o criterio de reporte explícitamente declarado. AP@[0.5:0.95] mantiene comparabilidad académica con el protocolo COCO-style y NMS-AP se conserva como referencia metodológica.

Tabla D. 2

Métricas de seguimiento multiobjeto adoptadas para el prototipo experimental


| Métrica | Justificación de adopción | Fuente de referencia | Compromiso |
| --- | --- | --- | --- |
| HOTA | Métrica integral de MOT valiosa para diagnóstico académico, pero costosa por requerir identidades persistentes. | Luiten et al. (2021) | Deseable |
| DetA / AssA | Submétricas útiles para desagregar si las fallas provienen de detección o asociación, siempre que se calcule HOTA. | Luiten et al. (2021) | Deseable |
| IDF1 | Métrica centrada en consistencia de identidad; útil como contraste complementario sobre subsets MOT bien anotados. | Ristani et al. (2016) | Deseable |
| MOTA | Comparabilidad con literatura legacy de tracking; valor diagnóstico complementario. | Bernardin y Stiefelhagen (2008) | Deseable |
| IDSW / Frag | Indicadores de estabilidad del tracker aplicables sólo sobre subsets con identidades consistentes. | Bernardin y Stiefelhagen (2008) | Deseable |
|  | Mide la reducción de falsas alarmas aportada por el tracking; exige declarar previamente cómo se cuenta un falso positivo. | Operacionalización propia | Obligatorio(*) |

Nota. HOTA = Higher Order Tracking Accuracy. DetA = Detection Accuracy. AssA = Association Accuracy. IDF1 = Identification F1. MOTA = Multiple Object Tracking Accuracy. IDSW = ID switches. Frag = fragmentación de trayectorias. = diferencia de falsos positivos entre corridas equivalentes con y sin tracker. Las métricas MOT basadas en identidades se ejecutarán sólo sobre subsets anotados para ese fin. Si no existe ground truth suficiente o no puede declararse una unidad estable de falso positivo —por frame, por track, por evento o por alerta—, no debe calcularse como métrica cuantitativa. En ese caso, sólo podrá reportarse como análisis exploratorio de estabilidad o como conteo descriptivo de activaciones espurias. (*) Si hay tracker y existe unidad de falso positivo comparable entre corridas.

Tabla D. 3

Métricas de rendimiento del pipeline y uso de recursos


| Métrica | Definición operativa | Formato de reporte | Compromiso | Criterio de estabilidad |
| --- | --- | --- | --- | --- |
| FPS efectivos | Cuadros completamente procesados por segundo al final del pipeline. | Media, P50, P95, P99 y variación | Obligatorio | Período de calentamiento previo y corrida sostenida |
| Latencia G2A | Intervalo entre captura o lectura del frame y disponibilidad del resultado de inferencia. | ms (P50, P95, P99) | Obligatorio | Timestamps monotónicos |
| Jitter | Variabilidad de la latencia entre cuadros consecutivos. | ms (desv. est. / coef. variación) | Deseable | Reportar junto con G2A |
| Uso de VRAM | Memoria de video ocupada por modelo, tensores y buffers. | MB y % | Obligatorio | Sin crecimiento monótono |
| Utilización GPU | Porcentaje de ocupación de la GPU durante la corrida. | % | Deseable | Registrar media y picos |
| Uso de RAM/CPU | Consumo de memoria del sistema y presión sobre CPU del proceso completo. | MB/GB y %CPU | Deseable | Registrar serie temporal |

Nota. G2A = Glass-to-Algorithm. FPS = Frames Per Second. VRAM = Video Random Access Memory. El reporte obligatorio mínimo incluye FPS efectivos, latencia G2A y uso de VRAM. Cuando sea posible, conviene registrar además GPU, RAM y CPU con muestreo periódico durante una corrida sostenida.

Tabla D. 4

Umbrales orientativos por severidad para la lectura operativa de la alerta


| Severidad | máx. orient. | TTFD máx. | SDR mín. orient. | Persistencia orient. | Prioridad FP/FN | Observación |
| --- | --- | --- | --- | --- | --- | --- |
| Crítica | 3-5 s | < 1 s | >= 0.50 | 2-4 s | Minimizar FN | Ventana corta; se prioriza no omitir eventos críticos |
| Alta | 5-10 s | < 3 s | >= 0.60 | 3-5 s | Balance FP/FN | Compromiso entre rapidez de respuesta y estabilidad |
| Media | 10-20 s | < 10 s | >= 0.70 | 5-10 s | Minimizar FP | Puede exigirse mayor evidencia antes de confirmar |

Nota. Los valores indicados son orientativos y se alinean con la lógica de persistencia definida en la taxonomía de condiciones de riesgo, patrones y prompts. La columna máx. orient. refiere al tiempo hasta la alerta confirmada dentro del sistema. Ese valor incluye la ventana funcional de persistencia más el presupuesto computacional del pipeline; por esa razón, excede necesariamente a la persistencia orient. La traducción de persistencia a fotogramas dependerá del throughput efectivo del sistema. La calibración empírica final corresponde a la validación experimental.

Tabla D. 5

Insumos mínimos requeridos antes de iniciar una campaña de medición


| Familia de métricas | Ground truth o insumo | Instrumentación mínima | Herramientas o artefactos | Salida mínima |
| --- | --- | --- | --- | --- |
| Detección (AP, P/R) | Bounding boxes y etiquetas por imagen o frame. | Export de predicciones por corrida. | pycocotools o conversión COCO equivalente. | AP y P/R por variante, con punto operativo o criterio de reporte explícitamente declarado. |
| Tracking (HOTA, DetA / AssA, IDF1, MOTA, IDSW / Frag) | Boxes y track_id persistente por frame. | Export MOT-compatible sobre subset anotado. | TrackEval u otra implementación equivalente. | Métricas MOT sobre subset, con declaración explícita de qué métricas fueron ejecutadas y cuáles no. |
| Pipeline (FPS, , jitter) | No requiere GT semántico. | Timestamps por etapa del pipeline. | Logs internos y scripts de agregación. | P50/P95/P99, promedio y variación. |
| Alerta y patrón (, TTFD, SDR, si aplica) | Inicio anotado de la condición de riesgo, duración o intervalo temporal del evento y criterio de activación del patrón. | Logs con timestamps de primera evidencia positiva, inicio de patrón candidato si corresponde, patrón confirmado, alerta registrada y disponibilidad/notificación si aplica. | Event log del pipeline, bitácora de corrida, export de eventos de patrón y scripts de agregación temporal. | TTFD, SDR y cuando exista evaluación de patrón y alerta registrada; sólo si existe trayecto instrumentado. |
| Recursos (VRAM, GPU, RAM, CPU) | No requiere GT semántico. | Muestreo periódico durante la corrida. | nvidia-smi, psutil u otras herramientas del sistema. | Series temporales y resumen. |
| Alerta (, si aplica, TTFD, SDR) | Inicio del evento, duración, severidad y criterio de activación del patrón. | Logs de detección, evaluación de patrón, confirmación de patrón, alerta registrada y consulta o notificación si aplica. | Motor de evaluación de patrones instrumentado; registro interno de alertas; logs del trayecto de consulta o notificación si aplica. | Tiempos y proporciones por evento, con declaración de métricas no aplicables cuando falte instrumentación. |
| Fine-tuning | Split train/eval disjunto y baseline zero-shot explícita. | Registro de entrenamiento y evaluación. | Logs de entrenamiento y scripts comparativos. | Deltas y costo de entrenamiento, cuando aplique. |

Nota. La ausencia de cualquiera de los insumos requeridos para una familia de métricas debe declararse antes de planificar la campaña experimental. En particular, no corresponde reemplazar ground truth inexistente por estimaciones informales ni interpretar logs incompletos como evidencia suficiente de desempeño. Toda métrica sin insumos mínimos deberá registrarse como no ejecutada o no aplicable, según corresponda.

Tabla D. 6

Campos mínimos recomendados para la bitácora experimental


| Campo | Contenido mínimo recomendado | Uso en la interpretación |
| --- | --- | --- |
| Identificación | Fecha, nombre de la corrida, responsable y objetivo. | Permite rastrear la prueba. |
| Modelo | Nombre, versión, checkpoint y variante zero-shot o fine-tuned. | Vincula resultados con artefactos concretos. |
| Entrada | Dataset o clip, resolución, FPS de origen y protocolo de video. | Contextualiza comparaciones. |
| Parámetros | Umbral, vocabulario activo, NMS, tracker on/off, ventana de persistencia, criterio de activación/desactivación del patrón e histéresis si aplica. | Hace reproducible la corrida y permite interpretar la confirmación o descarte de patrones. |
| Hardware | CPU, GPU, VRAM, RAM y equipo o nodo utilizado. | Permite interpretar latencia y uso de recursos. |
| Entorno de software | Sistema operativo, versiones de runtime, framework, librerías críticas y herramientas de instrumentación. | Permite reproducir la corrida y contextualizar diferencias de rendimiento o compatibilidad. |
| Temporalidad y logs | Fuente temporal declarada, período de calentamiento, duración efectiva de la corrida, ubicación de logs crudos y artefactos de evaluación. | Permite validar trazabilidad temporal y auditar métricas derivadas del pipeline y de alerta. |
| Eventos de patrón y alerta | Timestamps de primera evidencia positiva, inicio de patrón candidato si corresponde, patrón confirmado, alerta registrada y notificación o consulta si aplica; identificador del patrón y regla aplicada. | Permite reconstruir por qué y cuándo una detección se transformó en patrón confirmado y alerta registrada. |
| Resultados | Métricas calculadas, unidades y métricas no ejecutadas. | Consolida la salida cuantitativa. |
| Observaciones | Errores, cuellos de botella y cambios no planificados. | Evita lecturas descontextualizadas. |

Nota. Una métrica sin contexto de corrida pierde interpretabilidad y trazabilidad.


## Referencias

Abdalwhab, A. B. M., Imran, A., Heydarian, S., Iordanova, I., & St-Onge, D. (2025). Are open-vocabulary models ready for detection of MEP elements on construction sites? In Proceedings of the 42nd International Symposium on Automation and Robotics in Construction (pp. 1421–1424). International Association for Automation and Robotics in Construction. https://doi.org/10.22260/ISARC2025/0184

Active Silicon Ltd. (2025). Obtaining the lowest latency from your Harrier AF-Zoom IP camera (Technical Report Technical Note 015 (TN015)). Active Silicon. https://www.activesilicon.com/wp-content/uploads/TECH-NOTE-Harrier-IP-Lowest-Latency-Guide.pdf

Adobe. (2021, enero 13). Adobe Flash Player EOL General Information. https://www.adobe.com/hk_en/products/flashplayer/end-of-life-alternative.html

Advanced Micro Devices, Inc. (s. f.). AMD Ryzen 5 8645HS. https://www.amd.com/en/products/processors/laptop/ryzen/8000-series/amd-ryzen-5-8645hs.html

Adžemović, M. (2025). Deep Learning-Based Multi-Object Tracking: A Comprehensive Survey from Foundations to State-of-the-Art (arXiv:2506.13457). arXiv. https://doi.org/10.48550/arXiv.2506.13457

Agencia de Acceso a la Información Pública. (s. f.-a). Conocé tus derechos respecto a tus datos personales. Argentina.gob.ar. Recuperado el 12 de enero de 2026, de https://www.argentina.gob.ar/aaip/datospersonales/derechos

Agencia de Acceso a la Información Pública. (s. f.-b). Videovigilancia: ¿Por qué hay que registrar bases de datos de videovigilancia y presentar el manual de tratamiento? Argentina.gob.ar. Recuperado el 12 de enero de 2026, de https://www.argentina.gob.ar/aaip/datospersonales/responsables/videovigilancia

Aharon, N., Orfaig, R., & Bobrovsky, B.-Z. (2022). BoT-SORT: Robust Associations Multi-Pedestrian Tracking (arXiv:2206.14651). arXiv. https://doi.org/10.48550/arXiv.2206.14651

Ahmad, H. M., y Rahimi, A. (2025). SH17: A dataset for human safety and personal protective equipment detection in manufacturing industry. Journal of Safety Science and Resilience, 6(2), 175–185. https://doi.org/10.1016/j.jnlssr.2024.09.002

Ahmad, I., Xiaohui Wei, Yu Sun, & Ya-Qin Zhang. (2005). Video transcoding: An overview of various techniques and research issues. IEEE Transactions on Multimedia, 7(5), 793–804. https://doi.org/10.1109/TMM.2005.854472

AILab-CVC. (2024, January 30). YOLO-World. GitHub. Retrieved January 21, 2026, from https://github.com/AILab-CVC/YOLO-World

AirenSoft. (s. f.-a). Low-Latency HLS. AirenSoft. OvenMediaEngine Documentation. Recuperado el 8 de enero de 2026, de https://docs.ovenmediaengine.com/streaming/low-latency-hls

AirenSoft. (s. f.-b). OvenMediaEngine: Introduction. AirenSoft. OvenMediaEngine Documentation. Recuperado el 8 de enero de 2026, de https://docs.ovenmediaengine.com/

Amirante, A., Castaldi, T., Miniero, L., & Romano, S. P. (2014). Janus: A general purpose WebRTC gateway. Proceedings of the Conference on Principles, Systems and Applications of IP Telecommunications, 1–8. https://doi.org/10.1145/2670386.2670389

Amirante, A., Castaldi, T., Miniero, L., & Romano, S. P. (2015). Performance analysis of the Janus WebRTC gateway. Proceedings of the 1st Workshop on All-Web Real-Time Systems, 1–7. https://doi.org/10.1145/2749215.2749223

Ananthanarayanan, G., Bahl, P., Bodik, P., Chintalapudi, K., Philipose, M., Ravindranath, L., & Sinha, S. (2017). Real-Time Video Analytics: The Killer App for Edge Computing. Computer, 50(10), 58–67. https://doi.org/10.1109/MC.2017.3641638

Andre, E., Le Breton, N., Lemesle, A., Roux, L., & Gouaillard, A. (2018). Comparative Study of WebRTC Open Source SFUs for Video Conferencing. 2018 Principles, Systems and Applications of IP Telecommunications (IPTComm), 1–8. https://doi.org/10.1109/IPTCOMM.2018.8567642

Apple Developer. (2019). Introducing Low-Latency HLS [Video]. https://developer.apple.com/videos/play/wwdc2019/502/

Apple Developer. (s. f.). Enabling Low-Latency HTTP Live Streaming (HLS). Recuperado https://developer.apple.com/documentation/http-live-streaming/enabling-low-latency-http-live-streaming-hls

Argentina. (2000). Ley N.º 25.326: Ley de Protección de los Datos Personales. Infoleg. https://servicios.infoleg.gob.ar/infolegInternet/anexos/60000-64999/64790/texact.htm

Argentina. (2001, noviembre 29). Decreto 1558/2001: Ley 25.326—Reglamentación. Argentina.gob.ar. https://www.argentina.gob.ar/normativa/nacional/decreto-1558-2001-70368

Argentina. (2006, septiembre 19). Disposición 11/2006: Medidas de seguridad para el tratamiento y conservación de los datos personales. Argentina.gob.ar. https://www.argentina.gob.ar/normativa/nacional/disposici%C3%B3n-11-2006-120120

Argentina. (2015, febrero 24). Disposición 10/2015: Condiciones de licitud para las actividades de recolección y posterior tratamiento de imágenes digitales de personas con fines de seguridad. Argentina.gob.ar. https://www.argentina.gob.ar/normativa/nacional/disposici%C3%B3n-10-2015-243335

Axis Communications AB. (2015). Latency in live network video surveillance (63380/EN/R1/1504) [White paper]. https://www.axis.com/dam/public/9d/e4/5d/latency-in-live-network-video-surveillance-en-US-190945.pdf

Bachhuber, C., Steinbach, E., Freundl, M., & Reisslein, M. (2018). On the Minimization of Glass-to-Glass and Glass-to-Algorithm Delay in Video Communication. IEEE Transactions on Multimedia, 20(1), 238–252. https://doi.org/10.1109/TMM.2017.2726189

Badidi, E., Moumane, K., & Ghazi, F. E. (2023). Opportunities, Applications, and Challenges of Edge-AI Enabled Video Analytics in Smart Cities: A Systematic Review. IEEE Access, 11, 80543–80572. https://doi.org/10.1109/ACCESS.2023.3300658

Bar-Shalom, Y., Fortmann, T. E., & Cable, P. G. (1990). Tracking and Data Association. The Journal of the Acoustical Society of America, 87(2), 918–919. https://doi.org/10.1121/1.398863

Bar-Shalom, Y., Willett, P. K., & Tian, X. (2011). Tracking and data fusion: A handbook of algorithms. YBS Publishing.

Bass, L., Clements, P., & Kazman, R. (2022). Software architecture in practice (Fourth edition). Addison-Wesley.

Bentaleb, A., Taani, B., Begen, A. C., Timmerer, C., & Zimmermann, R. (2019). A Survey on Bitrate Adaptation Schemes for Streaming Media Over HTTP. IEEE Communications Surveys & Tutorials, 21(1), 562–585. https://doi.org/10.1109/COMST.2018.2862938

Bernardin, K., & Stiefelhagen, R. (2008). Evaluating multiple object tracking performance: The CLEAR MOT metrics. EURASIP Journal on Image and Video Processing, 2008(1), 1-10. https://doi.org/10.1155/2008/246309

Bewley, A., Ge, Z., Ott, L., Ramos, F., y Upcroft, B. (2016). Simple online and realtime tracking. En 2016 IEEE International Conference on Image Processing (ICIP) (pp. 3464-3468). IEEE. https://doi.org/10.1109/ICIP.2016.7533003

Bianchi, L., Carrara, F., Messina, N., Gennaro, C., & Falchi, F. (2024). The devil is in the fine-grained details: Evaluating open-vocabulary object detectors for fine-grained understanding. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 22520-22529). https://doi.org/10.1109/CVPR52733.2024.02125

bluenviron. (s. f.). MediaMTX [Software]. GitHub. Recuperado el 8 de enero de 2026, de https://github.com/bluenviron/mediamtx

Bonomi, F., Milito, R., Zhu, J., & Addepalli, S. (2012). Fog computing and its role in the internet of things. Proceedings of the First Edition of the MCC Workshop on Mobile Cloud Computing, 13–16. https://doi.org/10.1145/2342509.2342513

Bossen, F., Bross, B., Suhring, K., & Flynn, D. (2012). HEVC Complexity and Implementation Analysis. IEEE Transactions on Circuits and Systems for Video Technology, 22(12), 1685–1696. https://doi.org/10.1109/TCSVT.2012.2221255

Buslaev, A., Iglovikov, V. I., Khvedchenya, E., Parinov, A., Druzhinin, M., y Kalinin, A. A. (2020). Albumentations: Fast and flexible image augmentations. Information, 11(2), 125. https://doi.org/10.3390/info11020125

Cao, J., Pang, J., Weng, X., Khirodkar, R., & Kitani, K. (2023). Observation-Centric SORT: Rethinking SORT for Robust Multi-Object Tracking. 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 9686–9696. https://doi.org/10.1109/CVPR52729.2023.00934

Card, S. K., Moran, T. P., & Newell, A. (2008). The psychology of human-computer interaction (Repr). Erlbaum.

Carion, N., Massa, F., Synnaeve, G., Usunier, N., Kirillov, A., & Zagoruyko, S. (2020). End-to-End Object Detection with Transformers (arXiv:2005.12872). arXiv. https://doi.org/10.48550/arXiv.2005.12872

Centro de Computación de Alto Desempeño. (2026, 10 de abril). Clusters disponibles. UNC Supercómputo. https://wiki.ccad.unc.edu.ar/infra/clusters.html

Changpinyo, S., Sharma, P., Ding, N., & Soricut, R. (2021). Conceptual 12M: Pushing web-scale image-text pre-training to recognize long-tail visual concepts. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 3557–3567). https://doi.org/10.1109/CVPR46437.2021.00356

Chen, J., & Ran, X. (2019). Deep Learning With Edge Computing: A Review. Proceedings of the IEEE, 107(8), 1655–1674. https://doi.org/10.1109/JPROC.2019.2921977

Cheng, T., Song, L., Ge, Y., Liu, W., Wang, X., & Shan, Y. (2024). YOLO-World: Real-time open-vocabulary object detection. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 16901–16911). https://doi.org/10.1109/CVPR52733.2024.01599

Clark, A., Singh, V., & Wu, Q. (2013). RTP Control Protocol (RTCP) Extended Report (XR) Block for De-Jitter Buffer Metric Reporting (No. RFC7005; p. RFC7005). RFC Editor. https://doi.org/10.17487/rfc7005

Cohen, J. (1960). A coefficient of agreement for nominal scales. Educational and Psychological Measurement, 20(1), 37–46. https://doi.org/10.1177/001316446002000104

Cugola, G., & Margara, A. (2012). Processing flows of information: From data stream to complex event processing. ACM Computing Surveys, 44(3), 1–62. https://doi.org/10.1145/2187671.2187677

Dalvi, M., Singh, N., Bhingarde, S., & Chalke, K. (2025). Construction-PPE: Personal Protective Equipment Detection Dataset (Versión 1.0.0) [Dataset]. Ultralytics. https://docs.ultralytics.com/datasets/detect/construction-ppe/

DASH Industry Forum. (2020, marzo 27). Low-latency Modes for DASH. CR-Low-Latency-Live-r8. https://dashif.org/docs/CR-Low-Latency-Live-r8.pdf

Deber, J., Jota, R., Forlines, C., & Wigdor, D. (2015). How Much Faster is Fast Enough?: User Perception of Latency & Latency Improvements in Direct and Indirect Touch. Proceedings of the 33rd Annual ACM Conference on Human Factors in Computing Systems, 1827–1836. https://doi.org/10.1145/2702123.2702300

Decreto 351/79 de 1979. Reglamentación de la Ley 19.587 de Higiene y Seguridad en el Trabajo. (1979, febrero 5). Infoleg. https://servicios.infoleg.gob.ar/infolegInternet/anexos/30000-34999/32030/dto351-1979-anexo1.htm

Decreto 911/96 de 1996. Reglamento de Higiene y Seguridad para la Industria de la Construcción. (1996, 5 de agosto). Infoleg. https://servicios.infoleg.gob.ar/infolegInternet/anexos/35000-39999/38568/texact.htm

Dendorfer, P., Rezatofighi, H., Milan, A., Shi, J., Cremers, D., Reid, I., Roth, S., Schindler, K., & Leal-Taixé, L. (2020). MOT20: A benchmark for multi object tracking in crowded scenes (arXiv:2003.09003). arXiv. https://doi.org/10.48550/arXiv.2003.09003

Deschere, P. (2025, December 9). Introducing Roboflow Rapid: Text prompt to vision model in minutes. Roboflow Blog. Retrieved January 21, 2026, from https://blog.roboflow.com/roboflow-rapid/

Ding, M., Xiao, B., Codella, N., Luo, P., Wang, J., & Yuan, L. (2022, April 7). [2204.03645] DaViT: Dual Attention Vision Transformers. arXiv. Retrieved January 21, 2026, from https://arxiv.org/abs/2204.03645

Du, C., Lin, C., Jin, R., Chai, B., Yao, Y., & Su, S. (2024). Exploring the State-of-the-Art in Multi-Object Tracking: A Comprehensive Survey, Evaluation, Challenges, and Future Directions. Multimedia Tools and Applications, 83(29), 73151–73189. https://doi.org/10.1007/s11042-023-17983-2

Du, Y., Wei, F., Zhang, Z., Shi, M., Gao, Y., & Li, G. (2022). Learning to prompt for open-vocabulary object detection with vision-language model. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 14084-14093). https://doi.org/10.1109/CVPR52688.2022.01369

Duan, R., Deng, H., Tian, M., Deng, Y., y Lin, J. (2022). SODA: A large-scale open site object detection dataset for deep learning in construction. Automation in Construction, 142, 104499. https://doi.org/10.1016/j.autcon.2022.104499

Emami, P., Pardalos, P. M., Elefteriadou, L., & Ranka, S. (2021). Machine Learning Methods for Data Association in Multi-Object Tracking. ACM Computing Surveys, 53(4), 1–34. https://doi.org/10.1145/3394659

Erfanian, A., Amirpour, H., Tashtarian, F., Timmerer, C., & Hellwagner, H. (2021). LwTE: Light-Weight Transcoding at the Edge. IEEE Access, 9, 112276–112289. https://doi.org/10.1109/ACCESS.2021.3102633

European Data Protection Board. (2020, enero 30). Guidelines 3/2019 on processing of personal data through video devices (Version 2.0). EDPB. https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-32019-processing-personal-data-through-video_en

European Parliament & Council of the European Union. (2016, abril 27). Regulation (EU) 2016/679 (General Data Protection Regulation). EUR-Lex. https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng

Everingham, M., Van Gool, L., Williams, C. K. I., Winn, J., & Zisserman, A. (2010). The Pascal Visual Object Classes (VOC) Challenge. International Journal of Computer Vision, 88(2), 303–338. https://doi.org/10.1007/s11263-009-0275-4

Filali, A., Abouaomar, A., Cherkaoui, S., Kobbane, A., & Guizani, M. (2020). Multi-Access Edge Computing: A Survey. IEEE Access, 8, 197017–197046. https://doi.org/10.1109/ACCESS.2020.3034136

Fu, S., Yang, Q., Mo, Q., Yan, J., Wei, X., Meng, J., Xie, X., & Zheng, W.-S. (2025, January 31). [2501.18954] LLMDet: Learning Strong Open-Vocabulary Object Detectors under the Supervision of Large Language Models. arXiv. Retrieved January 21, 2026, from https://arxiv.org/abs/2501.18954

Garcia, B., Lopez-Fernandez, L., Gallego, M., & Gortazar, F. (2017). Kurento: The Swiss Army Knife of WebRTC Media Servers. IEEE Communications Standards Magazine, 1(2), 44–51. https://doi.org/10.1109/MCOMSTD.2017.1700006

Gettys, J., & Nichols, K. (2012). Bufferbloat: Dark buffers in the internet. Communications of the ACM, 55(1), 57–65. https://doi.org/10.1145/2063176.2063196

Go Packages. (s. f.). Mediamtx Command. Recuperado el 8 de enero de 2026, de https://pkg.go.dev/github.com/bluenviron/mediamtx

Google. (2022, May). owlvit-large-patch14. Hugging Face. https://huggingface.co/google/owlvit-large-patch14

Google. (2023, June). owlv2-base-patch16-ensemble. Hugging Face. https://huggingface.co/google/owlv2-base-patch16-ensemble

GStreamer. (s. f.-a). GStreamer application development manual. Recuperado el 12 de febrero de 2026, de https://gstreamer.freedesktop.org/documentation/?gi-language=c

GStreamer. (s. f.-b). shmsink: GStreamer Bad Plugins 1.0 Plugins Reference Manual. Recuperado el 12 de febrero de 2026, de https://www.manpagez.com/html/gst-plugins-bad-plugins-1.0/gst-plugins-bad-plugins-1.0-1.10.0/gst-plugins-bad-plugins-shmsink.php

Gu, X., Lin, T.-Y., Kuo, W., & Cui, Y. (2021). Open-vocabulary object detection via vision and language knowledge distillation. arXiv. https://doi.org/10.48550/arXiv.2104.13921

Gupta, A., Dollár, P., & Girshick, R. (2019). LVIS: A Dataset for Large Vocabulary Instance Segmentation (arXiv:1908.03195). arXiv. https://doi.org/10.48550/arXiv.1908.03195

HP Inc. (s. f.). Victus Gaming Laptop 15-fb2024la (A14LSLA): Todas las especificaciones técnicas. https://www.hp.com/py-es/products/laptops/product-details/product-specifications/2102249493

Hugging Face. (2024, September 25). OmDet-Turbo. Hugging Face. Retrieved January 21, 2026, from https://huggingface.co/docs/transformers/en/model_doc/omdet-turbo

IDEA-Research. (2023, April 6). IDEA-Research / Grounded-Segment-Anything: Grounded-Segment-Anything. GitHub. Retrieved January 21, 2026, from https://github.com/IDEA-Research/Grounded-Segment-Anything

IDEA-Research. (2024, August 1). IDEA-Research/Grounded-SAM-2: Grounded SAM 2: Ground and Track Anything in Videos. GitHub. Retrieved January 21, 2026, from https://github.com/IDEA-Research/Grounded-SAM-2

IDEA-Research. (2024, May 18). IDEA-Research/GroundingDINO: [ECCV 2024] Official implementation of the paper "Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection". GitHub. Retrieved January 21, 2026, from https://github.com/IDEA-Research/GroundingDINO

IDEA-Research. (2024, November 20). IDEA-Research / DINO-X-API: A Unified Vision Model for Open-World Object Detection and Understanding. GitHub. https://github.com/IDEA-Research/DINO-X-API

Intel. (2021). Upgrading from Intel® Media SDK to Intel® oneAPI Video Processing... https://www.intel.com/content/www/us/en/docs/onevpl/upgrade-from-msdk/2021-3/overview.html

Intel. (2022). H.265/HEVC Hardware Encoding and Decoding Support. https://www.intel.com/content/www/us/en/support/articles/000037112.html

Intel. (s. f.-a). Intel® Video Processing Library: Video Codecs. Recuperado https://www.intel.com/content/www/us/en/developer/tools/vpl/overview.html

Intel. (s. f.-b). Intel oneAPI Video Processing Library (oneVPL). Recuperado https://www.intel.com/content/www/us/en/docs/oneapi/programming-guide/2023-1/intel-oneapi-video-processing-library-onevpl.html

Intel. (s. f.-c). Media Capabilities Supported by Intel Hardware. Recuperado https://www.intel.com/content/www/us/en/docs/onevpl/developer-reference-media-intel-hardware/1-1/overview.html

Intel. (s. f.-d). VA-API: Video Acceleration (VA) API. Recuperado https://intel.github.io/libva/

Internet Assigned Numbers Authority. (s. f.). Service Name and Transport Protocol Port Number Registry. Recuperado el 9 de enero de 2026, de https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml

Iorga, M., Feldman, L., Barton, R., Martin, M. J., Goren, N., & Mahmoudi, C. (2018). Fog computing conceptual model (NIST SP 500-325; p. NIST SP 500-325). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.500-325

iSEE-Laboratory. (2025, January 31). iSEE-Laboratory/LLMDet: (CVPR 2025 highlight✨) Official repository of paper "LLMDet: Learning Strong Open-Vocabulary Object Detectors under the Supervision of Large Language Models". GitHub. Retrieved January 21, 2026, from https://github.com/iSEE-Laboratory/LLMDet

ISO. (2018). ISO 45001:2018 Occupational health and safety management systems—Requirements with guidance for use. ISO. https://www.iso.org/standard/63787.html

ISO. (2023). ISO/IEC 42001:2023—Artificial intelligence management system. ISO. https://www.iso.org/standard/42001

ISO/IEC. (2022). Information technology—Dynamic adaptive streaming over HTTP (DASH)—Part 1: Media presentation description and segment formats. ISO/IEC 23009-1:2022. https://www.iso.org/standard/83314.html

Jeong, E., Kim, J., & Ha, S. (2022). TensorRT-Based Framework and Optimization Methodology for Deep Learning Inference on Jetson Boards. ACM Transactions on Embedded Computing Systems, 21(5), 1–26. https://doi.org/10.1145/3508391

Jiang, K., Huang, J., Xie, W., Lei, J., Li, Y., Shao, L., & Lu, S. (2024). Domain adaptation for large-vocabulary object detectors. In Advances in Neural Information Processing Systems, 37 (pp. 75422–75453). https://doi.org/10.52202/079017-2401

Jiang, Q., Li, F., Zeng, Z., Ren, T., Liu, S., & Zhang, L. (2024). T-Rex2: Towards Generic Object Detection via Text-Visual Prompt Synergy (arXiv:2403.14610). arXiv. https://doi.org/10.48550/arXiv.2403.14610

Keranen, A., Holmberg, C., & Rosenberg, J. (2018). Interactive Connectivity Establishment (ICE): A Protocol for Network Address Translator (NAT) Traversal (No. RFC8445; p. RFC8445). RFC Editor. https://doi.org/10.17487/RFC8445

Khan, M. A., Baccour, E., Chkirbene, Z., Erbad, A., Hamila, R., Hamdi, M., & Gabbouj, M. (2022). A Survey on Mobile Edge Computing for Video Streaming: Opportunities and Challenges. IEEE Access, 10, 120514–120550. https://doi.org/10.1109/ACCESS.2022.3220694

Khattak, M. U., Rasheed, H., Maaz, M., Khan, S., & Khan, F. S. (2023). MaPLe: Multi-modal Prompt Learning (arXiv:2210.03117). arXiv. https://doi.org/10.48550/arXiv.2210.03117

Kim, J., Cho, E., Kim, S., & Kim, H. J. (2024). Retrieval-augmented open-vocabulary object detection. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 17427–17436). https://doi.org/10.1109/CVPR52733.2024.01650

Kirillov, A., Mintun, E., Ravi, N., Mao, H., Rolland, C., Gustafson, L., Xiao, T., Whitehead, S., Berg, A. C., Lo, W.-Y., Dollár, P., & Girshick, R. (2023). Segment Anything (arXiv:2304.02643). arXiv. https://doi.org/10.48550/arXiv.2304.02643

Kirkpatrick, J., Pascanu, R., Rabinowitz, N., Veness, J., Desjardins, G., Rusu, A. A., Milan, K., Quan, J., Ramalho, T., Grabska-Barwinska, A., Hassabis, D., Clopath, C., Kumaran, D., & Hadsell, R. (2017). Overcoming catastrophic forgetting in neural networks. Proceedings of the National Academy of Sciences, 114(13), 3521-3526. https://doi.org/10.1073/pnas.1611835114

Kreutz, D., Ramos, F. M. V., Esteves Verissimo, P., Esteve Rothenberg, C., Azodolmolky, S., & Uhlig, S. (2015). Software-Defined Networking: A Comprehensive Survey. Proceedings of the IEEE, 103(1), 14–76. https://doi.org/10.1109/JPROC.2014.2371999

Kuhn, H. W. (1955). The Hungarian method for the assignment problem. Naval Research Logistics Quarterly, 2(1–2), 83–97. https://doi.org/10.1002/nav.3800020109

Kurose, J. F., & Ross, K. W. (2021). Computer networking: A top-down approach (Eighth edition). Pearson.

Law, W. (2020). Meeting live broadcast requirements – the latest on DASH Low Latency [Presentation]. DVB World Online Presentation. https://dvb.org/wp-content/uploads/2020/03/Latest-on-DASH-low-latency.pdf

Ley 19.587 de 1972. Ley de Higiene y Seguridad en el Trabajo. (1972). Infoleg. https://servicios.infoleg.gob.ar/infolegInternet/anexos/15000-19999/17612/norma.htm

Li, L. H., Zhang, P., Zhang, H., Yang, J., Li, C., Zhong, Y., Wang, L., Yuan, L., Zhang, L., Hwang, J.-N., Chang, K.-W., & Gao, J. (2021, December 7). [2112.03857] Grounded Language-Image Pre-training. arXiv. Retrieved January 21, 2026, from https://arxiv.org/abs/2112.03857

Li, S., Danelljan, M., Ding, H., Huang, T. E., & Yu, F. (2022, July 26). Tracking Every Thing in the Wild. arXiv. https://arxiv.org/abs/2207.12978

Li, S., Fischer, T., Ke, L., Ding, H., Danelljan, M., & Yu, F. (2023). OVTrack: Open-Vocabulary Multiple Object Tracking. 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 5567–5577. https://doi.org/10.1109/CVPR52729.2023.00539

Li, S., Ren, H., Xie, X., & Cao, Y. (2025). A Review of Multi‐Object Tracking in Recent Times. IET Computer Vision, 19(1), e70010. https://doi.org/10.1049/cvi2.70010

Li, X., Cho, B., & Xiao, Y. (2022). Balancing Latency and Accuracy on Deep Video Analytics at the Edge. 2022 IEEE 19th Annual Consumer Communications & Networking Conference (CCNC), 299–306. https://doi.org/10.1109/CCNC49033.2022.9700636

Li, X., Salehi, M. A., Joshi, Y., Darwich, M. K., Landreneau, B., & Bayoumi, M. (2019). Performance Analysis and Modeling of Video Transcoding Using Heterogeneous Cloud Services. IEEE Transactions on Parallel and Distributed Systems, 30(4), 910–922. https://doi.org/10.1109/TPDS.2018.2870651

Lin, T.-Y., Maire, M., Belongie, S., Hays, J., Perona, P., Ramanan, D., Dollar, P. y Zitnick, C. L. (2014). Microsoft COCO: Common objects in context. En D. Fleet, T. Pajdla, B. Schiele y T. Tuytelaars (Eds.), Computer Vision - ECCV 2014 (Vol. 8693, pp. 740-755). Springer. https://doi.org/10.1007/978-3-319-10602-1_48

Liu, L., Li, H., & Gruteser, M. (2019). Edge Assisted Real-time Object Detection for Mobile Augmented Reality. The 25th Annual International Conference on Mobile Computing and Networking, 1–16. https://doi.org/10.1145/3300061.3300116

Liu, S., Zeng, Z., Ren, T., Li, F., Zhang, H., Yang, J., Jiang, Q., Li, C., Yang, J., Su, H., Zhu, J., & Zhang, L. (2024). Grounding DINO: Marrying DINO with grounded pre-training for open-set object detection. In Computer Vision - ECCV 2024 (pp. 38-55). Springer. https://doi.org/10.1007/978-3-031-72970-6_3

Long, Z., y Li, W. (2023). Open-GroundingDino [Repositorio de código]. GitHub. https://github.com/longzw1997/Open-GroundingDino

López, L., París, M., Carot, S., García, B., Gallego, M., Gortázar, F., Benítez, R., Santos, J. A., Fernández, D., Vlad, R. T., Gracia, I., & López, F. J. (2016). Kurento: The WebRTC Modular Media Server. Proceedings of the 24th ACM International Conference on Multimedia, 1187–1191. https://doi.org/10.1145/2964284.2973798

Luiten, J., Os̆ep, A., Dendorfer, P., Torr, P., Geiger, A., Leal-Taixé, L., & Leibe, B. (2021). HOTA: A Higher Order Metric for Evaluating Multi-object Tracking. International Journal of Computer Vision, 129(2), 548–578. https://doi.org/10.1007/s11263-020-01375-2

Luo, W., Xing, J., Milan, A., Zhang, X., Liu, W., & Kim, T.-K. (2021). Multiple object tracking: A literature review. Artificial Intelligence, 293, 103448. https://doi.org/10.1016/j.artint.2020.103448

Luxonis. (s. f.-b). OAK-D Pro PoE [Documentación de hardware]. Luxonis Docs. https://docs.luxonis.com/hardware/products/OAK-D%20Pro%20PoE

Mach, P., & Becvar, Z. (2017). Mobile Edge Computing: A Survey on Architecture and Computation Offloading. IEEE Communications Surveys & Tutorials, 19(3), 1628–1656. https://doi.org/10.1109/COMST.2017.2682318

Magalhães, S. C., Santos, F. N., Machado, P., Moreira, A. P., & Dias, J. (2023). Benchmarking Edge Computing Devices for Grape Bunches and Trunks Detection using Accelerated Object Detection Single Shot MultiBox Deep Learning Models. Engineering Applications of Artificial Intelligence, 117, 105604. https://doi.org/10.1016/j.engappai.2022.105604

Mahmud, R., Kotagiri, R., & Buyya, R. (2018). Fog Computing: A Taxonomy, Survey and Future Directions. En B. Di Martino, K.-C. Li, L. T. Yang, & A. Esposito (Eds.), Internet of Everything (pp. 103–130). Springer Singapore. https://doi.org/10.1007/978-981-10-5861-5_5

Mahy, R., Matthews, P., & Rosenberg, J. (2010). Traversal Using Relays around NAT (TURN): Relay Extensions to Session Traversal Utilities for NAT (STUN) (No. RFC5766; p. RFC5766). RFC Editor. https://doi.org/10.17487/rfc5766

Mallick, S. (2025, 3 de junio). Fine-tuning Grounding DINO: Open-vocabulary object detection. LearnOpenCV. https://learnopencv.com/fine-tuning-grounding-dino/

May, W. (2017). HTTP Live Streaming (R. Pantos, Ed.; No. RFC8216; p. RFC8216). RFC Editor. https://doi.org/10.17487/RFC8216

Mazor, M., Moran, R., & Fleming, S. M. (2021). Stage 2 registered report: Metacognitive asymmetries in visual perception. Neuroscience of Consciousness, 2021(1), niab025. https://doi.org/10.1093/nc/niab025

Meetecho. (s. f.). VideoRoom plugin documentation. Meetecho. Janus WebRTC Server Documentation. Recuperado el 8 de enero de 2026, de https://janus.conf.meetecho.com/docs/videoroom

Meinhardt, T., Kirillov, A., Leal-Taixe, L., & Feichtenhofer, C. (2022). TrackFormer: Multi-Object Tracking with Transformers. 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 8834–8844. https://doi.org/10.1109/CVPR52688.2022.00864

Mell, P. M., & Grance, T. (2011). The NIST definition of cloud computing (NIST SP 800-145; 0 ed., p. NIST SP 800-145). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-145

Mesa. (2025). Mesa 25.1.0 Release Notes / 2025-05-07—The Mesa 3D Graphics Library latest documentation. https://docs.mesa3d.org/relnotes/25.1.0.html

Meta AI. (2019). PyTorch [Software]. https://pytorch.org

Microsoft. (2024, June). Florence-2-large. Hugging Face. https://huggingface.co/microsoft/Florence-2-large

Milan, A., Leal-Taixe, L., Reid, I., Roth, S., & Schindler, K. (2016). MOT16: A Benchmark for Multi-Object Tracking (arXiv:1603.00831). arXiv. https://doi.org/10.48550/arXiv.1603.00831

Minderer, M., Gritsenko, A., & Houlsby, N. (2024). Scaling Open-Vocabulary Object Detection (arXiv:2306.09683). arXiv. https://doi.org/10.48550/arXiv.2306.09683

Minderer, M., Gritsenko, A., Stone, A., Neumann, M., Weissenborn, D., Dosovitskiy, A., Mahendran, A., Arnab, A., Dehghani, M., Shen, Z., Wang, X., Zhai, X., Kipf, T., & Houlsby, N. (2022). Simple open-vocabulary object detection with vision transformers. In Computer Vision – ECCV 2022 (pp. 728–755). Springer. https://doi.org/10.1007/978-3-031-20080-9_42

Minott, D., Siddiqui, S., & Haddad, R. J. (2025). Benchmarking Edge AI Platforms: Performance Analysis of NVIDIA Jetson and Raspberry Pi 5 with Coral TPU. SoutheastCon 2025, 1384–1389. https://doi.org/10.1109/SoutheastCon56624.2025.10971592

MLCommons. (2024, marzo 27). New MLPerf Inference Benchmark Results Highlight The Rapid Growth of Generative AI Models. MLCommons. https://mlcommons.org/2024/03/mlperf-inference-v4/

MLCommons. (s. f.-a). Benchmark MLPerf Inference: Datacenter | MLCommons V3.1. MLCommons. Recuperado https://mlcommons.org/benchmarks/inference-datacenter/

MLCommons. (s. f.-b). MLPerf Inference: Edge. MLCommons. MLCommons Benchmarks. Recuperado https://mlcommons.org/benchmarks/inference-edge/

Nakagawa, K., Tsukada, M., Shima, K., & Esaki, H. (2021). WebRTC-based measurement tool for peer-to-peer applications and preliminary findings with real users. Asian Internet Engineering Conference, 1–8. https://doi.org/10.1145/3497777.3498544

Nath, N. D., Behzadan, A. H., y Paal, S. G. (2020). Deep learning for site safety: Real-time detection of personal protective equipment. Automation in Construction, 112, 103085. https://doi.org/10.1016/j.autcon.2020.103085

NVIDIA Corporation. (2022, marzo). NVIDIA A30 data sheet. https://www.nvidia.com/content/dam/en-zz/Solutions/data-center/products/a30-gpu/pdf/a30-datasheet.pdf

NVIDIA Corporation. (2026a). DeepStream on WSL. https://docs.nvidia.com/metropolis/deepstream/dev-guide/text/DS_on_WSL2.html

NVIDIA Corporation. (2026b). Installing TensorRT. https://docs.nvidia.com/deeplearning/tensorrt/latest/installing-tensorrt/installing.html

NVIDIA Corporation. (s. f.-a). Compare GeForce RTX laptops. https://www.nvidia.com/en-us/geforce/laptops/compare/

NVIDIA Corporation. (s. f.-b). NVIDIA Video Codec SDK. https://developer.nvidia.com/video-codec-sdk

NVIDIA. (2022). NVIDIA Jetson AGX Orin series technical brief. NVIDIA. https://www.nvidia.com/content/dam/en-zz/Solutions/gtcf21/jetson-orin/nvidia-jetson-agx-orin-technical-brief.pdf

NVIDIA. (2024). DeepStream SDK 8.0 for NVIDIA dGPU/X86 and Jetson—DeepStream documentation. https://docs.nvidia.com/metropolis/deepstream/dev-guide/text/DS_Release_notes.html

NVIDIA. (2025). Welcome to the DeepStream documentation (DeepStream SDK overview). NVIDIA. NVIDIA DeepStream SDK Developer Guide. https://docs.nvidia.com/metropolis/deepstream/dev-guide/text/DS_Overview.html

NVIDIA. (s. f.-a). Installing PyTorch for Jetson platform. NVIDIA. NVIDIA Deep Learning Frameworks Documentation. Recuperado https://docs.nvidia.com/deeplearning/frameworks/install-pytorch-jetson-platform/index.html

NVIDIA. (s. f.-b). Interprocess Communication—CUDA Programming Guide. Recuperado https://docs.nvidia.com/cuda/cuda-programming-guide/04-special-topics/inter-process-communication.html

NVIDIA. (s. f.-c). JetPack software stack for NVIDIA Jetson. NVIDIA. NVIDIA Developer. Recuperado https://developer.nvidia.com/embedded/jetpack

NVIDIA. (s. f.-d). NVDEC Video Decoder API Programming Guide. Recuperado https://docs.nvidia.com/video-technologies/video-codec-sdk/13.0/nvdec-video-decoder-api-prog-guide/index.html

NVIDIA. (s. f.-e). NVENC Application Note. Recuperado https://docs.nvidia.com/video-technologies/video-codec-sdk/13.0/nvenc-application-note/index.html

NVIDIA. (s. f.-f). Using FFmpeg with NVIDIA GPU Hardware Acceleration. Recuperado https://docs.nvidia.com/video-technologies/video-codec-sdk/13.0/ffmpeg-with-nvidia-gpu/index.html

om-ai-lab. (2024, March 11). OmDet. GitHub. https://github.com/om-ai-lab/OmDet

ONNX Runtime. (s. f.). CUDA Execution Provider. https://onnxruntime.ai/docs/execution-providers/CUDA-ExecutionProvider.html

ONVIF. (2019). ONVIF Profile S Specification (ONVIF Profile S). ONVIF. https://www.onvif.org/wp-content/uploads/2019/12/ONVIF_Profile_-S_Specification_v1-3.pdf

OpenFog Consortium. (2017). OpenFog Reference Architecture for Fog Computing. Industrial Internet Consortium. https://www.iiconsortium.org/pdf/OpenFog_Reference_Architecture_2_09_17.pdf

Organisation for Economic Co-operation and Development. (2019, mayo 1). OECD AI Principles overview. OECD. https://oecd.ai/en/ai-principles

OSSRS. (s. f.). Introduction (SRS documentation). OSSRS. SRS Documentation (v6). Recuperado el 9 de enero de 2026, de https://ossrs.net/lts/en-us/docs/v6/doc/introduction

Otgonbold, M.-E., Gochoo, M., Alnajjar, F. S., Ali, L., Tan, T.-H., Hsieh, J.-W., y Chen, P.-Y. (2022). SHEL5K: An extended dataset and benchmarking for safety helmet detection. Sensors, 22(6), 2315. https://doi.org/10.3390/s22062315

Pantos, R. (2025). HTTP Live Streaming 2nd Edition (Internet-Draft). Internet Engineering Task Force. https://datatracker.ietf.org/doc/draft-pantos-hls-rfc8216bis/18/

Parmar, H., & Thornburgh, M. (2012). Adobe’s Real Time Messaging Protocol. Adobe. https://ptacts.uspto.gov/ptacts/public-informations/petitions/1557060/download-documents?artifactId=CX29dwexemvGTAgu1npsGb4QtKzyjACHSNYXLhjJp5m1SpQS4AAf-3A

Pereira, R., Carvalho, G., Garrote, L., & Nunes, U. J. (2022). Sort and Deep-SORT Based Multi-Object Tracking for Mobile Robotics: Evaluation with New Data Association Metrics. Applied Sciences, 12(3), 1319. https://doi.org/10.3390/app12031319

Pham, H. V., Tran, T. G., Le, C. D., Le, A. D., & Vo, H. B. (2024). Benchmarking Jetson Edge Devices with an End-to-End Video-Based Anomaly Detection System. En K. Arai (Ed.), Advances in Information and Communication (Vol. 920, pp. 358–374). Springer Nature Switzerland. https://doi.org/10.1007/978-3-031-53963-3_25

Potluri, S., Wang, H., Bureddy, D., Singh, A. K., Rosales, C., & Panda, D. K. (2012). Optimizing MPI Communication on Multi-GPU Systems Using CUDA Inter-Process Communication. 2012 IEEE 26th International Parallel and Distributed Processing Symposium Workshops & PhD Forum, 1848–1857. https://doi.org/10.1109/IPDPSW.2012.228

Radford, A., Kim, J. W., Hallacy, C., Ramesh, A., Goh, G., Agarwal, S., Sastry, G., Askell, A., Mishkin, P., Clark, J., Krueger, G., & Sutskever, I. (2021). Learning Transferable Visual Models From Natural Language Supervision (arXiv:2103.00020). arXiv. https://doi.org/10.48550/arXiv.2103.00020

Rakai, L., Song, H., Sun, S., Zhang, W., & Yang, Y. (2022). Data association in multiple object tracking: A survey of recent techniques. Expert Systems with Applications, 192, 116300. https://doi.org/10.1016/j.eswa.2021.116300

Rasaee, H., Koleilat, T., & Rivaz, H. (2025). Grounding DINO-US-SAM: Text-Prompted Multi-Organ Segmentation in Ultrasound with LoRA-Tuned Vision-Language Models. IEEE Transactions on Ultrasonics, Ferroelectrics, and Frequency Control, 72(10), 1414-1425. https://doi.org/10.1109/TUFFC.2025.3605285

Ravi, N., Gabeur, V., Hu, Y.-T., Hu, R., Ryali, C., Ma, T., Khedr, H., Rädle, R., Rolland, C., Gustafson, L., Mintun, E., Pan, J., Alwala, K. V., Carion, N., Wu, C.-Y., Girshick, R., Dollár, P., & Feichtenhofer, C. (2024). SAM 2: Segment Anything in Images and Videos (arXiv:2408.00714). arXiv. https://doi.org/10.48550/arXiv.2408.00714

Reddi, V. J., Cheng, C., Kanter, D., Mattson, P., Schmuelling, G., Wu, C.-J., Anderson, B., Breughe, M., Charlebois, M., Chou, W., Chukka, R., Coleman, C., Davis, S., Deng, P., Diamos, G., Duke, J., Fick, D., Gardner, J. S., Hubara, I., … Zhou, Y. (2020). MLPerf Inference Benchmark (arXiv:1911.02549). arXiv. https://doi.org/10.48550/arXiv.1911.02549

Ren, T., Chen, Y., Jiang, Q., Zeng, Z., Xiong, Y., Liu, W., Ma, Z., Shen, J., Gao, Y., Jiang, X., Chen, X., Song, Z., Zhang, Y., Huang, H., Gao, H., Liu, S., Zhang, H., Li, F., Yu, K., & Zhang, L. (2024, November 21). [2411.14347] DINO-X: A Unified Vision Model for Open-World Object Detection and Understanding. arXiv. Retrieved January 21, 2026, from https://arxiv.org/abs/2411.14347

Ren, T., Jiang, Q., Liu, S., Zeng, Z., Liu, W., Gao, H., Huang, H., Ma, Z., Jiang, X., Chen, Y., Xiong, Y., Zhang, H., Li, F., Tang, P., Yu, K., & Zhang, L. (2024). Grounding DINO 1.5: Advance the “Edge” of Open-Set Object Detection (Versión 2). arXiv. https://doi.org/10.48550/ARXIV.2405.10300

Ren, T., Liu, S., Zeng, A., Lin, J., Li, K., Cao, H., Chen, J., Huang, X., Chen, Y., Yan, F., Zeng, Z., Zhang, H., Li, F., Yang, J., Li, H., Jiang, Q., & Zhang, L. (2024). Grounded SAM: Assembling Open-World Models for Diverse Visual Tasks (arXiv:2401.14159). arXiv. https://doi.org/10.48550/arXiv.2401.14159

Ristani, E., Solera, F., Zou, R., Cucchiara, R., & Tomasi, C. (2016). Performance Measures and a Data Set for Multi-target, Multi-camera Tracking. En G. Hua & H. Jégou (Eds.), Computer Vision – ECCV 2016 Workshops (Vol. 9914, pp. 17–35). Springer International Publishing. https://doi.org/10.1007/978-3-319-48881-3_2

Robicheaux, P., Gallagher, J., Nelson, J., & Robinson, I. (2025, March 20). RF-DETR: A SOTA Real-Time Object Detection Model. Roboflow Blog. Retrieved January 26, 2026, from https://blog.roboflow.com/rf-detr/

Roboflow. (2023). Autodistill [Software]. GitHub. https://github.com/autodistill/autodistill

Roboflow. (2025, November 14). Build a Rapid Model | Roboflow Docs. Roboflow Documentation. Retrieved January 26, 2026, from https://docs.roboflow.com/rapid/build-a-rapid-model

Roboflow. (2025, November 14). What is Roboflow Rapid? Roboflow Docs. https://docs.roboflow.com/rapid/what-is-roboflow-rapid

Roy (Whalen), S. (2024, julio 18). RTMP vs. RTSP: Which Protocol Should You Choose? (Update). Wowza Media Systems. Wowza Blog. https://www.wowza.com/blog/rtmp-vs-rtsp-which-protocol-should-you-choose

Satyanarayanan, M. (2017). The Emergence of Edge Computing. Computer, 50(1), 30–39. https://doi.org/10.1109/MC.2017.9

Schulzrinne, H., Casner, S., Frederick, R., & Jacobson, V. (2003). RTP: A Transport Protocol for Real-Time Applications (No. RFC3550; p. RFC3550). RFC Editor. https://doi.org/10.17487/rfc3550

Schulzrinne, H., Rao, A., & Lanphier, R. (1998). Real Time Streaming Protocol (RTSP) (No. RFC2326; p. RFC2326). RFC Editor. https://doi.org/10.17487/rfc2326

Schulzrinne, H., Rao, A., Lanphier, R., & Westerlund, M. (2016). Real-Time Streaming Protocol Version 2.0 (M. Stiemerling, Ed.; No. RFC7826; p. RFC7826). RFC Editor. https://doi.org/10.17487/RFC7826

Sharabayko, M. (2022, marzo 14). Improving SRT Retransmissions—Experiments with Simulated Live Streaming. Innovation Labs Blog (Medium). https://medium.com/innovation-labs-blog/improving-srt-retransmissions-experiments-with-simulated-live-streaming-part-1-7d192483bba4

Sharabayko, M. P., Sharabayko, M. A., Dube, J., Kim, J., & Kim, J. (2024). The SRT Protocol (Internet-Draft (working copy)). Internet Engineering Task Force. https://haivision.github.io/srt-rfc/draft-sharabayko-srt.html

Sharma, P., Ding, N., Goodman, S., & Soricut, R. (2018). Conceptual captions: A cleaned, hypernymed, image alt-text dataset for automatic image captioning. In Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (pp. 2556–2565). https://doi.org/10.18653/v1/P18-1238

Shen, Y., Fu, C., Chen, P., Zhang, M., Li, K., Sun, X., Wu, Y., Lin, S., & Ji, R. (2023, December 4). Aligning and Prompting Everything All at Once for Universal Visual Perception. arXiv. https://arxiv.org/abs/2312.02153

Shi, W., Cao, J., Zhang, Q., Li, Y., & Xu, L. (2016). Edge Computing: Vision and Challenges. IEEE Internet of Things Journal, 3(5), 637–646. https://doi.org/10.1109/JIOT.2016.2579198

Shim, I., Oh, T.-H., Lee, J.-Y., Choi, J., Choi, D.-G., & Kweon, I. S. (2019). Gradient-Based Camera Exposure Control for Outdoor Mobile Platforms. IEEE Transactions on Circuits and Systems for Video Technology, 29(6), 1569–1583. https://doi.org/10.1109/TCSVT.2018.2846292

Shuvo, Md. M. H., Islam, S. K., Cheng, J., & Morshed, B. I. (2023). Efficient Acceleration of Deep Learning Inference on Resource-Constrained Edge Devices: A Review. Proceedings of the IEEE, 111(1), 42–91. https://doi.org/10.1109/JPROC.2022.3226481

Silvano, C., Ielmini, D., Ferrandi, F., Fiorin, L., Curzel, S., Benini, L., Conti, F., Garofalo, A., Zambelli, C., Calore, E., Schifano, S., Palesi, M., Ascia, G., Patti, D., Petra, N., De Caro, D., Lavagno, L., Urso, T., Cardellini, V., … Perri, S. (2025). A Survey on Deep Learning Hardware Accelerators for Heterogeneous HPC Platforms. ACM Computing Surveys, 57(11), 1–39. https://doi.org/10.1145/3729215

Sonono, T. (2019). Interoperable Retransmission Protocols with Low Latency and Constrained Delay: A Performance Evaluation of RIST and SRT [Master’s thesis, KTH Royal Institute of Technology]. https://www.diva-portal.org/smash/get/diva2:1335907/FULLTEXT01.pdf

SRT. (1997, julio 7). Resolución SRT 51/97 de 1997. Mecanismo Preventivo de Control en Obras de Construcción. Infoleg. https://servicios.infoleg.gob.ar/infolegInternet/anexos/40000-44999/44588/norma.htm

SRT. (1998, marzo 31). Resolución SRT 35/98 de 1998. Coordinación de Programas de Seguridad en Obras de Construcción. Infoleg. https://servicios.infoleg.gob.ar/infolegInternet/anexos/50000-54999/50188/norma.htm

SRT. (s. f.). Programa de Construcción. Argentina.gob.ar. Recuperado el 12 de enero de 2026, de https://www.argentina.gob.ar/srt/prevencion/programas/construccion

Stephen. (2026). elFarto/nvidia-vaapi-driver [C]. https://github.com/elFarto/nvidia-vaapi-driver (Obra original publicada en 2021)

Sullivan, G. J., Ohm, J.-R., Han, W.-J., & Wiegand, T. (2012). Overview of the High Efficiency Video Coding (HEVC) Standard. IEEE Transactions on Circuits and Systems for Video Technology, 22(12), 1649–1668. https://doi.org/10.1109/TCSVT.2012.2221191

Swaminathan, T. P., Silver, C., & Akilan, T. (2024). Benchmarking Deep Learning Models on NVIDIA Jetson Nano for Real-Time Systems: An Empirical Investigation (Versión 1). arXiv. https://doi.org/10.48550/ARXIV.2406.17749

SysCV. (2023, June 18). ovtrack. GitHub. https://github.com/SysCV/ovtrack

The FFmpeg developers. (s. f.-a). Documentación FFmpeg. Recuperado https://ffmpeg.org/about.html

The FFmpeg developers. (s. f.-b). FFmpeg Protocols Documentation. Recuperado https://ffmpeg.org/ffmpeg-protocols.html

The FFmpeg developers. (s. f.-c). HWAccelIntro – FFmpeg. Recuperado el 12 de febrero de 2026, de https://trac.ffmpeg.org/wiki/HWAccelIntro

The Linux Kernel. (s. f.). Buffer Sharing and Synchronization (dma-buf)—The Linux Kernel documentation. Recuperado https://docs.kernel.org/driver-api/dma-buf.html

THU-MIG. (2025). THU-MIG / yoloe: YOLOE: Real-Time Seeing Anything. GitHub. https://github.com/THU-MIG/yoloe

Twitch Developers. (s. f.). Video Broadcast. Twitch Developers. Recuperado el 11 de febrero de 2026, de https://dev.twitch.tv/docs/video-broadcast/

Ucar, A., Ro, S., Satwika, S., Gayathri, P. Y., & Balsha, M. G. (2025). Fine-Tuning Florence2 for Enhanced Object Detection in Un-constructed Environments: Vision-Language Model Approach (arXiv:2503.04918). arXiv. https://doi.org/10.48550/arXiv.2503.04918

United Nations Educational, Scientific and Cultural Organization. (2021, noviembre 1). Recommendation on the Ethics of Artificial Intelligence. UNESCO. https://unesdoc.unesco.org/ark:/48223/pf0000380455

Video Services Forum. (2020). Reliable Internet Stream Transport (RIST) protocol specification – Simple profile. Video Services Forum. https://static.vsf.tv/download/technical_recommendations/VSF_TR-06-1_2020_06_25.pdf

Video Services Forum. (2024). Reliable Internet Stream Transport (RIST) Protocol Specification – Main Profile. Video Services Forum. https://static.vsf.tv/download/technical_recommendations/VSF_TR-06-2_2024_06_12.pdf

Viitanen, M., Vanne, J., Hamalainen, T. D., Gabbouj, M., & Lainema, J. (2012). Complexity analysis of next-generation HEVC decoder. 2012 IEEE International Symposium on Circuits and Systems, 882–885. https://doi.org/10.1109/ISCAS.2012.6272182

Wang, A., Liu, L., Chen, H., Lin, Z., Han, J., & Ding, G. (2025). YOLOE: Real-Time Seeing Anything (arXiv:2503.07465). arXiv. https://doi.org/10.48550/arXiv.2503.07465

Wang, H., Hao, F., Zhu, C., Rodrigues, J. J. P. C., & Yang, L. T. (2012). An Android Multimedia Framework Based on Gstreamer. En J. J. P. C. Rodrigues, L. Zhou, M. Chen, & A. Kailas (Eds.), Green Communications and Networking (Vol. 51, pp. 51–62). Springer Berlin Heidelberg. https://doi.org/10.1007/978-3-642-33368-2_5

Wang, H., Ren, P., Jie, Z., Dong, X., Feng, C., Qian, Y., Ma, L., Jiang, D., Wang, Y., Lan, X., & Liang, X. (2024, July 10). OV-DINO: Unified Open-Vocabulary Detection with Language-Aware Selective Fusion. arXiv. https://arxiv.org/abs/2407.07844

Wang, H., Zhang, X., Chen, H., Xu, Y., & Ma, Z. (2022). Inferring End-to-End Latency in Live Videos. IEEE Transactions on Broadcasting, 68(2), 517–529. https://doi.org/10.1109/TBC.2021.3071060

Wang, X., Han, Y., Leung, V. C. M., Niyato, D., Yan, X., & Chen, X. (2020). Convergence of Edge Computing and Deep Learning: A Comprehensive Survey. IEEE Communications Surveys & Tutorials, 22(2), 869–904. https://doi.org/10.1109/COMST.2020.2970550

Wang, Z., Wu, Y., Yang, L., Thirunavukarasu, A., Evison, C., y Zhao, Y. (2021). Fast personal protective equipment detection for real construction sites using deep learning approaches. Sensors, 21(10), 3478. https://doi.org/10.3390/s21103478

Wiegand, T., Sullivan, G. J., Bjontegaard, G., & Luthra, A. (2003). Overview of the H.264/AVC video coding standard. IEEE Transactions on Circuits and Systems for Video Technology, 13(7), 560–576. https://doi.org/10.1109/TCSVT.2003.815165

Wojke, N., Bewley, A., & Paulus, D. (2017). Simple online and realtime tracking with a deep association metric. 2017 IEEE International Conference on Image Processing (ICIP), 3645–3649. https://doi.org/10.1109/ICIP.2017.8296962

World Wide Web Consortium. (2025). WebRTC: Real-Time Communication in Browsers (W3C Recommendation). World Wide Web Consortium. https://www.w3.org/TR/webrtc/

Xiao, B., Wu, H., Xu, W., Dai, X., Hu, H., Lu, Y., Zeng, M., Liu, C., & Yuan, L. (2024). Florence-2: Advancing a unified representation for a variety of vision tasks. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 4818–4829). https://doi.org/10.1109/CVPR52733.2024.00461

Yao, L., Han, J., Liang, X., Xu, D., Zhang, W., Li, Z., & Xu, H. (2023, April 10). [2304.04514] DetCLIPv2: Scalable Open-Vocabulary Object Detection Pre-training via Word-Region Alignment. arXiv. Retrieved January 29, 2026, from https://arxiv.org/abs/2304.04514

Yao, L., Han, J., Wen, Y., Liang, X., Xu, D., Zhang, W., Li, Z., Xu, C., & Xu, H. (2022, September 20). [2209.09407] DetCLIP: Dictionary-Enriched Visual-Concept Paralleled Pre-training for Open-world Detection. arXiv. Retrieved January 29, 2026, from https://arxiv.org/abs/2209.09407

Yao, L., Pi, R., Han, J., Liang, X., Xu, H., Zhang, W., Li, Z., & Xu, D. (2024, April 14). [2404.09216] DetCLIPv3: Towards Versatile Generative Open-vocabulary Object Detection. arXiv. https://arxiv.org/abs/2404.09216

Yao, Y., Liu, P., Zhao, T., Zhang, Q., Liao, J., Fang, C., Lee, K., & Wang, Q. (2024). How to evaluate the generalization of detection? A benchmark for comprehensive open-vocabulary detection. Proceedings of the AAAI Conference on Artificial Intelligence, 38(7), 6630-6638. https://doi.org/10.1609/aaai.v38i7.28485

Yousefpour, A., Fung, C., Nguyen, T., Kadiyala, K., Jalali, F., Niakanlahiji, A., Kong, J., & Jue, J. P. (2019). All one needs to know about fog computing and related edge computing paradigms: A complete survey. Journal of Systems Architecture, 98, 289–330. https://doi.org/10.1016/j.sysarc.2019.02.009

Žádník, J., Mäkitalo, M., Vanne, J., & Jääskeläinen, P. (2022). Image and Video Coding Techniques for Ultra-low Latency. ACM Computing Surveys, 54(11s), 1–35. https://doi.org/10.1145/3512342

Zang, Y., Li, W., Zhou, K., Huang, C., & Loy, C. C. (2022, March 22). [2203.11876] Open-Vocabulary DETR with Conditional Matching. arXiv. https://arxiv.org/abs/2203.11876

Zareian, A., Rosa, K. D., Hu, D. H., & Chang, S.-F. (2021). Open-Vocabulary Object Detection Using Captions (arXiv:2011.10678). arXiv. https://doi.org/10.48550/arXiv.2011.10678

Zhang, H., Ananthanarayanan, G., Bodik, P., Philipose, M., Bahl, P., & Freedman, M. J. (2017). Live Video Analytics at Scale with Approximation and Delay-Tolerance. 377–389. https://www.usenix.org/system/files/conference/nsdi17/nsdi17-zhang.pdf

Zhang, H., Zhang, P., Hu, X., Chen, Y.-C., Li, L. H., Dai, X., Wang, L., Yuan, L., Hwang, J.-N., & Gao, J. (2022). GLIPv2: Unifying Localization and Vision-Language Understanding (arXiv:2206.05836). arXiv. https://doi.org/10.48550/arXiv.2206.05836

Zhang, Y., Sun, P., Jiang, Y., Yu, D., Weng, F., Yuan, Z., Luo, P., Liu, W., & Wang, X. (2022). ByteTrack: Multi-object Tracking by Associating Every Detection Box. En S. Avidan, G. Brostow, M. Cissé, G. M. Farinella, & T. Hassner (Eds.), Computer Vision – ECCV 2022 (Vol. 13682, pp. 1–21). Springer Nature Switzerland. https://doi.org/10.1007/978-3-031-20047-2_1

Zhao, T., Liu, P., He, X., Zhang, L., & Lee, K. (2024). Real-time Transformer-based Open-Vocabulary Detection with Efficient Fusion Head (arXiv:2403.06892). arXiv. https://doi.org/10.48550/arXiv.2403.06892

Zhao, X., Chen, Y., Xu, S., Li, X., Wang, X., Li, Y., & Huang, H. (2024). An Open and Comprehensive Pipeline for Unified Object Grounding and Detection (arXiv:2401.02361). arXiv. https://doi.org/10.48550/arXiv.2401.02361

Zhou, K., Yang, J., Loy, C. C., & Liu, Z. (2022a). Conditional Prompt Learning for Vision-Language Models. IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2022). https://www.computer.org/csdl/proceedings-article/cvpr/2022/694600q6795/1H0OnmbArsY

Zhou, K., Yang, J., Loy, C. C., & Liu, Z. (2022b). Learning to Prompt for Vision-Language Models. International Journal of Computer Vision, 130(9), 2337–2348. https://doi.org/10.1007/s11263-022-01653-1

Zhou, Z., Chen, X., Li, E., Zeng, L., Luo, K., & Zhang, J. (2019). Edge Intelligence: Paving the Last Mile of Artificial Intelligence With Edge Computing. Proceedings of the IEEE, 107(8), 1738–1762. https://doi.org/10.1109/JPROC.2019.2918951

Zhu, X., Su, W., Lu, L., Li, B., Wang, X., & Dai, J. (2020, October 8). [2010.04159] Deformable DETR: Deformable Transformers for End-to-End Object Detection. arXiv. Retrieved January 29, 2026, from https://arxiv.org/abs/2010.04159

Zou, X., Dou, Z.-Y., Yang, J., Gan, Z., Li, L., Li, C., Dai, X., Behl, H., Wang, J., Yuan, L., Peng, N., Wang, L., Lee, Y. J., & Gao, J. (2023). Generalized Decoding for Pixel, Image, and Language (arXiv:2212.11270). arXiv. https://arxiv.org/abs/2212.11270

Zou, Z., Chen, K., Shi, Z., Guo, Y., & Ye, J. (2023). Object Detection in 20 Years: A Survey. Proceedings of the IEEE, 111(3), 257–276. https://doi.org/10.1109/JPROC.2023.3238524
