# Secciones nuevas para Etapa 3 — texto redactado, listo para copiar

- **Fecha:** 2026-07-12 · **v2, tras auditoría adversarial** (ver `95-auditoria-y-plan-de-cierre.md`)
- **Qué es esto:** el **texto en prosa** de los redlines que requieren escritura extensa, redactado en el
  registro del informe (impersonal, académico) para que lo revises, lo corrijas y lo **pegues en el Google
  Docs**. Cada sección corresponde a un ítem de `93-redlines-etapa3.md`.
- **Convención:** el texto que se copia va en **bloques de cita** (`>`). Lo que está fuera son **notas para
  vos**, no van al informe.
- **Regla de números, no negociable:** toda cifra de este documento sale de la **tabla canónica**
  (`92-anexo-concrecion-tecnica.md` §10), que dice qué corrida y qué detector la produjo. La v1 de este
  documento tenía cifras mal atribuidas y un JSON fabricado; la auditoría los encontró. **Si una cifra no
  está en la §10 del doc 92, no entra acá.**

> ✎ **2026-08-12 — dos correcciones antes de transcribir.**
>
> 1. **La regla de números de arriba está derogada en su parte de fuente.** Desde el 2026-08-05 las cifras
>    salen de los **cuatro índices de `e-ovrt_experimental-setup/results/`** (verificables con
>    `operacion/datos/96-verificar-indices.py`); la §10 del doc 92 sirve para saber **qué corrida produjo
>    qué**, no para citar el valor. El espíritu de la regla no cambia: **si una cifra no está en un índice
>    verificable, no entra acá.**
> 2. **La fila de identidad de sujeto de la Tabla 63 (§2) estaba desactualizada y se corrigió.** Decía que
>    el componente que puebla `track_id` no está implementado: es falso desde el 2026-08-04. La corrección
>    está aplicada en su lugar, con el reparto de contenido entre §17.3 y §17.4 que exige la regla de
>    no-anacronismo. Contexto completo: `92` §4.2.
> 3. **La distribución de alertas ya no se redacta como exclusión** (§1.1 y Tabla 61): ADR-016 la reabrió
>    como **trabajo comprometido**. Aplicado abajo.

| § de este doc | Redline | Destino en el capítulo |
|---|---|---|
| §1 | R-06 | §17.3.11 — contratos concretos |
| §2 | R-07 | §17.3.11.4 — evolución del contrato (**el pedido del tutor**) |
| §3 | R-08 | §17.3.8.1 y §17.3.8.4 — transporte concreto |
| §4 | R-09 | §17.3.5 — figura nueva (vista de procesos) |
| §5 | R-10 | §17.3.13 — diccionario de métricas |
| §6 | R-11 | §17.3.14 — temporalidad de la fuente |
| §7 | R-12 | sección nueva de verificación |
| §8 | R-13 | sección nueva de límites |
| §9 | R-26 | §17.3.17/18 — extensibilidad medida |

---

# §1 — Contratos concretos (R-06 → §17.3.11)

**Nota:** el orden importa. Primero se **conserva** el principio original (los contratos estabilizan
semántica, no tecnología); después se declara que **para el núcleo eso ya se materializó**; recién ahí se
muestra. Así no parece que nos desdecimos: parece que cumplimos.

## 1.1 Párrafo de apertura — reemplaza el hedge actual

> Los contratos definidos en esta sección cumplen la función de **estabilizar la semántica de intercambio**
> entre componentes: acuerdan qué información cruza cada frontera, no cómo se codifica. Esa función se
> mantiene. Sin embargo, a diferencia de la formulación inicial del diseño, **los contratos del núcleo
> validable ya no son denominaciones preliminares**: se materializaron durante la implementación como
> modelos de datos versionados, con serialización explícita, esquema verificable e interfaces de servicio
> concretas, y existen corridas registradas que los ejercitan de extremo a extremo.
>
> En consecuencia, esta sección presenta cada contrato del núcleo en dos planos: su **función
> arquitectónica** —qué acuerda y entre qué componentes— y su **materialización efectiva** —qué estructura
> de datos, qué versión de esquema y qué interfaz lo realizan—. Los contratos correspondientes a
> capacidades **aún no materializadas**, en particular los del tramo de distribución de alertas, conservan
> su carácter preliminar, y su estado de implementación se declara explícitamente en cada caso.

*(✎ 2026-08-12 — la frase final decía "capacidades **no implementadas** … se declaran explícitamente como
tales", redacción heredada de cuando la distribución era exclusión ejercida. **ADR-016 la reabrió como
trabajo comprometido**: el contrato sigue siendo preliminar, pero el texto no puede clausurar la
implementación. Al transcribir, ajustar según el estado real a la entrega — ver `03-etapa-3` §5.)*

## 1.2 Tabla de correspondencia — contrato preliminar ↔ artefacto real

> **Tabla 61**
> *Correspondencia entre los contratos preliminares del diseño y su materialización efectiva*
>
> | Contrato del diseño | Materialización | Versión de esquema | Componente |
> |---|---|---|---|
> | RunConfig | Manifiesto de experimento + configuraciones efectivas por plano | `experiment.manifest.v1` | Soporte experimental |
> | SourceDefinition | Sección de fuente de la configuración + registro de adaptadores de ingesta | — | Plano de medios |
> | ModelProfile | Catálogo de perfiles de modelo (un archivo por variante) | — | Plano de medios |
> | PromptDefinition | Conjunto de prompts versionado, identificado en cada evento | — | Soporte experimental |
> | FrameMetadata | Unidad visual interna + bloque de fuente del evento publicado | — | Plano de medios |
> | **PerceptionEvent** | **DetectionEvent** | **`media.detection.v1`** | Plano de medios |
> | PatternDefinition | Definición declarativa dentro del conjunto de patrones | — | Plano de control |
> | PatternStateChanged | PatternStateChanged | `control.pattern_state.v1` | Plano de control |
> | AlertEvent | AlertEvent (identificador determinista, idempotente) | `control.alert.v1` | Plano de control |
> | MetricSample | MetricSample / ControlMetricSample | `media.metric.v2` / `control.metric.v1` | Ambos planos |
> | ErrorEvent | Registro de errores por corrida | — | Ambos planos |
> | Bus interno de eventos | Publicación ZeroMQ con envoltorio versionado | `bus.envelope.v1` | Frontera entre planos |
> | Repositorio de eventos | Archivos de sólo adición por corrida | — | Ambos planos |
> | Referencia temporal de evaluación | Anotación de episodios por clip | `clip_gt.v2` | Soporte experimental |
> | Reporte experimental | Reporte consolidado de corrida | — | Soporte experimental |
> | Alerta distribuida | Notificación entregada por MQTT con confirmación y registro idempotente | `control.notification.v1` | Módulo de distribución |
>
> *Nota.* Los contratos con versión de esquema declarada están implementados y verificados en corridas
> registradas.

