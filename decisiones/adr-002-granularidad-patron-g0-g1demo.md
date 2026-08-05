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

---

## Adenda 2026-08-04 — G1 medida y operativa; el tracker vive en el control-plane

- **Estado:** **RATIFICADA por el usuario el 2026-08-05**, con la verificación en vivo
  (doc 91) y la re-revisión crítica ya incorporadas.
- **Motivo:** la campaña G1 (doc 89) midió el modo `subject` sobre los **34 clips** del
  banco y dio **F1 0,789 → 0,930** con las **mismas detecciones** (SDR y TTFD idénticos
  hasta el decimal: la mejora no es de percepción). Eso excede lo que este ADR
  anticipaba de una capacidad "demostrativa".

**Qué NO cambia (el núcleo de la decisión se mantiene):**

1. **G0 sigue siendo el núcleo** y las métricas del informe se siguen calculando a
   **nivel escena-condición** (punto 1). La campaña G1 respetó esto: el motor corrió
   por sujeto, pero el GT y todas las métricas siguieron siendo escena-condición.
2. **La exclusión del punto 3 sigue vigente**: **sin métricas MOT y sin GT de
   identidades** (E-10). No se promete atribución por sujeto como resultado. Lo que se
   reporta es **rendimiento de alertas**, que es justamente lo que el punto 1 manda
   medir a nivel escena.

**Qué sí cambia:**

3. **Dónde vive el productor de `track_id`.** El punto 2 preveía portar el
   `SimpleIoUTracker` **al media-plane**; nunca se ejecutó (doc 79: *"hoy nadie produce
   `track_id`"*). Se implementó en el **control-plane como decorador de fuente**
   (`sources/tracking.py`, activado por `input.track_persons`, opt-in y default
   `false`). Ventajas medidas frente al plan original:
   - cubre **DBE y EBE/live** por igual (decora cualquier `MediaEventSource`), así que
     la identidad **no depende de que el productor la emita**;
   - **no toca el pipeline congelado** del media-plane a 8 semanas de la defensa;
   - costo real: ~2 h con TDD (12 tests), contra 1–2 días + purga de estado +
     revalidación del port.
4. **El alcance de la demo creció**: el punto 2 decía "2–3 clips"; se corrieron los
   **34**, con guard contra degradación silenciosa a escena y verificación
   anti-artefacto (en P7 ambas campañas emiten las **mismas 7 alertas**; G1 acierta 5
   en vez de 2 y baja FP de 5 a 1 — no es que rocíe alertas).

**Trade-off declarado:** el `track_id` no queda embebido en `detections.jsonl` (la
fuente de verdad del media-plane) sino en los artefactos del control-plane
(`subject_key` de `pattern_events.jsonl`). La reproducibilidad se conserva —tracker
determinista + stream ordenado ⇒ mismo id en cada replay, **verificado: el camino
config-driven reproduce la campaña G1 exacto en los 34 clips, 11 campos por clip
(incluidos SDR/TTFD)**— y quien necesite el artefacto con `track_id` embebido lo
genera con `python -m eovrt_control.tools.track_detections`.

**Verificado en vivo (2026-08-05, doc 91):** humo EBE real con la OAK-D, verde. La
clave de estado pasa de `CR-01:smoke_ebe` (escena) a **`CR-01:smoke_ebe:subject_001`**
(sujeto), con `bus_dropped_events=0` y **sin `no_track_id`** en las causas de
degradación. La afirmación "cubre DBE y EBE/live por igual" ya no depende solo de tests
unitarios. En la misma sesión se corrió la **regresión del camino live** tras los
cambios de la jornada (150 unidades, 0 errores, 2 alertas): el despacho por estrategia
dentro de `pattern_engine.process()` no rompió EBE.

**Endurecido en la re-revisión crítica (2026-08-04):** el decorador delega
`close`/`request_stop`/`dropped_events` a la fuente interna — sin eso, en live
silenciaba `bus_dropped_events` (ADR-003), no cerraba el socket y anulaba la parada
cooperativa (trampa SIGABRT). Avisa además si el stream trae frames hacia atrás (no
puede ordenar, a diferencia de la herramienta post-hoc). De paso se atrapó y corrigió
una trampa de plataforma preexistente: colisión de directorios de run cuando dos
corridas del mismo nombre caen en el mismo segundo (`prepare_run` ahora desambigua los
ids autogenerados). Suite 310 passed.

**Deuda que queda abierta (ya no bloqueante):** el port al media-plane del spec 42 §3
sigue teniendo sentido si se quiere `track_id` en la fuente de verdad para todos los
consumidores. Deja de ser el camino obligatorio para tener G1.

**Límite que se mantiene:** el banco es material **guionado** con multitudes acotadas
(L4). La robustez del tracker en obra real no está medida.

## Referencias

Doc 02 §4.2, doc 03 §3, doc 07 D2, doc 01 §12, doc 10 E-03/E-10.
Adenda: doc 89 (campaña G1), doc 79 (scoping), doc 90 D-90.3.
