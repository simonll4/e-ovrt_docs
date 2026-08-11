# Relevamiento del informe (Etapa 3) frente a la implementación real — y respuesta a la observación del tutor técnico

> **✎ Actualización 2026-07-18 (doc 56):** desde este relevamiento (07-12) la plataforma
> sumó elementos arquitectónicos que el capítulo tampoco refleja y que se suman a la
> lista del §4 al escribir: (a) **OAK-D Pro PoE como fuente viva** + **prefilter EN-2
> on-device** opcional (fail-open, 87 % drop A/B) + métrica `capture_to_host_ms`;
> (b) **ledger por-frame de descartes** `media.dropped_unit.v1`; (c) **progreso parcial
> de patrones** `control.pattern_progress.v1` (observabilidad sin tocar la máquina de
> estados); (d) **vista correlacionada media↔control** por `unit_id` en la consola
> (evidencia visual de la trazabilidad extremo a extremo — argumento de extensibilidad);
> (e) **sesiones de preview en vivo** (posicionamiento de cámara + prueba de prompts sin
> corrida persistida); (f) gestión completa del ciclo de corridas desde la consola
> (borrado orquestado, `DELETE` en ambos planos). Fuente:
> [`operacion/56`](../../../operacion/56-relevamiento-plataforma-2026-07-18.md).

- **Fecha:** 2026-07-12
- **Insumo primario:** `informe/entregable/E-OVRT-VDP_Etapa_3_Diseno_Arquitectonico.docx` (§17.3.1–17.3.18, docx del 2026-07-06),
  texto plano en `informe/entregable/90-etapa3-texto-extraido.md`. **Es la versión vigente**: la Etapa 3 embebida
  en `E-OVRT-VDP_v1.1_05062026-sin-indice.docx` está desactualizada y no debe usarse como fuente.
- **Contrastado contra:** los cuatro repos (`e-ovrt_media-plane`, `e-ovrt_control-plane`,
  `e-ovrt_experimental-setup`, `e-ovrt_datasets`), los ADR-001…014, las specs 40–45 y los docs de
  operación 30–55.
- **Complementa (no reemplaza):** `nucleo/historicos/02-revision-critica-etapa3-y-norte.md` (crítica de julio 6,
  cuando casi nada de esto estaba construido) y `nucleo/historicos/08-alineacion-consolidacion-metodologica.md`.
- **Entregas asociadas:** `92-anexo-concrecion-tecnica.md` (material verificado + **tabla canónica de
  cifras**), `93-redlines-etapa3.md` (los 26 redlines con casilla de decisión), `94-secciones-nuevas-etapa3.md`
  (el texto redactado) y `95-auditoria-y-plan-de-cierre.md` (la auditoría de todo esto + el plan a 11 semanas).
- **⚠️ v2 — 2026-07-12.** Este documento fue **auditado adversarialmente** y corregido: había cifras mal
  atribuidas, una sobrevendida (G2A) y un dato falso (el aliasing "entre frames consecutivos"). Las
  correcciones están marcadas en línea. El detalle completo, en el doc 95.

---

## 1. Veredicto en una página

**El tutor tiene razón, y el problema es reparable con lo que ya existe.** La brecha que él ve no es
una brecha de sistema (el sistema está construido, corre de punta a punta y produce las cinco
métricas de la tesis): es una **brecha de documento**. El capítulo 17.3 se escribió el 2026-07-06,
antes de que existieran los servicios, el bus, el runner y el laboratorio de GT, y está redactado
íntegramente en modo prospectivo. Un dato objetivo del relevamiento del texto:

> **En las 1246 líneas del capítulo no hay una sola cifra, un solo nombre de clase, un solo endpoint,
> un solo esquema serializado, un solo formato de archivo, ni un solo resultado medido.** No hay
> "el sistema hace"; hay "el sistema deberá". Las seis figuras están vacías y cinco de ellas sin numerar.

Eso era correcto para un capítulo de *diseño arquitectónico* escrito antes de implementar. Deja de
serlo ahora, porque hoy podemos responder cada una de esas preguntas con evidencia. Y el hedge que el
tutor cita textualmente —"no imponen una tecnología, un formato de serialización ni una estructura de
código específica"— hoy es **falso por exceso de humildad**: sí hay tecnología (ZeroMQ + msgpack, HTTP,
JSONL), sí hay formato (`media.detection.v1`), y sí hay clases (`DetectionEvent`, `AlertEvent`,
`PatternStateChanged`, todas Pydantic, todas con `schema_version` en el payload).

