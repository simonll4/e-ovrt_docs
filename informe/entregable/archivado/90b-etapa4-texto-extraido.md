# 90b — Texto extraído del documento de trabajo: §17.4 Implementación (v1.15, bajada del 2026-09-08 con los pases 5, 5b, 5c, 5d y 5e aceptados; sin marcas, 3 comentarios abiertos. ETAPA 4 CERRADA)

> **Extracción derivada (2026-09-08)** del `.docx`
> `informe/entregable/E-OVRT-VDP_Seccion_17.4_Implementacion_v1.15.docx`, **solo para búsqueda y cita**
> (mismo estatuto que el doc 90): al editar, se edita el `.docx`/Google Docs, nunca
> este archivo. Tablas y figuras pueden haber perdido formato; las figuras no se
> extraen y las ecuaciones no se convierten — quedan `⟦FIGURA: no extraída — ver el .docx⟧` y
> `⟦ECUACIÓN: no extraída — ver el .docx⟧` donde estaban. Regenerado con
> `herramientas/extraer_informe.py` (regla D-C del manual de aplicación).

---

### 17.4. Implementación del prototipo experimental

La implementación materializa el diseño arquitectónico de la sección 17.3 en componentes construidos, contratos e interfaces concretados, mecanismos de acople y persistencia, y evidencia de verificación del funcionamiento técnico del prototipo.

#### 17.4.1. Componentes construidos y cadena de datos

El prototipo se materializó en tres componentes de plataforma, un módulo funcional de distribución y una cadena de datos externa a la plataforma que produce los insumos experimentales. La Figura 4.5 muestra esa organización con sus dos patrones de acople.

El plano de medios implementa la cadena de inferencia de vocabulario abierto, desde la ingesta hasta la publicación de evidencia perceptiva normalizada. El plano de control implementa el motor de patrones de riesgo, que consume esa evidencia, mantiene estado temporal y registra alertas internas. El soporte experimental no es un plano de ejecución. Reúne los catálogos de prompts y de experimentos, el orquestador reproducible de corridas, la consolidación de artefactos y la consola de inspección con su servicio intermediario.

El módulo de distribución de alertas es un módulo desacoplado y no un tercer plano de ejecución. Consume las alertas confirmadas desde el bus de alertas, aplica la política de notificación, controla idempotencia y supresión, entrega por MQTT en el nivel de calidad de servicio 1, con confirmación por mensaje y conserva un ledger de entregas de sólo adición. Su vista de resultados y su lanzamiento desde la orquestación quedaron integrados a la consola.

La cadena de datos comprende adquisición, validación, conversión y congelamiento de datasets y bancos de evaluación, y la sección 17.4.6 documenta cómo se construyó la del banco temporal de video. Alimenta a la plataforma pero no forma parte de su cadena operativa, porque su función es producir material reproducible y con procedencia para entrenamiento, selección y evaluación.

**Figura 4.5**

*Vista de procesos y patrones de acople de la plataforma experimental*

⟦FIGURA: no extraída — ver el .docx⟧

**Nota.** La figura representa la materialización efectiva de los dos patrones de acople. El gobierno de las corridas ocurre por interfaces HTTP en el plano de medios, el plano de control y el módulo de distribución, con el orquestador y la consola como clientes de los tres. El flujo de datos se desacopla mediante buses ZeroMQ de patrón publicador-suscriptor con serialización msgpack, uno para los eventos de percepción entre medios y control y otro para las alertas confirmadas entre control y distribución. El repositorio por ejecución experimental conserva los artefactos persistentes de cada corrida.

#### 17.4.2. Correspondencia y contratos materializados

Los contratos mínimos definidos durante el diseño se materializaron como modelos de datos, configuraciones versionadas, esquemas serializables, servicios ejecutables y artefactos persistentes. La Tabla 56 establece la correspondencia entre cada denominación conceptual y su realización efectiva.

**Tabla 56**

*Correspondencia entre los contratos del diseño y su materialización efectiva*

| **Elemento del diseño** | **Materialización efectiva** | **Versionado y trazabilidad** | **Componente** |
| --- | --- | --- | --- |
| Manifiesto de experimento | Archivo de manifiesto del experimento y configuraciones efectivas por plano | experiment.manifest.v1 | Soporte experimental |
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
| Repositorio de hechos | Archivos JSONL de sólo adición por corrida | Esquemas de cada evento persistido | Ambos planos |
| Referencia temporal | Anotación humana de episodios por clip | clip_gt.v2 | Soporte experimental |
| Reporte experimental | Reporte consolidado por experimento, report.json y report.md | Proyección regenerable de los artefactos primarios | Soporte experimental |
| NotificationEnvelope y DeliveryRecord | Envoltorio de notificación y registro de entrega en el ledger | control.notification.v1 / control.delivery.v1 | Módulo de distribución |

**Nota.** La tabla documenta la correspondencia semántica entre el diseño y la implementación. El versionado se materializa mediante esquemas explícitos, catálogos, conjuntos de configuración y artefactos congelados por el manifiesto de cada ejecución experimental.

Cinco de esos contratos concentran los hechos principales de la ejecución, y son el evento de percepción, el envoltorio del bus, el contrato de ciclo de vida, el evento de transición de patrón y la alerta interna. La tabla anterior los declara con su identificador de esquema.

Cada contrato es una clase de modelo declarada en el módulo de contratos de su componente, con tipos y campos obligatorios explícitos, validada en la frontera de entrada y persistida como un objeto JSON por línea, omitiendo los campos sin valor. Dentro del plano de medios la evidencia atraviesa además una cadena interna de contratos antes de publicarse. La unidad visual normaliza la lectura de la fuente, y la unidad preparada transporta los píxeles junto con la transformación espacial que devuelve del espacio del modelo al de la imagen original. La detección cruda recoge la salida del adaptador y la detección normalizada es la que se persiste. Esa cadena hace de la reproyección de coordenadas una operación declarada.

