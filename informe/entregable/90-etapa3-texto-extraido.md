# 90 — Texto extraído del documento de trabajo: §17.3 Diseño Arquitectónico (v1.4)

> **Extracción derivada (2026-08-23)** del `.docx`
> `informe/entregable/E-OVRT-VDP_Seccion_17.3_Diseno_Arquitectonico_v1.4.docx`, **solo para búsqueda y cita**
> (mismo estatuto que el doc 90): al editar, se edita el `.docx`/Google Docs, nunca
> este archivo. Tablas y figuras pueden haber perdido formato; las figuras no se
> extraen y las ecuaciones no se convierten — quedan `⟦FIGURA: no extraída — ver el .docx⟧` y
> `⟦ECUACIÓN: no extraída — ver el .docx⟧` donde estaban. Regenerado con
> `herramientas/extraer_informe.py` (regla D-C del manual de aplicación).

---

#### 17.3.1. Introducción y propósito del capítulo

El presente capítulo desarrolla el diseño arquitectónico de la plataforma experimental E-OVRT-VDP, tomando como punto de partida el alcance metodológico, las condiciones de riesgo, los escenarios de evaluación y las métricas definidas en las secciones anteriores. Su propósito es transformar esas definiciones en una organización técnica capaz de orientar la implementación de la plataforma experimental, manteniendo coherencia con los criterios de modularidad, trazabilidad, medición y control de alcance ya establecidos.

La arquitectura se estructura alrededor de una separación entre el procesamiento visual en tiempo real y la lógica de interpretación posterior. Para ello, se distinguen dos planos principales: el plano de medios, encargado de la ingesta, normalización, inferencia y publicación de resultados perceptivos; y el plano de control, responsable de evaluar patrones de riesgo, registrar alertas asistivas, conservar eventos y producir evidencia reconstruible. Esta división permite proteger la ruta crítica de vídeo y, al mismo tiempo, sostener la trazabilidad experimental necesaria para analizar cada corrida.

El capítulo describe las responsabilidades de los componentes principales, los flujos de información, las fronteras entre módulos, los contratos versionados, las interfaces de gobierno y transporte, los escenarios experimentales DBE y EBE, y los criterios de observabilidad que deberán acompañar la implementación. Su finalidad es consolidar una base arquitectónica que permita materializar el prototipo experimental de manera incremental, medible y trazable dentro del alcance experimental definido.

La pregunta que orienta el capítulo puede sintetizarse del siguiente modo: ¿qué arquitectura permite materializar una plataforma experimental de detección open-vocabulary en video en tiempo real, manteniendo modularidad, desacoplamiento, trazabilidad y evaluabilidad dentro del alcance metodológico ya definido?

#### 17.3.2. Insumos metodológicos y decisiones derivadas

La arquitectura propuesta se deriva de las definiciones metodológicas ya consolidadas: el alcance experimental del prototipo, el catálogo de condiciones de riesgo, los escenarios de evaluación, los roles funcionales del entorno, el marco de métricas y los lineamientos ético-legales actúan como restricciones de diseño. Lo que sigue no reitera el protocolo experimental: explicita qué consecuencia arquitectónica se deriva de cada uno de esos insumos, de modo que ningún módulo, frontera o flujo del sistema aparezca como una decisión aislada.

La arquitectura propuesta se deriva de las definiciones metodológicas consolidadas en las secciones anteriores. El alcance experimental, las condiciones de riesgo seleccionadas, los escenarios de evaluación, los roles funcionales del entorno, el framework de métricas y los lineamientos ético-legales actúan como restricciones de diseño. En consecuencia, los módulos, las fronteras y los flujos del sistema no se establecen como decisiones aisladas, sino como una traducción técnica de las condiciones necesarias para sostener la evaluabilidad, la trazabilidad y el control de alcance del prototipo.

El marco teórico de detección open-vocabulary, seguimiento temporal y procesamiento continuo de vídeo exige integrar percepción visión-lenguaje, tratamiento de fuentes audiovisuales y persistencia temporal cuando la condición evaluada lo requiera. De esta exigencia se deriva una arquitectura modular, con separación entre el plano de medios y el plano de control, una ruta crítica instrumentable y modelos sustituibles mediante adaptadores. La inferencia queda así desacoplada de la interpretación temporal, de modo que la incorporación o sustitución de un modelo no obligue a redefinir el resto de la cadena.

El núcleo validable se concentra en CR-01 y CR-02. Ambas condiciones se evalúan mediante evidencia positiva de persona y elementos de protección personal, seguida de una inferencia espacial de ausencia y de su estabilización temporal. Por esta razón, el flujo base prioriza la estrategia indirecta y comprende detección de entidades, asociación espacial por sujeto, evaluación de regiones relevantes y confirmación temporal del patrón. Las zonas externas, las relaciones contextuales complejas y las métricas formales de seguimiento multiobjeto se conservan como capacidades extensibles, pero no se convierten en dependencias del núcleo.

La coexistencia de los escenarios DBE y EBE introduce requisitos temporales diferentes. Las fuentes basadas en archivos pueden regular su ritmo de lectura, repetirse y detenerse sin alterar el contenido observado; las fuentes en vivo, en cambio, continúan evolucionando aunque el procesamiento no alcance la cadencia de captura. La arquitectura abstrae ambos tipos de fuente mediante contratos comunes, pero distingue para cada uno las políticas de reproducibilidad, actualidad, omisión, descarte y trazabilidad temporal. Esta separación permite compartir el pipeline sin ocultar las diferencias que afectan la interpretación experimental de cada corrida.

De los roles funcionales ya establecidos se deriva una restricción de diseño y no una nueva definición: se adoptan como responsabilidades de referencia que permiten declarar dónde se captura, dónde se ejecuta la inferencia y dónde se prepara una variante ajustada, sin que la distribución física de componentes pase a formar parte de la semántica de los contratos.

Finalmente, el framework de métricas y los lineamientos ético-legales condicionan la observabilidad y la persistencia desde el diseño. Cada corrida debe registrar su configuración efectiva, marcas de tiempo por tramo, métricas técnicas, eventos reconstruibles, descartes y errores, de manera que una alerta pueda vincularse con la evidencia que la produjo. Al mismo tiempo, el carácter asistivo del prototipo, la exclusión del reconocimiento de identidad personal y el criterio de minimización visual orientan la trazabilidad ordinaria hacia eventos, metadatos y referencias controladas. La conservación de clips, capturas o recortes queda limitada a los casos justificados por validación, auditoría técnica o comunicación académica.

#### 17.3.3. Alcance, requisitos y decisiones arquitectónicas iniciales

El diseño arquitectónico se formula para un prototipo experimental ejecutado en un entorno local y controlado. En consecuencia, la arquitectura debe orientar la implementación, la medición y la reconstrucción de resultados sin asumir responsabilidades propias de una solución productiva. La sección delimita el alcance efectivo del núcleo validable, las extensiones previstas, las capacidades requeridas, las cualidades no funcionales relevantes y las decisiones iniciales que deberán conservarse durante el desarrollo del prototipo experimental.

##### 17.3.3.1. Alcance del núcleo y extensiones

El alcance arquitectónico se organiza alrededor del núcleo validable definido en la consolidación metodológica. Sobre ese núcleo, la plataforma debe demostrar un flujo completo, medible y trazable desde una fuente visual hasta una alerta asistiva registrada. El objetivo no es ampliar prematuramente la cantidad de condiciones cubiertas, sino asegurar una base suficientemente sólida para procesar evidencia visual, publicar eventos, evaluar patrones, registrar alertas y reconstruir resultados experimentales.

El núcleo incluye las capacidades necesarias para operar sobre fuentes controladas, ejecutar inferencia open-vocabulary, versionar prompts, normalizar detecciones, aplicar reglas temporales simples, registrar eventos y producir métricas comparables. Las capacidades de mayor complejidad —seguimiento multiobjeto formal, reglas espaciales, zonas parametrizadas, preselección liviana en borde o adaptación al dominio— quedan previstas como extensiones condicionadas, siempre que no desplacen la validación inicial ni agreguen dependencias innecesarias al flujo base.

La inclusión de la gestión de prompts dentro del núcleo responde a la naturaleza open-vocabulary de la plataforma: cada resultado debe poder asociarse con una formulación, una estrategia de detección y un vocabulario activo registrados. Del mismo modo, la separación entre DBE y EBE permite distinguir la evaluación reproducible de la validación con captura continua, evitando mezclar variabilidad de cámara, iluminación, códec o red con el desempeño propio del detector.

En relación con la evidencia visual, el diseño retoma los criterios ya definidos de minimización, uso asistivo y ausencia de reconocimiento de identidad. La trazabilidad ordinaria se apoya en eventos, metadatos, identificadores, métricas y referencias controladas. Los clips, snapshots o recortes anotados sólo se consideran artefactos complementarios cuando resulten necesarios para validación, revisión técnica o defensa académica.

##### 17.3.3.2. Capacidades arquitectónicas requeridas

A partir del alcance definido, la arquitectura debe habilitar un conjunto mínimo de capacidades que permitan desarrollar un prototipo experimental medible, trazable y extensible. Estas capacidades no describen todavía componentes de implementación, sino responsabilidades que el diseño debe contemplar para que el sistema pueda procesar fuentes visuales, ejecutar inferencia open-vocabulary, evaluar patrones, registrar alertas y producir evidencia experimental.

La clasificación distingue capacidades del núcleo, capacidades asociadas a la evaluación controlada, capacidades complementarias previstas, extensiones condicionadas y ramas comparativas. Esta separación permite ordenar el desarrollo sin convertir funcionalidades deseables en dependencias obligatorias del flujo base.

**Tabla 39**

*Capacidades arquitectónicas y su tratamiento en el diseño*

| **Capacidad requerida** | **Compromiso** | **Lectura de diseño** |
| --- | --- | --- |
| Gestión de corrida reproducible | Núcleo | Cada ejecución debe asociarse a una configuración explícita de fuente, modelo, prompts, umbrales, entorno y versiones. |
| Procesamiento DBE | Núcleo de evaluación | Debe operar sobre imágenes, datasets o videos locales para estabilizar inferencia, contratos, eventos y métricas bajo condiciones reproducibles. |
| Procesamiento EBE | Complementario previsto | Debe admitir captura o streaming en entorno controlado para observar el comportamiento operativo del sistema. |
| Normalización de entrada visual | Núcleo | Cada frame debe representarse con metadatos de corrida, fuente, orden temporal, resolución y política de muestreo. |
| Inferencia OVD configurable | Núcleo | La arquitectura debe permitir integrar modelos de detección open-vocabulary sin acoplar el sistema a una única alternativa. |
| Gestión de prompts y vocabulario activo | Núcleo | Debe versionar formulaciones, aliases, estrategias de detección, vocabulario activo y umbrales asociados. |
| Normalización de detecciones | Núcleo | Las salidas heterogéneas de los modelos deben transformarse en detecciones comparables, trazables y aptas para evaluación posterior. |
| Evaluación de patrones de Nivel 1 | Núcleo | Las detecciones positivas deben asociarse espacialmente por sujeto, transformarse en un estado de ausencia evaluable y estabilizarse mediante persistencia temporal e histéresis. |
| Registro de alertas asistivas | Núcleo | Las alertas deben registrarse cuando un patrón alcanza estado confirmado, sin constituir un juicio normativo automático. |
| Publicación y persistencia de eventos | Núcleo | La arquitectura debe desacoplar la producción de evidencia perceptiva y conservar un historial reconstruible de eventos relevantes. |
| Observabilidad y métricas | Núcleo | Debe medir FPS, latencias por tramo, uso de recursos, estados de patrón, alertas, descartes y errores. |
| Reporte experimental | Núcleo | Debe sintetizar configuración, resultados, métricas, alertas, errores y limitaciones por corrida. |
| Inspección mínima de resultados | Núcleo | Debe permitir revisar corridas, alertas, métricas y evidencia asociada sin convertirse en un tablero operativo avanzado. |
| Gestión de evidencia visual controlada | Complementario previsto | Debe admitir clips, snapshots o recortes justificados para validación, revisión técnica o comunicación académica. |
| Video crudo continuo | Fuera del comportamiento ordinario | La trazabilidad principal se apoya en eventos, metadatos, métricas y referencias controladas. |
| Condiciones de riesgo de Nivel 2 y Nivel 3 | Extensión condicionada | Requieren capacidades adicionales de contexto, razonamiento espacial, zonas, proximidad o relaciones entre entidades. |
| Capacidades contextuales y relacionales | Extensión condicionada | Zonas y evaluadores relacionales quedan previstos sin bloquear CR-01 y CR-02; su habilitación requiere evidencia e instrumentación adecuadas. |
| Identidad temporal de sujeto y métricas MOT | Capacidad opcional; métricas fuera del núcleo | La arquitectura admite granularidad por sujeto mediante una identidad temporal válida. Las métricas MOT no condicionan la evaluación del núcleo ni deben confundirse con la capacidad de mantener identidad. |
| Adaptación al dominio (fine-tuning) | Rama comparativa condicionada | Sólo corresponde bajo una línea base preentrenada congelada, datos suficientes, partición disjunta y criterios de escalamiento definidos con anterioridad a los resultados. |

**Nota**. El compromiso “núcleo” identifica capacidades necesarias para el flujo base; “núcleo de evaluación” refiere a capacidades que sostienen la evaluación controlada; “complementario previsto” agrupa capacidades útiles para validación, revisión o comunicación académica; “extensión condicionada” identifica capacidades previstas pero no obligatorias; y “rama comparativa condicionada” refiere a variantes que sólo deben incorporarse si se cumplen las condiciones metodológicas correspondientes.

