# Handoff — continuar el tramo plataforma (plan 2: fuentes, bus y runtime live)

> **SUPERADO EL 2026-07-10.** Todo lo que este handoff pedía está **ejecutado** — el plan 2
> (ítems 2–3: `MediaEventSource`, bus ZeroMQ, runtime live 1:1), el ítem 4 (servicio mínimo
> :8081) y la mitad media-plane del ítem 5 (instrumentación G2A). **El punto de entrada ahora
> es `operacion/50-reporte-estado-tramo-plataforma.md`** (reporte consolidado: hecho, evidencia,
> defectos, deuda y lo que falta). Detalle por tramo: docs 37 (bus/live), 38 (servicio),
> 39 (G2A). Este doc se conserva como registro del punto de partida; su §3 lleva el tablero
> tachado al día.

- **Fecha de congelamiento:** 2026-07-10
- **Para quién:** la sesión que continúa la implementación. **Este doc reemplaza al
  doc 32 como punto de entrada** — aquel describía el arranque (Paso 0 + G0), que ya
  está ejecutado y commiteado.
- **Regla de oro (sin cambios):** las decisiones están cerradas (ADR-001…014). Si algo
  parece ambiguo, la respuesta está en un ADR o un spec — no re-litigar, buscar. Si de
  verdad falta una decisión, se escribe un ADR nuevo (así nacieron ADR-012 y ADR-013).

## 1. Qué está HECHO (no re-implementar)

| Qué | Dónde quedó | Evidencia |
|---|---|---|
| **Paso 0** (Fase 0 con motor `mati`) | doc 33 | cerrado; artefacto de input luego podado, números archivados en `datos/33-*.json` |
| **G0 completo** (ítem 1 del orden spec 41 §10): `granularity: scene\|subject`, clave de estado por escena, fallback `no_track_id` por fuente, ADR-012 (memoria solo G1), expiración a escena, `degraded`/`degradation_causes`, fixture `clip_gt.v2`, `subjects_in_evidence_max`, detección de fuente no temporal (ADR-013) | commit único en `e-ovrt_control-plane` (rama `feature/control-service`) | doc 34; gate **F1 = 1.0 en ambas granularidades**, verificado significativo (frames derivados a mano; trampa `pattern_id≠condition_id` probada por mutación) |
| **Revisión exhaustiva + ajustes** | mismo commit | 10 hallazgos; los 3 de corrección arreglados: validación cruzada `level`/claves en el GT (episodio `subject` sin `subject_key` explota, no infla F1), señal `granularity_mismatch` (GT v1 vs motor G0 avisa en vez de F1=0 mudo), y causas `persistence_unreachable_...` (solo `confirm_after_frames>1` bloquea) vs `inert_temporal_thresholds` (los umbrales en ms se IGNORAN sobre imágenes — medido: `confirm_after_ms=4000` emite una alerta por imagen) |
| **Verificación real E2E** | doc 35 | GDINO-tiny real en GPU sobre video (733 frames → CR-01 confirma en t=4000ms exacto) y sobre cámara RTSP (wallclock real); aliasing de `det_NNN` MEDIDO (1831px de recorrido) |
| **Suite** | — | `pytest -q --ignore=tests/labs` → **57 passed**; `ruff check` limpio |

**Corridas vivas** (todo lo demás de `runs/` fue podado por el usuario):
- `e-ovrt_media-plane/runs/run_20260710_011320_...` (video real, 733 frames)
- `run_20260710_011715_...` (RTSP real, 3 frames)
- `run_20260710_025433_...` (BENCH regenerado, 114 imgs — input de los configs `fase0_*`/`bench_*` del control-plane)
- `e-ovrt_control-plane/runs/`: `fase0_dbe_gdino_bench_20260706` (baseline motor viejo, 137 alertas), `bench_images_*`, `verify_*`.

## 2. Qué leer, en este orden (~30 min)

1. `operacion/34-implementacion-g0-resultados-y-deuda.md` — qué cambió en el motor y la deuda que dejó.
2. `operacion/35-verificacion-e2e-video-rtsp-real.md` — qué está probado con datos reales y qué no.
3. `specs/41-control-plane.md` **§3–§4** — `MediaEventSource`, `BusSource`, runtime live (lo que sigue).
4. `specs/42-media-plane.md` **§2** — `BusPublishingArtifactWriter` (el otro lado del bus) y **§3** (tracker/`track_id`, con el aviso de bloqueante).
5. `specs/40-plataforma-etapa4-integrador.md` **§3** (envelope `bus.envelope.v1`) y **§5.2** (métricas; se implementan en el plan 4, pero el bus debe dejar los campos posibles).
6. ADR-003 (ZeroMQ), ADR-007 (corrida 1:1), ADR-013 (aplicabilidad — ya implementado en replay; el runtime live la va a necesitar).

## 3. LO QUE SIGUE: plan 2 (el camino crítico)

Orden de trabajo (spec 41 §10), con los ítems 1–4 y la mitad del 5 ya hechos:

1. ~~G0~~ ✅ (doc 34)
2. ~~**`MediaEventSource` (jsonl/memory)**~~ ✅ (doc 37)
3. ~~**Bus + runtime live**~~ ✅ (doc 37) — gate de paridad replay↔stream en verde,
   verificado significativo por mutación; corrida live E2E sobre video real, 40 unidades,
   0 perdidas, cierre 1:1 por `run_finished`, artefactos live≡replay.
