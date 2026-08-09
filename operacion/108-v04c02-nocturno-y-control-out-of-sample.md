# 108 — `v04_c02` (nocturno): el primer éxito limpio del estrato B, y la palanca ganadora refutada fuera de muestra

**Fecha:** 2026-08-06, cierre. **Insumo:** el usuario anotó `v04_c02` en CVAT — el
segundo clip nocturno, pedido justamente para reforzar el eje que colgaba de `n=1`.
**Salida:** banco **38 clips**, y **dos resultados que cambian conclusiones del mismo
día**.


> ## ⚠️ CORRECCIÓN POSTERIOR — leer antes que nada (2026-08-09, doc 113 §B)
>
> La **revisión ciega del GT** determinó que los **2 episodios de `v04_c02` eran
> errores de anotación**: el único sujeto (track 6) está en la cabina de una máquina
> durante todo el clip y su estado (casco y chaleco) **no es observable** — ambos
> atributos corregidos con firma a `unknown`; el clip es **NEGATIVO** (volvió a la
> expectativa original de curación, P5). Eso toca las dos mitades de este doc:
>
> - **El "primer éxito limpio del estrato" (título incluido) queda invertido:** el
>   recall 1,000 / 0 FP que este doc celebra medía contra episodios que no existían.
>   Las mismas alertas son ahora **falsas alarmas sobre un negativo** (3 en `scene`,
>   4 en `subject`) — y el caso pasa a ser el ejemplo más crudo de la frontera de
>   juzgabilidad: **ni el anotador ni el motor podían juzgar, y los dos declararon
>   violación.**
> - **F-108.2 pierde su evidencia literal pero no su lección:** el "episodio real"
>   que la palanca `min_subject_confidence 0,50` costó fuera de muestra ya no existe
>   como episodio. Sigue siendo un HECHO que la palanca corrió la alerta de 4,0 s a
>   18,3 s sobre el primer material fresco — comportamiento no anticipado por la
>   calibración in-sample —, así que la conclusión operativa (ninguna configuración
>   sale recomendada; la celda combinada cerrada sin ejecutar, doc 110 §4) se
>   sostiene por esa razón, no por el "missed".
>
> Lo que NO cambia: §6 (la corrección de `v06_c01`, que esta misma revisión ciega
> re-confirma como patrón), F-108.4, F-108.5 (con su nota de FAR ya corregida) y la
> mecánica de F-108.1 (fragmentación por densidad). Cifras vigentes del estrato:
> banner del doc 111 y `results/clip_bench/index.md`.


---

## 1. Integración

Export **task-level** (task 15, 840 frames), alineado exacto con el `info.json`
existente (840). Cadena estándar sin desvíos: `corrected/` → `derive_clip_gt` →
`validate` (0 errores) → `promote_clip --state gt_ready` → `build_clip_bench`.

**Banco: 37 → 38 clips**, reportable, freeze 153 archivos OK. `manifest.yaml` sha256
`befd7de7…` (el freeze de 34 del rodaje sigue en el commit `f7a27fe6`; el de 37 del
estrato B en el historial de la jornada). Nota operativa: **`promote_clip` volvió a
borrar el bloque de comentarios del manifest** — la trampa que el doc 102 §3 ya había
documentado; restaurado a mano por segunda vez en el día.

**Escenario corregido contra el GT: P5 → P6.** El `clip.yaml` decía "cumplimiento
total" y anticipaba `negative: true`. El GT humano deja **un mismo sujeto (track 6)
violando las dos condiciones a la vez** durante 23,8 s ⇒ P6 (doc 72 §4.6). Es el
tercer clip del lote cuyo escenario de curación resultó falso (van `v04_c01` P8→P1,
`v06_c01` P5→P2 y ahora éste): **la clasificación previa a anotar no acertó ninguno de
los tres clips positivos.**

**GT resultante** — 2 episodios, ambos **evaluables SIN censura** (CR-01 exige 14 s
desde el onset, CR-02 exige 25 s, el clip dura 28 s):

| ep | condición | ventana | sujetos |
|---|---|---|---|
| ep1 | **CR-01** | 0 → 23.833 ms | 1 |
| ep2 | **CR-02** | 0 → 23.833 ms | 1 |

⚠ **Aviso A1: onset en t=0, sin pre-roll.** El TTFD de este clip colapsa a 0 como
artefacto del recorte (el master arranca con la infracción en curso) — misma patología
que los 4 pilotos (F-102.1). **Recall y precision son citables; TTFD y t_alert se leen
con esa advertencia.**

