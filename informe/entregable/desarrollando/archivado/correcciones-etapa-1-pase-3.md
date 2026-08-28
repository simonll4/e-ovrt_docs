# Correcciones a la Etapa 1 — pase 3: §16 Marco Teórico, Anexo A y cierre de §15

- **Fecha:** 2026-08-27 · **Para:** el redactor de la Etapa 1.
- **Qué cubre:** las **dos piezas de la Etapa 1 que nunca recibieron un pase** — §16 Marco
  Teórico (30.749 palabras) y el Anexo A — más los tres residuales que dejó el pase 2 sobre
  §15. Con esto la Etapa 1 queda completa.
- **Por qué existe:** `AJ-1.16` declaraba un hueco: *"el §16 no fue relevado contra el estado
  actual del proyecto… es un hueco de relevamiento, **no** una afirmación de que el §16 esté
  bien"*. Este documento **es** ese relevamiento.
- **IDs:** continúan la serie — comentarios **E1-24…E1-4x**, decisiones **D-E1-9…**.
- **Estado de §15:** pases 1 y 2 **aplicados y verificados**; no se vuelve a tocar salvo R1–R3.

---

## 0. Veredicto

**§16 está en peor estado que §15 antes del pase 1**, por tres razones que no se pisan:

1. **Nunca se le aplicó ningún pase.** Las erratas de cita que `AJ-1.10` corrigió en §15
   siguen enteras acá, y ahora **producen contradicciones entre secciones del mismo
   informe**: la misma obra citada con dos años distintos en §15 y en §16.
2. **Una afirmación de §16 quedó refutada por el §15 corregido.** §16.3.5.1 sostiene que la
   retención open-vocabulary depende de la familia arquitectónica; §15.2.3 y §15.2.4, tras
   el pase, dicen exactamente lo contrario y con fundamento. Si se entregan así, el informe
   se contradice a sí mismo en una página.
3. **Falta el fundamento conceptual del mecanismo central de la tesis.** La palabra
   *negación* aparece **cero veces** en §16 — y §16.3 es, por guardrail, "el corazón
   conceptual". Eso es una **adición**, no una poda, y manda sobre las podas.

Además, §16 repite el patrón que el pase 2 corrigió en §15, pero **peor**: tiene **cuatro**
secciones "Criterios orientadores para la selección de X" (3.628 palabras) que enuncian, en
voz normativa, requisitos que son decisiones del proyecto — **§16.4.4 y §16.7.4 no tienen ni
una sola cita**, y varias exigen capacidades que el trabajo nunca ejerció (prompts visuales,
segmentación, multi-protocolo, multi-flujo, jornadas de 8–10 h). Y hay un dato que ordena
todo el capítulo: **§16.7 y §16.8 suman 4.790 palabras con cero referencias** — la única masa
de texto de ese tamaño sin literatura en todo el marco teórico, y justo donde más prescribe.

**Sobre la extensión:** §16 tiene 30.749 palabras y las podas autorizadas (PODA-05…11)
proyectan **≈−16.500**. Igual que en §15, la reducción está justificada **en el agregado**:
§16.5 solo (12.926 palabras, el 42 % del capítulo) desarrolla códecs acelerados, frameworks,
nube y niebla que la plataforma no usa, y contiene **1.425 palabras que son la misma
subsección escrita dos veces**. Pero hay dos advertencias que cambian cómo se aplica:

- **PODA-06 y PODA-07 no son recortes, son reescrituras:** lo que mandan conservar **hoy no
  está escrito o está mal**. La ecuación que define la latencia extremo a extremo **está
  vacía** en el archivo; la descomposición de §16.5 tiene **seis** componentes y la que usa el
  resto del informe tiene **cuatro** (y le falta `t_preprocess`); y el patrón
  productor/consumidor que PODA-07 manda conservar **no aparece en el capítulo**.
- **§16 no debe salir solo más corto: debe salir con el mecanismo de la tesis fundado**, que
  hoy no está (E1-25).

---

## 1. Residuales de §15 (cierre del pase 2)

Rápidos y acotados; ninguno supera las 150 palabras.

**R1 · 🟡 · Tabla 4, fila OWL-ViT/OWLv2 "Fine-tuning end-to-end con regularización".** Es la
única fila que la prosa ya no sostiene: la palabra "regularización" aparece **solo dentro de
la tabla**. Agregar una oración en el párrafo de dual-encoders de §15.2.4 —*"el ajuste sobre
datasets cerrados exige estrategias de regularización para no colapsar el espacio de
embeddings compartido del que depende la capacidad abierta (Minderer et al., 2022)"*— o
eliminar la fila.

