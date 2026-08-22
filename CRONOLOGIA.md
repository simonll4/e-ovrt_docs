# Cronología de jornadas — el día a día del set documental

- **Qué es esto:** el registro jornada por jornada que hasta el 2026-08-10 vivía
  comprimido en una sola línea en la cabecera de `00-indice.md` (llegó a ~9 KB en un
  solo bullet). Acá se conserva completo y legible; el índice mantiene solo la fecha de
  la última actualización y el estado vigente.
- **Cómo se lee:** cada sección es una jornada, la más nueva arriba. El texto se
  conserva tal como se escribió al cierre de cada jornada — **es registro, no
  síntesis**: puede contener afirmaciones que una jornada posterior corrigió (la
  corrección aparece en la jornada más nueva). Para el estado VIGENTE, entrar por
  `GUIA-CIERRE.md` (qué falta), `sintesis/resultados-y-conclusiones.md` (resultados) y
  `operacion/97` (plataforma).
- **Jornadas anteriores al 2026-08-04:** no estaban en el changelog del índice; su
  registro son los propios docs de `operacion/` — ver el **mapa por tramos** en
  `00-indice.md` §`operacion/`.

---

## 2026-08-21 (tercera mitad) — el informe pasa a ser el único frente, y se producen **las cinco figuras**

El usuario fijó el orden: **primero el informe**; el smoke integral de Docker, C1, V2 y la
latencia pareada se difieren a la ventana post-entrega, mientras se esperan las
correcciones del jurado. La auditoría del frente de redacción encontró que lo único que
faltaba producir eran **las cinco figuras** de `ajustes/08` §6 —las 17 tablas ya estaban
en disco y se llenan copiando—, así que se produjeron las cinco:

- **FIG-A** (§17.4.1, vista de procesos) y **FIG-E** (§17.3.8.2, máquina de estados de
  cinco estados) — dibujadas desde la especificación de `94` §4 y desde el contrato
  `pattern_events` leído en el código.
- **FIG-B** (§17.5, calidad vs densidad) — generada leyendo los `metrics.json` de las ocho
  campañas del eje de densidad, con verificación que **falla si la cifra no coincide con
  el índice publicado**.
- **FIG-F** (§17.5, frontera de juzgabilidad de tres ejes) — dos paneles, de `operacion/103`
  §7.1 y `105` §4.1/F-105.3.
- **FIG-C** (§17.5, fotograma con alerta confirmada) — extraída del video V1 ya renderizado
  desde artefactos reales.

Todas en PNG 300 dpi + SVG, ancho de diseño 16 cm, paleta validada con el validador de
seis chequeos, y generadores reproducibles en `informe/figuras/scripts/`. Tres cosas se
corrigieron al dibujar, y quedaron anotadas como advertencias de cita: el **módulo de
distribución va en línea continua** (la nota al pie de `94` §4 quedó falsa desde
ADR-019/020), el **orden de arranque es el inverso del flujo de datos** (distribución →
control → medios, porque en PUB/SUB el consumidor debe suscribirse antes), y la
**reapertura de la máquina de estados va a `candidate`, no a `inactive`** — un error que
tenía mi propio primer dibujo y que se detectó contrastándolo con el código.
Constancia y notas al pie listas para pegar: `informe/figuras/README.md`. **Con esto el
inventario de materiales del informe queda completo: no falta ningún material para
redactar.**

## 2026-08-21 (segunda mitad) — el usuario declara el cierre: **acta del programa experimental** (doc 128)

Con la jornada de fine-tuning cerrada esa misma mañana, el usuario preguntó si quedaba algo
que valiera la pena probar y, ante el análisis (doc 127 §5-bis + acta 128 §2: los caminos
restantes o erosionan la pre-registración, o están bloqueados por diseño, o son trabajo
futuro), **ordenó iniciar el proceso de cierre y documentación completa**. Se emitió el
**acta `operacion/128`** — la nueva foto de estado vigente (reemplaza a `121`): mapa de los
13 frentes con constancia y salida citable, verificaciones del día en verde (índices ✅,
kit ✅, 46 tests ✅), y la lista final de lo que queda hasta la defensa **con dueño**:
smoke Docker integral (daemon apagado, sesión conjunta) · C1 · redacción · V2 · latencia FT
opcional · commits. Regla de salida: reabrir experimentos exige pre-registración nueva.
`GUIA-CIERRE.md` actualizada al nuevo estado. **La energía del proyecto pasa entera al
informe.**

## 2026-08-21 — T2 cierra: **NO-GO**, y la jornada E-04 queda completa en sus tres tiers (doc 127)

El job T2 v2 (`1167982`, enmienda D-FT-16: SGD lr0=0,01 explícito desde el peso base, techo
60 épocas/patience 15) corrió en Mendieta el 20/08 (`COMPLETED`, 26m10s) pero **colapsó en
entrenamiento**: EarlyStopping en la época 16/60 con **mejor época = 1** — el mejor checkpoint
es una época a LR de warmup; a lr0 pleno la validación interna se derrumbó (mAP50-95
0,084 → 0,018) y la recuperación por el decay se estancó en ~0,03. Con los dos regímenes de
full FT acotados por ambos lados (auto submuestreado en `1167864`; SGD estándar acá), ambos
quedan ~6× peor que el linear probing de T1 sobre los mismos datos.

**El fork lo firmó el usuario** (consumir los dos one-shot con ese `best.pt` vs cerrar sin
evaluar vs un tercer intento — descartado como ajuste post-hoc): cadena completa ejecutada el
21/08 — backup verificado (27 archivos, tar sha256 idéntico en ambos extremos), promoción
regla-7 (`yoloe-26s-ft-t2.yaml` **sin** `fixed_vocabulary`: T2 no hereda D-FT-08 y se sirve
open-vocabulary vía `set_classes`, como la baseline), bench 6.477/6.477 y COCO 5.000/5.000
con cero errores, evaluadores congelados con todos los sha256 verificados.

**Gates D-FT-15: ganancia PASA** — `bare_head` AP50 0,0000 → **0,0909** (el doble de T1),
pero íntegramente de `shel5k` (en los estratos de obra quedó 0,0) y con recall CR-01 0,0055.
**Retención in-domain FALLA ×4** (`person` −49,7 % · `helmet` −40,6 % · `vest` −65,6 % ·
mAP50 0,4193 → **0,2374**). **Retención OV FALLA** (COCO interno 0,4347 → **0,1247**,
−71,3 %, umbral 0,3912). Latencia no medida con causa (criterio F-123.1). **Las tres
expectativas pre-registradas del protocolo se confirmaron una por una.**

**F-127.1 — la respuesta a la pregunta del tier: el fallo de T1 NO era artefacto de
capacidad; el trade-off es ESTRUCTURAL** (2.946 imágenes de train para 10,35M parámetros).
La curva capacidad/retención de tres puntos —el valor declarado de D-FT-14/15— quedó
completa, con la nota fina de que T1 y T2 no ganan por la misma vía (T1 = recall CR-01
0,2089 con poca AP; T2 = AP 0,0909 con recall casi nulo). Checkpoint **no adoptado**; no
quedan brazos contra `bench_v3`. Propagado el mismo día a 117, ADR-017,
estado-de-implementacion, nucleo/10, síntesis, GUIA-REDACTORES y contingencia/20 §6.
Manifiestos: `t2_{promotion,go_no_go}_1167982.json`; driver reproducible nuevo
`finetuning/scripts/run_offline_media_plane.py`.

## 2026-08-19 — Limpieza general, la plataforma entera en Compose, y qué se respalda (doc 126)

Jornada de higiene pedida por el usuario: *"revisión completa del proyecto, todos los
repositorios… limpieza general, archivar código y configs legacy, actualizar docs y que la
declaración de la infra en docker compose esté completa para poder desplegar toda la
plataforma y hacerla reproducible en cualquier host"*.

Se auditaron los seis repos en paralelo antes de tocar nada. Lo que apareció no fue
desorden decorativo sino **deriva con consecuencias**: el `.dockerignore` del media-plane
no excluía `configs/runs/local/`, así que las credenciales RTSP de la cámara se horneaban
en la imagen; el README del control-plane afirmaba "no incluye servicio HTTP" (existe
desde ADR-0008) y **recomendaba el pattern set `v1` deprecado** —el que produce falsos
`missed` por F-DR9—; los nueve docs del distribuidor seguían describiendo el subproceso
como default un día después de que ADR-020 lo derogara; y en `datasets` había **7.683
archivos trackeados que el propio `.gitignore` del repo declaraba ignorables**. Todo eso
quedó corregido, con las suites verdes como condición de cierre.

