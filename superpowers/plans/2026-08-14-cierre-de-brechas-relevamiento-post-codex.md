# Cierre de brechas del relevamiento post-Codex (2026-08-14) — Plan de implementación

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Cerrar los ~30 hallazgos del relevamiento del 2026-08-14 (2 bugs graves de código en distribución, desfases doc↔código, propagación a medias de T-FT-023 y del doc 118, puertas del fine-tuning sin cerrar/derogar, licencias) dejando plataforma robusta y documentación al día, verificado mecánicamente.

**Architecture:** Remediación cross-repo en 5 bloques: (A) código de distribución (`e-ovrt_alert-distribution` + BFF de `e-ovrt_experimental-setup`), (B) resultados y verificador, (C) propagación en `docs/`, (D) puertas y encuadre del fine-tuning, (E) cierre (kit + constancia doc 119 + verificación global). Los bloques A/B/C/D son independientes entre sí **salvo**: Task 8 (steady-state) debe correr antes que Tasks 9 y 12 (citan su número), y Task 20 (doc 119) + Task 21 (verificación global) van al final.

**Tech Stack:** Python 3.11/3.12 (pytest, pydantic, paho-mqtt, FastAPI), Markdown (docs), scripts verificadores del repo `docs/`.

## Global Constraints

- **PROHIBIDO commitear/pushear**: el usuario maneja TODO el git. Ningún task tiene paso de commit. El plan termina con `git status` por repo para que el usuario commitee.
- **PROHIBIDO tocar `docs/informe/entregable/`** (la redacción §17.x espera orden explícita del usuario).
- **Nunca renumerar ni mover docs de `docs/`** (archivado lógico, ~2.800 refs por número). Correcciones dentro de un doc = enmienda fechada `[Corregido/Enmienda 2026-08-14]`, nunca reescritura silenciosa; los ADRs solo se tocan por adenda.
- **Cifras**: toda cifra nueva que entre a un índice de `results/` debe quedar cubierta por `docs/operacion/datos/96-verificar-indices.py`. Ninguna cifra se escribe a mano sin artefacto.
- **Encuadre ADR-017**: jamás escribir "falta de tiempo"/"presupuesto de tiempo" como causa; las causas son técnicas/protocolares.
- **Series de ADR**: al citar, decir la serie — `ADR-001…017` (proyecto, 3 dígitos) vs `ADR-0001…0013` (control-plane, 4 dígitos).
- Idioma de docs y mensajes: español (como el resto del set).
- Suites de referencia (deben quedar verdes al cierre): media-plane 658, webconsole backend 631 (+ los nuevos), control-plane 312, alert-distribution 69 (+ los nuevos), experimental-setup `tests/` 74.
- Venvs: webconsole backend `webconsole/backend/.venv`; control-plane `.venv`; media-plane `.venv`; alert-distribution `.venv`; experimental-setup `tests/` usa `.venv-talert`.
- Decisiones de diseño que este plan toma (el usuario puede vetarlas antes de ejecutar): **(i)** el ledger pasa a append-only con archivado por generaciones (opción "corregir el doc y aceptar la compactación" descartada porque destruye el argumento de observabilidad de 92b); **(ii)** la sonda `machinery` se **propone** derogar para T1 (D-FT-13 en estado `propuesta`, requiere firma del usuario — no se ejecuta como cerrada); **(iii)** el patrón BFF-subprocess se registra como **nota** en `estado-de-implementacion-adrs.md` (no se crea ADR-018; queda ofrecido como opcional); **(iv)** `results/evidence-runs/` se agrega a `.gitignore` (alinea la realidad con la excepción ya declarada en el README).

---

## BLOQUE A — Código: distribución de alertas

### Task 1: Ledger append-only con archivado por generaciones

El bug C-1: `DeliveryLedger.__init__` **reescribe** `notifications.jsonl` conservando solo los `delivered` (borra `suppressed_cooldown`/`failed`/`dead_letter` previos), y `Distributor.run` hace `unlink` de `dead_letter.jsonl`. Eso contradice la propiedad prometida en `92b` §2/§6/§8 ("append-only… ninguna alerta desaparece en silencio"). Nuevo diseño: al reabrir un `out_dir`, se **lee** el archivo previo (para rehidratar los `delivered`) y se **archiva íntegro** como `notifications.<n>.jsonl`; nada se borra nunca.

**Files:**
- Modify: `e-ovrt_alert-distribution/src/eovrt_distribution/ledger.py`
- Modify: `e-ovrt_alert-distribution/src/eovrt_distribution/distributor.py:51-52`
- Test: `e-ovrt_alert-distribution/tests/test_ledger.py`, `e-ovrt_alert-distribution/tests/test_distributor.py`
- Modify (doc): `docs/informe/ajustes/material-etapa-3/92b-concrecion-distribucion-alertas.md` (§6 y §8, ver Step 7)

**Interfaces:**
- Produces: `archive_previous(path: Path) -> Path | None` (módulo `ledger.py`, importable por `distributor.py`). Semántica: renombra `X.jsonl` existente a `X.<n>.jsonl` (primer `n ≥ 1` libre) y devuelve la ruta archivada; `None` si no existía.
- El resto de la API del ledger (`seen`, `append`) no cambia. `report.py` y `aggregate.py` leen `notifications.jsonl` por nombre exacto → siguen viendo solo la generación vigente (comportamiento intacto).

- [ ] **Step 1: Escribir los tests que fallan** — en `tests/test_ledger.py`, reemplazar `test_existing_file_without_deliveries_is_compacted_to_empty` (línea 71) y agregar:

```python
def test_reopen_archives_previous_file_intact_and_rehydrates(tmp_path):
    path = tmp_path / "notifications.jsonl"
    rows = [
        {"notification_id": "n1", "channel": "mqtt", "outcome": "delivered"},
        {"notification_id": "n2", "channel": "mqtt", "outcome": "suppressed_cooldown"},
        {"notification_id": "n3", "channel": "mqtt", "outcome": "dead_letter"},
    ]
    path.write_text("\n".join(json.dumps(r) for r in rows) + "\n")

    ledger = DeliveryLedger(path)

    # rehidratación: el delivered previo se reconoce
    assert ledger.seen("n1", "mqtt")
    assert not ledger.seen("n2", "mqtt")
    # el archivo previo se archivó ÍNTEGRO (3 filas), no se compactó
    archived = tmp_path / "notifications.1.jsonl"
    assert archived.exists()
    assert len(archived.read_text().splitlines()) == 3
    # la generación vigente arranca sin filas heredadas
    assert not path.exists() or path.read_text() == ""


def test_reopen_twice_increments_generation(tmp_path):
    path = tmp_path / "notifications.jsonl"
    path.write_text(json.dumps({"notification_id": "a", "channel": "mqtt", "outcome": "delivered"}) + "\n")
    DeliveryLedger(path)                      # archiva -> .1
    path.write_text(json.dumps({"notification_id": "b", "channel": "mqtt", "outcome": "failed"}) + "\n")
    DeliveryLedger(path)                      # archiva -> .2
    assert (tmp_path / "notifications.1.jsonl").exists()
    assert (tmp_path / "notifications.2.jsonl").exists()


def test_existing_file_without_deliveries_is_archived_intact(tmp_path):
    path = tmp_path / "notifications.jsonl"
    path.write_text(json.dumps({"notification_id": "x", "channel": "mqtt", "outcome": "failed"}) + "\n")
    ledger = DeliveryLedger(path)
    assert not ledger.seen("x", "mqtt")
    assert (tmp_path / "notifications.1.jsonl").read_text().count("\n") == 1
```

Y en `tests/test_distributor.py` (usar los fakes/fixtures existentes del archivo — hay un source fake y un channel dry_run; seguir su patrón):

```python
def test_rerun_over_same_out_dir_archives_dead_letter(tmp_path, ...):
    # 1ª corrida: forzar dead_letter (channel que siempre falla, max_attempts=1)
    # 2ª corrida sobre el MISMO out_dir:
    #   - dead_letter.jsonl de la 1ª debe existir como dead_letter.1.jsonl
    #   - las filas de la 1ª corrida NO desaparecen de notifications.*.jsonl (suma total)
```

- [ ] **Step 2: Correr y ver fallar**: `cd /home/simonll4/projects/e-ovrt_alert-distribution && .venv/bin/python -m pytest tests/test_ledger.py -q` → los 3 nuevos FALLAN (la compactación actual borra filas).

- [ ] **Step 3: Implementar** en `ledger.py` — eliminar `_rewrite_with_delivered_only` por completo (líneas 33-54) y reemplazar `__init__` (líneas 14-31):

```python
def archive_previous(path: Path) -> Path | None:
    """Renombra un artefacto previo a <stem>.<n>.jsonl. Nada se borra jamás:
    la generación anterior queda íntegra al lado de la vigente (92b §6)."""
    path = Path(path)
    if not path.exists():
        return None
    n = 1
    while True:
        candidate = path.with_name(f"{path.stem}.{n}{path.suffix}")
        if not candidate.exists():
            path.replace(candidate)
            return candidate
        n += 1


class DeliveryLedger:
    def __init__(self, notifications_path: Path) -> None:
        self._path = Path(notifications_path)
        self._delivered: set[tuple[str, str]] = set()
        self._path.parent.mkdir(parents=True, exist_ok=True)
        if self._path.exists():
            for line in self._path.read_text().splitlines():
                if not line.strip():
                    continue
                row = json.loads(line)
                if row.get("outcome") == "delivered":
                    self._delivered.add((row["notification_id"], row["channel"]))
            archive_previous(self._path)
```

(`import tempfile`/`os` quedan sin uso → quitarlos; `seen`/`append` no cambian.)

