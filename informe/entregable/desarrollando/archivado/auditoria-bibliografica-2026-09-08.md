# Auditoría bibliográfica del informe — 2026-09-08

> **Qué es.** Revisión de las citas y del listado de referencias del TFG. El listado global se
> tomó del maestro `desarrollando/E-OVRT-VDP_v1.1_05062026-sin-indice.docx` (export del 09-08);
> las citas válidas, de los cinco documentos de sección cerrados. Responde a seis preguntas: si la
> referencia está bien usada, si quedó huérfana, si está bien citada y sin riesgo de plagio, si es
> pertinente para un TFG, si conviene darla de baja, y qué más mirar antes de entregar.
>
> **Método, en dos capas.** Una **mecánica y reproducible**: se parsearon las 242 entradas y se
> extrajeron las citas de las diez piezas vigentes, y se cruzaron; todo número de este documento
> sale de ese cruce. Una **de lectura**: cinco auditorías en paralelo sobre el uso de cada cita en
> su contexto. **Cada hallazgo de la segunda capa se re-verificó contra el texto antes de entrar
> acá.** Los que no se pudieron confirmar no figuran.
>
> **Qué NO es.** No es un pase: no toca ningún `.docx`. Es el insumo para decidir qué corregir.

---

## 1. Veredicto en cinco líneas

El criterio bibliográfico del trabajo es maduro y en varios tramos ejemplar. No hay fraude, ni
apropiación, ni una sola transcripción literal sin atribuir. Lo que hay son tres cosas que un
jurado ve antes que el mérito. **La cadena entre la cita y la referencia está rota en trece
puntos**, y la causa es que el listado del maestro nunca se sincronizó con las correcciones de la
Etapa 1. **§17.5 reporta resultados sin invocar ninguna de las varas que §15 ya tiene relevadas.**
Y **§11–§14 no tiene una sola referencia**, incluida la premisa que justifica todo el trabajo.

Ninguno exige investigación nueva. Son fusiones, remisiones y citas puntuales, más una tanda de
higiene de formato. Sin esa pasada, el flanco más fácil de atacar es 15.2.5.4, porque es la
subsección que fundamenta por qué el trabajo existe y apoya sus cuatro cifras clave en una
referencia que el lector no puede encontrar.

---

## 2. Qué se comparó, y cuánto se cita

El listado global tiene **242 entradas**. Las citas se tomaron de las piezas que hoy son el
informe, no del cuerpo viejo del maestro, cuyas §15, §16, §17.1 y §17.3 quedaron superadas.

| Pieza | Palabras | Citas | Densidad |
|---|---:|---:|---|
| §11–§14 Glosario, Introducción, Objetivos y Plan (maestro) | 4.523 | **0** | — |
| §15 + §16 Estado del arte y Marco teórico (v1.4) | 18.670 | 169 | 1 cada 110 palabras |
| §17.1 Consolidación metodológica + Anexos C y D (v1.21) | 16.950 | 26 | 1 cada 651 |
| §17.3 Diseño arquitectónico (v1.12) | 14.128 | **0** | — |
| §17.4 Implementación (v1.15) | 7.483 | 1 | 1 cada 7.483 |
| §17.5 Evaluación y validación | 4.833 | **0** | — |
| Anexo A, matrices comparativas (90e) | 3.980 | 161 | 1 cada 24 |
| Anexo B, infraestructura (maestro) | 1.801 | 9 | 1 cada 200 |

Que §17.3 y §17.4 casi no citen **no es un defecto**: describen diseño y construcción propios. Que
§17.5 y §11–§14 no citen sí lo es, por razones distintas, y se tratan en los puntos 5 y 6.

---

## 3. Lo más grave, y su causa: el listado del maestro quedó viejo

Trece citas no resuelven contra el listado. Un lector busca la referencia y no la encuentra: en la
práctica es indistinguible de una cita inventada, y es lo primero que prueba un jurado.

**Pero la causa no es que falte investigar.** El listado corregido de la Etapa 1, que vive en
`90e-etapa1-anexo-a-y-referencias.md`, tiene **102 entradas**, y **doce de ellas no están en las
242 del maestro**. Verificado una por una:

> Chen y Zou (2025) · Choi y Greer (2024) · Kumar et al. (2022) · Lee et al. (2023) ·
> NVIDIA (s. f.-g), TAO Toolkit · NVIDIA (s. f.-h), Triton · OASIS (2019), MQTT 5.0 ·
> Thrush et al. (2022), Winoground · Ultralytics (2026), YOLO26 · UNESCO (2021) ·
> Yuksekgonul et al. (2023), ARO · Zhou et al. (2022), Detic

