# 96d — Texto extraído del informe v1.1: §16 Marco Teórico

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

## 16. Marco Teórico

El marco teórico concentra los conceptos, categorías normativas y fundamentos técnicos que sostienen el diseño posterior del prototipo. A diferencia del Estado del arte, no funciona como un inventario exhaustivo de modelos o herramientas, sino como base conceptual para justificar qué se detecta, cómo se interpreta, bajo qué restricciones opera el sistema y qué condiciones ético-legales delimitan su uso.


### 16.1. Organización Interna del Marco Teórico

El marco teórico se organiza a partir de los dominios conceptuales que sustentan el diseño y la evaluación de la plataforma experimental. Cada dominio responde a una pregunta central del proyecto y permite delimitar, desde una perspectiva técnica o normativa, las condiciones bajo las cuales resulta posible construir un sistema de detección open-vocabulary aplicado al monitoreo de seguridad en construcción civil.

En primer lugar, se aborda el dominio de aplicación, vinculado con la seguridad laboral en obras y con la identificación de condiciones de riesgo observables mediante análisis visual. Luego se desarrollan los fundamentos de la detección open-vocabulary, el seguimiento multiobjeto, la transmisión de video en tiempo real y las restricciones ético-legales asociadas al uso de sistemas de visión por computadora en contextos laborales. Esta organización permite que las decisiones posteriores de diseño, implementación y evaluación no aparezcan como elecciones aisladas, sino como consecuencia de un conjunto articulado de criterios técnicos, metodológicos y normativos.

La Tabla 9 resume la relación entre cada dominio del marco teórico, la pregunta que orienta su desarrollo y su contribución dentro del proyecto.

Tabla 9

Correspondencia entre dominios del marco teórico, preguntas articuladoras y contribución al proyecto.


| Dominio del marco teórico | Pregunta articuladora | Contribución al proyecto |
| --- | --- | --- |
| Seguridad laboral y condiciones de riesgo observables | ¿Qué condiciones debe poder identificar el sistema? | Define el dominio de aplicación y traduce obligaciones preventivas en evidencias visuales detectables. |
| Detección open-vocabulary y modelos visión-lenguaje | ¿Cómo puede el sistema interpretar descripciones abiertas en lenguaje natural? | Fundamenta el uso de modelos capaces de detectar conceptos no restringidos a un vocabulario cerrado. |
| Seguimiento multiobjeto | ¿Cómo se mantiene la continuidad temporal de las detecciones? | Justifica la incorporación de mecanismos de tracking para reducir inestabilidad frame-to-frame y evaluar persistencia. |
| Video en tiempo real, streaming y latencia | ¿Qué restricciones impone el procesamiento continuo de video? | Delimita los componentes del pipeline, las fuentes de latencia y los criterios para operar en tiempo real. |
| Marco ético-legal y privacidad | ¿Bajo qué condiciones es legítimo aplicar visión computacional en entornos laborales? | Establece límites de uso responsable, minimización de datos, carácter asistivo y ausencia de identificación personal. |
| Convergencias y criterios orientadores | ¿Qué criterios surgen de integrar los dominios anteriores? | Articula brechas, restricciones y criterios que orientan el diseño metodológico y técnico del prototipo. |

El punto de partida del análisis es el dominio de aplicación. Antes de evaluar qué puede detectar el sistema, es necesario precisar qué debe detectar y por qué, definiendo así qué condiciones de riesgo son relevantes en una obra de construcción, qué las hace observables visualmente y qué obligación normativa impone su prevención. Sin esa delimitación, cualquier evaluación del desempeño técnico del sistema carecería de criterio de referencia.


### 16.2. Condiciones de Riesgo Observables

La viabilidad técnica de un sistema de detección visual depende, en primer lugar, de una definición precisa de su objeto: qué condiciones deben ser detectadas, bajo qué criterio se las considera riesgosas y por qué son observables mediante visión por computadora. En el contexto de la construcción civil, esa definición no es arbitraria. Emerge de un marco normativo consolidado que establece, con carácter obligatorio, cuáles son las obligaciones del empleador en materia de prevención y qué condiciones físicas en la obra constituyen incumplimiento de esas obligaciones. Las siguientes secciones sistematizan ese marco y lo traducen al plano de los observables visuales que el sistema deberá identificar.

El sector de la construcción combina tareas simultáneas, entornos cambiantes y una elevada interacción entre personas, maquinaria y estructuras temporales. En este contexto, la regulación en materia de seguridad y salud en el trabajo cumple un rol ordenatorio: define obligaciones mínimas y mecanismos de control que orientan la prevención, y establece un lenguaje común para evaluar condiciones de riesgo.

Para un proyecto que analiza video en obra y emite alertas asistivas, la normativa no debe interpretarse como una lista de verificación aislada, sino como el fundamento que permite traducir riesgos típicos (por ejemplo, trabajo en altura sin protección colectiva o sin anclaje, presencia de personas en zonas de exclusión de equipos móviles o izajes, o interacción peatón-vehículo fuera de circuitos señalizados) en criterios observables y verificables. Esta sección desarrolla el marco normativo argentino aplicable y propone una articulación conceptual entre las obligaciones legales y las evidencias susceptibles de detección automatizada.


#### 16.2.1. La Normativa como Fuente de Condiciones de Riesgo

La seguridad laboral en la industria de la construcción civil se organiza a partir de un conjunto de instrumentos normativos que prescriben obligaciones concretas para empleadores, trabajadores y empresas. Una distinción metodológica relevante separa la normativa de cumplimiento obligatorio —leyes, decretos reglamentarios y resoluciones técnicas con fuerza vinculante— de los estándares voluntarios de gestión, que no generan exigibilidad legal por sí mismos, pero aportan marcos conceptuales útiles para organizar la prevención de manera sistemática. Ambos tipos de instrumentos resultan pertinentes para este análisis, siendo la normativa obligatoria la que define qué condiciones deben cumplirse y en consecuencia qué incumplimientos constituyen riesgo, y los estándares de gestión, en cambio, ofrecen un marco para comprender cómo se monitorea y verifica ese cumplimiento en la práctica operativa.


##### 16.2.1.1. Normativa de Cumplimiento Obligatorio

En Argentina, el sistema normativo de higiene y seguridad laboral se estructura jerárquicamente a partir de la Ley 19.587, reglamentada con carácter general por el Decreto 351/79 y con especificidad sectorial por el Decreto 911/96 para la industria de la construcción. Este cuerpo normativo se complementa con resoluciones técnicas emitidas por la Superintendencia de Riesgos del Trabajo, que operacionalizan los mecanismos de control y coordinación preventiva.


##### 16.2.1.2. Ley 19.587 y el Principio de Prevención

La Ley 19.587 de Higiene y Seguridad en el Trabajo establece el marco general aplicable a todo el territorio nacional y fija como eje conceptual el principio de prevención: las condiciones laborales deben ajustarse a normas técnicas destinadas a prevenir daños a la salud y a la integridad de las personas (Ley 19.587, 1972). Su alcance no se limita a un sector específico, sino que delimita obligaciones generales vinculadas al ambiente de trabajo, las instalaciones, los procesos productivos y la organización preventiva.

La contribución conceptual de esta ley para el presente análisis reside en instalar el deber de anticipación como componente central de la gestión de seguridad. La prevención no se concibe como respuesta reactiva a incidentes, sino como identificación y control sistemático de condiciones que preceden al daño. En una obra civil, por ejemplo, donde el riesgo se reconfigura constantemente con el avance de los trabajos, este principio implica que el sistema de monitoreo debe orientarse a detectar condiciones de riesgo antes de que se materialicen en accidentes, y no únicamente a registrar eventos ya ocurridos.


##### 16.2.1.3. Decreto 351/79: Reglamentación General

El Decreto 351/79 aprueba la reglamentación de la Ley 19.587 y desarrolla un conjunto de exigencias técnicas que permiten trasladar el deber general de prevención a requisitos operativos verificables (Decreto 351/79, 1979). Organiza aspectos como condiciones edilicias, instalaciones, señalización, iluminación, ventilación, protecciones de máquinas, orden y limpieza, y la estructuración de servicios especializados en higiene y seguridad.

El aporte conceptual de este decreto para el análisis es la noción de condición controlable, ya que muchos riesgos se expresan como estados observables del entorno —ausencia de resguardos, obstrucciones en vías de circulación, falta de señalización, desorden en zonas de trabajo—, lo que habilita estrategias de verificación sistemática basadas en la observación del espacio físico. El decreto consolida la idea de que la seguridad puede monitorearse a partir de indicadores verificables en el lugar de trabajo, idea que resulta directamente relevante para un sistema de monitoreo visual.


##### 16.2.1.4. Decreto 911/96: Reglamento Específico de Construcción

El Decreto 911/96 aprueba el Reglamento de Higiene y Seguridad específico para la industria de la construcción, atendiendo a particularidades que distinguen a este sector de otros entornos laborales, definiendo cuestiones del contexto de la obra como establecimiento temporal con geometría cambiante, la coexistencia simultánea de múltiples contratistas y subcontratistas, la presencia de estructuras provisorias en permanente transformación, y la exposición a riesgos que varían día a día con el avance de los trabajos (Decreto 911/96, 1996).

Este reglamento aborda de manera específica los riesgos más frecuentes y graves de la actividad: trabajos en altura con andamios y plataformas, excavaciones, instalaciones eléctricas provisorias, movimiento de materiales y operación de equipos pesados. Su contribución conceptual es doble. Por un lado, explicita que el riesgo en construcción no depende únicamente del comportamiento individual del trabajador, sino también del diseño del entorno físico —protecciones colectivas, delimitación de áreas, condiciones de acceso y circulación—. Por otro lado, vincula la seguridad a la gestión integral de la obra como sistema, donde la coordinación entre empleadores concurrentes y la planificación preventiva son tan relevantes como las medidas individuales de protección.


##### 16.2.1.5. Resoluciones SRT: Programas y Coordinación Preventiva

La Resolución SRT 51/97 y la Resolución SRT 35/98 completan el marco normativo estableciendo la dimensión organizacional de la prevención. La primera fija la obligación de comunicar el inicio de obra y de elaborar programas de seguridad específicos para cada proyecto, con intervención verificadora de las ART mediante visitas sistemáticas (SRT, 1997). La segunda regula los casos de concurrencia de múltiples empleadores imponiendo la coordinación de esos programas y su verificación conjunta (SRT, 1998).

En el ámbito de la construcción, el cumplimiento normativo se articula con instrumentos operativos impulsados por la Superintendencia de Riesgos del Trabajo (SRT) y por las Aseguradoras de Riesgos del Trabajo (ART). De forma complementaria, el Programa de Construcción difundido por la SRT explicita como objetivo el establecimiento de mecanismos de adopción de medidas preventivas, correctivas y de control, incluyendo la verificación de avisos de obra y la coordinación de programas (SRT, s/f).

Estas resoluciones refuerzan la concepción de la prevención como proceso continuo y organizado, no como conjunto de medidas puntuales. En este contexto, su relevancia conceptual reside en que sitúan la detección de condiciones de riesgo en un marco institucional más amplio, dado que las alertas generadas por un sistema de monitoreo asistivo no son decisiones autónomas, sino insumos para los mecanismos de supervisión humana y gestión preventiva previstos por la normativa vigente.


##### 16.2.1.6. Estándares Voluntarios de Gestión

Los estándares internacionales de gestión constituyen herramientas complementarias al marco legal. Si bien su adopción no es obligatoria, proporcionan estructuras sistemáticas para organizar la prevención de riesgos en torno a procesos definidos, responsabilidades asignadas y ciclos de mejora continua. En proyectos que integran tecnología al monitoreo de seguridad, estos estándares ofrecen un marco conceptual para situar las herramientas dentro de un sistema de gestión más amplio.


##### 16.2.1.7. ISO 45001 y Sistemas de Gestión de SST

La norma ISO 45001:2018 constituye el estándar internacional de referencia para sistemas de gestión de seguridad y salud en el trabajo. Si bien su adopción no es obligatoria bajo la normativa argentina, su marco conceptual resulta relevante para comprender cómo se organiza la prevención como sistema gestionable y auditable (ISO, 2018). El estándar integra identificación de peligros, evaluación de riesgos, control operacional, preparación ante emergencias y revisión del desempeño mediante auditorías y acciones correctivas, todo ello estructurado en el ciclo Planificar-Hacer-Verificar-Actuar (PDCA).

Su valor para el presente análisis reside en que convierte el cumplimiento normativo en una práctica gestionable y verificable: la organización no solo debe cumplir las obligaciones legales, sino demostrar que identifica peligros, implementa controles, verifica resultados y mejora sistemáticamente. Esta perspectiva permite ubicar un sistema de monitoreo asistivo como componente de un sistema de gestión más amplio, evitando interpretarlo como sustituto de la supervisión humana o del control institucional. Las alertas generadas por el sistema son insumos para ese ciclo de gestión, no reemplazos de ninguna de sus etapas.


#### 16.2.2. Operacionalización: Prescripción Normativa y Observable Visual

El propósito de las secciones anteriores fue establecer el marco legal y conceptual que define qué condiciones deben cumplirse en una obra civil. Sin embargo, para que este marco resulte operativo en un sistema de monitoreo visual, es necesario traducir las obligaciones normativas a condiciones físicamente observables que puedan ser identificadas en imágenes o video. Este proceso constituye lo que en metodología de investigación se denomina operacionalización, es decir, el proceso de traducción de un concepto abstracto o normativo en indicadores concretos y verificables (Decreto 351/79, 1979; Decreto 911/96, 1996).

La operacionalización aplicada en este capítulo parte de las obligaciones tipificadas en el marco normativo y las transforma en evidencias visuales que manifiestan, de manera observable, el cumplimiento o incumplimiento de cada obligación. Una prescripción como “el empleador debe proveer elementos de protección personal adecuados” (Ley 19.587, 1972) se traduce, por ejemplo, en la evidencia observable “presencia de casco en la región cefálica del trabajador”. Esta traducción no implica equiparar la observación visual con la certificación del cumplimiento normativo —una cuestión que requiere evaluación técnica en terreno y decisión humana—, sino construir un conjunto de señales de atención alineadas con categorías regulatorias reconocidas, que un sistema asistivo puede detectar y reportar para su posterior evaluación por los responsables.

Es importante señalar que esta operacionalización tiene limitaciones inherentes. La visión por computadora captura información visual bidimensional proyectada desde ángulos específicos, lo que puede generar ambigüedades de interpretación. Por ejemplo, un casco que en realidad está siendo transportado en la mano puede proyectarse de manera similar a uno que está siendo usado correctamente desde ciertos ángulos de cámara. Estas ambigüedades no invalidan el valor asistivo del sistema, pero refuerzan la necesidad de que las alertas generadas sean interpretadas por supervisores humanos con capacidad de contextualización, y no como determinaciones definitivas de cumplimiento o incumplimiento normativo.


##### 16.2.2.1. Taxonomía de Categorías de Riesgo

Para que la operacionalización sea sistemática y trazable al marco normativo, es necesario organizar el análisis en categorías de riesgo que agrupen obligaciones de naturaleza similar. En la construcción civil, las categorías de riesgo más relevantes para este proyecto son aquellas que combinan tres condiciones: presencia normativa, criticidad preventiva y posibilidad de observación visual.

Bajo ese criterio, se consideran principalmente las siguientes categorías: incumplimiento en el uso de equipos de protección personal (EPP), condiciones inseguras en trabajos en altura, acceso no autorizado o desprotegido a zonas restringidas, coexistencia riesgosa entre peatones y maquinaria, y condiciones inadecuadas del entorno físico de trabajo, como desorden, obstrucciones, instalaciones provisorias o ausencia de señalización.

Esta taxonomía no pretende agotar el universo de riesgos en obra. Su función es construir un puente entre obligaciones legales y evidencias verificables en video, de modo que las condiciones priorizadas puedan justificarse tanto desde el marco normativo como desde su factibilidad técnica de detección visual.


##### 16.2.2.2. Matriz de Evidencias Visuales

La Tabla 10 presenta la operacionalización del marco normativo en términos de evidencias visuales y condiciones detectables en video. Cada fila articula una obligación normativa tipificada, la evidencia física que la materializa, y la condición de riesgo observable que correspondería a su incumplimiento o ausencia. Esta tabla constituye el artefacto analítico central de este capítulo y funciona como insumo conceptual para las etapas posteriores del proyecto en las que se definirán los patrones de consulta del sistema.

Tabla 10

Correspondencia entre obligaciones normativas, evidencias visuales y condiciones de riesgo detectables en video


| Categoría de riesgo | Prescripción normativa | Evidencia operativa / visual | Condición detectable en video |
| --- | --- | --- | --- |
| Uso de EPP — casco | Ley 19.587, arts. 8-9; Dec. 911/96, arts. 98-115 | Casco de seguridad en región cefálica | Persona sin casco; persona en borde elevado sin protección cefálica visible |
| Uso de EPP — chaleco reflectivo | Ley 19.587, arts. 8-9; Dec. 911/96, arts. 98-115 | Chaleco de alta visibilidad en torso | Persona sin chaleco reflectivo en zona de tráfico o maquinaria |
| Uso de EPP — calzado de seguridad | Ley 19.587, arts. 8-9; Dec. 911/96, arts. 98-115 | Calzado con puntera reforzada o bota de seguridad | Persona con calzado inadecuado visible en zonas de riesgo de aplastamiento |
| Protección contra caídas en altura | Ley 19.587, arts. 8-9; Dec. 911/96, arts. 52-57, 98-115 | Arnés con línea de vida; barandas, redes y protecciones perimetrales | Trabajo en altura sin sistema anticaídas visible; borde desprotegido con personas próximas |
| Delimitación de áreas de riesgo | Dec. 351/79, cap. 12; Dec. 911/96, arts. 47, 61-62, 66-69 | Cintas, vallados, cartelería, zonas restringidas demarcadas | Persona dentro de zona restringida; cruce peligroso peatón-maquinaria; ausencia de segregación visible |
| Control de circulación y coexistencia con maquinaria | Dec. 911/96, arts. 47, 70-71 | Rutas separadas, balizamiento, señalero presente | Maquinaria circulando cerca de peatones; ausencia de separación; maniobras en zonas congestionadas |
| Orden, limpieza y gestión de obstáculos | Dec. 351/79, cap. 5; Dec. 911/96, arts. 46-47 | Superficies libres; materiales apilados; escombros contenidos | Pasillos obstruidos; materiales inestables; riesgo de tropiezo por desorden visible |
| Instalaciones eléctricas provisorias | Dec. 911/96, arts. 74-87 | Tableros protegidos; cables con doble aislación; disyuntores | Cableado expuesto en zonas de tránsito; conexiones improvisadas visibles |

Nota. La columna “Condición detectable en video” describe situaciones susceptibles de ser identificadas por análisis visual, no determinaciones de cumplimiento normativo. La tabla no constituye selección de prompts ni especificación de sistema; es un artefacto analítico conceptual cuya elaboración es independiente de la tecnología de detección que se adopte en etapas posteriores. Fuente: Elaboración propia basada en las fuentes citadas (Decreto 351/79, 1979; Decreto 911/96, 1996; Ley 19.587, 1972).

Para que las evidencias visuales sistematizadas en la tabla precedente resulten operativas en el contexto del sistema propuesto, es necesario establecer criterios de evaluabilidad que permitan valorar su detección de manera objetiva y reproducible. En este sentido, cada condición observable debe poder vincularse a métricas de desempeño del modelo —tales como precisión, exhaustividad (recall) y tasa de falsos positivos— así como a indicadores de rendimiento en tiempo real, entre los que se incluyen la latencia de inferencia y la tasa de cuadros procesados por segundo. Esta formalización permite no solo validar el comportamiento del sistema en escenarios controlados, sino también comparar configuraciones y arquitecturas de detección alternativas, asegurando coherencia con el marco de evaluación definido para el proyecto. Cabe señalar que los umbrales específicos y las expresiones formales de estos criterios constituyen decisiones de implementación que se abordarán en etapas posteriores del trabajo.


#### 16.2.3. Integración con Sistemas de Monitoreo Asistivo

De las secciones anteriores, es posible apreciar que el marco normativo de la construcción civil genera un conjunto definido y justificado de condiciones de riesgo que son, en principio, observables en el espacio físico de la obra. Esta observabilidad no es un hallazgo trivial, sino que implica la existencia de una correspondencia estructural entre las obligaciones legales y las señales visuales que un sistema de monitoreo puede capturar, lo que fundamenta la viabilidad conceptual del proyecto como herramienta de apoyo a la prevención.

Sin embargo, esta correspondencia tiene límites que deben quedar explícitos. En primer lugar, no todas las obligaciones normativas tienen correlatos visuales directos. Por ejemplo, prescripciones como la correcta certificación de los EPP según norma IRAM, el ajuste técnico de un arnés o la altura reglamentaria de una baranda son condiciones que, aun manifestándose en el espacio físico, no pueden determinarse con certeza a partir de la imagen. El sistema puede señalar la presencia o ausencia de un elemento, pero no verificar su conformidad técnica. En segundo lugar, la observabilidad visual de una condición no garantiza que el sistema la detecte con precisión en todas las circunstancias, ya que elementos como la iluminación, los ángulos de cámara y las oclusiones introducen variabilidad que el análisis conceptual no puede anticipar completamente.

La integración de estas condiciones en un sistema de este tipo tiene coherencia con el enfoque de la normativa vigente, que concibe la prevención como un proceso continuo de verificación y corrección (ISO, 2018; SRT, 1997, 1998). Un sistema que detecta señales de riesgo a modo de asistencia puede contribuir a sostener la continuidad del control en entornos con múltiples frentes de trabajo simultáneos, complementando la capacidad de observación de los supervisores humanos sin desplazar sus responsabilidades legales ni sustituir los mecanismos institucionales de fiscalización.

Desde la perspectiva del diseño de sistemas, esta integración puede modelarse mediante una arquitectura orientada a eventos (event-driven architecture, EDA), en la cual cada evidencia visual detectada se materializa como un evento estructurado —por ejemplo, persona_sin_casco_detectada— que es publicado por el módulo de análisis de video y consumido por componentes especializados en evaluación de patrones, generación de alertas y registro de trazabilidad. Esta aproximación desacopla la etapa de detección del procesamiento posterior, lo que facilita la escalabilidad del sistema y permite enrutar los eventos de manera diferenciada —por ejemplo, hacia registros de auditoría, notificaciones en tiempo real o módulos de análisis retrospectivo— sin modificar la lógica de detección subyacente. De este modo, la detección visual constituye la fuente primaria de eventos dentro del plano de control del sistema, operando como insumo base que puede enriquecerse mediante reglas configurables o procesamiento paralelo en etapas subsiguientes del flujo.

Esta lectura es coherente con el enfoque de las resoluciones de la SRT relativas a programas de seguridad, coordinación entre empleadores y verificación en obra, que conciben la prevención como un proceso continuo y organizado (SRT, 1997, 1998). La tecnología no sustituye la evaluación técnica en terreno ni el rol de las ART o de los responsables de seguridad, sino que puede integrarse como un soporte instrumental para fortalecer la detección, la trazabilidad y la respuesta ante condiciones de riesgo observables.


### 16.3. Percepción Visión-Lenguaje: Fundamentos conceptuales de la Detección Open-Vocabulary

Como se mencionó anteriormente, la detección de objetos en imágenes ha sido históricamente un problema de clasificación cerrada, donde los sistemas reconocen únicamente las categorías para las que fueron entrenados. Este supuesto es incompatible con el dominio de seguridad laboral, donde las condiciones de riesgo son heterogéneas, cambian según la etapa de la obra y pueden formularse con precisión en lenguaje natural pero difícilmente acotarse en un conjunto fijo de clases predefinidas. El paradigma de detección de vocabulario abierto (OVD) rompe esa restricción al incorporar un encoder de lenguaje que permite guiar la detección mediante descripciones textuales arbitrarias.

La presente sección caracteriza los fundamentos conceptuales de la detección open-vocabulary, con énfasis en la transición desde los enfoques de vocabulario cerrado hacia modelos capaces de vincular información visual y lenguaje natural. En particular, se desarrollan los principios de alineación visión-lenguaje, el rol del prompt como mecanismo de especificación dinámica y las condiciones que hacen posible formular consultas abiertas sobre escenas visuales.


#### 16.3.1. Del Closed-Set al Open-Vocabulary

En la detección de objetos tradicional, el modelo aprende a localizar instancias en una imagen y a clasificarlas dentro de un vocabulario fijo, establecido de antemano y sin posibilidad de expansión en tiempo de inferencia. Esta formulación permite optimizar el rendimiento sobre benchmarks bien delimitados, como MS COCO con 80 categorías (Lin et al., 2015) o PASCAL VOC (Everingham et al., 2010), pero introduce una dependencia estructural entre el dominio de entrenamiento y el dominio de aplicación, siendo que el sistema solo puede detectar lo que fue explícitamente contemplado en el diseño.

La detección open-vocabulary supera esta restricción al separar el espacio semántico del conjunto de categorías de entrenamiento. En lugar de aprender representaciones para clases discretas y fijas, los modelos OVD aprenden a alinear regiones visuales con descripciones lingüísticas en un espacio de embeddings compartido. La noción de clase deja de ser un identificador discreto y pasa a representarse como una entidad semántica continua, definida dinámicamente por el contenido de la consulta (Zareian et al., 2021). En consecuencia, una categoría expresada en lenguaje natural durante la inferencia puede ser reconocida aunque el modelo nunca la haya visto etiquetada durante el entrenamiento, siempre que su representación semántica sea coherente con el espacio aprendido.

