# 18 — Relevamiento: `e-ovrt_control-plane`

- **Fecha de relevamiento:** 2026-08-10
- **Reemplaza a:** `historicos/01-relevamiento-control-plane.md` (foto del 2026-07-06, histórica)
- **Método:** relevado **contra git y código**, no contra memoria. Los comandos de §2 se
  ejecutaron en esta máquina; la estructura de §3 es el árbol real; los contratos de §4
  salen de `src/eovrt_control/contracts/`. Ninguna afirmación sale de un mensaje de commit
  sin haber mirado el código.
- **Regla de este documento:** **no publica ninguna cifra de resultado.** Las métricas
  medidas viven en los cuatro índices de `e-ovrt_experimental-setup/results/`; la historia
  de capacidades, en `operacion/97`. Acá está qué es la pieza y cómo funciona.
- **Serie de ADRs:** las referencias `ADR-00NN` (cuatro dígitos) son de la **serie local
  del control-plane**, en `e-ovrt_control-plane/docs/decisions/`. Las `ADR-0NN` (tres
  dígitos) son del proyecto, en `docs/decisiones/`. Ver doc 13 §3.

---

## 1. Qué es, y qué no es

Motor de patrones de riesgo. Consume la **evidencia perceptual** que produce el
media-plane (`media.detection.v1`), evalúa **condiciones configurables** —hoy CR-01
"persona sin casco" y CR-02 "persona sin chaleco"— y emite **alertas internas trazables**.

La cadena conceptual, que sigue siendo la del doc 01 §1 y no cambió:

```
condición → patrón → evidencia perceptual → estado de patrón → alerta interna
```

**Una detección no es una alerta.** La alerta se emite solo cuando el motor confirma
persistencia temporal de la condición.

**Qué NO hace, deliberadamente:**

- **No ejecuta inferencia visual.** No carga modelos ni ve imágenes: recibe detecciones ya
  normalizadas.
- **No aplica política de notificación.** Emite un `AlertEvent` en **cada** confirmación,
  sin supresión. Cooldown, agrupación y rate-limiting son del módulo de distribución
  (ADR-011 del proyecto). El motor conserva el parámetro `realert_cooldown_*` como
  capacidad **no usada por la plataforma**: los pattern sets oficiales lo dejan sin
  configurar.
- **No distribuye alertas hacia afuera.** Publica en un bus de salida opcional; quién las
  entrega y por qué canal es el módulo de distribución (ADR-005 + ADR-016 del proyecto,
  ver `19`).
- **No hace tracking como productor.** La identidad de sujeto existe, pero como
  **decorador de fuente** opcional (§5.3), no como capacidad del emisor.

## 2. Cómo se ejecuta

```bash
cd e-ovrt_control-plane
python3.11 -m venv .venv && source .venv/bin/activate && pip install -e ".[dev]"

.venv/bin/eovrt-control serve --port 8081        # servicio HTTP (camino primario)
.venv/bin/eovrt-control replay --config <cfg>    # DBE offline desde detections.jsonl
.venv/bin/eovrt-control live --config <cfg>      # EBE en vivo, consumiendo el bus
.venv/bin/eovrt-control validate-config <cfg>
.venv/bin/eovrt-control evaluate-alerts ...      # alertas contra GT temporal
.venv/bin/eovrt-control export-alerts-csv ...

python3 -m pytest tests/ -q --ignore=tests/labs  # 312 passed (2026-08-10)
```

`tests/labs` se excluye porque no tiene numpy en este entorno.

**El servicio es el camino primario** desde el tramo de plataforma (ADR-0008 local); la
CLI se conserva para el camino offline reproducible y para diagnóstico.

## 3. Estructura del código

48 archivos bajo `src/eovrt_control/`. Los módulos y su responsabilidad:

```
src/eovrt_control/
├── cli.py                      # Typer: serve / replay / live / validate-config /
│                               #        evaluate-alerts / export-alerts-csv
├── config.py                   # ReplayConfig + PatternDefinition (region/evidence/timing)
├── contracts/                  # media.py · pattern.py · alerts.py · metrics.py · errors.py
├── engine/
│   ├── pattern_engine.py       # máquina de estados + despacho por estrategia
│   └── evaluators/
│       ├── spatial_absence.py  # E-IND: ausencia de EPP inferida por región
│       └── direct_evidence.py  # E-DIR: evidencia directa gateada por persona
├── sources/                    # el único acople a la forma de entrada
│   ├── base.py                 # MediaEventSource
│   ├── media_jsonl.py          # DBE: archivo, línea a línea
│   ├── bus.py                  # EBE: ZeroMQ SUB
│   ├── tracking.py             # decorador: asigna track_id (identidad de sujeto)
│   ├── jsonl.py · memory.py    # utilitarias / test
├── runtime/
│   ├── core.py                 # lo común a ambos caminos
│   ├── replay.py               # corrida finita (DBE)
│   └── live.py                 # corrida 1:1 con el run del media-plane (EBE)
├── service/                    # FastAPI :8081
│   ├── app.py · settings.py · run_manager.py · run_ids.py · run_request.py
│   └── routers/                # health.py · config.py · runs.py
├── sinks/                      # jsonl.py · artifacts.py · alerts_csv.py
├── transport/alert_bus.py      # publisher control.alert.v1 (XPUB, apagado por default)
├── metrics/latency.py          # instrumentación t_capture → alerta
├── evaluation/temporal.py      # evaluate-alerts: alertas vs GT temporal
└── tools/track_detections.py   # la identidad como herramienta post-hoc
```

**El acople a la entrada está aislado en `sources/`.** El motor es push-based
(`engine.process(event)` por evento), y por eso pasar de archivo a bus fue un cambio de
**fuente**, no de arquitectura.

## 4. Contratos

**Entrada** — `contracts/media.py::DetectionEvent`, espejo de `media.detection.v1`:
`run_id`, `unit_id`, `source{source_id, source_type, frame_index, timestamp_ms, width,
height}`, `model`, `prompts`, `detections[]`, `timing`. Un `model_validator(mode="before")`
retro-porta campos planos históricos para poder reprocesar artefactos viejos. Los campos
extra que emite el media-plane se ignoran sin error.

**Salida** — cinco contratos versionados:

| Contrato | Qué es |
|---|---|
| `control.pattern_state.v1` | Cambio de estado por sujeto/escena, con evidencia y timestamps |
| `control.pattern_progress.v1` | Progreso parcial de un patrón, para la consola en vivo |
| `control.alert.v1` | La alerta confirmada, con `alert_id` determinista |
| `control.metric.v1` | Muestra por unidad visual: conteos y `processing_ms` |
| `control.summary.v1` | Agregados de la corrida + rutas de artefactos |
| `control.error.v1` | Error por línea o unidad — **una línea inválida no aborta la corrida** |

**`alert_id` determinista:** `uuid5(control_run_id : media_run_id : unit_id : pattern_id :
subject_key)`. Reprocesar el mismo evento produce el mismo id — idempotencia por
construcción.

Una corrida escribe `runs/<control_run_id>/`: `effective_config.yaml`,
`pattern_events.jsonl`, `pattern_progress.jsonl`, `alerts.jsonl`, `alerts.csv`,
`metrics.jsonl`, `errors.jsonl`, `summary.json`.

## 5. Configuración y catálogos

### 5.1 Config de corrida

`run{scenario, name}` · `input{type, path|bus}` · `patterns{file, active_ids}` ·
`outputs` · `logging`. **Los paths se resuelven relativos al archivo de config**, no al
CWD — trampa conocida (§8).

`input.type` acepta **`media_jsonl`** (DBE, por archivo) o **`bus`** (EBE, ZeroMQ SUB).

### 5.2 Pattern sets — cuál usar