**R2 · 🟡 · Formato de la ficha de Florence-2.** Su rótulo ("Arquitectura, entrenamiento y
disponibilidad.") va **sin negrita**, mientras las demás fichas usan rótulos en negrita.
Unificar también la puntuación del rótulo, que quedó inconsistente entre fichas
(`**Arquitectura base.**` vs `**Arquitectura base**.`).

**R3 · 🟠 · Delta de referencias.** Verificado contra el listado vigente:
- **Dar de alta** (no existen): *Kumar et al. (2022)* · *Lee et al. (2023)* · *OASIS (2019)*
  · *Ultralytics (2026)*.
- **Corregir**: la cita dice *Luxonis (s. f.)* y la entrada del listado es
  **`Luxonis. (s. f.-b). OAK-D Pro PoE`** — lleva letra.
- **Ya existen y están bien** (no tocar): AILab-CVC 2024 · Google 2022/2023 · Kirkpatrick 2017
  · Li, L. H. 2021 (GLIP) · Microsoft 2024 · THU-MIG 2025 · IDEA-Research 2024a/2024c ·
  Adžemović · Rasaee · Ucar.
- **Bajas** que arrastra la poda de §15: OV-DETR, OV-DINO, OmDet-Turbo, Detic, DetCLIP,
  Grounded SAM / SAM 2, OVTrack, Roboflow/RF-DETR, Janus, Kurento, MediaMTX, OvenMediaEngine,
  SRS, y las obras de RTMP/HLS/DASH/CMAF/WebRTC/SRT/RIST **que ya no se citan en prosa**.
  ⚠ **Cuidado:** lo que sobreviva citado **solo en la nota de la Tabla 8 se conserva**
  (decisión D-E1-8). Verificar fuente por fuente antes de dar de baja.

---

## 2. §16 — hallazgos transversales

Estos cuatro valen para todo el capítulo y conviene resolverlos en una sola pasada.

### E1-24 · 🔴 · §16 contradice al §15 corregido sobre retención y fine-tuning

**Dice hoy** (§16.3.5.1, criterio "Independencia de entrenamiento específico por dominio"):

> *"la evidencia analizada en la sección 15.2.4.5 muestra que la capacidad de una
> arquitectura para preservar su generalización open-vocabulary durante el fine-tuning varía
> sustancialmente entre familias de modelos. Los detectores con fusión visión-lenguaje
> profunda y no removible exhiben mayor resiliencia frente al ajuste de dominio, mientras que
> aquellos con módulos de texto reparametrizables o desacoplables tienden a converger hacia un
> comportamiento closed-set."*

**Por qué está mal.** El §15, ya corregido, sostiene lo contrario y lo argumenta: *"La
evidencia revisada **no permite atribuir** la retención open-vocabulary a una familia
arquitectónica por sí sola, porque las comparaciones utilizan datos, módulos entrenables y
protocolos diferentes. La retención depende de la receta aplicada… **no debe inferirse de la
profundidad o removibilidad de la fusión**"* (§15.2.3), y §15.2.4 cierra: *"no corresponde
afirmar que una familia tolere mejor el ajuste completo"*. Son dos afirmaciones incompatibles
en el mismo informe, separadas por unas páginas.

**Encima, el puntero está roto:** cita **"sección 15.2.4.5"**, que tras la reorganización de
§15 ya no existe (el fine-tuning es ahora **§15.2.4**).

**Qué hacer.** Reescribir el criterio alineado al §15: la retención se describe **por receta
concreta** (qué parámetros se actualizan o congelan, si se conserva supervisión lingüística
amplia, si se evalúan categorías no vistas) y **no se infiere de la arquitectura**. Corregir
el puntero a §15.2.4. Es la corrección más urgente del capítulo.

### E1-25 · 🔴 · Falta el fundamento conceptual del mecanismo central de la tesis

**Qué pasa hoy.** En las 30.749 palabras de §16, la palabra **"negación" aparece cero veces**;
**"bolsa de palabras" / *bag-of-words*, cero**. §16.3 —que el guardrail protege como *"el
corazón conceptual de la tesis"*— explica qué es OVD, cómo alinea visión y lenguaje y que los
prompts son sensibles a la redacción, pero **nunca explica por qué una condición formulada
como negación puede fallar**, ni qué alternativa conceptual existe.

**Por qué importa.** Ese es el mecanismo que la tesis ejerce: el sistema **no le pide al
modelo la infracción como frase**, sino evidencia positiva, e **infiere la ausencia por
relación espacial**. El §15 ya trae la evidencia empírica de la dificultad (Chen y Zou 2025:
IoU < 20 % con restricciones de atributo; Choi y Greer 2024: `head` 0,1024 frente a `hardhat`
0,6493 sobre las mismas imágenes) — **pero la evidencia no es el fundamento**. Hoy el lector
llega a §17 sin haber leído nunca por qué el sistema razona la ausencia en vez de pedirla.

**Qué hacer.** Un bloque nuevo en §16.3 (≈400–500 palabras, entre §16.3.3 y §16.3.4), con dos
piezas y **sin un solo dato propio**:

1. **Por qué la composición y la negación son difíciles para un encoder contrastivo.** El
   entrenamiento contrastivo optimiza la correspondencia global imagen–texto y no obliga a
   representar la estructura de la frase; en consecuencia estos modelos se comportan, en
   buena medida, como *bolsa de palabras*: la representación de una frase con modificador
   queda dominada por sus sustantivos. Literatura verificada y directamente aplicable:
   - **Yuksekgonul, M., Bianchi, F., Kalluri, P., Jurafsky, D., & Zou, J.** — *"When and why
     vision-language models behave like bags-of-words, and what to do about it?"*
     (arXiv:2210.01936). Introduce el benchmark **ARO** (Attribution, Relation, Order,
     >50.000 casos) y muestra el desempeño pobre de VLMs de referencia en relación y
     atribución. **Es la cita canónica del mecanismo.**
   - **Thrush, T., Jiang, R., Bartolo, M., Singh, A., Williams, A., Kiela, D., & Ross, C.** —
     *"Winoground: Probing Vision and Language Models for Visio-Linguistic Compositionality"*
     (arXiv:2204.03162): con captions de **palabras idénticas y distinto orden**, los modelos
     evaluados no superan el azar. Aísla la composición del contenido léxico.
2. **La consecuencia de diseño, enunciada como alternativa conceptual y no como decisión
   nuestra:** si el modelo resuelve mejor "qué hay" que "qué falta", una condición definida
   por ausencia admite dos formulaciones —pedir la ausencia al modelo, o pedir la evidencia
   positiva y derivar la ausencia mediante razonamiento espacial sobre las detecciones—, y
   **cuál rinde mejor es una pregunta empírica que el estado del arte no responde**. Eso
   enlaza limpio con §15.2.5.1 (contextualización semántica limitada) y deja la brecha
   abierta para que §17.5 la conteste.

**Redacción, sin violar el no-anacronismo:** describir el problema y las dos formulaciones
posibles. **No** escribir que el proyecto eligió una, ni nombrar `E-IND`/`E-DIR`, ni dar
umbrales, regiones anatómicas ni resultados.

### E1-26 · 🟠 · Las cuatro secciones "Criterios orientadores": el mismo fallo que el pase 2 corrigió en §15

§16 tiene **cuatro** secciones de criterios de selección: **§16.3.5** (modelos OVD, 1.135 w),
**§16.4.4** (métodos MOT, 340 w), **§16.5.5** (protocolos y stack, 1.343 w) y **§16.7.4**
(selección tecnológica, 810 w) — **3.628 palabras**. Enuncian en voz normativa ("el modelo
**debe** sostener…", "**resultan preferibles** modelos que…") requisitos que son las
decisiones del proyecto. Es exactamente lo que en §15.3.2.1 hubo que reescribir (E1-16).

Tres agravantes concretos, verificados:

- **§16.4.4.1 no tiene ni una cita.** Sus cinco criterios ("Compatibilidad con detección
  open-vocabulary", "Latencia compatible con tiempo real", "Desacoplamiento arquitectónico",
  "Independencia de entrenamiento específico", "Robustez operativa suficiente") son las
  propiedades exactas del tracker que se construyó, presentadas como conclusión de la
  literatura. El último llega a justificar la elección de antemano: *"aun cuando no alcance el
  máximo rendimiento en benchmarks académicos"*.
- **Dos criterios exigen capacidades que el trabajo nunca ejerció.** §16.3.5.1 declara que
  *"el modelo **debe** permitir… ejemplos visuales de referencia (visual prompts)"* — la
  plataforma nunca usó prompts visuales; y §16.3.5.2 propone *"capacidad de extensión hacia
  segmentación"* — no hay segmentación en la tesis. Por la **regla de honestidad** (lo
  pre-registrado y no ejercido no se borra en silencio), o se baja de requisito a dimensión
  descrita en la literatura, o se declara con su causa. Lo que **no** puede quedar es un
  "debe" que el trabajo incumple sin decirlo.
- **§16.3.5.2 propone una arquitectura que el proyecto probó y descartó:** *"Configuraciones
  híbridas —donde diferentes modelos se ejecutan según la complejidad de la consulta o el
  contexto operativo— emergen como alternativas viables"*. Es especulación no fundada, y
  además anticipa un camino cuyo resultado se relata en §17.5.

**Qué hacer con las cuatro.** El §16 debe dejar **dimensiones de comparación con cita**, no
requisitos. Fórmula: *"la literatura permite comparar los métodos a lo largo de N ejes —
X (fuente), Y (fuente), Z (fuente)—; qué peso recibe cada eje es una decisión del diseño, que
se toma y se justifica en el protocolo experimental"*. Con eso las cuatro secciones se
comprimen fuerte y dejan de invadir a §17.1. PODA-09 y PODA-05 ya autorizan comprimir dos de
ellas; E1-26 extiende el criterio a las cuatro.

### E1-27 · 🟠 · Erratas de cita: `AJ-1.10` nunca se aplicó a §16, y ahora contradice a §15

`AJ-1.10` unificó las citas inconsistentes **solo en §15**. En §16 siguen, y el contraste
entre secciones es verificable por cualquiera:

| Obra | §16 cita | §15 (corregido) cita | Problema |
|---|---|---|---|
| Grounding DINO (Liu et al.) | **2023** | **2024** | misma obra, dos años, en el mismo informe |
| Florence-2 (Xiao et al.) | **2023** | **2024** | ídem |
| MS COCO (Lin et al.) | **2014 y 2015** (ambos, en §16) | **2014** | ídem, y ya inconsistente dentro de §16 |
| CoOp / prompt learning (Zhou et al.) | **2021, 2022a, 2022b** *(y 2019)* | **2022b** | la **misma obra citada como 2021 y como 2022a en párrafos contiguos** (§16.3.3) |
| Ren et al. | 2024, 2024a, 2024b, 2024c | "Ren, Jiang / Ren, Chen / Ren, Liu, et al." | dos convenciones distintas para desambiguar |
| Minderer et al. | 2022 | 2022 y 2023 | falta OWLv2 en §16 |

**Qué hacer.** Unificar §16 **contra §15**, que es el que ya pasó verificación, y adoptar en
todo el capítulo la convención de desambiguación por apellido de segundo autor que §15 usa
para Ren.

### E1-28 · 🟠 · Tres referencias cruzadas colgadas o hacia adelante

- **§16.4.2.3:** *"En sistemas que incorporan apariencia **(el análisis del modelado de
  apariencia)**, la asociación se beneficia…"* — paréntesis que perdió su destino. **Es
  literalmente el mismo defecto que se corrigió en §15.3.1.2**: viene del documento fuente y
  hay que buscarlo en todo el capítulo, no solo acá. Reemplazar por "(§16.4.2.4)".
