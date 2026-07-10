# Implementación de G0 — resultados verificados y deuda que deja

- **Fecha:** 2026-07-10
- **Qué se ejecutó:** el plan `e-ovrt_control-plane/docs/superpowers/plans/2026-07-09-g0-granularidad-escena.md`
  (9 tareas, TDD, revisión por tarea + revisión final de rama).
- **Rama:** `feature/control-service` (sin commitear al momento de escribir esto).
- **Estado:** **gate del motor alcanzado.** `pytest -q --ignore=tests/labs` → **52 passed, 0 failed**;
  `ruff check src tests` limpio.

## 1. Qué cambió

La clave de estado del motor pasó de `detection_id` (id inestable, re-enumerado frame a
frame) a la **escena**: `(pattern_id, source_id)`. `granularity: scene | subject` es ahora
un campo del patrón, con default `scene`. `detection_id` **ya no se usa como identidad,
nunca** — hay un test que lo blinda.

Decisiones implementadas: ADR-002 (G0 núcleo / G1 demostrativa), ADR-011 (cooldown
permanece en el motor sin uso por la plataforma), ADR-012 (memoria de cobertura inaplicable
bajo escena), ADR-013 (detección de fuente no temporal).

## 2. Resultados verificados

### 2.1 Gate de merge: F1 = 1.0 en ambas granularidades

Sobre el fixture temporal migrado a `clip_gt.v2` (episodios escena-condición) y su variante
con `track_id`. El gate se verificó **significativo, no tautológico**: los frames esperados
se derivaron a mano desde (fixture + semántica de escena + umbrales del pattern set) antes
de mirar la salida del motor, y coincidieron.

| Granularidad | Alertas | precision | recall | F1 |
|---|---|---|---|---|
| `scene` | CR-01 @ f4, CR-02 @ f5 | 1.0 | 1.0 | 1.0 |
| `subject` | CR-01 @ f5 (worker_a), CR-02 @ f7 (worker_c) | 1.0 | 1.0 | 1.0 |

Se probó además, por mutación, que el matching de episodios de escena es inmune a
`pattern_id != condition_id` (se renombró el patrón a `PR-01` manteniendo
`condition_id: CR-01` y el F1 siguió en 1.0). Sin esa protección, `cr01_cr02_v2` habría dado
F1 = 0 en silencio.

### 2.2 ADR-012 **confirmado**, no falsificado

El ADR-012 se declaró falsable por test. La primera versión del test tenía poco poder
discriminante (un solo frame de *clear* ⇒ `elapsed = 0`, de modo que cualquier
`resolve_after_ms > 0` pasaba). Se reemplazó por un **par discriminante**:

- parpadeo del EPP durante 3 frames consecutivos (100 ms totales) con `resolve_after_ms = 2000`
  ⇒ **no resuelve, no re-alerta**;
- cobertura sostenida más allá de la ventana (2400 ms) ⇒ **resuelve**.

Verificado por mutación: con `resolve_after_ms = 50` el primer test falla; con `1e9` falla el
control. La histéresis **sí** subsume la memoria de cobertura a la escala temporal de la
plataforma. La decisión se sostiene.

### 2.3 El BENCH agrupa por escena — por diseño, sin pérdida de información

Predicho en el plan. Bajo escena, una imagen con dos personas descubiertas emite **una**
alerta con `subjects_in_evidence_max = 2`, no dos alertas.

Medición original (2026-07-09, sobre `run_20260704_205708`, 82 imgs — **artefacto podado**,
ver doc 33):

| | CR-01 | CR-02 | total |
|---|---|---|---|
| Motor viejo (por persona) | 61 | 76 | **137** |
| Motor nuevo (por escena) | 40 | 37 | **77** |
| Σ `subjects_in_evidence_max` | **61** | **76** | **137** |

**Re-verificado el 2026-07-10** sobre un BENCH regenerado con GDINO fresco
(`run_20260710_025433`, 114 imgs de `bench_v2_val`), ya que el input original fue podado:

| | CR-01 | CR-02 | total |
|---|---|---|---|
| Personas descubiertas (semántica por-persona) | 72 | 69 | **141** |
| Alertas de escena emitidas | 42 | 35 | **77** |
| Σ `subjects_in_evidence_max` | **72** | **69** | **141** |

77 claves de escena distintas, una por imagen-patrón. **El invariante se sostiene exacto,
condición por condición, sobre datos nuevos.** La información no se pierde: se reagrupa.
El baseline del doc 33 §2 corresponde al motor pre-G0 y **no se re-litiga** con estos
números.

### 2.4 La detección de fuente no temporal funciona sobre corridas reales

`configs/fase0_dbe_gdino_bench_rerun.yaml` → `{"state": "not_applicable", "causes": ["non_temporal_source"]}`.
`configs/fase0_dbe_gdino_bench_persistence_probe.yaml` → suma
`persistence_unreachable_on_non_temporal_source`, con `alerts_count: 0`. Lo que el doc 33 §4
midió a ciegas, la plataforma ahora lo declara sola.

