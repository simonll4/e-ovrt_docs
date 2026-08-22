# E-OVRT-VDP - paquete de etapa 1

> Generado el 2026-08-22. Etapa 1: secciones 15 y 16, y Anexo A.

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

- **Etapa activa:** 1 - Etapa 1: secciones 15 y 16, y Anexo A.
- Este archivo contiene el texto vigente que se modifica y sus insumos de ajuste.
- No se trasladan resultados propios hacia secciones cronologicamente anteriores.
- Nombre propio de esta etapa (01-etapa-1-activa.md): regenerarla no pisa el paquete de ninguna otra etapa.

---

## Fuente: `docs/informe/entregable/96c-informe-v11-estado-del-arte.md`

> SHA-256 del bloque: `f618796da1aa4d49104725653785c9ef722e62f0d208ba89a4ff5e7e7950ed27`  
> Seleccion: documento completo.

# 96c — Texto extraído del informe v1.1: §15 Estado del Arte

> **Extracción derivada (2026-07-18)** del `.docx`
> `informe/entregable/E-OVRT-VDP_v1.1_05062026-sin-indice.docx`, **solo para búsqueda y cita**
> (mismo estatuto que el doc 90): al editar, se edita el `.docx`/Google Docs, nunca
> este archivo. Tablas y figuras pueden haber perdido formato; las figuras no se
> extraen. **La §17.3 embebida en el docx NO se incluye en esta serie: está
> desactualizada** — la Etapa 3 vigente es el doc 90 (extracción del standalone).
> Partición completa: 96a (frontmatter+intro+objetivos+plan), 96b (§17.1
> consolidación metodológica — el protocolo), 96c (estado del arte), 96d (marco
> teórico), 96e (cierre+anexos+referencias).

---

## 15. Estado del Arte

El estado del arte reúne los antecedentes técnicos y metodológicos necesarios para contextualizar el desarrollo de una plataforma experimental de detección open-vocabulary en video en tiempo real. Su propósito es revisar los enfoques, modelos y arquitecturas que permiten comprender el alcance actual de la detección visual guiada por lenguaje natural, así como sus limitaciones cuando se la traslada a escenarios dinámicos, con restricciones temporales y requerimientos de seguridad laboral.


### 15.1. Alcance del estado del arte y propósito de la fundamentación teórica

El análisis se organiza en torno a los dominios que condicionan la viabilidad del sistema: la detección open-vocabulary como alternativa frente a los enfoques de vocabulario cerrado, los modelos visión-lenguaje y sus principales familias arquitectónicas, el seguimiento multiobjeto como mecanismo de persistencia temporal, y las tecnologías de transmisión y procesamiento de vídeo necesarias para operar con baja latencia. De manera complementaria, se consideran las brechas que aparecen al aplicar estas tecnologías al dominio de la construcción civil, especialmente en relación con la detección de condiciones de riesgo, la estabilidad temporal de las predicciones, la sensibilidad a los prompts, la disponibilidad de datos y la evaluación de alertas en tiempo real.

Esta revisión no tiene por finalidad elegir de forma aislada un modelo, protocolo o herramienta, sino establecer un marco crítico para distinguir qué capacidades se encuentran suficientemente maduras, qué aspectos requieren validación experimental y qué limitaciones deben ser consideradas durante el diseño e implementación del prototipo. A partir de esta base se derivan criterios para la selección tecnológica, la definición del alcance experimental y la construcción posterior del protocolo de evaluación.


### 15.2. Detección open-vocabulary: modelos, paradigmas y brechas del estado del arte


#### 15.2.1. Paradigmas Arquitectónicos y Modelos Representativos

El estado del arte en OVD no constituye una solución homogénea, sino que se organiza en familias arquitectónicas con compromisos claramente diferenciados entre expresividad semántica, complejidad computacional y eficiencia temporal. A partir de un relevamiento exhaustivo realizado durante la investigación bibliográfica, se identificaron cuatro paradigmas dominantes, de los cuales se presentan a continuación los aspectos y modelos representativos más relevantes para el contexto de sistemas de video en tiempo real.

El primer paradigma extiende arquitecturas end-to-end basadas en Transformers —derivadas de DETR y DINO (Carion et al., 2020; H. Zhang et al., 2022)— incorporando el lenguaje dentro del proceso de predicción mediante mecanismos explícitos de fusión multimodal. El modelo representativo de esta familia es Grounding DINO (Liu et al., 2023), que introduce una fusión multimodal profunda estructurada en tres componentes: un Feature Enhancer que alinea semánticamente regiones visuales con tokens textuales, un Language-guided Query Selection que inicializa las consultas del decoder condicionadas por el texto y un Cross-modality Decoder que refina cajas y asocia predicciones a fragmentos del prompt mediante atención cruzada. Esta arquitectura resulta especialmente efectiva para expresiones referenciales complejas y frases con atributos, reportando 52.5 AP en COCO en configuración zero-shot (Liu et al., 2023).

Desarrollos posteriores como OmDet-Turbo (Zhao et al., 2024) abordan explícitamente la limitación de latencia de este paradigma mediante un módulo de fusión eficiente que permite reutilizar los embeddings textuales entre cuadros consecutivos, amortizando el costo del procesamiento lingüístico cuando el vocabulario de consulta permanece constante. Esta estrategia es directamente relevante para escenarios de monitoreo continuo, donde el conjunto de condiciones de riesgo se define al inicio de la sesión y se mantiene estable a lo largo del flujo de video.

Un segundo paradigma traslada la detección OVD a arquitecturas one-stage de alta eficiencia, derivadas de la familia YOLO, diseñando la integración visión-lenguaje para minimizar el costo adicional en inferencia. El exponente principal es YOLO-World (Cheng et al., 2024), que introduce un mecanismo de Re-Parameterizable Vision-Language Path Aggregation Network (RepVL-PAN) y un módulo de Cross-Modal Late Interaction (CSAM) para alinear características visuales densas con embeddings textuales durante el entrenamiento. En inferencia, los embeddings textuales pueden reparametrizarse como pesos equivalentes a los de un detector YOLO estándar, eliminando el overhead de la fusión multimodal en tiempo de ejecución. Su sucesor, YOLOE (A. Wang et al., 2025), extiende este principio logrando overhead computacional cero tras la reparametrización, reportando 35.9 AP en LVIS-minival con 102.5 FPS en hardware de inferencia optimizado. Este paradigma prioriza tasas de inferencia elevadas y baja latencia, a cambio de una menor expresividad semántica frente a consultas complejas o con atributos relacionales.

Una tercera familia plantea la detección como una extensión del paradigma de clasificación zero-shot de CLIP, utilizando un encoder visual y un encoder textual que proyectan imagen y texto en un espacio semántico compartido. La clasificación abierta se resuelve mediante puntajes de compatibilidad —producto punto entre embeddings visuales locales y embeddings textuales— en lugar de logits de clase fijos. El representante más relevante es OWL-ViT y su evolución OWLv2 (Minderer et al., 2022, 2024), que escala el entrenamiento mediante auto-entrenamiento sobre datos web a gran escala, generando más de mil millones de ejemplos de entrenamiento mediante pseudo-anotaciones. Esta estrategia mejora significativamente el rendimiento en categorías raras del benchmark LVIS (Gupta et al., 2019).

La ventaja principal de este paradigma es su modularidad, donde cambiar el vocabulario de consulta equivale simplemente a cambiar los prompts, sin modificar la arquitectura del modelo. La limitación principal reside en que el cómputo de embeddings textuales por cada nueva consulta introduce latencia variable, aunque esta puede mitigarse mediante caching cuando el vocabulario permanece estable entre cuadros consecutivos.

Un cuarto paradigma reformula la detección como un problema secuencia-a-secuencia condicionado por instrucciones en lenguaje natural, donde el modelo genera salidas estructuradas —texto que codifica cajas delimitadoras, etiquetas y descripciones— mediante decodificación autoregresiva. El modelo representativo es Florence-2 (Xiao et al., 2023), que unifica múltiples tareas de visión —detección, segmentación, captioning y razonamiento visual— bajo un esquema de prompting generalista, sin necesidad de rediseñar cabezales específicos por tarea. La ventaja de este paradigma es su flexibilidad para abordar condiciones de riesgo que requieren descripciones complejas o ricas en contexto.

La limitación crítica para aplicaciones de video en tiempo real es la dependencia de decodificación autoregresiva, que introduce mayor latencia de inferencia y variabilidad temporal respecto a los paradigmas anteriores. La naturaleza secuencial de la generación impide el paralelismo completo de la inferencia, y la inestabilidad frame-to-frame es más pronunciada en este paradigma que en los enfoques de predicción directa, dado que la variabilidad del proceso generativo se acumula entre cuadros consecutivos (Xiao et al., 2023). Esta característica limita su adecuación para sistemas de monitoreo continuo con requisitos estrictos de latencia E2E.

A continuación, se revisan modelos representativos de cada paradigma, enfocando el análisis en: (i) decisiones arquitectónicas, (ii) mecanismo de fusión/compatibilidad visión–lenguaje, (iii) régimen de entrenamiento y tipo de supervisión, y (iv) resultados en benchmarks estándar (COCO, LVIS), junto con consideraciones prácticas de inferencia relevantes para aplicaciones en vídeo.


##### 15.2.1.1. Bloque A — Detectores End-to-End Tipo DETR/DINO con Fusión Visión–Lenguaje en el Decoder


###### 15.2.1.1.1. GLIP y GLIPv2

Arquitectura base. GLIP (Grounded Language-Image Pre-training) unifica detección y phrase grounding bajo una formulación común: el modelo recibe una imagen y un prompt textual con las categorías o frases de interés. Su implementación se construye sobre un detector tipo Dynamic Head y emplea un backbone visual Swin Transformer, junto con un encoder de texto BERT y un módulo de fusión multimodal profunda (Li et al., 2021).

Mecanismo visión–lenguaje. La contribución central de GLIP es reformular la clasificación cerrada como alineamiento región–palabra/región–frase: en lugar de producir logits de clase fijos, reemplaza el clasificador por puntajes de alineamiento entre features visuales de región y features lingüísticas de tokens. A diferencia de enfoques donde visión y texto solo interactúan al final, GLIP enfatiza fusión profunda para integrar señales lingüísticas dentro del pipeline de detección (Li et al., 2021).

Entrenamiento y supervisión. GLIP escala el preentrenamiento mediante datos de grounding a gran escala, combinando 3 millones de anotaciones humanas y 24 millones de pares imagen–texto web con pseudo-cajas generadas mediante self-training, totalizando 27 millones de ejemplos (Li et al., 2021).

Evolución GLIPv2. GLIPv2 extiende el enfoque hacia un modelo unificado que cubre tareas de localización (detección, segmentación por instancias, grounding) y comprensión visión–lenguaje (VQA, captioning). El preentrenamiento unifica tres tareas: phrase grounding, region–word contrastive learning y masked language modeling (Zhang et al., 2022).

Resultados reportados. GLIP alcanza 49.8 AP en COCO y 26.9 AP en LVIS en evaluación directa zero-shot. Con fine-tuning en COCO, reporta 60.8 AP en val y 61.5 AP en test-dev. GLIPv2-H logra 60.6 AP en COCO test-dev y 59.8 AP (caja) en LVIS-minival (Li et al., 2021; Zhang et al., 2022).


###### 15.2.1.1.2. OV-DETR

Arquitectura base. OV-DETR (Zang et al., 2022) representa un enfoque temprano para llevar la detección end-to-end tipo DETR al escenario open-vocabulary. Parte de Deformable DETR como detector base (Zhu et al., 2020) y utiliza CLIP para representar consultas abiertas en forma de texto o imágenes ejemplares.

Mecanismo visión–lenguaje. El obstáculo central al extender DETR a open-vocabulary es que el entrenamiento estándar usa matching bipartito con un costo de clasificación definido sobre clases conocidas. OV-DETR evita este problema reformulando el aprendizaje como matching condicional binario: dado un concepto (texto o imagen), el modelo aprende a decidir si una predicción corresponde o no a esa consulta, en lugar de resolver una clasificación multiclase cerrada (Zang et al., 2022).

Resultados reportados. OV-DETR alcanza 17.4 AP en clases novedosas en el protocolo OV-LVIS y 29.4 AP50 en categorías novedosas en OV-COCO, demostrando que la formulación condicional permite detectar categorías no vistas con un marco end-to-end (Zang et al., 2022).

Licencia. El código se distribuye bajo licencia CC BY-NC-SA 4.0, lo que restringe el uso comercial (Zang, 2022).


###### 15.2.1.1.3. Grounding DINO

Arquitectura base. Grounding DINO propone un detector open-set construido sobre la línea DETR/DINO, con razonamiento global vía Transformer y diseño explícito para integrar lenguaje durante la predicción. El modelo emplea una arquitectura dual-encoder/single-decoder: un backbone visual (frecuentemente Swin Transformer) extrae características multi-escala y un backbone textual (BERT) codifica el prompt (Liu et al., 2023).

Mecanismo visión–lenguaje. La contribución central es una fusión multimodal profunda basada en atención cruzada en distintas etapas. Grounding DINO divide la fusión en tres componentes: Feature Enhancer (interacciones imagen–texto para alinear semántica y regiones), Language-guided Query Selection (inicializa consultas del decoder condicionadas por texto), y Cross-modality Decoder (agrega atención cruzada con texto para refinar cajas y asociar predicciones a fragmentos del prompt). Esto hace que el modelo sea especialmente efectivo con expresiones referenciales o frases con atributos (Liu et al., 2023).

Resultados reportados. En configuración zero-shot, Grounding DINO reporta 52.5 AP en COCO y un récord de 26.1 mAP promedio en ODinW (Liu et al., 2023).

Evolución Grounding DINO 1.5. La versión 1.5 Pro, orientada a máxima generalización, entrena con Grounding-20M (más de 20 millones de imágenes) y logra 54.3 AP en COCO y 55.7 AP en LVIS-minival en zero-shot transfer. La versión 1.5 Edge, orientada a despliegue eficiente, reporta 75.2 FPS y 36.2 AP en LVIS-minival con TensorRT, y despliegue en NVIDIA Orin NX con más de 10 FPS (Ren et al., 2024b).

Licencia. El repositorio oficial se distribuye bajo licencia Apache-2.0 (IDEA-Research, 2024 -a).


###### 15.2.1.1.4. OV-DINO

Arquitectura base. OV-DINO propone un detector open-vocabulary dentro del paradigma DETR/DINO, orientado a robustecer el preentrenamiento a gran escala y reducir el impacto del ruido típico de las pseudo-anotaciones. La receta se organiza alrededor de dos ideas: unificar fuentes de datos heterogéneas en un formato "detection-centric" y mejorar la fusión multimodal durante la predicción (Wang et al., 2024).

Mecanismo visión–lenguaje. OV-DINO introduce Unified Data Integration (UniDI) para integrar múltiples fuentes mitigando ruido de pseudo-labeling, y Language-Aware Selective Fusion (LASF), un módulo de fusión selectiva guiada por lenguaje para alineación visión–lenguaje más efectiva (Wang et al., 2024).

Resultados reportados. En evaluación zero-shot, OV-DINO reporta 50.6 AP en COCO y 40.1 AP en LVIS-minival (Wang et al., 2024).

Licencia. El repositorio oficial está bajo licencia Apache-2.0 (Wang, 2024).


###### 15.2.1.1.5. DINO-X

Arquitectura base. DINO-X es un modelo unificado y object-centric para detección open-world/open-vocabulary, desarrollado como evolución directa de Grounding DINO 1.5, manteniendo un esquema Transformer encoder–decoder orientado a representaciones a nivel objeto. A diferencia de detectores OV que dependen estrictamente de listas de clases, DINO-X soporta múltiples tipos de prompt: texto, prompts visuales y prompts personalizados (Ren et al., 2024a).

Mecanismo visión–lenguaje. La idea distintiva de DINO-X es combinar flexibilidad de entrada con un mecanismo prompt-free mediante un Universal Object Prompt que permite "detectar cualquier cosa" sin definir clases específicas (Ren et al., 2024a).

Entrenamiento. El trabajo construye y utiliza Grounding-100M, un conjunto con más de 100 millones de muestras de grounding de alta calidad para preentrenamiento (Ren et al., 2024a).

Resultados reportados. DINO-X Pro alcanza 56.0 AP en COCO, 59.8 AP en LVIS-minival y 63.3 AP en clases raras de LVIS-minival, estableciendo un nuevo estado del arte en detección abierta (Ren et al., 2024a).

Licencia. El repositorio público indica licencia Apache-2.0 (IDEA-Research, 2024 -c).


###### 15.2.1.1.6. OmDet-Turbo

Arquitectura base. OmDet-Turbo es un detector open-vocabulary basado en Transformers, diseñado explícitamente para tiempo real. El trabajo identifica cuellos de botella típicos en detectores OV tipo DETR y propone un módulo central llamado Efficient Fusion Head (EFH) que incluye ELA-Encoder (Efficient Language-Aware Encoder) para generar consultas eficientemente y ELA-Decoder que evita operaciones lentas tipo ROIAlign (Zhao et al., 2024).

Caching de embeddings textuales. Un punto clave para vídeo es que, si el vocabulario se mantiene constante a lo largo de una secuencia, OmDet-Turbo permite cachear embeddings textuales evitando recomputar el backbone textual en cada frame, ahorrando aproximadamente 40 ms en la variante Tiny (Zhao et al., 2024).

Resultados reportados. OmDet-Turbo-Base alcanza 53.4 AP en COCO y 34.7 AP en LVIS-minival con 18.6 FPS (PyTorch) y 100.2 FPS (TensorRT) en A100. La variante Tiny alcanza 42.5 AP en COCO con 140.0 FPS (TensorRT), posicionándolo como atractivo cuando el requerimiento dominante es latencia (Zhao et al., 2024).

Licencia. El repositorio oficial se publica bajo licencia Apache-2.0 y está integrado en Hugging Face Transformers (om-ai-lab, 2024.; Hugging Face, 2024).


##### 15.2.1.2. Bloque B: Detectores one-stage tipo YOLO con puntuación región–texto


###### 15.2.1.2.1. YOLO-World

Arquitectura base. YOLO-World adapta un detector one-stage de la familia YOLO al escenario open-vocabulary manteniendo predicción densa y diseño orientado a despliegue. Su contribución arquitectónica central es RepVL-PAN (Re-parameterizable Vision-Language Path Aggregation Network), un neck multiescala que incorpora interacción visión–lenguaje sin abandonar la estructura backbone–PAN–head propia de YOLO (Cheng et al., 2024).

Mecanismo visión–lenguaje. El modelo puntúa regiones mediante similitud en un espacio compartido región–texto. RepVL-PAN implementa esta interacción con Text-guided CSPLayer para inyectar guía textual en las features visuales e Image Pooling Attention para enriquecer embeddings textuales con contexto visual. En despliegue, YOLO-World opera con vocabulario offline y habilita una reparametrización que permite prescindir del encoder textual durante inferencia (Cheng et al., 2024).

Resultados reportados. YOLO-World-L reporta 35.4 AP en LVIS-minival con 52.0 FPS en NVIDIA V100 (sin TensorRT), mostrando un punto de operación competitivo para aplicaciones con restricción de latencia (Cheng et al., 2024).

Licencia. El repositorio declara licencia GPL-3.0, con posibilidad de gestionar licencia alternativa para uso comercial (AILab-CVC, 2024).


###### 15.2.1.2.2. YOLOE

Arquitectura base. YOLOE, presentado como "Real-Time Seeing Anything", propone un modelo one-stage que unifica detección y segmentación manteniendo el esquema backbone–PAN–heads típico de YOLO. Sus módulos de alineamiento se diseñan para que, tras reparametrización, el grafo de inferencia quede equivalente al de un YOLO cerrado (Wang et al., 2025).

Mecanismo visión–lenguaje. YOLOE integra tres modalidades: prompts de texto mediante RepRTA (Re-parameterizable Region-Text Alignment), prompts visuales mediante SAVPE (Semantic-Activated Visual Prompt Encoder), y modo prompt-free mediante LRPC (Lazy Region-Prompt Contrast) que reformula la asignación como retrieval evitando dependencia de modelos de lenguaje en inferencia (Wang et al., 2025).

Resultados reportados. En LVIS-minival zero-shot, YOLOE-v8-S reporta 27.9 AP con 305.8 FPS (NVIDIA T4, TensorRT) y YOLOE-v8-L alcanza 35.9 AP con 102.5 FPS, superando a YOLO-Worldv2-S por +3.5 AP con mayor velocidad (Wang et al., 2025).

Licencia. El repositorio declara licencia AGPL-3.0, lo que introduce requisitos copyleft que pueden condicionar adopción en integraciones propietarias (THU-MIG, 2025).


##### 15.2.1.3. Bloque C: Detectores Basados en Dual-Encoders (CLIP-like) y Matching por Similitud


###### 15.2.1.3.1. OWL-ViT y OWLv2

Arquitectura base. OWL-ViT propone una receta directa para llevar modelos visión–lenguaje a detección open-vocabulary usando un Vision Transformer (ViT) encoder-only con modificaciones mínimas. Se mantienen los tokens espaciales y se agregan cabezales livianos que predicen, por token, una caja y un embedding de compatibilidad. La clasificación abierta se logra reemplazando un clasificador cerrado por embeddings derivados del texto (Minderer et al., 2022).

Entrenamiento. OWLv2 escala mediante self-training (OWL-ST): usa un modelo OWL-ViT como annotator para generar pseudo-cajas sobre datos web a gran escala (WebLI). OWLv2 introduce mejoras de eficiencia de entrenamiento: un objectness head para entrenar pérdidas solo sobre un subconjunto de tokens más plausibles como objeto, y token dropping durante entrenamiento (Minderer et al., 2023).

Resultados reportados. OWL-ViT L/14 alcanza 34.6 AP y 31.2 AP en clases raras en LVIS. OWLv2 L/14 con OWL-ST reporta 44.6 AP en clases raras zero-shot en LVIS-val, y la variante G/14 alcanza 47.2 AP en clases raras (Minderer et al., 2022, 2023).

Licencia. Los pesos se distribuyen bajo Apache-2.0 (Google, 2022; Google, 2023).


###### 15.2.1.3.2. Detic

Arquitectura base. Detic ("Detecting Twenty-thousand Classes using Image-level Supervision") aborda la detección open-vocabulary desde un enfoque two-stage clásico (RPN y ROI head), planteando que en escenarios de gran vocabulario el cuello de botella no suele ser la generación de propuestas sino la clasificación de regiones (Zhou et al., 2022a).

Mecanismo visión–lenguaje. En configuración open-vocabulary, Detic reemplaza el clasificador cerrado por un esquema de matching: las features de región se puntúan contra embeddings lingüísticos de los nombres de clase usando embeddings de CLIP como pesos del clasificador (Zhou et al., 2022a).

Entrenamiento. El rasgo distintivo es cómo incorpora supervisión débil (labels a nivel imagen) para expandir el vocabulario. Su receta mezcla minibatches de datos con cajas y datos con etiquetas a nivel imagen, donde supervisa la clasificación usando la propuesta de mayor tamaño como proxy de objeto. Utiliza datasets de clasificación a gran escala (ImageNet-21K) para escalar hacia decenas de miles de conceptos (Zhou et al., 2022a).

Resultados reportados. En OV-LVIS, Detic reporta 26.8 mask mAP y 17.8 AP en clases raras. En OV-COCO alcanza 45.0 mAP50 (all) y 27.8 en categorías novel. Detic suele usarse como baseline fuerte para vocabularios grandes, aunque su naturaleza two-stage lo ubica lejos de objetivos de tiempo real (Zhou et al., 2022a).

