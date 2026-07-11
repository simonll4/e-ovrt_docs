# video-gt-lab — laboratorio de GT de video + reparación del contrato GT↔evaluador

> **✎ Actualización 2026-07-11 (más tarde, misma fecha):** los gaps del §5 se
> CERRARON casi todos en la sesión de compatibilidad E2E: **(1) knob `source_id`**
> implementado en el media-plane (`ingest.config.source_id`; sin él, el default
> llevaba la extensión — `"cb_b01_p7.mp4"` — y el matching daba recall 0 en
> silencio); **(2) SDR + TTFD implementados** en `evaluate-alerts`
> (`--detections`/`--patterns`; criterio positivo = `spatial_absence` del motor
> real, auditable); **(3) umbrales alineados** al pattern set oficial 4000/7000
> (Tabla D.4 vía `cr01_cr02_v2`) en derive y evaluador — los defaults 3000/5000
> eran stale; **(4) hook `clip_id`/`ground_truth`** en el manifiesto del
> experimental-setup (runner inyecta source_id, corre la evaluación post-replay,
> el reporte liga la trazabilidad); **(5) `promote_clip.py`** + banco
> `processed/clip_bench/` creados, con el primer clip real `cb_b01_p7`.
> **Smoke §8.8 EJECUTADO de verdad** (GDINO-tiny → replay → evaluate-alerts):
> las 5 métricas del spec 43 §10 computadas. Además: **GT PRELIMINAR** de
> `cb_b01_p7` por revisión visual asistida (estado `gt_preliminary` en el
> manifest — lo reemplaza la pasada humana en CVAT); primer benchmark real:
> P=0.5 R=1.0 F1=0.67, t_alert=4000ms, TTFD=0ms, SDR=0.999 (el FP CR-02 es
> hallazgo sobre GDINO-tiny, no de plomería). Defecto Critical adicional
> corregido: el suavizado votaba por índice de lista y cruzaba huecos de
> evidencia — ahora suaviza por segmento contiguo. Quedan pendientes del §5:
> el roundtrip CVAT real (PC del usuario), la grabación A+C y el EBE-desde-clip.
> Suites: datasets 102 · media-plane 520 · control-plane 212 · exp-setup 247.
> **Todo el trabajo de este doc quedó COMMITEADO y PUSHEADO** (datasets
> `f8a2f3bc`, media-plane `5653978`, control-plane `853f690`, exp-setup
> `eda5736`) — el "SIN COMMITEAR" del cuerpo es el snapshot de la mañana.

- **Fecha:** 2026-07-11
- **Qué es:** resultados del **laboratorio generador de GT temporal de video** (el
  tooling con el que se ejecuta el spec 43, ADR-010) y de la **auditoría exhaustiva**
  que le siguió — que descubrió y reparó una ruptura del contrato entre el GT y
  `evaluate-alerts` v2. Toca **tres repos**: `e-ovrt_datasets` (dueño),
  `e-ovrt_media-plane` (pre-anotación GPU) y `e-ovrt_control-plane`
  (`evaluation/temporal.py`). **SIN COMMITEAR en los tres.**
- **Spec y plan:** `e-ovrt_datasets/docs/superpowers/specs/2026-07-11-video-gt-lab-design.md`
  (reconciliado con el as-built) y `.../plans/2026-07-11-video-gt-lab.md`. Ledger:
  `e-ovrt_datasets/.superpowers/sdd/progress.md`.
- **Suites:** datasets **88 passed**, media-plane **503 passed**, control-plane
  **199 passed** (ruff limpio en los tres). Gate de regresión F1=1.0 del doc 52 intacto.
- **Ejecución:** subagent-driven-development (11 tasks + revisor por task + revisión
  final de rama) + auditoría exhaustiva posterior (3 auditores paralelos: consistencia
  interna, contrato productor↔consumidor, cadena de benchmarking) + 2 fixers.

## 1. Qué se construyó

Pipeline semi-automático de 5 etapas, artefacto en disco entre cada una
(laboratorio en `e-ovrt_datasets/datasets-videos/`, guía del anotador en
`datasets-videos/GUIA-CVAT.md`):

