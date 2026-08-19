# E-OVRT-VDP - paquete de etapa 6

> Generado el 2026-08-19. Etapa 6: secciones 17.6, 18 y 19.

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

- **Etapa activa:** 6 - Etapa 6: secciones 17.6, 18 y 19.
- Este archivo contiene el texto vigente que se modifica y sus insumos de ajuste.
- No se trasladan resultados propios hacia secciones cronologicamente anteriores.
- Nombre propio de esta etapa (01-etapa-6-activa.md): regenerarla no pisa el paquete de ninguna otra etapa.

---

## Fuente: `docs/informe/entregable/96e-informe-v11-cierre-anexos-referencias.md`

> SHA-256 del bloque: `3d054514a734cf944d87341e6f10df53d8bb128bd08741ccc4ecebdede898b44`  
> Seleccion: secciones 17.6, 18, 19 y referencias vigentes.

### 17.6. Documentación técnica, repositorio y evidencias de cierre

[Agregado futuro correspondiente a la Etapa 6]


## 18. Cierre del Proyecto

[Agregado futuro]


## 19. Anexos


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


### 19.2. Anexo B - Infraestructura, nodos y parámetros experimentales

Tabla B. 1

Especificaciones técnicas del Central Processing Node (CPN)


| Componente | Especificación |
| --- | --- |
| Modelo | HP Victus 15 Gaming Laptop 15-FB2024LA (2024) |
| CPU | AMD Ryzen 5 8645HS — arquitectura Zen 4; 6 núcleos / 12 hilos; frecuencia base 4.3 GHz, turbo 5.0 GHz |
| GPU dedicada | NVIDIA GeForce RTX 4060 Laptop — chip AD107; 3072 núcleos CUDA; 96 Tensor Cores (4.ª gen.); 8 GB GDDR6; 128-bit; TGP estimado 75 W |
| Decodificación de video | NVIDIA NVDEC de 5.ª generación integrado en la RTX 4060; soporte por hardware para H.264, H.265/HEVC y AV1 |
| Memoria RAM | 32 GB DDR5-5600 (2 × 16 GB SO-DIMM, Dual Channel) |
| Almacenamiento | 1 TB M.2 PCIe NVMe SSD |
| Sistema operativo | Windows 11 Home Single Language |

Nota. Basado en HP Inc. para la identificación del modelo del equipo, y en Advanced Micro Devices, Inc. y NVIDIA Corporation para las especificaciones de CPU y GPU (Advanced Micro Devices, Inc., s. f.; HP Inc., s. f.; NVIDIA Corporation, s. f.-a, s. f.-b).

Tabla B. 2

Especificaciones técnicas del Edge Node candidato (Luxonis OAK-D Pro PoE)


| Componente | Especificación |
| --- | --- |
| Modelo | Luxonis OAK-D Pro PoE (Series 2) |
| Procesador de visión | RVC2 — 4 TOPS totales de procesamiento (1.4 TOPS para AI) |
| Sensor RGB | Sony IMX378, hasta 12 MP (4056 × 3040), rolling shutter, 78° DFOV / 66° HFOV / 54° VFOV, auto-focus, hasta 60 FPS |
| Sensores estéreo | 2 × OV9282, 1 MP (1280 × 800), global shutter, 89.5° DFOV / 80° HFOV / 55° VFOV, hasta 255 FPS |
| Codificación de video | H.264, H.265 y MJPEG por hardware — hasta 4K/30 FPS y 1080p/60 FPS |
| Percepción IR | IR dot projector para estéreo activo + IR illumination LED para operación en baja o nula iluminación |
| IMU | BNO085, 9 ejes, integrada |
| Conectividad | PoE 802.3af Class 3, 1000BASE-T (1 Gbps); conector M12 para alimentación/datos y M8 para IO auxiliar |
| Consumo máximo | Base + streaming 2.5–3 W, más 0.5 W de circuito PoE; consumo total hasta aproximadamente 7.5 W según carga y subsistemas activos |
| Framework de desarrollo | DepthAI |
| Rango de profundidad | Rango ideal 70 cm–12 m; MinZ ~20 cm en 400P + extended disparity; error absoluto < 2 % por debajo de 4 m, < 4 % entre 4 m y 7 m y < 6 % entre 7 m y 10 m |

Nota. Basado en la página oficial del producto y en la documentación de hardware de OAK-D Pro PoE (Luxonis, s. f.-a, s. f.-b). La cámara utiliza PoE para alimentación y conectividad Gigabit Ethernet, dispone de percepción estéreo activa, iluminación IR y capacidades de procesamiento embebido sobre RVC2. La definición del rol exacto del EN en la topología del Escenario B —captura exclusiva, preprocesamiento o captura con inferencia ligera— se determinará en la Et apa 3.

Tabla B. 3

Stack de software candidato del CPN


| Componente | Especificación | Justificación |
| --- | --- | --- |
| Sistema operativo | Windows 11 Home | Plataforma nativa del CPN; compatibilidad con drivers NVIDIA para arquitectura Ada Lovelace. |
| CUDA / cuDNN | CUDA 12.x — cuDNN 9.x (stack candidato, a confirmar) | Combinación compatible con GPUs NVIDIA Ada Lovelace y con los frameworks de inferencia previstos; las versiones exactas se fijarán durante el setup del entorno. |
| Framework de deep learning | PyTorch | Framework oficial de referencia para Grounding DINO y YOLOE; compatibilidad directa con checkpoints preentrenados y ajustados al dominio. |
| Runtime de optimización (primario) | TensorRT | Runtime candidato de optimización para GPU NVIDIA, pertinente para evaluar configuraciones de baja latencia en el CPN. |
| Runtime de optimización (alternativo) | ONNX Runtime (proveedor CUDA) | Alternativa portable para exportar modelos en formato ONNX y contrastar su desempeño frente a TensorRT. |
| Framework de pipeline (a evaluar) | NVIDIA DeepStream vía WSL2 | Framework candidato, basado en GStreamer y documentado por NVIDIA para ejecución sobre Windows 11 mediante WSL2 con GPUs GeForce/Quadro en modo WDDM; su adopción efectiva se evaluará en la instancia de análisis y diseño arquitectónico frente a otras alternativas del plano de medios. |
| Gestión de entorno | conda o venv (a definir) | Aislamiento de dependencias entre modelos con distintos requisitos de versión. |

Nota. La configuración propuesta debe interpretarse como stack candidato del CPN y no como decisión de implementación ya cerrada. La selección final de versiones, runtimes y framework de pipeline corresponde a la instancia de análisis y diseño arquitectónico, en tanto forma parte del diseño arquitectónico del sistema. La instalación efectiva, integración y verificación de funcionamiento del stack sobre el hardware del CPN corresponden a la implementación del prototipo experimental. La selección de Grounding DINO y YOLOE como modelos candidatos se encuentra alineada con el análisis de modelos OVD, que los ubica como alternativas representativas de distintos compromisos entre expresividad semántica y eficiencia computacional. Asimismo, la separación entre PyTorch nativo, TensorRT y ONNX Runtime resulta consistente con el flujo de transferencia previsto entre el TN y el CPN, donde los checkpoints ajustados se exportan al formato requerido por el runtime de inferencia finalmente adoptado. La mención de DeepStream vía WSL2, TensorRT y ONNX Runtime se apoya en la documentación oficial correspondiente (NVIDIA Corporation, 2026a, 2026b; ONNX Runtime, s. f.).

Tabla B. 4

Especificaciones técnicas del Training Node (TN)


| Componente | Especificación |
| --- | --- |
| Tipo de recurso | Cluster de cómputo institucional (Mendieta, CCAD-UNC) |
| Nodos disponibles | 19 nodos de cómputo con GPU |
| GPU por nodo | 2 × NVIDIA A30 — 24 GB HBM2 cada una; arquitectura Ampere; soporte TF32, FP16, BF16 e INT8 |
| CPU por nodo | 20 núcleos / 20 hilos — Intel Xeon E5-2680 v2 |
| Memoria RAM por nodo | 64 GB |
| Almacenamiento local | 400 GB SSD SATA por nodo |
| Interconexión | 40 Gbps Infiniband QDR |
| Asignación mínima | 1/2 nodo (10 cores, 1 GPU) |
| Rol en el proyecto | Fine-tuning de modelos OVD candidatos sobre datos del dominio de construcción civil |
| Disponibilidad | Acceso institucional asignado al proyecto |

Nota. Especificaciones verificadas para el clúster Mendieta en la tabla oficial de infraestructura de CCAD-UNC, y complementadas con la ficha técnica oficial de NVIDIA A30 para las características de la GPU (Centro de Computación de Alto Desempeño, 2026; NVIDIA Corporation, 2022). La asignación mínima validada explícitamente por la fuente institucional es 1/2 nodo (10 cores, 1 GPU). Los clústeres Mulatona, Eulogia, Serafín y Boogie no presentan GPUs en la tabla comparativa oficial del CCAD, por lo que no son considerados para utilizar en el proyecto.

Tabla B. 5

Stack de software candidato del TN


| Componente | Especificación | Justificación |
| --- | --- | --- |
| Sistema operativo | Linux (distribución del cluster) | Entorno estándar para entrenamiento de modelos sobre GPU en infraestructura HPC. |
| CUDA / cuDNN | CUDA 12.x — cuDNN 9.x (stack candidato, a confirmar) | Combinación compatible con la arquitectura Ampere de las NVIDIA A30 y con frameworks de entrenamiento basados en PyTorch. |
| Framework de entrenamiento | PyTorch + bibliotecas de fine-tuning de cada modelo | Grounding DINO y YOLOE publican sus implementaciones oficiales en PyTorch, lo que favorece compatibilidad con checkpoints y rutinas de ajuste fino. |
| Multi-GPU | DistributedDataParallel (DDP) o equivalente (si la asignación efectiva lo permite) | Las 2 A30 por nodo habilitan entrenamiento distribuido para reducir tiempos de convergencia |

Nota. La configuración consignada debe interpretarse como stack candidato del TN y no como entorno de entrenamiento ya validado. La definición del procedimiento de fine-tuning —incluyendo esquema de ajuste, congelamiento de capas, tasa de aprendizaje, número de épocas y uso o no de entrenamiento distribuido— corresponde a la instancia de análisis y diseño arquitectónico como parte del diseño experimental. La instalación efectiva, integración y verificación de funcionamiento del entorno sobre el clúster corresponden a la implementación del prototipo experimental. Asimismo, cualquier comparación entre variantes zero-shot y fine-tuned exige mantener una baseline explícita y una partición train/eval estrictamente disjunta. Fuentes: Liu et al. (2023); Wang et al. (2025); NVIDIA Corporation (2022); Meta AI (2019).

Tabla B. 6

Parámetros de referencia orientativos del pipeline


| Parámetro | Valor de referencia |
| --- | --- |
| Resolución de captura | 1280 × 720 px (HD). Resolución de referencia del sensor o fuente de video. El pipeline incluye una etapa de preprocesamiento que adapta los frames a la resolución de entrada requerida por el modelo seleccionado; para los modelos actualmente priorizados, ello puede implicar configuraciones del orden de 640 × 640 px en variantes tipo YOLOE y 800 × 1333 px en variantes tipo Grounding DINO. |
| Framerate de captura de referencia | 30 FPS (estimativo). Valor orientativo para la fuente de video; no equivale a los FPS efectivos del pipeline, que dependerán de la latencia de inferencia, del presupuesto G2A y de la configuración de ejecución. |
| Presupuesto de latencia G2A | 50 ms - 250 ms. Presupuesto de referencia definido en el framework de métricas; véase allí su formalización y descomposición operativa. |

Nota. Valores orientativos sujetos a validación experimental en la validación experimental. La distinción entre resolución de captura y resolución de entrada del modelo es relevante: el pipeline incluye una etapa de redimensionamiento que adapta los frames al formato esperado por cada modelo OVD candidato. Elaboración propia.

Tabla B. 7

Topología de red del Escenario B


| Aspecto | Descripción |
| --- | --- |
| Topología | LAN. |
| Protocolo de transmisión | RTSP/RTP sobre UDP como protocolo de referencia para cámaras IP y flujos de video sobre red local; la decisión definitiva de transporte y topología interna corresponde a la instancia de análisis y diseño arquitectónico. |
| Acceso a internet | No disponible durante las pruebas. |
| Restricciones de red | Sin restricciones externas previstas; la configuración efectiva de buffering, transporte y eventual intermediación se definirá en la etapa de diseño. |

Nota. En el marco del proyecto, RTSP/RTP se adopta como referencia por su amplia compatibilidad con cámaras IP y por su adecuación a entornos LAN de videovigilancia y streaming controlado. Esta elección no implica fijar de manera anticipada la topología interna definitiva del pipeline ni descartar otras alternativas de transporte que pudieran resultar pertinentes según la arquitectura que se defina en la instancia de análisis y diseño arquitectónico.


### 19.3. Anexo C - Prompts, datos, datasets, benchmarks y logística

Tabla C. 1

Catálogo de prompts candidatos por condición de riesgo


| Código | Eje de variación | Prompt candidato (inglés) | Estrategia |
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

Nota. Las estrategias “Indirecta” y “Descompuesta” utilizan el separador “;” como notación analítica para indicar consultas independientes al modelo OVD; su materialización concreta depende de la sintaxis admitida por cada detector. Las variaciones “Template” utilizan formulaciones tipo “a photo of a [CLASS]”, alineadas con prácticas habituales de uso de modelos visión-lenguaje preentrenados como CLIP. Para CR-05 y CR-06, al tratarse de condiciones de Nivel 3, no se formulan prompts integrados sino prompts de entidades componentes; la evaluación de la condición completa se realiza en el módulo de razonamiento contextual. En particular, los elementos auxiliares de CR-06 no reemplazan la definición externa del polígono de zona restringida, sino que pueden funcionar como referencias visuales complementarias para experimentos o análisis cualitativo. Fuente: Elaboración propia basada en los ejes de variación de la Sección 17.1.5.4.2 y en los hallazgos de Zhou et al. (2022), Du et al. (2022), Gu et al. (2021) y Radford et al. (2021).

Tabla C. 2 Variables de sensibilidad candidatas para el Environment-Based Evaluation


| Variable | Niveles o condiciones retenidas | Uso dentro del protocolo |
| --- | --- | --- |
| Iluminación | Controlada; mixta; natural cuando el entorno lo permita. | Define condición base y barridos univariados de sensibilidad. |
| Resolución de fuente | 1280 × 720 como base; 1920 × 1080 como variante de sensibilidad si la configuración lo permite. | Estima el costo-beneficio entre visibilidad, carga computacional y estabilidad del pipeline. |
| Distancia cámara-sujeto | Rangos a cerrar en instancia de análisis y diseño arquitectónico según campo visual y tamaño aparente; guía inicial: 5-10 m y 10-20 m. | Permite observar el efecto de escala de objeto sin fijar una geometría de cámara antes del diseño del EBE. |
| Oclusión | Baja y media; la oclusión severa no se adopta como obligación de aceptación. | Tensiona la robustez sin convertir la campaña en irreproducible. |
| Tracker | Deshabilitado y habilitado cuando aplique. | Permite medir el aporte del tracking a estabilidad, persistencia y reducción de falsas alarmas. |
| Matriz de prompts | Conjunto acotado de variantes por condición. | Permite seleccionar y congelar el prompt primario antes de las corridas comparativas finales. |
| Composición del vocabulario activo | Configuraciones pequeñas y medianas, explícitamente documentadas. | Permite medir si la cantidad y tipo de consultas activas impacta precisión, latencia o ambas. |

Nota. El EBE se organiza de manera secuencial: condición base, barridos de sensibilidad y prueba de mayor exigencia sobre la mejor configuración retenida. Los niveles consignados son candidatos de diseño y deberán cerrarse al definir la topología y el espacio físico de prueba.

Tabla C. 3

Síntesis de cobertura conjunta por condición de riesgo


| Condición de riesgo | Nivel de cobertura | N.º de fuentes | Observación |
| --- | --- | --- | --- |
| CR-01 — Persona sin casco | Sólida | 7 | Redundancia alta para casco y ausencia de casco. La cobertura proviene de SH17, SHEL5K, CHV, Pictor-PPE, Construction-PPE, GDUT-HWD y SHWD. |
| CR-02 — Persona sin chaleco | Adecuada | 4 | Cobertura suficiente para evaluación, aunque menos redundante que CR-01. La cobertura principal proviene de SH17, CHV, Pictor-PPE y Construction-PPE. |
| CR-03 — Trabajo en altura sin anticaídas | BRECHA | 0 directas | No se identificó una fuente que combine persona en altura, ausencia de sistema anticaídas y anotación aprovechable de la condición completa. |
| CR-04 — Borde elevado desprotegido | BRECHA | 0 directas | No se identificó una fuente con anotaciones de borde elevado, ausencia de protección colectiva y proximidad de personas. |
| CR-05 — Maquinaria cerca de peatones | Parcial | 1 confirmada + 1 condicionada | SODA aporta entidades y contexto de obra. MOCS también aportaría trabajadores, maquinaria y vehículos. La condición completa requiere razonamiento espacial y, eventualmente, temporal. |
| CR-06 — Persona en zona restringida | Parcial | 1 | SODA aporta elementos contextuales útiles para delimitar zonas o barreras. MOCS podría aportar trabajadores y contexto dinámico. La condición requiere polígono externo y regla espacial. |

Nota. Elaboración propia basada en el mapeo de la Tabla 27. El nivel de cobertura refleja la disponibilidad de clases, entidades o contexto útil dentro del inventario, no la dificultad intrínseca de detección ni la complejidad del razonamiento posterior. El conteo de fuentes distingue entre cobertura directa de la condición, cobertura parcial de entidades o contexto, y apoyo contextual insuficiente para constituir por sí solo una etiqueta nativa del patrón de riesgo.

Tabla C. 4

Compatibilidad de formato de anotación entre datasets candidatos y modelos OVD priorizados


| Dataset | Formato nativo | Grounding DINO (ODVG) | YOLOE / pipeline Ultralytics |
| --- | --- | --- | --- |
| SH17 | YOLO; Pascal VOC a verificar | Medio. Desde YOLO requiere conversión YOLO→COCO→ODVG. Si se confirma Pascal VOC, la ruta alternativa sería VOC→COCO→ODVG.. | Nulo/Bajo. Nulo si se usa el formato YOLO disponible; Bajo sólo si se parte de una versión Pascal VOC verificada. |
| SHEL5K | Pascal VOC | Medio. Requiere conversión VOC→COCO→ODVG. | Bajo. Requiere conversión directa VOC→YOLO. |
| CHV | Formato nativo no validado | Medio. Requiere inspección del paquete y normalización previa a COCO/ODVG. | Medio. Requiere inspección del paquete y eventual conversión a YOLO. |
| Pictor-PPE | Formato nativo no validado | Medio. Requiere inspección de la versión pública disponible y normalización a COCO/ODVG. | Medio. Requiere inspección previa y eventual conversión a YOLO. |
| Construction-PPE | YOLO | Medio. Requiere conversión YOLO→COCO→ODVG. | Nulo. Ya se encuentra en formato nativo del pipeline Ultralytics. |
| GDUT-HWD | Formato nativo a verificar; cajas + label en benchmark SSD/Caffe | Medio. Requiere verificar la estructura efectiva de cajas/labels y normalizar a COCO/ODVG. | Medio. Requiere verificar la estructura efectiva de cajas/labels y convertir a YOLO. |
| SHWD | Pascal VOC | Medio. Requiere conversión VOC→COCO→ODVG. | Bajo. Requiere conversión directa VOC→YOLO. |
| SODA | Pascal VOC | Medio. Requiere conversión VOC→COCO→ODVG. | Bajo. Requiere conversión directa VOC→YOLO. |
| MOCS | Multi-type annotation / formato a verificar | Medio condicionado. Requiere acceso efectivo, inspección del paquete y normalización a COCO/ODVG. | Medio condicionado. Requiere acceso efectivo, inspección del paquete y eventual conversión a YOLO. |