El evento de percepción normaliza la salida del detector. Identifica la corrida y la unidad visual, y agrupa en bloques estructurados la fuente, el perfil de modelo, el conjunto de prompts efectivo, las detecciones y los tiempos medidos por unidad. Cada detección lleva su etiqueta, el identificador del prompt que la originó, el puntaje, la caja en píxeles y su equivalente normalizado. Esa composición permite que una detección se atribuya después a una variable concreta de la corrida y no a una combinación desconocida. La forma efectiva del evento, tal como se persiste, es la siguiente.

{   "schema_version": "media.detection.v1",   "event_type": "detection_event",   "run_id": "run_20260803_211225_dbe_grounding_dino_1e06f3",   "unit_id": "frame_000229",   "source":  { "source_id": "a_p1_c02", "source_type": "video_frame",                "frame_index": 229, "timestamp_ms": 7633.33,                "width": 1920, "height": 1080 },   "model":   { "name": "grounding_dino",                "model_id": "IDEA-Research/grounding-dino-tiny", "device": "cuda" },   "prompts": { "prompt_set_id": "cr01_cr02_v2_short" },   "detections": [     { "detection_id": "det_000001", "label": "person",       "prompt_id": "person", "source_prompt": "person", "confidence": 0.88,       "bbox_xyxy":      [1239.8, 149.8, 1503.2, 861.9],       "bbox_norm_xyxy": [0.6457, 0.1387, 0.7829, 0.7981],       "area_px": 187612.4, "model_name": "grounding_dino" },     { "detection_id": "det_000002", "label": "vest",       "prompt_id": "vest", "source_prompt": "vest", "confidence": 0.8755,       "bbox_xyxy":      [1286.5, 235.3, 1459.3, 487.0],       "bbox_norm_xyxy": [0.67, 0.2179, 0.76, 0.4509],       "area_px": 43490.1, "model_name": "grounding_dino" },     { "detection_id": "det_000003", "label": "helmet",       "prompt_id": "helmet", "source_prompt": "helmet", "confidence": 0.456,       "bbox_xyxy":      [1519.0, 432.5, 1648.1, 521.3],       "bbox_norm_xyxy": [0.7911, 0.4005, 0.8584, 0.4827],       "area_px": 11463.6, "model_name": "grounding_dino" }   ],   "timing": { "normalize_ms": 8.06, "inference_ms": 491.17,               "postprocess_ms": 0.08, "write_ms": 0.0, "total_ms": 491.27 } }

La misma estructura se declara en el código como modelo de datos con tipos explícitos. El campo de identidad entre fotogramas aparece aquí como opcional y con valor nulo por defecto, que es el mecanismo con el que un dato todavía no producido puede incorporarse sin cambiar la versión del esquema ni alterar los artefactos ya escritos.

class DetectionEvent(BaseModel):     schema_version: str = "media.detection.v1"     event_type: str = "detection_event"     run_id: str     unit_id: str     source: DetectionEventSource     model: DetectionEventModel     prompts: DetectionEventPrompts     detections: list[Detection]     timing: DetectionEventTiming  class Detection(BaseModel):     detection_id: str | None = None     track_id: str | None = None        # aditivo: identidad entre fotogramas     label: str     prompt_id: str | None = None     source_prompt: str | None = None     strategy: str | None = None     condition_id: str | None = None     confidence: float     bbox_xyxy: list[float]             # coordenadas en la imagen original     bbox_norm_xyxy: list[float]        # coordenadas normalizadas     area_px: float | None = None     model_name: str | None = None

El envoltorio del bus no reempaqueta ese contenido. Transporta como carga la misma cadena que ya se escribió en el artefacto y le agrega cuatro campos propios del transporte, que son el tópico, la clave de particionado, un número de secuencia monótono por publicador y el instante de publicación en reloj de pared. El módulo de distribución conserva ese instante como marca de confirmación. El número de secuencia se consume incluso cuando el envío se descarta por saturación del canal, de modo que la pérdida se vuelva un hueco observable del lado del consumidor.

El contrato de ciclo de vida no delimita el inicio de la corrida sino su cierre, y publica un único evento de finalización con el identificador de corrida y su estado, para que el final lógico se distinga de una interrupción. Ambos contratos se emplean sin variantes en los dos buses, porque el publicador de alertas del plano de control es un espejo deliberado del publicador de medios.

El evento de transición registra los cambios entre los estados del patrón que fija la máquina de estados del diseño, junto con la evidencia y los hitos temporales que los motivaron. Incorpora además el instante y la unidad de la primera evidencia positiva del episodio, que es el punto de partida de la medición de latencia. Un contrato hermano registra el progreso parcial mientras la condición está en curso y todavía no fue confirmada.

La alerta interna registra la confirmación del episodio, y su identificador no es un valor aleatorio. Se deriva de forma determinista sobre la cadena que concatena el identificador de corrida de control, el de corrida de medios, la unidad, el patrón y la clave de sujeto, que incorpora el identificador del sujeto sólo cuando el patrón opera con esa granularidad. La alerta conserva además el sujeto observado, las detecciones de soporte, la clase de protección ausente, la región evaluada, el puntaje y una justificación legible. El fragmento siguiente reproduce la alerta registrada sobre el mismo clip y la misma unidad que el evento anterior, y permite verificar la ventana de confirmación. La alerta transporta el fotograma de la primera evidencia, el 109, y el de la confirmación, el 229. A los 30 cuadros por segundo del clip, esos fotogramas corresponden a 3.633 y 7.633 ms de video, exactamente los 4.000 ms configurados para la condición. Los dos instantes en milisegundos que la alerta también conserva pertenecen al reloj del equipo de control y no al tiempo de video.

