# Revisión crítica de Etapa 3 y norte propuesto para el cierre del proyecto

> ⚠️ **2026-08-10 — DOCUMENTO HISTÓRICO.** Es la revisión crítica y el norte propuesto
> **antes** de ejecutar el tramo experimental; su última actualización es del 2026-07-09.
> El norte que propone **se ejecutó**. Estado vigente en `../../operacion/95`, conclusiones
> en `../../operacion/98`. Ver el `README.md` de esta carpeta.

- **Fecha:** 2026-07-06
- **Insumo:** `docs/informe/entregable/E-OVRT-VDP_Etapa_3_Diseno_Arquitectonico.docx` (§17.3.1–17.3.18)
- **Contexto:** presentación final de tesis en < 3 meses (~semana del 2026-09-29)
- **Complementa:** `01-relevamiento-control-plane.md`, `05-integracion-media-control-bus-eventos.md`, `06-diseno-distribucion-alertas.md`

## 1. Veredicto general

El documento es sólido y está por encima del estándar habitual de una tesis de grado:
la cadena `condición → estrategia → evidencia → patrón → alerta`, la política de
aplicabilidad de métricas (calculada / aplicable no calculada / no aplicable / no
interpretable) y la disciplina DBE-antes-que-EBE son defendibles y diferenciales.
**No hace falta más arquitectura: hace falta cerrar Etapa 4 (decisiones de
implementación) y ejecutar la campaña experimental.**

El hallazgo más importante de esta revisión es positivo: **la implementación ya está
por delante del backlog del documento**. De los 11 ítems del núcleo validable
(Tabla 58), 9 están construidos y testeados en los repos; de las extensiones
(Tabla 59), la EBE two-node y la interfaz de inspección ya existen. El riesgo del
proyecto no es técnico sino de foco: el documento deja abiertas 4–5 decisiones que,
si no se cierran ya, van a fragmentar los próximos 3 meses.

## 2. Fortalezas a conservar (no tocar)

1. **Separación detección ≠ patrón ≠ alerta** con máquina de estados de 5 estados —
   ya implementada tal cual en el control-plane. Es el corazón conceptual de la tesis.
2. **Política de aplicabilidad de métricas** (§17.3.13.3). Pocas tesis distinguen
   "no calculada" de "no aplicable" de "no interpretable por corrida degradada".
   Materializarla como campo literal (`status: computed|applicable_not_computed|
   not_applicable|not_interpretable` + `cause`) en el reporte de corrida es barato
   y rinde mucho en defensa.
3. **Alerta interna como métrica principal, distribución como trayecto derivado**
   (DA-13). Protege la medición de la variabilidad de canales externos.
4. **Minimización de evidencia visual** (DA-08/09) — bien argumentada ética y
   técnicamente.
5. **Roles CPN/EN/TN como roles lógicos, no máquinas** — y encaja perfecto con lo ya
   construido: en `infra/twonode/`, Nodo A ≈ EN-1 (ingesta + rate + normalización,
   sin semántica) y Nodo B ≈ CPN. Conviene hacer explícita esa correspondencia en
   Etapa 4 con una tabla rol→contenedor.
6. **Criterio de cierre por evidencia, no por código** (§17.3.17): "una unidad se
   completa cuando produce evidencia verificable dentro de una corrida".

## 3. Estado real vs. backlog del documento

