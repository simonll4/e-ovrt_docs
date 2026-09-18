# 90f — Texto extraído del documento de trabajo: §17.1 Consolidación Metodológica (v1.21, bajada del 2026-09-08 con los pases 5, 5d y 5e aceptados; limpia, sin comentarios ni marcas. ETAPA 2 CERRADA)

> **Extracción derivada (2026-09-08)** del `.docx`
> `informe/entregable/E-OVRT-VDP_Seccion_17.1_Consolidacion_Metodologica_v1.21.docx`, **solo para búsqueda y cita**
> (mismo estatuto que el doc 90): al editar, se edita el `.docx`/Google Docs, nunca
> este archivo. Tablas y figuras pueden haber perdido formato; las figuras no se
> extraen y las ecuaciones no se convierten — quedan `⟦FIGURA: no extraída — ver el .docx⟧` y
> `⟦ECUACIÓN: no extraída — ver el .docx⟧` donde estaban. Regenerado con
> `herramientas/extraer_informe.py` (regla D-C del manual de aplicación).

---

## 17. Desarrollo del producto

### 17.1. Consolidación metodológica del protocolo experimental

La consolidación metodológica transforma el marco teórico construido previamente en un protocolo experimental utilizable. Para ello fija decisiones sobre alcance, escenarios, infraestructura, datos, prompts, métricas y criterios de aceptación, integrando los desarrollos metodológicos en una secuencia coherente con el objetivo del prototipo experimental.

El referente experimental resultante delimita qué condiciones de riesgo integran el núcleo del prototipo, cómo se estructuran los escenarios de evaluación, con qué reglas se gestionan los datos, qué métricas deben producirse y cómo debe interpretarse la evidencia obtenida.

Esta instancia establece las condiciones de comparabilidad, medición e interpretación necesarias para el desarrollo del prototipo, y su posterior evaluación sobre bases explícitas y trazables.

#### 17.1.1. Función y alcance de la consolidación metodológica

El criterio rector prioriza la validez experimental, la trazabilidad y la correspondencia entre alcance, datos disponibles e instrumentación efectiva. El núcleo obligatorio del prototipo se ubica en las condiciones de Nivel 1 —CR-01 y CR-02—, donde convergen observabilidad visual, cobertura de datos, estrategias de evaluación defendibles y métricas aplicables con el hardware disponible; las condiciones de Niveles 2 y 3 se conservan como extensiones condicionadas, debido a brechas de datos, visibilidad y razonamiento contextual.

A partir de ese criterio se fija una secuencia experimental integrada —comparación primaria en Dataset-Based Evaluation (DBE), validación complementaria en Environment-Based Evaluation (EBE), reglas de partición sin leakage, política de formulación y congelamiento de prompts, jerarquía de métricas orientada al valor operativo de alerta y criterios para habilitar una rama comparativa de fine-tuning—, organizada sobre cuatro dimensiones temáticas: el entorno experimental, las condiciones de riesgo y su protocolo de prompts, la estrategia de datos y el framework de métricas.

#### 17.1.2. Alcance experimental consolidado del prototipo

##### 17.1.2.1. Catálogo de condiciones de riesgo y alcance de validación

El catálogo retenido comprende seis condiciones de riesgo organizadas en tres niveles de complejidad. Dentro de este catálogo, CR-01 y CR-02 constituyen el núcleo obligatorio de validación, porque son condiciones de Nivel 1 cuya relevancia preventiva, observabilidad y evaluabilidad están fundamentadas en la sección 16.2 y pueden abordarse mediante las estrategias de detección definidas para el protocolo, con cobertura de datos y métricas aplicables dentro del entorno experimental disponible.

Las condiciones restantes se conservan como extensiones condicionadas. CR-03 y CR-04 dependen de mayor visibilidad de atributos, evidencia de ausencia y datos complementarios, mientras que CR-05 y CR-06 requieren persistencia temporal, relaciones espaciales o regiones parametrizadas. Estas exigencias incrementan la dependencia de información contextual y de capacidades adicionales del pipeline, en concordancia con las dificultades documentadas para los modelos OVD ante atributos finos y dominios especializados de construcción (Bianchi et al., 2024; Abdalwhab et al., 2025). En consecuencia, la validación del prototipo no exige un desempeño uniforme sobre las seis condiciones, sino que la evidencia necesaria para sostener el alcance experimental se concentra en el núcleo obligatorio, mientras que las restantes condiciones conservan valor como extensiones del catálogo.

La definición completa, con el tipo de condición, el componente evaluador y la dificultad estimada, se presenta en la Tabla 20.

#### 17.1.3. Diseño metodológico general y lógica de escenarios

##### 17.1.3.1. Patrón de riesgo como unidad de análisis

El protocolo adopta como unidad de análisis el patrón de riesgo confirmado y no la detección aislada. Esta decisión evita reducir el problema a la mera producción de cajas por cuadro. En el proyecto, la condición de riesgo constituye la unidad semántica de entrada, mientras que el patrón de riesgo incorpora severidad, persistencia y, cuando corresponde, relaciones espaciales o temporales. Por último, la alerta constituye la salida operativa trazable del sistema.

##### 17.1.3.2. Cadena operativa mínima y motor de patrones

A partir de esa unidad de análisis, el protocolo asume una cadena operativa mínima entre percepción, evaluación y respuesta asistiva. En dicha cadena, las detecciones producidas por el modelo OVD funcionan como evidencia primaria, pero no constituyen por sí mismas una alerta. Para que una alerta sea considerada válida dentro del sistema, la evidencia debe ser agrupada, evaluada y confirmada como patrón de riesgo según los criterios definidos para cada condición.

En términos operativos, esta evaluación corresponde al motor de patrones, entendido como una abstracción lógica del plano de control que aplica criterios de persistencia, severidad, histéresis y lógica espacial o contextual sobre los eventos de detección. Sólo cuando un patrón alcanza el estado confirmado puede registrarse una alerta interna dentro del sistema. Su operacionalización se desarrolla en la sección 17.1.5.2.

##### 17.1.3.3. Escenarios de evaluación

Sobre esa base, la evaluación se organiza en dos escenarios complementarios —el Escenario A o Dataset-Based Evaluation (DBE), ámbito primario de comparación controlada y repetible, y el Escenario B o Environment-Based Evaluation (EBE), validación de plausibilidad operativa sobre captura continua—, cuya relación no es de reemplazo. Su caracterización completa se desarrolla en la sección 17.1.4.2.

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

El entorno experimental delimita las condiciones materiales y operativas bajo las cuales se aplica el protocolo. Su caracterización responde a la pregunta rectora P-E1-04 y vincula la capacidad de cómputo disponible, la forma de adquisición y transporte del video y el presupuesto temporal de procesamiento. Sobre esa base se distinguen los roles de ejecución y dos escenarios complementarios de evaluación, de modo que las mediciones de desempeño puedan interpretarse respecto del entorno en el que fueron obtenidas.

##### 17.1.4.1. Infraestructura y roles de ejecución

La infraestructura se organiza mediante tres roles funcionales, sin imponer que cada uno corresponda a un dispositivo físico exclusivo. El *Central Processing Node* (CPN) constituye la referencia para la inferencia open-vocabulary, el postproceso, la evaluación de patrones y la instrumentación de rendimiento; por ello, las conclusiones sobre viabilidad temporal y uso de recursos se anclan en este nodo. El rol se materializa sobre una laptop HP Victus 15 Gaming 15-FB2024LA con una GPU NVIDIA GeForce RTX 4060 Laptop de 8 GB de VRAM y entorno Linux mediante WSL2, combinación que condiciona el tamaño de los modelos ejecutables, la resolución de inferencia, la precisión numérica y la selección del runtime (HP Inc., s. f.). El stack debe conservar compatibilidad con los frameworks oficiales de Grounding DINO y YOLOE y permitir rutas reproducibles de inferencia acelerada (Liu et al., 2024; Wang et al., 2025).

El *Edge Node* (EN) representa la adquisición próxima a la fuente visual. El protocolo contempla una cámara IP mediante RTSP y una Luxonis OAK-D Pro PoE mediante su interfaz de captura; en ambos casos, el flujo base mantiene la inferencia OVD en el CPN y reserva el borde para captura, transmisión y, cuando corresponda, preprocesamiento liviano (Luxonis, s. f.-a, s. f.-b). Para flujos H.264 o H.265, la decodificación acelerada mediante NVDEC se conserva como alternativa declarable por corrida, ya que su uso modifica el reparto de carga entre CPU y GPU y, con ello, la interpretación del presupuesto temporal (NVIDIA Corporation, s. f.-b). Independientemente de la fuente, cada corrida debe registrar procedencia, resolución, tasa de captura y referencias temporales suficientes para interpretar las mediciones.

El Training Node (TN) se reserva para la preparación de variantes ajustadas y queda fuera del camino de inferencia evaluado. Se materializa mediante el clúster institucional Mendieta del CCAD-UNC y debe permitir preparación de datos, entrenamiento reproducible, conservación de checkpoints y exportación hacia el CPN (Centro de Computación de Alto Desempeño, 2026). La decisión de habilitar una rama de adaptación al dominio y sus condiciones de comparación se establecen en la sección 17.1.9, mientras que en este apartado sólo se fija la separación entre el entorno de preparación del modelo y el entorno sobre el que se juzga su comportamiento operativo.

El detalle técnico de los recursos de cómputo y captura, los entornos de software y los parámetros de referencia del entorno experimental se consolida en el Anexo B.

##### 17.1.4.2. Escenarios de evaluación

La evaluación se estructura en dos escenarios complementarios. El Dataset-Based Evaluation (DBE) constituye el ámbito primario de comparación controlada y reproducible: procesa imágenes o secuencias de video provenientes de datasets anotados y permite aislar variables, repetir una configuración sobre la misma entrada y, cuando los protocolos sean compatibles, contrastar los resultados con referencias externas. El Environment-Based Evaluation (EBE) incorpora captura continua en un entorno físico controlado y ejercita la cadena desde la adquisición del video hasta la evaluación temporal de patrones, introduciendo variables visuales y de conectividad que no pueden representarse completamente mediante archivos.

La relación entre ambos escenarios no es de reemplazo. El DBE sostiene la comparabilidad entre configuraciones y la evaluación cuantitativa bajo entradas congeladas; el EBE aporta evidencia de plausibilidad operativa al someter la plataforma a temporalidad continua, iluminación, oclusiones, escala y transporte de video. En ambos casos, el CPN mantiene el rol de referencia para la inferencia y la evaluación, mientras que el EN participa en el EBE como fuente de captura. Si una variante ajustada es habilitada conforme a la sección 17.1.9, debe compararse contra la baseline bajo material y configuración equivalentes, aislando la adaptación como variable experimental. Las variables de sensibilidad candidatas para el EBE se consolidan en la Tabla C.2 del Anexo C.

**Tabla 17**

*Comparación de los escenarios de evaluación DBE y EBE*

| **Aspecto** | **DBE** | **EBE** |
| --- | --- | --- |
| Entrada y temporalidad | Imágenes y secuencias de video provenientes de datasets anotados. Procesamiento sobre archivos con entrada reproducible. | Video en vivo desde el EN mediante RTSP o captura directa con OAK-D Pro PoE. Temporalidad continua. |
| Propósito metodológico | Comparación controlada de configuraciones, aislamiento de variables y repetibilidad de las mediciones. | Validación de plausibilidad operativa del pipeline integrado bajo condiciones visuales y de conectividad representativas. |
| Distribución funcional | CPN para inferencia y evaluación. No requiere transporte de video en vivo. | EN para captura y CPN para inferencia y evaluación. El transporte y sus referencias temporales forman parte de la instrumentación. |
| Variables dominantes | Modelo, prompt, dataset, partición, resolución y umbrales declarados. | Fuente de captura, iluminación, oclusión, escala, densidad de escena, transporte y buffering, además de la configuración del modelo. |
| Limitación principal | La reproducibilidad no elimina la brecha entre datasets y condiciones reales de operación. | La variabilidad del entorno reduce la reproducibilidad y exige documentar las condiciones de captura y ejecución. |

