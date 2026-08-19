# Fundamentos teóricos — entender la plataforma y sus resultados de punta a punta

- **Fecha:** 2026-08-06 · **Rol:** documento de estudio, **100% teórico-conceptual**.
- **Para qué existe:** poder explicar ante el jurado *qué* se construyó, *por qué* se
  construyó así, *cómo* se midió y *por qué* los resultados dan lo que dan. Cada
  sección desarrolla la teoría mínima y la conecta con la decisión o el resultado
  concreto del proyecto.
- **Compañeros de lectura:** los números viven en
  [`resultados-y-conclusiones.md`](resultados-y-conclusiones.md) (mismo directorio) y
  en los 4 índices de `e-ovrt_experimental-setup/results/`; las siglas, en el
  glosario (`docs/13`). Acá no hay cifras nuevas: hay **conceptos**.

> ✎ **2026-08-12 — puesto al día al mundo post-estrato-B. Leer esto antes que el cuerpo.**
> Este documento se escribió el **2026-08-06**, o sea **antes** del cierre del lote de
> internet y de la **revisión ciega del GT** (`operacion/109`–`113`). Los conceptos no se
> movieron —es lo que se esperaba de un documento teórico—, pero **tres estados sí**, y las
> tres correcciones ya están aplicadas en el cuerpo:
>
> | Decía | Vigente |
> |---|---|
> | El clip bench es de **34 clips** | **47 clips** = 32 positivos / 15 negativos / **37 episodios**, en dos bloques: **A** rodaje guionado (34) y **B** lote de obra real (13). Los denominadores de 34 siguen siendo correctos **cuando se dicen del Bloque A** |
> | **FAR/hora NO es métrica de este trabajo** | **Se mide y se reporta**, pero **no sostiene una cota** (limitación **L1**). Desde el 08-07 el banco tiene un clip de soak, así que la tasa **es computable** — y sigue faltando ~un orden de magnitud de exposición para afirmar nada operativo |
> | **L4 la levanta el lote de internet** | **L4 se precisó, no se levantó** (D-113.1, firmada): hay medición en obra real no guionada, y su aporte es **caracterizar dónde el sistema deja de ser evaluable**, no validarlo sobre obra real |
>
> Estas tres son, literalmente, tres de las siete trampas de `GUIA-REDACTORES.md` §4. Si
> encontrás una cuarta formulación vieja acá, gana el banner y hay que corregir el cuerpo.

---

## Parte I — El problema y el enfoque

### 1. El problema: condiciones de riesgo en obra, expresadas como percepción + tiempo

La seguridad en construcción tiene reglas del tipo *"ninguna persona debe permanecer
sin casco en la zona de trabajo"*. Una regla así tiene **dos mitades**:

1. **Una mitad perceptiva** — ver personas y ver (o no ver) su equipo de protección
   personal (EPP) en la imagen. Es un problema de **detección de objetos**.
2. **Una mitad temporal** — "permanecer": una condición de riesgo no es un frame, es
   un **estado que se sostiene en el tiempo**. Un casco que desaparece un frame por
   oclusión no es una infracción; una persona 10 segundos sin casco, sí.

El proyecto operacionaliza dos condiciones del catálogo del informe:
**CR-01 = persona sin casco** (severidad alta) y **CR-02 = persona sin chaleco
reflectante** (severidad media). Todo lo demás del catálogo (reglas espaciales,
zonas, maquinaria) quedó excluido con registro formal (doc 10).

La consecuencia arquitectónica de las dos mitades es la decisión más importante del
diseño: **separar el plano que percibe del plano que decide** (§10).

### 2. Detección de objetos: de vocabulario cerrado a vocabulario abierto

**Detección clásica (closed-set).** Un detector tradicional (Faster R-CNN, YOLO)
aprende un conjunto **fijo** de clases: la última capa es un clasificador con N
salidas, una por clase del dataset de entrenamiento. Detecta "casco" solo si fue
entrenado con miles de cascos anotados. Agregar una clase nueva = **re-anotar y
re-entrenar**.

**Detección open-vocabulary (OVD).** Un detector OVD reemplaza el clasificador fijo
por una **comparación entre embeddings**: el modelo proyecta cada región de la imagen
y cada **texto** (el *prompt*) a un mismo espacio vectorial, y una región "es" la
clase cuyo texto tiene mayor similitud. Las clases dejan de estar horneadas en los
pesos: **son un parámetro de entrada en lenguaje natural**. Esto viene de la línea de
modelos visión-lenguaje entrenados contrastivamente (la idea de CLIP: acercar en el
espacio de embeddings las imágenes y sus descripciones) llevada a detección
(*grounding*: no solo decir qué hay, sino **dónde** está lo que el texto nombra).

**Zero-shot** significa usar el modelo **sin ningún entrenamiento adicional** sobre
el dominio propio: se le da la imagen de obra y el texto "person. helmet. vest." y se
mide qué devuelve. Todo el trabajo experimental del proyecto es zero-shot — esa es la
pregunta de la tesis (§4).

**El trade-off estructural:** lo que se gana en flexibilidad se paga en dos monedas —
(a) **exactitud sobre clases raras o finas** (un detector cerrado entrenado con miles
de "bare heads" le gana a uno abierto que nunca vio el dominio), y (b) **costo
computacional** (procesar texto e imagen juntos es más caro que un clasificador
fijo). Los resultados del proyecto son, en buena parte, la **medición honesta de ese
trade-off**.

