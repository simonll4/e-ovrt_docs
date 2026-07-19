# Plan de cierre — implementación, adquisición del banco y experimentación

> **Qué es (2026-07-19):** el plan operativo para **cerrar el núcleo validable**
> aplicando el principio rector del doc 57 §7.6 (el cierre lo decide la cobertura
> de material; nada bloquea, lo no cubierto se declara). Tres frentes en paralelo:
> **(A)** tareas de implementación (Claude, no requieren material),
> **(B)** adquisición del banco (grabación propia + internet, equipo de 3),
> **(C)** experimentación en dos etapas (doc 57 §7.4) y reporte.
>
> **Insumos:** doc 57 (metodología del banco completa), spec 43 (guiones §3,
> `clip_gt.v2` §4, métricas §10), spec 41 §7 (`cr01_cr02_v2` 4000/7000),
> doc 55 PASO 4 (guía de grabación, ya actualizada), doc 52 (bug A del matching).

---

## A. Tareas de implementación (Claude) — arrancan YA, no dependen del material

En orden de ejecución (cada una desbloquea o protege métricas):

| # | Tarea | Repo | Qué desbloquea | Referencia |
|---|---|---|---|---|
| A1 ✅ | **HECHO + revisado (2026-07-19, TDD, 112/112).** Gate de dimensionamiento en `derive_clip_gt.py`: función pura `dimensioning_warnings(gt)` (por episodio, cada condición su `t_alert_upper`+`resolve`+cola; onset ≥ 2000 ms) → `provenance.dimensioning_warnings` + aviso en el timeline impreso (no bloquea). Verificado contra `video16_clip10`: caza el onset en t=0 y la censura CR-02. `DIMENSIONING_MS`={CR-01:10000/2000, CR-02:20000/3000}. **Revisión:** endurecido `duration_ms` opcional (`.get()`, no rompe; schema v2 la permite None) | datasets | Protege TTFD/t_alert de artefactos de recorte en TODO clip futuro | doc 57 §6.5.3 |
| A2 ✅ | **HECHO (2026-07-19, TDD, 231/231).** `metric_censored` en `_evaluate_v2` (control-plane `evaluation/temporal.py`): un episodio `missed` cuyo clip no cubre la ventana de matching completa (`duration_ms < start_ms + t_alert_max_ms`) se **censura** (sale del denominador de recall) en vez de contarse como fallo; un episodio con match cuenta normal. Modelo `CensoredEpisode`, campos `censored_episodes_count`/`censored_episodes`. Con ≥1 episodio evaluable el `applicability_state` sigue **`computed`** (recall es real sobre los evaluables; la censura se declara por `censored_episodes_count`+warning, sin romper a un consumidor que chequea `== "computed"`); solo si TODOS quedan censurados es `not_applicable:all_episodes_metric_censored` (ADR-006). Umbral < que el de A1 (sin resolve/cola): A1 avisa temprano en autoría, A2 censura solo lo no medible | control-plane | Banco estratificado sin contaminar denominadores (clips de 12 s conviven con los de 30 s) | doc 57 §6.7 |
| A3 ✅ | **HECHO + revisado (2026-07-19, TDD, 239/239).** FAR/hora en `_evaluate_v2`: campos `far_per_hour` (= FP ÷ `duration_ms`/3.6e6) y `observed_duration_ms` (para que el reporte agregue Σ FP / Σ horas entre clips soak, no promedio de tasas). `None` sin `duration_ms`. Verificado en clip negativo de 1 h con 2 FP → 2.0. **Revisión:** alertas sin timestamp → razón `missing_timestamp` (no `outside_all_episode_windows`) y excluidas del numerador de FAR; `observed_duration_ms` conservado en el early-return no-temporal | control-plane | La métrica con material en cero hoy — G1, la de mayor retorno | doc 57 §3.2 G1 |
| A4 ✅ | **HECHO + revisado (2026-07-19, TDD, 239/239).** Matching bipartito (Kuhn/augmenting-paths) reemplaza el greedy en `_evaluate_v2`: maximiza episodios cubiertos, ≤1 alerta por episodio y ≤1 episodio por alerta; adyacencia ordenada por timestamp. Verificado: P8 con 2 episodios solapados → recall 1.0 (greedy daba 0.5). **Revisión atrapó un bug real (bloqueante):** la interacción censura↔matching dependía del orden del GT (mismos datos → recall 1.0 o 0.5 según el orden de los episodios). **Fix:** ordenar los slots con los NO censurables primero, para que el match vaya al episodio evaluable y el censurable quede afuera — recall independiente del orden | control-plane | P8 scoreable — sin esto el clip P8 grabado se desperdicia | doc 52 §bug A |
| A5 ✅ | **HECHO (2026-07-19).** Verificado doc 04 §8: el criterio de desempate 2 usaba "menor latencia de alerta" (= t_alert-system). **Corregido a TTFD** con banner de enmienda al pre-registro fechado, antes de correr D1 (sigue bloqueado por acta `edir_v1`, así que la enmienda es legítima, no post-hoc). La latencia de alerta se sigue midiendo, pero como caracterización Nivel B, no como discriminante | docs | Protege la validez del experimento D1 | doc 57 §7.3.1 |
| A6 ⛔ | **NO REALIZABLE con el material actual (2026-07-19, hallazgo verificado).** Los videos en `datasets-videos/raw/` **también son de 12 s** — son clips ya cortados, no los originales largos; NO existe fuente más larga en disco para re-ventanear con onset en t≈3 s. Estos 12 s son el material original. Resolución (doc 57 §4/§6.7): mantienen su rol diagnóstico/negativo (P1-marginal/negativos, nunca P2/P4/P6/P8); A1 ya los marca con `dimensioning_warnings` al derivar. El fix real son los nuevos videos >20 s de internet (tarea del usuario, en curso), no salvar estos | datasets | (superado por adquisición nueva) | doc 57 §4.2 |
| A7 ✅→ reencuadrada | **CORRIDA y REENCUADRADA (2026-07-19, §B.2.1).** El prefiltro `bare_head` (GDINO-base vía `preannotate_video`) corrido sobre `4.1` (noche) y `2.1` (día) mostró que el modelo **sobre-marca `bare_head` masivamente** a la distancia de estas cámaras (4.1: 8/10 tracks, casi todos duración completa; 2.1: 7/31, corridas cortas) — debilidad `bare_head` del Sprint 2, cuantificada. **Consecuencia:** el prefiltro **NO puede auto-certificar los negativos** (marca infractores falsos en todos), así que los negativos quedan **verificados a ojo por el humano**, no por el modelo. La sobre-marca NO se descarta: es el **insumo directo de FAR/hora** (Nivel B) — las detecciones falsas sostenidas >4 s se vuelven falsas alertas CR-01 al pasar por la plataforma. Esto se mide en la fase C (experimentación), no en pre-anotación | media-plane | Caracterización Nivel A (piso de detección de casco a distancia) + test-bed de FAR | doc 57 §6.9/§7 |

