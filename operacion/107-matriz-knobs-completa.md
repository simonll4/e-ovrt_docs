# 107 — La matriz de knobs completa contra el estrato B (+ mecanismos y tests)

**Fecha:** 2026-08-06, última tanda de la jornada. **Qué es:** los 5 ítems que el doc
106 §3 dejó listos para disparar, ejecutados. Con esto **la matriz de configuración
del pattern set queda barrida completa** contra el estrato B (el doc 104 había hecho
`min_subject_area_px`; acá van los otros dos knobs de `evidence`, el `timing`, la
clasificación de mecanismos y la deuda de tests). Todo CPU, cero inferencia nueva,
ADR-015 intacto.

**Método idéntico al doc 104**: variable única sobre `cr01_cr02_v2_subject`, streams
trackeados de I2 (tiny), replay + evaluate por celda, ventanas de matching ancladas al
GT (`origin: gt_provenance`). **Calibración in-sample declarada**: caracteriza knobs,
no elige configuración de producción. Runner: `datos/107-barrido-knobs-runner.py`;
crudos en `datos/107-barrido-knobs/`.


> ## ⚠️ CORRECCIÓN POSTERIOR — leer antes que nada (2026-08-07, doc 108 §6)
>
> Este documento se escribió cuando el GT de **`v06_c01` tenía un episodio CR-02**
> (342.400–355.533 ms). La revisión visual en CVAT determinó que **era un error de
> anotación: la persona SÍ llevaba chaleco**. El episodio **no existe**; `v06_c01` es
> **negativo** (P5) y pasó a ser **el primer clip soak del banco**.
>
> **Qué NO cambia (todo el análisis de mecanismo de este doc):** la evidencia perpetua
> del modo escena, la fragmentación del tracker, el colapso de la asociación de `vest`
> con la escala, el acople alucinación↔supresión. Todo eso se midió sobre las
> **detecciones**, que no cambiaron.
>
> **Qué SÍ cambia:** los conteos que tratan a `v06_c01` como clip positivo. Sus alertas
> ya no son "el episodio que el motor no encontró" sino **falsas alarmas sobre un
> negativo**. Cifras vigentes: `results/clip_bench/index.md` y doc 108 §6.


---

## 1. Barrido A — `min_subject_confidence` (0,35 → 0,40/0,45/0,50)

Motivación: los sujetos de los FP de I1 entraban con confianza 0,39–0,40.

| valor | matched | FP pos. | FP neg. (`v10`) | precision |
|---|---|---|---|---|
| 0,35 (=I2) | 2/2 | 196 | 20 | 0,010 |
| 0,40 | 2/2 | 156 | 13 | 0,013 |
| 0,45 | 2/2 | 132 | 6 | 0,015 |
| **0,50** | **2/2** | **108** | **5** | **0,018** |

> **F-107.1 — la confianza del sujeto es LA MEJOR palanca individual del estrato B.**
> −48% de FP total (216→113) con **recall intacto hasta 0,50**, y supera al gate de
> área en su punto declarado (113 vs 133 FP a igual recall). Tiene sentido físico: los
> sujetos-fantasma del tracker (fragmentos, falsos person) viven en la cola de baja
> confianza. Igual que el gate: convierte "inutilizable" en "malo" (precision 0,018) —
> ninguna palanca individual cruza a "operable".

## 2. Barrido B — `min_absent_class_confidence` (0,25 → 0,30/0,40/0,50)

**Medido antes de barrer**: el stream tiene **piso 0,30 en las 3 clases**
(`box_threshold` del modelo) ⇒ el baseline 0,25 ya acepta toda la evidencia y
**bajarlo es no-op**. El control 0,30 lo confirma: reproduce I2 **exacto** (216 FP).

| valor | matched | FP total | FP `v10` (sin chalecos reales) |
|---|---|---|---|
| 0,30 (control) | 2/2 | 216 | 20 |
| 0,40 | 2/2 | 306 (+42%) | 26 |
| 0,50 | 2/2 | 356 (+65%) | 34 |

> **F-107.2 — el knob de confianza de la evidencia NO es accionable en este régimen:
> hacia abajo es no-op (piso del stream), hacia arriba fabrica ausencia.** La
> predicción pre-registrada se confirmó, y de paso quedó **medido el acople
> alucinación↔supresión** de F-104.4: en `v10_c01` (donde los "chalecos" detectados
> son alucinación sobre gente con arnés), rechazar evidencia débil destapa 20→34 FP.
> La alucinación estaba *suprimiendo* falsas alarmas. Corolario incómodo y citable:
> **en E-IND, una detección espuria de la clase de evidencia es un supresor de
> alertas** — el error de un lado enmascara el error del otro.

## 3. Barrido C — `timing.confirm_after_ms` de CR-02 (7.000 → 10.000/12.000)

**Chequeo de compatibilidad estilo F-DR9, ANTES de correr**: el GT clasifica
episodio/sub-umbral con 7.000 ms; un motor a 12.000 no puede confirmar violaciones
reales de 7–12 s (falsos missed). Con ESTE GT no existen (episodios de 14,0 y 13,1 s;
sub-umbral máximo 1,4 s) ⇒ el barrido es válido acá y **no generaliza a otro banco sin
re-chequear**.

