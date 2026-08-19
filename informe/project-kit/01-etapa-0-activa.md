# E-OVRT-VDP - paquete de etapa 0

> Generado el 2026-08-19. Etapa 0: secciones 11 a 14 y ajustes transversales.

## Que esta CERRADO y que esta ABIERTO (leer antes de redactar)

Lo **cerrado** se escribe como hecho, en pasado y sin condicionales: ya fue ejecutado y
verificado, y dejarlo como duda seria falsear el estado del trabajo. Lo **abierto** no se
escribe: se deja un marcador visible para que lo complete quien tiene el dato.

**CERRADO — se afirma:**

1. Distribucion de alertas: implementada, verificada e integrada (vista de webconsole,
   orquestacion y repositorio versionado, 2026-08-13). Su estatuto es trabajo comprometido
   con estado declarado a la entrega; los canales adicionales siguen fuera de alcance.
2. Identidad de sujeto: implementada y medida. Lo excluido son las metricas MOT.
3. Comparacion de estrategias de deteccion: ejecutada (la directa fue vetada por
   precision y la hibrida por disyuncion fue ejecutada y refutada).
4. Referencia temporal del banco: anotacion **humana** y congelada; se reporta como
   resultado, no como verificacion preliminar.
5. Rama de ajuste fino, **brazo T1: CERRADO con veredicto NO-GO** (2026-08-17). Los
   margenes se firmaron **antes** de la linea base, la corrida se ejecuto una vez y se
   evaluo una vez, y **el checkpoint ajustado no se adopta como modelo de servicio**.
   Tiene cifra medida y se escribe como **hallazgo, no como fracaso**: el ajuste rescata
   `bare_head` del cero absoluto (AP50 0,0000 -> 0,0455) pero **no alcanza el umbral**
   (faltaron 0,0045) y **rompe la retencion de `person`** (-11,62 %, tope 10 %). Va en
   tabla propia, por estrato, nunca mezclada con el nucleo zero-shot.

**ABIERTO — no se afirma; se marca:**

1. **Resultado del brazo T2**: no existe. T2 se reabrio como tier **exploratorio** por
   enmienda posterior al NO-GO (D-FT-14) y esta **enviado y en cola, sin empezar**; sus
   margenes ya estan firmados por adelantado (D-FT-15). No hay ninguna cifra de ese
   checkpoint y no la habra hasta que corra y se evalue: esa subseccion queda reservada
   con marcador. **T1 ya no es un hueco**: tiene resultado y se afirma (ver CERRADO 5).
2. **Cinco figuras sin producir** (vista de procesos, maquina de estados del motor,
   calidad frente a densidad, cuadro con alerta superpuesta y frontera de juzgabilidad).
   Se mencionan en el texto con marcador; no se describen como si existieran.
3. **Procedencia de origen del lote de obra real** (direccion y fecha de acceso por
   clip): pendiente. No bloquea redactar; si bloquea cerrar la version final.

### Convencion de marcadores (obligatoria)

Todo hueco se deja con doble corchete, de modo que sea localizable con una busqueda:

- `[[PENDIENTE: que falta · de que depende]]`
- `[[CIFRA: que cifra hace falta · de que indice saldria]]`
- `[[FIGURA: cual]]`

Reglas: nunca completar un marcador con una estimacion, un valor probable ni una
redaccion evasiva; nunca borrarlo para que el texto "fluya"; el marcador viaja hasta el
entregable y recien lo remueve quien aporta el dato. Un capitulo con marcadores visibles
es honesto; un capitulo que rellena huecos es indefendible.

## Estado vigente que manda sobre el resto

- Banco temporal: **47 clips = 32 positivos + 15 negativos, con 37 episodios**. Los 34
  clips corresponden solo al Bloque A del rodaje.
- **FAR/hora se mide y se reporta**, pero la exposicion disponible no permite sostener
  una cota operativa; siempre se cita el conteo, la duracion observada y la tasa derivada.
- **G1/identidad de sujeto esta implementada y medida**. Las metricas MOT siguen fuera
  de alcance; no debe confundirse la exclusion de esas metricas con la capacidad.
- La distribucion de alertas esta **funcionalmente implementada**: los seis criterios de
  spec 45 quedaron verificados, incluido reporte y broker MQTT real. La vista de
  webconsole y la orquestacion integral se cerraron el 2026-08-13 y el repo
  `e-ovrt_alert-distribution` ya tiene historia propia. **Si aporta cifra citable**:
  `t_alert-notification` **p95 = 64,534 ms (n = 460)** entregas live, y en regimen
  sostenido **p95 = 102,025 ms (n = 104)**; mide `bus de alertas -> PUBACK MQTT`, nunca
  sensor -> notificacion (`operacion/118`).
