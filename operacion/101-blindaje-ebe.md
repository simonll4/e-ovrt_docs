# 101 — Blindaje de EBE: auditoría del cierre, irregularidad del descarte live y verificación por decimado empírico

**Fecha**: 2026-08-05 · **Disparador**: pregunta del usuario mientras el lote de
internet está en CVAT — *"¿los resultados de EBE son lo mejor que podemos obtener?
¿probamos las dos familias de modelos de manera completa? ¿vale la pena volver a
juntar al equipo para recrear escenas y correr pruebas nuevas de realtime?"*

**Veredicto en una línea**: EBE está cerrado de forma defendible; las dos familias se
probaron hasta donde cada una lo justificaba con causa medida; **un re-rodaje no
cierra ningún hueco real** — y los dos refuerzos que sí valían la pena se ejecutaron
en este doc **sin cámara ni equipo**: la irregularidad del descarte live quedó
**medida** (F-101.1) y las conclusiones del eje de densidad quedaron **verificadas
contra esa irregularidad** (F-101.2/3/4). Queda un opcional ejecutable en solitario
(humo claqueta, §5).

---

## 1. Auditoría del análisis contra los docs

Cada afirmación del análisis se verificó contra su fuente. Resultado: **todo
verifica, con UNA corrección de precisión** (abajo).

### 1.1 Los cuatro planos de EBE y su estado (con fuente)

| Plano | Estado | Fuente |
|---|---|---|
| Integridad del acople | cerrado sin residuo: paridad byte-idéntica, `bus_dropped_events = 0` en las 6 corridas del rodaje + L0 + regresión post-cambios | docs 37/65/67/71/91; `results/realtime/index.md` §1 |
| Latencia operativa | medida con hardware real: GDINO fuera de presupuesto (p95 630–890 ms), YOLOE dentro (225–249 ms) pero inservible para la condición | doc 71 §2.1; índice §2 |
| Techo de throughput | diagnosticado (F-RT3: GIL), palanca única aplicada (F-RT5: 3,75→4,42 fps, p=0,0195), las demás descartadas con números (<15%) | docs 73/74; índice §3 |
| Calidad bajo tiempo real | R1–R6 con bootstrap pareado (F-96.4 central); límite declarado: decimado regular | doc 96; **este doc lo cierra** |

### 1.2 Cobertura de las familias de modelos

- **GDINO (familia núcleo): completa.** `tiny-560` corrió todo: Nivel B (T1/D1/H1/G1),
  eje de densidad (R1–R6), las corridas live del rodaje y los humos EBE.
  `base-560` tiene Nivel B completo (T2 doc 84, B1 doc 88).
- **YOLOE: completa para el rol que podía cumplir.** Corrió EN VIVO en el rodaje
  (P1–P3, dentro de presupuesto) y quedó descartada para la condición con causa
  medida, no supuesta: `bare_head` recall 0,000 en el bench de imágenes, una CR-02
  falsa al 100% en vivo, alertas con tiempo corrompido, y **F-RT2** (su percepción
  intermitente viola la condición de estabilidad que exige la ventana temporal del
  motor — doc 71 §2.3/§2.5). Que no tenga campaña Nivel B es la salida *"no
  ejecutada con causa"* del pre-registro: un modelo que no puede expresar la
  condición no tiene nada que medir contra el GT de alertas.
- **MM-GDINO**: descartada en la selección de modelos (bboxes rotas; Sprint 2,
  consolidado en la selección S1/S2 del doc 64).

### 1.3 Corrección encontrada por la auditoría (precisión de cita)