Licencia. El repositorio indica licencia Apache-2.0 (Zhou, s.f.).


###### 15.2.1.3.3. Familia DetCLIP

Arquitectura base. La familia DetCLIP se centra en escalar el aprendizaje open-vocabulary mediante preentrenamiento que integra datos heterogéneos (detección/grounding/imagen–texto) con mecanismos que refuerzan la semántica lingüística. DetCLIP se apoya en un detector tipo ATSS con backbone Swin y expansión semántica mediante un diccionario de conceptos (Yao et al., 2022).

Evolución. DetCLIPv2 reformula el objetivo hacia alineamiento fino palabra–región aprendido end-to-end directamente desde pares imagen–texto, sin depender de teachers CLIP congelados (Yao et al., 2023). DetCLIPv3 empuja el paradigma hacia detección más generativa incorporando un cabezal de captioning para etiquetas jerárquicas (Yao et al., 2024).

Resultados reportados. DetCLIP reporta 35.9 AP en LVIS (Swin-T). DetCLIPv2 alcanza 40.4 AP (Swin-T) y 44.7 AP (Swin-L) en LVIS-minival. DetCLIPv3 reporta 48.8 AP en LVIS-minival (Swin-L) y 49.9 AP en categorías raras (Yao et al., 2022, 2023, 2024).


##### 15.2.1.4. Bloque D: Modelos generativos guiados por instrucciones


###### 15.2.1.4.1. APE (Aligning and Prompting Everything)

Paradigma y tipo de consulta. APE se ubica en la línea de prompting generalista guiado por lenguaje: el mismo modelo puede ejecutarse como detección/segmentación open-vocabulary y como grounding a partir de listas grandes de categorías y/o descripciones en lenguaje natural. Aunque es guiado por prompts, APE no depende de decodificación autoregresiva, produciendo predicciones estructuradas de manera directa (Shen et al., 2023).

Arquitectura base. APE se construye sobre un pipeline tipo DETR (encoder–decoder Transformer) y combina vision backbone (ViT), modelo de lenguaje para embeddings de prompts, cross-modality encoder para fusionar texto–imagen, y decoder que produce predicciones a nivel objeto. Soporta salidas de detección (cajas) y segmentación (máscaras) (Shen et al., 2023).

Mecanismo visión–lenguaje. El núcleo de APE es alinear instancias con texto mediante una formulación unificada: cada prompt se procesa de forma independiente y el modelo calcula puntajes de alineamiento mediante producto punto. Para escalar a miles de categorías sin costo prohibitivo, APE introduce una interacción cross-modal "gated" que puede simplificarse para vocabularios grandes (Shen et al., 2023).

Resultados reportados. APE-L (D) reporta 59.6 AP (caja) y 53.0 AP (máscara) en LVIS, y 58.3 AP (caja) en COCO con un solo conjunto de pesos. En suites "in the wild", reporta 64.7 en Roboflow100 y 57.9 en ODinW-13 (Shen et al., 2023).

Licencia. El repositorio declara licencia Apache-2.0 (Shen, s.f.).


###### 15.2.1.4.2. Florence-2

Paradigma y tipo de consulta. Florence-2 se enmarca en el paradigma generativo guiado por instrucciones: interpreta un prompt textual de tarea (por ejemplo, "object detection", "dense caption", "OCR") y genera una salida en texto que se post-procesa para recuperar cajas, etiquetas u otras estructuras. Opera con task tokens y puede combinarse con texto adicional (Xiao et al., 2024).

Arquitectura base. Florence-2 adopta una formulación sequence-to-sequence con un Transformer encoder–decoder multimodal. El input combina tokens visuales producidos por un encoder de visión DaViT (Dual Attention Vision Transformer) y embeddings del prompt de tarea. Para representar salida espacial, el modelo amplía el vocabulario con tokens de localización cuantizados usando 1000 bins (Xiao et al., 2023; Ding et al., 2022).

Entrenamiento. El modelo se preentrena sobre FLD-5B, un dataset con 126 millones de imágenes y más de 5 mil millones de anotaciones desglosadas como 500 millones de anotaciones de texto, 1.3 mil millones de anotaciones región–texto y 3.6 mil millones de anotaciones texto–frase–región (Xiao et al., 2023).

Resultados reportados. En zero-shot, Florence-2-L (0.77B parámetros) reporta 37.5 mAP en COCO Det y 135.6 CIDEr en COCO Caption. Tras fine-tuning multitarea, alcanza 43.4 mAP en COCO Det y 93.4 Accuracy@0.5 en RefCOCO (Xiao et al., 2023).

Implicaciones para vídeo. Un solo modelo puede cubrir detección, grounding, captioning y OCR, útil para prototipado rápido. Sin embargo, al ser autoregresivo, el costo de inferencia y la latencia tienden a ser más altos y variables, y en vídeo esa variabilidad suele traducirse en inestabilidad temporal si no se complementa con tracking (Xiao et al., 2023).

Licencia. Los pesos publicados para Florence-2-large indican licencia MIT (Microsoft, 2024).


###### 15.2.1.4.3. LLMDet

Paradigma y tipo de consulta. LLMDet se ubica en una línea híbrida: incorpora señales generativas y conocimiento lingüístico de un LLM durante el entrenamiento, pero en inferencia opera como un detector open-vocabulary convencional sin LLM. El tipo de consulta en despliegue es el habitual: lista de clases y/o frases (Fu et al., 2025).

Arquitectura base. El trabajo toma como detector base MM Grounding DINO y añade un proyector que mapea features visuales al espacio de entrada del LLM, y un LLM que recibe features globales y por región para generar texto durante entrenamiento. El LLM se descarta en inferencia, eliminando overhead en producción (Fu et al., 2025).

Entrenamiento. Se construye el conjunto GroundingCap-1M, en el cual cada muestra incluye una imagen, texto de grounding, cajas asociadas a frases y un caption largo. El entrenamiento combina la pérdida de grounding del detector con pérdidas de language modeling, orientadas tanto a la generación de captions largos a nivel de imagen como de descripciones cortas a nivel de región. La incorporación de captions largos contribuye a mejorar el desempeño en clases raras y escenarios de long-tail (Fu et al., 2025).

Resultados reportados. Con Swin-L, LLMDet reporta 51.1 AP en LVIS-minival y 42.0 AP en LVIS-val, con mejoras marcadas en clases raras. También reportan mejoras en ODinW y robustez ante shift de distribución en COCO-O (Fu et al., 2025).

Licencia. El repositorio indica licencia Apache-2.0 (iSEE-Laboratory, 2025).


###### 15.2.1.4.4. T-Rex2

Paradigma y tipo de consulta. T-Rex2 entra en el Bloque D por su foco en prompting generalista multimodal: soporta prompts de texto, prompts visuales y prompts combinados, distinguiendo flujos interactivos (refinables) y genéricos (visual prompts reutilizables) (Jiang et al., 2024).

Arquitectura base. El paper plantea un modelo práctico de open-set object detection que explota la complementariedad: texto abstrae bien objetos comunes, mientras los prompts visuales representan mejor objetos raros o difíciles de describir. Su contribución de ingeniería clave es una fusión tardía que permite iterar/refinar prompts sin recalcular el encoder de imagen múltiples veces (Jiang et al., 2024).

Entrenamiento. El paper reporta entrenamiento diferenciado para texto y visual prompts con mezcla de datos etiquetados y pseudo-etiquetas, incluyendo self-training sobre SA-1B para visual prompts y cyclical training alternando texto/visual (Jiang et al., 2024).

Resultados reportados. Con Swin-L, T-Rex2 alcanza 46.7 AP en LVIS-minival (texto) y 46.8 AP (visual-genérico), además de números competitivos en ODinW y Roboflow100. El trabajo muestra que el texto gana en categorías frecuentes mientras que el visual gana en muchas categorías raras (Jiang et al., 2024).

Implicación para vídeo. T-Rex2 es interesante por permitir anclar la detección a un ejemplo visual (útil para seguimiento) y por fusión tardía que favorece flujos interactivos sin multiplicar el costo del encoder visual (Jiang et al., 2024).


##### 15.2.1.5. Bloque E — Pipelines, segmentación y despliegue (extensiones prácticas)


###### 15.2.1.5.1. Grounded SAM y Grounded SAM 2

Paradigma. Grounded SAM es representativo de una estrategia de pipeline (ensamblado de modelos foundation) más que de una arquitectura monolítica: resuelve segmentación open-vocabulary descomponiéndola en grounding/detección condicionado por texto y segmentación guiada condicionada por cajas/puntos (Ren et al., 2024c).

Arquitectura base. El pipeline estándar es: 1) Grounding DINO, 2) cajas (condicionadas por prompt textual) y luego 3) SAM con máscaras usando esas cajas como box prompts. SAM por sí solo no "entiende" texto; Grounded SAM lo vuelve text-promptable delegando la parte semántica al detector open-set (Kirillov et al., 2023; Ren et al., 2024c).

Evolución Grounded SAM 2. Grounded SAM 2 actualiza el componente de segmentación a SAM 2 (que soporta imagen y vídeo) y agrega demos de "ground & track". El repositorio soporta varios grounders (Grounding DINO, Florence-2, DINO-X) combinables con SAM 2 para segmentación y tracking (IDEA-Research, 2024 -b; Ravi et al., 2024).

Resultados reportados. Grounded SAM reporta 48.7 mean AP en SegInW con Grounding DINO-Base + SAM-Huge (Ren et al., 2024c).

Valor práctico. El pipeline es ideal para auto-anotación y análisis donde la segmentación precisa vale más que la latencia. En vídeo, Grounded SAM 2 empuja hacia ground & track con SAM 2, aunque el costo de encadenar modelos grandes no es el camino natural al tiempo real estricto (Ren et al., 2024c).

Licencia. Grounded-Segment-Anything se distribuye bajo Apache-2.0; Grounded-SAM-2 incluye componentes bajo Apache-2.0 y BSD-3-Clause (IDEA-Research, 2023; IDEA-Research, 2024 -b).


###### 15.2.1.5.2. OVTrack

Paradigma. OVTrack formaliza open-vocabulary multiple object tracking (MOT) como un problema donde, en test, el sistema recibe una lista de clases de interés (base + novel) y debe detectar y asociar instancias a lo largo del tiempo. La evaluación permite medir precisión/recobrado y calidad de clasificación para clases no vistas durante entrenamiento (Li et al., 2023).

Arquitectura base. OVTrack sigue el paradigma tracking-by-detection: localizador agnóstico a clase basado en Faster R-CNN para proponer cajas por frame, cabezas de embeddings (texto e imagen) para reemplazar el clasificador cerrado por un mecanismo abierto, y head de tracking que produce embedding de apariencia y realiza asociación mediante memoria de tracks (Li et al., 2023).

Entrenamiento. OVTrack entrena el tracker usando sólo imágenes estáticas (LVIS), evitando dependencia de grandes datasets de vídeo etiquetados. Para aprender apariencia útil en tracking sin vídeo real, introduce data hallucination con modelos de difusión (DDPM) para sintetizar pares de instancias positivas/negativas (Li et al., 2023).

Resultados reportados. En TAO open-vocabulary, OVTrack obtiene TETA 35.5 (base) y 27.8 (novel) en validation, y TETA 32.6 (base) y 24.1 (novel) en test (Li et al., 2022, 2023).

Implicaciones para despliegue. El embedding textual del vocabulario puede precalcularse/cachearse si la lista de clases se mantiene fija. Al depender de un detector two-stage por frame más asociación por embeddings, no está pensado como solución real-time end-to-end, sino como baseline fuerte y medible para escenarios abiertos y long-tail (Li et al., 2023).

Licencia. El repositorio reporta licencia Apache-2.0 (SysCV, 2023).


###### 15.2.1.5.3. Roboflow Rapid

Paradigma. Roboflow Rapid no es un modelo OVD en sentido estricto de inferencia con vocabulario abierto, sino un pipeline de operacionalización: parte de una consulta en lenguaje natural y/o ejemplos para auto-etiquetar, entrenar y desplegar rápidamente un detector funcional. El lenguaje se usa principalmente para definir el concepto y generar etiquetas, mientras que el modelo final opera como detector especialista (Deschere, 2025).

Arquitectura del sistema. Rapid implementa un flujo de extremo a extremo: ingesta de imágenes o vídeo, etiquetado asistido por prompt, entrenamiento de un modelo RF-DETR custom, y despliegue automático vía Roboflow Serverless API (Robicheaux et al., 2025; Roboflow, 2025a, 2025b).

Implicaciones prácticas. Rapid es útil para acelerar baselines y datasets, pero no reemplaza un OVD "real" cuando el requisito es cambiar vocabulario en tiempo de ejecución sin reentrenar. El modelo final se comporta más como cerrado/dominio-específico que como vocabulario abierto en tiempo de ejecución (Roboflow, 2025a).

Licencia. Rapid es un producto/plataforma sujeto a condiciones del servicio. RF-DETR (arquitectura base) se publica como open-source bajo Apache-2.0 (Robicheaux et al., 2025; Robinson et al., 2025).


#### 15.2.2. Composición de Modelos y Pipelines de Percepción

Los paradigmas arquitectónicos analizados en la sección 15.2.1 comparten un supuesto implícito: el modelo de detección opera como un componente autosuficiente que recibe una imagen y produce un conjunto de cajas delimitadoras con puntajes de compatibilidad semántica. Sin embargo, la experiencia acumulada en la literatura y en los ecosistemas de despliegue muestra que, en la práctica, los modelos OVD rara vez operan de manera aislada. Del análisis realizado, se identifican enfoques composicionales que integran capacidades complementarias —detección, segmentación de instancias y seguimiento temporal— para abordar tareas que exceden el alcance de un detector individual (Ren et al., 2024). Esta observación es relevante para el marco teórico del proyecto porque introduce una dimensión de diseño que no se reduce a la selección de un modelo, sino a la articulación de capacidades en una arquitectura de percepción.

El exponente más representativo de este enfoque composicional es Grounded SAM (Ren et al., 2024), un pipeline que descompone la segmentación open-vocabulary en dos etapas encadenadas: primero, un detector condicionado por texto —típicamente Grounding DINO (Liu et al., 2023)— genera cajas delimitadoras asociadas a las descripciones del prompt; luego, un modelo de segmentación universal —SAM, Segment Anything Model (Kirillov et al., 2023)— produce máscaras de instancia precisas utilizando esas cajas como señal de localización. El diseño es deliberadamente modular: SAM por sí solo carece de comprensión semántica, y Grounding DINO por sí solo no produce segmentación; es la composición la que habilita una capacidad que ninguno de los componentes posee individualmente. Esta arquitectura composicional introduce un compromiso explícito. Por un lado, la modularidad permite sustituir componentes de manera independiente —reemplazar el detector, actualizar el segmentador o intercalar etapas de procesamiento— sin rediseñar el pipeline completo. Por otro lado, la ejecución secuencial de múltiples modelos foundation acumula latencia y consumo de recursos, lo que limita su aplicabilidad directa en escenarios de video en tiempo real con requisitos estrictos de latencia extremo a extremo. Esta tensión entre modularidad y eficiencia es inherente al patrón composicional y debe considerarse como un factor de diseño en la evaluación de alternativas para etapas posteriores.

La evolución hacia Grounded SAM 2 (Ravi et al., 2024) extiende el pipeline al dominio temporal, incorporando SAM 2 como componente de segmentación capaz de operar tanto sobre imágenes estáticas como sobre secuencias de video, habilitando funcionalidades de segmentación y seguimiento combinados (ground and track).

Paralelamente, trabajos como OVTrack (S. Li et al., 2023) formalizan el problema del seguimiento multi-objeto en vocabulario abierto (open-vocabulary MOT), donde el sistema debe detectar y asociar temporalmente instancias de clases tanto conocidas como no vistas durante el entrenamiento. OVTrack adopta el paradigma tracking-by-detection con un localizador agnóstico a clase y cabezas de embeddings textuales y visuales para clasificación abierta, entrenando exclusivamente sobre imágenes estáticas mediante técnicas de data hallucination con modelos de difusión para sintetizar pares de apariencia (S. Li et al., 2023). Si bien el análisis detallado de los mecanismos de seguimiento temporal se desarrolla en la sección 15.3, la existencia de OVTrack como marco formalizado refuerza la observación de que la OVD se concibe cada vez más como un componente dentro de un sistema de percepción más amplio, no como una solución terminal.

La implicación de esta tendencia es que, en la práctica industrial y en la literatura reciente, los sistemas de percepción basados en OVD no se despliegan como detectores aislados, sino como cadenas de procesamiento donde la detección semántica constituye una etapa dentro de un flujo más amplio que típicamente incluye preprocesamiento de la señal visual, segmentación, seguimiento temporal y generación de eventos o alertas (S. Li et al., 2023; Ren et al., 2024). Esta observación refuerza que la evaluación de modelos OVD no puede limitarse a métricas de precisión aisladas, sino que debe considerar la integrabilidad de cada componente dentro de pipelines compuestos, incluyendo factores como la compatibilidad de formatos de entrada y salida entre etapas, el overhead acumulado por la ejecución secuencial de modelos y la estabilidad temporal de las predicciones a lo largo del flujo.


#### 15.2.3. Síntesis Comparativa y Trade-Offs para Tiempo Real

La Tabla 2 sintetiza las características fundamentales de los cuatro paradigmas arquitectónicos analizados, con énfasis en las dimensiones más relevantes para la viabilidad del sistema E-OVRT-VDP en un contexto de vídeo en tiempo real.

Tabla 2

Síntesis comparativa de paradigmas arquitectónicos OVD según dimensiones relevantes para sistemas de video en tiempo real


| Paradigma | Modelo(s) representativos | Mecanismo visión-lenguaje | Fortaleza principal | Limitación para tiempo real |
| --- | --- | --- | --- | --- |
| DETR/DINO + fusión profunda | Grounding DINO, OV-DINO, OmDet-Turbo, DINO-X | Fusión multimodal en decoder mediante atención cruzada visión-lenguaje | Alta precisión semántica; manejo de expresiones referenciales complejas | Costo computacional elevado; requiere optimización explícita para tiempo real |
| One-stage YOLO + puntuación región-texto | YOLO-World, YOLOE | Alineamiento región-texto reparametrizable; reducción progresiva del overhead de fusión mediante reparametrización | Alta velocidad de inferencia; compatible con hardware de borde | Menor expresividad semántica frente a consultas complejas o con atributos compuestos |
| Dual-encoder CLIP-like + matching por similitud | OWL-ViT, OWLv2, DetCLIP | Matching por similitud en espacio de embeddings compartido; reutilización directa de preentrenamiento contrastivo | Modularidad; cambio de vocabulario sin modificar el modelo | latencia variable según tamaño del vocabulario; requiere caching para vocabularios estables; requiere cómputo de embeddings por consulta |
| Generativo guiado por instrucciones | Florence-2, APE | Florence-2: decodificación autoregresiva seq2seq condicionada por instrucciones; APE: predicción directa con alineamiento por producto punto (Xiao et al., 2023; Shen et al., 2023) | Flexibilidad multitarea; soporte para prompts complejos y multimodales | Florence-2: latencia de inferencia variable e inestabilidad temporal por decodificación autoregresiva; APE: costo de prompting masivo escalable pero sin garantías de tiempo real estricto |

Nota. La columna “Limitación para tiempo real” describe el principal factor restrictivo de cada paradigma en escenarios de monitoreo continuo. Los modelos listados son representativos de cada familia; no constituyen una lista exhaustiva. Las métricas de velocidad son contextuales al hardware y configuración de inferencia reportados en la literatura primaria. Fuente: Elaboración propia basada en las fuentes mencionadas (Cheng et al., 2024; Liu et al., 2023; Minderer et al., 2022, 2024; A. Wang et al., 2025; Xiao et al., 2023).

Como complemento a esta síntesis por paradigmas, en la Tabla A.1 del Anexo A se incluye una matriz ampliada orientada a prototipado, donde se comparan modelos representativos según familia arquitectónica, mecanismo visión-lenguaje, métricas reportadas, rendimiento y licenciamiento. Dicha matriz conserva el detalle técnico necesario para respaldar la selección posterior de alternativas, sin sobrecargar el cuerpo principal del estado del arte.

Del análisis comparativo emergen tres tensiones técnicas que deben considerarse explícitamente como criterios orientadores para la selección tecnológica en etapas posteriores. La primera es la tensión entre precisión semántica y latencia de inferencia, ya que los modelos con fusión visión-lenguaje más profunda logran mayor robustez frente a consultas complejas, pero a un costo computacional que puede comprometer la tasa de frames procesados. La segunda es la tensión entre generalización zero-shot y especialización de dominio, cuya cuestión principal reside en que los benchmarks estándar sobre los que se reportan los resultados no representan las condiciones visuales de una obra civil, por lo que el desempeño reportado en la literatura no es directamente transferible al dominio objetivo. Esta tensión adquiere una dimensión adicional cuando se considera la posibilidad de adaptación de dominio mediante fine-tuning. El análisis detallado realizado anteriormente refleja que la capacidad de preservar la generalización open-vocabulary durante el ajuste de pesos varía sustancialmente entre familias arquitectónicas. Los detectores con fusión visión-lenguaje profunda y no removible, como Grounding DINO, exhiben mayor resiliencia, mientras que los detectores con módulos de texto reparametrizables, como YOLO-World y YOLOE, tienden a converger hacia un comportamiento closed-set bajo las configuraciones estándar de fine-tuning (Cheng et al., 2024; X. Zhao et al., 2024). Esta diferenciación entre arquitecturas constituye un factor relevante para la selección de modelos cuando se anticipa la necesidad de adaptación al dominio de la construcción civil. La tercera es la tensión entre expresividad semántica y simplicidad del prompt: consultas más precisas requieren mayor cuidado en la formulación, introduciendo una variable de diseño que no existe en sistemas closed-set.

Una observación transversal del análisis es que la reutilización de embeddings textuales entre cuadros consecutivos —cuando el vocabulario de consulta permanece estable— constituye la estrategia más relevante para aproximar la inferencia OVD a los requisitos de tiempo real, independientemente del paradigma arquitectónico adoptado (A. Wang et al., 2025; Zhao et al., 2024). Es en este contexto donde el conjunto de condiciones de riesgo se define al inicio de la sesión y se mantiene constante, esta estrategia es directamente aplicable y puede reducir significativamente el overhead de la fusión multimodal.

Adicionalmente, la tendencia hacia pipelines composicionales descrita en esta sección introduce una cuarta tensión que opera en un plano distinto a las anteriores: la tensión entre modularidad e integrabilidad. Los enfoques que ensamblan múltiples modelos foundation —como la combinación de un detector OVD con un segmentador universal— ofrecen mayor flexibilidad para sustituir componentes y abordar tareas compuestas, pero acumulan latencia de inferencia por la ejecución secuencial de etapas y aumentan la complejidad de integración entre formatos de entrada y salida. Esta tensión no invalida el patrón composicional, pero señala que la evaluación de alternativas en etapas posteriores deberá considerar no solo el rendimiento de cada modelo de forma aislada, sino el costo total del pipeline resultante bajo las restricciones temporales del escenario de aplicación.


##### 15.2.3.1. Análisis de Rendimiento para Tiempo Real

Desde el punto de vista del desempeño temporal, varios de los modelos analizados presentan características compatibles con aplicaciones de análisis de vídeo en tiempo real. La Tabla 3 resume el rendimiento reportado por los modelos más representativos, considerando distintos compromisos entre velocidad de inferencia, precisión en benchmarks open-vocabulary y viabilidad de despliegue sobre hardware acelerado.

