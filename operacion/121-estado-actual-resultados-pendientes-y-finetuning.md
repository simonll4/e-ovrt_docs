# 121 — Estado actual: resultados, qué falta ejecutar, fine-tuning por familia y datasets (2026-08-15)

> ⚠ **REEMPLAZADA COMO FOTO DE ESTADO (2026-08-21).** La foto vigente es
> [`operacion/128`](128-acta-cierre-programa-experimental.md) — acta de cierre del
> programa experimental. Este doc sigue siendo válido como registro del 08-15, pero sus
> §2/§3 sobre fine-tuning quedaron superados por los cierres T1 (`123`) y T2 (`127`).

- **Qué es esto:** una foto de una pasada del estado real del proyecto en tres ejes —
  **resultados medidos**, **qué queda por ejecutar** (con la verificación explícita del
  frente de cámaras/realtime) y **fine-tuning por familia + datasets**. Sirve para decidir
  qué se hace y qué no antes de la defensa.
- **Método:** todo lo de acá se verificó contra el repositorio el 2026-08-15 (índices de
  `results/`, manifiestos, registry, código y verificadores). Ninguna fila se escribió de
  memoria — regla heredada del doc 119.
- **Estado en una línea:** **el tramo experimental está completo y verificado**; lo que
  queda abierto es (a) **un smoke de cámara opcional** que no altera ninguna cifra, (b)
  **dos ejes de ingeniería ubicados y no ejecutados**, y (c) **la jornada de fine-tuning**,
  cuyo T1 quedó a un solo paso — el `RUN` manual del usuario.

---

## 1. Resultados — qué está cerrado

Los números viven en los **4 índices canónicos** de `e-ovrt_experimental-setup/results/`,
más la campaña de distribución. Verificación mecánica al día: `96-verificar-indices.py`
(exit 0), `109-verificar-organizacion.py` (exit 0), `113 --check` (exit 0),
`evidence_runs.py --check` (exit 0).

| Índice | Qué cierra | Cifra de cabecera |
|---|---|---|
| **`bench_imagenes/`** | Selección de modelos sobre `bench_v3` (6.477 imgs, 3 fuentes) | Campeón **`gdino-tiny-560`** (mAP50 obra **0,503**); `gdino-base-560` es el especialista CR-02 (vest AP **0,582**, recall CR-01 **0,400**); **YOLOE ciega a `bare_head` (AP 0,000 en las 4 variantes)** |
| **`bench_nivel_a/`** | Estado "sin EPP" por persona: E-DIR vs E-IND | El gate **no se dispara** (E-DIR pasa a Fase 2); complementariedad **18,5 % / 18,8 %** |
| **`clip_bench/`** | Alertas contra GT temporal humano — banco **47 clips / 37 episodios** | **E-IND núcleo F1 0,789 (T1)**; **G1 por sujeto F1 0,930 — el mejor del banco**, con las MISMAS detecciones; E-DIR **vetada por precisión** (0,146); E-HYB-or **refutada** (0,296) |
| **`realtime/`** | Camino en vivo: integridad, latencia, techo de fps, calidad bajo tiempo real | Bus íntegro; **el único modelo en presupuesto (YOLOE) es el que no ve la condición** — la tensión calidad↔latencia es hallazgo de primera línea |
| **`realtime/t_alert_notification/`** | Distribución `bus → PUBACK MQTT QoS 1` | **p95 64,534 ms (n = 460)**; sostenido 102,025 ms (n = 104) |

**Métricas de alertas: sin pendientes** (cerrado el 2026-08-15, doc 119 §7.3 y §8.1).
`t_alert-notification` está medida y es citable; **`t_alert-system` quedó materializada
como citable** — es la columna `t_alert` del clip bench (`t_alert_system_ms` de cada
`metrics.json`). Las tres métricas de alertas de `report.json`
(`precision_alertas`/`recall_alertas`/`F1_alertas`) están **emitidas y declaradas NO
citables**: duplican cifras que ya se publican por estrato.

**La cadena temporal se cita POR TRAMOS** (tabla en `results/index.md`): `capture_to_host`
202–217 ms → G2A por contexto → `t_alert-system` por campaña → `t_alert-notification`.
**Los percentiles no se suman entre tramos.** Lectura de conjunto: **la distribución no es
el cuello** (≈65 ms contra 630–890 ms del G2A live y 4–7 s de persistencia deliberada).

**Limitaciones canónicas L1–L8** cerradas y vigentes (`results/index.md`). Las que más
pesan al redactar: **L1** (FAR/hora se reporta pero no sostiene cota), **L4** (precisada,
no levantada, con el estrato B), **L8** (CR-02 a Nivel A no cerrada).

---

## 2. Qué falta ejecutar o completar

### 2.1 Runs de tiempo real con cámaras — **verificado, y la respuesta tiene matiz**