Es decir: **el listado global del maestro es anterior a las correcciones de la Etapa 1 y nunca se
sincronizó.** Diez de las once citas irresolubles se arreglan **fusionando `90e` en el listado del
maestro**, no buscando fuentes nuevas. Es la corrección más barata y más importante de toda esta
auditoría, y explica por qué las citas que faltan son justo las mejores: son las que la Etapa 1
agregó al corregirse.

**Las que quedan sin entrada aun después de fusionar** son dos, y sí requieren alta nueva:
**Liang y Han (2024)**, declarada «referencia primaria» de OVT-B en §17.1.6.4, y **Liu et al.
(2023)** del Anexo B, que además parece un error de año por Liu et al. (2024).

**El detalle de las citas irresolubles, con lo que sostiene cada una:**

| Cita | Dónde | Qué sostiene |
|---|---|---|
| **Choi y Greer (2024)** | §15.2.5.4 y Tabla 5 | las cuatro cifras del único antecedente OVD × EPP publicado |
| **Chen y Zou (2025)** | §15.2.5.4 | IoU bajo 20 % en objetivos con restricción de atributo |
| **Yuksekgonul et al. (2023)** | §16.3.4 | ARO, 50.000 casos |
| **Thrush et al. (2022)** | §16.3.4 | Winoground, desempeño no mejor que el azar |
| **Kumar et al. (2022)** | §15.2.4 | degradación fuera de distribución al ajustar |
| **Lee et al. (2023)** | §15.2.4 | ajuste selectivo de capas |
| **Ultralytics (2026)** | §15.2.1.2 | la advertencia que separa YOLOE-v8 de YOLOE-26 |
| **NVIDIA (s. f.-g) y (s. f.-h)** | §15.4.3.2 | TAO Toolkit y Triton; la serie del listado llega a `-f` |
| **OASIS (2019)** | §15.4.2 y §16.5.3 | MQTT, idempotencia y reentregas |
| **Liang y Han (2024)** | §17.1.6.4 | OVT-B, declarada «referencia primaria» |
| **Liu et al. (2023)** | Anexo B | ajuste fino y partición disjunta |

Las dos primeras y las dos de composicionalidad son las que más pesan: **Choi y Greer sostiene la
brecha que justifica el trabajo**, y Yuksekgonul y Thrush sostienen todo el argumento por el cual
CR-01 se formula por ausencia. Las cuatro están en `90e` y ninguna en el maestro.

El mismo desfase golpea a los anexos, y ahí rompe la cadena de verificación: la nota de la Tabla
A.1 cita a «X. Zhou et al. (2022)» para la fila de Detic, y esa entrada existe en `90e` pero no en
el maestro, de modo que **las cifras de Detic quedan sin fuente verificable en el documento
entregado**. La nota de la Tabla B.5 cita «Liu et al. (2023)», que no existe en ningún lado, y la
de la Tabla B.2 cita «Luxonis, s. f.-a», que tampoco.

**Con entrada, pero el año o el sufijo no coinciden.** Se corrige en un lado o en el otro:

| Cita | El listado tiene |
|---|---|
| Minderer et al. (2023), 4 apariciones | 2022 y **2024** para el mismo paper de OWLv2 |
| Axis Communications AB (s. f.), en §17.1.7.5 | 2015 |
| Luxonis (s. f.-a) | sólo `s. f.-b`, que además queda como «-b» sin «-a» |
| IDEA-Research (2024a) y (2024c) | tres entradas de 2024 **sin sufijo** |
| Zhou et al. (2022), en §17.1 | 2022a y 2022b |

Verificadas y **descartadas como falsas alarmas**: Agencia de Acceso a la Información Pública,
Advanced Micro Devices, DASH Industry Forum, ISO/IEC, UNESCO y NVIDIA Corporation resolvieron bien
contra el listado; eran artefactos de la extracción automática.

---

## 4. Citas mal usadas: un patrón, no casos sueltos

No son descuidos aislados. Hay una tendencia a **estirar la fuente** hasta la conclusión que el
párrafo necesita, y otra a **hacer cargar afirmaciones metodológicas a documentación comercial**.

**La fuente no trata el tema de la afirmación**