Esta capacidad no es absoluta. La calidad de la generalización zero-shot —ampliada en la sección 16.3.4— depende de la calidad y amplitud del preentrenamiento multimodal, y el desempeño sobre categorías muy específicas o visualmente inusuales puede ser significativamente inferior al observado sobre categorías cotidianas bien representadas en los datos de entrenamiento. Reconocer la potencia del paradigma OVD sin ignorar sus condiciones y límites es el propósito de las secciones que siguen.


#### 16.3.2. Mecanismos de Alineación Visión-Lenguaje

El pilar técnico central de OVD es el uso de representaciones conjuntas de visión y lenguaje. Estas representaciones se obtienen mediante modelos multimodales entrenados para proyectar imágenes, regiones visuales y textos en un espacio latente compartido, donde la proximidad geométrica refleja afinidad semántica. El trabajo seminal en esta dirección es CLIP (Contrastive Language–Image Pre-training), que demostró la viabilidad de entrenar modelos con cientos de millones de pares imagen-texto recopilados de la web para aprender representaciones visuales altamente transferibles, alineadas con descripciones en lenguaje natural (Radford et al., 2021).

El entrenamiento contrastivo opera sobre la base de maximizar la compatibilidad entre pares imagen-texto correctos y minimizar entre pares incorrectos, produciendo un encoder visual y un encoder textual que proyectan imagen y texto a un espacio semántico compartido (Minderer et al., 2022; Radford et al., 2021). El proceso de detección resultante puede describirse en tres etapas conceptuales, donde 1) a partir de una imagen, el backbone visual genera representaciones asociadas a regiones candidatas, 2) a partir de una consulta textual (prompt), el encoder de lenguaje obtiene una representación semántica y finalmente, 3) la detección se resuelve evaluando la compatibilidad entre ambas representaciones mediante funciones de similitud, atención cruzada u otros mecanismos de alineación, aplicando non-maximum suppression sobre las regiones con mayor compatibilidad semántica. Este esquema introduce una separación conceptual entre localización espacial y reconocimiento semántico, lo que permite evaluar nuevas descripciones en tiempo de inferencia sin modificar los parámetros del modelo (Minderer et al., 2022).


#### 16.3.3. Rol del Lenguaje Natural como Especificación Dinámica

En los enfoques OVD, el lenguaje natural actúa como un mecanismo de especificación dinámica del objetivo de detección. A diferencia de los detectores cerrados, donde cada clase se asocia a un vector de clasificación aprendido, en OVD el texto define el criterio semántico de forma flexible y contextual. Esta flexibilidad tiene implicaciones directas para el dominio de seguridad laboral: condiciones de riesgo como “persona sin casco”, “trabajador en zona restringida sin señalero visible” o “maquinaria operando en pasillo peatonal” son enunciados naturales para un supervisor humano y pueden ser formulados directamente como prompts de consulta al sistema, sin requerir que esas categorías hayan sido anticipadas en el diseño.

Sin embargo, el lenguaje natural introduce también una fuente de variabilidad que no existe en los sistemas closed-set, siendo esta la sensibilidad a la formulación exacta de la consulta. Investigaciones en modelos visión-lenguaje han demostrado que pequeños cambios en la redacción de las consultas pueden producir diferencias significativas en el desempeño, incluso cuando diferentes formulaciones refieren al mismo concepto subyacente (Zhou et al., 2022a). Esta observación motivó el desarrollo de técnicas de prompt learning, donde los tokens de contexto se reemplazan por vectores aprendibles optimizados con datos del dominio objetivo (Khattak et al., 2023; Zhou et al., 2022b). Adicionalmente, algunos modelos recientes soportan prompts visuales que permiten anclar la detección a ejemplos concretos en lugar de depender exclusivamente de descripciones textuales, ampliando la expresividad del mecanismo de consulta (Jiang et al., 2024).

La implicación práctica para el proyecto es que el diseño de los prompts de consulta no es un paso trivial ni secundario, más bien es una decisión de ingeniería que afecta directamente el desempeño del sistema.

Un desafío documentado en la literatura es la sensibilidad de los modelos visión-lenguaje a variaciones aparentemente menores en la formulación de las consultas. (Zhou et al., 2021) identificaron que pequeños cambios en la redacción pueden producir diferencias significativas en el desempeño, lo que convierte al diseño de prompts en una tarea que requiere experimentación iterativa. Esta observación motivó el desarrollo de técnicas de prompt learning, donde los tokens de contexto se reemplazan por vectores aprendibles que se optimizan con datos etiquetados del dominio objetivo (Zhou et al., 2021; Khattak et al., 2023). Tales enfoques han demostrado mejoras sustanciales respecto a los prompts diseñados manualmente, aunque introducen requisitos adicionales de datos y entrenamiento.

Desde una perspectiva complementaria, el prompt engineering manual —entendido como el diseño deliberado de plantillas y formulaciones textuales— permanece relevante en escenarios donde el ajuste fino no es viable o donde se requiere máxima flexibilidad para consultas ad-hoc. En el contexto específico de la detección open-vocabulary, se demostró que la optimización automática de representaciones de prompts —específicamente diseñada para tareas de detección— supera consistentemente a los prompts elaborados mediante ingeniería manual, evidenciando que las estrategias de formulación desarrolladas para clasificación de imágenes no se transfieren directamente al dominio de la detección de objetos (Du et al., 2022). Estos hallazgos sugieren que la efectividad de una consulta depende no solo de su contenido semántico, sino también de su estructura sintáctica y su alineación con los patrones lingüísticos presentes en el corpus de preentrenamiento del modelo (Gu et al., 2021).

En consecuencia, el desempeño del sistema no depende únicamente de la calidad de las características visuales, sino también de la capacidad del modelo para interpretar correctamente el contenido semántico de consultas formuladas con terminología de dominio. Esta intersección entre lenguaje técnico y representación visual constituye un área de investigación activa con implicancias directas para la aplicabilidad de los modelos OVD en entornos industriales.


#### 16.3.4. Generalización Zero-Shot y el Problema del Long-Tail Semántico

Un concepto estrechamente vinculado a la OVD es la generalización zero-shot, siendo esta la capacidad de reconocer conceptos no observados explícitamente durante el entrenamiento supervisado. Esta propiedad resulta especialmente relevante en dominios caracterizados por distribuciones de clases desbalanceadas o por una fuerte presencia de categorías poco frecuentes, denominadas en la literatura como long-tail semántico.

Los modelos OVD no eliminan por completo las limitaciones impuestas por los datos de preentrenamiento: categorías visualmente inusuales o semánticamente distantes de los conceptos bien representados en los datos de preentrenamiento pueden exhibir un desempeño notablemente inferior al observado en las categorías frecuentes. Para el dominio de construcción civil, esto implica que categorías como “arnés de seguridad”, “chaleco reflectivo” o “señalero” —que son relevantes operativamente pero no son objetos cotidianos frecuentes en los datasets de preentrenamiento— pueden presentar un desempeño inferior al esperado en condiciones zero-shot puras.


#### 16.3.5. Criterios Orientadores para la Selección de Modelos OVD

El análisis del estado del arte realizado en las secciones precedentes permite identificar un conjunto de criterios técnicos que deberán orientar la selección de modelos de detección open-vocabulary en etapas posteriores del proyecto. Estos criterios emergen de la intersección entre las características observadas en los modelos representativos, los trade-offs documentados en la literatura y los requisitos específicos de una implementación concreta orientada al análisis de video en tiempo real.


##### 16.3.5.1. Criterios derivados del análisis teórico

A partir de la revisión bibliográfica y la comparativa sistemática, se identifican seis ejes de evaluación relevantes para la selección futura de modelos OVD en el contexto de sistemas de vídeo en tiempo real.

Capacidad de inferencia en tiempo real. El modelo debe sostener tasas de procesamiento compatibles con flujos de video en vivo, típicamente en el orden de 20-30 FPS o superiores según los requisitos operativos del sistema. Este criterio implica evaluar no solo la latencia de inferencia aislada, sino también el overhead introducido por la fusión visión-lenguaje y la viabilidad de optimización mediante frameworks de aceleración como TensorRT (Zhao et al., 2024; Ren et al., 2024a). La comparativa sistemática evidencia que los modelos con fusión multimodal profunda tienden a presentar mayores latencias que aquellos basados en arquitecturas one-stage o con mecanismos de reparametrización (Wang et al., 2025; Cheng et al., 2024).

Generalización semántica open-set. El modelo debe demostrar capacidad efectiva para detectar conceptos no observados explícitamente durante el entrenamiento supervisado, respondiendo a consultas textuales arbitrarias sin degradación significativa del rendimiento. Este criterio resulta central para aplicaciones donde el vocabulario de interés puede variar dinámicamente según las necesidades del usuario (Zareian et al., 2021). La evaluación en benchmarks con distribución long-tail como LVIS (Gupta et al., 2019) proporciona indicadores relevantes de esta capacidad, particularmente el rendimiento en categorías raras no vistas durante el entrenamiento (Liu et al., 2023).

Compatibilidad con procesamiento de video. A diferencia de la detección sobre imágenes estáticas, el análisis de video introduce requisitos adicionales de estabilidad temporal y eficiencia sostenida. Resultan preferibles arquitecturas que soporten mecanismos de reutilización de embeddings textuales entre cuadros consecutivos, reduciendo el costo computacional cuando el vocabulario de consulta permanece constante durante intervalos prolongados (Zhao et al., 2024). Esta consideración adquiere relevancia particular en escenarios de monitoreo continuo donde el conjunto de clases de interés se define al inicio de la sesión y se mantiene estable a lo largo del flujo de video.

Desacoplamiento arquitectónico. El modelo de detección debe integrarse de forma modular con componentes de seguimiento temporal y, eventualmente, segmentación de instancias, sin introducir dependencias rígidas que dificulten la sustitución o actualización de módulos individuales. Este criterio favorece arquitecturas que exponen interfaces claras entre etapas del pipeline, facilitando la experimentación y evolución incremental del sistema (Ren et al., 2024c). La literatura reciente muestra que los enfoques de pipeline —donde un detector OVD se combina con segmentadores o trackers independientes— ofrecen mayor flexibilidad que las arquitecturas monolíticas end-to-end (Li et al., 2023).

Independencia de entrenamiento específico por dominio. Para maximizar la generalidad y reproducibilidad del prototipo experimental, resultan preferibles modelos que operen de manera efectiva con pesos preentrenados, sin requerir fine-tuning extensivo sobre datasets del dominio de aplicación. No obstante, debe considerarse que cierto grado de adaptación o calibración puede resultar necesario para optimizar el rendimiento en condiciones visuales específicas, dado que los benchmarks estándar como MS COCO o LVIS no capturan plenamente la complejidad de dominios especializados (Lin et al., 2014; Gupta et al., 2019). En este contexto, la evidencia analizada en la sección 15.2.4.5 muestra que la capacidad de una arquitectura para preservar su generalización open-vocabulary durante el fine-tuning varía sustancialmente entre familias de modelos. Los detectores con fusión visión-lenguaje profunda y no removible exhiben mayor resiliencia frente al ajuste de dominio, mientras que aquellos con módulos de texto reparametrizables o desacoplables tienden a converger hacia un comportamiento closed-set bajo las configuraciones estándar de fine-tuning (Cheng et al., 2024; X. Zhao et al., 2024). Este criterio implica, por tanto, evaluar no solo el rendimiento zero-shot del modelo, sino también su perfil de adaptabilidad, entendido como la viabilidad de mejorar el rendimiento en categorías del dominio sin degradar la capacidad de responder a consultas semánticas arbitrarias.

Soporte para prompts multimodales. El modelo debe permitir la especificación del objetivo de detección no solo mediante descripciones textuales, sino también a través de ejemplos visuales de referencia (visual prompts). Esta capacidad resulta relevante en escenarios donde la descripción textual de un objeto, condición o patrón de riesgo puede ser ambigua, incompleta o dependiente del contexto, permitiendo al operador anclar la detección a una instancia visual concreta. Desde el punto de vista del sistema, el soporte para prompts multimodales amplía la expresividad del mecanismo de consulta y mejora la usabilidad en entornos operativos complejos (Jiang et al., 2024; Ren et al., 2024b).


##### 16.3.5.2. Consideraciones complementarias

Además de los criterios primarios, el análisis identifica factores adicionales que pueden incidir en la evaluación según el contexto específico de implementación:

Balance entre precisión y velocidad. La comparativa sistemática evidencia una tensión inherente entre modelos que priorizan la máxima precisión zero-shot —alcanzando valores superiores a 55 AP en LVIS— y aquellos optimizados para baja latencia —con inferencias inferiores a 10 ms (Ren et al., 2024b; Zhao et al., 2024). La selección deberá ponderar este trade-off en función de los requisitos operativos concretos, considerando que ambos extremos del espectro pueden resultar relevantes para diferentes configuraciones del sistema.

Capacidad de extensión hacia segmentación. Algunos modelos OVD presentan variantes o extensiones que incorporan segmentación de instancias con overhead reducido (Wang et al., 2025; Ren et al., 2024c). Esta capacidad, aunque no constituye un requisito primario para el prototipo inicial, puede resultar valiosa para escenarios donde la localización precisa de contornos aporte información relevante para la evaluación de condiciones de riesgo.

Implicancias para etapas posteriores. Los criterios enunciados no determinan una selección única, sino que definen un espacio de soluciones factibles dentro del cual deberán evaluarse alternativas concretas durante las etapas de diseño arquitectónico e implementación. El análisis teórico sugiere que tanto los detectores basados en arquitecturas Transformer con fusión eficiente como los detectores one-stage con mecanismos de reparametrización presentan, en principio, perfiles compatibles con los requisitos identificados, aunque con diferentes compromisos entre generalización semántica y eficiencia computacional.

La tensión entre modelos de alta precisión open-set y modelos orientados a tiempo real no debe interpretarse como una dicotomía excluyente. Configuraciones híbridas —donde diferentes modelos se ejecutan según la complejidad de la consulta o el contexto operativo— emergen como alternativas viables que permiten aprovechar las fortalezas de cada enfoque sin comprometer los requisitos críticos del sistema.

La decisión final deberá considerar además factores prácticos —disponibilidad de implementaciones optimizadas, compatibilidad con el stack tecnológico seleccionado, requisitos de hardware y resultados de pruebas preliminares en el dominio de aplicación— que exceden el alcance de la fundamentación teórica y serán abordados en la etapa 2 (análisis metodológico) y etapa 3 (diseño arquitectónico) del proyecto.


### 16.4. Persistencia Temporal de Entidades y Fundamentos Conceptuales del Seguimiento Multi-Objeto

Una detección que no persiste no puede ser la base de una alerta. Para que el sistema distinga entre una persona que cruza brevemente una zona restringida y una que permanece en ella, necesita algo que la detección por fotograma no provee: identidad estable a lo largo del tiempo. El seguimiento multi-objeto (MOT) es el mecanismo que cumple esa función. Asigna a cada entidad detectada un identificador persistente, modela su trayectoria cuadro a cuadro y mantiene esa continuidad incluso cuando el detector falla en algún fotograma puntual. El presente capítulo caracteriza los fundamentos técnicos de ese mecanismo, sus métodos representativos y los trade-offs relevantes para su integración en el sistema E-OVRT-VDP.


#### 16.4.1. La Limitación Temporal de la Detección por Fotograma

Un detector de objetos —incluyendo los modelos OVD— opera de manera fundamentalmente estática: dada una imagen, produce un conjunto de regiones detectadas con sus etiquetas semánticas y puntajes de confianza. Esta operación se realiza de manera independiente para cada fotograma del flujo de video, sin memoria ni referencia a los cuadros anteriores. En consecuencia, el mismo objeto físico presente en dos cuadros consecutivos es tratado como dos entidades sin relación; no existe ningún mecanismo que les asigne una identidad común ni que modele su trayectoria a lo largo del tiempo (Bewley et al., 2016; Luo et al., 2021).

Esta limitación tiene consecuencias operativas directas para el sistema de monitoreo. En primer lugar, la variabilidad frame-a-frame que caracteriza a los modelos OVD —fluctuaciones en puntajes de confianza, apariciones y desapariciones espurias de detecciones, inconsistencias en la asignación de etiquetas entre cuadros consecutivos (Xiao et al., 2023)— no puede filtrarse ni estabilizarse sin una capa que integre información temporal. En segundo lugar, muchas condiciones de riesgo relevantes para la seguridad en construcción no son eventos instantáneos, sino estados que deben persistir durante un intervalo mínimo para ser considerados operativamente significativos: una persona dentro de una zona restringida durante tres segundos representa un riesgo cualitativamente diferente a una detección espuria de un único cuadro (Du et al., 2024). En tercer lugar, la generación de alertas basadas en comportamientos sostenidos —y no en detecciones aisladas— es una condición necesaria para mantener la carga cognitiva de los supervisores en niveles manejables, evitando la fatiga de alerta por falsos positivos frecuentes (Du et al., 2024).

El seguimiento multi-objeto provee exactamente la capa de integración temporal que la detección por fotograma no puede ofrecer: asigna identidades persistentes a las entidades detectadas, modela su estado y trayectoria a lo largo del tiempo, y produce como salida trayectorias estructuradas que permiten razonar sobre el comportamiento de las entidades en el dominio temporal (Du et al., 2024; Milan et al., 2016).


#### 16.4.2. Fundamentos del MOT y el paradigma tracking-by-detection

El problema MOT se formula como la estimación simultánea del número de objetos presentes en una secuencia de video y de sus trayectorias individuales a lo largo del tiempo, a partir de un flujo de observaciones ruidosas e incompletas. Formalmente, dado un conjunto de detecciones en cada instante, el objetivo es asignar cada detección a una trayectoria existente o inicializar una nueva, de modo que el conjunto de trayectorias resultante sea coherente con las observaciones y minimice errores de asociación, fragmentación e ID switches (Adžemović, 2025).

El paradigma dominante en MOT es el de tracking-by-detection, que desacopla el problema en dos etapas independientes: (1) detección de objetos en cada cuadro, producida por un detector externo, y (2) asociación de las detecciones entre cuadros consecutivos mediante un algoritmo de tracking que mantiene el estado de las trayectorias activas. Este desacoplamiento tiene una consecuencia arquitectónica fundamental para el proyecto: el tracker no impone restricciones sobre el tipo de detector utilizado, lo que permite integrar un modelo OVD con vocabulario abierto y consultas dinámicas sin necesidad de adaptar ni reentrenar el componente de tracking (Adžemović, 2025).

Dentro del paradigma tracking-by-detection, el problema de asociación de datos puede descomponerse en tres subproblemas técnicos: modelado del movimiento (predicción del estado futuro de cada trayectoria activa), cálculo de similitud (medida de compatibilidad entre cada trayectoria predicha y cada nueva detección) y asignación óptima (resolución del problema combinatorio de emparejamiento entre trayectorias y detecciones, típicamente mediante el algoritmo Húngaro) (Bewley et al., 2016).


##### 16.4.2.1. Formulación general del problema MOT

Desde una perspectiva conceptual, el problema de MOT puede descomponerse en tres subproblemas fundamentales (Du et al., 2024):

Estimación del estado del objeto. Cada objeto es modelado mediante un estado interno que suele incluir su posición espacial (por ejemplo, centro del bounding box), velocidad y, en algunos enfoques, aceleración u otros atributos geométricos. El objetivo es predecir cómo evolucionará este estado entre fotogramas consecutivos.

Asociación de datos (data association). Dado un conjunto de detecciones en el fotograma actual y un conjunto de trayectorias activas, el sistema debe decidir qué detección corresponde a qué trayectoria. Este paso es crítico y constituye una de las principales fuentes de error en MOT (Rakai et al., 2022).

Gestión del ciclo de vida de las trayectorias. Incluye la inicialización de nuevas trayectorias cuando aparecen objetos no vistos previamente, el mantenimiento de trayectorias activas durante oclusiones temporales y la terminación de trayectorias cuando un objeto abandona la escena de forma definitiva.

Estos tres componentes interactúan de manera continua y deben resolverse bajo restricciones de tiempo real en aplicaciones prácticas.


##### 16.4.2.2. Modelado de movimiento y estimación de estado

El filtro de Kalman es el modelo de movimiento de referencia en los métodos MOT modernos. Asume que el estado de cada objeto —posición, dimensiones y velocidad del bounding box— evoluciona de acuerdo con un modelo lineal-gaussiano, y proporciona una estimación bayesiana óptima del estado actual dado el historial de observaciones. En cada cuadro, el filtro realiza dos operaciones: predicción del estado en el instante siguiente según el modelo dinámico, y corrección del estado predicho a partir de la nueva detección asociada (Bewley et al., 2016). Esta estructura permite mantener estimaciones de estado coherentes incluso durante períodos en los que el objeto no es detectado, extendiendo la trayectoria a través de breves oclusiones o gaps de detección.

La principal limitación del filtro de Kalman lineal es su supuesto de movimiento rectilíneo uniforme, que puede ser inadecuado para entidades con trayectorias no lineales, cambios bruscos de velocidad, o movimiento de cámara. Métodos como OC-SORT introducen correcciones observation-centric que mejoran la estimación del modelo dinámico durante los períodos de oclusión, reduciendo el error de predicción cuando las trayectorias retoman la observación tras una ausencia (Cao et al., 2023).

En escenarios más complejos, donde los movimientos son no lineales o altamente impredecibles, se han explorado variantes como filtros extendidos, filtros de partículas o incluso modelos aprendidos mediante redes neuronales. No obstante, estos enfoques suelen implicar un mayor costo computacional (Li et al., 2025).


##### 16.4.2.3. Asociación de datos y métricas de similitud

La asociación de datos constituye el núcleo del seguimiento multiobjetivo. Dado un conjunto de trayectorias predichas y un conjunto de detecciones actuales, el sistema debe resolver un problema de asignación óptima que determine qué detección corresponde a cada trayectoria existente (Emami et al., 2021). Este problema se formula como una optimización bipartita: un conjunto de nodos representa las trayectorias activas, otro las detecciones del fotograma actual, y las aristas están ponderadas por un costo que refleja la probabilidad de correspondencia. La formulación más directa corresponde al problema de asignación lineal (Linear Assignment Problem, LAP), que busca un emparejamiento de peso mínimo en el grafo bipartito resultante.

Para construir la matriz de costos se emplean, típicamente, señales complementarias: métricas geométricas, métricas cinemático-estadísticas (derivadas del modelo de movimiento) y, en enfoques más robustos, términos de apariencia. Las métricas geométricas evalúan proximidad espacial entre predicciones y detecciones. Entre ellas, la intersección sobre unión (IoU) entre cajas delimitadoras es ampliamente utilizada por su simplicidad y por ofrecer una medida normalizada entre 0 y 1, invariante al tamaño absoluto (Bewley et al., 2016). Alternativamente, la distancia euclídea entre centroides constituye una opción computacionalmente simple, aunque menos robusta ante variaciones de escala y deformaciones del objeto observado (Pereira et al., 2022).

En paralelo, la consistencia temporal puede evaluarse mediante la distancia de Mahalanobis, que incorpora la incertidumbre de la predicción a través de la matriz de covarianza del filtro de Kalman. Esta distancia permite estimar cuán probable es que una detección corresponda a una trayectoria, considerando simultáneamente la posición predicha y la incertidumbre asociada (Wojke et al., 2017). En sistemas que incorporan apariencia (el análisis del modelado de apariencia), la asociación se beneficia de descriptores visuales que complementan la evidencia geométrica y cinemática, especialmente ante cruces de trayectorias u oclusiones.

Una vez construida la matriz de costos, el problema de asignación se resuelve mediante el algoritmo húngaro, propuesto por Kuhn (1955) y refinado por Munkres (1957), que garantiza la asignación óptima en tiempo polinómico O(n³). No obstante, su complejidad crece cúbicamente con el número de objetos, lo que motiva la aplicación de técnicas de gating o validación que restringen el conjunto de asociaciones candidatas. El gate define un umbral basado en la distancia estadística entre predicción y mediciones, de modo que solo las detecciones dentro de esta región se consideran candidatas válidas (Bar-Shalom et al., 2011). Este mecanismo reduce significativamente los pares a evaluar sin comprometer la precisión del seguimiento (Bar-Shalom et al., 1990).


##### 16.4.2.4. Modelado de apariencia y re-identificación

La medida de similitud entre trayectorias predichas y nuevas detecciones puede basarse en criterios geométricos, criterios de apariencia o una combinación de ambos. La similitud geométrica más utilizada es la Intersección sobre la Unión (IoU) entre el bounding box predicho por el tracker y el bounding box reportado por el detector: una IoU alta indica que la trayectoria predicha y la nueva detección corresponden probablemente al mismo objeto físico (Bewley et al., 2016).