El entregable central fue la infra: `infra/platform/docker-compose.yml` pasó de declarar
**2 componentes a 13 servicios** —consola, control-plane `:8081`, distribución `:8082`,
mosquitto como broker canónico y el fleet media por modelo, incluido el campeón
`gdino-tiny-560`—, con Dockerfiles nuevos en control-plane y distribución. Eso **revierte
explícitamente el descarte del 2026-08-13** ("no se implementa ni mantiene una imagen
propia del control-plane"), y la nota quedó escrita en el spec que lo descartaba: la
decisión cambió porque cambió el pedido. La pieza de diseño que lo hace reproducible en
cualquier host es la **paridad de rutas** — el workspace se monta en la misma ruta absoluta
dentro de los contenedores, porque los contratos de la plataforma intercambian rutas
absolutas por filesystem compartido (ADR-009 para los manifiestos, ADR-019 §3 para el
`out_dir` del distribuidor). Sin esa simetría, containerizar rompe el acople en silencio.
`docker compose config` valida los 13 servicios; **los builds y el smoke integral quedaron
pendientes porque el daemon de Docker estaba apagado** — se dice acá para que nadie lea
"declarado" como "verificado".

Dos deudas se cerraron de paso. El **gap de integridad de `bench_v3`**: dos de sus cuatro
fuentes congeladas (`chv`, `shel5k`) no tenían generador commiteado, así que el benchmark
era no-reproducible desde fuente; ahora lo tienen, con verificación por sha256 contra los
artefactos congelados. Y el **test rojo** del backend de la webconsole, que rechazaba el
prompt set `coco_val2017_80.yaml` del harness de retención T2 porque `track: retention` no
existía en el esquema.

El doc además fija el criterio de **respaldo a Drive**, que hasta hoy era implícito: el
código ya está a salvo en GitHub, así que Drive es exactamente para lo que git ignora.
Tres capas — **evidencia** (≈2,6 GB: la evidencia cruda de `operacion/datos`, los
checkpoints de Mendieta, las evaluaciones T1 que firmaron el NO-GO, los 4 índices
verificables, el GT de video anotado a mano), **seguro** (≈9,2 GB, con la advertencia de
que los videos de internet no se borran antes de cerrar C1: "regenerable" depende de que
las URLs sigan vivas) y **descarte** (≈23 GB que un comando versionado reconstruye). Más
una regla de seguridad: `cameras/` tiene credenciales en claro y nunca va sin cifrar.

Cierre: los seis repos commiteados y pusheados a sus remotos **sin merge a `main`**, y los
dos worktrees verificados como ya enviados —el de `experimental-setup` no tenía trabajo
único: sus 11 archivos sin trackear eran byte-idénticos a versiones ya commiteadas—.

---

## 2026-08-18 — ADR-020: HTTP queda como acople y el subproceso baja a fallback (doc 125)

Horas después de cerrar ADR-019, el usuario planteó eliminar el patrón BFF-subproceso
—"no tiene sentido mantenerlo ya que el servicio de alertas es HTTP y es lo que suma a la
plataforma"—, admitiendo hacerlo "aunque sea para la documentación en el informe". **Las
dos mitades no eran separables:** describir un solo acople HTTP mientras el sistema
arrancaba por subproceso habría sido documentar un sistema inexistente. Se resolvió con la
regla que gobierna el set —**el informe describe lo que el código hace**— y con la
distinción que la sostiene: *un patrón de acople es arquitectura; una bandera de
contingencia es operación*. ADR-020 **deroga ADR-018**, invierte el default (HTTP normal,
subproceso como fallback tras `EOVRT_CONSOLE_DISTRIBUTION_TRANSPORT=subprocess`) y devuelve
la plataforma a **DOS patrones de acople**: HTTP config-driven en los **tres** módulos
(`:8080`/`:8081`/`:8082`) y bus ZeroMQ (`:5557` detecciones, `:5558` alertas). Se descartó
**borrar** el subproceso: dejaría el sistema sin vía degradada. Costo declarado: la
webconsole ahora exige el servicio arriba cuando la distribución está habilitada.
Propagación completa (código, ADRs, material del informe, kit regenerado con guard nuevo y
prueba negativa) en el doc 125. **Dato para leer cualquier documento viejo:** el número de
patrones cambió tres veces en cuatro días (dos → tres con ADR-018 → tres con ADR-019 →
**dos** con ADR-020); sin enmienda del 08-18, un doc describe un estado intermedio.

## 2026-08-17/18 — el distribuidor pasa a ser también servicio HTTP (ADR-019, doc 124)

Pedido del usuario: que el módulo de distribución sea HTTP "para que el stack quede
completo para desplegar". Diseño por brainstorming con tres decisiones suyas (aditivo —
el CLI queda; solo el servicio, sin Docker; ADR-019 **complementa** ADR-018, no la
deroga), spec 45 §9 nueva, plan de 8 tareas ejecutado con subagente por tarea + revisor
por tarea + revisión final. **Sin ningún commit** (regla): bordes de revisión por
snapshots del working tree. Resultado: `eovrt-distribute serve` en `:8082` espejo del
control-plane (`POST /api/runs` 201/409/422, `/cancel` — desvío deliberado: el
control-plane no lo tiene—, `DELETE` que olvida el registro y **nunca** toca `out_dir`),
runner del BFF con cliente HTTP **opt-in** (`EOVRT_CONSOLE_DISTRIBUTION_TRANSPORT=http`;
default sigue subproceso). **Siguen siendo TRES patrones de acople** — el distribuidor
entró al primero; se corrigió a tiempo un "cuarto patrón" mal contado en el borrador del
ADR. Verificación: **DBE** con summary idéntico CLI vs HTTP y misma secuencia de
notificaciones; **EBE en vivo con la OAK-D real** (12→15 unidades, 2 alertas CR-01/CR-02,
`bus_dropped_events: 0`, MQTT real con PUBACK; cifras n=2 **no citables** — la citable
sigue siendo doc 118). El pase destapó y corrigió un **bug preexistente**: `cancelled`
era inalcanzable (el summary no tiene `termination_reason` en el nivel superior) — toda
corrida cancelada se reportaba `succeeded`; lo tapaba un assert flojo. Suites: distribuidor
133 (10 corridas sin flaky), webconsole 663. Containerización **diferida con causa**
(ADR-019 §4: el despliegue no es resultado del informe). Constancia: doc 124; trampas de
entorno (IP del preset vs fábrica, `alert_bus.enabled` default off, pgrep que se matchea
a sí mismo) en su §4.

## 2026-08-17 — la jornada de fine-tuning cierra: **NO-GO** (doc 123)

El job `1167640` arrancó el 16/08 a las 16:46 —seis horas antes de lo que Slurm había
proyectado— y terminó `COMPLETED` en **13m08s** sobre una A30: 10/10 épocas, alcance confirmado
en **3.096 parámetros / 12 tensores**. El watcher en el head node disparó el finalize solo y dejó
la auditoría con hashes.

De ahí en adelante, todo en un tirón: copia local verificada (234 MB, `MANIFEST.sha256` 22/22, y
los cuatro artefactos que audita el clúster coinciden byte a byte) → **integridad + binding de
clases + serving smoke** (los tres requisitos de la regla 7, ejecutados **antes** de tocar el
media-plane) → **promoción con sha256 preservado** → **corrida única** sobre las 6.477 imágenes
(0 fallos, 0 drops, 40.696 detecciones, 257 s) → evaluación con el comando congelado.

**El veredicto es NO-GO, y falla por partida doble.** El *gain gate* no pasa por ninguna de sus
dos vías: el ΔAP50 de `bare_head` fue **+0,0455** contra un umbral de **0,05** —faltaron
**0,0045**— y el rescate de recall, que exigía pasar de <0,1 a **>0,5**, llegó a **0,2089**. El
*retention gate* tampoco: `person` cayó **−11,62 %** sobre un tope de 10 % (`helmet` −4,49 % y
mAP50 −0,52 % sí pasan; `vest` **mejora** +24,6 %).

Lo que el resultado sí demuestra: con sólo la proyección de clase fusionada, el ajuste **saca
`bare_head` del cero absoluto** (0,0000 → 0,0455, de 10 detecciones a 1.264) y lleva el recall
CR-01 de **0,0002 a 0,2089** — de detectar *un* violador en todo el banco a detectar **1.109**.
El mecanismo funciona; la capacidad no alcanza y se paga con `person`. Por estrato la lectura
cambia de signo: `bench_obra_val` **mejora** (mAP50 +0,0828, `bare_head` 0,000 → 0,2614) y son
`chv`/`shel5k` los que arrastran el agregado hacia abajo, por `helmet`.

