# ADR-018 — El tercer módulo se acopla por **subproceso local**, no por servicio HTTP

> **No deroga ninguna ADR previa.** Registra, con fecha posterior a la implementación, un
> patrón de acople que [ADR-008](adr-008-control-plane-servicio-minimo.md) y
> [ADR-009](adr-009-config-centralizada-webconsole.md) no contemplan.
> **No agrega capacidad**: documenta lo que ya existe, verificado y con tests, de modo que
> **no colisiona con el cierre de puerta de [ADR-015](adr-015-cierre-de-alcance.md) §2a**
> ni con la cláusula de freno de [ADR-016](adr-016-reapertura-acotada-distribucion.md) §2b.

- **Fecha:** 2026-08-15
- **Estado:** Aceptada (usuario, 2026-08-15)
- **Decisión que atiende:** la plataforma tiene **tres** patrones de acople y el registro
  documental sólo declaraba dos. El tercero, además, impone un requisito de despliegue que
  hasta hoy vivía únicamente en un README de infraestructura.
- **Decisor:** usuario, 2026-08-15
- **Serie:** proyecto (`ADR-001…018`, tres dígitos). No confundir con la serie local del
  control-plane (`ADR-0001…0013`, cuatro dígitos).

---

## 1. Contexto

Hasta ADR-016, el registro describía dos maneras de acoplar componentes:

1. **HTTP config-driven.** El media-plane (`:8080`) y el control-plane (`:8081`) son
   servicios; la webconsole y el runner son **clientes** de ambos (ADR-008/009). Ninguno de
   los dos clientes toca el bus.
2. **Bus ZeroMQ PUB/SUB + msgpack.** El camino live media→control, con envelope
   `bus.envelope.v1` (ADR-003).

Cuando ADR-016 reabrió la distribución, el módulo nuevo (`e-ovrt_alert-distribution`) **no
se construyó como servicio**: expone un único entry point de consola,
`eovrt-distribute = "eovrt_distribution.cli:main"`, y no importa FastAPI ni uvicorn. No hay
puerto que llamar.

En consecuencia, el runner del BFF lo **lanza como proceso hijo local**
(`webconsole/backend/src/eovrt_webconsole/experiment/runner.py`, vía
`asyncio.subprocess` con `stdout`/`stderr` en PIPE). Ese es el tercer patrón, y no estaba
declarado en ningún ADR.

**Precisión importante sobre qué es lo nuevo.** El *dato* sigue viajando por el bus: el
distribuidor consume las alertas del control-plane con `ZmqSource` sobre `:5558`, que es la
familia de ADR-003. Lo que no tiene precedente es el **control del ciclo de vida**: quién
arranca, supervisa y cosecha el proceso. En los otros dos módulos eso lo resuelve un
servicio de larga vida al que se le hace una request; acá lo resuelve el BFF criando un
hijo por corrida.

## 2. Decisión

**(a) Se acepta el patrón BFF-subproceso para el módulo de distribución, y sólo para él.**
El runner resuelve el binario con `resolve_distribution_executable()` por orden de
preferencia explícito: variable de entorno `EOVRT_DISTRIBUTION_EXECUTABLE` → `shutil.which`
en el `PATH` → fallback al venv del repo hermano
(`../e-ovrt_alert-distribution/.venv/bin/eovrt-distribute`). Si ninguno resuelve, falla con
error explícito, nunca en silencio.

**(b) El requisito de contenedor es parte de la decisión, no una nota de operación.** La
consola dockerizada **no ve** el repo hermano: para orquestar distribución desde el
contenedor es **obligatorio** montar el binario en un path visible y setear
`EOVRT_DISTRIBUTION_EXECUTABLE`. Sin eso, el preflight falla antes de disparar la corrida.

**(c) No se convierte el distribuidor en servicio.** Sería capacidad nueva y está prohibido
por ADR-016 §2b. La CLI es además el camino reproducible offline (DBE), coherente con la
decisión equivalente que el control-plane ya tenía.

