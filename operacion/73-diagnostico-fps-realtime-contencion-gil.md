# 73 — Diagnóstico del techo de fps en realtime: la contención, no el modelo (2026-07-27)

**Alcance**: ejecución del spike de la palanca 1 de `71 §7.3` (cachear el embedding de
texto de GDINO) siguiendo su protocolo (a) perfilar → (b) implementar → (c) equivalencia
numérica → (d) re-validar contra el bench. El protocolo se detuvo —como él mismo
prescribe— en el paso (a): **la rama de texto no es el cuello**. La medición que lo
descartó destapó la causa real del techo de fps, que este documento identifica y acota.

> **⚠️ Leer §8 antes que nada: la opción 0 se ejecutó con cámara real y quedó REFUTADA**
> (apagar consola y bus no recupera fps), y apareció **F-RT4**, una biestabilidad de 2,6×
> sin variable identificada que es hoy el factor más grande en pie. §8.4 lista los errores
> de método cometidos y corregidos en esa sesión.
>
> **Estado: diagnóstico CERRADO, decisión de implementación ABIERTA.** Todo lo que sigue
> está medido en la máquina de referencia (RTX 4060 Laptop, misma que el rodaje). Nada
> commiteado, ningún código de producción modificado: el spike fue puramente de medición.
> El doc 71 §7.3 queda **corregido** en sus tres primeras palancas — ver §5.

**Hardware y franja**: RTX 4060 Laptop, clocks 2475–2490 MHz (máx 3105), GPU 57–71 °C
a lo largo de las corridas. Cada barrido declara su temperatura de inicio y fin, y las
configuraciones se recorren en **round-robin por rondas** para que la deriva térmica
afecte a todas por igual en vez de castigar a la última.

---

## 0. En llano: qué creíamos y qué resultó ser

Esta sección no tiene números nuevos: es la misma historia de las §1–§6 contada para
leerse de corrido. Sirve para el informe y para explicárselo a alguien que no vive adentro
del código.

### 0.1 La pregunta

Durante el rodaje, GDINO procesaba **1,2 a 2,6 cuadros por segundo** de los ~13 que
entrega la cámara: más del 90% de los frames se descartaban. Cada cuadro tardaba entre 430
y 560 ms en pasar por el detector. La pregunta era simple: **¿por qué tan lento, y qué se
puede hacer?**

### 0.2 Lo que creíamos (las cuatro sospechas del doc 71)

1. **"El modelo es pesado y la GPU de la notebook no da para más."** El fps bajo era un
   límite de hardware, y punto.
2. **"Hay un desperdicio evidente: el modelo relee el texto en cada cuadro."** GDINO
   detecta a partir de una frase (`"person. helmet. vest."`). Esa frase no cambia en toda
   la corrida, pero el programa la vuelve a procesar en cada cuadro. Parecía plata tirada:
   se estimaba que era el 30–40% del trabajo, y que cachearla llevaría de ~2 a ~3 fps.
3. **"Bajando la resolución de 560 a 480 píxeles se gana otro 25–30%."** Por analogía con
   el paso anterior de 800 a 560, que sí había dado −24%.
4. **"Se fue degradando durante el día por el calor."** La misma configuración rindió 2,4×
   peor a las 20 h que a las 13 h, y la GPU pasó de 41 a 61 °C en reposo.

Había una quinta creencia, más de fondo: al ver que la GPU marcaba solo 6–41% de uso, se
concluyó que ese perfil entrecortado era **la forma normal de trabajar de este tipo de
modelo**, no que estuviera ociosa.

### 0.3 Lo que resultó ser

**Ninguna de las cuatro se sostuvo.**

Lo primero que apareció al medir fue una contradicción: el modelo, corriendo solo en
**esta misma notebook**, procesa un cuadro en ~130 ms (y el camino completo en ~187 ms).
Eso daría más de 5 fps. Pero en el rodaje el mismo modelo, en la misma máquina, tardaba
430–560 ms. **Hay un factor 2–3× que no es del modelo ni de la GPU.** Los relojes de la
GPU explican como mucho un 10% de esa diferencia.

Y la explicación del calor tampoco cerraba: la corrida de las **17:50 tardó 201 ms** y la
de las **17:58 tardó 445 ms**. Ocho minutos de diferencia, misma cámara, mismo prompt. El
calor no sube y baja en ocho minutos.

Lo que sí separaba las corridas rápidas de las lentas era **de dónde venían las imágenes**:
las que leían de un archivo de video tardaban ~306 ms; las que leían de la cámara en vivo,
~426 ms. Y estaban intercaladas en el tiempo (19:52 archivo → 19:54 cámara → 19:57
archivo), así que no era el momento del día.

**La causa es cómo está armado el programa, no el modelo.**

El media-plane hace todo dentro de un mismo proceso de Python: leer la cámara, preparar la
imagen, correr la detección, escribir los archivos de resultados, publicar al bus, y además
atender la consola web. Python tiene un candado global —el **GIL**— que permite que **un
solo hilo ejecute código Python a la vez**. Todos esos trabajos se turnan para usarlo.

El problema es que **mandar trabajo a la GPU no es una orden sola: son miles de órdenes
chiquitas por cuadro**, y cada una necesita el candado para salir. Si el candado está
ocupado por el hilo que lee la cámara, la GPU se queda **esperando de brazos cruzados**
hasta que llegue la próxima orden.

