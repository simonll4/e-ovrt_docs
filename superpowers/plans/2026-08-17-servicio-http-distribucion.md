# Servicio HTTP del distribuidor de alertas — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Que `e-ovrt_alert-distribution` exponga un servicio HTTP en `:8082`, espejo del control-plane, para ser una unidad desplegable propia — **sin romper nada de lo ya implementado**.

**Architecture:** Extensión **aditiva**. Se agrega un paquete `service/` que envuelve al `Distributor` existente; el CLI (`replay`/`live`) no se toca. El runner del BFF gana una implementación HTTP del protocolo `RunDistribution` que ya está inyectado, y la implementación por subproceso se conserva como camino alternativo (por eso ADR-018 no se deroga).

**Tech Stack:** Python 3.11 · FastAPI + uvicorn (extra nuevo `[service]`) · pydantic v2 · pyzmq · pytest + `fastapi.testclient.TestClient` · httpx (cliente del BFF, ya presente ahí).

**Spec:** `docs/specs/45-distribucion-alertas.md` §9 · decisión: `docs/decisiones/adr-019-servicio-http-distribucion.md`

## Global Constraints

- **No romper nada implementado.** Requisito del usuario (2026-08-17). Toda suite existente debe seguir verde sin editarla: `tests/test_cli.py`, `test_distributor.py`, `test_zmq_source.py`, `test_sources.py`, `test_ledger.py`, `test_policy.py`, `test_channel_mqtt.py`, `test_contracts.py`.
- **NO hacer commits.** Regla del workspace (`CLAUDE.md`): *"Never create a git commit unless the user explicitly asks for one in that turn"*, y aplica explícitamente a los planes de superpowers. Este plan **reemplaza los pasos de commit por checkpoints de verificación**. Tampoco agregar `Co-Authored-By`.
- **Python del repo:** `requires-python = ">=3.11,<3.12"` (pin propio de `e-ovrt_alert-distribution`, no cambiarlo).
- **ruff:** `line-length = 100`, `target-version = "py311"`.
- **pytest:** `testpaths = ["tests"]`, `addopts = "-m 'not integration'"`, marker `integration: requires external services (MQTT broker)`.
- **Trampa ZeroMQ, no negociable:** nunca cerrar un socket ZeroMQ desde un hilo distinto del que lo creó mientras otro está en `recv_multipart` — libzmq aborta con `SIGABRT`. La parada es cooperativa vía `ZmqSource.request_stop()`, que **ya existe**.
- **Puerto:** `:8082` (serie `:8080` media-plane, `:8081` control-plane). Verificado libre en el workspace.
- **FastAPI no es dependencia base:** va en el extra `[service]`. Sin ese extra, el CLI tiene que seguir funcionando.
- **Contratos siempre aditivos** (regla 2 de `docs/specs/README.md`).

**Rutas base:**
- Distribuidor: `/home/simonll4/projects/e-ovrt_alert-distribution`
- BFF: `/home/simonll4/projects/e-ovrt_experimental-setup/webconsole/backend`
- Molde a espejar: `/home/simonll4/projects/e-ovrt_control-plane/src/eovrt_control/service/`

---

## File Structure

**Crear** (en `e-ovrt_alert-distribution/src/eovrt_distribution/`):

| Archivo | Responsabilidad |
|---|---|
| `service/__init__.py` | vacío |
| `service/settings.py` | `ServiceSettings.from_env()` — `runs_dir` |
| `service/run_ids.py` | validación de `run_id` como segmento de path + generación de ids |
| `service/run_request.py` | `DistributionRunRequest` (pydantic, `extra="forbid"`) |
| `service/run_manager.py` | una corrida activa; hilo, estado, summary, cancelación |
| `service/app.py` | `create_app()` + lifespan |
| `service/routers/__init__.py` | vacío |
| `service/routers/health.py` | `/healthz`, `/readyz` |
| `service/routers/runs.py` | `POST/GET/DELETE /api/runs*`, `POST /api/runs/{id}/cancel` |
| `service/routers/config.py` | `GET /api/config` |

**Tests a crear** (en `e-ovrt_alert-distribution/tests/`): `test_service_request.py`, `test_run_manager.py`, `test_service_api.py`, `test_service_live.py`, `test_cli_serve.py`.

**Modificar:**
- `e-ovrt_alert-distribution/pyproject.toml` — extra `[service]`, `httpx` en `dev`
- `e-ovrt_alert-distribution/src/eovrt_distribution/cli.py` — subcomando `serve`
- BFF `src/eovrt_webconsole/experiment/distribution_http.py` (**crear**) — cliente HTTP
- BFF `src/eovrt_webconsole/settings.py` — `distribution_service_url` + selector
- BFF `src/eovrt_webconsole/experiment/runner.py` — elegir implementación

---

## Task 1: Extra `[service]` y esqueleto que responde `/healthz`

**Files:**
- Modify: `e-ovrt_alert-distribution/pyproject.toml`
- Create: `src/eovrt_distribution/service/__init__.py`, `service/settings.py`, `service/app.py`, `service/routers/__init__.py`, `service/routers/health.py`
- Test: `tests/test_service_api.py`

**Interfaces:**
- Consumes: nada.
- Produces: `ServiceSettings(runs_dir: Path)` con `.from_env(env=None)`; `create_app(settings: ServiceSettings | None = None) -> FastAPI`.

- [ ] **Step 1: Agregar el extra sin tocar las deps base**

En `pyproject.toml`, dentro de `[project.optional-dependencies]`, dejar `mqtt` y `dev` como están y agregar:

```toml
service = ["fastapi>=0.110", "uvicorn[standard]"]
```

y agregar `"httpx"` a la lista `dev` (lo necesita `TestClient`):

```toml
dev = ["pytest>=8", "ruff>=0.4", "httpx"]
```

- [ ] **Step 2: Instalar**

```bash
cd /home/simonll4/projects/e-ovrt_alert-distribution
.venv/bin/pip install -e ".[mqtt,service,dev]"
```

- [ ] **Step 3: Escribir el test que falla**

Crear `tests/test_service_api.py`:

```python
from pathlib import Path

from fastapi.testclient import TestClient

from eovrt_distribution.service.app import create_app
from eovrt_distribution.service.settings import ServiceSettings


def _client(tmp_path: Path) -> TestClient:
    app = create_app(ServiceSettings(runs_dir=tmp_path / "runs"))
    return TestClient(app)


def test_healthz_responde_ok(tmp_path: Path) -> None:
    with _client(tmp_path) as client:
        response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_readyz_responde_ok(tmp_path: Path) -> None:
    with _client(tmp_path) as client:
        response = client.get("/readyz")
    assert response.status_code == 200


def test_lifespan_crea_runs_dir(tmp_path: Path) -> None:
    runs_dir = tmp_path / "runs"
    app = create_app(ServiceSettings(runs_dir=runs_dir))
    with TestClient(app):
        pass
    assert runs_dir.is_dir()
```

- [ ] **Step 4: Correr y verificar que falla**

```bash
.venv/bin/python -m pytest tests/test_service_api.py -v
```
Esperado: FAIL con `ModuleNotFoundError: No module named 'eovrt_distribution.service'`.

- [ ] **Step 5: Implementar `settings.py`**

```python
"""Configuracion operacional del servicio (ADR-009: vive con el servicio)."""

from __future__ import annotations

import os
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ServiceSettings:
    runs_dir: Path

    @classmethod
    def from_env(cls, env: Mapping[str, str] | None = None) -> "ServiceSettings":
        env = os.environ if env is None else env
        return cls(runs_dir=Path(env.get("EOVRT_DISTRIBUTION_RUNS_DIR", "runs")).resolve())
```

- [ ] **Step 6: Implementar `routers/health.py`**

```python
"""Sondas de vida y listo del servicio de distribucion (spec 45 §9.3)."""

from __future__ import annotations

from fastapi import APIRouter

router = APIRouter()


@router.get("/healthz")
def healthz() -> dict[str, str]:
    return {"status": "ok"}


@router.get("/readyz")
def readyz() -> dict[str, str]:
    return {"status": "ready"}
```

- [ ] **Step 7: Implementar `app.py`**

```python
"""Factory de la app FastAPI del servicio de distribucion (ADR-019)."""

from __future__ import annotations

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from eovrt_distribution.service.routers import health
from eovrt_distribution.service.settings import ServiceSettings

logger = logging.getLogger(__name__)


@asynccontextmanager
async def _lifespan(app: FastAPI):
    settings: ServiceSettings = app.state.settings
    settings.runs_dir.mkdir(parents=True, exist_ok=True)
    logger.info("distribucion lista (runs_dir=%s)", settings.runs_dir)
    yield


def create_app(settings: ServiceSettings | None = None) -> FastAPI:
    settings = settings or ServiceSettings.from_env()
    app = FastAPI(title="eovrt-alert-distribution", lifespan=_lifespan)
    app.state.settings = settings
    app.include_router(health.router)
    return app
```

Crear `service/__init__.py` y `service/routers/__init__.py` vacíos.

- [ ] **Step 8: Correr y verificar que pasa**

```bash
.venv/bin/python -m pytest tests/test_service_api.py -v
```
Esperado: 3 passed.

- [ ] **Step 9: CHECKPOINT — no rompimos nada**

```bash
.venv/bin/python -m pytest tests/ -q
.venv/bin/ruff check src tests
```
Esperado: toda la suite previa verde + los 3 nuevos. **Si algo previo falla, parar y reportar** — es el requisito duro del usuario. (No commitear: regla del workspace.)

---

## Task 2: Contrato del request

**Files:**
- Create: `src/eovrt_distribution/service/run_request.py`
- Test: `tests/test_service_request.py`

**Interfaces:**
- Consumes: nada.
- Produces: `DistributionRunRequest` con campos `mode: Literal["replay","live"]`, `out_dir: str`, `config_path: str | None`, `config: dict | None`, `alerts_path: str | None`, `endpoint: str | None`, `control_run_id: str | None`, `backfill: str | None`, `idle_timeout_ms: float | None`.

- [ ] **Step 1: Escribir el test que falla**

Crear `tests/test_service_request.py`:

```python
import pytest
from pydantic import ValidationError

from eovrt_distribution.service.run_request import DistributionRunRequest


def test_replay_valido() -> None:
    req = DistributionRunRequest(
        mode="replay", out_dir="/tmp/out", alerts_path="/tmp/alerts.jsonl", config_path="c.yaml"
    )
    assert req.mode == "replay"


def test_campo_desconocido_es_error() -> None:
    """extra='forbid': un typo no se ignora en silencio."""
    with pytest.raises(ValidationError):
        DistributionRunRequest(
            mode="replay", out_dir="/tmp/o", alerts_path="/a", config_path="c", modo="replay"
        )


def test_config_path_y_config_juntos_es_error() -> None:
    with pytest.raises(ValidationError):
        DistributionRunRequest(
            mode="replay", out_dir="/tmp/o", alerts_path="/a", config_path="c", config={"x": 1}
        )


def test_sin_ninguna_config_es_error() -> None:
    with pytest.raises(ValidationError):
        DistributionRunRequest(mode="replay", out_dir="/tmp/o", alerts_path="/a")


def test_replay_sin_alerts_path_es_error() -> None:
    with pytest.raises(ValidationError):
        DistributionRunRequest(mode="replay", out_dir="/tmp/o", config_path="c")


def test_live_sin_endpoint_es_error() -> None:
    with pytest.raises(ValidationError):
        DistributionRunRequest(mode="live", out_dir="/tmp/o", config_path="c")


def test_idle_timeout_no_positivo_es_error() -> None:
    with pytest.raises(ValidationError):
        DistributionRunRequest(
            mode="live", out_dir="/tmp/o", endpoint="tcp://127.0.0.1:5558",
            config_path="c", idle_timeout_ms=0,
        )
```

- [ ] **Step 2: Correr y verificar que falla**

```bash
.venv/bin/python -m pytest tests/test_service_request.py -v
```
Esperado: FAIL con `ModuleNotFoundError`.

- [ ] **Step 3: Implementar**