El modelado de apariencia incorpora descriptores visuales —embeddings extraídos por redes de re-identificación (ReID)— para complementar la similitud geométrica, particularmente en situaciones donde múltiples objetos presentan trayectorias que se cruzan o donde la IoU es ambigua. DeepSORT (Wojke et al., 2017) es el exponente paradigmático de este enfoque: introduce una función de costo que combina distancia de Mahalanobis sobre el estado predicho por Kalman y distancia coseno entre embeddings de apariencia, resolviendo la asignación mediante una estrategia en cascada que prioriza las trayectorias activas más recientes. La contrapartida es la dependencia de un modelo ReID preentrenado, cuyo rendimiento puede degradarse cuando el dominio visual del entorno de despliegue difiere del dominio de entrenamiento.

Los enfoques modernos incorporan vectores de características (embeddings) que capturan información visual distintiva del objeto, como textura, color o forma. Estas representaciones permiten comparar detecciones actuales con apariencias históricas, mejorando la capacidad de mantener la identidad a lo largo del tiempo.

Este principio se relaciona estrechamente con el problema de re-identificación (ReID), donde el objetivo es reconocer el mismo objeto tras una interrupción temporal o espacial. En MOT, la ReID no busca identificar a una persona concreta en términos biométricos, sino preservar la consistencia de los identificadores internos del sistema.


##### 16.4.2.5. Gestión de oclusiones y ambigüedades

Las oclusiones representan uno de los desafíos más complejos del seguimiento multi-objeto. Durante una oclusión, un objeto puede desaparecer parcial o totalmente del campo visual, generando ambigüedad en la asociación futura (Du et al., 2024).

Para mitigar este problema, los sistemas MOT suelen mantener trayectorias "latentes" durante un número limitado de fotogramas sin detecciones, usar predicciones de movimiento para estimar la posición esperada del objeto oculto, y reasociar detecciones posteriores basándose en criterios de similitud acumulada. El diseño de estos mecanismos implica un delicado equilibrio: mantener trayectorias demasiado tiempo puede generar asociaciones incorrectas, mientras que terminarlas prematuramente incrementa la fragmentación de identidades.


##### 16.4.2.6. Implicancias para sistemas en tiempo real y open-vocabulary

En el contexto de sistemas de análisis de video en tiempo real, los fundamentos descritos deben adaptarse a restricciones estrictas de latencia y recursos computacionales. Esto favorece enfoques determinísticos y eficientes, con mínima dependencia de reentrenamientos, y capaces de operar de forma desacoplada respecto al detector.

Estas características resultan especialmente compatibles con plataformas de detección open-vocabulary, donde el conjunto de objetos detectados puede variar dinámicamente según las consultas del usuario. En este escenario, el tracking no puede asumir un conjunto fijo de clases ni entrenarse específicamente para cada una, sino que debe operar sobre representaciones genéricas y detecciones dinámicas, reforzando la necesidad de algoritmos de MOT robustos, modulares y agnósticos al vocabulario (Li et al., 2025).


#### 16.4.3. Integración conceptual OVD + MOT

La integración de un detector OVD con un método MOT no es trivial desde el punto de vista arquitectónico. El detector produce detecciones con etiquetas semánticas abiertas —determinadas por el prompt de consulta— mientras que el tracker opera sobre bounding boxes y estados cinemáticos sin referencia semántica. Esta asimetría implica que la identidad asignada por el tracker es puramente geométrica y temporal, independiente de la etiqueta semántica de la detección. En consecuencia, el sistema puede rastrear entidades cuya etiqueta semántica varía entre cuadros —si el modelo OVD produce detecciones inconsistentes para el mismo objeto físico—, fenómeno que los trackers actuales no modelan explícitamente dado que operan bajo supuestos geométricos tradicionales sin integrar incertidumbre semántica (S. Li et al., 2025). La definición de una estrategia de estabilización semántica —por ejemplo, mediante agregación de etiquetas o ponderación por confianza a lo largo de la trayectoria— constituye un desafío de diseño que deberá abordarse durante las etapas de implementación del prototipo.

La arquitectura de integración más directa y modularmente limpia organiza el procesamiento en cuatro etapas secuenciales: cada cuadro de entrada es procesado por el detector OVD, que genera detecciones con sus etiquetas semánticas; estas detecciones son recibidas por el método MOT, que asigna identidades y actualiza las trayectorias activas; finalmente, un módulo de razonamiento temporal evalúa condiciones de persistencia sobre dichas trayectorias para decidir la emisión de alertas. Este flujo preserva el desacoplamiento entre los componentes, permite sustituir cualquiera de ellos de manera independiente, y mantiene la separabilidad entre el plano de medios —ingesta y procesamiento de video— y el plano de control —gestión de eventos y alertas—, de acuerdo con la arquitectura modular definida.

La literatura reciente confirma que esta integración es técnicamente viable y que el MOT puede aportar coherencia temporal significativa a las detecciones OVD, reduciendo la tasa de falsas alarmas generadas por detecciones espurias de corta duración (S. Li et al., 2023). No obstante, la calidad de la integración depende críticamente de la estabilidad del detector subyacente: un modelo OVD con alta variabilidad frame-a-frame introduce ruido en la entrada del tracker que puede superar la capacidad de corrección de los filtros de movimiento y las estrategias de asociación jerárquica.


#### 16.4.4. Criterios orientadores para la selección de métodos MOT

El análisis del estado del arte realizado en las secciones precedentes permite identificar un conjunto de criterios técnicos que deberán orientar la selección de métodos de seguimiento multi-objeto en las etapas posteriores del trabajo. Estos criterios emergen de la intersección entre las características observadas en los métodos representativos y los requisitos específicos de una implementación concreta orientada al análisis de vídeo en tiempo real.


##### 16.4.4.1. Criterios derivados del análisis teórico

A partir de la revisión bibliográfica y la comparativa sistemática, se identifican cinco ejes de evaluación relevantes para la selección futura:

Compatibilidad con detección open-vocabulary. El método de tracking debe operar sobre detecciones cuyas clases pueden variar dinámicamente según las consultas del usuario, sin asumir un vocabulario cerrado ni requerir entrenamiento específico por categoría.

Latencia compatible con tiempo real. Para aplicaciones de monitoreo continuo, el sistema completo (detección + tracking) debe sostener tasas de procesamiento que permitan respuesta operativa, típicamente en el orden de 20-30 FPS o superiores.

Desacoplamiento arquitectónico. Siguiendo el paradigma tracking-by-detection, el módulo de seguimiento debe integrarse de forma independiente al detector, permitiendo la sustitución o actualización de componentes sin rediseño del pipeline.

Independencia de entrenamiento específico. Para maximizar la generalidad y reproducibilidad del prototipo, resultan preferibles métodos que no requieran datasets de entrenamiento adicionales ni modelos auxiliares preentrenados en dominios específicos.

Robustez operativa suficiente. El método debe ofrecer estabilidad de identidades adecuada para evaluar persistencia temporal de condiciones, aun cuando no alcance el máximo rendimiento en benchmarks académicos.


##### 16.4.4.2. Implicancias para etapas posteriores

Los criterios enunciados no determinan una selección única, sino que definen un espacio de soluciones factibles dentro del cual deberán evaluarse alternativas concretas durante las etapas de diseño arquitectónico e implementación. El análisis teórico sugiere que los métodos de la familia tracking-by-detection basados en asociación geométrica presentan, en principio, mayor alineación con estos criterios que los enfoques end-to-end o aquellos que dependen de modelos de apariencia entrenados.

La decisión final deberá considerar además factores prácticos —disponibilidad de implementaciones, documentación, compatibilidad con el stack tecnológico seleccionado— que exceden el alcance de la fundamentación teórica y serán abordados en la etapa de análisis y diseño arquitectónico.


### 16.5. Operación en Tiempo Real y Fundamentos de Transmisión, Aceleración y Arquitecturas de Borde

Un sistema que detecta correctamente y rastrea con precisión puede ser, aun así, operativamente inútil. Si el tiempo que transcurre entre la aparición de una condición de riesgo y la generación de la alerta supera el margen disponible para intervenir, la detección llega tarde. La latencia no es un parámetro de rendimiento secundario: es una restricción de diseño que atraviesa cada componente del pipeline, desde el protocolo por el que ingresa el video hasta el hardware donde corre la inferencia. Esta sección caracteriza ese marco de restricciones —componentes de latencia, protocolos de transmisión, estrategias de aceleración por hardware y arquitecturas de procesamiento en el borde— y establece los criterios que deberán orientar las decisiones de diseño de etapas posteriores.


#### 16.5.1. La latencia end-to-end como restricción de diseño

En sistemas de video analítico en tiempo real, la latencia end-to-end —denominada también glass-to-glass (G2G) o sensor-to-screen— se define como el intervalo temporal desde que un fotograma es capturado por la cámara hasta que el resultado del análisis está disponible para el supervisor (Axis Communications AB, 2015). Esta definición general admite una distinción conceptual importante para el sistema E-OVRT-VDP: la latencia glass-to-glass (G2G) mide el tiempo hasta que el frame se visualiza en pantalla, mientras que la latencia glass-to-algorithm (G2A) mide el tiempo hasta que el módulo de inferencia produce un resultado sobre ese frame (Bachhuber et al., 2018). Para un sistema cuyo objetivo es generar alertas, la métrica operativamente relevante es G2A, ya que determina cuándo la condición de riesgo puede detectarse, no cuándo el video puede verse.

La latencia G2A puede modelarse como la suma de contribuciones de cada etapa del pipeline de procesamiento (H. Wang et al., 2022):


|  | (1) |
| --- | --- |

Cada término representa una fuente de retardo cuantificable y, en la mayoría de los casos, configurable mediante decisiones de diseño. El componente de inferencia introduce la latencia del módulo OVD al pipeline, transformando lo que en un sistema de videovigilancia convencional sería un pipeline de cinco etapas en uno de seis, con la particularidad de que la latencia de la etapa de inferencia es la de mayor variabilidad y de mayor dependencia de las decisiones de diseño arquitectónico del sistema (X. Li et al., 2022).

Un criterio de referencia relevante para calibrar el presupuesto de latencia del sistema proviene de la literatura sobre interacción humano-computadora: retrasos superiores a 100 ms en sistemas interactivos comienzan a erosionar la percepción de inmediatez en tareas de atención directa (Card et al., 2008), y estudios con interfaces táctiles evidencian que los usuarios perciben diferencias de latencia del orden de decenas de milisegundos en tareas de alta demanda atencional (Deber et al., 2015). Para sistemas de videovigilancia de seguridad con un operador humano en el bucle (human-in-the-loop), la literatura sobre sistemas de control remoto sitúa en el orden de las centenas de milisegundos el umbral de interactividad aceptable. Este rango de referencia es un insumo conceptual para la definición del presupuesto de latencia del prototipo, cuya formalización como requisito operativo corresponde a la segunda etapa del proyecto.

Una implicación crítica de la descomposición por componentes es que la latencia del sistema no es una propiedad del protocolo de streaming ni del modelo de inferencia por separado: es la resultante acumulada de todas las etapas del pipeline. En consecuencia, la optimización de un único componente puede resultar insuficiente si otro componente domina el presupuesto de latencia total. La gestión de buffers en el receptor es un ejemplo paradigmático: cada milisegundo de buffer añadido para estabilizar el flujo ante jitter de red incrementa directamente la latencia E2E, por lo que el diseño del sistema debe presupuestar explícitamente cuánto de la latencia total se asigna a cada componente (Axis Communications AB, 2015).


#### 16.5.2. Descomposición de componentes del pipeline

La Tabla 11 presenta la descomposición de los componentes de latencia del pipeline E2E, con sus rangos de referencia documentados en la literatura y las principales estrategias de reducción identificadas. Esta tabla constituye el marco analítico que guiará la instrumentación de medición de latencia en las fases experimentales del proyecto.

Tabla 11

Componentes de latencia del pipeline glass-to-algorithm en sistemas de video analítico con Computer Vision


| Componente | Rango de referencia | Principales factores determinantes | Estrategias de reducción documentadas |
| --- | --- | --- | --- |
| Captura | ~1 período de cuadro (≈33 ms a 30 fps) | Tasa de frames del sensor; exposición; procesamiento ISP interno (10–50 ms); algoritmos AEC/AGC | Aumentar frame rate; reducir tiempo de exposición; deshabilitar funciones no esenciales del ISP |
| Codificación | ~10–100 ms | Códec (H.264 vs H.265 vs AV1); GOP size; B-frames; aceleración HW | Perfil zerolatency; GOP=1; desactivar B-frames; encoder por GPU (NVENC, VA-API) |
| Transporte | ~1–500 ms según protocolo y red | RTT de red; jitter; pérdida de paquetes; buffers de transmisión; ARQ | Protocolo UDP sobre LAN; SRT con latency budget ajustado; minimizar saltos de red |
| Decodificación | ~5–50 ms | Complejidad del códec; dependencias entre frames; aceleración HW | Decodificación por GPU; streams con bajo nivel de dependencias entre frames |
| Renderizado / Jitter Buffer | ~10–120 ms | Tamaño del jitter buffer; tasa de refresco de pantalla; sincronización | Reducir jitter buffer al mínimo compatible con estabilidad; sincronización con v-sync |
| Inferencia OVD | ~10–150 ms por frame (modelo-dependiente) | Arquitectura del modelo; resolución de entrada; hardware de inferencia; caching de embeddings | Modelos one-stage con reparametrización; caching de text embeddings; inferencia por GPU (TensorRT) |

Nota. Los rangos de referencia son dependientes de configuración y hardware; no constituyen garantías de los protocolos o modelos. corresponde al componente adicional introducido por el módulo OVD respecto de un pipeline de videovigilancia convencional, cuya incorporación al modelo de latencia G2A está fundamentada en Bachhuber et al. (2018). La distinción entre rango de modelos one-stage (~10–30 ms) y arquitecturas Transformer sin optimización (~50–150 ms) sigue a Cheng et al. (2024) y Ren et al. (2024). El factor de caching de text embeddings y su impacto (~40 ms) sigue a Zhao et al. (2024). G2A = Glass-to-Algorithm. HW = Hardware. GOP = Group of Pictures. Fuente: Elaboración propia basada en Axis Communications AB (2015), Bachhuber et al. (2018), Cheng et al. (2024), Li et al. (2022), Wang et al. (2022) y Zhao et al. (2024)

La tabla evidencia que los seis componentes del pipeline presentan perfiles de variabilidad heterogéneos. Mientras los componentes de captura, decodificación y renderizado operan dentro de rangos relativamente acotados por las propiedades físicas del sensor, la complejidad algorítmica del códec y los ciclos de refresco del display, los componentes codificación, transporte e inferencia exhiben rangos que se extienden hasta dos órdenes de magnitud según el protocolo, la infraestructura de red y la arquitectura del modelo empleados. Esta heterogeneidad implica que la latencia G2A no es una propiedad emergente uniforme del pipeline, sino el resultado acumulado de contribuciones con naturalezas de variabilidad distintas. Las implicaciones de este perfil para la definición del protocolo experimental se desarrollan en los apartados metodológicos posteriores.


##### 16.5.2.1. Latencia de Captura

Este componente abarca múltiples factores en la etapa de adquisición de imagen, desde que la luz llega al sensor hasta que el frame está disponible para codificación y transmisión.

El factor dominante es la frecuencia de muestreo del sensor: en un sistema operando a 30 fps, por ejemplo, cada fotograma requiere aproximadamente 33,3 ms para completar su ciclo de exposición y lectura (Axis Communications AB, 2015). Este valor representa el límite temporal mínimo entre fotogramas consecutivos y constituye una restricción fundamental que no puede reducirse sin incrementar la frecuencia de captura. La relación es directamente proporcional: duplicar la frecuencia a 60 fps reduce el período de frame a 16,7 ms, aunque esto incrementa el ancho de banda requerido y la carga computacional de procesamiento posterior.

Un segundo elemento significativo de latencia en esta etapa proviene del procesamiento interno de la cámara mediante el Image Signal Processor (ISP). El ISP ejecuta funciones internas de mejora (balance de blancos, reducción de ruido, estabilización, etc.), cuyas operaciones pueden introducir una latencia adicional que varía entre los 10-50 ms, según la complejidad de la etapa del pipeline (Axis Communications AB, 2015). En aplicaciones donde el tiempo real estricto cobra importancia, resulta posible (y hasta necesario) disminuir esta latencia, deshabilitando funciones no esenciales del ISP, sacrificando calidad de imagen por capacidad de respuesta. El uso intensivo de funciones de ISP, según fabricantes, puede aumentar la latencia entre 2 y 6 frames (Active Silicon Ltd, 2025).

Otro elemento determinante en la latencia son los algoritmos de control automático de exposición y ganancia (AEC/AGC), cuyo mecanismo de retroalimentación introduce una latencia que puede alcanzar los dos frames en entornos de iluminación variable (Shim et al., 2019). Al igual que en el punto anterior, su desactivación puede constituir una mejora en los tiempos de respuesta, a cosa de trabajar con configuraciones manuales o entornos más controlados.


##### 16.5.2.2. Latencia de Codificación

La latencia de codificación representa el tiempo requerido para transformar los datos crudos del sensor en un flujo de video comprimido listo para transmisión. Este componente depende fundamentalmente de la complejidad algorítmica del códec empleado, su configuración operativa y el tipo de implementación utilizada (software vs hardware acelerado). La elección de estas variables define un compromiso entre eficiencia de compresión, latencia de procesamiento y calidad visual resultante. Las tecnologías de aceleración por hardware para codificación serán abordadas en detalle en la sección 16.5.3.2 , dado que constituyen un componente arquitectónico crítico de los sistemas de procesamiento de video en tiempo real.


###### 16.5.2.2.1. Naturaleza del Componente y Factores Determinantes

La latencia de codificación depende principalmente de (1) la complejidad del códec y (2) los recursos disponibles para ejecutarlo. Códecs modernos como H.264/AVC y H.265/HEVC reducen el tamaño de los datos explotando redundancias temporales (entre fotogramas) y espaciales (dentro de un fotograma), pero lo hacen con costos computacionales distintos.

H.264/AVC, publicado como estándar ISO/IEC 14496-10 e ITU-T H.264 en 2003, procesa video en unidades denominadas macrobloques de tamaño fijo 16×16 píxeles (Wiegand et al., 2003). Implementaciones optimizadas para baja latencia de este códec pueden alcanzar tiempos de procesamiento del orden de decenas de milisegundos por fotograma en configuraciones básicas (Axis Communications AB, 2015). Su amplia adopción en videovigilancia, videoconferencia y transmisión en vivo se debe a un equilibrio favorable entre eficiencia de compresión, latencia aceptable y disponibilidad ubicua de decodificadores compatibles (Wiegand et al., 2003).

H.265/HEVC, estandarizado en 2013 como ITU-T H.265 e ISO/IEC 23008-2, representa un avance significativo en eficiencia de compresión: ofrece aproximadamente un 50% de reducción de bitrate respecto a H.264/AVC para la misma calidad perceptual (Sullivan et al., 2012). Esta ganancia en eficiencia se logra mediante algoritmos de mayor complejidad computacional. HEVC utiliza Coding Tree Units (CTUs) de tamaño variable que pueden abarcar desde 16×16 hasta 64×64 píxeles, en contraste con los macrobloques fijos de 16×16 en H.264 (Sullivan et al., 2012). Esta flexibilidad permite al codificador asignar bloques grandes a regiones uniformes de la imagen (como cielos despejados) y bloques pequeños a regiones con alto detalle (como texturas o bordes), optimizando así la asignación de bits disponibles. Sin embargo, el proceso de decisión óptima sobre el tamaño y particionamiento de las CTUs introduce una carga computacional significativa: los codificadores HEVC se espera que sean varias veces más complejos que los codificadores H.264/AVC (Bossen et al., 2012).

El compromiso fundamental reside en que mayor eficiencia de compresión requiere algoritmos más sofisticados, lo que incrementa tanto la latencia de codificación como la demanda de recursos computacionales. En sistemas donde la latencia end-to-end debe minimizarse, puede ser preferible emplear H.264 en configuraciones de baja latencia antes que HEVC, a pesar de la penalización en eficiencia de compresión. Alternativamente, el uso de aceleración hardware mediante motores dedicados de codificación (como NVIDIA NVENC, Intel Quick Sync o AMD VCE) puede mitigar significativamente la latencia introducida por la codificación.


###### 16.5.2.2.2. Configuraciones para Minimizar Latencia

Existen modos operativos específicos orientados a reducir la latencia de codificación, los cuales sacrifican eficiencia de compresión en favor de un procesamiento más rápido y menor buffering. Para comprender estas configuraciones es necesario primero definir los tipos básicos de fotogramas utilizados en compresión de vídeo.

Los códecs de vídeo modernos emplean tres tipos fundamentales de fotogramas (Wiegand et al., 2003):

I-frames (Intra-coded frames): Fotogramas codificados de manera independiente sin referencias a otros fotogramas. Contienen una imagen completa comprimida utilizando únicamente redundancia espacial dentro del propio fotograma. Funcionan como puntos de acceso aleatorios y referencias para la decodificación de fotogramas posteriores.

P-frames (Predictive frames): Fotogramas codificados mediante predicción desde uno o más fotogramas de referencia previos. Contienen únicamente las diferencias (residuales de predicción) respecto a los fotogramas de referencia, junto con vectores de movimiento que indican las transformaciones espaciales entre el fotograma actual y las referencias. Requieren que el fotograma de referencia haya sido decodificado antes de poder procesar el P-frame.

B-frames (Bi-predictive frames): Fotogramas que pueden utilizar referencias tanto de fotogramas pasados como futuros (en orden de presentación). Permiten predicción bidireccional mediante interpolación de referencias temporalmente anteriores y posteriores, logrando mayor eficiencia de compresión que los P-frames. Sin embargo, introducen latencia adicional al requerir que el codificador procese fotogramas futuros antes de codificar el B-frame actual, y al obligar al decodificador a mantener en buffer tanto referencias pasadas como futuras.

Con base en estos tipos de fotogramas, las técnicas principales para minimizar latencia son:

Reducción del tamaño del Group of Pictures (GOP). Un GOP define la estructura de secuencia de tipos de fotogramas entre dos I-frames consecutivos. Un GOP corto (menor cantidad de cuadros entre I-frames) reduce el intervalo de dependencia temporal entre fotogramas, permitiendo que cada segmento pueda decodificarse de manera más independiente. Esto reduce el buffering necesario en el decodificador y facilita la recuperación ante pérdidas de paquetes, dado que el próximo I-frame restaura una referencia completa sin dependencias (Axis Communications AB, 2015). En configuraciones de latencia ultra-baja puede emplearse GOP=1, generando únicamente I-frames, aunque esto incrementa sustancialmente el bitrate requerido.

Eliminación de cuadros B (bi-predictive frames). Los cuadros B utilizan referencias tanto de fotogramas pasados como futuros, lo que introduce latencia adicional al requerir que el codificador espere a procesar fotogramas posteriores antes de codificar el cuadro B actual, y al obligar al decodificador a reordenar los fotogramas recibidos antes de su presentación. La configuración Baseline Profile de H.264/AVC excluye explícitamente los cuadros B, utilizando únicamente cuadros I (intra-coded) y P (predictive), lo que permite la codificación y decodificación en orden de presentación sin necesidad de reordenamiento ni buffering adicional de fotogramas futuros (Wiegand et al., 2003). Este perfil fue diseñado específicamente para aplicaciones de tiempo real como videoconferencia y transmisión en vivo donde la baja latencia es prioritaria.

Uso exclusivo de cuadros I y P. Al operar con solo cuadros I y P, cada fotograma puede decodificarse inmediatamente tras su recepción completa, sin esperar a futuros fotogramas de referencia. Esta configuración minimiza la interdependencia temporal entre fotogramas, reduciendo así tanto la latencia de codificación como la de decodificación (Axis Communications AB, 2015). El decodificador solo necesita mantener en su buffer de fotogramas decodificados (Decoded Picture Buffer, DPB) las referencias pasadas estrictamente necesarias, eliminando la necesidad de almacenar fotogramas futuros.

Estos ajustes tienen como consecuencia un incremento en el bitrate necesario para mantener una calidad visual equivalente, dado que se reduce la capacidad del códec para explotar redundancias temporales entre fotogramas distantes mediante predicción bidireccional. Sin embargo, en escenarios donde la latencia end-to-end es crítica para la operación del sistema, este compromiso resulta aceptable e incluso necesario (Wiegand et al., 2003).


##### 16.5.2.3. Latencia de Transporte

La latencia de transporte representa el tiempo requerido para que los paquetes de video codificados atraviesen la infraestructura de red desde el punto de transmisión hasta el punto de recepción. A diferencia de los componentes previos, es altamente variable y depende de factores externos al sistema de procesamiento de video, tales como la topología de red, el nivel de congestión y la distancia física entre nodos.


###### 16.5.2.3.1. Componentes de la Latencia de Transporte

La latencia total de transporte en redes de conmutación de paquetes se compone de cuatro elementos principales, cuya suma determina el retardo experimentado por cada paquete individual (Kurose & Ross, 2021):

Retardo de propagación. Tiempo físico de propagación de la señal a través del medio de transmisión, limitado por la velocidad de la luz en el material conductor.