##### 17.3.3.3. Requisitos no funcionales de referencia

Las cualidades no funcionales condicionan directamente la validez experimental del prototipo. No alcanza con detectar una condición de riesgo si el sistema no registra la configuración de la corrida, no mide latencia, no conserva trazabilidad suficiente o no controla la evidencia visual generada. Por esta razón, la reproducibilidad, la observabilidad, la privacidad, la modularidad, la integridad de eventos y el control de complejidad se consideran condiciones arquitectónicas del diseño.

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

**Nota**. Los requisitos no funcionales expresan cualidades necesarias para preservar la validez experimental del prototipo. Su finalidad es asegurar comparabilidad entre corridas, trazabilidad de resultados y control de decisiones que puedan afectar la latencia, privacidad, reproducibilidad u observabilidad.

##### 17.3.3.4. Decisiones arquitectónicas iniciales

Además de delimitar alcance, capacidades y cualidades no funcionales, el diseño debe explicitar un conjunto de decisiones arquitectónicas iniciales. Estas decisiones no fijan tecnologías concretas, pero establecen reglas estructurales que deberán preservarse durante el desarrollo del prototipo experimental para mantener coherencia con el alcance metodológico, la trazabilidad y la medición de resultados.

**Tabla 41**

*Decisiones arquitectónicas iniciales*

| **ID** | **Decisión** | **Justificación** |
| --- | --- | --- |
| DA-01 | Separar plano de medios y plano de control. | Protege la ruta crítica de vídeo y desacopla la inferencia de la lógica de interpretación. |
| DA-02 | Publicar evidencia perceptiva como eventos de percepción normalizados. | Permite desacoplar detecciones, patrones, métricas, alertas y persistencia. |
| DA-03 | Separar el gobierno de las corridas, el transporte de eventos durante la ejecución y el repositorio persistente de hechos. | Cada preocupación tiene un régimen propio: el gobierno es puntual y de solicitud–respuesta, el transporte es continuo y no debe bloquear la ruta crítica, y la persistencia debe sobrevivir a la corrida para habilitar su relectura. Mantenerlas separadas permite sustituir el mecanismo de transporte sin alterar el gobierno ni la evidencia, y reevaluar cualquier corrida sin depender de la mensajería. |
| DA-04 | Confirmar patrones mediante persistencia temporal e histéresis. | Reduce alertas generadas por detecciones aisladas, inestables o de corta duración. |
| DA-05 | Integrar modelos OVD mediante adaptadores. | Permite comparar modelos o variantes sin rediseñar la arquitectura general. |
| DA-06 | Admitir granularidad por sujeto mediante identidad temporal opcional, sin convertir las métricas MOT en requisito del núcleo. | Permite evaluar persistencia por persona cuando existe identidad válida y conserva la granularidad de escena como configuración independiente. |
| DA-07 | Tratar la adaptación al dominio como rama comparativa separada y condicionada por datos y protocolo. | Preserva una línea base zero-shot congelada y evita mezclar resultados de una variante ajustada con el núcleo sin entrenamiento. |
| DA-08 | Adoptar minimización visual como criterio ordinario de trazabilidad. | Evita que el almacenamiento indiscriminado de video crudo sea parte del comportamiento base. |
| DA-09 | Separar trazabilidad ordinaria de evidencia visual controlada. | Permite conservar clips, capturas o recortes sólo cuando estén justificados por validación, revisión técnica o comunicación académica. |
| DA-10 | Priorizar DBE antes de EBE. | Estabiliza contratos, inferencia, eventos y métricas antes de incorporar captura continua. |
| DA-11 | Permitir preselección liviana en el rol de captura como variante opcional, conservadora y deshabilitada por defecto, que conserva la unidad en el flujo principal ante falla o incertidumbre del preselector. | La variante puede reducir carga sin transformar el borde en fuente de verdad ni ocultar descartes, porque el flujo base continúa disponible y comparable. |
| DA-12 | Versionar prompts y vocabulario activo por corrida. | Garantiza la reproducibilidad y comparación entre formulaciones. |
| DA-13 | Registrar toda alerta interna antes de aplicar políticas de supresión o entrega externa. | Preserva la semántica y la medición del episodio; el cooldown, la limitación de tasa y la idempotencia pertenecen al tramo de distribución. |

**Nota.** Las decisiones fijan reglas estructurales adoptadas para el diseño del prototipo experimental. Su materialización y verificación se documentan en la sección 17.4.

Las decisiones DA-08 y DA-09 deben leerse de manera conjunta. La plataforma no utiliza el almacenamiento continuo de video crudo como mecanismo ordinario de trazabilidad; la reconstrucción experimental se apoya principalmente en eventos, metadatos, identificadores, métricas y referencias controladas. Sin embargo, la validación con captura continua, la revisión técnica o la defensa académica pueden requerir evidencia visual demostrativa. Por ello, se admite la generación de clips breves, snapshots o recortes anotados, siempre que estén justificados y cuenten con criterios explícitos de acceso, retención y anonimización.

La DA-13 complementa esta separación: para el núcleo del prototipo experimental, la alerta válida es el evento interno registrado por la plataforma. Cualquier notificación externa debe tratarse como una salida derivada, no bloqueante y medible por separado.

A estas decisiones se agregan tres precisiones de lectura arquitectónica: DBE y EBE se tratan como escenarios experimentales y no como topologías físicas; la diferencia entre fuentes reproducibles y fuentes en vivo condiciona los criterios de control de ritmo y trazabilidad temporal; y la distribución física de componentes no forma parte del compromiso conceptual de esta etapa.

#### 17.3.4. Principios arquitectónicos adoptados

Las decisiones enumeradas en la Tabla 41 se articulan alrededor de cuatro principios que orientarán la lectura del diseño en las secciones siguientes.

El primero es la **separación entre ruta crítica y lógica de control**: la inferencia y la publicación de evidencia perceptiva (DA-01, DA-02) deben mantenerse desacopladas de la evaluación de patrones, la persistencia, los reportes y las notificaciones externas, de modo que ninguna tarea posterior pueda bloquear el procesamiento visual.

El segundo es la **modularidad por contratos**: fuentes, modelos, prompts, detecciones, patrones y métricas deben intercambiarse mediante estructuras explícitas (DA-05, DA-12), evitando dependencias internas que dificulten la sustitución o la evaluación comparativa.

El tercero es la trazabilidad experimental: toda alerta debe poder reconstruirse a partir de la configuración de corrida, los eventos de percepción, el patrón evaluado y las métricas registradas (DA-03, DA-04, DA-13).

El cuarto es la **medición desde el diseño**: tiempos, FPS, descartes, errores y estados de patrón deben instrumentarse desde las primeras corridas, dado que forman parte de la validez experimental del prototipo.

A estos principios se suma el criterio transversal de **evolución incremental**: las capacidades condicionadas (DA-06, DA-07, DA-11) deben incorporarse sin desplazar el núcleo de Nivel 1 ni convertirse en dependencias del flujo base.

#### 17.3.5. Vista general de la arquitectura propuesta

La plataforma E-OVRT-VDP se organiza como una arquitectura lógica por bloques, orientada a procesar fuentes de video, generar evidencia perceptiva, evaluar patrones de riesgo y conservar resultados reconstruibles. Esta vista no representa una distribución obligatoria en procesos, servicios o nodos físicos independientes, sino una separación de responsabilidades que permite mantener el sistema modular, medible y trazable.

La arquitectura distingue un flujo principal y un conjunto de capacidades de soporte. La configuración experimental actúa de forma transversal sobre ese flujo: define las condiciones de cada corrida —escenario, modelo, prompts activos, umbrales, políticas de evidencia y parámetros de ejecución— para asegurar reproducibilidad sin intervenir directamente en el procesamiento frame a frame.

El flujo principal parte de fuentes visuales externas, como datasets, vídeos locales, cámaras o flujos de streaming. El plano de medios comienza en el adaptador de ingesta visual, que encapsula los distintos orígenes bajo una representación común. Desde ese punto se concentra la ruta crítica: lectura o captura, decodificación cuando corresponde, control de ritmo, normalización, inferencia open-vocabulary, postproceso y publicación de evidencia perceptiva normalizada. El plano no depende de tareas posteriores para continuar procesando unidades visuales.

A partir de los eventos publicados, el plano de control interpreta la evidencia producida por el plano de medios: evalúa patrones, administra estados de corrida y registra alertas asistivas internas cuando se confirma una condición de riesgo. Las alertas confirmadas se publican por un bus dedicado hacia el módulo de distribución, que aplica la política de notificación y registra los resultados de entrega sin bloquear al motor de patrones. El ciclo de vida de ambos planos y del módulo de distribución se gobierna mediante interfaces HTTP independientes; la interfaz de inspección y el orquestador experimental gobiernan el ciclo de vida mediante las interfaces de gobierno de cada módulo y no consumen directamente los buses.

Finalmente, la trazabilidad, la observabilidad y la inspección se agrupan en el bloque de soporte experimental, que no constituye una etapa lineal del flujo frame a frame sino una capacidad transversal. Este bloque conserva evidencia reconstruible, consolida telemetría técnica y permite revisar corridas, métricas, alertas y resultados experimentales sin interferir con la ruta crítica del plano de medios.

**Figura 4.1**

*Vista conceptual de la arquitectura E-OVRT-VDP*

⟦FIGURA: no extraída — ver el .docx⟧

*Nota.* La figura presenta una vista lógica de alto nivel. Las flechas sólidas representan el flujo principal de datos y eventos; las flechas punteadas representan influencia de configuración o capacidades de soporte. La figura no debe interpretarse como una distribución física obligatoria ni como una asignación definitiva a tecnologías específicas.

La materialización de esta vista distingue dos patrones de acople complementarios. El gobierno de las corridas se realiza mediante interfaces HTTP gobernadas por configuración en los tres módulos ejecutables. Se adopta HTTP porque el ciclo de vida de una corrida —crear, consultar, cancelar y cerrar— tiene semántica de solicitud y respuesta, admite múltiples clientes sin acoplarlos entre sí y permite disponer los módulos en un mismo host o en hosts distintos sin modificar su lógica; el gobierno por configuración garantiza que cada corrida declare sus parámetros en lugar de heredarlos de constantes ocultas. El intercambio de datos en ejecución se realiza mediante un bus ZeroMQ con patrón publicador-suscriptor y serialización binaria msgpack: un canal de detecciones entre los planos y un canal de alertas hacia la distribución. Se adopta ZeroMQ porque ofrece transporte de baja latencia sin requerir un broker como dependencia adicional del prototipo, y el patrón publicador-suscriptor desacopla al productor de sus consumidores sin bloquear la ruta crítica; msgpack reduce el costo de serialización respecto del texto plano conservando estructuras autodescriptivas. La durabilidad no se le exige al canal: cada hecho se persiste en archivos JSONL de sólo adición antes de publicarse, de modo que la evidencia pueda releerse y reevaluarse sin depender de la mensajería. La persistencia JSONL cumple esa función de durabilidad y relectura —inspeccionable, de sólo adición y sin introducir una base de datos como dependencia del núcleo— y no constituye un tercer patrón de acople. HTTP gobierna configuración y ciclo de vida; el bus transporta hechos de ejecución.

En conjunto, esta organización permite que el procesamiento de video, la interpretación de patrones, la distribución de alertas y el análisis experimental se mantengan separados y coordinados mediante contratos explícitos, favoreciendo la reproducibilidad y la evaluación controlada del prototipo.

#### 17.3.6. Configuración experimental y diseño de prompts

La configuración experimental concentra las decisiones que gobiernan una corrida de evaluación de la plataforma experimental. Su función es declarar, de manera explícita y reproducible, el escenario, la fuente visual, el modelo OVD, los prompts activos, los umbrales, la política de muestreo, los módulos habilitados, los criterios de patrón, la política de evidencia y la instrumentación de métricas.

Esta sección materializa, en términos arquitectónicos, definiciones establecidas en la consolidación metodológica. Las condiciones de riesgo, los escenarios, las métricas y los criterios de prompting pasan a expresarse como parámetros ejecutables que condicionan al plano de medios y al plano de control. De este modo, cada detección, transición de patrón, alerta interna, métrica o evidencia conservada puede asociarse con una configuración efectiva de corrida.

Dentro de esa configuración, los prompts se tratan como parte del vocabulario activo del experimento. En un sistema open-vocabulary, la consulta textual incide sobre la evidencia perceptiva generada; por lo tanto, debe registrarse, versionarse y mantenerse trazable hasta los resultados que contribuye a producir.

##### 17.3.6.1. Función arquitectónica de la configuración experimental

La configuración experimental actúa como punto de gobierno de la corrida. Antes de iniciar la ejecución, define qué se evaluará, con qué fuente, con qué modelo, con qué vocabulario activo y bajo qué criterios de interpretación. Esta función separa la definición de condiciones de ejecución del procesamiento efectivo de frames y eventos.

La separación protege la ruta crítica del plano de medios. Una vez iniciada la corrida, el pipeline debe disponer de la configuración efectiva sin depender de consultas externas bloqueantes para decidir qué modelo ejecutar, qué prompts utilizar o qué política de muestreo aplicar. La configuración gobierna la ejecución, pero no debe introducir latencia durante el procesamiento continuo.

También delimita la interpretación posterior de resultados. Una detección sólo es experimentalmente útil si puede relacionarse con su fuente, modelo, prompt, umbral, postproceso y patrón evaluado. Sin esa asociación, no sería posible atribuir diferencias de desempeño a una variable concreta de la corrida.