```python
"""Contrato del request de corrida de distribucion (spec 45 §9.2, ADR-019)."""

from __future__ import annotations

import math
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, model_validator


class DistributionRunRequest(BaseModel):
    # extra="forbid": un campo desconocido en el body -> 422, no se ignora en silencio.
    model_config = ConfigDict(extra="forbid")

    mode: Literal["replay", "live"]
    out_dir: str
    # ADR-009: la config llega por referencia (path a un YAML) o por payload completo.
    config_path: str | None = None
    config: dict[str, Any] | None = None
    # replay
    alerts_path: str | None = None
    # live
    endpoint: str | None = None
    control_run_id: str | None = None
    backfill: str | None = None
    idle_timeout_ms: float | None = None

    @model_validator(mode="after")
    def exactly_one_config_source(self) -> "DistributionRunRequest":
        if (self.config_path is None) == (self.config is None):
            raise ValueError(
                "Exactamente uno de `config_path` (por referencia) o `config` (por payload)"
            )
        return self

    @model_validator(mode="after")
    def campos_segun_modo(self) -> "DistributionRunRequest":
        if self.mode == "replay" and not self.alerts_path:
            raise ValueError("`alerts_path` es obligatorio en modo replay")
        if self.mode == "live" and not self.endpoint:
            raise ValueError("`endpoint` es obligatorio en modo live")
        return self

    @model_validator(mode="after")
    def idle_timeout_positivo(self) -> "DistributionRunRequest":
        if self.idle_timeout_ms is not None and (
            not math.isfinite(self.idle_timeout_ms) or self.idle_timeout_ms <= 0
        ):
            raise ValueError("`idle_timeout_ms` debe ser un numero finito mayor que cero")
        return self
```

- [ ] **Step 4: Correr y verificar que pasa**

```bash
.venv/bin/python -m pytest tests/test_service_request.py -v
```
Esperado: 7 passed.

- [ ] **Step 5: CHECKPOINT**

```bash
.venv/bin/python -m pytest tests/ -q && .venv/bin/ruff check src tests
```

---

## Task 3: `run_ids` y `RunManager` en modo replay

**Files:**
- Create: `src/eovrt_distribution/service/run_ids.py`, `service/run_manager.py`
- Test: `tests/test_run_manager.py`

**Interfaces:**
- Consumes: `DistributionRunRequest` (Task 2), `ServiceSettings` (Task 1), `DistributionConfig.load`, `Distributor`, `JsonlReplaySource`, `MqttChannel`, `NotificationPolicy` (todos ya existentes en el paquete).
- Produces: `RunManager(settings)` con `start_run(request) -> str`, `get(run_id) -> dict`, `current() -> dict`, `list_runs() -> list[dict]`, `cancel(run_id) -> None`, `join_active(timeout: float) -> None`, `shutdown() -> None`; excepciones `RunBusyError(active_run_id)`, `UnknownRunError`. Estados: `"running" | "succeeded" | "failed" | "cancelled"`.

- [ ] **Step 1: Escribir el test que falla**

Crear `tests/test_run_manager.py`:

```python
import json
from pathlib import Path

import pytest

from eovrt_distribution.service.run_manager import RunBusyError, RunManager, UnknownRunError
from eovrt_distribution.service.run_request import DistributionRunRequest
from eovrt_distribution.service.settings import ServiceSettings

ALERTA = {
    "alert_id": "a1",
    "experiment_id": "exp",
    "pattern_id": "CR-01",
    "severity": "high",
    "source_id": "cam1",
    "ts_ms": 1000,
}


def _alerts_file(tmp_path: Path) -> Path:
    path = tmp_path / "alerts.jsonl"
    path.write_text(json.dumps(ALERTA) + "\n", encoding="utf-8")
    return path


def _request(tmp_path: Path) -> DistributionRunRequest:
    return DistributionRunRequest(
        mode="replay",
        out_dir=str(tmp_path / "out"),
        alerts_path=str(_alerts_file(tmp_path)),
        config={"channel": {"mode": "dry_run"}},
    )


def _manager(tmp_path: Path) -> RunManager:
    return RunManager(ServiceSettings(runs_dir=tmp_path / "runs"))


def test_start_run_devuelve_id_y_termina(tmp_path: Path) -> None:
    manager = _manager(tmp_path)
    run_id = manager.start_run(_request(tmp_path))
    manager.join_active(timeout=10.0)
    info = manager.get(run_id)
    assert info["status"] == "succeeded"
    assert info["summary"] is not None


def test_run_id_es_segmento_de_path_seguro(tmp_path: Path) -> None:
    manager = _manager(tmp_path)
    run_id = manager.start_run(_request(tmp_path))
    manager.join_active(timeout=10.0)
    assert "/" not in run_id and ".." not in run_id


def test_segunda_corrida_con_una_activa_es_busy(tmp_path: Path) -> None:
    manager = _manager(tmp_path)
    manager.start_run(_request(tmp_path))
    try:
        with pytest.raises(RunBusyError):
            manager.start_run(_request(tmp_path))
    finally:
        manager.join_active(timeout=10.0)


def test_get_de_id_desconocido(tmp_path: Path) -> None:
    with pytest.raises(UnknownRunError):
        _manager(tmp_path).get("no-existe")


def test_config_invalida_es_value_error(tmp_path: Path) -> None:
    manager = _manager(tmp_path)
    request = DistributionRunRequest(
        mode="replay",
        out_dir=str(tmp_path / "out"),
        alerts_path=str(tmp_path / "no-esta.jsonl"),
        config={"channel": {"mode": "dry_run"}},
    )
    with pytest.raises(FileNotFoundError):
        manager.start_run(request)
```

- [ ] **Step 2: Correr y verificar que falla**

```bash
.venv/bin/python -m pytest tests/test_run_manager.py -v
```
Esperado: FAIL con `ModuleNotFoundError`.

- [ ] **Step 3: Implementar `run_ids.py`**

```python
"""Validacion del `run_id` como segmento de path, y generacion de ids unicos.

Mismo criterio que el control-plane y el media-plane: alfanumericos, `_` y `-`.
Descarta `..`, `/` y demas ANTES de construir cualquier ruta bajo `runs_dir`.
"""

from __future__ import annotations

import re
from datetime import UTC, datetime
from uuid import uuid4

from fastapi import HTTPException

RUN_ID_RE = re.compile(r"^[A-Za-z0-9_-]+$")


def is_valid_run_id(run_id: str) -> bool:
    return bool(RUN_ID_RE.match(run_id))


def require_valid_run_id(run_id: str) -> None:
    """Levanta 404 ("run desconocido") si el id no es un segmento seguro."""
    if not is_valid_run_id(run_id):
        raise HTTPException(status_code=404, detail=f"Run desconocido: {run_id}")


def new_distribution_run_id() -> str:
    """Postcondicion: el id devuelto siempre pasa `is_valid_run_id`."""
    stamp = datetime.now(tz=UTC).strftime("%Y%m%dT%H%M%SZ")
    return f"dist_{stamp}_{uuid4().hex[:6]}"
```

- [ ] **Step 4: Implementar `run_manager.py`**