Se verificó explícitamente porque era la duda planteada. El resultado:

**El eje real-time está CERRADO SIN PENDIENTES** desde el 2026-08-05 (doc 101, veredicto
literal: *"EBE queda cerrado SIN pendientes"*). Los cuatro planos del índice
(`realtime/index.md`) están en ✅: integridad del acople, latencia operativa, techo de
throughput y calidad bajo restricción de tiempo real. **No hay una campaña de cámara
pendiente que cambie una cifra.**

Pero hay **una corrida con cámara que estaba prevista y NO se ejecutó**, y conviene tenerla
nombrada con precisión:

| # | Qué | Estado real | ¿Bloquea? |
|---|---|---|---|
| **F-118.3** | **Smoke de cámara de la campaña `t_alert_notification`** | **`not_executed: hardware_source_not_connected`** — ni OAK-D ni RTSP estaban conectadas ese día (`camera-smoke.json`) | **No.** Era validación *suplementaria*; nunca fue fuente de muestras del p95. El acople completo quedó validado **desde video** (3 repeticiones E2E: 116,839 / 152,901 / 91,588 ms). La indisponibilidad física **no se interpreta como evidencia negativa** |
| — | **Latencia live de `gdino-base-560`** | **No medida.** Lo medido en vivo fue `gdino-base` a **800 px** (G2A p50 311–388 / p95 446–614 ms); el −24 % de la variante 560 es inferencia batch sobre el BENCH, no live | **No.** El doc 101 §1.3 es explícito: *"una corrida live nueva con base-560 no respondería ninguna pregunta abierta"* — aun proyectando −24 % no entra en presupuesto. **Consecuencia a declarar:** T2 y B1 quedan **sin costo operativo live declarado** |

**Si querés cerrar el frente de cámaras del todo**, lo único ejecutable y con sentido es
**correr el smoke de cámara de F-118.3** (OAK-D o RTSP conectada + `POST /api/runs` con
`bus.enabled` + distribuidor suscripto). Costo: bajo. Ganancia: convierte un
`not_executed` en evidencia positiva del acople sensor→notificación. **No cambia el p95 ni
ninguna cifra publicada** — y por eso no está en la ruta crítica del informe.

> **Lo que NO hay que hacer: re-rodar.** El doc 101 §1.4 tiene la tabla de por qué ninguno
> de los huecos declarados se cierra re-filmando, y el doc 95 lo dice igual: *"No hace falta
> volver a encender la cámara ni juntar gente para el tramo de resultados."* Una sesión
> nueva tendría **peor** control (degradación 2,4× intra-jornada, deriva del host ±150 ms) y
> todo GT nuevo pagaría el costo CVAT, que es el cuello real.

### 2.2 Ejes DECLARADOS CON CAUSA — no son pendientes (✎ reencuadrado 2026-08-15)

> **Dos correcciones al encabezado original de esta sección**, que decía *"dos ejes
> ubicados y no ejecutados"* y se leía como deuda:
>
> 1. **Eran dos, es uno.** El *port de `track_id` al pipeline online* **no está abierto**
>    (ver el párrafo al pie): se citaba el §7 del doc 89, que el propio doc marca como
>    *"el planteo original de la decisión, que la implementación reencuadró"* (§6 bis), y
>    la adenda de ADR-002 quedó **RATIFICADA el 2026-08-05**.
> 2. **El que queda no es un "eje abierto": es un eje DECLARADO CON CAUSA**, del mismo
>    tipo que `hyb_and` (D-90.4), los 800 px o FAR/hora (D-90.1). Ver §2.3 — pertenece a
>    esa categoría, no a ésta.

**Queda un solo eje, y está declarado con causa:**

| Eje | Qué respondería | Estado y causa |
|---|---|---|
| **Campaña EBE de punta a punta por el bus sobre los 34 clips** | Integridad y latencia operativa **contra GT**, no en humos | **Declarado con causa, no pendiente.** El bloqueo técnico es el **ancla wallclock↔media**: `RtspSource` estampa wallclock (`rtsp_source.py:104`) y el GT de CVAT está en media-ms, así que `_alert_in_episode_window` (`temporal.py:303-310`) compararía epoch-millis contra `episode.start_ms`. Es **ingeniería**, no material. **Y el proyecto lo resolvió por diseño**: el *protocolo de doble toma* del doc 58 (Toma A grabada → GT; Toma B live → métricas sin-GT) se creó **exactamente para no necesitar el ancla** — *"cada plano mide lo suyo; nadie necesita el ancla"*. Hoy el eje se cubre por densidad (R1–R6, con el proxy verificado contra el jitter real en el doc 101) + humos live |

#### F-121.1 — por qué correrla NO produciría ningún resultado nuevo

