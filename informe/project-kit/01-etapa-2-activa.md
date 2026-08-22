# E-OVRT-VDP - paquete de etapa 2

> Generado el 2026-08-22. Etapa 2: seccion 17.1 y Anexos C y D.

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

- **Etapa activa:** 2 - Etapa 2: seccion 17.1 y Anexos C y D.
- Este archivo contiene el texto vigente que se modifica y sus insumos de ajuste.
- No se trasladan resultados propios hacia secciones cronologicamente anteriores.
- Nombre propio de esta etapa (01-etapa-2-activa.md): regenerarla no pisa el paquete de ninguna otra etapa.

---

## Fuente: `docs/informe/entregable/96b-informe-v11-17-1-consolidacion-metodologica.md`

> SHA-256 del bloque: `adce32b4919bef66ae736d57166bf417bc4331504a9dc59a12eb0fd2923af034`  
> Seleccion: documento completo.

# 96b — Texto extraído del informe v1.1: §17.1 Consolidación Metodológica del Protocolo Experimental

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

## 17. Desarrollo del Producto


### 17.1. Consolidación Metodológica del Protocolo Experimental

La consolidación metodológica transforma el marco teórico construido previamente en un protocolo experimental utilizable. Para ello fija decisiones sobre alcance, escenarios, infraestructura, datos, prompts, métricas y criterios de aceptación, integrando los desarrollos metodológicos en una secuencia coherente con el objetivo del prototipo experimental.

El referente experimental resultante delimita qué condiciones de riesgo integran el núcleo del prototipo, cómo se estructuran los escenarios de evaluación, con qué reglas se gestionan los datos, qué métricas deben producirse y cómo debe interpretarse la evidencia obtenida.

Esta instancia no implementa el pipeline ni reporta resultados empíricos. Establece las condiciones de comparabilidad, medición e interpretación necesarias para que el prototipo pueda desarrollarse y evaluarse sobre bases explícitas, trazables y defendibles.


### 17.1.1. Función y Alcance de la Consolidación Metodológica


##### 17.1.1.1. Función Metodológica Dentro del Trabajo

La función principal de esta parte del trabajo es ordenar la transición entre la fundamentación teórica y las instancias posteriores de diseño, implementación y validación. Para ello, la consolidación metodológica no se limita a enumerar componentes técnicos, sino que define el modo en que esos componentes serán evaluados, comparados e interpretados dentro del alcance experimental declarado.

El criterio rector prioriza la validez experimental, la trazabilidad y la correspondencia entre alcance, datos disponibles e instrumentación efectiva. El núcleo obligatorio del prototipo se ubica en las condiciones de Nivel 1 —CR-01 y CR-02—, donde convergen observabilidad visual, cobertura de datos, estrategias de evaluación defendibles y métricas aplicables con el hardware disponible. Las condiciones de Niveles 2 y 3 se conservan como extensiones condicionadas, debido a brechas de datos, visibilidad y razonamiento contextual.

A partir de ese criterio, se fija una secuencia experimental integrada: comparación primaria en Dataset-Based Evaluation (DBE), validación complementaria en Environment-Based Evaluation (EBE), reglas de partición sin leakage, política de formulación y congelamiento de prompts, jerarquía de métricas orientada al valor operativo de alerta y criterios para habilitar una rama comparativa de fine-tuning.

El resultado es un marco de trabajo que ordena el diseño, la implementación y la validación del prototipo, y que permite comparar variantes, medir desempeño e interpretar la evidencia bajo criterios consistentes.


##### 17.1.1.2. Articulación Entre los Desarrollos Metodológicos

La consolidación metodológica se apoya en cuatro dimensiones temáticas. La primera caracteriza la infraestructura, los escenarios y las restricciones de ejecución; la segunda define el catálogo de condiciones, sus niveles de complejidad y la política de prompts; la tercera establece cobertura, brechas y reglas de partición de datos; y la cuarta organiza la evidencia mínima que el prototipo deberá producir.

La integración de estas dimensiones permite ordenar una cadena de decisión: primero se delimita qué debe construir el prototipo y bajo qué restricciones; luego se establece cómo será medido; finalmente se fijan los criterios de interpretación de la evidencia. Esta lógica evita tratar los componentes por separado y concentra las definiciones metodológicas que estructuran la continuidad del proyecto.

Tabla 16

Articulación entre las dimensiones metodológicas de la consolidación experimental


| Dimensión metodológica | Aporte principal | Decisión consolidada |
| --- | --- | --- |
| Entorno experimental | Define CPN, EN, TN, escenarios DBE y EBE, y restricciones de hardware y software. | Ubica la viabilidad operativa en el CPN, separa entrenamiento de inferencia y formaliza el rol metodológico de cada escenario. |
| Condiciones de riesgo y prompts | Organiza las condiciones de riesgo por niveles de complejidad y fija el protocolo de prompts. | Delimita el núcleo obligatorio del prototipo en condiciones de detección directa de Nivel 1 y ordena el resto del catálogo como extensión condicionada. |
| Datasets y benchmarks | Elabora un inventario de datasets, benchmarks, cobertura por condición y reglas de partición. | Determina qué condiciones tienen soporte suficiente para evaluación directa, qué módulos requieren benchmarks externos y qué brechas exigen prudencia metodológica. |
| Framework de métricas | Jerarquiza métricas, define latencia de alerta, fija niveles de compromiso y establece criterios de ejecutabilidad experimental. | Establece la evidencia mínima del prototipo y separa métricas obligatorias, deseables y conceptuales según el alcance implementado. |

Nota. La tabla resume cómo cada dimensión metodológica aporta una parte del protocolo experimental integrado y qué decisión transversal queda consolidada para la continuidad del proyecto.


#### 17.1.2. Alcance Experimental Consolidado del Prototipo


##### 17.1.2.1. Delimitación del Catálogo de Condiciones de Riesgo

El catálogo retenido comprende seis condiciones de riesgo organizadas en tres niveles de complejidad. La decisión principal es distinguir entre el catálogo metodológico completo y el núcleo obligatorio de validación: CR-01 y CR-02 constituyen el plano mínimo del prototipo, porque son condiciones de detección directa de Nivel 1 derivadas del marco de seguridad laboral y construcción (Decreto N.º 911/1996, 1996; Ley N.º 19.587, 1972).

Esa priorización se justifica porque ambas reúnen observabilidad visual relativa, estrategias de detección directa o indirecta ya definidas, cobertura de datos suficiente y métricas aplicables sin depender de módulos todavía no implementados. CR-03 y CR-04 conservan relevancia, pero dependen de visibilidad fina, ausencia visual y datos complementarios; CR-05 y CR-06 orientan la arquitectura relacional, aunque su evaluación completa requiere persistencia temporal, regiones externas o razonamiento contextual. Esta cautela es consistente con la evidencia sobre dificultades de los modelos OVD ante atributos finos y dominios especializados de construcción (Bianchi et al., 2024; Abdalwhab et al., 2025).


##### 17.1.2.2. Núcleo Obligatorio y Extensiones Condicionadas

La distinción entre núcleo obligatorio y extensión condicionada no elimina condiciones del catálogo. Explicita el nivel de compromiso que esta instancia puede sostener con los datos, la instrumentación y la complejidad disponible. En consecuencia, la aceptación mínima del prototipo no depende de un desempeño uniforme sobre las seis condiciones, sino de demostrar funcionamiento defendible sobre el núcleo obligatorio y de producir evidencia parcial o exploratoria sobre las extensiones condicionadas cuando la arquitectura y los datos lo permitan.

El catálogo completo conserva valor directivo, pero la validación se concentra en aquello que puede medirse con rigor. Esta decisión permite preservar la coherencia entre objetivo experimental, cobertura de datos, complejidad técnica y capacidad real de instrumentación.

Tabla 17

Catálogo consolidado de condiciones de riesgo y rol experimental


| Código y condición | Nivel | Evidencia visual dominante | Módulos requeridos | Rol metodológico |
| --- | --- | --- | --- | --- |
| CR-01 - Persona sin casco | 1 | Presencia o ausencia de casco en región cefálica. | OVD frame-a-frame; estrategia directa o indirecta. | Núcleo obligatorio del prototipo experimental; condición prioritaria para comparación y aceptación. |
| CR-02 - Persona sin chaleco reflectivo | 1 | Presencia o ausencia de prenda de alta visibilidad en torso. | OVD frame-a-frame; estrategia directa o indirecta. | Núcleo obligatorio del prototipo experimental; condición prioritaria para comparación y aceptación. |
| CR-03 - Persona en posición elevada sin sistema anticaídas visible | 2 | Persona sobre estructura elevada y ausencia visible de arnés o línea de vida. | OVD + reglas espaciales intra-frame. | Condición exploratoria y condicionada a datos complementarios y visibilidad suficiente. |
| CR-04 - Borde elevado desprotegido con personas próximas | 2 | Borde sin protección colectiva y proximidad humana. | OVD + reglas espaciales intra-frame. | Condición exploratoria y condicionada; no bloquea la aceptación del núcleo del prototipo. |
| CR-05 - Maquinaria en operación cerca de peatones | 3 | Co-ocurrencia de maquinaria y personas bajo distancia de seguridad. | OVD + MOT + razonamiento contextual. | Extensión condicionada a módulo relacional y datos contextuales adecuados. |
| CR-06 - Persona dentro de zona restringida | 3 | Persona dentro de un área previamente parametrizada como restringida. | OVD + MOT + región de interés fija. | Extensión condicionada; requiere cámara fija o parametrización espacial externa al prompt. |

Nota. La distinción entre núcleo obligatorio y extensión condicionada no elimina condiciones del catálogo. Explicita el nivel de compromiso que esta instancia puede sostener con los datos, la instrumentación y la complejidad disponible.


#### 17.1.3. Diseño Metodológico General y Lógica de Escenarios


##### 17.1.3.1. Patrón de Riesgo Como Unidad de Análisis

El protocolo adopta como unidad de análisis el patrón de riesgo confirmado y no la detección aislada. Esta decisión evita reducir el problema a la mera producción de cajas por fotograma. En el proyecto, la condición de riesgo constituye la unidad semántica de entrada; el patrón de riesgo incorpora severidad, persistencia y, cuando corresponde, relaciones espaciales o temporales; y la alerta constituye la salida operativa trazable del sistema. Esta distinción ordena la relación entre detector, tracker, lógica contextual y backend de eventos.


##### 17.1.3.2. Cadena Operativa Mínima y Motor de Patrones

A partir de esa unidad de análisis, el protocolo asume una cadena operativa mínima entre percepción, evaluación y respuesta asistiva. En dicha cadena, las detecciones producidas por el modelo OVD funcionan como evidencia primaria, pero no constituyen por sí mismas una alerta. Para que una alerta sea considerada válida dentro del sistema, la evidencia debe ser agrupada, evaluada y confirmada como patrón de riesgo según los criterios definidos para cada condición.

En términos operativos, esta evaluación corresponde al motor de patrones, entendido en esta instancia como una abstracción lógica del plano de control. Este componente recibe eventos de detección normalizados, información de tracking cuando exista, configuración de prompts y reglas de patrón; aplica criterios de persistencia, severidad, histéresis y lógica espacial o contextual; y emite cambios de estado del patrón. Sólo cuando un patrón alcanza el estado confirmado puede registrarse una alerta interna dentro del sistema.

De manera sintética, el flujo operativo se organiza como detección OVD, publicación de evento de detección, evaluación por el motor de patrones, confirmación del patrón, registro de alerta, disponibilidad de la alerta para consulta o notificación, e interpretación por parte del supervisor humano. Esta secuencia permite vincular la medición experimental con una lógica de ejecución trazable, sin atribuir al sistema una capacidad autónoma de decisión sobre el cumplimiento normativo o la gestión efectiva de la obra.


##### 17.1.3.3. Escenarios de Evaluación

Sobre esa base, la evaluación se organiza en dos escenarios complementarios. El Escenario A, o Dataset-Based Evaluation (DBE), funciona como ámbito primario de comparación controlada, repetible y cuantificable. El Escenario B, o Environment-Based Evaluation (EBE), añade una validación de plausibilidad operativa sobre captura continua en entorno simulado o controlado. La relación entre ambos no es de reemplazo: el DBE aporta comparabilidad metodológica, mientras que el EBE permite observar el comportamiento integrado del pipeline en condiciones más próximas al uso previsto.

La secuencia de pruebas se estructura de manera progresiva. Parte de una condición base controlada, continúa con barridos univariados o de baja combinación sobre la configuración retenida y culmina con una prueba de mayor exigencia aplicada a la mejor configuración disponible. Este esquema permite acotar la complejidad experimental, evitar un diseño factorial inmanejable y, al mismo tiempo, conservar capacidad analítica para observar la sensibilidad del sistema frente a variables relevantes.


##### 17.1.3.4. Decisiones Estructurales del Diseño Metodológico

Tabla 18

Decisiones estructurales del diseño metodológico


| Decisión | Formulación adoptada | Implicación para el protocolo |
| --- | --- | --- |
| Unidad de análisis | Patrón de riesgo confirmado y alerta asociada, no detección aislada. | Obliga a medir persistencia, tiempo de respuesta y estabilidad además de precisión de detección. |
| Cadena operativa mínima | Detección OVD, evento de detección, evaluación de patrón, patrón confirmado, alerta registrada, disponibilidad para consulta o notificación, e interpretación humana. | Conecta la evidencia perceptiva con una salida operativa trazable y evita tratar la alerta como una detección aislada. |
| Motor de patrones | Abstracción lógica del plano de control que evalúa eventos de detección, tracks cuando existan y configuración de patrones contra reglas de persistencia, severidad, histéresis y lógica espacial o contextual. | Define dónde se transforma la evidencia perceptiva en patrón candidato, confirmado o resuelto, y evita tratar la alerta como salida directa del detector OVD. |
| Carácter asistivo de la alerta | La alerta informa un patrón de riesgo confirmado según los criterios operativos del prototipo, pero no sustituye la decisión del supervisor humano. | Preserva el alcance experimental, ético y operativo del prototipo. |
| Escenario primario | DBE sobre datasets y benchmarks retenidos. | Asegura comparabilidad, control de variables y repetibilidad de las mediciones. |
| Escenario complementario | EBE en entorno simulado o controlado. | Permite observar el comportamiento del pipeline sobre captura continua y variables visuales realistas. |
| Baseline obligatoria | Toda variante se mide primero en zero-shot. | Protege la comparación entre modelos y evita atribuir al ajuste mejoras que dependen de cambios de evaluación. |
| Comparación entre variantes | Fine-tuning sólo cuando existe soporte metodológico suficiente. | Evita convertir la adaptación al dominio en supuesto previo de viabilidad. |

Nota. DBE = Dataset-Based Evaluation. EBE = Environment-Based Evaluation. La baseline zero-shot constituye la referencia mínima a partir de la cual recién puede discutirse el valor de prompts, tracking o fine-tuning. La cadena operativa mínima fija el recorrido lógico de la alerta dentro del protocolo experimental. El motor de patrones explicita el componente lógico que transforma evidencia perceptiva en patrón confirmado y opera como criterio de diseño para su instrumentación arquitectónica posterior.


#### 17.1.4. Entorno Experimental, Infraestructura y Escenarios de Evaluación


##### 17.1.4.1. Introducción y Alcance

La presente sección documenta el entorno experimental sobre el cual se desarrolla y evalúa la plataforma E-OVRT-VDP. Su función es caracterizar de manera integrada la infraestructura de cómputo disponible para inferencia y entrenamiento, el stack probable de software asociado, los escenarios de evaluación definidos para el proyecto y las condiciones operativas propias de cada escenario. La información aquí formalizada responde a la pregunta rectora P-E1-04 definida en la fundamentación teórica, que indaga por las restricciones del entorno de ejecución —capacidad computacional, protocolos de transmisión y presupuesto de procesamiento— que condicionan las decisiones arquitectónicas del prototipo. Asimismo, la definición de los escenarios de evaluación establece las condiciones concretas bajo las cuales se ejercitará el prototipo y delimita el referente experimental de la presente sección.


##### 17.1.4.2. Infraestructura de Evaluación

La infraestructura de evaluación se organiza a partir de nodos funcionales. En este trabajo, un nodo representa un rol dentro del entorno experimental: procesamiento central, captura en borde o entrenamiento/adaptación de modelos. Cada rol puede materializarse mediante uno o más dispositivos concretos según la disponibilidad, el escenario de evaluación y la configuración efectiva de la corrida.

Bajo este criterio, el Central Processing Node (CPN) concentra la ejecución del pipeline principal, la inferencia, la evaluación de patrones, la medición de latencia y la consolidación de resultados experimentales. El Edge Node (EN) se ubica próximo a la fuente visual y se orienta a captura, transmisión de video y eventual preprocesamiento liviano. El Training Node (TN), cuando corresponda, se reserva para tareas de ajuste o preparación de variantes de modelo, sin sustituir la evaluación operativa sobre el CPN.


###### 17.1.4.2.1. Central Processing Node (CPN)

El CPN concentra la lectura o recepción de frames, la inferencia open-vocabulary, el postproceso de detecciones, la evaluación de patrones, el registro de alertas internas y la medición de métricas técnicas y operativas.

Para la etapa inicial del proyecto, el candidato principal para materializar este rol es una laptop HP Victus 15 Gaming, modelo 15-FB2024LA, año de lanzamiento 2024 (HP Inc., s. f.). Este equipo se toma como referencia por contar con una GPU NVIDIA GeForce RTX 4060 para laptop, basada en la arquitectura Ada Lovelace, con 8 GB de VRAM GDDR6, recurso que condiciona el tamaño de los modelos ejecutables, la precisión numérica utilizada, la posibilidad de cuantización y el presupuesto de latencia alcanzable.

Las especificaciones técnicas completas del hardware candidato para el CPN, incluyendo procesador, memoria, GPU, VRAM, sistema operativo y capacidades relevantes para inferencia, se detallan en el Anexo B.


###### 17.1.4.2.2. Implicancias del NVDEC para el Pipeline de Medios

El motor de decodificación por hardware NVDEC de la RTX 4060 permite descargar la decodificación del flujo de video del CPU a un bloque dedicado del dispositivo, reduciendo la carga de procesamiento en CPU y evitando la necesidad de decodificación por software en ese procesador. En el contexto del Escenario B, donde el CPN recibe un flujo continuo codificado en H.264 o H.265, esta capacidad favorece que el CPU se concentre en tareas de control, transferencia y posprocesamiento, mientras la GPU se destina principalmente al preprocesamiento y la inferencia del modelo OVD (NVIDIA Corporation, s. f.-b).


###### 17.1.4.2.3. Edge Node (EN) y Dispositivo de Captura Candidato

El EN cumple la función de captura, recepción o transmisión de video hacia el CPN, según la topología definida para cada corrida. Dentro del núcleo experimental, su responsabilidad se limita a captura, transmisión y, eventualmente, preprocesamiento liviano. La inferencia open-vocabulary en borde no forma parte del flujo base; su eventual incorporación corresponde a una variante condicionada, sujeta a medición independiente.

Como candidato principal para materializar este rol se considera la cámara Luxonis OAK-D Pro PoE, dispositivo Series 2 basado en la arquitectura RVC2. El equipo combina captura de video, conectividad de red y capacidad de procesamiento embebido, por lo que constituye una opción técnicamente pertinente para el Escenario B, donde el flujo de video puede transmitirse al CPN a través de la red local. Además, incorpora capacidades diferenciales de interés experimental, como percepción estéreo e iluminación IR, que amplían las posibilidades de evaluación en condiciones visuales diversas (Luxonis, s. f.-a, s. f.-b).

La selección definitiva del dispositivo de captura se realizará durante la implementación, según disponibilidad de hardware, topología adoptada y necesidades de evaluación. La OAK-D Pro PoE se mantiene como candidata preferente, sin descartar cámaras IP convencionales u otras fuentes controladas.

Las especificaciones técnicas completas del dispositivo candidato para el EN, incluyendo sensor, resolución, conectividad, capacidades embebidas y condiciones de uso experimental, se presentan en el Anexo B.


###### 17.1.4.2.4. Plan de Contingencia para el EN

En caso de que el dispositivo seleccionado como EN no pueda cumplir el rol asignado en la topología del Escenario B por limitaciones técnicas no previstas, el plan de contingencia consiste en operar con una cámara IP de CCTV convencional como nodo de captura. En esta configuración, el flujo de video se integrará a la topología que se defina en la instancia de análisis y diseño arquitectónico, ya sea mediante ingesta directa en el CPN o a través de un nodo intermedio que realice funciones de preprocesamiento o adaptación del stream antes de su incorporación al pipeline principal. Esta alternativa elimina la capacidad de inferencia en borde, pero preserva la posibilidad de validar el transporte de video sobre red local y la evaluación del pipeline de extremo a extremo sobre video en tiempo real captado en el entorno físico.


###### 17.1.4.2.5. Stack de Software de Inferencia (CPN)

El stack de software del CPN se orienta a la ejecución de los modelos OVD candidatos bajo condiciones de inferencia en tiempo real. Los modelos candidatos para la evaluación experimental son Grounding DINO y YOLOE, seleccionados porque representan polos distintos del trade-off entre expresividad semántica y latencia de inferencia identificado en el análisis de Etapa 1 y retomado como criterio metodológico en la Etapa 2 (Liu et al., 2023; Wang et al., 2025). En coherencia con ese enfoque, el stack propuesto prioriza compatibilidad con los frameworks oficiales de los modelos, soporte para aceleración sobre GPU NVIDIA y apertura suficiente para evaluar distintas rutas de optimización durante la instancia de análisis y diseño arquitectónico. El detalle completo de librerías, frameworks y versiones candidatas se presenta en el Anexo B en la Tabla B.3.


##### 17.1.4.3. Adaptación de Modelos al Dominio

Los modelos OVD candidatos se evalúan tanto en su variante preentrenada (baseline zero-shot) como en una variante ajustada mediante fine-tuning supervisado sobre datos del dominio de construcción o similar. El fine-tuning es un proceso preparatorio previo a la ejecución de los escenarios de evaluación; los pesos resultantes se transfieren al CPN para su evaluación bajo las mismas condiciones de hardware, garantizando una comparación justa.

La incorporación del fine-tuning como experimento comparativo responde a la pregunta rectora P-E1-08. El alcance del prototipo experimental excluye el entrenamiento desde cero; el fine-tuning supervisado sobre un subconjunto acotado de datos del dominio es una forma de adaptación compatible con esta restricción.


###### 17.1.4.3.1. Training Node (TN)

El proyecto cuenta con acceso al clúster de cómputo de alto rendimiento Mendieta para las actividades de fine-tuning. Mendieta es administrado por el Centro de Computación de Alto Desempeño de la Universidad Nacional de Córdoba (CCAD-UNC) y dispone de 19 nodos de cómputo. De acuerdo con la tabla oficial de infraestructura del CCAD, es el único clúster del conjunto comparado que incorpora GPUs, con 2 × NVIDIA A30 por nodo, por lo que constituye el recurso institucional pertinente para las tareas de ajuste fino de modelos OVD del proyecto (Centro de Computación de Alto Desempeño, 2026). Sus especificaciones técnicas completas se presentan en la Tabla B.4 del Anexo B.


###### 17.1.4.3.2. Stack de Software de Entrenamiento (TN)

El stack de software de entrenamiento contempla las herramientas necesarias para preparar datos, ejecutar procesos de ajuste o adaptación de modelos y evaluar variantes entrenadas sobre el dominio de construcción civil. El detalle completo del entorno previsto, incluyendo librerías, frameworks y configuraciones candidatas, se presenta en el Anexo B en la Tabla B.5.


###### 17.1.4.3.3. Flujo de Transferencia y Evaluación

El TN no participa en la ejecución de los escenarios de evaluación; su rol se limita a la preparación de los modelos que luego serán evaluados en el CPN (y eventualmente en el EN para inferencia ligera). Los modelos candidatos se entrenan en el TN con el subconjunto de entrenamiento definido en la estrategia de datos, benchmarks y partición, los checkpoints resultantes se exportan al formato requerido por el runtime de inferencia del CPN (PyTorch nativo, TensorRT u ONNX), y se evalúan en los Escenarios A y B bajo las mismas condiciones de hardware y software que los modelos preentrenados. Esta separación garantiza que la comparación entre variantes preentrenada y fine-tuned refleje exclusivamente el efecto de la adaptación al dominio.


##### 17.1.4.4. Escenarios de Evaluación

Se definen dos escenarios de evaluación complementarios. El primero permite la evaluación controlada y reproducible del pipeline mediante datasets de referencia públicos; el segundo expone el sistema a condiciones visuales representativas del dominio real mediante vídeo en tiempo real captado en un entorno físico. Ambos escenarios son necesarios dado que el primero habilita la comparación cuantitativa entre variantes de modelo y, cuando el dataset y el protocolo lo permitan, el contraste con métricas reportadas en la literatura, mientras que el segundo valida la viabilidad operativa bajo condiciones que ningún dataset puede replicar completamente. En ambos escenarios, la evaluación contempla la ejecución tanto de modelos preentrenados (baseline) como de modelos ajustados mediante fine-tuning en el TN (Sección 17.1.9), permitiendo una comparación directa del impacto de la adaptación al dominio.


###### 17.1.4.4.1. Escenario A - Dataset-Based Evaluation (DBE)

En este escenario el pipeline procesa material de imagen o video proveniente de datasets públicos de referencia. La ausencia de condiciones en tiempo real permite reproducibilidad exacta, aislamiento de variables y, cuando el dataset y el protocolo de evaluación coincidan con los de la fuente de referencia, contraste con métricas reportadas en la literatura. Constituye el escenario primario para la evaluación cuantitativa de los componentes OVD y MOT del pipeline, tanto en su variante preentrenada como en la variante ajustada por fine-tuning. Los datasets candidatos se documentan en la estrategia de datos, benchmarks y partición.

Tabla 19

Características del Escenario A - Dataset-Based Evaluation (DBE)


| Aspecto | Descripción |
| --- | --- |
| Tipo de entrada | Imágenes y secuencias de video provenientes de datasets anotados |
| Fuente | Colección de datasets candidatos (la estrategia de datos, benchmarks y partición) |
| Nodo de ejecución | CPN para toda la inferencia y evaluación |
| Modelos evaluados | Variante preentrenada (baseline) y variante fine-tuned, cuando aplique, para los modelos candidatos seleccionados |
| Conectividad | No aplica; procesamiento off-line sobre archivos locales |
| Ventaja principal | Reproducibilidad exacta; comparación directa con benchmarks de la literatura; aislamiento del efecto del fine-tuning |
| Limitación principal | Existen datasets públicos de construcción civil para detección, pero no benchmarks del dominio con tracking anotado; la evaluación MOT requiere benchmarks generales complementarios y un protocolo propio de transferencia al dominio. |


###### 17.1.4.4.2. Escenario B - Environment-Based Evaluation (EBE)

En este escenario el pipeline opera sobre vídeo en tiempo real captado en un espacio de obra simulado. Este escenario valida la viabilidad operativa del sistema bajo condiciones visuales y de conectividad representativas del dominio real, incluyendo variaciones de iluminación, oclusiones y densidad de personas en escena. A diferencia del Escenario A, el pipeline se ejercita de extremo a extremo, incluyendo las etapas de captura y transporte de video, y permite evaluar el comportamiento del motor de razonamiento temporal bajo condiciones de operación continua. Al igual que en el Escenario A, se ejecutan las variantes preentrenada y fine-tuned de cada modelo candidato seleccionado tras la evaluación del Escenario A.

Tabla 20

Características del Escenario B - Environment-Based Evaluation (EBE)


| Aspecto | Descripción |
| --- | --- |
| Tipo de entrada | Video en tiempo real desde el EN (OAK-D Pro PoE, o cámara IP en contingencia). |
| Espacio físico | Espacio de obra simulado. |
| Participantes | Personas reales portando EPP (casco, chaleco reflectante, entre otros); configuración de escenas con y sin infracción deliberada. |
| Condiciones visuales | Variables según la configuración de prueba prevista para la validación experimental, definidas en función del diseño experimental del escenario y de las condiciones operativas que se establezcan para su evaluación. |
| Nodo de ejecución | CPN para inferencia central; EN para captura y opcionalmente inferencia ligera. |
| Modelos evaluados | Variante preentrenada (baseline) y variante fine-tuned, sobre el modelo o combinación seleccionada tras el Escenario A. |
| Conectividad | Red LAN. |
| Ventaja principal | Validación operativa bajo condiciones del dominio; ejercita el pipeline E2E completo incluyendo transporte de video y motor de razonamiento temporal. |
| Limitación principal | Menor reproducibilidad que el Escenario A; requiere gestión de consentimiento libre, expreso e informado e información previa a los participantes, conforme al régimen de protección de datos personales y videovigilancia aplicable (Argentina, 2000; Disposición 10/2015, 2015). |


