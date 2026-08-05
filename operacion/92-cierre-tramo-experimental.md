# 92 — Cierre del tramo experimental sobre el banco del rodaje (insumo R2)

- **Fecha:** 2026-08-05.
- **Qué es:** el "análisis de errores y reporte de cierre" que el plan maestro dejó
  como fase final (doc 62 §8), ejecutado sobre el tramo que quedó completo: **6
  campañas de Nivel B** sobre el mismo banco/GT/motor (T1, T2, D1, H1, B1, G1), la
  **Fase D de Nivel A** (doc 83) y los humos live (docs 65/67/91). Responde Q1–Q4 con
  sus n, llena la matriz diagnóstica SDR×recall y actualiza las 5 declaraciones de
  Etapa 4. **Es el insumo del capítulo de resultados del informe, no el informe.**
- **Marco de lectura (doc 81 §1, decisión del usuario):** cada número es el
  rendimiento medido de UNA combinación; el contraste entre combinaciones ES el
  experimento. Nada de esto es una nota de aprobación.

---

## 1. Las cuatro preguntas del plan maestro, respondidas con sus n

### Q1 — ¿Qué calidad de detección logra un OVD zero-shot en obra?

**Imágenes (n = 6.477, 3 fuentes independientes, `bench_v3`):** el campeón
(`gdino-tiny-560`) da mAP50 0,551 agregado / 0,447–0,503 en el núcleo curado de obra
(docs 64/66). Por clase, la asimetría es estructural: `person` y `helmet` sólidas,
`vest` la más débil de las positivas, `bare_head` fuerte solo en el especialista
(`gdino-base-560`: recall CR-01 0,599 vs 0,308, n = 5.313).

**Estado por persona (Fase D Nivel A, doc 83):** con umbrales calibrados en mitad A y
reporte en mitad B — CR-01: F1 0,546 (`shel5k`, n = 2.487 violadores; IC no solapados
con las alternativas) / 0,408 (`bench_obra`, n = 28). CR-02: F1 0,479 (`bench_obra`,
n = 142 violadores desde negativos explícitos del raw; **único estrato con GT de
chaleco** — IC solapados, CR-02 no cerrado a Nivel A).

**Video (n = 34 clips, 35 episodios, GT humano):** la percepción es **rápida cuando
ve** (TTFD 168 ms ≈ 5 frames, F-81.3) e **intermitente donde la clase es débil** (SDR
de chaleco 0,16–0,28 con tiny; 0,92 con base — F-84.6).

### Q2 — ¿Qué modelo es el mejor vehículo, y cuál es el trade calidad↔latencia?

`gdino-tiny-560` sigue siendo el campeón global tras 6 campañas de video: **ninguna
alternativa lo superó en F1 de alertas** (T2 base-560: 0,704 vs 0,789). La resolución
560 da −24% de latencia con igual o mejor mAP que 800 (doc 61). El especialista tiene
un rol acotado y medido: **base-560 es la palanca de CR-02** (SDR 0,281→0,920, t_alert
−2,2 s) y **no es palanca de CR-01 en video** (F-84.5: el pre-roll empeora — las
prematuras triplican su adelanto mediano). La elección de modelo mueve a E-IND; la de
formulación mueve a E-DIR (F-84.3): son palancas de carriles distintos.

### Q3 — ¿Qué agrega la plataforma sobre la detección cruda?

La respuesta con más evidencia del tramo, en tres capas:

1. **La histéresis temporal rescata percepción intermitente pero correcta** (F-81.1):
   CR-02 con SDR 0,16 llega igual a recall 1,000, pagando tiempo (t_alert 8,6 s vs
   4,3 s). El detector solo no sostendría CR-02; el patrón encima sí.
2. **Pero es palanca de doble filo, medida en los dos sentidos** (F-85.3): la misma
   persistencia **amplifica** evidencia persistente-pero-equivocada (D1: 35 FP; 2 FP
   en negativos donde el resto da 0) y la evidencia equivocada **temprana canibaliza
   alertas correctas** (F-87.2: la unión de evidencia NO es monótona en un motor
   temporal — P1 pasa de 1,000/0 FP a 0,000/12 FP **con la percepción mejorada**).
   El motor mide persistencia, no corrección.