***Nota****.* DBE = Dataset-Based Evaluation. EBE = Environment-Based Evaluation. La tabla sintetiza las diferencias metodológicas entre ambos escenarios; la estrategia de datos, el framework de métricas y las condiciones de adaptación al dominio se desarrollan en sus secciones específicas.

#### 17.1.5. Condiciones de riesgo, patrones y protocolo de prompts

La definición de las condiciones de riesgo, de los patrones asociados y de las consultas textuales que los buscan responde a la pregunta rectora P-E1-02 y transforma las condiciones preventivamente relevantes en unidades evaluables por la plataforma. El protocolo establece el catálogo experimental, los criterios temporales y contextuales que permiten confirmar un patrón y las reglas para diseñar, comparar y congelar los prompts OVD antes de la evaluación.

##### 17.1.5.1. Catálogo de condiciones de riesgo y evaluabilidad

La fundamentación teórica delimita las condiciones de riesgo observables por su relevancia preventiva, su evidencia visual anotable y su formulación evaluable (sección 16.2), y señala como posibles extensiones situaciones como el trabajo en altura, las zonas restringidas o la interacción con maquinaria. El prototipo experimental no pretende cubrir ese espacio de manera exhaustiva y selecciona un subconjunto acotado con tres criterios.

El primero es la **representatividad**, de modo que el catálogo incluya al menos una condición de cada nivel de complejidad y la evaluación ejercite las distintas capacidades del pipeline. El segundo es la **factibilidad de detección visual**, que exige correlatos visuales suficientemente diferenciados para resolverse mediante análisis de imagen en las resoluciones y ángulos de cámara típicos de un entorno de laboratorio o simulado. Quedan fuera las condiciones cuya manifestación depende de detalles de difícil resolución, como la distinción entre calzado de seguridad y calzado común o la presencia de guantes y gafas de protección, y las que carecen de correlato visual directo, como una capacitación insuficiente. También quedan fuera, aunque son preventivamente relevantes, condiciones de escena como la obstrucción de pasillos o la presencia de materiales inestables, que no admiten una definición visual estable para su anotación. El tercero es la **viabilidad de evaluación** con los recursos disponibles, de manera que cada condición pueda medirse con datasets públicos, con subconjuntos anotados de ellos o con material generado en entorno controlado, sin campañas de recolección incompatibles con un proyecto académico.

Las condiciones seleccionadas se clasifican en tres niveles según las capacidades que el sistema debe desplegar para evaluarlas, una distinción con consecuencias directas sobre la arquitectura del pipeline y sobre el protocolo aplicable a cada una. Las condiciones de Nivel 1 involucran una entidad simple o un atributo observable sobre ella, resoluble en principio con una consulta OVD sobre un cuadro individual, sin información temporal ni relacional. La detección de casco sobre una persona es el caso representativo, y la evaluación de la condición asociada admite las dos estrategias que se definen en la sección 17.1.5.3. Las condiciones de Nivel 2 agregan un atributo contextual que depende de la relación espacial entre la entidad y su entorno inmediato dentro del mismo cuadro, como la persona sobre un andamio. El detector puede localizar a la persona y a la estructura por separado, pero determinar que una está sobre la otra exige reglas geométricas de solapamiento o de posición relativa entre las detecciones, sin requerir todavía persistencia temporal ni mantenimiento de identidad. Las condiciones de Nivel 3 involucran dos o más entidades independientes cuya co-ocurrencia espacial o temporal constituye el riesgo, como la maquinaria pesada próxima a un peatón. Exceden la capacidad del detector cuadro a cuadro, porque requieren un módulo que evalúe relaciones geométricas entre entidades y las estabilice en el tiempo, y en ese nivel interviene el tracker MOT para preservar la identidad de cada objeto durante el intervalo de evaluación.

La Tabla 20 presenta las seis condiciones seleccionadas organizadas por nivel, con su código, el tipo de condición, la evidencia visual esperada, el componente del sistema responsable de su evaluación y una estimación cualitativa de la dificultad de detección OVD.

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

***Nota****.* “Componente evaluador” indica qué módulos participan en la evaluación. “OVD cuadro a cuadro” (una o más consultas al detector por cuadro), “OVD + contexto espacial intracuadro” (relaciones geométricas entre detecciones del mismo cuadro) y “OVD + MOT + razonamiento contextual” (persistencia temporal de trayectorias y lógica relacional). “Dificultad OVD estimada” es una valoración cualitativa basada en la degradación documentada de los modelos OVD ante atributos de granularidad fina, en la discrepancia de distribución y vocabulario en dominios especializados y en el menor desempeño frente a detectores ajustados en entornos de construcción (Bianchi et al., 2024; Jiang et al., 2024; Abdalwhab et al., 2025). No se pondera la dificultad del razonamiento contextual.

La selección prioriza condiciones con alta observabilidad visual y disponibilidad plausible de datos, pero dos de ellas exigen cautela desde el diseño experimental. CR-03 y CR-04 comparten una dificultad de evidencia negativa, porque la condición no se define por la presencia de un objeto sino por la ausencia de un elemento de protección, sea el sistema anticaídas sobre la persona en altura o la baranda en el borde de la losa. Esa ausencia depende fuertemente de la escala del objeto en imagen, del ángulo de cámara, de la oclusión y de la resolución disponible. CR-04 suma además una ambigüedad geométrica, ya que determinar si un borde es efectivamente elevado requiere información tridimensional que la proyección bidimensional de la cámara no preserva por completo.

Las condiciones de Nivel 3 no son evaluables mediante prompts integrados. Requieren detectar las entidades componentes y razonar sobre su relación, y en CR-06 la evaluabilidad presupone además una cámara fija y una parametrización espacial externa al prompt, como el polígono de la zona restringida definido por el operador. Este supuesto queda explícito desde esta etapa porque condiciona tanto el diseño experimental como la implementación del razonamiento contextual. En un escenario real varias condiciones pueden co-ocurrir sobre la misma persona, y el sistema las trata como unidades ortogonales, lo que simplifica la evaluación a costa de no explotar su correlación como señal de refuerzo. La resolución, el ángulo de cámara, la iluminación y la oclusión atraviesan a todas las condiciones y deben documentarse como variables experimentales para interpretar el desempeño observado.

##### 17.1.5.2. Patrones de riesgo y criterios de activación

Sobre la unidad de análisis definida en la sección 17.1.3, el protocolo fija para cada patrón una severidad, una regla temporal de confirmación y, cuando corresponde, criterios espaciales o relacionales de activación. Las definiciones tienen carácter analítico, y los valores numéricos que las acompañan son orientativos salvo donde se declaran como decisión de protocolo.

La severidad de un patrón refleja el perfil temporal de la condición, entendido como la velocidad con la que la exposición observable puede escalar hacia un incidente y la gravedad potencial de sus consecuencias. En articulación con el framework de métricas, orienta la urgencia operativa del patrón, las ventanas funcionales de persistencia y los objetivos del tiempo a la primera detección (TTFD) y de latencia de alerta del sistema, pero no determina por sí sola el costo computacional del pipeline, que el framework mide por separado. Se distinguen tres niveles. Cada uno se define como una categoría metodológica de prioridad temporal, fundamentada en el perfil temporal de consecuencias asociado a cada tipo de exposición, mientras que la relevancia preventiva de las condiciones subyacentes está establecida en la sección 16.2. La severidad ordena prioridades temporales del protocolo y no constituye una calificación normativa de la situación observada.

El **nivel crítico** corresponde a condiciones con potencial de escalada rápida hacia daño grave, como la exposición en altura sin protección visible o la interacción próxima entre peatones y maquinaria en operación, y justifica las ventanas de persistencia más cortas y los objetivos más exigentes de TTFD y de latencia de alerta. **El nivel alto** corresponde a exposiciones sostenidas que eliminan una barrera de protección sin producir por sí mismas el incidente, como la ausencia de casco en zona activa de obra o la permanencia en una zona restringida, y admite un compromiso intermedio entre rapidez y control de falsas alarmas. El **nivel medio** corresponde a riesgos latentes o de escalada más lenta, como la ausencia de chaleco reflectivo, cuya escalada depende del movimiento efectivo de vehículos o maquinaria en la zona, y por eso admite mayor acumulación de evidencia antes de confirmar la alerta. Tres niveles ofrecen un balance adecuado entre expresividad y manejabilidad para el alcance del prototipo, sin excluir una extensión posterior si la evaluación experimental lo exigiera.

La persistencia temporal define en qué condiciones una detección instantánea se considera un evento confirmado. Su propósito es reducir la tasa de falsas alarmas derivada de la variabilidad de la detección cuadro a cuadro, ya que el componente OVD introduce fluctuaciones en los puntajes de confianza y puede producir apariciones espurias entre cuadros consecutivos. El criterio se conceptualiza como una ventana temporal mínima durante la cual la condición debe observarse de manera sostenida, o con una proporción mínima de detecciones positivas, antes de que el patrón se considere activo. Las ventanas se expresan en duración y no en número de cuadros, porque la conversión depende del throughput efectivo del pipeline y del hardware de inferencia, y esa conversión corresponde a la instancia de análisis y diseño arquitectónico una vez conocida la tasa de cuadros real. La ventana de persistencia no debe confundirse con el tramo computacional por cuadro ni con la latencia de alerta del sistema, que integra además la confirmación operativa del patrón.

Los rangos se derivan del análisis cualitativo de la velocidad de escalada de cada tipo de riesgo y se fijan de modo compatible con los umbrales orientativos del framework de métricas. Para la severidad crítica se proponen ventanas de 2 a 4 segundos, que confirman la exposición con mínima acumulación de evidencia sin sacrificar la alerta temprana. Para la severidad alta se proponen ventanas de 3 a 5 segundos, con mayor evidencia acumulada para reducir falsos positivos sin perder capacidad de respuesta ante una exposición sostenida. Para la severidad media se proponen ventanas de 5 a 10 segundos, que admiten mayor acumulación en una condición de urgencia relativamente menor. Existe una tensión inherente entre severidad y confiabilidad de la activación, porque las ventanas más cortas que exige un patrón crítico implican menos evidencia y mayor probabilidad de falsos positivos. Este compromiso no tiene resolución analítica a priori y constituye un eje central de la calibración empírica, donde deberá evaluarse la curva de falsos positivos en función de la duración de la ventana para cada patrón.

La activación y la resolución de un patrón pueden utilizar ventanas distintas, siguiendo el comportamiento de histéresis habitual en los sistemas de alarmas industriales, de modo que una interrupción momentánea de la detección por oclusión parcial, por variabilidad del puntaje o por pérdida temporal del track no desactive prematuramente un patrón recién confirmado. La reaparición de la condición después de su resolución constituye un episodio nuevo, y la eventual supresión de notificaciones repetidas se define fuera del motor de patrones. Como valores de protocolo dentro de los rangos anteriores se fijan 4.000 ms de persistencia para la confirmación de PR-01 y 7.000 ms para PR-02, con umbrales de desactivación de 2.000 y 3.000 ms respectivamente. Los tiempos se expresan en milisegundos para conservar su significado ante distintos ritmos efectivos de cuadro.

El motor de patrones, entendido como la abstracción lógica del plano de control introducida en la sección 17.1.3.2, debe evaluar la evidencia acumulada conforme a las reglas declaradas por patrón. Recibe detecciones normalizadas, marcas de tiempo, la configuración de prompts y, cuando corresponde, información de seguimiento o de regiones parametrizadas, y decide sobre esa evidencia si el patrón alcanza los criterios de confirmación o deja de cumplirlos. Para las condiciones de Nivel 1 aplica criterios temporales, que pueden estimarse por proporción de cuadros positivos o por duración mínima de evidencia sin exigir MOT, salvo que la condición deba atribuirse a una persona individual durante toda la secuencia. En el Nivel 2 incorpora relaciones espaciales intracuadro, y en el Nivel 3 evalúa relaciones sostenidas entre entidades o entre una entidad y una región parametrizada, donde el seguimiento temporal adquiere mayor peso metodológico.

