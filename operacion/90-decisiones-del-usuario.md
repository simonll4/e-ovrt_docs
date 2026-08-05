# 90 — Tablero de decisiones del usuario (2026-08-04)

Con el eje experimental cerrado (docs 83–89: las cinco palancas del banco medidas,
E-IND núcleo por veto pre-registrado, G1 = 0,930 el mejor resultado), **lo que queda
por delante ya no se destraba con más corridas: se destraba con decisiones que son del
usuario**. Este doc las ordena por urgencia y dice qué desbloquea cada una. Faltan
~8 semanas para la defensa (~fin de septiembre).

Convención: **D-90.x**. Cada una con opciones, recomendación y qué desbloquea.
Las decisiones ya tomadas que NO se re-litigan (L2 sin doble anotación, `cb_b01_p7`
retirado, stride=1, MQTT al final) no aparecen.

---

## AHORA — tienen ventana de tiempo abierta

### ~~D-90.1 — Soak~~ → **RESUELTA 2026-08-04. Determinación: FAR/hora NO es una métrica reportable de esta tesis.**

**Insumo del usuario que cambió el análisis:** no consiguió videos largos de internet, y
anotar los largos es caro — el de 6 min todavía está en curso. Eso **refuta un supuesto
del doc 57**, no una decisión suya (ver corrección abajo).

#### La determinación

1. **FAR/hora se declara como limitación (L1) con causa cuantificada, no como un
   número de rendimiento.**
2. **La evidencia de falsas alarmas del informe es el control de negativos**, en su rol
   de evidencia **comparativa pareada** (mismas escenas, mismo GT, condiciones idénticas
   entre combinaciones): T1, T2, G1 y B1-eind dan **0 FP de 4 clips**; D1, H1 y
   B1-`bare_head` dan 2–3. Responde "¿qué combinación alarma cuando no debe?" — la
   pregunta comparativa, que es la de la tesis. Lo que NO responde es la tasa absoluta
   (2,1 min no cuantifican una tasa): esa queda declarada como L1.
3. El clip soak de 6 min, cuando esté, se reporta como el único con denominador
   temporal — **como contexto de la incertidumbre, nunca como rendimiento**.
4. Si al salir de CVAT los 13 clips cortos resultan negativos, se agrega un **análisis
   de sensibilidad** con el denominador ampliado, declarado como enmienda post-material.
   Opcional y secundario, no el número principal.

#### Por qué (cuatro razones, en orden de peso)

**(1) El número que yo había calculado no existe todavía.** Los 13 clips cortos **no
tienen GT** (`datasets-videos/gt/v*.json` = 0 archivos). Su `scenario: P5` es la
*expectativa* con que se curaron, no un hecho verificado — su propio `clip.yaml` lo dice:
*"El GT lo marcará `negative: true` si CVAT no deja ningún episodio de infracción"*.
Cualquier denominador que los incluya hoy está construido sobre una suposición. **Esta
es la falla que invalidaba mi primera recomendación.**

**(2) Ningún denominador alcanzable sostiene una afirmación.** Con 0 FP y la regla de 3
(umbrales **ilustrativos** — el proyecto no pre-registró un objetivo de FAR; el punto
es que ninguna cota alcanzable sirve):

| Para poder decir | hacen falta |
|---|---|
| FAR ≤ 10 FA/h | 0,3 h de video en cumplimiento anotado |
| FAR ≤ 5 FA/h | 0,6 h |
| FAR ≤ 2 FA/h | 1,5 h |
| **FAR ≤ 1 FA/h** | **3,0 h** |

El banco tiene entre **0,10 h** (soak pre-registrado) y **0,26 h** (todos los
negativos, *si* resultan negativos; tiempos efectivos descontando 7 s de warm-up por
clip — nadie puede alertar antes de la persistencia). Un sistema asistivo que no puede
descartar 11–30 falsas alarmas por hora **no es defendible como operativo** — o sea que
el número no puede sostener una afirmación positiva en ningún escenario alcanzable.
Reportarlo como métrica de rendimiento sería reportar ruido con dos decimales.