Nota. El esfuerzo se clasifica como Nulo —sin conversión—, Bajo —conversión directa o adaptación menor— o Medio —inspección previa del paquete y/o conversión en dos pasos—. La categoría “Medio condicionado” indica que el esfuerzo técnico no puede cerrarse hasta verificar acceso efectivo, estructura del paquete y términos de uso. Cuando la fuente visible no permite confirmar el formato nativo del dataset, el esfuerzo incluye una etapa previa de inspección antes de la normalización al formato de trabajo.

Tabla C. 5

Estimación de volumen de almacenamiento por dataset candidato


| Dataset | Imágenes | Vol. est. (GB) | Formato destino | Observación |
| --- | --- | --- | --- | --- |
| SH17 | 8.099 | ~3–5 | Nativo: YOLO; Pascal VOC a verificar. Destino: COCO/ODVG y/o YOLO. | Descarga desde repositorio/Kaggle del autor. |
| SHEL5K | 5.000 | ~0,5–1 | Nativo: Pascal VOC. Destino: COCO/ODVG y/o YOLO. | Disponible en Mendeley Data. |
| CHV | 1.330 | ~0,5–1 | Formato nativo a verificar. Destino: COCO/ODVG y/o YOLO. | Revisar estructura del paquete y términos de uso al descargar. |
| Pictor-PPE | 1.472 nominales; ~770–780 públicas | ~0,2–0,5 | Formato nativo a verificar. Destino: COCO/ODVG y/o YOLO. | Verificar alcance exacto de la versión pública antes de descargar. |
| Construction-PPE | 1.416 | ~0,18–0,3 | Nativo: YOLO. Destino: YOLO y, si corresponde, COCO/ODVG. | Disponible vía Ultralytics. |
| GDUT-HWD | 3.174 | ~0,5–1,5 | Formato nativo a verificar. Destino: COCO/ODVG y/o YOLO. | Confirmar estructura efectiva de cajas/labels y alcance de licencia sobre datos descargables. |
| SHWD | 7.581 | ~1–3 | Nativo: Pascal VOC. Destino: COCO/ODVG y/o YOLO. | Requiere conversión para ambos pipelines priorizados. |
| SODA | 19.846 | ~8–12 | Nativo: Pascal VOC. Destino: COCO/ODVG y/o YOLO. | Mayor volumen entre los datasets de acceso directo; filtrar según condición objetivo. |
| MOCS | 41.668 | ~15–25 | Multi-type annotation / formato a verificar. Destino condicionado a inspección del paquete. | Acceso por solicitud previa; no debe computarse como volumen operativo automático hasta confirmar acceso y términos. |
| Total estimado | ~88,9–89,6 mil | ~35–55 | — | Escenario condicionado por acceso efectivo, licencia y tamaño real del paquete entregado. |

Nota. Las estimaciones de almacenamiento son aproximadas y dependen de la resolución de las imágenes, la estructura del paquete descargado, la presencia de máscaras u otros tipos de anotación, y los formatos derivados que se generen en la instancia de análisis y diseño arquitectónico. La columna de imágenes se conserva con finalidad logística, ya que permite dimensionar almacenamiento, descarga, conversión y transferencia, sin reemplazar el análisis de cobertura y aptitud desarrollado en las secciones anteriores.


### 19.4. Anexo D - Métricas, instrumentación y bitácora experimental

Tabla D. 1

Métricas de detección OVD adoptadas para el prototipo experimental


| Métrica | Justificación de adopción | Fuente de referencia | Compromiso |
| --- | --- | --- | --- |
| AP@0.5 | Métrica base e interpretable para comparar variantes zero-shot y ajustadas al dominio; tolera errores moderados de localización y cuenta con soporte extendido en herramientas de evaluación. | Everingham et al. (2010) | Obligatorio |
| AP@[0.5:0.95] | Mantiene comparabilidad con el protocolo COCO-style al promediar AP sobre múltiples umbrales de IoU entre 0.50 y 0.95, pero no condiciona por sí sola las decisiones del prototipo experimental. | Lin et al. (2014) | Deseable |
| NMS-AP | Útil como referencia metodológica para análisis fino de OVD con etiquetas o prompts detallados y negativos duros, donde el AP convencional puede inflarse; excede el alcance operativo del prototipo experimental. | Yao et al. (2024) | Conceptual |
| Precision / Recall | Permite analizar el balance entre falsos positivos y falsos negativos con lectura operativa y desagregación por severidad, siempre que se declare explícitamente el punto operativo o criterio de reporte. | Everingham et al. (2010) | Obligatorio |

Nota. AP = Average Precision. NMS = Non-Maximum Suppression. AP@0.5 y Precision/Recall deben reportarse, como mínimo, para la baseline zero-shot y, cuando exista una variante ajustada al dominio metodológicamente comparable, para dicha variante. Precision/Recall deberá reportarse con el punto operativo o criterio de reporte explícitamente declarado. AP@[0.5:0.95] mantiene comparabilidad académica con el protocolo COCO-style y NMS-AP se conserva como referencia metodológica.

Tabla D. 2

Métricas de seguimiento multiobjeto adoptadas para el prototipo experimental


| Métrica | Justificación de adopción | Fuente de referencia | Compromiso |
| --- | --- | --- | --- |
| HOTA | Métrica integral de MOT valiosa para diagnóstico académico, pero costosa por requerir identidades persistentes. | Luiten et al. (2021) | Deseable |
| DetA / AssA | Submétricas útiles para desagregar si las fallas provienen de detección o asociación, siempre que se calcule HOTA. | Luiten et al. (2021) | Deseable |
| IDF1 | Métrica centrada en consistencia de identidad; útil como contraste complementario sobre subsets MOT bien anotados. | Ristani et al. (2016) | Deseable |
| MOTA | Comparabilidad con literatura legacy de tracking; valor diagnóstico complementario. | Bernardin y Stiefelhagen (2008) | Deseable |
| IDSW / Frag | Indicadores de estabilidad del tracker aplicables sólo sobre subsets con identidades consistentes. | Bernardin y Stiefelhagen (2008) | Deseable |
|  | Mide la reducción de falsas alarmas aportada por el tracking; exige declarar previamente cómo se cuenta un falso positivo. | Operacionalización propia | Obligatorio(*) |

Nota. HOTA = Higher Order Tracking Accuracy. DetA = Detection Accuracy. AssA = Association Accuracy. IDF1 = Identification F1. MOTA = Multiple Object Tracking Accuracy. IDSW = ID switches. Frag = fragmentación de trayectorias. = diferencia de falsos positivos entre corridas equivalentes con y sin tracker. Las métricas MOT basadas en identidades se ejecutarán sólo sobre subsets anotados para ese fin. Si no existe ground truth suficiente o no puede declararse una unidad estable de falso positivo —por frame, por track, por evento o por alerta—, no debe calcularse como métrica cuantitativa. En ese caso, sólo podrá reportarse como análisis exploratorio de estabilidad o como conteo descriptivo de activaciones espurias. (*) Si hay tracker y existe unidad de falso positivo comparable entre corridas.

Tabla D. 3

Métricas de rendimiento del pipeline y uso de recursos


| Métrica | Definición operativa | Formato de reporte | Compromiso | Criterio de estabilidad |
| --- | --- | --- | --- | --- |
| FPS efectivos | Cuadros completamente procesados por segundo al final del pipeline. | Media, P50, P95, P99 y variación | Obligatorio | Período de calentamiento previo y corrida sostenida |
| Latencia G2A | Intervalo entre captura o lectura del frame y disponibilidad del resultado de inferencia. | ms (P50, P95, P99) | Obligatorio | Timestamps monotónicos |
| Jitter | Variabilidad de la latencia entre cuadros consecutivos. | ms (desv. est. / coef. variación) | Deseable | Reportar junto con G2A |
| Uso de VRAM | Memoria de video ocupada por modelo, tensores y buffers. | MB y % | Obligatorio | Sin crecimiento monótono |
| Utilización GPU | Porcentaje de ocupación de la GPU durante la corrida. | % | Deseable | Registrar media y picos |
| Uso de RAM/CPU | Consumo de memoria del sistema y presión sobre CPU del proceso completo. | MB/GB y %CPU | Deseable | Registrar serie temporal |

Nota. G2A = Glass-to-Algorithm. FPS = Frames Per Second. VRAM = Video Random Access Memory. El reporte obligatorio mínimo incluye FPS efectivos, latencia G2A y uso de VRAM. Cuando sea posible, conviene registrar además GPU, RAM y CPU con muestreo periódico durante una corrida sostenida.

Tabla D. 4

Umbrales orientativos por severidad para la lectura operativa de la alerta


| Severidad | máx. orient. | TTFD máx. | SDR mín. orient. | Persistencia orient. | Prioridad FP/FN | Observación |
| --- | --- | --- | --- | --- | --- | --- |
| Crítica | 3-5 s | < 1 s | >= 0.50 | 2-4 s | Minimizar FN | Ventana corta; se prioriza no omitir eventos críticos |
| Alta | 5-10 s | < 3 s | >= 0.60 | 3-5 s | Balance FP/FN | Compromiso entre rapidez de respuesta y estabilidad |
| Media | 10-20 s | < 10 s | >= 0.70 | 5-10 s | Minimizar FP | Puede exigirse mayor evidencia antes de confirmar |

Nota. Los valores indicados son orientativos y se alinean con la lógica de persistencia definida en la taxonomía de condiciones de riesgo, patrones y prompts. La columna máx. orient. refiere al tiempo hasta la alerta confirmada dentro del sistema. Ese valor incluye la ventana funcional de persistencia más el presupuesto computacional del pipeline; por esa razón, excede necesariamente a la persistencia orient. La traducción de persistencia a fotogramas dependerá del throughput efectivo del sistema. La calibración empírica final corresponde a la validación experimental.

Tabla D. 5

Insumos mínimos requeridos antes de iniciar una campaña de medición


| Familia de métricas | Ground truth o insumo | Instrumentación mínima | Herramientas o artefactos | Salida mínima |
| --- | --- | --- | --- | --- |
| Detección (AP, P/R) | Bounding boxes y etiquetas por imagen o frame. | Export de predicciones por corrida. | pycocotools o conversión COCO equivalente. | AP y P/R por variante, con punto operativo o criterio de reporte explícitamente declarado. |
| Tracking (HOTA, DetA / AssA, IDF1, MOTA, IDSW / Frag) | Boxes y track_id persistente por frame. | Export MOT-compatible sobre subset anotado. | TrackEval u otra implementación equivalente. | Métricas MOT sobre subset, con declaración explícita de qué métricas fueron ejecutadas y cuáles no. |
| Pipeline (FPS, , jitter) | No requiere GT semántico. | Timestamps por etapa del pipeline. | Logs internos y scripts de agregación. | P50/P95/P99, promedio y variación. |
| Alerta y patrón (, TTFD, SDR, si aplica) | Inicio anotado de la condición de riesgo, duración o intervalo temporal del evento y criterio de activación del patrón. | Logs con timestamps de primera evidencia positiva, inicio de patrón candidato si corresponde, patrón confirmado, alerta registrada y disponibilidad/notificación si aplica. | Event log del pipeline, bitácora de corrida, export de eventos de patrón y scripts de agregación temporal. | TTFD, SDR y cuando exista evaluación de patrón y alerta registrada; sólo si existe trayecto instrumentado. |
| Recursos (VRAM, GPU, RAM, CPU) | No requiere GT semántico. | Muestreo periódico durante la corrida. | nvidia-smi, psutil u otras herramientas del sistema. | Series temporales y resumen. |
| Alerta (, si aplica, TTFD, SDR) | Inicio del evento, duración, severidad y criterio de activación del patrón. | Logs de detección, evaluación de patrón, confirmación de patrón, alerta registrada y consulta o notificación si aplica. | Motor de evaluación de patrones instrumentado; registro interno de alertas; logs del trayecto de consulta o notificación si aplica. | Tiempos y proporciones por evento, con declaración de métricas no aplicables cuando falte instrumentación. |
| Fine-tuning | Split train/eval disjunto y baseline zero-shot explícita. | Registro de entrenamiento y evaluación. | Logs de entrenamiento y scripts comparativos. | Deltas y costo de entrenamiento, cuando aplique. |

Nota. La ausencia de cualquiera de los insumos requeridos para una familia de métricas debe declararse antes de planificar la campaña experimental. En particular, no corresponde reemplazar ground truth inexistente por estimaciones informales ni interpretar logs incompletos como evidencia suficiente de desempeño. Toda métrica sin insumos mínimos deberá registrarse como no ejecutada o no aplicable, según corresponda.

Tabla D. 6

Campos mínimos recomendados para la bitácora experimental


| Campo | Contenido mínimo recomendado | Uso en la interpretación |
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

Nota. Una métrica sin contexto de corrida pierde interpretabilidad y trazabilidad.


## Referencias

Abdalwhab, A. B. M., Imran, A., Heydarian, S., Iordanova, I., & St-Onge, D. (2025). Are open-vocabulary models ready for detection of MEP elements on construction sites? In Proceedings of the 42nd International Symposium on Automation and Robotics in Construction (pp. 1421–1424). International Association for Automation and Robotics in Construction. https://doi.org/10.22260/ISARC2025/0184

Active Silicon Ltd. (2025). Obtaining the lowest latency from your Harrier AF-Zoom IP camera (Technical Report Technical Note 015 (TN015)). Active Silicon. https://www.activesilicon.com/wp-content/uploads/TECH-NOTE-Harrier-IP-Lowest-Latency-Guide.pdf

Adobe. (2021, enero 13). Adobe Flash Player EOL General Information. https://www.adobe.com/hk_en/products/flashplayer/end-of-life-alternative.html

Advanced Micro Devices, Inc. (s. f.). AMD Ryzen 5 8645HS. https://www.amd.com/en/products/processors/laptop/ryzen/8000-series/amd-ryzen-5-8645hs.html

Adžemović, M. (2025). Deep Learning-Based Multi-Object Tracking: A Comprehensive Survey from Foundations to State-of-the-Art (arXiv:2506.13457). arXiv. https://doi.org/10.48550/arXiv.2506.13457

Agencia de Acceso a la Información Pública. (s. f.-a). Conocé tus derechos respecto a tus datos personales. Argentina.gob.ar. Recuperado el 12 de enero de 2026, de https://www.argentina.gob.ar/aaip/datospersonales/derechos

Agencia de Acceso a la Información Pública. (s. f.-b). Videovigilancia: ¿Por qué hay que registrar bases de datos de videovigilancia y presentar el manual de tratamiento? Argentina.gob.ar. Recuperado el 12 de enero de 2026, de https://www.argentina.gob.ar/aaip/datospersonales/responsables/videovigilancia

Aharon, N., Orfaig, R., & Bobrovsky, B.-Z. (2022). BoT-SORT: Robust Associations Multi-Pedestrian Tracking (arXiv:2206.14651). arXiv. https://doi.org/10.48550/arXiv.2206.14651

Ahmad, H. M., y Rahimi, A. (2025). SH17: A dataset for human safety and personal protective equipment detection in manufacturing industry. Journal of Safety Science and Resilience, 6(2), 175–185. https://doi.org/10.1016/j.jnlssr.2024.09.002

Ahmad, I., Xiaohui Wei, Yu Sun, & Ya-Qin Zhang. (2005). Video transcoding: An overview of various techniques and research issues. IEEE Transactions on Multimedia, 7(5), 793–804. https://doi.org/10.1109/TMM.2005.854472

AILab-CVC. (2024, January 30). YOLO-World. GitHub. Retrieved January 21, 2026, from https://github.com/AILab-CVC/YOLO-World

AirenSoft. (s. f.-a). Low-Latency HLS. AirenSoft. OvenMediaEngine Documentation. Recuperado el 8 de enero de 2026, de https://docs.ovenmediaengine.com/streaming/low-latency-hls

AirenSoft. (s. f.-b). OvenMediaEngine: Introduction. AirenSoft. OvenMediaEngine Documentation. Recuperado el 8 de enero de 2026, de https://docs.ovenmediaengine.com/

Amirante, A., Castaldi, T., Miniero, L., & Romano, S. P. (2014). Janus: A general purpose WebRTC gateway. Proceedings of the Conference on Principles, Systems and Applications of IP Telecommunications, 1–8. https://doi.org/10.1145/2670386.2670389

Amirante, A., Castaldi, T., Miniero, L., & Romano, S. P. (2015). Performance analysis of the Janus WebRTC gateway. Proceedings of the 1st Workshop on All-Web Real-Time Systems, 1–7. https://doi.org/10.1145/2749215.2749223

Ananthanarayanan, G., Bahl, P., Bodik, P., Chintalapudi, K., Philipose, M., Ravindranath, L., & Sinha, S. (2017). Real-Time Video Analytics: The Killer App for Edge Computing. Computer, 50(10), 58–67. https://doi.org/10.1109/MC.2017.3641638

Andre, E., Le Breton, N., Lemesle, A., Roux, L., & Gouaillard, A. (2018). Comparative Study of WebRTC Open Source SFUs for Video Conferencing. 2018 Principles, Systems and Applications of IP Telecommunications (IPTComm), 1–8. https://doi.org/10.1109/IPTCOMM.2018.8567642

Apple Developer. (2019). Introducing Low-Latency HLS [Video]. https://developer.apple.com/videos/play/wwdc2019/502/

Apple Developer. (s. f.). Enabling Low-Latency HTTP Live Streaming (HLS). Recuperado https://developer.apple.com/documentation/http-live-streaming/enabling-low-latency-http-live-streaming-hls

Argentina. (2000). Ley N.º 25.326: Ley de Protección de los Datos Personales. Infoleg. https://servicios.infoleg.gob.ar/infolegInternet/anexos/60000-64999/64790/texact.htm

Argentina. (2001, noviembre 29). Decreto 1558/2001: Ley 25.326—Reglamentación. Argentina.gob.ar. https://www.argentina.gob.ar/normativa/nacional/decreto-1558-2001-70368

