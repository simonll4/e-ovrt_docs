# 90b — Texto extraído del documento de trabajo: §17.4 Implementación (v1.6)

> **Extracción derivada (2026-08-28)** del `.docx`
> `informe/entregable/E-OVRT-VDP_Seccion_17.4_Implementacion_v1.6.docx`, **solo para búsqueda y cita**
> (mismo estatuto que el doc 90): al editar, se edita el `.docx`/Google Docs, nunca
> este archivo. Tablas y figuras pueden haber perdido formato; las figuras no se
> extraen y las ecuaciones no se convierten — quedan `⟦FIGURA: no extraída — ver el .docx⟧` y
> `⟦ECUACIÓN: no extraída — ver el .docx⟧` donde estaban. Regenerado con
> `herramientas/extraer_informe.py` (regla D-C del manual de aplicación).

---

### 17.4. Implementación del prototipo experimental

La presente sección documenta la materialización del diseño arquitectónico desarrollado en la sección 17.3. Su propósito es establecer qué componentes fueron construidos, cómo se concretaron los contratos e interfaces previstos, qué mecanismos de acople y persistencia se implementaron y mediante qué evidencia se verificó el funcionamiento técnico del prototipo experimental.

La descripción se concentra en la implementación y en su verificabilidad. Los resultados comparativos de desempeño del detector, del motor temporal y de la plataforma completa se presentan en la sección 17.5, donde se declaran las combinaciones experimentales, los materiales, los denominadores y las limitaciones de cada medición. Esta separación evita confundir la existencia de una capacidad con su rendimiento cuantitativo.

#### 17.4.1. Componentes construidos y cadena de datos

El prototipo se materializó en tres componentes de plataforma, un módulo funcional de distribución y una cadena de datos externa a la plataforma que produce los insumos experimentales.

El plano de medios implementa el pipeline de inferencia open-vocabulary. Se ejecuta como un servicio gobernado por configuración, carga el modelo una única vez al iniciar y expone una interfaz HTTP para disparar una corrida por vez. El plano de control implementa el motor de patrones de riesgo que consume evidencia de percepción, mantiene estado temporal y registra alertas internas. También se ejecuta como servicio HTTP. El soporte experimental no constituye un plano de ejecución: reúne los catálogos de prompts y experimentos, el runner u orquestador reproducible, la consolidación de artefactos y la webconsole con su backend intermediario.

El módulo de distribución de alertas constituye un cuarto componente funcional y no un tercer plano. Al igual que los dos planos, se ejecuta como un servicio gobernado por configuración con interfaz HTTP propia. Consume las alertas confirmadas desde el bus de alertas, aplica la política de notificación, controla idempotencia y supresión, entrega por MQTT con confirmación de calidad de servicio y conserva un registro de entregas de sólo adición (ledger). La vista de resultados de entrega y el lanzamiento desde la orquestación quedaron integrados.

La **cadena de datos** comprende adquisición, validación, conversión y congelamiento de datasets y bancos de evaluación. Para el banco temporal de video esa cadena comprende la adquisición y curación del material, la preparación y segmentación temporal de los clips, la anotación asistida con revisión humana y la derivación, validación y congelamiento de la referencia; su construcción se documenta en la sección 17.4.8. Alimenta a la plataforma, pero no forma parte de su cadena operativa: su función es producir material reproducible y con procedencia para entrenamiento, selección y evaluación.

**Figura 4.7**

*Vista de procesos y patrones de acople de la plataforma experimental*

⟦FIGURA: no extraída — ver el .docx⟧

*Nota.* La figura representa la materialización efectiva de los dos patrones de acople de la plataforma experimental. El gobierno de las corridas se realiza mediante interfaces HTTP en el plano de medios (:8080), el plano de control (:8081) y el módulo de distribución (:8082), con el runner y la webconsole como clientes de los tres servicios. El flujo de datos se desacopla mediante buses ZeroMQ de patrón publicador-suscriptor con serialización msgpack: eventos de percepción desde medios hacia control (:5557) y alertas confirmadas desde control hacia distribución (:5558). El repositorio por ejecución experimental conserva los artefactos persistentes y el orden live inicia el control, confirma la suscripción y recién entonces habilita los medios.

#### 17.4.2. Correspondencia entre el diseño y los artefactos implementados

Los contratos preliminares definidos durante el diseño se materializaron como modelos de datos, configuraciones versionadas, esquemas serializables, servicios ejecutables y artefactos persistentes. La Tabla 56 establece la correspondencia entre cada denominación conceptual y su realización efectiva.

**Tabla 56**

*Correspondencia entre los contratos del diseño y su materialización efectiva*