Se evaluó formalmente el 2026-08-15 si convenía ejecutarla. **No.** El argumento es de
construcción, no de costo, y se deja escrito para que el eje no se reabra por olvido:

1. **El pipeline DBE es determinista y está verificado** (F-109.1: re-inferencia de 3
   clips → detecciones idénticas hasta la unidad, 284.189 = 284.189). Misma entrada ⇒
   mismas detecciones.
2. **El bus publica el evento ya persistido, byte-idéntico al del JSONL**
   (`service/bus_writer.py`: persiste primero y serializa *el mismo objeto*; invariante
   con gate de paridad replay↔stream **verificado por mutación** — doc 37 §3).
3. Mismo motor y mismo pattern set ⇒ **mismas alertas**.

**Conclusión: el resultado esperado es idéntico a T1 por construcción** (F1 0,789, los
mismos 28 matched / 6 missed / 9 FP). No agrega una fila a ninguna tabla: produce la
misma fila por otro camino.

**La única divergencia posible** es que el bus pierda eventos al llenarse el HWM — y eso
**se cuenta (`bus_dropped_events`) y degrada la corrida**, nunca sale un número
silenciosamente mal. Además, en DBE la presión sobre el bus es **menor** que en vivo
(publica al ritmo de la inferencia, no a 30 fps): sería un test de estrés **más flojo**
que los humos live que ya dieron `bus_dropped_events = 0`. Y las latencias no aportan:
con `source_clock: media` la plataforma declara `t_capture→alert` como
`not_interpretable / dbe_media_time` **por diseño** — mismo criterio que `report.py`
aplica a `wall_clock_dbe` (*"reloj de pared de un reproceso, no la métrica real"*).

**Por lo tanto no es un experimento, es un guard** — vale por lo que descartaría si
fallara, no por lo que mediría si pasa; y el modo de falla que buscaría ya tiene detector
propio. **Lo único que daría números nuevos** sería la variante cara: los 34 clips a **1×
real por RTSP** (G2A y recall contra GT en la misma corrida, con los frames que el sistema
realmente pierde). Requiere antes resolver el estampado de tiempo de medio en `RtspSource`
—hoy descarta el tiempo de presentación del stream—, **puede fallar** (OpenCV sobre RTSP
live suele no reportar `CAP_PROP_POS_MSEC` confiable), y su resultado sería
**confirmatorio del proxy R1–R6**, no un hallazgo independiente. **Decisión: no ejecutar**,
también por el freno de ADR-016 §2b a código nuevo cerca de la defensa.

**Lo que NO es un eje abierto — `track_id` (aclaración con evidencia):** la identidad por
sujeto **ya es capacidad de plataforma en los dos caminos**. Se implementó como
**decorador de fuente en el control-plane** (`sources/tracking.py`, activado por
`input.track_persons`, opt-in, default `false`), cableado en `runtime/replay.py` **y** en
`runtime/live.py` ⇒ **G1 corre en DBE y en EBE/live sin que el media-plane emita
`track_id`**. Verificado en vivo con la OAK-D (doc 91: la clave de estado pasa a
`CR-01:smoke_ebe:subject_001`, `bus_dropped_events=0`, sin `no_track_id`), y el camino
config-driven **reproduce la campaña G1 exacto en los 34 clips** (11 campos por clip,
SDR/TTFD incluidos). El port del spec 42 §3 sería una **decisión de arquitectura** —mover
el tracker al media-plane para embeber `track_id` en `detections.jsonl`—, con un
**trade-off ya declarado y aceptado** en la adenda: hoy la identidad vive en los
artefactos del control-plane (`subject_key` de `pattern_events.jsonl`) y quien necesite el
JSONL con `track_id` embebido lo genera con
`python -m eovrt_control.tools.track_detections`. **No es un pendiente de resultados.**

### 2.3 Cerrado CON CAUSA — no reabrir

*(La **campaña EBE por el bus** pertenece también a esta categoría desde el 2026-08-15;
se documenta arriba, en §2.2 + F-121.1, por su historia previa como "eje abierto".)*

Para que no vuelvan a aparecer como "pendientes" en una lectura futura:

- **`hyb_and`** — no ejecutable contra este banco sin romper la comparabilidad de las 6
  campañas (**D-90.4**).
- **Resolución 800 px sobre el banco temporal** — 560 domina a 800 en el bench; no
  ejecutada con causa.
- **FAR/hora** — **limitación declarada** (D-90.1, precisada), no métrica pendiente.
- **Sonda `machinery` en T1** — **derogada** por D-FT-13 (firmada 08-15); sigue exigible en
  T2/T3.
- **Tracker en obra real con multitud** — resuelto por el estrato B: `v06_c01` con 127
  personas en GT dio **182 identidades con FP** (F-103.2). Es un dato, no un hueco.