- [ ] **Step 4: Implementar** en `distributor.py` — reemplazar la línea 52 `dead_letter_path.unlink(missing_ok=True)` por:

```python
from eovrt_distribution.ledger import DeliveryLedger, archive_previous   # línea 17
...
archive_previous(dead_letter_path)
```

- [ ] **Step 5: Correr los tests del repo completos**: `.venv/bin/python -m pytest -q` → esperado: todos verdes (los tests 40/48 de rehidratación siguen pasando: la rehidratación se conserva; si alguno asertaba el contenido compactado del archivo, actualizar su assert a la semántica de archivado, que es el comportamiento correcto nuevo).

- [ ] **Step 6: Verificar consumidores de nombre exacto**: `grep -rn "notifications.jsonl\|dead_letter.jsonl" e-ovrt_experimental-setup/webconsole/backend/src e-ovrt_experimental-setup/tools e-ovrt_alert-distribution/src` — confirmar que todos leen el nombre exacto (generación vigente) y ninguno hace glob `notifications*.jsonl` que ahora arrastraría archivos archivados. Si alguno globa, restringirlo al nombre exacto.

- [ ] **Step 7: Alinear 92b** — en `docs/informe/ajustes/material-etapa-3/92b-concrecion-distribucion-alertas.md`: en §6, tras la frase "el ledger se rehidrata leyendo los registros `delivered` previos", agregar: `Al reabrir un directorio ya usado, la generación anterior se conserva íntegra como notifications.<n>.jsonl (y dead_letter.<n>.jsonl): el archivo vigente siempre corresponde a la ejecución en curso y ninguna fila se pierde.` En §8, en la línea del listado `notifications.jsonl # ... (append-only)`, agregar al final: `; generaciones previas archivadas como notifications.<n>.jsonl`.

### Task 2: `report.py` no puede publicar `t_alert-notification` desde un `dry_run`

El bug C-2: `_distribution_metric` decide `computed` mirando solo `latency_by_mode["live"]`, pero `latency_mode: "live"` denota la **base de tiempo** (había `confirmed_wall_ms` del bus), no que el canal MQTT fuera real. Con `channel.mode: dry_run` + control live, el summary trae `"mode": "dry_run"` (distributor.py:177) y un `live` que mide una serialización en memoria. `aggregate.py:160` ya guarda esto (exige `mode == "live"`); el reporte no.

**Files:**
- Modify: `e-ovrt_experimental-setup/webconsole/backend/src/eovrt_webconsole/experiment/report.py:317-339`
- Test: `e-ovrt_experimental-setup/webconsole/backend/tests/test_report_generator.py`

- [ ] **Step 1: Test que falla** — en `test_report_generator.py`, junto a los tests existentes de `_distribution_metric` (buscarlos con `grep -n "t_alert-notification\|_distribution_metric" tests/test_report_generator.py` y seguir su forma de construir el detail):

```python
def test_distribution_metric_dry_run_channel_never_computed():
    detail = {
        "schema_version": "control.distribution_summary.v1",
        "channel": "mqtt",
        "mode": "dry_run",
        "counts": {"delivered": 3},
        "talert_notification_ms": {"live": {"count": 3, "min": 1.0, "mean": 2.0, "p95": 7.8}},
    }
    metric = _distribution_metric(detail)
    assert metric.status == "applicable_not_computed"
    assert metric.cause == DISTRIBUTION_CHANNEL_DRY_RUN
    assert metric.value is None


def test_distribution_metric_live_channel_still_computed():
    detail = {
        "mode": "live",
        "counts": {"delivered": 3},
        "talert_notification_ms": {"live": {"count": 3, "min": 1.0, "mean": 2.0, "p95": 7.8}},
    }
    assert _distribution_metric(detail).status == "computed"
```

- [ ] **Step 2: Correr y ver fallar**: `cd .../webconsole/backend && .venv/bin/python -m pytest tests/test_report_generator.py -q` → FAIL (`DISTRIBUTION_CHANNEL_DRY_RUN` no definido / status `computed`).

- [ ] **Step 3: Implementar** — declarar la causa junto a las existentes (buscar dónde viven `NO_DISTRIBUTION`/`DISTRIBUTION_WALL_CLOCK_DBE_ONLY` con grep y agregar al lado):

```python
DISTRIBUTION_CHANNEL_DRY_RUN = (
    "canal en dry_run: la latencia no atraviesa un broker MQTT real; "
    "la metrica operativa exige channel.mode=live (92b SS8)"
)
```

y en `_distribution_metric`, después del guard `if not distribution_detail:` (línea 325-327), insertar:

```python
    if distribution_detail.get("mode") != "live":
        return MetricResult(name="t_alert-notification", unit="ms",
                            status="applicable_not_computed",
                            cause=DISTRIBUTION_CHANNEL_DRY_RUN)
```

Actualizar el docstring de la función: agregar `El summary ademas declara el modo del canal ('mode'): dry_run nunca produce una metrica computed, aunque latency_mode sea 'live'.`

- [ ] **Step 4: Correr la suite del backend completa**: `.venv/bin/python -m pytest -q` → esperado: 631+2 pass (si algún test existente construía un detail sin `"mode"` y esperaba `computed`, agregarle `"mode": "live"` — eso es el fix haciendo su trabajo).

### Task 3: El stderr del distribuidor deja de descartarse (log redactado)

B-1: `runner.py` lanza `eovrt-distribute` con `stderr=DEVNULL` y ante fallo levanta "salida omitida para no exponer configuracion sensible". Diagnóstico imposible. Nuevo comportamiento: stderr → `<consolidated>/distribution/stderr.log`, con los valores de `EOVRT_MQTT_PASSWORD`/`EOVRT_MQTT_USERNAME` enmascarados, y el error incluye las últimas líneas redactadas.

**Files:**
- Modify: `e-ovrt_experimental-setup/webconsole/backend/src/eovrt_webconsole/experiment/runner.py` (zona líneas 420-450; leer la función completa que arma el subprocess antes de tocar)
- Test: `e-ovrt_experimental-setup/webconsole/backend/tests/test_consolidation.py` o el archivo donde hoy se testea el lanzamiento del distribuidor (localizar con `grep -rln "eovrt-distribute\|create_subprocess_exec" tests/`)

- [ ] **Step 1: Leer la función real** que hace `asyncio.create_subprocess_exec` (runner.py:428-431 y su contexto) para ver si el proceso es de larga vida (live) o corto (replay). **Peligro real a evitar: deadlock por pipe lleno** — el hijo puede escribir mucho stderr; hay que drenarlo concurrentemente, nunca esperar al exit para leer.

- [ ] **Step 2: Test que falla** — con un ejecutable fake (script sh en tmp_path que escribe a stderr un texto que incluye el valor de `EOVRT_MQTT_PASSWORD` y sale con código 3), monkeypatcheando el resolver del binario y la env:

```python
async def test_distribution_failure_persists_redacted_stderr(tmp_path, monkeypatch):
    fake = tmp_path / "eovrt-distribute"
    fake.write_text("#!/bin/sh\necho \"boom secreto=$EOVRT_MQTT_PASSWORD\" 1>&2\nexit 3\n")
    fake.chmod(0o755)
    monkeypatch.setenv("EOVRT_DISTRIBUTION_EXECUTABLE", str(fake))
    monkeypatch.setenv("EOVRT_MQTT_PASSWORD", "hunter2")
    with pytest.raises(RuntimeError) as exc:
        ...  # invocar el camino real del runner que lanza distribución (seguir el arnés de tests existente)
    log = (out_dir / "distribution" / "stderr.log").read_text()
    assert "boom" in log and "hunter2" not in log and "***" in log
    assert "hunter2" not in str(exc.value)
    assert "stderr.log" in str(exc.value)
```

- [ ] **Step 3: Implementar**: `stderr=asyncio.subprocess.PIPE` + task lector concurrente que acumula (cap 1 MiB, descartando lo más viejo) y al terminar escribe el log redactado:

```python
def _redact(text: str) -> str:
    for var in ("EOVRT_MQTT_PASSWORD", "EOVRT_MQTT_USERNAME"):
        value = os.environ.get(var)
        if value:
            text = text.replace(value, "***")
    return text
```

En el camino de error, reemplazar el mensaje "salida omitida…" por: `f"distribution exit {returncode}; stderr redactado en {stderr_path}; ultimas lineas: {tail}"` donde `tail` son las últimas ~10 líneas redactadas. En el camino de éxito, escribir el log igual (vacío o con warnings del hijo: también es evidencia).

- [ ] **Step 4: Correr**: test nuevo PASS + suite backend completa verde.

### Task 4: Preflight de distribución (el experimento no muere al final)

B-2: `preflight` solo valida media y control; un manifiesto con `runs.distribution` gasta minutos de GPU y muere al final si falta el binario o el broker. Agregar: (a) binario resolvible, (b) si el YAML del distribuidor declara `channel.mode: live` → TCP connect a `channel.host:port` (timeout 2 s).

**Files:**
- Modify: el módulo de preflight — localizarlo primero: `grep -rn "preflight" e-ovrt_experimental-setup/webconsole/backend/src/ --include="*.py" -l` (la auditoría lo cita como `preflight.py:30-60`; no está en `experiment/`, puede vivir en otro paquete del backend)
- Modify: `runner.py` — extraer la resolución del binario (hoy inline, con fallback hardcodeado en línea ~113) a una función reutilizable
- Test: el archivo de tests del preflight existente (localizar con `grep -rln "preflight" tests/`)

**Interfaces:**
- Produces: `resolve_distribution_executable() -> Path` en `runner.py` — orden: `EOVRT_DISTRIBUTION_EXECUTABLE` → `shutil.which("eovrt-distribute")` → fallback al repo hermano (el actual). Lanza `FileNotFoundError` con mensaje que menciona la env var. La consume el preflight y el propio runner (una sola verdad).