La Tabla 21 consolida el catálogo de patrones asociados a las condiciones seleccionadas, con su severidad, el rango orientativo de persistencia, el criterio de activación, el perfil temporal que fundamenta la severidad asignada y el riesgo de falsos positivos asociado a la brevedad de la ventana.

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

***Nota****.* Los rangos de persistencia temporal son orientativos. La columna “Trade-off FP” indica cualitativamente el riesgo de falsos positivos asociado a la brevedad de la ventana de persistencia. La severidad es una clasificación interna del protocolo, fundamentada en el perfil temporal de la condición. No constituye una calificación normativa de la situación observada. La relevancia preventiva de las condiciones se fundamenta en la sección 16.2. Fuente: elaboración propia.

Los patrones PR-05 y PR-06 requieren criterios de activación combinada, que se definen a nivel conceptual. Para PR-05 la activación exige la detección simultánea de al menos una entidad clasificable como maquinaria de obra, como una excavadora, una retroexcavadora, un camión volquete o una grúa, y de al menos una persona, con una relación de proximidad inferior a un umbral configurable. Toda métrica de proximidad calculada en coordenadas de imagen es una medida geométrica bidimensional aproximada y no una distancia física, porque la perspectiva de la cámara altera las distancias aparentes. La evaluación debe sostenerse durante el intervalo de persistencia del patrón, lo que exige trayectorias suficientemente estables de las entidades involucradas.

Para PR-06 la activación exige la detección de al menos una persona cuya posición representativa esté contenida en un polígono predefinido que representa la zona restringida. El polígono forma parte de la parametrización del sistema, es configurable por el operador y externo al prompt, y presupone una cámara fija, supuesto adoptado para el alcance del prototipo experimental. La permanencia debe sostenerse durante el intervalo de persistencia, lo que implica seguimiento temporal cuando la persistencia se compute por entidad individual. En ambos patrones los cambios de identidad, las pérdidas temporales de trayectoria y las reasociaciones erróneas del tracker pueden interrumpir espuriamente la evaluación o reiniciar indebidamente la ventana, por lo que deben contemplarse en el diseño del razonamiento contextual y cuantificarse en la validación experimental.

##### 17.1.5.3. Diseño de prompts OVD

Las consultas textuales operan como interfaz del modelo OVD y su formulación altera el desempeño del detector. El análisis de modelos OVD documentó que cambios leves de redacción modifican significativamente el comportamiento de los modelos visión-lenguaje (Zhou et al., 2022), que el embedding textual de clase se genera a partir de los prompts ingresados al encoder y su alineación con las representaciones visuales requiere ajuste específico para la detección (Gu et al., 2021; Du et al., 2022), y que la evaluación se vuelve especialmente exigente ante atributos de granularidad fina, vocabularios dinámicos y clases negativas semánticamente cercanas, como muestran los benchmarks FG-OVD y OVDEval (Bianchi et al., 2024; Yao et al., 2024). Por eso el protocolo trata el diseño de prompts como una variable de ingeniería del sistema, gestionada con el mismo rigor que la selección de modelos o la definición de métricas, y la resuelve mediante contraste reproducible. Dos definiciones ordenan ese contraste. La matriz de prompts es el conjunto acotado de formulaciones alternativas que se ensayan para una misma condición. La composición del vocabulario activo es el conjunto de descripciones o consultas que el modelo evalúa en simultáneo dentro de una corrida determinada.

Para cada condición del catálogo (Tabla 20) se diseñan variaciones de prompt a lo largo de cuatro ejes controlados, de modo que la selección quede documentada con evidencia reproducible. El primer eje es la estructura sintáctica, que abarca frases nominales simples, oraciones descriptivas con contexto y variaciones en el uso de artículos, preposiciones o modificadores. Para la detección de casco, por ejemplo, las formulaciones “hard hat”, “person wearing hard hat” y “safety helmet on worker” difieren en estructura gramatical aunque refieren a conceptos visualmente relacionados. Se incluyen además variantes con template, como “*a photo of a [CLASS]*”, porque en los modelos de la familia CLIP transformar una etiqueta aislada en una descripción breve reduce la brecha con los textos naturales del preentrenamiento y puede mejorar el desempeño (Radford et al., 2021). El protocolo compara prompts con y sin template sin presuponer cuál resultará superior en el dominio de la construcción.

El segundo eje es el nivel de especificidad del vocabulario, desde términos genéricos hasta terminología propia del dominio. Las formulaciones “person”, “worker” y “construction worker” representan grados crecientes de especificidad para la misma entidad. La hipótesis metodológica es que los términos más específicos pueden mejorar la precisión al reducir la ambigüedad de la consulta y aproximarla al contexto de obra, aunque también pueden reducir el recall si la formulación resulta demasiado restrictiva o menos compatible con las representaciones aprendidas durante el preentrenamiento. Por eso la elección entre vocabulario genérico y específico se trata como variable experimental y no como una decisión evidente.

El tercer eje es la estrategia de detección y distingue tres familias identificadas con un código. La estrategia directa (E-DIR) formula un prompt que intenta describir la condición de riesgo completa, incluida la presencia o ausencia del elemento relevante. La estrategia indirecta (E-IND) consulta entidades visibles por separado, por ejemplo “person” y “hard hat” como prompts independientes, y reconstruye la condición mediante lógica externa al modelo que asocia las detecciones y verifica sus relaciones geométricas. La estrategia híbrida (E-HYB) combina consultas de ambos tipos bajo una regla de composición explícita. La distinción no es terminológica, porque los modelos OVD permiten consultar categorías o descripciones mediante texto pero no resuelven de forma robusta todos los atributos, posiciones y relaciones que implica una condición compuesta (Gu et al., 2021; Yao et al., 2024). La estrategia indirecta resulta especialmente pertinente para las condiciones cuya evidencia es la ausencia de un EPP, como CR-01, CR-02 y CR-03, y para las que requieren relaciones espaciales intracuadro, como CR-03 y CR-04. Su ganancia potencial en robustez semántica se paga con mayor complejidad de razonamiento y con una posible carga adicional de inferencia por cuadro, cuya magnitud deberá verificarse contra el presupuesto de latencia del framework de métricas. El protocolo compara ambas estrategias en todas las condiciones en que sean aplicables, sin presuponer la superioridad de ninguna, y los códigos identifican las variantes en el diseño arquitectónico y en la evaluación experimental.

El cuarto eje es la composición del vocabulario activo y evalúa cómo el conjunto de prompts simultáneamente activos afecta el desempeño de cada uno. FG-OVD muestra que varios detectores open-vocabulary tienen dificultades para distinguir y asignar correctamente descripciones finas cuando el vocabulario incluye clases negativas semánticamente cercanas al objetivo (Bianchi et al., 2024). En E-OVRT-VDP el sistema busca simultáneamente varias condiciones y entidades, como “hard hat”, “person”, “reflective vest” y “scaffolding”, y se plantea la hipótesis de que prompts semánticamente próximos compiten entre sí y generan confusiones de clasificación. Por eso cada prompt se evalúa tanto en aislamiento como dentro del vocabulario completo del sistema. El tamaño del vocabulario se considera además una variable experimental, porque puede afectar la precisión y el costo de inferencia de manera dependiente de la arquitectura. Las familias YOLO orientadas a open-vocabulary precomputan los embeddings textuales fuera del ciclo de inferencia, mientras que Grounding DINO procesa el par imagen-texto en cada consulta y un vocabulario mayor encarece la fusión cross-modal (Cheng et al., 2024; Wang et al., 2025; Liu et al., 2024). El detalle arquitectónico se desarrolla en el análisis de modelos OVD, y la consecuencia de diseño es que la cantidad de prompts sostenible dentro del presupuesto de latencia depende del modelo, de la sintaxis concreta, de la resolución de entrada y del hardware, por lo que su efecto se mide y no se presupone.

Los prompts primarios se formulan en inglés, porque los corpus de la línea de preentrenamiento de base de los modelos visión-lenguaje candidatos, como CLIP, Conceptual Captions y CC12M, se construyeron sobre material predominantemente en inglés (Radford et al., 2021; Sharma et al., 2018; Changpinyo et al., 2021). Aunque no todos los modelos publican una caracterización lingüística equivalente de sus datos de entrenamiento, la evidencia disponible justifica el inglés como idioma primario de consulta para favorecer la compatibilidad con los patrones lingüísticos dominantes del preentrenamiento. Como la plataforma se desarrolla en un contexto académico argentino y el idioma natural de trabajo de operadores e investigadores es el español, la traducción de las descripciones de condiciones al inglés se realiza manualmente durante el diseño de prompts. Como línea complementaria podrá explorarse la ejecución de prompts formulados directamente en español o mediados por traducción automática, para cuantificar la eventual degradación asociada a la brecha lingüística y documentar si alguno de los modelos candidatos ofrece soporte multilingüe funcional para el dominio.

El catálogo de prompts candidatos contempla, para las condiciones de Nivel 1 y Nivel 2, formulaciones directas, variantes léxicas y estrategias indirectas o descompuestas según el tipo de evidencia visual que se busca activar en el modelo. Para las condiciones de Nivel 3 no se proponen prompts integrados, porque su evaluación requiere razonamiento contextual sobre múltiples entidades, y se consideran prompts orientados a las entidades componentes, cuyos resultados utilizan el motor de patrones. El catálogo completo de formulaciones candidatas por condición y estrategia se consolida en la Tabla C.1 del Anexo C. La inclusión de candidatos para CR-03 y CR-04 no implica que ambas condiciones dispongan de soporte completo de evaluación en datasets públicos. Sus prompts permiten explorar formulaciones y detectar entidades o estados visuales parciales, pero la validación del patrón completo depende de contar con datos que representen la condición operacionalizada, por lo que los resultados deberán distinguir entre el desempeño del prompt sobre componentes visuales y la evaluación integral de la condición de riesgo.

##### 17.1.5.4. Protocolo de evaluación y congelamiento de prompts

El protocolo de evaluación determina, para cada condición de riesgo y cada modelo OVD candidato, qué formulación de prompt ofrece el mejor desempeño dentro del framework adoptado para el componente OVD, con lectura prioritaria sobre AP@0.5 y Precision/Recall en el punto operativo declarado. Adapta al alcance y a los recursos de un proyecto académico las prácticas de evaluación de FG-OVD y OVDEval (Bianchi et al., 2024; Yao et al., 2024). Este protocolo fija la estructura procedural de las pruebas en cinco fases.

**Fase 1. Preparación de la referencia.** Para cada condición se selecciona un subconjunto del inventario de datasets documentado en la estrategia de datos que contenga anotaciones de verdad fundamental relevantes, con variación en iluminación, ángulo de cámara, grado de oclusión y escala dentro de lo que los datos permitan. Cuando el ground truth existente no cubra directamente la condición, por ejemplo si el dataset anota “casco” pero no “persona sin casco”, se generan anotaciones complementarias sobre un conjunto acotado de imágenes con doble anotación independiente sobre al menos un 20 % del conjunto. Para etiquetas categóricas se calcula el coeficiente kappa de Cohen como indicador de confiabilidad interanotador (Cohen, 1960), y cuando la anotación involucra bounding boxes el acuerdo se evalúa además mediante IoU promedio o proporción de coincidencias por encima de un umbral predefinido. El requisito rige para toda anotación producida por el proyecto. Cuando la referencia se reutilice de la fuente sin reanotación, la doble anotación no aplica y la ausencia de una medida de acuerdo debe declararse como limitación del material. Como objetivo operativo se procura contar con al menos 200 instancias positivas anotadas por condición, complementadas con casos negativos cuando resulten necesarios para estimar precisión y falsos positivos. Cuando una condición o un estrato no alcance ese piso, se reporta el n efectivo con intervalos de confianza al 95 % obtenidos por bootstrap sobre las unidades de evaluación y se abstiene de ordenar variantes cuyos intervalos se superpongan.