{   "schema_version": "control.alert.v1",   "event_type": "alert_event",   "control_run_id": "bench_a_p1_c02_gdino_20260822_20260822T225536Z",   "media_run_id":   "run_20260803_211225_dbe_grounding_dino_1e06f3",   "alert_id": "394c9116-a38d-568d-b620-20d147c4cac9",   "pattern_id": "CR-01", "condition_id": "CR-01",   "subject_key": "CR-01:a_p1_c02", "source_id": "a_p1_c02",   "severity": "high", "state": "open",   "unit_id": "frame_000229", "frame_index": 229, "timestamp_ms": 7633.33,   "evidence": {     "subject": { "detection_id": "det_000001", "label": "person", "confidence": 0.88,                  "bbox_xyxy": [1239.8, 149.8, 1503.2, 861.9] },     "missing_class": "helmet",     "supporting": [],     "score": 0.88, "subjects_in_evidence": 1,     "rationale": "No se encontro evidencia 'helmet' en region 'upper_body' de 1 sujeto(s)."   },   "first_evidence_ms": 41990631.527, "first_evidence_unit_id": "frame_000109",   "first_evidence_frame_index": 109,   "alert_registered_ms": 41990642.511 }

La identidad de la alerta es entonces una función pura de esa quíntupla, con tres consecuencias verificables. Reprocesar la misma evidencia bajo el mismo identificador de corrida reproduce exactamente los mismos identificadores de alerta. La deduplicación no requiere estado compartido entre componentes, porque el módulo de distribución construye su clave de idempotencia a partir del identificador de alerta y la asienta en su propio registro sin consultar al plano de control. Y la identidad se asigna por confirmación y no por episodio, de modo que una confirmación posterior sobre el mismo sujeto recibe identidad propia y la idempotencia no oculta reincidencias reales.

Los contratos admiten además información que la implementación actual no produce, y la sección 17.4.8 informa cómo se ejerció esa capacidad sin romper la compatibilidad.

#### 17.4.3. Servicios, gobierno por configuración y acople

Los tres módulos de la cadena se implementaron como servicios independientes, gobernados por configuración y expuestos mediante HTTP. Cada uno carga su configuración al iniciarse, admite una corrida activa por vez, rechaza las solicitudes concurrentes señalando la que está en curso y los dos planos persisten además la configuración efectiva que utilizaron, que el módulo de distribución expone por su interfaz. El plano de medios carga además el modelo una sola vez al arrancar. Rutas, fuentes, umbrales, ventanas temporales y opciones de instrumentación se declaran en configuración, sin constantes ocultas en el código. La Tabla 57 reúne sus operaciones de gobierno.

**Tabla 57**

*Interfaces principales de los servicios de la plataforma*

| **Servicio** | **Operación** | **Función** |
| --- | --- | --- |
| Plano de medios (:8080) | GET /api/model | Expone el perfil de modelo, dispositivo y umbrales efectivos. |
|  | POST /api/runs | Dispara una corrida con fuente, prompts, parámetros, configuración de bus e identificador de experimento. |
|  | POST /api/runs/{id}/stop | Detiene cooperativamente la corrida en curso y el cierre se propaga a los consumidores por el bus. |
|  | GET /api/runs/{id} | Consulta estado y resumen de la corrida. |
|  | GET /api/runs/{id}/detections | Recupera evidencia perceptiva paginada. |
|  | POST /api/runs/{id}/evaluate | Ejecuta la evaluación de percepción cuando existe referencia aplicable. |
| Plano de control (:8081) | POST /api/runs | Dispara una corrida en modo diferido o en vivo. |
|  | GET /api/runs/{id}/alerts | Recupera las alertas internas registradas. |
|  | GET /api/config | Expone la configuración efectiva de control. |
| Módulo de distribución (:8082) | POST /api/runs | Inicia una corrida de entrega con fuente de alertas, política, canal e identificador de experimento. |
|  | GET /api/runs/{id} | Consulta estado y conteos de entrega; determina cuándo consolidar artefactos. |
|  | POST /api/runs/{id}/cancel | Detiene cooperativamente una corrida de entrega en curso. |
|  | GET /api/config | Expone la configuración efectiva de distribución. |
| Medios → control (:5557) | Bus ZeroMQ publicador-suscriptor (msgpack) | Transporta los eventos de percepción y el ciclo de vida de la corrida dentro del envoltorio versionado del bus. |
| Control → distribución (:5558) | Bus ZeroMQ publicador-suscriptor (msgpack) | Transporta las alertas internas confirmadas hacia el módulo de distribución. |
| Orquestador y consola | Clientes HTTP de los tres servicios | Gobiernan corridas y consolidan artefactos, sin consumir los buses de datos. |

El modelo no se transmite en la solicitud de corrida, de modo que comparar perfiles implica disponer procesos con perfiles distintos en lugar de reconfigurar pesos dentro de una corrida. La decisión mantiene el costo de carga fuera de la ruta crítica y evita estados ambiguos del servicio.

Las operaciones de consulta de configuración y de perfil de modelo permiten verificar antes de disparar que el servicio cargó lo que el experimento requiere. Sin ellas, una discrepancia entre lo configurado y lo desplegado sólo se descubriría en los resultados.

En una corrida en vivo el orquestador inicia primero el plano de control, después el módulo de distribución y por último el plano de medios. El control arranca primero porque debe quedar suscripto al canal de detecciones antes de que los medios publiquen, y la distribución va después porque su corrida se declara contra la corrida de control ya creada. La no pérdida en el canal de alertas no depende de ese orden sino del publicador, configurado por el orquestador para esperar a que haya un suscriptor antes de emitir. Un consumidor suscripto tarde perdería los eventos ya publicados sin ningún error observable, y las dos garantías juntas excluyen esa pérdida por construcción.