✎ **2026-08-18:** la fila "Alerta distribuida" decía *"(preliminar — pendiente de
materialización)"* y la nota le reservaba "carácter preliminar" — quedó superado (la
cabecera de este doc ya lo anticipaba: ADR-016 la reabrió como trabajo comprometido, y
se materializó). El contrato `control.notification.v1` está **implementado y verificado**
(docs `operacion/114`/`118`; entrega MQTT QoS 1 con ledger de idempotencia), y el módulo
se dispara por HTTP desde el orquestador, igual que los otros dos servicios (ADR-019 +
ADR-020, doc 124); el subproceso quedó como fallback operativo, fuera del relato.

## 1.3 El contrato central, mostrado

> El contrato de mayor centralidad arquitectónica es el **evento de percepción**, que traduce la salida
> heterogénea del detector en evidencia perceptiva común. Se materializa como una estructura de datos
> validada, identificada por la versión de esquema `media.detection.v1`, que agrupa: la identificación de
> la corrida y de la unidad visual; la descripción de la fuente; el modelo y el conjunto de prompts
> efectivamente utilizados; el conjunto de detecciones normalizadas; y la instrumentación temporal de la
> unidad.
>
> El fragmento siguiente reproduce un evento **real** de la corrida de evaluación: la unidad visual en la
> que el sistema confirma la condición CR-01, a los 4000 ms de persistencia configurados. De las
> veintidós detecciones que contiene la unidad se muestran dos.

**Nota:** presentalo como *Figura N — Evento de percepción (extracto de artefacto real)*, en monoespaciado.
Es lo que el tutor pidió con nombre propio ("un DTO"). **Este JSON es literal** — verificado contra
`detections.jsonl`, unidad `frame_000120`. No lo "mejores" al pegarlo.

> ⚠️ **2026-08-12 — RESOLVER ANTES DE PEGAR: el `source_id` es de un clip retirado.**
> La corrida de la que sale esta línea se hizo el 2026-07-11 sobre **`cb_b01_p7`**, y ese clip
> fue **retirado del banco el 2026-08-03** (licencia sin registrar + GT generado por IA;
> `datasets/processed/clip_bench/_retired/cb_b01_p7/MOTIVO.md`). El JSON es impecable como
> **ejemplo de esquema** —no se está citando ningún resultado suyo—, pero **mete en el informe
> el identificador de un clip que no existe en el banco congelado**, y es exactamente lo que la
> trampa 5 de `GUIA-REDACTORES` §4 manda no hacer.
>
> **No se arregla editando el identificador a mano**: eso rompería la garantía de transcripción
> literal que costó una auditoría establecer (la v1 de este documento tenía un JSON fabricado).
> Las dos salidas honestas:
>
> | Opción | Qué implica |
> |---|---|
> | **(a) Re-transcribir** ✅ recomendada | Correr un replay DBE sobre un clip **del banco vigente**, y transcribir esa línea literalmente. Es barato (replay, sin GPU nueva) y deja el ejemplo por encima de toda sospecha |
> | (b) Redactar el identificador | Conservar la línea real y sustituir el `source_id` por `"<clip_id>"`, **declarando en el pie que el identificador fue omitido**. Sigue siendo honesto porque la omisión se declara, pero pierde el "esto salió tal cual de un artefacto" |
>
> Lo que **no** es opción: pegarlo tal cual y esperar que nadie pregunte qué es `cb_b01_p7`.

> ```json
> {
>   "schema_version": "media.detection.v1",
>   "event_type": "detection_event",
>   "run_id": "run_20260711_211647_dbe_grounding_dino_6114c6",
>   "unit_id": "frame_000120",
>   "source":  { "source_id": "cb_b01_p7", "source_type": "video_frame",
>                "frame_index": 120, "timestamp_ms": 4000.0,
>                "width": 1920, "height": 1080 },
>   "model":   { "name": "grounding_dino",
>                "model_id": "IDEA-Research/grounding-dino-tiny", "device": "cuda" },
>   "prompts": { "prompt_set_id": "cr01_cr02_v2_short_inline" },
>   "detections": [
>     { "detection_id": "det_000001", "label": "person",
>       "prompt_id": "person", "source_prompt": "person", "confidence": 0.8257,
>       "bbox_xyxy":      [1734.6, 300.9, 1838.2, 525.8],
>       "bbox_norm_xyxy": [0.9034, 0.2786, 0.9574, 0.4869],
>       "area_px": 23291.6, "model_name": "grounding_dino" },
>     { "detection_id": "det_000002", "label": "person",
>       "prompt_id": "person", "source_prompt": "person", "confidence": 0.837,
>       "bbox_xyxy":      [159.5, 402.2, 253.4, 639.8],
>       "bbox_norm_xyxy": [0.0831, 0.3724, 0.132, 0.5924],
>       "area_px": 22312.3, "model_name": "grounding_dino" }
>   ],
>   "timing": { "normalize_ms": 8.25, "inference_ms": 214.37,
>               "postprocess_ms": 0.2, "write_ms": 0.0, "total_ms": 214.59 }
> }
> ```
>
> El evento se **persiste antes de publicarse**: la línea escrita en el repositorio de la corrida y el
> mensaje transmitido por el bus contienen exactamente el mismo contenido. Esta propiedad, verificada, es
> la que garantiza que toda corrida ejecutada en vivo sea **re-evaluable de forma offline** produciendo
> artefactos idénticos.

## 1.4 Los contratos del plano de control

> El plano de control produce dos contratos. El **cambio de estado de patrón**
> (`control.pattern_state.v1`) registra cada transición de la máquina de estados, junto con la evidencia
> que la motivó y los hitos temporales del episodio. La **alerta interna** (`control.alert.v1`) registra la
> confirmación de un episodio de riesgo. El fragmento siguiente reproduce la alerta **real** emitida por la
> corrida de evaluación sobre el clip de obra.