Argentina. (2006, septiembre 19). Disposición 11/2006: Medidas de seguridad para el tratamiento y conservación de los datos personales. Argentina.gob.ar. https://www.argentina.gob.ar/normativa/nacional/disposici%C3%B3n-11-2006-120120

Argentina. (2015, febrero 24). Disposición 10/2015: Condiciones de licitud para las actividades de recolección y posterior tratamiento de imágenes digitales de personas con fines de seguridad. Argentina.gob.ar. https://www.argentina.gob.ar/normativa/nacional/disposici%C3%B3n-10-2015-243335

Axis Communications AB. (2015). Latency in live network video surveillance (63380/EN/R1/1504) [White paper]. https://www.axis.com/dam/public/9d/e4/5d/latency-in-live-network-video-surveillance-en-US-190945.pdf

Bachhuber, C., Steinbach, E., Freundl, M., & Reisslein, M. (2018). On the Minimization of Glass-to-Glass and Glass-to-Algorithm Delay in Video Communication. IEEE Transactions on Multimedia, 20(1), 238–252. https://doi.org/10.1109/TMM.2017.2726189

Badidi, E., Moumane, K., & Ghazi, F. E. (2023). Opportunities, Applications, and Challenges of Edge-AI Enabled Video Analytics in Smart Cities: A Systematic Review. IEEE Access, 11, 80543–80572. https://doi.org/10.1109/ACCESS.2023.3300658

Bar-Shalom, Y., Fortmann, T. E., & Cable, P. G. (1990). Tracking and Data Association. The Journal of the Acoustical Society of America, 87(2), 918–919. https://doi.org/10.1121/1.398863

Bar-Shalom, Y., Willett, P. K., & Tian, X. (2011). Tracking and data fusion: A handbook of algorithms. YBS Publishing.

Bass, L., Clements, P., & Kazman, R. (2022). Software architecture in practice (Fourth edition). Addison-Wesley.

Bentaleb, A., Taani, B., Begen, A. C., Timmerer, C., & Zimmermann, R. (2019). A Survey on Bitrate Adaptation Schemes for Streaming Media Over HTTP. IEEE Communications Surveys & Tutorials, 21(1), 562–585. https://doi.org/10.1109/COMST.2018.2862938

Bernardin, K., & Stiefelhagen, R. (2008). Evaluating multiple object tracking performance: The CLEAR MOT metrics. EURASIP Journal on Image and Video Processing, 2008(1), 1-10. https://doi.org/10.1155/2008/246309

Bewley, A., Ge, Z., Ott, L., Ramos, F., y Upcroft, B. (2016). Simple online and realtime tracking. En 2016 IEEE International Conference on Image Processing (ICIP) (pp. 3464-3468). IEEE. https://doi.org/10.1109/ICIP.2016.7533003

Bianchi, L., Carrara, F., Messina, N., Gennaro, C., & Falchi, F. (2024). The devil is in the fine-grained details: Evaluating open-vocabulary object detectors for fine-grained understanding. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 22520-22529). https://doi.org/10.1109/CVPR52733.2024.02125

bluenviron. (s. f.). MediaMTX [Software]. GitHub. Recuperado el 8 de enero de 2026, de https://github.com/bluenviron/mediamtx

Bonomi, F., Milito, R., Zhu, J., & Addepalli, S. (2012). Fog computing and its role in the internet of things. Proceedings of the First Edition of the MCC Workshop on Mobile Cloud Computing, 13–16. https://doi.org/10.1145/2342509.2342513

Bossen, F., Bross, B., Suhring, K., & Flynn, D. (2012). HEVC Complexity and Implementation Analysis. IEEE Transactions on Circuits and Systems for Video Technology, 22(12), 1685–1696. https://doi.org/10.1109/TCSVT.2012.2221255

Buslaev, A., Iglovikov, V. I., Khvedchenya, E., Parinov, A., Druzhinin, M., y Kalinin, A. A. (2020). Albumentations: Fast and flexible image augmentations. Information, 11(2), 125. https://doi.org/10.3390/info11020125

Cao, J., Pang, J., Weng, X., Khirodkar, R., & Kitani, K. (2023). Observation-Centric SORT: Rethinking SORT for Robust Multi-Object Tracking. 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 9686–9696. https://doi.org/10.1109/CVPR52729.2023.00934

Card, S. K., Moran, T. P., & Newell, A. (2008). The psychology of human-computer interaction (Repr). Erlbaum.

Carion, N., Massa, F., Synnaeve, G., Usunier, N., Kirillov, A., & Zagoruyko, S. (2020). End-to-End Object Detection with Transformers (arXiv:2005.12872). arXiv. https://doi.org/10.48550/arXiv.2005.12872

Centro de Computación de Alto Desempeño. (2026, 10 de abril). Clusters disponibles. UNC Supercómputo. https://wiki.ccad.unc.edu.ar/infra/clusters.html

Changpinyo, S., Sharma, P., Ding, N., & Soricut, R. (2021). Conceptual 12M: Pushing web-scale image-text pre-training to recognize long-tail visual concepts. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 3557–3567). https://doi.org/10.1109/CVPR46437.2021.00356

Chen, J., & Ran, X. (2019). Deep Learning With Edge Computing: A Review. Proceedings of the IEEE, 107(8), 1655–1674. https://doi.org/10.1109/JPROC.2019.2921977

Cheng, T., Song, L., Ge, Y., Liu, W., Wang, X., & Shan, Y. (2024). YOLO-World: Real-time open-vocabulary object detection. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 16901–16911). https://doi.org/10.1109/CVPR52733.2024.01599

Clark, A., Singh, V., & Wu, Q. (2013). RTP Control Protocol (RTCP) Extended Report (XR) Block for De-Jitter Buffer Metric Reporting (No. RFC7005; p. RFC7005). RFC Editor. https://doi.org/10.17487/rfc7005

Cohen, J. (1960). A coefficient of agreement for nominal scales. Educational and Psychological Measurement, 20(1), 37–46. https://doi.org/10.1177/001316446002000104

Cugola, G., & Margara, A. (2012). Processing flows of information: From data stream to complex event processing. ACM Computing Surveys, 44(3), 1–62. https://doi.org/10.1145/2187671.2187677

Dalvi, M., Singh, N., Bhingarde, S., & Chalke, K. (2025). Construction-PPE: Personal Protective Equipment Detection Dataset (Versión 1.0.0) [Dataset]. Ultralytics. https://docs.ultralytics.com/datasets/detect/construction-ppe/

DASH Industry Forum. (2020, marzo 27). Low-latency Modes for DASH. CR-Low-Latency-Live-r8. https://dashif.org/docs/CR-Low-Latency-Live-r8.pdf

Deber, J., Jota, R., Forlines, C., & Wigdor, D. (2015). How Much Faster is Fast Enough?: User Perception of Latency & Latency Improvements in Direct and Indirect Touch. Proceedings of the 33rd Annual ACM Conference on Human Factors in Computing Systems, 1827–1836. https://doi.org/10.1145/2702123.2702300

Decreto 351/79 de 1979. Reglamentación de la Ley 19.587 de Higiene y Seguridad en el Trabajo. (1979, febrero 5). Infoleg. https://servicios.infoleg.gob.ar/infolegInternet/anexos/30000-34999/32030/dto351-1979-anexo1.htm

Decreto 911/96 de 1996. Reglamento de Higiene y Seguridad para la Industria de la Construcción. (1996, 5 de agosto). Infoleg. https://servicios.infoleg.gob.ar/infolegInternet/anexos/35000-39999/38568/texact.htm

Dendorfer, P., Rezatofighi, H., Milan, A., Shi, J., Cremers, D., Reid, I., Roth, S., Schindler, K., & Leal-Taixé, L. (2020). MOT20: A benchmark for multi object tracking in crowded scenes (arXiv:2003.09003). arXiv. https://doi.org/10.48550/arXiv.2003.09003

Deschere, P. (2025, December 9). Introducing Roboflow Rapid: Text prompt to vision model in minutes. Roboflow Blog. Retrieved January 21, 2026, from https://blog.roboflow.com/roboflow-rapid/

Ding, M., Xiao, B., Codella, N., Luo, P., Wang, J., & Yuan, L. (2022, April 7). [2204.03645] DaViT: Dual Attention Vision Transformers. arXiv. Retrieved January 21, 2026, from https://arxiv.org/abs/2204.03645

Du, C., Lin, C., Jin, R., Chai, B., Yao, Y., & Su, S. (2024). Exploring the State-of-the-Art in Multi-Object Tracking: A Comprehensive Survey, Evaluation, Challenges, and Future Directions. Multimedia Tools and Applications, 83(29), 73151–73189. https://doi.org/10.1007/s11042-023-17983-2

Du, Y., Wei, F., Zhang, Z., Shi, M., Gao, Y., & Li, G. (2022). Learning to prompt for open-vocabulary object detection with vision-language model. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 14084-14093). https://doi.org/10.1109/CVPR52688.2022.01369

Duan, R., Deng, H., Tian, M., Deng, Y., y Lin, J. (2022). SODA: A large-scale open site object detection dataset for deep learning in construction. Automation in Construction, 142, 104499. https://doi.org/10.1016/j.autcon.2022.104499

Emami, P., Pardalos, P. M., Elefteriadou, L., & Ranka, S. (2021). Machine Learning Methods for Data Association in Multi-Object Tracking. ACM Computing Surveys, 53(4), 1–34. https://doi.org/10.1145/3394659

Erfanian, A., Amirpour, H., Tashtarian, F., Timmerer, C., & Hellwagner, H. (2021). LwTE: Light-Weight Transcoding at the Edge. IEEE Access, 9, 112276–112289. https://doi.org/10.1109/ACCESS.2021.3102633

European Data Protection Board. (2020, enero 30). Guidelines 3/2019 on processing of personal data through video devices (Version 2.0). EDPB. https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-32019-processing-personal-data-through-video_en

European Parliament & Council of the European Union. (2016, abril 27). Regulation (EU) 2016/679 (General Data Protection Regulation). EUR-Lex. https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng

Everingham, M., Van Gool, L., Williams, C. K. I., Winn, J., & Zisserman, A. (2010). The Pascal Visual Object Classes (VOC) Challenge. International Journal of Computer Vision, 88(2), 303–338. https://doi.org/10.1007/s11263-009-0275-4

Filali, A., Abouaomar, A., Cherkaoui, S., Kobbane, A., & Guizani, M. (2020). Multi-Access Edge Computing: A Survey. IEEE Access, 8, 197017–197046. https://doi.org/10.1109/ACCESS.2020.3034136

Fu, S., Yang, Q., Mo, Q., Yan, J., Wei, X., Meng, J., Xie, X., & Zheng, W.-S. (2025, January 31). [2501.18954] LLMDet: Learning Strong Open-Vocabulary Object Detectors under the Supervision of Large Language Models. arXiv. Retrieved January 21, 2026, from https://arxiv.org/abs/2501.18954

Garcia, B., Lopez-Fernandez, L., Gallego, M., & Gortazar, F. (2017). Kurento: The Swiss Army Knife of WebRTC Media Servers. IEEE Communications Standards Magazine, 1(2), 44–51. https://doi.org/10.1109/MCOMSTD.2017.1700006

Gettys, J., & Nichols, K. (2012). Bufferbloat: Dark buffers in the internet. Communications of the ACM, 55(1), 57–65. https://doi.org/10.1145/2063176.2063196

Go Packages. (s. f.). Mediamtx Command. Recuperado el 8 de enero de 2026, de https://pkg.go.dev/github.com/bluenviron/mediamtx

Google. (2022, May). owlvit-large-patch14. Hugging Face. https://huggingface.co/google/owlvit-large-patch14

Google. (2023, June). owlv2-base-patch16-ensemble. Hugging Face. https://huggingface.co/google/owlv2-base-patch16-ensemble

GStreamer. (s. f.-a). GStreamer application development manual. Recuperado el 12 de febrero de 2026, de https://gstreamer.freedesktop.org/documentation/?gi-language=c

GStreamer. (s. f.-b). shmsink: GStreamer Bad Plugins 1.0 Plugins Reference Manual. Recuperado el 12 de febrero de 2026, de https://www.manpagez.com/html/gst-plugins-bad-plugins-1.0/gst-plugins-bad-plugins-1.0-1.10.0/gst-plugins-bad-plugins-shmsink.php

Gu, X., Lin, T.-Y., Kuo, W., & Cui, Y. (2021). Open-vocabulary object detection via vision and language knowledge distillation. arXiv. https://doi.org/10.48550/arXiv.2104.13921

Gupta, A., Dollár, P., & Girshick, R. (2019). LVIS: A Dataset for Large Vocabulary Instance Segmentation (arXiv:1908.03195). arXiv. https://doi.org/10.48550/arXiv.1908.03195

HP Inc. (s. f.). Victus Gaming Laptop 15-fb2024la (A14LSLA): Todas las especificaciones técnicas. https://www.hp.com/py-es/products/laptops/product-details/product-specifications/2102249493

Hugging Face. (2024, September 25). OmDet-Turbo. Hugging Face. Retrieved January 21, 2026, from https://huggingface.co/docs/transformers/en/model_doc/omdet-turbo

IDEA-Research. (2023, April 6). IDEA-Research / Grounded-Segment-Anything: Grounded-Segment-Anything. GitHub. Retrieved January 21, 2026, from https://github.com/IDEA-Research/Grounded-Segment-Anything

IDEA-Research. (2024, August 1). IDEA-Research/Grounded-SAM-2: Grounded SAM 2: Ground and Track Anything in Videos. GitHub. Retrieved January 21, 2026, from https://github.com/IDEA-Research/Grounded-SAM-2

IDEA-Research. (2024, May 18). IDEA-Research/GroundingDINO: [ECCV 2024] Official implementation of the paper "Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection". GitHub. Retrieved January 21, 2026, from https://github.com/IDEA-Research/GroundingDINO

IDEA-Research. (2024, November 20). IDEA-Research / DINO-X-API: A Unified Vision Model for Open-World Object Detection and Understanding. GitHub. https://github.com/IDEA-Research/DINO-X-API

Intel. (2021). Upgrading from Intel® Media SDK to Intel® oneAPI Video Processing... https://www.intel.com/content/www/us/en/docs/onevpl/upgrade-from-msdk/2021-3/overview.html

Intel. (2022). H.265/HEVC Hardware Encoding and Decoding Support. https://www.intel.com/content/www/us/en/support/articles/000037112.html

Intel. (s. f.-a). Intel® Video Processing Library: Video Codecs. Recuperado https://www.intel.com/content/www/us/en/developer/tools/vpl/overview.html

Intel. (s. f.-b). Intel oneAPI Video Processing Library (oneVPL). Recuperado https://www.intel.com/content/www/us/en/docs/oneapi/programming-guide/2023-1/intel-oneapi-video-processing-library-onevpl.html

Intel. (s. f.-c). Media Capabilities Supported by Intel Hardware. Recuperado https://www.intel.com/content/www/us/en/docs/onevpl/developer-reference-media-intel-hardware/1-1/overview.html

Intel. (s. f.-d). VA-API: Video Acceleration (VA) API. Recuperado https://intel.github.io/libva/

Internet Assigned Numbers Authority. (s. f.). Service Name and Transport Protocol Port Number Registry. Recuperado el 9 de enero de 2026, de https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml

Iorga, M., Feldman, L., Barton, R., Martin, M. J., Goren, N., & Mahmoudi, C. (2018). Fog computing conceptual model (NIST SP 500-325; p. NIST SP 500-325). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.500-325

iSEE-Laboratory. (2025, January 31). iSEE-Laboratory/LLMDet: (CVPR 2025 highlight✨) Official repository of paper "LLMDet: Learning Strong Open-Vocabulary Object Detectors under the Supervision of Large Language Models". GitHub. Retrieved January 21, 2026, from https://github.com/iSEE-Laboratory/LLMDet

ISO. (2018). ISO 45001:2018 Occupational health and safety management systems—Requirements with guidance for use. ISO. https://www.iso.org/standard/63787.html

ISO. (2023). ISO/IEC 42001:2023—Artificial intelligence management system. ISO. https://www.iso.org/standard/42001

ISO/IEC. (2022). Information technology—Dynamic adaptive streaming over HTTP (DASH)—Part 1: Media presentation description and segment formats. ISO/IEC 23009-1:2022. https://www.iso.org/standard/83314.html

Jeong, E., Kim, J., & Ha, S. (2022). TensorRT-Based Framework and Optimization Methodology for Deep Learning Inference on Jetson Boards. ACM Transactions on Embedded Computing Systems, 21(5), 1–26. https://doi.org/10.1145/3508391

Jiang, K., Huang, J., Xie, W., Lei, J., Li, Y., Shao, L., & Lu, S. (2024). Domain adaptation for large-vocabulary object detectors. In Advances in Neural Information Processing Systems, 37 (pp. 75422–75453). https://doi.org/10.52202/079017-2401

Jiang, Q., Li, F., Zeng, Z., Ren, T., Liu, S., & Zhang, L. (2024). T-Rex2: Towards Generic Object Detection via Text-Visual Prompt Synergy (arXiv:2403.14610). arXiv. https://doi.org/10.48550/arXiv.2403.14610

Keranen, A., Holmberg, C., & Rosenberg, J. (2018). Interactive Connectivity Establishment (ICE): A Protocol for Network Address Translator (NAT) Traversal (No. RFC8445; p. RFC8445). RFC Editor. https://doi.org/10.17487/RFC8445

Khan, M. A., Baccour, E., Chkirbene, Z., Erbad, A., Hamila, R., Hamdi, M., & Gabbouj, M. (2022). A Survey on Mobile Edge Computing for Video Streaming: Opportunities and Challenges. IEEE Access, 10, 120514–120550. https://doi.org/10.1109/ACCESS.2022.3220694

Khattak, M. U., Rasheed, H., Maaz, M., Khan, S., & Khan, F. S. (2023). MaPLe: Multi-modal Prompt Learning (arXiv:2210.03117). arXiv. https://doi.org/10.48550/arXiv.2210.03117

Kim, J., Cho, E., Kim, S., & Kim, H. J. (2024). Retrieval-augmented open-vocabulary object detection. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 17427–17436). https://doi.org/10.1109/CVPR52733.2024.01650

Kirillov, A., Mintun, E., Ravi, N., Mao, H., Rolland, C., Gustafson, L., Xiao, T., Whitehead, S., Berg, A. C., Lo, W.-Y., Dollár, P., & Girshick, R. (2023). Segment Anything (arXiv:2304.02643). arXiv. https://doi.org/10.48550/arXiv.2304.02643

Kirkpatrick, J., Pascanu, R., Rabinowitz, N., Veness, J., Desjardins, G., Rusu, A. A., Milan, K., Quan, J., Ramalho, T., Grabska-Barwinska, A., Hassabis, D., Clopath, C., Kumaran, D., & Hadsell, R. (2017). Overcoming catastrophic forgetting in neural networks. Proceedings of the National Academy of Sciences, 114(13), 3521-3526. https://doi.org/10.1073/pnas.1611835114

