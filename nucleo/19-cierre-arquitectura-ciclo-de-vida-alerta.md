# 19 — Cierre de la arquitectura: el ciclo de vida de la alerta y su distribución

> ✎ **2026-08-18 — banner de vigencia.** Este documento fotografía el estado al
> **2026-08-10**, cuando el cuarto eslabón estaba *diseñado y no construido*. Eso quedó
> superado dos veces: el módulo `e-ovrt_alert-distribution` está **implementado y
> verificado** desde el 2026-08-12/14 (docs `operacion/114` — relevamiento — y `118` —
> campaña de distribución, p95 64,534 ms n=460), y desde el 2026-08-17/18 **también
> expone servicio HTTP propio** (`eovrt-distribute serve`, `:8082`, ADR-019, doc
> `operacion/124`), quedando como unidad desplegable. ✎ Más tarde ese mismo día **ADR-020** derogó a
> ADR-018: **HTTP es el acople** (default del runner) y el subproceso bajó a fallback
> operativo, así que los patrones de acople de la plataforma son **dos**, no tres. **El cierre conceptual de este documento
> sigue siendo válido** — el ciclo de vida y los contratos que describe son los que el
> código implementa; lo que cambió es que ya no son promesa sino código verificado.

- **Fecha de relevamiento:** 2026-08-10
- **Qué cierra:** la cadena de la plataforma termina en una alerta confirmada. Este
  documento responde **dónde se gestiona el ciclo de vida completo de esa alerta y hacia
  dónde se distribuye** — la pregunta que hasta hoy contestaban cinco documentos distintos
  y ninguno entero.
- **Método:** consolida `historicos/06` (diseño completo), ADR-005, ADR-011, `specs/45` e
  `informe/ajustes/material-etapa-3/92b`. **No los reemplaza**: los cita. Lo que agrega es
  el estado real del código, verificado contra los repos el 2026-08-10.
- **Regla de este documento:** no publica ninguna cifra de resultado.

---

## 1. Por qué este documento existe

La plataforma implementa y mide tres eslabones de su cadena. El cuarto estaba solo
diseñado, y esa asimetría dejaba dos huecos:

- Un lector llega al final del sistema y encuentra alertas confirmadas que **no van a
  ningún lado**.
- ADR-011 sacó el cooldown del motor a propósito, asignándolo al módulo de distribución.
  Sin ese módulo descrito en un solo lugar, **la política de notificación queda sin
  domicilio** y parece un olvido en vez de una decisión.

ADR-016 (2026-08-10) autoriza construir el módulo. Pero **el cierre arquitectónico no
depende de que el código aterrice**: depende de que esté dicho dónde vive cada cosa. Eso
es lo que hace este documento.

## 2. La cadena y sus cuatro fronteras

```
   ┌──────────────┐   media.detection.v1   ┌───────────────┐   control.alert.v1   ┌──────────────────┐
   │ media-plane  │ ─────────────────────► │ control-plane │ ───────────────────► │  distribución    │ ──► canal
   │  percepción  │                        │   patrones    │                      │  notificación    │     (MQTT)
   └──────────────┘                        └───────────────┘                      └──────────────────┘
        detección          →      patrón        →       alerta       →      notificación   →   entrega
```

Cuatro fronteras, y cada una es una decisión, no un accidente de implementación:

| Frontera | Qué separa | Dónde está decidido |
|---|---|---|
| **detección → patrón** | Ver algo ≠ que sea una condición de riesgo. El motor no ve imágenes | ADR-001, `18` §1 |
| **patrón → alerta** | Una condición instantánea ≠ una alerta. Hace falta persistencia temporal confirmada | `18` §1, `specs/41` |
| **alerta → notificación** | Una alerta confirmada ≠ algo que amerite molestar a un humano | **ADR-011** |
| **notificación → entrega** | Decidir notificar ≠ haber entregado. El intento y su resultado se registran aparte | `historicos/06` §2, ADR-005 |

**La tercera es la que más se malinterpreta**, y es el corazón de este documento.

## 3. Qué vive de cada lado de la frontera alerta↔notificación

ADR-011 la fijó así, y es una decisión con fundamento medible:

**Se queda en el motor — absorbe *ruido perceptual*:**
umbrales de evidencia, región esperada, matching EPP↔persona 1:1, **memoria de cobertura**,
**histéresis confirm/resolve**, expiración de sujetos ausentes. Todo esto compensa que el
detector parpadee o que haya una oclusión breve. Es semántica del patrón.

**Va a la distribución — absorbe *política de consumo*:**
**cooldown de re-notificación**, supresión por ventana, agrupación, rate-limiting. Esto
decide **cuántas veces molestar a un consumidor con una condición ya avisada**. Es política
del tramo de entrega, no del fenómeno observado.

**El criterio que separa las dos listas:** si el ajuste corrige algo que el detector hizo
mal, va en el motor. Si el ajuste corrige algo que el *destinatario* no quiere recibir, va
en la distribución.

**Por qué importa para las métricas.** El motor emite un `AlertEvent` en **cada**
confirmación, sin supresión: `alerts.jsonl` es el registro fiel de la dinámica del patrón.
Si el motor suprimiera, la tasa de re-alertas —que es señal de estabilidad de la
percepción— quedaría oculta. Por eso el evaluador cuenta las `re_alerts` y **no las
penaliza como falsos positivos**.

**Consecuencia registrada:** el parámetro `realert_cooldown_ms/frames` existe en el motor
(heredado de la rama `mati`) pero los pattern sets de plataforma lo dejan **sin
configurar**. No es código muerto por descuido: es capacidad deliberadamente no usada.

## 4. El ciclo de vida de una alerta, objeto por objeto

```
AlertEvent  ──►  NotificationEnvelope  ──►  [política]  ──►  [ledger]  ──►  canal  ──►  DeliveryRecord
control.alert.v1   control.notification.v1                                              control.delivery.v1
```

**1. `AlertEvent` (`control.alert.v1`)** — lo que el motor emite al confirmar. Campos
reales hoy: `control_run_id`, `media_run_id`, `unit_id`, `source_id`, `alert_id`,
`pattern_id`, `condition_id`, `subject_key`, `severity`, `state="open"`, `evidence`,
`frame_index`, `timestamp_ms`, más instrumentación (`alert_registered_ms`,
`first_evidence_ms`, `first_evidence_unit_id`, `first_evidence_frame_index`) y
`experiment_id`. El `alert_id` es determinista —`uuid5` sobre la clave de la corrida y el
sujeto—, así que reprocesar produce el mismo id.

**2. `NotificationEnvelope` (`control.notification.v1`)** — evento **derivado**, con
contexto mínimo: no reemplaza a la alerta interna, la referencia. Su `notification_id` es
determinista a partir de `alert_id`, que es lo que hace posible la idempotencia aguas
abajo.

**3. Política de notificación** — decide si esta alerta se convierte en aviso.
`notification_policy.cooldown_ms` (valor inicial declarado 30 s, calibrable) con clave
`(condition_id, source_id)` por default. La clave es sobre condición-y-cámara, no sobre
sujeto, porque para notificación asistiva lo relevante es *"esta condición en esta cámara ya
fue avisada"*. Una alerta suprimida **no desaparece**: genera
`DeliveryRecord(outcome="suppressed_cooldown")`, contado en el summary.

**4. Ledger de idempotencia** — clave `(notification_id, channel)`, respaldado por los
`DeliveryRecord` con outcome `delivered` en `notifications.jsonl` (append-only). Una
re-ejecución es segura: produce `skipped_duplicate`.

**Las dos capas no son redundantes**, y esta es la distinción que más se confunde:

> **el ledger deduplica *exactos*** — la misma alerta procesada dos veces;
> **el cooldown suprime *semánticos*** — alertas **distintas** de la misma condición y
> fuente, demasiado seguidas.

Quitar cualquiera de las dos rompe algo diferente.

**5. Retry** — `max_attempts` (default 3) con espera fija corta. Agotado, `outcome:
dead_letter` más una línea en `dead_letter.jsonl`. Nada más: no hay backoff exponencial ni
cola persistente, y es deliberado.

**6. `DeliveryRecord` (`control.delivery.v1`)** — separa **alerta confirmada**, **intento**
y **resultado**, sin tocar la semántica del evento interno. Lleva `channel`, `mode`
(`dry_run`|`live`), `attempt`, `outcome`, `error`, `talert_notification_ms`, `attempted_at`
y `delivered_at`.