La detención de corridas es cooperativa en los dos servicios que la exponen. La solicitud marca la corrida y el hilo de ejecución la observa entre unidades, sin cortes abruptos que dejarían artefactos a medio escribir. El plano de control no expone detención y la asimetría es deliberada, porque su corrida en vivo se cierra con el evento de finalización que publica el plano de medios, con el que mantiene una relación uno a uno. El módulo de distribución sí requiere cancelación propia, porque una corrida de entrega puede quedar a la espera de alertas y debe poder abortarse sin reiniciar el servicio.

Sobre esos servicios se materializan los dos caminos experimentales, que describen cómo circula la evidencia entre los planos según la naturaleza de la ejecución.

En el camino DBE el acople entre planos se realiza por archivo. El plano de medios persiste su registro de detecciones y el plano de control lo relee, de modo que el repositorio de corrida es la fuente de verdad y permite repetir el procesamiento bajo condiciones controladas. En el camino EBE la evidencia se transmite por el bus dentro del envoltorio versionado.

La evidencia se persiste antes de publicarse, y el contenido lógico de la línea persistida y del mensaje transmitido es el mismo, lo que permite reevaluar una corrida en vivo por el camino diferido y reproducir sus artefactos. En los experimentos, los tres servicios se ejecutaron en un mismo equipo con unidad de procesamiento gráfico, el nodo central de procesamiento que describe la sección 17.1.4.1. Los contratos entre módulos no fijan esa topología, y la configuración de cada corrida registra la disposición efectiva.

#### 17.4.4. Configuración efectiva y catálogo de modelos

El conjunto de patrones efectivo del núcleo es el que el catálogo de configuración identifica como cr01_cr02_v2. CR-01, persona sin casco, se configuró con severidad alta, confirmación a los 4.000 ms y resolución a los 2.000 ms. CR-02, persona sin chaleco reflectivo, se configuró con severidad media, confirmación a los 7.000 ms y resolución a los 3.000 ms. Las precondiciones de evidencia exigen confianza mínima de 0,35 y área mínima de 400 píxeles cuadrados para el sujeto, y confianza mínima de 0,25 para el elemento de protección. La región de búsqueda se define de forma relativa a la caja del sujeto. Para CR-01 es la franja superior entre el 0 % y el 45 % de la altura con margen lateral del 12 %, y para CR-02 la franja del torso entre el 25 % y el 85 % con margen lateral del 8 %.

El conjunto opera con granularidad de escena y el motor registra cada confirmación sin supresión, conforme a la decisión de diseño DA-13. La identidad por sujeto se implementó como capacidad activable por configuración del plano de control y se trata en la sección 17.4.8.

El vocabulario activo del núcleo se compone de person como entidad y de helmet y vest como elementos de protección.

El catálogo de perfiles de modelo materializa la sustituibilidad prevista en el diseño. Reúne variantes de Grounding DINO en sus versiones tiny y base, que corresponden a los backbones Swin-T y Swin-B que presenta la sección 15.2.1.1, cada una con resolución de entrada de 800 y de 560 píxeles, y YOLOE-26 en cuatro tamaños, s, m, l y x, todas integradas mediante adaptadores sobre el mismo contrato de salida. Una tercera familia, MM-Grounding-DINO, se integró por el mismo mecanismo y se archivó fuera del catálogo activo tras la evaluación, cuyo resultado informa la sección 17.5.

El núcleo no fija un modelo único. Cada instancia del servicio de medios carga un perfil al iniciarse, de modo que comparar perfiles equivale a disponer instancias distintas bajo la misma configuración de corrida, y el despliegue integral define un servicio por cada uno de los nueve perfiles de servicio del catálogo, y deja fuera los dos perfiles de ajuste fino que se conservan sólo para reproducir su evaluación. Las campañas temporales y en vivo fijan un perfil por corrida, declarado en el manifiesto.

Cada perfil declara sus umbrales y su postproceso en el catálogo. El perfil operativo, fijado por criterio pre-registrado para las campañas temporales y en vivo, es la variante tiny de Grounding DINO con resolución de entrada de 560 píxeles, identificada en el catálogo como gdino-tiny-560, y declara umbral de caja de 0,30 y de texto de 0,25. Su postproceso aplica confianza mínima de 0,25, supresión de solapamientos con IoU de 0,50 y área mínima de caja de 100 píxeles cuadrados, y el control de ritmo opera con selección determinista de paso 1 y una cola máxima de ocho unidades. La inferencia corre en coma flotante de 16 bits sobre la unidad gráfica, una opción de la corrida y no del perfil, y la variante base de 560 píxeles, gdino-base-560, comparte resolución, umbrales y postproceso.

#### 17.4.5. Artefactos y trazabilidad por corrida

Cada ejecución produce un repositorio de artefactos de sólo adición. La organización por componente que reúne la Tabla 58 conserva la evidencia necesaria para reproducir el flujo, analizar fallas y reconstruir una alerta desde su configuración hasta su salida distribuida.

**Tabla 58**

*Artefactos persistidos por componente y experimento*

| **Tramo** | **Artefactos principales** | **Función de trazabilidad** |
| --- | --- | --- |
| Plano de medios | detections.jsonl; metrics.jsonl; errors.jsonl; summary.json; effective_config.yaml; run_manifest.json; run_provenance.json | Reconstruye fuente, unidades procesadas, detecciones, tiempos, errores, configuración, procedencia y versión de código. |
| Plano de control | pattern_events.jsonl; alerts.jsonl; alerts.csv; metrics.jsonl; errors.jsonl; summary.json; effective_config.yaml | Reconstruye transiciones del patrón, alertas internas, evidencia causal, métricas y configuración del motor. |
| Soporte experimental | manifest.effective.yaml; copias de artefactos livianos; referencias a artefactos pesados; report.json; report.md | Agrupa las corridas de ambos planos bajo un experiment_id y consolida el resultado de la ejecución experimental. |
| Distribución | notifications.jsonl (ledger de intentos y entregas, de sólo agregado); dead_letter.jsonl; distribution_summary.json | Relaciona cada intento y resultado de entrega con la alerta interna original sin reescribirla, y conserva por separado los descartes definitivos por agotamiento de reintentos. |