Kreutz, D., Ramos, F. M. V., Esteves Verissimo, P., Esteve Rothenberg, C., Azodolmolky, S., & Uhlig, S. (2015). Software-Defined Networking: A Comprehensive Survey. Proceedings of the IEEE, 103(1), 14–76. https://doi.org/10.1109/JPROC.2014.2371999

Kuhn, H. W. (1955). The Hungarian method for the assignment problem. Naval Research Logistics Quarterly, 2(1–2), 83–97. https://doi.org/10.1002/nav.3800020109

Kurose, J. F., & Ross, K. W. (2021). Computer networking: A top-down approach (Eighth edition). Pearson.

Law, W. (2020). Meeting live broadcast requirements – the latest on DASH Low Latency [Presentation]. DVB World Online Presentation. https://dvb.org/wp-content/uploads/2020/03/Latest-on-DASH-low-latency.pdf

Ley 19.587 de 1972. Ley de Higiene y Seguridad en el Trabajo. (1972). Infoleg. https://servicios.infoleg.gob.ar/infolegInternet/anexos/15000-19999/17612/norma.htm

Li, L. H., Zhang, P., Zhang, H., Yang, J., Li, C., Zhong, Y., Wang, L., Yuan, L., Zhang, L., Hwang, J.-N., Chang, K.-W., & Gao, J. (2021, December 7). [2112.03857] Grounded Language-Image Pre-training. arXiv. Retrieved January 21, 2026, from https://arxiv.org/abs/2112.03857

Li, S., Danelljan, M., Ding, H., Huang, T. E., & Yu, F. (2022, July 26). Tracking Every Thing in the Wild. arXiv. https://arxiv.org/abs/2207.12978

Li, S., Fischer, T., Ke, L., Ding, H., Danelljan, M., & Yu, F. (2023). OVTrack: Open-Vocabulary Multiple Object Tracking. 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 5567–5577. https://doi.org/10.1109/CVPR52729.2023.00539

Li, S., Ren, H., Xie, X., & Cao, Y. (2025). A Review of Multi‐Object Tracking in Recent Times. IET Computer Vision, 19(1), e70010. https://doi.org/10.1049/cvi2.70010

Li, X., Cho, B., & Xiao, Y. (2022). Balancing Latency and Accuracy on Deep Video Analytics at the Edge. 2022 IEEE 19th Annual Consumer Communications & Networking Conference (CCNC), 299–306. https://doi.org/10.1109/CCNC49033.2022.9700636

Li, X., Salehi, M. A., Joshi, Y., Darwich, M. K., Landreneau, B., & Bayoumi, M. (2019). Performance Analysis and Modeling of Video Transcoding Using Heterogeneous Cloud Services. IEEE Transactions on Parallel and Distributed Systems, 30(4), 910–922. https://doi.org/10.1109/TPDS.2018.2870651

Lin, T.-Y., Maire, M., Belongie, S., Hays, J., Perona, P., Ramanan, D., Dollar, P. y Zitnick, C. L. (2014). Microsoft COCO: Common objects in context. En D. Fleet, T. Pajdla, B. Schiele y T. Tuytelaars (Eds.), Computer Vision - ECCV 2014 (Vol. 8693, pp. 740-755). Springer. https://doi.org/10.1007/978-3-319-10602-1_48

Liu, L., Li, H., & Gruteser, M. (2019). Edge Assisted Real-time Object Detection for Mobile Augmented Reality. The 25th Annual International Conference on Mobile Computing and Networking, 1–16. https://doi.org/10.1145/3300061.3300116

Liu, S., Zeng, Z., Ren, T., Li, F., Zhang, H., Yang, J., Jiang, Q., Li, C., Yang, J., Su, H., Zhu, J., & Zhang, L. (2024). Grounding DINO: Marrying DINO with grounded pre-training for open-set object detection. In Computer Vision - ECCV 2024 (pp. 38-55). Springer. https://doi.org/10.1007/978-3-031-72970-6_3

Long, Z., y Li, W. (2023). Open-GroundingDino [Repositorio de código]. GitHub. https://github.com/longzw1997/Open-GroundingDino

López, L., París, M., Carot, S., García, B., Gallego, M., Gortázar, F., Benítez, R., Santos, J. A., Fernández, D., Vlad, R. T., Gracia, I., & López, F. J. (2016). Kurento: The WebRTC Modular Media Server. Proceedings of the 24th ACM International Conference on Multimedia, 1187–1191. https://doi.org/10.1145/2964284.2973798

Luiten, J., Os̆ep, A., Dendorfer, P., Torr, P., Geiger, A., Leal-Taixé, L., & Leibe, B. (2021). HOTA: A Higher Order Metric for Evaluating Multi-object Tracking. International Journal of Computer Vision, 129(2), 548–578. https://doi.org/10.1007/s11263-020-01375-2

Luo, W., Xing, J., Milan, A., Zhang, X., Liu, W., & Kim, T.-K. (2021). Multiple object tracking: A literature review. Artificial Intelligence, 293, 103448. https://doi.org/10.1016/j.artint.2020.103448

Luxonis. (s. f.-b). OAK-D Pro PoE [Documentación de hardware]. Luxonis Docs. https://docs.luxonis.com/hardware/products/OAK-D%20Pro%20PoE

Mach, P., & Becvar, Z. (2017). Mobile Edge Computing: A Survey on Architecture and Computation Offloading. IEEE Communications Surveys & Tutorials, 19(3), 1628–1656. https://doi.org/10.1109/COMST.2017.2682318

Magalhães, S. C., Santos, F. N., Machado, P., Moreira, A. P., & Dias, J. (2023). Benchmarking Edge Computing Devices for Grape Bunches and Trunks Detection using Accelerated Object Detection Single Shot MultiBox Deep Learning Models. Engineering Applications of Artificial Intelligence, 117, 105604. https://doi.org/10.1016/j.engappai.2022.105604

Mahmud, R., Kotagiri, R., & Buyya, R. (2018). Fog Computing: A Taxonomy, Survey and Future Directions. En B. Di Martino, K.-C. Li, L. T. Yang, & A. Esposito (Eds.), Internet of Everything (pp. 103–130). Springer Singapore. https://doi.org/10.1007/978-981-10-5861-5_5

Mahy, R., Matthews, P., & Rosenberg, J. (2010). Traversal Using Relays around NAT (TURN): Relay Extensions to Session Traversal Utilities for NAT (STUN) (No. RFC5766; p. RFC5766). RFC Editor. https://doi.org/10.17487/rfc5766

Mallick, S. (2025, 3 de junio). Fine-tuning Grounding DINO: Open-vocabulary object detection. LearnOpenCV. https://learnopencv.com/fine-tuning-grounding-dino/

May, W. (2017). HTTP Live Streaming (R. Pantos, Ed.; No. RFC8216; p. RFC8216). RFC Editor. https://doi.org/10.17487/RFC8216

Mazor, M., Moran, R., & Fleming, S. M. (2021). Stage 2 registered report: Metacognitive asymmetries in visual perception. Neuroscience of Consciousness, 2021(1), niab025. https://doi.org/10.1093/nc/niab025

Meetecho. (s. f.). VideoRoom plugin documentation. Meetecho. Janus WebRTC Server Documentation. Recuperado el 8 de enero de 2026, de https://janus.conf.meetecho.com/docs/videoroom

Meinhardt, T., Kirillov, A., Leal-Taixe, L., & Feichtenhofer, C. (2022). TrackFormer: Multi-Object Tracking with Transformers. 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 8834–8844. https://doi.org/10.1109/CVPR52688.2022.00864

Mell, P. M., & Grance, T. (2011). The NIST definition of cloud computing (NIST SP 800-145; 0 ed., p. NIST SP 800-145). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-145

Mesa. (2025). Mesa 25.1.0 Release Notes / 2025-05-07—The Mesa 3D Graphics Library latest documentation. https://docs.mesa3d.org/relnotes/25.1.0.html

Meta AI. (2019). PyTorch [Software]. https://pytorch.org

Microsoft. (2024, June). Florence-2-large. Hugging Face. https://huggingface.co/microsoft/Florence-2-large

Milan, A., Leal-Taixe, L., Reid, I., Roth, S., & Schindler, K. (2016). MOT16: A Benchmark for Multi-Object Tracking (arXiv:1603.00831). arXiv. https://doi.org/10.48550/arXiv.1603.00831

Minderer, M., Gritsenko, A., & Houlsby, N. (2024). Scaling Open-Vocabulary Object Detection (arXiv:2306.09683). arXiv. https://doi.org/10.48550/arXiv.2306.09683

Minderer, M., Gritsenko, A., Stone, A., Neumann, M., Weissenborn, D., Dosovitskiy, A., Mahendran, A., Arnab, A., Dehghani, M., Shen, Z., Wang, X., Zhai, X., Kipf, T., & Houlsby, N. (2022). Simple open-vocabulary object detection with vision transformers. In Computer Vision – ECCV 2022 (pp. 728–755). Springer. https://doi.org/10.1007/978-3-031-20080-9_42

Minott, D., Siddiqui, S., & Haddad, R. J. (2025). Benchmarking Edge AI Platforms: Performance Analysis of NVIDIA Jetson and Raspberry Pi 5 with Coral TPU. SoutheastCon 2025, 1384–1389. https://doi.org/10.1109/SoutheastCon56624.2025.10971592

MLCommons. (2024, marzo 27). New MLPerf Inference Benchmark Results Highlight The Rapid Growth of Generative AI Models. MLCommons. https://mlcommons.org/2024/03/mlperf-inference-v4/

MLCommons. (s. f.-a). Benchmark MLPerf Inference: Datacenter | MLCommons V3.1. MLCommons. Recuperado https://mlcommons.org/benchmarks/inference-datacenter/

MLCommons. (s. f.-b). MLPerf Inference: Edge. MLCommons. MLCommons Benchmarks. Recuperado https://mlcommons.org/benchmarks/inference-edge/

Nakagawa, K., Tsukada, M., Shima, K., & Esaki, H. (2021). WebRTC-based measurement tool for peer-to-peer applications and preliminary findings with real users. Asian Internet Engineering Conference, 1–8. https://doi.org/10.1145/3497777.3498544

Nath, N. D., Behzadan, A. H., y Paal, S. G. (2020). Deep learning for site safety: Real-time detection of personal protective equipment. Automation in Construction, 112, 103085. https://doi.org/10.1016/j.autcon.2020.103085

NVIDIA Corporation. (2022, marzo). NVIDIA A30 data sheet. https://www.nvidia.com/content/dam/en-zz/Solutions/data-center/products/a30-gpu/pdf/a30-datasheet.pdf

NVIDIA Corporation. (2026a). DeepStream on WSL. https://docs.nvidia.com/metropolis/deepstream/dev-guide/text/DS_on_WSL2.html

NVIDIA Corporation. (2026b). Installing TensorRT. https://docs.nvidia.com/deeplearning/tensorrt/latest/installing-tensorrt/installing.html

NVIDIA Corporation. (s. f.-a). Compare GeForce RTX laptops. https://www.nvidia.com/en-us/geforce/laptops/compare/

NVIDIA Corporation. (s. f.-b). NVIDIA Video Codec SDK. https://developer.nvidia.com/video-codec-sdk

NVIDIA. (2022). NVIDIA Jetson AGX Orin series technical brief. NVIDIA. https://www.nvidia.com/content/dam/en-zz/Solutions/gtcf21/jetson-orin/nvidia-jetson-agx-orin-technical-brief.pdf

NVIDIA. (2024). DeepStream SDK 8.0 for NVIDIA dGPU/X86 and Jetson—DeepStream documentation. https://docs.nvidia.com/metropolis/deepstream/dev-guide/text/DS_Release_notes.html

NVIDIA. (2025). Welcome to the DeepStream documentation (DeepStream SDK overview). NVIDIA. NVIDIA DeepStream SDK Developer Guide. https://docs.nvidia.com/metropolis/deepstream/dev-guide/text/DS_Overview.html

NVIDIA. (s. f.-a). Installing PyTorch for Jetson platform. NVIDIA. NVIDIA Deep Learning Frameworks Documentation. Recuperado https://docs.nvidia.com/deeplearning/frameworks/install-pytorch-jetson-platform/index.html

NVIDIA. (s. f.-b). Interprocess Communication—CUDA Programming Guide. Recuperado https://docs.nvidia.com/cuda/cuda-programming-guide/04-special-topics/inter-process-communication.html

NVIDIA. (s. f.-c). JetPack software stack for NVIDIA Jetson. NVIDIA. NVIDIA Developer. Recuperado https://developer.nvidia.com/embedded/jetpack

NVIDIA. (s. f.-d). NVDEC Video Decoder API Programming Guide. Recuperado https://docs.nvidia.com/video-technologies/video-codec-sdk/13.0/nvdec-video-decoder-api-prog-guide/index.html

NVIDIA. (s. f.-e). NVENC Application Note. Recuperado https://docs.nvidia.com/video-technologies/video-codec-sdk/13.0/nvenc-application-note/index.html

NVIDIA. (s. f.-f). Using FFmpeg with NVIDIA GPU Hardware Acceleration. Recuperado https://docs.nvidia.com/video-technologies/video-codec-sdk/13.0/ffmpeg-with-nvidia-gpu/index.html

om-ai-lab. (2024, March 11). OmDet. GitHub. https://github.com/om-ai-lab/OmDet

ONNX Runtime. (s. f.). CUDA Execution Provider. https://onnxruntime.ai/docs/execution-providers/CUDA-ExecutionProvider.html

ONVIF. (2019). ONVIF Profile S Specification (ONVIF Profile S). ONVIF. https://www.onvif.org/wp-content/uploads/2019/12/ONVIF_Profile_-S_Specification_v1-3.pdf

OpenFog Consortium. (2017). OpenFog Reference Architecture for Fog Computing. Industrial Internet Consortium. https://www.iiconsortium.org/pdf/OpenFog_Reference_Architecture_2_09_17.pdf

Organisation for Economic Co-operation and Development. (2019, mayo 1). OECD AI Principles overview. OECD. https://oecd.ai/en/ai-principles

OSSRS. (s. f.). Introduction (SRS documentation). OSSRS. SRS Documentation (v6). Recuperado el 9 de enero de 2026, de https://ossrs.net/lts/en-us/docs/v6/doc/introduction

Otgonbold, M.-E., Gochoo, M., Alnajjar, F. S., Ali, L., Tan, T.-H., Hsieh, J.-W., y Chen, P.-Y. (2022). SHEL5K: An extended dataset and benchmarking for safety helmet detection. Sensors, 22(6), 2315. https://doi.org/10.3390/s22062315

Pantos, R. (2025). HTTP Live Streaming 2nd Edition (Internet-Draft). Internet Engineering Task Force. https://datatracker.ietf.org/doc/draft-pantos-hls-rfc8216bis/18/

Parmar, H., & Thornburgh, M. (2012). Adobe’s Real Time Messaging Protocol. Adobe. https://ptacts.uspto.gov/ptacts/public-informations/petitions/1557060/download-documents?artifactId=CX29dwexemvGTAgu1npsGb4QtKzyjACHSNYXLhjJp5m1SpQS4AAf-3A

Pereira, R., Carvalho, G., Garrote, L., & Nunes, U. J. (2022). Sort and Deep-SORT Based Multi-Object Tracking for Mobile Robotics: Evaluation with New Data Association Metrics. Applied Sciences, 12(3), 1319. https://doi.org/10.3390/app12031319

Pham, H. V., Tran, T. G., Le, C. D., Le, A. D., & Vo, H. B. (2024). Benchmarking Jetson Edge Devices with an End-to-End Video-Based Anomaly Detection System. En K. Arai (Ed.), Advances in Information and Communication (Vol. 920, pp. 358–374). Springer Nature Switzerland. https://doi.org/10.1007/978-3-031-53963-3_25

Potluri, S., Wang, H., Bureddy, D., Singh, A. K., Rosales, C., & Panda, D. K. (2012). Optimizing MPI Communication on Multi-GPU Systems Using CUDA Inter-Process Communication. 2012 IEEE 26th International Parallel and Distributed Processing Symposium Workshops & PhD Forum, 1848–1857. https://doi.org/10.1109/IPDPSW.2012.228

Radford, A., Kim, J. W., Hallacy, C., Ramesh, A., Goh, G., Agarwal, S., Sastry, G., Askell, A., Mishkin, P., Clark, J., Krueger, G., & Sutskever, I. (2021). Learning Transferable Visual Models From Natural Language Supervision (arXiv:2103.00020). arXiv. https://doi.org/10.48550/arXiv.2103.00020

Rakai, L., Song, H., Sun, S., Zhang, W., & Yang, Y. (2022). Data association in multiple object tracking: A survey of recent techniques. Expert Systems with Applications, 192, 116300. https://doi.org/10.1016/j.eswa.2021.116300

Rasaee, H., Koleilat, T., & Rivaz, H. (2025). Grounding DINO-US-SAM: Text-Prompted Multi-Organ Segmentation in Ultrasound with LoRA-Tuned Vision-Language Models. IEEE Transactions on Ultrasonics, Ferroelectrics, and Frequency Control, 72(10), 1414-1425. https://doi.org/10.1109/TUFFC.2025.3605285

Ravi, N., Gabeur, V., Hu, Y.-T., Hu, R., Ryali, C., Ma, T., Khedr, H., Rädle, R., Rolland, C., Gustafson, L., Mintun, E., Pan, J., Alwala, K. V., Carion, N., Wu, C.-Y., Girshick, R., Dollár, P., & Feichtenhofer, C. (2024). SAM 2: Segment Anything in Images and Videos (arXiv:2408.00714). arXiv. https://doi.org/10.48550/arXiv.2408.00714

Reddi, V. J., Cheng, C., Kanter, D., Mattson, P., Schmuelling, G., Wu, C.-J., Anderson, B., Breughe, M., Charlebois, M., Chou, W., Chukka, R., Coleman, C., Davis, S., Deng, P., Diamos, G., Duke, J., Fick, D., Gardner, J. S., Hubara, I., … Zhou, Y. (2020). MLPerf Inference Benchmark (arXiv:1911.02549). arXiv. https://doi.org/10.48550/arXiv.1911.02549

Ren, T., Chen, Y., Jiang, Q., Zeng, Z., Xiong, Y., Liu, W., Ma, Z., Shen, J., Gao, Y., Jiang, X., Chen, X., Song, Z., Zhang, Y., Huang, H., Gao, H., Liu, S., Zhang, H., Li, F., Yu, K., & Zhang, L. (2024, November 21). [2411.14347] DINO-X: A Unified Vision Model for Open-World Object Detection and Understanding. arXiv. Retrieved January 21, 2026, from https://arxiv.org/abs/2411.14347

Ren, T., Jiang, Q., Liu, S., Zeng, Z., Liu, W., Gao, H., Huang, H., Ma, Z., Jiang, X., Chen, Y., Xiong, Y., Zhang, H., Li, F., Tang, P., Yu, K., & Zhang, L. (2024). Grounding DINO 1.5: Advance the “Edge” of Open-Set Object Detection (Versión 2). arXiv. https://doi.org/10.48550/ARXIV.2405.10300

