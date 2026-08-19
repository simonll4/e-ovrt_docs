# ADR-020 — HTTP es el acople de la distribución; el subproceso baja a fallback operativo

> **DEROGA [ADR-018](adr-018-acople-bff-subproceso-distribucion.md).** El patrón
> "BFF-subproceso" deja de ser un patrón de acople de la plataforma. **El código no se
> borra**: el camino por subproceso sigue implementado y probado, pero pasa a ser una
> **bandera de contingencia operativa**, no una decisión de arquitectura — y por lo tanto
> **no se cuenta ni se describe como acople** en el informe.

- **Fecha:** 2026-08-18
- **Estado:** Aceptada (usuario, 2026-08-18)
- **Decisión que atiende:** tras [ADR-019](adr-019-servicio-http-distribucion.md) el
  distribuidor quedó con **dos mecanismos de control de ciclo de vida** para el mismo
  módulo. Mantener los dos como patrones obliga al informe a explicar una excepción que no
  compra nada: el módulo ya es un servicio, y ser servicio es lo que lo hace desplegable
  junto al resto.
- **Decisor:** usuario, 2026-08-18
- **Serie:** proyecto (`ADR-001…020`, tres dígitos). No confundir con la serie local del
  control-plane (`ADR-0001…`, cuatro dígitos).

---

## 1. Contexto

ADR-018 registró el acople por subproceso porque, en ese momento, **era la única forma
posible**: el distribuidor era una CLI sin interfaz de red. Era una decisión correcta para
el estado del código de entonces.

ADR-019 eliminó esa restricción: el módulo expone servicio HTTP propio (`:8082`), espejo
del control-plane. Pero lo hizo de forma deliberadamente conservadora —aditiva, con el
subproceso como default— para no derogar nada mientras el camino nuevo no estuviera
verificado. Ya lo está: equivalencia DBE (mismo `distribution_summary.json` por los dos
caminos) y cadena EBE en vivo con hardware real (`operacion/124`).

Lo que queda es una asimetría sin beneficio: **el mismo módulo, dos maneras de
controlarle el ciclo de vida.** Para el informe eso significa describir un tercer patrón
de acople cuya única razón de existir es histórica.

## 2. Decisión

1. **HTTP es el acople de la distribución.** El runner del BFF le habla por HTTP **por
   default**, igual que a los otros dos planos (ADR-008/009).
2. **El subproceso baja a fallback operativo.** Sigue implementado y probado, detrás de
   `EOVRT_CONSOLE_DISTRIBUTION_TRANSPORT=subprocess`. No se borra: es red de seguridad
   para escenarios sin el servicio arriba.
3. **La plataforma vuelve a tener DOS patrones de acople**, no tres:
   **(a)** HTTP config-driven — ahora en los **tres** módulos de la cadena (`:8080`,
   `:8081`, `:8082`), con la webconsole y el runner como clientes; **(b)** bus ZeroMQ
   PUB/SUB + msgpack (ADR-003), para el dato: detecciones `:5557` y alertas `:5558`.
4. **En el informe se describe un solo acople para la distribución.** El fallback por
   subproceso es un detalle de operación: no aparece en la descripción arquitectónica.

### Por qué esto no es esconder algo

Un informe describe **el sistema entregado**, no su historia de commits. La distinción que
gobierna acá: **un patrón de acople es una decisión de arquitectura; una bandera de
contingencia es un detalle de operación.** Mientras el subproceso fue el default, era lo
primero y había que contarlo. Dejando de serlo, pasa a ser lo segundo.

La condición que hace legítima esta decisión —y que es la razón de que el código cambie
junto con el texto— es que **el informe describa lo que el código hace**. Por eso esta ADR
no es sólo documental: invierte el default. Describir HTTP mientras el sistema arranca por
subproceso sería el defecto que este proyecto viene corrigiendo.

## 3. Consecuencias

**A favor.** El relato arquitectónico pierde su única excepción: tres servicios uniformes
y un bus. La respuesta a "¿cómo se acopla cada módulo?" pasa a ser una sola frase. Y el
despliegue conjunto —el objetivo que motivó ADR-019— deja de tener un caso especial.

**El costo, declarado.** Con HTTP por default, **la webconsole exige el servicio de
distribución arriba** cuando la distribución está habilitada; antes se bastaba a sí misma
criando el proceso. Es una dependencia operativa nueva, y en un escenario de demostración
es una cosa más que puede fallar. La mitigación es el fallback del punto 2, que existe
justamente para eso.

**Lo que NO cambia.** Los contratos (`control.alert.v1`, `control.notification.v1`,
`bus.envelope.v1`), el transporte del dato por el bus `:5558`, la entrega MQTT, los
artefactos por corrida y las cifras ya medidas (`operacion/118`: p95 64,534 ms, n=460).
Esta decisión toca **quién arranca y supervisa el proceso**, nada más.

## 4. Alternativas consideradas

- **Borrar el subproceso del código.** Más simple todavía, pero pierde el fallback: sin el
  servicio arriba no hay distribución posible, ni siquiera degradada. Se descartó por el
  costo operativo en la defensa, no por apego al código.
- **Dejar los dos como patrones (statu quo de ADR-019).** Verdadero y verificado, pero
  obliga al informe a explicar una excepción que no aporta a la tesis.
- **Cambiar sólo el informe, sin tocar el código.** Rechazada de plano: describiría un
  acople que no es el que corre. Es exactamente el defecto de propagación que el set
  documental viene corrigiendo.

## 5. Interfaces

- **ADR-018** — derogada. Su cuerpo se conserva como registro histórico, con banner.
- **ADR-019** — vigente; su §2 se enmienda: el default que ahí quedaba en subproceso pasa
  a HTTP por esta ADR.
- **Spec 45 §9.6** y **spec 44** *(✎ 2026-08-19: decía "spec 44 §B4", ancla heredada de
  ADR-019 — la sección B4 nunca se escribió; el acople del runner quedó anotado en el
  spec 44 §2)* — el cliente HTTP es el camino normal; el subproceso queda documentado
  como fallback.
- **Informe** — `GUIA-REDACTORES` §"trampas" vuelve a **dos** patrones de acople; el
  material de etapa 3 y 4 describe la distribución como el tercer servicio HTTP.