> ```json
> {
>   "schema_version": "control.alert.v1",
>   "event_type": "alert_event",
>   "control_run_id": "bench_cb_b01_p7_gdino_20260712_20260712T232146Z",
>   "media_run_id":   "run_20260711_211647_dbe_grounding_dino_6114c6",
>   "alert_id": "ff1ffb62-60a9-5e19-a7b8-42d076864f14",
>   "pattern_id": "CR-01", "condition_id": "CR-01",
>   "subject_key": "CR-01:cb_b01_p7", "source_id": "cb_b01_p7",
>   "severity": "high", "state": "open",
>   "unit_id": "frame_000120", "frame_index": 120, "timestamp_ms": 4000.0,
>   "evidence": {
>     "subject": { "detection_id": "det_000013", "label": "person", "confidence": 0.502,
>                  "bbox_xyxy": [1065.4, 1005.4, 1185.9, 1081.2] },
>     "missing_class": "helmet",
>     "supporting": [ { "detection_id": "det_000021", "label": "person", "confidence": 0.4016 },
>                     { "detection_id": "det_000022", "label": "person", "confidence": 0.4147 } ],
>     "score": 0.502, "subjects_in_evidence": 3,
>     "rationale": "No se encontró evidencia de 'helmet' en la región 'upper_body' de 3 sujeto(s)."
>   },
>   "first_evidence_ms": 230525124.622, "first_evidence_unit_id": "frame_000000",
>   "alert_registered_ms": 230525159.420
> }
> ```
>
> Cuatro propiedades de estos contratos merecen ser señaladas, porque sostienen afirmaciones del diseño.
>
> **La identidad del sujeto de estado es explícita.** La clave de estado se compone como
> `(patrón, fuente)` bajo granularidad de escena, y como `(patrón, fuente, identidad)` bajo granularidad de
> sujeto. El identificador de detección **no se utiliza como identidad en ningún caso**, por las razones
> expuestas en §17.3.8.3.2.
>
> **La alerta es idempotente.** Su identificador se deriva de forma determinista del episodio que la
> origina, de modo que reprocesar una misma corrida produce el mismo identificador. Los consumidores aguas
> abajo pueden deduplicar sin necesidad de estado compartido.
>
> **La evidencia de la ausencia es auditable.** La alerta transporta el sujeto detectado, las detecciones
> de soporte, la clase de protección ausente, la región evaluada y una justificación legible. La ausencia
> no es una afirmación opaca del modelo: es una inferencia reconstruible. Este es, en términos prácticos,
> el argumento principal a favor de la estrategia indirecta adoptada en §17.3.9.2 — un prompt de negación
> produce una decisión, pero no produce esta evidencia.
>
> **El sistema confirma cuando su configuración lo prescribe.** La alerta se registra en la unidad visual
> correspondiente a `timestamp_ms = 4000,0`, que es exactamente la ventana de persistencia configurada
> para CR-01.

## 1.5 Las interfaces de servicio

> Los dos planos se ejecutan como **servicios independientes gobernados por configuración**, expuestos
> mediante interfaces HTTP. Esta materialización no estaba fijada en el diseño inicial —que deliberadamente
> difería la distribución de componentes— y se adoptó para permitir que ambos planos se dispongan en el
> mismo host o en hosts distintos sin modificar su lógica, y para que el soporte experimental pueda
> orquestar corridas de forma reproducible.
>
> **Tabla 62**
> *Interfaces principales de los servicios de la plataforma*
>
> | Servicio | Operación | Función |
> |---|---|---|
> | Plano de medios | `POST /api/runs` | Dispara una corrida. Recibe fuente, conjunto de prompts, parámetros de corrida, configuración de bus e identificador de experimento. Devuelve el identificador de corrida. |
> | | `GET /api/runs/{id}` | Estado y resumen de la corrida. |
> | | `GET /api/runs/{id}/detections` | Evidencia perceptiva paginada. |
> | | `POST /api/runs/{id}/evaluate` | Evaluación de percepción contra el conjunto de referencia. |
> | | `GET /readyz` | Disponibilidad del modelo cargado. |
> | Plano de control | `POST /api/runs` | Dispara una corrida en modo diferido o en vivo. |
> | | `GET /api/runs/{id}/alerts` | Alertas internas registradas. |
> | | `GET /api/config` | Configuración efectiva de la corrida. |
>
> Dos decisiones de diseño se materializan en estas interfaces. Primero, **el modelo no viaja en la
> petición**: se carga una única vez al iniciar el servicio, de modo que el costo de carga de pesos —del
> orden de decenas de segundos— queda fuera de la ruta crítica de la corrida; comparar modelos implica
> disponer servicios distintos, no reconfigurar uno. Segundo, **la respuesta afirmativa a una corrida en
> vivo del plano de control implica que su consumidor de eventos ya está suscripto al bus**, invariante que
> el orquestador verifica antes de disparar el plano de medios, por las razones expuestas en §17.3.8.4.

---

# §2 — Evolución del contrato de inferencia (R-07 → §17.3.11.4)

**Nota:** esta es **la** sección que responde al tutor. No promete: muestra la regla, muestra el campo, y
declara qué falta. Esa honestidad **es** el argumento.