> **La analogía**: la GPU es un cocinero rapidísimo, pero hay un solo mozo que le lleva los
> pedidos, y ese mozo también atiende las mesas, cobra y contesta el teléfono. El cocinero
> no cocina lento — **está parado esperando que le lleguen los pedidos**. Comprar una
> cocina mejor no cambia nada. Simplificar la receta (cachear el texto, bajar la
> resolución) tampoco: el cuello es el mozo.

Eso explica de una sola vez todo lo que no cerraba:

- **El "6–41% de uso de GPU" era exactamente lo que parecía: ociosidad.** No era la firma
  normal del modelo. Era el cocinero esperando.
- **Cámara vs archivo**: leer de la cámara en vivo es un trabajo mucho más pesado (imágenes
  de 1080p a 13 por segundo, de las que se tiran 9 de cada 10) que leer de un archivo de
  540p. Más trabajo compitiendo por el candado ⇒ más lento el detector.

**La prueba que lo confirma** es la más simple posible: puse a correr, al lado de la
detección, un hilo que **solo suma números enteros**. No toca la GPU, no toca la cámara, no
lee ni escribe nada. La latencia de detección pasó de **185 a 575 ms** — se triplicó. Un
bucle que suma números "hace más lenta a la GPU", lo cual es imposible… salvo que la GPU no
fuera el cuello.

Y el número cierra con el campo: la penalización que medí al agregar el trabajo de la
cámara fue **1,38×**; la diferencia real entre las corridas de cámara y las de archivo
durante el rodaje fue **1,39×** (426/306). Es el mismo fenómeno.

### 0.4 Qué pasó con las palancas que íbamos a construir

Ya que estaba, las medí igual, y ninguna vale la pena:

- **Cachear el texto**: no es el 30–40%, es el **8,2%**. Aunque se implementara perfecto,
  el techo es **1,09×** (de 2,0 a 2,2 fps). Además se creía que crecería al agregar clases
  al vocabulario, y **no crece**: multipliqué los tokens por seis y el costo quedó igual.
- **Bajar a 480 píxeles**: no da −25%, da **−5,8%**. El paso anterior (800→560) sí se
  reproduce (−27%), pero la extrapolación no valía, porque una parte del modelo tiene un
  costo fijo que no depende de la resolución.

En criollo: **las dos mejoras que teníamos planeadas suman menos del 15% juntas, mientras
que la causa que no habíamos visto vale un factor 2 o 3.**

### 0.5 Qué significa esto para la tesis

**No rompe nada de lo hecho, y mejora la explicación.**

- El camino **offline (DBE)** —con el que se van a medir los videos del rodaje— es
  **inmune**: procesa a la velocidad que haga falta y mide sobre los tiempos del video, no
  sobre el reloj de pared.
- Las **alertas live ya medidas siguen valiendo**: confirman por tiempo transcurrido, no
  por cantidad de cuadros vistos.
- Lo que cambia es **qué decimos sobre el fps bajo**. Antes se reportaba como *"la notebook
  no da para más"*. Ahora se puede afirmar, con medición, *"correr todo en un solo proceso
  de Python no da para más, y la GPU estaba ociosa la mayor parte del tiempo"*. Es un
  resultado de ingeniería mucho más interesante, y es **honesto**: es una limitación de
  arquitectura identificada y cuantificada, no una excusa.

### 0.6 Lo que todavía no sabemos

Está medido que **el trabajo de la cámara** explica el salto de 306 a 426 ms. **No está
medido** cuánto aportan los demás inquilinos del proceso (el que escribe los archivos y
comprime las previews, el que publica al bus, y el servidor web que alimenta la consola),
que juntos explicarían la brecha restante entre los 187 ms del banco aislado y los 306 ms
de las corridas de archivo. Es la misma causa, pero **repartirla entre culpables exige una
corrida instrumentada** — y hasta que se haga, se dice así, no se estima.

---

## 1. Palanca 1 (cacheo del embedding de texto): DESCARTADA con números

`grounding_dino_adapter.forward()` recalcula el encoder BERT sobre `"person. helmet.
vest."` en cada frame aunque el caption no cambie en toda la corrida. El doc 71 apostaba
a que esa rama fuera el 30–40% del forward, lo que llevaría GDINO de ~2 a ~3 fps.

Perfilado con hooks `forward_pre`/`forward` que encolan `torch.cuda.Event` en el stream
(sin `synchronize()` intermedio, que distorsionaría el pipeline asíncrono), 40 repeticiones,
`image_size: 560`, fp16, caption del prompt set congelado:

| submódulo | mediana | % del forward | params |
|---|---:|---:|---:|
| **text_backbone (BERT)** | **10,33 ms** | **8,1%** | 108,89 M |
| **text_projection** | **0,11 ms** | **0,1%** | 0,20 M |
| vision_backbone | 21,49 ms | 16,9% | 27,52 M |
| encoder (fusión cross-modal) | 58,19 ms | 45,6% | 21,91 M |
| decoder | 26,43 ms | 20,7% | 11,19 M |
| **FORWARD TOTAL** | **127,47 ms** | 100% | |

**La rama de texto es 8,2% del forward. Techo teórico del cacheo: 1,089×.** BERT es el
módulo más grande en parámetros y el más barato en tiempo: con un caption de 8 tokens
está limitado por latencia de lanzamiento de kernels, no por cómputo.

El doc 71 agregaba un argumento de futuro: "su valor crece con el nº de clases del
prompt". **Medido, es falso en el rango útil**:

| prompt | tokens | forward p50 | rama de texto | % | techo del cacheo |
|---|---:|---:|---:|---:|---:|
| 3 clases (el del rodaje) | 8 | 132,39 ms | 11,85 ms | 9,0% | 1,098× |
| 8 clases | 18 | 137,00 ms | 12,68 ms | 9,3% | 1,102× |
| 20 clases | 48 | 134,08 ms | 10,38 ms | 7,7% | 1,084× |