- §16.4.1: «pueden reducir la carga cognitiva y la fatiga de alerta asociada con falsos positivos
  frecuentes **(Du et al., 2024)**». Du et al. (2024) es *Exploring the State-of-the-Art in
  Multi-Object Tracking*, un survey técnico que no estudia fatiga de alerta.
- §15.2.5.2 y §16.4.1: la inestabilidad cuadro a cuadro atribuida a **Xiao et al. (2024)**, que es
  un paper de imagen estática y no mide estabilidad temporal. La segunda cita además generaliza a
  todos los OVD lo dicho de un modelo.
- §15.4.1.2: latencia, transporte seguro y control de congestión de WebRTC apoyados en
  **Keranen et al. (2018)**, que es el RFC de ICE y trata NAT traversal. La especificación de W3C
  está en el listado y no se cita ahí.
- §15.2.5.3 y §16.3.3: la sensibilidad del prompt **en detección** apoyada en **Zhou et al.
  (2022b)**, que es CoOp, sobre clasificación con CLIP. El propio informe advierte dos párrafos
  antes que lo de clasificación «no se transfiere directamente al contexto de detección».
- §15.2.5.1: «compatibilidad textual evaluada de manera independiente para cada región candidata
  (Zareian et al., 2021; **Liu et al., 2024**)». §15.2.1.1 describe a Grounding DINO como fusión
  profunda en el decoder, es decir lo contrario.
- §16.3.4: el solapamiento léxico y la negación atribuidos a **Liu et al. (2024)**, que no estudia
  ninguno de los dos.

**Cifra publicada atribuida a un repositorio o a una ficha de modelo**

- §15.2.1.1: los AP de MM-Grounding-DINO citados como «(IDEA-Research, 2024c; X. Zhao et al.,
  2024)». MM-Grounding-DINO es de OpenMMLab, y el paper está en la misma cita: alcanza con él.
- §15.2.1.3: los AP de OWLv2 **L/14 y G/14** citados con «(Google, 2022, 2023; …)», donde
  Google (2023) es la ficha de `owlv2-**base**-patch16-ensemble`, que no puede sostener cifras de
  las variantes grandes. Para la licencia de los pesos, en cambio, la ficha es la fuente correcta.

**Documentación de fabricante cargando una conclusión metodológica** (§17.1.4.1, cuatro casos):
HP Inc. sosteniendo que el hardware condiciona resolución, precisión numérica y elección de
runtime; Luxonis sosteniendo el reparto de roles entre borde y CPN; la página de producto del
Video Codec SDK de NVIDIA sosteniendo el efecto sobre el reparto CPU/GPU, cuando la guía de NVDEC,
que sí lo trata, ya está en el listado; y los papers de Grounding DINO y YOLOE sosteniendo
compatibilidad de frameworks y rutas de inferencia acelerada, que no es lo que esos papers tratan.

**Afirmación de consenso sobre una sola fuente, que es la proponente del método**: §15.2.5.3,
«Se demostró que la optimización automática de representaciones de prompts […] supera
consistentemente a los prompts elaborados mediante ingeniería manual (Du et al., 2022)».

---

## 5. Riesgo de plagio: dónde está y dónde no

**No hay transcripción literal sin atribuir.** En todo el informe hay sólo dos fragmentos
entrecomillados largos: una salida del propio sistema y el título de un paper. Tampoco se detectó
prosa que parezca traducida de un abstract. El riesgo formal más común no está presente.

El riesgo real es otro: **vocabulario y definiciones de terceros presentados en primera persona**.

**Definiciones de métricas y términos ajenos sin atribuir**

- §17.1.6.4: «**TETA** es Track Every Thing Accuracy y se descompone en LocA, ClsA y AssA». Es la
  definición de una métrica de terceros y su fuente, Li et al. (2022), **ya está en el listado**.
  Contrasta con MOTA, IDF1 y HOTA, que sí llevan sus tres fuentes en §17.1.7.3. Es el hueco de
  atribución más nítido del informe.
- §17.1.7.5 y Anexo D: «**G2A** = Glass-to-Algorithm», definido dos veces sin citar a Bachhuber et
  al. (2018), que acuñó el término, y además **con la frontera estrechada**: el original arranca en
  el vidrio y acá arranca en el `dequeue`. El texto es honesto en lo técnico, dice «No equivale a
  sensor → algoritmo»; le falta la atribución y una línea que declare el cambio de frontera.
