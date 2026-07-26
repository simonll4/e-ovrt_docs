# 71 — Relevamiento crítico del día de rodaje (2026-07-25)

**Alcance**: todo lo ejecutado el 2026-07-25 — grabación del shot-list completo (doc 69),
corridas EBE live GDINO y YOLOE, los 6 bugs encontrados y arreglados durante el día, y
los límites de realtime medidos. Fuentes: sidecars de `datasets-videos/raw/`, summaries
de `e-ovrt_media-plane/runs/` y `e-ovrt_control-plane/runs/`, `pattern_events.jsonl` de
cada corrida, y mediciones de GPU en vivo (`nvidia-smi dmon`). Escrito el mismo día,
con los servicios ya bajados a pedido del usuario.

> **Estado: CERRADO (2026-07-25, tarde-noche).** §1 (material) y §3 (bugs/fixes)
> cerradas al fin de la jornada. §2 y §4 (realtime) se cerraron después, en revisión
> conjunta con el usuario: se reprodujo el evaluador espacial frame a frame, se
> verificó la coreografía contra previews, y el usuario aportó la **verdad de campo**
> (qué EPP estaba puesto y cuándo, corrida por corrida). Esa revisión CORRIGIÓ la
> primera versión de este doc en tres puntos: la magnitud real de F-RT1 (`vest 0.73`
> sobre remera negra lisa, no 0,36–0,46), los **sujetos fantasma** de YOLOE como
> fuente independiente de evidencia espuria, y —el central— **F-RT2** (§2.5): la
> detección intermitente corrompe la ventana de confirmación temporal. El veredicto
> de YOLOE bajó de "2 correctas + 1 falsa" a **0/3 confiables**. §7 fija la
> continuación acordada: videos → GT humano; realtime alcanza para el cierre; las
> palancas de FPS van en §7.3 con protocolo de validación.

---

## 1. Material grabado — cobertura completa (salvo P7-c), con extras

**35 tomas sanas** (todas >20 s, `truncated: false`, sin error en el sidecar), cubriendo
**todo el shot-list P1–P9 del doc 69 salvo P7-c** (la opcional de roles invertidos,
única no grabada — anotada en el checkbox del doc 69) **y con extras**:

| Escena | OAK-D (60 fps, ~25 Mbps) | DVR RTSP (15 fps) |
|---|---|---|
| P1-a | take2, take3, take4 | take5 |
| P1-b | take3, take5 | take1 |
| P1-c | take5, take6 | take2, take4 |
| P2-a | take1 | take2 |
| P2-b / P2-c | take1 / take1, take2 | — |
| P3-a | take1, take2 | — |
| P4-a | take1 | take2 |
| P5-a | take1, take2 | take3 |
| P6-a | take1, take2 | — |
| P7-a / P7-b | take1 / take1, take2 | — / take3 |
| P8-a | take1 | — |
| P9-a | take2, take3 | take1 |
| P9-b | take1, take2 | — |

- **El subset DVR planificado (P1-a, P2-a, P5-a) está cubierto y AMPLIADO**: 9 tomas DVR
  en total (suma P1-b, P1-c ×2, P4-a, P7-b, P9-a). El sufijo `-dvr` del doc 69 §"hoja de
  registro" NO se usó — la cámara se distingue solo por el sidecar (`camera_id`/`plugin`),
  los nombres interlevan tomas de ambas cámaras bajo la misma numeración. **Cualquier
  script que asuma "takeN = OAK-D" se equivoca: leer siempre el sidecar.**
- P7-b es una variante extra no listada en el doc 69. P9 (confusables) tiene 5 tomas.
- `P1-a-take1` no existe: fue la grabación fallida del mediodía (RTSP unreachable, el
  recorder quedó trabado — destrabado vía `DELETE /api/recordings`).

**⚠️ Caveat crítico del material DVR**: las 9 tomas DVR pesan 3–13 MB para 27–57 s —
**~1,3–2 Mbps a 1920×1080**. El sidecar declara la resolución bien, pero ese bitrate es
compresión pesada: **verificación visual obligatoria antes de contarlas como material de
GT** (bloques de compresión pueden comerse el casco a distancia). El chequeo
`suspected_substream` pasó, pero el bitrate es un caveat que el doc 69 no preveía.