Tabla 3

Análisis comparativo de rendimiento de modelos OVD para tiempo real


| Modelo | Hardware | Framework | FPS | Latencia | LVIS AP |
| --- | --- | --- | --- | --- | --- |
| YOLOE-v8-S | T4 | TensorRT | 305.8 | 3.3 ms | 27.9 |
| OmDet-Turbo-Tiny | A100 | TensorRT | 140.0 | 7.1 ms | 30.3 |
| YOLOE-v8-L | T4 | TensorRT | 102.5 | 9.8 ms | 35.9 |
| OmDet-Turbo-Base | A100 | TensorRT | 100.2 | 10 ms | 34.7 |
| G-DINO 1.5 Edge | A100 | TensorRT | 75.2 | 13.3 ms | 36.2 |
| YOLO-World-L | V100 | PyTorch | 52.0 | 19.2 ms | 35.4 |

Nota: Los valores de FPS, latencia y AP reportados provienen de los trabajos originales y no siempre fueron obtenidos bajo condiciones idénticas de hardware, resolución, batch size o framework. En consecuencia, deben interpretarse como indicativos y comparativos, no como benchmarks estrictamente normalizados. Fuente: elaboración propia basada en Wang et al. (2025), Zhao et al. (2024), Ren et al. (2024b) y Cheng et al. (2024).


#### 15.2.4. Ventajas, Limitaciones y Trade-Offs Observables

El análisis de arquitecturas y modelos de detección open-vocabulary pone de manifiesto que no existe una solución dominante que optimice simultáneamente precisión semántica, latencia, robustez open-set y facilidad de despliegue. En la práctica, cada enfoque introduce compromisos específicos que deben evaluarse en función del contexto de aplicación, particularmente cuando el objetivo es el análisis de video en tiempo real.


##### 15.2.4.1. Eficiencia y Latencia

Los modelos que declaran soporte para escenarios de tiempo real suelen apoyarse en dos estrategias principales. La primera consiste en reducir el costo de la fusión multimodal, ya sea limitando el uso de atención cruzada profunda o reparametrizando la influencia del lenguaje para preservar el paralelismo de la inferencia (Zhao et al., 2024). La segunda se basa en el caching de embeddings textuales, especialmente relevante en flujos de video donde el vocabulario permanece constante durante intervalos prolongados.

En este sentido, enfoques como OmDet-Turbo hacen explícita esta línea de diseño, permitiendo amortizar el costo del procesamiento lingüístico a lo largo de múltiples cuadros (T. Zhao et al., 2024). De forma complementaria, variantes optimizadas como Grounding DINO 1.5 Edge formalizan una orientación específica a despliegues acelerados, reportando métricas concretas de FPS bajo inferencia optimizada con TensorRT (Ren et al., 2024b). YOLOE representa el avance más significativo al lograr overhead cero después de reparametrización, igualando exactamente la velocidad de detectores YOLO estándar (Wang et al., 2025).


##### 15.2.4.2. Generalización Semántica y Robustez Open-Set

Desde el punto de vista de la generalización, los modelos con fusión visión-lenguaje profunda tienden a mostrar mayor robustez frente a conceptos no vistos y descripciones complejas. Grounding DINO enfatiza una integración estrecha entre lenguaje y visión, con evaluaciones explícitas en benchmarks como COCO, LVIS y ODinW (Liu et al., 2023). DINO-X alcanza 63.3 AP en categorías raras de LVIS, demostrando capacidad excepcional para el long-tail semántico (Ren et al., 2024a).

Enfoques como OV-DINO introducen mecanismos adicionales para reducir el ruido asociado al pseudo-etiquetado y mejorar la alineación selectiva guiada por lenguaje (Wang et al., 2024). LLMDet demuestra que la integración de conocimiento lingüístico externo vía un LLM puede llevar la detección open-vocab a niveles de precisión sin precedentes, aunque con arquitectura compleja y alta demanda computacional (Fu et al., 2025).


##### 15.2.4.3. Licencias y Riesgo de Adopción

Un aspecto frecuentemente subestimado en el análisis técnico, pero crucial para prototipos con proyección, es el régimen de licenciamiento. YOLO-World y YOLOE presentan casos paradigmáticos: ofrecen combinaciones muy competitivas de velocidad y precisión open-vocabulary, pero sus licencias GPLv3 y AGPL-3.0 respectivamente introducen restricciones relevantes para usos comerciales o integraciones cerradas (Cheng et al., 2024; Wang et al., 2025). De forma similar, OV-DETR bajo CC BY-NC-SA 4.0 limita explícitamente su uso fuera del ámbito académico (Zang et al., 2022). En contraste, modelos como Grounding DINO, OmDet-Turbo, LLMDet y varios checkpoints modernos se alinean con licencias permisivas como Apache-2.0 o MIT, reduciendo la fricción legal y simplificando su incorporación en prototipos experimentales con potencial de evolución futura.

En el contexto del presente trabajo, las consideraciones de licenciamiento no constituyen un condicionante operativo. El proyecto se desarrolla con fines estrictamente académicos y experimentales, sin orientación a explotación comercial ni a integración en productos cerrados.


##### 15.2.4.4. Integración de Segmentación y Seguimiento

Una tendencia emergente es combinar detección OVD con segmentación de instancias y seguimiento temporal. Grounded SAM ilustra esta integración: al acoplar un detector open-vocabulary con un segmentador universal, es posible localizar y segmentar cualquier región indicada por texto (Ren et al., 2024c). La extensión Grounded SAM 2 demuestra que es factible incorporar un módulo de tracking para seguir objetos segmentados a lo largo de un vídeo.

X-Decoder (Zou et al., 2023) explora un enfoque unificado con un decodificador capaz de producir tanto máscaras píxel a píxel como descripciones textuales, logrando estado del arte en segmentación open-vocabulary y segmentación referencial. YOLOE integra capacidad de segmentación directamente en la arquitectura, añadiendo una rama de máscara con mínima sobrecarga (Wang et al., 2025).


##### 15.2.4.5. Adaptabilidad Mediante Fine-Tuning y Preservación de Capacidad Open-Vocabulary

Las secciones precedentes evaluaron los modelos OVD en su modalidad zero-shot, es decir, utilizando exclusivamente los pesos obtenidos durante el preentrenamiento a gran escala. Sin embargo, la literatura reciente documenta de manera creciente el comportamiento de estas arquitecturas cuando se someten a fine-tuning sobre datasets de dominio específico, revelando un compromiso fundamental que no se manifiesta en los detectores closed-set convencionales. En un detector tradicional, el fine-tuning mejora el rendimiento en las categorías del dataset objetivo sin costo conceptual adicional. En un modelo OVD, el ajuste de los pesos puede degradar la capacidad de generalización semántica que constituye la propiedad distintiva de estos sistemas, fenómeno conocido en la literatura de modelos foundation como olvido catastrófico o catastrophic forgetting (Kirkpatrick et al., 2017). La intensidad de esta degradación varía significativamente según la profundidad de la fusión visión-lenguaje en la arquitectura, las capas que se ajustan y la estrategia de entrenamiento empleada.

Es por ello que a continuación se analizará la evidencia disponible para cada familia arquitectónica identificada anteriormente, con foco en las estrategias de fine-tuning documentadas, su efecto sobre la capacidad OVD residual y las implicancias para la selección de modelos en el proyecto.

Bloque A: Detectores end-to-end tipo DETR/DINO con fusión profunda. Grounding DINO (Liu et al., 2023) presenta la arquitectura más favorable para preservar capacidad OVD durante el fine-tuning, debido a que la integración del lenguaje ocurre en múltiples etapas del detector (Feature Enhancer, Language-guided Query Selection y Cross-modality Decoder) y no puede removerse sin destruir la funcionalidad del modelo. Los estudios de ablación muestran que la eliminación de cualquier componente de fusión reduce el AP zero-shot en más de 12 puntos, mientras que el impacto sobre el rendimiento en fine-tuning closed-set es mínimo, lo que indica que la maquinaria de fusión multimodal es esencial específicamente para la generalización open-set (Liu et al., 2023).

El proyecto MM-Grounding-DINO (X. Zhao et al., 2024) implementó y comparó tres estrategias de fine-tuning sobre la arquitectura Grounding DINO, ofreciendo la evaluación más completa disponible hasta el momento. La primera estrategia, denominada fine-tuning closed-set, optimiza el modelo directamente sobre el dataset objetivo y restringe el vocabulario textual a las categorías del dataset tras el ajuste, eliminando la capacidad OVD. La segunda, denominada preentrenamiento continuado open-set, reduce el learning rate y congela módulos específicos mientras continúa el entrenamiento sobre el dataset objetivo, o combina el dataset objetivo con datos de preentrenamiento originales, preservando la generalización. La tercera, fine-tuning open-vocabulary, entrena sobre categorías base y evalúa sobre categorías novedosas no vistas, midiendo explícitamente la retención de capacidad OVD (X. Zhao et al., 2024). Las dos últimas estrategias fueron diseñadas específicamente para mantener la generalizabilidad del modelo mientras mejoran el rendimiento en el dataset objetivo.

Adicionalmente, la adaptación mediante técnicas de ajuste eficiente de parámetros (PEFT) ha mostrado resultados prometedores. Grounding DINO puede adaptarse al dominio de imagen médica por ultrasonido mediante adaptadores LoRA (Low-Rank Adaptation) aplicados sobre backbones ViT y BERT congelados, habilitando segmentación guiada por prompts textuales sin reentrenar las redes subyacentes (Rasaee et al., 2025). Este enfoque resulta especialmente relevante para contextos con datasets de dominio reducidos, dado que minimiza tanto el costo computacional como el riesgo de degradación de la capacidad OVD. Grounding DINO alcanza 63.0 AP en COCO con fine-tuning closed-set frente a 52.5 AP en zero-shot (Liu et al., 2023), evidenciando un margen sustancial de mejora disponible mediante adaptación de dominio.

Bloque B: Detectores one-stage tipo YOLO con alineamiento visión-lenguaje. YOLO-World (Cheng et al., 2024) presenta un comportamiento frente al fine-tuning cualitativamente distinto al de Grounding DINO, debido a que su mecanismo de fusión visión-lenguaje (RepVL-PAN) fue diseñado para ser reparametrizable, es decir, los embeddings textuales pueden incorporarse como pesos fijos del modelo, permitiendo remover el text encoder durante la inferencia. Esta decisión arquitectónica, orientada a maximizar la velocidad de despliegue, implica que el módulo de lenguaje es estructuralmente desacoplable del detector visual.

Su documentación oficial documenta tres recetas de fine-tuning (AILab-CVC, 2024). La primera, fine-tuning normal, utiliza MixedGroundingDataset con textos ricos y tareas de grounding, orientada a preservar la capacidad open-vocabulary. La segunda, fine-tuning closed-set, utiliza MultiModalDataset con un JSON de vocabulario fijo, restringiendo las clases detectables al dataset objetivo. La tercera, fine-tuning reparametrizado, remueve el RepVL-PAN y el text encoder, produciendo un modelo con arquitectura equivalente a YOLOv8 pero inicializado con pesos preentrenados a gran escala; esta variante ofrece mayor velocidad pero elimina completamente la capacidad OVD.

Un hallazgo crítico es la fragilidad del text encoder CLIP frente al fine-tuning (Cheng et al., 2024). Se observó que el ajuste del encoder textual CLIP durante el entrenamiento sobre Objects365 produce una caída severa del rendimiento, atribuyendo esta degradación a que el fine-tuning sobre un vocabulario cerrado destruye la capacidad de generalización del encoder. Este resultado sugiere que, en la familia YOLO-World, la preservación de capacidad OVD post-fine-tuning requiere congelar o ajustar con learning rate muy reducido el text encoder, concentrando la adaptación en las capas visuales y en el RepVL-PAN. La evaluación de segmentación open-vocabulary confirma este patrón. Cuando solo se ajusta el head de segmentación, el modelo retiene las capacidades zero-shot adquiridas durante el preentrenamiento; cuando se ajustan todos los módulos, el modelo se adapta mejor al dataset pero puede exhibir degradación de las capacidades zero-shot (Cheng et al., 2024).

YOLOE (Wang et al., 2025) comparte la filosofía de reparametrización y la amplía. Su estrategia RepRTA (Re-parameterizable Region-Text Alignment) permite que, tras el entrenamiento, los parámetros del modelo se reparametricen en un head YOLO estándar, preservando FLOPs y velocidad idénticos a los de YOLOv8 o YOLO11 (Wang et al., 2025). El pipeline de transferencia a datasets de dominio (denominado transferring en la documentación oficial) soporta tanto linear probing (es decir, solo la última convolución del head de clasificación es entrenable) como full tuning (todos los parámetros son entrenables). En ambos casos, el modelo resultante opera como un detector closed-set convencional. La capacidad OVD se preserva únicamente si se mantiene la rama de text prompts o visual prompts activa, lo que requiere configuración específica fuera del pipeline estándar de Ultralytics.

Bloque C: Detectores basados en dual-encoders CLIP-like. OWL-ViT (Minderer et al., 2022) y su sucesor OWLv2 (Minderer et al., 2023) ofrecen una perspectiva diferente sobre la relación entre fine-tuning y capacidad OVD. Estos modelos utilizan encoders de visión y texto preentrenados contrastivamente (CLIP o SigLIP) con heads ligeros de clasificación y localización adjuntos directamente a los tokens de salida del encoder visual. La detección open-vocabulary se habilita reemplazando los pesos fijos de clasificación por los embeddings de texto derivados del encoder lingüístico (Minderer et al., 2022). Dado que la capacidad OVD depende enteramente de la calidad del espacio de embeddings compartido, el fine-tuning sobre datasets cerrados requiere estrategias de regularización para evitar el colapso de dicho espacio. Dichas estrategias ya son proporcionadas por los mismos autores, sobre todo para lograr rendimiento competitivo tanto en detección zero-shot condicionada por texto como en detección one-shot condicionada por imagen (Minderer et al., 2022).

OWLv2 introduce una innovación relevante para el problema de la adaptación de dominio sin fine-tuning manual. Mediante la receta OWL-ST (OWL Self-Training), el modelo utiliza un detector existente para generar pseudo-anotaciones de cajas sobre pares imagen-texto a escala web, entrenándose sobre más de mil millones de ejemplos sin anotaciones humanas adicionales. Este enfoque mejora el AP en categorías raras de LVIS de 31.2% a 44.6% con arquitectura L/14 (Minderer et al., 2023). La selección del espacio de etiquetas para las pseudo-anotaciones resulta determinante. El uso de un vocabulario curado produce buen rendimiento en las clases del vocabulario pero generaliza pobremente a clases y datasets no vistos, mientras que la supervisión débil pero diversa derivada de n-gramas del texto asociado a cada imagen preserva la generalización open-vocabulary (Minderer et al., 2023). Esta evidencia refuerza la observación transversal de que la amplitud y diversidad del vocabulario de entrenamiento es un factor protector de la capacidad OVD.

Bloque D: Modelos generativos guiados por instrucciones. Florence-2 (Xiao et al., 2023) formula todas las tareas de visión como problemas de secuencia a secuencia, utilizando un encoder visual DaViT y un decoder Transformer estándar. Esta arquitectura unificada implica que el fine-tuning afecta al pipeline generativo completo, no a un módulo de fusión localizado. Florence-2 puede fine-tunearse para detección de objetos en entornos no estructurados y desordenados, alcanzando valores de mAP comparables a los de YOLOv8, YOLOv9 y YOLOv10 mediante LoRA y ajuste cuidadoso de capas Transformer (Ucar et al., 2025). La guía de Roboflow para fine-tuning de Florence-2 en detección (Skalski, 2025) reporta que el modelo fine-tuneado retiene parcialmente la capacidad de detectar clases base del preentrenamiento, aunque con rendimiento degradado respecto al modelo original. Los autores de Florence-2 reportan además que el fine-tuning con el encoder de imagen descongelado produce mejoras respecto al enfoque con encoder congelado (Xiao et al., 2023), pero esta estrategia maximiza el riesgo de degradación en categorías no vistas.

Síntesis y tabla comparativa. El análisis transversal revela un patrón consistente. La preservación de la capacidad OVD post-fine-tuning está directamente correlacionada con la profundidad e inextricabilidad de la fusión visión-lenguaje en la arquitectura. Los modelos con fusión profunda y no removible (Grounding DINO) ofrecen mayor resiliencia, dado que el fine-tuning necesariamente opera sobre una arquitectura que integra lenguaje en cada etapa de predicción. Los modelos con módulos de lenguaje removibles o reparametrizables (YOLO-World, YOLOE) tienden a perder capacidad OVD durante el fine-tuning estándar, salvo que se adopten configuraciones específicas de preservación. Los detectores dual-encoder (OWL-ViT/v2) dependen de la integridad del espacio de embeddings compartido y requieren regularización explícita o estrategias de self-training para mantener la generalización. Los modelos generativos (Florence-2) pueden adaptarse a dominios específicos mediante PEFT, pero el impacto sobre categorías no vistas requiere evaluación caso a caso.

La Tabla 4 sintetiza las estrategias de fine-tuning documentadas para los modelos representativos, indicando si preservan la capacidad OVD y las condiciones bajo las cuales lo hacen.

Tabla 4

Estrategias de fine-tuning documentadas y preservación de capacidad OVD por familia arquitectónica


| Familia / Modelo | Estrategia de fine-tuning | Preserva OVD | Condición clave |
| --- | --- | --- | --- |
| Grounding DINO | Fine-tuning closed-set | No | Vocabulario restringido post-ajuste |
| Grounding DINO | Preentrenamiento continuado open-set | Sí | LR reducido; módulos congelados; datos mixtos |
| Grounding DINO | Fine-tuning open-vocabulary (base→novel) | Sí | Evaluación explícita en categorías no vistas |
| Grounding DINO | Adaptación LoRA | Sí | Backbones congelados; solo adapters entrenables |
| YOLO-World | Fine-tuning con MixedGroundingDataset | Parcial | Depende de capas ajustadas; text encoder frágil |
| YOLO-World | Fine-tuning closed-set (MultiModalDataset) | No | Vocabulario fijo en JSON |
| YOLO-World | Reparametrización eficiente (sin RepVL-PAN) | No | Text encoder removido; equivale a YOLOv8 |
| YOLOE | Transferring (linear probing / full tuning) | No | Modelo reparametrizado como YOLO estándar |
| OWL-ViT / OWLv2 | Fine-tuning end-to-end con regularización | Parcial | Requiere estrategias de regularización |
| OWL-ViT / OWLv2 | Self-training (OWL-ST) con pseudo-anotaciones | Sí | Vocabulario diverso (n-gramas) preserva OVD |
| Florence-2 | Fine-tuning con LoRA | Parcial | Retención parcial de clases base; encoder congelado recomendado |

Nota. "Preserva OVD" indica si el modelo resultante puede recibir prompts textuales arbitrarios en inferencia y detectar categorías no vistas durante el fine-tuning. "Parcial" indica preservación dependiente de la configuración específica (capas congeladas, learning rate, datos de entrenamiento). Fuente: Elaboración propia basada en AILab-CVC (2024), Cheng et al. (2024), Liu et al. (2023), Minderer et al. (2022, 2023), Rasaee et al. (2025), Ucar et al. (2025), Wang et al. (2025), Xiao et al. (2023) y Zhao et al. (2024b).

La evidencia sintetizada en la Tabla 4 permite identificar una regularidad en la literatura. La preservación de la capacidad OVD post-fine-tuning depende de tres factores que operan conjuntamente. El primero es la profundidad de la integración visión-lenguaje en la arquitectura, donde los modelos con fusión profunda y no removible exhiben mayor resiliencia que aquellos con módulos de texto desacoplables. El segundo es la estrategia de congelamiento de parámetros, donde las técnicas de ajuste eficiente (LoRA, linear probing, congelamiento selectivo de capas) reducen el riesgo de degradación respecto del ajuste completo de todos los módulos. El tercero es la amplitud y diversidad del vocabulario utilizado durante el fine-tuning, donde los enfoques que mantienen vocabularios ricos o mixtos preservan mejor la generalización que aquellos que restringen el entrenamiento a un conjunto cerrado de categorías. Estos factores no son independientes entre sí, sino que interactúan de manera que las arquitecturas con fusión profunda toleran mejor el ajuste completo, mientras que las arquitecturas con módulos removibles requieren estrategias de preservación más conservadoras para retener capacidad OVD.


#### 15.2.5. Brechas identificadas en el dominio de la construcción civil

A partir de la revisión y síntesis de los enfoques presentados, se pone de manifiesto un conjunto de limitaciones estructurales que no quedan plenamente resueltas por los modelos actuales de detección open-vocabulary. Estas brechas delinean líneas de trabajo relevantes para etapas posteriores del proyecto y permiten anticipar desafíos técnicos que deberán abordarse durante el diseño arquitectónico y la implementación del prototipo.


##### 15.2.5.1. Contextualización semántica limitada

La mayoría de los detectores OVD actuales resuelven la detección como una combinación de localización espacial y compatibilidad textual evaluada de manera independiente para cada región candidata (Zareian et al., 2021; Liu et al., 2023). Este enfoque, aunque efectivo para identificar objetos individuales, no garantiza consistencia contextual entre múltiples entidades detectadas ni permite razonar sobre relaciones espaciales o semánticas entre ellas.

En entornos industriales y de construcción, muchos conceptos relevantes para la seguridad son inherentemente composicionales y dependen del contexto espacial. Condiciones como "persona sin casco cerca de excavación", "operario en zona de tránsito vehicular" o "escalera bloqueando salida de emergencia" requieren no solo detectar cada elemento de manera aislada, sino también evaluar sus relaciones geométricas y semánticas. Los modelos OVD actuales carecen de mecanismos nativos para este tipo de razonamiento relacional, lo que sugiere la necesidad de incorporar módulos adicionales de inferencia contextual o reglas de negocio que operen sobre las detecciones primarias.


##### 15.2.5.2. Ausencia de consistencia temporal nativa

Los modelos de detección open-vocabulary operan predominantemente sobre imágenes estáticas, procesando cada fotograma de manera independiente sin mantener memoria de estados previos ni modelar explícitamente la evolución temporal de las detecciones. Esta característica introduce variabilidad frame-to-frame que puede manifestarse como fluctuaciones en los puntajes de confianza, apariciones y desapariciones espurias de detecciones, e inconsistencias en la asignación de etiquetas entre cuadros consecutivos.

En aplicaciones de vídeo, particularmente aquellas orientadas a monitoreo continuo, esta variabilidad temporal resulta problemática. Los enfoques generativos, como Florence-2, tienden a exhibir mayor inestabilidad debido a la naturaleza autoregresiva de su decodificación (Xiao et al., 2023). La literatura reciente sugiere que la integración con módulos de seguimiento multi-objeto (MOT) constituye una estrategia efectiva para mitigar este problema, permitiendo que el tracker aporte coherencia temporal a las detecciones semánticamente ricas del OVD (Li et al., 2023). No obstante, esta integración introduce complejidad arquitectónica adicional y requiere considerar la compatibilidad entre el detector y el método de tracking seleccionado.


##### 15.2.5.3. Sensibilidad a la formulación del prompt

La flexibilidad semántica que caracteriza a la detección open-vocabulary introduce una dependencia significativa respecto de la formulación exacta de las consultas textuales. Investigaciones en modelos visión-lenguaje han demostrado que pequeños cambios en la redacción de las consultas pueden producir diferencias significativas en el desempeño, incluso cuando diferentes formulaciones refieren al mismo concepto subyacente (Zhou et al., 2022b). Esta sensibilidad tiene implicancias directas para la usabilidad del sistema: usuarios con diferentes niveles de experiencia o distintas convenciones lingüísticas pueden obtener resultados heterogéneos ante objetivos de detección equivalentes.