Esa función de gobierno sólo se sostiene si la configuración se resuelve y se valida antes de iniciar la ejecución: una corrida cuya declaración esté incompleta debe fallar al crearse y no producir artefactos que luego resulten inatribuibles. La función se proyecta además sobre los tres destinatarios de la configuración: el plano de medios recibe los parámetros que aplica sin diseñarlos ni versionarlos, el plano de control recibe los criterios con los que evalúa, y el soporte experimental la utiliza como clave de reconstrucción, de modo que todo evento, métrica, alerta o evidencia conservada pueda rastrearse hasta la corrida que le dio origen.

##### 17.3.6.2. Configuración de corrida como artefacto de reproducibilidad

La configuración de corrida se materializa como un manifiesto de experimento que referencia y congela las configuraciones efectivas de cada componente. Esta separación responde a que el plano de medios, el plano de control y el tramo de distribución poseen ciclos de vida y destinatarios distintos; una configuración monolítica no tendría un único consumidor ni permitiría reconstruir con precisión qué versión recibió cada servicio.

En este trabajo, se denomina ejecución experimental a la unidad lógica que agrupa las ejecuciones independientes de los componentes que participan en una misma instancia del experimento. Esta unidad se identifica mediante un experiment_id, mientras que cada componente conserva su propio identificador de corrida. La separación entre ambos niveles permite correlacionar configuraciones, eventos, métricas, alertas, entregas y artefactos bajo una clave común, sin imponer un ciclo de vida único ni una configuración monolítica a los servicios participantes.

El manifiesto declara un experiment_id, las referencias a las configuraciones de cada plano, el orden de disparo y los artefactos congelados —modelo, conjunto de prompts, conjunto de patrones y política de distribución—. Dos corridas sólo son comparables cuando se conoce qué variable cambió y cuáles permanecieron constantes. La Tabla 42 resume los elementos mínimos de este gobierno reproducible.

**Tabla 42**

*Elementos mínimos de la configuración experimental*

| **Elemento configurable** | **Contenido esperado** | **Función arquitectónica** |
| --- | --- | --- |
| Manifiesto de experimento | Versión del manifiesto, fecha, objetivo y referencias a las configuraciones efectivas del plano de medios, del plano de control y del módulo de distribución cuando se habilita. | Gobierna una ejecución experimental sin imponer una configuración monolítica a servicios con ciclos de vida independientes. |
| Identificador de experimento | experiment_id, junto con los identificadores de corrida de cada componente. | Vincula eventos, métricas, errores, alertas, entregas y artefactos de todos los componentes bajo una clave común. |
| Escenario y fuente visual | DBE o EBE; dataset, vídeo local, imagen, cámara o stream; naturaleza temporal; resolución, ritmo esperado, duración y restricciones conocidas. | Distingue fuentes reproducibles, fuentes temporales y fuentes en vivo sin confundir escenario con topología física. |
| Parámetros del pipeline | Resolución de procesamiento, selección o muestreo, criterios de omisión o descarte, tamaño de cola, ritmo esperado y calentamiento. | Condiciona latencia, cobertura temporal, unidades procesadas y lectura de descartes. |
| Modelo OVD | Modelo, versión, checkpoint, backend, precisión numérica, dispositivo y adaptador. | Permite sustituir o comparar modelos sin acoplar el resto de la arquitectura. |
| Prompts y vocabulario activo | Conjunto versionado, condición asociada, rol de cada clase, estrategia de formulación y umbral vinculado. | Garantiza trazabilidad entre consulta textual, evidencia producida y configuración. |
| Umbrales y postproceso | Confianza mínima, IoU/NMS, filtros por clase, tamaño, región y normalización de coordenadas. | Define qué salidas crudas se transforman en evidencia perceptiva normalizada. |
| Patrones activos | Condición, severidad, granularidad scene\|subject, ventana de confirmación, histéresis de resolución y criterio de evidencia. | Transforma evidencia puntual en estados y alertas internas por episodio. El cooldown no integra este contrato. |
| Capacidades habilitadas y evidencia | Identidad de sujeto, zonas, preselección en borde, inspección, distribución y política de evidencia visual. | Evita capacidades implícitas y preserva la comparabilidad entre corridas. |
| Política de distribución | Canal, calidad de servicio, idempotencia, supresión de re-notificación, limitación de tasa y retención del ledger. | Ubica cooldown y controles de comunicación aguas abajo de la alerta interna. |
| Instrumentación y entorno | Timestamps por tramo, métricas esperadas, estado de aplicabilidad, causa, entorno, librerías y runtime. | Permite calcular o rechazar métricas de forma explícita y reconstruir condiciones de ejecución. |

Nota. La tabla presenta los elementos mínimos del manifiesto y de las configuraciones referenciadas. Los contratos concretos se desarrollan en §17.3.11.

##### 17.3.6.3. Diseño de prompts y vocabulario activo

El diseño de prompts materializa la forma en que las condiciones de riesgo se expresan como consultas consumibles por un modelo OVD. En la metodología previa se trató la sensibilidad de estos modelos a la formulación de la consulta y se reconoció que el prompt no es un detalle accesorio, sino una variable de ingeniería que puede alterar detecciones, falsos positivos, falsos negativos y estabilidad temporal (Du et al., 2022; Zhou et al., 2022).

Para el prototipo, los prompts primarios se formulan en inglés. Esta decisión se apoya en la centralidad de ese idioma en los corpus y modelos visión-lenguaje utilizados como base, como CLIP, Conceptual Captions y CC12M, entrenados o construidos principalmente a partir de pares imagen-texto y recursos web en inglés (Changpinyo et al., 2021; Radford et al., 2021; Sharma et al., 2018). En consecuencia, el documento puede describir las condiciones en español, pero la capa de consulta del detector se diseña en inglés para favorecer la alineación con los patrones lingüísticos dominantes del preentrenamiento.

Cada prompt debe asociarse a una condición de riesgo, un texto de consulta, una estrategia de formulación, una versión y un conjunto de prompts activos. Una modificación de redacción debe registrarse como variante experimental, no como reemplazo informal. Esto permite explicar qué formulación produjo una detección y comparar resultados sin perder vínculo con la condición original.

El vocabulario activo representa el conjunto de prompts habilitados en una corrida. Su tamaño y composición afectan el comportamiento semántico del detector y, según el modelo, el costo de inferencia. Por ello, el núcleo validable debe trabajar con un vocabulario reducido y controlado: suficiente para evaluar sensibilidad de formulación, pero sin habilitar listas amplias que dificulten atribuir resultados.

También debe distinguirse entre prompt y estrategia de detección. Un prompt es una consulta semántica; una estrategia puede combinar prompts, postproceso, evidencia indirecta o reglas espaciales. Esta sección define el diseño y versionado de prompts. La integración entre condición, estrategia de detección, patrón y alerta se desarrolla posteriormente.

##### 17.3.6.4. Diseño inicial de prompts para el catálogo de condiciones

El diseño inicial distingue el vocabulario positivo del núcleo, los conjuntos correspondientes a ramas comparativas y el vocabulario condicionado de las condiciones de mayor complejidad. Para CR-01 y CR-02, el núcleo utiliza person, helmet y vest: la primera categoría identifica la entidad sujeto y las restantes representan los elementos de protección cuya presencia se evalúa espacialmente respecto de cada persona.

La ausencia de casco o chaleco no se formula como consulta principal del núcleo. Se infiere en el plano de control cuando existe evidencia suficiente de una persona y no se encuentra evidencia del EPP correspondiente dentro de la región configurada. Las consultas negativas o de estado observable se mantienen en conjuntos separados para las estrategias directa e híbrida ya distinguidas en la consolidación metodológica, de modo que sus resultados sean atribuibles a una estrategia explícita y no a una mezcla informal de vocabularios. En el diseño arquitectónico y en lo que sigue del trabajo, estas familias se identifican mediante un código: estrategia directa (E-DIR), cuando el prompt intenta describir la condición de riesgo completa; estrategia indirecta (E-IND), cuando el detector identifica entidades visibles por separado y la condición se reconstruye mediante lógica externa al modelo; y estrategia híbrida (E-HYB), cuando se combinan consultas de ambos tipos bajo una regla de composición explícita.

CR-03 y CR-04 conservan consultas compuestas y descompuestas de carácter condicionado, porque su confirmación requiere contexto espacial adicional. CR-05 y CR-06 se expresan mediante entidades componentes, ya que la condición completa depende de proximidad, seguimiento o zonas declaradas externamente. La Tabla 43 organiza estos vocabularios y su uso previsto.

**Tabla 43**

*Vocabulario inicial de prompts en inglés por condición de riesgo*

| **Condición y estrategia** | **Rol de la consulta** | **Consulta o categoría candidata** | **Uso previsto** |
| --- | --- | --- | --- |
| CR-01 y CR-02 — núcleo E-IND | Entidad sujeto | person | Localizar las personas sobre las cuales se evalúa la presencia o ausencia espacial del EPP. |
| CR-01 — núcleo E-IND | Evidencia positiva de EPP | helmet | Detectar casco asociable a una persona. La ausencia se infiere en el plano de control. |
| CR-02 — núcleo E-IND | Evidencia positiva de EPP | vest | Detectar chaleco asociable a una persona. La ausencia se infiere en el plano de control. |
| CR-01 — rama E-DIR | Ausencia o estado observable | bare_head; “person without hard hat”; “construction worker without safety helmet”; “person with bare head on construction site” | Comparar formulaciones directas bajo una configuración independiente del núcleo. |
| CR-02 — rama E-DIR | Ausencia o descripción visual | “person without reflective vest”; “worker without high-visibility vest”; “person without bright colored safety clothing” | Comparar formulaciones directas o atributivas bajo una configuración independiente del núcleo. |
| CR-03 — condicionada | Consulta compuesta | “person on scaffolding without harness”; “worker at height without fall protection equipment” | Explorar evidencia parcial; la confirmación requiere contexto espacial y observabilidad suficiente. |
| CR-03 — condicionada | Consulta descompuesta | “person on scaffolding”; “person on elevated platform”; “safety harness”; “fall arrest harness” | Detectar por separado persona en altura y elementos de protección para evaluación posterior. |
| CR-04 — condicionada | Consulta compuesta | “unprotected edge with person nearby”; “elevated platform without guardrail near workers” | Explorar evidencia parcial; la confirmación requiere proximidad y validación espacial. |
| CR-04 — condicionada | Consulta descompuesta | “platform edge”; “open edge”; “guardrail”; “safety railing”; “person near edge” | Detectar borde, protección colectiva y persona próxima como entidades independientes. |
| CR-05 — condicionada | Entidades de maquinaria | “excavator”; “backhoe loader”; “dump truck”; “crane”; “heavy machinery” | Producir evidencia para evaluar proximidad y persistencia con personas. |
| CR-05 — condicionada | Entidades humanas | person; “construction worker”; “pedestrian” | Producir evidencia humana para la evaluación relacional. |
| CR-06 — condicionada | Entidad persona | person; “worker”; “pedestrian” | Comparar la posición del sujeto con una zona declarada externamente. |
| CR-06 — condicionada | Elementos auxiliares | “restricted area sign”; “caution tape”; “warning tape”; “barrier”; “safety cone” | Aportar referencias visuales sin reemplazar la definición externa de la zona. |

Nota. El vocabulario del núcleo validable está compuesto por person, helmet y vest. Las formulaciones directas pertenecen a ramas comparativas independientes. Cada corrida conserva prompt_set_id, de modo que toda detección pueda atribuirse al conjunto que la produjo.

##### 17.3.6.5. Reglas de comparabilidad entre configuraciones

La configuración debe permitir comparar variantes sin producir conclusiones ambiguas. Al comparar prompts, deben mantenerse constantes modelo, fuente visual, resolución, política de muestreo, umbrales, postproceso y criterios de patrón. Así, una variación de desempeño puede atribuirse razonablemente a la formulación evaluada.

Al comparar modelos OVD, debe conservarse el mismo conjunto de prompts y condiciones equivalentes de fuente, resolución y postproceso. Si un modelo requiere umbrales distintos por la escala de sus puntajes, esa diferencia debe declararse como parte de la configuración y no ocultarse como detalle de implementación.

Al comparar DBE y EBE, debe declararse que cambia la naturaleza temporal de la fuente. En EBE intervienen captura continua, variabilidad de iluminación, codificación o decodificación cuando corresponda, continuidad temporal, omisiones, descartes y disponibilidad efectiva de frames. Por lo tanto, las diferencias observadas no deben atribuirse automáticamente al detector OVD.

Por la misma razón, ningún módulo opcional —evidencia visual, identidad temporal, zonas, preselección en el rol de captura o distribución externa— puede operar como comportamiento implícito: su habilitación se declara en la configuración de la corrida, porque una activación silenciosa alteraría la interpretación de latencia, cobertura temporal, privacidad y aplicabilidad de métricas, es decir, la base misma de la comparación.

#### 17.3.7. Diseño conceptual del plano de medios

El plano de medios se materializa en el componente lógico Pipeline de Medios de la plataforma experimental. Este componente concentra la ruta sensible a latencia: inicia cuando el adaptador de ingesta visual recibe, lee o decodifica una unidad visual proveniente de una fuente externa, y finaliza cuando se publica evidencia perceptiva normalizada hacia la frontera de integración. Su alcance incluye ingesta, decodificación cuando corresponda, control de ritmo, normalización visual, inferencia open-vocabulary, postproceso y publicación no bloqueante.

El límite del componente es estricto. El Pipeline de Medios no confirma condiciones de riesgo, no asigna severidad, no ejecuta reglas de patrón, no genera alertas y no depende de persistencia pesada para continuar procesando frames. Su salida representa evidencia perceptiva primaria asociada a una corrida, una fuente, una referencia temporal, un modelo y una configuración de procesamiento. La interpretación de esa evidencia corresponde al plano de control.