Retardo de encolado. Tiempo que un paquete permanece en las colas de dispositivos de red (routers, switches) antes de ser transmitido. Suele ser el componente más variable de la latencia de transporte porque depende directamente del nivel de congestión momentáneo, esto es, con tráfico bajo puede ser inferior a 1 ms, mientras que bajo alta carga puede escalar a decenas de milisegundos. Además, este retardo puede incrementarse de forma marcada cuando existen buffers excesivos en la red (fenómeno conocido como bufferbloat), alcanzando incluso cientos de milisegundos en conexiones de banda ancha (Gettys & Nichols, 2012).

Retardo de procesamiento. Tiempo que requieren los dispositivos de red para procesar encabezados de paquetes, realizar lookups de tablas de enrutamiento y tomar decisiones de reenvío.

Retardo de retransmisión. Presente únicamente cuando se utilizan protocolos orientados a confiabilidad, como TCP o protocolos de streaming con ARQ (Automatic Repeat reQuest). La retransmisión de paquetes perdidos introduce un retardo adicional equivalente al tiempo de ida y vuelta (RTT, Round-Trip Time) completo. Para aplicaciones de video en tiempo real, se priorizan protocolos de transporte no confiables como UDP en combinación con RTP (Real-time Transport Protocol) que eliminan el retardo de retransmisión a cambio de tolerar pérdidas ocasionales de paquetes (Schulzrinne et al., 2003a).


###### 16.5.2.3.2. Variabilidad Temporal: Jitter de Red

El jitter de red es la variación del retardo de llegada entre paquetes consecutivos. En redes de conmutación de paquetes, cada paquete puede experimentar un retardo distinto debido a fluctuaciones en el encolado y, en menor medida, a cambios en la ruta o en el estado instantáneo de los enlaces. Como resultado, aun cuando el emisor genere un flujo a intervalos regulares, el receptor observa irregularidades temporales en la entrega, lo que impacta directamente en la estabilidad del playout de video (Kurose & Ross, 2021).

En la práctica, protocolos de transporte de tiempo real como RTP, junto con RTCP, permiten estimar y reportar esta variabilidad a partir de timestamps y números de secuencia, facilitando el monitoreo de calidad y la adaptación del receptor ante condiciones cambiantes (Schulzrinne et al., 2003a). Para amortiguar el efecto del jitter sobre la continuidad del video, el extremo receptor utiliza buffers de reproducción (playout/de-jitter), que suavizan la entrega a costa de introducir latencia adicional.


##### 16.5.2.4. Latencia de Decodificación

La latencia de decodificación corresponde al tiempo requerido para reconstruir los fotogramas de vídeo a partir del flujo comprimido recibido en el extremo receptor. Este componente del pipeline de procesamiento de video es fundamental para sistemas de tiempo real, dado que determina el retardo mínimo entre la recepción de datos codificados y la disponibilidad de fotogramas decodificados listos para su visualización. Al igual que en la codificación, la latencia de decodificación depende de la complejidad algorítmica del códec empleado, la estructura de predicción temporal utilizada, y el tipo de implementación (software o aceleración hardware).


###### 16.5.2.4.1. Complejidad Algorítmica y Dependencias de Predicción

La complejidad de decodificación varía significativamente entre códecs de diferentes generaciones. Estudios de análisis de complejidad mediante perfilado de ciclos de CPU demuestran que la decodificación de H.265/HEVC presenta un incremento del 61% al 87% en complejidad computacional respecto a H.264/AVC, dependiendo del perfil de codificación empleado (Viitanen et al., 2012). Este aumento de complejidad se debe a las unidades de codificación de tamaño variable (CTUs de hasta 64×64 píxeles en HEVC frente a macrobloques fijos de 16×16 en H.264), las estructuras de predicción jerárquicas más sofisticadas, y los filtros de post-procesamiento adicionales como el Sample Adaptive Offset (SAO) incorporados en HEVC (Sullivan et al., 2012).

La estructura de predicción temporal (GOP) incide directamente en la latencia de decodificación porque determina dependencias entre fotogramas y, por ende, el buffering mínimo requerido en el receptor. Como se describió al tratar las configuraciones de codificación orientadas a baja latencia, los fotogramas I se reconstruyen sin referencias, mientras que P y B dependen de fotogramas de referencia.En decodificación, esto se traduce en dos efectos principales: (i) la necesidad de mantener referencias en el Decoded Picture Buffer (DPB) y (ii) la reordenación entre el orden de decodificación y el orden de presentación, especialmente cuando existen fotogramas B. En configuraciones de baja latencia (p. ej., sin B-frames y con GOP corto), se reduce el tamaño efectivo del DPB y puede eliminarse el retardo por reordenamiento, habilitando la presentación del fotograma inmediatamente tras su decodificación (Axis Communications AB, 2015; Wiegand et al., 2003).

Los decodificadores modernos explotan oportunidades de paralelización a nivel de slice (segmentos independientes dentro de un fotograma) y a nivel de macrobloque o CTU. Esta capacidad de procesamiento paralelo permite distribuir la carga computacional entre múltiples núcleos de CPU, reduciendo el tiempo de decodificación en arquitecturas multinúcleo. Sin embargo, el overhead de sincronización entre hilos y las dependencias de datos imponen límites prácticos a la escalabilidad del paralelismo (Viitanen et al., 2012).


###### 16.5.2.4.2. Implementaciones: Software vs Aceleración Hardware

La decodificación puede realizarse mediante implementaciones de software ejecutadas sobre CPUs de propósito general o mediante aceleración hardware utilizando unidades especializadas integradas en GPUs, VPUs (Video Processing Units) o ASICs dedicados. Las implementaciones por software típicamente exhiben latencias en el orden de 10 a 50 ms dependiendo de la potencia del procesador, la resolución del video y la complejidad del códec empleado. En contraste, los decodificadores hardware ofrecen latencias predecibles y significativamente menores, típicamente en el rango de los 5 a 15 ms (según códec, resolución y pipeline), junto con un consumo energético sustancialmente inferior (Axis Communications AB, 2015). Esta ventaja resulta particularmente relevante para códecs de alta complejidad como H.265/HEVC, donde la decodificación por software puede no alcanzar desempeño en tiempo real para resoluciones altas (4K UHD o superiores) sin hardware especializado.

La disponibilidad generalizada de decodificadores hardware para H.264/AVC y H.265/HEVC en dispositivos modernos ha mitigado el impacto de la mayor complejidad algorítmica de HEVC, permitiendo decodificación en tiempo real incluso para resoluciones elevadas. La elección de la vía de aceleración (GPU/VPU/ASIC) afecta la latencia, throughput y consumo energético, por lo que constituye una decisión arquitectónica relevante.


###### 16.5.2.5. Latencia de Renderizado

La latencia de renderizado abarca el tiempo transcurrido desde que los fotogramas decodificados están disponibles hasta su presentación visual efectiva en el dispositivo de visualización. Este componente comprende dos elementos principales: la compensación de la variabilidad en la llegada de paquetes mediante buffers de reproducción (playout buffers), y la sincronización con los ciclos de refresco del display. Este componente introduce un compromiso explícito entre continuidad de reproducción y latencia total del sistema, constituyendo el último punto de ajuste antes de la percepción visual por parte del usuario.


###### 16.5.2.5.1. Jitter Buffer y Compensación de Variabilidad

El jitter de red constituye la variabilidad en el retardo de llegada de paquetes consecutivos, fenómeno inherente a las redes de conmutación de paquetes. En el extremo receptor, los sistemas de video en tiempo real incorporan buffers de reproducción (playout buffers o de-jitter buffers) cuya función es absorber esta variabilidad mediante la introducción de un retardo deliberado que permita entregar los paquetes decodificados a una tasa constante hacia el subsistema de visualización, garantizando así una reproducción fluida y continua.

El dimensionamiento del jitter buffer impone un compromiso directo entre robustez y latencia: buffers más profundos toleran mayor jitter y disminuyen la probabilidad de interrupciones (paquetes que llegan tarde respecto al instante de presentación), pero incrementan la latencia end-to-end; buffers pequeños, en cambio, minimizan la latencia agregada, aunque aumentan la sensibilidad a fluctuaciones de red (Clark et al., 2013).

En la práctica, se emplean buffers fijos (profundidad constante) o adaptativos (profundidad variable según condiciones observadas). En aplicaciones interactivas (p. ej., videoconferencia) se utilizan típicamente buffers de 20–100 ms para limitar la latencia percibida, mientras que en streaming no interactivo pueden adoptarse buffers de segundos para priorizar continuidad ante variaciones de red (Axis Communications AB, 2015; Schulzrinne et al., 2003a).


###### 16.5.2.5.2. Tasa de Refresco de Pantalla y Sincronización

La tasa de refresco del dispositivo de visualización afecta la latencia de presentación al imponer instantes discretos en los que la imagen puede actualizarse (ciclo de refresco). Los monitores convencionales operan típicamente a 60 Hz, lo que representa un intervalo de aproximadamente 16,7 ms entre refrescos consecutivos. Dispositivos orientados a aplicaciones profesionales, juegos de alto rendimiento o sistemas de tiempo crítico pueden operar a frecuencias superiores (120 Hz, 144 Hz, 240 Hz o incluso 500 Hz), reduciendo proporcionalmente este componente de latencia (Axis Communications AB, 2015).

La sincronización entre la disponibilidad de fotogramas decodificados y el ciclo de refresco del display afecta la latencia de presentación. Sin sincronización vertical (VSync), el framebuffer puede actualizarse durante el escaneo del display, produciendo tearing. Al habilitar VSync, la actualización queda restringida al intervalo de vertical blanking (VBLANK), eliminando ese artefacto pero introduciendo espera: en el peor caso, un fotograma listo debe aguardar hasta el próximo refresco, añadiendo hasta un período completo (≈16,7 ms a 60 Hz) (Axis Communications AB, 2015).

Para reducir este compromiso, tecnologías de tasa de refresco variable (VRR) —por ejemplo, NVIDIA G-Sync y AMD FreeSync— ajustan dinámicamente el refresco del display a la cadencia de generación de fotogramas, mitigando tearing sin la penalización típica de VSync, siempre que exista soporte de GPU y monitor. Cuando la tasa de fotogramas es inestable o no se alinea con el refresco, puede aparecer stuttering (duraciones desiguales de fotogramas), lo que refuerza la necesidad de mantener una cadencia lo más constante posible para preservar fluidez y previsibilidad temporal.


##### 16.5.2.6. Componente Adicional en Sistemas de Detección Asistida por IA

Las subsecciones siguientes caracterizan en detalle la latencia de inferencia como componente adicional del pipeline de video analítico: los factores que la determinan, los valores reportados en modelos open-vocabulary de referencia, las técnicas de optimización disponibles y sus implicaciones para el presupuesto total de latencia del sistema.

Factores que Determinan la Latencia de Inferencia. La latencia de inferencia en modelos de detección de objetos depende de múltiples factores interrelacionados. En primer lugar, la complejidad arquitectónica del modelo, medida en términos de número de parámetros, profundidad de capas y tipo de operaciones (convoluciones vs. mecanismos de atención transformer), determina el volumen de cómputo requerido por fotograma. Los modelos basados en transformers, como Grounding DINO, generalmente presentan mayor complejidad computacional que arquitecturas convolucionales como YOLO debido al costo cuadrático de los mecanismos de atención multi-cabeza (S. Liu et al., 2023).

En segundo lugar, la resolución de entrada del frame afecta directamente el tiempo de procesamiento: incrementar la resolución de 640×640 a 1280×1280 puede cuadruplicar el número de operaciones en capas convolucionales, introduciendo un trade-off fundamental entre precisión de detección (favorecida por mayores resoluciones) y velocidad de inferencia.

En tercer lugar, el hardware de ejecución constituye quizás el factor más determinante: GPUs modernas pueden acelerar la inferencia entre 5 y 10 veces comparado con CPUs, mientras que aceleradores especializados como TPUs o hardware de edge computing (NVIDIA Jetson, Google Coral) ofrecen trade-offs específicos entre eficiencia energética, latencia y disponibilidad de memoria (Zou et al., 2023). La literatura sobre deep video analytics en el borde evidencia que estos factores operan de manera conjunta: la selección del punto de operación óptimo —en términos de precisión del modelo, resolución de entrada y capacidad de hardware— constituye un problema de optimización multi-objetivo que no puede resolverse a partir de métricas aisladas de cada componente (Li et al., 2022).

Latencias Típicas en Modelos Open-Vocabulary. Los modelos de detección open-vocabulary presentan latencias variables según su diseño arquitectónico y optimizaciones. YOLO-World, optimizado para velocidad mediante arquitectura convolucional ligera y alineación visión-lenguaje eficiente, alcanza tasas de inferencia del orden de 10–30 ms por frame en GPUs de gama alta (NVIDIA RTX 3090 o superiores), lo que equivale a 30–100 FPS (Cheng et al., 2024). Grounding DINO, en su versión original basada en transformers pesados, presenta latencias significativamente mayores: aproximadamente 50–150 ms por frame en la misma clase de hardware, alcanzando apenas 6–20 FPS. No obstante, la versión Grounding DINO 1.5 Edge, optimizada para despliegue en dispositivos edge mediante arquitectura EfficientViT y TensorRT, logra reducir esta latencia a aproximadamente 13 ms por frame (75 FPS) en GPU A100, representando una mejora de 4× respecto a la implementación PyTorch nativa (Ren et al., 2024).

En dispositivos de edge computing como NVIDIA Jetson Orin NX, Grounding DINO 1.5 Edge alcanza tasas de 10–14 FPS (70–100 ms por frame) con resolución de entrada 640×640, demostrando la viabilidad de detección OV en plataformas de recursos limitados. En contraste, la ejecución en CPU de propósito general puede incrementar la latencia de 5–10 veces, tornando impracticable el procesamiento en tiempo real para la mayoría de aplicaciones críticas (Zou et al., 2023).

Técnicas de Optimización. Diversas técnicas permiten reducir la latencia de inferencia sin comprometer excesivamente la precisión de detección. La cuantización de pesos y activaciones, que reduce la precisión numérica de FP32 a FP16 o INT8, puede acelerar la inferencia en hardware con soporte nativo para estas operaciones. Frameworks de optimización como TensorRT de NVIDIA y ONNX Runtime incorporan técnicas de fusión de operadores (kernel fusion), optimización de grafos computacionales y selección automática de implementaciones de bajo nivel, logrando mejoras adicionales del orden de 20–50% sobre implementaciones PyTorch o TensorFlow estándar.

Técnicas de compresión de modelos como knowledge distillation y network pruning permiten reducir la complejidad del modelo preservando gran parte de su capacidad de generalización. El despliegue en dispositivos edge, si bien introduce restricciones de memoria y cómputo, ofrece ventajas en términos de latencia de red al procesar localmente, evitando el overhead de transmisión hacia servidores remotos (Shi et al., 2016a).

Implicaciones para el Presupuesto de Latencia del Sistema. La latencia de inferencia representa la adición más variable e incierta al presupuesto G2A total: a diferencia de los componentes del pipeline clásico, cuya contribución puede acotarse mediante configuración de protocolo y codec, la latencia del modelo depende de variables de diseño —complejidad arquitectónica, resolución de entrada, hardware disponible— cuyas interacciones no son lineales (Li et al., 2022). Este carácter multi-variable implica que los valores reportados en benchmarks de modelos individuales (FPS en GPU aislada, AP en COCO/LVIS) no son directamente trasladables al rendimiento del pipeline completo, como se argumenta en la sección 15.4.3.1 .

La revisión bibliográfica permite identificar dos rangos de referencia relevantes para el diseño experimental: el rango de 10–30 ms por frame, asociado a modelos convolucionales ligeros con optimización hardware (Cheng et al., 2024), y el rango de 50–150 ms, característico de arquitecturas transformer sin optimización específica para edge (Ren et al., 2024). La aceleración por hardware emerge como condición necesaria —y no suficiente— para mantener la contribución de este componente dentro de márgenes compatibles con la generación de alertas en tiempo real (Zou et al., 2023). La cuantificación precisa de estos márgenes en el contexto del pipeline completo de E-OVRT-VDP constituye uno de los objetivos de la validación experimental planificada para etapas posteriores.


##### 16.5.2.7. Umbrales Perceptuales y Requisitos de Interactividad

Desde la perspectiva de la interacción humano-computadora, existen umbrales de latencia más allá de los cuales el retraso se torna perceptible y degrada la experiencia del usuario. Investigaciones seminales establecieron que retrasos superiores a 100 ms en sistemas interactivos comienzan a erosionar la sensación de inmediatez y respuesta instantánea (Card et al., 2008). Estudios más recientes en interfaces táctiles han demostrado que los usuarios pueden percibir diferencias de latencia del orden de decenas de milisegundos en tareas de manipulación directa, afectando su percepción de fluidez y responsividad del sistema (Deber et al., 2015).

En contextos críticos de video en tiempo real —tales como teleoperación remota, conducción autónoma o videovigilancia activa de seguridad— la minimización de la latencia resulta fundamental para garantizar que las acciones correctivas o alertas se produzcan de manera oportuna. El paradigma de computación en el borde (edge computing) ha surgido precisamente para abordar los requisitos de baja latencia mediante el procesamiento de datos cerca de su fuente de generación, reduciendo significativamente los retardos asociados al tránsito por redes extendidas (Shi et al., 2016a). Este enfoque permite que sistemas sensibles al tiempo, como los de videovigilancia inteligente, operen con latencias sustancialmente inferiores a las alcanzables mediante arquitecturas centralizadas en la nube.

A partir de los umbrales perceptuales reportados en la literatura y de la naturaleza operativa de sistemas de monitoreo y respuesta, se observa que la interactividad en escenarios human-in-the-loop requiere latencias acotadas al orden de las centenas de milisegundos, rango en el cual la respuesta del sistema se percibe como fluida y la capacidad de intervención humana no se ve comprometida significativamente (Card et al., 2008; Deber et al., 2015). Estos hallazgos constituyen un insumo conceptual relevante para la definición del presupuesto de latencia del sistema, cuya cuantificación específica —como umbral operativo del prototipo— corresponde a la Etapa 2 del proyecto, donde se establecerán los criterios experimentales en función de las restricciones concretas de hardware, conectividad y carga de inferencia.


#### 16.5.3. Arquitecturas de procesamiento de video en tiempo real

El diseño de sistemas de análisis de video en tiempo real exige decisiones arquitectónicas que trascienden la elección de protocolos de streaming. En este tipo de plataformas, el desempeño no depende únicamente del transporte, sino principalmente de cómo se organiza el procesamiento interno: dónde se introduce buffering, cómo se gestiona el flujo de datos (backpressure), qué tan costosas son las transferencias de memoria, y cómo se desacoplan los componentes para integrar módulos heterogéneos sin degradar la latencia.

En el contexto de E-OVRT-VDP, la arquitectura debe sostener un pipeline continuo de video (ingesta, decodificación, preprocesamiento, inferencia y salida) con latencia acotada y predecible, a la vez que habilita funciones de coordinación (configuración, eventos, alertas, trazabilidad y escalamiento) sin bloquear la ruta crítica. Por ello, este capítulo sistematiza los fundamentos necesarios para diseñar la plantilla de streaming en tiempo real: (i) la separación conceptual entre plano de medios y plano de control, (ii) el aprovechamiento de aceleración por hardware en etapas de códec y cómputo, (iii) mecanismos eficientes de comunicación inter-proceso para arquitecturas modulares, y (iv) el rol de frameworks multimedia como base para construir pipelines reproducibles y extensibles.

Finalmente, la sección establece criterios que se utilizarán en las secciones posteriores para justificar decisiones del prototipo experimental, especialmente en términos de presupuesto de latencia end-to-end, portabilidad entre plataformas de hardware y capacidad de evolución del sistema.


##### 16.5.3.1. Separación de planos: plano de medios y plano de control

En sistemas complejos de análisis de video resulta conceptualmente útil distinguir dos planos de ejecución con responsabilidades diferenciadas. Esta separación, originada en el ámbito de las redes de telecomunicaciones donde se distingue entre el plano de datos (forwarding) y el plano de control (routing decisions), ha sido adoptada progresivamente en arquitecturas de software distribuido y sistemas de procesamiento de streams (Kreutz et al., 2015).

El plano de medios se encarga del flujo continuo de datos audiovisuales. Su función principal consiste en mantener el procesamiento sincronizado con el tiempo real: capturar o recibir el stream, decodificar los frames, aplicar el procesamiento requerido (inferencia, filtrado, anotación) y generar la salida correspondiente. Este plano opera como un pipeline donde los datos fluyen con mínima interacción externa, priorizando el throughput sostenido y la latencia predecible.

El plano de control orquesta eventos discretos y coordina el comportamiento general del sistema. Siguiendo principios de arquitecturas orientadas a eventos (Event-Driven Architecture, EDA), los componentes de este plano emiten y responden a mensajes de control sin necesidad de operar a framerate constante (Cugola & Margara, 2012). En el contexto de videovigilancia, este plano maneja notificaciones de detección, comandos de configuración, generación de alertas y administración de recursos del sistema.

La separación de planos proporciona beneficios arquitectónicos significativos, en la medida en que los sistemas modulares favorecen la mantenibilidad y la escalabilidad al encapsular responsabilidades en subsistemas cohesivos (Bass et al., 2022). En términos prácticos, esta organización permite optimizar el plano de medios para throughput y latencia constante, mientras el plano de control gestiona la lógica de negocio de manera asíncrona. Por ejemplo, ante la detección de una situación de riesgo, el pipeline de medios puede emitir un evento que el plano de control procesa de forma independiente, evitando que el flujo de video se bloquee mientras se confirma el envío de alertas.

Además se incluyen: aislamiento de la complejidad, que facilita la depuración de problemas de latencia en el plano de medios sin interferencia de la lógica de control; flexibilidad tecnológica, que permite evaluar alternativas como GStreamer versus FFmpeg en el plano de medios sin modificar la capa de control; escalabilidad distribuida, que habilita la ejecución del plano de medios en un nodo edge y el de control en la nube, comunicados mediante eventos de red; y trazabilidad, dado que el plano de control puede registrar eventos detallados sin sobrecargar el pipeline de video.


##### 16.5.3.2. Decodificación y codificación acelerada por hardware

El procesamiento de video en tiempo real impone una carga computacional elevada, especialmente cuando se requiere ingestar múltiples flujos y mantener resoluciones altas de forma sostenida. En este contexto, las etapas de decodificación (necesaria para acceder a los frames) y codificación (relevante cuando se retransmite, se reempaqueta o se registra video) suelen convertirse en componentes dominantes del costo de cómputo si se ejecutan en software.

Por esta razón, los stacks multimedia modernos priorizan el uso de motores dedicados de códec (en GPU/SoC/ASIC) accesibles mediante APIs de aceleración. Estos motores permiten descargar la carga de encode/decode desde CPU y/o desde el motor de cómputo general (p. ej., evitando competir con la inferencia), incrementando la capacidad de concurrencia y estabilizando el rendimiento del pipeline. En NVIDIA, por ejemplo, la arquitectura de Video Codec SDK describe encoders/decoders de hardware separados del motor CUDA, con el objetivo explícito de liberar recursos para otras operaciones (NVIDIA, s/f-e; NVIDIA Developer, s/f). En Intel, el enfoque equivalente se expone a través de Intel VPL como acceso a hardware especializado para acelerar encode/decode y mejorar FPS respecto a enfoques centrados en CPU (Intel, s/f-b). Asimismo, en Linux, VA-API formaliza el objetivo de habilitar decodificación y codificación aceleradas por hardware como motivación central de la API (Intel, s/f-d).

En términos de latencia, la aceleración por hardware no garantiza por sí sola un tiempo end-to-end bajo; su contribución principal es reducir el costo de las etapas de códec y habilitar arquitecturas donde el flujo se mantiene con buffering controlado y con menor presión sobre CPU/memoria. Por ello, las subsecciones siguientes revisan las alternativas más relevantes (NVDEC/NVENC, Quick Sync/Intel VPL y VA-API) y su impacto en el diseño de pipelines de baja latencia para E-OVRT-VDP.

NVIDIA NVDEC y NVENC. Las GPUs de NVIDIA incorporan un motor dedicado de decodificación (NVDEC) que ejecuta la decodificación independientemente del motor de cómputo/gráficos de la GPU, y expone esta funcionalidad mediante la API NVDECODE (NVIDIA, s/f-d). En consecuencia, la decodificación puede descargarse a hardware fijo mientras el resto del pipeline utiliza la CPU y/o CUDA para tareas de mayor valor (por ejemplo, pre/post-procesamiento e inferencia), reduciendo la contención de recursos en escenarios multi-stream (NVIDIA, s/f-d).

En cuanto a compatibilidad, NVDEC puede decodificar por hardware varios códecs, incluyendo H.264/AVC, HEVC/H.265, VP8, VP9 y AV1; sin embargo, las capacidades exactas dependen de la arquitectura (p. ej., límites de resolución, perfiles y bit-depth), por lo que el diseño debe basarse en una consulta explícita de capacidades en tiempo de ejecución (NVIDIA, s/f-d).

Desde la perspectiva de baja latencia, la API describe un pipeline donde el demultiplexado alimenta un parser que gestiona buffers de decodificación (DPB) y callbacks de entrega. Dos parámetros son particularmente relevantes: (a) el dimensionamiento de superficies de decodificación para garantizar decodificación correcta sin sobre-asignación, y (b) el control de la demora de entrega de frames en orden de presentación mediante ulMaxDisplayDelay, donde 0 indica “sin delay” (NVIDIA, s/f-d). En paralelo, NVIDIA advierte que, en cargas intensivas, la decodificación puede bloquearse si la cola interna de espera del driver asociada a NVDEC se llena, lo que refuerza la necesidad de diseñar el pipeline con control de colas y backpressure para mantener estabilidad temporal (NVIDIA, s/f-d).

