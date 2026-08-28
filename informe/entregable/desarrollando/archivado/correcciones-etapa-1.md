# Correcciones a la Etapa 1 — §15 Estado del Arte

- **Fecha:** 2026-08-27 · **Sobre:** `Etapa 1.docx` (§15 completo, 22.169 palabras).
- **Para quién:** el redactor de la Etapa 1. El equipo de plataforma **no edita** esta
  sección; este documento dice **qué ajustar y contra qué**.
- **Objetivo del pase:** que el estado del arte quede **alineado con el proyecto que se
  construyó** — que cada modelo, método y protocolo que el §15 desarrolla tenga un rol en la
  tesis, y que cada resultado que el informe va a reportar más adelante (§17.5) tenga en el
  §15 su **vara** de literatura o su **brecha** declarada.
- **Regla que gobierna todo el pase — no-anacronismo:** el §15 narra el estado del arte
  *antes* del proyecto. **No entra ningún número medido por nosotros, ningún experimento
  propio, ninguna elección de diseño.** El §15 deja la vara (cifra publicada) o la brecha
  (lo que la literatura no responde); el cruce con lo medido se escribe en §17.5 y §18.
  Cuando abajo se cita una cifra del proyecto, es solo para explicar *qué vara falta* — esa
  cifra **no** va al §15.
- **IDs:** `E1-nn` comentarios (con prioridad 🔴 alta · 🟠 media · 🟡 baja) ·
  `PODA-nn` remite a la crítica de extensión ya existente (`ajustes/07`).

---

## 0. Alcance del archivo

**`Etapa 1.docx` cubre 1 de las 3 piezas de la Etapa 1.** La Etapa 1 del informe es
**§15 + §16 (Marco Teórico) + Anexo A**. El archivo trae §15 completo, nada de §16 y ninguna
tabla del Anexo A (las cita: "Tabla A.1", "Tabla A.3"). Tres consecuencias:

1. **§16 y Anexo A deben llegar como Etapa 1**, no como parte de la etapa siguiente
   (§17.1). El §16 todavía no fue relevado (`AJ-1.16`).
2. La corrección de licencias de GDINO 1.5 / DINO-X (`AJ-1.09`) quedó bien **en la prosa**
   del §15, pero la **Tabla A.1**, donde estaba la errata, no se puede verificar desde este
   archivo. Confirmar que también se corrigió.
