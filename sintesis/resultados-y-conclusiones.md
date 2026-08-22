# Síntesis de resultados y conclusiones — E-OVRT-VDP

> ## ✎ ESTADO AL 2026-08-09 — el cuerpo está AL DÍA
>
> Este documento se escribió el **08-06**, cuando el estrato B eran **3 clips**. El
> tramo de video **se cerró** desde entonces: lote **13/14 con GT** (banco **47**, doc
> `operacion/111`), campañas **re-corridas en gen. 3**, balance con lectura crítica
> (`operacion/112`) y revisión de ese balance (`operacion/113`, que ejecutó las
> correcciones documentales y lista lo que falta).
>
> **✎ 08-09, noche — el estrato B ya está INTEGRADO AL CUERPO**, no solo a este banner:
> **§4.1** (Nivel A sobre video) y **§5.1** (Nivel B sobre obra real no guionada y la
> frontera de juzgabilidad) son secciones nuevas con las cifras vigentes. Este banner
> queda como resumen de qué cambió y por qué; **ya no hay que leer el cuerpo "con la
> fecha del 08-06 en mente"**.
>
> **Cifras vigentes del estrato B (tras la revisión CIEGA del GT, doc 113 §B, 08-09
> noche):** Nivel B `scene` F1 **0,333** / `subject` **0,190** sobre **2 episodios
> evaluables**; Nivel A sobre 17 clips de video CR-01 **0,031** / CR-02 **0,018**; y
> **FAR/hora computable por primera vez** — 29,2 y 1.850,8, que son **3 y 190 FP en
> 6:09,6 del único clip soak**. La asimetría de FP entre granularidades es lo robusto:
> 26 vs 323 sobre 11 negativos (12×).
>
> **El resultado más fuerte de la revisión ciega: 5 de las 7 declaraciones de episodio
> que produjo el lote eran errores de anotación (~71%)** — v06_c01, v03_c02, v04_c02×2
> y v01_c01, TODAS sobre-declarando violación donde el estado no era observable (cabina
> de máquina, contraluz, borde del plano). Es la frontera de juzgabilidad medida
> también en el anotador, y convierte la calidad del GT en un resultado auditado: los
> 2 episodios que sobreviven están verificados a ciegas con evidencia de frame.
>
> **Cuatro cosas del cuerpo que ya no son ciertas:** (1) `v06_c01` **sí es negativo** —su
> episodio CR-02 era error de anotación (doc 108 §6)— y es **el clip soak del banco**,
> así que **L1 se precisa** en vez de quedar igual; (2) su escenario **P5 era correcto**,
> el error estaba en la anotación y no en la curación — y lo mismo terminó valiendo para
> `v04_c02` y `v01_c01`; (3) "ninguna lectura de cuál gana es válida" **sigue siendo
> cierto**, hoy con más fuerza: `n` = **2 episodios** — F-111.1 quedó enmendado; (4)
> `v04_c02` ya NO es "el único caso limpio del estrato": sus 2 episodios eran error y el
> clip es negativo (banner del doc 108).
>
> **§4.1, §5.1 y §11 son posteriores a la revisión ciega y mandan sobre cualquier cifra
> de estrato B anterior al 08-09.** El resto del cuerpo (imágenes, rodaje, tiempo real)
> no se vio afectado por la revisión: esas mediciones son del Bloque A y no cambiaron.

- **Fecha:** 2026-08-06 · **Estado del proyecto:** tramo experimental **COMPLETO**
  sobre el banco del rodaje; ✎ mismo día, más tarde: **llegaron las anotaciones CVAT
  del lote de internet, el GT del estrato B se derivó y promovió (banco 34→37, doc
  `operacion/102`), y las dos campañas I1/I2 CORRIERON.** El resultado no es una fila
  más: `v06_c01` (127 personas GT, el clip más denso del banco) rompió el mecanismo de
  las dos formas que la teoría del rodaje predecía en miniatura — `scene` recall
  0,000 (F-81.2(a) llevado al extremo: evidencia perpetua por multitud) vs `subject`
  recall 1,000 pero precision 0,010 (el tracker fragmenta identidades en escenas
  densas: 182 identidades con FP, más que las 127 personas reales). Detalle completo
  y por qué ninguna lectura de "cuál gana" es válida con n=1 clip así: `operacion/103`.
  **Mismo día, después:** los ajustes probados solo con configuración (`operacion/104`
  — el gate `min_subject_area_px` YA EXISTÍA en 400 px², recalibrado FP −32% con recall
  intacto; `base-560` REFUTADO, no transfiere a sujetos chicos) y la recuperación de
  los 4 clips piloto desde CVAT con **Nivel A sobre video** (`operacion/105` — el
  derrumbe confirmado con la métrica canónica; la juzgabilidad tiene TRES ejes: escala ×
  iluminación × oclusión; y la brecha humano/modelo es el contexto temporal, F-105.4).
  *(✎ las cifras de Nivel A sobre video de ese doc —CR-02 F1 0,154 piloto / 0,002
  estrato B— son de la gen. 2 y quedaron **supersedidas**; las vigentes, re-puntuadas
  el 08-09 sobre los 17 clips, son **CR-01 0,031 / CR-02 0,018** contra 0,408/0,479 en
  imágenes: `results/bench_nivel_a/`.)*
  **✎ 08-07/09:** artefactos reorganizados con fuente única (`operacion/109`),
  `v03_c02` integrado tras corrección a `unknown` (`operacion/110`) y **el lote de
  internet CERRADO: 13 de 14 con GT, banco 47 clips** (`operacion/111` — `v08_c01`
  excluido con causa; anotaciones del repo = fuente de verdad, guard `--check`).
  **✎ 08-09: las campañas gen. 3 CORRIERON** sobre los 13 clips, y después vino la
  **revisión ciega del GT** (`operacion/113` §B) que tiró 3 de los 5 episodios del
  estrato y obligó a re-derivar y re-evaluar. El banco quedó en **47 clips = 32
  positivos / 15 negativos / 37 episodios** (manifest `3f14f50a…`) y las cifras
  vigentes del estrato B son las del banner de arriba — **ninguna cifra de estrato B
  anterior al 08-09 sigue en pie**.
- **Qué es:** el "pasado en limpio" de todo lo medido y concluido, con el camino
  experimental que respalda cada número. Nace del **relevamiento integral de
  consistencia del 2026-08-06** (5 auditorías paralelas sobre conclusiones, redlines,
  kit de informe, alcance/ADRs e índices de resultados; los desfases encontrados se
  corrigieron en sus docs — ver §10).
- **Qué NO es:** una fuente primaria. **Ante cualquier conflicto mandan los 4 índices
  de `e-ovrt_experimental-setup/results/`** (verificados mecánicamente con
  `docs/operacion/datos/96-verificar-indices.py` — última corrida 2026-08-06, todo
  verde) y los docs de procedencia. Toda cifra de esta página fue relevada contra esos
  índices en la fecha de arriba.

---

## 1. La pregunta del trabajo, y la respuesta en una línea

> *¿Qué rendimiento se obtiene hoy, en construcción civil, con detección
> open-vocabulary **sin entrenar**, expresando las condiciones de riesgo en lenguaje —
> y qué aporta la plataforma alrededor del modelo?*

**Respuesta corta (doc `operacion/98` §1):** la detección zero-shot alcanza para
sostener una condición de riesgo (CR-01, sin casco) y no alcanza para la otra (CR-02,
sin chaleco), pero **la plataforma alrededor del modelo cambia el resultado más que
cualquier elección de modelo o de prompt** — y esa ganancia sobrevive a la restricción
del tiempo real.