##### 17.1.4.5. Parámetros Operativos de Referencia

Los parámetros operativos de referencia establecen una base inicial para orientar la evaluación del pipeline experimental. No constituyen valores definitivos de configuración, sino condiciones de partida que permiten delimitar resolución, tasa de cuadros, modalidad de transporte, procesamiento esperado y restricciones generales de ejecución. Su función es ofrecer un marco común para comparar pruebas posteriores y evitar que cada experimento se defina de manera aislada.


###### 17.1.4.5.1. Parámetros de referencia del pipeline

Los parámetros de referencia del pipeline resumen las condiciones operativas previstas para las primeras instancias de evaluación, incluyendo aspectos vinculados con entrada de vídeo, frecuencia de procesamiento, resolución, modalidad de inferencia y registro de resultados. Los valores orientativos se presentan en el Anexo B en la Tabla B.6


###### 17.1.4.5.2. Transporte de Video en el Escenario B

En el Escenario B, el transporte de video permite evaluar el comportamiento del sistema cuando la captura y el procesamiento no se encuentran concentrados en el mismo nodo. Este escenario introduce condiciones más cercanas a una operación distribuida, ya que el flujo visual debe ser transmitido desde el EN hacia el CPN a través de la red local antes de ser procesado por el pipeline de inferencia. La topología de red prevista y sus parámetros asociados se detallan en el Anexo B en la Tabla B.7.


##### 17.1.4.6. Restricciones y Condicionantes del Entorno Experimental

Las restricciones detalladas en la Tabla 21 condicionan las decisiones de diseño de etapas posteriores y deben tenerse presentes al interpretar los resultados experimentales.

Tabla 21

Restricciones y condicionantes del entorno experimental


| Restricción | Origen | Implicación para el diseño |
| --- | --- | --- |
| VRAM de 8 GB en el CPN | Hardware — RTX 4060 Laptop (8 GB VRAM) | Limita el tamaño de los modelos ejecutables sin cuantización y condiciona la resolución de entrada, el batch efectivo y la elección de runtime en inferencia. |
| Capacidad de inferencia del EN limitada a 1.4 TOPS para AI | Hardware — OAK-D Pro PoE / RVC2 | Restringe la complejidad de los modelos que pueden ejecutarse localmente; el uso del EN debe considerarse, en principio, para captura inteligente, preprocesamiento o inferencia ligera en borde. |
| Windows 11 como SO base del CPN | Hardware — CPN | Las versiones de CUDA, cuDNN, TensorRT y demás runtimes deben ser compatibles con Windows. En caso de adoptarse DeepStream, su integración deberá evaluarse en la instancia de análisis y diseño arquitectónico mediante la vía correspondiente sobre WSL2. |
| Cobertura limitada del dominio para evaluación de tracking | Datasets públicos analizados en la la estrategia de datos, benchmarks y partición | La evaluación MOT requiere benchmarks generales complementarios y la formalización de un protocolo de transferencia al dominio, dado que la cobertura específica del dominio para tracking anotado es insuficiente. |
| Presupuesto de latencia G2A de 50–250 ms | el framework de métricas | Condiciona la selección de modelos, la resolución de entrada y la configuración de runtimes. |
| Acceso al cluster sujeto a disponibilidad institucional del recurso | Infraestructura institucional — CCAD-UNC | El fine-tuning debe planificarse en función de la disponibilidad efectiva del recurso institucional, lo que puede condicionar la cantidad y secuencia de experimentos realizables. |
| Necesidad de split train/eval disjunto | Principio metodológico | Los datos utilizados para fine-tuning no pueden formar parte del conjunto de evaluación. La partición debe documentarse explícitamente. |
| Recaudos ético-legales en el Escenario B | Ley N.º 25.326 y Disposición 10/2015 | Las pruebas con personas en el campo visual requieren consentimiento informado e información previa. El carácter académico y controlado del prototipo atenúa el perfil de riesgo, pero no elimina las obligaciones de resguardo y minimización. |

Nota. Elaboración propia basada en las especificaciones del hardware disponible, la caracterización del TN y del EN en la presente sección, los criterios metodológicos fijados en la la estrategia de datos, benchmarks y partición y el marco normativo argentino aplicable a protección de datos personales y videovigilancia.


##### 17.1.4.7. Lectura Metodológica de la Infraestructura Operativa y sus Restricciones

La infraestructura del proyecto se organiza en tres nodos con roles diferenciados. El Central Processing Node (CPN) es la plataforma donde debe probarse la viabilidad operativa. El Training Node (TN), correspondiente al clúster institucional Mendieta, cumple una función acotada de entrenamiento o exportación de variantes ajustadas. El Edge Node (EN) aporta captura continua para el EBE y, sólo si la arquitectura lo justifica, preprocesamiento o inferencia ligera.

La consecuencia metodológica es que las conclusiones sobre tiempo real, latencia, consumo de recursos y sostenibilidad del pipeline deben anclarse en el CPN: una HP Victus 15 con GPU NVIDIA GeForce RTX 4060 Laptop de 8 GB de VRAM, 32 GB de RAM y Windows 11. Esta restricción orienta la selección de modelos, resolución de entrada, composición del vocabulario activo y runtimes de inferencia.

Tabla 22

Infraestructura experimental y función metodológica de cada nodo


| Nodo | Configuración relevante | Función metodológica | Lectura correcta dentro del protocolo |
| --- | --- | --- | --- |
| CPN | HP Victus 15; RTX 4060 Laptop 8 GB; 32 GB RAM; Windows 11. | Inferencia, evaluación del pipeline y medición de recursos y latencia. | Es el punto donde debe defenderse la viabilidad operativa del prototipo experimental. |
| TN | Clúster Mendieta; nodos con 2 x NVIDIA A30; Linux institucional. | Entrenamiento supervisado o exportación de variantes ajustadas, si aplica. | No sustituye la prueba operativa sobre el CPN ni redefine el presupuesto real del sistema. |
| EN | Dispositivo de captura candidato para el EBE; OAK-D Pro PoE o alternativa IP. | Suministro de video continuo y eventual preprocesamiento o inferencia ligera. | Su rol exacto depende de la arquitectura final; no debe asumirse capacidad de borde no validada. |

Nota. La separación entre CPN, TN y EN no es organizativa sino metodológica: define dónde se entrena, dónde se ejecuta y dónde debe interpretarse la capacidad real del prototipo.

El entorno impone restricciones explícitas. La VRAM de 8 GB limita el tamaño de los modelos y reduce el margen para batching agresivo o vocabularios extensos. La capacidad de IA en el borde del EN candidato no permite asumir que las variantes OVD principales puedan ejecutarse allí sin simplificaciones. La combinación Windows 11, CUDA y eventuales runtimes como ONNX Runtime, TensorRT o DeepStream vía WSL2 introduce además complejidad de integración que deberá quedar documentada en la bitácora del sistema.


#### 17.1.5. Condiciones de Riesgo, Patrones y Protocolo de Prompts


##### 17.1.5.1. Introducción y Alcance

La fundamentación teórica del proyecto E-OVRT-VDP dejó abierta una brecha metodológica entre la identificación normativa de condiciones de riesgo relevantes para seguridad laboral y su traducción en consultas textuales evaluables por modelos de detección open-vocabulary. Junto con esa brecha, el análisis previo señaló que la formulación del prompt no constituye un detalle accesorio, sino una variable que puede alterar de manera significativa el desempeño del detector en dominios especializados.

En ese marco, la presente sección responde a la pregunta rectora P-E1-02 definida en la fundamentación teórica. Define la taxonomía de condiciones de riesgo que integran el alcance del prototipo experimental, establece los patrones de riesgo asociados con severidad y persistencia orientativa, y fija un protocolo sistemático para el diseño y la evaluación de prompts OVD. En articulación con el framework de métricas, la sección delimita además cómo esas definiciones conceptuales deben leerse respecto de la latencia de alerta, las métricas operativas y los criterios de aplicación del framework evaluativo.

El alcance de la sección es metodológico. Establece qué condiciones deben detectarse, cómo se agrupan en patrones de riesgo, con qué severidad conceptual y criterios analíticos de persistencia se interpretan, y con qué formulaciones textuales se evaluarán. Además, incorpora una operacionalización preliminar del motor de patrones como componente lógico responsable de transformar detecciones y trayectorias en patrones candidatos, confirmados o resueltos. Esta definición no constituye todavía una implementación de software ni fija contratos técnicos finales, pero sí delimita la estructura mínima de ejecución que deberá materializarse en la instancia de análisis y diseño arquitectónico. Los umbrales cuantitativos finales de aceptación y la calibración empírica de ventanas, reglas e histéresis corresponden a el framework de métricas y a la validación experimental de la validación experimental.


##### 17.1.5.2. Taxonomía de Condiciones de Riesgo para el Prototipo

El primer paso consiste en delimitar el subconjunto de condiciones de riesgo que el prototipo experimental debe ser capaz de detectar. Para ello se explicitan los criterios de selección aplicados sobre el universo relevado en la fundamentación teórica, se presenta la clasificación en tres niveles de complejidad según las capacidades del sistema requeridas para su evaluación y, finalmente, se consolida el catálogo de condiciones seleccionadas junto con sus consideraciones de evaluabilidad. El resultado constituye el insumo directo tanto para la definición de patrones de riesgo como para el diseño de prompts OVD.


###### 17.1.5.2.1. Criterios de Selección del Subconjunto del Prototipo Experimental

El universo de condiciones de riesgo identificado en el análisis normativo de la fundamentación teórica abarca categorías como uso de EPP (casco, chaleco, calzado), protección contra caídas en altura, delimitación de áreas de riesgo, control de circulación con maquinaria, orden y limpieza e instalaciones eléctricas provisorias. El prototipo experimental no pretende cubrir la totalidad de ese espacio, sino seleccionar un subconjunto acotado que permita demostrar la viabilidad técnica del concepto. Con ese fin se aplican tres criterios de selección, calibrados a las restricciones reales de recursos y al contexto académico del proyecto.

Representatividad de niveles de complejidad. El subconjunto debe incluir al menos una condición de cada nivel de complejidad definido en la clasificación de la sección 17.1.5.2.2, de modo que la evaluación ejercite las capacidades del pipeline en sus distintas configuraciones. Este criterio es viable porque los niveles corresponden a capacidades del sistema que deben evaluarse independientemente de la cantidad de condiciones seleccionadas.

Factibilidad de detección visual. Las condiciones seleccionadas deben tener correlatos visuales suficientemente diferenciados como para ser evaluables mediante análisis de imagen en las resoluciones y ángulos de cámara típicos de un entorno de laboratorio o simulado. Esto excluye condiciones cuya manifestación visual depende de detalles de difícil resolución (por ejemplo, la distinción entre calzado de seguridad y calzado común), así como condiciones sin correlato visual directo (por ejemplo, “capacitación insuficiente” o “plan de seguridad no elaborado”). La exclusión deliberada de condiciones de baja observabilidad evita comprometer la validez de los resultados experimentales del prototipo con limitaciones ajenas al sistema. La pertinencia de este criterio se ve reforzada por evidencia empírica reciente que muestra, por un lado, que los modelos OVD preentrenados pueden presentar limitaciones importantes para discriminar detalles finos y atributos visuales sutiles (Bianchi et al., 2024) y, por otro, que en tareas de dominio especializado en construcción su desempeño puede caer marcadamente frente a detectores ajustados al dominio (Abdalwhab et al., 2025).

Viabilidad de evaluación con recursos disponibles. Las condiciones seleccionadas deben poder evaluarse con alguna combinación de datasets públicos existentes, subconjuntos anotados de los mismos o datos generados en entorno controlado, sin exigir campañas extensivas de recolección o anotación incompatibles con un proyecto académico. Este criterio no presupone cobertura perfecta desde el inicio, pero sí exige que la brecha entre lo disponible y lo necesario sea acotada y metodológicamente manejable.


###### 17.1.5.2.2. Clasificación por Niveles de Complejidad

La clasificación de las condiciones de riesgo en tres niveles de complejidad responde a una distinción funcional sobre las capacidades que el sistema debe desplegar para evaluarlas. Esta tipología tiene consecuencias directas tanto sobre la arquitectura del pipeline como sobre el protocolo de evaluación aplicable a cada condición.

Condiciones de Nivel 1: Entidad simple. Involucran la detección de un único objeto o atributo sobre una entidad. Su evaluación es resoluble, en principio, mediante una única consulta OVD sobre un fotograma individual, sin requerir información temporal ni relacional. Un ejemplo representativo es la detección de casco de seguridad sobre una persona, donde el modelo OVD recibe un prompt como “person with hard hat” o “hard hat” y debe localizar las instancias correspondientes en la imagen. La evaluación de la condición de riesgo asociada (presencia o ausencia del EPP) admite dos estrategias diferenciadas que se analizan en la Sección 17.1.5.4.

Condiciones de Nivel 2: Entidad con atributo contextual. Estas involucran entidades sobre las cuales debe verificarse un atributo que depende de información espacial dentro del mismo fotograma. A diferencia del Nivel 1, la condición no se reduce a la detección aislada de un objeto, sino que requiere evaluar la relación espacial entre la entidad y su contexto visual inmediato. Un ejemplo es la presencia de una persona sobre una estructura elevada (andamio, plataforma), donde el modelo OVD puede detectar individualmente a la persona y a la estructura, pero la determinación de que la persona se encuentra sobre la estructura requiere un análisis de las relaciones geométricas entre las detecciones, como la superposición vertical de bounding boxes. Este análisis puede implementarse mediante lógica de post-detección que opere sobre las salidas del modelo en el mismo fotograma, por ejemplo a través de reglas geométricas de solapamiento, proximidad o posicionamiento relativo entre regiones detectadas. A diferencia del Nivel 3, este tipo de condición no exige aún persistencia temporal ni mantenimiento de identidad entre frames, pero sí introduce una capa adicional de razonamiento espacial intra-frame. En consecuencia, las condiciones de Nivel 2 representan un escalón intermedio de complejidad, en el que la evaluabilidad depende tanto de la calidad de la detección de entidades como de la solidez de las reglas espaciales definidas para interpretar su relación contextual.

Condiciones de Nivel 3: Relación entre entidades. Por último, estas condiciones involucran dos o más entidades independientes cuya co-ocurrencia espacial o temporal constituye la condición de riesgo. Estas condiciones exceden la capacidad del detector OVD operando frame-a-frame, ya que requieren tanto la detección individual de cada entidad como un módulo de razonamiento que evalúe relaciones geométricas entre ellas (distancia, contención) y las estabilice temporalmente. El tracker MOT interviene en este nivel para preservar la identidad de cada objeto rastreado a lo largo de los frames consecutivos que abarca el intervalo de evaluación. Un ejemplo es la co-ocurrencia de maquinaria pesada y peatones por debajo de una distancia de seguridad, donde ambas entidades son detectables individualmente por el OVD, pero la evaluación de proximidad peligrosa requiere calcular distancias entre detecciones y sostener esa evaluación durante un intervalo temporal.


###### 17.1.5.2.3. Catálogo de condiciones de riesgo seleccionadas

La Tabla 23 presenta las seis condiciones de riesgo seleccionadas para el prototipo experimental, organizadas por nivel de complejidad. Para cada condición se indica su código identificador, la categoría normativa de origen, la descripción operativa, el componente del sistema responsable de su evaluación y una estimación cualitativa de la dificultad de detección OVD.

Tabla 23

Catálogo de condiciones de riesgo seleccionadas para el prototipo experimental.


| Código | Nivel | Cat. normativa | Condición de riesgo | Evidencia visual | Componente evaluador | Dificultad OVD estimada |
| --- | --- | --- | --- | --- | --- | --- |
| CR-01 | 1 | EPP — casco | Persona sin casco de seguridad en zona de obra | Presencia o ausencia de casco en región cefálica de la persona | OVD frame-a-frame | Media |
| CR-02 | 1 | EPP — chaleco | Persona sin chaleco reflectivo en zona de tráfico o maquinaria | Presencia o ausencia de prenda de alta visibilidad en torso | OVD frame-a-frame | Media-Baja |
| CR-03 | 2 | Protección contra caídas | Persona en posición elevada sin sistema anticaídas visible | Persona sobre andamio o plataforma sin arnés o línea de vida visible | OVD + contexto espacial intra-frame | Alta |
| CR-04 | 2 | Protección contra caídas | Borde elevado desprotegido con personas próximas | Borde de plataforma o losa sin baranda o red perimetral, con presencia humana | OVD + contexto espacial intra-frame | Alta |
| CR-05 | 3 | Coexistencia peatón-maquinaria | Maquinaria en operación en proximidad a peatones sin separación | Co-ocurrencia de maquinaria pesada y personas por debajo de distancia de seguridad | OVD + MOT + razonamiento contextual | Media |
| CR-06 | 3 | Delimitación de áreas | Persona dentro de zona restringida o delimitada | Presencia de persona en área demarcada como prohibida o restringida | OVD + MOT + razonamiento contextual | Media |

Nota. La columna “Componente evaluador” indica qué módulos del sistema participan en la evaluación de cada condición. “OVD frame-a-frame” significa que la condición es resoluble con una o más consultas al detector por fotograma. “OVD + contexto espacial intra-frame” indica que se requiere evaluar relaciones geométricas entre detecciones dentro del mismo frame (por ejemplo, superposición vertical de bounding boxes entre persona y andamio en CR-03, o proximidad entre persona y borde desprotegido en CR-04). “OVD + MOT + razonamiento contextual” indica que la evaluación requiere persistencia temporal de trayectorias y lógica de evaluación relacional cuyo diseño corresponde a la instancia de análisis y diseño arquitectónico. La columna “Dificultad OVD estimada” refleja una valoración cualitativa basada en la degradación documentada de modelos OVD ante atributos de granularidad fina (Bianchi et al., 2024), en las dificultades asociadas a la discrepancia de distribución y vocabulario cuando detectores de gran vocabulario se trasladan a dominios downstream o especializados (Jiang et al., 2024), y en evidencia reciente sobre el menor desempeño de modelos vision-language/open-vocabulary preentrenados frente a detectores ajustados al dominio en entornos de construcción (Abdalwhab et al., 2025). De manera únicamente conceptual, se considera además la asimetría entre juicios de presencia y ausencia observada en la percepción visual humana, invocada aquí como analogía metodológica y no como propiedad demostrada de los detectores OVD (Mazor et al., 2021). No se pondera en esta columna la dificultad propia del razonamiento contextual.


###### 17.1.5.2.4. Consideraciones sobre Evaluabilidad y Limitaciones

La selección prioriza condiciones con alta observabilidad visual y disponibilidad plausible de datos de evaluación. Aun así, presenta particularidades que conviene explicitar.

La condición CR-04 —borde desprotegido— presenta dos particularidades relevantes. La primera concierne a la naturaleza negativa de la evidencia visual de la condición de riesgo. Dado que esta condición se define por la ausencia de un elemento de protección —baranda o red perimetral—, su evaluación resulta conceptualmente más exigente que en condiciones basadas en la presencia explícita de objetos. En este sentido, la literatura sobre percepción visual humana sugiere asimetrías entre juicios de presencia y ausencia, con respuestas más lentas y menor confianza ante ciertos juicios de ausencia; sin embargo, esta evidencia proviene de tareas perceptuales humanas y no de evaluación automática en visión por computadora, por lo que se invoca aquí únicamente como analogía metodológica (Mazor et al., 2021). La segunda particularidad es geométrica: la determinación de si un borde es efectivamente elevado depende de información tridimensional que la proyección bidimensional de la cámara no preserva completamente. Por ello, la ambigüedad asociada a altura, profundidad, perspectiva y oclusión debe asumirse desde el diseño experimental.

La condición CR-03 también exige cautela. La evidencia visual relevante no es solo la presencia de una persona en altura, sino la ausencia visible de un sistema anticaídas, lo que depende fuertemente de la escala del objeto en imagen, el ángulo de cámara, la oclusión y la resolución disponible. En consecuencia, su dificultad no proviene únicamente del razonamiento espacial intra-frame, sino también de la visibilidad efectiva del EPP que debería observarse.

Las condiciones de Nivel 3 —CR-05 y CR-06— no son evaluables mediante prompts integrados de OVD, sino mediante la detección de entidades componentes más razonamiento contextual. En CR-06, además, la evaluabilidad presupone cámaras fijas y una parametrización espacial externa al prompt —por ejemplo, un polígono de zona restringida definido por el operador—. Este supuesto debe quedar explícito desde esta etapa, ya que condiciona tanto el diseño experimental como la futura implementación del módulo de razonamiento contextual.

En un escenario real, múltiples condiciones pueden co-ocurrir sobre la misma persona y el sistema las tratará como unidades de detección ortogonales. Esta decisión simplifica el diseño y la evaluación del prototipo experimental, pero también implica que la correlación entre condiciones no se explota como señal de refuerzo. A ello se suman factores contextuales transversales —resolución, ángulo de cámara, iluminación y oclusión— que deberán documentarse como variables experimentales para interpretar correctamente el desempeño observado.


##### 17.1.5.3. Definición Conceptual de Patrones de Riesgo

Esta sección define conceptualmente los patrones de riesgo que constituyen la unidad operativa de análisis del sistema E-OVRT-VDP. Para ello articula tres componentes: la definición del patrón como abstracción que integra condiciones detectadas con criterios de persistencia y severidad; la delimitación de los niveles de severidad que ordenan la urgencia de respuesta; y los criterios de activación. Todas las definiciones tienen carácter conceptual y analítico; los valores numéricos propuestos son orientativos y quedan sujetos a calibración empírica durante las etapas de implementación y validación.


###### 17.1.5.3.1. El Patrón de Riesgo como Unidad de Análisis

En el contexto del proyecto, se define patrón de riesgo como la especificación declarativa de una situación de seguridad relevante que combina una o más condiciones de riesgo detectadas con criterios de persistencia temporal y un nivel de severidad asignado. El patrón opera como unidad de transición entre el plano de medios (que produce detecciones y trayectorias) y el plano de control (que evalúa situaciones y genera alertas). Su función es transformar las detecciones instantáneas —inherentemente ruidosas y variables entre frames— en eventos operativamente significativos cuya confirmación justifique la generación de una alerta asistiva.

La distinción entre condición de riesgo y patrón de riesgo es funcional y tiene consecuencias arquitectónicas directas. La condición de riesgo es la unidad semántica que el plano de medios detecta (vía OVD y, cuando corresponde, MOT). El patrón de riesgo es la unidad que el plano de control evalúa, agregando criterios de persistencia temporal, severidad y, en los casos composicionales, lógica de activación combinada. La interfaz entre ambos planos se establece en la publicación de detecciones y trayectorias etiquetadas semánticamente como eventos, según la arquitectura event-driven.


###### 17.1.5.3.2. Niveles de Severidad

Cada patrón de riesgo se asocia a un nivel de severidad que refleja el perfil temporal del riesgo, entendido como la velocidad con la que la condición observable puede escalar hacia un incidente y la gravedad potencial de sus consecuencias. En articulación con el framework de métricas, la severidad orienta la urgencia operativa del patrón, las ventanas funcionales de persistencia y los objetivos de TTFD y talert-system; no fija por sí sola el costo computacional del pipeline, que debe distinguirse del tramo Glass-to-Algorithm (G2A).

Se distinguen tres niveles de severidad, cuya granularidad se considera suficiente para el alcance del prototipo experimental. La fundamentación de cada nivel se apoya en la normativa argentina aplicable y en el perfil temporal de consecuencias asociado a cada tipo de exposición.

El nivel crítico corresponde a condiciones con potencial de escalada rápida hacia daño grave o fatal. Los artículos 52 a 57 del Decreto 911/96 establecen medidas de prevención frente al riesgo de caída de personas y trabajos con riesgo de caída a distinto nivel, incluyendo protecciones colectivas, provisión de EPP acorde al riesgo y medidas mínimas para tareas de corta duración. Asimismo, para riesgos asociados a la interacción entre personas, vehículos y maquinaria, el Decreto 911/96 regula la operación de vehículos y maquinaria automotriz en los artículos 246 a 249, y prevé medidas de protección frente a la circulación vehicular en contextos específicos, como la señalización, vallado o cercado de áreas de trabajo en vía pública, la provisión de equipos de alta visibilidad y la protección mediante vallados, señales, luces, vigías u otras medidas eficaces. En ambos casos, la exposición observada puede transformarse con rapidez en un incidente severo, lo que justifica asociar estos patrones con ventanas de persistencia más cortas y objetivos más exigentes de TTFD y dentro del framework evaluativo.

El nivel alto corresponde a condiciones cuya exposición sostenida incrementa de forma significativa el riesgo, aunque con mayor margen de intervención que en el nivel crítico. El Decreto 911/96 regula en los artículos 98 a 102 la provisión, uso, condiciones y vida útil de los equipos y elementos de protección personal; en los artículos 103 a 106, las características generales de la vestimenta de trabajo; y en el artículo 107, la provisión de casco de seguridad para trabajadores que desarrollen tareas en obras de construcción o dependencias con riesgos específicos de accidentes. La ausencia de casco en zona activa de obra no produce por sí misma el incidente, pero elimina una barrera de protección frente a eventos plausibles durante la operación. En esa misma lógica, la permanencia en una zona restringida implica una exposición acumulativa a peligros específicos del sector delimitado.

El nivel medio corresponde a condiciones con riesgo latente o de escalada relativamente más lenta, donde puede exigirse mayor evidencia antes de confirmar la alerta. La obligación de emplear elementos reflectivos o de alta visibilidad en contextos de circulación vehicular se vincula en el Decreto 911/96 con los artículos 63 y 70, referidos respectivamente a trabajos nocturnos y a trabajadores ocupados en la construcción de carreteras en uso. Esta obligación puede complementarse con la Resolución SRT 299/2011, que establece criterios de registración y constancia de entrega de ropa de trabajo y elementos de protección personal. La ausencia de chaleco reflectivo o indumentaria de alta visibilidad reduce la visibilidad del trabajador ante operadores de vehículos o maquinaria, pero la escalada hacia un incidente depende del movimiento efectivo de esos equipos en la zona, lo que justifica ventanas funcionales más largas que en los niveles precedentes.

Si durante la evaluación experimental se identificara la necesidad de niveles adicionales de granularidad, la taxonomía podría extenderse; sin embargo, para el alcance del prototipo experimental, tres niveles proporcionan un balance adecuado entre expresividad y manejabilidad.


###### 17.1.5.3.3. Criterios de Persistencia Temporal

La persistencia temporal es el mecanismo analítico que define en qué condiciones una detección instantánea se considera un evento confirmado. Su propósito es reducir la tasa de falsas alarmas derivada de la variabilidad inherente a la detección fotograma a fotograma. Como se documentó en el análisis de modelos OVD, el componente OVD introduce variabilidad en los puntajes de confianza y puede producir apariciones espurias entre fotogramas consecutivos, por lo que la confirmación temporal constituye una necesidad operativa.

El criterio de persistencia se conceptualiza como una ventana temporal mínima durante la cual la condición debe observarse de manera sostenida —o con una proporción mínima de detecciones positivas dentro de la ventana— antes de que el patrón se considere activo. La presente sección define estos criterios en términos de duración temporal (segundos) y no de número de fotogramas, dado que la conversión depende del throughput efectivo del pipeline, que a su vez está condicionado por el hardware de inferencia. Esta parametrización en unidades temporales permite que la instancia de análisis y diseño arquitectónico realice la conversión una vez conocido el framerate real del sistema. En congruencia con el framework de métricas, esta ventana expresa y no debe confundirse ni con —subtramo computacional por frame— ni con, que integra además la confirmación operativa del patrón.