Los márgenes estaban firmados el 15/08, **antes** de que existieran la baseline y el checkpoint:
pre-registración estricta, así que **el negativo es resultado y no fracaso** (ADR-017), y la
causa nunca es temporal — el cómputo estuvo disponible y la corrida tardó trece minutos.

**F-123.1:** el gate de latencia no se midió, por dos razones que conviene no mezclar — no es
decisión-relevante (gain y retención ya fallan) y la pareja no existe, porque F-120.1 dejó al
brazo baseline sin latencias citables. Como dato descriptivo, el brazo tuned fue más rápido en
todos los percentiles, lo que sólo refuerza que la latencia no era el problema.

Dos cosas quedaron registradas por higiene y no por obligación: un primer lanzamiento **abortó
antes de toda inferencia** (ruta de pesos relativa al CWD; se verificó que no escribió artefactos,
así que no cuenta como observación del brazo one-shot), y una asimetría de registro entre brazos
—la baseline declaró el prompt inline y perdió el campo `strategy`— que **no entra al
`PromptPlan`**: ids, textos y orden son idénticos en los dos.

Propagado el mismo día a los docs 116, 117, 120 §5, 121, 122 §6, al índice y a esta cronología.
**Trampa que quedó marcada en 116/117: hay dos «NO-GO» distintos** — el veredicto científico de
D-FT-12 y la vieja puerta de autorización previa al envío, levantada el 15/08. Commiteado esa
misma jornada en los 5 repos con cambios (docs `2ac62df`).

**Más tarde el 17/08 — la escalera se aplicó, y después se enmendó (D-FT-14).** Primera
pasada: por la regla de entrada pre-registrada ("T2 solo si T1 mostró ganancia exigible") T2 y
T3 quedaron NO habilitados y la rama cerrada con evidencia. Después, a pedido explícito del
usuario, revisión crítica del cierre — y la crítica encontró algo real: la pre-registración
prohíbe **renegociar T1**, no prohíbe un experimento de seguimiento **con pre-registración
propia**; la cláusula "la rama se cierra" era gobernanza de presupuesto, no necesidad
epistémica. Resultado, por la vía de enmienda explícita que D-FT-03 prevé: **T2 reabierto como
tier EXPLORATORIO** — responde una pregunta nueva (¿el fallo de T1 es artefacto de capacidad o
el trade-off es estructural?), con márgenes propios (D-FT-15, borrador listo, **firma del
usuario requerida antes del RUN**), expectativa pre-registrada incluida (NO-GO probable; el
valor es la curva capacidad/retención de tres puntos), T1 intacto como confirmatorio y **T2
declarado último brazo contra `bench_v3`**. **T3 confirmado cerrado**: su bloqueo no es
cómputo sino la baseline MM-GDINO sana que nunca existió — arqueología de 1–2 semanas contra
la defensa. D-FT-04 pasó a diseño (COCO val2017 como subset de retención OV); tablero con
cadena T-FT-061…066. Constancias: doc 117 §3 (D-FT-14/15), adendas en `contingencia/20` §6 y
123 §8.

---

## 2026-08-16 — T1 full encolado en Mendieta + día 1 del pase de redacción

**Frente A — T1 full ENVIADO (cierre de T-FT-043, la noche del 08-15).** La evidencia
subió al clúster y se verificó por hash (8/8), `full-authorization.json` se emitió dentro
del contenedor (`gates=7`, verificación independiente), `TEST_ONLY` pasó y
`RUN_T1_10_EPOCHS` quedó encolado como **job `1167640`** (`ivb`/`multi`, 1 GPU/10 CPU/
60 GB/2 h; al encolar, inicio estimado 2026-08-17 ~06:20; watcher de finalización en
`tmux`). La constancia no existía en docs — quedó como ✎ en **doc 120 §5**. Resta esperar
el checkpoint y seguir T-FT-050→052.

**Frente B — arrancó el pase de redacción del informe (doc 122).** El usuario levantó el
bloqueo ("no arrancar §17.x hasta orden explícita") y firmó las tres decisiones del manual
(`informe/ajustes/08` §2) tal como estaban recomendadas: **D-A híbrida · D-B reparto por
juicio experimental · D-C re-extracción al cerrar con extractor** (+ ajuste: la vara del
§15 la borradorea Claude; los colegas integran). Se escribió la herramienta que D-C pedía
(`herramientas/extraer_informe.py`, stdlib puro, TDD 13 tests, títulos de §15 idénticos a
la foto `96c`, ecuaciones/figuras con marca visible) y los dos primeros borradores en
`informe/entregable/borradores/`: **`vara-15.md`** (AJ-1.01/02/13 — solo literatura,
desbloquea §17.5) y **`17-4.md`** (§17.4 completo, 12 AJ-4.x, absorbe R-12/13/26, con sus
4 cifras verificadas contra los índices y FIG-A/FIG-E marcadas como pendientes).
Verificadores 96/109/comparabilidad-T1 verdes al arranque; el kit estaba desactualizado
(`01-etapa-activa`) y se regeneró (`--check` verde). El tablero del manual no se marca:
los ajustes se marcan al llegar al entregable, no al borrador.

## 2026-08-15 (segunda mitad) — métricas de alertas consolidadas + T-FT-031/032 cerradas con baseline one-shot

La misma jornada de las firmas, el usuario ordenó cerrar los dos frentes que faltaban antes
del informe. Constancias: doc 119 §8.1 (adenda) y **doc 120**.

**Frente A — métricas del módulo de alertas: SIN pendientes.** `t_alert-system` quedó
**materializada como citable**: sección de equivalencia de nombres y regla de cita en
`results/clip_bench/index.md` (la columna `t_alert` ES `t_alert_system_ms` de los
`metrics.json`; citable por campaña/condición, jamás promediada entre campañas), y tabla de
la **cadena temporal completa POR TRAMOS** en `results/index.md` (`capture_to_host` 202–217
ms · G2A por contexto · `t_alert-system` por campaña · `t_alert-notification` p95 64,534 ms)
con dos reglas: los percentiles no se suman entre tramos, y `t_alert-system` tiene otra
referencia temporal (dominada por `confirm_after_ms`). Lectura de conjunto: **la
distribución no es el cuello**. Verificador 96 y kit verdes.

**Frente B — T-FT-031 y T-FT-032 CERRADAS (doc 120).** Lo ejecutado, en orden: (1)
`pycocotools` instalado; (2) **enforcement del vocabulario canónico v2 en el schema de
config del media-plane** (lo que D-FT-08 habilitaba; TDD, 5 tests de mutación, suite 665
verdes, Ruff limpio); (3) catálogo finetuned `yoloe-26s-ft-t1.yaml` versionado; (4)
**comando de evaluación congelado** `evaluate_t1_bench_v3.py` — verifica todos los hashes
del protocolo antes de computar, aborta si falta una imagen, 4 tests sintéticos; (5) run
E2E con el checkpoint smoke (8/8, jsonl parseable por el evaluador congelado); (6) el
protocolo pasó a `frozen` con el `go_no_go` de D-FT-12 y la enmienda trazada PRE-resultado;
(7) **baseline YOLOE-26s one-shot sobre las 6.477** (0 fallos/drops, 374,5 s CUDA):
**`bare_head` AP50 0,000 (6.181 GT / 10 det), recall CR-01 0,0167 bench_obra / 0,0000
shel5k / 0,0002 agregado** — la vía del rescate del gate queda abierta y exigible; retención
a proteger person 0,7843 / helmet 0,6286 / vest 0,2642 / mAP50 0,4193, por estrato en el
doc 120. **F-120.1**: el host pasó de batería a corriente con la corrida en curso —
detecciones válidas (aritmética idéntica), **latencias del run NO citables** como brazo del
gate de latencia; ese gate se medirá pareado con ambos brazos enchufados.

