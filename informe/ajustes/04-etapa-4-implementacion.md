# Etapa 4 — §17.4 Implementación del prototipo experimental

> ✅ **Estado (✎ 2026-09-04): CUATRO pases. §17.4 v1.7 entregada con sugerencias, a aceptar por el
> usuario.** El pase 4 ([`entregable/desarrollando/correcciones-etapa-4-pase-4.md`](../entregable/desarrollando/archivado/correcciones-etapa-4-pase-4.md),
> E4-32…E4-57) consolidó el capítulo: 16 → 9 títulos, **cero de nivel 4**, prosa y tablas
> 6.375 → 5.493 w, dos puntos 55 → 1, punto y coma 29 → 0, y la Tabla 60 pasó a prosa por estatuto.
> **Los dos handoffs de §0 quedaron aterrizados**: H2-01 (orden de arranque real, que la v1.6
> afirmaba al revés) y H2-02 (las 2.946 imágenes con su causa). También aterrizó **E4-31**, el
> detalle operativo del ledger que venía de §17.3.
> ⚠ **La numeración de subsecciones cambió**: toda ficha `AJ-4.x` y toda unidad E4-01…E4-31 se lee
> con [`entregable/desarrollando/mapa-secciones-17-4-v1-7.md`](../entregable/desarrollando/archivado/mapa-secciones-17-4-v1-7.md).
> **Lo que sigue es registro histórico.**
>
> ✅ **Estado (✎ 2026-08-23): la sección está REDACTADA y sus tres pases de corrección
> están APLICADOS Y VERIFICADOS** — documento de trabajo `§17.4 v1.5` (✎ 2026-08-28: vigente **v1.6**, `00-el-informe-hoy`) en
> `entregable/desarrollando/`, texto base extraído en `entregable/90b-etapa4-texto-extraido.md`.
> Lo que queda: **el handoff recibido de la Etapa 2 (§0, abajo)**, la revisión del autor, las
> URLs del lote (C1) y la integración al maestro. Las
> unidades `AJ-4.x` de abajo ya fueron incorporadas; se conservan como criterio de lectura.
>
> *Lo que sigue es el encuadre del 2026-08-10, conservado como registro histórico:*
>
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
| Prosa ya redactada | `material-etapa-3/94` §7 (verificación), §8 (alcance efectivo), §9 (extensibilidad) |
| Especificación por módulo | `specs/40` (integrador) · `41` control-plane · `42` media-plane · `43` clip bench · `44` experimental-setup · `45` distribución |
| Relevamientos vigentes por servicio (✎ 2026-08-10) | **`nucleo/14`** (mapa de la cadena) · `15` setup · `16` datasets · `17` media · `18` control · **`19` el ciclo de vida de la alerta** — relevados contra git y código, sin cifras |
| Estado real de la plataforma | `operacion/97-relevamiento-plataforma-2026-08-05.md` + `operacion/114-relevamiento-distribucion-alertas.md` |
| Decisiones a citar | `decisiones/` — ADR-001…018 (+ la serie propia del control-plane, 4 dígitos) |

---

## 0. Handoff recibido de la Etapa 2 — pendiente de escribir en §17.4

> ✎ **2026-08-30.** Estas dos unidades **no** son `AJ-4.x`: llegaron desde el cierre de la
> Etapa 2 y **todavía no están en `§17.4 v1.6`**. Origen:
> `entregable/desarrollando/archivado/correcciones-etapa-2-pase-2.md` §5, fila
> "§17.4 v1.6 · handoff Etapa 4".

| ID | Qué falta decir en §17.4 | Estado en v1.6 |
|---|---|---|
| **H2-01** | **Orden de disparo real de la corrida live: control → distribución → medios.** No es el orden del flujo de datos, es el inverso; la no-pérdida en el bus de alertas la garantiza el handshake del publicador, no el orden. Fuente: `operacion/130` R-01 · CLAUDE.md "Acople entre planos". | ausente |
| **H2-02** | **Desviación del rango de entrenamiento: 500–2.000 → 2.946, con causa.** Ver ficha abajo. | ausente (sólo aparece el cierre de T3 por fuentes compartidas) |

### H2-02 · la desviación del rango, y por qué NO es un incumplimiento

**El problema si no se escribe.** §17.1 fija un rango orientativo de **500 a 2.000 imágenes**
para el split de entrenamiento y exige explícitamente *"justificarse si se apartan de ese
rango"* (§17.1.6.2.4 y Tabla 28). El fine-tuning usó **2.946 train / 483 val**, un 47 % sobre
el techo. §17.5 ya reporta las 2.946 pero **no dice que exceden el rango ni por qué**: leído
así, parece que el protocolo se violó. No se violó — la desviación es **consecuencia directa
de cumplir la regla anti-leakage** de §17.1.6.5.

