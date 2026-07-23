# 61 — Benchmark realtime persona-only: matriz modelo × fuente live (2026-07-23)

**Objetivo:** barrer todas las combinaciones viables de modelo OVD × fuente live (RTSP EZVIZ,
OAK-D Pro PoE) detectando solo `person`, con GPU dedicada (pendiente explícito del dry-run
tramo 2, doc 60 §8), y decidir el mejor equilibrio realtime ↔ detección.

**Condiciones:** RTX 4060 Laptop 8 GB **sin contención** (646 MiB base, 0 procesos de cómputo
ajenos; no hizo falta cerrar nada). 24 corridas = 6 modelos × 2 fuentes × 2 repeticiones,
`max_units=60`, `warmup_frames` 15 (RTSP) / 30 (OAK-D), prompts inline `person` únicamente,
sin bus ni control-plane (person-only no dispara CR-01/CR-02; las métricas salen del
`summary.json` del media-plane). **24/24 `succeeded`.** Harness y crudos:
`bench_realtime.py` + `bench_results.jsonl` (scratchpad de la sesión; runs en
`e-ovrt_media-plane/runs/run_20260723_*`).

## Matriz y exclusiones

| Familia | Variantes corridas | Excluidos y por qué |
|---|---|---|
| Grounding DINO (HF) | `gdino-tiny`, `gdino-base` | **GDINO 1.5/1.6: NO viable local** — son modelos API-only de IDEA (DeepDataSpace, cloud pago); no hay pesos abiertos. |
| MM-Grounding-DINO | — | Descartado en Sprint 2 (bboxes rotas), se mantiene la exclusión. |
| YOLOE-26 | `26s`, `26m`, `26l`, `26x` | — |

## Resultados (por corrida)

proc/drop sobre 60 unidades; `inf_p50` = latencia de inferencia p50 (ms); `g2a` = captura→resultado (ms);
`u_pers` = unidades con ≥1 persona; `conf` = confianza media; `vram` = pico del proceso (MB).

| modelo | fuente | rep | proc/drop | fps_eff | inf_p50 | g2a_p50 | g2a_p95 | u_pers | conf | vram |
|---|---|---|---|---|---|---|---|---|---|---|
| yoloe-26s | rtsp | 1 | 10/50 | 1.59 | 37.9 | 100.3 | 3350.5 | 10 | 0.886 | 369 |
| yoloe-26s | rtsp | 2 | 44/16 | 7.00 | 28.6 | 35.6 | 164.6 | 44 | 0.898 | 142 |
| yoloe-26s | oak_d | 1 | 54/6 | 2.67 | 27.9 | 32.9 | 224.6 | 54 | 0.899 | 141 |
| yoloe-26s | oak_d | 2 | 55/5 | 2.26 | 40.9 | 46.1 | 308.1 | 55 | 0.831 | 141 |
| yoloe-26m | rtsp | 1 | 27/33 | 4.30 | 26.1 | 31.8 | 201.5 | 27 | 0.905 | 436 |
| yoloe-26m | rtsp | 2 | 49/11 | 7.82 | 30.4 | 36.2 | 201.4 | 49 | 0.890 | 210 |
| yoloe-26m | oak_d | 1 | 52/8 | 2.68 | 41.2 | 49.2 | 215.5 | 52 | 0.907 | 210 |
| yoloe-26m | oak_d | 2 | 53/7 | 2.20 | 33.2 | 39.9 | 228.1 | 53 | 0.905 | 210 |
| yoloe-26l | rtsp | 1 | 20/40 | 3.18 | 32.8 | 37.6 | 2777.6 | 20 | 0.886 | 453 |
| yoloe-26l | rtsp | 2 | 49/11 | 7.84 | 32.8 | 38.0 | 181.1 | 49 | 0.888 | 218 |
| yoloe-26l | oak_d | 1 | 54/6 | 2.72 | 38.3 | 43.9 | 212.3 | 54 | 0.896 | 218 |
| yoloe-26l | oak_d | 2 | 53/7 | 2.26 | 38.9 | 47.8 | 170.1 | 53 | 0.867 | 218 |
| yoloe-26x | rtsp | 1 | 17/43 | 2.70 | 41.7 | 55.1 | 2929.4 | 17 | 0.910 | 615 |
| yoloe-26x | rtsp | 2 | 46/14 | 7.25 | 40.6 | 52.2 | 142.8 | 46 | 0.907 | 336 |
| yoloe-26x | oak_d | 1 | 53/7 | 2.66 | 44.0 | 49.6 | 186.2 | 53 | 0.883 | 337 |
| yoloe-26x | oak_d | 2 | 53/7 | 2.20 | 40.0 | 45.2 | 228.3 | 53 | 0.868 | 336 |
| gdino-tiny | rtsp | 1 | 20/40 | 2.99 | 197.7 | 319.6 | 592.9 | 20 | 0.879 | 1741 |
| gdino-tiny | rtsp | 2 | 19/41 | 2.81 | 219.2 | 311.0 | 596.1 | 19 | 0.889 | 1741 |
| gdino-tiny | oak_d | 1 | 30/30 | 1.52 | 203.3 | 337.9 | 494.1 | 30 | 0.890 | 1741 |
| gdino-tiny | oak_d | 2 | 30/30 | 1.27 | 198.3 | 352.2 | 445.8 | 30 | 0.893 | 1741 |
| gdino-base | rtsp | 1 | 19/41 | 2.81 | 218.6 | 354.6 | 571.9 | 19 | 0.816 | 2102 |
| gdino-base | rtsp | 2 | 19/41 | 2.78 | 225.6 | 327.6 | 577.9 | 19 | 0.801 | 2102 |
| gdino-base | oak_d | 1 | 27/33 | 1.39 | 225.2 | 388.4 | 614.0 | 27 | 0.789 | 2102 |
| gdino-base | oak_d | 2 | 27/33 | 1.09 | 224.2 | 383.8 | 456.5 | 27 | 0.789 | 2102 |