**La cifra que lo condensa:** sobre el mismo banco, con **las mismas detecciones bit a
bit**, cambiar la granularidad del motor de escena a sujeto lleva el F1 de alertas de
**0,789 a 0,930**. Ninguna de las cuatro palancas de percepción o formulación probadas
(modelo, prompts, fusión, vocabulario nativo) se acercó.

**Marco de lectura (doc 81 §1, no negociable):** cada número es el rendimiento medido
de UNA combinación, no una nota de aprobación. El contraste entre filas ES el
experimento.

## 2. El recorrido del argumento, en cuatro números

1. **Qué ve el detector sin entrenar** — `gdino-tiny-560`, mAP50 **0,551** sobre 6.477
   imágenes de 3 fuentes independientes (robusto a la fuente). → §3
2. **Cómo conviene expresar la condición** — E-IND (evidencia positiva + inferencia)
   gana a E-DIR (prompts de ausencia) en los dos niveles; a Nivel B el **veto
   pre-registrado de precisión (0,146 < 0,5)** descarta a E-DIR como núcleo. → §4–5
3. **Qué agrega la plataforma sobre la detección cruda** — la histéresis rescata
   percepción intermitente (CR-02 recall 1,000 con SDR 0,281) y **la capa que más
   agrega es la identidad**: F1 0,789 → **0,930** con detecciones idénticas. → §5
4. **Qué sobrevive al tiempo real** — la ganancia de la identidad **excluye el cero en
   las cuatro densidades medidas** (bajo decimado regular; conserva la dirección bajo
   el descarte irregular medido del live, 6/6 — doc 101). → §6

## 3. Percepción sobre imágenes — selección de modelos y extensibilidad

**Banco:** `bench_v3`, congelado 2026-07-23 — **6.477 imágenes / 55.165 anotaciones,
3 estratos independientes**: `bench_obra` (147, núcleo curado y spot-checkeado), `chv`
(1.330, mejor AP de `vest`), `shel5k` (5.000, `bare_head` nativo). El agregado está
dominado por `shel5k` (77%) ⇒ **reportar siempre por estrato** (limitación L5). El
BENCH original de 196 imgs quedó como histórico (~20–25% fuera de dominio, doc 63).
Freeze verificable por sha256 (`4557024e…`).

**Camino experimental:** Fase S del plan maestro (doc 62) — S1/S2 sobre el núcleo
curado (docs 61/64) + confirmación B5 sobre `bench_v3` completo (doc 66).

| Modelo | mAP50 `bench_v3` (6.477) | mAP50 `bench_obra` (147) | recall CR-01 (n=5.313) |
|---|---|---|---|
| **`gdino-tiny-560`** (campeón) | **0,551** | **0,503** | 0,308 |
| `gdino-base-560` (especialista) | 0,525 | 0,474 | **0,599** |
| `yoloe-26x` | 0,442 | 0,405 | 0,000 |

- **Campeón `gdino-tiny-560`**: gana mAP50 en las dos escalas — robusto a la fuente.
  La resolución 560 da −24% de latencia batch con igual o mejor mAP que 800 (doc 61;
  no es medición live).
- **`gdino-base-560` es el especialista en dos ejes**: `bare_head` (evidencia de
  CR-01: recall 0,599 vs 0,308) y `vest`/CR-02 (AP 0,582 vs 0,520; en video, SDR
  CR-02 0,281→0,920). Candidato secundario cuando el foco sea esa condición.
- **La asimetría es estructural**: `person`/`helmet` sólidas (0,70–0,89 por estrato),
  `vest` débil (0,55–0,58), `bare_head` fuerte solo en el especialista (0,399 vs
  0,133 en `shel5k`). YOLOE es rápida (43 ms) pero ciega a `bare_head` (AP 0,000 en
  las cuatro variantes) ⇒ inservible para CR-01.

**Extensibilidad — el costo de una clase nueva, medido (A1, doc 94 → AF-4):**
**0 entrenamientos · 1 archivo de 48 líneas · 9 minutos · 0 GT nuevo anotado**, y
`machinery` (jamás configurada) da **AP@0.5 0,662 zero-shot** (n=99 cajas) — por
encima del agregado del campeón con las clases configuradas. **Contrapeso obligatorio
F-94.1:** la palabra tiene que alinear con la taxonomía (`vehicle` junto a `machinery`
= 0 detecciones; `gloves` = 252 detecciones y ninguna sobre un guante) — agregar la
clase cuesta minutos **y validar la palabra también** (el bench lo expone en ~3 min).

## 4. Nivel A — el estado "sin EPP" por persona (E-DIR vs E-IND)

**Camino experimental:** campaña D1 `d1_gdinotiny560_edir_vs_eind` (doc 83), con
prompt sets congelados por acta del usuario (2026-07-29, doc 76, sha256), umbrales
calibrados en mitad A y métricas solo sobre mitad B (anti-leakage), matching IoU≥0,5.

| Corte | E-IND F1 | mejor E-DIR | ratio E-DIR/E-IND |
|---|---|---|---|
| CR-01 `shel5k` (n+=2.487) | **0,546** | 0,188 (`obs`) | 0,34 (IC no solapados) |
| CR-01 `bench_obra` (n+=28) | **0,408** | 0,189 (`spec`) | 0,46 |
| CR-02 `bench_obra` (n+=82) | **0,479** | 0,418 (`obs`) | 0,87 |

- El **gate pre-registrado** (`nucleo/04` §8) exigía ambas condiciones <50% y **no se
  disparó** (0,87 en chaleco) ⇒ E-DIR pasó a Fase 2 (Nivel B), donde la decidió el
  veto de precisión (§5).
- **F-83.6 — E-DIR no es detector, es recuperador:** con F1 0,188 y 8.212 FP igual
  recupera el **18,5%** de lo que E-IND no ve (155/840 en `shel5k`). Su costo es
  precision, no recall.
- **F-83.4/83.5:** la formulación mueve el rendimiento y el eje ganador cambia con la
  condición; la negación sintáctica pura es siempre la más débil.
- **F-83.7 (versión corregida 2026-08-04):** la corroboración discrimina **en CR-01**
  (2,4×; réplica con `base-560`: 3,0×). En CR-02 no hay evidencia concluyente.
- **Limitación L8:** CR-02 a Nivel A **no está cerrado** (un solo estrato, n+=82, IC
  solapados). Declarado, no disimulado.

### 4.1 El mismo Nivel A, sobre VIDEO — el derrumbe, y de qué está hecho

**Camino experimental:** campaña `na1_gdinotiny560_v2short_video` (docs 105/111),
**17 clips** (13 del lote de internet + 4 del piloto), re-puntuada el 2026-08-09 tras la
revisión ciega del GT. Es la MISMA métrica de arriba —estado por persona, sin motor
temporal— aplicada a obra real en movimiento.

| Condición | Precision | Recall | **F1** | vs imágenes (`bench_obra`) |
|---|---|---|---|---|
| CR-01 (n+ = 92 de 10.356 person-frames) | 0,016 | 0,467 | **0,031** | 0,408 |
| CR-02 (n+ = 170 de 10.361 person-frames) | 0,009 | 0,318 | **0,018** | 0,479 |

- **El derrumbe es de PRECISION, no de recall.** El recall se sostiene en un rango
  reconocible (0,47 / 0,32); lo que se hunde es la precisión, dos órdenes de magnitud.
  El sistema **sigue viendo** lo que tiene que ver: lo que no puede es dejar de afirmar
  sobre personas cuyo estado no es determinable.
