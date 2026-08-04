# 85 — Fase 2 de D1: E-DIR a Nivel B (evaluador `direct_evidence` + campaña D1)

- **Fecha:** 2026-08-04 (madrugada, continuación de los docs 83/84).
- **Qué es:** el tramo de Nivel B del eje de la tesis. La Fase 1 (doc 83) dejó a
  E-DIR viva (el gate del §8 no se disparó); el pre-registro (doc 12 §6.2) manda
  correrla ahora por la cadena completa. Faltaba **el único código pendiente del
  eje**: el motor solo sabía consumir ausencia espacial.
- **Estado:** evaluador implementado (TDD, control-plane **285 passed**, +21 tests),
  humo verde, **campaña D1 corriendo** al escribir esto. **Sin commitear.**

## 1. Qué se construyó (spec 41 §6, ya diseñado — se implementó tal cual)

| Pieza | Qué hace |
|---|---|
| `evaluators/direct_evidence.py` | La evidencia del patrón es una **detección directa de la condición** ("construction worker without safety helmet"), gateada por persona (doc 12 §4.2): IoU≥0,5 para frases persona-céntricas, centro-en-región para partes (`bare_head`). Sin persona → `ungated_direct_hits` (diagnóstico), nunca evidencia. Emite el mismo `PatternEvaluationResult` que `spatial_absence`: **toda la lógica temporal del motor es común**. |
| `evidence.strategy` en la config del patrón | `eind` (default — los pattern sets existentes no cambian) / `edir` / `hyb_or` (unión, ya implementada) / `hyb_and` (**rechazada en validación** hasta el tramo de fusiones, para que no falle en silencio como un eind). |
| `evaluators/__init__.py::evaluate_pattern` | Despacho por estrategia: el motor llama una sola función y no conoce evaluadores concretos. |
| `configs/patterns/cr01_cr02_edir_v1.yaml` | Pattern set E-DIR: **única variable vs `v2` es la estrategia** — mismos timings (4000/7000), regiones y umbral de sujeto. |
| 21 tests nuevos | gating (IoU, región, umbrales, sin-persona), agregación escena/subject con degradación `no_track_id`, validación de config, dispatch, `hyb_or` (incluida la unión que deja pasar la evidencia directa aunque el casco esté detectado), integración con el motor, y el fix F-85.2. |

Decisión de diseño conservadora: `required_absent_class` **no se tocó** (sigue
requerida y documenta la clase EPP violada; los sinks aguas abajo la leen) — el
evaluador edir no la consume. Cero cambios de contrato.

## 2. Dos hallazgos del humo — ANTES de quemar la campaña

El humo sobre `a_p1_c09` (mismo protocolo que T1) atrapó dos cosas que habrían
invalidado la campaña entera:

### F-85.1 — Los umbrales calibrados en imágenes NO transfieren a video
El pattern set salió con los umbrales de la calibración de Fase 1 (mitad A de
`bench_obra`: `cr01_spec` 0,70 / `cr02_obs` 0,40). En el clip, `cr01_spec` disparó en
266/722 frames con **confianza máxima 0,37** — el dominio y la composición del
caption corren las confidencias (hasta `person` bajó: máx 0,46 vs ~0,9 con el caption
de `v2_short`). Con 0,70 la campaña daba **cero por construcción**.
**Decisión**: umbral de evidencia directa = **0,25, el default de la plataforma** —
exactamente el mismo `min_absent_class_confidence` que `v2` usa para E-IND. Trato
simétrico entre estrategias, sin calibrar sobre los clips (son el test set).
**Lección**: un umbral calibrado es relativo a su dominio Y a su caption; llevarlo a
otro régimen sin re-verificar es la trampa 8 en otra forma.

