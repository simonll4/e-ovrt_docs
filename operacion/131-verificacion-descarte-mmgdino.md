# 131 — Verificación experimental del descarte de MM-GDINO (2026-09-01)

**Por qué existe este doc.** Antes de escribir la justificación de T3 en el informe, el
usuario preguntó por la frase *"MM-GDINO-tiny se descartó en Sprint 2 por bboxes
geométricamente inválidas"*: **¿de eso estamos completamente seguros?** La respuesta
honesta era "no": la cadena documental tenía **tres versiones de la causa** que no podían
ser ciertas a la vez — el registro de Sprint 2 la atribuía a un bug de un adaptador propio
(`mmgdino_adapter.py`, "x2 colapsa"), `operacion/117` §2 decía "causa nunca diagnosticada",
y el hallazgo 5 de `operacion/64` decía que `large` "reproduce el bug" de la `tiny`. Se
verificó por experimento el 2026-09-01. **Veredicto: el descarte queda MÁS firme que antes,
pero con la causa corregida** — el defecto es del checkpoint publicado, no del proyecto.

Restricción respetada: **nada de esto tocó `bench_v3`** (acta `128` §5 intacta — no es un
brazo nuevo; es diagnóstico de geometría sobre imágenes raw, sin métrica contra GT).

## 1. Prueba A — artefactos crudos de S1 (2026-07-23), sin computar nada

Los `detections.jsonl` de las cuatro sondas MM-GDINO sobreviven en `media-plane/runs/`.
Son **la medición misma que tabula `results/bench_imagenes/index.md`**: los pares
test/valid de BENCH v2 (82 + 114 = 196 imgs de `raw/construction_site_safety`).

| run | ckpt | split | imgs | mAP50 | cajas | `person` w/h (med) | degeneradas (lado ≤1 px) |
|---|---|---|---|---|---|---|---|
| `run_20260723_023804…a07093` | base | test | 82 | 0,3361 | 374 | 0,34 | 0 |
| `run_20260723_023824…50e7a4` | base | valid | — | 0,3766 | 356 | 0,52 | 0 |
| `run_20260723_023904…173aa4` | large | test | 82 | **0,0025** | 195 | **1,74** | 0 |
| `run_20260723_024014…0bd288` | large | valid | 114 | **0,0273** | 242 | **1,72** | 0 |

(El "0,017" del índice ↔ el rango 0,0025–0,0273 de estos dos runs; el "0,360" de base ↔
0,3361/0,3766.)

Lectura: `large` colapsa **sin cajas degeneradas** — sus cajas tienen tamaño plausible
(mediana ~115×55 px, ~2–3 % del área) pero están **mal ubicadas y apaisadas** (una `person`
parada es vertical: base da w/h 0,34–0,52; large da 1,72–1,74). Se descartó que fueran una
transformación recuperable de cajas correctas, midiendo IoU contra las cajas de base en las
mismas imágenes: identidad 0,12 · swap x↔y 0,084 · cxcywh-leído-como-xyxy 0,214 — ninguna
alinea.

Reconciliación con el sanity-check del doc 64: con umbral **lado mínimo ≤3 px** salen
**1–2** casi-degeneradas por run (≤5 px: 3–5; base: 0 con cualquier umbral). **El conteo
"2–3 degeneradas" era honesto**; lo que no se sostiene es usarlas como causa (§4, F-131.3).

## 2. Prueba B — re-medición en vivo de la `tiny`, con `transformers` puro

La `tiny` no tenía artefactos supervivientes (excluida a priori en Sprint 2, 2026-06-18;
los runs de junio no se conservan). Se re-midió su geometría **sin una línea de código del
proyecto**: `AutoProcessor` + `AutoModelForZeroShotObjectDetection` +
`post_process_grounded_object_detection` de stock (transformers **5.12.1**, torch
**2.12.1+cu130**, RTX 4060), 12 imgs de `raw/construction_site_safety/train/images`,
prompt `"person. helmet. vest. head."`, umbrales 0,30/0,25. Script:
[`datos/131-diag-mmgdino.py`](datos/131-diag-mmgdino.py).

| ckpt (pesos locales del media-plane) | n | w med | h med | degeneradas (lado ≤1 px) | `person` w/h |
|---|---|---|---|---|---|
| **`mm-gdino-tiny`** | 62 | **3,1 px** | **455,4 px** | **21/62 (34 %)** | **0,01** |
| `mm-gdino-base` | 111 | 103,6 | 129,6 | 0 | 0,57 |
| `mm-gdino-large` | 85 | 87,6 | 27,4 | 0 | 2,26 |
| `gdino-tiny` (control, familia del campeón) | 103 | 86,3 | 145,0 | 0 | 0,59 |

Es **la firma exacta de Sprint 2** ("width≈0, height≈640"): x2 colapsa sobre x1 y la caja
queda como una línea vertical de la altura de la imagen.

## 3. Auditoría de la cadena de atribución