3. El §15 apunta hacia adentro del §16 tres veces ("sección 16.5.1", "16.5.2.3 y 16.5.2.5")
   y una vez a algo que no existe en el §15 ("el modelado de apariencia descrito en el
   análisis del modelado de apariencia", §15.3.1.2). El §16.5 va a reestructurarse
   (PODA-06…09): **cerrar §15 y §16 juntos** para que estos punteros no queden rotos.

---

## 1. Qué es la plataforma (el blanco de la alineación)

Descripción en llano de lo que se construyó y midió, para decidir qué del §15 sostiene algo
y qué no. Todo esto está verificado en el código de los repositorios.

| Componente | Lo que se implementó | Lo que **no** se implementó |
|---|---|---|
| **Detectores** | Grounding DINO en dos backbones — **Swin-T** (campeón, a 560 px) y **Swin-B** (especialista en `bare_head`, a 560 px) — y **YOLOE-26** en tallas s/m/l/x (release de Ultralytics posterior al paper). MM-Grounding-DINO se evaluó y se descartó. | Ningún otro modelo del catálogo (OmDet-Turbo, OWL, Detic, Florence-2, APE, LLMDet, T-Rex2, Grounded SAM…). Sin segmentación. |
| **Uso de los modelos** | **Zero-shot** con calibración operativa: resolución, vocabulario (prompt sets congelados), umbrales, estabilización temporal. | — |
| **Fine-tuning** | Jornada experimental cerrada sobre **YOLOE-26s**, con las **dos recetas estándar de Ultralytics**: *linear probing* (solo la proyección de clases) y *full tuning*. Se **midió** la retención in-domain y la retención open-vocabulary. Ningún checkpoint se adoptó. | No se ajustó Grounding DINO. |
| **Identidad por sujeto (tracking)** | Tracker **propio y mínimo**: asociación por IoU entre cuadros, **sin filtro de Kalman ni modelo de apariencia**, determinista. Su valor se mide por su efecto en las alertas, **no con MOTA/IDF1/HOTA** (métricas MOT excluidas del alcance con causa). | Ni ByteTrack, ni OC-SORT, ni DeepSORT, ni end-to-end en la plataforma. (ByteTrack se usó solo como herramienta de preanotación de ground truth.) |
| **Ingesta de video** | **RTSP** (cámaras IP) y **captura por SDK** de una cámara inteligente (OAK-D, con prefiltrado en el dispositivo). Servidor de medios (`mediamtx`) solo como herramienta de desarrollo. | Ni WebRTC, ni HLS/DASH, ni RTMP, ni SRT, ni RIST, ni servidor de medios en producción. Sin inferencia en el borde. |
| **Interior del sistema** | Bus de eventos publish/subscribe entre el plano de detección y el motor de reglas (condiciones CR-01 sin casco / CR-02 sin chaleco, con histéresis temporal). | — |
| **Salida** | Alertas confirmadas distribuidas por **MQTT QoS 1** con idempotencia; consola web. | — |
| **Evaluación** | Benchmark de imágenes propio y congelado (3 fuentes, 6.477 imgs), benchmark de clips con GT humano, latencia extremo a extremo (G2A), tasa de falsas alarmas, persistencia mínima. | Métricas MOT. Benchmarks generales (COCO/LVIS) solo como referencia externa. |

---

## 2. Alineación: qué ajustar en cada bloque

### 2.1 §15.2 Detección OVD — bien encuadrado, con huecos de vara

El §15.2 ya dejó bien puestas la vara supervisada de EPP (YOLOR 0,883 SHEL5K con `head`
0,907; YOLOv5x 0,866 CHV; YOLOv9-e ≈0,71 SH17), la vara zero-shot OVD×EPP (Choi & Greer
2024; Chen & Zou 2025), la caída COCO→ODinW de GDINO, la convención de métricas
(AP 0,50:0,95 vs mAP@0,5, nunca en la misma columna) y la distinción "calibración operativa
vs adaptación paramétrica". Eso **no se toca**. Lo que falta:

**E1-01 · 🟠 · Swin-B no tiene vara.** El proyecto despliega **dos** backbones de Grounding
DINO y el §17.5 reportará ambos. El §15 da la cifra zero-shot de Swin-L (52,5 COCO) y de
Swin-T (≈48,4) pero **no menciona Swin-B**. Ojo con la trampa: la cifra publicada del
GroundingDINO-B en el README oficial (~56,7 AP COCO) **no es zero-shot** — COCO figura entre
sus datos de preentrenamiento (verificar en la fuente). Pedido: una oración en §15.2.1.1.3
que diga que la variante Swin-B se distribuye con pesos abiertos pero **sin cifra zero-shot
comparable**, y por qué. Sin esa oración, el §17.5 no tiene vara honesta para el
especialista.

**E1-02 · 🟡 · YOLOE-v8 (paper) vs YOLOE-26 (plataforma).** El §15 cita YOLOE-v8-S/L
(Wang et al., 2025). La plataforma corre **YOLOE-26**, release posterior de Ultralytics
sobre YOLO26 sin paper propio. Pedido: decir que la familia tiene variantes v8/11/26 y que
las cifras publicadas corresponden a v8; si no, el §17.5 compara `yoloe-26s` contra la vara
de v8-S sin aviso.

**E1-03 · 🟠 · Tabla 4, fila YOLOE — contradicción latente con §17.5.** La fila dice:
*Transferring (linear probing / full tuning) → Retención OVD "No" → "Modelo reparametrizado
como YOLO estándar"*. El proyecto ejerció **exactamente esas dos recetas** y **midió** la
retención open-vocabulary como un número. Si el §15 afirma "No" absoluto por
reparametrización, el §17.5 va a reportar una retención medida y el lector verá una
contradicción (¿cómo se mide lo que no existe?). Reformular, sin adelantar nada: *"No
evaluada por los autores; la receta estándar produce un modelo de vocabulario fijo; la
retención debe medirse re-inyectando el vocabulario abierto sobre el modelo ajustado."* Ese
enunciado es el que el §17.5 puede confirmar o refutar.

**E1-04 · 🟡 · §15.2.4.5 pesa donde no se ejerció.** ~60 % del texto de fine-tuning
desarrolla recetas para Grounding DINO (las tres estrategias de MM-GDINO, LoRA en imagen
médica). La jornada fue sobre YOLOE. No es un error — GDINO es el campeón y la brecha se
declara — pero la vara que el §17.5 va a citar es la del Bloque B (YOLOE), que hoy tiene
menos desarrollo. Equilibrar. Además, el resultado del fine-tuning se va a explicar por la
relación entre **tamaño del conjunto de ajuste y parámetros entrenables**; hoy la única
frase que lo ancla es "PEFT relevante para datasets de dominio reducidos". Agregar una
oración con fuente sobre esa relación como condición de la retención. *(Sin cifras
nuestras.)*

**E1-05 · 🟠 · El Bloque D está mal rotulado.** Título: "Modelos generativos guiados por
instrucciones". De sus 4 modelos, **3 no son generativos en inferencia**, y el propio texto lo
dice: APE "no depende de decodificación autoregresiva, produciendo predicciones estructuradas
de manera directa"; LLMDet "en inferencia opera como un detector OVD convencional sin LLM";
T-Rex2 "entra en el Bloque D por su foco en prompting generalista multimodal". La Tabla 2 lo
agrava: fila "Generativo guiado por instrucciones" con mecanismo "APE: predicción directa con
alineamiento por producto punto". Un jurado atento lo ve. Renombrar el bloque (por ejemplo
*"Modelos guiados por prompts generalistas: generativos e híbridos"*) y corregir la fila de
la Tabla 2; alternativa: mover APE/T-Rex2 al Bloque A y LLMDet a la ficha de MM-GDINO.