VRAM total de servicio cargado (nvidia-smi): YOLOE ~0.9–1.2 GB; gdino-tiny 2.7 GB; gdino-base 3.2 GB.
Todos caben con holgura en los 8 GB; nunca hubo presión de VRAM.

## Hallazgos

1. **RESUELTO el misterio del 20× del dry-run (doc 60 / memoria 07-22).** La corrida
   lenta es **siempre la primera tras levantar el servicio** (RTSP r1 en los 4 YOLOE:
   g2a_p95 de 2.8–3.4 s, fps 1.6–4.3; r2 idéntica config: 7.0–7.8 fps, g2a_p50 ~36 ms).
   Causa: **warm-up de kernels CUDA a la resolución real** — el warmup del adaptador usa un
   dummy que no representa el primer frame 1080p; las primeras inferencias reales pagan
   autotuning, generan backlog y drops. Las corridas OAK-D r1 NO lo sufren porque llegan
   después de las RTSP (modelo ya caliente). La "corrida A vs B" del dry-run (7870 → 332 ms)
   era exactamente esto, no varianza aleatoria. **Acción sugerida:** warmup del adaptador con
   frame sintético a resolución de producción, o descartar la primera corrida post-arranque.
2. **YOLOE cumple el presupuesto G2A (50–250 ms); GDINO no.** En caliente, YOLOE-26 (todas
   las tallas) da g2a_p50 33–52 ms y p95 143–308 ms. GDINO-tiny/base: p50 311–388 ms,
   p95 446–614 ms — **fuera de presupuesto siempre**, en ambas fuentes.
3. **Throughput en caliente (RTSP 15 fps):** YOLOE procesa 44–49/60 frames (7.0–7.8 fps
   efectivos, ~la mitad del stream); GDINO procesa 19–20/60 (~2.8 fps). La inferencia YOLOE
   (26–44 ms) es 5–7× más rápida que GDINO (198–226 ms), consistente con G-E2.
4. **La talla de YOLOE casi no cambia la latencia** (26s→26x: p50 28→42 ms) porque a 640 px
   el costo está dominado por pre/post y transferencia, no por el backbone. Elegir talla por
   calidad de detección, no por velocidad.
5. **OAK-D entrega ~2.5–3 fps efectivos constantes entre modelos** (60 unidades en ~20–24 s,
   incluido el connect de ~9 s), aun con inferencia de 30 ms ⇒ el cuello es la **fuente**
   (pacing/cola del OakDSource), no el modelo. Abierto para investigar si el rodaje EBE
   necesita más tasa de la OAK-D; para el banco actual alcanza.
