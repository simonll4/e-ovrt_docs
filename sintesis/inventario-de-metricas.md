# Inventario de métricas de la plataforma

- **Fecha:** 2026-08-06
- **Qué es:** la lista completa de las métricas que la plataforma calcula o reporta, con
  una línea por métrica. Pensado como referencia rápida (y como material para el
  glosario / el knowledge de un Project).
- **Fuentes:** contratos en código — `e-ovrt_control-plane/src/eovrt_control/contracts/metrics.py`,
  `evaluation/temporal.py`, `metrics/latency.py`; `e-ovrt_media-plane/src/eovrt_media/contracts/events.py` —
  más `sintesis/fundamentos-teoricos.md` Parte IV–V y los 4 índices de
  `e-ovrt_experimental-setup/results/`.
- **Nota:** un nombre en `monoespaciado` es el campo tal cual sale en el JSON del
  artefacto; el resto es el nombre con el que se cita en el informe.

---

## 1. Nivel imagen — percepción espacial (banco `bench_v3`)

| Métrica | Qué es |
|---|---|
| **IoU** | Solapamiento caja predicha / caja GT (intersección ÷ unión). Umbral de acierto: IoU ≥ 0,5. |
| **Matching greedy 1:1** | Cada predicción se asigna a lo sumo a un GT, por score descendente. No es una métrica, es la regla que define TP/FP/FN. |
| **Precision (P)** | TP ÷ (TP+FP) — de lo que el detector afirmó, cuánto era cierto. |
| **Recall (R)** | TP ÷ (TP+FN) — de lo que había anotado, cuánto encontró. |
| **AP@0.5** | Área bajo la curva precision-recall barriendo el umbral de confianza, con IoU≥0,5. Un número por clase. |
| **mAP50** | Promedio de AP@0.5 entre clases. **La métrica de selección de modelo del proyecto.** |
| **AP por clase y por estrato** | El mismo AP@0.5 desagregado (`person`, `helmet`, `vest`, `bare_head` × `bench_obra`/`chv`/`shel5k`). Obligatorio por la limitación L5: el agregado engaña. |

## 2. Nivel persona ("Nivel A") — el estado *sin EPP* por sujeto

| Métrica | Qué es |
|---|---|
| **P / R / F1 por condición** | Las mismas P y R, pero la unidad es *una persona en un estado* ("esta persona está sin casco"), no una caja. F1 = media armónica. |
| **recall CR-01** | Fracción de personas violadoras de CR-01 recuperadas, contra el GT person-level (`person_gt_shel5k.json`). Es el eje que decide si un modelo sirve para CR-01. |
| **n+** | Cantidad de positivos del corte. Va siempre junto al F1: es lo que separa "resultado" de "anécdota". |
| **IC95 por bootstrap** | Intervalo de confianza del recall/F1 por remuestreo. Si dos IC no se solapan, hay diferencia real; si se cruzan, es ruido. |
| **ratio F1 E-DIR / E-IND** | Cociente entre estrategias de prompt. Umbral pre-registrado del gate: ambas condiciones < 0,50. |
| **Complementariedad** | De lo que la estrategia ganadora **no** ve, qué fracción recupera la otra. Umbral pre-registrado: > 15% ⇒ hay margen para fusión. |
| **Tasa de corroboración** | Qué porcentaje de los TP y de los FP de una estrategia son confirmados por la otra. Mide si la fusión discrimina o solo suma ruido. |

## 3. Nivel alerta ("Nivel B") — el resultado principal (`evaluate-alerts`)

Contrato `control.eval.temporal.v1`. La unidad es el **episodio**: un intervalo
[inicio, fin] de una condición dentro de un clip, contra GT temporal humano.

