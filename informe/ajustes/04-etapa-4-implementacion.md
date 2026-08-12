# Etapa 4 — §17.4 Implementación del prototipo experimental

> **Estado (2026-08-10):** la sección **está vacía**. En el informe v1.1 dice
> literalmente `[Agregado futuro correspondiente a la Etapa 4]`. Esto **no es un frente
> de correcciones: es redacción desde cero.**
>
> **La buena noticia:** los insumos están completos y verificados. `92` trae la
> concreción técnica contrastada contra código, `94` §7–§9 trae prosa ya redactada,
> `operacion/97` trae el relevamiento de plataforma con la suite de tests en verde, y las
> seis specs de la serie 40 son la especificación por módulo. **No hay que investigar
> nada nuevo para escribir el §17.4.**

| Dónde | Qué |
|---|---|
| Texto actual | `entregable/96e` — placeholder vacío |
| Concreción técnica verificada contra código | `material-etapa-3/92` (§1 correspondencia · §2 el evento · §3 las APIs · §5 contratos del control · §6 config efectiva · §8 artefactos · §9 puntos de extensión) |
| Prosa ya redactada | `material-etapa-3/94` §7 (verificación), §8 (no implementado), §9 (extensibilidad) |
| Especificación por módulo | `specs/40` (integrador) · `41` control-plane · `42` media-plane · `43` clip bench · `44` experimental-setup · `45` distribución |
| Relevamientos vigentes por servicio (✎ 2026-08-10) | **`nucleo/14`** (mapa de la cadena) · `15` setup · `16` datasets · `17` media · `18` control · **`19` el ciclo de vida de la alerta** — relevados contra git y código, sin cifras |
| Estado real de la plataforma | `operacion/97-relevamiento-plataforma-2026-08-05.md` |
| Decisiones a citar | `decisiones/` — ADR-001…016 (+ la serie propia del control-plane, 4 dígitos) |

---

## 1. Tablero de contenidos a escribir

