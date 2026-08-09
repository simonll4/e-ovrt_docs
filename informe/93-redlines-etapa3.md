# Redlines de Etapa 3 — hoja de trabajo para revisión

- **Fecha:** 2026-07-12
- **Qué es esto:** la lista **completa y accionable** de ajustes al capítulo 17.3, uno por uno, en orden
  del documento. **No se toca el `.docx` desde acá.** Cada ítem está redactado para que vos lo analices,
  lo critiques y lo resuelvas directo en el Google Docs.
- **Insumos:** `91-relevamiento-etapa3-vs-implementacion.md` (el análisis) y
  `92-anexo-concrecion-tecnica.md` (el material verificado contra código).
- **Texto nuevo largo:** los ítems marcados con **→ doc 94** tienen la prosa completa ya redactada en
  `94-secciones-nuevas-etapa3.md`. Acá va la instrucción; allá va el texto para copiar.

## Cómo leer cada ítem

```
R-nn · §sección · [TIPO] · PRIORIDAD
DICE HOY  →  cita literal del capítulo, o síntesis marcada como tal (o "no dice nada")
DEBE DECIR →  la instrucción concreta, o el texto propuesto
POR QUÉ   →  la evidencia que lo respalda (código, ADR, corrida medida) — cuando aporta algo
DECISIÓN  →  [ ] acepto   [ ] modifico   [ ] rechazo        ← tu casilla
```

**Tipos:** `CONTRADICE` (el capítulo dice lo contrario de lo que el sistema hace — no es opinable) ·
`CONCRETA` (falta el "cómo está hecho" que pide el tutor) · `PRECISA` (el capítulo no se equivoca, se
queda corto) · `EVIDENCIA` (falta el número medido) · `ERRATA` (forma).

**Los bloques (1–4) son temáticos, no de prioridad.** La prioridad de cada ítem está en su encabezado y en
el tablero; hay ítems críticos en bloques "medios" y viceversa.

**Numeración de tablas y figuras nuevas.** El capítulo cierra en la Tabla 60. Las tablas nuevas están
numeradas **61 a 67** en el doc 94; al transcribir, verificá que no colisionen con las que agregues vos.

> ⚠️ **v2 — 2026-07-12, tras auditoría adversarial.** Se corrigieron tres citas que no eran literales
> (R-01, R-04, R-15), el matiz del `cooldown` (R-02), y se agregaron **R-25** y **R-26**. Todas las cifras
> remiten ahora a la tabla canónica del doc 92 §10. Detalle en `95-auditoria-y-plan-de-cierre.md`.
>
> ✎ **2026-08-06 — sobre esa remisión:** "doc 92 §10" es **`informe/92`** (serie del
> informe, no `operacion/92`) y quedó **derogado como fuente de números el
> 2026-08-05**: al transcribir un redline, las cifras se toman de los **4 índices de
> `e-ovrt_experimental-setup/results/`** (verificados con
> `operacion/datos/96-verificar-indices.py`) vía el brief `informe/97` §5.

---

## Tablero de control

| # | § | Tipo | Prioridad | Título | Decisión |
|---|---|---|---|---|---|
| R-01 | 17.3.9.2 | CONTRADICE | 🔴 crítica | La estrategia del núcleo es E-IND, no la directa | [ ] |
| R-02 | Tabla 44 | CONTRADICE | 🔴 crítica | El `cooldown` no es parámetro de patrón | [ ] |
| R-03 | Tabla 44 / 17.3.6.2 | CONTRADICE | 🔴 crítica | `RunConfig` es un manifiesto + configs por plano | [ ] |
| R-04 | 17.3.8.3.2 | PRECISA | 🔴 crítica | Granularidad `scene\|subject` + caveat semántico de escena | [ ] |
| R-05 | Tabla 45 / 17.3.6.4 | CONTRADICE | 🔴 crítica | El vocabulario del núcleo es positivo (person/helmet/vest) | [ ] |
| R-06 | 17.3.11 | CONCRETA | 🔴 crítica | Partir el hedge en dos + tabla de correspondencia | → doc 94 §1 · [ ] |
| R-07 | 17.3.11.4 | CONCRETA | 🔴 crítica | Regla de evolución del evento (el pedido del tutor) | → doc 94 §2 · [ ] |
| R-08 | 17.3.8.1 / .4 | CONCRETA | 🟠 alta | El bus existe y tiene tecnología: ZeroMQ + msgpack | → doc 94 §3 · [ ] |
| R-09 | 17.3.5 | CONCRETA | 🟠 alta | Figura nueva: vista de procesos (dos servicios HTTP) | → doc 94 §4 · [ ] |
| R-10 | 17.3.13 | CONCRETA | 🟠 alta | Diccionario de métricas con t0/t1 + criterio de relojes | → doc 94 §5 · [ ] |
| R-11 | 17.3.14 (nueva .6) | PRECISA | 🟠 alta | Temporalidad de la fuente y el "cero silencioso" | → doc 94 §6 · [ ] |
| R-12 | cierre (nueva) | EVIDENCIA | 🟠 alta | Sección de verificación: qué funciona y cómo se midió | → doc 94 §7 · [ ] |
| R-13 | cierre (nueva) | EVIDENCIA | 🟠 alta | Registro de lo no implementado | → doc 94 §8 · [ ] |
| R-14 | 17.3.8.2 / Tabla 46 | PRECISA | 🟠 alta | Ventanas efectivas: 4000 / 7000 ms; severidades `high`/`medium` | [ ] |
| R-15 | 17.3.12.1 | CONCRETA | 🟡 media | El repositorio es JSONL append-only, con layout | [ ] |
| R-16 | 17.3.13.3 | PRECISA | 🟡 media | La aplicabilidad es un campo literal (`status` + `cause`) | [ ] |
| R-17 | 17.3.15 | CONCRETA | 🟡 media | Tabla rol → contenedor (Nodo A ≈ EN-1, Nodo B ≈ CPN) | [ ] |
| R-18 | Tabla 43 (DA-01…13) | PRECISA | 🟡 media | Actualizar el estado de las decisiones condicionadas | [ ] |
| R-19 | Tabla 50 | ERRATA | 🟡 media | `PatternDefinition` es huérfano: falta su fila | [ ] |
| R-20 | Tabla 57 | PRECISA | 🟡 media | Riesgos: los que se materializaron y cómo se mitigaron | [ ] |
| R-21 | Tablas 58/59 | EVIDENCIA | 🟠 alta | Backlog: estado real de los 16 ítems | [ ] |
| R-22 | 17.3.14.5 | PRECISA | 🟡 media | EBE: la cámara IP real ya se usó; la brecha que queda | [ ] |
| R-23 | varias | ERRATA | 🟢 baja | Figuras sin numerar y vacías, títulos pegados, duplicados | [ ] |
| R-24 | fuera de 17.3 | PRECISA | 🟡 media | Inventario de datasets desactualizado | [ ] |
| R-25 | 17.3.11 / 17.3.13 | CONCRETA | 🟠 alta | Contrato de GT temporal + convención de identidad + los 5 hitos | [ ] |
| R-26 | 17.3.17 / 17.3.18 | CONCRETA | 🟠 alta | **Extensibilidad medida: cuánto cuesta una condición nueva** | → doc 94 §9 · [ ] |