**Estado (2026-07-19):** A1–A5 ✅ hechas (pre-rodaje, listas antes de anotar el
primer clip). **A6 ⛔ descartada** (el material fuente es de 12 s, sin original
largo — ver fila). **A7 ⏳** corre en cuanto haya videos de internet en
`datasets-videos/`.

---

## B. Adquisición del banco

### B.1 Grabación propia (Bloque A + C) — la jornada única

> **✎ 2026-07-19: el shot-list operativo para llevar impreso a la sesión es el
> `operacion/59-guion-grabacion-bloque-a.md`** (casillas por toma, hoja de
> registro, checklist de cierre). Este §B.1 queda como la referencia de
> planificación; ante cualquier divergencia de números, doc 59 fue reconciliado
> el 07-19 con los canónicos (P2×3, P8=30 s mín, P9=infracción real).

**Setup común:** cámara fija en trípode (sin zoom/paneo — condición EBE), 720p
base (1080p en 1–2 clips como variante), FPS nativo declarado. **2 tomas por
guion**, se promueve la mejor. Onset **siempre en t≈3–4 s**. Roles: 1
cámara/director con el timeline planificado (regla de oro spec 43 §3.3: el plan
garantiza que los casos ocurran, el GT sale del video), 2 actores (rotan; P7
necesita 2–3 en cuadro).