La separación protege la ruta frame-evento frente a tareas que pueden introducir bloqueo o variabilidad, como la evaluación de patrones, la reconstrucción histórica, la generación de reportes, la inspección visual o la distribución de notificaciones externas. La sección precisa cómo debe comportarse el componente que transforma entrada visual en evidencia perceptiva utilizable por el resto del sistema.

Las fuentes utilizadas en DBE y EBE ingresan al Pipeline de Medios mediante una misma frontera conceptual: el adaptador de ingesta visual. La diferencia entre ambos escenarios se resuelve en la forma de lectura, disponibilidad del frame, metadatos temporales y control de ritmo, no en la salida del plano. En DBE predomina la lectura reproducible; en EBE puede aparecer irregularidad temporal, atraso acumulado, variabilidad de captura o disponibilidad de frames recientes. En ambos casos, la salida debe conservar trazabilidad suficiente para reconstruir qué se procesó, bajo qué configuración y con qué resultado.

La configuración experimental actúa como entrada transversal del Pipeline de Medios, pero no es una responsabilidad interna de este plano. Fuente, resolución, política conceptual de selección o muestreo, modelo, prompts activos, umbrales y modo de inferencia son definidos por la configuración de corrida. El plano de medios debe consumir esa configuración, aplicarla durante la ejecución y propagar sus identificadores en la evidencia publicada, sin convertirse en el módulo encargado de gobernarla o versionarla.

**Figura 4.2**

*Flujo conceptual del Pipeline de Medios*

⟦FIGURA: no extraída — ver el .docx⟧

Nota. La figura representa el flujo interno del plano de medios. Las fuentes visuales son externas al plano; el plano comienza en el adaptador de ingesta visual, responsable de recibir, leer o decodificar la fuente y transformarla en una unidad visual procesable. La configuración de corrida parametriza la ejecución como entrada transversal, sin formar parte del procesamiento frame a frame. El evento de percepción normalizado se ubica por fuera del recuadro para señalar la frontera de salida hacia el bus interno de eventos y el plano de control.

##### 17.3.7.1. Flujo operativo del Pipeline de Medios

El flujo interno del Pipeline de Medios se organiza como una cadena de transformación progresiva. Cada etapa recibe una representación visual o perceptiva, aplica una operación acotada y entrega una salida que mantiene relación con la corrida y con la referencia temporal original. Esta organización permite sustituir fuentes, modelos o políticas de procesamiento sin modificar la responsabilidad general del plano.

**Ingesta y decodificación. La primera responsabilidad interna del plano de medios es recibir la entrada visual desde fuentes externas, como datasets, imágenes, videos locales, cámaras o streams. La fuente queda encapsulada por un adaptador de ingesta visual que oculta diferencias de formato sin eliminar información relevante para la evaluación. Cuando la entrada proviene de vídeo codificado o streaming, la decodificación convierte el flujo en frames procesables y registra la información necesaria para distinguir disponibilidad, recepción, orden lógico y referencia temporal. En DBE suele alcanzar con conservar índice de secuencia y orden de lectura; en EBE puede ser necesario registrar además timestamps de captura o recepción, irregularidad temporal y eventuales descartes por atraso.**

**Control de ritmo y selección de unidades visuales. Antes de ingresar a inferencia, el pipeline debe decidir qué unidades visuales serán efectivamente procesadas. Esta decisión puede consistir en aceptar todos los frames, aplicar una selección determinista, reducir la frecuencia de procesamiento o priorizar unidades recientes cuando existe captura continua. Lo importante para el diseño no es imponer una política concreta, sino evitar decisiones invisibles: toda unidad omitida, reemplazada o descartada debe quedar asociada a una causa y a una política declarada en la corrida. Los detalles concretos de colas, buffers o algoritmos de descarte corresponden a la implementación.**

**Normalización visual. El frame aceptado se adapta a los requisitos del modelo seleccionado. Esta etapa puede modificar resolución, formato, espacio de color, disposición de tensores o escala de entrada. El diseño debe preservar la relación entre coordenadas originales y coordenadas de inferencia, porque esa relación permite interpretar cajas delimitadoras, revisar evidencia visual y comparar resultados entre configuraciones con distinta resolución. Reescalado, recortes o relleno de bordes no deben tratarse como operaciones invisibles.**

**Inferencia open-vocabulary.** La inferencia ejecuta el detector configurado sobre la entrada normalizada y el conjunto de prompts activos. El modelo se integra mediante un adaptador para evitar que el resto del plano dependa de una salida particular de Grounding DINO, YOLOE u otro candidato. Esta etapa produce resultados crudos: cajas, puntajes, etiquetas, frases asociadas o estructuras equivalentes, según el formato propio del detector utilizado. Cuando el modelo lo permita, el adaptador puede reutilizar representaciones textuales precalculadas o mecanismos equivalentes para reducir el costo de inferencia, siempre que esa optimización no altere la trazabilidad de la corrida.

**Postproceso y normalización de detecciones. Luego de la inferencia, el Pipeline de Medios aplica los filtros definidos por la configuración de corrida —umbrales, supresión de detecciones redundantes, normalización de etiquetas y remapeo de coordenadas— para convertir las salidas del modelo en evidencia perceptiva común. Esta salida queda asociada al frame, prompt, condición y nivel de confianza correspondiente, pero no interpreta riesgo ni genera alertas; sólo entrega evidencia normalizada al plano de control.**

**Publicación de evidencia perceptiva.** La publicación cierra el plano de medios. La evidencia normalizada se entrega como evento liviano hacia la frontera de integración, asociado a corrida, fuente, referencia temporal, modelo, prompts y timestamps relevantes. A partir de ese punto, la evidencia puede ser evaluada por el plano de control, persistida de manera reconstruible o inspeccionada por componentes de soporte; ninguna de esas tareas debe ser requisito para que el Pipeline de Medios continúe procesando la siguiente unidad visual.

En consecuencia, la salida del plano de medios no se reduce a cajas y puntajes sin contexto, pero tampoco incorpora severidad, confirmación de patrón ni decisión de alerta. Su producto es evidencia visual primaria, normalizada y trazable: la interpretación de esa evidencia corresponde al plano de control, y la comparación entre configuraciones, modelos y prompts, al análisis experimental posterior.

##### 17.3.7.2. Criterios de diseño aplicados al plano de medios

Los criterios de diseño del plano de medios no agregan nuevas decisiones generales respecto de la arquitectura ya definida; traducen esas decisiones al comportamiento específico de la ruta frame-evento. El objetivo es que el procesamiento visual sea medible, sustituible y defendible sin mezclarlo con lógica de patrones, persistencia pesada o salidas externas.

El primer criterio es **mantener una ruta no bloqueante**. La inferencia y la publicación de evidencia no deben esperar indefinidamente a consumidores posteriores. Si el bus interno, la persistencia, la inspección o una salida externa fallan o se saturan, esa condición debe registrarse como parte de la ejecución, pero no debe convertir a esos consumidores en dependencia directa del procesamiento visual.

El segundo criterio es hacer visible la variabilidad temporal. En video, una latencia aparentemente baja puede ocultar pérdida de frames, colas saturadas o reemplazo de frames antiguos por frames recientes. Por eso, el Pipeline de Medios debe registrar timestamps por tramo, profundidad de cola cuando corresponda, frames aceptados, frames omitidos y descartes. La pérdida de evidencia no puede quedar fuera de la interpretación experimental.

El tercer criterio es **encapsular la heterogeneidad de modelos**. Los detectores OVD pueden diferir en formato de entrada, tipo de prompt, estructura de salida, semántica de puntajes y costo de inferencia. El plano de medios debe absorber esa heterogeneidad mediante adaptadores y entregar una evidencia perceptiva estable. De ese modo, el plano de control no queda acoplado a un modelo específico ni a detalles internos de su implementación.

El cuarto criterio es **conservar la trazabilidad mínima del resultado perceptivo**. Cada evidencia publicada debe poder asociarse con la corrida, la fuente, la referencia temporal, el modelo utilizado, los prompts activos y la política de procesamiento aplicada. Esta trazabilidad no implica almacenar video crudo de manera continua ni resolver la reconstrucción histórica dentro del plano de medios; implica producir eventos suficientes para que el soporte experimental pueda reconstruir la corrida posteriormente.

El quinto criterio es **no trasladar responsabilidades del plano de control hacia el plano de medios**. La persistencia temporal de un patrón, la histéresis, la severidad y el registro interno de alerta pertenecen al motor de patrones. El plano de medios puede mejorar la calidad de la evidencia perceptiva, pero no debe decidir si una condición observada se convirtió en una situación de riesgo confirmada.

##### 17.3.7.3. Control de ritmo según tipo de fuente

La política de control de ritmo se define por corrida y afecta qué evidencia visual llega a inferencia. En el diseño del plano de medios, esta política no se trata como una optimización secundaria, sino como parte de la configuración que condiciona la lectura de resultados. Cambiar la selección de unidades visuales, la frecuencia de procesamiento o el criterio de omisión equivale a cambiar la variante experimental evaluada.

En corridas DBE, o en general con fuentes cuya lectura puede regularse —conjuntos de imágenes, videos locales o archivos—, el lector puede regularse sin pérdida temporal de evidencia. Por ello, la prioridad arquitectónica es preservar reproducibilidad, orden lógico y trazabilidad de las unidades visuales procesadas. Si no se procesan todos los frames, la selección debe ser determinista, declarada en la configuración y mantenida constante entre corridas comparables.

En corridas EBE, o en general con fuentes en vivo como cámaras, streams o capturas continuas, la escena evoluciona aunque la inferencia se retrase. Por ello, el diseño debe priorizar que el atraso acumulado no crezca indefinidamente y que toda omisión, irregularidad temporal o descarte quede registrado. La estrategia concreta de selección de unidades visuales se declara en la configuración efectiva de cada corrida; su efecto sobre latencia, cobertura temporal y evidencia disponible debe ser observable desde el diseño.

El resultado esperado de esta política no es maximizar FPS de forma aislada, sino hacer interpretable el comportamiento del pipeline. Un sistema que procesa menos frames puede ser válido para una corrida exploratoria o comparativa, pero esa reducción debe ser visible para no confundir rendimiento con cobertura temporal.

##### 17.3.7.4. Capacidades opcionales sin desplazar el núcleo validable

El núcleo validable del plano de medios debe poder operar sin exigir seguimiento multiobjeto formal, preselección en borde ni adaptación de modelos al dominio. Estas capacidades pueden incorporarse como variantes del flujo, pero no deben convertirse en requisitos para demostrar el procesamiento básico de CR-01 y CR-02, y su incorporación no modifica el contrato de salida del plano de medios. La preselección en borde se adopta además bajo un criterio de degradación segura, denominado fail-open: ante una falla o una decisión incierta del preselector, la unidad visual se conserva para el flujo principal. De ese modo la variante puede descartar carga, pero nunca convertirse en causa de pérdida de evidencia.

El tracking o MOT puede ubicarse después del postproceso cuando resulte necesario estabilizar entidades, reducir oscilaciones entre frames o entregar identificadores temporales al plano de control. Aun así, un identificador temporal no equivale a una condición de riesgo sostenida.

Las variantes de ejecución orientadas a eficiencia deben tratarse con el mismo criterio: pueden ser útiles durante la implementación, pero no deben ocupar el centro del diseño conceptual del plano de medios. Reducciones de resolución, cambios de modo de inferencia o exportaciones a motores optimizados corresponden a decisiones de implementación y evaluación posterior; en esta sección sólo interesa fijar que cualquier variante que altere la ruta frame-evento debe quedar declarada en la configuración de corrida.

#### 17.3.8. Diseño conceptual del plano de control

El plano de control concentra la interpretación de la evidencia perceptiva producida por el plano de medios. Su responsabilidad comienza cuando ingresa un evento de percepción normalizado y termina cuando el sistema registra estados de patrón, alertas internas, eventos persistibles, métricas y salidas de inspección o distribución desacopladas. A diferencia del Pipeline de Medios, no procesa frames crudos ni necesita operar al ritmo constante de captura; trabaja sobre eventos y sobre cambios de estado derivados de reglas configuradas.

La separación entre detección, patrón y alerta es la decisión arquitectónica central de esta sección. Una detección puntual expresa una observación del modelo sobre una unidad visual; un patrón confirmado expresa que esa evidencia fue evaluada durante una ventana temporal bajo criterios explícitos de persistencia, umbral e histéresis; una alerta interna registra un episodio asistivo generado por una transición válida del patrón. Por lo tanto, el plano de control no debe transformar cada detección en una alerta, sino estabilizar la evidencia antes de producir salidas operativas.

Esta organización evita que la variabilidad propia de la inferencia OVD —falsos positivos, falsos negativos, fluctuación de puntajes, sensibilidad al prompt u oclusiones parciales— se traslade directamente al sistema de alertas. También permite mantener al plano de medios aislado de consumidores lentos, persistencia histórica, reportes, notificaciones externas o interfaces de inspección. El plano de control puede ejecutar esas funciones de forma asíncrona sin bloquear la producción de evidencia perceptiva.

En el alcance del prototipo experimental, el plano de control se orienta principalmente al núcleo validable. Para CR-01 y CR-02, la evaluación puede resolverse mediante persistencia temporal simple y estados de patrón sin exigir seguimiento multiobjeto formal. El tracking, las zonas espaciales o las reglas relacionales pueden enriquecer escenarios posteriores, pero no deben convertirse en una dependencia del núcleo validable.

**Figura 4.3**

*Flujo conceptual del plano de control*