- §17.1.5.4: intervalos de confianza «obtenidos por **bootstrap**», sin fuente, en un párrafo donde
  kappa sí está atribuida a Cohen.
- §15.3.1 y §16.4.2: **el algoritmo húngaro y el filtro de Kalman** se nombran sin cita. Ver el
  punto 8.

**Patrones y estilos de arquitectura descritos como acuñación propia** (§17.3): publicación-
suscripción y su semántica de pérdida por suscripción tardía, tubos y filtros («El flujo interno se
organiza como una cadena de transformación progresiva…»), el patrón adaptador —que es el mecanismo
de sustituibilidad de toda la arquitectura, en DA-05—, el registro de sólo adición, la clave de
idempotencia y el ledger de entregas, la taxonomía de requisitos no funcionales de la Tabla 40, y
`fail-open`, introducido con un «denominado» que lo presenta como acuñación del trabajo. El listado
ya tiene a Bass, Clements y Kazman (2022) y no se lo cita nunca.

**Tecnologías centrales sin ninguna entrada en las 242 referencias**, verificado uno por uno:

| Tecnología | Dónde carga peso |
|---|---|
| **ZeroMQ** | §17.3.3 justifica su adopción por latencia y ausencia de broker |
| **msgpack** | §17.3.3 afirma que «reduce el costo de serialización respecto del texto plano» |
| **MQTT** | §17.3.7 y §17.4.1; es el único canal de entrega ejercido del sistema |
| **CVAT** | §17.4.6; con ella se construyó toda la referencia humana de evaluación |
| **Swin Transformer** | §17.4.4 remite a §15.2.1.1 por los *backbones*, que no tienen fuente |

**Y el hallazgo más serio de §17.4**: el detector de vocabulario abierto y el algoritmo de
seguimiento que **preanotaron la verdad de terreno** no se nombran, ni con versión ni con cita
(«Cada clip se preanotó automáticamente con un detector de vocabulario abierto de mayor capacidad
que el modelo evaluado, elección deliberada para evitar circularidad»). Sin identificarlos, el
argumento de no circularidad no se puede auditar ni la referencia se puede reproducir. En la misma
línea, la biblioteca de entrenamiento cuyo comportamiento interno justifica descartar una corrida
entera tampoco se nombra, y ni la biblioteca de validación visible en el propio fragmento de código
ni el framework HTTP aparecen en ningún lado.

---

## 6. §17.5 reporta sin vara, teniendo la vara al lado

§17.5 tiene **cero citas** en 4.833 palabras. Que las cifras propias salgan de artefactos del
proyecto está bien. El problema es que **ninguna se lee contra una cifra publicada**, y §15 tiene
relevadas y citadas exactamente las que hacían falta. Verificado que existen en §15:

| Lo que §17.5 reporta | La vara que §15 ya tiene |
|---|---|
| mAP50 0,551, «el más alto en el agregado» | «YOLOR alcanzó un mAP@0,5 de 0,883 sobre SHEL5K»; «YOLOv5x alcanzó un mAP@0,5 de 0,866 sobre CHV» |
| recall de CR-01 por evidencia directa, 0,308 y 0,599 | «la clase *head* —cabeza sin casco— alcanzó 0,1024 AP» zero-shot, y «AP@0,5 de 0,907 para la clase head» supervisado |
| p95 de 630 a 890 ms, «fuera del presupuesto» | «La literatura reporta órdenes de 10–30 ms para alternativas one-stage optimizadas y 50–150 ms para Transformers» |
| 1,16 a 4,42 fps en vivo | la tabla de puntos de operación publicados de §15.2.3.1 |

Además, en §17.5 **los dos datasets que aportan el 98 % del banco no se nombran** («obra con mayor
cobertura de chaleco», «una fuente con clase nativa de cabeza descubierta» son CHV y SHEL5K, ambos
en el listado), el modelo campeón aparece sólo con su alias interno, Grounding DINO no se nombra ni
una vez, COCO 2017 se usa como material de retención sin citar a Lin et al. (2014), y las métricas
excluidas —las de seguimiento multiobjeto— se declaran no ejecutadas sin nombrarlas: una exclusión
sólo es defendible si el lector sabe qué se excluyó.

El arreglo no es investigación nueva. Es tejer §17.5 con §15 y §16 mediante remisiones y una docena
de citas que ya están en el listado. **Cuidado con una trampa**: la vara más pertinente, Choi y
Greer (2024), es una de las que no tienen entrada. Hay que darla de alta antes de apoyarse en ella.