Los rangos de persistencia propuestos se derivan del análisis cualitativo de la velocidad de escalada de cada tipo de riesgo y se fijan de modo compatible con los umbrales orientativos del framework de métricas. Para las condiciones de severidad crítica, se proponen ventanas de 2 a 4 segundos, buscando confirmar la exposición con mínima acumulación de evidencia sin sacrificar la capacidad de alerta temprana. Para condiciones de severidad alta, se proponen ventanas de 3 a 5 segundos, que ofrecen mayor evidencia acumulada para reducir falsos positivos sin perder capacidad de respuesta ante una exposición sostenida. Para condiciones de severidad media, se proponen ventanas de 5 a 10 segundos, admitiendo mayor acumulación de evidencia para controlar falsas alarmas en una condición cuya urgencia operativa es relativamente menor.

Conviene precisar que estos rangos tienen carácter analítico y orientativo. Los valores definitivos se calibrarán empíricamente durante la validación experimental (validación), una vez que el pipeline completo esté operativo y se conozca el throughput efectivo. La instancia de análisis y diseño arquitectónico tomará estos rangos como referencia para diseñar los mecanismos computacionales de evaluación de persistencia.

Un aspecto adicional que la instancia de análisis y diseño arquitectónico deberá considerar es el comportamiento de histéresis en la activación y desactivación de patrones. En sistemas de alarmas industriales es habitual que el umbral de activación de una alerta difiera del umbral de desactivación, de modo que una interrupción momentánea de la detección —por oclusión parcial, variabilidad del puntaje de confianza o pérdida temporal del track— no desactive prematuramente un patrón recién confirmado. Esta definición queda planteada como criterio de diseño para la etapa arquitectónica.

Existe una tensión inherente entre la severidad del patrón y la confiabilidad de su activación. Algunos patrones críticos requieren ventanas de persistencia más cortas para responder con la urgencia que su perfil de riesgo demanda. Sin embargo, ventanas más cortas implican menos evidencia acumulada, lo que incrementa la probabilidad de falsos positivos. Este trade-off no tiene resolución analítica a priori y constituye uno de los ejes centrales de calibración empírica de la validación experimental, donde deberá evaluarse la curva de tasa de falsos positivos en función de la duración de la ventana de persistencia para cada patrón.


###### 17.1.5.3.4. Operacionalización Preliminar del Motor de Patrones

La definición conceptual de patrones de riesgo requiere una traducción operativa mínima que permita explicar cómo una detección aislada puede convertirse, en tiempo de ejecución, en una alerta asistiva trazable. Para ello, se introduce el motor de patrones como abstracción lógica del sistema, responsable de evaluar la evidencia visual producida por el detector y determinar el estado de cada patrón definido.

El motor de patrones no se entiende como un modelo de visión ni como parte del detector OVD. Su función es posterior a la inferencia: recibe detecciones normalizadas, timestamps, configuración de prompts, reglas del patrón y, cuando corresponda, información de tracking o de regiones parametrizadas. A partir de esos insumos, aplica criterios de persistencia, severidad, histéresis y relaciones espaciales para decidir si un patrón permanece inactivo, pasa a estado candidato, se confirma o se considera resuelto.

Esta distinción evita tratar una detección puntual como una alerta automática. Una detección indica evidencia visual en un frame o instante determinado; un patrón candidato indica que esa evidencia comenzó a sostenerse o a cumplir una condición contextual; un patrón confirmado indica que se alcanzaron los criterios definidos para generar una alerta registrada; y un patrón resuelto indica que la evidencia dejó de sostenerse durante el intervalo de cierre establecido. De este modo, la alerta queda asociada a una evaluación lógica sobre evidencia acumulada y no a una única salida del modelo.

Para los patrones de Nivel 1, como PR-01 y PR-02, la evaluación puede apoyarse en ventanas temporales de evidencia sin requerir obligatoriamente MOT. En ese caso, la persistencia puede estimarse por proporción de frames positivos, duración mínima de evidencia o continuidad aproximada de detecciones relevantes. Si se requiere atribuir la condición a una persona individual durante toda la secuencia, será necesario incorporar MOT o un mecanismo equivalente de asociación temporal. Para los patrones de Nivel 2, la evaluación agrega reglas espaciales intra-frame, como proximidad, solapamiento o relación vertical entre entidades. Para los patrones de Nivel 3, la evaluación exige relaciones sostenidas entre entidades o entre una entidad y una zona parametrizada, por lo que el seguimiento temporal adquiere mayor importancia metodológica.

La histéresis forma parte del comportamiento esperado del motor. Un patrón no debería activarse por una detección espuria ni cerrarse por una pérdida momentánea del detector, una oclusión breve o una caída puntual de confianza. Por ello, los criterios de activación y desactivación pueden utilizar ventanas diferentes: la activación exige evidencia suficiente para confirmar el patrón, mientras que la desactivación puede requerir ausencia sostenida de evidencia durante un intervalo mínimo. Esta separación reduce oscilaciones de estado y evita alertas repetidas sobre una misma situación.

En esta etapa, el motor de patrones queda definido como una estructura lógica preliminar y no como una implementación cerrada. La instancia de análisis y diseño arquitectónico deberá traducir esta definición en componentes, contratos, eventos y configuraciones concretas; la implementación del prototipo experimental deberá implementarla en el prototipo experimental; y la validación experimental deberá calibrar empíricamente sus umbrales, ventanas e histéresis. Con esta delimitación, se busca cerrar la brecha entre patrón conceptual y evaluación en runtime, hasta que queden completamente definidas en el diseño arquitectónico.


###### 17.1.5.3.5. Catálogo de Patrones de Riesgo

La Tabla 24 presenta el catálogo de patrones de riesgo asociados a las condiciones seleccionadas. Para cada patrón se especifica la condición o condiciones de activación, el nivel de severidad, el rango de persistencia temporal orientativo, el perfil temporal del riesgo que fundamenta la asignación de severidad y el trade-off de falsos positivos asociado.

Tabla 24

Catálogo de patrones de riesgo del prototipo E-OVRT-VDP


| Patrón | Cond. | Severidad | Persistencia | Criterio de activación | Perfil temporal del riesgo | Trade-off FP |
| --- | --- | --- | --- | --- | --- | --- |
| PR-01 | CR-01 | Alto | 3–5 s | Persona detectada sin casco durante el intervalo mínimo | Exposición sostenida a caída de objetos o impactos en zona activa de obra; incidente posible ante evento desencadenante (Decreto 911/96, arts. 50, 98–102 y 107). | Moderado |
| PR-02 | CR-02 | Medio | 5–10 s | Persona detectada sin chaleco o indumentaria de alta visibilidad en zona de circulación durante el intervalo | Riesgo de atropello o interferencia operacional por baja visibilidad; escalada dependiente del movimiento efectivo de vehículos o maquinaria (Decreto 911/96, arts. 47, 63 y 70). | Bajo |
| PR-03 | CR-03 | Crítico | 2–4 s | Persona en posición elevada sin sistema anticaídas durante el intervalo | Caída a distinto nivel con consecuencia potencialmente fatal; requiere respuesta temprana ante exposición en altura sin protección suficiente (Decreto 911/96, arts. 52, 54–56 y 112). | Elevado |
| PR-04 | CR-04 | Crítico | 2–4 s | Persona próxima a borde desprotegido durante el intervalo | Caída a distinto nivel desde abertura, borde o plataforma sin protección colectiva eficaz (Decreto 911/96, arts. 52 y 54–56). | Elevado |
| PR-05 | CR-05 | Crítico | 2–4 s | Maquinaria y peatón co-detectados por debajo del umbral de distancia mínima durante el intervalo | Atropello, aplastamiento o contacto peligroso por interacción próxima entre peatones, vehículos y maquinaria de obra (Decreto 911/96, arts. 47, 61, 70, 71 y 246–249; Ley 19.587, arts. 8 y 9). | Elevado |
| PR-06 | CR-06 | Alto | 3–5 s | Persona detectada dentro del polígono de zona restringida durante el intervalo | Exposición sostenida a riesgos propios de una zona señalizada, delimitada, de exclusión, de seguridad o de acceso restringido (Decreto 911/96, arts. 66–69, 95(a), 139, 140(e)–(f), 156 y 176). | Moderado |

Nota. Los rangos de persistencia temporal son orientativos y quedan sujetos a calibración empírica durante la validación experimental, una vez conocido el throughput efectivo del pipeline. La columna “Trade-off FP” indica cualitativamente el riesgo de falsos positivos asociado a la brevedad de la ventana de persistencia. Los artículos normativos referenciados en la columna “Perfil temporal del riesgo” fundamentan la severidad asignada a cada patrón a partir del tipo de exposición, la barrera preventiva omitida y la potencialidad de daño; no definen por sí mismos los umbrales computacionales de activación, distancia, persistencia o latencia del sistema. Fuente: Elaboración propia basada en el análisis normativo de la Ficha-SH, el Decreto 911/96 y la Ley 19.587.


###### 17.1.5.3.6. Criterios de Activación Combinada para Condiciones de Nivel 3

Los patrones PR-05 y PR-06, asociados a condiciones composicionales de Nivel 3, requieren criterios de activación que evalúen relaciones espaciales o de contención entre entidades detectadas independientemente. Los criterios se definen a continuación a nivel conceptual; su materialización en reglas computacionales evaluables corresponde a la instancia de análisis y diseño arquitectónico.

PR-05 — maquinaria en proximidad a peatones. La activación requiere la detección simultánea de al menos una entidad clasificable como maquinaria de obra —por ejemplo, excavadora, retroexcavadora, camión volquete, grúa u otra maquinaria pesada— y al menos una persona, cuyas detecciones presenten una relación de proximidad inferior a un umbral configurable. Como aproximación inicial para el prototipo, puede evaluarse la distancia euclidiana entre puntos representativos de las detecciones en coordenadas de imagen, tales como centroides de bounding boxes o puntos medios inferiores. Sin embargo, esta métrica debe interpretarse como una medida geométrica 2D aproximada y no como una distancia física real, dado que la perspectiva de cámara altera las distancias aparentes en la imagen. Durante la implementación podrán evaluarse métricas alternativas, como la distancia mínima entre bordes de bounding boxes, la distancia entre puntos de apoyo proyectados al plano de suelo o, cuando la cámara lo permita, una distancia corregida mediante calibración u homografía. La evaluación debe sostenerse durante el intervalo de persistencia definido para el patrón, lo que implica que el módulo MOT mantenga trayectorias suficientemente estables de las entidades involucradas a lo largo de los frames consecutivos.

PR-06 — persona en zona restringida. La activación requiere la detección de al menos una persona cuya posición representativa se encuentre contenida dentro de un polígono predefinido que represente la zona restringida. Para zonas definidas sobre el plano del suelo, resulta preferible utilizar el punto medio inferior del bounding box como aproximación del punto de apoyo de la persona, en lugar del centroide de la caja, aunque ambas alternativas podrán compararse durante la implementación. El polígono debe ser configurable por el operador como parte de la parametrización del sistema, no como parte del prompt OVD. La definición de zonas restringidas mediante polígonos en coordenadas de imagen presupone una cámara fija o, en su defecto, algún mecanismo de recalibración o compensación de movimiento de cámara. Para el alcance del prototipo experimental, se asume el uso de cámaras fijas. La condición requiere que la permanencia dentro del polígono se sostenga durante el intervalo de persistencia, lo cual implica seguimiento temporal mediante el módulo MOT cuando la persistencia se compute por entidad individual. La instancia de análisis y diseño arquitectónico debe diseñar tanto el mecanismo de definición de polígonos como la lógica de evaluación de contención punto-en-polígono.

Ambos patrones dependen del módulo MOT en la medida en que la evaluación de relaciones sostenidas en el tiempo requiere trayectorias estables de los objetos rastreados durante el intervalo de persistencia. Los ID switches, pérdidas temporales de track y reasociaciones erróneas pueden generar interrupciones espurias en la evaluación del patrón o reinicios indebidos de la ventana de persistencia. Por ello, estos errores deben contemplarse en el diseño del módulo de razonamiento contextual durante la instancia de análisis y diseño arquitectónico y cuantificarse en la evaluación experimental de la validación experimental.


###### 17.1.5.3.7. Frontera Explícita con la Instancia de Análisis y Diseño Arquitectónico

El desarrollo de esta sección deja tres insumos directos para la instancia de análisis y diseño arquitectónico: el catálogo de condiciones de riesgo clasificado por niveles de complejidad (Tabla 23), el catálogo de patrones con severidad y persistencia temporal orientativa (Tabla 24), y los criterios conceptuales de activación combinada para PR-05 y PR-06. Estos últimos incluyen el supuesto de cámara fija para la evaluación de zonas restringidas, la necesidad de definir métricas de proximidad y contención espacial, y la conveniencia de incorporar mecanismos de histéresis para evitar activaciones o desactivaciones espurias ante detecciones intermitentes.

Sobre esa base, la instancia de análisis y diseño arquitectónico deberá materializar el esquema declarativo de patrones, el motor de evaluación, la parametrización de zonas restringidas, la lógica de proximidad entre entidades, la lógica de contención punto-en-polígono, los mecanismos computacionales de persistencia temporal y el tratamiento de errores asociados al seguimiento, como pérdidas temporales de track o cambios de identidad. En particular, deberá definir cómo se traducen los criterios conceptuales en reglas operativas configurables, incluyendo la selección de puntos representativos de las detecciones, las métricas geométricas aplicables en coordenadas de imagen y, si correspondiera, mecanismos de calibración o compensación de perspectiva.

La instancia de análisis y diseño arquitectónico podrá establecer valores iniciales configurables para umbrales espaciales, ventanas temporales y criterios de activación/desactivación, con el fin de implementar y ensayar el sistema. Sin embargo, la calibración empírica final de esos umbrales y ventanas corresponde a la validación experimental, bajo el framework cuantitativo definido en el framework de métricas.


##### 17.1.5.4. Protocolo de Diseño y Evaluación de Prompts OVD

Esta sección establece el marco metodológico para el diseño, la variación sistemática y la evaluación empírica de los prompts textuales que operan como interfaz de consulta del modelo OVD. Se apoya en la evidencia sobre sensibilidad a la formulación del prompt documentada en el análisis de modelos OVD y en antecedentes de la literatura que muestran que el desempeño de modelos visión-lenguaje y detectores open-vocabulary puede verse afectado por la redacción de la consulta textual y por la forma en que esta se transforma en representaciones textuales para la detección (Du et al., 2022; Zhou et al., 2022). Asimismo, toma como referencia protocolos de evaluación recientes orientados a examinar limitaciones de los detectores OVD ante atributos de granularidad fina, vocabularios dinámicos, negativos difíciles, comprensión posicional y relaciones entre objetos (Bianchi et al., 2024; Yao et al., 2024). Su objetivo es sistematizar el proceso de selección de prompts, reducir la arbitrariedad y dejar documentadas las decisiones de formulación con evidencia empírica. El protocolo se articula con el framework definido en el framework de métricas, de la cual toma las métricas de evaluación y los criterios operativos aplicables al componente OVD.


###### 17.1.5.4.1. Sensibilidad a la Formulación del Prompt como Variable del Sistema

El análisis de modelos OVD documentó que los modelos de detección open-vocabulary presentan sensibilidad a variaciones en la formulación de las consultas textuales. Esta observación es consistente con antecedentes de la literatura sobre modelos visión-lenguaje, que muestran que cambios leves en la redacción del prompt pueden producir variaciones importantes en el desempeño, especialmente en modelos que operan mediante alineación entre representaciones visuales y textuales (Zhou et al., 2022). En OVD, esta sensibilidad se vincula con el hecho de que las categorías pueden consultarse mediante embeddings textuales generados por el encoder de un modelo visión-lenguaje preentrenado, que luego se alinean o comparan con representaciones visuales de regiones o propuestas de objetos (Gu et al., 2021). En este marco, la formulación del prompt no constituye un detalle accesorio: se ha mostrado que el class text embedding puede generarse a partir de prompts ingresados al encoder textual, que el diseño del prompt requiere ajuste cuidadoso, y que estrategias de prompt learning desarrolladas para clasificación de imágenes pueden resultar subóptimas cuando se trasladan directamente a la detección de objetos, por lo que la optimización de prompts requiere evaluación específica para la tarea de detección (Du et al., 2022).

Investigaciones recientes muestran además que la evaluación de detectores OVD se vuelve especialmente exigente cuando intervienen atributos de granularidad fina, vocabularios dinámicos y clases negativas semánticamente cercanas. El benchmark FG-OVD evalúa la capacidad de los detectores para detectar, distinguir y asignar descripciones finas a objetos en presencia de hard-negative classes, considerando propiedades como color, patrón y material, y evidencia que muchos modelos OVD presentan dificultades para capturar y diferenciar detalles finos (Bianchi et al., 2024). Por su parte, OVDEval documenta limitaciones en comprensión de atributos, posición y relaciones entre objetos, y propone NMS-AP como métrica complementaria para evitar resultados engañosos del AP tradicional en evaluaciones con etiquetas de granularidad fina (Yao et al., 2024). De manera complementaria, trabajos recientes muestran que la incorporación de clases negativas semánticamente relacionadas durante el entrenamiento puede mejorar la discriminación del detector; aunque esta técnica excede el alcance del presente proyecto —que trabaja con modelos preentrenados y sin reentrenamiento específico—, su hallazgo refuerza indirectamente la hipótesis de que la composición semántica del vocabulario considerado por el modelo puede influir sobre su desempeño (Kim et al., 2024).

En conjunto, estas evidencias justifican tratar el diseño de prompts como una variable de ingeniería del sistema, que debe gestionarse con un rigor comparable al de las decisiones de arquitectura, selección de modelos o definición de métricas. El protocolo que se presenta a continuación busca ordenar ese proceso para el dominio específico de detección de condiciones de riesgo en construcción civil.


###### 17.1.5.4.2. Estrategia de Variación Sistemática

Para cada condición de riesgo del catálogo (Tabla 23) se diseñan múltiples variaciones de prompt que difieren a lo largo de ejes controlados. La variación sistemática permite identificar qué formulaciones logran la mejor alineación semántica con las características visuales del dominio y documenta las decisiones de selección con evidencia reproducible. Se definen cuatro ejes principales.

Estructura sintáctica. El primer eje comprende variaciones en la organización de los elementos de la consulta, incluyendo frases nominales simples, oraciones descriptivas con contexto y variaciones en el uso de artículos, preposiciones o modificadores. Por ejemplo, para la detección de casco, las formulaciones “hard hat”, “person wearing hard hat” y “safety helmet on worker” difieren en estructura gramatical, aunque refieren a conceptos visualmente relacionados. Los encoders textuales utilizados por modelos visión-lenguaje y detectores OVD pueden producir representaciones distintas ante formulaciones diferentes, incluso cuando estas remiten a una misma categoría o atributo visual. Esta sensibilidad ha sido documentada en modelos visión-lenguaje, donde cambios leves en la redacción del prompt pueden impactar significativamente el desempeño (Zhou et al., 2022), y también en el contexto de OVD, donde el embedding textual de clase depende de los prompts ingresados al encoder textual y requiere ajuste específico para la tarea de detección (Du et al., 2022).

Se incluyen además variaciones con template, como “a photo of a [CLASS]”. Esta decisión se fundamenta en el uso habitual de templates en modelos tipo CLIP, donde transformar una etiqueta aislada en una descripción textual breve puede reducir la brecha entre nombres de clase y textos naturales observados durante el preentrenamiento, y mejorar el desempeño frente al uso de la etiqueta sin contexto (Radford et al., 2021). En consecuencia, el protocolo compara prompts con y sin template, sin presuponer a priori cuál formulación resultará superior para el dominio específico de seguridad en construcción.

Nivel de especificidad del vocabulario. El segundo eje comprende variaciones en la granularidad de los términos utilizados, desde vocabulario genérico hasta terminología específica del dominio de construcción. Por ejemplo, “person”, “worker” y “construction worker” representan distintos niveles de especificidad semántica para referirse a entidades humanas observables en una escena de obra. La hipótesis metodológica es que términos más específicos pueden mejorar la precisión en el dominio al reducir la ambigüedad de la consulta y aproximarla al contexto visual de obra. Sin embargo, también pueden reducir el recall si la formulación elegida resulta demasiado restrictiva o menos compatible con las representaciones textuales aprendidas por el modelo durante el preentrenamiento. Por ello, la selección entre vocabulario genérico y vocabulario específico no se asume como una decisión evidente, sino como una variable experimental del diseño de prompts. Esta expectativa se fundamenta en que, en los modelos OVD, las categorías consultadas dependen de representaciones textuales generadas a partir del prompt y alineadas con representaciones visuales del detector (Gu et al., 2021). Asimismo, la literatura sobre prompt learning para OVD muestra que la formulación textual de las clases requiere ajuste específico para la tarea de detección, por lo que variaciones léxicas aparentemente menores pueden afectar el desempeño y deben evaluarse empíricamente (Du et al., 2022).

Estrategia de detección. El tercer eje distingue entre formulaciones directas y formulaciones indirectas o descompuestas. En las formulaciones directas, el prompt intenta describir la condición de riesgo completa, incluyendo presencia o ausencia del elemento relevante; en las indirectas, el detector identifica entidades visibles por separado y la evaluación de la condición se reconstruye mediante lógica externa al modelo OVD. Esta distinción no es meramente terminológica: define dos modos de consulta con implicancias diferentes sobre precisión, costo computacional y complejidad de integración en el pipeline. La distinción resulta pertinente porque los modelos OVD permiten consultar categorías o descripciones mediante entradas textuales, pero no necesariamente resuelven de forma robusta todos los atributos, posiciones y relaciones espaciales implicados en una condición compuesta (Gu et al., 2021; Yao et al., 2024).

La elección entre ambas estrategias está condicionada por la dificultad práctica de evaluar condiciones formuladas en términos de ausencia visible. Mientras la estrategia directa intenta describir de manera íntegra la condición de riesgo, la indirecta opera con prompts de presencia pura —por ejemplo, “person” y “hard hat” como consultas separadas— y traslada al sistema la responsabilidad de asociar detecciones y verificar relaciones geométricas. El beneficio potencial en robustez semántica se compensa, sin embargo, con mayor complejidad de razonamiento y una posible carga adicional de inferencia por fotograma, cuya magnitud deberá verificarse frente al presupuesto de latencia definido en el framework de métricas. La estrategia indirecta resulta especialmente pertinente para condiciones cuya evidencia visual es la ausencia de un EPP —CR-01, CR-02, CR-03— y para condiciones que requieren evaluación de relaciones espaciales intra-frame —CR-03, CR-04—.

El protocolo de evaluación de la Sección 17.1.5.4.5 compara empíricamente ambas estrategias para todas las condiciones en que sean aplicables, sin presuponer la superioridad de ninguna. La instancia de análisis y diseño arquitectónico deberá materializar la lógica de asociación espacial requerida por la estrategia indirecta y determinar si su costo computacional adicional es compatible con las restricciones operativas del sistema.

Composición del vocabulario activo. El cuarto eje evalúa cómo el conjunto de prompts simultáneamente activos en el vocabulario del detector afecta el desempeño de cada prompt individual. El benchmark FG-OVD muestra que la evaluación de detectores open-vocabulary se vuelve especialmente exigente cuando el vocabulario incluye clases negativas de granularidad fina, es decir, descripciones semánticamente cercanas al prompt objetivo pero referidas a categorías o atributos distintos. En ese escenario, varios modelos OVD presentan dificultades para detectar, distinguir y asignar correctamente descripciones finas en presencia de hard-negative classes (Bianchi et al., 2024).

En el contexto de E-OVRT-VDP, donde el sistema busca simultáneamente múltiples condiciones y entidades —por ejemplo, “hard hat”, “person”, “reflective vest” y “scaffolding”—, se plantea la hipótesis de que prompts semánticamente próximos pueden competir entre sí y generar confusiones de clasificación. Por ello, este eje propone evaluar el desempeño de cada prompt tanto en aislamiento como dentro del vocabulario completo del sistema.

Implicancias del tamaño del vocabulario activo. El número total de prompts simultáneamente activos en el vocabulario del detector puede tener consecuencias tanto sobre la latencia de inferencia como sobre la precisión de la detección. Desde la perspectiva computacional, los modelos difieren en la forma en que procesan el vocabulario textual, por lo que el impacto del tamaño del vocabulario no debe asumirse uniforme entre arquitecturas. Esto puede observarse con dos ejemplos: por un lado, los modelos de la familia YOLO orientados a detección open-vocabulary adoptan estrategias de precomputación o reparametrización de embeddings textuales para favorecer una inferencia eficiente. YOLO-World utiliza un paradigma prompt-then-detect, en el que los prompts definidos por el usuario pueden codificarse previamente como un vocabulario offline y luego reparametrizarse como pesos del modelo para el despliegue (Cheng et al., 2024). En una línea similar, YOLOE propone una estrategia de alineación región-texto reparametrizable —RepRTA— que refina embeddings textuales preentrenados mediante una red auxiliar liviana y permite reparametrizar esa información en la cabeza de clasificación durante la inferencia, reduciendo el costo asociado al procesamiento textual en tiempo de ejecución (Wang et al., 2025). Esto no implica necesariamente que el costo total de inferencia sea completamente independiente del tamaño del vocabulario, ya que pueden existir efectos residuales asociados a la cabeza de predicción, el número de categorías activas, el postprocesamiento o la implementación concreta. Sin embargo, estas arquitecturas desplazan una parte relevante del costo textual fuera del ciclo de inferencia por imagen o frame, lo que resulta particularmente pertinente para un sistema orientado a tiempo real. Por otro lado, Grounding DINO recibe como entrada un par imagen-texto y, para tareas de detección de objetos, concatena los nombres de categorías como texto de entrada. Su arquitectura incluye un backbone textual —por ejemplo, BERT—, módulos de fusión imagen-texto, selección de consultas guiada por lenguaje y decodificación cross-modal. En consecuencia, cuando el vocabulario activo crece, aumenta también la longitud/tokenización de la entrada textual y el costo asociado al procesamiento y fusión de esas representaciones, salvo que se implementen mecanismos específicos de precomputación o caché de embeddings (Liu et al., 2024).

Estas diferencias arquitectónicas tienen consecuencias directas sobre cuántos prompts pueden mantenerse activos simultáneamente dentro del presupuesto de latencia del sistema. Por ello, la selección del vocabulario activo deberá evaluarse junto con el modelo OVD elegido, la sintaxis concreta de los prompts, la resolución de entrada y el hardware de inferencia disponible.


###### 17.1.5.4.3. Consideraciones sobre el Idioma de los Prompts

Los modelos OVD candidatos analizados en el análisis de modelos OVD —Grounding DINO, YOLO-World, YOLOE, Florence-2 y OWL-ViT— se apoyan en arquitecturas visión-lenguaje donde la entrada textual cumple un rol central. Grounding DINO procesa pares imagen-texto y utiliza un backbone textual basado en BERT; YOLO-World emplea un encoder textual tipo CLIP; YOLOE utiliza MobileCLIP-B(LT) para codificar prompts textuales; OWL-ViT transfiere modelos imagen-texto preentrenados a detección open-vocabulary; y Florence-2 opera mediante una representación unificada basada en prompts para múltiples tareas de visión y visión-lenguaje (Liu et al., 2024; Cheng et al., 2024; Wang et al., 2025; Minderer et al., 2022; Xiao et al., 2024).

La decisión de formular los prompts primarios en inglés se fundamenta en la centralidad de ese idioma en varios de los modelos y corpus visión-lenguaje utilizados como base. CLIP fue entrenado sobre pares imagen-texto recolectados de la web y se utiliza ampliamente mediante prompts textuales en inglés; Conceptual Captions se construyó a partir de páginas web en inglés y filtros lingüísticos basados en vocabulario de Wikipedia en inglés; y CC12M amplía la escala de esa línea de recolección para preentrenamiento visión-lenguaje (Radford et al., 2021; Sharma et al., 2018; Changpinyo et al., 2021). Aunque no todos los modelos candidatos publican una caracterización lingüística equivalente de sus datos de entrenamiento, la evidencia disponible justifica utilizar el inglés como idioma primario de consulta para favorecer la compatibilidad con los patrones lingüísticos dominantes del preentrenamiento. Esta decisión tiene una implicación práctica relevante: la plataforma se desarrolla en un contexto académico argentino y constituye un prototipo experimental, no un sistema productivo. En consecuencia, el idioma natural de trabajo de operadores e investigadores es el español, mientras que la capa de consulta del detector se formulará primariamente en inglés para favorecer la alineación con los modelos candidatos. En el prototipo experimental, la traducción de las descripciones de condiciones de riesgo al inglés se realiza manualmente durante la fase de diseño de prompts.

