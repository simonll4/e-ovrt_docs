# 62 — Plan maestro de experimentos para justificar la tesis (2026-07-23)

**Documento autocontenido**: consolida el arco experimental completo de E-OVRT-VDP. Repite
deliberadamente lo necesario de 57 (metodología), 58 (plan de cierre), 59 (shot-list),
61 (benchmark realtime) y nucleo/04 (D1) para que este doc alcance como guía única de
ejecución. Ante conflicto, este doc es el vigente (2026-07-23) y los anteriores quedan como
fundamento.

## 1. Objetivo: qué tiene que justificar la experimentación

La tesis NO afirma "OVD detecta mejor" (doc 09 — nunca discutir eso). Afirma: **una
plataforma con condiciones de riesgo expresadas en lenguaje natural, sobre detectores de
vocabulario abierto sin entrenar, y la medición honesta de qué se logra y qué no**. Las
preguntas que los experimentos responden:

- **Q1** — ¿Qué calidad de detección logra un OVD zero-shot en el dominio de obra
  (person/helmet/vest/bare_head)? → Fase S (imágenes) + Fase T (temporal).
- **Q2** — ¿Qué modelo/configuración es el mejor vehículo, y cuál es el trade
  calidad↔latencia? → Fase S (campeones por familia) + doc 61 (5–7× medido).
- **Q3** — ¿Qué agrega la plataforma (persistencia temporal, episodios, re_alerts) sobre la
  detección cruda? → Fase P (Nivel B) + Fase L (EBE live).
- **Q4** — ¿Prompts directos de ausencia (E-DIR) o evidencia positiva + inferencia (E-IND)?
  → Fase D (D1).

**Principio rector del cierre (57 §7.6, decisión del usuario):** el núcleo validable se
cierra con las métricas que el material efectivamente cubra. Lo no cubierto se declara
`censored`/`not_applicable` con causa (ADR-006 + `metric_censored`), nunca bloquea ni se
fabrica.

## 2. Marco de métricas y pre-registros

**Nivel A — rendimiento OVD** (compara modelos/prompts): AP@0.5 por clase, mAP50, recall
CR-01 de detección, TTFD, SDR, G2A. **Nivel B — alertado de la plataforma** (valida el
sistema, NO compara modelos): precision/recall/F1 de alertas por episodio, t_alert-system,
FAR/hora (régimen doc 59 §6: FP/min ventana agregada + cota ~3/N con FP=0), t_compute-budget.
Estados de aplicabilidad ADR-006 en todo artefacto.

**Pre-registros que este documento fija (antes de correr):**

1. **Campeón de calidad por familia (Fase S): primario mAP@50 sobre las 4 clases canónicas;
   desempate recall CR-01 de detección.** El AP por clase se reporta siempre (vest se vigila
   por CR-02; bare_head se reporta aunque sea débil — es un resultado, no un fracaso).
   Selección sobre el agregado test+val del BENCH v2 (196 imgs), ambos splits reportados.
2. **Campeón realtime por familia: el de menor g2a_p50 live que no pierda detección** según
   doc 61 (ya medido: yoloe-26m/l ~35 ms; gdino-tiny-560 −24% vs 800 con mAP igual o mejor).
3. **D1 (E-DIR vs E-IND) se decide en Nivel A con desempate TTFD** (nucleo/04 §8.2,
   enmendado en A5 del doc 58). t_alert-system NUNCA compara modelos.
4. La matriz S1 corre con **prompts congelados** `cr01_cr02_bench_v2` (etiquetas cortas,
   idénticas para todos los modelos) y **plataforma congelada** (motor idéntico, umbrales
   4000/7000 donde aplique).

## 3. Fase S — Selección de modelos (DBE imágenes; EJECUTABLE YA)

No depende del rodaje ni de anotaciones. Motivación doble: (a) completar la matriz que
Sprint 2 dejó a medias — GDINO-base ganó vest (0.439 vs 0.245) y recall CR-01 (0.523 vs
0.414) aunque perdió mAP, MM-GDINO-large y YOLOE-26m/x nunca se midieron, y la dimensión
resolución (560) apareció recién en doc 61; (b) **auditar la calidad de los datasets** antes
de apoyar conclusiones en ellos (duda explícita del usuario 2026-07-23; además la auditoría
visual del `person_gt.json` quedó pendiente desde Sprint 2, Task 4.3).