**Las escenas, una por una** (duraciones del doc 57 §2/§6.3; consentimientos Ley
25.326 ANTES de grabar — bloqueante legal):

| Escena | Tomas | Dur. | Guion (timeline real) | Variables C.2 |
|---|---|---|---|---|
| **P1-a** sin casco persistente | 2 | 20 s | 0–3 con casco → 3 se lo quita → 3–17 infracción sostenida → 17 se lo pone → 17–20 cola | interior, 5–10 m |
| **P1-b** ídem, variante | 2 | 20 s | mismo guion | **exterior, 10–20 m** |
| **P2-a** sin chaleco persistente | 2 | 30 s | 0–4 con chaleco → 4 se lo quita → 4–26 infracción → 26 se lo pone → 26–30 cola | interior, 5–10 m |
| **P2-b** ídem, variante | 2 | 30 s | mismo guion | **exterior**, 5–10 m |
| **P2-c** ídem, tercera | 2 | 30 s | mismo guion | 10–20 m |
| **P3** transitorio NO alertable | 2 | 15 s | 0–3 con EPP → 3–5 sin casco (**solo 2 s**) → 5 se lo pone → 5–15 cumplimiento (se observa ≥1 ventana completa sin alerta) | libre |
| **P4** resolución | 2 | 25 s | 0–3 con casco → 3 se lo quita → 3–13 infracción (≥10 s) → 13 **se lo pone** → 13–25 permanece en cuadro resuelto | libre |
| **P5 (=V3)** cumplimiento total | 2 | 15–20 s | EPP completo todo el clip, actividad normal de obra | exterior si se puede |
| **P6** doble condición | 2 | 30 s | como P2 pero se quita **casco y chaleco** juntos → episodios CR-01+CR-02 solapados | libre |
| **P7-a** multi-persona | 2 | 30 s | 3 personas, una sin casco; **cruces y oclusiones** deliberadas entre 10–20 s | oclusión media |
| **P7-b** ídem, variante | 2 | 30 s | 3 personas, una sin chaleco, cruces | oclusión media |
| **P8** entrada/salida | 2 | **30 s** | 0–3 cuadro vacío → 3 **entra ya sin casco** → 3–11 infracción → 11 **sale de cuadro** → 11–16 ausencia (≥5 s > resolve) → 16–24 vuelve sin casco → 24 se lo pone → 24–30 cola. GT: **2 episodios** (ep2 arranca en t≈16 s ⇒ el clip DEBE llegar a 30 s: floor A1 = 16000+10000+2000+2000 = 30000; a 28 s el gate avisaría) | libre |
| **P9** confusables | 2 | **18–20 s** (✎ 07-19: era 15 s — al ser infracción CR-01 real rige el floor 3+10+2+2=17 s) | Actores con **gorra** (sin casco), **campera naranja** (sin chaleco), casco **en la mano/colgado**. **GT corregido (✎ 07-19): estos SON infracciones reales** (gorra sin casco ⇒ episodio CR-01; campera naranja sin chaleco ⇒ CR-02) — el confusable no testea FP sino si el modelo **PIERDE** la alerta (confunde gorra con casco = falso cumplimiento). Recall bajo estrés semántico | libre |
| **V1** (defensa) cadena completa | 2 | 25–30 s | infracción clara → detección → alerta (el clip demo E2E) | el más vistoso |
| **V2** (defensa) clase nueva por config | 2 | 20–30 s | según guion doc 09 (condición nueva solo por prompt/config) | libre |
| **Soak propio** | 1 | **5–10 min** | trípode fijo, obra/actividad normal en cumplimiento, SIN guion — dejar correr | la escena más "real" |