**`gdino-base-560` NO tiene latencia live medida.** Lo que el doc 61 midió en vivo
(RTSP y OAK-D reales) fue **`gdino-base` a 800 px**: G2A p50 311–388 ms / p95
446–614 ms — fuera del presupuesto 50–250 ms (doc 61, hallazgo 2). El **−24%** de
latencia de la variante 560 es **inferencia de `tiny-560` sobre el BENCH** (D-61.4),
no una medición live de base-560. **La conclusión no cambia**: aun proyectando −24%
sobre el G2A de base-800, no entra en presupuesto (y la reducción sobre G2A es menor
que sobre inferencia pura, porque G2A incluye overhead no-modelo). Pero la cita
correcta es esa, y una corrida live nueva con base-560 no respondería ninguna
pregunta abierta: su calidad Nivel B ya se conoce (peor agregado que tiny, F-84.5;
CR-02 mucho mejor, F-84.6).

### 1.4 Por qué el re-rodaje no cierra ningún hueco

| Hueco declarado (índice realtime §7) | ¿Lo cierra re-rodar? | Qué lo cierra |
|---|---|---|
| Campaña EBE por el bus **contra GT** (34 clips) | No — el bloqueo es el **ancla wallclock↔media** (docs 54 §5.8, 55, 58), que es ingeniería. El rodaje además YA ejecutó el protocolo de doble toma del doc 58 (toma grabada→GT + corridas live sin GT) | resolver el ancla + receta de streaming |
| Descarte live irregular vs decimado regular | No hace falta — los artefactos ya estaban en disco | **CERRADO en este doc** (§2–3) |
| Tracker en obra real con multitud | No — otra escena guionada sigue siendo L4 | lote de internet / obra real |
| FAR/hora | No — cerrado por determinación D-90.1 (limitación, no métrica) | nada en esta tesis, por decisión |

Coincide con lo ya asentado en el doc 95: *"No hace falta volver a encender la
cámara ni juntar gente para el tramo de resultados."* Una sesión nueva tendría
además **peor** control que el material existente (degradación 2,4× intra-jornada,
doc 71 §4; deriva del host F-RT4 ±150 ms, doc 74) y todo GT nuevo pagaría el costo
CVAT que hoy es el cuello (doc 90 D-90.1: el clip de 6 min lleva >1 jornada).

---

## 2. F-101.1 — La irregularidad del descarte live, medida

**El hueco declarado** (doc 96 / índice realtime §7): las campañas R1–R6 deciman con
`stride` **regular**, pero el live descarta con **jitter** según lo que el consumidor
tome. Ese efecto no estaba medido. Se midió desde los artefactos existentes — los
`detections.jsonl` de **todas** las corridas live reales (`source_type: oak_d`) en
`e-ovrt_media-plane/runs/`: huecos entre `source.timestamp_ms` de frames procesados
consecutivos (script `datos/101-descarte-live-irregularidad.py`, artefacto
`datos/101-descarte-live-distribucion.json`).

| Grupo (modelo@jornada) | n huecos | media | ~frames@30 | fps | CV | p95 | max | frac ±50% mediana |
|---|---|---|---|---|---|---|---|---|
| GDINO rodaje (07-25) | 1.280 | 402 ms | **12,06** | 2,49 | **0,357** | 624 ms | 1.167 ms | 0,808 |
| GDINO post-F-RT5 (07-28) | 1.793 | 224 ms | 6,71 | 4,47 | 0,197 | 297 ms | 665 ms | 0,978 |
| GDINO humos doc 91 (08-05) | 338 | 243 ms | **7,28** | 4,12 | **0,221** | 332 ms | 559 ms | 0,956 |
| YOLOE rodaje (07-25) | 698 | 125 ms | 3,75 | 8,01 | 0,472 | 181 ms | 670 ms | 0,895 |

**Lecturas:**

- **El descarte live es moderadamente irregular, no caótico**: CV 0,20–0,36 para
  GDINO según el estado del host, con ~81–96% de los huecos dentro de ±50% de la
  mediana y colas hasta ~35 frames (1,17 s, rodaje). Las colas son exactamente lo
  que estresa a la histéresis (mecanismo F-96.2), de ahí la verificación del §3.
- **El ancla stride 7 de R1/R2 queda validada empíricamente**: la cadencia del
  camino live en su estado actual (humos 08-05, código de hoy) es **7,28 frames@30
  de hueco medio (4,12 fps)** — el doc 96 la había elegido por el rango 3,75–4,42
  de F-RT5, y la distribución real cae ahí.