| Ítem backlog (Tabla 58/59) | Estado real en los repos |
|---|---|
| 1. Configuración de corrida | ✅ Manifiestos en `e-ovrt_experimental-setup/experiments/` + `effective_config` persistida en ambos planos. Falta el paraguas único (ver §4.4). |
| 2. Lectura de fuentes DBE | ✅ `ImageFolderSource`, `VideoFileSource` (+ `RtspSource` para EBE). |
| 3. Prompts versionados CR-01/CR-02 | ✅ Prompt sets versionados en experimental-setup, `prompt_set_id` propagado en eventos. |
| 4. Modelo OVD baseline por adaptador | ✅ GDINO / MM-GDINO / YOLOE / mock vía `BaseDetectorAdapter`. Sprint 2 ya comparó 5 variantes sobre BENCH v2. |
| 5. Postproceso y normalización | ✅ `Detection` normalizada, bbox px+norm, `media.detection.v1`. |
| 6. Instrumentación plano de medios | ✅ Latencias por sub-etapa (µs), p50/p95/p99, FPS, drops, backpressure. |
| 7. Publicación + persistencia append-only | ◐ Persistencia JSONL sí (el "repositorio de eventos" del §17.3.12 ya existe de facto); **bus interno de eventos: no existe** — hoy el acople es por archivo. |
| 8. Evaluación de patrones CR-01/CR-02 | ✅ `PatternEngine` con ventana ms/frames, histéresis por resolve, estados completos. *2026-07-09 (rama `mati`, doc 01 §12):* + matching 1:1, región adaptativa por pose, memoria de cobertura, expiración de sujetos y cooldown. |
| 9. Alertas internas por episodio | ✅ `AlertEvent` en transición a confirmed, `alert_id` determinista (idempotente). |
| 10. Instrumentación plano de control | ✅ `pattern_events.jsonl`, `metrics.jsonl`, latencia de procesamiento. Falta TTFA formal (existe en la eval temporal). |
| 11. Reporte experimental | ◐ `summary.json` por plano; falta el reporte consolidado de corrida con estados de métricas (§4.6). |
| 12. EBE con fuente viva | ◐ RTSP + two-node dockerizado y verificado; **falta la corrida EBE end-to-end con control-plane** (bloqueada por el bus). |
| 13. Rol EN | ✅ Nodo A del two-node = EN-1. |
| 14. Inspección mínima | ✅ Webconsole (React+FastAPI) — mira media-plane; desde 2026-07-06 muestra también corridas two-node con ciclo de vida correcto (`running`/`succeeded`/`failed`+`live`), validado E2E (doc 11 §8). Falta la vista de alertas del control-plane. |
| 15. Comparación fine-tuning | ✗ No iniciada (correctamente condicionada por DA-07). |
| 16. MOT / zonas / reglas espaciales | ✗ No iniciada (correctamente exploratoria). |

**Lectura:** el "primer objetivo de implementación" del documento (cerrar núcleo DBE)
está a una corrida real de distancia. Nunca se ejecutó la cadena completa
media-plane → control-plane sobre detecciones reales; ese es el paso 0 de todo.

## 4. Puntos críticos a resolver (donde el documento necesita decisión o corrección)

### 4.1 Contradicción en la estrategia de detección del núcleo — la más importante

§17.3.9.2 adopta como estrategia del núcleo el **prompt directo de ausencia**
("person without hard hat") y relega las consultas positivas (person/helmet/vest) a
"diagnóstico que no confirma ausencia". Pero:

- La Tabla 47 (PR-01/PR-02) admite ambas: "evidencia OVD directa **o evidencia
  auxiliar de persona y casco**".
- **La implementación real hace exactamente lo contrario**: el control-plane infiere
  ausencia espacialmente desde evidencia positiva (persona + casco/chaleco en región
  del bbox). Es la única estrategia implementada y testeada.
- La evidencia empírica propia (Sprint 2) y la literatura coinciden: los VLM tipo
  CLIP manejan mal la **negación** — "person without helmet" tiende a matchear
  "person" + "helmet" como bolsa de conceptos. El proxy de estado observable
  (`bare_head`) salió débil en los 5 modelos evaluados sobre BENCH v2.

**Recomendación:** invertir la adopción y convertir la tensión en resultado de tesis.
Definir dos estrategias nombradas y versionadas:
- **E-IND (núcleo):** evidencia positiva + inferencia espacial de ausencia (lo
  implementado). Ventaja adicional defendible: la evidencia es auditable (bbox de la
  persona + región + ausencia verificable), mientras que el prompt de negación es
  una caja negra.
