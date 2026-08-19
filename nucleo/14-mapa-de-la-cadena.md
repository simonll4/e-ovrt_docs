# 14 — Mapa de la cadena: quién habla con quién

- **Fecha de relevamiento:** 2026-08-10
- **Qué es:** el prólogo de la serie de relevamientos por servicio (`14`–`19`). Da la vista
  de conjunto; el detalle de cada pieza está en su documento.
- **Regla de la serie:** **ningún relevamiento publica cifras de resultado.** Las cifras
  salen de los cuatro índices de `e-ovrt_experimental-setup/results/`; la historia de
  capacidades medidas, de `operacion/97`. Acá está **qué es cada pieza y cómo funciona**.

---

## 1. El workspace no es un repo

`/home/simonll4/projects` **no** es un repositorio: es un directorio de trabajo que
contiene **cinco repos git hermanos e independientes**, cada uno con su propio historial y
su propio remoto. Se commitean por separado.

Que sean hermanos **en disco** no es cosmético: varias configuraciones usan rutas relativas
cross-repo (`../e-ovrt_datasets/...`), así que mover un repo rompe al vecino.

## 2. La cadena

```
                        ┌──────────────────────────────┐
                        │   experimental-setup   (15)  │   consola + runner + catálogos
                        │   orquesta por HTTP los dos  │   y LOS ÍNDICES DE RESULTADOS
                        │   planos; nunca toca el bus  │
                        └───────┬──────────────┬───────┘
                                │ HTTP :8080   │ HTTP :8081
> ✎ **2026-08-18 — la caja "NO CONSTRUIDA" del diagrama quedó superada DOS veces.** El
> módulo de distribución está **implementado y verificado** desde el 2026-08-12/14
> (docs `operacion/114`/`118`: MQTT QoS 1, ledger de idempotencia, p95 64,534 ms n=460)
> y desde el 2026-08-17/18 **también expone servicio HTTP propio** (`:8082`, ADR-019,
> doc `operacion/124`) — ~~el subproceso del runner sigue siendo el default (ADR-018)~~
> ✎ 2026-08-19: **ADR-020 (2026-08-18) derogó a ADR-018 — HTTP es el default del
> runner** y el subproceso quedó como fallback operativo
> (`EOVRT_CONSOLE_DISTRIBUTION_TRANSPORT=subprocess`).
> El diagrama se conserva como cuerpo histórico por convención del set.

                                ▼              ▼
   ┌────────────┐  imágenes  ┌──────────────┐        ┌───────────────┐  control.alert.v1  ┌──────────────┐
   │ datasets   │  y video   │ media-plane  │ media. │ control-plane │ ─────────────────► │ distribución │
   │   (16)     │ ─────────► │    (17)      │ detec- │     (18)      │                    │     (19)     │
   │ vocabulario│            │  percepción  │ tion.v1│   patrones    │                    │ NO CONSTRUIDA│
   │ + bancos   │            │   OVD :8080  │ ─────► │   alertas     │                    │              │
   └────────────┘            └──────────────┘        └───────────────┘                    └──────────────┘

        insumos          →       detección       →        patrón → alerta      →        notificación → entrega
```

| # | Repo | Qué es | Documento |
|---|---|---|---|
| 1 | `e-ovrt_experimental-setup` | El centro operativo: consola, runner, catálogos y resultados | **`15`** |
| 2 | `e-ovrt_datasets` | Los insumos: vocabulario canónico, bancos de imágenes y de video | **`16`** |
| 3 | `e-ovrt_media-plane` | Percepción OVD, servicio `:8080` | **`17`** |
| 4 | `e-ovrt_control-plane` | Motor de patrones de riesgo, servicio `:8081` | **`18`** |
| 5 | `e-ovrt_alert-distribution` | Ciclo de vida y distribución de la alerta — ~~diseñado, no implementado~~ ✎ 2026-08-18: **implementado y verificado** (docs 114/118); ✎ 2026-08-19: **servicio HTTP `:8082`** (ADR-019, doc 124) como **acople default del runner** (ADR-020, deroga ADR-018); CLI para el camino offline; subproceso = fallback operativo | **`19`** |

Y un sexto repo que no es software: **`docs/`**, el set documental. Es un repo git propio.
~~local y sin remoto, por decisión del proyecto~~ ✎ 2026-08-18: desde el 2026-08-10, cuando
el equipo empezó a necesitar acceso, tiene remote propio (`e-ovrt_docs`, rama `main`).

## 3. Los dos caminos de acople

Media-plane y control-plane se acoplan de dos maneras según el escenario de despliegue.
**No son alternativas de implementación: son dos escenarios distintos, y los dos se
ejercieron.**

**DBE (offline, un host) — acople por archivo.** El media-plane escribe
`runs/<id>/detections.jsonl`; el control-plane lo relee. El repositorio es la fuente de
verdad, y **el pipeline es determinista** (verificado: re-inferir da detecciones idénticas
bit a bit).