| **Contrato del diseño** | **Materialización efectiva** | **Versionado y trazabilidad** | **Componente** |
| --- | --- | --- | --- |
| RunConfig | Manifiesto de experimento y configuraciones efectivas por plano | experiment.manifest.v1 | Soporte experimental |
| SourceDefinition | Sección de fuente de la configuración y registro de adaptadores de ingesta | Esquema de configuración; congelado por el manifiesto | Plano de medios |
| ModelProfile | Catálogo de perfiles de modelo, con un archivo por variante | Catálogo versionado; un archivo por variante | Plano de medios |
| PromptDefinition | Conjunto de prompts versionado e identificado en cada corrida | prompt_set_id registrado en cada corrida | Soporte experimental |
| FrameMetadata | Unidad visual y unidad preparada internas, y bloque de fuente del evento publicado | Contrato interno; viaja dentro del evento publicado | Plano de medios |
| PerceptionEvent | Evento de percepción normalizado | media.detection.v1 | Plano de medios |
| PatternDefinition | Definición declarativa dentro del conjunto de patrones | Conjunto de patrones versionado (pattern set) | Plano de control |
| PatternStateChanged | Evento de transición del patrón | control.pattern_state.v1 | Plano de control |
| AlertEvent | Alerta interna con identificador determinista e idempotente | control.alert.v1 | Plano de control |
| MetricSample | Muestras de métricas de medios y control | media.metric.v2 / control.metric.v1 | Ambos planos |
| ErrorEvent | Registro de errores y anomalías por corrida | Esquema por componente, registrado por corrida | Ambos planos |
| Bus interno de eventos | Publicación ZeroMQ con envoltorio versionado | bus.envelope.v1 | Frontera entre planos |
| Cierre de corrida | Evento de finalización publicado al cerrar la corrida | run.lifecycle.v1 (evento run_finished) | Plano de medios |
| Repositorio de eventos | Archivos JSONL de sólo adición por corrida | Esquemas de cada evento persistido | Ambos planos |
| Referencia temporal | Anotación humana de episodios por clip | clip_gt.v2 | Soporte experimental |
| Reporte experimental | Reporte consolidado report.json y por experimento | Proyección regenerable de los artefactos primarios | Soporte experimental |
| Alerta distribuida | NotificationEnvelope y DeliveryRecord | control.notification.v1 / control.delivery.v1 | Módulo de distribución |

**Nota.** La tabla documenta la correspondencia semántica entre el diseño y la implementación. El versionado se materializa mediante esquemas explícitos, catálogos, conjuntos de configuración y artefactos congelados por el manifiesto de cada ejecución experimental.

La correspondencia permite verificar que la implementación no sustituyó silenciosamente las fronteras arquitectónicas. El plano de medios continúa produciendo evidencia perceptiva, el plano de control conserva la interpretación temporal y la alerta interna, el soporte experimental gobierna y consolida corridas, y la distribución opera como tramo posterior desacoplado.

#### 17.4.3. Contratos de datos materializados

Cinco contratos concentran los hechos principales de la ejecución: el evento de percepción, el envoltorio del bus, el contrato de ciclo de vida, el evento de transición de patrón y la alerta interna. Los cinco están declarados con su identificador en la tabla anterior; lo que sigue precisa cómo se materializan, qué lleva cada uno y qué propiedad técnica habilita.

La materialización no es una denominación conceptual. Cada contrato es una clase de modelo declarada en el módulo de contratos de su componente, con tipos y campos obligatorios explícitos, validada en la frontera de entrada, persistida como un objeto JSON por línea en los artefactos de sólo adición —omitiendo los campos sin valor— y transportada por el bus dentro de un envoltorio serializado en formato binario compacto. Dentro del plano de medios la evidencia atraviesa además una cadena interna de contratos antes de publicarse: la unidad visual normaliza la lectura de la fuente, la unidad preparada transporta los píxeles junto con la transformación espacial que permite volver del espacio del modelo al de la imagen original, la detección cruda recoge la salida del adaptador y la detección normalizada es la que finalmente se persiste. Esa cadena es la que hace que la reproyección de coordenadas sea una operación declarada y no un ajuste disperso en el código.

El evento de percepción, DetectionEvent, normaliza la salida del detector. Identifica la corrida y la unidad visual, y agrupa en bloques estructurados la fuente, el perfil de modelo, el conjunto de prompts efectivo, las detecciones y los tiempos medidos por unidad. Cada detección lleva su etiqueta, el identificador del prompt que la originó, el puntaje, la caja en píxeles y su equivalente normalizado. Esa composición es la que permite que una detección se atribuya después a una variable concreta de la corrida y no a una combinación desconocida. La forma efectiva del evento, tal como se persiste, es la siguiente:

{   "schema_version": "media.detection.v1",   "event_type": "detection_event",   "run_id": "run_20260805_033712_dbe_grounding_dino_53cb6f",   "unit_id": "frame_000000",   "source":  { "source_id": "a_p1_c02", "source_type": "video_frame",                "frame_index": 0, "timestamp_ms": 0.0,                "width": 1920, "height": 1080 },   "model":   { "name": "grounding_dino",                "model_id": "IDEA-Research/grounding-dino-tiny",                "device": "cuda" },   "prompts": { "prompt_set_id": "cr01_cr02_v2_short" },   "detections": [     { "detection_id": "det_000001", "label": "person", "prompt_id": "person",       "confidence": 0.8784,       "bbox_xyxy": [1027.3, 105.5, 1340.8, 1083.9],       "bbox_norm_xyxy": [0.5351, 0.0977, 0.6983, 1.0],       "area_px": 306732.1, "model_name": "grounding_dino" },     { "detection_id": "det_000002", "label": "helmet", "prompt_id": "helmet",       "confidence": 0.8387,       "bbox_xyxy": [1098.1, 106.5, 1255.8, 217.3],       "bbox_norm_xyxy": [0.5719, 0.0986, 0.6541, 0.2012],       "area_px": 17475.1, "model_name": "grounding_dino" }   ],   "timing": { "normalize_ms": 11.53, "inference_ms": 445.76,               "postprocess_ms": 0.11, "write_ms": 0.0, "total_ms": 445.88 } }

El envoltorio del bus no reempaqueta ese contenido: transporta como carga la misma cadena que se escribió en el artefacto —la persistencia ocurre primero y la publicación después— y le agrega cuatro campos propios del transporte: el tópico, la clave de particionado, un número de secuencia monótono por publicador y el instante de publicación en reloj de pared, que es el que el módulo de distribución conserva luego como marca de confirmación. El número de secuencia se consume incluso cuando el envío se descarta por saturación del canal, de modo que la pérdida se vuelva observable como un hueco del lado del consumidor en lugar de pasar por ausencia de evidencia. El contrato de ciclo de vida, por su parte, no delimita el inicio de la corrida —eso lo establece la respuesta afirmativa de la operación de creación en el servicio— sino su cierre: publica un único evento de finalización con el identificador de corrida y su estado, de modo que el final lógico se distinga de una interrupción y los consumidores puedan cerrarse y consolidar sus artefactos. Ambos contratos se emplean sin variantes en los dos buses de la plataforma, el de detecciones y el de alertas: el publicador de alertas del plano de control es un espejo deliberado del publicador de medios, con el mismo envoltorio y las mismas garantías.

