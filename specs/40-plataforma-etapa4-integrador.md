# Spec 40 — Plataforma / Etapa 4 (integrador)

- **Fecha:** 2026-07-09
- **Estado:** Escrito — primero de la cola (ADR-010: tramo plataforma)
- **Ámbito:** transversal — fija los contratos, identificadores, criterios y
  definiciones que los specs 41/42/44/45 citan; no implementa nada por sí mismo.
- **Decisiones que implementa:** ADR-003 (bus ZeroMQ), ADR-004 (`experiment_id`),
  ADR-006 (reporte + aplicabilidad), ADR-007 (semántica 1:1). Toca: ADR-002
  (contrato `track_id`), ADR-008/009 (superficies de servicio y gestión).
  Insumos: doc 05 (diseño del bus), doc 08 §2.2/§2.5/§5.2 (métricas, hitos,
  Tablas D.4/D.5/D.6), doc 02 §4.8 (nombres contractuales preliminares).

## 1. Mapa contrato-preliminar ↔ artefacto real

Etapa 3 usa "denominaciones contractuales preliminares"; el informe final debe
incluir esta tabla de correspondencia (doc 02 §4.8). Es normativa: los specs y la
escritura usan **los nombres reales**, citando el preliminar solo al presentarlos.

| Contrato preliminar (Etapa 3) | Artefacto real | Dónde vive |
|---|---|---|
| `RunConfig` | **Manifiesto paraguas** + configs por plano referenciadas (ADR-004/009) | `experimental-setup` (centralizado) |
| `PerceptionEvent` | `media.detection.v1` (`DetectionEvent`) | media-plane `contracts/`; espejo en control-plane |
| `FrameMetadata` | Bloque `source` de `media.detection.v1` (`source_id`, `frame_index`, `timestamp_ms`, `width`, `height`) + `VisualUnit` interno | media-plane |
| Estado de patrón | `control.pattern_state.v1` (`PatternStateChanged`) | control-plane `contracts/pattern.py` |
| Alerta interna | `control.alert.v1` (`AlertEvent`, `alert_id` uuid5 determinista) | control-plane `contracts/alerts.py` |
| Alerta distribuida | `control.notification.v1` (`NotificationEnvelope`) + `control.delivery.v1` | repo distribución (ADR-005) |
| Repositorio de eventos (§17.3.12) | JSONL append-only por corrida (`runs/<id>/*.jsonl`) | cada plano |
| Bitácora experimental (Tabla D.6) | **Reporte consolidado** `report.json`/`report.md` (§6) | experimental-setup |

**Regla de evolución de contratos:** cambios siempre **aditivos** (campos
opcionales con default). `track_id` (ADR-002) entra como campo opcional de
`media.detection.v1` — **no** hay bump a v2 (cierra la pregunta doc 05 §10.2).

## 2. Identidad de corrida y trazabilidad (`experiment_id`)

- **Generación:** el runner o la webconsole (ADR-009) generan
  `experiment_id = exp_<YYYYMMDD>T<HHMMSS>Z_<slug>` al instanciar un manifiesto.
  Único, ordenable, legible; el slug viene del manifiesto.
- **Propagación (campo opcional aditivo en todos los casos):**

| Artefacto | Campo | Estado |
|---|---|---|
| Manifiesto paraguas | `experiment_id` (raíz) | nuevo (spec 44) |
| `RunSummary` media-plane | `experiment_id` | **ya existe** — poblarlo siempre |
| Eventos + summary control-plane | `experiment_id` | nuevo (spec 41) |
| `NotificationEnvelope` / `DeliveryRecord` | `experiment_id` | nuevo (spec 45) |
| `report.json` | `experiment_id` (clave del reporte) | nuevo (spec 44) |

- **Cadena de reconstrucción exigible** (la promesa de §17.3.11.1): desde una
  alerta → `alert_id` → `control_run_id` + `media_run_id` + `experiment_id` →
  manifiesto → configs efectivas + `prompt_set_id` (+ parámetros de fusión si
  E-HYB, doc 12 §6.4) → clip/fuente. El criterio de terminado del tramo
  plataforma (ADR-010) es poder ejecutar esta cadena para cualquier alerta.