- E-04/fine-tuning es una **rama comparativa separada y en curso**. F-100.1 esta
  resuelta. `1166583` cerro freeze/smoke tecnico con 12 tensores/3.096 parametros y
  optimizer 12/12; dual gate, serving real y **procedencia T-FT-023 (cerrada el
  2026-08-13, snapshot tar `639e60df...`)** estan verdes. **El 2026-08-15 el usuario firmo
  D-FT-08 (contrato de serving), D-FT-12 (objetivo y margenes go/no-go, firmada ANTES de
  la baseline) y D-FT-13 (derogacion de la sonda `machinery` solo para T1)**, T-FT-005
  quedo `done` y **no queda ninguna decision humana pendiente**. La misma jornada se
  cerraron **T-FT-031** (comando de evaluacion congelado + enforcement canonico v2 en
  config + catalogo finetuned) y **T-FT-032**: la **baseline YOLOE-26s corrio UNA vez
  sobre las 6.477 imagenes de `bench_v3`** (doc 120) — `bare_head` AP50 **0,000**
  (6.181 GT / 10 detecciones), recall CR-01 0,0167/0,0000 por fuente y **0,0002
  agregado**; retencion a proteger person 0,7843 / helmet 0,6286 / vest 0,2642. Estas
  cifras son **de la rama comparativa**: van SIEMPRE en tablas propias, por estrato, y
  NO se promueven a `results/` hasta cerrar la jornada; **no hay cifra del checkpoint
  ajustado** (no existe todavia) ✎ *superado el 2026-08-17: el checkpoint T1 SI tiene
  cifra — ver la enmienda al pie de esta vineta; el que sigue sin cifra es T2*.
  F-120.1: las latencias de ese run NO se citan (cambio
  de energia en curso); el gate de latencia se mide pareado aparte.
  **✎ 2026-08-15 (noche) — T1 full ENVIADO: T-FT-043 esta CERRADA.** La autorizacion se
  emitio y verifico en el cluster con sus 7 gates, el ensayo `--test-only` paso, y el
  `RUN` quedo **encolado como job `1167640`** (1 GPU / 10 CPU / 60 GB / 2 h). Al encolar
  figuraba en espera, con inicio estimado por el planificador el 2026-08-17; una
  estimacion del planificador **no es reserva ni promesa**, y el envio **no es un
  resultado**. Lo que sigue abierto es la corrida en si y, despues, la promocion del
  checkpoint por hash, su evaluacion unica y el veredicto go/no-go contra los margenes ya
  firmados. **Hasta que eso ocurra no existe ninguna cifra del modelo ajustado**: la
  subseccion correspondiente se deja con `[[PENDIENTE: ...]]`, jamas con un valor
  estimado ni con una redaccion que sugiera que la comparacion ya se hizo.
  La sonda de clase nueva (`machinery`) quedo **derogada para T1 y reasignada a T2/T3**
  por D-FT-13; en T2/T3, de vocabulario abierto, sigue siendo exigible.
  **✎ 2026-08-17 — la jornada T1 CERRO: veredicto NO-GO.** El job `1167640` corrio el
  16/08, el checkpoint se promovio por hash y se evaluo **una sola vez** contra
  `bench_v3`: `bare_head` AP50 **0,0000 -> 0,0455** (gate A pedia >= 0,05: **faltaron
  0,0045**) y la retencion de `person` cayo **0,7843 -> 0,6932 (-11,62 %, tope 10 %)**.
  **El checkpoint no se adopta.** Los margenes (D-FT-12) estaban firmados desde el 15/08,
  antes de la baseline, y **no se renegociaron**: eso es lo que hace al resultado
  defendible. La cifra **existe y es citable**, en tabla propia por estrato; el gate de
  latencia **no se midio** y se dice explicito (F-123.1), no se omite.
  **La misma jornada, DESPUES del veredicto, el usuario firmo la enmienda D-FT-14**: T2
  se reabre como tier **exploratorio** —para separar si el fallo fue de capacidad o
  estructural—, no como reintento de T1, y **T3 queda cerrado como trabajo futuro con
  causa tecnica** (sin baseline MM-GDINO geometricamente sana el delta es
  ininterpretable), **jamas por "falta de tiempo"**. **D-FT-15** fijo los margenes de T2
  **antes de todo resultado T2**, con la retencion de vocabulario abierto sobre COCO
  val2017 congelada en mAP50 **0,434676 => umbral NO-GO 0,391208**, y con la expectativa
  **pre-registrada** de que T2 tambien de NO-GO. **T2 esta enviado y en cola, sin
  empezar**: no tiene ni una cifra. Al redactar, la secuencia se cuenta completa y en ese
  orden —veredicto, enmienda posterior, margenes firmados por adelantado—: **la
  transparencia de la secuencia ES el argumento**, y suavizarla la destruye.