⟦FIGURA: no extraída — ver el .docx⟧

**Nota.** La figura representa el flujo conceptual del plano de control. La configuración de corrida parametriza la evaluación como entrada transversal, sin formar parte del procesamiento evento a evento. El evento de percepción normalizado ingresa desde el plano de medios como entrada externa; dentro del plano se evalúan patrones, se actualizan estados y se derivan registros persistibles y métricas. La alerta interna por episodio se muestra por fuera del recuadro para indicar la frontera de salida del plano de control, quedando disponible para consumidores o adaptadores posteriores.

##### 17.3.8.1. Flujo lógico y responsabilidades del plano de control

El plano de control recibe evidencia perceptiva normalizada, selecciona los patrones activos, evalúa la evidencia espacial y temporal, administra el estado de cada patrón y registra una alerta interna cuando se confirma un episodio. En paralelo, persiste transiciones, métricas y errores necesarios para reconstruir la decisión.

El bus interno cumple una función de integración y no de razonamiento. La arquitectura conserva el transporte como mecanismo sustituible, pero fija para el prototipo una publicación ZeroMQ con patrón publicador-suscriptor, serialización msgpack y un envoltorio versionado. El plano de control consume ese contrato por el canal de detecciones del bus; no interpreta formatos propios de un detector ni recibe frames crudos.

El gobierno de la corrida no viaja por el bus. El plano de control se configura y se inicia mediante su interfaz HTTP, mientras que el bus transporta los hechos de ejecución. Esta separación entre gobierno y datos permite disponer los componentes en un mismo host o en hosts distintos sin modificar su semántica.

La evaluación transforma evidencia puntual en estados operativamente interpretables. No ejecuta inferencia visual, no asigna identidad personal y no determina cumplimiento normativo: aplica reglas declaradas de asociación espacial, persistencia, granularidad e histéresis.

Cuando un patrón alcanza el estado confirmado se registra la alerta interna: es el hecho principal del sistema y precede a cualquier notificación. La persistencia y el soporte experimental se mantienen fuera de la ruta crítica del plano de medios.

##### 17.3.8.2. Evaluación de patrones y máquina de estados

La máquina de estados distingue inactive, candidate, confirmed, sustained y resolved. Una evidencia inicial abre el estado candidato; la confirmación sólo ocurre cuando la condición satisface la ventana temporal y los umbrales declarados; la continuidad mantiene el episodio; y la ausencia sostenida durante la histéresis lo resuelve.

La transición a confirmed registra una alerta interna por episodio. El estado sostenido actualiza duración y evidencia sin convertir cada frame positivo en una alerta nueva. Una nueva confirmación posterior se conserva como re-alerta y se evalúa por separado de los falsos positivos.

Las ventanas se expresan en milisegundos y no en frames, de modo que la semántica temporal no cambie con la cadencia de procesamiento. Los componentes de una definición de patrón, incluidos los criterios espaciales de CR-01 y CR-02, se presentan al describir el motor de evaluación (sección 17.3.8.3.1); los valores adoptados para el núcleo se documentan en la sección 17.4.6.

La confirmación representa el cumplimiento de una regla interna bajo la configuración de la corrida; no constituye certificación normativa ni decisión automática de intervención.

**Figura 4.4**

*Máquina de estados del motor de patrones*

⟦FIGURA: no extraída — ver el .docx⟧

Nota. La figura representa el ciclo de vida temporal de un patrón de riesgo en el plano de control. Una condición observada inicia el estado candidate; si la evidencia satisface la ventana de confirmación configurada, el patrón pasa a confirmed y se registra la alerta interna correspondiente. Mientras la condición permanece activa, el patrón evoluciona a sustained. Cuando la evidencia deja de sostenerse y se cumple la ventana de resolución, el episodio pasa a resolved y posteriormente retorna a inactive. Si la evidencia inicial resulta insuficiente o no persiste durante la ventana de confirmación, el patrón vuelve a inactive sin generar una alerta.

##### 17.3.8.3. Motor de evaluación de patrones de riesgo

El motor de evaluación de patrones de riesgo es el componente lógico del plano de control encargado de transformar evidencia perceptiva normalizada en estados de patrón, episodios y alertas internas. No procesa imágenes ni ejecuta inferencia OVD; consume los eventos publicados por el plano de medios, consulta las definiciones activas de patrón declaradas en la configuración experimental y actualiza el estado correspondiente dentro de la corrida.

Su función arquitectónica es cerrar la brecha entre detección visual y salida operativa asistiva. Una detección indica que el modelo observó una evidencia en un frame o instante determinado; un patrón confirmado indica que esa evidencia fue evaluada bajo criterios de persistencia, umbral, histéresis y, cuando corresponda, reglas espaciales o contextuales. Por lo tanto, el motor constituye la frontera donde la evidencia perceptiva deja de ser una salida aislada del detector y pasa a formar parte de una interpretación temporal trazable.

El motor se diseña para admitir el catálogo completo de patrones del prototipo, pero su activación efectiva depende de la configuración de corrida, los módulos habilitados y la disponibilidad de evidencia suficiente. De este modo, la arquitectura puede incorporar progresivamente patrones de mayor complejidad sin modificar la lógica central del plano de control.

###### 17.3.8.3.1. Patrón de riesgo como unidad evaluable

El motor no evalúa condiciones de riesgo sueltas, sino patrones de riesgo activos. Cada patrón referencia una condición del catálogo y define cómo esa condición debe ser evaluada durante la corrida. De este modo, la condición conserva el significado semántico del riesgo observado, mientras que el patrón agrega criterios operativos de activación, sostenimiento y cierre.

Esta separación evita que el sistema dependa de reglas rígidas incorporadas directamente en el código. Una misma condición puede evaluarse mediante distintas estrategias de evidencia, umbrales, ventanas temporales o dependencias opcionales, siempre que la configuración experimental lo declare. El patrón funciona, por lo tanto, como una definición evaluable: indica qué evidencia acepta, durante cuánto tiempo debe sostenerse, qué severidad tiene, qué histéresis aplica y qué evento debe emitirse cuando cambia de estado. La codificación PR-01 a PR-06 identifica cada patrón y lo mantiene distinguible de la condición observable que evalúa (CR-01 a CR-06): una nombra el fenómeno, la otra la regla operativa que decide cuándo se lo considera sostenido.

• **Identificación del patrón**. Código, condición asociada y versión.

• Evidencia requerida. Detecciones o relaciones necesarias. En el núcleo: person y evidencia positiva de helmet o vest.

• Granularidad. Por escena (scene) o por sujeto (subject).

• **Criterio temporal**. Ventana de confirmación expresada en milisegundos, declarada por patrón.

• **Histéresis y cierre**. Ventana de resolución expresada en milisegundos, declarada por patrón.

• **Umbrales y precondiciones de evidencia**. Confianza mínima del sujeto y del EPP, y área mínima del sujeto, declaradas por patrón; umbrales de postproceso declarados en la configuración del plano de medios.

• **Región de evaluación**. Franja vertical y margen lateral relativos a la caja del sujeto, declarados por patrón (región cefálica para PR-01; torso para PR-02).

• **Severidad configurada**. Severidad conceptual asignada por patrón desde el catálogo metodológico.

• **Dependencias opcionales**. Identidad temporal, zonas y relaciones entre entidades.

• **Salida esperada**. Transición de estado, alerta interna y eventos asociados.

**Nota.** La tabla define los componentes de una definición de patrón de riesgo. Los valores adoptados para el núcleo validable se documentan junto a la configuración efectiva en la sección 17.4.6. Los tiempos se expresan en milisegundos para conservar su significado ante distintas cadencias de procesamiento.

En particular, la severidad no debe derivarse de una detección aislada en un frame, sino de la definición del patrón y del catálogo metodológico consolidado. En el núcleo del prototipo, este valor es estático por corrida: orienta la interpretación de prioridad y latencia esperada, pero no se recalcula frame a frame ni depende de la inferencia OVD, de la publicación de evidencia perceptiva ni de los mecanismos de distribución externa. Cualquier ajuste posterior de severidad por zona, proximidad, persistencia o combinación de condiciones corresponde a extensiones condicionadas y debe declararse explícitamente en la configuración de corrida.

###### 17.3.8.3.2. Memoria temporal y ciclo de evaluación

La granularidad de la memoria temporal es un parámetro explícito de la definición de patrón. Bajo granularidad de escena, el estado se indexa por (patrón, fuente) y evalúa la continuidad de la condición en la escena. Bajo granularidad de sujeto, se indexa por (patrón, fuente, identidad) y exige una identidad temporal válida.

El identificador de detección es local a una unidad visual y no constituye identidad entre frames. La granularidad de sujeto sólo puede utilizar una identidad producida por un componente de seguimiento o por un decorador equivalente del plano de control. La capacidad puede habilitarse por configuración sin modificar el contrato de percepción; la identidad resultante se conserva en los artefactos del control, no en el JSONL ordinario del plano de medios.

La granularidad de escena sostiene una afirmación precisa: la condición persiste en la escena. No permite concluir que el mismo sujeto sostuvo el riesgo durante toda la ventana, porque una rotación de personas podría mantener la condición de forma continua. Esa segunda afirmación requiere granularidad de sujeto.

La exclusión de métricas MOT no elimina esta capacidad. La arquitectura separa la identidad necesaria para indexar el estado del patrón de la evaluación formal del desempeño de seguimiento.

El ciclo de evaluación selecciona evidencias, actualiza la memoria, aplica la ventana de confirmación y la histéresis, registra la transición y conserva la causa. Los descartes de fuente, huecos temporales y pérdida de identidad se distinguen de la ausencia real de evidencia.

###### 17.3.8.3.3. Evaluación según niveles de complejidad del catálogo

El motor debe respetar la clasificación metodológica de condiciones por nivel de complejidad ya definida en el desarrollo metodológico. Desde el diseño arquitectónico, esa clasificación se traduce en distintos requisitos de evaluación: algunos patrones pueden resolverse con evidencia perceptiva y persistencia temporal simple, mientras que otros sólo deben activarse cuando la corrida habilite insumos adicionales como tracking, zonas parametrizadas o reglas espaciales.

Esta diferenciación permite diseñar un motor único sin sobredimensionar el prototipo experimental. La arquitectura mantiene una lógica común de evaluación, pero adapta sus entradas y criterios según el patrón activo y la configuración de corrida. De este modo, el plano de control puede incorporar condiciones más complejas sin rediseñarse, siempre que existan los insumos necesarios para evaluarlas de manera trazable.

**Tabla 44**

*Diseño del motor de patrones según condición de riesgo*

| **Patrón y condición asociada** | **Evidencia y regla de evaluación** | **Dependencias arquitectónicas** | **Tratamiento en el prototipo** |
| --- | --- | --- | --- |
| PR-01 / CR-01 — Persona sin casco | Detecciones positivas de person y helmet. Para cada persona, el plano de control evalúa casco en la región cefálica y estabiliza la ausencia inferida mediante confianza, persistencia e histéresis. | Eventos de percepción, coordenadas comparables y referencia temporal. La granularidad de sujeto requiere identidad temporal válida; la de escena no. | Núcleo validable. Produce estados candidato, confirmado, sostenido y resuelto, además de una alerta interna trazable por episodio. |
| PR-02 / CR-02 — Persona sin chaleco reflectivo | Detecciones positivas de person y vest. Para cada persona, el plano de control evalúa chaleco en la región del torso y estabiliza la ausencia inferida mediante los criterios temporales configurados. | Eventos de percepción, coordenadas comparables y referencia temporal. Comparte la misma frontera contractual que PR-01. | Núcleo validable. Se evalúa mediante la misma cadena arquitectónica, con severidad y ventanas propias. |
| PR-03 / CR-03 — Trabajo en altura sin anticaídas visible | Evidencia de persona en altura o sobre estructura elevada, junto con ausencia o baja evidencia de sistema anticaídas visible. El motor requiere validar contexto espacial antes de confirmar. | OVD sobre entidades o atributos, reglas espaciales intra-frame y evidencia visual suficiente del escenario. | Extensión condicionada. No bloquea el núcleo; sólo debe activarse si existen datos o escenas que permitan evaluar la condición completa. |
| PR-04 / CR-04 — Borde elevado desprotegido con personas próximas | Evidencia de borde, plataforma o zona elevada, ausencia de baranda o protección colectiva y presencia de personas próximas. El motor evalúa proximidad y condición de protección. | OVD de entidades del entorno, reglas espaciales, posible parametrización de regiones y cámara con perspectiva adecuada. | Extensión condicionada. Puede reportarse parcialmente si sólo se detectan componentes visuales sin validar la condición completa. |
| PR-05 / CR-05 — Maquinaria cerca de peatones | Evidencia de maquinaria y personas con relación de proximidad sostenida. El motor evalúa distancia relativa, duración del acercamiento y persistencia del episodio. | OVD de entidades, seguimiento temporal o asociación equivalente, reglas de proximidad y métricas de continuidad. | Condicionado a módulo contextual. No pertenece al núcleo; requiere instrumentación temporal y control de falsos positivos relacionales. |
| PR-06 / CR-06 — Persona en zona restringida | Evidencia de persona dentro de un polígono o zona definida externamente. El motor evalúa permanencia, entrada, salida y cierre por ausencia sostenida. | Cámara fija o geometría controlada, polígono de zona, OVD de persona y, preferentemente, tracking o asociación temporal. | Condicionado a escenario EBE controlado o fuente fija. Requiere parametrización explícita de zona en la configuración de corrida. |