**Fase 2. Matriz experimental.** Se construye la matriz de combinaciones a evaluar, donde cada celda es una tupla de modelo OVD, condición de riesgo, variación de prompt y contexto de vocabulario. El último término responde al cuarto eje y distingue la evaluación en aislamiento, donde el prompt o el conjunto mínimo que exige la estrategia indirecta es el único vocabulario activo del modelo, de la evaluación en contexto completo, donde opera junto con los demás prompts activos del sistema. Los hiperparámetros del modelo, como el umbral de confianza y el umbral de NMS, se fijan constantes durante toda la evaluación para garantizar comparabilidad entre variaciones, y si se evalúan múltiples umbrales se documentan como variable adicional de la matriz.

**Fase 3. Ejecución.** Para cada combinación de la matriz se ejecuta la inferencia en condiciones controladas, con hardware, resolución de entrada y preprocesamiento constantes, y se registran por imagen las detecciones con sus coordenadas, puntaje de confianza y etiqueta en un formato estructurado que permita el cálculo posterior de métricas y la reproducción de los experimentos.

**Fase 4. Cálculo de métricas.** Para cada tupla se calculan las métricas definidas en el framework para el componente OVD, junto con el puntaje de confianza medio de los verdaderos positivos como indicador complementario de la estabilidad de la respuesta ante cada formulación. Para las condiciones evaluadas con estrategia indirecta se calculan también las métricas de cada entidad componente por separado, de modo que pueda identificarse si la degradación proviene de la detección de las entidades individuales, del atributo visual evaluado o de la lógica de asociación.

**Fase 5. Selección y congelamiento.** Se construye una matriz de resultados que identifica, para cada condición, la combinación de modelo y prompt que maximiza el criterio de selección definido en el framework de métricas. Los resultados se analizan por condición y de manera transversal, buscando patrones sistemáticos como la superioridad consistente de los prompts con template o de la estrategia indirecta en las condiciones de EPP, y se documenta la sensibilidad de cada modelo al contexto de vocabulario cuantificando la diferencia entre aislamiento y contexto completo. Las formulaciones seleccionadas se congelan antes de las corridas comparativas posteriores.

El protocolo produce como salida un registro estructurado de métricas por combinación, que alimenta la selección de prompts primarios para la configuración del sistema en la instancia de análisis y diseño arquitectónico y el análisis de sensibilidad y robustez de la validación experimental. Ese registro, junto con los scripts de ejecución y los datasets utilizados, constituye el artefacto de reproducibilidad del protocolo.

#### 17.1.6. Estrategia de datos, benchmarks y partición

##### 17.1.6.1. Alcance y criterios de selección

La estrategia de datos responde a las preguntas rectoras P-E1-03 y P-E1-08 formuladas en la sección 16.7.3. Su función es seleccionar fuentes públicas que puedan gestionarse dentro del proyecto, determinar qué condiciones CR-01 a CR-06 permiten evaluar y establecer las reglas de datos para una eventual comparación entre la línea base zero-shot y una variante ajustada al dominio. La aptitud de una fuente se juzga respecto de la condición de riesgo operacionalizada, no por la presencia aislada de alguna de sus entidades.

El inventario distingue fuentes de gestión directa y benchmarks de referencia. Las primeras pueden descargarse, normalizarse, particionarse y utilizarse para evaluación o ajuste. Los segundos se reservan para verificar módulos específicos bajo protocolos reconocidos y no sustituyen la validación en construcción civil. Se excluyen los corpus generalistas empleados para preentrenar los modelos, las colecciones sin acceso o condiciones de uso verificables y las fuentes exclusivamente sintéticas que carezcan de validación manual o contraste documentado con escenas reales.

En esta sección, una fuente retenida es metodológicamente admisible para consideración posterior. La denominación no implica utilización efectiva ni asignación definitiva. Cada fuente debe quedar asociada a ajuste, validación interna o banco de evaluación antes de la ejecución. Esta sección fija criterios y restricciones. La materialización de las particiones y los resultados se documenta en las secciones posteriores.

Los criterios C1 a C7 de la Tabla 22 no tienen pesos fijos. Su relevancia depende del papel previsto para cada fuente y del nivel de evaluación que deba sostener.

**Tabla 22**

*Criterios de evaluación para la selección de fuentes de datos*

| **#** | **Dimensión** | **Descripción operativa** |
| --- | --- | --- |
| C1 | Pertinencia al dominio | Presencia de escenas de construcción, industria o trabajadores con EPP. Se valora la diversidad de iluminación, ángulo de cámara, escala y condiciones ambientales. |
| C2 | Cobertura de las condiciones operativas | Grado en que las anotaciones permiten evaluar una o más condiciones CR-01 a CR-06. La presencia de entidades relacionadas no equivale a cobertura de la condición completa. |
| C3 | Compatibilidad semántica | Posibilidad de mapear etiquetas, descripciones y granularidad de anotación al vocabulario activo y a las reglas de evaluación de forma explícita y reproducible. |
| C4 | Soporte temporal | Disponibilidad de secuencias, anotaciones cuadro a cuadro y, cuando corresponda, identidades persistentes para seguimiento o evaluación temporal. |
| C5 | Calidad de anotación | Exhaustividad y consistencia de cajas, máscaras o relaciones según el uso previsto. Se prefieren anotaciones manuales con control de calidad documentado. |
| C6 | Condiciones desafiantes | Presencia de oclusiones, baja iluminación, movimiento, multitudes o cambios de escala que permitan evaluar robustez en escenas próximas al uso previsto. |
| C7 | Viabilidad de gestión y uso | Formato estandarizado o convertible, acceso verificable, procedencia identificable y licencia o condiciones de uso compatibles. La ausencia de términos explícitos mantiene la fuente en estado condicional hasta su verificación. |

*Nota.* C4 se aplica únicamente cuando la fuente se destina a seguimiento, continuidad temporal o alertas por episodio. La ausencia de soporte temporal no invalida una colección apropiada para percepción por imagen o estado por persona.

##### 17.1.6.2. Fuentes de gestión directa, cobertura y brechas

Cuatro colecciones se retienen como candidatas de gestión directa por su pertinencia para CR-01 y CR-02, su disponibilidad y su viabilidad de integración. La Tabla 23 resume la cobertura que ofrecen, su condición de uso, los papeles que podrían asumir y la restricción principal de cada una. Esos papeles son alternativas metodológicas y no una reconstrucción de la utilización posterior.

**Tabla 23**

*Fuentes retenidas para gestión directa y papel metodológico posible*

| **Fuente y volumen o versión** | **Cobertura** | **Formato y condición de uso** | **Papel posible** | **Restricción principal** |
| --- | --- | --- | --- | --- |
| SHEL5K (Otgonbold et al., 2022). 5.000 imágenes. | CR-01 directa. | Pascal VOC. Licencia CC BY 4.0. | Ajuste o evaluación de CR-01, con asignación exclusiva. | No cubre chaleco ni condiciones espaciales o relacionales. |
| CHV (Wang et al., 2021). 1.330 imágenes. | CR-01 y CR-02. | Formato nativo por inspeccionar. El paquete no presenta una licencia formal y exige citar la fuente. | Ajuste o evaluación de CR-01 y CR-02, sujeto a verificación de uso. | Deben verificarse los términos de acceso, transformación y redistribución. |
| construction_site_safety. Roboflow Universe, versión 27. | CR-01 y CR-02. | YOLO mediante Roboflow. Licencia registrada CC BY 4.0. | Ajuste de dominio o evaluación, con asignación exclusiva. | Exige deduplicación por linaje y separación respecto del banco de evaluación. |
| ppe_siabar. Roboflow Universe, versión 1. | CR-01 y CR-02. | YOLO mediante Roboflow. Licencia registrada CC BY 4.0. | Ajuste de dominio o evaluación complementaria, con asignación exclusiva. | Requiere curación y una fuente independiente para evaluar generalización. |

*Nota.* Los papeles indicados no constituyen una asignación efectiva y son mutuamente excluyentes dentro de una misma comparación principal.

Las demás colecciones no se incorporan al uso principal cuando su acceso, licencia, dominio o cobertura no aportan una base defendible para el núcleo. La exclusión delimita su papel dentro del protocolo y no constituye una evaluación general de su calidad científica. MOCS conserva un alcance exploratorio por su contenido de maquinaria y trabajadores.

**Tabla 24**

*Fuentes no retenidas para el uso principal y motivo metodológico*

| **Fuente** | **Motivo de exclusión o alcance residual** |
| --- | --- |
| SH17 | La licencia CC BY-NC-SA 4.0 y el predominio de escenas industriales limitan su adopción como fuente principal del núcleo. |
| Pictor-PPE | La licencia no pudo verificarse y la versión pública es parcial. Estas condiciones impiden una gestión y redistribución reproducibles. |
| Construction-PPE | La licencia atribuida como AGPL-3.0 y su aplicabilidad al paquete de datos requieren verificación. La cobertura de EPP ya está atendida por fuentes retenidas, sin un aporte diferencial suficiente. |
| GDUT-HWD y SHWD | La licencia de los paquetes no está verificada y la condición principal ya queda cubierta. Se conservan como referencia, no como insumo gestionado. |
| SODA | Aporta contexto de obra, pero su cobertura se orienta a condiciones fuera del núcleo y no representa de forma nativa CR-01 o CR-02. |
| MOCS | La copia pública es parcial. Su utilidad se limita a exploraciones sobre maquinaria, vehículos y trabajadores, sin uso principal en ajuste o evaluación de EPP. |

*Nota.* Las licencias consignadas son las que declara cada paquete de datos. Cuando la declaración proviene de un repositorio de código, de una publicación o de una copia y no del paquete original, la fuente se mantiene en estado condicional.

El cruce entre las fuentes retenidas y el catálogo muestra un soporte sólido para CR-01 y adecuado para CR-02. CR-03 y CR-04 mantienen brechas directas, mientras que CR-05 y CR-06 carecen de cobertura nativa de la condición completa. La Tabla 25 sintetiza esa diferencia y su consecuencia metodológica.

**Tabla 25**

*Cobertura de datos por condición y consecuencia metodológica*

| **Condición** | **Nivel de cobertura** | **Fuentes retenidas o apoyo** | **Uso metodológico definido** |
| --- | --- | --- | --- |
| CR-01 — Persona sin casco | Sólida | SHEL5K, CHV, construction_site_safety y ppe_siabar. | Integra el núcleo obligatorio. Admite evaluación directa o composición del estado por persona. |
| CR-02 — Persona sin chaleco reflectivo | Adecuada | CHV, construction_site_safety y ppe_siabar. | Integra el núcleo obligatorio, con menor redundancia de fuentes que CR-01. |
| CR-03 — Trabajo en altura sin anticaídas | Brecha directa | No existe una fuente retenida con la condición completa. | Sólo permite evaluación exploratoria de componentes o material complementario controlado. |
| CR-04 — Borde elevado desprotegido | Brecha directa | No existe una fuente retenida con la condición completa. | Se mantiene como extensión condicionada y no bloquea la aceptación del núcleo. |
| CR-05 — Maquinaria cerca de peatones | Sin cobertura directa retenida | Se requieren entidades relacionadas y evidencia temporal. | La evaluación depende de material específico y lógica contextual. |
| CR-06 — Persona en zona restringida | Sin cobertura directa retenida | Se requieren un polígono externo y una cámara fija. | La evaluación depende de parametrización espacial externa al prompt. |

***Nota****.* La cobertura se refiere a la posibilidad de evaluar la condición operativa completa y no sólo a la presencia de algunas de sus entidades en una colección.

Las cuatro fuentes retenidas permiten estudiar el núcleo, pero no sostienen por sí solas conclusiones sobre altura, zonas restringidas, relaciones peatón-maquinaria o desempeño en obra no controlada. La transferibilidad se interpreta según la proximidad visual al dominio, la diversidad de escalas, la presencia de negativos y la correspondencia entre anotaciones y condición evaluada.