- **sha256 local == hub**: `model.safetensors` de la `tiny` local da
  `ad9d9f5f…8755`, idéntico al `lfs.sha256` que publica la API de HF para
  `openmmlab-community/mm_grounding_dino_tiny_o365v1_goldg_v3det` ⇒ no es corrupción de
  descarga; lo verificado es **el artefacto publicado**.
- **`mmgdino_adapter.py` NUNCA existió.** El historial git del media-plane arranca el
  2026-06-09 (cubre Sprint 2). En el árbol del 2026-06-17 (`f187f31`) los adaptadores eran
  `grounding_dino_adapter.py`, `yoloe_adapter.py` y `mock_detector.py`; el de GDINO tenía
  **cero** menciones a mm/openmmlab (sin rama especial). MM-GDINO pasó siempre por el
  adaptador compartido que, en las mismas corridas, funcionaba bien para gdino-tiny/base.
- **Versiones cruzadas**: Sprint 2 (junio) y esta verificación (septiembre) usaron
  versiones distintas de transformers ⇒ la degeneración reproduce **a través de versiones**
  del stack HF.

## 4. Hallazgos

- **F-131.1 — La degeneración de `mm-gdino-tiny` está CONFIRMADA y reproducida.** Ya no es
  "una sola medición del 2026-06-18 sobre el BENCH viejo": reproduce hoy, con stack limpio,
  sobre imágenes que no son del banco.
- **F-131.2 — La causa NO es del proyecto.** Reproduce sin código eovrt, con copia local
  byte-idéntica a la publicada, y el adaptador acusado no existió nunca. El defecto está
  **aguas arriba, en el checkpoint publicado** (o en su interacción con la conversión/stack
  HF — distinguir eso exigiría correrlo por MMDetection nativo y es irrelevante para la
  plataforma, que consume el stack HF). La atribución del registro de Sprint 2 ("bug en
  `mmgdino_adapter.py`") era **doblemente falsa**; el "causa nunca diagnosticada" de
  `operacion/117` §2 queda **diagnosticado en lo esencial**.
- **F-131.3 — `large` falla DISTINTO, y el hallazgo 5 del doc 64 fusiona dos fallas.**
  `tiny` degenera masivamente (34 % de cajas-línea); `large` **mislocaliza con geometría
  normal** (0 degeneradas estrictas; cajas apaisadas). Las 1–2 casi-degeneradas del
  sanity-check no pueden llevar el mAP de 0,34 a 0,0025. "Large reproduce el bug de
  Sprint 2" es falso **como causa**; el conteo del sanity-check era correcto.
- **F-131.4 — `mm-gdino-base` es geométricamente sano** (0,336–0,377 en estas sondas, cajas
  normales). La frase de `operacion/117` §2 *"sin baseline MM-GDINO geométricamente sana"*
  **no se sostiene como formulación**: sana la hay (base); lo que no hay es una baseline de
  la **variante que T3 iba a tunear** (`tiny`) ni una que valga la pena (base es mediocre
  sin ventaja en nada, doc 64 §5). El cierre de T3 se encabeza por **linaje** (lo tuneado
  sería MM-GDINO, no el campeón desplegado `gdino-tiny-560` HF) y **escalera pre-registrada**
  (T1 NO-GO + T2 NO-GO ⇒ T3 no se activa); las cajas van de refuerzo.

## 5. Cómo citarlo en el informe

Frase segura: *"la variante tiny se excluyó por cajas degeneradas del checkpoint publicado,
reproducidas con el stack `transformers` estándar sin código del proyecto y verificadas
contra el hash del repositorio de origen; las variantes base y gdino-tiny, evaluadas en
idénticas condiciones, no presentan el defecto"*.

Nunca escribir: "bug de nuestro adaptador" (falso, F-131.2) · "MM-GDINO tiene bboxes
rotas" como propiedad de la familia (base es sano, F-131.4) · "large reproduce el bug de
tiny" (son dos fallas distintas, F-131.3) · "sin baseline MM-GDINO geométricamente sana"
sin el matiz de F-131.4.

## 6. Constancia de reparaciones (mismo día)

✎ anotados con referencia a este doc: `operacion/64` (hallazgo 5) · `operacion/117` §2
(bullet de T3) · `results/bench_imagenes/index.md` (nota bajo la tabla de descartados; el
kit de redactores se regeneró después, porque copia esa tabla). Los pesos siguen en
`media-plane/models/mm-grounding-dino/` (2,8 GB) y los catálogos
`configs/models/mm-grounding-dino/*.yaml` se recuperan del historial git (archivados
2026-08-19).

## Reproducción

```bash
cd e-ovrt_media-plane
systemd-run --user --scope -p MemoryMax=5G \
  .venv/bin/python ../docs/operacion/datos/131-diag-mmgdino.py
# hash local vs hub:
sha256sum models/mm-grounding-dino/original/mm_grounding_dino_tiny_o365v1_goldg_v3det/model.safetensors
# ↔ lfs.sha256 en https://huggingface.co/api/models/openmmlab-community/mm_grounding_dino_tiny_o365v1_goldg_v3det?blobs=true
```