- **Regla declarada del scorer (D-113.2):** las person-frames que el anotador marcó
  `unknown` **salen del denominador** (1.414 y 1.409 excluidas), pero la predicción del
  modelo sobre esa persona **sí cuenta como FP** — "la alerta suena igual". Es una
  decisión firmada, no un artefacto: inflar el denominador con lo no juzgable sería
  premiar al sistema por acertar donde nadie puede verificar.
- **Mecanismo, no anécdota:** esto es la **frontera de juzgabilidad** (§5.1) medida sin
  motor temporal — el mismo fenómeno que a Nivel B, aislado de la histéresis y de la
  identidad. Por eso las dos capas se leen juntas.

## 5. Nivel B — alertas contra GT temporal humano (el resultado principal)

**Banco:** 34 clips del rodaje (2026-07-25), **35 episodios (28 CR-01 / 7 CR-02), 34
evaluables** (1 censurado con causa — denominador citable: **"34 evaluables sobre
35"**). GT **humano en CVAT, `gt_ready` desde 2026-08-03** (doc 80) ⇒ estas métricas
se reportan como **RESULTADO** de la tesis. Escenarios P1–P9; los 4 clips negativos
quedan fuera de P/R/F1 y son el **control de falsas alarmas** (F-EV1).

**Camino experimental:** GT (doc 80) → línea de base y fixes del evaluador (doc 81) →
campañas de combinación T2/D1/H1/B1/G1 (docs 84/85/87/88/89) → cierre (doc 92) →
conclusiones (doc 98). Seis campañas, mismo banco/GT/motor, variable única por fila:

| # | Combinación | Recall | Prec. | **F1** | t_alert | SDR | FP neg |
|---|---|---|---|---|---|---|---|
| **T1** | tiny-560 + `v2_short` + escena (**núcleo E-IND**) | 0,824 | 0,757 | **0,789** | 5.327 ms | 0,698 | 0/4 |
| T2 | base-560 (contraste de modelo) | 0,735 | 0,676 | 0,704 | 4.899 ms | 0,819 | 0/4 |
| D1 | `edir_v1` (E-DIR de punta a punta) | 0,176 | **0,146** | 0,160 | 6.611 ms | 0,210 | 2/4 |
| H1 | fusión `hyb_or` | 0,353 | 0,255 | 0,296 | 6.956 ms | 0,738 | 2/4 |
| **G1** | T1 + granularidad **por sujeto** | **0,971** | **0,892** | **0,930** | 5.236 ms | 0,698 | 0/4 |
| B1 | base-560 + `bare_head` directo | 0,382 | 0,371 | 0,377 | 3.919 ms | 0,940 | 3/4 |

**Veredicto del eje D1 (pre-registrado en `nucleo/04` §8):** E-IND **0,789 = núcleo**
· E-DIR 0,160, **descartada por veto de precisión (0,146 < 0,5)** · E-HYB-or 0,296,
**predicción refutada** (el recall se derrumba 0,824→0,353; **F-87.2**: la unión de
evidencia NO es monótona en un motor temporal — evidencia más temprana corre las
alertas fuera de su ventana) · **`hyb_and` no ejecutada con causa** (D-90.4: no
medible contra este banco sin romper la comparabilidad de las 6 campañas). Las tres
fallas están **explicadas por mecanismo**, no solo cuantificadas. La brecha E-DIR se
**agranda** al pasar por la plataforma (ratio 0,20 a Nivel B vs 0,34–0,46 a Nivel A).

**Los dos aportes medidos de la plataforma:**

- **La histéresis rescata percepción intermitente (F-81.1):** en T1, CR-02 confirma
  **7/7 = recall 1,000 con SDR 0,281** (evidencia en ~1 de cada 6 frames), pagando
  t_alert (8.572 vs 4.314 ms de CR-01). Es palanca de doble filo (F-85.3: en D1
  también amplifica los FP) y tiene límite de cadencia (F-96.2, §6).
- **La identidad es la capa que más agrega (F-89.1/89.2):** G1 usa **las mismas
  detecciones bit a bit** que T1 (SDR y TTFD idénticos) ⇒ los **+0,141 de F1 vienen
  100% del motor**, cero de percepción. P7 pasa de 0,400 a 1,000; prematuras de
  pre-roll 5→1. Corre sin GPU (0,4 min) y el camino config-driven la reproduce exacto.
  Por eso E-10 (métricas MOT) sigue "no aplicable" con fundamento **medido**: la
  ganancia se expresa en alertas, no en MOTA/IDF1.

Sobre el sub-banco CR-01 puro (23 clips / 25 episodios): T1 0,731 · T2 0,615 ·
B1-eind 0,582 · B1 `bare_head` directo 0,480 (**F-88.2**: la vía del vocabulario
nativo tampoco alcanza, sobre las mismas detecciones) · D1 0,231. **F-88.1**: una
clase más en el caption cuesta 0,082 de F1 (costo medido del caption). **F-88.3**: lo
que ordena el eje es la formulación (etiqueta corta > frase negada), no el mecanismo.

### 5.1 Estrato B — obra real NO guionada, y la frontera de juzgabilidad

Todo lo de arriba es el **rodaje guionado**. El lote de internet es el contraste que
faltaba: **13 clips de obra real** (uno de 14 excluido con causa), GT humano, la misma
combinación intacta — la única variable es el material. Se reporta como **fila aparte,
nunca fusionado al agregado del rodaje** (D-90.6). Banco resultante: **47 clips = 32
positivos / 15 negativos / 37 episodios**.

**Antes de las cifras, el resultado que las condiciona.** Una **revisión ciega** de los
episodios del estrato (doc 113 §B) encontró que **5 de las 7 declaraciones de episodio
que el lote produjo eran errores de anotación** (~71%), **todas sobre-declarando donde
el estado no era observable**: el ex "caso limpio" `v04_c02` tenía a su único sujeto
dentro de la cabina de una máquina, y `v01_c01` estaba a contraluz. **La calidad del GT
es acá un resultado en sí, no un detalle de método**: la misma frontera que derrota al
modelo derrota al anotador humano. Quedan **2 episodios evaluables**.

| | I1 `scene` | I2 `subject` |
|---|---|---|
| recall (2 episodios) | 0,500 | **1,000** |
| precision | **0,250** | 0,105 |
| **F1** | **0,333** | 0,190 |
| FP sobre los 11 negativos | **26** | **323** |

- **La ganancia de la identidad NO se reproduce en este régimen.** G1 fue la mejor
  combinación del banco del rodaje (+0,141 de F1); acá `subject` compra el episodio que
  `scene` pierde (recall 0,500 → 1,000) pagando **un orden de magnitud más FP**: ~6× en
  positivos y **12× en los negativos** (323 vs 26). **F-108.1: no hay una granularidad
  mejor, hay una correcta para cada régimen de densidad.** El mecanismo es el de L6 —
  el tracker fragmenta identidades en escena densa (182 identidades con FP contra 127
  personas reales en `v06_c01`).
- **Con n = 2, ningún ranking por F1 sale de acá** (F-111.1, enmendado). Lo robusto es
  la **asimetría de FP**, que son conteos grandes y sobrevivió intacta a la corrección
  del GT. Quien cite "0,333 le gana a 0,190" está leyendo ruido.
- **Falsas alarmas, dicho con el denominador a la vista:** el clip soak `v06_c01`
  (6:09,6 de obra real donde nadie infringe) da **3 FP en `scene` y 190 en `subject`**.
  Las tasas derivadas (29,2 y 1.850,8 FA/hora) **se reportan pero no sostienen una
  cota** — 0,1027 h están a dos órdenes de magnitud de las 3 h que exigiría afirmarla
  (**limitación L1, precisada**). Ninguna configuración probada cruza a operable
  (doc 107).
- **Qué queda entonces, y es lo valioso:** la limitación **L4 se precisó, no se
  levantó** (D-113.1). Hay medición en obra real, y su aporte es **caracterizar por
  mecanismo dónde el sistema deja de ser evaluable** — tres ejes medidos (**escala ×
  iluminación × oclusión**) y una propiedad negativa verificada: **el `unknown` del
  anotador no predice la juzgabilidad** (F-105.2/3/4). No existe un índice escalar
  barato para saber de antemano si el material es juzgable. Eso es un aporte
  metodológico, no un número de rendimiento.

## 6. Tiempo real — qué sobrevive a la restricción del camino live

**Camino experimental:** rodaje EBE (docs 71/73) → diagnóstico del techo (docs 73/74)
→ eje de densidad R1–R6 (doc 96) → blindaje y verificación adversarial (doc 101).

- **Integridad del acople (cerrada):** paridad replay↔stream **byte-idéntica**;
  6 corridas del rodaje con `bus_dropped_events = 0`; corrida 1:1 (ADR-007).
- **Densidad de evidencia (R1–R6, doc 96):** el banco corre a 30 fps de evidencia; el
  live entrega 1,16–4,42 fps. A densidad del techo live (≈4,29 fps): escena 0,794,
  sujeto 0,866. Al peor caso (≈1,15): escena 0,646, sujeto 0,742. **F-96.4 (el
  central): la ganancia de la identidad excluye el cero en las CUATRO densidades**
  (+0,141 / +0,072 / +0,137 / +0,096, bootstrap pareado por clip) — única palanca del
  banco significativa bajo esa restricción. Los deltas del agregado **de escena** no
  excluyen el cero; bajo sujeto el peor caso sí (R6−G1 = −0,188 [−0,334, −0,040]).
  "G1 a 4,29 fps > T1 a 30 fps" es **estimación puntual** (IC [−0,071, +0,229]), se
  reporta como consistente, no como hallazgo.
- **Trampas de instrumento (cazadas antes de reportar):** el **SDR no se compara
  entre cadencias** (F-96.6, ~100% artefacto) y el **t_alert agregado no se compara
  entre densidades sin control de supervivencia** (F-96.5: el costo real entre
  supervivientes es +0,7 a +1,3 s sobre políticas de 4–7 s).
- **Blindaje EBE (doc 101 — EBE CERRADO SIN PENDIENTES, no se re-rueda):** el
  descarte live irregular quedó **medido** (CV 0,22 hoy / 0,36 rodaje) y el eje de
  densidad **verificado por decimado empírico** (12/12 IC jitter−regular cruzan el
  cero; la identidad conserva el signo en 6/6 realizaciones). La claqueta cerró con
  hardware real y reloj externo: política 4.142 ms vs umbral 4.000, residuo de
  relojes 4 ms, **ancla física tono→fotón +1.066 ms**.
- **Latencia (con la advertencia obligatoria F-101.8):** G2A single-host p50
  **14,7 ms** / p95 31,8 (dentro del presupuesto 50–250 ms); live sobre OAK-D:
  GDINO tiny-560 p95 630–890 ms (fuera), YOLOE 225–249 ms (dentro **pero inservible
  para la condición** — F-RT2). **F-101.8: el G2A se mide desde el dequeue, no desde
  el fotón** — vidrio→alerta suma `capture_to_host` (202–217 ms en el rodaje; hasta
  1,6 s degradado), y el informe debe decirlo. `base-560` no tiene latencia live
  medida (declarado).
- **Techo de fps y su causa:** el techo es **contención de GIL** (F-RT3), no térmico
  (la hipótesis térmica del rodaje fue refutada por doc 73: lo que separa las
  poblaciones es la fuente). Palanca aplicada F-RT5: sacar el round-trip PIL del
  productor = **3,75→4,42 fps (+18%), −14,4% latencia, p=0,0195** (rama
  `perf/producer-pil-roundtrip`, merge = decisión del usuario). Prefilter EN-2
  on-device: **87% de descarte** medido A/B, opcional, default off.
- **Patrones en vivo (rodaje + smoke doc 91):** CR-01 7 confirmaciones legítimas
  (4,1–4,6 s sobre umbral de 4,0), CR-02 3 (7,1 s+ sobre 7,0); G1 verificado en vivo
  (`subject_key` por sujeto, 0 dropped). F-RT1: la sobre-marca de `vest` puede
  suprimir CR-02 en silencio (vestuario a franjas).

## 7. El estado del arte como vara — qué dice el informe, qué dice la literatura, y dónde quedan nuestros números (PRELIMINAR)

> **Estatuto de esta sección (2026-08-06):** relevamiento del §15 del informe +
> verificación independiente contra fuentes externas (web, fuentes primarias
> fetcheadas) + contraste con nuestros números actuales. Es **preliminar en los dos
> extremos**: el §15 del informe todavía se va a corregir en el pase de redlines, y
> nuestro agregado puede moverse cuando entre el estrato B (lote de internet). Las
> cifras nuestras salen de `results/`; las externas llevan marca de confianza:
> **[P]** = verificada en fuente primaria, **[S]** = fuente secundaria oficial,
> **[R]** = circulante sin verificar en esta pasada.

### 7.1 Lo que el informe desarrolló (preliminarmente) — y qué le encontró la verificación

El §15 del informe (`informe/96c`) trae un estado del arte OVD extenso: 4 paradigmas
(DETR/DINO con fusión profunda · one-stage YOLO · dual-encoder CLIP-like ·
generativos), ~25 modelos con cifras COCO/LVIS, la Tabla 3 de "OVD para tiempo real"
y la Tabla A.1 de prototipado (`informe/96e`). Los criterios de selección
(§17.1.9.2) fundan el par GDINO+YOLOE como "polos del trade-off expresividad
semántica ↔ latencia de inferencia", con reglas pre-registradas (baseline zero-shot
obligatoria, test congelado, ganancia exigible).