Ren, T., Liu, S., Zeng, A., Lin, J., Li, K., Cao, H., Chen, J., Huang, X., Chen, Y., Yan, F., Zeng, Z., Zhang, H., Li, F., Yang, J., Li, H., Jiang, Q., & Zhang, L. (2024). Grounded SAM: Assembling Open-World Models for Diverse Visual Tasks (arXiv:2401.14159). arXiv. https://doi.org/10.48550/arXiv.2401.14159

Ristani, E., Solera, F., Zou, R., Cucchiara, R., & Tomasi, C. (2016). Performance Measures and a Data Set for Multi-target, Multi-camera Tracking. En G. Hua & H. Jégou (Eds.), Computer Vision – ECCV 2016 Workshops (Vol. 9914, pp. 17–35). Springer International Publishing. https://doi.org/10.1007/978-3-319-48881-3_2

Robicheaux, P., Gallagher, J., Nelson, J., & Robinson, I. (2025, March 20). RF-DETR: A SOTA Real-Time Object Detection Model. Roboflow Blog. Retrieved January 26, 2026, from https://blog.roboflow.com/rf-detr/

Roboflow. (2023). Autodistill [Software]. GitHub. https://github.com/autodistill/autodistill

Roboflow. (2025, November 14). Build a Rapid Model | Roboflow Docs. Roboflow Documentation. Retrieved January 26, 2026, from https://docs.roboflow.com/rapid/build-a-rapid-model

Roboflow. (2025, November 14). What is Roboflow Rapid? Roboflow Docs. https://docs.roboflow.com/rapid/what-is-roboflow-rapid

Roy (Whalen), S. (2024, julio 18). RTMP vs. RTSP: Which Protocol Should You Choose? (Update). Wowza Media Systems. Wowza Blog. https://www.wowza.com/blog/rtmp-vs-rtsp-which-protocol-should-you-choose

Satyanarayanan, M. (2017). The Emergence of Edge Computing. Computer, 50(1), 30–39. https://doi.org/10.1109/MC.2017.9

Schulzrinne, H., Casner, S., Frederick, R., & Jacobson, V. (2003). RTP: A Transport Protocol for Real-Time Applications (No. RFC3550; p. RFC3550). RFC Editor. https://doi.org/10.17487/rfc3550

Schulzrinne, H., Rao, A., & Lanphier, R. (1998). Real Time Streaming Protocol (RTSP) (No. RFC2326; p. RFC2326). RFC Editor. https://doi.org/10.17487/rfc2326

Schulzrinne, H., Rao, A., Lanphier, R., & Westerlund, M. (2016). Real-Time Streaming Protocol Version 2.0 (M. Stiemerling, Ed.; No. RFC7826; p. RFC7826). RFC Editor. https://doi.org/10.17487/RFC7826

Sharabayko, M. (2022, marzo 14). Improving SRT Retransmissions—Experiments with Simulated Live Streaming. Innovation Labs Blog (Medium). https://medium.com/innovation-labs-blog/improving-srt-retransmissions-experiments-with-simulated-live-streaming-part-1-7d192483bba4

Sharabayko, M. P., Sharabayko, M. A., Dube, J., Kim, J., & Kim, J. (2024). The SRT Protocol (Internet-Draft (working copy)). Internet Engineering Task Force. https://haivision.github.io/srt-rfc/draft-sharabayko-srt.html

Sharma, P., Ding, N., Goodman, S., & Soricut, R. (2018). Conceptual captions: A cleaned, hypernymed, image alt-text dataset for automatic image captioning. In Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (pp. 2556–2565). https://doi.org/10.18653/v1/P18-1238

Shen, Y., Fu, C., Chen, P., Zhang, M., Li, K., Sun, X., Wu, Y., Lin, S., & Ji, R. (2023, December 4). Aligning and Prompting Everything All at Once for Universal Visual Perception. arXiv. https://arxiv.org/abs/2312.02153

Shi, W., Cao, J., Zhang, Q., Li, Y., & Xu, L. (2016). Edge Computing: Vision and Challenges. IEEE Internet of Things Journal, 3(5), 637–646. https://doi.org/10.1109/JIOT.2016.2579198

Shim, I., Oh, T.-H., Lee, J.-Y., Choi, J., Choi, D.-G., & Kweon, I. S. (2019). Gradient-Based Camera Exposure Control for Outdoor Mobile Platforms. IEEE Transactions on Circuits and Systems for Video Technology, 29(6), 1569–1583. https://doi.org/10.1109/TCSVT.2018.2846292

Shuvo, Md. M. H., Islam, S. K., Cheng, J., & Morshed, B. I. (2023). Efficient Acceleration of Deep Learning Inference on Resource-Constrained Edge Devices: A Review. Proceedings of the IEEE, 111(1), 42–91. https://doi.org/10.1109/JPROC.2022.3226481

Silvano, C., Ielmini, D., Ferrandi, F., Fiorin, L., Curzel, S., Benini, L., Conti, F., Garofalo, A., Zambelli, C., Calore, E., Schifano, S., Palesi, M., Ascia, G., Patti, D., Petra, N., De Caro, D., Lavagno, L., Urso, T., Cardellini, V., … Perri, S. (2025). A Survey on Deep Learning Hardware Accelerators for Heterogeneous HPC Platforms. ACM Computing Surveys, 57(11), 1–39. https://doi.org/10.1145/3729215

Sonono, T. (2019). Interoperable Retransmission Protocols with Low Latency and Constrained Delay: A Performance Evaluation of RIST and SRT [Master’s thesis, KTH Royal Institute of Technology]. https://www.diva-portal.org/smash/get/diva2:1335907/FULLTEXT01.pdf

SRT. (1997, julio 7). Resolución SRT 51/97 de 1997. Mecanismo Preventivo de Control en Obras de Construcción. Infoleg. https://servicios.infoleg.gob.ar/infolegInternet/anexos/40000-44999/44588/norma.htm

SRT. (1998, marzo 31). Resolución SRT 35/98 de 1998. Coordinación de Programas de Seguridad en Obras de Construcción. Infoleg. https://servicios.infoleg.gob.ar/infolegInternet/anexos/50000-54999/50188/norma.htm

SRT. (s. f.). Programa de Construcción. Argentina.gob.ar. Recuperado el 12 de enero de 2026, de https://www.argentina.gob.ar/srt/prevencion/programas/construccion

Stephen. (2026). elFarto/nvidia-vaapi-driver [C]. https://github.com/elFarto/nvidia-vaapi-driver (Obra original publicada en 2021)

Sullivan, G. J., Ohm, J.-R., Han, W.-J., & Wiegand, T. (2012). Overview of the High Efficiency Video Coding (HEVC) Standard. IEEE Transactions on Circuits and Systems for Video Technology, 22(12), 1649–1668. https://doi.org/10.1109/TCSVT.2012.2221191

Swaminathan, T. P., Silver, C., & Akilan, T. (2024). Benchmarking Deep Learning Models on NVIDIA Jetson Nano for Real-Time Systems: An Empirical Investigation (Versión 1). arXiv. https://doi.org/10.48550/ARXIV.2406.17749

SysCV. (2023, June 18). ovtrack. GitHub. https://github.com/SysCV/ovtrack

The FFmpeg developers. (s. f.-a). Documentación FFmpeg. Recuperado https://ffmpeg.org/about.html

The FFmpeg developers. (s. f.-b). FFmpeg Protocols Documentation. Recuperado https://ffmpeg.org/ffmpeg-protocols.html

The FFmpeg developers. (s. f.-c). HWAccelIntro – FFmpeg. Recuperado el 12 de febrero de 2026, de https://trac.ffmpeg.org/wiki/HWAccelIntro

The Linux Kernel. (s. f.). Buffer Sharing and Synchronization (dma-buf)—The Linux Kernel documentation. Recuperado https://docs.kernel.org/driver-api/dma-buf.html

THU-MIG. (2025). THU-MIG / yoloe: YOLOE: Real-Time Seeing Anything. GitHub. https://github.com/THU-MIG/yoloe

Twitch Developers. (s. f.). Video Broadcast. Twitch Developers. Recuperado el 11 de febrero de 2026, de https://dev.twitch.tv/docs/video-broadcast/

Ucar, A., Ro, S., Satwika, S., Gayathri, P. Y., & Balsha, M. G. (2025). Fine-Tuning Florence2 for Enhanced Object Detection in Un-constructed Environments: Vision-Language Model Approach (arXiv:2503.04918). arXiv. https://doi.org/10.48550/arXiv.2503.04918

United Nations Educational, Scientific and Cultural Organization. (2021, noviembre 1). Recommendation on the Ethics of Artificial Intelligence. UNESCO. https://unesdoc.unesco.org/ark:/48223/pf0000380455

Video Services Forum. (2020). Reliable Internet Stream Transport (RIST) protocol specification – Simple profile. Video Services Forum. https://static.vsf.tv/download/technical_recommendations/VSF_TR-06-1_2020_06_25.pdf

Video Services Forum. (2024). Reliable Internet Stream Transport (RIST) Protocol Specification – Main Profile. Video Services Forum. https://static.vsf.tv/download/technical_recommendations/VSF_TR-06-2_2024_06_12.pdf

Viitanen, M., Vanne, J., Hamalainen, T. D., Gabbouj, M., & Lainema, J. (2012). Complexity analysis of next-generation HEVC decoder. 2012 IEEE International Symposium on Circuits and Systems, 882–885. https://doi.org/10.1109/ISCAS.2012.6272182

Wang, A., Liu, L., Chen, H., Lin, Z., Han, J., & Ding, G. (2025). YOLOE: Real-Time Seeing Anything (arXiv:2503.07465). arXiv. https://doi.org/10.48550/arXiv.2503.07465

Wang, H., Hao, F., Zhu, C., Rodrigues, J. J. P. C., & Yang, L. T. (2012). An Android Multimedia Framework Based on Gstreamer. En J. J. P. C. Rodrigues, L. Zhou, M. Chen, & A. Kailas (Eds.), Green Communications and Networking (Vol. 51, pp. 51–62). Springer Berlin Heidelberg. https://doi.org/10.1007/978-3-642-33368-2_5

Wang, H., Ren, P., Jie, Z., Dong, X., Feng, C., Qian, Y., Ma, L., Jiang, D., Wang, Y., Lan, X., & Liang, X. (2024, July 10). OV-DINO: Unified Open-Vocabulary Detection with Language-Aware Selective Fusion. arXiv. https://arxiv.org/abs/2407.07844

Wang, H., Zhang, X., Chen, H., Xu, Y., & Ma, Z. (2022). Inferring End-to-End Latency in Live Videos. IEEE Transactions on Broadcasting, 68(2), 517–529. https://doi.org/10.1109/TBC.2021.3071060

Wang, X., Han, Y., Leung, V. C. M., Niyato, D., Yan, X., & Chen, X. (2020). Convergence of Edge Computing and Deep Learning: A Comprehensive Survey. IEEE Communications Surveys & Tutorials, 22(2), 869–904. https://doi.org/10.1109/COMST.2020.2970550

Wang, Z., Wu, Y., Yang, L., Thirunavukarasu, A., Evison, C., y Zhao, Y. (2021). Fast personal protective equipment detection for real construction sites using deep learning approaches. Sensors, 21(10), 3478. https://doi.org/10.3390/s21103478

Wiegand, T., Sullivan, G. J., Bjontegaard, G., & Luthra, A. (2003). Overview of the H.264/AVC video coding standard. IEEE Transactions on Circuits and Systems for Video Technology, 13(7), 560–576. https://doi.org/10.1109/TCSVT.2003.815165

Wojke, N., Bewley, A., & Paulus, D. (2017). Simple online and realtime tracking with a deep association metric. 2017 IEEE International Conference on Image Processing (ICIP), 3645–3649. https://doi.org/10.1109/ICIP.2017.8296962

World Wide Web Consortium. (2025). WebRTC: Real-Time Communication in Browsers (W3C Recommendation). World Wide Web Consortium. https://www.w3.org/TR/webrtc/

Xiao, B., Wu, H., Xu, W., Dai, X., Hu, H., Lu, Y., Zeng, M., Liu, C., & Yuan, L. (2024). Florence-2: Advancing a unified representation for a variety of vision tasks. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 4818–4829). https://doi.org/10.1109/CVPR52733.2024.00461

Yao, L., Han, J., Liang, X., Xu, D., Zhang, W., Li, Z., & Xu, H. (2023, April 10). [2304.04514] DetCLIPv2: Scalable Open-Vocabulary Object Detection Pre-training via Word-Region Alignment. arXiv. Retrieved January 29, 2026, from https://arxiv.org/abs/2304.04514

Yao, L., Han, J., Wen, Y., Liang, X., Xu, D., Zhang, W., Li, Z., Xu, C., & Xu, H. (2022, September 20). [2209.09407] DetCLIP: Dictionary-Enriched Visual-Concept Paralleled Pre-training for Open-world Detection. arXiv. Retrieved January 29, 2026, from https://arxiv.org/abs/2209.09407

Yao, L., Pi, R., Han, J., Liang, X., Xu, H., Zhang, W., Li, Z., & Xu, D. (2024, April 14). [2404.09216] DetCLIPv3: Towards Versatile Generative Open-vocabulary Object Detection. arXiv. https://arxiv.org/abs/2404.09216

Yao, Y., Liu, P., Zhao, T., Zhang, Q., Liao, J., Fang, C., Lee, K., & Wang, Q. (2024). How to evaluate the generalization of detection? A benchmark for comprehensive open-vocabulary detection. Proceedings of the AAAI Conference on Artificial Intelligence, 38(7), 6630-6638. https://doi.org/10.1609/aaai.v38i7.28485

Yousefpour, A., Fung, C., Nguyen, T., Kadiyala, K., Jalali, F., Niakanlahiji, A., Kong, J., & Jue, J. P. (2019). All one needs to know about fog computing and related edge computing paradigms: A complete survey. Journal of Systems Architecture, 98, 289–330. https://doi.org/10.1016/j.sysarc.2019.02.009

Žádník, J., Mäkitalo, M., Vanne, J., & Jääskeläinen, P. (2022). Image and Video Coding Techniques for Ultra-low Latency. ACM Computing Surveys, 54(11s), 1–35. https://doi.org/10.1145/3512342

Zang, Y., Li, W., Zhou, K., Huang, C., & Loy, C. C. (2022, March 22). [2203.11876] Open-Vocabulary DETR with Conditional Matching. arXiv. https://arxiv.org/abs/2203.11876

Zareian, A., Rosa, K. D., Hu, D. H., & Chang, S.-F. (2021). Open-Vocabulary Object Detection Using Captions (arXiv:2011.10678). arXiv. https://doi.org/10.48550/arXiv.2011.10678

Zhang, H., Ananthanarayanan, G., Bodik, P., Philipose, M., Bahl, P., & Freedman, M. J. (2017). Live Video Analytics at Scale with Approximation and Delay-Tolerance. 377–389. https://www.usenix.org/system/files/conference/nsdi17/nsdi17-zhang.pdf

Zhang, H., Zhang, P., Hu, X., Chen, Y.-C., Li, L. H., Dai, X., Wang, L., Yuan, L., Hwang, J.-N., & Gao, J. (2022). GLIPv2: Unifying Localization and Vision-Language Understanding (arXiv:2206.05836). arXiv. https://doi.org/10.48550/arXiv.2206.05836

Zhang, Y., Sun, P., Jiang, Y., Yu, D., Weng, F., Yuan, Z., Luo, P., Liu, W., & Wang, X. (2022). ByteTrack: Multi-object Tracking by Associating Every Detection Box. En S. Avidan, G. Brostow, M. Cissé, G. M. Farinella, & T. Hassner (Eds.), Computer Vision – ECCV 2022 (Vol. 13682, pp. 1–21). Springer Nature Switzerland. https://doi.org/10.1007/978-3-031-20047-2_1

Zhao, T., Liu, P., He, X., Zhang, L., & Lee, K. (2024). Real-time Transformer-based Open-Vocabulary Detection with Efficient Fusion Head (arXiv:2403.06892). arXiv. https://doi.org/10.48550/arXiv.2403.06892

Zhao, X., Chen, Y., Xu, S., Li, X., Wang, X., Li, Y., & Huang, H. (2024). An Open and Comprehensive Pipeline for Unified Object Grounding and Detection (arXiv:2401.02361). arXiv. https://doi.org/10.48550/arXiv.2401.02361

Zhou, K., Yang, J., Loy, C. C., & Liu, Z. (2022a). Conditional Prompt Learning for Vision-Language Models. IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2022). https://www.computer.org/csdl/proceedings-article/cvpr/2022/694600q6795/1H0OnmbArsY

Zhou, K., Yang, J., Loy, C. C., & Liu, Z. (2022b). Learning to Prompt for Vision-Language Models. International Journal of Computer Vision, 130(9), 2337–2348. https://doi.org/10.1007/s11263-022-01653-1

Zhou, Z., Chen, X., Li, E., Zeng, L., Luo, K., & Zhang, J. (2019). Edge Intelligence: Paving the Last Mile of Artificial Intelligence With Edge Computing. Proceedings of the IEEE, 107(8), 1738–1762. https://doi.org/10.1109/JPROC.2019.2918951

Zhu, X., Su, W., Lu, L., Li, B., Wang, X., & Dai, J. (2020, October 8). [2010.04159] Deformable DETR: Deformable Transformers for End-to-End Object Detection. arXiv. Retrieved January 29, 2026, from https://arxiv.org/abs/2010.04159

Zou, X., Dou, Z.-Y., Yang, J., Gan, Z., Li, L., Li, C., Dai, X., Behl, H., Wang, J., Yuan, L., Peng, N., Wang, L., Lee, Y. J., & Gao, J. (2023). Generalized Decoding for Pixel, Image, and Language (arXiv:2212.11270). arXiv. https://arxiv.org/abs/2212.11270

Zou, Z., Chen, K., Shi, Z., Guo, Y., & Ye, J. (2023). Object Detection in 20 Years: A Survey. Proceedings of the IEEE, 111(3), 257–276. https://doi.org/10.1109/JPROC.2023.3238524

---

## Fuente: `docs/informe/ajustes/06-etapa-6-documentacion-y-cierre.md`

> SHA-256 del bloque: `a272f5aa52f28944bb818ac7f91c9b4836d16c0d140e8d8fcdf1de906e08c2cb`  
> Seleccion: documento completo.

# Etapa 6 — §17.6, §18 Cierre y §19 Anexos