3. **La capa que más agrega es la identidad** (G1, doc 89): F1 0,789 → **0,930** con
   SDR y TTFD idénticos hasta el decimal — la mejora es 100% atribuible al motor,
   cero a la percepción. P7 (multitud) pasa de 0,400 a 1,000. **El margen del sistema
   no estaba en el modelo ni en los prompts: estaba en la noción de identidad.**
   Verificado en vivo (doc 91) y reproducible por config (34/34 idénticos).

Y el costo de decisión de la plataforma es la política, no la percepción (F-81.3:
t_alert ≈ persistencia + TTFD).

### Q4 — ¿Prompts directos de ausencia (E-DIR) o evidencia positiva + inferencia (E-IND)?

**E-IND, por el criterio pre-registrado y en las dos fases.** Nivel A: el gate del §8
no se dispara (CR-01 ratio 0,34–0,46 en dos estratos; CR-02 0,87) → E-DIR pasó a
Fase 2 sin re-litigar. Nivel B: **precision 0,146 < 0,5 dispara el veto** → E-DIR
descartada como núcleo; brecha final de F1 0,63 (0,160 vs 0,789), y **se agranda al
pasar por la plataforma** (ratio 0,20 en video vs 0,34–0,46 en imágenes).

Lo que la serie agrega sobre el binario ganó/perdió:

- **El mecanismo de la falla está identificado**: ceguera al atributo (54% de los FP
  de E-DIR caen sobre personas que cumplen, medido a Nivel A) que la persistencia
  convierte en falsas alertas confirmadas.
- **La debilidad es estructural, no de capacidad** (F-84.1: ratio 0,34 con ambos
  modelos, idéntico al segundo decimal).
- **Lo que manda es la formulación, no el mecanismo** (F-88.3): ausencia espacial con
  etiqueta corta 0,582–0,731 > `bare head` directo (etiqueta corta) 0,480 > frases
  negadas 0,231. La ventaja de E-IND no es "inferir > detectar": es que su
  vocabulario son etiquetas cortas que el modelo entiende.
- **E-HYB-or refutada** (predicción registrada "sube recall": el recall se derrumbó,
  F-87.1/87.2); `hyb_and` **no ejecutada con causa y predicción escrita** (doc 87 §5,
  salida prevista por el pre-registro §6.2). La complementariedad medida (18,5%
  CR-01 / 18,8% CR-02) y la única victoria local de E-DIR (P9: 0,800 vs 0,600)
  quedan como trabajo futuro ubicado: la fusión tiene margen en el pre-roll, no en
  general.

---

## 2. La matriz diagnóstica SDR×recall (doc 57 §7.3.2), llena

Cada celda tiene diagnóstico distinto — y el tramo pobló las cuatro:

| | **SDR alto** | **SDR bajo** |
|---|---|---|
| **recall alto** | T1-CR01 (0,79/0,81) y **G1** (0,97/0,70): percepción y patrón sanos. T2-CR02 (1,0/0,92): percepción resuelta por modelo | **T1-CR02 (1,00/0,28): la firma de F-81.1** — el patrón rescata percepción intermitente; techo declarado (alargar persistencia rompería CR-02) |
| **recall bajo** | **H1 (0,35/0,74) y B1 (0,38/0,94): la firma de F-87.2** — el problema es CUÁNDO se ve, no SI se ve: evidencia temprana corre la alerta fuera de la ventana. T2-CR01 parcial (prematuras) | **D1 (0,18/0,21): percepción ausente o equivocada** — la evidencia directa casi no existe donde el GT la exige (CR-02: recall 0, SDR 0,02) |

Lectura transversal: **recall bajo con SDR alto nunca es un problema de percepción**
— es timing/ventana (pre-roll, granularidad, evidencia temprana). Esa distinción, que
la matriz prometía, es la que separó "cambiar de modelo" (no arregla P7–P9, F-84.5)
de "cambiar la granularidad" (lo arregla, F-89.1).

## 3. Las 5 declaraciones de Etapa 4 (doc 57 §7.5), actualizadas a lo que pasó

