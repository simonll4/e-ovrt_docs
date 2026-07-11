# Servicio mínimo del control-plane (:8081) — resultados

- **Fecha:** 2026-07-10
- **Qué cubre:** ítem 4 del orden de implementación de la spec 41 §10 (ADR-008: el control-plane
  deja de ser solo CLI; ADR-009: config por payload o por referencia).
- **Plan ejecutado:** `e-ovrt_control-plane/docs/superpowers/plans/2026-07-10-servicio-minimo-control-plane.md`
- **Estado:** completo, **sin commitear** (regla del workspace).

## 1. Qué quedó construido

| Pieza | Archivo |
|---|---|
| `create_app` + lifespan | `src/eovrt_control/service/app.py` |
| `RunManager` (un run activo, 409, suscripción sincrónica en live) | `src/eovrt_control/service/run_manager.py` |
| Contrato del request (payload o referencia) | `src/eovrt_control/service/run_request.py` |
| Config operacional (`EOVRT_CONTROL_RUNS_DIR`) | `src/eovrt_control/service/settings.py` |
| Validación del `run_id` como segmento de path | `src/eovrt_control/service/run_ids.py` |
| Los 7 endpoints | `src/eovrt_control/service/routers/{health,runs,config}.py` |
| `eovrt-control serve --port 8081` | `src/eovrt_control/cli.py` |
| Runtime disparable desde un objeto config + contadores en vivo | `runtime/core.py`, `runtime/{replay,live}.py` |
| Parada cooperativa de fuentes de red | `sources/base.py`, `sources/bus.py` |

| Método | Ruta | Éxito | Errores |
|---|---|---|---|
| `POST` | `/api/runs` | 201 `{"control_run_id"}` | 409 (+`active_run_id`); 422 config inválida |
| `GET` | `/api/runs/current` | 200 estado + `progress` + `subscribed` | 404 sin run activo |
| `GET` | `/api/runs/{id}` | 200 (+`summary`, `degraded`, `degradation_causes`) | 404 |
| `GET` | `/api/runs/{id}/alerts` | 200 lista de `AlertEvent` | 404 |
| `GET` | `/api/config` | 200 `effective_config` | 404 sin corridas |
| `GET` | `/healthz`, `/readyz` | 200 | — |

`/readyz` siempre responde `ready`: este plano no carga modelo. Se conserva por simetría de
plataforma (healthcheck del compose).

## 2. Suites (medidas)

| Repo | Antes | Después | Lint |
|---|---|---|---|
| control-plane (`pytest -q --ignore=tests/labs`) | 89 passed | **154 passed** | `ruff`: limpio |
| media-plane (`pytest -q`) | 456 passed | **456 passed** (sin cambios) | `ruff`: limpio |

## 3. La invariante que da sentido al servicio, y su gate

**Cuando `POST /api/runs` con `mode: live` devuelve 201, el `BusSource` ya está suscripto.**
Importa porque el orquestador dispara el media-plane *después* de ese 201, y PUB/SUB no retiene
lo publicado antes de que el suscriptor exista (spec 44 §79 fija ese orden).

El primer intento de gate era **vacuo**, y se descubrió corriendo la mutación obligatoria: al
mover la suscripción al hilo de fondo, el test seguía pasando — incluso con un `sleep(2 s)`
inyectado. La causa: el helper `wait_for_subscriber()` del publicador de prueba bloquea hasta que
llegan las notificaciones de suscripción, absorbiendo cualquier retraso.

**La invariante no es testeable por timing.** `zmq_connect` sobre un SUB es asincrónico: publicar
en el microsegundo siguiente al 201 haría perder eventos también al código correcto (por eso el
publicador real tiene su propio `wait_for_subscriber_ms`). Es una invariante de **orden de
operaciones**, y se prueba estructuralmente:

`tests/test_service_live.py::test_the_201_response_implies_the_bus_source_is_already_subscribed`
bloquea el hilo ejecutor antes de que corra y verifica que `GET /api/runs/current` ya reporta
`subscribed: true`. **Verificado discriminante por mutación**: moviendo `build_bus_source` a
`_execute`, falla (`assert False is True`). El test funcional hermano pasa igual — y su docstring
ahora dice explícitamente que no discrimina el orden.

## 4. Corrida end-to-end con los DOS servicios (criterio de terminado)

`eovrt-control serve --port 8097` + media-plane (`EOVRT_MODEL_REF=mock`) en :8098, sobre
`data/samples/videos/recorte-1.mp4`, `max_units: 30`. Orden del spec 44: **control-plane primero**.