## 3. Bus media→control (normativo; implementación en specs 41/42)

### 3.1 Envelope `bus.envelope.v1` (msgpack)

```
{ schema_version: "bus.envelope.v1",
  topic:  "media.detection.v1.<media_run_id>",
  key:    "<source_id>",
  seq:    <int, contador por publisher, monótono desde 0>,
  ts_publish_ms: <float, reloj del publicador>,
  payload: <evento serializado tal cual se persiste en JSONL> }
```

- `payload` es **byte-compatible** con la línea JSONL: un evento consumido por bus
  y uno releído del archivo son el mismo objeto (base del test de paridad, §3.4).
- Topics jerárquicos; suscripción por prefijo. Tramos: `media.detection.v1.*`
  (este bus) y `control.alert.v1.*` (bus control→distribución, spec 45 — mismo
  envelope, mismas primitivas `transport/`).
- **Fin de corrida:** evento de control `run.lifecycle.v1` con
  `{event: "run_finished", media_run_id, status}` publicado al cerrar el run
  (sentinela END del patrón two-node). Fallback del consumidor: polling de
  `GET /api/runs/{id}` (doc 05 §6.3, ya soportado por el media-plane).

### 3.2 Reglas de fiabilidad (obligatorias — ADR-003 / doc 07 H6)

1. **Orden de arranque:** el consumidor se suscribe **antes** de dispararse el run
   (el runner/webconsole lo garantiza: primero control-plane listo, luego POST al
   media-plane).
2. **Detección de pérdida:** huecos en `seq` → contador de drops en las métricas
   del consumidor; si drops > 0, la corrida se reporta **degradada** con causa
   (taxonomía §17.3.13.3). Nunca se silencia.
3. **No-bloqueante:** el publicador usa HWM finito y nunca frena la inferencia;
   la durabilidad la da el JSONL (el bus transporta, no almacena).
4. **Re-evaluabilidad:** toda corrida live es re-ejecutable offline desde el JSONL;
   la comparación live-vs-replay es un resultado de robustez (R4).

### 3.3 Quién consume el bus (cierra doc 05 §10.4)

Solo procesos de la plataforma (control-plane; futuro: distribución en su tramo).
**La webconsole NO consume ZeroMQ**: consume las APIs/WS de los servicios (patrón
BFF existente). El bus queda interno entre planos — un solo cliente por tecnología
de transporte, cero CORS/proxy nuevos.

### 3.4 Test de paridad replay↔stream (gate del tramo plataforma)

Con el fixture temporal sintético: correr el motor (a) por `JsonlSource` y (b) por
`BusSource` alimentado por un publicador que reproduce el mismo archivo. Los
`pattern_events.jsonl` y `alerts.jsonl` resultantes deben ser **idénticos módulo
timestamps de procesamiento**. Es el criterio de que "el motor es agnóstico de la
fuente" (doc 05, Fase A/B) y se suma al gate de regresión F1=1.0.

## 4. Semántica de corrida (ADR-007) y relojes

- **1:1:** una corrida del control-plane por run del media-plane; nace suscripta,
  cierra con `run_finished` (o fallback por estado) y emite su summary. Ventanas
  propias = trabajo futuro declarado.
- **Relojes (EBE two-node — hueco señalado en doc 02 §4.6):** regla normativa:
  - Latencias **intra-nodo** se miden con el reloj monotónico local de cada nodo
    (sub-etapas del media-plane; `processing_ms` del control-plane).
  - Latencias **end-to-end entre nodos** se miden **en un solo reloj**: el del
    receptor (diferencia entre eventos recibidos), nunca restando timestamps de
    hosts distintos.
  - Si una métrica exige cruzar relojes (`t_alert-system` con t0 anotado en la
    fuente), se declara la sincronización (chrony/NTP) y su error estimado en el
    reporte; sin sincronización declarada, la métrica cae a
    `not_interpretable` con causa `clock_skew`.
  - `ts_publish_ms` del envelope + `ts_receive` del consumidor dan la latencia de
    transporte del bus (informativa, mismo criterio).

