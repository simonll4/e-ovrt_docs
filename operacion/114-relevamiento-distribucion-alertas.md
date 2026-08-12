# 114 — Relevamiento del módulo de distribución de alertas (estado, brechas y plan de infra)

- **Fecha:** 2026-08-11
- **Qué es esto:** relevamiento del repo `e-ovrt_alert-distribution` tras la
  implementación del grueso del módulo. Determina el estado real **verificado
  ejecutando**, lista las brechas, y define cómo incorporarlo al deploy local
  junto con los demás servicios para probarlo contra las corridas ya ejecutadas.
- **Normativa:** [ADR-016](../decisiones/adr-016-reapertura-acotada-distribucion.md)
  (estatuto vigente: trabajo comprometido, recorte de ADR-005, E-06 excluida) ·
  ADR-005 · ADR-011 · [spec 45](../specs/45-distribucion-alertas.md) ·
  [`informe/ajustes/material-etapa-3/92b`](../informe/ajustes/material-etapa-3/92b-concrecion-distribucion-alertas.md)
  (concreción técnica: es el contrato contra el que se releva).
- **Evidencia:** `datos/114-relevamiento-distribucion/` (3 summaries, las 2 configs
  usadas, el broker stub y un mensaje MQTT publicado).

**✎ 2026-08-11, misma jornada — C1 y C3 CERRADOS con TDD.** El usuario pidió seguir
con el orden del §6. **C3**: `distribution_summary.json` ahora agrega
`talert_notification_ms` **por `latency_mode`** (`{"live": {...}, "wall_clock_dbe":
{...}}`), no un bloque ciego — resuelto agrupando en `Distributor.run()`; test nuevo
con alertas mixtas (`DirectSource` ahora acepta `SourcedAlert` con `ts_publish_ms`,
además de dicts). **C1**: una alerta con campo requerido faltante ya **no aborta la
corrida** — `NotificationEnvelope.from_alert` se envuelve en `try/except (KeyError,
ValidationError)`, se cuenta en `skipped_invalid_alerts` (nuevo campo del summary,
al lado de `source_stats`) y la corrida sigue. Re-corrido el fixture exacto que
disparó el `KeyError` original (`datos/114-.../` no lo persistía, se reconstruyó
igual): `exit 0`, `skipped_invalid_alerts: 1`, summary escrito, las otras 2 alertas
entregadas. Suite: **39 tests + 1 integración**, ruff limpio. Sin commitear (regla
del workspace). El §3.5 y §4 de abajo quedan como estaban **al momento del
relevamiento** — es lo que corresponde corregir con código, no reescribir el
registro; ver el veredicto actualizado en el §1.

**✎ 2026-08-11, misma jornada — A1 CERRADO con TDD (el 6º criterio de terminado).**
`report.py` de `experimental-setup` ya integra `distribution_summary.json` como
cuarto hermano `runs/exp_<id>/distribution/` (ADR-014). Diseño (mismo patrón que
`t_capture->alert` con `DBE_MEDIA_TIME`, y que `censored_episodes`): la métrica
`t_alert-notification` en `resultados` es `computed` (p95 del modo `live`) **solo**
si hay latencia `live`; si el summary **solo** trae `wall_clock_dbe`, es
`not_interpretable` / `distribution_wall_clock_dbe_only` — nunca se reporta un
reloj de pared de reproceso como si fuera la latencia real (exactamente el
caveat que 92b §8 exige). Sin `distribution/`, comportamiento intacto
(`not_applicable`/`no_distribution`, 0 reportes viejos rotos). El
`distribution_summary.json` completo (counts, `skipped_invalid_alerts`, la
latencia por modo) pasa verbatim en una sección nueva `report["distribucion"]`
— mismo patrón que el detalle de censura. El hito `notificacion_entregada`
—hardcodeado `False` desde que existía el campo— ahora refleja `delivered > 0`
real. Verificado contra una corrida consolidada real (`video16_clip10_gt`, 2
alertas, DBE puro): `not_interpretable`/`distribution_wall_clock_dbe_only`,
`notificacion_entregada: true`, sección `distribucion` completa, `report.md`
renderiza la fila sin romper. **28 tests nuevos/tocados en
`test_report_generator.py`, suite completa del backend 592 pasan, ruff limpio.**