Seis veces más tokens, el mismo costo. **D-73.1: se descarta el cacheo del embedding de
texto.** Un cambio invasivo sobre internals de HF, que obliga a re-validar mAP contra el
bench, a cambio de ≤9% y sin crecimiento futuro, no paga. El protocolo del doc 71 §7.3
previó exactamente este desenlace ("si es menos, se documenta y se descarta con números").

## 2. El costo NO está fuera del modelo

El timer del pipeline (`runtime/pipeline.py:217-236`) envuelve **todo**
`adapter.forward()`, no solo `model(**inputs)`. Atribución del camino completo con 40
frames reales de la corrida `0eb1fd` del rodaje (no sintéticos: el costo del post-proceso
depende del nº de detecciones):

| etapa | p50 | p95 | % |
|---|---:|---:|---:|
| 1. tokenize (CPU, por frame) | 0,48 ms | 0,73 ms | 0,3% |
| 2. to_device (H2D) | 0,35 ms | 0,77 ms | 0,2% |
| 3. preprocess (letterbox) | 4,21 ms | 6,16 ms | 2,2% |
| **4. model forward (GPU)** | **176,35 ms** | 241,35 ms | **94,1%** |
| 5. post_process (D2H) | 2,08 ms | 3,94 ms | 1,1% |
| 6. bind + NMS (CPU) | 0,13 ms | 0,27 ms | 0,1% |
| **TOTAL `adapter.forward()`** | **187,47 ms** | 254,11 ms | 100% |

Confirma el diagnóstico base del doc 71 ("el costo es 100% inferencia"): todo lo que no
es el modelo suma ~7 ms. La tokenización por frame, que a primera vista es el mismo
desperdicio que el encoder de texto, cuesta 0,48 ms — irrelevante.

## 3. Palanca 3 (`gdino-tiny-480`): mucho más floja de lo estimado

| image_size | forward p50 | vs 560 |
|---|---:|---:|
| 480 | 124,70 ms | **−5,8%** |
| 560 | 132,39 ms | — |
| 800 | 182,39 ms | +37,8% |

El doc 71 estimaba −25–30% para 560→480 extrapolando el −24% que dio 800→560. La
extrapolación no vale: el 800→560 se reproduce (−27,4% medido acá) pero el 560→480 rinde
**−5,8%**. El costo no escala con los píxeles porque el decoder tiene costo fijo (sus
queries no dependen de la resolución) y ya pesa 20,7% del forward.

**D-73.2: `gdino-tiny-480` no se construye.** −5,8% no justifica una re-validación de mAP
contra `bench_obra`.

## 4. EL hallazgo (F-RT3): el techo de fps es contención de GIL, no la GPU

### 4.1 La anomalía que lo destapó

El forward mide 127 ms y el camino completo del adapter 187 ms **en esta misma máquina**.
El rodaje midió `inference_ms` p50 de 426–560 ms. Un factor 2–3× sin explicar; los clocks
(2250 durante el rodaje vs 2490 ahora) dan como mucho 10%.

Revisando las 16 corridas GDINO del 2026-07-25 por `metrics.jsonl`, aparecen dos cosas
que el doc 71 no había cruzado:

- **La hipótesis térmica no se sostiene.** El doc 71 §4.2 atribuye el 2,4× a thermal soak.
  Pero la corrida de las **17:50 rindió 201 ms** y la de las **17:58 rindió 445 ms** —
  ocho minutos de diferencia, misma fuente, mismo prompt set, 2,2×. Y la de las 13:33
  (231 ms) es más lenta que la de las 17:50 (201 ms), al revés de lo que predice el soak.
- **La fuente separa las poblaciones, intercaladas en el tiempo**: `video_file` p50 306 ms
  vs `oak_d` live p50 426 ms. A las **19:52 video_file 299 ms → 19:54 oak_d 469 ms → 19:57
  video_file 309 ms**: mismo estado térmico, ida y vuelta.

`latency_normalize_ms` es constante (8–12 ms) en todas las corridas, así que el exceso no
está en el preprocesamiento. Está *dentro* del timer de inferencia.

### 4.2 Hipótesis y test

> **Hipótesis**: el `inference_ms` de las corridas live no es costo de GPU. El hilo
> productor normaliza frames al ritmo de cámara (OAK-D ~13 fps, 1080p) y descarta el 92%;
> el hilo consumidor necesita el GIL para lanzar **cada** kernel CUDA. Starvado, la GPU
> queda ociosa entre kernels y el reloj de pared del forward se infla sin que la GPU esté
> más cargada.

Test de una sola variable: el mismo bucle de inferencia, con y sin un hilo de fondo que
hace el trabajo del productor. Condiciones en round-robin, 14 rondas.

| condición | p50 | p95 | vs base |
|---|---:|---:|---:|
| A. consumidor solo | 184,9 ms | 228,9 ms | 1,00× |
| B. + productor 1080p a 13 fps | 255,6 ms | 333,1 ms | **1,38×** |
| C. + productor 540p a 13 fps | 203,4 ms | 375,8 ms | 1,10× |
| D. + hilo Python puro (duty cycle) | 575,2 ms | 839,2 ms | **3,11×** |

**Confirmada.** La condición D no toca la GPU ni memoria pesada —es un `for` sumando
enteros— y **triplica la latencia de inferencia medida**, aterrizando justo en el rango de
campo. El orden B > C (1080p > 540p) reproduce el orden observado `oak_d` > `video_file`.