- [ ] **Step 1: Tests que fallan** (en el archivo de tests del preflight, siguiendo su arnés):

```python
def test_preflight_fails_when_distribution_executable_missing(monkeypatch, ...):
    monkeypatch.setenv("EOVRT_DISTRIBUTION_EXECUTABLE", "/no/existe")
    # manifiesto con runs.distribution -> preflight debe reportar el fallo ANTES de correr nada

def test_preflight_fails_when_live_broker_unreachable(monkeypatch, tmp_path, ...):
    # config del distribuidor con channel.mode: live, host 127.0.0.1, port en un puerto cerrado
    # monkeypatch de socket.create_connection -> ConnectionRefusedError
    # preflight debe fallar con causa "broker MQTT inalcanzable"

def test_preflight_skips_broker_check_for_dry_run(...):
    # channel.mode: dry_run -> no intenta conectar
```

- [ ] **Step 2: Correr y ver fallar.**

- [ ] **Step 3: Implementar**: en runner.py la extracción de `resolve_distribution_executable()` (mismo comportamiento actual + `shutil.which` intercalado — esto cierra también el hallazgo A-2); en preflight, si el manifiesto trae `runs.distribution`: resolver binario; leer el YAML de `runs.distribution.config`; si `channel.mode == "live"`, `socket.create_connection((host, port), timeout=2)` con `contextlib.closing`. Mensajes de error accionables (mencionar `EOVRT_DISTRIBUTION_EXECUTABLE` y el broker esperado).

- [ ] **Step 4: Correr**: tests nuevos PASS + suite backend verde.

- [ ] **Step 5: Documentar el requisito del contenedor**: en `e-ovrt_experimental-setup/infra/platform/README.md`, sección de la consola, agregar: `La consola dockerizada NO ve el repo hermano e-ovrt_alert-distribution: para orquestar distribución dentro del contenedor es OBLIGATORIO montar el binario y setear EOVRT_DISTRIBUTION_EXECUTABLE.`

### Task 5: Endurecimiento MQTT + base de tiempo del cooldown

B-3 (cliente muerto se reintenta contra sí mismo) y B-4 (el cooldown compara tiempo de media contra wall-clock en la misma clave).

**Files:**
- Modify: `e-ovrt_alert-distribution/src/eovrt_distribution/channels/mqtt.py`
- Modify: `e-ovrt_alert-distribution/src/eovrt_distribution/policy.py`
- Test: `e-ovrt_alert-distribution/tests/test_channel_mqtt.py`, `e-ovrt_alert-distribution/tests/test_policy.py`

- [ ] **Step 1 (B-4): Tests de policy que fallan**:

```python
def test_cooldown_never_compares_media_time_against_wall_clock():
    policy = NotificationPolicy(cooldown_ms=30000)
    env_media = _env(condition_id="cr01", source_id="cam1", media_timestamp_ms=1000.0)
    env_wall = _env(condition_id="cr01", source_id="cam1", media_timestamp_ms=None)
    policy.mark_notified(env_media, now_wall_ms=1.7e12)
    # bases distintas => nunca suprimir por una comparación inválida
    assert not policy.is_suppressed(env_wall, now_wall_ms=1.7e12 + 1)

def test_cooldown_media_base_still_suppresses_within_window():
    policy = NotificationPolicy(cooldown_ms=30000)
    a = _env(condition_id="cr01", source_id="cam1", media_timestamp_ms=1000.0)
    b = _env(condition_id="cr01", source_id="cam1", media_timestamp_ms=2000.0)
    policy.mark_notified(a, now_wall_ms=0.0)
    assert policy.is_suppressed(b, now_wall_ms=0.0)
```

(`_env` = helper del archivo de tests existente; si construye `NotificationEnvelope` directo, seguir ese patrón.)

- [ ] **Step 2 (B-4): Implementar en `policy.py`** — guardar la base junto al timestamp:

```python
def _time(self, env: NotificationEnvelope, now_wall_ms: float) -> tuple[str, float]:
    if env.media_timestamp_ms is not None:
        return ("media", env.media_timestamp_ms)
    return ("wall", now_wall_ms)

def is_suppressed(self, env: NotificationEnvelope, now_wall_ms: float) -> bool:
    if self.cooldown_ms <= 0:
        return False
    base, t = self._time(env, now_wall_ms)
    prior = self._last_notified_ms.get(self._key(env))
    if prior is None:
        return False
    prior_base, last = prior
    if prior_base != base:
        return False  # bases incomparables: jamás suprimir por una resta inválida
    return (t - last) < self.cooldown_ms

def mark_notified(self, env: NotificationEnvelope, now_wall_ms: float) -> None:
    if self.cooldown_ms <= 0:
        return
    self._last_notified_ms[self._key(env)] = self._time(env, now_wall_ms)
```

Actualizar el docstring del módulo (la política ante base mixta: se registra y no se suprime). Ajustar los tests existentes que asuman el formato viejo del dict interno, si alguno lo inspecciona.

- [ ] **Step 3 (B-3): Test de canal que falla** — en `test_channel_mqtt.py` (usar el fake de paho del archivo; si no hay, monkeypatchear `paho.mqtt.client.Client`):

```python
def test_failed_publish_resets_client_so_next_attempt_reconnects(monkeypatch):
    # 1ª send: publish devuelve info con is_published() False -> SendResult(ok=False)
    # aserción: channel._client quedó en None (el próximo send reconecta)
    # 2ª send con broker "recuperado" -> se crea un cliente NUEVO (contar llamadas a connect)
```

- [ ] **Step 4 (B-3): Implementar en `mqtt.py`** — agregar `_reset_client` y llamarlo en los dos caminos de fallo de `_send_live`:

```python
def _reset_client(self) -> None:
    client = getattr(self, "_client", None)
    self._client = None
    if client is None:
        return
    for op in ("loop_stop", "disconnect"):
        try:
            getattr(client, op)()
        except (OSError, RuntimeError, ValueError):
            logger.debug("fallo %s durante reset del cliente MQTT", op, exc_info=True)
```

En `_send_live`: tras `if not info.is_published(): self._reset_client(); return SendResult(ok=False, ...)` y en el `except (OSError, RuntimeError, ValueError)` → `self._reset_client()` antes del return. Así los reintentos del `Distributor` (3 × 500 ms) reconectan en vez de golpear un cliente muerto. **No** agregar backoff ni sesiones persistentes (ADR-005 del proyecto recorta a retry mínimo — serie de 3 dígitos).

- [ ] **Step 5: Correr todo el repo**: `.venv/bin/python -m pytest -q` → verde.

### Task 6: Testigo MQTT — fix del `NameError` + suite de tests propia

E-6: en `mqtt_witness.py:79-91`, si `timeout_s <= 0` (deadline ya vencido) el `while` no ejecuta y la línea 90 usa `observed` sin ligar → `NameError` en vez de `GateViolation`. E-2: el testigo es la evidencia independiente de la cifra citable y no tiene ningún test.

**Files:**
- Modify: `e-ovrt_experimental-setup/tools/talert_campaign/mqtt_witness.py:79-91`
- Create: `e-ovrt_experimental-setup/tests/test_talert_mqtt_witness.py`

- [ ] **Step 1: Test que falla**:

```python
def test_wait_for_ids_with_expired_deadline_raises_gate_violation_not_nameerror():
    witness = MqttWitness(...)  # construible sin conectar (no llamar start/connect)
    with pytest.raises(GateViolation) as exc:
        witness.wait_for_ids({"n1"}, timeout_s=0.0)
    assert "missing notification IDs" in str(exc.value)
```

Más 3 tests de lógica pura (sin broker): (a) `wait_for_ids` retorna cuando `_messages` ya contiene los ids (inyectarlos directo en la estructura interna bajo el lock); (b) `snapshot()` calcula `multiplicity` correcta con duplicados; (c) un error en `_errors` hace que `wait_for_ids` lance `GateViolation` con ese texto.

- [ ] **Step 2: Correr y ver fallar** con el venv correcto: `cd /home/simonll4/projects/e-ovrt_experimental-setup && .venv-talert/bin/python -m pytest tests/test_talert_mqtt_witness.py -q` → el primero muere con `NameError`.

- [ ] **Step 3: Fix mínimo** en `wait_for_ids`:

```python
def wait_for_ids(self, expected: set[str], timeout_s: float = 5.0) -> None:
    deadline = time.monotonic() + timeout_s
    observed: set[str] = set()
    while time.monotonic() < deadline:
        ...
```

- [ ] **Step 4: Correr**: los 4 tests PASS; suite `tests/` completa del repo verde (74 + 4, con el fix de Task 10 aplicado o pendiente — anotar si el test de evidence sigue rojo porque Task 10 aún no corrió).

### Task 7: Menores de robustez (integración MQTT, doble consolidación, barrera del bus, shim media-plane)

**Files:**
- Modify: `e-ovrt_alert-distribution/tests/test_mqtt_live.py`
- Modify: `e-ovrt_experimental-setup/webconsole/backend/src/eovrt_webconsole/experiment/runner.py` (rama replay, ~695 y ~754)
- Modify: `e-ovrt_media-plane/src/eovrt_media/service/routers/runs.py:10` y `e-ovrt_media-plane/tests/test_eval_api.py:139`
- Investigar: `wait_for_subscriber` (E-4)