**A3/B3 — resuelto sin Docker.** El usuario decidió NO dockerizar el broker:
**el bloque `mosquitto` queda escrito en el compose de `infra/platform`** (para
cuando el resto del deploy se dockerice) **pero sin verificar** — el camino
que corre HOY es un proceso común del host, igual que el control-plane. En vez
de Mosquitto (necesita `apt`/`sudo`, no disponible en esta sesión), se usó
**`amqtt`** — broker MQTT 3.1.1 puro Python, instalable con `pip` en un venv
aislado, sin tocar el sistema. Con `amqtt` corriendo y un **suscriptor
independiente** (equivalente exacto a `mosquitto_sub -t 'eovrt/alerts/#' -v`,
`datos/114-.../` script `mqtt_sub.py`), se re-corrió el replay de `v06_c01`
(193 alertas) en `channel.mode: live`: **23/23 mensajes recibidos por el
suscriptor, en vivo, contra un broker MQTT real** — no ya el stub de 80 líneas
de la primera pasada. Esto era la única parte del criterio 3 (spec 45 §7) que
seguía siendo un smoke; ahora es la demo real que pide 92b §7. Evidencia:
`datos/114-.../08-mqtt-real-broker-summary.json` y
`09-mqtt-real-broker-mensajes-recibidos.jsonl`. Documentado en
`infra/platform/README.md` (nueva sección) + `infra/platform/mosquitto/`
(`mosquitto.conf` para Docker, `amqtt.yaml` para el camino real de hoy).

Sin commitear.

---

## 1. Veredicto en una línea

**El módulo está funcionalmente completo y hoy verifiqué 5 de los 6 criterios de
terminado** de spec 45 §7 / 92b §11 — incluidos los dos que el plan de
implementación había dejado abiertos (live contra el publisher real, y entrega
MQTT con PUBACK). Lo que falta **no es el módulo: es su acople** — reporte,
webconsole, broker en el compose — más tres asperezas de robustez y el hecho de
que **el repo no tiene ni un commit**.

---

## 2. Estado del repo

`e-ovrt_alert-distribution`, rama `main`, remote `git@github.com:simonll4/e-ovrt_alert-distribution.git`.

| Aspecto | Estado |
|---|---|
| Tareas del plan (11) | 1–10 completas; 11 completa salvo el criterio de MQTT real |
| Código | 9 módulos, ~530 líneas en `src/` — la estructura exacta de spec 45 §2 |
| Tests | **37 pasan** + 1 de integración (`-m integration`), que hoy también pasó |
| Lint | `ruff check src tests` limpio |
| Contratos | `control.notification.v1` y `control.delivery.v1` idénticos a 92b §3.2/§3.3, campo por campo |
| **Commits** | **cero** — todo el árbol está untracked |

El pipeline de 5 etapas de 92b §2 está implementado tal cual (source → policy →
ledger → channel con retry → records), con las tres fuentes (`DirectSource`,
`JsonlReplaySource`, `ZmqSource`), el cooldown por `(condition_id, source_id)`
sobre `media_timestamp_ms`, el ledger rehidratado desde `notifications.jsonl` y
los cinco `outcome` del contrato.

---

## 3. Lo que verifiqué ejecutando (no leyendo)

Corrida de referencia: **`v06_c01` del lote de internet, campaña gen.3** —
193 alertas reales, la corrida de control más densa del banco.

### 3.1 Criterio 1 — replay DBE sobre corrida real + idempotencia ✔

```
1ª pasada:  delivered 23 · suppressed_cooldown 170   (193 leídas, 0 malformadas)
2ª pasada:  skipped_duplicate 23 · suppressed_cooldown 170
```

El ledger reconoce las 23 entregadas y no re-entrega ninguna.

### 3.2 Criterio 2 — live EBE contra el publisher real del control-plane ✔

Es el criterio que el plan había declarado *"fuera del alcance de este repo"*.
Lo cerré: levanté `eovrt-distribute live` suscripto a `tcp://127.0.0.1:5558`, y
después disparé el mismo clip por el control-plane con `alert_bus.enabled: true`
y `wait_for_subscriber_ms: 10000`.