Cuando una condición brechada permanezca dentro del alcance exploratorio, se prioriza primero la curación de fuentes públicas con licencia compatible. Si la cobertura continúa siendo insuficiente, se recurre a anotación complementaria acotada y, en última instancia, a material controlado del EBE. La ampliación debe aplicar las salvaguardas de la sección 17.1.10 y aportar evidencia interpretable sin desplazar la evaluación del núcleo.

La evaluación temporal exige además un material construido para ese fin, porque ninguna de las fuentes retenidas aporta secuencias con episodios anotados de las condiciones del núcleo. Ese banco se construye con dos bloques de procedencia y control experimental distintos, un rodaje guionado registrado con el hardware de captura del prototipo y un lote de obra real no guionada obtenido de fuentes públicas, que aporta tiempo en cumplimiento y permite medir especificidad. Cada clip conserva su procedencia y su grado de control como atributo, y la referencia de episodios se congela antes de reportar.

##### 17.1.6.3. Asignación de roles y partición experimental

Antes de ejecutar, cada fuente retenida se asigna a ajuste, validación interna del ajuste o banco de evaluación. Una fuente destinada al ajuste no integra el banco de evaluación de la comparación principal, aun cuando sus particiones nominales sean disjuntas. Esta regla es más restrictiva que la separación de imágenes y busca controlar duplicados, derivados o linajes comunes entre colecciones.

Si la rama de ajuste fino se habilita conforme a la sección 17.1.9, se limita a CR-01 y CR-02 y utiliza fuentes con cobertura, licencia y formato compatibles. El conjunto de entrenamiento se mantiene dentro del rango orientativo de 500 a 2.000 imágenes fijado por el protocolo. Su composición, la conversión de formatos y las operaciones de aumento de datos se declaran antes de entrenar. La línea base zero-shot y la variante ajustada se evalúan sobre el mismo banco congelado, sin presuponer que el ajuste deba resultar superior. La comparación debe informar tanto la ganancia en dominio como la retención de capacidades abiertas. Las proporciones concretas y cualquier desviación del rango se justifican durante la implementación.

**Tabla 26**

*Condiciones metodológicas para la partición de datos*

| **Condición** | **Descripción** |
| --- | --- |
| Disyunción estricta | Ninguna unidad del banco de evaluación puede aparecer en entrenamiento, ni directamente ni mediante derivados o aumento de datos. |
| Banco de evaluación común | La línea base zero-shot y las variantes ajustadas se evalúan sobre el mismo material y con las mismas reglas. |
| Semilla reproducible | Toda partición aleatoria registra la semilla y el procedimiento necesarios para regenerarla. |
| Particiones publicadas | Cuando la fuente dispone de una partición oficial, se la revisa antes de redefinirla. Cualquier apartamiento requiere una justificación explícita. |
| Rango protocolar de entrenamiento | El subconjunto de ajuste se orienta a 500–2.000 imágenes. La composición se congela antes de iniciar el entrenamiento. |
| Deduplicación cruzada | Cuando se combinan fuentes, se verifican duplicados y casi duplicados, en especial en colecciones obtenidas de la Web o mediante contribución distribuida. |
| Congelamiento previo | El banco de evaluación queda definido antes de entrenar y no interviene en calibración, selección de hiperparámetros, selección de checkpoints ni aumento de datos. La calibración de umbrales de decisión, que no modifica el modelo, se admite sobre una mitad predeclarada del banco, disjunta de aquella sobre la que se informan las métricas. |

##### 17.1.6.4. Benchmarks de referencia para seguimiento

Las métricas de seguimiento basadas en identidades persistentes sólo son defendibles cuando existen secuencias anotadas con trayectorias. Por ese motivo, MOT17 y OVT-B se incorporan como benchmarks de referencia. Su función es verificar el módulo de seguimiento y su instrumentación bajo protocolos conocidos. No sustituyen la evaluación de las condiciones de riesgo en construcción civil.

**Tabla 27**

*Benchmarks de referencia para el módulo de seguimiento*

| **Benchmark** | **Escala y licencia registrada** | **Métricas previstas** | **Función en el protocolo** | **Límite de interpretación** |
| --- | --- | --- | --- | --- |
| MOT17 | 14 secuencias reales, operacionalizadas como 42 entradas al considerar DPM, Faster R-CNN y SDP. CC BY-NC-SA 3.0. | MOTA, IDF1 y HOTA. | Verificar la implementación local y el cálculo de métricas. Permite contrastar con resultados públicos de trackers como ByteTrack y OC-SORT. | Seguimiento de peatones. No representa obra ni condiciones de riesgo. |
| OVT-B | 1.973 videos, 637.608 cajas y 1.048 categorías. Apache-2.0 registrada en el repositorio oficial. | TETA, con LocA, ClsA y AssA. | Ejercitar la integración OVD+MOT bajo vocabulario abierto y trayectorias de múltiples categorías. | No declara cobertura específica del dominio de la construcción. |

***Nota****.* TrackingNet y LaSOT se excluyen porque corresponden a seguimiento de objeto único. OVT-B se prioriza sobre OV-TAO por su mayor escala. TETA es Track Every Thing Accuracy y se descompone en LocA, ClsA y AssA, que miden localización, clasificación y asociación. Las referencias primarias son Milan et al. (2016) para MOT17 y Liang y Han (2024) para OVT-B.

MOT17 responde a una pregunta de corrección de implementación y reproducibilidad. OVT-B permite observar la integración entre detección open-vocabulary y asociación temporal bajo un vocabulario amplio. Ninguno habilita inferencias directas sobre desempeño en obra. Esa validación permanece separada.

##### 17.1.6.5. Licencias, ética y logística de datos

El uso de los datos se limita a investigación académica y no contempla reconocimiento facial, identificación individual ni tratamiento biométrico. Para material propio rigen las salvaguardas de minimización y consentimiento de la sección 17.1.10.

Las condiciones de uso son heterogéneas. CHV no presenta una licencia formal del paquete, y la licencia de un artículo, repositorio o código no se traslada por inferencia al conjunto de datos. Antes de descargar, combinar o publicar derivados, se verifican los términos aplicables y se registran la procedencia, la versión o fecha de acceso, la licencia y las transformaciones.

La gestión comprende adquisición, verificación de integridad, inspección del formato, normalización, conversión, partición, deduplicación y congelamiento. Cuando se habilita el ajuste fino, los subconjuntos de entrenamiento y validación interna se transfieren al TN Mendieta. El banco de evaluación permanece separado y la inferencia comparativa se ejecuta en el CPN. La logística por fuente se detalla en la Tabla C.3 del Anexo C.

Esta estrategia proporciona soporte defendible para CR-01 y CR-02 y conserva las demás condiciones como extensiones condicionadas. Toda afirmación posterior sobre desempeño depende de la procedencia, el papel experimental y la partición declarados.

#### 17.1.7. Framework de métricas, viabilidad operativa y presupuesto de latencia

##### 17.1.7.1. Propósito, alcance y principio de aplicabilidad

El framework responde a las preguntas rectoras P-E1-06 y P-E1-01. La primera exige evaluar de manera integral la detección open-vocabulary, el estado observable de cada persona y la capacidad de la plataforma para producir alertas temporales trazables. La segunda requiere convertir la noción de baja latencia en tramos medibles y en referencias compatibles con el hardware disponible. La sección fija unidades de análisis, métricas, condiciones de aplicación, criterios de lectura y requisitos mínimos de instrumentación. No presenta resultados ni presupone que toda métrica pueda calcularse en cualquier corrida.

La factibilidad no se determina mediante una cifra aislada. Una configuración puede localizar objetos con precisión y, aun así, asociar incorrectamente el equipo de protección a la persona, perder continuidad temporal o confirmar una alerta demasiado tarde. Por ese motivo, la evidencia se organiza en tres niveles enlazados. El primero evalúa percepción por imagen, el segundo evalúa estado por persona y el tercero evalúa alertas por episodio. Este último representa a la plataforma completa porque incorpora la estabilización temporal, la decisión del patrón y el registro de la alerta. Las mediciones de rendimiento complementan esa jerarquía y permiten juzgar si la cadena sostiene el ritmo de la fuente dentro del presupuesto declarado.

Cada métrica debe acompañarse de un estado explícito. Puede haber sido calculada, ser aplicable pero no calculada, resultar no aplicable por ausencia de datos o instrumentación, o producir un valor no interpretable por insuficiencia del denominador o incompatibilidad entre corridas. Estos estados no son equivalentes. Un valor ausente nunca se reemplaza por cero y una métrica no aplicable no se presenta como resultado omitido.

El nivel de compromiso de una métrica es independiente de su estado de aplicabilidad. Una métrica obligatoria es la que el núcleo del prototipo debe reportar cuando sus precondiciones se cumplen. Una métrica deseable amplía el análisis y su omisión justificada no invalida el protocolo. Un tratamiento conceptual conserva valor metodológico aunque requiera datos o módulos que exceden una corrida determinada. Una métrica se considera exigible cuando responde a la pregunta experimental, dispone de una referencia anotada verificable, el módulo que produce la señal existe, el tramo está suficientemente instrumentado y el costo de anotación o procesamiento es compatible con el alcance del proyecto. Bajo estos criterios una métrica puede estar correctamente definida en el framework y aun así no corresponder en una corrida concreta. Si los recursos experimentales no permiten ejecutar todo el repertorio con la misma profundidad, el núcleo evaluativo queda dado por las métricas obligatorias de los tres niveles y por los diagnósticos mínimos del pipeline.

##### 17.1.7.2. Niveles de evaluación y jerarquía de evidencia

El nivel de percepción por imagen determina si el detector localiza las entidades o estados visuales relevantes respecto de una referencia anotada. Su unidad es la imagen y su resultado describe al componente perceptivo. El nivel de estado por persona determina, para cada sujeto evaluable, si la condición derivada coincide con la referencia. En CR-01 y CR-02 esto exige asociar la persona con la evidencia de casco o chaleco y decidir el estado observable correspondiente. La unidad deja de ser la caja aislada y pasa a ser la persona.

El nivel de alerta temporal evalúa episodios. Una detección correcta por cuadro sólo contribuye a este nivel cuando la evidencia se sostiene, satisface la regla del patrón y origina una alerta trazable. La unidad es el episodio anotado, con inicio y cierre definidos. Los clips o intervalos sin episodios positivos se tratan como material negativo y se analizan mediante falsos positivos. No ingresan en precisión, recall ni F1 porque no aportan verdaderos positivos ni falsos negativos de episodio.

Los niveles se relacionan, pero no se sustituyen. El desempeño perceptivo ayuda a explicar el estado por persona, y ambos ayudan a interpretar las alertas, aunque ningún resultado inferior garantiza el superior. La identidad temporal y las métricas de seguimiento se incorporan cuando permiten estudiar continuidad o asociación, pero no reemplazan la evaluación por episodio. La Tabla 28 consolida esta jerarquía junto con las familias de evidencia complementarias.

**Tabla 28**

*Framework de métricas por nivel de evaluación y familia de evidencia*