6. **Detección (proxy, sin GT):** persona detectada en el 100% de las unidades procesadas
   por TODOS los modelos; confianzas YOLOE 0.83–0.91, gdino-tiny ~0.89, gdino-base 0.79–0.82
   (la más baja). Person-only no discrimina calidad entre familias — para vocabulario EPP
   completo sigue valiendo el BENCH v2 (Sprint 2: GDINO-tiny mejor mAP; YOLOE sin
   vest/bare_head).

## Veredicto: mejor equilibrio realtime ↔ detección

**Ganador para live person-only: `yoloe/yoloe-26m` o `yoloe-26l`** — g2a_p50 ~32–49 ms
(dentro de presupuesto con margen), 7.8 fps efectivos sobre RTSP, confianza ~0.89–0.91,
~210–220 MB de VRAM. `26x` no aporta (misma detección, +40% latencia); `26s` mostró la
confianza más inestable (0.83 en una corrida). Entre 26m y 26l: empate técnico en este
proxy; desempatar con el BENCH v2 si se quiere una sola.

**GDINO queda para el carril de detección EPP (DBE/offline o live asumiendo ~0.3–0.4 s de
g2a):** es el único con vocabulario EPP completo probado (helmet/vest/bare_head), pero no
entra en el presupuesto G2A live. Para el protocolo de doble toma del rodaje (doc 59 §7)
esto no lo invalida — la toma live con GDINO-tiny sigue siendo evaluable, solo que con
t_capture→alert ~0.35 s por encima del piso YOLOE.

**Implicación para la tesis (E-HYB):** estos números refuerzan la pista doble del doc 12 §3
— YOLOE como réplica rápida / GDINO-tiny como primaria de calidad — y cuantifican el trade:
**5–7× de latencia por el vocabulario abierto completo.**

## Adenda 2026-07-23: mejoras aplicadas (misma sesión, todo TDD, sin commitear)

1. **`prepare_run` (media-plane).** El hallazgo 1 se re-diagnosticó con los artefactos: la
   primera inferencia de CADA corrida pagaba el binding lazy de prompts (`set_classes` de
   YOLOE: text encoder fp32 + round-trip float→half, ~1.1 s en corrida caliente, 3.3 s en
   fría con autotune CUDA) **con la fuente ya produciendo** → 16–50 drops por `queue_full`.
   Fix: `BaseDetectorAdapter.prepare_run(plan)` (inferencia dummy con el plan REAL) llamado
   por `execute_run` ANTES de arrancar el productor. **Verificado en hardware:** yoloe-26m ×
   RTSP primera corrida pasó de 10–27 proc / 33–50 drops a **60/0**, frame 0 de 3350 → 101 ms,
   7.0 fps ya en la primera corrida. Tests: `tests/test_prepare_run.py`.
2. **fp16: verificado OK** — `runtime.half_precision=True` llega a ambos adaptadores desde el
   catálogo; los números del benchmark ya son con fp16. Sin cambio.
3. **Rate control: el hallazgo 3 se CORRIGE** — el loader ya deriva `bounded_freshness`
   (ring de 2, evict-oldest) para toda fuente live; los drops `queue_full` en live son
   evicciones manteniendo el frame más fresco (comportamiento deseado), no backlog. `stride`
   queda como knob deliberado. Sin cambio.
4. **Cache de embeddings de texto GDINO: DESCARTADA con profile** — el processor completo
   (resize+normalize+tokenize CPU) son 28 ms de los ~283; el text encoder es una fracción
   menor con captions cortos. La cirugía sobre el forward de HF no se justifica.
5. **`image_size` para GDINO + catálogo `grounding-dino/gdino-tiny-560`** (nuevo). El knob
   existía en `ModelSection` (lo usaba YOLOE) pero GDINO lo ignoraba; ahora `input_spec` y
   `predict` (processor `size=`) lo honran consistentemente. **Medido live RTSP:** inferencia
   p50 205 → 156 ms (−24 %), 21 → 27 frames procesados de 60 (+30 %); en 6 imágenes CHV el
   conteo de personas es idéntico a 800 (conf ±0.08). `gdino-tiny` (800) queda intacto para
   comparabilidad con el BENCH v2; validar EPP completo en el banco antes de usar 560 fuera
   de person-only.