**Total: 15 escenas × 2 tomas ≈ 31 tomas + 1 soak ≈ media jornada de rodaje.**
Clips finales promovidos: **15** (13 Bloque A + V1 + V2) + soak propio.

Nota P8: el timeline correcto es *entra ya sin casco* (la primera aparición abre
el episodio 1); la salida corta el episodio; la reentrada abre el 2. No arrancar
el clip con la persona en cuadro.

### B.2 Videos de internet — cuotas, roles y criterios de aceptación

**Criterios de aceptación (todos):** cámara fija o casi fija, **sin cortes de
edición dentro del tramo usado**, sin zoom/paneo brusco, ≥720p, obra de
construcción real, licencia registrable (asentar SIEMPRE en
`datasets/registry/license_registry.md` + `download_log.md` — regla del repo).
Se recortan con `prepare_clip.sh` aplicando la regla de onset (si tienen evento)
o como negativos (si no).

| Cuota | Cantidad | Duración | Rol en el banco | Métricas que cubre |
|---|---|---|---|---|
| **Cortos en cumplimiento** (todos con casco+chaleco) | **5–8** (objetivo 6) | 12–15 s c/u | P5-negativos adicionales (2–3), confusables naturales (2: gorras/ropa naranja/cascos colgados), diversidad C.2 (1–2: otras obras, luces, distancias) | **precision** (FP semánticos), robustez visual — **NO recall** (0 episodios, doc 57 §6.9) |
| **Medianos 20–30 s** | **3–5** (objetivo 4) | 20–30 s c/u | (a) negativos largos (mejor denominador de precision); (b) **candidatos a minado de positivos** (A7): si contienen una infracción real espontánea → episodio de validación externa no guionado (oro); (c) si alguno es continuo y fijo → mini-soak | precision, FAR parcial; recall externo SOLO si el minado encuentra infracción |
| **Soak de internet** (si existe) | 0–2 | ≥5 min continuos, cámara fija | complementa/reemplaza parcialmente el soak propio — OJO: la mayoría del footage público tiene cortes; si no aparece uno continuo, el soak sale del rodaje propio (B.1) y esta cuota queda en 0 sin problema | **FAR/hora** |

**Regla de esfuerzo:** no gastar más de una sesión de búsqueda por cuota. Si una
cuota no se llena, rige el principio §7.6: la métrica afectada se reporta con el
n que haya o `censored` con causa. Las cuotas de internet **nunca** bloquean el
cierre — solo el rodaje propio es crítico, y tiene piso n≥8 (spec 43).

#### B.2.1 ESTADO: lote adquirido 2026-07-19 — cuotas de internet CUBIERTAS

**14 videos nuevos en `datasets-videos/raw/`** (todos 1080p/30 fps, ~15.9 min
totales, obra real, cumplimiento PPE ≈100% salvo un evento). Inventario y roles:

| Video | Dur. | Rol |
|---|---|---|
| **6.1** | **6:10 min** | **SOAK** ✅ — ≥5 min continuos, **0 cortes de escena** (verificado con detector, umbral 0.35). Cuota soak: cubierta |
| 3.2 (1:45), 5.1 (1:19), 10.1 (0:59) | >50 s | mini-soaks / negativos largos (también 0 cortes) |
| 2.1, 8.1, 9.1, 1.1 | 35–50 s | negativos largos |
| 1.2, 4.3, 4.2, 7.1, 3.1 | 20–33 s | cuota "medianos": pedía 3–5, hay 6+ ✅ |
| **4.1** | **19.1 s** | **POSITIVO real no guionado** (ver abajo) |