| ID | Tipo | Pri | Qué tiene que decir el §17.4 | Insumo |
|---|---|---|---|---|
| **AJ-4.01** | CONCRETA | 🟠 | **Las piezas de software que existen**: tres hoy — cuatro solo si la distribución llega con código a la entrega (ADR-016). | `GUIA-REDACTORES` §1 · CLAUDE.md |
| **AJ-4.02** | CONCRETA | 🟠 | La **correspondencia diseño → artefacto real**: es la respuesta directa al pedido del tutor técnico. | `92` §1 · `94` §1.2 |
| **AJ-4.03** | CONCRETA | 🟠 | Los **contratos de datos reales**, con esquema y serialización. | `92` §2 y §5 · `94` §1.3–1.4 |
| **AJ-4.04** | CONCRETA | 🟠 | Los dos planos son **servicios HTTP config-driven**, no CLIs. | `92` §3 · `94` §1.5 · ADR-008/009 |
| **AJ-4.05** | CONCRETA | 🟠 | Los **dos caminos de acople** (DBE por archivo · EBE por bus), con el orden de disparo y sus trampas. | `94` §3 · ADR-003/007 · `operacion/37`, `38` |
| **AJ-4.06** | EVIDENCIA | 🟡 | **El JSONL es la verdad en los dos caminos**: toda corrida live es re-evaluable offline. | `operacion/37`, `109` |
| **AJ-4.07** | CONCRETA | 🟡 | La **configuración efectiva** y el modelo desplegado. | `92` §6 |
| **AJ-4.08** | CONCRETA | 🟡 | **Artefactos y layout por experimento**. | `92` §8 · ADR-004/014/006 |
| **AJ-4.09** | CONCRETA | 🟡 | La **construcción del GT temporal** y su trampa de método. | `specs/43` · `operacion/80` · `99` §2.3 |
| **AJ-4.10** | EVIDENCIA | 🟠 | **El sistema es ejecutable y verificable**, con el número de la suite. | `94` §7 · `operacion/97` |
| **AJ-4.11** | EVIDENCIA | 🟠 | **Lo que NO se implementó**, cada ítem con su estatuto exacto. | `94` §8 · ADR-005/015/**016** |
| **AJ-4.12** | CONCRETA | 🟠 | **Extensibilidad**: los puntos de extensión, y cuánto costó medido. | `92` §9 · `94` §9 |

---

## 2. Los contenidos, desarrollados

### AJ-4.01 · 🟠 — tres piezas de software, no cuatro

- **`e-ovrt_media-plane`** — pipeline de inferencia OVD. Desde Fase 1 es un **servicio**
  FastAPI (HTTP/WS) config-driven en `:8080`; el modelo se carga una vez al arranque y una
  corrida se dispara con `POST /api/runs` (una activa a la vez).
- **`e-ovrt_control-plane`** — motor de patrones de riesgo CR-01/CR-02 sobre eventos
  `media.detection.v1`; también servicio HTTP en `:8081`.
- **`e-ovrt_experimental-setup`** — **no es un plano**: catálogos de experimento
  (`prompts/`, `experiments/`), el runner reproducible y la **webconsole** (React +
  FastAPI BFF), cliente HTTP de ambos planos.

**El cuarto repositorio (`e-ovrt_alert-distribution`) existe en disco pero hoy no es una
cuarta pieza:** es un esqueleto de paquete sin lógica ni commits. ✎ 2026-08-10, ADR-016:
su implementación pasó a ser **trabajo comprometido** antes de la defensa — si al momento
de la entrega tiene código verificado, esta sección pasa a describir **cuatro** piezas;
si no, se reporta el estado tal cual (ver `AJ-4.11`).

A esto se suma **`e-ovrt_datasets`**, que no es plataforma sino la cadena de adquisición,
validación y conversión que produce los datasets y el benchmark de imágenes.

---

### AJ-4.02 · 🟠 — la correspondencia diseño → artefacto

**Es el corazón del §17.4 y responde literalmente lo que pidió el tutor técnico**: cada
contrato preliminar declarado en Etapa 3 contra el artefacto que existe hoy en el
código. La tabla está armada en `92` §1 y con prosa de apertura en `94` §1.2.

Sin esta tabla, el §17.4 es una descripción; con ella, es una verificación.

---

### AJ-4.03 · 🟠 — los contratos de datos reales

Los que hay que documentar con esquema y serialización:

| Contrato | Qué transporta |
|---|---|
| `media.detection.v1` | la detección por frame — el evento que consume el plano de control |
| `bus.envelope.v1` | el envelope del bus (msgpack) con `seq` para detectar huecos |
| `run.lifecycle.v1` | ciclo de vida de la corrida; cierra con `run_finished` |
| `control.alert.v1` | la alerta confirmada que sale del motor (publisher desactivado por defecto) |
| `pattern_events` | la traza del motor: `candidate` → `confirmed` → `resolved`, con `confirm_after_ms` |

El material está en `92` §2 (el evento de detección) y §5 (los otros dos eventos del
plano de control), con las referencias a archivo y línea. La **máquina de estados del
motor** es la figura **FIG-E** del inventario de cierre.

---

### AJ-4.04 · 🟠 — dos servicios HTTP config-driven

Hay que decir explícitamente que **ninguno de los dos planos es una CLI** (la CLI del
control-plane se conserva solo para el camino offline), que **no hay paths ni umbrales
hardcodeados** —todo es YAML— y que la webconsole y el runner son **clientes HTTP de
ambos planos y nunca consumen el bus** (ADR-008/009). Ese detalle importa: es lo que hace
que la consola siga funcionando en el despliegue de dos nodos.

Material: `92` §3 (las APIs, con el contrato de disparo de corrida) y `94` §1.5.

---

### AJ-4.05 · 🟠 — los dos caminos de acople, y sus trampas

- **DBE (offline), acople por archivo:** el media-plane escribe
  `runs/<id>/detections.jsonl` y el control-plane lo relee. El repositorio es la fuente
  de verdad.
- **EBE (live), acople por bus:** **ZeroMQ PUB/SUB + msgpack** (ADR-003), envelope
  `bus.envelope.v1`. La corrida es **1:1** (ADR-007) y cierra con `run_finished`.

**Dos trampas que el capítulo tiene que declarar, porque son decisiones de diseño y no
accidentes:**

1. **El orden de disparo no es arbitrario.** PUB/SUB **pierde todo lo publicado antes de
   la suscripción**, así que primero se dispara el control-plane (`POST :8081/api/runs`
   con `mode: live`, cuyo 201 implica que ya está suscripto) y **después** el media-plane
   con `bus.enabled: true`. Los huecos de `seq` se cuentan como `bus_dropped_events` y
   **degradan la corrida; nunca se silencian**.
2. **La parada cooperativa de las fuentes de red.** Cerrar un socket ZeroMQ desde un hilo
   distinto del que lo creó, mientras otro está en `recv_multipart`, hace que libzmq
   aborte el proceso. Por eso las fuentes de red exponen `request_stop()`. Es el tipo de
   restricción de implementación que un capítulo de Etapa 4 debería registrar.

El despliegue EBE dockerizado en dos nodos (`infra/twonode/`) está verificado y es parte
de esta sección.

---

### AJ-4.06 · 🟡 — el JSONL es la verdad en los dos caminos

**Toda corrida live es re-evaluable offline y produce artefactos idénticos** (verificado,
incluido el determinismo del camino DBE). Es la propiedad que sostiene la
reproducibilidad de todo el capítulo de resultados: nada de lo que se reporta depende de
haber estado presente cuando la cámara filmaba.

---

### AJ-4.07 · 🟡 — la configuración efectiva

Los **valores que el capítulo de diseño nunca da** y el de implementación sí debe
(`92` §6): el pattern set oficial **`cr01_cr02_v2`** (CR-01 `high`/4000 ms, CR-02
`medium`/7000 ms), los prompt sets congelados, y el modelo desplegado — **`grounding-dino/gdino-tiny-560`**,
la variante `image_size: 560` seleccionada como campeón.

---

### AJ-4.08 · 🟡 — artefactos y layout por experimento

Qué produce una corrida y dónde queda: el layout por experimento (ADR-014), la corrida
paraguas y el `experiment_id` (ADR-004), el `report.json` consolidado con
**estados de aplicabilidad** (ADR-006) y el `effective_config`. Material: `92` §8.

---

### AJ-4.09 · 🟡 — la construcción del GT temporal, y su trampa

La cadena del clip bench: **split → derive → validate → promote → aggregate** (spec 43).

**La trampa que hay que declarar** porque cambia el resultado en silencio: el export de
CVAT es a nivel **PROYECTO**, y sin `split_cvat_project.py` **el GT sale negativo sin
avisar**. El lote de internet llegó a nivel **TASK**, donde aplicar el split habría sido
el error simétrico. La lección de método —verificar `meta/task` vs `meta/project` antes
de decidir el primer paso— es material del informe, no solo del runbook.

Y la regla de fuente de verdad: **las anotaciones del repo mandan sobre CVAT**, con un
guard (`apply_attribute_corrections.py --check`) que falla si una corrección firmada
falta en el GT.

---

### AJ-4.10 · 🟠 — el sistema es ejecutable y verificable

La sección de verificación tiene **prosa ya redactada en `94` §7** (redline R-12), y su
insumo actualizado es `operacion/97`, el relevamiento de plataforma con la suite completa
en verde. **El número de tests se cita desde `operacion/97`, no desde acá** — como
cualquier cifra.

---

### AJ-4.11 · 🟠 — lo que NO se implementó

**Cada ítem con su estatuto exacto — ya no comparten uno solo.** Los tres:

- **Distribución de alertas por MQTT** — sigue **sin implementar** (el repo es un
  esqueleto sin commits), pero ✎ 2026-08-10 su estatuto cambió: **ADR-016 derogó la
  cláusula de exclusión cerrada (ADR-015 §2c)** y la puso en alcance como **trabajo
  comprometido**. Se redacta describiendo el diseño (`92b`, y `nucleo/19` para el ciclo
  de vida de la alerta) y **declarando el estado real al momento de la entrega** —
  nunca en presente mientras no haya código verificado. E-06 (dashboard) sigue excluida.
- **Métricas MOT** (exclusión E-10). Atención al matiz de R-21: lo excluido son las
  **métricas**, no la capacidad — el tracker existe y la granularidad por sujeto es el
  mejor resultado del banco.
- **Fine-tuning** (E-04) — ✎ 2026-08-11 su estatuto cambió: **ADR-017 la puso en
  alcance como jornada experimental comprometida** (escalera T1→T2/T3 con go/no-go
  pre-registrados, Mendieta, costo medido **≈1 GPU-h**). Se redacta como **rama
  condicionada por datos y protocolo desde el diseño** (F-100.1, regla Tabla 37) y
  **declarando el estado real de la jornada al momento de la entrega**, con causa
  técnica — nunca "por tiempo", y nunca en presente mientras no haya corrida
  verificada. *Decía "no ejercida por secuenciación"*.

**Prosa ya redactada en `94` §8** (redline R-13), con la anotación importante: de los 8
límites que esa lista enumera, **5 estaban ya resueltos** cuando ADR-015 cerró el
alcance. Transcribirla sin revisar declararía como faltante algo que existe.

---

### AJ-4.12 · 🟠 — extensibilidad: los puntos de extensión, y su costo medido

Dos mitades:

1. **Los puntos de extensión del sistema** — el "cómo agrego X" (`92` §9).
2. **Cuánto costó realmente agregar una condición nueva**, medido: **0 entrenamientos,
   48 líneas, 9 minutos**, con la clase `machinery` alcanzando **AP 0,662 zero-shot**
   sin haber sido configurada jamás. Es la tabla **T-77** y la conclusión **AF-4**.

**Prosa ya redactada en `94` §9** (redline R-26, "la más valiosa"). **Con su
contrapeso**: el hallazgo F-94.1 —una clase que parece detectarse y no se está
detectando— es parte honesta del mismo resultado y va escrito junto, no aparte.

---

## 3. 🚫 Lo que no hay que escribir en el §17.4

1. **La distribución de alertas en presente.** Mientras no haya implementación
   verificada, cualquier frase que la describa funcionando es falsa. Su estatuto vigente
   es **trabajo comprometido con estado a la entrega** (ADR-016) — no "exclusión cerrada"
   (esa era ADR-015 §2c, derogada) ni "capacidad existente".
2. **Cifras de resultados.** El §17.4 describe **qué se construyó y cómo**; el desempeño
   es el §17.5. Mezclarlos es lo que hace que un capítulo de implementación se lea como
   una defensa apresurada.
3. **La CLI como interfaz principal** del media-plane: dejó de serlo en Fase 1. Las
   utilidades ex-CLI viven en `eovrt_media.tools.*`.

## 4. Fuentes

`material-etapa-3/92` y `92b` · `material-etapa-3/94` §7–§9 · `specs/40`–`45` ·
`nucleo/14`–`19` (relevamientos vigentes por servicio; el `19` para el ciclo de vida de
la alerta) · `operacion/97` · `operacion/37`, `38`, `80`, `109` · `decisiones/` (ADR-003,
004, 005, 006, 007, 008, 009, 013, 014, 015, 016) · `gobierno/99` §2.3.