---

# 🔴 Bloque 1 — Contradicciones (no son opinables)

## R-01 · §17.3.9.2 · CONTRADICE · crítica
### La estrategia adoptada para el núcleo es E-IND, no la detección directa

**DICE HOY** — cita **literal** (líneas 623 y 627), corregida tras auditoría:
> *"Para el núcleo validable, la estrategia adoptada es la detección directa de condiciones de EPP mediante
> prompts configurados para CR-01 y CR-02."*
>
> *"[Las consultas auxiliares positivas] pueden habilitarse con finalidad diagnóstica o comparativa. Su uso
> permite analizar falsos positivos… pero no reemplaza la estrategia directa ni confirma por sí mismo una
> ausencia."*

**DEBE DECIR** — invertir la adopción. Texto propuesto para reemplazar el párrafo central:

> La estrategia adoptada para el núcleo validable es la **detección indirecta por evidencia positiva con
> inferencia espacial de ausencia (E-IND)**. El plano de medios consulta al detector open-vocabulary por
> **entidades presentes y observables** —persona, casco, chaleco— y el plano de control infiere la
> ausencia del elemento de protección evaluando su presencia dentro de una región derivada del bounding
> box del sujeto. La ausencia, por lo tanto, no se consulta al modelo: se **deriva** de evidencia
> perceptiva positiva.
>
> Esta adopción responde a tres razones. Primero, una razón metodológica: la consolidación metodológica
> de este trabajo (§17.1.5.4.2) exige comparar estrategias directas e indirectas **sin presuponer la
> superioridad de ninguna**, de modo que adoptar la estrategia directa como núcleo por definición sería
> incompatible con el propio protocolo. Segundo, una razón empírica: la evaluación comparativa de modelos
> sobre el conjunto BENCH muestra que el estado observable que sostiene la estrategia directa
> (`bare_head`) es débil en todos los modelos evaluados, al punto de que una de las familias evaluadas
> detecta entre 0 y 1 instancias sobre 69 presentes en la referencia. Tercero, una razón de auditabilidad:
> la evidencia producida por E-IND es **inspeccionable** —el bounding box del sujeto, la región evaluada y
> la ausencia verificable dentro de ella—, mientras que un prompt de negación produce una decisión opaca,
> no reconstruible.
>
> La **detección directa (E-DIR)** y las **estrategias híbridas (E-HYB)** se conservan como **ramas
> comparativas** del protocolo experimental, no como diagnóstico subordinado. La comparación cuantitativa
> entre estrategias queda **especificada** como protocolo, y su ejecución se declara conforme al alcance
> final del trabajo.

> 🔴 **DECISIÓN TUYA, Y ES URGENTE.** El último párrafo tiene dos versiones posibles y **no podés
> postergarla**:
>
> - **(a) Comprometida:** *"la comparación entre estrategias es, en sí misma, uno de los resultados
>   previstos del trabajo"*. Suena mucho mejor — **pero promete un resultado que hoy no existe**: los
>   evaluadores E-DIR/E-HYB no están implementados y están **bloqueados esperando que firmes el acta del
>   catálogo de prompts (`edir_v1`)**. Si escribís esto y D1 no corre, el tribunal va a pedir esa tabla.
> - **(b) Prudente** (la que dejé arriba): la comparación queda **especificada**, y su ejecución depende
>   del alcance final.
>
> **Regla:** si firmás el acta esta semana y D1 entra en la campaña, poné (a). Si no, poné (b) y dormí
> tranquilo. Lo que **no** se puede es escribir (a) y no correrlo.

**POR QUÉ** — ADR-001; §17.1.5.4.2 del propio informe (que exige comparar directas contra indirectas "sin
presuponer la superioridad de ninguna"); doc 31 (benchmark de **6** modelos: YOLOE recall CR-01
0.000–0.014, con 0–1 detecciones de `bare_head` sobre 69 de referencia); el evaluador implementado es
`spatial_absence` y es el único que existe.

**OJO — efecto dominó.** Este redline arrastra a **R-05** (el vocabulario de la Tabla 45) y toca el
encuadre del capítulo de resultados. Es el ajuste más importante de todo el documento.

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

## R-02 · Tabla 44 · CONTRADICE · crítica
### El `cooldown` no es un parámetro de la evaluación de patrones

**DICE HOY** (Tabla 44, fila "Patrones activos", línea 287):
> *"…ventana de persistencia, histéresis, **cooldown** y criterio de confirmación."*
(Es la única mención en todo el capítulo: nunca se explica.)

**DEBE DECIR** — dos cambios:

1. **Sacar `cooldown` de la Tabla 44.** La fila queda: *"ventana de persistencia, histéresis y criterio de
   confirmación."*
2. **Agregar en §17.3.10.3** (distribución) el párrafo:

> El motor de patrones **registra una alerta interna en cada confirmación de episodio, sin supresión**: el
> registro de alertas es el reflejo fiel de la dinámica del patrón y no debe ser filtrado por
> consideraciones de comunicación. Las políticas de **supresión de re-notificación** —cooldown por
> condición y fuente, agrupación, limitación de tasa— pertenecen al **tramo de distribución**, aguas abajo
> de la alerta interna, y se declaran como parámetros de la política de notificación. Esta separación
> preserva la métrica principal: una alerta suprimida por política de notificación **existió**, fue
> registrada y es medible, aunque no se haya comunicado.
>
> En consecuencia, las alertas sucesivas correspondientes a un mismo episodio confirmado se contabilizan
> como **re-alertas**, un indicador de estabilidad temporal del patrón, y **no se computan como falsos
> positivos** en la evaluación.

**POR QUÉ** — ADR-011. El conjunto de patrones adoptado **no configura cooldown**; el evaluador excluye
explícitamente las re-alertas del denominador de la precisión.

> ⚠️ **Matiz que encontró la auditoría, y que hay que respetar al redactar.** El cooldown **sí existe en el
> motor** (`PatternTimingConfig.realert_cooldown_ms` + `PatternEngine._cooldown_ok()`): lo que ocurre es
> que **el conjunto de patrones adoptado lo deja sin configurar**, y ADR-011 lo declara literalmente
> "capacidad no usada por la plataforma". Redactá *"el motor no suprime, porque el conjunto de patrones
> adoptado no configura supresión"* — **nunca** *"el motor no puede suprimir"*. Si alguien abre el código y
> encuentra un cooldown que el informe negaba, el daño supera al beneficio de la frase simple.