**`4.1.mp4` — episodio CR-01 espontáneo, evaluable end-to-end** (verificado
frame a frame): obra vial **nocturna**, ~4 trabajadores en cumplimiento; en
t≈6 s **entra una persona sin casco** (chaleco amarillo, cabeza descubierta),
permanece ~11 s (camina, se agacha, cruza el cuadro) y **sale en t≈17–18 s**.
Chequeos: onset 6000 ms ≥ 2000 ✅ (primer clip del banco con TTFD real, no
artefacto); evento ~11 s ≥ persistencia 4 s ✅ (el motor debe confirmar en
~t=10 s); censura A2: 19066 ≥ 6000+10000 ✅ **recall y t_alert evaluables**;
gate A1: 19066 < 20000 ⚠️ warning marginal esperado (cola post-salida corta),
declarado, no invalida. Semántica P8 de apertura/cierre por presencia. Valor
doble: episodio de **validación externa** + condición **nocturna** (diversidad
C.2 que ningún otro material tenía).

**Decisión sobre cortos de 12 s (2026-07-19):** NO sumar por volumen — la cuota
"cortos" quedó obsoleta con este lote (para precision/FAR cuenta el tiempo
observado, ya hay ~16 min; un 12 s agrega 0.2 min y paga overhead fijo de
registry/prepare/verificación). Solo se agregan cortos que llenen un **hueco de
escena C.2 identificado** — prioridad: **confusables naturales (P9)** (gorras,
ropa naranja no-chaleco, cascos colgados), y exterior diurno con sol si el lote
resulta mayormente nocturno. Los 7 clips viejos de 12 s ya ocupan el rol
"cortos diagnósticos".

**Diversidad C.2 (barrido 2026-07-19): fuerte, sin hueco urgente.** Iluminación
✅ (≈10 diurnos + 4 nocturnos: 4.1/4.2/4.3/5.1); tipo de obra ✅ muy diverso
(fachada 1.1/1.2/10.1, excavación 2.1/3.1/3.2, estructura de acero en altura
7.1/8.1/9.1, vial/pavimentación 6.1/5.1, demolición nocturna 4.2/4.3); densidad
mixta; **todas cámaras fijas elevadas** (condición EBE, fuente única = canal de
obra SF → licencia simple). Los dos huecos (banda de distancia **cercana 5–10 m**;
**confusables P9**) los cubre mejor el **rodaje propio** (variable de grabación /
escena guionada), no más cortos de internet.

**Matiz sobre `4.1` tras A7:** sigue siendo un positivo real evaluable, pero es un
caso **DURO, no un showcase**: de noche el modelo marca `bare_head` en casi todos,
así que el clip mostrará **recall alto + precision baja** (el GT humano marca solo
el episodio real; el modelo inunda de falsos). Es un resultado honesto y un stress
de Nivel A — los positivos "limpios" de demostración salen del rodaje diurno.

**Pendientes del lote (antes de anotar):**
1. **A7 ✅ corrida** — hallazgo: el prefiltro sobre-marca, no certifica negativos
   (ver fila A7). Los negativos quedan **verificados a ojo** (ya lo hiciste); la
   sobre-marca alimenta la medición de FAR en fase C.
2. **Licencias:** registrar los 14 en `license_registry.md` + `download_log.md`
   (fuente/URL/licencia c/u) — **lo ejecuta el usuario**.
3. **Cámara fija/sin cortes:** ✅ verificado en los 14 (0 cortes de escena,
   detector umbral 0.35).
4. **Diversidad C.2:** ✅ barrido hecho (arriba).

### B.3 Anotación (post-rodaje, equipo de 3)

Pipeline del doc 54 (prepare → preannotate GDINO-base → CVAT → derive →
validate → promote). GT temporal por episodio: ~10–15 min/clip salvo los 2 P7
subject-level. Reparto: cada uno anota un tercio; **doble anotación ≥20% (mín. 3
clips, incluyendo 1 P7)** cruzándose entre dos, el tercero arbitra; kappa
reportado. Los negativos de internet: anotación casi nula (`negative: true` +
verificación visual de que no hay infracción espontánea). **Presupuesto total:
2–3 tardes.**

---

## C. Experimentación de cierre (protocolo doc 57 §7.4)

Con A1–A5 implementadas y el banco promovido:

1. **Etapa A — elegir el modelo (Nivel A):** correr los candidatos
   (GDINO-tiny primaria; YOLOE-26s réplica según doc 12 §3) sobre BENCH imágenes
   + banco temporal, **plataforma congelada** (4000/7000, motor idéntico).
   Comparar por AP@0.5 / TTFD / SDR / G2A. Sale el modelo del cierre (o el
   trade-off explícito calidad vs FPS).
2. **Etapa B — validar la plataforma (Nivel B):** congelar ese modelo; correr
   el banco completo + soak vía el runner del experimental-setup (trazabilidad
   `experiment_id → clip_id → gt`). Reportar recall / precision / FAR-hora /
   t_alert-system / t_compute-budget contra Tabla 35/D.4, con **n declarado por
   métrica** y estados de aplicabilidad.
3. **Análisis de errores (R3):** re_alerts, inesperadas, sub-umbral alertadas,
   matriz diagnóstica SDR×recall (doc 57 §7.3.2) — cada celda tiene diagnóstico
   distinto.
4. **Reporte de cierre:** las 5 declaraciones de Etapa 4 (doc 57 §7.5) + la
   cobertura como resultado ("estas métricas cierran con este n; estas quedan
   declaradas") — formato del principio §7.6.

### C.5 EBE en el rodaje — corridas live durante la sesión de grabación (agregado 2026-07-19)

**Por qué en el rodaje:** por ADR-013, hay métricas que solo una fuente live
(reloj wallclock) computa — en DBE-replay quedan `not_interpretable /
dbe_media_time`. La sesión de grabación es la única ocasión con actores +
escenarios controlados + cámara real: se ejecuta EBE ahí mismo.

**Qué mide EBE (y nada más puede medir):**

| Métrica | Qué responde | Target |
|---|---|---|
| **`t_capture→alert`** (spec 40 §5.2; `computed` SOLO en live) | captura del frame de 1ª evidencia → `AlertEvent` registrado | ≈ persistencia + G2A + bus: **~4.1–4.6 s** CR-01 / **~7.1–7.6 s** CR-02 |
| **`t_compute-budget`** (= t_capture→alert − persistencia efectiva) | overhead nuestro vs persistencia declarada | pequeño y estable (G2A 50–250 ms + bus + reasoning) |
| **G2A live** P50/P95/P99 + FPS efectivo + drops | costo del pipeline con cámara real | presupuesto 50–250 ms |
| **`bus_dropped_events`** | salud del bus ZeroMQ | **= 0** (gate de validez; huecos de `seq` degradan, no se silencian) |
| **Paridad live↔offline** | replay posterior del `detections.jsonl` live ⇒ artefactos idénticos | evidencia citable con contenido real (ya verificada con sintético) |

**Protocolo de DOBLE TOMA por escena (evita el problema del ancla):** el GT
temporal se anota en media-ms sobre archivo; la corrida live estampa wallclock;
el ancla wallclock↔media sigue **sin resolver** (EBE-desde-clip, declarado). Por
eso: **Toma A grabada** → banco DBE → CVAT → TTFD/SDR/t_alert/recall con GT;
**Toma B live** (misma coreografía) → corrida EBE 1:1 → t_capture→alert/G2A/bus
**sin GT** (las métricas sin-GT del spec 40 §5.2 existen exactamente para esto).
Cada plano mide lo suyo; nadie necesita el ancla.

**Escenas live mínimas:** 1× P1, 1× P2, **1× P3** (infracción breve que NO
alerta en tiempo real = la demo más fuerte de la persistencia; además es
material V1-like para la defensa). Opcional P6. Cada una = **una corrida 1:1**
con su `experiment_id`.

**Stretch opcional (no bloquea):** 1 escena con **claqueta** (palmada visible +
wallclock anotado por el operador) → GT live anclado
(`onset_wallclock = claqueta_wallclock + (onset_media − claqueta_media)`) →
**verificación numérica de la identidad `t_alert-system = TTFD +
t_capture→alert`** (spec 40 §5.2.2) — cerraría la promesa del spec con datos
reales. Si la logística no da, se declara diferido sin costo.

**Prerrequisitos técnicos (dry-run el día ANTES del rodaje):**
1. Ambos servicios sanos (`:8080` media / `:8081` control) + cámara (OAK-D
   192.168.1.50 o RTSP con preset de la ventana Cámaras; preview para encuadre).
2. **Orden de disparo live, no negociable:** `POST :8081/api/runs` (`mode:
   live`) primero — su 201 implica suscripto — y DESPUÉS `POST :8080/api/runs`
   con `bus.enabled: true` (PUB/SUB pierde lo anterior a la suscripción).
   Preferir el **runner del experimental-setup** (manifest live, control-first
   con `SubscriptionNotConfirmed`) por trazabilidad `experiment_id`.
3. **Pattern set `cr01_cr02_v2` en la config live** (4000/7000) — NO el `v1`
   diagnóstico de confirm=1.
4. Modelo `grounding-dino/gdino-tiny` cargado (`EOVRT_MODEL_REF`), single-host
   (un solo reloj — sin requisito de chrony).
5. Disco libre para `runs/` y NO borrar nada al terminar la sesión.
6. Smoke live de 1 min con un actor (quitarse el casco 6 s → debe confirmar
   CR-01 a ~4 s) — si el smoke no alerta, se arregla ANTES del rodaje.

**Dependencias D1:** la Fase 2 de D1 consume este mismo banco; el acta `edir_v1`
(usuario) sigue siendo el bloqueante de D1, no el banco.

---

## D. Secuencia consolidada (quién hace qué, en qué orden)

```
HECHO (2026-07-19):
  Claude:  A1 gate ✅ → A2 metric_censored ✅ → A3 FAR/hora ✅ → A4 bipartito ✅ → A5 doc 04 ✅
           (A6 ⛔ descartada: raw/ viejo también es 12 s, sin fuente larga)
  Equipo:  búsqueda internet (B.2) ✅ CUBIERTA — lote de 14 videos (§B.2.1):
           soak 6:10 + 12 negativos 20s–1:45 + POSITIVO real 4.1 (CR-01
           espontáneo evaluable). Cuota cortos: obsoleta (solo confusables si
           aparece hueco C.2).

SIGUIENTE (paralelo):
  Claude:  A7 prefiltro bare_head sobre los 13 negativos → luego prepare +
           derive de 4.1 (primer TTFD real del banco) y del soak 6.1
  Equipo:  licencias de los 14 en registry → consentimientos + guion impreso (B.1)
           → anotación del lote (4.1 en CVAT; negativos = verificación visual)

DÍA ANTES DEL RODAJE:                  dry-run EBE (§C.5 / doc 59 §7): servicios
                                        + cámara + smoke live (si no alerta, se
                                        arregla ese día)

JORNADA DE RODAJE (media jornada):     15 escenas × 2 tomas + soak propio
                                        + CORRIDAS EBE LIVE (doble toma §C.5:
                                          ≥1 P1 + ≥1 P2 + ≥1 P3 live)
                                        (los POSITIVOS guionados P1–P9 siguen
                                         saliendo SOLO de acá — P2 el crítico)

POST-RODAJE (2–3 tardes):              anotación B.3 → promote al banco
                                        (pasada humana CVAT reemplaza TODO
                                         gt_preliminary — incluye cb_b01_p7)

EXPERIMENTACIÓN:                        C.1 Etapa A → C.2 Etapa B → C.3 → C.4

DESPUÉS (no bloquea el cierre):         spec 45 (MQTT, para lo último),
                                        EBE-desde-clip (sin resolver, declarado)
```

**Criterio de "cerrado":** banco promovido con GT humano + corridas A/B con
reporte que declara cobertura por métrica. No hay métrica individual cuya
ausencia lo frene (§7.6) — pero A1–A4 sí son bloqueantes de la *calidad* del
reporte, por eso van primero.