El evento de transición, PatternStateChanged, registra los cambios entre los estados del patrón —los mismos que fija la máquina de estados del diseño— junto con la evidencia y los hitos temporales que los motivaron, e incorpora el instante y la unidad de la primera evidencia positiva del episodio, que es el punto de partida de la medición de latencia. Un contrato hermano registra el progreso parcial mientras la condición está en curso y no ha sido confirmada todavía.

La alerta interna, AlertEvent, registra la confirmación del episodio. Su identificador no es un valor aleatorio: se deriva como un identificador único universal de versión 5 —un resumen determinista— sobre la cadena que concatena el identificador de corrida de control, el de corrida de medios, la unidad, el patrón y la clave de sujeto, donde esa clave adopta la forma CR-01:a_p1_c08 cuando el patrón opera con granularidad de escena y CR-01:a_p1_c08:subject_001 cuando opera con identidad de sujeto. La identidad de la alerta es entonces una función pura de esa quíntupla, con tres consecuencias verificables. Primero, reprocesar la misma evidencia bajo el mismo identificador de corrida de control reproduce exactamente los mismos identificadores de alerta. Segundo, la deduplicación no requiere estado compartido entre componentes: el módulo de distribución construye su clave de idempotencia como un resumen criptográfico del identificador de alerta y la asienta en un registro de sólo agregado, sin consultar al plano de control. Tercero, la identidad se asigna por confirmación y no por episodio, de modo que una confirmación posterior sobre el mismo sujeto recibe identidad propia; esto es coherente con la decisión de no suprimir dentro del motor (DA-13) y evita que el mecanismo de idempotencia oculte reincidencias reales. La alerta conserva además evidencia auditable: sujeto observado, detecciones de soporte, clase de protección ausente, región evaluada, puntaje y justificación legible. Por eso la ausencia no se presenta como una afirmación opaca del detector, sino como una inferencia del plano de control reconstruible sobre evidencia positiva.

Los contratos se diseñaron para admitir información que la implementación actual no produce, y esa capacidad fue ejercida antes de declararse. La detección normalizada incluye hoy un campo de identidad de sujeto entre fotogramas que ningún productor emite:

class Detection(BaseModel):          # media.detection.v1     detection_id:   str | None = None     track_id:       str | None = None   # identidad entre fotogramas; hoy sin productor     label:          str     prompt_id:      str | None = None     confidence:     float     bbox_xyxy:      list[float]         # píxeles [x1, y1, x2, y2]     bbox_norm_xyxy: list[float]         # normalizado [0, 1]     area_px:        float | None = None     model_name:     str | None = None

El campo se declara como opcional con valor por defecto, se omite al serializar cuando no tiene valor —de modo que su presencia en el contrato no altera un solo byte de los artefactos existentes— y, sin embargo, el plano de control ya lo consume como clave de estado cuando opera con granularidad por sujeto. El contrato conservó su versión: la extensión no exigió un cambio incompatible ni la coordinación de un despliegue conjunto. Tres decisiones de implementación sostienen esa propiedad. Los campos nuevos se agregan como opcionales con valor por defecto; los consumidores validan contra su propia declaración del contrato y descartan sin error los campos que no conocen, en lugar de rechazar el mensaje; y la frontera de la distribución declara explícitamente que admite campos adicionales. El plano de control mantiene por eso su propia declaración espejo del evento de percepción, no una biblioteca compartida con el plano de medios: la frontera entre planos es el esquema serializado y no una dependencia de código, lo que permite versionarlos y desplegarlos por separado. Éste es el mecanismo por el cual velocidad, dirección, pose, segmentación o detecciones asociadas podrían incorporarse a la evidencia perceptiva; su costo se detalla en la sección 17.4.11, donde también se declara que hoy no están implementadas.

#### 17.4.4. Interfaces de servicio y gobierno por configuración

Los dos planos se implementaron como servicios independientes gobernados por configuración y expuestos mediante HTTP. Esta concreción permite disponerlos en un mismo host o en hosts distintos sin modificar su lógica y habilita que el soporte experimental orqueste corridas de manera reproducible. Rutas, fuentes, umbrales, ventanas temporales y opciones de instrumentación se declaran en configuración; cada corrida persiste la configuración efectiva utilizada.

**Tabla 57**

*Interfaces principales de los servicios de la plataforma*