**La verificación externa confirma las cifras ancla** (GDINO 52,5 AP COCO zero-shot
y 26,1 mean AP ODinW [P]; YOLO-World-L 35,4 AP LVIS @ 52 FPS [P]; YOLOE-v8-S/L
27,9/35,9 AP LVIS @ 305,8/102,5 FPS T4-TensorRT [P/S]; GDINO 1.5 Pro 54,3/55,7 y
Edge 36,2 @ 75,2 FPS [S]) — **pero encontró dos huecos estructurales y una lista de
erratas** que el pase de redlines debe atacar:

- **Hueco 1 — no hay línea base de EPP supervisado.** El informe **no reporta ni una
  cifra de mAP** de la literatura de detección de EPP con modelos entrenados
  (SHEL5K/CHV/SH17 se citan solo como datasets). Sin eso, el lector no tiene contra
  qué leer nuestro 0,551 — y toda la defensa pivotea sobre ese contraste.
- **Hueco 2 — el estado del arte y la evidencia propia no se cruzan nunca.** El dato
  más contundente del proyecto (YOLOE con 35,9 AP en LVIS publicado pero **recall
  CR-01 = 0,000** medido acá) no está escrito en §15; ídem el trade-off de latencia,
  que §17.1.9.2 justifica con GPUs ajenas cuando ya existe medido en nuestro hardware
  (G2A live 630–890 ms GDINO vs 225–249 ms YOLOE; keep-up 22% vs 63–69% en Sprint 2).