- El grupo 07-23 (bench realtime, doc 61) tiene CV 0,90 — inflado por las corridas
  de warm-up con backlog que el propio doc 61 diagnosticó (hallazgo 1); no se usa
  como distribución de referencia.

---

## 3. Verificación por decimado empírico: ¿el jitter cambia las conclusiones R1–R6?

**Diseño** (runner `datos/101-decimado-empirico-runner.py`, contraste
`datos/101-decimado-empirico-contraste.py`): cuatro variantes sobre las detecciones
a 30 fps de T1 (bit a bit las de G1), cadenas de replay/evaluación idénticas a las
del doc 96, 34 clips, dos granularidades:

| Variante | Muestreo | Para qué |
|---|---|---|
| `s7dec` | regular stride 7 | **guard de equivalencia** contra R1 (que re-infirió) |
| `j7` | huecos empíricos 08-05 reescalados a media 7,0 (factor 0,962; CV 0,22 preservado) | jitter como variable única vs R1/R2 |
| `s12` | regular media 12 | control regular a la densidad REAL del rodaje (2,5 fps) |
| `j12` | huecos CRUDOS del rodaje (media 12,06; CV 0,36; sin reescalar) | jitter como variable única vs s12 |

**Guards, todos verdes:**

- **F-101.2 — decimado ≡ re-inferencia, verificado exacto en 34/34 clips**: decimar
  T1 a stride 7 reproduce las corridas de R1 con frames, timestamps y detecciones
  **idénticos**, y los 34 evals **idénticos campo a campo** (matched/missed/FP/
  re_alerts/P/R/F1). La técnica queda legitimada (es la misma que F-96.6 usó para
  el artefacto del SDR).
- Densidad realizada: j7 = 4,23 fps promedio (vs 4,29 de R1, −1,4%); j12 = 2,53 ≈
  s12 = 2,52 (pareo limpio). Guard por clip con umbral estadístico (±5% o 3·SE de
  la media, lo mayor — clips cortos tienen ~20–30 huecos).
- Sujeto: ninguna persona sin `track_id` en ninguna variante (el guard de G0
  silencioso del doc 89).
- Robustez: **3 semillas** de muestreo (101/202/303) para las variantes jitter.

### Resultados (semilla 101; multi-semilla abajo)

| Variante | fps ev. | Muestreo | Recall | Prec. | F1 | FP neg |
|---|---|---|---|---|---|---|
| R1 escena | 4,29 | regular | 0,794 | 0,794 | **0,794** | 0/4 |
| j7 escena | 4,23 | empírico CV 0,22 | 0,706 | 0,774 | **0,738** | 0/4 |
| s12 escena | 2,52 | regular | 0,735 | 0,781 | **0,758** | 0/4 |
| j12 escena | 2,53 | empírico CV 0,36 | 0,765 | 0,812 | **0,788** | 0/4 |
| R2 sujeto | 4,29 | regular | 0,853 | 0,879 | **0,866** | 0/4 |
| j7 sujeto | 4,23 | empírico CV 0,22 | 0,794 | 0,871 | **0,831** | 0/4 |
| s12 sujeto | 2,52 | regular | 0,824 | 0,933 | **0,875** | 0/4 |
| j12 sujeto | 2,53 | empírico CV 0,36 | 0,794 | 0,871 | **0,831** | 0/4 |

**F-101.3 — el jitter no produce un efecto detectable sobre el agregado.** Los 12
contrastes jitter−regular (2 densidades × 2 granularidades × 3 semillas, bootstrap
pareado por clip, 10k resamples) **cruzan todos el cero**, con signos mezclados
(escena@4,2: −0,048 a −0,108; escena@2,5: −0,030 a +0,048; sujeto en el medio). El
`t_alert` entre supervivientes comunes se mueve **+11 ms** (21 clips, j7 vs R1) y el
control de negativos da **0 FP de 4 en las 16 variantes**. Con n=30 positivos los IC
son anchos (~±0,1): "no detectable" no es "cero demostrado" — es el mismo estatus
que el doc 96 le da a los deltas de densidad del agregado. **El decimado regular de
R1–R6 queda verificado como proxy del descarte irregular del live a estas
densidades**: el hueco declarado del doc 96 pasa de "no medido" a "medido, sin
efecto detectable".