**Higiene de catálogo y entorno (docs 119/121).** Además del relevamiento, se cerraron
tres frentes de higiene: **(1)** `splits/v2/` archivado **entero** (los tres roles estaban
huérfanos y `bench.txt` lo *regeneraba* un comando activo) junto con `sh17` y
`construction_ppe`, cuyo status describía vistas que ya no existían; se documentó además
**por qué** los 4 candidatos del catálogo nunca se descargaron (`soda` cubre CR-05/CR-06,
**excluidas por E-02**; los otros caen en el criterio obligatorio de licencia). **(2)** El
eje EBE quedó declarado con causa (F-121.1). **(3) F-119.1 CERRADA**: `experimental-setup`
tiene venv canónico `.venv/` (3.11) con `requirements-dev.txt` — **88 + 46 + 643 tests
desde un solo intérprete**. Dos correcciones honestas del cierre: la "deriva de versiones"
era un **contrato declarado** (`alert-distribution` pinnea `<3.12`), no un desorden; y el
hallazgo decía que la suite no era reproducible, cuando **sí lo era** — existía un
`.venv-talert/` que corría los 88, pero gitignoreado, sin documentar y con nombre engañoso.
Lo real era que **no era descubrible**.

**Foto de estado (doc 121).** Al cierre de la jornada se relevó el estado completo para
decidir qué falta: resultados, pendientes reales, fine-tuning por familia y datasets. Dos
verificaciones que valen: **(a) el eje real-time está CERRADO SIN PENDIENTES** (doc 101) —
la única corrida con cámara prevista y no ejecutada es el **smoke de F-118.3**, que era
suplementario y no altera el p95 ni ninguna cifra; y `gdino-base-560` no tiene latencia
live medida, pero el doc 101 §1.3 argumenta que medirla no respondería nada abierto (queda
declarado que T2/B1 no tienen costo operativo live). **No hay que re-rodar.** **(b)** **el banco no tiene frentes abiertos.** La campaña EBE por el bus contra GT
—bloqueada por el ancla wallclock↔media— se evaluó formalmente y quedó **DECLARADA CON
CAUSA** (**F-121.1**): correrla **no daría ningún resultado nuevo**, porque el pipeline
DBE es determinista (F-109.1) y el bus publica el evento **byte-idéntico** al del JSONL
(paridad verificada por mutación, doc 37 §3) ⇒ el resultado sería **idéntico a T1 por
construcción**. La única divergencia posible (pérdida en el bus) ya se cuenta y degrada la
corrida, y en DBE la presión sobre el bus es *menor* que en vivo. No es un experimento: es
un guard de un modo de falla que ya tiene detector. Sumado a que el *protocolo de doble
toma* del doc 58 se diseñó justamente para no necesitar el ancla. Propagado a
`operacion/98`, `101`, `121` y los índices `clip_bench`/`realtime`.
✎ **Corregido en la misma jornada:** el doc 121
listaba también el *port del `track_id` al pipeline online* como eje abierto, citando el
§7 del doc 89 que el propio doc marca como reencuadrado por la implementación (§6 bis).
**No está abierto**: la adenda de ADR-002 se ratificó el 08-05 y la identidad ya corre en
DBE **y** EBE/live como decorador del control-plane (`input.track_persons`). La misma
fila stale vivía en `results/clip_bench/index.md`; ambas corregidas.

**Estado E-04 al cierre:** las **7 gates** de `full-authorization.json`
(T-FT-005/023/026/030/031/032/042R) están cerradas. Restan sólo acciones del usuario:
emitir la autorización (token `APPROVE_D_FT_08`) y el `RUN` manual en Mendieta (T-FT-043).
Cero jobs full. No comparar la baseline con la tabla histórica del doc 64 (doc 120 §2.5:
protocolos distintos).

---

## 2026-08-15 — el usuario firma las seis decisiones pendientes

**Ninguna decisión queda en `propuesta`.** Antes de propagar se verificó que ninguna
estuviera ya ejecutada como aprobada: las tres FT seguían en `propuesta` (`117:70,74,133`),
el registro de licencias decía "pendiente de firma" y el patrón BFF-subprocess seguía como
nota. El usuario firmó las seis **como se recomendaba y sin cambios**:

1. **D-FT-08** (contrato de serving T1: vocabulario fijo y ordenado, `set_classes()`
   prohibido) → T-FT-005 pasó a `done` y T-FT-031 a `ready`.
2. **D-FT-12** (objetivo `bare_head` y márgenes go/no-go) → **firmada ANTES de la baseline
   T-FT-032 y con cero jobs full**: la pre-registración conserva su valor y la enmienda
   `vest`→`bare_head` de `contingencia/20` queda firme.
3. **D-FT-13** (derogación de la sonda `machinery` sólo para T1) → **la puerta del doc
   `operacion/100` §6 queda CERRADA en ese ítem**, corrigiendo el estado que esta cronología
   registraba el 08-14 como INCOMPLETA.
4. **Licencias**: checkpoint derivado T1 hereda AGPL-3.0 (uso local, no redistribuible);
   `mobileclip2_b.ts` **se mantiene `NOASSERTION` por decisión expresa**; y la subida del
   asset a Mendieta del 08-13 queda **ratificada como excepción acotada y retroactiva** a la
   política CC BY 4.0 del doc 100 §6.3, que sigue vigente sin cambios para datos.
5. **[ADR-018](decisiones/adr-018-acople-bff-subproceso-distribucion.md)** — la nota del
   08-14 sobre el patrón BFF-subproceso se promovió a ADR aceptada. La serie del proyecto
   pasa a `ADR-001…018` y **el informe debe describir tres patrones de acople, no dos**.
6. **Métricas de `report.json`** — y acá el propio doc 119 estaba mal: **no eran cuatro
   métricas nuevas, eran tres.** `t_alert-system` ya estaba en el diccionario de la spec 40
   §5.1 (el plan del 07-11 es explícito: *"figuran en `resultados`, no se omiten"*); lo que
   cambió es que dejó de estar clavada en `not_applicable`. Queda **citable**.
   `precision_alertas`/`recall_alertas`/`F1_alertas` quedan **emitidas pero no citables**:
   duplican cifras que ya se reportan vía `evaluate-alerts` con denominadores por estrato.

**Efecto neto sobre E-04:** el **NO-GO de T1 full persiste, pero cambió de naturaleza** — ya
no hay ninguna decisión humana en la cadena. Restan sólo la evaluación T-FT-031 (`ready`,
requiere instalar `pycocotools` en el venv de media-plane) y la baseline YOLOE-26s T-FT-032.
Cero jobs full. Constancia: `operacion/119` §8.

**No ejecutado y registrado como tal:** el enforcement del vocabulario canónico v2 en el
schema de config de media-plane, que D-FT-08 desbloquea pero es trabajo de código.

---

## 2026-08-14 — relevamiento post-Codex y cierre de brechas

Se cerró la doble falencia crítica detectada tras el relevamiento:
gravedad del módulo de distribución (ledger en append-only con generaciones y
`report.py` con guard de dry_run), trazabilidad operativa del canal de distribución
(stderr redactado en disco, preflight de binary + broker, reconexión acotada y
latencia de cooldown con base temporal explícita), y la cobertura completa del
verificador del agregado de `realtime`.

Además, se avanzó sobre las puertas pendientes del bloque de finetuning, que **siguen
abiertas** (✎ 2026-08-14 — el titular decía "quedaron cerradas las puertas pendientes",
y es sobredicho): `--allow-cpu` quedó acotado a preflights
(`--check-only/--check-freeze`) y el estado del gate `machinery` quedó explicitado como
propuesta (`D-FT-13`) en lugar de cerrado por defecto. La puerta del doc `operacion/100`
§6 sigue **INCOMPLETA**: la derogación de la sonda de clase nueva (`machinery`) está
propuesta como `D-FT-13` en estado `propuesta`, **pendiente de firma del usuario**
[✎ firmada el 2026-08-15 — ver la jornada de arriba; esa puerta ya está cerrada]. Se
consolidó el cierre documental con `operacion/119`, se regeneró el
`informe/project-kit/` y se re-ejecutaron los verificadores de organización y del kit.

Dos resultados cambiaron de estado en la jornada:
- **Análisis steady-state de la latencia de notificación**, publicado desde el mismo
  `outcomes.csv` y **sin re-corrida**: régimen sostenido **p95 = 102,025 ms (n = 104
  entregas subsiguientes)** contra **49,869 ms (n = 356 primeras entregas por corrida)**
  — `e-ovrt_experimental-setup/results/realtime/t_alert_notification/metrics.json`,
  bloque `steady_state`.
- **Fila nueva `T-85`** en el inventario de cierre (`informe/ajustes/gobierno/99` §1)
  para la latencia de notificación de la distribución de alertas.

Evidencia de estado:
- `operacion/119-relevamiento-post-codex-y-cierre-de-brechas.md` (constancia integral),
- `e-ovrt_experimental-setup/tools/evidence_runs.py --check`,
- suites de verificación y regresión ejecutadas en el bloque E (media-plane, backend de la
  webconsole, control-plane, alert-distribution y `tests/` de experimental-setup;
  ✎ 2026-08-14: la lista decía "datasets", suite que no se ejecutó en esta verificación),