**Todo el GT sigue `gt_preliminary`** — nada de esto tiene pasada humana CVAT todavía.

---

## 2. Corridas EBE live — el corazón del día

### 2.1 La comparación GDINO vs YOLOE (las 6 corridas finales, prompt set congelado)

Misma escena, misma cámara (OAK-D), mismo prompt set (`cr01_cr02_v2_short`), mismos
patrones (v2: CR-01 4000 ms / CR-02 7000 ms). Única variable: el modelo.

| Corrida | proc/drop | fps_eff | inf p50 | g2a p95 (budget 250) | Alertas (veredicto §2.5) |
|---|---|---|---|---|---|
| GDINO P1 (`0ca90e`) | 47/767 (94% drop) | **1.16** | 567 ms | 890 ms ✗ | CR-01 ✓ **legítima** (4,3 s reales de evidencia continua) |
| GDINO P2 (`0eb1fd`) | 93/1115 (92%) | 1.76 | 439 ms | 665 ms ✗ | **ninguna** ✗ (CR-02 suprimida por F-RT1) |
| GDINO P3 (`12394a`) | 55/629 (92%) | 1.51 | 432 ms | 630 ms ✗ | ninguna ✓ (silencio correcto) |
| YOLOE P1 (`210d40`) | 254/615 (71%) | **5.55** | 116 ms | **232 ms ✓** | CR-01 ⚠️ tiempo corrompido + **CR-02 FALSA 100%** |
| YOLOE P2 (`73535e`) | 295/710 (71%) | 5.98 | 118 ms | **225 ms ✓** | CR-02 ⚠️ tiempo corrompido (alertó DURANTE el sacado) |
| YOLOE P3 (`e2bfe1`) | 152/322 (68%) | 5.12 | 112 ms | **249 ms ✓** | ninguna ✓ (por poco — ver §2.3) |

`bus_dropped_events = 0` y `degraded = false` en las 6 — el acople EBE estuvo sano todo
el día, sin excepción (también en las corridas de la tarde). Ese subsistema está cerrado.

### 2.2 GDINO: percepción densa, pero CR-02 SUPRIMIDA por F-RT1

- **P1: 4/4 en el día.** CR-01 confirmó en las cuatro corridas P1 de la jornada
  (18:30, 19:21, 19:43, 20:10), siempre con delta candidate→confirmed ≈ 4,1–4,3 s
  (umbral 4,0). El caso 19:21 además demostró la resolución con histéresis: 17 s de
  `sustained` con 17 "brillos de pelada" (helmet 0,25–0,46 intermitente) que NO
  cerraron la alerta; resolvió 2,0 s después del casco real (conf 0,79+ sostenida).
  Detalle fino: en la P1 final el casco se detecta en 47/47 frames (está EN MANO) y
  CR-01 dispara igual — **el matching espacial distingue "casco presente" de "casco
  puesto"**. Ese es el argumento A4 con datos live.
- **P2: 0 alertas en la corrida final — resultado negativo REAL, anotado a pedido del
  usuario.** El perfil por frame lo explica: durante el hold sin chaleco, GDINO siguió
  emitiendo `vest` sobre el torso (F-RT1, doc 70 — sobre-marca sobre ropa, ahora
  confirmada como supresora en vivo). **El análisis profundo posterior subió la
  magnitud: el falso llega a `vest 0.73` sobre remera negra lisa** (preview
  `frame_000670` de `0eb1fd`, verificado visualmente — el doc 70 había medido
  0,36–0,46 en la toma exploratoria). De 83 frames con sujeto, solo 4 tuvieron
  evidencia CR-02, en rachas de 0,0 s: la confirmación fue estructuralmente imposible,
  no "le faltó poco". Los episodios abrieron dos veces (f613–722, f761–1009) y
  murieron a ~4 s de los 7. **Con este modelo, esta cámara y este vestuario, CR-02
  live no confirma.** El umbral de confianza no lo arregla (probado por replay, doc
  70 — y con falsos a 0,73 queda doblemente descartado), el phrasing tampoco.
