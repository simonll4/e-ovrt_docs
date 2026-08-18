# 124 — El distribuidor de alertas pasa a ser servicio HTTP (2026-08-17/18)

- **Decisión:** [ADR-019](../decisiones/adr-019-servicio-http-distribucion.md) · **Diseño:**
  [spec 45 §9](../specs/45-distribucion-alertas.md) · **Plan:**
  `superpowers/plans/2026-08-17-servicio-http-distribucion.md`
- **Estado: cerrado y verificado**, incluida una corrida **en vivo con la OAK-D real**.
- **Alcance diferido con causa:** containerización (Dockerfile, `docker-compose.yml`, y el
  control-plane que tampoco corre en contenedor). **El despliegue no es un resultado del
  informe**: es evidencia de lo implementado y de portabilidad, y se reporta con su estado
  a la entrega (ADR-019 §4).
  ✎ **2026-08-18 (precisión del usuario):** "no es un resultado" **no es "no se menciona"**.
  Se **va a hacer** después de cerrar la redacción, su razón de ser es la **reproducibilidad**
  de la plataforma, su **documentación operativa vive en los repositorios** (`infra/`,
  READMEs) y **sí se habla de ella en el informe** — como compromiso declarado con su causa
  (§17.6/§18/§19), nunca en presente ni como instructivo de despliegue.

---

## 1. Qué cambió, en una línea

El distribuidor era el único módulo sin interfaz de red: el BFF lo criaba como proceso
hijo, así que **no podía ser una unidad desplegable propia**. Ahora **también** expone
servicio HTTP (`eovrt-distribute serve`, `:8082`, espejo del control-plane). **El CLI y el
acople por subproceso siguen intactos y el subproceso sigue siendo el default del runner**:
ADR-018 no se deroga.

**Siguen siendo TRES patrones de acople, no cuatro.** Lo que desaparece es la excepción: el
primer patrón (HTTP config-driven) pasa a cubrir los tres módulos en vez de dos.

> ⛔ ✎ **2026-08-18 (horas más tarde) — los dos párrafos de arriba quedaron SUPERADOS por
> [ADR-020](../decisiones/adr-020-http-como-unico-acople-de-distribucion.md), constancia en
> [doc 125](125-adr020-http-unico-acople.md).** ADR-018 **sí fue derogada**: HTTP pasó a ser
> el **default** del runner y el subproceso bajó a **fallback operativo**
> (`EOVRT_CONSOLE_DISTRIBUTION_TRANSPORT=subprocess`), dejando de ser un patrón de acople.
> Por lo tanto los patrones son **DOS**, no tres. Todo lo demás de este documento —el
> servicio, sus contratos, la verificación DBE y la cadena EBE en vivo— sigue vigente tal
> cual: lo único que cambió es cuál de los dos caminos es el default.

## 2. Verificación

**DBE — equivalencia semántica (el criterio central).** La misma corrida de 12 alertas por
el camino histórico (CLI) y por el nuevo (HTTP), a directorios distintos:

| | Resultado |
|---|---|
| `distribution_summary.json` | **idéntico** (normalizando sólo la latencia) |
| `counts` | `delivered: 6` · `suppressed_cooldown: 6` |
| `notifications.jsonl` | 12 registros en ambos · **secuencia `(alert_id, outcome)` idéntica** |

**EBE — cadena viva completa con hardware real (2026-08-18).** OAK-D `169.254.31.137` →
media-plane (`gdino-tiny-560`) → bus `:5557` → control-plane → bus de alertas `:5558` →
**servicio HTTP de distribución** → MQTT real:

| Tramo | Resultado |
|---|---|
| control | 15 unidades · **2 alertas (CR-01 high + CR-02 medium)** · `bus_dropped_events: 0` · `degraded: False` |
| distribución | leyó **2 del bus, 0 perdidas** · `counts: {delivered: 2}` con PUBACK real |
| `t_alert_notification_ms` | n=2 · min 4,834 · mean 22,811 · **p95 40,789 ms** |