### F-85.2 — El derivador de SDR/TTFD tenía hardcodeada la estrategia E-IND
`_positive_flags_for_source` (evaluation/temporal.py) llamaba **siempre** a
`evaluate_spatial_absence` para decidir si un frame es "detección positiva". Con un
run E-DIR —cuyo caption no trae clase EPP— **toda persona contaba como evidencia de
ausencia**: el humo dio SDR 0,994 con **cero alertas**. El principio del propio
docstring ("reusa el evaluador real del motor, no se inventa una tercera fuente de
verdad") exige despachar por estrategia: ahora usa `evaluate_pattern`. TDD; los SDR
de T1/T2 no cambian (sus patterns son `eind`). Familia F-EV: cuarto artefacto de
medición encontrado validando antes de reportar.

### El humo como resultado
Con los fixes: cadena verde (2 alertas, histéresis, SDR 0,370 — coherente con los
266/722 frames de evidencia). En ese clip: **P=R=0** — confirma a los 4,0 s con
evidencia **desde el frame 0**, o sea la frase dispara sobre la persona durante el
pre-roll donde el GT dice "cumple" (episodio arranca a 3,9 s; borde de matching 7,4 s).
Es la **ceguera al atributo** medida en Nivel A (54% de los FP de E-DIR sobre
personas CON casco) apareciendo a Nivel B como confirmación prematura. Un solo clip:
la campaña dirá si es el patrón general.

## 3. La campaña D1 (corriendo)

`d1_gdinotiny560_edirpair_scene`: tiny-560 × caption "person + cr01_spec + cr02_obs"
(ganadoras por condición en calibración de Fase 1, frases congeladas de `edir_v1`) ×
`cr01_cr02_edir_v1` × escena × DBE stride=1 × los 34 clips. El brazo E-IND de la
comparación **es T1** (caption byte-idéntico, doc 83 §5 bis). Declaración completa:
`results/clip_bench/d1_gdinotiny560_edirpair_scene/campaign.yaml`.

Caveat de lectura declarado: los SDR/TTFD de D1 usan el criterio de frame-positivo de
SU estrategia (hit directo gateado) — interpretables y comparables contra el GT, pero
el criterio difiere del de T1 (ausencia espacial).

## 4. Resultados — 34/34 clips, 0 errores

| Métrica | T1 (E-IND) | **D1 (E-DIR)** |
|---|---|---|
| Recall micro | **0,824** (28/34) | **0,176** (6/34) |
| Precision micro | **0,757** | **0,146** |
| F1 | **0,789** | **0,160** |
| SDR | 0,698 | 0,210 |
| TTFD | 168 ms | 847 ms |
| `t_alert-system` | 5.327 ms | 6.611 ms |
| FP / re_alerts | 9 / 7 | **35** / 2 |
| **Negativos (control de FP)** | **0 FP** de 4 | **2 FP** de 4 |

### Por condición — y acá está lo que da vuelta la Fase 1

| | T1 SDR | D1 SDR | T1 FP | D1 FP | D1 recall |
|---|---|---|---|---|---|
| CR-01 | 0,805 | 0,252 | 8 | **27** | — |
| CR-02 | 0,281 | **0,020** | 1 | **14** | **0,000** (0/7) |

### Por escenario

| Esc. | T1 | D1 | FP T1 → D1 |
|---|---|---|---|
| P1 | 1,000 | **0,091** | 0 → **16** |
| P2 | 1,000 | 0,000 | 1 → 8 |
| P4 | 1,000 | 0,500 | 0 → 1 |
| P6 | 1,000 | 0,000 | 0 → 6 |
| P7 | 0,400 | 0,000 | 5 → 1 |
| P8 | 0,500 | 0,000 | 1 → 2 |
| **P9** | 0,600 | **0,800** | 2 → 1 |

## 5. El veredicto pre-registrado

`nucleo/04` §8 criterio 1 (**veto de precisión**, fijado antes de correr): *"una
estrategia con precision de alertas < 0.5 no puede ser núcleo aunque gane en F1"*.

**D1 tiene precision 0,146. El veto se dispara. E-DIR queda descartada como núcleo y
E-IND queda confirmada como la estrategia del núcleo validable** (ADR-001), ahora por
medición y no por prior. El criterio se aplica sin desempates: no hace falta llegar al
§8.2 (ΔF1 < 0,05) porque la brecha es de 0,63 en F1.

Ratio F1 E-DIR/E-IND a Nivel B: **0,20** — muy por debajo del 0,34–0,46 de Nivel A.
**La brecha se AGRANDA al pasar por la plataforma**, no se cierra.

## 6. Hallazgos

### F-85.3 — La histéresis es una palanca de doble filo, y ahora está medida en los dos sentidos
F-81.1 mostró que el motor temporal **rescata** una percepción intermitente pero
correcta: CR-02 con SDR 0,16 llegaba igual a recall 1,000 porque la persistencia
acumulaba evidencia débil hasta confirmar. D1 muestra la cara simétrica: el motor
**amplifica** una percepción persistente pero equivocada. E-DIR dispara sobre personas
que cumplen (la ceguera al atributo del Nivel A: 54% de sus FP sobre gente CON casco),
la evidencia errónea es *sostenida* —no intermitente—, y la histéresis la convierte en
alerta confirmada: **35 FP contra 9**, y por primera vez **2 FP en los clips negativos**
(T1 y T2 tenían 0/4). La histéresis no distingue "débil pero correcta" de "fuerte pero
equivocada": solo mide persistencia. **Es el argumento pro-plataforma de F-81.1 y su
límite, medidos con la misma cadena y el mismo GT.**

### F-85.4 — El ranking de Nivel A NO transfiere a Nivel B, y se invierte en CR-02
En imágenes, CR-02 era **el punto fuerte** de E-DIR (ratio 0,87, casi empate con
E-IND) y CR-01 su punto débil (0,34). En video se da vuelta: **CR-02 colapsa a recall
0,000 con SDR 0,020** (la evidencia directa de chaleco prácticamente no existe durante
los episodios) mientras CR-01 conserva algo de señal (SDR 0,252). Una estrategia
competitiva a nivel percepción-en-imagen puede ser inservible a nivel alerta-en-video:
**el Nivel A no es un predictor suficiente del Nivel B**, que es justamente por qué el
pre-registro exige las dos fases y decide en la segunda.

### F-85.5 — P9 es la única victoria de E-DIR, y es donde E-IND es más débil
`P9` (pre-roll frágil) es el **único** escenario donde E-DIR supera a E-IND:
**0,800 vs 0,600**, y con menos FP (1 vs 2). Es coherente con la complementariedad
medida en Nivel A (E-DIR recupera 18,5% de lo que E-IND no ve): la evidencia directa
aporta donde la inferencia espacial falla. **No alcanza para ser núcleo —el veto es
sobre el agregado— pero es exactamente el insumo que justifica E-HYB** como rama
experimental (ADR-001) y lo ubica: la fusión tiene margen en el pre-roll, no en general.

### Mecanismo de las fallas (`datos/85-mecanismo-de-fallas.py`)

| Tipo | T1 | D1 |
|---|---|---|
| `prematura_pre_roll` | 5 | **14** |
| `sin_episodio_activo` | 0 | **12** |
| `cruzada_de_condicion` | 4 | 8 |
| `tardia` | 0 | 3 |
| adelanto mediano de prematuras | 0,5 s | **2,5 s** |

Las prematuras casi se triplican y su adelanto mediano pasa de 0,5 a 2,5 s: E-DIR
confirma **dentro** del tramo que el GT marca como "cumple". Y aparecen 12 alertas
`sin_episodio_activo` (categoría vacía en T1): evidencia sostenida donde no hay
violación en absoluto — el mecanismo detrás de los 2 FP en negativos.

## 7. Qué habilita / qué sigue

- **El eje central de la tesis está resuelto con datos**: E-IND es el núcleo por el
  criterio pre-registrado, con Nivel A y Nivel B medidos, mecanismo explicado y la
  estrategia perdedora documentada con sus números (§8 criterio 4: nada se tira).
- **E-HYB queda mejor ubicada que antes**: F-85.5 dice dónde buscar (pre-roll/P9), no
  "en general". `hyb_or` ya corre por config; `hyb_and` (factor de ventana) sigue
  pendiente y ahora tiene una predicción específica que contrastar.
- Sin cambios para la plataforma: `cr01_cr02_v2` (E-IND) sigue siendo el pattern set
  desplegado. Todo lo de este doc es aditivo.