### 3. Los modelos concretos

**Grounding DINO (GDINO)** — el caballo de batalla del proyecto. Arquitectura
conceptual:

- Un **backbone visual** tipo transformer (Swin) extrae features multi-escala de la
  imagen; un **encoder de texto** tipo BERT procesa el *caption* (la lista de clases
  concatenada: `"person. helmet. vest."`).
- Un módulo de **fusión cross-modal** hace que las features de imagen "miren" al
  texto y viceversa (atención cruzada), de modo que la representación visual ya está
  condicionada por lo que se busca.
- La selección de queries del decoder está **guiada por el lenguaje**: el modelo
  propone regiones candidatas relevantes *para ese texto*.
- La salida son **cajas + un score de similitud contra los tokens/frases del
  caption**: umbralizar ese score da las detecciones por clase.

Variantes usadas: `tiny` (backbone chico, más rápido) y `base` (más grande, mejor en
clases difíciles). El sufijo `-560` es la **resolución de entrada** (560 px en vez de
800): menos píxeles ⇒ menos tokens visuales ⇒ menos cómputo. El hallazgo de la Fase S
fue que 560 px da −24% de latencia con igual o mejor mAP — la información que las
condiciones necesitan sobrevive a la resolución menor.

**YOLOE** — el otro polo del trade-off: una familia YOLO (one-stage, tiempo real) con
vocabulario abierto vía embeddings de texto pre-computables (y prompts visuales). Al
poder pre-computar el embedding de las clases, en inferencia corre casi como un YOLO
cerrado (~43 ms). El resultado del proyecto: es **rápido pero ciego a `bare_head`**
(AP 0,000), la clase que sostiene CR-01 — el ejemplo perfecto de que "entra en el
presupuesto de latencia" no sirve si no ve la condición (F-RT2).

**MM-Grounding-DINO** — reimplementación de GDINO del ecosistema MMDetection; quedó
descartada en dos pasos (tiny con cajas degeneradas; large con mAP 0,017).

**Por qué importa la elección por *variante* y no solo por familia:** el proyecto no
compara "GDINO vs YOLO" en abstracto; congela una **combinación** concreta (modelo +
resolución + prompt set + umbrales) y la mide. El "campeón" (`gdino-tiny-560`) y el
"especialista" (`gdino-base-560`) son variantes de la misma familia con roles
distintos medidos por estrato.

### 4. Qué defiende la tesis (y qué NO)

**La tesis NO es "OVD detecta mejor que un modelo cerrado".** Esa afirmación es
indefendible (un detector cerrado bien entrenado en el dominio gana en su clase) y no
es la pregunta. La tesis es:

> Una **plataforma** donde las condiciones de riesgo se expresan **en lenguaje**
> permite (a) **medir** qué se logra hoy sin entrenar, con qué latencia y bajo qué
> límites — declarados, no disimulados —, y (b) **extender** el sistema a condiciones
> nuevas por configuración, en minutos, sin re-anotar ni re-entrenar.

De ahí los dos tipos de resultado: los **números del banco** (qué se logra hoy: F1
0,789 núcleo / 0,930 con identidad) y el **número de extensibilidad** (A1: una clase
jamás configurada, con AP mejor que el agregado, en 9 minutos y 48 líneas de YAML —
con el contrapeso F-94.1: la palabra hay que validarla contra la taxonomía). El
contraste entre combinaciones **es** el experimento; ningún número es una nota de
aprobación.

---

## Parte II — Del píxel a la alerta: la cadena conceptual

### 5. Los tres niveles de medición

El error clásico es medir todo junto. El proyecto separa **tres niveles**, cada uno
con su GT y su métrica, porque responden preguntas distintas:

| Nivel | Unidad | Pregunta | Métrica | Banco |
|---|---|---|---|---|
| **Imagen** (percepción espacial) | caja | ¿el detector ve personas/EPP? | AP@0.5, mAP50, recall | `bench_v3` (6.477 imgs) |
| **Persona** (Nivel A) | persona-estado | ¿esta persona está "sin casco"? | P/R/F1 por violador | `person_gt` (atributos `has_helmet`/`has_vest`) |
| **Alerta** (Nivel B) | episodio temporal | ¿la plataforma alertó cuando y donde debía? | recall/precision/F1 de episodios, t_alert, TTFD, SDR | clip bench (**47 clips**, GT temporal humano: 34 del rodaje + 13 de obra real) |

La lógica de la cadena: un modelo puede ver bien (nivel imagen) y aun así razonar mal
el estado (nivel persona); y un estado bien razonado puede producir malas alertas si
el motor temporal se equivoca (nivel alerta). **Cada capa se aísla para poder
atribuir el error** — y la atribución es lo que hace defendibles las conclusiones
(p. ej.: la ganancia de G1 es 100% del motor porque las detecciones son idénticas).

### 6. El prompt como interfaz: las estrategias de formulación

En OVD el prompt no es cosmético: **es la especificación ejecutable de la
condición**. El experimento D1 (la única dimensión empírica del tablero de
decisiones) compara dos filosofías:

- **E-IND (indirecta):** pedirle al modelo solo **evidencia positiva** — `person`,
  `helmet`, `vest` — y razonar la **ausencia** por geometría (§7). El modelo hace lo
  que mejor sabe (detectar cosas que existen); la negación la pone el sistema.
- **E-DIR (directa):** pedirle la **infracción como frase** — "person without
  helmet", "worker with bare head" — en tres ejes de formulación: negación
  sintáctica, especificidad, estado observable.
- **E-HYB (híbrida):** correr ambas y fusionar (unión `or` / corroboración `and`,
  con gating por persona).

**Por qué era esperable que E-DIR sufriera (y por qué había que medirlo igual):** los
encoders de texto entrenados contrastivamente tienden a comportarse como "bolsa de
palabras": la representación de *"person **without** helmet"* queda dominada por
"person" y "helmet", y el modificador de negación pesa poco. El resultado empírico
lo confirmó con mecanismo: la falla dominante de E-DIR es la **ceguera al atributo**
(54% de sus FP) — devuelve cajas de "person without helmet" sobre personas **con**
casco. No es que no vea: es que **la frase no significa para el modelo lo que
significa para nosotros**.

Dos matices que los resultados obligan a sostener:

- **E-DIR no es un detector, pero es un recuperador (F-83.6):** recupera ~18,5% de lo
  que E-IND no ve, a costo de precisión. Por eso la fusión era una hipótesis
  razonable — y por eso su refutación (F-87.2, §20) es un hallazgo y no un descuido.
- **Lo que manda es la formulación, no el mecanismo (F-88.3):** la etiqueta corta
  (`helmet`) activa mejor el encoder que la frase compuesta ("safety helmet") — de
  ahí el prompt set congelado `cr01_cr02_v2_short`. Y B1 mostró que hasta el
  vocabulario "nativo" (`bare_head` como clase directa, que `shel5k` anota) rinde
  menos que la ausencia espacial sobre las mismas detecciones.

### 7. Inferencia espacial de ausencia: cómo se razona "sin casco" sin pedir "sin casco"

E-IND operacionalizada (evaluador `spatial_absence` del control-plane): para cada
**persona** detectada se define una **región anatómica esperada** del EPP, por
proporciones de la caja de la persona:

- CR-01: región `upper_body` — la franja superior de la caja (0–45% del alto, con
  margen lateral del 12%): ahí debería haber un `helmet`.
- CR-02: región `torso` — la franja media (25–85% del alto, margen 8%): ahí debería
  haber un `vest`.

La regla: si hay una persona con confianza ≥0,35 y área ≥400 px², y **ninguna**
detección del EPP con confianza ≥0,25 cae en su región ⇒ esa persona está **en
evidencia de infracción** en ese frame. Los umbrales bajos para el EPP son
deliberados: para *descartar* una infracción alcanza evidencia débil del casco (es
mejor perdonar de más a nivel frame — el filtro fuerte lo pone el tiempo, §8).

Este razonamiento geométrico es la mitad "sistema" de E-IND: convierte detecciones
(qué hay y dónde) en **estados por frame** (quién está sin qué). Es simple a
propósito: 2D, por proporciones, sin pose — sus límites (personas agachadas,
oclusiones) los absorbe la capa temporal o quedan declarados.

### 8. El motor de patrones temporal: la histéresis como filtro de verdad

El estado por frame es ruidoso: la percepción **parpadea** (un chaleco se detecta 1
de cada 6 frames; un casco desaparece al agacharse). El motor de patrones convierte
ese parpadeo en decisiones estables con una **máquina de estados con histéresis**,
por patrón y por clave de granularidad:

```
inactive → candidate → confirmed → sustained → resolved
```

- **inactive → candidate:** aparece evidencia de infracción.
- **candidate → confirmed:** la evidencia se **sostiene** `confirm_after_ms`
  (CR-01: 4.000 ms; CR-02: 7.000 ms — más tiempo porque la percepción de chaleco es
  más ruidosa). Al confirmar, se **emite la alerta**.
- **confirmed/sustained → resolved:** la evidencia **falta** durante
  `resolve_after_ms` (2.000/3.000 ms). Ojo con la asimetría: no hace falta evidencia
  continua para sostener — hace falta que los **huecos** sean menores que la ventana
  de resolución.

Esa asimetría es la clave teórica de dos resultados:

- **F-81.1 (el rescate):** una percepción con SDR 0,281 (evidencia en ~1 de cada 6
  frames) igual confirma 7/7 episodios de CR-02, porque los huecos entre detecciones
  son más cortos que `resolve_after_ms`. La histéresis **integra** evidencia
  intermitente. El precio es tiempo: t_alert sube.
- **F-RT2 (el límite):** el mismo mecanismo exige que los huecos sean < ventana. Un
  modelo rápido pero con detecciones muy espaciadas (YOLOE) no llega a confirmar:
  entra en presupuesto de latencia y no sirve para la condición.

**Decisiones de frontera que hay que poder explicar:**

- **El motor emite en CADA confirmación (ADR-011).** Si una condición se resuelve y
  reaparece, hay una alerta nueva (`re_alert`). La supresión/cooldown/agrupación es
  **política de notificación** del distribuidor —no del motor—; por eso el evaluador
  cuenta los `re_alerts` aparte y **no** los castiga como FP. El distribuidor aplica y
  registra esa política en el tramo mínimo verificado por spec 45.