- **Erratas duras a corregir** (verificables contra los papers): el 52,5 AP de GDINO
  **es del backbone Swin-L y el informe nunca lo declara** — lo desplegado acá es
  Swin-T, cuyo zero-shot COCO publicado es ≈48,4 [S]; OmDet-Turbo-Tiny "30,3 LVIS"
  (probable mislabel de ODinW-13) y 34,0 vs 34,7 entre tablas; LLMDet "51,1–52,4"
  con el 52,4 sin origen; el caching "ahorra ≈40 ms" en un modelo al que la misma
  tabla asigna 7,1 ms totales; la columna Latencia de la Tabla 3 es 1000/FPS
  (derivada, no medida); el 53,4 COCO de OmDet-Turbo probablemente no es zero-shot;
  citas inconsistentes (Liu 2023/2024, Minderer, Xiao, Lin 2014/2015, Ren a/b/c);
  y la Tabla A.1 lista GDINO 1.5/DINO-X como "Apache-2.0" cuando son **API cerrada
  sin pesos abiertos** (la licencia es del SDK, no del modelo) [S].
- Además, MM-Grounding-DINO —que el proyecto evaluó y descartó empíricamente— no
  tiene ninguna cifra de benchmark en el informe (publicadas: tiny 50,4–50,6 COCO
  zero-shot / 35,7–41,4 LVIS [P/S]).

### 7.2 El estado del arte verificado — las tres varas que importan

**⚠ Advertencia de métrica antes de comparar nada:** las cifras COCO/LVIS de los
papers OVD son **AP promediado sobre IoU 0,50:0,95** (LVIS además con protocolo
Fixed AP); los papers de EPP y nuestro bench reportan **mAP@0,5**, que da
numéricamente más alto para el mismo detector. **Nunca poner las dos series en la
misma columna.** El error previsible del jurado: "GDINO da 48–52 en COCO y ustedes
0,55 — rinde igual". No: en mAP@0,5 sobre COCO estaría muy por encima; nuestra caída
es real y es el costo de dominio.

**Vara 1 — el techo supervisado in-domain (mAP@0,5)** [P/S]:

| Dataset (paper) | Mejor modelo entrenado | mAP@0,5 | Dato fino |
|---|---|---|---|
| SHEL5K (Otgonbold 2022, Sensors) | YOLOR | **0,883** | `head` (cabeza sin casco) **0,907** — supervisada NO es difícil |
| CHV (Wang 2021, Sensors) | YOLOv5x | **0,866** | 6 clases (person, vest, 4 colores de casco) |
| SH17 (2024; 17 clases, industrial) | YOLOv9-e | **≈0,71** | YOLOv8 n→x: 0,58–0,69 — con vocabulario grande el techo baja |

**Vara 2 — OVD fuera de dominio (lo publicado):** GDINO-L cae a **26,1 mean AP**
(0,5:0,95) sobre los 35 datasets de ODinW [P] — la referencia de "cuánto colapsa un
OVD fuera de su distribución".

**Vara 3 — el cruce OVD×EPP (casi vacío, y eso es el hueco que ocupamos):**
- **OWLv2 zero-shot sobre obra** (Choi & Greer 2024, arXiv:2410.12225): AP@IoU>0,5
  **0,649 para hardhat** y **0,677 para person** sobre 5.210 imágenes [P] — la única
  cifra publicada directamente comparable con nuestro AP@0,5 por clase.
- **VLMs grounding con atributo/negación** (Chen 2025, arXiv:2508.11011): "workers
  wearing white hard hats" → **IoU <20%** [P] — la literatura confirma nuestra
  "ceguera al atributo" de E-DIR.
- **No existe paper 2023–2026 con GDINO/YOLO-World zero-shot medido sobre
  SHEL5K/CHV** ni sobre un bench de EPP multi-fuente con protocolo COCO — `bench_v3`
  está esencialmente solo en ese cruce.

### 7.3 Nuestros números contra esas varas — ¿tienen sentido?

**Sí: caen exactamente en la banda que la literatura predice, y en dos puntos quedan
por encima del único comparable directo.** Todo en mAP@0,5 / AP@0,5:

| Qué | Nuestro (zero-shot, preliminar) | Vara externa | Lectura |
|---|---|---|---|
| Agregado 3 fuentes | **0,551** (`gdino-tiny-560`, n=6.477) | techo supervisado in-domain 0,86–0,88 | **≈63% del techo sin entrenar** — la banda esperable; lejos del colapso tipo ODinW |
| `person` | 0,77–0,86 por estrato | OWLv2 zero-shot 0,677 | **por encima** del único zero-shot publicado |
| `helmet` | 0,71–0,89 por estrato | OWLv2 hardhat 0,649 | **por encima**, mismo orden de métrica |
| `vest` | ~0,55 | **sin cifra zero-shot publicada** | dato genuinamente nuevo; su brecha vs ~0,87 supervisado es coherente (menor presencia léxica en el preentrenamiento) |
| `bare_head` | 0,13 (tiny) / 0,40 (base) | **0,907 supervisado** (SHEL5K) | **LA historia**: la clase no es difícil — el zero-shot léxico-conceptual sí (lo respaldan el propio paper de GDINO en clases raras y el <20% de Chen 2025). Es el fundamento externo de AF-5 y de F-88.3 |
| YOLOE-26x | 0,442 agregado, `bare_head` 0,000, recall CR-01 0,000 | YOLOE26-L **36,8 AP LVIS** publicado (serie récord en su benchmark) | **los benchmarks generales no predicen la condición de dominio** — el argumento medido de por qué la selección se hizo sobre bench propio y no sobre LVIS |
| A1 `machinery` | 0,662 zero-shot jamás configurada | — | consistente con que GDINO rinde mejor en objetos "gruesos" y frecuentes que en atributos finos |
| Nivel B (F1 0,789 escena / 0,930 sujeto) | — | **sin vara externa**: la literatura no publica F1 de alertas contra GT temporal humano en obra | no se puede rankear afuera — se sostiene por mecanismo + IC internos, y es parte de la contribución (la capa que la literatura no mide) |

**Tres frases para la defensa que salen de esta sección:** (1) *"zero-shot logramos
~63% del techo que la literatura reporta entrenando en el dominio — y medimos
exactamente dónde se pierde el resto: en las clases léxico-conceptualmente débiles"*;
(2) *"en las clases comparables quedamos por encima del único zero-shot publicado
sobre obra (OWLv2)"*; (3) *"el cruce que nuestro bench mide —OVD zero-shot,
multi-fuente, protocolo COCO, sobre EPP— no existe publicado: no hay tabla de la
cual copiarse, por eso construimos la nuestra"*.

### 7.4 Orientación de las conclusiones: qué aporta cada una frente al estado del arte

La dirección para la redacción (fijada 2026-08-06): **cada conclusión se presenta
posicionada contra la literatura**, de modo que el aporte de la tesis quede leído
como *nueva perspectiva y adaptación de estos modelos*. La palabra "adaptación" hay
que usarla con precisión ante el jurado: **el núcleo medido NO adapta los pesos** —
adapta los modelos **operativamente**: resolución (560), formulación del vocabulario
(prompt sets congelados), y las capas de plataforma alrededor (histéresis temporal,
identidad por sujeto, política de alerta). Medir cuánto rinde ese "stack de
adaptación sin entrenar" ES la perspectiva nueva. El fine-tuning (E-04) es una
**rama experimental aparte, comprometida como jornada** (✎ 2026-08-11, ADR-017):
sus resultados, si existen a la entrega, se rotulan como rama comparativa y no se
funden con el núcleo zero-shot.