| Etapa | Herramienta | Repo | Qué hace |
|---|---|---|---|
| 0 | `datasets/scripts/videogt/prepare_clip.sh` | datasets | normaliza a **CFR** sin audio (los celulares graban VFR y rompen el mapeo frame↔ms) + `info.json` con sha256/fps/n_frames |
| 1 | `python -m eovrt_media.tools.preannotate_video` | media-plane | **GDINO-base** (más fuerte que el tiny evaluado = anti-circularidad) + ByteTrack → tracks de persona con atributos `has_helmet`/`has_vest` en XML **CVAT for video 1.1** + preview H.264 |
| 2 | CVAT (PC del usuario) | — | corrección humana; labels reproducibles en `cvat_labels.json` (atributos **radio `unknown/true/false`, default `unknown`**) |
| 3 | `datasets/scripts/videogt/derive_clip_gt.py` | datasets | derivación **determinística** de episodios CR-01/CR-02 → `clip_gt.v2` + bloque `provenance` |
| 4 | `bench/validate_clip_gt.py` + `videogt/compare_annotations.py` | datasets | validación schema/manifest/sha256 + kappa de doble anotación |

**Invariante central, defendida de punta a punta:** la incertidumbre **nunca fabrica
una infracción**. Atributo `unknown`/ausente → `None` → corta la corrida de violación;
el writer omite atributos `None`; el default de CVAT es `unknown`. Verificado con
roundtrip writer→parser entre repos.

## 2. Verificación (medida, no declarada)

- **Smoke E2E real:** `recorte-1.mp4` (obra real, ~10 operarios, 1080p/30fps/24.4s)
  → pre-anotación GDINO-base en GPU RTX 4060 (7m19s, 41 tracks) → derivación →
  `validate_clip_gt` 0 errores → kappa emitido.
- **Carga cruzada (la prueba reina):** el GT real `lab_recorte1.json` **valida en el
  `ClipGroundTruthV2` real del control-plane** — 13 episodios, `source_id`,
  `subject_key` y `provenance` leídos. Es la primera vez que productor y consumidor
  se cruzan (ambos se habían escrito contra el spec 43 §4 por separado).
- **Base de tiempo DBE verificada sana:** `VideoFileSource` estampa media-clock real
  del archivo, el rate-gate **no re-numera** los frames que pasan, el motor copia el
  timestamp, el evaluador compara en la misma base. El riesgo #1 de "métricas mal en
  silencio" quedó descartado con evidencia de código.

## 3. Defectos que las revisiones atraparon (resumen; detalle en el ledger)

**Ronda 1 — revisión final de rama (3 Critical + 5 Important, todos corregidos):**
fusionar antes de umbralar fabricaba episodios de escena que ningún sujeto sostuvo
(subestimaba recall CR-01); cero tracks `person` producía un `negative:true` silencioso;
el default `checkbox=false` de CVAT convertía "no tocado" en "sin casco"; el umbral de
persona era inoperante (ByteTrack fija `det_thresh = activation + 0.1` internamente);
`any()` en la asociación EPP escondía infracciones en multitud; truncamiento silencioso
por XML de otro video; sin provenance; spans no matcheados descartados sin señal.

**Ronda 2 — auditoría exhaustiva (contrato roto + robustez):**

| # | Hallazgo | Fix |
|---|---|---|
| C | **`evaluate-alerts` v2 RECHAZABA el GT real** — exige `source_id` (scene) / `subject_key` (subject); el productor no emitía ninguno | el productor emite `source_id` en **todo** episodio (convención **`source_id = clip_id`**, override en clip.yaml) y `subject_key = subject_label` en subject; el validador de datasets espeja el contrato |
| C | `subject_label` (local a CVAT) **no mapea** a las claves `{pattern}:{source}:{track}` del motor | asumido por diseño: clips P7 subject-level = comparación **cualitativa** G0/G1; para métricas se derivan a nivel **scene** |
| I | **Doble fuente de umbrales:** el evaluador ignoraba `provenance.pattern_set_ms` y usaba su default (coincidían por casualidad) | `temporal.py` resuelve ventanas **caller > provenance del GT > defaults** y declara el origen en `effective_matching_windows` (campo aditivo) |
| I | `level` con typo caía a scene en silencio (fusionaba sujetos); clip.yaml incompleto = KeyError crudo; `compare_annotations` truncaba con `duration_ms` distinto (kappa=1.0 falso); manifest sin cruce de `source_file`; pattern-set malformado = traceback | los seis con validación explícita + error claro + test |