**F-101.4 — la ganancia de la identidad conserva el signo bajo jitter en 6/6
realizaciones; la significancia por-semilla se degrada, como corresponde a ruido
inyectado.** Sujeto − escena (bootstrap pareado):

| Densidad | Muestreo | Δ obs | IC 95% |
|---|---|---|---|
| 4,29 fps | regular (= F-96.4, IC canónico doc 96) | +0,072 | [+0,013, +0,145] **excluye el 0** |
| 4,23 fps | jitter, semillas 101/202/303 | **+0,092 / +0,132 / +0,060** | [+0,000,+0,196] / [+0,031,+0,252] / [−0,012,+0,162] |
| 2,52 fps | regular (control nuevo) | +0,117 | [+0,029, +0,219] **excluye el 0** |
| 2,53 fps | jitter, semillas 101/202/303 | **+0,043 / +0,012 / +0,042** | cruzan el 0 las tres |

Lectura honesta, en tres partes: (a) **F-96.4 queda como está** — su afirmación se
estableció bajo decimado regular y este doc no la re-litiga; el control regular
nuevo a 2,5 fps también excluye el cero (+0,117). (b) Bajo jitter la ganancia **no
se invierte nunca** (6/6 estimaciones puntuales positivas) y a la densidad de hoy
una semilla excluye el cero, otra lo toca y otra lo cruza — con este n, la potencia
no alcanza para separar cada realización individual. (c) **Matiz declarado**: a la
densidad del rodaje (2,5 fps) las estimaciones bajo jitter son consistentemente
menores que bajo decimado regular (+0,01..+0,04 vs +0,12), con IC que no separan la
diferencia. El mecanismo NO es fragmentación del tracker (97–103 tracks vs 103 de
R2). Si el informe cita F-96.4, la formulación segura es: *"la ganancia de la
identidad excluye el cero en las cuatro densidades bajo decimado regular, y conserva
la dirección bajo el descarte irregular medido del live (6/6 realizaciones
positivas, doc 101)"*.

---

## 4. Estado de EBE después de este doc

- ~~Irregularidad del descarte live~~ → **MEDIDA** (F-101.1) y su efecto
  **verificado** (F-101.3/4). El residuo teórico que queda es de segundo orden: el
  jitter real correlaciona con el contenido de la escena (más carga → más lento) y
  el muestreado es i.i.d.; declarado, no medido.
- **Campaña EBE por el bus contra GT (34 clips)**: sigue siendo el único upgrade
  real del eje, y es **ingeniería** (ancla wallclock↔media + receta de streaming),
  no rodaje. Con el proxy ahora verificado también contra el jitter, su prioridad
  baja aún más: solo ante una objeción concreta esperada del tribunal.
- **Tracker en obra real con multitud**: sigue en L4; lo levanta el lote de
  internet, no un re-rodaje.
- **FAR/hora**: D-90.1, sin cambios.
- ~~Humo claqueta~~ → **CERRADO (§5)**: las **cuatro patas** verificadas con
  hardware real y reloj externo (ancla física +1.066 ms, onset = 1ª evidencia,
  política +142 ms, relojes con 4 ms de residuo, cadena completa 7.045 ms). Cierra
  el stretch que el doc 58 declaró diferible. De yapa: **F-101.8** (el presupuesto
  G2A se mide desde el dequeue, no desde el fotón — la latencia vidrio→alerta suma
  `capture_to_host`, hoy 1,6 s contra 104 ms en el doc 91) y **F-101.9** (un
  episodio no se cierra cuando el sujeto sale de cuadro), más cinco trampas
  operativas (F-101.5/6/7) y cuatro guards verificados en los dos sentidos.