**Salidas por corrida:** `notifications.jsonl`, `dead_letter.jsonl` y
`distribution_summary.json` (conteos por outcome + agregados de `t_alert-notification`).

## 5. Por qué MQTT, y por qué es un ejemplo

MQTT es el canal **elegido para demostrar el mecanismo**, no una integración con un sistema
real de obra. El fundamento (doc 07 D5):

- **Peso mínimo** — un Mosquitto en el compose, sin infraestructura adicional.
- **Estándar de integración IoT** — es la respuesta defendible a "¿cómo se conecta esto con
  el mundo?".
- **Medición limpia** — `t_alert-notification` sin la variabilidad de una API externa. Un
  canal tipo Telegram habría medido la latencia de un servicio ajeno al sistema.

**Y una consecuencia que no es opcional:** MQTT QoS 1 puede **duplicar entregas**. Por eso
el ledger no es un lujo de diseño — es requisito del canal elegido. Lo mismo valdría para
cualquier broker at-least-once.

**Qué queda explícitamente afuera (E-06):** canales adicionales y dashboard dedicado. La
vista de alertas va en la **webconsole existente**. ADR-016 ratifica esta exclusión.

## 6. Estado real, sin maquillaje

**Construido:** la **frontera de salida** del control-plane —
`transport/alert_bus.py`, publisher `control.alert.v1` sobre XPUB, persiste-primero,
**apagado por default**. Es lo único de este tramo que existe como código en producción.

**No construido:** todo el resto. El repo hermano `e-ovrt_alert-distribution/` existe desde
el 2026-07-18 y al 2026-08-10 está así:

- **cero commits**
- `src/eovrt_distribution/` son cuatro paquetes **vacíos** (`__init__.py` en la raíz,
  `contracts/`, `channels/`, `transport/`)
- `tests/` tiene únicamente `conftest.py`
- lo real es el spec de diseño en su `docs/superpowers/`

**Estatuto:** ADR-016 (2026-08-10) lo declara **trabajo comprometido** con el recorte de
ADR-005. Entre el 2026-08-05 y esa fecha estuvo declarado como exclusión cerrada por
ADR-015 §2c, cláusula hoy derogada. **Ninguna cifra del informe sale de este módulo**, y su
implementación **no bloquea la redacción**: si no llega a tiempo, se declara como estaba.

### 6.1 Un desfase que quien implemente va a chocar

El diseño de `historicos/06` §6.1 asume que el `NotificationEnvelope` se arma con un
**`confirmed_at_ms`** tomado de la alerta. **`control.alert.v1` no tiene ese campo.** Lo que
sí tiene es `timestamp_ms` (del evento que confirmó), `alert_registered_ms` y
`first_evidence_ms`. Al construir el envelope hay que decidir cuál de los tres es el
instante de confirmación —y esa decisión afecta directamente a `t_alert-notification`, que
es la métrica del tramo. Queda anotado acá para que se resuelva con criterio y no por
descarte.

## 7. Qué leer después

| Pregunta | Documento |
|---|---|
| El diseño completo del módulo (ledger, retry, dead-letter, canales, paridad DBE/EBE) | `historicos/06` — 20 secciones |
| Por qué el cooldown no está en el motor | **ADR-011** |
| Por qué MQTT y por qué repo propio | **ADR-005** |
| Por qué se implementa después de haberse declarado cerrado | **ADR-016** |
| Cómo implementarlo (orden y criterios de terminado) | `specs/45-distribucion-alertas.md` |
| La versión para el informe | `informe/ajustes/material-etapa-3/92b-concrecion-distribucion-alertas.md` |
| Quién emite las alertas y con qué contrato | `18` §4 |

## Referencias

`historicos/06` (diseño original; su §4 sobre ubicación quedó superado por ADR-005) · ADR-005 ·
**ADR-011** · ADR-015 §2c (derogada) · **ADR-016** · `specs/45` · `informe/92b` ·
`nucleo/10` ítem 5 y E-06 · `18` §6 (la frontera de salida) · doc 07 D5/H11.