**(3) La enmienda al pre-registro no compra nada.** Pasar de ≤29,8 a ≤11,4 FA/h es
ajustar una cota que sigue siendo inservible, al costo de exponer un cambio de criterio
**después** de ver el material (más débil que la enmienda del doc 04 §8, que se hizo
antes de correr). El fundamento era bueno —la regla "≥5 min" es un proxy de "tiempo
aburrido" y los P5 lo son por definición— pero no se justifica gastar esa exposición
por un número que no cambia ninguna conclusión.

**(4) La pregunta de fondo ya está respondida por otra vía.** G1 da precision 0,892 y
**0 FP en los negativos**; D1 y H1, que rompen el control de negativos, quedan
descartadas por otros criterios. El riesgo que el gate G1 quería cubrir —"precision alta
falsa por falta de tiempo aburrido"— se mitiga declarando la composición del banco, que
es lo que L5 ya obliga a hacer.

#### Corrección al doc 57 (es un supuesto mío/del doc, no un pendiente del usuario)

El doc 57 estima el material soak en **"≈0 anotación; mayor retorno del banco"**. Es
**falso en la práctica**: un soak de obra en cumplimiento tiene gente en cuadro, y
certificar que *nadie* viola durante 6 minutos exige trackear a todos frame a frame —
no hay atajo dentro del pipeline actual. El `--allow-empty` de `derive_clip_gt` existe
para el caso contrario (clip **sin personas**), no para éste. Medido en la práctica:
el clip de 6 min lleva más de una jornada de trabajo.

*Trabajo futuro anotado (no para esta tesis):* un modo "negativo atestiguado" —revisión
humana con protocolo documentado, sin cajas— volvería barato el soak. El sesgo es
conservador (una violación no vista infla FAR), pero es una vía de GT nueva que no se
abre a 8 semanas de la defensa.

#### Lo que sí sigue

**El clip de 6 min se termina** (decisión del usuario): es el único que califica bajo el
criterio pre-registrado y es el ancla del único denominador temporal del banco.

### D-90.2 — Pedir el commit de la segunda tanda (trámite, pero es tuyo por regla)

Sin commitear: docs 87/88/89 + evidencia, `merge_dual_run` (+11 tests),
`tools/track_detections` (+8 tests), 3 pattern sets (hyb_or, bare_head, v2_subject),
results H1/B1/G1. Suites verdes (control-plane 293 / datasets 283). La regla vigente es
que Claude solo commitea a pedido explícito de ese turno.
**Recomendación:** pedirlo ya — es el trabajo que sostiene los docs 87–89.

---

## ESTA SEMANA — definen el relato del informe

### ~~D-90.3 — Estatus de G1~~ → **RESUELTA 2026-08-04 implementando una cuarta opción**

**Instrucción del usuario que reencuadró la decisión:** *"los docs de desarrollo no son
la fuente de la verdad; lo que podamos implementar y concluir es lo que va a
desarrollarse en los informes"*. Con ese criterio, la pregunta dejó de ser "¿qué
permite ADR-002?" y pasó a ser "¿qué capacidad podemos sostener?".

**Hallazgo del análisis crítico:** las tres opciones que yo había planteado partían de
un falso dilema (dejar G1 como script post-hoc **o** portar el tracker al media-plane,
1–2 días tocando el pipeline congelado). Existía una cuarta: **implementar la identidad
como decorador de FUENTE en el control-plane**. Decora cualquier `MediaEventSource`, así
que sirve para **DBE y EBE/live** por igual y **el port al media-plane deja de ser
necesario para tener G1**.

**Ejecutado (~2 h, TDD):**
- `sources/tracking.py` — `TrackingSource`, un tracker **por `source_id`** (con dos
  cámaras, uno solo cruzaría identidades entre fuentes), streaming en orden de llegada,
  transparente a los items de error.
- `input.track_persons` — opt-in, default `false`: **ninguna corrida ni config
  existente cambia de comportamiento**.
- Cableado en los dos runtimes (`replay.py` DBE y `live.py` EBE).
- **12 tests nuevos**; suite del control-plane **305 passed**.

**Verificación que valida el reporte:** el camino config-driven **reproduce la campaña
G1 exacto en los 34 clips**, comparando **11 campos por clip** (matched/missed/FP,
re_alerts, precision/recall/F1, t_alert, **SDR y TTFD incluidos**). O sea que el
**0,930 no es "un script que corrí": es lo que hace la plataforma configurada por
YAML**, verificado campo por campo sobre el banco completo.

