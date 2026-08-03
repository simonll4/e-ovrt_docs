# 81 — Primera campaña DBE sobre el banco del rodaje + 3 fixes del evaluador

- **Fecha:** 2026-08-03 (misma jornada que el doc 80: GT derivado → banco
  reportable → campaña completa, en un día).
- **Qué es:** la primera ejecución del tramo **T→P** del plan maestro (doc 62)
  sobre GT temporal **humano**: los 34 clips del banco del rodaje procesados de
  punta a punta (percepción → patrón → evaluación de alertas, 5 métricas). Hasta
  hoy el Nivel B solo se había ejercitado contra el `gt_preliminary` de
  `cb_b01_p7` (retirado, doc 80 §5).
- **Estado:** campaña 34/34 sin errores (~50 min, GPU RTX 4060). Fixes del
  evaluador con TDD, control-plane **264 passed**. **Sin commitear.**

---

## 1. Marco de lectura — qué significa un número "malo" acá

**Esto es lo que se está investigando, no un examen que se aprueba o se
desaprueba.** La pregunta de la tesis (doc 09) no es "¿OVD detecta bien?" sino:
*¿qué rendimiento se puede obtener HOY, en el ámbito de la construcción civil,
con detección open-vocabulary sin entrenar — expresando las condiciones de
riesgo en lenguaje — y qué aporta la plataforma alrededor del modelo?*

Cada cifra de abajo es el rendimiento medido de UNA combinación concreta:

| Componente | Valor medido en esta campaña |
|---|---|
| Modelo | `grounding-dino/gdino-tiny-560` (campeón S1/S2, doc 64) — zero-shot, cero imágenes de este dominio en entrenamiento |
| Prompt set | `cr01_cr02_v2_short` (CONGELADO, `frozen_sha256 df81fd48…`) — `person`/`helmet`/`vest` |
| Pattern set | `cr01_cr02_v2` (CR-01 4000 ms high / CR-02 7000 ms medium) |
| Granularidad | escena (G0) — sin `track_id` |
| Camino | DBE, `stride=1` (sin límite de tasa: mide percepción+patrón, no latencia operativa — ADR-013) |
| GT | banco del rodaje, 34 clips `gt_ready` (doc 80), manifest `cef5082e…` |

Un recall de 0,40 en P7 no es "fallamos": es **el dato** — lo que esta
combinación rinde en escena multi-persona, medido con GT humano y evaluador
verificado. Cambiar un componente (prompts E-DIR/E-IND de la Fase D, modelo
`gdino-base-560`, granularidad G1) produce OTRA combinación cuyo rendimiento se
compara contra éste. Ese contraste ES el experimento.

## 2. La cadena ejecutada

```
clip.mp4 ──POST /api/runs──▶ media-plane (gdino-tiny-560, source_id=clip_id)
        ──▶ detections.jsonl ──eovrt-control replay──▶ alerts.jsonl
        ──evaluate-alerts --detections --patterns──▶ eval_<clip>.json
```

Runner: `datos/81-ciclo-rodaje-runner.py` (secuencial, guardado incremental,
reanudable; identifica el run del control por **diferencia de directorios**, no
por mtime — el mtime podía cruzar alertas de un clip con el GT de otro en
silencio). Smoke previo sobre `a_p1_c09`: P=R=F1=1,0, t_alert 4.233 ms
(= 4.000 de persistencia + 233 de TTFD — la aritmética cierra), SDR 0,924.

**Evidencia** (convención datos/95-*): `datos/81-campana-rodaje-dbe-*` —
resultados consolidados, evals por clip, control-runs completos (tar.gz),
procedencia clip→`media_run_id` (las detecciones quedan en `runs/` del
media-plane, fuente de verdad, DA-03) y el log de campaña.

## 3. Tres fixes del evaluador — hallados validando ANTES de reportar

La validación pre-campaña (formas de GT que el smoke no cubría: negativos,
CR-02, dos condiciones, dos episodios de la misma condición) y la inspección de
los primeros resultados encontraron **tres artefactos de medición** en
`evaluation/temporal.py`. Los tres **subestimaban** la plataforma. TDD (rojo →
verde), 13 tests nuevos en dos módulos; suite del control-plane **264 passed**.