Como línea complementaria de evaluación, podrá explorarse la ejecución de prompts formulados directamente en español o mediados por traducción automatizada, con el fin de cuantificar la eventual degradación asociada a la brecha lingüística y documentar si alguno de los modelos candidatos ofrece soporte multilingüe funcional para el dominio. De realizarse, estas pruebas corresponderán a la validación experimental y constituirán una contribución adicional al análisis de viabilidad del sistema.


###### 17.1.5.4.4. Catálogo de Prompts Candidatos

El catálogo de prompts candidatos define las formulaciones previstas para evaluar las condiciones de riesgo seleccionadas. Para las condiciones de Nivel 1 y Nivel 2 se contemplan formulaciones directas, variantes léxicas y estrategias indirectas o descompuestas, según el tipo de evidencia visual que se busca activar en el modelo. Por ejemplo, una condición como ausencia de casco puede evaluarse mediante consultas directas orientadas a identificar una “persona sin casco” o mediante variantes que busquen evidencias positivas de “casco de seguridad” sobre la región cefálica. De forma similar, una condición asociada al chaleco reflectivo puede abordarse mediante prompts como “persona con chaleco de seguridad” o formulaciones equivalentes vinculadas a ropa de alta visibilidad.

En el caso de las condiciones de Nivel 3, no se proponen prompts integrados como una única consulta OVD, dado que su evaluación requiere razonamiento contextual sobre múltiples entidades o relaciones espaciales. Por ello, se consideran prompts orientados a detectar las entidades componentes, cuyos resultados podrán ser utilizados posteriormente por el motor de patrones. El catálogo completo de prompts candidatos y sus variantes se desarrolla en el Anexo C en la Tabla C.1.

La inclusión de prompts candidatos para CR-03 y CR-04 no implica que ambas condiciones dispongan de soporte completo de evaluación en datasets públicos. En estos casos, los prompts permiten explorar formulaciones posibles y detectar entidades o estados visuales parciales, pero la validación del patrón completo depende de contar con datos que representen la condición operacionalizada. Por ello, los resultados sobre CR-03 y CR-04 deberán distinguir explícitamente entre desempeño del prompt sobre componentes visuales y evaluación integral de la condición de riesgo.


###### 17.1.5.4.5. Protocolo de Evaluación de Prompts

El protocolo de evaluación tiene por objetivo determinar, para cada condición de riesgo y cada modelo OVD candidato, qué formulación de prompt ofrece el mejor desempeño dentro del framework adoptado para el componente OVD, con lectura prioritaria sobre AP@0.5 y Precision/Recall en el punto operativo declarado. Su diseño se fundamenta en prácticas de evaluación documentadas en la literatura reciente, particularmente FG-OVD y OVDEval (Bianchi et al., 2024; Yao et al., 2024), adaptadas al alcance y los recursos de un proyecto académico. Las métricas, los criterios de reporte y los umbrales orientativos se definen en el framework de métricas; el presente protocolo describe la estructura procedural de las pruebas de prompts dentro de ese marco. Se organiza en cinco fases.

Fase 1 - Preparación del dataset de evaluación. Para cada condición de riesgo, se selecciona un subconjunto del inventario de datasets documentado en la estrategia de datos, benchmarks y partición que contenga imágenes o frames con anotaciones de verdad fundamental o ground truth relevantes para la condición evaluada. La selección sigue el principio de representatividad, de modo que el subconjunto incluya variación en iluminación, ángulo de cámara, grado de oclusión y escala de los objetos de interés, dentro de lo que los datos disponibles permitan.

Cuando el ground truth existente no cubra directamente la condición —por ejemplo, si el dataset anota “casco” pero no “persona sin casco”—, se generarán anotaciones complementarias sobre un conjunto acotado de imágenes, garantizando acuerdo interanotador mediante doble anotación independiente sobre al menos un 20% del conjunto. Para etiquetas categóricas sobre unidades previamente definidas se calculará el coeficiente kappa de Cohen como indicador de confiabilidad interanotador (Cohen, 1960); cuando la anotación involucre localización espacial mediante bounding boxes, el acuerdo se evaluará además mediante criterios de solapamiento geométrico, como IoU promedio o proporción de coincidencias por encima de un umbral IoU predefinido.

Como objetivo operativo de esta evaluación comparativa se procurará contar con al menos 200 instancias positivas anotadas por condición, complementadas con casos negativos o imágenes sin la condición objetivo cuando sean necesarios para estimar precisión, falsos positivos y desempeño frente a confusores. Este piso no reemplaza los criterios globales de cobertura definidos en la estrategia de datos, sino que fija un mínimo razonable para comparar variaciones de prompt dentro del proyecto. Si la disponibilidad de datos no permitiera alcanzar ese objetivo, se documentará el tamaño efectivo del subconjunto evaluado y se reportarán intervalos de confianza junto con las métricas obtenidas.

Fase 2 - Definición de la matriz experimental. Se construye la matriz de combinaciones a evaluar, donde cada celda corresponde a una tupla (modelo OVD, condición de riesgo, variación de prompt, contexto de vocabulario). El último término responde al eje de composición de vocabulario definido en la Sección 17.1.5.4.2, y distingue dos condiciones experimentales por prompt: evaluación en aislamiento, donde el prompt —o el conjunto mínimo de prompts requerido por la estrategia indirecta o descompuesta— es el único vocabulario activo del modelo, y evaluación en contexto completo, donde el prompt opera junto con los demás prompts activos del sistema.

Los hiperparámetros del modelo —umbral de confianza, umbral de NMS— se fijan a valores constantes durante toda la evaluación para garantizar comparabilidad entre variaciones de prompt. Si se evalúan múltiples umbrales, estos se documentan como variable adicional de la matriz.

Fase 3 - Ejecución sistemática. Para cada combinación de la matriz, se ejecuta la inferencia sobre el dataset de evaluación correspondiente, registrando para cada imagen las detecciones producidas con sus coordenadas de bounding box, puntaje de confianza y etiqueta asignada por el modelo. La ejecución se realiza en condiciones controladas, manteniendo constantes el hardware, la resolución de entrada y la configuración de pre-procesamiento. Los resultados se almacenan en formato estructurado que permita el cálculo posterior de métricas y la reproducción de los experimentos.

Fase 4 - Cálculo de métricas. Para cada tupla (modelo, condición, prompt, contexto de vocabulario), se calculan las métricas definidas en el framework de métricas para el componente OVD. Se registra también el puntaje de confianza medio de las detecciones verdaderas positivas como indicador complementario de la estabilidad de la respuesta del modelo ante cada formulación de prompt.

Para las condiciones evaluadas con estrategia indirecta o descompuesta, se calculan también las métricas de cada entidad componente por separado, de modo que pueda identificarse si la degradación proviene de la detección de las entidades individuales, del atributo visual evaluado o de la lógica de asociación.

Fase 5 - Análisis comparativo y selección. Se construye una matriz de resultados que permite identificar, para cada condición, la combinación (modelo, prompt) que maximiza el criterio de selección definido en el framework de métricas. Los resultados se analizan tanto por condición individual como de manera transversal, identificando patrones sistemáticos —por ejemplo, si los prompts con template superan consistentemente a los prompts sin template, o si la estrategia indirecta supera a la directa para condiciones de EPP—. Se documenta también la sensibilidad de cada modelo al contexto de vocabulario, cuantificando la diferencia de desempeño entre aislamiento y contexto completo.

El protocolo produce como salida un registro estructurado de métricas por combinación, que alimenta directamente las decisiones de la instancia de análisis y diseño arquitectónico —selección de prompts primarios para la configuración del sistema— y las conclusiones de la validación experimental —análisis de sensibilidad y robustez frente a variaciones de formulación—. Este registro, junto con los scripts de ejecución y los datasets utilizados, constituye el artefacto de reproducibilidad del protocolo.


##### 17.1.5.5. Síntesis parcial de condiciones, prompts y variantes de prueba

La formulación del prompt se asume como variable experimental del sistema. En OVD, cambios de sintaxis, especificidad o selección léxica pueden modificar el comportamiento del detector, especialmente cuando la condición se formula por ausencia de un elemento, por atributos finos o por composición contextual (Du et al., 2022; Bianchi et al., 2024). Por ello, la instancia de análisis y diseño arquitectónico deberá contrastar familias de prompts antes de congelar la configuración comparativa final.

Para evitar ambigüedades terminológicas, esta sección adopta dos definiciones operativas. La primera es matriz de prompts, entendida como el conjunto acotado de formulaciones alternativas que se ensayan para una misma condición. La segunda es la composición del vocabulario activo, entendida como el conjunto de descripciones, etiquetas o consultas que el modelo evalúa en simultáneo dentro de una corrida determinada. Esta aclaración reemplaza formulaciones más difusas de la versión anterior y deja explícito qué variable se está midiendo cuando se habla del “tamaño” o de la “composición” del vocabulario.

El desarrollo completo de las matrices de prompts, sus variantes y los criterios de prueba se presenta en el Anexo C.


#### 17.1.6. Estrategia de datos, benchmarks y partición


##### 17.1.6.1. Introducción y Alcance


###### 17.1.6.1.1. Propósito y Preguntas Rectoras

La presente sección responde a las preguntas rectoras P-E1-03 y P-E1-08 formuladas en la sección 16.7.6 de la fundamentación teórica. En relación con P-E1-03, construye un inventario crítico de datasets públicos potencialmente utilizables para evaluar el prototipo experimental sobre las condiciones de riesgo definidas en la taxonomía de condiciones de riesgo, patrones y prompts, documentando cobertura, formato, acceso, licencia y restricciones operativas. En relación con P-E1-08, analiza qué colecciones pueden funcionar como insumo de un experimento comparativo acotado de fine-tuning, bajo las condiciones metodológicas fijadas por el framework de métricas para preservar la validez de la comparación entre baseline zero-shot y variante ajustada al dominio.

El propósito operativo de esta sección es cuádruple. Primero, construir un inventario sistematizado de datasets públicos relevantes para detección open-vocabulary en entornos de construcción civil, documentando para cada uno los atributos técnicos, de acceso y de licencia que condicionan su viabilidad. Segundo, establecer un mapeo explícito entre cada dataset candidato y las condiciones de riesgo CR-01 a CR-06 definidas en la taxonomía de condiciones de riesgo, patrones y prompts. Tercero, evaluar la aptitud de cada colección para su eventual uso en experimentos comparativos de ajuste de dominio, si ello resulta metodológicamente viable. Cuarto, fijar las condiciones metodológicas mínimas que cualquier estrategia de partición deberá satisfacer para sostener una comparación válida entre baseline zero-shot y variante fine-tuned, cuando esa comparación aplique.

El análisis parte del reconocimiento, establecido en la fundamentación teórica, de que los modelos OVD preentrenados en colecciones generalistas presentan una brecha de dominio respecto de la construcción civil. Esa brecha no se resuelve únicamente con mayor volumen: también exige distinguir entre condiciones con evidencia visual directa —como CR-01 y CR-02—, condiciones espaciales o de ausencia visual fina —como CR-03 y CR-04— y condiciones relacionales o dependientes de parametrización externa —como CR-05 y CR-06—. En consecuencia, la aptitud de un dataset no se agota en la presencia de una clase aislada, sino que debe leerse en articulación con la taxonomía y el protocolo de evaluación definidos por la taxonomía de condiciones de riesgo, patrones y prompts y el framework de métricas.

El alcance de la sección es metodológico. Elabora un inventario de datasets, explicita criterios de inclusión y exclusión, mapea cobertura contra CR-01–CR-06, analiza compatibilidad con los pipelines de ajuste priorizados y fija condiciones mínimas para su eventual partición y uso experimental. No define todavía la combinación definitiva de datasets, no ejecuta particiones ni campañas de curación o anotación complementaria y no implementa mediciones; esas decisiones corresponden a la instancia de análisis y diseño arquitectónico y su validación empírica a la validación experimental.


###### 17.1.6.1.2. Criterios de Categorización y Exclusión

El inventario de esta sección se organiza en dos categorías con criterio de pertenencia explícito. La primera agrupa los datasets sobre los cuales se ejecutan operaciones directas (descarga, procesamiento, partición y uso experimental). La segunda comprende benchmarks establecidos cuyas particiones de test se emplean para medir el rendimiento de módulos específicos del sistema en condiciones comparables con la literatura. Toda colección que no satisfaga al menos uno de estos dos criterios queda fuera del alcance de la sección.

Categoría 1 — Datasets de gestión directa. Un dataset pertenece a esta categoría si se descarga, procesa y utiliza directamente para evaluación del pipeline OVD en el dominio de construcción civil y/o como insumo del experimento comparativo de fine-tuning. La pertenencia a esta categoría no implica decisión de uso; la confirmación de qué datasets se gestionan efectivamente corresponde a la instancia de análisis y diseño arquitectónico. Los datasets listados en la Sección 17.1.6.2 constituyen el conjunto de candidatos analizados en esta sección.

Categoría 2 — Benchmarks de evaluación de referencia. Un dataset pertenece a esta categoría si es un benchmark establecido cuyas particiones de test se emplearán para medir el rendimiento de módulos específicos del sistema bajo condiciones comparables con la literatura. Cada benchmark incluido debe tener una función explícita dentro del protocolo de evaluación, indicando qué módulo se evalúa con él, en qué etapa se utiliza y qué métricas se obtienen.

Alcance y exclusiones explícitas. Quedan fuera del alcance de la presente sección las colecciones generalistas de gran escala sobre las cuales los modelos OVD fueron preentrenados por sus autores, tales como Visual Genome, LVIS v1.0, Objects365 v2, Open Images V7, entre otras. Estas colecciones no constituyen datos gestionados por el proyecto: no se descargan, procesan ni particionan, sino que se aprovechan indirectamente a través de los pesos públicos de los modelos candidatos. Su documentación corresponde al análisis de el análisis de modelos OVD, donde se describe la procedencia de las capacidades open-vocabulary de cada modelo y las restricciones de licencia asociadas.

También quedan fuera del inventario las colecciones que no satisfacen los criterios mínimos de selección definidos en la Sección 17.1.6.1.3, en particular aquellas sin disponibilidad pública verificable, sin condiciones de uso suficientemente documentadas, con baja pertinencia respecto del dominio de construcción civil, con cobertura insuficiente de las condiciones de riesgo CR-01 a CR-06, o con anotaciones incompletas que impidan su conversión o evaluación bajo el protocolo del proyecto. De igual modo, se excluyen como fuente principal de evaluación los datasets compuestos exclusivamente por imágenes sintéticas sin validación manual o sin contraste documentado con escenas reales, dado que no permiten caracterizar adecuadamente el sesgo de dominio respecto de entornos reales de construcción y podrían comprometer la validez ecológica del protocolo experimental.

Las condiciones de calzado inadecuado, ausencia de guantes o gafas de protección, y obstrucción de pasillos o materiales inestables, aunque presentes en la taxonomía normativa de la fundamentación teórica, no integran el alcance experimental definido en la taxonomía de condiciones de riesgo, patrones y prompts para la Etapa 2. Su análisis de cobertura queda diferido a etapas posteriores, en caso de que se decida ampliar el conjunto de condiciones evaluadas.


###### 17.1.6.1.3. Criterios Metodológicos de Selección y Evaluación

La evaluación de cada dataset candidato se realiza sobre siete dimensiones que derivan del análisis teórico de la fundamentación teórica y de las necesidades operativas del proyecto. Estas dimensiones no tienen pesos fijos a priori; su ponderación relativa depende de la función que la instancia de análisis y diseño arquitectónico asigne al dataset dentro de la estrategia combinatoria. Un dataset orientado a ajuste de dominio priorizaría la pertinencia al dominio (C1) y la cobertura normativa (C2), mientras que uno orientado a preservar capacidades open-vocabulary priorizaría la compatibilidad semántica (C3) y la posibilidad de conversión o integración en los pipelines efectivamente seleccionados.

Tabla 25

Criterios de evaluación para la selección de datasets candidatos


| # | Dimensión | Descripción operativa |
| --- | --- | --- |
| C1 | Pertinencia al dominio | Presencia de escenas de construcción, industria o trabajadores con EPP. Se valoran entornos realistas con variaciones de iluminación, ángulo de cámara y condiciones climáticas. |
| C2 | Cobertura normativa | Proporción de categorías anotadas que se corresponden con alguna condición de riesgo de la taxonomía operacionalizada en la taxonomía de condiciones de riesgo, patrones y prompts, derivada del marco normativo argentino. |
| C3 | Compatibilidad OV | Amplitud del vocabulario, presencia de anotaciones en lenguaje natural o descripciones que permitan consultas semánticas. |
| C4 | Soporte temporal | Existencia de secuencias con entidades persistentes (IDs de trayectoria) o anotaciones cuadro a cuadro, necesarias para la integración con módulos de seguimiento multi-objeto (MOT). |
| C5 | Calidad de anotación | Exhaustividad y consistencia de las anotaciones (cajas delimitadoras, máscaras, relaciones). Se prefieren anotaciones manuales con protocolos de control de calidad documentados. |
| C6 | Condiciones desafiantes | Presencia de oclusiones, escenas nocturnas o de baja iluminación, movimiento, multitudes o cambios de escala que permitan evaluar robustez en condiciones realistas de obra. |
| C7 | Viabilidad técnico-legal | Formato estandarizado o convertible; disponibilidad pública verificada; licencia explícita o declaración pública de uso académico compatible. Cuando la fuente sólo indique “free use” o la licencia no sea visible, el dataset se mantiene como candidato condicional y requiere verificación manual antes de su gestión efectiva. |

Nota. Los criterios C1 a C7 no tienen pesos fijos; su ponderación relativa dependerá de la función asignada al dataset en la instancia de análisis y diseño arquitectónico. Elaboración propia basada en el análisis metodológico de la Etapa 2.


##### 17.1.6.2. Datasets de Gestión Directa (Categoría 1)

Este grupo reúne las colecciones retenidas como candidatas a gestión directa por su relevancia temática y disponibilidad pública, aunque no todas presentan el mismo grado de certeza sobre formato nativo, licencia o alcance exacto de la versión descargable. Por esa razón, el inventario distingue entre especificaciones verificadas en fuente primaria y aspectos que deberán confirmarse antes de la gestión efectiva en la instancia de análisis y diseño arquitectónico. La decisión final sobre cuáles se descargan, convierten y particionan sigue quedando diferida a esa etapa.


###### 17.1.6.2.1. Inventario y Análisis Individual

Tabla 26

Datasets candidatos a gestión directa para EPP y dominio construcción


| Dataset | Imgs / Inst. | Clases principales | Formato | Licencia | Cobertura | Limitaciones |
| --- | --- | --- | --- | --- | --- | --- |
| SH17 (Ahmad y Rahimi, 2025) | 8.099 imgs.; 75.994 inst. | 17 clases (person, helmet, safety-vest, gloves, shoes, glasses y otras partes/elementos de seguridad) | YOLO; Pascal VOC a verificar | CC BY-NC-SA 4.0 | CR-01 directa; CR-02 parcial | Dominio manufactura/industrial. Sin video. No cubre altura. |
| SHEL5K (Otgonbold et al., 2022) | 5.000 imgs.; ≈75,58k labels | 6 clases (helmet, head with helmet, person with helmet, head, person without helmet, face) | Pascal VOC | CC BY 4.0 | CR-01 directa | Sólo casco. Sin color. Sin video. |
| CHV (Wang et al., 2021) | 1.330 imgs.; 9.209 inst. | 6 clases (person, vest, blue/red/white/yellow helmet) | Formato nativo no validado | Uso libre declarado; paper CC BY 4.0 | CR-01 y CR-02 directas | Volumen modesto; términos de redistribución del dataset a verificar. |
| Pictor-PPE (Nath et al., 2020) | 1.472 imgs. nominales; versión pública parcial (~770–780 imgs.) | 3 clases base (worker, hat, vest); compliance W/WH/WV/WHV en tareas derivadas | Formato nativo no validado | No especificada en fuente visible | CR-01 y CR-02 directas | Versión pública parcial; alcance exacto de la fracción pública y licencia a verificar. |
| Construction-PPE (Dalvi et al., 2025) | 1.416 imgs.; 11 clases | 11 clases de PPE, persona y ausencia/incumplimiento de EPP | YOLO | AGPL-3.0 | CR-01 y CR-02 directas; missing PPE explícito | Tamaño pequeño. Copyleft fuerte si se redistribuye. |
| GDUT-HWD (Wu et al., 2019) | 3.174 imgs.; 18.893 inst. | 5 clases (blue, white, yellow, red, none) | Formato nativo a verificar (cajas + label; benchmark SSD/Caffe) | Apache-2.0 visible en repositorio | CR-01 directa (incluye ausencia de casco) | Sólo casco/color. Sin chaleco. Alcance efectivo de la licencia sobre los datos descargables a confirmar. |
| SHWD (njvisionpower, 2024) | 7.581 imgs.; 120.558 inst. | 2 clases operativas (hat, person); positivos y negativos para casco | Pascal VOC | MIT | CR-01 directa | Sólo casco. Sin color. La clase negativa se operacionaliza como person/head sin casco. |
| SODA (Duan et al., 2022) | 19.846 imgs; 286.201 obj. | 15 clases (person, helmet, vest, board, wood, rebar, brick, scaffold, handcart, cutter, ebox, hopper, hook, fence, slogan) | Pascal VOC | Acceso abierto documentado | CR-05 y CR-06 parciales; apoyo contextual a CR-01/CR-02 | No modela relaciones espaciales ni ausencia de EPP. |
| MOCS (An et al., 2021) | 41.668 imgs.; 222.861 inst. | 13 clases de objetos móviles de obra (worker, tower crane, hanging hook, vehicle crane, roller, bulldozer, excavator, truck, loader, pump truck, concrete transport mixer, pile driver, other vehicle) | Multi-type annotation / formato a verificar | CC BY-NC 4.0 + términos adicionales; acceso por solicitud | Maquinaria, trabajadores y contexto dinámico de obra; apoyo parcial para CR-05 | No cubre EPP ni ausencia de EPP. Acceso condicionado por solicitud y términos adicionales. No modela por sí solo la relación espacial de riesgo. |

Nota. La columna “Cobertura” se refiere a la correspondencia directa o parcial con las condiciones de riesgo CR-01–CR-06 definidas en la taxonomía de condiciones de riesgo, patrones y prompts. En Pictor-PPE se distingue entre el tamaño nominal reportado por los autores y la fracción públicamente accesible indicada en la fuente visible. MOCS se incorpora como candidato complementario para contexto de obra y maquinaria, aunque su acceso oficial requiere solicitud previa y no aporta clases de EPP.


###### 17.1.6.2.2. Mapeo a Condiciones de Riesgo

El siguiente mapeo articula el inventario de candidatos a gestión directa con las seis condiciones de riesgo del catálogo CR-01–CR-06 establecido en la taxonomía de condiciones de riesgo, patrones y prompts. La lectura del mapeo distingue entre cobertura directa de la condición, cobertura parcial de entidades o contexto, y brechas de cobertura visual directa. Esta distinción es necesaria porque, en el proyecto, no todas las condiciones se resuelven del mismo modo: algunas dependen principalmente de detección frame-a-frame, mientras que otras requieren razonamiento espacial intra-frame, definición de regiones de interés o integración con MOT y lógica contextual. En todos los casos, la presencia de objetos relevantes en un dataset no equivale necesariamente a una etiqueta nativa del patrón de riesgo completo. Esta distinción resulta especialmente importante para CR-03 y CR-04: la existencia de clases como persona, andamio, plataforma, borde, valla o baranda puede aportar evidencia contextual o entidades auxiliares, pero no alcanza por sí sola para validar trabajo en altura sin sistema anticaídas ni borde elevado desprotegido con personas próximas. Por ello, la tabla diferencia entre datasets que permiten evaluar una condición de manera directa, datasets que sólo aportan componentes visuales parciales para reconstruirla, y condiciones que permanecen como brechas de cobertura dentro del inventario.

Tabla 27

Mapeo de condiciones de riesgo a datasets candidatos a gestión directa


| Código / condición | Descripción | Datasets con cobertura | Brecha / observación |
| --- | --- | --- | --- |
| CR-01 — Persona sin casco | Persona sin casco de seguridad en zona de obra o entorno operativo asimilable. | H17, SHEL5K, CHV, Pictor-PPE, Construction-PPE, GDUT-HWD y SHWD. | Cobertura sólida. Existe redundancia suficiente para casco y ausencia de casco. Algunas colecciones proveen etiqueta negativa explícita o clases de incumplimiento; en otras, la condición puede reconstruirse de forma indirecta. |
| CR-02 — Persona sin chaleco | Persona sin chaleco reflectivo en zona de tráfico, maquinaria o circulación operativa. | SH17, CHV, Pictor-PPE y Construction-PPE. | Cobertura adecuada. CHV y Pictor-PPE aportan persona, chaleco y cumplimiento combinado; Construction-PPE incorpora clases de EPP y ausencia/incumplimiento. SODA contiene helmet/vest/person, pero no etiqueta nativamente la condición de incumplimiento. |
| CR-03 — Trabajo en altura sin anticaídas | Persona en posición elevada sin sistema anticaídas visible. | Ninguno con cobertura directa. SODA puede aportar contexto parcial de obra, pero no anota sistema anticaídas ni condición de altura operativa. | BRECHA. No se identificó un dataset del inventario que combine persona en altura, sistema anticaídas y anotación aprovechable para reconstruir la condición completa. |
| CR-04 — Borde elevado desprotegido | Borde elevado sin baranda, red u otra protección colectiva, con personas próximas. | Ninguno con cobertura directa. SODA aporta layout parcial mediante clases como scaffold o fence, pero no anota borde elevado desprotegido como entidad o relación. | BRECHA. La ausencia de protección colectiva y la proximidad de personas al borde requieren información espacial específica no provista de forma nativa por los datasets inventariados. |
| CR-05 — Maquinaria cerca de peatones | Maquinaria o vehículo de obra circulando u operando en proximidad de peatones o trabajadores. | MOCS aporta trabajadores y maquinaria/vehículos de obra; SODA aporta personas y elementos de contexto/máquinas de obra. | Cobertura parcial. La condición completa depende de razonamiento espacial y temporal externo al dataset. |
| CR-06 — Persona en zona restringida | Persona dentro de zona delimitada, restringida o no habilitada para circulación. | SODA. MOCS puede aportar trabajadores, pero no delimita zonas restringidas ni elementos normativos de acceso. | Cobertura parcial. La condición requiere polígono externo y regla espacial. |

Nota. Elaboración propia basada en el catálogo CR-01–CR-06 de la taxonomía de condiciones de riesgo, patrones y prompts y el inventario de la Tabla 26. “Cobertura directa” indica clases o etiquetas suficientes para evaluar la condición con transformación metodológica defendible; “cobertura parcial” indica entidades o contexto útiles, pero no una etiqueta nativa del patrón de riesgo completo.


###### 17.1.6.2.3. Síntesis de Cobertura Conjunta y Brechas

El análisis individual de los datasets y su mapeo a condiciones de riesgo permite extraer una conclusión de cobertura agregada. Las condiciones de EPP principales del prototipo experimental —CR-01 persona sin casco y CR-02 persona sin chaleco— cuentan con la cobertura más robusta del inventario. CR-01 presenta una cobertura sólida, respaldada por múltiples colecciones independientes centradas en casco, ausencia de casco y cumplimiento de EPP. CR-02 presenta una cobertura adecuada, aunque menos redundante que CR-01, porque depende de un subconjunto menor de datasets que anotan chaleco, persona y/o combinaciones de cumplimiento.

Las condiciones CR-03 —trabajo en altura sin sistema anticaídas visible— y CR-04 —borde elevado desprotegido con personas próximas— mantienen brechas estructurales de cobertura visual directa dentro del inventario actual. No se identifican datasets que combinen, de forma nativa y aprovechable, las entidades, relaciones espaciales y ausencias visuales necesarias para evaluar esas condiciones completas. Por ello, su presencia en el catálogo no debe interpretarse como compromiso de validación plena mediante datasets públicos disponibles, sino como una definición metodológica de condiciones relevantes cuya evaluación queda condicionada a datos complementarios, anotación específica o escenas controladas. En ausencia de ese soporte, sólo corresponde reportar evidencia parcial sobre componentes visuales o reglas espaciales exploratorias, sin atribuir esos resultados al patrón de riesgo completo.