- **E-DIR (variante comparativa):** prompts directos de ausencia y estado observable.

El experimento "E-DIR vs E-IND sobre BENCH + clips" es barato (la infraestructura de
prompt sets ya lo soporta), llena la sección de "sensibilidad al prompt" que la
metodología promete, y transforma una contradicción en un capítulo de resultados.
Requiere un ajuste menor de redacción en §17.3.9.2 del documento final.

### 4.2 Granularidad del patrón: escena vs. sujeto (el hueco de identidad)

§17.3.8.3.2 dice que la memoria del núcleo "puede organizarse **por fuente y
condición**, sin exigir identidad persistente de persona". La implementación, en
cambio, mantiene estado **por sujeto** usando `detection_id` del media-plane como
identidad — y ese id es un índice por frame (`det_000001`), no un track. Resultado:
la persistencia temporal por sujeto opera hoy sobre identidad rota (aliasing entre
personas en video real).

**Recomendación:** hacer explícitas dos granularidades en la definición de patrón:
- **G0 — nivel escena/fuente (núcleo):** "existe al menos una persona sin casco en
  esta fuente" con persistencia por fuente+condición. Coincide con lo que el
  documento ya declara para el núcleo, no requiere tracking, y es robusta. Cambio
  chico en el `PatternEngine` (clave de estado por `(pattern, source)` con conteo
  de sujetos en evidencia).
- **G1 — nivel sujeto (extensión condicionada):** requiere `track_id` estable
  emitido por el media-plane (tracker liviano IoU/centroid post-normalización,
  campo opcional aditivo en `media.detection.v1`).

Para la tesis alcanza con G0 en el núcleo + G1 demostrada en un clip si el tracker
liviano entra en agenda; si no, G1 queda especificada y justificada como extensión
(DA-06 ya lo prevé). Lo indefendible es el estado intermedio actual (G1 con
identidad falsa) — hay que resolverlo en el spec del control-plane.

### 4.3 El bus interno existe en el documento pero no en el código

DA-02/DA-03 y §17.3.8.4 asumen un bus de eventos separado del repositorio
persistente. Hoy: repositorio ✅ (JSONL por corrida), bus ✗ (acople por archivo).
La decisión tecnológica está bien diferida en Etapa 3, pero **Etapa 4 tiene que
fijarla ya**. Propuesta (detallada en el doc de integración del 2026-07-06):

- **DBE:** el "bus" se realiza como fuente directa in-process/archivo — el replay
  actual ya es conforme al diseño (el repositorio es la fuente de verdad).
- **EBE:** ZeroMQ PUB/SUB + msgpack con envelope versionado, reutilizando el patrón
  `transport/` ya construido para two-node. Publicador = decorador junto al
  `EventEmittingArtifactWriter`; consumidor = `BusSource` en el control-plane.
- **Kafka/broker: fuera del alcance de los 3 meses.** Documentar el seam (una
  implementación más de `BusPublisher`/`BusSource`) y justificar con DA-03: la
  durabilidad la da el log, el bus sólo transporta. Es coherente, defendible y evita
  un servicio pesado en la plataforma Docker/WSL.

### 4.4 Tres configuraciones sin paraguas: falta materializar `RunConfig`

El documento trata `RunConfig` como un artefacto único que gobierna ambos planos.
En la práctica hay tres configs (manifiesto experimental, run del media-plane,
replay del control-plane) sin un identificador que las una. La trazabilidad
"reconstruir la alerta hasta la configuración" (§17.3.11.1) hoy se corta en la
frontera entre planos.

**Recomendación:** materializar la corrida experimental como manifiesto paraguas en
`e-ovrt_experimental-setup` con un `experiment_id` que se propague a ambos planos
(el `RunSummary` del media-plane **ya tiene el campo** `experiment_id`; falta
agregarlo a los eventos del control-plane y al disparo de corridas). Costo bajo,
cierra la promesa central de trazabilidad del capítulo.

### 4.5 Ground truth temporal real: el mayor hueco experimental