- **Sin memoria de cobertura bajo G0 (ADR-012):** recordar "esta persona tenía casco
  hace 3 s" exige identidad; bajo escena no la hay, y la histéresis subsume el
  parpadeo. Decisión falsable por test — la falsación se corrió y quedó superada.

### 9. Granularidad: por qué "por sujeto" cambia todo sin cambiar la percepción

**G0 (escena):** el estado del patrón se indexa por `(pattern_id, source_id)` — hay
**un solo** CR-01 por cámara. **G1 (sujeto):** se indexa además por `subject_key` —
hay un CR-01 **por persona**.

El tracker que sostiene G1 es deliberadamente simple: **asociación por IoU** frame a
frame (una detección de persona continúa el track con el que más se solapa;
expiración si desaparece). Se implementó como **decorador de la fuente en el
control-plane** (adenda ADR-002): lee las detecciones, les agrega `track_id`, y el
motor ni se entera — por eso G1 corre sobre **exactamente las mismas detecciones**
que G0 (bit a bit), sin GPU.

**El mecanismo de la mejora (F-89.1/89.2)** — esto es lo que hay que saber explicar,
porque es el mejor resultado del banco (+0,141 de F1, 100% del motor):

- Bajo escena, el estado es **compartido**: la persona A (con casco) y la persona B
  (sin casco) alimentan el mismo acumulador. La evidencia de B puede confirmar una
  alerta "de la escena" que el matching temporal atribuye mal (alertas **cruzadas de
  condición**), y la evidencia del pre-roll (antes del episodio GT) puede dejar el
  acumulador "caliente" y confirmar **prematuro**.
- Bajo sujeto, cada persona tiene su acumulador: la evidencia de B confirma **sobre
  B**, alineada con su episodio. Las prematuras de pre-roll caen de 5 a 1; P7 (el
  escenario multi-persona) pasa de 0,400 a 1,000.

**Por qué las métricas MOT "no aplican" y eso es correcto (E-10):** MOTA/IDF1 miden
calidad de **identidades** contra un GT de identidades persistentes — que no existe
en el banco. Y no haría falta: como las detecciones son idénticas, la ganancia de G1
**no es de percepción ni de tracking fino**: es de **atribución de estado**, y se
expresa (y se mide) en alertas. Ese es el fundamento *medido* de la exclusión, no una
excusa.

---

## Parte III — La plataforma como sistema

### 10. Tres servicios HTTP config-driven, eventos normalizados

**Arquitectura:** tres servicios HTTP config-driven — los dos planos más el módulo
de distribución (ADR-019/020).

- **media-plane (:8080)** — el plano de medios: ingesta de fuentes (carpeta de
  imágenes, archivo de video, RTSP, OAK-D), normalización, inferencia OVD (el modelo
  se carga una vez al arranque), y emisión de **eventos normalizados**
  `media.detection.v1` (cajas, clases, scores, `unit_id`, timestamps). Escribe
  `runs/<id>/detections.jsonl`.
- **control-plane (:8081)** — el plano de control: consume esos eventos, corre el
  motor de patrones (§8), emite alertas, y trae el **evaluador** contra GT.
- **distribución (:8082)** — el módulo de salida: consume las **alertas confirmadas**
  y las entrega hacia afuera por **MQTT (QoS 1)**, con un **ledger de idempotencia**
  para que un reintento nunca duplique una notificación. Escribe
  `notifications.jsonl` y su `distribution_summary.json`.

Las decisiones arquitectónicas que lo gobiernan (DA-01/02/03): separar percepción de
decisión, publicar la evidencia como **eventos normalizados** (el motor no sabe qué
modelo corre — puede cambiarse el detector sin tocar una línea del motor), y separar
**transporte** de **persistencia**: el bus mueve, el **JSONL persiste y es la fuente
de verdad**.

**Dos patrones de acople, y solo dos.** (1) **HTTP config-driven**: los tres
servicios se operan igual —`POST /api/runs`, estado por polling— y la webconsole y
el runner son **clientes de los tres**, nunca del bus. (2) **Bus ZeroMQ PUB/SUB**:
`:5557` mueve las detecciones (media → control) y `:5558` las alertas confirmadas
(control → distribución); ambos exigen suscribirse **antes** de disparar. MQTT no es
un tercer patrón: es la **salida** de la plataforma hacia el receptor, no un acople
interno.

**Config-driven:** no hay rutas ni umbrales hardcodeados. Una corrida se define por
YAMLs versionados (modelo+resolución, prompt set, pattern set, fuente); los catálogos
de experimento (prompt sets congelados, manifiestos) viven en `experimental-setup`,
que también trae el **runner** (orquesta los servicios por HTTP en el orden correcto)
y la **webconsole** (React + BFF FastAPI). Esto es lo que vuelve **reproducible por
configuración** cada campaña, y lo que hace barato el experimento A1 (una condición
nueva = un YAML).

### 11. DBE vs EBE: los dos escenarios de evaluación

- **DBE (Dataset-Based Evaluation, offline):** el media-plane escribe
  `detections.jsonl`; el control-plane lo **relee** (replay). Determinista,
  re-corrible infinitas veces, ideal para comparar combinaciones (todas las campañas
  del banco son DBE a 30 fps de evidencia).
