# ADR-015 — Cierre de alcance al final del tramo experimental: el alcance creció, y se registra

> **✎ 2026-08-10 — PARCIALMENTE DEROGADO por [ADR-016](adr-016-reapertura-acotada-distribucion.md).**
> **Caen §2b** (ninguna capacidad nueva), **§2c** (la distribución MQTT declarada no
> implementada y no reabierta) **y §6** (criterio de invalidación). El usuario decidió
> construir el módulo de distribución para cerrar la arquitectura de la plataforma; ADR-016
> lo autoriza con el recorte exacto de ADR-005 y vuelve a cerrar la puerta detrás.
>
> **SIGUEN VIGENTES Y RATIFICADOS: §2a, §3, §4 y §5** — la tabla del alcance que creció
> (E-03/E-04/E-07/E-13) y **la lista de límites que reemplaza a R-13, con las limitaciones
> L1–L8**, que son la fuente de la sección de límites del informe. Citar §3 de este
> documento sigue siendo correcto.
>
> Lo único que cambia en §3 es la fila *"Distribución no implementada"*: deja de ser
> exclusión cerrada y pasa a **trabajo comprometido**, con su estado al momento de la
> entrega (ADR-016 §5).

> **✅ ACEPTADA por el usuario el 2026-08-05.** Los cambios que este ADR mandaba ya se
> aplicaron al doc 10: el **ítem 10** de la lista de alcance (G1 dejó de decir
> "demostrativa … en 2–3 clips") y las filas **E-03 / E-04 / E-07 / E-13** de la tabla de
> exclusiones. Con eso, el registro de alcance y los resultados dicen lo mismo.

- **Fecha:** 2026-08-05
- **Estado:** **Aceptada** (usuario, 2026-08-05)
- **Decisión que atiende:** el doc 95 §5.1 lo pedía como *"ADR-015 — recorte final de
  alcance"*, con este fundamento: los docs 91/94 declaraban el **tracker/G1 como no
  implementado**, y hacía falta una decisión formal que recortara. **Esa premisa se
  invirtió.** G1 se implementó, se midió sobre los 34 clips y es **el mejor resultado del
  banco** (F1 0,930). Así que el ADR que falta no es un recorte: es el **registro de que
  el alcance creció, con evidencia, y de qué sigue excluido**.
- **Decisor:** usuario, **2026-08-05** (delegó la redacción y aceptó el contenido)
- **Bloquea/desbloquea:** **R-13** (registro de lo no implementado) y **R-21** (estado del
  backlog, Tablas 58/59) del doc 93 — el doc 95 §5.3 los dejó explícitamente esperando
  este ADR. Son los dos únicos redlines con dependencia formal abierta.

---

## 1. El hueco

El doc 10 (registro de alcance y exclusiones, 2026-07-07) fijó el principio: *"el proyecto
implementa el núcleo validable y lo detiene ahí"*, con 11 ítems de alcance y 13
exclusiones E-01…E-13. Tres ADRs lo ampliaron de forma acotada y quedaron registrados
ahí mismo (ADR-002, ADR-008, ADR-009).

Después de eso corrió **todo el tramo experimental** (docs 61–101: rodaje, 12 campañas de
Nivel B, Fase D de Nivel A, Fase L de tiempo real, piloto A1, blindaje EBE). Y el alcance
real se movió en cuatro exclusiones, **sin que ninguna decisión lo registre**:

- **E-03** decía que G1 entraba solo como *capacidad demostrativa* (2–3 clips). Terminó
  medida en **34/34 clips y verificada en vivo**. ADR-002 ya lleva una adenda del
  2026-08-04 que lo reconoce, pero el doc 10 sigue diciendo "demostrada en 2–3 clips".
- **E-07** (borde) pasó de excluida a **parcial**: OAK-D como fuente ejercida y prefilter
  EN-2 implementado con 87% de descarte on-device medido.