## 5. Diccionario de métricas (única fuente: §17.1.7 + Tablas 35/D.4; doc 08 §2.2)

### 5.1 Tabla del diccionario

Las métricas marcadas *(derivada, propia)* no son del informe: lo **descomponen**,
no lo sustituyen (fundamento en §5.2 y doc 08 §2.2 adenda).

| Métrica | t0 | t1 | Unidad | Condición de aplicación |
|---|---|---|---|---|
| **G2A** | captura/lectura del frame | resultado algorítmico disponible | ms | siempre (media-plane); presupuesto **50–250 ms** |
| **t_alert-system** (principal) | **inicio anotado** del evento (GT) | alerta confirmada y registrada | s | requiere GT temporal (tramo evaluación) |
| **t_capture→alert** (§5.2 — derivada, propia) | captura del frame de **primera evidencia** del episodio | `AlertEvent` registrado | ms | **sin GT**; `computed` en fuente viva (EBE); en DBE-archivo → `not_interpretable / dbe_media_time` (ver §5.2.3) |
| **t_compute-budget** (§5.2 — derivada, propia) | — | `t_capture→alert` − `T_persistencia_efectiva` | ms | **siempre** (monotónico, independiente de la fuente) |
| **t_alert-notification** | alerta confirmada | entrega efectiva por canal | ms | solo con trayecto de distribución instrumentado; en DBE se etiqueta wall-clock-DBE |
| **TTFD** | inicio anotado (GT) | captura del frame de primera evidencia positiva (criterio declarado, §5.2.2) | s | requiere GT temporal |
| **SDR** | — | proporción del intervalo anotado con detección sostenida | ratio | requiere GT temporal |
| **TTFA interna** (diagnóstico) | primera evidencia positiva | alerta | ms/frames | siempre (ya en eval temporal); NO sustituye a t_alert-system |
| **ΔFP_tracker** | — | FP con tracker − FP sin tracker | conteo (unidad declarada) | solo si tracker activo Y unidad de FP comparable (Tabla D.2); si no, exploratorio |
| Latencias por sub-etapa, FPS efectivo, drops | — | — | ms / fps / conteo | siempre (instrumentación existente) |

### 5.2 `t_capture→alert` — la cadena frame→evento del tramo plataforma

**Qué es.** La latencia del sistema desde que se captura el frame que produjo la
**primera evidencia positiva** de un episodio hasta que el `AlertEvent` queda
registrado. Es la única métrica end-to-end de la cadena media→control que **no
requiere ground truth**, y por eso es el criterio de validación del tramo
plataforma (ADR-010).

**Estatus epistemológico (declararlo así en el informe):** es una métrica
**derivada, propia de este trabajo**, no una de las oficiales del §17.1.7. No
sustituye a `t_alert-system`: la **descompone**. Se introduce porque el tramo
plataforma debe demostrar instrumentación completa antes de que exista el dataset
con GT.

#### 5.2.1 Descomposición

```
t_capture→alert = G2A(f₀) + t_bus + T_persistencia_efectiva + t_reasoning(f_conf)
                  └ f₀ = frame de primera evidencia   f_conf = frame de confirmación

t_compute-budget = t_capture→alert − T_persistencia_efectiva
                 = G2A(f₀) + t_bus + t_reasoning(f_conf) + overheads
```

`T_persistencia_efectiva` = tiempo (en timestamps de fuente) entre la primera
evidencia y la confirmación; está gobernado por `confirm_after_ms` del pattern set,
no por el cómputo. `t_compute-budget` es exactamente **el "presupuesto
computacional" por el cual la Tabla D.4 dice que `t_alert` excede necesariamente a
la persistencia** — y es medible en DBE y EBE por igual.

#### 5.2.2 Identidad con la métrica oficial (el argumento de la secuenciación)

Si se declara que el `t1` de **TTFD** es el **instante de captura** del frame de
primera evidencia (y no el instante en que la detección termina de computarse),
entonces vale exactamente:

```
t_alert-system  =  TTFD  +  t_capture→alert
                   └ GT ┘   └ plataforma ┘
```

Consecuencia práctica y defendible: **el tramo plataforma mide su mitad de la
métrica principal sin ningún GT**; cuando el clip bench llegue (spec 43), obtener
`t_alert-system` es sumar TTFD. Esta identidad se verifica numéricamente en la
primera corrida con GT y se reporta como control de consistencia.

#### 5.2.3 Aplicabilidad (ADR-006) — dos casos que hay que declarar

1. **DBE sobre archivo:** los `timestamp_ms` de la fuente son **tiempo de medio**,
   no reloj de pared; el replay consume el archivo más rápido (o más lento) que
   tiempo real. `t_capture→alert` se reporta `not_interpretable` con causa
   `dbe_media_time`. **`t_compute-budget` sí es válido** (se mide con relojes
   monotónicos del proceso) y es el número que vale en DBE.
2. **EBE two-node:** la captura ocurre en el Nodo A y el `AlertEvent` se registra
   en el host del control-plane → **cruza relojes**. Aplica §4: se declara la
   sincronización (chrony/NTP) con su error estimado, o la métrica cae a
   `not_interpretable / clock_skew`. En EBE single-host es un solo reloj y sale
   `computed` sin condiciones.

#### 5.2.4 Instrumentación requerida (quién persiste qué)

| Dato | Dónde se produce | Artefacto |
|---|---|---|
| `capture_monotonic_ns` + `capture_wallclock_ms` por unidad | media-plane, al leer el frame | `metrics.jsonl` (por `unit_id`) |
| `g2a_ms` por unidad | media-plane | `metrics.jsonl` (por `unit_id`) |
| `source_clock: wallclock \| media` (decide la aplicabilidad, §5.2.3) | media-plane, por fuente | `summary.json` |
| `ts_publish_ms` | media-plane (publisher) | envelope §3.1 |
| `ts_receive_ms` | control-plane (`BusSource`) | `metrics.jsonl` |
| `first_evidence_unit_id` + `first_evidence_ms` del episodio | control-plane | evento de transición + `alerts.jsonl` |
| `alert_registered_ms` (instante de escritura) | control-plane | `alerts.jsonl` |
| `processing_ms` por unidad | control-plane | `metrics.jsonl` |

El **join es por `unit_id`**: el reporte consolidado (§6) une la unidad de primera
evidencia referenciada por la alerta con la fila de métricas del media-plane que la
produjo. Por eso `first_evidence_unit_id` es obligatorio en el contrato de alerta
(spec 41 §8.2) — sin él la métrica no se puede atribuir.

### 5.3 Umbrales, reporte temporal y estados

- **Umbrales por severidad (Tabla D.4):** Alta/PR-01: t_alert 5–10 s, TTFD < 3 s,
  SDR ≥ 0.60, persistencia 3–5 s, balance FP/FN. Media/PR-02: 10–20 s, < 10 s,
  ≥ 0.70, 5–10 s, minimizar FP. (Crítica: 3–5 s / <1 s / ≥0.50 — sin patrón
  asignado en el núcleo.) El t_alert máximo **excede** a la persistencia por el
  presupuesto computacional — cuidar esa lectura en el evaluador. Ese excedente es
  precisamente `t_compute-budget` (§5.2.1), que el tramo plataforma ya mide: si
  supera el margen de la Tabla D.4, la configuración es indefendible **antes** de
  tener el GT.
- **Reporte temporal mínimo:** P50/P95/P99 + promedio, warm-up declarado,
  timestamps monotónicos con fuente explícita.
- **Estados de aplicabilidad** (ADR-006, §17.3.13.3): toda métrica del diccionario
  figura en cada reporte con `status: computed | applicable_not_computed |
  not_applicable | not_interpretable` + `cause`. En el tramo plataforma (ADR-010),
  las que exigen GT figuran `not_applicable / no_ground_truth` — **figuran**, no
  se omiten: eso demuestra que la instrumentación está lista antes que el GT.