| **Servicio** | **Operación** | **Función** |
| --- | --- | --- |
| Plano de medios (:8080) | GET /api/model | Expone el perfil de modelo, dispositivo y umbrales efectivos. |
| Plano de medios (:8080) | POST /api/runs | Dispara una corrida con fuente, prompts, parámetros, configuración de bus e identificador de experimento. |
| Plano de medios (:8080) | POST /api/runs/{id}/stop | Detiene cooperativamente la corrida en curso; el cierre se propaga a los consumidores por el bus. |
| Plano de medios (:8080) | GET /api/runs/{id} | Consulta estado y resumen de la corrida. |
| Plano de medios (:8080) | GET /api/runs/{id}/detections | Recupera evidencia perceptiva paginada. |
| Plano de medios (:8080) | POST /api/runs/{id}/evaluate | Ejecuta la evaluación de percepción cuando existe referencia aplicable. |
| Plano de control (:8081) | POST /api/runs | Dispara una corrida en modo replay o live. |
| Plano de control (:8081) | GET /api/runs/{id}/alerts | Recupera las alertas internas registradas. |
| Plano de control (:8081) | GET /api/config | Expone la configuración efectiva de control. |
| Módulo de distribución (:8082) | POST /api/runs | Inicia una corrida de entrega con fuente de alertas, política, canal e identificador de experimento. |
| Módulo de distribución (:8082) | GET /api/runs/{id} | Consulta estado y conteos de entrega; determina cuándo consolidar artefactos. |
| Módulo de distribución (:8082) | POST /api/runs/{id}/cancel | Detiene cooperativamente una corrida de entrega en curso. |
| Módulo de distribución (:8082) | GET /api/config | Expone la configuración efectiva de distribución. |
|  | Bus ZeroMQ publicador-suscriptor (msgpack) | Transporta los eventos de percepción y el ciclo de vida de la corrida dentro del envoltorio versionado del bus. |
|  | Bus ZeroMQ publicador-suscriptor (msgpack) | Transporta las alertas internas confirmadas hacia el módulo de distribución. |
| Runner y webconsole | Clientes HTTP de los tres servicios | Gobiernan corridas y consolidan artefactos; no consumen los buses de datos. |

*Nota.* La tabla resume las operaciones de gobierno principales; no es un inventario exhaustivo (listados, corrida actual, artefactos por corrida, comprobaciones de salud y limpieza del registro se omiten). La detención figura únicamente donde el servicio la expone: el plano de control no ofrece detención de una corrida en curso, y esa asimetría es deliberada (ver el texto).

El modelo no se transmite en la solicitud de corrida. Se carga una sola vez al iniciar el servicio de medios; por ello, comparar perfiles de modelo implica disponer procesos con perfiles distintos y no reconfigurar pesos dentro de una corrida. Esta decisión mantiene el costo de carga fuera de la ruta crítica y evita estados ambiguos del servicio.

Los tres servicios implementan el mismo contrato de gobierno: admiten una corrida activa por vez y rechazan solicitudes concurrentes señalando la corrida en curso; cada corrida declara su configuración al crearse y el servicio persiste la configuración efectiva utilizada. Las operaciones de consulta de configuración y de perfil de modelo permiten verificar, antes de disparar, que el servicio cargó lo que el experimento requiere: sin ellas, una discrepancia entre lo configurado y lo desplegado sólo se descubriría en los resultados.

En una corrida en vivo, la respuesta afirmativa de cada consumidor del bus implica que su suscripción ya está establecida: la del plano de control sobre el canal de detecciones y la del módulo de distribución sobre el canal de alertas. De esa garantía se deriva el orden de disparo, inverso al flujo de datos: primero la distribución, después el control, por último el plano de medios. Un consumidor suscripto tarde perdería los eventos ya publicados sin ningún error observable; el orden de disparo excluye esa pérdida por construcción.

La detención de corridas es cooperativa en los dos servicios que la exponen: la solicitud marca la corrida y el hilo de ejecución la observa entre unidades, sin cortes abruptos que dejarían artefactos a medio escribir. El plano de control no expone detención, y la asimetría es deliberada: su corrida en vivo se cierra con el evento de finalización que publica el plano de medios —la relación entre ambas corridas es uno a uno—, de modo que la intervención del operador se ejerce aguas arriba y el cierre llega por el mismo canal que los datos. El módulo de distribución, en cambio, requiere cancelación propia: una corrida de entrega puede permanecer a la espera de alertas y debe poder abortarse sin reiniciar el servicio.

#### 17.4.5. Patrones de acople y caminos experimentales

La implementación distingue dos patrones técnicos de acople y dos caminos experimentales. Los patrones describen cómo se coordinan los componentes; los caminos DBE y EBE describen cómo circula la evidencia entre los planos según la naturaleza de la ejecución. Mantener ambas clasificaciones separadas evita reducir la plataforma a una dicotomía incompleta.

En el camino **DBE** el acople entre planos se realiza por archivo. El plano de medios persiste detections.jsonl y el plano de control lo relee. El repositorio de corrida constituye la fuente de verdad y permite repetir el procesamiento bajo condiciones controladas. En el camino **EBE** la evidencia se transmite por el bus ZeroMQ dentro del envoltorio versionado del bus; la relación entre una corrida de medios y una de control es uno a uno y el cierre se comunica mediante el evento de finalización del contrato de ciclo de vida.

El orden de disparo implementado sigue la regla definida en la sección 17.3.8.4: primero se inicia el plano de control y se confirma su suscripción; después se inicia el plano de medios. Cada mensaje incluye un número de secuencia, y cualquier hueco se contabiliza como pérdida del bus y degrada la corrida en lugar de ocultarse.

La evidencia se persiste antes de publicarse. El contenido lógico de la línea JSONL y del payload transmitido es el mismo, lo que permite reevaluar offline una corrida live y reproducir sus artefactos. En los experimentos del presente trabajo, los servicios se ejecutaron co-ubicados en un único host con GPU. Los contratos entre módulos no fijan esa topología, y la configuración de cada corrida registra la disposición efectiva.

#### 17.4.6. Configuración efectiva y catálogo de modelos

El conjunto de patrones efectivo del núcleo es cr01_cr02_v2. CR-01, persona sin casco, se configuró con severidad alta, confirmación a los 4.000 ms y resolución a los 2.000 ms. CR-02, persona sin chaleco reflectivo, se configuró con severidad media, confirmación a los 7.000 ms y resolución a los 3.000 ms. Las precondiciones de evidencia exigen confianza mínima de 0,35 y área mínima de 400 píxeles cuadrados para el sujeto, y confianza mínima de 0,25 para el elemento de protección. La región de búsqueda se define de forma relativa a la caja del sujeto: para CR-01, la franja superior entre el 0 % y el 45 % de la altura con margen lateral del 12 %; para CR-02, la franja del torso entre el 25 % y el 85 % con margen lateral del 8 %.