**(d) Este patrón no se extiende.** Cualquier módulo futuro se acopla por HTTP o por bus.
Si aparece un segundo BFF-subproceso, este ADR queda violado (§5).

## 3. Fundamento

**Por qué se llegó acá y no fue un error.** El recorte de ADR-005 pedía "un canal MQTT en
repo propio", no un cuarto servicio. Levantar un proceso de larga vida para un módulo que
sólo actúa durante una corrida —y que en DBE se ejecuta *después* de que la corrida
terminó, sobre `control/alerts.jsonl`— habría agregado superficie operativa sin
contrapartida. El subproceso es el acople más barato que cumple el recorte.

**Por qué merece ADR igual.** Tres razones concretas, todas verificadas:

- **Rompe la simetría que el informe describe.** Un lector que tome ADR-008/009 al pie de
  la letra espera tres servicios y una consola cliente. Hay dos servicios, una CLI y un
  padre que la cría.
- **Tiene una falla de despliegue propia.** El binario puede no existir, no estar en el
  `PATH`, o estar fuera del contenedor. Por eso existe el preflight de binario (y de TCP al
  broker cuando `channel.mode: live`) — un chequeo que los otros dos acoples no necesitan.
- **Tiene una falla de observabilidad propia.** Un proceso hijo puede llenar el pipe de
  `stderr` y trabarse. Por eso el runner drena el pipe concurrentemente, con cap de 1 MiB,
  redacción de secretos y volcado a `stderr.log`. Nada de eso aplica a un cliente HTTP.

**Por qué no toca ninguna cifra.** Este ADR no modifica un solo número medido. Describe
código ya escrito, probado y verificado al 2026-08-14.

## 4. Impacto

- **ADR-008 / ADR-009:** sin derogación. Se les agrega un vecino: la webconsole sigue
  siendo cliente HTTP de los dos planos, y además es **padre** del distribuidor.
- **ADR-003:** sin cambios. El bus sigue siendo el transporte de datos, incluido el tramo
  control→distribución (`:5558`).
- **ADR-016:** sin cambios; este ADR documenta cómo aterrizó su §2a.
- **`infra/platform/README.md`:** su requisito de `EOVRT_DISTRIBUTION_EXECUTABLE` deja de
  ser sólo operativo y pasa a estar respaldado por decisión registrada.
- **Informe:** la sección de arquitectura debe describir **tres** patrones de acople, no
  dos, y nombrar la asimetría del tercero como decisión con causa.
- **`estado-de-implementacion-adrs.md`:** la nota del 2026-08-14 sobre el patrón se
  reemplaza por el puntero a este ADR.

## 5. Criterio de invalidación

Este ADR queda violado si ocurre cualquiera de estas dos cosas:

1. **Aparece un segundo acople por subproceso.** El patrón se aceptó como excepción
   acotada a un módulo, no como alternativa general a HTTP/bus.
2. **El distribuidor se convierte en servicio de larga vida.** Eso sería capacidad nueva
   (ADR-016 §2b) y exige un ADR sucesor, no una enmienda a éste.

## Referencias

ADR-003 (bus ZeroMQ) · ADR-005 (recorte de la distribución, repo propio) ·
ADR-008 (control-plane como servicio mínimo) · ADR-009 (webconsole superficie primaria) ·
ADR-011 (frontera de la política de alertas) · ADR-016 (reapertura acotada) ·
`webconsole/backend/src/eovrt_webconsole/experiment/runner.py`
(`resolve_distribution_executable`, drenaje de `stderr`, consolidación) ·
`webconsole/backend/src/eovrt_webconsole/preflight.py` ·
`e-ovrt_experimental-setup/infra/platform/README.md` ·
`e-ovrt_alert-distribution/pyproject.toml` (`[project.scripts]`) ·
`operacion/119` §2 (hallazgos A-1, A-2, B-1, B-2 que motivaron el registro).