Esta observación motivó el desarrollo de técnicas de prompt learning, donde los tokens de contexto se reemplazan por vectores aprendibles que se optimizan con datos etiquetados del dominio objetivo (Zhou et al., 2022b; Khattak et al., 2023). Sin embargo, las estrategias desarrolladas para clasificación de imágenes no se transfieren directamente al contexto de detección. Se demostró que la optimización automática de representaciones de prompts —específicamente diseñada para tareas de detección— supera consistentemente a los prompts elaborados mediante ingeniería manual, evidenciando la necesidad de enfoques especializados para el dominio OVD (Du et al., 2022) . Adicionalmente, algunos modelos recientes abordan parcialmente esta limitación mediante el soporte de prompts visuales que permiten anclar la detección a ejemplos concretos en lugar de depender exclusivamente de descripciones textuales (Jiang et al., 2024).


##### 15.2.5.4. Sensibilidad al dominio de aplicación

Los benchmarks estándar utilizados para evaluar modelos OVD —como MS COCO con 80 categorías de objetos cotidianos (Lin et al., 2014) o LVIS con más de 1200 categorías de distribución long-tail (Gupta et al., 2019)— no representan plenamente las condiciones visuales y semánticas de entornos industriales especializados. En el contexto específico de obras de construcción, factores como iluminación extrema, oclusiones frecuentes por maquinaria y estructuras, indumentaria especializada de protección, y presencia de equipamiento industrial introducen distribuciones visuales que difieren significativamente de los datos de preentrenamiento.

Esta brecha de dominio sugiere que, incluso con la capacidad de generalización zero-shot que caracteriza a los modelos OVD, será necesario algún grado de adaptación o calibración para optimizar el rendimiento en el dominio objetivo. Las estrategias potenciales incluyen el ajuste de umbrales de confianza por tipo de escena, la incorporación de filtros de post-procesamiento para falsos positivos recurrentes, y eventualmente el refinamiento ligero (fine-tuning) sobre conjuntos reducidos de imágenes representativas del entorno de obra. No obstante, el fine-tuning en modelos OVD introduce un compromiso entre mejora de rendimiento en categorías vistas y potencial degradación de la capacidad open-vocabulary, cuya intensidad depende de la arquitectura del modelo y de la estrategia de ajuste empleada.


##### 15.2.5.5. Protocolos de evaluación específicos para seguridad industrial

Las métricas de evaluación predominantes en la literatura OVD —como Average Precision (AP) en COCO o LVIS— constituyen indicadores generales de rendimiento que no capturan adecuadamente el valor operativo de un sistema de detección en el contexto de seguridad industrial (Gupta et al., 2019). Estas métricas evalúan la precisión de localización y clasificación frame-by-frame, sin considerar aspectos temporales ni el impacto diferenciado de distintos tipos de error en escenarios de monitoreo de riesgos.

Para validar la plataforma en su dominio de aplicación, resulta necesario diseñar métricas y protocolos de evaluación alineados con los objetivos de seguridad en construcción. Esto incluye considerar la tasa de eventos de riesgo detectados correctamente a lo largo de secuencias de video, el tiempo transcurrido entre el inicio de una condición de riesgo y su detección (latencia de alerta), la tasa de falsas alarmas por unidad de tiempo de monitoreo, y la persistencia mínima requerida para considerar válida una detección.


##### 15.2.5.6. Tabla comparativa de brechas identificadas

Tabla 5

Brechas identificadas en la aplicación de modelos OVD al dominio de seguridad en construcción civil


| Brecha identificada | Descripción | Implicación para el proyecto |
| --- | --- | --- |
| Contextualización semántica limitada | Los modelos OVD detectan entidades localmente pero no infieren relaciones espaciales complejas entre ellas (p. ej., “persona dentro de zona restringida” requiere razonamiento relacional) | El sistema no puede depender exclusivamente del detector para condiciones composicionales; se requieren módulos adicionales de razonamiento contextual |
| Ausencia de consistencia temporal nativa | La detección frame-a-frame introduce variabilidad en puntajes de confianza, apariciones y desapariciones espurias entre cuadros consecutivos | Necesidad de integración con módulo MOT para aportar coherencia temporal a las detecciones semánticas (S. Li et al., 2023) |
| Sensibilidad a la formulación del prompt | Pequeños cambios en la redacción producen diferencias significativas en el desempeño, incluso para conceptos equivalentes (Zhou et al., 2022b) | El diseño de prompts para condiciones de riesgo requiere un proceso sistemático; la selección informal puede comprometer la robustez del sistema |
| Brecha de dominio con benchmarks estándar | MS COCO (80 categorías) y LVIS (1200+ categorías) no representan las condiciones visuales de obras civiles: iluminación extrema, oclusiones por maquinaria, indumentaria especializada (Gupta et al., 2019; Lin et al., 2015) | El desempeño reportado en benchmarks no es directamente transferible al dominio objetivo; se requiere evaluación empírica en condiciones representativas |
| Ausencia de protocolos de evaluación específicos para seguridad industrial | Las métricas AP en COCO/LVIS (Gupta et al., 2019; Lin et al., 2015) no capturan el valor operativo del sistema: no consideran latencia de alerta, persistencia de la detección ni impacto diferenciado de falsos positivos/negativos. | La Etapa 2 del proyecto debe diseñar métricas y protocolos de evaluación alineados con los objetivos de seguridad laboral |

Nota. Las brechas listadas no constituyen limitaciones insalvables, sino desafíos técnicos que definen el espacio de problemas a abordar en las Etapas 2 y 3 del proyecto. Fuente: Elaboración propia basada en las fuentes mencionadas (Gupta et al., 2019; S. Li et al., 2023; Lin et al., 2015; Liu et al., 2023; Zareian et al., 2021; Zhou et al., 2022a, 2022b).


#### 15.2.6. Síntesis de la sección y avance al seguimiento multi-objeto

El análisis de los paradigmas OVD evidencia que la viabilidad de su integración en sistemas de monitoreo continuo está condicionada por cuatro factores: balance entre expresividad semántica y eficiencia de inferencia, diseño sistemático de prompts para el dominio específico, mecanismos de compensación de la variabilidad temporal frame-a-frame, y evaluación empírica en condiciones visuales de construcción civil. Los dos últimos factores remiten directamente al problema de persistencia temporal: dado que la OVD produce observaciones instantáneas sin identidad ni continuidad, la sección siguiente analiza los métodos de seguimiento multiobjeto como mecanismo para sostener esas detecciones a lo largo del tiempo


### 15.3. Seguimiento multiobjeto: métodos, métricas y brechas del estado del arte

El seguimiento multiobjeto (MOT) constituye el mecanismo que transforma las detecciones instantáneas producidas por el sistema OVD en trayectorias persistentes a lo largo del tiempo, habilitando la agregación temporal de evidencias necesaria para la generación de alertas operativas. En esta sección se analizan los métodos representativos del estado del arte en MOT para sistemas de video en tiempo real, las métricas de evaluación relevantes para el contexto del proyecto y las brechas identificadas en la intersección entre MOT y detección open-vocabulary.


#### 15.3.1. Métodos Representativos

El estado del arte en MOT para sistemas de video en tiempo real está dominado por la familia SORT extendida, cuya evolución refleja el progreso en el manejo de oclusiones, la explotación de detecciones de baja confianza y la eliminación de dependencias de entrenamiento específico por dominio.


##### 15.3.1.1. SORT

SORT (Simple Online and Realtime Tracking) establece el esquema de referencia del paradigma tracking-by-detection moderno. Combina el filtro de Kalman para el modelado del movimiento con el algoritmo Húngaro para la asignación óptima de detecciones a trayectorias, utilizando IoU como única métrica de similitud. Su diseño minimalista prescinde de cualquier modelado de apariencia, lo que resulta en latencia muy baja —capacidad de operar a tasas superiores a 200 FPS— y ausencia total de dependencias de entrenamiento. La principal limitación de SORT es su baja robustez ante oclusiones: cuando un objeto no es detectado durante varios cuadros consecutivos, la trayectoria se termina y la re-asociación posterior puede producir un cambio de identificador (ID switch), fragmentando la trayectoria en múltiples segmentos (Bewley et al., 2016).


##### 15.3.1.2. DeepSORT

DeepSORT extiende SORT incorporando el modelado de apariencia descrito en el análisis del modelado de apariencia, con el objetivo de mitigar las ambigüedades de asociación en presencia de oclusiones y cruces (Wojke et al., 2017). En términos operativos, mantiene el marco de predicción de movimiento y validación cinemático-estadística, pero introduce un término adicional de similitud visual basado en embeddings extraídos por una red neuronal, integrando la evidencia de movimiento y apariencia en la función de costo de asociación (Wojke et al., 2017).

La consecuencia directa es una reducción significativa de cambios de identidad y una mayor capacidad de re-asociación tras desapariciones temporales, particularmente en secuencias con oclusiones parciales o alta densidad de objetos. Sin embargo, este aumento de robustez implica mayores requerimientos computacionales y dependencia de un modelo de re-identificación entrenado. En aplicaciones estrictamente en tiempo real, esta dependencia puede degradar el rendimiento si no se optimiza adecuadamente el extractor de características. Asimismo, en entornos open-vocabulary dinámicos, la dependencia de embeddings entrenados con dominios específicos puede introducir restricciones adicionales o degradaciones cuando el dominio visual o las categorías observadas se alejan del régimen de entrenamiento (Wojke et al., 2017).


##### 15.3.1.3. ByteTrack

ByteTrack introduce una innovación conceptualmente simple pero con impacto significativo sobre la robustez del tracker: en lugar de descartar las detecciones por debajo de un umbral de confianza del detector —como hace SORT—, las utiliza en una segunda etapa de asociación para mantener la continuidad de trayectorias existentes. La idea central es que una detección de baja confianza en el cuadro t puede corresponder a un objeto parcialmente ocluso cuya trayectoria fue establecida en cuadros anteriores; descartarla produce una fragmentación innecesaria. La asociación se estructura en dos pasos jerárquicos: primero se asocian las detecciones de alta confianza con las trayectorias activas; luego, las trayectorias no asociadas se intentan conectar con las detecciones de baja confianza. ByteTrack mantiene la ausencia de modelos de apariencia y logra tasas de inferencia superiores a 170 FPS, siendo directamente compatible con detectores one-stage como YOLO-World (Adžemović, 2025; Y. Zhang et al., 2022).


##### 15.3.1.4. OC-SORT

OC-SORT (Observation-Centric SORT) aborda una limitación distinta de SORT: la degradación del modelo de movimiento durante los períodos de oclusión. En SORT, cuando un objeto no es detectado durante varios cuadros, el filtro de Kalman continúa actualizando el estado interno basándose únicamente en predicciones del modelo dinámico, acumulando error de estimación que se manifiesta en asociaciones incorrectas cuando el objeto reaparece. OC-SORT introduce dos correcciones principales: el Observation-Centric Momentum (OCM), que estima la dirección y magnitud del movimiento del objeto a partir de sus observaciones históricas en lugar de basarse en las predicciones del filtro, y el Observation-Centric Re-Update (OCR), que reajusta las estimaciones del filtro utilizando las observaciones reales durante los períodos de oclusión. Estas correcciones reducen los ID switches sin incorporar modelos de apariencia ni incrementar significativamente el costo computacional (Cao et al., 2023).


##### 15.3.1.5. BoT-SORT y métodos end-to-end

BoT-SORT (Aharon et al., 2022) representa un punto de convergencia entre la eficiencia de ByteTrack y la robustez de DeepSORT: incorpora embeddings de apariencia, compensación de movimiento de cámara (CMC) mediante homografía, y la estrategia de asociación jerárquica de ByteTrack. Este diseño maximiza la precisión en benchmarks a costa de una mayor complejidad computacional y la dependencia de un modelo ReID preentrenado, posicionándolo como una opción de alta precisión cuando la robustez prima sobre la latencia.

En el extremo opuesto del espectro de complejidad, los enfoques end-to-end basados en Transformers —como TrackFormer (Meinhardt et al., 2022) y MOTR— formulan el tracking como un problema de predicción conjunta de detecciones y asociaciones en una única red entrenada conjuntamente. Si bien estas arquitecturas ofrecen ventajas teóricas en términos de coherencia global del pipeline, sus altos requisitos computacionales, la complejidad del entrenamiento conjunto y la limitada flexibilidad para integrar detectores OVD externos hacen que su adopción en sistemas experimentales de tiempo real sea actualmente limitada (Adžemović, 2025).


#### 15.3.2. Síntesis comparativa de métodos MOT

La Tabla 6 sintetiza las características principales de los métodos MOT analizados, con énfasis en las dimensiones más relevantes para su integración en el sistema E-OVRT-VDP: paradigma, modelo de movimiento, estrategia de asociación, robustez ante oclusiones, latencia y dependencias de entrenamiento.

Tabla 6

Síntesis comparativa de métodos MOT representativos según dimensiones relevantes para sistemas de video en tiempo real con detección open-vocabulary


| Método | Paradigma | Modelo de movimiento | Asociación de datos | Robustez a oclusiones | Latencia / FPS | Dependencia de entrenamiento |
| --- | --- | --- | --- | --- | --- | --- |
| SORT | Tracking-by- detection | Kalman lineal | IoU + Húngaro | Baja | Muy alta (>200 FPS) | Ninguna |
| DeepSORT | Tracking-by- detection | Kalman lineal | Cascada: movimiento + apariencia | Media-Alta | Media | Modelo ReID preentrenado |
| ByteTrack | Tracking-by- detection | Kalman lineal | Jerárquica: alta/baja confianza + IoU | Alta | Muy alta (>170 FPS) | Ninguna |
| OC-SORT | Tracking-by- detection | Kalman + correcciones OC | IoU + consistencia de momento (OCM) | Media-Alta | Muy alta | Ninguna |
| BoT-SORT | Tracking-by- detection | Kalman mejorado + CMC | Fusión IoU-ReID | Alta | Media | Modelo ReID preentrenado |
| TrackFormer / MOTR | End-to-end (Transformer) | Atención temporal aprendida | Mecanismo de atención global | Muy alta | Baja | Entrenamiento conjunto requerido |

Nota. CMC = Compensación de Movimiento de Cámara (Camera Motion Compensation). OC = Observation-Centric. La columna 'Dependencia de entrenamiento' refiere a componentes adicionales al detector base que requieren entrenamiento supervisado. FPS estimados corresponden a las configuraciones reportadas en los trabajos originales sobre hardware de referencia; pueden variar significativamente según el hardware y la resolución de entrada. Fuente: Elaboración propia basada en las fuentes citadas (Adžemović, 2025; Aharon et al., 2022; Bewley et al., 2016; Cao et al., 2023; Wojke et al., 2017; Y. Zhang et al., 2022).


##### 15.3.2.1. Observaciones críticas sobre la comparativa

La comparativa evidencia que los métodos de tracking-by-detection puramente geométricos, como SORT, ByteTrack y OC-SORT, presentan una mayor compatibilidad con detectores open-vocabulary, ya que no dependen de modelos de apariencia entrenados en dominios específicos y permiten desacoplar el detector del módulo de seguimiento. Esta propiedad resulta especialmente relevante en sistemas donde las clases de interés pueden variar dinámicamente según las consultas del usuario y donde se requiere sustituir modelos sin reentrenamiento. En términos operativos, se observa un trade-off entre velocidad y robustez: los métodos geométricos alcanzan altas tasas de procesamiento y menor latencia, aunque son más sensibles a oclusiones prolongadas, mientras que enfoques como DeepSORT o BoT-SORT mejoran la estabilidad de identidades mediante embeddings visuales, a costa de mayor carga computacional. Por su parte, los métodos end-to-end como FairMOT o TrackFormer ofrecen integración profunda entre detección y seguimiento, pero su necesidad de entrenamiento conjunto limita la flexibilidad requerida por pipelines OVD modulares. En este marco, ByteTrack y OC-SORT representan alternativas particularmente equilibradas, al introducir mejoras sobre SORT —asociación de detecciones de baja confianza y correcciones observation-centric— sin perder eficiencia computacional. Por ello, para una plataforma experimental de detección open-vocabulary en tiempo real, la familia SORT extendida se presenta como la opción más adecuada, al combinar independencia del detector, bajo costo computacional, robustez suficiente y mayor transparencia para la iteración, auditoría y diagnóstico de fallos.


#### 15.3.3. Métricas de evaluación para MOT

La evaluación del desempeño de algoritmos MOT requiere métricas estandarizadas que capturen diferentes aspectos del problema: precisión de detección, consistencia de identidad y localización espacial. Las tres métricas principales en la literatura son MOTA, IDF1 y HOTA, cada una con sesgos y alcances distintos que hacen necesaria su interpretación conjunta (Luiten et al., 2021).


##### 15.3.3.1. MOTA (Multiple Object Tracking Accuracy)

MOTA es la métrica clásica de evaluación MOT. Se define como: MOTA = 1 − (FN + FP + IDSW) / GT, donde FN son falsos negativos, FP son falsos positivos, IDSW son cambios de identidad, y GT es el total de objetos ground truth. MOTA está sesgada hacia medir la precisión de detección, penalizando fuertemente los errores de detección sobre los errores de asociación (Bernardin & Stiefelhagen, 2008).


##### 15.3.3.2. IDF1 (Identification F1-Score)

IDF1 se enfoca en la consistencia de identidad a largo plazo. Calcula el F1-score entre detecciones verdaderas positivas que mantienen la identidad correcta. IDF1 está sesgada hacia medir la asociación, a expensas de ignorar mejoras en la detección (Ristani et al., 2016).


##### 15.3.3.3. HOTA (Higher Order Tracking Accuracy)

HOTA surge como respuesta a las limitaciones de MOTA e IDF1. HOTA balancea explícitamente la precisión de detección y asociación mediante la fórmula:


|  | (1) |
| --- | --- |

donde DetA es la precisión de detección y AssA es la precisión de asociación (Luiten et al., 2021). HOTA también incorpora la precisión de localización, ausente en MOTA e IDF1. La métrica ha sido adoptada por los principales benchmarks como MOTChallenge y se recomienda para evaluaciones comprehensivas de trackers modernos.

Sin embargo, las tres métricas presentan una limitación común para el dominio de seguridad laboral: evalúan el desempeño del tracker de manera agnóstica al valor operativo de cada tipo de error. Un ID switch en una trayectoria de persona dentro de zona restringida tiene un impacto operativo muy diferente a un ID switch en una trayectoria de maquinaria estacionaria, pero ambos contribuyen de manera idéntica al cómputo de MOTA o HOTA. Esta homogeneización del error es incompatible con los requisitos de un sistema de alerta cuya efectividad depende de distinguir entre tipos de error con consecuencias asimétricas. La consolidación metodológica posterior del proyecto deberá abordar el diseño de criterios de evaluación complementarios alineados con los objetivos de seguridad laboral.


#### 15.3.4. Brechas identificadas y desafíos para el prototipo

El análisis del estado del arte en MOT revela un conjunto de brechas que condicionan el diseño del prototipo y las decisiones metodológicas de la consolidación metodológica posterior. La Tabla 7 organiza estas brechas con su descripción técnica y su implicación específica para el proyecto.

Tabla 7

Brechas identificadas en la aplicación de métodos MOT al contexto de seguridad en construcción civil en combinación con detección open-vocabulary


| Brecha identificada | Descripción | Implicación para el proyecto |
| --- | --- | --- |
| Dependencia de la calidad del detector subyacente | El rendimiento del MOT está fuertemente acoplado al desempeño del detector. Errores de detección —FP, FN, bounding boxes inestables— se propagan al tracking, produciendo fragmentación de trayectorias, pérdidas de identidad y asociaciones erróneas (S. Li et al., 2025) | En el pipeline OVD + MOT, la variabilidad inherente de la detección open-vocabulary puede amplificar errores de asociación; el diseño del sistema debe contemplar estrategias de filtrado y umbralización que reduzcan el ruido de entrada al tracker |
| Fragilidad ante oclusiones prolongadas | Aunque los métodos modernos manejan oclusiones breves, las oclusiones de larga duración producen terminación prematura de trayectorias, re-asociaciones inciertas y aumento de ID switches (Du et al., 2024) | En entornos de obra civil con alta densidad de obstrucciones (andamios, maquinaria, materiales), la robustez ante oclusiones es una restricción de diseño relevante que debe evaluarse empíricamente |
| Ausencia de semántica en los identificadores de tracking | Los identificadores asignados por MOT son puramente internos y efímeros: no persisten entre sesiones, cámaras ni reinicios del sistema (Du et al., 2024) | El sistema no puede utilizar el tracking para correlación inter-cámara sin mecanismos adicionales; las alertas basadas en persistencia de identidad quedan limitadas al contexto temporal inmediato de cada flujo de video |
| Métricas estándar no alineadas con objetivos operativos de seguridad | Las métricas MOTA, IDF1 y HOTA evalúan el desempeño del tracking frame-a-frame sin considerar el impacto operativo diferenciado de distintos tipos de error en el contexto de seguridad laboral (Luiten et al., 2021) | Se deben definir criterios de evaluación del componente MOT alineados con el dominio: persistencia mínima para disparar alertas, penalización diferenciada de ID switches en condiciones de riesgo, y tolerancia ante falsos positivos por oclusión |
| Ausencia de datasets de construcción con anotaciones de tracking | Los benchmarks estándar de MOT (MOT17, MOT20, DanceTrack) no contemplan el dominio de obras civiles; la evaluación del tracker en condiciones representativas requiere datos del dominio específico (Dendorfer et al., 2020; Milan et al., 2016) | La validación del componente MOT en el prototipo no puede apoyarse en benchmarks estándar; se requiere la definición de un protocolo de evaluación propio con datos recopilados en el contexto del proyecto |

Nota. Las brechas listadas definen el espacio de problemas abiertos que deben abordarse en el diseño experimental (etapa 2) y en la implementación del prototipo (etapa 4). Fuente: Elaboración propia basada en las fuentes citadas (Adžemović, 2025; Dendorfer et al., 2020; Du et al., 2024; S. Li et al., 2025; Luiten et al., 2021; Milan et al., 2016).

La brecha de ausencia de datasets de construcción con anotaciones de tracking merece una consideración adicional. Los benchmarks estándar de MOT —MOT17, MOT20, DanceTrack— fueron diseñados para escenarios de peatones en entornos urbanos y eventos de danza respectivamente, con distribuciones visuales que difieren significativamente de una obra civil: densidad de cámara fija en planos elevados, entidades heterogéneas (personas, maquinaria, materiales), indumentaria de protección que puede confundir a los modelos de apariencia, y configuraciones de oclusión determinadas por la geometría de la obra. Esta brecha no puede resolverse mediante adaptación de los benchmarks existentes; requiere la definición de un protocolo de evaluación propio que se apoyará en los datos recopilados durante la fase experimental del proyecto.


### 15.4. Video en tiempo real y streaming: protocolos, servidores y brechas del estado del arte


#### 15.4.1. Protocolos de transmisión de video de baja latencia

Los protocolos de transmisión de vídeo constituyen un componente relevante dentro del análisis de sistemas de vídeo en tiempo real, debido a que condicionan la forma en que los flujos provenientes de cámaras o fuentes de vídeo son transportados hacia los módulos de procesamiento, visualización o almacenamiento. En el contexto del presente proyecto, su estudio resulta necesario porque la detección open-vocabulary no opera sobre imágenes aisladas, sino sobre secuencias continuas que deben ser recibidas, decodificadas y procesadas con una latencia compatible con la generación oportuna de alertas.