```python
"""Gestor de corridas del servicio de distribucion (spec 45 §9.4).

Una corrida activa por vez. La corrida vive en un hilo propio; la fuente ZeroMQ
se detiene de forma COOPERATIVA (`request_stop()`), nunca cerrando su socket
desde otro hilo: eso aborta el proceso con SIGABRT.
"""

from __future__ import annotations

import threading
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from eovrt_distribution.channels.mqtt import MqttChannel
from eovrt_distribution.config import DistributionConfig
from eovrt_distribution.distributor import Distributor
from eovrt_distribution.policy import NotificationPolicy
from eovrt_distribution.service.run_ids import new_distribution_run_id
from eovrt_distribution.service.run_request import DistributionRunRequest
from eovrt_distribution.service.settings import ServiceSettings
from eovrt_distribution.sources import JsonlReplaySource


class RunBusyError(RuntimeError):
    def __init__(self, active_run_id: str) -> None:
        super().__init__(f"Ya hay una corrida activa: {active_run_id}")
        self.active_run_id = active_run_id


class UnknownRunError(KeyError):
    pass


@dataclass
class _RunState:
    run_id: str
    status: str = "running"
    summary: dict[str, Any] | None = None
    error: str | None = None
    out_dir: str = ""
    source: Any = None
    thread: threading.Thread | None = field(default=None, repr=False)


class RunManager:
    def __init__(self, settings: ServiceSettings) -> None:
        self._settings = settings
        self._lock = threading.Lock()
        self._runs: dict[str, _RunState] = {}
        self._active: _RunState | None = None

    def start_run(self, request: DistributionRunRequest) -> str:
        with self._lock:
            if self._active is not None and self._active.status == "running":
                raise RunBusyError(self._active.run_id)

        cfg = self._load_config(request)
        source = self._build_source(request)  # valida rutas: puede levantar FileNotFoundError
        run_id = new_distribution_run_id()
        state = _RunState(run_id=run_id, out_dir=request.out_dir, source=source)

        distributor = Distributor(
            source=source,
            channel=MqttChannel(
                mode=cfg.channel.mode,  # type: ignore[arg-type]
                host=cfg.channel.host,
                port=cfg.channel.port,
                topic_prefix=cfg.channel.topic_prefix,
                qos=cfg.channel.qos,
            ),
            policy=NotificationPolicy(
                cooldown_ms=cfg.notification_policy.cooldown_ms,
                key_fields=tuple(cfg.notification_policy.key),
            ),
            out_dir=Path(request.out_dir),
            max_attempts=cfg.retry.max_attempts,
            retry_wait_ms=cfg.retry.wait_ms,
        )

        def _target() -> None:
            try:
                summary = distributor.run()
            except Exception as exc:  # el hilo no puede propagar: se registra en el estado
                state.status = "failed"
                state.error = f"{type(exc).__name__}: {exc}"
                return
            state.summary = summary
            reason = (summary.get("termination_reason") if isinstance(summary, dict) else None)
            state.status = "cancelled" if reason == "requested_stop" else "succeeded"

        thread = threading.Thread(target=_target, name=f"dist-{run_id}", daemon=True)
        state.thread = thread
        with self._lock:
            self._runs[run_id] = state
            self._active = state
        thread.start()
        return run_id

    def get(self, run_id: str) -> dict[str, Any]:
        state = self._runs.get(run_id)
        if state is None:
            raise UnknownRunError(run_id)
        return {
            "distribution_run_id": state.run_id,
            "status": state.status,
            "out_dir": state.out_dir,
            "summary": state.summary,
            "error": state.error,
        }

    def current(self) -> dict[str, Any]:
        active = self._active
        if active is None:
            raise UnknownRunError("no hay run activo")
        return self.get(active.run_id)

    def list_runs(self) -> list[dict[str, Any]]:
        return [self.get(run_id) for run_id in self._runs]

    def cancel(self, run_id: str) -> None:
        state = self._runs.get(run_id)
        if state is None:
            raise UnknownRunError(run_id)
        request_stop = getattr(state.source, "request_stop", None)
        if request_stop is not None:
            request_stop()

    def join_active(self, timeout: float) -> None:
        active = self._active
        if active is not None and active.thread is not None:
            active.thread.join(timeout=timeout)

    def shutdown(self) -> None:
        for state in self._runs.values():
            if state.status == "running":
                request_stop = getattr(state.source, "request_stop", None)
                if request_stop is not None:
                    request_stop()

    def _load_config(self, request: DistributionRunRequest) -> DistributionConfig:
        if request.config_path is not None:
            return DistributionConfig.load(Path(request.config_path))
        return DistributionConfig.model_validate(request.config)

    def _build_source(self, request: DistributionRunRequest) -> Any:
        if request.mode == "replay":
            alerts_path = Path(request.alerts_path or "")
            if not alerts_path.is_file():
                raise FileNotFoundError(f"no existe: {alerts_path}")
            return JsonlReplaySource(alerts_path)

        from eovrt_distribution.transport.zmq_source import ZmqSource

        backfill_path = Path(request.backfill) if request.backfill else None
        if backfill_path is not None and not backfill_path.is_file():
            raise FileNotFoundError(f"no existe: {backfill_path}")
        return ZmqSource(
            endpoint=request.endpoint or "",
            backfill_path=backfill_path,
            idle_timeout_ms=request.idle_timeout_ms,
            control_run_id=request.control_run_id,
        )
```

> **Nota para quien implementa:** `DistributionConfig.load` y `.model_validate` — verificar la API real en `src/eovrt_distribution/config.py` antes de escribir; si `DistributionConfig` no es un modelo pydantic, cargar el payload por el mismo camino que usa el CLI (`DistributionConfig.load`) escribiendo el dict a un YAML temporal. **No inventar la API.**

- [ ] **Step 5: Correr y verificar que pasa**

```bash
.venv/bin/python -m pytest tests/test_run_manager.py -v
```
Esperado: 5 passed.

- [ ] **Step 6: CHECKPOINT**

```bash
.venv/bin/python -m pytest tests/ -q && .venv/bin/ruff check src tests
```

---

## Task 4: Router de corridas y camino replay completo por HTTP

**Files:**
- Create: `src/eovrt_distribution/service/routers/runs.py`, `service/routers/config.py`
- Modify: `src/eovrt_distribution/service/app.py`
- Test: `tests/test_service_api.py` (agregar)

**Interfaces:**
- Consumes: `RunManager` (Task 3), `DistributionRunRequest` (Task 2).
- Produces: endpoints `POST /api/runs` (201 `{"distribution_run_id": str}`), `GET /api/runs`, `GET /api/runs/current`, `GET /api/runs/{id}`, `DELETE /api/runs/{id}` (204), `POST /api/runs/{id}/cancel` (202), `GET /api/config`.