**Nota.** Los nombres de archivo corresponden a los artefactos implementados. Los artefactos pesados se referencian en la ejecución experimental para evitar duplicación, mientras que las configuraciones y reportes se conservan junto al experimento.

La disposición del repositorio del soporte experimental es la siguiente.

runs/<experiment_id>/  (repositorio del soporte experimental)   manifest.effective.yaml   media/    summary.json · metrics.jsonl · effective_config.yaml             detections.ref.json             (referencia al detections.jsonl del plano de medios)   control/  alerts.jsonl · pattern_events.jsonl · metrics.jsonl             summary.json · effective_config.yaml             (y la evaluación temporal, cuando la corrida la habilita)   distribution/  notifications.jsonl · distribution_summary.json                  dead_letter.jsonl               (cuando la corrida habilita el tramo de distribución)   report/   report.json · report.md

La ejecución experimental consolida así los cuatro componentes bajo una misma clave. El manifiesto de corrida registra la versión de código que produjo los artefactos. Junto con la configuración efectiva, el conjunto de prompts y la procedencia de la fuente, ese dato permite reconstruir cada alerta hasta el modelo y la revisión de código que intervinieron. El reporte consolidado declara el estado de aplicabilidad de cada métrica como computada, aplicable no computada, no aplicable o no interpretable, siempre con una causa explícita.

El ledger de entregas del módulo de distribución registra una fila por intento y una más por el descarte definitivo cuando se agotan los reintentos, de modo que la unidad de conteo del tramo es la notificación y no la fila. Al reutilizar un directorio de salida, la generación anterior se archiva íntegra y la deduplicación considera todas las generaciones, para que un reprocesamiento no vuelva a entregar lo ya entregado ni pierda la traza de lo entregado antes.

#### 17.4.6. Banco temporal y referencia humana de evaluación

La evaluación temporal se apoya en una referencia humana de episodios por clip, materializada mediante el esquema clip_gt.v2. La primera generación registraba alertas esperadas por sujeto y fue reemplazada por episodios a nivel de escena y condición, con tiempos en milisegundos y estados de aplicabilidad por clip. Para la anotación se seleccionó CVAT, una herramienta de código abierto con soporte de interpolación temporal y exportación estructurada.

**Adquisición del material.** El banco proviene de dos fuentes con procedencia y grado de control experimental distintos, y esa diferencia se conserva como atributo de cada clip. La primera es un rodaje guionado ejecutado con el hardware real de captura del prototipo. Cada escenario se diseñó en función de una condición de riesgo del núcleo. Un guion segundo a segundo fija la entrada del sujeto en cumplimiento, el inicio diferido de la infracción y su persistencia sostenida durante lapsos muy superiores a las ventanas de confirmación. El guion incluye además escenas negativas y escenas deliberadamente por debajo de ese umbral. Las tomas se registraron con margen temporal adicional respecto del clip previsto, y tanto la grabación como el recorte se hicieron desde la propia consola del prototipo.

La segunda fuente es un lote de obra real no guionada, obtenido de videos públicos e incorporado como bloque separado con criterios de selección definidos de antemano. Reúne material de obra en cumplimiento destinado a medir especificidad y falsos positivos, no sensibilidad, prohíbe concatenar segmentos cortos para fabricar unidades largas y exige que toda exclusión se declare con causa y firma en lugar de descartarse en silencio.