## 2. Nivel B: el primer éxito limpio de todo el estrato B

| config | matched | missed | FP | re_alerts | SDR | t_alert |
|---|---|---|---|---|---|---|
| **`scene`** | **2/2** | 0 | **0** | 1 | 0,646 | 5.533 ms |
| **`subject`** | **2/2** | 0 | **0** | 3 | 0,646 | 9.133 ms |

**Recall 1,000 y precision 1,000 en las dos granularidades.** Es la primera vez en
todo el lote de internet que una configuración acierta todo sin una sola falsa alarma.

> **F-108.1 — `scene` funciona perfecto acá, y eso CONFIRMA por contraste el mecanismo
> de F-103.1.** En `v06_c01` (127 personas) la condición queda en **evidencia perpetua**
> y nunca re-arma: el motor emite una alerta y se calla 6 minutos — verificado en
> `pattern_events.jsonl`, y **sigue siendo cierto tras la corrección del GT** (§6), que
> no toca el comportamiento del motor sino contra qué se lo juzga. `v04_c02` es nocturno
> y **disperso**: esencialmente un violador en cuadro. Sin multitud no hay captura, y la
> escena — inservible en `v06` — acá alcanza. **La variable no era la granularidad: era
> la densidad.** `subject` solo hace falta cuando los sujetos se relevan.
>
> Corolario para el informe: **no existe "la mejor granularidad" del banco; existe la
> granularidad correcta para un régimen de densidad.** G1 gana en el rodaje y en
> `v06`; en escenas dispersas, escena empata con menos maquinaria (y con **t_alert
> 3,6 s más rápido**: 5,5 s vs 9,1 s).

## 3. El control out-of-sample: la palanca ganadora del doc 107, REFUTADA

El doc 107 midió que `min_subject_confidence: 0,50` era **la mejor palanca individual**
(FP 216→113, −48%, recall 2/2 intacto) — pero calibrada sobre los 3 clips del estrato
B, es decir **in-sample**. `v04_c02` no participó de esa calibración: es el primer test
fuera de muestra que el banco permite.

| config | matched | missed | FP | SDR ep1 / ep2 |
|---|---|---|---|---|
| `subject`, conf 0,35 (desplegado) | **2/2** | 0 | 0 | 0,513 / 0,779 |
| `subject`, **conf 0,50** (la "ganadora") | **1/2** | **1** | **1** | **0,229** / 0,583 |

**Mecanismo, leído en los `alerts.jsonl` crudos:** con 0,35 el motor confirma CR-01 a
los **4,0 s**; con 0,50 esa alerta **desaparece** y CR-01 recién se confirma a los
**18,3 s** — fuera de la ventana de matching (onset 0 + 4 s de persistencia + 10 s de
`t_alert_upper` = 14 s). El episodio real pasa a `missed` y la alerta tardía se cuenta
como FP. La cobertura de percepción del episodio cae a la mitad (SDR 0,513 → 0,229).

> **F-108.2 — la calibración in-sample era engañosa, y el primer clip fresco lo
> demuestra.** De noche la confianza del sujeto es baja por construcción; subir el
> umbral a 0,50 no filtra "sujetos-fantasma", **filtra al violador real**. La palanca
> que ganaba −48% de FP sobre los clips de su propia calibración **cuesta un episodio
> real** en el primero que no vio.
>
> Esto **valida la decisión del doc 107 §4 de NO correr la celda combinada**
> (`conf 0,50` + gate + persistencia 12 s): habría producido una "configuración
> far-field" recomendada que este clip refuta. Y **degrada** el estatus de las cuatro
> palancas del doc 104/107: dejan de ser candidatas a configuración y quedan como
> **caracterización de mecanismos**, que es lo que siempre dijeron ser en su salvedad.

**Lo que queda en pie del doc 107:** los mecanismos (dónde vive el ruido, qué lo mueve
y a qué costo) y las dos advertencias de lectura (F-107.2 alucinación↔supresión,
F-107.4 saturación de la taxonomía). **Lo que NO queda en pie:** cualquier lectura de
"0,50 es el valor recomendado".

## 4. Nivel A: perfecto arriba, malo abajo

Mismo scorer y punto de operación desplegado (`datos/108-nivel-a-v04c02.json`):

| condición | n eval | unknown | violadores | P | R | F1 |
|---|---|---|---|---|---|---|
| CR-01 | 218 | 10,7% | 51 | 0,069 | 0,039 | 0,050 |
| CR-02 | 242 | 0,8% | 51 | 0,095 | 0,137 | 0,112 |