Finalmente, cuando el caso de uso requiere codificar (p. ej., para re-streaming, grabación o transcoding), es crítico distinguir la latencia de codificación de la latencia total del sistema. En la guía de integración con FFmpeg, NVIDIA caracteriza un modo de “low latency” en el que se deshabilitan B-frames, se utilizan modos de bitrate constante y se mantienen tamaños de VBV muy bajos, indicando que la latencia “puede ser tan baja como 16 ms” bajo esas restricciones, con el trade-off explícito de menor calidad resultante (NVIDIA, s/f-f).

Intel Quick Sync Video y oneVPL. Los procesadores Intel que incluyen gráficos integrados incorporan capacidades dedicadas de procesamiento de medios comercializadas como Intel Quick Sync Video, orientadas a acelerar tareas de decodificación y codificación de video y, al mismo tiempo, permitir que el procesador ejecute otras cargas (Intel, s/f-a). En consecuencia, Quick Sync constituye una alternativa relevante para sistemas que no disponen de una GPU discreta, siempre que el modelo de CPU efectivamente incluya processor graphics (Intel, s/f-c).

El acceso programático a estas capacidades se realiza mediante Intel oneAPI Video Processing Library (oneVPL). Intel describe a oneVPL como una interfaz para decodificación, codificación y procesamiento de video orientada a construir pipelines portables sobre CPUs, GPUs y otros aceleradores, incorporando además mecanismos de descubrimiento/selección de dispositivo y primitivas de zero-copy buffer sharing (Intel, s/f-b).

Desde la perspectiva de evolución tecnológica, Intel explicita que oneVPL es el sucesor de Intel Media SDK y su continuidad como API 2.x, recomendando oneVPL para desarrollos nuevos y para habilitar características de hardware futuras (Intel, 2021). Respecto del soporte de códecs, resulta incorrecto asumir un conjunto fijo (por ejemplo H.264/HEVC/VP9) para todos los equipos: Intel advierte que las capacidades de códec varían por dispositivo y configuración, y que procesadores sin gráficos integrados no disponen de soporte de medios (Intel, s/f-c). Por ello, un diseño robusto debe basarse en consulta de capacidades (p. ej., tablas y/o mecanismos de enumeración del runtime) y seleccionar dinámicamente el camino de aceleración compatible con el hardware disponible (Intel, 2023; Intel, 2024).

Video Acceleration API (VAAPI). VA-API (Video Acceleration API) es una especificación/API y un ecosistema de implementación en Linux (libva) cuyo objetivo es proporcionar acceso a aceleración por hardware para tareas de decodificación y codificación (y procesamiento asociado) mediante una interfaz común, delegando la ejecución real a backends específicos por proveedor (Intel, 2022). En consecuencia, el valor arquitectónico principal de VA-API es la portabilidad a nivel de interfaz: un mismo componente puede invocar VA-API y utilizar diferentes aceleradores dependiendo del driver/stack disponible, sin reescribir la lógica principal (Intel, 2022).

Sin embargo, esa portabilidad no implica uniformidad funcional: el conjunto de capacidades efectivas (perfiles, bit-depth, resoluciones, códecs y si existe encode/decode completo) depende del backend y del hardware concreto, por lo que un diseño robusto debe tratar a VA-API como una abstracción con variabilidad de features y validar capacidades en el entorno objetivo (Intel, 2022). En términos prácticos, esto se traduce en mayor necesidad de configuración y diagnóstico (selección de driver VA, compatibilidad de formatos/superficies, y verificación de rutas de cero copia dentro del framework), comparado con APIs propietarias donde el vendor controla de punta a punta el stack (Intel, 2022).

En el caso de GPUs AMD en Linux, el soporte suele apoyarse en el stack abierto (Mesa), donde el frontend VA (frontends/va) se integra con rutas de video del driver (radeonsi) asociadas a bloques de decodificación como UVD y VCN, evidenciado por cambios y fixes explícitos en componentes frontends/va y radeonsi/uvd/radeonsi/vcn dentro del release notes de Mesa (Mesa, 2025). En este escenario, VA-API puede ser una opción consistente para despliegues heterogéneos Linux, siempre que el hardware y el driver soporten los códecs/perfiles requeridos y que el pipeline evite conversiones que rompan la ruta acelerada (Mesa, 2025).

Para GPUs NVIDIA, en cambio, VA-API no es el camino primario en el driver propietario en el ecosistema de aplicaciones; por ello aparecen soluciones comunitarias que traducen VA-API hacia NVDEC. En particular, nvidia-vaapi-driver se presenta como una implementación VA-API respaldada por NVDEC, diseñada especialmente para Firefox y con la limitación explícita de decodificación solamente (sin soporte de encoding) (Stephen, 2021/2026). Esta situación es reconocida en discusiones del propio foro de NVIDIA, donde se menciona como “solución” comunitaria con foco en NVDEC y sin NVENC (NVIDIA, 2024).

Impacto en la latencia del sistema. La aceleración por hardware reduce el costo computacional de las etapas de códec, pero la latencia end-to-end del sistema sigue dependiendo del diseño completo del pipeline, incluyendo buffering, conversiones de formato, transferencias de memoria y, especialmente, el tiempo de inferencia (NVIDIA, s/f-f; The FFmpeg developers, s/f-c).

En este marco, suele plantearse como objetivo de diseño minimizar transferencias del host al dispositivo y evitar conversiones que fuercen a “bajar” los frames a memoria del sistema cuando se pretende encadenar decodificación, procesamiento y (si aplica) recodificación. En la práctica, esto se describe como un enfoque “zero-copy” o “hardware pipeline”, pero su factibilidad depende del acelerador disponible (GPU/iGPU/ASIC), de la ruta de procesamiento seleccionada y del framework (por ejemplo, si ciertos filtros o formatos intermedios rompen la continuidad del camino acelerado) (NVIDIA, s/f-f; The FFmpeg developers, s/f-c).


##### 16.5.3.3. Mecanismos de comunicación inter-proceso

La arquitectura modular de una plataforma de analítica de vídeo puede requerir separar etapas del pipeline en procesos distintos (ingesta, inferencia, visualización). En estos escenarios, el mecanismo IPC determina la latencia efectiva: si introduce copias adicionales o sincronización ineficiente, degrada el desempeño end-to-end.

Para transferencia de frames de video, existen alternativas estándar y mecanismos específicos de plataforma que explotan características del hardware subyacente. Las subsecciones siguientes analizan opciones relevantes para E-OVRT-VDP.

DMA-BUF para compartir superficies/buffers entre subsistemas. Cuando intervienen rutas aceleradas (captura por V4L2, composición/DRM, decodificación por hardware), es frecuente que los frames existan como superficies que conviene compartir sin copias entre subsistemas. En Linux, dma-buf provee un marco para compartir buffers con acceso DMA exponiéndolos a userspace como descriptores de archivo, lo cual habilita que dichos buffers se transfieran entre procesos y componentes sin materializar copias a RAM en cada salto (The Linux Kernel, s/f).

No obstante, su aplicabilidad efectiva depende del soporte del driver y del camino de datos disponible en la plataforma objetivo: no todos los dispositivos o decodificadores exportan superficies como dma-buf en todos los entornos.

CUDA Inter-Process Communication (CUDA IPC). En sistemas donde los datos permanecen en memoria de GPU, CUDA IPC permite compartir ciertos recursos entre procesos en Linux, incluyendo el uso de handles para eventos, y, en plataformas compatibles, handles para memoria de dispositivo (NVIDIA, n.d.-b). Este tipo de IPC se alinea con objetivos de baja latencia al evitar transferencias a memoria de host cuando el flujo de datos puede mantenerse en GPU, y ha sido utilizado como técnica de optimización en escenarios de alto rendimiento (Potluri et al., 2012).

Sin embargo, esta elección tiene implicancias directas para plataformas edge basadas en Tegra/Jetson: la guía oficial indica que, en L4T y Tegra embebido, las APIs de IPC para event sharing están soportadas (bajo ciertas condiciones), mientras que las APIs de memory sharing no lo están (NVIDIA, s/f-b). Para un diseño orientado a edge, este punto obliga a tratar CUDA IPC (memoria) como una opción dependiente de plataforma y a contemplar alternativas de interoperabilidad (por ejemplo, mecanismos basados en descriptores o rutas específicas de la plataforma) cuando el hardware objetivo sea Jetson.

Mecanismos específicos de plataforma (DeepStream). Además de IPC genérico, algunos SDKs incorporan componentes diseñados para pipelines multi-proceso dentro de su ecosistema. En el caso de NVIDIA DeepStream (sobre GStreamer), el plugin Gst-nvunixfd se orienta a transferir buffers NVMM entre procesos mediante descriptores, lo que puede simplificar ingeniería en despliegues NVIDIA (NVIDIA, 2024). En una etapa de investigación, estos mecanismos deben compararse contra alternativas estándar (POSIX shm, descriptores por Unix sockets, dma-buf) en términos de portabilidad, costo de integración y restricciones operativas.


##### 16.5.3.4. Frameworks de procesamiento multimedia

El desarrollo de sistemas de análisis de video se beneficia significativamente del uso de frameworks multimedia que proporcionan abstracciones de alto nivel para construcción de pipelines de procesamiento. Estos frameworks encapsulan la complejidad de manejo de buffers, sincronización temporal y negociación de formatos, permitiendo al desarrollador enfocarse en la lógica de aplicación.


###### 16.5.3.4.1. GStreamer

GStreamer es un framework de código abierto para procesamiento multimedia basado en una arquitectura de pipeline donde componentes denominados elementos se conectan formando grafos de flujo de datos (GStreamer, s/f-a). Cada elemento realiza una función específica (fuente, filtro, codificador, sink) y se comunica con otros elementos mediante pads (puertos tipados). Los datos fluyen encapsulados en objetos buffer que contienen el contenido multimedia junto con metadatos temporales, mientras que events y messages proporcionan mecanismos de control y notificación.

La arquitectura de plugins de GStreamer permite extender sus capacidades sin modificar el núcleo del framework. Existen plugins para prácticamente cualquier códec, protocolo o dispositivo, incluyendo soporte para aceleración por hardware mediante componentes específicos para NVDEC, NVENC, VAAPI y Quick Sync. Diversos estudios han analizado su desempeño como framework multimedia en entornos móviles, destacando mejoras en eficiencia, compatibilidad y universalidad frente a otras soluciones (H. Wang et al., 2012).


###### 16.5.3.4.2. FFmpeg y Libav

FFmpeg constituye una colección de bibliotecas y herramientas de línea de comandos para procesamiento de audio y video. Sus componentes principales incluyen libavformat para manejo de formatos contenedores y entrada/salida de streams, libavcodec para codificación y decodificación de cientos de códecs, y libavfilter para filtrado de video y audio. La fortaleza de FFmpeg radica en su extensa cobertura de formatos y códecs, junto con optimizaciones de rendimiento desarrolladas durante más de dos décadas (The FFmpeg developers, s/f-a).

A diferencia de GStreamer, FFmpeg proporciona los bloques fundamentales pero no estructura el flujo de procesamiento por sí mismo; esa responsabilidad recae en el desarrollador. El modelo de programación típico consiste en un loop que demultiplexa paquetes, los decodifica, aplica procesamiento y los recodifica. Esta aproximación más procedural puede resultar apropiada para componentes específicos del sistema pero ofrece menor flexibilidad para orquestación de pipelines complejos comparado con GStreamer.

FFmpeg incluye soporte para aceleración por hardware mediante hwaccel, permitiendo utilizar NVDEC, Quick Sync o VAAPI de manera transparente. La herramienta de línea de comandos puede configurarse con flags de baja latencia para minimizar el buffering interno, aunque alcanzar latencias óptimas requiere configuración cuidadosa.


###### 16.5.3.4.3. NVIDIA DeepStream SDK

DeepStream es un SDK de NVIDIA orientado a video analytics en tiempo real, construido sobre GStreamer. El SDK integra la pila CUDA-X de NVIDIA (decodificación por hardware, inferencia con TensorRT, tracking) como plugins de GStreamer, facilitando la creación de aplicaciones de análisis de video sin requerir integraciones de bajo nivel (NVIDIA, 2024).

Entre los plugins que DeepStream proporciona destacan: nvstreammux, que multiplexa múltiples streams de entrada en un batch unificado para procesamiento eficiente; nvinfer, que ejecuta inferencia de redes neuronales mediante TensorRT; nvtracker, que implementa algoritmos de seguimiento de objetos como DeepSORT; y nvosd, que renderiza elementos gráficos (bounding boxes, texto) sobre los frames. Adicionalmente, DeepStream incluye integraciones con servicios de mensajería (Kafka, MQTT) para reportar eventos detectados, alineándose con el concepto de plano de control.

Estudios de benchmarking en plataformas Jetson demuestran el rendimiento alcanzable con DeepStream. Se han reportado velocidades de inferencia de hasta 47.56 FPS en tareas de detección de anomalías en video ejecutadas completamente en dispositivos Jetson edge (Pham et al., 2024). Asimismo, modelos optimizados con TensorRT exhiben, en promedio, una mejora del 16.11% en velocidad de inferencia respecto de sus contrapartes no optimizadas en Jetson Nano (Swaminathan et al., 2024).


##### 16.5.3.5. Plataformas de hardware para edge computing

La ejecución de analítica de video en el borde (edge computing) se propone como estrategia para reducir la latencia end-to-end y el consumo de ancho de banda, al acercar el cómputo al origen del stream y disminuir la dependencia de la conectividad hacia la nube. Sin embargo, esta decisión no es universalmente superior: su conveniencia depende de condiciones de red, criticidad temporal del caso de uso, costo operativo, y restricciones físicas del despliegue (energía, temperatura, espacio y mantenimiento). En este sentido, la literatura de revisión destaca que la convergencia entre edge computing y deep learning emerge, en gran medida, como respuesta a los costos de transferencia de datos y a la variabilidad de latencia asociados a arquitecturas centradas en nube para cargas sensibles al tiempo (X. Wang et al., 2020a).

En términos de diseño, la “plataforma de hardware” en edge AI no debe entenderse únicamente como capacidad de cómputo (p. ej., TOPS/FLOPS), sino como el conjunto de recursos que determinan el desempeño real del pipeline: decodificación/encodificación por hardware, ancho de banda de memoria, rutas de copia (CPU a GPU), y soporte de runtime y librerías de optimización. También intervienen factores de ingeniería que condicionan resultados en campo (p. ej., thermal throttling, estabilidad del driver, ciclo de vida del producto y disponibilidad de repuestos).

Dentro del espectro de opciones, las plataformas con aceleración integrada para visión (GPU/NPU/DLA) son relevantes cuando el objetivo incluye múltiples flujos concurrentes y presupuesto de latencia acotado. Un ejemplo representativo en esta categoría es la familia NVIDIA Jetson, cuyo stack combina CPU ARM, GPU con soporte CUDA, aceleradores dedicados y motores de códec (NVENC/NVDEC) en módulos orientados a despliegue embebido; su documentación técnica explicita, además, parámetros de arquitectura (p. ej., ancho de banda de memoria) y capacidades de video por hardware que son directamente pertinentes para cargas de video analítico (NVIDIA, 2022).

En paralelo, la evidencia empírica en sistemas Jetson muestra que el rendimiento depende fuertemente de técnicas de optimización y particionamiento del cómputo. Se han reportado mejoras sustanciales de rendimiento y reducciones en el consumo energético respecto de una línea base GPU-only mediante estrategias de pipelining, asignación eficiente de buffers y duplicación de red en un marco basado en TensorRT (Jeong et al., 2022a).

Para evitar sesgos tecnológicos en una etapa de investigación, es recomendable anclar la comparación en suites de benchmarking neutrales y reproducibles. MLCommons mantiene MLPerf Inference, que incluye escenarios para sistemas de edge y publica resultados con metodología estandarizada y reproducible, abarcando distintos perfiles de despliegue (por ejemplo, medidas de latencia en SingleStream y capacidad bajo carga en escenarios de concurrencia) (MLCommons, s/f-a). En ese marco, existen resultados públicos de múltiples organizaciones y stacks (incluyendo proveedores y arquitecturas variadas), lo que permite contextualizar el rendimiento de una plataforma sin asumir equivalencia directa con el desempeño del sistema completo de videovigilancia (MLCommons, 2024). Complementariamente, fabricantes como NVIDIA agregan y referencian sus propias presentaciones de resultados en la categoría Edge de MLPerf, lo cual puede ser útil como insumo técnico siempre que se mantenga la comparación con la fuente neutral (MLCommons) y se expliciten las condiciones de ejecución (software stack, versión de TensorRT/CUDA, modo de potencia, etc.) (NVIDIA, s/f-b).


#### 16.5.4. Computación en el borde para video analytics en tiempo real

Los sistemas de análisis de video en tiempo real que emplean modelos de aprendizaje profundo enfrentan una tensión fundamental entre la carga computacional de la inferencia y los requisitos de latencia del pipeline. En arquitecturas centralizadas basadas en la nube, los fotogramas capturados en el punto de origen deben transportarse a centros de datos remotos para su procesamiento, lo que introduce latencias de red variables, dependencia de la conectividad externa y potenciales implicaciones de privacidad al transmitir imágenes fuera del perímetro local (Shi et al., 2016b).

El edge computing —cómputo en o cerca de la fuente de datos— surge como respuesta a estas limitaciones, acercando la capacidad de procesamiento al punto de captura para reducir la latencia de ida y vuelta, aliviar el consumo de ancho de banda y mantener los datos sensibles dentro del entorno local. Esta aproximación resulta especialmente relevante cuando los modelos de inferencia son computacionalmente intensivos, como ocurre con las arquitecturas de detección basadas en visión-lenguaje (open-vocabulary detection), cuyo costo por fotograma es significativamente mayor que el de los detectores tradicionales de vocabulario cerrado. En estos escenarios, la decisión de qué etapas del pipeline ejecutar en el borde y cuáles delegar a infraestructura remota se convierte en un problema de diseño central, condicionado por factores como el presupuesto de latencia, el ancho de banda disponible, la carga de inferencia del modelo y las restricciones energéticas y térmicas del hardware local.

Esta sección examina la taxonomía edge/fog/cloud, los patrones de despliegue reportados para deep learning en el borde y los criterios técnicos que orientan la distribución del cómputo en sistemas de video analytics sensibles a la latencia.


##### 16.5.4.1. Fundamentos de Edge Computing

El paradigma de edge computing traslada recursos de cómputo y almacenamiento desde centros de datos centralizados hacia la periferia de la red, ubicándolos en proximidad física y de red a las fuentes de datos. Se caracteriza por ser una forma de ofrecer capacidades tipo cloud con alta capacidad de respuesta mediante infraestructura situada a muy pocos saltos de red de los dispositivos finales, lo que resulta crítico cuando los retardos de ida y vuelta hacia datacenters remotos degradan la viabilidad operativa de aplicaciones sensibles a la latencia (Satyanarayanan, 2017).

Las motivaciones clásicas para su adopción se apoyan en tres tensiones estructurales: (i) la proliferación de dispositivos conectados y el volumen de datos generados, (ii) los requerimientos de baja latencia incompatibles con el procesamiento remoto, y (iii) la necesidad de limitar la exposición de datos sensibles. Estas fuerzas proponen desafíos de investigación como la programabilidad para entornos heterogéneos, la seguridad y privacidad en nodos distribuidos, la gestión de recursos y el equilibrio edge–cloud (Shi et al., 2016b).

En paralelo, la convergencia entre edge computing y aprendizaje profundo dio lugar al concepto de edge intelligence, es decir, el despliegue de servicios de deep learning en el borde para responder con menor latencia y reducir el consumo de ancho de banda, manteniendo datos sensibles cerca de su origen. Sin embargo, esta convergencia también expone un límite técnico, donde los modelos visión‑lenguaje y de vocabulario abierto, si bien habilitan generalización semántica, demandan cómputo y ancho de banda de memoria difíciles de sostener en dispositivos embebidos, generando un “cuello de botella” de percepción incluso sobre hardware edge avanzado. Este concepto será ampliado en secciones posteriores.


##### 16.5.4.2. Taxonomía: Edge, Fog y Cloud Computing

La computación distribuida contemporánea suele describirse como un continuum que va desde los dispositivos que generan los datos (p. ej., cámaras y gateways) hasta centros de datos centralizados. Esta taxonomía es útil para razonar sobre video analytics porque permite ubicar, de forma comparativa, dónde se ejecuta el cómputo (y por ende qué latencias, consumos de red y restricciones operativas se heredan). En la literatura, los términos edge y fog no siempre se usan con el mismo alcance: algunos trabajos los tratan como sinónimos o con fronteras difusas, mientras que otros proponen una jerarquía explícita entre "cercano al dispositivo" (edge) y "capa intermedia de agregación" (fog) (Yousefpour et al., 2019).


###### 16.5.4.2.1. Cloud Computing

El modelo de cloud computing se caracteriza por concentrar recursos computacionales en centros de datos accesibles mediante red y provistos bajo demanda. La definición de NIST describe la nube como un modelo para habilitar acceso ubicuo y bajo demanda a un pool compartido de recursos configurables que pueden aprovisionarse y liberarse con mínima gestión, junto con cinco características esenciales (autoservicio bajo demanda, acceso amplio por red, pooling de recursos, elasticidad rápida y servicio medido), tres modelos de servicio (SaaS, PaaS, IaaS) y cuatro modelos de despliegue (Mell & Grance, 2011).

Desde una perspectiva aplicada a analítica de video, la nube ofrece ventajas como elasticidad, centralización del almacenamiento y acceso a hardware de alto desempeño. De igual manera, también introduce limitaciones típicas para escenarios de tiempo real la ruta de red hacia un datacenter puede sumar latencias variables y exigir un consumo de ancho de banda elevado si se transmiten flujos de video completos, además de ampliar la superficie de exposición de datos sensibles cuando abandonan el perímetro local. Encuestas sobre edge intelligence y despliegue de deep learning en el borde remarcan que un enfoque cloud-only puede ser inadecuado para aplicaciones con requerimientos estrictos de respuesta, debido a los costos de comunicación, la variabilidad de la red y las restricciones operativas asociadas (X. Wang et al., 2020b; Zhou et al., 2019).


###### 16.5.4.2.2. Fog Computing

El concepto de fog computing surge para describir arquitecturas donde el cómputo, el almacenamiento y las funciones de red se distribuyen entre los dispositivos finales y la nube, habilitando procesamiento cercano a la fuente con menor latencia. Puede considerarse como una extensión del paradigma cloud hacia el borde, destacando atributos como baja latencia y conciencia de ubicación, distribución geográfica, soporte para aplicaciones de streaming en tiempo real y heterogeneidad de nodos (Bonomi et al., 2012).

El NIST, por su parte, define fog computing como un paradigma que extiende la nube hacia el extremo de la red, ubicando recursos más cerca de las fuentes de datos y actuadores, y advierte que, en la práctica, la terminología relacionada (incluyendo edge) presenta solapamientos y usos no uniformes, por lo que resulta recomendable explicitar la convención adoptada en cada trabajo (Iorga et al., 2018). En la misma línea, la OpenFog Reference Architecture conceptualiza fog como una arquitectura horizontal que distribuye capacidades de cómputo, almacenamiento, control y networking a lo largo del continuo cloud-to-things, enfatizando principios como seguridad, autonomía, escalabilidad y jerarquía (OpenFog Consortium, 2017).

En términos aplicados a video analytics, fog suele describirse como una capa intermedia capaz de agregar múltiples flujos, filtrar o transformar datos antes de su envío a niveles superiores y coordinar políticas operativas (p. ej., QoS, buffering, priorización), enviando hacia la nube preferentemente resultados, metadatos o eventos en lugar de video crudo cuando el caso de uso lo permite. Este espacio queda sintetizado en una taxonomía de desafíos recurrentes —gestión de recursos, QoS, seguridad/privacidad y soporte a aplicaciones— resaltando el rol del fog en analítica cercana a la fuente para aplicaciones sensibles a latencia (Mahmud et al., 2018).


###### 16.5.4.2.3. Edge Computing

A partir de la distinción conceptual entre cloud, fog y edge desarrollada en esta sección, el término edge computing se reserva aquí para el cómputo ubicado en el dispositivo, en el gateway inmediato o en un servidor de borde próximo a la fuente de video. En este marco, se distinguen patrones de despliegue que ayudan a clarificar su uso en escenarios prácticos: (a) inferencia en el dispositivo (on-device), (b) inferencia asistida por un servidor de borde (edge server) cercano y (c) arquitecturas colaborativas o híbridas, donde el cómputo se distribuye o particiona entre dispositivo, edge y/o cloud, con decisiones guiadas por compromisos entre latencia, consumo energético y capacidad disponible (Chen & Ran, 2019). Dada la variabilidad terminológica del área, en este trabajo se adopta la siguiente convención: edge refiere al cómputo en el dispositivo o gateway inmediato; fog, a una capa intermedia de agregación cercana o regional; y cloud, a centros de datos centralizados. Esta distinción resulta necesaria porque la literatura sobre fog computing y paradigmas relacionados —como cloudlets, MEC o mist computing— documenta solapamientos conceptuales y usos no uniformes de estos términos (Yousefpour et al., 2019).