Las métricas estrella del plano de control (TTFA/latencia de alerta, SDR, missed/
unexpected alerts) hoy sólo se validaron contra **un fixture sintético**. El BENCH
v2 da GT de detección por frame, pero no GT de **episodios** (persona sin casco
del t1 al t2 ⇒ alerta esperada). Sin clips reales anotados, el capítulo de
resultados del plano de control queda apoyado en simulación — el punto más débil
frente a un tribunal.

**Recomendación (empezar ya, es lo de mayor lead time):** *(✎ superada en
secuencia por ADR-010, 2026-07-09: el diseño quedó hecho —spec 43— y su ejecución
se dispara al cierre del spec 44 —experimental-setup: configs trazables + runner
+ reporte—; el armado del material crudo de videos, ya en proceso, y los trámites
—Intel, consentimientos— corren en paralelo)* construir un "clip bench"
de 8–15 clips cortos (10–60 s) desde el split DEMO o grabaciones propias, con GT
temporal débil por episodio (formato `ground_truth.json` ya definido en el
control-plane). Con eso, `evaluate-alerts` ya calcula precision/recall/F1/latencia
sin código nuevo. Es una tarea del repo datasets, paralelizable con todo lo demás.

### 4.6 Métricas: operacionalizar definiciones y cuidar los relojes

- En §17.3.13.1 la extracción de texto muestra **nombres de métrica vacíos**.
  CORRECCIÓN posterior (doc 08 §3): son objetos de ecuación de Word
  (`t_alert-system`, `t_alert-notification`) que la extracción automática no captura
  — en el Word original casi seguro se ven bien. Verificar visualmente al exportar a
  PDF, pero no tratarlo como errata confirmada.
- TTFD, SDR y T-alert necesitan **definición operacional** (evento t0, evento t1,
  unidad, ventana) en Etapa 4 — un diccionario de métricas de una página, cada una
  mapeada a las señales ya instrumentadas (`timestamp_ms`, transiciones, alertas).
- **Clock skew:** en EBE two-node, t0 (lectura en Nodo A) y t1 (confirmación en
  Nodo B/control) viven en hosts distintos. El documento no lo menciona. Definir:
  latencias por tramo intra-nodo + latencia end-to-end medida en un solo reloj
  (recepción), o sincronización declarada (chrony/NTP) con error estimado. Una
  frase en el spec evita una pregunta incómoda en la defensa.

### 4.7 Distribución de alertas: recortar el diseño de 2026-07-04

El diseño del módulo de distribución (ledger, retry, dead-letter, 4 canales,
dashboard propio) es bueno pero sobredimensionado para 3 meses. El documento sólo
exige (Tabla 48, §17.3.10.3): consumidores desacoplados, registro intento/resultado,
métrica separada. **Recorte propuesto:**
- **Un canal demostrativo** (Telegram para el efecto en la defensa, o MQTT por
  simplicidad — elegir uno) + `NotificationEnvelope` + ledger de idempotencia simple.
- **Dashboard de inspección: no construir uno nuevo** — extender la webconsole
  existente para listar alertas/episodios (lee `alerts.jsonl` o se suscribe al bus).
- Retry/dead-letter: política mínima (N intentos, registro), sin más.

### 4.8 Erratas y consistencia del documento (para la versión final)

- Varias figuras sin numerar ("Figura x") y títulos de tabla pegados
  ("Tabla 44Elementos…", "Tabla 51Hechos…", "Tabla 53…", "Tabla 58/59…").
- Oración duplicada en §17.3.15 ("La definición de estos roles no implica…" aparece
  dos veces seguidas con variantes).
- Los nombres contractuales del capítulo (PerceptionEvent, RunConfig, FrameMetadata)
  difieren de los reales del código (`media.detection.v1`, manifiesto, `VisualUnit`).
  Es legítimo (son "denominaciones contractuales preliminares"), pero Etapa 4 debe
  incluir la **tabla de correspondencia contrato-preliminar ↔ artefacto real** —
  refuerza la coherencia diseño→implementación ante el tribunal.