### S0 — Auditoría de calidad del BENCH v2

Sobre `construction_site_safety` (BENCH: 82 test + 114 val) y su `person_gt.json`:

- **Estadística del GT:** conteos por clase y split; bboxes degeneradas (w/h≤2 px, fuera de
  imagen, aspect extremo); anotaciones duplicadas (IoU>0.9 misma clase); imágenes sin GT;
  distribución de tamaños (proxy de distancia cámara-sujeto — relevante porque el rodaje será
  a 5–10 m).
- **Muestra visual:** ≥20 imágenes con GT dibujado, inspección de: cajas corridas, clases
  mal etiquetadas, personas sin anotar, criterio de `bare_head` (¿gorra cuenta?).
- **Veredicto escrito:** `usable` / `usable con salvedades declaradas` / `reemplazar`. Las
  salvedades entran al reporte de cierre como límites del instrumento, no se ocultan.

### S1 — Matriz completa de modelos (10 configuraciones × 2 splits = 20 corridas DBE)

| Familia | Configuraciones | Nota |
|---|---|---|
| Grounding DINO (HF) | `gdino-tiny`, `gdino-tiny-560`, `gdino-base`, `gdino-base-560` | 560 = catálogo con `image_size` (mejora 5, doc 61) |
| MM-Grounding-DINO | `mm-gdino-base`, `mm-gdino-large` | adaptador HF estándar; **tiny EXCLUIDO** (bboxes degeneradas, Sprint 2); sanity-check de bboxes en el análisis por si la familia reincide |
| YOLOE-26 | `26s`, `26m`, `26l`, `26x` | zero-shot puro, se espera vest/bare_head ≈ 0 (Sprint 2) — se corre igual: es el dato del trade |

Protocolo: servicio por modelo (`EOVRT_MODEL_REF`), `POST /api/runs` con
`dataset: bench_v2_{test,val}`, `POST /evaluate` (AP@0.5, mAP50, recall CR-01), prompts §2.4.
Costo estimado total ≤ 1 h en la RTX 4060. **Excluidos con causa:** GDINO 1.5/1.6 (API-only
IDEA, sin pesos locales), MM-GDINO-tiny (bug), fine-tuning (fuera de alcance de tesis).

### S2 — Cierre de la selección

Tabla final: campeón calidad + campeón realtime por familia + la decisión de qué corre en
cada fase siguiente (T/P con campeón calidad; L con campeón realtime de la familia elegida).
Si campeón calidad ≠ lo ya medido live en doc 61, una corrida live breve de verificación.
**Esto enmienda formalmente la Etapa A del 58 §C y la pista doble del doc 12 §3** (que fijaba
GDINO-tiny + YOLOE-26s por presunción; ahora se elige con matriz completa).

## 4. Fase T — Banco temporal (ESPERA anotaciones)

Bloqueada por: GT de los videos de internet (14, lote B.2.1) + rodaje anotado (CVAT, pasada
humana — todo GT actual sigue `gt_preliminary`). Cuando esté:

1. Promoción laboratorio→banco (`processed/clip_bench/`, gap conocido doc 54 §6).
2. Correr **solo los campeones de S** (no la matriz) sobre el banco temporal completo.
3. Métricas Nivel A temporal: TTFD, SDR, recall de episodios, censura A2 y
   `dimensioning_warnings` A1 aplicadas; `4.1.mp4` como primer positivo real (duro, nocturno
   — no showcase, doc 58 §B.2.1).
4. Si el orden de campeones se invierte respecto de S1 (imágenes), gana el temporal: la tesis
   es de video, y se documenta la inversión como hallazgo.

## 5. Fase P — Validación de la plataforma (Nivel B; tras T)