> ## Evolución del contrato de evidencia perceptiva
>
> El evento de percepción es el contrato con mayor superficie de cambio previsible del sistema: es el punto
> por el que ingresan las capacidades perceptivas que el prototipo no ejerce —identidad persistente de
> sujeto, cinemática, pose, segmentación— y las que aún no se han considerado. Un contrato que deba
> reescribirse cada vez que el sistema aprende algo nuevo sobre la escena no es un contrato: es un cuello
> de botella. Por esa razón su regla de evolución se define explícitamente y forma parte del diseño.
>
> **Primera regla: la evolución es aditiva.** Toda capacidad nueva se incorpora como **campo opcional con
> valor por defecto**, nunca como campo requerido. Un productor que aún no computa la capacidad omite el
> campo; un consumidor que no la conoce lo ignora.
>
> **Segunda regla: un cambio aditivo no incrementa la versión del esquema.** El evento conserva su versión
> `media.detection.v1` cuando incorpora identidad de sujeto o cinemática, porque ningún consumidor escrito
> contra esa versión deja de ser válido. La versión se incrementa **únicamente** cuando cambia el
> significado de un campo existente o cuando un campo se elimina, es decir, cuando la compatibilidad se
> rompe de verdad.
>
> **Tercera regla: la versión viaja dentro del evento, no en el transporte.** El identificador de esquema
> es un campo del propio evento, tanto en su forma persistida como en su forma publicada. Un artefacto
> almacenado es, por lo tanto, **autodescriptivo**: puede releerse e interpretarse sin conocer el canal por
> el que viajó ni la versión del código que lo produjo, lo cual es una condición necesaria de la
> reproducibilidad experimental.
>
> **Cuarta regla: los consumidores toleran lo antiguo.** El plano de control acepta artefactos producidos
> por versiones anteriores del plano de medios, de modo que las corridas históricas permanecen evaluables.
>
> La tabla siguiente detalla el camino previsto para cada una de las extensiones perceptivas contempladas,
> y declara su estado efectivo en el prototipo.
>
> **Tabla 63**
> *Superficie de crecimiento del evento de percepción*
>
> | Capacidad | Materialización prevista en el contrato | Estado en el prototipo |
> |---|---|---|
> | **Identidad de sujeto** (seguimiento) | Campo opcional de identidad en la detección. Es la **única identidad válida entre frames**. | **Contrato completo en ambos planos**: el campo está definido en el esquema del productor —opcional, con la propiedad verificada de que su ausencia no altera la serialización— y el motor de patrones lo utiliza como clave de estado bajo granularidad de sujeto. **Es, además, la única extensión de esta tabla efectivamente ejercida**: la identidad se materializó como decorador de la fuente de eventos en el plano de control, activable por configuración y aplicable por igual al acople por archivo y al acople por bus, **sin modificar el contrato ni el plano de medios**. El plano de medios no emite el campo, de modo que la evidencia perceptiva persistida permanece inalterada; el núcleo validable se define sobre granularidad de escena y la granularidad de sujeto se reporta como capacidad medida (§17.4). |
> | **Velocidad y dirección** | Campos opcionales derivados. No requieren información nueva del detector: se derivan de la identidad de sujeto y de las marcas temporales **que el evento ya transporta**. | Especificado, no implementado. |
> | **Pose** | Campo opcional de puntos clave. | No implementado. El evaluador de patrones **sí parametriza la región de búsqueda según la geometría del sujeto** —la región se extiende a altura completa cuando la relación de aspecto sugiere una postura no erguida—, pero se trata de una heurística geométrica y **no de información de pose**. |
> | **Segmentación** | Campo opcional de máscara, **junto** al bounding box y no en su reemplazo, para no invalidar a los consumidores existentes. | Especificado, no implementado. |
> | **Detecciones asociadas** | Ya modelado, pero en el **plano de control**: la evidencia de patrón vincula el sujeto con sus detecciones de soporte y con la clase de protección ausente. | **Implementado.** |
>
> Este último punto expresa una frontera del diseño que conviene hacer explícita: **el plano de medios no
> asocia detecciones entre sí**. Publica evidencia perceptiva individual, normalizada y trazable; toda
> relación entre detecciones —espacial, temporal o de identidad— pertenece al plano de control. Esta
> separación es la que permite que el mismo evento de percepción sirva simultáneamente a la evaluación de
> patrones, a la evaluación de percepción contra el conjunto de referencia y a la reconstrucción
> experimental, sin que ninguna de esas lecturas contamine a las otras.
>
> Finalmente, se declara una restricción semántica que el contrato hace explícita porque su violación
> produce un error silencioso: **el identificador de detección es un índice dentro del frame y no
> constituye identidad entre frames**. Su uso como identidad temporal genera aliasing verificable: sobre
> una corrida de vídeo real, la detección identificada como `det_000001` recorre 1831 píxeles del ancho del
> cuadro —de 1920 píxeles— a lo largo de la corrida, con desplazamientos de hasta 1749 píxeles entre
> cuadros consecutivos. Es esa medición, y no una preferencia de diseño, la que fundamenta la adopción de
> la granularidad de escena para el núcleo validable.

**✎ 2026-08-12 — nota para el redactor sobre la fila de identidad de sujeto (leer antes de transcribir).**
La versión anterior de esa fila decía *"el componente que lo puebla no está implementado"*. **Era cierta el
12/07 y es falsa desde el 2026-08-04**, y da la casualidad de que es **la fila que más le importa al
tutor**: él preguntó si el evento puede sostener datos que hoy no están —tracking el primero de su lista—.
La respuesta honesta hoy es más fuerte que la que teníamos: **esa extensión se recorrió de punta a punta y
se midió**, y salió el mejor resultado del banco (identidad de sujeto contra escena, **con las mismas
detecciones bit a bit**: la ganancia es íntegramente del motor, no de la percepción).

Cómo se reparte, por la **regla de no-anacronismo**:

- **Acá (§17.3.11.4, Etapa 3)** va el **estado del contrato y el mecanismo**, sin cifra: contrato completo
  en ambos planos, productor no emisor, identidad resuelta como capacidad del consumidor por configuración.
  Eso es diseño, y corresponde a esta etapa.
- **La cifra, la comparación pareada y el trade-off van a §17.4** (`AJ-4.12`) **y §17.5**. Ahí se cita desde
  el índice de `results/`, y ahí se dice que el `track_id` **no queda en el JSONL del plano de medios** sino
  en los artefactos del control, con la trazabilidad sostenida por el determinismo del seguidor.
- **No confundir con la exclusión E-10:** lo excluido son las **métricas MOT**, no la capacidad.

Insumo verificado contra código, con ruta y línea: `92` §4.2 y su recuadro.

---

# §3 — El transporte, concreto (R-08 → §17.3.8.1 y §17.3.8.4)