- [ ] **Step 1 (E-3): skip limpio del test de integración** — en `test_mqtt_live.py`, envolver la conexión: ante `ConnectionRefusedError`/`TimeoutError`/`OSError` → `pytest.skip(f"broker MQTT no disponible en 127.0.0.1:1883: {exc}")`. Verificar: `.venv/bin/python -m pytest -m integration -q` sin broker → `1 skipped` (hoy: `1 failed`). Documentar en el README del repo cómo correrlo con broker levantado (`amqtt -c infra/platform/mosquitto/amqtt.yaml` desde experimental-setup).

- [ ] **Step 2 (E-5): doble consolidación en replay** — leer `runner.py:690-760`: la rama replay llama `_consolidate_runs` (≈695) y luego `_write_report_if_possible` vuelve a consolidar (≈754). Hacer que `_write_report_if_possible` reciba/detecte que la consolidación ya ocurrió (parámetro `already_consolidated: bool = False` o chequeo de `manifest.effective.yaml` existente) y no repita. Test: espiar con monkeypatch un contador sobre `_consolidate_runs` en el camino replay → exactamente 1 llamada. Suite backend verde.

- [ ] **Step 3 (E-4): barrera de suscripción del bus** — descubrir el plumbing: `grep -rn "wait_for_subscriber\|subscriptions_expected" /home/simonll4/projects/e-ovrt_control-plane/src /home/simonll4/projects/e-ovrt_alert-distribution/src /home/simonll4/projects/e-ovrt_experimental-setup/tools /home/simonll4/projects/e-ovrt_experimental-setup/experiments`. El publisher (`alert_bus.py`) espera `expected=1` suscripción, pero `ZmqSource` del distribuidor emite **dos** SUBSCRIBE (alertas + lifecycle) y `campaign.yaml` declara `subscriptions_expected: 2`. **Si** el valor es plumbeable por config en el camino que usa la campaña → pasarlo (2) y agregar test de regresión en el repo dueño. **Si** el default afecta otros flujos EBE existentes (riesgo de romper la barrera del acople webconsole/control) → NO tocar el default; en su lugar dejar constancia del carácter laxo de la barrera en el doc 119 §hallazgos-residuales (Task 20). No adivinar: decidir con el grep a la vista.

- [ ] **Step 4 (INFO media-plane): retirar el shim** — en `test_eval_api.py:139` importar `_mean_ap50` desde `eovrt_media.evaluation.runner`; en `routers/runs.py:10` borrar el import-alias. Correr: `cd /home/simonll4/projects/e-ovrt_media-plane && .venv/bin/python -m pytest -q` → 658 pass, y `.venv/bin/ruff check src tests` limpio.

---

## BLOQUE B — Resultados: steady-state, payload y verificador

### Task 8: Publicar el análisis steady-state y el tamaño de payload (D-2)

El p95 publicado (64,534 ms) está dominado por primeras entregas de cada corrida (77,4 % de la muestra, las más rápidas: proceso y conexión MQTT recién nacidos). El régimen sostenido (entregas 2.ª+, n=104) da p95 ≈102 ms. El design de la campaña (§10) exigía publicar ambos y el payload size; no se hizo. Nada se re-corre: todo sale de `outcomes.csv` existente.

**Files:**
- Modify: `e-ovrt_experimental-setup/tools/talert_campaign/aggregate.py`
- Modify: `e-ovrt_experimental-setup/results/realtime/t_alert_notification/metrics.json` (regenerado, no a mano), `.../README.md`
- Modify: `e-ovrt_experimental-setup/results/realtime/index.md`, `e-ovrt_experimental-setup/results/index.md`
- Modify: `docs/operacion/118-campana-t-alert-notification.md`
- Test: donde vivan los tests del agregador (`grep -rln "aggregate" e-ovrt_experimental-setup/tests/`); si no existen, crear `tests/test_talert_aggregate_steady_state.py`

- [ ] **Step 1: Leer `aggregate.py` y `outcomes.csv`** (cabecera) para confirmar nombres de columnas: se necesita la columna de latencia elegible, el identificador de corrida (`run`/`control_run_id`) y `payload_bytes` (la auditoría confirmó que existe).

- [ ] **Step 2: Test que falla** — con un CSV sintético de 2 corridas × 3 entregas:

```python
def test_steady_state_splits_first_delivery_per_run_from_subsequent(tmp_path):
    # corrida A: latencias 10, 100, 110 ; corrida B: latencias 12, 90
    # first_delivery_per_run = [10, 12] ; subsequent = [100, 110, 90]
    metrics = aggregate(...)
    assert metrics["steady_state"]["first_delivery_per_run"]["count"] == 2
    assert metrics["steady_state"]["subsequent_deliveries"]["count"] == 3
    assert metrics["steady_state"]["subsequent_deliveries"]["p95"] == 110
    assert metrics["payload_bytes"]["count"] == 5
```

- [ ] **Step 3: Implementar** en `aggregate.py`: bloque `steady_state` (partición por primera-entrega-de-su-corrida en orden temporal, mismas estadísticas y **mismo nearest-rank** que el bloque principal — reutilizar la función de percentil existente, no introducir otra) y bloque `payload_bytes` (`count/min/p50/p95/max`). Los bloques existentes de `metrics.json` no deben cambiar ni un byte.

- [ ] **Step 4: Regenerar `metrics.json` real** con el comando de agregación de la campaña (leer el README de `results/realtime/t_alert_notification/` para el comando exacto). Verificar con `git diff`: solo claves nuevas; el bloque primario (64.5341796875 / 460 / etc.) byte-idéntico. Registrar los valores reales que salgan (esperados ≈: first n=356 p95≈49,9; subsequent n=104 p95≈102; si difieren en decimales por el nearest-rank propio, **los del artefacto mandan** — usarlos en todos los pasos siguientes).

- [ ] **Step 5: Publicar la lectura** (con los valores del Step 4):
  - `results/realtime/t_alert_notification/README.md` — sección nueva: `## Régimen sostenido (steady-state)` con la tabla first/subsequent y la frase: `El p95 principal agrega todas las entregas; el 77,4 % son primeras entregas de su corrida (proceso y conexión MQTT recién creados) y resultan las MÁS rápidas. La cota honesta para operación continua es el p95 del régimen sostenido.`
  - `results/realtime/index.md` — en la fila/sección de distribución, agregar la línea secundaria: `Régimen sostenido (entregas 2.ª+ de cada corrida): p95 = <valor> ms (n = <n>); primeras entregas: p95 = <valor> ms (n = <n>).`
  - `docs/operacion/118-campana-t-alert-notification.md` — subsección nueva `### Análisis steady-state (agregado 2026-08-14)` con los mismos números, la composición 77,4 %, y la aclaración de que sale del MISMO `outcomes.csv` sin re-corrida.

- [ ] **Step 6: Correr** los tests del agregador y la suite `tests/` del repo → verdes.

### Task 9: El verificador 96 cubre `realtime/` (la cifra estrella queda blindada)

**Files:**
- Modify: `docs/operacion/datos/96-verificar-indices.py`

- [ ] **Step 1: Leer el script** (estructura de la lista de cifras y del guard de cobertura §2.1).

- [ ] **Step 2: Agregar entradas** siguiendo el formato existente:
  - `results/realtime/index.md` cita `64,534` ↔ `results/realtime/t_alert_notification/metrics.json` p95 (64.5341796875) y `n = 460` ↔ count.
  - `results/index.md` cita `64,534` ↔ ídem.
  - Las dos cifras steady-state publicadas en Task 8 (p95 sostenido y su n) ↔ claves `steady_state.*` del mismo metrics.json.

- [ ] **Step 3: Extender la cobertura §2.1**: además de `clip_bench/*` y `bench_nivel_a/*`, escanear `results/realtime/*/metrics.json` y exigir que toda campaña con metrics.json esté cubierta por al menos una CIFRA.

- [ ] **Step 4: Correr**: `cd /home/simonll4/projects/docs && python3 operacion/datos/96-verificar-indices.py` → `✅ Todo verificado` con las filas nuevas listadas `ok`. **Prueba negativa obligatoria**: editar temporalmente una cifra del índice (64,534→64,999), correr, ver que FALLA, revertir, correr de nuevo verde.

### Task 10: Menores de `results/` y del árbol de experimental-setup

**Files:**
- Modify: `e-ovrt_experimental-setup/tests/test_evidence_manifest.py:240`
- Modify: `e-ovrt_experimental-setup/results/bench_imagenes/index.md`
- Modify: `e-ovrt_experimental-setup/results/index.md` (fila L1)
- Modify: `e-ovrt_experimental-setup/.gitignore`

- [ ] **Step 1 (E-1)**: confirmar la causa del `assert 59 == 53`: `git -C e-ovrt_experimental-setup diff results/evidence-runs.yaml | grep -c "operacion/118"` — los +6 deben ser las requests manuales con `source_ref` al doc 118. Si es así, actualizar la expectativa a 59 **y** el comentario del test explicando la composición (53 previas + 6 del doc 118). Si NO coincide, detenerse y reportar (no maquillar el número). Correr: `.venv-talert/bin/python -m pytest tests/test_evidence_manifest.py -q` → verde.

- [ ] **Step 2**: tabla de descartes de `bench_imagenes/index.md` (las 6 configuraciones que no llegaron a `bench_obra`): contrastar CADA mAP (0,401 / 0,360 / 0,017 / …) contra `docs/operacion/64-…` (sección de decisiones S2). Corregir discrepancias si las hay y agregar al pie de la tabla: `Fuente: doc 64 (BENCH v2, 196 imgs — sin metrics.json mecánico; verificado a mano 2026-08-14).`