---

## 7. §11 a §14: cuatro mil quinientas palabras sin una sola referencia

Ni una. El párrafo de apertura afirma que la seguridad laboral en la construcción «constituye un
problema de alta relevancia técnica, social y organizacional» y caracteriza la limitación del
vocabulario cerrado, todo sin fuente. Es el lugar donde un jurado pregunta «¿según quién?», y es lo
primero que se lee.

Hay una buena noticia dentro: **el informe no arriesga ninguna cifra de accidentología, costo ni
adopción sin respaldo.** No dice «el X % de los accidentes fatales en obra». Ese error clásico no
está. Lo que hay son tres afirmaciones sustantivas presentadas como sentido común:

- «Los sistemas tradicionales de detección de objetos operan, en general, bajo un paradigma de
  vocabulario cerrado». Es **la premisa que justifica el trabajo entero**, y Zareian et al., Gu et
  al. y Liu et al. están en el listado exactamente para eso.
- «La observación humana continua puede verse afectada por fatiga, distracciones, simultaneidad de
  eventos o limitaciones propias de la atención sostenida». Afirmación empírica sobre atención
  sostenida, sin fuente, y es la que sostiene la utilidad del sistema frente al supervisor humano.
- §14.2.1 anuncia una revisión de la normativa de seguridad en construcción y §13.2 fija como
  objetivo analizar los fundamentos normativos, sin nombrar ni una norma, teniendo el Decreto
  911/96, el Decreto 351/79, la Ley 19.587 y dos resoluciones de la Superintendencia en el listado.

En §11, el glosario define MOTA, IDF1 y HOTA sin atribución, cuando el Anexo A sí las cita. Es
incoherente hacia adentro.

El trabajo **tiene con qué responder**: todo está en §15, §16 y §16.2.1. Falta traerlo. Es la
corrección de mayor retorno de la auditoría: entre seis y diez citas bien puestas.

---

## 8. Huérfanas, bajas, y el paper de 1955

**104 de las 242 entradas están huérfanas: el 43 %.** Se verificó dos veces, por clave autor-año y
después buscando el apellido cerca del año; el segundo paso rescató 31 entradas que sí estaban
citadas. La causa es conocida: la Etapa 1 podó el estado del arte a menos de la mitad y la
reestructuración de §17.1 recortó otro 35 %. El texto se achicó; el listado no.

| Tema de las huérfanas | Cuántas |
|---|---:|
| Streaming y protocolos de transporte | 32 |
| Borde, niebla, nube y benchmarks de hardware | 21 |
| Documentación de producto: Intel, GStreamer, FFmpeg, Mesa, drivers | 33 |
| Seguimiento y asociación de datos | 9 |
| Detección, OVD y datasets | 9 |

**Bajas propuestas, en orden de seguridad.** Ninguna es obligatoria: una huérfana no invalida nada,
sólo infla el listado y delata que el texto se recortó sin revisar la bibliografía.

1. **Las 53 de streaming y de borde.** §15.4 y §16.5 siguen existiendo y siguen bien sostenidas,
   con 22 fuentes cada una y densidad de 1 cada 110 palabras. Se pueden dar de baja sin dejar
   ninguna afirmación sin respaldo.
2. **Las 33 de documentación de producto** que ya no sostienen nada. Son las que más bajan la
   proporción de literatura arbitrada del listado.
3. **Las 18 de seguimiento y detección, una por una**: son las más cercanas al núcleo. Varias
   conviene conservarlas **citándolas**, no dándolas de baja.
4. **Ninguna de normativa y legislación**, aunque quede huérfana: en un trabajo sobre seguridad
   laboral el marco legal completo tiene valor propio. Sí conviene verificar la vigencia de la
   Disposición 11/2006 frente a la normativa posterior de la AAIP.

**El paper viejo es Kuhn (1955)**, «The Hungarian method for the assignment problem», la entrada
más antigua del listado, y **está huérfana**. Pero la baja directa no es la respuesta, porque el
texto sí nombra el algoritmo dos veces sin atribuir, en §15.3.1 y en §16.4.2, y hay una asimetría:
el **filtro de Kalman se nombra y no tiene ninguna entrada**. Recomendación: citar a Kuhn donde el
algoritmo aparece por primera vez y dar de alta a Kalman (1960). Son los dos clásicos que sostienen
a SORT, y una fecha de 1955 no es un defecto cuando lo que se cita es el origen de un método
vigente. La alternativa, tratar ambos como conocimiento de manual y dar de baja a Kuhn, también es
defendible; lo que no se puede es dejarlo como está. Corregir además «Húngaro» a «húngaro».

