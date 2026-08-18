# ADR-019 — El distribuidor **también** expone servicio HTTP, para ser una unidad desplegable

> **No deroga ninguna ADR previa, y en particular no deroga
> [ADR-018](adr-018-acople-bff-subproceso-distribucion.md).** El acople por subproceso
> local sigue existiendo, sigue implementado y sigue siendo el camino **default** del
> runner: lo que este ADR registra **no es un patrón nuevo**, sino que el distribuidor
> **entra al primero de los tres que ya existían** (HTTP config-driven). Los patrones
> siguen siendo **tres**; lo que desaparece es la **excepción**: hasta hoy ese patrón
> cubría dos módulos de tres, y el distribuidor era el único sin interfaz de red.
> *(✎ 2026-08-18: la primera redacción de este ADR decía "un cuarto patrón de acople".
> Era impreciso y se corrigió antes de que llegara al informe — contar cuatro patrones
> sugeriría una complejidad de acople que la plataforma no tiene.)*
>
> ⚠️ **✎ 2026-08-18 (mismo día, más tarde) — [ADR-020](adr-020-http-como-unico-acople-de-distribucion.md)
> movió el mojón otra vez, y en la dirección contraria a este párrafo:** ADR-018 **sí
> quedó derogada**, el default pasó a HTTP y el subproceso bajó a fallback operativo. Por
> lo tanto los patrones de acople son **DOS**, no tres: HTTP config-driven (los tres
> módulos) y bus ZeroMQ. Lo que este ADR aporta sigue en pie —el servicio, su contrato y
> su verificación—; lo que cambió es el estatuto del subproceso.
> Todo lo escrito sobre ADR-018 —incluida la fila del §17.3 y los relevamientos 114/118—
> **sigue siendo cierto** y sigue siendo citable.

- **Fecha:** 2026-08-17
- **Estado:** Aceptada (usuario, 2026-08-17)
- **Decisión que atiende:** el distribuidor era el único módulo de la plataforma sin
  interfaz de red, y por eso **no podía ser una unidad desplegable propia**: al ser criado
  como proceso hijo, quedaba obligado a compartir contenedor y host con el BFF que lo
  lanza. ADR-018 §1 ya había señalado que ese patrón "impone un requisito de despliegue".
- **Decisor:** usuario, 2026-08-17
- **Serie:** proyecto (`ADR-001…019`, tres dígitos). No confundir con la serie local del
  control-plane (`ADR-0001…`, cuatro dígitos).

---

## 1. Contexto

Tras ADR-018 la plataforma tiene tres patrones de acople: HTTP config-driven a los dos
planos (ADR-008/009), bus ZeroMQ PUB/SUB (ADR-003) y BFF-subproceso para la distribución.

El tercero resuelve el control del ciclo de vida criando un proceso hijo
(`asyncio.create_subprocess_exec` en
`webconsole/backend/src/eovrt_webconsole/experiment/runner.py`), lo que impone dos
condiciones que los otros dos módulos no tienen:

1. **Co-ubicación obligatoria.** Quien controla la corrida tiene que poder ejecutar el
   binario. No hay puerto que llamar, así que el distribuidor no puede vivir en su propio
   contenedor ni en otro host.
2. **Instalación acoplada.** La imagen de la consola tendría que traer el paquete del
   distribuidor además del backend, mezclando dos repos en un artefacto.

Eso vuelve al distribuidor el único módulo que no se puede levantar por separado, y es
justamente lo que impide que la plataforma se despliegue completa en otra máquina.

## 2. Decisión

El distribuidor **suma** un servicio HTTP, espejo del control-plane:

- Nuevo subcomando `eovrt-distribute serve` (puerto por defecto `:8082`, siguiendo la
  serie `:8080` media-plane / `:8081` control-plane).
- `POST /api/runs` dispara una corrida y devuelve `201` con su id; el estado y el resumen
  se leen por `GET /api/runs/{id}`. La corrida es **asíncrona**: una corrida live dura
  minutos y no puede sostener una conexión HTTP abierta.
- **El CLI se conserva sin cambios.** `replay` y `live` siguen siendo el camino offline,
  igual que el control-plane conservó el suyo.
- El runner del BFF **puede** hablarle por HTTP, reutilizando el mismo patrón de polling
  que ya usa con los otros dos planos. **El default del runner sigue siendo el
  subproceso (ADR-018)**: el camino HTTP es **opt-in** vía
  `EOVRT_CONSOLE_DISTRIBUTION_TRANSPORT=http`. La función que cría el subproceso se
  conserva intacta — por eso ADR-018 no se deroga.
  > ✎ **2026-08-18 — superado por [ADR-020](adr-020-http-como-unico-acople-de-distribucion.md):**
  > el default se **invirtió**. HTTP pasó a ser el camino normal y el subproceso quedó
  > como **fallback** (`EOVRT_CONSOLE_DISTRIBUTION_TRANSPORT=subprocess`), dejando de ser
  > un patrón de acople. ADR-018 quedó **derogada**. El resto de esta ADR sigue vigente:
  > lo que cambió es cuál de los dos caminos es el default, no el diseño del servicio.