```
[1] POST control-plane (mode=live)  -> 201 control_run_id=e2e_dos_servicios_20260710T080858Z_2e2c92
[1b] GET /api/runs/current          -> status=running  subscribed=True   <-- ANTES del media-plane
[2] POST media-plane (bus.enabled)  -> 201 run_id=run_20260710_080858_dbe_mock_786638
[3] segundo POST al control-plane   -> 409  active_run_id=e2e_dos_servicios_...
[4] la corrida cerro SOLA (run_finished) -> status=succeeded  degraded=False
      media_run_id        run_20260710_080858_dbe_mock_786638   (== run_id del POST al media-plane)
      experiment_id       exp-dos-servicios
      source              bus
      units_processed     30      == 30 lineas de detections.jsonl   (conservacion exacta)
      units_failed        0
      errors_count        0       (no hubo BusIdleTimeout: cerro por run_finished)
      bus_dropped_events  0
      alerts_count        3
      pattern_events_count 6
[5] GET /api/runs/{id}/alerts  -> 200, 3 alertas (CR-01, sev=medium)
[6] GET /api/config            -> 200, experiment_id=exp-dos-servicios
```

Los dos planos son ahora servicios config-driven y la consola/runner los orquesta por HTTP: la
simetría arquitectónica que motiva ADR-008.

Evidencia archivada en `datos/` (`runs/` es git-ignored):
`38-2026-07-10-dos-servicios-{control,media}-summary.json` y
`38-2026-07-10-dos-servicios-control-alerts.jsonl`.

## 5. Peligro de concurrencia detectado y neutralizado

`shutdown()` **no puede cerrar el socket ZeroMQ de una corrida live desde el hilo del servidor**:
libzmq aborta el proceso con `SIGABRT` (aserción en `session_base.cpp`) si se cierra un socket
mientras otro hilo está en `recv_multipart`. Ya había ocurrido en este repo durante el plan 2.

Solución: **parada cooperativa**. `MediaEventSource.request_stop()` (no-op por default) y
`BusSource.request_stop()` levantan un `threading.Event` que `__iter__` mira entre polls; el
socket lo cierra el hilo que lo creó. `test_shutdown_unblocks_a_live_run_cooperatively` falla con
`SIGABRT` si alguien vuelve a cerrarlo desde afuera. Verificado 5/5 corridas sin abortos.

Una corrida detenida así deja rastro: `BusSource` emite un `ErrorEvent` de fuente
(`error_type: "BusStopRequested"`), igual que ya hacía el cierre por idle timeout. No miente
`succeeded` en silencio.

## 6. Defectos encontrados y corregidos durante la implementación

El código de referencia del plan traía defectos reales, hallados por la revisión adversarial por
tarea y corregidos con test de regresión. Se registran porque son las trampas del dominio:

1. **Path traversal desde el payload (Critical).** `new_control_run_id` devolvía el `run.id` /
   `run.name` del usuario **sin validar**, y `runs_dir / run_id` con `run.id="../../etc/evil"`
   resolvía **fuera** de `runs_dir`. Ahora la validez del id es una **postcondición** de la
   función (levanta `ValueError` ⇒ 422), no algo que cada caller deba recordar. Verificado: 7
   nombres hostiles, 0 escapes.
2. **Config inválida del cliente respondía 500 (Critical).** El router atrapaba
   `(ValueError, FileNotFoundError)`, lista blanca demasiado angosta: un `input.bus.endpoint`
   malformado (`zmq.ZMQError`) o un `config_path` a un YAML corrupto (`yaml.YAMLError`) salían
   como error del servidor. Normalizado en la raíz con `InvalidRunConfigError(ValueError)`, **sin**
   ensanchar el `except` del router: un bug nuestro sigue siendo 500. Verificado: 6 entradas
   inválidas ⇒ 422; bug interno ⇒ 500.
3. **Run activo fantasma, permanente (Important).** `_execute` atrapaba `except Exception`: un
   `BaseException` (`KeyboardInterrupt`, `SystemExit`) dejaba el slot tomado y **todo `POST`
   posterior devolvía 409 para siempre**. La limpieza pasó a un `finally`.
4. **Por referencia, los artefactos se escribían fuera de `runs_dir` (Important).** El override de
   `outputs.base_dir` solo corría en la rama del payload; una corrida por referencia escribía en
   otro lado y después `GET /api/runs/{id}` daba 404. El dueño del `runs_dir` es el **despliegue**,
   no el experimento (ADR-009 §2).