- [ ] **Step 1: Escribir el test que falla**

Agregar a `tests/test_service_api.py`:

```python
import json


def _replay_body(tmp_path):
    alerts = tmp_path / "alerts.jsonl"
    alerts.write_text(
        json.dumps(
            {
                "alert_id": "a1",
                "experiment_id": "exp",
                "pattern_id": "CR-01",
                "severity": "high",
                "source_id": "cam1",
                "ts_ms": 1000,
            }
        )
        + "\n",
        encoding="utf-8",
    )
    return {
        "mode": "replay",
        "out_dir": str(tmp_path / "out"),
        "alerts_path": str(alerts),
        "config": {"channel": {"mode": "dry_run"}},
    }


def test_post_runs_devuelve_201_y_llega_a_terminal(tmp_path):
    with _client(tmp_path) as client:
        created = client.post("/api/runs", json=_replay_body(tmp_path))
        assert created.status_code == 201
        run_id = created.json()["distribution_run_id"]
        client.app.state.manager.join_active(timeout=10.0)
        info = client.get(f"/api/runs/{run_id}")
    assert info.status_code == 200
    assert info.json()["status"] == "succeeded"
    assert info.json()["summary"] is not None


def test_campo_desconocido_da_422(tmp_path):
    body = _replay_body(tmp_path) | {"modo": "replay"}
    with _client(tmp_path) as client:
        response = client.post("/api/runs", json=body)
    assert response.status_code == 422


def test_run_desconocido_da_404(tmp_path):
    with _client(tmp_path) as client:
        response = client.get("/api/runs/no-existe")
    assert response.status_code == 404


def test_run_id_con_traversal_da_404(tmp_path):
    with _client(tmp_path) as client:
        response = client.get("/api/runs/..%2F..%2Fetc")
    assert response.status_code == 404


def test_current_sin_corrida_da_404(tmp_path):
    with _client(tmp_path) as client:
        response = client.get("/api/runs/current")
    assert response.status_code == 404
```

- [ ] **Step 2: Correr y verificar que falla**

```bash
.venv/bin/python -m pytest tests/test_service_api.py -v
```
Esperado: los 5 nuevos fallan con 404 (no existe el router).

- [ ] **Step 3: Implementar `routers/runs.py`**

```python
"""API de corridas del servicio de distribucion (spec 45 §9.3)."""

from __future__ import annotations

import shutil

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse, Response

from eovrt_distribution.service.run_ids import require_valid_run_id
from eovrt_distribution.service.run_manager import RunBusyError, RunManager, UnknownRunError
from eovrt_distribution.service.run_request import DistributionRunRequest

router = APIRouter(prefix="/api")


def _manager(request: Request) -> RunManager:
    return request.app.state.manager


@router.post("/runs", status_code=201)
def create_run(body: DistributionRunRequest, request: Request):
    try:
        run_id = _manager(request).start_run(body)
    except RunBusyError as exc:
        return JSONResponse(
            status_code=409,
            content={"detail": str(exc), "active_run_id": exc.active_run_id},
        )
    except (ValueError, FileNotFoundError) as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    return {"distribution_run_id": run_id}


@router.get("/runs")
def list_runs(request: Request):
    return _manager(request).list_runs()


# ANTES de /runs/{run_id}: si no, `current` se matchea como un run_id.
@router.get("/runs/current")
def get_current_run(request: Request):
    try:
        return _manager(request).current()
    except UnknownRunError as exc:
        raise HTTPException(status_code=404, detail="No hay run activo") from exc


@router.get("/runs/{run_id}")
def get_run(run_id: str, request: Request):
    require_valid_run_id(run_id)
    try:
        return _manager(request).get(run_id)
    except UnknownRunError as exc:
        raise HTTPException(status_code=404, detail=f"Run desconocido: {run_id}") from exc


@router.post("/runs/{run_id}/cancel", status_code=202)
def cancel_run(run_id: str, request: Request):
    """Parada COOPERATIVA (`request_stop`). Desvio deliberado del espejo: el
    control-plane no expone cancelacion y su corrida live no se puede cancelar."""
    require_valid_run_id(run_id)
    try:
        _manager(request).cancel(run_id)
    except UnknownRunError as exc:
        raise HTTPException(status_code=404, detail=f"Run desconocido: {run_id}") from exc
    return {"status": "cancelling", "distribution_run_id": run_id}


@router.delete("/runs/{run_id}", status_code=204)
def delete_run(run_id: str, request: Request):
    require_valid_run_id(run_id)
    manager = _manager(request)
    try:
        info = manager.get(run_id)
    except UnknownRunError as exc:
        raise HTTPException(status_code=404, detail=f"Run desconocido: {run_id}") from exc
    if info["status"] == "running":
        raise HTTPException(status_code=409, detail="No se puede borrar un run activo")
    shutil.rmtree(request.app.state.settings.runs_dir / run_id, ignore_errors=True)
    return Response(status_code=204)
```

- [ ] **Step 4: Implementar `routers/config.py`**

```python
"""Config efectiva del servicio de distribucion."""

from __future__ import annotations

from fastapi import APIRouter, Request

router = APIRouter(prefix="/api")


@router.get("/config")
def effective_config(request: Request) -> dict[str, str]:
    return {"runs_dir": str(request.app.state.settings.runs_dir)}
```

- [ ] **Step 5: Conectar en `app.py`**

En `_lifespan`, después de crear `runs_dir`, agregar:

```python
    app.state.manager = RunManager(settings)
```

y al final del lifespan (después del `yield`):

```python
    app.state.manager.shutdown()
    app.state.manager.join_active(timeout=10.0)
```

En `create_app`, agregar los routers:

```python
    app.include_router(runs.router)
    app.include_router(config_router.router)
```

con los imports:

```python
from eovrt_distribution.service.routers import config as config_router
from eovrt_distribution.service.routers import health, runs
from eovrt_distribution.service.run_manager import RunManager
```

- [ ] **Step 6: Correr y verificar que pasa**

```bash
.venv/bin/python -m pytest tests/test_service_api.py -v
```
Esperado: 8 passed.

- [ ] **Step 7: CHECKPOINT**

```bash
.venv/bin/python -m pytest tests/ -q && .venv/bin/ruff check src tests
```

---

## Task 5: Modo live y cancelación cooperativa

