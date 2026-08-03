# 78 — Lo que falta para cerrar (lista limpia)

- **Última actualización:** 2026-07-29
- **Propósito:** SOLO lo pendiente, sin historia. El detalle, la evidencia y el
  porqué de cada ítem viven en el doc 75 (tablero auditado); esta es la lista
  operativa para mirar cada mañana. Defensa: ~fines de septiembre 2026.

## A. Usuario

| # | Tarea | Esfuerzo | Referencia |
|---|---|---|---|
| A1 | 🔄 **Pasada CVAT de los 48 clips** (en curso desde 29/07) — la única latencia real del proyecto | días | GUIA-CIERRE §1 |
| A2 | **Task 4.3**: auditoría visual con el kit (24 PNGs + tabla pre-cargada) en `e-ovrt_datasets/datasets/processed/audit_task43/` — marcar ✓/✗, resumen y firma | ~15 min | `registry/bench_gt_audit.md` |
| A3 | **Receta git del doc 77**: merges a `main` ×4, borrar `mati`, merge de `perf` (recomendado; ya no es fast-forward), bundle de `docs` a otro disco | ~30 min | doc 77 |
| A4 | ~~Licencia CHV~~ **VERIFICADA Y DECLARADA 2026-07-29** (GitHub API `license: None` + README "open for free use" con cita `wang2021ppe`; estado `Aprobado` sin redistribución de imágenes — cumplido por construcción; vocabulario del registry normalizado). Te queda: **visto bueno a la declaración + incluir la cita `wang2021ppe` en la bibliografía de la tesis** | 5 min | `license_registry.md` §Verificación CHV |
| A5 | **Decisiones** (elegir y anotar, no implementar): F-RT3, two-node 2c, `stopped`-consolida, destino de manifiestos exploratorios, config `replay_dbe` duplicada, banner v1 por API | minutos c/u | doc 75 §5 |
| A6 | **Verificar administrativo del rodaje**: consentimientos firmados y archivados | verificación | GUIA-CIERRE §2 |

## B. Colega de front (rama `front-design`)

| # | Tarea | Referencia |
|---|---|---|
| B1 | Frontend completo de la webconsole sobre `front-design` (nace de `159167b`); mantener los 381 tests verdes; no tocar backend | specs en `docs/superpowers/` del repo |
| B2 | Al terminar: merge de `front-design` → `feature/webconsole-consola-tesis` + las dos suites. Convención mientras viva la rama: nosotros NO tocamos `webconsole/frontend/` | — |

## C. Claude (a pedido)

| # | Tarea | Nota |
|---|---|---|
| C1 | **Clips soak** para FAR/hora (1–2 negativos de 5–10 min; el video 6.1 de 6:10 ya está verificado sin cortes) | coordinar: no tocar `datasets-videos/` con el lote CVAT abierto |
| C2 | **`track_id` + overlay** para V1–V3 — **scoping HECHO (doc 79)**: ruta recomendada = renderer offline post-hoc (horas–1 día; doc 09 ya decidió V1–V3 pre-renderizados; `supporting_bboxes` ya está en los artefactos). Falta: que el usuario responda las **3 preguntas de alcance del doc 79** → implementación | brainstorming reducido a 3 preguntas |
| C3 | `docs/experiments.md` al día (10 manifiestos v1) | tras la decisión A5 sobre su destino |

## D. Con el GT humano (el tramo final, sin código nuevo)

1. Por clip corregido: export XML → `derive_clip_gt` → `promote_clip` →
   `build_clip_bench` + `sha256sum -c` (secuencia en el docstring de
   `build_clip_bench.py`). Protocolo de acuerdo inter-anotador: doc 58 §B.3.
2. **Fase T** (banco temporal) → **Fase P** (plataforma, Nivel B) → **Fase D**
   (D1 E-DIR vs E-IND, prompts ya congelados por acta 76) → análisis de errores →
   **reporte de cierre** (doc 62 §8), versionando el informe de resultados v2.
3. Re-verificar **parity live↔offline** con las corridas nuevas.
4. Material de defensa: **V1** (toma vistosa infracción→alerta, checklist doc 69);
   re-toma P2 live limpia opcional.

## Recordatorios operativos

- `EOVRT_MODEL_REF` quedó en `yoloe/yoloe-26x` → volver a `grounding-dino/gdino-tiny-560`.
- El manifiesto que referencia `a_p1_c01.mp4` apunta a un clip inexistente (la serie
  arranca en `c02`).
- Flake a vigilar: suite frontend mostró 1 archivo rojo en 1 de 4 corridas (29/07),
  no reproducido.
- Limitaciones que se DECLARAN (no se arreglan): doc 75 §6 — A6-material, CR-02 sin
  GT de imagen, caveats por estrato, F-RT4, GT preliminar hasta la pasada humana.