Hay además un segundo hallazgo, independiente del tutor y **más grave para la defensa**: el capítulo
tiene tres afirmaciones que la implementación **contradice**, no que meramente precisa. Si el
documento final las conserva, el tribunal encontrará un sistema que hace lo contrario de lo que su
propio capítulo de diseño declara.

Ese es el trabajo: **(A)** reparar tres contradicciones, **(B)** concretar los contratos como pide el
tutor, **(C)** agregar la evidencia de que funciona y de cómo se mide, **(D)** erratas.

---

## 2. Qué pide exactamente el tutor, traducido a requisitos verificables

La observación tiene tres pedidos distintos. Vale separarlos porque tienen costos muy distintos.

| # | Pedido (sus palabras) | Traducción operativa | Costo |
|---|---|---|---|
| **T1** | "una concreción técnica (que sería *cómo está hecho*)" — "no siempre se evidencia cómo se implementan concretamente (clases, APIs, servicios)" | Para cada contrato conceptual, mostrar el artefacto real: **la clase**, **el JSON serializado**, **el endpoint**. Bastan ejemplos, no exhaustividad ("No espero un detalle extremo, pero sí algo como un DTO / una API `POST /events/detection` / una `class DetectionEvent`"). | **Bajo.** Todo existe; hay que transcribirlo. Ver `92-anexo-concrecion-tecnica.md`. |
| **T2** | "evidencia (qué funciona y cómo se mide para saber si funciona bien)" — "se llegue a un sistema ejecutable y **verificable**" | Números reales de corridas reales, con el procedimiento de medición: definiciones operacionales t0/t1 de cada métrica, y al menos una corrida end-to-end reportada. | **Bajo-medio.** Los números existen (docs 31/33/34/35/37/38/39/51/54). Falta escribirlos. |
| **T3** | "ser muy claro en la definición de eventos tipo inferencias para que den soporte a datos que a lo mejor hoy no están, pero mañana sí: tracking, velocidad, dirección, eventualmente pose o segmentación" | **Es el pedido más profundo y el más fácil de subestimar.** No pide implementar tracking: pide que el contrato del evento de detección esté diseñado para **crecer sin romperse**, y que eso esté escrito. | **Medio.** La regla existe (spec 40 §1: evolución aditiva sin bump de versión) y `track_id` ya está en el contrato del consumidor — **pero el media-plane no lo emite**. Hay que documentar la regla y ser honestos sobre el estado. |

**T3 merece una nota, porque es donde el tutor puso el dedo en algo real.** Hoy `Detection` (media-plane,
`contracts/detection.py:28`) **no tiene** `track_id`, ni `attributes`, ni ningún bolsillo de extensión;
mientras que `Detection` (control-plane, `contracts/media.py:11`) **sí tiene** `track_id: str | None`, y
el motor ya lo consume. Es decir: **la costura de extensión está abierta del lado consumidor y cerrada
del lado productor.** El capítulo debe (a) declarar la regla de evolución, (b) mostrar el evento con sus
campos futuros como opcionales, y (c) decir con todas las letras qué está emitido hoy y qué no.

---

## 3. Las tres contradicciones (prioridad máxima — no son de forma)

### 3.1 §17.3.9.2 adopta la estrategia equivocada como núcleo

**Dice el capítulo:** la estrategia del núcleo para CR-01/CR-02 es la **detección directa mediante prompts
de ausencia** ("person without hard hat"); las consultas positivas quedan como "diagnóstico que no
confirma ausencia".

**Hace el sistema:** exactamente lo contrario. El prompt set oficial (`cr01_cr02_v2_short.yaml`) pide
`person`, `helmet`, `vest` —evidencia **positiva**— y la ausencia la **infiere el plano de control** con el
evaluador `spatial_absence` (`engine/evaluators/spatial_absence.py:154`), que busca el EPP en una región
del bbox de la persona. Es la única estrategia implementada, testeada y corrida.

**Por qué el sistema tiene razón y el capítulo no:** (a) **ADR-001** ya invirtió la decisión; (b) la
evidencia propia la respalda — sobre BENCH v2, `bare_head` (el proxy de la estrategia directa) sale débil
en los **seis** modelos evaluados, y YOLOE detecta **0–1 instancias sobre 69 de GT** (doc 31); (c) la
literatura coincide en que los VLM tipo CLIP manejan mal la negación; y (d) —lo más incómodo— **la
adopción de la estrategia directa contradice la propia consolidación metodológica del informe**
(§17.1.5.4.2 exige comparar directas contra indirectas "sin presuponer la superioridad de ninguna").