Modelo congelado (campeón final). Banco completo + soak (6.1 = 6:10 sin cortes) vía runner
del experimental-setup (`experiment_id → clip_id → gt`, consolidación ADR-014). Reporta:
precision/recall/F1 por episodio (matching bipartito A4, `re_alerts` no son FP), FAR/hora con
`observed_duration_ms` (A3), t_alert-system, t_compute-budget, con **n declarado por métrica**
y estados de aplicabilidad. Deuda a cablear antes: `far_per_hour`/`censored_episodes` al
reporte del experimental-setup — detalle en §9 "Deuda de implementación".

## 6. Fase L — EBE live

### L0 — Ensayo preliminar pre-rodaje (EJECUTABLE YA, sin actores)

Objetivo: que el día del rodaje no haya sorpresas (pedido explícito del usuario 2026-07-23).
Con cámaras reales y la config final:

1. Corrida EBE 1:1 completa con el **campeón realtime** y pattern set `cr01_cr02_v2`
   (F-DR9): control-plane primero (`201 subscribed:true`), media-plane después, cierre por
   `run_finished`, `bus_dropped_events=0`.
2. Verificar las mejoras del doc 61 en el camino live real: pre-flight `prepare_run` (sin
   drops del frame 0), OAK-D `fps: 30`, g2a live dentro de presupuesto para YOLOE / declarado
   para GDINO.
3. Ensayo mecánico de **doble toma** (58 §C.5): toma A grabada desde la consola →
   `prepare_clip.sh` la corta; toma B live → corrida 1:1. Sin EPP y sin valor evaluativo:
   valida el circuito, los tiempos de setup y el checklist del doc 59 §7.
4. Claqueta de prueba (palmada + wallclock anotado): ensayar la identidad
   `t_alert = TTFD + t_capture→alert` con GT informal, para decidir si el stretch del 58 §C.5
   entra al rodaje.
5. Salida: **checklist del día del rodaje verificada punta a punta** + tiempos medidos de
   setup por escena (insumo para el plan de jornada del doc 59).

### L1 — EBE del rodaje (día de grabación)

Protocolo de doble toma del 58 §C.5 tal cual: toma A → banco DBE con GT; toma B live →
t_capture→alert (~4.1–4.6 s CR-01 / ~7.1–7.6 s CR-02), t_compute-budget, G2A live, bus=0,
paridad live↔offline. Escenas live mínimas: 1×P1, 1×P2, 1×P3 (P3 = demo de persistencia).
Decisiones vigentes: **sin prefilter EN-2** (D-61.2), **sin cascada** (D-61.1), pipeline
directo (D-61.3).

## 7. Fase D — D1: E-DIR vs E-IND (bloqueada por acta `edir_v1`)

Pre-registrado en nucleo/04 §8.2: se decide en Nivel A, desempate TTFD. Requiere el acta del
usuario que congele `edir_v1` (hoy `frozen_pending_review`). Corre sobre el banco de T con el
campeón de S: mismas corridas, prompt sets distintos (carriles de la estrategia de prompts,
doc 2026-07-17). Complemento: mini-piloto MOCS de clase nueva (argumento A3 de la defensa).

## 8. Análisis de errores y reporte de cierre

- Matriz diagnóstica SDR×recall (57 §7.3.2): cada celda tiene diagnóstico distinto.
- `re_alerts`, alertas inesperadas, sub-umbral alertadas; sobre-marca de `bare_head` como
  insumo de FAR (hallazgo A7) — declarar variante de modelo en provenance (nota D-61.4: 560
  emite más detecciones que 800).
- Reporte final: las 5 declaraciones de Etapa 4 (57 §7.5) + cobertura como resultado, formato
  §7.6. Q1–Q4 respondidas con sus n.

## 9. Secuencia, responsables y exclusiones

**Estado 2026-07-23** — actualizado tras el cierre de S/S0/S1/S2 (docs 63/64), la ampliación
del bench (doc 66, `bench_v3` congelado) y L0 tramo 1 (doc 65).