4. ~~**Servicio mínimo** control-plane (spec 41 §5, :8081)~~ ✅ (doc 38) — los 7 endpoints,
   `eovrt-control serve`, corrida E2E con **los dos servicios** hablándose (30 unidades, 0
   perdidas, 409 verificado, cierre 1:1). Gate de orden ("el 201 implica suscripto") verificado
   discriminante por mutación.
5. **Instrumentación `t_capture→alert`** (spec 40 §5.2.4) — ~~mitad media-plane~~ ✅ (doc 39:
   instante de captura, `source_clock`, `g2a_ms` por unidad, bloque `g2a` en el summary).
   **← ACÁ ESTAMOS: la mitad control-plane** (`ts_receive_ms`, hitos `first_evidence_*`,
   `alert_registered_ms`, percentiles de `processing_ms`, TTFA) + pattern set `cr01_cr02_v2`
   oficial (spec 41 §7: PR-01 high `confirm_after_ms: 4000`, PR-02 `7000`, sin cooldown) +
   publisher `control.alert.v1.*` (spec 41 §8.6). Alcance completo en el **doc 50 §8.1**.
6. **experimental-setup** (spec 44). 7. **Evaluadores D1** (necesita acta `edir_v1` del usuario).

**Escribir el plan con superpowers:writing-plans antes de codear**, como se hizo con G0
(`e-ovrt_control-plane/docs/superpowers/plans/2026-07-09-g0-granularidad-escena.md` es el
modelo: código exacto, TDD, gates, gotchas verificados contra el código real).

## 4. Deuda conocida que el plan 2 debe absorber o agendar (doc 34 §4 + review)

1. **Nadie produce `track_id`** — `eovrt_labs/tracking.py:311` lo escribe en
   `detection_id` (prohibido como identidad tras G0). El port del tracker al media-plane
   (spec 42 §3) es parte natural del plan 2. Hasta entonces `granularity: subject` solo
   vive en fixtures.
2. **Purga de estado del motor** — `self._state` no se limpia sin
   `subject_absent_timeout`; necesario antes de corridas live largas (ítem 4).
3. **Overlay pinta una caja por escena** — decisión pendiente para los videos V1–V3:
   renderer que consuma `supporting`, o modo `subject` (depende de 1).
4. **Hallazgos menores de la review NO aplicados** (deliberadamente, son limpieza):
   `supporting` materializa `EvidenceRef` por frame aunque se descarte en `sustained`
   (eficiencia, `spatial_absence.py:204`); el fallback `no_track_id` vive en el evaluador
   y las causas son strings literales dispersos (altitud — extraer a `contracts` cuando
   aparezca el segundo evaluador); helpers de test triplicados sin `conftest.py`;
   `state_key` no escapa `:` (colisión plausible con `source_id` conteniendo `:`);
   `README.md:50` y `docs/architecture.md:52` del control-plane aún describen el warning
   de `det_NNN` retirado.
5. **El README del media-plane documenta un request shape viejo** (secciones
   `run.scenario`/`source`/`model` que el servicio rechaza con 422). El shape real es
   `{ingest: {plugin, config}, prompts: {set_inline: PromptSet completo, active_ids}, run:
   {name, stride, max_units, ...}}` — verificado contra `service/run_request.py`. El
   modelo NO va en el request: se fija con `EOVRT_MODEL_REF` al arrancar.

## 5. Trampas operativas (verificadas en esta sesión)

- El media-plane se levanta con `EOVRT_MODEL_REF=grounding-dino/gdino-tiny uvicorn
  --factory eovrt_media.service.app:create_app` (el paquete requiere `pip install -e .`
  si el venv se regeneró). Cargar GDINO tarda ~30–60 s; esperar `/readyz`.
- `configs/replay_hf_*.yaml` y `replay_dbe_cr01_cr02.yaml` del control-plane apuntan a
  `runs/latest`, que no existe (trampa preexistente, doc 32 §4.1).
- Quedan 14 dirs de **root** en `media-plane/runs/` (los escribió Docker two-node); solo
  salen con sudo. Docker escribiendo como root en `runs/` reaparecerá en Fase 2c — resolver
  con `user:` en el compose.
- `tests/labs/` falla por `numpy` ausente en el extra dev (conocida, no bloqueante):
  correr `pytest -q --ignore=tests/labs`.
- La retención del servicio (`gc_runs_dir`) está INACTIVA salvo que se seteen
  `EOVRT_RUNS_MAX_AGE_DAYS`/`EOVRT_RUNS_MAX_TOTAL_GB`. No borra sola.
- `runs/` es git-ignored en ambos planos: **la evidencia que un doc cite debe archivarse
  en `docs/operacion/datos/`** (lección de los docs 31/33: los artefactos se podan).

## 6. Reglas del workspace (sin cambios, no negociables)

1. Nunca commitear sin pedido explícito del usuario en ese turno.
2. Nunca `Co-Authored-By` (auditado 2026-07-10: cero ocurrencias en los 5 repos).
3. Nada en GitHub; todo local.
4. Cuidado con Docker/WSL (blast radius; la Capa 3 mata WSL).
5. Contratos SIEMPRE aditivos, sin bump de `schema_version`.

## 7. Pendiente del usuario (no avanzar solo)

1. Integrar `mati` → `main` en el control-plane (coordinación con el compañero).
2. Push del media-plane (3 commits sin pushear + el trabajo local).
3. Acta de revisión de `edir_v1` (doc 12 §2.2) — bloquea el experimento D1.
4. `sudo rm` de los 14 dirs de root, si quiere completar la poda.