El conjunto de patrones oficial opera con granularidad de escena. En coherencia con la decisión de diseño que separa la alerta interna de su comunicación (DA-13), el motor registra cada confirmación sin supresión: el cooldown, la agrupación y la limitación de tasa pertenecen a la política del módulo de distribución. La identidad por sujeto se implementó como capacidad activable por configuración del plano de control y se trata en la sección 17.4.11.

La estrategia perceptiva del núcleo utiliza evidencia positiva: person como entidad y helmet y vest como elementos de protección. La ausencia se infiere en el plano de control y no se consulta como una negación opaca al detector.

El catálogo de perfiles de modelo materializa la sustituibilidad prevista en el diseño: variantes de Grounding DINO —tiny y base, cada una con resolución de entrada de 800 y de 560 píxeles— y de YOLOE en cuatro tamaños, todas integradas mediante adaptadores sobre el mismo contrato de salida. Una tercera familia, MM-Grounding DINO, se integró por el mismo mecanismo y fue descartada durante la evaluación; su descarte se informa con los resultados y sus perfiles quedaron archivados fuera del catálogo activo.

El núcleo no fija un modelo único. Cada instancia del servicio de medios carga un perfil al iniciarse, la comparación entre perfiles se materializa disponiendo instancias con perfiles distintos bajo la misma configuración de corrida, y el despliegue integral de la plataforma instancia un servicio por perfil del catálogo, orquestados desde la consola. Los perfiles vigentes se compararon sobre el banco de imágenes congelado; las campañas temporales y en vivo fijan un perfil por corrida, declarado en el manifiesto. Los resultados por modelo y por familia, y los criterios pre-registrados con que se seleccionó el perfil de cada campaña, se presentan en la sección 17.5.

Cada perfil declara sus umbrales y su postproceso en el catálogo, y cada corrida persiste la configuración efectiva utilizada, sin constantes ocultas en el código. A título de ejemplo, el perfil fijado por criterio pre-registrado para las corridas en vivo declara umbral de caja de 0,30 y de texto de 0,25; su postproceso aplica confianza mínima de 0,25, supresión de solapamientos con IoU de 0,50 y área mínima de caja de 100 píxeles cuadrados; y el control de ritmo opera con selección determinista de paso 1 y una cola máxima de ocho unidades.

#### 17.4.7. Artefactos y trazabilidad por corrida

Cada ejecución produce un repositorio de artefactos de sólo adición. La organización por componente conserva la evidencia necesaria para reproducir el flujo, analizar fallas y reconstruir una alerta desde su configuración hasta su salida distribuida.

**Tabla 58**

*Artefactos persistidos por componente y experimento*

| **Tramo** | **Artefactos principales** | **Función de trazabilidad** |
| --- | --- | --- |
| Plano de medios | detections.jsonl; metrics.jsonl; errors.jsonl; summary.json; effective_config.yaml; run_manifest.json; run_provenance.json | Reconstruye fuente, unidades procesadas, detecciones, tiempos, errores, configuración, procedencia y versión de código. |
| Plano de control | pattern_events.jsonl; alerts.jsonl; alerts.csv; metrics.jsonl; errors.jsonl; summary.json; effective_config.yaml | Reconstruye transiciones del patrón, alertas internas, evidencia causal, métricas y configuración del motor. |
| Soporte experimental | manifest.effective.yaml; copias de artefactos livianos; referencias a artefactos pesados; report.json; | Agrupa las corridas de ambos planos bajo un experiment_id y consolida el resultado de la ejecución experimental. |
| Distribución | notifications.jsonl (ledger de intentos y entregas, de sólo agregado); dead_letter.jsonl; distribution_summary.json | Relaciona cada intento y resultado de entrega con la alerta interna original sin reescribirla, y conserva por separado los descartes definitivos por agotamiento de reintentos. |

**Nota.** Los nombres de archivo corresponden a los artefactos implementados. Los artefactos pesados se referencian en la ejecución experimental para evitar duplicación, mientras que las configuraciones y reportes se conservan junto al experimento.

Cada plano conserva su repositorio completo por corrida: el plano de medios registra detecciones, métricas, errores, resumen, configuración efectiva, manifiesto y procedencia; el plano de control registra transiciones, alertas, métricas, errores, resumen y configuración efectiva. El soporte experimental consolida la ejecución experimental copiando los artefactos livianos y referenciando los pesados:

runs/<experiment_id>/                (repositorio del soporte experimental)   manifest.effective.yaml   media/           summary.json · metrics.jsonl · effective_config.yaml ·                    detections.ref.json  (referencia al detections.jsonl del plano de medios)   control/         alerts.jsonl · pattern_events.jsonl · metrics.jsonl ·                    summary.json · effective_config.yaml                    (y la evaluación temporal, cuando la corrida la habilita)   distribution/    notifications.jsonl · distribution_summary.json · dead_letter.jsonl                    (cuando la corrida habilita el tramo de distribución)   report/          report.json · report.md

La ejecución experimental consolida así los cuatro componentes bajo una misma clave. La modularidad de la plataforma se expresa en que un tramo pueda no estar habilitado, no en que su evidencia se consolide de otro modo cuando lo está.

El manifiesto de corrida registra la versión de código que produjo los artefactos. Junto con la configuración efectiva, el conjunto de prompts y la procedencia de la fuente, este dato permite reconstruir cada alerta hasta el modelo y el commit que intervinieron. El reporte consolidado declara el estado de aplicabilidad de cada métrica como computada, aplicable no computada, no aplicable o no interpretable, siempre con una causa explícita.