***Nota****.* La tabla diseña el comportamiento esperado del motor frente al catálogo completo de patrones. El tratamiento “núcleo validable” identifica patrones obligatorios para el prototipo experimental; el tratamiento “extensión condicionada” indica capacidades previstas que sólo deben habilitarse cuando existan datos, módulos e instrumentación suficientes.

###### 17.3.8.3.4. Salidas, episodios y trazabilidad del motor

La salida principal del motor no es una alerta aislada, sino una secuencia de eventos derivados que describen el ciclo de vida del patrón: inicio de candidato, confirmación, sostenimiento, resolución o descarte por evidencia insuficiente. La alerta interna se registra sólo cuando una transición válida confirma el patrón. Esta decisión evita que el sistema emita alertas por cada frame positivo y permite analizar episodios con inicio, duración, evidencia causal y cierre.

Cada transición debe conservar trazabilidad suficiente para explicar su origen: configuración de corrida, patrón evaluado, condición asociada, evidencia considerada, ventana temporal, umbrales aplicados, estado previo, estado nuevo y referencia temporal. Esta información permite reconstruir por qué una alerta fue generada, por qué un episodio se resolvió, qué evidencia fue descartada y qué parámetros condicionaron el resultado.

Las métricas operativas del plano de control se apoyan en estas transiciones: el tiempo hasta la primera detección (TTFD) se ancla en la primera evidencia perceptiva relevante; la latencia de alerta (t_alert-system) se cierra con el registro de la alerta interna que sigue a la transición a confirmado; la tasa de detección sostenida (SDR) se calcula sobre la continuidad del episodio; y los errores o descartes permiten distinguir una ausencia real de evidencia de una falla técnica o de una pérdida por muestreo.

De esta manera, el motor de evaluación de patrones permite que la arquitectura sostenga una cadena operativa completa: detección OVD, evidencia perceptiva normalizada, patrón candidato, patrón confirmado, alerta interna por episodio, sostenimiento, resolución y reconstrucción experimental. Con este diseño, CR-01 y CR-02 pueden implementarse como núcleo validable, mientras que los patrones más complejos permanecen incorporables sin alterar la separación entre plano de medios y plano de control.

##### 17.3.8.4. Transporte, persistencia y trazabilidad experimental

La arquitectura diferencia el canal de transporte del repositorio persistente. El canal desacopla productores y consumidores; el repositorio conserva los hechos necesarios para reconstruir la corrida. Esta separación evita atribuir durabilidad a un mecanismo de mensajería diseñado para baja latencia.

El repositorio es la fuente de verdad. Cada evento de percepción se escribe en un archivo JSONL de sólo adición antes de publicarse. Los cambios de estado, alertas, métricas y errores siguen la misma regla en sus componentes respectivos. Si el canal falla, el hecho persistido permanece disponible para relectura.

En el camino de ejecución en vivo correspondiente a EBE, el canal adopta ZeroMQ con patrón publicador-suscriptor, msgpack, tópicos por tipo de evento y un número de secuencia monótono dentro del envoltorio versionado del bus. El payload publicado corresponde al mismo contenido lógico persistido, de modo que la corrida pueda releerse posteriormente por el camino diferido sin redefinir la evidencia.

El consumidor debe suscribirse antes de que el productor publique. Por ello, una corrida en vivo se inicia primero en el plano de control y luego en el plano de medios. La respuesta de creación del control implica disponibilidad del consumidor y el orquestador verifica esa precondición.

La pérdida se detecta mediante huecos de secuencia. Un hueco incrementa bus_dropped_events, degrada la corrida y queda expuesto en el reporte; nunca se interpreta como ausencia de evidencia en la escena.

El cierre de la corrida se propaga mediante un evento de ciclo de vida cuyo hito de finalización delimita el final lógico y permite cerrar consumidores, consolidar artefactos y distinguir un fin normal de una interrupción.

La sustitución futura por un broker conserva la misma frontera contractual. La durabilidad, la re-evaluación y la causalidad no dependen de la tecnología del canal, sino de la regla persistir-primero y de los esquemas versionados.

#### 17.3.9. Integración entre condición, estrategia de detección, patrón y alerta

Esta sección precisa cómo las condiciones de riesgo definidas metodológicamente se materializan dentro de la arquitectura. Su finalidad es vincular la condición observable con una estrategia de detección, la evidencia perceptiva publicada por el plano de medios, la evaluación del patrón en el plano de control y el registro de una alerta interna por episodio. De este modo, la plataforma evita tratar los prompts como condiciones completas o las detecciones individuales como alertas directas, conservando una cadena causal trazable entre percepción, evaluación y salida asistiva.

##### 17.3.9.1. Cadena de traducción arquitectónica

La cadena de traducción comienza con una condición observable del catálogo metodológico. Esa condición define qué fenómeno se desea monitorear, pero no determina por sí misma cómo debe detectarse. La estrategia de detección cumple esa función: establece si la evidencia se buscará mediante un prompt directo, una combinación de consultas, evidencia auxiliar o reglas contextuales habilitadas por la configuración de corrida.

El plano de medios aplica la estrategia configurada y publica evidencia perceptiva normalizada. Esa evidencia queda asociada a la corrida, la fuente, el modelo, los prompts activos, los umbrales y la referencia temporal correspondiente. Sin embargo, todavía no constituye una alerta. Su función es alimentar al plano de control con información comparable y trazable.

El plano de control evalúa esa evidencia mediante el patrón correspondiente y, cuando la evaluación confirma el episodio, registra una alerta interna. Esa alerta es una salida asistiva del sistema: no equivale a una notificación externa ni a una certificación normativa.

**Figura 4.5**

*Cadena de traducción entre condición, estrategia, evidencia, patrón y alerta*

⟦FIGURA: no extraída — ver el .docx⟧

**Nota.** La figura muestra cómo una condición definida metodológicamente se materializa en la arquitectura. La estrategia orienta la producción de evidencia en el plano de medios; el patrón evalúa esa evidencia en el plano de control; y la alerta interna registra el episodio confirmado.

##### 17.3.9.2. Estrategia adoptada para el núcleo validable

Para el núcleo validable se adopta la estrategia indirecta con inferencia espacial de ausencia (E-IND). La frontera que esa elección fija es explícita: el plano de medios informa qué entidades observó, dónde y con qué confianza; el plano de control decide si la evidencia del elemento de protección se asocia al sujeto, construye el estado evaluable de la condición y lo estabiliza antes de registrar una alerta.

La estrategia se adopta por auditabilidad: cada evaluación puede reconstruirse a partir de la caja del sujeto, la región analizada, las detecciones de protección, los umbrales y la regla aplicada, de modo que la ausencia no se presenta como una conclusión opaca del modelo. La detección directa (E-DIR) y las variantes híbridas (E-HYB) se conservan como ramas comparativas configurables, con conjuntos de prompts y reglas identificados por separado; comparten los contratos de publicación, evaluación temporal y registro, de modo que la comparación no requiera alterar la arquitectura central.

##### 17.3.9.3. Comparabilidad entre estrategias

Para que la comparación entre variantes sea posible, cada evidencia publicada conserva el vínculo con la condición que representa, la estrategia de detección utilizada y la configuración efectiva de la corrida. Una misma condición puede evaluarse con distintas estrategias sin alterar la semántica del sistema, siempre que la corrida declare la variante utilizada y los eventos resultantes conserven esa referencia. Es esa referencia declarada, y no una reinterpretación posterior de los artefactos, la que permite atribuir una diferencia de resultados a la estrategia evaluada y no a un cambio no declarado en la cadena.

#### 17.3.10. Distribución de alertas confirmadas

La alerta interna es el hecho terminal del plano de control, pero todavía no es un aviso. Esta sección define el tramo que la convierte en entregas observables sin incorporar la comunicación a la ruta que la produjo.

##### 17.3.10.1. Función arquitectónica de la distribución

La función arquitectónica de la distribución es transformar una alerta ya confirmada en intentos de entrega registrados, sin participar del razonamiento que la produjo. El plano de control publica cada alerta confirmada en un bus de alertas dedicado; el módulo de distribución la consume desde allí, aplica la política de notificación y registra el resultado de cada intento. No constituye un tercer plano ni un cuarto rol funcional: es un módulo desacoplado, y esa condición es la que impide que la indisponibilidad de un canal externo se propague al motor de patrones.

El pipeline de distribución comprende una fuente de alertas, una política de notificación, un sobre versionado, un adaptador de canal y un ledger de entregas. La misma lógica admite relectura DBE desde artefactos persistidos y consumo EBE desde el bus de alertas, sin modificar la semántica de la alerta de entrada.

La política ordinaria prioriza trazabilidad, idempotencia y operación no bloqueante. Una falla del canal genera un resultado de entrega y un error interpretable, pero no invalida ni elimina la alerta interna.

##### 17.3.10.2. Consumidores, canales y control de ciclo de vida.

El tramo de distribución separa el dato del gobierno. Las alertas confirmadas llegan por el bus de alertas dedicado, en sentido único desde el plano de control. Las órdenes de ciclo de vida, en cambio, llegan por una interfaz de gobierno propia del módulo, que permite crear, consultar, cancelar y descartar corridas de entrega. La interfaz de inspección y el orquestador experimental lo gobiernan por esa vía —del mismo modo que a los otros módulos— y nunca consumen el bus directamente. Para la relectura DBE el módulo conserva una entrada offline sobre alertas persistidas. Ambos caminos utilizan los mismos contratos de alerta interna, sobre de notificación y registro de entrega, por lo que la modalidad de ejecución no modifica la semántica de la alerta ni del resultado de entrega.

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

*Nota.* El módulo de distribución conserva su propio estado operativo y su ledger; no utiliza el almacenamiento continuo de video ni requiere acceso a frames crudos.

##### 17.3.10.3. Política, medición y límites de interpretación

El conjunto de patrones adoptado no suprime confirmaciones: cada alerta interna se registra para conservar la dinámica real del episodio. La decisión es deliberada —el motor dispone de control de re-confirmación por patrón y sujeto y el núcleo lo deja inactivo— porque un motor que suprimiera dejaría de reflejar la duración del episodio y no permitiría distinguir una condición que persiste de una que se resolvió.

La supresión de re-notificación se reubica en la política del módulo de distribución, y al reubicarse cambia de granularidad: el motor la aplicaría por patrón y sujeto, mientras que la política de entrega aplica una ventana de silencio por condición y fuente, porque para una notificación asistiva lo relevante es que esa condición en esa cámara ya fue avisada. La agrupación de avisos y la limitación de tasa quedan como punto de extensión de la política. Una alerta suprimida para comunicación existió y continúa siendo medible: las re-alertas de un episodio activo se informan por separado y no se computan como falsos positivos, de modo que una decisión de comunicación no altera la precisión del motor.

El ledger de entregas aplica una clave de idempotencia por notificación y canal, es de sólo agregado y acumula entre corridas: al reutilizar un directorio de salida la generación anterior se archiva íntegra y la deduplicación considera todas las generaciones, por lo que un reprocesamiento no vuelve a entregar lo ya entregado. Cada fila conserva número de intento, marca temporal, resultado, motivo de error y confirmación del canal, y distingue cinco resultados: entrega exitosa, supresión por política, descarte por duplicado, falla de un intento y descarte definitivo por agotamiento de reintentos. La unidad de conteo del tramo es la notificación y no la fila: una notificación no entregada deja una fila por cada intento más la del descarte definitivo.

Cada fila registra además la modalidad en que se midió t_alert-notification, y la latencia del tramo se informa siempre separada por modalidad: en relectura diferida el intervalo incorpora el ritmo de reinyección de las alertas persistidas, que es propiedad del reprocesamiento y no del canal.

#### 17.3.11. Contratos e interfaces internas

Los contratos estabilizan la semántica de intercambio entre componentes: definen qué información cruza cada frontera y bajo qué versión. En la arquitectura consolidada del núcleo se expresan como modelos de datos versionados, con serializaciones explícitas e interfaces concretas, y cada uno queda asociado a una corrida para que productores y consumidores puedan evolucionar de forma independiente. La versión viaja dentro del payload y no en el envoltorio de transporte: el canal puede cambiar sin que el hecho persistido pierda la identificación de su esquema. Las capacidades futuras deben evolucionar de forma aditiva sin romper la lectura de corridas históricas.

##### 17.3.11.1. Fronteras informacionales de intercambio

Cada frontera existe para proteger una decisión. La del gobierno del experimento evita una configuración monolítica y vincula ciclos de vida independientes. La de entrada visual unifica los dos escenarios sin ocultar su temporalidad. La de salida del plano de medios encapsula la heterogeneidad del detector. La de entrada del plano de control obliga a evaluar reglas sobre eventos y no sobre frames crudos. La de salida del plano de control diferencia detección, patrón y alerta. La de distribución mantiene la comunicación y la idempotencia aguas abajo de la alerta interna. Y la de referencia y soporte sostiene la medición y la reconstrucción con estados de aplicabilidad. Las fronteras son lógicas: no prescriben que cada responsabilidad se despliegue en una máquina, proceso o contenedor independiente.

##### 17.3.11.2. Contratos mínimos e interfaces

Todo contrato declara su identidad de esquema y su versión como primer elemento del payload.

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

*Nota.* Los contratos de referencia temporal y distribución tienen el mismo estatuto formal que los eventos de percepción y control: una medición o entrega no es reproducible si su entrada carece de versión y procedencia.

El evento central del sistema es el evento de percepción. Agrupa la identidad de esquema versionada, la corrida, la unidad visual, la fuente, el modelo, los prompts, las detecciones y los tiempos. Cada detección conserva etiqueta, prompt, confianza, caja en píxeles y normalizada y área. detection_id sólo identifica una detección dentro de la unidad visual; no constituye identidad entre frames. Los campos opcionales se incorporan de forma aditiva y se omiten cuando no están disponibles.