Siete sets en `configs/patterns/`. **El oficial vigente es `cr01_cr02_v2`.**

| Set | Para qué |
|---|---|
| **`cr01_cr02_v2`** | **Oficial.** CR-01 severidad `high` / confirm 4000 ms; CR-02 `medium` / 7000 ms; `granularity: scene` |
| `cr01_cr02_v2_subject` | Idéntico al oficial salvo `granularity: subject` — la única variable |
| `cr01_cr02_edir_v1` | Variante E-DIR (evidencia directa) |
| `cr01_cr02_hyb_or_v1` | Variante de fusión por unión |
| `cr01_bare_head_v1` | Usa `bare_head` como evidencia directa |
| `cr01_cr02_temporal_eval` | Fixture sintético de persistencia temporal |
| ⚠️ `cr01_cr02_v1` | **DEPRECADO (F-DR9).** Timing por frames. **Solo smoke y tests unitarios de mecánica** — con él los episodios nunca confirman y aparecen falsos `missed` |

### 5.3 Las perillas que importan

**Evidencia** (`evidence`): `min_subject_confidence` 0.35 · `min_absent_class_confidence`
0.25 · `min_subject_area_px` 400.

**Estrategia** (`evidence.strategy`), despachada dentro de `pattern_engine.process()`:

- **`eind`** (default) — ausencia espacial: se infiere la violación por *no encontrar* el
  EPP en la región esperada.
- **`edir`** — evidencia directa gateada por persona (p. ej. `bare_head`).
- **`hyb_or`** — unión: hay evidencia si cualquiera de las dos la aporta.
- **`hyb_and`** — corroboración. **Rechazada en validación de config, a propósito**: si se
  configura, el motor falla con mensaje explícito en vez de comportarse silenciosamente
  como `eind`. Llega con el tramo de fusiones.

**Granularidad** (`granularity`): `scene` (default, clave por `(pattern_id, source_id)`) o
`subject` (clave por sujeto, requiere identidad).

**Identidad** (`input.track_persons`, default `false`): opt-in. `sources/tracking.py`
decora **cualquier** fuente, así que la identidad sirve igual en DBE y en EBE, con un
tracker **por `source_id`** — con dos cámaras, un tracker único continuaría el track de una
con las cajas de la otra por solapamiento geométrico.

**Temporales** (`timing`): `confirm_after_ms` / `resolve_after_ms` (preferidos, por
`timestamp_ms`) con fallback por frames; `subject_absent_timeout_*`; `coverage_memory_*`
(inaplicable bajo `scene`, ADR-0012 local); `realert_cooldown_*` (existe, **no se usa en
plataforma**, ADR-011 del proyecto).

## 6. Acople con los vecinos

**Aguas arriba — media-plane**, por dos caminos:

- **DBE (offline):** lee `runs/<id>/detections.jsonl`. El repositorio es la fuente de verdad.
- **EBE (live):** consume el bus ZeroMQ PUB/SUB con envelope `bus.envelope.v1` (ADR-003 del
  proyecto). La corrida es **1:1** con la del media-plane y cierra por
  `run.lifecycle.v1/run_finished` (ADR-0007 local).

**Orden de disparo, no negociable en live:** PUB/SUB pierde lo publicado antes de la
suscripción, así que se dispara **primero** `POST :8081/api/runs` con `mode: live` —cuyo
201 implica que ya está suscripto— y **después** `POST :8080/api/runs` con
`bus.enabled: true`. Los huecos de `seq` se cuentan como `bus_dropped_events` y **degradan
la corrida; nunca se silencian**.

**Aguas abajo — distribución:** `transport/alert_bus.py` publica `control.alert.v1` (XPUB,
persiste-primero, **apagado por default**). Es la única frontera de salida construida. Ver
`19`.

**Clientes HTTP:** la webconsole y el runner de `experimental-setup` (ADR-008/009 del
proyecto). **Ninguno consume el bus directamente.**

### 6.1 Endpoints