5. **Reusar un `run.id` reportaba una corrida fallida como exitosa (Important).** Los sinks JSONL
   truncan, pero `summary.json` solo se reescribe al final: una corrida B que reusaba el id de A y
   fallaba a mitad dejaba el `summary.json` **de A** con `status: succeeded` sobre artefactos
   parciales de B. Ahora el servicio rechaza (422) un `run.id` cuyo directorio ya tiene
   `summary.json`, **sin borrar** los artefactos viejos.
6. **`alerts()` moría con 500 ante una línea corrupta (Important).** Ahora la saltea con un
   warning que nombra `run_id` y número de línea, y devuelve el resto.
7. **Gate vacuo (§3).** El más instructivo: un test que decía probar la invariante central y no
   podía fallar.
8. **Minors:** fuga de socket si `BusSource.__init__` fallaba en `connect()`; `limit` negativo con
   slicing raro; el test de `limit=-1` era vacuo (`[x][:-1] == []`) y se hizo discriminante; el
   test de path traversal pasaba por el 404 nativo de Starlette sin llegar al guard.

## 7. Corrección de un error de un doc anterior

El doc 37 §7.2 (y el handoff 36, y la memoria de arranque) afirmaban que la purga de `self._state`
del motor "pasó de teórica a real" con el runtime live. **Es falso, y se midió.** Bajo
`granularity: scene` la clave de estado es `(pattern_id, "pattern_id:source_id")`: el estado crece
con la cantidad de **`source_id` distintos**, no con el tiempo. 5000 frames de una fuente única ⇒
`len(_state) == 2`; `RtspSource`/`VideoFileSource` emiten un `source_id` **constante**. La fuga real
aparece con `granularity: subject` + `track_id` (que nadie produce todavía). Los tres documentos
fueron corregidos.

## 8. Deuda que este plan NO absorbió

1. **No hay `POST /api/runs/{id}/stop`.** Una corrida live sin `run_finished` solo termina por
   `idle_timeout_s` o por el fallback de polling; mientras tanto el servicio responde 409.
   `shutdown()` (SIGTERM) la desbloquea cooperativamente.
2. **No hay `GET /api/runs` (listado).** La spec 41 §5 no lo pide; la webconsole navega por
   `experiment_id`. Es aditivo si hace falta.
3. **Sin retención de `runs/`** (E-12): el directorio crece sin límite. Además, un `POST` con un
   endpoint de bus inválido deja un directorio huérfano (`effective_config.yaml` sin `summary.json`)
   porque `prepare_run` corre antes de `build_bus_source`.
4. **Una corrida fallida es indistinguible de una inexistente (404).** El `RunSummary` del
   control-plane no tiene campo `status`: una corrida que explotó no escribe summary, así que
   `get()` la reporta como desconocida, y el estado `failed` solo se ve por `current()` en la
   ventana efímera antes de soltar el slot. **Arreglarlo requiere estampar `status` en el summary**
   (campo aditivo) — decisión de contrato pendiente, no la tomó este plan.
5. **Una corrida detenida por `request_stop()` escribe `summary.json` sin marca de "stopped"** más
   allá del `ErrorEvent` en `errors.jsonl`. Mismo origen que el punto 4.
6. **Lectura de archivos sin acotar.** `config_path`, `patterns.file` e `input.path` son rutas
   arbitrarias elegidas por el cliente: el servicio puede leer cualquier YAML/JSONL que su usuario
   pueda leer. La **escritura** sí está confinada a `runs_dir`. Aceptado por el modelo de amenaza
   (servicio experimental, local, monousuario — E-12), pero queda declarado.

## 9. Cómo levantar la plataforma

```bash
# Terminal 1 — media-plane (carga el modelo; esperar /readyz)
cd e-ovrt_media-plane && source .venv/bin/activate
EOVRT_MODEL_REF=grounding-dino/gdino-tiny uvicorn --factory eovrt_media.service.app:create_app

# Terminal 2 — control-plane
cd e-ovrt_control-plane && source .venv/bin/activate
EOVRT_CONTROL_RUNS_DIR=runs python -m eovrt_control.cli serve --port 8081

# Terminal 3 — disparar: control-plane PRIMERO (queda suscripto), media-plane despues.
#   POST :8081/api/runs  {"mode":"live","experiment_id":"...","config":{...input.type: bus...}}
#   POST :8080/api/runs  {"ingest":{...},"prompts":{...},"bus":{"enabled":true,"endpoint":"tcp://127.0.0.1:5557"}}
```

Invertir ese orden pierde los eventos previos a la suscripción; el hueco inicial de `seq` se cuenta
como `bus_dropped_events` y la corrida se marca degradada (no se silencia). El publicador acepta
`wait_for_subscriber_ms > 0` para despliegues donde el orden no se puede garantizar.