| **Nivel o familia** | **Unidad evaluada** | **Métricas y medidas** | **Condición de aplicación** | **Lectura dentro del protocolo** |
| --- | --- | --- | --- | --- |
| Percepción por imagen | Imagen y clase | AP@0,5, AP@[0,50:0,95], precisión, recall y F1. | Anotaciones espaciales y regla de asociación explícita. | Mide la salida perceptiva. No representa por sí sola una alerta. |
| Estado por persona | Persona evaluable | Precisión, recall y F1 por condición. Matriz de confusión cuando aporte al diagnóstico. | Referencia que asocie persona y EPP o estado observable. | Captura errores de detección, asociación y derivación del estado. |
| Alerta temporal | Episodio anotado | Precisión, recall y F1 por episodio, t_alert-system, TTFD y SDR. | Inicio y cierre temporal, patrón configurado y alerta trazable. | Representa el comportamiento de la plataforma completa. |
| Material negativo | Clip o intervalo sin episodio positivo | Conteo de falsos positivos, duración observada y FAR/hora derivada. | Referencia temporal negativa y criterio de falso positivo fijado. | Caracteriza activaciones espurias. No ingresa en precisión, recall ni F1. |
| Identidad temporal | Persona o trayectoria | ΔFP_tracking y variación de re-alertas. MOTA, IDF1 y HOTA de forma condicionada. | Identidad temporal habilitada. Las métricas MOT exigen referencia persistente. | Distingue el aporte operativo de la identidad de la calidad MOT clásica. |
| Viabilidad operativa | Corrida y unidad procesada | FPS efectivos, t_G2A, latencias por tramo, uso de VRAM, GPU, RAM y estabilidad. | Tramos instrumentados, régimen y duración declarados. | Determina si la cadena sostiene la fuente sin acumulación de atraso no acotada. |
| Comparación de ajuste | La misma unidad que la línea base | Deltas de AP, precisión, recall y F1, retención open-vocabulary y costo de entrenamiento. | Banco común congelado y separación estricta entre entrenamiento y evaluación. | Mide el efecto de la adaptación. No constituye un nivel evaluativo adicional. |

***Nota****.* AP@0,5 y AP@[0,50:0,95] se reportan como convenciones distintas y no se intercambian. FAR/hora es una tasa derivada del conteo y de la duración negativa observada. Una re-alerta asociada al mismo episodio no es un falso positivo. Las métricas MOT sólo se calculan cuando la referencia conserva identidades persistentes.

##### 17.1.7.3. Métricas adoptadas y reglas de lectura

En percepción por imagen se adoptan AP@0,5 y AP@[0,50:0,95], junto con precisión, recall y F1 en el punto operativo declarado. La regla de correspondencia debe fijar el umbral de intersección sobre unión, el tratamiento de predicciones duplicadas y la correspondencia entre etiquetas de la fuente y vocabulario activo. Las dos variantes de AP se informan por separado, ya que responden a convenciones diferentes. NMS-AP se conserva como referencia conceptual para análisis de vocabulario fino, pero no sustituye las métricas estándar ni constituye un requisito del núcleo (Everingham et al., 2010; Lin et al., 2014; Yao et al., 2024).

En el nivel de estado por persona, la predicción se obtiene después de vincular la evidencia perceptiva con cada sujeto evaluable. Para CR-01 y CR-02, una persona se clasifica según la presencia o ausencia observable del EPP en la región definida por el protocolo. La evaluación usa precisión, recall y F1 por condición. Los errores de asociación forman parte del resultado porque una detección correcta de casco o chaleco no resuelve el estado si se asigna a la persona equivocada. Cuando se comparen estrategias directas, indirectas o híbridas, la unidad y el conjunto de personas evaluables deben permanecer constantes.

En el nivel de alerta, un verdadero positivo es una alerta que corresponde a un episodio anotado conforme a la regla temporal de asociación. Un falso negativo es un episodio evaluable sin alerta válida. Un falso positivo es una alerta sin episodio positivo asociado bajo el mismo criterio. La precisión, el recall y el F1 se calculan sobre episodios positivos. El material negativo se informa mediante el número de falsos positivos y la duración observada. FAR/hora puede presentarse como derivación, pero no sostiene por sí sola una cota operativa cuando la exposición negativa es reducida.

t_alert-system mide el intervalo entre el inicio anotado del episodio y la marca temporal de la unidad visual que satisface la confirmación del patrón y origina el registro de la alerta. Sólo corresponde en corridas con evaluación de patrón, referencia temporal y alerta trazable. TTFD mide el intervalo entre ese inicio y la primera evidencia positiva válida según el criterio declarado. No debe confundirse con la alerta confirmada. SDR expresa qué proporción de la duración o de las unidades temporales válidas mantiene evidencia correcta mientras la condición está activa. Su definición debe indicar si se calcula en tiempo o en cuadros, y sólo admite comparación directa entre corridas con la misma cadencia de muestreo.

La severidad funciona como estrato de lectura y no como métrica. Cuando se reporte desempeño por severidad, cada resultado debe conservar el tamaño muestral, el punto operativo y la condición incluida. No se mezclan niveles de severidad en un agregado sin mostrar el desglose. La prioridad temporal asignada a cada patrón orienta los objetivos de TTFD y t_alert-system, pero no modifica retrospectivamente la referencia anotada ni la definición de un episodio.

La identidad temporal se evalúa primero por su efecto sobre la salida operativa. ΔFP_tracking compara el conteo de falsos positivos entre corridas equivalentes con identidad deshabilitada y habilitada. La unidad del falso positivo debe definirse antes del contraste y mantenerse estable. Las re-alertas o reconfirmaciones del mismo episodio se contabilizan por separado. MOTA, IDF1 y HOTA permanecen disponibles como métricas condicionadas para secuencias con referencia de identidad persistente. Su ausencia no implica que la capacidad de identidad temporal esté fuera del sistema, sino que no corresponde juzgarla mediante métricas MOT sin datos adecuados (Bernardin & Stiefelhagen, 2008; Ristani et al., 2016; Luiten et al., 2021).

La viabilidad operativa se caracteriza mediante la cadencia efectiva, las latencias por tramo, el consumo de recursos y la estabilidad. Los FPS efectivos se calculan sobre unidades realmente procesadas y deben distinguirse de la tasa nominal de captura. La media de latencia se complementa con P50, P95 y P99 cuando se conservan observaciones individuales suficientes. El uso de VRAM, GPU, RAM y CPU se registra junto con el modelo, la resolución y la precisión numérica. Una configuración sólo se considera capaz de sostener la fuente cuando el atraso permanece acotado y no crece de forma sostenida durante la corrida. Las definiciones operativas, el formato de reporte y los criterios de estabilidad de estas medidas se consolidan en la Tabla D.1 del Anexo D.

Toda cifra se informa con la combinación que la produjo, el material o estrato sobre el que se calculó y su denominador. Los agregados pueden sintetizar, pero no reemplazan los desgloses cuando existen fuentes, condiciones o escenarios heterogéneos. Esta regla alcanza tanto a las métricas de calidad como a las temporales y operativas.

##### 17.1.7.4. Comparación entre línea base zero-shot y variante ajustada

La comparación entre una línea base zero-shot y una variante ajustada al dominio busca medir el efecto de la adaptación, no demostrar de antemano que el ajuste sea superior. La línea base se ejecuta primero y conserva el punto de referencia de cada métrica. La variante ajustada se evalúa sobre el mismo banco congelado, con la misma unidad de análisis y el mismo procedimiento, salvo la modificación paramétrica que se desea estudiar. Las reglas de disyunción, deduplicación y congelamiento de datos se establecen en la sección 17.1.6.

El contraste informa el cambio absoluto de cada métrica mediante la diferencia entre la variante ajustada y la línea base. La calidad dentro del dominio se mide con AP, precisión, recall y F1 en los niveles donde corresponda. Los cambios en TTFD, SDR o t_alert-system sólo se calculan cuando ambas variantes se ejecutan sobre video, comparten episodios evaluables y mantienen la misma configuración temporal. La retención open-vocabulary se mide sobre categorías separadas del ajuste y debe informar el valor de referencia, el valor posterior y la variación observada.

El costo de adaptación forma parte del resultado comparativo. Deben registrarse horas de GPU, tiempo total, cantidad de imágenes, parámetros entrenables, procedimiento de ajuste y checkpoints considerados. Ninguna variante se declara mejor a partir de una única métrica. El veredicto debe identificar qué combinación mejoró, sobre qué material, con qué denominador y qué costo o degradación acompañó esa mejora. Si falta una línea base válida, existe filtración entre entrenamiento y evaluación o las unidades no son equivalentes, el delta se declara no interpretable.

##### 17.1.7.5. Presupuesto temporal y referencias por severidad

El presupuesto temporal separa tres naturalezas. La primera corresponde a tramos de captura y procesamiento que pueden instrumentarse como intervalos de ejecución. La segunda es la espera funcional necesaria para acumular evidencia y confirmar un patrón. La tercera corresponde a la distribución de una alerta ya confirmada. Estas magnitudes contribuyen a la oportunidad observada, pero no deben presentarse como si fueran un único costo computacional.

Toda latencia debe declarar el hito inicial, el hito final y el dominio de reloj. Los relojes monotónicos son adecuados para intervalos medidos dentro de un mismo proceso o dominio temporal. No se restan directamente marcas monotónicas de procesos o nodos distintos. En una cadena distribuida, los tramos se correlacionan mediante marcas de la fuente, relojes sincronizados o identificadores que permitan vincular una misma unidad. Cuando no existe una marca confiable de captura, el informe comienza en el primer hito instrumentado y no presenta ese intervalo como latencia completa desde el sensor.

Las métricas temporales asociadas a la alerta se definen mediante diferencias entre hitos correlacionados, no mediante la suma de componentes agregados. Para un episodio evaluable *e*, la definición formal de t_alert-system es la siguiente.

⟦ECUACIÓN: no extraída — ver el .docx⟧

El hito inicial es el comienzo anotado de la condición. El hito final es la marca temporal, en el reloj de la fuente, de la unidad visual que satisface la regla de confirmación y origina la alerta. Ambas marcas deben corresponder al mismo episodio y expresarse en una referencia temporal compatible.

Para una alerta *a* cuyo trayecto externo esté instrumentado, la definición formal de t_alert-notification es la siguiente.

⟦ECUACIÓN: no extraída — ver el .docx⟧

El hito inicial es la marca de publicación con la que la alerta queda disponible para distribución. El hito final es la confirmación verificable del canal instrumentado. Este tramo no incluye t_alert-system. La composición entre ambas métricas sólo es válida cuando cada observación conserva hitos correlacionables y compatibles. Sus percentiles agregados no se suman.

La Tabla 29 ubica estas fronteras dentro de la cadena temporal y las relaciona con los demás tramos y condiciones de instrumentación.

**Tabla 29**

*Tramos temporales y condiciones de instrumentación*

| **Tramo o componente** | **Hito inicial y final** | **Aplicabilidad** | **Regla de reporte** |
| --- | --- | --- | --- |
| Captura a host (capture_to_host) | Marca temporal de captura o lectura → dequeue de la unidad visual. | Sólo cuando la fuente aporta una referencia temporal confiable. | Se informa por separado. Si falta, no se infiere ni se suma a otro tramo. |
| G2A instrumentado (t_G2A) | dequeue → fin de inferencia. | Corridas con detector instrumentado. | Debe declarar sus fronteras. No equivale a sensor → algoritmo cuando la captura queda fuera. |
| Preprocesamiento | dequeue → entrada preparada para el modelo. | Corridas integradas de percepción. | Se desglosa por resolución, normalización y transferencias CPU-GPU. |
| Inferencia | Inicio del modelo → detecciones disponibles. | Toda corrida que evalúe un detector. | Se reporta por modelo, resolución, precisión numérica y tamaño de lote. |
| Identidad temporal | Detecciones → asociaciones o estados por sujeto. | Sólo cuando la identidad esté habilitada. | Se informa con el método, la densidad de escena y el número de unidades. |
| Evaluación de patrón | Evidencia normalizada → actualización del estado del patrón. | Corridas integradas con motor de patrones. | Mide cómputo. No incluye la espera funcional de persistencia. |
| Ventana funcional | Primera evidencia aceptada → criterio de confirmación. | Patrones con persistencia temporal. | Es una regla funcional configurada, no una latencia computacional. |
| Alerta del sistema (t_alert-system) | Inicio anotado del episodio → unidad visual que confirma el patrón y origina la alerta. | Episodio temporal, patrón activo y alerta trazable. | No incluye la notificación externa. Se informa por condición y material. |
| Notificación (t_alert-notification) | Alerta disponible para distribución → confirmación del canal instrumentado. | Sólo cuando exista un canal externo medible. | Es un tramo independiente. No se suman percentiles no correlacionados. |

***Nota****.* G2A = Glass-to-Algorithm. Cada corrida conserva las fronteras temporales y el dominio de reloj de los tramos que reporta.

