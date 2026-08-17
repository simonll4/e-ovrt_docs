# 120 — Cierre de T-FT-031/T-FT-032: baseline YOLOE-26s congelada sobre `bench_v3` (2026-08-15)

- **Estado:** T-FT-031 y T-FT-032 **cerradas** la misma jornada de las firmas (doc 119 §8).
  **El NO-GO de T1 full quedó reducido a su último eslabón**: emitir
  `full-authorization.json` y la confirmación manual del usuario (T-FT-043).
- **Encuadre:** rama comparativa E-04 (ADR-017). **Estas cifras se rotulan como rama
  comparativa y viven en tablas propias — nunca se funden con el núcleo zero-shot.**
  No se promueven a `results/` hasta que la jornada complete (tuned evaluado y go/no-go
  aplicado); la evidencia re-verificable vive en los artefactos hasheados de abajo.
- **Regla heredada del doc 119:** ninguna fila de evidencia sin haber corrido el comando.
  Todo lo de abajo fue ejecutado y observado el 2026-08-15.

## 1. T-FT-031 — catálogo, comando congelado y enforcement (cerrada)

Cinco piezas, todas verificadas:

1. **`pycocotools` instalado** en el venv del media-plane (era la dependencia ausente
   señalada el 08-14); 30 tests de evaluación verdes.
2. **Enforcement del vocabulario canónico v2 en config** — lo que D-FT-08 habilitó y el
   doc 119 §8.1 registraba como no ejecutado: `CANONICAL_V2_FIXED_VOCABULARY` en
   `e-ovrt_media-plane/src/eovrt_media/config/schemas.py`; cualquier `fixed_vocabulary`
   que difiera del contrato en ids, nombres u orden **se rechaza en config**, antes de
   llegar al adapter. TDD: 5 tests de mutación (reordenado / subset / id no canónico /
   text no exacto / superset) + los previos; **suite completa del media-plane 665
   passed, Ruff limpio**.
3. **Catálogo finetuned versionado**: `configs/models/yoloe/yoloe-26s-ft-t1.yaml`
   (sha256 `97129219…cc9f`), `lineage: finetuned`, pesos esperados en
   `models/yoloe/finetuned/t1/best.pt` — aterrizan recién en la promoción T-FT-050;
   hasta entonces usar el ref falla, y ese fallo es correcto.
4. **Comando de evaluación congelado**: `finetuning/scripts/evaluate_t1_bench_v3.py`
   (sha256 `88797bee…8f46`) — la única vía admitida para evaluar baseline y tuned.
   Verifica **todos** los insumos del protocolo por sha256 antes de computar (evaluador,
   bench, 4 estratos, 2 person-GT), **aborta si falta una sola imagen** de cobertura, y
   emite exactamente los artefactos del protocolo. 4 tests sintéticos (hash-mismatch
   aborta sin escribir; cobertura incompleta aborta; happy path emite todo; arm inválido
   rechazado). Suite `finetuning/tests/` 46 passed.
5. **Serving E2E ejercido con el checkpoint smoke** (`run_20260815_193622_dbe_yoloe_e31020`,
   CPU, 8/8): startup por catálogo fixed-vocabulary, run completo, `detections.jsonl`
   parseable por el evaluador congelado. 0 detecciones — **esperado** del checkpoint
   smoke (1 época al 5 %, no científico); la validación es mecánica, NO citable.
   Manifest durable: `finetuning/manifests/t1_smoke_e2e_run_20260815.json`.

**El protocolo se actualizó PRE-resultado** (guards en `false` al momento de la
enmienda, trazada en `amendments`): `go_no_go` completado con los márgenes D-FT-12
firmados, `schemas.py` re-congelado (`a81c51df…`→`d026cdc3…`, causa: el enforcement),
comando congelado y catálogo agregados. La regla one-shot prohíbe cambios **después** de
observar resultados, no antes.

## 2. T-FT-032 — baseline YOLOE-26s ejecutada UNA vez (cerrada)

`run_20260815_193750_dbe_yoloe_1113f7` → promovido a
`finetuning/runs/t1_yoloe26s_baseline_bench_v3/`. **6.477/6.477 unidades, 0 fallos,
0 drops, 41.661 detecciones**, 374,5 s de inferencia (17,29 fps ef., CUDA), cobertura
verificada por el comando congelado. `errors.jsonl` vacío (0 bytes).

### 2.1 Percepción — agregado (mAP50 = **0,4193**)

| Clase | AP50 | n_gt | n_det |
|---|---|---|---|
| person | 0,7843 | 24.172 | 23.596 |
| helmet | 0,6286 | 22.949 | 16.758 |
| vest | 0,2642 | 1.863 | 1.297 |
| **bare_head** | **0,000** | **6.181** | **10** |