> *Gantt ID 5 — "Documentación y defensa", 17/07/26 – 21/08/26.*
>
> **Estado (2026-08-10):** es la etapa del cierre documental. En el informe está repartida
> en tres lugares, con estados distintos:
>
> | Sección | Qué es | Estado |
> |---|---|---|
> | **§17.6** Documentación técnica, repositorio y evidencias de cierre | los repos y dónde vive cada evidencia | `[Agregado futuro correspondiente a la Etapa 6]` — **vacía** |
> | **§18** Cierre del Proyecto | **las conclusiones propiamente** | existe, pero se escribió **antes** de tener resultados |
> | **§19** Anexos A–D | reproducibilidad, licencias, métricas, infraestructura | existen; se completan |
>
> **Se escribe después del §17.5 y con el mismo material.** La división es: el §17.5
> reporta *qué se midió y cuánto dio*; el §18 dice *qué significa*, con qué fuerza, y qué
> queda afuera. Los insumos ya están armados en `gobierno/99` y en
> `sintesis/resultados-y-conclusiones.md`.

| Dónde | Qué |
|---|---|
| Texto actual | `entregable/96e` — §17.6 vacía · §18 y §19 escritos pre-resultados |
| Materiales de cierre | `gobierno/99` §2 (reproducibilidad), §3 (licencias y citas), §4 (limitaciones y ADRs) |
| Las conclusiones y su fuerza | `sintesis/resultados-y-conclusiones.md` §1–§2, §8 (escala **AF-1…AF-11**), §11 |
| Alcance y exclusiones | `nucleo/10` + `decisiones/adr-015-cierre-de-alcance.md` |

---

## 1. Tablero de contenidos a escribir

| ID | Sección | Tipo | Pri | Qué tiene que decir |
|---|---|---|---|---|
| **AJ-6.01** | §18 | EVIDENCIA | 🟠 | **Las conclusiones propiamente**, cada una con su fuerza declarada. |
| **AJ-6.02** | §19 | CONCRETA | 🟠 | El **anexo de reproducibilidad** — lo que hace auditable todo el capítulo. |
| **AJ-6.03** | §19 | EVIDENCIA | 🟠 | **Licencias, consentimientos y citas obligatorias.** |
| **AJ-6.04** | §17.6 | CONCRETA | 🟡 | **Repositorio y evidencias de cierre.** |
| **AJ-6.05** | §18 | CONCRETA | 🟡 | El **trabajo futuro**, que sale de las exclusiones ejercidas. |

---

## 2. Los contenidos, desarrollados

### AJ-6.01 · §18 Cierre del Proyecto · EVIDENCIA · 🟠 — las conclusiones propiamente

**El §18 existe pero fue escrito antes de tener resultados.** Hay que reescribirlo contra
lo medido, y hay una forma correcta de hacerlo:

- **Cada conclusión con su fuerza declarada**, usando la escala `AF-1…AF-11`
  (`sintesis/resultados-y-conclusiones.md` §8). Aplanar todo a "se logró" es más débil, no
  más fuerte: la regla aplicada fue **degradar la afirmación cuando el intervalo de
  confianza no excluía el cero**, y eso se sostiene mejor ante un jurado que una lista de
  éxitos.
- **En tres tiempos** (`AJ-5.11`, y viene de `AJ-1.15`): *qué dice la literatura* → *qué
  medimos nosotros* → *qué tipo de aporte queda*. Nunca al revés.
- **Las refutaciones son conclusiones.** E-DIR vetada por precisión con criterio
  pre-registrado, y E-HYB-or ejecutada y refutada, no son fracasos: son resultados.
- **Sin capacidades nuevas** fuera de las dos comprometidas por ADR firmado (016:
  distribución; 017: jornada de fine-tuning): el §18 no puede prometer ni insinuar
  nada más que no esté medido.
- **La precisión sobre "adaptación"**: el núcleo medido **no adapta los pesos** — se
  adaptó **operativamente** (resolución 560, prompt sets congelados, las capas de
  plataforma). Medir cuánto rinde ese stack sin entrenar **es** la contribución. La
  rama de fine-tuning (E-04) es una **jornada comprometida aparte** (ADR-017): sus
  resultados, si existen a la entrega, se rotulan como rama comparativa — nunca se
  mezclan con el núcleo zero-shot.

La narrativa de la que sale este texto: `sintesis/resultados-y-conclusiones.md` §1 (la
pregunta y la respuesta en una línea), §2 (el recorrido del argumento) y §11 (qué queda, y
qué **no** cambia).

---

### AJ-6.02 · §19 · CONCRETA · 🟠 — el anexo de reproducibilidad

Está armado en `gobierno/99` §2, y es **lo que convierte el capítulo de resultados en algo
auditable por un tercero**:

- **Huellas sha256** de los artefactos congelados (banco de clips con su freeze, `bench_v3`
  con su manifiesto por fuente).
- **Cadena de comandos por material**: reconstruir el banco, evaluar una corrida contra el
  bench, disparar una corrida — con la advertencia del export de CVAT a nivel PROYECTO vs
  TASK, que decide el primer paso.
- **Trazabilidad corrida → resultado**, y **los dos verificadores mecánicos**.

El §17.5 tiene que citarlo (es `AJ-5.02`: toda tabla lleva su `campaign_id` o el sha256 del
banco al pie).

---

### AJ-6.03 · §19 · EVIDENCIA · 🟠 — licencias, consentimientos y citas

Armado en `gobierno/99` §3, con dos reglas **no negociables**:

- **El lote de internet es *Standard YouTube License*.** Se cita el canal público como
  fuente y **nunca** se presenta como CC. *(Único residuo abierto del cierre: anotar URL +
  fecha de acceso por video en los 18 `clip.yaml` — `operacion/113` §C1.)*
- **El consentimiento del rodaje**: en los 34 clips del Bloque A aparecen los propios
  integrantes del proyecto, actuando según guion y sin terceros en cuadro; sujetos y
  responsables son los mismos. **La identificación del responsable va en el informe.**

Además: licencia por dataset —con la **limitación L7**, licencia parcial de `chv`— y los
**pesos de modelo**: Grounding DINO Apache-2.0, YOLOE AGPL-3.0, registrados en
`license_registry.md` §PESOS DE MODELO.

---

### AJ-6.04 · §17.6 · CONCRETA · 🟡 — repositorio y evidencias de cierre

Sección vacía. Qué tiene que decir:

- **Los cuatro repos del proyecto** y qué contiene cada uno, con sus ramas de trabajo — más
  el quinto, `e-ovrt_alert-distribution`: hoy un esqueleto sin implementación, ✎ 2026-08-10
  con estatuto de **trabajo comprometido** (ADR-016). Se reporta **con su estado real al
  momento de la entrega**, sea el que sea.
  ✎ **2026-08-18: ese estado real ya se conoce** — el módulo está **implementado, medido y
  verificado**, y es un **servicio HTTP** más de la plataforma (`:8082`), igual que los
  otros dos (docs `operacion/114`/`118`/`124`/`125`). Se escribe en presente.
- ✎ **2026-08-18 — LA CONTAINERIZACIÓN SÍ VA EN ESTA SECCIÓN, y así se escribe.** Es
  **trabajo comprometido para después de la entrega del informe**, cuya razón de ser es la
  **reproducibilidad de la plataforma** (que un tercero pueda levantarla en otra máquina),
  no cerrar el capítulo. Qué decir: que los tres servicios son config-driven y aptos para
  empaquetarse; que el empaquetado está **planificado y pendiente**, con su causa
  —diferido a conciencia, no por falta de tiempo—; y que **su documentación operativa vive
  en los repositorios** (`infra/`, READMEs), no en el informe, porque la tesis no es un
  manual de despliegue. **Cómo NO escribirlo:** en presente, ni como capacidad existente,
  ni con instrucciones de despliegue. La frase que gobierna: *describir el compromiso y su
  fundamento es correcto; describir un despliegue que no corrió es falso.*
- **Que `docs/` es un repo git propio**, con remote desde el 2026-08-10 (`e-ovrt_docs`,
  rama `main`) para el acceso del equipo, y que además se respalda con copia a otro disco.
  *(✎ 2026-08-18: decía "local sin remote" — esa era la decisión inicial del 2026-07-09,
  superada al sumar redactores externos.)*
- **Dónde vive cada evidencia**: `results/` (los índices y sus artefactos),
  `datasets/processed/clip_bench/` (el banco, con su freeze y sha256),
  `docs/operacion/datos/` (la evidencia cruda por campaña).
- **Los dos verificadores mecánicos** y qué cubre cada uno
  (`96-verificar-indices.py` para las cifras de los índices,
  `109-verificar-organizacion.py` para la organización del material).

---

### AJ-6.05 · §18 · CONCRETA · 🟡 — el trabajo futuro sale de las exclusiones

No hay que inventarlo: **el trabajo futuro son las exclusiones ejercidas, con su costo ya
medido**, y eso es mucho más sólido que una lista de deseos.

- **El fine-tuning dejó de ser trabajo futuro** ✎ 2026-08-11: **ADR-017 lo puso en
  alcance como jornada experimental comprometida** — escalera T1→T2/T3 con go/no-go
  y Mendieta disponible. ✎ **2026-08-13:** F-100.1, freeze/smoke técnico, dual gate y serving
  real y T-FT-023 están cerrados; T1 full permanece en NO-GO por D-FT-08/T-FT-005,
  T-FT-031 y T-FT-032 (snapshot de procedencia `639e60df…`). ✎ **2026-08-15:
  D-FT-08/T-FT-005, D-FT-12 y D-FT-13 firmadas, y T-FT-031/032 cerradas la misma jornada**
  (doc 120: baseline 26s one-shot) — el NO-GO queda reducido a `full-authorization.json`
  + `RUN` manual del usuario.
  Si a la entrega la jornada produjo resultados, se reportan como
  rama comparativa con sus limitaciones; si quedó a medias, **lo pendiente se declara
  como estado con causa técnica, no como promesa** — y lo que sí sigue siendo trabajo
  futuro son los tiers que los go/no-go no habiliten (T2/T3 sin ganancia exigible
  previa). *Decía "no ejercido por secuenciación; la continuación más obvia"*.
- **La distribución de alertas dejó de ser trabajo futuro** ✎ 2026-08-10: ADR-016 la puso
  en alcance como **trabajo comprometido** antes de la defensa. Si a la entrega está
  implementada, se reporta en §17.4; si quedó incompleta, **lo pendiente se declara como
  estado, no como promesa** — y lo que sí sigue siendo trabajo futuro es **E-06** (el
  dashboard de consumo), que ADR-016 mantiene excluida.
- **FAR/hora**: requiere ~3 h de cumplimiento anotado (**limitación L1**). Es un requisito
  de dato, no de software.
- **Las celdas de la frontera de juzgabilidad** que quedaron sin cruzar, y la **validación
  sobre obra real** que la limitación L4 caracteriza pero explícitamente **no** cierra.
- **Métricas MOT** (E-10) — recordando el matiz de R-21: lo excluido son las métricas, no
  el tracker.

---

## 3. 🚫 Lo que no hay que escribir en esta etapa

| # | No escribir | Por qué |
|---|---|---|
| 1 | Conclusiones sin su nivel de fuerza | La escala `AF` existe justamente para eso; aplanarla debilita el capítulo. |
| 2 | Capacidades o promesas nuevas | ADR-015 cerró el alcance hasta la defensa. |
| 3 | "Adaptamos los modelos" a secas | La adaptación del núcleo es **operativa**, sin tocar pesos. La rama de fine-tuning es una jornada aparte (ADR-017): si tiene resultados se rotulan como rama comparativa, nunca se funden con el núcleo. |
| 4 | El lote de internet como material CC | Es *Standard YouTube License*. |
| 5 | ~~El módulo de distribución como funcionando~~ ⛔ **✎ 2026-08-18: esta prohibición quedó INVERTIDA** | Ya hay código verificado y medido: el módulo **funciona, está integrado y es un servicio HTTP** (`:8082`). **Se escribe en presente.** Lo que sí sigue prohibido: fundir sus cifras con las del núcleo, y presentar la **containerización** como hecha. |
| 7 | ✎ **La containerización en presente, o como instructivo** | Es trabajo comprometido **posterior** a la entrega del informe, para **reproducibilidad**. Se **puede y conviene** mencionarla como compromiso declarado con su causa (§17.6/§18/§19), pero su documentación operativa vive en los repositorios, no acá: el informe no es un manual de despliegue. |
| 6 | "L4 se levantó" | Se **precisó** (D-113.1). |

## 4. Fuentes

`gobierno/99` §2–§4 · `sintesis/resultados-y-conclusiones.md` §1, §2, §8, §9, §11 ·
`nucleo/10-registro-alcance-y-exclusiones.md` · `nucleo/19` (ciclo de vida de la alerta) ·
`decisiones/adr-005`, `adr-015`, `adr-016`, `adr-017` ·
`operacion/100` §6 (costo del fine-tuning), `operacion/113` §C1 (el residuo de licencias) ·
`e-ovrt_datasets/datasets/registry/license_registry.md`.

---

## Fuente: `docs/informe/ajustes/07-critica-extension-y-poda.md`

> SHA-256 del bloque: `44cc87962e89066323feb695800b7b2c3c61a1fa07ff69bb42b3e58abafc900a`  
> Seleccion: podas 17 y 18, tablero y guardrails aplicables al cierre.

## 7. §18, §19 y Referencias (12.339 palabras)

### PODA-17 · §19.1 Anexo A — comparativas técnicas (749) · C3 · 🟡
Con la vara supervisada dentro del §15 (AJ-1.01/1.13), el anexo de "estado del arte
complementario" pierde su función. Rescatar lo vivo (la Tabla A.1 con las licencias
**corregidas** — AJ-1.09) hacia §15 o Anexo B, y eliminar el resto. **Ahorro: ~500** ·
DECISIÓN → [ ]

### PODA-18 · Referencias (5.886) · consecuencia · 🟡
Se poda sola al caer las secciones (los ~25 modelos, los protocolos, los servidores de
medios arrastran decenas de entradas), y el pase de AJ-1.10 unifica duplicados
(Liu 2023/2024, Lin 2014/2015, Ren a/b/c). **Ahorro estimado: ~800** · DECISIÓN → [ ]

**Anexos B/C/D: no se podan** — son el destino natural de lo que sale del cuerpo
(PODA-14) y del anexo de reproducibilidad (`AJ-6.02`).

---

## 8. Tablero de poda

| ID | Sección | Hoy | Acción | Ahorro | Pri |
|---|---|---:|---|---:|---|
| PODA-01 | §15.2.1 catálogo de modelos | 4.530 | comprimir a modelos con rol | ~2.000 | 🟠 |
| PODA-02 | §15.2.3+.4 síntesis duplicada | 3.917 | fusionar en una | ~1.500 | 🟠 |
| PODA-03 | §15.3 MOT | 2.484 | comprimir; eliminar métricas MOT | ~1.600 | 🟠 |
| PODA-04 | §15.4 streaming/servidores | 7.998 | **comprimir a decisión tomada** | **~6.800** | 🔴 |
| PODA-05 | §16.4 MOT teórico | 2.769 | mantener lo que motiva G1/histéresis | ~1.400 | 🟠 |
| PODA-06 | §16.5.2 pipeline | 4.874 | mantener solo definición de G2A | ~3.400 | 🔴 |
| PODA-07 | §16.5.3 arquitecturas de video | 3.594 | comprimir a patrón usado | ~3.000 | 🔴 |
| PODA-08 | §16.5.4 borde | 2.729 | comprimir a EN-2 + exclusión EN-3 | ~2.000 | 🔴 |
| PODA-09 | §16.5.5 criterios streaming | 1.686 | párrafo puente | ~1.400 | 🔴 |
| PODA-10 | §16.6 ético-legal | 4.364 | podar genérico, mantener lo implementado | ~1.400 | 🟠 |
| PODA-11 | §16.7 convergencias | 4.429 | **fusionar con 16.8, es meta-texto** | ~3.400 | 🔴 |
| PODA-12 | §17.1.6.2 catálogo datasets | 5.054 | comprimir a usados + descartes (con R-24) | ~3.000 | 🔴 |
| PODA-13 | §17.1.10 proyección | 637 | párrafo puente | ~450 | 🟡 |
| PODA-14 | §17.1.4 infra | 3.252 | detalle al Anexo B | ~1.000 | 🟡 |
| PODA-15 | §17.3.15 roles | 1.319 | con R-17: tabla, no prosa | ~700 | 🟡 |
| PODA-16 | §17.3.17 backlog | 1.101 | con R-21: estado final | ~500 | 🟡 |
| PODA-17 | §19.1 Anexo A | 749 | eliminar tras AJ-1.01/1.09 | ~500 | 🟡 |
| PODA-18 | Referencias | 5.886 | consecuencia + AJ-1.10 | ~800 | 🟡 |
| **Total** | | | | **~34.900 (~27%)** | |

**Resultado esperado (consecuencia, no meta):** de ~127k a **~92k escritas**; con
§17.4/§17.5/§17.6 sumadas (15–20k), el informe final queda en ~110k en lugar de ~145k.
✎ 2026-08-11 — **no hay objetivo numérico** (regla de gobierno del encabezado): estas
cifras miden el efecto de podar lo que no aporta, no un tope a alcanzar. No hay segunda
vuelta sobre §17.1.5/§17.1.7.

**Orden recomendado:** los ocho 🔴 primero (son el 65% del ahorro y tienen el riesgo
argumental más bajo: nada de lo que eliminan sostiene un resultado ni un argumento de
defensa). Los 🟠 en el pase de cada sección junto a sus AJ-. Los 🟡 al final.

---

## 9. Guardrails — lo que esta crítica NO autoriza a tocar

1. **§16.3** (visión-lenguaje) y **§16.2** (normativa→condiciones): el corazón
   conceptual y el ancla de CR-01/CR-02.
2. **§17.1.5 y §17.1.7**: el protocolo ejercido y el framework de métricas — son la
   columna vertebral metodológica que §17.5 va a citar.
3. **La latencia como restricción** (§16.5.1) y la definición de G2A: el eje de tiempo
   real es un resultado central, no un survey.
4. **Nada pre-registrado se borra en silencio**: fine-tuning, kappa, TN — se comprimen a
   decisión declarada con causa (regla `97` §3; los textos de declaración ya existen:
   `94` §8, AJ-2.06, AJ-2.11). (✎ 2026-08-11: el fine-tuning dejó de ser caso
   "no ejercido" — ADR-017 lo compromete como jornada; `94` §8 y AJ-2.11 ya están
   reescritos con ese encuadre.)
5. **Ningún texto que un redline necesita como ancla**: antes de eliminar un párrafo de
   §17.3, verificar que ningún R-xx lo cita como "DICE HOY".
6. **Las adiciones mandan sobre las podas**: AJ-1.01/1.02/1.13 (la vara y el cruce)
   *agregan* al §15 — la poda les hace lugar, no compite con ellas.

## 10. Fuentes

Conteos: medidos el 2026-08-11 sobre `entregable/90` y `96a`–`96e` (por encabezado,
`wc -w` por sección). Alineación: `nucleo/10` (exclusiones E-01…E-13) · ADR-002/003/015/016 ·
`nucleo/14`–`19` (los relevamientos vigentes) · `operacion/97` (la plataforma verificada) ·
`sintesis/resultados-y-conclusiones.md` §7 (lo que el §15 debe ganar) ·
`material-etapa-3/93` (los redlines con los que esta poda se coordina).