**Respuesta a la pregunta del usuario**: sí, los resultados de EBE son lo mejor
obtenible con este host y este material — el techo de fps tiene causa diagnosticada
y palanca única aplicada; la calidad bajo restricción está medida y ahora verificada
contra la irregularidad real; y las dos familias están cubiertas hasta su punto de
descarte con causa. **No hace falta juntar al equipo**: ninguno de los huecos
restantes se cierra con escenas recreadas.

---

## 5. Humo claqueta: qué quedó verificado y las tres trampas nuevas

Objetivo: la identidad `t_alert-system = TTFD + t_capture→alert` (spec 40 §5.2.2),
stretch que el doc 58 declaró diferible y cuyo ancla el doc 67 §G2 ensayó a mano
(palmada ↔ `capture_wallclock_ms`: 222 ms). Herramientas:
`datos/101-claqueta-smoke.py` (captura) + `datos/101-claqueta-verificar.py`
(verificación), separadas a propósito para poder iterar el análisis sin volver a
filmar.

### 5.1 Lo que la descomposición verifica de verdad (y lo que es álgebra)

Hallazgo de método, encontrado al escribir el verificador: **el residual de la
identidad es algebraicamente 0** una vez que se usa el mapeo wallclock↔monotónico
que el propio `metrics.jsonl` provee (`capture_wallclock_ms` +
`capture_monotonic_ns` por unidad). Reportar "residual = 0 ms" como si fuera un
resultado sería vacío. Lo que sí tiene contenido empírico son cuatro patas
independientes, y **dos ya quedaron verificadas sin filmar nada nuevo**, sobre los
artefactos del humo live del doc 91:

| Pata | Instrumento | Resultado |
|---|---|---|
| **C) Política** | control-plane | `alert_registered − first_evidence` = **4.082 ms** contra `confirm_after_ms` 4.000 (CR-01, +82 ms) y **7.068 ms** contra 7.000 (CR-02, +68 ms). Consistente con los 4,1–4,6 s del doc 71 |
| **D) Relojes entre procesos** | media + control | `alert_registered_ms` (monotónico del **control**) − `capture_monotonic_ns` (monotónico del **media**) = **+256 ms**, contra un G2A de **255 ms** de ese frame → **1 ms** de residuo. **Comparten base monotónica**, que es justo el supuesto del que cuelga la identidad del spec |
| **A) Ancla física→estampa** | reloj externo | **CERRADA con la toma anclada del 17:33** — ver §5.4/§5.5 |
| **B) Onset observado = 1ª evidencia del motor** | previews + control | verificada en el doc 91 (`frame_000012`) y de nuevo en la toma anclada (`frame_000060`, con confirmación visual) |

La pata D es el resultado más valioso de esta sección: sin ella, sumar un tiempo
del media-plane con uno del control-plane no estaría justificado. Las cuatro patas
quedaron cerradas el mismo día (§5.4).

### 5.2 Tres trampas nuevas, todas medidas hoy