- [ ] **Step 3**: fila L1 de `results/index.md`: hoy arranca en negrita con la posición derogada ("**FAR/hora no reportable** (D-90.1)…"). Reordenar para que la negrita lidere con la posición vigente: `**FAR/hora: se reporta como conteo crudo y no sostiene cota** (enmienda a D-90.1; formulación original: "no reportable") …` conservando el resto del texto y las referencias intactas. Verificar que `sintesis/resultados-y-conclusiones.md` (que ya está alineada en sustancia) no cite textual la negrita vieja: `grep -n "no reportable" docs/sintesis/resultados-y-conclusiones.md`.

- [ ] **Step 4 (iv)**: agregar a `.gitignore` de experimental-setup la línea `results/evidence-runs/` con comentario `# copia de evidencia (120 MB): excepción de versionado declarada en README §Runs de evidencia`. Verificar: `git -C e-ovrt_experimental-setup status --short | grep -c evidence-runs/` → 0 (los archivos `evidence-runs.md`/`.yaml` en la raíz de results/ SÍ siguen trackeables — no los tape el patrón).

- [ ] **Step 5**: correr `python3 docs/operacion/datos/96-verificar-indices.py` de nuevo (los índices cambiaron) → verde.

---

## BLOQUE C — Docs: propagación y desfases

### Task 11: T-FT-023 cerrado en TODOS los sitios (defecto #1)

La frase "NO-GO por … procedencia (T-FT-023) …" quedó congelada en 14+ lugares mientras 116/117 la dan por cerrada (tar `639e60df…`). Regla de reemplazo: donde la causa del NO-GO liste procedencia/T-FT-023 como abierta, la lista pasa a ser **"contrato de serving (D-FT-08/T-FT-005), evaluación (T-FT-031) y baseline (T-FT-032)"**, y en la primera mención de cada doc se agrega: `— la procedencia (T-FT-023) quedó CERRADA el 2026-08-13 (snapshot tar 639e60df…)`.

**Files (sitios confirmados por la auditoría; verificar con grep antes de editar cada uno):**
- Modify: `docs/00-indice.md` (líneas ~14, ~224, ~268), `docs/decisiones/README.md:41`, `docs/decisiones/estado-de-implementacion-adrs.md:36`, `docs/GUIA-REDACTORES.md:191`, `docs/sintesis/fundamentos-teoricos.md:597`, `docs/sintesis/resultados-y-conclusiones.md:539`, `docs/informe/ajustes/02-etapa-2-consolidacion-metodologica.md:217`, `docs/informe/ajustes/04-etapa-4-implementacion.md:199`, `docs/informe/ajustes/05-etapa-5-evaluacion-y-validacion.md:326,336`, `docs/informe/ajustes/06-etapa-6-documentacion-y-cierre.md:133`, `docs/informe/ajustes/material-etapa-3/94-secciones-nuevas-etapa3.md:605`
- El kit (`docs/informe/project-kit/`, ×5 sitios) NO se edita a mano: se regenera en Task 19.

- [ ] **Step 1**: censo previo: `grep -rn "T-FT-023\|T023" /home/simonll4/projects/docs --include="*.md" | grep -v "informe/project-kit"` — listar todos los sitios (pueden ser más que los 14 auditados).

- [ ] **Step 2**: aplicar el reemplazo sitio por sitio (leer contexto de cada uno; la redacción exacta varía — la regla de arriba manda). Los sitios que ya están al día (operacion/100, 116, 117, CRONOLOGIA, adenda del ADR-017) no se tocan.

- [ ] **Step 3**: guard final: `grep -rn "T-FT-023" /home/simonll4/projects/docs --include="*.md" | grep -v "informe/project-kit" | grep -viE "cerrad|CERRADA|639e60df|done|snapshot"` → revisar a ojo cada línea restante: ninguna puede listar T-FT-023 como causa abierta de NO-GO.

### Task 12: El doc 118 entra a la capa de navegación; IDs; fix de §4 (defectos #2, #5, D-1, D-3, y encuadre del 115)

**Files:**
- Modify: `docs/CRONOLOGIA.md`, `docs/GUIA-REDACTORES.md`, `docs/00-indice.md`, `docs/operacion/118-campana-t-alert-notification.md`, `docs/operacion/115-soporte-experimental-metricas-reportes-consola-diferido.md`

- [ ] **Step 1 — CRONOLOGIA**: en la jornada 2026-08-13 (hoy solo habla de fine-tuning), agregar el bloque:

```markdown
**2026-08-13 (bis) — distribución de alertas: campaña `t_alert-notification` (doc 118) y soporte experimental (doc 115).**
El módulo del quinto repo (`e-ovrt_alert-distribution`) produjo la cifra citable del tramo de distribución:
**p95 = 64,534 ms (n = 460 entregas live contra broker MQTT real, testigo independiente al 100 %)** — F-118.1,
artefacto en `e-ovrt_experimental-setup/results/realtime/t_alert_notification/`. El cooldown suprimió el 44,976 %
de los eventos (F-118.2); la pata de cámara quedó `not_executed: hardware_source_not_connected` (F-118.3).
El doc 115 declara cerrado el gate de instrumentación (D-115.1: no falta un "repo de métricas") y difiere
seis frentes A–F con causa (D-115.2). La orden de arrancar la redacción sigue siendo del usuario.
```

- [ ] **Step 2 — GUIA-REDACTORES**: junto al bloque de distribución (línea ~57), agregar:

```markdown
La cifra citable del tramo de distribución es **`t_alert-notification` p95 = 64,534 ms (n = 460 entregas live)**
(`results/realtime/t_alert_notification/metrics.json`; protocolo y contención en `operacion/118`). Reglas de cita:
(1) el tramo medido es **bus de alertas → PUBACK MQTT** — NO incluye captura, inferencia ni evaluación del patrón;
(2) en régimen sostenido (entregas 2.ª en adelante, n = <n Task 8>) el p95 es **<valor Task 8> ms** — al hablar de
operación continua, citar ambos; (3) lo que NO se cita como desempeño sigue siendo el smoke de loopback — la
campaña del doc 118 sí es una cifra de la tesis.
```

Y en la sección de trampas de cita, agregar: `Trampa del banco de clips: 47 = 34 rodaje + 13 internet (bloques A/B del manifest) y, por otra partición, 32 positivos + 15 negativos. Nunca mezclar las dos descomposiciones en una misma frase.`

- [ ] **Step 3 — 00-indice**: (a) en la cabecera, restituir la línea de pendientes: `**Pendientes del usuario:** C1 URLs de los 18 clip.yaml · video V2 · la redacción §17.x espera su orden explícita.`; (b) en la fila del doc 100, re-agregar las anclas perdidas: `D-100.1 (el entrenamiento NUNCA corre en la PC local; solo clúster Mendieta) · D-100.2 · F-100.1 (resuelta por cuarta vía `finetuning_v1` — ver adenda) · F-100.2 · F-100.3 (walltime 48 h como condición técnica)`; (c) en el mapa de tramos, agregar la fila `Distribución de alertas + soporte experimental (ago 12–13) | 114, 115, 118` y verificar que la fila de fine-tuning diga `116–117`; (d) actualizar la descripción del 116 que dice "P2/procedencia y P3 siguen abiertos" → alinear con el estado real (P2 cumplido; abiertos D-FT-08/T-FT-005, T-FT-031, T-FT-032).

- [ ] **Step 4 — doc 118, IDs y §4**: (a) asignar IDs: en el resultado principal, anteponer `**F-118.1**`; al hallazgo del cooldown 44,976 %, `**F-118.2**`; al registro de la cámara `not_executed`, `**F-118.3**`. (b) Corregir §4:

```markdown
- `runs.distribution.endpoint` = SUB de ZeroMQ al bus de alertas del control-plane: `tcp://127.0.0.1:5558`.
  El broker MQTT (`tcp://127.0.0.1:1883`) NO va en este campo: vive en `channel.host`/`channel.port`
  del YAML del distribuidor (`distribution-live.yaml`).
- Manifiestos reales de la campaña: `campaign.yaml` · `distribution-live.yaml` · `distribution-replay.yaml` ·
  `video/manifest.template.yaml` · `camera/*.template.yaml` (en `e-ovrt_experimental-setup/experiments/t_alert_notification/`).
```

(reemplaza las dos líneas erróneas que mencionan `tcp://127.0.0.1:1883` como endpoint y la lista `manifest.yaml / media.yaml / control.yaml / distribution.yaml`). (c) Nota de nomenclatura donde menciona el suplementario: `El conjunto "544 runs decimado empírico (control_replay_empirico)" figura en corpus.json como supplemental_derived_ebe: son el mismo conjunto.`

- [ ] **Step 5 — doc 115, encuadre**: en las dos frases que habilitan la redacción (líneas ~121 y ~213), agregar a continuación: `Este cierre levanta el gate TÉCNICO; la orden de arrancar la redacción sigue siendo del usuario (regla vigente desde el 08-05).` Además, etiquetar las dos decisiones: `**D-115.1**` (no crear repo de métricas; el soporte es un subsistema transversal) y `**D-115.2**` (diferir los frentes A–F) en el punto donde cada una se declara.

- [ ] **Step 6**: guard: `grep -n "64,534\|F-118.1" docs/CRONOLOGIA.md docs/GUIA-REDACTORES.md docs/00-indice.md` → las tres capas la mencionan.

### Task 13: 92b coherente de punta a punta + fila T-85 en gobierno/99 (defecto #3, E-7)

**Files:**
- Modify: `docs/informe/ajustes/material-etapa-3/92b-concrecion-distribucion-alertas.md`
- Modify: `docs/informe/ajustes/gobierno/99-materiales-de-cierre.md`
- Modify: `docs/informe/ajustes/03-etapa-3-diseno-arquitectonico.md`