| Conclusión / resultado | Frente al estado del arte | Tipo de aporte |
|---|---|---|
| AF-3 — campeón `tiny-560` sobre `bench_v3` | El cruce "OVD zero-shot, multi-fuente, protocolo COCO, sobre EPP" **no existe publicado** (§7.2); la selección por benchmark propio en vez de LVIS quedó justificada por el caso YOLOE (35,9 AP LVIS → recall CR-01 0,000) | **Hueco ocupado** + dato metodológico (los benchmarks generales no predicen la condición de dominio) |
| Resolución 560 (−24% latencia, igual mAP) | La literatura OVD reporta a resolución de paper; el ajuste de resolución como palanca dominio-específica no está caracterizado para EPP | **Adaptación operativa medida** (sin tocar pesos) |
| AF-5 — especialización por clase (`base-560` en `bare_head`/`vest`) | No hay cifras zero-shot publicadas por clase de EPP; `vest` ~0,55 es la **primera cifra zero-shot de chaleco** y `bare_head` 0,13–0,40 vs 0,907 supervisado **cuantifica la brecha léxico-conceptual** | **Dato nuevo** |
| AF-2 — E-DIR vetada (0,146 < 0,5) + mecanismo (ceguera al atributo, 54% FP) | La literatura VLM reporta el fenómeno cualitativamente (grounding con atributo <20% IoU, Chen 2025; comportamiento bag-of-words de encoders contrastivos) | **Confirmación cuantificada con veto pre-registrado**, y elevada de percepción a **nivel sistema** (Nivel B) |
| F-83.6 — E-DIR como recuperador (18,5%) | No reportado en la literatura del cruce | **Dato nuevo** (matiza la conclusión anterior) |
| AF-9 — E-HYB-or refutada (F-87.2: la unión no es monótona en un motor temporal) | La literatura de fusión/ensambles es frame-level, donde unir evidencia solo puede subir recall; **nadie mide fusión a nivel de alerta temporal** | **Perspectiva nueva** — un resultado imposible de ver sin la capa temporal |
| AF-6/AF-7 — la histéresis rescata (recall 1,000 con SDR 0,281) y su límite de cadencia | Los papers de EPP miden mAP por frame; **qué agrega una capa temporal sobre percepción intermitente no está benchmarkeado** | **Perspectiva nueva** — el aporte de plataforma que la métrica estándar no captura |
| AF-1 — identidad: 0,789→0,930 con detecciones idénticas, sobrevive a las 4 densidades | La literatura MOT mide la identidad **como fin** (MOTA/IDF1, GT de identidades); acá se mide **como medio** para atribución de alertas, con la percepción controlada bit a bit | **Perspectiva nueva** — la contribución central; agnóstica al detector |
| AF-4 — extensibilidad medida (48 líneas, 9 min, AP 0,662) + F-94.1 | El argumento clásico pro-OVD ("agregar clases es barato") se **afirma** en la literatura pero no se **mide** como costo marginal end-to-end; F-94.1 agrega el contrapeso (validar la palabra es parte del costo) | **Dato nuevo** — el argumento A1 con número y con su letra chica |
| AF-8/AF-10/AF-11 + L1–L8 | Los trabajos aplicados rara vez declaran qué NO pueden afirmar | **Aporte metodológico** — la escala de fuerza y las limitaciones codificadas |

Regla de redacción que sale de esta tabla: en el informe, cada conclusión se escribe
en tres tiempos — *qué dice la literatura* (con la cifra de §7.2) → *qué medimos
nosotros* (con la cifra de `results/`) → *qué tipo de aporte queda* (columna 3).
Nunca al revés (empezar por el número propio sin vara es lo que hoy le pasa al §15).

**Pendiente que esta sección deja planteado (para el pase de redlines del informe):**
incorporar la Vara 1 con cifras al §15 (o declarar la ausencia como brecha),
declarar el backbone de cada cifra de GDINO, corregir las erratas de 7.1, cruzar la
Tabla 3 con la evidencia propia (YOLOE 0,000; G2A medidos), y corregir el uso de
Abdalwhab 2025 (compara YOLO11 fine-tuned vs OVD zero-shot en componentes MEP — es
evidencia de brecha de vocabulario zero-shot, no del efecto de ajustar OVD).

