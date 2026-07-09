# Benchmark de modelos OVD en el host local — GDINO y YOLOE

- **Fecha de ejecución:** 2026-07-09
- **Propósito:** medir, en el host de desarrollo, el compromiso entre **calidad de
  detección** (BENCH v2 val, con GT) y **rendimiento en tiempo real** (cámara RTSP en
  vivo) para las 6 variantes de GDINO y YOLOE disponibles.
- **Datos crudos:** `datos/31-benchmark-modelos-host-local.datos.json`
- **Script reproducible:** `datos/31-benchmark-modelos-host-local.driver.py`
- **Alcance:** este documento mide **modelos zero-shot sin fine-tuning** (E-04 sigue
  excluido, ver doc 10). No decide D1 — es insumo para el pre-registro del doc 04.

---

## 1. Resumen ejecutivo

Cuatro hallazgos, en orden de impacto sobre las decisiones abiertas:

1. **YOLOE es ciego a `bare_head`.** Las cuatro variantes emiten entre 0 y 1 detección de
   `bare_head` sobre 69 instancias de GT. Su recall CR-01 es 0.000–0.014. Como CR-01
   ("persona sin casco") se materializa por la estrategia E1 (detectar `bare_head`),
   **ninguna variante de YOLOE puede sostener CR-01 tal como está definida hoy**. Este es
   el resultado más consecuente del benchmark.
2. **El mAP oculta lo que importa para la tesis.** GDINO-tiny gana en mAP@0.5 (0.458 vs
   0.409), pero **GDINO-base gana donde cuenta**: recall CR-01 de 0.586 vs 0.443
   (+32 % relativo) y AP de `vest` de 0.467 vs 0.296 (+58 % relativo). Elegir por mAP
   llevaría a la decisión equivocada para el objetivo de seguridad.
3. **Solo YOLOE sostiene la cámara en tiempo real.** Frente a un stream de ~10 fps, YOLOE
   procesa 58–69 % de los frames; GDINO, 14–22 %. La política `bounded_freshness` descarta
   el resto (comportamiento correcto, no un fallo).
4. **Escalar el modelo no mejora la calidad de forma monótona.** En YOLOE, 26m (0.334) es
   *peor* que 26s (0.380), y 26x (0.424) supera a 26l (0.375). En GDINO, base es peor que
   tiny en mAP. Más parámetros no compran calidad en este dominio zero-shot.

**Consecuencia práctica:** hay un conflicto duro entre CR-01 y tiempo real. Los únicos
modelos capaces de CR-01 (GDINO) son los que no siguen el ritmo de la cámara. Ver §6.

---

## 2. Host y versiones

| Componente | Valor |
|---|---|
| GPU | NVIDIA GeForce RTX 4060 Laptop, 8188 MiB, driver 610.47 |
| CPU | AMD Ryzen 7 7735HS (16 hilos) |
| RAM | 7.4 GiB |
| SO | WSL2, kernel 6.6.114.1-microsoft-standard |
| Python / Torch | 3.12.13 / 2.12.1+cu130 (CUDA 13.0) |
| `code_version` | `96fe720` (+ 17 archivos modificados sin commitear) |

Todos los modelos corrieron en `cuda`, con `half_precision: true` y `warmup: true`.

## 3. Metodología

**Aislamiento.** Cada modelo se midió en un **proceso de servicio propio**
(`EOVRT_MODEL_REF=<ref>`, levantar → medir → bajar). Esto evita que la VRAM o los cachés de
un modelo contaminen al siguiente, y permite medir el tiempo de carga limpio.

**Prompt set congelado.** Los 6 modelos usaron el mismo `cr01_cr02_bench_v2` (etiquetas
cortas `person` / `helmet` / `vest` / `bare head`), marcado como *NO modificar* por
reproducibilidad. `active_ids` = las 4 clases.

**Suite A — BENCH v2 val (determinista).** 114 imágenes de obra con GT canonical_v2.
Métricas: AP@0.5 por clase, mAP@0.5, recall CR-01, latencia, VRAM. La evaluación corre por
`POST /api/runs/{id}/evaluate`, que restringe el GT a las imágenes efectivamente procesadas
(el COCO del BENCH cubre val+test; sin restringir, el AP se deflacta artificialmente).

**Suite B — Cámara RTSP en vivo.** 100 unidades pedidas a una cámara IP de la LAN
(1920×1080, ~10 fps). Mide **capacidad de tiempo real**, no calidad: la escena no contiene
EPP, así que las detecciones de esta suite no son interpretables como acierto o error.

**VRAM.** `torch.cuda.max_memory_allocated()`, reiniciado al inicio de cada corrida
(`pipeline.py:433`), por lo que el pico es por corrida y no acumulado entre suites.

## 4. Resultados — Suite A: BENCH v2 val (114 imgs, con GT)

