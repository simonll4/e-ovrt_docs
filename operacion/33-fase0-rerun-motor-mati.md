# Paso 0 — Fase 0 re-ejecutada con el motor de `mati`

> **Estado de los artefactos (2026-07-10).** El `detections.jsonl` de entrada
> (`run_20260704_205708_dbe_grounding_dino_96b2b0`, 82 unidades) fue **podado del disco**
> en una limpieza de `runs/` — que está git-ignored. **La comparación de este documento no
> es reproducible.** Sus números sobreviven íntegros en
> `operacion/datos/33-fase0-rerun-motor-mati.datos.json` (los tres `summary.json` y el
> conteo de items disputados), y el `alerts.jsonl` del motor viejo (137 alertas) sigue en
> `e-ovrt_control-plane/runs/fase0_dbe_gdino_bench_20260706/`. El script
> `datos/33-*.probe.py` apunta al input podado y ya no corre tal cual.
>
> Lo que sí se re-verificó sobre un BENCH regenerado (114 imgs, GDINO fresco): la
> propiedad estructural de G0 (doc 34 §2.3). El hallazgo central de este doc —cero EPP
> disputado ⇒ el matching 1:1 es un no-op sobre imágenes— es una propiedad del corpus,
> no del artefacto, y sigue en pie.

- **Fecha:** 2026-07-09
- **Disparador:** `operacion/32-handoff-arranque-tramo-plataforma.md` §4.
- **Estado:** **cerrado**. Los tres criterios de terminado se cumplen.
- **Resultado en una línea:** el motor nuevo produce **exactamente las mismas 137 alertas**
  que el viejo sobre el BENCH; la baja de CR-02 que el handoff predecía **no ocurre, y es
  correcto que no ocurra** — este corpus no contiene la situación que el matching 1:1 arregla.

## 1. Qué se corrió

| | Corrida |
|---|---|
| **Input (idéntico en ambas)** | `e-ovrt_media-plane/runs/run_20260704_205708_dbe_grounding_dino_96b2b0/detections.jsonl` — GDINO sobre BENCH v2, 82 unidades |
| **Pattern set (idéntico en ambas)** | `configs/patterns/cr01_cr02_v1.yaml` (`confirm_after_frames: 1`, sin cooldown) |
| Motor viejo (matching por contención) | `runs/fase0_dbe_gdino_bench_20260706` (2026-07-06) |
| Motor nuevo (`mati`, HEAD `443712b`) | `runs/fase0_dbe_gdino_bench_mati_20260709` |
| Config del re-run | `configs/fase0_dbe_gdino_bench_rerun.yaml` |

La rama `feature/control-service` está en `443712b`, que incluye
`db19315 fix(engine): matching de cardinalidad maxima en asociacion EPP<->persona`.
El motor nuevo es, verificadamente, el que corrió.

## 2. Tabla comparativa

| Métrica | Motor viejo | Motor nuevo | Δ |
|---|---|---|---|
| `units_processed` | 82 | 82 | = |
| `units_failed` | 0 | 0 | = |
| `errors_count` | 0 | 0 | = |
| `pattern_events_count` | 137 | 137 | = |
| `alerts_count` | **137** | **137** | **=** |
| — de las cuales CR-01 | 61 | 61 | = |
| — de las cuales CR-02 | 76 | 76 | = |
| `avg_processing_ms` | 0.129 | 0.754 | **×5.8** |
| `warnings` | — | `[]` | — |

Las alertas no solo coinciden en el total: coinciden condición por condición.

## 3. Hallazgo 1 — la igualdad es correcta, no es una regresión

El handoff §4.3 predecía menos alertas de CR-02 porque el matching bipartito 1:1 elimina
el "robo" de EPP entre personas superpuestas. Esa predicción **es falsable y falló**, así
que se investigó antes de seguir, como el propio handoff exigía.

El matching 1:1 solo puede diferir del matching por contención cuando un item de EPP cae
en la región de **más de una** persona. Se instrumentó el input para contar exactamente eso:

| Patrón | Unidades | Unidades con >1 persona | Items EPP | Items en 1 región | Items en 0 regiones | **Items disputados (>1 región)** |
|---|---|---|---|---|---|---|
| CR-01 (`helmet`) | 82 | 27 | 101 | 72 | 29 | **0** |
| CR-02 (`vest`) | 82 | 27 | 61 | 54 | 7 | **0** |

**Cero disputas.** Con cero disputas las dos funciones de matching son idénticas por
construcción, y la salida idéntica es el resultado esperado.

El matching nuevo no es código muerto: se ejecuta sin gate de configuración
(`spatial_absence.py:165`) y el test `test_overlapping_persons_do_not_steal_each_others_helmet`
lo cubre y pasa. El corpus BENCH, con ~1,7 personas por imagen y solapamiento escaso,
simplemente no lo ejercita. El experimento del 2026-06-26 que motivó el cambio usaba otro
material, con personas superpuestas.