Los videos maestros del lote se obtuvieron de una lista de reproducción pública de YouTube compilada por el equipo (https://www.youtube.com/playlist?list=PLVG3-xIaXtKzAC9JJnZJUY4aBCg0BNPKV, consultada el 8 de septiembre de 2026) y no se redistribuyen. La dirección de origen y la fecha de acceso de cada video se consignan en el anexo de licencias y procedencia de la sección 19.

**Segmentación temporal.** Los videos maestros se conservaron sin modificación y las unidades de evaluación se generaron como clips derivados, con criterios temporales fijados antes de ejecutar las campañas y aplicados como reglas ejecutables. Cada clip del rodaje se recortó con un preludio fijo de 3,5 s antes del inicio de la condición, porque un episodio que arranca en el primer fotograma impide medir el tiempo hasta la primera detección. Lleva además una cola posterior al cierre del episodio de entre 3 y 10 s según el escenario, y un piso de duración que garantiza que una alerta válida pero lenta ocurra dentro del clip.

Ese piso resulta de sumar al inicio del episodio el techo del objetivo de latencia de alerta de su patrón, la ventana de resolución y un margen final, y se verifica mediante un control automático durante la derivación de la referencia. El clip que no lo alcanza no se vuelve a recortar, y sus métricas de latencia y sensibilidad quedan censuradas y así se declaran.

El fundamento del dimensionamiento es bidireccional. Un clip demasiado corto subestima al sistema, porque produce latencias artefactuales y cuenta como omisión una alerta que no tuvo tiempo de ocurrir. Un clip sin tiempo muerto sobreestima la precisión, porque elimina los tramos donde aparecen los falsos positivos. La selección de tomas se hizo por calidad visual de la escena y no por duración, y los límites de todos los clips quedaron congelados bajo control de versiones antes de ejecutar las campañas. Los clips del lote de obra real no se segmentaron, porque recortarlos alteraría el tiempo negativo que ese bloque aporta.

**Preanotación y revisión humana.** La anotación no partió de video crudo. Cada clip se preanotó automáticamente con un detector de vocabulario abierto de mayor capacidad que el modelo evaluado, elección deliberada para evitar circularidad entre el sistema medido y su referencia. Ese detector se acopló a un algoritmo de seguimiento que propone trayectorias por sujeto, con los atributos de protección inicializados por asociación espacial.

Sobre esa propuesta se realizó la pasada humana en CVAT. Esa revisión corrigió las cajas y las trayectorias de los 47 clips del banco, verificó la identidad de cada sujeto a lo largo de la secuencia y asignó los atributos observables tramo por tramo. Marcó como estado desconocido aquellos tramos donde el atributo no resulta observable, en lugar de forzar un valor, y fijó los límites temporales de los 37 episodios de referencia. La interpolación temporal y la preanotación redujeron las operaciones repetitivas, pero no sustituyeron ninguna de esas decisiones. La referencia experimental es el producto de esa revisión. Cuatro clips de un piloto anterior sobre video de obra real, anotados con la misma referencia de atributos y ajenos al banco temporal, se conservaron para la medición del estado por persona que informa la sección 17.5.3. La anotación la realizó un único anotador, sin la doble anotación sobre el 20 % del material que la sección 17.1.5.4 exige para la anotación propia, desviación que la sección 17.5.7 registra como limitación.

**Derivación y congelamiento.** La salida de la anotación se procesa mediante una cadena reproducible de separación, derivación, validación, promoción y agregación. La cadena valida la estructura de cada exportación antes de derivar. La derivación clasifica los episodios con las mismas ventanas de confirmación que utiliza el motor de patrones, de modo que la referencia y el sistema evaluado apliquen un criterio temporal idéntico. Una divergencia entre ambos produciría omisiones ficticias. Las correcciones humanas posteriores se aplican como registros firmados sobre los artefactos versionados, nunca editando la herramienta, y un control automático falla cuando una corrección firmada no aparece en la referencia derivada. Las anotaciones promovidas quedan congeladas bajo control de versiones, con huella criptográfica por clip y un manifiesto agregado del banco. La referencia experimental es la versión promovida en el repositorio y no el estado mutable de CVAT.

#### 17.4.7. Verificación, alcance efectivo y brechas

El criterio de cierre de la implementación exigió que cada unidad funcional produjera evidencia verificable dentro de una corrida y que su comportamiento pudiera repetirse mediante pruebas automatizadas o artefactos persistidos. La Tabla 59 reúne esa evidencia, concentrada en gobierno por configuración, cierre de corridas, paridad entre caminos, determinismo del motor y funcionamiento de la integración.

**Tabla 59**

*Evidencia de verificación técnica del prototipo*

| **Propiedad verificada** | **Evidencia de implementación** |
| --- | --- |
| Servicios ejecutables y gobernados por configuración | Las operaciones de salud, disponibilidad, creación y consulta de corridas operan sobre configuraciones validadas, y cada servicio limita la concurrencia de corridas activas. |
| Cadena DBE de extremo a extremo | La relectura por archivo produce detecciones, transiciones, alertas, métricas, resumen y configuración efectiva, y repetir el camino conserva los artefactos deterministas. |
| Cadena EBE y cierre de ciclo de vida | El consumidor confirma la suscripción antes del productor, la corrida cierra con el evento de finalización y los huecos de secuencia se registran como degradación. |
| Paridad entre repositorio y bus | La evidencia persistida y la transmitida conservan el mismo contenido lógico, y una corrida en vivo puede reevaluarse por el camino diferido. |
| Motor de patrones e idempotencia | Las transiciones respetan las ventanas configuradas y la alerta usa un identificador determinista, estable ante el reprocesamiento de la misma corrida. |
| Distribución de alertas | Se verificaron la relectura diferida, el consumo en vivo, la supresión, la idempotencia, la entrega MQTT con confirmación contra un broker real, el ledger y el reporte. |

**Nota.** La tabla acredita funcionamiento técnico y reproducibilidad. Cada módulo mantiene su propio conjunto de pruebas automatizadas, con el que estas propiedades se vuelven a verificar. No presenta métricas de desempeño del banco experimental, que se informan con sus denominadores y condiciones en la sección 17.5.

La verificación confirmó además que las fallas instrumentales no se convierten en ceros silenciosos, porque una pérdida de bus degrada la corrida, una métrica sin reloj comparable se declara no interpretable y un canal no habilitado se declara no aplicable.

El cierre de la implementación requiere declarar con precisión qué capacidades se ejercieron, cuáles permanecen fuera del núcleo y con qué estatuto, porque no todas las brechas son del mismo tipo.

La concentración del prototipo en el núcleo validable no responde a una reducción tardía del alcance sino a las condiciones de evaluabilidad de cada condición del catálogo. Las de Nivel 1 cuentan con datasets públicos y bancos con verdad de terreno para persona y elementos de protección, lo que permite medir percepción, estado temporal y alerta con denominadores declarados. Las de Nivel 2 y Nivel 3 exigen insumos que el material disponible no provee, y su justificación se desarrolla en la sección 17.5.7. Incorporarlas sin esa base habría producido capacidades no medibles, de modo que el esfuerzo se concentró en llevar el núcleo a capacidad medida. Las doce capacidades del núcleo y la operación sobre fuentes en vivo quedaron implementadas, se describen en las secciones 17.4.1 a 17.4.5 y se ejercieron en las campañas de la sección 17.5.

Dos capacidades opcionales de la Tabla 39 y dos propiedades del diseño quedaron implementadas y medidas. La identidad persistente de sujeto opera como decorador configurable de la fuente del plano de control y constituye una capacidad medida, aunque las métricas formales de seguimiento permanezcan excluidas por falta de anotación de identidad. Las tres estrategias de detección se implementaron y su comparación se ejecutó, con la salvedad de la variante híbrida por conjunción que declara la sección 17.5.6. La distribución de alertas quedó implementada, verificada e integrada a la consola y a la orquestación, con MQTT como canal ejercido. Y la paridad entre la relectura por archivo y el transporte por bus quedó verificada. Los valores de todas ellas se informan en la sección 17.5.

Una capacidad se implementó y se caracterizó fuera del régimen evaluativo. La preselección liviana en el rol de captura funciona como filtro de personas ejecutado en el dispositivo, con criterio de degradación segura y deshabilitada por defecto, y no existe para las fuentes por red. Permaneció deshabilitada en todas las corridas evaluativas, y esa exclusión es deliberada y anterior a los resultados, porque un filtro de cuadros sin persona suprimiría las detecciones sostenidas que la tasa de falsas alarmas existe para medir. La sección 17.5.7 informa su reducción de carga medida.

Las condiciones de riesgo de Nivel 2 y Nivel 3 quedaron especificadas y no implementadas. Su incorporación requiere evaluadores relacionales, zonales o de trayectoria y evidencia adecuada, y por eso no forman parte del núcleo validable.

La gestión de evidencia visual controlada quedó implementada como opción de corrida. El plano de medios puede conservar una previsualización por unidad procesada, con un tope configurable, y un video anotado de la corrida completa. La previsualización viene habilitada por defecto, un valor que invierte la regla de habilitación explícita que el diseño fija para los módulos opcionales, y el video anotado viene deshabilitado. Las campañas del banco declararon apagadas las dos, conforme a la política de minimización de evidencia visual, de modo que los artefactos evaluativos conservan identificadores, metadatos y coordenadas, y no imágenes.

La rama comparativa de ajuste fino se ejerció por completo. El protocolo, la procedencia, el servicio de inferencia, la evaluación y la línea base quedaron congelados, y la escalera de tres tramos, registrada antes de entrenar, se ejecutó entera. Los dos tramos entrenados se evaluaron una única vez contra el banco congelado, sin que ninguno superara los criterios de incorporación, que se firmaron antes de que existiera el punto de control al que se aplicarían. El tercer tramo, que habría ajustado MM-Grounding-DINO como linaje entrenable de Grounding DINO, se cerró con causa técnica por dos razones. La escalera lo condicionaba a que alguno de los dos tramos anteriores alcanzara sus criterios, y ninguno lo hizo. Y la variante que iba a ajustarse entregaba cajas degeneradas con origen en el punto de control publicado, verificado con la biblioteca de referencia sin código del proyecto, mientras que la variante sana de esa familia no había mostrado ventaja en ninguna dimensión evaluada, de modo que el linaje ajustado no habría sido el del perfil operativo. Ninguno se adoptó como modelo de servicio ni entró al despliegue, y sus perfiles permanecen en el catálogo sólo para reproducir la evaluación. Los valores por tramo se informan en la sección 17.5.6.

El subconjunto de ajuste reunió 2.946 imágenes, por encima del rango orientativo de 500 a 2.000 que fija el protocolo, y ese exceso es consecuencia de aplicar la regla de partición y no de apartarse de ella. Se tomó el total de los linajes elegibles después de excluir íntegramente la única fuente que el banco de evaluación incorpora completa y de deduplicar de forma perceptual contra él, sin submuestrear hasta el techo del rango. Los controles de solapamiento con el banco y de componentes compartidos entre entrenamiento y validación quedaron en cero, y la semilla de partición se registró con el resto de la configuración.

El cumplimiento de esa regla tuvo un límite que conviene declarar. Una de las dos fuentes retenidas para el ajuste aporta además el estrato curado del banco de imágenes, de modo que en ese punto la partición se apartó del protocolo, que reserva para el banco a toda fuente que lo integre aunque sus particiones nominales sean disjuntas. Excluirla habría reducido el conjunto de ajuste de 2.946 a 743 imágenes. La desviación se admitió con dos controles verificados, particiones disjuntas y deduplicación perceptual contra el banco en cero, y la retención medida sobre el banco, que incluye ese estrato, se lee con esa salvedad.

La asignación efectiva de las cuatro fuentes de la sección 17.1.6.2 fue la siguiente. SHEL5K y CHV integran el banco de evaluación como los estratos de 5.000 y 1.330 imágenes, y CHV es la fuente que quedó excluida íntegramente del ajuste. construction_site_safety aportó 2.203 imágenes al ajuste y es además el origen del estrato curado de obra, que es la desviación declarada arriba. ppe_siabar aportó las 743 restantes. La retención open-vocabulary se midió sobre las 5.000 imágenes de validación de COCO 2017, un material ajeno al dominio y distinto del estrato de 5.000 imágenes del banco.

El aumento de datos fue el conjunto por defecto de la biblioteca de entrenamiento, mosaico, variación de color, traslación, escala, volteo horizontal y borrado aleatorio, sin ajustes propios, y quedó registrado en la configuración efectiva de cada corrida. El costo fue de 7,7 minutos para el primer tramo y de 23,8 para el segundo, sobre una unidad gráfica NVIDIA A30 del clúster de cómputo.

Los dos tramos entrenados ajustaron la variante s de YOLOE-26 sobre la misma partición de 2.946 imágenes de ajuste y 483 de validación, con imágenes a 640 píxeles de lado, lotes de ocho, semilla fija y ejecución determinista, y en cada uno se conservó el punto de control de mejor mAP50-95 sobre las cuatro clases de validación y no el de la última época. Lo que la escalera varía es el alcance entrenable. El primer tramo entrenó sólo la proyección de clases, 3.096 parámetros, en la modalidad de linear probing que describe la sección 15.2.4. El segundo entrenó el detector completo con las rutas de prompt congeladas, 10,35 millones de parámetros, y modificó además su régimen de época y de optimización por una enmienda registrada antes de observar resultado alguno.

Ese régimen es la segunda diferencia entre ambos. El primer tramo recorrió 10 épocas completas con la selección automática de optimizador de la biblioteca de entrenamiento, y su detención temprana quedó inoperante porque la paciencia configurada superaba ese techo. El segundo fijó un techo de 60 épocas y una detención tras 15 sin mejora, ambos valores registrados antes de observar resultado alguno, y declaró el optimizador de forma explícita, por descenso de gradiente estocástico con tasa de aprendizaje inicial 0,01, momento 0,937 y tres épocas de calentamiento. La detención se activó en la época 16 y la mejor época fue la primera, que es el dato sobre el que se apoya la lectura de colapso durante el entrenamiento.

La declaración explícita del optimizador responde a un hallazgo de una corrida anterior del mismo tramo, descartada por esa causa. El modo automático de la biblioteca de entrenamiento deriva la tasa de aprendizaje del número de clases y no del alcance entrenable, de modo que asignaba el mismo valor a un tramo de 3.096 parámetros y a otro de 10,35 millones. Esa corrida se conservó como evidencia del hallazgo y no como candidata a incorporación.

El prototipo conserva su carácter experimental y asistivo. No implementa reconocimiento de identidad personal, no determina incumplimientos normativos y no reemplaza la supervisión de seguridad, conforme a las salvaguardas de la sección 17.1.10.

#### 17.4.8. Extensibilidad y costo de extensión

La extensibilidad se verificó en dos dimensiones, la incorporación de nuevas capacidades mediante puntos de extensión acotados y la evolución aditiva del evento de percepción. La plataforma no sostiene que toda condición pueda incorporarse sólo con lenguaje, y la Tabla 60 delimita qué cambios requieren configuración y cuáles requieren código nuevo.

**Tabla 60**

*Puntos de extensión y costo técnico de incorporación*

| **Extensión** | **Intervención requerida** | **Costo técnico esperado** |
| --- | --- | --- |
| Condición del mismo tipo: sujeto sin EPP | Entrada declarativa en el conjunto de patrones y formulaciones de prompt, con clase del sujeto, clase ausente, región, umbrales y ventanas. | Sólo configuración. Sin reentrenamiento ni cambios en el motor. |
| Familia nueva de condiciones | Nuevo evaluador para relaciones, zonas, trayectorias u otra semántica no cubierta por el evaluador de ausencia espacial. | Código acotado al evaluador, con los contratos y el resto de la cadena conservados. |
| Modelo de detección | Adaptador que normalice la salida y perfil de modelo en el catálogo. | Código acotado al adaptador y configuración. |
| Fuente visual | Adaptador de ingesta que produzca unidades visuales normalizadas. | Código acotado al adaptador y su validación. |
| Canal de notificación | Implementación de un consumidor del contrato de notificación y su integración de ciclo de vida. | Fuera de los dos planos; no modifica la alerta interna. |
| Dato adicional en la detección | Campo opcional con valor por defecto y consumidor tolerante a su ausencia. | Evolución aditiva sin ruptura del contrato de percepción. |

***Nota****.* La frontera entre la primera y la segunda fila delimita la extensibilidad por configuración. Una ausencia de EPP sobre un sujeto observable reutiliza el evaluador existente, mientras que una relación nueva entre entidades requiere lógica de evaluación específica.

El costo de incorporar vocabulario nuevo se midió en un piloto sobre la clase machinery. No requirió entrenamiento y demandó 48 líneas de configuración y nueve minutos de trabajo. El ejercicio mostró también que la extensión no termina al obtener detecciones, porque la alineación entre el término elegido y el concepto visual debe validarse. La sección 17.5.2 informa su desempeño y los dos fallos semánticos que aparecieron.

La identidad de sujeto recorrió el segundo camino de extensión. Se implementó como un decorador configurable de la fuente de eventos del plano de control, desactivado por defecto y utilizable tanto en el camino diferido como en el camino en vivo. La incorporación no exigió modificar el plano de medios ni romper el contrato de percepción. El identificador se conserva en los artefactos de control y no en los del plano de medios, pero el seguidor, que asocia cajas de persona por solapamiento entre cuadros consecutivos, y el orden del flujo son deterministas, de modo que una relectura reproduce las mismas identidades. Su efecto cuantitativo se informa en la sección 17.5.

El evento de percepción admite además información que la implementación actual no produce, y esa capacidad se ejerció antes de declararse. La detección normalizada incluye un campo de identidad entre fotogramas que ningún productor emite, declarado como opcional con valor por defecto y omitido al serializar cuando no tiene valor, de modo que su presencia no altera un solo byte de los artefactos existentes. El plano de control ya lo consume como clave de estado cuando opera con granularidad por sujeto, y el contrato conservó su versión.

Tres decisiones de implementación sostienen esa propiedad. Los campos nuevos se agregan como opcionales con valor por defecto, los consumidores validan contra su propia declaración del contrato y descartan sin error los campos que no conocen, y la frontera de la distribución admite explícitamente campos adicionales. Cada plano mantiene además su propia declaración del evento en lugar de una biblioteca compartida, de modo que la frontera entre ellos es el esquema serializado y no una dependencia de código, y ambos pueden versionarse y desplegarse por separado.

Lo excluido son las métricas formales de seguimiento multiobjeto y no la capacidad de asociar sujetos. De manera análoga, la velocidad, la dirección, la pose y la segmentación permanecen previstas como campos opcionales, sin presentarse como implementadas.

En conjunto, la implementación materializó la cadena que va del video a la alerta distribuida como un prototipo ejecutable, configurable, reproducible y auditable, que conserva la separación entre planos, opera por archivo o por bus y explicita sus brechas. Sobre esa base, la sección 17.5 evalúa su rendimiento sin atribuirle capacidades que no fueron medidas.