**EBE (live, dos nodos) — acople por bus.** ZeroMQ PUB/SUB con msgpack y envelope
`bus.envelope.v1` (ADR-003). La corrida es **1:1** y cierra con
`run.lifecycle.v1/run_finished`.

> **El orden de disparo en live no es negociable.** PUB/SUB pierde todo lo publicado antes
> de que el consumidor se suscriba. Por eso va **primero** `POST :8081/api/runs` con
> `mode: live` —cuyo 201 implica que ya está suscripto— y **después** `POST :8080/api/runs`
> con `bus.enabled: true`. Los huecos de `seq` se cuentan como `bus_dropped_events` y
> **degradan la corrida; nunca se silencian**.

**La distribución cuelga del mismo esquema** *(✎ 2026-08-19)*: las alertas confirmadas
viajan por el **bus de alertas `:5558`** (control → distribución), con la misma regla de
suscripción previa que el bus de detecciones; y el acople del runner con el distribuidor
es **HTTP `:8082`** (ADR-019/020), igual que con los otros dos servicios.

**El JSONL es la verdad en los dos casos:** toda corrida live es re-evaluable offline y
produce artefactos idénticos. Eso está verificado, y es lo que hace auditable al camino en
vivo.

## 4. Las cuatro fronteras

La cadena tiene cuatro cortes, y cada uno es una decisión registrada:

| Frontera | Qué separa |
|---|---|
| detección → patrón | Ver algo no es que sea riesgo. El motor no ve imágenes |
| patrón → alerta | Una condición instantánea no es una alerta: hace falta persistencia confirmada |
| alerta → notificación | Una alerta confirmada no es algo que amerite molestar a un humano (ADR-011) |
| notificación → entrega | Decidir notificar no es haber entregado |

Las tres primeras están implementadas y medidas. **La cuarta está diseñada y no
construida** — su domicilio conceptual completo está en `19`, que es lo que cierra la
arquitectura con independencia de que el código exista.

> ✎ **2026-08-18:** el párrafo de arriba quedó superado — **las cuatro fronteras están
> implementadas y medidas**. La cuarta (notificación → entrega) se construyó y verificó
> el 2026-08-12/14 (docs 114/118) y desde ADR-019 el módulo además corre como servicio
> HTTP (doc 124). El `19` sigue siendo el domicilio conceptual; ahora con código real
> detrás.

## 5. El acople duro: el vocabulario canónico

`datasets` y `media-plane` comparten el **vocabulario canónico v2**: `person`, `helmet`,
`vest`, `bare_head` (más los atributos `has_helmet` / `has_vest` en la vista BENCH).

**Cambiar un nombre de clase o una condición obliga a mover los dos repos a la vez.** Es la
dependencia menos visible del proyecto y la que más fácil se rompe.

## 6. Cómo leer esta serie

1. **Este documento**, para la vista de conjunto.
2. **`15`** si vas a operar el sistema — desde ahí se dispara todo.
3. **`16` → `17` → `18`** para seguir el dato de punta a punta.
4. **`19`** para entender dónde termina la cadena y por qué esa parte no está construida.

**Para otras preguntas, otros documentos:**

| Pregunta | Dónde |
|---|---|
| ¿Cuánto dio? | Los cuatro índices de `e-ovrt_experimental-setup/results/` |
| ¿Qué capacidades se construyeron y con qué evidencia? | `operacion/97` |
| ¿Por qué se decidió así? | `decisiones/` + `decisiones/estado-de-implementacion-adrs.md` |
| ¿Qué está fuera de alcance? | `nucleo/10` |
| ¿Qué significa esta sigla? | `../13-glosario-y-convenciones-de-lectura.md` |

## 7. Dos convenciones que se confunden

**Las dos series de ADR.** `ADR-001…018` (tres dígitos) son del **proyecto**, en
`docs/decisiones/`. `ADR-0001…0013` (cuatro dígitos) son de la **serie local del
control-plane**, en `e-ovrt_control-plane/docs/decisions/`. **Al citar, decir la serie.**

**Los documentos históricos mandan por su banner, no por su cuerpo.** Un doc con banner ✎
o ⚠️ al tope se lee desde ahí: el banner dice qué quedó superado y qué conserva vigencia.
`historicos/01` y `historicos/11` son los relevamientos históricos que esta serie reemplaza —
siguen en su lugar con su número, porque moverlos rompería miles de referencias.

## Referencias

`15`, `16`, `17`, `18`, `19` (los cinco relevamientos) · `historicos/01` y `historicos/11` (históricos,
reemplazados) · `03-spec-plataforma-dos-caminos.md` · `05-integracion-media-control-bus-eventos.md` ·
`10` (alcance y exclusiones) · `13` (glosario) · `operacion/97` (capacidades) ·
`operacion/37` y `38` (bus y servicio del control-plane).