### 2.4 Pendientes que son del usuario, no técnicos

1. **C1 — URLs + fecha de acceso de los 18 `clip.yaml`** (evidencia perecedera; propagar y
   re-promover es delegable después).
2. **Video V2** de la defensa (V1/V3/VG1/VG1e listos).
3. **§17.x del informe** — no arranca hasta orden explícita. Además, el manual
   `informe/ajustes/08` tiene **3 decisiones tuyas en su §2** y **5 figuras por producir**.
4. **Git**: ~121 entradas sin commitear en 5 repos; y elegir archivo `LICENSE` por repo
   (único residual del hallazgo 3 de `gobierno/99`).

---

## 3. Fine-tuning por familia

**Encuadre invariante (ADR-017):** E-04 es una **rama experimental condicionada por datos y
protocolo desde el planteo**; la causa temporal está **prohibida**. Los resultados de la
rama van **rotulados como comparativos y en tablas propias**, nunca fundidos con el núcleo
zero-shot. La escalera **T1 → T2 → T3** está pre-registrada (D-FT-03) y cambiarla requiere
enmienda explícita.

### 3.1 Semáforo por familia

| Familia | Qué es | Estado al 2026-08-15 | Qué falta |
|---|---|---|---|
| **T1 — YOLOE-26s linear probing** | 12 tensores / 3.096 params entrenables sobre `finetuning_v1` | 🟢 **LISTO PARA EL RUN** | Sólo `full-authorization.json` + `RUN` manual del usuario |
| **T2 — YOLOE full fine-tuning** | Tabla 32 completa (Δ + retención generalista) | 🟡 **Condicionado** | Que T1 cumpla el go/no-go **y** que **D-FT-04** congele el subset y la métrica de retención *antes* de correr |
| **T3 — MM-GDINO open-vocabulary** | Fine-tuning OV en Mendieta sobre ODVG | 🔴 **No habilitado** | 10 ítems de su checklist; ver §3.4 |

### 3.2 T1 — a un solo paso

**Cerrado el 2026-08-15** (docs 119 §8 y 120): las tres decisiones humanas firmadas
(D-FT-08 contrato de serving, D-FT-12 go/no-go **pre-registrado antes de la baseline**,
D-FT-13 sonda `machinery`), y las gates técnicas ejecutadas — enforcement del vocabulario
canónico v2 en config, catálogo finetuned, **comando de evaluación congelado** y **baseline
YOLOE-26s one-shot** sobre las 6.477 imágenes.

**Lo que la baseline fijó** (cifras de la rama, por estrato en el doc 120):

- Vía de ganancia **abierta y exigible**: `bare_head` AP50 **0,000** (6.181 GT / 10 det) →
  el tuned necesita **≥ +0,05 absoluto**; recall CR-01 **0,0002** (≪ 0,1) → la vía del
  rescate exige **> 0,5**.
- Retención a proteger (≤10 % de caída relativa): person **0,7843** · helmet **0,6286** ·
  vest **0,2642** · mAP50 **0,4193**.
- **F-120.1**: las latencias de ese run **no** se citan (cambio batería→AC durante la
  corrida); el gate de latencia se medirá **pareado**, ambos brazos con corriente.

**Las 7 gates de `full-authorization.json` están cerradas**
(T-FT-005/023/026/030/031/032/042R). Tareas que restan, en orden:

| # | Tarea | Quién | Detalle |
|---|---|---|---|
| 1 | Emitir `full-authorization.json` | **usuario** | `prepare_t1_full_authorization.py`, token exacto `APPROVE_D_FT_08`, evidencia por archivo de las 7 gates; el verificador exige el inventario exacto |
| 2 | **T-FT-043** — `RUN` manual en Mendieta | **usuario** | 10 épocas, envelope 1 GPU / 10 CPU / 60 GB / 2 h. **Cero jobs full a la fecha** |
| 3 | T-FT-044 — monitorear y finalizar | delegable | `sacct`, logs, hashes, costo, transferencia |
| 4 | T-FT-050 — promover checkpoint | delegable | copia por hash al catálogo `yoloe-26s-ft-t1.yaml` (**ya preparado**) |
| 5 | T-FT-051 — eval única | delegable | `evaluate_t1_bench_v3.py --arm tuned` (una sola vez; `last.pt` nunca es segundo candidato) |
| 6 | T-FT-052 — aplicar go/no-go | delegable | con los márgenes **ya firmados** — no se negocian después de ver el resultado |
| 7 | Medición pareada de latencia | delegable | F-120.1: ambos brazos, misma sesión, con corriente, post-warmup |