Corroboración cuantitativa: la penalización que impone el productor en mismo proceso
(**1,38×**) coincide con la razón de campo entre las dos poblaciones (426/306 = **1,39×**).

Esto reinterpreta el perfil "bursty, SM 6–41%" que el doc 71 §4.1 leyó como *"la firma de
un transformer a batch=1, no ociosidad"*: **es ociosidad** — kernels que llegan tarde
porque el hilo que los lanza no tiene el GIL. El mecanismo es el *convoy effect* de
CPython: el consumidor suelta el GIL en cada llamada C corta (un lanzamiento CUDA) y al
re-adquirirlo va al fondo de la cola detrás del hilo CPU-bound, pagando hasta un intervalo
de conmutación por cada round-trip, miles de veces por forward.

### 4.3 Qué NO lo arregla: `sys.setswitchinterval()`

Si el costo es proporcional al intervalo de conmutación del GIL (default 5 ms), bajarlo
debería recortarlo. Barrido intervalo × carga:

| switch interval | productor 1080p | hilo Python puro (continuo) |
|---|---:|---:|
| 5,00 ms (default) | **284,7 ms** | 34.644 ms |
| 1,00 ms | 727,7 ms | 7.451 ms |
| 0,20 ms | 731,6 ms | 2.142 ms |
| 0,05 ms | 426,8 ms | 1.240 ms |

En el caso patológico (hilo girando al 100%, sin duty cycle) la mejora es de 28× y
confirma el mecanismo del convoy effect —el costo escala con el intervalo—. Pero **en el
caso realista el signo se invierte**: bajarlo empeora al productor 1080p de 285 a 728 ms,
porque con una carga duty-cycled la conmutación más frecuente es puro overhead.

**D-73.3: no se toca `sys.setswitchinterval()`.** Es un cambio global de una línea cuyo
signo depende de la carga: mejora el peor caso y degrada el caso real.

> Nota de método: la columna "hilo Python puro" de esta tabla usa un hilo **continuo**
> (peor caso absoluto), mientras que la condición D de §4.2 usaba duty cycle a 13 fps. No
> son comparables entre sí; cada tabla es internamente consistente.

### 4.4 Qué sí lo arregla: sacar la inferencia del proceso compartido

Mismo test, con la inferencia en un **proceso propio** (GIL propio) y el productor en el
padre, bloques alternados con y sin carga:

| condición | p50 | p95 |
|---|---:|---:|
| inferencia en proceso propio, padre ocioso | 314,3 ms | 812,0 ms |
| inferencia en proceso propio, padre con productor 1080p | 323,0 ms | 787,0 ms |
| **penalización por contención** | **1,03×** | |

**La contención desaparece** (1,03× contra 1,38× en mismo proceso).

> Los absolutos de esta tabla (314 ms) **no** son comparables con los 185 ms de §4.2: acá
> el hijo infiere a demanda con huecos de ida y vuelta entre padre e hijo, y la GPU baja
> de clock entre inferencias (se la observó cayendo a 210 MHz en reposo). Lo válido es la
> **razón dentro de cada harness**, que es lo que el diseño alterna y controla.

### 4.5 Alcance del hallazgo: qué explica y qué no

Lo medido explica la brecha `oak_d` vs `video_file` (1,38× medido ≈ 1,39× de campo). **No
explica** por sí solo la brecha entre el banco aislado (185 ms) y las corridas
`video_file` de campo (306 ms). El resto de la explicación es el mismo mecanismo con más
contendientes, pero **no está medido con esta rigurosidad**: durante el rodaje el proceso
del media-plane también corría el writer de artefactos (JSONL + encode JPEG de previews),
el publicador del bus (msgpack), y el servicio FastAPI/uvicorn atendiendo la consola y el
streaming WS de previews — todo Python, todo compitiendo por el mismo GIL, más el
control-plane y el browser en la misma máquina. Cuantificar la contribución de cada uno
requiere una corrida instrumentada; queda como trabajo abierto, no como conclusión.

## 5. Corrección al doc 71 §7.3

La lista de palancas "en orden de retorno" queda así después de medirlas:

| # | palanca (doc 71) | estimación | medido |
|---|---|---|---|
| 1 | cachear embedding de texto | fps 2 → 3 | **8,2% del forward; techo 1,09×** → descartada (D-73.1) |
| 1b | "crece con el nº de clases" | sí | **no**: 8 → 48 tokens, mismo costo |
| 2 | controlar la variable térmica | hipótesis principal del 2,4× | **contradicha por los propios datos del rodaje** (§4.1); sigue siendo buena higiene experimental, no es la causa |
| 3 | `gdino-tiny-480` | −25–30% | **−5,8%** → descartada (D-73.2) |
| 4 | `torch.compile` / TensorRT | esfuerzo alto | sin medir; **ataca el 94% que sí es GPU**, sigue siendo el techo real del modelo |
| 5 | descartados con evidencia | — | sin cambios |
| **nuevo** | **eliminar la contención de GIL** | — | **1,38× medido en el caso productor; el resto de la brecha de campo es del mismo mecanismo, sin cuantificar** |

La meta honesta del doc 71 ("con 1+2+3, techo plausible ~4–6 fps") se apoyaba en tres
palancas que suman ≤15% real. El camino a más fps es la contención, y después el modelo.

## 6. Decisión abierta: qué hacer con F-RT3