Desde una perspectiva general, los protocolos de streaming pueden diferenciarse por dimensiones como el modelo de entrega, el esquema de distribución, la tolerancia a pérdidas, los mecanismos de buffering y el orden de magnitud de latencia que suelen alcanzar bajo determinadas condiciones de red y configuración. Sin embargo, estos valores no deben interpretarse como propiedades absolutas de cada protocolo, ya que la latencia final depende del pipeline completo: captura, codificación, transporte, decodificación, inferencia, evaluación de patrones y comunicación de resultados. Estos componentes serán retomados con mayor detalle en el marco teórico y en la descripción técnica del sistema, donde se analizará su impacto dentro de la arquitectura experimental.

En esta sección, el análisis se limita a revisar los protocolos y familias de transmisión más relevantes para aplicaciones de baja latencia, identificando sus características principales, sus restricciones prácticas y su grado de compatibilidad con un sistema de análisis automatizado de vídeo. Esta revisión permite establecer criterios preliminares para la selección posterior del stack de medios, sin definir todavía una implementación definitiva.


##### 15.4.1.1. Criterios de clasificación de protocolos

Modelo de entrega push. En el modelo push, una vez establecida la sesión, el emisor entrega el flujo de manera continua hacia el receptor (típicamente sobre UDP o sobre una sesión persistente), minimizando esperas asociadas a la solicitud de unidades discretas de contenido. Protocolos de tiempo real, como RTP y flujos interactivos como WebRTC, se alinean más naturalmente con push (ISO/IEC, 2022; May, 2017a).

Modelo de entrega pull. En el modelo pull, el control de la entrega reside principalmente en el cliente: el receptor solicita (por HTTP) segmentos o partes de segmentos en forma sucesiva, habilitando escalabilidad y cacheo, pero introduciendo buffering y latencias asociadas a segmentación y recarga. Los esquemas adaptativos sobre HTTP, como HLS y MPEG-DASH, responden al patrón pull (cliente-driven).

Esquema de distribución unicast. En unicast, cada cliente mantiene una conexión individual y recibe un flujo dedicado, lo que simplifica control por receptor (adaptación, seguridad, métricas), pero escala el consumo de ancho de banda en el emisor.

Esquema de distribución multicast. En multicast, el emisor envía un único flujo a un grupo multicast y la red replica hacia múltiples receptores, siendo eficiente en redes administradas. Protocolos basados en RTP pueden operar sobre unicast o multicast; sin embargo, el multicast IP no es viable en Internet abierta (en general no es ruteable extremo-a-extremo y complica control de congestión por receptor).

Orden de magnitud de latencia. Otra forma práctica de categorizar protocolos es por la latencia end-to-end típica que habilitan bajo configuraciones habituales. En términos operativos pueden distinguirse tres rangos:

Alta latencia (>~3 s). Protocolos orientados a distribución masiva y robustez. Aquí se ubican implementaciones “clásicas” de HLS y MPEG-DASH con segmentos de varios segundos. Al apoyarse en HTTP/HTTPS y CDN, priorizan escalabilidad y tolerancia a fallos, usualmente con latencias del orden de varios segundos a decenas de segundos (ISO/IEC, 2022; May, 2017a).

Latencia media (~0,5 a 3 s). Incluye protocolos como RTMP (en ingesta), RTSP cuando se opera con buffers conservadores o sobre TCP, y variantes de baja latencia de HLS/DASH basadas en segmentación fina y entrega parcial.

Baja latencia (<~500 ms). Protocolos diseñados para interactividad estricta y respuesta casi en tiempo real: WebRTC, SRT, RIST y flujos RTP con mínima capa de sesión. En general emplean UDP para evitar la penalidad de retransmisiones fuera de plazo y operan con buffers pequeños, compensando la pérdida con estrategias específicas (p. ej., ARQ “dentro de un presupuesto de tiempo” en SRT/ RIST). En WebRTC, además, la conectividad extremo-a-extremo depende de mecanismos de traversal NAT como ICE, que influyen en la latencia efectiva según el tipo de red (Keranen et al., 2018; Nakagawa et al., 2021; Schulzrinne et al., 2003b; M. P. Sharabayko et al., 2024; Video Services Forum, 2020).


##### 15.4.1.2. Mapa de familias de protocolos según los criterios de clasificación

En esta sección, se analizan los protocolos más relevantes aplicando sistemáticamente (i) modelo de entrega, (ii) esquema de distribución y (iii) latencia típica, además de consideraciones prácticas pertinentes a cada protocolo (NAT, resiliencia, seguridad, tooling).

RTSP/RTP: El estándar de cámaras IP industriales. El Real-Time Streaming Protocol (RTSP) es un protocolo de capa de aplicación orientado al control de sesiones de streaming. Fue especificado inicialmente en el RFC 2326 (Schulzrinne et al., 1998a) y posteriormente revisado en RTSP 2.0 mediante el RFC 7826, dejando obsoleta la versión original (Schulzrinne et al., 2016). En términos funcionales, RTSP opera como plano de control: define cómo un cliente describe una sesión, negocia parámetros y ejecuta acciones de control, mientras que el transporte del audio y el video no suele ocurrir en RTSP sino en un protocolo de medios separado. RTSP mantiene estado de sesión y utiliza comandos bidireccionales con sintaxis similar a HTTP.

En este esquema, el transporte de medios suele realizarse con el Real-time Transport Protocol (RTP), definido en el RFC 3550, acompañado por RTCP que informa métricas como pérdida y jitter, útiles para diagnóstico y sincronización (Schulzrinne et al., 2003b). RTP se encapsula típicamente sobre UDP e incorpora cabeceras con timestamps y números de secuencia para facilitar la reconstrucción temporal del flujo, la sincronización entre medios y el manejo del jitter en el receptor..

RTSP/RTP se adoptó ampliamente en entornos industriales y de videovigilancia por su compatibilidad y madurez, y su uso se encuentra alineado con especificaciones del ecosistema IP de seguridad, como ONVIF Profile S, donde RTSP aparece como componente central para consumo/control de streams (ONVIF, 2019). Operativamente, la combinación RTSP/RTP es particularmente conveniente en redes controladas (LAN) por su eficiencia cuando se usa UDP; no obstante, en escenarios con NAT y firewalls puede aparecer fricción por la necesidad de múltiples flujos/puertos para RTP/RTCP. Para mitigar este problema, RTSP contempla la posibilidad de transportar RTP/RTCP interleaved sobre la misma conexión TCP, simplificando el cruce de firewalls, aunque introduciendo trade-offs propios de TCP (por ejemplo, mayor sensibilidad a variaciones y efectos de bloqueo por orden) (Schulzrinne et al., 1998a, 2016). En términos de puertos, el registro de IANA asocia comúnmente rtsp con 554/TCP y 554/UDP, y rtsps con 322/TCP y 322/UDP, aunque en la práctica los vendors pueden operar con puertos alternativos por configuración (Internet Assigned Numbers Authority, s/f).

En cuanto a latencia, es importante explicitar un criterio: los valores reportados para un protocolo son rangos típicos observados y no compromisos del estándar. Ni RTSP ni RTP garantizan un valor en específico. La latencia end-to-end (glass-to-glass) se ve dominada por el pipeline completo (captura, codificación, red, decodificación) y, de manera muy marcada, por el buffer del receptor y las políticas del cliente de reproducción. En literatura técnica de videovigilancia se describe explícitamente que múltiples etapas suman retardo y que el play-out buffer puede convertirse en un componente dominante, elevando la latencia para priorizar estabilidad ante jitter (Axis Communications AB, 2015). Bajo condiciones favorables, RTSP/RTP puede operar con latencias del orden de cientos de milisegundos (por ejemplo, ~200–800 ms). En despliegues reales con Video Management Software (VMS), donde se prioriza continuidad y tolerancia a variaciones de red, es frecuente observar valores que suben a 1.000–2.000 ms o más, configurados explícitamente por buffering y por el comportamiento del cliente (Axis Communications AB, 2015).

RTMP: El protocolo de ingesta dominante de la era Flash. El Real-Time Messaging Protocol (RTMP) fue impulsado históricamente por el ecosistema Flash y, aunque Flash Player quedó oficialmente descontinuado (fin de soporte el 31/12/2020 y bloqueo de contenido desde el 12/01/2021), RTMP sigue teniendo un rol vigente como protocolo de ingesta hacia plataformas y servidores de streaming (Adobe, 2021; Twitch Developers, s/f). Conceptualmente, RTMP se apoya sobre TCP y establece una conexión persistente en la que viajan audio, video y datos de control multiplexados; el diseño incorpora un mecanismo de “chunking” para intercalar flujos y sostener continuidad de entrega: el tamaño máximo de chunk por defecto es 128 bytes, aunque puede renegociarse mediante mensajes de control (Parmar & Thornburgh, 2012). En la práctica operativa, suele utilizar el puerto 1935 (por defecto), y existen variantes para atravesar restricciones de red, como RTMPS (RTMP sobre TLS) o tunelado por HTTP (The FFmpeg developers, s/f-b).

Desde el punto de vista de arquitectura, RTMP se comporta como un canal “siempre abierto” entre codificador (OBS/encoder/cámara) y servidor/plataforma, en el que la sesión intercambia comandos y metadatos además de los paquetes de medios (Parmar & Thornburgh, 2012). Esa persistencia simplifica la ingesta en escenarios clásicos de broadcasting, y explica por qué muchas plataformas todavía aceptan RTMP como entrada aunque distribuyan al público con otros formatos; por ejemplo, Twitch describe explícitamente que el envío hacia su infraestructura se realiza usando RTMP (Twitch Developers, s/f).

En latencia, RTMP suele ubicarse en un rango “bajo” comparado con protocolos segmentados, pero no es ultra-bajo en sentido estricto: en implementaciones reales, es común observar ~2–5 s (2000–5000 ms) de glass-to-glass en configuraciones típicas, muy influido por el buffering del reproductor y por la estabilidad de la red (Roy (Whalen), 2024).

Además, varios stacks incorporan buffers explícitos del lado cliente/encoder: por ejemplo, en tooling común se expone un “client buffer time” configurable y con valores por defecto del orden de 3000 ms (The FFmpeg developers, s/f-b). Esto es clave para la plantilla: cuando el documento menciona latencias, debe quedar claro que el número final no es una propiedad “fija” del protocolo, sino la resultante del buffering + RTT/jitter + códec + política de retransmisión de TCP.

En cuanto a vigencia y compatibilidad, el motivo principal por el que RTMP persiste es pragmático: es un “idioma común” de ingesta para encoders y plataformas. Sin embargo, para un diseño nuevo orientado a tiempo real, sus límites aparecen rápido ya que, al estar sobre TCP, en presencia de pérdida/jitter el comportamiento de retransmisión puede traducirse en demoras variables (latencia “elástica”), y en general no ofrece, por sí mismo, garantías modernas de resiliencia/recuperación orientadas a tiempo real como las que hoy se buscan con alternativas basadas en UDP (p. ej., SRT/WebRTC en otras secciones). En paralelo, también hay un punto de “futuro del ecosistema”: RTMP tiene una especificación publicada y ampliamente implementada, pero su evolución no siguió una trayectoria de estandarización comparable a los RFCs, y buena parte de su protagonismo histórico estuvo atado a Flash (Adobe, 2021; Parmar & Thornburgh, 2012).

Respecto de códecs, el RTMP “clásico” se consolidó como baseline interoperable en FLV con H.264/AAC, y plataformas documentan RTMP/RTMPS con soporte típico de H.264 como opción compatible (Parmar & Thornburgh, 2012). Aun así, el estado del arte se está moviendo: especificaciones como Enhanced RTMP/Enhanced FLV proponen extensiones (incluida señalización por FOURCC) para habilitar códecs modernos como HEVC y AV1, y tooling ampliamente usado ya lo implementa en escenarios acotados (p. ej., OBS con Enhanced RTMP en beta para YouTube). Por lo tanto, es más preciso afirmar que la limitación es principalmente de interoperabilidad y soporte homogéneo (encoder + servidor + plataforma) que una imposibilidad conceptual absoluta.

Protocolos HTTP adaptativos: HLS, MPEG-DASH y CMAF. Las tecnologías de streaming adaptativo sobre HTTP se consolidaron como estándar para distribuir vídeo a grandes audiencias por su escalabilidad y porque reutilizan infraestructura web existente (CDN, proxies, cachés y firewalls “amigables” con HTTP). En esta familia, HLS y MPEG-DASH comparten la idea central de “segmentar + describir en un manifiesto + descargar por HTTP”, y CMAF aparece como pieza clave para reducir duplicación de contenedores y habilitar variantes de baja latencia. Sin embargo, incluso en sus modos “low latency”, suelen ubicarse en el rango de latencia de pocos segundos, muy por encima de los protocolos de ultra-baja latencia orientados a interactividad estricta.

HTTP Live Streaming (HLS). Define un esquema en el cual el contenido se publica como una secuencia de segmentos (históricamente MPEG-TS, y en implementaciones modernas también fMP4/CMAF) y se expone un manifiesto (playlist M3U8) para que el cliente los descargue y reproduzca en orden (May, 2017a). En su configuración “clásica”, la latencia tiende a ser elevada porque el cliente suele mantener un buffer de seguridad y porque los segmentos suelen tener duraciones de varios segundos; el propio RFC 8216 describe el modelo de “segmentos + playlist” y un comportamiento típico de segmentación que, en la práctica, deriva en latencias del orden de decenas de segundos dependiendo del empaquetado y del reproductor (May, 2017a).

Con Low-Latency HLS (LL-HLS) el objetivo es reducir la latencia sin abandonar HTTP/CDN, principalmente habilitando la entrega “temprana” de contenido antes de que el segmento completo esté terminado. Este comportamiento está especificado en la evolución del estándar, incorporando mecanismos como partial segments (PART), recargas bloqueantes del playlist y señales para “preanunciar” contenido próximo (Pantos, 2025). En términos prácticos, LL-HLS puede configurarse para emitir “partes” muy cortas —por ejemplo, del orden de ~200 ms— que el cliente puede comenzar a consumir apenas se codifican, sin esperar el cierre del segmento completo (Apple Developer, s/f). Importante: esos 200 ms son un tamaño de “parte/chunk” (granularidad de publicación), no la latencia end-to-end total; la latencia final depende también de parámetros como el hold-back del reproductor, el buffer mínimo, la cadencia de actualización del playlist, la latencia de codificación (GOP), y la red. En presentaciones técnicas de Apple sobre LL-HLS se reporta la posibilidad de lograr streaming “casi en vivo” con latencias sub-2s en escenarios optimizados, precisamente gracias a este enfoque de entrega incremental sobre HTTP (Apple Developer, 2019).

MPEG-DASH (ISO/IEC 23009-1). Cuenta con un manifiesto (MPD) que describe representaciones (bitrate/resolución) y el cliente descarga segmentos por HTTP, permitiendo adaptación dinámica. Su modo de baja latencia se apoya en CMAF y en técnicas de entrega temprana (por ejemplo, HTTP chunked transfer) para que el reproductor pueda empezar a consumir el segmento mientras se produce. Documentos de la industria (DASH-IF) definen explícitamente el objetivo de “low-latency service offering” con una latencia objetivo típicamente entre 2 y 10 segundos, manteniendo compatibilidad con CDN y con clientes legacy que seguirían reproduciendo con más delay si no soportan el modo LL (DASH Industry Forum, 2020). Esto vuelve a reforzar la idea clave: en HTTP adaptativo, la baja latencia es “baja” en términos OTT (segundos), no en términos de interactividad estricta (centenas de ms).

CMAF (ISO/IEC 23000-19). No es un protocolo sino un formato contenedor y de segmentación basado en fragmented MP4, pensado para que un mismo set de fragmentos/segmentos sea utilizable tanto por HLS como por DASH, reduciendo duplicaciones y facilitando interoperabilidad. En el contexto de baja latencia, CMAF permite estructurar el contenido en unidades más pequeñas (chunks/fragments) que pueden ser decodificables progresivamente; por ejemplo, en materiales técnicos vinculados a perfiles DVB/DASH se ven parámetros que acotan la duración máxima de un “chunk” a ~500 ms en ciertos esquemas de señalización, nuevamente como granularidad de entrega y no como garantía de latencia end-to-end (Law, 2020). En otras palabras: que el sistema “empaquete” en 200 ms o 500 ms ayuda, pero la latencia total sigue estando dominada por decisiones de pipeline y buffers de reproducción.

Ventajas y limitaciones. HLS/DASH (y sus variantes LL sobre CMAF) siguen siendo imbatibles para distribución masiva y robusta —aprovechan CDNs, se comportan bien con firewalls y permiten bitrate adaptativo—, pero pagan el costo de una latencia que, aún optimizada, suele quedar en pocos segundos.

WebRTC: Ultra-baja latencia para aplicaciones interactivas. Web Real-Time Communication (WebRTC) no es un protocolo único, sino una pila completa de estándares y APIs orientada a comunicación de audio/video en tiempo real, nacida en el contexto del navegador pero extendida hoy a SDKs móviles y servidores. A nivel de estandarización, WebRTC se apoya en un conjunto de especificaciones IETF (por ejemplo, el documento de visión general y la definición de transportes) y en la API JavaScript normalizada por W3C, que expone primitivas como RTCPeerConnection para establecer sesiones de comunicación con latencias típicamente sub-segundo cuando la red lo permite (World Wide Web Consortium, 2025).

En términos funcionales, WebRTC resuelve “de punta a punta” (en el sentido de la pila de comunicación) tres problemas que otros enfoques suelen delegar a componentes externos: (1) negociación de conectividad en presencia de NAT/firewalls, (2) transporte de medios en tiempo real sobre UDP con control de congestión y métricas de calidad, y (3) cifrado obligatorio del canal de medios. Esta integración es relevante para casos donde la latencia es prioritaria y donde la operación ocurre en redes variables (obra, 4G/5G, Wi-Fi corporativo), porque evita depender de segmentación HTTP y reduce buffering estructural.

La arquitectura base combina señalización (fuera de banda) con transporte de medios. WebRTC utiliza SDP con el modelo offer/answer para describir capacidades (códecs, direcciones, parámetros), pero el “plano de señalización” no está fijado por WebRTC y queda en manos de la aplicación (HTTP, WebSocket, MQTT, etc.). En la práctica, el estándar JSEP define cómo una aplicación JavaScript controla esa máquina de estados de establecimiento y aplica las descripciones SDP a la conexión, manteniendo la flexibilidad de integrar WebRTC en arquitecturas más grandes sin imponer un protocolo de señalización único.

En la capa de conectividad, WebRTC se apoya en ICE para atravesar NAT, usando STUN para descubrir direcciones públicas y TURN como relé cuando no hay ruta directa viable. ICE está estandarizado en RFC 8445 y, además, la especificación de transportes de WebRTC explicita requerimientos de soporte (incluyendo el uso de TURN para escenarios de NATs restrictivos), lo que lo vuelve un “supuesto operativo” del stack y no un agregado opcional.

Respecto de la latencia —bajo el marco conceptual desarrollado en la sección 16.5.1— conviene distinguir dos métricas que suelen confundirse: el RTT de red (ida y vuelta de paquetes, útil para caracterizar conectividad) y la latencia glass-to-glass (captura → codificación → transporte → decodificación → render). En WebRTC pueden observarse RTTs muy bajos en rutas P2P favorables; sin embargo, el desempeño “glass-to-glass” depende principalmente del pipeline extremo a extremo (códec, parámetros del encoder como GOP/B-frames/rate control, jitter buffer y render del receptor). En mediciones experimentales sobre escenarios WebRTC se reportan latencias extremo a extremo del orden de centenas de milisegundos cuando el pipeline está optimizado. Asimismo, en estudios con usuarios reales, una fracción relevante de conexiones P2P alcanza RTTs compatibles con aplicaciones altamente sensibles a sincronización, aunque no es un comportamiento universal porque depende del acceso y de las condiciones de NAT.

En seguridad, WebRTC impone cifrado en el plano de medios como requisito: el establecimiento de claves se hace mediante DTLS y luego el contenido viaja cifrado con SRTP (DTLS-SRTP), lo que elimina configuraciones “sin cifrar” a nivel de medios. La arquitectura y el modelo de amenazas de WebRTC están desarrollados en documentos específicos de seguridad, que además aclaran implicancias prácticas (por ejemplo, exposición de direcciones, consideraciones de privacidad y superficie de ataque). Un matiz relevante para arquitectura: cuando se introduce un servidor intermedio (p. ej., SFU), el cifrado sigue existiendo en los enlaces WebRTC, pero el “extremo” criptográfico puede ser el servidor (no necesariamente un cifrado E2E entre productor y consumidor final), salvo que se implementen mecanismos adicionales a nivel aplicación.

Para simplificar su uso en streaming (ingesta/egreso) sin implementar señalización compleja, surgen perfiles HTTP. WHIP ya está estandarizado como RFC 9725 y define un mecanismo de ingesta WebRTC basado en HTTP que reduce fricción operativa (publicación vía HTTP y negociación asociada).

SRT: Transporte confiable de baja latencia sobre UDP. Secure Reliable Transport (SRT) es un protocolo de transporte para video en vivo diseñado para mantener baja latencia tolerando pérdida, jitter y variaciones de ancho de banda en redes no confiables. Desarrollado por Haivision y liberado como código abierto en 2017, actualmente es mantenido por la SRT Alliance. Su especificación técnica fue documentada como Internet-Draft en IETF, lo que formaliza su comportamiento y terminología (M. P. Sharabayko et al., 2024).

SRT utiliza UDP como transporte base y agrega una capa de control a nivel de usuario para lograr confiabilidad selectiva. El receptor detecta huecos en la secuencia de paquetes y solicita retransmisiones puntuales mediante NACK (Negative Acknowledgements), un esquema conocido como ARQ selectivo. La diferencia fundamental con TCP radica en que SRT opera con un presupuesto de tiempo configurable, denominado SRT Latency: dentro de esa ventana, el protocolo intenta recuperar paquetes perdidos; si un paquete no puede recuperarse a tiempo, se descarta mediante el mecanismo TLPKTDROP (Too-Late Packet Drop) para mantener la continuidad del flujo. De este modo, la latencia no es un valor fijo universal sino una configuración que se ajusta según las condiciones del enlace, permitiendo latencia acotada y predecible (M. Sharabayko, 2022; M. P. Sharabayko et al., 2024).

En condiciones prácticas, SRT opera con latencias configuradas típicamente entre 120 y 500 ms, pudiendo incrementarse si el RTT es alto o la pérdida significativa. En redes locales de muy baja pérdida puede configurarse más agresivamente, respetando el piso operativo recomendado de aproximadamente 120 ms (M. P. Sharabayko et al., 2024).

En cuanto a conectividad, SRT soporta modos Caller, Listener y Rendezvous, lo que facilita escenarios de despliegue detrás de NAT o firewalls sin requerir aperturas permanentes de puertos entrantes en todos los extremos. Esto resulta relevante para entornos donde la conectividad depende de routers 4G/5G o redes con reglas de acceso restrictivas (M. P. Sharabayko et al., 2024). Además, SRT incorpora cifrado opcional con AES (128, 192 o 256 bits), proporcionando confidencialidad del contenido en tránsito cuando se habilita (M. P. Sharabayko et al., 2024).