- **EBE (Environment-Based Evaluation, live):** acople por **bus ZeroMQ PUB/SUB con
  msgpack** (envelope `bus.envelope.v1`). Conceptos clave:
  - **`seq` monotónico por publicador**, que se incrementa **aunque el envío se
    descarte**: así un hueco de `seq` en el consumidor delata pérdida — se cuenta
    como `bus_dropped_events` y degrada la corrida, nunca se silencia. (Teoría:
    PUB/SUB no tiene entrega garantizada; la integridad no se supone, se
    **instrumenta**.)
  - **PUB/SUB pierde lo publicado antes de suscribirse** ⇒ orden de arranque no
    negociable: primero el control-plane (su `201` implica suscripto), después el
    media-plane.
  - **Corrida 1:1** (ADR-007): un run de control por run de media, cierre por
    `run_finished`.
- **El puente entre ambos:** toda corrida live es **re-evaluable offline** — el JSONL
  que produjo el camino live, releído por replay, da artefactos **byte-idénticos**
  (verificado con un gate que falla si se muta 1 píxel). Esto es lo que permite decir
  que los números DBE hablan del camino live, con la densidad de evidencia como la
  diferencia a medir (§17).

### 12. Reproducibilidad como diseño, no como promesa

Cadena de trazabilidad de cualquier número: `metrics.json` (forma única
`clip_campaign_metrics.v1`) ← `evals/` por clip ← alertas del run ← `campaign.yaml`
(la combinación declarada + **sha256 del prompt set congelado y del manifest del
banco**) ← `provenance.json` (apunta a los runs del media-plane, que no se copian —
DA-03). Congelar con hash y verificar con script (`96-verificar-indices.py`) es lo
que convierte "confía en mí" en "corré esto".

---

## Parte IV — Cómo se mide (la teoría de las métricas)

### 13. Nivel imagen: IoU, AP y por qué el agregado engaña

- **IoU (Intersection over Union):** solapamiento entre caja predicha y caja GT
  (área de intersección / área de unión). El umbral estándar **IoU ≥ 0,5** define
  qué cuenta como acierto (por eso "AP@0.5").
- **Matching:** cada predicción se asigna a lo sumo a un GT (greedy por score, 1:1);
  predicción sin GT = FP, GT sin predicción = FN.
- **Precision / Recall:** P = TP/(TP+FP) — de lo que dije, cuánto era cierto;
  R = TP/(TP+FN) — de lo que había, cuánto encontré. Todo detector intercambia una
  por otra moviendo el umbral de confianza.
- **AP (Average Precision):** el área bajo la curva precision-recall al barrer el
  umbral — resume el trade-off completo en un número por clase. **mAP50** = promedio
  de AP@0.5 entre clases.
- **Estratificación (regla L5):** `bench_v3` junta 3 fuentes con estilos y
  anotaciones distintas, y el 77% de las imágenes es de una sola (`shel5k`). Un
  agregado puede mejorar mientras el estrato que importa empeora (la lógica de la
  paradoja de Simpson). Por eso la regla no negociable: **reportar por estrato,
  siempre** — y por eso "campeón robusto a la fuente" significa "gana en las dos
  escalas", no "gana en el promedio".

### 14. Nivel persona: calibración/test y por qué se parte la muestra

Nivel A pregunta por el **estado** ("esta persona está sin casco"), que exige elegir
umbrales de confianza. Elegir el umbral y medir **sobre los mismos datos** infla el
resultado (el umbral se sobreajusta a la muestra). Protocolo del proyecto:
**calibrar en la mitad A, medir solo en la mitad B** — la forma mínima de un
train/test split, aplicada a hiperparámetros de decisión. Los IC por bootstrap (§16)
acompañan cada F1; "IC no solapados" entre E-IND y E-DIR en `shel5k` es lo que
permite hablar de diferencia real y no de ruido.

### 15. Nivel alerta: episodios, matching temporal y las métricas de la plataforma

El GT temporal define **episodios**: intervalos [inicio, fin] por condición dentro de
cada clip ("de 00:05 a 00:31 la persona está sin casco"). El evaluador matchea
alertas contra episodios (misma fuente — convención `source_id = clip_id` —, misma
condición, dentro de la ventana derivada de la persistencia nominal):

- **Recall (micro, por episodio):** episodios con alerta / episodios evaluables.
- **Precision:** alertas que corresponden a un episodio / alertas totales.
- **t_alert:** cuánto tardó el sistema desde que la condición se sostiene hasta
  confirmar. Su valor **ideal** no es 0: es el umbral de la política (4.000/7.000
  ms) — un t_alert de 4.100 ms es un motor puntual, no lento.
- **TTFD:** cuánto tardó la **percepción** en ver la primera evidencia del episodio.
  Separa el costo del detector (TTFD) del costo de la política (t_alert).
- **SDR:** fracción del episodio cubierta por detecciones — la densidad de la
  percepción. (Con la trampa F-96.6: su cálculo funde huecos menores al paso
  nominal, así que **no se compara entre cadencias**.)
- **Censura:** un episodio más corto que la ventana necesaria para confirmar
  (`clip_too_short_for_t_alert_window`) **no puede** medirse — sale del denominador
  con causa, en vez de contarse como fallo. De ahí el denominador citable: **34
  evaluables sobre 35 en el bloque del rodaje** (el calificador no es opcional: 34 es el
  Bloque A, no el banco). (Teoría: análisis de datos censurados — excluir con registro
  es honesto; contar como miss sería sesgar en contra; contar como hit, a favor.)