**Redline:** reescribir §17.3.9.2 adoptando **E-IND** (evidencia positiva + inferencia espacial de
ausencia) como estrategia del núcleo, con **E-DIR** y **E-HYB** como ramas comparativas de primera clase
del experimento D1. Argumento adicional que conviene incorporar porque rinde en defensa: la evidencia de
E-IND es **auditable** (bbox de la persona + región inspeccionada + ausencia verificable), mientras que el
prompt de negación es una caja negra.

### 3.2 Tabla 44 pone el `cooldown` en el lugar equivocado

**Dice el capítulo:** `cooldown` es un parámetro de la configuración de patrones (Tabla 44), junto a
ventana de persistencia, histéresis y criterio de confirmación. (Nunca lo vuelve a explicar: aparece una
sola vez en todo el capítulo.)

**Decide ADR-011:** el motor **emite una alerta en cada confirmación, sin supresión** — `alerts.jsonl` es
el registro fiel de la dinámica del patrón. El cooldown y toda política de notificación (supresión,
agrupación, rate-limiting) **pertenecen al módulo de distribución** (`notification_policy.cooldown_ms`,
spec 45 §6). El pattern set oficial no tiene cooldown.

**Corolario que hay que escribir, porque toca los resultados:** las alertas repetidas del mismo episodio
son **`re_alerts`** (una métrica de estabilidad) y **no cuentan como falsos positivos** en el evaluador
(`_evaluate_v2`, `evaluation/temporal.py:1002`). Sin esta frase, la tabla de precision del capítulo de
resultados es ininterpretable.