**La re-revisión crítica (pedida por el usuario) atrapó y corrigió 2 bugs reales antes
de que llegaran a ningún reporte:**
1. **El decorador silenciaba el ciclo de vida del bus en live.** La base de fuentes
   define no-ops para `close`/`request_stop`/`dropped_events`; sin delegación
   explícita, `TrackingSource` en EBE **silenciaba `bus_dropped_events`** (violación
   de ADR-003: los drops nunca se silencian), no cerraba el socket y anulaba la
   parada cooperativa — cuya alternativa es la trampa SIGABRT. El camino DBE
   verificado no estaba afectado, pero la afirmación "sirve para live" era falsa tal
   como estaba. Fix con TDD (+4 tests, incluido el aviso por frames hacia atrás:
   el decorador no puede ordenar como hace la herramienta post-hoc).
2. **Colisión de directorios de run con resolución de segundos** (trampa de plataforma
   nueva, atrapada al correr la verificación a ritmo CPU): dos corridas del mismo
   nombre dentro del mismo segundo escribían en el **mismo directorio** y la segunda
   pisaba los artefactos de la primera en silencio. Los runners de campaña lo
   esquivaban por accidente (clip_id en el nombre). Fix en `prepare_run` (sufijo
   de desambiguación para ids autogenerados; un `run.id` explícito conserva su
   contrato) + test. **Las campañas ya corridas NO están afectadas** (verificado:
   nombres únicos por clip en los runners 81/85/87/88/89).

Suite del control-plane tras la revisión: **310 passed**, ruff limpio.

**Cómo se reporta entonces:** G1 es una **capacidad operativa de la plataforma en ambos
caminos**, medida sobre el banco completo. Se mantiene sin tocar lo que ADR-002 excluyó
(sin métricas MOT, sin GT de identidades; métricas del informe a nivel
escena-condición) y se declara el límite vigente: banco **guionado** con multitudes
acotadas (L4), robustez del tracker en obra real no medida.

~~**Residuo declarado:** falta un humo EBE real con `track_persons: true`~~ →
**CERRADO 2026-08-05 con hardware real (doc 91).** Dos humos en vivo con la OAK-D, ambos
verdes: **(A)** regresión del camino live tras todos los cambios de la jornada (150
unidades, 0 errores, `bus_dropped_events=0`, 2 alertas reales) y **(B)** G1 en vivo, con
la evidencia exacta en el contraste de claves de estado — `CR-01:smoke_ebe` bajo escena
vs **`CR-01:smoke_ebe:subject_001`** bajo sujeto, y **sin `no_track_id`** en las causas
de degradación (si apareciera, habría medido G0 creyendo medir G1). La afirmación
"cubre DBE y EBE/live por igual" de la adenda de ADR-002 ya no depende solo de tests
unitarios.

**Lo único que queda para vos:** ratificar la **adenda de ADR-002**
(`decisiones/adr-002-…md`), que registra los dos desvíos respecto del plan original
—tracker en el control-plane en vez del media-plane; 34 clips en vez de 2–3— y deja
la deuda del spec 42 §3 abierta pero **ya no bloqueante**. Ese ADR tiene
`Decisor: usuario`, por eso la adenda está marcada como pendiente de ratificación.

### ~~D-90.4~~ → **ACEPTADA 2026-08-05, con un fundamento más fuerte del que tenía**

Al cerrarla se verificó cómo el evaluador deriva la ventana de matching y el argumento
cambió de categoría. El borde inferior es **`persistencia_min_ms` con
`origin: gt_provenance`** — la persistencia **nominal** con la que `derive_clip_gt`
construyó los episodios — y el evaluador **no sabe** que `hyb_and` acorta la ventana en
runtime. Con `corroboration_factor: 0.5` el motor confirmaría a `onset+2s` cuando la
ventana abre en `onset+4s`: doble castigo por construcción, y **cuanto mejor funcione la
corroboración, peor puntúa**. Medirla de verdad exigiría regenerar el GT o hacer al
evaluador corroboration-aware, y **las dos cosas rompen la comparabilidad** con las 6
campañas ya corridas.