En cambio, CR-05 —maquinaria cerca de peatones— y CR-06 —persona en zona restringida— no carecen por completo de entidades de apoyo. SODA y MOCS aportan contexto de obra, trabajadores, maquinaria o elementos del entorno que pueden ser útiles para aproximar escenarios relacionales. Sin embargo, la condición operativa completa no está anotada como patrón de riesgo nativo y depende de razonamiento composicional externo al dataset, reglas espaciales, definición de regiones de interés o integración con seguimiento temporal.

Considerando el tamaño nominal de las colecciones candidatas de gestión directa, el inventario reúne aproximadamente entre 88,9 mil y 89,6 mil imágenes si se incluye MOCS como candidato condicionado, según se contabilice sólo la porción públicamente accesible de Pictor-PPE o su tamaño nominal completo. Sin MOCS, el volumen operativo preliminar se ubica aproximadamente entre 47,2 mil y 47,9 mil imágenes. Esta distinción es metodológicamente relevante porque MOCS requiere solicitud previa de acceso y verificación de condiciones de uso antes de poder considerarse efectivamente gestionable en la instancia de análisis y diseño arquitectónico.

Puede verse la síntesis de cobertura conjunta por condición de riesgo en la Tabla C.3 del Anexo C.


###### 17.1.6.2.4. Análisis de Viabilidad para Fine-Tuning

Esta sección evalúa la aptitud de los datasets de Categoría 1 como posibles insumos para el experimento comparativo de fine-tuning contemplado en el proyecto. Dicho experimento busca determinar si la adaptación de dominio mediante fine-tuning ligero mejora el rendimiento en categorías de seguridad industrial o construcción civil directamente representadas en los datos —categorías vistas— sin degradar la capacidad de generalización open-vocabulary a categorías no entrenadas —categorías no vistas—. La línea base del prototipo experimental opera con modelos preentrenados en modo zero-shot, y el fine-tuning constituye un experimento comparativo acotado, no el eje central del prototipo. El protocolo de evaluación mide ambas dimensiones simultáneamente, conforme a lo establecido en el framework de métricas. La inclusión de un dataset en la Categoría 1 no implica, por sí misma, que sea igualmente apto para fine-tuning. Algunos datasets presentan una correspondencia directa con las condiciones de EPP priorizadas —especialmente CR-01 y CR-02— y pueden funcionar como insumo de entrenamiento o evaluación. Otros aportan principalmente contexto de obra, maquinaria, trabajadores o elementos del entorno, por lo que su utilidad para fine-tuning depende de la estrategia experimental definida en la instancia de análisis y diseño arquitectónico.

El experimento comparativo de fine-tuning se plantea sobre un máximo de dos modelos. Con base en el análisis de la la sección de entorno experimental, infraestructura y escenarios de evaluación, los modelos priorizados son Grounding DINO y YOLOE, seleccionados por representar los extremos del trade-off entre latencia de inferencia y expresividad semántica identificado en la fundamentación teórica. La confirmación definitiva de cuáles se ajustan efectivamente, qué datasets se emplean como entrenamiento y cuáles se reservan para evaluación corresponde a la instancia de análisis y diseño arquitectónico.

El entrenamiento se ejecutará en el clúster de cómputo de alto rendimiento Mendieta (CCAD-UNC), mientras que la evaluación e inferencia operativa se realizarán en el hardware local documentado en la sección de entorno experimental, infraestructura y escenarios de evaluación. La presente sección sólo necesita esa distinción funcional; el detalle completo del entorno queda remitido a dicha sección.

Compatibilidad de Formato de Anotación. Los modelos OVD candidatos requieren pipelines de datos distintos. En la implementación Open-GroundingDINO, el entrenamiento se organiza en formato ODVG y la validación se ejecuta sobre COCO. En el caso de YOLOE, la vía operativa considerada por el proyecto es el pipeline de Ultralytics, cuyo formato nativo de trabajo es YOLO y admite datasets previamente convertidos. Esto puede verse con más detalle en la tabla C.4 del Anexo C, donde no se equipara abstractamente a todos los modelos OVD, sino que organiza la compatibilidad de formatos en función de los dos pipelines que esta etapa analiza como alternativas principales para el experimento comparativo.

Volumen y Suficiencia para Fine-Tuning. Como antecedente práctico de ajuste ligero, implementaciones públicas de fine-tuning de Grounding DINO muestran que la adaptación al dominio puede ejecutarse con algunos centenares de imágenes, pero también que el modelo puede sobreajustarse rápidamente si el entrenamiento se prolonga sin control (Mallick, 2025). Asimismo, la implementación Open-GroundingDINO documenta un pipeline de entrenamiento que permite adaptar el modelo a datasets personalizados mediante conversión al formato requerido por dicho entorno (Long y Li, 2023). Sobre esa base —y como decisión metodológica propia del proyecto— se mantiene un rango conservador de 500 a 2.000 imágenes anotadas para el split de entrenamiento destinado al experimento comparativo. Este rango no pretende universalidad: funciona como diseño experimental acotado y deberá validarse empíricamente en la validación experimental.

La presente sección no define todavía el subset de entrenamiento definitivo. Su función es establecer si el inventario cuenta con volumen suficiente para construirlo, manteniendo margen para curación, balance de clases y reserva de conjuntos de evaluación disjuntos. La selección concreta de imágenes, la proporción aportada por cada dataset y la separación final entre entrenamiento, validación y evaluación corresponden a la instancia de análisis y diseño arquitectónico.

Desde el punto de vista estrictamente cuantitativo, varios datasets superan holgadamente el rango definido. SODA —19.846 imágenes—, SH17 —8.099 imágenes—, SHWD —7.581 imágenes—, SHEL5K —5.000 imágenes— y GDUT-HWD —3.174 imágenes— ofrecen volumen suficiente para seleccionar subconjuntos curados sin necesidad de utilizar la colección completa (Duan et al., 2022; Ahmad y Rahimi, 2025; NJVisionPower, 2019; Otgonbold et al., 2022; Wu et al., 2019). Esta posibilidad es metodológicamente relevante porque permite controlar balance de clases, calidad de anotación, diversidad visual y separación entre entrenamiento y evaluación.

CHV —1.330 imágenes— y Construction-PPE —1.416 imágenes— se ubican dentro del rango definido para el split de entrenamiento (Wang et al., 2021; Dalvi et al., 2025). Por su tamaño y pertinencia visual, podrían funcionar como insumos de entrenamiento acotado, entrenamiento complementario o evaluación, según la estrategia de partición que se defina en la instancia de análisis y diseño arquitectónico. Pictor-PPE requiere una lectura más cautelosa: su tamaño nominal es de 1.472 imágenes, pero la porción pública preliminarmente identificada se ubica alrededor de 770–780 imágenes (Nath et al., 2020; CIBER Lab, 2020). En ambos escenarios se mantiene dentro del rango operativo, aunque su aporte efectivo deberá confirmarse al momento de la descarga, inspección y curación.

MOCS —41.668 imágenes— supera ampliamente el rango de entrenamiento, pero no debe interpretarse como volumen disponible automáticamente para fine-tuning (An et al., 2021). Su contribución principal no está vinculada a EPP, sino a trabajadores, maquinaria, vehículos y contexto dinámico de obra. Por ello su eventual uso tendría un rol más probable en tareas de contexto, evaluación relacional o apoyo a condiciones como CR-05, antes que como fuente principal para ajuste de las condiciones de EPP.

En síntesis, el inventario presenta suficiencia cuantitativa para construir un subset de entrenamiento acotado dentro del rango definido para el experimento comparativo de fine-tuning, especialmente sobre las condiciones de EPP que integran el núcleo del prototipo —CR-01 y CR-02—. Esta suficiencia no debe extenderse automáticamente a las condiciones complejas del catálogo. En particular, CR-03 y CR-04 no quedan resueltas por el volumen total de imágenes disponibles, ya que su validación requiere anotaciones sobre relaciones espaciales, ausencia visible de protecciones y configuración contextual de la escena. Por ello, la decisión de uso no debe basarse sólo en la cantidad de imágenes. La instancia de análisis y diseño arquitectónico deberá priorizar subconjuntos según cobertura efectiva de las condiciones de riesgo, compatibilidad de formato, claridad de licencia, calidad de anotación y necesidad de preservar conjuntos de evaluación estrictamente disjuntos.


###### 17.1.6.2.5. Análisis Cualitativo de Transferibilidad

La transferibilidad de un dataset al escenario operativo objetivo —construcción civil en condiciones típicas argentinas, obra a cielo abierto o semi-cubierta, iluminación diurna predominante— depende de la similitud entre las condiciones visuales capturadas en el dataset y las del entorno real de despliegue. En esta sección, la transferibilidad se analiza de manera cualitativa: no se estima formalmente el domain shift, sino que se identifican las colecciones con mayor proximidad visual, semántica y contextual respecto de las condiciones de riesgo definidas en la taxonomía de condiciones de riesgo, patrones y prompts.

Desde el punto de vista del contexto de obra, SODA presenta alta transferibilidad estimada, porque fue construido específicamente sobre escenas de sitios de construcción e incluye trabajadores, materiales, maquinaria y elementos de layout relevantes para interpretar el entorno operativo (Duan et al., 2022). MOCS también resulta pertinente para contexto dinámico de obra, trabajadores y maquinaria en movimiento, aunque su aporte se vincula principalmente con condiciones relacionales como CR-05 y no con las condiciones de EPP (An et al., 2021).

Para las condiciones de EPP, CHV y Construction-PPE presentan alta cercanía visual con escenas reales de construcción y son especialmente pertinentes para CR-01 y CR-02, por incluir personas, cascos, chalecos y/o clases explícitas de incumplimiento de EPP (Wang et al., 2021; Dalvi et al., 2025). GDUT-HWD también es transferible para CR-01, dado que se orienta a la detección de uso y color de casco en construcción, aunque no aporta chaleco ni contexto relacional (Wu et al., 2019). SHWD aporta volumen relevante para casco y ausencia de casco, pero su utilidad se concentra en CR-01 (NJVisionPower, 2019).

SH17 ofrece la mayor amplitud de clases de seguridad y puede funcionar como puente de dominio para EPP, aunque su dominio primario es manufactura/industria y no construcción civil (Ahmad y Rahimi, 2025). SHEL5K resulta útil para detección de casco y ausencia de casco, pero su cobertura se concentra en CR-01 (Otgonbold et al., 2022). Pictor-PPE es pertinente para combinaciones de cumplimiento casco/chaleco, aunque su aporte debe interpretarse con cautela por la disponibilidad pública parcial de la colección (Nath et al., 2020; CIBER Lab, 2020).

En síntesis, la mayor transferibilidad contextual corresponde a SODA y MOCS; la mayor transferibilidad para EPP en construcción corresponde a CHV, Construction-PPE y GDUT-HWD; y la mayor amplitud semántica complementaria corresponde a SH17. SHEL5K, SHWD y Pictor-PPE aportan valor específico para casco o cumplimiento básico de EPP, pero con menor capacidad para representar la complejidad completa del escenario operativo. Esta evaluación no define todavía la asignación final de datasets a entrenamiento o evaluación; esa decisión corresponde a la instancia de análisis y diseño arquitectónico y deberá contrastarse empíricamente en la validación experimental.

Estimación de Esfuerzo de Anotación Complementaria. El mapeo de la Tabla 27 identificó dos brechas directas de cobertura: CR-03 —trabajo en altura sin sistema anticaídas visible— y CR-04 —borde elevado desprotegido con personas próximas—. En ambos casos, el inventario no ofrece datasets con anotaciones suficientes para reconstruir la condición completa de manera directa. CR-05 y CR-06, en cambio, disponen de cobertura parcial de entidades y contexto mediante SODA y MOCS, pero podrían requerir datos complementarios si la instancia de análisis y diseño arquitectónico decide evaluar con mayor control el razonamiento espacial, la definición de zonas de riesgo o la persistencia temporal.

Como estimación operativa propia del proyecto, si la instancia de análisis y diseño arquitectónico decidiera habilitar una evaluación complementaria sobre condiciones directamente brechadas, se considera un piso exploratorio de 150 a 200 imágenes por condición. Esto equivale a 300 a 400 imágenes totales para CR-03 y CR-04, no como garantía de validación plena, sino como base mínima para ensayar anotaciones, reglas espaciales y criterios de interpretación sobre escenas relevantes. La anotación manual inicial con cajas delimitadoras en formato COCO se estima entre 2 y 5 minutos por imagen, dependiendo de la densidad de objetos, la complejidad de la escena y la cantidad de clases o entidades a etiquetar.

Bajo ese rango, el esfuerzo manual inicial se ubicaría aproximadamente entre 10 y 33,3 horas-persona. Si se adopta un escenario promedio de 3,5 minutos por imagen, el esfuerzo esperado para la anotación inicial sería de 17,5 a 23,3 horas-persona. Estos valores son aritméticamente consistentes, pero deben interpretarse como una cota inferior: CR-03 y CR-04 no requieren sólo dibujar cajas, sino también interpretar ausencias visuales, relaciones espaciales y condiciones de contexto.

Al incorporar revisión de calidad, resolución de inconsistencias, refinamiento de criterios y normalización final de formato, el esfuerzo operativo completo podría ubicarse de forma más realista en torno a 20–45 horas-persona, dependiendo de la complejidad de las escenas y del nivel de detalle exigido por el protocolo de evaluación. La Sección 17.1.6.2.6 analiza alternativas —como anotación asistida por modelo, curación de imágenes abiertas o grabación en entorno simulado— que podrían reducir o redistribuir ese esfuerzo.


###### 17.1.6.2.6. Alternativas para Datos Complementarios

Las brechas directas de cobertura y las necesidades parciales de razonamiento identificadas en el inventario pueden requerir datos complementarios si la instancia de análisis y diseño arquitectónico decide mantener dentro del alcance experimental condiciones para las cuales la cobertura actual es insuficiente o demasiado indirecta. Se presentan a continuación cinco alternativas en orden de preferencia según viabilidad operativa, madurez de las herramientas y alineación con el alcance de un prototipo experimental académico.

Anotación asistida por modelo. La herramienta Autodistill (Roboflow, 2023, licencia Apache-2.0) permite utilizar modelos OVD como Grounding DINO en modo zero-shot para generar pseudo-anotaciones automáticas sobre imágenes sin etiquetar. El workflow consiste en definir prompts de detección, generar cajas automáticamente y luego revisar y corregir manualmente las predicciones. Esta estrategia transforma la tarea de creación de anotaciones en una tarea de revisión y corrección, reduciendo el esfuerzo estimado en un factor de 2× a 3× según la calidad del modelo sobre las condiciones específicas. Herramientas alternativas con capacidades similares incluyen Grounding SAM (combinación de Grounding DINO con Segment Anything Model) y Label Studio con backends de preanotación automática.

Data augmentation. La aplicación de transformaciones sobre imágenes existentes mediante la biblioteca Albumentations (Buslaev et al., 2020) permite ampliar artificialmente la diversidad del conjunto de datos. Las transformaciones más relevantes para el dominio incluyen variaciones de brillo y contraste, rotaciones leves, recortes aleatorios, desenfoque por movimiento y adición de ruido. Esta técnica incrementa la diversidad visual sin requerir imágenes nuevas, pero no resuelve la ausencia de categorías no representadas; su utilidad es complementaria a la anotación de datos originales, no sustitutiva.

Curación de imágenes de dominio abierto. Plataformas de imágenes abiertas y repositorios académicos contienen material visual de contextos de construcción que, aunque no anotado, puede combinarse con la anotación asistida por modelo. La búsqueda dirigida en repositorios con licencias compatibles (CC BY, CC0) permite generar un corpus de imágenes relevantes que luego se anota con el workflow de la primera alternativa. Esta opción requiere un esfuerzo de curación adicional —verificación de licencia, filtrado de calidad y eliminación de duplicados— pero tiene el potencial de cubrir brechas de cobertura sin necesidad de grabación propia.

Grabación en entorno simulado. La captura de video o imágenes en un entorno controlado —laboratorio o espacio de prácticas del centro educativo— con participantes informados bajo protocolo de consentimiento informado y anonimización de rostros, conforme a la normativa vigente de protección de datos personales (Ley 25.326, 2000), permite generar datos con las condiciones de riesgo específicas que los datasets públicos no cubren. Esta alternativa ofrece control total sobre las condiciones visuales (iluminación, ángulo, EPP utilizado) pero introduce limitaciones de diversidad ambiental y requiere coordinación logística y recaudos éticos (consentimiento informado, anonimización de rostros).

Exclusión de la condición del alcance experimental. Como opción residual, si ninguna de las alternativas anteriores resulta viable dentro del cronograma y los recursos disponibles, las condiciones sin cobertura adecuada se excluirían del alcance experimental con mención explícita como limitación del trabajo. Esta exclusión no afectaría la evaluación de las condiciones de EPP principales, que cuentan con cobertura sólida en el inventario.

La decisión entre estas alternativas corresponde a la instancia de análisis y diseño arquitectónico, considerando el cronograma disponible, la calidad preliminar del modelo zero-shot sobre las condiciones objetivo y la viabilidad logística de la grabación simulada.


###### 17.1.6.2.7. Condiciones para la Partición de Datos

La evaluación comparativa zero-shot vs. fine-tuned requiere que los conjuntos de entrenamiento y evaluación sean estrictamente disjuntos, tal como exige el framework de métricas para sostener la validez de la comparación. El diseño concreto de la partición —qué proporciones se asignan a entrenamiento, validación y evaluación, qué datasets alimentan el subset de entrenamiento y qué colecciones se reservan para test— corresponde a la instancia de análisis y diseño arquitectónico, una vez definidos los modelos seleccionados y la estrategia de adaptación de dominio. La presente sección documenta sólo las condiciones metodológicas que cualquier esquema de partición deberá satisfacer.

Tabla 28

Condiciones metodológicas para la partición de datos


| Condición | Descripción |
| --- | --- |
| Disyunción estricta | Ninguna imagen del split de test debe aparecer en el split de entrenamiento, ni directamente ni mediante data augmentation aplicada sobre imágenes de test. El incumplimiento de esta condición invalidaría la comparación pretrained vs. fine-tuned. |
| Test set compartido | El split de evaluación debe ser idéntico para la línea base pretrained y los modelos fine-tuned, a fin de garantizar comparabilidad directa. |
| Semilla reproducible | Cuando la partición sea aleatoria, debe documentarse la semilla utilizada, de modo que el split pueda regenerarse y verificarse independientemente. |
| Splits oficiales | Cuando exista un split publicado por la fuente (p. ej., CHV en el paper o Construction-PPE en Ultralytics), conviene revisarlo antes de redefinirlo. La instancia de análisis y diseño arquitectónico podrá apartarse de ese esquema si justifica la decisión. |
| Rango de entrenamiento | El split de entrenamiento para fine-tuning se acota a 500–2.000 imágenes, conforme al análisis de suficiencia desarrollado en la sección 17.1.6.2.4. La baseline zero-shot se evalúa siempre sobre el test set congelado. |
| No solapamiento cruzado | Si se combinan múltiples datasets para formar un split unificado, debe verificarse la ausencia de imágenes duplicadas entre colecciones, especialmente entre datasets de PPE web-mined o crowd-sourced que podrían compartir fuentes de origen. |
| Congelamiento previo | El test set debe quedar definido y congelado antes del inicio de cualquier entrenamiento, incluida la aplicación de data augmentation sobre el split de entrenamiento, para evitar data leakage inadvertido. |

Nota. Estas condiciones son requisitos metodológicos; las proporciones concretas de partición y la composición final del subset de entrenamiento corresponden a la instancia de análisis y diseño arquitectónico. Cuando exista una divergencia entre el split publicado por una fuente y las necesidades experimentales del proyecto, la desviación deberá justificarse explícitamente en la bitácora.


###### 17.1.6.2.8. Evaluación de Aptitud por Propósito

La siguiente tabla sintetiza la aptitud de cada dataset candidato para los dos propósitos principales del proyecto —fine-tuning y evaluación—, sin definir todavía su asignación definitiva. La valoración resume los criterios ya desarrollados en las secciones anteriores: cobertura de condiciones de riesgo, pertinencia al dominio, volumen disponible, compatibilidad de formato y restricciones de acceso o uso.

En esta síntesis, la aptitud para fine-tuning se interpreta en relación con el subset de entrenamiento acotado previsto para el experimento comparativo. Por ello, los datasets con cobertura directa de EPP tienen mayor prioridad para ajuste de dominio, mientras que las colecciones orientadas a contexto de obra, maquinaria o layout se valoran principalmente por su utilidad para evaluación, análisis relacional o datos complementarios.

Tabla 29

Aptitud de cada dataset candidato para fine-tuning y evaluación


| Dataset | Aptitud FT | Aptitud eval. | Justificación |
| --- | --- | --- | --- |
| SH17 | Alta | Alta | Fuente robusta para EPP, especialmente CR-01 y apoyo a CR-02. Su dominio industrial exige controlar el posible sesgo respecto de construcción civil. |
| SHEL5K | Media-Alta | Alta | Muy sólido para CR-01 por su foco en casco y ausencia de casco. Su utilidad fuera de esa condición es limitada. |
| CHV | Media-Alta | Alta | Alta pertinencia visual para CR-01 y CR-02 en escenas reales de construcción. Requiere verificar condiciones de redistribución. |
| Pictor-PPE | Media/Condicionada | Media/Condicionada | Útil para cumplimiento casco/chaleco, pero condicionado por disponibilidad pública parcial y licencia no claramente estandarizada. |
| Construction-PPE | Media-Alta | Alta | Valioso para evaluación de incumplimientos de EPP por sus clases explícitas positivas y negativas. Su volumen es reducido y la licencia AGPL-3.0 requiere atención. |
| GDUT-HWD | Media-Alta | Alta | Relevante para CR-01 en construcción, especialmente uso y color de casco. No aporta cobertura para chaleco ni condiciones contextuales. |
| SHWD | Media-Alta | Alta | Volumen relevante y formato Pascal VOC, con anotaciones centradas en casco/persona. Es útil para CR-01, especialmente como fuente complementaria para presencia o ausencia de casco. |
| SODA | Media | Media-Alta | Aporta contexto de obra, materiales, maquinaria y layout. Su mayor valor está en evaluación contextual y apoyo a CR-05/CR-06, no como fuente principal de EPP. |
| MOCS | Baja/Condicionada | Media/Condicionada | Útil como apoyo contextual para maquinaria, trabajadores y CR-05. No es adecuado para fine-tuning de EPP y depende de acceso, formato y términos de uso. |

Nota. La categoría “condicionada” indica que el uso efectivo del dataset requiere verificar acceso, formato, licencia o términos específicos antes de su gestión en la instancia de análisis y diseño arquitectónico. La asignación definitiva de roles corresponde a dicha etapa.


##### 17.1.6.3. Benchmarks de Evaluación de Referencia (Categoría 2)

Tal como establece el framework de métricas, las métricas MOT basadas en identidades persistentes sólo resultan metodológicamente defendibles cuando se dispone de secuencias o benchmarks específicamente anotados con IDs de trayectoria. Por ello, los benchmarks de esta categoría no sustituyen la evaluación del dominio del proyecto: cumplen una función acotada de verificación de implementación y comparación de referencia para el módulo de seguimiento.

Tabla 30

Benchmarks de evaluación de referencia para módulos de seguimiento


| Dataset | Características | Licencia | Métricas | Aptitud en el proyecto | Limitaciones |
| --- | --- | --- | --- | --- | --- |
| MOT17 | 14 secuencias reales; benchmark operacionalizado como 42 entradas al considerar tres sets públicos de detecciones por secuencia: DPM, Faster R-CNN y SDP. | CC BY-NC-SA 3.0 | MOTA, IDF1, HOTA | Adecuado para verificar que la implementación del tracker reproduce resultados comparables a trackers de referencia bajo un protocolo conocido. | Benchmark centrado en seguimiento de peatones; no representa el dominio construcción. |
| OVT-B | 1.973 videos; 637.608 anotaciones de bounding boxes; 1.048 categorías. | Apache-2.0 visible en el repositorio oficial | TETA como métrica principal; LocA, ClsA y AssA como componentes. | Adecuado para evaluar la integración OVD+MOT bajo vocabulario abierto extenso y múltiples categorías. | No declara cobertura específica del dominio construcción. |

Nota. TETA = Track Every Thing Accuracy; LocA = Localization Accuracy; ClsA = Classification Accuracy; AssA = Association Accuracy. MOTA = Multiple Object Tracking Accuracy; IDF1 = ID F1 Score; HOTA = Higher Order Tracking Accuracy. TrackingNet y LaSOT se descartan por corresponder a benchmarks de single-object tracking; OV-TAO se descarta porque OVT-B ofrece mayor escala y una adecuación más directa al problema open-vocabulary multi-object tracking del proyecto.


###### 17.1.6.3.1. MOT17 — Justificación de Uso

MOT17 no representa el dominio de construcción civil. Su inclusión responde a una razón de ingeniería específica: constituye un benchmark de referencia ampliamente utilizado para evaluar trackers multiobjeto bajo un protocolo conocido. En particular, permite contrastar la implementación local del módulo de seguimiento con resultados públicos de trackers de referencia, como ByteTrack y OC-SORT, antes de trasladar el análisis al dominio del proyecto. Por lo tanto, la evaluación sobre MOT17 responde a una pregunta de corrección de implementación y reproducibilidad técnica, no de validez operativa en obra.


###### 17.1.6.3.2. OVT-B — Justificación de Uso

OVT-B es el benchmark más cercano a la arquitectura conceptual del proyecto, porque evalúa explícitamente el seguimiento multiobjeto en régimen open-vocabulary. Su utilidad no reside en representar el dominio de construcción civil, sino en evaluar la integración OVD+MOT bajo un vocabulario extenso y trayectorias de múltiples categorías. Por ello, OVT-B se interpreta como benchmark de referencia para robustez semántica y asociación temporal, mientras que la validación del dominio específico se mantiene separada y deberá realizarse sobre los datos del proyecto o sobre el escenario complementario que se defina en la instancia de análisis y diseño arquitectónico.


##### 17.1.6.4. Consideraciones Transversales

Las secciones precedentes analizaron los datasets desde una perspectiva técnica y metodológica. La presente sección documenta dos dimensiones que atraviesan el inventario completo con independencia de la categoría o del propósito asignado a cada dataset: las condiciones éticas y de licencia que enmarcan el uso de los datos, y las restricciones logísticas que condicionan su gestión operativa. Ambas dimensiones son insumos directos para la planificación de la instancia de análisis y diseño arquitectónico.


###### 17.1.6.4.1. Consideraciones Éticas sobre los Datos

Los datasets de Categoría 1 reúnen imágenes provenientes de fuentes heterogéneas: imágenes web-mined o crowd-sourced, repositorios públicos, contextos industriales, escenas reales de construcción y, en el caso de MOCS, datos disponibles sólo mediante solicitud previa. En todos los casos, el uso previsto por el proyecto se limita a investigación académica, sin reconocimiento facial, identificación individual ni tratamiento biométrico. Las anotaciones consideradas son principalmente cajas delimitadoras, máscaras o etiquetas de objetos, en alineación con el principio de privacidad documentado en la el marco ético-legal de la fundamentación teórica.

Para cualquier dato generado ad hoc conforme a las alternativas de la Sección 17.1.6.2.6, se aplicará un protocolo específico de consentimiento informado, anonimización de rostros y minimización de datos personales, sin retención de identificadores biométricos. Este criterio se adopta en consonancia con la normativa argentina vigente de protección de datos personales, en particular la Ley 25.326.

Desde el punto de vista de licencias y condiciones de uso, la situación del inventario no es homogénea. SH17 declara licencia CC BY-NC-SA 4.0; SHEL5K se publica bajo CC BY 4.0; Construction-PPE se distribuye bajo AGPL-3.0; GDUT-HWD presenta licencia Apache-2.0 visible en el repositorio; y SHWD presenta licencia MIT. CHV declara acceso abierto o uso libre en su repositorio, aunque sin una licencia estandarizada visible para el paquete de datos. Pictor-PPE y SODA documentan disponibilidad pública, pero sus condiciones específicas de reutilización del paquete descargable deberán verificarse antes de cualquier integración, redistribución o generación de derivados. MOCS, por su parte, queda sujeto a solicitud previa, uso científico no comercial, licencia CC BY-NC 4.0 y restricciones explícitas de redistribución y alteración del dataset.