1. **FAR/hora** — superada por la determinación D-90.1: **no se reporta como métrica
   de rendimiento** (ninguna cota alcanzable sostiene afirmación: harían falta 3 h de
   cumplimiento anotado y el banco llega a 0,10–0,26 h). La evidencia de FP es el
   **control de negativos**, comparativo pareado: T1/T2/G1/B1-eind = 0 FP de 4;
   D1/H1/B1-barehead = 2–3. El estatuto epistemológico queda declarado igual, con la
   corrección al doc 57 (el soak NO cuesta ≈0 de anotación) registrada.
2. **Piso de ~200 instancias** — cumplido por la vía correcta: el piso aplica a lo
   espacial (bench de 6.477 imgs; 2.487 violadores en la mitad de test de shel5k) y
   las métricas por-episodio van con n efectivo declarado e IC (bootstrap en Nivel A;
   n=34 episodios con desglose obligatorio en Nivel B). Los cortes donde el n no
   alcanza están **dichos**: CR-02 Nivel A (IC solapados), todo `bench_obra` con
   n<30 por condición (F-84.4: lo de n chico NO replicó).
3. **`metric_censored`** — operativa: 1 episodio censurado descontado del denominador
   en todas las campañas (34 evaluables de 35).
4. **P9 confusables + soak** — P9 existe y resultó discriminante (es el único
   escenario donde E-DIR gana y donde G1 no llega a 1,0). El soak quedó en la
   determinación D-90.1 (limitación, no métrica).
5. **"t_alert-system no compara estrategias"** — cumplida a tiempo: la enmienda al
   pre-registro D1 (desempate por TTFD) se hizo ANTES de correr (doc 04 §8 ✎), y el
   tramo la confirmó empíricamente (D1: t_alert 6,6 s vs 5,3 s dice poco; TTFD 847 ms
   vs 168 ms dice todo).

## 4. Cobertura como resultado (principio §7.6)

| Métrica | Cubierta por | Estado |
|---|---|---|
| AP/mAP por clase | bench_v3 (6.477) | ✅ medida, 3 fuentes |
| Estado por persona (CR-01) | bench_obra + shel5k | ✅ medida con IC |
| Estado por persona (CR-02) | bench_obra (142) | ⚠️ medida, **IC solapados — no cerrada** |
| Recall/precision/F1 de alertas | 34 clips, 35 episodios | ✅ medida, 6 combinaciones |
| TTFD / SDR | ídem (pre-roll real) | ✅ medida |
| t_alert PR-01/PR-02 | episodios ≥17 s / ≥29 s | ✅ medida (censura aplicada) |
| **FAR/hora** | — | 🔴 **limitación declarada (D-90.1), no se reporta** |
| Generalización a no-guionado (L4) | — | 🔴 pendiente del lote de internet (CVAT) |
| Latencia operativa live | humos EBE (65/67/91) | ✅ funcional verificada; caracterización en docs 73/74 |

## 5. Limitaciones que el informe declara (sin novedad, consolidadas)

L1 FAR (determinación D-90.1) · L2 sin doble anotación (decisión, sin kappa) · L3 seis
bordes adjudicados · L4 un solo bloque guionado, sin obra real en video · L5
escenarios desbalanceados (reportar siempre por escenario) · CR-02 a Nivel A en un
solo estrato · el `track_id` de G1 es post-hoc/decorador (verificado en vivo, pero el
tracker no está medido en obra real) · `run_descriptor` sin variante de modelo
(D-61.4: la procedencia vive en los campaign.yaml).

## 6. Dónde está cada número

- **Tabla comparativa de campañas** (la que va al informe):
  `e-ovrt_experimental-setup/results/clip_bench/index.md` (+ `results/bench_nivel_a/`).
- Mecanismo de fallas por campaña: `datos/85-mecanismo-de-fallas.py` (reproducible).
- Docs por campaña: 81 (T1), 84 (T2+réplica), 85 (D1), 87 (H1), 88 (B1), 89 (G1),
  83 (Nivel A), 91 (live).

## 7. Qué le falta al capítulo (y quién lo destraba)

1. **Lote de internet** → L4 y el análisis de sensibilidad de FP (usuario: CVAT).
2. **Videos V1–V3 de la defensa** → D-90.7 (2 preguntas de alcance; el tracking
   post-hoc ya existe, falta la composición visual).
3. **Ratificación de la adenda ADR-002** y aceptación de `hyb_and`-con-causa
   (D-90.4) → una palabra del usuario cada una.
4. Traducción de este insumo a las secciones §17.x del informe (redacción).