- **Negativos:** los clips de cumplimiento no entran a P/R/F1 (no hay episodios que
  recuperar) — su métrica son los **FP en negativos**, el control de falsas alarmas.
  Promediar su "F1" hundiría el agregado contando aciertos como catástrofes (F-EV1).

**Por qué FAR/hora se reporta pero no sostiene una cota (limitación L1):** una tasa de
falsas alarmas por hora es estadística de **eventos raros**: para afirmar
"FAR ≤ 1/hora" observando 0 eventos hace falta una exposición de ~3 horas de
cumplimiento anotado (regla de 3: con 0 eventos en T horas, el IC 95% superior de la
tasa es ≈3/T). El banco junta 0,10–0,26 h ⇒ cualquier cota honesta (11–30 FA/h) no
sostiene ninguna afirmación operativa. Por eso el peso lo lleva el **control comparativo
de negativos**, que sí discrimina entre combinaciones (0 FP vs 2–3 FP sobre los mismos
4 clips).

> ✎ **2026-08-12 — precisión, y no es cosmética.** La formulación anterior decía que
> *"FAR/hora NO es métrica de este trabajo"*, y de ahí salió una de las siete trampas de la
> guía de redactores. **La tasa se mide y se reporta**: desde el 08-07 el banco tiene un
> clip de soak (`v06_c01`, 0,1027 h), así que es computable. Lo que no cambia es la
> conclusión —**no sostiene una cota**, faltan casi dos órdenes de magnitud de exposición—,
> y ese es el contenido de **L1**. Al citarla nunca va la tasa desnuda: va el conteo de
> falsos positivos con su duración observada, y la tasa horaria como derivada
> (`GUIA-REDACTORES` §3).

### 16. La estadística de las comparaciones: bootstrap pareado e IC

Comparar dos campañas por su F1 global esconde que ambas corrieron **sobre los mismos
34 clips del Bloque A** — y que los clips varían muchísimo en dificultad. El método:

- **Bootstrap pareado por clip:** remuestrear clips con reposición (10.000 veces),
  recalculando el delta de F1 **entre las dos campañas sobre la misma muestra**. El
  pareo cancela la dificultad del clip (el factor común) y deja la diferencia entre
  combinaciones.
- **IC 95% que excluye el cero** ⇒ la diferencia sobrevive al remuestreo ⇒ se puede
  afirmar. **IC que cruza el cero** ⇒ estimación puntual: se reporta como
  observación consistente, **no** como hallazgo.
