# ADR-002 — Granularidad del patrón: G0 núcleo + G1 demostrativa

- **Fecha:** 2026-07-09
- **Estado:** Aceptada
- **Dimensión que atiende:** D2 (doc 03 §3; re-discusión abierta por la rama `mati`)
- **Decisor:** usuario, 2026-07-09

## Decisión

1. **G0 (escena/fuente) es el núcleo**: el `PatternEngine` mantiene estado por
   clave `(pattern_id, source_id)` con conteo de sujetos en evidencia como metadato
   del episodio. Todas las métricas del informe (TTFA/TTFD, SDR, precision/recall de
   alertas) se calculan a nivel escena-condición.
2. **G1 (sujeto) entra como capacidad demostrativa**: se porta el `SimpleIoUTracker`
   de `eovrt_labs` (rama `mati`) al **media-plane** como componente opcional
   post-normalización, que emite `track_id` como **campo aditivo opcional** en
   `media.detection.v1`. G1 se demuestra sobre 2–3 clips del clip bench comparando
   episodios G0 vs G1.
3. **Límite declarado:** G1 es demostrativa, no validada — **sin métricas MOT**
   (siguen "no aplicables", E-10) y sin GT de identidades. La atribución por sujeto
   no se promete como resultado; se muestra como extensión operativa del contrato.

## Alternativas consideradas

- **G0 solo, tracker en labs** (recomendación previa de los docs, E-03 original):
  cero riesgo de agenda, pero desaprovecha un tracker ya implementado y calibrado
  (doc 01 §12.2–12.3) y deja la plataforma sin identidad estable ni demo por sujeto.
- **G1 pleno como núcleo:** indefendible con 12 semanas — exige GT de identidades y
  anotación cara del clip bench (doc 07 D2.4); es el "estado intermedio
  indefendible" del doc 02 §4.2 si no se mide.

## Fundamento

- El costo de código es ~cero (el tracker existe, con apariencia, gates y tuning
  YAML probados sobre video real); el costo real era la evaluación rigurosa — que
  este ADR excluye explícitamente al declararla demostrativa.
- Cierra el punto débil de identidad (doc 01 §6): el motor deja de operar sobre
  `det_NNN` aliasado cuando el track está activo, y el warning de la rama `mati`
  cubre el caso degradado.
- G0 preserva la línea ético-legal (menos individualización, doc 07 D2.1) y es lo
  que §17.3.8.3.2 declara para el núcleo.

## Impacto

- **Motor:** refactor menor de clave de estado + regenerar fixture temporal y GT a
  nivel escena-condición (~1–2 días, presupuestado en doc 07 D2.3).
- **media-plane:** puerto del tracker post-normalización + campo `track_id`
  (spec media-plane).
- **E-03 (doc 10) se redefine**: lo excluido queda acotado a métricas MOT y a G1
  como modo del núcleo. G1-demo es lo primero que se sacrifica si la agenda aprieta
  (antes que overlay renderer y distribución).
- **Clip bench:** GT se anota a nivel escena-condición; identidad solo en los 2–3
  clips destinados a la demo G1 (anotación mínima, no GT MOT).

## Referencias

Doc 02 §4.2, doc 03 §3, doc 07 D2, doc 01 §12, doc 10 E-03/E-10.