Ordenado por mAP@0.5. En negrita el mejor de cada columna.

| Modelo | mAP@0.5 | AP person | AP helmet | AP vest | AP bare_head | **recall CR-01** | p50 lat. | fps | VRAM pico |
|---|---|---|---|---|---|---|---|---|---|
| gdino-tiny | **0.4577** | 0.7167 | 0.7977 | 0.2960 | **0.0202** | 0.4429 | 233 ms | 3.99 | 1747 MB |
| yoloe-26x | 0.4239 | 0.7147 | **0.7989** | 0.1818 | 0.0000 | 0.0000 | 50 ms | 11.47 | 619 MB |
| gdino-base | 0.4093 | 0.6346 | 0.5276 | **0.4674** | 0.0076 | **0.5857** | 242 ms | 3.98 | 2109 MB |
| yoloe-26s | 0.3797 | 0.6289 | 0.6171 | 0.2727 | 0.0000 | 0.0143 | 39 ms | 10.77 | 373 MB |
| yoloe-26l | 0.3749 | 0.7128 | 0.6199 | 0.1667 | 0.0000 | 0.0000 | 44 ms | 11.42 | 457 MB |
| yoloe-26m | 0.3341 | 0.6355 | 0.6101 | 0.0909 | 0.0000 | 0.0000 | 36 ms | 15.74 | 440 MB |

**Detecciones propuestas por clase** (`n_det`), contra el GT `person`=166, `helmet`=79,
`vest`=41, `bare_head`=69. Esta tabla explica los AP de arriba mejor que el AP mismo:

| Modelo | person | helmet | vest | bare_head |
|---|---|---|---|---|
| gdino-tiny | 151 | 73 | 77 | 67 |
| gdino-base | 118 | 74 | 45 | 73 |
| yoloe-26s | 132 | 53 | 10 | **1** |
| yoloe-26m | 133 | 56 | 2 | **0** |
| yoloe-26l | 137 | 56 | 6 | **0** |
| yoloe-26x | 139 | 69 | 6 | **0** |

YOLOE no "falla" en `bare_head`: **no propone el concepto en absoluto**. Con 0 detecciones,
el AP no es un puntaje bajo, es una ausencia. Lo mismo, atenuado, con `vest` (2–10
propuestas para 41 instancias). GDINO propone las 4 clases en volumen razonable.

**Cross-check con Sprint 2.** El baseline registrado para GDINO-tiny en BENCH val era
mAP@0.5 = 0.441; acá dio 0.4577 con fp16 + warmup. Consistente con el gate documentado en
`configs/runs/local/gdino_bench_v2_val_fp16.yaml`, que buscaba justamente confirmar que
`half_precision` no introduce regresión. No hay regresión.

## 5. Resultados — Suite B: cámara RTSP en vivo (100 units, ~10 fps)

`keep-up` = fracción del stream efectivamente procesada. El resto lo descarta
`bounded_freshness` para preservar actualidad en vez de acumular cola.

| Modelo | procesados | descartados | **keep-up** | p50 lat. | fps efectivo | VRAM pico |
|---|---|---|---|---|---|---|
| yoloe-26l | 69 | 31 | **69 %** | 49 ms | 8.60 | 218 MB |
| yoloe-26m | 63 | 37 | 63 % | 39 ms | 7.78 | 210 MB |
| yoloe-26x | 63 | 37 | 63 % | 46 ms | 7.83 | 337 MB |
| yoloe-26s | 58 | 42 | 58 % | 35 ms | 7.17 | 142 MB |
| gdino-tiny | 22 | 78 | 22 % | 250 ms | 2.60 | 1747 MB |
| gdino-base | 14 | 86 | **14 %** | 377 ms | 1.64 | 2109 MB |

`max_staleness_observed_ms` fue 0.0 en las seis corridas: la política nunca entregó un
frame obsoleto al detector. El descarte es el mecanismo funcionando, no degradación.

**Tiempo de carga del modelo** (arranque del servicio hasta `/readyz`, incluye ~2 s de
uvicorn): gdino-base 18 s, gdino-tiny 20 s, yoloe-26s 19 s, yoloe-26m 24 s, yoloe-26l 25 s,
**yoloe-26x 54 s**. Relevante para el reinicio de instancias en la consola.

## 6. Lectura: el conflicto CR-01 ↔ tiempo real

Cruzando ambas suites, los modelos se parten en dos grupos disjuntos:

| | Capaz de CR-01 (`bare_head`) | Sostiene ~10 fps |
|---|---|---|
| **GDINO** (tiny, base) | Sí (recall 0.44–0.59) | No (14–22 % keep-up) |
| **YOLOE** (26s/m/l/x) | **No** (recall ≈ 0) | Sí (58–69 % keep-up) |

No hay un modelo que haga las dos cosas. Las salidas posibles, sin fine-tuning:

- **Aceptar el descarte.** Con GDINO-tiny a 2.6 fps efectivos, un evento de riesgo que dure
  ≥ 3 s (PR-01: ventana alta 3–5 s) es observado ~8 veces. El descarte no impide detectar
  la condición; reduce la resolución temporal. Esta es probablemente la respuesta correcta
  y hay que **medirla explícitamente** contra el TTFD del doc 08, no asumirla.
- **Bajar la resolución de entrada de GDINO** para subir su fps. No probado acá.
- **Replantear la materialización de CR-01** para no depender de `bare_head` (p. ej.
  `person` ∧ ¬`helmet` por solapamiento). Esto cambia D1/D2 y toca al control-plane; es la
  ruta que YOLOE haría viable, y hoy no está evaluada.

**Si CR-01 sigue anclada a `bare_head`, YOLOE queda fuera del núcleo**, con independencia de
su velocidad. Vale registrarlo antes de correr el experimento del doc 04.

## 7. Limitaciones — leer antes de citar estos números

1. **Los umbrales no son homogéneos entre variantes de GDINO.** `gdino-tiny` usa
   `box_threshold=0.35` y `gdino-base` `0.30` (defaults del catálogo,
   `configs/models/grounding-dino/*.yaml`). La comparación tiny-vs-base está **confundida
   por ese parámetro**: no se puede atribuir la diferencia de mAP solo a la capacidad del
   modelo. Para cerrar D1 hay que re-correr con umbral homogéneo o barrer el umbral.
2. **n = 1 por modelo.** Una corrida por suite, sin repeticiones. No hay intervalos de
   confianza; las latencias son una muestra, no una distribución estimada.
3. **`avg_latency_ms` está contaminado por el primer frame** (carga de cachés CUDA). En
   YOLOE-26s el promedio (91 ms) supera al p95 (56 ms). **Usar p50, no el promedio.**
   Igual criterio para el p99 de la suite RTSP (~1.5 s en YOLOE): es el frame de apertura
   del stream.
4. **La suite RTSP no mide calidad.** La cámara apunta a una escena doméstica sin EPP. Solo
   es válida para keep-up, latencia y VRAM.
5. **Laptop bajo WSL2.** GPU móvil sujeta a throttling térmico y overhead de virtualización;
   los valores absolutos de fps no trasladan a la GPU de despliegue.
6. **114 imágenes** (split val). El BENCH completo son 196 (val+test). Falta `bench_v2_test`.
7. **MM-GDINO quedó fuera** deliberadamente: descartado en Sprint 2 por bboxes rotos.

## 8. Reproducir

```bash
cd e-ovrt_media-plane
# requiere configs/runs/local/rtsp_camera.env (gitignored) para la suite RTSP
.venv/bin/python ../docs/operacion/datos/31-benchmark-modelos-host-local.driver.py
```

El script levanta y baja un servicio por modelo, corre ambas suites y escribe el JSON
crudo. Los artefactos de cada corrida quedan en `e-ovrt_media-plane/runs/<run_id>/`
(gitignored). `run_id` de cada medición, para trazabilidad:

| Modelo | run BENCH | run RTSP |
|---|---|---|
| gdino-tiny | `run_20260709_163954_dbe_grounding_dino_051ede` | `run_20260709_164024_dbe_grounding_dino_db6145` |
| gdino-base | `run_20260709_164055_dbe_grounding_dino_6d555e` | `run_20260709_164125_dbe_grounding_dino_3040fc` |
| yoloe-26s | `run_20260709_164157_dbe_yoloe_63052a` | `run_20260709_164207_dbe_yoloe_4b28de` |
| yoloe-26m | `run_20260709_164244_dbe_yoloe_248407` | `run_20260709_164252_dbe_yoloe_00392c` |
| yoloe-26l | `run_20260709_164330_dbe_yoloe_574ee2` | `run_20260709_164340_dbe_yoloe_ca8815` |
| yoloe-26x | `run_20260709_164447_dbe_yoloe_a15cbe` | `run_20260709_164457_dbe_yoloe_58dc6d` |

## 9. Próximos pasos sugeridos

1. **Re-correr GDINO tiny vs base con umbral homogéneo** (limitación 1). Sin esto, la
   comparación intra-familia no es concluyente.
2. **Completar con `bench_v2_test`** (82 imgs) para cubrir el BENCH entero.
3. **Medir TTFD real bajo `bounded_freshness`** con GDINO-tiny sobre un clip con GT
   temporal: convertir el "22 % keep-up" en una afirmación sobre latencia de alerta
   (métricas del doc 08), que es lo que la tesis necesita defender.
4. **Decidir si CR-01 sigue atada a `bare_head`** antes del experimento del doc 04: la
   respuesta determina si YOLOE entra o no al espacio de búsqueda.