**Impacto en resultados:** sin este párrafo, la tabla de precisión del capítulo de resultados es
ininterpretable (el lector no sabe qué entra en el denominador).

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

## R-03 · Tabla 44 y §17.3.6.2 · CONTRADICE · crítica
### `RunConfig` no es un artefacto único: es un manifiesto que referencia configuraciones por plano

**DICE HOY** — la Tabla 44 y toda la §17.3.6 tratan la configuración de corrida como **un** artefacto que
gobierna la corrida completa, del que cuelgan fuente, modelo, prompts, umbrales, patrones y evidencia.

**DEBE DECIR** — reencuadrar §17.3.6.2 con este párrafo antes de la Tabla 44:

> La configuración de corrida se materializa como un **manifiesto de experimento**, que no contiene la
> configuración completa sino que **referencia** la configuración efectiva de cada plano y las **congela**
> bajo un identificador común. La razón es estructural: los planos se ejecutan como servicios
> independientes, cada uno con su propio ciclo de vida y su propia configuración efectiva, de modo que una
> configuración monolítica no tendría un único destinatario.
>
> El manifiesto declara: un **identificador de experimento** (`experiment_id`) que se propaga a todos los
> eventos y resúmenes de **ambos** planos; las referencias a la configuración de cada plano; el orden de
> disparo; y el conjunto de artefactos congelados de la corrida (conjunto de prompts, conjunto de patrones,
> referencia del modelo). Ese identificador es la **clave de trazabilidad** que permite reconstruir una
> alerta hasta la configuración, el conjunto de prompts, el modelo y la versión de código que la
> produjeron —la promesa formulada en §17.3.11.1—, y sin él la cadena causal se cortaría en la frontera
> entre planos.

Y **agregar una fila a la Tabla 44**: *"Identificador de experimento — clave común que vincula las corridas
de ambos planos y todos sus artefactos."*

**POR QUÉ** — ADR-004, ADR-009, ADR-014. Artefacto real: `manifest.effective.yaml` (`experiment.manifest.v1`),
con `experiment_id` presente en `pattern_events.jsonl`, `alerts.jsonl` y los `summary.json` de ambos planos.

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

## R-04 · §17.3.8.3.2 · PRECISA (pero es crítica) · crítica
### La granularidad es un parámetro del patrón — y la de escena tiene un caveat que hay que declarar

**DICE HOY** — cita **literal** (línea 547), corregida tras auditoría:
> *"Para los patrones del núcleo validable, esta memoria puede organizarse **por fuente y condición**, sin
> exigir identidad persistente de persona."*

Es correcto, pero se queda a mitad de camino: hoy eso es un **parámetro explícito** del patrón, y su
elección tiene una **consecuencia semántica** sobre la afirmación central del trabajo.

**DEBE DECIR** — reemplazar el párrafo por:

> La granularidad de la memoria temporal es un **parámetro explícito de la definición de patrón**, con dos
> valores posibles. Bajo granularidad de **escena** (el núcleo validable), el estado se indexa por
> `(patrón, fuente)` y la persistencia se evalúa sobre la condición observada en la escena, sin exigir
> identidad persistente de persona. Bajo granularidad de **sujeto**, el estado se indexa por
> `(patrón, fuente, identidad)` y requiere que el plano de medios emita una identidad estable entre frames.
>
> El núcleo adopta la granularidad de escena por una razón medida, no por conveniencia: el identificador de
> detección que produce el detector es un **índice por frame**, no una identidad temporal, y utilizarlo como
> tal produce aliasing verificable —sobre una corrida de vídeo real, la detección identificada como
> `det_000001` recorre 1831 píxeles del ancho del cuadro, de 1920 píxeles, a lo largo de la corrida, con
> desplazamientos de hasta 1749 píxeles entre cuadros consecutivos—. Se declara, en consecuencia, que **el
> identificador de detección no constituye identidad entre frames** y que la única identidad válida es la
> emitida por un componente de seguimiento.
>
> Esta elección tiene una **consecuencia semántica que debe explicitarse**. Bajo granularidad de escena, la
> persistencia no mide que *el mismo sujeto* sostenga la condición de riesgo, sino que *la escena exhiba la
> condición de forma continua*. Una escena con rotación de personas —cada una brevemente descubierta— puede
> confirmar un episodio sin que ningún individuo haya estado persistentemente en riesgo. La afirmación que
> el sistema sostiene bajo el núcleo validable es, por lo tanto, **"la condición de riesgo persiste en la
> escena"**, y no "un sujeto persiste en riesgo". La segunda afirmación requiere granularidad de sujeto, que
> el diseño prevé y el prototipo deja especificada como extensión.

**POR QUÉ** — ADR-002, ADR-012; doc 34 §3 (el caveat, demostrado en fixture: un sujeto transitorio adelanta
el reloj del episodio); doc 35 §1.1 (el aliasing, medido — ojo con la formulación: los 1831 px son el
**rango total** de la corrida, no un salto entre dos cuadros; el salto máximo consecutivo es ~1749 px).

**Este es el ítem que más protege la defensa.** Escrito por nosotros es rigor metodológico; encontrado por
el tribunal es un agujero en la afirmación central.

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

## R-05 · Tabla 45 y §17.3.6.4 · CONTRADICE · crítica
### El vocabulario activo del núcleo es positivo

**DICE HOY** — la Tabla 45 presenta como formulaciones principales de CR-01/CR-02 los prompts de ausencia
(`"person without hard hat"`, `"person without reflective vest"`) y relega a auxiliares los positivos
(`"person"`, `"hard hat"`, `"safety helmet"`, `"reflective vest"`).

**DEBE DECIR** — invertir la jerarquía de la tabla, **coherentemente con R-01**:

- **Vocabulario activo del núcleo (E-IND):** `person`, `helmet`, `vest`. Es el conjunto efectivamente
  ejecutado (`cr01_cr02_v2_short`), con las clases tipificadas por rol: `person` como **entidad sujeto**,
  `helmet` y `vest` como **elementos de protección**.
- **Vocabulario de la rama comparativa (E-DIR):** las formulaciones de ausencia y de estado observable, que
  pasan a ser el objeto del experimento de sensibilidad al prompt, no el núcleo.
- Conservar el resto de la tabla (CR-03…CR-06) tal como está: son condiciones no implementadas y su
  vocabulario sigue siendo candidato.

**Nota importante que conviene agregar bajo la tabla:** el conjunto de formulaciones se **versiona** y la
corrida registra el identificador del conjunto activo (`prompt_set_id`), de modo que toda detección es
atribuible a la formulación exacta que la produjo.

**POR QUÉ** — ADR-001; el prompt set real es `cr01_cr02_v2_short.yaml` (`person` / `helmet` / `vest`);
`prompt_set_id` viaja en cada `DetectionEvent`.

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