**Cohen (1960), la segunda más antigua, está bien y no se toca**: §17.1 la cita para definir kappa
y §17.5 declara que «La referencia temporal no tuvo doble anotación ni medida de acuerdo entre
anotadores». El protocolo prescribe, el resultado informa que no se ejerció. Único retoque: §17.5
no nombra la métrica, así que el lazo queda implícito.

**Y al revés: cuatro entradas del listado que §15/§16 debería usar y no usa.** Abdalwhab et al.
(2025), sobre modelos open-vocabulary en obra, es exactamente el cruce que §15.2.5.4 declara vacío,
y sólo se cita en §17.1. Con Yao et al. (2024) sobre OVDEval, Nath et al. (2020) y Duan et al.
(2022) sobre SODA pasa algo parecido. Su ausencia es el flanco más fácil de atacar cuando se
declara una brecha.

**Una brecha declarada sin protocolo de búsqueda.** «El relevamiento de publicaciones entre 2023 y
2026 no identificó evaluaciones de Grounding DINO o YOLO-World zero-shot sobre SHEL5K o CHV» y tres
subsecciones enteras de §15.4.3 con cero citas afirman qué **no** existe en la literatura. Una
afirmación negativa sobre el estado del arte necesita decir cómo se buscó: bases, cadenas, ventana
y fecha de corte. Alcanza con una nota metodológica.

---

## 9. Defectos de forma

**Entradas que comparten autor y año sin distinguirse.** IDEA-Research (2024) ×3 sin sufijo, y el
texto cita 2024a y 2024c. Roboflow (2025) ×2, ambas del 14 de noviembre. **NVIDIA aparece con dos
nombres de organización**, «NVIDIA» y «NVIDIA Corporation», y eso produce **dos entradas «s. f.-a»,
dos «s. f.-b» y dos de 2022**: una cita a «NVIDIA, s. f.-a» hoy es irresoluble. Hay que unificar el
nombre y renumerar toda la serie. En cambio Ren, T. (2024) ×3 **no es un error**: el texto los
distingue con «Ren, Chen, et al.» y «Ren, Jiang, et al.», que es la forma prevista.

**Homónimos sin inicial.** APA pide la inicial cuando dos autores distintos comparten apellido y
año. El informe lo hace bien con Li y Zhao, y no lo hace en **Jiang et al. (2024)**, 6 citas, con
Jiang, K. y Jiang, Q. en el listado; **Yao et al. (2024)**, 5 citas, con Yao, L. y Yao, Y.; y
**Zhang et al. (2022)**, 3 citas con inicial y 1 sin ella. En el caso de Jiang la ambigüedad cambia
la fuente: sin inicial, la cita sobre prompts visuales resuelve al trabajo equivocado.

**Dos estilos de conjunción conviviendo.** El listado usa «&» en 129 entradas y « y » en 8; en el
texto, las nueve citas de dos autores usan «&» y ninguna usa « y ». Para un TFG en español bajo APA
corresponde « y » en los dos lados. Reemplazo mecánico, pero hay que hacerlo simultáneo.

**Idioma y formato de fecha mezclados**: «Retrieved» en 16 entradas y «Recuperado» en 30; meses en
inglés en 28, en español en 16, y un tercer formato «(1996, 5 de agosto)» en 3.

**Orden alfabético**: correcto salvo un par, que se resuelve al unificar el nombre de NVIDIA.

**«SRT» es ambiguo en un informe de streaming.** El listado usa la sigla como autor para las
resoluciones de la Superintendencia de Riesgos del Trabajo, sin desarrollarla, y a la vez cita el
protocolo Secure Reliable Transport. Una cita «(SRT, 1997)» no se lee. Desarrollar el organismo.

**Cuatro estilos distintos para la legislación argentina** conviven en el listado: autor-país
(«Argentina, 2000»), norma como autor con fecha duplicada («Decreto 911/96 de 1996… (1996, 5 de
agosto)»), «Ley 19.587 de 1972… (1972)» y sigla de organismo («SRT, 1997»). Elegir uno.