> ✎ **2026-08-17 — las siete filas de arriba están CERRADAS (salvo la 7, descartada con causa).**
> La autorización se emitió (`gates=7`), el job `1167640` corrió (`COMPLETED`, 10/10 épocas) y la
> cadena T-FT-044/050/051/052 se completó: **veredicto D-FT-12 = NO-GO**
> ([doc 123](123-cierre-jornada-t1-no-go.md)). La fila 7 **no se ejecutó y no se va a ejecutar
> para este gate**: no es decisión-relevante (gain y retención ya fallan) y el brazo baseline no
> tiene latencias citables (F-120.1 → F-123.1). **Este bloque queda como histórico.**

**Pendiente del checklist doc 100 §6.2 que sigue en pie:** entorno reproducible en el
clúster (CUDA/torch) y transporte de las imágenes. El puente de evaluación **ya no falta**:
es el comando congelado.

### 3.3 T2 — qué hay que decidir antes de que sea ejecutable

No es un problema de cómputo: es **una decisión pre-registrada que falta**.

- **D-FT-04 (diferida)** — elegir **subset y métrica de retención** después del resultado
  T1 pero **antes** de ejecutar T2. La tabla de `contingencia/20` propone COCO val u
  OVDEval parcial.
- **Diferencia clave con T1:** la retención de T1 es **in-domain** (`person`/`helmet`/`vest`
  sobre `bench_v3`) porque D-FT-08 fija vocabulario cerrado. **T2 es donde recién se puede
  medir retención open-vocabulary generalista** — y por eso la erosión OV del ADR-017 §1.3
  está fuera del alcance medible de T1.
- **Dependencia técnica ya resuelta:** `pycocotools` (que bloqueaba la Tabla 32) quedó
  instalado el 2026-08-15.
- Costo estimado: 4–10 GPU-h · +2–3 días de pared.

### 3.4 T3 — el más lejos, y con un antecedente en contra

T3 (MM-GDINO-tiny open-vocabulary) tiene **tres decisiones diferidas** y un problema de
fondo:

- **D-FT-02** (variante GDINO), **D-FT-05** (salida: conversión HF vs adapter MMDetection) y
  **D-FT-06** (recursos distribuidos, batch/LR para la asignación real) siguen `diferidas`.
- **El antecedente pesa:** MM-GDINO fue **descartada empíricamente** en la selección de
  modelos — `tiny` con **bboxes degeneradas** y `large` con mAP 0,017. **T3 no puede ignorar
  ese hecho**: hay que resolverlo antes, no durante.
- **Datos:** el ODVG existe (`datasets/processed/odvg/canonical_v2/`, 4 fuentes) **pero no
  hay un payload ODVG anti-leakage derivado de `finetuning_v1`**. T3 debe entrenar con
  CSS + PPE Siabar únicamente — no con las 5.540 que incluyen CHV — y necesita **un monitor
  propio que no use `bench_v3`**.
- Checklist de "T3 listo para pedir GPU": **10 ítems, ninguno tildado**.
- Costo estimado: 8–24 GPU-h · 1–2 semanas de pared · **riesgo alto**.

> **Lectura honesta para la defensa:** si la escalera se respeta, **T3 sólo se habilita si
> T2 sostiene el resultado**. Pedir "un YOLOE y un GDINO" como corridas paralelas requiere
> **enmendar el protocolo explícitamente** — el estado vigente no lo habilita.

---

## 4. Datasets — estado

### 4.1 Lo que está cerrado

| Artefacto | Estado |
|---|---|
| **Vocabulario canónico v2** (`person`, `helmet`, `vest`, `bare_head`) | Vigente; 4 fuentes convertidas a `canonical_v2` (COCO/YOLO/ODVG) |
| **`bench_v3`** — bench de imágenes | **CONGELADO**: 6.477 imgs / 55.165 anotaciones, 3 fuentes estratificadas, sha256 por fuente. Inmutable por gate invariante |
| **`finetuning_v1`** — payload T1 | **Construido y auditado**: 3.429 imgs seleccionadas → **train 2.946 / val 483**, seed 42, split por grupos de linaje |
| **Cero leakage — verificado** | `bench_overlap_selected: 0` · `shared_components_train_val: 0` · `val_all_canonical_classes: true`; 781 imgs excluidas (56 por componente perceptual del bench, 25 por linaje, 700 por dedup) |
| **Licencias del payload** | CSS + PPE Siabar, **ambos CC BY 4.0** — compatibles con transporte al clúster |
| **Suite** | `datasets/tests/` **418 passed** |

### 4.2 Reglas que gobiernan y no se tocan

1. **Bench inmutable:** `bench_v3` no se copia, redivide, edita ni se usa para construir
   `val`.
2. **Sin leakage:** **CHV y SHEL5K no entran al fine-tuning** (ninguna familia), ni ningún
   linaje de CSS con variante en el bench.
3. **Split por grupo:** variantes de una misma imagen fuente y duplicados perceptuales
   nunca se separan entre train y val.