O sea: no es "no da el tiempo", es que **el experimento pre-registrado no es medible
contra este banco sin invalidar el resto de la serie**. Queda como trabajo futuro con
su predicción **y su condición de medición** escritas (doc 87 §5).

#### (planteo original, conservado)

Quedó sin implementar con predicción registrada (doc 87 §5): su único efecto es
*acelerar* la confirmación, y F-87.2 mostró que adelantar es el modo de falla de este
banco. El pre-registro permite esa salida (§6.2) — pero ADR-001 decía "las fusiones se
corren siempre", así que confirmarla es tuyo.

- **(a) Aceptar**: queda como trabajo futuro con predicción falsable escrita.
- (b) Implementarla igual (1–2 días de motor) para completitud del pre-registro.

**Recomendación: (a).** Implementarla compra un número ya anticipado al precio del
único bloque de motor que queda caro.

### ~~D-90.5~~ → **EJECUTADA 2026-08-05: el reporte de cierre existe (doc 92)**

El usuario delegó la decisión ("decidí cómo continuar") y la recomendación era
arrancar ya. **`operacion/92-cierre-tramo-experimental.md`** ejecuta el doc 62 §8:
Q1–Q4 respondidas con sus n, la matriz SDR×recall llena (las cuatro celdas pobladas,
con la lectura transversal "recall bajo + SDR alto nunca es percepción, es timing"),
las 5 declaraciones de Etapa 4 actualizadas a lo que efectivamente pasó, cobertura
como resultado y limitaciones consolidadas. Lo que queda es redacción hacia las
secciones §17.x del informe — más el lote de internet cuando salga de CVAT (se
integra como sección incremental, no bloquea).

#### (planteo original, conservado)

El material del eje está completo: 6 campañas comparables, 3 estrategias decididas por
criterios pre-registrados, fallas explicadas por mecanismo, tablas listas en
`results/clip_bench/index.md` y `results/bench_nivel_a/index.md`. El lote de internet
**no bloquea** el capítulo del eje (aporta L1/L4, que se integran aparte).

- **(a) Empezar ya** el análisis de errores + reporte de cierre (doc 62 §8): matriz
  SDR×recall, las 5 declaraciones de Etapa 4, Q1–Q4 con sus n.
- (b) Esperar el lote de internet para escribir todo junto.

**Recomendación: (a).** Quedan ~8 semanas y la escritura siempre descubre huecos que
conviene encontrar con margen. El lote llega como sección incremental.
**Desbloquea:** el capítulo de resultados de la tesis.

---

## CUANDO LLEGUE EL MATERIAL

### D-90.6 — Lote de internet: tu parte es cerrar CVAT; después decidís cómo entra

Cuando el GT esté: la campaña la corro yo (misma cadena, un comando). La decisión tuya
es de encuadre: ¿los v-clips entran al banco como **estrato B** (guionado + no guionado
en una tabla, separados por estrato como bench_v3) o se reportan como **banco aparte**?
**Recomendación:** estrato B con desglose obligatorio — es la misma regla L5/bench_v3
que ya usás.

---

## COLA FIJA — tuyas, sin dependencia técnica (del doc 82, siguen pendientes)

### ~~D-90.7~~ → **RESUELTA 2026-08-05 por delegación del usuario** ("respondelas vos de acuerdo a lo que mejor se alinea a la tesis")

**Principio rector de la resolución (doc 81 §1): los videos ilustran combinaciones
MEDIDAS, no montajes ideales.** Cada video muestra exactamente la combinación cuyos
números están en las tablas del informe — así ningún jurado puede preguntar "¿y esto
que estoy viendo, dónde está medido?".

1. **V1–V3: UNA persona, granularidad de ESCENA, sin identidad visible.** Son la
   ilustración del núcleo medido (T1: `gdino-tiny-560` + `v2_short` + escena,
   F1 0,789): P1 para V1 (la cadena completa), P3 para V3 (el silencio correcto,
   verificado 2/2 en vivo — doc 71). Menos capas sobreimpresas = el mensaje temporal
   se lee mejor; y evita consumir `supporting_*`, la mitad cara del renderer.
