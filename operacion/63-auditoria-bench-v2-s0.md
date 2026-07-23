# 63 — S0: Auditoría de calidad del BENCH v2 (2026-07-23)

Fase S0 del plan maestro (doc 62 §3). Motivada por la duda explícita del usuario sobre la
calidad de los datasets seleccionados; además cierra la auditoría visual pendiente desde
Sprint 2 (Task 4.3). Instrumento auditado: `construction_site_safety_bench.json` (196 imgs,
741 anotaciones, splits test 82 + val 114) del dataset Roboflow `construction_site_safety`.

## Estadística del GT

- **Por clase:** person 340, helmet 189, bare_head 110, vest 102. El denominador de vest es
  flaco (ya anticipado en doc 57: P2×3 en el rodaje por esta razón).
- **52/196 imágenes (27%) sin ninguna anotación.** Mezcla de negativos legítimos (obra sin
  personas) y fuera-de-dominio (ver abajo). Para AP no molestan (solo aportan FPs), pero
  inflan la sensación de tamaño del banco: el banco *anotado* efectivo es 144 imgs.
- **4 bboxes degeneradas**, todas `bare_head` de ~2×2,5 px — indetectables por diseño.
  `bare_head` tiene p10 de área relativa ≈ 0,00%: una fracción del GT de esa clase es
  esencialmente invisible. **Esto explica parte del AP≈0.02–0.09 universal en bare_head**
  (Sprint 2 y doc 61): no es solo debilidad del modelo, es GT sub-pixel.
- Sin bboxes fuera de imagen; sin duplicados (IoU>0.9). Tamaños: helmet mediana 0,40% del
  área, person 5,06% — objetos chicos, consistente con cámara lejana.

## Hallazgo principal: contaminación de dominio (inspección visual, 36 imgs muestreadas)

El dataset Roboflow mezcla fuentes que NO son obra. Confirmado a ojo con GT dibujado:

| Grupo (prefijo de archivo) | n | Qué es | Veredicto |
|---|---|---|---|
| `IMG_*`, `Movie-on*`, `Mask2_mov*`, `RPReplay*`, `YouTube_FreeStock*` | ~28 | **Selfies indoor con barbijo COVID**, `bare_head` anotado sobre el pelo | FUERA de dominio |
| `2008_*`/`2009_*` (PASCAL VOC) | ≥4 | Perro en pasto, hombre con botella, bicis en playa; **un `vest` mal etiquetado sobre camisa a cuadros** | FUERA + error de etiqueta |
| `airport_inside*`, `casino*`, `bookstore*`, `Inside-merge*` | ~5 | Interiores sin relación (uno con recorte de cartón de una persona) | FUERA |
| `autox*` | 6 | Karting/racing | FUERA |
| `youtube-*` | 61 | Obra real en su mayoría; incluye 1–2 placas/infografías de video | DOMINIO (con ruido menor) |
| `construction-*`, `ppe_*`, `image_*` | ~36 | Obra/PPE real | DOMINIO |
| `class1_*` | 6 | Escenas actuadas de escalera con casco (trabajo en altura) | DOMINIO adyacente |
| `681_alamy`, `003357` | 2 | Obra con **watermark de stock** encima | DOMINIO degradado |

**Estimación: ~20–25% del BENCH (≈40–50 imgs) es fuera-de-dominio**, concentrado en las
clases person/bare_head (los selfies con barbijo aportan GT de `bare_head` en contexto
absurdo para la tesis).

## Veredicto: `usable con salvedades declaradas`

1. **Para COMPARAR modelos (Fase S1) sigue siendo válido**: el GT es idéntico para todos los
   candidatos; el sesgo afecta el nivel absoluto, no el orden relativo (salvedad menor: un
   modelo podría ser diferencialmente mejor en selfies — se mitiga con el punto 3).
2. **Para afirmar "esto logra un OVD en obra" (Q1, reporte de cierre) NO se usa el número
   crudo del BENCH completo**: se reporta sobre el sub-split limpio (punto 3) o con la
   contaminación declarada como límite del instrumento.
3. **Acción derivada — sub-split `bench_obra`**: excluir por regla de prefijo los grupos
   FUERA de la tabla (lista reproducible), regenerar el COCO filtrado y re-puntuar a los
   campeones de S1 con `tools/evaluate --bench-coco`. Los dos números (completo y obra) van
   al reporte con su n.
4. Las 4 bboxes degeneradas de `bare_head` se excluyen del sub-split obra (regla w·h ≥ 9 px²)
   y la debilidad de `bare_head` se re-lee con eso en mano.
5. Nada de esto bloquea S1 (ya corriendo): la matriz se evalúa en ambos marcos.

Evidencia: mosaicos anotados en el scratchpad de la sesión (`s0_mosaics/`); estadística
reproducible con el script embebido en la sesión (COCO puro, stdlib).

## Actualización 2026-07-23: curación FORMALIZADA en el repo de datasets

El punto 3 del veredicto quedó implementado como artefacto reproducible (TDD, 7 tests,
suite datasets 119 passed), con la política **original intacto / curado aparte**:

- Script: `e-ovrt_datasets/datasets/scripts/curate/build_bench_obra.py` (reglas codificadas:
  12 prefijos de exclusión + área mínima 9 px²).
- Salidas: `datasets/processed/coco/bench/curated/construction_site_safety_bench_obra_{test,val}.json`
  + `bench_obra_manifest.json` (deltas exactos vs original: 49 imágenes excluidas con causa
  imagen-por-imagen, 4 anotaciones sub-área, conteos por clase antes/después).
- Registro humano: `datasets/registry/curation_bench_obra.md` (qué se ajustó y por qué, con
  la tabla de deltas — bare_head pierde 45% de su GT al limpiar: leer la clase contra n=61).
- **Paridad verificada**: los JSON del repo son idénticos a los sub-splits ad-hoc usados en
  la re-puntuación del doc 64 — los números publicados allí siguen válidos tal cual.