# 🟠 Bloque 2 — Concreción técnica (la observación del tutor)

## R-06 · §17.3.11 · CONCRETA · crítica → **texto completo en doc 94 §1**
### Partir el hedge en dos: lo implementado se muestra; lo pendiente sigue preliminar

**DICE HOY** (línea 699) — el párrafo que el tutor citó textualmente:
> *"…los nombres utilizados en esta sección, como RunConfig, FrameMetadata, PerceptionEvent o AlertEvent,
> deben interpretarse como denominaciones contractuales preliminares. **No imponen una tecnología, un
> formato de serialización ni una estructura de código específica.**"*

**DEBE DECIR** — este párrafo **era verdadero el 6 de julio y hoy es falso para el núcleo**. No hay que
borrarlo: hay que **partirlo**.

- Para el **núcleo validable**: los contratos ya no son preliminares. Son modelos de datos versionados, con
  serialización explícita, esquema verificable y corridas que los ejercitan. Se muestran con su artefacto
  real (clase, DTO serializado, endpoint).
- Para lo **no implementado** (los contratos del tramo de distribución): el estatus preliminar **se
  conserva y se declara como tal**.

Concretamente, la sección debe incorporar: **(a)** la tabla de correspondencia contrato preliminar ↔
artefacto real; **(b)** el contrato central (`PerceptionEvent` → `DetectionEvent` / `media.detection.v1`)
mostrado como **clase** y como **DTO serializado**; **(c)** los dos contratos del plano de control
(`PatternStateChanged`, `AlertEvent`); **(d)** las **APIs** de los dos servicios.

**→ El texto completo, con la tabla, los DTO y los endpoints, está en `94-secciones-nuevas-etapa3.md` §1.**