- `python3 herramientas/generar_project_kit.py --etapa 6 --check`.

## 2026-08-13 — `finetuning_v1` cierra F-100.1; smoke técnico verde, full en NO-GO

### 2026-08-13 (bis) — distribución de alertas y soporte experimental

La campaña `t_alert-notification` (doc 118) produjo **F-118.1: p95 = 64,534 ms
(n = 460 entregas live contra broker MQTT real, testigo independiente al 100 %)**.
El cooldown suprimió el 44,976 % de los eventos (F-118.2) y la cámara quedó
`not_executed: hardware_source_not_connected` (F-118.3). El doc 115 cerró el gate
de instrumentación (D-115.1) y difirió con causa seis frentes A–F (D-115.2). La
orden de arrancar la redacción sigue siendo del usuario.

Se materializó `finetuning_v1` con 2.946 train/483 val, cuatro clases y disjunción de
train/val/`bench_v3`; D-FT-01 quedó aprobada. En Mendieta, después de cerrar dependencias
offline y compatibilidad CPU, `1166552` terminó `COMPLETED 0:0` en una A30 (1:44; 7,82 GB),
produjo checkpoints y pasó recarga/inferencia. La revisión adversarial posterior encontró
estado optimizer para 366/366 tensores: el freeze upstream del linear probing no fue efectivo.
El run se conserva como evidencia de infraestructura, pero su gate metodológico y sus marcadores
de full quedan revocados. T1 completo pasa a NO-GO con cero jobs enviados. Antes de repetir:
corregir y blindar el freeze, congelar procedencia, cerrar D-FT-08/P3, preparar baseline 26s
sobre `bench_v3`, ejecutar un nuevo mini-smoke y dejar monitor/finalización del full.

La corrección posterior pasó preflight sobre el modelo real con exactamente 12 tensores/3.096
parámetros entrenables, sólo en `cv3` y `one2one_cv3`. Se reconstruyó el bundle `r19`
(manifiesto SHA-256 `3213808898446caa1684d83d6a4ab84581f1d06dbf840afc703912250430cba2`) y se
envió únicamente el mini-smoke `1166578` (1 época, 5 %, 10 min máximo), pero se canceló
deliberadamente tras 37 s GPU al detectar que un smoke técnico todavía podía crear
`ready-for-manual-full.txt` con D-FT-08, baseline y procedencia abiertos. No fue un fallo del
trainer ni un gate. Se abrió T-FT-026 para separar `technical-smoke-ready.txt` de
`full-authorization.json` antes de repetir T-FT-042R; el NO-GO y T-FT-043 `blocked` siguen.

T-FT-026 quedó después `done`: el autorizador exige estados exactos
T005/023/026/030/031/032/042R, D-FT-08 aprobada y hashes; una prueba `RUN` sin autorización
terminó `exit=1` y dejó cero full. El bundle activo `r20` contiene 6.888 entradas; el índice
`bundle.sha256` tiene SHA-256 `1049b3ea1bebd8ebbeb78224daf0febf8dfcaac22503721feeaa0ca39893e026`
y `bundle.json`, `084c8842f54e531f5065192b3b733b068b046f0d9789c463dfeda8c144d14954`;
`r19` quedó archivado. El nuevo smoke `1166583` terminó `COMPLETED 0:0` en A30 y validó exactamente 12
tensores/3.096 parámetros, optimizer 12/12, artefactos y gate v2/live verify de 20 críticos.
T-FT-030 también quedó técnicamente `done` con checkpoint real servido fuera del sandbox,
39 tests focalizados, 100 ampliados y Ruff verdes. T-FT-023 quedó después cerrado con un
snapshot inmutable de 72 fuentes: inventario `431e43a4…3617`, manifiesto `f487347b…9bc8` y tar
`639e60df…3ebe`, más atestación posterior `4fe5aa3c…1bbda`, verificados localmente y en
Mendieta, sin commit ni staging. D-FT-08/T005,
D-FT-12, T031 y T032 siguen abiertos; T-FT-043 continúa `blocked`. `sbatch --test-only` aceptó
el full de 2 h y proyectó
2026-08-18 por la cola observada, sin constituir reserva ni promesa.

---

## 2026-08-11 — ADR-017: el fine-tuning deja de ser "exclusión" y pasa a jornada comprometida

Orden del usuario sobre el encuadre del informe: el fine-tuning **nunca debe leerse
como "descartado por falta de tiempo"** — es una **rama experimental desde las etapas
iniciales** (la Tabla 37 ya lo decía: baseline primero, ajuste cuando vale la pena),
condicionada por **datos y protocolo** (F-100.1, licencias/transporte, go/no-go), no
por cómputo (Mendieta disponible, T1 ≈1 GPU-h medido) ni por plazo (el cronograma lo
define el propio proyecto). Se acuñó
**[ADR-017](decisiones/adr-017-fine-tuning-jornada-experimental.md)**: E-04 **se
ejerce como jornada completa** — escalera T1→T2/T3 con go/no-go pre-registrados,
entrenar en el clúster / evaluar local, resultados **y limitaciones** documentados con
su estado a la entrega; no bloquea el informe. Deroga E-04 de la cláusula (b) de
ADR-016 y de ADR-015 §2a; el freno sigue para EN-3/E-10/E-06/CR nuevas. **Propagado**:
`nucleo/10` (ficha E-04 + banner + tabla), `contingencia/20` (de "si sobra tiempo" a
plan de la jornada; §7 derogado), **AJ-2.11 reescrito** (decía "exclusión por
presupuesto de tiempo"), `ajustes/00/01/04/06/07`, redlines `93`/`94` (incluida la
prosa lista-para-pegar de R-13), `gobierno/98/99`, las dos síntesis (incluido el guion
de la pregunta hostil *"¿por qué no fine-tuning?"*), glosario, índice, `nucleo/16/17`,
`operacion/62/100` (D-100.2: condición cumplida), históricos `02/07/08` anotados, y el
`informe-project-kit/` regenerado. Puertas técnicas previas a pedir turno en Mendieta:
**decisión del usuario sobre F-100.1** + checklist doc 100 §6.

## 2026-08-11 — el módulo de distribución, relevado ejecutándolo (doc 114)

El usuario implementó el grueso de `e-ovrt_alert-distribution` (el módulo que ADR-016
reabrió el día anterior) y pidió relevarlo. **Está funcionalmente completo**: 37 tests,
ruff limpio, contratos idénticos a `92b` campo por campo — pero **con cero commits**.

Lo relevante es que el relevamiento **no se hizo leyendo, se hizo corriéndolo** contra
una prueba ya ejecutada (`v06_c01` del lote de internet, 193 alertas reales), y eso
cerró **5 de los 6 criterios de terminado** de spec 45 §7:

- **Replay DBE**: 23 delivered / 170 suppressed_cooldown; re-ejecución 23
  `skipped_duplicate` ⇒ idempotencia verificada.
- **Live EBE contra el publisher real del control-plane** — el criterio que el plan
  había dado por *"fuera del alcance de este repo"*. 193/193 leídas del bus,
  `bus_dropped_events 0`, cierre por el sentinel `run_finished`, `experiment_id`
  end-to-end, y **resultado idéntico al del archivo ⇒ paridad DBE↔EBE**.
- **Entrega MQTT real con QoS 1 y PUBACK**: como no hay Mosquitto ni Docker en esta WSL,
  se escribió un broker MQTT 3.1.1 mínimo (80 líneas) — 23 mensajes en
  `eovrt/alerts/medium`. **Es un smoke contra un stub de loopback: sus latencias no son
  una cifra reportable** y no reemplazan la demo con `mosquitto_sub`.

**El 6º no se cumple**: `report.json` no integra la distribución (`report.py:418` la
tiene hardcodeada como `not_applicable`/`no_distribution`). Y lo que falta **no es el
módulo, es su acople**: reporte, vista en la webconsole (que **ADR-016 §2a nombra
explícitamente**) y Mosquitto en el compose.

Tres asperezas más, **verificadas y no deducidas**: una alerta con JSON válido pero un
campo faltante **aborta la corrida entera** (`KeyError`, exit 1, sin summary — contradice
la garantía de `92b` §2 de que ninguna alerta desaparece en silencio); `notifications.jsonl`
crece sin techo entre pasadas (193 → 386 líneas); y el `latency_mode` no llega al summary,
que es justo el caveat que `92b` §8 manda declarar siempre.