**Qué tiene que decir §17.4** (la causa es implementación; §17.5 no se toca):

> La causa de la desviación es el cumplimiento de la regla anti-leakage de §17.1.6.5, no su
> incumplimiento: se tomó el 100 % de los linajes elegibles tras excluir íntegramente la
> fuente compartida con el banco (1.330 imágenes) y deduplicar perceptualmente contra él
> (81 imágenes más), sin submuestrear al techo del rango. Declarar también los controles en
> cero — solapamiento con el banco, y componentes compartidos entre entrenamiento y
> validación — y la semilla registrada: son la evidencia de las reglas 3 y 4 de §17.1.6.5.

**Evidencia verificable** (`e-ovrt_experimental-setup/finetuning/manifests/`):

| Dato | Valor | Archivo |
|---|---|---|
| Gates de disyunción | `bench_overlap_selected: 0` · `bench_rows_in_manifest: 0` · `shared_components_train_val: 0` | `finetuning_v1.summary.json` |
| Semilla | `seed: 42` | ídem |
| Banco congelado al auditar | sha256 `4557024e…` · `unchanged: true` · 6.477 imgs | `finetuning_v1.audit.json` |
| Excluidas por solapamiento | 81 imágenes (56 por componente perceptual · 25 por linaje de fuente), 34 linajes | ídem |
| Cadena de selección | 4.210 candidatas → 4.129 tras el guard → 3.429 seleccionadas (2.946 + 483) | ídem |
| Regla perceptual | `ahash`+`dhash` 64 bits, Hamming ≤ 2, **y** MAE gris ≤ 2,0 sobre thumbnail 16×16 — las tres deben pasar | `finetuning_v1.audit.json` §parameters |

Constancia de la desviación: `operacion/130` R-03 (no estaba justificada por escrito en
ADR-017 / doc 100 / D-FT-11 hasta esa nota).