##### 16.5.4.3. Edge Computing para Video Analytics

El video analytics en vivo suele considerarse un caso emblemático para el edge computing debido a la combinación de requisitos de baja latencia, altas tasas de datos y alto costo computacional de los pipelines de visión (decodificación, detección, seguimiento y analítica posterior). Para video analytics en tiempo real y a gran escala, resulta necesario un enfoque geo‑distribuido que incorpore recursos de cómputo cerca de las cámaras, además de clusters privados y/o nubes públicas. Esto se apoya en tres cuestiones técnicas: (i) latencia, ya que muchas aplicaciones requieren respuestas por debajo del segundo y algunas llegan a decenas de milisegundos; (ii) ancho de banda, dado que incluso video comprimido en HD suele ubicarse en el orden de varios megabits por segundo por flujo y puede escalar a decenas de megabits en 4K, dependiendo del códec, la tasa de cuadros y la complejidad de la escena, lo que vuelve rápidamente inviable transmitir masivamente flujos crudos a ubicaciones remotas; y (iii) aprovisionamiento, donde filtrar o procesar cerca del origen puede reducir el consumo de recursos aguas abajo (Ananthanarayanan et al., 2017).

Desde la perspectiva de sistemas, la dificultad no es sólo correr modelos, sino administrar recursos en escenarios con múltiples streams y cargas variables. En analítica de video a escala, la gestión eficiente depende de reconocer (a) el trade‑off recurso–calidad (p. ej., variando resolución, FPS y parámetros internos) y (b) la diversidad de objetivos de calidad y tolerancia al lag entre consultas, ya que algunas deben responder con bajo retardo, mientras que otras admiten demoras de segundos o minutos (Zhang et al., 2017). La carga puede fluctuar por picos en la escena (por ejemplo, aumento de objetos a seguir), lo que vuelve relevante el aprovisionamiento dinámico y las políticas de scheduling orientadas a objetivos (calidad/lag), más allá del reparto “justo” de recursos.

En cuanto a dominios de aplicación, se propone el uso de Edge‑AI en video analytics para ciudades inteligentes, casos como seguridad y vigilancia, transporte y gestión del tráfico, salud, educación y entretenimiento (Badidi et al., 2023). En este marco, el edge (y/o fog) habilita que parte del procesamiento ocurra más cerca de donde se generan los datos, lo que típicamente se asocia con menor latencia y ahorro de ancho de banda, y además abre espacio para técnicas de preservación de privacidad al minimizar la exposición de video crudo fuera del perímetro local.

Finalmente, la convergencia entre edge computing y deep learning suele justificarse porque ni el cloud‑only (por latencia/costos de transporte) ni el on‑device‑only (por capacidad limitada) resultan suficientes para muchas aplicaciones de IA en el borde. El edge permite desplazar el procesamiento hacia la cercanía de los datos, reduciendo latencia, mientras que los avances en deep learning habilitan aplicaciones intensivas como multimedia inteligente y vigilancia, a costa de nuevos desafíos de eficiencia y despliegue (X. Wang et al., 2020b).


##### 16.5.4.4. Plataformas de Hardware para Inferencia en el Borde

La ejecución de modelos de deep learning en el borde requiere capacidad de cómputo sostenida bajo restricciones de consumo energético, disipación térmica y factor de forma. En cargas de video analytics, además, el desempeño efectivo no depende sólo de la inferencia, sino del pipeline completo (decodificación/transferencias del CPU al acelerador, preprocesamiento, inferencia y posprocesamiento), donde el ancho de banda de memoria, las rutas de copia y el soporte de runtimes/optimizadores influyen materialmente en la latencia y el throughput observados (X. Wang et al., 2020b).


###### 16.5.4.4.1. Categorías de aceleradores

La literatura y el mercado de Edge AI describen varias familias de hardware para inferencia (Silvano et al., 2025):

GPUs embebidas (SoC/Modules): integran CPU y GPU en módulos compactos orientados a despliegue embebido/industrial. Su ventaja es la flexibilidad (soportan múltiples frameworks) y el acceso a toolchains maduras de optimización (p. ej., TensorRT).

ASICs/NPU/TPU de borde: aceleradores dedicados a operaciones típicas de redes neuronales, con énfasis en eficiencia energética. Suelen requerir modelos compilados o convertidos a formatos específicos (p. ej., TensorFlow Lite cuantizado en Edge TPU).

Aceleradores especializados (p. ej., NPUs de terceros): chips de inferencia con toolchains propias (compilación, cuantización, kernels soportados), que pueden ofrecer eficiencia elevada, pero condicionan portabilidad y selección de modelos.

FPGAs con DPU (Deep Learning Processor Unit): permiten implementar datapaths dedicados y optimizar latencias de manera controlada; su atractivo está en la personalización y en perfiles donde el determinismo/latencia es relevante. En ecosistemas AMD/Xilinx, el término DPU es un soft IP para inferencia dentro del flujo Vitis AI.

En la práctica, muchas plataformas combinan capacidades heterogéneas (CPU + acelerador) y el rendimiento real depende de cómo el software reparte el cómputo y minimiza copias/movimientos de datos (Shuvo et al., 2023).


###### 16.5.4.4.2. Métricas de evaluación y comparabilidad

Para comparar plataformas edge AI de forma técnicamente defendible, la evaluación suele considerar:

Throughput: FPS o “streams simultáneos” sostenibles bajo una configuración dada (resolución, códec, tamaño de lote, precisión numérica).

Latencia: tiempo por fotograma y, especialmente, cola (p95/p99) y jitter, dado que aplicaciones de tiempo real suelen degradarse por picos más que por promedios.

Eficiencia energética: potencia media (W) y/o energía por inferencia (J/frame), útil para contrastar desempeño bajo límites térmicos/energéticos.

Memoria y bandwidth: capacidad y presión de memoria, y costo de transferencias entre CPU y acelerador.

Estabilidad térmica: riesgo de thermal throttling y degradación bajo carga sostenida.

Un punto crítico es que métricas “brutas” como TOPS no siempre son comparables entre fabricantes, porque dependen del tipo de operación (INT8/FP16), sparsity y condiciones de medición. Por ello, se recomienda complementar con suites estandarizadas y reproducibles: MLPerf Inference define reglas y escenarios (p. ej., SingleStream para latencia y Offline para throughput), buscando comparabilidad entre stacks heterogéneos (MLCommons, s/f-b; Reddi et al., 2020).


###### 16.5.4.4.3. Evidencia empírica y estudios comparativos

La evidencia experimental en edge AI muestra que el rendimiento resulta de la interacción hardware, optimización y stack:

Una comparación de plataformas de Edge AI para detección de objetos basadas en YOLOv5 muestra diferencias sustanciales de desempeño entre configuraciones destacando que el balance rendimiento/energía depende fuertemente de la plataforma y de las condiciones de operación (consumo de potencia y estabilidad térmica), por lo que la comparación debe reportar explícitamente estas variables junto con los FPS (Minott et al., 2025).

Otro benchmarking de plataformas heterogéneas para detección en el borde (GPU embebida, TPU y DPU/FPGA) muestra que el desempeño observado depende de forma material de la adaptación del modelo al hardware objetivo (p. ej., conversión, compilación y despliegue específico por acelerador), por lo que la comparación debe reportar explícitamente el stack y el pipeline utilizado. Las diferencias de throughput entre arquitecturas resultan marcadas bajo condiciones experimentales comparables, reforzando la necesidad de medir el pipeline completo y no sólo el “hardware nominal” (Magalhães et al., 2023).

Jeong, Kim y Ha (2022) presentan un framework sobre TensorRT para plataformas Jetson con procesamiento heterogéneo (p. ej., combinación de CPU/GPU/NPU) y reportan mejoras sustanciales de desempeño (del orden de 101 %–680 %) junto con reducciones de energía de hasta 55 % respecto de una línea base ejecutada sólo en GPU, mediante estrategias como multithreading, pipelining, asignación de buffers y duplicación de red. Esto refuerza que, en inferencia en el borde, el rendimiento observado depende tanto del hardware como del stack de ejecución y la optimización del pipeline (Jeong et al., 2022b).

En conjunto, estos resultados apoyan una idea recurrente en la literatura de benchmarking donde, para cargas de visión, la comparación más fiel surge de medir el pipeline completo bajo condiciones reproducibles y reportar explícitamente software, versiones, precisión y modos de potencia.


###### 16.5.4.4.4. Ejemplos representativos de la industria

A modo ilustrativo, el ecosistema actual ofrece familias de productos representativas de cada categoría:

GPUs embebidas: plataformas tipo NVIDIA Jetson, apoyadas por un stack de software embebido (p. ej., JetPack) y toolchains de despliegue/optimización (p. ej., TensorRT), con soporte documentado para frameworks de deep learning (p. ej., PyTorch) y SDKs orientados a video analytics (p. ej., DeepStream) (NVIDIA, s/f-a, s/f-c, 2025).

TPU/NPU de borde: Google Coral Edge TPU, orientada a inferencia eficiente con modelos compatibles (típicamente TFLite cuantizado).

Aceleradores ASIC especializados: familias como Hailo, que apuntan a alta eficiencia para inferencia en el borde mediante toolchains propios.

FPGA + DPU (Deep Learning Processor Unit): plataformas AMD/Xilinx con flujos Vitis AI, orientadas a integrar inferencia acelerada en diseños embebidos con configuraciones adaptables.


#### 16.5.5. Criterios orientadores para la selección de protocolos y stacks de streaming

El análisis del estado del arte realizado en las secciones precedentes permite identificar un conjunto de criterios técnicos que deberán orientar la evaluación de protocolos de transmisión, servidores de medios, frameworks de procesamiento y plataformas de ejecución en etapas posteriores del proyecto. Estos criterios emergen de la intersección entre las características observadas en las familias de protocolos, los compromisos documentados en la literatura sobre arquitecturas de procesamiento de video, y los requisitos generales de una plataforma experimental orientada a detección open-vocabulary en tiempo real.

La formulación de criterios no anticipa decisiones de diseño ni establece preferencia por tecnologías concretas: su propósito es delimitar ejes de evaluación que permitan contrastar alternativas de manera sistemática durante las etapas de análisis metodológico, diseño arquitectónico e implementación, preservando la apertura necesaria para que cada decisión se sustente en evidencia empírica y no en supuestos teóricos aislados.


##### 16.5.5.1. Criterios derivados del análisis teórico

Se identifican siete ejes de evaluación relevantes para la selección futura de componentes del plano de medios en el contexto de sistemas de video analytics en tiempo real.


###### 16.5.5.1.1. Latencia end-to-end como variable de diseño

El análisis demostró que la latencia en sistemas de video en tiempo real no constituye una propiedad singular, sino una magnitud compuesta determinada por la contribución acumulada de cada etapa del pipeline estándar de streaming.

Como se estableció anteriormente, la literatura sobre interacción humano-computadora sitúa los umbrales de interactividad para escenarios human-in-the-loop en el orden de las centenas de milisegundos (Card et al., 2008; Deber et al., 2015). Este hallazgo acota el rango de referencia, pero la adopción de un presupuesto de latencia específico como requisito operativo del sistema constituye una decisión que deberá formalizarse durante la etapa 2 del proyecto, considerando las restricciones concretas de hardware, conectividad y carga de inferencia del prototipo. En consecuencia, la evaluación de stacks candidatos deberá contemplar la latencia end-to-end como una variable de diseño cuyo umbral queda por definir, y no como un parámetro fijo predeterminado.

Asimismo, la evaluación debería atender a la distribución estadística de las latencias y no únicamente a promedios, dado que colas largas o jitter elevado pueden comprometer la consistencia temporal de las detecciones. En particular, reportar métricas de dispersión o percentiles sobre la latencia end-to-end —y, cuando resulte instrumentalmente viable, del componente de inferencia— permitiría capturar el comportamiento bajo carga de manera más representativa que un promedio aislado.


###### 16.5.5.1.2. Compatibilidad con fuentes heterogéneas y soporte multi-protocolo

En entornos reales de videovigilancia en construcción civil, es esperable que el parque de cámaras instalado sea heterogéneo, con predominancia de dispositivos que exponen flujos mediante protocolos establecidos como RTSP que se integran bajo perfiles ONVIF (ONVIF, 2019; Schulzrinne et al., 1998). La capacidad de un stack candidato para ingestar flujos desde estas fuentes sin imponer la sustitución del equipamiento existente constituye un factor relevante de evaluación.

El soporte multi-protocolo no implica necesariamente utilizar todos los protocolos disponibles de manera simultánea, sino habilitar roles diferenciados según el tramo del pipeline (García et al., 2017). La evaluación de alternativas deberá considerar hasta qué punto cada opción permite incorporar fuentes diversas sin comprometer la coherencia interna del plano de medios ni introducir dependencias rígidas con un protocolo específico.


###### 16.5.5.1.3. Eficiencia en la gestión de buffers y transferencias de memoria

El análisis puso de manifiesto que la forma en que los frames transitan entre las etapas de decodificación, preprocesamiento e inferencia tiene impacto directo sobre la latencia y el throughput del pipeline. En particular, la capacidad de preservar frames en memoria del acelerador y evitar copias innecesarias hacia la RAM del host aparece en la literatura como un factor determinante del desempeño en plataformas con aceleración por GPU (NVIDIA, s/f-b).

Para la evaluación de alternativas, este eje se traduce en verificar si el stack candidato permite que los frames permanezcan en memoria del acelerador a lo largo de la ruta crítica, o si introduce copias o conversiones de formato entre etapas. La operación en modo zero-copy no debe asumirse como propiedad garantizada de ningún stack, sino considerarse como una característica a confirmar en función de la combinación concreta de framework, códec y acelerador disponibles para el prototipo (NVIDIA, s/f-d; FFmpeg, s/f-b).


###### 16.5.5.1.4. Capacidad de abstracción sobre códec y aceleración por hardware

Dado el carácter experimental del proyecto, resulta conveniente que el framework de procesamiento multimedia que se adopte para el plano de medios permita modificar parámetros de códec y aceleración por hardware sin requerir cambios estructurales en la lógica de aplicación ni en el pipeline de detección. Como se discutió en la sección 16.5.3.4, los frameworks difieren en la forma en que exponen estas configuraciones: algunos permiten ajustarlas de forma declarativa, mientras que otros requieren adaptaciones específicas por plataforma (GStreamer, s/f-a; FFmpeg, s/f-b). Este aspecto se considerará como criterio complementario en la evaluación de frameworks candidatos para el plano de medios, priorizando la flexibilidad de configuración sobre la portabilidad multiplataforma, que excede el alcance del prototipo.


###### 16.5.5.1.5. Separabilidad entre flujo de datos y lógica de control

La separación entre plano de medios y plano de control constituye un principio arquitectónico recurrente en la literatura de sistemas de video analytics que combinan procesamiento de baja latencia con lógica de negocio event-driven (Bass et al., 2022; Cugola & Margara, 2012). En la evaluación de componentes candidatos para el plano de medios, resulta pertinente considerar si estos exponen mecanismos que faciliten dicha separación —como buses de mensajes, callbacks o interfaces de eventos— o si, por el contrario, acoplan el flujo de datos con la lógica de control en una misma ruta de ejecución.

Este criterio no prescribe un mecanismo de comunicación particular ni una topología concreta, sino que plantea la separabilidad de planos como una dimensión de análisis al contrastar alternativas. El grado de desacoplamiento efectivamente necesario y su implementación corresponden al diseño arquitectónico de la Etapa 3.


###### 16.5.5.1.6. Viabilidad de integración con modelos de inferencia open-vocabulary

Un aspecto central para el proyecto es la capacidad del pipeline de medios para articularse con modelos de detección open-vocabulary. Como se analizó en la sección 16.5.3.4, los frameworks de procesamiento multimedia pueden adoptar enfoques diferenciados de integración: incorporar la inferencia como una etapa interna del pipeline o extraer frames hacia un proceso externo que ejecute el modelo de forma desacoplada. Cada enfoque implica compromisos distintos en latencia, complejidad operativa y flexibilidad para sustituir o actualizar modelos.

Dado que los modelos OVD incorporan componentes de fusión visión-lenguaje, la evaluación deberá prestar atención a barreras de integración específicas, en particular la compatibilidad con arquitecturas que combinan un encoder visual con un encoder textual y requieren mecanismos de inyección de prompts en lenguaje natural. La viabilidad y el costo de estas integraciones constituyen variables abiertas cuya resolución dependerá de pruebas empíricas en etapas posteriores.


###### 16.5.5.1.7. Afinidad con procesamiento cercano a la fuente

Del análisis se identificó que las condiciones típicas de obras de construcción civil —necesidad de respuesta rápida ante eventos de seguridad, conectividad potencialmente intermitente, consideraciones de privacidad— configuran un escenario donde el procesamiento cercano a la fuente de captura podría resultar ventajoso (Lee & Hsieh, 2026; Kotevska et al., 2022). La evaluación de alternativas deberá considerar hasta qué punto cada stack candidato resulta desplegable en entornos de borde con recursos acotados, y en qué medida permite una partición flexible entre funciones locales y funciones que podrían ubicarse en niveles fog o cloud (Iorga et al., 2018).

Este criterio se formula como dimensión de evaluación y no como decisión de arquitectura: la conveniencia de un enfoque edge-first, la definición del límite entre procesamiento local y remoto, y la selección de la plataforma de hardware asociada constituyen decisiones que deberán sustentarse en la evaluación empírica del prototipo, considerando restricciones de costo, disponibilidad y carga de inferencia.


##### 16.5.5.2. Consideraciones complementarias

Además de los criterios formulados en la sección anterior, la evaluación de alternativas se beneficiará de considerar la facilidad de instrumentación que cada framework ofrezca: la posibilidad de obtener métricas operativas básicas —tasa de frames, latencia end-to-end, uso de recursos del acelerador— sin requerir instrumentación manual extensiva, lo cual constituye un factor práctico que puede incidir en la eficiencia del trabajo experimental.

Los criterios enunciados no determinan una selección única de tecnologías, sino que definen un espacio de soluciones factibles dentro del cual deberán evaluarse alternativas concretas durante las etapas de análisis metodológico, diseño arquitectónico e implementación. El análisis teórico realizado en las secciones precedentes sugiere que existen múltiples combinaciones de frameworks, servidores de medios y protocolos capaces de satisfacer subconjuntos de los requisitos identificados, con diferentes compromisos entre flexibilidad, complejidad operativa y costo de integración.


### 16.6. Marco ético-legal para el análisis automatizado de video en entornos laborales

Un sistema técnicamente correcto puede ser, al mismo tiempo, normativamente inadmisible. El análisis de video en entornos laborales involucra el tratamiento de imágenes de personas que no controlan el sistema, desconocen sus detalles técnicos y pueden verse afectadas por sus errores. Esa asimetría no se resuelve declarando que el propósito es preventivo: exige condiciones sustantivas sobre qué datos se capturan, cómo se almacenan, quién accede a ellos y cómo se comunican los resultados. En Argentina, ese conjunto de condiciones tiene base normativa concreta. Esta sección sistematiza ese marco, identifica las restricciones de diseño que se derivan de él y establece los principios que deben orientar las decisiones de arquitectura y operación del sistema E-OVRT-VDP.

El despliegue de sistemas de visión por computadora en contextos de videovigilancia introduce desafíos que exceden lo meramente técnico, en tanto involucra el tratamiento de imágenes que pueden constituir datos personales y afectar derechos fundamentales. En entornos laborales, y particularmente en obras de construcción, la captura y análisis automatizado de video mediante modelos de inteligencia artificial requiere un encuadre normativo y ético que delimite condiciones de licitud, proporcionalidad y seguridad, además de establecer criterios de transparencia, responsabilidad y control sobre el ciclo de vida de los datos. Este marco permite comprender qué obligaciones y principios deben considerarse para evaluar y documentar el uso responsable de analítica visual, especialmente en escenarios donde se procura minimizar el impacto sobre las personas mediante decisiones de diseño como la no identificación individual y el carácter asistivo de las alertas.


#### 16.6.1. El problema de la legitimidad en la vigilancia asistida por IA

El despliegue de sistemas de visión por computadora en entornos laborales introduce una asimetría estructural que no existe en otros contextos de aplicación de la IA: el sujeto de análisis —el trabajador— no controla el sistema, raramente conoce sus detalles técnicos, y puede sufrir consecuencias derivadas de errores o interpretaciones automatizadas sobre su comportamiento o condiciones de trabajo. Esta asimetría no se resuelve simplemente declarando que el sistema tiene fines preventivos: la legitimidad del despliegue depende de condiciones sustantivas relacionadas con la finalidad real del tratamiento, la proporcionalidad de los medios respecto del fin, la transparencia hacia los titulares de los datos, y la existencia de mecanismos de supervisión y rendición de cuentas que impidan la expansión funcional del sistema más allá de sus objetivos declarados (Organisation for Economic Co-operation and Development, 2019; United Nations Educational, 2021).

La distinción entre un sistema de monitoreo de seguridad laboral y un sistema de vigilancia generalizada no es técnica sino normativa y ética: ambos pueden compartir la misma arquitectura, los mismos modelos y protocolos, pero se diferencian en las garantías organizacionales y jurídicas que rodean su operación. Esta distinción tiene consecuencias directas para el diseño del sistema E-OVRT-VDP: decisiones aparentemente técnicas —qué datos almacenar, por cuánto tiempo, quién puede acceder a ellos, cómo se generan y comunican las alertas— son en realidad decisiones de gobernanza que determinan si el sistema opera dentro o fuera de los parámetros de legitimidad que la normativa y la ética imponen.


#### 16.6.2. Delimitación del tratamiento de datos en sistemas de visión por computadora

Los sistemas de visión por computadora aplicados a entornos laborales suelen apoyarse en flujos continuos de imágenes para identificar objetos, personas y condiciones de trabajo. Desde una perspectiva jurídico-técnica, este tipo de información no se agota en su dimensión “visual”: en muchos escenarios, una imagen constituye un dato personal en la medida en que permite identificar, directa o indirectamente, a una persona o hacerla identificable a partir de asociaciones razonables con otros datos disponibles (Agencia de Acceso a la Información Pública, s/f-a; Argentina, 2000). En consecuencia, aun cuando el objetivo operativo del sistema sea la prevención de riesgos, la captación y el análisis de video pueden configurar un tratamiento de datos personales sujeto a obligaciones específicas.

En un caso de uso típico de obra —videovigilancia con analítica basada en IA— el tratamiento involucra, como mínimo, (i) la recolección (captura por cámaras), (ii) el almacenamiento o transmisión del flujo, (iii) el análisis automatizado (inferencia) y (iv) la generación de salidas (alertas, registros, reportes). Cada una de estas etapas puede incrementar o reducir el impacto sobre la privacidad, según se adopten medidas de minimización, segmentación funcional y control de acceso. Este encuadre es relevante porque la protección de datos personales se estructura en torno a la finalidad y a la proporcionalidad del tratamiento: no basta con que el objetivo sea legítimo, sino que el diseño del sistema debe evitar captaciones y usos innecesarios o excesivos para el fin perseguido (Argentina, 2000; European Data Protection Board, 2020).

En el plano organizacional, el régimen de protección de datos distingue roles con responsabilidades diferenciadas. Quien determina los fines y medios del tratamiento asume el carácter de responsable del banco de datos, mientras que terceros que procesan información por cuenta del responsable actúan como encargados o prestadores de servicios. Esta distinción resulta central en soluciones tecnológicas que integran proveedores de infraestructura, plataformas de análisis o servicios en la nube, ya que exige definir obligaciones contractuales, medidas de seguridad y límites de uso coherentes con la finalidad declarada (Argentina, 2000, 2001).


##### 16.6.2.1. Régimen argentino de protección de datos aplicable a imágenes y videovigilancia

En Argentina, el tratamiento de datos personales se rige por la Ley 25.326 de Protección de los Datos Personales y su reglamentación mediante el Decreto 1558/2001 (Argentina, 2000, 2001). El marco establece que los datos deben ser recolectados para fines determinados, explícitos y legítimos, y que su tratamiento no puede desviarse de esos fines. Los principios de calidad y proporcionalidad imponen que la información sea adecuada, pertinente y no excesiva en relación con la finalidad declarada (Argentina, 2000).

La Ley 25.326 define como dato personal toda información referida a personas determinadas o determinables (Argentina, 2000). Esta definición tiene implicaciones operativas directas: una imagen puede identificar a una persona de manera directa por sus rasgos físicos, o de manera indirecta por la combinación con metadatos como hora, zona de obra, turno de trabajo o secuencia de posiciones. De allí que, aun cuando el sistema excluya explícitamente el reconocimiento facial, el análisis de impacto sobre la privacidad no puede limitarse a las salidas directas del modelo: debe considerar la identificabilidad global que emerge del ecosistema de datos que el sistema genera y almacena (Agencia de Acceso a la Información Pública, s/f-a; Argentina, 2000).