- **Acoples vigentes (ADR-020, 2026-08-18):** los patrones de acople son DOS, no tres.
  **(a) HTTP config-driven en los TRES modulos** de la plataforma: medios `:8080`,
  control `:8081` y **distribucion `:8082`** (`eovrt-distribute serve`), con la
  webconsole y el runner como clientes de los tres — ninguno consume el bus.
  **(b) bus ZeroMQ PUB/SUB + msgpack** para el dato: detecciones `:5557`
  (medios->control), alertas `:5558` (control->distribucion).
  **NO escribir "BFF-subproceso" ni contar un tercer patron.** El subproceso del
  distribuidor sigue en el codigo como **fallback operativo**
  (`EOVRT_CONSOLE_DISTRIBUTION_TRANSPORT=subprocess`) — implementado y probado, pero
  es un detalle de operacion, no arquitectura, y no va al informe. Tampoco escribir
  "el modulo es una CLI y no un servicio": es servicio, y ademas conserva su CLI
  para el camino offline (igual que el control-plane).
  *(Historia del numero, solo para quien la necesite — ningun documento anterior al
  2026-08-18 describe el estado vigente de arriba: ADR-018 (2026-08-15) declaro que
  "la plataforma tiene TRES patrones de acople, no dos", con el tercero siendo
  **BFF-subproceso** porque el modulo de distribucion, que es CLI y no servicio,
  no tenia otra forma de acoplarse. ADR-019 (2026-08-17/18) le dio servicio HTTP
  propio al distribuidor sin cambiar el conteo — seguian siendo tres. **ADR-020**,
  el mismo dia, derogo a ADR-018 e invirtio el default: HTTP paso a ser el acople
  normal, el subproceso bajo a fallback, y volvieron a ser DOS.)*
- **La containerizacion SI se puede mencionar en el informe** (✎ 2026-08-18, precision del
  usuario — antes esto se leia como "no mencionarla"). Esta **diferida con causa**
  (ADR-019 §4): se va a hacer **despues** de cerrar la redaccion, su razon de ser es la
  **reproducibilidad** de la plataforma —que un tercero pueda levantarla en otra maquina—
  y **no** cerrar el informe, y su **documentacion operativa vive en los repositorios**
  (`infra/`, READMEs), no en la tesis. **Como escribirla:** como **trabajo comprometido
  con su causa**, en el cierre (§17.6/§18) y en el camino de reproducibilidad (§19).
  **Como NO escribirla:** en presente, como capacidad existente, o con instrucciones de
  despliegue — el informe no es un manual. La frase que gobierna: *describir el compromiso
  y su fundamento es correcto; describir un despliegue que no corrio es falso.*
- **Metricas de `report.json`**: `t_alert-system` es **citable** (esta en el diccionario de
  la spec 40 §5.1 y siempre debio figurar; dejo de estar clavada en `not_applicable`).
  `precision_alertas` / `recall_alertas` / `F1_alertas` **existen pero NO son citables**:
  duplican cifras que ya se reportan via `evaluate-alerts` con denominadores por estrato.
  **La citabilidad esta materializada**: `t_alert-system` ES la columna `t_alert` del
  clip bench (campo `t_alert_system_ms` de cada `metrics.json`) — citable por campana y
  por condicion, nunca promediada entre campanas. NO confundir con `t_alert-notification`
  (bus→PUBACK, la campana de distribucion): son tramos con relojes distintos y **los
  percentiles no se suman entre tramos** — la cadena temporal completa se cita POR TRAMOS
  segun la tabla de `results/index.md`.
- Las cifras se toman del índice raíz `results/index.md` (limitaciones L1–L8 y procedencia)
  más los 4 índices canónicos (`bench_imagenes`, `bench_nivel_a`, `clip_bench`,
  `realtime`), incluidos en la sección de resultados operativa. Ante una contradiccion,
  manda este estado, luego el banner mas reciente de la fuente y finalmente su cuerpo
  historico.

## Contrato de uso

- **Etapa activa:** 0 - Etapa 0: secciones 11 a 14 y ajustes transversales.
- Este archivo contiene el texto vigente que se modifica y sus insumos de ajuste.
- No se trasladan resultados propios hacia secciones cronologicamente anteriores.
- Nombre propio de esta etapa (01-etapa-0-activa.md): regenerarla no pisa el paquete de ninguna otra etapa.

---

## Fuente: `docs/informe/entregable/96a-informe-v11-frontmatter-intro-objetivos-plan.md`

> SHA-256 del bloque: `65ee1710f1317a82c1c51928797e873be5537d1542f76be0d9cb8e98f77b969d`  
> Seleccion: texto vigente de las secciones 11 a 14.

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

---

## Fuente: `docs/informe/ajustes/00-mapa-de-ajustes.md`