El tramo computacional reúne el preprocesamiento, la inferencia, la identidad temporal cuando corresponde y la evaluación del patrón. La ventana de evidencia se mantiene separada porque representa acumulación funcional. t_alert-system se obtiene a partir de los hitos del episodio y de la alerta, no mediante la suma de percentiles de componentes.

Para instrumentar la cadena y estimar la plausibilidad del presupuesto se adopta además un modelo de presupuesto de ingeniería con notación propia, separada de las métricas medidas por hitos. B denota la estimación orientativa de un tramo y W una espera funcional. Los componentes sólo se suman cuando son sucesivos y no se solapan.

⟦ECUACIÓN: no extraída — ver el .docx⟧

⟦ECUACIÓN: no extraída — ver el .docx⟧

B_captura-host corresponde al tramo capture_to_host de la Tabla 29 y sólo se incluye cuando la fuente aporta una marca de captura confiable. B_identidad corresponde a la identidad temporal cuando está habilitada y B_reglas al cómputo de la evaluación del patrón. B_alerta es una referencia de plausibilidad y no reemplaza a t_alert-system, que se obtiene de los hitos reales del episodio y de la alerta. La latencia vidrio a alerta de un episodio se aproxima entonces a la suma de TTFD y B_alerta. t_alert-system, medida entre hitos del reloj de la fuente, comprende la reacción perceptiva inicial y la ventana funcional, pero no la cola de procesamiento del cuadro que confirma, que se informa por separado mediante capture_to_host y t_G2A. La estimación orientativa que sigue corresponde a B_procesamiento.

Con el perfil de hardware de referencia, una LAN controlada y modelos orientados a inferencia eficiente, el tramo previo a la acumulación temporal puede ubicarse de manera orientativa entre 35 y 250 ms por unidad procesada. La captura y el transporte pueden aportar del orden de 10 a 50 ms cuando se dispone de una referencia temporal compatible. El preprocesamiento se estima entre 5 y 20 ms, la inferencia entre 15 y 150 ms, la identidad temporal entre 5 y 20 ms cuando se habilita y la evaluación de reglas simples por debajo de 10 ms. Son estimaciones de ingeniería para evaluar plausibilidad, no cotas universales ni sustitutos de la medición. La literatura relevada respalda la sensibilidad de estos tramos al transporte, al modelo y al método de seguimiento (Axis Communications AB, s. f.; Bachhuber et al., 2018; Cheng et al., 2024; Wang et al., 2025; Bewley et al., 2016; Zhang et al., 2022).

La latencia de alerta incorpora además la ventana de evidencia definida para cada patrón. Por ello, un tiempo computacional bajo no garantiza una alerta temprana si la confirmación exige mayor persistencia. Las referencias de la Tabla 30 ordenan la lectura temporal por severidad y mantienen TTFD por debajo del objetivo de confirmación para que mida respuesta perceptiva inicial. El objetivo de t_alert-system de cada severidad debe ser compatible con la ventana de persistencia fijada para sus patrones en la sección 17.1.5.2 y dejar margen para el procesamiento y la variabilidad de la cadena. Los valores orientativos deben recalibrarse antes de utilizarse como criterio de aceptación cuando cambien el modelo, la resolución de entrada, la cadencia o las condiciones de transporte.

**Tabla 30**

*Referencias temporales orientativas por severidad*

| **Severidad** | **Máximo orientativo de t_alert-system** | **Objetivo orientativo de TTFD** | **Referencia mínima de SDR** | **Lectura operativa** |
| --- | --- | --- | --- | --- |
| Crítica | 3 a 5 s | < 1 s | ≥ 0,50 | Se prioriza no omitir episodios y se admite menor estabilidad inicial. |
| Alta | 5 a 10 s | < 3 s | ≥ 0,60 | Se busca equilibrio entre rapidez, persistencia y control de falsas alertas. |
| Media | 10 a 20 s | < 10 s | ≥ 0,70 | Puede exigirse mayor evidencia antes de confirmar, con mayor tolerancia temporal. |

***Nota****.* Los valores ordenan prioridades y criterios de lectura. No constituyen límites normativos ni universales del dominio. Deben calibrarse con la cadencia efectiva, las ventanas del patrón y el material de evaluación, sin modificar después de observar resultados la definición de los episodios o las reglas de asociación.

##### 17.1.7.6. Instrumentación, aplicabilidad y reporte

Toda corrida debe registrar el contexto necesario para reproducirla con los campos mínimos consolidados en la Tabla D.3 del Anexo D. En una comparación de ajuste se agregan la semilla, la partición, la composición del corpus y el procedimiento de entrenamiento.

Las corridas temporales deben conservar los hitos que permiten reconstruir la cadena evaluada. Esto incluye la referencia del episodio, la primera evidencia positiva válida, el inicio del patrón candidato cuando corresponda, la unidad que confirma el patrón, el registro de la alerta y, si aplica, la confirmación del canal externo. Cada marca temporal se acompaña del dominio de reloj y del identificador necesario para correlacionarla. La falta de uno de estos hitos limita el tramo que puede reportarse.

Las mediciones de rendimiento incluyen un período de calentamiento identificado y una ventana estable de observación. Se informan promedio, P50, P95 y P99 cuando existen observaciones individuales suficientes, junto con el número de muestras y la duración de la corrida. Cuando sólo se conserva un agregado, se reporta ese estadístico y se declara la imposibilidad de reconstruir percentiles. No se generan distribuciones sintéticas ni se presentan estimaciones como mediciones.

La aplicabilidad se determina antes de interpretar el valor. Las métricas MOT no corresponden sin referencia de identidad persistente. t_alert-system no corresponde en pruebas que terminan en detecciones por imagen. TTFD y SDR no corresponden sin continuidad temporal e inicio anotado. t_alert-notification no corresponde sin un trayecto externo instrumentado. Los deltas de ajuste no son interpretables sin una línea base equivalente o cuando existe filtración entre entrenamiento y evaluación. En cada caso se informa el estado y su causa. Los insumos mínimos que habilitan cada familia de métricas se consolidan en la Tabla D.2 del Anexo D.

El reporte se organiza por condición, fuente o estrato y escenario. Toda cifra incluye el denominador efectivo. Los clips negativos se presentan mediante el conteo de falsos positivos, la duración negativa observada y, sólo después, la tasa horaria derivada. Las re-alertas del mismo episodio se mantienen separadas. SDR se compara únicamente bajo una cadencia equivalente. Las latencias de alerta se contrastan sobre conjuntos comunes de episodios evaluables o se declara la diferencia de cobertura que impide la comparación.

Este framework vincula la calidad perceptiva con el comportamiento temporal y la viabilidad de la plataforma sin confundir niveles de evidencia. La sección 17.1.8 utiliza estas reglas para formular criterios de aceptación y riesgos experimentales. Las secciones de implementación y resultados documentan, respectivamente, qué tramos y métricas se instrumentaron, cuáles se calcularon y qué limitaciones condicionaron su interpretación.

#### 17.1.8. Protocolo experimental integrado

La secuencia experimental busca evitar que decisiones tardías alteren la validez comparativa del estudio. Ninguna fase que modifique el estado del modelo o del conjunto de datos se ejecuta antes de congelar el software relevante, los checkpoints retenidos, el banco de evaluación y la estructura mínima de bitácora. Sobre esa base el protocolo se ordena en las fases sucesivas de la Tabla 33 y no como un conjunto abierto de ensayos.

El conjunto de métricas aplicables a cada corrida se fija antes de ejecutarla con las reglas de aplicabilidad de la sección 17.1.7.6. Las métricas temporales y las de seguimiento sólo se exigen cuando la evidencia disponible las habilita.

**Tabla 33**

*Fases del protocolo experimental integrado*

| **Fase** | **Objetivo** | **Salida esperada** | **Criterio de cierre** |
| --- | --- | --- | --- |
| Preparación | Congelar entorno, versiones, checkpoints, datasets retenidos y estructura mínima de bitácora. | Artefactos y configuración de corrida documentados. | Reproducibilidad básica garantizada. |
| Baseline DBE | Medir cada modelo candidato en zero-shot sobre el banco de evaluación congelado. | Línea base por condición, prompt y métrica obligatoria. | Predicciones exportadas y métricas obligatorias calculadas. |
| Sensibilidad de prompts | Comparar familias de prompts y congelar la formulación primaria por condición. | Matriz comparativa y selección justificada. | Prompt principal y variantes de contraste definidos. |
| Pipeline y seguimiento | Medir t_G2A, FPS, recursos y aporte del tracker. | Diagnóstico del comportamiento integrado. | Logs temporales y métricas de estabilidad disponibles. |
| Fine-tuning condicionado | Ejecutar adaptación al dominio sólo si se cumplen las condiciones metodológicas fijadas. | Variante comparativa exportada al CPN. | Comparación válida respecto de baseline y banco de evaluación compartido. |
| EBE complementario | Ejecutar captura continua en entorno controlado o simulado. | Evidencia de plausibilidad operativa y latencia integrada. | Eventos, timestamps y alertas registradas. |
| Reporte | Integrar métricas aplicadas, métricas no aplicables y causas de exclusión. | Informe de resultados trazable y replicable. | Se explicitan alcance, límites y condiciones de interpretación. |

*Nota.* La secuencia expresa dependencias entre fases y no un calendario. El orden y las fechas efectivas de ejecución se documentan en la implementación.

#### 17.1.9. Estrategia de adaptación al dominio

La adaptación al dominio se mantiene como una rama comparativa condicionada y no como un requisito para demostrar la viabilidad del enfoque. Adoptarla de antemano convertiría una hipótesis todavía no probada en un supuesto metodológico. La rama sólo se habilita cuando existe soporte de datos suficiente y la comparación puede sostenerse sin romper la integridad del protocolo. Sus condiciones de habilitación son de datos y de protocolo y no de disponibilidad de cómputo. El TN aporta el entrenamiento y el CPN conserva la referencia operativa.

La comparación se concentra como máximo en dos candidatos, Grounding DINO y YOLOE, que representan compromisos distintos entre expresividad semántica y eficiencia de inferencia (Liu et al., 2024; Wang et al., 2025). Cuál de ellos se ajusta depende de la factibilidad real de integración, exportación y ejecución sobre el CPN y no sólo de su rendimiento en benchmarks generales.

La rama se ejecuta como una jornada experimental completa con criterios prerregistrados, una única línea base, márgenes fijados antes de evaluar y un veredicto determinado por reglas de aceptación declaradas de antemano. La Tabla 34 consolida esa regla de decisión.

**Tabla 34**

*Regla metodológica de decisión para la adaptación al dominio*

| **Regla** | **Decisión adoptada** | **Sentido metodológico** |
| --- | --- | --- |
| Existencia de baseline | Ningún ajuste se evalúa sin baseline zero-shot previa sobre el mismo banco de evaluación. | Sin baseline explícita no existe comparación defendible. |
| Disponibilidad de datos | Se priorizan CR-01 y CR-02. CR-03 y CR-04 quedan fuera del camino ordinario mientras no exista cobertura suficiente. | Concentra el ajuste donde puede producir evidencia útil y comparaciones válidas. |
| Integridad comparativa | El banco de evaluación debe ser compartido y permanecer congelado. | Evita leakage y falsas mejoras por cambio de evaluación. |
| Ganancia exigible | La variante ajustada debe superar el margen fijado antes de evaluar y no mostrar sólo una ventaja marginal. | Protege al protocolo de ciclos costosos de ajuste con retorno metodológico débil. |
| Costo operativo | La variante ajustada no debe comprometer materialmente la latencia ni el presupuesto de recursos del CPN. | Una mejora semántica que destruye la viabilidad operativa no fortalece al prototipo. |

*Nota.* La regla no prescribe que el ajuste deba ejecutarse. Define cuándo vale la pena hacerlo sin distorsionar el objetivo principal del prototipo.

#### 17.1.10. Supuestos, riesgos de validez y consideraciones ético-legales