Durante la implementación aparecieron dos estados que el ADR-013 no había previsto y que
reintroducían el cero silencioso por otra puerta; se agregaron al ADR: sin unidades
procesadas ⇒ `applicable_not_computed / no_units_processed`; `source_type` mezclados ⇒
`not_interpretable / mixed_source_types`. Y `cause` (string) pasó a `causes` (lista), para
que el reporte de la spec 44 mapee contra la taxonomía cerrada en vez de parsear separadores.

## 3. Corroboración empírica de la limitación D2 del doc 07

El doc 07 §D2, contraargumento 2, declaraba: *"SDR y duración de episodio se contaminan si
distintas personas alternan la condición dentro del mismo episodio de escena"*. La
implementación lo **demostró**, sin buscarlo.

En el fixture temporal, `worker_b` (riesgo transitorio, descubierto en los frames 2–3) no
puede confirmar por sí solo (2 frames < umbral de 3). Pero bajo agregación de escena su
evidencia **adelanta el reloj** del episodio: la condición de escena arranca en f2, no en f3
cuando `worker_a` se saca el casco, y CR-01 confirma en f4 en vez de f5.

**La consecuencia hay que decirla de frente, y va más allá de un comentario en el fixture:**
bajo escena, la persistencia ya no mide que *el mismo riesgo* se sostenga, sino que *la
escena exhiba la condición de forma continua* — posiblemente por relevo de sujetos distintos,
cada uno brevemente descubierto. Una escena con rotación de gente puede confirmar sin que
ninguna persona haya estado persistentemente en riesgo.

Esto no es un defecto de la implementación: es la semántica declarada de G0 ("la escena está
en evidencia si ≥1 sujeto la aporta"), y desaparece bajo `subject` con `track_id`. Pero es un
caveat de la afirmación central de "riesgo sostenido" y **debe figurar en el encuadre del
informe**, no solo en el doc 07. Es, además, otro argumento para que G1 exista como
demostración (ADR-002).

## 4. Deuda que deja (ordenada por lo que bloquea)

### 4.1 Nadie produce `track_id`: el modo `subject` está muerto fuera de fixtures

`eovrt_labs/perception/tracking.py:311` (`apply_person_tracking`) escribe el id del tracker
en **`detection_id`** — el campo que G0 acaba de prohibir como identidad. El media-plane no
emite `track_id` en absoluto. Consecuencia: `eovrt-labs generate-detections --track` sobre un
patrón `granularity: subject` **siempre degrada a escena** con causa `no_track_id`.

`--track` quedó **inerte para el motor**. No es una regresión de corrección (G1 es
demostrativa, ADR-002), pero toda la rama `subject` del diseño carece de productor real.
Cierre: el port del tracker al media-plane con `track_id` como campo aditivo (spec 42 §3).
Hasta entonces, `subject` solo se ejercita con fixtures escritos a mano.

### 4.2 El overlay pierde el mapeo una-caja-por-persona

Bajo escena, `PatternEvidence.supporting` pasó a contener **las otras personas descubiertas**
(antes, para patrones de ausencia espacial, era siempre `[]`). `sinks/alerts_csv.py` las
vuelca en `supporting_labels`/`supporting_bboxes`, columnas pensadas para evidencia de EPP.
Y `frame_drawing.draw_annotations` dibuja **solo el bbox del representante**, rotulado con la
clave de escena.

Es decir: un frame con N trabajadores sin casco pinta **una sola caja**. Para los videos de
defensa (V1–V3) hay que decidir si el renderer consume `supporting_*` para pintar a los
demás, o si esos videos corren en modo `subject` — lo que remite a §4.1.

### 4.3 El estado del motor no tiene política de purga

`self._state` se keyea por `(pattern_id, subject_key)`. Bajo RTSP el `source_id` es constante
⇒ una entrada por patrón, acotado. Pero con `source_id` de alta cardinalidad (carpeta de
imágenes: una por archivo) crece O(#unidades), y `_expire_absent_subjects` solo purga si hay
`subject_absent_timeout_*` configurado. No es fatal hoy (las imágenes son `not_applicable` y
el bench es finito) ni es una regresión (la clave vieja también incluía `source_id`), pero el
**runtime live y el servicio HTTP necesitan una purga explícita** de claves resueltas antes de
sostener corridas largas o multi-fuente.

## 5. Qué NO se tocó

`_cooldown_ok` y `_maybe_alert` siguen intactos: el cooldown permanece en el motor como
capacidad no usada por la plataforma (ADR-011 §3), con su test. `eovrt_labs` no se modificó.
Los contratos son todos aditivos, sin bump de `schema_version`: un consumidor viejo de
`alerts.jsonl` o `summary.json` sigue funcionando.