> **F-108.3 — Nivel A malo con Nivel B perfecto, en el MISMO clip.** A nivel persona el
> sistema acierta poquísimo (F1 0,05–0,11); a nivel alerta acierta **todo** (2/2, 0 FP).
> No es contradicción: la alerta necesita que **un** sujeto sostenga la evidencia el
> tiempo de persistencia, y el motor temporal integra sobre 23,8 s de episodio; el
> Nivel A puntúa **cada persona en cada frame**. Con un solo violador real y mucho
> tiempo, basta con acertarle una fracción de los frames.
>
> Es una réplica independiente de **F-85.4** ("el ranking de Nivel A no transfiere a
> Nivel B"), ahora en la dirección optimista: **el motor temporal rescata percepción
> mediocre cuando la escena es dispersa y el episodio largo.** Y explica por qué el
> derrumbe de `v06` era tan severo: allá no había ni dispersión ni un solo sujeto.

## 5. Qué cambia en el cuadro general

1. **El estrato B deja de ser uniformemente malo.** Ahora tiene un clip donde el
   sistema funciona perfecto (`v04_c02`: 2/2, 0 FP), uno donde funciona a medias
   (`v04_c01`: 2/2 con `subject`, 9 FP) y dos negativos donde solo puede equivocarse
   — y en el denso se equivoca muchísimo (`v06_c01`: 190 FP en 6 min con `subject`).
   **La variable que los ordena es la densidad**, no la iluminación: los dos nocturnos
   dan los mejores resultados y el diurno denso es el peor.
   *(✎ redactado tras la corrección de §6: `v06_c01` ya no es un positivo que el
   sistema pierde, es un negativo que el sistema inunda de falsas alarmas. El
   mecanismo es el mismo; cambia qué nombre lleva el error.)*
2. **El eje nocturno queda reforzado** (era el pedido): de `n=1` a `n=2`, y con el
   segundo dando el mejor resultado del lote. **La noche no es la causa del fracaso**
   — es un agravante de percepción (SDR 0,646 vs 0,995 en `v06`) que el motor temporal
   absorbe cuando la escena es simple.
3. **Ninguna configuración recomendada sale de esta jornada**, y ahora está demostrado
   por qué: la única que se probó fuera de muestra falló.

## 6. ✎ MISMA NOCHE: la revisión visual de `v06_c01` corrigió el GT, y el banco ganó su primer soak

Mientras corría lo anterior, el usuario revisó en CVAT el track 110 de `v06_c01` —los
tres tramos que la auditoría del doc 102 §2.3 había marcado— y volvió con un veredicto
que **cambia el clip entero**:

| tramo | frames | veredicto del revisor | acción |
|---|---|---|---|
| ① `unknown` largo | 9935–10205 | *"está justo a un costado y no se puede diferenciar bien el vest"* | **confirmado correcto**, no se adjudica |
| ② `unknown` corto | 10207–10271 | *"está detrás de unas rejas y no se ve bien"* | **confirmado correcto**, no se adjudica |
| ③ el episodio | 10272–10665 | **la persona SÍ lleva chaleco** | **corregido `false` → `true`** |

**① y ② quedan cerrados como incertidumbre legítima** — y eso es un resultado, no un
hueco: confirma que el `unknown` del anotador marcaba material genuinamente no
juzgable (F-104.4 / F-105.4), no desidia.

**③ era un error de anotación.** No es una adjudicación de incertidumbre: es pisar un
valor explícito, algo que `apply_adjudications.py` **se niega a hacer por diseño**.

### 6.1 El mecanismo nuevo: `apply_attribute_corrections.py`

Herramienta hermana, deliberadamente separada, con **más** ceremonia que la de
adjudicaciones (8 campos obligatorios) y tres guards: `previous_value` verificado
(corta si el XML dice otra cosa), idempotencia, y rango-que-no-matchea es error.
13 tests (suite: **304 verdes**).

> **F-108.4 — el guard atajó un error real, y de ahí salió un campo obligatorio.** La
> primera redacción de la corrección no declaraba `track_id`, solo el rango de frames.
> En `v06_c01` ese rango contiene cajas de **7 tracks distintos**: la corrección
> firmada para *una persona* habría tocado a las demás. El guard de `previous_value`
> lo frenó (3 cajas del track 109 tenían `unknown`), y el arreglo fue hacer
> **`track_id` obligatorio sin default**: *una corrección es sobre el estado de una
> persona, no sobre un intervalo de tiempo.* Verificado tras aplicar: 394 cajas del
> track 110 cambiadas, track 109 intacto.

### 6.2 Lo que cambió en el banco — y por qué importa

`v06_c01` pierde su único episodio ⇒ **pasa a NEGATIVO** ⇒ y como dura 6:09,6
continuos, cumple la definición de soak (negativo ≥5 min, doc 57 §3.2 G1):

| | antes | ahora |
|---|---|---|
| escenario de `v06_c01` | P2 | **P5** |
| banco | 38 clips, 32 pos / 5 neg / **0 soak** | 38 clips, **32 pos / 6 neg / 1 SOAK** |
| episodios | CR-01 30 · CR-02 9 | CR-01 30 · **CR-02 8** |
| **denominador FAR** | **0,0 h — no computable** | **0,1027 h** |

> **F-108.5 — el banco tiene por primera vez un FAR/hora medido sobre obra real, y el
> número es malo: 48,7 FA/hora (escena) y 2.045,6 FA/hora (sujeto).** Durante toda la
> tesis FAR/hora fue *no reportable* por falta de horas de cumplimiento anotado
> ✎ **2026-08-09 — las cifras de FAR/hora de este doc quedaron corregidas.** El
> agregador calculaba `far_per_hour` con el numerador de todos los negativos y el
> denominador de solo los soak. Los valores correctos son **29,2** (escena) y
> **1.850,8** (sujeto). Detalle: doc 111 §6.

> (D-90.1). Ahora es computable — y lo que muestra no es un sistema con pocas falsas
> alarmas, sino uno que dispara **casi una por minuto en escena y más de 30 por minuto
> por sujeto**, sobre 6 minutos de obra real donde nadie infringe.
>
> **D-90.1 NO queda derogada, queda precisada.** Su argumento era que ningún
> denominador alcanzable permite afirmar *"≤1 FA/hora"*: con 0,1027 h y la regla de 3
> harían falta 3,0 h para sostener esa cota, y sigue faltando. Lo que cambió es que ya
> no hace falta el argumento: **no hay que declarar la métrica como no medible cuando
> el dato medido la refuta directamente.** Es un resultado más fuerte y más honesto
> que la limitación que reemplaza.

### 6.3 Campañas re-evaluadas (obligatorio, no opcional)

El GT cambió ⇒ los evals de `v06_c01` quedaron inválidos. Re-evaluados y re-agregados:

| | I1 `scene` | I2 `subject` |
|---|---|---|
| positivos | 1 clip, 1 episodio | 1 clip, 1 episodio |
| recall | 0,000 | **1,000** |
| precision | 0,000 | **0,100** (era 0,010) |
| F1 | — | **0,182** (era 0,020) |
| FP positivos / negativos | 2 / 5 | 9 / 210 |
| **FAR/hora** | **48,7** | **2.045,6** |

La precision de I2 sube 10× **sin que el sistema mejore**: los 187 FP de `v06` se
mudaron del cubo de positivos al de negativos. Es un recordatorio de la advertencia
F-104.2/§5.2 — *el conteo de FP se mueve por razones que no tienen que ver con
acertar*, y ahora también la precision.

**Distinción que sostengo:** re-agregar era **corrección obligatoria** (el GT cambió,
los números viejos son falsos). Sumar `v04_c02` a estas campañas sigue siendo
**decisión de encuadre pendiente** (§7.1) y no la tomé.

## 7. Estado y qué queda

Artefactos: `datos/108-v04c02/{scene,subject,subject_conf050}` + `eval_subject_conf050.json`
+ `datos/108-nivel-a-v04c02.json`. Banco 38 reportable, validadores en 0 errores,
suite 291 verde, GPU liberada.

**Abierto:**
1. **Las campañas I1/I2 siguen con 3 clips y ahora hay 4 en el lote.** Sus
   `metrics.json` NO incluyen `v04_c02` (sí incluyen ya la corrección de `v06_c01`,
   que era obligatoria). **Decisión de encuadre**: ¿el estrato B se reporta con 3
   clips —como se corrió— o con 4? Mi recomendación: incorporarlo, porque el clip es
   del mismo lote y excluirlo sería arbitrario, y además **`v04_c02` es el único que
   aporta un episodio CR-02 evaluable** ahora que `v06_c01` dejó de tenerlo. Es cambio
   de cifras publicadas y no lo hago sin que lo decidan.
2. Si `v04_c03` (el tercer clip del mismo master nocturno) vale la pena anotar para
   llevar el eje a `n=3`.
3. Lo de siempre: URL por video, adjudicación de `v06_c01`, decisiones de encuadre.