En consecuencia, la instancia de análisis y diseño arquitectónico deberá verificar manualmente los términos efectivos de cada fuente antes de descargar, fusionar, redistribuir o publicar derivados de los datos. La gestión del corpus deberá conservar trazabilidad por dataset de origen, registrar licencias y condiciones aplicables, y evitar que la combinación de colecciones con licencias heterogéneas genere obligaciones incompatibles con el alcance académico del proyecto.


###### 17.1.6.4.2. Logística de Datos

El pipeline de gestión de datos comprende cinco pasos secuenciales: descarga o solicitud de acceso desde las fuentes de origen, verificación de integridad, inspección del formato nativo y conversión al formato de trabajo requerido por cada pipeline, partición conforme a las condiciones metodológicas definidas anteriormente, y transferencia del subset de entrenamiento y, cuando corresponda, del conjunto de validación al clúster de cómputo de alto rendimiento Mendieta para el experimento de fine-tuning. La evaluación e inferencia operativa se ejecutarán en el hardware local, manteniendo la separación funcional entre entrenamiento y despliegue documentada en la sección de entorno experimental, infraestructura y escenarios de evaluación. Esto puede verse en detalle en la Tabla C.5 del Anexo C.


##### 17.1.6.5. Síntesis parcial de la estrategia de datos, benchmarks y partición

La estrategia de datos, benchmarks y partición muestra una cobertura desigual respecto del catálogo retenido. Las condiciones de EPP poseen el soporte más sólido: CR-01 cuenta con múltiples fuentes centradas en casco o ausencia de casco, y CR-02 dispone de cobertura adecuada para chaleco, aunque menos redundante. En cambio, CR-03 y CR-04 mantienen brechas directas de cobertura, mientras que CR-05 y CR-06 dependen de entidades auxiliares y contexto parcial, no de etiquetas nativas del patrón de riesgo completo.

Tabla 31 Cobertura de datos por condición y consecuencia metodológica


| Condición | Nivel de cobertura | Fuentes o apoyo principal | Uso metodológico definido |
| --- | --- | --- | --- |
| CR-01 - Persona sin casco | Sólida | SH17, SHEL5K, CHV, Pictor-PPE, Construction-PPE, GDUT-HWD y SHWD. | Integra el núcleo obligatorio del experimento y la comparación entre baseline y fine-tuning. |
| CR-02 - Persona sin chaleco reflectivo | Adecuada | SH17, CHV, Pictor-PPE y Construction-PPE. | Integra el núcleo obligatorio del experimento, con menor redundancia que CR-01. |
| CR-03 - Trabajo en altura sin anticaídas | Brecha directa | Sin dataset con condición completa operacionalizada. | Sólo puede evaluarse si la instancia de análisis y diseño arquitectónico aporta datos complementarios metodológicamente defendibles. |
| CR-04 - Borde elevado desprotegido | Brecha directa | Sin dataset con condición completa operacionalizada. | Se mantiene como extensión condicionada; no forma parte del plano obligatorio de aceptación. |
| CR-05 - Maquinaria cerca de peatones | Parcial por entidades y contexto | SODA y MOCS como apoyo de entidades y contexto; material de entorno controlado sólo si se genera. | Permite pruebas condicionadas del módulo relacional; no constituye por sí sola evidencia plena de aceptación con datasets públicos. |
| CR-06 - Persona en zona restringida | Parcial y dependiente del contexto | SODA como apoyo contextual; EBE con cámara fija y polígono externo cuando se defina la región restringida. | Su validación depende de parametrización espacial externa al prompt; no se resuelve con datasets abiertos por sí sola. |

Nota. La cobertura se refiere a la posibilidad de evaluar la condición operativa completa y no sólo a la presencia de algunas de sus entidades en una colección de imágenes.

Los benchmarks de referencia cumplen un papel más acotado. MOT17 puede utilizarse para verificar instrumentación y cálculo de métricas de tracking bajo un protocolo ampliamente conocido; OVT-B puede servir para observar integración entre open vocabulary y tracking. Ninguno de los dos se interpretará como evidencia directa de desempeño en construcción civil. Su valor es instrumental: permiten auditar módulos del sistema antes de reinsertarlos en el dominio objetivo.

Esta clasificación evita una sobre-declaración del alcance experimental. En particular, la presencia de entidades relacionadas con CR-03 o CR-04 en una colección de imágenes no habilita por sí sola la validación de la condición completa. Para esas condiciones, el protocolo sólo podrá reportar resultados completos cuando exista evidencia anotada sobre la combinación operativa requerida; de lo contrario, deberá distinguir entre detección de componentes visuales, prueba exploratoria de reglas espaciales y validación efectiva del patrón de riesgo.

La partición de datos se rige por cinco reglas obligatorias: el test set debe congelarse antes de cualquier entrenamiento o augmentation; la baseline zero-shot y toda variante fine-tuned deben evaluarse sobre el mismo conjunto de test; los splits deben ser estrictamente disjuntos; la semilla y el procedimiento de partición deben registrarse; y toda anotación complementaria debe separar material de desarrollo y material de evaluación. Estas reglas sostienen la comparabilidad del protocolo.

Para las condiciones brechadas, la política de datos complementarios sigue un orden de preferencia conservador: primero curación y conversión de fuentes públicas compatibles; después anotación complementaria acotada sobre material estrictamente necesario; y sólo en último término producción específica de material controlado en el EBE. El objetivo es evitar que la expansión del corpus consuma el tiempo y la capacidad que el proyecto necesita reservar para integración, instrumentación y validación del sistema.


#### 17.1.7. Framework de Métricas, Viabilidad Operativa y Presupuesto de Latencia


##### 17.1.7.1. Introducción y Alcance


###### 17.1.7.1.1. Propósito y Preguntas Rectoras

La fundamentación teórica del proyecto E-OVRT-VDP identificó una brecha persistente entre las métricas académicas estándar y la evidencia operativa que debe ofrecer un sistema de alerta asistiva orientado a seguridad laboral. Aunque métricas como AP, HOTA y los indicadores convencionales de rendimiento del pipeline resultan necesarias para la comparabilidad técnica, por sí solas no permiten establecer si el sistema detecta, sostiene y transforma una condición de riesgo en una alerta con la oportunidad, la estabilidad y la trazabilidad requeridas por el dominio.

En ese marco, la presente sección responde a dos de las preguntas rectoras formuladas en la fundamentación teórica. En relación con P-E1-06, define el framework de métricas para evaluar de manera integral detección OVD, seguimiento multiobjeto, rendimiento del pipeline y desempeño operativo de alerta, junto con umbrales orientativos diferenciados por severidad. En relación con P-E1-01, operacionaliza el presupuesto de latencia admisible mediante una descomposición en componentes medibles y una estimación orientativa compatible con el perfil de hardware de referencia.

El alcance de la sección es metodológico. Define métricas, niveles de compromiso, criterios de aplicación, umbrales orientativos y requisitos mínimos de instrumentación y reporte, pero no implementa la medición en código ni ejecuta campañas experimentales. Esas tareas corresponden, respectivamente, a la instancia de análisis y diseño arquitectónico y a la validación experimental. Las definiciones formales de las métricas estándar pueden consultarse en las secciones correspondientes de la fundamentación teórica.

En consecuencia, el framework no debe interpretarse como una promesa de ejecución uniforme de todas las métricas definidas, sino como una matriz metodológica de aplicación condicionada. Cada métrica sólo será exigible cuando existan los datos, módulos, referencias de evaluación e instrumentación necesarios para calcularla de manera trazable. Cuando esas condiciones no se cumplan, la salida metodológicamente correcta será declararla como no ejecutada o no aplicable, indicando la causa.


##### 17.1.7.2. Alcance Evaluativo y Definición Operativa de la Latencia de Alerta

A efectos evaluativos, se distinguen tres tramos temporales que no deben confundirse. El primero es Glass-to-Algorithm (G2A), que mide el intervalo entre la captura o lectura de un frame y la disponibilidad del resultado algorítmico asociado a ese frame. El segundo es Glass-to-Alert, que mide el intervalo entre el inicio anotado de una condición de riesgo y la generación de una alerta confirmada y registrada dentro del sistema. El tercero es glass-to-glass, que extiende la cadena hasta la visualización remota del video procesado (Axis Communications AB, s. f.; Bachhuber et al., 2018).

La presente sección concentra su validación primaria en el tramo Glass-to-Alert hasta la alerta confirmada y registrada dentro del sistema. En consecuencia, la métrica operativa principal es , entendida como el tiempo entre el inicio anotado del evento y la generación de una alerta registrada luego de la evaluación del patrón correspondiente. Esta definición distingue la alerta de una detección aislada y la ubica como salida operativa trazable del sistema.

En las configuraciones que incluyan un trayecto instrumentado de consulta o notificación, se reportará adicionalmente como medida complementaria. Esta métrica extiende la medición hacia la disponibilidad de la alerta en el canal definido, pero no forma parte del núcleo evaluativo mínimo.

Bajo esta convención, G2A se entiende como el subtramo instrumental del pipeline que va desde la captura o lectura del frame hasta la disponibilidad del resultado algorítmico. El tramo Glass-to-Alert integra, además de ese subtramo, los módulos de seguimiento y razonamiento que correspondan y, sobre todo, la ventana funcional de persistencia requerida para confirmar el patrón de riesgo. Esta delimitación permite separar con claridad la latencia estrictamente computacional de las demoras asociadas al trayecto de consulta, notificación, distribución o interpretación humana.


##### 17.1.7.3. Estructura del Framework y Criterios de Viabilidad

El framework se organiza en torno a una jerarquía de métricas y a niveles de compromiso que permiten priorizar evidencia sin sobredimensionar el alcance experimental. La combinación de ambos ejes preserva el rigor metodológico y, al mismo tiempo, reconoce que no todas las métricas útiles son igualmente ejecutables dentro del prototipo experimental.


###### 17.1.7.3.1. Jerarquía de métricas

La jerarquía del framework se organiza en tres niveles. El nivel primario reúne las métricas que capturan valor operativo directo para el prototipo: , Tiempo a la Primera Detección (TTFD), Tasa de Detección Sostenida (SDR) y Precision/Recall por severidad. El nivel secundario reúne las métricas que explican el comportamiento del detector, del tracker y del pipeline sin constituir por sí mismas evidencia suficiente de valor operativo: AP@0.5, AP@[0.5:0.95], HOTA y los indicadores complementarios de MOT y desempeño computacional. El nivel transversal reúne las métricas de comparación entre variantes zero-shot y fine-tuned, siempre que existan baseline explícita, particiones disjuntas y soporte de datos suficiente.

La pertenencia de una métrica al nivel primario expresa su prioridad interpretativa, no su aplicabilidad automática. Una métrica primaria puede no ejecutarse si el escenario evaluado no dispone de eventos anotados, persistencia temporal, motor de patrones, severidad asignada o logs suficientes. En esos casos, la métrica conserva su rol dentro del framework, pero debe reportarse como no aplicable para esa corrida o condición específica.

Esta jerarquía tiene una consecuencia práctica: si los recursos experimentales no permitieran ejecutar todo el repertorio con la misma profundidad, el núcleo evaluativo del prototipo estará dado por las métricas primarias y por los diagnósticos mínimos del pipeline. Las métricas deseables o conceptuales conservan valor analítico y comparativo, pero no deben desplazar la evidencia central sobre capacidad de alerta.


###### 17.1.7.3.2. Niveles de Compromiso

No todas las métricas definidas en esta sección asumen el mismo nivel de compromiso. Obligatorio designa métricas que el núcleo del prototipo experimental debe reportar para sostener sus conclusiones; deseable designa métricas que enriquecen el análisis, pero cuya omisión no invalida el experimento si se explicita la razón; conceptual designa tratamientos o extensiones metodológicas cuya formulación analítica es pertinente, aunque su evaluación empírica completa exceda el alcance experimental del prototipo.

El nivel de compromiso también depende del alcance efectivamente implementado. Una métrica puede ser obligatoria para condiciones evaluables mediante detección directa o indirecta ya instrumentada, y no resultar exigible allí donde todavía falten módulos de razonamiento contextual, anotación especializada o trayectos completos de notificación.


###### 17.1.7.3.3. Criterios de Factibilidad Experimental

Una métrica sólo se asumirá como obligatoria cuando cumpla simultáneamente cinco condiciones: necesidad operativa para responder la pregunta de validación del prototipo experimental; disponibilidad de ground truth o referencia verificable; existencia del módulo que produce la señal evaluada; instrumentación suficiente mediante timestamps, logs o exportación de resultados; y costo de anotación o procesamiento compatible con el proyecto. Bajo estos criterios, una métrica puede estar correctamente definida en el framework y, aun así, no corresponder en una corrida concreta. Esta distinción evita validar el prototipo con indicadores que los datos, el entorno o la implementación no permiten sostener.


##### 17.1.7.4. Métricas Adoptadas

Las secciones siguientes presentan las familias de métricas seleccionadas para los tres planos del sistema evaluable: detección OVD, seguimiento multiobjeto (MOT) y rendimiento del pipeline. La selección no pretende agotar la literatura, sino establecer un conjunto defendible de métricas candidatas y niveles de compromiso coherentes con el alcance del prototipo.


###### 17.1.7.4.1. Métricas de Detección OVD

La evaluación del componente de detección open-vocabulary adopta un subconjunto de las métricas estándar revisadas en el análisis de modelos OVD. AP@0.5 y Precision/Recall constituyen el núcleo mínimo por su interpretabilidad, su disponibilidad en herramientas de evaluación consolidadas y su utilidad para contrastar variantes zero-shot y fine-tuned. AP@[0.5:0.95] se conserva como métrica deseable de comparabilidad académica, mientras que NMS-AP permanece en plano conceptual por su valor analítico sobre vocabularios extensos y su menor prioridad operativa en el prototipo experimental. Pueden verse estas métricas en la Tabla D.1 del Anexo D.


###### 17.1.7.4.2. Métricas de Seguimiento Multiobjeto

La evaluación MOT recupera como base las métricas estándar desarrolladas en la el análisis de seguimiento multiobjeto, pero recalibra su nivel de compromiso según el alcance efectivo del prototipo experimental. En ese marco, HOTA se conserva como métrica de referencia académica, aunque su cálculo riguroso —al igual que DetA, AssA e IDF1— exige anotaciones frame-a-frame con identidades persistentes, por lo que estas métricas quedan como deseables sobre subsets específicamente preparados para MOT. MOTA, IDSW y fragmentación conservan valor diagnóstico complementario en esos mismos subsets.

Para el núcleo del prototipo experimental, la métrica más útil es , incorporada en esta etapa como operacionalización propia y entendida como la diferencia de falsos positivos observada entre corridas equivalentes con y sin tracker habilitado. Su valor metodológico reside en estimar si el seguimiento reduce detecciones espurias o falsas alertas sin exigir ground truth de identidades. No obstante, su interpretación sólo es válida si la unidad de conteo del falso positivo se declara previamente y se mantiene constante durante la comparación.

El análisis de las métricas de seguimiento multiobjeto puede verse en la Tabla D.2 del Anexo D.


###### 17.1.7.4.3. Métricas de Rendimiento del Pipeline

El rendimiento del pipeline integrado constituye una familia de métricas propia, porque la utilidad del sistema no depende sólo de la calidad semántica de detección o tracking, sino también del comportamiento sostenido de la cadena completa. FPS efectivos, latencia G2A y consumo de recursos permiten interpretar cuellos de botella, estabilidad temporal y margen operativo del hardware disponible. El análisis de las métricas de rendimiento del pipeline queda desarrollado en la Tabla D.3 del Anexo D.


##### 17.1.7.5. Métricas Operativas Específicas del Dominio

Las métricas estándar de detección, seguimiento y rendimiento aportan comparabilidad técnica, pero no alcanzan por sí solas para describir el valor operativo del sistema en seguridad laboral. En este dominio, no interesa únicamente si el modelo detecta objetos o atributos en un frame, sino si el prototipo puede reaccionar frente a una condición de riesgo, sostener evidencia temporal suficiente y transformar esa evidencia en una alerta trazable cuando corresponda.

Por ello, esta sección incorpora métricas operativas específicas del dominio: latencia de alerta, tiempo a la primera detección, tasa de detección sostenida y evaluación diferenciada por severidad. Su aplicación queda condicionada por la disponibilidad de secuencias temporales, eventos anotados, criterios de detección positivos previamente definidos e instrumentación suficiente. En consecuencia, estas métricas no deben interpretarse como aplicables a toda corrida experimental, sino como métricas ejecutables sólo cuando los datos y el alcance implementado permiten calcularlas de manera válida.


###### 17.1.7.5.1. Latencia de Alerta ()

La latencia de alerta se evalúa principalmente mediante . Esta métrica no mide una detección aislada, sino la capacidad del prototipo para transformar evidencia visual en una alerta confirmada y registrada dentro del sistema.

Por lo tanto, sólo corresponde cuando la corrida incluye, como mínimo, detección OVD, evaluación de patrón, confirmación del patrón y registro interno de la alerta. Una detección temprana puede contribuir a la alerta, pero no la constituye por sí misma si no satisface los criterios de persistencia, severidad o activación definidos para el patrón evaluado.

En pruebas puramente frame-a-frame, donde sólo se evalúa la salida del detector OVD sin evaluación de patrón ni alerta registrada, no corresponde reportar . En esos casos, el análisis debe limitarse a métricas de detección, rendimiento del pipeline o latencia Glass-to-Algorithm (G2A), declarando explícitamente la no aplicación de métricas de alerta.

Cuando la configuración evaluada incluya un trayecto instrumentado de consulta, exposición o notificación, se reportará adicionalmente como medida complementaria. Esta métrica no forma parte del núcleo mínimo de validación de la alerta, porque depende de componentes de interfaz o comunicación que pueden variar según el diseño arquitectónico adoptado.


###### 17.1.7.5.2. Tiempo a la Primera Detección (TTFD)

El Tiempo a la Primera Detección, o TTFD, mide el tiempo transcurrido entre el inicio anotado de una condición de riesgo y la primera detección positiva válida producida por el sistema, según el criterio declarado para la corrida. A diferencia de , esta métrica no requiere confirmación por persistencia, evaluación completa del patrón ni generación de alerta. Su función es medir la rapidez con la que el sistema produce la primera evidencia perceptiva asociada a una condición nueva.

TTFD debe interpretarse como una métrica de reacción inicial y no como una métrica de alerta. Una primera detección temprana puede ser útil para reducir la latencia operativa posterior, pero no implica por sí sola que exista un patrón de riesgo confirmado ni una alerta válida dentro del sistema. La transición desde TTFD hacia depende de que las detecciones posteriores satisfagan los criterios de persistencia, severidad o activación definidos para la condición evaluada.

Esta métrica resulta especialmente informativa en eventos de severidad crítica o alta, donde interesa conocer cuánto tarda el sistema en producir la primera señal visual relevante. Sin embargo, su aplicación requiere que el evento tenga un inicio temporal anotado y que el criterio de detección positiva esté definido previamente. En datasets estáticos de imágenes, o en evaluaciones sin secuencia temporal ni inicio de evento identificable, TTFD no corresponde como métrica operativa y debe declararse como no aplicable.


###### 17.1.7.5.3. Tasa de Detección Sostenida (SDR)

La Tasa de Detección Sostenida, o SDR, mide la proporción del intervalo anotado de una condición de riesgo durante la cual el sistema mantiene detecciones positivas, según el criterio definido para la corrida. Su función es evaluar la estabilidad temporal de la evidencia, no la generación de una alerta.

En el protocolo, SDR permite distinguir entre una detección puntual y una condición sostenida. Una detección aislada puede no ser suficiente para confirmar un patrón de riesgo; por eso, esta métrica aporta evidencia sobre la persistencia necesaria para alimentar la lógica de confirmación del patrón.

SDR sólo corresponde cuando existe una secuencia temporal con inicio y duración anotados de la condición evaluada. En datasets estáticos de imágenes, o en evaluaciones sin ventana temporal identificable, la métrica no resulta aplicable y debe declararse como tal.


###### 17.1.7.5.4. Condición de Aplicación de Métricas Temporales

Las métricas , TTFD y SDR sólo son ejecutables sobre secuencias temporales donde pueda identificarse el inicio de la condición de riesgo, su duración efectiva y la respuesta temporal del sistema. No corresponde calcularlas sobre datasets compuestos únicamente por imágenes estáticas no ordenadas temporalmente.

En esos casos, la evaluación debe limitarse a métricas de detección por imagen o por frame, como AP@0.5 y Precision/Recall, además de métricas de rendimiento del pipeline cuando exista instrumentación suficiente. Las métricas temporales quedan reservadas para clips, secuencias anotadas o corridas EBE con eventos definidos.


###### 17.1.7.5.5. Evaluación Diferenciada por Severidad

No todos los errores del sistema tienen el mismo impacto operativo. Por ello, el framework adopta como obligación mínima el reporte de Precision y Recall por severidad, o por grupos de condiciones con severidad homogénea, acompañado por el tamaño muestral correspondiente.

Esta evaluación sólo corresponde cuando la severidad haya sido asignada previamente a la condición, patrón o evento evaluado. Si la severidad no fue definida de forma explícita, Precision y Recall podrán reportarse por condición de riesgo, pero no como métricas diferenciadas por severidad.

La asignación formal de pesos distintos a falsos positivos y falsos negativos se mantiene en plano conceptual. Aunque puede ser metodológicamente útil para reflejar diferencias de impacto operativo, depende de criterios de política de riesgo que exceden el alcance del prototipo experimental.


##### 17.1.7.6. Protocolo Comparativo entre Variantes Preentrenada y Ajustada al Dominio

La comparación entre la variante preentrenada y la variante ajustada al dominio (fine-tuned) debe entenderse como un protocolo evaluativo condicionado, no como un resultado garantizado. Su finalidad es determinar si el ajuste al dominio aporta mejoras medibles sin comprometer la validez experimental ni degradar de manera no controlada la capacidad open-vocabulary del modelo. En ese marco, toda variante ajustada al dominio requiere una baseline zero-shot explícita, evaluada previamente sobre el conjunto de evaluación reservado. Esa baseline constituye el punto de referencia mínimo de toda comparación. En ausencia de baseline zero-shot, soporte de datos suficiente o separación estricta entre entrenamiento y evaluación, el contraste entre variantes no corresponde como evidencia metodológicamente válida. La separación estricta entre datos de entrenamiento y evaluación es condición de validez experimental y deberá quedar formalizada en la estrategia de datos, benchmarks y partición. Asimismo, la selección de checkpoints no debe hacerse sobre el conjunto de evaluación ni sobre clips o frames reutilizados en la línea base o baseline. Toda corrida comparativa deberá conservar el mismo conjunto de evaluación y la misma configuración experimental, salvo la variable que se busque aislar. Cuando exista una variante ajustada y soporte de datos suficiente para una condición de riesgo determinada, se reportarán los deltas ΔAP, ΔRecall, ΔPrecision y ΔSDR respecto de la baseline zero-shot. Los deltas sobre y TTFD se consideran deseables cuando la condición evaluada permita medirlos con trazabilidad suficiente. Del mismo modo, resulta deseable verificar si el ajuste al dominio degrada la capacidad open-vocabulary sobre categorías externas al entrenamiento mediante un subset generalista separado del dominio específico.

Toda ejecución de ajuste al dominio debe documentar horas-GPU, tiempo total, horas-persona, cantidad de imágenes y criterios de selección del checkpoint. Sin ese contexto, la ganancia observada pierde interpretabilidad como insumo para decisiones metodológicas.

Tabla 32

Métricas y criterios de reporte para la comparación entre variantes


| Métrica | Qué captura | Relación con métricas estándar | Compromiso | Nivel |
| --- | --- | --- | --- | --- |
| ΔAP, ΔRecall, ΔPrecision, ΔSDR por CR-XX | Ganancia del fine-tuning respecto de la baseline zero-shot. | Diferencia entre variantes | Obligatorio si aplica | Transversal |
| Δtalert, ΔTTFD | Verifica que el ajuste al dominio no degrade ni la respuesta inicial. | Diferencia entre variantes | Deseable | Transversal |
| AP generalista post fine-tuning | Retención de capacidad abierta fuera del dominio de entrenamiento. | Comparación sobre subset generalista | Deseable | Transversal |
| Costo de entrenamiento | Horas-GPU, tiempo total, horas-persona e imágenes utilizadas. | Registro documental | Obligatorio si hay fine-tuning | Transversal |

Nota. Δ = diferencia respecto de la baseline zero-shot. La expresión «si aplica» indica que la métrica sólo se exige cuando existe una variante ajustada al dominio, una baseline zero-shot explícita, soporte de datos suficiente y partición estrictamente disjunta entre entrenamiento y evaluación. AP generalista post fine-tuning refiere a la retención de capacidad open-vocabulary fuera del dominio de ajuste.


##### 17.1.7.7. Presupuesto de Latencia y Componentes Medibles

La latencia de alerta se trata aquí como un presupuesto descomponible en componentes observables. En este marco, G2A representa el subtramo instrumental del pipeline por frame, mientras que operacionaliza la latencia de alerta hasta su confirmación interna. En las configuraciones que incluyan un trayecto instrumentado de notificación, se considerará además .


###### 17.1.7.7.1. Descomposición Operativa

La descomposición temporal adoptada es la siguiente:

Aquí, representa la ventana funcional de persistencia necesaria para confirmar el evento, no un costo de cómputo en sentido estricto. El modelo es deliberadamente aditivo y conservador: aunque en una implementación real pueden existir solapamientos, buffering o paralelismo, la descomposición lineal sigue siendo útil para instrumentar mediciones, detectar cuellos de botella y comparar configuraciones.


###### 17.1.7.7.2. Componentes Medibles y Adscripción por Tramo

La descomposición temporal presentada en la subsección anterior sólo resulta metodológicamente útil si cada componente queda adscrito a un tramo evaluativo preciso. En ese marco, la presente tabla no fija valores cerrados por componente, sino que organiza qué partes del retardo pertenecen al subtramo instrumental G2A, cuáles integran la confirmación interna de la alerta operacionalizada como y cuál corresponde, cuando exista, al trayecto adicional de notificación expresado por . Su función es guiar la instrumentación mínima del sistema efectivamente implementado y evitar que se mezclen costos computacionales, ventanas funcionales de evidencia y demoras externas de interfaz o distribución.

Tabla 33

Componentes del presupuesto de latencia y adscripción a G2A, y


| Componente | Criterio orientativo | Variables dominantes | Tramo | Compromiso |
| --- | --- | --- | --- | --- |
|  | Debe medirse como parte del origen temporal de la corrida. | Sensor, buffer de captura, FPS de origen. | G2A | Obligatorio |
|  | Debe medirse sobre el mecanismo de suministro efectivamente utilizado, ya sea red, stream o lectura local instrumentada. | RTSP/WebRTC, RTT, buffering, codificación/decodificación e I/O de lectura. | G2A | Obligatorio |
|  | Incluye transformaciones de entrada y, cuando corresponda, transferencias entre CPU y GPU. | Resize, normalización y movimiento CPU-GPU. | G2A | Obligatorio |
|  | Debe medirse por modelo y resolución; suele concentrar la mayor carga computacional. | Arquitectura OVD, resolución, caching de embeddings. | G2A | Obligatorio |
|  | Corresponde a la ventana funcional de persistencia necesaria para confirmar el evento; no debe confundirse con un costo de cómputo. | Severidad, regla de persistencia, duración mínima del evento y frecuencia de muestreo. |  | Obligatorio cuando exista confirmación por persistencia |
|  | Sólo corresponde si hay tracker. | Método MOT, matching, cantidad de objetos. |  | Obligatorio si hay tracker |
|  | Debe distinguirse de y medirse como costo computacional de las reglas aplicadas. | Reglas de persistencia, lógica espacial, patrones activos. |  | Obligatorio si existe |
|  | Sólo aplica en configuraciones que incluyan un trayecto instrumentado de notificación hacia interfaz, cliente o canal externo. | MQTT/HTTP/WebSocket, cola de eventos, cliente e interfaz. |  | Deseable |

Nota. La tabla organiza los componentes del presupuesto y explicita a qué tramo pertenece cada uno: G2A, o . No fija valores cerrados por componente; su función es guiar la instrumentación y la interpretación del retardo sobre el sistema efectivamente implementado. La inclusión explícita de responde a que la latencia de alerta confirmada no se reduce al costo computacional del pipeline, sino que incorpora además la ventana funcional necesaria para acumular evidencia suficiente antes de registrar una alerta interna.