`GET /healthz` · `GET /readyz` · `GET /config` · `POST /api/runs` (201) ·
`GET /api/runs` · `GET /api/runs/current` · `GET /api/runs/{id}` ·
`DELETE /api/runs/{id}` (204) · `GET /api/runs/{id}/alerts` ·
`GET /api/runs/{id}/pattern-progress` · `GET /api/runs/{id}/pattern-events` ·
`GET /api/runs/{id}/received-units`

## 7. Estado de implementación y límites

**Construido y ejercido:** los dos caminos (DBE y EBE) con paridad verificada · el
servicio HTTP · las cuatro estrategias de evidencia (tres operativas, `hyb_and` rechazada
con causa) · las dos granularidades · identidad de sujeto como decorador · `evaluate-alerts`
con cinco métricas · la frontera de salida de alertas.

**Lo que no está:**

- **El módulo de distribución** — comprometido por ADR-016 del proyecto, aún no
  implementado. Solo existe la frontera. Ver `19`.
  ✎ **2026-08-18: superado.** El módulo está **implementado y verificado** desde el
  2026-08-12/14 (docs `operacion/114`/`118`) y desde ADR-019 además expone servicio HTTP
  propio (`:8082`, doc `operacion/124`). Lo que sigue siendo cierto de esta viñeta: la
  frontera de salida del control-plane (`alert_bus`, apagada por default) es el punto de
  acople, y este documento no la modificó.
- **`hyb_and`** — no ejecutable sin romper la comparabilidad del banco; rechazada en
  validación a propósito, no por olvido.
- **Métricas MOT** — excluidas (E-10). La ganancia de la identidad se mide en la métrica de
  la plataforma, no en MOTA/IDF1.
- **`eovrt_labs`** — paquete experimental separado (extra `.[labs]`), con su propio
  generador de detecciones y tracker IoU. **No es la percepción canónica de la plataforma:
  esa es el media-plane.** Es herramienta de calibración y de generación de fixtures. Si no
  se declara así, se lee como dos pipelines compitiendo.

**Runs no citados:** al 2026-08-10, de 41 runs en `runs/` hay 36 que no cita ningún
documento ni índice (9 con nombre de smoke o diagnóstico). Todos conservan su
`effective_config.yaml`. `runs/` está gitignoreado.

## 8. Trampas conocidas

1. **Nunca cerrar un socket ZeroMQ desde un hilo distinto del que lo creó** mientras otro
   está en `recv_multipart`: libzmq aborta el proceso con `SIGABRT`. Por eso las fuentes de
   red exponen `request_stop()` — parada cooperativa.
2. **Un decorador de fuente que no delega ciclo de vida rompe el bus en silencio.** Si no
   proxya `close`/`request_stop`/`dropped_events`, se pierden los `bus_dropped_events`
   (violación de ADR-003 del proyecto), no se cierra el socket y se anula la parada
   cooperativa — cuya alternativa es la trampa 1.
3. **`outputs.base_dir` resuelve relativo al archivo de config**, no al CWD. Ha producido
   diagnósticos falsos de "no se creó el directorio" sobre corridas que funcionaron.
4. **El pattern set `v1` produce falsos `missed`** (F-DR9). Si una evaluación da recall
   sospechosamente bajo, verificar primero qué set se usó.
5. **Colisión de directorios de run** con id autogenerado dentro del mismo segundo.
6. **Si aparece `no_track_id` en las causas bajo `granularity: subject`**, se está midiendo
   escena creyendo medir sujeto. Es la verificación que separa G0 de G1.

## Referencias

`historicos/01` (relevamiento histórico) · `19` (ciclo de vida de la alerta) · `14` (mapa de la
cadena) · `specs/41-control-plane.md` · `operacion/97` (capacidades y evidencia medida) ·
ADRs del proyecto 002/003/005/008/011/016 · ADRs locales del control-plane 0001–0013 ·
`operacion/37` y `38` (bus y servicio).