---

## Fuente: `docs/informe/ajustes/gobierno/99-materiales-de-cierre.md`

> SHA-256 del bloque: `24f181cbf0fc984010ece44806a85399040ce32da594b80f1c653c317f7152ef`  
> Seleccion: reproducibilidad, licencias, limitaciones y mecanismos.

## 2. Anexo de reproducibilidad

### 2.1 Huellas de los artefactos congelados (verificadas el 2026-08-05; ✎ re-verificadas el 2026-08-10 — cambió solo el manifest del banco de clips)

| Artefacto | sha256 | Verificación |
|---|---|---|
| `bench_v3.json` (banco de imágenes) | `4557024ecc4ee497…a4462` | `sha256sum` **coincide** con `bench_v3_manifest.json → bench_v3_sha256` |
| estrato `bench_obra_test` | `e82eed03469665a3…af61a` | coincide con `source_sha256` |
| estrato `bench_obra_val` | `b2326724b71e7776…4c58c` | coincide con `source_sha256` |
| estrato `chv` | `6d15ff9b46407511…39a7` | coincide con `source_sha256` |
| estrato `shel5k` | `bf35f63bcf726c1c…d1e0f` | coincide con `source_sha256` |
| `manifest.yaml` (banco de clips, **47 — vigente desde 2026-08-09**) | `3f14f50a53c0d6c57b429378544dcfb6ed87fc942640db302c53ba1470001a75` | `sha256sum` directo == `clip_bench_manifest.json`; freeze `clip_bench.sha256` **189/189 OK** (verificador 109) |
| `manifest.yaml` (freeze histórico del sub-banco del rodaje, 34) | `cef5082e1eb1981c…260e8` | commit `f7a27fe6` — es el freeze que citan T1/T2/D1/H1/G1/B1/R1–R6 |
| prompt set `cr01_cr02_v2_short` | `df81fd48b6daf892…b309a` | `frozen_sha256` en el YAML, acta doc 76 |
| prompt set `eind_v1` | `7a0126f45eb1362a…ed770` | idem |
| prompt set `edir_v1` | `a1278d0c34cd13be…43703` | idem |

> **Queda saldado un riesgo de la auditoría del doc 75**: decía que el sha256 de
> `bench_v3` **no era verificable con `sha256sum`**. Sí lo es — se verificó hoy, y los
> cuatro sha256 por estrato también. El manifest guarda exactamente el digest del
> archivo, sin canonicalización de por medio.

### 2.2 El verificador mecánico de cifras

```bash
cd docs && python3 operacion/datos/96-verificar-indices.py
```

✎ 2026-08-14 — **el alcance volvió a crecer** (docs 113 y 118). Corrido hoy:
**`✅ Todo verificado`** — **25 cifras** contra `metrics.json` (14 F1 de `clip_bench`,
5 de `bench_nivel_a` y 6 valores de `realtime/t_alert_notification`), **guard de
cobertura 17/17 campañas** (falla si aparece una campaña sin fila de verificación),
3 deltas de bootstrap con su IC, 1.447 enlaces y **35 docs de procedencia** (ninguno
faltante). *(Decía: 8 F1, 31 docs, "solo cubre T1, G1 y R1–R6" — ese hueco quedó
cerrado por el guard.)*

**Lo que sigue sin cubrir, y se chequea a mano:** `bench_imagenes/`; el descarte se
contrasta contra el doc 64. `realtime/t_alert_notification` ya tiene `metrics.json`,
prueba negativa obligatoria y cobertura mecánica.

**Segundo verificador** (✎ 08-10):
`python3 docs/operacion/datos/109-verificar-organizacion.py` — las 6 reglas de
organización del material de video: estratos en su lugar (34+13+4 retirados), campaña
citable vs evidencia exploratoria, anotaciones del repo como fuente de verdad
(correcciones firmadas con guard `--check`), integridad lab↔banco por sha256,
exclusiones firmadas (`v08_c01`), banco reportable con freeze 189/189.

### 2.3 Cadena de comandos por material

Los cuatro repos son hermanos en disco y las rutas relativas lo asumen.

**Banco de imágenes (`bench_v3`) y percepción**
```bash
# reconstruir el banco (idempotente, lee las 4 fuentes curadas)
python3 datasets/scripts/curate/build_bench_v3.py
# evaluar una corrida del media-plane contra el banco
cd e-ovrt_media-plane && .venv/bin/python -m eovrt_media.tools.evaluate \
    --run runs/<run_id> \
    --bench-coco ../e-ovrt_datasets/datasets/processed/coco/bench/curated/bench_v3.json
```

**Servicio del media-plane y disparo de una corrida**
```bash
cd e-ovrt_media-plane && EOVRT_MODEL_REF=grounding-dino/gdino-tiny-560 make serve  # :8080
curl -s localhost:8080/healthz localhost:8080/readyz          # = make smoke
# POST /api/runs con el run config (una corrida activa a la vez)
```

**Camino offline (DBE) y camino en vivo (EBE)**
```bash
cd e-ovrt_control-plane
.venv/bin/eovrt-control serve --port 8081                       # servicio
.venv/bin/eovrt-control replay   --config <cfg>                 # DBE: relee detections.jsonl
.venv/bin/eovrt-control live     --config <cfg>                 # EBE: consume el bus
.venv/bin/eovrt-control evaluate-alerts ...                     # 5 métricas contra GT temporal
```
> **EBE, orden no negociable:** primero `POST :8081/api/runs` con `mode: live` (su 201
> implica suscripción hecha), después `POST :8080/api/runs` con `bus.enabled: true`.
> PUB/SUB pierde todo lo publicado antes de la suscripción.

**Cadena de GT de video** (✎ 08-10: las anotaciones llegaron — docs 102–111 — y la
cadena quedó ejercitada de punta a punta sobre 13 clips)
```bash
# ¡verificar meta/task vs meta/project ANTES de decidir el primer paso! Un export a
# nivel PROYECTO exige el split (sin él el GT sale negativo EN SILENCIO); el lote llegó
# a nivel TASK y aplicárselo habría sido el error simétrico (doc 102).
python3 <video-gt-lab>/split_cvat_project.py ...
python3 <video-gt-lab>/derive_clip_gt.py ...
python3 <video-gt-lab>/validate_clip_gt.py ...
python3 <video-gt-lab>/promote_clip.py ...        # suma el clip al banco
python3 <video-gt-lab>/aggregate_clip_campaign.py ...   # métricas de campaña
# guard de correcciones firmadas (✎ 08-10): apply_attribute_corrections.py --check
# sale 1 si una corrección firmada del repo falta en el GT (doc 111)
```

**Piloto de clase nueva (A1)** — un solo archivo de config de 48 líneas, 0 entrenamientos;
procedencia de las 5 corridas en `operacion/datos/94-piloto-clase-nueva/resultados.json`.

### 2.4 Trazabilidad corrida→resultado

Cada campaña de `results/` trae su procedencia en disco, y es lo que hay que citar:

| Archivo | Qué garantiza |
|---|---|
| `campaign.yaml` | la definición de la campaña (modelo, prompt set, granularidad, pattern set) |
| `provenance.json` / `provenance_runs.json` | los `run_id` exactos del media-plane y del control-plane |
| `evals/eval_<clip>.json` | la evaluación por clip, uno por clip del banco |
| `metrics.json` | el agregado (`positives`, `negatives`, `by_condition`, `by_scenario`, `by_clip`) |

**Entorno:** media-plane Python 3.12 (`pip install -e ".[gpu,dev]"`), control-plane y BFF
Python 3.11, `datasets` sin paquete (scripts sueltos, requiere `Pillow`). Puertos 8080
(media) y 8081 (control). El JSONL es la verdad en los dos caminos: **toda corrida live
es re-evaluable offline y produce artefactos idénticos** (paridad verificada por mutación).

---

## 3. Licencias, consentimientos y citas obligatorias

### 3.1 Lo que efectivamente sostiene un resultado reportado

Solo estas fuentes aparecen en los números del capítulo. El resto del
`license_registry.md` (SH17, GDUT-HWD, SHWD, SODA, Pictor-PPE, Construction-PPE,
`construction_safety_hardhat`) **no se cita**: o quedó descartado o nunca entró.