| valor | matched | FP total | t_alert del episodio real (`v06`) |
|---|---|---|---|
| 7.000 (=I2) | 2/2 | 216 | 8.433 ms |
| 10.000 | 2/2 | 171 (−21%) | 8.900 ms |
| 12.000 | 2/2 | 147 (−32%) | **15.667 ms** |

> **F-107.3 — la persistencia mata fragmentos a un costo de latencia medido.** −32%
> de FP a 12 s, recall intacto, pero el t_alert del episodio real se va de 8,4 s a
> **15,7 s — a 4,3 s del borde de la ventana de 20 s**. Es la palanca con el
> trade-off más explícito: cada segundo de persistencia extra compra FP y paga
> latencia uno a uno.

## 4. La matriz completa, en una tabla

Las cuatro palancas de configuración contra el mismo material, mismas detecciones:

| palanca | mejor valor probado | FP 216→ | recall | costo |
|---|---|---|---|---|
| `min_subject_confidence` | 0,50 | **113** | 2/2 | ninguno visible acá |
| `min_subject_area_px` (doc 104) | 16.500 | 81* | 2/2 | *sin margen: violador ≈19.200 px² |
| `confirm_after_ms` CR-02 | 12.000 | 147 | 2/2 | t_alert 8,4→15,7 s |
| `min_absent_class_confidence` | — | contraproducente | 2/2 | no accionable (F-107.2) |

**La celda combinada NO se corrió, a propósito.** Apilar los knobs ganadores sobre los
mismos 3 clips que motivaron cada elección sería sobre-ajuste in-sample por
acumulación: cada barrido individual caracteriza un mecanismo; la combinación solo
tendría sentido contra clips frescos. Queda escrito como el experimento que valida (o
no) la config "far-field" si alguna vez se anotan más clips.

**La conclusión del doc 103/104 no cambia: ninguna palanca, ni la mejor, cruza a
operable** (la mejor precision individual es 0,018). La frontera es real; la
configuración la corre, no la elimina.

## 5. Mecanismo de los FP de I1/I2 (taxonomía del doc 85)

`datos/85-mecanismo-de-fallas.py` (con un fix retrocompatible: el escenario ahora
puede salir del GT cuando el naming no lo trae — los `vNN_cNN` no tienen `_pX_`):

| tipo | I1 (scene) | I2 (subject) | rodaje (T1, referencia) |
|---|---|---|---|
| `prematura_pre_roll` | 2 | **117** | 5 |
| `cruzada_de_condicion` | 3 | 79 | 4 |
| `sin_episodio_activo` | 2 | 20 | 0 |
| `tardia` | 0 | 0 | 0 |
| **adelanto mediano de "prematuras"** | 341,9 s | **221,2 s** | **0,5 s** |

> **F-107.4 — la taxonomía satura en clips largos y hay que leerla con eso.** En el
> rodaje, "prematura" significaba una alerta que se adelanta medio segundo al borde de
> la ventana — un problema de bordes. Acá el adelanto mediano es **221 segundos**: la
> etiqueta técnica aplica (misma condición, antes de la ventana) pero el mecanismo es
> otro — **otra persona, en otra parte del plano, fabricando la misma condición
> minutos antes del episodio real**. Es la firma numérica de la evidencia fabricada
> del doc 103, vista desde la taxonomía. Para el informe: las columnas I1/I2 de esta
> tabla no se comparan con las del rodaje sin esta nota.

## 6. Tests del scorer de Nivel A (la deuda del doc 106)

`datasets/tests/test_score_clip_person_state.py` — **8 tests, fixture sintética** al
estilo de la suite (suite completa: **291 verdes**). Cubren los 5 riesgos: `unknown`
excluido (ni FP ni cumplimiento), geometría con `outside=1` descartado, atributos en
cajas interpoladas, la región suprime/no-suprime según corresponde, y el stride.
Regresión verificada: el scorer testeado reproduce exactamente los números del doc 105.

De paso quedó documentada una trampa de fixture para el futuro: **el export real de
CVAT repite los atributos mutables en CADA caja** (también las interpoladas,
`keyframe="0"`); un fixture que los ponga solo en el keyframe produce `None` en los
frames intermedios y no representa lo que CVAT emite (`attribute_states` lee la caja
vigente, no "el último keyframe con atributo").

## 7. Cierre del frente

Con esto, los 5 ítems del doc 106 §3 están ejecutados. **El frente de los clips nuevos
queda sin trabajo pendiente del lado de la plataforma**: matriz de knobs completa,
mecanismos clasificados, deuda de tests saldada. Lo que sigue es lo que ya decía el
doc 106 §4: el orden del usuario (videos V1–V3 → redacción), las decisiones de
encuadre del equipo, y —si alguna vez llega material nuevo anotado— la celda combinada
del §4 como primera validación out-of-sample.