## 4. Correcciones al doc 52

- El "listo para su GT" del doc 52 §5 era **engañoso en dos sentidos**: (a) el GT real
  no cargaba (contrato de identidad, arriba); (b) **SDR y TTFD no están implementados**
  — `evaluate_temporal_alerts` no recibe `detections.jsonl` y su modelo de salida no
  tiene esos campos. v2 cubre **2 de las 5 métricas** del spec 43 §10 (P/R/F1 + una
  latencia proxy de `t_alert-system`). El control de consistencia
  `t_alert-system = TTFD + t_capture→alert` (spec 43 §4.1) tampoco es computable aún.
- `temporal.py` cambió **sin commitear** sobre el HEAD pusheado: `provenance` tipado,
  `_resolve_matching_windows`, `effective_matching_windows`. 199 passed (192 + 7).

## 5. Estado del dataset con GT — PENDIENTE (la ejecución del spec 43)

El **tooling está completo y verificado**; la **ejecución del banco** sigue pendiente
y es el camino que desbloquea R3/D1-Fase2. En orden:

1. **Roundtrip CVAT real** (PC del usuario; `GUIA-CVAT.md` paso 6) — único contrato
   del laboratorio sin validar: el XML del writer nunca pasó por un CVAT real.
2. **Grabación A+C** del spec 43 §3 (guiones P1–P8 + V1–V3, consentimientos
   Ley 25.326, EPP, trípode) + bloque B (videos Intel) cuando lleguen.
3. **Anotación** con el laboratorio (5–10 min/clip esperados) + doble anotación ≥20%.
4. **Promoción al banco** — **GAP de tooling:** `datasets/processed/clip_bench/` no
   existe ni hay script de promoción (media git-ignored + gt + XML corregido +
   manifest con sha256/block/scenario/estado). Sin esto, 8–15 clips a mano =
   inconsistencia garantizada.
5. **SDR + TTFD en `evaluate-alerts`** — **GAP de código** (no de datos): falta
   `detections_path` en la firma y la lógica de ambas métricas.
6. **`clip_id` en el manifiesto del experimental-setup** — **GAP:** la trazabilidad
   `experiment_id → clip_id → gt/*.json` (spec 43 §6) no tiene ningún hook en el
   código; spec 44 §8 la asumió sin verificar. Hoy una corrida DBE puede apuntar al
   archivo del clip (plugin `video_file`), pero el reporte no liga con el clip.
7. **Smoke E2E del spec 43 §8.8:** clip → detecciones → replay → `evaluate-alerts`
   con GT v2 → P/R/F1 + latencias persistidas.
8. **EBE-desde-clip (H4)** — **brecha de diseño documentada, no bloqueante:** no
   existe la receta mediamtx+ffmpeg (el runbook serie 30 no la tiene) y `RtspSource`
   estampa wallclock mientras el GT está en media-ms — falta un ancla de
   sincronización. Resolver antes de la comparación DBE↔EBE con fuente idéntica.

**Convención nueva no negociable:** la corrida del bench configura su fuente con
**`source_id = clip_id`** — el matching de escena del evaluador es literalmente
`alert.source_id == episode.source_id`.

## 6. Cómo continuar

- **Ya (usuario):** roundtrip CVAT (ítem 1) — 30 min, desbloquea confiar en la
  herramienta. En paralelo: consentimientos + guiones de grabación (papel, no código).
- **Siguiente sesión de implementación (en este orden):** SDR+TTFD en el evaluador
  (ítem 5 — cierra las 5 métricas del spec 43 §10 y el control de consistencia),
  script de promoción al banco (ítem 4), `clip_id` en el manifiesto (ítem 6). Los
  tres son acotados y ninguno depende de la grabación.
- **Después:** grabación + anotación del banco (ítems 2–3) → smoke §8.8 (ítem 7) →
  R3/D1-Fase2. El spec 45 (distribución MQTT) sigue PARA LO ÚLTIMO por decisión del
  usuario; EBE-desde-clip (ítem 8) se resuelve cuando toque H4.