**E1-06 · 🟡 · Duplicación interna (es la superficie de PODA-01/02).** La introducción de
§15.2.1 (párrafos 2–8) ya describe GDINO, OmDet-Turbo, YOLO-World, YOLOE, OWL-ViT y Florence-2
con las mismas cifras que sus fichas de más abajo (52,5 AP; 35,9 AP a 102,5 FPS; etc.).
Criterio: los paradigmas en la introducción; **fichas completas solo para los modelos con rol
en la tesis** (Grounding DINO y MM-GDINO · YOLO-World y YOLOE · OWLv2 como único comparable
externo zero-shot sobre obra · GDINO 1.5/DINO-X como techo de API cerrada). El resto, una
línea en la Tabla A.1. La Tabla 3 se reduce a esas filas — y con ella se van las cifras aún
sin verificar de OmDet-Turbo (ver §3).

### 2.2 §15.3 Seguimiento multiobjeto — la recomendación del texto no es lo que se construyó

**E1-07 · 🟠 · §15.3.2.1 recomienda un método que el diseño no adoptó.** El cierre dice que
"ByteTrack y OC-SORT representan alternativas particularmente equilibradas" y que "la
familia SORT extendida se presenta como la opción más adecuada". La plataforma usa algo
**más simple que SORT** (asociación IoU, sin modelo de movimiento) y lo mide por alertas.
Cuando el §17.3 lo describa, el lector que vuelva al §15 verá que el estado del arte
"recomendaba otra cosa". El §15 no debe elegir método (eso es del diseño): reescribir el
cierre en clave de **criterios** — independencia respecto del detector, determinismo y
reproducibilidad, costo nulo de entrenamiento, transparencia para auditoría — que son los
que fundan lo construido, sin nombrar ganador. La ficha de SORT (tracking-by-detection +
IoU + asignación) es la vara conceptual que queda; los demás métodos, comprimidos en la
Tabla 6.

Erratas del bloque: "FairMOT" aparece en §15.3.2.1 sin haber sido introducido (la sección
presenta TrackFormer/MOTR) · §15.3.1.2 refiere a "el análisis del modelado de apariencia",
que no existe en el §15.

**E1-08 · 🟡 · §15.3.3 métricas MOT — comprimir, no eliminar (matiz a PODA-03).** PODA-03
pide eliminar §15.3.3 entero. Matiz: la tesis **excluye** MOTA/IDF1/HOTA con causa, y para
que el §17.1/§17.5 justifiquen esa exclusión el lector tiene que saber qué miden esas
métricas y por qué no capturan valor operativo. Ese argumento (último párrafo de §15.3.3.3)
es el que motiva medir por alerta. Dejar ~120 palabras: las tres métricas en una oración
cada una + ese párrafo. La ecuación (1) y las tres subsecciones sobran.

**E1-09 · 🟡 · Tabla 7.** La fila "ausencia de datasets de construcción con anotaciones de
tracking → protocolo propio con datos del proyecto" está **alineada** (el proyecto construyó
ese GT) — se queda. La fila "ausencia de semántica en identificadores… correlación
inter-cámara" está fuera del alcance (una cámara) — podable.