**Redline:** sacar `cooldown` de la Tabla 44 y declararlo parámetro del tramo de distribución, con una
frase que explique la frontera (§17.3.10 ya la sostiene conceptualmente: "primero se confirma el patrón y
luego se distribuye la alerta").

### 3.3 `RunConfig` no existe como artefacto único

**Dice el capítulo:** `RunConfig` es *el* artefacto de configuración que gobierna la corrida (Tabla 44,
Tabla 50), del que cuelgan fuente, modelo, prompts, umbrales, patrones y evidencia.

**Hace el sistema:** hay **tres** configuraciones y **un paraguas** que las une (ADR-004/009/014):
un **manifiesto** (`experiment.manifest.v1`) en `experimental-setup` con un `experiment_id` que se propaga
a los eventos de ambos planos, y que **referencia** la run config del media-plane y la del control-plane.
La razón es estructural, no cosmética: los dos planos son **servicios HTTP independientes**, y cada uno
recibe su config por payload al dispararse.

**Redline:** reescribir la Tabla 44 como *contrato de configuración de experimento* con su descomposición,
y agregar el `experiment_id` como clave de trazabilidad de la cadena completa (que es, además, la promesa
central del §17.3.11.1 — "reconstruir la alerta hasta la configuración" — que hoy el capítulo no puede
cumplir porque no tiene con qué unir los dos planos).

---

## 4. Lo que el capítulo no puede estar reflejando (nuevo desde el 2026-07-06)

Ordenado por cuánto cambia el dibujo de la arquitectura. Nada de esto es "detalle de implementación
diferible": son **elementos de arquitectura** que un capítulo de diseño arquitectónico debe contener.

| # | Elemento | Qué cambia en el capítulo | Fuente |
|---|---|---|---|
| 1 | **Los dos planos son servicios HTTP** (`:8080` y `:8081`), config-driven, más un **orquestador** (runner CLI / webconsole) y un **repositorio adicional** para el módulo de distribución | La vista de componentes (§17.3.5, Figura 4.1) hoy dibuja bloques lógicos; falta la **vista de procesos/despliegue** real. Es exactamente el "cómo está hecho" que pide el tutor. | ADR-008, ADR-005, spec 44 |
| 2 | **Bus ZeroMQ publicador/suscriptor + msgpack** (el publicador usa XPUB, que es lo que permite **verificar** la suscripción en vez de suponerla), envelope `bus.envelope.v1`, `seq`, `run.lifecycle.v1`, **orden de arranque control-first** | §17.3.8.1 dice "el diseño no exige una tecnología específica de mensajería". Ya la exige: está elegida, implementada, medida y con sus trampas documentadas. | ADR-003, spec 40 §3, doc 37 |
| 3 | **Granularidad del patrón (`scene | subject`)** como parámetro de primera clase, con **G0 = núcleo** | §17.3.8.3.2 dice que la memoria "puede organizarse por fuente y condición". Hoy eso es un **campo del `PatternDefinition`** con default `scene`, y trae un **caveat semántico que debe estar en el encuadre del informe** (ver §5). | ADR-002, ADR-012, doc 34 |
| 4 | **Temporalidad de la fuente** (`wallclock \| media \| none`, **derivada** del tipo de fuente, no configurable) y el "cero silencioso" | Un pattern set con persistencia sobre un dataset de **imágenes** produce **0 alertas por construcción** — indistinguible de "no hubo riesgo". Medido: **77 eventos de patrón, 0 alertas** *(⚠️ corregido: el run de los "137 eventos" fue podado; el equivalente vivo con el motor actual da 77)*. La plataforma hoy **lo detecta y lo declara sola** (`not_applicable / non_temporal_source`). El capítulo no distingue fuentes temporales de no temporales. | ADR-013 |
| 5 | **Criterio de relojes** | El capítulo no menciona clock skew. En two-node, t0 (Nodo A) y t1 (Nodo B) viven en hosts distintos: **los relojes monotónicos de dos hosts no se restan**. Regla adoptada: latencias end-to-end medidas en **un solo reloj**, o la métrica cae a `not_interpretable / clock_skew`. | spec 40 §4 |
| 6 | **Métricas derivadas** (`t_capture→alert`, `t_compute-budget`) | Se declaran como instrumento auxiliar que **descompone** la métrica oficial, no la reemplaza. **Vender esto como "aporte instrumental propio" es contraproducente**: invita al tribunal a auditarlo. Va en nota al pie (ver doc 94 §5). | spec 40 §5.2, doc 08 §2.2 |
| 7 | **`clip_gt.v2`** (contrato de GT temporal por episodios) + la convención **`source_id = clip_id`** + los **cinco hitos por alerta** (`first_evidence_unit_id` como clave de join obligatoria) | Contratos nuevos, ausentes del capítulo. La convención de identidad no es negociable: sin ella el matching da **recall 0 en silencio** (doc 54 §5). | spec 43, doc 54 |
| 8 | **Severidades y ventanas alineadas al informe**: PR-01 `high` / 4000 ms, PR-02 `medium` / 7000 ms (resolve 2000/3000) | La desalineación que doc 08 §2.1 marcaba como "la más importante" **ya está corregida en el código** (`cr01_cr02_v2.yaml`). El capítulo debe declarar los valores efectivos. Ojo: el informe pide bandas 3–5 s / 5–10 s; 4000 ms cae dentro de la primera, **7000 ms cae dentro de la segunda** — coherente. | doc 51 |
| 9 | **Layout de artefactos y consolidación** (`runs/<experiment_id>/` con híbrido selectivo: copia lo liviano, referencia los `detections.jsonl` pesados) | Materializa el "repositorio de eventos" del §17.3.12 con un formato concreto sin romper DA-03. | ADR-014 |
| 10 | **La webconsole NO consume el bus** (patrón BFF: consume las APIs) | Frontera arquitectónica explícita que el capítulo no tiene y que evita una pregunta previsible. | spec 40 §3.3 |

---

## 5. Un caveat que el capítulo debe declarar (y hoy no declara)

De todo el relevamiento, este es el punto que más puede doler en una defensa, y no es una errata:

> Bajo `granularity: scene` (el núcleo), la persistencia **ya no mide que el mismo riesgo se sostenga**,
> sino que **la escena exhiba la condición de forma continua** — posiblemente por relevo de sujetos
> distintos, cada uno brevemente descubierto. Una escena con rotación de gente puede confirmar sin que
> ninguna persona haya estado persistentemente en riesgo. *(doc 34 §3; demostrado en fixture: un sujeto
> transitorio adelanta el reloj del episodio.)*

Es el precio, explícito y asumido, de no tener identidad persistente (que es E-03, exclusión declarada).
La decisión es correcta —el aliasing de `detection_id` está **medido**: `det_000001` recorre **1831 px** del
ancho del cuadro (de 1920 px) a lo largo de la corrida, con saltos de hasta **~1749 px entre cuadros
consecutivos** (doc 35 §1.1; *⚠️ corregido: la formulación anterior decía "1831 px entre frames
consecutivos", que es falsa — el argumento se sostiene igual, pero la cifra era verificable y errónea*)—
pero **la afirmación central de "riesgo sostenido" queda acotada**, y eso tiene que estar escrito en el
encuadre, no escondido en un doc interno.
Escrito por nosotros es rigor; encontrado por el tribunal es un agujero.

---

## 6. Evidencia disponible para el pedido T2 ("qué funciona y cómo se mide")

No hay que producir nada nuevo: hay que **escribirlo**.

> 🔴 **La tabla de esta sección se movió.** La auditoría del 2026-07-12 encontró que varias cifras estaban
> **mal atribuidas** (números de una corrida citados como si fueran de otra) y una **sobrevendida** (G2A).
> Para que eso no pueda repetirse, ahora hay **una sola tabla canónica de cifras**, con la corrida y el
> detector de cada una: **`92-anexo-concrecion-tecnica.md` §10**. Ninguna cifra entra al informe si no está
> ahí. Este documento ya no re-tabula números: los cita.

Lo que la evidencia ya sostiene, en una línea cada uno:

- El pipeline **corre sobre vídeo real de obra** sin fallos (733 unidades, 15.914 detecciones).
- El **bus y el repositorio transportan lo mismo**: la corrida live releída offline da artefactos
  byte-idénticos ⇒ toda corrida en vivo es re-evaluable.
- Las **ventanas temporales hacen lo que declaran**: CR-01 confirma a los 4000 ms exactos, CR-02 a los 7000.
- La **granularidad de escena no pierde información** frente a la de sujeto (F1 = 1,0 en el gate).
- El **"cero silencioso"** sobre fuentes no temporales se detecta y se declara solo.
- La **cadena completa computa las cinco métricas** contra referencia temporal anotada, sobre un clip de
  obra real.

**Tres advertencias de honestidad, que son parte del resultado:**

1. **G2A: el número que veníamos citando era de una corrida con detector simulado.** Con el detector real
   (GDINO-tiny), el p95 es de **2604 ms** contra un presupuesto de 50–250 ms, y el sistema lo marca
   `p95_within_budget: false`. **No hay que esconderlo: es un hallazgo**, y es el mismo que el conflicto
   CR-01 ↔ tiempo real del doc 31. La instrumentación funciona *precisamente porque* detecta el
   incumplimiento. La restricción está en el detector, no en la plataforma.
2. **Las cinco métricas son una verificación de instrumento, no un resultado**: salen de **un clip**, con
   **dos alertas** y **GT preliminar**. Reportarlas como "desempeño del sistema" es indefendible;
   reportarlas como "la cadena de medición está completa y es correcta" es exactamente lo que son.
3. **El único falso positivo es un hallazgo sobre el modelo, no un bug** (el detector pierde el chaleco de
   un trabajador que sí lo lleva). Contarlo así —y no maquillarlo— es el tipo de evidencia que el tutor
   está pidiendo.

---

## 7. Lo que hay que declarar como no hecho (o el tribunal lo encuentra)

Un capítulo "verificable" también declara sus límites. **Esta es la lista canónica** — los mismos ocho
ítems, en el mismo orden, están redactados para el informe en el doc 94 §8. (En la v1, este documento, el
redline R-13 y el texto del 94 listaban cosas distintas: inaceptable, y justamente acá.)

1. **Nadie produce identidad de sujeto (`track_id`).** El tracker (spec 42 §3) no está implementado.
   Consecuencia: `granularity: subject` existe en el motor pero **siempre degrada a escena** con causa
   declarada; G1 sólo vive en fixtures; y el overlay pinta **una caja por escena**, no una por persona.
2. **Los evaluadores de la comparación de estrategias (E-DIR / E-HYB) están pendientes**, bloqueados por el
   acta de revisión del catálogo de prompts. **Es el único bloqueo de código que depende de vos.**
3. **La distribución (spec 45, MQTT) no está implementada.** La métrica `t_alert→notification` se reporta
   como `not_applicable / no_distribution` — que es exactamente para lo que sirve la política de
   aplicabilidad del §17.3.13.3. **Es una fortaleza del diseño, si se la cuenta.**
4. **G2A no es computable en la topología de dos nodos** (relojes monotónicos de hosts distintos): se
   declara `not_interpretable`, no se inventa un número. *(Y en un solo nodo, con detector real, **no
   cumple el presupuesto** — ver §6.)*
5. **El GT del único clip del banco es preliminar** (revisión visual asistida), pendiente de la pasada
   humana en CVAT.
6. **EBE-desde-clip tiene una brecha de diseño documentada**: la fuente en vivo estampa reloj de pared
   mientras la anotación está en tiempo de medio; falta el ancla de sincronización. Bloquea la comparación
   DBE↔EBE con fuente idéntica.
7. **El emparejamiento voraz del evaluador puede deflacionar la exhaustividad** en clips con dos episodios
   simultáneos de la misma condición; el fix correcto es emparejamiento bipartito óptimo. Identificado.
8. **El inventario de datasets del informe está desactualizado** (lista SH17, SHEL5K, Pictor-PPE…; la
   selección v2 real es `construction_site_safety`, `chv`, `ppe_siabar`). Hay que declarar qué candidatos
   se retuvieron y por qué. *(Vive fuera del §17.3 — es R-24.)*

**Ojo con los ítems 1 y 3:** el registro de alcance (doc 10) los tiene **dentro** del alcance (G1
demostrativa = ítem 10; distribución MQTT = ítem 5). Declararlos como no hechos en el informe **sin
actualizar doc 10** deja dos documentos diciendo cosas distintas. Es el recorte que hay que formalizar
(ver `95-auditoria-y-plan-de-cierre.md`).

---

## 8. Plan de acción

**El plan vive en otro lado, y a propósito.** Este documento es el *diagnóstico*; el plan es una hoja de
trabajo con casillas de decisión, y mantener dos versiones garantizaba que divergieran (ya había empezado
a pasar). Las cuatro entregas de este relevamiento son:

| Documento | Qué es | Cuándo lo usás |
|---|---|---|
| **91** (este) | El **veredicto y el diagnóstico**: qué está mal, qué falta, qué no hay que tocar. | Para entender el problema. |
| **92** | El **material técnico verificado** contra código, con ruta:línea, y la **tabla canónica de cifras** (§10). | Es la fuente de verdad. Ninguna cifra entra al informe si no está ahí. |
| **93** | La **hoja de redlines** (R-01…R-26), en orden del capítulo, con casilla de decisión por ítem. | Para decidir, ítem por ítem. |
| **94** | El **texto ya redactado**, en registro de informe, listo para copiar al Google Docs. | Para escribir. |
| **95** | La **auditoría adversarial** de estos cuatro documentos + el **plan de cierre a 11 semanas** y las decisiones que dependen de vos. | Para saber qué hacer esta semana. |

---

## 9. Lo que NO hay que tocar

El capítulo tiene fortalezas reales que la implementación **confirmó**, y conviene no diluirlas al reescribir:

1. **Separación detección ≠ patrón ≠ alerta**, con máquina de 5 estados. Está implementada tal cual. Es el corazón conceptual de la tesis.
2. **Política de aplicabilidad de métricas** (calculada / aplicable-no-calculada / no aplicable / no interpretable). Hoy es un **campo literal** en los artefactos (`status` + `cause`). Pocas tesis distinguen "no medí" de "no aplica" de "medí pero no significa nada". Es un diferencial y ya rinde: `t_alert→notification` = `not_applicable / no_distribution` en vez de un cero mentiroso.
3. **Alerta interna como métrica principal, distribución como tramo derivado** (DA-13). Protege la medición de la variabilidad de canales externos.
4. **DBE antes que EBE** (DA-10) y el criterio de cierre por evidencia ("una unidad se completa cuando produce evidencia verificable dentro de una corrida").
5. **Minimización de evidencia visual** (DA-08/09).
6. **Roles CPN/EN/TN como roles lógicos, no máquinas** — sólo hay que aterrizarlos con la tabla rol→contenedor (B6), sin convertirlos en hardware.

---

## 10. Nota de método sobre el hedge

Conviene ser preciso, porque el hedge no era un error en su momento y no hay que sobrecorregir. La frase
"los contratos son denominaciones preliminares" era **correcta el 6 de julio** y sigue siendo correcta
**para las capacidades no implementadas** (los contratos de la distribución, por ejemplo, siguen siendo
preliminares porque el spec 45 no se implementó). Lo que cambió es que para el **núcleo validable** ya no
son preliminares: son clases, son JSON, son endpoints, y hay corridas que los ejercitan.

La reescritura correcta no es borrar el hedge: es **partirlo en dos**. Lo implementado se muestra con su
artefacto real; lo no implementado conserva el estatus preliminar **y lo declara**. Eso es exactamente lo
que el tutor pide cuando dice "como aún falta parte del desarrollo, asumo que será parte del documento
final": no quiere adivinación, quiere que la parte concretada se muestre concretada.