```
delivered 23 · suppressed_cooldown 170
source_stats: read 193 · bus_dropped_events 0 · skipped_malformed 0
experiment_id: "relev-dist-2026-08-11"   ← propagado end-to-end
```

Tres cosas quedan probadas de una sola vez:

1. **Paridad DBE↔EBE:** el resultado por el bus es **idéntico** al del archivo
   (23/170). Es la misma propiedad que sostiene al resto de la plataforma.
2. **Cierre 1:1 (ADR-007):** el proceso terminó por el sentinel `run_finished`
   del topic `run.lifecycle.v1.*`, no por timeout — el `--idle-timeout-ms 30000`
   nunca se agotó.
3. **`experiment_id` (ADR-004)** viaja del `AlertEvent` al summary sin pérdidas.

### 3.3 Criterio 3 — entrega MQTT real con QoS 1 y PUBACK ✔ (con salvedad)

No hay Mosquitto instalado ni Docker disponible en esta WSL, así que escribí un
**broker MQTT 3.1.1 mínimo** (CONNECT/PUBLISH-QoS1/PUBACK/PINGREQ, 80 líneas, en
`datos/114-.../06-mini-broker-mqtt.py`) y corrí el canal en `mode: live`:

```
delivered 23 · mode "live" · 23 mensajes recibidos en el broker
topic: eovrt/alerts/medium        payload: NotificationEnvelope JSON completo
t_alert-notification: min 0,73 ms · mean 3,41 ms · p95 1,80 ms
```

**Salvedad:** un stub no es Mosquitto. Prueba que el camino paho (conexión lazy,
`publish`, `wait_for_publish`, PUBACK de QoS 1) funciona y que el payload sale
bien formado; **no** sustituye la demo con `mosquitto_sub` que pide 92b §7. Los
números de latencia de arriba son de loopback contra un stub: **no son una cifra
reportable**, son un smoke.

### 3.4 Criterios 4 y 5 — dedup de QoS 1 y ráfaga de cooldown ✔

Cubiertos por tests (`test_qos1_duplicate_delivery_deduped_by_ledger`,
`test_burst_same_condition_source_suppressed`, `test_reallows_after_window`) y
además observables en la corrida real: 170 de 193 alertas suprimidas es
exactamente la política de ADR-011 haciendo su trabajo sobre una corrida densa.

### 3.5 Criterio 6 — `report.json` con la distribución integrada ✘

**No cumplido.** Es la brecha A1 de abajo.

---

## 4. Brechas

### A. Acople — lo que falta para cerrar el recorte comprometido por ADR-016

| # | Brecha | Dónde | Por qué importa |
|---|---|---|---|
| **A1** | `report.json` **no** integra la distribución: `t_alert-notification` está hardcodeado como `not_applicable` / causa `no_distribution` | `experimental-setup`, `experiment/report.py:418` | Es el 6º criterio de terminado de spec 45 §7 y de 92b §11 |
| **A2** | La webconsole **no** muestra los `outcome` de entrega | `experimental-setup/webconsole` | **ADR-016 §2a lo nombra explícitamente** dentro del recorte comprometido ("vista en la webconsole existente"). Hoy el frontend solo tiene la etiqueta `no_distribution` en `labels.ts` |
| **A3** | **Mosquitto no está en ningún compose** | `experimental-setup/infra/platform` | spec 45 §5 y 92b §10 lo dan por hecho; sin él no hay demo de defensa |

### B. Infra y orquestación

| # | Brecha | Nota |
|---|---|---|
| **B1** | El repo de distribución no tiene `Dockerfile` | — |
| **B2** | **El control-plane tampoco está dockerizado** — el compose de plataforma solo trae `console` + 7 `mp-*`; la consola lo alcanza en `http://localhost:8081` del host | Preexistente, no una regresión. **Define la forma correcta de meter la distribución** (ver §5) |
| **B3** | Docker no está disponible en esta WSL ahora mismo (integración de Docker Desktop apagada) | Bloquea el camino compose hasta que se encienda |
| **B4** | Nadie orquesta al distribuidor: `experiment/runner.py` secuencia media→control y no lanza `eovrt-distribute` | En live, la regla *suscribirse antes del run* recae hoy en el operador. Para DBE no hace falta |
| **B5** | Los artefactos de distribución no tienen lugar en el layout de corrida (ADR-014) | Hoy `--out-dir` es libre. El reporte necesita una convención fija para levantarlos |