- **E-13** (modelos extra / E-HYB) se ejercitó más de lo previsto: **E-HYB-or corrió y
  quedó refutada** con número, y `hyb_and` **no se ejecutó por fundamento**, no por
  tiempo.
- **E-04** (fine-tuning) sigue no ejercida, pero cambió de estado: los splits están
  materializados y el camino está operacionalizado — es *decisión de no ejercerla*, no
  falta de preparación.

Y en paralelo, **la lista de "lo no implementado" que el capítulo iba a declarar (R-13)
quedó vieja**: de sus 8 ítems, **5 ya no son ciertos**. Publicarla tal cual sería declarar
como límites cosas que se resolvieron — el error simétrico al de sobrevender.

## 2. Decisión

**(a) El alcance final es el del doc 10 más cuatro movimientos, y se declaran como
alcance ampliado con evidencia, no como hallazgo tardío.** Se registran acá y se
reflejan en el doc 10:

| Exclusión | Cómo quedó al cierre | Evidencia |
|---|---|---|
| **E-03** — G1 como modo del núcleo / GT de identidades | **Se amplía**: G1 es **capacidad operativa config-driven**, no demostrativa. Medida en los 34 clips (F1 0,930 vs 0,789 de G0) y verificada en vivo. **Sigue excluido:** GT de identidades y validación MOT | doc 89, doc 91, ADR-002 adenda 2026-08-04, `results/clip_bench/g1_*` |
| **E-10** — métricas MOT estándar | **No cambia: sigue "no aplicable"**, y ahora con fundamento medido — la ganancia de G1 se mide en la métrica de la plataforma (alertas), no en MOTA/IDF1, porque **las detecciones son bit a bit las mismas** (F-89.1) | doc 89; ADR-002 |
| **E-07** — borde / EN-2 / OAK-D | **Parcial, ya registrado**: OAK-D como fuente (2026-07-13) y EN-2 opcional default off (2026-07-15), con **87% de descarte on-device** medido A/B contra GDINO. **Sigue excluido:** inferencia en borde (EN-3) | doc 10 E-07; doc 10 E-07 evidencia |
| **E-13** — modelos extra / E-HYB-vote | **Ejercida más allá de lo previsto**: T2/B1 (modelo especialista) y **E-HYB-or ejecutada y refutada** (F-87.2: la unión de evidencia no es monótona). **`hyb_and` no ejecutada con causa** (D-90.4: no medible contra este banco sin romper la comparabilidad de las 6 campañas) | docs 84/87/88; `results/clip_bench/` |
| **E-04** — fine-tuning / TN | **No se ejerce** (se mantiene). Cambia el motivo declarable: no es falta de preparación (splits materializados, camino operacionalizado, costo medido ≤1 GPU-h en A30) sino **decisión de secuenciación** | doc 100; ADR-010 |
| E-01, E-02, E-05, E-06, E-08, E-09, E-11, E-12 | **Sin cambios.** Siguen como el doc 10 las declaró | doc 10 |

**(b) No se agrega ninguna capacidad más.** Este ADR **cierra** el alcance: de acá al
informe solo se corre, se mide y se escribe (regla del doc 02 §7). El material que falta
(GT del lote de internet) **no agrega capacidad**: agrega una sección de generalización
sobre capacidad que ya existe.

**(c) La distribución MQTT (ADR-005 / spec 45) queda declarada como NO implementada, y
no se reabre.** Era el "punto de decisión" que el doc 95 §5.4 puso en la semana 6. La
decisión es: **no**. Se declara como exclusión ejercida con su justificación, no como
deuda.

**(d) R-13 se reescribe** — la lista de límites del capítulo es la de §3, no la de 8
ítems del doc 93.