4. **Al clúster sólo material CC BY 4.0** — con **una excepción ratificada y retroactiva**:
   `mobileclip2_b.ts` (asset de modelo, `NOASSERTION`), firmada el 2026-08-15. La regla
   **sigue intacta para datos**.

### 4.3 Higiene del catálogo — ✎ **RESUELTA el 2026-08-15** (ya no queda nada abierto)

La primera versión de esta sección listaba cuatro ítems "abiertos". Se investigaron y
resolvieron los cuatro; **tres eran imprecisiones de este documento**, no problemas del
repositorio.

**(a) `splits/v2/` — ARCHIVADO ENTERO, no sólo `bench.txt`.** Al ir a archivar el BENCH
viejo apareció que el problema era mayor y distinto: **los tres roles estaban huérfanos**
(ningún script, config ni test del pipeline activo los consumía) y **`bench.txt` no era un
archivo suelto: lo regeneraba `build_role_views.py`**, listado como comando activo en el
`CLAUDE.md` del workspace. Archivar el artefacto sin su generador habría sido cosmético.
Se movieron los dos a `legacy/` (`legacy/splits/v2/` + `legacy/scripts/curate/`), con la
constancia y la tabla de supersesión en `datasets/splits/DEPRECATED.md`:

| Rol | Superado por |
|---|---|
| BENCH (196) | **`bench_v3`** (6.477 imgs, 3 fuentes, congelado) — el split viejo era ~20–25 % fuera de dominio (doc 63) |
| TRAIN (5.540) | **`finetuning_v1`** (selección por grupos con gates anti-leakage); las 5.540 incluyen CHV, que no puede entrar al fine-tuning |
| DEMO (1.064) | El catálogo del media-plane apunta **directo al raw**; nunca leyó el manifiesto |

La regla metodológica de balance de clases (G6/G7) **no se perdió**: su guard sigue en
`datasets/tests/test_balance.py`, importando el helper desde `legacy/` por ruta explícita.
**418 tests verdes** tras el archivado. **Trampa que sobrevive:** los números 196 / 5.540 /
1.064 se citan como historia — **nunca citar "el BENCH de 196 imágenes" como benchmark**.

**(b) Candidatos nunca descargados — investigado; hay DOS razones distintas, no una.** El
doc decía "inventario de candidatos no seleccionados" sin explicar por qué, y además
agrupaba mal a `pictor_ppe` (su status es `pending_license_review`, **no** `pending_download`).
La razón real quedó escrita en la ficha de cada uno en `datasets_metadata.yaml`:

| Candidato | Por qué nunca se descargó |
|---|---|
| **`soda`** | **Razón definitiva y distinta a las demás: cubre CR-05 y CR-06, EXCLUIDAS por E-02** (`nucleo/10`, Nivel 3 relacional/zonas). No quedó fuera por calidad ni licencia — quedó fuera porque **las condiciones que aporta no se miden en esta tesis**. Descargarlo no habría producido ningún dato reportable |
| **`gdut_hwd`** · **`shwd`** | Candidatos de **refuerzo/apoyo sobre CR-01**, condición ya cubierta por `construction_site_safety` (el único con negativos explícitos, el requisito más exigente). Su licencia dice literalmente *"verificar contra fuente descargada"* y se distribuyen por Google Drive **sin SPDX** — que la rúbrica del reinicio v2 §7 descarta como criterio **obligatorio**. Y la regla de proceso es *"no procesar nada antes de seleccionar"*: bajarlos para recién ahí poder verificar la licencia invierte ese orden |
| **`pictor_ppe`** | `pending_license_review`, prioridad `condicionada`: **nunca estuvo habilitado para bajarse**. Bloqueado en el criterio obligatorio de licencia, antes de cualquier consideración de calidad |

A lo que se suma, para los tres últimos, el cierre de alcance de ADR-015/016.

**(c) `sh17` y `construction_ppe` — ARCHIVADOS, y su status era falso.** Decían
`raw_absent_views_stale`, que describe *"vistas processed/original huérfanas"*: se verificó
que **esas vistas ya no existen en disco**. El único artefacto remanente de cada uno era su
`*_conversion_report.json`, movidos a `legacy/processed_reports/`. Status corregido a
`legacy_archived` con la causa. Ninguno entró nunca al pipeline v2 ni a un resultado
reportable, y ambos eran **inelegibles por licencia** para los roles publicables: sh17 es
CC BY-NC-SA (NC + share-alike) y `construction_ppe` es AGPL-3.0 (viral sobre datos) — la
rúbrica §7 descarta ambas.

**(d) MOCS — la descripción anterior estaba incompleta y lo subvaloraba.** Su status no es
"sólo uso evaluativo": es **`used_pilot_a1`, prioridad `cerrada`**, con **dos usos, ambos
cerrados**:

1. **Candidato a BENCH → DESCARTADO** con causa registrada: lo que hay en disco es la
   *copia Roboflow* (`mocs-bowib`, 1.471 imgs) y **su única clase anotada es `Worker`** —
   cero anotaciones de EPP. Para TRAIN no aportaría señal de CR-01/CR-02, y en BENCH sería
   **engañoso** porque no cubre las clases de evaluación. Por eso no está en `canonical_v2`
   ni entra al entrenamiento.
2. **Material del mini-piloto A1 de clase nueva** (doc 94): aportó la evidencia cualitativa
   de amplitud de vocabulario (`excavator` / `tower_crane` / `dump_truck` sobre 151 imgs) y
   el **ancla cross-dataset `person` ↔ `Worker`**. O sea que **MOCS sí sostiene un resultado
   del informe** — el argumento A1 —, aunque no sea de entrenamiento ni de benchmark.

Caveat de licencia a conservar: el CC BY 4.0 es **declarado por el uploader de Roboflow**,
no por el MOCS original de anlab340; está registrado como tal en la ficha.

**Para T3, lo que falta del lado datos** (§3.4): derivar un **payload ODVG anti-leakage**
desde `finetuning_v1` y **definir su monitor**. Hoy no existe.

---

## 5. Resumen ejecutable — qué se puede hacer y qué gana

> **Para el plan de cierre concreto —quién cierra qué, cómo, y en qué orden— entrar por
> §5.1.** Esta tabla dice *qué conviene hacer*; §5.1 dice *cómo se cierra*.

| Prioridad | Acción | Quién | Qué gana | ¿Bloquea el informe? |
|---|---|---|---|---|
| **1** | Emitir `full-authorization.json` + **`RUN` T1** en Mendieta | **usuario** | Convierte E-04 de "rama preparada" en "rama con resultado" | **No** — la jornada corre en paralelo por diseño (ADR-017 §2f) |
| **2** | C1: URLs de los 18 `clip.yaml` | **usuario** | Cierra el último residual del hallazgo 1 de `gobierno/99` | No, pero es evidencia perecedera |
| **3** | Video **V2** de la defensa | **usuario** | Completa V1–V3 | No |
| 4 | Smoke de cámara F-118.3 | delegable | Convierte un `not_executed` en evidencia positiva del acople sensor→notificación | **No** — no cambia ninguna cifra |
| 5 | Decidir **D-FT-04** (retención T2) | **usuario**, después de T1 | Habilita T2 | No |
| — | **Campaña EBE por el bus contra GT** | — | **DECLARADA CON CAUSA — evaluada y descartada el 2026-08-15 (F-121.1): correrla daría el resultado idéntico a T1 por construcción** (determinismo verificado + paridad byte-idéntica bus↔JSONL). No es un experimento, es un guard de un modo de falla que ya tiene detector | No |
| — | ~~Port de `track_id` al pipeline online~~ | — | **NO es un pendiente**: G1 ya corre en DBE y EBE/live (decorador del control-plane, ADR-002 adenda ratificada 08-05, verificada en vivo doc 91) | No |

**Nada de lo pendiente cambia una conclusión** (doc 98 §7). El informe puede arrancar
cuando el usuario lo indique.

### 5.1 Cómo se cierra cada pendiente (✎ 2026-08-15)

**Un pendiente se cierra de una de cuatro maneras**, y confundirlas es lo que hace que
listas como ésta se estiren para siempre:

| Modo | Qué significa | Ejemplos de hoy |
|---|---|---|
| **Ejecutar** | hay que correr algo | `RUN` T1 |
| **Decidir** | no falta trabajo, falta una firma | `LICENSE` por repo · los 3 residuos · D-FT-04 |
| **Declarar** | ya está resuelto; falta escribirlo bien | eje EBE · `track_id` · los 4 de datasets — **los siete cerrados hoy** |
| **Delegar** | es mío, se cierra cuando lo pidas | propagación de C1 · F-119.1 |

#### A. Sólo tuyas — nadie más las puede cerrar