**Consecuencia metodológica:** el BENCH de imágenes **no sirve** para demostrar el valor del
matching 1:1. Esa demostración necesita material con personas superpuestas — es decir, el
clip bench (spec 43) o un fixture sintético dedicado.

## 4. Hallazgo 2 — el warning de `det_NNN` es inalcanzable con `cr01_cr02_v1`

El criterio 3 del Paso 0 pedía capturar el warning de ids inestables. Con el pattern set
prescrito **no puede dispararse**: el warning está gateado por `persistence_required`
(`runtime/replay.py:149`), que es verdadero solo si
`confirm_after_frames > 1` o hay `confirm_after_ms` (`replay.py:31-32`). `cr01_cr02_v1`
tiene `confirm_after_frames: 1`. No hay nada roto: `warnings: []` es el comportamiento correcto.

Para satisfacer el criterio sin contaminar la comparación (que exige variable única) se
corrió un **diagnóstico aparte**, idéntico salvo `confirm_after_frames: 2`:

- Pattern set: `configs/patterns/cr01_cr02_persistence_probe.yaml`
- Config: `configs/fase0_dbe_gdino_bench_persistence_probe.yaml`
- Run: `runs/fase0_dbe_gdino_bench_persistence_probe_20260709`

Resultado: **137 eventos de patrón, 0 alertas confirmadas**, y el warning emitido.

> Persistencia temporal inactiva: los patrones exigen confirmacion multi-frame pero ninguna
> persona trae detection_id estable (solo fallback det_NNN). El motor no podra confirmar
> condiciones (…)

Esta es la evidencia empírica que respalda **G0 como primer cambio** (spec 41 §2): en cuanto
una condición exige persistencia temporal, el estado sobre ids inestables no confirma nada.

### 4.1 Matiz importante sobre G0 en este corpus

El `subject_key` actual es `{pattern_id}:{source_id}:{detection_id}`
(`spatial_absence.py:139-141`). En este corpus **cada imagen es su propio `source_id`**
(`source_id` = nombre del archivo), de modo que el estado nunca colisiona entre unidades.
El aliasing de `det_NNN` que motiva G0 **no se manifiesta acá**: se manifiesta en video,
donde `source_id` es la cámara y permanece constante mientras `det_NNN` re-enumera personas
distintas frame a frame.

Dicho de otro modo: sobre imágenes independientes el Paso 0 puede mostrar el *síntoma*
(nada confirma) pero no el *daño* (estado de la persona A atribuido a la persona B). El daño
solo es observable sobre video, y por eso el gate de G0 (F1 = 1.0 en ambas granularidades)
se corre contra el fixture de escena-condición, no contra el BENCH.

## 5. Hallazgo 3 — coste de cómputo

`avg_processing_ms` sube de 0,129 a 0,754 ms por unidad (×5,8). Es el precio del matching de
cardinalidad máxima (caminos aumentantes) frente a la contención codiciosa, más el trabajo
extra del motor nuevo. En términos absolutos es irrelevante: 0,75 ms por unidad está tres
órdenes de magnitud por debajo del presupuesto de inferencia, y no afecta a
`t_compute-budget` (spec 40 §5.2). Se registra para que la cifra no sorprenda más adelante.

## 6. Criterio de terminado (handoff §4.4)

- [x] Corrida completa sin errores de contrato (`errors_count: 0`).
- [x] Tabla comparativa viejo-vs-nuevo, alertas por condición (§2).
- [x] Warning de ids inestables (`det_NNN`) capturado como evidencia (§4).

Adicionalmente: el contrato sigue alineado tras la migración de `timing` que hizo `mati`
(`read_ms`/`preprocess_ms` → `normalize_ms`) — 82/82 unidades parseadas, `errors_count: 0`.

## 7. Correcciones que este registro introduce al handoff (doc 32)

1. **§4.3 "Qué esperar del motor nuevo"** queda corregido: sobre el BENCH **no** hay que
   esperar menos alertas de CR-02, y que no bajen **no** es motivo para investigar. La
   condición de alarma correcta sería que cambien las alertas, no que se mantengan.
2. **§4.4 criterio 3** es inalcanzable con el pattern set que §4.2 prescribe. Requiere la
   corrida diagnóstica de §4 de este documento.

## 8. Qué NO se puede concluir de esta corrida

- **No** valida el matching 1:1 (el input no lo ejercita).
- **No** dice nada sobre la calidad de detección de GDINO ni sobre umbrales: el pattern set
  es el de arranque, sin calibrar.
- **No** mide `t_capture→alert` ni `t_compute-budget`: la instrumentación es el punto 5 del
  orden de trabajo (spec 40 §5.2.4), todavía sin implementar.

## 9. Evidencia cruda

`operacion/datos/33-fase0-rerun-motor-mati.datos.json` — los tres `summary.json`
(viejo, nuevo, probe) y el conteo de items disputados.