#### 17.4.8. Construcción del banco temporal y de la referencia humana de evaluación

La evaluación temporal se apoya en una referencia humana de episodios por clip, materializada mediante el esquema clip_gt.v2, segunda versión de la referencia: la primera generación registraba alertas esperadas por sujeto y fue reemplazada por episodios a nivel de escena y condición con tiempos en milisegundos, junto con estados de aplicabilidad por clip. Su construcción comprendió la adquisición y conformación del material audiovisual, la preparación y segmentación temporal de los clips, la anotación asistida con revisión humana y la derivación, validación, promoción y congelamiento de la referencia. Para la anotación se seleccionó CVAT, una herramienta de código abierto con soporte de interpolación temporal y exportación estructurada.

##### 17.4.8.1. Adquisición y conformación del material audiovisual

El material del banco proviene de dos fuentes con procedencia y grado de control experimental distintos, y esa diferencia se conserva como atributo de cada clip. La primera fuente es un rodaje guionado ejecutado con el hardware real de captura del prototipo: cada escenario se diseñó en función de una condición de riesgo del núcleo, con un guion segundo a segundo que fija la entrada del sujeto en cumplimiento, el inicio diferido de la infracción y su persistencia sostenida durante lapsos muy superiores a las ventanas de confirmación de los patrones, e incluye escenas negativas y escenas deliberadamente por debajo del umbral de confirmación. Las tomas se registraron con margen temporal adicional respecto del clip previsto, para que el recorte fino fuera una operación posterior y controlada; la grabación y el recorte se realizaron desde la propia consola del prototipo, que incorpora esa capacidad. La segunda fuente es un lote de obra real no guionada obtenido de videos públicos de internet, incorporado como bloque separado con criterios de selección definidos de antemano: material de obra en cumplimiento destinado a medir especificidad y falsos positivos —no sensibilidad—, prohibición de concatenar segmentos cortos para fabricar unidades largas, y exclusiones declaradas con causa y firma en lugar de descartes silenciosos.

*[[PENDIENTE: dirección de origen y fecha de acceso por clip del lote de obra real · depende de completar la ficha de procedencia primaria antes del cierre final del informe]]*

##### 17.4.8.2. Preparación y segmentación temporal de los clips

Los videos maestros se conservaron sin modificación y las unidades de evaluación se generaron como clips derivados, con criterios temporales explícitos fijados antes de ejecutar las campañas y aplicados como reglas ejecutables, no como juicio caso por caso. Cada clip del rodaje se recortó con un preludio fijo de 3,5 s antes del inicio de la condición —el inicio nunca coincide con el primer fotograma, porque un episodio que arranca en el origen impide medir el tiempo hasta la primera detección—, una cola posterior al cierre del episodio de entre 3 y 10 s según el escenario, y un piso de duración que garantiza que una alerta válida pero lenta pueda ocurrir dentro del clip: el inicio del episodio más el techo del objetivo de latencia de alerta de su patrón, más la ventana de resolución y un margen final. Ese piso se verifica mediante un control automático durante la derivación de la referencia, y el clip que no lo alcanza no se vuelve a recortar: sus métricas de latencia y sensibilidad quedan censuradas y así se declaran. El fundamento del dimensionamiento es bidireccional: un clip demasiado corto subestima al sistema, porque produce latencias artefactuales y cuenta como omisión una alerta que no tuvo tiempo de ocurrir; un clip sin tiempo muerto sobreestima la precisión, porque elimina los tramos donde aparecen los falsos positivos. El dimensionamiento correcto elimina ambos artefactos, de modo que cada métrica resulte atribuible al sistema y no al recorte. La selección de tomas se realizó por criterio visual de calidad de la escena, no por duración, y los límites de todos los clips quedaron congelados bajo control de versiones antes de ejecutar las campañas que los evalúan. Los clips del lote de internet no se segmentaron: cada uno es el video original completo, porque recortarlos alteraría precisamente el tiempo negativo que ese bloque aporta a la medición de falsos positivos.

##### 17.4.8.3. Preanotación asistida y revisión humana en CVAT

La anotación no partió de video crudo. Cada clip se preanotó automáticamente con un detector de vocabulario abierto de mayor capacidad que el modelo evaluado —elección deliberada para evitar circularidad entre el sistema medido y su referencia— acoplado a un algoritmo de seguimiento que propone trayectorias por sujeto, con los atributos de protección inicializados por asociación espacial. Sobre esa propuesta se realizó la pasada humana en CVAT: revisión y corrección de cajas y trayectorias, verificación de identidades a lo largo de la secuencia, asignación de los atributos observables por tramo, marcación explícita como estado desconocido de los tramos donde el atributo no resulta observable —en lugar de forzar un valor—, y fijación de los límites temporales de cada episodio. La interpolación temporal y la preanotación redujeron las operaciones repetitivas, pero no sustituyeron la revisión humana de las trayectorias, los atributos ni los límites de cada episodio: la construcción de la referencia fue una actividad intensiva en revisión, no un etiquetado manual fotograma por fotograma ni una validación automática.

##### 17.4.8.4. Derivación, validación, promoción y congelamiento

La salida de la anotación se procesa mediante una cadena reproducible de separación, derivación, validación, promoción y agregación. La cadena valida la estructura de cada exportación antes de derivar, y la derivación clasifica los episodios con las mismas ventanas de confirmación que utiliza el motor de patrones —4.000 ms para CR-01 y 7.000 ms para CR-02—, de modo que la referencia y el sistema evaluado apliquen un criterio temporal idéntico; una divergencia entre ambos produciría omisiones ficticias. Las correcciones humanas posteriores a la derivación se aplican como registros firmados sobre los artefactos versionados —nunca editando la herramienta de anotación— y un control automático falla cuando una corrección firmada no aparece en la referencia derivada. Las anotaciones promovidas quedan congeladas bajo control de versiones, con huella criptográfica por clip y un manifiesto agregado del banco. CVAT funciona así como instrumento de captura: la referencia experimental es la versión promovida en el repositorio, no el estado mutable de la herramienta.