| Métrica | Qué es |
|---|---|
| **Recall** | Episodios con alerta ÷ episodios evaluables (micro, por episodio). |
| **Precision** | Alertas que caen dentro de la ventana de un episodio ÷ alertas totales. |
| **F1** | Media armónica de las dos. **La cifra que compara combinaciones.** |
| **`t_alert`** | (`avg_latency_ms_from_episode_start`) Desde que la condición se sostiene hasta la confirmación. Su ideal **no es 0**: es el umbral de la política (4.000 ms CR-01 / 7.000 ms CR-02). |
| **`TTFD`** | (`avg_ttfd_ms`) Desde el inicio del episodio hasta la primera evidencia. Separa el costo de la **percepción** del costo de la **política**. |
| **`SDR`** | (`avg_sdr`) *Sustained detection ratio*: fracción del episodio cubierta por detecciones — la densidad de la evidencia, en [0,1]. **No comparable entre cadencias** (F-96.6). |
| **`FP` en negativos** | Alertas emitidas sobre los 4 clips de cumplimiento. Los negativos **no** entran a P/R/F1: esta es su métrica, y es el control de falsas alarmas del proyecto. |
| **`re_alerts_count`** | Re-confirmaciones de una condición ya alertada. **No son falsos positivos** (ADR-011: el cooldown vive fuera del motor). |
| **`censored_episodes_count`** | Episodios que no pueden medirse porque el clip termina antes del borde de la ventana (`clip_too_short_for_t_alert_window`). Salen del denominador con causa, no cuentan como fallo. |
| **`duplicate_alerts_count`** | Alertas repetidas sobre un mismo episodio ya matcheado. |
| **`sub_threshold_count`** | Eventos anotados en el GT como por debajo del umbral de confirmación: lo que el motor **debía** ignorar. |
| **Conteos crudos** | `expected_alerts_count`, `observed_alerts_count`, `matched_alerts_count`, `missed_alerts_count`, `unexpected_alerts_count` — la trazabilidad detrás de P/R/F1. |
| **`avg_latency_ms_from_first_evidence`** | Latencia de la política medida desde la primera evidencia (no desde el inicio anotado). Diagnóstico. |
| **Mecanismo de los FP** | Clasificación de cada alerta inesperada: `prematura_pre_roll`, `cruzada_de_condicion`, `sin_episodio_activo`, `tardia`. No cuantifica: explica. |
| **Desagregados obligatorios** | Todo lo anterior por **escenario** (P1–P9) y por **condición** (CR-01 / CR-02). Nunca solo el agregado. |

## 4. Runtime del media-plane — costo de la percepción

Contratos `media.detection.v1` (por unidad) y `media.summary.v2` (por corrida).

| Métrica | Qué es |
|---|---|
| **`inference_ms`** | Tiempo del forward del modelo por unidad. El grueso de la latencia. |
| **`normalize_ms`** | Pre-procesamiento (decodificación, resize, conversiones) antes del modelo. |
| **`postprocess_ms`** | Filtrado por umbral, NMS y armado de las detecciones. |
| **`write_ms`** | Serialización y escritura del evento al JSONL / al bus. |
| **`total_ms`** | Suma de las etapas por unidad; `avg_latency_ms` es su promedio de corrida. |
| **`fps_effective`** | Unidades procesadas ÷ duración real de la corrida. El throughput que la máquina sostuvo. |
| **`units_processed` / `units_failed` / `units_dropped`** | Cuántas unidades entraron, fallaron y se descartaron por no llegar a tiempo. El **drop%** sale de acá. |
| **`backpressure_wait_ms`** | Cuánto esperó el productor por contrapresión del consumidor. |
| **`max_staleness_observed_ms`** | Antigüedad máxima de un frame al entrar a inferencia: cuán viejo es lo que se está mirando. |
| **`gpu_memory_peak_mb`** | Pico de VRAM del proceso. Sirve para descartar la GPU como cuello de botella. |
| **`total_detections` / `detections_by_label` / `detections_by_prompt_id`** | Volumen de detecciones, desagregado por clase y por prompt. Es lo que expone que una palabra "detecta" sin detectar lo que dice (F-94.1). |
| **`capture_to_host`** | p50/p95 del tramo sensor→host (driver, red, cola). Solo en corridas OAK-D. **Queda fuera de G2A** — de ahí F-101.8. |
| **`prefilter` (EN-2)** | Bloque del preselector on-device: habilitado o no, y `dropped_no_person` — frames descartados dentro de la cámara (87% medido A/B). |

## 5. Runtime del control-plane — costo e integridad del motor

Contratos `control.metric.v1` (por unidad) y `control.summary.v1` (por corrida).