### Lo que NO cambia

- **El dato sigue viajando por el bus.** El distribuidor consume las alertas del
  control-plane con `ZmqSource` sobre `:5558` (familia ADR-003). Este ADR toca el control
  del ciclo de vida, no el transporte del dato.
- **La salida sigue siendo MQTT** (spec 45, ADR-005/011).
- **`t_alert-notification` sigue valiendo tal cual está medido.** Mide `bus de alertas →
  PUBACK MQTT` (p95 = 64,534 ms, n = 460; `operacion/118`), tramo que este cambio no
  atraviesa. No hay que re-medirlo ni re-reportarlo.

## 3. Consecuencias

**A favor.** Cada módulo pasa a ser una unidad desplegable con interfaz de red, y la
plataforma se puede levantar completa en otra máquina. Desaparece la asimetría de tener
un módulo que se controla distinto que los otros dos, y el BFF pasa a tener un solo
patrón de cliente.

**Restricción que queda declarada, no escondida.** `out_dir` es una ruta que el BFF y el
distribuidor comparten **por sistema de archivos**. Hoy es gratis (mismo host); al
containerizar es un volumen compartido. Es la misma condición que ya tienen los `runs_dir`
de los otros dos planos, así que no introduce deuda nueva — pero es la que hay que
resolver primero en el paso de Docker, y por eso se registra acá.

**Costo.** Hay dos caminos de control de ciclo de vida que mantener (HTTP y subproceso).
Se acepta a conciencia: es lo que permite que ADR-018 siga vigente y que nada de lo ya
escrito y verificado haya que reescribirlo.

## 4. Alcance diferido, con causa

**La containerización NO entra en esta decisión** y queda para el final del tramo:
Dockerfile del distribuidor, su entrada en `infra/platform/docker-compose.yml` y la
containerización del control-plane —que hoy tampoco corre en contenedor, pese a ser
servicio HTTP desde ADR-008—.

La causa es de encuadre, no de tiempo: **el despliegue no es un resultado del informe.**
Es evidencia de lo implementado y de que la plataforma se puede levantar en otro lado, y
como tal se reporta con su estado a la entrega. Esta decisión habilita ese paso; no lo
ejecuta.

> ✎ **2026-08-18 — precisión del usuario, y corrige una lectura posible del párrafo de
> arriba.** "No es un resultado del informe" **no significa "no se menciona"**. La
> containerización:
>
> 1. **Se va a hacer** — es compromiso, no posibilidad—, **después** de cerrar la
>    redacción del informe. No la bloquea, y por eso se difiere.
> 2. **Su razón de ser es la reproducibilidad de la plataforma**, no cerrar el informe.
> 3. **Su documentación operativa vive en los repositorios** (`infra/`, READMEs), no en la
>    tesis: el informe no es un manual de despliegue.
> 4. **Sí se puede hablar de ella en el informe**, y corresponde hacerlo — como
>    **trabajo declarado con su causa** en el cierre (§17.6/§18) y como parte del camino
>    de reproducibilidad (§19). Lo que no se puede es **escribirla en presente ni
>    presentarla como capacidad existente** mientras no exista.
>
> La distinción operativa, para quien redacte: *describir el compromiso y su fundamento* es
> correcto; *describir un despliegue que no corrió* es falso.

## 5. Alternativas consideradas

- **Containerizar tal cual, sin servicio.** Meter `eovrt-distribute` en la imagen de la
  consola y dejar el subproceso intacto. Más barato y no tocaba nada, pero conserva la
  co-ubicación obligatoria: el distribuidor nunca sería unidad propia, que es el problema
  a resolver.
- **Reemplazar el subproceso.** Más uniforme —un solo camino que mantener—, pero deroga
  ADR-018 a dos días de aceptada, obliga a reescribir spec 44 B4 y el runner, y a
  re-verificar la integración end-to-end en pleno camino crítico de redacción.
- **Contenedor propio sin HTTP** (worker de vida larga suscripto al bus). Da unidad propia
  sin inventar una API, pero el BFF pierde el control de ciclo de vida por corrida, que es
  exactamente lo que el runner usa hoy.

## 6. Interfaces

- **Spec 45** — recibe la sección de diseño del servicio (§9): contratos, módulos,
  ciclo de vida y criterios de terminado.
- **Spec 44** — el runner del BFF pasa a cliente HTTP; §B4 (subproceso) se mantiene como
  camino alternativo, no se reescribe.
- **ADR-008/009** — el servicio sigue sus mismas reglas: config por referencia o por
  payload, un solo run activo, artefactos por corrida en disco.