**POR QUÉ** — es el pedido literal del tutor ("no espero un detalle extremo, pero sí algo como un DTO, una
API, o una clase"). Todo el material existe y está verificado con ruta:línea en el doc 92.

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

## R-07 · §17.3.11.4 · CONCRETA · crítica → **texto completo en doc 94 §2**
### La regla de evolución del evento de inferencia (el pedido más profundo del tutor)

**DICE HOY** (líneas 785–797) — la sección existe y es correcta en espíritu ("cambios aditivos aceptables;
cambiar o eliminar significado = ruptura contractual → nueva versión"), pero es **abstracta**: no muestra el
evento, no nombra un solo campo, no dice qué se emite hoy y qué no.

**DEBE DECIR** — el tutor pidió esto con nombre y apellido:
> *"Es muy importante ser muy claro en la definición de eventos tipo inferencias para que den soporte a
> datos que a lo mejor hoy no están, pero mañana sí: tracking, velocidad, dirección, pose, segmentación."*

La sección debe: **(a)** enunciar las cuatro reglas de evolución (aditivo, sin bump de versión, la versión
viaja en el payload, ruptura sólo por cambio de significado); **(b)** **mostrar el evento con su superficie
de crecimiento** —los campos futuros como opcionales, explícitos en el esquema—; **(c)** declarar
**honestamente** el estado de cada extensión.

**El hallazgo que hay que contar (y que juega a favor):** `track_id` existe **en ambos contratos** —el
consumidor lo usa como identidad en el motor de patrones desde antes; el productor lo incorporó el
2026-07-13 (commit `0133d38` del media-plane, como campo aditivo con tests de serialización)— pero **nadie
lo puebla todavía**: el tracker no está implementado, el campo vale `None` y no aparece en los artefactos.
La distinción para el informe es exactamente esa: **el contrato está completo; la capacidad que lo
alimenta, no**. Decirlo así demuestra lo que el tutor quiere ver: que el contrato fue **diseñado para
crecer** (y se puede mostrar el esquema, no prometerlo), y que sabemos dónde está parado hoy.

**→ Texto completo en `94-secciones-nuevas-etapa3.md` §2.**

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

## R-08 · §17.3.8.1 y §17.3.8.4 · CONCRETA · alta → **texto completo en doc 94 §3**
### El bus tiene tecnología, y sus trampas están medidas

**DICE HOY** (línea 477):
> *"El diseño **no exige una tecnología específica de mensajería** en esta instancia."*

**DEBE DECIR** — ya la exige. Está elegida (ZeroMQ PUB/SUB + msgpack), implementada, medida, y tiene
**reglas de operación que se descubrieron corriéndola** y que un capítulo de arquitectura debería contener:

- El envelope versionado y su relación con el JSONL (el payload publicado es **byte-idéntico** a la línea
  persistida ⇒ toda corrida en vivo es re-evaluable offline).
- **El orden de arranque es control-primero**, y no es negociable: PUB/SUB **pierde todo lo publicado antes
  de la suscripción**.
- **Persistir primero, publicar después**: el repositorio es la verdad, el bus sólo transporta (DA-03).
- **La pérdida se detecta por hueco de número de secuencia** — un publicador ZeroMQ descarta en silencio al
  llenarse su cola, sin señalar error. Un hueco degrada la corrida; nunca se silencia.
- El broker (Kafka/RabbitMQ) queda **fuera de alcance con la costura documentada**.

**→ Texto completo en `94-secciones-nuevas-etapa3.md` §3.**

**POR QUÉ** — ADR-003, spec 40 §3, doc 37 (40/40 unidades, 0 perdidas, artefactos byte-idénticos).

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

## R-09 · §17.3.5 · CONCRETA · alta → **especificación de figura en doc 94 §4**
### Falta la vista de procesos: el sistema son dos servicios HTTP

**DICE HOY** — la Figura 4.1 es una **vista lógica** de bloques (fuentes → adaptador → plano de medios → bus
→ plano de control → distribución), con la nota de que "no debe interpretarse como una distribución física".

**DEBE DECIR** — la vista lógica **se conserva** (es correcta y es la que ordena el capítulo). Lo que falta
es una **segunda figura**: la vista de **procesos/despliegue real**, que es literalmente el "cómo está
hecho" que reclama el tutor. Debe mostrar: los dos servicios HTTP (`:8080` y `:8081`), el bus ZeroMQ entre
ellos, el orquestador que dispara la corrida paraguas por HTTP, la webconsole como cliente de ambas APIs
(**no consume el bus**), el repositorio JSONL por corrida, y el módulo de distribución como consumidor
externo del bus de alertas.

**→ Especificación de la figura (cajas, flechas, etiquetas) en `94-secciones-nuevas-etapa3.md` §4.**

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

## R-10 · §17.3.13 · CONCRETA · alta → **texto completo en doc 94 §5**
### Diccionario de métricas con definiciones operacionales, y el criterio de relojes

**DICE HOY** — §17.3.13.1 nombra TTFD, SDR y la latencia de alerta, y los vincula a tramos ("TTFD se vincula
con la primera evidencia perceptiva"). No define t0, t1, unidad ni condición de aplicación de ninguna.
Y **no menciona el problema de los relojes**.

**DEBE DECIR** — una tabla de diccionario con `t0 / t1 / unidad / condición de aplicabilidad` por métrica, y
tres cosas que hoy faltan:

1. **El criterio de relojes** (el hueco más caro): las latencias intra-nodo usan reloj monotónico local; las
   end-to-end se miden **en un solo reloj**. **Los relojes monotónicos de dos hosts no se restan** — en la
   topología de dos nodos, la métrica correspondiente se declara *no interpretable* con su causa, en lugar
   de publicar un número sin significado.
2. **Las dos métricas derivadas propias** (`t_capture→alert` y `t_compute-budget`), con su **estatus
   epistemológico declarado**: son un aporte instrumental de este trabajo, **no** reemplazan la métrica
   oficial — la **descomponen**. Identidad declarada: `t_alert-system = TTFD + t_capture→alert`.
3. **El criterio de detección positiva no se reimplementa**: el evaluador reutiliza el evaluador real del
   motor, de modo que no puede haber dos definiciones de "positivo" divergiendo en silencio.

**→ Texto completo, con la tabla del diccionario, en `94-secciones-nuevas-etapa3.md` §5.**

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

## R-11 · §17.3.14 (subsección nueva) · PRECISA · alta → **texto completo en doc 94 §6**
### Temporalidad de la fuente: el "cero silencioso"

**DICE HOY** — nada. El capítulo distingue DBE de EBE por el **origen** de la fuente (dataset vs entorno),
pero no por su **naturaleza temporal**.

**DEBE DECIR** — es una dimensión de aplicabilidad que el capítulo no contempla y que produce un **modo de
falla silencioso**:

> Un conjunto de patrones con persistencia temporal, evaluado sobre una fuente **no temporal** (un dataset
> de imágenes independientes), produce **cero alertas por construcción** — un resultado indistinguible de
> "no hubo riesgo en los datos". Se midió: **77 transiciones de patrón y 0 alertas**.

La plataforma hoy **detecta la temporalidad de la fuente y lo declara sola** (`no aplicable / fuente no
temporal`), en lugar de reportar un cero engañoso. Es la política de aplicabilidad del §17.3.13.3 haciendo
exactamente el trabajo para el que fue diseñada, y conviene mostrarlo como tal.

**→ Texto completo en `94-secciones-nuevas-etapa3.md` §6.**

**POR QUÉ** — ADR-013. ⚠️ **Ojo con la cifra:** el run original de los "137 eventos / 0 alertas" (doc 33 §4)
**fue podado y ya no existe**. El equivalente vivo, con el motor actual, da **77 transiciones / 0 alertas** —
y ese artefacto **sí** está en disco, con `not_applicable / non_temporal_source` declarado. Usá 77.

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

# 🟠 Bloque 3 — Evidencia ("qué funciona y cómo se mide")

## R-12 · Sección nueva al cierre · EVIDENCIA · alta → **texto completo en doc 94 §7**
### Verificación: el sistema es ejecutable, y estos son los números

**DICE HOY** — nada. El capítulo **no contiene una sola cifra medida**.

**DEBE DECIR** — una sección de verificación con la evidencia ya producida: 733 unidades sin fallos sobre
vídeo real; el bus y el repositorio transportando lo mismo (artefactos byte-idénticos); CR-01 confirmando en
t=4000 ms exacto; F1=1.0 en el gate de granularidad; y **las cinco métricas contra referencia temporal
anotada sobre un clip de obra real** (P=0,50 · R=1,00 · F1=0,67 · t_alert-system=4000 ms · TTFD=0 ms ·
SDR=0,999).

> 🔴 **TRES CORRECCIONES DE LA AUDITORÍA — sin esto, la tabla es indefendible.**
>
> 1. **G2A: el número que veníamos citando era de una corrida MOCK.** "p95 = 31,8 ms, dentro de presupuesto"
>    sale de una corrida con detector simulado. **Con GDINO real, el p95 es 2604 ms** y el propio sistema
>    marca `p95_within_budget: false` — diez veces por encima del presupuesto. **No lo escondas: es un
>    hallazgo.** La instrumentación funciona *porque* detecta el incumplimiento, y coincide con el conflicto
>    CR-01 ↔ tiempo real del doc 31. Reformulado así en el doc 94 §7.
> 2. **Las cinco métricas son una VERIFICACIÓN DE INSTRUMENTO, no un resultado.** Salen de **un clip**, con
>    **dos alertas observadas** y **GT preliminar**. Una "precisión de 0,50" derivada de dos eventos invita
>    a la pregunta *"¿su precisión es una moneda al aire?"*. Hay que decir **n = 1 clip, 2 alertas** y
>    llamarlo verificación, no medición de desempeño.
> 3. **No fusiones corridas distintas.** La byte-identidad se verificó sobre una corrida de **40 unidades**;
>    las **300 unidades** son otra corrida. Y **ambas usaron detector mock**. Van en filas separadas.

**Y contarlo con honestidad**: el único falso positivo de ese benchmark es **un hallazgo sobre el modelo, no
un bug** (el detector pierde el chaleco de un trabajador), y el GT de ese clip es **preliminar** hasta la
pasada humana en CVAT. Decir ambas cosas **fortalece** el resultado; ocultarlas lo destruye si alguien
pregunta.

**→ Texto completo, con la tabla de evidencia ya corregida, en `94-secciones-nuevas-etapa3.md` §7.**
**→ Todas las cifras, con su corrida y su detector, en `92-anexo-concrecion-tecnica.md` §10** (tabla canónica).

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

## R-13 · Sección nueva al cierre · EVIDENCIA · alta → **texto completo en doc 94 §8**
### Registro de lo no implementado

> ✎ **2026-08-05 — DESBLOQUEADO, y la lista de abajo quedó vieja.** Este ítem esperaba
> ADR-015 (doc 95 §5.3), que ya está escrito:
> [`decisiones/adr-015-cierre-de-alcance.md`](../decisiones/adr-015-cierre-de-alcance.md)
> (✅ aceptada el 2026-08-05). **De los 8 ítems de abajo, 5 están resueltos**
> — auditados uno por uno contra artefacto en el **ADR-015 §3**, que es de donde hay que
> redactar: `track_id` (G1 es capacidad operativa medida), evaluadores de D1 (corrió: veto
> de precisión), GT preliminar (el banco está `gt_ready`), matching greedy (es bipartito
> desde la enmienda A4) e inventario de datasets (al día, `operacion/99`).
> **Sobreviven 3**: distribución no implementada, brecha del ancla EBE (precisada) y G2A
> no computable entre dos hosts (ahora agravada por F-101.8). **Y el tramo experimental
> agregó 9 límites nuevos** (L1–L8 + el registro de licencias de video). Publicar la lista
> de abajo tal cual sería declarar como límites cosas ya resueltas.

**DECÍA (julio 2026, superado)** — un capítulo "verificable" también declara sus límites, **antes** de que los encuentre el
tribunal. Ocho ítems: sin productor de `track_id`; distribución no implementada; evaluadores de D1
pendientes; GT preliminar; brecha de sincronización en EBE-desde-clip; G2A no computable en dos nodos;
matching greedy que puede deflacionar recall; inventario de datasets desactualizado.

Cada uno **anclado a su regla de exclusión** (doc 10, E-01…E-13), para que se lea como alcance declarado y
no como omisión.

**→ Texto completo en `94-secciones-nuevas-etapa3.md` §8.**

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

## R-14 · §17.3.8.2 y Tabla 46 · PRECISA · alta
### Los valores efectivos: 4000 / 7000 ms, `high` / `medium`

**DICE HOY** — el capítulo declara la severidad "estática por corrida" pero **nunca enumera los niveles**, y
no da **ningún** valor de ventana temporal (no hay una sola cifra en todo el capítulo).

**DEBE DECIR** — agregar los valores efectivos del núcleo, y su justificación contra las bandas del informe:

| Patrón | Condición | Severidad | Persistencia (confirmación) | Histéresis (resolución) | Banda del informe (Tabla 24) |
|---|---|---|---|---|---|
| PR-01 | Persona sin casco | `high` | **4000 ms** | 2000 ms | alto · 3–5 s ✓ |
| PR-02 | Persona sin chaleco | `medium` | **7000 ms** | 3000 ms | medio · 5–10 s ✓ |

Y una frase que conviene incluir porque responde a una pregunta previsible: la persistencia se expresa **en
milisegundos, no en frames**, tal como exige §17.1.5.3.3 — de otro modo la ventana temporal dependería de la
tasa de muestreo y dejaría de ser comparable entre corridas.

**Y los umbrales efectivos** (que tampoco están en el capítulo, y el tutor los va a buscar):

| Parámetro | Valor | Dónde |
|---|---|---|
| Umbral de caja / de texto / de confianza / IoU | 0,35 / 0,25 / 0,25 / 0,50 | Inferencia |
| Confianza mínima de postproceso · área mínima | 0,25 · 100 px² | Postproceso |
| Confianza mínima del sujeto · del elemento ausente · área mínima del sujeto | 0,35 · 0,25 · 400 px² | Evidencia de patrón |
| Región de búsqueda CR-01 (casco) | franja superior del sujeto: 0–45 % de su altura, margen lateral 12 % | Evaluador espacial |
| Región de búsqueda CR-02 (chaleco) | franja media: 25–85 % de la altura, margen lateral 8 % | Evaluador espacial |

**POR QUÉ** — `cr01_cr02_v2.yaml`. Verificado: CR-01 confirma en t=4000 ms exacto sobre video real (doc 35);
con ~1 s de video no hay alertas y con ~10 s aparecen (doc 51) — la ventana **hace** lo que dice.

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

# 🟡 Bloque 4 — Precisiones y forma

## R-15 · §17.3.12.1 · CONCRETA · media
### El repositorio de eventos es JSONL append-only, y tiene un layout

**DICE HOY** — cita **literal y completa** (línea 809). La versión anterior de este redline recortaba la
frase de un modo que **cambiaba su sentido**: omitía la subordinada que la salva. El original dice:
> *"…alcanza con una persistencia simple y verificable […] La decisión arquitectónica relevante **no es la
> tecnología concreta de almacenamiento, sino la imposibilidad de sobrescribir silenciosamente los hechos
> que explican una corrida**."*

O sea: el capítulo **no está indeciso**, está priorizando bien. El redline no es "el capítulo se lava las
manos", es "el capítulo tiene razón y además ya podemos decir qué elegimos".

**DEBE DECIR** — el principio es correcto y se conserva; lo que falta es decir **qué se eligió**: un archivo
**JSONL append-only por corrida y por tipo de evento**, con la configuración efectiva, el manifiesto (que
incluye el **SHA de git del código que produjo la corrida**) y la procedencia de los datos junto a los
eventos. Conviene mostrar el layout de artefactos (está en el doc 92 §8) y cerrar con la frase que hace
verdadera la promesa de §17.3.11.1:

> Toda alerta se reconstruye hasta la configuración efectiva, el conjunto de prompts, el modelo y la versión
> de código que la produjeron.

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

## R-16 · §17.3.13.3 · PRECISA · media
### La política de aplicabilidad ya no es una política: es un campo

**DICE HOY** — describe los cuatro estados de una métrica (calculada / aplicable no calculada / no aplicable /
no interpretable) como criterio de interpretación.

**DEBE DECIR** — agregar que se **materializó como campo literal** del reporte (`status` + `cause`), con
ejemplos reales:

- `t_alert→notification` → **no aplicable** / *no hay canal de distribución*.
- `t_capture→alert` → **no interpretable** / *reloj de medio, no de pared*.
- G2A en dos nodos → **no interpretable** / *relojes monotónicos de hosts distintos*.
- TTFD sin detección positiva en el episodio → **nulo** con causa, **nunca 0.0 por defecto**.

Esta es una de las fortalezas diferenciales del trabajo y hoy está subvendida: el capítulo la enuncia como
criterio y no muestra que **el sistema se niega a publicar un número que no significa nada**. Vale una frase
explícita: *"la plataforma no publica un cero cuando lo correcto es declarar una causa"*.

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

## R-17 · §17.3.15 · CONCRETA · media
### Tabla rol → contenedor

**DICE HOY** — CPN/EN/TN son roles lógicos, "no implican necesariamente máquinas físicas separadas". (Correcto,
**no tocar el principio**.)

**DEBE DECIR** — aterrizarlo con la correspondencia real, que existe y está verificada en la topología de dos
nodos:

| Rol | Materialización en el prototipo | Responsabilidades ejercidas |
|---|---|---|
| **EN** (modo EN-1) | Nodo A (contenedor de borde, sin GPU) | Ingesta, control de ritmo, normalización visual. **Sin semántica**: no ejecuta inferencia. |
| **CPN** | Nodo B (contenedor con GPU) | Inferencia OVD, postproceso, publicación, evaluación de patrones, alertas, persistencia, observabilidad. |
| **TN** | No materializado | Rol previsto, no ejercido (exclusión declarada E-04, por presupuesto de tiempo). |

Agregar también el hallazgo de relojes que surge de esta topología (ver R-10).

**Y de paso, la errata:** en §17.3.15 la oración *"La definición de estos roles no implica…"* aparece
**duplicada** con variantes.

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

## R-18 · Tabla 43 (DA-01…DA-13) · PRECISA · media
### Actualizar el estado de las decisiones

Varias decisiones "condicionadas" ya se resolvieron y algunas "adoptadas" cambiaron de contenido. Revisión
sugerida (a validar una por una):

| DA | Dice | Estado real | Acción |
|---|---|---|---|
| DA-03 | canal ≠ repositorio; tecnología diferida | **Tecnología fijada**: ZeroMQ + msgpack; broker excluido con costura documentada | Actualizar |
| DA-06 | MOT opcional | **Acotada**: granularidad de sujeto especificada, tracker **no implementado** | Precisar |
| DA-07 | fine-tuning condicionado | **No ejercida** — y la razón importa: por **presupuesto de tiempo**, no por falta de datos ni de recursos (el split de entrenamiento ya está generado) | Precisar la razón |
| DA-11 | preselección en borde condicionada | **No ejercida** (E-07) | Confirmar |
| DA-13 | alerta interna antes que notificación | **Adoptada y reforzada** por ADR-011 (el motor no suprime; la política vive aguas abajo) | Reforzar |

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

## R-19 · Tabla 50 · ERRATA · media
### `PatternDefinition` es huérfano

`PatternDefinition` aparece en la **Tabla 49** (como contrato de entrada al plano de control) pero **no tiene
fila en la Tabla 50**, que es la única tabla que da contenido a los contratos. Falta agregarla:

> **PatternDefinition** — *Define la condición evaluable y su criterio temporal.* Información mínima:
> identificador de patrón, condición asociada, clase del sujeto, clase de protección requerida, **granularidad**,
> región de evaluación, umbrales de evidencia, ventana de confirmación, histéresis de resolución y severidad
> configurada.

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

## R-20 · Tabla 57 (riesgos) · PRECISA · media
### Los riesgos que se materializaron

La tabla de riesgos es prospectiva. Hoy sabemos **cuáles se materializaron**, y contarlo con la mitigación
efectiva es más fuerte que la previsión original. Los tres principales:

1. **Riesgo materializado: no hay un modelo que haga las dos cosas.** Los modelos capaces de sostener CR-01
   no siguen el ritmo de la cámara (14–22 % de keep-up en RTSP); los que sí lo siguen son ciegos al estado
   observable de CR-01. Es un hallazgo del trabajo, no una falla.
2. **Riesgo materializado: identidad de detección inestable** ⇒ mitigado con granularidad de escena (R-04).
3. **Riesgo materializado: pérdida silenciosa en el transporte** ⇒ mitigado con numeración de secuencia y
   degradación explícita de la corrida (R-08).

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

## R-21 · Tablas 58 y 59 (backlog) · EVIDENCIA · alta
### El backlog ya no es un backlog: es un estado

> ✎ **2026-08-05 — DESBLOQUEADO, con una corrección sustantiva.** Este ítem esperaba
> ADR-015 (doc 95 §5.3), ya escrito:
> [`decisiones/adr-015-cierre-de-alcance.md`](../decisiones/adr-015-cierre-de-alcance.md)
> (✅ aceptada el 2026-08-05). **El resumen de estado de abajo tiene un punto FALSO al cierre:** dice
> *"MOT ✗ (especificado, tracker no implementado, E-03)"*. La granularidad por sujeto **sí
> está implementada y medida** — es el mejor resultado del banco (F1 0,930 sobre 34 clips,
> más verificación en vivo). Lo excluido son las **métricas** MOT (E-10, "no aplicable"),
> no la capacidad. Corregir esa fila al transcribir; el resto del resumen (11/11 del
> núcleo, EBE ✅, rol EN ✅, inspección ✅, fine-tuning ✗ E-04) se sostiene. Estado
> completo por exclusión: **ADR-015 §2a**.

Los 16 ítems del backlog tienen hoy un estado real y verificable. Propuesta: **convertir las Tablas 58/59 en
una tabla de estado** (ítem → entregable → **estado** → evidencia), que es exactamente el tipo de tabla que
el tutor espera encontrar en un capítulo de concreción.

Resumen del estado (a transcribir ítem por ítem): **de los 11 ítems del núcleo, 11 están construidos**
(configuración, lectura DBE, prompts versionados, adaptador OVD, postproceso, instrumentación de medios,
publicación y persistencia, evaluación de patrones, alertas por episodio, instrumentación de control,
reporte consolidado). De las 5 extensiones: EBE ✅ (two-node dockerizado, verificado con cámara IP real),
rol EN ✅ (Nodo A), inspección ✅ (webconsole), fine-tuning ✗ (excluido, E-04), MOT ✗ (especificado,
tracker no implementado, E-03).

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

## R-22 · §17.3.14.5 · PRECISA · media
### EBE: lo que ya se hizo y la brecha que queda

**DEBE DECIR** — dos precisiones honestas:

1. **La fuente viva ya se ejercitó realmente**: cámara IP por RTSP, con timestamps de reloj de pared
   verificados. El EN candidato del informe (OAK-D Pro PoE) no estuvo disponible al inicio y se ejerció la
   **contingencia oficial ya prevista** en §17.1.4.2.4 (cámara IP convencional). **Update 2026-07-13: el
   hardware llegó y quedó integrado y verificado E2E como fuente `oak_d`** — la narrativa para el informe
   es doble y más fuerte: la contingencia estaba escrita antes de necesitarla, Y el EN candidato terminó
   funcionando como estaba previsto (captura en la OAK, inferencia en el host). **Update 2026-07-15/18:
   además, EN-2 quedó implementada como variante opcional on-device** (gate de personas en la cámara,
   fail-open, default off; A/B real con GDINO: 87 % de drop on-device) — ver nucleo/10 E-07 y doc 56 §2.1;
   la afirmación previa "EN-2 sigue fuera de alcance" quedó superada.
2. **Queda una brecha declarada**: comparar DBE y EBE **sobre la misma fuente** (reproducir un clip anotado
   como stream) requiere un ancla de sincronización entre el reloj de pared del stream y el tiempo de medio
   del ground truth. Está identificada, no resuelta.

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

## R-23 · varias · ERRATA · baja
### Erratas de forma

- **Las seis figuras están vacías** en el documento y **cinco no tienen número** ("Figura x"). Hay que
  dibujarlas: vista lógica (4.1), pipeline de medios, plano de control, máquina de estados, cadena de
  traducción, roles. **Más la vista de procesos nueva** (R-09).
- Títulos de tabla pegados al número: "Tabla 44Elementos…", "Tabla 45Vocabulario…", "Tabla 51Hechos…",
  "Tabla 58Backlog…", "Tabla 59Backlog…".
- Oración **duplicada** en §17.3.15 (ver R-17).
- Frases pegadas sin espacio tras el punto en §17.3.15 y §17.3.18 ("…condicionadas.La arquitectura…").
- Errata de puntuación en §17.3.5, línea 235: "…o flujos de streaming**, El** plano de medios…".
- **NO son erratas** (verificar sólo visualmente al exportar a PDF): los "nombres de métrica vacíos" de la
  §17.3.13.1 y la Tabla 52 son **objetos de ecuación de Word** que la extracción automática no captura.
  En el documento original casi con seguridad se ven bien.

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

## R-24 · fuera del §17.3 · PRECISA · media
### Inventario de datasets desactualizado

> ✎ **2026-08-06 — el insumo ya existe (escritura pura):** el inventario quedó **al
> día el 2026-08-05** (`operacion/99` — relevamiento completo de datasets de imágenes,
> registry actualizado), como ya lo registró la anotación de R-13. El redline sigue
> siendo transcribir la selección efectiva al informe; la evidencia está lista.

El inventario del informe (SH17, SHEL5K, CHV, Pictor-PPE, Construction-PPE, GDUT-HWD, SHWD, SODA, MOCS) es
**anterior a la selección efectiva**. Los tres conjuntos realmente utilizados son
`construction_site_safety`, `chv` y `ppe_siabar`. El documento final debe declarar **qué candidatos se
retuvieron y por qué** — no dejar la lista larga como si todos se hubieran usado.

*(Este ítem vive fuera del capítulo 17.3, pero se registra acá para no perderlo.)*

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

## R-25 · §17.3.11 (Tabla 50) y §17.3.13 · CONCRETA · alta
### El contrato de ground truth temporal y la convención de identidad de fuente

**DICE HOY** — nada. El capítulo define contratos para la corrida, pero **ninguno para la referencia contra
la que se evalúa**. Sin embargo, la evaluación de alertas —de donde salen P/R/F1, TTFD y SDR— depende de un
contrato de anotación tan formal como los otros.

**DEBE DECIR** — agregar el contrato a la tabla:

> **Referencia temporal de evaluación** (`clip_gt.v2`) — *Anota, por clip, los episodios en que una
> condición de riesgo está efectivamente presente.* Información mínima: identificador de clip, episodios
> con inicio y fin en milisegundos y condición asociada, eventos por debajo del umbral de persistencia,
> tolerancia de frontera, procedencia de la anotación (anotador, doble anotación, coeficiente de acuerdo) y
> las ventanas de persistencia del conjunto de patrones con el que se comparará.

Y declarar **dos invariantes** que no son detalle de implementación —son condiciones de validez de la
medición— y que se descubrieron por las malas:

1. **La identidad de la fuente y la del clip anotado son la misma.** El emparejamiento entre una alerta y un
   episodio anotado es, literalmente, una comparación de identificadores de fuente. Si la corrida etiqueta
   la fuente de un modo y la anotación de otro, **el emparejamiento falla en silencio y la exhaustividad da
   cero** sin ningún error visible. Es una convención de contrato, no una preferencia.
2. **La incertidumbre nunca fabrica una infracción.** Cuando el estado de un elemento de protección no puede
   determinarse en la anotación, el episodio **no se declara**: un atributo desconocido corta la corrida de
   violación en lugar de extenderla. La referencia se construye para ser conservadora.

**Y los cinco hitos por alerta** (que hoy tampoco están, y son los que hacen computable la cadena): primera
evidencia positiva —con su unidad visual, que es la clave de unión entre planos—, transición a candidato,
transición a confirmado, registro de la alerta y, cuando exista canal, confirmación de entrega.

**POR QUÉ** — spec 43 (`clip_gt.v2`), doc 54 §5 (la convención de identidad: sin ella, recall 0 en silencio),
spec 40 §5.4 (los cinco hitos).

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

## R-26 · §17.3.17 / §17.3.18 · CONCRETA · **alta (y es la más valiosa)** → **texto en doc 94 §9**
### Extensibilidad medida: cuánto cuesta agregar una condición nueva

**DICE HOY** — nada. Y es, probablemente, el hueco más caro de todo el capítulo.

**DEBE DECIR** — tu tesis **no** es "OVD detecta mejor". Es *"qué se logra con una plataforma que expresa
condiciones en lenguaje, sin entrenar"*. Todo el resto del capítulo mide latencias, pérdidas y ventanas —
cosas que un sistema de vocabulario cerrado también podría medir. **Esta sección mide lo único que un
detector cerrado no puede hacer**, y hoy no está escrita en ningún lado.

La tabla de costos de extensión, con su frontera declarada:

- Una **condición nueva del mismo tipo** (sujeto sin elemento de protección) → **sólo configuración**: una
  entrada declarativa en el conjunto de patrones + las formulaciones de prompt. **Cero código, cero
  reentrenamiento.**
- Una **familia nueva** de condiciones (relacional, zonal, de trayectoria) → **un evaluador nuevo**.
- Un **modelo nuevo** → un adaptador. Una **fuente nueva** → un adaptador.

**El contraste entre las dos primeras filas es la contribución arquitectónica del trabajo**: delimita la
frontera real de la extensibilidad por lenguaje, en vez de prometer que "todo es configurable".

> ✎ **2026-08-06 — DESBLOQUEADO: A1 YA CORRIÓ (2026-08-05, `operacion/94`).** El
> condicional de abajo quedó viejo — el número existe y es AF-4 del doc 98:
> **0 entrenamientos · 1 archivo de 48 líneas · 9 minutos · 0 GT nuevo anotado**,
> `machinery` **AP@0.5 0,662 zero-shot** (n=99 cajas), por encima del agregado del
> campeón con las clases configuradas. Con el contrapeso obligatorio **F-94.1**
> (validar la palabra: `vehicle` junto a `machinery` = 0 detecciones; el bench lo
> expone en ~3 min). Cifras: `results/bench_imagenes/index.md` §4.

Si el **mini-experimento A1** (costo marginal de una condición nueva, doc 10 ítem 8) llega a correrse, su
número va acá: *N líneas de configuración, T minutos, una corrida registrada*. Vale más, en la defensa, que
media docena de latencias.

**→ Texto completo en `94-secciones-nuevas-etapa3.md` §9.**

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

## Orden sugerido de trabajo

1. **R-01 y R-05 juntos** (van de la mano: estrategia + vocabulario). Es el ajuste que más cambia el capítulo.
   *Antes de escribirlo, decidí el punto (a)/(b) de R-01: compromete o no el experimento comparativo.*
2. **R-02, R-03, R-04** (las otras contradicciones). Con esto el capítulo deja de contradecir al sistema.
3. **R-06, R-07 y R-25** (contratos concretos + evolución del evento + contrato de la referencia). Con esto
   el capítulo deja de ser conceptual: es la respuesta al tutor.
4. **R-26** (extensibilidad medida). Barato de escribir y es el argumento central de la tesis.
5. **R-12 y R-13** (evidencia + límites). Con esto el capítulo es *verificable*, que es la palabra que usó él.
6. El resto, en orden de prioridad de la tabla.