### 2.2 Percepción — por estrato (nunca sólo el agregado)

| Estrato | imgs | mAP50 | person | helmet | vest | bare_head |
|---|---|---|---|---|---|---|
| bench_obra_test | 62 | 0,3564 | 0,6293 | 0,6256 | 0,1705 | 0,000 |
| bench_obra_val | 85 | 0,3781 | 0,6229 | 0,6166 | 0,2727 | 0,000 |
| chv | 1.330 | 0,6423 | 0,7904 | 0,8035 | 0,3330 | — (sin GT) |
| shel5k | 5.000 | 0,4451 | 0,7084 | 0,6270 | — (sin GT) | 0,000 |

(Los «—» son `None` correctos: `bare_head` no existe en `chv` ni `vest` en `shel5k`.)

### 2.3 CR-01 — recall por fuente (nunca el combinado histórico)

| Fuente | violators | detectados | recall |
|---|---|---|---|
| bench_obra (test+val) | 60 | 1 | 0,0167 |
| shel5k | 5.248 | 0 | 0,0000 |
| **agregado por conteos** | **5.308** | **1** | **0,0002** |

### 2.4 Lo que esta baseline fija para el gate D-FT-12

- **Vía de ganancia abierta y exigible**: `bare_head` AP50 0,000 → el tuned necesita
  **≥ 0,05 absoluto**; recall CR-01 0,0002 (≪ 0,1) → la vía del rescate exige **> 0,5**.
- **Retención in-domain a proteger** (≤10 % de caída relativa, por clase y agregado):
  person 0,7843 · helmet 0,6286 · vest 0,2642 · mAP50 0,4193.
- **Gate de latencia: NO se alimenta de este run** — ver §3.

### 2.5 No comparar con la tabla histórica del doc 64

El 26s histórico reportaba recall CR-01 0,049 con **otro protocolo**: person-GT
**combinado** (n=5.313) que este protocolo prohíbe, y agregación distinta. La baseline
pareada existe exactamente para que el contraste tuned-vs-baseline sea limpio; el
contraste contra el histórico no lo es, y no se hace.

## 3. F-120.1 — nota de instrumento: cambio de energía durante la corrida

El host pasó de **batería a corriente con la corrida en curso** (entre la unidad ~2.364
y ~4.556; aviso del usuario en el momento). Consecuencias, en ambas direcciones:

- **Las detecciones NO se afectan**: el throttling cambia el reloj, no la aritmética —
  AP50/recall son válidas tal cual.
- **Las latencias de este run quedan mezcladas** entre condiciones de energía y **no son
  citables como brazo baseline del gate de latencia D-FT-12**. Ese gate se medirá
  aparte, **pareado** (baseline y tuned en la misma sesión, ambos con corriente,
  post-warmup, mismo host/runtime), cuando exista el checkpoint T1. Registrado también
  en `baseline.execution.instrument_note_power` del protocolo.

## 4. Evidencia (sha256)

Artefactos en `finetuning/runs/t1_yoloe26s_baseline_bench_v3/` (git-ignored por
D-FT-07; los hashes de abajo y el `artifact.sha256` del eval los vuelven verificables):

| Artefacto | sha256 |
|---|---|
| `detections.jsonl` | `81398d1b59932a0f1bd0888d85ecea86c501fce5a7a945be5d43ac746c9fede7` |
| `eval/eval_perception.aggregate.json` | `93874b8244e9bcfebdb3548bc5cb69df03c87e1679c289a1639456b42b8f5fec` |
| `eval/eval_perception.by_stratum.json` | `f02f3a64c0b3c892a99481bac5cdd47fec389328d29fd050175e15f1b466935b` |
| `eval/eval_cr01.by_source.json` | `e69c5ef3526249a0ed03bb0648383643b22f5d0911cdd2e8e44396e358edb14c` |
| `eval/protocol_snapshot.json` | `43f20835305c6d4b1bec150c201ce8ce7fe220394e47f4436167646b6a90c145` |

Protocolo rector: `finetuning/manifests/t1_yoloe26s_bench_v3_protocol.json`
(estado `frozen…`, `pre_result_guards.baseline_executed=true`, resto de guards `false`).

**Copia versionable de la evidencia de evaluación** (los tres JSON + `artifact.sha256`,
verificados byte a byte contra los del run):
`finetuning/manifests/t1_baseline_eval_20260815/` — así la evidencia citable de este doc
no depende del `runs/` git-ignored.

## 5. Qué queda para T1 full — todo en manos del usuario