- **§16.4.3:** *"…mantiene la separabilidad entre el **plano de medios** —ingesta y
  procesamiento de video— y el **plano de control** —gestión de eventos y alertas—, de acuerdo
  con **la arquitectura modular definida**"*. Doble problema: nombra **nuestra** arquitectura
  con **nuestros** nombres, y remite a una sección posterior. Es anacronismo. Reescribir en
  términos genéricos ("separación entre la etapa de percepción y la de razonamiento sobre
  eventos") y quitar el reenvío.
- **§16.2.2.2:** *"…asegurando coherencia con el marco de evaluación **definido para el
  proyecto**"* — reenvío hacia adelante. Basta con "que se define en el protocolo
  experimental".

---

## 3. §16 — hallazgos por bloque

### 3.1 §16.1 Organización (474 w) y §16.2 Condiciones de riesgo (3.008 w) — **el ancla, se conserva**

Guardrail 1 protege §16.2: es lo que ancla las condiciones a la normativa; sin esto, las
condiciones que el sistema detecta son arbitrarias. **Está bien construido y se conserva**: la
cadena Ley 19.587 → Decreto 351/79 → Decreto 911/96 → Resoluciones SRT → ISO 45001 es sólida,
y la **Tabla 10** (obligación normativa → evidencia visual → condición detectable en video) es
el artefacto que justifica todo el dominio de aplicación. Su nota ya aclara que no constituye
selección de prompts. Correcto que liste ocho categorías aunque el trabajo ejerza dos: es el
universo normativo, no el alcance.

**E1-29 · 🟠 · §16.2.3 describe nuestra arquitectura de eventos.** El último párrafo dice:

> *"esta integración puede modelarse mediante una arquitectura orientada a eventos (EDA), en
> la cual cada evidencia visual detectada se materializa como un evento estructurado —por
> ejemplo, `persona_sin_casco_detectada`— que es publicado por el módulo de análisis de video
> y consumido por componentes especializados en evaluación de patrones, generación de alertas
> y registro de trazabilidad… la detección visual constituye la fuente primaria de eventos
> dentro del **plano de control** del sistema"*.

Eso no es marco teórico: es el diseño del sistema (§17.3), con su vocabulario. Además es
justo lo que PODA-10 autoriza a recortar de §16.2.3 (~300 palabras). **Eliminar el párrafo**;
el concepto que sí vale —que la prevención es un proceso continuo y que la alerta es insumo
de supervisión humana, no decisión autónoma— ya está dicho en los párrafos anteriores y en
§16.2.1.7.

### 3.2 §16.3 Percepción visión-lenguaje (2.542 w) — **el corazón, hay que reforzarlo**

Se conserva por guardrail. §16.3.1 (closed-set → open-vocabulary), §16.3.2 (alineación
contrastiva, CLIP) y §16.3.4 (zero-shot y long-tail) están bien y son el fundamento correcto.
Sobre esta sección operan **E1-25** (la adición del mecanismo de negación/composicionalidad —
lo más importante del pase) y **E1-24/E1-26** (§16.3.5).

**E1-30 · 🟠 · §16.3.3 dice tres veces lo mismo, con tres citas distintas de la misma obra.**
La subsección (589 w) tiene **tres párrafos consecutivos** que repiten el mismo contenido —
sensibilidad del prompt → *prompt learning* con tokens aprendibles → la optimización
automática supera al diseño manual (Du et al., 2022)— citando a Zhou como **2022a**, como
**2021** y de nuevo como **2021**. Consolidar en **un** párrafo (~250 w) con una sola cita
correcta. Es, además, el punto donde §16 duplica a §15.2.5.3, que ya trata la sensibilidad al
prompt: dejar en §16 el **fundamento** (por qué el texto es una especificación y por qué su
forma importa) y en §15 la **brecha** documentada.

### 3.3 §16.4 Persistencia temporal y MOT (2.684 w) — PODA-05

**Se conserva** lo que funda el trabajo: **§16.4.1** (la limitación del fotograma: por qué una
detección que no persiste no puede sostener una alerta — es el fundamento de la histéresis
temporal) y **§16.4.3** (integración OVD+MOT, que funda la identidad por sujeto). Ambos están
bien escritos y son de los mejores pasajes del capítulo.

**E1-31 · 🟡 · §16.4.2 (1.551 w) comprimir a ~700, como manda PODA-05.** Es un tratado de
fundamentos MOT: formulación del problema, filtro de Kalman y estimación de estado, LAP y
algoritmo húngaro con su complejidad O(n³), *gating*, distancia de Mahalanobis, ReID y
DeepSORT, oclusiones. La plataforma usa asociación **geométrica sin filtro de movimiento ni
apariencia**, y las métricas MOT están excluidas del alcance. Conservar: la formulación del
problema (predicción · similitud · asignación), IoU como métrica de similitud, y el
desacoplamiento *tracking-by-detection* —que es lo que permite integrar un detector OVD sin
reentrenar nada—. Comprimir fuerte Kalman, Mahalanobis, ReID/DeepSORT y complejidad
algorítmica: son correctos pero no sostienen ninguna decisión ni ningún resultado.
**Errata de paso:** §16.4.2.3 y §16.4.2.4 **explican IoU dos veces**, casi con las mismas
palabras.

**E1-32 · 🟠 · §16.4.4 (340 w): PODA-05 la elimina; aplicar con el criterio de E1-26.** No
hubo selección de método de catálogo, y sus cinco criterios no tienen citas. Si se prefiere
conservar algo, que sea **una** oración de dimensiones con cita dentro de §16.4.3.

### 3.4 Anexo A — la pieza que D-E1-7 rescató

**E1-33 · 🔴 · La Tabla A.1 conserva la errata de licencias que §15 ya corrigió.** Lista
**DINO-X**, **G-DINO 1.5 Pro** y **G-DINO 1.5 Edge** como **"Apache-2.0"**. El §15, corregido,
dice: *"se ofrecen mediante API y no publican pesos abiertos; la licencia Apache-2.0
corresponde al SDK de acceso y no al modelo"*. Es `AJ-1.09` sin aplicar, y hoy **contradice
frontalmente al cuerpo**. Corregir a "API cerrada — Apache-2.0 aplica al SDK, no a los pesos".

**E1-34 · 🔴 · Grounding DINO no está en la Tabla A.1.** La matriz tiene 12 filas —DINO-X,
G-DINO 1.5 Pro, G-DINO 1.5 Edge, LLMDet, OV-DINO, DetCLIPv3, OWLv2 L/14, YOLOE-v8-L,
YOLO-World-L, OmDet-Turbo, YOLOE-v8-S, Florence-2-L— y **falta el Grounding DINO original**
(y MM-Grounding-DINO). Es el modelo sobre el que se construyó el trabajo. Con **D-E1-7** la
Tabla A.1 pasó a ser el lugar que conserva la amplitud del catálogo que salió del cuerpo, así
que el hueco es doblemente grave. **Agregar las filas de Grounding DINO (Swin-T y Swin-L, con
sus regímenes) y MM-Grounding-DINO**, y las de los modelos cuyas fichas se podaron del cuerpo
y no estén ya (GLIP, OV-DETR, Detic, APE, T-Rex2).

**E1-35 · 🟠 · Las Tablas A.2 y A.3 quedaron huérfanas.** Tras la poda, el §15 **solo** cita
la Tabla A.1: la **A.2** (limitaciones de MOTA/IDF1/HOTA) y la **A.3** (comparativa de
servidores de medios) ya no las llama nadie. Decidir explícitamente → **D-E1-9**. Recomendación:
**conservar la A.2** citándola desde §15.3.3 (sostiene la exclusión de las métricas MOT con un
argumento que hoy está comprimido en tres líneas) y **eliminar la A.3**, porque los servidores
de medios ya no sostienen ninguna decisión ni aparecen en el cuerpo.

---

## 4. Podas de §16 — qué se conserva, y con qué criterio

Las podas están autorizadas desde `ajustes/07` §4. El criterio es **aporte, no cuota**: una
subsección se queda si sostiene un concepto que el resto del informe usa. Y rige el
**guardrail 6**: las adiciones mandan sobre las podas — E1-25 (el mecanismo de negación)
**entra** aunque el capítulo esté adelgazando.

| Poda | Sobre | Hoy | Acción | Enmienda de este pase |
|---|---|---:|---|---|
| PODA-05 | §16.4 MOT | 2.684 | conservar 16.4.1 y 16.4.3; comprimir 16.4.2 → ~700; eliminar 16.4.4 | E1-31, E1-32 |
| **PODA-06** | §16.5.2 descomposición | 4.881 | conservar solo lo que define la latencia y sus componentes | ⚠ **es REESCRITURA**: la ecuación está vacía y la descomposición no coincide con la del informe (E1-36, E1-37) |
| **PODA-07** | §16.5.3 arquitecturas | 3.604 | comprimir a ~600 con el patrón productor/consumidor | ⚠ **es REDACCIÓN NUEVA**: ese patrón no está escrito, y hay que **agregar publish/subscribe** o el bus y MQTT quedan sin fundamento (E1-38) |
| PODA-08 | §16.5.4 borde | 2.741 | comprimir a ~700 | salvar **sí o sí** el filtrado cerca del origen y la convención borde/niebla/nube (E1-39 y tabla de §5) |
| PODA-09 | §16.5.5 criterios de stack | 1.437 | párrafo puente | aplicar con el criterio de E1-26; **no reciclar** el criterio multi-protocolo |
| PODA-10 | §16.6 ético-legal | 4.266 | conservar 16.6.2 y 16.6.6; podar 16.6.4/16.6.5; comprimir 16.6.7 | rescatar **una frase** de cada podada; E1-46, E1-47 |
| **PODA-11** | §16.7 + §16.8 | 4.790 | fusionar en un cierre de ~1.000; rescatar el mapa de brechas | ⚠ **el mapa está 5/6 duplicado con §15** (E1-51): se rescata **una** fila, no la tabla |
| — | §16.5.1 latencia como restricción | 503 | **NO TOCAR** (guardrail 3) | — |
| — | §16.2, §16.3 | 5.550 | **NO TOCAR** (guardrail 1) | salvo E1-29, E1-30 y **la adición E1-25** |

**Resultado esperado:** de 30.749 a **≈14.000 palabras**, con el mecanismo central de la tesis
fundado por primera vez. La cifra es consecuencia, no meta.

---

## 5. §16.5 — Operación en tiempo real (12.926 w, el 42 % del capítulo)

Aquí operan PODA-06 a PODA-09. Pero **dos de las cuatro no son recortes: son reescrituras**,
porque lo que mandan conservar hoy no está escrito o está mal.

### E1-36 · 🔴 · La ecuación que define la latencia extremo a extremo **está vacía**

En §16.5.2 (líneas 373–375) la ecuación **(1)** —la que descompone la latencia en sus
componentes— quedó como una tabla de dos celdas vacías: `|  | (1) |`. Se perdió al exportar
el documento. Lo mismo pasó con los símbolos en la nota de la Tabla 11 y, fuera de §16, en
§17.1.7 (*"no corresponde reportar ."*, *"G2A abarca , , y ."*).

Es **exactamente el contenido que PODA-06 manda conservar**, y hoy no existe. Reponer la
ecuación **antes** de podar nada; si no, la poda deja la sección sin su único aporte.

### E1-37 · 🔴 · La descomposición de §16.5 no coincide con la que usa el resto del informe

§16.5.2 descompone el pipeline en **seis** componentes (captura · codificación · transporte ·
decodificación · **renderizado** · inferencia). El §17.1.7 formaliza la latencia
extremo a extremo con **cuatro**: `t_capture`, `t_transport`, **`t_preprocess`**,
`t_inference`. Consecuencias:

- **`t_preprocess`** —redimensionado, normalización, copia de memoria hacia el acelerador—
  **no existe en §16.5.2**, y es el término que usan §17.1.7, §17.5 y las figuras.
- **Codificación, decodificación y renderizado no son componentes** de la latencia que el
  informe define y mide.
- La **Tabla 11** se titula *"Componentes de latencia del pipeline glass-to-algorithm"* pero
  incluye una fila *"Renderizado / Jitter Buffer ~10–120 ms"*, que por la propia definición de
  §16.5.1 pertenece al recorrido **hasta el vidrio**, no hasta el algoritmo. **La tabla mide
  una cosa y se llama por otra.**

**Por eso PODA-06 es una reescritura.** El bloque de ~1.400 palabras que se conserva debe
**establecer la descomposición de cuatro componentes** con la notación de §17.1.7, no podar
la de seis. Rehacer la Tabla 11 a cuatro filas o sustituirla por prosa.

### E1-38 · 🟠 · Lo que PODA-07 manda conservar tampoco está escrito

PODA-07 dice comprimir §16.5.3 "a ~600: el patrón productor/consumidor como fundamento
conceptual". **Ese patrón no aparece en §16.5**: la pareja "productor/consumidor" no está
escrita en ninguna parte del capítulo, y *backpressure* aparece dos veces, una en un párrafo
de meta-texto y otra dentro de una advertencia sobre un decodificador de hardware. Hay que
**redactar** esas ~200 palabras, no comprimirlas.

**Y hay un riesgo peor.** La plataforma acopla sus planos con un **bus publish/subscribe** y
distribuye alertas por **MQTT**. En todo el marco teórico, MQTT se menciona **una sola vez**,
de refilón, dentro del párrafo sobre un framework de terceros — **que es justamente uno de los
párrafos que PODA-07 elimina**. Aplicada tal cual, la poda dejaría al informe sin ningún
fundamento conceptual para el bus de eventos ni para la mensajería de alertas, que son dos
piezas centrales del sistema. El bloque comprimido debe incluir **publish/subscribe
desacoplado** como patrón, con cita (Cugola y Margara 2012 ya está citado en §16.5.3.1 y
sirve para ambos).

### E1-39 · 🟠 · Prescripciones de diseño y promesas incumplidas dentro de §16.5

- **§16.5.5 completa (1.437 w) es un pliego de requisitos del prototipo, no marco teórico.**
  Ejemplo: *"resulta conveniente que el framework… permita modificar parámetros de códec…
  **priorizando la flexibilidad de configuración sobre la portabilidad multiplataforma, que
  excede el alcance del prototipo**"* — una decisión de alcance del proyecto, sin cita,
  presentada como conclusión del análisis. La sección incluso **se autodesmiente**: abre
  diciendo *"La formulación de criterios no anticipa decisiones de diseño"* y a continuación
  las anticipa. → cae con PODA-09 (ver E1-26).
- **Promete evaluación multi-protocolo que nunca ocurrió** (§16.5.5.1.2: *"El soporte
  multi-protocolo… habilitar roles diferenciados según el tramo del pipeline"*). La ingesta
  construida es RTSP + SDK, y nada más. No reciclar ese criterio en el párrafo puente.
- **Promete un plano de control en la nube** (§16.5.3.1): *"escalabilidad distribuida, que
  habilita la ejecución del plano de medios en un nodo edge y el de control **en la nube**"*,
  y en la misma oración *"permite evaluar alternativas como GStreamer versus FFmpeg"*. Ni lo
  uno ni lo otro existió: un solo host, sin nube, y esa comparación nunca se hizo. §16.5.3.1
  **se conserva** (es el fundamento de la separación de planos, y está bien citado), pero
  **con esas dos cláusulas borradas**.
- **Tres subsecciones abren diciendo que analizan alternativas "para E-OVRT-VDP"** (códecs
  acelerados, mecanismos de comunicación entre procesos): ninguna de esas tecnologías entró al
  sistema. Caen con PODA-07.
- **La Tabla 11 receta protocolos que no se usaron**: *"SRT con latency budget ajustado"*,
  *"inferencia por GPU (TensorRT)"*. Al rehacerla, dejar solo estrategias documentadas sin
  nombrar stacks que el informe no vuelve a mencionar.

### E1-40 · 🟠 · Duplicación masiva, con prueba forense de que el material se escribió dos veces

- **§16.5.3.5 y §16.5.4.4 son la misma subsección escrita dos veces** (532 + 893 = 1.425 w):
  ambas sobre plataformas de hardware para el borde, ambas con Jetson, ambas argumentando que
  la métrica TOPS no es comparable, ambas remitiendo al mismo benchmark.
  **La prueba:** el mismo trabajo aparece como `Jeong et al., 2022a` en una y
  `Jeong et al., 2022b` en la otra, **con una sola entrada en el listado de referencias**.
  Idéntico patrón con `Shi et al., 2016a/2016b` y `X. Wang et al., 2020a/2020b`.
  **Las letras de desambiguación son falsas** y hay que corregirlas donde el texto sobreviva.
- **El umbral perceptual de interacción humana aparece cuatro veces**, siempre con las mismas
  dos citas: en §16.5.1, dos veces en §16.5.2.7 y otra en §16.5.5.1.1 (más una quinta vez en
  §15.4). Sobrevive **solo** el de §16.5.1, que es el que el guardrail protege.
- **Codificación y decodificación se explican dos veces** (I/P/B-frames, GOP, buffer de
  imágenes decodificadas), y el propio texto lo admite: *"Como se describió al tratar las
  configuraciones de codificación…"*. Ambas caen con PODA-06.

### E1-41 · 🟡 · Meta-texto y un anuncio que describe una estructura inexistente

Cuatro pasajes anuncian lo que viene en vez de decir algo. Uno es defectuoso además de
inútil: *"Las subsecciones siguientes caracterizan en detalle la latencia de inferencia…"* —
y **no hay subsecciones**: lo que sigue son párrafos. Otro cierra con una promesa sin destino:
*"Este concepto será ampliado en secciones posteriores"*, sin puntero ni sección
identificable. Eliminar los cuatro.

### E1-42 · 🟡 · Un encabezado con nivel equivocado

§16.5.2.5 ("Latencia de Renderizado") está un nivel más abajo que sus hermanas 16.5.2.1–.4,
así que hoy renderiza como hija de §16.5.2.4. Si se regenera la numeración automáticamente,
"16.5.2.5" pasa a ser "16.5.2.4.3". Como PODA-06 elimina esa subsección, el punto se resuelve
solo — pero **conviene verificar que no haya más encabezados con nivel mal puesto** antes de
regenerar la numeración del capítulo.

> ✅ **Un riesgo que ya está resuelto.** El §15 anterior remitía a "las secciones 16.5.2.3 y
> 16.5.2.5", que PODA-06 elimina. **El §15 vigente ya no contiene ningún puntero hacia §16**
> (desaparecieron al podar §15.4). Verificado: cero coincidencias. No hay nada que arreglar
> de ese lado; el trabajo pendiente es solo el inverso, los punteros de §16 hacia §15
> (E1-24, E1-28).

### Qué se conserva de §16.5, en concreto

| Bloque | Se conserva | Se va |
|---|---|---|
| **§16.5.1** (503 w) | **Íntegra** (guardrail 3): la latencia como restricción, la distinción entre el recorrido hasta el vidrio y hasta el algoritmo, el umbral perceptual y el principio de **presupuestar** el buffer en vez de eliminarlo | — |
| **§16.5.2** (4.881 → ~1.400) | Un bloque único que **define la latencia y sus cuatro componentes** con la notación de §17.1.7 + la ecuación repuesta (E1-36) · captura acotada por el período de cuadro · el transporte como el componente de mayor variabilidad externa, y que **lo que compromete el tiempo real es su cola, no su media** (funda el reporte por percentiles) · **párrafo nuevo de `t_preprocess`** · dos rangos de referencia de inferencia | codificación · decodificación · **renderizado** (no es parte de la latencia que se mide) · el catálogo de técnicas de optimización · §16.5.2.7 (duplica §16.5.1) |
| **§16.5.3** (3.604 → ~600) | **§16.5.3.1 separación de planos** casi íntegra, menos las dos cláusulas de E1-39 · **~200 w nuevos**: productor/consumidor con cola acotada y contrapresión, y **publish/suscripción** como patrón de notificación desacoplada (E1-38) | intro (meta-texto normativo) · códecs acelerados por hardware · comunicación entre procesos · frameworks de terceros · plataformas de borde (duplica §16.5.4.4) |
| **§16.5.4** (2.741 → ~700) | Las tres tensiones que motivan el borde · **la convención terminológica borde/niebla/nube y los tres patrones de despliegue** (permite entender, en §17.3, que se ejerció el prefiltrado en el dispositivo y se excluyó la inferencia en el borde) · **el punto de que filtrar cerca del origen reduce el consumo aguas abajo** — *es el fundamento conceptual del prefiltrado y lo único que PODA-08 debe salvar sí o sí* · opcional: que la latencia en el borde se juzga por percentiles | taxonomías de nube y niebla · geo-distribución y ciudades inteligentes · catálogo de aceleradores y métricas de hardware |
| **§16.5.5** (1.437 → ~120) | **Nada de los siete criterios.** Un párrafo que enuncie **la brecha**: la literatura evalúa por separado protocolos, stacks de códec y modelos, y no ofrece un marco integrado para presupuestar latencia extremo a extremo en un pipeline con inferencia open-vocabulary. Como esa brecha **ya está en §15.4.3.1**, el puente debe remitir sin repetirla | los siete criterios y las consideraciones complementarias |

**Ahorro de §16.5: ≈9.800 palabras** (de 12.926 a ~3.100).

---

## 6. §16.6 ético-legal, §16.7 convergencias y §16.8 (9.056 w)

### E1-43 · 🔴 · §16.7 y §16.8 suman **4.790 palabras con cero citas**

Es la única masa de texto de ese tamaño en todo el marco teórico que no se apoya en
literatura — y es justamente donde el capítulo prescribe con más fuerza. El **62 % de §16.7**
es literalmente recapitulación de §16.2–§16.6 o anticipo de §17: 1.393 palabras de resumen,
455 que describen la arquitectura del sistema y 838 de proyección metodológica. PODA-11 tenía
razón en llamarlo "meta-texto puro".

### E1-44 · 🔴 · §16.7.4: los "siete criterios orientadores" son el diseño del proyecto, sin una sola fuente

La subsección abre diciendo *"El análisis del estado del arte no selecciona tecnologías:
establece los criterios que deben orientar esa selección"* —es decir, se declara derivada de
la literatura— y a continuación desarrolla 810 palabras y una tabla **sin ninguna referencia**.
Cuatro de los siete criterios son el sistema construido, escrito en futuro:

- *"El flujo de video… y la lógica de negocio… **deben operar en planos arquitectónicamente
  separados**"*, evaluable por *"posibilidad de sustituir el modelo sin modificar el sistema
  de alertas"*. Eso **es** la arquitectura de dos planos, no un criterio de la literatura.
- *"Latencia de alerta medida en percentiles (P50, P95, P99)…"* — es el protocolo de medición
  propio.
- **El criterio 3 repite la afirmación que E1-24 refuta**: *"la preservación de esta capacidad
  **varía significativamente entre familias arquitectónicas**"*, otra vez sin fuente. Es la
  **segunda** aparición de la afirmación incompatible con el §15 corregido: al aplicar E1-24
  hay que corregir **las dos**.

Agravante: §16.8.2 presenta esos siete criterios como un **logro** del capítulo, así que el
problema es estructural. **Acción:** §16.7.4 completa se va (PODA-11). Lo que se quiera
conservar, va a §17.1 como decisión metodológica propia y declarada — que es donde
corresponde—, no a §16 como derivación del estado del arte.

### E1-45 · 🔴 · §16.7.5 describe la arquitectura implementada dentro del marco teórico

455 palabras, cero citas: *"El plano de medios… se estructura en cuatro etapas secuenciales:
ingesta… normalización… inferencia… tracking"*; *"Todos los eventos… se registran de manera
inmutable en el repositorio de event sourcing"*; *"La ruta crítica de latencia del sistema pasa
íntegramente por este plano"*. **El propio texto admite el origen**: *"coherente con la
arquitectura de dos planos planteada en el anteproyecto del proyecto"* — o sea, viene del
anteproyecto, no del estado del arte. Es anacronismo puro e invade §17.3. **Eliminar íntegra.**
Si algo se salva, una línea diciendo que la separación entre plano de medios y plano de
control es un patrón documentado — y eso ya vive, **con citas**, en §16.5.3.1.

### E1-46 · 🔴 · La Tabla 12 llama "decisiones de diseño" a controles que nunca se implementaron

§16.6.6 es **núcleo vivo** y la única tabla densamente citada del tramo (21 citas), pero su
columna se titula **"Decisión de diseño implicada"** y lista, entre otros: *"control de acceso
basado en roles con principio de mínimo privilegio; cifrado de flujos de video en tránsito;
registros de auditoría de acceso"*, *"señalización visible en obra; mecanismo de contacto con
el responsable del tratamiento"*, *"política explícita de retención y borrado seguro"*. En un
prototipo académico de un solo host, **leídas como decisiones tomadas son falsas**.

**El arreglo es de una palabra y salva la subsección entera:** renombrar la columna a
**"Restricción que impone al diseño"** y pasar a voz de exigencia las tres o cuatro celdas
que hoy están en presente descriptivo. Con eso dejan de ser falsas y quedan correctas.

### E1-47 · 🟠 · Una obligación legal abierta que el informe nunca cierra

§16.6.7 afirma: *"Cualquier validación experimental del prototipo que involucre personas en el
campo visual de las cámaras requiere evaluar la obligación de inscripción ante la AAIP y la
elaboración previa del manual de tratamiento… deberán definirse en la etapa 2."* **El proyecto
sí grabó personas.** Hoy queda una obligación planteada, remitida a una etapa, y nunca cerrada
— exactamente el hilo del que un jurado tira.

Además, esa fila **no es una brecha**: la inscripción es un requisito explícito y vigente,
resuelto en la norma; está en la tabla equivocada. **Acción:** sacarla de la tabla de brechas
e integrarla como una frase en §16.6.2.2, donde el requisito ya se enuncia; y **cerrar el
punto en §17.1/§17.4** (por qué el contexto controlado y académico no dispara la inscripción,
qué recaudo se tomó). → **D-E1-11**.

### E1-48 · 🟠 · Se promete razonamiento relacional multi-entidad; el trabajo entregó atributo por entidad

§16.7.3 y su párrafo de desarrollo concluyen que *"la arquitectura **debe** incluir una capa de
razonamiento contextual sobre las trayectorias… capaz de evaluar condiciones que involucren
**múltiples entidades y su relación espacial**"*, con ejemplos como *"persona en zona
restringida sin señalero visible"*. Las condiciones que el sistema evalúa son de **entidad
única más atributo**, con persistencia temporal. **No hay razonamiento relacional
multi-entidad**, y §17.5 no puede satisfacer esa expectativa.

Conservar la **brecha conceptual** (la detección por fotograma no modela relaciones — eso sí
es literatura y §15.2.5.1 ya lo dice con citas) y **borrar la prescripción arquitectónica**, o
declarar explícitamente que queda fuera del alcance. Mismo criterio para la enumeración
"arnés, chaleco reflectivo y señalero" cuando solo se ejercieron casco y chaleco.

### E1-49 · 🟠 · Dos preguntas rectoras quedaron huérfanas

§16.7.6 plantea ocho preguntas rectoras con código propio. Verificado sobre todo el
entregable: seis se retoman en §17.1, pero **dos no se retoman en ninguna parte** — la de
condiciones experimentales y la de recaudos ético-legales (que incluye *"consentimiento
informado… protocolo de anonimización"*, y es justo la que conecta con E1-47). O se eliminan
de la lista, o §17.1 las responde. No pueden quedar planteadas y sin retomar.

⚠ **Dependencia a vigilar:** §17.1 cita **"la sección 16.7.6" por su número** y usa los
códigos de esas preguntas nueve veces. Si §16.7.6 desaparece como subsección numerada al
fusionar, hay que actualizar esa remisión y las nueve invocaciones.

### E1-50 · 🟡 · Duplicación en §16.6 y §16.8

- **La introducción de §16.6 y §16.6.1 son el mismo texto dos veces** (249 + 243 w): ambas
  abren con la asimetría entre el trabajador y el sistema y con que *"esa asimetría no se
  resuelve declarando que el propósito es preventivo"*. Hay incluso un tercer párrafo que
  repite el encuadre. Las 492 palabras se comprimen a ~150.
- **§16.8 (429 w) no aporta nada que §16.7 no diga**, salvo tres líneas: las **tres
  limitaciones del propio marco teórico** de §16.8.2 (evolución acelerada del campo; datos de
  rendimiento obtenidos en condiciones no operativas; dinamismo del marco regulatorio). Eso
  se rescata; el resto —incluida la autoevaluación *"permitieron alcanzar los objetivos
  propuestos"*— se va. *(Al citarlas: no confundir con las limitaciones numeradas del
  proyecto, que son otra serie.)*
- **Tautologías** para eliminar de paso: *"deben utilizarse en la instancia de diseño
  arquitectónico para estructurar las decisiones de diseño arquitectónico"* · *"El diseño de
  esta capa es una decisión arquitectónica de la instancia de diseño arquitectónico"*. Y
  §16.7.2 es un título con 29 palabras de cuerpo, cuyo nombre es indistinguible del de
  §16.7.1.

### E1-51 · 🟠 · Corrección a PODA-11: el "mapa de brechas" que mandaba rescatar está 5/6 duplicado

PODA-11 designa el mapa de brechas transversales de §16.7.3 como *"lo único que se rescata"*.
**Verificado: cinco de sus seis filas ya están en §15**, algunas por triplicado:

| Fila de §16.7.3 | Ya está en |
|---|---|
| Ausencia de benchmarks para construcción | §15.2.5.4 · §15.3.4 · §15.4.3.1 |
| Métricas académicas no alineadas con el valor operativo | §15.2.5.5 · §15.3.4 · §15.4.3.4 — **triplicada** |
| Integración del pipeline no caracterizada | §15.4.3.1 · §15.4.3.2 |
| Condiciones composicionales | §15.2.5.1 |
| Sensibilidad al diseño de prompts | §15.2.5.3, casi textual |
| **Marco normativo-ético como restricción arquitectónica** | **única genuinamente nueva** |

**Lo transversal de verdad es una sola fila.** El cierre debe conservarla en prosa y
reemplazar las otras cinco por **una frase de remisión** a las tablas de §15 — no re-tabularlas.

### Qué se conserva de §16.6–§16.8, en concreto

| Bloque | Se conserva | Se va |
|---|---|---|
| **§16.6** (4.266 → ~2.850) | **§16.6.2 completa** (imagen como dato personal, etapas del tratamiento, roles, régimen argentino, identificabilidad indirecta, los tres ejes de la disposición aplicable): es lo que sostiene la minimización de evidencia visual efectivamente implementada · **§16.6.3** (seguridad de la información y retención) · **§16.6.6 con la Tabla 12 intacta**, aplicando E1-46 · **§16.6.7 comprimida a ~400 w en prosa**: las cuatro brechas legítimas con sus citas, sin la columna de implicaciones · **un solo párrafo** de encuadre (E1-50) | §16.6.4 referentes comparados — **rescatando una frase**: la distinción entre captación de video e identificación biométrica, que es lo que fundamenta excluir el reconocimiento facial · §16.6.5 gobernanza — **rescatando una frase** que sostenga las dos filas de la Tabla 12 que dependen de esas fuentes · el párrafo duplicado del encuadre · la fila de la AAIP (E1-47) |
| **§16.7 + §16.8** (4.790 → ~950) | Un cierre único, en cuatro bloques: **(1)** interdependencia de los dominios, ~200 w, sin "event sourcing" · **(2)** la única brecha genuinamente transversal, ~200 w (E1-51) · **(3)** las preguntas rectoras **como lista**, ~350 w, resolviendo las dos huérfanas (E1-49) · **(4)** cierre con la viabilidad teórica y **las tres limitaciones del marco** de §16.8.2, ~200 w | §16.7.2 y sus tres subsecciones (recapitulación) · la Tabla 14 como tabla · **§16.7.4 completa** (E1-44) · **§16.7.5 completa** (E1-45) · introducción de §16.8, la autoevaluación y la transición |

**Ahorro de §16.6–§16.8: ≈5.240 palabras** (algo más que las ~4.800 previstas, porque el mapa
de brechas resulta redundante y §16.8.3 también cae).

---

## 7. Acciones previas obligatorias

Estas cuatro van **antes** de aplicar cualquier poda; si se podan primero, se pierde material
que hay que reponer igual.

1. **Reponer la ecuación (1)** de §16.5.2, hoy vacía, con la notación de cuatro términos que
   usa §17.1.7 — y revisar los símbolos perdidos en §17.1.7 (*"G2A abarca , , y ."*). Es el
   contenido que PODA-06 debe conservar (E1-36).
2. **Fijar la descomposición en cuatro componentes** (E1-37), incluida la definición nueva de
   `t_preprocess`, antes de recortar la de seis.
3. **Redactar** el patrón productor/consumidor y publish/subscribe (E1-38) **antes** de
   eliminar §16.5.3.2–.3.5, o el bus de eventos y MQTT se quedan sin fundamento.
4. **Corregir las citas con letra de desambiguación falsa** —`Jeong 2022a/b`, `Shi 2016a/b`,
   `X. Wang 2020a/b`, una sola entrada cada una— dondequiera que el texto sobreviva (E1-40).

---

## 8. Orden de trabajo sugerido

1. **§15, residuales:** R1, R2, R3 (§1). Cierra la sección.
2. **§16, contradicciones y erratas duras** (una pasada, sin decisión previa): **E1-24** (las
   **dos** apariciones: §16.3.5.1 y §16.7.4) · E1-27 citas · E1-28 referencias colgadas ·
   E1-36 ecuación · E1-40 letras falsas · E1-50 tautologías.
3. **§16, la adición:** **E1-25** — el mecanismo de negación y composicionalidad en §16.3. Es
   lo más valioso del pase; hacerlo antes de podar, para que no se pierda en el ajetreo.
4. **§16, alineación:** E1-26 (las cuatro secciones de criterios) · E1-29 · E1-30 · E1-37 ·
   E1-38 · E1-39 · E1-44 · E1-45 · E1-46 · E1-47 · E1-48 · E1-49.
5. **§16, podas** con las enmiendas de §4: PODA-05…11, en ese orden.
6. **Anexo A:** E1-33 licencias · E1-34 filas faltantes · E1-35 tablas huérfanas.
7. **Delta de referencias** del capítulo entero (altas de E1-25, bajas de las podas).

**Lo que NO hay que hacer:** volver a tocar §15 más allá de R1–R3 · reaplicar E1-01…E1-23 ·
podar §16.2, §16.3 o §16.5.1 · dejar §16 más corto pero sin el fundamento de E1-25.

---

## 9. Decisiones del equipo

| ID | Decisión | Recomendación | ✔ |
|---|---|---|---|
| D-E1-9 | Tablas A.2 y A.3 quedaron sin quien las cite (E1-35). | Conservar **A.2** y citarla desde §15.3.3; **eliminar A.3**. | [ ] |
| D-E1-10 | La adición E1-25 suma ~450 palabras a un capítulo que se está podando. | Aceptar: es el fundamento del mecanismo central y rige el guardrail 6. | [ ] |
| D-E1-11 | La obligación de inscripción ante la AAIP (E1-47) queda planteada en §16 y nunca cerrada, y el proyecto sí grabó personas. | Sacarla de la tabla de brechas **y cerrarla en §17.1/§17.4** con el recaudo efectivamente tomado. **Requiere una definición del equipo, no del redactor.** | [ ] |
| D-E1-12 | Dos preguntas rectoras quedaron huérfanas (E1-49): condiciones experimentales y recaudos ético-legales. | Eliminarlas de la lista, salvo que §17.1 vaya a responderlas. Ligada a D-E1-11. | [ ] |

---

## 10. Fuentes de esta revisión

Texto de §16: `entregable/96d`. Anexo A: `entregable/96e` §19.1. Tablero original:
`ajustes/01` (`AJ-1.16`). Podas y guardrails: `ajustes/07` §4 y §9. Teoría vigente del
trabajo, contra la que `AJ-1.16` pide contrastar: `sintesis/fundamentos-teoricos.md`.
Citas nuevas verificadas contra arXiv (lista de autores exacta): **arXiv:2210.01936** (ARO) y
**arXiv:2204.03162** (Winoground). Estado de §15: `correcciones-etapa-1.md` y
`correcciones-etapa-1-pase-2.md`.