| Fuente | Dónde entra | Licencia | Obligación en el informe |
|---|---|---|---|
| `construction_site_safety` (Roboflow) | estratos `bench_obra` (147 imgs) + split TRAIN | **CC BY 4.0** | atribución |
| `chv` (GitHub `ZijianWang-ZW/PPE_detection`) | estrato `chv`, **1.330 imgs = 20,5% de `bench_v3`** | **sin licencia formal** (SPDX: none); grant informal de los autores: *"open for free use"* | **cita obligatoria `wang2021ppe`** + declarar *"dataset académico de terceros usado para evaluación bajo el grant de uso libre de sus autores, con cita; imágenes no redistribuidas"*. Se cumple por construcción: raw gitignorado, solo se versionan anotaciones derivadas |
| **SHEL5K** (Mendeley) | estrato `shel5k`, **5.000 imgs (77% del agregado)** | **CC BY 4.0**, DOI `10.17632/9rcv8mm682.4` | atribución + DOI |
| `ppe_siabar` (Roboflow) | split TRAIN | CC BY 4.0 | atribución (**y declarar el estado del entrenamiento a la entrega**: el TRAIN se construyó y la jornada de fine-tuning está **comprometida — ADR-017**; si a la entrega no se entrenó, se dice con causa técnica, nunca "quedó fuera") |
| **MOCS** (copia Roboflow `mocs-bowib`) | piloto A1 (evidencia cualitativa + ancla `person`↔`Worker`) | CC BY 4.0 **declarada por el uploader de la copia**; el original de `anlab340` nunca se descargó ni se verificó | **citar el paper original de MOCS** + declarar que se usó una copia de terceros, sin redistribución |
| **Rodaje propio 2026-07-25** | **el banco de 34 clips = el resultado principal** | material propio | consentimientos de los participantes (ver §3.3) |
| **Lote de internet (14 clips — ✎ 08-10: 13 con GT humano, `v08_c01` excluido con causa firmada)** | estrato B del banco de clips (Bloque B); **precisa L4, no la levanta** (D-113.1) | ✎ **2026-08-05: origen registrado** — canal de YouTube **`@HospitalConstruction`** (https://www.youtube.com/@HospitalConstruction). **Es *Standard YouTube License*, no Creative Commons** ⇒ base de uso: **académico/evaluativo con cita y sin redistribución** (postura `chv`), **nunca presentado como licencia de libre uso** | **citar el canal como fuente de las escenas** + los caveats de §3.3 (no es cámara-nativo · caras difuminadas en figuras · velocidad real verificada) |

### 3.2 Licencias de los modelos: hueco abierto

Los catálogos de `e-ovrt_media-plane/configs/models/` (`grounding-dino/`,
`mm-grounding-dino/`, `yoloe/`) **no traen campo de licencia**. El informe cita tres
familias de pesos y hoy no hay registro de bajo qué términos se usan. **Hay que
verificarlo y registrarlo antes de citarlas** — mirar el `LICENSE` del repo de origen de
cada familia de pesos y anotarlo junto al catálogo. No lo doy por sabido acá: es
exactamente el tipo de dato que no se declara de memoria.

### 3.3 El lote de internet: origen registrado el 2026-08-05, con dos salvedades

> ✅ **RESUELTO en lo esencial el mismo día.** El usuario aportó la procedencia: las 14
> escenas salen del **canal público de YouTube `@HospitalConstruction`**
> (https://www.youtube.com/@HospitalConstruction), cuyas descripciones declaran que los
> videos son públicos. **Decisión: se cita el canal como fuente de las escenas.** Quedó
> registrado en `e-ovrt_datasets/datasets/registry/license_registry.md`, sección
> **"Material de VIDEO"** — que hasta hoy no existía —, junto con la entrada del rodaje
> propio. La base de uso declarada es la misma que ya se usa para `chv`: **uso
> académico/evaluativo con cita, sin redistribución** (los `.mp4` están gitignorados; solo
> se versionan anotaciones derivadas, previews y nombres de archivo).
>
> **Salvedad 1 — RESUELTA, y define cómo se redacta: es *Standard YouTube License*.** Se
> revisó la descripción: **no hay marcador de Creative Commons**, así que rige la licencia
> por defecto, que no concede reproducción ni obra derivada. La descripción sí declara que
> lo grabado son vistas y escenas visibles al público — pero eso dice **qué se filmó**, no
> otorga reuso. ⇒ El informe declara **uso académico/evaluativo con cita y sin
> redistribución** (postura `chv`), y **nunca** "licencia CC" ni "material de libre uso".
>
> **Salvedad 2 — personas identificables de terceros**, consentimiento no obtenible. La
> declaración del autor ayuda **acá**: respalda que no hay expectativa razonable de
> privacidad sobre lo filmado. Mitigaciones igual: no se redistribuye, sin datos personales
> en el repo (DA-08/09), E-11 intacta. **Regla: si un frame del lote se publica como
> figura, se difuminan las caras.**
>
> **Dos caveats metodológicos del estrato, que van declarados con él:**
> **(1) velocidad real verificada por dos vías ⇒ las métricas temporales aplican** — el
> canal publica sobre todo time-lapse, y un clip time-lapse volvería inservibles TTFD /
> `confirm_after_ms` / SDR; el autor declara velocidad original y además se **midió** sobre
> las pre-anotaciones de los 14 clips: **0,4–2,8 px/frame de mediana** (máx ~23), propio de
> 30 fps continuos. Los 14 masters son 1920×1080 @ 30 fps.
> **(2) el material no es cámara-nativo** — el autor declara corrección de color,
> estabilización y recortes. Preproceso ajeno que no controlamos: se declara. El rodaje sí
> es cámara-nativo, así que los dos estratos se leen por separado (L5).
>
> **Falta**: URL y fecha de acceso por video (hoy: el canal + un video de referencia,
> subido 2015-04-05, grabado 2015-03-28).
>
> Lo que sigue abajo es el diagnóstico original. **Se conserva solo como rastro**: explica
> por qué registrar la procedencia no era opcional y qué se verificó antes de tenerla. Los
> dos puntos que abría —licencia del lote y consentimiento del rodaje— están cerrados
> (este banner y §3.3 arriba, más el registry).

Verificado el 2026-08-05 (antes de que se aportara el origen), tres cosas independientes:

1. Los **14 `clip.yaml` del lote de internet no tienen cláusula de licencia** (a
   diferencia de `cb_b01_p7`, que sí llevaba la condición escrita). ✎ 08-06: los 3
   promovidos (`v04_c01`/`v06_c01`/`v10_c01`) **ya la llevan** (bloque `license:` con
   `video_url: TODO` — la URL por video sigue pendiente, hallazgo 2 de §6).
2. El `license_registry.md` **no tiene ninguna entrada de video** — ni rodaje, ni banco
   de clips, ni lote de internet.
3. **No hay URL de origen registrada** para los 14 masters (`raw/1.1.mp4` … `10.1.mp4`).

Y la regla que lo vuelve vinculante ya estaba escrita: **spec 43 §7, "Marco legal
(bloqueante de la grabación, no del diseño)"**, que exige dos cosas distintas:

- *"**Consentimiento libre, expreso e informado por escrito** de cada persona grabada
  (**Ley 25.326, Disposición 10/2015** — doc 08 §1.3), archivado y **referenciado en
  `license_registry.md`** (sin datos personales en el repo)"*.
- *"**Bloque B: registrar la licencia** del dataset antes de usar los videos **en
  resultados reportables**"*.

Su ítem de checklist **`[ ] Consentimientos y licencias en license_registry.md; sha256 en
manifest` sigue sin marcar** (spec 43 §9). Y es el motivo #1 por el que `cb_b01_p7` se
retiró, que cita esa misma sección: *"licencia/consentimiento sin registrar — motivo
vinculante… no se resuelve con una pasada de CVAT"*.

**La consecuencia práctica:** cuando lleguen las anotaciones, el lote **queda
igualmente inelegible para resultados reportables** hasta que su procedencia esté
registrada. Anotarlo no lo desbloquea. Es decidible **hoy**, en paralelo al CVAT, y solo
lo puede hacer quien sepa de dónde salieron los videos.

**Dos casos, severidades distintas — no confundirlos:**

- **Rodaje (34 clips, el resultado principal): ✅ resuelto por declaración (2026-08-05).**
  Las personas que aparecen son **los propios integrantes del proyecto**, actuando según el
  guion del doc 69, **sin terceros en cuadro**: son a la vez los sujetos y los responsables
  del material, y las situaciones son actuadas — no documentan conducta laboral real de
  nadie. Eso es lo que se declara en el informe, y es una posición más fuerte que un
  formulario. Lo administrativo lo maneja el equipo por su cuenta; la identificación del
  responsable va en el informe, no en el registry. Queda disponible
  `registry/plantilla-consentimiento-audiovisual.md` por si la facultad pide el formulario.
- **Lote de internet (14 clips):** obra real de terceros, con personas identificables y
  **procedencia desconocida en el repo**. Riesgo alto: si no se puede acreditar el origen
  y sus términos, el material no entra al capítulo — exactamente como `cb_b01_p7`.

**Lo que se puede hacer sin esperar a nadie** (✎ 2026-08-06: la entrada de video **ya
se creó** ese mismo día — §3.3; lo que sigue faltando del bloque es solo **URL + fecha
de acceso por master**): completar en `license_registry.md` §Material de VIDEO la URL
de origen y términos por master, y el sha256 en el manifest. Si el lote no acredita, el capítulo **se sostiene
igual** con L4 declarada — es la regla del doc 57 §7.6: *el cierre lo decide la cobertura
del material; lo no cubierto se declara con causa, nunca se fabrica*.

---

## 4. Limitaciones y ADRs

### 4.1 Lista canónica de limitaciones: L1–L8 (cerrada 2026-08-05)

**Resuelto.** `results/index.md` definía **L1–L5** y `operacion/98` §6 listaba **7**
limitaciones con solo **4 etiquetadas** (L4, L1, L5, L2) — L3 no aparecía y tres iban
sueltas. Ahora las ocho tienen código en los dos lugares, con `results/index.md`
§Limitaciones declaradas como versión de referencia.

> **Colisión de etiquetas que hay que respetar al redactar:** la **Fase L** del doc 62 usa
> `L0`/`L1` para sus hitos (`L0` = ensayo pre-rodaje, `L1` = el rodaje). Se decidió
> **mantener el prefijo `L` para las limitaciones** (ya estaban citadas en varios docs) y
> desambiguar en prosa: escribir **"limitación L1"**, nunca `L1` a secas.

| ID | Limitación | Estado | Fuente |
|---|---|---|---|
| **L4** | **Un solo bloque guionado, sin obra real en video.** La más citable: mismos actores, misma locación, escenarios guionados | declarada; ✎ 08-06: licencia registrada y GT humano en marcha; **✎ 08-10 — formulación VIGENTE (D-113.1, firmada): "L4 se precisó, no se levantó** — existe medición en obra real no guionada (I1/I2, 13 clips, revisión ciega incluida) y esa medición **caracteriza por mecanismo dónde el sistema deja de ser evaluable; no lo valida sobre obra real**". No se crea L9: la frontera de juzgabilidad es el contenido nuevo de L4. Versión de referencia: `results/index.md` | `operacion/98` §6 + D-113.1 |
| **L1** | **FAR/hora no sostiene una cota.** Harían falta ~3 h de cumplimiento anotado; el control de negativos discrimina (T1/T2/G1: 0 FP de 4; D1/H1/B1: 2–3) | declarada con causa cuantificada (D-90.1) — **✎ 08-10: precisada**: desde el 08-07 hay un clip soak (`v06_c01`, 0,1027 h) y la tasa **es computable**; se cita como **"3 y 190 FP en 6:09,6 del único soak"** con la tasa horaria como derivada (29,2 / 1.850,8 FA/h). Sigue sin sostener una cota. Versión de referencia: `results/index.md` | `operacion/98` §6 |
| **L5** | **Escenarios desbalanceados** ⇒ obliga a reportar siempre por escenario y por estrato | declarada; es regla de lectura, no solo limitación | `results/index.md` |
| **L2** | **Sin doble anotación ni kappa** — decisión declarada, no omisión | declarada | `results/index.md` |
| **L3** | **Seis bordes adjudicados** en el GT del rodaje (oclusión, no cambio de estado), con firma en `clip.yaml` | declarada; trazable en `apply_adjudications.py` | `results/index.md` |
| **L6** | **El tracker no está medido en obra real con multitud** — G1 se verificó en vivo con pocos sujetos; el `track_id` es post-hoc/decorador | declarada y **etiquetada 2026-08-05** — **✎ 08-10: parcialmente levantada**: en `v06_c01` (127 personas reales) el tracker produjo **182 identidades con FP** — fragmenta en denso y el costo de G1 escala con la escena (F-103.2). Versión de referencia: `results/index.md` | `operacion/98` §6 |
| **L7** | **Licencia de `chv` parcial** (20,5% del bench de imágenes): uso permitido con cita, sin redistribución | declarada y **etiquetada 2026-08-05** | `operacion/98` §6 + §3.1 |
| **L8** | **CR-02 a Nivel A no cerrada** — un solo estrato, IC solapados | declarada y **etiquetada 2026-08-05** | `operacion/98` §6 |

**Y una que este armado agrega:** la latencia G2A **no es** vidrio→alerta (F-101.8). No
es una limitación del sistema sino del **instrumento**, y ya tiene su advertencia
obligatoria en el doc 97 §5.4. Decidir si entra a la lista con etiqueta propia o queda
solo como caveat de la tabla de latencia.

### 4.2 ADRs: dos series que se confunden

**Trampa de numeración, va al informe:** hay **dos** series de ADR y se confunden a
simple vista.

- `docs/decisiones/` → **ADR-001…ADR-019** (3 dígitos): las decisiones **del proyecto**
  (✎ 2026-08-06: *decía "…014"*; el 015 es el cierre de alcance. ✎ 2026-08-10: el 016 es
  la reapertura acotada de la distribución. ✎ 2026-08-18: *decía "…016"* — el 017 es la
  jornada de fine-tuning, el 018 el acople BFF-subproceso —**derogado el mismo 08-18 por
  el 020**—, el 019 el servicio HTTP del distribuidor y el **020** el cierre: HTTP es el
  acople, el subproceso baja a fallback ⇒ **dos** patrones de acople, no tres).
- `e-ovrt_control-plane/docs/decisions/` → **ADR-0001…ADR-0013** (4 dígitos, falta 0005):
  las decisiones **internas del control-plane**.

Se solapan en tema y difieren en número (p. ej. aplicabilidad de métricas es ADR-006 del
proyecto y ADR-0006 del control-plane). **Al citar, decir siempre la serie.**
✎ 2026-08-06: **la convención quedó fijada en el glosario (doc 13 §3, entrada
"ADR-NNN (dos series)")** y las citas sin serie de `nucleo/01` y `nucleo/10` fueron
aclaradas en el lugar.

> Queda saldado otro ítem del doc 75: reclamaba **8 ADRs inexistentes**
> (`ADR-0006..0013` del control-plane). **Existen los 8**, verificado hoy.

**Los del proyecto** (ADR-015 va en prosa aparte, §5/§6), con dónde aterrizan:

| ADR | Decisión | Dónde se declara |
|---|---|---|
| 001 | Estrategia del núcleo: **E-IND** (encuadre) | §17.3 estrategia + veredicto del eje (T-68) |
| 002 | Granularidad: G0 núcleo + G1 demostrativa | **Revisar el texto**: G1 dejó de ser demostrativa — es el mejor resultado del banco (F1 0,930) |
| 003 | Bus media→control: **ZeroMQ PUB/SUB**, broker diferido | arquitectura EBE (FIG-A, T-76) |
| 004 | Corrida paraguas y `experiment_id` | reproducibilidad (§2.4) |
| 005 | Distribución de alertas: recorte, canal MQTT, repo propio | ✎ **2026-08-12: funcionalmente implementada y verificada** — seis criterios de spec 45 cerrados, incluidos DBE/EBE, reporte y MQTT real. Quedan la vista de webconsole, la orquestación integral y el primer commit; E-06 sigue excluida. **✎ 2026-08-14: los tres pendientes del 08-12 quedaron cerrados el 2026-08-13** — vista de webconsole (`13c801e`, "feat(webconsole): mostrar outcomes de distribución") y orquestación integral (`42529e2`, "feat(experiments): orquestar distribución de alertas") en `e-ovrt_experimental-setup`; el repo `e-ovrt_alert-distribution` ya tiene historia propia (`c9903cc`, `1e6d8fa`). E-06 sigue excluida |
| **016** | **Reapertura acotada de la distribución** para cerrar la arquitectura | deroga ADR-015 §2b/§2c/§6; ratifica §2a/§3/§4/§5. E-06 sigue excluida |
| 006 | Reporte consolidado y **aplicabilidad de métricas** | lenguaje de estados: `not_applicable` / `non_temporal_source` |
| 007 | Semántica de corrida en EBE: **1:1** | T-76 |
| 008 | Control-plane como servicio mínimo | arquitectura |
| 009 | Config centralizada + webconsole como superficie de gestión | arquitectura + método |
| 010 | Secuenciación: plataforma primero, GT al final | método y cronología |
| 011 | Frontera de la política: el motor emite siempre; la supresión es de distribución | **`re_alerts` no son FP** |
| 012 | Sin memoria de cobertura bajo G0; la histéresis la subsume | mecanismo (F-81.1 / F-85.3) |
| 013 | Aplicabilidad por temporalidad de la fuente | estados de aplicabilidad |
| 014 | Layout y consolidación de artefactos por experimento | §2.4 |
| **017** *(✎ fila agregada 2026-08-18)* | El fine-tuning (E-04) se ejerce como jornada, nunca "falta de tiempo" | rama comparativa del §17.5 — **jornada T1 ejercida y cerrada con veredicto pre-registrado** (doc 123); T2 exploratorio en curso (D-FT-14/15) |
| ~~**018**~~ | ~~Tercer patrón de acople: BFF-subproceso~~ ⛔ **DEROGADA por 020** | **no va al informe** — registro histórico |
| **019** *(✎ fila agregada 2026-08-18)* | El distribuidor también como **servicio HTTP** (`:8082`) | §17.4 despliegue: los tres módulos son servicios HTTP config-driven; containerización diferida con causa (doc 124) |
| **020** *(✎ fila agregada 2026-08-18)* | **HTTP es el acople de la distribución**; el subproceso baja a fallback operativo y deja de ser patrón | §17.4/§17.3: **DOS patrones de acople** — (a) HTTP config-driven en los tres módulos, (b) bus ZeroMQ. El fallback **no se describe**: es operación, no arquitectura |

**ADR-015 — ✅ escrito y ACEPTADO el 2026-08-05.**
`decisiones/adr-015-cierre-de-alcance.md` (fuente: `docs/decisiones/adr-015-cierre-de-alcance.md`).
El doc 95 §5.1 lo pedía como *"recorte final de alcance"* porque los docs 91/94 declaraban
tracker/G1 como no implementado; **su premisa se invirtió** (G1 es el mejor resultado del
banco), así que no es un recorte: es el **registro de que el alcance creció, con
evidencia, y de qué sigue excluido**. Qué hace:

- **Registra los cuatro movimientos**: E-03 (G1 de demostrativa a capacidad operativa
  medida en 34/34), E-07 (parcial: OAK-D + EN-2 con 87% de descarte), E-13 (E-HYB-or
  ejecutada y refutada; `hyb_and` no ejecutada con causa), E-04 (no ejercida, pero por
  secuenciación — ✎ 2026-08-11: fila **superada por ADR-017**, E-04 es jornada
  experimental comprometida y la causa temporal está derogada). **E-10 y las otras
  ocho exclusiones no cambian.**
- **Cierra la puerta** (§2b): ninguna capacidad nueva de acá a la defensa — es la parte
  que *restringe*, y es el riesgo que el doc 95 realmente quería cubrir.
- **Registró un estado transitorio del condicional de ADR-005.** ADR-016 lo sustituyó:
  el condicional quedó resuelto en **sí** y el recorte mínimo fue implementado y
  verificado. §2b/§2c/§6 de ADR-015 quedaron derogados; §2a, §3, §4 y §5 —incluida
  **la lista de límites L1–L8**— siguen vigentes.
- **Desbloquea R-13** con una lista auditada ítem por ítem: **de los 8 límites de julio,
  5 estaban resueltos** (`track_id`, evaluadores de D1, GT preliminar, matching greedy,
  inventario de datasets) y sobreviven 3, uno de ellos agravado por F-101.8.
- **Desbloquea R-21 corrigiendo un punto falso**: su tabla dice *"MOT ✗ tracker no
  implementado"*; lo excluido son las **métricas** MOT (E-10), no la capacidad.

Integrado en `decisiones/README.md`, `estado-de-implementacion-adrs.md` (§0 y §1) y
anotaciones en R-13 y R-21 del doc 93. **Y aplicado al doc 10 el mismo día**: el ítem 10 de
la lista de alcance quedó reescrito (G1 = capacidad operativa medida en 34 clips, ya no
"demostrativa en 2–3") y las filas **E-03/E-04/E-07/E-13** de la tabla de exclusiones
llevan su estado real con evidencia. **Registro de alcance y resultados ya dicen lo mismo.**

*De yapa, en la misma pasada:* la fila del ADR-001 en `estado-de-implementacion-adrs.md`
§3 decía *"sigue abierto (acta `edir_v1` pendiente)"* — **el acta se firmó el 2026-07-29
(doc 76) y D1 corrió en los dos niveles**. Corregida.

---

## 5. Catálogo de mecanismos: lo que el CVAT no movió — y lo que agregó

Esta es la parte del capítulo que da credibilidad. La premisa original ("es inmune al
lote de internet: el GT nuevo puede mover un agregado, no un mecanismo medido") **quedó
verificada por los hechos** (✎ 2026-08-10): el CVAT llegó (docs 102–113), hubo
re-derivaciones y hasta una revisión ciega del GT, y el catálogo del Bloque A de abajo
sobrevivió intacto. El tramo de video **agregó mecanismos propios** — bloque nuevo al
final de esta sección. Texto fuente: los índices de `results/` (verificados
mecánicamente) — de ahí se transcribe, no de acá.

**Cómo la plataforma agrega sobre la detección cruda**
- **F-81.1** — la **histéresis rescata percepción intermitente**: CR-02 se detecta en ~1
  de cada 6 frames del episodio (F-G2.1) y el motor igual confirma.
- **F-85.3** — y es **palanca de doble filo, medida en los dos sentidos**: rescata lo
  intermitente-correcto y también sostiene lo intermitente-equivocado.
- **F-87.2** — **la unión de evidencia NO es monótona en un motor temporal**: sumar un
  brazo (`hyb_or`) no sube el recall, lo derrumba (0,824 → 0,353). Predicción
  pre-registrada **refutada**.
- **F-89.1 / F-89.2** — **el margen no estaba en el modelo ni en los prompts, sino en la
  identidad**: F1 0,789 → 0,930 con las detecciones **bit a bit las mismas** (SDR y TTFD
  idénticos). Es el hallazgo central del capítulo.
- **F-81.3** — TTFD ~5 frames: la latencia de la plataforma **es la política**, no el modelo.

**Cómo se expresa la condición en lenguaje (y su modo de falla propio)**
- **F-88.3** — **la etiqueta corta gana a la frase negada**, y eso ordena el eje.
- **F-88.1** — **el caption tiene costo medido**: 0,082 de F1 por una palabra.
- **F-88.2** — `bare_head` como evidencia directa **tampoco alcanza** (0,480 vs 0,582 de
  la ausencia espacial, **sobre las mismas detecciones**).
- **F-83.6** — **E-DIR no es un detector, es un recuperador**: recupera 18,5% de lo que
  E-IND no ve.
- **F-85.4** — **el ranking de Nivel A no transfiere a Nivel B**: la brecha se agranda
  con la plataforma.
- **F-85.5** — P9 es la única victoria de E-DIR, y está donde E-IND es más débil.
- **F-94.1** — **la palabra tiene que alinear con la taxonomía del despliegue**:
  `vehicle` junto a `machinery` da **0 detecciones**; aislada, AP 0,026 porque el 67% cae
  sobre lo que ese GT llama `machinery`. Segundo caso independiente el 2026-08-05
  (`gloves`: 252 detecciones, ninguna sobre un guante). **Va junto al número de A1, no
  después.**

**Qué sobrevive al tiempo real**
- **F-RT3** — el techo de fps es **contención de GIL**, no térmico ni la rama de texto.
- **F-RT5** — palanca aplicada y significativa: 3,75 → 4,42 fps, −14,4% latencia, p = 0,0195.
- **F-RT2** — la ventana temporal **exige estabilidad perceptual**: YOLOE entra en
  presupuesto y es inservible para la condición.
- **F-96.1** — a ~4 fps el agregado **no se degrada de forma detectable**, pero un
  agregado plano **escondía una redistribución completa**.
- **F-96.2** — **lo primero que se rompe bajo tiempo real es el rescate de F-81.1**:
  CR-02/P2 cae 1,00 → 0,60 → 0,20. Límite de cadencia declarado.
- **F-96.4** — **la ganancia de la identidad excluye el cero en las 4 densidades**
  (bootstrap pareado por clip). Formulación segura: doc 101 §3.
- **F-101.8** — **el G2A se mide desde el dequeue, no desde el fotón**: vidrio→alerta =
  `capture_to_host` (202–217 ms en el rodaje, 1.600 ms en tomas degradadas) **+ G2A**.

**Trampas de instrumento — se declaran o el número engaña**
- **F-EV1** — los clips negativos **no entran** a P/R/F1; su métrica son los FP.
- **F-96.6** — el **SDR no se compara entre cadencias**: sube al bajar la densidad, ~100%
  artefacto, verificado por decimación de las mismas detecciones.
- **F-96.5** — el **`t_alert` agregado no se compara entre densidades** sin control de
  supervivencia (corregido en revisión adversarial).
- **F-96.7** — 0 FP en negativos (✎ 08-10: acotado a las campañas del **Bloque A**): con
  4 clips es **control, no tasa**. El estrato B sí produce FP sobre sus 11 negativos —
  y ahí el conteo ES la métrica (ver el bloque del tramo de video).
- **F-RT1** — la sobre-marca de `vest` suprime CR-02 (dependiente de la vestimenta).
- **F-RT4** — deriva del host ±150 ms ⇒ las palancas <20% exigen ~10 pares **pareados
  intra-campaña** (protocolo doc 74).

**Qué agregó el tramo de video (estrato B) — ✎ 2026-08-10**
- **F-103.2** — bajo `subject` la identidad recupera el recall también en denso, **pero
  el tracker multiplica el ruido por la multitud**: en `v06_c01`, 182 identidades con FP
  contra 127 personas reales — el precio escala con la escena, no con el modelo.
- **F-105.2** — **la caída del estrato B queda confirmada a nivel PERSONA con el scorer
  oficial**: el mismo E-IND pasa de F1 0,41–0,55 en imágenes a ~0,15/0,01 sobre video
  real; **el recall se sostiene (~0,33), lo que se derrumba es la precision**.
- **F-105.3** — **la juzgabilidad NO se reduce a la escala**: `video02_clip07` tiene los
  sujetos más grandes del conjunto (370 px) y rinde F1 0,084 por oclusión mutua (58,5%
  de personas solapadas) — los ejes son **escala × iluminación × oclusión**.
- **F-105.4** — **el `unknown` del anotador mide la juzgabilidad HUMANA, no la del
  modelo**: el humano usa continuidad temporal (siguió a cada persona 6 minutos y
  determinó el 94%), el modelo decide frame a frame sin memoria — la vía de mejora
  señalada es **agregación temporal de evidencia para DETERMINAR estado**, no solo para
  confirmar.
- **F-108.1** — **la variable no era la granularidad: era la densidad** — `subject` solo
  hace falta cuando los sujetos se relevan; no existe "la mejor granularidad" del banco,
  existe la correcta para un régimen de densidad.
- **F-111.1 (enmendado — citar la versión enmendada)** — en obra real densa **la ventaja
  de la identidad que G1 mostró en el rodaje no se reproduce, y `subject` paga un orden
  de magnitud más FP** (asimetría 12× en negativos); el ranking por F1 **no se afirma**
  (n = 2 evaluables). La enmienda misma es citable como método.
- **F-113.1** — hallazgo de REPRODUCIBILIDAD: **re-evaluar sin re-agregar congela la
  procedencia** (el agregador copia `campaign.yaml` dentro de `metrics.json` — los
  `metrics.json` de I1/I2 declaraban el freeze pre-corrección); detectado y corregido
  **sin mover ninguna cifra**.
- **D-113.1** — decisión firmada: **se precisa L4, no se crea L9** — la frontera de
  juzgabilidad es el contenido nuevo de L4 (formulación de cita en §4.1).
- **D-113.2** — decisión firmada: la persona `unknown` **sale del denominador** del
  scorer de Nivel A, **pero una violación predicha sobre ella cuenta como FP** — "la
  alerta sobre una persona no juzgable suena igual"; la regla simétrica se evaluó y se
  descartó (medido: 48% de los FP de CR-01 en los pilotos caen sobre `unknown`).

**Resto del catálogo** (F-83.3/4/5/7, F-84.1/5/6, F-81.2, F-96.x restantes,
F-101.1/3/5/6/7/9, F-EV2/3, F-DR*, F-GT1): están en los índices de `results/` y en sus
docs de origen. **No los transcribo acá para no crear una segunda fuente**: el catálogo
vive en los índices verificados y este documento solo señala los que sostienen una
afirmación del capítulo.

---