El fix de raíz es sacar la inferencia a un proceso propio. **Eso ya existe diseñado y
dockerizado en el repo: la topología two-node** (`runtime/two_node.py`, Nodo A ingesta /
Nodo B GPU, `infra/twonode/`, Fase 2c). Este hallazgo le da una **segunda justificación,
independiente de la original**: no es solo para escalar a una GPU dedicada en otra máquina
—elimina la contención de GIL incluso en un solo host.

Cuatro opciones, para decidir con el usuario:

0. **[EJECUTADA Y REFUTADA — ver §8]** Higiene operativa, sin tocar código: si el cuello
   es la competencia por el GIL dentro del proceso, entonces **descargar el proceso durante
   las corridas oficiales debería recuperar fps sin cambiar una línea**: cerrar la consola
   y el browser de la máquina de inferencia (o servirlos desde otra), apagar previews y
   streaming WS en las corridas evaluativas, y no correr el control-plane en el mismo host.
   Es una **predicción falsable** del diagnóstico: si no mejora, F-RT3 explica menos de lo
   que este documento afirma y hay que volver a §4.5. Conviene medirlo **antes** que
   cualquier opción con código, porque además acota cuánto de la brecha no medida de §4.5
   es atribuible a estos inquilinos.
1. **No implementar nada** y citar el diagnóstico. Consistente con el doc 71 §7.2: el
   camino live ya está medido y es citable para el cierre, y el fps bajo se reporta como
   caracterización de hardware. F-RT3 mejora esa caracterización: convierte "la notebook
   no da más" en "la arquitectura de un solo proceso Python no da más", que es un hallazgo
   de ingeniería reportable y bastante más interesante.
2. **Medir el two-node en un solo host** (ambos nodos en la misma máquina, procesos
   separados) contra una corrida single-host equivalente. Es medición, no ingeniería
   nueva: el código existe. Cuantificaría el premio de punta a punta y cerraría §4.5.
3. **Implementar el split de proceso en single-host** (mover el consumidor de inferencia a
   un proceso propio dentro del despliegue actual). Es la ganancia máxima sin desplegar dos
   máquinas, y es cambio de arquitectura del plano.

**Aclaración sobre `g2a_ms`** (verificada en el código, no asumida): la métrica se marca
`not_interpretable` en `run_artifact_writer.py:199` por una condición sintáctica —
`config.topology.mode == "two_node"`— **sin mirar si los dos nodos están en la misma
máquina**. En Linux `time.monotonic()` tiene origen común para todo el sistema, así que
entre dos **procesos del mismo host** la resta sí significa algo: un split en single-host
(opción 3) **no rompe conceptualmente el G2A**, aunque hoy el código lo invalidaría por esa
condición. Y al revés, es una trampa para la opción 2: medir two-node en un solo host
devolverá `not_interpretable`, así que la latencia hay que leerla de `latency_inference_ms`
del nodo B (local a ese proceso y válida), no del bloque `g2a`.

**Ninguna de las tres bloquea el cierre de la tesis**: el camino DBE (offline) es inmune a
todo esto, porque procesa a la velocidad que haga falta y mide sobre timestamps de media.

## 8. Ejecución de la opción 0 (2026-07-27, madrugada): REFUTADA

Se ejecutó la opción 0 con la cámara real, el servicio real y el modelo campeón ya cargado.
No es una simulación: 16 corridas OAK-D, prompt set congelado, `gdino-tiny-560`.

### 8.1 Ablación de inquilinos: plano

Cinco condiciones incrementales, 3 pasadas alternadas (ida / vuelta / ida), 35 s de captura
cada una. `latency_inference_ms` p50:

| | A: media solo | B: +previews | C: +bus | D: +BFF | E: +consola (WS) |
|---|---:|---:|---:|---:|---:|
| Pasada 1 | 549 | 543 | 546 | 550 | 530 |
| Pasada 2 | 558 | 524 | 557 | 531 | 560 |
| Pasada 3 | 282 | 263 | 232 | 245 | **210** |

**Entre condiciones no hay señal.** Previews, publicador del bus, BFF y consola abierta no
cuestan nada medible; en la pasada 1 la condición del rodaje (E, todo encendido) fue incluso
la más rápida de las cinco.

**D-73.4: la opción 0 queda refutada. Apagar la consola y el bus no recupera fps.** La
predicción escrita en §4.5 —que esos inquilinos explicaban la brecha entre el banco aislado
y las corridas de campo— era incorrecta.

Por qué falló la predicción, en retrospectiva: los inquilinos ablacionados son todos de
**baja actividad** (el BFF consulta cada tanto, el WS empuja unos pocos eventos por
segundo). El contendiente de alta actividad —el hilo de ingesta que lee la cámara y
normaliza a ritmo de sensor— **está presente en las cinco condiciones, incluida la mínima**:
el experimento nunca pudo apagarlo. El nulo no refuta F-RT3; refuta que *estos* inquilinos
fueran los culpables.

### 8.2 Lo que sí quedó medido

- **La fuente entregó ~20 fps constantes en las 16 corridas**, con 85–94% de descartes
  siempre. La cámara nunca estuvo starvada: el consumidor fue el cuello en todas.
- **La GPU está ociosa, no saturada.** Corrida instrumentada con muestreo a 100 ms:
  `clocks_throttle_reasons` = `GPU_IDLE` en **215 de 227 muestras**, utilización p50 37%,
  potencia p50 30,7 W. Esto **confirma la relectura de §4.2**: el perfil "SM 6–41%" del
  doc 71 es ociosidad, y ahora está medido con el registro de throttling del propio driver,
  no inferido.