- `cooldown` figura en la Tabla 44 pero no existe en el motor; o se agrega el
  parámetro (trivial) o se quita del texto. **✎ Resuelto 2026-07-09 (dos vueltas):**
  la rama `mati` lo implementó en el motor, y luego ADR-011 lo reubicó — el redline
  correcto para la Tabla 44 es declararlo **parámetro del tramo de distribución**
  (`notification_policy.cooldown_ms`, spec 45 §6), no de la evaluación de patrones.

## 5. Recorte de alcance propuesto (must / should / won't)

**Must (sin esto no hay tesis):**
1. Corrida DBE end-to-end real: media-plane → control-plane sobre detecciones reales, con reporte consolidado.
2. Clip bench con GT temporal + evaluación de alertas sobre clips reales (§4.5).
3. Bus ZeroMQ media→control + corrida EBE end-to-end (RTSP, two-node) con alertas en vivo.
4. Experimento E-DIR vs E-IND (§4.1) y calibración de umbrales/regiones con datos reales.
5. `experiment_id` paraguas + diccionario de métricas + estados de aplicabilidad en el reporte.
6. Un canal de distribución + vista de alertas en webconsole.

**Should (si la agenda acompaña):**
- Cooldown y refinamientos menores del motor. *(✎ 2026-07-09: el cooldown se
  implementó en la rama `mati` y luego ADR-011 lo reubicó — es política de
  notificación del módulo de distribución, no refinamiento del motor.)*

**Won't — ACTUALIZADO 2026-07-07:** por decisión del usuario, el proyecto implementa
el núcleo validable y se detiene ahí. Todas las exclusiones (CR-03…06, MOT/G1,
fine-tuning/TN, broker, canales extra, borde/EN-2, zonas, etc.) quedaron cerradas
formalmente en `10-registro-alcance-y-exclusiones.md`, cada una con estado,
justificación anclada en las reglas del informe, rastro documental y frase de
declaración. G1/tracker, que figuraba aquí como "should", pasó a exclusión E-03
(especificada, no implementada).

## 6. El norte: cuatro resultados defendibles

La tesis se sostiene sobre cuatro resultados, cada uno mayormente apoyado en
infraestructura ya existente:

- **R1 — Benchmark DBE de modelos OVD** en seguridad de obra (BENCH v2, 5 modelos,
  AP@0.5/recall CR-01): **ya está** (Sprint 2). Sólo falta redactarlo como resultado.
- **R2 — Estudio de estrategia de detección y sensibilidad al prompt** (E-DIR vs
  E-IND, variantes de formulación): convierte la contradicción de §4.1 en aporte.
- **R3 — Cadena completa trazable con métricas temporales** sobre clips reales:
  detección → patrón → alerta interna, con TTFD/T-alert/SDR, precision/recall de
  alertas y reconstrucción causal de un episodio (demo de trazabilidad).
- **R4 — Viabilidad operativa EBE** en topología two-node (EN/CPN) con RTSP:
  latencia por tramo, FPS efectivo, descartes, alerta en vivo + notificación.

## 7. Plan indicativo de 12 semanas

> **✎ Re-secuenciado 2026-07-09 (ADR-010):** el proyecto corre en dos tramos —
> **plataforma primero** (servicios, bus, config centralizada, trazabilidad,
> instrumentación: specs 40–42/44/45), **evaluación después** (spec 43 + Fase 2 de
> D1 + R3 + calibración final). Las filas de este plan valen como dependencias,
> no como semanas literales, para los ítems de clip bench y campañas.