- **F-101.5 — la fuente OAK-D no cierra de forma cooperativa y se lleva el proceso
  puesto.** Tras `request_stop()` el productor no manda END ("ventana de drenaje
  agotada... posible fuente colgada") y después el hilo monitor de depthai cierra
  el device y lanza `std::system_error` **desde un hilo no-Python** →
  `std::terminate` → **SIGABRT: el media-plane muere**. Es la misma familia que la
  trampa no negociable de ZeroMQ (docs 37/68) con otro culpable. Ocurrió al parar
  la **segunda** corrida OAK-D de la misma vida del servicio. Mitigación adoptada:
  **una sola corrida OAK-D por vida del servicio**, y el script ya no exige que el
  media siga vivo para cerrar — los artefactos se salvan igual porque
  `detections.jsonl`/`metrics.jsonl` se escriben incrementalmente y `alerts.jsonl`
  lo escribe el control-plane, que sobrevive.
- **F-101.6 — el device crashea y reconecta, y el ping ICMP miente (variante
  nueva).** En la primera toma el log del servicio muestra **tres ciclos** de
  `ping was missed, closing the device connection` → `Device likely crashed but did
  not reboot in time` → `OAK-D no disponible (intento 1/12): sin frames durante 10s
  con la conexión abierta`. Efecto sobre los datos: **dos huecos de 41,4 s y 40,2 s**
  con mediana de 309 ms, y `capture_to_host_ms` de 5–12 s al arranque (el host
  drenando frames capturados segundos antes). **Al mismo tiempo el ping ICMP daba
  0% de pérdida, ttl=64 y jitter de 0,14 ms.** La memoria ya tenía "el ping miente"
  por el gateway en NAT; **ésta es otra**: la pila de red del PoE responde con la
  aplicación del device caída. Remedio: **power-cycle de la OAK-D**.
- **F-101.7 — el status en vivo del media-plane no trae `units_processed`.**
  Mid-run, `GET /api/runs/{id}` devuelve solo
  `{run_id, name, status, started_at, model, live}`; `units_processed` aparece
  recién en el `summary` al cerrar. Cualquier script que espere frames leyéndolo de
  ahí concluye **"la cámara no entregó frames" con la cámara funcionando perfecto**
  (el probe que lo destapó procesó 102 unidades). La señal correcta es contar
  `detections.jsonl`, que se escribe incrementalmente. El script del doc 91 no lo
  sufría porque leía el progreso del **control**-plane.

### 5.3 Guard de contaminación (lo que impide reportar basura plausible)

La primera toma **produjo números completos y plausibles que estaban mal**: con el
device crasheando, CR-01 "confirmó a 7.828 ms" contra una política de 4.000 — eso
mide el stall, no la política. Es exactamente el modo de falla que el proyecto
combate con guards (la lección del `no_track_id` de G1). Implementado en
`101-claqueta-verificar.py`: aborta con exit 3 si el hueco máximo supera
`max(5× mediana, 3 s)` o si `capture_to_host_ms` p95 > 2 s, e imprime el remedio.

**Verificado en los dos sentidos**, que es lo que hace útil a un guard: exit **3**
sobre la toma contaminada (hueco 41,4 s, `capture_to_host` p95 7.312 ms) y exit
**0** sobre el humo limpio del doc 91 (CV 0,211, `capture_to_host` 104 ms).

### 5.4 La pata A CERRADA: el ancla física, y cómo se resolvió el problema del cue

**El obstáculo no era la cámara: era que el operador está frente a la cámara y no ve
la terminal del agente**, así que una cuenta regresiva impresa no le llega. Se
resolvió haciendo **hablar a la PC**: WSL invoca `powershell.exe` y usa
`System.Speech` + `[console]::beep` para guiar al operador por los parlantes del
host. Precisión del ancla: PowerShell espera hasta un **instante absoluto** y
**devuelve por stdout el wallclock real en que sonó el tono** — así el ancla es un
instante medido y no una estimación afectada por el arranque del proceso ni por la
duración variable del habla. Desvío medido: **−1 ms** respecto del programado
(+11 ms en las dos tomas previas).

**Toma final: 2026-08-05 17:33, `run_20260805_173354…780a1c` +
`smoke_claqueta_20260805T173350Z_b9c64e`.** Calidad de instrumento: 193 unidades,
cadencia 3,60 fps con **CV 0,016** (la más regular medida en todo el proyecto), sin
stalls. Las cuatro patas:

| Pata | Medición | Veredicto |
|---|---|---|
| **A) Ancla física→estampa** | tono → captura del **fotón** = **+1.066 ms**, con `capture_to_host` de 1.650 ms en ese frame | ✅ chico y positivo = reacción humana + cuantización de frame (275 ms) + lo que tarda el cuerpo en entrar lo suficiente |
| **B) Onset observado = 1ª evidencia del motor** | ambos en **`frame_000060`** | ✅ coinciden. Confirmado visualmente: el preview muestra **un pedazo de hombro entrando por el borde**, `person 0.39` — el instante real de la entrada, con el cuadro vacío antes (14 frames) |
| **C) Política** | `alert_registered − first_evidence` = **4.142 ms** vs `confirm_after_ms` 4.000 | ✅ +142 ms, dentro del rango 4.100–4.600 del doc 71 |
| **D) Relojes entre procesos** | control − media = **+166 ms** vs G2A **162 ms** | ✅ **4 ms** de residuo: comparten base monotónica |
| **E) Cadena completa contra reloj externo** | tono → alerta = **7.045 ms** = 2.716 (TTFD externo) + 4.329 (captura→alerta) | ✅ cierra |