### C. Robustez del código — las tres las verifiqué, no las deduje

**C1 — una alerta con JSON válido pero un campo faltante aborta la corrida entera.**
`NotificationEnvelope.from_alert` indexa con `alert["severity"]`; `JsonlReplaySource`
solo cuenta `skipped_malformed` cuando el JSON no parsea. Probado con un fixture de
3 alertas donde la 2ª no trae `severity`:

```
KeyError: 'severity' → exit 1 · notifications.jsonl con 1 línea
distribution_summary.json NUNCA se escribe
```

Contradice de frente la propiedad que 92b §2 declara como la garantía del módulo
(*"ninguna alerta desaparece en silencio"*): acá desaparecen todas las posteriores,
y encima sin summary. Corresponde `outcome: failed` con el error, o un contador
`skipped_invalid` en `source_stats`, y seguir.

**C2 — `notifications.jsonl` crece sin techo entre re-ejecuciones.** La policy corre
**antes** que el ledger, así que las supresiones se re-escriben en cada pasada. Medido:
193 alertas → 386 líneas tras dos pasadas. El ledger relee el archivo completo al
arrancar. No es un error de corrección (el resultado es idempotente), pero un clip
denso re-corrido varias veces infla el artefacto y el arranque.

**C3 — `latency_mode` no llega al summary.** El bloque `talert_notification_ms`
agrega min/mean/p95 sin decir si son `live` o `wall_clock_dbe`; hay que abrir
`notifications.jsonl` y mirar registro por registro. **92b §8 dice que el caveat va
declarado siempre**, y lo compara nominalmente con el error del G2A. Hoy el summary
—que es lo que va a leer el reporte— no lo declara.

**C4 — el venv del repo es Python 3.14**, contra 3.11 del control-plane y de la
consola. Funciona, pero la imagen debería fijar 3.11 para no descubrir diferencias
recién en el deploy.

**C5 — cero commits.** Todo el trabajo está untracked. (No commiteo: regla del
workspace.)

---

## 5. Cómo incorporarlo a la infra local

### 5.1 La decisión de forma, primero

El compose de plataforma **no dockeriza el control-plane**: corre en el host y la
consola lo alcanza por `EOVRT_CONSOLE_CONTROL_SERVICE_URL`. Meter el distribuidor
como contenedor mientras el plano del que consume vive en el host sería incoherente,
y además el bus ZeroMQ (`tcp://…:5558`) cruzaría la frontera del contenedor para
nada.

