# 125 — ADR-020: HTTP queda como acople de la distribución; el subproceso baja a fallback (2026-08-18)

- **Decisión:** [ADR-020](../decisiones/adr-020-http-como-unico-acople-de-distribucion.md)
  — **deroga [ADR-018](../decisiones/adr-018-acople-bff-subproceso-distribucion.md)**.
- **Antecedente inmediato:** [doc 124](124-servicio-http-distribucion.md) (ADR-019: el
  distribuidor sumó servicio HTTP, verificado en vivo con la OAK-D).
- **Estado: cerrado.** Decisión firmada, código invertido, documentación propagada, kit
  regenerado.

---

## 1. Qué se decidió, y por qué el mismo día

ADR-019 dejó al distribuidor con **dos mecanismos de control de ciclo de vida** para el
mismo módulo: el subproceso (default) y el servicio HTTP (opt-in). Fue deliberadamente
conservador — no derogaba nada mientras el camino nuevo no estuviera verificado.

Verificado el camino, la asimetría dejó de tener función. **ADR-020 invierte el default:**
HTTP es el acople; el subproceso queda como **fallback operativo** detrás de
`EOVRT_CONSOLE_DISTRIBUTION_TRANSPORT=subprocess`, implementado y probado pero **fuera del
relato arquitectónico**.

**Consecuencia para el informe: la plataforma tiene DOS patrones de acople, no tres.**
**(a)** HTTP config-driven en los **tres** módulos (`:8080` medios, `:8081` control,
`:8082` distribución), con la webconsole y el runner como clientes; **(b)** bus ZeroMQ
PUB/SUB + msgpack para el dato (detecciones `:5557`, alertas `:5558`).

## 2. La condición que hizo legítima la decisión

El pedido original admitía dos lecturas: *eliminar el patrón* o *no contarlo en el
informe*. **No eran separables.** Describir un solo acople HTTP mientras el sistema
entregado arrancaba por subproceso habría sido documentar un sistema que no existe —
exactamente el defecto que este set documental viene corrigiendo.

Por eso ADR-020 **no es sólo documental**: cambia el default del código. La regla que
gobernó la decisión: **el informe describe lo que el código hace.**

La distinción que la sostiene: **un patrón de acople es una decisión de arquitectura; una
bandera de contingencia es un detalle de operación.** Mientras el subproceso fue el
default, era lo primero y había que contarlo. Dejando de serlo, pasa a ser lo segundo.

## 3. El costo, declarado

Con HTTP por default, **la webconsole exige el servicio de distribución arriba** cuando la
distribución está habilitada; antes se bastaba a sí misma criando el proceso. Es una
dependencia operativa nueva y, en un escenario de demostración, una cosa más que puede
fallar. La mitigación es el fallback, que existe justamente para eso.

Se descartó explícitamente **borrar** el subproceso del código: habría dejado el sistema
sin ninguna vía degradada.

## 4. El número de patrones cambió tres veces en cuatro días

Vale registrarlo, porque cualquier documento sin enmienda del 2026-08-18 describe un
estado intermedio:

| Fecha | Patrones | Causa |
|---|---|---|
| hasta 08-14 | **dos** | HTTP config-driven (dos planos) + bus ZeroMQ |
| 08-15 | **tres** | ADR-018 registra BFF-subproceso |
| 08-17/18 | tres | ADR-019 suma servicio HTTP al distribuidor *(un borrador llegó a decir "cuatro"; se corrigió antes de llegar al informe)* |
| **08-18** | **dos** | **ADR-020**: el subproceso baja a fallback y deja de ser patrón |

## 5. Lo que NO cambió

Contratos (`control.alert.v1`, `control.notification.v1`, `bus.envelope.v1`), transporte
del dato por el bus `:5558`, entrega MQTT, artefactos por corrida, y las cifras medidas
(`operacion/118`: p95 64,534 ms, n=460). Esta decisión toca **quién arranca y supervisa el
proceso**, nada más.

## 6. Propagación ejecutada

- **Código:** default invertido en el runner del BFF y en el preflight (sondeo `/healthz`
  por default; chequeo de binario sólo en el fallback), con los tests de ambos caminos
  adaptados y prueba negativa.
- **Decisiones:** ADR-020 nueva · ADR-018 con banner de derogación (cuerpo conservado) ·
  ADR-019 §2 enmendada · `estado-de-implementacion-adrs` (filas 018/019 enmendadas + 020)
  · `decisiones/README`.
- **Informe:** `GUIA-REDACTORES` trampa 7 reescrita (vuelve a **dos** patrones, con la
  lista explícita de qué **no** escribir) · glosario 13 · anexo `92` §3 y tabla · redlines
  `93` (R-17 y spec de FIG-A) · `94` (Tabla 61 y nota de figura) · ficha
  `04-etapa-4` (AJ-4.04) · borrador `17-4` (FIG-A y nota de despliegue **retirada**) ·
  `gobierno/99` (tabla de ADRs).
- **Kit:** `generar_project_kit.py` con el bloque de acoples reescrito, guard del test
  actualizado con prueba negativa, y los 8 archivos regenerados.
- **Índices:** `00-indice.md`, `CRONOLOGIA.md`, `CLAUDE.md` del workspace.

## 7. Nota de alcance: la containerización (precisión del usuario, 2026-08-18)

Sigue **diferida con causa** y se hará **después** de cerrar la redacción del informe.
Tres precisiones que corrigen una lectura posible de "no es un resultado del informe":

1. **No es opcional:** es trabajo comprometido, no una posibilidad.
2. **Su razón de ser es la reproducibilidad** —que un tercero pueda levantar la
   plataforma en otra máquina—, no cerrar el capítulo. Por eso no lo bloquea.
3. **Su documentación operativa vive en los repositorios** (`infra/`, READMEs), no en la
   tesis: el informe no es un manual de despliegue.

**Y sí se habla de ella en el informe**, como trabajo declarado con su fundamento, en el
cierre (§17.6/§18) y en el anexo de reproducibilidad (§19). La regla para quien redacte:
*describir el compromiso y su fundamento es correcto; describir un despliegue que no
corrió es falso.* Propagado a `ADR-019` §4, ficha `06-etapa-6` (AJ-6.04 y §3), contexto
base del kit y `GUIA-REDACTORES`.