### 5.5 F-101.8 — el presupuesto G2A se mide desde el DEQUEUE, no desde el fotón

Hallazgo de la pata A, y el más relevante de esta sección para el informe. Leyendo
`OakDSource`: `capture_to_host_ms = dai.Clock.now() − msg.getTimestamp()` (la edad
real del frame al salir de la cola; timesync PoE <0,5 ms) y `capture_wallclock_ms`
se estampa con `time.time()` **en ese mismo momento**. O sea:

> `capture_wallclock_ms` es el instante de **dequeue en el host**, no el de captura
> del fotón. El wallclock del fotón es `capture_wallclock_ms − capture_to_host_ms`.

Consecuencia: **el presupuesto G2A de 50–250 ms (spec 40) no incluye el backlog de
cámara/transporte.** La latencia vidrio→resultado es `capture_to_host + G2A`, y
`capture_to_host` **varía un orden de magnitud con el estado de la fuente** (medido
sobre los `metrics.jsonl`, medianas por corrida): **202–217 ms en las 6 corridas del
rodaje**, **169 ms** en el humo del doc 91, y **1.600 ms constantes** en las tomas de
hoy — mismo config `fps: 30`, con huecos perfectamente regulares de 275 ms, o sea
régimen estacionario de cola, no un stall. Es consistente con el doc 61 hallazgo 5
("el cuello es la fuente, no el modelo").

**Implicación para los números ya publicados: ninguna que los invalide.** Durante el
rodaje el término era chico y estable (~0,21 s), así que la lectura del doc 71
("GDINO fuera del presupuesto G2A, YOLOE dentro") se sostiene; solo hay que sumarle
~0,21 s si se quiere hablar de vidrio→alerta. Lo que hoy agrega es la advertencia:
ese término **puede ser 1,6 s** según el estado de la fuente, está instrumentado por
frame, y el informe no debe presentar G2A como latencia vidrio→alerta sin declararlo.

**La pata A es la validación física de ese campo**: si `capture_to_host` mintiera, la
resta tono→fotón daría negativa o absurda; dio +1.066 ms, que es exactamente el
orden de una reacción humana. **Está instrumentado por frame, así que es declarable,
no un hueco** — pero el informe no debe presentar el G2A como latencia
vidrio→alerta sin sumarle este término.

### 5.6 F-101.9 — un episodio no se cierra cuando el sujeto sale de cuadro

Descubierto al fallar la segunda toma. Con el sujeto en cuadro al arrancar se abrió
un episodio CR-01 que confirmó a los 4 s; el sujeto salió **más de 5 s** (contra
`resolve_after_ms: 2000`) y volvió a entrar, y **no se generó ninguna alerta nueva**:
la única alerta seguía en `state: open` con `first_evidence: frame_000000`.

Lectura (inferencia del comportamiento observado, no leída en el código del motor):
**la ausencia del sujeto no es evidencia de cumplimiento**, así que la ventana de
resolución no corre y el episodio queda abierto. Es coherente con el diseño —el
motor no puede declarar "ya cumple" sobre alguien que no ve— pero tiene dos
consecuencias prácticas que conviene declarar: en operación real, una persona que se
va de la escena **deja su episodio abierto**; y para cualquier toma anclada, **la
corrida tiene que empezar con el cuadro vacío** (si no, la reentrada no produce la
alerta anclada). El script ahora pide salir de cuadro **antes** de arrancar el media
y el verificador rechaza con exit 5 las alertas no ancladas.