###### 17.1.7.7.3. Consideración sobre el Razonamiento Temporal

El componente debe distinguirse explícitamente de . El primero corresponde al costo computacional asociado a la evaluación de reglas de persistencia, asociaciones espaciales y patrones activos una vez disponibles las detecciones. El segundo corresponde al tiempo funcional que el sistema requiere para acumular evidencia suficiente antes de confirmar una alerta. Esta distinción es metodológicamente central, porque evita interpretar la latencia de alerta confirmada como si fuera únicamente un problema de rendimiento computacional: integra el presupuesto computacional del sistema, mientras que integra el presupuesto operativo de confirmación que queda absorbido por .


###### 17.1.7.7.4. Cierre Operativo del Presupuesto

En términos operativos, G2A abarca , , y . La latencia de alerta hasta su confirmación interna, operacionalizada mediante , agrega, según la configuración evaluada, , y la ventana funcional . El trayecto de notificación hacia interfaz, cliente o canal externo debe tratarse como una extensión adicional del sistema, expresada mediante , y no como condición para validar el núcleo del prototipo experimental.


###### 17.1.7.7.5. Estimación Orientativa del Presupuesto de Latencia

La descomposición presentada permite construir una estimación orientativa del presupuesto de latencia sin confundir el rendimiento por frame del subtramo G2A con la latencia de alerta confirmada expresada por . Esta estimación no reemplaza la calibración empírica de la validación experimental, sino que funciona como referencia de plausibilidad para interpretar los umbrales de la Sección 17.1.7.7.6 y verificar que las metas de resulten consistentes con el hardware de referencia.

Tomando como perfil de referencia el hardware de inferencia documentado en el entorno experimental, infraestructura y escenarios de evaluación, puede asumirse como orientación inicial un rango de 10 a 50 ms para + en una LAN controlada y configurada para baja latencia. Ese orden de magnitud es consistente con la literatura relevada en el análisis de operación en tiempo real, donde la captura a 30 fps impone un piso del orden de un período de cuadro y los protocolos orientados a entornos IP controlados —en particular RTSP/RTP— se presentan como alternativas operativamente convenientes en redes locales cuando el buffering se mantiene acotado (Axis Communications AB, s. f.; Bachhuber et al., 2018). Para , un rango de 5 a 20 ms constituye una estimación de ingeniería razonable para operaciones de redimensionado, normalización y, cuando corresponda, transferencia entre CPU y GPU sobre frames de 640 px; no debe interpretarse como una banda cerrada directamente respaldada por un benchmark único, sino como una aproximación plausible para el perfil experimental adoptado. Para , conviene tratar el rango de 15 a 150 ms como una banda orientativa de ingeniería para inferencia local acelerada, apoyada en dos referencias complementarias. Por un lado, la el análisis de operación en tiempo real identifica un rango de 10–30 ms por frame asociado a modelos ligeros optimizados y otro de 50–150 ms característico de arquitecturas transformer sin optimización específica para edge; por otro, la el análisis de modelos OVD documenta ejemplos concretos dentro de la familia OVD eficiente, como YOLOE-v8-S (3,3 ms) y YOLOE-v8-L (9,8 ms) sobre T4 con TensorRT, YOLO-World-L (19,2 ms) sobre V100 sin TensorRT, y variantes optimizadas como OmDet-Turbo-Base (10 ms) y G-DINO 1.5 Edge (13,3 ms) sobre A100 con TensorRT (Cheng et al., 2024; Wang et al., 2025). En este punto, la mención de YOLO-World debe leerse únicamente como referencia comparativa dentro de la subfamilia eficiente de detectores OVD, no como modelo priorizado del protocolo experimental de E2, cuyos candidatos de trabajo siguen siendo YOLOE y Grounding DINO. Para , un rango de 5 a 20 ms constituye una estimación conservadora y plausible para trackers ligeros de familia tracking-by-detection. En la literatura de referencia del proyecto, SORT se presenta como un método orientado a muy baja carga computacional y ByteTrack como una alternativa que preserva viabilidad en tiempo real dentro de sistemas de seguimiento más completos (Bewley et al., 2016; Zhang et al., 2022); sin embargo, esos valores no deben interpretarse como una cota universal del tracker aislado, sino como órdenes de magnitud útiles para un presupuesto experimental favorable. Para con reglas simples de persistencia y lógica espacial, un valor menor a 10 ms sigue siendo una estimación de ingeniería plausible, sujeta a verificación empírica.

Bajo estos supuestos, el tramo estrictamente computacional desde la captura hasta la disponibilidad de evidencia utilizable para alerta puede ubicarse orientativamente en el orden de 35 a 250 ms por frame cuando se emplean OVD eficientes, red local de baja latencia, tracker ligero y reglas simples. , sin embargo, incorpora además : para severidad crítica, una persistencia orientativa de 2 a 4 s combinada con ese presupuesto computacional vuelve metodológicamente coherente el objetivo de 3 a 5 s; para severidad alta y media, ventanas funcionales más largas hacen igualmente plausibles objetivos orientativos de 5 a 10 s y 10 a 20 s, respectivamente.

El presupuesto precedente corresponde, por tanto, a un escenario favorable de inferencia local sin cuello de botella severo de red y con una familia de modelos optimizada para tiempo real. En este marco, los rangos asignados a y deben interpretarse como estimaciones de ingeniería plausibles, pero no como bandas cerradas directamente respaldadas por la bibliografía citada; su validación definitiva corresponde a la calibración empírica de la validación experimental. Si el hardware efectivo difiriera significativamente del perfil de referencia —por ejemplo, por el uso de modelos más pesados, resolución de entrada superior a 640 px o protocolos de transporte con mayor latencia—, los umbrales de la siguiente sección deberán recalibrarse antes de operar como criterio de aceptación.


###### 17.1.7.7.6. Umbrales orientativos por nivel de severidad

La taxonomía de severidad definida en la taxonomía de condiciones de riesgo, patrones y prompts exige interpretar los umbrales de aceptación de manera diferenciada según la urgencia de la condición, la persistencia requerida para confirmarla y la tolerancia relativa a falsos positivos y falsos negativos. Los valores que siguen son orientativos: ordenan la evaluación del prototipo y deberán recalibrarse en la validación experimental con el throughput efectivo del pipeline. Los umbrales de TTFD se fijan por debajo de las ventanas orientativas de persistencia para preservar su función como métrica de responsividad inicial y evitar que quede absorbida por el tiempo total de confirmación de la alerta.

Severidad crítica. Corresponde a condiciones con potencial de escalada rápida hacia daño grave. Se prioriza minimizar falsos negativos y, por lo tanto, sostener ventanas cortas de confirmación y tiempos exigentes tanto para TTFD como para .

Severidad alta. Corresponde a condiciones donde la exposición sostenida incrementa de forma significativa el riesgo, aunque con un margen de intervención algo mayor. Se admite un compromiso intermedio entre rapidez, estabilidad y control de falsas alarmas.

Severidad media. Corresponde a condiciones con riesgo latente o de escalada más lenta. En este nivel puede exigirse mayor evidencia antes de confirmar la alerta, con menor tolerancia a falsos positivos y ventanas funcionales de persistencia más largas.

Una lista de los umbrales orientativos por severidad puede verse en la Tabla D.4 del Anexo D.


##### 17.1.7.8. Operacionalización de la Medición y Condiciones de no Aplicación

Para que el framework sea ejecutable y no meramente declarativo, la presente sección traduce las métricas anteriores a requisitos mínimos de instrumentación, preparación y registro. Su propósito no es redefinir las métricas, sino fijar las condiciones bajo las cuales su medición resulta metodológicamente defendible.


###### 17.1.7.8.1. Reglas Generales de Instrumentación

Toda corrida debe declarar, como mínimo, modelo, versión, checkpoint, variante, resolución de entrada, hardware, entorno de software, protocolo o mecanismo de suministro de video, umbral de confianza, configuración de NMS, vocabulario activo, ventana de persistencia y presencia o ausencia de tracker. Las corridas comparativas deben ejecutarse sobre el mismo conjunto de clips o frames y con igual configuración experimental, salvo la variable que se busque aislar. En las corridas que involucren fine-tuning, la semilla de partición, el identificador del split y la composición del corpus deberán quedar registrados de manera explícita para permitir regeneración y auditoría del contraste experimental. Las métricas temporales deben usar timestamps monotónicos, consistentes a lo largo del pipeline y con fuente temporal explícitamente declarada.

En las corridas integradas que reporten métricas de alerta, la instrumentación deberá registrar además los hitos temporales asociados a la evaluación del patrón. Como mínimo, deberán conservarse el timestamp de la detección o evidencia positiva inicial, el timestamp de inicio del patrón candidato cuando corresponda, el timestamp de confirmación del patrón, el timestamp de registro interno de la alerta y, si aplica, el timestamp de disponibilidad, consulta o notificación externa. Estos hitos deben provenir de logs trazables y utilizar una fuente temporal coherente con el resto del pipeline. Sin estos registros, no corresponde reportar ni ; sólo podrán reportarse métricas de detección, rendimiento o reacción inicial, según corresponda.

Toda medición debe incluir un período de calentamiento previo. Las métricas temporales se reportarán, como mínimo, con P50, P95 y P99, además del promedio, salvo que el tamaño muestral no lo permita. Si una métrica depende de ground truth específico inexistente o insuficiente, la salida correcta es declararla no ejecutada, no improvisar una aproximación. Esto se desarrolla de manera más sintética en la Tabla D.5 del Anexo D.


###### 17.1.7.8.2. Alcance Efectivo y Casos en los que no Corresponde Medir

El compromiso efectivo de cada métrica depende de la condición de riesgo, del escenario de evaluación y de los módulos realmente implementados e instrumentados. En el alcance metodológico ya consolidado del prototipo experimental, CR-01 y CR-02 constituyen el núcleo evaluativo obligatorio por su cobertura de datos y operacionalización directa, mientras que CR-03 a CR-06 permanecen condicionadas a la disponibilidad de evidencia visual, razonamiento contextual e instrumentación suficiente. En consecuencia, las métricas asociadas a condiciones condicionadas podrán ejecutarse de manera parcial o declararse no aplicables sin comprometer la validez del núcleo del prototipo experimental, siempre que esa decisión quede explícitamente justificada en el reporte.

No corresponde medir HOTA, DetA / AssA, IDF1, MOTA, IDSW ni fragmentación sin ground truth con identidades persistentes. Tampoco corresponde comparar variantes zero-shot y fine-tuned si no existe baseline zero-shot explícita o si la partición train/eval no es estrictamente disjunta. En esos casos, la métrica o comparación debe declararse como no aplicable, no como resultado omitido.

En el caso de las métricas de alerta, no corresponde medir si la configuración evaluada no incluye evaluación de patrón ni registro interno de alerta confirmada. En pruebas puramente frame-a-frame, donde sólo se evalúa la salida del detector OVD, las métricas aplicables son las de detección, rendimiento del pipeline o latencia algorítmica. La ausencia de una cadena operativa instrumentada debe declararse explícitamente como condición de no aplicación de las métricas de alerta.

Del mismo modo, no corresponde medir si la configuración evaluada no incluye un trayecto instrumentado de consulta o notificación, o si dicho trayecto no genera timestamps confiables. Esta métrica sólo debe reportarse cuando la alerta registrada pueda vincularse con un hito posterior verificable de disponibilidad, entrega o consulta en el canal definido.

Tampoco corresponde medir TTFD, SDR ni sobre imágenes estáticas, datasets sin continuidad temporal o corridas donde no se haya anotado el inicio y fin del evento. No corresponde medir Precision/Recall por severidad si la severidad no fue asignada previamente por condición o evento. No corresponde reportar deltas de fine-tuning si la baseline zero-shot no fue ejecutada sobre el mismo conjunto de evaluación o si existe filtración entre entrenamiento y test. Estas restricciones no reducen el valor del framework; delimitan su aplicación válida.


###### 17.1.7.8.3. Precisiones Operativas sobre Métricas Críticas

En , la unidad de conteo del falso positivo deberá declararse antes de medir —detección por fotograma, evento de alerta o sesión consolidada— y mantenerse idéntica en ambas corridas comparativas. Además, ambas corridas deberán conservar igual configuración experimental, salvo la activación o desactivación del tracker.

En TTFD, la primera evidencia positiva no se confunde con la alerta confirmada. Debe declararse explícitamente qué cuenta como primera evidencia positiva —umbral de confianza, criterio de matching y cualquier filtro previo aplicado—. La definición elegida para la corrida debe permanecer estable y quedar registrada en la bitácora.

En y , el hito temporal de cierre debe quedar definido antes de medir. En el primer caso, corresponde al registro interno de la alerta generado luego de la confirmación del patrón evaluado; en el segundo, a la emisión, disponibilidad o consulta verificable de la notificación en el trayecto instrumentado. Para que la medición sea válida, los logs deben permitir reconstruir la secuencia mínima entre primera evidencia positiva, patrón candidato si corresponde, patrón confirmado y alerta registrada. Si alguno de estos hitos no se instrumenta de manera confiable, la métrica de alerta debe declararse no aplicable.

En SDR, el criterio de cálculo —tiempo o fotogramas válidos— debe declararse explícitamente. Si el throughput resulta inestable, conviene privilegiar el cálculo en tiempo por sobre el conteo puro de cuadros.

En Precision/Recall por severidad, los resultados deben acompañarse del tamaño muestral utilizado, del criterio de agrupamiento aplicado y del punto operativo o umbral con el que fueron calculados, evitando mezclar severidades en una misma lectura agregada.


###### 17.1.7.8.4. Registro Mínimo por Corrida y Reporte

Todo reporte deberá conservar contexto experimental suficiente para reproducir e interpretar la corrida. Como mínimo, la bitácora debe registrar identificación, modelo, entrada, parámetros, hardware y entorno de software, temporalidad y logs, resultados y observaciones.

Antes del reporte final debe verificarse que cada métrica corresponda al alcance implementado, que las corridas comparativas usen el mismo conjunto de evaluación y que la instrumentación incluya período de calentamiento previo, duración suficiente y conservación y trazabilidad de logs crudos y artefactos de evaluación. Asimismo, toda métrica no ejecutada deberá declararse junto con la razón metodológica o instrumental de su omisión.


##### 17.1.7.9. Síntesis Parcial del Framework de Métricas

La evidencia central del prototipo no puede reducirse a métricas académicas de detección o tracking. Debe mostrar si el sistema detecta una condición relevante, la sostiene durante el tiempo requerido y la transforma en una alerta dentro de un margen compatible con su severidad. Por eso el protocolo diferencia métricas obligatorias, deseables y conceptuales: AP y Precision/Recall se conservan como base de detección, HOTA, IDF1 y CLEAR MOT como métricas de seguimiento cuando exista anotación suficiente, y NMS-AP como referencia conceptual para evaluaciones OVD de vocabulario fino (Everingham et al., 2010; Lin et al., 2014; Bernardin & Stiefelhagen, 2008; Ristani et al., 2016; Luiten et al., 2021; Yao et al., 2024).

La jerarquía de métricas no implica que todas deban ejecutarse en todos los escenarios ni sobre todas las condiciones de riesgo. Cada métrica queda subordinada a un criterio de ejecutabilidad experimental: debe existir una referencia de evaluación suficiente, el módulo que produce la señal correspondiente, instrumentación confiable mediante logs o timestamps, y una salida exportable para análisis posterior. Por esta razón, el protocolo diferencia entre métricas definidas, métricas efectivamente medibles y métricas no aplicables.

Tabla 34 Jerarquía de métricas adoptadas para el prototipo experimental


| Plano | Métricas obligatorias | Métricas deseables o conceptuales | Condición de aplicación |
| --- | --- | --- | --- |
| OVD | AP@0.5; Precision/Recall con criterio de reporte explícito. | AP@[0.5:0.95] como deseable; NMS-AP como conceptual. | Aplicable a toda condición efectivamente evaluada con ground truth de detección. |
| MOT | cuando el tracker esté integrado. | HOTA, DetA, AssA, IDF1, MOTA, IDSW y Frag sobre subsets anotados. | Sólo aplica cuando exista tracker y, para las métricas estándar, anotación temporal suficiente. |
| Pipeline | FPS efectivos; ; uso de VRAM. | Jitter; uso de GPU, RAM y CPU. | Obligatorio en toda corrida integrada. |
| Alerta | ; TTFD; SDR; Precision/Recall por severidad cuando exista evento anotado. | , si existe trayecto instrumentado de consulta o notificación. | Obligatorio cuando exista evento anotado, criterio de activación definido, evaluación de patrón y alerta registrada dentro del sistema. |

Nota. = Glass-to-Algorithm. TTFD = Time to First Detection. SDR = Sustained Detection Rate. Lo no implementado o no instrumentado debe declararse como no aplicable y no quedar implícitamente omitido.

La latencia operativa principal es , definida como el intervalo entre el inicio anotado de la condición de riesgo y la generación de una alerta confirmada y registrada dentro del sistema. Esta métrica integra la inferencia, la persistencia requerida y la evaluación del patrón. No corresponde reportarla en pruebas puramente frame-a-frame donde sólo se evalúa la salida del detector OVD. En esos casos, el análisis debe limitarse a métricas de detección, rendimiento del pipeline o latencia Glass-to-Algorithm. Cuando exista un trayecto instrumentado hacia consulta, interfaz o notificación, podrá reportarse adicionalmente como métrica complementaria.

TTFD mide el tiempo hasta la primera detección positiva válida desde el inicio anotado del evento. SDR mide la proporción del intervalo del evento durante la cual el sistema sostiene detecciones positivas. Ambas métricas sólo corresponden sobre secuencias temporales con inicio y duración anotados. No deben calcularse sobre datasets de imágenes estáticas sin continuidad temporal.

Tabla 35 Umbrales orientativos por severidad para la lectura operativa de la alerta


| Severidad | máximo orientativo | TTFD máximo | SDR mínima orientativa | Lectura operativa |
| --- | --- | --- | --- | --- |
| Crítica | 3-5 s | < 1 s | >= 0.50 | Se prioriza no omitir eventos críticos y se admite menor estabilidad inicial. |
| Alta | 5-10 s | < 3 s | >= 0.60 | Se busca equilibrio entre rapidez de respuesta y estabilidad. |
| Media | 10-20 s | < 10 s | >= 0.70 | Puede exigirse mayor evidencia antes de confirmar la alerta, con mayor tolerancia temporal. |

Nota. Los valores son orientativos y deberán calibrarse con la evidencia de validación experimental. En consolidación metodológica su función es ordenar prioridades y criterios de lectura, no fijar universales del dominio.

Finalmente, todo reporte experimental deberá conservar trazabilidad mínima de la corrida: modelo, prompts, dataset o fuente de video, parámetros, módulos habilitados, hardware, timestamps, métricas calculadas y métricas no aplicadas con su causa. Esto permite distinguir entre resultado negativo, falta de instrumentación y no aplicabilidad por alcance experimental.

Además del framework de métricas, cada ejecución deberá conservar una bitácora mínima: identificación de corrida, modelo y checkpoint, dataset o clip utilizado, resolución efectiva, parámetros relevantes, timestamps de etapas críticas, consumo de recursos y observaciones. Esta bitácora garantiza que la evidencia de validación experimental pueda reconstruirse, auditarse y discutirse.


#### 17.1.8. Protocolo Experimental Integrado


##### 17.1.8.1. Secuencia General del Protocolo

La secuencia experimental busca evitar que decisiones tardías alteren la validez comparativa del estudio. Ninguna fase que modifique el estado del modelo o del conjunto de datos debe ejecutarse antes de congelar el software relevante, los checkpoints retenidos, el test set y la estructura mínima de bitácora. Sobre esa base, el protocolo se ordena en fases sucesivas y no como un conjunto abierto de ensayos sin jerarquía.

En cada corrida, el conjunto de métricas aplicables deberá definirse antes de la ejecución según el tipo de evidencia disponible. En DBE sobre imágenes estáticas se priorizarán métricas de detección por imagen o frame; las métricas temporales —TTFD, SDR y talert-system— quedarán reservadas para secuencias o corridas con eventos anotados e instrumentación suficiente. Del mismo modo, las métricas de tracking sólo serán exigibles sobre subconjuntos con identidades persistentes o en análisis ablativos previamente definidos.

Tabla 36

Fases del protocolo experimental integrado


| Fase | Objetivo | Salida esperada | Criterio de cierre |
| --- | --- | --- | --- |
| Preparación | Congelar entorno, versiones, checkpoints, datasets retenidos y estructura mínima de bitácora. | Artefactos y configuración de corrida documentados. | Reproducibilidad básica garantizada. |
| Baseline DBE | Medir cada modelo candidato en zero-shot sobre el test set congelado. | Línea base por condición, prompt y métrica obligatoria. | Predicciones exportadas y métricas primarias calculadas. |
| Sensibilidad de prompts | Comparar familias de prompts y congelar la formulación primaria por condición. | Matriz comparativa y selección justificada. | Prompt principal y variantes de contraste definidos. |
| Pipeline y tracking | Medir tG2A, FPS, recursos y aporte del tracker. | Diagnóstico del comportamiento integrado. | Logs temporales y métricas de estabilidad disponibles. |
| Fine-tuning condicionado | Ejecutar adaptación al dominio sólo si se cumplen las condiciones metodológicas fijadas. | Variante comparativa exportada al CPN. | Comparación válida respecto de baseline y test compartido. |
| EBE complementario | Ejecutar captura continua en entorno controlado o simulado. | Evidencia de plausibilidad operativa y latencia integrada. | Eventos, timestamps y alertas registradas. |
| Reporte | Integrar métricas aplicadas, métricas no aplicables y causas de exclusión. | Informe de resultados trazable y replicable. | Se explicitan alcance, límites y condiciones de interpretación. |

Nota. La baseline zero-shot y el test congelado constituyen la base sobre la que recién puede discutirse el valor de prompts, tracking o ajuste al dominio.


#### 17.1.9. Estrategia de Adaptación al Dominio


##### 17.1.9.1. Criterio Metodológico General

La adaptación al dominio se mantiene como una rama comparativa progresiva y condicionada. No se adopta como requisito previo para demostrar la viabilidad del enfoque OVD, porque eso convertiría una hipótesis todavía no probada en un supuesto metodológico. La baseline zero-shot es el punto de partida obligatorio; el fine-tuning sólo se habilita cuando existe soporte de datos suficiente y cuando la comparación puede sostenerse sin romper la integridad del protocolo.


##### 17.1.9.2. Candidatos de Comparación y Condiciones de Decisión

En términos operativos, la comparación se concentrará como máximo en dos candidatos principales —Grounding DINO y YOLOE— por representar compromisos distintos entre expresividad semántica y eficiencia de inferencia (Liu et al., 2024; Wang et al., 2025). La decisión final sobre cuál o cuáles serán ajustados dependerá de la factibilidad real de integración, exportación y ejecución sobre el CPN, y no sólo de su rendimiento reportado en benchmarks generales.

Tabla 37

Regla metodológica de decisión para la adaptación al dominio


| Regla | Decisión adoptada | Sentido metodológico |
| --- | --- | --- |
| Existencia de baseline | Ningún ajuste se evalúa sin baseline zero-shot previa sobre el mismo test. | Sin baseline explícita no existe comparación defendible. |
| Disponibilidad de datos | Se priorizan CR-01 y CR-02; CR-03 y CR-04 quedan fuera del camino ordinario mientras no exista cobertura suficiente. | El ajuste debe concentrarse donde puede producir evidencia útil y comparaciones metodológicamente válidas. |
| Integridad comparativa | El test set debe ser compartido y permanecer congelado. | Evita leakage y falsas mejoras por cambio de evaluación. |
| Ganancia exigible | La variante ajustada debe mostrar una mejora operativamente significativa y no una ventaja marginal difícil de sostener. | Protege al protocolo de ciclos costosos de ajuste con retorno metodológico débil. |
| Costo operativo | La variante ajustada no debe comprometer materialmente la latencia ni el presupuesto de recursos del CPN. | Una mejora semántica que destruye la viabilidad operativa no fortalece al prototipo. |

Nota. La regla no prescribe que el fine-tuning deba ejecutarse; define cuándo vale la pena hacerlo sin distorsionar el objetivo principal del prototipo experimental.


#### 17.1.10. Proyección Metodológica Hacia las Instancias Posteriores

La proyección hacia instancias posteriores se concentra en esta sección para reunir las dependencias operativas entre entorno experimental, condiciones y prompts, estrategia de datos y framework de métricas.


##### 17.1.10.1. Proyección del Entorno Experimental

La principal proyección del entorno experimental hacia la instancia de análisis y diseño arquitectónico es el congelamiento temprano de la topología operativa del sistema, precisando qué funciones quedan en el CPN, qué rol efectivo tendrá el EN, si existirá procesamiento ligero en borde y cuál será la ruta primaria de ingesta y decodificación de video. Sin esa decisión, la medición de latencia y recursos quedaría contaminada por cambios simultáneos de arquitectura.

Hacia la validación experimental, toda lectura de viabilidad se ancla en el CPN. El TN interviene exclusivamente como apoyo de entrenamiento y exportación, mientras que el EBE se ejecuta bajo una topología ya congelada y documentada, de modo que la evidencia obtenida sea interpretable y reproducible.


##### 17.1.10.2. Proyección de las Condiciones de Riesgo y los Prompts

La dimensión de condiciones de riesgo y prompts proyecta hacia la instancia de análisis y diseño arquitectónico la traducción de la taxonomía conceptual en reglas ejecutables: congelar para cada condición la formulación primaria del prompt, definir la matriz acotada de variantes comparativas, explicitar la composición del vocabulario activo y decidir cómo se operacionalizan persistencia, severidad, histéresis y lógica contextual dentro del prototipo.

Esa traducción se materializa en el diseño del motor de patrones como componente lógico del plano de control: el diseño arquitectónico establece cómo las detecciones normalizadas, los timestamps, la configuración de prompts y las reglas de patrón se transforman en cambios de estado y en alertas registradas, manteniéndose desacoplado del detector OVD para preservar la posibilidad de sustituir modelos, prompts o trackers sin rediseñar la lógica de alerta.

Hacia la validación experimental, la misma dimensión establece un criterio de lectura: el desempeño se interpreta por condición y por nivel de complejidad, sin extrapolar el comportamiento del núcleo obligatorio a las condiciones espaciales o relacionales. En el núcleo del prototipo experimental, CR-01 y CR-02 se evalúan mediante persistencia temporal simple sin requerir MOT obligatorio, siempre que la evaluación se mantenga a nivel de patrón y no exija identidad individual persistente. Las condiciones de Nivel 2 se resuelven principalmente mediante reglas espaciales intra-frame, mientras que las condiciones de Nivel 3 requieren relaciones sostenidas entre entidades o entre entidades y regiones parametrizadas, con tracking o mecanismos equivalentes de asociación temporal cuando la evaluación lo exija.


##### 17.1.10.3. Proyección de la Estrategia de Datos

La proyección principal de la estrategia de datos hacia la instancia de implementación es la ejecución de la combinación de datasets seleccionados: descarga, verificación de formatos y licencias, producción efectiva de particiones según los criterios ya fijados y generación de material complementario sólo cuando resulte indispensable, sin desplazar el foco del proyecto hacia una campaña de datos desproporcionada respecto del alcance del prototipo.

Hacia la validación experimental, la estrategia de datos impone un criterio de interpretación: las condiciones con cobertura sólida o adecuada sostienen comparaciones directas; las condiciones con cobertura parcial o brechada se reportan como extensiones condicionadas, especificando qué parte fue efectivamente evaluada y qué parte sigue dependiendo de datos adicionales.


##### 17.1.10.4. Proyección del Framework de Métricas

El framework de métricas proyecta hacia la instancia de análisis y diseño arquitectónico una necesidad instrumental concreta: la arquitectura queda instrumentada desde el inicio para registrar timestamps, estados de alerta, consumo de recursos y metadatos de corrida. Sin esa instrumentación, la validación experimental no puede producir , ni diagnóstico defendible del pipeline integrado.

Hacia la validación experimental, el framework de métricas establece un criterio de cierre: la evidencia principal se apoya en métricas de alerta, sostén y desempeño del pipeline, mientras que las métricas académicas de OVD y MOT funcionan como explicación del comportamiento observado y no como sustituto del valor operativo del sistema.