⚠️ **Forma de nombrar las fuentes:** §17.5 las describe **sin identificador** ("obra con mayor
cobertura de chaleco, n = 1.330"), mientras §17.1 sí las nombra. Usar la forma que ya emplee
§17.4 en su entorno; no mezclar las dos en el mismo párrafo.

🚫 **Lo que NO se hace acá:** no se toca §17.5 (ya reporta las 2.946; la causa vive en §17.4),
no se reabre la Etapa 2 (§17.1 previó la desviación y sus cinco reglas se cumplieron), y no
se crea una limitación nueva — el set `L1–L8` está cerrado (D-113.1).

---

## 1. Tablero de contenidos a escribir

| ID | Tipo | Pri | Qué tiene que decir el §17.4 | Insumo |
|---|---|---|---|---|
| **AJ-4.01** | CONCRETA | 🟠 | **Las piezas de software que existen**: tres componentes originales + el módulo funcional de distribución; datasets permanece como cadena de datos. | `GUIA-REDACTORES` §1 · `operacion/114` · CLAUDE.md |
| **AJ-4.02** | CONCRETA | 🟠 | La **correspondencia diseño → artefacto real**: es la respuesta directa al pedido del tutor técnico. | `92` §1 · `94` §1.2 |
| **AJ-4.03** | CONCRETA | 🟠 | Los **contratos de datos reales**, con esquema y serialización. | `92` §2 y §5 · `94` §1.3–1.4 |
| **AJ-4.04** | CONCRETA | 🟠 | Los dos planos son **servicios HTTP config-driven**, no CLIs. | `92` §3 · `94` §1.5 · ADR-008/009 |
| **AJ-4.05** | CONCRETA | 🟠 | Los **dos caminos de acople** (DBE por archivo · EBE por bus), con el orden de disparo y sus trampas. | `94` §3 · ADR-003/007 · `operacion/37`, `38` |
| **AJ-4.06** | EVIDENCIA | 🟡 | **El JSONL es la verdad en los dos caminos**: toda corrida live es re-evaluable offline. | `operacion/37`, `109` |
| **AJ-4.07** | CONCRETA | 🟡 | La **configuración efectiva** y el modelo desplegado. | `92` §6 |
| **AJ-4.08** | CONCRETA | 🟡 | **Artefactos y layout por experimento**. | `92` §8 · ADR-004/014/006 |
| **AJ-4.09** | CONCRETA | 🟡 | La **construcción del GT temporal** y su trampa de método. | `specs/43` · `operacion/80` · `99` §2.3 |
| **AJ-4.10** | EVIDENCIA | 🟠 | **El sistema es ejecutable y verificable**, con el número de la suite. | `94` §7 · `operacion/97` |
| **AJ-4.11** | EVIDENCIA | 🟠 | **Límites y brechas restantes**, cada ítem con su estatuto exacto. | `94` §8 · ADR-005/015/**016**/**017** · `operacion/114` |
| **AJ-4.12** | CONCRETA | 🟠 | **Extensibilidad**: los puntos de extensión, y cuánto costó medido. | `92` §9 · `94` §9 |

---

## 2. Los contenidos, desarrollados

### AJ-4.01 · 🟠 — componentes del prototipo y cadena de datos

- **`e-ovrt_media-plane`** — pipeline de inferencia OVD. Desde Fase 1 es un **servicio**
  FastAPI (HTTP/WS) config-driven en `:8080`; el modelo se carga una vez al arranque y una
  corrida se dispara con `POST /api/runs` (una activa a la vez).
- **`e-ovrt_control-plane`** — motor de patrones de riesgo CR-01/CR-02 sobre eventos
  `media.detection.v1`; también servicio HTTP en `:8081`.
- **`e-ovrt_experimental-setup`** — **no es un plano**: catálogos de experimento
  (`prompts/`, `experiments/`), el runner reproducible y la **webconsole** (React +
  FastAPI BFF), cliente HTTP de ambos planos.

**`e-ovrt_alert-distribution` es el cuarto repositorio funcional, pero no un tercer
plano.** Consume alertas confirmadas, aplica la política de notificación, entrega por
MQTT y conserva el ledger. Los seis criterios de spec 45 están verificados (`operacion/114`).
✎ **2026-08-14:** la integración se completó el 2026-08-13 — vista de webconsole
(`13c801e`), orquestación (`42529e2`) y repo versionado (`c9903cc`, `1e6d8fa`); el párrafo
decía que las tres faltaban (ver `AJ-4.11`).

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

✎ **2026-08-18 (ADR-019 + ADR-020): la ficha se redacta como TRES servicios HTTP
config-driven, no dos.** El módulo de distribución también expone el suyo (`:8082`,
espejo del control-plane; doc `operacion/124`), con lo que la afirmación fuerte del
capítulo pasa a ser: *los tres módulos de la cadena son servicios HTTP config-driven, y
la webconsole y el runner son clientes de los tres*. **ADR-020 derogó a ADR-018**: el
runner le habla por HTTP **por default** y el subproceso quedó como fallback operativo —
**no se menciona en el capítulo**, es operación y no arquitectura. Los patrones de acople
del informe son **dos**: HTTP config-driven y bus ZeroMQ. Material: `92` §3 (banner ✎
08-18) y doc 124.

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

> ✎ **2026-08-20 — resuelto por E4-19** (`entregable/desarrollando/correcciones-etapa-3-4.md`):
> §17.4.8 se amplía a cuatro subsecciones (adquisición/rodaje · segmentación con criterios
> ex-ante · preanotación + revisión en CVAT · derivación/congelamiento). La trampa del nivel
> de export queda en §17.4.8.4 como una cláusula ("valida la estructura de cada exportación")
> y su detalle operativo va al anexo de reproducibilidad §19 (AJ-6.02). La lección de los
> "person N" de la interfaz vs. `track_id` del XML sigue siendo material de §17.5 (AJ-5.07).

---

### AJ-4.10 · 🟠 — el sistema es ejecutable y verificable

La sección de verificación tiene **prosa ya redactada en `94` §7** (redline R-12), y su
insumo actualizado es `operacion/97`, el relevamiento de plataforma con la suite completa
en verde. **El número de tests se cita desde `operacion/97`, no desde acá** — como
cualquier cifra.

---

### AJ-4.11 · 🟠 — límites y brechas restantes

**Cada ítem con su estatuto exacto — ya no comparten uno solo.** Los tres frentes:

- **Distribución de alertas por MQTT** — **implementada, verificada e integrada**
  (✎ 2026-08-22; antes esta línea decía que quedaban pendientes la vista de webconsole,
  la orquestación y los commits del repo — las tres cosas están hechas: consola y
  orquestación integradas, repo versionado y con remoto). E-06 (canales extra y
  dashboard propio) sigue excluida. Diseño y contratos: `92b`; evidencia ejecutada:
  `operacion/114`.
- **Métricas MOT** (exclusión E-10). Atención al matiz de R-21: lo excluido son las
  **métricas**, no la capacidad — el tracker existe y la granularidad por sujeto es el
  mejor resultado del banco.
- **Fine-tuning** (E-04) — ✅ **✎ 2026-08-22: la jornada está COMPLETA en sus tres
  tramos y ya no hay estado que "declarar a la entrega": se declara el CIERRE.**
  T1 NO-GO (`operacion/123`) · T2 NO-GO (`operacion/127`) · T3 cerrado con causa técnica
  (`operacion/117` §2). Para §17.4 rige **E4-27** (pase 3): la fila de la Tabla 68 dice
  que la escalera pre-registrada se ejecutó completa, que ningún checkpoint se incorporó
  y que el veredicto negativo es pre-registrado — el marcador `[[PENDIENTE]]` de esa fila
  se elimina. Las cifras y su lectura (curva de tres puntos, F-127.1: fallo estructural
  de datos, no de capacidad) van en §17.5, no acá. Sigue rigiendo: **rama comparativa
  condicionada por datos y protocolo, nunca "por tiempo"** (ADR-017). *(Las notas 08-11 →
  08-15 que estaban en este bullet quedaron como historia en `estado-de-implementacion-adrs.md`,
  fila 017, que está al día.)*

**Prosa ya redactada y corregida en `94` §8** (redline R-13). Transcribir una versión
anterior declararía como faltantes G1, la comparación de estrategias, distribución y la
paridad DBE/EBE, todos ejercidos después de la primera redacción.

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

**✎ 2026-08-12 — hay una tercera mitad, y es la que le contesta al tutor técnico.**
La extensibilidad no se midió sólo sobre una **condición** nueva: también se midió sobre
el **evento de percepción**, que es exactamente lo que el tutor pidió asegurar ("que den
soporte a datos que hoy no están, pero mañana sí: tracking, velocidad, dirección, pose,
segmentación"). De esa lista, **identidad de sujeto se recorrió de punta a punta**:

- se materializó **por configuración**, como decorador de la fuente de eventos del plano
  de control (`input.track_persons`, opt-in), **sin tocar el contrato ni el plano de
  medios**, y sirve igual para el acople por archivo y por bus;
- la campaña **G1** la midió **contra escena con las mismas detecciones bit a bit** — la
  ganancia es íntegramente del motor — y resultó **el mejor resultado del banco**;
- el camino config-driven **reproduce la campaña exacto**: el número es lo que rinde la
  plataforma por YAML, no un script suelto.

Esto convierte la regla de evolución de §17.3.11.4 (que allá se enuncia **sin cifra**, por
no-anacronismo) en **capacidad verificada** acá. **La cifra se cita desde el índice de
`results/`**, nunca desde una tabla-atajo. Va con sus dos honestidades: el `track_id` **no
queda en el JSONL del plano de medios** sino en los artefactos del control (trazabilidad
sostenida por el determinismo del seguidor y el orden del stream), y **lo excluido por
E-10 son las métricas MOT, no la capacidad**.

Insumo: `92` §4.2 y su recuadro · `94` §2 · `operacion/89` · `operacion/90` (D-90.3).

---

## 3. 🚫 Lo que no hay que escribir en el §17.4

1. **La distribución de alertas en presente.** Mientras no haya implementación
   verificada, cualquier frase que la describa funcionando es falsa. Su estatuto vigente
   es **trabajo comprometido con estado a la entrega** (ADR-016) — no "exclusión cerrada"
   (esa era ADR-015 §2c, derogada) ni "capacidad existente".
   ✎ **2026-08-18 — este ítem quedó INVERTIDO: ahora SÍ hay implementación verificada, y
   la prohibición cambió de signo.** El módulo funciona y está medido (docs
   `operacion/114`/`118`), el runner lo orquesta (ADR-018) (✎ 2026-08-28: **por HTTP, ADR-020** —
   ADR-018 quedó derogada ese mismo 08-18, ver L119 de esta ficha; el subproceso es fallback y no
   se describe) y expone servicio HTTP propio
   (ADR-019, doc 124). **Se escribe en presente y como capacidad existente**, con su
   estatuto: trabajo comprometido por ADR-016, entregado y verificado. Lo que sigue
   estando prohibido: citar cifras de la verificación funcional del servicio HTTP (n=2,
   doc 124 — no citables) en lugar de las de la campaña (doc 118), y presentar la
   containerización como hecha (diferida con causa, ADR-019 §4). (✎ 2026-08-28, `operacion/130`
   R-09: la containerización está **definida** —imagen y compose de 13 servicios escritos y
   validados por configuración el 08-19/20, Dockerfiles en los tres repos— y lo diferido es
   **build + smoke integral**, post-entrega. Se escribe "definida, despliegue no verificado";
   nunca "hecha/desplegada" ni "diferida".)
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