La referencia temporal de evaluación impone dos invariantes de validez. Primero, la identidad de la fuente de la corrida y la del clip anotado deben coincidir; para el banco temporal se utiliza source_id = clip_id. Segundo, la incertidumbre no fabrica una infracción: cuando el estado del EPP no es juzgable, el episodio no se extiende como violación.

La cadena temporal conserva cinco hitos por alerta: primera evidencia positiva —identificada por unit_id—, transición a candidato, transición a confirmado, registro de la alerta interna y, cuando existe distribución, confirmación de entrega. Estos hitos permiten medir cada tramo sin mezclar relojes ni poblaciones.

##### 17.3.11.3. Criterios de evolución durante la implementación experimental

La superficie de crecimiento del evento de percepción se mantiene acotada y separada de las reglas de riesgo. La identidad temporal de sujeto es un campo opcional y la única identidad válida entre frames: el contrato la admite y el plano de control puede materializarla por configuración, sin que el plano de medios necesite emitirla y sin mezclar esa capacidad con las métricas de seguimiento. Velocidad, dirección, puntos clave de pose y máscaras de segmentación quedan previstos como campos opcionales que no modifican la semántica mínima del evento ni desplazan al bounding box. Las relaciones entre sujeto, evidencia de soporte y clase ausente, en cambio, pertenecen al plano de control: el plano de medios publica detecciones individuales.

#### 17.3.12. Trazabilidad experimental y minimización de evidencia visual

La trazabilidad experimental permite reconstruir cómo una corrida produjo una alerta interna. Para ello, la arquitectura debe conservar la relación entre configuración de corrida, fuente visual, modelo utilizado, prompts activos, evidencia perceptiva, transición de estado del patrón, alerta registrada y métricas o errores asociados. Sin esa relación, una alerta pierde valor experimental porque no puede auditarse, compararse ni analizarse con suficiente rigor.

En continuidad con los contratos versionados definidos en la sección anterior, esta sección no vuelve a especificar estructuras de intercambio, sino que precisa qué hechos deben conservarse y bajo qué política se gestiona la evidencia visual. El objetivo es sostener la interpretación de resultados sin convertir la trazabilidad en almacenamiento indiscriminado de video ni ampliar el alcance del prototipo experimental.

##### 17.3.12.1. Repositorio de eventos para reconstrucción experimental

El repositorio utiliza archivos JSONL de sólo adición por corrida y por tipo de hecho. La decisión principal continúa siendo impedir la sobrescritura silenciosa; la materialización elegida agrega una representación simple, inspeccionable y re-evaluable sin introducir una base de datos como dependencia del núcleo.

Cada corrida conserva configuración efectiva, manifiesto, procedencia y versión de código junto a detecciones, métricas, errores, transiciones y alertas. El soporte experimental agrupa los runs de los componentes bajo experiment_id, copia los artefactos livianos y referencia los de mayor volumen.

Toda alerta puede reconstruirse hasta la configuración efectiva, el conjunto de prompts, el modelo, la fuente y la versión de código que la produjeron. La persistencia no requiere video crudo continuo y mantiene separados los hechos originales de sus proyecciones tabulares o reportes.

##### 17.3.12.2. Hechos persistibles mínimos

Los hechos persistibles mínimos representan aquello que debe conservarse para interpretar una corrida y reconstruir una alerta interna. No constituyen una nueva lista de contratos ni una especificación definitiva de base de datos. Mientras los contratos establecidos estabilizan el intercambio entre responsabilidades, los hechos persistibles establecen qué información debe quedar disponible para análisis posterior, comparación entre corridas y reconstrucción de evidencia. Dado que todos los elementos incluidos en la tabla forman parte del mínimo necesario, no se distingue un carácter obligatorio fila por fila.

**Tabla 47**

*Hechos persistibles mínimos para reconstrucción experimental*

| **Hecho persistible mínimo** | **Uso en reconstrucción** |
| --- | --- |
| Inicio y cierre de corrida | Delimita la ejecución y vincula los hechos a los identificadores de experimento y de corrida. |
| Manifiesto y configuraciones efectivas | Reconstruye escenario, fuente, modelo, prompts, patrones, módulos, versiones y políticas aplicadas. |
| Procedencia e identidad de fuente | Conserva dataset o clip, partición, huella y la invariante source_id = clip_id cuando existe referencia temporal. |
| Eventos de percepción | Permiten reconstruir detecciones, unidad visual, modelo, prompt, coordenadas, puntajes y tiempos del plano de medios. |
| Unidades omitidas o descartadas | Explican pérdida de cobertura temporal, control de ritmo, saturación o degradación. |
| Cambios de estado del patrón | Reconstruyen candidato, confirmado, sostenido y resuelto, con evidencia y tiempos. |
| Primera evidencia positiva | Registra unit_id y tiempo de la evidencia que inicia la cadena causal entre planos. |
| Alertas internas | Identifican episodio, patrón, severidad, sujeto o escena, evidencia causal y momento de registro. |
| Entregas de distribución | Conservan canal, resultado, intento, idempotencia y confirmación de entrega cuando el tramo está habilitado. |
| Métricas y estado de aplicabilidad | Distinguen valores calculados, no calculados, no aplicables o no interpretables, siempre con causa. |
| Errores y anomalías | Permiten explicar fallas de fuente, inferencia, transporte, persistencia, evaluación o entrega. |
| Referencias de evidencia visual controlada | Vinculan capturas o clips autorizados sin convertir el video crudo continuo en mecanismo ordinario de trazabilidad. |

**Nota.** La tabla expresa hechos mínimos necesarios para reconstrucción experimental, no servicios ni clases de implementación. Los hechos asociados a seguimiento temporal, zonas, distribución externa de alertas, adaptación de modelos o evidencia visual controlada se incorporan sólo cuando la corrida habilita esas capacidades; no forman parte del conjunto mínimo para CR-01 y CR-02.

Esta selección prioriza la reconstrucción de la cadena causal de la alerta. Una detección aislada no es suficiente para explicar un episodio; debe poder relacionarse con la configuración que la produjo, el patrón que la evaluó, la transición que confirmó la condición y las métricas o anomalías que condicionaron el resultado. Por esa razón, los errores y descartes relevantes tienen el mismo valor interpretativo que los eventos funcionales: permiten distinguir una ausencia real de evidencia de una falla técnica, un descarte por muestreo o una limitación de la fuente.

Las extensiones condicionadas deben mantener esta lógica. Si se incorpora seguimiento temporal, zonas, reglas espaciales, notificaciones externas o adaptación de modelos, esos hechos podrán persistirse como información adicional de la corrida. Sin embargo, no deben desplazar la cadena mínima de reconstrucción ni convertir capacidades exploratorias en requisitos del núcleo experimental.

##### 17.3.12.3. Política de evidencia visual mínima

La arquitectura adopta una política de minimización de evidencia visual. En el comportamiento ordinario del prototipo experimental, la trazabilidad se apoya en identificadores, metadatos, eventos, métricas, coordenadas, referencias temporales y relaciones causales entre hechos persistidos. El almacenamiento continuo de video crudo no forma parte del flujo base, porque aumenta volumen, complejidad y riesgo de privacidad sin ser necesario para reconstruir la mayoría de las decisiones experimentales.

Cuando se requiera evidencia visual para revisión técnica, validación o comunicación académica, ésta debe conservarse como artefacto controlado: snapshot, recorte anotado, clip breve, hash, referencia a archivo o vínculo asociado a una alerta o corrida específica. Su uso debe estar justificado por la finalidad experimental y no reemplaza métricas, eventos persistidos ni criterios explícitos de evaluación.

Esta decisión preserva el carácter asistivo y no identificatorio de la plataforma. El sistema no realiza reconocimiento facial, no identifica nominalmente a trabajadores, no extrae biometría y no emite decisiones normativas autónomas. La alerta interna sólo orienta la atención humana sobre una condición visualmente observable; la interpretación final y cualquier acción preventiva permanecen fuera del sistema automatizado.

#### 17.3.13. Observabilidad arquitectónica e instrumentación de métricas

La observabilidad forma parte del contrato experimental. Cada métrica debe declarar la señal que utiliza, el inicio y el cierre del reloj, la unidad, la población y la condición de aplicabilidad. Cuando una medición no tiene significado, la plataforma conserva la causa en lugar de publicar cero u omitir el campo.

##### 17.3.13.1. Materialización arquitectónica de las métricas

**Tabla 48**

*Métricas y evidencias por tramo arquitectónico*

| **Tramo** | **Punto de medición** | **Métricas o evidencias** |
| --- | --- | --- |
| Captura y host | Captura física, timestamp de fuente y dequeue en el host. | capture_to_host, jitter y disponibilidad temporal, cuando existe ancla compatible. |
| Plano de medios | Dequeue, normalización, inferencia, postproceso y publicación. | G2A, latencia de inferencia, FPS efectivo, throughput y descartes. |
| Bus media-control | Publicación, secuencia y recepción. | Huecos de seq, integridad, atraso y correlación por unit_id. |
| Plano de control | Primera evidencia, candidato, confirmado, alerta y resolución. | TTFD, t_alert-system, latencia interna, SDR, transiciones y re-alertas. |
| Distribución | Disponibilidad de alerta, intento y confirmación del canal. | t_alert-notification, resultados de entrega, supresiones, duplicados y errores. |
| Soporte experimental | Consolidación por corrida y entorno. | Recursos, estados de aplicabilidad, causas, robustez y reporte reconstruible. |

*Nota.* La cadena temporal completa se informa por tramos. Los percentiles de tramos diferentes no son aditivos y no deben sumarse para fabricar una latencia de extremo a extremo.

##### 17.3.13.2. Definiciones operacionales y criterio de relojes

**Tabla 49**

*Diccionario de métricas: definiciones operacionales*

| **Métrica** | **Inicio** | **Cierre** | **Unidad y aplicación** |
| --- | --- | --- | --- |
| capture_to_host | Captura física o timestamp equivalente de la fuente | Dequeue de la unidad en el host | ms; sólo sobre fuente en vivo con ancla temporal interpretable. |
| G2A | Dequeue de la unidad en el host de procesamiento | Resultado algorítmico o alerta asociada a esa unidad | ms, p50/p95/p99; exige un único dominio de reloj. No empieza en el fotón. |
| TTFD | Inicio anotado del episodio | Primera evidencia positiva | ms; requiere la referencia temporal anotada. Si no hay evidencia, es nulo con causa. |
| t_alert-system | Inicio anotado del episodio | Registro de la alerta interna | ms; se reporta por campaña y condición. |
| Latencia interna | Primera evidencia positiva | Registro de la alerta interna | ms; separa cómputo y espera deliberada por persistencia. |
| SDR | Episodio anotado | Cobertura positiva dentro del episodio | Proporción [0,1]; sólo comparable dentro de una misma cadencia. |
| Precisión / exhaustividad / F1 de alertas | Alertas y episodios evaluables | Matching por episodio | Proporción; los negativos no integran P/R/F1 y las re-alertas no son FP. |
| t_alert-notification | Alerta disponible en el bus de distribución | Confirmación de entrega del canal | ms; no aplica sin distribución y no se suma a t_alert-system. |

Las latencias intra-host utilizan reloj monotónico local. Los monotónicos de hosts distintos no se restan. Cuando un trayecto cruza dominios de reloj sin una sincronización válida, la métrica se declara not_interpretable con su causa.

El criterio de detección positiva se comparte con el motor de patrones. La evaluación no reimplementa una segunda definición de evidencia, lo que evita divergencias silenciosas entre el sistema que decide y el sistema que mide.

##### 17.3.13.3. Señales observables y estados de aplicabilidad

**Tabla 50**

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

Cada métrica incluye status y cause. Los estados admitidos son computed, applicable_not_computed, not_applicable y not_interpretable. La plataforma no publica un cero cuando lo correcto es declarar una causa.

Una fuente de imágenes independientes produce not_applicable/non_temporal_source para patrones temporales; un trayecto con monotónicos de dos hosts produce not_interpretable/cross_node_monotonic_clock; una corrida sin referencia produce not_applicable/no_ground_truth; y un TTFD sin detección positiva permanece nulo con causa.

##### 17.3.13.4. Registro de resultados por corrida

El reporte consolida manifiesto, configuraciones efectivas, métricas por tramo, estado de aplicabilidad, alertas, re-alertas, descartes, errores, recursos y limitaciones de interpretación. Cada valor mantiene la condición, el escenario y la población sobre la que se calculó.

t_alert-system integra el diccionario citable de la plataforma. Las métricas de precisión, exhaustividad y F1 de alertas se obtienen mediante el evaluador temporal que conserva denominadores por estrato; no se duplican mediante agregados sin procedencia en el reporte general.

El reporte constituye una proyección de hechos persistidos. Puede regenerarse sin modificar los eventos originales y no se utiliza como fuente de verdad cuando existe el artefacto primario.

#### 17.3.14. Escenarios experimentales DBE y EBE

La definición metodológica de ambos escenarios corresponde a la sección 17.1.4.4; aquí se conservan únicamente sus consecuencias arquitectónicas.

##### 17.3.14.1. DBE como escenario de estabilización reproducible

En DBE, la fuente es regulable y puede releerse bajo la misma configuración; por ello, la arquitectura prioriza identidad estable de unidades, orden lógico, persistencia previa y reconstrucción determinista de eventos, patrones y alertas. Esta propiedad permite estabilizar contratos y comparar configuraciones sin que la variabilidad de captura se convierta en una variable implícita.

##### 17.3.14.2. EBE como escenario de fuente en vivo controlada