- **La regla de degradación (doc 98):** cuando la estimación era vistosa pero el IC
  cruzaba el cero, la afirmación se degradó (caso testigo: "G1 a 4,29 fps supera a
  T1 a 30 fps"). Esta regla es la espina dorsal de la **escala AF**: no todo lo
  medido tiene el mismo estatuto — establecida / direccional (n chico) / tendencia
  con mecanismo / no cerrada / limitación — y decirlo explícitamente es más fuerte
  ante un tribunal que aplanarlo.

**Pre-registro:** los criterios de decisión del eje D1 (el gate de Nivel A, el veto
de precisión < 0,5 a Nivel B, el umbral de adopción de la fusión) se fijaron **antes
de correr** (`nucleo/04` §8). Eso convierte "descartamos E-DIR" de opinión en
resultado, y hace que la refutación de la predicción propia (E-HYB-or) sume
credibilidad en vez de restarla.

---

## Parte V — El tiempo real

### 17. Densidad de evidencia: el puente DBE↔EBE

El banco corre offline a **30 fps de evidencia**; el camino live entrega **1,16–4,42
fps** (el resto de los frames se descarta porque la inferencia no llega). ¿Cuánto de
la calidad medida sobrevive a esa dieta? El experimento: re-correr el banco
**decimando** las detecciones con un `stride` (tomar 1 de cada 7 ≈ 4,29 fps; 1 de
cada 26 ≈ 1,15 fps) — la variable única es la cadencia.

**La objeción teórica y su cierre (doc 101):** el decimado regular es un muestreo
determinista; el descarte real del live es **irregular** (jitter — se midió su
coeficiente de variación: CV 0,22–0,36). ¿Invalida eso el proxy? Se verificó
empíricamente: re-correr con decimado **empírico** (huecos muestreados de la
distribución real, 3 semillas) no produce ningún contraste detectable contra el
regular (12/12 IC cruzan el cero) y la ganancia de la identidad conserva el signo en
6/6 realizaciones. Por eso la formulación obligatoria de AF-1 dice "bajo decimado
regular, conservando la dirección bajo el descarte irregular medido".

**Los dos artefactos de instrumento que había que cazar antes de reportar:**

- **F-96.6:** el SDR "mejora" al bajar la densidad — 100% artefacto (el cálculo funde
  huecos ≤ paso nominal, y el paso crece con el stride). Regla: SDR no se compara
  entre cadencias.
- **F-96.5 (sesgo de supervivencia):** el t_alert agregado parecía no empeorar al
  bajar densidad — porque los episodios **lentos mueren como missed** y salen del
  promedio justo cuando el costo sube. Entre supervivientes comunes, el costo real es
  +0,7 a +1,3 s. Regla: t_alert no se compara entre densidades sin control de
  supervivencia.

### 18. Latencia: qué mide G2A y qué no (F-101.8)

**G2A ("glass-to-algorithm")** = tiempo desde la captura hasta el resultado
algorítmico, con presupuesto de diseño 50–250 ms. El hallazgo fino que el informe
debe declarar: la estampa de "captura" del pipeline se toma en el **dequeue** (cuando
el frame sale de la cola interna), **no en el fotón**. Entre el mundo físico y esa
estampa hay un tramo (`capture_to_host`: driver, red, cola) de 202–217 ms medianos en
el rodaje — y hasta 1,6 s con el host degradado. Se validó **contra el mundo físico**
con una claqueta (evento audiovisual sincronizado + reloj externo): el ancla física
tono→fotón→estampa dio +1.066 ms en la toma medida. Moral teórica: toda cadena de
latencia se cita **declarando desde dónde se mide**; "vidrio→alerta = capture_to_host
+ G2A + política".

También se verificó la **política contra reloj externo**: confirmación a 4.142 ms con
umbral de 4.000 (el motor es puntual: el exceso es la cadencia de muestreo), y el
residuo entre relojes fue de 4 ms.

### 19. El techo de fps: por qué era el GIL y no la GPU ni el calor

El live entregaba pocos fps con la GPU subutilizada. Diagnóstico por descarte
instrumentado (docs 73/74):

- **No es la GPU:** triple verificación (CUDA activo, VRAM del proceso, `dmon` con
  SM 6–41%).
- **No es térmico:** la hipótesis del "correlato de temperatura" se refutó con los
  propios datos (corridas lentas y rápidas intercaladas en el tiempo; lo que separa
  poblaciones es la **fuente**: archivo vs cámara).
- **Es contención de GIL (F-RT3):** en CPython un solo hilo ejecuta bytecode a la
  vez. La inferencia libera el GIL mientras corre en CUDA, pero todo el pre/post
  procesamiento en Python (decodificación, conversiones de imagen, serialización)
  compite por él en un proceso con productor + consumidor + publicador. La firma:
  perfil "bursty" con GPU ociosa.
- **La palanca que lo demuestra (F-RT5):** sacar un round-trip PIL innecesario del
  productor dio +18% de fps y −14,4% de latencia (p=0,0195, 11 pares pareados).
  Lección metodológica: palancas <20% exigen ~10 pares intra-campaña para
  distinguirse de la deriva (±150 ms) — y el profiler (py-spy) infla 2× en WSL, así
  que se mide con el instrumento apagado.

El complemento de borde: el prefilter **EN-2** corre un detector de personas liviano
**dentro de la cámara** (OAK-D) y descarta on-device el 87% de los frames sin
personas — menos presión sobre el host sin tocar el modelo principal. Opcional,
apagado por defecto, fail-open (si falla, deja pasar todo: pierde eficiencia, no
evidencia).

---

## Parte VI — Leer los resultados: los mecanismos, traducidos

La fuerza del trabajo no es que los números sean altos — es que **cada falla y cada
ganancia tiene mecanismo identificado**. Los que hay que poder contar de memoria:

| Hallazgo | El mecanismo, en una frase |
|---|---|
| **F-81.1** (histéresis rescata) | La máquina de estados integra evidencia intermitente: mientras los huecos < `resolve_after_ms`, el episodio no se cae — se paga en t_alert. |
| **F-85.3** (doble filo) | El mismo integrador que rescata evidencia verdadera intermitente también **acumula evidencia falsa** intermitente: la histéresis amplifica lo que le den (D1: 35 FP). |
| **F-87.2** (la unión no es monótona) | En un clasificador estático, unir evidencia solo puede subir el recall. En un **motor temporal**, evidencia extra más temprana **adelanta** la confirmación — y una alerta adelantada cae fuera de su ventana de matching: cuenta como FP *y* deja el episodio sin alerta. Más evidencia ⇒ menos recall. Es el resultado más contraintuitivo del banco y por eso se pre-registró la predicción contraria. |
| **F-88.1** (costo del caption) | Cada clase extra en el caption compite por la atención del encoder: una palabra más costó 0,082 de F1 con todo lo demás igual. El prompt es un presupuesto, no una lista de deseos. |
| **F-88.3** (formulación > mecanismo) | Ordena el eje la *forma* del texto (etiqueta corta > frase negada), no la vía (directa/indirecta/nativa). |
| **F-89.1/89.2** (identidad) | Separar acumuladores por sujeto elimina las alertas cruzadas y las prematuras de pre-roll: misma percepción, mejor atribución (§9). |
| **F-94.1** (validar la palabra) | La clase nueva rinde solo si la palabra significa en el modelo lo que significa en la taxonomía del despliegue (`vehicle` murió por solapamiento semántico con `machinery`; `gloves` detectó 252 veces cualquier cosa menos guantes). |
| **F-96.1** (redistribución oculta) | Un agregado plano puede esconder que unos escenarios caen y otros suben: el promedio no es el fenómeno. |
| **F-RT1** (sobre-marca de `vest`) | El modelo "ve chalecos" en texturas de alta visibilidad (campera a franjas) ⇒ suprime CR-02 en silencio. La falsa evidencia positiva es más peligrosa que la ausencia: apaga la alarma. |
| **F-83.6** (recuperador) | Una vía con precisión inservible puede aportar recall complementario — por eso se probó la fusión (y falló por F-87.2, no porque la idea fuera absurda). |

## Parte VII — El cierre metodológico

### 21. Alcance por registro, exclusiones con causa, limitaciones con código

Tres instrumentos que conviene poder explicar como *metodología* (no como burocracia):

- **ADRs (Architecture Decision Records):** cada decisión con su contexto,
  alternativas y consecuencias; no se re-litigan sin causa registrada. Dos series:
  ADR-001…015 del proyecto y ADR-0001…0013 internos del control-plane (citar siempre
  la serie). **ADR-015** es el cierre: registra que el alcance **creció** con
  evidencia (G1 de demostrativa a capacidad medida; E-HYB-or ejercida y refutada),
  cierra la puerta a capacidad nueva y declara MQTT no implementada — exclusión
  ejercida, no deuda.
- **Exclusiones E-01…E-13 (doc 10):** cada cosa que NO se hizo, con la regla del
  informe que la ampara, su rastro y su frase de declaración. La declaración clave:
  las decisiones se tomaron **antes** de los resultados — eso las vuelve metodología
  y no excusa.
- **Limitaciones L1–L8:** con código y citables ("limitación L4"), porque una
  limitación declarada es un resultado sobre el instrumento, no una vergüenza. Las
  dos que más preguntas atraen: **L4** (un solo bloque guionado — ✎ el lote de obra real
  la **precisó, no la levantó**: aporta medición no guionada y, sobre todo, caracteriza
  **dónde el sistema deja de ser evaluable**) y **L2** (sin doble anotación/kappa —
  decisión declarada de presupuesto de anotación).

### 22. Mapa mental para la defensa (una frase por eslabón)

1. **Qué construimos:** una plataforma de dos planos donde la condición de riesgo es
   *configuración en lenguaje* — percibir (media-plane) y decidir en el tiempo
   (control-plane), acoplados por eventos.
2. **Qué preguntamos:** cuánto rinde eso HOY sin entrenar, y qué aporta la
   plataforma alrededor del modelo.
3. **Qué encontramos:** el detector sostiene CR-01 y no CR-02 (asimetría
   estructural); la formulación indirecta gana con veto pre-registrado; **la palanca
   más grande no fue el modelo sino el motor** (identidad: 0,789→0,930 con las
   mismas detecciones); y esa ganancia es la única que sobrevive con significancia a
   la densidad del tiempo real.
4. **Qué declaramos:** los límites con código (L1–L8), las exclusiones con causa, y
   una escala explícita de cuánta fuerza tiene cada afirmación (AF-1…AF-11).
5. **Qué demostramos de extensibilidad:** una condición nueva cuesta minutos y un
   YAML — y validar la palabra contra la taxonomía es parte del costo (F-94.1).

**Las preguntas hostiles previsibles y su eje de respuesta:** *"¿por qué no
fine-tuning?"* → la pregunta parte de una premisa vieja: el fine-tuning **es una rama
experimental del proyecto y se ejerce como jornada completa** (✎ 2026-08-11, ADR-017)
— condicionada desde el diseño por la regla metodológica (Tabla 37: baseline primero)
y por datos/protocolo, no por falta de cómputo ni por tiempo. F-100.1, freeze/smoke técnico,
dual gate y serving real ya quedaron resueltos; el estado vigente es NO-GO T1 full por
~~D-FT-08/T-FT-005,~~ evaluación T-FT-031 y baseline 26s T-FT-032. La procedencia
T-FT-023 quedó CERRADA el 2026-08-13 (snapshot tar `639e60df…`). ✎ **2026-08-15:
D-FT-08/T-FT-005, D-FT-12 y D-FT-13 firmadas por el usuario, y T-FT-031/T-FT-032 cerradas
la misma jornada** con la baseline YOLOE-26s one-shot ejecutada (doc 120) — el NO-GO quedó
en su último eslabón: `full-authorization.json` + `RUN` manual. La
baseline zero-shot era el prerequisito y ES la pregunta central; los resultados y
limitaciones de la jornada se documentan con su estado a la entrega. *"¿un YOLO
entrenado no haría esto mejor?"* → en su clase sí; la tesis mide otra cosa:
condiciones en lenguaje, extensibilidad y el aporte de la capa temporal/identidad,
que es agnóstica al detector. *"¿cuál es el FAR/hora?"* → se mide y se reporta, pero
**no sostiene una cota**: afirmarla sin ~3 h de cumplimiento anotado sería fabricarla.
Está declarada como limitación L1, y el peso lo lleva el control comparativo de negativos. *"¿el tracker no necesita métricas MOT?"* →
no hay GT de identidades y la ganancia es de atribución de alertas — F-89.1 lo
fundamenta con detecciones bit a bit idénticas.

---

**Ruta de profundización, en orden:** este doc → `resultados-y-conclusiones.md`
(los números) → `results/index.md` y sus 4 índices (las tablas con artefacto) →
`operacion/98` (la escala AF) → los docs de campaña (81, 83–89, 96, 101) para cada
mecanismo → `nucleo/04`/`12` (el pre-registro) y `nucleo/09` (la defensa de OVD).