**Files:**
- Test: `tests/test_service_live.py`

**Interfaces:**
- Consumes: todo lo anterior + `ZmqSource`.
- Produces: nada nuevo; verifica el camino live.

- [ ] **Step 1: Escribir el test que falla**

Crear `tests/test_service_live.py`. Usa un PUB real efímero (mismo patrón que `tests/test_zmq_source.py` — **leerlo primero y reusar sus helpers/fixtures**):

```python
import time

from fastapi.testclient import TestClient

from eovrt_distribution.service.app import create_app
from eovrt_distribution.service.settings import ServiceSettings


def _live_body(tmp_path, endpoint):
    return {
        "mode": "live",
        "out_dir": str(tmp_path / "out"),
        "endpoint": endpoint,
        "idle_timeout_ms": 500.0,
        "config": {"channel": {"mode": "dry_run"}},
    }


def test_live_termina_por_idle_timeout(tmp_path):
    app = create_app(ServiceSettings(runs_dir=tmp_path / "runs"))
    with TestClient(app) as client:
        created = client.post("/api/runs", json=_live_body(tmp_path, "tcp://127.0.0.1:55999"))
        assert created.status_code == 201
        run_id = created.json()["distribution_run_id"]
        app.state.manager.join_active(timeout=15.0)
        info = client.get(f"/api/runs/{run_id}").json()
    assert info["status"] in {"succeeded", "cancelled"}


def test_cancel_detiene_sin_sigabrt(tmp_path):
    """Si el socket se cerrara desde otro hilo, el proceso moriria con SIGABRT
    y el test no llegaria a la asercion final."""
    app = create_app(ServiceSettings(runs_dir=tmp_path / "runs"))
    with TestClient(app) as client:
        created = client.post("/api/runs", json=_live_body(tmp_path, "tcp://127.0.0.1:55998"))
        run_id = created.json()["distribution_run_id"]
        time.sleep(0.2)
        cancelled = client.post(f"/api/runs/{run_id}/cancel")
        assert cancelled.status_code == 202
        app.state.manager.join_active(timeout=15.0)
        info = client.get(f"/api/runs/{run_id}").json()
    assert info["status"] in {"cancelled", "succeeded"}


def test_segunda_corrida_con_live_activa_da_409(tmp_path):
    app = create_app(ServiceSettings(runs_dir=tmp_path / "runs"))
    with TestClient(app) as client:
        client.post("/api/runs", json=_live_body(tmp_path, "tcp://127.0.0.1:55997"))
        segunda = client.post("/api/runs", json=_live_body(tmp_path, "tcp://127.0.0.1:55997"))
        assert segunda.status_code == 409
        assert "active_run_id" in segunda.json()
        app.state.manager.join_active(timeout=15.0)


def test_apagado_con_live_activa_no_cuelga(tmp_path):
    app = create_app(ServiceSettings(runs_dir=tmp_path / "runs"))
    with TestClient(app) as client:
        client.post("/api/runs", json=_live_body(tmp_path, "tcp://127.0.0.1:55996"))
        time.sleep(0.2)
    # salir del context manager dispara el lifespan de apagado; si colgara o
    # abortara, el test no terminaria.
    assert True
```

- [ ] **Step 2: Correr y verificar**

```bash
.venv/bin/python -m pytest tests/test_service_live.py -v
```
Si falla por la API real de `ZmqSource`, ajustar el test al patrón de `tests/test_zmq_source.py` — **no cambiar la semántica de la parada cooperativa**.

- [ ] **Step 3: CHECKPOINT**

```bash
.venv/bin/python -m pytest tests/ -q && .venv/bin/ruff check src tests
```
Esperado: todo verde, **sin `SIGABRT`** y sin cuelgues.

---

## Task 6: Subcomando `serve` en el CLI

**Files:**
- Modify: `src/eovrt_distribution/cli.py`
- Test: `tests/test_cli_serve.py`

**Interfaces:**
- Consumes: `create_app` (Task 1).
- Produces: `eovrt-distribute serve [--host H] [--port 8082]`.

- [ ] **Step 1: Escribir el test que falla**

Crear `tests/test_cli_serve.py`:

```python
from unittest.mock import patch

from eovrt_distribution.cli import main


def test_serve_usa_8082_por_defecto() -> None:
    with patch("uvicorn.run") as run:
        assert main(["serve"]) == 0
    assert run.call_args.kwargs["port"] == 8082
    assert run.call_args.kwargs["host"] == "127.0.0.1"


def test_serve_acepta_puerto_explicito() -> None:
    with patch("uvicorn.run") as run:
        assert main(["serve", "--port", "9100"]) == 0
    assert run.call_args.kwargs["port"] == 9100


def test_replay_sigue_funcionando(tmp_path) -> None:
    """Guard de no-regresion: agregar `serve` no puede romper el CLI existente."""
    alerts = tmp_path / "a.jsonl"
    alerts.write_text("", encoding="utf-8")
    assert main(["replay", "--alerts", str(alerts), "--out-dir", str(tmp_path / "o")]) == 0
```

- [ ] **Step 2: Correr y verificar que falla**

```bash
.venv/bin/python -m pytest tests/test_cli_serve.py -v
```
Esperado: FAIL — `serve` no es un subcomando válido.

- [ ] **Step 3: Implementar**

En `cli.py`, después del parser `p_live` y antes de `args = parser.parse_args(argv)`:

```python
    p_serve = sub.add_parser("serve", help="servicio HTTP (ADR-019)")
    p_serve.add_argument("--host", default="127.0.0.1")
    p_serve.add_argument("--port", type=int, default=8082)
```

Y justo después de `args = parser.parse_args(argv)`, **antes** de `cfg = DistributionConfig.load(...)` (serve no necesita config de corrida):

```python
    if args.command == "serve":
        import uvicorn

        from eovrt_distribution.service.app import create_app

        uvicorn.run(create_app(), host=args.host, port=args.port)
        return 0
```

- [ ] **Step 4: Correr y verificar que pasa**

```bash
.venv/bin/python -m pytest tests/test_cli_serve.py -v
```
Esperado: 3 passed.

- [ ] **Step 5: CHECKPOINT — la suite del CLI original intacta**

```bash
.venv/bin/python -m pytest tests/ -q && .venv/bin/ruff check src tests
```
Esperado: `tests/test_cli.py` verde **sin haberlo editado**. Es la prueba de que el cambio es aditivo.

---

## Task 7: El BFF habla por HTTP (conservando el subproceso)