### F-EV1 — Clip negativo puntuado como fracaso total
Un clip negativo con 0 alertas —comportamiento **perfecto**— salía
`P=0, R=0, F1=0` con `applicability_state="computed"`: `_safe_div(0,0)=0` sin
que nada lo señalara. Con 4 negativos sobre 34, promediar F1 por clip hundía el
agregado con 4 aciertos contados como catástrofes. Era la deuda "clip negativo
F1=0 'computed'" anotada como menor en el doc 54 — no era menor.
**Fix:** `evaluable_episodes == 0` sin censura →
`not_applicable:negative_clip_no_episodes` + warning explícito ("NO deben
promediarse; lo que sí es dato real: FP y far_per_hour").
Tests: `test_negative_clip_applicability.py` (6).

### F-EV2 — La tolerancia de bordes del GT se ignoraba
El GT declara `annotation.start_end_tolerance_ms: 500` (la incertidumbre de sus
propios bordes de episodio, escrita por `derive_clip_gt`) y el evaluador usaba
un borde inferior **duro** en `start_ms + persistencia`. El modelo detecta la
ausencia unos frames antes del límite del anotador → el motor confirma unos ms
antes del borde → el episodio contaba `missed` **y** la alerta `unexpected`:
doble castigo a una detección correcta. Medido: desvíos de −67, −100 y −433 ms
(3 clips), los tres dentro de la tolerancia declarada. Familia F-DR9.
**Fix:** la ventana de matching hereda la tolerancia del GT (ambos bordes; un GT
sin el campo conserva el borde duro — retrocompatible).

### F-EV3 — Re-confirmación con la infracción activa contada como FP
ADR-011: el motor emite en cada confirmación y "el evaluador cuenta `re_alerts`,
no los penaliza como FP" — pero solo las detectaba DENTRO de la ventana de
matching. Una segunda alerta posterior a la ventana **con el episodio todavía
abierto** (violación ocurriendo) caía a `outside_all_episode_windows` y
deflacionaba precision. Medido: 5 casos (p.ej. `a_p1_c08`: match a 7,3 s,
re-confirmación a 14,7 s, episodio activo hasta 19,9 s).
**Fix:** una alerta **posterior al match** de un episodio ya confirmado, dentro
del span del episodio (+tolerancia), es `re_alert`. **El primer intento fue
demasiado amplio y lo atraparon dos gates existentes** (una alerta *anterior* al
match es *prematura* —el motor confirmó sin acumular la persistencia— y sigue
siendo FP): el fix quedó acotado y la distinción fijada por test.
Tests: `test_matching_tolerance_and_realerts.py` (7).

**Efecto conjunto sobre datos reales** (21 clips re-evaluados en el momento):
3 episodios missed→matched, FP 9→1 en ese subconjunto. La re-evaluación es
barata: las detecciones y alertas persisten, `evaluate-alerts` es CPU
(`datos/81-reevaluar.py` re-corre los 34 en segundos).

## 4. Resultados — combinación C_rodaje (gdino-tiny-560 × v2_short × v2 × escena)

### Agregado (30 clips positivos, 35 episodios, 1 censurado → 34 evaluables)

| Métrica | Valor |
|---|---|
| Recall | **0,824** (28/34) |
| Precision | **0,757** (28/37) — 7 re_alerts NO cuentan como FP (ADR-011) |
| F1 | 0,789 |
| `t_alert-system` (medio) | 5.327 ms |
| TTFD (medio) | **168 ms** |
| SDR (medio) | 0,70 |
| **Negativos (4 clips)** | **0 falsos positivos** en 2,1 min |

FAR/hora **no se reporta** (L1: sin clips soak). Kappa **no existe** (L2:
decisión declarada). Reportar SIEMPRE con el desglose por escenario (L5).

### Por condición

| | Clips | Episodios | Recall | FP | SDR | t_alert |
|---|---|---|---|---|---|---|
| CR-01 (casco) | 25 | 28 | 0,793 | 8 | **0,805** | 4.314 ms |
| CR-02 (chaleco) | 7 | 7 | **1,000** | 1 | **0,281** | 8.572 ms |

### Por escenario (regla L5 — acá está la historia real)

| Esc. | Clips | Recall | FP | SDR | Lectura |
|---|---|---|---|---|---|
| P1 | 11 | **1,000** | 0 | 0,816 | un actor, CR-01: resuelto |
| P2 | 5 | **1,000** | 1 | **0,160** | CR-02: recall pleno con evidencia débil (F-81.1) |
| P3/P5 | 4 | (neg.) | **0** | — | control de FP limpio |
| P4 | 2 | **1,000** | 0 | 0,924 | |
| P6 | 2 | **1,000** | 0 | 0,585 | CR-01+CR-02 simultáneas, ambas |
| **P7** | 4 | **0,400** | 5 | 0,884 | multitud: límite de la granularidad de escena (F-81.2) |
| **P8** | 1 | **0,500** | 1 | 0,865 | entrada/salida (F-81.2b) |
| **P9** | 5 | **0,600** | 2 | 0,749 | pre-roll frágil (F-81.2b) |

Los 6 missed y 8 de los 9 FP se concentran en P7/P8/P9. En P1/P2/P4/P6
(21 clips, 23 episodios): **recall 1,000 con 1 FP**.

## 5. Hallazgos

### F-81.1 — La histéresis del motor rescata una percepción intermitente (CR-02)
SDR de chaleco 0,281 vs 0,805 de casco (en P2 puro: 0,160 — factor 5). La
evidencia `spatial_absence(vest)` aparece en ~1 de cada 6 frames del episodio
(la sobre-marca de vest de F-G2.1, ahora medida de punta a punta). **Y aun así
recall CR-02 = 1,000**: el motor acumula evidencia intermitente hasta confirmar,
pagando tiempo — t_alert 8.572 ms vs 4.314 de CR-01 (~2,6 s sobre el umbral de
7 s, contra ~0,3 s de holgura en CR-01). **Argumento A-favor-de-plataforma
medido:** el detector solo no sostendría CR-02; el patrón temporal encima sí.
También define el techo actual: con SDR ~0,16, alargar la persistencia o exigir
continuidad estricta rompería CR-02.

### F-81.2 — Dónde se rompe la combinación actual: multitud y pre-roll
Los missed de P7/P8/P9 tienen dos mecanismos, **ninguno es un bug** (verificados
alerta por alerta contra el GT):

- **(a) Granularidad de escena vs GT por sujeto** (P7, multitud ~10+): el GT
  exige que UN sujeto sostenga la violación 4 s (regla C1 de `derive_clip_gt`);
  el motor a nivel escena acumula "alguien sin casco", y en multitud los sujetos
  se relevan → alerta temprana que cae fuera de la ventana del episodio + FP de
  CR-02 sin episodio CR-02 en el GT. Es la asimetría C1/ADR-012 apareciendo en
  datos reales — el costo medido de operar sin `track_id` (G0). La comparación
  G1 (`subject`) contra estos mismos clips es exactamente el experimento que el
  doc 79 dejó scopeado.
- **(b) Mis-detección en el pre-roll** (`a_p7_c01`, `a_p9_c06`, `a_p9_c08`): el
  GT marca los primeros ~3 s como *cumple* (persona CON casco) y el modelo no
  ve el casco ahí → confirma 0,7–2,4 s ANTES del inicio del episodio (más allá
  de la tolerancia de 500 ms) → doble castigo missed+FP. Es percepción: el
  casco a esa distancia/ángulo no se detecta de forma estable. Candidato a
  mejorar por prompts (Fase D) o modelo (`gdino-base-560`, especialista
  CR-01/bare_head — doc 64).

### F-81.3 — La percepción es rápida cuando ve: TTFD 168 ms
El TTFD medio (primer frame con evidencia desde el onset) es de ~5 frames. La
latencia hasta la alerta es esencialmente la persistencia del patrón (t_alert ≈
persistencia + TTFD + intermitencia). En CR-01, t_alert medio 4.314 ≈ 4.000 +
314. El "costo de decisión" de la plataforma es la política, no la percepción.

## 6. Qué habilita

- **Fase D (E-DIR vs E-IND, doc 76)**: mismo banco, mismo pipeline, otros prompt
  sets congelados — la comparación es directa contra esta línea de base.
- **Comparación de modelos** sobre video (gdino-base-560 en P7/P9, donde el doc
  64 lo señala especialista CR-01).
- **G0 vs G1** sobre los clips P7 (doc 79) — el costo de escena quedó medido.
- **Lote de internet** (cuando salga de CVAT): misma cadena, un comando; aporta
  soak → FAR/hora, y material no guionado (L4).

Pendiente inmediato: commits (control-plane: fixes+tests; datasets: splitter,
adjudicador, banco; docs: 80/81+datos) — los arma el usuario cuando lo pida.