6. **OAK-D:** el techo era en gran parte el default `fps: 10` de la config (el poll del host
   es de 10 ms, inocente). Con `ingest.config.fps: 30` el sensor entrega ~12,7 fps reales
   (inter-arrival p50 78,9 ms; mínimo 61 ms ⇒ tope por exposición con la luz actual) y
   g2a_p95 cae a 59–95 ms. Preset local `cameras/oak_d_lab.yaml` actualizado con `fps: 30`.
   **Follow-up abierto:** el connect de ~9 s se paga por corrida (keep-alive del device entre
   runs = cambio arquitectural); `fps_effective` del summary queda deflactado por
   connect+warmup en fuentes live (sesgo de métrica, no de pipeline).
7. **E-HYB en cascada (YOLOE gate + GDINO en frames con persona): NO aplicada** — es una
   decisión de diseño de la tesis, queda propuesta.

Estado tras la adenda: media-plane **635 passed**, ruff limpio. Nota de escena: en las
corridas GDINO de la adenda no había persona frente a la cámara RTSP (0 detecciones en 800 y
560 por igual); la validación de detección se hizo con imágenes CHV del banco.

## Cierre 2026-07-23: decisiones asentadas

**D-61.1 — Cascada E-HYB (YOLOE gate + GDINO condicional): DESCARTADA para la tesis.**
Justificación: (a) las condiciones de riesgo son *sostenidas* por diseño — CR-01 confirma a
4000 ms y CR-02 a 7000 ms, así que GDINO-tiny a ~3–4 fps muestrea un episodio evaluable ~12+
veces antes de confirmar: el motor no necesita todos los frames, necesita suficientes; (b) en
la latencia de alerta punta a punta (~4,3 s) el g2a de GDINO es ~7% — la cascada optimiza el
término chico; (c) toda etapa de filtrado vuelve el recall **multiplicativo**
(`recall_gate × recall_GDINO`) e introduce el modo de fallo "falso cumplimiento" (P9) sin
caracterizar; (d) ADR-001 ya dejó E-HYB en Fase 2. Queda como **trabajo futuro cuantificado**
en la defensa, con el trade 5–7× de este doc como respaldo. Cero código.

**D-61.2 — Prefilter EN-2 on-device (OAK-D): APAGADO en todo lo evaluativo.** Banco, rodaje
DBE, tomas live del protocolo doble y soak de FAR/hora corren SIN prefilter. Justificación:
misma trampa multiplicativa de D-61.1 con un detector más débil (VPU de la cámara), y además
**un filtro de frames vacíos suprime las falsas detecciones sostenidas que son el insumo de
FAR/hora** (hallazgo A7: la sobre-marca de `bare_head` es lo que FAR mide) — lo invalidaría o
cambiaría su provenance. EN-2 queda para usos no evaluativos: posicionamiento, previews, demos.

**D-61.3 — Carril live: GDINO-tiny directo, sin etapas intermedias.** Con las mejoras de la
adenda (pre-flight `prepare_run`, `fps: 30` en la OAK-D) el carril cumple lo que exige el
protocolo del doc 59 §7. La protección contra "perder situaciones de riesgo" no es más
arquitectura: son las condiciones sostenidas (toleran muestreo ralo), el ledger
`dropped_units.jsonl`, el `bus_dropped_events` que nunca se silencia, y el BENCH midiendo el
recall del detector.

**D-61.4 — `gdino-tiny-560` VALIDADA en BENCH v2 test (82 imgs): el caveat de la mejora 5 se
cierra.** Corridas `run_20260723_020952` (800) vs `run_20260723_021021` (560), crudos en
`datos/bench_v2_gdino560_eval_2026-07-23.json`:

| métrica | gdino-tiny (800) | gdino-tiny-560 |
|---|---|---|
| mAP50 | 0.4197 | **0.4474** |
| recall CR-01 | 0.3659 | **0.4146** |
| AP50 person | 0.6179 | **0.6813** |
| AP50 helmet | **0.7955** | 0.7780 |
| AP50 vest | 0.2351 | **0.2395** |
| AP50 bare_head | 0.0303 | **0.0909** |

560 iguala o mejora en todo salvo helmet (−0.02): **sin pérdida EPP y −24% de latencia**. Es
apta como referencia del carril live sin restricción a person-only. Nota: emite más
detecciones (n_det person 172 vs 138, bare_head 65 vs 39) — el AP ya descuenta la precisión,
pero para FAR/hora en fase C declarar qué variante corre (provenance), porque la tasa de
falsos sostenidos puede diferir entre 800 y 560.

Cierre verificado: media-plane 635 passed + ruff limpio, GPU y puertos liberados, crudos de
todas las corridas archivados en `datos/`. Todo sin commitear (regla vigente).