| Métrica | Qué es |
|---|---|
| **`processing_ms` / `avg_processing_ms`** | Tiempo del motor de patrones por unidad y su promedio. |
| **`processing_ms_percentiles`** | p50/p95/p99 deterministas del anterior. |
| **`ttfa_internal_ms_percentiles`** | TTFA interna (`alert_registered_ms − first_evidence_ms`): latencia del motor **sin** el media-plane. Diagnóstico, no cifra citable de sistema. |
| **`pattern_evidence_count` / `pattern_events_count` / `alerts_count`** | El embudo del motor: evidencia → eventos de patrón → alertas confirmadas. |
| **`subjects_count`** | Sujetos vistos por unidad. Es lo que la granularidad por sujeto (G1) usa como eje. |
| **`bus_dropped_events`** | Huecos de `seq` en el bus ZeroMQ. **> 0 ⇒ corrida degradada** (ADR-003); nunca se silencia. |
| **`degraded` / `degradation_causes`** | Bandera y causas de degradación de la corrida. |
| **`units_failed` / `errors_count`** | Unidades que no se pudieron procesar y errores acumulados. |

## 6. Tiempo real / EBE

| Métrica | Qué es |
|---|---|
| **G2A** (*glass-to-algorithm*) | Captura → resultado algorítmico, con p50/p95 y **presupuesto de diseño 50–250 ms**. Ojo: la estampa de "captura" es el **dequeue**, no el fotón (F-101.8) ⇒ vidrio→alerta = `capture_to_host` + G2A + política. |
| **Densidad de evidencia (fps)** | Los fps que efectivamente llegan al motor (1,15 / 2,0 / 4,29 vs 30 del banco offline). Es la variable única de las campañas de densidad. |
| **Drop rate del live** | Fracción de frames descartados por no llegar la inferencia (68–94% según modelo). |
| **CV del intervalo de descarte** | Coeficiente de variación de los huecos reales del live (0,22–0,36): mide cuán **irregular** es el descarte, y es lo que valida usar decimado regular como proxy. |
| **Deltas de confirmación contra reloj externo** | Latencia de la política medida con claqueta/reloj físico (4,1–4,6 s contra umbral de 4,0 s). Es la verificación de que el motor es puntual. |

## 7. Estadística de las comparaciones

| Métrica | Qué es |
|---|---|
| **Bootstrap pareado por clip** | Remuestreo de clips con reposición (10.000 iteraciones) recalculando el **delta de F1** entre dos campañas sobre la misma muestra. El pareo cancela la dificultad del clip. |
| **IC95 del delta** | Si **excluye el cero** ⇒ la diferencia se afirma. Si **cruza el cero** ⇒ estimación puntual: se reporta como observación, no como hallazgo. |
| **p-valor pareado** | Usado en el único caso de palanca fina (F-RT5: +18% fps, p=0,0195 con 11 pares pareados). |
| **Escala AF-1…AF-11** | No es una métrica sino el estatuto de cada afirmación: establecida / direccional / tendencia con mecanismo / no cerrada / limitación. |

## 8. Estados de aplicabilidad (acompañan a las métricas, ADR-006/013)

Vocabulario cerrado con el que una métrica declara que **no** se calculó, en vez de
aparecer como 0 o como ausencia: `computed`, `applicable_not_computed`,
`not_applicable:<causa>`, `not_interpretable`. Se usa en `pattern_evaluation`,
`ttfd_sdr_applicability` y el bloque G2A.

## 9. Métricas que la plataforma NO reporta (y por qué)

| Métrica | Estado |
|---|---|
| **FAR/hora** (`far_per_hour`) | **El código la calcula, el informe no la reporta** — limitación **L1**: con 0 eventos en T horas la cota honesta es ≈3/T, y el banco junta 0,10–0,26 h ⇒ ninguna afirmación operativa se sostiene. Se reemplaza por el control de negativos. |
| **Métricas MOT** (HOTA, DetA/AssA, IDF1, MOTA, IDSW/Frag) | **Exclusión E-10.** Lo excluido son las métricas y el GT de identidades, no la capacidad de tracking: la ganancia de la granularidad por sujeto se mide en **alertas**, porque las detecciones son bit a bit idénticas (F-89.1). |
| **COCO AP@[0.50:0.95]** | No se usa. El proyecto reporta **mAP@0.5**. Confundirlas es una trampa previsible al comparar contra literatura: son escalas distintas, no el mismo número. |
| **Doble anotación / kappa inter-anotador** | No medido — limitación **L2**, decisión declarada (un solo anotador, con 6 bordes adjudicados y firma). |