| Semanas | Foco | Entregables |
|---|---|---|
| 1–2 | Cierre de decisiones + Fase 0 | Specs Etapa 4 por módulo (ver §8); corrida DBE real end-to-end; `experiment_id`; inicio del clip bench (selección de clips). |
| 3–4 | Experimentos DBE | Clip bench anotado; E-DIR vs E-IND sobre BENCH; calibración de umbrales/regiones; decisión G0/G1 implementada. |
| 5–6 | Bus + streaming | Publisher ZeroMQ en media-plane, `BusSource` + runtime live en control-plane; paridad replay↔stream verificada con el fixture. |
| 7–8 | EBE + distribución | Corrida EBE two-node end-to-end con alertas; canal de notificación; webconsole con vista de alertas; medición de latencias con criterio de relojes. |
| 9–10 | Campaña experimental | Corridas finales R1–R4 congeladas, tablas y figuras de resultados; nada de features nuevas. |
| 11–12 | Escritura + defensa | Capítulos Etapa 4/5 y resultados; erratas de Etapa 3 (§4.8); demo ensayada (DBE replay + EBE en vivo); buffer. |

Regla de oro para el tramo final: **después de la semana 8 no se agrega capacidad,
sólo se corre, se mide y se escribe.**

## 8. Specs a escribir ahora (uno por módulo, cortos, con las decisiones cerradas)

> **✎ 2026-07-09 — ESCRITOS.** Los seis specs están en `specs/` (serie 40, ver su
> README); esta lista queda como insumo histórico. Ajustes posteriores a esta
> lista: el "cooldown" del punto 3 se reubicó al tramo de distribución (ADR-011)
> y el orden de ejecución es plataforma-primero (ADR-010).

1. **Plataforma / Etapa 4 (integrador):** mapa contrato-preliminar↔artefacto real;
   bus ZeroMQ (envelope, topics, END/run_finished); `experiment_id`; criterio de
   relojes; diccionario de métricas con estados de aplicabilidad.
2. **media-plane:** `BusPublishingArtifactWriter`; `track_id` opcional (si entra G1);
   propagación `experiment_id`.
3. **control-plane:** `MediaEventSource` (jsonl/memory/bus); runtime live;
   granularidad G0 (+G1 condicionada); cooldown; TTFA en métricas; reporte con
   estados de aplicabilidad.
4. **datasets:** clip bench (selección, formato GT temporal, procedimiento de
   anotación, tamaño objetivo 8–15 clips).
5. **experimental-setup:** manifiesto paraguas de corrida; webconsole: vista de
   alertas/episodios; definición de campañas E-DIR/E-IND.
6. **distribución:** versión recortada del diseño 2026-07-04 (un canal + ledger,
   dashboard→webconsole).

## 9. Decisiones a tomar ya (bloqueantes de los specs)

> **2026-07-09 — TODAS RESUELTAS** (decisión del usuario, formalizadas en
> `decisiones/ADR-001…011`). Los specs quedan desbloqueados (y escritos, ver §8).

1. ~~¿Se invierte la estrategia del núcleo a E-IND con E-DIR como variante?~~ —
   **SÍ (ADR-001)**; el experimento del doc 04 corre igual y cuantifica.
2. ~~¿Granularidad G0 como núcleo y G1 condicionada?~~ — **SÍ, con G1 demostrativa
   (ADR-002)**: tracker de la rama `mati` portado al media-plane, sin métricas MOT.
3. ~~¿Canal de distribución demostrativo: Telegram o MQTT?~~ — **MQTT (ADR-005)**,
   módulo en repo propio.
4. ~~¿Semántica de corrida del control-plane en EBE: 1:1?~~ — **SÍ (ADR-007)**;
   ventanas propias quedan como trabajo futuro declarado.
5. ~~Confirmar el "won't" de fine-tuning/TN~~ — **RESUELTO 2026-07-07**: exclusión
   formalizada como E-04 en `10-registro-alcance-y-exclusiones.md` (razón: presupuesto
   de tiempo, no falta de recursos ni de datos — Mendieta y el split train_v2 ya
   están disponibles; protocolo comparativo completo dejado especificado).
   (✎ 2026-08-11: el "won't" quedó **superado por ADR-017** — E-04 se ejerce como
   jornada experimental comprometida, y la razón "presupuesto de tiempo" está
   derogada como encuadre.)