### 5.4 Hitos obligatorios por alerta (instrumentación — doc 08 §2.5 / Tabla D.5)

Timestamps persistidos por episodio: **primera evidencia positiva** (campo nuevo,
con su `unit_id` — §5.2.4), patrón candidato, confirmado, alerta registrada,
notificación entregada. Los tres del medio ya existen en `pattern_events.jsonl`;
el primero es campo nuevo (spec 41), el último es del tramo distribución (spec 45).
Estos cinco hitos son exactamente los insumos de `t_capture→alert` y de la familia
"alerta y patrón" de la Tabla D.5.

## 6. Reporte consolidado (`report.json` / `report.md`)

- **Generador:** script en experimental-setup (spec 44) — no servicio, no DB.
  Entrada: `experiment_id` → localiza manifiesto + `runs/` de ambos planos (+
  distribución si existe). Salida: `report.json` (máquina) + `report.md` (humano).
- **Schema: mapear campo a campo contra la Tabla D.6** (bitácora):
  identificación (`experiment_id`, run ids, fecha), modelo/checkpoint/variante,
  entrada (fuente, clip/dataset, resolución), parámetros (prompt set, pattern set,
  umbrales, tracker on/off, ventanas, histéresis, fusión), hardware/entorno,
  temporalidad (warm-up, relojes, criterio §4), eventos de patrón y alerta
  (conteos + hitos §5.4), resultados (diccionario §5 con estados), observaciones.
- Regla: el reporte **no recalcula** — agrega lo que los planos ya persistieron;
  si un insumo falta, la métrica correspondiente queda `applicable_not_computed`
  con causa, y el reporte se emite igual.

## 7. Criterios de terminado del tramo plataforma (gate de ADR-010)

- [ ] Corrida disparada desde webconsole o runner con `experiment_id` propagado a
      **todos** los artefactos de §2.
- [ ] Bus operando con las reglas de §3.2; test de paridad §3.4 en verde.
- [ ] Corrida EBE two-node con alertas en vivo cerrando 1:1 (§4) y latencias
      reportadas con el criterio de relojes.
- [ ] `report.json` generado con el diccionario completo de §5 — cada métrica con
      su estado (las de GT en `not_applicable/no_ground_truth`).
- [ ] **`t_capture→alert` y `t_compute-budget` computados y atribuidos** para al
      menos una alerta real de una corrida EBE (join por `unit_id`, §5.2.4), con
      su descomposición G2A / bus / persistencia / reasoning. En una corrida DBE de
      archivo, `t_capture→alert` figura `not_interpretable/dbe_media_time` y
      `t_compute-budget` `computed` — la taxonomía de aplicabilidad, ejercitada de
      verdad.
- [ ] `t_compute-budget` contrastado contra el margen de la Tabla D.4 (§5.3).
- [ ] Cadena de reconstrucción de §2 ejecutada sobre una alerta real y documentada
      (es la demo de trazabilidad de R3, ensayable ya sin GT).

## 8. Interfaces con los demás specs

- **41 (control-plane):** `MediaEventSource` + `BusSource`, runtime live 1:1,
  servicio mínimo, `experiment_id`, hito "primera evidencia", TTFA, estados de
  aplicabilidad en sus evals.
- **42 (media-plane):** `BusPublishingArtifactWriter` (envelope §3.1, seq, END),
  `track_id` opcional, `experiment_id` poblado, G2A explícito contra presupuesto.
- **44 (experimental-setup):** manifiesto + generación de `experiment_id`, runner,
  generador de reporte §6, webconsole (§3.3: APIs, no bus).
- **45 (distribución):** mismo envelope y `transport/` para `control.alert.v1.*`;
  `t_alert-notification` según §5; `experiment_id` en sus registros.
- **43 (clip bench, diferido):** consume las definiciones de §5 tal cual (su §10
  ya mapea contra este diccionario); al ejecutarse, las métricas `not_applicable`
  pasan a `computed` sin tocar la plataforma.
