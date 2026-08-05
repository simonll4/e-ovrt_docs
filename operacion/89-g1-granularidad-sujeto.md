# 89 — G1: granularidad por sujeto. El resultado más grande del banco

- **Fecha:** 2026-08-04.
- **Qué es:** la última palanca abierta (doc 88 §6). Ataca el mecanismo **(a)** de
  F-81.2 — el único de los diagnosticados que ninguna palanca de percepción ni de
  formulación puede tocar.
- **Estado:** 34/34 clips, **sin GPU**, 0,4 min. Suites verdes.

## 1. El resultado

| Métrica | T1 (escena, G0) | **G1 (sujeto)** |
|---|---|---|
| Recall micro | 0,824 (28/34) | **0,971** (33/34) |
| Precision micro | 0,757 | **0,892** |
| **F1** | **0,789** | **0,930** |
| Episodios perdidos | 6 | **1** |
| FP | 9 | **4** |
| Negativos | 0/4 | **0/4** |
| **SDR** | 0,698 | **0,698** |
| **TTFD** | 167,8 ms | **167,8 ms** |

**SDR y TTFD son idénticos hasta el decimal.** No es coincidencia: las detecciones son
bit a bit las de T1 —no hubo inferencia nueva— y esas dos métricas miden percepción.
**Los +0,141 de F1 vienen enteros de la granularidad del motor.** Es el contraste de
variable única más limpio de toda la serie.

### Por escenario

| Esc. | T1 | **G1** | FP |
|---|---|---|---|
| P1 | 1,000 | 1,000 | 0 → 0 |
| P2 | 1,000 | 1,000 | 1 → 1 |
| P4 | 1,000 | 1,000 | 0 → 0 |
| P6 | 1,000 | 1,000 | 0 → 0 |
| **P7** (multitud) | **0,400** | **1,000** | **5 → 1** |
| **P8** (entrada/salida) | **0,500** | **1,000** | 1 → 1 |
| **P9** (pre-roll frágil) | 0,600 | **0,800** | 2 → 1 |

Los tres escenarios que concentraban todas las fallas del banco desde el doc 81 se
resuelven o mejoran. **P7 pasa de 0,400 a 1,000.**

## 2. Cómo se corrió: post-hoc, sin GPU y sin tocar el pipeline

El motor consume `Detection.track_id` bajo `granularity: subject` desde siempre
(spec 41 §2.1) y el contrato existe de punta a punta: **lo único que faltaba era el
productor** (doc 79). Se aportó **post-hoc** sobre las corridas ya hechas:

```
detections.jsonl de T1 → track_detections → tracked.jsonl → replay (subject) → evaluate
```

`python -m eovrt_control.tools.track_detections` reusa `SimpleIoUTracker` de
`eovrt_labs` (ya testeado) y suma 8 tests para el pegamento, que es donde estaban las
trampas: escribe en **`track_id`** y no en `detection_id` (el bug del doc 34 §4.1 que
el doc 79 señalaba), procesa los frames **en orden** (desordenados el tracker ve saltos
hacia atrás y fragmenta identidades) y deja el resto de las clases intacto.

Es la ruta (b) que el doc 79 recomendaba —*renderer offline post-hoc, la defensa no
exige `track_id` en vivo*— y confirma su análisis de esfuerzo: horas, no días, y **cero
riesgo sobre el pipeline congelado**.

**Guard contra medir G0 creyendo medir G1:** si una persona quedara sin `track_id`, el
motor degrada a clave de escena con causa `no_track_id` **en silencio**. El runner
verifica por clip que ninguna quede sin identidad y aborta ese clip si ocurre. 34/34
pasaron.

## 3. Verificación: la ganancia no es un artefacto del evaluador

La sospecha razonable es que con N sujetos haya N oportunidades de alertar dentro de la
ventana, y que el recall suba por rociar alertas. **No es lo que pasa.** En los 4 clips
de P7:

| | alertas emitidas | matched | re_alerts | FP |
|---|---|---|---|---|
| T1 (escena) | **7** | 2 | 0 | 5 |
| G1 (sujeto) | **7** | **5** | 1 | **1** |

**El mismo presupuesto de alertas** (7 y 7): lo que cambia es que aterrizan donde
corresponde. Y la precisión global sube (0,757 → 0,892) en vez de bajar, que es lo que
pasaría si el motor rociara.

## 4. F-89.1 — El déficit de P7 era exactamente lo que F-81.2a decía

El doc 81 diagnosticó: *"el GT exige que UN sujeto sostenga la violación 4 s (regla C1
de `derive_clip_gt`); el motor a nivel escena acumula 'alguien sin casco', y en multitud
los sujetos se relevan"*. Se registró como **el costo medido de operar sin `track_id`**.