El régimen también garantiza derechos de los titulares —como acceso, rectificación, actualización y supresión— y prevé la vía constitucional del habeas data para proteger la intimidad y controlar el uso de la información personal. Estas garantías son relevantes en escenarios de videovigilancia, donde el titular puede desconocer el alcance de la captación, la duración de conservación o los destinatarios de la información. Por ello, la transparencia y la trazabilidad del tratamiento se vuelven condiciones prácticas para que los derechos no queden meramente formales (Agencia de Acceso a la Información Pública, s/f-a; Argentina, 2000).


##### 16.6.2.2. Disposición 10/2015

La Disposición 10/2015 de la Dirección Nacional de Protección de Datos Personales —hoy bajo la órbita de la Agencia de Acceso a la Información Pública (AAIP)— constituye el principal instrumento reglamentario específico para sistemas de videovigilancia en Argentina. Su función es operacionalizar los principios generales de la Ley 25.326 en el contexto de la captación sistemática de imágenes, traduciendo los principios de licitud, finalidad, proporcionalidad, transparencia y seguridad en criterios prácticos de diseño e implementación (Argentina, 2015).

Las condiciones de licitud más relevantes que establece la Disposición 10/2015 se organizan en tres ejes. El primero es el requisito de información previa al titular del dato, que puede cumplirse mediante cartelería visible que informe la existencia de dispositivos de captación, la finalidad del tratamiento y los datos de contacto del responsable para el ejercicio de derechos (Argentina, 2015). El segundo es la exigencia de contar con un manual o política de tratamiento de datos personales que defina finalidades, responsables, procedimientos de gestión, mecanismos de seguridad, criterios de conservación y pautas de acceso y divulgación (Argentina, 2015); este manual opera como el instrumento que vincula el diseño técnico del sistema con el cumplimiento normativo. El tercero es la obligación de inscribir las bases de datos de videovigilancia ante la AAIP, acompañando la solicitud con el manual de tratamiento (Agencia de Acceso a la Información Pública, s/f-b), requisito aplicable a todo despliegue que involucre personas en el campo visual de las cámaras.

Este requerimiento no se reduce a una formalidad administrativa: contribuye a que la videovigilancia sea gestionada como un tratamiento regulado, con trazabilidad, y no como un recurso técnico difuso susceptible de ampliarse por inercia a nuevos fines.


#### 16.6.3. Medidas de seguridad y protección de la información

Una vez establecidos los requisitos de licitud, transparencia y delimitación de finalidades en el tratamiento de imágenes, adquiere centralidad el plano de la protección efectiva de la información. En los sistemas de videovigilancia —y, en particular, en aquellos que incorporan procesamiento automatizado—, el cumplimiento normativo no se agota en la legitimidad de la captación, sino que exige la adopción de medidas técnicas y organizativas orientadas a prevenir accesos indebidos, usos no autorizados y pérdidas de información. La seguridad de los datos visuales se convierte así en un componente estructural del tratamiento, en tanto condiciona la posibilidad real de garantizar la confidencialidad, la integridad y la disponibilidad de la información, y de sostener en la práctica los principios de protección de datos personales frente a riesgos operativos y de privacidad.

La Disposición 11/2006 establece medidas de seguridad aplicables a archivos y bases de datos de carácter privado, orientadas a preservar la confidencialidad, integridad y disponibilidad de la información (Argentina, 2006). Si bien no prescribe una arquitectura tecnológica específica, fija un estándar de diligencia: el responsable debe adoptar controles proporcionales a la naturaleza de los datos y a los riesgos del tratamiento.

En el contexto de un sistema de análisis de video con inferencia por IA, este estándar se traduce en cuatro dimensiones de control: gestión de accesos bajo el principio de mínimo privilegio, registros de auditoría que permitan reconstruir quién accedió a qué información y cuándo, cifrado en tránsito para los flujos de video y las alertas generadas, y segregación de entornos que impida el acceso lateral desde componentes no críticos hacia el repositorio de video o el historial de alertas (Argentina, 2000, 2006). En sistemas con componente de IA, estos controles deben complementarse con mecanismos de trazabilidad del modelo: versiones, configuraciones de prompts, umbrales de decisión y criterios de actualización deben estar documentados para permitir la auditoría del comportamiento del sistema ante resultados inesperados (ISO, 2023).

La seguridad también se vincula con la temporalidad del tratamiento. En contextos preventivos, la conservación indefinida de video suele resultar difícil de justificar bajo parámetros de proporcionalidad. Por ello, los criterios de retención, borrado seguro y gestión de copias se integran naturalmente a la estrategia de minimización: conservar lo estrictamente necesario para el fin de seguridad y por el tiempo necesario para cumplirlo, evitando acumulaciones que aumenten el impacto ante incidentes o accesos indebidos (European Data Protection Board, 2020).


#### 16.6.4. Referentes comparados

Aunque el régimen argentino constituye la referencia normativa primaria y vinculante para el proyecto, el análisis de referentes internacionales permite incorporar criterios más desarrollados de proporcionalidad, diseño y gobernanza del dato visual. En particular, los marcos comparados resultan valiosos no como normas directamente aplicables, sino como fuentes interpretativas que orientan prácticas responsables en sistemas complejos de videovigilancia y procesamiento automatizado, aportando estándares conceptuales útiles para anticipar riesgos y fortalecer decisiones de diseño desde una perspectiva preventiva.


##### 16.6.4.1. GDPR y Directrices 3/2019 del EDPB sobre dispositivos de video

En el ámbito europeo, el Reglamento General de Protección de Datos (GDPR) establece un marco integral para el tratamiento de datos personales (European Parliament & Council of the European Union, 2016). El Comité Europeo de Protección de Datos (EDPB) complementa este marco con las Directrices 3/2019 sobre el tratamiento de datos personales mediante dispositivos de video, que desarrollan un test de proporcionalidad estructurado en etapas: evaluación de necesidad, adecuación y balance entre el interés legítimo perseguido y los derechos de las personas captadas (European Data Protection Board, 2020).

El aporte más relevante de las Directrices 3/2019 para el proyecto es la distinción operacional entre la captación de video —que puede implicar datos personales desde el momento en que permite identificar a una persona, aunque sea indirectamente— y el uso de técnicas de identificación biométrica —como el reconocimiento facial— que eleva el nivel de sensibilidad del tratamiento y exige bases legales y salvaguardas reforzadas (European Data Protection Board, 2020). Esta distinción opera como criterio orientador para el diseño de sistemas de videovigilancia: la exclusión de técnicas de identificación biométrica en sistemas orientados a detectar condiciones y no identidades reduce el nivel de intrusión del tratamiento y simplifica el análisis de proporcionalidad, aunque no elimina la aplicación de la normativa de protección de datos, dado que la captación de imágenes de personas sigue constituyendo tratamiento de datos personales bajo el derecho argentino vigente.

Las Directrices 3/2019 también introducen la noción de gobernanza del ciclo de vida del dato visual: no basta con regular el momento de la captación; el marco debe extenderse al almacenamiento, el acceso, la conservación, la transmisión y la eliminación de los datos visuales, con mecanismos que permitan responder a solicitudes de acceso y supresión sin degradar la seguridad del sistema (European Data Protection Board, 2020). Este principio constituye una referencia relevante para las etapas de diseño del proyecto, donde la arquitectura del plano de control deberá contemplar mecanismos que concilien la trazabilidad operativa con los derechos de los titulares de los datos.


#### 16.6.5. Ética y gobernanza de IA aplicada a visión por computadora

Los marcos éticos internacionales identifican riesgos que la regulación vigente no ha formalizado aún, pero que son operativamente relevantes para garantizar que el sistema funcione de manera justa, explicable y responsable en el tiempo. El componente de analítica automatizada introduce riesgos que no se agotan en la privacidad clásica: los sistemas de IA pueden amplificar asimetrías, producir errores sistemáticos o inducir decisiones organizacionales basadas en señales incompletas. Por ello, los marcos éticos internacionales incorporan dimensiones como equidad, explicabilidad, rendición de cuentas y supervisión humana, que resultan particularmente relevantes cuando el análisis se aplica a personas en entornos laborales (Organisation for Economic Co-operation and Development, 2019; United Nations Educational, 2021).

La Recomendación sobre la Ética de la Inteligencia Artificial de la UNESCO plantea una orientación basada en derechos, promoviendo el desarrollo y uso de sistemas de IA apoyado en transparencia, responsabilidad, inclusión y evaluación de impactos, con atención explícita a contextos donde pueden existir vulnerabilidades o desigualdades de poder (United Nations Educational, 2021). En escenarios de videovigilancia laboral, estos principios son directamente pertinentes: el trabajador monitorizado raramente ocupa una posición simétrica respecto al empleador que opera el sistema, y los errores del sistema —falsos positivos en particular— pueden tener consecuencias asimétricas sobre el trabajador sin que este tenga mecanismos de impugnación claros. En este sentido, la ética funciona como puente entre la licitud formal y la legitimidad social del despliegue tecnológico.

Los Principios de IA de la OECD establecen que los sistemas de IA deben ser confiables, robustos y seguros, respetuosos de los derechos humanos y con mecanismos de rendición de cuentas a lo largo de todo el ciclo de vida del sistema (Organisation for Economic Co-operation and Development, 2019). Su valor práctico reside en que estos principios son directamente traducibles a requisitos funcionales de ingeniería: documentación suficiente para auditoría del modelo, monitoreo del desempeño, gestión de incidentes con trazabilidad, y asignación clara de responsabilidades organizacionales para cada componente.

En el plano de los estándares de gestión, la norma ISO/IEC 42001:2023 establece requisitos para sistemas de gestión de IA, con énfasis en la identificación de impactos, la gestión de riesgos específicos de la IA, la documentación del ciclo de vida de los modelos y los mecanismos de mejora continua (ISO, 2023). Si bien su adopción no es obligatoria en el contexto argentino, proporciona un marco de referencia para documentar y gestionar el componente de IA del sistema de manera que sea auditable, lo que anticiparía requisitos que probablemente serán exigibles cuando la regulación de IA madure en el contexto nacional.

De esta manera, mientras el marco argentino establece obligaciones de licitud, finalidad y seguridad para el tratamiento del dato personal, los marcos comparados y éticos amplían el horizonte hacia preguntas de gobernanza: qué controles sostienen la proporcionalidad en el tiempo, cómo se auditan los resultados, cómo se corrigen sesgos y qué rol cumple la supervisión humana. Este desplazamiento es especialmente relevante cuando se pretende operar en tiempo real y con decisiones asistidas, donde la rapidez no debe desplazar la responsabilidad.


#### 16.6.6. Implicaciones para el diseño responsable del sistema

El análisis normativo y ético desarrollado en las secciones anteriores genera un conjunto de restricciones de diseño que actúan como condiciones de contorno sobre las decisiones técnicas de la plataforma experimental. La Tabla 12 organiza las principales restricciones derivadas del marco normativo y ético, con su base legal y su traducción a decisiones específicas de diseño.

Tabla 12

Principios normativos y éticos y su traducción a restricciones de diseño para sistemas de análisis automatizado de video en entornos laborales


| Principio normativo / ético | Fuente | Aplicación | Decisión de diseño implicada |
| --- | --- | --- | --- |
| Licitud y finalidad determinada | Ley 25.326 (Argentina, 2000); Disposición 10/2015 (Argentina, 2015) | El tratamiento de imágenes debe limitarse estrictamente a la detección de condiciones de riesgo laboral; no puede desviarse hacia control de desempeño, disciplina o vigilancia generalizada | El sistema no debe implementar mecanismos orientados a la identificación individual; el propósito de cada módulo debe estar documentado y auditado |
| Proporcionalidad y minimización | Ley 25.326 (Argentina, 2000); EDPB Guidelines 3/2019 (European Data Protection Board, 2020) | La captación y el procesamiento deben limitarse a lo estrictamente necesario para el fin preventivo; la identificabilidad de las personas debe reducirse al mínimo posible | Exclusión deliberada de reconocimiento facial o biométrico; análisis orientado a condiciones (EPP, posición, zona) y no a identidades individuales |
| Transparencia e información al titular | Ley 25.326 (Argentina, 2000); Disposición 10/2015 (Argentina, 2015) | Los trabajadores deben ser informados de la existencia, finalidad y responsable del sistema de monitoreo; la información debe ser accesible y comprensible | Señalización visible en obra; documentación del sistema accesible al personal; mecanismo de contacto con el responsable del tratamiento |
| Seguridad de la información | Disposición 11/2006 (Argentina, 2006); Ley 25.326 (Argentina, 2000) | El sistema debe adoptar controles técnicos proporcionales al riesgo: gestión de accesos, cifrado en tránsito, segregación de entornos, registros de auditoría | Control de acceso basado en roles con principio de mínimo privilegio; cifrado de flujos de video en tránsito; registros de auditoría de acceso a grabaciones y alertas |
| Supervisión humana y no automatización de decisiones individuales | UNESCO Recomendación IA (United Nations Educational, 2021); OECD Principios de IA (Organisation for Economic Co-operation and Development, 2019) | Las alertas generadas por el sistema son insumos para la supervisión humana, no determinaciones definitivas; el operador humano toma la decisión final de intervención | Las alertas generadas son insumos para la supervisión humana; no ejecuta acciones autónomas; el flujo de decisión preserva siempre un paso de revisión humana antes de la intervención |
| Rendición de cuentas y trazabilidad del modelo | ISO/IEC 42001:2023 (ISO, 2023); OECD Principios de IA (Organisation for Economic Co-operation and Development, 2019) | El comportamiento del sistema de IA debe ser documentable y auditables: versiones de modelos, configuraciones, umbrales de decisión, historial de alertas y falsos positivos | Registro auditable del comportamiento del sistema; versionado de modelos y configuraciones; métricas de desempeño documentadas y accesibles para revisión |
| Temporalidad y retención mínima | EDPB Guidelines 3/2019 (European Data Protection Board, 2020); Ley 25.326 (Argentina, 2000) | La conservación de grabaciones debe limitarse al tiempo estrictamente necesario para el fin de seguridad; la retención indefinida no puede justificarse bajo criterios de proporcionalidad | Política explícita de retención y borrado seguro; conservación limitada al tiempo estrictamente necesario para el fin preventivo. |

Nota. Las fuentes normativas listadas son obligatorias en el derecho argentino (Ley 25.326, Disposiciones 10/2015 y 11/2006). Los marcos éticos (UNESCO, OECD, ISO/IEC 42001) son referencias de buenas prácticas internacionales. EPP = Equipo de Protección Personal. Fuente: Elaboración propia basada en Argentina (2000, 2006, 2015), EDPB (2020), ISO (2023), OECD (2019) y UNESCO (2021).

Las restricciones sistematizadas en la Tabla 12 operan como condiciones de contorno para las decisiones técnicas de etapas posteriores del proyecto. Su cumplimiento no es verificable en abstracto: depende de cómo se materialicen en la arquitectura, los flujos de datos y los procedimientos operativos del sistema. Sin embargo, el análisis del marco normativo y ético también revela un conjunto de brechas y tensiones que la normativa vigente no resuelve de manera directa y que condicionan el diseño del prototipo. La sección siguiente organiza esas brechas y sus implicaciones para el proyecto.


#### 16.6.7. Brechas identificadas y tensiones no resueltas

El análisis del marco ético-legal revela un conjunto de brechas y tensiones que condicionan el diseño del prototipo y que no tienen resolución directa en la normativa vigente. La Tabla 13 organiza estas brechas con su descripción y su implicación específica para las decisiones del proyecto.

Tabla 13

Brechas y tensiones ético-legales identificadas en el despliegue de sistemas de análisis automatizado de video en entornos laborales


| Brecha identificada | Descripción | Implicación para el proyecto |
| --- | --- | --- |
| Ausencia de regulación específica sobre IA analítica en entornos laborales en el derecho argentino vigente | La Ley 25.326 y la Disposición 10/2015 regulan el tratamiento de datos personales y la videovigilancia en términos generales, pero no contemplan específicamente el procesamiento automatizado mediante modelos de inteligencia artificial ni la generación de alertas basadas en analítica visual. Los marcos éticos y de gobernanza de IA analizados —como los principios de la OECD y la Recomendación de la UNESCO— amplían la mirada hacia dimensiones de supervisión, rendición de cuentas y control que el derecho argentino vigente no aborda de manera directa (ISO, 2023; Organisation for Economic Co-operation and Development, 2019; United Nations Educational, 2021) | Dado el carácter experimental del prototipo, esta ausencia no constituye un impedimento operativo inmediato, pero representa una condición del contexto regulatorio que las etapas de diseño deberán considerar al definir los criterios de gobernanza del componente de analítica automatizada. |
| Ambigüedad en la identificabilidad indirecta de las personas captadas | Incluso sin reconocimiento facial, la combinación de imágenes con metadatos de tiempo, zona de obra, turno o posición puede generar identificabilidad indirecta. La Ley 25.326 protege datos de personas 'determinables' (Argentina, 2000), lo que puede incluir trayectorias de personas sin nombre si el contexto permite singularizarlas | El análisis de impacto sobre la privacidad del sistema debe evaluar no solo las salidas directas del modelo (detecciones, alertas) sino también los metadatos asociados (timestamp, zona, duración) que en conjunto pueden constituir datos personales aunque el sistema no persiga identificación nominal |
| Tensión entre retención de evidencias de seguridad y minimización de datos | La lógica de seguridad laboral puede justificar la conservación de grabaciones vinculadas a incidentes o condiciones de riesgo para su análisis posterior. Esta justificación colisiona con el principio de minimización y proporcionalidad, que exige limitar la retención al mínimo necesario (Argentina, 2000; European Data Protection Board, 2020) | Las etapas de diseño deberán definir una política de retención que concilie la justificación preventiva con el principio de minimización, estableciendo criterios de conservación y borrado seguro proporcionales a la finalidad del tratamiento. Dicha política debe integrarse al manual de tratamiento requerido por la Disposición 10/2015 (Argentina, 2015). |
| Ausencia de criterios estandarizados para comunicar la incertidumbre de sistemas de IA a operadores finales | Los sistemas de analítica automatizada producen resultados con grados variables de certeza, cuya interpretación por parte de operadores no especializados puede derivar en sobre-confianza o en subestimación de las alertas. Los marcos éticos analizados promueven la transparencia y la explicabilidad como principios generales, pero no proporcionan criterios operativos específicos para comunicar la incertidumbre inherente a los resultados automatizados en entornos laborales (Organisation for Economic Co-operation and Development, 2019; United Nations Educational, 2021). | Las etapas de diseño deberán definir mecanismos que permitan a los operadores interpretar las alertas como señales asistivas con margen de error, evitando tanto la sobre-confianza como la subestimación de los resultados automatizados. |
| Requisito de inscripción de bases de datos de videovigilancia ante la AAIP | La normativa argentina exige la inscripción de bases de datos de videovigilancia ante la Agencia de Acceso a la Información Pública (AAIP), acompañando el manual de tratamiento conforme la Disposición 10/2015 (Agencia de Acceso a la Información Pública, s/f-b; Argentina, 2015). | Cualquier validación experimental del prototipo que involucre personas en el campo visual de las cámaras requiere evaluar la obligación de inscripción ante la AAIP y la elaboración previa del manual de tratamiento conforme la Disposición 10/2015. Las condiciones específicas del entorno experimental y los procedimientos de información a los participantes deberán definirse en la etapa 2. |

Nota. Las brechas listadas no invalidan la viabilidad del proyecto, sino que definen restricciones y tareas adicionales que deben abordarse en el diseño experimental (Etapa 2) y en cualquier validación que involucre personas en el campo visual de las cámaras. AAIP = Agencia de Acceso a la Información Pública. Fuente: Elaboración propia basada en Argentina (2000, 2015), Agencia de Acceso a la Información Pública (s/f-b), European Data Protection Board (2020), ISO (2023), Organisation for Economic Co-operation and Development (2019) y United Nations Educational (2021).

Con el marco ético-legal caracterizado y sus implicaciones de diseño establecidas, quedan delimitados los principales dominios que sustentan teóricamente el proyecto: el problema de seguridad laboral en construcción, la detección open-vocabulary como enfoque de percepción, la persistencia temporal mediante seguimiento multiobjeto, las restricciones del video en tiempo real y las condiciones de uso responsable del sistema. A partir de esta base, la sección siguiente integra los aportes de estos dominios para identificar brechas transversales, criterios orientadores y condiciones de diseño que deberán ser consideradas en el desarrollo posterior del prototipo experimental.


### 16.7. Convergencias, brechas transversales y criterios orientadores

Mientras que las secciones anteriores del marco teórico caracterizaron de manera individual cada dominio técnico y normativo relevante para el problema de investigación, esta sección opera en el plano horizontal, cruzando los cinco dominios para producir conclusiones que ningún capítulo individual puede generar por sí solo. Su función es identificar qué convergencias emergen de la lectura conjunta del análisis, qué brechas resultan más difíciles de abordar precisamente porque atraviesan múltiples capas del problema, y qué criterios deberían orientar las decisiones metodológicas y tecnológicas de etapas posteriores.


#### 16.7.1. Convergencia de los dominios analizados

La revisión desarrollada en las secciones precedentes permite identificar que el sistema E-OVRT-VDP no es un problema de detección de objetos en tiempo real al que se le añaden módulos de soporte, más bien es un sistema de cinco componentes fuertemente interdependientes, en el que el desempeño de cada componente condiciona y es condicionado por los otros cuatro. Esta interdependencia tiene consecuencias directas sobre cómo deben plantearse las decisiones de diseño.

El componente de percepción OVD determina qué condiciones de riesgo pueden detectarse y con qué confianza, pero su desempeño depende de la calidad del video que recibe del pipeline de streaming y de la formulación de los prompts que el diseñador provee. El componente de persistencia temporal MOT estabiliza y enriquece las detecciones del OVD, pero su calidad depende directamente de la estabilidad del detector subyacente: un modelo OVD con alta variabilidad frame-a-frame degrada el tracker independientemente de la sofisticación del algoritmo de asociación. El pipeline de transmisión de medios define el presupuesto de latencia disponible para la inferencia, pero la latencia del modelo OVD es a su vez la variable de mayor rango de variación de todo el pipeline. El marco normativo y ético no es un componente técnico, pero impone restricciones que afectan qué datos pueden almacenarse, cómo deben comunicarse las alertas y qué arquitectura del plano de control es admisible. Y el dominio de aplicación define cuáles de los anteriores importan, no en términos de métricas académicas, sino en términos del tiempo que transcurre entre una condición de riesgo y la posibilidad de intervención humana para neutralizarla.

Esta interdependencia tiene la consecuencia metodológica directa de que las decisiones tecnológicas de las etapas posteriores no pueden tomarse componente por componente. Deben evaluarse en función de su contribución al desempeño del sistema integrado, medido en las métricas operativas del dominio de aplicación. Un modelo OVD que maximiza la precisión en COCO pero introduce 200 ms adicionales de latencia de inferencia puede ser una elección incorrecta si ese overhead hace que el pipeline completo supere el presupuesto de latencia de alerta admisible. Un método MOT con alta precisión en MOTChallenge pero con dependencia de un modelo ReID específico por dominio puede ser inadecuado porque introduce una dependencia de entrenamiento que el proyecto no puede satisfacer en ausencia de datasets etiquetados de construcción civil.


#### 16.7.2. Convergencias del análisis

La lectura conjunta de los cinco dominios produce tres argumentos que emergen de múltiples secciones de manera convergente y que constituyen los pilares del juicio de viabilidad del sistema.


##### 16.7.2.1. La modularidad y el desacoplamiento como necesidad técnica

El argumento a favor de la modularidad emerge de al menos cuatro análisis independientes. En el dominio OVD, la reparametrización de embeddings textuales entre cuadros consecutivos —la estrategia más efectiva para aproximar la inferencia OVD a los requisitos de tiempo real— es posible precisamente porque el encoder de lenguaje puede desacoplarse del proceso de inferencia visual. En el dominio MOT, el paradigma tracking-by-detection es preferible a los enfoques end-to-end no porque produzca mayor precisión en benchmarks, sino porque permite sustituir el detector sin reentrenar el tracker, habilitando la integración de modelos OVD con vocabulario dinámico sin modificar el componente de seguimiento. En el dominio de streaming, la separación entre protocolo de ingesta y protocolo de entrega al dashboard permite optimizar cada segmento del pipeline de manera independiente, sin que la elección de protocolo para las cámaras de obra imponga restricciones sobre cómo se presenta el video analizado al supervisor. Y en el dominio ético-legal, la separación entre el plano de medios y el plano de control es lo que habilita el diseño de una política de retención y acceso diferenciada: el video crudo puede borrarse según la política de minimización, mientras que los eventos de alerta se conservan en el repositorio inmutable de event sourcing sujetos a las garantías de acceso y supresión de los titulares. El corolario de esta convergencia es que la modularidad no emerge del análisis como una preferencia estilística de arquitectura, sino como una propiedad que habilita simultáneamente varias funciones que se identifican como relevantes: la evaluación comparativa de alternativas tecnológicas sin rediseño del pipeline completo, la sustitución de componentes sin reentrenamiento de los restantes, la trazabilidad y auditoría del comportamiento de cada módulo de manera independiente, y la gestión diferenciada de datos según las restricciones normativas que apliquen a cada tipo de información (video crudo, trayectorias, eventos de alerta) Un diseño que acople estos componentes en un único proceso o framework comprometería, según el análisis realizado, la posibilidad de satisfacer estas funciones de manera conjunta. La determinación del grado de desacoplamiento necesario y su materialización en una arquitectura concreta corresponden a las etapas de diseño del proyecto.