#### 17.4.9. Verificación técnica de la implementación

El criterio de cierre de la implementación exigió que cada unidad funcional produjera evidencia verificable dentro de una corrida y que su comportamiento pudiera repetirse mediante pruebas automatizadas o artefactos persistidos. La verificación se concentró en corrección de contratos, cierre de corridas, paridad entre caminos, determinismo y funcionamiento de la integración, sin sustituir la evaluación de desempeño de la sección 17.5.

**Tabla 59**

*Evidencia de verificación técnica del prototipo*

| **Propiedad verificada** | **Evidencia de implementación** |
| --- | --- |
| Servicios ejecutables y gobernados por configuración | Los endpoints de salud, disponibilidad, creación y consulta de corridas operan sobre configuraciones validadas; cada plano limita la concurrencia de corridas activas. |
| Cadena DBE de extremo a extremo | La relectura por archivo produce detecciones, transiciones, alertas, métricas, resumen y configuración efectiva; repetir el camino conserva los artefactos deterministas. |
| Cadena EBE y cierre de ciclo de vida | El consumidor confirma la suscripción antes del productor, la corrida cierra con el evento de finalización y los huecos de secuencia se registran como degradación. |
| Paridad entre repositorio y bus | La evidencia persistida y la transmitida conservan el mismo contenido lógico; una corrida live puede reevaluarse offline. |
| Motor temporal e idempotencia | Las transiciones respetan las ventanas configuradas y la alerta usa un identificador determinista, estable ante el reprocesamiento de la misma corrida. |
| Distribución de alertas | Se verificaron replay DBE, consumo EBE, supresión, idempotencia, entrega MQTT QoS 1 contra un broker real, ledger y reporte; la consola y la orquestación quedaron integradas. |
| Pruebas automatizadas | El relevamiento integral registró 2.203 pruebas aprobadas, sin fallos, en cinco suites de la plataforma; el módulo de distribución añadió posteriormente su suite propia, también verificada. |

**Nota.** La tabla acredita funcionamiento técnico y reproducibilidad. No presenta métricas de desempeño del banco experimental, que se informan con sus denominadores y condiciones en la sección 17.5.

La verificación también confirmó que las fallas instrumentales no se convierten en ceros silenciosos. Una pérdida de bus degrada la corrida, una métrica sin reloj comparable se declara no interpretable y un canal no habilitado se declara no aplicable. Esta política preserva la diferencia entre ausencia de capacidad, ausencia de datos y resultado desfavorable.

#### 17.4.10. Alcance efectivo, límites y brechas

El cierre de la implementación requiere declarar con precisión qué capacidades fueron ejercidas, cuáles permanecen fuera del núcleo y qué resultados continúan abiertos. La Tabla 60 evita tratar todas las brechas como si tuvieran el mismo estatuto.

La concentración del prototipo en el núcleo validable no responde a una reducción tardía del alcance, sino a las condiciones de evaluabilidad de cada condición del catálogo. Las condiciones de Nivel 1 cuentan con datasets públicos y bancos de evaluación con verdad de terreno para persona y elementos de protección personal, lo que permite medir percepción, estado temporal y alerta con denominadores declarados. Las condiciones de Nivel 2 y Nivel 3, en cambio, exigen insumos que el material disponible no provee: verdad de terreno de andamios, arneses, bordes desprotegidos o zonas restringidas; definiciones externas de zona y geometría de cámara controlada; y evaluadores relacionales o de trayectoria cuya validación requeriría bancos propios que no existen en el dominio. Incorporarlas sin esa base habría producido capacidades no medibles, contrarias al criterio metodológico de no convertir extensiones en dependencias del flujo base. El esfuerzo experimental se concentró, en cambio, en llevar el núcleo a capacidad medida: la misma decisión que limitó la cantidad de condiciones cubiertas es la que permite reportar cada resultado con su evidencia.

**Tabla 60**

*Capacidades ejercidas, exclusiones y brechas de implementación*