**Decisión de infra recomendada:** al compose va **solo el broker**; el distribuidor corre
en el host igual que el control-plane —que tampoco está dockerizado—, y los artefactos
entran como cuarto hermano `runs/exp_<id>/distribution/`. Ninguna cifra del tramo
experimental se toca (ADR-016 §4).

**Mismo día, siguiendo el orden recomendado — C3, C1 y A1 cerrados con TDD:**
`distribution_summary.json` ahora agrega `talert_notification_ms` **por
`latency_mode`** (nunca mezclado); una alerta con campo faltante ya no aborta la
corrida (`skipped_invalid_alerts`, la corrida sigue); y `experimental-setup` integra
el summary al `report.json` —cerrando el 6º criterio— con el mismo criterio que
`t_capture->alert`/reloj de medio: **DBE wall-clock nunca se reporta como si fuera
la latencia operativa real** (`not_interpretable`, no `computed`). Verificado contra
una corrida consolidada real. Suites: alert-distribution 39+1 · backend
experimental-setup 592. Sin commitear.

---

## 2026-08-10/11 — ADR-016 (distribución reabierta) + serie de relevamientos 14–19 + `nucleo/` partida por vigencia

**El disparador:** el usuario encontró que `nucleo/01` §10 citaba como "pendientes" cinco
ítems superados desde el 2026-07-29 — el relevamiento del control-plane era una foto del
07-06 con **siete de once secciones vencidas** (la peor trampa: §8 daba como vigente el
pattern set `v1`, deprecado por F-DR9). Auditado el set: `nucleo/11` (media-plane) estaba
igual, y tres decisiones ya escritas eran inencontrables (la regla de archivado de
`_archived/README.md`, la frontera de ADR-011, el "sube a Drive a mano" de
`datasets-videos/README.md`) — el síntoma que la serie nueva viene a curar.

**Tres frentes ejecutados:**

1. **ADR-016 — reapertura acotada de la distribución.** El usuario decidió implementar el
   módulo de distribución **antes de la defensa** para cerrar la arquitectura (dónde vive
   el ciclo de vida de la alerta: cooldown, re-notificación, supresión). Colisionaba con
   ADR-015 §2c/§6; ADR-016 deroga **puntualmente** §2b/§2c/§6 y ratifica §2a/§3/§4/§5
   (la lista L1–L8 se sigue citando desde ahí). E-06 sigue excluida; **no bloquea el
   informe** (si el módulo no llega, se declara como estaba). Propagado a 9 lugares
   (ADR-005/015, README y estado de decisiones, `nucleo/10`, `informe/99`,
   `GUIA-REDACTORES`).
2. **Serie `nucleo/14–19`** — relevamientos por servicio, **contra git y código** (suites
   corridas: control 312 · media 641 · datasets 418 · BFF 586), **cero cifras de
   resultado** (las cifras siguen en `results/`; capacidades en `operacion/97`). `14`
   mapa de la cadena · `15` setup · `16` datasets · `17` media (reemplaza al 11) · `18`
   control (reemplaza al 01) · `19` **cierre de la arquitectura: el ciclo de vida de la
   alerta** (consolida 06/ADR-005/ADR-011/spec 45/92b; deja anotado el desfase
   `confirmed_at_ms` que el implementador va a chocar).
3. **`nucleo/` partida por vigencia** (criterio del usuario: histórico = todo lo no
   actualizado a lo implementado): raíz = `10` + `14`–`19`; **`nucleo/historicos/`** =
   `01`–`09`, `11`, `12` (ninguno posterior al 07-13), con banner cada uno y `README.md`
   con punteros. `04`/`12` marcados **"no se toca"** (pre-registro de D1, valen por no
   actualizarse). **Hallazgo:** `09` (los argumentos A1–A5 de la defensa) quedó histórico
   por el criterio — no incorpora los números medidos después (A1 se midió en
   `operacion/94`); amerita sucesor. 25 rutas reescritas, enlaces verificados (73/73),
   verificadores 96 y 109 **verdes** (el 96 ajustado para buscar también en
   `historicos/`). De paso: 4 enlaces rotos preexistentes de la reorg de `informe/`
   corregidos.

**Relevamiento de consistencia de `informe/` (2026-08-11, tras ADR-016):** los siete docs
de `informe/ajustes/` se pusieron al día con el estatuto nuevo de la distribución — AJ-0.01,
el §5 del `03`, AJ-4.01/4.11 del `04` y AJ-6.04/6.05 del `06` dejaron de citar ADR-015 §2c
(derogada) y dicen **trabajo comprometido con estado a la entrega**; en el `06`, la
distribución **salió del trabajo futuro** (queda E-06). Se reparó además lo que la jornada
de ADR-016 dejó a medio propagar: el **encabezado del `92b`** (todavía decía "coherente con
ADR-015… no ejercida"), el rango de serie **`ADR-001…016`** en seis lugares (mapa AJ-0.02,
`99` §4.2 y §6, `98` §2 ×2, glosario 13), el "15 ADRs" del `98` §1 y del índice (fila del 99
y §decisiones), e insumos nuevos en el `04` (`nucleo/14`–`19`). Verificación: 0 links rotos
en `informe/` completo, IDs `AJ-` 7+16+12+12+12+5 sin duplicados, verificadores 96/109
verdes. **Kit refrescado**: 36 copias re-sincronizadas + 7 agregadas (`adr-016`,
`nucleo-14…19`) — nivel1 55 / nivel2 17 / nivel3 21.

**Crítica de extensión del informe (2026-08-11, pedido del usuario):** nuevo
`informe/ajustes/07-critica-extension-y-poda.md` — no existía nada que midiera longitud
(el 93 audita corrección, el 95 sacrificaba redlines contra tiempo). Medición por sección
(`wc -w` por encabezado sobre los extractos): **~126.800 palabras escritas** con
§17.4/17.5/17.6 aún vacías. Titular: **21.260 palabras (17%) cubren DOS VECES los dos
temas menos alineados** — MOT (§15.3 2.484 + §16.4 2.769, con E-10 excluyendo las
métricas) y streaming/arquitecturas/borde (§15.4 7.998 + §16.5.3–5 8.009, con la decisión
colapsada a RTSP+ZeroMQ y EN-3 excluida). Otros hallazgos: §16.7 = 4.429 de meta-texto ·
§17.1.6.2 = 5.054 de catálogo de datasets pre-`bench_v3` (se poda junto con R-24) ·
§16.5.2 duplica el framework de métricas de §17.1.7. **18 podas `PODA-nn`** (serie
verificada libre) con casilla de decisión, 5 criterios, **ahorro ~34.900 (~27%)**, orden
recomendado (los 8 🔴 = 65% del ahorro) y 6 guardrails (16.2/16.3/17.1.5/17.1.7 intactas;
lo pre-registrado no ejercido se comprime a decisión declarada, no se borra). Cableada en
mapa (§1/§2), índices, GUIA-REDACTORES y kit.

**Regla de no-anacronismo (2026-08-11, fijada por el usuario):** *"las primeras etapas no
tienen que mencionar resultados o experimentos de etapas posteriores — sería adivinar el
futuro"*. El caso que la disparó: el borrador de `AJ-1.02` pedía meter en §15 el keep-up
del Sprint 2 y los G2A live (datos de Etapa 4/5). Registrada como **regla 5 del mapa de
ajustes**, con la frontera precisa: decisiones y correcciones de diseño SÍ se aplican
hacia atrás; resultados medidos y refutaciones NO — la brecha se declara con literatura
en §15/§16, el criterio en §17.1, y el cruce con lo medido vive en §17.5/§18 (los "tres
tiempos" operan ahí y solo ahí). Barrido aplicado: `AJ-1.02` reescrito (la brecha se
sostiene con ODinW + Chen 2025, cero números propios) · `AJ-1.11`/`AJ-1.13`/`AJ-1.15`
precisados · `AJ-2.05`/`AJ-2.09`/`AJ-2.11` reescritos (el n efectivo, el cumplimiento de
la instrumentación y el costo medido del fine-tuning aterrizan en §17.4/§17.5/§18) ·
**doc 03 §3b nuevo: R-12/R-13 ("secciones al cierre" del §17.3) aterrizan en §17.4** —
cambia el destino, no el texto del `94` §7–§8; R-20/R-22 con la parte retrospectiva como
nota fechada · PODA-04/07/08 ajustadas (las justificaciones de decisión no van en
§15/§16) · GUIA-REDACTORES con la regla en §2.