**Files:**
- Create: `webconsole/backend/src/eovrt_webconsole/experiment/distribution_http.py`
- Modify: `webconsole/backend/src/eovrt_webconsole/settings.py`, `experiment/runner.py`
- Test: `webconsole/backend/tests/test_distribution_http.py`

**Interfaces:**
- Consumes: el servicio de Tasks 1-6.
- Produces: `run_distribution_http(*, mode, alerts_path, out_dir, config_path, endpoint, control_run_id, backfill_path, idle_timeout_ms, timeout_s, base_url) -> dict` — misma firma por keyword que `RunDistribution` (`Callable[..., Any]`), devuelve el mismo summary dict.

- [ ] **Step 1: Escribir el test que falla**

Crear `webconsole/backend/tests/test_distribution_http.py`:

```python
import pytest

from eovrt_webconsole.experiment.distribution_http import run_distribution_http

# El backend usa `asyncio_mode = "auto"` (pyproject): los tests async NO llevan
# marcador. `os` y `functools` ya estan importados en runner.py (lineas 20 y 16).


class _FakeResponse:
    def __init__(self, status_code: int, payload: dict) -> None:
        self.status_code = status_code
        self._payload = payload

    def json(self) -> dict:
        return self._payload

    def raise_for_status(self) -> None:
        if self.status_code >= 400:
            raise AssertionError(f"HTTP {self.status_code}")


class _FakeClient:
    """Devuelve 201 al POST y un run terminal al primer GET."""

    def __init__(self, *args, **kwargs) -> None:
        self.posted: dict | None = None

    async def __aenter__(self):
        return self

    async def __aexit__(self, *exc) -> None:
        return None

    async def post(self, url, json=None):
        self.posted = json
        return _FakeResponse(201, {"distribution_run_id": "dist_x"})

    async def get(self, url):
        return _FakeResponse(
            200,
            {
                "distribution_run_id": "dist_x",
                "status": "succeeded",
                "summary": {"delivered": 1},
                "error": None,
            },
        )


async def test_devuelve_el_summary_del_servicio(monkeypatch, tmp_path):
    monkeypatch.setattr("eovrt_webconsole.experiment.distribution_http.httpx.AsyncClient", _FakeClient)
    summary = await run_distribution_http(
        mode="replay",
        alerts_path=tmp_path / "a.jsonl",
        out_dir=tmp_path / "out",
        config_path=None,
        endpoint=None,
        control_run_id=None,
        backfill_path=None,
        idle_timeout_ms=None,
        timeout_s=30.0,
        base_url="http://localhost:8082",
    )
    assert summary == {"delivered": 1}


async def test_modo_invalido_es_error(tmp_path):
    with pytest.raises(ValueError):
        await run_distribution_http(
            mode="nope", alerts_path=None, out_dir=tmp_path, config_path=None,
            endpoint=None, control_run_id=None, backfill_path=None,
            idle_timeout_ms=None, timeout_s=1.0, base_url="http://x",
        )
```

- [ ] **Step 2: Correr y verificar que falla**

```bash
cd /home/simonll4/projects/e-ovrt_experimental-setup/webconsole/backend
../../.venv/bin/python -m pytest tests/test_distribution_http.py -v
```
Esperado: FAIL con `ModuleNotFoundError`.

- [ ] **Step 3: Implementar el cliente**

```python
"""Cliente HTTP del servicio de distribucion (ADR-019).

Implementacion alternativa del protocolo `RunDistribution` del runner. La
implementacion por subproceso (`run_distribution`, spec 44 §B4) se CONSERVA:
ADR-018 sigue vigente y este camino se suma, no la reemplaza.
"""

from __future__ import annotations

import asyncio
from pathlib import Path
from typing import Any

import httpx

_TERMINALES = {"succeeded", "failed", "cancelled"}


async def run_distribution_http(
    *,
    mode: str,
    alerts_path: Path | None,
    out_dir: Path,
    config_path: str | None,
    endpoint: str | None,
    control_run_id: str | None,
    backfill_path: Path | None,
    idle_timeout_ms: float | None,
    timeout_s: float,
    base_url: str,
    poll_interval_s: float = 0.5,
) -> dict[str, Any]:
    if mode not in {"replay", "live"}:
        raise ValueError(f"modo de distribucion invalido: {mode}")
    if mode == "replay" and not alerts_path:
        raise ValueError("distribucion en replay sin alerts_path")
    if mode == "live" and not endpoint:
        raise ValueError("distribucion en live sin endpoint")

    body: dict[str, Any] = {"mode": mode, "out_dir": str(out_dir)}
    if mode == "replay":
        body["alerts_path"] = str(alerts_path)
    else:
        body["endpoint"] = endpoint
        if control_run_id:
            body["control_run_id"] = control_run_id
        if backfill_path is not None:
            body["backfill"] = str(backfill_path)
        if idle_timeout_ms is not None:
            body["idle_timeout_ms"] = idle_timeout_ms
    if config_path:
        body["config_path"] = config_path

    async with httpx.AsyncClient(base_url=base_url, timeout=timeout_s) as client:
        created = await client.post("/api/runs", json=body)
        created.raise_for_status()
        run_id = created.json()["distribution_run_id"]

        async def _poll() -> dict[str, Any]:
            while True:
                response = await client.get(f"/api/runs/{run_id}")
                response.raise_for_status()
                info = response.json()
                if info["status"] in _TERMINALES:
                    return info
                await asyncio.sleep(poll_interval_s)

        info = await asyncio.wait_for(_poll(), timeout=timeout_s)

    if info["status"] != "succeeded":
        raise RuntimeError(
            f"distribucion {info['status']}: {info.get('error') or 'sin detalle'}"
        )
    return info["summary"]
```

- [ ] **Step 4: Correr y verificar que pasa**

```bash
../../.venv/bin/python -m pytest tests/test_distribution_http.py -v
```
Esperado: 2 passed.

- [ ] **Step 5: Agregar la URL a settings**

En `src/eovrt_webconsole/settings.py`, junto a `control_service_url` (línea ~44), agregar el campo:

```python
    distribution_service_url: str = "http://localhost:8082"
```

y en el `from_env` (junto a la línea ~135 de `EOVRT_CONSOLE_CONTROL_SERVICE_URL`):

```python
            distribution_service_url=env.get(
                "EOVRT_CONSOLE_DISTRIBUTION_SERVICE_URL", "http://localhost:8082"
            ).rstrip("/"),
```

- [ ] **Step 6: Elegir implementación en el runner**

