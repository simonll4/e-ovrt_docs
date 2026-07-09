# ADR-010 — Secuenciación: plataforma primero, dataset/GT de evaluación al final

- **Fecha:** 2026-07-09
- **Estado:** Aceptada
- **Decisión que atiende:** nueva (decisión del usuario) — orden de ejecución del
  proyecto. **Supera el "clip bench primero / mayor lead time" de docs 02 §4.5/§7,
  03 §8, 04 §7 e índice 00.**
- **Decisor:** usuario, 2026-07-09

## Decisión

El proyecto se ejecuta en dos tramos secuenciales:

1. **Tramo plataforma (primero):** media-plane y control-plane operando como
   servicios (ADR-008), bus media→control (ADR-003), config experimental
   centralizada y gestionada desde la webconsole (ADR-009), corridas y configs
   **trazables** de punta a punta (`experiment_id`, ADR-004), y **toda la
   infraestructura de instrumentación** para producir las métricas (hitos por
   alerta, percentiles, reporte consolidado con estados de aplicabilidad —
   ADR-006). Criterio de salida del tramo: la cadena completa corre sobre fuentes
   de prueba con cada número reconstruible hasta su configuración.
2. **Tramo evaluación (después):** recién con la plataforma funcionando se
   ejecuta el **dataset curado con GT temporal por escenario** (spec 43, ya
   escrito) y se corren las campañas que dependen de él: Fase 2 del experimento
   D1, R3 y la calibración final.
   **Precisión 2026-07-09 (usuario):** el disparador de la ejecución del spec 43
   es **el cierre del spec 44 (experimental-setup)** — corridas y configs
   trazables + runner + reporte operativos — no el final absoluto del tramo: la
   distribución (spec 45) no es prerequisito del clip bench y puede avanzar en
   paralelo. Además, el **material crudo del dataset (videos) ya está en proceso
   de armado** en paralelo al tramo plataforma — lo diferido es la ejecución
   formal del spec (GT, anotación, validación, registry), no la recolección.

## Qué NO se difiere (sigue disponible temprano)

- **R1** ya está (Sprint 2 / doc 31).
- **La Fase 1 de D1** (scoring por persona sobre BENCH v2, imágenes) no necesita
  clips — puede correr apenas exista `edir_v1`, sobre la plataforma del tramo 1.
- El fixture temporal sintético del control-plane sigue siendo el gate de
  regresión del motor durante todo el tramo 1.

## Riesgo aceptado y mitigación

Los docs 02/07 argumentaban "clip bench primero" por lead time: diferirlo comprime
R3, la Fase 2 de D1 y la escritura hacia el final (el riesgo I2 de la auditoría).
Se acepta a cambio de un beneficio real: **el GT se diseña una sola vez, contra una
plataforma estable** (contratos, pattern set v2, evaluador y matching definitivos),
en lugar de anotarse dos veces o contra un motor que aún cambia. Mitigaciones:

- El spec 43 queda **congelado y ejecutable** (guiones, schema `clip_gt.v2`,
  procedimiento): cuando llegue el tramo 2, la ejecución es ~1 semana sin diseño.
- La coordinación de los videos Intel (bloque B) y los consentimientos pueden
  gestionarse en paralelo durante el tramo 1 (son trámites, no foco).
- La regla de la auditoría se mantiene: escritura incremental — el tramo 1 produce
  directamente el contenido de Etapa 4 (specs, ADRs, reporte).

## Impacto

- Orden de la cola de specs (`specs/README.md`): **40 → 41 → 42 → 44 → 43**;
  el 45 (distribución) no bloquea al 43 y corre tras el 44, en paralelo con él.
- El plan indicativo de 12 semanas (doc 02 §7) deja de leerse literalmente para
  los ítems de clip bench/R3: valen las dependencias, no las semanas.
- Los avisos "arranca ya / mayor lead time" en docs 02, 03, 04 e índice quedan
  marcados como superados por este ADR.

## Referencias

Spec 43 (diseño completo, diferido), doc 02 §4.5/§7, doc 03 §8, doc 04 §7,
doc 07 I2/H2, ADR-002/003/004/006/008/009.