> SHA-256 del bloque: `96c69fa216a61363d5ebb4f06e3d5289d4a2634b66b383e024a32fa6436e5671`  
> Seleccion: ajustes AJ-0.01 a AJ-0.07.

## 4. Etapa 0 — ajustes transversales del frontmatter (§11–§14)

Van acá porque no pertenecen a ninguna etapa: son el encuadre del documento.

| ID | Sección | Tipo | Pri | Enunciado | Fuente del texto |
|---|---|---|---|---|---|
| **AJ-0.01** | §12.4 Alcance, límites y condiciones | CONTRADICE | 🔴 | El alcance declarado quedó viejo: **ADR-015 registra que el alcance CRECIÓ**, no que se recortó (E-03 pasó de demostrativa a capacidad operativa medida; E-07 parcial; E-13 ejecutada y refutada). ✎ 2026-08-10: sobre la **distribución MQTT** manda **ADR-016** — dejó de ser exclusión cerrada y es **trabajo comprometido**, se declara con su estado al momento de la entrega (E-06 sigue excluida). ✎ 2026-08-11: sobre el **fine-tuning** manda **ADR-017** — E-04 dejó de ser exclusión y es **jornada experimental comprometida**, encuadrada como rama condicionada por datos y protocolo (nunca "por tiempo"). | `decisiones/adr-015-cierre-de-alcance.md` (§2a/§3/§4/§5 ratificados) + `adr-016-reapertura-acotada-distribucion.md` + `adr-017-fine-tuning-jornada-experimental.md` + `nucleo/10-registro-alcance-y-exclusiones.md` |
| **AJ-0.02** | §11 Glosario y símbolos | PRECISA | 🟠 | El vocabulario canónico vigente es **`person`, `helmet`, `vest`, `bare_head`** (`canonical_v2`); `canonical_cr01_cr02` está deprecado. Y hay que declarar las **colisiones de etiquetas**: "limitación L1" ≠ `L1` de la Fase L · `AF-1…AF-11` ≠ `A1–A5` · **dos series de ADR** (`ADR-001…018` del proyecto vs `ADR-0001…0013` del control-plane, 4 dígitos). | `13-glosario-y-convenciones-de-lectura.md` §4.1–4.3 · `gobierno/99` §4.1–4.2 |
| **AJ-0.03** | §14.3 Cronograma · Figura 1 (Gantt) | ERRATA | 🟡 | **El Gantt está vencido.** Sus seis filas dan: investigación 31/10/25–28/11/25 · análisis 05/12/25–09/01/26 · diseño 16/01/26–06/03/26 · **implementación MVP 20/03/26–29/05/26** · evaluación 12/06/26–10/07/26 · **documentación y defensa 17/07/26–21/08/26**. La implementación siguió hasta agosto, el tramo experimental cerró el 2026-08-09 y la defensa es ~fin de septiembre. Hay que regenerar la figura o declarar la desviación. *(Verificado extrayendo la imagen del `.docx`, 2026-08-10.)* | Figura 1 del `96a` |
| **AJ-0.04** | §14.2 Etapas | PRECISA | 🟡 | Las semanas del plan **no se leen literalmente** (ADR-010 reordenó: plataforma primero, dataset/GT de evaluación al final). Lo que sí vale y conviene explicitar es la **correspondencia 1:1 con las fases de la Tabla 36** — es coherencia metodológica gratis en la defensa. | `nucleo/08` §2.4 + `decisiones/adr-010-secuenciacion-plataforma-primero.md` |
| **AJ-0.05** | §17.2 Costos asociados · §14.4 | EVIDENCIA | 🟡 | **Hueco abierto, no relevado.** Nadie contrastó todavía los costos declarados contra lo efectivamente gastado. Para T1, la extrapolación medida da ≈16 min centrales (prudente 30–45 min; walltime 2 h), `operacion/100` adenda; la cifra histórica “≈1 GPU-h” quedó superada. | a relevar — insumo parcial en `operacion/100` §6 |
| **AJ-0.06** | §14.2 · introducción de §17 | CONCRETA | 🟠 | **El informe está ordenado por sección y casi no menciona las etapas.** Las etapas son la **guía de desarrollo** del proyecto, no una estructura del documento, y hoy el lector no tiene forma de saber qué sección corresponde a qué etapa. Agregar la **tabla de correspondencia etapa → sección** (la del §0 de este mapa): cierra el círculo entre el plan de trabajo declarado en §14 y el desarrollo del producto en §17. | §0 de este documento |
| **AJ-0.07** | fuera de §17.3 | PRECISA | 🟡 | Inventario de datasets desactualizado. **Ya tiene ID propio en Etapa 3: es `R-24`** — se enruta desde acá para que no se pierda, pero su ficha canónica está en `material-etapa-3/93`. | `material-etapa-3/93` · R-24 |

---