**Recomendación: al compose va solo el broker; el distribuidor corre en el host,
igual que el control-plane.** Es lo que dice literalmente 92b §10 (*"el broker
Mosquitto va en el compose"* — del distribuidor no dice nada) y es lo mínimo que
cierra el módulo sin tocar la arquitectura de deploy a un mes de la defensa
(ADR-016 §6.2: si la implementación compromete el cronograma, se revierte).

El Dockerfile del distribuidor (B1) queda como **opcional**, para después de la
entrega o si se decide dockerizar el control-plane.

### 5.2 Paso 1 — Mosquitto en el compose (cierra A3)

En `e-ovrt_experimental-setup/infra/platform/docker-compose.yml`:

```yaml
  mosquitto:
    image: eclipse-mosquitto:2
    ports: ["1883:1883"]
    networks: [eovrt]
    volumes:
      - ./mosquitto/mosquitto.conf:/mosquitto/config/mosquitto.conf:ro
    healthcheck:
      test: ["CMD", "mosquitto_sub", "-t", "$$SYS/#", "-C", "1", "-i", "hc", "-W", "3"]
      interval: 30s
      timeout: 5s
```

con `infra/platform/mosquitto/mosquitto.conf`:

```
listener 1883
allow_anonymous true     # laboratorio single-host, sin exposición externa —
                         # mismo criterio ya aceptado para el socket de Docker
persistence false
```

Sin `profiles:`, para que suba con la consola. Requiere **B3** (encender la
integración de Docker Desktop en WSL).

### 5.3 Paso 2 — convención de artefactos (cierra B5)

El layout de corrida consolidada es `runs/exp_<id>/{media,control,report}/`.
La distribución entra como **cuarto hermano**:

```
runs/exp_<id>/distribution/{notifications.jsonl,dead_letter.jsonl,distribution_summary.json}
```

Es decir, `--out-dir runs/exp_<id>/distribution`. Nada que implementar: es fijar
la convención y usarla.

### 5.4 Paso 3 — el reporte levanta el summary (cierra A1)

`generate_report(consolidated_dir)` ya lee `media/` y `control/` con
`_read_json`, que devuelve `{}` si el archivo no está. El parche es simétrico y
tolerante:

- leer `consolidated_dir / "distribution" / "distribution_summary.json"`;
- si está vacío → se conserva el `not_applicable` / `no_distribution` de hoy
  (ninguna corrida vieja cambia);
- si está → emitir `t_alert-notification` con el valor real **y el `latency_mode`
  como caveat** — lo que exige resolver **C3** primero, porque hoy el summary no
  lo trae.

Orden correcto: **C3 antes que A1.**

### 5.5 Paso 4 — la vista en la webconsole (cierra A2)

Es el ítem que ADR-016 nombra y el único con superficie de UI. Lo mínimo que
cumple el recorte —sin dashboard propio, que es E-06— es una fila de conteos por
`outcome` en la vista de corrida, alimentada por el mismo `report.json` del paso
3. Si el tiempo aprieta, este es el ítem a negociar, no A1.

### 5.6 Cómo probarlo contra las pruebas ya ejecutadas

Las corridas de control archivadas están en `docs/operacion/datos/109-…` y
`110-estrato-b-gen3/` (13 clips del lote, dos granularidades). **DBE no necesita
nada de lo anterior** — se puede barrer hoy mismo:

```bash
cd e-ovrt_alert-distribution
for A in ../docs/operacion/datos/110-estrato-b-gen3/subject/control_runs/*/alerts.jsonl; do
  R=$(basename "$(dirname "$A")")
  .venv/bin/eovrt-distribute replay --alerts "$A" --out-dir "runs/$R" --config configs/example.yaml
done
```

Con Mosquitto arriba, el mismo barrido con `channel.mode: live` y un
`mosquitto_sub -t 'eovrt/alerts/#' -v` al lado es **exactamente la demo de
defensa** de 92b §7 — y sobre datos reales del banco, no sintéticos.

Para EBE está la receta que usé hoy: config del control-plane con
`alert_bus.enabled: true` + `wait_for_subscriber_ms`, distribuidor arriba primero,
control-plane después (`datos/114-…/04-…yaml`).

---

## 6. Orden sugerido

Ordenado por *cierra un criterio escrito* sobre *mejora el código*:

1. **C3** — `latency_mode` al summary (bloquea A1, y es lo que 92b §8 exige declarar).
2. **C1** — no morir por una alerta incompleta (contradice la garantía declarada del módulo).
3. **A3 + B3** — Mosquitto en el compose, con Docker encendido.
4. **B5 + A1** — convención de artefactos y reporte integrado ⇒ **cierra el 6º criterio**.
5. **Barrido DBE sobre los 13 clips del lote** ⇒ primeras cifras de distribución sobre datos reales.
6. **A2** — vista en la webconsole (lo que ADR-016 nombra; negociable si aprieta el cronograma).
7. **C2** (higiene del JSONL), **C4** (Python 3.11), **B1/B4** (Docker del distribuidor, orquestación en el runner) — **todos post-entrega**, ninguno bloquea.

**C5 (commitear el repo) es del usuario y va cuando él lo diga.**

---

## 7. Lo que este relevamiento NO toca

Ninguna cifra medida del tramo experimental. ADR-016 §4 lo dice y se cumple: el
módulo no re-corre nada, no cambia un solo número, y las latencias del §3.3 son
un smoke contra un stub de loopback — **no son un resultado y no van al informe**.