- **El costo de alimentar la GPU desde el servicio**: banco aislado 148 ms vs servicio
  232 ms con la misma resolución de entrada y el mismo modelo = **1,57×**. Ese es el precio
  de la arquitectura de un proceso, medido de punta a punta.
- **Duty cycle: real pero menor.** Con huecos artificiales entre inferencias los clocks
  caen de verdad (2475 → 1702 MHz con 800 ms de hueco) pero la latencia sube solo **1,09×**.
  Descartado como explicación del factor grande.

### 8.3 El hallazgo abierto (F-RT4): biestabilidad de 2,6× sin variable identificada

Entre la pasada 2 y la 3 el consumidor pasó de ~550 ms a ~210 ms **con todas las variables
medidas constantes**: misma configuración, misma tasa de fuente (~20 fps), mismos clocks,
misma temperatura, mismos inquilinos. La transición ocurrió **dentro de una corrida** (la
11: primer tercio 452 ms → último tercio 248 ms) y siguió mejorando durante cinco corridas
seguidas (282 → 263 → 232 → 245 → 210, con descartes cayendo de 91% a 85%).

Es el mismo fenómeno que el doc 71 §4.2 atribuyó al calor y que §4.1 de este documento ya
había mostrado incompatible con esa explicación (17:50 → 201 ms, 17:58 → 445 ms).
**Es el factor más grande que queda en pie —2,6×, más que todas las palancas juntas— y no
está explicado.** Descartados con medición: inquilinos del proceso, tasa de entrada,
resolución de la fuente, duty cycle, clocks, temperatura y configuración.

No se pudo forzar el régimen lento para instrumentarlo: al momento de escribir esto la
máquina está en el régimen rápido. **Próximo paso natural**: un muestreo con `py-spy` sobre
el proceso del servicio (no instalado hoy) durante una corrida lenta, que mostraría en qué
llamada se va el tiempo del hilo consumidor sin tener que adivinar.

> **Actualización (segunda sesión, §9)**: el intento con py-spy resultó una trampa de
> medición en WSL (efecto observador 2×), y tras reiniciar WSL el régimen lento no volvió
> a aparecer en 10 corridas — F-RT4 queda reencuadrado como estado global del host, ver §9.3.

### 8.4 Errores de método cometidos en esta sesión (y corregidos)

Se dejan anotados porque cualquiera que repita estas mediciones puede caer en los mismos:

1. **Alimentar `prepare_model_input` con el frame crudo de 1080p.** El pipeline real le pasa
   el payload **ya redimensionado por el productor** (`normalize_spatial` deja
   `target_size`). El error infló la línea base de 148 a 509 ms —2,7×— e **invalidó la
   primera versión del test de duty cycle**, cuya conclusión ("no hay efecto") era un
   artefacto. Rehecho con el payload correcto, el efecto existe y es de 1,09×.
2. **Correlacionar el intervalo entre unidades procesadas con la latencia de inferencia.**
   Da r = 1,000 y no significa nada: el espaciado de las unidades que sobreviven al rate
   gate **es, por construcción,** el tiempo de servicio del consumidor. Se midió una
   consecuencia y se la leyó como causa.
3. **Lanzar el `control.yaml` del rodaje directo contra el control-plane**: da 422 porque
   le falta `input.type: bus` — se lo inyecta el runner de la consola (bug #1 del doc 71
   §3). Las condiciones C/D/E corrieron sin suscriptor; como fue por igual en las tres, la
   comparación incremental se sostiene y de hecho quedó mejor separada (aísla el publicador
   del bus, que es in-proceso, del control-plane, que es otro proceso).

## 9. Segunda sesión (2026-07-27, ~05:00, tras reinicio de WSL): F-RT4 no reaparece y py-spy resulta trampa

La sesión anterior murió con WSL; al retomar, la máquina quedó en un estado distinto al de
la madrugada: **arranque fresco de WSL, sin control-plane, sin BFF, sin navegador** — solo
el media-plane recién levantado con `gdino-tiny-560` y la OAK-D por link-local.

### 9.1 La trampa: py-spy en WSL infla la latencia 2× y estira su propia ventana

Se corrió el cazador planificado en §8.3: 4 corridas de 60 s con py-spy disparado a mitad
de corrida (`record --gil --rate 200 -d 25`). Las 4 corridas mostraron un patrón nítido:
primeros ~10 s rápidos (~200–300 ms) y el resto lento (~340–460 ms). Parecía la
biestabilidad F-RT4 capturada en vivo.

**Era efecto observador.** Dos datos lo prueban:

1. **mtimes de los artefactos**: el `dump` sale a t=20 s del POST y el SVG se termina de
   escribir 86–91 s después — py-spy apunta a `rate × duration` = 5000 muestras, y en WSL
   el muestreo por ptrace es tan lento que tarda ~90 s en juntarlas. Su ventana real cubrió
   desde t≈10 s de métricas hasta el final de cada corrida: exactamente el "régimen lento".
2. **Cada muestra pausa el proceso**: la inflación medida es ~2× (250 → 420–450 ms),
   consistente entre las 4 corridas. En las ventanas sin py-spy de esas mismas corridas la
   latencia fue siempre 190–290 ms.

Moraleja para quien repita: en WSL, py-spy `record` **no sirve para medir latencia mientras
perfila** (sí sirve el flamegraph resultante como estructura relativa), y `-d` no es
duración de reloj sino objetivo de muestras.

### 9.2 Lo que el flamegraph sí mostró (estructura, no magnitudes)