Darle identidad al motor lo elimina: P7 de 0,400 a 1,000. **El diagnóstico era correcto
y la predicción se cumplió.** Es la asimetría C1/ADR-012 cerrada con datos.

## 5. F-89.2 — El "pre-roll frágil" era también un problema de identidad, no solo de percepción

Las alertas prematuras de pre-roll caen de **5 a 1** (mecanismo por
`85-mecanismo-de-fallas.py`).

Esto **refina F-81.2b**. El doc 81 atribuyó esas prematuras a percepción — *"el modelo
no ve el casco a esa distancia/ángulo"* — y el doc 84 mostró que un modelo mejor no las
arregla (T2 las empeoraba). Ahora se ve por qué: bajo escena, **basta que CUALQUIER
persona del cuadro esté sin casco** para que la escena entre en evidencia, incluso
durante el pre-roll en que el sujeto objetivo sí cumple. No era (solo) que el modelo no
viera el casco del actor: era que el motor estaba mirando a otra persona.

Bajo sujeto, cada persona acumula su propia persistencia y el pre-roll del violador real
empieza cuando corresponde. Queda 1 prematura de 0,5 s —dentro del ruido de la
tolerancia— y P9 no llega a 1,000 (0,800): ahí sí queda un residuo de percepción.

## 6. Lo que esto cambia en la lectura de toda la serie

Cuatro palancas de **percepción y formulación** se probaron y **ninguna** superó a T1:

| Palanca | Campaña | F1 |
|---|---|---|
| Formulación directa (frases) | D1 | 0,160 |
| Fusión E-HYB-or | H1 | 0,296 |
| Modelo especialista | T2 | 0,704 |
| Vocabulario nativo (`bare_head`) | B1 | 0,377 |
| — línea de base — | **T1** | **0,789** |
| **Granularidad por sujeto** | **G1** | **0,930** |

**El margen que quedaba no estaba en el modelo ni en los prompts: estaba en la noción
de identidad del motor.** Es un resultado fuerte para la tesis porque es exactamente el
argumento de la plataforma: lo que agregó valor no fue cambiar el detector —el detector
es el mismo, con las mismas detecciones bit a bit— sino **lo que la plataforma construye
encima**. Y se consiguió sin re-inferir, en 0,4 min de CPU.

## 6 bis. ✎ 2026-08-04: G1 dejó de ser post-hoc — es capacidad de la plataforma

Tras este doc se implementó la identidad como **decorador de fuente en el
control-plane** (`sources/tracking.py`, `input.track_persons`, opt-in default `false`),
cableado en los dos runtimes. Decora cualquier `MediaEventSource`, así que **G1 está
disponible en DBE y en EBE/live sin que el media-plane emita `track_id`** — el port del
spec 42 §3 deja de ser el camino obligatorio. 12 tests nuevos, suite 305 passed.

**Verificado:** el camino config-driven **reproduce esta campaña exacto en los 34
clips**, 11 campos por clip (matched/missed/FP, re_alerts, precision/recall/F1,
t_alert, SDR y TTFD). El 0,930 es lo que rinde la plataforma configurada por YAML, no
un script. La re-revisión crítica endureció además el decorador (delegación de
`close`/`request_stop`/`dropped_events` — sin eso live silenciaba las pérdidas del
bus) y atrapó una trampa preexistente de la plataforma (colisión de directorios de run
en el mismo segundo, fix en `prepare_run`). Suite 310 passed.

La adenda correspondiente está en `decisiones/adr-002-…md` (pendiente de ratificación
del usuario). El §7 de abajo se conserva como el planteo original de la decisión, que
la implementación reencuadró: ya no hay que elegir entre "post-hoc" y "portar al
media-plane".

## 7. Decisión que queda para el usuario (no se re-litiga sola)

**ADR-002 fija G0 (escena) como núcleo y `subject` como demostrativa.** Esta medición
dice que `subject` no es solo demostrativa: es **+0,141 de F1** sobre el banco, con
menos FP y sin costo de percepción.

Reabrir o no ese ADR es decisión del usuario, y hay argumentos del lado de mantenerlo:
- el `track_id` de esta campaña es **post-hoc**; en vivo requiere el port al pipeline
  (spec 42 §3, 1–2 días) con purga de estado del motor y revalidación;
- el banco es de **material guionado** (L4) con multitudes acotadas; la robustez del
  tracker en obra real no está medida;
- ADR-002 se tomó por auditabilidad y costo, no por rendimiento.

Lo que sí cambia sin discusión es **cómo se reporta**: la comparación G0-vs-G1 deja de
ser "una demo" y pasa a ser **un resultado con número**, y el costo de G0 queda
cuantificado para el informe.