### 5.7 Los guards, que son la mitad del resultado

Tres tomas, tres modos de falla distintos, cada uno convertido en un guard
automático. Ninguna de las tres habría sido detectable a ojo: **las tres produjeron
números completos y plausibles**.

| Toma | Falla | Guard que la caza | Exit |
|---|---|---|---|
| 17:14 | device crasheando (F-101.6): huecos de 41 s | hueco máx > max(5× mediana, 3 s); `capture_to_host` **creciente** | 3 |
| 17:26 | el operador entró **1,1 s antes** del tono (reaccionó al "tres, dos, uno") | ventana previa al tono debe estar **sin `person`** | 4 |
| 17:30 | alerta **pre-tono** (F-101.9): la corrida arrancó con el sujeto en cuadro | la alerta analizada debe tener su 1ª evidencia **después** del tono | 5 |
| **17:33** | — | los tres pasan | **0** |

Los guards se verificaron **en los dos sentidos** (rechazan las tomas malas y
aceptan las buenas: exit 0 sobre el humo limpio del doc 91 y sobre la toma final).
El criterio de `capture_to_host` distingue explícitamente **cola estacionaria alta**
(1.650 ms constantes: régimen legítimo, se declara) de **cola creciente** (backlog
drenándose: frames no contemporáneos, contamina).

Además, un guard operativo del propio script: **espera a que los datos confirmen el
cuadro vacío** antes de armar el tono (5 s sin `person`, por encima del
`resolve_after_ms` de 2 s), en vez de pedirlo por voz y suponer que pasó.

---

## 6. Procedencia

| Qué | Dónde |
|---|---|
| Medición de irregularidad | `datos/101-descarte-live-irregularidad.py` → `datos/101-descarte-live-distribucion.json` |
| Runner del decimado empírico (guards a/b/c) | `datos/101-decimado-empirico-runner.py` → `datos/101-rt-*/` (16 dirs: 4 variantes × 2 gran. + semillas 202/303 de j7/j12; cada uno con `resultados.json`, `evals` `eval_*.json`, `metrics.json` del agregador testeado del banco) |
| Contraste + bootstrap pareado (semilla 96→101, 10k) | `datos/101-decimado-empirico-contraste.py` → `.log` + `.json` |
| Log de la campaña | `datos/101-decimado-empirico.log`, `datos/101-decimado-seed{202,303}.log` |
| Humo claqueta: captura (guía por voz vía interop WSL→PowerShell) y verificación (4 guards, exits 3/4/5) | `datos/101-claqueta-smoke.py` + `datos/101-claqueta-verificar.py` |
| **TOMA FINAL anclada (las 4 patas)** | `e-ovrt_media-plane/runs/run_20260805_173354_dbe_grounding_dino_780a1c` + `e-ovrt_control-plane/runs/smoke_claqueta_20260805T173350Z_b9c64e` + `datos/101-claqueta-{captura,verificacion}.json`; preview del onset: `previews/frame_000060.preview.jpg` |
| Tomas descartadas por los guards (evidencia de F-101.6 y F-101.9) | `run_20260805_171426…0c2cbe` (device crasheando), `run_20260805_172632…f4fc5f` (entrada anticipada), `run_20260805_173014…376f78` (alerta pre-tono) + log del servicio |
| Patas C y D, primera verificación (sin filmar nada nuevo) | artefactos del doc 91: `run_20260805_003533…3246e1` + `smoke_ebe_a_20260805T003533Z_1593d8` |
| Insumos | T1: `results/clip_bench/t1_.../provenance.json` (34 media runs 08-03); R1/R2: `results/clip_bench/r{1,2}_...` (doc 96); corridas live: `e-ovrt_media-plane/runs/` (`source_type: oak_d`) |