### 2.3 §15.4 Streaming — comprimir fuerte, con una excepción

**E1-10 · 🔴 · Aplicar PODA-04, conservando RTSP/RTP íntegro y §15.4.3 entero.** El §15.4
tiene **8.068 palabras** (protocolos 4.054 · servidores de medios 2.616) para una ingesta que
es **solo RTSP + SDK de cámara**. Ni WebRTC, ni HLS/DASH/CMAF, ni RTMP, ni SRT, ni RIST, ni
Janus/Kurento/OME/SRS sostienen una decisión del sistema construido. **Excepción, que la
crítica de extensión no había marcado:** el párrafo de RTSP/RTP (latencia ~200–800 ms en
condiciones favorables, dominada por el *play-out buffer* del receptor — Axis 2015) es la
**única vara de literatura** para la latencia de captura que el §17.5 va a reportar y para la
regla de que la latencia extremo a extremo se descompone en captura + procesamiento. **Ese
párrafo se queda entero.** Y **§15.4.3 (brechas) se queda entero**: §15.4.3.1 "ausencia de
benchmarks end-to-end integrados para pipelines OVD" es exactamente la brecha que la
medición de latencia del proyecto ocupa — es de las mejores piezas del §15. Todo lo demás se
comprime a una tabla-mapa de protocolos de ingesta (la Tabla 8 ya casi lo es) más un párrafo
de criterios. La *justificación* de la elección (RTSP en la entrada, bus de eventos adentro)
no va acá: es del §17.1/§17.3.

**E1-11 · 🟠 · Falta la vara de dos cosas que sí se construyeron.**
(a) **Ingesta por SDK de cámara inteligente** (OAK-D, prefiltrado en el dispositivo): el
§15.4 solo conoce protocolos de red. Si la cobertura vive en §16.5.4 (borde), el §15.4 debe
al menos nombrar la captura por SDK como alternativa al stream de red.
(b) **Distribución de alertas por mensajería pub/sub (MQTT QoS 1)**: es un componente
implementado y medido y **no tiene una sola línea de estado del arte** — ni protocolos de
mensajería IoT, ni garantías de entrega, ni idempotencia. §15.4.3.4 habla de "la
notificación al operador" sin fuente. Un párrafo con fuente, o dejar declarado que lo cubre
el §16/§17.3. Sin vara, la latencia de distribución que reporte el §17.5 queda flotando.

**E1-12 · 🔴 · Texto de instrucción colado al informe.** §15.4.1.2 (RTMP): *"Esto es clave
para la plantilla: cuando el documento menciona latencias, debe quedar claro que…"*. Es una
directiva de redacción, no prosa del informe. Eliminar. Es 🔴 no por gravedad técnica sino
porque delata el proceso ante el jurado.

Erratas del bloque: "jitter en el receptor.." (doble punto) · "Ahmad et al., 2005" es un
paper de **transcodificación** y está citado para "el comportamiento bajo carga" de Janus
(§15.4.2.5) — atribución errónea; bastan Amirante 2014/2015 · Tabla 8 rotula RTSP/RTP como
"Pull" mientras §15.4.1.1 alinea RTP con *push* (RTSP controla, RTP empuja: decirlo así o
unificar).

### 2.4 Lo que está bien alineado — no tocar

- §15.2.5.1 contextualización limitada → justifica un motor de reglas sobre las detecciones. ✔
- §15.2.5.2 sin consistencia temporal nativa → justifica estabilización temporal e identidad
  por sujeto. ✔
- §15.2.5.3 sensibilidad al prompt → justifica prompt sets congelados; y Choi & Greer
  (asociación jerárquica: `head` 0,1024 vs `hardhat` 0,6493) es la vara natural para
  comparar formulaciones directas e indirectas del vocabulario. ✔
- §15.2.5.4 / §15.2.5.5 → baseline zero-shot propia, test congelado, latencia de alerta,
  tasa de falsas alarmas, persistencia mínima: es exactamente el protocolo que se ejerció. ✔
- §15.2.2 composición de pipelines → la arquitectura **es** composición (detector + tracker
  + motor de reglas + distribución). ✔ El ejemplo es Grounded SAM y no hay segmentación en la
  tesis: podable a la mitad, conservando la idea.
- §15.2.6 calibración operativa vs adaptación paramétrica → el encuadre correcto. ✔

---

## 3. Pendientes del pase de corrección anterior

Del tablero `AJ-1.01…1.16` quedaron **12 resueltos**. Falta:

| ID | Qué falta |
|---|---|
| AJ-1.04 | OmDet-Turbo-Tiny "30,3 AP LVIS-minival" (Tabla 3 y ficha): probable *mislabel* de ODinW-13. Verificar contra el paper y corregir o anotar. (Si se aplica E1-06, la fila se va.) |
| AJ-1.05 | OmDet-Turbo-Base "53,4 AP COCO bajo evaluación zero-shot": verificar que sea zero-shot; si no, etiquetar. |
| AJ-1.09 | Confirmar la Tabla A.1 del Anexo A (la prosa ya está bien). |
| AJ-1.16 | Relevar el §16 — llega con la segunda pieza de la Etapa 1. |
| Cifra nueva | "Grounding DINO Swin-L alcanza 63,0 AP en COCO tras fine-tuning closed-set" (§15.2.4.5) entró sin pasar el filtro de verificación. Plausible (paper: 62,6 val / 63,0 test-dev): declarar el split. |

---

## 4. Poda: el pase no se aplicó

La crítica de extensión (`ajustes/07`) fijó que la poda se aplica **en el mismo pase** que las
correcciones. Ese pase no vino:

| Bloque | Palabras hoy | Poda propuesta | Aplicada |
|---|---:|---|---|
| §15 total | 22.169 | ~−11.900 | no |
| §15.2.1 catálogo de modelos | 4.777 | PODA-01 −2.000 (ver E1-06) | no |
| §15.2.3 + §15.2.4 síntesis duplicada | 3.877 | PODA-02 fusionar en una, −1.500 | no |
| §15.3 MOT | 2.530 | PODA-03 −1.600 (ver matiz E1-08) | no |
| §15.4 streaming y servidores | 8.068 | **PODA-04 −6.800** (ver excepción E1-10) | **no** |

El criterio de poda **no es cuota, es aporte**: una sección se queda si sostiene un
resultado, una decisión de diseño o un argumento de defensa. Las adiciones de vara
(AJ-1.01/1.13, E1-01/02/11) mandan sobre las podas: la poda les hace lugar.

---

## 5. Decisiones del equipo (marcar antes de enviar)

| ID | Decisión | Recomendación | ✔ |
|---|---|---|---|
| D-E1-1 | ¿La poda de §15 se aplica **en este pase** o en un pase transversal al final? | En este pase. §16 es Etapa 1 también y trae PODA-05…11; los punteros §15→§16.5 se arreglan una sola vez. | [ ] |
| D-E1-2 | ¿§16 y Anexo A llegan como **Etapa 1**, antes de §17.1? | Sí, en un `.docx` propio. | [ ] |
| D-E1-3 | Excepción a PODA-04: conservar RTSP/RTP íntegro y §15.4.3 entero. | Sí. Anotar la enmienda en `ajustes/07`. | [ ] |
| D-E1-4 | Tabla A.1: confirmar licencias corregidas y resolver PODA-17. | Migrar la Tabla A.1 corregida al Anexo B; eliminar el resto del Anexo A. | [ ] |
| D-E1-5 | Bloque D: renombrar vs mover modelos. | Renombrar y corregir la fila de la Tabla 2 — menor cirugía. | [ ] |
| D-E1-6 | Al cerrar el pase: re-extraer el §15 a `entregable/` y fechar en `00-el-informe-hoy.md` (regla D-C); versionar el `.docx` como los demás (`…Seccion_15_Estado_del_Arte_v1.x.docx`). | Hacerlo al cerrar, no antes. | [ ] |

---

## 6. Orden sugerido

1. **Erratas duras** (sin decisión): E1-12 · Ahmad 2005 · doble punto · FairMOT · referencia
   colgada §15.3.1.2 · Tabla 8 push/pull · split del 63,0 · AJ-1.04/1.05.
2. **Alineación**: E1-01 Swin-B · E1-02 YOLOE-26 · E1-03 Tabla 4 · E1-05 Bloque D ·
   E1-07 cierre de §15.3.2.1 · E1-11 SDK + MQTT.
3. **Poda** (con D-E1-1/D-E1-3): PODA-01/02 (E1-06) · PODA-03 con E1-08 · PODA-04 con E1-10 ·
   E1-09.
4. **§16 y Anexo A** como Etapa 1 (D-E1-2): AJ-1.16 · PODA-05…11 · D-E1-4 · reparar los
   punteros desde §15.
5. **Cierre**: D-E1-6.