En las 4 corridas el hilo productor concentra 33–41% de las muestras, casi todo en
`normalize_spatial` → conversión PIL (`Image.tobytes` + `__array_interface__`, ~15% cada
una): trabajo de CPU puro con el GIL tomado, compitiendo con el consumidor. Es la firma
concreta, con nombres de función, de la contención F-RT3 medida en §4 (1,38×). Si algún
día se ataca en un solo proceso, el blanco es esa conversión PIL→numpy del productor.

### 9.3 F-RT4 no reaparece: 10 corridas limpias, todas rápidas

Con telemetría GPU a 2 Hz (potencia, clocks, utilización, temperatura, throttle) + CPU:

- **7 corridas limpias** (1 tras el cazador, 3 con el servicio ya usado, 3 con **servicio
  recién reiniciado = contexto CUDA fresco**): p50 200–236 ms **sostenido de punta a
  punta**, ~4,3–4,7 fps procesados, GPU a 31–44 W / 2000–2475 MHz, siempre con throttle
  por potencia (0x01) activo, temperatura 62–74 °C sin efecto.
- El quiebre a los ~10 s **no aparece nunca** sin py-spy. Contexto CUDA frío o caliente,
  GPU fría o caliente, proceso nuevo o viejo: da igual.

Quedan refutadas para F-RT4 dos hipótesis nuevas de esta sesión: warm-up del contexto
CUDA por corridas sucesivas y ventana de boost de ~10 s del gestor de potencia.

**Lo que queda en pie**: el régimen rápido (~210 ms, el mismo de la pasada 3 de §8.3) es
el estado natural de la máquina con el sistema descargado. El régimen lento de la
madrugada (~550 ms) y del rodaje (426 ms) ocurrió con WSL con horas de uptime y
control-plane + BFF + navegador corriendo; esta noche, con WSL recién reiniciado y sin
esos procesos, es inalcanzable — no se pudo forzar. F-RT4 pasa de "biestabilidad sin
variable" a **"régimen lento correlacionado con estado global del host (uptime de
WSL/Windows y carga acumulada), pendiente de aislar la variable concreta"**. La ablación
de §8.1 toggleaba inquilinos *por corrida* pero los procesos (control-plane, BFF) seguían
vivos en todas las condiciones: nunca se midió el estado "host limpio" hasta ahora, y da
2,6× de diferencia.

**Implicación operativa inmediata** (barata y accionable): antes de una sesión de medición
o rodaje, reiniciar WSL y levantar solo los servicios necesarios deja la plataforma en el
régimen rápido sostenido (~4,5 fps de procesamiento con `gdino-tiny-560` @ OAK-D 1080p).
Verificarlo con 60 s de corrida y `metrics.jsonl` (p50 < 300 ms) cuesta un minuto.
**Codificado como checklist operativa en `docs/operacion/74`** (2026-07-28).

Scripts de esta sesión (en el tmp del job, mover al repo si se sigue):
`serve_traceable.py` (lanza uvicorn con `PR_SET_PTRACER_ANY` para py-spy sin sudo),
`cazar_frt4.py` (cazador con py-spy), `telemetria_frt4*.py` (corridas con telemetría
GPU+CPU alineada por wallclock con `metrics.jsonl`).

## 10. Palanca nueva (F-RT5): el round-trip PIL del productor — MEDIDA Y CONFIRMADA (+18% fps)

Salió del flamegraph de §9.2 y **no estaba en ninguna lista de palancas** (ni doc 71 §7.3 ni
§5 de este doc). Es la única palanca nueva de todo el spike.

### 10.1 El hallazgo, verificado leyendo el código

`image_loader.load_image()` devolvía un `PIL.Image` y `normalize_spatial()` lo desenvolvía
en la línea siguiente con `np.asarray(...)`. Para fuentes vivas (OAK-D/RTSP) y para frames
de video, eso es un round-trip **ndarray → PIL → ndarray** completamente innecesario: dos
copias del frame de 1080p (6,2 MB cada una) en Python, **con el GIL tomado**, en el hilo
productor — el mismo que compite con el consumidor de inferencia (F-RT3).

Cuánto pesa realmente: los descartes de una corrida OAK-D son **todos `queue_full`**, nunca
`rate_gate` (verificado en `dropped_units.jsonl`), así que el productor normaliza **todos**
los frames de la cámara (~24/s), no sólo los ~2–4 que se procesan. A ~13 ms cada uno, eso
es **0,3–0,5 s de GIL por segundo de reloj gastados en frames que después se tiran.**

### 10.2 Implementado con TDD (rama `perf/producer-pil-roundtrip`)

`load_image_array()` devuelve el ndarray RGB directo; `load_image()` se conserva para
consumidores que quieran PIL; la rama de archivo de imagen sigue decodificando con PIL,
que es donde hace falta. 9 tests nuevos (`tests/test_image_loader_array.py`): equivalencia
con el camino PIL en las tres ramas de carga, guard de que `normalize_spatial` no construye
un `PIL.Image` para fuentes vivas ni para frames de video, y guard de regresión de píxeles.
**Suite completa: 650 passed / 5 skipped. `ruff` limpio.**

### 10.3 Lo medido, separado por confianza

**Costo del productor — concluyente:**

| medición | antes | después |
|---|---|---|
| micro-benchmark de `normalize_spatial`, 1080p, 2 pasadas | 15,4 / 20,2 ms | **1,07 / 1,42 ms** |
| `latency_normalize_ms` p50 del servicio real (7 corridas OAK-D) | ~13,5 ms | **~1,5 ms** |

Checksum del payload idéntico (67378166) entre ambos caminos: la salida es byte a byte la
misma, además de los tests.

**Efecto end-to-end — CONFIRMADO (23 bloques, 4 campañas, 11 pares):**