**Fechas de consulta donde no corresponden**: 7 entradas de arXiv y 7 de GitHub las llevan, y APA
las reserva para contenido diseñado para cambiar. Nueve entradas arrastran el identificador de
arXiv dentro del título, entre corchetes, y dieciséis dicen «Recuperado» seguido directamente de
la URL, sin fecha.

**Entradas puntuales que un jurado señalaría**: «Stephen. (2026)» como autoría por nombre de pila,
con la etiqueta de lenguaje de GitHub tomada por descriptor de medio; «Go Packages» como autor,
que es un índice autogenerado y cuya fuente real ya está en el listado; la especificación de RTMP
enlazada a un anexo de litigio de la oficina de patentes; una entrada de Intel con el título
truncado con puntos suspensivos; y un artículo con tres de sus cuatro autores sin invertir, que
además rompe el orden alfabético.

**Una entrada pide justificación explícita**: Mazor et al. (2021), un *registered report* de
neurociencia de la conciencia. Si el cuerpo no la ancla con precisión, es la primera que van a
preguntar.

**Una URL cruda en el cuerpo**: la lista de reproducción de §17.4.6 aparece como dirección entre
paréntesis. Debería ser entrada del listado, con el detalle por video en el anexo de licencias.

**Rangos de latencia de la Tabla 8 sostenidos en fuentes no arbitradas.** La nota atribuye los
rangos a quince fuentes, pero ninguna RFC ni especificación publica latencias extremo a extremo:
los números sólo pueden venir de Roy (2024), un post del blog de Wowza, y de Sonono (2019), una
tesis de maestría. Hay que declarar que el origen es industrial, o reemplazarlos. El mismo problema,
sin ninguna cita, en §15.4.1.2: «RTSP/RTP puede operar aproximadamente entre 200 y 800 ms […]
valores de entre 1.000 y 2.000 ms o más».

---

## 10. Lo que está bien, y conviene no tocar

- **Autocontención impecable en las cinco secciones.** Ni un ADR por número, ni una ficha, ni una
  ruta del repositorio, ni un guion propio citados como fuente. Verificado con búsqueda exhaustiva.
  Los nombres de archivo de §17.4 son artefactos de salida del sistema y su nota los legitima.
- **Las diez tablas de §15 y §16 declaran fuente y llevan nota.** La Tabla 3 aclara que su columna
  de latencia se derivó de la tasa publicada y «no corresponde a una medición independiente». Ese
  cuidado es lo que un jurado espera y rara vez encuentra.
- **§17.1 atribuye bien lo más expuesto**: AP@0,5 a Everingham y Lin, MOTA, IDF1 y HOTA a
  Bernardin, Ristani y Luiten, kappa a Cohen, el *template* a Radford, el costo del vocabulario a
  Cheng, Wang y Liu.
- **§17.5 es sobria y honesta**: declara denominadores, separa estratos, distingue no computable de
  cero, marca censuras y reporta veredictos negativos pre-registrados.
- **La composición del listado es defendible**: 90 entradas con DOI y 36 preprints suman más de la
  mitad. La documentación de fabricante está donde tiene que estar, en el Anexo B y en el capítulo
  de medios: no existe paper arbitrado que diga qué codecs soporta un decodificador de una placa
  concreta. Las entradas normativas **son** fuente primaria, no un sustituto de una.
- **La nota de la Tabla A.1 hace lo correcto con una matriz comparativa**: declara sus diecisiete
  fuentes, advierte que «las cifras conservan el protocolo, el conjunto de evaluación y el hardware
  informados por cada fuente; por ello, no constituyen un benchmark homogéneo» y marca N/D donde no
  hay dato. Verificadas las veinte filas: cada modelo tiene su fuente. Eso desactiva el riesgo real
  de plagio en el lugar donde más suele aparecer. Le falta sólo una cosa: la columna de licencias
  no tiene atribución propia, y no puede salir de los papers, que no declaran licencia de pesos.

---

## 11. Plan de corrección, por retorno

1. **Fusionar el listado de `90e` en el del maestro.** Doce entradas, ya redactadas y corregidas,
   que resuelven diez de las once citas irresolubles. Es media hora de trabajo y es lo que más
   cambia. Después, **dar de alta sólo dos**: Liang y Han (2024) para OVT-B, y corregir el «Liu et
   al. (2023)» del Anexo B.