2. **Identidad visible: SÍ, pero en una pieza propia (V-G1, ~20 s), no en V1–V3.**
   El mejor resultado del banco (G1, F1 0,930) merece su evidencia visual, y el lugar
   donde el mecanismo SE VE es P7 (multitud): bajo escena el motor "miraba a otra
   persona" (F-89.1, recall 0,400) y bajo sujeto las mismas detecciones bit a bit dan
   1,000. V-G1 es el único video con N>1 y con color/ID por sujeto — ahí la identidad
   ES el mensaje, en V1–V3 sería ruido. (Doc 09 §6.2 preveía "3 esenciales + 1 bonus";
   V-G1 se agrega como segundo bonus porque G1 se midió DESPUÉS de escribir ese doc.)
3. ~~¿G1 capacidad ejecutable o diseño?~~ — **cerrada del todo**: capacidad operativa
   config-driven verificada en DBE (34/34 campo a campo) y en vivo (doc 91).

**V2 (open-vocabulary) sigue PENDIENTE y su clase la decide el usuario.** El intento
de Claude con `gloves` (iniciativa propia, fuera de lo delegado) se **descartó por
falso**: auditadas las 252 detecciones, las de mayor confianza caen sobre el **casco
amarillo** y el resto sobre manga/cabeza/chaleco/piso — cero guantes (evidencia:
corrida `run_20260805_180847…9357a7`; detalle en
`experimental-setup/defensa/README.md` §V2). Es un **segundo caso independiente de
F-94.1** y como tal es citable en el informe. **Requisito que queda fijado: auditar
visualmente la clase nueva antes de renderizar o de afirmar nada — un conteo de
detecciones no es evidencia de que funcione.**

### D-90.8 — Administrativo del rodaje
Consentimientos archivados (pendiente desde doc 82 item 5).

### D-90.9 — Backup de `docs` a otro disco
`git bundle` (sin remote por decisión). Hoy hay 7 docs nuevos y ~90 commits solo en
este disco.

### D-90.10 — Llevar `main` al estado que se defiende
Los 4 repos con remote están pusheados pero en ramas `feature/*`; `main` sigue atrás
(señalado ya en doc 75 §3.1). La receta es la del doc 77 (merge + push por repo,
la ejecutás vos o la pedís).

---

## Resumen en una línea por decisión

| # | Decisión | Recomendación | Urgencia |
|---|---|---|---|
| ~~D-90.1~~ | ~~Soak extra~~ | **RESUELTA: FAR/hora = limitación declarada, no métrica. El control de negativos es la evidencia de FP** | cerrada 08-04 |
| ~~D-90.2~~ | ~~Commit de la tanda~~ | **EJECUTADO 2026-08-05: el gate (cerrar las decisiones que tocan archivos) se cumplió con D-90.4 + la ratificación de ADR-002** | cerrada 08-05 |
| ~~D-90.3~~ | ~~Estatus de G1~~ | **RESUELTA implementando: identidad como decorador de fuente en el control-plane (DBE+live, opt-in). Verificada EN VIVO (doc 91). Queda ratificar la adenda de ADR-002** | cerrada 08-04/05 |
| ~~D-90.5~~ | ~~Arrancar el informe~~ | **EJECUTADA: doc 92 = reporte de cierre (Q1–Q4 con n, matriz SDR×recall, 5 declaraciones, cobertura)** | cerrada 08-05 |
| ~~D-90.4~~ | ~~`hyb_and`~~ | **ACEPTADA: no es falta de tiempo — no es medible contra este banco sin romper la comparabilidad de las 6 campañas** | cerrada 08-05 |
| D-90.5 | Arrancar el informe | **sí, ya** | esta semana |
| D-90.6 | Encuadre del lote de internet | estrato B con desglose | al llegar el GT |
| ~~D-90.7~~ | ~~Alcance videos V1–V3~~ | **RESUELTA por delegación: V1–V3 = 1 persona/escena/sin identidad (ilustran T1); + V-G1 (P7, multitud, color por sujeto — ilustra G1). 4 videos listos; V2 pendiente: el intento con `gloves` se descartó por falso** | cerrada 08-05 (V2 abierto) |
| D-90.8 | Consentimientos | — | cola |
| D-90.9 | Backup `docs` | git bundle | cola (creciente) |
| D-90.10 | Merge a `main` | receta doc 77 | antes del cierre |