- [ ] **Step 1 — §11 criterios de terminado**: leer los 6 checkboxes (92b:398-410). Marcar `[x]` SOLO los que tengan evidencia real, cada uno con su referencia. Mapeo esperado: entrega MQTT real + p95 en summary → `[x] — verificado: campaña doc 118 (p95 64,534 ms, n=460, testigo MQTT 100 %)`; duplicado QoS 1 deduplicado → `[x] — tests test_ledger.py + notification_id = sha1(alert_id)[:16]`; ráfaga misma condición-fuente → una sola → `[x] — policy (condition_id, source_id) + 376 suppressed_cooldown en la campaña`. Para los otros 3: leerlos y buscar la evidencia (operacion/114 relevamiento, suite del repo, artefactos de campaña). **Si a alguno no le encontrás evidencia real, NO se marca**: se anota `— pendiente: <qué falta>` (la honestidad del checklist vale más que el verde).

- [ ] **Step 2 — el JSON ficticio**: inmediatamente antes del bloque de ejemplo con `"mode": "dry_run"` y `p95: 7.8` (92b:395-398), insertar: `> Ejemplo ILUSTRATIVO con valores ficticios (este `p95: 7.8` NO es una medición). La cifra real del tramo vive en `results/realtime/t_alert_notification/metrics.json` y en el doc 118 (p95 = 64,534 ms).`

- [ ] **Step 3 — §8 forma real del summary**: reemplazar el ejemplo plano de `talert_notification_ms` por la forma real (anidada por `latency_mode`, con los campos que emite `distributor.py`):

```json
{
  "schema_version": "control.distribution_summary.v1",
  "channel": "mqtt",
  "mode": "live",
  "counts": {"delivered": 3, "suppressed_cooldown": 2},
  "skipped_invalid_alerts": 0,
  "source_stats": {"...": "..."},
  "talert_notification_ms": {
    "live": {"count": 3, "min": 31.2, "mean": 41.0, "p95": 58.7}
  }
}
```

y corregir las rutas de salida donde diga `runs/<distribution_run>/` → `runs/<experiment_id>/distribution/{notifications.jsonl, dead_letter.jsonl, distribution_summary.json}` (ADR-014, serie del proyecto). Corregir también 92b:15 `ADR-001…016` → `ADR-001…017`.

- [ ] **Step 4 — gobierno/99 §1**: agregar la fila de inventario (la numeración termina en T-84):

```markdown
| T-85 | Latencia de notificación (distribución) | tabla corta: p95 64,534 ms (n=460) + régimen sostenido | `results/realtime/t_alert_notification/metrics.json` + `operacion/118` | §17.3.10 |
```

(ajustar las columnas al formato real de la tabla — leerla antes; la sección/redline destino es §17.3.10.)

- [ ] **Step 5 — ajustes/03**: donde se borró la frase "§17.3.10 no tiene figuras ni tablas… y eso es correcto" sin reemplazo, agregar en ese punto: `§17.3.10 tiene UNA pieza de evidencia en el inventario de cierre: T-85 (gobierno/99 §1) — la latencia de notificación medida por la campaña del doc 118.`

- [ ] **Step 6**: guard: `grep -n "\[ \]" docs/informe/ajustes/material-etapa-3/92b-*.md` → solo pueden quedar checkboxes sin marcar los que tengan anotado `pendiente:` con causa.

### Task 14: estado-de-implementacion-adrs (ADR-009/014 + nota BFF), Tabla 66, "≈1 GPU-h", síntesis L6 (defectos #6, #7, A-1 y 115 §4.F)

**Files:**
- Modify: `docs/decisiones/estado-de-implementacion-adrs.md`
- Modify: `docs/informe/ajustes/material-etapa-3/94-secciones-nuevas-etapa3.md` (Tabla 66)
- Modify: `docs/informe/ajustes/02-etapa-2-consolidacion-metodologica.md:221`, `docs/informe/ajustes/00-mapa-de-ajustes.md:141`, `docs/informe/ajustes/07-critica-de-extension.md:83` (localizar el nombre exacto del 07 con `ls docs/informe/ajustes/`)
- Modify: `docs/sintesis/resultados-y-conclusiones.md` (resumen de L6)

- [ ] **Step 1 — ADR-009**: leer `docs/operacion/115-…md` §2.2 y §4.F (la reconciliación pendiente que el propio 115 pidió). En la fila ADR-009 (línea ~29, hoy "Implementado y superado"), agregar: `Nota 2026-08-14: cumplida de forma INCOMPLETA según doc 115 §2.2 — la UI está rediseñada, pero el historial durable y la promoción runs/→results/ quedaron diferidos (frentes C/D del 115, D-115.2). La calificación "superado" describía la UI, no el ciclo de evidencia.`

- [ ] **Step 2 — ADR-014**: leer qué brecha señala 115 §4.F para ADR-014 y escribir la reconciliación equivalente en su fila (con referencia al frente del 115 que la difiere). No inventar la brecha: citarla del 115.

- [ ] **Step 3 — nota BFF-subprocess (A-1)**: en la fila de ADR-008/ADR-009 (o sección de notas del documento), agregar: `Nota 2026-08-14: para la distribución de alertas, el runner del BFF lanza eovrt-distribute como SUBPROCESO local (runner.py) — un tercer patrón de acople que ADR-008/009 (serie del proyecto) no contemplan. Decisión consciente registrada en el design 2026-08-12 de experimental-setup; consecuencia operativa: la consola dockerizada requiere EOVRT_DISTRIBUTION_EXECUTABLE (ver infra/platform/README). Si el patrón se consolida, merece ADR propia (propuesta abierta, no ejercida).`

- [ ] **Step 4 — Tabla 66 (94:~605)**: reemplazar la celda "Paridad ejercida" de la fila "Comparación DBE/EBE sobre fuente idéntica" por: `Paridad de transporte y de reparto VERIFICADA (replay/live producen artefactos de distribución idénticos). El anclaje de sincronización entre reloj de captura y tiempo de media para EBE-desde-clip sigue NO implementado (operacion/97): la paridad plena queda acotada a lo verificado.`

- [ ] **Step 5 — "≈1 GPU-h" (3 sitios)**: reemplazar en 02:221, 00-mapa:141 y 07:83 por: `costo T1 por extrapolación medida: ≈16 min centrales (prudente 30–45 min; walltime 2 h) — operacion/100 adenda; la cifra histórica "≈1 GPU-h" quedó superada`. Guard: `grep -rn "1 GPU-h\|GPU-h" docs/informe/ajustes --include="*.md"` → ninguna aparición sin la marca de superada (las de `adr-017` y `adr-015` cuerpo son historia protegida: NO tocarlas).

- [ ] **Step 6 — síntesis L6**: en el resumen de L6 de `sintesis/resultados-y-conclusiones.md`, re-agregar la cláusula que el índice canónico conserva: `Sigue en pie: no hay métricas MOT (E-10) y el track_id es post-hoc.`

---

## BLOQUE D — Fine-tuning: puertas, encuadre y licencias

### Task 15: Doc 100 — corregir el cuerpo §4 (afirmación falsa, 400K→3.096, cuarta vía)

**Files:**
- Modify: `docs/operacion/100-t1-dimensionamiento-medido.md` (§4 líneas ~173-177 y adenda)

- [ ] **Step 1**: en §4:175-177, reemplazar la afirmación falsa por:

```markdown
[Corregido 2026-08-14] La premisa original de este párrafo — "armar un val con `bare_head` que no sea
estrato de `bench_v3` hoy no existe: `bare_head` nativo solo lo trae shel5k" — resultó FALSA al auditar
el corpus: `construction_site_safety`/train aporta `bare_head` nativo (1.900 instancias en train y 408
en val de `finetuning_v1`; ver `finetuning_v1.summary.json`). El bloqueo real que F-100.1 señalaba era
la ausencia de un val CON GARANTÍAS (sin leakage por linaje), y se resolvió por la cuarta vía (split
por grupos de `finetuning_v1`).
```

- [ ] **Step 2**: en §4:~173, corregir `400 K params` → `3.096 parámetros (los 12 tensores cv3/one2one_cv3 congelados por manifiesto; "400 K" era el orden de magnitud del head completo, no del alcance entrenable real)` — el argumento anti-sobreajuste se FORTALECE; decirlo.

- [ ] **Step 3**: en la adenda 08-13 del mismo doc, agregar el punto: `F-100.1 se resolvió por una CUARTA vía no listada en §4 (split propio finetuning_v1 por grupos, D-FT-11/D-FT-01, aprobadas por el usuario el 2026-08-13). Las tres enmiendas originales de §4 quedan históricas. (ADR-017 §2d hablaba de "las tres enmiendas": esta nota deja constancia de que lo ejecutado fue una cuarta, superadora.)`

### Task 16: Enmienda vest→bare_head, derogación PROPUESTA de la sonda, retención OV, smoke≠training

**Files:**
- Modify: `docs/contingencia/20-investigacion-finetuning-condicionada-e04.md`
- Modify: `docs/operacion/117-decisiones-y-tareas-finetuning.md`
- Modify: `docs/operacion/116-plan-maestro-finetuning.md`
- Modify: `docs/operacion/100-t1-dimensionamiento-medido.md` (§6.2, un marcador)
- Modify: `docs/informe/ajustes/05-etapa-5-evaluacion-y-validacion.md` (bloque fine-tuning)

- [ ] **Step 1 — enmienda de clase objetivo** (hallazgo 2): en `contingencia/20`, después de la fila T1 de la tabla §6 (o al final de §4.3 — leer y elegir el punto de anclaje natural), insertar:

```markdown
### Enmienda 2026-08-14 — clase objetivo de T1: de `vest` a `bare_head` (pre-resultado)

La pre-registración original de este documento fijaba `vest` como hipótesis de T1 (§4.3 "¿10 épocas
rescatan la clase que el vocabulario zero-shot no trae?"; tabla §6, fila T1). D-FT-12 (doc 117) propone
`bare_head` como clase objetivo: es evidencia directa de CR-01 y tiene 6.181 anotaciones en `bench_v3`
(vs 1.863 de `vest`). Consecuencia declarada que motiva registrar esto como ENMIENDA y no como matiz:
cambia qué estrato del bench carga el resultado — `vest` no existe en shel5k y `bare_head` no existe
en chv. La enmienda es PREVIA a cualquier resultado de entrenamiento full (0 jobs full al 2026-08-14)
y queda supeditada a la aprobación de D-FT-12 por el usuario.
```

En `117`, dentro de D-FT-12, agregar: `Esta decisión constituye una ENMIENDA a la pre-registración de contingencia/20 §4.3/§6 (registrada allí el 2026-08-14): la hipótesis original era vest.`

- [ ] **Step 2 — sonda de clase nueva** (hallazgo 1): en `117`, agregar la decisión (siguiendo el formato de las D-FT existentes):

```markdown
### D-FT-13 — sonda de clase nueva (`machinery`) para T1 — estado: `propuesta` (requiere firma del usuario)

El doc 100 §6.2 listaba "el GT de `machinery` del doc 94 como sonda de clase nueva" dentro de la
checklist de evaluación. Ese ítem NO es aplicable al artefacto T1: el contrato de serving D-FT-08 fija
vocabulario CERRADO y ordenado (person/helmet/vest/"bare head") y prohíbe `set_classes()`; una clase
fuera del vocabulario no puede evaluarse sobre ese checkpoint. Propuesta: derogar la sonda PARA T1 con
esta causa técnica y reasignarla a T2/T3 (vocabulario abierto), donde el riesgo de erosión que la sonda
mide es ejercitable. Mientras esta decisión siga en `propuesta`, la puerta del doc 100 §6 se considera
INCOMPLETA en ese ítem (no se disimula).
```

En `100` §6.2, junto al ítem de la sonda, agregar el marcador: `[2026-08-14: ítem NI cerrado NI derogado — derogación para T1 propuesta como D-FT-13 (doc 117), pendiente de firma]`. En `116` §6 (gates), agregar una línea remitiendo a D-FT-13.

- [ ] **Step 3 — retención OV como limitación de diseño** (hallazgo 3): en `116` (sección de gates o donde se describa la evaluación), agregar:

```markdown
**Limitación de diseño de T1 (declarada):** T1 NO mide retención open-vocabulary generalista.
D-FT-08 prohíbe `set_classes()` sobre el checkpoint y la "retención" de D-FT-12 es in-domain
(person/helmet/vest dentro de bench_v3). El riesgo de erosión OV que motiva ADR-017 §1.3 queda
FUERA del alcance medible de T1: cualquier GO se acota a in-domain. La medición generalista
(COCO val / OVDEval, pre-registrada en contingencia/20 §6) queda para T2/T3.
```

Espejo corto en `117` (contexto de D-FT-12) y en `ajustes/05` (bloque fine-tuning): `Si T1 se reporta en el informe, la retención OV generalista se declara NO MEDIDA por diseño (contrato de vocabulario fijo), nunca como casilla verde.`

- [ ] **Step 4 — smoke≠training** (hallazgo 9): en `116` §8 (evidencia), agregar:

```markdown
### Turnos consumidos vs la puerta (ADR-017 §5.2) — declaración explícita

Los 7 jobs enviados a Mendieta (1166382, 1166456, 1166465, 1166520, 1166552, 1166583, 294502) fueron
SMOKES técnicos en partición `short`, no entrenamiento full: (a) F-100.1 estaba decidida antes del
primero; (b) los ítems abiertos de la checklist (T-FT-031 evaluación, T-FT-032 baseline) son del lado
de la EVALUACIÓN LOCAL, que un smoke no ejercita; (c) 5 de los 7 murieron por infraestructura (Docker
Hub inalcanzable, descarga AMP, SIGILL de Polars) y el 1166552 fue REVOCADO metodológicamente por la
auditoría del freeze. El turno que la puerta protege — el full de 10 épocas — sigue sin pedirse
(NO-GO vigente). El informe debe conservar esta distinción para que no la descubra el tribunal.
```

- [ ] **Step 5**: guard de encuadre: `grep -rniE "falta de tiempo|presupuesto de tiempo" docs/operacion/116* docs/operacion/117* docs/contingencia/20*` → cero apariciones nuevas (la única legítima es la prohibición misma).

### Task 17: Licencias — checkpoint derivado, `mobileclip2_b.ts`, frase YOLOE, seeds, pycocotools

**Files:**
- Modify: `e-ovrt_datasets/datasets/registry/license_registry.md`
- Modify: `docs/operacion/116-plan-maestro-finetuning.md` (§7 contrato), `docs/operacion/117-decisiones-y-tareas-finetuning.md` (fila T-FT-031)
- Modify: `docs/informe/ajustes/gobierno/99-materiales-de-cierre.md` (§6, hallazgo de licencias)

- [ ] **Step 1 — posición sobre el checkpoint derivado** (hallazgo 5): en `license_registry.md`, sección de modelos, agregar:

```markdown
### Checkpoint derivado T1 (si la jornada lo produce) — POSICIÓN PROPUESTA (requiere confirmación del usuario)

El peso base (`yoloe-26s-seg.pt`) y el trainer (`ultralytics` 8.4.86) son AGPL-3.0: en lectura
conservadora, un checkpoint fine-tuneado HEREDA esa obligación. Posición registrada: uso local y
académico; el checkpoint NO se redistribuye, NO se commitea y NO se publica con la tesis; si la
defensa exigiera publicarlo, se publicaría bajo AGPL-3.0. Esta fila existe porque el registro previo
solo cubría los pesos BASE y nunca mencionaba el artefacto nuevo que la jornada va a producir.
```

- [ ] **Step 2 — `mobileclip2_b.ts`**: investigar la licencia real (WebSearch/WebFetch: release de assets de Ultralytics para YOLOE + upstream Apple MobileCLIP2 — el asset lo redistribuye Ultralytics; buscar el LICENSE del release y el del modelo original de Apple). Registrar en `license_registry.md` lo que se encuentre CON URL de fuente; si no es asertable, mantener `NOASSERTION` y agregar: `Riesgo declarado: el asset (253 MB) viajó a Mendieta dentro del bundle r20 el 2026-08-13 como dependencia técnica del text-encoder de YOLOE (uso privado de investigación, sin redistribución). La política "al clúster solo sube material CC BY 4.0" (doc 100 §6.3) se enunció para DATOS; esta fila la extiende a assets de modelo con la anotación del caso. Decisión final del usuario pendiente.`

- [ ] **Step 3 — frase YOLOE future-proof**: en `license_registry.md`, reemplazar `Ningún resultado del núcleo depende de sus pesos` por `Ningún resultado del núcleo ZERO-SHOT vigente depende de sus pesos; si la jornada E-04 produce un GO de T1, esta frase se revisa (el checkpoint T1 sería un resultado que sí depende de ellos).`

- [ ] **Step 4 — seeds y pycocotools**: en `116` §7 (contrato), agregar: `Seeds registrados: split 42 · trainer 100 · inferencia 42 — tres etapas con generadores independientes; se registran para reproducibilidad exacta de cada etapa.` En `117`, fila T-FT-031, agregar: `Dependencia local: pycocotools AUSENTE del venv de media-plane (verificado 2026-08-14) — no bloquea T1, bloquea la Tabla 32 de T2; instalar antes de ejecutar T-FT-031.`

- [ ] **Step 5 — gobierno/99 §6**: actualizar el hallazgo abierto de licencias: `Parcialmente cerrado 2026-08-14: license_registry.md (datasets) ya registra los catálogos de modelos con SPDX y la posición propuesta sobre el checkpoint derivado. Quedan: decisión de archivo LICENSE por repo, y la firma del usuario sobre la posición del checkpoint + mobileclip2.`

### Task 18: `--allow-cpu` restringido a los modos de preflight (hallazgo 6)

**Files:**
- Modify: `e-ovrt_experimental-setup/finetuning/scripts/train_t1.py` (líneas ~394-407)

- [ ] **Step 1**: tras el parseo de args (la zona de las líneas 392-407), agregar el guard:

```python
if args.allow_cpu and not (args.check_only or args.check_freeze):
    parser.error(
        "--allow-cpu solo es valido junto a --check-only/--check-freeze "
        "(D-100.1: el entrenamiento nunca corre fuera del cluster)"
    )
```

- [ ] **Step 2: Verificación por CLI** (no hay suite propia en `finetuning/scripts/`; verificar a mano y dejar el registro en el doc 119):

```bash
cd /home/simonll4/projects/e-ovrt_experimental-setup
CUDA_VISIBLE_DEVICES="" .venv-talert/bin/python finetuning/scripts/train_t1.py --allow-cpu --config finetuning/configs/t1_yoloe26s_lp.yaml ; echo "exit=$?"
# esperado: exit=2 con el mensaje del guard (argparse error), SIN llegar al chequeo CUDA
CUDA_VISIBLE_DEVICES="" .venv-talert/bin/python finetuning/scripts/train_t1.py --allow-cpu --check-only --config finetuning/configs/t1_yoloe26s_lp.yaml ; echo "exit=$?"
# esperado: pasa el guard y ejecuta el preflight (exit=0 si el preflight da bien)
```

(si `train_t1.py` requiere otro intérprete o flags obligatorios extra, leer su `--help` primero y ajustar la invocación, no el guard; si el venv `.venv-talert` no tiene las deps del script, usar el intérprete que el README de `finetuning/` indique.)