**Fuentes externas de esta sección** (verificadas 2026-08-06): Grounding DINO
arXiv:2303.05499 · MM-GDINO arXiv:2401.02361 · YOLO-World arXiv:2401.17270 (CVPR'24)
· YOLOE arXiv:2503.07465 (ICCV'25) + docs Ultralytics YOLOE26 · GDINO 1.5
arXiv:2405.10300 · DINO-X arXiv:2411.14347 · SHEL5K Sensors 22(6):2315 · CHV Sensors
21(10):3478 · SH17 arXiv:2407.04590 · OWLv2-hardhat arXiv:2410.12225 ·
ConstructionSite 10k arXiv:2508.11011.

## 8. La escala de conclusiones — qué se afirma y con qué fuerza (doc 98 §2)

**No todo lo medido tiene el mismo estatuto, y decirlo es más fuerte que aplanarlo.**
Regla aplicada: si la estimación puntual era vistosa pero el IC no excluía el cero,
**se degradó la afirmación** (caso testigo: la cruzada G1@4,29 > T1@30).

| # | Afirmación | Respaldo | Fuerza |
|---|---|---|---|
| AF-1 | La granularidad por sujeto mejora el F1 de alertas | ΔF1 +0,141 [+0,032, +0,258]; excluye el cero en las 4 densidades (bajo decimado regular; dirección conservada bajo descarte irregular, 6/6 — doc 101) | **Establecida** |
| AF-2 | E-DIR no sirve como núcleo | Veto pre-registrado de precisión (0,146 < 0,5); brecha F1 0,63; mecanismo: ceguera al atributo (54% de los FP) | **Establecida** (criterio fijado antes de correr) |
| AF-3 | `gdino-tiny-560` es el campeón | mAP50 1º en las dos escalas (147 y 6.477 imgs, 3 fuentes) | **Establecida** (robusta a la fuente) |
| AF-4 | Agregar una condición nueva no cuesta entrenar | 0 entrenamientos, 48 líneas, 9 min, `machinery` AP 0,662 zero-shot (+ contrapeso F-94.1) | **Establecida** (medida, no afirmada) |
| AF-5 | `gdino-base-560` es el especialista (en `bare_head`/CR-01 y en `vest`/CR-02) | recall CR-01 0,599 vs 0,308 (n=5.313); vest AP 0,582 vs 0,520; CR-02 SDR 0,281→0,920 | **Establecida** |
| AF-6 | La histéresis temporal rescata percepción intermitente | CR-02 recall 1,000 con SDR 0,281, pagando t_alert | **Establecida**, con límite (AF-7) |
| AF-7 | Ese rescate tiene un límite de cadencia | P2 cae 1,00 → 0,60 → 0,20 al bajar la densidad | **Establecida direccionalmente** (n=5 episodios) |
| AF-8 | El costo del tiempo real sobre el agregado | Estimaciones puntuales +0,005 / −0,050 / −0,143, decrecientes; ningún IC del agregado de escena excluye el cero | **Tendencia con mecanismo**, no efecto establecido |
| AF-9 | La fusión E-HYB-or no ayuda | Predicción pre-registrada refutada (recall 0,824→0,353), mecanismo F-87.2; `hyb_and` no ejecutada con causa (D-90.4) | **Establecida** (refutación de predicción propia) |
| AF-10 | CR-02 a Nivel A | Un solo estrato (n+=82), IC solapados | **No cerrada** — declarado (L8) |
| AF-11 | FAR/hora | Ninguna cota alcanzable sostiene afirmación (harían falta 3 h anotadas; el banco llega a 0,1027 h de soak sobre 0,2725 h negativas) | **Limitación L1, precisada — no derogada** (✎ 08-09): la métrica **se computa y se reporta** (29,2 escena / 1.850,8 sujeto), pero no sostiene una cota. Citar como **"3 y 190 FP en 6:09,6 del único clip soak"**, con la tasa horaria como derivada. La evidencia principal de FP sigue siendo el control de negativos |

*(La escala usa prefijo **AF** para no confundirse con los argumentos de defensa
A1–A5 de `nucleo/09` — convención en el glosario, doc 13.)*

## 9. Alcance, limitaciones y reglas de lectura

**ADR-015 (aceptado 2026-08-05) — cierre de alcance:** la premisa del "recorte" se
invirtió: **el alcance CRECIÓ con evidencia** — E-03 (G1 de demostrativa a capacidad
operativa medida en 34/34), E-07 parcial (OAK-D + EN-2 87%), E-13 (E-HYB-or ejecutada
y refutada). Desbloqueó R-13 y R-21. Sus cláusulas de puerta cerrada fueron derogadas
después por dos ADRs firmados: ✎ **ADR-016 (2026-08-10)** — la **distribución de
alertas** se reabre con el recorte exacto de ADR-005 y queda **funcionalmente
implementada y verificada** (seis criterios de spec 45; quedan webconsole,
orquestación y primer commit; E-06 sigue excluida) — y ✎ **ADR-017 (2026-08-11)** — el **fine-tuning
(E-04)** pasa de "no ejercida por secuenciación" a **jornada experimental
comprometida** (escalera T1→T2/T3 con go/no-go y Mendieta). ✎ **Adenda 2026-08-13:**
F-100.1 quedó resuelta por `finetuning_v1`; `1166583` cerró freeze/smoke técnico con 12
tensores/3.096 parámetros y optimizer 12/12, y dual gate/serving real están verdes. El full
sigue en NO-GO por ~~contrato de serving D-FT-08/T-FT-005,~~ evaluación T-FT-031 y baseline
26s T-FT-032. La procedencia T-FT-023 quedó CERRADA el 2026-08-13 (snapshot tar
`639e60df…`). ✎ **2026-08-15: el contrato de serving quedó firmado** (D-FT-08, junto con
D-FT-12 y D-FT-13) **y T-FT-031/T-FT-032 cerraron la misma jornada** — baseline YOLOE-26s
one-shot ejecutada y evaluada (doc 120: `bare_head` AP50 0,000, recall CR-01 agregado
0,0002; cifras de la rama comparativa, nunca fundidas con el núcleo). El NO-GO quedó en su
último eslabón: `full-authorization.json` + `RUN` manual del usuario. La
rama permanece condicionada **por datos y protocolo**, nunca por tiempo; la proyección Slurm
2026-08-18 es coyuntural y no una promesa.
✎ **2026-08-15 (noche): ese último eslabón se cerró — T-FT-043 CERRADA.** La autorización
se emitió y verificó en el clúster (7 gates) y el `RUN` quedó **encolado (job `1167640`)**.
Ya no queda tarea previa pendiente; lo abierto es **la corrida y su evaluación**. Enviar no
es medir: **no existe cifra del modelo ajustado** y la subsección correspondiente se
redacta reservada.
✎ **2026-08-17: la jornada CERRÓ — veredicto D-FT-12 = NO-GO**
([`operacion/123`](../operacion/123-cierre-jornada-t1-no-go.md)). **La cifra ya existe y la
subsección deja de ir reservada**: `bare_head` AP50 **0,0000 → 0,0455**, recall CR-01
**0,0002 → 0,2089**, `vest` 0,2642 → **0,3292**, contra `person` 0,7843 → 0,6932 y mAP50
0,4193 → 0,4171. Falla el gain gate por **0,0045** y la retención por `person`
(**−11,62 %**, tope 10 %). Checkpoint **no adoptado**. Márgenes firmados antes de la
baseline ⇒ **negativo pre-registrado: es resultado, no fracaso**. Rama comparativa: **no se
funde con el núcleo zero-shot ni va a `results/`**, y no se compara con el doc 64.
✎ **2026-08-21: T2 también CERRÓ — D-FT-15 = NO-GO, y la jornada E-04 está COMPLETA en sus
tres tiers** ([`operacion/127`](../operacion/127-cierre-t2-no-go-curva-capacidad.md)). El
tier exploratorio (enmienda D-FT-14, márgenes D-FT-15 firmados pre-resultado) respondió su
pregunta: **el fallo de T1 no era artefacto de capacidad — el trade-off es estructural
(F-127.1)**. Con ×3.343 de capacidad entrenable, el gate de ganancia PASA (`bare_head`
0,0000 → **0,0909**, sólo en `shel5k`) pero la retención in-domain FALLA ×4 (`person`
−49,7 %, mAP50 0,4193 → **0,2374**) y la retención open-vocabulary FALLA (COCO interno
0,4347 → **0,1247**, −71,3 %). Curva de 3 puntos completa — es el valor declarado del tier.
Secuencia que el informe declara entera: `1167864` submuestreado (`optimizer=auto` ciego a
los parámetros) ⇒ enmienda **D-FT-16** pre-resultado (SGD explícito desde peso base) ⇒
`1167982` colapsó en entrenamiento (early stop 16/60, mejor época = 1: el checkpoint
evaluado lleva ese caveat siempre). Checkpoint no adoptado; mismas reglas de rama
comparativa que T1.
Ambos frentes se declaran con su **estado a la entrega**
y no bloquean el informe. Todo lo demás sigue cerrado (EN-3, E-10, E-06, CR nuevas).

**Limitaciones canónicas L1–L8** (lista cerrada 2026-08-05; referencia =
`results/index.md`; citar como "limitación Lx"): L1 FAR/hora se reporta pero no
sostiene una cota operativa · L2 sin
doble anotación ni kappa (decisión declarada) · L3 bordes adjudicados en 6 clips ·
L4 medición de obra real acotada que caracteriza la frontera de juzgabilidad, sin
validar el sistema en obra real · L5 escenarios desbalanceados ⇒ reportar por
estrato/escenario · L6 tracker medido en multitud, con fragmentación y costo de FP.
**Sigue en pie: no hay métricas MOT (E-10) y el `track_id` es post-hoc.** · L7 licencia parcial de `chv` ·
L8 CR-02 a Nivel A no cerrada.

**Reglas de lectura no negociables** (familia F-EV, doc 81 §3): reportar por estrato
y escenario, nunca solo agregado · clips negativos fuera de P/R/F1 (su métrica son
los FP) · `re_alerts` ≠ FP (ADR-011) · SDR no comparable entre cadencias · t_alert no
comparable entre densidades sin control de supervivencia · métricas que no aplican
con estado `not_applicable:<causa>` (ADR-006/013).

## 10. Qué encontró y corrigió el relevamiento del 2026-08-06

El relevamiento verificó que **ningún número de los índices está inventado** (todas
las tablas coinciden con sus `metrics.json` y artefactos de bootstrap) y que la
escala AF, los 26 redlines y las cifras canónicas del brief son consistentes.
Los desfases corregidos fueron de **propagación y redacción**, no de datos:

- **ADR-015 aplicado a medias al doc 10** (lo más serio): el ítem 5 (MQTT) seguía
  "dentro del alcance" y las frases de declaración de E-03/E-04/E-06/E-10/E-13 —las
  que van literales al informe— tenían el texto pre-ADR-015. Corregido, junto con
  `estado-de-implementacion-adrs` (filas 001/002/005) y el glosario (doc 13).
- **Derogaciones sin banner**: `operacion/92` no avisaba que ya no es fuente de
  números (el 56 sí lo hacía). Banner agregado; `operacion/98` §8 y `informe/93/95`
  ahora remiten a `results/`.
- **Calificadores obligatorios ausentes en el doc rector de conclusiones**: AF-1 sin
  el "bajo decimado regular" (doc 101 §3) y el G2A sin la advertencia F-101.8.
  Agregados.
- **Índices de `results/`**: el denominador "34 de 35" no estaba escrito; faltaban las
  filas B1/G1/H1 en los desgloses (regla L5); un hallazgo retractado seguía vigente
  (F-83.7/CR-02); "ningún delta excluye el cero" sin el scope de escena (R6−G1 sí
  excluye); la etiqueta "especialista CR-02/`bare_head`" mezclaba los ejes; el soak
  se leía como si habilitara FAR/hora. Todo corregido.
- **Navegación**: doc 101 y ADR-015 no estaban en `00-indice.md`; `GUIA-CIERRE.md`
  describía el proyecto de hace 12 días; el glosario no tenía las convenciones AF-x,
  "limitación L vs hito L" ni las dos series de ADR (hallazgo 6 de `informe/99`,
  **cerrado** con esto). Actualizado.

## 11. Lo que queda (a la espera del equipo) — y qué NO cambia

| Pendiente | Quién | Qué habilita |
|---|---|---|
| ~~**CVAT del lote de internet**~~ ✎ **HECHO 2026-08-06 (doc `operacion/102`)**: llegaron 3 (`v04_c01`, `v06_c01`, `v10_c01`), GT humano derivado/validado/promovido — banco 34→37, **L4 parcialmente levantada** (n = 2 episodios ⇒ fila aparte, D-90.6). Ojo: la trampa del runbook NO aplicó — estos exports eran **task-level** (`split_cvat_project.py` habría sido el error simétrico; mirar `meta/task` vs `meta/project`). Dos escenarios corregidos contra el GT (`v04_c01` P8→P1, `v06_c01` P5→P2); `v06_c01` **no salió negativo** ⇒ sigue sin haber soak y **L1 no se mueve**. Los 11 restantes: marginales (doc 93). **✎ 2026-08-09 — CERRADO y con dos correcciones al registro de arriba** (docs `operacion/108` §6 y `111`): el lote quedó en **13 de 14 con GT** (banco **47**; `v08_c01` excluido con causa firmada), y de los dos escenarios que el GT parecía desmentir **solo `v04_c01` estaba mal** — el **P5 de `v06_c01` era correcto**: su episodio CR-02 era **error de anotación**, así que el clip **es negativo y es el único clip soak del banco** ⇒ **L1 sí se movió** (FAR/hora pasó a computable, aunque insuficiente para sostener una cota). Los "11 restantes" se anotaron salvo uno. Fuente de verdad del GT = las anotaciones versionadas del repo, no CVAT | ~~equipo~~ | — |
| ~~Runs/evals del estrato B~~ ✎ **HECHO 2026-08-06**: I1/I2 corrieron. **El resultado no cierra el banco con un número — abre un hallazgo nuevo** (doc `operacion/103`): en `v06_c01` (127 personas GT) `scene` recall 0,000 (F-81.2(a) extremo) y `subject` recall 1,000 / precision 0,010 (182 identidades del tracker con FP, más que las 127 reales). **Decisión pendiente del equipo:** si esto entra al informe como limitación nueva (densidad de escena) o como ampliación de L4/L6, y si vale anotar más clips en densidad intermedia. **✎ 2026-08-09 — la gen. 3 corrió sobre el lote completo** (doc `operacion/111` §6) **y esa misma noche la revisión CIEGA del GT tiró 3 de los 5 episodios** (doc 113 §B): cifras vigentes `scene` F1 **0,333** vs `subject` **0,190** sobre **2 episodios evaluables** — el mecanismo se confirmó a escala, pero **ese `n` no sostiene ningún ranking entre granularidades** (F-111.1 enmendado); lo robusto es la **asimetría de FP** (~6× en positivos, **12× en los 11 negativos**: 26 vs 323). Nivel A de video: CR-01 **0,031** / CR-02 **0,018**. **Las dos preguntas de esta fila quedaron CERRADAS el 08-09 (D-113.1):** anotar más clips **NO** (doc 112 §8) y el encuadre es **precisar L4** — el set L1–L8 de `informe/99` §6 sigue cerrado, no se crea `L9`. Celda vigente: `results/index.md` §L4; doc 103 §3 cerrado con la misma decisión | ~~Claude~~ / ~~equipo decide el encuadre~~ ✅ decidido | nombra el límite real de G1/scene, no solo "material no guionado" |
| **Videos V1–V3 de la defensa** (pausados; 2 preguntas de alcance, D-90.7) | usuario decide | material de defensa, no resultado |
| Redacción §17.x + regenerar `informe-project-kit` | después de lo anterior (orden 2026-08-05) | el informe |
| Corregir el §15 del informe (erratas + línea base EPP supervisada + backbone de cada cifra + cruce con evidencia propia — ver §7.1/§7.4 de este doc) | pase de redlines (misma puerta que §17.x) | estado del arte defendible |
| ~~Licencias de los catálogos de modelos~~ ✅ **CERRADO 2026-08-10** — y **la premisa era falsa**: los 11 catálogos ya declaraban `license:` y `source:`. Lo que faltaba era el registro, ya escrito: sección **"PESOS DE MODELO"** en `license_registry.md` (GDINO y MM-GDINO **Apache-2.0**, YOLOE **AGPL-3.0**, las tres verificadas contra evidencia independiente: model cards y la cadena embebida en el `.pt`), con la implicancia AGPL declarada. **Residual: los repos no tienen `LICENSE` propio** — decisión del usuario antes de publicar, no bloqueo de defensa | ~~verificar y registrar~~ ✅ | citar los modelos en el informe |
| URL + fecha de acceso por video del lote (evidencia perecedera) — ✎ **son 18 `clip.yaml` con `video_url: TODO`** (14 del lote + 4 del piloto) y **13 copias promovidas** que lo arrastran: se arregla re-promoviendo, no a mano (doc `operacion/113` §C1) | usuario | robustece la cita de la fuente |
| Consentimiento escrito del rodaje (resuelto por declaración; plantilla disponible) | equipo/facultad | formalidad administrativa |
| Backup de `docs/` a otro disco | usuario | redundancia adicional (el repo tiene remote propio desde 2026-08-10, pero el respaldo a disco sigue vigente) |

**Nada de lo pendiente cambia una conclusión** (doc 98 §7): los mecanismos (F-81.x,
F-87.2, F-88.x, F-89.x, F-96.x, F-101.x), el veredicto del eje y las cifras por
estrato ya publicadas no se mueven; el GT del lote solo puede mover el agregado del
clip bench, el texto de L4 y el contexto del control de FP.

---

**Cómo re-verificar esta página:** correr
`python3 docs/operacion/datos/96-verificar-indices.py` — desde el 2026-08-09 cubre
**19 cifras sobre las 16 campañas con artefacto** (incluidas I1/I2 del estrato B y el
Nivel A sobre video de §4.1/§5.1), los deltas de bootstrap, y un **guard de cobertura**
que falla si aparece una campaña sin cifra verificada. Comparar el resto contra los 4 índices de
`e-ovrt_experimental-setup/results/` — cada tabla de allá tiene su artefacto
(`metrics.json`, `campaign.yaml` con sha256, `evals/`) y su doc de procedencia.