RIST: Estándar abierto para transporte resiliente de video. Reliable Internet Stream Transport (RIST) es una especificación para transporte confiable de video en tiempo real sobre redes IP no administradas, desarrollada por el Video Services Forum (VSF) con un foco explícito en interoperabilidad multivendor. El protocolo se publica como Recomendaciones Técnicas (TR) de acceso público, organizadas en perfiles incrementales: Simple Profile (TR-06-1), Main Profile (TR-06-2) y Advanced Profile (TR-06-3), donde cada perfil agrega capacidades sobre el anterior (Video Services Forum, 2020, 2024).

El punto diferencial de RIST es su elección de base protocolar: se apoya en el ecosistema existente de RTP/RTCP (Schulzrinne et al., 2003b) y añade mecanismos de recuperación de pérdidas de forma interoperable. En el Simple Profile, el enfoque central es un esquema ARQ impulsado por el receptor, donde la pérdida se detecta por discontinuidades en los números de secuencia RTP y se solicitan retransmisiones mediante mensajes NACK a través de RTCP, conforme al perfil de retroalimentación extendido RTP/AVPF (Video Services Forum, 2020, 2024). Esto permite recuperar paquetes perdidos dentro de una ventana temporal definida, evitando convertir el transporte en un flujo perfecto pero excesivamente tardío para reproducción en tiempo real. Al igual que SRT, el diseño busca un equilibrio práctico: recuperar lo recuperable a tiempo y descartar lo que llegue demasiado tarde.

La latencia en RIST, al igual que en SRT, no es una propiedad fija del protocolo sino resultado del presupuesto de buffering y de las condiciones del enlace. La ventana disponible para retransmisión está acotada por la latencia objetivo del pipeline; cuanto mayor es el RTT y la variabilidad, mayor debe ser el buffer para mantener alta tasa de recuperación. En evaluaciones empíricas comparando RIST Simple Profile y SRT bajo condiciones controladas de laboratorio, se observó que ambos protocolos pueden comportarse de manera comparable en recuperación de pérdida y latencia cuando se configuran con presupuestos equivalentes, y que las diferencias prácticas aparecen más por implementación y parametrización que por el mecanismo ARQ en sí (Sonono, 2019).

En comparación con SRT, la discusión práctica se organiza en torno a tres ejes. Primero, la base protocolar: RIST prioriza RTP/RTCP y un modelo de extensiones alineado con estándares del broadcast, mientras que SRT utiliza un stack propio sobre UDP derivado de UDT (M. P. Sharabayko et al., 2024). Segundo, la distribución: RIST incluye soporte explícito para IP multicast y escenarios uno-a-muchos desde su Simple Profile (Video Services Forum, 2020), mientras que SRT se utiliza predominantemente en contribución unicast. Tercero, la seguridad: SRT incorpora cifrado AES integrado a nivel de protocolo, mientras que RIST Main Profile emplea DTLS con autenticación basada en certificados, un enfoque que ofrece mayor granularidad en la gestión de identidades (Video Services Forum, 2024).


#### 15.4.2. Servidores de medios de código abierto para transmisión en baja latencia


##### 15.4.2.1. Roles funcionales del servidor de medios

Un servidor de medios puede desempeñar diferentes funciones según los requisitos del sistema. La literatura y las especificaciones técnicas distinguen roles que afectan tanto la latencia end-to-end como la complejidad computacional.

En particular, clasificaremos estos roles entre (i) aquellos que no requieren decodificar/recodificar y (ii) aquellos que sí implican procesamiento multimedia. Adicionalmente, se considera el rol de gateway como función de interoperabilidad entre protocolos y ecosistemas heterogéneos.


###### 15.4.2.1.1. Roles que no requieren decodificar/recodificar

Relay (retransmisión). En este modo, el servidor actúa como punto de paso que recibe paquetes desde un origen y los reenvía a uno o más destinos sin modificar el contenido multimedia. En arquitecturas WebRTC, este rol se implementa típicamente mediante servidores TURN (Traversal Using Relays around NAT), especificados en el RFC 5766, para habilitar conectividad cuando no existe una ruta directa viable entre extremos (Mahy et al., 2010).

Un relay no introduce retardo por procesamiento de medios (no hay decodificación/recodificación). Sin embargo, puede aumentar la latencia efectiva al agregar un salto adicional en la ruta (tráfico vía relé), sumando tiempo de propagación y overhead de entrada/salida. Por lo tanto, su contribución típica a la latencia es baja en comparación con roles que procesan contenido, aunque queda condicionada por ubicación del relé, congestión y buffering del receptor, factores vinculados con los componentes de transporte y renderizado desarrollados en las secciones 16.5.2.3 y 16.5.2.5.

Selective Forwarding Unit (SFU). SFU es uno de los patrones más utilizados en arquitecturas WebRTC multiparte. Cada cliente publica uno (o pocos) flujos hacia el servidor y la SFU reenvía selectivamente esos flujos a los receptores correspondientes sin decodificar ni transcodificar. En términos de latencia, esto es relevante porque, evitar procesamiento pesado sobre el contenido multimedia, la SFU tiende a no sumar retardos comparables a los de una transcodificación; su impacto se concentra en el salto adicional, el enrutamiento, el manejo de colas y el comportamiento bajo carga.

En el caso de Janus, su concepción como gateway WebRTC modular y extensible habilita el uso en configuraciones tipo SFU mediante plugins (Amirante et al., 2014), y su análisis de performance reporta escenarios de videoconferencia y “webinar” donde el cuello de botella pasa a estar dominado por recursos del servidor y número de conexiones simultáneas (Amirante et al., 2015).

Ahora bien, la performance real de una SFU depende del setup y del perfil de carga. En estudios comparativos realizados con el framework KITE se observaron diferencias claras entre implementaciones bajo campañas controladas: algunas SFU mantienen el RTT bajo durante la rampa de carga y degradan de forma gradual, mientras que otras exhiben incrementos mayores de RTT y/o inestabilidad al alcanzar la carga objetivo (Andre et al., 2018). Asimismo, se ha señalado que métricas como RTT o bitrate constituyen indicadores útiles de estrés y degradación, pero no son equivalentes por sí mismas a la latencia glass-to-glass ni agotan la caracterización de la calidad percibida, la cual puede deteriorarse de forma marcada cuando el bitrate desciende por debajo de ciertos umbrales (Andre et al., 2018).

Transmux (re-empaquetamiento). La operación de transmuxing consiste en cambiar el contenedor o el protocolo de entrega sin modificar los flujos ya codificados de audio y video (es decir, sin decodificar ni recodificar). Por ejemplo, al convertir una ingesta RTMP hacia una salida HLS, el sistema puede re-empaquetar el flujo comprimido en segmentos y manifiestos HLS, manteniendo el códec original (May, 2017; Parmar & Thornburgh, 2012).

Aunque el transmux suele agregar poca sobrecarga computacional por no transcodificar, el paso desde un esquema persistente a uno segmentado puede introducir latencia principalmente por segmentación y buffering del reproductor (May, 2017). En streaming adaptativo, el empaquetamiento dinámico se utiliza para flexibilizar la entrega sin duplicar el costo de codificación y para evitar mantener representaciones pre-empaquetadas en múltiples formatos, con beneficios operativos en escenarios a escala (Bentaleb et al., 2019).


###### 15.4.2.1.2. Roles que sí implican procesamiento multimedia

Transcode (transcodificación). La transcodificación implica la decodificación completa del flujo entrante y su posterior recodificación con parámetros distintos (códec, resolución, tasa de bits o frecuencia de cuadros). En sistemas de tiempo real, introduce procesamiento directo sobre el contenido, con impacto material en el retardo. La transcodificación tiene como objetivos centrales: (i) aprovechar información del bitstream original, (ii) preservar calidad visual cerca a una codificación directa desde la fuente y (iii) minimizar retardo y memoria para cumplir requisitos de tiempo real (Ahmad et al., 2005).

En cuanto a latencia, la transcodificación suele convertirse en uno de los aportes dominantes cuando el pipeline exige recodificar en línea. El retardo agregado depende de la complejidad del códec, la resolución, la estructura del GOP y los recursos de hardware. Algunos documentos muestran que la aceleración por hardware permite sostener altas tasas de procesamiento con latencias más controladas que implementaciones puramente en software, y que decisiones de codificación como el uso de B-frames tienden a aumentar la latencia, mientras GOPs más cortos pueden reducir retardo a costa de menor eficiencia de compresión.


###### 15.4.2.1.3. Interoperabilidad

Gateway (pasarela). Un gateway de medios actúa como puente entre distintos protocolos, redes o tecnologías, habilitando interoperabilidad cuando fuentes y consumidores no comparten el mismo transporte o señalización. En WebRTC, Janus fue concebido explícitamente como gateway de propósito general para interconectar clientes WebRTC con tecnologías de tiempo real heredadas mediante una arquitectura modular basada en plugins (Amirante et al., 2014).

Este rol es particularmente relevante cuando se integran fuentes legacy —por ejemplo, cámaras IP que exponen RTSP en ecosistemas ONVIF— con consumidores modernos en navegador, donde WebRTC suele ser el mecanismo natural para interacción en tiempo real (ONVIF, 2019; Schulzrinne et al., 1998b). Desde la perspectiva de latencia end-to-end, el impacto del gateway depende de qué transformación realice: puede limitarse a señalización y reenvío, o incorporar transmux/transcodificación según el caso, alterando sustancialmente su contribución al retardo total.


##### 15.4.2.2. Capacidades transversales y operación

Además de los roles funcionales, en sistemas de transmisión de baja latencia la operación diaria del servidor de medios exige capacidades transversales para diagnosticar degradaciones, validar supuestos de configuración y sostener objetivos bajo carga. Entre ellas, la observabilidad resulta clave porque vincula métricas del servidor y de la red con el comportamiento de protocolos y topologías discutidos en las secciones anteriores.


###### 15.4.2.2.1. Observabilidad y monitoreo

Los servidores de medios contemporáneos suelen incorporar capacidades de observabilidad para monitorear el estado del sistema en tiempo real y facilitar diagnóstico operativo.

Un ejemplo representativo de esto es Kurento, el cual expone métricas y estadísticas mediante APIs programables, facilitando integración con sistemas de monitoreo externos. Entre las señales típicas se incluyen: flujos/sesiones activas, utilización de CPU/memoria, indicadores de desempeño del pipeline y eventos de error. Esta información es clave para detectar cuellos de botella, validar configuraciones de buffers y sostener objetivos de latencia bajo distintas condiciones de carga (Garcia et al., 2017).


##### 15.4.2.3. Patrones de despliegue

La ubicación física del servidor de medios respecto a las fuentes de video y a los consumidores finales tiene un impacto directo sobre la latencia end-to-end del sistema . En particular, el emplazamiento condiciona el componente de red (propagación + jitter + pérdida), la necesidad de buffers para estabilizar la reproducción/análisis y, por ende, el grado en que resulta viable sostener perfiles de ultra-baja latencia con los protocolos discutidos anteriormente. Con base en la literatura de edge computing, es útil organizar el análisis en tres patrones: despliegue en el borde, centralizado en nube y un enfoque híbrido edge-cloud.

Despliegue en el borde (Edge). El paradigma de Multi-access Edge Computing (MEC) propone ubicar cómputo y almacenamiento en proximidad a usuarios/dispositivos, reduciendo la distancia física del tramo crítico y, por lo tanto, la latencia asociada al transporte hacia un centro remoto (Filali et al., 2020). En surveys de MEC y offloading se destaca que la reducción de latencia es uno de los objetivos de QoS más recurrentes en la literatura, precisamente por la sensibilidad de aplicaciones interactivas y “casi en tiempo real” a demoras y variabilidad de red (Mach & Becvar, 2017).

En el caso de streaming, esta proximidad se vuelve particularmente relevante por la intensidad de tráfico. Los requisitos de bitrate para video de muy alta resolución pueden escalar a órdenes elevados (por ejemplo, rangos típicos reportados de ~20–50 Mbps para 4K y ~50–200 Mbps para 8K, según supuestos y configuraciones), lo que refuerza el valor de procesar cerca de la fuente para evitar que enlaces WAN se conviertan en cuello de botella (Khan et al., 2022). Para videovigilancia/visión por computadora en tiempo real, un nodo edge también reduce la dependencia de conectividad hacia la nube central en el tramo donde se requieren decisiones rápidas, ayudando a sostener objetivos estrictos de latencia operacional.

Adicionalmente, la literatura muestra estrategias específicas para “hacer viable” edge cuando hay restricciones de recursos. Existe un enfoque de transcodificación liviana en el borde, orientado a reducir costo computacional y tráfico de red asociado, lo que es consistente con el objetivo de reservar el presupuesto de latencia para el pipeline crítico (captura-codificación-red-procesamiento-alerta) y no consumir innecesariamente en transporte a un cloud remoto (Erfanian et al., 2021).

Despliegue centralizado (Cloud). En el modelo centralizado, los servidores de medios residen en centros de datos remotos operados por proveedores cloud. Este enfoque simplifica operación (consolidación, elasticidad y administración), pero agrega latencia por distancia geográfica y por la variabilidad típica de enlaces de acceso hacia la nube. En consecuencia, para requerimientos de ultra-baja latencia, la literatura de MEC suele contrastar este patrón con edge indicando que el acceso a nubes centralizadas introduce retardos estructurales que pueden ser problemáticos para cargas altamente sensibles a la latencia (Filali et al., 2020).

Dicho esto, el modelo centralizado sigue siendo apropiado cuando el caso de uso tolera mayor latencia: almacenamiento de grabaciones, analítica diferida, enriquecimiento histórico, o distribución a audiencias amplias mediante mecanismos tolerantes a segundos. En un diseño modular, esto permite separar explícitamente el “plano crítico” de detección/alerta (sensitivo a ms) de funciones cloud que priorizan escala y persistencia.

Despliegue híbrido (Edge-Cloud). Las arquitecturas híbridas combinan nodos edge para el procesamiento sensible a la latencia con recursos cloud para funciones que requieren mayor capacidad elástica o almacenamiento a largo plazo. En la práctica, propuestas de edge-assisted para tareas de visión por computadora buscan precisamente repartir el pipeline para cumplir restricciones de “tiempo real” en el borde, dejando al cloud tareas menos urgentes o más pesadas (L. Liu et al., 2019).


##### 15.4.2.4. Impacto en latencia y gestión de buffers

Como se mencionó anteriormente, la latencia end-to-end resulta de la suma de contribuciones de las etapas a lo largo de todo el pipeline. En consecuencia, cuando en esta sección se discuten “latencias” asociadas a un componente (p. ej., el servidor), deben interpretarse como una porción del retardo total.

En roles que no procesan el contenido multimedia, la contribución del servidor tiende a ser baja en comparación con etapas como codificación/decodificación, porque el servidor se limita a recibir y reenviar paquetes sin recodificar (Amirante et al., 2015). Aun así, el retardo efectivo puede aumentar por factores “sistémicos” como un salto adicional en la ruta o colas internas bajo carga.

Cuando el servidor asume roles de procesamiento o adaptación del flujo, la contribución a la latencia puede volverse material. En particular, en escenarios donde el sistema pasa de un esquema continuo a uno segmentado, la latencia final suele quedar dominada por la segmentación y por las políticas de buffering del reproductor, más que por el costo computacional del servidor (Bentaleb et al., 2019; May, 2017b). La transcodificación, por su parte, requiere decodificación completa y recodificación, por lo que suele ser la operación más demandante del pipeline y puede agregar desde cientos de milisegundos hasta varios segundos según códec, resolución, estructura de GOP y hardware disponible (Ahmad et al., 2005; Li et al., 2019; Žádník et al., 2022).

La gestión de buffers es el otro factor crítico que condiciona la latencia percibida. Cada milisegundo de buffer “comprado” para estabilidad incrementa la latencia end-to-end. Por eso, si el caso de uso exige respuesta humana rápida, el problema no es “eliminar buffers”, sino presupuestarlos: definir un presupuesto de latencia total y repartirlo explícitamente entre codificación, red/recuperación y reproducción, validándolo con mediciones glass-to-glass y no solo con métricas de red como RTT.

En términos de orden de magnitud, como referencia para sistemas human-in-the-loop, se reporta que latencias constantes por debajo de ~300 ms pueden ser manejables, mientras que a partir de ese umbral se vuelve significativamente más difícil mantener operación en tiempo real en tareas de control remoto.


##### 15.4.2.5. Servidores de medios de código abierto

El ecosistema de servidores de medios de código abierto reúne herramientas con perfiles técnicos distintos: (a) gateways/SFUs WebRTC orientados a interactividad y baja latencia, (b) servidores con pipelines de procesamiento multimedia integrables (útiles cuando se evalúa procesamiento “en el plano de medios”), y (c) routers/gateways multiprotocolo pensados para compatibilidad y operación liviana, además de alternativas enfocadas en broadcasting con salidas WebRTC y/o LL-HLS. Estas opciones se presentan como posibles candidatos a evaluar en etapas posteriores.

Janus WebRTC Gateway. Janus es un gateway WebRTC modular que, en configuraciones típicas de videoconferencia y distribución interna, implementa un patrón publish/subscribe mediante su plugin VideoRoom, operando como una SFU (Meetecho, s/f). Su diseño por plugins lo vuelve relevante cuando se requiere separar un núcleo de señalización/gestión WebRTC de funcionalidades específicas (p. ej., videoroom, streaming), y su comportamiento bajo carga fue estudiado en distintos escenarios de publicación/suscripción (Ahmad et al., 2005; Amirante et al., 2014, 2015).

Kurento Media Server. Kurento se caracteriza por un enfoque orientado a media pipelines: además de endpoints (p. ej., WebRTC), define “media elements” encadenables para construir grafos de procesamiento. Esta arquitectura resulta pertinente cuando se analiza la alternativa de integrar procesamiento multimedia (p. ej., módulos basados en OpenCV) dentro del pipeline del servidor, en lugar de tratar al servidor como un componente de transporte puro (Garcia et al., 2017; López et al., 2016). Para E-OVRT-VDP, Kurento se ubica naturalmente en el grupo de servidores donde la evaluación debe considerar explícitamente el trade-off entre capacidad de procesamiento y latencia agregada.

MediaMTX. MediaMTX se presenta como un servidor/proxy “zero-dependency” concebido como media router, con capacidad de publicar/leer/proxy/record/playback y de convertir entre protocolos de manera directa (bluenviron, s/f). De acuerdo con su documentación, soporta un conjunto amplio de entradas/salidas típicas para integración (incluyendo RTSP, RTMP, WebRTC, SRT, HLS/LL-HLS, MPEG-TS y RTP), lo que lo posiciona como candidato cuando el objetivo principal es compatibilidad multiprotocolo y operación liviana en escenarios cercanos a las fuentes (bluenviron, s/f; Go Packages, s/f).

OvenMediaEngine. OvenMediaEngine (OME) se presenta como un servidor orientado a baja latencia y escala, con soporte de ingesta multiprotocolo (p. ej., WebRTC, SRT, RTMP, RTSP, MPEG-2 TS) y salidas centradas en WebRTC y LL-HLS (AirenSoft, s/f-a, s/f-b). En su documentación se explicita que LL-HLS apunta a latencias end-to-end del orden de segundos (≈2–5 s) y que el soporte oficial está disponible desde versiones específicas del proyecto (AirenSoft, s/f-a, s/f-b). En un marco de evaluación, OME es relevante cuando se desea comparar un enfoque “broadcast-oriented” que combine una salida ultra-baja latencia (WebRTC) con una salida HTTP de baja latencia (LL-HLS) para compatibilidad.

SRS (Simple Realtime Server). SRS se describe como un servidor de medios de alta eficiencia con soporte para múltiples protocolos de ingestión/entrega (p. ej., RTMP, WebRTC, HLS, HTTP-FLV, SRT, MPEG-DASH, entre otros) y con un rol explícito de media gateway, facilitando conversiones entre protocolos en un modelo publish/subscribe (OSSRS, s/f). Esto lo vuelve candidato cuando se busca evaluar compatibilidad y comparar un “gateway multiprotocolo” frente a alternativas más especializadas (SFU pura, procesamiento embebido, etc.).

Puede verse un análisis comparativo de estos servidores en la Tabla A.3 del Anexo A.


#### 15.4.3. Brechas del estado del arte en el streaming/OVD

Las tecnologías y arquitecturas actuales de streaming presentan un conjunto de limitaciones que condicionan directamente el diseño del pipeline experimental.


##### 15.4.3.1. Ausencia de benchmarks end-to-end integrados para pipelines OVD

La literatura revisada evidencia una fragmentación sistemática en la evaluación de desempeño: los benchmarks de inferencia de modelos OVD (p. ej., AP en COCO/LVIS, FPS en GPU aislada) operan de forma independiente respecto de los benchmarks de streaming (latencia de transporte, throughput de protocolo) y de las métricas de plataformas de edge computing (TOPS, FPS bajo carga térmica). Para una plataforma como E-OVRT-VDP el criterio de selección debe basarse en mediciones reproducibles del pipeline completo, y no extrapolarse directamente de métricas parciales o aisladas.

Esta brecha implica que no existen referentes directos en la literatura que permitan predecir con confianza el desempeño de un sistema que combina ingesta multi-protocolo, decodificación acelerada, inferencia OVD y emisión de eventos bajo restricciones de latencia propias de operación en tiempo real. En consecuencia, la validación empírica del pipeline completo constituye una contribución necesaria del proyecto, y la definición de protocolos de medición reproducibles deberá abordarse como parte del diseño experimental en la etapa 2.


##### 15.4.3.2. Integración de modelos OVD dentro de pipelines de streaming optimizados

Los frameworks de streaming más maduros para video analytics en tiempo real, como NVIDIA DeepStream, han sido históricamente diseñados y optimizados para detectores de clases fijas con arquitecturas convolucionales estándar, cuyos patrones de integración asumen una entrada de imagen y un conjunto predefinido de clases de salida (NVIDIA, 2024). Si bien el ecosistema ha comenzado a incorporar soporte para modelos open-vocabulary —por ejemplo, NVIDIA TAO Toolkit incluye flujos de exportación y despliegue para Grounding DINO (NVIDIA, s/f-g)—, la integración de estos modelos en pipelines de streaming presenta desafíos técnicos que no se resuelven con la misma inmediatez que los detectores convencionales.

En particular, la conversión de modelos OVD a formatos optimizados como TensorRT puede requerir adaptaciones no triviales cuando la arquitectura incluye operadores no soportados nativamente o componentes dinámicos asociados a la codificación de prompts textuales. Dado que TensorRT no admite entradas de tipo texto, la etapa de tokenización debe separarse del grafo del modelo y gestionarse externamente (NVIDIA, s/f-g), lo que introduce complejidad adicional en el diseño del pipeline. Más ampliamente, la arquitectura multi-modal que caracteriza a los modelos OVD —con un encoder visual y un encoder textual que interactúan mediante mecanismos de fusión— no se alinea directamente con los patrones de integración nativos de los plugins de inferencia estándar de estos frameworks, aunque rutas alternativas como la integración con Triton Inference Server ofrecen mayor flexibilidad al soportar modelos en múltiples formatos y frameworks (NVIDIA, s/f-h). Esta brecha, si bien se está reduciendo, sugiere que la integración de modelos OVD dentro del pipeline de streaming requerirá capas de adaptación específicas cuya complejidad y costo deberán evaluarse empíricamente.


##### 15.4.3.3. Interoperabilidad efectiva entre protocolos heterogéneos

Si bien se estableció un mapa de roles potenciales por familia de protocolos y se analizaron las capacidades de interoperabilidad de servidores de medios de código abierto, la literatura no ofrece evidencia consolidada sobre el overhead real introducido por las pasarelas de protocolo (p. ej., RTSP a WebRTC, RTMP a SRT) en condiciones de operación representativas del caso de uso. La transcodificación, el re-empaquetamiento entre formatos contenedores de medios (p. ej., MPEG-TS, FLV, fMP4) y la adaptación entre pilas de transporte pueden introducir latencias adicionales y puntos de fallo que no se capturan en las especificaciones de protocolo individuales.