> **Estas cifras son de una verificación funcional, no de una campaña de medición**: n=2 y
> una sola corrida. **No se citan como resultado del informe**; la cifra citable de
> `t_alert-notification` sigue siendo la de `operacion/118` (p95 64,534 ms, n=460).

**Suites:** distribuidor **133 passed** (0 fallos en 10 corridas) · webconsole backend
**663 passed**. Ninguna suite previa fue editada.

## 3. Lo que la revisión encontró y que conviene no perder

- **Un bug real de producción, preexistente al plan**: `run_manager` leía
  `summary["termination_reason"]`, clave inexistente (vive en `source_stats`) ⇒ el estado
  `cancelled` era **inalcanzable** y toda corrida cancelada se reportaba `succeeded`.
  Aguas abajo, el cliente del BFF habría tratado una distribución **cancelada como
  exitosa**. Corregido y **confirmado en vivo**: `POST /cancel` → 202 → `cancelled`.
  Lo destapó **apretar un assert flojo** (`status in {"cancelled","succeeded"}`): un assert
  que acepta un conjunto puede estar ocultando que una rama nunca se alcanza.
- **Un `DELETE` decorativo**: borraba `runs_dir/<run_id>`, directorio que nadie crea (los
  artefactos van a `out_dir`, que elige el cliente). Devolvía 204 sin borrar nada.
  Ahora olvida el registro en memoria y **nunca toca `out_dir`** — borrarlo desde un
  endpoint HTTP sería borrado arbitrario de directorios a pedido del cliente.
- **La instalación documentada dejaba la suite rota**: `pip install -e ".[mqtt,dev]"` sin
  el extra `service` impedía importar ~40 de 133 tests. La verificación de aislamiento
  cubría el *runtime*, no el *desarrollo*.
- **Dos condiciones de carrera** en la reserva de corrida activa, cerradas con
  check-and-reserve atómico y liberación del slot bajo el mismo lock, con test de
  regresión determinístico (sin `sleep`) verificado por prueba negativa.

## 4. Trampas de entorno encontradas al verificar (no son del código)

1. **La IP de la OAK-D se lee del preset `cameras/oak_d_lab.yaml` (`169.254.31.137`)**, no
   se asume. La de fábrica `169.254.1.222` **responde al ping con la MAC real y aparece
   `REACHABLE` en ARP**, pero `depthai` falla ahí con `Failed to find device after
   booting` — ese mensaje (distinto de `Cannot find any device`) es la pista de que la IP
   está equivocada, no de que la cámara esté mal.
2. **`alert_bus.enabled` está en `False` por default** y el `control.yaml` de
   `ebe_oakd_live` no lo enciende (es anterior a esta integración): sin inyectarlo, la
   distribución lee **0 alertas** aunque el control produzca varias.
3. **`pgrep -af "mosquitto|amqtt"` matchea su propio comando** y hace creer que hay broker.
   Verificar con `ss -ltn`. Sin broker, la distribución hace 3 reintentos y manda a
   `dead_letter`, que es el comportamiento correcto.
4. **`pkill -f <patrón>` mata el propio shell** (trampa ya documentada del proyecto). Matar
   por PID.

## 5. Qué queda abierto

- Containerización (§1), diferida con causa.
- Menores registrados y triados en la revisión final: warning `httpx`→`httpx2`, cobertura
  de la rama `isfinite`, contrato no documentado de `get()`/`cancel()` sobre el GIL,
  `response.json()` del poll sin protección. Ninguno bloquea.
- **Ajeno a este trabajo:** `test_prompt_store.py::test_repo_frozen_sets_integrity` falla
  por `prompts/coco_val2017_80.yaml` (`track: retention`, sin commitear, del arnés de
  retención de T2) contra el `Literal["core","demo","comparative"]` de `prompt_store.py`.
  Y `test_stream_proxy.py::test_ws_preview_reenvia_binario` es **flaky preexistente**
  (pasa aislado, falla intermitentemente bajo carga). Decisión del usuario.