Con T-FT-005/023/026/030/031/032/042R cerradas y D-FT-08 aprobada, **la cadena previa a
`full-authorization.json` está completa**. Lo que sigue:

1. **Emitir `full-authorization.json`** con `prepare_t1_full_authorization.py`
   (token exacto `APPROVE_D_FT_08`, bundle manifest + smoke gate + evidencia por archivo
   de las 7 gates). El verificador exige el inventario exacto de tareas.
   ✎ **2026-08-15 — PAQUETE PREPARADO Y ENSAYADO**: `finetuning/authorization/` reúne la
   evidencia de las 7 gates (incluido `t1_dft08_decision.json`, creado para **T-FT-005**,
   que no tenía artefacto previo) + `MANIFEST.sha256` + **runbook completo para Mendieta**
   basado en la wiki del CCAD. El flujo `prepare` → `verify` se ensayó **localmente** con
   un simulacro de la raíz de autorización: `gates=7`, `verify exit 0`, y **prueba
   negativa** (alterar un archivo de evidencia ⇒ `evidence hash mismatch for T-FT-005`;
   verde al restaurar). **Dos hallazgos del ensayo:** (a) cuatro archivos de evidencia
   **nunca viajaron** — el bundle r20 es del 08-13 y dos se produjeron el 08-15; (b) el
   script **no puede correr en el login** de Mendieta (Python 3.6 vs `from __future__
   import annotations`, 3.7+): va **dentro del contenedor Apptainer**, con el bind de la
   raíz **sin `:ro`** porque escribe la salida. `smoke-ready.json` **no** se puede
   preparar localmente: lo genera el clúster con un `created_at` no determinista, así que
   regenerarlo rompería el `binding`.
2. **T-FT-043**: `RUN` manual del usuario en Mendieta (10 épocas, envelope
   1 GPU/10 CPU/60 GB/2 h). Cero jobs full al cierre de este doc.
   ✎ **2026-08-15 (noche) — EJECUTADO. T1 full ENVIADO al clúster.** La misma noche del
   paquete: evidencia subida y verificada por hash en Mendieta (8/8 archivos),
   `full-authorization.json` **emitida dentro del contenedor Apptainer** y verificada
   independiente (`gates=7`, D-FT-08 registrada), `TEST_ONLY_T1_10_EPOCHS` en verde, y
   `RUN_T1_10_EPOCHS` encolado: **`job_id=1167640`** (cluster `ivb`, partición `multi`,
   1 GPU/10 CPU/60 GB/2 h). Al encolar: estado `PD`, último en prioridad de su partición,
   inicio estimado por Slurm 2026-08-17 ~06:20. Un watcher en `tmux` del head node
   dispara la finalización (colecta de artefactos) al terminar el job; el seguimiento es
   por consulta (`squeue`/`sacct` vía el helper de conexión). Con esto **T-FT-043 queda
   CERRADA**; el paso 3 (T-FT-050→052) queda a la espera del checkpoint.
3. Al volver el checkpoint: T-FT-050 (promoción por hash al catálogo
   `yoloe-26s-ft-t1.yaml`, ya preparado) → T-FT-051 (eval única con
   `evaluate_t1_bench_v3.py --arm tuned`) → T-FT-052 (go/no-go con los márgenes ya
   firmados — no se negocian después de ver el resultado) → medición pareada de
   latencia (§3).

> ✎ **2026-08-16/17 — todo el punto 3 se ejecutó y la jornada cerró.** El job corrió el 16/08
> (`COMPLETED`, 10/10 épocas, 13m08s; arrancó seis horas antes de la estimación de Slurm de
> arriba). El 17/08 se cerraron T-FT-044/050/051/052: **veredicto D-FT-12 = NO-GO**
> ([doc 123](123-cierre-jornada-t1-no-go.md)). La **baseline de este doc es el brazo de
> comparación** de ese resultado: `bare_head` 0,000 → **0,0455**, recall CR-01 agregado
> 0,0002 → **0,2089**, y la retención que este doc dejó "a proteger" se rompió en `person`
> (0,7843 → 0,6932, **−11,62 %** sobre un tope de 10 %). La **medición pareada de latencia no
> se hizo**: no es decisión-relevante y F-120.1 (§3) dejó este brazo sin latencias citables
> (F-123.1).

## 6. Suites al cierre (todo corrido el 2026-08-15)

| Suite / verificador | Resultado |
|---|---|
| media-plane (tras el enforcement) | **665 passed, 5 skipped**; Ruff limpio |
| `finetuning/tests/` | **46 passed** (42 + 4 del comando congelado) |
| `datasets/tests/` | **418 passed** |
| Verificadores 96 / 109 / kit | verdes (ver doc 119 §8.2 para el detalle del frente A) |