- [ ] **Step 3**: reflejar el cierre en `docs/operacion/117-decisiones-y-tareas-finetuning.md` (tabla de tareas, como tarea nueva `T-FT-0xx` con el siguiente número libre, estado `done`): `Restringir --allow-cpu de train_t1.py a --check-only/--check-freeze (guard D-100.1). Cerrada 2026-08-14.`

---

## BLOQUE E — Cierre

### Task 19: Kit — precisión de "los cinco índices" + regeneración

**Files:**
- Modify: `docs/herramientas/generar_project_kit.py`
- Regenerar: `docs/informe/project-kit/` (salida del generador, nunca a mano)

- [ ] **Step 1**: localizar la frase: `grep -n "cinco" docs/herramientas/generar_project_kit.py docs/informe/project-kit/00-contexto-base.md`. Editar EN EL GENERADOR (la fuente de la frase; si viene de un doc fuente embebido, editar ese doc): `los cinco indices de resultados` → `el índice raíz results/index.md (limitaciones L1–L8 y procedencia) más los 4 índices canónicos (bench_imagenes, bench_nivel_a, clip_bench, realtime)`.

- [ ] **Step 2**: correr los tests del generador: `cd /home/simonll4/projects/docs && python3 -m unittest herramientas.tests.test_generar_project_kit` → `Ran 14 tests ... OK` (si la frase editada rompe una fixture, actualizar la fixture — es el cambio esperado).

- [ ] **Step 3**: determinar la etapa vigente (leer `docs/informe/ajustes/gobierno/00-README-gobierno.md` o el encabezado del kit actual) y regenerar: `python3 herramientas/generar_project_kit.py --etapa <N>`; después `python3 herramientas/generar_project_kit.py --etapa <N> --check` → `OK: kit vigente`.

- [ ] **Step 4**: guards sobre el kit regenerado: `grep -c "cinco indices" docs/informe/project-kit/00-contexto-base.md` → 0; `grep -n "T-FT-023" docs/informe/project-kit/*.md | grep -viE "cerrad|639e60df"` → vacío (esto confirma que Task 11 llegó al kit); `grep -c "64,534" docs/informe/project-kit/00-contexto-base.md` → ≥1 (la cifra de distribución entró vía GUIA-REDACTORES).

### Task 20: Constancia — `operacion/119` + CRONOLOGIA 08-14 + índice

**Files:**
- Create: `docs/operacion/119-relevamiento-post-codex-y-cierre-de-brechas.md`
- Modify: `docs/00-indice.md`, `docs/CRONOLOGIA.md`

- [ ] **Step 1**: escribir el doc 119 con esta estructura fija (el contenido variable sale de lo efectivamente ejecutado — citar salidas reales de verificadores y tests, jamás esperadas):

```markdown
# 119 — Relevamiento post-Codex (08-11→08-13) y cierre de brechas (2026-08-14)

## 1. Contexto y método
Cuatro auditorías paralelas sobre los 6 repos (docs, media-plane, control-plane, experimental-setup,
datasets, alert-distribution) tras la jornada con Codex. Veredicto global: el norte se preservó
(ADR-016/017 respetados — serie del proyecto —, cifras canónicas intactas, cero leakage verificado
byte a byte, cero entrenamiento local); la deuda encontrada fue de propagación a medias y de
divergencia doc↔código.

## 2. Hallazgos → acciones (tabla completa)
| # | Hallazgo | Severidad | Acción | Evidencia del cierre |
(una fila por hallazgo de este plan: C-1, C-2, B-1..B-4, D-1, D-2, E-1..E-7, A-1, A-2,
defectos de docs #1..#7, hallazgos FT 1..9, licencias, kit; con archivo:línea y el test/guard que lo cierra)

## 3. Decisiones que quedan en `propuesta` (firma del usuario)
- D-FT-13 (derogación de la sonda machinery para T1) — doc 117.
- Posición de licencia del checkpoint derivado + mobileclip2_b.ts — license_registry (datasets).
- Opcional: ADR propia para el patrón BFF-subprocess (hoy: nota en estado-de-implementacion-adrs).
- (Siguen del tablero, previas a este plan: D-FT-08, D-FT-12.)

## 4. Hallazgos residuales aceptados con causa
(p.ej. la barrera wait_for_subscriber si Task 7 decidió no tocarla; reconexión MQTT acotada a
reset-de-cliente por ADR-005 — serie del proyecto; compose mosquitto declarado sin verificar.)

## 5. Verificación
(salidas REALES: 96-verificar-indices.py con las filas nuevas de realtime; 109; 113 --check;
evidence_runs --check; suites: media-plane / webconsole / control-plane / alert-distribution /
experimental tests — números exactos.)

## 6. Estado git al cierre
(git status --short por repo; NADA commiteado: el usuario decide los commits.)
```

- [ ] **Step 2**: agregar la fila del 119 a la tabla de docs de `00-indice.md`, sumarlo al tramo correspondiente del mapa, y agregar la jornada `2026-08-14` a `CRONOLOGIA.md` (relevamiento + cierre de brechas, con las 2-3 cifras que cambiaron de estado: steady-state publicado, T-85, D-FT-13 propuesta).

### Task 21: Verificación global y entrega

- [ ] **Step 1 — suites completas** (reportar números exactos):

```bash
cd /home/simonll4/projects/e-ovrt_media-plane && .venv/bin/python -m pytest -q
cd /home/simonll4/projects/e-ovrt_experimental-setup/webconsole/backend && .venv/bin/python -m pytest -q
cd /home/simonll4/projects/e-ovrt_control-plane && .venv/bin/python -m pytest tests/ -q --ignore=tests/labs
cd /home/simonll4/projects/e-ovrt_alert-distribution && .venv/bin/python -m pytest -q && .venv/bin/ruff check src tests
cd /home/simonll4/projects/e-ovrt_experimental-setup && .venv-talert/bin/python -m pytest tests/ -q
```

Esperado: todo verde; alert-distribution además `pytest -m integration -q` → `1 skipped` (sin broker).

- [ ] **Step 2 — verificadores de docs/results**:

```bash
cd /home/simonll4/projects/docs
python3 operacion/datos/96-verificar-indices.py            # ✅ con las filas realtime nuevas
python3 operacion/datos/109-verificar-organizacion.py      # ✅
python3 operacion/datos/113-regenerar-provenance-estrato-b.py --check   # ✅
python3 -m unittest herramientas.tests.test_generar_project_kit          # 14 OK
python3 herramientas/generar_project_kit.py --etapa <N> --check          # OK
cd /home/simonll4/projects/e-ovrt_experimental-setup && .venv-talert/bin/python tools/evidence_runs.py --check
```

- [ ] **Step 3 — greps de cierre** (todos deben dar el resultado indicado):

```bash
# T-FT-023 nunca como causa abierta (fuera de historia protegida):
grep -rn "T-FT-023" /home/simonll4/projects/docs --include="*.md" | grep -viE "cerrad|639e60df|done|snapshot|adr-017|operacion/11[67]|operacion/100|CRONOLOGIA|119-"
# → vacío o solo menciones legítimas revisadas a ojo
grep -rniE "falta de tiempo" /home/simonll4/projects/docs/operacion/11[5-9]* # → vacío
grep -rn "informe-project-kit" /home/simonll4/projects/docs --include="*.md" | grep -v "No regenerar"  # sin refs vivas al kit viejo
git -C /home/simonll4/projects/docs status --short | grep "informe/entregable/"  # → vacío (no se tocó)
```

- [ ] **Step 4 — entrega al usuario**: imprimir `git status --short` de los 6 repos (docs, media-plane, control-plane, experimental-setup, datasets, alert-distribution) + el resumen: qué se cerró, qué quedó en `propuesta` esperando su firma (D-FT-13, licencias, ADR opcional), y qué sigue siendo solo suyo (C1 URLs, video V2, D-FT-08/D-FT-12, commits, orden de redacción). **No commitear nada.**

---

## Orden recomendado de ejecución

1. **A** (Tasks 1–7) — los dos graves primero (1, 2); el resto en cualquier orden.
2. **B** (Tasks 8→9→10) — 8 antes que 9 (el verificador cubre lo publicado) y antes que 12 (la GUIA cita el steady-state).
3. **C** (Tasks 11–14) y **D** (Tasks 15–18) — independientes entre sí; dentro de C, la 12 necesita los números de la 8.
4. **E** (19→20→21) — el kit se regenera después de TODAS las ediciones de docs; el 119 y la verificación global cierran.

## Qué NO hace este plan (deliberado)

- No aprueba D-FT-08 ni D-FT-12, no firma D-FT-13 ni la posición de licencias: son del usuario.
- No re-corre ninguna campaña ni job de clúster; no toca `bench_v3`, GT, ni `metrics.json` a mano (el único metrics.json que cambia se REGENERA con su agregador y su bloque primario queda byte-idéntico).
- No toca `informe/entregable/` (§17.x), no crea ADR-018 (queda propuesto), no reescribe los commits "actualizacion1-4" (historia; si el usuario quiere reescribirla, docs no tiene remote y puede hacerlo él).
- No implementa reconexión MQTT "robusta" (backoff/sesiones persistentes): ADR-005 (serie del proyecto) la recorta; solo se arregla el reintento contra cliente muerto.
- No agrega la validación "el `fixed_vocabulary` debe ser el canónico v2" al schema de config de media-plane (hallazgo 7 del relevamiento): ese enforcement es la letra de D-FT-08, que sigue en `propuesta` — implementarlo antes de la firma sería ejecutar una decisión no tomada. Queda registrado en el doc 119 §3 como consecuencia pendiente de D-FT-08 (hoy el binding canónico ya se valida contra checkpoint y plan, no contra config).
