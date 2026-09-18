# 90 — Texto extraído del INFORME FINAL completo v0.1 (bajada del 2026-09-16): portada, §2–§19, Anexos A–F y Referencias. Limpio: sin comentarios ni cambios rastreados. Supersede las fotos por sección (90b–90g, 96a, 96e), archivadas.

> **Extracción derivada (2026-09-18)** del `.docx`
> `informe/entregable/desarrollando/E-OVRT-VDP_Informe_Final_2026-09-16_v0.1.docx`, **solo para búsqueda y cita**
> (mismo estatuto que el doc 90): al editar, se edita el `.docx`/Google Docs, nunca
> este archivo. Tablas y figuras pueden haber perdido formato; las figuras no se
> extraen y las ecuaciones no se convierten — quedan `⟦FIGURA: no extraída — ver el .docx⟧` y
> `⟦ECUACIÓN: no extraída — ver el .docx⟧` donde estaban. Regenerado con
> `herramientas/extraer_informe.py` (regla D-C del manual de aplicación).

---

**CENTRO REGIONAL UNIVERSITARIO CÓRDOBA IUA**

**FACULTAD DE INGENIERÍA**

⟦FIGURA: no extraída — ver el .docx⟧

**PROYECTO INTEGRADOR**

**PLATAFORMA EXPERIMENTAL DE DETECCIÓN OPEN-VOCABULARY EN VIDEO EN TIEMPO REAL PARA MONITOREO ASISTIVO DE RIESGOS EN CONSTRUCCIÓN**

**INGENIERÍA EN INFORMÁTICA**

**TUTOR**

García Mattio, Mariano

**INTEGRANTES**

Carrizo, Matías Lautaro

Guillaumet, Gabriel Agustín

Llamosas, Simon

## 2. Hoja de Aceptación del Trabajo Final

*[se completará más adelante]*

## 3. Dedicatoria

*[se completará más adelante]*

## 4. Agradecimientos

*[se completará más adelante]*

## 5. Título del proyecto

Plataforma experimental de detección open-vocabulary en video en tiempo real para monitoreo asistivo de riesgos en construcción.

## 6. Abstract

### Resumen

Se investigó la factibilidad de transformar condiciones de riesgo expresadas en lenguaje natural en alertas trazables sobre video para monitoreo asistivo en construcción. Se diseñó, implementó y evaluó E-OVRT-VDP, una plataforma que separa ingesta e inferencia, interpretación temporal y distribución de alertas, con configuraciones y registros reproducibles. El núcleo utilizó modelos preentrenados sin ajuste de pesos y abordó persona sin casco y persona sin chaleco reflectivo. La evaluación distinguió percepción por imagen, estado por persona y alerta por episodio, mediante procesamiento diferido y pruebas en vivo. El banco temporal reunió 47 clips —32 positivos y 15 negativos— y 37 episodios, con resultados separados para rodaje guionado y obra real. Con Grounding DINO tiny a 560 píxeles y estrategia indirecta, mantener estados por sujeto elevó el F1 de alertas de 0,789 a 0,930 frente a la granularidad de escena, sobre 34 episodios evaluables del rodaje y con detecciones idénticas. En cambio, sobre 11 clips negativos de obra real se registraron 26 falsos positivos por escena y 323 por sujeto. La operación en vivo quedó verificada, aunque la inferencia excedió el presupuesto de latencia. La rama separada de ajuste fino no produjo una variante que cumpliera los criterios de incorporación. Se comprobó la factibilidad técnica de la cadena, no su aptitud operativa general ni una superioridad frente a detectores supervisados. El aporte es una plataforma configurable y auditable que permite medir el efecto de las decisiones perceptivas y temporales y delimitar sus condiciones de uso.

**Abstract**

This study investigated the feasibility of transforming risk conditions expressed in natural language into traceable video alerts for assistive construction safety monitoring. E-OVRT-VDP was designed, implemented, and evaluated as a platform separating video ingestion and inference, temporal interpretation, and alert distribution through reproducible configurations and records. Its core used pretrained models without weight adaptation and addressed persons without hard hats and persons without reflective vests. Evaluation distinguished image perception, per-person state, and episode-level alerts through offline processing and live tests. The temporal benchmark comprised 47 clips—32 positive and 15 negative—and 37 episodes, with results reported separately for scripted recordings and real construction footage. Using Grounding DINO tiny at 560 pixels with an indirect strategy, maintaining per-person states increased alert F1 from 0.789 to 0.930 compared with scene-level granularity, over 34 evaluable scripted episodes with identical detections. Conversely, the 11 negative real construction clips produced 26 false positives at scene level and 323 at person level. Live operation was verified, although inference exceeded the latency budget. A separate fine-tuning branch produced no variant meeting the adoption criteria. The results established the technical feasibility of the processing chain, rather than general operational suitability or superiority over supervised detectors. The contribution is a configurable, auditable platform that enables measurement of perceptual and temporal decisions and delineation of their conditions of use.

## 7. Palabras clave

- Detección de vocabulario abierto

- Modelos visión-lenguaje

- Visión por computadora

- Procesamiento de video en tiempo real

- Evaluación de alertas temporales

- Seguridad laboral en construcción civil

- Patrones de riesgo

- Arquitectura orientada a eventos

- Trazabilidad experimental

- Seguimiento multiobjeto

## Tabla de contenido

**8. Tabla de contenido .................................................................................................................	9**

**9. Índice de Gráficos .................................................................................................................	20**

**10. Índice de Tablas ..................................................................................................................	21**

**11. Glosario, listado de símbolos y convenciones ...................................................................	26**

**12. Introducción ........................................................................................................................	39**

12.1. Motivación y contexto del proyecto ............................................................................	39

12.2. Problema identificado .................................................................................................	40

12.3. Enfoque propuesto e hipótesis de trabajo ....................................................................	41

12.4. Alcance, límites y condiciones de trabajo ...................................................................	43

12.5. Enfoque metodológico general ....................................................................................	44

**13. Objetivos del proyecto .......................................................................................................	45**

13.1. Objetivo general ..........................................................................................................	45

13.2. Objetivos específicos ...................................................................................................	46

**14. Plan De Trabajo De Proyecto Integrador ........................................................................	47**

14.1. Enfoque general de trabajo ..........................................................................................	47

14.2. Etapas del proyecto .....................................................................................................	47

14.2.1. Etapa 1 - Investigación bibliográfica y fundamentación teórica ........................	47

14.2.2. Etapa 2 - Análisis metodológico y estrategia de evaluación ..............................	48

14.2.3. Etapa 3 - Diseño arquitectónico de la plataforma experimental ........................	49

14.2.4. Etapa 4 - Implementación del prototipo experimental .......................................	50

14.2.5. Etapa 5 - Evaluación y validación de desempeño ..............................................	51

14.2.6. Etapa 6 - Documentación final, revisión y presentación ....................................	51

14.3. Cronograma y esquema gráfico ...................................................................................	53

14.4. Costos asociados al proyecto .......................................................................................	54

**15. Estado del arte ....................................................................................................................	55**

15.1. Alcance del estado del arte y propósito de la fundamentación teórica .......................	55

15.2. Detección open-vocabulary: modelos, paradigmas y brechas del estado del arte .......	56

15.2.1. Paradigmas arquitectónicos y modelos representativos .....................................	56

15.2.1.1. Detectores end-to-end derivados de DETR/DINO con fusión multimodal profunda ...................................................................................................................	58

15.2.1.2. Detectores one-stage de la familia YOLO con alineamiento región-texto .	59

15.2.1.3. Detectores dual-encoder CLIP-like con correspondencia por similitud ...	61

15.2.1.4. Modelos guiados por prompts generalistas: formulaciones generativas e híbridas .....................................................................................................................	61

15.2.2. Composición de modelos y pipelines de percepción .........................................	62

15.2.3. Síntesis comparativa y trade-offs para tiempo real ............................................	63

15.2.3.1. Análisis de rendimiento para tiempo real ..................................................	69

15.2.4. Adaptabilidad mediante fine-tuning y preservación de capacidad open-vocabulary .............................................................................................................	71

15.2.5. Brechas identificadas en el dominio de la construcción civil ............................	75

15.2.5.1. Contextualización semántica limitada .......................................................	75

15.2.5.2. Ausencia de consistencia temporal nativa .................................................	76

15.2.5.3. Sensibilidad a la formulación del prompt .................................................	76

15.2.5.4. Sensibilidad al dominio de aplicación .......................................................	77

15.2.5.5. Protocolos de evaluación específicos para seguridad industrial ...............	79

15.2.5.6. Tabla comparativa de brechas identificadas ..............................................	80

15.2.6. Síntesis de la sección y avance al seguimiento multi-objeto ..............................	84

15.3. Seguimiento multiobjeto: métodos, métricas y brechas del estado del arte ................	84

15.3.1. Métodos representativos .....................................................................................	85

15.3.1.1. SORT .........................................................................................................	85

15.3.1.2. Contraste con variantes posteriores ...........................................................	85

15.3.2. Síntesis comparativa de métodos MOT .............................................................	86

15.3.2.1. Observaciones críticas sobre la comparativa ............................................	89

15.3.3. Métricas de evaluación para MOT .....................................................................	89

15.3.4. Brechas identificadas y desafíos para el prototipo .............................................	90

15.4. Video en tiempo real y streaming: protocolos, servidores y brechas del estado del arte ........................................................................................................................................	93

15.4.1. Protocolos de transmisión de video de baja latencia ..........................................	93

15.4.1.1. Criterios de clasificación de protocolos ....................................................	94

15.4.1.2. Mapa de familias de protocolos según los criterios de clasificación ........	95

15.4.2. Alternativas complementarias de ingesta, transporte y distribución ..................	96

15.4.3. Brechas del estado del arte en el streaming/OVD ..............................................	98

15.4.3.1. Ausencia de benchmarks extremo a extremo integrados para pipelines OVD .........................................................................................................................	98

15.4.3.2. Integración de modelos OVD dentro de pipelines de streaming optimizados ..............................................................................................................	98

15.4.3.3. Interoperabilidad efectiva entre protocolos heterogéneos .........................	99

15.4.3.4. Métricas de evaluación alineadas con objetivos de seguridad laboral ......	100

15.4.4. Síntesis comparativa de protocolos ....................................................................	100

**16. Marco teórico ....................................................................................................................	105**

16.1. Organización interna del marco teórico ....................................................................	105

16.2. Condiciones de riesgo observables ...........................................................................	108

16.2.1. Marco normativo de referencia ........................................................................	108

16.2.2. Operacionalización de las condiciones nucleares ............................................	109

16.2.3. Alcance y límites de la observación visual ......................................................	111

16.3. Percepción visión-lenguaje: fundamentos conceptuales de la detección open-vocabulary .................................................................................................................	112

16.3.1. Del closed-set al open-vocabulary ...................................................................	112

16.3.2. Mecanismos de alineación visión-lenguaje ......................................................	113

16.3.3. Rol del lenguaje natural como especificación dinámica ..................................	114

16.3.4. Composicionalidad, negación y condiciones definidas por ausencia ..............	115

16.3.5. Generalización zero-shot y el problema del long-tail semántico .....................	117

16.3.6. Dimensiones de comparación de modelos OVD ..............................................	117

16.4. Persistencia temporal de entidades y fundamentos conceptuales del seguimiento multiobjeto .........................................................................................................................	118

16.4.1. La limitación temporal de la detección por cuadro ..........................................	118

16.4.2. Fundamentos del MOT y del paradigma tracking-by-detection ......................	119

16.4.3. Integración conceptual entre OVD y MOT ......................................................	121

16.5. Operación en tiempo real, transmisión y procesamiento cercano a la fuente ...........	122

16.5.1. La latencia extremo a extremo como restricción de diseño .............................	122

16.5.2. Descomposición instrumental de Glass-to-Algorithm .....................................	124

16.5.3. Separación de planos y flujo productor-consumidor ........................................	129

16.5.4. Computación en el borde y filtrado cercano al origen .....................................	130

16.5.5. Brecha de evaluación integrada ........................................................................	132

16.6. Marco ético-legal para el análisis automatizado de video en entornos laborales ......	133

16.6.1. Protección de datos y finalidad del tratamiento ...............................................	133

16.6.2. Minimización, seguridad y exclusión de identificación personal ....................	134

16.6.3. Supervisión humana, trazabilidad y alcance asistivo .......................................	135

16.7. Convergencias y preguntas rectoras ..........................................................................	135

16.7.1. Interdependencia de los dominios ....................................................................	135

16.7.2. Del marco conceptual al protocolo experimental .............................................	136

16.7.3. Preguntas rectoras para la consolidación metodológica ...................................	136

16.8. Conclusiones parciales de la fundamentación teórica ...............................................	138

**17. Desarrollo del producto ...................................................................................................	139**

17.1. Consolidación metodológica del protocolo experimental .........................................	139

17.1.1. Función y alcance de la consolidación metodológica ......................................	139

17.1.2. Alcance experimental consolidado del prototipo .............................................	140

17.1.2.1. Catálogo de condiciones de riesgo y alcance de validación ....................	140

17.1.3. Diseño metodológico general y lógica de escenarios .......................................	141

17.1.3.1. Patrón de riesgo como unidad de análisis ...............................................	141

17.1.3.2. Cadena operativa mínima y motor de patrones .......................................	141

17.1.3.3. Escenarios de evaluación ........................................................................	141

17.1.3.4. Decisiones estructurales del diseño metodológico ..................................	142

17.1.4. Entorno experimental, infraestructura y escenarios de evaluación ..................	145

17.1.4.1. Infraestructura y roles de ejecución ........................................................	145

17.1.4.2. Escenarios de evaluación ........................................................................	146

17.1.5. Condiciones de riesgo, patrones y protocolo de prompts .................................	150

17.1.5.1. Catálogo de condiciones de riesgo y evaluabilidad ................................	150

17.1.5.2. Patrones de riesgo y criterios de activación ............................................	155

17.1.5.3. Diseño de prompts OVD .........................................................................	163

17.1.5.4. Protocolo de evaluación y congelamiento de prompts ............................	168

17.1.6. Estrategia de datos, benchmarks y partición ....................................................	170

17.1.6.1. Alcance y criterios de selección ..............................................................	170

17.1.6.2. Fuentes de gestión directa, cobertura y brechas ......................................	173

17.1.6.3. Asignación de roles y partición experimental .........................................	179

17.1.6.4. Benchmarks de referencia para seguimiento ...........................................	182

17.1.6.5. Licencias, ética y logística de datos ........................................................	184

17.1.7. Framework de métricas, viabilidad operativa y presupuesto de latencia .........	185

17.1.7.1. Propósito, alcance y principio de aplicabilidad .......................................	185

17.1.7.2. Niveles de evaluación y jerarquía de evidencia ......................................	186

17.1.7.3. Métricas adoptadas y reglas de lectura ....................................................	190

17.1.7.4. Comparación entre línea base zero-shot y variante ajustada ...................	192

17.1.7.5. Presupuesto temporal y referencias por severidad ..................................	193

17.1.7.6. Instrumentación, aplicabilidad y reporte .................................................	200

17.1.8. Protocolo experimental integrado ....................................................................	201

17.1.9. Estrategia de adaptación al dominio .................................................................	203

17.1.10. Supuestos, riesgos de validez y consideraciones ético-legales ......................	206

17.1.11. Conclusiones parciales de la consolidación metodológica ............................	209

17.2. Costos asociados .......................................................................................................	209

17.2.1. Alcance y supuestos de la evaluación económica ............................................	209

17.2.2. Esfuerzo del equipo ..........................................................................................	211

17.2.3. Recursos materiales aportados .........................................................................	212

17.2.4. Infraestructura, operación y mantenimiento .....................................................	214

17.2.5. Gasto efectivo, financiamiento, ahorros e ingresos ..........................................	217

17.3. Diseño arquitectónico ................................................................................................	220

17.3.1. Propósito y pregunta rectora ............................................................................	220

17.3.2. Alcance, capacidades y decisiones arquitectónicas ..........................................	220

17.3.2.1. Capacidades arquitectónicas requeridas ..................................................	221

17.3.2.2. Requisitos no funcionales de referencia ..................................................	226

17.3.2.3. Decisiones arquitectónicas y principios de lectura .................................	228

17.3.3. Vista general y patrones de acople ...................................................................	232

17.3.4. Configuración experimental, vocabulario y estrategia del núcleo ...................	236

17.3.4.1. Configuración de corrida como artefacto de reproducibilidad ................	237

17.3.4.2. Diseño de prompts y vocabulario activo .................................................	241

17.3.4.3. Vocabulario y estrategia del núcleo validable .........................................	241

17.3.4.4. Reglas de comparabilidad entre configuraciones ....................................	246

17.3.5. Diseño conceptual del plano de medios ...........................................................	246

17.3.5.1. Flujo operativo del Pipeline de Medios ...................................................	249

17.3.5.2. Capacidades opcionales y degradación segura ........................................	252

17.3.6. Diseño conceptual del plano de control ...........................................................	253

17.3.6.1. Máquina de estados y ciclo del episodio .................................................	254

17.3.6.2. Motor de evaluación y definición de patrón ............................................	257

17.3.6.3. Transporte, persistencia y trazabilidad experimental ..............................	264

17.3.6.4. Cadena de traducción entre condición, evidencia, patrón y alerta ..........	265

17.3.7. Distribución de alertas confirmadas .................................................................	268

17.3.8. Contratos, trazabilidad y evidencia visual ........................................................	272

17.3.8.1. Contratos mínimos e interfaces ...............................................................	272

17.3.8.2. Repositorio de hechos y reconstrucción experimental ............................	276

17.3.8.3. Política de evidencia visual mínima ........................................................	277

17.3.9. Observabilidad y aplicabilidad de métricas .....................................................	278

17.3.10. Escenarios experimentales y topología de referencia ....................................	282

17.3.10.1. Equivalencia arquitectónica y alcance de EBE .....................................	283

17.3.10.2. Naturaleza temporal de la fuente y aplicabilidad ..................................	287

17.3.10.3. Roles funcionales y unidades desplegables de referencia .....................	287

17.3.11. Riesgos, plan de materialización y cierre .......................................................	290

17.4. Implementación del prototipo experimental .............................................................	293

17.4.1. Componentes construidos y cadena de datos ...................................................	293

17.4.2. Correspondencia y contratos materializados ....................................................	296

17.4.3. Servicios, gobierno por configuración y acople ...............................................	304

17.4.4. Configuración efectiva y catálogo de modelos ................................................	309

17.4.5. Artefactos y trazabilidad por corrida ................................................................	311

17.4.6. Banco temporal y referencia humana de evaluación ........................................	314

17.4.7. Verificación, alcance efectivo y brechas ..........................................................	317

17.4.8. Extensibilidad y costo de extensión .................................................................	326

17.5. Evaluación y validación del prototipo .......................................................................	331

17.5.1. Encuadre y reglas de lectura .............................................................................	331

17.5.2. Percepción sobre imágenes ..............................................................................	332

17.5.3. Estado por persona ...........................................................................................	335

17.5.4. Alerta por episodio contra la referencia temporal humana ..............................	339

17.5.5. Tiempo real ......................................................................................................	344

17.5.6. Caminos probados y no adoptados ...................................................................	349

17.5.7. Lo no ejecutado y lo no implementado ............................................................	353

17.6. Documentación técnica, repositorio y evidencias de cierre ......................................	356

17.6.1. Organización del software y de la documentación ...........................................	356

17.6.2. Identificación de las ejecuciones y conservación de la evidencia ....................	357

17.6.3. Verificaciones automatizadas y alcance de la comprobación ..........................	358

17.6.4. Estado de entrega y límites de reproducibilidad ..............................................	359

**18. Cierre del proyecto ...........................................................................................................	361**

18.1. Respuesta a la hipótesis y alcance de la factibilidad .................................................	361

18.2. Expresividad semántica, selección del perfil y extensibilidad ..................................	362

18.3. Aporte temporal de la plataforma y cambio de régimen en obra real .......................	364

18.4. Funcionamiento en vivo y restricciones de oportunidad ...........................................	365

18.5. Interpretación de la rama de ajuste fino ....................................................................	367

18.6. Balance de objetivos y líneas de continuidad ............................................................	369

**19. Anexos ...............................................................................................................................	372**

19.1. Anexo A - Comparativas técnicas y estado del arte complementario .......................	373

19.2. Anexo B - Infraestructura, nodos y parámetros experimentales ...............................	379

19.3. Anexo C - Prompts, datos, datasets, benchmarks y logística ....................................	388

19.4. Anexo D - Métricas, instrumentación y bitácora experimental .................................	393

19.5. Anexo E - Reproducibilidad y comprobación de la evidencia ..................................	399

19.6. Anexo F - Procedencia, licencias y tratamiento del material ....................................	406

**Referencias ..............................................................................................................................	411**

## 9. Índice de Gráficos

Figura 1	Diagrama de Gantt de las etapas previstas del proyecto	53

Figura 4.1	Vista conceptual de la arquitectura E-OVRT-VDP	234

Figura 4.2	Flujo conceptual del Pipeline de Medios	248

Figura 4.3	Máquina de estados del motor de patrones	256

Figura 4.4	Cadena de traducción entre condición, estrategia, evidencia, patrón y alerta	267

Figura 4.5	Vista de procesos y patrones de acople de la plataforma experimental	295

Figura 4.6	Fotograma con alerta confirmada de CR-01	343

## 10. Índice de Tablas

Tabla 1	Glosario y listado de símbolos y convenciones del proyecto E-OVRT-VDP	26

Tabla 2	Síntesis comparativa de paradigmas arquitectónicos OVD según dimensiones relevantes para sistemas de video en tiempo real	64

Tabla 3	Análisis comparativo de rendimiento de modelos OVD para tiempo real	70

Tabla 4	Estrategias de fine-tuning documentadas y retención OVD reportada por familia arquitectónica	73

Tabla 5	Brechas identificadas en la aplicación de modelos OVD al dominio de seguridad en construcción civil	81

Tabla 6	Síntesis comparativa de métodos MOT representativos según dimensiones relevantes para sistemas de video en tiempo real con detección open-vocabulary	87

Tabla 7	Brechas identificadas en la aplicación de métodos MOT al contexto de seguridad en construcción civil en combinación con detección open-vocabulary	91

Tabla 8	Comparativa de protocolos de transmisión de video de baja latencia para sistemas de video analítico en tiempo real	101

Tabla 9	Correspondencia entre dominios del marco teórico, preguntas articuladoras y contribución al proyecto	106

Tabla 10	Operacionalización de las condiciones nucleares del trabajo	110

Tabla 11	Componentes instrumentales del subtramo Glass-to-Algorithm	125

Tabla 12	Decisiones estructurales del diseño metodológico	143

Tabla 13	Comparación de los escenarios de evaluación DBE y EBE	148

Tabla 14	Catálogo de condiciones de riesgo seleccionadas para el prototipo experimental	152

Tabla 15	Catálogo de patrones de riesgo del prototipo E-OVRT-VDP	160

Tabla 16	Criterios de evaluación para la selección de fuentes de datos	172

Tabla 17	Fuentes retenidas para gestión directa y papel metodológico posible	174

Tabla 18	Fuentes no retenidas para el uso principal y motivo metodológico	175

Tabla 19	Cobertura de datos por condición y consecuencia metodológica	177

Tabla 20	Condiciones metodológicas para la partición de datos	181

Tabla 21	Benchmarks de referencia para el módulo de seguimiento	183

Tabla 22	Framework de métricas por nivel de evaluación y familia de evidencia	188

Tabla 23	Tramos temporales y condiciones de instrumentación	195

Tabla 24	Referencias temporales orientativas por severidad	199

Tabla 25	Fases del protocolo experimental integrado	202

Tabla 26	Regla metodológica de decisión para la adaptación al dominio	204

Tabla 27	Riesgos metodológicos y operativos relevantes para las instancias siguientes	207

Tabla 28	Esfuerzo del equipo. Horas-persona previstas y ejecutadas	211

Tabla 29	Recursos materiales aportados. Condición de uso y origen	213

Tabla 30	Infraestructura, operación y mantenimiento. Magnitud de uso registrada y gasto	215

Tabla 31	Resumen del proyecto. Esfuerzo, recursos aportados, gasto efectivo y fuentes de financiamiento	217

Tabla 32	Capacidades arquitectónicas y su tratamiento en el diseño	222

Tabla 33	Requisitos no funcionales de referencia	226

Tabla 34	Decisiones arquitectónicas iniciales	228

Tabla 35	Elementos mínimos de la configuración experimental	238

Tabla 36	Vocabulario de prompts en inglés del núcleo validable y de las ramas comparativas	244

Tabla 37	Diseño del motor de patrones según condición de riesgo	261

Tabla 38	Consumidores y salidas del tramo de distribución	270

Tabla 39	Contratos mínimos para la ejecución experimental	273

Tabla 40	Métricas y evidencias por tramo arquitectónico	279

Tabla 41	Señales observables del sistema	280

Tabla 42	Condiciones observables para interpretar EBE	285

Tabla 43	Correspondencia de diseño entre roles funcionales y unidades desplegables de referencia	289

Tabla 44	Riesgos arquitectónicos y mitigaciones de diseño	290

Tabla 45	Plan de materialización del núcleo	292

Tabla 46	Correspondencia entre los contratos del diseño y su materialización efectiva	297

Tabla 47	Interfaces principales de los servicios de la plataforma	306

Tabla 48	Artefactos persistidos por componente y experimento	312

Tabla 49	Evidencia de verificación técnica del prototipo	319

Tabla 50	Puntos de extensión y costo técnico de incorporación	327

Tabla 51	Resultados de percepción por combinación en el banco congelado	333

Tabla 52	Resultados de estado por persona	337

Tabla 53	Alerta por episodio en el bloque de rodaje guionado	340

Tabla 54	Resultados del camino en vivo por densidad, integridad y tramo temporal	346

Tabla 55	Curva de capacidad de la rama comparativa de ajuste fino	351

Tabla A.1	Matriz ampliada de alternativas de detección open-vocabulary y modelos relacionados	373

Tabla A.2	Comparación conceptual de métricas MOT y sus límites para evaluar alertas temporales	378

Tabla B.1	Equipo de referencia del nodo central de procesamiento	379

Tabla B.2	Fuente de captura propia y capacidades del nodo de borde	380

Tabla B.3	Entorno de software de procesamiento: utilizado y no ejercido	381

Tabla B.4	Recurso institucional para la rama de ajuste fino	382

Tabla B.5	Identificación de las ejecuciones de ajuste fino	383

Tabla B.6	Parámetros de referencia y configuraciones identificadoras del núcleo	384

Tabla B.7	Topología y fronteras operativas de la ejecución en vivo	386

Tabla C.1	Catálogo de prompts candidatos por condición de riesgo	388

Tabla C.2	Variables de sensibilidad candidatas para el Environment-Based Evaluation	390

Tabla C.3	Logística de conversión y acceso de los datasets retenidos	392

Tabla D.1	Métricas de rendimiento del pipeline y uso de recursos	393

Tabla D.2	Insumos mínimos requeridos antes de iniciar una campaña de medición	395

Tabla D.3	Campos mínimos recomendados para la bitácora experimental	397

Tabla E.1	Artefactos de referencia y comprobaciones de reproducción	400

Tabla E.2	Huellas de referencia de los materiales congelados	401

Tabla F.1	Procedencia de los datos y condiciones de conservación	407

## 11. Glosario, listado de símbolos y convenciones

**Tabla 1**

*Glosario y listado de símbolos y convenciones del proyecto E-OVRT-VDP*

| **Término / sigla** | **Definición / uso en el trabajo** |
| --- | --- |
| E-OVRT-VDP | Experimental Open-Vocabulary Real-Time Video Detection Platform. Nombre abreviado de la plataforma experimental desarrollada en el trabajo. |
| Inteligencia artificial | Disciplina orientada al desarrollo de sistemas capaces de realizar tareas que normalmente requieren inteligencia humana. |
| Visión por computadora | Área de la inteligencia artificial dedicada al procesamiento e interpretación de imágenes y video. |
| OVD | Open-Vocabulary Detection. Detección que vincula regiones visuales con consultas de un vocabulario definido en inferencia. No equivale, por sí sola, a reconocer una condición de riesgo ni a confirmar una alerta. |
| Closed-set detection | Detección de vocabulario cerrado. Enfoque en el que el modelo solo reconoce categorías definidas durante su entrenamiento. |
| Open-set | Concepto tratado en la fundamentación para describir la operación frente a categorías no vistas o no previstas durante el entrenamiento. No designa, por sí solo, una capacidad evaluada de manera independiente en el prototipo. |
| Zero-shot | Modalidad de inferencia en la que el modelo reconoce conceptos que no fueron objeto de un entrenamiento supervisado específico. En este trabajo designa el uso de modelos preentrenados sin ajuste de pesos con datos del dominio; la selección de consultas, umbrales y resolución es calibración operativa, no entrenamiento. |
| Prompt | Consulta o instrucción, generalmente textual, que especifica el concepto o condición que se desea detectar. |
| Prompt visual | Imagen o región de referencia utilizada para especificar visualmente un objeto o condición de interés. Se trata como modalidad de prompting en la revisión; no se utilizó en el núcleo evaluado. |
| Fine-tuning | Ajuste de un modelo preentrenado mediante datos adicionales de un dominio específico. |
| LoRA | Low-Rank Adaptation. Técnica de ajuste eficiente en parámetros revisada como alternativa de adaptación. No se ejecutó en la rama de ajuste fino del proyecto. |
| MOT | Multi-Object Tracking. Seguimiento multiobjeto; técnica para mantener identificadores consistentes de personas u objetos a lo largo del video. |
| Tracking-by-detection | Paradigma de seguimiento en el que primero se detectan objetos por fotograma y luego se asocian temporalmente entre cuadros consecutivos. |
| EPP / PPE | Equipo de Protección Personal (EPP; Personal Protective Equipment, PPE). Elementos destinados a proteger al trabajador, como casco, chaleco, guantes, calzado de seguridad o arnés. |
| Pub/Sub | Patrón publicador-suscriptor utilizado para desacoplar el transporte de eventos durante la ejecución. En la plataforma se materializa con ZeroMQ para detecciones y alertas confirmadas. |
| Patrón de riesgo | Definición configurable que transforma evidencia de una condición observable en un estado temporal y una eventual alerta, mediante reglas de asociación, confirmación y resolución. |
| Condición de riesgo observable | Estado visual definido para la evaluación asistiva de una situación de interés preventivo. Su observación no constituye, por sí sola, una determinación de incumplimiento normativo. |
| Arquitectura orientada a eventos (EDA) | Enfoque en el que los componentes producen y consumen eventos de forma desacoplada. En la plataforma sustenta el intercambio de hechos durante la ejecución, separado del gobierno de corridas por HTTP. |
| Plano de medios | Componente responsable de la ingesta visual, el control de ritmo, la normalización, la inferencia open-vocabulary, el postproceso y la publicación de eventos de percepción. |
| Plano de control | Componente que consume eventos de percepción, asocia evidencia a las condiciones, mantiene estados temporales, evalúa patrones y registra alertas confirmadas. |
| Streaming | Transmisión continua de datos multimedia, como audio o video, sin requerir descarga completa previa. |
| Latencia end-to-end | Tiempo entre los extremos explícitamente declarados de una cadena de procesamiento. En el informe se distinguen los tramos instrumentados y sus relojes, no se suman percentiles de tramos independientes. |
| Latencia de alerta | Intervalo entre el inicio del episodio de referencia y la alerta confirmada. En la evaluación temporal se expresa como t_alert-system, sobre el reloj de la fuente. |
| FPS | Frames per second o cuadros por segundo. Métrica de rendimiento que indica cuántos fotogramas procesa o visualiza el sistema por segundo. |
| Precisión | Proporción de detecciones positivas del sistema que son realmente correctas. |
| Recall | Proporción de instancias relevantes reales que fueron detectadas por el sistema. |
| F1-score | Media armónica entre precisión y recall; se utiliza para evaluar balanceadamente el desempeño de detección. |
| AP | Average Precision. Área bajo la curva precisión-recall de una clase bajo el criterio de solapamiento declarado. En los resultados propios, AP50 utiliza IoU = 0,50. |
| mAP | Mean Average Precision. Promedio del AP de las clases incluidas en una combinación bajo el mismo criterio de solapamiento. En los resultados propios, mAP50 promedia AP a IoU = 0,50; se distingue de AP@[0,50:0,95], que promedia múltiples umbrales. |
| MOTA | Multiple Object Tracking Accuracy. Métrica de seguimiento multiobjeto tratada en el marco teórico. No se utilizó para evaluar el prototipo. |
| IDF1 | Métrica de seguimiento que evalúa consistencia de identidad. No se utilizó para evaluar el prototipo. |
| HOTA | Higher Order Tracking Accuracy. Métrica que combina detección y asociación en seguimiento multiobjeto. No se utilizó para evaluar el prototipo. |
| DBE | Dataset-Based Evaluation. Escenario A: evaluación diferida y reproducible sobre archivos, con entradas y configuraciones declaradas. |
| EBE | Environment-Based Evaluation. Escenario B: evaluación en vivo, con captura continua e intercambio de eventos por bus entre componentes. |
| CPN | Central Processing Node. Nodo central de procesamiento encargado de ejecutar inferencia, evaluación de patrones o servicios principales. |
| EN | Edge Node. Nodo cercano a la fuente de captura, usado para adquisición, preprocesamiento o transmisión de video. |
| TN | Training Node. Nodo destinado a entrenamiento o adaptación de modelos, cuando corresponda. |
| Dataset | Conjunto de datos utilizado para entrenamiento, validación, prueba o análisis experimental. |
| Benchmark | Conjunto de referencia o procedimiento estandarizado para comparar desempeño entre modelos o configuraciones. |
| API | Application Programming Interface. Interfaz que permite que distintos componentes de software se comuniquen de forma estructurada. |
| Prototipo experimental | Versión funcional acotada de la plataforma, desarrollada con fines de investigación, validación técnica y evaluación controlada. Integra los componentes necesarios para poner a prueba la hipótesis de trabajo, sin constituir un producto final ni una solución lista para despliegue productivo. |
| HTTP | Hypertext Transfer Protocol. Se utiliza para el gobierno solicitud-respuesta de las corridas y para las consultas a los servicios de medios, control y distribución; no transporta los eventos de percepción ni las alertas confirmadas entre módulos. |
| MQTT | Protocolo de mensajería publicador-suscriptor utilizado en el canal externo de distribución de alertas confirmadas. |
| RTSP | Real Time Streaming Protocol. Protocolo de control de sesiones utilizado por las fuentes RTSP integradas en la plataforma. |
| RTP | Real-time Transport Protocol. Protocolo de transporte de audio y video tratado como fundamento de la combinación con RTSP; no se evaluó como alternativa independiente. |
| RTMP | Real-Time Messaging Protocol. Protocolo revisado como antecedente de streaming; no fue adoptado por el prototipo. |
| WebRTC | Tecnología y conjunto de protocolos para comunicación de audio, video y datos en tiempo real con baja latencia, analizada como alternativa interactiva. No fue un canal de visualización implementado por el prototipo. |
| SRT | Secure Reliable Transport. Alternativa de transporte de video orientada a confiabilidad y baja latencia en redes variables. Fue analizada en la fundamentación y no se utilizó para los resultados presentados. |
| HLS | HTTP Live Streaming. Antecedente de distribución segmentada sobre HTTP analizado en la fundamentación; no fue una salida del prototipo. |
| MPEG-DASH (DASH) | Dynamic Adaptive Streaming over HTTP. Técnica de streaming adaptativo basada en segmentos HTTP, analizada como antecedente; no fue una salida del prototipo. |
| ZeroMQ | Biblioteca de mensajería que materializa los buses Pub/Sub de la plataforma entre medios y control, y entre control y distribución. |
| msgpack | Formato binario de serialización utilizado en los buses ZeroMQ para transportar los sobres versionados y sus eventos. |
| JSONL | JSON Lines. Formato de persistencia de sólo adición utilizado para conservar hechos por corrida, incluidos eventos, alertas, métricas y errores, y habilitar su relectura y trazabilidad. |
| NVDEC | Decodificador de video por hardware disponible en el entorno de referencia. Se consideró como alternativa de decodificación, pero las corridas reportadas utilizaron decodificación por software. |
| TensorRT | Herramienta de optimización de inferencia considerada en el análisis de alternativas. No fue el runtime utilizado para obtener los resultados presentados. |
| Edge Computing | Paradigma de procesamiento cercano a la fuente de datos, orientado a reducir latencia y carga de red. |
| ⟦ECUACIÓN: no extraída — ver el .docx⟧ | Tiempo entre el inicio del episodio anotado y la marca de tiempo del fotograma que confirma la alerta, sobre el reloj de la fuente. |
| ⟦ECUACIÓN: no extraída — ver el .docx⟧ | Tiempo medido desde el bus de alertas hasta la confirmación de publicación MQTT (PUBACK). No incluye captura, inferencia, confirmación del patrón ni respuesta humana. |
| TTFD | Time To First Detection. Tiempo hasta la primera detección de una condición relevante desde su aparición observable. Se computó en las campañas, pero no se informó como resultado comparativo. |
| SDR | Sustained Detection Rate. Proporción de unidades visuales evaluables con evidencia correcta durante el episodio, bajo la cadencia de muestreo declarada. No equivale al estado confirmed del motor. |
| Latencia de inferencia | Tiempo que tarda el modelo en procesar una entrada visual y producir detecciones. |
| Latencia por tramo | Tiempo medido en una etapa específica del flujo, como ingesta, inferencia, postproceso, publicación o evaluación de patrón. |
| Vocabulario activo | Conjunto de consultas (prompts) simultáneamente activas en una corrida. Su composición condiciona el desempeño del detector, por lo que se declara en cada configuración. |
| Estrategia de detección | Forma de formular una condición ante el detector. La estrategia directa (E-DIR) describe la condición completa en un prompt; la indirecta (E-IND) consulta las entidades por separado y reconstruye la condición con reglas de asociación externas al modelo; la híbrida (E-HYB) combina ambas bajo una regla explícita. |
| G2A | Glass-to-Algorithm. Latencia entre el dequeue de la unidad visual y la disponibilidad del resultado de inferencia. No incluye la captura ni el transporte hasta el host, que se informan aparte cuando la fuente aporta una marca de tiempo confiable. |
| Episodio | Unidad de la referencia temporal humana: intervalo anotado durante el cual una condición de riesgo está presente en un clip. Se distingue del ciclo interno de estados del motor; una resolución y una posterior confirmación pueden ocurrir dentro del mismo episodio de referencia. |
| Re-alerta | Nueva confirmación del motor sobre el mismo episodio de referencia humana después de una resolución. Se contabiliza por separado y no se computa como falsa alerta. |
| CR-01 / CR-02 | Condiciones nucleares de evaluación: persona sin casco (CR-01) y persona sin chaleco reflectivo (CR-02). Los patrones que las operacionalizan se identifican como PR-01 y PR-02. |
| Vocabulario canónico | Conjunto de etiquetas de evidencia perceptiva normalizadas por la plataforma. El núcleo utiliza person, helmet y vest; bare_head interviene en ramas comparativas. Una etiqueta expresa lo que el detector localiza y no equivale a una alerta. |
| Evento de percepción | Evidencia normalizada emitida por el plano de medios y consumida por el plano de control. Su contrato versionado es media.detection.v1. |
| Identidad temporal por sujeto | Identificador que permite asociar observaciones de una persona a lo largo de una secuencia y mantener su estado. No identifica civil ni biométricamente a la persona. |
| Granularidad | Por escena (scene): estado común para una condición en una fuente. Por sujeto (subject): estado independiente por persona con identidad temporal válida. |
| Distribución de alertas | Módulo que consume alertas confirmadas, aplica la política de entrega y registra los resultados del canal externo, separado de la decisión del patrón. |
| FAR | False Alarm Rate. Tasa de falsas alertas por tiempo observado. Se informa con el conteo y la duración que la originan; una tasa derivada no establece una cota operativa. |

## 12. Introducción

### 12.1. Motivación y contexto del proyecto

La seguridad laboral en la industria de la construcción civil constituye un problema de alta relevancia técnica, social y organizacional. Se trata de un sector caracterizado por entornos dinámicos, tareas simultáneas, circulación de personas y maquinaria, estructuras temporales, cambios frecuentes en la disposición del espacio de trabajo y exposición permanente a condiciones de riesgo. En este contexto, la supervisión visual cumple un papel preventivo relevante, pero también presenta limitaciones cuando depende exclusivamente de la observación humana continua sobre múltiples cámaras o frentes de obra.

El presente Proyecto Integrador aborda esta necesidad mediante el estudio, diseño, implementación y evaluación de una plataforma experimental de detección open-vocabulary en video en tiempo real. La motivación central no consiste en reemplazar al supervisor humano ni en automatizar decisiones de cumplimiento normativo, sino en investigar bajo qué condiciones la detección guiada por lenguaje natural, integrada con procesamiento temporal y generación de alertas, puede aportar evidencia visual trazable para el monitoreo asistivo de riesgos en construcción. De esta forma, el proyecto se ubica en la intersección entre inteligencia artificial, visión por computadora, procesamiento de video en tiempo real, seguridad laboral y diseño responsable de sistemas asistivos.

La elección del tema se fundamenta en una brecha concreta. Los detectores de vocabulario cerrado reconocen un conjunto de categorías definido durante su entrenamiento, mientras que el monitoreo de riesgos requiere representar condiciones que pueden combinar entidades, atributos, relaciones espaciales y persistencia temporal. Por ejemplo, «persona sin casco» no equivale a localizar una persona y un casco de manera independiente, sino que exige establecer su asociación y determinar el estado observable. La apertura del vocabulario ofrece una alternativa para formular consultas, pero no resuelve por sí sola esa transformación de detecciones en condiciones evaluables.

Frente a esta limitación, los enfoques de detección de vocabulario abierto permiten formular consultas mediante lenguaje natural. Esta capacidad habilita un modo de especificación más flexible: el usuario puede definir las entidades de interés sin depender de un conjunto rígido de etiquetas preestablecidas, aunque una consulta lingüísticamente válida no garantiza por sí sola una detección correcta. Sobre esa base, el proyecto evalúa la factibilidad técnica de una plataforma que procese video, interprete consultas open-vocabulary, detecte entidades y condiciones observables, aplique criterios de persistencia temporal y genere alertas asistivas trazables.

### 12.2. Problema identificado

El problema que orienta el trabajo puede expresarse como una discontinuidad entre la naturaleza dinámica y semánticamente abierta de los riesgos en obra y el vocabulario fijo de los sistemas de detección visual closed-set. Mientras que el entorno de construcción introduce situaciones variables, dependientes del contexto y difíciles de reducir a categorías fijas, muchos sistemas de visión computacional requieren que las clases detectables hayan sido definidas, anotadas y entrenadas previamente. De ahí la pregunta que orienta el desarrollo, ¿Cómo transformar condiciones de riesgo expresadas en lenguaje natural en alertas trazables sobre un flujo de video, y con qué desempeño y limitaciones puede sostenerse esa transformación?

Esta problemática tiene consecuencias prácticas. En primer lugar, una condición no contemplada por un detector de vocabulario cerrado queda fuera de su capacidad de detección aunque sea relevante para la seguridad, e incorporarla exige recolectar datos, anotar y adaptar el modelo, con un costo en tiempo y recursos. En segundo lugar, en un enfoque open-vocabulary, incorporar o reformular una consulta no elimina la necesidad de validar sus detecciones ni las asociaciones que sustentan la condición de riesgo. En tercer lugar, la detección por fotograma aislado no representa por sí sola situaciones que dependen de duración o reiteración; el análisis de video requiere mecanismos de persistencia temporal y criterios explícitos para distinguir evidencia aislada de episodios que justifican una alerta.

A esta problemática técnica se suma una dimensión operativa. La supervisión de múltiples cámaras o zonas de trabajo motiva la búsqueda de herramientas de apoyo a la observación humana. En este proyecto, ese propósito se acota a producir señales asistivas, trazables y no vinculantes. No se evalúa la reducción de la carga cognitiva del supervisor ni el efecto del sistema sobre la incidencia de accidentes; por lo tanto, esos beneficios potenciales no constituyen resultados del trabajo.

El proyecto no parte de la premisa de que la inteligencia artificial pueda resolver por sí sola la seguridad en obra. Por el contrario, reconoce que una alerta visual no equivale a una determinación jurídica ni técnica de incumplimiento. La función del sistema propuesto es detectar indicios observables, registrar evidencia, activar patrones previamente definidos y asistir a la supervisión humana. Esta delimitación resulta central para sostener el carácter experimental del trabajo y evitar una interpretación excesiva de las capacidades del prototipo.

### 12.3. Enfoque propuesto e hipótesis de trabajo

La hipótesis de trabajo sostiene que los modelos de detección open-vocabulary, al permitir expresar condiciones de interés mediante lenguaje natural en tiempo de inferencia y sin ajustar los pesos del modelo, constituyen un habilitador tecnológico viable para superar parte de la rigidez de los sistemas closed-set en el monitoreo visual de seguridad en construcción. Bajo esta hipótesis, una plataforma experimental podría recibir consultas o patrones como "persona sin casco" o "persona sin chaleco reflectivo" y transformarlos en alertas evaluables dentro de un flujo de video. La hipótesis no presupone que un detector open-vocabulary supere a un detector supervisado ni que la plataforma resulte apta para cualquier escenario de obra.

Sin embargo, esta hipótesis se formula de manera condicionada. La viabilidad no depende únicamente de detectar objetos en imágenes estáticas, sino de integrar la selección de modelos visión-lenguaje, la formulación de consultas, la asociación de evidencia, la estabilidad temporal, los datos de evaluación, el rendimiento en el hardware disponible, la arquitectura de transporte de video, el presupuesto de latencia, la trazabilidad de eventos y las salvaguardas de privacidad en el tratamiento de video en contextos laborales.

Por este motivo, el proyecto se estructura como una plataforma experimental y no como un producto industrial terminado. El objetivo es construir un prototipo que permita evaluar el comportamiento del enfoque bajo condiciones controladas y reproducibles. La solución se organiza alrededor de una cadena operativa mínima, donde intervienen la ingesta o lectura de video, inferencia open-vocabulary, seguimiento temporal, evaluación de patrones de riesgo, registro de alertas y su distribución. Esta cadena permite analizar no sólo la precisión de detección, sino también la oportunidad y la estabilidad de las alertas generadas, en tres niveles de evidencia: la percepción por imagen, el estado por persona y la alerta por episodio.

La propuesta incluye una rama comparativa de ajuste fino al dominio, separada del núcleo sin ajuste de pesos y condicionada a la disponibilidad de datos y a la integridad del protocolo de comparación. Esta rama contrasta variantes adaptadas con una línea base sobre un banco común y considera tanto la ganancia en el dominio como la retención de capacidad open-vocabulary, mediante criterios de adopción definidos antes de la evaluación. La adaptación no se presupone beneficiosa ni se establece como requisito para construir la plataforma, ya que su valor se determina a partir de la evidencia experimental.

### 12.4. Alcance, límites y condiciones de trabajo

El alcance del trabajo comprende el estudio, diseño, implementación y evaluación de una plataforma experimental de detección open-vocabulary en video en tiempo real aplicada al monitoreo asistivo de riesgos en construcción civil. El núcleo evaluativo está constituido por CR-01, persona sin casco, y CR-02, persona sin chaleco reflectivo. Las condiciones relativas a zonas, interacciones con maquinaria y otras relaciones complejas se conservan en el marco conceptual y en el catálogo de extensiones, pero no se presentan como capacidades evaluadas del núcleo.

No se busca construir un sistema de fiscalización automática ni una herramienta de certificación normativa. Las alertas generadas por el prototipo se interpretan como señales asistivas destinadas a apoyar la supervisión humana. En consecuencia, el sistema no sustituye la evaluación técnica en terreno, no define responsabilidades legales, no toma decisiones operativas autónomas y no activa medidas físicas de control. Su valor se analiza como instrumento de apoyo, trazabilidad y experimentación académica. El trabajo tampoco evalúa el efecto del sistema sobre la carga cognitiva del supervisor ni sobre la incidencia de accidentes, principalmente porque esos beneficios potenciales no forman parte de sus resultados.

El prototipo no realiza reconocimiento de identidad personal ni asocia individuos a nombres, credenciales o perfiles. La identidad temporal por sujeto mantiene estados independientes por persona durante una secuencia, sin identificación biométrica. La plataforma incluye además la distribución de alertas confirmadas hacia un canal externo mediante MQTT. Permanecen fuera de alcance la integración completa con sistemas externos de gestión de seguridad, los canales adicionales de notificación y la activación de infraestructura física de alarmas.

La evaluación distingue dos escenarios complementarios: el Escenario A o DBE, evaluación diferida y reproducible sobre archivos, y el Escenario B o EBE, evaluación en vivo con captura continua e intercambio de eventos entre componentes. El material de video comprende un rodaje controlado y material de obra real, cuyos resultados se interpretan por separado. La procedencia, la referencia humana y las condiciones de observabilidad de los datos delimitan qué conclusiones pueden sostenerse en cada escenario.

El trabajo utiliza modelos preentrenados y herramientas disponibles; el entrenamiento desde cero queda fuera de alcance. La selección de modelos, las consultas, la asociación temporal y los mecanismos de ingesta e inferencia se fundamentan en viabilidad técnica, reproducibilidad, licenciamiento y compatibilidad con el hardware disponible. La factibilidad se juzga mediante la plataforma construida y la evidencia obtenida bajo un protocolo explícito, no por su equivalencia con una solución industrial completa.

### 12.5. Enfoque metodológico general

El desarrollo del proyecto adopta un enfoque progresivo e iterativo. En primer lugar, se construye una fundamentación teórica orientada a delimitar el problema, revisar el estado del arte y establecer criterios conceptuales. Esta instancia permite responder qué debe detectar el sistema, cómo pueden interpretarse consultas de lenguaje natural, qué restricciones impone el video en tiempo real, qué papel cumple el seguimiento temporal y bajo qué condiciones ético-legales puede analizarse video en contextos laborales.

En segundo lugar, la fundamentación se traduce en una consolidación metodológica que define condiciones de riesgo, patrones, escenarios de evaluación, infraestructura disponible, estrategia de datos, protocolo de prompts, métricas y presupuesto de latencia. Esta etapa cumple una función de puente entre el análisis conceptual y la implementación, ya que transforma criterios generales en decisiones operativas evaluables.

El diseño arquitectónico define los módulos, los flujos de datos, los contratos de interfaz y la separación entre el plano de medios, el plano de control y la distribución de alertas. La implementación materializa esas decisiones en un prototipo reproducible e incorpora el soporte experimental y los bancos de evaluación. La evaluación experimental mide percepción, estado por persona, alertas por episodio y rendimiento de ejecución. El análisis de esos resultados delimita el alcance de la factibilidad, sus limitaciones y las líneas de continuidad.

La metodología se orienta a la trazabilidad. Cada decisión técnica relevante se vincula con una necesidad del problema, un fundamento conceptual, una restricción metodológica o una condición experimental. El cuerpo del informe desarrolla la argumentación, las decisiones y los resultados necesarios para sostener las conclusiones. Los anexos reúnen información técnica complementaria y condiciones de reproducibilidad, mientras que los artefactos experimentales conservan configuraciones, registros y evidencia por corrida para permitir su inspección.

## 13. Objetivos del proyecto

### 13.1. Objetivo general

Diseñar, implementar y evaluar la factibilidad técnica de una plataforma experimental de detección open-vocabulary en video en tiempo real, orientada a la identificación asistiva de condiciones de riesgo en obras de construcción civil, mediante la integración de modelos de visión-lenguaje, procesamiento de video de baja latencia, seguimiento temporal, patrones de riesgo y mecanismos de alerta evaluables bajo condiciones controladas.

### 13.2. Objetivos específicos

- Analizar el estado del arte y los fundamentos técnicos, metodológicos, normativos y ético-legales vinculados con la detección open-vocabulary, el seguimiento multiobjeto, la transmisión de video en tiempo real y la seguridad laboral en construcción civil, a fin de establecer criterios de diseño y evaluación para la plataforma experimental.

- Definir y operacionalizar un conjunto de condiciones de riesgo visualmente observables en entornos de obra, vinculándolas con patrones de riesgo, niveles de severidad, criterios de persistencia temporal y formulaciones de consulta compatibles con modelos de detección open-vocabulary.

- Diseñar una arquitectura modular de procesamiento de video en tiempo real que distinga el plano de medios y el plano de control, permitiendo integrar de manera desacoplada componentes de ingesta, inferencia, seguimiento temporal, evaluación de patrones, registro de eventos, generación de alertas y su distribución hacia canales externos.

- Implementar un prototipo experimental capaz de ejecutar el flujo experimental previsto, incorporando ingesta o lectura de video, inferencia open-vocabulary, evaluación de patrones de riesgo, registro de eventos, alertas internas y su distribución, e instrumentación de métricas técnicas y operativas.

- Evaluar el desempeño del prototipo mediante un protocolo experimental reproducible, considerando escenarios basados en datasets y escenarios controlados representativos, con métricas de detección, seguimiento, rendimiento del pipeline, latencia de alerta y utilidad operativa de las notificaciones generadas.

- Incorporar lineamientos de ética, privacidad y seguridad de la información acordes con el uso responsable de sistemas de análisis automatizado de video en contextos laborales, manteniendo el carácter asistivo de las alertas y evitando mecanismos de reconocimiento de identidad personal.

- Documentar las decisiones técnicas, metodológicas y experimentales adoptadas durante el desarrollo del proyecto, junto con sus resultados, limitaciones, evidencias generadas y posibles líneas de continuidad o mejora futura.

## 14. Plan De Trabajo De Proyecto Integrador

### 14.1. Enfoque general de trabajo

Se adopta un proceso iterativo-incremental, de inspiración ágil, orientado a construir progresivamente la plataforma experimental y la evidencia académica asociada. El avance se organiza en ciclos de planificación, ejecución, verificación y ajuste, priorizando las tareas según su aporte directo a los objetivos del proyecto. Esta metodología permite incorporar hallazgos de investigación, restricciones técnicas emergentes y resultados preliminares sin alterar el propósito general del trabajo.

La documentación acompaña cada etapa del proceso. Las decisiones técnicas, configuraciones, supuestos, limitaciones, pruebas y resultados parciales se registran a medida que se producen, favoreciendo la reproducibilidad del prototipo y la trazabilidad de las decisiones adoptadas. Esta forma de trabajo permite distinguir qué decisiones derivan del análisis teórico, cuáles responden a restricciones metodológicas y cuáles surgen de la implementación concreta del sistema.

### 14.2. Etapas del proyecto

#### 14.2.1. Etapa 1 - Investigación bibliográfica y fundamentación teórica

**Duración estimada:** 4–5 semanas 	**Propósito:** construir un marco teórico, técnico, ético y normativo que sustente el proyecto, comprendiendo en profundidad las tecnologías involucradas sin tomar decisiones de diseño ni selección definitiva.

**Actividades:**

- Revisión sistemática de literatura y documentación técnica sobre:

  - Modelos *open-vocabulary detection (OVD)*

  - Técnicas de *multi-object tracking (MOT)*

  - Protocolos y arquitecturas de transmisión de medios en baja latencia

  - Enfoques ético-legales y de privacidad en visión por computadora

  - Normativa de seguridad laboral en la construcción

- Elaboración de fichas de lectura, matrices comparativas y síntesis crítica.

- Integración de los resultados en un informe académico estructurado.

**Resultado esperado:**

- Informe “*Fundamentación teórica y estado del arte*”.

- Criterios conceptuales para orientar las decisiones metodológicas de la Etapa 2.

#### 14.2.2. Etapa 2 - Análisis metodológico y estrategia de evaluación

**Duración estimada:** 5–6 semanas 	**Propósito:** definir los criterios experimentales, métricas, datasets y condiciones de prueba que permitirán evaluar la factibilidad del sistema en laboratorio y entorno simulado.

**Actividades:**

- Determinar supuestos y restricciones técnicas (hardware, cámaras, entornos controlados).

- Definir métricas de evaluación: precisión, recall, F1-score, FPS, latencia.

- Explorar, seleccionar y documentar datasets de referencia y del dominio construcción.

- Diseñar un protocolo de evaluación reproducible y escalable a futuro.

- Elaborar matriz de riesgos técnicos y operativos con mitigaciones básicas.

**Resultado esperado:**

- Documento “*Plan metodológico y protocolo de evaluación*”.

- Inventario de datasets validados y criterios de evaluación.

- Matriz de riesgos y supuestos experimentales.

#### 14.2.3. Etapa 3 - Diseño arquitectónico de la plataforma experimental

**Duración estimada:** 7–9 semanas 	**Propósito:** definir una **arquitectura conceptual y modular**, lo suficientemente clara para implementar un prototipo funcional, sin buscar una ingeniería de producto completa.

**Actividades:**

- Diseño del **plano de medios** (captura, normalización, transporte de video).

- Diseño del **plano de control** (detección, eventos, alertas, almacenamiento).

- Definición de módulos principales.

- Elaboración de diagramas de arquitectura y flujo de datos.

- Definición preliminar de APIs internas y contratos de comunicación.

- Planificación del backlog de desarrollo incremental (sprints o hitos).

- Redacción del documento técnico de arquitectura.

**Resultado esperado:**

- Documento “*Diseño de arquitectura modular*”.

- Diagramas de flujo, componentes y contratos de interfaz.

- Backlog inicial priorizado para la implementación.

#### 14.2.4. Etapa 4 - Implementación del prototipo experimental

**Duración estimada:** 10–12 semanas 	**Propósito:** construir el prototipo experimental que materializa la arquitectura definida, integrando los módulos esenciales en un flujo funcional de extremo a extremo.

**Actividades:**

- Implementar el módulo de ingesta y transmisión de video de baja latencia, conforme al diseño del plano de medios.

- Integrar un modelo OV pre entrenado capaz de procesar secuencias de video en tiempo real.

- Incorporar, en la medida en que resulte viable, componentes complementarios como**:**

  - Módulo de seguimiento temporal (MOT),

  - Lógica básica de patrones de riesgo,

  - Sistema simplificado de alertas o registro de eventos,

  - Interfaz de prueba (API o panel web básico).

- Documentar de manera continua las configuraciones, dependencias, decisiones técnicas y limitaciones observadas durante la implementación.

- Realizar una **validación técnica preliminar** del flujo mínimo en entorno controlado, midiendo latencia, FPS y estabilidad general.

**Resultado esperado:**

- Prototipo funcional reproducible con documentación técnica.

- Video o demo funcional end-to-end.

- Log de pruebas iniciales (latencia, FPS).

- Registro de decisiones técnicas y limitaciones.

#### 14.2.5. Etapa 5 - Evaluación y validación de desempeño

**Duración estimada:** 	4–5 semanas 	**Propósito:** medir cuantitativa y cualitativamente el desempeño del prototipo en laboratorio y en entorno simulado de obra civil.

**Actividades:**

- Ejecución de pruebas en dataset controlado (laboratorio).

- Ejecución en escenario representativo de obra simulada.

- Registro de métricas: precisión, recall, F1, FPS, latencia.

- Evaluación de robustez frente a condiciones reales (iluminación, oclusión, movimiento).

- Análisis comparativo con resultados del estado del arte.

- Elaborar el informe de resultados y análisis crítico.

**Resultado esperado:**

- Informe “*Evaluación de desempeño y validación experimental*”.

- Tablas de métricas y gráficos analíticos.

- Discusión de fortalezas, debilidades y limitaciones del sistema.

#### 14.2.6. Etapa 6 - Documentación final, revisión y presentación

**Duración estimada:** 5–6 semanas 	**Propósito:** consolidar los resultados técnicos y académicos del proyecto, garantizando una entrega completa, reproducible y lista para defensa.

**Actividades:**

- Redactar el Informe Final estructurado.

- Incorporar anexos técnicos (APIs, diagramas, logs, parámetros).

- Compilar manual de despliegue y documentación del repositorio.

- Preparar presentación oral y material multimedia (slides, video demo).

- Validar y etiquetar el repositorio final (versión definitiva).

**Resultado esperado:**

- Entrega académica completa: informe PDF, anexos, repositorio y presentación.

- Defensa lista ante tribunal con documentación de respaldo.

### 14.3. Cronograma y esquema gráfico

El cronograma del proyecto se organiza en torno a las seis etapas descritas. La secuencia general mantiene una progresión desde la investigación y fundamentación inicial hasta la validación experimental y el cierre documental. El esquema gráfico permite distinguir la duración estimada de cada etapa, su relación temporal con las demás y el estado de avance correspondiente.

**Figura 1**

*Diagrama de Gantt de las etapas previstas del proyecto.*

⟦FIGURA: no extraída — ver el .docx⟧

### 14.4. Costos asociados al proyecto

El proyecto se autofinancia con recursos de los integrantes y no requiere desembolsos significativos. Esa característica no es casual sino una consecuencia de tres decisiones de diseño. La plataforma se despliega en forma local sobre equipamiento propio, el cómputo intensivo de ajuste fino se deriva a un clúster institucional y toda la cadena de software se construye con componentes de código abierto y conjuntos de datos publicados bajo licencias abiertas.

Los gastos previstos para la realización del trabajo, agrupados según las categorías más relevantes, son los siguientes.

**Movilidad.** Un único traslado del equipo a las instalaciones de la empresa Steel Brox S.R.L., en la ciudad de Córdoba, para la jornada de captura de video con escenas guionadas. Las reuniones de tutoría no generan traslados adicionales.

**Alquiler de servidores o VPS.** No se contrata. Los tres servicios de la plataforma corren en un mismo equipo local y el entrenamiento de modelos se ejecuta en el clúster Mendieta del Centro de Computación de Alto Desempeño de la Universidad Nacional de Córdoba, cuyo acceso es institucional y sin cargo.

**Licencias de software.** Sin costo. El conjunto de herramientas de desarrollo, inferencia y despliegue es íntegramente de código abierto, y los conjuntos de datos se usan bajo licencias abiertas con atribución.

**Suscripciones.** No se contratan servicios pagos. El control de versiones y el resguardo de la evidencia experimental usan los planes gratuitos de GitHub y Google Drive.

**Consumibles del trabajo de campo.** Sin costo. El casco y el chaleco reflectivo empleados como utilería son prestados por la misma empresa que facilita el espacio de grabación, y la cámara de borde es prestada por el tutor.

La evaluación económica completa del proyecto, que valoriza además las horas de trabajo, el equipamiento aportado y el cómputo institucional, se desarrolla en la sección 17.2.

## 15. Estado del arte

Esta sección reúne los antecedentes técnicos y metodológicos necesarios para contextualizar el desarrollo de una plataforma experimental de detección *open-vocabulary* en video en tiempo real. Su propósito es revisar los enfoques, modelos y arquitecturas que permiten comprender el alcance actual de la detección visual guiada por lenguaje natural, así como sus limitaciones cuando se la traslada a escenarios dinámicos, con restricciones temporales y requerimientos de seguridad laboral.

### 15.1. Alcance del estado del arte y propósito de la fundamentación teórica

El análisis se organiza en torno a los dominios que condicionan la viabilidad del sistema: la detección open-vocabulary como alternativa frente a los enfoques de vocabulario cerrado, los modelos visión-lenguaje y sus principales familias arquitectónicas, el seguimiento multiobjeto como mecanismo de persistencia temporal, y las tecnologías de transmisión y procesamiento de video necesarias para operar con baja latencia. De manera complementaria, se consideran las brechas que aparecen al aplicar estas tecnologías al dominio de la construcción civil, especialmente en relación con la detección de condiciones de riesgo, la estabilidad temporal de las predicciones, la sensibilidad a los *prompts*, la disponibilidad de datos y la evaluación de alertas en tiempo real.

Esta revisión no tiene por finalidad elegir de forma aislada un modelo, protocolo o herramienta, sino establecer un marco crítico para distinguir qué capacidades se encuentran suficientemente maduras, qué aspectos requieren validación experimental y qué limitaciones deben ser consideradas durante el diseño e implementación del prototipo. A partir de esta base se derivan criterios para la selección tecnológica, la definición del alcance experimental y la construcción posterior del protocolo de evaluación.

### 15.2. Detección open-vocabulary: modelos, paradigmas y brechas del estado del arte

#### 15.2.1. Paradigmas arquitectónicos y modelos representativos

El estado del arte en OVD no constituye una solución homogénea, sino que se organiza en familias arquitectónicas con compromisos claramente diferenciados entre expresividad semántica, complejidad computacional y eficiencia temporal. A partir de un relevamiento exhaustivo realizado durante la investigación bibliográfica, se identificaron cuatro paradigmas dominantes, de los cuales se presentan a continuación los aspectos y modelos representativos más relevantes para el contexto de sistemas de video en tiempo real.

El primer paradigma extiende arquitecturas *end-to-end* basadas en Transformers —derivadas de DETR y DINO (Carion et al., 2020; H. Zhang et al., 2022)— e incorpora el lenguaje dentro de la predicción mediante fusión multimodal. Grounding DINO (Liu et al., 2024) organiza esa integración en un *Feature Enhancer* que alinea representaciones visuales y textuales, una selección de consultas guiada por lenguaje y un *decoder* de modalidad cruzada que refina cajas y las vincula con fragmentos del prompt. La fusión profunda favorece expresiones referenciales y consultas con atributos, aunque incrementa el costo computacional y la complejidad de despliegue.

El segundo paradigma adapta detectores *one-stage* de la familia YOLO para puntuar regiones frente a representaciones textuales. YOLO-World (Cheng et al., 2024) incorpora interacción visión-lenguaje en su *neck* y permite reutilizar un vocabulario precomputado; YOLOE (A. Wang et al., 2025) amplía la reparametrización para admitir prompts textuales, visuales y un modo sin prompt. Esta familia prioriza eficiencia y compatibilidad con *pipelines* de baja latencia, a cambio de una expresividad más acotada ante consultas relacionales o altamente composicionales.

Una tercera familia deriva la detección del paradigma *dual-encoder* de CLIP: imagen y texto se proyectan en un espacio compartido y la clase de cada región se obtiene por compatibilidad semántica, no mediante *logits* fijos. OWL-ViT y OWLv2 (Minderer et al., 2022, 2023) representan este enfoque y muestran cómo el autoentrenamiento puede escalar la supervisión sin alterar el mecanismo de consulta. Su principal ventaja es la modularidad, donde el vocabulario cambia con los prompts. Su costo depende del número de consultas y puede mitigarse mediante el cacheo de *embeddings* cuando el vocabulario permanece estable.

El cuarto paradigma agrupa modelos guiados por prompts generalistas, generativos e híbridos. Florence-2 (Xiao et al., 2024) formula las tareas como traducción secuencia-a-secuencia y genera representaciones textuales de cajas, etiquetas u otras salidas estructuradas. APE, LLMDet y T-Rex2 adoptan *prompting* generalista sin compartir necesariamente una decodificación autorregresiva (Shen et al., 2023; Fu et al., 2025; Jiang et al., 2024). Esta flexibilidad amplía la variedad de tareas y modalidades de consulta, pero en los modelos generativos introduce latencia variable y menor paralelismo que la predicción directa.

A continuación, se revisan modelos representativos de cada paradigma, enfocando el análisis en: (i) decisiones arquitectónicas, (ii) mecanismo de fusión/compatibilidad visión–lenguaje, (iii) régimen de entrenamiento y tipo de supervisión, y (iv) resultados en *benchmarks* estándar (COCO, LVIS), junto con consideraciones prácticas de inferencia relevantes para aplicaciones en video.

##### 15.2.1.1. Detectores end-to-end derivados de DETR/DINO con fusión multimodal profunda

En los detectores derivados de DETR y DINO, el texto participa del propio proceso de predicción en lugar de aplicarse como clasificación posterior sobre regiones ya obtenidas. Grounding DINO extiende el *phrase grounding* de GLIP mediante un esquema dual-encoder/single-decoder, donde un *backbone* visual extrae características multiescala, un *encoder* BERT representa el prompt y un Transformer produce cajas condicionadas por ambas modalidades (L. H. Li et al., 2021; Liu et al., 2024). La alineación se distribuye entre el Feature Enhancer, que relaciona características visuales y textuales, la *Language-guided Query Selection*, que prioriza consultas relevantes y el *Cross-modality Decoder*, que refina las cajas y su asociación con fragmentos del prompt. Esta fusión profunda favorece expresiones referenciales y atributos compuestos, pero incrementa el costo de inferencia y la complejidad de despliegue (Liu et al., 2024).

Las cifras publicadas deben leerse junto con el backbone, el protocolo y los datos de entrenamiento. Grounding DINO con Swin-L reporta 52,5 AP en COCO y 26,1 mean AP en ODinW bajo evaluación *zero-shot*, mientras que Swin-T alcanza aproximadamente 48,4 AP en COCO (Liu et al., 2024). La variante Swin-B dispone de pesos públicos, pero su *checkpoint* incluye COCO entre los datos de entrenamiento; por ello, el 56,7 AP informado para esa configuración no constituye una referencia zero-shot directamente comparable. MM-Grounding-DINO conserva esta línea arquitectónica en una tubería unificada y, en sus variantes Tiny, reporta entre 50,4 y 50,6 AP@[0,50:0,95] en COCO zero-shot y entre 35,7 y 41,4 AP@[0,50:0,95] en LVIS-minival, según la configuración evaluada (IDEA-Research, 2024c; X. Zhao et al., 2024).

Las extensiones recientes exploran generalización y eficiencia como objetivos diferenciados. Grounding DINO 1.5 Pro, preentrenado con Grounding-20M, reporta 54,3 AP en COCO y 55,7 AP en LVIS-minival en zero-shot transfer; la variante *Edge* alcanza 75,2 FPS con 36,2 AP en LVIS-minival mediante TensorRT y supera 10 FPS en NVIDIA Orin NX (Ren, Jiang, et al., 2024). DINO-X amplía las modalidades de consulta con prompts textuales, visuales y personalizados, además de un *Universal Object Prompt* para operar sin una lista explícita de clases. Preentrenado sobre Grounding-100M, DINO-X Pro reporta 56,0 AP en COCO, 59,8 AP en LVIS-minival y 63,3 AP en las clases raras de LVIS-minival (Ren, Chen, et al., 2024). La familia ofrece alta precisión semántica y manejo de expresiones referenciales complejas, a costa de mayor exigencia computacional y, en las variantes cerradas, menor reproducibilidad independiente. El repositorio del Grounding DINO original se distribuye bajo Apache-2.0, mientras que Grounding DINO 1.5 y DINO-X se ofrecen mediante API sin pesos abiertos. La licencia Apache-2.0 corresponde a sus SDK de acceso (IDEA-Research, 2024a, 2024c; Ren, Chen, et al., 2024; Ren, Jiang, et al., 2024).

##### 15.2.1.2. Detectores one-stage de la familia YOLO con alineamiento región-texto

La familia one-stage traslada la capacidad open-vocabulary a una estructura orientada a predicción densa y baja latencia. En lugar de sostener un decoder multimodal profundo, realiza el alineamiento región-texto dentro del flujo backbone-PAN-head y procura absorber parte de ese costo mediante reparametrización. YOLO-World introduce RepVL-PAN, con *Text-guided CSPLayer* para incorporar guía textual en las características visuales e *Image Pooling Attention* para enriquecer los embeddings del vocabulario. Cuando este permanece estable, puede precomputarse y utilizarse *offline*, prescindiendo del encoder textual durante la inferencia reparametrizada (Cheng et al., 2024). YOLOE amplía la estrategia con RepRTA para prompts textuales, SAVPE para prompts visuales y LRPC para un modo sin prompt explícito. Tras la reparametrización, su grafo de inferencia conserva una estructura equivalente a la de un YOLO de vocabulario cerrado (A. Wang et al., 2025).

Los puntos de operación publicados reflejan esa prioridad temporal. YOLO-World-L reporta 35,4 AP en LVIS-minival con 52,0 FPS sobre una NVIDIA V100 sin TensorRT. En LVIS-minival zero-shot, YOLOE-v8-S alcanza 27,9 AP con 305,8 FPS y YOLOE-v8-L 35,9 AP con 102,5 FPS sobre una NVIDIA T4 mediante TensorRT (Cheng et al., 2024; A. Wang et al., 2025). Estas cifras provienen de hardware y *runtimes* distintos y no constituyen un benchmark homogéneo. También debe distinguirse la versión evaluada, donde el trabajo original informa variantes YOLOE-v8 y YOLOE-11, mientras que YOLOE-26 es una extensión posterior de Ultralytics. Los resultados de las variantes v8 no deben presentarse como mediciones de YOLOE-26 (A. Wang et al., 2025; Ultralytics, 2026).

YOLO-World se distribuye bajo GPL-3.0 y YOLOE bajo AGPL-3.0, licencias que pueden imponer obligaciones copyleft en integraciones posteriores (AILab-CVC, 2024; THU-MIG, 2025). La fortaleza de este paradigma es la velocidad y su compatibilidad con hardware de borde, y su limitación es una expresividad relativamente menor frente a consultas relacionales o con atributos altamente compuestos, no la ausencia de apertura semántica.

##### 15.2.1.3. Detectores dual-encoder CLIP-like con correspondencia por similitud

Los enfoques derivados de CLIP separan con mayor claridad la representación visual de la textual. OWL-ViT utiliza un Vision Transformer *encoder-only* que conserva *tokens* espaciales y agrega cabezales livianos para predecir, por token, una caja y un embedding de compatibilidad. La categoría de cada región se obtiene por similitud con embeddings derivados de las consultas, en lugar de surgir de un clasificador con logits fijos, lo que permite que el vocabulario pueda modificarse sin alterar los parámetros ni los cabezales del detector (Minderer et al., 2022). OWLv2 mantiene ese mecanismo y escala la supervisión mediante OWL-ST, que utiliza un modelo OWL-ViT para generar pseudo-cajas sobre WebLI. El entrenamiento incorpora un *objectness head* para concentrar las pérdidas en tokens plausibles como objetos y *token dropping* para reducir el costo de optimización (Minderer et al., 2023).

En LVIS, OWL-ViT L/14 reporta 34,6 AP y 31,2 AP en clases raras; OWLv2 L/14 con OWL-ST alcanza 44,6 AP zero-shot en clases raras de LVIS-val, y la variante G/14 llega a 47,2 AP. Los pesos de ambas generaciones se distribuyen bajo Apache-2.0 (Google, 2022, 2023; Minderer et al., 2022, 2023).

La principal fortaleza de la familia es la modularidad. Esto permite que el vocabulario se amplíe o sustituya mediante nuevas consultas. Su costo depende, sin embargo, de la cantidad de embeddings activos. Cuando el vocabulario permanece estable entre cuadros, el cacheo evita recomputar la representación textual. Aun así, sostener una latencia estable exige controlar el tamaño del conjunto de consultas.

##### 15.2.1.4. Modelos guiados por prompts generalistas: formulaciones generativas e híbridas

Esta familia se define por ampliar la forma de especificar la tarea y el tipo de salida, no por una única topología de detector. Florence-2 constituye el caso propiamente generativo, donde interpreta una instrucción y produce secuencias de texto o tokens de localización. APE utiliza prompting generalista, pero genera predicciones estructuradas de manera directa. LLMDet incorpora conocimiento de un modelo de lenguaje durante el entrenamiento y prescinde de ese componente en inferencia. T-Rex2, en cambio, combina prompts textuales y visuales dentro de una formulación multimodal (Shen et al., 2023; Fu et al., 2025; Jiang et al., 2024; Xiao et al., 2024). El rasgo común es la flexibilidad de interacción, por lo que no corresponde atribuir decodificación autorregresiva ni una misma restricción temporal a toda la familia.

Florence-2 materializa esa unificación con un encoder visual DaViT y un Transformer *encoder-decoder* multimodal que genera etiquetas, cajas y otras salidas estructuradas sin cabezales específicos por tarea. Fue preentrenado sobre FLD-5B, compuesto por 126 millones de imágenes y 5,4 mil millones de anotaciones, y su variante large reporta 37,5 mAP en detección zero-shot sobre COCO. Los pesos se publican bajo licencia MIT (Microsoft, 2024; Xiao et al., 2024). La decodificación autorregresiva introduce latencia variable y menor paralelismo, mientras que en APE el prompting masivo no equivale a una garantía de tiempo real estricto. LLMDet y T-Rex2 muestran que la flexibilidad lingüística o multimodal también puede integrarse sin mantener un generador autorregresivo en inferencia.

Esta familia aporta flexibilidad multitarea y multimodal, pero su aptitud temporal debe verificarse por modelo y configuración.

#### 15.2.2. Composición de modelos y pipelines de percepción

Los detectores OVD pueden integrarse en pipelines que combinan capacidades complementarias. Grounded SAM ejemplifica esta composición al encadenar detección condicionada por texto con segmentación universal, mientras que OVTrack formaliza una extensión temporal mediante *tracking-by-detection* en vocabulario abierto (Ren, Liu, et al., 2024; S. Li et al., 2023). El aporte conceptual de estos enfoques no es un modelo aislado, sino la posibilidad de desacoplar etapas con responsabilidades distintas.

La modularidad permite sustituir componentes y ampliar capacidades, pero también acumula latencia, dependencias de integración y fuentes de variabilidad. Para sistemas de video en tiempo real, la evaluación debe considerar el pipeline completo y no sólo la precisión de cada modelo por separado; este criterio enlaza la detección con el seguimiento temporal y con las etapas posteriores de generación de eventos.

#### 15.2.3. Síntesis comparativa y trade-offs para tiempo real

La Tabla 2 sintetiza las características fundamentales de los cuatro paradigmas arquitectónicos analizados, con énfasis en las dimensiones más relevantes para la viabilidad del sistema E-OVRT-VDP en un contexto de video en tiempo real.

**Tabla 2**

*Síntesis comparativa de paradigmas arquitectónicos OVD según dimensiones relevantes para sistemas de video en tiempo real*

| **Paradigma** | **Modelo(s) representativos** | **Mecanismo visión-lenguaje** | **Fortaleza principal** | **Limitación para tiempo real** |
| --- | --- | --- | --- | --- |
| DETR/DINO + fusión profunda | Grounding DINO, MM-Grounding-DINO, DINO-X | Fusión multimodal en decoder mediante atención cruzada visión-lenguaje | Alta precisión semántica; manejo de expresiones referenciales complejas | Costo computacional elevado; requiere optimización explícita para tiempo real |
| One-stage YOLO + puntuación región-texto | YOLO-World, YOLOE | Alineamiento región-texto reparametrizable; reducción progresiva del *overhead* de fusión mediante reparametrización | Alta velocidad de inferencia; compatible con hardware de borde | Menor expresividad semántica frente a consultas complejas o con atributos compuestos |
| Dual-encoder CLIP-like + *matching* por similitud | OWL-ViT, OWLv2 | Matching por similitud en espacio de embeddings compartido; reutilización directa de preentrenamiento contrastivo | Modularidad; cambio de vocabulario sin modificar el modelo | latencia variable según tamaño del vocabulario; requiere *caching* para vocabularios estables; requiere cómputo de embeddings por consulta |
| Prompts generalistas: generativo e híbrido | Florence-2, APE, LLMDet, T-Rex2 | Mecanismos heterogéneos: generación autorregresiva en Florence-2; predicción directa o integración híbrida en APE, LLMDet y T-Rex2 | Flexibilidad multitarea; soporte para prompts complejos y multimodales | Florence-2: latencia de inferencia variable e inestabilidad temporal por decodificación autorregresiva; APE: costo de prompting masivo escalable pero sin garantías de tiempo real estricto |

***Nota.*** La columna “Limitación para tiempo real” describe el principal factor restrictivo de cada paradigma en escenarios de monitoreo continuo. Los modelos listados son representativos de cada familia; no constituyen una lista exhaustiva. Las métricas de velocidad son contextuales al hardware y configuración de inferencia reportados en la literatura primaria. Fuente: Elaboración propia basada en las fuentes mencionadas (Cheng et al., 2024; Liu et al., 2024; Minderer et al., 2022, 2023; A. Wang et al., 2025; Xiao et al., 2024).

El régimen de disponibilidad constituye una dimensión independiente del rendimiento. YOLO-World y YOLOE se publican bajo GPL-3.0 y AGPL-3.0, respectivamente, mientras que el Grounding DINO original y OWLv2 utilizan licencias permisivas Apache-2.0; por otra parte, Grounding DINO 1.5 y DINO-X se ofrecen mediante API sin pesos abiertos. Estas diferencias afectan la reproducción independiente, la redistribución de artefactos y la continuidad tecnológica, aun en un prototipo académico. Por ello, la comparación de alternativas debe distinguir entre licencia del código, licencia de los pesos y condiciones del servicio de acceso (AILab-CVC, 2024; Google, 2022, 2023; IDEA-Research, 2024a, 2024c; THU-MIG, 2025).

Como complemento a esta síntesis por paradigmas, en la Tabla A.1 del Anexo A se incluye una matriz ampliada orientada a prototipado, donde se comparan modelos representativos según familia arquitectónica, mecanismo visión-lenguaje, métricas reportadas, rendimiento y licenciamiento.

Del análisis comparativo emergen tres tensiones técnicas que deben considerarse como criterios de selección.

1) La tensión entre precisión semántica y latencia de inferencia. Los modelos con fusión visión-lenguaje más profunda suelen ofrecer mayor capacidad frente a consultas complejas, pero con un costo computacional que puede reducir la tasa de procesamiento.

2) La tensión entre generalización zero-shot y especialización de dominio. Los benchmarks generales no representan por sí mismos las condiciones visuales de una obra civil. Esta tensión se extiende al fine-tuning. La evidencia revisada no permite atribuir la retención open-vocabulary a una familia arquitectónica por sí sola, porque las comparaciones utilizan datos, módulos entrenables y protocolos diferentes. La retención depende de la receta aplicada, lo cual define qué parámetros se ajustan o congelan, si se conserva supervisión lingüística amplia y si se evalúan categorías no vistas (Cheng et al., 2024; Minderer et al., 2023; X. Zhao et al., 2024). Por ello, debe describirse para cada configuración y no inferirse de la profundidad o removibilidad de la fusión.

3) La tensión entre expresividad semántica y simplicidad del prompt. Las consultas más precisas exigen mayor control de formulación, introduciendo una variable de diseño ausente en sistemas closed-set.

Una observación transversal es que, en los modelos que permiten reutilizar la representación textual, el cacheo de embeddings entre cuadros reduce el costo recurrente cuando el vocabulario permanece estable (A. Wang et al., 2025; T. Zhao et al., 2024). Dado que las condiciones de riesgo se definen al inicio de la sesión y se mantienen constantes, esta estrategia resulta directamente aplicable al escenario considerado.

Adicionalmente, la tendencia hacia pipelines composicionales descrita en esta sección introduce una cuarta tensión que opera en un plano distinto a las anteriores, siendo esta la tensión entre modularidad e integrabilidad. Los enfoques que ensamblan múltiples modelos foundation —como la combinación de un detector OVD con un segmentador universal— ofrecen mayor flexibilidad para sustituir componentes y abordar tareas compuestas, pero acumulan latencia de inferencia por la ejecución secuencial de etapas y aumentan la complejidad de integración entre formatos de entrada y salida. Esta tensión no invalida el patrón composicional, pero señala que la evaluación de alternativas en etapas posteriores deberá considerar no solo el rendimiento de cada modelo de forma aislada, sino el costo total del pipeline resultante bajo las restricciones temporales del escenario de aplicación.

##### 15.2.3.1. Análisis de rendimiento para tiempo real

Desde el punto de vista del desempeño temporal, varios de los modelos analizados presentan características compatibles con aplicaciones de análisis de video en tiempo real. La Tabla 3 resume puntos de operación publicados para modelos representativos y calcula, a partir de sus FPS, una latencia teórica por cuadro; estos valores no constituyen mediciones homogéneas de latencia.

**Tabla 3**

*Análisis comparativo de rendimiento de modelos OVD para tiempo real*

| **Modelo** | **Hardware** | ***Framework*** | **FPS** | **Latencia derivada (ms/cuadro)** | **LVIS-minival AP@[0,50:0,95]** |
| --- | --- | --- | --- | --- | --- |
| YOLOE-v8-S | T4 | TensorRT | 305,8 | 3,3 ms | 27,9 |
| YOLOE-v8-L | T4 | TensorRT | 102,5 | 9,8 ms | 35,9 |
| G-DINO 1.5 Edge | A100 | TensorRT | 75,2 | 13,3 ms | 36,2 |
| YOLO-World-L | V100 | PyTorch | 52,0 | 19,2 ms | 35,4 |

***Nota.*** La columna «Latencia derivada» se calculó como 1000/FPS y expresa milisegundos por cuadro inferidos de la tasa publicada; no corresponde a una medición independiente de latencia. Los valores de FPS y AP provienen de trabajos originales con hardware, resolución, *batch size* y runtime no homogéneos. Por ello, la tabla muestra puntos de operación indicativos, no benchmarks normalizados ni latencia extremo a extremo. Fuente: elaboración propia basada en A. Wang et al. (2025), Ren, Jiang, et al. (2024) y Cheng et al. (2024).

Los puntos de operación de la tabla describen rendimiento publicado sobre benchmarks generales y no constituyen una predicción del desempeño sobre condiciones de EPP en construcción. La brecha entre benchmark general y condición de dominio se desarrolla en la sección 15.2.5.4.

#### 15.2.4. Adaptabilidad mediante fine-tuning y preservación de capacidad open-vocabulary

El ajuste de un modelo preentrenado introduce un compromiso entre especialización de dominio y preservación de las representaciones adquiridas. La literatura muestra que actualizar todos los parámetros puede mejorar el desempeño *in-domain* y, al mismo tiempo, deteriorar la generalización fuera de distribución frente a estrategias que congelan la mayor parte del modelo; este fenómeno se vincula con el olvido catastrófico (*catastrophic forgetting*) y exige medir la retención de forma explícita (Kirkpatrick et al., 2017; Kumar et al., 2022). Cuando la evidencia del dominio es limitada, la cantidad y ubicación de los parámetros actualizados también importan. Una solución es el ajuste selectivo de capas, el cual puede preservar mejor información preentrenada que el ajuste completo (Lee et al., 2023).

En Grounding DINO se documentan fine-tuning *closed-set*, preentrenamiento continuado *open-set* y ajuste open-vocabulary. MM-Grounding-DINO, por su parte, muestra que la retención depende de mantener supervisión y evaluación sobre categorías no vistas (X. Zhao et al., 2024). La adaptación con LoRA constituye una variante de actualización acotada en la que se conservan congelados los backbones y se entrenan adaptadores de bajo rango (Rasaee et al., 2025). Como referencia de especialización, Grounding DINO con Swin-L reporta 62,6 AP en COCO val y 63,0 AP en test-dev tras fine-tuning closed-set, frente a 52,5 AP en su evaluación zero-shot; los regímenes no son equivalentes y no deben confundirse (Liu et al., 2024).

Para YOLO-World, la documentación distingue el ajuste con Mixed Grounding *Dataset*, que conserva textos y tareas de grounding, del ajuste closed-set con MultiModal Dataset y vocabulario fijo. La variante reparametrizada elimina RepVL-PAN y el encoder textual, con lo cual prioriza eficiencia a costa de cerrar el vocabulario. El ajuste del encoder textual puede degradar la generalización, mientras que congelarlo o conservar supervisión abierta reduce ese riesgo (AILab-CVC, 2024; Cheng et al., 2024).

YOLOE ofrece linear probing y full tuning para transferencia a un dominio. La receta estándar produce un modelo de vocabulario fijo después del ajuste; los autores no reportan una métrica de retención open-vocabulary para ese camino. Evaluarla exige reinyectar vocabulario abierto y aplicar un protocolo explícito, de modo que especialización in-domain y capacidad abierta permanezcan como dimensiones separadas (A. Wang et al., 2025).

En los dual-encoders, el ajuste de extremo a extremo sobre datasets cerrados requiere estrategias de regularización para evitar el colapso del espacio de embeddings compartido del que depende la capacidad abierta (Minderer et al., 2022). OWLv2 aporta además la receta OWL-ST de autoentrenamiento con pseudoanotaciones; el uso de un vocabulario diverso derivado de n-gramas preserva mejor la generalización que un espacio de etiquetas estrecho (Minderer et al., 2023). En Florence-2, el ajuste mediante LoRA modifica una fracción acotada de parámetros, aunque la retención de clases base se informa como parcial y dependiente de la configuración (Ucar et al., 2025; Xiao et al., 2024).

Como tal, no existe una jerarquía universal de familias frente al fine-tuning. La comparación defendible se realiza por receta concreta, distinguiendo parámetros actualizados, datos de adaptación y evaluación posterior de generalización. La Tabla 4 resume las estrategias documentadas y sus condiciones de retención.

**Tabla 4**

*Estrategias de fine-tuning documentadas y retención OVD reportada por familia arquitectónica*

| **Familia / Modelo** | **Estrategia de fine-tuning** | **Retención OVD reportada** | **Condición clave** |
| --- | --- | --- | --- |
| Grounding DINO | Fine-tuning closed-set | No | Vocabulario restringido post-ajuste |
| Grounding DINO | Preentrenamiento continuado open-set | Sí | LR reducido; módulos congelados; datos mixtos |
| Grounding DINO | Fine-tuning open-vocabulary (base a novel) | Sí | Evaluación explícita en categorías no vistas |
| Grounding DINO | Adaptación LoRA | Sí | Backbones congelados; solo *adapters* entrenables |
| YOLO-World | Fine-tuning con MixedGroundingDataset | Parcial | Depende de capas ajustadas; text encoder frágil |
| YOLO-World | Fine-tuning closed-set (MultiModalDataset) | No | Vocabulario fijo en JSON |
| YOLO-World | Reparametrización eficiente (sin RepVL-PAN) | No | Text encoder removido; equivale a YOLOv8 |
| YOLOE | Transferring (linear probing / full tuning) | No evaluada por los autores | La receta estándar produce vocabulario fijo; la retención requiere reinyectar y evaluar vocabulario abierto |
| OWL-ViT / OWLv2 | Fine-tuning de extremo a extremo con regularización | Parcial | Requiere estrategias de regularización |
| OWL-ViT / OWLv2 | Self-training (OWL-ST) con pseudo-anotaciones | Sí | Vocabulario diverso (n-gramas) preserva OVD |
| Florence-2 | Fine-tuning con LoRA | Parcial | Retención parcial de clases base; encoder congelado recomendado |

***Nota.*** “Retención OVD reportada” resume el comportamiento informado para la receta y el protocolo indicados; no constituye una propiedad universal de la familia arquitectónica. “Parcial” indica una retención dependiente de la configuración específica —capas congeladas, tasa de aprendizaje, datos de entrenamiento y evaluación sobre categorías no vistas—. Fuente: elaboración propia basada en AILab-CVC (2024), Cheng et al. (2024), Liu et al. (2024), Minderer et al. (2022, 2023), Rasaee et al. (2025), Ucar et al. (2025), A. Wang et al. (2025), Xiao et al. (2024) y X. Zhao et al. (2024).

La evidencia sintetizada en la Tabla 4 permite identificar tres factores recurrentes: qué parámetros se ajustan o congelan, la amplitud y diversidad del vocabulario utilizado durante el entrenamiento, y la existencia de una evaluación explícita sobre categorías no vistas. Estos factores interactúan con la arquitectura, pero los trabajos revisados no aíslan sus efectos mediante un protocolo común. Por ello, no corresponde afirmar que una familia tolere mejor el ajuste completo, más bien, corresponde describir qué receta retuvo capacidad OVD, bajo qué datos y con qué protocolo de evaluación.

#### 15.2.5. Brechas identificadas en el dominio de la construcción civil

A partir de la revisión y síntesis de los enfoques presentados, se pone de manifiesto un conjunto de limitaciones estructurales que no quedan plenamente resueltas por los modelos actuales de detección *open-vocabulary*. Estas brechas delinean líneas de trabajo relevantes para etapas posteriores del proyecto y permiten anticipar desafíos técnicos que deberán abordarse durante el diseño arquitectónico y la implementación del prototipo.

##### 15.2.5.1. Contextualización semántica limitada

La mayoría de los detectores OVD actuales resuelven la detección como una combinación de localización espacial y compatibilidad textual evaluada de manera independiente para cada región candidata (Zareian et al., 2021; Liu et al., 2024). Este enfoque, aunque efectivo para identificar objetos individuales, no garantiza consistencia contextual entre múltiples entidades detectadas ni permite razonar sobre relaciones espaciales o semánticas entre ellas.

En entornos industriales y de construcción, muchos conceptos relevantes para la seguridad son inherentemente composicionales y dependen del contexto espacial. Condiciones como "persona sin casco cerca de excavación", "operario en zona de tránsito vehicular" o "escalera bloqueando salida de emergencia" requieren no solo detectar cada elemento de manera aislada, sino también evaluar sus relaciones geométricas y semánticas. Esta limitación impide dar por resueltas las condiciones relacionales a partir de la salida local del detector y exige que cualquier tratamiento adicional se defina y valide de forma explícita.

##### 15.2.5.2. Ausencia de consistencia temporal nativa

Los modelos de detección open-vocabulary operan predominantemente sobre imágenes estáticas, procesando cada cuadro de manera independiente sin mantener memoria de estados previos ni modelar explícitamente la evolución temporal de las detecciones. Esta característica introduce variabilidad entre cuadros consecutivos que puede manifestarse como fluctuaciones en los puntajes de confianza, apariciones y desapariciones espurias de detecciones, e inconsistencias en la asignación de etiquetas entre cuadros consecutivos.

En aplicaciones de video, particularmente aquellas orientadas a monitoreo continuo, esta variabilidad temporal resulta problemática. Los enfoques generativos, como Florence-2, tienden a exhibir mayor inestabilidad debido a la naturaleza autorregresiva de su decodificación (Xiao et al., 2024). La literatura reciente sugiere que la integración con módulos de seguimiento multi-objeto (MOT) constituye una estrategia efectiva para mitigar este problema, permitiendo que el *tracker* aporte coherencia temporal a las detecciones semánticamente ricas del OVD (S. Li et al., 2023). No obstante, esta integración introduce complejidad arquitectónica adicional y requiere considerar la compatibilidad entre el detector y el método de seguimiento seleccionado.

##### 15.2.5.3. Sensibilidad a la formulación del prompt

La flexibilidad semántica que caracteriza a la detección open-vocabulary introduce una dependencia significativa respecto de la formulación exacta de las consultas textuales. Investigaciones en modelos visión-lenguaje han demostrado que pequeños cambios en la redacción de las consultas pueden producir diferencias significativas en el desempeño, incluso cuando diferentes formulaciones refieren al mismo concepto subyacente (Zhou et al., 2022b). Esta sensibilidad tiene implicancias directas para la usabilidad del sistema. Por ejemplo, usuarios con diferentes niveles de experiencia o distintas convenciones lingüísticas pueden obtener resultados heterogéneos ante objetivos de detección equivalentes.

Esta observación motivó el desarrollo de técnicas de prompt learning, donde los tokens de contexto se reemplazan por vectores aprendibles que se optimizan con datos etiquetados del dominio objetivo (Zhou et al., 2022b; Khattak et al., 2023). Sin embargo, las estrategias desarrolladas para clasificación de imágenes no se transfieren directamente al contexto de detección. Se demostró que la optimización automática de representaciones de prompts —específicamente diseñada para tareas de detección— supera consistentemente a los prompts elaborados mediante ingeniería manual, evidenciando la necesidad de enfoques especializados para el dominio OVD (Du et al., 2022). Adicionalmente, algunos modelos recientes abordan parcialmente esta limitación mediante el soporte de prompts visuales que permiten anclar la detección a ejemplos concretos en lugar de depender exclusivamente de descripciones textuales (Jiang et al., 2024).

##### 15.2.5.4. Sensibilidad al dominio de aplicación

Los benchmarks estándar utilizados para evaluar modelos OVD —como MS COCO con 80 categorías de objetos cotidianos (Lin et al., 2014) o LVIS con más de 1200 categorías de distribución long-tail (Gupta et al., 2019)— no representan plenamente las condiciones visuales y semánticas de entornos industriales especializados. En el contexto específico de obras de construcción, factores como iluminación extrema, oclusiones frecuentes por maquinaria y estructuras, indumentaria especializada de protección, y presencia de equipamiento industrial introducen distribuciones visuales que difieren significativamente de los datos de preentrenamiento.

Los resultados publicados en benchmarks generales no predicen por sí mismos el desempeño sobre una condición de dominio específica. Grounding DINO con backbone Swin-L pasa de 52,5 AP en COCO a 26,1 mean AP sobre los 35 conjuntos de ODinW. En consecuencia, la transferencia al dominio de construcción debe verificarse mediante una línea base zero-shot propia y un conjunto de prueba congelado, sin asumir equivalencia entre COCO o LVIS y la condición objetivo (Liu et al., 2024).

Como referencia supervisada in-domain, YOLOR alcanzó un mAP@0,5 de 0,883 sobre SHEL5K y un AP@0,5 de 0,907 para la clase *head*; YOLOv5x alcanzó un mAP@0,5 de 0,866 sobre CHV; y YOLOv9-e reportó un mAP@0,5 aproximado de 0,71 sobre SH17, con valores entre 0,58 y 0,69 para las variantes de YOLOv8 (Otgonbold et al., 2022; Wang et al., 2021; Ahmad & Rahimi, 2025).

Estas cifras corresponden a detectores entrenados sobre taxonomías específicas de EPP y no constituyen una comparación directa con los resultados de COCO o LVIS. En particular, el AP@0,5 de 0,907 para la clase head muestra que un detector supervisado puede alcanzar un desempeño alto sobre esa categoría en SHEL5K. La cifra no permite inferir una dificultad intrínseca universal, pero sí establece una referencia in-domain para analizar el costo de formular la condición sin entrenamiento específico.

La evidencia ubicada específicamente en el cruce entre vocabulario abierto y EPP es todavía limitada. Choi y Greer (2024) evaluaron OWLv2 zero-shot sobre 5.210 imágenes: obtuvieron AP@IoU>0,5 de 0,6767 para *person* y 0,6493 para detección directa de *hardhat*. Al introducir asociación jerárquica, la clase head —cabeza sin casco— alcanzó 0,1024 AP y la cascada multietapa obtuvo 0,2699 AP para detección de casco. Estas cifras no equivalen a una métrica de condición o alerta, pero muestran que la asociación persona–cabeza–EPP agrega dificultad respecto de detectar los componentes por separado.

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
| Escasez de evaluación OVD × EPP | La literatura ofrece evidencia directa limitada. Choi y Greer (2024) reportan AP@IoU>0,5 de 0,6767 para person, 0,6493 para detección directa de *hardhat*, 0,1024 para la clase head y 0,2699 para la cascada multietapa. El relevamiento no identificó evaluaciones de Grounding DINO o YOLO-World zero-shot sobre SHEL5K o CHV, ni un benchmark de EPP multi-fuente bajo protocolo COCO. | Se requiere una línea base zero-shot propia y un conjunto de prueba congelado; la respuesta experimental se presenta fuera del estado del arte. |

***Nota.*** Las brechas listadas delimitan problemas técnicos que el protocolo y la arquitectura deben abordar. No se presentan como limitaciones insalvables. Fuente: elaboración propia basada en Choi y Greer (2024), Chen y Zou (2025), Gupta et al. (2019), S. Li et al. (2023), Lin et al. (2014), Liu et al. (2024), Zareian et al. (2021) y Zhou et al. (2022b).

#### 15.2.6. Síntesis de la sección y avance al seguimiento multi-objeto

El análisis de los paradigmas OVD evidencia que la viabilidad de su integración en sistemas de monitoreo continuo está condicionada por cuatro factores: balance entre expresividad semántica y eficiencia de inferencia, diseño sistemático de prompts para el dominio específico, mecanismos de compensación de la variabilidad temporal cuadro a cuadro, y evaluación empírica en condiciones visuales de construcción civil. Los dos últimos factores remiten directamente al problema de persistencia temporal: dado que la OVD produce observaciones instantáneas sin identidad ni continuidad, la sección siguiente analiza los métodos de seguimiento multiobjeto como mecanismo para sostener esas detecciones a lo largo del tiempo.

En las secciones posteriores se distinguirá entre calibración operativa y adaptación paramétrica. La primera comprende cambios de resolución de entrada, formulación del vocabulario, umbrales, postproceso y estabilización temporal sin modificar los pesos del modelo; la segunda refiere exclusivamente al ajuste de parámetros mediante fine-tuning u otras técnicas de entrenamiento. Con esta distinción se evita presentar configuraciones de plataforma como si fueran modelos reentrenados.

### 15.3. Seguimiento multiobjeto: métodos, métricas y brechas del estado del arte

El seguimiento multiobjeto (MOT) constituye el mecanismo que transforma las detecciones instantáneas producidas por el sistema OVD en trayectorias persistentes a lo largo del tiempo, habilitando la agregación temporal de evidencias necesaria para la generación de alertas operativas. En esta sección se analizan los métodos representativos del estado del arte en MOT para sistemas de video en tiempo real, las métricas de evaluación relevantes para el contexto del proyecto y las brechas identificadas en la intersección entre MOT y detección open-vocabulary.

#### 15.3.1. Métodos representativos

El estado del arte en MOT para sistemas de video en tiempo real está dominado por la familia SORT extendida, cuya evolución refleja el progreso en el manejo de oclusiones, la explotación de detecciones de baja confianza y la eliminación de dependencias de entrenamiento específico por dominio.

##### 15.3.1.1. SORT

SORT (Simple *Online* and Realtime *Tracking*) establece el esquema de referencia del paradigma tracking-by-detection moderno. Combina el filtro de Kalman para el modelado del movimiento con el algoritmo Húngaro para la asignación óptima de detecciones a trayectorias, utilizando IoU como única métrica de similitud. Su diseño minimalista prescinde de cualquier modelado de apariencia, lo que resulta en latencia muy baja —capacidad de operar a tasas superiores a 200 FPS— y ausencia total de dependencias de entrenamiento. La principal limitación de SORT es su baja robustez ante oclusiones: cuando un objeto no es detectado durante varios cuadros consecutivos, la trayectoria se termina y la re-asociación posterior puede producir un cambio de identificador (ID switch), fragmentando la trayectoria en múltiples segmentos (Bewley et al., 2016).

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

***Nota.*** CMC = Compensación de Movimiento de Cámara (Camera Motion Compensation). OC = Observation-Centric. La columna 'Dependencia de entrenamiento' refiere a componentes adicionales al detector base que requieren entrenamiento supervisado. FPS estimados corresponden a las configuraciones reportadas en los trabajos originales sobre hardware de referencia; pueden variar significativamente según el hardware y la resolución de entrada. Fuente: Elaboración propia basada en las fuentes citadas (Adžemović, 2025; Aharon et al., 2022; Bewley et al., 2016; Cao et al., 2023; Wojke et al., 2017; Y. Zhang et al., 2022).

##### 15.3.2.1. Observaciones críticas sobre la comparativa

La literatura comparativa muestra que los métodos de seguimiento difieren no sólo en sus resultados agregados, sino también en las dependencias que introducen. Los enfoques geométricos sin modelos de apariencia pueden acoplarse a detectores externos sin requerir entrenamiento adicional de ReID, mientras que las variantes basadas en apariencia o entrenamiento conjunto dependen de datos y componentes específicos (Adžemović, 2025; Wojke et al., 2017). Esta diferencia delimita un compromiso entre simplicidad de integración y robustez de asociación; por sí sola, no determina la elección de un tracker para una plataforma OVD.

#### 15.3.3. Métricas de evaluación para MOT

La comparación entre métodos de seguimiento requiere complementar sus diferencias arquitectónicas con criterios que permitan cuantificar la calidad de las trayectorias obtenidas. La evaluación de MOT considera dimensiones relacionadas pero distintas —como los errores de detección, la continuidad de identidad y la calidad de asociación—, por lo que la literatura emplea métricas específicas y complementarias para caracterizar su desempeño.

MOTA resume falsos negativos, falsos positivos y cambios de identidad respecto del *ground truth*, aunque su lectura está fuertemente condicionada por los errores de detección (Bernardin & Stiefelhagen, 2008). IDF1 enfatiza la consistencia de identidad a lo largo de la secuencia (Ristani et al., 2016), mientras que HOTA separa y combina calidad de detección, asociación y localización (Luiten et al., 2021). Estas métricas caracterizan al tracker, pero no miden el valor temporal de una alerta; la evaluación de un sistema asistivo exige niveles adicionales, cuya definición corresponde al protocolo experimental. Una comparación ampliada de estas métricas y de sus limitaciones se presenta en la Tabla A.2 del Anexo A.

#### 15.3.4. Brechas identificadas y desafíos para el prototipo

El análisis del estado del arte en MOT revela un conjunto de brechas que condicionan el diseño del prototipo y las decisiones metodológicas de la consolidación metodológica posterior. La Tabla 7 organiza estas brechas con su descripción técnica y su implicación específica para el proyecto.

**Tabla 7**

*Brechas identificadas en la aplicación de métodos MOT al contexto de seguridad en construcción civil en combinación con detección open-vocabulary*

| **Brecha identificada** | **Descripción** | **Implicación para el proyecto** |
| --- | --- | --- |
| Dependencia de la calidad del detector subyacente | El rendimiento del MOT está fuertemente acoplado al desempeño del detector. Errores de detección —FP, FN, *bounding boxes* inestables— se propagan al seguimiento, produciendo fragmentación de trayectorias, pérdidas de identidad y asociaciones erróneas (S. Li et al., 2025) | En el pipeline OVD + MOT, la variabilidad inherente de la detección open-vocabulary puede amplificar errores de asociación; el diseño del sistema debe contemplar estrategias de filtrado y umbralización que reduzcan el ruido de entrada al tracker |
| Fragilidad ante oclusiones prolongadas | Aunque los métodos modernos manejan oclusiones breves, las oclusiones de larga duración producen terminación prematura de trayectorias, re-asociaciones inciertas y aumento de ID switches (Du et al., 2024) | En entornos de obra civil con alta densidad de obstrucciones (andamios, maquinaria, materiales), la robustez ante oclusiones es una restricción de diseño relevante que debe evaluarse empíricamente |
| Métricas estándar no alineadas con objetivos operativos de seguridad | Las métricas MOTA, IDF1 y HOTA evalúan el desempeño del seguimiento cuadro a cuadro sin considerar el impacto operativo diferenciado de distintos tipos de error en el contexto de seguridad laboral (Luiten et al., 2021) | Se deben definir criterios de evaluación del componente MOT alineados con el dominio: persistencia mínima para disparar alertas, penalización diferenciada de ID switches en condiciones de riesgo, y tolerancia ante falsos positivos por oclusión |
| Ausencia de datasets de construcción con anotaciones de seguimiento | Los benchmarks estándar de MOT (MOT17, MOT20, DanceTrack) no contemplan el dominio de obras civiles; la evaluación del tracker en condiciones representativas requiere datos del dominio específico (Dendorfer et al., 2020; Milan et al., 2016) | La validación del componente MOT en el prototipo no puede apoyarse en benchmarks estándar; se requiere la definición de un protocolo de evaluación propio con datos recopilados en el contexto del proyecto |

***Nota.*** Las brechas listadas definen el espacio de problemas abiertos que se abordan en las siguientes etapas. Fuente: Elaboración propia basada en las fuentes citadas (Adžemović, 2025; Dendorfer et al., 2020; Du et al., 2024; S. Li et al., 2025; Luiten et al., 2021; Milan et al., 2016).

La brecha de ausencia de datasets de construcción con anotaciones de seguimiento merece una consideración adicional. Los benchmarks estándar de MOT —MOT17, MOT20, DanceTrack— fueron diseñados para escenarios de peatones en entornos urbanos y eventos de danza respectivamente, con distribuciones visuales que difieren significativamente de una obra civil: densidad de cámara fija en planos elevados, entidades heterogéneas (personas, maquinaria, materiales), indumentaria de protección que puede confundir a los modelos de apariencia, y configuraciones de oclusión determinadas por la geometría de la obra. Esta brecha no puede resolverse mediante adaptación de los benchmarks existentes, sino que requiere de la definición de un protocolo de evaluación propio que se apoyará en los datos recopilados durante la fase experimental del proyecto.

### 15.4. Video en tiempo real y streaming: protocolos, servidores y brechas del estado del arte

#### 15.4.1. Protocolos de transmisión de video de baja latencia

Los protocolos de transmisión de video constituyen un componente relevante dentro del análisis de sistemas de video en tiempo real, debido a que condicionan la forma en que los flujos provenientes de cámaras o fuentes de video son transportados hacia los módulos de procesamiento, visualización o almacenamiento. En el contexto del presente proyecto, su estudio resulta necesario porque la detección open-vocabulary no opera sobre imágenes aisladas, sino sobre secuencias continuas que deben ser recibidas, decodificadas y procesadas con una latencia compatible con la generación oportuna de alertas.

Desde una perspectiva general, los protocolos de streaming pueden diferenciarse por dimensiones como el modelo de entrega, el esquema de distribución, la tolerancia a pérdidas, los mecanismos de *buffering* y el orden de magnitud de latencia que suelen alcanzar bajo determinadas condiciones de red y configuración. Sin embargo, estos valores no deben interpretarse como propiedades absolutas de cada protocolo, ya que la latencia final depende del pipeline completo: captura, codificación, transporte, decodificación, inferencia, evaluación de patrones y comunicación de resultados. Estos componentes serán retomados con mayor detalle en el marco teórico y en la descripción técnica del sistema, donde se analizará su impacto dentro de la arquitectura experimental.

En esta sección, el análisis se limita a revisar los protocolos y familias de transmisión más relevantes para aplicaciones de baja latencia, identificando sus características principales, sus restricciones prácticas y su grado de compatibilidad con un sistema de análisis automatizado de video. Esta revisión permite establecer criterios preliminares para la selección posterior del *stack* de medios, sin definir todavía una implementación definitiva.

##### 15.4.1.1. Criterios de clasificación de protocolos

Los protocolos de transmisión no se comparan adecuadamente mediante una única etiqueta de latencia. Su comportamiento resulta de la combinación entre la forma de controlar la entrega, la topología de distribución y la configuración temporal del flujo. Estas dimensiones permiten ordenar alternativas sin asumir que una familia sea superior en todos los escenarios.

La primera dimensión distingue quién gobierna la transferencia. En un esquema push, una vez establecida la sesión, el emisor sostiene el envío continuo y el receptor consume las unidades a medida que llegan. En un esquema pull, el receptor inicia y regula solicitudes sucesivas de contenido. La diferencia no determina por sí sola la latencia ni la confiabilidad: indica dónde reside el control operativo de la entrega y cómo avanza el flujo.

La segunda dimensión corresponde a la topología de distribución. En unicast, cada receptor mantiene una comunicación individual con el origen o con un intermediario; en multicast, una única transmisión se replica dentro de la red para un conjunto de receptores. Esta dimensión es independiente del modelo push o pull y permite analizar el costo de escalar destinatarios, el control por receptor y las restricciones de la infraestructura de red.

La tercera dimensión es el orden de magnitud de la latencia extremo a extremo. Su clasificación en rangos bajos, medios o altos tiene valor comparativo, pero no constituye una propiedad invariable del protocolo. El resultado depende también de la captura, la codificación, las pérdidas y retransmisiones, las colas, la decodificación y el buffer de reproducción. Por ello, la latencia debe interpretarse como efecto de una configuración completa y no como garantía aislada del estándar.

Estas dimensiones conforman un marco teórico común. La sección siguiente lo aplica a las principales familias de protocolos y explicita qué combinación de control de entrega, topología y compromiso temporal caracteriza a cada una.

##### 15.4.1.2. Mapa de familias de protocolos según los criterios de clasificación

Al aplicar los criterios anteriores, las familias se organizan por su perfil operativo dominante y por el tramo del sistema que resuelven. El mapa resultante no establece equivalencias ni un ordenamiento general: muestra cómo cada alternativa combina control de entrega, distribución, resiliencia y latencia.

RTSP/RTP representa el perfil de ingesta continua asociado a cámaras IP. RTSP gobierna la sesión mediante la descripción del flujo, la negociación de parámetros y las operaciones de reproducción, mientras que RTP transporta el medio como un flujo continuo y RTCP informa pérdida y *jitter* (Schulzrinne et al., 1998, 2003, 2016). En esta combinación, el cliente controla el establecimiento de la sesión, pero, una vez iniciada, el medio se envía de forma continua. RTP puede operar en unicast o multicast y sobre UDP, o intercalado sobre la conexión TCP de RTSP. Su madurez y su adopción por ONVIF Profile S explican su presencia extendida en videovigilancia y cámaras IP industriales (ONVIF, 2019).

Su ubicación en el mapa no implica una latencia invariable. El retardo extremo a extremo depende de la captura, la codificación, la red, la decodificación y, de manera marcada, del buffer del receptor. Axis Communications AB (2015) identifica el play-out buffer como un componente que puede dominar el retardo cuando se prioriza estabilidad frente a jitter. Bajo condiciones favorables, RTSP/RTP puede operar aproximadamente entre 200 y 800 ms, mientras que configuraciones de videovigilancia con buffering conservador pueden elevarlo a valores de entre 1.000 y 2.000 ms o más.

Las demás familias responden a prioridades diferentes. RTMP se utiliza principalmente para contribución push y unicast hacia un servidor mediante una sesión persistente. HLS y MPEG-DASH adoptan entrega pull y segmentada sobre HTTP; su integración con cachés y CDN favorece la distribución masiva, a costa del retardo de segmentación, incluso cuando las variantes de baja latencia reducen ese margen. WebRTC privilegia la interacción subsegundo mediante transporte seguro y control de congestión, mientras que SRT y RIST combinan transporte sobre UDP con recuperación selectiva de pérdidas dentro de un presupuesto temporal. No son sustitutos directos: el mapa distingue perfiles orientados a contribución, distribución escalable, interacción y transporte resiliente de baja latencia. La Tabla 8 sintetiza estos compromisos sin convertirlos en un ranking universal (ISO/IEC, 2022; Keranen et al., 2018; May, 2017; Sharabayko et al., 2024; Video Services Forum, 2020).

#### 15.4.2. Alternativas complementarias de ingesta, transporte y distribución

El mapa anterior caracteriza el transporte de un flujo de medios ya codificado, pero un pipeline completo incorpora decisiones que pertenecen a capas distintas. La captura mediante SDK, la intermediación de un servidor de medios y la distribución de alertas intervienen, respectivamente, en el acceso a la fuente, la transformación o retransmisión del video y la entrega de eventos posteriores a la inferencia; por ello, no corresponde tratarlas como alternativas de una misma categoría.

En la entrada, la captura mediante SDK evita consumir necesariamente un *stream* de red preconfigurado. En cámaras inteligentes, el *host* puede gobernar un pipeline ejecutado en el dispositivo y recibir las unidades visuales o salidas requeridas para el procesamiento posterior. Esta modalidad permite desplazar operaciones acotadas de adquisición o preprocesamiento hacia la fuente, sin equipararla a la ejecución de inferencia OVD en el borde (Luxonis, s. f.-b).

Cuando se incorpora un servidor de medios, su efecto depende de la función que cumpla. Un relay agrega principalmente un salto de red y gestión de colas; una pasarela o un reempaquetador adapta protocolos o contenedores; y la transcodificación añade decodificación y recodificación. Para un sistema de analítica visual, esta distinción resulta más informativa que un catálogo de productos, porque permite separar el costo del transporte del costo de transformar el contenido (Ahmad et al., 2005; Amirante et al., 2014, 2015).

Después de la inferencia, el problema deja de ser el transporte de video y pasa a ser la distribución de eventos. Los patrones publicador-suscriptor desacoplan la generación de alertas de sus consumidores. MQTT formaliza niveles de calidad de servicio. QoS 1 requiere confirmación mediante PUBACK y ofrece una semántica de entrega al menos una vez, por lo que la aplicación debe tolerar reentregas y controlar idempotencia cuando un mismo evento no deba producir efectos duplicados (OASIS, 2019).

#### 15.4.3. Brechas del estado del arte en el streaming/OVD

Las tecnologías y arquitecturas actuales de streaming presentan un conjunto de limitaciones que condicionan directamente el diseño del pipeline experimental.

##### 15.4.3.1. Ausencia de benchmarks extremo a extremo integrados para pipelines OVD

Los benchmarks de inferencia de modelos OVD (p. ej., AP en COCO/LVIS, FPS en GPU aislada) operan de forma independiente respecto de los benchmarks de streaming (latencia de transporte, *throughput* de protocolo) y de las métricas de plataformas de edge computing (TOPS, FPS bajo carga térmica). Para una plataforma como E-OVRT-VDP el criterio de selección debe basarse en mediciones reproducibles del pipeline completo, y no extrapolarse directamente de métricas parciales o aisladas.

Esta brecha implica que no existen referentes directos en la literatura que permitan predecir con confianza el desempeño de un sistema que combina ingesta de video, inferencia OVD y emisión de eventos bajo restricciones de latencia propias de operación en tiempo real. En consecuencia, la validación empírica del pipeline completo constituye una contribución necesaria del proyecto. La definición de protocolos de medición reproducibles se aborda en las siguientes secciones.

##### 15.4.3.2. Integración de modelos OVD dentro de pipelines de streaming optimizados

Los frameworks de streaming más maduros para video analytics en tiempo real, como NVIDIA DeepStream, han sido históricamente diseñados y optimizados para detectores de clases fijas con arquitecturas convolucionales estándar, cuyos patrones de integración asumen una entrada de imagen y un conjunto predefinido de clases de salida (NVIDIA, 2024). Si bien el ecosistema ha comenzado a incorporar soporte para modelos open-vocabulary —por ejemplo, NVIDIA TAO Toolkit incluye flujos de exportación y despliegue para Grounding DINO (NVIDIA, s. f.-g)—, la integración de estos modelos en pipelines de streaming presenta desafíos técnicos que no se resuelven con la misma inmediatez que los detectores convencionales.

En particular, la conversión de modelos OVD a formatos optimizados como TensorRT puede requerir adaptaciones no triviales cuando la arquitectura incluye operadores no soportados nativamente o componentes dinámicos asociados a la codificación de prompts textuales. Dado que TensorRT no admite entradas de tipo texto, la etapa de tokenización debe separarse del grafo del modelo y gestionarse externamente (NVIDIA, s. f.-g), lo que introduce complejidad adicional en el diseño del pipeline. Más ampliamente, la arquitectura multi-modal que caracteriza a los modelos OVD —con un encoder visual y un encoder textual que interactúan mediante mecanismos de fusión— no se alinea directamente con los patrones de integración nativos de los plugins de inferencia estándar de estos frameworks, aunque rutas alternativas como la integración con Triton Inference Server ofrecen mayor flexibilidad al soportar modelos en múltiples formatos y frameworks (NVIDIA, s. f.-h). Esta brecha en particular implica que la integración de modelos OVD dentro del pipeline de streaming requerirá capas de adaptación específicas.

##### 15.4.3.3. Interoperabilidad efectiva entre protocolos heterogéneos

Aun cuando la literatura describe los roles del servidor de medios y las funciones de pasarela, reempaquetamiento y transcodificación, no ofrece evidencia consolidada sobre el overhead real introducido por las conversiones entre protocolos —por ejemplo, de RTSP a WebRTC o de RTMP a SRT— en condiciones de operación representativas. La transcodificación, el reempaquetamiento entre contenedores de medios —como MPEG-TS, FLV o fMP4— y la adaptación entre pilas de transporte pueden agregar latencia y puntos de fallo que no quedan reflejados en las especificaciones de cada protocolo por separado.

En el contexto del proyecto, esta brecha resulta relevante, dado que en entornos reales de obra el parque de cámaras puede exponer flujos mediante protocolos diversos. Si bien el prototipo experimental operará previsiblemente con un conjunto acotado de fuentes y protocolos, la identificación de este vacío en la literatura permite anticipar un factor de complejidad para escenarios de despliegue más amplios y orienta el diseño a una solución que no introduzca dependencias rígidas con un único protocolo de ingesta.

##### 15.4.3.4. Métricas de evaluación alineadas con objetivos de seguridad laboral

Las métricas estándar de evaluación de sistemas de streaming, tales como latencia media, throughput, tasa de pérdida de paquetes y calidad visual (PSNR/SSIM), no capturan adecuadamente el valor operativo de un sistema orientado a la detección asistiva de riesgos en obra. De manera análoga a lo identificado en la sección de OVD respecto de las métricas de detección, las métricas de streaming convencionales no consideran aspectos como el tiempo transcurrido entre el inicio de una condición de riesgo y la notificación al operador, la continuidad de detección bajo variaciones de calidad del stream, o el impacto diferenciado de artefactos de compresión sobre la detectabilidad de elementos de protección personal.

#### 15.4.4. Síntesis comparativa de protocolos

La Tabla 8 sintetiza las características principales de los protocolos analizados, con énfasis en las dimensiones de mayor relevancia para el diseño del sistema E-OVRT-VDP.

**Tabla 8**

*Comparativa de protocolos de transmisión de video de baja latencia para sistemas de video analítico en tiempo real*

| **Protocolo** | **Lat. E2E** | **Transporte base** | **Modelo de entrega** | **Resiliencia a pérdida** | **Cifrado nativo** | **Caso de uso principal** |
| --- | --- | --- | --- | --- | --- | --- |
| RTSP/RTP | ~200–800 ms | UDP (o TCP) | RTSP controla la sesión; RTP transporta el flujo | Media (con RTCP) | Opcional (RTSPS) | Cámaras IP industriales, CCTV, entornos LAN controlados |
| RTMP | ~2–5 s | TCP | Push | Alta (TCP garantiza entrega) | Sí (RTMPS/TLS) | Ingesta a plataformas de streaming; encoders hacia servidores |
| HLS / MPEG-DASH | ~5–45 s (LL: ~2–10 s) | HTTP/TCP | Pull (segmentado) | Alta (CDN + HTTP) | Sí (HTTPS) | Distribución masiva de contenido; viewers simultáneos elevados |
| WebRTC | < 500 ms | UDP (SRTP sobre DTLS) | Push/Pull (P2P o SFU) | Media (con NACK/FEC) | Sí (DTLS-SRTP, obligatorio) | Interactividad ultra-baja latencia; videoconferencia; monitoreo P2P |
| SRT | ~120–500 ms (configurable) | UDP + ARQ selectivo | Push o Pull | Alta (ARQ con presupuesto de tiempo) | Sí (AES-128/256) | Contribución broadcast; enlaces WAN no confiables; 4G/5G |
| RIST | ~120–500 ms | RTP + ARQ (RTCP FB) | Push o Pull (multicast posible) | Alta (ARQ + FEC) | Sí (DTLS) | Broadcast profesional; distribución multicast en redes gestionadas |

***Nota.*** Los rangos de latencia extremo a extremo reportados son valores típicos dependientes de configuración, no compromisos de los estándares. La latencia final está determinada por el pipeline completo (captura, codificación, transporte, decodificación, inferencia), no únicamente por el protocolo. HLS/DASH LL = Low-Latency HLS / DASH. DTLS-SRTP = combinación de Datagram TLS y Secure RTP (cifrado obligatorio en WebRTC). ARQ = Automatic Repeat reQuest. FEC = Forward Error Correction. SFU = Selective Forwarding Unit. NACK = Negative Acknowledgement. Fuente: Elaboración propia basada en Axis Communications AB (2015), DASH Industry Forum (2020), ISO/IEC (2022), Keranen et al. (2018), May (2017), Pantos (2025), Parmar y Thornburgh (2012), Roy (2024), Schulzrinne et al. (1998, 2003, 2016), Sharabayko et al. (2024), Sonono (2019), Video Services Forum (2020, 2024) y World Wide Web Consortium (2025).

La tabla muestra que no existe un protocolo que maximice simultáneamente latencia mínima, alta resiliencia a pérdidas y escalabilidad, lo cual es coherente con el enfoque de diseño de cada estándar, orientado a prioridades diferentes según el contexto de aplicación. En arquitecturas comúnmente adoptadas, esta situación suele abordarse mediante esquemas híbridos que emplean protocolos distintos por tramo del flujo de video. Un esquema típico suele dedicar uno para ingesta y transporte desde el origen hacia un servidor o plataforma de medios (en entornos LAN o WAN con distintos niveles de control), y otro para distribución/visualización hacia clientes finales, donde los requerimientos de interactividad, número de usuarios y compatibilidad con navegadores influyen de manera determinante. De forma complementaria, también es habitual que los protocolos HTTP adaptativos (HLS/DASH) se reserven para consumo masivo, reproducción diferida o escenarios donde la prioridad sea la escalabilidad y la tolerancia a variaciones de red, más que la inmediatez.

## 16. Marco teórico

El marco teórico concentra los conceptos, categorías normativas y fundamentos técnicos que sostienen el diseño posterior del prototipo. Su propósito es establecer una base conceptual para justificar qué se detecta, cómo se interpreta, bajo qué restricciones opera el sistema y qué condiciones ético-legales delimitan su uso.

### 16.1. Organización interna del marco teórico

Este capítulo se organiza a partir de los dominios conceptuales que sustentan el diseño y la evaluación de la plataforma experimental. Cada dominio responde a una pregunta central del proyecto y permite delimitar, desde una perspectiva técnica o normativa, las condiciones bajo las cuales resulta posible construir un sistema de detección open-vocabulary aplicado al monitoreo de seguridad en construcción civil.

En primer lugar, se aborda el dominio de aplicación, vinculado con la seguridad laboral en obras y con la identificación de condiciones de riesgo observables mediante análisis visual. Luego se desarrollan los fundamentos de la detección open-vocabulary, el seguimiento multiobjeto, la transmisión de video en tiempo real y las restricciones ético-legales asociadas al uso de sistemas de visión por computadora en contextos laborales.

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
| Convergencias y preguntas rectoras | ¿Qué brechas atraviesan los dominios y qué debe definir el protocolo experimental? | Integra restricciones, explica límites y formula las preguntas que guían la consolidación metodológica. |

***Nota.*** Cada dominio se corresponde con una sección de este capítulo. Fuente: elaboración propia.

### 16.2. Condiciones de riesgo observables

El análisis visual requiere delimitar qué se entiende por condición de riesgo observable. En este trabajo, esa expresión no designa un incumplimiento normativo demostrado, sino una configuración visible de personas, elementos de protección o componentes del entorno que resulta relevante para la prevención y puede representarse en imágenes o video. La normativa aporta el fundamento de esa relevancia, pero no se utiliza como una lista exhaustiva de requisitos que el prototipo deba fiscalizar.

Para integrar una condición al alcance experimental se consideran tres propiedades: su correspondencia con un riesgo preventivo reconocido, la existencia de evidencia visual susceptible de anotación humana y una definición suficientemente precisa para contrastar la salida del sistema con una referencia. Con esta delimitación, lo que se busca es evitar confundir la observación de una señal con la certificación del cumplimiento de una obligación.

#### 16.2.1. Marco normativo de referencia

Como referencia general del dominio, la Ley 19.587 establece que las condiciones de higiene y seguridad deben orientarse a prevenir daños en el trabajo (Ley 19.587, 1972). Para la industria de la construcción, el Decreto 911/96 desarrolla disposiciones específicas sobre medidas preventivas y equipos de protección personal, atendiendo a los riesgos propios de una obra (Decreto 911/96, 1996). En esta sección, ambas normas se emplean para justificar la relevancia preventiva de determinadas evidencias visuales, no para reconstruir de manera exhaustiva el régimen jurídico aplicable.

De este marco se retienen dos ideas. La primera es que la prevención se orienta a reconocer y controlar condiciones anteriores al daño. La segunda es que algunas medidas preventivas poseen correlatos visibles, como la presencia de protección cefálica o de elementos de alta visibilidad. Sin embargo, la exigencia y adecuación de cada elemento dependen de la tarea, del riesgo y del contexto de uso. Por ello, la ausencia observada en una imagen no constituye por sí sola una infracción ni permite atribuir responsabilidades.

También quedan fuera del alcance de la observación visual las obligaciones cuya verificación exige documentación, mediciones, certificaciones, capacitación, inspección física o conocimiento detallado de la tarea. Una cámara puede registrar que un elemento no resulta visible, pero no determinar su homologación, vida útil, ajuste técnico ni correspondencia con todas las condiciones particulares del puesto. Esta diferencia entre referencia preventiva y juicio normativo delimita el papel del prototipo.

#### 16.2.2. Operacionalización de las condiciones nucleares

La operacionalización transforma una categoría preventiva en una evidencia que pueda observarse y evaluarse. El recorrido conceptual comprende tres niveles: una referencia normativa que justifica la relevancia del riesgo, una evidencia visual que puede anotarse en imagen o video y una condición formulada de manera evaluable. La relación entre esos niveles es metodológica y no convierte la predicción del sistema en una conclusión jurídica.

En el núcleo del trabajo se priorizan dos condiciones vinculadas con equipos de protección personal: CR-01, persona sin casco, y CR-02, persona sin chaleco reflectivo. Su selección responde a que pueden definirse mediante evidencia visual localizada sobre una persona y admiten una referencia humana reproducible. La Tabla 10 resume esta operacionalización y explicita el límite de lectura de cada condición.

**Tabla 10**

*Operacionalización de las condiciones nucleares del trabajo*

| **Condición nuclear** | **Evidencia visual de referencia** | **Lectura permitida y límite** |
| --- | --- | --- |
| CR-01 — Persona sin casco | Persona visible. No se observa casco en la región cefálica. | Indicio de posible ausencia de protección cefálica. No verifica homologación, estado, ajuste ni el contexto completo de exigibilidad. |
| CR-02 — Persona sin chaleco reflectivo | Persona visible. No se observa chaleco reflectivo en el torso. | Indicio de posible ausencia de alta visibilidad. No determina por sí solo si la tarea o la zona requerían ese EPP. |

***Nota.*** Las condiciones se expresan como señales visuales para evaluación experimental. La ausencia indicada no equivale a una determinación normativa ni permite verificar la certificación, el estado o el ajuste del EPP. Fuente: elaboración propia a partir de la Ley 19.587 (1972) y del Decreto 911/96 (1996).

En ambos casos, el objeto de análisis no es un elemento aislado, sino el estado observable de una persona respecto de un EPP esperado. La condición se construye a partir de la presencia de la persona y de que el elemento no resulte visible en la región correspondiente. Esta estructura composicional distingue la detección de objetos de la interpretación de una condición expresada por ausencia y enlaza con los fundamentos de percepción visión-lenguaje desarrollados en la sección siguiente.

El mismo criterio permitiría formular otras condiciones asociadas con trabajos en altura, zonas restringidas, interacción con maquinaria u obstrucciones. No obstante, su sola relevancia preventiva no basta para incorporarlas al núcleo, ya que pueden requerir relaciones espaciales, estimación geométrica, contexto operativo o evidencia adicional. Por ello, se consideran posibilidades de extensión y no capacidades asumidas del prototipo.

#### 16.2.3. Alcance y límites de la observación visual

La observabilidad conceptual, la detectabilidad técnica y la interpretación normativa constituyen niveles distintos. Una condición puede ser visible para una persona y, aun así, resultar difícil de detectar por variaciones de iluminación, resolución, perspectiva u oclusión. A su vez, una detección visual correcta puede no aportar el contexto necesario para determinar si una medida era exigible o si el elemento observado cumplía sus especificaciones técnicas.

En consecuencia, las salidas del sistema se interpretan como indicios trazables que requieren revisión humana. Las alertas son asistivas y no vinculantes, es decir, no certifican cumplimiento, no establecen responsabilidades, no realizan reconocimiento de identidad personal y no sustituyen al responsable de seguridad ni a la evaluación técnica en terreno. Su función consiste en señalar evidencia visual relevante, conservarla para su revisión y favorecer una supervisión más oportuna.

De esta forma, el marco normativo cumple una función que fundamenta por qué las condiciones seleccionadas son preventivamente pertinentes, de tal manera que la operacionalización define qué evidencia puede evaluarse y los límites de interpretación evitan atribuir al análisis visual capacidades que no posee.

### 16.3. Percepción visión-lenguaje: fundamentos conceptuales de la detección open-vocabulary

Como se mencionó anteriormente, la detección de objetos en imágenes ha sido históricamente un problema de clasificación cerrada, donde los sistemas reconocen únicamente las categorías para las que fueron entrenados. Este supuesto es incompatible con el dominio de seguridad laboral, donde las condiciones de riesgo son heterogéneas, cambian según la etapa de la obra y pueden formularse con precisión en lenguaje natural pero difícilmente acotarse en un conjunto fijo de clases predefinidas. El paradigma de detección de vocabulario abierto (OVD) rompe esa restricción al incorporar un encoder de lenguaje que permite guiar la detección mediante descripciones textuales arbitrarias.

La presente sección caracteriza los fundamentos conceptuales de la detección open-vocabulary, con énfasis en la transición desde los enfoques de vocabulario cerrado hacia modelos capaces de vincular información visual y lenguaje natural.

#### 16.3.1. Del closed-set al open-vocabulary

En la detección de objetos tradicional, el modelo aprende a localizar instancias en una imagen y a clasificarlas dentro de un vocabulario fijo, establecido de antemano y sin posibilidad de expansión en tiempo de inferencia. Esta formulación permite optimizar el rendimiento sobre benchmarks bien delimitados, como MS COCO con 80 categorías (Lin et al., 2014) o PASCAL VOC (Everingham et al., 2010), pero introduce una dependencia estructural entre el dominio de entrenamiento y el dominio de aplicación, porque el sistema solo puede detectar lo que fue explícitamente contemplado en el diseño.

La detección open-vocabulary supera esta restricción al separar el espacio semántico del conjunto de categorías de entrenamiento. En lugar de aprender representaciones para clases discretas y fijas, los modelos OVD aprenden a alinear regiones visuales con descripciones lingüísticas en un espacio de embeddings compartido. La noción de clase deja de ser un identificador discreto y pasa a representarse como una entidad semántica continua, definida dinámicamente por el contenido de la consulta (Zareian et al., 2021). En consecuencia, una categoría expresada en lenguaje natural durante la inferencia puede ser reconocida aunque el modelo nunca la haya visto etiquetada durante el entrenamiento, siempre que su representación semántica sea coherente con el espacio aprendido.

Esta capacidad no es absoluta. La calidad de la generalización zero-shot —ampliada en la sección 16.3.5— depende de la calidad y amplitud del preentrenamiento multimodal, y el desempeño sobre categorías muy específicas o visualmente inusuales puede ser significativamente inferior al observado sobre categorías cotidianas bien representadas en los datos de entrenamiento. Reconocer la potencia del paradigma OVD sin ignorar sus condiciones y límites es el propósito de las secciones que siguen.

#### 16.3.2. Mecanismos de alineación visión-lenguaje

El pilar técnico central de OVD es el uso de representaciones conjuntas de visión y lenguaje. Estas representaciones se obtienen mediante modelos multimodales entrenados para proyectar imágenes, regiones visuales y textos en un espacio latente compartido, donde la proximidad geométrica refleja afinidad semántica. El trabajo seminal en esta dirección es CLIP (Contrastive Language–Image Pre-training), que demostró la viabilidad de entrenar modelos con cientos de millones de pares imagen-texto recopilados de la web para aprender representaciones visuales altamente transferibles, alineadas con descripciones en lenguaje natural (Radford et al., 2021).

El entrenamiento contrastivo opera sobre la base de maximizar la compatibilidad entre pares imagen-texto correctos y minimizar entre pares incorrectos, produciendo un encoder visual y un encoder textual que proyectan imagen y texto a un espacio semántico compartido (Minderer et al., 2022, 2023; Radford et al., 2021). El proceso de detección resultante puede describirse en tres etapas conceptuales, donde 1) a partir de una imagen, el backbone visual genera representaciones asociadas a regiones candidatas, 2) a partir de una consulta textual (prompt), el encoder de lenguaje obtiene una representación semántica y finalmente, 3) la detección se resuelve evaluando la compatibilidad entre ambas representaciones mediante funciones de similitud, atención cruzada u otros mecanismos de alineación, aplicando non-maximum suppression sobre las regiones con mayor compatibilidad semántica. Este esquema introduce una separación conceptual entre localización espacial y reconocimiento semántico, lo que permite evaluar nuevas descripciones en tiempo de inferencia sin modificar los parámetros del modelo (Minderer et al., 2022).

#### 16.3.3. Rol del lenguaje natural como especificación dinámica

En detección open-vocabulary, el lenguaje funciona como una especificación de inferencia. Esto quiere decir que la consulta textual define qué concepto debe localizarse sin modificar el clasificador ni volver a entrenar el modelo. Esta propiedad permite expresar entidades, atributos y relaciones mediante vocabulario natural, pero introduce una variable ausente en los detectores closed-set, donde las formulaciones semánticamente cercanas no necesariamente producen representaciones equivalentes. La sensibilidad depende del encoder textual, del contexto léxico y del régimen de alineación empleado durante el preentrenamiento (Zhou et al., 2022b).

La literatura aborda este problema mediante ingeniería sistemática de prompts, prompt learning con tokens de contexto aprendibles y, en algunas arquitecturas, prompts visuales que anclan la consulta a un ejemplo (Du et al., 2022; Jiang et al., 2024; Khattak et al., 2023). Estas alternativas son modalidades de consulta documentadas, no requisitos universales. Para evaluar una condición de dominio, la formulación textual debe tratarse como parte del protocolo experimental,  comparando variantes bajo los mismos datos, umbrales y métricas y evitando atribuir al modelo diferencias producidas únicamente por la redacción.

#### 16.3.4. Composicionalidad, negación y condiciones definidas por ausencia

El aprendizaje contrastivo aproxima representaciones globales de imágenes y textos al recompensar la compatibilidad entre pares correctos y separar pares incorrectos. Ese objetivo no obliga a codificar de manera explícita quién realiza una acción, qué atributo modifica a cada entidad ni en qué orden aparecen los términos. Esto no significa que los modelos ignoren las palabras, sino que un buen desempeño de recuperación puede coexistir con baja sensibilidad a la estructura relacional de la frase.

Yuksekgonul et al. (2023) estudian esta limitación mediante ARO, un benchmark con más de 50.000 casos organizados en atribución, relación y orden. Los resultados muestran que modelos visión-lenguaje de referencia pueden apoyarse fuertemente en el inventario léxico y resolver coincidencias globales sin representar con igual robustez los vínculos entre sustantivos, atributos y relaciones. El comportamiento se aproxima así a una bolsa de palabras: los conceptos dominantes conservan gran peso aunque se intercambien modificadores o cambie la estructura que determina el significado.

Winoground aísla la composicionalidad con pares de captions que contienen exactamente las mismas palabras en distinto orden y se asocian con dos imágenes diferentes. Los modelos evaluados no superaron de manera consistente el azar al vincular cada caption con la imagen correcta (Thrush et al., 2022). La prueba elimina la ventaja del contenido léxico compartido y muestra que la alineación global no garantiza razonamiento visio-lingüístico sobre roles y relaciones.

En detección y phrase grounding, la asociación entre tokens y regiones aporta localización más fina que la recuperación global, pero la negación mantiene una dificultad conceptual. Una frase como «persona sin casco» contiene el concepto positivo casco. Sin embargo, la ausencia no constituye una región visible que pueda recibir una caja. Además, el solapamiento léxico puede hacer que el sustantivo positivo conserve influencia aun cuando el modificador cambie la condición solicitada (Liu et al., 2024). Evaluar ausencia exige definir qué región de la persona resulta pertinente, qué evidencia positiva debería encontrarse y bajo qué relación espacial se considera asociada.

Por ello, una condición definida por ausencia admite al menos dos formulaciones conceptuales. La primera pide directamente al modelo que localice la infracción completa. La segunda solicita evidencia positiva y deriva la ausencia mediante razonamiento sobre las detecciones. La primera delega composición y negación al modelo; la segunda separa percepción y relación, pero introduce reglas y posibles errores de asociación. La literatura no establece una alternativa universalmente superior. Su desempeño depende del modelo, del prompt, de la granularidad espacial y del dominio, por lo que la comparación debe permanecer como pregunta empírica. Esta limitación enlaza con la brecha de contextualización semántica de la sección 15.2.5.1 sin anticipar la estrategia que adopte el diseño.

#### 16.3.5. Generalización zero-shot y el problema del long-tail semántico

Un concepto estrechamente vinculado a la OVD es la generalización zero-shot, siendo esta la capacidad de reconocer conceptos no observados explícitamente durante el entrenamiento supervisado. Esta propiedad resulta especialmente relevante en dominios caracterizados por distribuciones de clases desbalanceadas o por una fuerte presencia de categorías poco frecuentes, denominadas en la literatura como long-tail semántico.

Los modelos OVD no eliminan por completo las limitaciones impuestas por los datos de preentrenamiento. Las categorías visualmente inusuales o semánticamente distantes de los conceptos mejor representados pueden exhibir un desempeño inferior al observado en categorías frecuentes. En construcción civil, esto afecta especialmente a categorías especializadas del dominio —incluidos determinados EPP y roles operativos— cuya representación en los datos generalistas puede ser limitada. Por ello, su desempeño zero-shot debe verificarse en material de dominio y no inferirse desde benchmarks generales.

La ampliación de datos y el autoentrenamiento mejoran la cobertura de categorías raras, pero no eliminan la brecha entre benchmarks generalistas y dominios especializados (Minderer et al., 2023).

#### 16.3.6. Dimensiones de comparación de modelos OVD

La literatura permite comparar modelos OVD a lo largo de dimensiones distintas, por ejemplo, la capacidad de generalización zero-shot y transferencia de dominio, la expresividad frente a atributos y relaciones, la latencia y dependencia del hardware, la modalidad de consulta, la disponibilidad de código y pesos y las posibilidades de adaptación paramétrica. Ninguna dimensión determina por sí sola la adecuación de una alternativa, y los resultados de benchmarks no son directamente transferibles entre hardware, resoluciones y regímenes de evaluación diferentes (Cheng et al., 2024; Liu et al., 2024; Minderer et al., 2022, 2023).

La retención open-vocabulary después del fine-tuning tampoco puede atribuirse a la familia arquitectónica. Como se sintetiza en la sección 15.2.4, depende de la receta concreta, es decir, qué parámetros se actualizan o congelan, si se conserva supervisión lingüística amplia y si el protocolo evalúa categorías no vistas (A. Wang et al., 2025; X. Zhao et al., 2024). Los prompts visuales, la segmentación o la ejecución híbrida entre modelos pueden describirse como capacidades presentes en parte de la literatura, pero no constituyen requisitos generales.

### 16.4. Persistencia temporal de entidades y fundamentos conceptuales del seguimiento multiobjeto

Una detección aislada no basta para sustentar una alerta temporal. Para distinguir entre una aparición breve y una condición que permanece, se requiere continuidad entre cuadros, una propiedad que la detección por cuadro no provee. El seguimiento multiobjeto (MOT) cumple esa función al asignar identificadores temporales internos a las entidades detectadas, estimar sus trayectorias cuadro a cuadro y sostener la continuidad ante omisiones breves. La presente sección caracteriza los fundamentos técnicos de ese mecanismo, sus métodos representativos y los compromisos relevantes para integrarlo en un sistema de monitoreo.

#### 16.4.1. La limitación temporal de la detección por cuadro

Un detector de objetos —incluyendo los modelos OVD— opera de manera fundamentalmente estática, donde dada una imagen, produce un conjunto de regiones detectadas con sus etiquetas semánticas y puntajes de confianza. Esta operación se realiza de manera independiente para cada cuadro del flujo de video, sin memoria ni referencia a los cuadros anteriores. En consecuencia, el mismo objeto físico presente en dos cuadros consecutivos es tratado como dos entidades sin relación, de tal forma que no existe ningún mecanismo que les asigne una identidad común ni que modele su trayectoria a lo largo del tiempo (Bewley et al., 2016; Luo et al., 2021).

Esta limitación tiene consecuencias operativas directas para el sistema de monitoreo. En primer lugar, la variabilidad cuadro a cuadro que caracteriza a los modelos OVD —fluctuaciones en puntajes de confianza, apariciones y desapariciones espurias e inconsistencias entre cuadros consecutivos (Xiao et al., 2024)— no puede filtrarse ni estabilizarse sin una capa que integre información temporal. En segundo lugar, muchas condiciones de riesgo no son eventos instantáneos, sino estados que deben persistir durante un intervalo mínimo para resultar operativamente significativos: una presencia sostenida en una zona restringida no equivale a una detección espuria de un único cuadro (Du et al., 2024). En tercer lugar, las alertas basadas en evidencia sostenida —y no en detecciones aisladas— pueden reducir la carga cognitiva y la fatiga de alerta asociada con falsos positivos frecuentes (Du et al., 2024).

El seguimiento multiobjeto aporta la capa de integración temporal que la detección por cuadro no ofrece, asignando identificadores temporales internos a las entidades detectadas, modelando su estado y trayectoria a lo largo de la secuencia y produciendo trayectorias estructuradas sobre las que puede agregarse evidencia temporal (Du et al., 2024; Milan et al., 2016).

#### 16.4.2. Fundamentos del MOT y del paradigma tracking-by-detection

El seguimiento multiobjeto estima trayectorias a partir de detecciones ruidosas e incompletas. En el paradigma tracking-by-detection, un detector externo localiza objetos en cada cuadro y el tracker mantiene un estado temporal para cada trayectoria activa. Este desacoplamiento permite integrar detectores con vocabularios y arquitecturas diferentes sin reentrenar necesariamente el componente temporal, aunque conserva una dependencia inevitable: toda trayectoria se origina en las observaciones entregadas por el detector (Adžemović, 2025; Bewley et al., 2016).

El estado de una trayectoria resume información acumulada dentro de la secuencia, como el identificador temporal, última caja observada, la antigüedad y el número de cuadros sin asociación, entre otros atributos posibles. Ese identificador sólo organiza observaciones dentro del flujo, y no representa identidad personal ni garantiza continuidad entre cámaras, sesiones o reinicios. Una trayectoria puede encontrarse en estado tentativo, activo o perdido según la evidencia disponible, pero la terminología concreta depende del método y no constituye un requisito universal (Milan et al., 2016).

El ciclo de seguimiento comprende tres operaciones conceptuales. La predicción estima dónde debería encontrarse una trayectoria en el cuadro siguiente; puede utilizar el último estado observado o un modelo de movimiento. La similitud cuantifica la compatibilidad entre una predicción y una detección. La intersección sobre unión (IoU) divide el área de intersección de dos cajas por el área de su unión y ofrece una señal geométrica interpretable, sin parámetros aprendidos. Su principal límite aparece cuando el desplazamiento, la oclusión o la inestabilidad de las cajas reducen la superposición aun cuando ambas observaciones correspondan a la misma entidad (Bewley et al., 2016).

La asignación convierte la matriz de similitudes en correspondencias globales. Habitualmente se formula como un problema bipartito entre trayectorias y detecciones y se resuelve con el algoritmo húngaro. Los mecanismos de gating descartan pares incompatibles antes de asignar; los umbrales controlan qué costo resulta aceptable. Las detecciones no asignadas pueden iniciar trayectorias nuevas y las trayectorias sin observación pueden conservarse durante una ventana limitada. Esta memoria tolera omisiones breves, pero incrementarla también aumenta el riesgo de reasociar una detección a la trayectoria equivocada.

La apariencia agrega embeddings de reidentificación a la evidencia geométrica y puede mejorar la reasociación durante cruces u oclusiones. A cambio, introduce cómputo, parámetros entrenados y sensibilidad al dominio visual (Wojke et al., 2017). Los métodos puramente geométricos reducen esas dependencias, pero son más frágiles cuando varias personas ocupan posiciones cercanas o desaparecen por intervalos prolongados. Ningún mecanismo recupera información que el detector nunca observó. Esto implica que falsos negativos, cajas inestables y detecciones espurias pueden fragmentar trayectorias o producir cambios de identificador.

Por ello, el aporte del tracker debe interpretarse como organización temporal de evidencia, no como corrección semántica automática. La evaluación del seguimiento distingue localización, asociación y continuidad; la evaluación de una alerta agrega otras decisiones —persistencia mínima, reglas de estado y tratamiento de episodios— que pertenecen al protocolo experimental. Esta separación evita trasladar métricas MOT a la plataforma completa cuando no existen anotaciones ni objetivos específicos para ese problema.

#### 16.4.3. Integración conceptual entre OVD y MOT

Un detector OVD produce cajas, etiquetas abiertas y puntajes condicionados por el prompt, donde un tracker opera principalmente sobre geometría, movimiento y continuidad temporal. La identidad de seguimiento es, por lo tanto, un identificador interno y efímero dentro de un flujo, no una identidad personal ni un mecanismo de reconocimiento. Esta separación permite agregar evidencia por entidad a lo largo de una secuencia sin atribuir nombre o identidad civil a la persona observada.

La integración básica encadena percepción y asociación. Las detecciones de cada cuadro alimentan al tracker, que actualiza trayectorias, sobre las cuales pueden agregarse puntajes, evaluar persistencia y reconocer cambios de estado. El tracker aporta continuidad, pero no resuelve por sí mismo la incertidumbre semántica. Si la etiqueta o el puntaje del detector fluctúan, el sistema necesita una regla separada de agregación temporal para decidir qué evidencia conserva y durante cuánto tiempo.

La literatura muestra que el seguimiento puede reducir la sensibilidad a detecciones aisladas y sostener evidencia durante omisiones breves, aunque su calidad continúa limitada por la estabilidad del detector y por las oclusiones (S. Li et al., 2023, 2025). Una asociación geométricamente correcta no implica que la condición semántica esté bien interpretada. De manera inversa, una detección semánticamente correcta puede asignarse a una trayectoria equivocada. Esta distinción justifica evaluar percepción y persistencia como niveles relacionados pero no equivalentes.

Los métodos sin apariencia reducen dependencias de entrenamiento, mientras que los métodos con ReID pueden mejorar la reasociación a costa de modelos y datos adicionales (Adžemović, 2025; Wojke et al., 2017).

### 16.5. Operación en tiempo real, transmisión y procesamiento cercano a la fuente

Un sistema de percepción puede ser preciso y, aun así, resultar operativamente inadecuado si la evidencia llega después del margen disponible para interpretarla. La latencia es una propiedad acumulativa del pipeline completo y no del modelo o del protocolo por separado.

#### 16.5.1. La latencia extremo a extremo como restricción de diseño

En sistemas de video analítico, la expresión latencia extremo a extremo sólo resulta interpretable cuando se declara el punto inicial y el punto final. *Glass-to-Glass* (G2G) abarca desde la captura hasta la presentación del contenido en una interfaz. *Glass-to-Algorithm* (G2A) termina cuando el resultado algorítmico asociado a un cuadro queda disponible (Axis Communications AB, 2015; Bachhuber et al., 2018). En una plataforma de alertas, G2A caracteriza un subtramo instrumental por cuadro, donde no incluye por sí solo la asociación temporal, la ventana necesaria para confirmar una condición, el registro de la alerta ni su distribución.

La percepción humana aporta una referencia, no una cota universal. Retardos alrededor de 100 ms comienzan a afectar la sensación de inmediatez en tareas interactivas, y diferencias de decenas de milisegundos pueden percibirse en tareas de manipulación directa (Card et al., 2008; Deber et al., 2015). Un sistema de supervisión puede admitir presupuestos mayores según el perfil temporal del riesgo, el tipo de intervención y el papel del operador. La magnitud admisible debe fijarse en el protocolo experimental y relacionarse con la condición evaluada.

La latencia total es acumulativa. Captura, suministro de la fuente, transformaciones, copias de memoria e inferencia aportan retardos de naturaleza diferente. Optimizar un componente no garantiza una reducción equivalente del total si otro domina la ruta crítica. Además, una tasa media compatible con tiempo real puede ocultar colas crecientes o episodios de saturación; por eso la medición debe considerar percentiles, backlog y comportamiento sostenido, no sólo el promedio.

El buffering ilustra el compromiso central. Una cola o jitter buffer absorbe variaciones y desacopla ritmos entre productor y consumidor, pero cada unidad retenida incrementa el retardo. Es por esto que el diseño debe presupuestar los buffers y declarar sus políticas, ya que eliminarlos indiscriminadamente puede producir pérdidas e inestabilidad, mientras sobredimensionarlos convierte un déficit de throughput en latencia acumulada (Axis Communications AB, 2015; Gettys & Nichols, 2012).

#### 16.5.2. Descomposición instrumental de Glass-to-Algorithm

Para mantener una notación consistente con el protocolo experimental, el subtramo G2A se descompone en cuatro componentes observables:

⟦ECUACIÓN: no extraída — ver el .docx⟧   (1)

*t_capture* representa la adquisición o lectura del cuadro hasta su disponibilidad para el host o consumidor instrumentado. *t_transport* comprende el suministro efectivo de la fuente —red, stream o lectura local—, incluidos los buffers y operaciones de entrada/salida que correspondan. *t_preprocess* agrupa decodificación cuando aplique, conversión de formato, redimensionado, normalización y transferencias de memoria. *t_inference* mide la ejecución del modelo hasta producir su salida algorítmica. La separación evita introducir renderizado o notificación en una métrica que termina antes de la interfaz (Bachhuber et al., 2018; H. Wang et al., 2022).

La Tabla 11 sintetiza los cuatro componentes instrumentales y los criterios necesarios para interpretar cada uno.

**Tabla 11**

*Componentes instrumentales del subtramo Glass-to-Algorithm*

| **Componente** | **Definición operativa** | **Fuentes principales de variabilidad** | **Criterio de interpretación** |
| --- | --- | --- | --- |
| *t_capture* | Captura, lectura o *dequeue* del cuadro en el punto temporal definido por la instrumentación | Período de cuadro, exposición, ISP y buffering de la fuente | Debe declararse el origen exacto del *timestamp*; a 30 fps, un período de cuadro es ≈33,3 ms |
| *t_transport* | Entrega del cuadro desde la fuente al consumidor del pipeline, por red, stream o I/O local | Jitter, colas, pérdida, retransmisiones, buffers y ritmo de lectura | La cola y los percentiles describen mejor la estabilidad que la media aislada |
| *t_preprocess* | Preparación de la entrada del modelo | Decodificación, formato de píxel, resize, normalización y movimiento CPU–GPU | Debe medirse por configuración porque las copias de memoria pueden dominar en pipelines acelerados |
| *t_inference* | Ejecución del modelo hasta obtener detecciones o resultados equivalentes | Arquitectura, resolución, vocabulario, runtime y hardware | La literatura reporta órdenes de 10–30 ms para alternativas one-stage optimizadas y 50–150 ms para Transformers sin optimización equivalente |

***Nota.*** Los rangos son referencias contextuales y no garantías. G2A no equivale a latencia de alerta: el seguimiento, el razonamiento, la ventana de persistencia y la distribución pertenecen a tramos posteriores. Fuente: elaboración propia basada en Axis Communications AB (2015), Bachhuber et al. (2018), Cheng et al. (2024), H. Wang et al. (2022) y Ren, Jiang, et al. (2024).

La captura está condicionada por el ritmo de origen. A 30 fps, el período entre cuadros es de aproximadamente 33,3 ms, aunque el punto de observación puede encontrarse después de exposición, procesamiento interno o buffers de cámara. Por ello, “captura” no debe suponerse equivalente al instante físico en que la luz alcanza el sensor.

El transporte es el componente más expuesto a variación externa. Propagación y procesamiento de red suelen ser relativamente estables, mientras que el encolado, el jitter y las retransmisiones dependen de la carga. En una fuente local, el término sigue existiendo como costo de lectura, demultiplexado o buffering. Lo que compromete el tiempo real no es sólo un valor medio elevado, sino una cola que crece porque el consumidor procesa por debajo del ritmo de entrada. Percentiles y ocupación de cola permiten distinguir un episodio aislado de un déficit sostenido (Gettys & Nichols, 2012; Kurose & Ross, 2021).

El preprocesamiento debe incluir todas las transformaciones efectivamente ejecutadas antes del modelo. La decodificación, la conversión de color, el redimensionado, la normalización y las transferencias CPU–GPU pueden constituir una fracción relevante, especialmente cuando se introducen copias intermedias. Agruparlas bajo un término explícito evita atribuir a la inferencia demoras que pertenecen a la preparación de datos.

La inferencia depende de arquitectura, resolución, número de consultas, runtime y hardware. Los rangos publicados para alternativas one-stage optimizadas y Transformers no optimizados son órdenes de magnitud obtenidos en configuraciones heterogéneas, por lo que no deben trasladarse como predicción. La medición por componentes permite identificar si una configuración está limitada por el modelo, por la fuente o por el movimiento de datos, y separa el costo por cuadro de la confirmación temporal de una alerta.

Los límites deben ser observables y utilizar un dominio temporal coherente. Cuando el origen no expone el instante físico de captura, *t_capture* comienza en el punto más temprano que la aplicación puede medir y esa convención debe declararse. Los timestamps de CPU y acelerador tampoco son intercambiables sin sincronización: una operación asíncrona puede parecer concluida antes de que el dispositivo haya terminado el trabajo. Por ello, los límites de *t_preprocess* y *t_inference* deben definirse con las barreras o sincronizaciones que correspondan al runtime (H. Wang et al., 2022). En este trabajo la instrumentación fija ese punto en el retiro de la unidad por parte del consumidor, de modo que el tramo anterior, desde la captura hasta la disponibilidad en el host, se mide y se informa por separado.

La ecuación expresa el recorrido temporal de una unidad, pero no implica que la tasa de procesamiento sea el inverso de esa latencia. En un pipeline, distintas etapas pueden solaparse. Por ejemplo, mientras un cuadro se infiere, otro puede estar siendo capturado o preparado. El throughput describe cuántas unidades se completan por unidad de tiempo, mientras que la latencia describe cuánto tarda una unidad desde su origen hasta su salida. Para localizar cuellos de botella deben medirse ambos y evitarse sumas de promedios obtenidos sobre corridas o poblaciones diferentes (Bachhuber et al., 2018; Bass et al., 2022).

Un reporte reproducible debe declarar período de calentamiento, tamaño de lote, resolución, vocabulario o número de consultas, precisión numérica, runtime, fuente de video y política de colas. Además del tamaño muestral y la tendencia central, conviene informar percentiles de latencia, cuadros descartados, ocupación máxima de cola y throughput sostenido. Estas variables permiten distinguir la variación ocasional de saturación sistemática y vincular el resultado global con el componente que la produce (Gettys & Nichols, 2012).

#### 16.5.3. Separación de planos y flujo productor-consumidor

En sistemas de análisis continuo resulta útil distinguir una ruta de datos —captura, transformación e inferencia— de una ruta de control que administra configuración, eventos y coordinación. La separación deriva de patrones de planos de datos y control y permite optimizar el flujo continuo sin bloquearlo con operaciones discretas de gobierno o notificación (Kreutz et al., 2015). No prescribe una distribución física ni una tecnología particular, lo que implica que ambos planos pueden coexistir en un host o distribuirse cuando el diseño lo justifique.

La ruta de datos prioriza throughput sostenido, latencia acotada y un orden definido de transformaciones. La ruta de control procesa comandos, cambios de configuración y eventos a ritmos no necesariamente ligados a la tasa de cuadros. Mantener responsabilidades diferenciadas facilita aislar cuellos de botella y evita que una operación de registro o notificación bloquee la recepción del siguiente cuadro (Bass et al., 2022).

La ruta crítica puede modelarse como una cadena productor-consumidor. Cada etapa produce unidades que la siguiente consume, y cuando el productor supera sostenidamente la capacidad del consumidor, una cola sin límite convierte el déficit de throughput en latencia creciente. Las colas acotadas, la contrapresión y las políticas explícitas de descarte, muestreo o sustitución permiten mantener el sistema observable. La política adecuada depende de la semántica: conservar todas las unidades puede ser necesario para relectura reproducible, mientras que una ruta viva puede priorizar evidencia reciente para evitar procesar cuadros obsoletos.

El desacoplamiento no elimina la necesidad de medir. Deben observarse ritmo de producción, ritmo de consumo, ocupación de cola, unidades descartadas y tiempo de residencia. Un sistema que reporta FPS aceptables pero acumula backlog no opera en tiempo real; simplemente procesa con retraso.

Para eventos discretos, el patrón publish/subscribe separa productores y consumidores: el emisor publica sin conocer todos los destinos y cada suscriptor procesa los tipos de evento pertinentes. Conviene distinguir tres responsabilidades: el transporte en ejecución entrega eventos a consumidores activos, la persistencia conserva hechos para relectura o auditoría y la distribución externa comunica una alerta. Un bus puede desacoplar componentes, pero no garantiza por sí mismo que los eventos sobrevivan a una desconexión, ya que la durabilidad requiere un repositorio o una política de retención independiente de la mensajería en vivo (Cugola & Margara, 2012).

Las garantías de entrega también forman parte del contrato conceptual. Una entrega al menos una vez puede producir reenvíos y, por lo tanto, duplicados, mientras que una entrega como máximo una vez puede perder mensajes y exactamente una vez exige coordinación adicional. Cuando una alerta no debe producir efectos repetidos, el evento necesita una identidad estable y el consumidor debe procesarlo de manera idempotente. MQTT QoS 1 ejemplifica la primera semántica mediante confirmación, sin convertirla en una garantía de ausencia de duplicados (OASIS, 2019).

#### 16.5.4. Computación en el borde y filtrado cercano al origen

La literatura utiliza edge, fog y *cloud* con fronteras variables. En este trabajo, edge designa cómputo en el dispositivo, gateway inmediato o servidor próximo a la fuente, fog una capa intermedia de agregación cercana o regional y cloud centros de datos centralizados (Iorga et al., 2018; Yousefpour et al., 2019). La convención permite describir tres patrones: procesamiento en el dispositivo, procesamiento en un nodo cercano y partición colaborativa entre niveles (Chen & Ran, 2019).

Acercar cómputo al origen puede reducir ida y vuelta de red, ancho de banda y exposición de video crudo, pero introduce límites de memoria, energía y temperatura (Satyanarayanan, 2017; Shi et al., 2016). La nube ofrece elasticidad y recursos centralizados, aunque depende de conectividad y amplía el recorrido del dato. Una capa fog puede agregar varias fuentes, aplicar políticas o resumir información antes de enviarla a niveles superiores. Ningún nivel es intrínsecamente superior y su conveniencia depende del tramo que se desplace y de la carga sostenida.

No toda operación cercana al sensor equivale a inferencia completa en el borde. Una cámara inteligente puede ejecutar adquisición, filtrado, selección de cuadros, conversión o preprocesamiento y enviar sólo las unidades necesarias al consumidor principal. Este reparto reduce el consumo aguas abajo sin atribuir al dispositivo capacidades de detección que no ejecuta. La distinción es importante para analizar gateways y cámaras programables sin confundir prefiltrado con despliegue integral del modelo.

En video analytics, filtrar o resumir cerca del origen disminuye tráfico y carga posterior. Ananthanarayanan et al. (2017) muestran que procesar cerca de las cámaras permite reducir el ancho de banda y distribuir recursos en cargas de video a escala. En un prototipo, el mismo principio puede evaluarse de forma acotada, midiendo cuánto trabajo se ejecuta antes del host, qué evidencia se descarta y qué impacto tiene esa decisión sobre calidad y latencia.

El punto de partición debe evaluarse por latencia, throughput, privacidad, capacidad sostenida y reproducibilidad. Métricas nominales como TOPS no bastan para anticipar el comportamiento de una aplicación. Bajo carga prolongada, límites térmicos, memoria compartida y variaciones del runtime pueden degradar el ritmo; por ello, los percentiles de latencia, el uso de memoria, el throughput efectivo y los eventos de saturación resultan más informativos que un máximo instantáneo (Satyanarayanan, 2017; Shi et al., 2016). La decisión de ejecutar inferencia en el borde, en un host cercano o en infraestructura remota debe mantenerse separada de la decisión de filtrar cerca del origen.

El filtrado cercano al origen introduce, a su vez, un compromiso metodológico. Seleccionar cuadros, reducir resolución, limitar regiones o descartar unidades disminuye carga y ancho de banda, pero modifica la evidencia que recibe el detector y puede afectar la continuidad temporal. Por ello, la política de prefiltrado debe declararse junto con la fuente y conservar parámetros suficientes para reproducirla.

Desplazar procesamiento hacia la fuente puede reducir la transmisión de video crudo, pero no elimina por sí mismo el tratamiento de datos personales. Metadatos temporales, zonas, trayectorias y recortes pueden mantener capacidad de identificación indirecta, por lo que la minimización debe evaluarse sobre el conjunto de datos producido y no únicamente sobre la ubicación física del cómputo (European Data Protection Board, 2020).

#### 16.5.5. Brecha de evaluación integrada

Las fuentes principales de investigación caracterizan por separado protocolos, códecs, hardware y modelos de inferencia, pero no ofrecen un marco universal para presupuestar la latencia extremo a extremo de un pipeline que integra detección open-vocabulary. Los resultados aislados sólo funcionan como referencias externas; la adecuación debe verificarse mediante instrumentación del sistema completo y una definición explícita del tramo medido. Esta brecha se corresponde con la identificada en la sección 15.4.3.1 y fundamenta la necesidad de un protocolo reproducible sin anticipar la selección del stack.

### 16.6. Marco ético-legal para el análisis automatizado de video en entornos laborales

El análisis automatizado de video en entornos laborales introduce restricciones que exceden el desempeño técnico del sistema. Las imágenes pueden constituir datos personales y las salidas de un modelo de inteligencia artificial pueden influir en la evaluación de situaciones que involucran a trabajadores. Por ello, el marco ético-legal se concentra en las condiciones de contorno relevantes para un uso preventivo y asistivo: finalidad determinada, minimización de datos, seguridad, transparencia, ausencia de identificación biométrica, supervisión humana y trazabilidad. Estos principios delimitan el tratamiento de la información y la interpretación de las alertas, sin convertir una observación visual en una determinación normativa sobre una persona (Organisation for Economic Co-operation and Development, 2019; UNESCO, 2021).

#### 16.6.1. Protección de datos y finalidad del tratamiento

En Argentina, la Ley 25.326 considera dato personal a la información referida a personas determinadas o determinables. En consecuencia, un flujo de video puede quedar comprendido en el régimen de protección de datos aun cuando el análisis no utilice reconocimiento facial: la imagen y su combinación con elementos contextuales —como tiempo, ubicación o secuencia de observaciones— pueden permitir una identificación directa o indirecta (Agencia de Acceso a la Información Pública, s. f.-a; Argentina, 2000).

La finalidad preventiva no elimina estas exigencias. La recolección y el uso de imágenes deben responder a un propósito definido y conservar una relación de proporcionalidad con él, evitando datos o usos que resulten innecesarios para la función declarada. En materia de videovigilancia, la Disposición 10/2015 aplica estos principios mediante pautas de información al titular, definición de responsabilidades y documentación de las condiciones de tratamiento, acceso, seguridad y conservación (Argentina, 2000, 2015). De este modo, la captación de video se entiende como un tratamiento delimitado y no como una fuente de información reutilizable sin restricciones para finalidades distintas.

#### 16.6.2. Minimización, seguridad y exclusión de identificación personal

La minimización debe evaluarse sobre el conjunto de información que produce el sistema y no únicamente sobre el video original. Recortes de imagen, marcas temporales, zonas, trayectorias internas, alertas y registros pueden conservar capacidad de identificación indirecta o ampliar el alcance del tratamiento. Por ello, la captación, la persistencia y la conservación de evidencias deben limitarse a aquello que resulte necesario para la finalidad preventiva, con criterios explícitos de retención y eliminación (Argentina, 2000; European Data Protection Board, 2020).

La protección de la información exige, además, medidas técnicas y organizativas proporcionales al riesgo del tratamiento. Para este marco resulta suficiente retener que el acceso a imágenes y registros debe estar restringido, su almacenamiento y transmisión deben protegerse frente a usos no autorizados y la conservación no debe extenderse indefinidamente sin una finalidad que la justifique (Argentina, 2006; European Data Protection Board, 2020). La selección concreta de controles no modifica el principio general de reducir exposición y superficie de acceso.

Debe distinguirse también entre el tratamiento de imágenes y la identificación biométrica. Una imagen puede constituir un dato personal sin que exista reconocimiento facial. El tratamiento adquiere carácter biométrico cuando se procesan características físicas o fisiológicas con el propósito de identificar de manera unívoca a una persona (European Data Protection Board, 2020). En consecuencia, la detección de personas, elementos de protección o condiciones observables, así como el uso de identificadores temporales internos para mantener continuidad dentro de una secuencia, no requieren atribuir identidad civil ni incorporar mecanismos de reconocimiento personal.

#### 16.6.3. Supervisión humana, trazabilidad y alcance asistivo

Los marcos de gobernanza de inteligencia artificial enfatizan la supervisión humana, la rendición de cuentas y la comunicación comprensible de las limitaciones del sistema. En un contexto de seguridad laboral, una alerta algorítmica debe interpretarse como evidencia para revisión y no como una decisión autónoma sobre cumplimiento, conducta o responsabilidad de una persona. La incertidumbre, los falsos positivos y los falsos negativos forman parte de las limitaciones que deben permanecer visibles para quien utiliza la salida del sistema (ISO, 2023; Organisation for Economic Co-operation and Development, 2019; UNESCO, 2021).

La trazabilidad complementa ese carácter asistivo. Versiones de modelos y configuraciones, criterios de inferencia y registros suficientes para reconstruir el origen de una alerta permiten auditar resultados inesperados sin asumir que la predicción sea correcta. Así, el marco ético-legal condiciona qué información se procesa, cuánto se conserva y con qué alcance se interpreta una alerta. Estas restricciones se integran con las brechas técnicas en la sección 16.7 (ISO, 2023; Organisation for Economic Co-operation and Development, 2019).

### 16.7. Convergencias y preguntas rectoras

#### 16.7.1. Interdependencia de los dominios

La viabilidad de una plataforma de análisis asistivo no depende de un componente aislado, sino de la articulación entre los dominios desarrollados en este marco. Una condición de riesgo debe ser observable y evaluable; su formulación en lenguaje debe poder vincularse con evidencia visual; esa evidencia debe conservar continuidad suficiente para distinguir estados transitorios de condiciones sostenidas; y el procesamiento del video debe realizarse dentro de restricciones temporales explícitas. A su vez, la captura y el tratamiento de imágenes quedan sujetos a criterios de finalidad, minimización, seguridad y revisión humana. En consecuencia, calidad perceptiva, continuidad temporal, latencia y trazabilidad forman parte de una misma cadena de análisis y no pueden interpretarse como propiedades independientes (Bass et al., 2022; Cugola & Margara, 2012).

#### 16.7.2. Del marco conceptual al protocolo experimental

El marco teórico no determina una arquitectura ni una configuración concreta, pero sí delimita las decisiones que el protocolo experimental debe volver evaluables. Esto comprende definir qué condiciones integran el núcleo de análisis y cómo se representan, qué materiales y anotaciones permiten contrastarlas, qué restricciones de ejecución condicionan configuraciones comparables, qué niveles y métricas separan percepción, estado por entidad y alerta temporal, y bajo qué condiciones resulta pertinente explorar adaptación paramétrica. La consolidación metodológica transforma estos fundamentos en variables, criterios y comparaciones reproducibles, sin confundir una capacidad conceptual con una función implementada o un resultado medido.

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

El marco teórico sostiene la factibilidad conceptual de una plataforma asistiva que interpreta observables expresados mediante lenguaje sobre video, mantiene continuidad temporal y produce alertas trazables para revisión humana. Esta factibilidad no implica superioridad de OVD frente a detectores supervisados ni habilita conclusiones de cumplimiento desde una observación visual; depende de condiciones evaluables, del comportamiento en el dominio y de restricciones temporales explícitas.

La fundamentación delimita también qué debe resolverse empíricamente: los benchmarks generales no predicen el rendimiento en construcción; una detección por cuadro no equivale a una alerta; un identificador de seguimiento no representa identidad personal; y una capacidad de la literatura no constituye una función implementada. En un campo en evolución, estas separaciones exigen decisiones trazables y validación reproducible.

## 17. Desarrollo del producto

### 17.1. Consolidación metodológica del protocolo experimental

La consolidación metodológica transforma el marco teórico construido previamente en un protocolo experimental utilizable. Para ello fija decisiones sobre alcance, escenarios, infraestructura, datos, prompts, métricas y criterios de aceptación, integrando los desarrollos metodológicos en una secuencia coherente con el objetivo del prototipo experimental.

El referente experimental resultante delimita qué condiciones de riesgo integran el núcleo del prototipo, cómo se estructuran los escenarios de evaluación, con qué reglas se gestionan los datos, qué métricas deben producirse y cómo debe interpretarse la evidencia obtenida.

Esta instancia establece las condiciones de comparabilidad, medición e interpretación necesarias para el desarrollo del prototipo, y su posterior evaluación sobre bases explícitas y trazables.

#### 17.1.1. Función y alcance de la consolidación metodológica

El criterio rector prioriza la validez experimental, la trazabilidad y la correspondencia entre alcance, datos disponibles e instrumentación efectiva. El núcleo obligatorio del prototipo se ubica en las condiciones de Nivel 1 —CR-01 y CR-02—, donde convergen observabilidad visual, cobertura de datos, estrategias de evaluación defendibles y métricas aplicables con el hardware disponible; las condiciones de Niveles 2 y 3 se conservan como extensiones condicionadas, debido a brechas de datos, visibilidad y razonamiento contextual.

A partir de ese criterio se fija una secuencia experimental integrada —comparación primaria en *Dataset-Based Evaluation* (DBE), validación complementaria en *Environment-Based Evaluation* (EBE), reglas de partición sin *leakage*, política de formulación y congelamiento de prompts, jerarquía de métricas orientada al valor operativo de alerta y criterios para habilitar una rama comparativa de fine-tuning—, organizada sobre cuatro dimensiones temáticas: el entorno experimental, las condiciones de riesgo y su protocolo de prompts, la estrategia de datos y el framework de métricas.

#### 17.1.2. Alcance experimental consolidado del prototipo

##### 17.1.2.1. Catálogo de condiciones de riesgo y alcance de validación

El catálogo retenido comprende seis condiciones de riesgo organizadas en tres niveles de complejidad. Dentro de este catálogo, CR-01 y CR-02 constituyen el núcleo obligatorio de validación, porque son condiciones de Nivel 1 cuya relevancia preventiva, observabilidad y evaluabilidad están fundamentadas en la sección 16.2 y pueden abordarse mediante las estrategias de detección definidas para el protocolo, con cobertura de datos y métricas aplicables dentro del entorno experimental disponible.

Las condiciones restantes se conservan como extensiones condicionadas. CR-03 y CR-04 dependen de mayor visibilidad de atributos, evidencia de ausencia y datos complementarios, mientras que CR-05 y CR-06 requieren persistencia temporal, relaciones espaciales o regiones parametrizadas. Estas exigencias incrementan la dependencia de información contextual y de capacidades adicionales del pipeline, en concordancia con las dificultades documentadas para los modelos OVD ante atributos finos y dominios especializados de construcción (Bianchi et al., 2024; Abdalwhab et al., 2025). En consecuencia, la validación del prototipo no exige un desempeño uniforme sobre las seis condiciones, sino que la evidencia necesaria para sostener el alcance experimental se concentra en el núcleo obligatorio, mientras que las restantes condiciones conservan valor como extensiones del catálogo.

La definición completa, con el tipo de condición, el componente evaluador y la dificultad estimada, se presenta en la Tabla 14.

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

**Tabla 12**

*Decisiones estructurales del diseño metodológico*

| **Decisión** | **Formulación adoptada** | **Implicación para el protocolo** |
| --- | --- | --- |
| Unidad de análisis | Patrón de riesgo confirmado y alerta asociada, no detección aislada. | Obliga a medir persistencia, tiempo de respuesta y estabilidad además de precisión de detección. |
| Cadena operativa mínima | Detección OVD, evento de detección, evaluación de patrón, patrón confirmado, alerta registrada, disponibilidad para consulta o notificación, e interpretación humana. | Conecta la evidencia perceptiva con una salida operativa trazable y evita tratar la alerta como una detección aislada. |
| Motor de patrones | Abstracción lógica del plano de control que evalúa eventos de detección, trayectorias cuando existan y configuración de patrones contra reglas de persistencia, severidad, histéresis y lógica espacial o contextual. | Define dónde se transforma la evidencia perceptiva en patrón candidato, confirmado o resuelto, y evita tratar la alerta como salida directa del detector OVD. |
| Carácter asistivo de la alerta | La alerta informa un patrón de riesgo confirmado según los criterios operativos del prototipo, pero no sustituye la decisión del supervisor humano. | Preserva el alcance experimental, ético y operativo del prototipo. |
| Escenario primario | DBE sobre datasets y benchmarks retenidos. | Asegura comparabilidad, control de variables y repetibilidad de las mediciones. |
| Escenario complementario | EBE en entorno simulado o controlado. | Permite observar el comportamiento del pipeline sobre captura continua y variables visuales realistas. |
| *Baseline* obligatoria | Toda variante se mide primero en zero-shot. | Protege la comparación entre modelos y evita atribuir al ajuste mejoras que dependen de cambios de evaluación. |
| Comparación entre variantes | Fine-tuning sólo cuando existe soporte metodológico suficiente. | Evita convertir la adaptación al dominio en supuesto previo de viabilidad. |

***Nota.*** DBE = Dataset-Based Evaluation. EBE = Environment-Based Evaluation. La baseline zero-shot constituye la referencia mínima a partir de la cual recién puede discutirse el valor de prompts, seguimiento o fine-tuning. La cadena operativa mínima fija el recorrido lógico de la alerta dentro del protocolo experimental. El motor de patrones explicita el componente lógico que transforma evidencia perceptiva en patrón confirmado y opera como criterio de diseño para su instrumentación arquitectónica posterior.

#### 17.1.4. Entorno experimental, infraestructura y escenarios de evaluación

El entorno experimental delimita las condiciones materiales y operativas bajo las cuales se aplica el protocolo. Su caracterización responde a la pregunta rectora P-E1-04 y vincula la capacidad de cómputo disponible, la forma de adquisición y transporte del video y el presupuesto temporal de procesamiento. Sobre esa base se distinguen los roles de ejecución y dos escenarios complementarios de evaluación, de modo que las mediciones de desempeño puedan interpretarse respecto del entorno en el que fueron obtenidas.

##### 17.1.4.1. Infraestructura y roles de ejecución

La infraestructura se organiza mediante tres roles funcionales, sin imponer que cada uno corresponda a un dispositivo físico exclusivo. El *Central Processing Node* (CPN) constituye la referencia para la inferencia open-vocabulary, el postproceso, la evaluación de patrones y la instrumentación de rendimiento; por ello, las conclusiones sobre viabilidad temporal y uso de recursos se anclan en este nodo. El rol se materializa sobre una laptop HP Victus 15 Gaming 15-FB2024LA con una GPU NVIDIA GeForce RTX 4060 Laptop de 8 GB de VRAM y entorno Linux mediante WSL2, combinación que condiciona el tamaño de los modelos ejecutables, la resolución de inferencia, la precisión numérica y la selección del runtime (HP Inc., s. f.). El stack debe conservar compatibilidad con los frameworks oficiales de Grounding DINO y YOLOE y permitir rutas reproducibles de inferencia acelerada (Liu et al., 2024; Wang et al., 2025).

El *Edge Node* (EN) representa la adquisición próxima a la fuente visual. El protocolo contempla una cámara IP mediante RTSP y una Luxonis OAK-D Pro PoE mediante su interfaz de captura; en ambos casos, el flujo base mantiene la inferencia OVD en el CPN y reserva el borde para captura, transmisión y, cuando corresponda, preprocesamiento liviano (Luxonis, s. f.-a, s. f.-b). Para flujos H.264 o H.265, la decodificación acelerada mediante NVDEC se conserva como alternativa declarable por corrida, ya que su uso modifica el reparto de carga entre CPU y GPU y, con ello, la interpretación del presupuesto temporal (NVIDIA Corporation, s. f.-b). Independientemente de la fuente, cada corrida debe registrar procedencia, resolución, tasa de captura y referencias temporales suficientes para interpretar las mediciones.

El *Training Node* (TN) se reserva para la preparación de variantes ajustadas y queda fuera del camino de inferencia evaluado. Se materializa mediante el clúster institucional Mendieta del CCAD-UNC y debe permitir preparación de datos, entrenamiento reproducible, conservación de checkpoints y exportación hacia el CPN (Centro de Computación de Alto Desempeño, 2026). La decisión de habilitar una rama de adaptación al dominio y sus condiciones de comparación se establecen en la sección 17.1.9, mientras que en este apartado sólo se fija la separación entre el entorno de preparación del modelo y el entorno sobre el que se juzga su comportamiento operativo.

El detalle técnico de los recursos de cómputo y captura, los entornos de software y los parámetros de referencia del entorno experimental se consolida en el Anexo B.

##### 17.1.4.2. Escenarios de evaluación

La evaluación se estructura en dos escenarios complementarios. El Dataset-Based Evaluation (DBE) constituye el ámbito primario de comparación controlada y reproducible: procesa imágenes o secuencias de video provenientes de datasets anotados y permite aislar variables, repetir una configuración sobre la misma entrada y, cuando los protocolos sean compatibles, contrastar los resultados con referencias externas. El Environment-Based Evaluation (EBE) incorpora captura continua en un entorno físico controlado y ejercita la cadena desde la adquisición del video hasta la evaluación temporal de patrones, introduciendo variables visuales y de conectividad que no pueden representarse completamente mediante archivos.

La relación entre ambos escenarios no es de reemplazo. El DBE sostiene la comparabilidad entre configuraciones y la evaluación cuantitativa bajo entradas congeladas; el EBE aporta evidencia de plausibilidad operativa al someter la plataforma a temporalidad continua, iluminación, oclusiones, escala y transporte de video. En ambos casos, el CPN mantiene el rol de referencia para la inferencia y la evaluación, mientras que el EN participa en el EBE como fuente de captura. Si una variante ajustada es habilitada conforme a la sección 17.1.9, debe compararse contra la baseline bajo material y configuración equivalentes, aislando la adaptación como variable experimental. Las variables de sensibilidad candidatas para el EBE se consolidan en la Tabla C.2 del Anexo C.

**Tabla 13**

*Comparación de los escenarios de evaluación DBE y EBE*

| **Aspecto** | **DBE** | **EBE** |
| --- | --- | --- |
| Entrada y temporalidad | Imágenes y secuencias de video provenientes de datasets anotados. Procesamiento sobre archivos con entrada reproducible. | Video en vivo desde el EN mediante RTSP o captura directa con OAK-D Pro PoE. Temporalidad continua. |
| Propósito metodológico | Comparación controlada de configuraciones, aislamiento de variables y repetibilidad de las mediciones. | Validación de plausibilidad operativa del pipeline integrado bajo condiciones visuales y de conectividad representativas. |
| Distribución funcional | CPN para inferencia y evaluación. No requiere transporte de video en vivo. | EN para captura y CPN para inferencia y evaluación. El transporte y sus referencias temporales forman parte de la instrumentación. |
| Variables dominantes | Modelo, prompt, dataset, partición, resolución y umbrales declarados. | Fuente de captura, iluminación, oclusión, escala, densidad de escena, transporte y buffering, además de la configuración del modelo. |
| Limitación principal | La reproducibilidad no elimina la brecha entre datasets y condiciones reales de operación. | La variabilidad del entorno reduce la reproducibilidad y exige documentar las condiciones de captura y ejecución. |

***Nota.*** DBE = Dataset-Based Evaluation. EBE = Environment-Based Evaluation. La tabla sintetiza las diferencias metodológicas entre ambos escenarios; la estrategia de datos, el framework de métricas y las condiciones de adaptación al dominio se desarrollan en sus secciones específicas.

#### 17.1.5. Condiciones de riesgo, patrones y protocolo de prompts

La definición de las condiciones de riesgo, de los patrones asociados y de las consultas textuales que los buscan responde a la pregunta rectora P-E1-02 y transforma las condiciones preventivamente relevantes en unidades evaluables por la plataforma. El protocolo establece el catálogo experimental, los criterios temporales y contextuales que permiten confirmar un patrón y las reglas para diseñar, comparar y congelar los prompts OVD antes de la evaluación.

##### 17.1.5.1. Catálogo de condiciones de riesgo y evaluabilidad

La fundamentación teórica delimita las condiciones de riesgo observables por su relevancia preventiva, su evidencia visual anotable y su formulación evaluable (sección 16.2), y señala como posibles extensiones situaciones como el trabajo en altura, las zonas restringidas o la interacción con maquinaria. El prototipo experimental no pretende cubrir ese espacio de manera exhaustiva y selecciona un subconjunto acotado con tres criterios.

El primero es la **representatividad**, de modo que el catálogo incluya al menos una condición de cada nivel de complejidad y la evaluación ejercite las distintas capacidades del pipeline. El segundo es la **factibilidad de detección visual**, que exige correlatos visuales suficientemente diferenciados para resolverse mediante análisis de imagen en las resoluciones y ángulos de cámara típicos de un entorno de laboratorio o simulado. Quedan fuera las condiciones cuya manifestación depende de detalles de difícil resolución, como la distinción entre calzado de seguridad y calzado común o la presencia de guantes y gafas de protección, y las que carecen de correlato visual directo, como una capacitación insuficiente. También quedan fuera, aunque son preventivamente relevantes, condiciones de escena como la obstrucción de pasillos o la presencia de materiales inestables, que no admiten una definición visual estable para su anotación. El tercero es la **viabilidad de evaluación** con los recursos disponibles, de manera que cada condición pueda medirse con datasets públicos, con subconjuntos anotados de ellos o con material generado en entorno controlado, sin campañas de recolección incompatibles con un proyecto académico.

Las condiciones seleccionadas se clasifican en tres niveles según las capacidades que el sistema debe desplegar para evaluarlas, una distinción con consecuencias directas sobre la arquitectura del pipeline y sobre el protocolo aplicable a cada una. Las condiciones de Nivel 1 involucran una entidad simple o un atributo observable sobre ella, resoluble en principio con una consulta OVD sobre un cuadro individual, sin información temporal ni relacional. La detección de casco sobre una persona es el caso representativo, y la evaluación de la condición asociada admite las dos estrategias que se definen en la sección 17.1.5.3. Las condiciones de Nivel 2 agregan un atributo contextual que depende de la relación espacial entre la entidad y su entorno inmediato dentro del mismo cuadro, como la persona sobre un andamio. El detector puede localizar a la persona y a la estructura por separado, pero determinar que una está sobre la otra exige reglas geométricas de solapamiento o de posición relativa entre las detecciones, sin requerir todavía persistencia temporal ni mantenimiento de identidad. Las condiciones de Nivel 3 involucran dos o más entidades independientes cuya co-ocurrencia espacial o temporal constituye el riesgo, como la maquinaria pesada próxima a un peatón. Exceden la capacidad del detector cuadro a cuadro, porque requieren un módulo que evalúe relaciones geométricas entre entidades y las estabilice en el tiempo, y en ese nivel interviene el tracker MOT para preservar la identidad de cada objeto durante el intervalo de evaluación.

La Tabla 14 presenta las seis condiciones seleccionadas organizadas por nivel, con su código, el tipo de condición, la evidencia visual esperada, el componente del sistema responsable de su evaluación y una estimación cualitativa de la dificultad de detección OVD.

**Tabla 14**

*Catálogo de condiciones de riesgo seleccionadas para el prototipo experimental*

| **Código** | **Nivel** | **Tipo de condición** | **Condición de riesgo** | **Evidencia visual** | **Componente evaluador** | **Dificultad OVD estimada** |
| --- | --- | --- | --- | --- | --- | --- |
| CR-01 | 1 | EPP — casco | Persona sin casco de seguridad en zona de obra | Presencia o ausencia de casco en región cefálica de la persona | OVD cuadro a cuadro | Media |
| CR-02 | 1 | EPP — chaleco | Persona sin chaleco reflectivo en zona de tráfico o maquinaria | Presencia o ausencia de prenda de alta visibilidad en torso | OVD cuadro a cuadro | Media-Baja |
| CR-03 | 2 | Protección contra caídas | Persona en posición elevada sin sistema anticaídas visible | Persona sobre andamio o plataforma sin arnés o línea de vida visible | OVD + contexto espacial intracuadro | Alta |
| CR-04 | 2 | Protección contra caídas | Borde elevado desprotegido con personas próximas | Borde de plataforma o losa sin baranda o red perimetral, con presencia humana | OVD + contexto espacial intracuadro | Alta |
| CR-05 | 3 | Coexistencia peatón-maquinaria | Maquinaria en operación en proximidad a peatones sin separación | Co-ocurrencia de maquinaria pesada y personas por debajo de distancia de seguridad | OVD + MOT + razonamiento contextual | Media |
| CR-06 | 3 | Delimitación de áreas | Persona dentro de zona restringida o delimitada | Presencia de persona en área demarcada como prohibida o restringida | OVD + MOT + razonamiento contextual | Media |

***Nota.*** “Componente evaluador” indica qué módulos participan en la evaluación. “OVD cuadro a cuadro” (una o más consultas al detector por cuadro), “OVD + contexto espacial intracuadro” (relaciones geométricas entre detecciones del mismo cuadro) y “OVD + MOT + razonamiento contextual” (persistencia temporal de trayectorias y lógica relacional). “Dificultad OVD estimada” es una valoración cualitativa basada en la degradación documentada de los modelos OVD ante atributos de granularidad fina, en la discrepancia de distribución y vocabulario en dominios especializados y en el menor desempeño frente a detectores ajustados en entornos de construcción (Bianchi et al., 2024; Jiang et al., 2024; Abdalwhab et al., 2025). No se pondera la dificultad del razonamiento contextual.

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

La Tabla 15 consolida el catálogo de patrones asociados a las condiciones seleccionadas, con su severidad, el rango orientativo de persistencia, el criterio de activación, el perfil temporal que fundamenta la severidad asignada y el riesgo de falsos positivos asociado a la brevedad de la ventana.

**Tabla 15**

*Catálogo de patrones de riesgo del prototipo E-OVRT-VDP*

| **Patrón** | **Cond.** | **Severidad** | **Persistencia** | **Criterio de activación** | **Perfil temporal de la condición** | **Trade-off FP** |
| --- | --- | --- | --- | --- | --- | --- |
| PR-01 | CR-01 | Alto | 3–5 s | Persona detectada sin casco durante el intervalo mínimo | Exposición sostenida a caída de objetos o impactos en zona activa de obra; incidente posible ante evento desencadenante. | Moderado |
| PR-02 | CR-02 | Medio | 5–10 s | Persona detectada sin chaleco o indumentaria de alta visibilidad en zona de circulación durante el intervalo | Riesgo de atropello o interferencia operacional por baja visibilidad; escalada dependiente del movimiento efectivo de vehículos o maquinaria. | Bajo |
| PR-03 | CR-03 | Crítico | 2–4 s | Persona en posición elevada sin sistema anticaídas durante el intervalo | Caída a distinto nivel con consecuencia potencialmente fatal; requiere respuesta temprana ante exposición en altura sin protección suficiente. | Elevado |
| PR-04 | CR-04 | Crítico | 2–4 s | Persona próxima a borde desprotegido durante el intervalo | Caída a distinto nivel desde abertura, borde o plataforma sin protección colectiva eficaz. | Elevado |
| PR-05 | CR-05 | Crítico | 2–4 s | Maquinaria y peatón co-detectados por debajo del umbral de distancia mínima durante el intervalo | Atropello, aplastamiento o contacto peligroso por interacción próxima entre peatones, vehículos y maquinaria de obra. | Elevado |
| PR-06 | CR-06 | Alto | 3–5 s | Persona detectada dentro del polígono de zona restringida durante el intervalo | Exposición sostenida a riesgos propios de una zona señalizada, delimitada, de exclusión, de seguridad o de acceso restringido. | Moderado |

***Nota.*** Los rangos de persistencia temporal son orientativos. La columna “Trade-off FP” indica cualitativamente el riesgo de falsos positivos asociado a la brevedad de la ventana de persistencia. La severidad es una clasificación interna del protocolo, fundamentada en el perfil temporal de la condición. No constituye una calificación normativa de la situación observada. La relevancia preventiva de las condiciones se fundamenta en la sección 16.2. Fuente: elaboración propia.

Los patrones PR-05 y PR-06 requieren criterios de activación combinada, que se definen a nivel conceptual. Para PR-05 la activación exige la detección simultánea de al menos una entidad clasificable como maquinaria de obra, como una excavadora, una retroexcavadora, un camión volquete o una grúa, y de al menos una persona, con una relación de proximidad inferior a un umbral configurable. Toda métrica de proximidad calculada en coordenadas de imagen es una medida geométrica bidimensional aproximada y no una distancia física, porque la perspectiva de la cámara altera las distancias aparentes. La evaluación debe sostenerse durante el intervalo de persistencia del patrón, lo que exige trayectorias suficientemente estables de las entidades involucradas.

Para PR-06 la activación exige la detección de al menos una persona cuya posición representativa esté contenida en un polígono predefinido que representa la zona restringida. El polígono forma parte de la parametrización del sistema, es configurable por el operador y externo al prompt, y presupone una cámara fija, supuesto adoptado para el alcance del prototipo experimental. La permanencia debe sostenerse durante el intervalo de persistencia, lo que implica seguimiento temporal cuando la persistencia se compute por entidad individual. En ambos patrones los cambios de identidad, las pérdidas temporales de trayectoria y las reasociaciones erróneas del tracker pueden interrumpir espuriamente la evaluación o reiniciar indebidamente la ventana, por lo que deben contemplarse en el diseño del razonamiento contextual y cuantificarse en la validación experimental.

##### 17.1.5.3. Diseño de prompts OVD

Las consultas textuales operan como interfaz del modelo OVD y su formulación altera el desempeño del detector. El análisis de modelos OVD documentó que cambios leves de redacción modifican significativamente el comportamiento de los modelos visión-lenguaje (Zhou et al., 2022), que el embedding textual de clase se genera a partir de los prompts ingresados al encoder y su alineación con las representaciones visuales requiere ajuste específico para la detección (Gu et al., 2021; Du et al., 2022), y que la evaluación se vuelve especialmente exigente ante atributos de granularidad fina, vocabularios dinámicos y clases negativas semánticamente cercanas, como muestran los benchmarks FG-OVD y OVDEval (Bianchi et al., 2024; Yao et al., 2024). Por eso el protocolo trata el diseño de prompts como una variable de ingeniería del sistema, gestionada con el mismo rigor que la selección de modelos o la definición de métricas, y la resuelve mediante contraste reproducible. Dos definiciones ordenan ese contraste. La matriz de prompts es el conjunto acotado de formulaciones alternativas que se ensayan para una misma condición. La composición del vocabulario activo es el conjunto de descripciones o consultas que el modelo evalúa en simultáneo dentro de una corrida determinada.

Para cada condición del catálogo (Tabla 14) se diseñan variaciones de prompt a lo largo de cuatro ejes controlados, de modo que la selección quede documentada con evidencia reproducible. El primer eje es la estructura sintáctica, que abarca frases nominales simples, oraciones descriptivas con contexto y variaciones en el uso de artículos, preposiciones o modificadores. Para la detección de casco, por ejemplo, las formulaciones “hard hat”, “person wearing hard hat” y “safety *helmet* on worker” difieren en estructura gramatical aunque refieren a conceptos visualmente relacionados. Se incluyen además variantes con template, como “*a photo of a [CLASS]*”, porque en los modelos de la familia CLIP transformar una etiqueta aislada en una descripción breve reduce la brecha con los textos naturales del preentrenamiento y puede mejorar el desempeño (Radford et al., 2021). El protocolo compara prompts con y sin template sin presuponer cuál resultará superior en el dominio de la construcción.

El segundo eje es el nivel de especificidad del vocabulario, desde términos genéricos hasta terminología propia del dominio. Las formulaciones “person”, “worker” y “construction worker” representan grados crecientes de especificidad para la misma entidad. La hipótesis metodológica es que los términos más específicos pueden mejorar la precisión al reducir la ambigüedad de la consulta y aproximarla al contexto de obra, aunque también pueden reducir el recall si la formulación resulta demasiado restrictiva o menos compatible con las representaciones aprendidas durante el preentrenamiento. Por eso la elección entre vocabulario genérico y específico se trata como variable experimental y no como una decisión evidente.

El tercer eje es la estrategia de detección y distingue tres familias identificadas con un código. La estrategia directa (E-DIR) formula un prompt que intenta describir la condición de riesgo completa, incluida la presencia o ausencia del elemento relevante. La estrategia indirecta (E-IND) consulta entidades visibles por separado, por ejemplo “person” y “hard hat” como prompts independientes, y reconstruye la condición mediante lógica externa al modelo que asocia las detecciones y verifica sus relaciones geométricas. La estrategia híbrida (E-HYB) combina consultas de ambos tipos bajo una regla de composición explícita. La distinción no es terminológica, porque los modelos OVD permiten consultar categorías o descripciones mediante texto pero no resuelven de forma robusta todos los atributos, posiciones y relaciones que implica una condición compuesta (Gu et al., 2021; Yao et al., 2024). La estrategia indirecta resulta especialmente pertinente para las condiciones cuya evidencia es la ausencia de un EPP, como CR-01, CR-02 y CR-03, y para las que requieren relaciones espaciales intracuadro, como CR-03 y CR-04. Su ganancia potencial en robustez semántica se paga con mayor complejidad de razonamiento y con una posible carga adicional de inferencia por cuadro, cuya magnitud deberá verificarse contra el presupuesto de latencia del framework de métricas. El protocolo compara ambas estrategias en todas las condiciones en que sean aplicables, sin presuponer la superioridad de ninguna, y los códigos identifican las variantes en el diseño arquitectónico y en la evaluación experimental.

El cuarto eje es la composición del vocabulario activo y evalúa cómo el conjunto de prompts simultáneamente activos afecta el desempeño de cada uno. FG-OVD muestra que varios detectores open-vocabulary tienen dificultades para distinguir y asignar correctamente descripciones finas cuando el vocabulario incluye clases negativas semánticamente cercanas al objetivo (Bianchi et al., 2024). En E-OVRT-VDP el sistema busca simultáneamente varias condiciones y entidades, como “hard hat”, “person”, “reflective *vest*” y “scaffolding”, y se plantea la hipótesis de que prompts semánticamente próximos compiten entre sí y generan confusiones de clasificación. Por eso cada prompt se evalúa tanto en aislamiento como dentro del vocabulario completo del sistema. El tamaño del vocabulario se considera además una variable experimental, porque puede afectar la precisión y el costo de inferencia de manera dependiente de la arquitectura. Las familias YOLO orientadas a open-vocabulary precomputan los embeddings textuales fuera del ciclo de inferencia, mientras que Grounding DINO procesa el par imagen-texto en cada consulta y un vocabulario mayor encarece la fusión *cross-modal* (Cheng et al., 2024; Wang et al., 2025; Liu et al., 2024). El detalle arquitectónico se desarrolla en el análisis de modelos OVD, y la consecuencia de diseño es que la cantidad de prompts sostenible dentro del presupuesto de latencia depende del modelo, de la sintaxis concreta, de la resolución de entrada y del hardware, por lo que su efecto se mide y no se presupone.

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

Los criterios C1 a C7 de la Tabla 16 no tienen pesos fijos. Su relevancia depende del papel previsto para cada fuente y del nivel de evaluación que deba sostener.

**Tabla 16**

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

***Nota.*** C4 se aplica únicamente cuando la fuente se destina a seguimiento, continuidad temporal o alertas por episodio. La ausencia de soporte temporal no invalida una colección apropiada para percepción por imagen o estado por persona.

##### 17.1.6.2. Fuentes de gestión directa, cobertura y brechas

Cuatro colecciones se retienen como candidatas de gestión directa por su pertinencia para CR-01 y CR-02, su disponibilidad y su viabilidad de integración. La Tabla 17 resume la cobertura que ofrecen, su condición de uso, los papeles que podrían asumir y la restricción principal de cada una. Esos papeles son alternativas metodológicas y no una reconstrucción de la utilización posterior.

**Tabla 17**

*Fuentes retenidas para gestión directa y papel metodológico posible*

| **Fuente y volumen o versión** | **Cobertura** | **Formato y condición de uso** | **Papel posible** | **Restricción principal** |
| --- | --- | --- | --- | --- |
| SHEL5K (Otgonbold et al., 2022). 5.000 imágenes. | CR-01 directa. | Pascal VOC. Licencia CC BY 4.0. | Ajuste o evaluación de CR-01, con asignación exclusiva. | No cubre chaleco ni condiciones espaciales o relacionales. |
| CHV (Wang et al., 2021). 1.330 imágenes. | CR-01 y CR-02. | Formato nativo por inspeccionar. El paquete no presenta una licencia formal y exige citar la fuente. | Ajuste o evaluación de CR-01 y CR-02, sujeto a verificación de uso. | Deben verificarse los términos de acceso, transformación y redistribución. |
| construction_site_safety. Roboflow Universe, versión 27. | CR-01 y CR-02. | YOLO mediante Roboflow. Licencia registrada CC BY 4.0. | Ajuste de dominio o evaluación, con asignación exclusiva. | Exige deduplicación por linaje y separación respecto del banco de evaluación. |
| ppe_siabar. Roboflow Universe, versión 1. | CR-01 y CR-02. | YOLO mediante Roboflow. Licencia registrada CC BY 4.0. | Ajuste de dominio o evaluación complementaria, con asignación exclusiva. | Requiere curación y una fuente independiente para evaluar generalización. |

***Nota.*** Los papeles indicados no constituyen una asignación efectiva y son mutuamente excluyentes dentro de una misma comparación principal.

Las demás colecciones no se incorporan al uso principal cuando su acceso, licencia, dominio o cobertura no aportan una base defendible para el núcleo. La exclusión delimita su papel dentro del protocolo y no constituye una evaluación general de su calidad científica. MOCS conserva un alcance exploratorio por su contenido de maquinaria y trabajadores.

**Tabla 18**

*Fuentes no retenidas para el uso principal y motivo metodológico*

| **Fuente** | **Motivo de exclusión o alcance residual** |
| --- | --- |
| SH17 | La licencia CC BY-NC-SA 4.0 y el predominio de escenas industriales limitan su adopción como fuente principal del núcleo. |
| Pictor-PPE | La licencia no pudo verificarse y la versión pública es parcial. Estas condiciones impiden una gestión y redistribución reproducibles. |
| Construction-PPE | La licencia atribuida como AGPL-3.0 y su aplicabilidad al paquete de datos requieren verificación. La cobertura de EPP ya está atendida por fuentes retenidas, sin un aporte diferencial suficiente. |
| GDUT-HWD y SHWD | La licencia de los paquetes no está verificada y la condición principal ya queda cubierta. Se conservan como referencia, no como insumo gestionado. |
| SODA | Aporta contexto de obra, pero su cobertura se orienta a condiciones fuera del núcleo y no representa de forma nativa CR-01 o CR-02. |
| MOCS | La copia pública es parcial. Su utilidad se limita a exploraciones sobre maquinaria, vehículos y trabajadores, sin uso principal en ajuste o evaluación de EPP. |

***Nota.*** Las licencias consignadas son las que declara cada paquete de datos. Cuando la declaración proviene de un repositorio de código, de una publicación o de una copia y no del paquete original, la fuente se mantiene en estado condicional.

El cruce entre las fuentes retenidas y el catálogo muestra un soporte sólido para CR-01 y adecuado para CR-02. CR-03 y CR-04 mantienen brechas directas, mientras que CR-05 y CR-06 carecen de cobertura nativa de la condición completa. La Tabla 19 sintetiza esa diferencia y su consecuencia metodológica.

**Tabla 19**

*Cobertura de datos por condición y consecuencia metodológica*

| **Condición** | **Nivel de cobertura** | **Fuentes retenidas o apoyo** | **Uso metodológico definido** |
| --- | --- | --- | --- |
| CR-01 — Persona sin casco | Sólida | SHEL5K, CHV, construction_site_safety y ppe_siabar. | Integra el núcleo obligatorio. Admite evaluación directa o composición del estado por persona. |
| CR-02 — Persona sin chaleco reflectivo | Adecuada | CHV, construction_site_safety y ppe_siabar. | Integra el núcleo obligatorio, con menor redundancia de fuentes que CR-01. |
| CR-03 — Trabajo en altura sin anticaídas | Brecha directa | No existe una fuente retenida con la condición completa. | Sólo permite evaluación exploratoria de componentes o material complementario controlado. |
| CR-04 — Borde elevado desprotegido | Brecha directa | No existe una fuente retenida con la condición completa. | Se mantiene como extensión condicionada y no bloquea la aceptación del núcleo. |
| CR-05 — Maquinaria cerca de peatones | Sin cobertura directa retenida | Se requieren entidades relacionadas y evidencia temporal. | La evaluación depende de material específico y lógica contextual. |
| CR-06 — Persona en zona restringida | Sin cobertura directa retenida | Se requieren un polígono externo y una cámara fija. | La evaluación depende de parametrización espacial externa al prompt. |

***Nota.*** La cobertura se refiere a la posibilidad de evaluar la condición operativa completa y no sólo a la presencia de algunas de sus entidades en una colección.

Las cuatro fuentes retenidas permiten estudiar el núcleo, pero no sostienen por sí solas conclusiones sobre altura, zonas restringidas, relaciones peatón-maquinaria o desempeño en obra no controlada. La transferibilidad se interpreta según la proximidad visual al dominio, la diversidad de escalas, la presencia de negativos y la correspondencia entre anotaciones y condición evaluada.

Cuando una condición brechada permanezca dentro del alcance exploratorio, se prioriza primero la curación de fuentes públicas con licencia compatible. Si la cobertura continúa siendo insuficiente, se recurre a anotación complementaria acotada y, en última instancia, a material controlado del EBE. La ampliación debe aplicar las salvaguardas de la sección 17.1.10 y aportar evidencia interpretable sin desplazar la evaluación del núcleo.

La evaluación temporal exige además un material construido para ese fin, porque ninguna de las fuentes retenidas aporta secuencias con episodios anotados de las condiciones del núcleo. Ese banco se construye con dos bloques de procedencia y control experimental distintos, un rodaje guionado registrado con el hardware de captura del prototipo y un lote de obra real no guionada obtenido de fuentes públicas, que aporta tiempo en cumplimiento y permite medir especificidad. Cada clip conserva su procedencia y su grado de control como atributo, y la referencia de episodios se congela antes de reportar.

##### 17.1.6.3. Asignación de roles y partición experimental

Antes de ejecutar, cada fuente retenida se asigna a ajuste, validación interna del ajuste o banco de evaluación. Una fuente destinada al ajuste no integra el banco de evaluación de la comparación principal, aun cuando sus particiones nominales sean disjuntas. Esta regla es más restrictiva que la separación de imágenes y busca controlar duplicados, derivados o linajes comunes entre colecciones.

Si la rama de ajuste fino se habilita conforme a la sección 17.1.9, se limita a CR-01 y CR-02 y utiliza fuentes con cobertura, licencia y formato compatibles. El conjunto de entrenamiento se mantiene dentro del rango orientativo de 500 a 2.000 imágenes fijado por el protocolo. Su composición, la conversión de formatos y las operaciones de aumento de datos se declaran antes de entrenar. La línea base zero-shot y la variante ajustada se evalúan sobre el mismo banco congelado, sin presuponer que el ajuste deba resultar superior. La comparación debe informar tanto la ganancia en dominio como la retención de capacidades abiertas. Las proporciones concretas y cualquier desviación del rango se justifican durante la implementación.

**Tabla 20**

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

**Tabla 21**

*Benchmarks de referencia para el módulo de seguimiento*

| **Benchmark** | **Escala y licencia registrada** | **Métricas previstas** | **Función en el protocolo** | **Límite de interpretación** |
| --- | --- | --- | --- | --- |
| MOT17 | 14 secuencias reales, operacionalizadas como 42 entradas al considerar DPM, Faster R-CNN y SDP. CC BY-NC-SA 3.0. | MOTA, IDF1 y HOTA. | Verificar la implementación local y el cálculo de métricas. Permite contrastar con resultados públicos de trackers como ByteTrack y OC-SORT. | Seguimiento de peatones. No representa obra ni condiciones de riesgo. |
| OVT-B | 1.973 videos, 637.608 cajas y 1.048 categorías. Apache-2.0 registrada en el repositorio oficial. | TETA, con LocA, ClsA y AssA. | Ejercitar la integración OVD+MOT bajo vocabulario abierto y trayectorias de múltiples categorías. | No declara cobertura específica del dominio de la construcción. |

***Nota.*** TrackingNet y LaSOT se excluyen porque corresponden a seguimiento de objeto único. OVT-B se prioriza sobre OV-TAO por su mayor escala. TETA es Track Every Thing Accuracy y se descompone en LocA, ClsA y AssA, que miden localización, clasificación y asociación. Las referencias primarias son Milan et al. (2016) para MOT17 y Liang y Han (2024) para OVT-B.

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

Los niveles se relacionan, pero no se sustituyen. El desempeño perceptivo ayuda a explicar el estado por persona, y ambos ayudan a interpretar las alertas, aunque ningún resultado inferior garantiza el superior. La identidad temporal y las métricas de seguimiento se incorporan cuando permiten estudiar continuidad o asociación, pero no reemplazan la evaluación por episodio. La Tabla 22 consolida esta jerarquía junto con las familias de evidencia complementarias.

**Tabla 22**

*Framework de métricas por nivel de evaluación y familia de evidencia*

| **Nivel o familia** | **Unidad evaluada** | **Métricas y medidas** | **Condición de aplicación** | **Lectura dentro del protocolo** |
| --- | --- | --- | --- | --- |
| Percepción por imagen | Imagen y clase | AP@0,5, AP@[0,50:0,95], precisión, recall y F1. | Anotaciones espaciales y regla de asociación explícita. | Mide la salida perceptiva. No representa por sí sola una alerta. |
| Estado por persona | Persona evaluable | Precisión, recall y F1 por condición. Matriz de confusión cuando aporte al diagnóstico. | Referencia que asocie persona y EPP o estado observable. | Captura errores de detección, asociación y derivación del estado. |
| Alerta temporal | Episodio anotado | Precisión, recall y F1 por episodio, *t_alert-system*, TTFD y SDR. | Inicio y cierre temporal, patrón configurado y alerta trazable. | Representa el comportamiento de la plataforma completa. |
| Material negativo | Clip o intervalo sin episodio positivo | Conteo de falsos positivos, duración observada y FAR/hora derivada. | Referencia temporal negativa y criterio de falso positivo fijado. | Caracteriza activaciones espurias. No ingresa en precisión, recall ni F1. |
| Identidad temporal | Persona o trayectoria | *ΔFP_tracking* y variación de re-alertas. MOTA, IDF1 y HOTA de forma condicionada. | Identidad temporal habilitada. Las métricas MOT exigen referencia persistente. | Distingue el aporte operativo de la identidad de la calidad MOT clásica. |
| Viabilidad operativa | Corrida y unidad procesada | FPS efectivos, *t_G2A*, latencias por tramo, uso de VRAM, GPU, RAM y estabilidad. | Tramos instrumentados, régimen y duración declarados. | Determina si la cadena sostiene la fuente sin acumulación de atraso no acotada. |
| Comparación de ajuste | La misma unidad que la línea base | Deltas de AP, precisión, recall y F1, retención open-vocabulary y costo de entrenamiento. | Banco común congelado y separación estricta entre entrenamiento y evaluación. | Mide el efecto de la adaptación. No constituye un nivel evaluativo adicional. |

***Nota.*** AP@0,5 y AP@[0,50:0,95] se reportan como convenciones distintas y no se intercambian. FAR/hora es una tasa derivada del conteo y de la duración negativa observada. Una re-alerta asociada al mismo episodio no es un falso positivo. Las métricas MOT sólo se calculan cuando la referencia conserva identidades persistentes.

##### 17.1.7.3. Métricas adoptadas y reglas de lectura

En percepción por imagen se adoptan AP@0,5 y AP@[0,50:0,95], junto con precisión, recall y F1 en el punto operativo declarado. La regla de correspondencia debe fijar el umbral de intersección sobre unión, el tratamiento de predicciones duplicadas y la correspondencia entre etiquetas de la fuente y vocabulario activo. Las dos variantes de AP se informan por separado, ya que responden a convenciones diferentes. NMS-AP se conserva como referencia conceptual para análisis de vocabulario fino, pero no sustituye las métricas estándar ni constituye un requisito del núcleo (Everingham et al., 2010; Lin et al., 2014; Yao et al., 2024).

En el nivel de estado por persona, la predicción se obtiene después de vincular la evidencia perceptiva con cada sujeto evaluable. Para CR-01 y CR-02, una persona se clasifica según la presencia o ausencia observable del EPP en la región definida por el protocolo. La evaluación usa precisión, recall y F1 por condición. Los errores de asociación forman parte del resultado porque una detección correcta de casco o chaleco no resuelve el estado si se asigna a la persona equivocada. Cuando se comparen estrategias directas, indirectas o híbridas, la unidad y el conjunto de personas evaluables deben permanecer constantes.

En el nivel de alerta, un verdadero positivo es una alerta que corresponde a un episodio anotado conforme a la regla temporal de asociación. Un falso negativo es un episodio evaluable sin alerta válida. Un falso positivo es una alerta sin episodio positivo asociado bajo el mismo criterio. La precisión, el recall y el F1 se calculan sobre episodios positivos. El material negativo se informa mediante el número de falsos positivos y la duración observada. FAR/hora puede presentarse como derivación, pero no sostiene por sí sola una cota operativa cuando la exposición negativa es reducida.

*t_alert-system* mide el intervalo entre el inicio anotado del episodio y la marca temporal de la unidad visual que satisface la confirmación del patrón y origina el registro de la alerta. Sólo corresponde en corridas con evaluación de patrón, referencia temporal y alerta trazable. TTFD mide el intervalo entre ese inicio y la primera evidencia positiva válida según el criterio declarado. No debe confundirse con la alerta confirmada. SDR expresa qué proporción de la duración o de las unidades temporales válidas mantiene evidencia correcta mientras la condición está activa. Su definición debe indicar si se calcula en tiempo o en cuadros, y sólo admite comparación directa entre corridas con la misma cadencia de muestreo.

La severidad funciona como estrato de lectura y no como métrica. Cuando se reporte desempeño por severidad, cada resultado debe conservar el tamaño muestral, el punto operativo y la condición incluida. No se mezclan niveles de severidad en un agregado sin mostrar el desglose. La prioridad temporal asignada a cada patrón orienta los objetivos de TTFD y *t_alert-system*, pero no modifica retrospectivamente la referencia anotada ni la definición de un episodio.

La identidad temporal se evalúa primero por su efecto sobre la salida operativa. *ΔFP_tracking* compara el conteo de falsos positivos entre corridas equivalentes con identidad deshabilitada y habilitada. La unidad del falso positivo debe definirse antes del contraste y mantenerse estable. Las re-alertas o reconfirmaciones del mismo episodio se contabilizan por separado. MOTA, IDF1 y HOTA permanecen disponibles como métricas condicionadas para secuencias con referencia de identidad persistente. Su ausencia no implica que la capacidad de identidad temporal esté fuera del sistema, sino que no corresponde juzgarla mediante métricas MOT sin datos adecuados (Bernardin & Stiefelhagen, 2008; Ristani et al., 2016; Luiten et al., 2021).

La viabilidad operativa se caracteriza mediante la cadencia efectiva, las latencias por tramo, el consumo de recursos y la estabilidad. Los FPS efectivos se calculan sobre unidades realmente procesadas y deben distinguirse de la tasa nominal de captura. La media de latencia se complementa con P50, P95 y P99 cuando se conservan observaciones individuales suficientes. El uso de VRAM, GPU, RAM y CPU se registra junto con el modelo, la resolución y la precisión numérica. Una configuración sólo se considera capaz de sostener la fuente cuando el atraso permanece acotado y no crece de forma sostenida durante la corrida. Las definiciones operativas, el formato de reporte y los criterios de estabilidad de estas medidas se consolidan en la Tabla D.1 del Anexo D.

Toda cifra se informa con la combinación que la produjo, el material o estrato sobre el que se calculó y su denominador. Los agregados pueden sintetizar, pero no reemplazan los desgloses cuando existen fuentes, condiciones o escenarios heterogéneos. Esta regla alcanza tanto a las métricas de calidad como a las temporales y operativas.

##### 17.1.7.4. Comparación entre línea base zero-shot y variante ajustada

La comparación entre una línea base zero-shot y una variante ajustada al dominio busca medir el efecto de la adaptación, no demostrar de antemano que el ajuste sea superior. La línea base se ejecuta primero y conserva el punto de referencia de cada métrica. La variante ajustada se evalúa sobre el mismo banco congelado, con la misma unidad de análisis y el mismo procedimiento, salvo la modificación paramétrica que se desea estudiar. Las reglas de disyunción, deduplicación y congelamiento de datos se establecen en la sección 17.1.6.

El contraste informa el cambio absoluto de cada métrica mediante la diferencia entre la variante ajustada y la línea base. La calidad dentro del dominio se mide con AP, precisión, recall y F1 en los niveles donde corresponda. Los cambios en TTFD, SDR o *t_alert-system* sólo se calculan cuando ambas variantes se ejecutan sobre video, comparten episodios evaluables y mantienen la misma configuración temporal. La retención open-vocabulary se mide sobre categorías separadas del ajuste y debe informar el valor de referencia, el valor posterior y la variación observada.

El costo de adaptación forma parte del resultado comparativo. Deben registrarse horas de GPU, tiempo total, cantidad de imágenes, parámetros entrenables, procedimiento de ajuste y checkpoints considerados. Ninguna variante se declara mejor a partir de una única métrica. El veredicto debe identificar qué combinación mejoró, sobre qué material, con qué denominador y qué costo o degradación acompañó esa mejora. Si falta una línea base válida, existe filtración entre entrenamiento y evaluación o las unidades no son equivalentes, el delta se declara no interpretable.

##### 17.1.7.5. Presupuesto temporal y referencias por severidad

El presupuesto temporal separa tres naturalezas. La primera corresponde a tramos de captura y procesamiento que pueden instrumentarse como intervalos de ejecución. La segunda es la espera funcional necesaria para acumular evidencia y confirmar un patrón. La tercera corresponde a la distribución de una alerta ya confirmada. Estas magnitudes contribuyen a la oportunidad observada, pero no deben presentarse como si fueran un único costo computacional.

Toda latencia debe declarar el hito inicial, el hito final y el dominio de reloj. Los relojes monotónicos son adecuados para intervalos medidos dentro de un mismo proceso o dominio temporal. No se restan directamente marcas monotónicas de procesos o nodos distintos. En una cadena distribuida, los tramos se correlacionan mediante marcas de la fuente, relojes sincronizados o identificadores que permitan vincular una misma unidad. Cuando no existe una marca confiable de captura, el informe comienza en el primer hito instrumentado y no presenta ese intervalo como latencia completa desde el sensor.

Las métricas temporales asociadas a la alerta se definen mediante diferencias entre hitos correlacionados, no mediante la suma de componentes agregados. Para un episodio evaluable *e*, la definición formal de *t_alert-system* es la siguiente.

⟦ECUACIÓN: no extraída — ver el .docx⟧

El hito inicial es el comienzo anotado de la condición. El hito final es la marca temporal, en el reloj de la fuente, de la unidad visual que satisface la regla de confirmación y origina la alerta. Ambas marcas deben corresponder al mismo episodio y expresarse en una referencia temporal compatible.

Para una alerta *a* cuyo trayecto externo esté instrumentado, la definición formal de *t_alert-notification* es la siguiente.

⟦ECUACIÓN: no extraída — ver el .docx⟧

El hito inicial es la marca de publicación con la que la alerta queda disponible para distribución. El hito final es la confirmación verificable del canal instrumentado. Este tramo no incluye *t_alert-system*. La composición entre ambas métricas sólo es válida cuando cada observación conserva hitos correlacionables y compatibles. Sus percentiles agregados no se suman.

La Tabla 23 ubica estas fronteras dentro de la cadena temporal y las relaciona con los demás tramos y condiciones de instrumentación.

**Tabla 23**

*Tramos temporales y condiciones de instrumentación*

| **Tramo o componente** | **Hito inicial y final** | **Aplicabilidad** | **Regla de reporte** |
| --- | --- | --- | --- |
| Captura a host (capture_to_host) | Marca temporal de captura o lectura → dequeue de la unidad visual. | Sólo cuando la fuente aporta una referencia temporal confiable. | Se informa por separado. Si falta, no se infiere ni se suma a otro tramo. |
| G2A instrumentado (*t_G2A*) | dequeue → fin de inferencia. | Corridas con detector instrumentado. | Debe declarar sus fronteras. No equivale a sensor → algoritmo cuando la captura queda fuera. |
| Preprocesamiento | dequeue → entrada preparada para el modelo. | Corridas integradas de percepción. | Se desglosa por resolución, normalización y transferencias CPU-GPU. |
| Inferencia | Inicio del modelo → detecciones disponibles. | Toda corrida que evalúe un detector. | Se reporta por modelo, resolución, precisión numérica y tamaño de lote. |
| Identidad temporal | Detecciones → asociaciones o estados por sujeto. | Sólo cuando la identidad esté habilitada. | Se informa con el método, la densidad de escena y el número de unidades. |
| Evaluación de patrón | Evidencia normalizada → actualización del estado del patrón. | Corridas integradas con motor de patrones. | Mide cómputo. No incluye la espera funcional de persistencia. |
| Ventana funcional | Primera evidencia aceptada → criterio de confirmación. | Patrones con persistencia temporal. | Es una regla funcional configurada, no una latencia computacional. |
| Alerta del sistema (*t_alert-system*) | Inicio anotado del episodio → unidad visual que confirma el patrón y origina la alerta. | Episodio temporal, patrón activo y alerta trazable. | No incluye la notificación externa. Se informa por condición y material. |
| Notificación (*t_alert-notification*) | Alerta disponible para distribución → confirmación del canal instrumentado. | Sólo cuando exista un canal externo medible. | Es un tramo independiente. No se suman percentiles no correlacionados. |

***Nota.*** G2A = Glass-to-Algorithm. Cada corrida conserva las fronteras temporales y el dominio de reloj de los tramos que reporta.

El tramo computacional reúne el preprocesamiento, la inferencia, la identidad temporal cuando corresponde y la evaluación del patrón. La ventana de evidencia se mantiene separada porque representa acumulación funcional. *t_alert-system* se obtiene a partir de los hitos del episodio y de la alerta, no mediante la suma de percentiles de componentes.

Para instrumentar la cadena y estimar la plausibilidad del presupuesto se adopta además un modelo de presupuesto de ingeniería con notación propia, separada de las métricas medidas por hitos. *B* denota la estimación orientativa de un tramo y *W* una espera funcional. Los componentes sólo se suman cuando son sucesivos y no se solapan.

⟦ECUACIÓN: no extraída — ver el .docx⟧

⟦ECUACIÓN: no extraída — ver el .docx⟧

*B_captura-host* corresponde al tramo capture_to_host de la Tabla 23 y sólo se incluye cuando la fuente aporta una marca de captura confiable. *B_identidad* corresponde a la identidad temporal cuando está habilitada y *B_reglas* al cómputo de la evaluación del patrón. *B_alerta* es una referencia de plausibilidad y no reemplaza a *t_alert-system*, que se obtiene de los hitos reales del episodio y de la alerta. La latencia vidrio a alerta de un episodio se aproxima entonces a la suma de TTFD y *B_alerta*. *t_alert-system*, medida entre hitos del reloj de la fuente, comprende la reacción perceptiva inicial y la ventana funcional, pero no la cola de procesamiento del cuadro que confirma, que se informa por separado mediante capture_to_host y *t_G2A*. La estimación orientativa que sigue corresponde a *B_procesamiento*.

Con el perfil de hardware de referencia, una LAN controlada y modelos orientados a inferencia eficiente, el tramo previo a la acumulación temporal puede ubicarse de manera orientativa entre 35 y 250 ms por unidad procesada. La captura y el transporte pueden aportar del orden de 10 a 50 ms cuando se dispone de una referencia temporal compatible. El preprocesamiento se estima entre 5 y 20 ms, la inferencia entre 15 y 150 ms, la identidad temporal entre 5 y 20 ms cuando se habilita y la evaluación de reglas simples por debajo de 10 ms. Son estimaciones de ingeniería para evaluar plausibilidad, no cotas universales ni sustitutos de la medición. La literatura relevada respalda la sensibilidad de estos tramos al transporte, al modelo y al método de seguimiento (Axis Communications AB, s. f.; Bachhuber et al., 2018; Cheng et al., 2024; Wang et al., 2025; Bewley et al., 2016; Zhang et al., 2022).

La latencia de alerta incorpora además la ventana de evidencia definida para cada patrón. Por ello, un tiempo computacional bajo no garantiza una alerta temprana si la confirmación exige mayor persistencia. Las referencias de la Tabla 24 ordenan la lectura temporal por severidad y mantienen TTFD por debajo del objetivo de confirmación para que mida respuesta perceptiva inicial. El objetivo de *t_alert-system* de cada severidad debe ser compatible con la ventana de persistencia fijada para sus patrones en la sección 17.1.5.2 y dejar margen para el procesamiento y la variabilidad de la cadena. Los valores orientativos deben recalibrarse antes de utilizarse como criterio de aceptación cuando cambien el modelo, la resolución de entrada, la cadencia o las condiciones de transporte.

**Tabla 24**

*Referencias temporales orientativas por severidad*

| **Severidad** | **Máximo orientativo de** ***t_alert-system*** | **Objetivo orientativo de TTFD** | **Referencia mínima de SDR** | **Lectura operativa** |
| --- | --- | --- | --- | --- |
| Crítica | 3 a 5 s | < 1 s | ≥ 0,50 | Se prioriza no omitir episodios y se admite menor estabilidad inicial. |
| Alta | 5 a 10 s | < 3 s | ≥ 0,60 | Se busca equilibrio entre rapidez, persistencia y control de falsas alertas. |
| Media | 10 a 20 s | < 10 s | ≥ 0,70 | Puede exigirse mayor evidencia antes de confirmar, con mayor tolerancia temporal. |

***Nota.*** Los valores ordenan prioridades y criterios de lectura. No constituyen límites normativos ni universales del dominio. Deben calibrarse con la cadencia efectiva, las ventanas del patrón y el material de evaluación, sin modificar después de observar resultados la definición de los episodios o las reglas de asociación.

##### 17.1.7.6. Instrumentación, aplicabilidad y reporte

Toda corrida debe registrar el contexto necesario para reproducirla con los campos mínimos consolidados en la Tabla D.3 del Anexo D. En una comparación de ajuste se agregan la semilla, la partición, la composición del corpus y el procedimiento de entrenamiento.

Las corridas temporales deben conservar los hitos que permiten reconstruir la cadena evaluada. Esto incluye la referencia del episodio, la primera evidencia positiva válida, el inicio del patrón candidato cuando corresponda, la unidad que confirma el patrón, el registro de la alerta y, si aplica, la confirmación del canal externo. Cada marca temporal se acompaña del dominio de reloj y del identificador necesario para correlacionarla. La falta de uno de estos hitos limita el tramo que puede reportarse.

Las mediciones de rendimiento incluyen un período de calentamiento identificado y una ventana estable de observación. Se informan promedio, P50, P95 y P99 cuando existen observaciones individuales suficientes, junto con el número de muestras y la duración de la corrida. Cuando sólo se conserva un agregado, se reporta ese estadístico y se declara la imposibilidad de reconstruir percentiles. No se generan distribuciones sintéticas ni se presentan estimaciones como mediciones.

La aplicabilidad se determina antes de interpretar el valor. Las métricas MOT no corresponden sin referencia de identidad persistente. *t_alert-system* no corresponde en pruebas que terminan en detecciones por imagen. TTFD y SDR no corresponden sin continuidad temporal e inicio anotado. *t_alert-notification* no corresponde sin un trayecto externo instrumentado. Los deltas de ajuste no son interpretables sin una línea base equivalente o cuando existe filtración entre entrenamiento y evaluación. En cada caso se informa el estado y su causa. Los insumos mínimos que habilitan cada familia de métricas se consolidan en la Tabla D.2 del Anexo D.

El reporte se organiza por condición, fuente o estrato y escenario. Toda cifra incluye el denominador efectivo. Los clips negativos se presentan mediante el conteo de falsos positivos, la duración negativa observada y, sólo después, la tasa horaria derivada. Las re-alertas del mismo episodio se mantienen separadas. SDR se compara únicamente bajo una cadencia equivalente. Las latencias de alerta se contrastan sobre conjuntos comunes de episodios evaluables o se declara la diferencia de cobertura que impide la comparación.

Este framework vincula la calidad perceptiva con el comportamiento temporal y la viabilidad de la plataforma sin confundir niveles de evidencia. La sección 17.1.8 utiliza estas reglas para formular criterios de aceptación y riesgos experimentales. Las secciones de implementación y resultados documentan, respectivamente, qué tramos y métricas se instrumentaron, cuáles se calcularon y qué limitaciones condicionaron su interpretación.

#### 17.1.8. Protocolo experimental integrado

La secuencia experimental busca evitar que decisiones tardías alteren la validez comparativa del estudio. Ninguna fase que modifique el estado del modelo o del conjunto de datos se ejecuta antes de congelar el software relevante, los checkpoints retenidos, el banco de evaluación y la estructura mínima de bitácora. Sobre esa base el protocolo se ordena en las fases sucesivas de la Tabla 25 y no como un conjunto abierto de ensayos.

El conjunto de métricas aplicables a cada corrida se fija antes de ejecutarla con las reglas de aplicabilidad de la sección 17.1.7.6. Las métricas temporales y las de seguimiento sólo se exigen cuando la evidencia disponible las habilita.

**Tabla 25**

*Fases del protocolo experimental integrado*

| **Fase** | **Objetivo** | **Salida esperada** | **Criterio de cierre** |
| --- | --- | --- | --- |
| Preparación | Congelar entorno, versiones, checkpoints, datasets retenidos y estructura mínima de bitácora. | Artefactos y configuración de corrida documentados. | Reproducibilidad básica garantizada. |
| Baseline DBE | Medir cada modelo candidato en zero-shot sobre el banco de evaluación congelado. | Línea base por condición, prompt y métrica obligatoria. | Predicciones exportadas y métricas obligatorias calculadas. |
| Sensibilidad de prompts | Comparar familias de prompts y congelar la formulación primaria por condición. | Matriz comparativa y selección justificada. | Prompt principal y variantes de contraste definidos. |
| Pipeline y seguimiento | Medir *t_G2A*, FPS, recursos y aporte del tracker. | Diagnóstico del comportamiento integrado. | Logs temporales y métricas de estabilidad disponibles. |
| Fine-tuning condicionado | Ejecutar adaptación al dominio sólo si se cumplen las condiciones metodológicas fijadas. | Variante comparativa exportada al CPN. | Comparación válida respecto de baseline y banco de evaluación compartido. |
| EBE complementario | Ejecutar captura continua en entorno controlado o simulado. | Evidencia de plausibilidad operativa y latencia integrada. | Eventos, timestamps y alertas registradas. |
| Reporte | Integrar métricas aplicadas, métricas no aplicables y causas de exclusión. | Informe de resultados trazable y replicable. | Se explicitan alcance, límites y condiciones de interpretación. |

***Nota.*** La secuencia expresa dependencias entre fases y no un calendario. El orden y las fechas efectivas de ejecución se documentan en la implementación.

#### 17.1.9. Estrategia de adaptación al dominio

La adaptación al dominio se mantiene como una rama comparativa condicionada y no como un requisito para demostrar la viabilidad del enfoque. Adoptarla de antemano convertiría una hipótesis todavía no probada en un supuesto metodológico. La rama sólo se habilita cuando existe soporte de datos suficiente y la comparación puede sostenerse sin romper la integridad del protocolo. Sus condiciones de habilitación son de datos y de protocolo y no de disponibilidad de cómputo. El TN aporta el entrenamiento y el CPN conserva la referencia operativa.

La comparación se concentra como máximo en dos candidatos, Grounding DINO y YOLOE, que representan compromisos distintos entre expresividad semántica y eficiencia de inferencia (Liu et al., 2024; Wang et al., 2025). Cuál de ellos se ajusta depende de la factibilidad real de integración, exportación y ejecución sobre el CPN y no sólo de su rendimiento en benchmarks generales. La elección del candidato para adaptación se distingue de la selección del perfil operativo del núcleo sin ajuste de pesos. Para medir el efecto del ajuste, la referencia es la línea base del mismo modelo, no la de un perfil operativo de otro linaje.

La rama se ejecuta como una jornada experimental completa con criterios prerregistrados, una única línea base, márgenes fijados antes de evaluar y un veredicto determinado por reglas de aceptación declaradas de antemano. La Tabla 26 consolida esa regla de decisión.

**Tabla 26**

*Regla metodológica de decisión para la adaptación al dominio*

| **Regla** | **Decisión adoptada** | **Sentido metodológico** |
| --- | --- | --- |
| Existencia de baseline | Ningún ajuste se evalúa sin baseline zero-shot previa sobre el mismo banco de evaluación. | Sin baseline explícita no existe comparación defendible. |
| Disponibilidad de datos | Se priorizan CR-01 y CR-02. CR-03 y CR-04 quedan fuera del camino ordinario mientras no exista cobertura suficiente. | Concentra el ajuste donde puede producir evidencia útil y comparaciones válidas. |
| Integridad comparativa | El banco de evaluación debe ser compartido y permanecer congelado. | Evita leakage y falsas mejoras por cambio de evaluación. |
| Ganancia exigible | La variante ajustada debe superar el margen fijado antes de evaluar y no mostrar sólo una ventaja marginal. | Protege al protocolo de ciclos costosos de ajuste con retorno metodológico débil. |
| Costo operativo | La variante ajustada no debe comprometer materialmente la latencia ni el presupuesto de recursos del CPN. | Una mejora semántica que destruye la viabilidad operativa no fortalece al prototipo. |

***Nota.*** La regla no prescribe que el ajuste deba ejecutarse. Define cuándo vale la pena hacerlo sin distorsionar el objetivo principal del prototipo.

#### 17.1.10. Supuestos, riesgos de validez y consideraciones ético-legales

El marco ético-legal del protocolo se apoya en la minimización de datos y en el uso asistivo del sistema. Cuando el proyecto genera material propio para el EBE rigen salvaguardas de finalidad determinada, acceso restringido, retención acotada y ausencia de reconocimiento de identidad personal o tratamiento biométrico, en línea con los principios de la sección 16.6 y con el régimen argentino de protección de datos personales y videovigilancia (Argentina, 2000, 2015).

La interpretación de los resultados descansa en cinco supuestos. El prototipo es un sistema asistivo y una alerta no equivale a una sanción ni a una determinación automática de incumplimiento normativo. La evaluabilidad de varias condiciones depende de variables que el detector no controla del todo, como la escala aparente, el ángulo de cámara, la oclusión o la iluminación. CR-06 presupone una parametrización espacial externa al prompt y no se evalúa como si el lenguaje por sí solo definiera la zona restringida. El EBE valida en entorno controlado o simulado y no en obra real.

El quinto supuesto es que la disyunción entre datos de entrenamiento y banco de evaluación sólo es verificable sobre el ajuste propio del trabajo. Los modelos preentrenados de vocabulario abierto provienen de corpus de terceros no inspeccionables, de modo que no puede descartarse que imágenes del banco hayan participado de ese preentrenamiento. Es una condición estructural de toda evaluación de modelos preentrenados y no una particularidad de este protocolo. Por eso las cifras zero-shot se leen como una comparación entre combinaciones bajo condiciones idénticas y no como afirmaciones sobre generalización a material inédito. La Tabla 27 reúne los riesgos metodológicos y operativos que condicionan las instancias siguientes y la mitigación adoptada para cada uno.

**Tabla 27**

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

Las instancias siguientes toman estas definiciones como referencia. El análisis y diseño arquitectónico las traduce en una organización técnica y la validación experimental produce resultados sobre las condiciones, los escenarios y las métricas fijadas, con la instrumentación de *t_G2A* y *t_alert-system* definida en la sección 17.1.7. En todos los casos debe declararse qué elementos del catálogo se implementaron, cuáles no aplicaron y cuáles permanecieron condicionados. Esa trazabilidad entre definición metodológica, diseño, implementación y validación es el principal resultado de esta parte del proyecto y sostiene su orientación central, que es evaluar si la detección open-vocabulary puede integrarse como herramienta asistiva para el monitoreo de condiciones de riesgo en construcción civil.

### 17.2. Costos asociados

#### 17.2.1. Alcance y supuestos de la evaluación económica

La sección 17.1 fija qué se mide y con qué infraestructura. Esta sección estima qué recursos consume esa plataforma experimental, quién los aporta y qué ahorros produce, antes de que la sección 17.3 desarrolle su diseño. La evaluación separa tres magnitudes que conviene no mezclar. El esfuerzo es el trabajo de los integrantes, medido en horas-persona. Los recursos aportados son los bienes y servicios que el proyecto usa sin pagarlos, porque preexisten, porque se prestan o porque los provee una institución. El gasto efectivo es el dinero que el proyecto desembolsa. Sólo la tercera magnitud se expresa en moneda.

Esta distinción responde a la naturaleza del trabajo. Se trata de un trabajo final de grado, no de un proyecto contratado, y el esfuerzo de los integrantes es parte del proceso formativo. Valorizarlo a una tarifa de mercado produciría una cifra que no corresponde a ningún flujo de dinero real y que distorsionaría la lectura del gasto efectivo. Por la misma razón, el equipamiento preexistente o prestado se inventaría con su condición de uso, pero no se le asigna un precio de reposición. El proyecto no lo adquirió ni lo consumió.

Los supuestos de la estimación son tres. El horizonte es la duración del proyecto, definido en cronograma original de la Figura 1. La dedicación de referencia de cada integrante es de ocho horas semanales, sostenida a lo largo de todo el proyecto. La moneda del gasto efectivo es el peso argentino.

No se calculan indicadores de rentabilidad como el valor actual neto o la tasa interna de retorno. El producto es un prototipo experimental sin flujo de ingresos, y el objetivo de esta sección es transparentar el esfuerzo, los recursos y el gasto, e identificar los ahorros que las decisiones de diseño producen, no proyectar un negocio.

#### 17.2.2. Esfuerzo del equipo

El equipo lo integran tres estudiantes con una dedicación aproximada de ocho horas semanales cada uno, más la dirección académica del tutor. La Tabla 28 compara las horas previstas por el cronograma original con las efectivamente dedicadas hasta la defensa. El trabajo no se remunera y no se valoriza. La tabla expresa el esfuerzo del proyecto en horas-persona, que es la unidad en la que ese esfuerzo se planificó y se controló.

**Tabla 28**

*Esfuerzo del equipo. Horas-persona previstas y ejecutadas*

| **Recurso** | **Dedicación** | **Semanas previstas** | **Horas previstas** | **Semanas ejecutadas** | **Horas ejecutadas** |
| --- | --- | --- | --- | --- | --- |
| Integrante 1 | 8 h por semana | 42 | 336 | 48 | 384 |
| Integrante 2 | 8 h por semana | 42 | 336 | 48 | 384 |
| Integrante 3 | 8 h por semana | 42 | 336 | 48 | 384 |
| Tutoría académica | Reuniones de seguimiento y revisión de entregables | — | — | — | No cuantificada |
| **Total integrantes** | **24 h por semana** | **42** | **1.008** | **48** | **1.152** |

***Nota.*** Las semanas previstas corresponden al cronograma de la Figura 1 (31 de octubre de 2025 a 21 de agosto de 2026). Las ejecutadas se extienden hasta la defensa prevista para fines de septiembre de 2026. Las horas son una estimación a partir de la dedicación de referencia y no un registro de tiempos. La tutoría es un aporte institucional en especie y no se cuantifica.

La diferencia de 144 horas entre lo previsto y lo ejecutado, un 14 %, se explica por la extensión de la implementación y de la redacción final más allá del cronograma original. El esfuerzo total del proyecto, unas 1.152 horas-persona, es la magnitud principal que el trabajo consume. En un proyecto de esta naturaleza el recurso crítico es el tiempo de trabajo calificado, no el hardware ni el dinero.

#### 17.2.3. Recursos materiales aportados

La plataforma corre sobre tres nodos cuyas especificaciones detalla el Anexo B. El nodo de procesamiento es una notebook de consumo preexistente, propiedad de uno de los integrantes. El nodo de borde es una cámara Luxonis OAK-D Pro PoE prestada por el tutor. El nodo de entrenamiento es el clúster institucional, que se trata en 17.2.4 por ser un recurso de operación. La Tabla 29 inventaría el equipamiento con su condición de uso y su origen. Ninguno de estos bienes fue adquirido para el proyecto, de modo que su inversión efectiva es nula y no se les asigna valor de referencia.

**Tabla 29**

*Recursos materiales aportados. Condición de uso y origen*

| **Ítem** | **Función en el proyecto** | **Condición** | **Origen** | **Gasto efectivo (ARS)** |
| --- | --- | --- | --- | --- |
| Notebook HP Victus 15-fb2024la (Ryzen 5 8645HS, RTX 4060 Laptop 8 GB, 32 GB DDR5, SSD 1 TB) | Nodo de procesamiento. Inferencia, plano de control y distribución de alertas | Preexistente | Propiedad de un integrante | 0 |
| Cámara Luxonis OAK-D Pro PoE (Series 2) con cable Ethernet M12/RJ45 | Nodo de borde. Captura por DepthAI | Prestada | Tutor | 0 |
| Switch PoE gigabit | Alimentación y conectividad de la cámara PoE | Preexistente | Propiedad de un integrante | 0 |
| Cámara IP RTSP con grabador (DVR) | Fuente RTSP de los escenarios de evaluación | Preexistente, de uso doméstico | Propiedad de un integrante | 0 |
| Casco y chaleco reflectivo | Utilería de la jornada de rodaje | Prestados | Steel Brox S.R.L. | 0 |
| Locación de rodaje | Espacio para la captura de escenas guionadas | Cedida por una jornada | Steel Brox S.R.L. | 0 |
| **Total** |  |  |  | **0** |

***Nota.*** Los bienes se inventarían con su condición de uso y no se valorizan. Son recursos preexistentes o prestados que el proyecto no adquirió ni consumió, y cuyo precio de reposición no forma parte del costo del trabajo. Las especificaciones técnicas se consolidan en el Anexo B.

El inventario muestra que la plataforma completa se sostiene con un único equipo de consumo con GPU, una cámara PoE y accesorios de red de uso corriente. No interviene hardware especializado ni infraestructura de centro de datos. Esa observación se retoma en 17.2.5 como uno de los ahorros del proyecto.

#### 17.2.4. Infraestructura, operación y mantenimiento

Los costos de operación del prototipo son bajos por construcción. No hay servidores alquilados ni servicios en la nube. Los tres servicios de la plataforma, el plano de medios, el plano de control y la distribución de alertas, corren en el nodo de procesamiento, en forma nativa o en contenedores. El resguardo de la evidencia experimental usa una cuenta gratuita de Google Drive y el código se aloja en repositorios gratuitos de GitHub. El ajuste fino de modelos, la única tarea que excede la capacidad del equipo local, se ejecuta en el clúster Mendieta del Centro de Computación de Alto Desempeño de la Universidad Nacional de Córdoba, con acceso institucional sin cargo. La Tabla 30 resume las magnitudes de uso registradas y su gasto.

**Tabla 30**

*Infraestructura, operación y mantenimiento. Magnitud de uso registrada y gasto*

| **Concepto** | **Magnitud registrada** | **Gasto efectivo (ARS)** | **Observación** |
| --- | --- | --- | --- |
| Cómputo local de inferencia (RTX 4060 Laptop) | 472 corridas registradas entre julio y agosto de 2026, 34,4 h de GPU | 0 | Energía absorbida en el consumo doméstico. A una potencia de 100 a 150 W, equivale a entre 3 y 5 kWh |
| Cómputo en el clúster Mendieta (1 × NVIDIA A30, 10 núcleos por trabajo) | 15 trabajos enviados entre el 13 y el 20 de agosto de 2026, 10 con GPU asignada, 6 completados. 1,2 GPU-h en total, de las cuales 0,94 corresponden a las tres corridas completas de ajuste fino | 0 | Acceso institucional (CCAD-UNC) |
| Alquiler de servidores o VPS | Ninguno | 0 | Despliegue local |
| Almacenamiento y control de versiones | 2,6 GB de evidencia no regenerable en Google Drive. Código en GitHub | 0 | Planes gratuitos |
| Licencias de software | Conjunto de herramientas de código abierto de punta a punta | 0 | Ver nota sobre AGPL-3.0 |
| Conjuntos de datos y pesos de modelos | Licencias abiertas con atribución (CC BY 4.0 y equivalentes, Apache-2.0, AGPL-3.0) | 0 | Descarga directa de las fuentes |
| Conectividad a Internet | Uso doméstico de los integrantes | 0 | No discriminada |
| Mantenimiento | Suites de pruebas automatizadas de los cinco repositorios, ejecutadas en el equipo local | 0 | Sin integración continua paga |
| **Total** |  | **0** |  |

***Nota.*** Las horas de cómputo local provienen de los registros de duración de cada corrida del plano de medios. Las horas de clúster provienen de la contabilidad de Slurm del clúster Mendieta. El único componente del conjunto de herramientas con licencia AGPL-3.0 es la biblioteca de inferencia de los modelos YOLOE, de uso académico libre. Un despliegue comercial derivado exigiría publicar el código bajo la misma licencia o adquirir una licencia empresarial. El modelo campeón, Grounding DINO, se distribuye bajo Apache-2.0 y no impone esa condición.

#### 17.2.5. Gasto efectivo, financiamiento, ahorros e ingresos

**Tabla 31**

*Resumen del proyecto. Esfuerzo, recursos aportados, gasto efectivo y fuentes de financiamiento*

| **Componente** | **Magnitud** | **Gasto efectivo (ARS)** | **Fuente de financiamiento** |
| --- | --- | --- | --- |
| Esfuerzo del equipo (Tabla 28) | 1.152 horas-persona | 0 | Trabajo no remunerado de los integrantes |
| Recursos materiales aportados (Tabla 29) | Notebook, cámara PoE, switch, cámara RTSP, utilería y locación | 0 | Aporte propio (notebook, switch, cámara RTSP), préstamo del tutor (cámara OAK-D) y de Steel Brox S.R.L. (locación y utilería) |
| Infraestructura y operación (Tabla 30) | 34,4 h de GPU local, 1,2 GPU-h de clúster, 2,6 GB de evidencia | 0 | Aportes en especie de CCAD-UNC, GitHub y Google |
| Movilidad (un traslado a la locación de rodaje) | Un viaje de ida y vuelta a la sucursal de Steel Brox S.R.L. | 10.000 | Aporte propio |
| **Total gasto efectivo** |  | **10.000** |  |

***Nota.*** El esfuerzo y los recursos aportados se informan en sus propias unidades y no se valorizan. El gasto efectivo suma únicamente los desembolsos reales del proyecto.

La lectura de la tabla es directa. El proyecto consume unas 1.150 horas-persona de trabajo no remunerado, se apoya en equipamiento preexistente o prestado y en servicios institucionales o gratuitos, y su gasto efectivo se limita al traslado a la locación de rodaje. Esa es la conclusión económica central. El proyecto se financia íntegramente con trabajo propio y con aportes en especie, sin subsidios ni financiamiento externo, y ninguno de esos aportes exige una contraprestación.

**Ingresos esperados.** No los hay ni se proyectan. El producto es una plataforma experimental de medición, no un sistema comercial, y su valor se expresa en la evidencia que produce y en el conocimiento transferible sobre detección de vocabulario abierto en el dominio de la obra.

**Ahorros.** Se identifican tres costos evitados, dos de ellos medidos en el propio proyecto. En primer lugar, las licencias. El conjunto de herramientas de código abierto elimina el costo de licencias de software de inferencia, de anotación y de despliegue, con la única salvedad sobre AGPL-3.0 señalada en la Tabla 30. En segundo lugar, costos de entrenamiento. La detección de vocabulario abierto permite operar sin entrenar. Agregar un conjunto de cinco clases que la plataforma nunca había configurado costó un archivo de configuración de 48 líneas y nueve minutos de tiempo de pared, sin anotar datos ni entrenar, y la clase machinery alcanzó una AP@0.5 zero-shot de 0,662. En contraste, la rama de ajuste fino consumió 1,2 GPU-h de clúster más el esfuerzo de preparar datos, entorno y recetas, y no produjo un modelo adoptable. Para el alcance de este trabajo, el costo de entrenar fue un esfuerzo sin retorno y el costo de no entrenar fue nulo. Por último, el hardware. La plataforma completa, con sus tres servicios y la inferencia del modelo campeón, corre en una notebook de consumo. No requiere estación de trabajo ni servidor con GPU de centro de datos.

### 17.3. Diseño arquitectónico

#### 17.3.1. Propósito y pregunta rectora

El diseño arquitectónico transforma el alcance metodológico, el catálogo de condiciones de riesgo, los escenarios de evaluación, el marco de métricas y los lineamientos ético-legales ya consolidados en una organización técnica capaz de orientar la implementación del prototipo. Esos insumos operan como restricciones, de modo que cada módulo, frontera y flujo del capítulo se derive de una decisión metodológica previa y no de una preferencia técnica aislada.

La plataforma se estructura alrededor de la separación entre el procesamiento visual en tiempo real y la lógica de interpretación posterior, fundamentada en la sección 16.5.3. El plano de medios, la ruta de datos de la sección 16.5.3, produce evidencia perceptiva, y el plano de control, su ruta de control, la interpreta. Esa división protege la ruta crítica de video y sostiene la trazabilidad experimental necesaria para analizar cada corrida.

La pregunta que orienta el capítulo es qué arquitectura permite materializar una plataforma experimental de detección open-vocabulary sobre video en tiempo real conservando modularidad, desacoplamiento, trazabilidad y evaluabilidad dentro del alcance ya definido. El capítulo la responde fijando las responsabilidades de los componentes, los flujos de información, las fronteras entre módulos, los contratos versionados, las interfaces de gobierno y transporte, los escenarios experimentales y los criterios de observabilidad que acompañan la implementación.

#### 17.3.2. Alcance, capacidades y decisiones arquitectónicas

El diseño se formula para un prototipo experimental ejecutado en un entorno local y controlado, y orienta la implementación, la medición y la reconstrucción de resultados sin asumir responsabilidades propias de una solución productiva. Sobre el núcleo validable la plataforma demuestra un flujo completo, medible y trazable desde una fuente visual hasta una alerta asistiva registrada. El objetivo no es ampliar la cantidad de condiciones cubiertas, sino asegurar una base capaz de procesar evidencia visual, publicar eventos, evaluar patrones, registrar alertas y reconstruir resultados experimentales.

El núcleo comprende las capacidades necesarias para operar sobre fuentes controladas, ejecutar inferencia open-vocabulary, versionar prompts, normalizar detecciones, aplicar reglas temporales simples, registrar eventos y producir métricas comparables. El seguimiento multiobjeto formal, las reglas espaciales, las zonas parametrizadas, la preselección liviana en el borde y la adaptación al dominio quedan previstas como extensiones condicionadas que no desplazan la validación inicial ni agregan dependencias al flujo base. La gestión de prompts pertenece al núcleo porque en una plataforma open-vocabulary cada resultado se atribuye a una formulación, una estrategia de detección y un vocabulario activo registrados.

##### 17.3.2.1. Capacidades arquitectónicas requeridas

La arquitectura habilita un conjunto mínimo de capacidades que permiten desarrollar un prototipo medible, trazable y extensible. La enumeración reúne responsabilidades del diseño y no componentes de implementación.

La Tabla 32 declara el régimen de cada capacidad mediante cinco compromisos, cuyo alcance precisa la nota.

**Tabla 32**

*Capacidades arquitectónicas y su tratamiento en el diseño*

| **Capacidad requerida** | **Compromiso** | **Lectura de diseño** |
| --- | --- | --- |
| Gestión y gobierno de la corrida | Núcleo | Debe existir un punto explícito para declarar y congelar la configuración efectiva de cada ejecución, gobernar su ciclo de vida —creación, consulta, cancelación y cierre— y ordenar el disparo entre módulos. |
| Operación sobre fuentes reproducibles | Núcleo | Debe operar sobre imágenes, datasets o videos locales cuya lectura pueda regularse, repetirse y detenerse sin alterar el contenido. Este escenario estabiliza inferencia, contratos, eventos y métricas antes de incorporar captura continua. |
| Operación sobre fuentes en vivo | Complementario previsto | Debe admitir captura o streaming en entorno controlado, donde la fuente continúa evolucionando aunque el procesamiento no sostenga la cadencia, para observar el comportamiento operativo del sistema. |
| Normalización de entrada visual | Núcleo | Cada *frame* debe incluir metadatos de corrida, fuente, orden temporal, resolución y política de muestreo, para compartir el pipeline sin ocultar las diferencias temporales entre fuentes. |
| Inferencia OVD configurable | Núcleo | Debe integrar modelos OVD mediante adaptadores, de modo que puedan sustituirse o compararse sin rediseñar la cadena. |
| Gestión de prompts y vocabulario activo | Núcleo | Debe versionar formulaciones, aliases, estrategias de detección, vocabulario activo y umbrales asociados. |
| Normalización de detecciones | Núcleo | La salida del plano de medios debe expresarse como un contrato de evento de percepción versionado, única unidad de evidencia compartida para interpretar patrones, persistir y releer corridas. |
| Evaluación de patrones de Nivel 1 | Núcleo | Las detecciones positivas deben asociarse espacialmente por sujeto, convertirse en un estado evaluable de ausencia y estabilizarse mediante persistencia temporal e histéresis. |
| Registro de alertas asistivas | Núcleo | Las alertas deben registrarse al confirmarse un patrón, sin constituir un juicio normativo automático. |
| Publicación y persistencia de eventos | Núcleo | La publicación debe desacoplar productores y consumidores sin bloquear la ruta crítica; la persistencia debe conservar un historial de sólo adición que sobreviva a la corrida y permita su relectura. |
| Observabilidad y métricas | Núcleo | La instrumentación debe integrarse al pipeline: cada tramo emite sus mediciones, sin reconstruirlas después desde artefactos que no las registraron. |
| Reporte experimental | Núcleo | Cada corrida debe persistir una síntesis de configuración, resultados y limitaciones, legible sin acceso al sistema en ejecución. |
| Inspección mínima de resultados | Núcleo | Debe ofrecer una interfaz acotada para revisar corridas, alertas, métricas y evidencia, sin convertirse en un tablero operativo. |
| Gestión de evidencia visual controlada | Complementario previsto | Debe admitir clips, *snapshots* o recortes justificados para validación, revisión técnica o comunicación académica. |
| Distribución de alertas confirmadas | Capacidad opcional | Debe convertir alertas confirmadas en intentos de entrega registrados, después del registro interno y fuera del razonamiento del patrón, para que una falla externa no se propague al motor de patrones. |
| Preselección liviana en el rol de captura | Capacidad opcional | Debe reducir carga antes de la inferencia con un preselector conservador: ante falla o incertidumbre, la unidad continúa por el flujo principal; el borde no es fuente de verdad y todo descarte queda visible. |
| Identidad temporal de sujeto | Capacidad opcional | Debe admitir granularidad por sujeto mediante identidad temporal válida. Las métricas formales de seguimiento multiobjeto no condicionan la evaluación del núcleo ni deben confundirse con la capacidad de mantener identidad. |
| Capacidades contextuales y relacionales | Extensión condicionada | Debe prever contexto, razonamiento espacial, zonas, proximidad y evaluadores relacionales para las condiciones de Nivel 2 y Nivel 3, sin bloquear CR-01 y CR-02. Su habilitación exige evidencia e instrumentación adecuadas. |
| Adaptación al dominio (fine-tuning) | Rama comparativa condicionada | Sólo corresponde con una línea base preentrenada congelada, datos suficientes, partición disjunta y criterios de escalamiento fijados antes de los resultados. |

***Nota.*** El compromiso declara el régimen de cada capacidad. «Núcleo» identifica las capacidades necesarias para el flujo base. «Complementario previsto» agrupa las útiles para la validación, la revisión técnica o la comunicación académica. «Capacidad opcional» identifica las que el diseño contempla pero se declaran en la configuración de cada corrida y permanecen deshabilitadas por defecto, de modo que ninguna opere como comportamiento implícito. «Extensión condicionada» identifica las que exigen evidencia e instrumentación adicionales. «Rama comparativa condicionada» refiere a variantes que sólo se incorporan si se cumplen las condiciones metodológicas correspondientes.

##### 17.3.2.2. Requisitos no funcionales de referencia

Las cualidades no funcionales condicionan la validez experimental del prototipo. No alcanza con detectar una condición de riesgo si el sistema no registra la configuración de la corrida, no mide latencia, no conserva trazabilidad o no controla la evidencia visual generada. La Tabla 33 reúne las cualidades que el diseño trata como condiciones arquitectónicas y no como aspiraciones.

**Tabla 33**

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

***Nota.*** Los requisitos no funcionales expresan las cualidades necesarias para preservar la validez experimental del prototipo y aseguran comparabilidad entre corridas, trazabilidad de resultados y control de las decisiones que afectan la latencia, la privacidad, la reproducibilidad o la observabilidad.

##### 17.3.2.3. Decisiones arquitectónicas y principios de lectura

Las decisiones arquitectónicas iniciales no fijan tecnologías concretas y establecen reglas estructurales que se preservan durante el desarrollo del prototipo. La Tabla 34 las reúne alrededor de cuatro ejes. La **separación entre ruta crítica y lógica de control** mantiene la inferencia y la publicación de evidencia perceptiva desacopladas de la evaluación de patrones, la persistencia, los reportes y las notificaciones externas (DA-01, DA-02). La **modularidad por contratos** hace que fuentes, modelos, prompts, detecciones, patrones y métricas se intercambien mediante estructuras explícitas, sin dependencias internas que dificulten la sustitución o la evaluación comparativa (DA-05, DA-12). La **trazabilidad experimental** permite reconstruir toda alerta a partir de la configuración de corrida, los eventos de percepción, el patrón evaluado y las métricas registradas (DA-03, DA-04, DA-13). La **medición desde el diseño** instrumenta tiempos, cadencia efectiva, descartes, errores y estados de patrón desde las primeras corridas, porque forman parte de la validez experimental.

**Tabla 34**

*Decisiones arquitectónicas iniciales*

| **ID** | **Decisión** | **Justificación** |
| --- | --- | --- |
| DA-01 | Separar plano de medios y plano de control. | Protege la ruta crítica de video y desacopla la inferencia de la lógica de interpretación. |
| DA-02 | Publicar evidencia perceptiva como eventos de percepción normalizados. | Permite desacoplar detecciones, patrones, métricas, alertas y persistencia. |
| DA-03 | Separar el gobierno de las corridas, el transporte de eventos durante la ejecución y el repositorio persistente de hechos. | Cada preocupación tiene un régimen propio, porque el gobierno es puntual y de solicitud y respuesta, el transporte es continuo y no debe bloquear la ruta crítica, y la persistencia sobrevive a la corrida para habilitar su relectura. |
| DA-04 | Confirmar patrones mediante persistencia temporal e histéresis. | Reduce alertas generadas por detecciones aisladas, inestables o de corta duración. |
| DA-05 | Integrar modelos OVD mediante adaptadores. | Permite comparar modelos o variantes sin rediseñar la arquitectura general. |
| DA-06 | Admitir granularidad por sujeto mediante identidad temporal opcional, sin convertir las métricas MOT en requisito del núcleo. | Permite evaluar persistencia por persona cuando existe identidad válida y conserva la granularidad de escena como configuración independiente. |
| DA-07 | Tratar la adaptación al dominio como rama comparativa separada y condicionada por datos y protocolo. | Preserva una línea base zero-shot congelada y evita mezclar resultados de una variante ajustada con el núcleo sin entrenamiento. |
| DA-08 | Adoptar minimización visual como criterio ordinario de trazabilidad. | Evita que el almacenamiento indiscriminado de video crudo sea parte del comportamiento base. |
| DA-09 | Separar trazabilidad ordinaria de evidencia visual controlada. | Permite conservar clips, capturas o recortes sólo cuando estén justificados por validación, revisión técnica o comunicación académica. |
| DA-10 | Priorizar DBE antes de EBE. | Estabiliza contratos, inferencia, eventos y métricas antes de incorporar captura continua. |
| DA-11 | Permitir preselección liviana en el rol de captura como variante opcional, conservadora, deshabilitada por defecto y fail-open. | La variante puede reducir carga sin transformar el borde en fuente de verdad ni ocultar descartes, porque el flujo base continúa disponible y comparable. |
| DA-12 | Versionar prompts y vocabulario activo por corrida. | Garantiza la reproducibilidad y comparación entre formulaciones. |
| DA-13 | Registrar toda alerta interna antes de aplicar políticas de supresión o entrega externa. | Preserva la semántica y la medición del episodio; el *cooldown*, la limitación de tasa y la idempotencia pertenecen al tramo de distribución. |

***Nota.*** Las decisiones fijan reglas estructurales adoptadas para el diseño del prototipo experimental. Su materialización y su verificación se documentan en conjunto en la sección 17.4.

A esos cuatro ejes se suma un criterio transversal de **evolución incremental**, por el cual las capacidades condicionadas (DA-06, DA-07, DA-11) se incorporan sin desplazar el núcleo ni convertirse en dependencias del flujo base.

En la adaptación al dominio, esta evolución incremental se expresa como una rama comparativa de carácter exploratorio. El diseño contempla la posibilidad de evaluar variantes ajustadas, pero no fija una receta única ni presupone su adopción. La elección del modelo, del alcance entrenable y de la configuración se concreta durante el desarrollo experimental, bajo las condiciones de la sección 17.1.9. Las variantes ajustadas se mantienen separadas de la línea base sin ajuste de pesos, de modo que la adaptación no se convierta en una dependencia del núcleo.

#### 17.3.3. Vista general y patrones de acople

La plataforma se organiza como una arquitectura lógica por bloques que procesa fuentes de video, genera evidencia perceptiva, evalúa patrones de riesgo y conserva resultados reconstruibles. La vista separa responsabilidades y no prescribe una distribución obligatoria en procesos, servicios o nodos físicos.

El flujo principal parte de fuentes visuales externas, como datasets, videos locales, cámaras o flujos de streaming, y entra al plano de medios por el adaptador de ingesta visual, que encapsula los distintos orígenes bajo una representación común. Desde ese punto se concentra la ruta crítica, que va de la lectura o la captura hasta la publicación de evidencia perceptiva normalizada. El plano no depende de tareas posteriores para continuar procesando unidades visuales. La configuración experimental atraviesa ese flujo y define las condiciones de cada corrida, entre ellas el escenario, el modelo, los prompts activos, los umbrales, las políticas de evidencia y los parámetros de ejecución, sin intervenir en el procesamiento frame a frame.

A partir de los eventos publicados, el plano de control evalúa patrones, administra estados de corrida y registra alertas asistivas internas cuando confirma una condición de riesgo. Las alertas confirmadas viajan por un bus dedicado hacia el módulo de distribución. El ciclo de vida de los tres módulos se gobierna mediante interfaces independientes, que la interfaz de inspección y el orquestador experimental utilizan sin consumir los buses.

La trazabilidad, la observabilidad y la inspección se agrupan en el bloque de soporte experimental, que es una capacidad transversal y no una etapa del flujo frame a frame. Ese bloque conserva evidencia reconstruible, consolida telemetría técnica y permite revisar corridas, métricas, alertas y resultados sin interferir con la ruta crítica. La Figura 4.1 presenta esa organización en una vista lógica de alto nivel. Las flechas sólidas representan el flujo principal de datos y eventos, y las punteadas, la influencia de la configuración o las capacidades de soporte.

**Figura 4.1**

*Vista conceptual de la arquitectura E-OVRT-VDP*

⟦FIGURA: no extraída — ver el .docx⟧

La vista se materializa mediante dos patrones de acople complementarios. El gobierno de las corridas ocurre por interfaces HTTP gobernadas por configuración en los tres módulos ejecutables. Se adopta HTTP porque el ciclo de vida de una corrida, que abarca crear, consultar, cancelar y cerrar, tiene semántica de solicitud y respuesta, admite múltiples clientes sin acoplarlos entre sí y permite disponer los módulos en un mismo host o en hosts distintos sin modificar su lógica. El gobierno por configuración obliga a que cada corrida declare sus parámetros en lugar de heredarlos de constantes ocultas.

El intercambio de datos en ejecución ocurre mediante un bus ZeroMQ con patrón publicador-suscriptor (PUB/SUB) y serialización binaria msgpack, con un canal de detecciones entre los planos y un canal de alertas hacia la distribución. Se adopta ZeroMQ porque ofrece transporte de baja latencia sin requerir un *broker* como dependencia adicional del prototipo, y porque el patrón publicador-suscriptor desacopla al productor de sus consumidores sin bloquear la ruta crítica. msgpack reduce el costo de serialización respecto del texto plano y conserva estructuras autodescriptivas.

La durabilidad no se le exige al canal. Cada hecho se persiste en archivos JSONL de sólo adición antes de publicarse, de modo que la evidencia se pueda releer y reevaluar sin depender de la mensajería. El gobierno fija la configuración y el ciclo de vida, el bus transporta los hechos de ejecución y la persistencia sostiene la relectura sin constituir un tercer patrón de acople.

Esta organización mantiene separados, y coordinados por contratos explícitos, el procesamiento de video, la interpretación de patrones, la distribución de alertas y el análisis experimental.

#### 17.3.4. Configuración experimental, vocabulario y estrategia del núcleo

La configuración experimental concentra las decisiones que gobiernan una corrida y declara de manera explícita y reproducible el escenario, la fuente visual, el modelo OVD, los prompts activos, los umbrales, la política de muestreo, los módulos habilitados, los criterios de patrón, la política de evidencia y la instrumentación de métricas. Al fijarlas antes de la ejecución, separa la definición de las condiciones del procesamiento efectivo de frames y eventos, y permite que cada detección, transición de patrón, alerta interna, métrica o evidencia conservada se asocie con una configuración efectiva de corrida.

Esa separación protege la ruta crítica, porque el pipeline dispone de la configuración efectiva sin consultas externas bloqueantes para decidir qué modelo ejecuta, qué prompts utiliza o qué política de muestreo aplica. También delimita la interpretación posterior de los resultados, ya que una detección sólo resulta experimentalmente útil si puede relacionarse con su fuente, modelo, prompt, umbral, postproceso y patrón evaluado. Sin esa asociación no es posible atribuir diferencias de desempeño a una variable concreta de la corrida.

El gobierno se sostiene sólo si la configuración se resuelve y se valida antes de iniciar la ejecución, de manera que una corrida con declaración incompleta falle al crearse y no produzca artefactos que no puedan atribuirse a una configuración declarada. La configuración alcanza a tres destinatarios. El plano de medios recibe los parámetros que aplica sin diseñarlos ni versionarlos, el plano de control recibe los criterios con los que evalúa y el soporte experimental la utiliza como clave de reconstrucción, de modo que todo evento, métrica, alerta o evidencia conservada pueda rastrearse hasta la corrida que le dio origen.

##### 17.3.4.1. Configuración de corrida como artefacto de reproducibilidad

La configuración de corrida se materializa como un manifiesto de experimento que referencia y congela las configuraciones efectivas de cada componente. El plano de medios, el plano de control y el tramo de distribución tienen ciclos de vida y destinatarios distintos, y una configuración monolítica no tendría un único consumidor ni permitiría reconstruir con precisión qué versión recibió cada servicio.

Se denomina ejecución experimental a la unidad lógica que agrupa las ejecuciones independientes de los componentes que participan en una misma instancia del experimento. Esa unidad se identifica mediante un identificador de experimento (*experiment_id*), mientras que cada componente conserva su propio identificador de corrida. La separación entre ambos niveles permite correlacionar configuraciones, eventos, métricas, alertas, entregas y artefactos bajo una clave común, sin imponer un ciclo de vida único ni una configuración monolítica a los servicios participantes.

El manifiesto declara un *experiment_id*, las referencias a las configuraciones de cada plano, el orden de disparo y los artefactos congelados, entre ellos el modelo, el conjunto de prompts, el conjunto de patrones y la política de distribución. Dos corridas sólo son comparables cuando se conoce qué variable cambió y cuáles permanecieron constantes. La Tabla 35 reúne los elementos mínimos de ese gobierno reproducible.

**Tabla 35**

*Elementos mínimos de la configuración experimental*

| **Elemento configurable** | **Contenido esperado** | **Función arquitectónica** |
| --- | --- | --- |
| Manifiesto de experimento | Versión del manifiesto, fecha, objetivo y referencias a las configuraciones efectivas del plano de medios, del plano de control y del módulo de distribución cuando se habilita. | Gobierna una ejecución experimental sin imponer una configuración monolítica a servicios con ciclos de vida independientes. |
| Identificador de experimento | experiment_id, junto con los identificadores de corrida de cada componente. | Vincula eventos, métricas, errores, alertas, entregas y artefactos de todos los componentes bajo una clave común. |
| Escenario y fuente visual | DBE o EBE; dataset, video local, imagen, cámara o stream; naturaleza temporal; resolución, ritmo esperado, duración y restricciones conocidas. | Distingue fuentes reproducibles, fuentes temporales y fuentes en vivo sin confundir escenario con topología física. |
| Parámetros del pipeline | Resolución de procesamiento, selección o muestreo, criterios de omisión o descarte, tamaño de cola, ritmo esperado y calentamiento. | Condiciona latencia, cobertura temporal, unidades procesadas y lectura de descartes. |
| Modelo OVD | Modelo, versión, checkpoint, *backend*, precisión numérica, dispositivo y adaptador. | Permite sustituir o comparar modelos sin acoplar el resto de la arquitectura. |
| Prompts y vocabulario activo | Conjunto versionado, condición asociada, rol de cada clase, estrategia de formulación y umbral vinculado. | Garantiza trazabilidad entre consulta textual, evidencia producida y configuración. |
| Umbrales y postproceso | Confianza mínima, IoU/NMS, filtros por clase, tamaño, región y normalización de coordenadas. | Define qué salidas crudas se transforman en evidencia perceptiva normalizada. |
| Patrones activos | Condición, severidad, granularidad scene\|subject, ventana de confirmación, histéresis de resolución y criterio de evidencia. | Transforma evidencia puntual en estados y alertas internas por episodio. El cooldown no integra este contrato. |
| Capacidades habilitadas y evidencia | Identidad de sujeto, zonas, preselección en borde, inspección, distribución y política de evidencia visual. | Evita capacidades implícitas y preserva la comparabilidad entre corridas. |
| Política de distribución | Canal, calidad de servicio, idempotencia, supresión de re-notificación, limitación de tasa y retención del ledger. | Concentra los controles de comunicación aguas abajo de la alerta interna. |
| Instrumentación y entorno | Timestamps por tramo, métricas esperadas, estado de aplicabilidad, causa, entorno, librerías y runtime. | Permite calcular o rechazar métricas de forma explícita y reconstruir condiciones de ejecución. |

***Nota.*** La tabla presenta los elementos mínimos del manifiesto y de las configuraciones referenciadas. Los contratos concretos se desarrollan en la sección 17.3.8.

##### 17.3.4.2. Diseño de prompts y vocabulario activo

El diseño de prompts expresa las condiciones de riesgo como consultas consumibles por un modelo OVD. La sección 17.1.5.3 estableció la sensibilidad de estos modelos a la formulación de la consulta y fijó el inglés como idioma primario del vocabulario, de modo que aquí sólo se fija la consecuencia arquitectónica. La consulta textual incide sobre la evidencia perceptiva generada, y por eso se registra, se versiona y se mantiene trazable hasta los resultados que contribuye a producir.

Cada prompt se asocia a una condición de riesgo, un texto de consulta, una estrategia de formulación, una versión y un conjunto de prompts activos. Una modificación de redacción se registra como variante experimental y no como reemplazo informal, de manera que pueda explicarse qué formulación produjo una detección y compararse resultados sin perder el vínculo con la condición original.

El vocabulario activo es el conjunto de prompts habilitados en una corrida. Su tamaño y su composición afectan el comportamiento semántico del detector y, según el modelo, el costo de inferencia. Por eso el núcleo validable trabaja con un vocabulario reducido y controlado, suficiente para evaluar la sensibilidad de formulación y sin listas amplias que dificulten atribuir resultados.

Un prompt y una estrategia de detección no son lo mismo. Un prompt es una consulta semántica, mientras que una estrategia puede combinar prompts, postproceso, evidencia indirecta o reglas espaciales.

##### 17.3.4.3. Vocabulario y estrategia del núcleo validable

El diseño inicial distingue el vocabulario positivo del núcleo, los conjuntos de las ramas comparativas y el vocabulario condicionado de las condiciones de mayor complejidad. Para CR-01 y CR-02 el núcleo utiliza person, helmet y vest, donde la primera categoría identifica la entidad sujeto y las restantes representan los elementos de protección cuya presencia se evalúa espacialmente respecto de cada persona.

La ausencia de casco o chaleco no se formula como consulta principal del núcleo. Se infiere en el plano de control cuando existe evidencia suficiente de una persona y no se encuentra evidencia del EPP correspondiente dentro de la región configurada. Las consultas negativas o de estado observable se mantienen en conjuntos separados para las estrategias directa (E-DIR) e híbrida (E-HYB) definidas en la consolidación metodológica, de modo que sus resultados sean atribuibles a una estrategia explícita y no a una mezcla informal de vocabularios.

Para el núcleo validable se adopta la estrategia indirecta con inferencia espacial de ausencia (E-IND). La frontera que esa elección fija es explícita. El plano de medios informa qué entidades observó, dónde y con qué confianza. El plano de control decide si la evidencia del elemento de protección se asocia al sujeto, construye el estado evaluable de la condición y lo estabiliza antes de registrar una alerta.

La estrategia se adopta por auditabilidad, porque cada evaluación puede reconstruirse a partir de la caja del sujeto, la región analizada, las detecciones de protección, los umbrales y la regla aplicada, y así la ausencia no se presenta como una conclusión opaca del modelo. La detección directa (E-DIR) y las variantes híbridas (E-HYB) se conservan como ramas comparativas configurables, con conjuntos de prompts y reglas identificados por separado, y comparten los contratos de publicación, evaluación temporal y registro, de modo que la comparación no requiera alterar la arquitectura central.

CR-03 y CR-04 conservan consultas compuestas y descompuestas de carácter condicionado, porque su confirmación requiere contexto espacial adicional. CR-05 y CR-06 se expresan mediante entidades componentes, ya que la condición completa depende de proximidad, seguimiento o zonas declaradas externamente. La Tabla 36 organiza el vocabulario del núcleo y de las ramas comparativas, y el catálogo completo de formulaciones candidatas por condición y estrategia se consolida en el Anexo C.

**Tabla 36**

*Vocabulario de prompts en inglés del núcleo validable y de las ramas comparativas*

| **Condición y estrategia** | **Rol de la consulta** | **Consulta o categoría candidata** | **Uso previsto** |
| --- | --- | --- | --- |
| CR-01 y CR-02 — núcleo E-IND | Entidad sujeto | person | Localizar las personas sobre las cuales se evalúa la presencia o ausencia espacial del EPP. |
| CR-01 — núcleo E-IND | Evidencia positiva de EPP | helmet | Detectar casco asociable a una persona. La ausencia se infiere en el plano de control. |
| CR-02 — núcleo E-IND | Evidencia positiva de EPP | vest | Detectar chaleco asociable a una persona. La ausencia se infiere en el plano de control. |
| CR-01 — rama E-DIR | Ausencia o estado observable | bare_head; “person without hard hat”; “construction worker without safety helmet”; “person with *bare head* on construction site” | Comparar formulaciones directas bajo una configuración independiente del núcleo. |
| CR-02 — rama E-DIR | Ausencia o descripción visual | “person without reflective vest”; “worker without high-visibility vest”; “person without bright colored safety clothing” | Comparar formulaciones directas o atributivas bajo una configuración independiente del núcleo. |

***Nota.*** El vocabulario del núcleo validable está compuesto por person, helmet y vest. Las formulaciones directas pertenecen a ramas comparativas independientes y el vocabulario condicionado de CR-03 a CR-06 se consolida en el Anexo C. Cada corrida conserva prompt_set_id, de modo que toda detección pueda atribuirse al conjunto que la produjo.

##### 17.3.4.4. Reglas de comparabilidad entre configuraciones

La configuración permite comparar variantes sin producir conclusiones ambiguas. Al comparar prompts se mantienen constantes el modelo, la fuente visual, la resolución, la política de muestreo, los umbrales, el postproceso y los criterios de patrón, de modo que una variación de desempeño pueda atribuirse a la formulación evaluada. Al comparar modelos OVD se conserva el mismo conjunto de prompts y condiciones equivalentes de fuente, resolución y postproceso, y si un modelo requiere umbrales distintos por la escala de sus puntajes, esa diferencia se declara como parte de la configuración y no se oculta como detalle de implementación.

Al comparar DBE y EBE se declara que cambia la naturaleza temporal de la fuente. En EBE intervienen la captura continua, la variabilidad de iluminación, la codificación o decodificación cuando corresponda, la continuidad temporal, las omisiones, los descartes y la disponibilidad efectiva de frames, de modo que las diferencias observadas no se atribuyan automáticamente al detector OVD.

Por la misma razón, ningún módulo opcional opera como comportamiento implícito. La evidencia visual, la identidad temporal, las zonas, la preselección en el rol de captura y la distribución externa se habilitan en la configuración de la corrida, porque una activación silenciosa alteraría la interpretación de la latencia, la cobertura temporal, la privacidad y la aplicabilidad de las métricas. Es esa referencia declarada, y no una reinterpretación posterior de los artefactos, la que permite atribuir una diferencia de resultados a la variante evaluada y no a un cambio no declarado en la cadena.

#### 17.3.5. Diseño conceptual del plano de medios

El plano de medios se materializa en el componente lógico Pipeline de Medios, que concentra la ruta sensible a la latencia. Comienza cuando el adaptador de ingesta visual recibe, lee o decodifica una unidad visual proveniente de una fuente externa y termina cuando publica evidencia perceptiva normalizada hacia la frontera de integración. Su alcance abarca ingesta, decodificación cuando corresponda, control de ritmo, normalización visual, inferencia open-vocabulary, postproceso y publicación no bloqueante.

El límite del componente es estricto. El Pipeline de Medios no confirma condiciones de riesgo, no asigna severidad, no ejecuta reglas de patrón, no genera alertas y no depende de persistencia pesada para continuar procesando frames. Su salida es evidencia perceptiva primaria asociada a una corrida, una fuente, una referencia temporal, un modelo y una configuración de procesamiento, y su interpretación corresponde al plano de control.

Las fuentes utilizadas en DBE y EBE ingresan por una misma frontera conceptual, el adaptador de ingesta visual, y la diferencia entre escenarios se resuelve en la forma de lectura, la disponibilidad del frame, los metadatos temporales y el control de ritmo, no en la salida del plano. En DBE predomina la lectura reproducible. En EBE pueden aparecer irregularidades temporales, atraso acumulado, variabilidad de captura o disponibilidad de frames recientes. En ambos casos la salida conserva trazabilidad suficiente para reconstruir qué se procesó, bajo qué configuración y con qué resultado. La Figura 4.2 representa ese flujo interno. Las fuentes visuales son externas al plano, que comienza en el adaptador de ingesta visual, responsable de recibir, leer o decodificar la fuente y transformarla en una unidad visual procesable. La configuración de corrida parametriza la ejecución como entrada transversal, sin formar parte del procesamiento frame a frame. El evento de percepción normalizado se ubica por fuera del recuadro para señalar la frontera de salida hacia el bus interno de eventos y el plano de control.

**Figura 4.2**

*Flujo conceptual del Pipeline de Medios*

⟦FIGURA: no extraída — ver el .docx⟧

##### 17.3.5.1. Flujo operativo del Pipeline de Medios

El flujo interno se organiza como una cadena de transformación progresiva. Cada etapa recibe una representación visual o perceptiva, aplica una operación acotada y entrega una salida que mantiene relación con la corrida y con la referencia temporal original, de modo que fuentes, modelos o políticas de procesamiento puedan sustituirse sin modificar la responsabilidad general del plano.

**Ingesta y decodificación.** La primera responsabilidad interna del plano es recibir la entrada visual desde fuentes externas, como datasets, imágenes, videos locales, cámaras o streams. La fuente queda encapsulada por un adaptador de ingesta visual que oculta diferencias de formato sin eliminar información relevante para la evaluación. Cuando la entrada proviene de video codificado o de streaming, la decodificación convierte el flujo en frames procesables y registra la información necesaria para distinguir disponibilidad, recepción, orden lógico y referencia temporal. En DBE suele alcanzar con conservar el índice de secuencia y el orden de lectura. En EBE puede ser necesario registrar además timestamps de captura o recepción, irregularidad temporal y descartes por atraso.

**Control de ritmo y selección de unidades visuales.** Antes de ingresar a inferencia, el pipeline decide qué unidades visuales se procesan. La decisión puede aceptar todos los frames, aplicar una selección determinista, reducir la frecuencia de procesamiento o priorizar unidades recientes cuando existe captura continua. La política se declara por corrida, porque cambiar la selección de unidades, la frecuencia de procesamiento o el criterio de omisión equivale a cambiar la variante experimental evaluada. Lo que el diseño exige no es una política concreta sino la ausencia de decisiones invisibles, de manera que toda unidad omitida, reemplazada o descartada quede asociada a una causa y a una política declarada.

En corridas DBE, o con fuentes cuya lectura puede regularse, la prioridad es preservar reproducibilidad, orden lógico y trazabilidad de las unidades procesadas, y si no se procesan todos los frames la selección es determinista y se mantiene constante entre corridas comparables. En corridas EBE, o con fuentes en vivo, la prioridad es que el atraso acumulado no crezca indefinidamente y que toda omisión, irregularidad temporal o descarte quede registrada. El resultado esperado no es maximizar la cadencia de forma aislada sino hacer interpretable el comportamiento del pipeline, porque un sistema que procesa menos frames puede ser válido para una corrida exploratoria y esa reducción debe ser visible para no confundir rendimiento con cobertura temporal.

**Normalización visual**. El frame aceptado se adapta a los requisitos del modelo seleccionado. Esta etapa puede modificar resolución, formato, espacio de color, disposición de tensores o escala de entrada. El diseño preserva la relación entre coordenadas originales y coordenadas de inferencia, porque esa relación permite interpretar cajas delimitadoras, revisar evidencia visual y comparar resultados entre configuraciones con distinta resolución. Reescalado, recortes o relleno de bordes no deben tratarse como operaciones invisibles.

**Inferencia open-vocabulary.** La inferencia ejecuta el detector configurado sobre la entrada normalizada y el conjunto de prompts activos. El modelo se integra mediante un adaptador para evitar que el resto del plano dependa de la salida particular de un detector concreto. Esta etapa produce resultados crudos, como cajas, puntajes, etiquetas o frases asociadas, según el formato propio del detector utilizado. Cuando el modelo lo permita, el adaptador puede reutilizar representaciones textuales precalculadas o mecanismos equivalentes para reducir el costo de inferencia, siempre que esa optimización no altere la trazabilidad de la corrida.

**Postproceso y normalización de detecciones.** Luego de la inferencia, el pipeline aplica los filtros definidos por la configuración de corrida, entre ellos umbrales, supresión de detecciones redundantes, normalización de etiquetas y remapeo de coordenadas, para convertir las salidas del modelo en evidencia perceptiva común. Esa salida queda asociada al frame, al prompt, a la condición y al nivel de confianza correspondiente. No interpreta riesgo ni genera alertas, y sólo entrega evidencia normalizada al plano de control.

**Publicación de evidencia perceptiva.** La publicación cierra el plano de medios. La evidencia normalizada se entrega como evento liviano hacia la frontera de integración, asociada a la corrida, la fuente, la referencia temporal, el modelo, los prompts y los timestamps relevantes. A partir de ese punto la evidencia puede evaluarse en el plano de control, persistirse de manera reconstruible o inspeccionarse desde el soporte experimental, y ninguna de esas tareas es requisito para que el pipeline continúe con la siguiente unidad visual.

En consecuencia, la salida del plano de medios no se reduce a cajas y puntajes sin contexto y tampoco incorpora severidad, confirmación de patrón ni decisión de alerta. Su producto es evidencia visual primaria, normalizada y trazable, cuya interpretación corresponde al plano de control.

Sobre esa cadena el diseño mantiene una ruta no bloqueante. Si el bus interno, la persistencia, la inspección o una salida externa fallan o se saturan, esa condición se registra como parte de la ejecución y no convierte a esos consumidores en dependencia directa del procesamiento visual. El plano hace visible además la variabilidad temporal, porque una latencia aparentemente baja puede ocultar pérdida de frames, colas saturadas o reemplazo de frames antiguos por frames recientes, y por eso registra timestamps por tramo, profundidad de cola cuando corresponde, frames aceptados, frames omitidos y descartes.

Los adaptadores absorben la heterogeneidad de los detectores OVD, que difieren en formato de entrada, tipo de prompt, estructura de salida, semántica de puntajes y costo de inferencia, y entregan una evidencia perceptiva estable que no acopla al plano de control con un modelo específico ni con los detalles internos de su implementación. La persistencia temporal de un patrón, la histéresis, la severidad y el registro interno de la alerta pertenecen al motor de patrones, de modo que el plano de medios pueda mejorar la calidad de la evidencia perceptiva sin decidir si una condición observada se convirtió en una situación de riesgo confirmada.

##### 17.3.5.2. Capacidades opcionales y degradación segura

El núcleo validable del plano de medios opera sin seguimiento multiobjeto formal, sin preselección en borde y sin adaptación de modelos al dominio. Estas capacidades se incorporan como variantes del flujo, no son requisito para demostrar el procesamiento de CR-01 y CR-02 y no modifican el contrato de salida. La preselección en borde se adopta bajo un criterio de degradación segura, denominado *fail-open*, por el cual una falla o una decisión incierta del preselector conserva la unidad visual para el flujo principal. La variante puede descartar carga y nunca ser causa de pérdida de evidencia.

El seguimiento puede ubicarse después del postproceso cuando resulte necesario estabilizar entidades, reducir oscilaciones entre frames o entregar identificadores temporales al plano de control. Un identificador temporal no equivale a una condición de riesgo sostenida.

Las variantes orientadas a eficiencia reciben el mismo tratamiento. Las reducciones de resolución, los cambios de modo de inferencia o las exportaciones a motores optimizados corresponden a la implementación, y cualquier variante que altere la ruta frame-evento se declara en la configuración de corrida.

#### 17.3.6. Diseño conceptual del plano de control

El plano de control interpreta la evidencia perceptiva producida por el plano de medios. Su responsabilidad comienza cuando ingresa un evento de percepción normalizado y termina cuando el sistema registra estados de patrón, alertas internas, eventos persistibles, métricas y salidas de inspección o distribución desacopladas. A diferencia del Pipeline de Medios no procesa frames crudos ni opera al ritmo constante de captura, porque trabaja sobre eventos y sobre cambios de estado derivados de reglas configuradas.

La separación entre detección, patrón y alerta es su decisión arquitectónica central. Una detección puntual expresa una observación del modelo sobre una unidad visual. Un patrón confirmado expresa que esa evidencia fue evaluada durante una ventana temporal bajo criterios explícitos de persistencia, umbral e histéresis. Una alerta interna registra un episodio asistivo generado por una transición válida del patrón. El plano no transforma cada detección en una alerta, sino que estabiliza la evidencia antes de producir salidas operativas.

Esa organización evita que la variabilidad propia de la inferencia OVD, con sus falsos positivos, falsos negativos, fluctuación de puntajes, sensibilidad al prompt u oclusiones parciales, se traslade directamente al sistema de alertas. También mantiene al plano de medios aislado de consumidores lentos, persistencia histórica, reportes, notificaciones externas o interfaces de inspección, que el plano de control ejecuta de forma asíncrona.

En el alcance del prototipo el plano de control se orienta al núcleo validable. Para CR-01 y CR-02 la evaluación se resuelve mediante persistencia temporal simple y estados de patrón, sin exigir seguimiento multiobjeto formal. El seguimiento, las zonas espaciales y las reglas relacionales enriquecen escenarios posteriores y no son dependientes del núcleo validable.

El plano recibe evidencia perceptiva normalizada, selecciona los patrones activos, evalúa la evidencia espacial y temporal, administra el estado de cada patrón y registra una alerta interna cuando confirma un episodio, mientras persiste transiciones, métricas y errores. La evaluación no ejecuta inferencia visual, no asigna identidad personal y no determina cumplimiento normativo, porque aplica reglas declaradas de asociación espacial, persistencia, granularidad e histéresis. La alerta interna que sigue a la confirmación es el hecho principal del sistema y precede a cualquier notificación.

##### 17.3.6.1. Máquina de estados y ciclo del episodio

La máquina de estados distingue inactivo (*inactive*), candidato (*candidate*), confirmado (*confirmed*), sostenido (*sustained*) y resuelto (*resolved*). Una evidencia inicial abre el estado candidato. La confirmación ocurre cuando la condición satisface la ventana temporal y los umbrales declarados. La continuidad mantiene el episodio y la ausencia sostenida durante la histéresis lo resuelve.

La transición a confirmed registra una alerta interna por episodio. El estado sostenido actualiza duración y evidencia sin convertir cada frame positivo en una alerta nueva. Una nueva confirmación posterior se conserva como re-alerta y se evalúa por separado de los falsos positivos.

Las ventanas se expresan en milisegundos y no en frames, de modo que la semántica temporal no cambie con la cadencia de procesamiento. Los valores adoptados para los patrones del núcleo se documentan junto con la configuración efectiva en la sección 17.4.4.

El ciclo de evaluación selecciona evidencias, actualiza la memoria, aplica la ventana de confirmación y la histéresis, registra la transición y conserva la causa. Los descartes de fuente, los huecos temporales y la pérdida de identidad se distinguen de la ausencia real de evidencia. La confirmación representa el cumplimiento de una regla interna bajo la configuración de la corrida y no constituye certificación normativa ni decisión automática de intervención. La Figura 4.3 representa el ciclo de vida temporal de un patrón de riesgo en el plano de control. La condición observada abre el estado candidate y, cuando la evidencia satisface la ventana de confirmación configurada, el patrón pasa a confirmed y se registra la alerta interna correspondiente. Mientras la condición permanece activa el patrón evoluciona a sustained. Cumplida la ventana de resolución, el episodio pasa a resolved y retorna a inactive. Si la evidencia inicial resulta insuficiente o no persiste durante la ventana de confirmación, el patrón vuelve a inactive sin generar una alerta.

**Figura 4.3**

*Máquina de estados del motor de patrones*

⟦FIGURA: no extraída — ver el .docx⟧

##### 17.3.6.2. Motor de evaluación y definición de patrón

El motor de evaluación es el componente lógico del plano de control que transforma evidencia perceptiva normalizada en estados de patrón, episodios y alertas internas. No procesa imágenes ni ejecuta inferencia OVD. Consume los eventos publicados por el plano de medios, consulta las definiciones activas de patrón declaradas en la configuración experimental y actualiza el estado correspondiente dentro de la corrida.

El motor admite el catálogo completo de patrones del prototipo y su activación efectiva depende de la configuración de corrida, los módulos habilitados y la disponibilidad de evidencia suficiente, de modo que la arquitectura pueda incorporar patrones de mayor complejidad sin modificar la lógica central del plano de control.

El motor no evalúa condiciones de riesgo aisladas, sino patrones activos que las operacionalizan durante una corrida. La condición identificada mediante CR-01 a CR-06 conserva el significado semántico del fenómeno observable, y el patrón correspondiente, identificado mediante PR-01 a PR-06, establece la regla con la que ese fenómeno se convierte en un estado evaluable. La separación permite modificar la estrategia de evidencia, la granularidad o el comportamiento temporal sin alterar el catálogo de condiciones de riesgo.

Cada patrón se declara mediante configuración y reúne, como una única definición evaluable, los criterios necesarios para admitir evidencia, mantener estado y producir una salida trazable, de modo que la lógica del motor no dependa de reglas particulares incorporadas de manera rígida en el código. La definición comprende siete elementos.

**Identidad y vínculo semántico**. El código y la versión del patrón lo relacionan con una condición de riesgo determinada. Esta asociación permite reconstruir qué regla evaluó la evidencia y bajo qué definición, sin confundir el fenómeno observable con su tratamiento operativo.

**Evidencia admisible.** El patrón especifica qué detecciones o relaciones pueden intervenir en la evaluación. En el núcleo, el motor utiliza detecciones positivas de person y del elemento de protección correspondiente, helmet o vest, y determina su presencia o ausencia mediante asociación espacial. La condición de riesgo no se deriva de una detección negativa opaca.

**Granularidad y región de evaluación.** La granularidad scene mantiene el estado por patrón y fuente, mientras que subject lo mantiene además por identidad temporal de sujeto. Cuando la condición depende de un elemento asociado a la persona, el patrón también declara la región relativa de la caja donde se busca la evidencia, que es la región cefálica para PR-01 y el torso para PR-02.

**Precondiciones de evidencia**. La definición establece los requisitos mínimos que deben satisfacer el sujeto y el elemento de protección para contribuir al patrón, como confianza y área del sujeto. Estos criterios se aplican sobre la evidencia ya normalizada por el plano de medios y evitan que detecciones insuficientes modifiquen el estado temporal.

**Regla temporal e histéresis**. El patrón declara una ventana de confirmación que exige evidencia sostenida antes de registrar la condición y una ventana de resolución que impide cerrar el episodio ante pérdidas breves, oclusiones o fluctuaciones del detector. Ambas se expresan en milisegundos para que su significado no dependa de la cadencia de procesamiento.

**Severidad y dependencias opcionales**. La severidad proviene del catálogo metodológico y permanece asociada al patrón durante la corrida. Las capacidades adicionales —identidad temporal, zonas o relaciones entre entidades— sólo intervienen cuando fueron habilitadas explícitamente y existe evidencia suficiente para utilizarlas.

**Estado y salida observable.** A partir de los criterios anteriores, el motor actualiza el estado del patrón y registra las transiciones correspondientes. Cuando la evidencia satisface la regla de confirmación, produce la alerta interna y los eventos necesarios para reconstruir posteriormente la evaluación.

La granularidad de la memoria temporal es un parámetro explícito de la definición de patrón. Bajo granularidad de escena el estado se indexa por (patrón, fuente) y evalúa la continuidad de la condición en la escena. Bajo granularidad de sujeto se indexa por (patrón, fuente, identidad) y exige una identidad temporal válida.

La granularidad de sujeto sólo puede utilizar una identidad producida por un componente de seguimiento o por un decorador equivalente del plano de control, porque el identificador de detección no vale entre frames. La capacidad se habilita por configuración sin modificar el contrato de percepción, y la identidad resultante se conserva en los artefactos del control y no en el registro ordinario del plano de medios.

La granularidad de escena sostiene una afirmación precisa, que es la persistencia de la condición en la escena. No permite concluir que el mismo sujeto sostuvo el riesgo durante toda la ventana, porque una rotación de personas podría mantener la condición de forma continua. Esa segunda afirmación requiere granularidad de sujeto.

La exclusión de las métricas formales de seguimiento multiobjeto no elimina esta capacidad, porque la arquitectura separa la identidad necesaria para indexar el estado del patrón de la evaluación formal del desempeño de seguimiento.

El motor respeta la clasificación metodológica de condiciones por nivel de complejidad. Desde el diseño arquitectónico, esa clasificación se traduce en requisitos de evaluación distintos, porque algunos patrones se resuelven con evidencia perceptiva y persistencia temporal simple y otros sólo se activan cuando la corrida habilita insumos adicionales como seguimiento, zonas parametrizadas o reglas espaciales.

Esa diferenciación permite diseñar un motor único sin sobredimensionar el prototipo experimental, con una lógica común de evaluación que adapta sus entradas y criterios según el patrón activo y la configuración de corrida. La Tabla 37 reúne las dependencias arquitectónicas de cada patrón y su tratamiento en el prototipo.

**Tabla 37**

*Diseño del motor de patrones según condición de riesgo*

| **Patrón y condición asociada** | **Evidencia y regla de evaluación** | **Dependencias arquitectónicas** | **Tratamiento en el prototipo** |
| --- | --- | --- | --- |
| PR-01 / CR-01 — Persona sin casco | Detecciones positivas de person y helmet, con evaluación de la región cefálica por sujeto. | Eventos de percepción, coordenadas comparables y referencia temporal. La granularidad de sujeto requiere identidad temporal válida; la de escena no. | Núcleo validable. Produce estados candidato, confirmado, sostenido y resuelto, además de una alerta interna trazable por episodio. |
| PR-02 / CR-02 — Persona sin chaleco reflectivo | Detecciones positivas de person y vest, con evaluación de la región del torso por sujeto. | Eventos de percepción, coordenadas comparables y referencia temporal. Comparte la misma frontera contractual que PR-01. | Núcleo validable. Se evalúa mediante la misma cadena arquitectónica, con severidad y ventanas propias. |
| PR-03 / CR-03 — Trabajo en altura sin anticaídas visible | Persona en altura o sobre estructura elevada junto con ausencia o baja evidencia de sistema anticaídas visible. | OVD sobre entidades o atributos, reglas espaciales intra-frame y evidencia visual suficiente del escenario. | Extensión condicionada. No bloquea el núcleo; sólo debe activarse si existen datos o escenas que permitan evaluar la condición completa. |
| PR-04 / CR-04 — Borde elevado desprotegido con personas próximas | Borde, plataforma o zona elevada sin protección colectiva, con personas próximas. | OVD de entidades del entorno, reglas espaciales, posible parametrización de regiones y cámara con perspectiva adecuada. | Extensión condicionada. Puede reportarse parcialmente si sólo se detectan componentes visuales sin validar la condición completa. |
| PR-05 / CR-05 — Maquinaria cerca de peatones | Maquinaria y personas con relación de proximidad sostenida. | OVD de entidades, seguimiento temporal o asociación equivalente, reglas de proximidad y métricas de continuidad. | Condicionado a módulo contextual. No pertenece al núcleo; requiere instrumentación temporal y control de falsos positivos relacionales. |
| PR-06 / CR-06 — Persona en zona restringida | Persona dentro de un polígono o zona definida externamente. | Cámara fija o geometría controlada, polígono de zona, OVD de persona y, preferentemente, tracking o asociación temporal. | Condicionado a escenario EBE controlado o fuente fija. Requiere parametrización explícita de zona en la configuración de corrida. |

***Nota.*** La tabla declara las dependencias arquitectónicas de cada patrón y el tratamiento que recibe en el prototipo. El tratamiento «núcleo validable» identifica los patrones obligatorios del prototipo experimental. El tratamiento «extensión condicionada» indica capacidades previstas que sólo deben habilitarse cuando existan datos, módulos e instrumentación suficientes. Las reglas de evidencia, la severidad y los rangos de persistencia de cada patrón se establecen en la sección 17.1.5.2.

La salida principal del motor no es una alerta aislada, sino una secuencia de eventos derivados que describen el ciclo de vida del patrón, desde el inicio del candidato hasta la confirmación, el sostenimiento y la resolución o el descarte por evidencia insuficiente. La alerta interna se registra sólo cuando una transición válida confirma el patrón, lo que evita emitir alertas por cada frame positivo y permite analizar episodios con inicio, duración, evidencia causal y cierre.

Cada transición conserva trazabilidad suficiente para explicar su origen, con la configuración de corrida, el patrón evaluado, la condición asociada, la evidencia considerada, la ventana temporal, los umbrales aplicados, el estado previo, el estado nuevo y la referencia temporal. Esa información permite reconstruir por qué se generó una alerta, por qué se resolvió un episodio, qué evidencia se descartó y qué parámetros condicionaron el resultado.

##### 17.3.6.3. Transporte, persistencia y trazabilidad experimental

La arquitectura diferencia el canal de transporte del repositorio persistente, de modo que la durabilidad no se atribuya a un mecanismo de mensajería diseñado para baja latencia. El repositorio es la fuente de verdad. Cada evento de percepción se escribe en un archivo JSONL de sólo adición antes de publicarse, y los cambios de estado, las alertas, las métricas y los errores siguen la misma regla en sus componentes respectivos. Si el canal falla, el hecho persistido permanece disponible para relectura.

En el camino de ejecución en vivo el canal adopta ZeroMQ con patrón publicador-suscriptor, msgpack, tópicos por tipo de evento y un número de secuencia monótono dentro del envoltorio versionado del bus. El plano de control consume ese contrato por el canal de detecciones y no interpreta formatos propios de un detector ni recibe frames crudos. El *payload* publicado corresponde al mismo contenido lógico persistido, de manera que la corrida pueda releerse por el camino diferido sin redefinir la evidencia.

Todo consumidor se suscribe antes de que su productor publique, y el orquestador verifica esa precondición al crear la corrida, porque la respuesta de creación de un consumidor implica su disponibilidad, y cuando un consumidor se crea después de su productor, como ocurre con el módulo de distribución, es el publicador el que retiene la emisión hasta que exista un suscriptor. El orden efectivo de arranque de los módulos se documenta en la sección 17.4.

La pérdida se detecta mediante huecos de secuencia. Un hueco incrementa *bus_dropped_events*, degrada la corrida y queda expuesto en el reporte, y nunca se interpreta como ausencia de evidencia en la escena.

El cierre de la corrida se propaga mediante un evento de ciclo de vida cuyo hito de finalización delimita el final lógico y permite cerrar consumidores, consolidar artefactos y distinguir un fin normal de una interrupción.

La frontera contractual no depende de que el transporte utilice o no un broker, porque la durabilidad, la reevaluación y la causalidad se sostienen en la regla de persistir antes de publicar y en los esquemas versionados.

##### 17.3.6.4. Cadena de traducción entre condición, evidencia, patrón y alerta

La cadena que va de la condición observable hasta la alerta atraviesa los dos planos. La condición del catálogo metodológico define qué fenómeno se monitorea, la estrategia de detección establece si la evidencia se busca mediante un prompt directo, una combinación de consultas, evidencia auxiliar o reglas contextuales, el plano de medios publica evidencia perceptiva normalizada y el plano de control la evalúa mediante el patrón correspondiente. Cuando la evaluación confirma el episodio, registra una alerta interna, que es una salida asistiva del sistema y no equivale a una notificación externa ni a una certificación normativa. La Figura 4.4 muestra cómo una condición definida metodológicamente se materializa en la arquitectura. La estrategia orienta la producción de evidencia en el plano de medios, el patrón la evalúa en el plano de control y la alerta interna registra el episodio confirmado.

**Figura 4.4**

*Cadena de traducción entre condición, estrategia, evidencia, patrón y alerta*

⟦FIGURA: no extraída — ver el .docx⟧

#### 17.3.7. Distribución de alertas confirmadas

La alerta interna es el hecho terminal del plano de control y todavía no es un aviso. El tramo de distribución la convierte en intentos de entrega registrados sin participar del razonamiento que la produjo.

El plano de control publica cada alerta confirmada en un bus de alertas dedicado, y el módulo de distribución la consume desde allí, aplica la política de notificación y registra el resultado de cada intento. No constituye un tercer plano ni un cuarto rol funcional, sino un módulo desacoplado, y esa condición es la que impide que la indisponibilidad de un canal externo se propague al motor de patrones.

El pipeline de distribución comprende una fuente de alertas, una política de notificación, un sobre versionado, un adaptador de canal y un *ledger* de entregas. La misma lógica admite la relectura desde artefactos persistidos y el consumo en vivo desde el bus de alertas, sin modificar la semántica de la alerta de entrada.

La política ordinaria prioriza trazabilidad, idempotencia y operación no bloqueante. Una falla del canal genera un resultado de entrega y un error interpretable, y no invalida ni elimina la alerta interna. Toda notificación externa es una salida derivada de la alerta interna y se mide por separado.

El tramo separa el dato del gobierno. Las alertas confirmadas llegan por el bus de alertas en sentido único desde el plano de control, mientras que las órdenes de ciclo de vida llegan por una interfaz de gobierno propia del módulo, que permite crear, consultar, cancelar y descartar corridas de entrega. Para la relectura diferida el módulo conserva una entrada offline sobre alertas persistidas, y ambos caminos utilizan los mismos contratos de alerta interna, sobre de notificación y registro de entrega, por lo que la modalidad de ejecución no modifica la semántica de la alerta ni la del resultado.

La Tabla 38 distingue los consumidores del evento confirmado. Ninguno puede modificar retrospectivamente el patrón, la alerta interna o su referencia temporal.

**Tabla 38**

*Consumidores y salidas del tramo de distribución*

| **Consumidor o salida** | **Uso previsto** | **Tratamiento arquitectónico** |
| --- | --- | --- |
| MQTT QoS 1 | Publicar el sobre de notificación y esperar confirmación de entrega del broker. | Canal de entrega mediante adaptador; el resultado queda asentado como registro de entrega. |
| Interfaz de inspección | Mostrar alerta, política aplicada, intento y resultado de entrega. | Proyección de consulta; no consume el bus de percepción ni confirma patrones. |
| Reporte experimental | Consolidar conteos por resultado de entrega, errores y latencia del tramo. | Se calcula desde el ledger y se mantiene separado de las métricas de alerta interna. |
| Relectura DBE | Distribuir alertas ya persistidas de una corrida. | Debe ser idempotente: reprocesar el mismo evento no duplica entregas. |
| Canales adicionales | Correo, webhook u otras integraciones futuras. | Punto de extensión por adaptador; no forma parte del núcleo ni altera los contratos existentes. |

***Nota.*** El módulo de distribución conserva su propio estado operativo y su ledger, y no utiliza el almacenamiento continuo de video ni requiere acceso a frames crudos.

El conjunto de patrones adoptado no suprime confirmaciones, porque cada alerta interna se registra para conservar la dinámica real del episodio. La decisión es deliberada. El motor dispone de control de re-confirmación por patrón y sujeto y el núcleo lo deja inactivo, ya que un motor que suprimiera dejaría de reflejar la duración del episodio y no permitiría distinguir una condición que persiste de una que se resolvió.

La supresión de re-notificación se reubica en la política del módulo de distribución y, al reubicarse, cambia de granularidad. El motor la aplicaría por patrón y sujeto, mientras que la política de entrega aplica una ventana de silencio por condición y fuente, porque para una notificación asistiva lo relevante es que esa condición en esa cámara ya fue avisada. La agrupación de avisos y la limitación de tasa quedan como punto de extensión de la política. Una alerta suprimida para comunicación existió y continúa siendo medible, y las re-alertas de un episodio activo se informan por separado y no se computan como falsos positivos, de modo que una decisión de comunicación no altere la precisión del motor.

El ledger de entregas es de sólo agregado, aplica una clave de idempotencia por notificación y canal y acumula entre corridas, de manera que un reprocesamiento no vuelva a entregar lo ya entregado. Cada fila conserva el número de intento, la marca temporal, el resultado, el motivo de error y la confirmación del canal, y distingue entrega exitosa, supresión por política, descarte por duplicado, falla de un intento y descarte definitivo por agotamiento de reintentos. Cada fila registra además la modalidad en que se midió la latencia del tramo, que se informa siempre separada por modalidad, porque en relectura diferida el intervalo incorpora el ritmo de reinyección de las alertas persistidas, que es propiedad del reprocesamiento y no del canal. El detalle operativo del ledger, incluida la unidad de conteo del tramo, se documenta en la sección 17.4.

#### 17.3.8. Contratos, trazabilidad y evidencia visual

Los contratos estabilizan la semántica de intercambio entre componentes y definen qué información cruza cada frontera y bajo qué versión. En la arquitectura consolidada del núcleo se expresan como modelos de datos versionados, con serializaciones explícitas e interfaces concretas, y cada uno queda asociado a una corrida para que productores y consumidores evolucionen de forma independiente. La versión viaja dentro del payload y no en el envoltorio de transporte, de manera que el canal pueda cambiar sin que el hecho persistido pierda la identificación de su esquema. Las capacidades futuras evolucionan de forma aditiva sin romper la lectura de corridas históricas.

Las fronteras son lógicas y no prescriben que cada responsabilidad se despliegue en una máquina, un proceso o un contenedor independiente.

##### 17.3.8.1. Contratos mínimos e interfaces

Todo contrato declara su identidad de esquema y su versión como primer elemento del payload. La Tabla 39 reúne los contratos mínimos de la ejecución experimental.

**Tabla 39**

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

***Nota.*** Los contratos de referencia temporal y distribución tienen el mismo estatuto formal que los eventos de percepción y control, porque una medición o una entrega no es reproducible si su entrada carece de versión y procedencia.

El evento central del sistema es el evento de percepción, que agrupa la identidad de esquema versionada, la corrida, la unidad visual, la fuente, el modelo, los prompts, las detecciones y los tiempos. Cada detección conserva etiqueta, prompt, confianza, caja en píxeles y normalizada, y área. El *detection_id* sólo identifica una detección dentro de la unidad visual y no constituye identidad entre frames. Los campos opcionales se incorporan de forma aditiva y se omiten cuando no están disponibles.

La referencia temporal de evaluación impone dos invariantes de validez. La identidad de la fuente de la corrida y la del clip anotado deben coincidir, y para el banco temporal se utiliza *source_id = clip_id*. Y la incertidumbre no fabrica una infracción, de modo que cuando el estado del EPP no es juzgable el episodio no se extiende como violación.

La cadena temporal conserva cinco hitos por alerta, que son la primera evidencia positiva identificada por *unit_id*, la transición a candidato, la transición a confirmado, el registro de la alerta interna y, cuando existe distribución, la confirmación de entrega. Esos hitos permiten medir cada tramo sin mezclar relojes ni poblaciones.

La superficie de crecimiento del evento de percepción se mantiene acotada y separada de las reglas de riesgo. La identidad temporal de sujeto es un campo opcional y la única identidad válida entre frames, que el plano de control puede materializar por configuración sin que el plano de medios necesite emitirla. La velocidad, la dirección, los puntos clave de pose y las máscaras de segmentación quedan previstos como campos opcionales que no modifican la semántica mínima del evento ni desplazan al bounding box. Las relaciones entre sujeto, evidencia de soporte y clase ausente pertenecen al plano de control, porque el plano de medios publica detecciones individuales.

##### 17.3.8.2. Repositorio de hechos y reconstrucción experimental

La trazabilidad experimental permite reconstruir cómo una corrida produjo una alerta interna. La arquitectura conserva la relación entre la configuración de corrida, la fuente visual, el modelo utilizado, los prompts activos, la evidencia perceptiva, la transición de estado del patrón, la alerta registrada y las métricas o errores asociados. Sin esa relación una alerta pierde valor experimental, porque no puede auditarse, compararse ni analizarse con suficiente rigor.

El repositorio utiliza archivos JSONL de sólo adición por corrida y por tipo de hecho. La regla impide la sobrescritura silenciosa y ofrece una representación simple, inspeccionable y re-evaluable sin introducir una base de datos como dependencia del núcleo.

Cada corrida conserva configuración efectiva, manifiesto, procedencia y versión de código junto a detecciones, métricas, errores, transiciones y alertas. El soporte experimental agrupa los runs de los componentes bajo *experiment_id*, copia los artefactos livianos y referencia los de mayor volumen.

Toda alerta puede reconstruirse hasta la configuración efectiva, el conjunto de prompts, el modelo, la fuente y la versión de código que la produjeron. La persistencia no requiere video crudo continuo y mantiene separados los hechos originales de sus proyecciones tabulares o reportes.

Los hechos que la reconstrucción exige exceden a los contratos de intercambio. Junto al inicio y cierre de corrida, al manifiesto con las configuraciones efectivas y a la procedencia e identidad de la fuente, el repositorio conserva los eventos de percepción, las unidades omitidas o descartadas con su causa, los cambios de estado del patrón, la primera evidencia positiva, las alertas internas, las entregas cuando el tramo está habilitado, las métricas con su estado de aplicabilidad y los errores y anomalías. Los hechos asociados a seguimiento temporal, zonas, distribución externa, adaptación de modelos o evidencia visual controlada se incorporan sólo cuando la corrida habilita esas capacidades y no forman parte del conjunto mínimo para CR-01 y CR-02.

Esta selección prioriza la reconstrucción de la cadena causal de la alerta. Una detección aislada no explica un episodio, porque debe relacionarse con la configuración que la produjo, el patrón que la evaluó, la transición que confirmó la condición y las métricas o anomalías que condicionaron el resultado. Por esa razón los errores y descartes relevantes tienen el mismo valor interpretativo que los eventos funcionales, ya que permiten distinguir una ausencia real de evidencia de una falla técnica, un descarte por muestreo o una limitación de la fuente.

Las extensiones condicionadas mantienen esta lógica. Si se incorpora seguimiento temporal, zonas, reglas espaciales, notificaciones externas o adaptación de modelos, esos hechos se persisten como información adicional de la corrida, sin desplazar la cadena mínima de reconstrucción ni convertir capacidades exploratorias en requisitos del núcleo experimental.

##### 17.3.8.3. Política de evidencia visual mínima

La arquitectura adopta una política de minimización de evidencia visual. En el comportamiento ordinario del prototipo la trazabilidad se apoya en identificadores, metadatos, eventos, métricas, coordenadas, referencias temporales y relaciones causales entre hechos persistidos. El almacenamiento continuo de video crudo no forma parte del flujo base, porque aumenta volumen, complejidad y riesgo de privacidad sin ser necesario para reconstruir las decisiones experimentales.

Cuando la revisión técnica, la validación o la comunicación académica requieren evidencia visual, ésta se conserva como artefacto controlado, en forma de snapshot, recorte anotado, clip breve, huella criptográfica, referencia a archivo o vínculo asociado a una alerta o corrida específica. Su uso se justifica por la finalidad experimental, cuenta con criterios explícitos de acceso, retención y anonimización, y no reemplaza métricas, eventos persistidos ni criterios de evaluación.

La política preserva el carácter asistivo y no identificatorio de la plataforma. El sistema no realiza reconocimiento facial, no identifica nominalmente a trabajadores, no extrae biometría y no emite decisiones normativas autónomas. La alerta interna orienta la atención humana sobre una condición visualmente observable, y la interpretación final y cualquier acción preventiva permanecen fuera del sistema automatizado.

#### 17.3.9. Observabilidad y aplicabilidad de métricas

La observabilidad forma parte del contrato experimental. Cada métrica declara la señal que utiliza, el inicio y el cierre del reloj, la unidad, la población y la condición de aplicabilidad. Cuando una medición no tiene significado, la plataforma conserva la causa en lugar de publicar cero u omitir el campo.

La instrumentación se ancla en los puntos donde la arquitectura ya produce hechos. Las transiciones del motor sostienen las métricas del plano de control, porque el tiempo hasta la primera detección se ancla en la primera evidencia perceptiva relevante, la latencia de alerta del sistema se cierra con el registro de la alerta interna que sigue a la transición a confirmado y la tasa de detección sostenida se calcula sobre la continuidad del episodio. Las definiciones operacionales de cada métrica, sus hitos y sus reglas de lectura se establecen en las secciones 17.1.7.3 y 17.1.7.5 y en el Anexo D. La Tabla 40 ubica cada medición en el tramo arquitectónico que la produce.

**Tabla 40**

*Métricas y evidencias por tramo arquitectónico*

| **Tramo** | **Punto de medición** | **Métricas o evidencias** |
| --- | --- | --- |
| Captura y host | Captura física, timestamp de fuente y dequeue en el host. | capture_to_host, jitter y disponibilidad temporal, cuando existe ancla compatible. |
| Plano de medios | Dequeue, normalización, inferencia, postproceso y publicación. | G2A, latencia de inferencia, FPS efectivo, throughput y descartes. |
| Bus media-control | Publicación, secuencia y recepción. | Huecos de seq, integridad, atraso y correlación por unit_id. |
| Plano de control | Primera evidencia, candidato, confirmado, alerta y resolución. | TTFD, *t_alert-system*, latencia interna, SDR, transiciones y re-alertas. |
| Distribución | Disponibilidad de alerta, intento y confirmación del canal. | *t_alert-notification*, resultados de entrega, supresiones, duplicados y errores. |
| Soporte experimental | Consolidación por corrida y entorno. | Recursos, estados de aplicabilidad, causas, robustez y reporte reconstruible. |

***Nota.*** La cadena temporal completa se informa por tramos, y cada tramo declara su hito inicial, su hito final y su dominio de reloj. Los percentiles de tramos diferentes no son aditivos y no deben sumarse para fabricar una latencia de extremo a extremo. La medición del plano de medios comienza en el ingreso de la unidad al host de procesamiento y no en la captura física, que constituye un tramo propio.

Las latencias dentro de un mismo host utilizan reloj monotónico local, y los monotónicos de hosts distintos no se restan. Cuando un trayecto cruza dominios de reloj sin una sincronización válida, la métrica se declara no interpretable con su causa.

El criterio de detección positiva se comparte con el motor de patrones, de modo que la evaluación no reimplemente una segunda definición de evidencia y no aparezcan divergencias silenciosas entre el sistema que decide y el sistema que mide. La Tabla 41 reúne las señales observables sobre las que se apoyan estas mediciones.

**Tabla 41**

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

Cada métrica incluye un estado y una causa. Los estados admitidos son *computed*, *applicable_not_computed*, *not_applicable* y *not_interpretable*, y la plataforma no publica un cero cuando lo correcto es declarar una causa.

Una fuente de imágenes independientes produce not_applicable con causa *non_temporal_source* para los patrones temporales. Un trayecto con monotónicos de dos hosts produce not_interpretable con causa cross_node_monotonic_clock. Una corrida sin referencia anotada produce not_applicable con causa *no_ground_truth*. Y un tiempo hasta la primera detección sin evidencia positiva permanece nulo con su causa.

El reporte consolida el manifiesto, las configuraciones efectivas, las métricas por tramo, el estado de aplicabilidad, las alertas, las re-alertas, los descartes, los errores, los recursos y las limitaciones de interpretación, y cada valor mantiene la condición, el escenario y la población sobre la que se calculó.

El reporte constituye una proyección de hechos persistidos. Puede regenerarse sin modificar los eventos originales y no se utiliza como fuente de verdad cuando existe el artefacto primario.

#### 17.3.10. Escenarios experimentales y topología de referencia

La definición metodológica de ambos escenarios corresponde a la sección 17.1.4.2, y aquí se conservan únicamente sus consecuencias arquitectónicas. En DBE la fuente es regulable y puede releerse bajo la misma configuración, de modo que la arquitectura priorice identidad estable de unidades, orden lógico, persistencia previa y reconstrucción determinista de eventos, patrones y alertas. En EBE la fuente opera en vivo y la escena continúa evolucionando aunque el pipeline se retrase, de modo que la arquitectura instrumente captura o recepción, colas, descartes, jitter, actualidad y dominio de reloj. Ninguno de los dos es una topología física.

##### 17.3.10.1. Equivalencia arquitectónica y alcance de EBE

DBE y EBE convergen en la misma arquitectura una vez normalizada la entrada visual. La diferencia entre escenarios se ubica antes y alrededor de la disponibilidad del frame, en el origen de la fuente, la referencia temporal, la política de muestreo, el control de ritmo y la instrumentación de omisiones o descartes. Después de esa frontera, la inferencia OVD, el postproceso, la publicación de evidencia perceptiva, la evaluación de patrones y el registro de alertas internas mantienen la misma semántica.

La equivalencia evita construir dos flujos incompatibles, cuyos resultados dejarían de ser comparables. Al conservar la misma estructura de eventos, métricas y hechos persistibles, la arquitectura permite distinguir qué parte de la variación proviene de la fuente continua y qué parte del detector o de la evaluación de patrones.

La comparación entre escenarios declara explícitamente qué variables cambiaron. Una corrida DBE y una corrida EBE pueden compartir modelo, prompts, umbrales y reglas de patrón y diferir en fuente, temporización, iluminación, compresión o criterio de descarte, y esas diferencias se registran como parte de la configuración y de la observabilidad.

EBE admite cámaras IP por RTSP, la OAK-D Pro PoE y otras fuentes continuas declaradas mediante el mismo adaptador conceptual. La arquitectura contempla tanto el dispositivo candidato como la contingencia con cámara IP convencional, y ninguna alternativa modifica los contratos de percepción y control.

El rol de captura puede operar como ingesta, preprocesamiento no semántico o preselección conservadora. La variante de preselección liviana en el borde es opcional, está deshabilitada por defecto y opera con el criterio de degradación segura fijado para las capacidades opcionales del plano de medios, de modo que una falla o una incertidumbre del preselector no elimine la unidad del flujo principal. Toda transformación, descarte o cambio de resolución se registra.

La comparación entre una corrida DBE sobre archivo y una corrida EBE del mismo contenido exige un ancla común entre el tiempo de medio y el reloj de pared. Sin ese ancla, el matching temporal contra la referencia anotada se declara no interpretable, mientras que la integridad del bus y la relectura offline continúan siendo evaluables por separado. La Tabla 42 reúne las condiciones que cada corrida EBE debe registrar para que sus resultados sean interpretables.

**Tabla 42**

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

##### 17.3.10.2. Naturaleza temporal de la fuente y aplicabilidad

La procedencia DBE o EBE no determina por sí sola si una fuente sostiene razonamiento temporal. Un video de archivo y un stream en vivo son temporales, mientras que un conjunto de imágenes independientes no lo es. La configuración deriva esta propiedad del tipo de fuente y no permite que el operador la contradiga.

Aplicar una ventana de persistencia sobre imágenes independientes produciría cero alertas por construcción, un resultado indistinguible de la ausencia real de riesgo. Para evitar ese cero silencioso, la evaluación de patrones se declara not_applicable/non_temporal_source. La corrida conserva valor para percepción y asociación espacial, pero no para continuidad o alerta temporal.

Las imágenes permiten afirmar sobre percepción. Los clips temporales permiten afirmar además sobre estado y episodios. Las fuentes en vivo permiten afirmar también sobre transporte, actualidad y comportamiento operativo. Cada reporte limita sus conclusiones al régimen que la fuente permite observar.

##### 17.3.10.3. Roles funcionales y unidades desplegables de referencia

La topología de referencia materializa los roles funcionales establecidos en la sección 17.1.4.1 y ubica en ella al módulo de distribución. Ninguno de los roles equivale necesariamente a una máquina dedicada, y la distribución física de los componentes no forma parte del compromiso conceptual del diseño.

La topología dispone un nodo de borde para captura y un nodo central con GPU para procesamiento. El nodo de entrenamiento permanece fuera del camino operativo de inferencia, porque cualquier adaptación produce un checkpoint candidato que se evalúa después sobre el nodo central y se mantiene como rama comparativa separada. El módulo de distribución se modela como una unidad desplegable propia, gobernada por su propia interfaz de gobierno y consumidora del bus de alertas, y puede co-ubicarse con el nodo central o separarse sin modificar los contratos de alerta interna, notificación y entrega. La Tabla 43 fija la correspondencia entre roles y unidades desplegables. Las métricas se atribuyen al rol y al despliegue efectivamente declarados en la corrida, y no se extrapolan entre unidades desplegables distintas.

**Tabla 43**

*Correspondencia de diseño entre roles funcionales y unidades desplegables de referencia*

| **Rol o unidad desplegable** | **Materialización de referencia** | **Responsabilidades** |
| --- | --- | --- |
| EN (modo base de captura) | Nodo de captura o unidad de ejecución de borde, sin GPU requerida. | Ingesta, control de ritmo, timestamps, healthcheck y normalización no semántica. La preselección liviana es opcional, fail-open y deshabilitada por defecto. |
| CPN | Nodo central o unidad de ejecución con GPU. | Inferencia OVD, postproceso, publicación, evaluación de patrones, alertas internas, persistencia, observabilidad y reporte. |
| TN | Clúster Mendieta u otro recurso de entrenamiento separado. | Preparación de checkpoints de una rama comparativa bajo datos, protocolo y criterios de escalamiento predefinidos; no sustituye la evaluación sobre el CPN. |
| Módulo de distribución | Servicio gobernado por configuración con interfaz HTTP propia, co-ubicable con el CPN o desplegable por separado. | Consumo de la alerta interna desde el bus de alertas, política de notificación, ledger de idempotencia, entrega MQTT y registro del sobre de notificación y del resultado de entrega. |

#### 17.3.11. Riesgos, plan de materialización y cierre

Los riesgos arquitectónicos se formulan como modos de falla observables y se vinculan con una mitigación concreta. La arquitectura no presupone que una mitigación elimina el riesgo, sino que exige instrumentarlo y declarar su efecto sobre la interpretación de la corrida. La Tabla 44 reúne esos riesgos y sus mitigaciones de diseño.

**Tabla 44**

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

El plan de materialización ordena dependencias de diseño y no reemplaza el registro de implementación. El núcleo se construye primero sobre DBE para estabilizar contratos, evidencia, patrones y reporte, y luego se incorporan EBE y las capacidades opcionales sin modificar la semántica del flujo base. La Tabla 45 fija el entregable arquitectónico de cada incremento y el criterio que permite decidir si es verificable. El estado alcanzado por el conjunto de los incrementos corresponde a la sección 17.4.

**Tabla 45**

*Plan de materialización del núcleo*

| **Incremento** | **Criterio de avance** |
| --- | --- |
| Manifiesto y configuración | Una corrida puede reconstruirse mediante experiment_id, configs efectivas y versiones. |
| Fuentes DBE | Imágenes y videos ingresan con identidad, orden y naturaleza temporal declarados. |
| Vocabulario E-IND | Cada detección se atribuye a prompt_set_id y al rol de la clase. |
| Adaptador OVD | El modelo puede sustituirse sin modificar el contrato de percepción. |
| Normalización y postproceso | Las detecciones conservan coordenadas originales, normalizadas y filtros declarados. |
| Persistencia y bus | El hecho se persiste antes de publicarse y toda pérdida resulta detectable. |
| Patrones CR-01/CR-02 | La configuración fija región, granularidad, severidad y ventanas en milisegundos. |
| Alertas internas | Cada episodio confirmado produce una alerta idempotente y auditable. |
| Observabilidad | Cada métrica declara tramo, reloj, unidad, status y cause. |
| Reporte | La salida puede regenerarse desde los artefactos primarios. |

La frontera de extensibilidad distingue tres clases de cambio. Una condición nueva del tipo «sujeto sin EPP» requiere una definición declarativa de patrón y vocabulario, sin modificar contratos ni reentrenar el modelo. Una familia relacional, zonal o de trayectoria requiere un evaluador nuevo en el plano de control. Un modelo, una fuente o un canal nuevos requieren sus respectivos adaptadores y mantienen estables los contratos centrales. Esa frontera evita presentar la extensibilidad open-vocabulary como una capacidad ilimitada, y el costo medido de incorporar extensiones se documenta en las secciones de implementación y evaluación.

El diseño define una plataforma experimental compuesta por el plano de medios, el plano de control, el soporte experimental y un tramo desacoplado de distribución, que protege la ruta crítica, separa la evidencia de su interpretación y conserva una cadena causal reconstruible desde la fuente hasta la entrega. La granularidad de escena y la granularidad de sujeto se tratan como configuraciones semánticamente distintas, y la identidad personal permanece fuera del alcance.

El capítulo deja preparado el paso a la implementación. La sección 17.4 documenta qué componentes se materializaron y cómo se verificaron, y la sección 17.5 concentra las mediciones y su interpretación experimental.

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

***Nota.*** La figura representa la materialización efectiva de los dos patrones de acople. El gobierno de las corridas ocurre por interfaces HTTP en el plano de medios, el plano de control y el módulo de distribución, con el orquestador y la consola como clientes de los tres. El flujo de datos se desacopla mediante buses ZeroMQ de patrón publicador-suscriptor con serialización msgpack, uno para los eventos de percepción entre medios y control y otro para las alertas confirmadas entre control y distribución. El repositorio por ejecución experimental conserva los artefactos persistentes de cada corrida.

Por el bus viajan el evento de percepción y el ciclo de vida de la corrida; por el canal de alertas, únicamente las alertas ya confirmadas por el motor de patrones. Los marcadores 1, 2 y 3 indican el orden de arranque que impone el orquestador: primero el servicio de control, luego el módulo de distribución y por último el servicio de medios, de modo que el control queda suscripto a las detecciones antes de que los medios comiencen a emitir. La no pérdida de alertas la garantiza el publicador, que espera la presencia del suscriptor antes de emitir. Los tres módulos se ejecutan como servicios independientes gobernados por configuración y pueden disponerse en un mismo host o en hosts distintos sin modificar su lógica. La interfaz de inspección no se conecta al bus, sino que consulta las interfaces de servicio de los planos de medios y de control; esa ausencia de enlace es una frontera de diseño y no una omisión del diagrama.

#### 17.4.2. Correspondencia y contratos materializados

Los contratos mínimos definidos durante el diseño se materializaron como modelos de datos, configuraciones versionadas, esquemas serializables, servicios ejecutables y artefactos persistentes. La Tabla 46 establece la correspondencia entre cada denominación conceptual y su realización efectiva.

**Tabla 46**

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

***Nota.*** La tabla documenta la correspondencia semántica entre el diseño y la implementación. El versionado se materializa mediante esquemas explícitos, catálogos, conjuntos de configuración y artefactos congelados por el manifiesto de cada ejecución experimental.

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

Los tres módulos de la cadena se implementaron como servicios independientes, gobernados por configuración y expuestos mediante HTTP. Cada uno carga su configuración al iniciarse, admite una corrida activa por vez, rechaza las solicitudes concurrentes señalando la que está en curso y los dos planos persisten además la configuración efectiva que utilizaron, que el módulo de distribución expone por su interfaz. El plano de medios carga además el modelo una sola vez al arrancar. Rutas, fuentes, umbrales, ventanas temporales y opciones de instrumentación se declaran en configuración, sin constantes ocultas en el código. La Tabla 47 reúne sus operaciones de gobierno.

**Tabla 47**

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

Cada ejecución produce un repositorio de artefactos de sólo adición. La organización por componente que reúne la Tabla 48 conserva la evidencia necesaria para reproducir el flujo, analizar fallas y reconstruir una alerta desde su configuración hasta su salida distribuida.

**Tabla 48**

*Artefactos persistidos por componente y experimento*

| **Tramo** | **Artefactos principales** | **Función de trazabilidad** |
| --- | --- | --- |
| Plano de medios | detections.jsonl; metrics.jsonl; errors.jsonl; summary.json; effective_config.yaml; run_manifest.json; run_provenance.json | Reconstruye fuente, unidades procesadas, detecciones, tiempos, errores, configuración, procedencia y versión de código. |
| Plano de control | pattern_events.jsonl; alerts.jsonl; alerts.csv; metrics.jsonl; errors.jsonl; summary.json; effective_config.yaml | Reconstruye transiciones del patrón, alertas internas, evidencia causal, métricas y configuración del motor. |
| Soporte experimental | manifest.effective.yaml; copias de artefactos livianos; referencias a artefactos pesados; report.json; report.md | Agrupa las corridas de ambos planos bajo un experiment_id y consolida el resultado de la ejecución experimental. |
| Distribución | notifications.jsonl (ledger de intentos y entregas, de sólo agregado); dead_letter.jsonl; distribution_summary.json | Relaciona cada intento y resultado de entrega con la alerta interna original sin reescribirla, y conserva por separado los descartes definitivos por agotamiento de reintentos. |

***Nota.*** Los nombres de archivo corresponden a los artefactos implementados. Los artefactos pesados se referencian en la ejecución experimental para evitar duplicación, mientras que las configuraciones y reportes se conservan junto al experimento.

La disposición del repositorio del soporte experimental es la siguiente.

runs/<experiment_id>/  (repositorio del soporte experimental)   manifest.effective.yaml   media/    summary.json · metrics.jsonl · effective_config.yaml             detections.ref.json             (referencia al detections.jsonl del plano de medios)   control/  alerts.jsonl · pattern_events.jsonl · metrics.jsonl             summary.json · effective_config.yaml             (y la evaluación temporal, cuando la corrida la habilita)   distribution/  notifications.jsonl · distribution_summary.json                  dead_letter.jsonl               (cuando la corrida habilita el tramo de distribución)   report/   report.json · report.md

La ejecución experimental consolida así los cuatro componentes bajo una misma clave. El manifiesto de corrida registra la versión de código que produjo los artefactos. Junto con la configuración efectiva, el conjunto de prompts y la procedencia de la fuente, ese dato permite reconstruir cada alerta hasta el modelo y la revisión de código que intervinieron. El reporte consolidado declara el estado de aplicabilidad de cada métrica como computada, aplicable no computada, no aplicable o no interpretable, siempre con una causa explícita.

El ledger de entregas del módulo de distribución registra una fila por intento y una más por el descarte definitivo cuando se agotan los reintentos, de modo que la unidad de conteo del tramo es la notificación y no la fila. Al reutilizar un directorio de salida, la generación anterior se archiva íntegra y la deduplicación considera todas las generaciones, para que un reprocesamiento no vuelva a entregar lo ya entregado ni pierda la traza de lo entregado antes.

#### 17.4.6. Banco temporal y referencia humana de evaluación

La evaluación temporal se apoya en una referencia humana de episodios por clip, materializada mediante el esquema clip_gt.v2. La primera generación registraba alertas esperadas por sujeto y fue reemplazada por episodios a nivel de escena y condición, con tiempos en milisegundos y estados de aplicabilidad por clip. Para la anotación se seleccionó CVAT, una herramienta de código abierto con soporte de interpolación temporal y exportación estructurada.

**Adquisición del material.** El banco proviene de dos fuentes con procedencia y grado de control experimental distintos, y esa diferencia se conserva como atributo de cada clip. La primera es un rodaje guionado ejecutado con el hardware real de captura del prototipo. Cada escenario se diseñó en función de una condición de riesgo del núcleo. Un guion segundo a segundo fija la entrada del sujeto en cumplimiento, el inicio diferido de la infracción y su persistencia sostenida durante lapsos muy superiores a las ventanas de confirmación. El guion incluye además escenas negativas y escenas deliberadamente por debajo de ese umbral. Las tomas se registraron con margen temporal adicional respecto del clip previsto, y tanto la grabación como el recorte se hicieron desde la propia consola del prototipo.

La segunda fuente es un lote de obra real no guionada, obtenido de videos públicos e incorporado como bloque separado con criterios de selección definidos de antemano. Reúne material de obra en cumplimiento destinado a medir especificidad y falsos positivos, no sensibilidad, prohíbe concatenar segmentos cortos para fabricar unidades largas y exige que toda exclusión se declare con causa y firma en lugar de descartarse en silencio.

Los videos maestros del lote se obtuvieron de la lista de reproducción pública de YouTube *“Raw” construction videos* (s. f.) y no se redistribuyen. El Anexo F identifica la lista como referencia conjunta de los videos utilizados y delimita el alcance de su fecha de consulta.

**Segmentación temporal.** Los videos maestros se conservaron sin modificación y las unidades de evaluación se generaron como clips derivados, con criterios temporales fijados antes de ejecutar las campañas y aplicados como reglas ejecutables. Cada clip del rodaje se recortó con un preludio fijo de 3,5 s antes del inicio de la condición, porque un episodio que arranca en el primer fotograma impide medir el tiempo hasta la primera detección. Lleva además una cola posterior al cierre del episodio de entre 3 y 10 s según el escenario, y un piso de duración que garantiza que una alerta válida pero lenta ocurra dentro del clip.

Ese piso resulta de sumar al inicio del episodio el techo del objetivo de latencia de alerta de su patrón, la ventana de resolución y un margen final, y se verifica mediante un control automático durante la derivación de la referencia. El clip que no lo alcanza no se vuelve a recortar, y sus métricas de latencia y sensibilidad quedan censuradas y así se declaran.

El fundamento del dimensionamiento es bidireccional. Un clip demasiado corto subestima al sistema, porque produce latencias artefactuales y cuenta como omisión una alerta que no tuvo tiempo de ocurrir. Un clip sin tiempo muerto sobreestima la precisión, porque elimina los tramos donde aparecen los falsos positivos. La selección de tomas se hizo por calidad visual de la escena y no por duración, y los límites de todos los clips quedaron congelados bajo control de versiones antes de ejecutar las campañas. Los clips del lote de obra real no se segmentaron, porque recortarlos alteraría el tiempo negativo que ese bloque aporta.

**Preanotación y revisión humana.** La anotación no partió de video crudo. Cada clip se preanotó automáticamente con un detector de vocabulario abierto de mayor capacidad que el modelo evaluado, elección deliberada para evitar circularidad entre el sistema medido y su referencia. Ese detector se acopló a un algoritmo de seguimiento que propone trayectorias por sujeto, con los atributos de protección inicializados por asociación espacial.

Sobre esa propuesta se realizó la pasada humana en CVAT. Esa revisión corrigió las cajas y las trayectorias de los 47 clips del banco, verificó la identidad de cada sujeto a lo largo de la secuencia y asignó los atributos observables tramo por tramo. Marcó como estado desconocido aquellos tramos donde el atributo no resulta observable, en lugar de forzar un valor, y fijó los límites temporales de los 37 episodios de referencia. La interpolación temporal y la preanotación redujeron las operaciones repetitivas, pero no sustituyeron ninguna de esas decisiones. La referencia experimental es el producto de esa revisión. Cuatro clips de un piloto anterior sobre video de obra real, anotados con la misma referencia de atributos y ajenos al banco temporal, se conservaron para la medición del estado por persona que informa la sección 17.5.3. La anotación la realizó un único anotador, sin la doble anotación sobre el 20 % del material que la sección 17.1.5.4 exige para la anotación propia, desviación que la sección 17.5.7 registra como limitación.

**Derivación y congelamiento.** La salida de la anotación se procesa mediante una cadena reproducible de separación, derivación, validación, promoción y agregación. La cadena valida la estructura de cada exportación antes de derivar. La derivación clasifica los episodios con las mismas ventanas de confirmación que utiliza el motor de patrones, de modo que la referencia y el sistema evaluado apliquen un criterio temporal idéntico. Una divergencia entre ambos produciría omisiones ficticias. Las correcciones humanas posteriores se aplican como registros firmados sobre los artefactos versionados, nunca editando la herramienta, y un control automático falla cuando una corrección firmada no aparece en la referencia derivada. Las anotaciones promovidas quedan congeladas bajo control de versiones, con huella criptográfica por clip y un manifiesto agregado del banco. La referencia experimental es la versión promovida en el repositorio y no el estado mutable de CVAT.

#### 17.4.7. Verificación, alcance efectivo y brechas

El criterio de cierre de la implementación exigió que cada unidad funcional produjera evidencia verificable dentro de una corrida y que su comportamiento pudiera repetirse mediante pruebas automatizadas o artefactos persistidos. La Tabla 49 reúne esa evidencia, concentrada en gobierno por configuración, cierre de corridas, paridad entre caminos, determinismo del motor y funcionamiento de la integración.

**Tabla 49**

*Evidencia de verificación técnica del prototipo*

| **Propiedad verificada** | **Evidencia de implementación** |
| --- | --- |
| Servicios ejecutables y gobernados por configuración | Las operaciones de salud, disponibilidad, creación y consulta de corridas operan sobre configuraciones validadas, y cada servicio limita la concurrencia de corridas activas. |
| Cadena DBE de extremo a extremo | La relectura por archivo produce detecciones, transiciones, alertas, métricas, resumen y configuración efectiva, y repetir el camino conserva los artefactos deterministas. |
| Cadena EBE y cierre de ciclo de vida | El consumidor confirma la suscripción antes del productor, la corrida cierra con el evento de finalización y los huecos de secuencia se registran como degradación. |
| Paridad entre repositorio y bus | La evidencia persistida y la transmitida conservan el mismo contenido lógico, y una corrida en vivo puede reevaluarse por el camino diferido. |
| Motor de patrones e idempotencia | Las transiciones respetan las ventanas configuradas y la alerta usa un identificador determinista, estable ante el reprocesamiento de la misma corrida. |
| Distribución de alertas | Se verificaron la relectura diferida, el consumo en vivo, la supresión, la idempotencia, la entrega MQTT con confirmación contra un broker real, el ledger y el reporte. |

***Nota.*** La tabla acredita funcionamiento técnico y reproducibilidad. Cada módulo mantiene su propio conjunto de pruebas automatizadas, con el que estas propiedades se vuelven a verificar. No presenta métricas de desempeño del banco experimental, que se informan con sus denominadores y condiciones en la sección 17.5.

La verificación confirmó además que las fallas instrumentales no se convierten en ceros silenciosos, porque una pérdida de bus degrada la corrida, una métrica sin reloj comparable se declara no interpretable y un canal no habilitado se declara no aplicable.

El cierre de la implementación requiere declarar con precisión qué capacidades se ejercieron, cuáles permanecen fuera del núcleo y con qué estatuto, porque no todas las brechas son del mismo tipo.

La concentración del prototipo en el núcleo validable no responde a una reducción tardía del alcance sino a las condiciones de evaluabilidad de cada condición del catálogo. Las de Nivel 1 cuentan con datasets públicos y bancos con verdad de terreno para persona y elementos de protección, lo que permite medir percepción, estado temporal y alerta con denominadores declarados. Las de Nivel 2 y Nivel 3 exigen insumos que el material disponible no provee, y su justificación se desarrolla en la sección 17.5.7. Incorporarlas sin esa base habría producido capacidades no medibles, de modo que el esfuerzo se concentró en llevar el núcleo a capacidad medida. Las doce capacidades del núcleo y la operación sobre fuentes en vivo quedaron implementadas, se describen en las secciones 17.4.1 a 17.4.5 y se ejercieron en las campañas de la sección 17.5.

Dos capacidades opcionales de la Tabla 32 y dos propiedades del diseño quedaron implementadas y medidas. La identidad persistente de sujeto opera como decorador configurable de la fuente del plano de control y constituye una capacidad medida, aunque las métricas formales de seguimiento permanezcan excluidas por falta de anotación de identidad. Las tres estrategias de detección se implementaron y su comparación se ejecutó, con la salvedad de la variante híbrida por conjunción que declara la sección 17.5.6. La distribución de alertas quedó implementada, verificada e integrada a la consola y a la orquestación, con MQTT como canal ejercido. Y la paridad entre la relectura por archivo y el transporte por bus quedó verificada. Los valores de todas ellas se informan en la sección 17.5.

Una capacidad se implementó y se caracterizó fuera del régimen evaluativo. La preselección liviana en el rol de captura funciona como filtro de personas ejecutado en el dispositivo, con criterio de degradación segura y deshabilitada por defecto, y no existe para las fuentes por red. Permaneció deshabilitada en todas las corridas evaluativas, y esa exclusión es deliberada y anterior a los resultados, porque un filtro de cuadros sin persona suprimiría las detecciones sostenidas que la tasa de falsas alarmas existe para medir. La sección 17.5.7 informa su reducción de carga medida.

Las condiciones de riesgo de Nivel 2 y Nivel 3 quedaron especificadas y no implementadas. Su incorporación requiere evaluadores relacionales, zonales o de trayectoria y evidencia adecuada, y por eso no forman parte del núcleo validable.

La gestión de evidencia visual controlada quedó implementada como opción de corrida. El plano de medios puede conservar una previsualización por unidad procesada, con un tope configurable, y un video anotado de la corrida completa. La previsualización viene habilitada por defecto, un valor que invierte la regla de habilitación explícita que el diseño fija para los módulos opcionales, y el video anotado viene deshabilitado. Las campañas del banco declararon apagadas las dos, conforme a la política de minimización de evidencia visual, de modo que los artefactos evaluativos conservan identificadores, metadatos y coordenadas, y no imágenes.

En la rama de adaptación, YOLOE-26s proporcionó un punto de partida de alcance acotado mediante el ajuste exclusivo de la proyección de clases, conforme a la modalidad de linear probing descrita en la sección 15.2.4. La preparación experimental verificó los parámetros entrenables y la carga del punto de control en el servicio de inferencia, y fijó una línea base y una evaluación propias. Estos elementos concretaron el criterio de factibilidad de la sección 17.1.9, sin equiparar la elección del modelo para ajuste con la del perfil operativo Grounding DINO.

El mismo linaje permitió ampliar después el alcance entrenable y conservar las particiones de datos, sin introducir además un cambio de arquitectura. La comparación no aisló únicamente la cantidad de parámetros, porque también variaron la optimización y la duración del entrenamiento, cuyos detalles se declaran más adelante. MM-Grounding-DINO quedó como alternativa de un tercer tramo condicionado y no como continuación directa del punto de control operativo. Este recorrido no establece una superioridad general de YOLOE para el ajuste ni una imposibilidad de adaptar Grounding DINO.

La secuencia general de esta rama exploratoria comprendió tres tramos y se registró antes del entrenamiento. El protocolo, la procedencia, el servicio de inferencia, la evaluación y la línea base quedaron congelados. Las revisiones posteriores se documentaron durante la ejecución y se aplicaron a las configuraciones siguientes, sin modificar retrospectivamente los criterios con los que se juzgaron los resultados anteriores.

El primer tramo entrenó sólo la proyección de clases de YOLOE-26s, con 3.096 parámetros entrenables. El segundo amplió el ajuste al detector completo, con las rutas de prompt congeladas y 10,35 millones de parámetros entrenables, y modificó también el régimen de épocas y de optimización. El tercero contemplaba ajustar MM-Grounding-DINO como linaje entrenable de Grounding DINO y su activación estaba condicionada a que alguno de los tramos anteriores alcanzara los criterios establecidos.

El subconjunto de ajuste reunió 2.946 imágenes, por encima del rango orientativo de 500 a 2.000 que fija el protocolo, y ese exceso es consecuencia de aplicar la regla de partición y no de apartarse de ella. Se tomó el total de los linajes elegibles después de excluir íntegramente la única fuente que el banco de evaluación incorpora completa y de deduplicar de forma perceptual contra él, sin submuestrear hasta el techo del rango. Los controles de solapamiento con el banco y de componentes compartidos entre entrenamiento y validación quedaron en cero, y la semilla de partición se registró con el resto de la configuración.

El cumplimiento de esa regla tuvo un límite que conviene declarar. Una de las dos fuentes retenidas para el ajuste aporta además el estrato curado del banco de imágenes, de modo que en ese punto la partición se apartó del protocolo, que reserva para el banco a toda fuente que lo integre aunque sus particiones nominales sean disjuntas. Excluirla habría reducido el conjunto de ajuste de 2.946 a 743 imágenes. La desviación se admitió con dos controles verificados, particiones disjuntas y deduplicación perceptual contra el banco en cero, y la retención medida sobre el banco, que incluye ese estrato, se lee con esa salvedad.

La asignación efectiva de las cuatro fuentes de la sección 17.1.6.2 fue la siguiente. SHEL5K y CHV integran el banco de evaluación como los estratos de 5.000 y 1.330 imágenes, y CHV es la fuente que quedó excluida íntegramente del ajuste. construction_site_safety aportó 2.203 imágenes al ajuste y es además el origen del estrato curado de obra, que es la desviación declarada arriba. ppe_siabar aportó las 743 restantes. La retención open-vocabulary se midió sobre las 5.000 imágenes de validación de COCO 2017, un material ajeno al dominio y distinto del estrato de 5.000 imágenes del banco.

El aumento de datos fue el conjunto por defecto de la biblioteca de entrenamiento, mosaico, variación de color, traslación, escala, volteo horizontal y borrado aleatorio, sin ajustes propios, y quedó registrado en la configuración efectiva de cada corrida. El costo fue de 7,7 minutos para el primer tramo y de 23,8 para el segundo, sobre una unidad gráfica NVIDIA A30 del clúster de cómputo.

Los dos tramos entrenados ajustaron la variante s de YOLOE-26 sobre la misma partición de 2.946 imágenes de ajuste y 483 de validación, con imágenes a 640 píxeles de lado, lotes de ocho, semilla fija y ejecución determinista, y en cada uno se conservó el punto de control de mejor mAP50-95 sobre las cuatro clases de validación y no el de la última época.

El primer tramo recorrió 10 épocas completas con la selección automática de optimizador de la biblioteca de entrenamiento, y su detención temprana quedó inoperante porque la paciencia configurada superaba ese techo.

Tras el veredicto del primer tramo, la regla de escalamiento dejó sin habilitación a los siguientes. Una enmienda posterior reabrió el segundo como tramo exploratorio para examinar si el alcance entrenable limitado explicaba el desenlace del primero, con márgenes y expectativas propios fijados antes de la nueva evaluación. El veredicto del primer tramo permaneció intacto y el tercero no se reabrió. Para el segundo se fijaron un techo de 60 épocas y una detención tras 15 sin mejora, ambos registrados antes de su evaluación.

Una corrida inicial del segundo tramo utilizó el modo automático de la biblioteca de entrenamiento. Ese modo derivaba la tasa de aprendizaje del número de clases y no del alcance entrenable, de modo que asignaba el mismo valor a un tramo de 3.096 parámetros y a otro de 10,35 millones. La corrida se descartó como candidata, se conservó como evidencia del hallazgo y no se evaluó contra el banco congelado.

A partir de ese hallazgo, una nueva enmienda fijó el optimizador por descenso de gradiente estocástico, con tasa de aprendizaje inicial 0,01, momento 0,937 y tres épocas de calentamiento. La configuración revisada se registró antes de su evaluación y se ejecutó desde el peso base. La detención se activó en la época 16 y la mejor época fue la primera, que es el dato sobre el que se apoya la lectura de colapso durante el entrenamiento.

La rama quedó cerrada con dos tramos entrenados y un tercero cerrado sin entrenamiento. Los dos tramos entrenados se evaluaron una única vez contra el banco congelado y ninguno superó los criterios de incorporación, firmados antes de que existiera el punto de control al que se aplicarían. Ningún punto de control se adoptó como modelo de servicio ni entró al despliegue, y sus perfiles permanecen en el catálogo sólo para reproducir la evaluación.

El cierre del tercer tramo se sostuvo en la condición de activación y en la discontinuidad de linaje respecto del perfil operativo. Ninguno de los tramos previos alcanzó sus criterios de incorporación, y el linaje ajustado no habría sido el del perfil operativo. La variante tiny candidata entregaba cajas degeneradas con origen en el punto de control publicado, reproducidas con la biblioteca de referencia sin código del proyecto. La variante sana de esa familia no había mostrado ventaja en ninguna dimensión evaluada. Estas observaciones reforzaron el cierre técnico sin extender la anomalía a toda la familia. Los resultados y veredictos por tramo se informan en la sección 17.5.6.

El prototipo conserva su carácter experimental y asistivo. No implementa reconocimiento de identidad personal, no determina incumplimientos normativos y no reemplaza la supervisión de seguridad, conforme a las salvaguardas de la sección 17.1.10.

#### 17.4.8. Extensibilidad y costo de extensión

La extensibilidad se verificó en dos dimensiones, la incorporación de nuevas capacidades mediante puntos de extensión acotados y la evolución aditiva del evento de percepción. La plataforma no sostiene que toda condición pueda incorporarse sólo con lenguaje, y la Tabla 50 delimita qué cambios requieren configuración y cuáles requieren código nuevo.

**Tabla 50**

*Puntos de extensión y costo técnico de incorporación*

| **Extensión** | **Intervención requerida** | **Costo técnico esperado** |
| --- | --- | --- |
| Condición del mismo tipo: sujeto sin EPP | Entrada declarativa en el conjunto de patrones y formulaciones de prompt, con clase del sujeto, clase ausente, región, umbrales y ventanas. | Sólo configuración. Sin reentrenamiento ni cambios en el motor. |
| Familia nueva de condiciones | Nuevo evaluador para relaciones, zonas, trayectorias u otra semántica no cubierta por el evaluador de ausencia espacial. | Código acotado al evaluador, con los contratos y el resto de la cadena conservados. |
| Modelo de detección | Adaptador que normalice la salida y perfil de modelo en el catálogo. | Código acotado al adaptador y configuración. |
| Fuente visual | Adaptador de ingesta que produzca unidades visuales normalizadas. | Código acotado al adaptador y su validación. |
| Canal de notificación | Implementación de un consumidor del contrato de notificación y su integración de ciclo de vida. | Fuera de los dos planos; no modifica la alerta interna. |
| Dato adicional en la detección | Campo opcional con valor por defecto y consumidor tolerante a su ausencia. | Evolución aditiva sin ruptura del contrato de percepción. |

***Nota.*** La frontera entre la primera y la segunda fila delimita la extensibilidad por configuración. Una ausencia de EPP sobre un sujeto observable reutiliza el evaluador existente, mientras que una relación nueva entre entidades requiere lógica de evaluación específica.

El costo de incorporar vocabulario nuevo se midió en un piloto sobre la clase machinery. No requirió entrenamiento y demandó 48 líneas de configuración y nueve minutos de trabajo. El ejercicio mostró también que la extensión no termina al obtener detecciones, porque la alineación entre el término elegido y el concepto visual debe validarse. La sección 17.5.2 informa su desempeño y los dos fallos semánticos que aparecieron.

La identidad de sujeto recorrió el segundo camino de extensión. Se implementó como un decorador configurable de la fuente de eventos del plano de control, desactivado por defecto y utilizable tanto en el camino diferido como en el camino en vivo. La incorporación no exigió modificar el plano de medios ni romper el contrato de percepción. El identificador se conserva en los artefactos de control y no en los del plano de medios, pero el seguidor, que asocia cajas de persona por solapamiento entre cuadros consecutivos, y el orden del flujo son deterministas, de modo que una relectura reproduce las mismas identidades. Su efecto cuantitativo se informa en la sección 17.5.

El evento de percepción admite además información que la implementación actual no produce, y esa capacidad se ejerció antes de declararse. La detección normalizada incluye un campo de identidad entre fotogramas que ningún productor emite, declarado como opcional con valor por defecto y omitido al serializar cuando no tiene valor, de modo que su presencia no altera un solo byte de los artefactos existentes. El plano de control ya lo consume como clave de estado cuando opera con granularidad por sujeto, y el contrato conservó su versión.

Tres decisiones de implementación sostienen esa propiedad. Los campos nuevos se agregan como opcionales con valor por defecto, los consumidores validan contra su propia declaración del contrato y descartan sin error los campos que no conocen, y la frontera de la distribución admite explícitamente campos adicionales. Cada plano mantiene además su propia declaración del evento en lugar de una biblioteca compartida, de modo que la frontera entre ellos es el esquema serializado y no una dependencia de código, y ambos pueden versionarse y desplegarse por separado.

Lo excluido son las métricas formales de seguimiento multiobjeto y no la capacidad de asociar sujetos. De manera análoga, la velocidad, la dirección, la pose y la segmentación permanecen previstas como campos opcionales, sin presentarse como implementadas.

En conjunto, la implementación materializó la cadena que va del video a la alerta distribuida como un prototipo ejecutable, configurable, reproducible y auditable, que conserva la separación entre planos, opera por archivo o por bus y explicita sus brechas. Sobre esa base, la sección 17.5 evalúa su rendimiento sin atribuirle capacidades que no fueron medidas.

### 17.5. Evaluación y validación del prototipo

#### 17.5.1. Encuadre y reglas de lectura

La evaluación informa cuánto produjo el prototipo bajo las condiciones experimentales definidas. Los resultados se organizan por pregunta de medición y distinguen tres niveles. La percepción sobre imágenes caracteriza al detector, el estado observable por persona evalúa la reconstrucción de una condición por sujeto, y la alerta temporal por episodio representa a la plataforma completa. Las mediciones de percepción, estado por persona y alerta por episodio pertenecen al Escenario A, sobre material congelado y relectura por archivo, y las de tiempo real al Escenario B, sobre captura continua.

Rigen las reglas de lectura fijadas en la sección 17.1.7.3. Cada cifra se acompaña de la combinación que la produjo, del material o estrato sobre el que se calculó y de su denominador. Precisión, recall y F1 se calcularon sólo sobre casos positivos con referencia aplicable, los materiales negativos se analizaron por conteo de falsos positivos, las re-alertas se contabilizaron aparte y los percentiles de tramos con relojes distintos no se sumaron. Los nombres abreviados de esta sección siguen al marco de métricas, con dos equivalencias. AP50 y mAP50 designan la precisión media a solapamiento 0,5 que el marco escribe AP@0,5, y la latencia de alerta es el intervalo que el marco llama *t_alert-system*. La latencia de alerta mide el intervalo entre el inicio del episodio anotado y su alerta confirmada, y la cobertura del episodio, que las tablas abrevian SDR, expresa qué proporción del tiempo con la condición activa mantuvo evidencia correcta.

El banco temporal congelado comprendió 47 clips, distribuidos en 32 positivos y 15 negativos, con 37 episodios de referencia. Lo integran 34 clips de un bloque de rodaje guionado y 13 de un estrato de obra real no guionada. El estrato de obra real no guionada se mantuvo separado y no se utilizó para ordenar granularidades cuando su denominador efectivo fue insuficiente. La referencia temporal fue humana y quedó congelada antes del reporte.

Una métrica se trató como computable sólo cuando existieron referencia, reloj e instrumentación compatibles con su definición. Cuando faltó alguno de esos elementos, el resultado se declaró no aplicable o no interpretable en lugar de convertir la ausencia de medición en un cero.

#### 17.5.2. Percepción sobre imágenes

La primera pregunta examinó la capacidad perceptiva de las combinaciones sobre un banco congelado de 6.477 imágenes y 55.165 anotaciones. El material se dividió en tres estratos independientes de 147, 1.330 y 5.000 imágenes, correspondientes a obra curada, a obra con mayor cobertura de chaleco y a una fuente con clase nativa de cabeza descubierta. El tercero aportó el 77 % del banco, de modo que el agregado se leyó siempre junto con el desglose por estrato.

La Tabla 51 muestra que la combinación gdino-tiny-560 alcanzó el mAP50 más alto en el agregado y en el núcleo curado, mientras que gdino-base-560 produjo el recall más alto de CR-01 por evidencia directa. El veredicto se formuló entonces por combinación. El primer perfil se retuvo como configuración operativa por un criterio fijado antes de leer los resultados, y el segundo como contraste especializado para cabeza descubierta y chaleco. No se estableció una jerarquía universal entre modelos. Las dos comparten resolución de entrada y umbrales, que declara la sección 17.4.4, y difieren en el tamaño del perfil.

**Tabla 51**

*Resultados de percepción por combinación en el banco congelado*

| **Combinación** | **mAP50** ***agregado (n = 6.477 imágenes)*** | **mAP50** ***obra curada (n = 147 imágenes)*** | **Recall de CR-01 por evidencia directa** ***(n+ = 5.313)*** | **Veredicto por combinación** |
| --- | --- | --- | --- | --- |
| gdino-tiny-560 | 0,551 | 0,503 | 0,308 | Retenida como perfil operativo por liderar el mAP50 en las dos escalas reportadas. |
| gdino-base-560 | 0,525 | 0,474 | 0,599 | Retenida como contraste de mayor cobertura de cabeza descubierta y chaleco. |
| yoloe-26x | 0,442 | 0,405 | 0,000 | Ciega a la cabeza descubierta, de modo que no sostiene la formulación directa. Su límite para el núcleo es el chaleco, con AP 0,182 en obra curada frente a 0,520 del perfil operativo. |

***Nota.*** El denominador del agregado es el banco completo. El recall de CR-01 se informa sobre 5.313 positivos, el conteo de la referencia con la que se ejecutó la campaña. Una corrección posterior de esa referencia lo dejó en 5.308 y la medición no se repitió. Esa columna cuenta sólo detecciones de cabeza descubierta, de modo que mide la formulación directa. El núcleo opera con la indirecta, que deriva la ausencia desde persona y casco, y su capacidad para la condición no se lee en esta columna.

La especialización del perfil base también apareció en chaleco, con AP 0,582 frente a 0,520 del perfil operativo sobre el estrato de obra curada. Para el perfil operativo, persona y casco se mantuvieron entre 0,70 y 0,89 de AP en los dos estratos públicos, mientras que chaleco quedó en 0,553 y 0,520 en los dos estratos que anotan esa clase. La asimetría no dependió de una única fuente, porque se sostuvo en ambos.

La familia YOLOE presentó una limitación distinta. Sus cuatro variantes produjeron AP 0,000 para bare_head, la clase de cabeza descubierta, sobre el banco anterior al congelado, y la variante mayor repitió el cero sobre el estrato que anota esa clase de forma nativa. Aunque resultó adecuada para rutas de mayor velocidad, esa ceguera la volvió inservible para la formulación directa de CR-01 en la configuración evaluada.

La extensibilidad semántica se ejerció sobre una clase nueva, cuyo costo de incorporación informa la sección 17.4.8. La clase alcanzó AP50 de 0,662 sobre 99 cajas de referencia sin ninguna corrida de entrenamiento. El costo reducido no eliminó la necesidad de validación semántica. Sobre el mismo material, la palabra *vehicle* no produjo ninguna detección cuando acompañó a *machinery* en el vocabulario y, aislada, produjo 118 cajas con AP 0,026, porque el modelo la resolvió sobre la maquinaria misma.

#### 17.5.3. Estado por persona

El nivel intermedio evaluó si la evidencia perceptiva permitía determinar el estado observable de cada persona. La calibración se realizó sobre una mitad del material y las métricas sobre la otra, con IoU mayor o igual que 0,5. La partición en mitades se registró con su semilla y fue la misma para todos los brazos, de modo que ninguna imagen que ajustó un umbral entró después en la medición. Se compararon E-IND, la estrategia indirecta que reconstruye la ausencia desde evidencia positiva, y E-DIR, la formulación directa retenida para el contraste. La medición sobre video abarcó 17 clips de obra real, los 13 del estrato de obra real del banco temporal y 4 de un piloto anterior, evaluados al nivel del estado por persona sobre su referencia de atributos, submuestreados a 2 Hz y sin calibración de umbrales, con el punto de operación desplegado, y no incluyó el motor de patrones. La Tabla 52 reúne los resultados.

**Tabla 52**

*Resultados de estado por persona*

| **Material y condición** | **Resultado E-IND** | **Contraste E-DIR** | **Denominador** | **Lectura** |
| --- | --- | --- | --- | --- |
| Imágenes, CR-01 | *F1* 0,546 | *F1* 0,188 | *n+* = 2.487 | Los intervalos de confianza no se solaparon. |
| Núcleo curado, CR-01 | *F1* 0,408 | *F1* 0,189 | *n+* = 28 | La ventaja se conservó en el estrato objetivo. |
| Imágenes, CR-02 | *F1* 0,479 | *F1* 0,418 | *n+* = 82 | Un único estrato; el resultado no cerró la condición. |
| Video de obra real - CR-01 | *P* 0,016 · *R* 0,467 · *F1* 0,031 | No corresponde a esta medición | *n+* = 92 de 10.356 cuadros con persona | La caída provino de precisión, no de recall. |
| Video de obra real - CR-02 | *P* 0,009 · *R* 0,318 · *F1* 0,018 | No corresponde a esta medición | *n+* = 170 de 10.361 cuadros con persona | La misma frontera de juzgabilidad dominó el resultado. |

La estrategia directa no se comportó como un detector estable del estado, sino como un recuperador de casos omitidos por la estrategia indirecta. Recuperó el 18,5 % de esos casos, equivalentes a 155 de 840, pero lo hizo a costa de precisión. Esa relación explica por qué la estrategia no se adoptó aunque aportara evidencia complementaria en un subconjunto.

La medición sobre 17 clips de obra real mostró un cambio de régimen. La caída del F1 provino de la precisión y no del recall, por acumulación de falsos positivos sobre personas cuyo estado no podía determinarse visualmente. El evaluador excluyó del denominador 1.414 cuadros con persona no juzgables para CR-01, aquellos en los que el anotador no pudo determinar el estado, y 1.409 para CR-02, y contabilizó como falso positivo cualquier predicción emitida sobre ellos.

Esa frontera tiene al menos tres ejes y ninguno de los tres, por sí solo, anticipa si el material es evaluable. La escala ordena dentro de un mismo régimen de luz. En los clips diurnos del estrato de obra real, la proporción de sujetos detectados a los que se asocia un chaleco pasa de alrededor del 10 % en la banda de 80 a 120 píxeles de altura a entre 63 y 73 % en la banda de 220 a 320, y en el bloque de rodaje, con medianas de altura por encima de 700 píxeles, esa misma asociación se sostuvo entre 96 y 100 %. La iluminación desplaza la curva entera, porque en el clip nocturno del estrato la banda de 80 a 120 píxeles cae a 0 % y las siguientes, hasta 320, quedan entre 6 y 13 %. Y la oclusión invierte el orden de los dos ejes anteriores, ya que el clip con los sujetos más grandes del conjunto, con mediana de 370 píxeles, quedó entre los peores resultados con *F1* 0,084 sobre una cuadrilla apiñada en la que el 58,5 % de las personas aparece solapada con otra. Tampoco la juzgabilidad humana anticipa el rendimiento del sistema, porque el clip con la segunda proporción más baja de cuadros no observables para el anotador rindió el peor F1 del conjunto.

#### 17.5.4. Alerta por episodio contra la referencia temporal humana

La alerta por episodio constituyó el resultado principal porque integra percepción, asociación, histéresis, estado temporal y registro de alerta. El bloque de rodaje guionado reunió 34 clips y 35 episodios de referencia, 28 de CR-01 y 7 de CR-02. Treinta y cuatro episodios resultaron evaluables y uno quedó censurado con causa declarada, porque su duración no permitía que una alerta lenta ocurriera dentro del clip, y cuatro clips fueron negativos. La Tabla 53 reúne las combinaciones ejecutadas sobre ese material, cada una con una sola variable cambiada respecto de la línea de base.

**Tabla 53**

*Alerta por episodio en el bloque de rodaje guionado*

| **Combinación** | **Recall** | **Precisión** | **F1** | ***t_alert*** **en ms (n de episodios confirmados)** | **SDR** | **FP en 4 negativos** | **Veredicto local** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Núcleo E-IND, escena | 0,824 | 0,757 | 0,789 | 5.327 (*n* = 28) | 0,698 | 0/4 | Línea de base de la plataforma. |
| Contraste base-560 | 0,735 | 0,676 | 0,704 | 4.899 (*n* = 25) | 0,819 | 0/4 | Mayor SDR, menor F1 que el perfil operativo. |
| E-DIR de extremo a extremo | 0,176 | 0,146 | 0,160 | 6.611 (*n* = 6) | 0,210 | 2/4 | Vetada por precisión. |
| E-HYB por disyunción | 0,353 | 0,255 | 0,296 | 6.956 (*n* = 12) | 0,738 | 2/4 | Ejecutada y refutada. |
| Núcleo E-IND, sujeto | 0,971 | 0,892 | 0,930 | 5.236 (*n* = 33) | 0,698 | 0/4 | La identidad elevó F1 sin cambiar las detecciones. |
| Vocabulario nativo bare_head | 0,382 | 0,371 | 0,377 | 3.919 (*n* = 13) | 0,940 | 3/4 | Alerta temprana, con mayor costo en falsos positivos. |

***Nota.*** Las métricas temporales se calcularon sobre 34 episodios evaluables de 35 en el bloque de rodaje, y el número entre paréntesis de la columna de latencia es la cantidad de episodios confirmados, mientras que la media se promedia por clip con alerta confirmada, un conteo menor cuando un mismo clip contiene las dos condiciones. Los falsos positivos se cuentan sobre los cuatro clips negativos y no incluyen re-alertas.

La histéresis rescató evidencia intermitente. CR-02 confirmó sus 7 episodios, con recall 1,000 y SDR 0,281, aunque requirió una latencia de alerta de 8.572 ms frente a 4.314 ms para CR-01. Las dos medias se promediaron por clip con alerta confirmada, siete en CR-02 y veintiuno en CR-01. La diferencia fue coherente con ventanas de confirmación de 7,0 y 4,0 s. Una detección sostenida sólo durante una fracción del episodio pudo producir una alerta correcta cuando acumuló evidencia suficiente dentro de la ventana. La Figura 4.6 muestra un fotograma con la alerta ya confirmada. Las referencias por severidad de la sección 17.1.7.5 no se usaron como criterio de aceptación, porque el propio protocolo las condiciona a una recalibración previa que esta evaluación no realizó, y sus valores se leen como dato.

**Figura 4.6**

*Fotograma con alerta confirmada de CR-01*

⟦FIGURA: no extraída — ver el .docx⟧

***Nota.*** Fotograma del clip a_p1_c04 del bloque de rodaje a los 8,5 s, en la corrida de línea de base, con la alerta emitida a los 7,3 s y el motor en estado sostenido. El casco visible sobre la mesa, que el detector marca en cuadros vecinos, no suprime la condición, porque CR-01 se evalúa sobre la región del sujeto y no sobre la escena.

La identidad temporal fue la capa con mayor aporte medido dentro del banco. Con las mismas detecciones, la granularidad por sujeto elevó el F1 de 0,789 a 0,930, una diferencia de 0,141 sobre los 34 episodios evaluables. En el escenario de mayor dificultad el resultado pasó de 0,400 a 1,000, es decir de dos episodios confirmados sobre cinco a los cinco. La mejora no provino del detector, sino de evitar que la evidencia de personas distintas se mezclara dentro de un mismo estado de escena.

El vocabulario activo también se comportó como una variable experimental. Sobre la combinación de contraste base-560, un ensayo posterior mantuvo fijos el modelo, el evaluador, el conjunto de patrones, la referencia y los tiempos, y sumó al vocabulario una sola palabra, la de cabeza descubierta. El F1 por episodio bajó de 0,704 a 0,622, el recall de 0,735 a 0,676 y la precisión de 0,676 a 0,575. La interacción entre términos de un mismo vocabulario no resultó despreciable, de modo que dos configuraciones sólo son comparables cuando declaran el vocabulario completo que vieron.

El estrato de obra real no guionada se informó por separado y comprendió 13 clips. Una revisión ciega encontró que 5 de las 7 declaraciones de episodio eran errores de anotación por sobre-declarar estados que no resultaban observables, y dejó 2 episodios evaluables y 11 clips negativos. Ese denominador impidió ordenar granularidades. El resultado robusto del estrato fue la asimetría de falsos positivos, 26 con granularidad de escena frente a 323 con granularidad por sujeto sobre los mismos 11 clips negativos. Esa asimetría es el *ΔFP_tracking* que adopta el marco de métricas de la sección 17.1.7, y su signo es el contrario al del riesgo que la sección 17.1.10 anticipaba, que el seguimiento agregara complejidad sin reducir falsas alarmas.

Sobre el único tramo continuo de cumplimiento, de 6 minutos y 9,6 segundos, los conteos fueron 3 falsos positivos con granularidad de escena y 190 con granularidad por sujeto. Las tasas de 29,2 y 1.850,8 falsas alarmas por hora se derivan de esa exposición de 0,1027 h y se informan como magnitudes derivadas, nunca como cota operativa, porque la exposición disponible estuvo casi treinta veces por debajo de la necesaria para sostener una.

#### 17.5.5. Tiempo real

La evaluación en vivo examinó qué parte del resultado temporal sobrevivía cuando la densidad de procesamiento descendía respecto de la evidencia disponible. El banco se representó a 30 fps, mientras que el camino en vivo entregó entre 1,16 y 4,42 fps. Para cubrir esa franja, los 34 clips del bloque de rodaje se remuestrearon de manera pareada a cuatro densidades, de 30 a 1,15 cuadros por segundo. La Tabla 54 reúne esas mediciones junto con las de integridad y latencia por tramo.

**Tabla 54**

*Resultados del camino en vivo por densidad, integridad y tramo temporal*

| **Eje** | **Condición o material** | **Resultado** | **Denominador** | **Lectura** |
| --- | --- | --- | --- | --- |
| Densidad | Referencia del banco, 30 fps | Escena 0,789 · sujeto 0,930 | *n* = 34 episodios evaluables | Punto de partida de la comparación. |
|  | Techo en vivo, aproximadamente 4,29 fps | Escena 0,794 · sujeto 0,866 | *n* = 34 episodios evaluables | La ganancia por identidad se conservó. |
|  | Intermedia, aproximadamente 2,00 fps | Escena 0,738 · sujeto 0,875 | *n* = 34 episodios evaluables | La pérdida no avanza de manera uniforme. |
|  | Peor caso, aproximadamente 1,15 fps | Escena 0,646 · sujeto 0,742 | *n* = 34 episodios evaluables | La restricción redujo ambos resultados sin invertir el orden. |
| Identidad | Cuatro densidades medidas | Ganancias de F1 +0,141 · +0,072 · +0,137 · +0,096 | *n* = 4 densidades sobre 34 clips; remuestreo pareado por clip | El intervalo empírico excluyó el cero en las cuatro condiciones. |
| Integridad | Relectura frente a transmisión | 0 eventos perdidos · paridad byte a byte verificada en una corrida y protegida por prueba automatizada | *n* = 6 corridas del rodaje para los eventos. *n* = 1 corrida para la paridad | El transporte no alteró la evidencia. |
| Latencia | Sobrecarga de la plataforma con detector simulado, en diferido | p50 14,7 - p95 31,8 ms | *n* = 20 unidades | Costo propio de la cadena sin inferencia, dentro del presupuesto de la sección 17.1.7. |
| Latencia | Detector open-vocabulary en vivo | p95 630–890 ms | *n* = 47, 93 y 55 unidades procesadas en las tres corridas en vivo | Fuera del presupuesto; la corrida lo declaró. |
| Captura | Antes del retiro de la unidad | 202–217 ms | medianas por corrida; *n* = 47 a 295 unidades procesadas en cada una de las seis corridas | No está incluida en el tramo anterior. |
| Alerta | CR-01 en vivo | 7 alertas: 4,1–4,6 s | *n* = 7 confirmaciones | Ventana: 4,0 s. |
| Alerta | CR-02 en vivo | 3 alertas: ≥ 7,1 s | *n* = 3 confirmaciones | Ventana: 7,0 s. |
| Canal | Bus de alertas a confirmación del canal | p95 64,534 ms · sostenido 102,025 ms | *n* = 460 · sostenido *n* = 104 | Tramo separado; no se suma a la alerta del sistema. |

***Nota.*** Los percentiles pertenecen a tramos con relojes distintos y no se suman. El tramo desde el retiro de la unidad comienza en el dequeue, no en la captura de la escena.

La cobertura del episodio no se comparó entre cadencias porque depende de cuántas unidades sobreviven al muestreo. Tampoco se comparó la latencia agregada entre densidades sin controlar la supervivencia, porque los episodios que no alcanzan a confirmar desaparecen del promedio y lo sesgan. Entre los episodios supervivientes, el costo de bajar la densidad fue de 0,7 a 1,3 s sobre ventanas de 4 a 7 s, medido sobre 21, 20 y 16 episodios comunes a las cadencias comparadas. Entre la densidad del banco y el techo del camino en vivo el resultado por escena no cambió de manera apreciable y el resultado por sujeto perdió 0,064, mientras que en la densidad más baja la caída ya alcanza 0,143 y 0,188 respectivamente. Con 34 episodios evaluables, las diferencias del orden de un episodio, 0,029 de recall, quedan dentro de la resolución del banco y no se leen como orden.

La medición confirmó además la separación entre captura, procesamiento y distribución. Los tres tramos corresponden a relojes distintos y por eso sus percentiles no se suman. El del tramo de distribución describe el intervalo desde el bus de alertas hasta la confirmación del canal, y no la latencia completa de la plataforma.

#### 17.5.6. Caminos probados y no adoptados

Los caminos no adoptados se evaluaron contra criterios fijados antes de leer sus resultados. La estrategia directa quedó descartada por un veto de precisión, cuyo umbral de 0,5 se fijó de antemano en el pre-registro de la comparación de estrategias y quedó muy por encima del valor obtenido. La brecha que ya mostraba en el estado por persona se amplió al atravesar el motor de patrones.

La fusión híbrida por disyunción fue ejecutada y refutada, porque el recall descendió respecto del núcleo indirecto en lugar de crecer. La unión de evidencia no resultó monótona dentro del motor de patrones, ya que las detecciones más tempranas desplazaron confirmaciones fuera de la ventana de referencia. La variante por conjunción no se ejecutó, porque no podía medirse contra el banco sin romper la comparabilidad de las seis combinaciones. La familia MM-Grounding-DINO se integró por el mismo mecanismo de adaptación y se archivó durante la selección de modelos, sobre el banco anterior al congelado, de modo que no tiene cifra comparable en esta sección. Una de sus variantes no aportó ventaja en ninguna dimensión evaluada, otra entregó cajas degeneradas con origen en el punto de control publicado y no en el adaptador que las integró, y la tercera localizó mal con geometría normal.

La rama comparativa de ajuste fino se cerró como una curva de capacidad, con criterios y expectativas registrados antes de cada evaluación, y sus cifras se mantuvieron separadas de las del núcleo sin entrenamiento. La secuencia experimental y las configuraciones se documentan en la sección 17.4.7. La Tabla 55 recorre los tres puntos medidos y registra el cierre del tercer tramo sin entrenamiento.

**Tabla 55**

*Curva de capacidad de la rama comparativa de ajuste fino*

| **Punto o tramo** | **Resultado de ganancia** | **Retención y comportamiento** | **Veredicto** |
| --- | --- | --- | --- |
| Línea base sin ajuste | AP50 bare_head 0,0000 · recall de CR-01 por evidencia directa 0,0002 | Referencia previa a los tramos entrenados. | Punto de partida. |
| Primer tramo entrenado | AP50 bare_head 0,0455 · recall de CR-01 por evidencia directa 0,2089 | Quedó a 0,0045 del umbral de AP50 0,05 y redujo person de 0,7843 a 0,6932 (−11,62 %), con tope de 10 %. | Veredicto negativo pre-registrado; checkpoint no adoptado. |
| Segundo tramo entrenado | AP50 bare_head 0,0909 | Detención temprana 16/60, mejor época 1; person de 0,7843 a 0,3943 (−49,7 %) y mAP50 en dominio de 0,4193 a 0,2374 (−43,4 %); retención open-vocabulary 0,4347 a 0,1247 (−71,3 %) · *n* = 5.000 imágenes de validación de COCO 2017. | Veredicto negativo pre-registrado; checkpoint no adoptado. |
| Tramo adicional | No corresponde | Cerrado con causa técnica antes de producir una comparación interpretable. | Sin checkpoint y sin nuevo brazo contra el banco. |

***Nota.*** Los puntos medidos pertenecen a una rama comparativa separada. Las métricas en dominio de la línea base y de los dos tramos entrenados se calcularon sobre el banco congelado de 6.477 imágenes. El primer tramo agregó principalmente recall y el segundo, AP, de modo que no existe una combinación ajustada universalmente superior. Los tres puntos corresponden a la variante s de YOLOE-26. La retención open-vocabulary se midió sobre un material ajeno al dominio, distinto del estrato de 5.000 imágenes del banco.

El segundo tramo duplicó el AP50 de cabeza descubierta respecto del primero, pero colapsó durante el entrenamiento y falló las dos retenciones. El patrón conjunto mostró que el límite no fue capacidad de cómputo sino estructura experimental, con 2.946 imágenes de ajuste frente a 10,35 millones de parámetros, un conjunto cuya composición, regla de partición y configuración de entrenamiento declara la sección 17.4.7. Ningún checkpoint se adoptó como modelo de servicio, y los veredictos negativos se conservaron como resultados pre-registrados y no como trabajo pendiente.

#### 17.5.7. Lo no ejecutado y lo no implementado

Las condiciones de Nivel 2 y Nivel 3 no se implementaron en el núcleo evaluativo porque el material disponible no aportaba verdad de terreno del dominio ni evaluadores relacionales, zonales o de trayectoria que pudieran validarse. Incorporarlas habría producido capacidades sin medición defendible y habría confundido extensión arquitectónica con resultado experimental.

Las métricas formales de seguimiento multiobjeto tampoco se calcularon, porque faltó una referencia de identidad apta para ese propósito. La exclusión no alcanzó a la capacidad de identidad temporal, que sí fue implementada y medida por su efecto sobre la alerta. La ganancia informada más arriba y su persistencia en las cuatro densidades pertenecen a esa capacidad y no a una métrica de seguimiento.

La preselección liviana en el dispositivo de captura fue implementada para la fuente propia y caracterizada mediante una comparación pareada. Descartó el 87 % de las unidades antes de abandonar el dispositivo, 206 de las 236 que vio la compuerta, frente a las 277 que procesó la rama sin preselección, y permaneció deshabilitada en todas las corridas evaluativas. La exclusión fue deliberada, porque un filtro de cuadros sin persona habría suprimido la evidencia sostenida que la medición de falsas alarmas debía observar y habría superpuesto el error de un detector auxiliar sobre la cadena evaluada.

Tampoco se sostuvo una cota operativa de falsas alarmas. Para hacerlo se requerían aproximadamente 3 h de cumplimiento anotado, mientras que la exposición continua disponible fue de 0,1027 h. La tasa horaria se reportó como derivación observacional, pero el material no habilitó una afirmación poblacional.

Finalmente, la comparación temporal directa entre una fuente en vivo y su reproducción desde clip se declaró no interpretable. Sin un ancla común entre el reloj de pared y el tiempo del medio, el emparejamiento habría mezclado desfases instrumentales con el comportamiento de la plataforma.

El sub-experimento formal que evaluaba cada prompt en aislamiento y dentro del vocabulario completo no se ejecutó sobre las combinaciones finalistas. La pregunta que lo motivaba quedó respondida por el contraste de variable única informado más arriba, que midió el costo de sumar un término al vocabulario activo.

El marco de métricas admite además medidas que esta evaluación no reporta, y su estado se declara en lugar de omitirse. El tiempo hasta la primera detección se computó en todas las campañas y no se informa aquí, porque la comparación entre combinaciones se resolvió con la latencia de alerta, que es la que integra el motor de patrones. La precisión media promediada sobre el rango de umbrales de solapamiento quedó sin computar, porque la lectura se fijó en un único umbral. El percentil 99 de latencia se computó por corrida y no se consolidó como resultado comparativo, porque las corridas en vivo procesaron entre 30 y 295 unidades, muy por debajo de lo que ese percentil requiere. El consumo de memoria del acelerador se registró por corrida y no se consolidó como resultado comparativo, porque describe al perfil cargado y no a la combinación evaluada. Los benchmarks públicos de seguimiento multiobjeto previstos en la estrategia de datos no se ejecutaron, por la misma falta de referencia de identidad que excluyó a sus métricas. La curva de falsos positivos en función de la duración de la ventana, que la sección 17.1.5.2 prevé como eje de la calibración empírica, no se ejecutó, y las ventanas se usaron con sus valores de protocolo.

Ocho limitaciones acotan la lectura de todo lo anterior. La tasa de falsas alarmas por hora no sostiene una cota operativa. La referencia temporal no tuvo doble anotación ni medida de acuerdo entre anotadores. Los bordes de episodio se adjudicaron por criterio único en seis clips. El material guionado proviene de un solo bloque de rodaje, y la medición sobre obra real precisó esa limitación sin levantarla, porque caracteriza por mecanismo dónde el sistema deja de ser evaluable en lugar de validarlo sobre obra real. Los escenarios quedaron desbalanceados, de modo que todo resultado se reporta por estrato además del agregado. El seguimiento no tiene métricas formales en obra real con multitud, aunque un clip con 127 personas mostró la fragmentación de identidades que explica la precisión por sujeto de ese estrato. Una de las fuentes de imágenes conserva licencia parcial. Y la condición de chaleco no quedó cerrada al nivel del estado por persona.

### 17.6. Documentación técnica, repositorio y evidencias de cierre

La implementación y la evaluación dejaron un conjunto de componentes, configuraciones y registros que permite examinar cómo se produjo cada resultado. En esta sección, se establece qué se conservó, qué verificaciones lo respaldaron y hasta dónde alcanza la reproducción de la evidencia.

#### 17.6.1. Organización del software y de la documentación

El proyecto se organizó en cinco repositorios de software y datos, complementados por un repositorio documental. El plano de medios reunió las fuentes visuales, los adaptadores de inferencia, la normalización de las detecciones y su instrumentación. El plano de control concentró la lectura de eventos, la asociación temporal por sujeto, la evaluación de patrones y el registro de alertas. El soporte experimental integró el orquestador, la consola de inspección, los catálogos de configuración y la consolidación de resultados. El repositorio de datos conservó los procedimientos de preparación, las anotaciones, los manifiestos y los registros de procedencia y licencias. El módulo de distribución reunió la política de notificación, la entrega por MQTT y la persistencia de sus resultados.

Esta organización separó la evolución del código de la conservación de los materiales experimentales. Los pesos de los modelos y las imágenes o videos originales no se incorporaron indiscriminadamente al control de versiones. En cambio, se conservaron las referencias necesarias para identificar los insumos, reconstruir su preparación y relacionarlos con los resultados derivados. La disponibilidad de una anotación o de un manifiesto no se interpretó como autorización para redistribuir el material visual al que remite.

Las ramas experimentales se distinguieron de la línea de implementación adoptada: una modificación medida no se presentó automáticamente como parte de la versión operativa. La unidad de identificación de una ejecución fue la revisión de código junto con su configuración efectiva, no el nombre mutable de una rama.

#### 17.6.2. Identificación de las ejecuciones y conservación de la evidencia

El manifiesto de una ejecución experimental vinculó las corridas de los servicios con la fuente, el perfil del modelo, el vocabulario activo, el conjunto de patrones y las opciones de instrumentación. La conservación de la configuración efectiva permitió distinguir los parámetros solicitados de los aplicados. De este modo, dos ejecuciones con el mismo modelo nominal pudieron diferenciarse por resolución, umbrales, prompts, granularidad o política temporal, sin atribuir sus resultados a una familia de detectores en abstracto.

El inventario de la sección 17.4.5 establece los artefactos producidos por cada componente. Los eventos de percepción conservaron la evidencia que recibió el plano de control, los cambios de estado y las alertas permitieron reconstruir su interpretación temporal y el registro del distribuidor vinculó cada intento de entrega con la alerta que lo originó. Los reportes experimentales constituyeron proyecciones de esos registros, no una fuente independiente capaz de reemplazarlos.

La regla de persistencia antes de publicación desacopló la conservación de los hechos de su transporte en vivo. Una vez finalizada una corrida, los eventos pudieron releerse para inspeccionar la secuencia o repetir la evaluación del plano de control, sin que el canal de mensajería hubiera conservado el historial. Esta propiedad no convierte al transporte en durable ni demuestra ausencia de fallas bajo cualquier carga, más bien preserva una vía de auditoría independiente del canal empleado durante la ejecución.

La cadena de una alerta pudo rastrearse hasta el sujeto o la escena evaluada, la evidencia perceptiva, el patrón, la primera evidencia y la unidad visual que confirmó la condición. La distribución añadió el canal y el resultado de entrega sin modificar la semántica de la alerta interna. Como el registro de los intentos fallidos y de los descartes definitivos permaneció separado del de confirmación del patrón, contar filas del registro de distribución no equivale a contar alertas distintas ni entregas satisfactorias.

#### 17.6.3. Verificaciones automatizadas y alcance de la comprobación

Las pruebas automatizadas verificaron propiedades de los módulos y de sus fronteras. En el plano de medios se comprobaron la configuración de las fuentes, el ciclo de vida de la corrida y la producción de los artefactos esperados. En el plano de control se verificaron la evaluación de patrones, la asociación determinista por sujeto y la relectura de eventos. Las pruebas de integración examinaron la correspondencia entre el camino por archivo y el camino por bus, así como la conservación de la evidencia durante el cierre de las ejecuciones.

En el soporte experimental se verificaron la orquestación y la consolidación de los registros. En distribución se comprobaron la idempotencia, la supresión de notificaciones conforme a la política configurada, el tratamiento de los intentos fallidos y la entrega contra un broker MQTT real. Estas comprobaciones respaldan las propiedades ensayadas y el estado implementado de la cadena completa; no reemplazan la evaluación de precisión, latencia o robustez presentada en la sección 17.5.

El control del material experimental incluyó dos verificaciones complementarias. La primera contrastó las cifras declaradas con los artefactos de evaluación y sus denominadores, y detectó inconsistencias entre los resultados conservados y sus resúmenes. Su cobertura no incluyó una recomputación automática de todas las cifras de percepción por imagen, que tuvieron una comprobación específica. La segunda verificó la organización del material de video, la separación de estratos, las exclusiones, la correspondencia de las anotaciones y la integridad de los elementos congelados.

La reconstrucción del banco de imágenes fue comprobada por el equipo y reprodujo el artefacto congelado byte a byte. Asimismo, las verificaciones de relectura respaldaron el determinismo de los componentes que operan sobre eventos conservados. Son propiedades distintas de repetir una nueva captura o una inferencia en otro entorno, las cuales incorporaron condiciones de fuente, hardware y software que deben declararse y volver a medirse.

#### 17.6.4. Estado de entrega y límites de reproducibilidad

Los planos de medios y control, el soporte experimental y la distribución de alertas quedaron implementados e integrados en el flujo evaluado. La identidad temporal por sujeto también quedó implementada y medida, cuya presencia no implica reconocimiento de identidad personal ni validación mediante métricas MOT. La rama de ajuste fino conservó sus configuraciones, registros y veredictos como evidencia de un experimento concluido, sin incorporar un checkpoint ajustado al núcleo operativo.

El empaquetado en contenedores quedó definido y validado por configuración, con las especificaciones de construcción de los servicios y su composición. El despliegue no fue verificado, de tal forma que no se ejecutó la construcción de las imágenes ni la prueba integral de arranque y funcionamiento. En consecuencia, ese empaquetado no se presenta como evidencia de portabilidad ejecutada. Su documentación operativa acompaña al software, y el Anexo E delimita el camino de reproducción y las comprobaciones que respaldan los resultados.

El cierre dejó, por tanto, una plataforma experimental documentada y una cadena de evidencia inspeccionable, con los alcances de reproducción que delimita el Anexo E. Las condiciones de acceso y reutilización del material, incluida la referencia conjunta de los videos de obra real, se declaran en el Anexo F.

## 18. Cierre del proyecto

### 18.1. Respuesta a la hipótesis y alcance de la factibilidad

El proyecto mostró la factibilidad técnica de integrar detección open-vocabulary, procesamiento de video, estabilización temporal y distribución de alertas en una plataforma experimental trazable. La respuesta a la hipótesis de la sección 12.3 es afirmativa en ese alcance y condicionada respecto de su utilización operativa: se construyó y evaluó una cadena funcional sin ajustar los pesos del núcleo, pero no se demostró una solución general de seguridad en obra ni el cumplimiento simultáneo de todos los objetivos de calidad y latencia.

La evidencia principal es la evaluación por episodio de la sección 17.5.4. Con el perfil gdino-tiny-560, la estrategia indirecta E-IND y granularidad por sujeto, el F1 de alertas fue 0,930 sobre los 34 episodios evaluables del bloque de rodaje, frente a 0,789 con granularidad por escena y las mismas detecciones. Ambas configuraciones produjeron cero falsos positivos en los cuatro clips negativos de ese bloque. El resultado establece un aporte de la plataforma sobre una entrada perceptiva constante; no demuestra superioridad del detector frente a un modelo supervisado ni ausencia de falsas alarmas fuera del material observado.

La distinción es consistente con la fundamentación de las secciones 15 y 16. Los antecedentes de detección de EPP con modelos visión-lenguaje examinan la viabilidad de reconocer y relacionar entidades visuales, pero no sustituyen una evaluación de alertas temporales bajo las condiciones del proyecto (Choi y Greer, 2024; Chen y Zou, 2025). El aporte propio fue convertir esa posibilidad en una cadena configurable y medir por separado percepción, estado por persona, alerta por episodio y temporalidad de ejecución. No se equipararon los valores de AP publicados en otros conjuntos con el F1 de episodios obtenido aquí.

Las conclusiones siguientes distinguen resultados establecidos dentro del protocolo, evidencia direccional, tendencias y cuestiones no cerradas. Una estimación puntual favorable no se trató como diferencia establecida cuando su intervalo de confianza incluyó el cero. Esta regla delimita la fuerza del resultado, sin transformar una ausencia de significación en prueba de equivalencia.

### 18.2. Expresividad semántica, selección del perfil y extensibilidad

La selección de un modelo no pudo resolverse mediante su rendimiento general publicado. En el estrato de obra curada de 147 imágenes, gdino-tiny-560 encabezó el mAP50 por delante de gdino-base-560 y de yoloe-26x, y la sección 17.5.2 reportó que conservó el liderazgo en el banco completo, integrado por ese estrato y otros dos de mayor tamaño. El veredicto de retenerlo como perfil operativo quedó establecido para las combinaciones y los materiales evaluados, no como clasificación universal de las familias.

El perfil base conservó un papel distinto. La sección 17.5.2 lo retuvo como contraste especializado en cabeza descubierta y chaleco, no como reemplazo general del perfil operativo. En el mismo estrato, su AP de chaleco fue 0,582 frente a 0,520 del perfil operativo. Esa ventaja en una clase no implicó el mejor resultado de la plataforma completa, y por eso el contraste se justifica por el comportamiento de la combinación en condiciones concretas y no por el tamaño del modelo.

La comparación de estrategias mostró por qué expresar una condición en lenguaje no equivale a obtener una medición confiable de su ausencia. En el subconjunto curado de CR-01, E-IND ya superaba a E-DIR en la comparación por persona. En el nivel temporal, la formulación directa obtuvo una precisión de 0,146 sobre los 34 episodios evaluables del rodaje, por debajo del umbral de 0,5 fijado para su aceptación. Su exclusión como núcleo es un resultado establecido por un criterio previo a la evaluación, no una conclusión general sobre la imposibilidad de representar negaciones mediante lenguaje.

La estrategia indirecta aportó una explicación inspeccionable de la decisión: una persona detectada, una región de asociación y la ausencia de evidencia del EPP en esa región. Sin embargo, la ausencia de una detección puede deberse a una limitación perceptiva. La trazabilidad permite revisar esa diferencia, pero no la elimina. En CR-02, la comparación por persona quedó abierta: F1 de 0,479 con E-IND y de 0,418 con E-DIR sobre un único estrato y con intervalos solapados. El éxito temporal de esa condición no autoriza a declarar resuelta su clasificación por persona.

La extensibilidad sin entrenamiento sí fue ejercida. La incorporación de machinery produjo AP50 de 0,662 sin ninguna corrida de entrenamiento, según la sección 17.5.2. Esto establece la posibilidad de añadir una clase por configuración en el material ensayado. No establece extensibilidad semántica automática: sobre el mismo material, vehicle no produjo detecciones cuando acompañó a machinery y, de manera aislada, obtuvo AP de 0,026 al localizar la propia maquinaria. El costo de entrenamiento pudo evitarse, pero el costo de validación permaneció.

Esa sensibilidad también alcanzó al vocabulario del núcleo. Con gdino-base-560, E-IND y las demás condiciones constantes, añadir la consulta de cabeza descubierta redujo el F1 temporal de 0,704 a 0,622 en ese bloque. El resultado demuestra que ampliar el vocabulario puede modificar detecciones de otras clases y degradar una decisión posterior. No reemplaza el ensayo factorial de vocabulario aislado frente a completo que el protocolo contempló y no se ejecutó.

### 18.3. Aporte temporal de la plataforma y cambio de régimen en obra real

La separación entre detección y alerta permitió medir el aporte de la asociación temporal sin volver a entrenar ni ejecutar otro detector. En el rodaje, cambiar de escena a sujeto produjo, con detecciones idénticas, el salto de F1 citado en la sección 18.1. La diferencia conservó signo positivo e intervalos que excluyeron el cero en las cuatro cadencias de remuestreo regular de la sección 17.5.5. La mejora de las alertas por identidad temporal queda establecida dentro de ese bloque y ese procedimiento; no equivale a una evaluación MOT del tracker ni a una garantía de conservación de identidades en cualquier escena.

La persistencia temporal permitió confirmar una condición aún con evidencia intermitente. Para CR-02, E-IND con granularidad por escena recuperó los siete episodios evaluables del rodaje, con recall de 1,000 y SDR de 0,281. El resultado establece que, bajo las ventanas configuradas y esa cadencia, la confirmación temporal pudo sostenerse sin detección correcta continua. No significa que la histéresis recupere información ausente: el costo y el límite de esa recuperación dependen de que exista evidencia suficiente y oportuna.

La fusión por disyunción refutó una expectativa del propio diseño experimental. En ese bloque, el recall pasó de 0,824 con E-IND a 0,353 con E-HYB por disyunción. Incorporar evidencia adicional no aseguró una mejora de la alerta, porque la confirmación pudo adelantarse respecto de la ventana de referencia y perjudicar la correspondencia temporal del episodio. La refutación es establecida para esa regla de fusión y no se extiende a la variante por conjunción, que no se ejecutó. El rendimiento de una composición temporal no puede deducirse de la unión de detecciones por imagen.

El estrato de obra real impidió generalizar el resultado favorable del rodaje. Tras la revisión de su referencia, quedaron dos episodios evaluables y once clips negativos. En estos últimos se registraron 26 falsos positivos por escena y 323 por sujeto. Ese contraste caracteriza una asimetría de falsas alertas sobre material común; los dos episodios positivos no permiten ordenar las granularidades por F1. La misma capacidad de mantener estados por sujeto que fue útil en el rodaje pudo multiplicar oportunidades de confirmación errónea bajo fragmentación y dificultades perceptivas.

La evaluación intermedia sobre 17 clips de obra real —los 13 del estrato temporal y cuatro de un piloto— corroboró la necesidad de conservar esa frontera. Con E-IND a 2 Hz y sin motor temporal, CR-01 obtuvo F1 de 0,031 y CR-02 de 0,018, sobre más de diez mil cuadros con persona juzgables en cada condición. La precisión, inferior a 0,02 en ambas, fue la principal restricción. Esta evidencia no valida un uso operativo en obra real: delimita la distancia entre una condición visualmente formulable, una condición anotable y una condición correctamente reconocida por el sistema.

Tampoco el control de negativos del rodaje permite sostener una cota horaria. En el único clip negativo continuo de obra real, de 6 minutos y 9,6 segundos, las tasas derivadas fueron 29,2 falsas alertas por hora con granularidad de escena y 1.850,8 por sujeto. La duración observada, no una hora de exposición, es el respaldo de esas tasas. El resultado mantiene la limitación de exposición de la sección 17.5.7 y no autoriza una promesa de falsas alarmas máximas.

### 18.4. Funcionamiento en vivo y restricciones de oportunidad

El funcionamiento en vivo quedó demostrado, pero no se identificó con el cumplimiento del presupuesto de latencia. Con gdino-tiny-560 y OAK-D, el p95 del tramo entre el dequeue y la finalización de la inferencia se ubicó entre 630 y 890 ms en tres corridas. Esos valores excedieron el presupuesto de referencia. No son una medición desde el sensor: la captura hasta el dequeue se instrumentó por separado para OAK-D, mientras que ese tramo no se midió para RTSP.

En el rodaje en vivo, CR-01 produjo siete confirmaciones legítimas entre 4,1 y 4,6 segundos para una ventana de 4 segundos; CR-02 produjo tres desde 7,1 segundos para una ventana de 7 segundos. Estas observaciones respaldan el funcionamiento temporal del patrón bajo la configuración ensayada. No convierten el tiempo de inferencia en latencia completa de alerta ni demuestran una equivalencia cuantitativa entre captura en vivo y procesamiento diferido del mismo episodio.

El remuestreo regular permitió examinar el efecto de disponer de menos evidencia temporal sin cambiar las detecciones originales. En los 34 episodios evaluables del rodaje, el F1 por escena fue 0,789 a 30 FPS, 0,794 a 4,29 FPS, 0,738 a 2 FPS y 0,646 a 1,15 FPS. Las diferencias agregadas respecto de la cadencia completa no excluyeron el cero: se interpretan como una tendencia con un mecanismo plausible, no como un efecto agregado establecido. En el subconjunto de mayor dificultad, de cinco episodios, la pérdida de recuperación al reducir la cadencia aportó evidencia direccional, cuyo tamaño no permite extrapolar una curva general.

La granularidad por sujeto mantuvo una ventaja dentro de cada cadencia, pero el contraste cruzado entre cadencias distintas no es concluyente. Tampoco corresponde comparar SDR entre cadencias, porque cambia el instrumento con el que se observa la continuidad de la evidencia.

La distribución completó un tramo externo verificable. El p95 entre el bus de alertas y la confirmación MQTT fue 64,534 ms sobre 460 entregas en vivo, y 102,025 ms en el régimen sostenido, sobre 104 entregas. El resultado establece el desempeño de ese tramo bajo las condiciones ensayadas. No mide recepción consciente por un operador, respuesta humana ni reducción de accidentes. Sus percentiles no se suman a los de captura o inferencia para fabricar una latencia extremo a extremo que no se midió.

### 18.5. Interpretación de la rama de ajuste fino

La literatura de adaptación advierte que modificar pesos puede deteriorar representaciones útiles fuera del dominio de ajuste y que el efecto depende de qué parámetros se actualicen (Kumar et al., 2022; Lee et al., 2023). Ese antecedente justifica evaluar ganancia y retención por separado; no anticipa el resultado de una receta concreta sobre el material del proyecto.

La rama de ajuste fino no modificó la conclusión sobre el núcleo sin entrenamiento. Se ejecutó como comparación separada sobre YOLOE-26s, con una línea base explícita, criterios previos de ganancia y retención, y una secuencia de autorizaciones que mantuvo distinguibles las decisiones anteriores y posteriores a cada resultado. Los dos tramos entrenados produjeron veredictos negativos de adopción y el tercero quedó cerrado por las condiciones de activación y de linaje. Ningún checkpoint ajustado se adoptó. La secuencia experimental y sus configuraciones se documentaron en la sección 17.4.7. Los resultados que sustentan estos veredictos se presentan en la sección 17.5.6.

La curva de línea base, ajuste de la proyección de clases y ajuste de mayor capacidad mostró que recuperar una clase no basta para justificar una variante. En el ajuste de la proyección de clases no se alcanzó la ganancia exigida y se incumplió la retención de persona. En el de mayor capacidad se superó el criterio de ganancia de cabeza descubierta, pero fallaron las retenciones del dominio y de vocabulario abierto. Estos veredictos se establecieron sobre el protocolo de la rama, cuyo banco de dominio fue el mismo de la sección 17.5.2. No implica que ambos ajustes mejoraran o empeoraran de igual manera todas las fuentes ni que exista una variante ajustada superior según una única métrica.

La medición de retención abierta aporta un resultado especialmente claro y separado del banco de construcción. En COCO 2017 de validación, con 5.000 imágenes, la métrica de retención pasó de 0,4347 a 0,1247 en ese tramo, una reducción del 71,3 %. La recuperación de la clase objetivo no compensó esa pérdida bajo la regla de aceptación. Además, el checkpoint evaluado provino de una ejecución detenida anticipadamente en la época 16 de 60, cuyo mejor punto había quedado en la primera época. La latencia de los checkpoints ajustados no se midió, y no se infieren efectos sobre clips o captura en vivo porque sólo se evaluaron sobre imágenes.

El entrenamiento utilizó 2.946 imágenes, procedentes de construction_site_safety y ppe_siabar, con 483 de validación; CHV se excluyó para proteger la separación con el banco. El aumento de capacidad hasta 10,35 millones de parámetros entrenables no resolvió la adopción. El diagnóstico del experimento apunta, por tanto, a la relación entre datos, capacidad y retención, y no permite reducir el resultado del primer tramo a falta de parámetros. No demuestra, sin embargo, que todo método de adaptación falle con ese volumen: no se exploró una tasa de aprendizaje intermedia ni una familia completa de técnicas eficientes en parámetros.

El cierre del tercer tramo se sostiene primero en la escalera de activación y en que la variante ajustable no preservaba el linaje del perfil desplegado. La anomalía geométrica reproducida en el checkpoint publicado de la variante tiny reforzó esa restricción, sin atribuirla al adaptador del proyecto ni extenderla a toda la familia. El resultado de la jornada fue una decisión de no adopción sustentada y auditable, no una promesa de mejoras posteriores.

### 18.6. Balance de objetivos y líneas de continuidad

El objetivo general de diseñar, implementar y evaluar una plataforma experimental se alcanzó en el alcance documentado. Los objetivos específicos de revisión, operacionalización y diseño se materializaron en un protocolo, un núcleo de condiciones y fronteras entre componentes; los de implementación y evaluación se respaldaron en las verificaciones de la sección 17.4 y en los resultados de la sección 17.5. No se equipara ese cumplimiento con haber ejecutado todas las métricas o extensiones previstas: el estado por persona de CR-02, la evaluación MOT y la validez operativa en obra real mantienen los límites ya expuestos.

El cumplimiento de los objetivos en el alcance documentado no implicó el cumplimiento del cronograma original. La implementación y la redacción final se extendieron más allá del cierre previsto para el 21 de agosto de 2026. La sección 17.2.2 cuantifica esa extensión en el horizonte de esfuerzo estimado hasta la defensa prevista para fines de septiembre. Esta desviación temporal se informa de manera separada del cumplimiento técnico y no se utiliza para explicar ni justificar capacidades no ejecutadas o resultados negativos.

Las preguntas rectoras de la sección 16.7.3 reciben respuestas de distinta fuerza. El presupuesto temporal y sus extremos de medición quedaron instrumentados por tramos, sin cierre de una latencia completa desde el sensor para todas las fuentes. Las condiciones mínimas evaluables se concretaron en CR-01 y CR-02, pero la clasificación por persona y la alerta por episodio no resultaron equivalentes. La estrategia de datos produjo bancos identificables y una separación explícita de ajuste y evaluación, aunque la referencia humana no tuvo doble anotación independiente. La infraestructura permitió ejecutar la cadena, sin asegurar el presupuesto temporal de su perfil operativo. Las métricas distinguieron niveles de análisis y permitieron aceptar o refutar combinaciones. La adaptación paramétrica se resolvió mediante una decisión negativa de adopción, no mediante su omisión. Así se cierra el vínculo con las conclusiones metodológicas de la sección 17.1.11.

El carácter asistivo permaneció como límite de interpretación. Se registraron evidencias y alertas para revisión humana, sin reconocer identidad personal, calificar cumplimiento normativo ni accionar medidas físicas. El desempeño medido no prueba reducción de incidentes, utilidad percibida por responsables de seguridad o aceptación de los usuarios: esos resultados requerirían otra evaluación. Las salvaguardas de acceso y conservación delimitan el tratamiento adoptado, sin convertir el prototipo en un sistema certificado.

Las continuidades justificadas se desprenden de lo que quedó fuera del protocolo ejecutado. La primera es ampliar la evidencia de cumplimiento sostenido y de obra no guionada, con anotación independiente y condiciones de acceso resueltas, antes de fijar una cota de falsas alarmas o generalizar el efecto del tracker. La segunda es evaluar la conservación de identidades con referencia apropiada, separando sus errores de los de percepción en escenas con múltiples personas. La tercera exige anotaciones y evaluadores adecuados antes de extender el núcleo a relaciones espaciales o condiciones de mayor complejidad.

En adaptación, una continuidad defendible exige un nuevo protocolo y un corpus independiente, junto con métodos eficientes en parámetros y criterios de retención; no consiste en continuar probando variantes contra el banco congelado hasta obtener una mejora. En distribución, los canales adicionales y la evaluación del consumo humano son extensiones distintas del servicio MQTT ya implementado. En reproducibilidad, la construcción y prueba integral del empaquetado definido permitirían comprobar una portabilidad que esta entrega no verificó. Estas posibilidades delimitan nuevas preguntas de trabajo y no comprometen su ejecución por el equipo.

El aporte final es una plataforma con evidencia que permite distinguir qué funcionó, bajo qué configuración, dónde dejó de hacerlo y qué observación falta para sostener una afirmación más fuerte. La detección open-vocabulary resultó un habilitador de experimentación y extensibilidad sin entrenamiento del núcleo; su valor quedó condicionado por la semántica del vocabulario, la observabilidad de la escena y la continuidad temporal. Esa respuesta acotada, junto con los resultados negativos y sus registros, constituye el cierre del proyecto.

## 19. Anexos

Los anexos conservan el soporte técnico, metodológico y documental de las secciones precedentes. Las comparativas de literatura, las capacidades de infraestructura y las prescripciones del protocolo se distinguen de los procedimientos efectivamente ejercidos. La reproducibilidad y las condiciones de reutilización de los materiales se desarrollan en los Anexos E y F.

### 19.1. Anexo A - Comparativas técnicas y estado del arte complementario

El Anexo A reúne comparativas complementarias que respaldan el estado del arte. La Tabla A.1 amplía el catálogo de alternativas de detección open-vocabulary y modelos relacionados; la Tabla A.2 sintetiza el alcance y las limitaciones de las métricas MOT tratadas en la sección 15.3.3.

**Tabla A.1**

*Matriz ampliada de alternativas de detección open-vocabulary y modelos relacionados*

| **Modelo** | **Familia** | **Mecanismo visión-lenguaje** | **AP zero-shot reportado** | **Rendimiento reportado** | **Licencia / disponibilidad** |
| --- | --- | --- | --- | --- | --- |
| DINO-X | Transformer | Universal Object Prompt | 59,8 (LVIS-minival) | N/D | API cerrada; Apache-2.0 aplica al SDK, no a los pesos |
| G-DINO 1.5 Pro | Transformer | Fusión cross-modal profunda | 55,7 (LVIS-minival) | N/D | API cerrada; Apache-2.0 aplica al SDK, no a los pesos |
| G-DINO 1.5 Edge | Transformer | Fusión cross-modal optimizada | 36,2 (LVIS-minival) | 75,2 FPS (A100, TensorRT) | API cerrada; Apache-2.0 aplica al SDK, no a los pesos |
| Grounding DINO Swin-L | Transformer | Feature Enhancer, selección de consultas guiada y decoder cross-modal | 52,5 (COCO); 26,1 mean AP (ODinW-35) | N/D | Apache-2.0 |
| Grounding DINO Swin-T | Transformer | Feature Enhancer, selección de consultas guiada y decoder cross-modal | 48,4 (COCO) | N/D | Apache-2.0 |
| MM-Grounding-DINO Tiny | Transformer | Pipeline unificado de grounding y detección | 50,4–50,6 (COCO); 35,7–41,4 (LVIS-minival) | N/D | Apache-2.0 |
| GLIP | Dynamic Head + Swin | Alineamiento región-palabra con fusión profunda | 49,8 (COCO); 26,9 (LVIS) | N/D | MIT |
| OV-DINO | Transformer | LASF + UniDI | 50,6 (COCO) | N/D | Apache-2.0 |
| OV-DETR | Deformable DETR | Matching condicional binario con prompts textuales o visuales | 17,4 novel (OV-LVIS); 29,4 AP50 novel (OV-COCO) | N/D | CC BY-NC-SA 4.0 |
| APE-L (D) | Transformer | Alineamiento por producto punto y encoder cross-modal | 59,6 caja (LVIS); 58,3 caja (COCO) | N/D | Apache-2.0 |
| LLMDet | Transformer + LLM | Coentrenamiento con LLM; LLM descartado en inferencia | 51,1 (LVIS-minival) | N/D | Apache-2.0 |
| DetCLIPv3 | Transformer | Formulación generativa con VLLM | 48,8 (LVIS-minival) | N/D | N/D |
| OWLv2 L/14 | ViT dual-encoder | Autoentrenamiento escalable | 44,6 (LVIS rare) | N/D | Apache-2.0 |
| Detic | *Two-stage* | Embeddings CLIP como pesos del clasificador de regiones | 17,8 rare (OV-LVIS); 27,8 novel AP50 (OV-COCO) | N/D | Apache-2.0 |
| T-Rex2 Swin-L | Transformer multimodal | Prompts textuales y visuales con fusión tardía | 46,7 texto / 46,8 visual (LVIS-minival) | N/D | IDEA License 1.0; uso no comercial |
| YOLOE-v8-L | One-stage | RepRTA + SAVPE + LRPC | 35,9 (LVIS-minival) | 102,5 FPS (T4, TensorRT) | AGPL-3.0 |
| YOLO-World-L | One-stage | RepVL-PAN contrastivo | 35,4 (LVIS-minival) | 52,0 FPS (V100, PyTorch) | GPL-3.0 |
| OmDet-Turbo-Base | Transformer para tiempo real | EFH + caché textual | 34,7 (LVIS-minival) | 100,2 FPS (A100, TensorRT + caché textual) | Apache-2.0 |
| YOLOE-v8-S | One-stage | RepRTA reparametrizable | 27,9 (LVIS-minival) | 305,8 FPS (T4, TensorRT) | AGPL-3.0 |
| Florence-2-L | Seq2Seq | Generación condicionada por instrucciones | 37,5 (COCO) | Variable | MIT |

***Nota.*** Las cifras conservan el protocolo, el conjunto de evaluación y el hardware informados por cada fuente; por ello, no constituyen un benchmark homogéneo. N/D indica información no reportada o no comparable. En DINO-X y Grounding DINO 1.5, la licencia Apache-2.0 corresponde al SDK de acceso y no a pesos abiertos. Fuente: elaboración propia basada en Cheng et al. (2024), Fu et al. (2025), Jiang et al. (2024), L. H. Li et al. (2021), Liu et al. (2024), Minderer et al. (2023), Ren, Chen, et al. (2024), Ren, Jiang, et al. (2024), Shen et al. (2023), A. Wang et al. (2025), H. Wang et al. (2024), Xiao et al. (2024), Yao et al. (2024), Zang et al. (2022), T. Zhao et al. (2024), X. Zhao et al. (2024) y X. Zhou et al. (2022).

**Tabla A.2**

*Comparación conceptual de métricas MOT y sus límites para evaluar alertas temporales*

| **Métrica** | **Qué caracteriza** | **Sesgo principal** | **Límite respecto de las alertas** |
| --- | --- | --- | --- |
| MOTA | Errores acumulados de detección y cambios de identidad | Está fuertemente condicionada por falsos positivos y falsos negativos del detector | No mide persistencia, oportunidad ni resolución de episodios de alerta |
| IDF1 | Consistencia de identidad a lo largo de una secuencia | Privilegia la correspondencia de identidad y exige anotaciones de trayectorias | No mide la condición semántica ni el comportamiento temporal de la alerta |
| HOTA | Calidad combinada de detección, asociación y localización | Resume componentes del tracker y requiere referencia MOT explícita | No sustituye la evaluación por persona ni la evaluación por episodio temporal |

***Nota.*** MOTA resume errores de detección y cambios de identidad; IDF1 enfatiza la continuidad de identidad; HOTA separa y combina detección, asociación y localización. Las tres caracterizan el seguimiento, pero no miden por sí mismas el estado semántico ni el episodio de alerta. Fuente: elaboración propia basada en Bernardin y Stiefelhagen (2008), Ristani et al. (2016) y Luiten et al. (2021).

### 19.2. Anexo B - Infraestructura, nodos y parámetros experimentales

Este anexo reúne la infraestructura de referencia y distingue sus capacidades de las funciones efectivamente utilizadas. Los roles CPN, EN y TN conservan el significado definido en la sección 17.1.4; no implican que cada servicio de la plataforma ocupe una máquina dedicada. Las especificaciones de fabricante describen el recurso, mientras que la sección 17.4 y los registros de corrida identifican su utilización experimental.

**Tabla B.1**

*Equipo de referencia del nodo central de procesamiento*

| **Componente** | **Especificación registrada** | **Alcance de la declaración** |
| --- | --- | --- |
| Equipo | HP Victus 15, modelo 15-FB2024LA | Equipo utilizado como recurso central de procesamiento. |
| Procesador | AMD Ryzen 5 8645HS, 6 núcleos y 12 hilos | Identificación del hardware; no constituye una medición de ocupación durante las corridas. |
| GPU | NVIDIA GeForce RTX 4060 Laptop, 8 GB de memoria | Recurso de inferencia del prototipo. Las latencias corresponden a las condiciones de la sección 17.5.5. |
| Memoria y almacenamiento | 32 GB DDR5 y unidad SSD NVMe de 1 TB | Capacidad registrada del equipo, no memoria o espacio consumidos por una ejecución. |
| Entorno de ejecución | Linux mediante WSL2 sobre el equipo con Windows 11 | El entorno efectivo no fue Windows nativo. |
| Decodificación | Por software en las corridas reportadas | La disponibilidad de NVDEC en el hardware no se presenta como aceleración ejercida. |

***Nota.*** Identificación del equipo y de sus componentes según el inventario experimental y las fichas de HP Inc. (s. f.), Advanced Micro Devices, Inc. (s. f.) y NVIDIA (s. f.-a). La capacidad nominal del equipo se distingue de su rendimiento medido.

**Tabla B.2**

*Fuente de captura propia y capacidades del nodo de borde*

| **Componente** | **Especificación de referencia** | **Utilización y límite** |
| --- | --- | --- |
| Cámara | Luxonis OAK-D Pro PoE | Captura propia mediante DepthAI. |
| Procesador de visión | RVC2 | Soporte del dispositivo; no ejecutó el detector OVD del núcleo. |
| Sensor RGB | Sony IMX378, hasta 12 MP | La resolución de la fuente se registró por corrida; no se presupone uso de la resolución máxima. |
| Sensores estéreo | Dos sensores OV9282 | Capacidad de hardware; la evaluación del núcleo no se fundamentó en profundidad estéreo. |
| Conexión | Alimentación PoE y Gigabit Ethernet | Integración de la fuente de captura al entorno experimental. |
| Preselección de personas | Filtro opcional en el dispositivo, con degradación segura | Implementado y caracterizado fuera del régimen evaluativo; permaneció deshabilitado en las corridas de evaluación. |

***Nota.*** Las características del dispositivo se apoyan en la documentación de Luxonis (s. f.). Su disponibilidad no implica que todas sus funciones hayan sido utilizadas. La preselección no existe para las fuentes RTSP de la plataforma.

**Tabla B.3**

*Entorno de software de procesamiento: utilizado y no ejercido*

| **Componente** | **Estado en el trabajo** | **Información necesaria para repetir una corrida** |
| --- | --- | --- |
| Entorno Python y dependencias | Entornos separados por componente | Revisión del código y dependencias de la ejecución que se reproduce. |
| Inferencia | Adaptadores de Grounding DINO y YOLOE integrados | Perfil, checkpoint, precisión numérica, resolución y umbrales efectivos. |
| Transporte interno | ZeroMQ con serialización msgpack | Fuente de eventos, configuración del bus y orden de inicialización. |
| Gobierno de servicios | HTTP gobernado por configuración | Parámetros de medios, control y distribución vinculados a la ejecución. |
| TensorRT, ONNX Runtime y DeepStream | Alternativas del análisis previo, no runtimes utilizados en los resultados presentados | No se atribuyen al prototipo optimizaciones ni latencias de estas alternativas. |
| Contenedores | Definidos y validados por configuración; despliegue no verificado | La construcción y prueba integral no forman parte de la evidencia ejecutada. |

***Nota.*** La tabla describe la implementación de la sección 17.4, no una recomendación de versiones actuales. Los manuales de TensorRT, DeepStream y ONNX Runtime documentan alternativas consideradas, no su adopción efectiva (NVIDIA, 2026a, 2026b; ONNX Runtime, s. f.).

**Tabla B.4**

*Recurso institucional para la rama de ajuste fino*

| **Aspecto** | **Recurso de referencia** | **Uso declarado** |
| --- | --- | --- |
| Institución | Clúster Mendieta, CCAD-UNC | Recurso de cómputo institucional de entrenamiento. |
| GPU por nodo | Dos NVIDIA A30, con 24 GB por GPU | La disponibilidad por nodo no implica entrenamiento multi-GPU. |
| Asignación mínima de referencia | Medio nodo, con 10 núcleos de CPU y una GPU | La asignación de cada trabajo pertenece a su registro de ejecución. |
| Memoria del nodo | 64 GB | Especificación de infraestructura, no utilización medida. |
| Función en el proyecto | Ajuste y evaluación técnica de las variantes de la rama comparativa | El TN no formó parte del camino de inferencia en vivo del prototipo. |

***Nota.*** Infraestructura según el relevamiento utilizado por el proyecto y la documentación de CCAD y NVIDIA (Centro de Computación de Alto Desempeño, 2026; NVIDIA, 2022). Los veredictos de adopción se informan en la sección 17.5.6.

**Tabla B.5**

*Identificación de las ejecuciones de ajuste fino*

| **Elemento** | **Registro conservado o condición aplicada** |
| --- | --- |
| Plataforma | Entorno Linux del clúster y ejecución de trabajos de entrenamiento. |
| Modelo de referencia | YOLOE-26s; línea base separada del núcleo zero-shot de la plataforma. |
| Primer tramo | Ajuste de la proyección de clases, con registro de los parámetros entrenables y del optimizador. |
| Segundo tramo | Ajuste del detector con las rutas de prompt congeladas; ejecución evaluada con SGD explícito desde el peso base. |
| Datos | Particiones de entrenamiento y validación de construction_site_safety y ppe_siabar, disjuntas del banco de evaluación según la regla aplicada. |
| Artefactos | Configuración, registros de entrenamiento, checkpoint evaluado, referencia de evaluación y veredicto. |
| Alcance | Evaluación sobre imágenes. No se atribuyen mediciones de clips ni de captura en vivo a los checkpoints ajustados. |

***Nota.*** La tabla conserva las condiciones materiales de la rama documentada en la sección 17.4.7. No transforma opciones candidatas de entrenamiento distribuido en procedimientos ejecutados.

**Tabla B.6**

*Parámetros de referencia y configuraciones identificadoras del núcleo*

| **Parámetro** | **Valor o regla** | **Interpretación** |
| --- | --- | --- |
| Resolución y cadencia de la fuente | Declaradas por fuente y corrida | No equivalen a la resolución de entrada del detector ni a los FPS efectivos. |
| Perfil gdino-tiny-560 | 560 px; box_threshold 0,30; text_threshold 0,25; NMS IoU 0,50; fp16 | Combinación operativa que debe identificarse completa. |
| Perfil gdino-base-560 | 560 px, con los mismos umbrales del perfil anterior | Contraste especializado; el cambio de perfil no implica equivalencia de latencia. |
| Perfil gdino-tiny de 800 px | box_threshold 0,35 | No permite atribuir exclusivamente a la resolución una diferencia de calidad frente a 560 px. |
| Confirmación de CR-01 / CR-02 | 4.000 / 7.000 ms | Ventanas metodológicas de evidencia; no son límites derivados de normativa. |
| Resolución de CR-01 / CR-02 | 2.000 / 3.000 ms | Histéresis del motor de patrones. |
| Granularidad | scene o subject, declarada en el conjunto de patrones | Cada resultado se vincula con la granularidad que lo produjo. |
| Control de re-confirmación del motor | Sin cooldown en la configuración del núcleo | La política de notificación se aplica en distribución. |

***Nota.*** Configuraciones efectivas según la sección 17.4.4. El presupuesto metodológico de latencia se conserva en la sección 17.1.7; los valores de esta tabla no lo reemplazan por un resultado medido. Para YOLOE se aplican los umbrales propios de su adaptador y no los campos inertes de otra familia.

**Tabla B.7**

*Topología y fronteras operativas de la ejecución en vivo*

| **Aspecto** | **Materialización y alcance** |
| --- | --- |
| Fuentes | Captura OAK-D por SDK y fuentes de video RTSP. |
| Gobierno | Servicios HTTP de medios, control y distribución; el orquestador y la consola son sus clientes. |
| Dato en ejecución | Canal de detecciones entre medios y control, y canal de alertas entre control y distribución. |
| Orden de arranque con distribución | Control, distribución y medios. El distribuidor requiere la identificación de la corrida de control. |
| Sincronización de publicación | El publicador de alertas espera la suscripción del distribuidor; la protección inicial no se atribuye sólo al orden de arranque. |
| Conservación | Persistencia de eventos antes de publicación y registros de entrega independientes. |
| Temporalidad | Relojes y extremos declarados por tramo. La medición de captura hasta el dequeue sólo se sostuvo para OAK-D. |

***Nota.*** Síntesis de las fronteras operativas de la sección 17.4. Los esquemas versionados conservan su función al distribuir los servicios; una topología admitida por el diseño no constituye, por sí sola, una prueba de desempeño.

### 19.3. Anexo C - Prompts, datos, datasets, benchmarks y logística

Se conserva el catálogo metodológico de prompts y la logística de datos de la sección 17.1. Las Tablas C.1, C.2 y C.3 describen opciones y condiciones del protocolo, no una declaración de que todas fueron ejecutadas. Su estado de ejercicio se informa en la sección 17.5.7.

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

***Nota.*** En las estrategias indirecta y descompuesta el separador punto y coma indica consultas independientes al modelo y su materialización depende de la sintaxis de cada detector. Para CR-05 y CR-06 no se formulan prompts integrados sino prompts de entidades componentes, y la condición completa se evalúa en el módulo de razonamiento contextual.

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

***Nota.*** Los niveles consignados son candidatos de diseño y se cierran al definir la topología y el espacio físico de prueba, siguiendo la secuencia progresiva de la sección 17.1.3.3.

**Tabla C.3**

*Logística de conversión y acceso de los datasets retenidos*

| **Dataset** | **Formato nativo** | **Formato de trabajo** | **Vía de acceso** | **Observación** |
| --- | --- | --- | --- | --- |
| SHEL5K | Pascal VOC | COCO/ODVG y/o YOLO | Mendeley Data | Conversión directa VOC→YOLO; para el pipeline de Grounding DINO, VOC→COCO→ODVG. |
| CHV | Formato nativo a inspeccionar | COCO/ODVG y/o YOLO | Repositorio del autor | Revisar estructura del paquete y términos de uso al descargar; cita obligatoria. |
| construction_site_safety | YOLO (Roboflow) | COCO/ODVG y/o YOLO | Roboflow | Requiere conversión YOLO→COCO→ODVG para el pipeline de Grounding DINO. |
| ppe_siabar | YOLO (Roboflow) | COCO/ODVG y/o YOLO | Roboflow | Requiere conversión YOLO→COCO→ODVG para el pipeline de Grounding DINO. |

***Nota.*** La secuencia de gestión se describe en la sección 17.1.6.5 y los volúmenes y versiones por fuente en la Tabla 17. El esfuerzo de conversión es directo cuando basta un paso y en dos pasos cuando exige inspección o normalización previa.

### 19.4. Anexo D - Métricas, instrumentación y bitácora experimental

Las Tablas D.1, D.2 y D.3 conservan los compromisos y los insumos del protocolo de medición. La existencia de una métrica en este anexo no implica que se haya calculado; la sección 17.5 distingue los resultados producidos de las métricas no ejecutadas o no consolidadas.

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

***Nota.*** G2A = Glass-to-Algorithm. FPS = Frames Per Second. VRAM = Video Random Access Memory. El reporte obligatorio mínimo incluye FPS efectivos, latencia G2A y uso de VRAM. Cuando sea posible, conviene registrar además GPU, RAM y CPU con muestreo periódico durante una corrida sostenida.

**Tabla D.2**

*Insumos mínimos requeridos antes de iniciar una campaña de medición*

| **Familia de métricas** | **Ground truth o insumo** | **Instrumentación mínima** | **Herramientas o artefactos** | **Salida mínima** |
| --- | --- | --- | --- | --- |
| Detección (AP, P/R) | Bounding boxes y etiquetas por imagen o cuadro. | Export de predicciones por corrida. | pycocotools o conversión COCO equivalente. | AP y P/R por variante, con punto operativo o criterio de reporte explícitamente declarado. |
| Tracking (HOTA, DetA / AssA, IDF1, MOTA, IDSW / Frag) | Boxes y track_id persistente por cuadro. | Export MOT-compatible sobre subset anotado. | TrackEval u otra implementación equivalente. | Métricas MOT sobre subset, con declaración explícita de qué métricas fueron ejecutadas y cuáles no. |
| Pipeline (FPS, latencia G2A, jitter) | No requiere GT semántico. | Timestamps por etapa del pipeline. | Logs internos y scripts de agregación. | P50/P95/P99, promedio y variación. |
| Alerta y patrón (*t_alert-system*; *t_alert-notification* si aplica; TTFD; SDR) | Inicio anotado de la condición de riesgo, duración o intervalo temporal del evento, severidad asignada y criterio de activación del patrón. | Logs con timestamps de primera evidencia positiva, inicio de patrón candidato si corresponde, patrón confirmado, alerta registrada y disponibilidad, consulta o notificación si aplica. | Motor de patrones instrumentado, registro interno de alertas, event log del pipeline, bitácora de corrida y scripts de agregación temporal. | TTFD, SDR y *t_alert-system* por episodio. *t_alert-notification* sólo si existe trayecto instrumentado. Toda métrica sin insumos se declara no aplicable. |
| Recursos (VRAM, GPU, RAM, CPU) | No requiere GT semántico. | Muestreo periódico durante la corrida. | nvidia-smi, psutil u otras herramientas del sistema. | Series temporales y resumen. |
| Fine-tuning | *Split* train/eval disjunto y baseline zero-shot explícita. | Registro de entrenamiento y evaluación. | Logs de entrenamiento y scripts comparativos. | Deltas y costo de entrenamiento, cuando aplique. |

***Nota.*** La ausencia de cualquiera de los insumos requeridos para una familia de métricas debe declararse antes de planificar la campaña experimental. En particular, no corresponde reemplazar ground truth inexistente por estimaciones informales ni interpretar logs incompletos como evidencia suficiente de desempeño. Toda métrica sin insumos mínimos deberá registrarse como no ejecutada o no aplicable, según corresponda.

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

### 19.5. Anexo E - Reproducibilidad y comprobación de la evidencia

La reproducción se organiza por material y por nivel de evaluación. Deben conservarse juntas la entrada identificada, su referencia humana, la configuración efectiva y las salidas primarias. No resulta suficiente repetir el nombre de un modelo ni disponer de una tabla agregada. La Tabla E.1 distingue los objetos que se mantienen estables y la comprobación que respalda cada reconstrucción.

**Tabla E.1**

*Artefactos de referencia y comprobaciones de reproducción*

| **Material** | **Elementos que se conservan** | **Comprobación pertinente** |
| --- | --- | --- |
| Banco de imágenes | bench_v3.json, manifiesto de composición, anotaciones y referencia de cada fuente | Integridad del archivo y de sus estratos; reproducción de la construcción del banco. |
| Vocabulario | Conjuntos de prompts identificados y congelados | Coincidencia del contenido con el utilizado por la corrida; no basta el nombre del conjunto. |
| Banco temporal | Manifiesto, clips elegibles y referencia clip_gt.v2 | Integridad, pertenencia al estrato, episodios y exclusiones; correspondencia de las correcciones de anotación. |
| Corrida de medios | Detecciones, configuración efectiva, manifiesto y procedencia | Modelo y parámetros aplicados, fuente e identificación de cada unidad visual. |
| Corrida de control | Eventos del patrón, alertas, configuración y métricas | Relectura de la evidencia bajo el mismo evaluador y reglas temporales. |
| Distribución | Registro de notificaciones, descartes definitivos y resumen | Correspondencia alerta–intento–resultado, sin contar como alertas distintas los registros de una misma entrega. |
| Resultados derivados | Evaluaciones por clip y resúmenes por condición, escenario y estrato | Coincidencia de numeradores, denominadores y reglas de agregación. |

***Nota.*** El inventario por componente se desarrolla en la sección 17.4.5. Las huellas de integridad identifican contenidos; no acreditan derechos de uso ni validez de una anotación.

La Tabla E.2 consigna la identificación de los contenidos congelados. La huella completa del manifiesto temporal corresponde al banco de 47 clips; no sustituye a la referencia histórica utilizada por los experimentos sobre el bloque de rodaje. Las identificaciones abreviadas se contrastan con el valor completo conservado en el manifiesto respectivo.

**Tabla E.2**

*Huellas de referencia de los materiales congelados*

| **Material** | **Identificación conservada** | **Alcance de la comprobación** |
| --- | --- | --- |
| Manifiesto del banco temporal de 47 clips | 3f14f50a53c0d6c57b429378544dcfb6ed87fc942640db302c53ba1470001a75 | Huella SHA-256 completa del manifiesto. |
| Banco de imágenes bench_v3.json | 4557024ecc4ee497…a4462 | Abreviatura de identificación; el valor completo se contrasta con el manifiesto del banco. |
| Estratos de obra de prueba y validación | e82eed03469665a3…af61a y b2326724b71e7776…4c58c | Identificación abreviada de cada partición; no se intercambian. |
| Estratos CHV y SHEL5K | 6d15ff9b46407511…39a7 y bf35f63bcf726c1c…d1e0f | Identificación abreviada por fuente. |
| Manifiesto histórico del bloque de rodaje | cef5082e1eb1981c…260e8 | Referencia de las comparaciones sobre ese bloque, no del banco completo. |
| Conjuntos cr01_cr02_v2_short, eind_v1 y edir_v1 | df81fd48b6daf892…b309a, 7a0126f45eb1362a…ed770 y a1278d0c34cd13be…43703 | Identificaciones abreviadas del contenido textual congelado. |

***Nota.*** El signo de elipsis identifica una abreviatura, no un valor utilizable para una verificación criptográfica completa. Las comprobaciones se realizan con las huellas completas que acompañan a los artefactos, sin completarlas por inferencia. Fuente: elaboración propia a partir de los materiales congelados.

Los materiales identificados en la Tabla E.2 se reproducen por caminos distintos, que las secuencias siguientes describen. La comprobación del banco de imágenes comienza por reconstruirlo desde las fuentes y particiones identificadas, sin reemplazarlas por una descarga actual de contenido distinto. A continuación se verifica su integridad y se evalúan las predicciones conservadas contra la referencia correspondiente. La separación de los estratos de obra curada, CHV y SHEL5K se mantiene durante el reporte, porque la composición desbalanceada del banco condiciona el agregado. La semilla de la partición de calibración se conserva cuando se reproduce la evaluación del estado por persona.

Para el banco temporal, la referencia se obtiene de las anotaciones humanas mediante una secuencia de conversión, validación y promoción al conjunto evaluable. El nivel de exportación de la herramienta de anotación debe corresponder al que espera el procedimiento de conversión: una exportación por tarea no se trata como una exportación por proyecto. Se comprueban los atributos, las correcciones adjudicadas, los intervalos de episodio y la pertenencia de cada clip al material reportable antes de calcular métricas.

La secuencia operativa distingue construcción, procesamiento y evaluación. La construcción del banco de imágenes se realiza con build_bench_v3.py; las predicciones conservadas se contrastan mediante python -m eovrt_media.tools.evaluate, indicando la corrida con --run y la referencia con --bench-coco. La relectura de detecciones se ejecuta con eovrt-control *replay* --config, el consumo en vivo con eovrt-control live --config, y la evaluación contra la referencia temporal con eovrt-control evaluate-alerts. Los argumentos concretos deben identificar los artefactos de la ejecución que se reproduce; no se reemplazan por una configuración actual que haya cambiado. Esta secuencia identifica las operaciones de reproducción, no constituye un procedimiento de instalación o despliegue.

La relectura del plano de control opera sobre los eventos de percepción conservados. Repetirla con la misma configuración permite examinar el determinismo del motor; cambiar granularidad, evaluador, vocabulario de origen o ventanas define otra combinación y exige identificarla como tal. Los clips positivos se evalúan por episodios con referencia aplicable; los negativos se conservan para el conteo de falsos positivos. Las re-confirmaciones con la condición todavía activa se contabilizan aparte y no se reclasifican como errores para modificar el F1.

La agregación conserva la unidad estadística y las exclusiones del procedimiento original. Un promedio de latencias por clip no se presenta como percentil, y los intervalos obtenidos mediante remuestreo mantienen la unidad y el pareamiento del contraste original. La precaución importa sobre todo al comparar granularidades con detecciones idénticas o cadencias obtenidas por remuestreo del mismo material.

La repetición en vivo exige, además, fijar el entorno, verificar que los servicios estén preparados y establecer las suscripciones antes de publicar los datos pertinentes. Con distribución, el orden de lanzamiento fue control, distribución y medios. La espera de la suscripción por parte del publicador protege el comienzo del canal de alertas y no se sustituye por una pausa supuesta. El periodo de preparación del modelo permanece fuera de la ventana de medición.

La definición de G2A aplicada en este trabajo se restringe al intervalo desde el dequeue hasta el resultado de inferencia. Al relacionarla con la literatura de latencia de video debe mantenerse explícita la diferencia con el extremo físico de captura (Bachhuber et al., 2018). Cada tramo conserva sus hitos y su dominio de reloj, de modo que una medición ausente de RTSP no se completa con la cifra de captura de OAK-D.

Las pruebas automatizadas y los verificadores descritos en la sección 17.6.3 permiten comprobar las propiedades para las que fueron construidos. La reproducción byte a byte del banco no equivale a una repetición independiente de toda la inferencia sobre otro equipo, y el empaquetado definido no acredita un despliegue ejecutado, según lo delimitado en la sección 17.6.4. El material conservado respalda la inspección y reconstrucción de las ejecuciones documentadas, sin presentar una validación externa de portabilidad que no existe.

### 19.6. Anexo F - Procedencia, licencias y tratamiento del material

El acceso a código, pesos, anotaciones y material audiovisual se trata por separado. La licencia de un repositorio no se atribuye automáticamente a todos los pesos o datos que utiliza; del mismo modo, que un video sea públicamente visible no acredita autorización para redistribuirlo. La Tabla F.1 identifica las fuentes que sostuvieron las ejecuciones y el tratamiento documentado para cada una. Las cantidades efectivamente incorporadas se reportan en las secciones 17.4 y 17.5, y no se sustituyen por los volúmenes actuales de los portales de descarga.

**Tabla F.1**

*Procedencia de los datos y condiciones de conservación*

| **Fuente** | **Función en el proyecto** | **Condición registrada y tratamiento** |
| --- | --- | --- |
| construction_site_safety | Obra curada del banco de imágenes y una parte del conjunto de ajuste | Fuente de Roboflow con CC BY 4.0; atribución al conjunto utilizado. |
| CHV | Estrato de evaluación de persona, casco y chaleco | Sin licencia formal identificada; declaración informal de uso libre de los autores, con cita. Imágenes no redistribuidas. |
| SHEL5K | Estrato de imágenes con cabeza descubierta | CC BY 4.0 en la versión identificada de Mendeley Data; atribución al artículo y al conjunto de datos. |
| ppe_siabar | Segunda fuente del conjunto de ajuste | Fuente de SiaBar en Roboflow, con CC BY 4.0; atribución y separación respecto de la evaluación. |
| Copia de MOCS en Roboflow | Material del piloto de extensibilidad y referencia de entidades | CC BY 4.0 declarada por quien publicó la copia; no se atribuye esa declaración al conjunto original no verificado. Sin redistribución. |
| Rodaje propio | Bloque guionado del banco temporal | Participación de integrantes del proyecto, sin terceros en cuadro; situaciones actuadas y tratamiento de material propio. |
| Canal @HospitalConstruction | Escenas del estrato de obra real | Licencia estándar de YouTube, no Creative Commons. Uso académico y evaluativo declarado por el proyecto, con cita y sin redistribución; localización conjunta en la lista de reproducción citada. |

***Nota.*** Las fuentes de imágenes se identifican mediante Roboflow Universe Projects (2026), Wang et al. (2021), Otgonbold et al. (2022), Gochoo (2022), SiaBar (2024) y MOCS (2024). La publicación del conjunto MOCS se atribuye a Xuehui et al. (2021). HospitalConstruction (s. f.) identifica el canal de origen; la lista *“Raw” construction videos* (s. f.) reúne los videos utilizados.

CHV requiere una salvedad expresa. Se utilizó como conjunto académico de terceros para evaluación bajo la declaración de uso libre de sus autores y con la cita correspondiente, no como un recurso con licencia abierta formal plenamente caracterizada (Wang et al., 2021). Las imágenes originales no se redistribuyeron. Esta condición limita la manera de compartir el banco y no queda resuelta por la disponibilidad de anotaciones derivadas.

Para SHEL5K se conserva la identificación de la versión del conjunto, además de la referencia al artículo que describe su ampliación y evaluación (Gochoo, 2022; Otgonbold et al., 2022). Para la copia de MOCS se distinguen el artículo original y la copia efectivamente utilizada: la declaración del publicador de Roboflow no constituye una verificación de los derechos del original (MOCS, 2024; Xuehui et al., 2021). Las consultas bibliográficas a los portales no modifican las particiones ni los archivos congelados del experimento.

Los responsables del rodaje y del material experimental fueron los autores del proyecto, Matías Lautaro Carrizo, Gabriel Agustín Guillaumet y Simon Llamosas, quienes representaron las situaciones del guion, sin terceros en cuadro. No se trató como evidencia de conducta laboral real de personas ajenas al estudio. El tratamiento documentado se sustentó en esa participación informada y en el control del material por el equipo; no se afirma la existencia de formularios firmados individuales que no se incorporaron como evidencia de esta entrega. Los datos personales y las constancias administrativas no integran el conjunto de artefactos destinado a difusión.

El material de obra real provino del canal @HospitalConstruction. El proyecto declaró un uso académico y evaluativo, con cita y sin redistribución; esa declaración no equivale a una licencia de libre reutilización ni a una conclusión jurídica sobre permisos. Los videos incorporaron procesamiento de terceros, como corrección de color, estabilización y recortes, por lo que no se equipararon con captura nativa de la cámara propia. Se verificó el uso de fragmentos a velocidad real para la evaluación temporal. El tratamiento previsto para publicar un fotograma de ese lote exige difuminar los rostros identificables.

La lista de reproducción *“Raw” construction videos* (s. f.), alojada en YouTube, reúne los videos utilizados del lote de obra real y permite acceder a sus publicaciones de origen. La fecha de consulta consignada en la referencia corresponde a la lista como conjunto, no a la fecha de acceso original de cada video.

En los modelos se registraron Apache-2.0 para Grounding DINO y MM-Grounding-DINO, y AGPL-3.0 para YOLOE. La ficha pública de Grounding-DINO tiny y las licencias de las implementaciones permiten distinguir la disponibilidad del código de la de los artefactos concretos (IDEA-Research, s. f.; OpenMMLab, s. f.; Ultralytics, s. f.). La entrega documental no redistribuye pesos. Las condiciones registradas para las variantes utilizadas no se extienden a los modelos de API cerrada de la Tabla A.1.

## Referencias

Abdalwhab, A. B. M., Imran, A., Heydarian, S., Iordanova, I., y St-Onge, D. (2025). Are open-vocabulary models ready for detection of MEP elements on construction sites? En *Proceedings of the 42nd International Symposium on Automation and Robotics in Construction* (pp. 1421–1424). International Association for Automation and Robotics in Construction. https://doi.org/10.22260/ISARC2025/0184

Advanced Micro Devices, Inc. (s. f.). *AMD Ryzen 5 8645HS*. https://www.amd.com/en/products/processors/laptop/ryzen/8000-series/amd-ryzen-5-8645hs.html

Adžemović, M. (2025). *Deep Learning-Based Multi-Object Tracking: A Comprehensive Survey from Foundations to State-of-the-Art* (arXiv:2506.13457). arXiv. https://doi.org/10.48550/arXiv.2506.13457

Agencia de Acceso a la Información Pública. (s. f.). *Conocé tus derechos respecto a tus datos personales*. Argentina.gob.ar. Recuperado el 12 de enero de 2026, de https://www.argentina.gob.ar/aaip/datospersonales/derechos

Aharon, N., Orfaig, R., y Bobrovsky, B.-Z. (2022). *BoT-SORT: Robust Associations Multi-Pedestrian Tracking* (arXiv:2206.14651). arXiv. https://doi.org/10.48550/arXiv.2206.14651

Ahmad, H. M., y Rahimi, A. (2025). SH17: A dataset for human safety and personal protective equipment detection in manufacturing industry. *Journal of Safety Science and Resilience, 6*(2), 175–185. https://doi.org/10.1016/j.jnlssr.2024.09.002

Ahmad, I., Wei, X., Sun, Y., y Zhang, Y.-Q.. (2005). Video transcoding: An overview of various techniques and research issues. *IEEE Transactions on Multimedia, 7*(5), 793–804. https://doi.org/10.1109/TMM.2005.854472

AILab-CVC. (2024, enero 30). *YOLO-World*. GitHub. Recuperado el 21 de enero de 2026, de https://github.com/AILab-CVC/YOLO-World

Amirante, A., Castaldi, T., Miniero, L., y Romano, S. P. (2014). Janus: A general purpose WebRTC gateway. *Proceedings of the Conference on Principles, Systems and Applications of IP Telecommunications*, 1–8. https://doi.org/10.1145/2670386.2670389

Amirante, A., Castaldi, T., Miniero, L., y Romano, S. P. (2015). Performance analysis of the Janus WebRTC gateway. *Proceedings of the 1st Workshop on All-Web Real-Time Systems*, 1–7. https://doi.org/10.1145/2749215.2749223

Ananthanarayanan, G., Bahl, P., Bodik, P., Chintalapudi, K., Philipose, M., Ravindranath, L., y Sinha, S. (2017). Real-Time Video Analytics: The Killer App for Edge Computing. *Computer, 50*(10), 58–67. https://doi.org/10.1109/MC.2017.3641638

Argentina. (2000). *Ley N.º 25.326: Ley de Protección de los Datos Personales*. Infoleg. https://servicios.infoleg.gob.ar/infolegInternet/anexos/60000-64999/64790/texact.htm

Argentina. (2006, septiembre 19). *Disposición 11/2006: Medidas de seguridad para el tratamiento y conservación de los datos personales*. Argentina.gob.ar. https://www.argentina.gob.ar/normativa/nacional/disposici%C3%B3n-11-2006-120120

Argentina. (2015, febrero 24). *Disposición 10/2015: Condiciones de licitud para las actividades de recolección y posterior tratamiento de imágenes digitales de personas con fines de seguridad*. Argentina.gob.ar. https://www.argentina.gob.ar/normativa/nacional/disposici%C3%B3n-10-2015-243335

Axis Communications AB. (2015). *Latency in live network video surveillance (63380/EN/R1/1504) [White paper]*. https://www.axis.com/dam/public/9d/e4/5d/latency-in-live-network-video-surveillance-en-US-190945.pdf

Bachhuber, C., Steinbach, E., Freundl, M., y Reisslein, M. (2018). On the Minimization of Glass-to-Glass and Glass-to-Algorithm Delay in Video Communication. *IEEE Transactions on Multimedia, 20*(1), 238–252. https://doi.org/10.1109/TMM.2017.2726189

Bass, L., Clements, P., y Kazman, R. (2022). *Software architecture in practice (4.ª ed.)*. Addison-Wesley.

Bernardin, K., y Stiefelhagen, R. (2008). Evaluating multiple object tracking performance: The CLEAR MOT metrics. *EURASIP Journal on Image and Video Processing, 2008*(1), 1-10. https://doi.org/10.1155/2008/246309

Bewley, A., Ge, Z., Ott, L., Ramos, F., y Upcroft, B. (2016). Simple online and realtime tracking. En *2016 IEEE International Conference on Image Processing (ICIP)* (pp. 3464-3468). IEEE. https://doi.org/10.1109/ICIP.2016.7533003

Bianchi, L., Carrara, F., Messina, N., Gennaro, C., y Falchi, F. (2024). The devil is in the fine-grained details: Evaluating open-vocabulary object detectors for fine-grained understanding. En *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition* (pp. 22520-22529). https://doi.org/10.1109/CVPR52733.2024.02125

Cao, J., Pang, J., Weng, X., Khirodkar, R., y Kitani, K. (2023). Observation-Centric SORT: Rethinking SORT for Robust Multi-Object Tracking. *2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, 9686–9696. https://doi.org/10.1109/CVPR52729.2023.00934

Card, S. K., Moran, T. P., y Newell, A. (2008). *The psychology of human-computer interaction (Reimpresión)*. Erlbaum.

Carion, N., Massa, F., Synnaeve, G., Usunier, N., Kirillov, A., y Zagoruyko, S. (2020). End-to-end object detection with transformers. En *Computer Vision – ECCV 2020*. Springer. https://www.ecva.net/papers/eccv_2020/papers_ECCV/html/832_ECCV_2020_paper.php

Centro de Computación de Alto Desempeño. (2026, 10 de abril). *Clusters disponibles*. UNC Supercómputo. https://wiki.ccad.unc.edu.ar/infra/clusters.html

Changpinyo, S., Sharma, P., Ding, N., y Soricut, R. (2021). Conceptual 12M: Pushing web-scale image-text pre-training to recognize long-tail visual concepts. En *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition* (pp. 3557–3567). https://doi.org/10.1109/CVPR46437.2021.00356

Chen, J., y Ran, X. (2019). Deep Learning With Edge Computing: A Review. *Proceedings of the IEEE, 107*(8), 1655–1674. https://doi.org/10.1109/JPROC.2019.2921977

Chen, X., y Zou, Z. (2025). *Are large pre-trained vision language models effective construction safety inspectors?* (arXiv:2508.11011). arXiv. https://doi.org/10.48550/arXiv.2508.11011

Cheng, T., Song, L., Ge, Y., Liu, W., Wang, X., y Shan, Y. (2024). YOLO-World: Real-time open-vocabulary object detection. En *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition* (pp. 16901–16911). https://doi.org/10.1109/CVPR52733.2024.01599

Choi, L., y Greer, R. (2024). *Evaluating cascaded methods of vision-language models for zero-shot detection and association of hardhats for increased construction safety* (arXiv:2410.12225). arXiv. https://doi.org/10.48550/arXiv.2410.12225

Cohen, J. (1960). A coefficient of agreement for nominal scales. *Educational and Psychological Measurement, 20*(1), 37–46. https://doi.org/10.1177/001316446002000104

Cugola, G., y Margara, A. (2012). Processing flows of information: From data stream to complex event processing. *ACM Computing Surveys, 44*(3), 1–62. https://doi.org/10.1145/2187671.2187677

DASH Industry Forum. (2020, marzo 27). *Low-latency Modes for DASH*. CR-Low-Latency-Live-r8. https://dashif.org/docs/CR-Low-Latency-Live-r8.pdf

Deber, J., Jota, R., Forlines, C., y Wigdor, D. (2015). How Much Faster is Fast Enough?: User Perception of Latency y Latency Improvements in Direct and Indirect Touch. *Proceedings of the 33rd Annual ACM Conference on Human Factors in Computing Systems*, 1827–1836. https://doi.org/10.1145/2702123.2702300

Decreto 911/1996. (1996, agosto 5). *Reglamento de higiene y seguridad para la industria de la construcción*. Infoleg. https://servicios.infoleg.gob.ar/infolegInternet/anexos/35000-39999/38568/texact.htm

Dendorfer, P., Rezatofighi, H., Milan, A., Shi, J., Cremers, D., Reid, I., Roth, S., Schindler, K., y Leal-Taixé, L. (2020). *MOT20: A benchmark for multi object tracking in crowded scenes* (arXiv:2003.09003). arXiv. https://doi.org/10.48550/arXiv.2003.09003

Du, C., Lin, C., Jin, R., Chai, B., Yao, Y., y Su, S. (2024). Exploring the State-of-the-Art in Multi-Object Tracking: A Comprehensive Survey, Evaluation, Challenges, and Future Directions. *Multimedia Tools and Applications, 83*(29), 73151–73189. https://doi.org/10.1007/s11042-023-17983-2

Du, Y., Wei, F., Zhang, Z., Shi, M., Gao, Y., y Li, G. (2022). Learning to prompt for open-vocabulary object detection with vision-language model. En *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition* (pp. 14084-14093). https://doi.org/10.1109/CVPR52688.2022.01369

European Data Protection Board. (2020, enero 30). *Guidelines 3/2019 on processing of personal data through video devices (Version 2.0)*. EDPB. https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-32019-processing-personal-data-through-video_en

Everingham, M., Van Gool, L., Williams, C. K. I., Winn, J., y Zisserman, A. (2010). The Pascal Visual Object Classes (VOC) Challenge. *International Journal of Computer Vision, 88*(2), 303–338. https://doi.org/10.1007/s11263-009-0275-4

Fu, S., Yang, Q., Mo, Q., Yan, J., Wei, X., Meng, J., Xie, X., y Zheng, W.-S. (2025). LLMDet: Learning strong open-vocabulary object detectors under the supervision of large language models. En *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition* (pp. 14987–14997). https://openaccess.thecvf.com/content/CVPR2025/html/Fu_LLMDet_Learning_Strong_Open-Vocabulary_Object_Detectors_under_the_Supervision_of_CVPR_2025_paper.html

Gettys, J., y Nichols, K. (2012). Bufferbloat: Dark buffers in the internet. *Communications of the ACM, 55*(1), 57–65. https://doi.org/10.1145/2063176.2063196

Gochoo, M. (2022). *Safety helmet detection with extended labels 5K images (SHEL5K)* (Versión 4) [Conjunto de datos]. Mendeley Data. https://doi.org/10.17632/9rcv8mm682.4

Google. (2022, mayo). *owlvit-large-patch14*. Hugging Face. https://huggingface.co/google/owlvit-large-patch14

Google. (2023, junio). *owlv2-base-patch16-ensemble*. Hugging Face. https://huggingface.co/google/owlv2-base-patch16-ensemble

Gu, X., Lin, T.-Y., Kuo, W., y Cui, Y. (2021). Open-vocabulary object detection via vision and language knowledge distillation (arXiv:2104.13921). arXiv. https://doi.org/10.48550/arXiv.2104.13921

Gupta, A., Dollár, P., y Girshick, R. (2019). LVIS: A dataset for large vocabulary instance segmentation. En *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition* (pp. 5356–5364). https://openaccess.thecvf.com/content/CVPR_2019/html/Gupta_LVIS_A_Dataset_for_Large_Vocabulary_Instance_Segmentation_CVPR_2019_paper.html

HospitalConstruction. (s. f.). *HospitalConstruction* [Canal de YouTube]. YouTube. Recuperado el 8 de septiembre de 2026, de https://www.youtube.com/@HospitalConstruction

HP Inc. (s. f.). *Victus Gaming Laptop 15-fb2024la (A14LSLA): Todas las especificaciones técnicas*. https://www.hp.com/py-es/products/laptops/product-details/product-specifications/2102249493

IDEA-Research. (2024a, noviembre 20). *DINO-X-API: A unified vision model for open-world object detection and understanding [Repositorio de código]*. GitHub. https://github.com/IDEA-Research/DINO-X-API

IDEA-Research. (2024b, agosto 1). *IDEA-Research/Grounded-SAM-2: Grounded SAM 2: Ground and Track Anything in Videos*. GitHub. Recuperado el 21 de enero de 2026, de https://github.com/IDEA-Research/Grounded-SAM-2

IDEA-Research. (2024c, mayo 18). *GroundingDINO: Official implementation of “Grounding DINO: Marrying DINO with grounded pre-training for open-set object detection” [Repositorio de código]*. GitHub. https://github.com/IDEA-Research/GroundingDINO

IDEA-Research. (s. f.). *Grounding-DINO tiny* [Ficha de modelo]. Hugging Face. Recuperado el 8 de septiembre de 2026, de https://huggingface.co/IDEA-Research/grounding-dino-tiny/blob/main/README.md

Iorga, M., Feldman, L., Barton, R., Martin, M. J., Goren, N., y Mahmoudi, C. (2018). *Fog computing conceptual model (NIST SP 500-325; p*. NIST SP 500-325). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.500-325

ISO. (2018). *ISO 45001:2018 Occupational health and safety management systems—Requirements with guidance for use*. ISO. https://www.iso.org/standard/63787.html

ISO. (2023). *ISO/IEC 42001:2023—Artificial intelligence management system*. ISO. https://www.iso.org/standard/42001

ISO/IEC. (2022). *Information technology—Dynamic adaptive streaming over HTTP (DASH)—Part 1: Media presentation description and segment formats*. ISO/IEC 23009-1:2022. https://www.iso.org/standard/83314.html

Jiang, K., Huang, J., Xie, W., Lei, J., Li, Y., Shao, L., y Lu, S. (2024). *Domain adaptation for large-vocabulary object detectors*. In Advances in Neural Information Processing Systems, 37 (pp. 75422–75453). https://doi.org/10.52202/079017-2401

Jiang, Q., Li, F., Zeng, Z., Ren, T., Liu, S., y Zhang, L. (2024). *T-Rex2: Towards Generic Object Detection via Text-Visual Prompt Synergy* (arXiv:2403.14610). arXiv. https://doi.org/10.48550/arXiv.2403.14610

Keranen, A., Holmberg, C., y Rosenberg, J. (2018). *Interactive Connectivity Establishment (ICE): A Protocol for Network Address Translator (NAT) Traversal (RFC 8445)*. RFC Editor. https://doi.org/10.17487/RFC8445

Khattak, M. U., Rasheed, H., Maaz, M., Khan, S., y Khan, F. S. (2023). MaPLe: Multi-modal prompt learning. En *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition* (pp. 19113–19122). https://openaccess.thecvf.com/content/CVPR2023/html/Khattak_MaPLe_Multi-Modal_Prompt_Learning_CVPR_2023_paper.html

Kirkpatrick, J., Pascanu, R., Rabinowitz, N., Veness, J., Desjardins, G., Rusu, A. A., Milan, K., Quan, J., Ramalho, T., Grabska-Barwinska, A., Hassabis, D., Clopath, C., Kumaran, D., y Hadsell, R. (2017). Overcoming catastrophic forgetting in neural networks. *Proceedings of the National Academy of Sciences, 114*(13), 3521-3526. https://doi.org/10.1073/pnas.1611835114

Kreutz, D., Ramos, F. M. V., Esteves Verissimo, P., Esteve Rothenberg, C., Azodolmolky, S., y Uhlig, S. (2015). Software-Defined Networking: A Comprehensive Survey. *Proceedings of the IEEE, 103*(1), 14–76. https://doi.org/10.1109/JPROC.2014.2371999

Kumar, A., Raghunathan, A., Jones, R. M., Ma, T., y Liang, P. (2022). Fine-tuning can distort pretrained features and underperform out-of-distribution. *International Conference on Learning Representations*. https://iclr.cc/virtual/2022/oral/5946

Kurose, J. F., y Ross, K. W. (2021). *Computer networking: A top-down approach (Eighth edition)*. Pearson.

Lee, Y., Chen, A. S., Tajwar, F., Kumar, A., Yao, H., Liang, P., y Finn, C. (2023). Surgical fine-tuning improves adaptation to distribution shifts. *International Conference on Learning Representations*. https://iclr.cc/virtual/2023/poster/12230

Ley 19.587. (1972). *Higiene y seguridad en el trabajo*. Infoleg. https://servicios.infoleg.gob.ar/infolegInternet/anexos/15000-19999/17612/norma.htm

Li, L. H., Zhang, P., Zhang, H., Yang, J., Li, C., Zhong, Y., Wang, L., Yuan, L., Zhang, L., Hwang, J.-N., Chang, K.-W., y Gao, J. (2021). Grounded language-image pre-training (arXiv:2112.03857). arXiv. https://doi.org/10.48550/arXiv.2112.03857

Li, S., Danelljan, M., Ding, H., Huang, T. E., y Yu, F. (2022). Tracking every thing in the wild. En *Computer Vision – ECCV 2022*. Springer. https://doi.org/10.1007/978-3-031-20047-2_29

Li, S., Fischer, T., Ke, L., Ding, H., Danelljan, M., y Yu, F. (2023). OVTrack: Open-Vocabulary Multiple Object Tracking. *2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, 5567–5577. https://doi.org/10.1109/CVPR52729.2023.00539

Li, S., Ren, H., Xie, X., y Cao, Y. (2025). A Review of Multi‐Object Tracking in Recent Times. IET Computer Vision, 19(1), e70010. https://doi.org/10.1049/cvi2.70010

Li, X., Cho, B., y Xiao, Y. (2022). Balancing Latency and Accuracy on Deep Video Analytics at the Edge. *2022 IEEE 19th Annual Consumer Communications y Networking Conference (CCNC)*, 299–306. https://doi.org/10.1109/CCNC49033.2022.9700636

Liang, H., y Han, R. (2024). OVT-B: A new large-scale benchmark for open-vocabulary multi-object tracking. En *Advances in Neural Information Processing Systems* (Vol. 37). https://proceedings.neurips.cc/paper_files/paper/2024/hash/1adeeac24ce6168e20bcee85645720e9-Abstract-Datasets_and_Benchmarks_Track.html

Lin, T.-Y., Maire, M., Belongie, S., Hays, J., Perona, P., Ramanan, D., Dollar, P. y Zitnick, C. L. (2014). *Microsoft COCO: Common objects in context*. En D. Fleet, T. Pajdla, B. Schiele y T. Tuytelaars (Eds.), Computer Vision - ECCV 2014 (Vol. 8693, pp. 740-755). Springer. https://doi.org/10.1007/978-3-319-10602-1_48

Liu, S., Zeng, Z., Ren, T., Li, F., Zhang, H., Yang, J., Jiang, Q., Li, C., Yang, J., Su, H., Zhu, J., y Zhang, L. (2024). *Grounding DINO: Marrying DINO with grounded pre-training for open-set object detection*. In Computer Vision - ECCV 2024 (pp. 38-55). Springer. https://doi.org/10.1007/978-3-031-72970-6_3

Luiten, J., Os̆ep, A., Dendorfer, P., Torr, P., Geiger, A., Leal-Taixé, L., y Leibe, B. (2021). HOTA: A Higher Order Metric for Evaluating Multi-object Tracking. *International Journal of Computer Vision, 129*(2), 548–578. https://doi.org/10.1007/s11263-020-01375-2

Luo, W., Xing, J., Milan, A., Zhang, X., Liu, W., y Kim, T.-K. (2021). Multiple object tracking: A literature review. *Artificial Intelligence, 293*, 103448. https://doi.org/10.1016/j.artint.2020.103448

Luxonis. (s. f.). *OAK-D Pro PoE [Documentación de hardware]*. Luxonis Docs. https://docs.luxonis.com/hardware/products/OAK-D%20Pro%20PoE

May, W. (2017). HTTP live streaming (R. Pantos, Ed.; RFC 8216). RFC Editor. https://doi.org/10.17487/RFC8216

Microsoft. (2024, junio). *Florence-2-large*. Hugging Face. https://huggingface.co/microsoft/Florence-2-large

Milan, A., Leal-Taixe, L., Reid, I., Roth, S., y Schindler, K. (2016). *MOT16: A Benchmark for Multi-Object Tracking* (arXiv:1603.00831). arXiv. https://doi.org/10.48550/arXiv.1603.00831

Minderer, M., Gritsenko, A., Stone, A., Neumann, M., Weissenborn, D., Dosovitskiy, A., Mahendran, A., Arnab, A., Dehghani, M., Shen, Z., Wang, X., Zhai, X., Kipf, T., y Houlsby, N. (2022). *Simple open-vocabulary object detection with vision transformers*. In Computer Vision – ECCV 2022 (pp. 728–755). Springer. https://doi.org/10.1007/978-3-031-20080-9_42

Minderer, M., Gritsenko, A., y Houlsby, N. (2023). Scaling open-vocabulary object detection. En *Advances in Neural Information Processing Systems* (Vol. 36). https://proceedings.neurips.cc/paper_files/paper/2023/hash/e6d58fc68c0f3c36ae6e0e64478a69c0-Abstract-Conference.html

MOCS. (2024). *MOCS* [Conjunto de datos]. Roboflow Universe. https://universe.roboflow.com/mocs/mocs-bowib

NVIDIA Corporation. (s. f.-b). NVIDIA Video Codec SDK. https://developer.nvidia.com/video-codec-sdk

NVIDIA. (2022, marzo). *NVIDIA A30 data sheet*. https://www.nvidia.com/content/dam/en-zz/Solutions/data-center/products/a30-gpu/pdf/a30-datasheet.pdf

NVIDIA. (2024). *DeepStream SDK 8.0 for NVIDIA dGPU/X86 and Jetson—DeepStream documentation*. https://docs.nvidia.com/metropolis/deepstream/dev-guide/text/DS_Release_notes.html

NVIDIA. (2026a). *DeepStream on WSL*. https://docs.nvidia.com/metropolis/deepstream/dev-guide/text/DS_on_WSL2.html

NVIDIA. (2026b). *Installing TensorRT*. https://docs.nvidia.com/deeplearning/tensorrt/latest/installing-tensorrt/installing.html

NVIDIA. (s. f.-a). *Compare GeForce RTX laptops*. https://www.nvidia.com/en-us/geforce/laptops/compare/

NVIDIA. (s. f.-g). Grounding DINO. NVIDIA TAO Toolkit Documentation. Recuperado el 27 de agosto de 2026, de https://docs.nvidia.com/tao/tao-toolkit/latest/text/cv_finetuning/pytorch/object_detection/grounding_dino.html

NVIDIA. (s. f.-h). NVIDIA Triton Inference Server. Recuperado el 27 de agosto de 2026, de https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/index.html

OASIS. (2019). *MQTT Version 5.0*. OASIS Standard. https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html

ONNX Runtime. (s. f.). *CUDA Execution Provider*. https://onnxruntime.ai/docs/execution-providers/CUDA-ExecutionProvider.html

ONVIF. (2019). *ONVIF Profile S Specification (ONVIF Profile S)*. ONVIF. https://www.onvif.org/wp-content/uploads/2019/12/ONVIF_Profile_-S_Specification_v1-3.pdf

OpenMMLab. (s. f.). *MMDetection: License* [Licencia de software]. GitHub. Recuperado el 8 de septiembre de 2026, de https://github.com/open-mmlab/mmdetection/blob/main/LICENSE

Organisation for Economic Co-operation and Development. (2019, mayo 1). *OECD AI Principles overview*. OECD. https://oecd.ai/en/ai-principles

Otgonbold, M.-E., Gochoo, M., Alnajjar, F. S., Ali, L., Tan, T.-H., Hsieh, J.-W., y Chen, P.-Y. (2022). SHEL5K: An extended dataset and benchmarking for safety helmet detection. *Sensors, 22*(6), 2315. https://doi.org/10.3390/s22062315

Pantos, R. (2025). *HTTP Live Streaming 2nd Edition (Internet-Draft)*. Internet Engineering Task Force. https://datatracker.ietf.org/doc/draft-pantos-hls-rfc8216bis/18/

Parmar, H., y Thornburgh, M. (2012). *Adobe’s Real Time Messaging Protocol*. Adobe. https://ptacts.uspto.gov/ptacts/public-informations/petitions/1557060/download-documents?artifactId=CX29dwexemvGTAgu1npsGb4QtKzyjACHSNYXLhjJp5m1SpQS4AAf-3A

Radford, A., Kim, J. W., Hallacy, C., Ramesh, A., Goh, G., Agarwal, S., Sastry, G., Askell, A., Mishkin, P., Clark, J., Krueger, G., y Sutskever, I. (2021). Learning transferable visual models from natural language supervision. En *Proceedings of the 38th International Conference on Machine Learning* (Vol. 139, pp. 8748–8763). PMLR. https://proceedings.mlr.press/v139/radford21a.html

Rasaee, H., Koleilat, T., y Rivaz, H. (2025). Grounding DINO-US-SAM: Text-Prompted Multi-Organ Segmentation in Ultrasound with LoRA-Tuned Vision-Language Models. *IEEE Transactions on Ultrasonics, Ferroelectrics, and Frequency Control, 72*(10), 1414-1425. https://doi.org/10.1109/TUFFC.2025.3605285

*“Raw” construction videos* [Lista de reproducción]. (s. f.). YouTube. Recuperado el 15 de septiembre de 2026, de https://www.youtube.com/playlist?list=PLVG3-xIaXtKzAC9JJnZJUY4aBCg0BNPKV

Ren, T., Chen, Y., Jiang, Q., Zeng, Z., Xiong, Y., Liu, W., Ma, Z., Shen, J., Gao, Y., Jiang, X., Chen, X., Song, Z., Zhang, Y., Huang, H., Gao, H., Liu, S., Zhang, H., Li, F., Yu, K., y Zhang, L. (2024). *DINO-X: A unified vision model for open-world object detection and understanding* (arXiv:2411.14347). arXiv. https://doi.org/10.48550/arXiv.2411.14347

Ren, T., Jiang, Q., Liu, S., Zeng, Z., Liu, W., Gao, H., Huang, H., Ma, Z., Jiang, X., Chen, Y., Xiong, Y., Zhang, H., Li, F., Tang, P., Yu, K., y Zhang, L. (2024). *Grounding DINO 1.5: Advance the “Edge” of Open-Set Object Detection (Versión 2). arXiv*. https://doi.org/10.48550/ARXIV.2405.10300

Ren, T., Liu, S., Zeng, A., Lin, J., Li, K., Cao, H., Chen, J., Huang, X., Chen, Y., Yan, F., Zeng, Z., Zhang, H., Li, F., Yang, J., Li, H., Jiang, Q., y Zhang, L. (2024). *Grounded SAM: Assembling Open-World Models for Diverse Visual Tasks* (arXiv:2401.14159). arXiv. https://doi.org/10.48550/arXiv.2401.14159

Ristani, E., Solera, F., Zou, R., Cucchiara, R., y Tomasi, C. (2016). *Performance Measures and a Data Set for Multi-target, Multi-camera Tracking*. En G. Hua y H. Jégou (Eds.), Computer Vision – ECCV 2016 Workshops (Vol. 9914, pp. 17–35). Springer International Publishing. https://doi.org/10.1007/978-3-319-48881-3_2

Roboflow Universe Projects. (2026). *Construction site safety* [Conjunto de datos]. Roboflow Universe. https://universe.roboflow.com/roboflow-universe-projects/construction-site-safety

Roy (Whalen), S. (2024, julio 18). RTMP vs. RTSP: Which protocol should you choose? (Update). Wowza Media Systems. https://www.wowza.com/blog/rtmp-vs-rtsp-which-protocol-should-you-choose

Satyanarayanan, M. (2017). The Emergence of Edge Computing. *Computer, 50*(1), 30–39. https://doi.org/10.1109/MC.2017.9

Schulzrinne, H., Casner, S., Frederick, R., y Jacobson, V. (2003). *RTP: A Transport Protocol for Real-Time Applications (RFC 3550)*. RFC Editor. https://doi.org/10.17487/rfc3550

Schulzrinne, H., Rao, A., Lanphier, R., y Westerlund, M. (2016). *Real-Time Streaming Protocol Version 2.0 (M*. Stiemerling, Ed.; RFC 7826). RFC Editor. https://doi.org/10.17487/RFC7826

Schulzrinne, H., Rao, A., y Lanphier, R. (1998). *Real Time Streaming Protocol (RTSP) (RFC 2326)*. RFC Editor. https://doi.org/10.17487/rfc2326

Sharabayko, M. P., Sharabayko, M. A., Dube, J., Kim, J., y Kim, J. (2024). *The SRT Protocol (Internet-Draft (working copy))*. Internet Engineering Task Force. https://haivision.github.io/srt-rfc/draft-sharabayko-srt.html

Sharma, P., Ding, N., Goodman, S., y Soricut, R. (2018). Conceptual captions: A cleaned, hypernymed, image alt-text dataset for automatic image captioning. En *Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics* (pp. 2556–2565). https://doi.org/10.18653/v1/P18-1238

Shen, Y., Fu, C., Chen, P., Zhang, M., Li, K., Sun, X., Wu, Y., Lin, S., y Ji, R. (2023). Aligning and prompting everything all at once for universal visual perception (arXiv:2312.02153). arXiv. https://doi.org/10.48550/arXiv.2312.02153

Shi, W., Cao, J., Zhang, Q., Li, Y., y Xu, L. (2016). Edge Computing: Vision and Challenges. *IEEE Internet of Things Journal, 3*(5), 637–646. https://doi.org/10.1109/JIOT.2016.2579198

SiaBar. (2024). *PPE dataset for workplace safety* [Conjunto de datos]. Roboflow Universe. https://universe.roboflow.com/siabar/ppe-dataset-for-workplace-safety

Sonono, T. (2019). *Interoperable Retransmission Protocols with Low Latency and Constrained Delay: A Performance Evaluation of RIST and SRT [Tesis de maestría, KTH Royal Institute of Technology]*. https://www.diva-portal.org/smash/get/diva2:1335907/FULLTEXT01.pdf

Thrush, T., Jiang, R., Bartolo, M., Singh, A., Williams, A., Kiela, D., y Ross, C. (2022). Winoground: Probing vision and language models for visio-linguistic compositionality. En *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition* (pp. 5238–5248). https://openaccess.thecvf.com/content/CVPR2022/html/Thrush_Winoground_Probing_Vision_and_Language_Models_for_Visio-Linguistic_Compositionality_CVPR_2022_paper.html

THU-MIG. (2025). *THU-MIG / yoloe: YOLOE: Real-Time Seeing Anything*. GitHub. https://github.com/THU-MIG/yoloe

Ucar, A., Ro, S., Satwika, S., Gayathri, P. Y., y Balsha, M. G. (2025). *Fine-Tuning Florence2 for Enhanced Object Detection in Un-constructed Environments: Vision-Language Model Approach* (arXiv:2503.04918). arXiv. https://doi.org/10.48550/arXiv.2503.04918

Ultralytics. (2026). *Ultralytics YOLO26*. https://docs.ultralytics.com/models/yolo26/

Ultralytics. (s. f.). *Ultralytics: License* [Licencia de software]. GitHub. Recuperado el 8 de septiembre de 2026, de https://github.com/ultralytics/ultralytics/blob/main/LICENSE

UNESCO. (2021). *Recommendation on the ethics of artificial intelligence*. https://unesdoc.unesco.org/ark:/48223/pf0000380455

Video Services Forum. (2020). *Reliable Internet Stream Transport (RIST) protocol specification – Simple profile*. Video Services Forum. https://static.vsf.tv/download/technical_recommendations/VSF_TR-06-1_2020_06_25.pdf

Video Services Forum. (2024). *Reliable Internet Stream Transport (RIST) Protocol Specification – Main Profile*. Video Services Forum. https://static.vsf.tv/download/technical_recommendations/VSF_TR-06-2_2024_06_12.pdf

Wang, A., Liu, L., Chen, H., Lin, Z., Han, J., y Ding, G. (2025). YOLOE: Real-time seeing anything. En *Proceedings of the IEEE/CVF International Conference on Computer Vision* (pp. 24591–24602). https://openaccess.thecvf.com/content/ICCV2025/html/Wang_YOLOE_Real-Time_Seeing_Anything_ICCV_2025_paper.html

Wang, H., Ren, P., Jie, Z., Dong, X., Feng, C., Qian, Y., Ma, L., Jiang, D., Wang, Y., Lan, X., y Liang, X. (2024). *OV-DINO: Unified open-vocabulary detection with language-aware selective fusion* (arXiv:2407.07844). arXiv. https://doi.org/10.48550/arXiv.2407.07844

Wang, H., Zhang, X., Chen, H., Xu, Y., y Ma, Z. (2022). Inferring End-to-End Latency in Live Videos. *IEEE Transactions on Broadcasting, 68*(2), 517–529. https://doi.org/10.1109/TBC.2021.3071060

Wang, Z., Wu, Y., Yang, L., Thirunavukarasu, A., Evison, C., y Zhao, Y. (2021). Fast personal protective equipment detection for real construction sites using deep learning approaches. *Sensors, 21*(10), 3478. https://doi.org/10.3390/s21103478

Wojke, N., Bewley, A., y Paulus, D. (2017). Simple online and realtime tracking with a deep association metric. *2017 IEEE International Conference on Image Processing (ICIP)*, 3645–3649. https://doi.org/10.1109/ICIP.2017.8296962

World Wide Web Consortium. (2025). *WebRTC: Real-Time Communication in Browsers (W3C Recommendation)*. World Wide Web Consortium. https://www.w3.org/TR/webrtc/

Xiao, B., Wu, H., Xu, W., Dai, X., Hu, H., Lu, Y., Zeng, M., Liu, C., y Yuan, L. (2024). Florence-2: Advancing a unified representation for a variety of vision tasks. En *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition* (pp. 4818–4829). https://doi.org/10.1109/CVPR52733.2024.00461

Xuehui, A., Li, Z., Zuguang, L., Chengzhi, W., Pengfei, L., y Zhiwei, L. (2021). Dataset and benchmark for detecting moving objects in construction sites. *Automation in Construction, 122*, 103482. https://doi.org/10.1016/j.autcon.2020.103482

Yao, L., Han, J., Wen, Y., Liang, X., Xu, D., Zhang, W., Li, Z., Xu, C., y Xu, H. (2022). DetCLIP: Dictionary-enriched visual-concept paralleled pre-training for open-world detection. En *Advances in Neural Information Processing Systems* (Vol. 35). https://proceedings.neurips.cc/paper_files/paper/2022/hash/3ba960559212691be13fa81d9e5e0047-Abstract-Conference.html

Yao, L., Pi, R., Han, J., Liang, X., Xu, H., Zhang, W., Li, Z., y Xu, D. (2024). DetCLIPv3: Towards versatile generative open-vocabulary object detection. En *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition* (pp. 27391–27401). https://openaccess.thecvf.com/content/CVPR2024/html/Yao_DetCLIPv3_Towards_Versatile_Generative_Open-vocabulary_Object_Detection_CVPR_2024_paper.html

Yao, Y., Liu, P., Zhao, T., Zhang, Q., Liao, J., Fang, C., Lee, K., y Wang, Q. (2024). How to evaluate the generalization of detection? A benchmark for comprehensive open-vocabulary detection. *Proceedings of the AAAI Conference on Artificial Intelligence, 38*(7), 6630-6638. https://doi.org/10.1609/aaai.v38i7.28485

Yousefpour, A., Fung, C., Nguyen, T., Kadiyala, K., Jalali, F., Niakanlahiji, A., Kong, J., y Jue, J. P. (2019). All one needs to know about fog computing and related edge computing paradigms: A complete survey. *Journal of Systems Architecture, 98*, 289–330. https://doi.org/10.1016/j.sysarc.2019.02.009

Yuksekgonul, M., Bianchi, F., Kalluri, P., Jurafsky, D., y Zou, J. (2023). *When and why vision-language models behave like bags-of-words, and what to do about it? International Conference on Learning Representations*. https://arxiv.org/abs/2210.01936

Zang, Y., Li, W., Zhou, K., Huang, C., y Loy, C. C. (2022). Open-vocabulary DETR with conditional matching. En *Computer Vision – ECCV 2022*. Springer. https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/1248_ECCV_2022_paper.php

Zareian, A., Rosa, K. D., Hu, D. H., y Chang, S.-F. (2021). Open-vocabulary object detection using captions. En *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition* (pp. 14393–14402). https://openaccess.thecvf.com/content/CVPR2021/html/Zareian_Open-Vocabulary_Object_Detection_Using_Captions_CVPR_2021_paper.html

Zhang, H., Zhang, P., Hu, X., Chen, Y.-C., Li, L. H., Dai, X., Wang, L., Yuan, L., Hwang, J.-N., y Gao, J. (2022). GLIPv2: Unifying localization and vision-language understanding. En *Advances in Neural Information Processing Systems* (Vol. 35). https://proceedings.neurips.cc/paper_files/paper/2022/hash/ea370419760b421ce12e3082eb2ae1a8-Abstract-Conference.html

Zhang, Y., Sun, P., Jiang, Y., Yu, D., Weng, F., Yuan, Z., Luo, P., Liu, W., y Wang, X. (2022). *ByteTrack: Multi-object Tracking by Associating Every Detection Box*. En S. Avidan, G. Brostow, M. Cissé, G. M. Farinella, y T. Hassner (Eds.), Computer Vision – ECCV 2022 (Vol. 13682, pp. 1–21). Springer Nature Switzerland. https://doi.org/10.1007/978-3-031-20047-2_1

Zhao, T., Liu, P., He, X., Zhang, L., y Lee, K. (2024). *Real-time Transformer-based Open-Vocabulary Detection with Efficient Fusion Head* (arXiv:2403.06892). arXiv. https://doi.org/10.48550/arXiv.2403.06892

Zhao, X., Chen, Y., Xu, S., Li, X., Wang, X., Li, Y., y Huang, H. (2024). *An Open and Comprehensive Pipeline for Unified Object Grounding and Detection* (arXiv:2401.02361). arXiv. https://doi.org/10.48550/arXiv.2401.02361

Zhou, K., Yang, J., Loy, C. C., y Liu, Z. (2022a). Conditional Prompt Learning for Vision-Language Models. *IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2022)*. https://www.computer.org/csdl/proceedings-article/cvpr/2022/694600q6795/1H0OnmbArsY

Zhou, K., Yang, J., Loy, C. C., y Liu, Z. (2022b). Learning to Prompt for Vision-Language Models. *International Journal of Computer Vision, 130*(9), 2337–2348. https://doi.org/10.1007/s11263-022-01653-1

Zhou, X., Girdhar, R., Joulin, A., Krähenbühl, P., y Misra, I. (2022). Detecting twenty-thousand classes using image-level supervision. En *Computer Vision – ECCV 2022*. Springer. https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/2557_ECCV_2022_paper.php

Zou, X., Dou, Z.-Y., Yang, J., Gan, Z., Li, L., Li, C., Dai, X., Behl, H., Wang, J., Yuan, L., Peng, N., Wang, L., Lee, Y. J., y Gao, J. (2023). Generalized decoding for pixel, image, and language. En *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition* (pp. 15116–15127). https://openaccess.thecvf.com/content/CVPR2023/html/Zou_Generalized_Decoding_for_Pixel_Image_and_Language_CVPR_2023_paper.html

Zou, Z., Chen, K., Shi, Z., Guo, Y., y Ye, J. (2023). Object Detection in 20 Years: A Survey. *Proceedings of the IEEE, 111*(3), 257–276. https://doi.org/10.1109/JPROC.2023.3238524