El marco ético-legal del protocolo se apoya en la minimización de datos y en el uso asistivo del sistema. Cuando el proyecto genera material propio para el EBE rigen salvaguardas de finalidad determinada, acceso restringido, retención acotada y ausencia de reconocimiento de identidad personal o tratamiento biométrico, en línea con los principios de la sección 16.6 y con el régimen argentino de protección de datos personales y videovigilancia (Argentina, 2000, 2015).

La interpretación de los resultados descansa en cinco supuestos. El prototipo es un sistema asistivo y una alerta no equivale a una sanción ni a una determinación automática de incumplimiento normativo. La evaluabilidad de varias condiciones depende de variables que el detector no controla del todo, como la escala aparente, el ángulo de cámara, la oclusión o la iluminación. CR-06 presupone una parametrización espacial externa al prompt y no se evalúa como si el lenguaje por sí solo definiera la zona restringida. El EBE valida en entorno controlado o simulado y no en obra real.

El quinto supuesto es que la disyunción entre datos de entrenamiento y banco de evaluación sólo es verificable sobre el ajuste propio del trabajo. Los modelos preentrenados de vocabulario abierto provienen de corpus de terceros no inspeccionables, de modo que no puede descartarse que imágenes del banco hayan participado de ese preentrenamiento. Es una condición estructural de toda evaluación de modelos preentrenados y no una particularidad de este protocolo. Por eso las cifras zero-shot se leen como una comparación entre combinaciones bajo condiciones idénticas y no como afirmaciones sobre generalización a material inédito. La Tabla 35 reúne los riesgos metodológicos y operativos que condicionan las instancias siguientes y la mitigación adoptada para cada uno.

**Tabla 35**

*Riesgos metodológicos y operativos relevantes para las instancias siguientes*

| **Riesgo** | **Imp. probable** | **Mitigación adoptada** |
| --- | --- | --- |
| La configuración retenida excede el presupuesto de VRAM o rompe la latencia esperada del CPN. | Alto | Priorizar variantes ejecutables en la laptop, ajustar resolución y composición del vocabulario activo y justificar toda optimización sobre el CPN. |
| Persisten brechas de datos para condiciones de Niveles 2 y 3. | Alto | Mantener esas condiciones como extensiones condicionadas y producir datos complementarios sólo si no desplazan el núcleo del prototipo experimental. |
| El tracker agrega complejidad sin reducir falsas alarmas. | Medio | Medir primero ΔFPtracking y sólo exigir métricas MOT completas en subsets donde el costo de anotación esté justificado. |
| El diseño experimental se vuelve inmanejable por exceso de variables combinadas. | Alto | Sostener el diseño reducido de la sección 17.1.3.3, con la prueba de mayor exigencia sólo sobre la configuración retenida. |
| La generación de material propio introduce dudas de privacidad o de consentimiento. | Medio | Aplicar las salvaguardas de la sección 17.1.10, con registro explícito de finalidad y condiciones de captura. |

#### 17.1.11. Conclusiones parciales de la consolidación metodológica

La consolidación metodológica cierra con un protocolo experimental integrado y ajustado al alcance real del prototipo. El núcleo obligatorio queda en las condiciones de detección directa de Nivel 1, la comparación controlada en DBE se separa de la plausibilidad operativa en EBE, la estrategia de datos evita la filtración entre entrenamiento y evaluación, el framework de métricas se centra en el valor operativo de la alerta y una regla explícita decide cuándo habilitar o descartar la adaptación al dominio.

Las instancias siguientes toman estas definiciones como referencia. El análisis y diseño arquitectónico las traduce en una organización técnica y la validación experimental produce resultados sobre las condiciones, los escenarios y las métricas fijadas, con la instrumentación de t_G2A y t_alert-system definida en la sección 17.1.7. En todos los casos debe declararse qué elementos del catálogo se implementaron, cuáles no aplicaron y cuáles permanecieron condicionados. Esa trazabilidad entre definición metodológica, diseño, implementación y validación es el principal resultado de esta parte del proyecto y sostiene su orientación central, que es evaluar si la detección open-vocabulary puede integrarse como herramienta asistiva para el monitoreo de condiciones de riesgo en construcción civil.

### Anexo C — Prompts, datos, datasets, benchmarks y logística

**Tabla C.1**

*Catálogo de prompts candidatos por condición de riesgo*

| **Código** | **Eje de variación** | **Prompt candidato (inglés)** | **Estrategia** |
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

***Nota****.* En las estrategias indirecta y descompuesta el separador punto y coma indica consultas independientes al modelo y su materialización depende de la sintaxis de cada detector. Para CR-05 y CR-06 no se formulan prompts integrados sino prompts de entidades componentes, y la condición completa se evalúa en el módulo de razonamiento contextual.

**Tabla C.2**

*Variables de sensibilidad candidatas para el Environment-Based Evaluation*

| **Variable** | **Niveles o condiciones retenidas** | **Uso dentro del protocolo** |
| --- | --- | --- |
| Iluminación | Controlada; mixta; natural cuando el entorno lo permita. | Define condición base y barridos univariados de sensibilidad. |
| Resolución de fuente | 1280 × 720 como base; 1920 × 1080 como variante de sensibilidad si la configuración lo permite. | Estima el costo-beneficio entre visibilidad, carga computacional y estabilidad del pipeline. |
| Distancia cámara-sujeto | Rangos a cerrar en instancia de análisis y diseño arquitectónico según campo visual y tamaño aparente; guía inicial: 5-10 m y 10-20 m. | Permite observar el efecto de escala de objeto sin fijar una geometría de cámara antes del diseño del EBE. |
| Oclusión | Baja y media; la oclusión severa no se adopta como obligación de aceptación. | Tensiona la robustez sin convertir la campaña en irreproducible. |
| Tracker | Deshabilitado y habilitado cuando aplique. | Permite medir el aporte del tracking a estabilidad, persistencia y reducción de falsas alarmas. |
| Matriz de prompts | Conjunto acotado de variantes por condición. | Permite seleccionar y congelar el prompt primario antes de las corridas comparativas finales. |
| Composición del vocabulario activo | Configuraciones pequeñas y medianas, explícitamente documentadas. | Permite medir si la cantidad y tipo de consultas activas impacta precisión, latencia o ambas. |

***Nota****.* Los niveles consignados son candidatos de diseño y se cierran al definir la topología y el espacio físico de prueba, siguiendo la secuencia progresiva de la sección 17.1.3.3.

**Tabla C.3**

*Logística de conversión y acceso de los datasets retenidos*

| **Dataset** | **Formato nativo** | **Formato de trabajo** | **Vía de acceso** | **Observación** |
| --- | --- | --- | --- | --- |
| SHEL5K | Pascal VOC | COCO/ODVG y/o YOLO | Mendeley Data | Conversión directa VOC→YOLO; para el pipeline de Grounding DINO, VOC→COCO→ODVG. |
| CHV | Formato nativo a inspeccionar | COCO/ODVG y/o YOLO | Repositorio del autor | Revisar estructura del paquete y términos de uso al descargar; cita obligatoria. |
| construction_site_safety | YOLO (Roboflow) | COCO/ODVG y/o YOLO | Roboflow | Requiere conversión YOLO→COCO→ODVG para el pipeline de Grounding DINO. |
| ppe_siabar | YOLO (Roboflow) | COCO/ODVG y/o YOLO | Roboflow | Requiere conversión YOLO→COCO→ODVG para el pipeline de Grounding DINO. |

*Nota.* La secuencia de gestión se describe en la sección 17.1.6.5 y los volúmenes y versiones por fuente en la Tabla 23. El esfuerzo de conversión es directo cuando basta un paso y en dos pasos cuando exige inspección o normalización previa.

### Anexo D — Métricas, instrumentación y bitácora experimental

**Tabla D.1**

*Métricas de rendimiento del pipeline y uso de recursos*

| **Métrica** | **Definición operativa** | **Formato de reporte** | **Compromiso** | **Criterio de estabilidad** |
| --- | --- | --- | --- | --- |
| FPS efectivos | Cuadros completamente procesados por segundo al final del pipeline. | Media, P50, P95, P99 y variación | Obligatorio | Período de calentamiento previo y corrida sostenida |
| Latencia G2A | Intervalo entre el dequeue de la unidad visual y la disponibilidad del resultado de inferencia. La captura y el transporte hasta el dequeue se informan aparte como capture_to_host. | ms (P50, P95, P99) | Obligatorio | Hitos y dominio de reloj declarados |
| Jitter | Variabilidad de la latencia entre cuadros consecutivos. | ms (desv. est. / coef. variación) | Deseable | Reportar junto con G2A |
| Uso de VRAM | Memoria de video ocupada por modelo, tensores y buffers. | MB y % | Obligatorio | Sin crecimiento monótono |
| Utilización GPU | Porcentaje de ocupación de la GPU durante la corrida. | % | Deseable | Registrar media y picos |
| Uso de RAM/CPU | Consumo de memoria del sistema y presión sobre CPU del proceso completo. | MB/GB y %CPU | Deseable | Registrar serie temporal |

*Nota.* G2A = Glass-to-Algorithm. FPS = Frames Per Second. VRAM = Video Random Access Memory. El reporte obligatorio mínimo incluye FPS efectivos, latencia G2A y uso de VRAM. Cuando sea posible, conviene registrar además GPU, RAM y CPU con muestreo periódico durante una corrida sostenida.

**Tabla D.2**

*Insumos mínimos requeridos antes de iniciar una campaña de medición*

| **Familia de métricas** | **Ground truth o insumo** | **Instrumentación mínima** | **Herramientas o artefactos** | **Salida mínima** |
| --- | --- | --- | --- | --- |
| Detección (AP, P/R) | Bounding boxes y etiquetas por imagen o cuadro. | Export de predicciones por corrida. | pycocotools o conversión COCO equivalente. | AP y P/R por variante, con punto operativo o criterio de reporte explícitamente declarado. |
| Tracking (HOTA, DetA / AssA, IDF1, MOTA, IDSW / Frag) | Boxes y track_id persistente por cuadro. | Export MOT-compatible sobre subset anotado. | TrackEval u otra implementación equivalente. | Métricas MOT sobre subset, con declaración explícita de qué métricas fueron ejecutadas y cuáles no. |
| Pipeline (FPS, latencia G2A, jitter) | No requiere GT semántico. | Timestamps por etapa del pipeline. | Logs internos y scripts de agregación. | P50/P95/P99, promedio y variación. |
| Alerta y patrón (t_alert-system; t_alert-notification si aplica; TTFD; SDR) | Inicio anotado de la condición de riesgo, duración o intervalo temporal del evento, severidad asignada y criterio de activación del patrón. | Logs con timestamps de primera evidencia positiva, inicio de patrón candidato si corresponde, patrón confirmado, alerta registrada y disponibilidad, consulta o notificación si aplica. | Motor de patrones instrumentado, registro interno de alertas, event log del pipeline, bitácora de corrida y scripts de agregación temporal. | TTFD, SDR y t_alert-system por episodio. t_alert-notification sólo si existe trayecto instrumentado. Toda métrica sin insumos se declara no aplicable. |
| Recursos (VRAM, GPU, RAM, CPU) | No requiere GT semántico. | Muestreo periódico durante la corrida. | nvidia-smi, psutil u otras herramientas del sistema. | Series temporales y resumen. |
| Fine-tuning | Split train/eval disjunto y baseline zero-shot explícita. | Registro de entrenamiento y evaluación. | Logs de entrenamiento y scripts comparativos. | Deltas y costo de entrenamiento, cuando aplique. |

***Nota****.* La ausencia de cualquiera de los insumos requeridos para una familia de métricas debe declararse antes de planificar la campaña experimental. En particular, no corresponde reemplazar ground truth inexistente por estimaciones informales ni interpretar logs incompletos como evidencia suficiente de desempeño. Toda métrica sin insumos mínimos deberá registrarse como no ejecutada o no aplicable, según corresponda.

**Tabla D.3**

*Campos mínimos recomendados para la bitácora experimental*

| **Campo** | **Contenido mínimo recomendado** | **Uso en la interpretación** |
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