| # | Pendiente | Cómo se cierra | Después, delegable a mí |
|---|---|---|---|
| **A1** | ~~**T1 full**~~ ✎ **CERRADA 2026-08-17** | se cerró completa: autorización `gates=7` → job `1167640` `COMPLETED` → promoción → eval única | **veredicto NO-GO** ([doc 123](123-cierre-jornada-t1-no-go.md)); la latencia pareada se descartó con causa (F-123.1) |
| **A2** | **C1 — URLs + fecha de acceso de los 18 `clip.yaml`** | las conseguís vos (evidencia perecedera) | propagar a los 18, re-promover las 13 copias `meta/`, correr verificadores |
| **A3** | **Video V2** | elegir el material y validarlo **visualmente** antes de afirmar la clase (lección del intento fallido con `gloves`) | render con `armar_videos.py` |
| **A4** | **Git — 138 entradas en 5 repos** | decidís qué y cuándo | te preparo el desglose por repo con mensajes propuestos |
| **A5** | **Archivo `LICENSE` por repo** | es una decisión, no trabajo. **Único residual del hallazgo 3** de `gobierno/99` | agregarlos donde digas |
| **A6** | **Los 4 residuos** (`tmp-run-dbe-test/`, `uv.lock`, `notas.txt`, y desde el 2026-08-15 `.venv-talert/` — 120 MB, redundante tras cerrar F-119.1) | decidir borrar o conservar; no son míos | borrarlos |
| **A7** | **§17.x** | **no arranca hasta orden explícita tuya.** Antes hacen falta las **3 decisiones del manual `informe/ajustes/08` §2** (D-A dónde se escribe · D-B quién hace qué · D-C cuándo se re-extrae la foto del `.docx` — las tres con recomendación escrita) y **5 figuras** por producir (§6) | redacción y figuras según D-B |

#### B. Delegables — las cierro cuando digas

- ~~**F-119.1** — crear un venv propio de `e-ovrt_experimental-setup`…~~ → ✅ **CERRADA el
  2026-08-15.** `.venv/` (Python 3.11) + `requirements-dev.txt` con los tres hermanos en
  editable; **88 + 46 + 643 tests desde un solo intérprete**, reproducido desde cero en un
  venv limpio. La "deriva de versiones" resultó ser un **contrato declarado**, no un
  desorden: `alert-distribution` pinnea `<3.12`, los otros dos declaran `>=3.11` — no hay
  nada que unificar, 3.11 es el denominador común. Y el hallazgo original estaba a medias
  equivocado: existía un `.venv-talert/` que ya corría los 88, pero gitignoreado, sin
  documentar y con nombre engañoso (doc 119 F-119.1). **Deja un residuo:** `.venv-talert/`
  quedó redundante (120 MB) — decisión del usuario, como los otros tres.
- **Smoke de cámara F-118.3** — *semi-tuyo*: vos conectás la OAK-D o la RTSP, yo corro la
  campaña. Convierte un `not_executed` en evidencia positiva del acople
  sensor→notificación. **No cambia ninguna cifra** — por eso no está en la ruta crítica.

#### C. Condicionadas — no se cierran ahora, y está bien

- **D-FT-04** (subset y métrica de retención T2) → se decide **después** del resultado T1
  y **antes** de correr T2. Decidirla ahora sería inventar.
- **T2** → requiere que T1 pase el go/no-go.
- **T3** → 10 ítems sin tildar + resolver el antecedente de bboxes degeneradas + derivar
  el payload ODVG anti-leakage. **No se habilita antes que T1/T2** sin enmendar el
  protocolo explícitamente.

#### D. Orden recomendado

1. **A1 primero, hoy si se puede** — es el de mayor latencia: la cola de Mendieta proyectó
   inicio 2026-08-18 y el resultado no existe hasta que el job corra. **Va en paralelo a
   todo lo demás** (ADR-017 §2f: la jornada no bloquea el informe).
2. **A2 y A3 en paralelo** — son tuyas y no dependen de nada.
3. **B (F-119.1)** cuando quieras; no bloquea a nadie.
4. **A7 al final**, con su orden explícita.
5. **A4/A5/A6** son de higiene: se resuelven en una sola pasada cuando decidas commitear.

**La lista no se achica más por trabajo técnico.** ✎ **2026-08-15: F-119.1 se cerró**, y
con eso **no queda ningún pendiente puramente delegable**. Todo lo que resta es **decisión
o material del usuario** (A1–A7), más el smoke de cámara F-118.3, que es semi-suyo porque
necesita hardware conectado. Ese es el estado esperado a esta altura del proyecto.

## 6. Dónde está cada cosa

| Qué | Dónde |
|---|---|
| Cifras canónicas | los 4 índices de `e-ovrt_experimental-setup/results/` |
| Síntesis de una pasada | `docs/sintesis/resultados-y-conclusiones.md` |
| Teoría para la defensa | `docs/sintesis/fundamentos-teoricos.md` |
| Cierre EBE y por qué no re-rodar | `operacion/101` §1.3/§1.4 |
| Campaña de distribución | `operacion/118` + `results/realtime/t_alert_notification/` |
| Firma de las seis decisiones | `operacion/119` §8 |
| T-FT-031/032 y baseline 26s | `operacion/120` |
| Plan maestro y tablero E-04 | `operacion/116` y `117` |
| Estado por familia YOLOE/GDINO | `e-ovrt_datasets/docs/finetuning/2026-08-12-…md` |
| Contrato de datos y gates invariantes | `operacion/116` §6 + `finetuning/manifests/` |