#### 17.1.11. Supuestos, Riesgos de Validez y Consideraciones Ético-Legales


##### 17.1.11.1. Política de Minimización y Uso Asistivo

El marco ético-legal del proyecto se apoya en una política de minimización de datos y de uso asistivo del sistema. Cuando la evaluación utilice datasets públicos o material pregrabado sin nuevas capturas, el requisito central será respetar licencias, condiciones de acceso y límites de uso académico. Cuando el proyecto genere material propio para el EBE, deberán adoptarse salvaguardas de finalidad explícita, acceso restringido, retención acotada y ausencia de reconocimiento de identidad personal o tratamiento biométrico, conforme al régimen argentino de protección de datos personales y videovigilancia (Argentina, 2000; Disposición 10/2015, 2015).


##### 17.1.11.2. Supuestos de Interpretación

También conviene fijar con claridad los supuestos de interpretación. Primero, el prototipo es un sistema asistivo: una alerta no equivale a una sanción ni a una determinación automática de incumplimiento normativo. Segundo, la evaluabilidad de varias condiciones depende de variables no controlables del todo por el detector, como escala aparente, ángulo de cámara, oclusión o iluminación. Tercero, CR-06 presupone una parametrización espacial externa al prompt y no debe evaluarse como si el lenguaje por sí solo definiera la zona restringida. Cuarto, el EBE constituye una validación en entorno simulado o controlado, no un despliegue real en obra.

Tabla 38

Riesgos metodológicos y operativos relevantes para las instancias siguientes


| Riesgo | Impacto probable | Mitigación adoptada |
| --- | --- | --- |
| La configuración retenida excede el presupuesto de VRAM o rompe la latencia esperada del CPN. | Alto | Priorizar variantes ejecutables en la laptop, ajustar resolución y composición del vocabulario activo y justificar toda optimización sobre el CPN. |
| Persisten brechas de datos para condiciones de Niveles 2 y 3. | Alto | Mantener esas condiciones como extensiones condicionadas y producir datos complementarios sólo si no desplazan el núcleo del prototipo experimental. |
| El tracker agrega complejidad sin reducir falsas alarmas. | Medio | Medir primero ΔFPtracking y sólo exigir métricas MOT completas en subsets donde el costo de anotación esté justificado. |
| El diseño experimental se vuelve inmanejable por exceso de variables combinadas. | Alto | Sostener un diseño reducido con condición base, barridos acotados y prueba de mayor exigencia sólo sobre la configuración retenida. |
| La generación de material propio introduce dudas de privacidad o de consentimiento. | Medio | Aplicar minimización, acceso restringido y registro explícito de finalidad y condiciones de captura. |

Nota. La mitigación forma parte del diseño metodológico. En varios casos, preservar validez implica acotar el alcance antes que incrementar complejidad sin evidencia suficiente.


#### 17.1.12. Conclusiones Parciales de la Consolidación Metodológica


##### 17.1.12.1. Cierre del Alcance Metodológico

La consolidación metodológica queda cerrada con un protocolo experimental integrado, consistente con las dimensiones desarrolladas y ajustado al alcance real del prototipo. Ese cierre se expresa en seis definiciones principales: núcleo obligatorio centrado en condiciones de detección directa de Nivel 1; separación entre comparación controlada en DBE y plausibilidad operativa en EBE; estrategia de datos y partición orientada a evitar leakage; framework de métricas centrado en valor operativo de alerta; regla explícita para habilitar o descartar adaptación al dominio; y proyección metodológica que ordena el pasaje hacia diseño, implementación y validación.


##### 17.1.12.2. Articulación con las Instancias de Diseño e Implementación

Las definiciones consolidadas en esta instancia orientan directamente las etapas siguientes del trabajo. El análisis y diseño arquitectónico transforma el protocolo metodológico en una organización técnica consistente, mientras que la validación experimental produce resultados sobre las condiciones, escenarios y métricas fijadas. En todos los casos, deberá declararse qué elementos del catálogo fueron implementados, cuáles no aplicaron y cuáles permanecieron condicionados. Esa trazabilidad entre definición metodológica, diseño, implementación y validación constituye el principal resultado de esta parte del proyecto.

Alcance experimental consolidado. Establece la frontera inicial del prototipo experimental y permite priorizar el núcleo obligatorio sin convertir las extensiones condicionadas en requisitos bloqueantes. En la etapa de diseño, orienta qué capacidades deben implementarse primero y cuáles deben quedar previstas como ampliaciones posibles. En la validación, define qué condiciones integran el plano principal de evaluación y evita interpretar capacidades exploratorias como resultados plenamente validados.

Escenarios e infraestructura. Fijan el marco operativo en el que deberá interpretarse la viabilidad del sistema. Para el diseño arquitectónico, esto implica organizar la captura, el procesamiento y el eventual entrenamiento alrededor de los roles funcionales CPN, EN y TN. Para la validación, permite diferenciar la lectura de resultados entre DBE y EBE, evitando mezclar la estabilidad de una evaluación basada en datos controlados con la variabilidad propia de una captura o transmisión continua.

Estrategia de datos y partición. Condiciona la selección de datasets, la construcción de particiones experimentales y el uso de datos complementarios. Su función es sostener la comparabilidad entre la línea base preentrenada y cualquier variante ajustada al dominio, evitando contaminación entre entrenamiento, validación y prueba. De esta manera, los resultados obtenidos podrán interpretarse como evidencia experimental y no como consecuencia de una partición inconsistente.

Framework de métricas y registro. Define qué evidencia mínima deberá producir el prototipo. En la etapa de diseño, guía la instrumentación de timestamps, logs, eventos, métricas por tramo y salidas del pipeline. En la validación, establece qué debe reportarse para analizar detección, rendimiento, latencia, persistencia temporal y alertas. Las métricas se reportarán cuando existan datos, módulos e instrumentación suficientes, y se declararán no aplicables cuando esas condiciones no estén presentes.

Regla de adaptación al dominio. Ordena la posible incorporación de fine-tuning o variantes ajustadas. Esta adaptación no constituye un punto de partida obligatorio, sino una comparación condicionada a la existencia de datos suficientes, partición válida y una línea base preentrenada previamente evaluada. Su propósito es permitir una lectura controlada de mejoras o degradaciones frente al enfoque zero-shot, sin sobredimensionar el alcance real del prototipo experimental.

Supuestos y riesgos de validez. Delimitan cómo deben interpretarse los resultados futuros. En el diseño, obligan a construir módulos y pruebas dentro del alcance declarado. En la validación, evitan extrapolar evidencia parcial como si constituyera una validación plena del sistema. Esta precaución preserva el carácter experimental del trabajo y mantiene la orientación central del proyecto: evaluar si la detección open-vocabulary puede integrarse como herramienta asistiva útil para el monitoreo de condiciones de riesgo en construcción civil, sin reemplazar la supervisión humana ni asumir decisiones operativas automáticas.


### 17.2. Costos asociados

[Pendiente]

---

## Fuente: `docs/informe/entregable/96e-informe-v11-cierre-anexos-referencias.md`

> SHA-256 del bloque: `400305128d8f6cb5f6e208294f5089eedb182dc557fe109e803ed90adb08fde7`  
> Seleccion: Anexos C y D vigentes.

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

---

## Fuente: `docs/informe/ajustes/02-etapa-2-consolidacion-metodologica.md`

> SHA-256 del bloque: `3609ddddd4bb3b698cbf9997d2f0d7fe1ab6a0d00170de9679e064aee38f72bd`  
> Seleccion: documento completo.

# Etapa 2 — ajustes a la consolidación metodológica (§17.1) y a los Anexos C y D

> **Estado (2026-08-10):** relevado, **sin pase de correcciones aplicado**. El
> relevamiento es `nucleo/historicos/08-alineacion-consolidacion-metodologica.md`, que leyó el
> §17.1 completo contra lo que el proyecto construyó. Su §1 registra lo que el informe
> **valida y refuerza** (no se toca); su §2 las **desalineaciones**; su §4 las acciones.
> Este documento las convierte en ajustes con ID y las cruza con el estado real de hoy.
>
> **Particularidad de esta etapa:** varias desalineaciones **ya se resolvieron en el
> código** (el pattern set `cr01_cr02_v2` existe y es el oficial). Lo que queda
> pendiente es que **el informe lo diga** — el ajuste es documental, no de
> implementación. Están marcados 🛠️ *ya resuelto en código*.
>
> ✎ **2026-08-11 — regla de no-anacronismo (mapa, regla 5), aplicada a esta etapa:**
> el §17.1 es Etapa 2 y **se corrige como protocolo** — entran decisiones, definiciones
> y criterios (valores de configuración elegidos dentro de rangos declarados incluidos);
> **no entran resultados medidos** ni estados de implementación, que se reportan en
> §17.4/§17.5. Los ajustes AJ-2.05, AJ-2.09 y AJ-2.11 se reescribieron para respetar
> esa frontera.

| Dónde | Qué |
|---|---|
| Texto actual | `entregable/96b` (§17.1 Consolidación Metodológica + §17.2 Costos) · `entregable/96e` §19.3–19.4 (Anexos C y D) |
| Fuente del relevamiento | `nucleo/08` §1–§5 |
| Texto ya redactado | `material-etapa-3/94` §5 (diccionario de métricas, cubre `AJ-2.03`) |

---

## 1. Tablero de ajustes

| ID | Sección | Tipo | Pri | Enunciado |
|---|---|---|---|---|
| **AJ-2.01** | §17.1.5.3.3 / Tabla 24 | PRECISA | 🟠 | Severidades y ventanas: reportar los **valores efectivos** (`high`/4000 ms, `medium`/7000 ms) y que la persistencia se parametriza **en ms, no en frames**. 🛠️ |
| **AJ-2.02** | §17.1 (política de alerta) | CONTRADICE | 🔴 | El **cooldown no es del motor**: por ADR-011 la supresión de re-notificación es política del tramo de distribución. Y **`re_alerts` ≠ FP**. |
| **AJ-2.03** | §17.1.7 / Tabla 35 | CONCRETA | 🟠 | Diccionario de métricas con nombres, definiciones operacionales y umbrales — **más** las dos métricas derivadas propias, declaradas como descomposición. |
| **AJ-2.04** | §17.1.5.4.2/.5 | PRECISA | 🟠 | Ejes del protocolo de prompts que el diseño original no tenía: **vocabulario aislado vs completo**, variantes **template**, **hiperparámetros congelados**. |
| **AJ-2.05** | §17.1.5.4 | PRECISA | 🟡 | Piso muestral: **~200 instancias positivas por condición** o tamaño efectivo + IC. Declarar por cuál vía se cumplió. |
| **AJ-2.06** | §17.1.5.4.5 | EVIDENCIA | 🟠 | **Doble anotación ≥20% + kappa de Cohen: NO se hizo.** Hay que declararlo como decisión, y es la **limitación L2**. |
| **AJ-2.07** | §17.1.5.4 / Anexo C | PRECISA | 🟡 | El prompt set debe declararse construido desde el **Anexo C (Tabla C.1)**; sumar **confianza media de los TP** y **métricas por entidad componente**. |
| **AJ-2.08** | §17.1.6 / Tabla 36 | PRECISA | 🟡 | Usar los **nombres de fase de la Tabla 36** y declarar la correspondencia 1:1 con lo ejecutado (con la nota ADR-010). |
| **AJ-2.09** | §17.1.7.8 | CONCRETA | 🟠 | Instrumentación: los **cinco hitos por alerta**, **P50/P95/P99**, warm-up declarado por corrida, bitácora mínima. |
| **AJ-2.10** | §17.1.4.2.4 | PRECISA | 🟡 | Fuente EBE (H4): la **contingencia oficial se ejerció primero**; la OAK-D está integrada; el RTSP sintético es herramienta, no fuente experimental. |
| **AJ-2.11** | §17.1 / Tabla 37 | PRECISA | 🟡 | Reencuadrar el **fine-tuning (I1)** conforme **ADR-017**: rama experimental condicionada (Tabla 37) que **se ejerce como jornada completa**; condiciones de datos y protocolo, no de cómputo — la causa "presupuesto de tiempo" queda **prohibida**. |
| **AJ-2.12** | §17.1.7 | PRECISA | 🟠 | Declarar los **estados de aplicabilidad** (`not_applicable:<causa>`, ADR-006/013) y las **reglas de lectura** que ninguna métrica puede violar. |

---

## 2. Los ajustes, desarrollados

### AJ-2.01 · §17.1.5.3.3 y Tabla 24 · PRECISA · 🟠 · 🛠️ ya resuelto en código

**Qué pedía el informe.** La Tabla 24 fija PR-01 (CR-01, sin casco) severidad **Alto**,
persistencia **3–5 s**; PR-02 (CR-02, sin chaleco) severidad **Medio**, persistencia
**5–10 s**. Y §17.1.5.3.3 exige parametrizar la persistencia **en segundos, no en
frames** (la conversión depende del throughput).

**Qué había.** El control-plane usaba severidad `medium` para ambos y
`confirm_after_frames: 1`.

**Qué hay hoy.** El pattern set oficial **`cr01_cr02_v2`**: CR-01 `high` /
`confirm_after_ms: 4000`, CR-02 `medium` / `7000`, con histéresis
activación≠desactivación (`resolve_after_*`). El set con `confirm=1 frame` quedó como
**configuración de diagnóstico DBE-imágenes**, documentada como tal.

**El ajuste, entonces, es documental:** el §17.1 debe reportar los **valores efectivos**
y que caen dentro de los rangos declarados. Cruza con **R-14** en Etapa 3 (§17.3.8.2 y
Tabla 46), que es la ficha canónica de esos valores.

---

### AJ-2.02 · §17.1 · CONTRADICE · 🔴 — el cooldown no vive en el motor

**Por ADR-011 el motor emite en cada confirmación**; la supresión de re-notificación es
política del **tramo de distribución de alertas**, no de la evaluación de patrones.
Corolario que hay que escribir: **las `re_alerts` no son falsos positivos** — contarlas
como FP degrada artificialmente toda la precisión reportada.

Su ficha canónica es **R-02** (Tabla 44) en Etapa 3; acá se registra porque el §17.1
también describe la política de alerta y arrastra el mismo error.

---

### AJ-2.03 · §17.1.7 y Tabla 35 · CONCRETA · 🟠 — el diccionario de métricas

**Adoptar los nombres del informe, textuales** — no hay que inventar nada, es
transcribir §17.1.7 + Tabla 35:

| Métrica | Definición | Nota |
|---|---|---|
| **G2A** (Glass-to-Algorithm) | captura/lectura del frame → resultado algorítmico. Componentes: `t_capture` + `t_transport` + `t_preprocess` + `t_inference` | presupuesto **50–250 ms** |
| **t_alert-system** | **inicio anotado del evento** → alerta confirmada y registrada. Integra G2A + `t_track` + `t_reasoning` + `T_persistencia` | métrica operativa **principal** |
| **t_alert-notification** | complementaria; solo con trayecto instrumentado | |
| **TTFD** | inicio anotado → primera detección positiva válida (criterio declarado) | |
| **SDR** | proporción del intervalo anotado con detecciones positivas sostenidas | |
| **ΔFP_tracker** | delta de FP con/sin tracker, unidad de conteo declarada | |

Reporte temporal mínimo: **P50/P95/P99 + promedio**, con warm-up previo declarado y
timestamps monotónicos de fuente explícita.

**Y hay que declarar las dos métricas derivadas propias** (spec 40 §5.2), que **no son
del informe**: `t_capture→alert` (captura del frame de primera evidencia → alerta
registrada) y `t_compute-budget` (= `t_capture→alert` − `T_persistencia_efectiva`).
**No sustituyen a `t_alert-system`: la descomponen.** Existen porque son las únicas
métricas end-to-end computables **sin GT**, lo que permitió validar el tramo plataforma
antes de que existiera el clip bench (ADR-010).

**El texto para esto ya está escrito**: `material-etapa-3/94` §5 (redline R-10).

---

### AJ-2.04 · §17.1.5.4.2/.5 · PRECISA · 🟠 — los ejes del protocolo de prompts

El protocolo del informe (5 fases) exige tres cosas que el diseño de prompts original no
contemplaba:

1. **Contexto de vocabulario como variable**: cada prompt se evalúa **en aislamiento y
   en vocabulario completo**, porque prompts semánticamente próximos compiten. Aplicar
   al menos a las formulaciones finalistas.
2. **Variantes con template** (*"a photo of a [CLASS]"*) como eje de estructura
   sintáctica: sumar 1–2 variantes template al prompt set.
3. **Hiperparámetros congelados** (confianza y NMS constantes entre variantes de
   prompt): explicitarlo en la configuración de las corridas.

---

### AJ-2.05 · §17.1.5.4 · PRECISA · 🟡 — el piso muestral

El protocolo pide **~200 instancias positivas por condición**, o bien reportar tamaño
efectivo **+ intervalos de confianza**. En **§17.1** el ajuste es declarar la vía
elegida como decisión de protocolo (IC por bootstrap) — **el n efectivo contra ese piso
se reporta en §17.5**, que es donde el n existe (regla de no-anacronismo, mapa regla 5).

---

### AJ-2.06 · §17.1.5.4.5 · EVIDENCIA · 🟠 — la doble anotación que no se hizo

El protocolo pide **≥20% doblemente anotado, kappa de Cohen para etiquetas e IoU para
cajas**, aplicable al clip bench y a cualquier anotación nueva de estado EPP.

**No se hizo.** Es la **limitación L2** de la lista canónica, y hay que escribirla como
decisión declarada, no omitirla. Hay un contrapeso que sí conviene reportar: la
**revisión ciega del GT del lote de internet** (2026-08-09) encontró que **5 de 7
declaraciones de episodio eran errores de anotación (~71%)** — evidencia directa, y
medida en el propio trabajo, de por qué el protocolo pedía doble anotación. Eso vive en
Etapa 5 como `AJ-5.07` y como tabla **T-84**.

---

### AJ-2.07 · §17.1.5.4 y Anexo C · PRECISA · 🟡

- El catálogo de formulaciones candidatas vive en el **Anexo C (Tabla C.1)** del propio
  informe: el prompt set debe declararse **construido desde ahí**.
- Sumar **confianza media de los TP** como indicador de estabilidad por formulación.
- Para la estrategia indirecta, **métricas por entidad componente** (`person`, `helmet`,
  `vest` por separado) para atribuir la degradación — el bench ya las produce.

> ✎ **2026-08-18 — el Anexo C también trae el catálogo de DATASETS, y ahí hay dos
> precisiones que no son de esta ficha pero se escriben en la misma sección:**
> **(1)** hay que separar **candidatos evaluados** (la lista larga: SH17, Pictor-PPE,
> GDUT-HWD, SHWD, SODA, MOCS…, con por qué no se retuvieron) de **utilizados**, y dentro
> de utilizados distinguir los de **entrenamiento** (`construction_site_safety`, `chv`,
> `ppe_siabar`) de las **fuentes del banco de imágenes** (`construction_site_safety`,
> `chv`, `shel5k`) — comparten dos nombres de tres, y confundirlos es el error fácil.
> **(2)** `bench_obra` **no es un dataset**: es el estrato curado internamente a partir de
> `construction_site_safety`. Guía completa con la cadena de procedencia y una frase lista
> para el informe: **redline R-24** (`material-etapa-3/93`) y glosario `13` §4.4.

---

### AJ-2.08 · §17.1.6 y Tabla 36 · PRECISA · 🟡 — las fases

Usar los **nombres de fase de la Tabla 36** (Preparación · Baseline DBE zero-shot ·
Sensibilidad de prompts · Pipeline y tracking · Fine-tuning condicionado · EBE
complementario · Reporte) y declarar la correspondencia con lo ejecutado. Es coherencia
metodológica gratis.

**Con la nota de ADR-010:** las semanas del plan **no se leen literalmente** — vale la
correspondencia de fases y sus dependencias. Cruza con `AJ-0.03` (§14.2/§14.3).

---

### AJ-2.09 · §17.1.7.8 · CONCRETA · 🟠 — instrumentación

El informe exige, por alerta, cinco hitos con timestamp: **primera evidencia positiva ·
patrón candidato · confirmado · alerta registrada · notificación**. Estado real:

- El control-plane **persiste candidate/confirmed/alert** (`pattern_events.jsonl`) ✓
- **Falta explicitar la primera evidencia positiva** — es derivable del primer hit;
  dejarlo como campo del episodio.
- **Percentiles P50/P95/P99** en las métricas del control-plane (hoy solo promedio).
- **Warm-up declarado por corrida** (verificar en media-plane; N/A en replay).
- **Bitácora mínima por corrida** ≈ `report.json` consolidado + `effective_config`, ya
  cubierta.

**Dónde aterriza cada cosa (no-anacronismo):** el §17.1.7.8 **ya exige** los cinco
hitos — como protocolo casi no se edita. Los bullets de "estado real" de arriba son el
**cumplimiento**, y eso se escribe en **§17.4** (qué se instrumentó, con sus huecos:
percentiles solo promedio, primera evidencia derivable). Su ficha canónica en Etapa 3 es
**R-25** (§17.3.11 Tabla 50 y §17.3.13), que trae el contrato de GT temporal y los cinco
hitos juntos — a nivel de *diseño*, que sí corresponde a esa etapa.

---

### AJ-2.10 · §17.1.4.2.4 · PRECISA · 🟡 — la fuente del escenario EBE

El informe define el nodo de captura candidato (**OAK-D Pro PoE**, integrada como fuente
`oak_d` del media-plane desde 2026-07-13) **con plan de contingencia oficial: cámara IP
convencional**. En la práctica **la contingencia se ejerció primero**. Actualizar la
prioridad declarada: contingencia oficial primero, y el **RTSP sintético
(mediamtx+ffmpeg) como herramienta de desarrollo y vía de reproducibilidad DBE↔EBE con
fuente idéntica** — no como fuente experimental.

---

### AJ-2.11 · §17.1 y Tabla 37 · PRECISA · 🟡 — el encuadre del fine-tuning

> ✎ **2026-08-11 — reescrito conforme
> ADR-017 (fuente: `docs/decisiones/adr-017-fine-tuning-jornada-experimental.md`)**; *decía "la
> exclusión es por presupuesto de tiempo y por secuenciación"* — esa causa queda
> **prohibida** en el informe.

Reformular citando la Tabla 37 **tal como está escrita**: la regla *"no prescribe que
el fine-tuning deba ejecutarse; define cuándo vale la pena"* — es decir, la rama es
**experimental y condicionada desde el diseño metodológico**, no una exclusión ni un
descarte. Aclarar que **el nodo de entrenamiento existe** (clúster Mendieta, CCAD-UNC)
y que las condiciones que gobiernan la rama son **de datos y de protocolo**. ✎ **Estado
2026-08-13:** F-100.1, freeze/smoke técnico, dual gate y serving real están cerrados;
permanecen D-FT-08/T-FT-005, evaluación T-FT-031 y baseline T-FT-032. La procedencia
T-FT-023 quedó CERRADA el 2026-08-13 (snapshot tar `639e60df…`). ✎ **2026-08-15:
D-FT-08/T-FT-005, D-FT-12 y D-FT-13 firmadas; T-FT-031 y T-FT-032 cerradas la misma jornada
(doc 120, baseline 26s one-shot). Resta sólo `full-authorization.json` + `RUN` manual.** Son gates
técnicos, **no una falta de cómputo ni de plazo**. La rama **se ejerce como jornada
completa** (ADR-017): escalera T1→T2/T3 con
sus criterios pre-registrados, documentando resultados y limitaciones. **En §17.1 va
la regla y su criterio**; la jornada, el **costo T1 por extrapolación medida: ≈16 min
centrales (prudente 30–45 min; walltime 2 h) — `operacion/100` adenda; la cifra
histórica “≈1 GPU-h” quedó superada**
y sus resultados son datos posteriores y se citan donde corresponde: §17.4 (estado a
la entrega), la sección comparativa de resultados (si la jornada produjo datos a la
entrega) y §18 (`AJ-6.05`: lo que quede más allá de la escalera) — regla de
no-anacronismo.

---

### AJ-2.12 · §17.1.7 · PRECISA · 🟠 — aplicabilidad y reglas de lectura

Dos cosas que el §17.1 no declara y que gobiernan todo el §17.5:

- **Estados de aplicabilidad**: una métrica que no aplica se reporta como
  `not_applicable:<causa>`, nunca como 0 ni omitida (ADR-006 / ADR-013).
- **Reglas de lectura no negociables** (familia F-EV): reportar **por estrato y
  escenario**, nunca solo el agregado · los clips negativos **no** entran a P/R/F1 (su
  métrica son los FP) · `re_alerts` ≠ FP · el **SDR no se compara entre cadencias** ·
  `t_alert` no se compara entre densidades sin control de supervivencia.

---

## 3. 🚫 Lo que no hay que tocar

1. **Los "nombres de métrica vacíos"** de §17.1.5.3.2, §17.1.7 y Tabla 33 **no son una
   errata del documento**: son objetos de ecuación de Word que la extracción XML no
   captura. En el Word original casi seguro se ven bien. **Verificar visualmente, no
   corregir.** (Esta es una autocorrección: se había reportado como errata en `nucleo/02`
   §4.8 y `nucleo/07`, y se retiró — `nucleo/08` §3.)
2. **Todo el §1 de `nucleo/08`** — lo que el informe **valida y refuerza**. El §17.1 es
   metodológicamente sólido; lo que tiene son desalineaciones puntuales y huecos de
   concreción, no un problema de fondo.
3. **La histéresis activación≠desactivación** ya estaba pedida por §17.1.5.3.3 y ya está
   soportada. No es un agregado nuestro: es cumplimiento.

## 4. Fuentes

`nucleo/historicos/08-alineacion-consolidacion-metodologica.md` (§1 lo validado · §2.1–2.6 las
desalineaciones · §3 la autocorrección · §4 las acciones · §5 adenda de Anexos C y D,
leídos 2026-07-07) · `decisiones/adr-006`, `adr-010`, `adr-011`, `adr-013`, `adr-015` ·
`specs/40` §5.2 · `material-etapa-3/94` §5 · `gobierno/99` §4.1 (limitación L2).

---

## Fuente: `docs/informe/ajustes/07-critica-extension-y-poda.md`

> SHA-256 del bloque: `9eac33b95dff535adc583f1a881d979a6a456c996fb6c3035bc6d79e2342f474`  
> Seleccion: podas 12 a 14 aplicables a la seccion 17.1.

## 5. §17.1 Consolidación Metodológica (32.222 palabras)

**Advertencia previa:** este es el capítulo **mejor alineado** del informe — el
protocolo que describe se ejerció casi completo, y `nucleo/historicos/08` §1 documenta
que valida lo construido. La poda acá es quirúrgica, no estructural.

### PODA-12 · §17.1.6.2 Datasets de gestión directa (5.054) · C5 · 🔴
Un catálogo de 5.000 palabras de datasets, escrito **antes** de que la selección
colapsara a **3 datasets TRAIN** (`construction_site_safety`, `chv`, `ppe_siabar`) y un
benchmark (`bench_v3`, 3 fuentes) — y es exactamente lo que **R-24** marca como
inventario desactualizado. Comprimir a: ficha de los efectivamente usados + tabla de
descartados con causa (una línea cada uno). Se corrige y se poda en el mismo pase.
**Ahorro: ~3.000** · DECISIÓN → [ ]

### PODA-13 · §17.1.10 Proyección hacia instancias posteriores (637) · C4 · 🟡
Las "instancias posteriores" **ya ocurrieron** — son §17.4 y §17.5. Reemplazar por un
párrafo puente. **Ahorro: ~450** · DECISIÓN → [ ]

### PODA-14 · §17.1.4 Entorno e infraestructura (3.252) · C5 parcial · 🟡
Parámetros y detalle de infraestructura que el **Anexo B ya existe para alojar**
(1.792). Mover el detalle al anexo, dejar en el cuerpo el diseño de escenarios DBE/EBE.
**Ahorro neto: ~1.000** · DECISIÓN → [ ]

**Lo que NO se toca en §17.1:** §17.1.5 (9.426 — condiciones, patrones y protocolo de
prompts: es el protocolo que SÍ se ejerció; lo no ejercido de adentro —kappa/doble
anotación— se **declara**, AJ-2.06, no se borra) · §17.1.7 (6.605 — el framework de
métricas es la fuente del diccionario y de todo §17.5).

---