**(e) R-21 se corrige en un punto sustantivo**: su tabla de estado dice *"MOT ✗
especificado, tracker no implementado, E-03"*. **Es falso al cierre.** Debe decir que la
granularidad por sujeto es capacidad operativa medida, y que lo excluido son las
**métricas** MOT (E-10), no la capacidad.

## 3. La lista de límites que va al capítulo (reemplaza la de R-13)

Auditada ítem por ítem contra artefacto el 2026-08-05. De los 8 originales, **5 se
resolvieron**:

| Ítem original de R-13 | Estado real al cierre |
|---|---|
| Sin productor de `track_id` | **RESUELTO / cambió de forma.** G1 es capacidad operativa config-driven y el tracker vive en el control-plane; no hace falta productor en el media-plane (ADR-002 adenda) |
| Distribución no implementada | ✎ **2026-08-10 (ADR-016): SIGUE sin implementar, pero como TRABAJO COMPROMETIDO**, no como exclusión cerrada. Se reporta con su estado al momento de la entrega. *Decía "exclusión ejercida y cerrada, no como deuda (§2c)"* — §2c fue derogada |
| Evaluadores de D1 pendientes | **RESUELTO.** D1 corrió (doc 85): E-DIR descartada por **veto de precisión** (0,146 < 0,5) |
| GT preliminar | **RESUELTO para el banco.** Los 34 clips están `gt_ready` (CVAT humano + 6 bordes adjudicados con firma). **Sigue** para los 14 clips del lote de internet |
| Brecha de sincronización en EBE-desde-clip | **SIGUE**, y se precisa: falta el ancla wallclock↔media **como ingeniería de campaña** (doc 101 §3). El ancla *puntual* sí se cerró con reloj externo (doc 101 §5.4, las 4 patas) |
| G2A no computable en dos nodos | **SIGUE** (relojes monotónicos de hosts distintos no son comparables) **y se agrava con F-101.8**: incluso en un host, G2A se mide desde el *dequeue*, no desde el fotón |
| Matching greedy que puede deflacionar recall | **RESUELTO.** Matching **bipartito** implementado (enmienda A4 del doc 58, TDD) |
| Inventario de datasets desactualizado | **RESUELTO.** `operacion/99` (2026-08-05) puso al día el registry |

**Y los límites que el tramo experimental agregó** (no estaban en la lista de R-13). Son la
**lista canónica L1–L8**, cerrada el 2026-08-05; la versión de referencia con el texto largo
está en `e-ovrt_experimental-setup/results/index.md` §Limitaciones declaradas. **Al citar
`L1` escribir "limitación L1"**: la Fase L usa `L0`/`L1` para sus hitos.

- **L4** — un solo bloque guionado, sin obra real en video. La más citable; la levanta el
  lote de internet cuando tenga GT (su procedencia ya está registrada).
- **L1** — FAR/hora no reportable (D-90.1): se reemplaza por el control de negativos.
- **L8 — CR-02 a Nivel A no cerrada**: un solo estrato, IC solapados.
- **L5** — escenarios desbalanceados ⇒ reportar siempre por escenario y estrato.
- **L2** — sin doble anotación ni kappa (decisión declarada).
- **L3** — seis bordes del GT adjudicados por oclusión, con firma.
- **L6 — el tracker no está medido en obra real con multitud**: G1 se verificó en vivo con
  pocos sujetos; el `track_id` es post-hoc/decorador.
- **L7 — licencia de `chv` parcial** (20,5% del bench de imágenes): uso permitido con cita,
  sin redistribución.
- **Procedencia del material de video, declarada** (spec 43 §7, registrada el 2026-08-05):
  el **rodaje** es material propio en el que los grabados son los integrantes del proyecto
  actuando según guion, sin terceros en cuadro; el **lote de internet** es material de
  terceros (canal público `@HospitalConstruction`, *Standard YouTube License*) usado con
  cita y **sin redistribución**, con dos caveats declarables: no es cámara-nativo
  (corregido de color y estabilizado por el autor) y las caras se difuminan si un frame va
  como figura. La velocidad real está verificada, así que las métricas temporales aplican.