##### 16.7.2.2. Las brechas estructurales del dominio de construcción civil

El argumento sobre las brechas de dominio emerge de manera convergente en las tres secciones técnicas. Los modelos OVD preentrenados en datos web a gran escala presentan desempeño inferior en categorías semánticamente distantes de los conceptos cotidianos bien representados en esos datos: arnés de seguridad, chaleco reflectivo y señalero son conceptos operativamente críticos para la seguridad en construcción pero infrecuentes en MS COCO o en los datasets de preentrenamiento de CLIP. Los benchmarks estándar de MOT —diseñados para peatones en entornos urbanos— no contemplan la densidad de oclusiones por maquinaria y materiales, la heterogeneidad de entidades (personas, equipos, vehículos de obra) ni la perspectiva de cámara fija en planos elevados típica de instalaciones de videovigilancia de obra. Los benchmarks de latencia de modelos OVD reportan tiempos de inferencia en condiciones estáticas sobre hardware estándar, sin caracterizar el comportamiento bajo procesamiento continuo de múltiples flujos durante turnos completos de trabajo.

La consecuencia de esta convergencia no es que el proyecto sea inviable, más bien que la evaluación del prototipo no puede apoyarse en los benchmarks existentes como métricas de referencia directa. La consolidación metodológica posterior debe diseñar un protocolo de evaluación propio, con condiciones representativas del dominio de construcción civil, métricas alineadas con el valor operativo del sistema, y un conjunto de condiciones de riesgo seleccionadas a partir del análisis normativo desarrollado en la sección 16.2. Este protocolo es uno de los productos más críticos ya que sin él no hay base para afirmar que el desempeño del prototipo es adecuado para el dominio.


##### 16.7.2.3. La latencia de alerta como restricción operativa central

El argumento sobre la métrica operativa central emerge de la intersección entre el análisis del dominio de aplicación, las restricciones temporales del pipeline y el marco ético-legal. La normativa de seguridad laboral analizada establece obligaciones de supervisión activa que requieren capacidad de intervención ante condiciones de riesgo. Esta capacidad de intervención sólo es operativamente significativa si el sistema detecta la condición de riesgo y la comunica al supervisor con suficiente anticipación para que la intervención sea posible antes de que se produzca el incidente.

La latencia de inferencia del modelo OVD —la métrica que domina las publicaciones académicas sobre modelos en tiempo real— es solo uno de los componentes de la latencia de alerta total. Los otros componentes —latencia de captura y codificación, latencia de transporte de red, latencia de procesamiento MOT y razonamiento temporal, latencia de entrega de la alerta— contribuyen de manera acumulativa y variable a la latencia total. Un modelo OVD que opera a 30 ms de inferencia pero que se integra en un pipeline con 300 ms de latencia de transporte y 200 ms de buffering produce una latencia de alerta de 530 ms o más, que puede ser insuficiente para ciertos tipos de riesgo. Esta observación tiene una implicación directa para las etapas posteriores: la definición del presupuesto de latencia admisible no puede tratarse como un parámetro único e indiferenciado, dado que el análisis normativo de la sección 16.2 evidencia que las condiciones de riesgo presentan perfiles temporales heterogéneos —desde situaciones que escalan en segundos hasta condiciones que persisten durante minutos antes de materializarse en un incidente—. La forma en que esa heterogeneidad se incorpore a los criterios de evaluación del pipeline es una decisión metodológica que excede el alcance del presente análisis teórico.


#### 16.7.3. Mapa de brechas transversales

Además de las convergencias identificadas en la sección anterior, el análisis revela un conjunto de brechas que no pertenecen a un único dominio sino que emergen de la intersección entre dos o más de los dominios analizados, las cuales condicionan decisiones que involucran simultáneamente múltiples componentes del problema. La Tabla 14 organiza las seis brechas transversales identificadas, con su descripción integrada y su implicación para las etapas posteriores del proyecto.

Tabla 14

Brechas transversales identificadas en el análisis integrado del sistema E-OVRT-VDP


| Brecha transversal | Descripción integrada | Implicación para el diseño |
| --- | --- | --- |
| Ausencia de benchmarks específicos para construcción civil | Los benchmarks estándar de OVD (COCO, LVIS), MOT (MOT17, MOT20) y streaming no contemplan las condiciones visuales, de conectividad y de distribución semántica propias de una obra civil. Las métricas reportadas en la literatura no son directamente transferibles al dominio objetivo. | La ausencia de benchmarks específicos impone la necesidad de un protocolo de evaluación propio que contemple condiciones representativas del dominio. |
| Métricas académicas no alineadas con el valor operativo de seguridad laboral | Las métricas de detección (AP), tracking (HOTA, MOTA) y streaming (throughput, jitter) no capturan el valor operativo central: el tiempo entre la ocurrencia de la condición de riesgo y la disponibilidad de la alerta para el supervisor, ni el impacto diferenciado de falsos positivos versus falsos negativos en contextos de seguridad laboral. | Se requiere definir como variable de diseño primaria la latencia de alerta end-to-end, entendida como el tiempo desde la aparición de la condición de riesgo hasta la entrega de la alerta al supervisor, incluyendo las contribuciones del pipeline de medios, la inferencia OVD, el MOT y el razonamiento temporal. |
| Integración no caracterizada de componentes heterogéneos en un pipeline unificado | La literatura caracteriza cada componente del sistema —modelos OVD, métodos MOT, protocolos de streaming— de manera independiente. No existen estudios que caractericen el comportamiento del pipeline integrado OVD + MOT + streaming bajo carga sostenida y con condiciones de red variables. | Impone una validación experimental del sistema integrado, midiendo degradación de latencia end-to-end y propagación de errores entre componentes bajo carga sostenida y conectividad variable. |
| Condiciones de riesgo composicionales que exceden la percepción frame-a-frame | Muchas condiciones de riesgo operativamente relevantes son composicionales: “persona en zona restringida sin señalero visible”, “maquinaria operando cerca de peatones”. Requieren razonamiento sobre relaciones espaciales y temporales entre entidades que exceden la capacidad del detector OVD frame-a-frame. | La arquitectura debe incluir una capa de razonamiento contextual sobre las trayectorias producidas por el módulo MOT, capaz de evaluar condiciones que involucren múltiples entidades y su relación espacial. El diseño de esta capa es una decisión arquitectónica de la instancia de diseño arquitectónico. |
| Sensibilidad al diseño de prompts como variable de desempeño no trivial | El diseño de los prompts de consulta no es una tarea de configuración trivial: pequeñas variaciones en la formulación producen diferencias significativas en el desempeño. Esta variable no existe en sistemas closed-set y no tiene metodología estandarizada para el dominio de seguridad laboral. | La sensibilidad a la formulación de prompts introduce una variable de desempeño que requiere tanto un protocolo sistemático de diseño y evaluación de prompts como un mecanismo arquitectónico que permita iterar sobre formulaciones sin modificar el modelo. |
| Marco normativo-ético como restricción de diseño con consecuencias arquitectónicas | El cumplimiento de la Ley 25.326 y la Disposición 10/2015 impone restricciones estructurales sobre qué datos pueden almacenarse, por cuánto tiempo, con qué controles de acceso y bajo qué condiciones de transparencia. Estas restricciones afectan directamente las decisiones de arquitectura del plano de control. | El repositorio de eventos (event sourcing) del plano de control debe diseñarse con conciencia de los derechos de los titulares; el sistema no puede almacenar trayectorias contextualizadas de manera indefinida; la interfaz de alertas debe incluir indicadores de confianza que posicionen las alertas como señales asistivas. |

Nota. Las brechas se denominan transversales porque emergen de la intersección de al menos dos dominios del marco teórico, no de uno solo. Su resolución requiere decisiones de arquitectura que afecten simultáneamente a múltiples componentes del sistema. Fuente: Elaboración propia a partir del análisis integrado de las secciones del marco teórico.

De las seis brechas listadas, la relacionada con las condiciones de riesgo composicionales merece una consideración adicional por su alcance. Como se analizó en las secciones anteriores, la detección OVD opera a nivel de entidades individuales por cuadro, y el MOT aporta persistencia temporal a cada entidad de manera independiente. Sin embargo, ninguno de los dos mecanismos modela relaciones entre entidades: una condición como "persona dentro de zona restringida" requiere detectar la persona, detectar la delimitación del área, evaluar si la posición de la primera se encuentra contenida en la segunda, y determinar si esa permanencia es transitoria o sostenida. Esta brecha no es una limitación de un modelo particular, sino una propiedad estructural del paradigma de detección por fotograma complementado con tracking: el razonamiento relacional y contextual constituye una capacidad que el estado del arte analizado no provee de manera nativa y cuya resolución deberá abordarse como problema de diseño en etapas posteriores.


#### 16.7.4. Criterios orientadores para la selección tecnológica

El análisis del estado del arte no selecciona tecnologías: establece los criterios que deben orientar esa selección. La Tabla 15 organiza los siete criterios orientadores derivados del análisis integrado, con su descripción, la dimensión evaluable y el origen en el análisis. Estos criterios deben utilizarse en la instancia de diseño arquitectónico para estructurar las decisiones de diseño arquitectónico y en la validación experimental para diseñar el protocolo de evaluación comparativa entre alternativas.

Tabla 15

Criterios orientadores multidimensionales para las decisiones tecnológicas de las etapas de diseño y validación del sistema E-OVRT-VDP


| Criterio orientador | Descripción y fundamento | Dimensión evaluable |
| --- | --- | --- |
| Compatibilidad con detección open-vocabulary | Cada componente del sistema (tracker, servidor de medios, framework de procesamiento) debe poder integrarse con un detector OVD cuyo vocabulario varía dinámicamente en tiempo de ejecución, sin requerir reentrenamiento ni modificación de parámetros. | Presencia de API de desacoplamiento; ausencia de dependencias de clases fijas en el componente. |
| Latencia de alerta E2E compatible con intervención humana oportuna | El sistema completo —desde la aparición de la condición de riesgo hasta la entrega de la alerta al supervisor— debe operar dentro de un presupuesto de latencia que habilite la intervención humana antes de que la condición produzca un incidente. Este presupuesto debe formalizarse en la consolidación metodológica. | Latencia de alerta medida en percentiles (P50, P95, P99) bajo carga sostenida con múltiples flujos. |
| Independencia de entrenamiento específico por dominio | Los componentes del pipeline deben poder operar de manera efectiva con pesos preentrenados en modalidad zero-shot. Cuando se considere fine-tuning de dominio, la arquitectura del modelo OVD debe permitir adaptación sin degradar la capacidad de responder a consultas semánticas arbitrarias, dado que la preservación de esta capacidad varía significativamente entre familias arquitectónicas. | Desempeño evaluable en condiciones zero-shot; perfil de adaptabilidad documentado (retención de capacidad OVD post-fine-tuning). |
| Desacoplamiento entre plano de medios y plano de control | El flujo de video (ingesta, inferencia, visualización) y la lógica de negocio (eventos, alertas, trazabilidad) deben operar en planos arquitectónicamente separados, de modo que la modificación de cualquier componente de uno de los planos no requiera modificaciones en el otro. | Posibilidad de sustituir el modelo OVD sin modificar el sistema de alertas; posibilidad de cambiar el protocolo de streaming sin modificar el repositorio de eventos. |
| Robustez operativa para entornos de obra | El sistema debe mantener un desempeño aceptable ante condiciones adversas: oclusiones frecuentes, variabilidad de iluminación, conectividad de red variable, y operación continua durante turnos de trabajo de 8 a 10 horas. | Tasa de fragmentación de trayectorias MOT; estabilidad de latencia bajo carga térmica sostenida; resiliencia del protocolo ante pérdida de paquetes. |
| Minimización del impacto sobre la privacidad por diseño | El sistema debe diseñarse desde el inicio con mecanismos que reduzcan la identificabilidad de las personas captadas, de conformidad con la Ley 25.326 y la Disposición 10/2015. Esta restricción condiciona qué datos generar, almacenar y transmitir. | Ausencia de identificadores biométricos; política de retención diferenciada documentada; controles de acceso verificables. |
| Carácter asistivo y auditabilidad del sistema de alertas | Las alertas deben comunicarse con indicadores de confianza comprensibles para operadores no técnicos; el flujo de decisión debe preservar revisión humana antes de toda intervención; el historial de alertas, configuraciones y versiones debe ser auditable. | Presencia de indicadores de confianza en la interfaz; registro inmutable de eventos con metadatos de versión de modelo; capacidad de responder consultas de auditoría. |

Nota. Los criterios listados no son métricas de selección directa sino dimensiones de evaluación: cada candidato tecnológico debe evaluarse en función de su desempeño en todas las dimensiones relevantes, sin que ninguna dimensión sea suficiente por sí sola para determinar la selección. La ponderación relativa de los criterios depende de las restricciones específicas del escenario de despliegue experimental, que deben formalizarse en la consolidación metodológica.

Los siete criterios presentan tensiones entre sí que deben gestionarse explícitamente durante el diseño. La tensión más relevante es la que existe entre el criterio de latencia de alerta E2E (criterio 2) y el criterio de compatibilidad con OVD (criterio 1): los modelos OVD con mayor expresividad semántica —paradigma DETR/DINO con fusión profunda— suelen introducir mayor latencia de inferencia, mientras que los de menor latencia —paradigma one-stage YOLO con reparametrización— tienen menor capacidad para manejar condiciones composicionales con atributos relacionales complejos. La elección del modelo OVD debe realizarse con plena conciencia de este trade-off y validarse empíricamente en el dominio específico antes de fijar la selección.

Una segunda tensión existe entre el criterio de robustez operativa (criterio 5) y el criterio de minimización del impacto sobre la privacidad (criterio 6): los métodos de tracking con mayor robustez ante oclusiones prolongadas suelen incorporar modelos de apariencia que generan representaciones más ricas de las personas rastreadas, aumentando la identificabilidad indirecta.


#### 16.7.5. Lectura arquitectónica integrada

La lectura conjunta del marco teórico produce una imagen conceptual del sistema que es coherente con la arquitectura de dos planos planteada en el anteproyecto del proyecto, y que el análisis de los cinco dominios permite ahora describir con mayor precisión técnica.

El plano de medios realiza el procesamiento en tiempo real del flujo de video. Se estructura en cuatro etapas secuenciales: ingesta —captación de video desde cámaras IP mediante protocolos como RTSP/RTP en entornos LAN controlados o mediante SRT en conectividad WAN variable—, normalización —estandarización de resolución, frame rate y formato de píxel para garantizar compatibilidad con el modelo de inferencia—, inferencia —ejecución del modelo OVD sobre los frames normalizados con la consulta de prompts definida para las condiciones de riesgo activas, conforme al análisis de modelos y paradigmas OVD desarrollado en la sección 15.2.1— y tracking —asociación de las detecciones OVD entre cuadros consecutivos mediante el método MOT seleccionado para producir trayectorias persistentes con identidades estables—. La salida del plano de medios es un flujo de trayectorias etiquetadas semánticamente que se publica como eventos al plano de control. La ruta crítica de latencia del sistema pasa íntegramente por este plano; cualquier cuello de botella de latencia que supere el presupuesto definido en la etapa 2 debe diagnosticarse y resolverse en este plano.

El plano de control realiza el procesamiento orientado a la lógica de negocio y la gobernanza del sistema. Consume los eventos de trayectorias publicados por el plano de medios y los evalúa mediante un módulo de razonamiento contextual que determina si una trayectoria o conjunto de trayectorias satisface las condiciones de riesgo configuradas. Cuando una condición de riesgo se detecta como persistente durante el intervalo temporal mínimo configurado, el sistema genera una alerta asistiva que se entrega al supervisor a través del canal de notificación definido. Todos los eventos —detecciones, trayectorias, alertas generadas, configuraciones de prompts, versiones de modelos— se registran de manera inmutable en el repositorio de event sourcing, que constituye el mecanismo de trazabilidad y auditoría del sistema. El diseño del plano de control debe contemplar explícitamente las restricciones normativas analizadas en la sección 16.6: política de retención diferenciada para eventos con y sin alerta, controles de acceso por rol y mecanismos de respuesta a solicitudes de derechos de los titulares de los datos.

Esta lectura arquitectónica integrada permite identificar dónde se producen las interfaces más críticas entre componentes: la interfaz entre el tracker MOT y el módulo de razonamiento contextual —que recibe trayectorias geométrico-temporales y debe producir evaluaciones semánticas sobre condiciones de riesgo— es el punto de mayor complejidad conceptual del sistema, porque es donde la brecha entre la percepción computacional (entidades rastreadas con bounding boxes) y el razonamiento operativo (condiciones de riesgo del dominio laboral) debe cerrarse.


#### 16.7.6. Proyección hacia la consolidación metodológica

El análisis realizado cumple su propósito cuando establece con precisión qué se sabe, qué no se sabe y qué debe definirse antes de avanzar hacia la consolidación metodológica, el diseño y la implementación. Las preguntas que siguen constituyen las cuestiones abiertas que el marco teórico no puede resolver por sí mismo y que la consolidación metodológica —análisis metodológico y estrategia de evaluación— debe abordar como su tarea central. Cada pregunta se identifica con un código (P-E1-XX) para facilitar la referencia cruzada desde los apartados metodológicos posteriores.

P-E1-01. ¿Cuál es el presupuesto de latencia de alerta admisible para el sistema, diferenciado por el perfil temporal de cada categoría de condición de riesgo del dominio? La respuesta requiere analizar la velocidad de escalada desde la condición observable hasta el incidente potencial para los riesgos identificados en la sección 16.2, y traducir ese análisis en umbrales de latencia end-to-end que operen como criterio de referencia para las decisiones de selección tecnológica del pipeline.

P-E1-02. ¿Cuál es el conjunto mínimo de condiciones de riesgo que el prototipo debe ser capaz de detectar para constituir una demostración de viabilidad, y cómo deben formularse esas condiciones como prompts textuales evaluables por modelos OVD? La selección debe incluir, del catálogo de condiciones desarrollado en la sección 16.2, un subconjunto representativo que abarque condiciones simples (entidad única con atributo observable) y condiciones composicionales (relación entre múltiples entidades), de modo que el prototipo ejercite las capacidades del sistema en toda su extensión sin agotar los recursos del proyecto en un catálogo exhaustivo. La formulación como prompts debe considerar las limitaciones lingüísticas documentadas en los modelos candidatos de la sección 16.3.

P-E1-03. ¿Qué datasets públicos con anotaciones de calidad suficiente están disponibles para evaluar la capacidad de detección y de tracking del sistema en el dominio de construcción civil, y cuáles de ellos resultan además aptos como datos de entrenamiento para fine-tuning de modelos preentrenados? La ausencia de benchmarks integrados del dominio, identificada en los análisis de seguimiento multiobjeto y operación en tiempo real, implica que la estrategia de evaluación deberá combinar datasets existentes con materiales recolectados ad hoc, y que la aptitud para fine-tuning deberá evaluarse en función del volumen, formato de anotación y transferibilidad al dominio.

P-E1-04. ¿Cuáles son las restricciones del entorno de ejecución —capacidad computacional del hardware de inferencia, recursos del entorno de entrenamiento, protocolos de transmisión de video y presupuesto de procesamiento— que condicionan las decisiones arquitectónicas del prototipo? El análisis desarrollado en la sección 15.4 documenta las características de los protocolos candidatos, pero la selección concreta depende de la caracterización del hardware disponible y de la asignación del presupuesto computacional entre los componentes del pipeline.

P-E1-05. ¿Bajo qué condiciones experimentales —iluminación, resolución, distancia de cámara, oclusión, densidad de personas en escena— debe evaluarse el prototipo para que los resultados sean representativos del dominio de construcción civil? La definición de estas condiciones implica establecer las variables de control, los niveles de prueba y los criterios de aceptación que determinarán si el prototipo demuestra la hipótesis de viabilidad en un entorno que, aun siendo controlado, preserve la validez ecológica respecto del dominio operativo.

P-E1-06. ¿Qué framework de métricas debe adoptarse para evaluar de manera integral las capacidades del sistema —detección OVD, tracking multiobjeto y razonamiento temporal sobre condiciones persistentes— y cuáles son los umbrales de aceptación para cada componente? El análisis teórico identifica familias de métricas estándar (mAP, HOTA, MOTA) pero no establece los umbrales operacionales ni las métricas derivadas que capturen el comportamiento específico del sistema bajo las condiciones del dominio.

P-E1-07. ¿Qué recaudos ético-legales, proporcionados al carácter académico y controlado de las pruebas experimentales, deben incorporarse al diseño de la estrategia de evaluación? El marco normativo analizado en la sección 16.6 establece los principios de licitud y proporcionalidad, pero la determinación de las medidas concretas —consentimiento informado, minimización de datos, protocolo de anonimización— corresponde a la consolidación metodológica, en función de las condiciones experimentales que se definan en respuesta a P-E1-05.

P-E1-08. ¿Constituye el fine-tuning ligero de modelos OVD preentrenados un experimento comparativo viable dentro de las restricciones de recursos del proyecto, y bajo qué condiciones ese ajuste mejoraría la detección de categorías vistas sin degradar la capacidad open-vocabulary sobre categorías no vistas? La viabilidad depende de la disponibilidad de datos de entrenamiento (P-E1-03), de la capacidad computacional del entorno de entrenamiento —distinta del entorno de inferencia— (P-E1-04), y de la factibilidad de diseñar un protocolo experimental que aísle el efecto del fine-tuning (P-E1-06).

Como puede apreciarse, estas preguntas se condicionan mutuamente. El presupuesto de latencia (P-E1-01) determina qué modelos y protocolos son viables; la selección de condiciones de riesgo (P-E1-02) condiciona los datasets necesarios (P-E1-03); las restricciones del entorno de ejecución (P-E1-04) limitan las opciones arquitectónicas; las condiciones experimentales (P-E1-05) definen el alcance de las métricas (P-E1-06); y los recaudos ético-legales (P-E1-07) imponen restricciones transversales sobre todas las anteriores. Por esta razón, la siguiente etapa debe abordarse de manera iterativa y no secuencial, buscando la coherencia interna de un protocolo que sea, simultáneamente, técnicamente riguroso, representativo del dominio y normativamente admisible.


### 16.8. Conclusiones parciales de la fundamentación teórica

La fundamentación teórica construye el marco teórico que sustenta las decisiones metodológicas y tecnológicas posteriores del proyecto E-OVRT-VDP, mediante la caracterización de cinco dominios: seguridad laboral en construcción, detección open-vocabulary, seguimiento multiobjeto, transmisión de video en baja latencia y regulación ético-legal.


#### 16.8.1. Sobre la viabilidad teórica de la hipótesis de trabajo

El análisis del estado del arte y la confección del marco teórico permite concluir que la hipótesis de que la detección open-vocabulary, como habilitador tecnológico, para el monitoreo asistivo de seguridad en construcción es teóricamente sostenible. Existen arquitecturas OVD con latencias de inferencia compatibles con vídeo continuo, métodos MOT integrables con detectores externos sin reentrenamiento, protocolos de streaming con perfiles de latencia documentados, y un marco normativo argentino que no prohíbe el procesamiento propuesto siempre que se cumplan condiciones de licitud y minimización de datos.

Esta viabilidad está condicionada por cuatro factores identificados en el análisis: (a) la selección de un modelo OVD con balance adecuado entre precisión semántica y latencia para el hardware disponible, (b) el diseño de los prompts de consulta para las condiciones de riesgo del dominio, (c) la integración de tracking que compense la variabilidad temporal de las detecciones por fotograma, y (d) el cumplimiento de las restricciones ético-legales como condiciones de diseño no negociables.


#### 16.8.2. Sobre la completitud del marco teórico construido

El marco teórico, articulado con los desarrollos temáticos previos, cubre los dominios necesarios para fundamentar el proyecto, junto con la identificación de las brechas transversales que emergen de la intersección entre dominios y la formulación de siete criterios orientadores multidimensionales para las decisiones tecnológicas posteriores. En este sentido, la construcción del marco teórico y su síntesis crítica permitieron alcanzar los objetivos propuestos para esta primera instancia de fundamentación, consolidando una base conceptual suficiente para orientar el desarrollo de la etapa siguiente.

Es crucial mencionar que el marco presenta tres limitaciones que deben reconocerse como inherentes al dominio de aplicación y de las herramientas ponderadas, siendo 1) la evolución acelerada del campo OVD puede modificar el panorama de modelos disponibles antes de la implementación; 2) los datos de rendimiento reportados en la literatura corresponden a condiciones experimentales que difieren de las operativas en construcción civil y 3) el dinamismo regulatorio argentino en materia de inteligencia artificial podría introducir requisitos adicionales durante el ciclo de vida del proyecto.


#### 16.8.3. Transición hacia la consolidación metodológica

La consolidación metodológica deberá traducir los criterios teóricos establecidos en esta fundamentación teórica en un protocolo de evaluación experimental concreto: definir los datasets de referencia, las métricas aplicables, las condiciones de prueba y los umbrales de aceptación. El mapa de brechas, los criterios planteados y la taxonomía de riesgos de las distintas secciones de esta fundamentación proveen los insumos directos para esa tarea.