En EBE, la fuente opera en vivo y la escena continúa evolucionando aunque el pipeline se retrase; por ello, la arquitectura instrumenta captura o recepción, colas, descartes, jitter, actualidad y dominio de reloj. La compatibilidad de contratos se conserva, pero la interpretación de latencia y cobertura temporal debe incluir los efectos propios de la fuente continua.

##### 17.3.14.3. Equivalencia arquitectónica entre escenarios

DBE y EBE deben converger en la misma arquitectura una vez normalizada la entrada visual. La diferencia entre escenarios se ubica antes y alrededor de la disponibilidad del frame: origen de la fuente, referencia temporal, política de muestreo, control de ritmo e instrumentación de omisiones o descartes. Después de esa frontera, la inferencia OVD, el postproceso, la publicación de evidencia perceptiva, la evaluación de patrones y el registro de alertas internas deben mantener la misma semántica.

Esta equivalencia evita construir dos flujos incompatibles. Si DBE y EBE produjeran contratos distintos o exigieran reglas de patrón diferentes, los resultados dejarían de ser comparables. En cambio, al conservar la misma estructura de eventos, métricas y hechos persistibles, la arquitectura permite analizar qué parte de la variación proviene de la fuente continua y qué parte corresponde al comportamiento del detector o de la evaluación de patrones.

La comparación entre escenarios debe declarar explícitamente qué variables cambiaron. Una corrida DBE y una corrida EBE pueden compartir modelo, prompts, umbrales y reglas de patrón, pero diferir en fuente, temporización, iluminación, compresión o criterio de descarte. Esas diferencias deben registrarse como parte de la configuración y de la observabilidad, no tratarse como detalles secundarios.

##### 17.3.14.4. Comparación arquitectónica entre DBE y EBE

La Tabla 51 resume las diferencias principales entre ambos escenarios desde una lectura arquitectónica. Su finalidad no es repetir la definición metodológica de DBE y EBE, sino mostrar qué decisiones de diseño se derivan de cada modo de evaluación y cómo deben interpretarse sus resultados.

**Tabla 51**

*Comparación arquitectónica entre escenarios DBE y EBE*

| **Dimensión** | **DBE** | **EBE** | **Implicancia arquitectónica** |
| --- | --- | --- | --- |
| Fuente de entrada | Imagen, dataset o vídeo local. | Cámara, RTSP, OAK-D o captura controlada. | La fuente se abstrae mediante metadatos comunes; su naturaleza temporal se declara por separado. |
| Control temporal | Alto; la secuencia puede repetirse bajo condiciones equivalentes. | Menor; intervienen captura, buffers, jitter, decodificación y disponibilidad del último frame. | EBE requiere instrumentar timestamps, colas, descartes y atraso acumulado. |
| Variabilidad externa | Baja o controlada, según cobertura del dataset. | Media o alta, según cámara, red local, códec, iluminación, movimiento, buffers y entorno. | Las diferencias de desempeño no deben atribuirse automáticamente al modelo OVD. |
| Instrumentación adicional | Orden lógico, referencia a dataset o archivo, política de muestreo y frames procesados. | Captura o recepción, profundidad de cola, descartes, jitter, reemplazo de frames y estado de fuente. | La observabilidad debe registrar diferencias temporales para interpretar latencia y cobertura. |
| Métricas prioritarias | Percepción; asociación espacial; y, sólo sobre vídeo temporal, patrones y alertas. | Integridad, capture_to_host, G2A, descartes, alertas y estado de entrega cuando corresponda. | Cada métrica debe declarar su punto de inicio, cierre, reloj y condición de aplicación. |
| Condición de comparabilidad | Misma configuración lógica y fuente reproducible; ground truth cuando corresponda. | Misma configuración lógica, con variabilidad temporal y condiciones de captura documentadas. | La comparación DBE/EBE requiere declarar qué variables permanecen constantes y cuáles cambian. |

***Nota.*** *DBE y EBE se interpretan como escenarios experimentales de una misma arquitectura. La diferencia principal se ubica en la fuente visual, la temporalidad y la instrumentación requerida; los contratos de evidencia, patrón, alerta, métricas y errores deben mantenerse compatibles para preservar comparabilidad experimental.*

Con esta organización, DBE funciona como escenario de estabilización y comparación controlada, mientras que EBE permite observar la integración con fuente en vivo bajo condiciones instrumentadas. La arquitectura no debe privilegiar un escenario mediante contratos diferentes, sino conservar una frontera común de entrada visual normalizada y registrar explícitamente las condiciones que afectan la interpretación de cada corrida.

##### 17.3.14.5. Alcance arquitectónico de EBE

EBE admite cámaras IP por RTSP, la OAK-D Pro PoE y otras fuentes continuas declaradas mediante el mismo adaptador conceptual. La arquitectura contempla tanto el dispositivo candidato como la contingencia con cámara IP convencional; ninguna alternativa modifica los contratos de percepción y control.

El rol EN puede operar como captura, preprocesamiento no semántico o preselección conservadora. La variante de preselección liviana en el borde es opcional, está deshabilitada por defecto y opera con el criterio de degradación segura fijado para las capacidades opcionales del plano de medios: una falla o incertidumbre del preselector no elimina la unidad del flujo principal. Toda transformación, descarte o cambio de resolución se registra.

La comparación entre una corrida DBE sobre archivo y una corrida EBE del mismo contenido exige una ancla común entre tiempo de medio y reloj de pared. Sin esa ancla, el matching temporal contra la referencia temporal se declara no interpretable; la integridad del bus y la relectura offline continúan siendo evaluables por separado.

**Tabla 52**

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

*Nota.* EBE es un escenario experimental y no una topología fija. La ubicación de servicios y dispositivos se declara por corrida.

##### 17.3.14.6. Naturaleza temporal de la fuente y aplicabilidad

La procedencia DBE o EBE no determina por sí sola si una fuente sostiene razonamiento temporal. Un vídeo de archivo y un stream vivo son temporales; un conjunto de imágenes independientes no lo es. La configuración deriva esta propiedad del tipo de fuente y no permite que el operador la contradiga.

Aplicar una ventana de persistencia sobre imágenes independientes produciría cero alertas por construcción, un resultado indistinguible de la ausencia real de riesgo. Para evitar ese cero silencioso, la evaluación de patrones se declara not_applicable/non_temporal_source. La corrida conserva valor para percepción y asociación espacial, pero no para continuidad o alerta temporal.

Las imágenes permiten afirmar sobre percepción; los clips temporales, sobre estado y episodios; y las fuentes en vivo, además, sobre transporte, actualidad y comportamiento operativo. Cada reporte debe limitar sus conclusiones al régimen que la fuente permite observar.

#### 17.3.15. Roles funcionales y unidades desplegables de referencia

Esta sección no redefine los roles funcionales ya establecidos en la consolidación metodológica: fija la topología de referencia con la que se materializan en el prototipo y ubica en ella al módulo de distribución. La única precisión que el diseño agrega es que ninguno de los tres roles equivale necesariamente a una máquina dedicada.

La topología de referencia dispone un nodo de borde para captura y un nodo central con GPU para procesamiento. El TN permanece fuera del camino operativo de inferencia: cualquier adaptación produce un checkpoint candidato que debe evaluarse posteriormente sobre el CPN y mantenerse como rama comparativa separada. El módulo de distribución no constituye un tercer plano ni un cuarto rol funcional: se modela como una unidad desplegable propia, gobernada por su propia interfaz HTTP y consumidora del bus de alertas. Puede co-ubicarse con el CPN o separarse sin modificar los contratos de alerta interna, notificación y entrega.

**Figura 4.6**

*Roles funcionales CPN, EN y TN*

⟦FIGURA: no extraída — ver el .docx⟧

*Nota.* Las flechas representan transferencia de vídeo, metadatos y checkpoints. No prescriben una cantidad de hosts ni incorporan el TN al trayecto de alerta.

**Tabla 53**

*Correspondencia de diseño entre roles funcionales y unidades desplegables de referencia*

| **Rol o unidad desplegable** | **Materialización de referencia** | **Responsabilidades** |
| --- | --- | --- |
| EN (modo base de captura) | Nodo de captura o unidad de ejecución de borde, sin GPU requerida. | Ingesta, control de ritmo, timestamps, healthcheck y normalización no semántica. La preselección liviana es opcional, fail-open y deshabilitada por defecto. |
| CPN | Nodo central o unidad de ejecución con GPU. | Inferencia OVD, postproceso, publicación, evaluación de patrones, alertas internas, persistencia, observabilidad y reporte. |
| TN | Clúster Mendieta u otro recurso de entrenamiento separado. | Preparación de checkpoints de una rama comparativa bajo datos, protocolo y criterios de escalamiento predefinidos; no sustituye la evaluación sobre el CPN. |
| Módulo de distribución | Servicio gobernado por configuración con interfaz HTTP propia, co-ubicable con el CPN o desplegable por separado. | Consumo de la alerta interna desde el bus de alertas, política de notificación, ledger de idempotencia, entrega MQTT y registro del sobre de notificación y del resultado de entrega. |

*Nota.* Las métricas se atribuyen al rol y al despliegue efectivamente declarados en la corrida. No se extrapolan entre CPN, EN y TN.

#### 17.3.16. Riesgos arquitectónicos y mitigaciones de diseño

Los riesgos arquitectónicos se formulan como modos de falla observables y se vinculan con una mitigación concreta. La arquitectura no presupone que una mitigación elimina el riesgo: exige instrumentarlo y declarar su efecto sobre la interpretación de la corrida.

**Tabla 54**

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

*Nota.* La materialización y la verificación de estos riesgos se documentan en las secciones de implementación y evaluación; aquí se conserva su tratamiento de diseño.

#### 17.3.17. Plan de materialización y criterios de avance

El plan de materialización ordena dependencias de diseño y no reemplaza el registro de implementación. El núcleo se construye primero sobre DBE para estabilizar contratos, evidencia, patrones y reporte; luego se incorporan EBE y capacidades opcionales sin modificar la semántica del flujo base.

El estado ejecutado de cada ítem corresponde a §17.4. En esta sección se conservan únicamente el entregable arquitectónico y el criterio que permite decidir si el incremento es verificable.

**Tabla 55**

*Plan de materialización del núcleo*

| **Incremento** | **Criterio de avance** |
| --- | --- |
| Manifiesto y configuración por componente | Una corrida puede reconstruirse mediante experiment_id, configs efectivas y versiones. |
| Fuentes DBE | Imágenes y vídeos ingresan con identidad, orden y naturaleza temporal declarados. |
| Vocabulario E-IND | Cada detección se atribuye a prompt_set_id y al rol de la clase. |
| Adaptador OVD | El modelo puede sustituirse sin modificar el contrato de percepción. |
| Normalización y postproceso | Las detecciones conservan coordenadas originales, normalizadas y filtros declarados. |
| Persistencia y bus | El hecho se persiste antes de publicarse y toda pérdida resulta detectable. |
| Patrones CR-01/CR-02 | La configuración fija región, granularidad, severidad y ventanas en milisegundos. |
| Alertas internas | Cada episodio confirmado produce una alerta idempotente y auditable. |
| Observabilidad | Cada métrica declara tramo, reloj, unidad, status y cause. |
| Reporte | La salida puede regenerarse desde los artefactos primarios. |

*Nota.* El núcleo no requiere canales externos, métricas MOT ni condiciones de Nivel 2 o 3 para sostener su cadena experimental.

La frontera de extensibilidad distingue tres clases de cambio. Una condición nueva del tipo «sujeto sin EPP» requiere una definición declarativa de patrón y vocabulario, sin modificar contratos ni reentrenar el modelo. Una familia relacional, zonal o de trayectoria requiere un evaluador nuevo en el plano de control. Un modelo, una fuente o un canal nuevos requieren sus respectivos adaptadores, manteniendo estables los contratos centrales. El costo medido de incorporar extensiones se documenta en las secciones de implementación y evaluación.

#### 17.3.18. Cierre del diseño arquitectónico

El diseño define una plataforma experimental compuesta por plano de medios, plano de control, soporte experimental y un tramo desacoplado de distribución. La organización protege la ruta crítica, separa evidencia de interpretación y conserva una cadena causal reconstruible desde la fuente hasta la entrega.

El núcleo de CR-01 y CR-02 utiliza evidencia positiva de person, helmet y vest, inferencia espacial de ausencia y estabilización temporal por patrón. La granularidad de escena y la granularidad de sujeto se tratan como configuraciones semánticamente distintas; la identidad personal permanece fuera del alcance.

La arquitectura fija contratos versionados, JSONL de sólo adición y dos patrones de acople: gobierno mediante HTTP, gobernado por configuración, para medios, control y distribución; y transporte ZeroMQ con patrón publicador-suscriptor y msgpack para detecciones y alertas. La naturaleza temporal de la fuente, los dominios de reloj y los estados de aplicabilidad forman parte de la validez de cada métrica.

Las extensiones se clasifican por su costo arquitectónico: una condición del mismo tipo se incorpora por configuración; una familia nueva requiere un evaluador; y nuevos modelos, fuentes o canales requieren adaptadores. Esta frontera evita presentar la extensibilidad open-vocabulary como una capacidad ilimitada.

La sección deja preparado el paso a la implementación sin anticipar sus resultados. §17.4 documenta qué componentes se materializaron y cómo se verificaron; §17.5 concentra las mediciones y su interpretación experimental.

El diseño se considera completo cuando cada una de estas decisiones —separación de responsabilidades, estrategia perceptiva, configuración reproducible, contratos versionados, persistencia y transporte diferenciados, temporalidad declarada, alerta interna protegida y extensibilidad delimitada— posee un criterio verificable en la implementación.