Esta brecha resulta relevante en el contexto de E-OVRT-VDP, dado que en entornos reales de obra el parque de cámaras puede exponer flujos mediante protocolos diversos. Si bien el prototipo experimental operará previsiblemente con un conjunto acotado de fuentes y protocolos, la identificación de este vacío en la literatura permite anticipar un factor de complejidad para escenarios de despliegue más amplios y orienta el diseño hacia soluciones que no introduzcan dependencias rígidas con un único protocolo de ingesta.


##### 15.4.3.4. Métricas de evaluación alineadas con objetivos de seguridad laboral

Las métricas estándar de evaluación de sistemas de streaming, tales como latencia media, throughput, tasa de pérdida de paquetes y calidad visual (PSNR/SSIM), no capturan adecuadamente el valor operativo de un sistema orientado a la detección asistiva de riesgos en obra. De manera análoga a lo identificado en la sección de OVD respecto de las métricas de detección, las métricas de streaming convencionales no consideran aspectos como el tiempo transcurrido entre el inicio de una condición de riesgo y la notificación al operador, la continuidad de detección bajo variaciones de calidad del stream, o el impacto diferenciado de artefactos de compresión sobre la detectabilidad de elementos de protección personal.


#### 15.4.4. Síntesis comparativa de protocolos

La Tabla 8 sintetiza las características principales de los protocolos analizados, con énfasis en las dimensiones de mayor relevancia para el diseño del sistema E-OVRT-VDP.

Tabla 8

Comparativa de protocolos de transmisión de video de baja latencia para sistemas de video analítico en tiempo real


| Protocolo | Latencia típica E2E | Transporte base | Modelo de entrega | Resiliencia a pérdida | Cifrado nativo | Caso de uso principal |
| --- | --- | --- | --- | --- | --- | --- |
| RTSP/RTP | ~200–800 ms | UDP (o TCP) | Pull (sesión controlada) | Media (con RTCP) | Opcional (RTSPS) | Cámaras IP industriales, CCTV, entornos LAN controlados |
| RTMP | ~2–5 s | TCP | Push | Alta (TCP garantiza entrega) | Sí (RTMPS/TLS) | Ingesta a plataformas de streaming; encoders hacia servidores |
| HLS / MPEG-DASH | ~5–45 s (LL: ~2–10 s) | HTTP/TCP | Pull (segmentado) | Alta (CDN + HTTP) | Sí (HTTPS) | Distribución masiva de contenido; viewers simultáneos elevados |
| WebRTC | < 500 ms | UDP (SRTP sobre DTLS) | Push/Pull (P2P o SFU) | Media (con NACK/FEC) | Sí (DTLS-SRTP, obligatorio) | Interactividad ultra-baja latencia; videoconferencia; monitoreo P2P |
| SRT | ~120–500 ms (configurable) | UDP + ARQ selectivo | Push o Pull | Alta (ARQ con presupuesto de tiempo) | Sí (AES-128/256) | Contribución broadcast; enlaces WAN no confiables; 4G/5G |
| RIST | ~120–500 ms | RTP + ARQ (RTCP FB) | Push o Pull (multicast posible) | Alta (ARQ + FEC) | Sí (DTLS) | Broadcast profesional; distribución multicast en redes gestionadas |

Nota. Los rangos de latencia E2E reportados son valores típicos dependientes de configuración, no compromisos de los estándares. La latencia final está determinada por el pipeline completo (captura, codificación, transporte, decodificación, inferencia), no únicamente por el protocolo. HLS/DASH LL = Low-Latency HLS / DASH. DTLS-SRTP = combinación de Datagram TLS y Secure RTP (cifrado obligatorio en WebRTC). ARQ = Automatic Repeat reQuest. FEC = Forward Error Correction. Fuente: Elaboración propia basada en Axis Communications AB (2015), DASH Industry Forum (2020), ISO/IEC (2022), Keranen et al. (2018), May (2017), Pantos (2025), Parmar y Thornburgh (2012), Roy (2024), Schulzrinne et al. (1998, 2003, 2016), Sharabayko et al. (2024), Sonono (2019), Video Services Forum (2020, 2024) y World Wide Web Consortium (2025).

La tabla muestra que no existe un protocolo que maximice simultáneamente latencia mínima, alta resiliencia a pérdidas y escalabilidad, lo cual es coherente con el enfoque de diseño de cada estándar, orientado a prioridades diferentes según el contexto de aplicación. En arquitecturas comúnmente adoptadas, esta situación suele abordarse mediante esquemas híbridos que emplean protocolos distintos por tramo del flujo de video: uno para ingesta y transporte desde el origen hacia un servidor o plataforma de medios (en entornos LAN o WAN con distintos niveles de control), y otro para distribución/visualización hacia clientes finales, donde los requerimientos de interactividad, número de usuarios y compatibilidad con navegadores influyen de manera determinante. De forma complementaria, también es habitual que los protocolos HTTP adaptativos (HLS/DASH) se reserven para consumo masivo, reproducción diferida o escenarios donde la prioridad sea la escalabilidad y la tolerancia a variaciones de red, más que la inmediatez. En consecuencia, la evidencia comparativa respalda que la selección de protocolos debe abordarse como una decisión dependiente del escenario y de la infraestructura, y suele validarse mediante pruebas empíricas sobre el pipeline completo (captura, codificación, transporte, decodificación e integración con analítica), antes de su adopción en un sistema específico.

---

## Fuente: `docs/informe/entregable/96d-informe-v11-marco-teorico.md`

> SHA-256 del bloque: `f9d18899356a0b4f74e1278602023ffb08f98dcf9cfcc86a4de545d68907b8cd`  
> Seleccion: documento completo.

# 96d — Texto extraído del informe v1.1: §16 Marco Teórico

> **Extracción derivada (2026-07-18)** del `.docx`
> `informe/entregable/E-OVRT-VDP_v1.1_05062026-sin-indice.docx`, **solo para búsqueda y cita**
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

---

## Fuente: `docs/informe/entregable/96e-informe-v11-cierre-anexos-referencias.md`

> SHA-256 del bloque: `181799f6438299eb111302a479f0e1750fae6f5dfeea7200636d55633c6a7018`  
> Seleccion: Anexo A vigente.

### 19.1. Anexo A - Comparativas técnicas y estado del arte complementario

Tabla A. 1

Síntesis de modelos OVD orientada a prototipado


| Modelo | Familia | Mecanismo V-L | AP Zero-shot | FPS | Licencia |
| --- | --- | --- | --- | --- | --- |
| DINO-X | Transformer | Universal Object Prompt | 59.8 (LVIS) | N/D | Apache-2.0 |
| G-DINO 1.5 Pro | Transformer | Fusión cross-modal profunda | 55.7 (LVIS) | N/D | Apache-2.0 |
| G-DINO 1.5 Edge | Transformer | Fusión cross-modal optimizada | 36.2 (LVIS) | 75.2 (TRT) | Apache-2.0 |
| LLMDet | Transformer+LLM | Co-entrenamiento con LLM | 51.1–52.4 (LVIS) | N/D | Apache-2.0 |
| OV-DINO | Transformer | LASF + UniDI | 50.6 (COCO) | N/D | Apache-2.0 |
| DetCLIPv3 | Transformer | Generativo + VLLM | 48.8 (LVIS) | N/D | N/D |
| OWLv2 L/14 | ViT | Self-training escalable | 44.6 (LVIS rare) | N/D | Apache-2.0 |
| YOLOE-v8-L | One-stage | RepRTA + SAVPE + LRPC | 35.9 (LVIS) | 102.5 (TRT) | AGPL-3.0 |
| YOLO-World-L | One-stage | RepVL-PAN contrastivo | 35.4 (LVIS) | 52.0 (V100) | GPLv3 |
| OmDet-Turbo | Transformer RT | EFH + caching texto | 34.0 (LVIS) | 100.2 (TRT) | Apache-2.0 |
| YOLOE-v8-S | One-stage | RepRTA reparametrizable | 27.9 (LVIS) | 305.8 (TRT) | AGPL-3.0 |
| Florence-2-L | Seq2Seq | Generación condicionada | 37.5 (COCO) | Variable | MIT |

Nota: Las velocidades citadas indican condiciones específicas (hardware GPU: V100, T4 o A100; uso de TensorRT; batch size 1; FP16 y/o caching de texto). Las licencias GPL/AGPL requieren derivar código abierto, limitando la adopción industrial. N/D indica no reportado o no optimizado para tiempo real. Fuente: elaboración propia basada en Ren et al. (2024a, 2024b), Fu et al. (2025), Wang et al. (2024, 2025), Yao et al. (2024), Minderer et al. (2023), Cheng et al. (2024), Zhao et al. (2024) y Xiao et al. (2023).

Tabla A. 2

Métricas de evaluación estándar en seguimiento multi-objeto: características y limitaciones


| Métrica | Qué mide | Fortaleza principal | Limitación principal |
| --- | --- | --- | --- |
| MOTA | Precisión global: penaliza FP, FN e ID switches ponderados sobre el total de ground truth (Bernardin & Stiefelhagen, 2008) | Métrica clásica, simple y ampliamente adoptada para medir el desempeño de detección | Sesgada hacia errores de detección; subestima errores de asociación |
| IDF1 | Consistencia de identidad: F1-score sobre detecciones que mantienen el identificador correcto a lo largo del tiempo (Ristani et al., 2016) | Captura la estabilidad de las identidades asignadas | Ignora mejoras en detección (Ristani et al., 2016); no considera localización espacial (Luiten et al., 2021) |
| HOTA | Balance explícito entre precisión de detección (DetA) y precisión de asociación (AssA), con componente de localización (Luiten et al., 2021) | Métrica integral adoptada por MOTChallenge como estándar de referencia | Mayor complejidad conceptual respecto a MOTA/IDF1, al requerir la interpretación conjunta de sus componentes DetA, AssA y LocA para el diagnóstico de fallos (Luiten et al., 2021) |

Nota. MOTA = Multiple Object Tracking Accuracy. IDF1 = Identification F1-Score. HOTA = Higher Order Tracking Accuracy. DetA = Detection Accuracy. AssA = Association Accuracy. FP = Falsos Positivos. FN = Falsos Negativos. IDSW = ID Switches. GT = Ground Truth. Fuente: Elaboración propia basada en las fuentes citadas (Bernardin & Stiefelhagen, 2008; Luiten et al., 2021; Ristani et al., 2016).

Tabla A. 3

Comparativa de servidores de medios de código abierto


| Servidor | Lenguaje | Rol principal | Protocolos | Transcode | Fortaleza |
| --- | --- | --- | --- | --- | --- |
| Janus | C | SFU/Gateway | WebRTC, SIP | Plugins | Modularidad, documentación académica |
| Kurento | C++ | MCU/ Procesamiento | WebRTC, RTSP, RTP | Sí (integrado) | Integración OpenCV, pipelines |
| MediaMTX | Go | Router/Proxy | RTSP, RTMP, WebRTC, SRT, HLS | No | Ligereza, multi-protocolo |
| OvenMediaEngine | C++ | Origin-Edge | WebRTC, LL-HLS, RTMP | Sí (GPU) | Escalabilidad, baja latencia |
| SRS | C++ | Streaming | RTMP, WebRTC, SRT, HLS | Limitado | Eficiencia, cloud-native |

Nota. Elaboración propia basada en las fuentes tratadas en la sección (Ahmad et al., 2005; AirenSoft, s/f-a, s/f-b; Amirante et al., 2014, 2015; bluenviron, s/f; Garcia et al., 2017; Li et al., 2019; López et al., 2016; Meetecho, s/f; OSSRS, s/f; Žádník et al., 2022).

---

## Fuente: `docs/informe/ajustes/01-etapa-1-fundamentacion-teorica.md`

> SHA-256 del bloque: `2fdeb4186e7a62d65205f4d5bf58fc1b4510a60ef071308f848065d08fcfe576`  
> Seleccion: documento completo.

# Etapa 1 — ajustes a la fundamentación teórica (§15 Estado del Arte, §16 Marco Teórico)

> **Estado (2026-08-10):** relevado, **sin pase de correcciones aplicado**. El
> relevamiento salió de contrastar el §15 del informe contra fuentes primarias
> fetcheadas y contra nuestra propia evidencia medida (`sintesis/resultados-y-conclusiones.md`
> §7, relevamiento del 2026-08-06). El §16 (Marco Teórico) **no fue relevado todavía**
> — es `AJ-1.16`, y es un hueco declarado, no un "no hay nada que cambiar".
>
> **Marca de confianza de las cifras externas**, tal como la fija la fuente:
> **[P]** verificada en fuente primaria · **[S]** fuente secundaria oficial ·
> **[R]** circulante sin verificar.

| Dónde | Qué |
|---|---|
| Texto actual | `entregable/96c` (§15 Estado del Arte) · `entregable/96d` (§16 Marco Teórico) · `entregable/96e` §19.1 (Anexo A, Tabla A.1) |
| Fuente del relevamiento | `sintesis/resultados-y-conclusiones.md` §7.1–§7.4 |
| Teoría de apoyo para redactar | `sintesis/fundamentos-teoricos.md` |

---

## 1. Por qué esta etapa no se puede saltear