En `experiment/runner.py`, donde hoy dice (línea ~689):

```python
    distribution_caller: RunDistribution = run_distribution or _default_run_distribution
```

dejarlo **igual** y agregar arriba la selección por entorno, de modo que el default siga siendo el subproceso salvo que se pida HTTP explícitamente:

```python
    if run_distribution is None and os.environ.get("EOVRT_CONSOLE_DISTRIBUTION_TRANSPORT") == "http":
        from eovrt_webconsole.experiment.distribution_http import run_distribution_http
        from eovrt_webconsole.settings import Settings

        run_distribution = functools.partial(
            run_distribution_http, base_url=Settings.from_env().distribution_service_url
        )
```

> **Por qué el default sigue siendo subproceso:** el requisito del usuario es no romper nada. Con el default intacto, toda la suite existente (`test_runner_distribution.py`, `test_distribution_infra.py`, `test_distribution_preflight_unit.py`) sigue ejercitando el mismo camino sin editarse. HTTP se activa con `EOVRT_CONSOLE_DISTRIBUTION_TRANSPORT=http`.

- [ ] **Step 7: CHECKPOINT — la suite del BFF entera**

```bash
cd /home/simonll4/projects/e-ovrt_experimental-setup/webconsole/backend
../../.venv/bin/python -m pytest -q
```
Esperado: **643 passed** (la línea base del `CLAUDE.md`) + los 2 nuevos. Si baja de 643, **parar**: se rompió algo.

---

## Task 8: Verificación DBE y EBE contra el sistema real

**Files:** ninguno (verificación).

**Interfaces:** consume todo lo anterior.

> **Esta tarea NO se ejecuta sola.** Requiere que el usuario levante servicios y, para EBE, hardware. Pedir antes de correr.

- [ ] **Step 1: Levantar el servicio y comprobar que está vivo**

```bash
cd /home/simonll4/projects/e-ovrt_alert-distribution
.venv/bin/eovrt-distribute serve --port 8082 &
curl -sf http://localhost:8082/healthz
```
Esperado: `{"status":"ok"}`.

- [ ] **Step 2: DBE — misma corrida por los dos caminos, mismo resultado**

Elegir una corrida existente con `alerts.jsonl` real. Correr primero por CLI (camino histórico) y después por HTTP, a `out_dir` distintos, y comparar:

```bash
.venv/bin/eovrt-distribute replay --alerts <alerts.jsonl> --out-dir /tmp/dbe-cli
curl -sf -X POST http://localhost:8082/api/runs -H 'content-type: application/json' \
  -d '{"mode":"replay","out_dir":"/tmp/dbe-http","alerts_path":"<alerts.jsonl>","config_path":"configs/default.yaml"}'
# esperar terminal y comparar
diff <(jq -S 'del(.started_at,.finished_at)' /tmp/dbe-cli/distribution_summary.json) \
     <(jq -S 'del(.started_at,.finished_at)' /tmp/dbe-http/distribution_summary.json)
```
Esperado: **sin diferencias** salvo marcas de tiempo. Es la prueba de que el servicio no cambió la semántica.

- [ ] **Step 3: 🛑 GATE — PEDIR LA OAK-D ANTES DE EBE**

**PARAR ACÁ. Pedirle al usuario que conecte la OAK-D y esperar su confirmación explícita antes de seguir.** Instrucción suya (2026-08-17). Sin la cámara, EBE falla por falta de fuente y el error parece un bug del código nuevo — se pierde el tiempo depurando una causa inexistente.

Al pedirlo, recordar de `docs` las trampas ya conocidas: la OAK PoE trae IP estática de fábrica `169.254.1.222`; no mezclar depthai v3 con v2; en WSL el ping puede mentir si la red no está en modo `mirrored`.

- [ ] **Step 4: EBE — cadena viva completa**

Con la cámara confirmada, y **respetando el orden de suscripción** (el consumidor se suscribe ANTES de que se dispare el run, porque PUB/SUB pierde lo publicado antes de la suscripción):

1. `POST :8082/api/runs` con `mode: live` y el endpoint del bus de alertas → 201.
2. `POST :8081/api/runs` (control-plane) con `mode: live`.
3. `POST :8080/api/runs` (media-plane) con `bus.enabled: true` y fuente `oak_d`.

Verificar: `GET :8082/api/runs/current` pasa a terminal al cerrar la corrida; `notifications.jsonl` no vacío; `distribution_summary.json` con `t_alert-notification`; sin huecos de `seq` (se cuentan como `bus_dropped_events`, nunca se silencian).

- [ ] **Step 5: Cancelación en vivo**

Con una corrida live activa, `POST :8082/api/runs/<id>/cancel` → 202; la corrida termina con `termination_reason = "requested_stop"`, **el proceso NO muere con `SIGABRT`** y no queda hilo huérfano.

- [ ] **Step 6: CHECKPOINT final**

```bash
cd /home/simonll4/projects/e-ovrt_alert-distribution && .venv/bin/python -m pytest tests/ -q
cd /home/simonll4/projects/e-ovrt_experimental-setup/webconsole/backend && ../../.venv/bin/python -m pytest -q
```
Esperado: ambas verdes. Reportar resultados **con la salida real**; si algo falla, decirlo con el output, no resumirlo como éxito.

---

## Propagación documental (después de que todo esté verde)

No es código, pero cierra el trabajo y evita la deuda de propagación que ya mordió antes:

- [ ] `docs/decisiones/estado-de-implementacion-adrs.md` — agregar la fila de ADR-019.
- [ ] `docs/informe/ajustes/material-etapa-3/93-redlines-etapa3.md` — R-17 (tabla rol→contenedor): **fila nueva**, sin reescribir la tabla.
- [x] `docs/herramientas/generar_project_kit.py` — ~~el bloque "TRES patrones de acople" del `BASE_PREAMBLE` pasa a **CUATRO**~~ ✎ 2026-08-18: **este ítem estaba MAL en el plan** — la decisión final (ADR-019, con su propia enmienda) es que siguen siendo **TRES** patrones: el distribuidor entró al primero. El bloque se enmendó en ese sentido y el guard del test exige literalmente `"TRES patrones — no cuatro"`. No seguir este ítem tal como estaba escrito.
- [ ] Regenerar el kit: `python3 herramientas/generar_project_kit.py --etapa all` + `--check`.
- [ ] `docs/operacion/` — constancia de la jornada con los resultados de DBE y EBE.

**Nada de esto se commitea** salvo que el usuario lo pida explícitamente en ese turno.