**Auditoría de material (mismo tramo):** clasificador de runs contra-verificado (4
pasadas hasta converger): 670 runs, 434 citados, **236 no citados = solo 0,26 GiB**, cero
huérfanos. Lo pesado está todo gitignoreado — lo que recibe quien clona son ~17.600
archivos versionados (354 MB). `scripts/` (5,7 G, raíz del workspace) confirmado huérfano
del intento inicial de descarga (0 de 16 IDs citados). El respaldo del material
irremplazable (`datasets-videos/`, 8,4 G) a Drive **lo maneja el usuario** (carpeta
privada, sin link público — de eso depende el "sin redistribución" del informe). Queda
del usuario: C1 (URLs de los 18 `clip.yaml` — no reconstruible desde disco) y la decisión
sobre la vista YOLO (6.338 archivos, sostiene el argumento de E-04). Spec del tramo:
`herramientas/2026-08-10-relevamientos-por-servicio-design.md`.

---

## 2026-08-10 — kit de redacción reparado para externos + reorganización del set

**Contexto que cambió el requisito:** el informe lo redactan los otros dos integrantes
del equipo, que **no participaron del tramo experimental**. El kit de redacción no
estaba listo para externos: los documentos que se autodeclaraban canónicos describían
el mundo **pre-estrato-B** (banco de 34 clips, 12 campañas, "lote sin GT", "FAR/hora no
es una métrica") con etiqueta de "verificado contra disco".

- **`informe/97` reparado** — banner de cabecera con tabla "dice / vigente" (banco
  34→47, 12→16 campañas, lote con GT, FAR/hora precisada, cobertura del verificador);
  §5.1 acotada al Bloque A; §3 corregida; **puerta de redacción LEVANTADA** (la
  redacción está habilitada y es el carril principal).
- **`informe/98` reparado** — custom instructions reescritas (banco 47 en dos bloques,
  prohibición de rankear con n=2, regla del FAR); manifiesto ampliado con `sintesis/`
  (faltaba entero) y `operacion/109/111/112/113`; aviso de que `informe-project-kit/`
  estaba viejo.
- **Glosario `13` purgado** — 5 filas muertas eliminadas + §4.1/4.2/4.3 nuevas: códigos
  `F-NN.N`/`D-NNN.N` (no estaban definidos en ninguna parte), IDs de campaña, estratos
  A/B, y las tres colisiones de símbolos (`R1–R4`/`R1–R6`/`R-01…R-26` · `D1` ·
  `A1`).
- **`GUIA-REDACTORES.md` creada** — el único documento del set cuyo lector previsto es
  un externo: proyecto en 5 minutos, orden de lectura en 5 pasos, qué NO abrir, cómo
  citar una cifra (12 ejemplos pareados), las 5 trampas, escala AF y dónde vive cada
  cosa.
- **Hallazgo 3 de `informe/99` §6 CERRADO — y la premisa era falsa:** los 11 catálogos
  de modelos **sí** declaran `license:` y `source:`; lo que faltaba era el registro —
  nueva sección "PESOS DE MODELO" en `license_registry.md` (GDINO/MM-GDINO Apache-2.0,
  YOLOE AGPL-3.0, verificados contra evidencia independiente).

**Segunda pasada de la jornada — reorganización del set para el equipo** (validación
previa: verificadores 96 y 109 corridos en verde):

- **`00-indice.md` reestructurado**: el changelog de ~9 KB en una sola línea se movió a
  este archivo (`CRONOLOGIA.md`, nuevo); se agregaron el **modelo de tres capas**
  (entrada/canónico/bitácora), el **mapa por tramos** de los 75 docs de `operacion/`,
  la sección de `sintesis/` que faltaba, la fila del **doc 108** (no estaba indexado),
  y se eliminó la fila duplicada del 102. Decisión de diseño: **el archivado es lógico
  (índice + banners), no físico** — mover/renumerar es prohibitivo (~2.800 referencias
  por número de doc, 7 scripts con rutas absolutas, y artefactos de `results/` que
  citan `docs/operacion/…` como procedencia).
- **`informe/99` puesto al día al mundo post-estrato-B**: banco 47 (T-78), filas nuevas
  T-82…T-84/FIG-F, freeze vigente `3f14f50a…` (189/189), alcance real de los dos
  verificadores en §2.2, L1/L4/L6 en su formulación vigente, bloque nuevo de mecanismos
  del tramo de video (F-103.2…D-113.2) y puerta de redacción levantada en §6.
- **`informe-project-kit/` REGENERADO** (76 archivos: 44+17+15) según `informe/98` §1,
  con `GUIA-REDACTORES.md` agregada al Nivel 1 del manifiesto; el paquete del
  2026-07-18 quedó descartado.
- **Higiene del repo `docs/`**: se eliminó `informe/desarrollo-docs/` — una
  re-exportación de los dos `.docx` (verificado: **mismo texto exacto**, 169.583 y
  870.920 caracteres, y el mismo conjunto de imágenes; solo cambiaba la numeración
  interna de los `media/`), sin una sola referencia en los 5 repos. Y se **empaquetó el
  repo por primera vez** (`git gc`: 3.272 objetos sueltos, `size-pack: 0`) ⇒ **`.git` de
  102 MB a 69 MB**, sin tocar la historia ni el árbol de trabajo (`fsck` limpio). **No
  se reescribió la historia** y es decisión deliberada: recuperaría solo 13,4 MB y
  cambiaría todos los hashes de commit, y hay **5 citas de hashes del repo `docs/`** en
  la propia documentación (`571652c` baseline, `924f972`, `a256250`).

**Tercera pasada — `informe/` partida en dos, y los ajustes ordenados por etapa.** Hasta
acá los ajustes al informe estaban dispersos: el `93` cubría **solo la Etapa 3** (26
redlines), los de Etapa 2 vivían en `nucleo/08` §2, los de Etapa 1 en
`sintesis/resultados-y-conclusiones.md` §7, y los de Etapa 5 en `informe/99` §1. **Nadie
tenía la lista completa, y nadie había mirado las etapas 4 y 5 como frente propio.**

- **La carpeta se partió en `entregable/` y `ajustes/`.** Los 17 archivos se movieron con
  `git mv`; **ningún número cambió** (se sigue citando "el doc 93", "informe/99"), y las
  ~30 referencias por ruta completa se corrigieron en `00-indice.md`, `GUIA-REDACTORES.md`,
  `adr-015`, `operacion/92`, el `97`, el `91` y `results/index.md`. No había ningún link
  markdown apuntando a esas rutas (verificado), así que no quedó nada roto.
- **Hallazgo que ordenó todo el diseño:** cada etapa tiene una **sección exacta** del
  informe, y **§17.4, §17.5 y §17.6 están literalmente vacías**
  (`[Agregado futuro correspondiente a la Etapa 4/5/6]` en el `96e`). Eso parte el trabajo
  en dos naturalezas distintas: etapas 1–3 son **corrección de texto existente**, etapas
  4–5 son **redacción desde cero** — y son el camino crítico.
- **Las etapas son seis, y se verificaron contra el Gantt.** Hubo un ida y vuelta: se
  planteó que eran cinco (con "conclusiones" como última), y **la verificación lo resolvió**
  — se extrajo `word/media/image5.jpg` del `.docx` y el **Gantt de la Figura 1 muestra seis
  tareas con sus fechas**, coincidiendo 1:1 con §14.2.1–14.2.6 (y con el §14.3, que dice
  textualmente *"las seis etapas descritas"*). El mapa quedó ordenado por las seis, con la
  tabla del Gantt como lista canónica. **Detalle que conviene recordar: el Gantt numera las
  tareas 0–5 y el §14.2 numera las etapas 1–6** — misma secuencia corrida en uno; en el set
  se usa siempre la del §14.2.
- **`AJ-0.06` nuevo:** **el informe está ordenado por sección y casi no menciona las
  etapas**, así que el lector no puede mapear el plan de trabajo (§14) con el desarrollo del
  producto (§17). Hay que meterle la tabla de correspondencia.
- **El Gantt aportó un ajuste propio (`AJ-0.03`, ERRATA):** sus fechas están vencidas —
  implementación MVP 20/03/26–29/05/26 y documentación/defensa 17/07/26–**21/08/26**,
  cuando la implementación siguió hasta agosto, el tramo experimental cerró el 08-09 y la
  defensa es ~fin de septiembre.
- **7 documentos nuevos**: el `00-mapa-de-ajustes.md` (maestro) y uno por etapa (`01`–`06`).
  Total relevado: **90 ajustes — 11 🔴 / 43 🟠 / 36 🟡-🟢**, con serie nueva `AJ-<etapa>.<nn>`
  (prefijo elegido por estar libre y no chocar con `A1–A5`, `AF-1…AF-11`, `L1–L8`, `E-01…`
  ni `T-68…T-84`). **`R-01…R-26` de Etapa 3 no se renumera**: se enruta.
- **Dos huecos de relevamiento que aparecieron al hacer el mapa**, y quedaron declarados
  como tales en vez de tapados: **`AJ-1.16`** — el **§16 Marco Teórico nunca se relevó**
  contra el estado actual del proyecto (todo el pase de Etapa 1 fue sobre el §15 y el
  Anexo A); y **`AJ-0.04`** — los **costos** (§17.2/§14.4) no se contrastaron nunca contra
  lo efectivamente gastado.
- **Categoría nueva de ajuste: 🚫 NO-TOCAR** — cinco cosas que *parecen* errores y
  corregirlas empeora el informe (la más traicionera: los nombres de métrica que aparecen
  vacíos en §17.1.7 y Tabla 33 **no** son una errata, son objetos de ecuación de Word que
  la extracción XML no captura).
- **Kit**: se sincronizaron las copias afectadas y se sumaron los 6 documentos nuevos al
  Nivel 1 (`informe/98` §1 actualizado con las rutas nuevas y con el aviso de que los
  nombres aplanados no cambian).

---

## 2026-08-09 — cierre del tramo de video: gen. 3, revisión ciega y sincronización

### Cierre de jornada: pase de sincronización de índices y procedencia (doc `operacion/113` §G)

Relevamiento completo de `results/` pedido por el usuario: los datos estaban sólidos,
la presentación no —la revisión ciega se había propagado al fondo de los docs pero no a
sus bordes—. Cerradas **6 contradicciones** (encabezado de `clip_bench` con banco de
38 → **47**; censo raíz 34 clips/12 campañas → **47 y 14**; las **tres** formulaciones
divergentes de FAR/hora unificadas en la de **L1**; `realtime/index.md` §7 que
contradecía a L1 y L6; cuerpo de la síntesis con cifras muertas; `GUIA-CIERRE.md` tres
jornadas atrás). **F-113.1, el hallazgo del pase y es de REPRODUCIBILIDAD:** los
`metrics.json` de I1/I2 traían las cifras post-revisión pero declaraban el **freeze
pre-corrección** (`299ccc19…`) ⇒ quien reprodujera obtenía 0,500 en vez de 0,333 —
causa: el agregador copia `campaign.yaml` adentro, así que **re-evaluar sin re-agregar
congela la procedencia**; corregido y regenerado **sin mover ninguna cifra**. Misma
familia: `provenance.json` de I1/I2 declaraba 4 corridas para 13 clips y NA1 no tenía
ninguna ⇒ regenerados con `datos/113-regenerar-provenance-estrato-b.py` (idempotente,
`--check`), **las 16 campañas con artefacto tienen hoy procedencia completa**.
`96-verificar-indices.py` pasó de 8 cifras a **19, cobertura 16/16, con guard que falla
si aparece una campaña sin verificar**. Los 4 artefactos secundarios quedaron
declarados (**solo 2 son supersedidos**; el control de B1 y la réplica base-560 están
VIGENTES). **El estrato B quedó integrado al CUERPO de la síntesis, §4.1 y §5.1.**
Verificadores 96/109/113 y suite datasets 418: verdes. Nada commiteado.

### Misma noche: REVISIÓN CIEGA DEL GT EJECUTADA

El resultado más fuerte del tramo de video: **5 de las 7 declaraciones de episodio del
lote eran ERRORES de anotación (~71%)**, todas sobre-declarando donde el estado no era
observable. Cayeron los 2 episodios de `v04_c02` —el ex "caso limpio"— y el de
`v01_c01`; estrato B vigente: **2 evaluables, `scene` F1 0,333 / `subject` 0,190,
Nivel A 0,031/0,018**, FAR sin cambio (3 y 190 FP en 0,1027 h). **Banco 47 = 32
positivos / 15 negativos / 37 episodios, manifest `3f14f50a…`.** Cadena completa:
correcciones firmadas → re-derivación → re-evaluación determinista (11/11) →
propagación con banners (111, 108) y notas (110, 112, índices de `results/`).
Decisiones firmadas D-113.1 (precisar L4, no L9) y D-113.2 (regla `unknown` del
scorer, declarada). CONSTANCIA citable en el doc 113 §B. **ENTRAR POR EL 113.**

### Mismo día

Gen. 3 corrida (doc 111), balance crítico (112), manual de cierre (113).

---

## 2026-08-07 (noche) — el CVAT llegando por goteo

Doc **109** = fuente única del material de video y de las campañas citables; doc
**110** = último clip integrado, `v03_c02`, banco **39 clips** — y la gen. 3 de las
campañas del estrato B **lista para correr, sin correr**, con la recomendación de
esperar los 9 clips que faltaban.

---

## 2026-08-06 — llegada del lote de internet + relevamiento integral de consistencia

**El día del CVAT del lote** (docs 102–107, con el 108 al cierre): GT del estrato B
(102, banco 34→37), campañas I1/I2 corridas (103, el hallazgo de densidad real),
ajustes probados solo con config (104), Nivel A sobre video con los 4 pilotos
recuperados (105), inventario y cómo continuar (106), matriz de knobs completa (107) —
el frente de clips quedó sin pendientes de plataforma esa misma noche.

**Y el relevamiento integral de consistencia:** se auditó todo el set — conclusiones
AF, redlines, kit de informe, alcance/ADRs, índices de `results/` (verificador
mecánico: todo verde) — y se corrigieron los desfases encontrados: **doc 10 con
ADR-015 propagado completo** (ítem 5/MQTT, cuerpos E-03/E-04/E-10/E-13, L2),
`estado-de-implementacion-adrs` (filas 001/002/005 + condicional ADR-005), glosario
doc 13 (jerarquía de verdad → 97 + `results/`, estatuto del GT, convenciones AF-x /
limitación-L vs hito-L / dos series de ADR), banner de derogación en `operacion/92`,
R-24/R-26 anotados en `informe/93`, y el índice. **Síntesis consolidada de resultados
y conclusiones: `sintesis/resultados-y-conclusiones.md`** — nuevo punto de entrada
para leer el estado del trabajo de una sola pasada.

---

## 2026-08-05 — cierre de resultados + relevamiento de datasets

Docs 92–98 cerraron el capítulo de resultados —entrar por el **98** (conclusiones
transversales) y por `results/index.md`—, el **99** relevó y ordenó los datasets de
imágenes con el registry al día y la limpieza ejecutada, y el **100** midió por
primera vez el costo de E-04/T1 (**≈1 h de GPU**, confirma el rango pre-registrado)
dejando **F-100.1 como el único bloqueo para ejercerlo**. Estado de plataforma
vigente = doc **97** (reemplaza al 56).

---

## 2026-08-04 — el tramo experimental sobre el banco del rodaje COMPLETO

**El eje de la tesis RESUELTO.** Jornada 83–90: Fase D Nivel A (gate no se dispara) →
réplica base-560 (F-84.1: la debilidad de E-DIR es estructural) → evaluador
`direct_evidence` (285 passed) → campaña D1 (**veto de precisión: E-IND confirmada
núcleo por medición**) → H1 E-HYB-or (predicción refutada; F-87.2: la unión no es
monótona en un motor temporal) → B1 bare_head (F-88.1: el caption tiene costo medido,
0,082 F1 por una palabra; F-88.3: etiqueta corta > frase negada ordena el eje) →
**G1 granularidad por sujeto = 0,930, el mejor resultado del banco** (+0,141 sobre T1
con las MISMAS detecciones; P7 0,400→1,000). Veredicto: E-IND 0,789 núcleo / E-DIR
0,160 descartada / E-HYB-or 0,296 no supera; las tres fallas explicadas POR MECANISMO.
FAR/hora declarado LIMITACIÓN, no métrica (D-90.1). Primera tanda commiteada y
pusheada (datasets `7ae79b2e`, control `5327080`, exp-setup `6f0391a`, media
`94660e6`, docs `924f972` local); segunda tanda (87–90) SIN COMMITEAR (✎ commiteada al
cierre del 08-05 — deuda git 0 en los 5 repos). **Punto de entrada: doc 90 (tablero de
decisiones) + `results/clip_bench/index.md` (tabla del informe)**. Suites:
control-plane 293 / datasets 283.