- **P3: silencio correcto** (candidate f309 → resolved f412, sin confirmar). La
  persistencia temporal filtró el transitorio de 2 s, como diseñado. 2/2 en el día.

### 2.3 YOLOE-26x: 3× más rápido, pero 0/3 alertas confiables (verdad de campo verificada)

**Verdad de campo confirmada por el actor** (2026-07-25, revisión conjunta contra
previews): en P1 el chaleco estuvo puesto TODA la corrida y el casco se sacó entre
t=8,9 s (frame #251) y t=11,45 s (#325, ya completamente fuera); en P2 el casco NUNCA
se sacó y el chaleco se sacó entre t=10,44 s (#249) y t=11,56 s (#281).

- **Percepción esparsa**: helmet detectado en 46%/85%/72% de los frames y vest en
  **46%/30%/57%** (P1/P2/P3), contra ~100% de GDINO. Mediana de conf vest en P2: 0,37.
  La intermitencia es el punto: huecos de detección de 0,1–2 s, ni presencia estable
  ni ausencia estable.
- **P1 / CR-02: FALSA al 100%.** Chaleco naranja reflectante puesto toda la escena
  (previews `frame_000247`, `frame_000365` — verificados visualmente), detectado solo
  46% de los frames. Alertó "sin chaleco" a t=12,9 s. Sin atenuantes.
- **P1 / CR-01: contenido correcto, MEDICIÓN INSERVIBLE.** El episodio abrió a t=7,5 s
  — **1,4 s antes de que el actor empezara a sacarse el casco**. La alerta (t=11,60 s)
  llegó con **0,2 s de infracción real**, contra un umbral de 4,0 s.
- **P2 / CR-02: contenido correcto, MEDICIÓN INSERVIBLE.** El episodio abrió a
  t=4,36 s (primer frame con la persona en cuadro, chaleco puesto pero no detectado) y
  **nunca cerró**: las rachas de cobertura continua fueron 0,13/0,38/0,45/0,45/0,51/
  1,97 s — ninguna llegó a los 3,0 s de `resolve_after_ms`. Los 7 s de confirmación se
  consumieron ÍNTEGROS con el chaleco puesto, y la alerta (t=11,45 s, frame #278) cayó
  **en medio del proceso de sacado** (#249→#281): llegó ANTES de que el actor terminara
  de sacárselo. Espera real de infracción: ~1,0 s de los 7,0 prometidos.
- **P2 / CR-01: correcto — pero 12 de los 22 frames de evidencia vinieron del sujeto
  FANTASMA** (persona alucinada sobre el cuadro colgado en la pared, conf mediana
  0,45 > umbral de sujeto 0,35; GDINO: 0 fantasmas en 195 frames). Los 7 episodios
  espurios los cerró la histéresis — por márgenes chicos, no por diseño robusto.
- **P3: silencio correcto, pero por poco.** 34 frames de evidencia CR-02 espuria
  repartidos en 13,3 s; no confirmó únicamente porque esos huecos de cobertura
  superaron los 3 s y el episodio se reinició. Con una distribución apenas distinta
  de los mismos falsos, alertaba.
- **Pero: es el único que entra en presupuesto.** g2a p95 225–249 ms (budget 50–250),
  5,1–6,0 fps efectivos, 68–71% de drops vs 92–94% de GDINO.

### 2.4 Corridas anteriores del día (contexto, prompt set NO congelado en parte)

- `r1` (13:33, Composición → **solo media, sin control**): error operativo #1.
- `ebe_oakd_live` 15:47: **primera EBE completa del día con set congelado — CR-01 a
  4,3 s Y CR-02 a 7,1 s del onset, ambas confirmadas.** La única CR-02 legítima de la
  jornada. Clave: en esa toma el chaleco salió de cuadro de verdad.
- `rt1`/`rt-01` (17:50/17:58, set `cr01_cr02_v2_safety_vest` NO congelado): material de
  F-RT1 (doc 70), no comparable con el bench. La CR-01 de rt-01 confirmó con delta
  4,60 s (el mayor del día — la evidencia abrió más tarde por los brillos).
- Dos corridas con 0 unidades (15:55, 17:54): cortadas a los ~10 s, antes del arranque
  del pipeline (~11 s) — impaciencia de operador, sin daño.

### 2.5 EL hallazgo central (F-RT2): la detección intermitente corrompe la ventana temporal

El mecanismo, verificado frame a frame con verdad de campo:

> **La ventana de persistencia (`confirm_after_ms`) solo es una garantía si la
> percepción es lo bastante estable como para que la histéresis (`resolve_after_ms`)
> pueda cerrar los episodios espurios. Con detección intermitente cuyos huecos de
> cobertura son más cortos que `resolve_after_ms`, el episodio nunca cierra y el
> umbral de persistencia se consume con tiempo de CUMPLIMIENTO. La propiedad "espero
> N segundos de infracción antes de alertar" se viola en silencio: el sistema emite
> una alerta bien formada, con timestamp y evidencia, que no esperó lo que declara
> haber esperado.**

Consecuencias medidas: TTFD corrompido (mediría 1,0 s donde el diseño promete 7,0);
falso positivo garantizado si el sujeto corrige antes de que venza el reloj (en P2, si
el actor se re-ponía el chaleco a los 11 s, la alerta salía igual); y la alerta
"correcta" de P2 es la respuesta correcta por la razón equivocada — la coreografía
coincidió con el vencimiento del reloj, nada más. **Corrección explícita a la primera
versión de este doc**: la CR-02 de YOLOE P2 no era "correcta pero no atribuible" — está
mal medida, por el mismo mecanismo que produjo la falsa de P1. Y "la histéresis
absorbió el ruido de YOLOE" vale solo para los fantasmas de CR-01; para la
intermitencia del chaleco la histéresis no protegió: **la habilitó**.

El control positivo existe en los mismos datos: en GDINO P1, la ventana de 4,3 s tuvo
**0% de frames con el casco cubierto** — evidencia continua real, la persistencia hizo
exactamente lo que promete. Los modos de falla quedan simétricos y opuestos:

| | GDINO (sobre-detección) | YOLOE (sub-detección intermitente) |
|---|---|---|
| Estabilidad perceptual | ~100% de frames | vest 29–57%, huecos 0,1–2 s |
| Error característico | alucina EPP que no está (`vest 0.73` en remera negra) | no ve EPP que sí está (46% con chaleco puesto) |
| Consecuencia en patrones de ausencia | **suprime alertas reales** (falso negativo: CR-02 nunca confirma) | **fabrica alertas y corrompe el reloj** (falso positivo + TTFD inválido) |
| Sujetos fantasma | 0/195 frames | 2–10% de frames (cuadro de la pared, conf med 0,45) |
| Presupuesto temporal (g2a p95 vs 250 ms) | 630–890 ms ✗ | 225–249 ms ✓ |

**Síntesis para la tesis**: ninguno de los dos modelos cierra solo, pero la lección no
es "elegir mejor modelo" — es que **la capa de patrones temporales hereda su validez de
una condición de calidad perceptual que hay que declarar y verificar**: estabilidad de
detección con huecos < `resolve_after_ms`. GDINO la cumple (y por eso sus alertas y sus
silencios son interpretables, incluso los negativos como F-RT1); YOLOE no la cumple, y
por eso sus 3 alertas son artefactos aunque dos "acierten". Confirma doc 64 en vivo y
lo supera: el bench de imágenes (recall CR-01 = 0,000) ni siquiera podía anticipar este
modo de falla, porque es una propiedad de la DINÁMICA temporal, invisible en fotos.

---

## 3. Bugs encontrados y ARREGLADOS durante el día (cronológico)

Todos con TDD, test de regresión, y verificación E2E. **Nada commiteado** (regla del
workspace) — ver §6.

1. **Runner live roto de fábrica** — `runner.py` pisaba `input` entero con
   `{"type": "bus"}`; el control-plane exige `input.bus` (endpoint sin default) → 422 y
   el experimento moría antes de lanzar nada. La rama live del runner **jamás había
   corrido contra el control-plane real** (los fakes no validan schema). Fix: fusión en
   vez de reemplazo + el bloque `input.bus` en el manifiesto + test de la costura.
2. **"Nueva corrida" ≠ plataforma** — dos pruebas (r1, rt1) salieron sin alertas porque
   Composición lanza solo el media-plane (su payload ni tiene campo `bus`). No es bug de
   código sino de UX/doc: el doc 69 §5.2 **instruía usar esa pantalla** para las tomas
   B. Corregido el doc (⛔ explícito) + botón "+ Nuevo experimento" en el sidebar.
3. **Experimento zombie tras Detener** — `TERMINAL_STATUSES` no incluía `"stopped"` (el
   estado real del stop manual del media-plane) → el experimento quedaba `running` en el
   BFF hasta el timeout de 300 s, bloqueando el siguiente lanzamiento con "hay un
   experimento en curso". Fix de una línea + test que reproduce el cuelgue.
4. **Banner "riesgo activo" mostraba "hace 1785005982s"** — el frontend restaba
   `since_timestamp_ms` (reloj de FUENTE, relativo al video) contra `Date.now()`. Fix:
   `active_ms` calculado por el motor con su monotónico (el mismo de
   `alert_registered_ms`), el cliente solo redondea.
5. **La traza post-corrida no mostraba el riesgo sostenido** (el reporte del usuario:
   "frame_000456 sin nada") — `alerts.jsonl` solo tiene el flanco de subida y
   `pattern_progress.jsonl` solo `candidate`; ningún endpoint servía
   `pattern_events.jsonl` (el único con el ciclo completo). Fix en 3 capas: endpoint
   `GET /api/runs/{id}/pattern-events` (control-plane), reconstrucción del intervalo
   `confirmed→resolved` en `compose_trace` (BFF), badge persistente en la tabla (front).
6. **Bundle fósil en :8090** — el BFF sirve `dist/` si existe; había un build de la
   madrugada y el usuario veía la consola vieja aunque el dev server (:5199) tuviera
   todo. Costó una ronda de "no veo el botón" en incógnito. Regla operativa nueva:
   **cambio de frontend ⇒ `npm run build`** si se entra por :8090.

**Features construidas en el día** (SDD, spec + plan + 5 tareas + review final):
derivación de manifiestos desde la UI (`+ Nuevo experimento`, precarga, procedencia
`derives_from`/`changes`, escritura atómica por directorio), con dos hallazgos CRÍTICOS
cazados por la review final antes de mergear: **fuga de credenciales RTSP a
`experiments/` (versionado, con remote)** — resuelto rechazando cámaras con userinfo —
y `active_ids` huérfano al cambiar prompt set. Más el banner de riesgo activo en vivo
(estado del motor por `/api/runs/current`, ADR-011 intacta).

**Documentos**: doc 69 corregido (§5.2 paso 6 y 9, §7 con la trampa de recarga y
F-RT1), doc 70 creado y luego **corregido tras el replay** (la primera versión culpaba
a la plataforma; el motor real hubiera alertado CR-02 a los 8,1 s en `rt1` — la
no-alerta era el error operativo #2).

---

## 4. Qué frenó (y qué frena) el realtime — crítico

1. **GDINO fuera de presupuesto temporal, y NO es un bug**: inferencia 300–570 ms/frame
   con 3 prompts → 1,2–2,6 fps, 92–94% de frames descartados, g2a p95 630–890 ms contra
   un budget de 250. La GPU se usa (verificado triple: `torch.cuda`, 1,6 GB VRAM del
   proceso, dmon con SM 6–41%) — el perfil "bursty" es la firma de un transformer a
   batch=1, no ociosidad. Confirmado que el gráfico por defecto del Task Manager de
   Windows (motor "3D") NO muestra CUDA — fuente de la falsa alarma "no usa la GPU".
2. **Degradación monótona a lo largo del día**: la MISMA config (gdino-tiny-560, OAK-D,
   3 prompts) rindió p50 235 ms / 2,62 fps a las 13:33 y 567 ms / 1,16 fps a las 20:10
   — **2,4× más lento al final de la jornada**. Correlato: GPU idle a 41 °C a las 13 h,
   55–61 °C idle a las 19–20 h, clocks nunca por encima de 2250 MHz (máx 3105).
   Hipótesis principal: thermal soak del chasis notebook en sesión sostenida + carga
   ambiente (consola, browser). **No probado causalmente** — queda como variable a
   controlar: los números "oficiales" de una comparación deben tomarse en la misma
   franja horaria/térmica. La comparación GDINO/YOLOE de §2.1 es válida entre sí
   (20:10–20:20, misma franja) pero el GDINO de esa franja está en su peor momento.
3. **El encoder de texto se recalcula por frame** (`grounding_dino_adapter.forward()`:
   BERT sobre "person. helmet. vest." en cada unidad). Identificado, NO implementado el
   cacheo (invasivo, exigiría revalidar contra el bench). Es la única palanca real de
   aceleración sin cambiar de modelo; su valor crece con el nº de clases del prompt.
4. **Un modelo por proceso** (`EOVRT_MODEL_REF` al arrancar): comparar modelos exige
   bajar/subir el media-plane. La orquestación multi-instancia existe (Plataforma /
   `EOVRT_CONSOLE_COMPOSE_DIR`) pero no está habilitada en este despliegue.
5. **Sin consolidación para corridas detenidas**: el runner consolida y genera reporte
   solo si ambos planos terminan `succeeded`; el stop manual da `stopped` → `ok: false`
   → **los 6 experimentos de la comparación no tienen dir consolidado ni report.json**.
   Los datos están completos en los `runs/` de cada plano, pero el artefacto paraguas
   no existe. Decisión pendiente: ¿`stopped` limpio debería consolidar?
6. **La card Alertas del detalle de experimento sigue cargando una sola vez** (sin
   refresh) — mitigado con el banner en vivo y documentado en doc 69 §7, no arreglado.

---

## 5. Otros hallazgos del relevamiento (ninguno bloquea, todos a la lista)

- **Basura de tests en `experimental-setup/runs/`**: ~74 directorios `exp_*_orq_*` /
  `gate_orq` de hoy — cada `pytest` del backend deja artefactos de la suite de
  orquestación en el runs/ REAL. Contamina el inventario de experimentos. Bug menor de
  aislamiento de tests, a arreglar y limpiar.
- `test_prompt_store.py::test_repo_frozen_sets_integrity` sigue rojo (preexistente):
  `prompts/edir_v1.yaml` declara `track: comparative` y `strategy: direct_absence` que
  el schema no acepta. Ligado al acta edir_v1 pendiente.
- Manifiestos exploratorios que quedaron: `rt-01` (prompt set NO congelado — renombrar
  o borrar para que nadie lo confunda con material comparable), `diag_riesgo_activo`
  (diagnóstico, borrable), y `experiments/realt-time-safety_vest.yaml` (payload suelto
  guardado desde Composición durante la exploración, con typo en el nombre — borrable).
- El fix de credenciales dejó **cerrado derivar hacia el DVR** (400 por userinfo en la
  URL del preset). Si un experimento futuro necesita el DVR, falta la opción "guardar
  camera_id y resolver al lanzar". Aparte: `GET /api/cameras` ya expone las credenciales
  al browser (preexistente, distinto problema).
- Parity live↔offline (replay del detections.jsonl live ⇒ artefactos idénticos): NO se
  re-verificó hoy con las corridas nuevas — sigue apoyada en la verificación previa.

## 6. Estado final y trabajo sin commitear

Servicios: **los tres abajo** (a pedido, fin de jornada). El media-plane quedó apagado
con la última config = `yoloe/yoloe-26x`; **al relevantar, volver a
`EOVRT_MODEL_REF=grounding-dino/gdino-tiny-560`** (es el campeón; YOLOE fue solo para
la comparación).

Sin commitear (todo el trabajo del día):
- `e-ovrt_control-plane` (7 archivos): `snapshot_active` + `active_ms`, endpoint
  `pattern-events`, tests.
- `e-ovrt_experimental-setup` (59): fix runner (bus + stopped), derivación completa
  (backend+frontend+tests), banner riesgo activo, trace `active_patterns`,
  `has_rtsp_credentials`, manifiestos `ebe_p1/p2/p3_live` + `yoloe_p1/p2/p3_live`,
  specs/planes SDD, ledger en `.superpowers/sdd/` (SIN commits, el ledger es el único
  registro del proceso — no borrarlo).
- `docs` (8): docs 69/70/71 nuevos (69 tildado con resultados, 70 con adenda, 71 este),
  índice, GUIA-CIERRE, y 59/67/68 tocados.
- `e-ovrt_media-plane` y `e-ovrt_datasets`: limpios (las grabaciones son gitignoradas
  por diseño).

## 7. Cómo continuar (fijado el 2026-07-25 con el usuario)

### 7.1 Camino de los videos grabados (Bloque A → banco DBE → cierre Nivel B)

El material está adquirido; el cuello es el GT humano, no la plataforma. En orden:

1. **Verificación visual del subset DVR** (9 tomas a 1,3–2 Mbps): confirmar que la
   compresión no se come el casco/chaleco a la distancia de escena. Si alguna no
   sirve, se declara y el subset queda con las que pasen — no bloquea al resto.
2. **Seleccionar la mejor toma por escena** (35 tomas → ~12–15 clips) y derivar clips
   con la herramienta de la consola (ventana Clips) o `prepare_clip.sh`. Respetar la
   trampa conocida: `--to` es relativo a `--ss` (duración, no fin absoluto).
3. **Pasada humana de GT en CVAT** — el paso crítico y el único sin atajo. Todo el GT
   actual del banco es `gt_preliminary`; ninguna métrica de cierre (TTFD/SDR/recall/
   precision/FAR) es citable hasta esto. Arrancar con P1-a y P2-a que son las escenas
   de las condiciones principales. El gate de dimensionamiento (A1, doc 58) avisa si
   un recorte deja episodios no medibles.
4. **Corridas DBE del banco** (replay de cada clip por ambos planos vía experimentos
   `media_first`) + `evaluate-alerts` → las 5 métricas por clip, matriz SDR×recall
   (doc 57 §7.3.2) y reporte consolidado. Acá el fps NO importa: DBE procesa a la
   velocidad que haga falta, la medición va sobre timestamps de media.
5. Los artefactos live del día (6 corridas EBE) quedan como el capítulo
   `t_capture→alert`/G2A sin GT (doc 58: "cada plano mide lo suyo") — ya están
   completos, no requieren re-toma salvo decisión explícita tras revisar §2.

### 7.2 Realtime: ¿alcanza lo que hay?

**Veredicto: para el cierre de la tesis, SÍ alcanza — con una re-toma opcional.**

- Lo que la tesis necesita del camino live ya está medido y es citable: **7
  confirmaciones CR-01 live con GDINO** (deltas 4,1–4,6 s sobre umbral 4,0: las 4 P1
  en 4,1–4,3; 15:47 en 4,3; rt-01 en 4,6; más una tardía en P2 19:54 con delta 4,4
  pero sin verdad de campo del cierre de esa toma), una CR-02 live legítima (15:47,
  delta 7,1), el acople EBE con 0 eventos perdidos en toda la jornada, y DOS
  resultados negativos de primera línea (F-RT1: la sobre-marca suprime CR-02; F-RT2:
  la intermitencia corrompe la ventana temporal). Los negativos no son fallas del
  trabajo: son exactamente la medición honesta "qué se logra sin entrenar" que la
  defensa argumenta (doc 09).
- El fps bajo de GDINO **no invalida las alertas live** (confirman por tiempo, no por
  conteo de frames) ni el camino DBE (offline). Invalida solo la pretensión de "tiempo
  real fluido", que se reporta como caracterización de hardware, no como meta fallida.
- **Única re-toma que valdría la pena** (opcional): una P2 live con GDINO en franja
  térmica temprana, remera lisa clara (no negra) y chaleco fuera de cuadro, para
  intentar UNA CR-02 live limpia adicional. Si vuelve a no confirmar, F-RT1 queda
  triple-confirmada y se cierra igual.
- Formalizar en el informe la condición de validez descubierta (F-RT2): **la ventana
  temporal exige estabilidad perceptual con huecos < `resolve_after_ms`** — GDINO la
  cumple, YOLOE no. Es un aporte, no una vergüenza.

### 7.3 Aumentar el procesamiento de frames (FPS) — palancas reales, en orden de retorno

Diagnóstico base (medido): el costo es 100% inferencia (normalize ~10 ms), GPU en uso
real pero no saturada (SM 6–41%, perfil transformer batch=1), fp16 ya activo, 560px ya
elegido. Palancas, de mayor a menor retorno esperado:

1. **Cachear el embedding de texto de GDINO** (el hallazgo del día): el encoder BERT
   re-procesa "person. helmet. vest." en CADA frame aunque el prompt no cambie en toda
   la corrida. Es la única palanca grande sin cambiar modelo ni calidad. **Spike
   aparte, con protocolo**: (a) perfilar qué fracción del forward es la rama de texto
   (medir, no estimar); (b) implementar el cacheo tocando internals del modelo HF;
   (c) verificar equivalencia numérica de detecciones contra 100 frames de referencia;
   (d) re-validar mAP contra `bench_obra` antes de adoptarlo. Si la rama de texto es
   ~30–40% del forward, el fps de GDINO pasaría de ~2 a ~3; si es menos, se documenta
   y se descarta con números.
2. **Controlar la variable térmica** (gratis): la MISMA config rindió 2,4× distinto
   entre las 13 h y las 20 h (p50 235→567 ms; GPU idle 41→61 °C; clocks nunca >2250
   de 3105 MHz). Toda comparación oficial va en franja térmica temprana, notebook
   ventilada, y con `nvidia-smi dmon` corriendo como testigo. Es plausible recuperar
   buena parte del 2,4× solo con esto — y es medición, no ingeniería.
3. **Variante `gdino-tiny-480`** (solo config + re-validación): el catálogo ya
   parametriza `image_size`; 560→480 daría ~25–30% menos cómputo de visión. Mismo
   protocolo que el punto 1(d): solo se adopta si `bench_obra` no se degrada. Es la
   continuación natural de la decisión 800→560 que ya dio −24% (doc 61/64).
4. **`torch.compile` / TensorRT sobre el adapter GDINO**: retorno potencial real
   (transformers chicos se benefician mucho de fusión de kernels) pero esfuerzo alto
   y riesgo de divergencia numérica; solo si 1–3 no alcanzan y sobra tiempo. No es
   camino de tesis, es ingeniería.
5. **Descartado con evidencia**: cambiar de modelo (no existe GDINO más rápido que
   tiny-560; YOLOE queda inhabilitado para EPP por §2.5), batching (suma latencia en
   vivo), y el prefilter EN-2 on-device (reduce carga pero no acelera la inferencia
   del frame que sí pasa; sigue disponible como reductor de duty-cycle, no de
   latencia).

Meta honesta: con 1+2+3 el techo plausible de GDINO en esta máquina es **~4–6 fps**
(300 ms → ~150–200 ms/frame en franja fría). No va a llegar a los 13 fps de la OAK-D:
eso se declara como límite del hardware de referencia, con el two-node (GPU dedicada)
como camino de escalado ya diseñado y dockerizado (Fase 2c) para quien lo necesite.

## 8. Los cinco números del día

1. **35/35 tomas sanas, shot-list completo + 6 tomas DVR extra** — el banco de video
   del cierre está adquirido (falta GT humano y verificación visual del bitrate DVR).
2. **CR-01 live (GDINO): 7 confirmaciones, deltas 4,1–4,6 s** sobre umbral de 4,0 —
   confirmó en TODAS las corridas GDINO-con-control donde hubo infracción de casco
   (4×P1, 15:47, rt-01, y la tardía de P2 19:54); 6 de las 7 con verdad de campo.
3. **CR-02 live: 1 legítima en el día (15:47, chaleco fuera de cuadro) y 1 supresión
   reproducida dos veces por F-RT1** — el vestuario/encuadre decide CR-02, no el motor.
4. **YOLOE: g2a p95 225–249 ms (único dentro de budget) con 0/3 alertas confiables** —
   1 falsa al 100% y 2 con el reloj de confirmación corrompido (F-RT2, §2.5): esperó
   0,2–1,0 s de infracción real donde el diseño promete 4,0–7,0.
5. **bus_dropped_events = 0 en el 100% de las corridas EBE del día** — el acople
   ZeroMQ 1:1 no perdió un solo evento en toda la jornada.