2. **Unificar cinco años y sufijos**: Minderer, Axis, Luxonis, IDEA-Research y Zhou.
3. **Dar de alta las tecnologías que sostienen decisiones**: ZeroMQ, msgpack, CVAT y Swin
   Transformer, y nombrar el detector y el seguidor que preanotaron la verdad de terreno. MQTT ya
   queda cubierto por OASIS (2019) al fusionar `90e`.
3-bis. **Reemplazar veintiún preprints por su versión publicada.** DETR, CLIP, SAM, LVIS, GLIP y
   GLIPv2, la trilogía DetCLIP, OV-DETR, Deformable DETR, DaViT, MaPLe, X-Decoder, APE, OWLv2,
   TETA, MLPerf, LLMDet y las dos fundacionales de OVD, Zareian et al. y Gu et al., están
   publicados en CVPR, ECCV, ICCV, NeurIPS, ICML, ICLR e ISCA. El listado ya lo hace con Grounding
   DINO y con OWL-ViT, así que la inconsistencia es interna. **Sube la proporción de literatura
   arbitrada del 37 % al 46 % sin agregar una sola fuente.**
4. **Atribuir lo que ya tiene fuente en el listado**: TETA a Li et al. (2022), G2A a Bachhuber et
   al. (2018), los patrones de arquitectura a Bass, Clements y Kazman (2022).
5. **Poner citas en §11–§14**, trayendo las que ya están en §15, §16 y §16.2.1.
6. **Tejer §17.5 con las varas de §15**, con remisiones y una docena de citas ya disponibles.
7. **Desdoblar las siete citas estiradas** del punto 4, y degradar las cuatro fuentes de fabricante
   a lo que sí prueban.
8. **Agregar iniciales** a Jiang, Yao y Zhang; unificar «&» por « y »; unificar idioma de fechas.
9. **Declarar el protocolo de búsqueda** que sostiene las brechas.
10. **Decidir las bajas** del punto 8, empezando por las 53 de streaming y borde.

---

## 12. Hallazgo posterior, del mismo día: la Figura 4.3 contradice al sistema

No es bibliográfico, pero apareció al escribir la guía de figuras y es del mismo orden de gravedad,
porque **un lector confía en el dibujo más que en el párrafo**. Verificado contra el motor de
patrones del plano de control, leyendo el código, no la documentación.

| Lo que la Figura 4.3 dibuja hoy | Lo que hace el sistema |
|---|---|
| `candidate → inactive`, «evidencia insuficiente / no persiste» | desde `candidate` el patrón va a **`resolved`**, no a `inactive` |
| `resolved → inactive`, «cierre del episodio» | **no existe ninguna transición hacia `inactive`**: es sólo el estado inicial y nada vuelve a él |

Faltan además tres cosas que el sistema sí hace: el **salto directo a `confirmed`** cuando la
primera evidencia ya cumple la ventana; la **reapertura desde `resolved`**, que es la que produce
las re-alertas que §17.5 contabiliza aparte de los falsos positivos; y los **dos caminos distintos**
por los que se llega a `resolved`, despeje sostenido y ausencia por expiración.

**El texto de 17.3.6.1 arrastra el mismo error**, en dos oraciones: «el episodio pasa a resolved y
retorna a inactive» y «el patrón vuelve a inactive sin generar una alerta». §17.3 está cerrada, así
que la corrección la decide el autor. La versión correcta y completa, lista para dibujar, está en
la sección 5.3 de [`../../figuras/GUIA-DE-FIGURAS.md`](../../../figuras/GUIA-DE-FIGURAS.md).

---

## 13. Fuera de la bibliografía, para la entrega

- **§17.2 «Costos asociados» dice `[Pendiente]`**; §17.6 y §18 dicen `[Agregado futuro]`. Las tres
  últimas están previstas para la Etapa 6, pero **§17.2 no está en ningún plan**: hay que
  escribirla o sacarla del índice.
- **Catorce números de tabla libres** en la numeración global (12–15, 18–19, 31–32, 36–38, 53–55).
  Se resuelve al integrar, con campos de Word.
- **Cuatro entradas viven sólo en el Anexo A y cuatro sólo en el Anexo B.** Si esos anexos no
  llegan a §19, esas ocho quedan huérfanas y además dejan dos remisiones colgadas en §15.2.3 y
  §15.3.3.
- **Una baja pendiente ya anotada**: «AAIP, s. f.-b», cuyo párrafo se borró.
- **El typo «puede puede»** de §15.2.4 sigue ahí; se corrige en Google Docs.