El §17.5 (Etapa 5) va a reportar **mAP@0,5 0,551 agregado** sobre `bench_v3`. Un número
así, sin vara, no significa nada para un jurado — y hoy **el §15 no da la vara**: cita
SHEL5K, CHV y SH17 únicamente como datasets, sin reportar ni una cifra de mAP de la
literatura supervisada. Toda la defensa pivotea sobre ese contraste ("~63% del techo
sin entrenar"). **La vara se construye acá; el contraste se hace en §17.5/§18** — el
§15 no cita resultados propios (regla de no-anacronismo, mapa regla 5).

Los dos primeros ajustes son, por eso, los únicos 🔴 de esta etapa.

---

## 2. Tablero de ajustes

| ID | Sección | Tipo | Pri | Enunciado |
|---|---|---|---|---|
| **AJ-1.01** | §15 | CONCRETA | 🔴 | **Hueco 1: falta la línea base de EPP supervisado.** Incorporar la Vara 1 con cifras, o declarar la ausencia como brecha. |
| **AJ-1.02** | §15 / Tabla 3 | CONCRETA | 🔴 | **Hueco 2: el §15 no deja declarada la brecha que motiva el bench propio** — y la brecha se sostiene con literatura, sin adelantar resultados. |
| **AJ-1.03** | §15 | ERRATA | 🟠 | El 52,5 AP de GDINO es del backbone **Swin-L** y el informe nunca lo declara; lo desplegado acá es **Swin-T**. |
| **AJ-1.04** | §15 / tablas | ERRATA | 🟡 | OmDet-Turbo-Tiny "30,3 LVIS" (probable *mislabel* de ODinW-13) y 34,0 vs 34,7 entre tablas. |
| **AJ-1.05** | §15 | ERRATA | 🟡 | El 53,4 COCO de OmDet-Turbo probablemente **no es zero-shot**. |
| **AJ-1.06** | §15 | ERRATA | 🟡 | LLMDet "51,1–52,4": el 52,4 no tiene origen. |
| **AJ-1.07** | §15 | ERRATA | 🟡 | El caching "ahorra ≈40 ms" en un modelo al que la misma tabla asigna **7,1 ms totales**. |
| **AJ-1.08** | Tabla 3 | PRECISA | 🟡 | La columna Latencia es **1000/FPS**: derivada, no medida. Declararlo. |
| **AJ-1.09** | Anexo A / Tabla A.1 | ERRATA | 🟠 | GDINO 1.5 y DINO-X figuran como "Apache-2.0" siendo **API cerrada sin pesos abiertos** (la licencia es del SDK). |
| **AJ-1.10** | §15 / Referencias | ERRATA | 🟡 | Citas inconsistentes: Liu 2023/2024, Minderer, Xiao, Lin 2014/2015, Ren a/b/c. |
| **AJ-1.11** | §15 | CONCRETA | 🟡 | **MM-Grounding-DINO no tiene ninguna cifra en el informe**, y el proyecto lo evaluó y lo descartó. |
| **AJ-1.12** | §15 | PRECISA | 🟠 | **Advertencia de métrica**: AP 0,50:0,95 (COCO/LVIS) y mAP@0,5 (EPP y nuestro bench) **nunca en la misma columna**. |
| **AJ-1.13** | §15 | CONCRETA | 🟠 | Incorporar la **Vara 3** — el cruce OVD×EPP está casi vacío en la literatura: la brecha se declara acá; quién la ocupa se relata en §17.5. |
| **AJ-1.14** | §15 | PRECISA | 🟠 | Corregir el uso de **Abdalwhab 2025**: es evidencia de brecha de vocabulario zero-shot, **no** del efecto de ajustar un OVD. |
| **AJ-1.15** | §15 → §17.5 | PRECISA | 🟠 | Fijar la **regla de tres tiempos** para presentar conclusiones, y usar "adaptación" con precisión. |
| **AJ-1.16** | **§16** | EVIDENCIA | 🟡 | **Hueco: el §16 Marco Teórico no fue relevado** contra lo que hoy sabemos. |

---

## 3. Los ajustes, desarrollados

### AJ-1.01 · §15 · CONCRETA · 🔴 — la vara supervisada in-domain

**Qué pasa hoy.** El informe **no reporta ni una cifra de mAP** de la literatura de
detección de EPP con modelos entrenados. SHEL5K, CHV y SH17 aparecen solo como
datasets.

**Qué debe decir.** La Vara 1, en **mAP@0,5** [P/S]:

| Dataset (paper) | Mejor modelo entrenado | mAP@0,5 | Dato fino que importa |
|---|---|---|---|
| SHEL5K (Otgonbold 2022, *Sensors* 22(6):2315) | YOLOR | **0,883** | `head` (cabeza sin casco) **0,907** — supervisada, la clase **no** es difícil |
| CHV (Wang 2021, *Sensors* 21(10):3478) | YOLOv5x | **0,866** | 6 clases (person, vest, 4 colores de casco) |
| SH17 (2024; 17 clases, industrial) | YOLOv9-e | **≈0,71** | YOLOv8 n→x: 0,58–0,69 — con vocabulario grande el techo baja |

El dato de `head` 0,907 es el fundamento externo de dos conclusiones propias (AF-5 y
F-88.3): **la clase `bare_head` no es difícil; lo difícil es alcanzarla por vía
léxico-conceptual sin entrenar.**

**Alternativa admisible** si no se quiere ampliar el §15: declarar explícitamente la
ausencia como brecha del estado del arte. Lo que **no** es admisible es dejar el 0,551
sin vara.

---

### AJ-1.02 · §15 y Tabla 3 · CONCRETA · 🔴 — declarar la brecha que motiva el bench propio (sin adelantar resultados)

> ✎ **2026-08-11 — reescrito por la regla de no-anacronismo** (mapa, regla 5). La
> versión anterior de este ajuste pedía meter en §15 el cruce con la evidencia propia
> (YOLOE recall 0,000; G2A live; keep-up del Sprint 2) — **datos de Etapa 4/5 que el
> §15, siendo Etapa 1, no puede conocer**. El cruce se hace en §17.5/§18 (`AJ-5.11`,
> `AJ-6.01`); acá queda solo lo que la literatura sostiene.

**Qué pasa hoy.** El §15 cataloga modelos por sus cifras COCO/LVIS y no deja escrita la
pregunta que esas cifras no responden: **¿predicen los benchmarks generales el
rendimiento sobre una condición de dominio específica?**

**Qué debe decir — y todo se sostiene con literatura, sin un solo número propio:**

- **ODinW**: GDINO-L cae de ~52 AP en COCO a **26,1 mean AP** sobre los 35 datasets de
  ODinW [P] — la referencia publicada de cuánto colapsa un OVD fuera de distribución.
- **Chen 2025** (arXiv:2508.11011): grounding con atributo/negación → **IoU <20%** [P]
  — la evidencia publicada de que la composición léxica fina no la resuelve el
  preentrenamiento.
- Conclusión que el §15 puede firmar en su tiempo narrativo: *los benchmarks generales
  no garantizan la condición de dominio, y no existe benchmark publicado del cruce
  OVD×EPP* (→ AJ-1.13) — **esa brecha es la que justifica que el protocolo (§17.1.9.2)
  exija baseline zero-shot propia y test congelado**.

**Dónde queda el resto:** la *confirmación medida* de esta brecha (el caso YOLOE:
35,9 AP LVIS publicado vs recall CR-01 = 0,000 acá; los G2A medidos en nuestro hardware
vs la columna Latencia derivada de la Tabla 3) es material de **§17.5**, escrito en tres
tiempos contra esta vara. El §15 planta la pregunta; el §17.5 la responde.

---

### AJ-1.03 · §15 · ERRATA · 🟠 — declarar el backbone de cada cifra de GDINO

El **52,5 AP COCO zero-shot corresponde a Swin-L**, y el informe no lo declara. Lo
desplegado en este trabajo es **Swin-T**, cuyo zero-shot COCO publicado es **≈48,4**
[S]. Regla a aplicar en todo el §15: **ninguna cifra de GDINO sin su backbone al lado.**

---

### AJ-1.04 a AJ-1.08 · erratas y precisiones verificables contra los papers

Se agrupan porque se corrigen en una sola pasada, todas contra fuente:

- **AJ-1.04** — OmDet-Turbo-Tiny aparece con "30,3 LVIS", que es un *mislabel* probable
  de **ODinW-13**; y el mismo modelo figura con **34,0 en una tabla y 34,7 en otra**.
- **AJ-1.05** — el **53,4 COCO** de OmDet-Turbo probablemente **no es zero-shot**;
  verificar y etiquetar.
- **AJ-1.06** — LLMDet "51,1–52,4": el **52,4 no tiene origen** rastreable.
- **AJ-1.07** — se afirma que el caching **"ahorra ≈40 ms"** en un modelo al que la
  misma tabla asigna **7,1 ms totales**. Es aritméticamente imposible.
- **AJ-1.08** — la **columna Latencia de la Tabla 3 es 1000/FPS**: es una derivación, no
  una medición. Declararlo en la nota de la tabla (y es la bisagra para introducir
  nuestras latencias medidas, AJ-1.02).

---

### AJ-1.09 · Anexo A / Tabla A.1 · ERRATA · 🟠 — la licencia de GDINO 1.5 y DINO-X

La Tabla A.1 las lista como **"Apache-2.0"**. Son **API cerrada sin pesos abiertos**:
lo Apache-2.0 es el **SDK**, no el modelo [S]. Es una errata con consecuencia — una
afirmación de licencia incorrecta en un anexo de comparación técnica es exactamente el
tipo de cosa que un jurado verifica.

---

### AJ-1.10 · Referencias · ERRATA · 🟡

Citas inconsistentes a lo largo del §15: **Liu 2023/2024** (misma obra, dos años),
**Minderer**, **Xiao**, **Lin 2014/2015**, **Ren a/b/c**. Unificar contra el listado de
referencias del `96e`.

---

### AJ-1.11 · §15 · CONCRETA · 🟡 — MM-Grounding-DINO

El informe **no trae ninguna cifra publicada** de MM-Grounding-DINO, siendo un candidato
de la misma familia. Publicadas: **tiny 50,4–50,6 COCO zero-shot / 35,7–41,4 LVIS**
[P/S]. **Al §15 va solo la cifra publicada** (es literatura); el descarte empírico del
proyecto (bboxes roto en MM-GDINO-tiny) es un resultado y se relata en §17.5 — pero sin
la cifra en el §15, ese relato posterior queda sin contexto.

---

### AJ-1.12 · §15 · PRECISA · 🟠 — la advertencia de métrica (la trampa del jurado)

Las cifras COCO/LVIS de los papers OVD son **AP promediado sobre IoU 0,50:0,95** (LVIS
además con protocolo *Fixed AP*). Los papers de EPP y nuestro bench reportan
**mAP@0,5**, que da numéricamente más alto para el mismo detector.

**Nunca poner las dos series en la misma columna.** El error previsible del jurado es
*"GDINO da 48–52 en COCO y ustedes 0,55 — rinde igual"*. No: en mAP@0,5 sobre COCO
estaría muy por encima; **nuestra caída es real y es el costo de dominio**. Esta
advertencia tiene que estar escrita en el informe, no solo entendida.

---

### AJ-1.13 · §15 · CONCRETA · 🟠 — la Vara 3: el cruce OVD×EPP

Es el hueco que el trabajo ocupa, y hay que decirlo con las tres piezas:

- **OWLv2 zero-shot sobre obra** (Choi & Greer 2024, arXiv:2410.12225): AP@IoU>0,5
  **0,649 hardhat** y **0,677 person** sobre 5.210 imágenes [P] — la **única** cifra
  publicada directamente comparable con nuestro AP@0,5 por clase.
- **VLMs con atributo/negación** (Chen 2025, arXiv:2508.11011): *"workers wearing white
  hard hats"* → **IoU <20%** [P] — la literatura confirma la "ceguera al atributo" de
  E-DIR que medimos.
- **No existe paper 2023–2026** con GDINO o YOLO-World zero-shot medido sobre
  SHEL5K/CHV, ni sobre un bench de EPP multi-fuente con protocolo COCO. **Esa es la
  brecha, y el §15 la deja declarada como brecha** — que `bench_v3` la ocupa es la
  lectura de §17.5/§18, no de acá (regla de no-anacronismo).

Las fuentes externas verificadas el 2026-08-06 están listadas al final de
`sintesis/resultados-y-conclusiones.md` §7.4 — reusar ese listado, no rearmarlo.

---

### AJ-1.14 · §15 · PRECISA · 🟠 — Abdalwhab 2025 está mal usado

El paper compara **YOLO11 fine-tuned vs OVD zero-shot** en componentes MEP. Eso es
**evidencia de brecha de vocabulario zero-shot**, no evidencia del efecto de ajustar un
OVD. Como está citado hoy, sostiene una conclusión que el paper no sostiene.

---

### AJ-1.15 · §15 → §17.5 · PRECISA · 🟠 — la regla de tres tiempos, y "adaptación"

**Regla de redacción** (fijada 2026-08-06): cada conclusión se escribe en tres tiempos —
*qué dice la literatura* (cifra de la Vara) → *qué medimos nosotros* (cifra de
`results/`) → *qué tipo de aporte queda*. **Nunca al revés**: empezar por el número
propio sin vara es exactamente lo que hoy le pasa al §15.

**Dónde opera la regla (no-anacronismo):** los tres tiempos se escriben **en §17.5 y
§18**, que sí conocen los resultados. El rol del §15 en esta regla es pasivo: dejar la
vara y la brecha listas para que el tercer capítulo las cite — **al §15 no entra ningún
número propio**.

**Y una precisión de vocabulario que hay que cuidar ante el jurado:** el núcleo medido
de la tesis **no adapta los pesos**. Adapta los modelos **operativamente**: resolución
(560), formulación del vocabulario (prompt sets congelados) y las capas de plataforma
alrededor (histéresis temporal, identidad por sujeto, política de alerta). **Medir
cuánto rinde ese stack de adaptación sin entrenar es la perspectiva nueva** — decirlo
así, y no "adaptamos los modelos". El fine-tuning (E-04) es una **rama experimental
aparte, comprometida como jornada (ADR-017)**: sus resultados, si existen a la entrega,
se rotulan como rama comparativa y nunca se funden con el núcleo zero-shot.

---

### AJ-1.16 · §16 Marco Teórico · EVIDENCIA · 🟡 — hueco declarado

**El §16 no fue relevado contra el estado actual del proyecto.** Todo el relevamiento
de Etapa 1 se concentró en el §15 y en el Anexo A. Antes de dar la etapa por cerrada
hay que pasar el §16 (`entregable/96d`) contra `sintesis/fundamentos-teoricos.md`, que
es la versión hoy vigente de la teoría del trabajo, y anotar acá lo que aparezca.

Esto es un hueco de relevamiento, **no** una afirmación de que el §16 esté bien.

---

## 4. 🚫 Lo que no hay que tocar en esta etapa

- **Las cifras ancla verificadas.** La verificación externa **confirmó** GDINO 52,5 AP
  COCO / 26,1 mean AP ODinW [P]; YOLO-World-L 35,4 AP LVIS @ 52 FPS [P]; YOLOE-v8-S/L
  27,9/35,9 AP LVIS @ 305,8/102,5 FPS T4-TensorRT [P/S]; GDINO 1.5 Pro 54,3/55,7 y Edge
  36,2 @ 75,2 FPS [S]. Están bien: lo que falta es el backbone (AJ-1.03) y el cruce
  (AJ-1.02).
- **La estructura del §15** (4 paradigmas · ~25 modelos · Tabla 3 · Tabla A.1) y los
  criterios de selección de §17.1.9.2, que fundan el par GDINO+YOLOE como polos del
  trade-off expresividad semántica ↔ latencia. El encuadre es correcto y sobrevive.

## 5. Fuentes

`sintesis/resultados-y-conclusiones.md` §7.1–§7.4 (relevamiento y verificación externa
del 2026-08-06, con el listado completo de arXiv/DOI consultados) ·
`sintesis/fundamentos-teoricos.md` · `entregable/96c`, `96d`, `96e` §19.1.

---

## Fuente: `docs/informe/entregable/borradores/vara-15.md`

> SHA-256 del bloque: `d82aac011a58729e9bf7aeae19bf8147734f7704b635b7140ec18d7c4ba0d496`  
> Seleccion: borrador listo para integrar: la vara del 15 (AJ-1.01/1.02/1.13).

# Borrador — la vara del §15 (AJ-1.01 · AJ-1.02 · AJ-1.13)

> **Qué es esto (2026-08-16).** Borrador *texto listo para copiar* (patrón del doc `94`)
> redactado según el ✎ 2026-08-16 del manual `ajustes/08` §2: la vara del §15 se adelanta
> como borrador para desbloquear el §17.5; **los colegas la revisan e integran en Google
> Docs** (D-A híbrida: la §15 existe, así que la edición final es en el documento). La
> decisión fina de anclaje es de quien integra; acá va la propuesta.
>
> **Regla cumplida:** cero cifras propias del proyecto (no-anacronismo, mapa `00` regla 5).
> Todo lo que sigue es literatura, con la métrica de cada cifra declarada al lado
> (evita de paso la trampa de AJ-1.12: nunca mezclar AP 0,50:0,95 con mAP@0,5).
>
> **Al integrar:** marcar `AJ-1.01`/`AJ-1.02`/`AJ-1.13` en el tablero (manual `08` §5),
> anotar cualquier desvío como ✎ en la ficha (`ajustes/01`), sumar las referencias del
> §4 de este borrador al listado del `96e`, y re-extraer la foto de §15
> (`herramientas/extraer_informe.py`, regla D-C).

---

## 1. Dónde ancla cada bloque

| Bloque | Ajuste | Punto de inserción propuesto |
|---|---|---|
| Bloque A — Vara 1, la línea base supervisada | `AJ-1.01` 🔴 | **§15.2.5**, al comienzo: antes de declarar brechas, fijar qué logra lo supervisado in-domain |
| Bloque B — la pregunta que los benchmarks generales no responden | `AJ-1.02` 🔴 | **§15.2.5**, a continuación del Bloque A · más la **nota al pie de la Tabla 3** (§15.2.3) |
| Bloque C — Vara 3, el cruce OVD×EPP | `AJ-1.13` 🟠 | **§15.2.5**, cierre de la subsección: la brecha queda declarada |

Los tres bloques forman una secuencia narrativa única dentro de §15.2.5 (vara supervisada
→ pregunta de generalización → brecha del cruce), así que conviene integrarlos en un solo
pase. La subsección existente se conserva; esto se intercala donde hoy la brecha se
menciona sin cifras.

---

## 2. Los tres bloques, texto listo para copiar

### Bloque A — la línea base supervisada in-domain (AJ-1.01)

La detección de EPP con modelos supervisados entrenados in-domain constituye una línea
base madura, con cifras publicadas sobre los mismos conjuntos de datos que este trabajo
adopta como fuentes. Sobre SHEL5K, Otgonbold et al. (2022) reportan para YOLOR un
mAP@0,5 de **0,883**, con **0,907** para la clase *head* (cabeza sin casco); sobre CHV,
Wang et al. (2021) reportan para YOLOv5x un mAP@0,5 de **0,866** sobre seis clases
(persona, chaleco y cuatro colores de casco). En conjuntos de mayor vocabulario el techo
desciende: en SH17 (2024; 17 clases de entorno industrial), YOLOv9-e alcanza
aproximadamente **0,71** de mAP@0,5, y la familia YOLOv8 (variantes n a x) se ubica entre
**0,58 y 0,69**.

Dos lecturas de esta vara importan para lo que sigue. Primero, la detección supervisada
de EPP es un problema esencialmente resuelto en su formulación estándar: con
entrenamiento in-domain, las clases centrales superan 0,85 de mAP@0,5. Segundo — y es el
dato fino que esta vara deja establecido —, la clase *cabeza sin casco*, que podría
suponerse difícil por su granularidad semántica, **no lo es para un detector
supervisado**: 0,907 en SHEL5K, por encima incluso del promedio del conjunto. Cualquier
dificultad que aparezca sobre esa clase por otras vías de detección no podrá atribuirse,
entonces, a la clase en sí.

### Bloque B — la pregunta que los benchmarks generales no responden (AJ-1.02)

Los modelos open-vocabulary del presente capítulo se comparan habitualmente por sus
cifras sobre benchmarks generales (COCO, LVIS; Tabla 3). Esas cifras responden cuánto
generaliza el modelo *sobre la distribución de esos benchmarks*, pero dejan sin
responder la pregunta que este trabajo necesita: **¿predicen los benchmarks generales el
rendimiento sobre una condición de dominio específica?** La evidencia publicada sugiere
que no. El propio equipo de Grounding DINO reporta que su variante grande, con ~52 AP
(COCO, 0,50:0,95) en el benchmark general, cae a **26,1 de mean AP sobre los 35
datasets de ODinW** (Liu et al., 2023) — la referencia publicada de cuánto colapsa un
detector open-vocabulary fuera de distribución. Y cuando la consulta exige composición
léxica fina — atributo o negación, del tipo *"trabajadores con casco blanco"* —, Chen
et al. (2025) miden sobre escenas de construcción que los modelos de
grounding quedan por debajo de **20% de IoU**: el preentrenamiento no resuelve por sí
solo la composición.

De ambas evidencias queda una conclusión que este capítulo puede firmar: **los
benchmarks generales no garantizan el rendimiento sobre la condición de dominio, y no
existe benchmark publicado del cruce entre detección open-vocabulary y EPP** (§15.2.5,
cierre). Esa brecha es la que justifica la decisión metodológica, adoptada en el
protocolo experimental (§17.1.9.2), de exigir una línea base zero-shot propia sobre un
conjunto de evaluación congelado, en lugar de seleccionar modelos por sus cifras
publicadas.

**Nota al pie propuesta para la Tabla 3 (§15.2.3):** *Las cifras de precisión de esta
tabla corresponden a benchmarks generales (COCO/LVIS, AP 0,50:0,95 salvo indicación) y
no son directamente trasladables a una condición de dominio específica; la validez de
esa extrapolación se discute en §15.2.5.*

### Bloque C — la Vara 3: el cruce OVD×EPP está casi vacío (AJ-1.13)

El cruce entre detección open-vocabulary y EPP en obra cuenta con una única cifra
publicada directamente comparable con una evaluación por clase a AP@0,5: Choi y Greer
(2024) miden OWLv2 zero-shot sobre 5.210 imágenes de obra y reportan **0,649 para
*hardhat*** y **0,677 para *person*** (AP a IoU>0,5). Sobre la composición con atributo,
la evidencia citada arriba (Chen et al., 2025; IoU <20%) confirma que la vía léxica fina
está lejos de resuelta. Fuera de esas dos piezas, la revisión efectuada no encontró
**ningún trabajo publicado entre 2023 y 2026 que mida Grounding DINO ni YOLO-World
zero-shot sobre SHEL5K o CHV, ni sobre un benchmark de EPP multi-fuente con protocolo
COCO**. La comparación entre la vara supervisada del Bloque A (mAP@0,5 ≥ 0,86 con
entrenamiento in-domain) y la única cifra zero-shot disponible (0,649 en la clase más
favorable) queda, por lo tanto, sin un puente publicado: **esa es la brecha que el
estado del arte deja declarada**.

---

## 3. Qué NO va acá (y dónde vive)

- La confirmación **medida** de la brecha (el caso YOLOE: 35,9 AP LVIS publicado vs el
  recall propio; los G2A medidos vs la columna de latencia derivada) es material de
  **§17.5**, escrito en tres tiempos contra esta vara (`AJ-5.11`).
- Que `bench_v3` **ocupa** la brecha declarada es lectura de §17.5/§18, no del §15.
- La lectura de la clase `bare_head` contra la vía léxico-conceptual (AF-5) también:
  acá queda solo el fundamento externo (head 0,907 supervisado).

## 4. Referencias a incorporar al listado del `96e`

Verificadas 2026-08-06 (listado de `sintesis/resultados-y-conclusiones.md` §7.4):

- Otgonbold, M.-E. et al. (2022). *SHEL5K: An Extended Dataset and Benchmarking for
  Safety Helmet Detection*. **Sensors 22(6):2315**.
- Wang, Z. et al. (2021). *Fast Personal Protective Equipment Detection for Real
  Construction Sites Using Deep Learning Approaches*. **Sensors 21(10):3478** (dataset CHV).
- SH17 (2024). *Dataset for human safety and PPE detection in manufacturing industry*.
  **arXiv:2407.04590**.
- Liu, S. et al. (2023). *Grounding DINO: Marrying DINO with Grounded Pre-Training for
  Open-Set Object Detection*. **arXiv:2303.05499** (cifra ODinW-35).
- Choi, J. & Greer, R. (2024). *Language-guided zero-shot object detection: OWLv2 sobre
  hardhat en obra*. **arXiv:2410.12225**.
- Chen et al. (2025). *ConstructionSite-10k: grounding con atributo y negación en escenas
  de construcción*. **arXiv:2508.11011**.

> ⚠️ Al integrar en el `96e`, unificar el formato con el listado existente (AJ-1.10:
> hoy conviven Liu 2023/2024 y variantes). Los títulos de Choi & Greer y Chen 2025
> están parafraseados acá — **verificar el título exacto contra el arXiv al citarlos**.

---

## Fuente: `docs/informe/ajustes/07-critica-extension-y-poda.md`

> SHA-256 del bloque: `f0bc2cab64b1686d1abb153948f5386d72eaa38183b8ec0465f820c8f88602b8`  
> Seleccion: podas 01 a 11 aplicables a las secciones 15 y 16.

## 3. §15 Estado del Arte (21.575 palabras)

### PODA-01 · §15.2.1 Paradigmas y modelos (4.530) · C5 · 🟠
El catálogo trae **~25 modelos con cifras COCO/LVIS**; el trabajo evaluó **tres familias**
(GDINO, MM-GDINO, YOLOE) y tiene **un** comparable externo (OWLv2). Comprimir a: los 4
paradigmas en un párrafo cada uno + ficha solo de los modelos con rol en el trabajo
(GDINO/MM-GDINO/YOLO-World/YOLOE/OWLv2 · GDINO 1.5/DINO-X como techo de API cerrada) +
la Tabla 3 reducida a esas filas. Beneficio doble: **menos superficie de erratas** — las
AJ-1.04…08 viven justo en las filas que se van (OmDet-Turbo, LLMDet, el caching de 40 ms).
**Ahorro: ~2.000** · DECISIÓN → [ ] acepto [ ] modifico [ ] rechazo

### PODA-02 · §15.2.4 Ventajas/limitaciones/trade-offs (2.764) · C3/C4 · 🟠
Solapa con §15.2.3 (síntesis comparativa, 1.153) y con §16.7. Fusionar 15.2.3+15.2.4 en
una sola síntesis de ~1.200 con tabla. **Ahorro: ~1.500** · DECISIÓN → [ ]

### PODA-03 · §15.3 MOT completo (2.484) · C1 · 🟠
La plataforma **no evalúa MOT**: E-10 excluye MOTA/IDF1 con causa medida, y el tracker
que existe se mide por alertas. Mantener ~800: tracking-by-detection en un párrafo (es lo
que fundamenta G1) + la brecha. **Eliminar §15.3.3 entero** (métricas MOT, 385 — no se
usa ni una) y podar el catálogo de métodos (§15.3.1–15.3.2) a los dos que expliquen el
approach del tracker propio. **Ahorro: ~1.600** · DECISIÓN → [ ]

### PODA-04 · §15.4 Streaming y servidores de medios (7.998) · C1/C2 · 🔴 la mayor
**La sección más desalineada del informe.** 4.041 palabras de protocolos (WebRTC, HLS,
SRT, …) + 2.594 de comparativa de servidores de medios open source + criterios — y la
decisión final fue: **RTSP como ingesta, ZeroMQ+msgpack como bus interno (ADR-003),
mediamtx solo como herramienta de desarrollo, archivo JSONL como verdad**. Ni WebRTC ni
HLS ni la comparativa de servidores sostienen una sola decisión del sistema construido.
Comprimir a ~1.200: panorama mínimo de protocolos de **ingesta** + la brecha
streaming×OVD (§15.4.3, que sí vale). La *justificación de la decisión tomada*
(RTSP en la entrada, bus de eventos adentro) no va acá: es material de §17.1/§17.3
(regla de no-anacronismo — el §15 no relata elecciones del proyecto).
**Ahorro: ~6.800** · DECISIÓN → [ ]

**Lo que el §15 GANA mientras pierde esto:** la vara supervisada (AJ-1.01), el cruce con
la evidencia propia (AJ-1.02) y la Vara 3 OVD×EPP (AJ-1.13). La poda no deja al §15 más
flaco de contenido útil — lo deja con el contenido que la defensa necesita.

---

## 4. §16 Marco Teórico (31.732 palabras)

### Lo que NO se toca (y por qué)
- **§16.3 Percepción visión-lenguaje (2.594)** — es el **corazón conceptual de la
  tesis** (el lenguaje como especificación dinámica; sostiene AF-2/AF-5 y toda la
  narrativa léxico-conceptual). Intacta.
- **§16.2 Condiciones de riesgo observables (3.100)** — es lo que ancla CR-01/CR-02 a la
  normativa; sin esto las condiciones son arbitrarias. A lo sumo podar §16.2.3 (~300).
- **§16.5.1 Latencia end-to-end como restricción (494)** — el eje de tiempo real ES
  central a los resultados (G2A, densidad live). La poda de §16.5 es de *surveys*, no
  del concepto.

### PODA-05 · §16.4 MOT teórico (2.769) · C1/C3 · 🟠
Segunda casa del MOT. Mantener §16.4.1 (la limitación del fotograma — motiva la
histéresis) y §16.4.3 (integración OVD+tracking — motiva G1); comprimir §16.4.2
(fundamentos MOT, 1.600 → ~700) y **eliminar §16.4.4** (criterios de selección de
métodos MOT, 487 — no hubo selección de método de catálogo). **Ahorro: ~1.400** ·
DECISIÓN → [ ]

### PODA-06 · §16.5.2 Descomposición del pipeline (4.874) · C3 · 🔴
Mantener lo que **define G2A y sus componentes** (t_capture/t_transport/t_preprocess/
t_inference — es vocabulario que §17.1.7 y los resultados usan): ~1.400. El resto
duplica lo que §17.1.7 ya formaliza como framework de métricas. **Ahorro: ~3.400** ·
DECISIÓN → [ ]

### PODA-07 · §16.5.3 Arquitecturas de procesamiento de video (3.594) · C1/C2 · 🔴
Survey de frameworks/arquitecturas de video analytics — y la plataforma es **un pipeline
Python propio de dos servicios config-driven**. Comprimir a ~600: el patrón
productor/consumidor como fundamento conceptual; la elección concreta (pipeline propio,
no framework) se justifica en §17.3, no en el marco teórico. **Ahorro: ~3.000** ·
DECISIÓN → [ ]

### PODA-08 · §16.5.4 Computación en el borde (2.729) · C1 · 🔴
**EN-3 (inferencia en borde) está excluida.** Lo ejercido es el prefilter EN-2 on-device
(87% de descarte medido) y la OAK-D como fuente. Comprimir a ~700: el fundamento
**conceptual** del prefiltrado en el borde; la decisión de dónde vive la inferencia (y su
resultado medido) pertenecen a §17.3 y §17.5. **Ahorro: ~2.000** · DECISIÓN → [ ]

### PODA-09 · §16.5.5 Criterios para protocolos y stacks de streaming (1.686) · C2 · 🔴
Criterios de selección para una selección que ya ocurrió y colapsó (ver PODA-04). Un
párrafo puente a la decisión tomada. **Ahorro: ~1.400** · DECISIÓN → [ ]

### PODA-10 · §16.6 Marco ético-legal (4.364) · C5 parcial · 🟠
Tiene núcleo vivo: §16.6.2 (delimitación del tratamiento de datos — **implementada** en
§17.3.12, minimización de evidencia visual) y §16.6.6 (implicaciones de diseño). Podar lo
genérico: §16.6.4 referentes comparados (422), §16.6.5 gobernanza de IA (499), y
comprimir §16.6.7 (955 → ~400). **Ahorro: ~1.400** · DECISIÓN → [ ]

### PODA-11 · §16.7 Convergencias y brechas transversales (4.429) · C4 · 🔴
**Meta-texto puro**: seis subsecciones que re-resumen el propio §16 y anticipan §17.1
("convergencias del análisis", "lectura arquitectónica integrada", "proyección hacia la
consolidación"). El lector ya leyó el §16 y va a leer el §17.1; este puente de 4.400
palabras no aporta contenido nuevo. Fusionar con §16.8 en un cierre único de ~1.000
(el mapa de brechas de §16.7.3 es lo único que se rescata, comprimido). **Ahorro:
~3.400** · DECISIÓN → [ ]

---

---

## Fuente: `docs/sintesis/fundamentos-teoricos.md`

> SHA-256 del bloque: `59f89d6fbeff40e2ea805a21ee051a3429aacdfef6feeb9715658516207980eb`  
> Seleccion: documento completo.

# Fundamentos teóricos — entender la plataforma y sus resultados de punta a punta

- **Fecha:** 2026-08-06 · **Rol:** documento de estudio, **100% teórico-conceptual**.
- **Para qué existe:** poder explicar ante el jurado *qué* se construyó, *por qué* se
  construyó así, *cómo* se midió y *por qué* los resultados dan lo que dan. Cada
  sección desarrolla la teoría mínima y la conecta con la decisión o el resultado
  concreto del proyecto.
- **Compañeros de lectura:** los números viven en
  `resultados-y-conclusiones.md` (fuente: `docs/sintesis/resultados-y-conclusiones.md`) (mismo directorio) y
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