| **Capacidad** | **Estado de implementación** | **Consecuencia para el informe** |
| --- | --- | --- |
| Identidad persistente de sujeto | Implementada y ejercida como decorador configurable de la fuente del plano de control. | La granularidad por sujeto constituye una capacidad medida. Las métricas MOT permanecen excluidas por falta de anotaciones de identidad. |
| Estrategias directa (E-DIR), indirecta (E-IND) e híbrida (E-HYB) | Las variantes se implementaron y la comparación prevista se ejecutó. | La estrategia indirecta integra el núcleo; los resultados y los veredictos comparativos se presentan en la sección 17.5. |
| Distribución de alertas | Implementada, verificada e integrada a la consola y a la orquestación. | MQTT constituye el canal ejercido. Los canales adicionales y un tablero operativo propio permanecen fuera del alcance. |
| Rama comparativa de ajuste fino | Protocolo, procedencia, servicio de inferencia, evaluación y línea base quedaron congelados, y la escalera de tramos pre-registrada se ejecutó completa. Los dos tramos entrenados se evaluaron una única vez contra el banco congelado y ninguno superó los criterios de incorporación, firmados antes de que existiera el checkpoint que se les aplicaría. El tercer tramo se cerró con causa técnica: el único corpus disponible de ese volumen comparte fuentes con el banco de evaluación y deriva la clase de cabeza descubierta de una forma que el vocabulario canónico vigente no admite. | Ningún checkpoint se incorporó como modelo de servicio. El resultado es un veredicto negativo pre-registrado y no un tramo abierto: los criterios y los márgenes se firmaron antes de la evaluación, y las tres expectativas registradas de antemano se confirmaron. Los valores por tramo y la lectura de la curva se informan en la sección 17.5. |
| Condiciones de riesgo de nivel 2 y 3 | Especificadas, pero no implementadas en el prototipo. | No forman parte del núcleo validable; su incorporación requiere evaluadores relacionales, zonales o de trayectoria y evidencia adecuada. |
| Preselección liviana en el rol de captura | Implementada para la fuente de captura propia como filtro de personas ejecutado en el dispositivo, con criterio de degradación segura y deshabilitada por defecto; su reducción de carga se midió en una comparación pareada contra el flujo completo, con un 87 % de unidades descartadas antes de salir de la cámara. No existe para las fuentes por red. Permaneció deshabilitada en todas las corridas evaluativas. | La exclusión de lo evaluativo es deliberada y anterior a los resultados: un filtro de fotogramas sin persona suprimiría las detecciones sostenidas que la tasa de falsos positivos por hora existe para medir, y superpondría el error de un detector auxiliar más débil sobre la cadena que se busca caracterizar. Habilitarlo cambiaría la procedencia de esas métricas en lugar de mejorarlas. La capacidad se reporta, entonces, como implementada y caracterizada fuera del régimen evaluativo. |
| Paridad DBE/EBE sobre fuente equivalente | La paridad de transporte y relectura fue verificada. | La reevaluación offline de una corrida live produce artefactos equivalentes; la paridad de transporte y relectura queda verificada. |

**Nota.** Los estados distinguen capacidad implementada, capacidad medida, exclusión metodológica y resultado todavía abierto.

El prototipo conserva su carácter experimental y asistivo. No implementa reconocimiento de identidad personal, no determina incumplimientos normativos y no reemplaza la supervisión de seguridad. Las alertas son registros no vinculantes producidos bajo una configuración explícita y sujetos a revisión humana.

#### 17.4.11. Extensibilidad implementada y costo de extensión

La extensibilidad se verificó en dos dimensiones: la incorporación de nuevas capacidades mediante puntos de extensión acotados y la evolución aditiva del evento de percepción. La plataforma no sostiene que toda condición pueda incorporarse sólo con lenguaje; delimita qué cambios requieren configuración y cuáles requieren código nuevo.

**Tabla 61**

*Puntos de extensión y costo técnico de incorporación*

| **Extensión** | **Intervención requerida** | **Costo técnico esperado** |
| --- | --- | --- |
| Condición del mismo tipo: sujeto sin EPP | Entrada declarativa en el conjunto de patrones y formulaciones de prompt: clase del sujeto, clase ausente, región, umbrales y ventanas. | Sólo configuración; sin reentrenamiento ni cambios en el motor. |
| Familia nueva de condiciones | Nuevo evaluador para relaciones, zonas, trayectorias u otra semántica no cubierta por spatial_absence. | Código acotado al evaluador; los contratos y el resto de la cadena se conservan. |
| Modelo de detección | Adaptador que normalice la salida y perfil de modelo en el catálogo. | Código acotado al adaptador y configuración. |
| Fuente visual | Adaptador de ingesta que produzca unidades visuales normalizadas. | Código acotado al adaptador y su validación. |
| Canal de notificación | Implementación de un consumidor del contrato de notificación y su integración de ciclo de vida. | Fuera de los dos planos; no modifica la alerta interna. |
| Dato adicional en la detección | Campo opcional con valor por defecto y consumidor tolerante a su ausencia. | Evolución aditiva sin ruptura del contrato de percepción. |

**Nota.** La frontera entre la primera y la segunda fila delimita la extensibilidad por configuración: una ausencia de EPP sobre un sujeto observable reutiliza el evaluador existente; una relación nueva entre entidades requiere lógica de evaluación específica.

El costo de incorporar vocabulario nuevo se midió en un piloto sobre la clase machinery: no requirió entrenamiento, demandó 48 líneas de configuración y nueve minutos de trabajo. El ejercicio mostró también que la extensión no termina al obtener detecciones; la alineación entre el término elegido y el concepto visual debe validarse, porque una palabra puede producir cajas plausibles sobre objetos distintos del objetivo. El desempeño cuantitativo de ese piloto se presenta en la sección 17.5.

La identidad de sujeto recorrió el segundo camino de extensión. Se implementó como un decorador configurable de la fuente de eventos del plano de control, desactivado por defecto y utilizable tanto en DBE como en EBE. La incorporación no exigió modificar el plano de medios ni romper el contrato de percepción. El identificador se conserva en los artefactos de control; no se persiste en detections.jsonl, pero el seguidor y el orden del flujo son deterministas, por lo que una relectura reproduce las mismas identidades. Su efecto cuantitativo se informa en la sección 17.5.

Lo excluido son las métricas formales de seguimiento multiobjeto, no la capacidad de asociar sujetos. De manera análoga, velocidad, dirección, pose y segmentación permanecen previstos como campos opcionales o artefactos complementarios, pero no se presentan como implementados. Esta distinción conserva la compatibilidad del contrato sin convertir previsiones de evolución en capacidades inexistentes.

En conjunto, la Etapa 4 materializó la cadena video-evento de percepción-patrón-alerta-distribución como un prototipo ejecutable, configurable, reproducible y auditable. La implementación conserva la separación entre planos, permite operar por archivo o por bus, registra la configuración y la procedencia de cada corrida, y explicita sus brechas. Sobre esta base, la sección 17.5 evalúa el rendimiento de la percepción, del estado por persona y de la alerta temporal por episodio sin atribuir a la arquitectura capacidades que no fueron medidas.