**Nota:** el primer párrafo reemplaza la frase de **§17.3.8.1** ("el diseño no exige una tecnología
específica de mensajería"); el resto reemplaza **§17.3.8.4**.

> **[Reemplazo del párrafo de §17.3.8.1]** El bus interno cumple una función de **integración, no de
> razonamiento**: desacopla al productor de evidencia perceptiva de sus consumidores. El diseño no ata esa
> función a una tecnología —el mecanismo es deliberadamente sustituible—, pero el prototipo **sí adopta
> una**, y su elección, junto con las reglas de operación que se derivan de ella, se detalla en §17.3.8.4.

> ## Transporte y persistencia
>
> El diseño distingue el **canal de transporte** del **repositorio de eventos** (DA-03): el primero
> desacopla productores de consumidores; el segundo conserva los hechos para su reconstrucción. Esa
> distinción se mantiene, y la implementación la materializa de la siguiente manera.
>
> **El repositorio es la fuente de verdad.** Cada corrida escribe archivos de **sólo adición**, uno por
> tipo de hecho —evidencia perceptiva, cambios de estado, alertas, muestras de métricas, errores—, junto
> con la configuración efectiva, la procedencia de los datos y un manifiesto que registra la **versión de
> código** que produjo la corrida. El evento **se persiste antes de publicarse**: si el canal falla, el
> hecho no se pierde.
>
> **El canal transporta, y puede perder.** Se adoptó una publicación con patrón publicador/suscriptor sobre
> ZeroMQ, con serialización binaria compacta, envoltorio versionado y tópicos jerárquicos por corrida. La
> elección responde a tres criterios: no introducir un servicio intermediario pesado en el prototipo; no
> bloquear nunca la ruta crítica de inferencia; y conservar la capacidad de sustituir el mecanismo por un
> intermediario de mensajería (*broker*) sin modificar los planos, dado que la durabilidad la aporta el
> repositorio y no el canal.
>
> De la operación efectiva del canal se derivan tres reglas que forman parte del diseño y no de su
> implementación, porque su violación produce corridas inválidas.
>
> **El consumidor debe suscribirse antes de que el productor publique.** El patrón publicador/suscriptor
> **no retiene** los mensajes emitidos antes de que exista una suscripción. En consecuencia, el orden de
> disparo de una corrida en vivo es **primero el plano de control y después el plano de medios**, y el
> orquestador verifica la suscripción efectiva antes de continuar. No es una precaución: es una condición
> de corrección, y el prototipo la hace verificable — el publicador notifica las suscripciones activas, de
> modo que el sistema **comprueba** que hay un consumidor escuchando en lugar de suponerlo.
>
> **La pérdida se detecta, no se supone.** Un publicador con cola acotada **descarta mensajes en silencio**
> al saturarse, sin señalar error al emisor. Por esa razón cada mensaje transporta un **número de secuencia
> monótono**, y el consumidor contabiliza los huecos: una corrida con huecos se marca **degradada**, con su
> causa registrada. La corrida degradada no se descarta ni se silencia: se declara, y sus métricas se
> interpretan a la luz de esa declaración.
>
> **El canal no frena la percepción.** La publicación es no bloqueante: ante saturación, el sistema
> prefiere **descartar y declarar** antes que introducir contrapresión sobre la ruta crítica de vídeo, en
> coherencia con el principio de protección de la ruta crítica (§17.3.4).
>
> Como consecuencia de estas reglas se verifica una propiedad que sostiene la comparabilidad entre
> escenarios: **una corrida ejecutada en vivo y la relectura offline de sus artefactos producen resultados
> idénticos**. El escenario EBE no constituye, por lo tanto, un régimen de medición distinto, sino la misma
> cadena alimentada por una fuente de naturaleza temporal diferente.
>
> Finalmente, se registra una frontera de consumo: **el bus es interno a la plataforma**. La interfaz de
> inspección no consume el canal de eventos, sino las interfaces de servicio de ambos planos. Esto evita
> que una herramienta de observación introduzca acoplamiento con el mecanismo de transporte, que es
> deliberadamente sustituible.

---

# §4 — Figura nueva: vista de procesos (R-09 → §17.3.5)

**Nota:** esto **no** es texto para pegar: es la especificación de la figura. La Figura 4.1 actual se
**conserva** (es la vista lógica). Ésta es la segunda: la que muestra "cómo está hecho".

**Título propuesto:** *Figura N — Vista de procesos de la plataforma experimental*

**Cajas (procesos reales):**

| Caja | Etiqueta | Contenido |
|---|---|---|
| 1 | **Servicio de medios** | Ingesta → control de ritmo → normalización → inferencia OVD → postproceso → publicación. Modelo cargado al arranque. |
| 2 | **Servicio de control** | Consumo de eventos → motor de patrones → alertas internas → persistencia → métricas. |
| 3 | **Orquestador experimental** | Manifiesto de experimento; dispara ambos servicios; consolida artefactos; genera el reporte. |
| 4 | **Interfaz de inspección** | Cliente de las interfaces de servicio de ambos planos. |
| 5 | **Módulo de distribución** | Consumidor externo funcional: política, ledger, MQTT y registros. Marcar por separado las integraciones pendientes. |
| 6 | **Repositorio de corrida** | Archivos de sólo adición, uno por plano. |

**Flechas:**

- Orquestador **→** Servicio de control (corrida en vivo) — **1º**; su respuesta afirmativa implica suscripción activa.
- Orquestador **→** Servicio de medios (con bus habilitado) — **2º**. *Etiquetar el orden: es una regla de corrección, no un detalle de implementación.*
- Servicio de medios **→ bus →** Servicio de control. Etiqueta: evento de percepción + ciclo de vida de corrida.
- Servicio de medios **→** Repositorio, con la flecha **numerada antes** que la del bus (persiste primero, publica después).
- Servicio de control **→** Repositorio.
- Servicio de control **→ canal de alertas →** Módulo de distribución. La flecha es
  efectiva; anotar que su lanzamiento todavía no forma parte de la orquestación integral.
  ✎ **2026-08-18: la segunda cláusula quedó superada** — el lanzamiento SÍ forma parte de
  la orquestación integral desde el 2026-08-13, y desde ADR-019/ADR-020 **el orquestador
  lo dispara por HTTP** contra su propio servicio (`:8082`), igual que a los otros dos.
  En la figura, el módulo va con **línea continua** y flecha del orquestador hacia él,
  idéntica a las de medios y control.
- Interfaz de inspección **→** ambos servicios. **No hay flecha del bus a la interfaz de inspección**: esa ausencia comunica una frontera de diseño.
- Repositorio **→** Orquestador (consolidación y reporte).

**Nota al pie de la figura (esto sí va al informe):**

> *Nota.* La figura representa la disposición efectiva de procesos del prototipo, complementaria de la
> vista lógica de la Figura 4.1. Los dos planos se ejecutan como servicios independientes gobernados por
> configuración, y pueden disponerse en un mismo host o en hosts distintos sin modificar su lógica. El
> módulo de distribución se representa en línea punteada por corresponder a una capacidad especificada y no
> implementada dentro del alcance del prototipo.

✎ **2026-08-18 — REEMPLAZO de la nota al pie (la de arriba quedó falsa; usar esta):**

> *Nota.* La figura representa la disposición efectiva de procesos del prototipo, complementaria de la
> vista lógica de la Figura 4.1. Los tres módulos de la cadena se ejecutan como servicios independientes
> gobernados por configuración, y pueden disponerse en un mismo host o en hosts distintos sin modificar
> su lógica. El módulo de distribución admite dos modos de ejecución equivalentes en semántica: como
> proceso lanzado y supervisado por el orquestador experimental, o como servicio propio con interfaz
> de red; la selección es una decisión de despliegue, no de diseño.

---

# §5 — Diccionario de métricas (R-10 → §17.3.13)

> ## Definiciones operacionales de las métricas
>
> Las métricas del framework metodológico se instrumentan sobre las señales observables descritas en la
> sección anterior. Para que una medición sea reproducible e interpretable no basta con nombrarla: es
> necesario declarar **qué evento la inicia, qué evento la cierra, en qué unidad se expresa y bajo qué
> condiciones es aplicable**. La tabla siguiente cumple esa función.
>
> **Tabla 64**
> *Diccionario de métricas: definiciones operacionales*
>
> | Métrica | Inicio (t₀) | Cierre (t₁) | Unidad | Condición de aplicabilidad |
> |---|---|---|---|---|
> | **G2A** | Captura de la unidad visual | Fin de la inferencia | ms (p50/p95/p99) | Requiere reloj único. **No interpretable** cuando el trayecto atraviesa dos hosts (relojes monotónicos no comparables). Presupuesto declarado: 50–250 ms. |
> | **TTFD** | Inicio anotado del episodio | Primera detección positiva dentro del episodio | ms | Requiere referencia temporal anotada. Si no hay detección positiva en el episodio, se declara **nula con causa**, nunca cero. |
> | **t_alert-system** | Inicio anotado del episodio | Registro de la alerta interna | ms | Requiere referencia temporal anotada. |
> | **Latencia de alerta interna** | Primera evidencia perceptiva del episodio | Registro de la alerta interna | ms (p50/p95/p99) | Calculable sobre toda fuente temporal; **no requiere anotación**. |
> | **SDR** | — | — | proporción [0,1] | Fracción del episodio anotado cubierta por detección positiva continua. Requiere referencia temporal anotada. |
> | **Precisión / Exhaustividad / F1** | — | — | proporción | Evaluadas **a nivel de episodio**, no de frame. Las alertas sucesivas de un mismo episodio no se computan como falsos positivos. |
> | **t_alert-notification** | Registro de la alerta interna | Confirmación de entrega | ms | **No aplicable** si no hay canal de distribución habilitado. |
> | **t_capture→alert** *(derivada)* | Captura del frame que aporta la primera evidencia | Registro de la alerta interna | ms | Requiere reloj de pared en la fuente. **No interpretable** sobre fuentes de archivo (tiempo de medio). |
>
> Tres precisiones metodológicas acompañan a este diccionario.
>
> **Criterio de relojes.** Las latencias internas a un nodo se miden con un reloj monotónico local. Las
> latencias de extremo a extremo se miden **en un único reloj**. Cuando el trayecto atraviesa dos hosts,
> los relojes monotónicos respectivos **no son comparables entre sí** y su diferencia carece de
> significado; en esa situación la métrica se declara **no interpretable**, con su causa registrada, en
> lugar de publicar un valor. Esta regla es la razón por la cual la instrumentación de la topología de dos
> nodos reporta una ausencia declarada y no un número.
>
> **Una métrica derivada, declarada como tal.** La instrumentación incorpora la magnitud
> `t_capture→alert`, que mide el trayecto desde la captura del frame que aporta la primera evidencia hasta
> el registro de la alerta. **No forma parte del framework metodológico original** y se declara como
> instrumento auxiliar de este trabajo: su función no es sustituir a la métrica oficial de latencia de
> alerta, sino **descomponerla**, separando el tiempo que el sistema consume del tiempo que el sistema
> *espera por diseño* —la ventana de persistencia exigida por el patrón—.[^1]
>
> **El criterio de detección positiva no se reimplementa.** La evaluación de alertas contra la referencia
> anotada reutiliza el **mismo evaluador** que emplea el motor de patrones en tiempo de corrida, en lugar
> de redefinir qué constituye una detección positiva. Esta decisión elimina una fuente de error silencioso:
> la divergencia entre el criterio con el que el sistema decide y el criterio con el que el sistema es
> evaluado.
>
> [^1]: Descontando de `t_capture→alert` la persistencia efectivamente exigida se obtiene el tiempo de
> cómputo real del trayecto. Ambas magnitudes son auxiliares y se reportan junto a la métrica oficial,
> nunca en su lugar.

**Nota:** bajé deliberadamente el tono del pasaje de las métricas derivadas. En la v1 las presentaba como
"aporte instrumental propio" con una identidad algebraica — sonaba lindo y **te invitaba a que el tribunal
lo auditara**. El diccionario y el criterio de relojes son lo valioso; `t_compute-budget` va a nota al pie
y no se vende como contribución.

---

# §6 — Temporalidad de la fuente (R-11 → §17.3.14, subsección nueva)

> ## Naturaleza temporal de la fuente y aplicabilidad de la evaluación de patrones
>
> La distinción entre DBE y EBE se formula en términos del **origen** de la fuente visual. Existe, sin
> embargo, una segunda distinción, independiente de la anterior y con consecuencias directas sobre la
> interpretación de los resultados: la **naturaleza temporal** de la fuente.
>
> Una fuente de vídeo —un archivo o un flujo en vivo— produce unidades visuales **ordenadas en el tiempo**,
> sobre las cuales la noción de persistencia tiene sentido. Un conjunto de imágenes independientes, en
> cambio, produce unidades **sin relación temporal entre sí**: la persistencia de una condición no es una
> propiedad observable, porque no hay continuidad que observar.
>
> Esta diferencia genera un **modo de falla silencioso** que conviene documentar. Un conjunto de patrones
> configurado con una ventana de persistencia, evaluado sobre un conjunto de imágenes independientes,
> produce **cero alertas por construcción**: ningún episodio puede sostenerse porque no hay sucesión
> temporal que lo sostenga. El resultado —cero alertas— es **indistinguible** de la conclusión legítima "no
> hubo condiciones de riesgo en los datos". Se verificó empíricamente: sobre el conjunto de referencia, la
> evaluación registró **77 transiciones de patrón y ninguna alerta**.
>
> La plataforma **deriva la naturaleza temporal de la fuente** a partir del tipo de fuente declarado —no
> es un parámetro que el operador pueda contradecir— y, cuando la fuente no es temporal, declara la
> evaluación de patrones como **no aplicable, con su causa**, en lugar de reportar un cero interpretable
> como ausencia de riesgo. La corrida no se rechaza: conserva su valor como verificación del contrato entre
> planos y como diagnóstico de la asociación espacial, pero **sus alertas no se interpretan como una
> medición de persistencia**.
>
> En términos del framework de evaluación, esto significa que **cada tipo de fuente sostiene un tipo
> distinto de afirmación**: los conjuntos de imágenes permiten medir percepción y asociación espacial; los
> clips de vídeo con anotación temporal permiten medir patrones, latencia de alerta y continuidad; las
> fuentes en vivo permiten, además, medir el comportamiento de extremo a extremo bajo condiciones de
> transmisión continua. Confundir estos regímenes no produce un error visible, sino un número correctamente
> calculado sobre una pregunta equivocada — que es precisamente el tipo de error que la política de
> aplicabilidad de métricas (§17.3.13.3) fue diseñada para impedir.

---

# §7 — Verificación: qué funciona y cómo se midió (R-12 → sección nueva)

**Nota — leé esto antes de copiar.** La v1 de esta tabla tenía tres problemas que la auditoría encontró y
que en una defensa hubieran sido letales: (a) atribuía cifras a la corrida equivocada; (b) presentaba como
"dentro de presupuesto" una latencia medida **con detector simulado**, cuando el detector real está diez
veces por encima; y (c) llamaba "métricas" a lo que es una verificación de instrumento sobre **un solo
clip con dos alertas**. La v2 dice la verdad — y la verdad, contada así, **es más fuerte**.

> ## Verificación del diseño sobre el sistema implementado
>
> El criterio de cierre adoptado (§17.3.17) establece que una unidad se considera completa **cuando produce
> evidencia verificable dentro de una corrida experimental**. Esta sección presenta esa evidencia. Todas
> las mediciones proceden de corridas ejecutadas sobre la plataforma implementada, con sus artefactos
> conservados y reproducibles. Se indica en cada caso el detector utilizado, dado que la naturaleza del
> detector condiciona la interpretación de las latencias.
>
> **Tabla 65**
> *Evidencia de verificación del núcleo validable*
>
> | Propiedad verificada | Condiciones | Resultado |
> |---|---|---|
> | El pipeline de percepción opera sobre vídeo real de obra | Clip de 733 unidades, detector open-vocabulary en GPU | **0 fallos**, 15.914 detecciones, latencia de inferencia p50 220 ms / p95 267 ms, 4,39 fps efectivos |
> | El repositorio y el canal transportan lo mismo | Corrida en vivo por bus, releída de forma offline (detector de referencia) | Artefactos **idénticos**; ninguna unidad perdida |
> | La cadena completa cierra en vivo | Corrida en vivo de 300 unidades (detector de referencia) | 300/300 unidades, **0 pérdidas**, dos alertas registradas, cierre por evento de fin de corrida |
> | Las ventanas temporales operan según su configuración | Corrida sobre vídeo con persistencia declarada | CR-01 confirma en **t = 4000 ms**; CR-02 en **t = 7000 ms** (valores configurados) |
> | La granularidad de escena no degrada la evaluación | Comparación de granularidades sobre el mismo corpus | **F1 = 1,0** en ambas; invariante de conteo de sujetos verificada |
> | La instrumentación de latencia **detecta el incumplimiento** | Presupuesto declarado 50–250 ms | Con detector de referencia: p95 = **31,8 ms** (dentro). Con el detector open-vocabulary evaluado: p95 = **2604 ms**, y el sistema lo **declara fuera de presupuesto** |
> | La cadena completa computa las cinco métricas del framework sobre referencia temporal anotada | **Verificación de instrumento**: 1 clip de obra real, GT preliminar, 2 alertas observadas | Precisión 0,50 · Exhaustividad 1,00 · F1 0,67 · t_alert-system 4000 ms · TTFD 0 ms · SDR 0,999 |
>
> Tres comentarios acompañan a esta tabla, y son parte del resultado.
>
> **La instrumentación se cumple; el detector no.** La medición de latencia captura-a-resultado opera
> correctamente y compara contra el presupuesto declarado. Con el detector open-vocabulary evaluado, ese
> presupuesto **no se cumple**, y el sistema lo señala. Este resultado es consistente con la evaluación
> comparativa de modelos: los detectores capaces de sostener CR-01 no siguen el ritmo de una cámara, y los
> que lo siguen no sostienen CR-01. **La restricción operativa está en el detector, no en la plataforma**, y
> el instrumento sirve precisamente para localizarla. Un instrumento que sólo devolviera resultados
> favorables no sería un instrumento.
>
> **La verificación de instrumento no es un resultado experimental.** Las cinco métricas de la última fila
> se computaron sobre **un solo clip**, con una anotación de referencia **preliminar** —revisión visual
> asistida, pendiente de validación humana definitiva— y sobre **dos alertas observadas**. Demuestran que
> la cadena de medición está completa y es correcta; **no** constituyen una medición del desempeño del
> sistema, que requiere el banco completo de clips anotados. Se reportan aquí como cierre del diseño, no
> como resultado.
>
> **El falso positivo es información.** La única alerta no esperada corresponde a una condición CR-02
> emitida cuando el detector pierde transitoriamente el elemento de protección de un trabajador que sí lo
> porta. No es un defecto de la plataforma ni un error de la evaluación: es exactamente el tipo de
> comportamiento que el instrumento fue construido para **medir**.

---

# §8 — Registro del alcance efectivo y brechas (R-13 → sección nueva)

**Nota:** ✎ **actualizada el 2026-08-12** contra los resultados cerrados y
`operacion/114`. La versión inicial mezclaba capacidades aún no ejercidas con exclusiones;
varias se implementaron después. Esta tabla registra el estado final sin borrar esa
cronología.

> ## Alcance efectivo: capacidades no ejercidas
>
> El diseño distingue desde su formulación entre el **núcleo validable** y las **extensiones
> condicionadas**. Cerrado el ciclo de implementación, corresponde declarar con precisión qué capacidades
> fueron efectivamente ejercidas y cuáles permanecen especificadas sin materializar. Esta declaración no
> constituye una enumeración de faltantes, sino el registro del alcance conforme a las reglas de exclusión
> establecidas **con anterioridad a la obtención de resultados**.
>
> **Tabla 66**
> *Capacidades ejercidas, exclusiones y brechas de integración*
>
> | Capacidad | Estado | Consecuencia declarada |
> |---|---|---|
> | **Identidad persistente de sujeto** | **Implementada y medida** como decorador de fuente del control-plane; el media-plane no la persiste en su JSONL | G1 se reporta como capacidad medida; el núcleo validable conserva G0. Las métricas MOT continúan excluidas. |
> | **Comparación de estrategias de detección** (directa, indirecta, híbrida) | **Implementada y evaluada** | E-IND queda como núcleo; E-DIR fue vetada por precisión y E-HYB-or fue ejecutada y refutada. Las cifras pertenecen a §17.5, no a esta sección de diseño. |
> | **Distribución de alertas** (canal de notificación) | **Funcionalmente implementada** | DBE/EBE, cooldown, idempotencia, MQTT QoS 1 y reporte fueron verificados. Quedan la vista de webconsole, la orquestación y versionar el repo. |
> | **Latencia captura-a-resultado en topología de dos nodos** | Instrumentada; **no computable** | Los relojes monotónicos de hosts distintos no son comparables: la métrica se declara **no interpretable**, con causa, en lugar de publicarse. |
> | **Comparación con modelo adaptado** (ajuste fino) | Rama experimental comprometida; **T1 full en NO-GO técnico** (adenda ADR-017, 2026-08-13) | F-100.1, freeze/smoke, dual gate, serving y procedencia T-FT-023 están cerrados (snapshot `639e60df…`). ✎ **2026-08-15: D-FT-08/T-FT-005, D-FT-12 y D-FT-13 firmadas, y T-FT-031/032 cerradas la misma jornada** (doc 120: baseline 26s one-shot — `bare_head` AP50 0,000, recall CR-01 agregado 0,0002); resta `full-authorization.json` + `RUN` manual. La causa es técnica/protocolar, nunca temporal; se declarará el estado real a la entrega. |
> | **Métricas de seguimiento multiobjeto** | **No aplicables** | No se dispone de anotación de identidades; su cómputo carecería de referencia. Caso ejemplar de la política de aplicabilidad. |
> | **Condiciones de riesgo de nivel 2 y 3** | Especificadas, no implementadas | Excluidas conforme al núcleo validable declarado. Se conservan la definición de sus patrones y su vocabulario. |
> | **Comparación DBE / EBE sobre fuente idéntica** | Paridad de transporte y de reparto **VERIFICADA** | Replay/live producen artefactos de distribución idénticos. El anclaje de sincronización entre reloj de captura y tiempo de media para EBE-desde-clip sigue **NO implementado** (`operacion/97`): la paridad plena queda acotada a lo verificado. |
>
> Se registran, además, dos limitaciones conocidas del procedimiento de evaluación. Primera: el
> emparejamiento entre alertas observadas y episodios anotados se resuelve de forma voraz, lo cual puede
> subestimar la exhaustividad en escenarios con múltiples episodios simultáneos de una misma condición y
> ventanas solapadas; la solución correcta —emparejamiento bipartito óptimo— está identificada y su efecto
> se acota a los escenarios de ese tipo. Segunda: el GT temporal vigente es humano y está
> congelado, pero no tuvo una segunda anotación independiente ni estadístico de acuerdo;
> esa limitación se declara como L2.

---

# §9 — Extensibilidad medida (R-26 → §17.3.17 / §17.3.18)

**Nota:** esta sección **no estaba** en la v1 y es, probablemente, la más valiosa de todas para tu defensa.
Tu tesis no es "OVD detecta mejor" — es **"qué se logra con condiciones en lenguaje, sin entrenar"**. Todo
lo demás del capítulo mide latencias y pérdidas: **esto mide lo único que un detector cerrado no puede
hacer.** El mini-experimento A1 se ejecutó y verificó: acá queda el mecanismo y su costo
de cambio; la cifra medida corresponde a §17.4/§17.5 por no-anacronismo.

> ## Extensibilidad de la plataforma: costo de incorporar una condición nueva
>
> Una arquitectura orientada a la detección open-vocabulary sólo resulta justificada si la incorporación de
> una condición de riesgo nueva es efectivamente más barata que en una arquitectura de vocabulario cerrado.
> Esa afirmación no debe postularse: debe **medirse**. La tabla siguiente declara el costo real de cada
> tipo de extensión sobre el sistema implementado.
>
> **Tabla 67**
> *Costo de extensión de la plataforma*
>
> | Extensión | Qué requiere | Costo |
> |---|---|---|
> | Una **condición nueva del mismo tipo** (sujeto sin elemento de protección) | Una entrada declarativa en el conjunto de patrones —clase del sujeto, clase ausente, región, umbrales, ventana temporal— y las formulaciones de prompt correspondientes | **Sólo configuración. Sin reentrenamiento y sin código.** |
> | Una **familia nueva de condiciones** (relacional, zonal, de trayectoria) | Un evaluador nuevo en el motor de patrones | Código acotado al evaluador; el resto de la cadena no se modifica |
> | Un **modelo de detección nuevo** | Un adaptador que normalice su salida al contrato de evidencia perceptiva | Código acotado al adaptador |
> | Una **fuente visual nueva** | Un adaptador de ingesta que produzca unidades visuales normalizadas | Código acotado al adaptador |
> | Un **canal de notificación nuevo** | Un consumidor del contrato de alerta | Externo a los dos planos |
>
> El contraste entre la primera y la segunda fila delimita, con precisión, **la frontera real de la
> extensibilidad por lenguaje**: una condición expresable como ausencia de un elemento observable sobre un
> sujeto observable se incorpora por configuración; una condición que requiere una relación nueva entre
> entidades requiere un evaluador. Declarar esa frontera —en lugar de afirmar genéricamente que "todo es
> configurable"— es la contribución arquitectónica que este trabajo sostiene.