Diseño: bloques A/B alternados de 60 s con la OAK-D real, **levantando el servicio de cero
en cada bloque** (el código difiere por proceso), orden de arranque alternado entre campañas
para no sesgar. El análisis es **pareado sobre bloques adyacentes dentro de una misma
campaña** — nunca cruzando campañas, porque entre ellas hay horas y cambios de régimen
(F-RT4). Con el pareado, la deriva del host se cancela dentro de cada par.

| | pares a favor de B | mejora media | mediana | p (permutación, unilateral) |
|---|---|---|---|---|
| latencia de inferencia | **10 / 11** | 37,3 ms (**14,4%**) | 43,9 ms | **0,0195** |
| fps procesado | **10 / 11** | +0,63 fps | — | — |

Agregado por condición, **restringido al régimen rápido** (campañas 3 y 4, host estable,
n=8 por rama — la comparación más limpia):

| condición | inferencia p50 mediana | rango | fps medio |
|---|---|---|---|
| A (con PIL) | 222,3 ms | 194–236 | 3,75 |
| B (sin PIL) | **183,8 ms** | 162–212 | **4,42 (+18%)** |

El mejor bloque individual de toda la investigación fue una corrida B: **5,12 fps**.

El único par en contra fue **la primerísima corrida B de todas**, con el worktree recién
creado y caché de disco frío. No se lo excluye (sería el error de método de §8.4); con él
adentro el resultado igual es significativo.

**Por qué las primeras dos campañas no vieron el efecto**: con n=3/n=4 la dispersión de la
deriva F-RT4 (±150 ms) es mayor que el efecto (~37 ms). No es que no existiera: hacía falta
pareado y n. Queda como advertencia para futuras mediciones en esta máquina — **cualquier
palanca de menos del 20% necesita ~10 pares para separarse del ruido del host.**

**Chequeo mecánico**: se eliminan ~11 ms × ~24 frames/s ≈ **0,26 s de GIL por segundo de
reloj**; la ganancia observada en capacidad de procesamiento es ~0,11 s/s. Mismo orden de
magnitud, recuperación parcial — consistente con que el GIL era *una* restricción y no
*la* restricción.

**Qué dice esto de F-RT3**: lo confirma parcialmente y lo acota. La contención de GIL era
real y **sacarle trabajo al productor sí acelera al consumidor**, pero el premio es 14–18%,
no el 1,38× que sugería el test aislado de §4.2. Los frames normalizados por corrida se
mantienen constantes (~1370–1520) con y sin el cambio: el productor nunca fue el cuello de
*throughput*, sólo un competidor por el GIL.

**Contexto contra el doc 71 §7.3**: las tres palancas planificadas (cachear texto, 480 px,
térmica) sumaban <15% y quedaron descartadas con números. Esta palanca —que no estaba en
ninguna lista y salió de mirar un flamegraph— sola da **+18% de fps** y lleva la máquina de
3,75 a 4,42 fps, dentro del rango 4–6 fps que el doc 71 se había puesto como meta.

### 10.4 Estado y adopción

**La medición está cerrada y el código está commiteado y pusheado**: commit `3deb64c` en la
rama `perf/producer-pil-roundtrip` (a pedido del usuario, 2026-07-28). El merge a
`feature/inference-service` es decisión y ejecución del usuario — el manejo de git es suyo.

Notas para el merge:

- No requiere re-validar mAP: la salida es byte a byte idéntica (checksum + 9 tests de
  equivalencia). Beneficia por igual a OAK-D, RTSP y `video_file`.
- `load_image()` se conservó a propósito: no tiene consumidores de producción (el
  preanotador usa su propio camino PIL — verificado), pero es la implementación de
  referencia contra la que los tests de equivalencia comparan.
- Suite completa verificada sobre el commit: 650 passed / 5 skipped, ruff limpio.

- Worktree: `e-ovrt_media-plane/.claude/worktrees/pil-roundtrip`, rama
  `perf/producer-pil-roundtrip` (creada desde HEAD de `feature/inference-service`, **no**
  desde `main`, que está 59 commits atrás).
- Trampa de setup: los pesos están gitignoreados, el worktree no los tiene. Hay que
  enlazarlos (`find models -name '*.safetensors' -o -name '*.bin'` → symlinks) o el
  servicio arranca y se queda en 503 con `OSError` de checkpoint.
- El servicio del worktree se levanta con el venv del checkout principal y
  `PYTHONPATH=<worktree>/src` (el editable install es un `.pth` simple, así que PYTHONPATH
  gana).
- Script del A/B: `ab_pil_roundtrip.py` (bloques alternados, levanta el servicio de cero
  por bloque, mide sobre `metrics.jsonl`).

## 7. Reproducibilidad

Scripts del spike (no versionados, viven en el scratchpad de la sesión; se pueden mover al
repo si se decide seguir):

- `profile_gdino_text.py` — perfilado por submódulo con CUDA events (§1)
- `profile_adapter_path.py` — atribución de `adapter.forward()` con frames reales (§2)
- `sweep_gdino.py` — barrido caption × image_size en round-robin (§1, §3)
- `test_gil_contention.py` — test de hipótesis, 4 condiciones (§4.2)
- `test_switch_interval.py` — barrido intervalo × carga (§4.3)
- `test_process_isolation.py` — aislamiento por proceso, bloques alternados (§4.4)

Ninguna medición usó datos de campo como única fuente: todas se reprodujeron en la máquina
de referencia, y las corridas del rodaje se usaron solo para verificar que el mecanismo
medido explica lo observado.