| Orden | Qué | Estado | Quién | Depende de |
|---|---|---|---|---|
| 1 | S0 auditoría BENCH + S1 matriz 20/30 corridas + S2 campeón + B5 `bench_v3` | ✅ **CERRADO** | Claude | nada |
| 2 | L0 ensayo EBE pre-rodaje | 🟡 **tramo 1 hecho** (doc 65, VERDE); **tramo 2 pendiente** (doc 67 G2: doble toma + claqueta, ~1h) | Claude + **usuario** | cámaras arriba |
| 3 | Pasada humana CVAT videos internet + acta `edir_v1` + consentimientos | ⏳ pendiente | **Usuario** | — |
| 4 | Rodaje (doc 59, guion §9 cerrado) con L1 embebido | ⏳ pendiente | Usuario + Claude | 2 y 3 |
| 5 | GT CVAT del rodaje (equipo de 3, 58 §B.3) | ⏳ pendiente | Usuario | 4 |
| 6 | T banco temporal → P plataforma → D si hay acta | ⏳ bloqueado | Claude | 3/5 |
| 7 | Análisis de errores + reporte de cierre | ⏳ bloqueado | Claude | 6 |

### Deuda de implementación (Claude, sin bloqueo de material — ejecutable ya)

Ninguna bloquea el rodaje; se pueden tomar en cualquier momento libre antes de la Fase P:

1. **Cablear `far_per_hour`/`censored_episodes` al reporte del experimental-setup** (ítem 6,
   deuda desde doc 51/58; ya calculados en `_evaluate_v2` del control-plane, A3/A2 — falta
   que el generador de `report.json`/`report.md` los lea y los muestre). Requisito de Fase P
   (§5); mejor resuelta antes de que la Fase P arranque, no durante.
2. **B3 — auditoría de `ppe_siabar`** (doc 66, prioridad baja): scoring original lo marca
   `dominio_obra_civil: no`; 20 imgs con GT dibujado deciden si entra a `bench_v3` como 4º
   estrato o queda fuera. ~30 min.
3. **Bug de denominador gemelo en `datasets/scripts/bench/evaluate_bench.py` (standalone,
   NO el CLI del media-plane que ya está arreglado).** `evaluate_cr01()` recibe
   `images_by_filename` como parámetro pero nunca lo usa para restringir `person_gt_records`
   — sin ningún flag de opt-in (a diferencia del CLI del media-plane, que hoy sí restringe
   por default). Mitigado porque `CLAUDE.md` raíz ya recomienda el CLI del media-plane sobre
   este script; igual es una trampa latente si alguien lo invoca directo con un
   `--person-gt` más ancho que su `--bench-coco`. Fix: aplicar el mismo patrón
   `restrict_gt_to_detections` o, más simple, deprecar el script standalone a favor del CLI.
4. **Promoción laboratorio→banco** (`processed/clip_bench/` no existe aún, gap doc 54 §6) —
   necesaria para la Fase T; puede prepararse (script, tests) antes de que llegue el GT.

### Exclusiones vigentes (no re-litigar)

Cascada E-HYB (D-61.1, trabajo futuro), EN-2 en corridas evaluativas (D-61.2), GDINO 1.5/1.6
(API-only), MM-GDINO-tiny/large (bug de bboxes reproducido dos veces), fine-tuning, CSS-train
como fuente de bench (100% aumentado por Roboflow, doc 66 B1), spec 45 MQTT para lo último
(decisión usuario). Regla transversal: nada se commitea sin pedido explícito.

### Lo único que falta del lado del usuario (resumen ejecutivo)

1. **G2**: coordinar ~1h con cámaras para el ensayo de doble toma (doc 67).
2. **Pasada humana CVAT** de los 14 videos de internet (desbloquea Fase T sola, sin esperar
   el rodaje).
3. **Rodaje**: consentimientos + coordinación de colegas + EPP físico (doc 59 guion listo).
4. **Acta `edir_v1`** (desbloquea Fase D; no bloquea T/P).

Todo lo demás — selección de modelo, plataforma de medición, bench de imágenes, config del
rodaje, preparación EBE — está **cerrado y verificado** (auditoría de cierre 2026-07-23).