La lista consolidada y etiquetada está en `informe/ajustes/gobierno/99-materiales-de-cierre.md` §4.1.

## 4. Fundamento

**Por qué registrar un alcance que creció, en vez de dejarlo pasar.** El proyecto tiene
una regla estructural (doc 95 §3, nacida de una auditoría que encontró una cifra estrella
sin respaldo): *ninguna afirmación sin artefacto, y ningún cambio silencioso*. Un alcance
que se amplía sin registro es la versión inversa del mismo problema — el tribunal
encuentra en los resultados una capacidad que el registro de alcance declaraba excluida, y
eso **debilita todo lo demás**, aunque la capacidad esté bien medida. Declararlo lo
convierte en lo que es: una ampliación acotada, justificada y medida.

**Por qué no es "recorte".** El doc 95 escribió su pedido en julio, cuando G1 no existía.
Cumplir literalmente ese pedido hoy —recortar alcance— obligaría a **esconder el mejor
resultado del banco** o a presentarlo como fuera de alcance. Sería cumplir la letra
violando el propósito.

**Por qué cierra también la puerta.** El riesgo real que el doc 95 quería cubrir sigue
vivo, y es el otro: seguir agregando capacidad cerca de la defensa. §2b y §2c son ese
cierre, y son la parte de este ADR que **restringe**.

## 5. Impacto

- **Doc 10: ✅ aplicado el 2026-08-05.** ADR-015 está en el encabezado, el **ítem 10** de
  la lista de alcance quedó reescrito (G1 = capacidad operativa medida en 34 clips, no
  "demostrativa en 2–3") y las filas **E-03 / E-04 / E-07 / E-13** de la tabla de
  exclusiones quedaron actualizadas con su evidencia.
- **Doc 93:** **R-13 y R-21 quedan desbloqueados**. R-13 se redacta desde §3; R-21 se
  corrige en el punto de MOT/tracker.
- **ADR-002:** su adenda del 2026-08-04 queda subsumida acá; no se re-litiga.
- **ADR-005:** su condicional ("¿MQTT sí o no?") queda **resuelto: no** (§2c).
- **Informe:** la sección de límites y la tabla de estado del backlog salen de §3 y §2,
  no de las listas de julio.
- **Lo que NO cambia:** ninguna cifra. Este ADR no toca un solo número medido — reordena
  qué se declara como alcance y como límite.

## 6. Criterio de falsación

Este ADR es un registro, no una hipótesis técnica, así que no tiene test. Pero sí tiene un
**criterio de invalidación**: si entre hoy y la defensa se agrega **cualquier capacidad
nueva** (una condición CR nueva implementada, distribución MQTT, inferencia en borde,
métricas MOT), este ADR queda **violado** y hay que reemplazarlo, no enmendarlo. La
señal es simple: si aparece código nuevo que no sea corrección de un defecto medido,
§2b se rompió.

## Referencias

Doc 10 (registro de alcance, E-01…E-13) · doc 95 §5.1/§5.3 (el pedido original de
ADR-015 y la dependencia de R-13/R-21) · doc 93 R-13 y R-21 · ADR-002 + su adenda
2026-08-04 (G1 medida) · ADR-005 (distribución) · ADR-010 (secuenciación) · doc 89
(campaña G1) · doc 85 (D1, veto de precisión) · doc 87 (E-HYB-or refutada) · doc 101 §3
y §5.4/§5.5 (ancla y F-101.8) · doc 58 enmienda A4 (matching bipartito) · doc 100
(camino de fine-tuning) · `operacion/99` (registry de datasets al día) ·
`operacion/98` §6 (limitaciones) · `informe/ajustes/gobierno/99-materiales-de-cierre.md` §4
(limitaciones y ADRs) · spec 43 §7 (marco legal del material de video).
