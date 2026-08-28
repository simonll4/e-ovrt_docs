# E-OVRT-VDP - paquete de etapa 3

> Generado el 2026-08-28. Etapa 3: seccion 17.3, diseno arquitectonico.

## Que esta CERRADO y que esta ABIERTO (leer antes de redactar)

Lo **cerrado** se escribe como hecho, en pasado y sin condicionales: ya fue ejecutado y
verificado, y dejarlo como duda seria falsear el estado del trabajo. Lo **abierto** no se
escribe: se deja un marcador visible para que lo complete quien tiene el dato.

**CERRADO — se afirma:**

1. Distribucion de alertas: implementada, verificada e integrada (vista de webconsole,
   orquestacion y repositorio versionado, 2026-08-13). Su estatuto es trabajo comprometido
   con estado declarado a la entrega; los canales adicionales siguen fuera de alcance.
2. Identidad de sujeto: implementada y medida. Lo excluido son las metricas MOT.
3. Comparacion de estrategias de deteccion: ejecutada (la directa fue vetada por
   precision y la hibrida por disyuncion fue ejecutada y refutada).
4. Referencia temporal del banco: anotacion **humana** y congelada; se reporta como
   resultado, no como verificacion preliminar.
5. Rama de ajuste fino (E-04): **JORNADA COMPLETA en sus tres tramos, cerrada con
   veredictos pre-registrados** — T1 NO-GO (2026-08-17) · T2 NO-GO (2026-08-21) · T3
   cerrado con causa tecnica. Se escribe como **curva de capacidad de tres puntos** y
   como hallazgo, no fracaso. T1: rescata `bare_head` del cero (AP50 0,0000 -> 0,0455)
   pero falta 0,0045 al umbral y rompe la retencion de `person` (-11,62 %, tope 10 %).
   T2 (SGD explicito, D-FT-16): la ganancia PASA (`bare_head` -> 0,0909, el doble de T1)
   pero colapsa en entrenamiento (early stop 16/60, mejor epoca = 1) y **fallan las dos
   retenciones** (in-domain: `person` -49,7 %; open-vocabulary: COCO -71,3 %).
   **F-127.1: el fallo es ESTRUCTURAL (2.946 imagenes vs 10,35M parametros), no de
   capacidad.** Margenes y expectativas firmados ANTES de cada evaluacion, sin
   renegociar; ningun checkpoint se adopto; no hay mas brazos contra `bench_v3`.
   **Trampa de cita: T1 gana por recall CR-01, T2 por AP — no hay "mejor tuned" de
   metrica unica.** Va en tabla propia, por estrato, nunca mezclada con el nucleo
   zero-shot.
6. **Plataforma relevada de punta a punta el 2026-08-28** (`operacion/130`, seis repos, solo
   lectura): lo estructural coincide con los docs; las 26 cifras de los cuatro indices verifican
   (EXIT 0); `bench_v3` reproduce byte a byte. Lo que 130 corrigio manda sobre cualquier foto
   anterior (en particular sobre `operacion/97`).
7. **Etapa 1 del informe CERRADA** (2026-08-28): §15 + §16 en su documento v1.0, verificador OK.

**ABIERTO — no se afirma; se marca:**

1. **Procedencia de origen del lote de obra real** (direccion y fecha de acceso por
   clip): pendiente. No bloquea redactar; si bloquea cerrar la version final.
2. **Insercion de las figuras en el `.docx`.** Las seis figuras estan **PRODUCIDAS**
   desde el 2026-08-21 (PNG 300 dpi + SVG en `informe/figuras/`: vista de procesos,
   maquina de estados, calidad frente a densidad, alerta superpuesta, frontera de
   juzgabilidad, mas la FIG-D preexistente), pero **pegarlas en el documento sigue
   pendiente**: en el texto se referencian con `[[FIGURA: cual]]` y no se describe una
   figura como presente mientras la seccion no la tenga insertada.
3. **La integracion al documento maestro.** ✎ 2026-08-28: cada seccion se trabaja **en su
   propio documento** en `entregable/desarrollando/`; lo que queda al final es
   **integrarlas al maestro**, que todavia tiene §17.3/§17.4 en su version previa y §17.5 vacia. Estado:
   **Etapa 1 CERRADA** (`E-OVRT-VDP_Secciones_15_y_16_…_v1.0.docx`, cinco pases aplicados y
   verificados; texto base `90d`; solo D-E1-11 abierta) · **§17.3 v1.4 · §17.4 v1.6 · §17.5 v1.3**
   con sus tres pases APLICADOS Y VERIFICADOS (textos base `90` / `90b` / `90c`) · **§17.1 v1.3
   (Etapa 2) con el pase E2 y el de formato APLICADOS Y VERIFICADOS** el 2026-08-28 (texto base
   `90f`; quedan `90g` —Anexos C y D— y los handoffs hacia 17.3/17.4/17.5) · §17.6, §18 y §19
   sin redactar. El texto base vigente de cada etapa es SIEMPRE su extraccion
   (`90d`/`90f`/`90`/`90b`/`90c`), nunca el placeholder del maestro, los borradores ni las fotos
   `96x` del informe v1.1 (superadas para §15, §16 y §17.1).
4. **D-E1-11 — inscripcion ante la AAIP**: decision del EQUIPO, marcada con `[[PENDIENTE]]`
   en §16.6.2.2 y con marcador espejo en §17.1.11 (D-E2-7); viaja hasta que el equipo la resuelva.

### Convencion de marcadores (obligatoria)

Todo hueco se deja con doble corchete, de modo que sea localizable con una busqueda:

- `[[PENDIENTE: que falta · de que depende]]`
- `[[CIFRA: que cifra hace falta · de que indice saldria]]`
- `[[FIGURA: cual]]`

Reglas: nunca completar un marcador con una estimacion, un valor probable ni una
redaccion evasiva; nunca borrarlo para que el texto "fluya"; el marcador viaja hasta el
entregable y recien lo remueve quien aporta el dato. Un capitulo con marcadores visibles
es honesto; un capitulo que rellena huecos es indefendible.

## Como se trabaja y como se entrega (obligatorio, ✎ 2026-08-27)

**No se trabaja sobre una unidad de Drive conectada, ni editando el documento en su nube.**
Se trabaja **dentro del Project**, con estos archivos de knowledge como unica fuente: el
paquete de la etapa activa **ya contiene el texto vigente completo** de la seccion que se
esta corrigiendo (la extraccion `90`/`90b`/`90c`/`90d`/`90f` segun la etapa). No hace falta ir a
buscar el documento a ningun lado, y hacerlo empeora el resultado.

*Por que la regla existe.* En la entrega del 2026-08-27 el contenido salio bien pero
**cinco encabezados numerados contiguos perdieron su estilo de titulo** (`16.5.3`, `16.5.4`,
`16.5.5`, `16.6`, `16.6.1`): se ven como titulos y no lo son, asi que desaparecen del indice
automatico y de la numeracion de campos. El defecto aparecio al editar via Drive y no se ve
leyendo el texto. Ese ida y vuelta tambien pierde los cambios controlados.

**Forma de la entrega**, por seccion y no del documento completo:

1. Un `.docx` armado **sobre una COPIA del DOCX base** de formato, nunca sobrescribiendolo.
2. **Cada titulo con su estilo de encabezado real** (`Heading 2/3/4/5`), jamas texto en
   negrita imitando un titulo. Si se elimina una subseccion, **renumerar sus hermanas**: un
   salto (por ejemplo `16.7.1`, `16.7.2`, `16.7.6`) se ve en el indice.
3. **Con cambios controlados activados**, o en su defecto con el bloque de trazabilidad por
   unidad que piden las instrucciones del Project (diagnostico · texto propuesto ·
   trazabilidad · pendientes).
4. Sin markdown crudo pegado (`###`, `|---|`, cercos de codigo) y sin identificadores
   internos: `AJ-`, `R-`, `PODA-`, `E1-`/`E3-`/`E4-`, lineas `SHA-256`, cabeceras
   `> Seleccion:`. **Excepcion**: los codigos `P-E1-xx` de las preguntas rectoras SI son
   parte del informe.
5. Los marcadores `[[PENDIENTE: …]]` / `[[CIFRA: …]]` / `[[FIGURA: …]]` **viajan**: no se
   completan con estimaciones ni se borran.
6. **Delta de referencias explicito**: altas completas en APA 7 con DOI/URL, y bajas de lo
   que dejo de citarse. Si una obra queda citada solo desde la nota de una tabla, decirlo.

**Verificacion mecanica antes de dar una entrega por buena** (la corre el equipo, es parte
del circuito y no un extra): `python3 herramientas/verificar_entregable.py <entrega.docx>
--seccion <N>` (p. ej. `--seccion 15 --seccion 16`, o `--seccion 17.1`). Falla con titulos sin estilo, huecos de numeracion, fugas de
andamiaje, markdown crudo y citas sin entrada en referencias; e informa las referencias
huerfanas, la misma autoria con años distintos y si faltan los cambios controlados.

## Estado vigente que manda sobre el resto

- Banco temporal: **47 clips = 32 positivos + 15 negativos, con 37 episodios**. Los 34
  clips corresponden solo al Bloque A del rodaje.
- **FAR/hora se mide y se reporta**, pero la exposicion disponible no permite sostener
  una cota operativa; siempre se cita el conteo, la duracion observada y la tasa derivada.
- **G1/identidad de sujeto esta implementada y medida**. Las metricas MOT siguen fuera
  de alcance; no debe confundirse la exclusion de esas metricas con la capacidad.
- La distribucion de alertas esta **funcionalmente implementada**: los seis criterios de
  spec 45 quedaron verificados, incluido reporte y broker MQTT real. La vista de
  webconsole y la orquestacion integral se cerraron el 2026-08-13 y el repo
  `e-ovrt_alert-distribution` ya tiene historia propia. **Si aporta cifra citable**:
  `t_alert-notification` **p95 = 64,534 ms (n = 460)** entregas live, y en regimen
  sostenido **p95 = 102,025 ms (n = 104)**; mide `bus de alertas -> PUBACK MQTT`, nunca
  sensor -> notificacion (`operacion/118`).
- E-04/fine-tuning: **jornada COMPLETA y CERRADA en sus tres tramos** (✎ 2026-08-22) —
  T1 NO-GO (`operacion/123`) · T2 NO-GO (`operacion/127`) · T3 cerrado con causa tecnica
  (`operacion/117` §2, sin baseline MM-GDINO geometricamente sana el delta es
  ininterpretable), **jamas "por falta de tiempo"** (ADR-017). Ningun checkpoint se
  adopto; no hay mas brazos contra `bench_v3` (reabrir exige pre-registracion nueva,
  acta `operacion/128` §5). Reglas de cita que siguen mandando: las cifras de la rama
  van SIEMPRE en tablas propias, por estrato, jamas fundidas con el nucleo zero-shot;
  la secuencia se cuenta completa y en orden (baseline una sola vez -> margenes D-FT-12
  firmados ANTES -> veredicto T1 -> enmienda D-FT-14 DESPUES del veredicto -> margenes
  D-FT-15 pre-firmados con expectativas -> corrida y veredicto T2) porque **la
  transparencia de la secuencia ES el argumento**; T1 gana por recall CR-01 y T2 por AP
  (no hay "mejor tuned" de metrica unica); el gate de latencia de T1 no se midio y se
  dice explicito (F-123.1); F-120.1: las latencias del run de la baseline no se citan.
  Baseline YOLOE-26s (doc 120, una sola corrida sobre `bench_v3`): `bare_head` AP50
  0,000 (6.181 GT / 10 det), recall CR-01 agregado 0,0002, retencion a proteger person
  0,7843 / helmet 0,6286 / vest 0,2642. En §17.4 la fila de la Tabla 68 la fija E4-27
  (pase 3); en §17.5, el bloque ✎ 2026-08-22 de AJ-5.13.
- **Acoples vigentes (ADR-020, 2026-08-18):** los patrones de acople son DOS, no tres.
  **(a) HTTP config-driven en los TRES modulos** de la plataforma: medios `:8080`,
  control `:8081` y **distribucion `:8082`** (`eovrt-distribute serve`), con la
  webconsole y el runner como clientes de los tres — ninguno consume el bus.
  **(b) bus ZeroMQ PUB/SUB + msgpack** para el dato: detecciones `:5557`
  (medios->control), alertas `:5558` (control->distribucion).
  **NO escribir "BFF-subproceso" ni contar un tercer patron.** El subproceso del
  distribuidor sigue en el codigo como **fallback operativo**
  (`EOVRT_CONSOLE_DISTRIBUTION_TRANSPORT=subprocess`) — implementado y probado, pero
  es un detalle de operacion, no arquitectura, y no va al informe. Tampoco escribir
  "el modulo es una CLI y no un servicio": es servicio, y ademas conserva su CLI
  para el camino offline (igual que el control-plane).
  *(Historia del numero, solo para quien la necesite — ningun documento anterior al
  2026-08-18 describe el estado vigente de arriba: ADR-018 (2026-08-15) declaro que
  "la plataforma tiene TRES patrones de acople, no dos", con el tercero siendo
  **BFF-subproceso** porque el modulo de distribucion, que es CLI y no servicio,
  no tenia otra forma de acoplarse. ADR-019 (2026-08-17/18) le dio servicio HTTP
  propio al distribuidor sin cambiar el conteo — seguian siendo tres. **ADR-020**,
  el mismo dia, derogo a ADR-018 e invirtio el default: HTTP paso a ser el acople
  normal, el subproceso bajo a fallback, y volvieron a ser DOS.)*
- **Orden de arranque de una corrida live CON distribucion (✎ 2026-08-28, `operacion/130`
  R-01 — corrige a FIG-A, al CLAUDE.md raiz y a la nota de 128 §4, que decian lo contrario):**
  el runner lanza **control → distribucion → medios**: primero `POST :8081/api/runs`
  (`mode: live`, con `alert_bus.enabled` y `wait_for_subscriber_ms ≥ 10 s`), despues
  `POST :8082/api/runs` (necesita el `control_run_id`) y por ultimo `POST :8080/api/runs`. La
  no-perdida en el bus de alertas la garantiza el **handshake XPUB del publicador** (el control
  espera la suscripcion del distribuidor hasta 10 s), no el orden literal. **NO escribir
  "distribucion primero" ni "orden inverso al flujo de datos".** §17.4 v1.6 todavia lo dice
  (pendiente de la etapa 4).
- **Campeon y sus umbrales (✎ 2026-08-28, `operacion/130` R-04/R-11):** citar siempre el par
  completo `gdino-tiny-560` = 560 px · `box_threshold` **0,30** · `text_threshold` 0,25 · NMS
  IoU 0,50 · fp16. **`gdino-tiny` (800 px) corrio a 0,35**: la comparacion "560 no degrada mAP
  respecto de 800" esta confundida con el umbral en el par tiny (el par base si esta a 0,30 en
  ambos: 0,453 vs 0,401); el −24 % de latencia no depende del umbral. El **n=5.313** del recall
  CR-01 (S1/S2) es el del GT del 2026-07-23; con el GT vigente (29-jul) el denominador es 5.308
  y la medicion no se repitio: citarlo fechado. `effective_config.yaml` imprime tambien los
  campos inertes de la otra familia (`confidence_threshold 0,25` en GDINO; `box_threshold 0,35`
  en YOLOE): **GDINO usa `box`+`text`+`iou`; YOLOE usa `confidence`+`iou`**. El campo
  `run.scenario` **no clasifica** DBE/EBE (siempre dice `DBE`): se distingue por `source_type` +
  `bus.enabled`.
- **Motor de patrones (✎ 2026-08-28, `operacion/130` R-07):** **cinco** estados
  `inactive → candidate → confirmed → sustained → resolved`, alerta solo al entrar a
  `confirmed`, reapertura `resolved → candidate`; `cr01_cr02_v2` = CR-01 `high` 4.000/2.000 ms,
  CR-02 `medium` 7.000/3.000 ms, **sin cooldown** (la capacidad existe en el codigo, desactivada);
  la persistencia se implementa como **duracion desde la primera evidencia con tolerancia a
  huecos**, no como proporcion de frames positivos. Hitos persistidos 4 de 5 (la notificacion es
  del distribuidor). Causa two-node = `clock_skew` (no `cross_node_monotonic_clock`).
- **Fine-tuning y datos (✎ 2026-08-28, `operacion/130` R-02/R-03):** el entrenamiento efectivo
  (`finetuning_v1`, T1/T2) uso `construction_site_safety` 2.203 + `ppe_siabar` 743 = **2.946
  train / 483 val** y **EXCLUYO `chv`** por anti-leakage (el 100 % de `chv` es estrato del banco);
  "css + chv + ppe_siabar" es el rol TRAIN **historico** (`train_v2`, archivado 08-15) y NO se
  escribe como lo entrenado. El protocolo (Tabla 28 de §17.1) acotaba el split a 500–2.000
  imagenes: **2.946 es una desviacion que se declara** (100 % de linajes elegibles tras dedup y
  exclusion del banco; F-127.1 muestra que aun asi es insuficiente). Los checkpoints ajustados
  **solo se evaluaron en DBE-imagenes**, nunca en clips ni EBE (ΔSDR/Δt_alert/ΔTTFD no existen).
  De los 9 datasets de la Tabla 26 de §17.1 solo SHEL5K y CHV se usaron (como fuentes del banco);
  css y ppe_siabar, los que se entrenaron, no figuran en esa tabla.
- **G2A y la cadena temporal (✎ 2026-08-28, `operacion/130` R-17):** el G2A medido va del
  **dequeue** (el proceso ya leyo el frame) al **fin de la inferencia**; el tramo sensor→dequeue
  (`capture_to_host`, 202–217 ms) existe **solo para OAK-D** — para RTSP ese tramo **no se midio**
  (no "se suma", falta). NVDEC no se uso (decodificacion por software). El SO real es Linux/WSL2,
  no Windows 11 como decia el protocolo.
- **La containerizacion SI se puede mencionar en el informe** (✎ 2026-08-18, precision del
  usuario). ✎ 2026-08-28 (`operacion/130` R-09): **esta DEFINIDA y validada por configuracion**
  desde el 2026-08-19/20 — Dockerfiles en los tres repos de servicio y `infra/platform/` con el
  compose de 13 servicios y paridad de rutas; lo que sigue **pendiente y diferido a post-entrega
  es el build y el smoke integral** (nunca se corrieron). Su razon de ser es la
  **reproducibilidad** (que un tercero levante la plataforma en otra maquina), y su documentacion
  operativa vive en los repositorios, no en la tesis. **Como escribirla:** "definida y validada
  por configuracion; despliegue no verificado", como trabajo comprometido con su causa, en el
  cierre (§17.6/§18) y en el camino de reproducibilidad (§19). **Como NO escribirla:** ni
  "diferida" (ya esta escrita), ni en presente como capacidad desplegada, ni con instrucciones
  de despliegue — el informe no es un manual. *Describir el compromiso y su fundamento es correcto; describir un despliegue
  que no corrio es falso.*
- **Metricas de `report.json`**: `t_alert-system` es **citable** (esta en el diccionario de
  la spec 40 §5.1 y siempre debio figurar; dejo de estar clavada en `not_applicable`).
  `precision_alertas` / `recall_alertas` / `F1_alertas` **existen pero NO son citables**:
  duplican cifras que ya se reportan via `evaluate-alerts` con denominadores por estrato.
  **La citabilidad esta materializada**: `t_alert-system` ES la columna `t_alert` del
  clip bench (campo `t_alert_system_ms` de cada `metrics.json`) — citable por campana y
  por condicion, nunca promediada entre campanas. ✎ 2026-08-28 (`operacion/130` R-05): esa
  cifra es un **PROMEDIO por campana** — `evaluate-alerts` no produce percentiles ni persiste
  latencias por episodio; los **P50/P95/P99** existen solo para el tramo de plataforma
  (`summary.json` de medios y control: G2A, `processing_ms`, `ttfa_internal`) y para
  `t_alert-notification` (`metrics.json` de la campana 118). Decirlo cuando se cite. Y
  `t_alert-system` cierra en el **reloj de fuente del frame que confirmo** (`alert.timestamp_ms`),
  no en el registro interno monotónico. NO confundir con `t_alert-notification`
  (bus→PUBACK, la campana de distribucion): son tramos con relojes distintos y **los
  percentiles no se suman entre tramos** — la cadena temporal completa se cita POR TRAMOS
  segun la tabla de `results/index.md`.
- Las cifras se toman del índice raíz `results/index.md` (limitaciones L1–L8 y procedencia)
  más los 4 índices canónicos (`bench_imagenes`, `bench_nivel_a`, `clip_bench`,
  `realtime`), incluidos en la sección de resultados operativa. Ante una contradiccion,
  manda este estado, luego el banner mas reciente de la fuente y finalmente su cuerpo
  historico.

## Contrato de uso

- **Etapa activa:** 3 - Etapa 3: seccion 17.3, diseno arquitectonico.
- Este archivo contiene el texto vigente que se modifica y sus insumos de ajuste.
- No se trasladan resultados propios hacia secciones cronologicamente anteriores.
- Nombre propio de esta etapa (01-etapa-3-activa.md): regenerarla no pisa el paquete de ninguna otra etapa.

---

## Fuente: `docs/informe/entregable/desarrollando/archivado/correcciones-etapa-3-4.md`

> SHA-256 del bloque: `51874c00197c596a36df9bf27427a83a27bdb09ac860a614a9c8efd6fb1b7011`  
> Seleccion: pase de cierre 1 (2026-08-19): YA APLICADO - NO volver a aplicarlo; sus decisiones D1-D4 y la regla de autocontención SIGUEN RIGIENDO. Excepcion (✎ 2026-08-28, D-E2-2): el bautismo E-DIR/E-IND/E-HYB de D3/C-1 no quedo en §17.1 en su momento (E3-42 lo hizo nacer en §17.3.6.4); la etapa 2 lo aplica ahora en §17.1.5.4.2 y §17.3.6.4 debera recortar su glosa a una remision (dependencia inversa, pase 3 §I).

# Correcciones para cerrar §17.3 (Diseño Arquitectónico) y §17.4 (Implementación)

**Fecha:** 2026-08-19 · **Insumos:** `E-OVRT-VDP_Seccion_17.3_Diseno_Arquitectonico_v0.1.docx`,
`E-OVRT-VDP_Seccion_17.4_Implementacion_v0.1.docx`, `observaciones-etapa-3-4.txt` (41 comentarios, todos resueltos acá).
**Verificación:** todos los valores citados fueron contrastados contra los repos el 2026-08-19 (ver §D).
**✎ 2026-08-20:** se agrega la enmienda **E4-19** (amplía §17.4.8 — la construcción del banco temporal se
documenta como desarrollo; enmienda a E4-14) con sus hechos verificados propios al final de §D.
**Este archivo es fuente del project-kit** (etapas 3 y 4): al cambiar algo acá, regenerar el kit.
La sección §E da la renumeración de tablas y figuras que resulta de aplicar todo lo anterior.

---

## Decisiones firmadas (rigen todo el documento)

- **D1 — Término único:** el evento que publica el plano de medios se llama **"evento de percepción"**
  (denominación de diseño: *PerceptionEvent*). El nombre *DetectionEvent* se elimina del informe.
  El contrato que lo materializa se llama por su id: `media.detection.v1`.
- **D2 — Doctrina de reparto entre etapas:** §17.3 es **conceptual y paramétrico** — patrones de acople y
  tecnologías elegidas CON su justificación (son decisiones de diseño), pero **sin puertos numéricos, sin
  tablas de endpoints, sin tabla de correspondencia diseño→materialización y sin valores numéricos del
  patrón**. §17.4 es **concreto y efectivo** — puertos, endpoints, correspondencia, vista de procesos
  (FIG-A) y valores efectivos de configuración. Excepción coherente: la **máquina de estados (FIG-E) es
  diseño** → vive en §17.3.8.2; §17.4 la referencia sin repetirla.
- **D3 — Códigos de estrategia:** se agrega un mini-ajuste en **§17.1.5.4.2** que bautiza E-DIR / E-IND /
  E-HYB (ver §C-1). §17.3/§17.4/§17.5 los usan con un recordatorio breve al primer uso.
- **D4 — Justificación del núcleo-solo:** párrafo dedicado en **§17.4.10** + eco breve en las conclusiones.
  La justificación **nunca** es "falta de tiempo" (ver E4-17).
- **Regla de autocontención (GUIA §3.1):** el informe no referencia documentos locales, ADRs, fichas ni
  índices del repositorio. Todo texto sugerido acá ya cumple esa regla; no agregar citas internas.
- Los "textos guía" son orientativos: ChatGPT puede reformularlos manteniendo el contenido y el registro
  académico del informe (decimales con coma; milisegundos como "4.000 ms").

---

## A. Correcciones a §17.3 — Diseño Arquitectónico

### E3-01 · §17.3.3.1, Tabla 40 — justificación del núcleo-solo *(obs 2 / comentario C0)*
**Sin cambio en 17.3.** La justificación de por qué solo se implementó el núcleo validable se desarrolla
en §17.4.10 (ver E4-17). Opcional: no agregar nada acá; la Tabla 40 ya declara el tratamiento de cada
capacidad.

### E3-02 · §17.3.3.4, Tabla 43 — eliminar la columna "Estado" *(obs 3 / C1)*
Todas las filas dicen "Adoptada": la columna no discrimina nada.
1. Eliminar la columna **Estado**.
2. En DA-11, quitar la marca "(opcional)": el texto de la decisión ya dice "variante opt-in… deshabilitada
   por defecto".
3. Reescribir la Nota (hoy menciona "decisiones condicionadas" que ya no existen en la tabla).
   **Texto guía:** *"Nota. Las decisiones fijan reglas estructurales adoptadas para el diseño del prototipo
   experimental. Su materialización y verificación se documentan en la sección 17.4."*

### E3-03 · §17.3.5 — quitar "webconsole" y "runner" del diseño *(obs 4 / C2)*
En diseño, los nombres concretos quedan sin contexto. Reemplazar en el párrafo del comentario C2:
*"la webconsole y el runner no consumen directamente los buses"* →
**"la interfaz de inspección y el orquestador experimental gobiernan el ciclo de vida mediante las
interfaces de gobierno de cada módulo y no consumen directamente los buses"**.
Aplicar el mismo criterio en §17.3.10.2 (*"la webconsole y el runner lo gobiernan…"* → *"la interfaz de
inspección y el orquestador experimental lo gobiernan…"*). Los nombres concretos (webconsole, runner) se
introducen recién en §17.4.1 como materialización del soporte experimental.

### E3-04 · §17.3.5 — reescribir el párrafo de materialización: sin puertos y CON justificación de tecnologías *(obs 5 y 6 / C3)*
El párrafo actual ("La materialización de esta vista distingue dos patrones…") enumera puertos
(:8080/:8081/:8082/:5557/:5558) — eso migra a §17.4 (D2). En su lugar, el diseño debe **justificar** la
elección de cada tecnología. **Texto guía (reemplaza el párrafo completo):**

> *"La materialización de esta vista distingue dos patrones de acople complementarios. El gobierno de las
> corridas se realiza mediante interfaces HTTP gobernadas por configuración en los tres módulos
> ejecutables. Se adopta HTTP porque el ciclo de vida de una corrida —crear, consultar, cancelar, cerrar—
> tiene semántica de solicitud y respuesta, admite múltiples clientes sin acoplarlos entre sí y permite
> disponer los módulos en un mismo host o en hosts distintos sin modificar su lógica; el gobierno por
> configuración garantiza que cada corrida declare sus parámetros en lugar de heredarlos de constantes
> ocultas. El intercambio de datos en ejecución se realiza mediante un bus ZeroMQ con patrón
> publicador-suscriptor y serialización binaria msgpack: un canal de detecciones entre los planos y un
> canal de alertas hacia la distribución. Se adopta ZeroMQ porque ofrece transporte de baja latencia sin
> requerir un broker como dependencia adicional del prototipo, y el patrón publicador-suscriptor desacopla
> al productor de sus consumidores sin bloquear la ruta crítica; msgpack reduce el costo de serialización
> respecto de texto plano conservando estructuras autodescriptivas. La durabilidad no se le exige al canal:
> cada hecho se persiste en archivos JSONL de sólo adición antes de publicarse, de modo que la evidencia
> pueda releerse y reevaluarse sin depender de la mensajería. La persistencia JSONL cumple esa función de
> durabilidad y relectura —inspeccionable, de sólo adición y sin introducir una base de datos como
> dependencia del núcleo— y no constituye un tercer patrón de acople. HTTP gobierna configuración y ciclo
> de vida; el bus transporta hechos de ejecución."*

### E3-05 · Figura 4.2 (vista de procesos) — mover a §17.4.1 *(obs 6 / C4)*
La vista de procesos con puertos es concreción de implementación (D2) y §17.4.1 ya tiene el placeholder de
esa misma figura. Acciones:
1. Eliminar de §17.3.5 la Figura 4.2 con su nota (van a §17.4.1, ver E4-02).
2. §17.3 conserva solo la Figura 4.1 (vista conceptual).
3. Renumerar las figuras siguientes de §17.3 (mapa completo en §E).
4. Enmienda al plan de figuras: FIG-A tiene destino único §17.4.1 (ver §C-2).

### E3-06 · §17.3.6.2 — "ejecución experimental": ya resuelto *(obs 7 / C5)*
Sin cambio: el término quedó bien definido acá (unidad lógica identificada por `experiment_id`).
El rezago de "corrida paraguas" está en §17.4 (ver E4-15).

### E3-07 · §17.3.6.4 — recordatorio de las estrategias al primer uso *(obs 8 / C6)*
Depende del mini-ajuste en §17.1.5.4.2 (§C-1). En §17.3.6.4, donde dice *"…se mantienen en conjuntos
separados para E-DIR y E-HYB…"*, anteponer el recordatorio:
**"…para las estrategias directa (E-DIR) e híbrida (E-HYB) definidas en la consolidación metodológica
(§17.1.5.4.2)…"**. La Tabla 39 y la Tabla 45 pueden seguir usando los códigos sin glosa (la prosa ya los
ancló). En §17.3.9.2 mantener la expansión que ya existe ("estrategia indirecta basada en evidencia
positiva con inferencia espacial de ausencia (E-IND)") — está bien como está.

### E3-08 · §17.3.8.2, Figura 4.5 — la máquina de estados queda ACÁ; limpiar el placeholder doble *(obs 9 / C7)*
Decisión D2: FIG-E es diseño → vive en §17.3.8.2. Acciones:
1. La figura tiene hoy DOS notas (la spec provisoria "La figura deberá representar…" y la nota final).
   Dejar **una sola figura con una sola nota** (conservar la nota final, que es la definitiva).
2. La figura se dibuja con los **cinco estados**: inactive → candidate → confirmed → sustained → resolved
   (verificado contra el motor; ver §D).
3. En §17.4.3 se elimina el placeholder duplicado y se referencia esta figura (ver E4-04).
4. Enmienda al plan de figuras: FIG-E destino §17.3.8.2 (ver §C-2).

### E3-09 · §17.3.8.3 y Tabla 46 — el motor se DISEÑA acá; los valores numéricos migran a §17.4.6 *(obs 10 y 11 / C8, C9)*
Respuesta a la duda de fondo: **§17.3.8.3 se queda** — desarrolla el motor como diseño (qué evalúa, con qué
reglas, con qué estados y granularidad), que es exactamente lo que corresponde a la etapa 3. Lo que NO
corresponde son los **valores numéricos efectivos**, que ya están duplicados en §17.4.6 (D2). Acciones
sobre la Tabla 46:
1. Fila "Criterio temporal": *"Confirmación: 4000 ms para PR-01 y 7000 ms para PR-02"* →
   **"Ventana de confirmación expresada en milisegundos, declarada por patrón."**
2. Fila "Histéresis y cierre": quitar los valores →
   **"Ventana de resolución expresada en milisegundos, declarada por patrón."**
3. Fila "Umbrales y precondiciones de evidencia": quitar los valores →
   **"Confianza mínima del sujeto y del EPP, y área mínima del sujeto, declaradas por patrón; umbrales de
   postproceso declarados en la configuración del plano de medios."**
4. Fila "Región de evaluación": quitar los porcentajes →
   **"Franja vertical y margen lateral relativos a la caja del sujeto, declarados por patrón (región
   cefálica para PR-01; torso para PR-02)."**
5. Fila "Severidad configurada": quitar high/medium →
   **"Severidad conceptual asignada por patrón desde el catálogo metodológico."**
6. Reescribir la Nota: **"Nota. La tabla define los componentes de una definición de patrón de riesgo. Los
   valores adoptados para el núcleo validable se documentan junto a la configuración efectiva en la
   sección 17.4.6. Los tiempos se expresan en milisegundos para conservar su significado ante distintas
   cadencias de procesamiento."**
7. Verificar que §17.4.6 conserve TODOS los valores desplazados (ya tiene ventanas y severidades; agregar
   los umbrales de evidencia del patrón y las regiones — ver E4-11).
8. Ajustar la frase que introduce la tabla en §17.3.8.2 (*"Los parámetros efectivos del núcleo, incluidos
   los criterios espaciales de CR-01 y CR-02, se sintetizan en la Tabla 46"*), que quedaría falsa sin los
   valores → **"Los componentes de una definición de patrón, incluidos los criterios espaciales de CR-01
   y CR-02, se sintetizan en la Tabla 46; los valores adoptados para el núcleo se documentan en la
   sección 17.4.6."**

### E3-10 · §17.3.10 — reescribir la apertura de la distribución para engancharla con la cadena *(obs 12 / C10)*
El problema es que §17.3.10.1 arranca en seco. **Texto guía para un párrafo puente inicial (antes del
contenido actual de 17.3.10.1):**

> *"La cadena descripta hasta aquí termina en un hecho interno: el plano de control registra una alerta
> cuando un patrón confirma un episodio. Falta el último tramo: hacer llegar esa alerta a un canal externo
> sin comprometer al motor que la produjo. De ese tramo se ocupa el módulo de distribución. El plano de
> control publica cada alerta confirmada en un bus de alertas dedicado; el módulo de distribución la
> consume desde allí, aplica la política de notificación y registra el resultado de cada intento de
> entrega. No forma parte del razonamiento del patrón ni constituye un tercer plano: es un módulo
> desacoplado que transforma una alerta ya confirmada en intentos de entrega observables."*

Además, por D2, en §17.3.10.2 quitar los puertos: *"El dato de distribución viaja por el bus de alertas
:5558. El módulo expone una interfaz HTTP config-driven en :8082…"* → **"El dato de distribución viaja por
el bus de alertas dedicado. El módulo expone su propia interfaz de gobierno para crear, consultar, cancelar
y cerrar corridas de entrega…"**. La Tabla 48 se conserva (es diseño: consumidores y salidas).

### E3-11 · §17.3.10.3 — aclarar qué es "el motor" *(obs 13 / C11)*
Reescribir: *"El motor posee una capacidad técnica de control de re-confirmación, pero no se utiliza como
política del núcleo"* → **"El motor de patrones del plano de control posee una capacidad técnica de
control de re-confirmación, pero la decisión de diseño adoptada no la utiliza en el núcleo: la supresión
de re-notificación —cooldown, agrupación o limitación de tasa— pertenece a la política del módulo de
distribución."** (Y eliminar la oración siguiente que quedaría redundante.)

### E3-12 · Tabla 50 — término único del evento *(obs 14 / C12)*
Fila "DetectionEvent" → **"PerceptionEvent"** (misma función y contenido; la columna de información mínima
sigue citando `media.detection.v1`). Con D1 no debe quedar ninguna aparición de "DetectionEvent" en §17.3.

### E3-13 · §17.3.11.3 — eliminar la Tabla 61 y la Tabla 62 de §17.3 *(obs 14 y 15 / C13, C14)*
Por D2, la correspondencia diseño→materialización (Tabla 61) y el inventario de interfaces con puertos
(Tabla 62) pertenecen a §17.4 (allí ya existen; ver E4-05/E4-06). Acciones:
1. Eliminar de §17.3.11.3 la Tabla 61 completa (con eso desaparece también el comentario C13).
2. Eliminar la Tabla 62 completa. Las dos filas de buses y las filas de distribución que solo estaban acá
   se incorporan a la Tabla 62 de §17.4 (ver E4-06).
3. Conservar el párrafo *"El evento central del sistema es media.detection.v1…"* (es diseño del contrato).
4. Conservar las invariantes de `clip_gt.v2` y los cinco hitos temporales (párrafos posteriores).
5. Renumerar las tablas del capítulo tras la eliminación (mapa completo en §E — ojo: hoy los números de
   las Tablas 61–64 de §17.3 COLISIONAN con los de §17.4).

### E3-14 · §17.3.12.1 — mover el árbol de directorios `runs/` a §17.4 *(obs 16 / C15)*
El listado del repositorio por ejecución es materialización (D2) y hoy aparece en seco. Acciones:
1. Eliminar el bloque `runs/<experiment_id>/ …` de §17.3.12.1; la prosa de principios (sólo adición, sin
   sobrescritura, agrupación por `experiment_id`) se conserva.
2. Incorporarlo en §17.4.7 como cuadro con introducción (ver E4-13).

### E3-15 · Tablas 52, 64 y 53 — VALIDADAS, sin cambios de fondo *(obs 17 / C16, C17, C18)*
Se verificó contra los repos: nombres de métricas y tramos, definiciones operacionales (G2A desde el
dequeue, capture_to_host solo con ancla temporal, SDR solo comparable a igual cadencia, re-alertas ≠ FP),
estados de aplicabilidad (computed / applicable_not_computed / not_applicable / not_interpretable) y los
esquemas `media.metric.v2` / `control.metric.v1`. Quitar los tres comentarios; no hay correcciones.

### E3-16 · §17.3.14 — abreviar el desarrollo DBE/EBE *(obs 18 / C19)*
La definición de los escenarios ya está en §17.1.3.3 y §17.1.4.4 (con las Tablas 19 y 20). Acciones:
1. Comprimir §17.3.14.1 y §17.3.14.2 a **un párrafo cada uno**, eliminando lo que repite la definición
   metodológica y conservando solo la lectura arquitectónica (DBE: fuente pulleable, prioridad de
   reproducibilidad; EBE: fuente viva, instrumentación de temporalidad). Abrir con una remisión:
   **"La definición metodológica de ambos escenarios corresponde a la sección 17.1.4.4; aquí se conservan
   únicamente sus consecuencias arquitectónicas."**
2. Conservar §17.3.14.3 (equivalencia arquitectónica) completo — es el aporte propio de esta etapa.
3. En la Tabla 54, eliminar las filas que no derivan una implicancia arquitectónica nueva ("Objetivo
   experimental" y "Riesgo principal" repiten metodología; conservar fuente, control temporal,
   instrumentación adicional, métricas prioritarias y condición de comparabilidad).
4. Conservar §17.3.14.5 y §17.3.14.6 (alcance arquitectónico y naturaleza temporal — son diseño).

### E3-17 · §17.3.14.5, Tablas 55 y 56 — eliminar el código "EN-2" *(obs 19 / C20, C21)*
El código EN-2 quedó huérfano: la tabla de modos del EN (EN-0/EN-1/EN-2) existía en la versión anterior de
la etapa 3 y desapareció en esta reescritura. Respuesta a "¿se utilizó?": la preselección está implementada
en el código (opt-in, deshabilitada por defecto, fail-open — verificado), pero quedó fuera de los
experimentos finales, así que no se reporta como resultado. Acciones:
1. §17.3.14.5: *"La variante EN-2 es opcional…"* → **"La variante de preselección liviana en el borde es
   opcional, deshabilitada por defecto y fail-open…"**
2. Tabla 55, fila "EN-2" → **"Preselección en el borde"** (mismo contenido).
3. Tabla 56, fila EN: *"La preselección EN-2 es opcional…"* → **"La preselección liviana es opcional…"**,
   y en la misma fila *"(modo base EN-1)"* → eliminar el código: **"EN (modo base de captura)"**.
4. Verificar que no quede ningún "EN-1"/"EN-2" en §17.3 ni en §17.4.

### E3-18 · Barrido final de puertos en §17.3 *(consecuencia de D2)*
Quitar todo puerto numérico restante:
- §17.3.8.1: *"por el canal de detecciones :5557"* → **"por el canal de detecciones del bus"**.
- §17.3.15 (prosa): *"gobernada por HTTP en :8082 y consumidora del bus de alertas :5558"* →
  **"gobernada por su propia interfaz HTTP y consumidora del bus de alertas"**.
- Tabla 56, fila Módulo de distribución: *"Servicio HTTP config-driven en :8082…"* →
  **"Servicio gobernado por configuración con interfaz HTTP propia, co-ubicable con el CPN o desplegable
  por separado"**; y en Responsabilidades: *"desde el bus :5558"* → **"desde el bus de alertas"**.
- Tabla 59, fila Tramo de distribución: *"Gobernar la corrida por HTTP en :8082, consumir control.alert.v1
  desde el bus :5558…"* → **"Gobernar la corrida por su interfaz HTTP, consumir control.alert.v1 desde el
  bus de alertas…"**.
- §17.3.18 (cierre) ya está sin puertos: no tocar.

---

## B. Correcciones a §17.4 — Implementación

### E4-01 · §17.4.1 — borrar las menciones a las CLI preliminares *(obs 23 / C0, C1)*
1. Eliminar: *"Sus utilidades históricas de línea de comandos se conservaron como herramientas auxiliares
   y dejaron de constituir la interfaz principal."*
2. Eliminar: *"la interfaz de línea de comandos se conservó para la relectura offline"* (la relectura DBE
   queda descripta por el modo replay del servicio; ver Tabla 62).

### E4-02 · §17.4.1 — la vista de procesos (FIG-A) se materializa ACÁ *(cierra E3-05)*
El placeholder ya existe. La figura incorpora los tres servicios con sus puertos (:8080, :8081, :8082),
el soporte experimental como cliente HTTP, el módulo de distribución **con línea continua** (es un servicio
más, no un apéndice), los dos buses (:5557 detecciones, :5558 alertas), el repositorio de corrida y el
orden de disparo. La nota que acompañaba a la Figura 4.2 de §17.3 se adapta como nota de esta figura.

### E4-03 · §17.4.1 — distribución como servicio HTTP *(obs 24 / C2)*
Reescribir el párrafo del módulo de distribución. **Texto guía:**

> *"El módulo de distribución de alertas constituye un cuarto componente funcional y no un tercer plano.
> Al igual que los dos planos, se ejecuta como un servicio gobernado por configuración con interfaz HTTP
> propia. Consume las alertas confirmadas desde el bus de alertas, aplica la política de notificación,
> controla idempotencia y supresión, entrega por MQTT con confirmación de calidad de servicio y conserva
> un registro de entregas de sólo adición (ledger). La vista de resultados de entrega y el lanzamiento
> desde la orquestación quedaron integrados."*

### E4-04 · §17.4.3 — eliminar el placeholder de la máquina de estados *(obs 9 / cierra E3-08)*
Eliminar el placeholder `[[FIGURA: máquina de estados…]]` y su marca. En el párrafo de
`control.pattern_state.v1`, referenciar: **"…las transiciones entre los estados inactive, candidate,
confirmed, sustained y resolved (figura de la sección 17.3.8.2)…"** — sin número hardcodeado: la figura
cambia de número con la renumeración de §E.

### E4-05 · Tabla 61 — reemplazar los "No aplica" por el mecanismo real de trazabilidad *(obs 25 y 26 / C3, C4, C5)*
No se inventan versiones nuevas en el código: el versionado de esos contratos existe por otros mecanismos y
la columna debe decir cuáles. Con la Tabla 61 de §17.3 eliminada (E3-13), esta pasa a ser la única.
1. Renombrar la columna **"Esquema o versión"** → **"Versionado y trazabilidad"**.
2. Reemplazos fila por fila:
   - SourceDefinition: "No aplica" → **"Esquema de configuración; congelado por el manifiesto"**
   - ModelProfile: → **"Catálogo versionado; un archivo por variante"**
   - PromptDefinition: → **"prompt_set_id registrado en cada corrida"**
   - FrameMetadata: → **"Contrato interno; viaja dentro del evento publicado"**
   - PatternDefinition: → **"Conjunto de patrones versionado (pattern set)"**
   - ErrorEvent: → **"Esquema por componente, registrado por corrida"**
   - Repositorio de eventos: → **"Esquemas de cada evento persistido"**
   - Reporte experimental: → **"Proyección regenerable de los artefactos primarios"**
3. Fila "PerceptionEvent / DetectionEvent" (D1): la denominación de diseño queda **"PerceptionEvent"**, la
   materialización **"Evento de percepción normalizado"**, versión `media.detection.v1`.
4. La Nota se simplifica: ya no hay "sin versión propia".

### E4-06 · Tabla 62 — única tabla de interfaces del informe *(obs 27 y 28 / C6, C7)*
1. **Eliminar la fila** "GET /healthz y GET /readyz" (acordado con tu colega).
2. **Agregar las filas de distribución (:8082):** `POST /api/runs` (inicia una corrida de entrega con
   fuente de alertas, política, canal e identificador de experimento); `GET /api/runs/{id}` (estado);
   `POST /api/runs/{id}/cancel` (cancela); `GET /api/config` (configuración efectiva).
3. **Agregar las dos filas de buses** (vienen de la Tabla 62 eliminada de §17.3):
   medios → control, ZeroMQ PUB/SUB + msgpack en :5557, transporta `media.detection.v1` y el ciclo de vida
   dentro de `bus.envelope.v1`; control → distribución, ídem en :5558, transporta `control.alert.v1`.
4. **Agregar la fila de clientes:** runner y webconsole como clientes HTTP de los tres servicios; gobiernan
   corridas y consolidan artefactos; no consumen los buses de datos.
5. Precisión verificada: NO existe `cancel` en el plano de medios (el verbo real es `stop`) ni en el plano
   de control. No listarlos; la Nota existente ("interfaces de administración y detención") los cubre.

### E4-07 · §17.4.5 y Tabla 63 — DOS patrones de acople, no tres *(obs 29 / C8)*
El acople BFF-subproceso fue reemplazado por la interfaz HTTP del módulo de distribución y ya no es un
patrón de la plataforma (queda solo como contingencia operativa interna, que el informe no necesita
mencionar). Acciones:
1. §17.4.5 primer párrafo: *"tres patrones técnicos de acople"* → **"dos patrones técnicos de acople"**.
2. Tabla 63: eliminar la fila "BFF-subproceso" y su Nota.
3. Fila "HTTP gobernado por configuración": Participantes → **"Soporte experimental, plano de medios,
   plano de control y módulo de distribución"**.
4. Nueva Nota. **Texto guía:** *"Nota. Los dos patrones separan gobierno y datos: HTTP gobierna
   configuración y ciclo de vida de los tres servicios; el bus transporta los hechos de ejecución."*

### E4-08 · §17.4.5 — borrar el párrafo de la parada cooperativa *(obs 30 / C9)*
Eliminar completo: *"La parada de fuentes de red se implementó de manera cooperativa…"*.

### E4-09 · §17.4.5 — dockerización: reproducibilidad, sin "dos nodos" *(obs 31 y 37 / C10)*
Reemplazar *"El despliegue EBE en dos nodos se contenedorizó y verificó con imágenes separadas por rol,
sin modificar los contratos de los planos."* por un desarrollo breve de la idea. **Texto guía:**

> *"La plataforma se contenedorizó con imágenes separadas por rol funcional. La finalidad no es la
> distribución física, sino la reproducibilidad del despliegue: cada imagen congela las dependencias, la
> versión de código y la configuración de arranque de su rol, de modo que el entorno de ejecución deje de
> ser una variable implícita de la corrida. El arranque ordenado de los servicios —control antes que
> medios, conforme al orden de suscripción del bus— se declara en la composición y no depende de pasos
> manuales. Los contratos entre módulos no distinguen si los servicios comparten host o no; la topología
> efectiva de cada corrida se registra en su configuración. En los experimentos del presente trabajo, los
> servicios se ejecutaron co-ubicados en un único host con GPU; la separación por roles se conserva como
> organización lógica del despliegue, no como topología exigida."*

(Nota interna, no va al informe: al cierre se consolida la infra dockerizada en los repositorios para que
el texto y el código coincidan.)

### E4-10 · §17.4.6 — borrar la oración de milisegundos *(obs 32 / C11)*
Eliminar: *"Los tiempos se expresan en milisegundos y no en cuadros, por lo que su significado se conserva
frente a cambios de cadencia."* — ya está dicho en §17.3.8.2 y en la nota de la Tabla 46.

### E4-11 · §17.4.6 — supresión como decisión de diseño + valores del patrón completos *(obs 33 / C12, y cierre de E3-09)*
1. Reescribir: *"El conjunto de patrones oficial opera con granularidad de escena y no configura supresión
   de re-alertas. El motor dispone de esa capacidad, pero la configuración adoptada la mantiene desactivada
   porque…"* → **Texto guía:** *"El conjunto de patrones oficial opera con granularidad de escena. En
   coherencia con la decisión de diseño que separa la alerta interna de su comunicación (DA-13), el motor
   registra cada confirmación sin supresión: el cooldown, la agrupación y la limitación de tasa pertenecen
   a la política del módulo de distribución."*
2. Completar los valores del patrón que migran desde la Tabla 46 (E3-09). Agregar tras las ventanas:
   **"Las precondiciones de evidencia exigen confianza mínima de 0,35 y área mínima de 400 píxeles
   cuadrados para el sujeto, y confianza mínima de 0,25 para el elemento de protección. La región de
   búsqueda se define de forma relativa a la caja del sujeto: para CR-01, la franja superior entre el 0 %
   y el 45 % de la altura con margen lateral del 12 %; para CR-02, la franja del torso entre el 25 % y el
   85 % con margen lateral del 8 %."** (Valores verificados contra el pattern set; ver §D.)

### E4-12 · §17.4.6 — catálogo de modelos y corrección del umbral *(obs 34 / C13 + discrepancia verificada)*
Reescribir el párrafo del perfil desplegado. Dos correcciones obligatorias: **box_threshold es 0,30, no
0,35** (verificado en el perfil del campeón y en los registros de las campañas oficiales), y
"confidence_threshold" no es un umbral del carril Grounding DINO. **Texto guía:**

> *"La estrategia perceptiva del núcleo utiliza evidencia positiva: person como entidad y helmet y vest
> como elementos de protección. La ausencia se infiere en el plano de control y no se consulta como una
> negación opaca al detector. El catálogo de perfiles de modelo materializa la sustituibilidad prevista en
> el diseño: incluye variantes de Grounding DINO (tiny y base, con resolución de entrada de 800 y de 560
> píxeles), de MM-Grounding DINO y de YOLOE, todas integradas mediante adaptadores sobre el mismo contrato
> de salida. El perfil desplegado para el núcleo es grounding-dino/gdino-tiny-560, seleccionado en la
> comparación de modelos que se presenta en la sección 17.5. Su configuración efectiva fija el umbral de
> caja en 0,30 y el umbral de texto en 0,25; el postproceso aplica confianza mínima de 0,25, supresión de
> solapamientos con IoU de 0,50 y área mínima de caja de 100 píxeles cuadrados; el control de ritmo opera
> con selección determinista de paso 1 y una cola máxima de ocho unidades. Estos valores quedan persistidos
> con cada corrida y no dependen de constantes ocultas en el código."*

### E4-13 · §17.4.7 — incorporar el árbol del repositorio de corrida *(cierra E3-14)*
El árbol que estaba en §17.3.12.1 no coincidía con el layout real: la consolidación del soporte
experimental **copia los artefactos livianos y referencia los pesados** (exactamente lo que ya dice la
Nota de la Tabla 64) — verificado contra los repositorios de ejecución reales el 2026-08-19. Después de
la Tabla 64, insertar con introducción. **Texto guía:**

> *"Cada plano conserva su repositorio completo por corrida (el plano de medios: detecciones, métricas,
> errores, resumen, configuración efectiva, manifiesto y procedencia; el plano de control: transiciones,
> alertas, métricas, errores, resumen y configuración efectiva). El soporte experimental consolida la
> ejecución experimental copiando los artefactos livianos y referenciando los pesados:"*

```
runs/<experiment_id>/                (repositorio del soporte experimental)
  manifest.effective.yaml
  media/      summary.json · metrics.jsonl · effective_config.yaml ·
              detections.ref.json   (referencia al detections.jsonl del plano de medios)
  control/    alerts.jsonl · pattern_events.jsonl · metrics.jsonl ·
              summary.json · effective_config.yaml
              (y la evaluación temporal, cuando la corrida la habilita)
  report/     report.json · report.md
```

Cuando el tramo de distribución está habilitado, su ledger y su reporte se consolidan del mismo modo.
En la Nota de la Tabla 64: *"…se referencian en la corrida paraguas…"* → **"…se referencian en la ejecución
experimental…"** *(rezago del término detectado)*.

### E4-14 · §17.4.8 — CVAT con nombre propio; podar los detalles de exportación *(obs 35 y 36 / C14, C15, C16)*
Reescribir la sección completa. **Texto guía:**

> *"La evaluación temporal se apoya en una referencia humana de episodios por clip, materializada mediante
> el esquema clip_gt.v2. Para la anotación de los videos se seleccionó CVAT, una herramienta de anotación
> de código abierto con soporte de interpolación temporal y exportación estructurada, que permite anotar
> episodios sobre video con esfuerzo humano acotado. Su salida se procesa mediante una cadena reproducible
> de separación, derivación de la referencia temporal, validación, promoción y agregación; la cadena valida
> la estructura de cada exportación antes de derivar, y las anotaciones promovidas quedan congeladas bajo
> control de versiones. La herramienta de anotación funciona así como instrumento de captura: la referencia
> experimental es la versión promovida en el repositorio."*

(Se eliminan: el párrafo del nivel de exportación proyecto/tarea con su error simétrico, y el párrafo de
correcciones firmadas — quedan cubiertos por "valida la estructura" y "congeladas bajo control de
versiones". El marcador `[[PENDIENTE: dirección de origen…]]` se conserva.)

> ✎ **2026-08-20 — ENMENDADO por E4-19.** La sección se amplía en cuatro subsecciones en lugar de
> comprimirse: este texto guía queda subsumido en E4-19 (que conserva CVAT con nombre propio y la doctrina
> de instrumento de captura, y elimina la frase "con esfuerzo humano acotado"). No aplicar E4-14 suelto.

### E4-15 · Tabla 65 — despliegue contenedorizado sin "dos nodos" *(obs 37 / C17 en su antecedente)*
Fila "Despliegue en dos nodos" → **"Despliegue contenedorizado por rol"**; evidencia →
**"Los servicios se construyeron como imágenes por rol y se ejercieron sin modificar los contratos entre
planos."** Estado: Verificada (eso sí ocurrió).

### E4-16 · Tabla 66 — eliminar las filas/celdas de lo que no se hizo *(obs 37 y 38 / C17, C18)*
1. **Eliminar la fila completa** "Latencia captura-resultado en topología de dos nodos" (los experimentos
   finales se ejecutaron en un solo nodo; la regla general de relojes queda en §17.3.13.2, que no afirma
   ejecución).
2. Fila "Paridad DBE/EBE sobre fuente equivalente": eliminar la celda-consecuencia actual (*"La
   sincronización explícita entre reloj de captura…"*) y reemplazar por **"La reevaluación offline de una
   corrida live produce artefactos equivalentes; la paridad de transporte y relectura queda verificada."**
3. **Actualizar la fila de la rama de ajuste fino** (quedó desactualizada): *"la corrida completa fue
   autorizada y encolada en el nodo de entrenamiento"* → **Texto guía:** *"Protocolo, procedencia, servicio
   de inferencia, evaluación y línea base quedaron congelados. El primer tramo ejecutado se evaluó contra
   el banco congelado y no superó los criterios de incorporación predefinidos; un tramo exploratorio
   adicional permanece en ejecución."* El marcador `[[PENDIENTE: …]]` se conserva hasta el veredicto final.
   (Regla de encuadre: la rama es condicionada por datos y protocolo, nunca "por falta de tiempo".)

### E4-17 · §17.4.10 — párrafo nuevo: por qué solo el núcleo validable *(obs 2 / C0 de §17.3)*
Insertar después del primer párrafo de §17.4.10 (antes de la Tabla 66). **Texto guía:**

> *"La concentración del prototipo en el núcleo validable no responde a una reducción tardía del alcance,
> sino a las condiciones de evaluabilidad de cada condición del catálogo. Las condiciones de Nivel 1
> cuentan con datasets públicos y bancos de evaluación con verdad de terreno para persona y elementos de
> protección personal, lo que permite medir percepción, estado temporal y alerta con denominadores
> declarados. Las condiciones de Nivel 2 y Nivel 3, en cambio, exigen insumos que el material disponible no
> provee: verdad de terreno de andamios, arneses, bordes desprotegidos o zonas restringidas; definiciones
> externas de zona y geometría de cámara controlada; y evaluadores relacionales o de trayectoria cuya
> validación requeriría bancos propios que no existen en el dominio. Incorporarlas sin esa base habría
> producido capacidades no medibles, contrarias al criterio metodológico de no convertir extensiones en
> dependencias del flujo base. El esfuerzo experimental se concentró, en cambio, en llevar el núcleo a
> capacidad medida: la misma decisión que limitó la cantidad de condiciones cubiertas es la que permite
> reportar cada resultado con su evidencia."*

(Eco breve en las conclusiones cuando se redacte esa etapa — no repetir el argumento, solo reafirmarlo.)

### E4-18 · Barrido general anti-redundancia con §17.3 *(obs 32, criterio general)*
Además de E4-10, revisar que §17.4 no re-explique reglas ya establecidas en el diseño; donde haga falta el
concepto, referenciar la sección de §17.3. Casos concretos detectados:
- §17.4.4 último párrafo y §17.4.5 tercer párrafo repiten el orden de suscripción ya diseñado en §17.3.8.4:
  conservarlo UNA vez en §17.4.5 (como condición de corrección verificada) y quitar la repetición de
  §17.4.4 (dejar solo *"En una corrida live, la respuesta afirmativa del plano de control implica que su
  consumidor ya está suscripto"*).
- §17.4.5: *"El patrón publicador-suscriptor no retiene mensajes emitidos antes de la suscripción"* puede
  abreviarse remitiendo al diseño (*"conforme a la restricción de suscripción previa establecida en la
  sección 17.3.8.4"*).

### E4-19 · §17.4.8 — ENMIENDA a E4-14 (✎ 2026-08-20): la construcción del banco temporal es desarrollo y se documenta *(revisión de cobertura post-cierre)*

**Motivo.** La revisión de cobertura del 2026-08-20 confirmó que el trabajo de preparación del material
—rodaje guionado, lote de obra real de internet, recorte temporal con criterios previos, preanotación
asistida y revisión humana en CVAT— quedó reducido a una mención instrumental, siendo parte del desarrollo
experimental efectivamente ejecutado (herramientas construidas, operaciones realizadas, artefactos
producidos). E4-14 se enmienda: se **conserva** de él CVAT con nombre propio y la doctrina "instrumento de
captura / la referencia experimental es la versión promovida"; se **reemplaza** su texto guía por la
sección ampliada de abajo; y se **elimina** la frase "con esfuerzo humano acotado" (no hay medición de
horas que la respalde y minimiza una actividad intensiva en revisión).

**Reparto que la enmienda respeta** (no cargar §17.4.8 con lo que no le toca):
- Los denominadores y la composición del banco (clips, positivos/negativos, episodios, evaluables por
  bloque) van en **§17.5** (AJ-5.07 / T-78) — acá NO se cita ningún conteo.
- La cadena de comandos y la trampa del export a nivel proyecto/tarea van al **anexo de reproducibilidad
  (§19, AJ-6.02)**; en §17.4.8 queda una sola cláusula ("valida la estructura de cada exportación antes de
  derivar"). Esto resuelve la tensión pendiente con AJ-4.09.
- La lección de los identificadores de la interfaz de CVAT vs. el XML es material de §17.5 (AJ-5.07).

**Nota de sustento (no va al informe):** la afirmación "criterios fijados antes de ejecutar las campañas"
es verificable y verificada — criterios publicados el 2026-07-18/19 (pre-rodaje), constantes en código
(`window.py`, gate A1 de `derive_clip_gt.py`), recortes del Bloque A congelados el 2026-07-28 (seis días
antes de la primera campaña), lote de internet sin recortar, episodio censurado nunca "rescatado".
Detalle en §D (hechos 2026-08-20). Los únicos cambios post-hoc fueron de anotación GT, firmados y en
contra del sistema (revisión ciega), nunca de límites de clip.

**Acciones:**
1. Retitular: **"17.4.8. Construcción del banco temporal y de la referencia humana de evaluación"**, con
   cuatro subsecciones (17.4.8.1–17.4.8.4).
2. En §17.4.1, tras *"La cadena de datos comprende adquisición, validación, conversión y congelamiento de
   datasets y bancos de evaluación."*, insertar: **"Para el banco temporal de video esa cadena comprende
   la adquisición y curación del material, la preparación y segmentación temporal de los clips, la
   anotación asistida con revisión humana y la derivación, validación y congelamiento de la referencia;
   su construcción se documenta en la sección 17.4.8."**
3. Reemplazar el cuerpo de §17.4.8 por el párrafo de apertura y los cuatro textos guía siguientes. El
   marcador `[[PENDIENTE: dirección de origen…]]` se conserva, al cierre de 17.4.8.1.

**Texto guía — apertura de §17.4.8:**

> *"La evaluación temporal se apoya en una referencia humana de episodios por clip, materializada mediante
> el esquema clip_gt.v2. Su construcción comprendió la adquisición y conformación del material audiovisual,
> la preparación y segmentación temporal de los clips, la anotación asistida con revisión humana y la
> derivación, validación, promoción y congelamiento de la referencia. Para la anotación se seleccionó CVAT,
> una herramienta de código abierto con soporte de interpolación temporal y exportación estructurada."*

**Texto guía — 17.4.8.1. Adquisición y conformación del material audiovisual:**

> *"El material del banco proviene de dos fuentes con procedencia y grado de control experimental
> distintos, y esa diferencia se conserva como atributo de cada clip. La primera fuente es un rodaje
> guionado ejecutado con el hardware real de captura del prototipo: cada escenario se diseñó en función de
> una condición de riesgo del núcleo, con un guion segundo a segundo que fija la entrada del sujeto en
> cumplimiento, el inicio diferido de la infracción y su persistencia sostenida durante lapsos muy
> superiores a las ventanas de confirmación de los patrones, e incluye escenas negativas y escenas
> deliberadamente por debajo del umbral de confirmación. Las tomas se registraron con margen temporal
> adicional respecto del clip previsto, para que el recorte fino fuera una operación posterior y
> controlada; la grabación y el recorte se realizaron desde la propia consola del prototipo, que incorpora
> esa capacidad. La segunda fuente es un lote de obra real no guionada obtenido de videos públicos de
> internet, incorporado como bloque separado con criterios de selección definidos de antemano: material de
> obra en cumplimiento destinado a medir especificidad y falsos positivos —no sensibilidad—, prohibición de
> concatenar segmentos cortos para fabricar unidades largas, y exclusiones declaradas con causa y firma en
> lugar de descartes silenciosos."*
>
> `[[PENDIENTE: dirección de origen y fecha de acceso por clip del lote de obra real · depende de completar
> la ficha de procedencia primaria antes del cierre final del informe]]`

**Texto guía — 17.4.8.2. Preparación y segmentación temporal de los clips:**

> *"Los videos maestros se conservaron sin modificación y las unidades de evaluación se generaron como
> clips derivados, con criterios temporales explícitos fijados antes de ejecutar las campañas y aplicados
> como reglas ejecutables, no como juicio caso por caso. Cada clip del rodaje se recortó con un preludio
> fijo de 3,5 s antes del inicio de la condición —el inicio nunca coincide con el primer fotograma, porque
> un episodio que arranca en el origen impide medir el tiempo hasta la primera detección—, una cola
> posterior al cierre del episodio de entre 3 y 10 s según el escenario, y un piso de duración que
> garantiza que una alerta válida pero lenta pueda ocurrir dentro del clip: el inicio del episodio más el
> techo del objetivo de latencia de alerta de su patrón, más la ventana de resolución y un margen final.
> Ese piso se verifica mediante un control automático durante la derivación de la referencia, y el clip que
> no lo alcanza no se vuelve a recortar: sus métricas de latencia y sensibilidad quedan censuradas y así se
> declaran. El fundamento del dimensionamiento es bidireccional: un clip demasiado corto subestima al
> sistema, porque produce latencias artefactuales y cuenta como omisión una alerta que no tuvo tiempo de
> ocurrir; un clip sin tiempo muerto sobreestima la precisión, porque elimina los tramos donde aparecen los
> falsos positivos. El dimensionamiento correcto elimina ambos artefactos, de modo que cada métrica resulte
> atribuible al sistema y no al recorte. La selección de tomas se realizó por criterio visual de calidad de
> la escena, no por duración, y los límites de todos los clips quedaron congelados bajo control de
> versiones antes de ejecutar las campañas que los evalúan. Los clips del lote de internet no se
> segmentaron: cada uno es el video original completo, porque recortarlos alteraría precisamente el tiempo
> negativo que ese bloque aporta a la medición de falsos positivos."*

**Texto guía — 17.4.8.3. Preanotación asistida y revisión humana en CVAT:**

> *"La anotación no partió de video crudo. Cada clip se preanotó automáticamente con un detector de
> vocabulario abierto de mayor capacidad que el modelo evaluado —elección deliberada para evitar
> circularidad entre el sistema medido y su referencia— acoplado a un algoritmo de seguimiento que propone
> trayectorias por sujeto, con los atributos de protección inicializados por asociación espacial. Sobre esa
> propuesta se realizó la pasada humana en CVAT: revisión y corrección de cajas y trayectorias,
> verificación de identidades a lo largo de la secuencia, asignación de los atributos observables por
> tramo, marcación explícita como estado desconocido de los tramos donde el atributo no resulta observable
> —en lugar de forzar un valor—, y fijación de los límites temporales de cada episodio. La interpolación
> temporal y la preanotación redujeron las operaciones repetitivas, pero no sustituyeron la revisión humana
> de las trayectorias, los atributos ni los límites de cada episodio: la construcción de la referencia fue
> una actividad intensiva en revisión, no un etiquetado manual fotograma por fotograma ni una validación
> automática."*

**Texto guía — 17.4.8.4. Derivación, validación, promoción y congelamiento:**

> *"La salida de la anotación se procesa mediante una cadena reproducible de separación, derivación,
> validación, promoción y agregación. La cadena valida la estructura de cada exportación antes de derivar,
> y la derivación clasifica los episodios con las mismas ventanas de confirmación que utiliza el motor de
> patrones —4.000 ms para CR-01 y 7.000 ms para CR-02—, de modo que la referencia y el sistema evaluado
> apliquen un criterio temporal idéntico; una divergencia entre ambos produciría omisiones ficticias. Las
> correcciones humanas posteriores a la derivación se aplican como registros firmados sobre los artefactos
> versionados —nunca editando la herramienta de anotación— y un control automático falla cuando una
> corrección firmada no aparece en la referencia derivada. Las anotaciones promovidas quedan congeladas
> bajo control de versiones, con huella criptográfica por clip y un manifiesto agregado del banco. CVAT
> funciona así como instrumento de captura: la referencia experimental es la versión promovida en el
> repositorio, no el estado mutable de la herramienta."*

---

## C. Ajustes fuera de los dos documentos

### C-1 · Mini-ajuste en §17.1.5.4.2 (etapa 2) — bautizar las estrategias *(decisión D3)*
En el pasaje que distingue formulaciones directas de indirectas, insertar los códigos. **Texto guía:**

> *"En este trabajo, estas familias se identifican como estrategia directa (E-DIR), cuando el prompt
> intenta describir la condición de riesgo completa; estrategia indirecta (E-IND), cuando el detector
> identifica entidades visibles por separado y la condición se reconstruye mediante lógica externa al
> modelo; y estrategia híbrida (E-HYB), cuando se combinan consultas de ambos tipos bajo una regla de
> composición explícita. Estos códigos identifican las variantes en el diseño arquitectónico y en la
> evaluación experimental."*

Es un ajuste quirúrgico sobre una sección ya integrada en Google Docs (regla D-A: se corrige directo en el
maestro).

### C-2 · Enmienda al plan de figuras (manual 08 §6 / materiales 99)
- **FIG-E** (máquina de estados): destino **§17.3.8.2** (Figura 4.5), con los **cinco** estados
  (inactive → candidate → confirmed → sustained → resolved) — resuelve además la discrepancia del plan,
  que la rotulaba con tres estados. §17.4.3 la referencia sin figura propia.
- **FIG-A** (vista de procesos): destino **único §17.4.1** (ya no va también en §17.3.5). En §17.3 queda
  solo la Figura 4.1 conceptual.
- La puerta P4 de §17.4 pasa a exigir solo FIG-A.

### C-3 · Recordatorios de cierre (no van al informe)
- Al cerrar cada sección en el maestro: re-extraer el `.md` y fechar en `entregable/00-el-informe-hoy.md`
  (regla D-C).
- El eco del encuadre "núcleo-solo" queda anotado para el pase de conclusiones (etapa 5/6).
- Consolidar la infra dockerizada en los repositorios antes del cierre final, para que E4-09 quede
  respaldado 1:1 por el código.

---

## D. Hechos verificados (2026-08-19) — NO "corregir" estos valores

Verificados contra los repositorios; cualquier texto que los contradiga está mal, no ellos.

| Hecho | Valor verificado | Fuente |
|---|---|---|
| Ventanas CR-01 | confirmación 4.000 ms · resolución 2.000 ms · severidad high | `e-ovrt_control-plane/configs/patterns/cr01_cr02_v2.yaml` |
| Ventanas CR-02 | confirmación 7.000 ms · resolución 3.000 ms · severidad medium | ídem |
| Evidencia del patrón | sujeto ≥ 0,35 y ≥ 400 px² · EPP ≥ 0,25 (campo único para helmet/vest) | ídem |
| Regiones | CR-01: 0–45 % superior, margen 12 % · CR-02: 25–85 %, margen 8 % | ídem |
| Cooldown | NO configurado en el pattern set; el cooldown vive en distribución (default 30 s) | pattern set + `eovrt_distribution/policy.py` |
| Estados del motor | inactive, candidate, confirmed, sustained, resolved (los 5, exactos) | `pattern_engine.py` |
| Perfil campeón | `grounding-dino/gdino-tiny-560` · **box_threshold 0,30** (no 0,35) · text 0,25 · image_size 560 | `configs/models/grounding-dino/gdino-tiny-560.yaml` + `results/*/campaign.yaml` |
| Postproceso | min_confidence 0,25 · IoU 0,50 · área mínima 100 px² | `eovrt_media/config/schemas.py` |
| Control de ritmo | stride 1 (determinista) · cola máxima 8 | ídem |
| Catálogo de modelos | 11 perfiles: gdino tiny/base × 800/560 · mm-gdino tiny/base/large · yoloe 26s/m/l/x · mock · +ft-t1 | `e-ovrt_media-plane/configs/models/` |
| Endpoints medios (:8080) | healthz, readyz, /api/model, POST/GET /api/runs, GET detections, POST/GET evaluate, **stop (no cancel)**, dropped, artifacts, websockets | routers del servicio |
| Endpoints control (:8081) | POST/GET /api/runs, GET alerts, pattern-progress, pattern-events, received-units, /api/config, healthz/readyz · **sin cancel** | ídem |
| Endpoints distribución (:8082) | POST/GET /api/runs, **POST /api/runs/{id}/cancel**, /api/config, healthz/readyz | ídem |
| Esquemas | media.detection.v1 · control.pattern_state.v1 · control.alert.v1 · control.notification.v1 · control.delivery.v1 · bus.envelope.v1 · run.lifecycle.v1 · media.metric.v2 · control.metric.v1 — todos existen con ese nombre exacto | contracts de los 3 repos |
| Preselección en borde | implementada, `enabled: False` por defecto, fail-open estructural; fuera de los experimentos finales | `schemas.py` + `oak_d_source.py` |
| Pruebas | 2.203 aprobadas en cinco suites (relevamiento integral) | constancia operacional |
| Puertos | medios :8080 · control :8081 · distribución :8082 · bus detecciones :5557 · bus alertas :5558 | servicios + CLAUDE.md |
| Repo de ejecución consolidado | `manifest.effective.yaml` + `media/` (livianos + `detections.ref.json`) + `control/` (livianos) + `report/` — los pesados se referencian, no se copian | `experimental-setup/runs/exp_*` |

### Hechos verificados 2026-08-20 (sustento de E4-19) — NO "corregir" estos valores

| Hecho | Valor verificado | Fuente |
|---|---|---|
| Recorte del rodaje (constantes en código) | pre-roll **3,5 s** · cola 3,0 s default / 5,0 s (P2) / 10,0 s (P4) · duraciones objetivo por escenario (P1 20 · P2 30 · P3 15 · P5 15 · P9 18 s) | `webconsole/.../clips/window.py` (`PRE_ROLL_S`, `SCENARIO_TAIL_S`, `SCENARIO_TARGET_S`) |
| Gate A1 (dimensionamiento) | onset del primer episodio ≥ 2.000 ms · piso por episodio = inicio + techo de t_alert (10.000 ms CR-01 / 20.000 ms CR-02) + resolución (2.000/3.000 ms) + 2.000 ms de cola | `e-ovrt_datasets/datasets/scripts/videogt/derive_clip_gt.py` (`MIN_ONSET_MS`, `DIMENSIONING_MS`) |
| Derivación ↔ motor | mismas ventanas de confirmación **4.000/7.000 ms** (pattern set v2), selladas en `provenance.pattern_set_ms` de los 47 GT | `derive_clip_gt.py` + `clip_bench/gt/*.json` |
| Preanotación | **GDINO-base + ByteTrack** — variante MÁS fuerte que el campeón evaluado (anti-circularidad); atributos por asociación espacial | `eovrt_media.tools.preannotate_video` + `datasets/registry/clip_bench.md` |
| Lote de internet | **SIN recortar**: los 14 manifiestos llevan "El clip ES el master SIN RECORTAR (doc 59 §6)"; exclusión única (`v08_c01`) firmada con causa, pre-anotación | `datasets-videos/v*.clip.yaml` |
| Cronología ex-ante | criterios publicados 2026-07-18/19 (doc 57, pre-rodaje) · rodaje 07-25 · recortes del Bloque A congelados **2026-07-28** (commit `f637875b`) · primera campaña **2026-08-03** · cada campaña declara el sha256 del manifiesto usado | git de `e-ovrt_datasets` + `results/clip_bench/*/campaign.yaml` |
| Censura respetada | el episodio censurado (`a_p1_c05` ep2, `clip_too_short_for_t_alert_window`) atravesó TODAS las campañas censurado; el clip nunca se re-recortó (un solo commit) | `clip_bench/gt/a_p1_c05.json` + git |
| Prohibición ex-ante de re-recorte | "se anota como hallazgo, no se re-recorta para 'arreglarlo'" | doc 72 (manual de recorte) |
| Guion del rodaje | onset a los 3–4 s · persistencias sostenidas **14 s** (CR-01) / **22 s** (CR-02) · escena sub-umbral de 2 s guionada y cronometrada | doc 69 (guion operativo) |
| Cambios post-hoc (los únicos) | adjudicaciones de `unknown` firmadas (F-GT1, limitación L3) y revisión ciega 08-09 (movió F1 0,500 → 0,333, EN CONTRA del sistema) — anotación GT, **nunca límites de clip** | commits `f7a27fe6` / `7961ac62` + doc 113 §B |

---

## E. Renumeración de tablas y figuras (consecuencia de aplicar §A y §B)

Hoy los números COLISIONAN: §17.3 tiene Tablas 61/62/63/64 intercaladas fuera de orden (entre la 50 y la
51) que repiten los números de las Tablas 61–67 de §17.4. Tras eliminar las Tablas 61 y 62 de §17.3
(E3-13), la renumeración queda así (la numeración definitiva la fija el maestro al integrar):

**Tablas de §17.3** — 39 a 50 sin cambio; luego, en orden de aparición en el documento:

| Número actual | Contenido | Número nuevo |
|---|---|---|
| Tabla 63 | Superficie de crecimiento del evento de percepción (§17.3.11.4) | **51** |
| Tabla 51 | Hechos persistibles mínimos (§17.3.12.2) | **52** |
| Tabla 52 | Métricas y evidencias por tramo (§17.3.13.1) | **53** |
| Tabla 64 | Diccionario de métricas (§17.3.13.2) | **54** |
| Tabla 53 | Señales observables (§17.3.13.3) | **55** |
| Tabla 54 | Comparación DBE/EBE (§17.3.14.4) | **56** |
| Tabla 55 | Condiciones observables para interpretar EBE (§17.3.14.5) | **57** |
| Tabla 56 | Roles funcionales y unidades desplegables (§17.3.15) | **58** |
| Tabla 57 | Riesgos arquitectónicos (§17.3.16) | **59** |
| Tabla 58 | Plan de materialización del núcleo (§17.3.17) | **60** |
| Tabla 59 | Capacidades complementarias (§17.3.17) | **61** |
| Tabla 60 | Criterios de cierre (§17.3.18) | **62** |

Referencias en prosa de §17.3 a actualizar: *"La Tabla 63 explicita…"* (§17.3.11.4) → **51**;
*"La Tabla 54 resume…"* (§17.3.14.4) → **56**. Las referencias a las Tablas 39–50 no cambian.

**Tablas de §17.4** — corren +2 para continuar desde la 62 final de §17.3: 61→**63** (correspondencia),
62→**64** (interfaces), 63→**65** (patrones de acople), 64→**66** (artefactos), 65→**67** (verificación),
66→**68** (brechas), 67→**69** (extensibilidad). Referencias en prosa: *"La Tabla 61 establece…"*
(§17.4.2) → **63**; *"La Tabla 66 evita…"* (§17.4.10) → **68**.

**Figuras de §17.3** — tras mover la Figura 4.2 a §17.4.1 (E3-05): 4.1 sin cambio; 4.3→**4.2** (flujo del
plano de medios), 4.4→**4.3** (flujo del plano de control), 4.5→**4.4** (máquina de estados, FIG-E),
4.6→**4.5** (cadena de traducción), 4.7→**4.6** (roles CPN/EN/TN). La prosa de §17.3 no referencia
figuras por número, así que solo cambian los rótulos.

**Figura de §17.4** — la vista de procesos (FIG-A, §17.4.1) toma el número consecutivo siguiente
(**4.7**), sujeto al esquema de numeración del maestro al integrar.

---

## Fuente: `docs/informe/entregable/desarrollando/archivado/correcciones-etapa-3-4-pase-2.md`

> SHA-256 del bloque: `425ac974e295664e517b0ada5df5732a72fbcf3105f70e548774feb910ad551d`  
> Seleccion: pase de cierre 2 (2026-08-20): YA APLICADO Y VERIFICADO en el documento de trabajo (2026-08-23) - NO volver a aplicarlo; sus decisiones D-P2-1..6 siguen rigiendo como criterio de lectura.

# Correcciones — pase 2 sobre §17.3 (Diseño Arquitectónico) y §17.4 (Implementación)

**Fecha:** 2026-08-20 · **Insumos:** `E-OVRT-VDP_Seccion_17.3_Diseno_Arquitectonico_v1.1.docx` y
`E-OVRT-VDP_Seccion_17.4_Implementacion_v1.2.docx` (las versiones vigentes, ya con el pase 1 aplicado).
**Verificación:** todos los conteos, duplicaciones y citas de este documento fueron contrastados contra
esos dos `.docx` el 2026-08-20 (ver §D, con el procedimiento para re-verificarlos).

**Relación con el pase 1** (`archivado/correcciones-etapa-3-4.md`, ítems E3-01…E3-18 y E4-01…E4-19):
este pase **continúa la numeración** y **no re-abre** ninguna de sus decisiones. Las decisiones firmadas
del pase 1 (D1 término único, D2 doctrina 17.3-conceptual / 17.4-concreto, D3 códigos de estrategia,
D4 justificación del núcleo-solo, regla de autocontención) **siguen rigiendo**. Dos unidades de este pase
son consecuencia directa de aplicar el criterio del pase 1 donde había quedado sin aplicar (E3-19 y E4-21).

**Numeración de tablas usada acá:** la **vigente en los `.docx`** (§17.3 = Tablas 39–62; §17.4 = Tablas
63–69), es decir la que ya resulta de §E del pase 1. Aplicar este pase la vuelve a mover: el mapa nuevo
está en §E.

> ✅ **Nota operativa (no es contenido del informe) — RESUELTA.** El generador del project-kit apuntaba a la
> ruta vieja de `correcciones-etapa-3-4.md` (movida a `archivado/` el 2026-08-20) y `--check --etapa all`
> fallaba. Corregido: hoy el generador toma **ambos pases** —el 1 desde `archivado/` y el 2 desde acá— en
> las etapas 3 y 4, `--check --etapa all` da **OK** y los 36 tests del generador pasan
> (verificado 2026-08-22).

> ✎ **Estado al 2026-08-22.** Al pase original (E3-19…E3-28 · E4-20…E4-22 · C-01…C-04) se agregaron
> **E3-29, E3-30, E3-31, E4-23, E4-24, E4-25** y **E4-26**, las decisiones **D-P2-5** y **D-P2-6**, y una
> **enmienda a E3-28**. Ninguna toca el mapa de tablas de §E (E4-24 y E4-25 agregan **filas** a las Tablas
> 63 y 64, no tablas; E4-26 retitula §17.4.6); sí se agregó a §E el corrimiento de **subsecciones**, que
> faltaba.

---

## Decisiones que rigen este pase

- **D-P2-1 — Criterio de tabla.** Una tabla se justifica cuando **se consulta, no se lee**: filas
  estrictamente paralelas sobre los mismos atributos, celdas cortas, y el valor está en comparar *entre*
  filas. Corolarios que se aplican de forma mecánica en §A y §B:
  1. **Dos columnas = una lista con bordes.** No es una tabla.
  2. **Dos filas = una oración.**
  3. **Una columna cuyas celdas dicen todas lo mismo = una columna que sobra.**
  4. **Celdas de más de ~120 caracteres = prosa maquetada en grilla.**
- **D-P2-2 — Nada de lo que se elimina se pierde.** Ninguna unidad de este pase elimina un compromiso de
  diseño: cada tabla que sale se reemplaza por texto que en tres casos **ya existe** en el párrafo
  introductorio o en la Nota contigua.
- **D-P2-3 — El momento es ahora.** §17.5 y §17.6 todavía no están redactadas y numerarían desde la
  Tabla 70. Podar después obliga a renumerar dos veces y a corregir referencias ya escritas. Aplicado este
  pase, §17.5 arranca en la Tabla **63**.
- **D-P2-4 — Alcance declarado.** Este pase cubre §17.3 y §17.4. Las secciones cerradas se relevaron y su
  resultado se informa en §F, pero **no se tocan acá**.
- **D-P2-5 — Identificadores versionados de contratos (✎ 2026-08-22, extiende D2 sin reabrirla).** §17.3
  nombra los contratos por su **denominación conceptual** (la de la Tabla 50 y de la columna "Contrato del
  diseño" de la Tabla 63: evento de percepción / PerceptionEvent, alerta interna / AlertEvent, referencia
  temporal de evaluación, …). Los **identificadores de cable con sufijo de versión**
  (`media.detection.v1`, `clip_gt.v2`, `bus.envelope.v1`, …) y los literales de protocolo (`run_finished`)
  son **materialización efectiva** y pertenecen a §17.4, cuyo punto de declaración es la Tabla 63. §17.3
  conserva **el compromiso de versionado enunciado en abstracto** (la regla de evolución de §17.3.11.4 y
  "la versión viaja dentro del payload"). Excepción coherente, espejo de la de FIG-E en D2: los **nombres
  de estados** de la máquina de patrones (`inactive`…`resolved`) son vocabulario del diseño y se quedan en
  §17.3.8.2. Fundamento y aplicación: **E3-31** y **E4-23**.
  **Límite de la regla — NO sobre-aplicar.** D-P2-5 alcanza **sólo** al sufijo de versión del esquema y a
  los literales de protocolo. **Se quedan en §17.3**, y quitarlos sería un error: (a) los **nombres de
  campo** que el diseño decide que crucen la frontera —`experiment_id`, `run_id`, `unit_id`, `source_id`,
  `track_id`, `detection_id`, `prompt_set_id`, `clip_id`—, porque *qué información cruza* es diseño;
  verificado que §17.4 no los redeclara (`unit_id`, `source_id`, `track_id`, `detection_id` y `clip_id`
  aparecen **cero veces** en §17.4, de modo que sacarlos de §17.3 los dejaría huérfanos en todo el informe);
  (b) las **tecnologías con su justificación** (ZeroMQ, patrón publicador-suscriptor, msgpack, JSONL de sólo
  adición, HTTP, MQTT con QoS 1), que D2 y E3-04 ya fijaron como diseño; (c) los **nombres de estados** de
  la máquina de patrones. La prueba práctica: si el término nombra *qué* se intercambia o *por qué*, es
  diseño; si nombra *la versión concreta del esquema* o *el literal que viaja por el cable*, es §17.4.
- **D-P2-6 — Un identificador literal se declara una vez; la prosa se lee en castellano** (✎ 2026-08-22;
  completa a D-P2-5, que resolvió *en qué etapa* van, no *cuántas veces*). Fundamento medido: de los 11
  identificadores del par, **9 son `.v1`** — el sufijo varía en dos casos, así que en la enorme mayoría de
  las apariciones no aporta información y sólo quiebra el registro del texto. Reglas:
  1. **La prosa usa siempre la denominación en castellano** ("evento de percepción", "alerta interna",
     "envoltorio del bus", "contrato de ciclo de vida", "referencia temporal de evaluación"). Un
     identificador literal nunca es sujeto gramatical de una oración del informe.
  2. **Cada identificador aparece una sola vez**, y esa vez es la **Tabla 63** de §17.4.2 — el único punto
     de declaración. Sí se mantiene el identificador en prosa cuando **la versión o el literal son el
     argumento del párrafo** (hoy, sólo la glosa de la referencia temporal en §17.4.8, ver E4-23).
  3. **El CamelCase queda como está**: es la denominación de diseño que fijó D1 y aparece **sólo en celdas
     de tabla** (verificado: cero en prosa en ambas secciones). No se persigue.
  Aplicación: **E3-31** deja §17.3 en cero identificadores; **E4-24** aplica las reglas 1 y 2 a §17.4.
- **Heredadas del pase 1:** regla de autocontención (el informe no referencia documentos locales, ADRs,
  fichas ni índices del repositorio — todos los textos guía de este archivo ya la cumplen) y carácter
  orientativo de los "textos guía" (pueden reformularse conservando contenido y registro académico;
  decimales con coma, milisegundos como "4.000 ms").

---

## A. Correcciones a §17.3 — Diseño Arquitectónico

### E3-19 · §17.3.3.4, Tabla 43, fila DA-03 — la columna "Justificación" no justifica

**Problema (tres capas, la primera es dura):**

1. **Contradice al párrafo que introduce la tabla**, dos renglones antes: *"Estas decisiones **no fijan
   tecnologías concretas**, pero establecen reglas estructurales…"*. DA-03 fija tres (HTTP config-driven,
   ZeroMQ PUB/SUB con msgpack, JSONL). Misma página.
2. **La celda enumera en lugar de justificar.** Las otras doce filas dan una razón (DA-01: *"Protege la
   ruta crítica…"*; DA-05: *"Permite comparar modelos sin rediseñar…"*). DA-03 responde "¿con qué?", no
   "¿por qué?". El porqué existe y está escrito: es §17.3.5 (*"Se adopta HTTP porque… Se adopta ZeroMQ
   porque… msgpack reduce…"*). La tabla se quedó con el "qué" y la prosa con el "porqué", invertido.
3. **Congela como invariante lo que el propio informe declara sustituible.** La tabla se presenta como
   *"reglas estructurales que deberán preservarse"*; §17.3.9.1 dice la doctrina correcta: *"conserva el
   transporte como mecanismo sustituible, pero fija para el prototipo una publicación ZeroMQ…"*. Si el bus
   fuera otro, DA-03 quedaría "incumplida" aunque la regla de diseño se preserve intacta.

Además es la única de trece filas con anglicismo crudo ("HTTP config-driven", "PUB/SUB") cuando el cuerpo
ya normalizó a *"interfaces HTTP gobernadas por configuración"* y *"publicador-suscriptor"*, y duplica casi
textualmente la Tabla 65 de §17.4 (que E4-20 elimina).

**Acción — reescribir sólo la celda de Justificación.** La Decisión no cambia.

> **DA-03 · Decisión:** Separar gobierno de corrida, transporte de datos en ejecución y repositorio
> persistente de hechos.
> **Justificación:** Cada preocupación tiene un régimen propio: el gobierno es puntual y de
> solicitud–respuesta, el transporte es continuo y no debe bloquear la ruta crítica, y la persistencia debe
> sobrevivir a la corrida para habilitar su relectura. Mantenerlas separadas permite sustituir el mecanismo
> de transporte sin alterar el gobierno ni la evidencia, y reevaluar cualquier corrida sin depender de la
> mensajería.

**Verificado:** DA-03 no está referenciada en ningún punto de §17.4 (la única fila del pase citada allí es
DA-13, en §17.4.6), así que el cambio no deja referencias colgadas. Las tecnologías siguen nombradas —con
su fundamento— en §17.3.5 y §17.3.9.1, que es donde D2 las admite.

---

### E3-20 · §17.3.6.6 "Validaciones previas al inicio de la corrida" — eliminar la subsección y reubicar

**Problema.** La subsección promete un mecanismo (un control de admisión) y entrega una lista de buenas
intenciones: ocho "debe/debería" en tres párrafos y sólo uno con consecuente. Nunca dice **quién** valida,
**en qué momento** ni **qué pasa cuando falla**. Párrafo por párrafo:

- **¶1** — el inventario *"fuente visual, modelo OVD, vocabulario activo, umbrales, política de registro"*
  ya está dos veces: es la **Tabla 44** completa y es §17.3.6.1 (*"**Antes de iniciar la ejecución**,
  define qué se evaluará, con qué fuente, con qué modelo, con qué vocabulario activo…"*). La segunda
  oración (*"tampoco debería evaluarse una alerta si no existe al menos un patrón activo"*) es
  tautológica. **Salvable:** la idea de compuerta.
- **¶2** — es un eco débil y anticipado de **§17.3.13.3**, que lo dice con precisión (los cuatro estados
  `computed / applicable_not_computed / not_applicable / not_interpretable`, cada uno con causa, más los
  ejemplos). Además está mal ubicado: declarar aplicabilidad no es una validación previa al inicio, es una
  propiedad del reporte. **Se elimina sin reemplazo.**
- **¶3** — solapa DA-11, §17.3.7.5 y §17.3.12.3. **Lo propio** es el consecuente: que un módulo implícito
  corrompe la interpretación de latencia, cobertura, privacidad y aplicabilidad.

**Acción.**
1. **Eliminar §17.3.6.6 completa.** §17.3.6.7 pasa a ser §17.3.6.6.
2. **Rescate 1 — al final del párrafo del punto de gobierno de §17.3.6.1:**
   > *"Esa función de gobierno sólo se sostiene si la configuración se resuelve y se valida antes de
   > iniciar la ejecución: una corrida cuya declaración esté incompleta debe fallar al crearse y no
   > producir artefactos que luego resulten inatribuibles."*
3. **Rescate 2 — como cierre de §17.3.6.5 (reglas de comparabilidad):**
   > *"Por la misma razón, ningún módulo opcional —evidencia visual, identidad temporal, zonas,
   > preselección en el rol de captura o distribución externa— puede operar como comportamiento implícito:
   > su habilitación se declara en la configuración de la corrida, porque una activación silenciosa
   > alteraría la interpretación de latencia, cobertura temporal, privacidad y aplicabilidad de métricas,
   > es decir, la base misma de la comparación."*

**Verificado:** ninguna prosa de §17.3 ni de §17.4 referencia §17.3.6.6. El hecho no se pierde del informe:
la Tabla 67 de §17.4 ya acredita que *"los endpoints… operan sobre configuraciones validadas"*.
**Saldo:** −1 subsección, ~180 palabras, cero compromisos de diseño perdidos.

---

### E3-21 · §17.3.3.1 y §17.3.3.2, Tablas 40 y 41 — fusionar en una sola tabla

**Problema — es la duplicación más cara del capítulo.** Dos tablas en subsecciones contiguas, con la misma
forma de columnas (`capacidad | tratamiento | justificación`), que asignan valores de **la misma taxonomía
de cinco términos**, con ~8 filas repetidas entre 12 y 16 (DBE, EBE, prompts, Nivel 1, evidencia visual,
inspección, identidad/MOT, adaptación al dominio). La prueba está en las Notas, que son la misma frase
dos veces con distinta redacción:

> **T40:** *"…'complementario previsto' agrupa capacidades útiles pero no obligatorias; 'extensión
> condicionada' identifica capacidades previstas sujetas a disponibilidad de datos y módulos; y 'rama
> comparativa condicionada'…"*
> **T41:** *"…'complementario previsto' agrupa capacidades útiles para validación…; 'extensión
> condicionada' identifica capacidades previstas pero no obligatorias; y 'rama comparativa
> condicionada'…"*

El lector no puede distinguir "alcance" de "capacidades requeridas" porque, operativamente, son lo mismo.

**Acción.**
1. **Una sola tabla**, ubicada en §17.3.3.2, titulada **"Capacidades arquitectónicas y su tratamiento en el
   diseño"**, con las columnas de la Tabla 41 (`Capacidad requerida | Compromiso | Lectura de diseño`).
2. **Base:** las 16 filas de la Tabla 41, que son las más granulares y mejor ordenadas.
3. **Absorber de la Tabla 40** las dos filas que sólo ella tiene, con su texto actual:
   - **Video crudo continuo** — *Fuera del comportamiento ordinario* — *"La trazabilidad principal se apoya
     en eventos, metadatos, métricas y referencias controladas."* (es una declaración de frontera, no puede
     perderse)
   - **Condiciones de riesgo de Nivel 2 y Nivel 3** — *Extensión condicionada* — se mantiene como fila
     propia, separada de "Capacidades contextuales y relacionales": una es el catálogo de condiciones, la
     otra los mecanismos que las habilitarían.
4. **Conservar la redacción de la Tabla 40** en dos celdas donde es más precisa que la de la 41:
   - identidad temporal / métricas MOT: *"La arquitectura admite granularidad por sujeto mediante una
     identidad temporal válida. Las métricas MOT no condicionan la evaluación del núcleo ni deben
     confundirse con la capacidad de mantener identidad."*
   - adaptación al dominio: *"Sólo corresponde bajo una línea base preentrenada congelada, datos
     suficientes, partición disjunta y criterios de escalamiento definidos con anterioridad a los
     resultados."*
5. **Una sola Nota**, con la glosa de los cinco tratamientos (la de la Tabla 41, que es la más completa).
6. **§17.3.3.1 conserva su prosa** —define el alcance del núcleo y las extensiones— y pierde su tabla; la
   frase que la introduce (*"La Tabla 40 detalla…"*) pasa a remitir a la tabla única de §17.3.3.2.

**Resultado:** ~18 filas, una taxonomía, una glosa. **−1 tabla, −10 filas, −1 nota duplicada.**

---

### E3-22 · §17.3.2, Tabla 39 — pasar a viñetas

**Problema.** 6 filas × 3 columnas con celdas de 125 caracteres de mediana (máximo 299): es prosa
maquetada en grilla (D-P2-1.4). Y su columna del medio —"Criterio ya definido"— es un **resumen de §17.1**:
repetición de un capítulo anterior dentro de una tabla. Lo valioso es el vínculo insumo → decisión, que son
seis oraciones. Quitar sólo la columna del medio la dejaría en dos columnas, o sea en una lista (D-P2-1.1);
conviene hacer el paso completo.

**Acción — reemplazar la tabla y su Nota por el siguiente cierre de §17.3.2** (el párrafo que hoy la
introduce se conserva y encadena con esto):

> *"Cada decisión de diseño se vincula con un insumo metodológico ya consolidado:*
> - *del **marco teórico** de detección de vocabulario abierto, seguimiento y procesamiento de video se
>   deriva una arquitectura modular, con separación de planos, ruta crítica medible y modelos sustituibles
>   mediante adaptadores;*
> - *de las **condiciones de riesgo seleccionadas**, priorizar el flujo completo de equipo de protección
>   mediante la estrategia indirecta (E-IND) y mantener zonas, relaciones complejas y métricas de
>   seguimiento como capacidades no bloqueantes;*
> - *de los **escenarios de evaluación**, abstraer las fuentes visuales para que ambos ingresen al pipeline
>   mediante contratos comunes, distinguiendo reproducibilidad, frescura, omisión, descarte y trazabilidad
>   temporal según la naturaleza de la fuente;*
> - *de los **roles funcionales**, definirlos como roles de referencia que organizan el diseño y delimitan
>   responsabilidades sin fijar una distribución obligatoria en hardware, procesos o contenedores;*
> - *del **marco de métricas**, instrumentar marcas temporales, configuración de corrida, métricas por
>   tramo y eventos reconstruibles desde el inicio del diseño;*
> - *de los **lineamientos ético-legales**, priorizar eventos, metadatos y referencias controladas y
>   conservar evidencia visual sólo cuando esté justificada por validación, auditoría o comunicación
>   académica."*

Eliminar también la referencia en prosa *"La Tabla 39 sintetiza esta relación…"*.

---

### E3-23 · §17.3.11.2, Tabla 49 — subsumida por la Tabla 50

**Problema.** Su columna "Contrato principal" **es la columna 1 de la Tabla 50**, una página después; y
"Información que cruza" es la "Información mínima" de la Tabla 50 en grano grueso. Ejemplo textual:

> **T49:** *Salida del plano de medios | Detecciones normalizadas, modelo, prompts, coordenadas, puntajes y
> tiempos | media.detection.v1*
> **T50:** *PerceptionEvent | Publica evidencia perceptiva normalizada | media.detection.v1, run, unidad,
> fuente, modelo, prompts, detecciones y timing*

Lo único que la Tabla 49 aporta y la 50 no es la columna **"Decisión protegida"**, que es justamente lo
valioso: dice *por qué* existe cada frontera.

**Acción.**
1. **Eliminar la Tabla 49** y su Nota. La Tabla 50 queda como la única tabla de contratos del capítulo.
2. **Conservar las siete decisiones protegidas como prosa** en §17.3.11.2, encadenadas al párrafo que hoy
   introduce la tabla. **Texto guía:**
   > *"Cada frontera existe para proteger una decisión. La del gobierno del experimento evita una
   > configuración monolítica y vincula ciclos de vida independientes. La de entrada visual unifica los dos
   > escenarios sin ocultar su temporalidad. La de salida del plano de medios encapsula la heterogeneidad
   > del detector. La de entrada del plano de control obliga a evaluar reglas sobre eventos y no sobre
   > frames crudos. La de salida del plano de control diferencia detección, patrón y alerta. La de
   > distribución mantiene la comunicación y la idempotencia aguas abajo de la alerta interna. Y la de
   > referencia y soporte sostiene la medición y la reconstrucción con estados de aplicabilidad. Las
   > fronteras son lógicas: no prescriben que cada responsabilidad se despliegue en una máquina, proceso o
   > contenedor independiente."*
3. Eliminar la referencia *"La Tabla 49 resume las fronteras que el diseño protege…"*, cuyo contenido pasa
   al texto anterior.

---

### E3-24 · §17.3.11.4, Tabla 51 — pasar a párrafo

**Problema.** Tres de sus cinco filas dicen textualmente *"Extensión prevista; …"* en la columna "Estado de
diseño": densidad informativa nula (D-P2-1.3). Y el contenido es un roadmap de campos opcionales, no una
decisión de diseño. La única fila con carga real —identidad temporal— ya está en DA-06 y se desarrolla en
§17.4.11.

**Acción — reemplazar la tabla por un párrafo** en §17.3.11.4, antes de la Nota (que se conserva porque
enuncia la regla de versionado):

> *"La superficie de crecimiento del evento de percepción se mantiene acotada y separada de las reglas de
> riesgo. La identidad temporal de sujeto es un campo opcional y la única identidad válida entre frames: el
> contrato la admite y el plano de control puede materializarla por configuración, sin que el plano de
> medios necesite emitirla y sin mezclar esa capacidad con las métricas de seguimiento. Velocidad,
> dirección, puntos clave de pose y máscaras de segmentación quedan previstos como campos opcionales que no
> modifican la semántica mínima del evento ni desplazan al bounding box. Las relaciones entre sujeto,
> evidencia de soporte y clase ausente, en cambio, pertenecen al plano de control: el plano de medios
> publica detecciones individuales."*

Eliminar la referencia *"La Tabla 51 explicita la superficie de crecimiento…"*.

---

### E3-25 · §17.3.17, Tabla 61 — eliminar

**Problema.** Tres razones convergentes:
1. Es de dos columnas (D-P2-1.1).
2. Duplica las filas de tratamiento "complementario previsto" y "extensión condicionada" de las Tablas 40 y
   41 (que E3-21 fusiona), y la Tabla 69 de §17.4 la reemplaza con ventaja: agrega el costo técnico y está
   respaldada por implementación.
3. **El párrafo que le sigue ya la sustituye en prosa:** *"La frontera de extensibilidad distingue tres
   clases de cambio. Una condición nueva del tipo «sujeto sin EPP» requiere una definición declarativa de
   patrón y vocabulario… Una familia relacional, zonal o de trayectoria requiere un evaluador nuevo… Un
   modelo, una fuente o un canal nuevos requieren sus respectivos adaptadores…"*.

**Acción.** Eliminar la Tabla 61 y su encabezado. El párrafo siguiente queda solo y basta.

---

### E3-26 · §17.3.18, Tabla 62 — eliminar

**Problema.** Es una **tabla-resumen dentro de una sección-resumen**: sus diez filas recapitulan decisiones
ya tomadas y desarrolladas —"Responsabilidades separadas" = DA-01; "Persistencia y transporte diferenciados"
= DA-03; "Alerta interna protegida" = DA-13; "Trazabilidad y minimización" = DA-08/DA-09; "Plan de
materialización" = Tabla 60—. No agrega un solo compromiso nuevo, y además es de dos columnas.

**Acción.** Eliminar la tabla y su Nota. §17.3.18 conserva su prosa de cierre, que ya declara el paso a la
implementación sin anticipar resultados. Si se quiere conservar la función de checklist, alcanza con una
oración al cierre:

> *"El diseño se considera completo cuando cada una de estas decisiones —separación de responsabilidades,
> estrategia perceptiva, configuración reproducible, contratos versionados, persistencia y transporte
> diferenciados, temporalidad declarada, alerta interna protegida y extensibilidad delimitada— posee un
> criterio verificable en la implementación."*

---

### E3-27 · §17.3.8.3.1, Tabla 46 — podar la tercera columna

**Problema.** Después de E3-09 (pase 1), que le quitó los valores numéricos, la columna **"Función en el
motor" quedó circular** en cuatro de diez filas: *"Identificación del patrón → Identifica la regla y su
configuración"*; *"Severidad configurada → Asigna la prioridad conceptual de la condición"*; *"Evidencia
requerida → Define la evidencia utilizada"*; *"Región de evaluación → Delimita dónde se busca el EPP"*. La
columna repite el nombre de la fila con otras palabras.

**Acción.** Eliminar la columna "Función en el motor". La tabla queda como
`Componente | Contenido esperado` — que es una lista, así que la alternativa equivalente es pasarla a
viñetas con el componente en negrita. **Recomiendo las viñetas**, por coherencia con D-P2-1.1. La Nota se
conserva sin cambios (remite a §17.4.6 por los valores).

---

### E3-28 · Terminología `opt-in` / `fail-open` y el párrafo desubicado de §17.3.7.3

**Problema.** Ninguno de los dos términos viene de etapas anteriores: **cero apariciones** en el
frontmatter/objetivos/plan, en §17.1, en el estado del arte, en el marco teórico y en el cierre/anexos.
Ambos **nacen en §17.3**, y su primera aparición es **DA-11, dentro de una celda de la Tabla 43**, crudos y
sin glosa. Después:

- `fail-open` **se glosa dos veces**, ninguna en su primer uso, y con las mismas palabras:
  > §17.3.7.3: *"…con comportamiento fail-open: ante incertidumbre o falla, la unidad se conserva para el
  > flujo principal."*
  > §17.3.14.5: *"…es opcional, deshabilitada por defecto y fail-open: una falla o incertidumbre del
  > preselector no debe eliminar la unidad del flujo principal."*
- `opt-in` **no se define nunca**, y no hace falta: siempre viene pegado a *"deshabilitada por defecto"*,
  que es su definición. Peor: el propio informe usa "opcional" para lo mismo en §17.3.14.5 y en la Tabla 58,
  con lo cual alterna dos términos para un solo concepto sin criterio.
- El párrafo de §17.3.7.3 está **en la subsección equivocada**: los otros cuatro párrafos de "Control de
  ritmo según tipo de fuente" son todos ritmo (fuentes pulleables vs. vivas, atraso acumulado, descartes,
  FPS vs. cobertura); ése abre con *"Las capacidades opcionales del plano de medios…"*. §17.3.7.5 se titula
  literalmente **"Capacidades opcionales sin desplazar el núcleo validable"**.

**Acción — cinco ediciones puntuales.**

1. **Tabla 43, DA-11 — glosar acá (primer uso) y eliminar el anglicismo:**
   > **Decisión:** Permitir preselección liviana en el EN como variante **opcional**, conservadora y
   > deshabilitada por defecto, con comportamiento fail-open.
   > **Justificación:** El comportamiento fail-open conserva la unidad en el flujo principal ante falla o
   > incertidumbre del preselector, de modo que la variante puede reducir carga sin transformar el borde en
   > fuente de verdad ni ocultar descartes; el flujo base continúa disponible.

2. **§17.3.7.3 — eliminar el cuarto párrafo completo** (el que empieza *"Las capacidades opcionales del
   plano de medios se incorporan sin modificar su contrato de salida…"*). La subsección queda con cuatro
   párrafos, todos sobre ritmo, y cierra donde debe. De sus cuatro oraciones: la de preselección se va
   porque §17.3.14.5 la dice mejor; la de instrumentación también está allá; y la última (*"la identidad
   temporal, las asociaciones y el razonamiento contextual permanecen en el plano de control"*) ya está en
   §17.3.7.4 y en §17.3.7.5.

3. **§17.3.7.5 — rescatar la única oración que no está en otro lado.** Al final del primer párrafo:
   > *"Estas capacidades pueden incorporarse como variantes del flujo, pero no deben convertirse en
   > requisitos para demostrar el procesamiento básico de CR-01 y CR-02, **y su incorporación no modifica el
   > contrato de salida del plano de medios**."*

4. **§17.3.14.5 — quitar la glosa, que ahora es la segunda.** La subsección conserva el párrafo (ahí el rol
   EN *es* el tema: la preselección sólo existe en EBE), pero la segunda oración pasa a
   *"…una falla o incertidumbre del preselector no elimina la unidad del flujo principal"*, sin volver a
   definir el término.

5. **Las dos celdas que quedan con `opt-in`:**
   - Tabla 57, fila *Preselección en el borde*: *"Estado opt-in, criterio, fail-open y ledger de
     decisiones"* → **"Estado de habilitación, criterio, comportamiento fail-open y ledger de decisiones"**.
   - Tabla 59, fila *Preselección en borde descarta evidencia*: *"…como variante opt-in y fail-open, con
     ledger…"* → **"…como variante opcional y fail-open, con ledger…"**.

**Resultado:** `opt-in` desaparece del informe (4 de 4) y `fail-open` queda glosado una sola vez, en su
primera aparición. Ver **E4-22**, que cierra el otro extremo del mismo problema.

---

#### ✎ ENMIENDA 2026-08-22 — rigen las acciones 1, 3 y 4 de este bloque, no las de arriba

**Por qué se enmienda.** Un lector del capítulo llegó a §17.3.14.5, leyó *"…es opcional, deshabilitada por
defecto y fail-open: una falla o incertidumbre del preselector no debe eliminar la unidad del flujo
principal"* y reportó **no poder rastrear de dónde salía el concepto**. Esa es la falla real, y el
diagnóstico de E3-28 la explica: la primera aparición del término está **cruda, dentro de una celda de la
Tabla 43**, y la subsección que sí es dueña del concepto —§17.3.7.5, "Capacidades opcionales sin desplazar
el núcleo validable"— **nunca lo nombra**. El lector recibe una definición pero no encuentra la decisión.

La acción 4 original **agravaba ese recorrido**: quitaba la glosa precisamente en §17.3.14.5, dejando como
única definición del término una celda de tabla. Además contradice D-P2-1: una tabla se consulta, no se lee,
y no es lugar para la única definición de un concepto que reaparece seis veces.

**Criterio de la enmienda:** el término se nombra y se define **en prosa**, en la subsección que ya es dueña
del concepto; las tablas quedan libres de jerga; y el punto de reuso lleva un ancla breve en lugar de una
redefinición o de nada.

**Acciones 2 y 5: sin cambios** (eliminar el párrafo desubicado de §17.3.7.3; erradicar `opt-in` de las dos
celdas restantes).

**Acción 1 enmendada — Tabla 43, DA-11: enunciar la decisión sin el anglicismo.**

> **Decisión:** Permitir preselección liviana en el rol de captura como variante opcional, conservadora y
> deshabilitada por defecto, que conserva la unidad en el flujo principal ante falla o incertidumbre del
> preselector.
> **Justificación:** La variante puede reducir carga sin transformar el borde en fuente de verdad ni ocultar
> descartes, porque el flujo base continúa disponible y comparable.

**Acción 3 enmendada — §17.3.7.5, primer párrafo: acá nace el término.** Absorbe la oración que la acción 3
original rescataba, y agrega la definición:

> El núcleo validable del plano de medios debe poder operar sin exigir seguimiento multiobjeto formal,
> preselección en borde ni adaptación de modelos al dominio. Estas capacidades pueden incorporarse como
> variantes del flujo, pero no deben convertirse en requisitos para demostrar el procesamiento básico de
> CR-01 y CR-02, y su incorporación no modifica el contrato de salida del plano de medios. La preselección
> en borde se adopta además bajo un criterio de degradación segura, denominado fail-open: ante una falla o
> una decisión incierta del preselector, la unidad visual se conserva para el flujo principal. De ese modo
> la variante puede descartar carga, pero nunca convertirse en causa de pérdida de evidencia.

**Acción 4 enmendada — §17.3.14.5: ancla breve, ni redefinición ni vacío.** La segunda oración pasa a:

> La variante de preselección liviana en el borde es opcional, está deshabilitada por defecto y opera con el
> criterio de degradación segura fijado para las capacidades opcionales del plano de medios: una falla o
> incertidumbre del preselector no elimina la unidad del flujo principal.

*(Ancla descriptiva y no numérica a propósito: una referencia "§17.3.7.5" quedaría expuesta a los
corrimientos de numeración de este pase. Si se prefiere la forma explícita, el precedente es E3-07.)*

**Recorrido resultante para el lector**, que es lo que la enmienda arregla:

| Orden | Sección | Qué encuentra |
| --- | --- | --- |
| 1 | §17.3.3.1 | "preselección liviana en borde" como extensión condicionada — sin jerga |
| 2 | §17.3.3.4, DA-11 | la **decisión**, enunciada en castellano — sin jerga |
| 3 | §17.3.7.5 | el **término nombrado y definido en prosa**, con su razón |
| 4 | §17.3.14.5 · Tablas 57, 58 y 59 | usos posteriores, ya anclados |

**Huella final de `fail-open`: cuatro apariciones** — la definitoria de §17.3.7.5 más tres celdas de tabla:
**Tabla 57** (condiciones para interpretar EBE), **Tabla 58** (roles funcionales, fila *EN — modo base de
captura*) y **Tabla 59** (riesgos). Contra las siete actuales: §17.3.7.3 se elimina por la acción 2, DA-11
suelta el término por la acción 1 enmendada, la Tabla 61 desaparece por E3-25 y **§17.3.14.5 también deja de
usar el término** —el texto de la acción 4 enmendada dice "criterio de degradación segura", no `fail-open`—.
`opt-in`: cero (4 de 4).

⚠ **La Tabla 58 no la toca ninguna acción de E3-28, y está bien así.** Su celda dice *"La preselección
liviana es opcional, fail-open y deshabilitada por defecto"*; se deja intacta a propósito, porque con la
enmienda el término ya viene definido en prosa mucho antes (§17.3.7.5 precede a las tres tablas y a
§17.3.14.5). Se deja constancia para que no se lea como omisión ni se "corrija" por las dudas.

**Propiedad verificada:** con el orden resultante —§17.3.7.5 (L387 del texto extraído) antes de §17.3.14.5
(L877) y de las Tablas 57, 58 y 59 (L881, L919, L936)— **ninguna aparición del término precede a su
definición en prosa.** Es exactamente la propiedad que hoy falta y que originó esta enmienda.

---

### E3-29 · §17.3.10.3 "Política, medición y límites de interpretación" — reescritura completa

**Origen:** dos objeciones de lectura sobre el primer párrafo — *"¿por qué nombrar una configuración que no
se utiliza?"* y *"parece que estamos prediciendo el futuro; el diseño va antes que la implementación"*. Al
verificar el párrafo contra el código aparecieron además **dos afirmaciones falsas** en los párrafos
siguientes, y **dos límites de interpretación ausentes** en una subsección que los promete en el título.

**No afecta la numeración de tablas** (no agrega ni elimina tablas): §E queda igual.

#### Verificación (2026-08-22) — qué es cierto y qué no

| Afirmación del texto vigente | Veredicto |
| --- | --- |
| El motor posee capacidad técnica de control de re-confirmación | **Cierto.** Existe control de re-alerta por patrón y sujeto, en ventana temporal o por cuadros. |
| El núcleo no la utiliza | **Cierto.** El conjunto de patrones adoptado lo declara en su propia descripción: el motor emite en cada confirmación. |
| La supresión pertenece a la política del módulo de distribución | **Cierto sólo para el cooldown**, que está implementado y activo por defecto (ventana de 30.000 ms, clave condición + fuente). |
| "…—cooldown, **agrupación o limitación de tasa**—" | **FALSO.** Sólo existe el cooldown. La configuración de política admite exactamente dos parámetros (ventana y clave) y **rechaza claves desconocidas**: los otros dos mecanismos no están apagados, no son expresables. |
| "clave idempotente por evento, canal **y política**" | **FALSO.** La clave es de **dos** componentes: notificación y canal. La política no forma parte de la clave. |
| "distinguir entregas exitosas, supresiones deliberadas, duplicados y fallas de canal" | **Incompleto.** Los resultados posibles son **cinco**, no cuatro. Falta el descarte definitivo por agotamiento de reintentos, que es distinto de la falla de un intento y se registra además en un artefacto aparte. |
| `t_alert-notification` "mide desde la disponibilidad … hasta la confirmación" | **Incompleto.** La métrica se registra en **dos modalidades** y el propio reporte agrega las latencias **separadas por modalidad**. El texto describe una sola y no advierte que no son comparables. |

**Además, ausente y verificable:** el registro de entregas es de **sólo agregado y acumulativo entre
corridas** —ninguna fila se elimina jamás, la generación anterior se archiva íntegra al reutilizar un
directorio, y la deduplicación considera todas las generaciones—. Es un compromiso de trazabilidad que
corresponde exactamente a una subsección titulada "Política, medición y límites de interpretación".

#### Respuesta a la objeción 1 (¿por qué nombrar lo que no se usa?)

Se conserva la mención, con la razón explicitada. La capacidad inactiva no es trivia: es lo que convierte
una limitación aparente en una decisión. El reclamo que depende de ella es el del párrafo siguiente —las
re-alertas no se computan como falsos positivos—. Un lector que observa más alertas que episodios sospecha
un defecto o precisión inflada; nombrar la capacidad que existe y se dejó apagada es lo que responde eso.
El defecto del texto vigente no es mencionarla, es **dar el hecho y dejar el motivo para el párrafo
siguiente**, de modo que en su lugar se lee como dato suelto.

#### Respuesta a la objeción 2 (¿predicción del futuro?)

Correcta, pero apunta media cláusula a la izquierda. Asignar una responsabilidad a un módulo **es** el acto
de diseño, no una predicción — y en este caso ya está realizado: el cooldown existe. Lo que sí predice el
futuro es la **enumeración de tres mecanismos** cuando sólo hay uno. El informe ya tiene un idiom honesto
para eso: la Tabla 48 declara los canales adicionales como *punto de extensión*, no como política vigente.
La reescritura usa el mismo idiom.

#### Qué NO se explica acá porque ya está en Etapa 2 (§17.1)

Se relevó §17.1 contra esta subsección. Resultado, y criterio de poda aplicado al texto guía:

| Material | Dónde está ya | Consecuencia en §17.3.10.3 |
| --- | --- | --- |
| Qué mide `t_alert-notification` y su alcance | §17.1: *"extiende la medición hacia la disponibilidad de la alerta en el canal definido, pero no forma parte del núcleo evaluativo mínimo"*, más las condiciones para reportarla | **No se redefine.** §17.3 sólo agrega lo que es nuevo: que el registro conserva la modalidad de medición. |
| No mezclar costo computacional, ventana funcional de evidencia y demora de interfaz o distribución | §17.1, delimitación G2A / Glass-to-Alert | **No se reargumenta.** Sólo se declara el corte nuevo: entre modalidades. |
| La unidad de conteo del falso positivo debe declararse previamente y mantenerse constante | §17.1: la regla es explícita | **No se justifica.** Sólo se **declara** la unidad del tramo: la notificación, no la fila. |
| Ventanas de persistencia y trade-off de falsos positivos por severidad | §17.1, Tabla 24 | No se toca. |

**Lo que sí nace en §17.3 y no se recorta:** §17.1 no menciona en ninguna parte la supresión de
re-notificación, el cooldown, las re-alertas, la idempotencia ni el ledger de entregas — cero apariciones
de esos términos en todo el capítulo de Etapa 2. Todo el compromiso de política y trazabilidad del tramo
de distribución se establece por primera vez acá, de modo que no hay repetición que quitar.

#### Texto guía

> El conjunto de patrones adoptado no suprime confirmaciones: cada alerta interna se registra para
> conservar la dinámica real del episodio. La decisión es deliberada —el motor dispone de control de
> re-confirmación por patrón y sujeto y el núcleo lo deja inactivo— porque un motor que suprimiera dejaría
> de reflejar la duración del episodio y no permitiría distinguir una condición que persiste de una que se
> resolvió.
>
> La supresión de re-notificación se reubica en la política del módulo de distribución, y al reubicarse
> cambia de granularidad: el motor la aplicaría por patrón y sujeto, mientras que la política de entrega
> aplica una ventana de silencio por condición y fuente, porque para una notificación asistiva lo relevante
> es que esa condición en esa cámara ya fue avisada. La agrupación de avisos y la limitación de tasa quedan
> como punto de extensión de la política. Una alerta suprimida para comunicación existió y continúa siendo
> medible: las re-alertas de un episodio activo se informan por separado y no se computan como falsos
> positivos, de modo que una decisión de comunicación no altera la precisión del motor.
>
> El ledger de entregas aplica una clave de idempotencia por notificación y canal, es de sólo agregado y
> acumula entre corridas: al reutilizar un directorio de salida la generación anterior se archiva íntegra y
> la deduplicación considera todas las generaciones, por lo que un reprocesamiento no vuelve a entregar lo
> ya entregado. Cada fila conserva número de intento, marca temporal, resultado, motivo de error y
> confirmación del canal, y distingue cinco resultados: entrega exitosa, supresión por política, descarte
> por duplicado, falla de un intento y descarte definitivo por agotamiento de reintentos. La unidad de
> conteo del tramo es la notificación y no la fila: una notificación no entregada deja una fila por cada
> intento más la del descarte definitivo.
>
> Cada fila registra además la modalidad en que se midió `t_alert-notification`, y la latencia del tramo se
> informa siempre separada por modalidad: en relectura DBE el intervalo incorpora el ritmo de reinyección de
> las alertas persistidas, que es propiedad del reprocesamiento y no del canal.

**Balance de extensión:** cuatro párrafos contra seis, y una vez descontada la definición de la métrica y
la justificación de la regla de conteo —ambas de Etapa 2— la subsección queda apenas por encima del texto
vigente, con las dos afirmaciones falsas corregidas y los dos límites presentes.

**Nota de consistencia tipográfica** (no es contenido): en §17.1 la métrica aparece como ecuación de Word y
en §17.3.10.3 como texto corrido. Conviene unificar la forma de escribirla al cerrar las dos secciones.

---

### E3-30 · §17.3.11.1 "Criterios de diseño de contratos" — eliminar la subsección y rescatar una cláusula

**Origen:** pregunta de lectura — *"¿esta sección realmente suma?"*. Se relevó cada afirmación de la
subsección contra el resto de §17.3 y contra §17.1.

**No es solapamiento con Etapa 2.** §17.1 no trata contratos: cero apariciones de "versionado",
"autodescriptivo" o "payload", y delega el asunto de forma explícita —*"la instancia de análisis y diseño
arquitectónico deberá traducir esta definición en componentes, contratos, eventos y configuraciones"*—. El
material pertenece a §17.3. El problema es **redundancia interna del propio capítulo**.

#### Relevamiento afirmación por afirmación

| Afirmación de §17.3.11.1 | Dónde ya está | Veredicto |
| --- | --- | --- |
| Contratos explícitos, autodescriptivos, versionados, estables | En el **párrafo introductorio de §17.3.11, inmediatamente arriba**: *"modelos de datos versionados, serializaciones explícitas e interfaces concretas"*, *"bajo qué versión"* | Reformulación del párrafo anterior como lista normativa. |
| "La versión viaja dentro del payload" | **§17.3.11.4**: *"La versión viaja en el payload persistido y publicado"* | **Duplicado casi literal**, dentro de la misma §17.3.11. |
| "el transporte no sustituye la identificación del esquema" | En ningún otro lugar del capítulo | **ÚNICO aporte real.** Se rescata. |
| Un mismo evento se persiste como JSONL y se transporta en el envoltorio del bus sin volverse dos contratos | Dicho **tres veces antes**: §17.3.5 (*"la persistencia JSONL … no constituye un tercer patrón de acople"*), §17.3.8.4 (*"el payload publicado corresponde al mismo contenido lógico persistido"*), §17.3.10.2 (*"la modalidad de ejecución no modifica la semántica"*) | Cuarta enunciación, y la más débil: las tres anteriores están donde el lector las necesita. |
| Los identificadores delimitan niveles distintos y no son intercambiables | Ver defecto abajo | Defectuoso e innecesario. |

#### El defecto del párrafo de identificadores

Anuncia **cinco** identificadores y define **tres**.

- `run_id` **aparece una única vez en todo §17.3** —exactamente en esa oración— y nunca se define.
- `experiment_id` ya está definido, mejor y mucho antes, en **§17.3.6.2**: *"esta unidad se identifica
  mediante un `experiment_id`, mientras que cada componente conserva su propio identificador de corrida"*.
- `unit_id` y `source_id` se usan ya definidos en §17.3.11.3, §17.3.12.2 y §17.3.13.
- **Falta `detection_id`**, que es el identificador cuya confusión sí importa: §17.3.11.3 aclara que *"sólo
  identifica una detección dentro de la unidad visual; no constituye identidad entre frames"*, §17.3.8.3.2
  lo repite, y **§17.3.16 lo lista como riesgo arquitectónico** (*"identidad de detección interpretada como
  identidad temporal"*). El párrafo que promete decir cuáles identificadores no son intercambiables omite
  el único caso que el capítulo trata como trampa.

#### Corrección: eliminar la subsección, reforzar el párrafo introductorio de §17.3.11

**Texto guía** (reemplaza el párrafo introductorio de §17.3.11 y absorbe lo rescatable de §17.3.11.1):

> Los contratos estabilizan la semántica de intercambio entre componentes: definen qué información cruza
> cada frontera y bajo qué versión. En la arquitectura consolidada del núcleo se expresan como modelos de
> datos versionados, con serializaciones explícitas e interfaces concretas, y cada uno queda asociado a una
> corrida para que productores y consumidores puedan evolucionar de forma independiente. La versión viaja
> dentro del payload y no en el envoltorio de transporte: el canal puede cambiar sin que el hecho
> persistido pierda la identificación de su esquema. Las capacidades futuras deben evolucionar de forma
> aditiva sin romper la lectura de corridas históricas.

**Lo que se elimina y no se pierde:** la tesis de un contrato con dos transportes queda en sus tres
enunciaciones existentes; los niveles de identidad quedan definidos en los lugares donde cada identificador
se usa. Nada de esto es un compromiso de diseño que desaparezca (D-P2-2).

**Variante si se quiere conservar los niveles de identidad reunidos:** agregar una oración al final de
§17.3.11.3 —que ya trata `detection_id`— en lugar de una subsección propia, y ahí sí nombrar los cinco
identificadores **más** `detection_id`, definiendo los seis. No se recomienda: duplicaría definiciones que
ya funcionan en su lugar de uso.

#### ⚠ Consecuencia de numeración — afecta a E3-23 y E3-24

Eliminar el encabezado §17.3.11.1 corre las tres subsecciones siguientes:

| Hoy | Después de E3-30 |
| --- | --- |
| 17.3.11.1 Criterios de diseño de contratos | *(eliminada; absorbida en el intro de §17.3.11)* |
| 17.3.11.2 Fronteras informacionales de intercambio | **17.3.11.1** |
| 17.3.11.3 Contratos mínimos e interfaces | **17.3.11.2** |
| 17.3.11.4 Criterios de evolución durante la implementación experimental | **17.3.11.3** |

**E3-23** está redactada contra "§17.3.11.2, Tabla 49" y **E3-24** contra "§17.3.11.4, Tabla 51". Si se
aplica E3-30, esas dos unidades pasan a apuntar a **§17.3.11.1** y **§17.3.11.3** respectivamente. Aplicar
E3-30 **primero** y leer E3-23/E3-24 con el mapa nuevo, o aplicarlas antes y renumerar una sola vez al
final. No afecta la numeración de **tablas**: §E queda igual.

---

### E3-31 · Identificadores versionados en §17.3 — migran TODOS a §17.4 (aplica D-P2-5) ✎ REVISADA 2026-08-22

**Origen:** pregunta de lectura — *"§17.3 nombra versiones de contratos (`media.detection.v1`) porque ya
tenemos la plataforma implementada; ¿no debería eso ir a Etapa 4?"*.

> ⚠ **Esta unidad reemplaza a su primera versión (mismo día).** La primera versión proponía un criterio
> estrecho —"`.v1` se queda porque es declarable ex-ante; sólo `.v2` delata historia"— y desestimaba la
> variante estricta. La verificación contra el `.docx` de §17.4 v1.2 la refutó. Rige la versión estricta,
> formalizada como **D-P2-5**.

#### Los tres hechos que refutan el criterio estrecho (verificados 2026-08-22)

1. **§17.4 ya está escrito bajo el criterio estricto, y el par se contradice.** §17.4.2 abre con *"los
   contratos preliminares definidos durante el diseño se materializaron como…"* y su **Tabla 63** titula la
   primera columna **"Contrato del diseño"** con las denominaciones conceptuales (PerceptionEvent,
   AlertEvent, Referencia temporal…) y la segunda **"Materialización efectiva"** con los identificadores
   versionados. Bajo la lógica del propio informe, `media.detection.v1` **es** materialización. Si §17.3
   dice nueve veces `media.detection.v1`, la fila *PerceptionEvent → media.detection.v1* de la Tabla 63
   queda tautológica y la narrativa diseño→implementación se contradice a sí misma.

2. **El pase 1 ya venía moviéndose en esta dirección.** El texto guía de E3-04 (aplicado en la v1.1
   vigente) reescribió el párrafo de acople de §17.3.5 nombrando ZeroMQ, msgpack y JSONL **sin ningún
   identificador versionado**. La tecnología con su justificación es diseño (D2); el nombre de cable no lo
   acompañó.

3. **La asimetría existente prueba que el corte `.v1`/`.v2` era casualidad, no principio.** §17.3 nunca
   nombra `media.metric.v2` ni `control.metric.v1` — dice "contratos de métricas", genérico — y §17.4 los
   declara en la Tabla 63. Las métricas ya siguen el patrón correcto. Y los dos únicos `.v2` del par
   (`clip_gt.v2`, `media.metric.v2`) son exactamente los contratos que **iteraron durante la
   construcción**: el corte "los `.v1` pueden quedarse" sobrevivía sólo porque los demás contratos no
   alcanzaron a romperse. Si el evento de percepción hubiera iterado, §17.3 filtraría `media.detection.v2`
   con el mismo mecanismo.

**Qué conserva §17.3 (esto no cambia):** las decisiones de versionado como propiedades de diseño —"la
versión viaja dentro del payload", la regla de evolución aditiva de §17.3.11.4— enunciadas **en
abstracto**; las tecnologías con su justificación (D2/E3-04); las denominaciones conceptuales de la Tabla
50; y los nombres de estados `inactive`…`resolved` de §17.3.8.2 (vocabulario de la máquina de estados, que
es diseño por la excepción de D2 — se deja constancia para que no parezca omisión).

#### Inventario de aplicación — §17.3 queda con CERO identificadores `.vN`

Recuento sobre la v1.1 vigente: **42 menciones de 9 identificadores**. **11 mueren solas** con unidades ya
firmadas — 8 en la Tabla 49 (E3-23; son 7 filas pero 8 menciones), 2 en la Tabla 61 (E3-25) y 1 en
§17.3.11.1 (E3-30). Quedan **31 menciones en 19 puntos de edición**, todos mecánicos: el reemplazo usa
denominaciones que §17.3 ya definió. Números de tabla según la numeración **vigente** en el `.docx` v1.1
(el mapa post-pase está en §E).

| # | Ubicación | Vigente | Reemplazo |
| --- | --- | --- | --- |
| 1 | §17.3.8.1, párrafo del bus | "…serialización msgpack y envoltorio `bus.envelope.v1`" | "…serialización msgpack y un envoltorio versionado" |
| 2 | §17.3.8.1, párrafo siguiente | "Cuando un patrón alcanza el estado confirmado se registra `control.alert.v1`. La alerta interna es el hecho principal…" | "Cuando un patrón alcanza el estado confirmado se registra la alerta interna: es el hecho principal del sistema y precede a cualquier notificación." |
| 3–4 | §17.3.8.3.3, **Tabla 47**, filas PR-01 y PR-02, columna de insumos | "Eventos `media.detection.v1`, coordenadas…" (×2) | "Eventos de percepción, coordenadas…" (×2) |
| 5 | §17.3.8.4, camino EBE | "un seq monótono dentro de `bus.envelope.v1`" | "un número de secuencia monótono dentro del envoltorio versionado del bus" |
| 6 | §17.3.8.4, cierre | "El cierre se propaga mediante `run.lifecycle.v1`. El evento `run_finished` delimita el final lógico…" | "El cierre de la corrida se propaga mediante un evento de ciclo de vida cuyo hito de finalización delimita el final lógico…" (los DOS literales migran; quedan declarados en la fila *Cierre de corrida* que **E4-24** agrega a la Tabla 63) |
| 7 | §17.3.10.2, prosa | "Ambos caminos utilizan `control.alert.v1`, `control.notification.v1` y `control.delivery.v1`, por lo que…" | "Ambos caminos utilizan los mismos contratos de alerta interna, sobre de notificación y registro de entrega, por lo que…" |
| 8 | §17.3.10.2, **Tabla 48**, fila MQTT QoS 1 | "Publicar `control.notification.v1` y esperar…" · "…queda registrado en `control.delivery.v1`" | "Publicar el sobre de notificación y esperar…" · "…queda asentado como registro de entrega" |
| 9 | §17.3.11.3, **Tabla 50**, columna "Información mínima" — 6 celdas: PerceptionEvent, PatternStateChanged, AlertEvent, Referencia temporal de evaluación, NotificationEnvelope y DeliveryRecord | cada celda abre con su identificador (`media.detection.v1, run, unidad…`) | **quitar el identificador inicial de las 6 celdas** y habilitarlo con una oración única antes de la tabla: **"Todo contrato declara su identidad de esquema y su versión como primer elemento del payload."** El resto de cada celda queda igual. |
| 10 | §17.3.11.3, prosa | "El evento central del sistema es `media.detection.v1`. Agrupa la identidad de esquema, la corrida…" | "El evento central del sistema es el evento de percepción. Agrupa la identidad de esquema versionada, la corrida…" |
| 11 | §17.3.11.3, prosa | "La referencia `clip_gt.v2` impone dos invariantes…" | "La referencia temporal de evaluación impone dos invariantes…" (las invariantes quedan íntegras: son diseño) |
| 12 | §17.3.11.4 | "Un cambio aditivo conserva `media.detection.v1` porque no invalida consumidores existentes." | "Un cambio aditivo conserva la versión vigente del contrato porque no invalida consumidores existentes." (el resto de la subsección no se toca: la regla es diseño) |
| 13 | §17.3.13.2, **Tabla 54** (diccionario de métricas), fila TTFD | "requiere `clip_gt.v2`" | "requiere referencia temporal anotada" |
| 14 | §17.3.13.3, **Tabla 55** (señales observables), primera fila | "Eventos `media.detection.v1`" | "Eventos de percepción" |
| 15 | §17.3.14.5, prosa | "el matching temporal contra `clip_gt.v2` se declara no interpretable" | "el matching temporal contra la referencia temporal se declara no interpretable" |
| 16 | §17.3.15, **prosa** (cierre del párrafo del módulo de distribución) | "Puede co-ubicarse con el CPN o separarse sin modificar `control.alert.v1`, `control.notification.v1` ni `control.delivery.v1`." | "…sin modificar los contratos de alerta interna, notificación y entrega." |
| 17 | §17.3.15, **Tabla 58** (roles funcionales), fila *Módulo de distribución* | "Consumo de `control.alert.v1` desde el bus de alertas, política de notificación, ledger de idempotencia, entrega MQTT y registro de `control.notification.v1` y `control.delivery.v1`." | "Consumo de la alerta interna desde el bus de alertas, política de notificación, ledger de idempotencia, entrega MQTT y registro del sobre de notificación y del resultado de entrega." |
| 18 | §17.3.16, **Tabla 59** (riesgos y mitigaciones), fila *Notificación externa altera la métrica* | "Registrar primero `control.alert.v1`; ubicar cooldown…" | "Registrar primero la alerta interna; ubicar cooldown…" |
| 19 | §17.3.17, **Tabla 60** (plan de materialización), fila *Adaptador OVD* | "El modelo puede sustituirse sin modificar el contrato `media.detection.v1`." | "El modelo puede sustituirse sin modificar el contrato del evento de percepción." |

**No inventar un `clip_gt.v1` en §17.3.** El diseño no fija números de versión de ningún contrato; la
historia real de la referencia temporal se declara en §17.4 (ver E4-23).

**Verificación al aplicar:** buscar "`.v1`", "`.v2`" y "`run_finished`" en §17.3 → **cero resultados**.
Aritmética de control: 42 = 11 que mueren con E3-23/E3-25/E3-30 + 31 en los 19 puntos de arriba.
Todos los identificadores quedan declarados en la **Tabla 63** de §17.4.2 —incluida la fila *Cierre de
corrida* que agrega **E4-24**— más la excepción glosada de §17.4.8 (E4-23). Verificado contra el `.docx`
v1.2: el traspaso no deja ningún identificador huérfano.

**Ojo con los puntos 16–19: son cuatro ubicaciones distintas, no una.** Están en cuatro subsecciones y tres
tablas diferentes; tratarlas como un solo reemplazo global deja menciones vivas. En particular el punto 19
está en la **Tabla 60, que SOBREVIVE** (E3-25 elimina la 61, no la 60): es el punto que más fácil se pasa
por alto y sin él la verificación de "cero identificadores" falla.

**Interacciones:** los textos guía de E3-29 y E3-30 ya cumplen D-P2-5 (no nombran identificadores). E3-23 y
E3-25/E3-26 eliminan tablas que contenían menciones — aplicarlas no genera conflicto en ningún orden. La
fila 9 convive con la renumeración de E3-30 (§17.3.11.3 pasa a ser §17.3.11.2). Si se aplican las
opcionales, C-01 pasa a viñetas las Tablas 59 y 60 (puntos 18 y 19): el texto del reemplazo es el mismo.

**Decisión aceptada 2026-08-22 — la Tabla 50 conserva el CamelCase, NO se castellaniza.** Tras aplicar esta
unidad, la primera columna de la Tabla 50 (PerceptionEvent, AlertEvent, …) queda como único "identificador"
visible en §17.3. Es deliberado: ese CamelCase es la denominación de diseño que fijó D1 y es la **clave de
join** con la columna "Contrato del diseño" de la Tabla 63 — el lector que quiere el id de cable recorre
Tabla 50 → Tabla 63 y lo encuentra declarado una sola vez. Castellanizar la Tabla 50 rompería ese join.
No "corregirla" al aplicar el pase.

---

## B. Correcciones a §17.4 — Implementación

### E4-20 · §17.4.5, Tabla 65 — eliminar

**Problema.** **Dos filas.** Es el caso más claro del informe (D-P2-1.2): su propia Nota las resume
completas en una oración —*"HTTP gobierna configuración y ciclo de vida de los tres servicios; el bus
transporta los hechos de ejecución"*— y el párrafo que la introduce ya anuncia los dos patrones. Es, además,
la tercera formulación del mismo contenido: DA-03 (§17.3.3.4), el párrafo de materialización (§17.3.5) y
esta tabla.

**Acción.** Eliminar la tabla y su encabezado. El texto de la Nota se integra como cierre del párrafo que
hoy la introduce; **los puertos y los participantes ya están en la Tabla 64** (interfaces), que es donde
corresponde por D2. Actualizar la referencia en prosa si la hubiera.

---

### E4-21 · §17.4.9, Tabla 67 — eliminar la columna "Estado"

**Problema.** Las **siete filas dicen "Verificada"**. Es exactamente el defecto que E3-02 del pase 1 ya
eliminó de la Tabla 43 (*"Todas las filas dicen 'Adoptada': la columna no discrimina nada"*), que quedó sin
aplicar en §17.4.

**Acción.**
1. Eliminar la columna "Estado". El párrafo que introduce la tabla ya declara que todo lo listado es
   evidencia de verificación, y la Nota lo reafirma.
2. Sin esa columna la tabla queda en dos columnas, o sea en una lista (D-P2-1.1): **pasarla a viñetas** con
   la propiedad verificada en negrita y su evidencia a continuación. Se conservan íntegras las siete
   evidencias, incluida la de pruebas automatizadas (2.203 aprobadas, sin fallos, en cinco suites, más la
   suite propia del módulo de distribución).
3. Conservar la Nota tal cual (acota que la tabla acredita funcionamiento técnico y no desempeño).

---

### E4-22 · §17.4.10, Tabla 68 — fila nueva: la preselección en el borde no se ejerció

**Problema — es el agujero de rendición de cuentas del capítulo.** La preselección liviana en el rol de
captura aparece **once veces en §17.3** (§17.3.3.1, DA-11, Tabla 44, §17.3.6.6, §17.3.7.3, §17.3.7.5,
§17.3.14.5 y las Tablas 57, 58, 59 y 61: cuatro tablas distintas le dedican una fila). En **§17.4 aparece
cero veces**. Y **no está declarada como exclusión**: la Tabla 68 —que es el lugar del informe donde se
rinden cuentas de capacidades ejercidas, exclusiones y brechas— tiene seis filas (identidad de sujeto,
estrategias E-DIR/E-IND/E-HYB, distribución de alertas, rama comparativa de ajuste fino, condiciones de
Nivel 2 y 3, paridad DBE/EBE) y ninguna es el rol de captura. Mientras tanto §17.4.5 dice que *"los
servicios se ejecutaron co-ubicados en un único host con GPU"*, que implícitamente significa que ese rol
nunca se desplegó.

Un lector que cuenta once menciones de una capacidad en el diseño y no la encuentra en el balance de
implementación se queda con una pregunta que el informe no contesta.

**Acción — agregar una fila a la Tabla 68**, después de *Condiciones de riesgo de nivel 2 y 3*:

> **Preselección liviana en el rol de captura** || *Especificada en el diseño como variante opcional y
> deshabilitada por defecto; no ejercida. Las corridas se ejecutaron con los servicios co-ubicados en un
> único host, sin desplegar el rol de captura como unidad separada.* || *La capacidad no integra los
> resultados: su efecto sobre carga, cobertura temporal y latencia queda fuera de lo medido y no puede
> reclamarse como propiedad verificada del prototipo.*

**Complemento recomendado (no obligatorio):** bajar la huella en §17.3. E3-25 ya elimina una de las cuatro
tablas con fila de preselección (la 61); las unidades opcionales C-01 y C-03 se ocupan de otras dos. Con
DA-11 más el párrafo de §17.3.14.5 alcanza y sobra para dejar la decisión declarada.

---

### E4-23 · §17.4 como único punto de declaración de identificadores versionados (contraparte de E3-31)

**Qué verifica y qué agrega.** Con E3-31 aplicada, §17.4 pasa a ser el primer lugar del informe donde el
lector ve un identificador `.vN`. Se verificó contra el `.docx` v1.2 que el traspaso está completo — **no
hay que agregar ninguna declaración**: la Tabla 63 ya declara `experiment.manifest.v1`,
`media.detection.v1`, `control.pattern_state.v1`, `control.alert.v1`, `media.metric.v2` /
`control.metric.v1`, `bus.envelope.v1`, `clip_gt.v2` y `control.notification.v1` / `control.delivery.v1`.
`run.lifecycle.v1` y el literal `run_finished` aparecen hoy en la prosa de §17.4.3 y §17.4.5; con **E4-24**
esa prosa pasa al castellano y ambos quedan declarados en la fila *Cierre de corrida* que E4-24 agrega a la
Tabla 63 — así el punto 6 de E3-31 los suelta sin dejarlos huérfanos. La Tabla 63 deja de ser parcialmente
tautológica y pasa a hacer el trabajo para el que existe.

**Única edición requerida — glosar por qué la referencia temporal es v2.** Tras E3-31, `clip_gt.v2` y
`media.metric.v2` quedan como los únicos sufijos "2" del informe, sin que ninguna v1 se mencione jamás. Para
la referencia temporal la pregunta es esperable (es el esquema del que dependen los resultados temporales de
§17.5) y la historia es real y honesta: la primera generación de la referencia registraba alertas esperadas
por sujeto, y fue reemplazada por episodios a nivel escena-condición con tiempos en milisegundos. En
§17.4.8, donde dice:

> *"…materializada mediante el esquema clip_gt.v2."*

pasa a:

> *"…materializada mediante el esquema clip_gt.v2, segunda versión de la referencia: la primera
> generación registraba alertas esperadas por sujeto y fue reemplazada por episodios a nivel de escena y
> condición con tiempos en milisegundos, junto con estados de aplicabilidad por clip."*

(Autocontenido: enuncia el hecho sin citar documentos del repositorio. Para `media.metric.v2` no se
propone glosa: es una fila de la Tabla 63 sin peso argumental en §17.5.)

**Qué NO hacer en §17.4:** no "corregir" la Tabla 63 reemplazando su columna "Contrato del diseño" por los
identificadores versionados — esa columna es el ancla hacia §17.3 y con D-P2-5 quedó exactamente bien como
está.

---

### E4-24 · §17.4 — sacar los identificadores literales de la prosa y sanear la Tabla 63 (aplica D-P2-6)

**Medición.** §17.4 tiene **22 menciones** de identificadores versionados: **14 en celdas de tabla** y
**8 en prosa**. Las 8 de prosa son el ruido; se reducen a **1**. Total resultante: **15**.

#### 1. §17.4.3 "Contratos de datos materializados" — el punto más denso (5 de las 8)

Hoy tres oraciones consecutivas usan un identificador como sujeto. **Texto guía** para los dos primeros
párrafos (el tercero, sobre evidencia auditable de la alerta, no se toca):

> Cinco contratos concentran los hechos principales de la ejecución; la Tabla 63 los identifica por su
> esquema y versión. El evento de percepción normaliza la salida del detector e incluye identificación de
> corrida y unidad visual, descripción de la fuente, perfil de modelo, conjunto de prompts, detecciones con
> coordenadas en píxeles y normalizadas, y tiempos por unidad. El envoltorio del bus encapsula el mismo
> payload para su transmisión e incorpora un número de secuencia monótono que vuelve detectable cualquier
> hueco.
>
> El contrato de ciclo de vida delimita la corrida y la cierra mediante un evento de finalización. El
> registro de transiciones del patrón recorre los estados inactive, candidate, confirmed, sustained y
> resolved (figura de la sección 17.3.8.2), junto con la evidencia y los hitos temporales que las motivaron.
> La alerta interna registra la confirmación de un episodio mediante un identificador determinista, de modo
> que reprocesar la misma corrida produce la misma identidad de alerta y permite deduplicar sin estado
> compartido.

Se conservan íntegros el contenido, los nombres de estados (D-P2-5) y la referencia a la figura.

#### 2. Las tres menciones de prosa restantes

| Ubicación | Vigente | Acción |
| --- | --- | --- |
| §17.4.5, camino EBE | "la evidencia se transmite por el bus ZeroMQ dentro de `bus.envelope.v1`; … el cierre se comunica mediante `run_finished`" | "…dentro del envoltorio versionado del bus; … el cierre se comunica mediante el evento de finalización de la corrida". **Ambos literales ya están declarados** (`bus.envelope.v1` en la Tabla 63; para el evento de finalización, agregar la fila de la regla 3 abajo). |
| §17.4.8, referencia temporal | "materializada mediante el esquema `clip_gt.v2`" | **SE CONSERVA**, con la glosa de E4-23: acá la versión *es* el argumento del párrafo (excepción de la regla 2). |
| §17.4.11, identidad de sujeto | mención en el párrafo de extensiones | Reemplazar por la denominación en castellano; el contrato ya está en la Tabla 63. |

#### 3. Tabla 63 — que cada columna haga un solo trabajo

Auditada fila por fila, la columna **"Versionado y trazabilidad"** mezcla **8 celdas que son un
identificador literal** con **8 que son una oración en prosa** ("Catálogo versionado; un archivo por
variante", "Contrato interno; viaja dentro del evento publicado", "Esquema por componente, registrado por
corrida"…). El lector no puede escanearla para saber si un contrato tiene esquema versionado propio o no.

**Acción mínima y suficiente — ampliar la Nota al pie**, sin tocar las 16 filas:

> **Nota.** La tabla documenta la correspondencia semántica entre el diseño y la implementación. Nueve
> contratos se materializan como **esquema versionado con identificador propio**, que es el que viaja en el
> payload y queda registrado en los artefactos de cada corrida; los restantes se versionan por **catálogo,
> configuración congelada o por el manifiesto de la ejecución experimental**, sin esquema propio. Esta tabla
> es el único punto del informe donde se declaran esos identificadores: el resto del capítulo se refiere a
> cada contrato por su denominación.

**Fila nueva** (para que el evento de finalización quede declarado al soltarlo §17.3 y §17.4.5):

> **Cierre de corrida** || *Evento de finalización publicado al cerrar la corrida* || `run.lifecycle.v1`
> (evento `run_finished`) || *Ambos planos*

*(Con esta fila la tabla pasa de 16 a 17 filas y de 9 a 10 contratos con esquema propio — ajustar el "nueve"
de la Nota a **diez** al aplicar.)*

**Lo que NO se hace:** reemplazar la columna 1 por identificadores. Es el ancla hacia §17.3 (D-P2-5) y su
mezcla de CamelCase y castellano es la que fijó D1 — se deja.

**Verificación al aplicar:** en §17.4, identificadores `.vN` fuera de la Tabla 63 → **una sola** ocurrencia,
la de §17.4.8 con su glosa. Y ningún identificador literal como sujeto gramatical en todo el capítulo.

### E4-25 · §17.4.4, Tabla 64 — el propósito de cada interfaz, cerrado y sin asimetrías falsas

**Origen:** directiva del usuario — *"el propósito de cada interfaz relevante que mostramos en el informe
tiene que estar súper claro y justificado, para no dejar dudas para el tribunal"*. Auditada la Tabla 64
contra las rutas reales de los tres servicios (2026-08-22), aparecen tres defectos y un remanente de E4-24.

#### Defectos verificados

1. **Asimetría de detención FALSA por omisión — el peor de los tres.** La tabla muestra `cancel` sólo en la
   distribución. Verificado contra el código: **el plano de medios SÍ expone detención**
   (`POST /api/runs/{id}/stop`, 202, cooperativa) y no figura; **el plano de control es el ÚNICO que no la
   expone**, y eso no se señala ni se justifica. Un tribunal que escanee la tabla concluye exactamente lo
   contrario de la realidad. La Nota agrava: *"las interfaces de administración y detención conservan…"*
   insinúa endpoints sin decir cuáles existen y cuáles no.
2. **Celdas que parafrasean el verbo HTTP** en lugar de decir para qué está la operación ("Consulta el
   estado de la corrida de entrega" no informa nada que el nombre del endpoint no diga).
3. **La garantía de suscripción está enunciada sólo para el control.** El párrafo final dice *"la respuesta
   afirmativa del plano de control implica que su consumidor ya está suscripto"* — pero la misma garantía
   del 201 de la distribución (bus de alertas) no está, y el **orden de disparo inverso al flujo de datos**
   (distribución → control → medios), que es la doctrina que justifica la existencia misma del
   `POST /api/runs` de la distribución, no se deriva en ninguna parte.
4. **Remanente de E4-24:** quedan 4 identificadores en celdas fuera de la Tabla 63 — 3 en la Tabla 64
   (fila `:5557` y fila `:5558`) y 1 en la Tabla 69.

**Hecho verificado que habilita la justificación:** los tres servicios implementan el mismo contrato de
gobierno — una corrida activa por vez, rechazo de solicitudes concurrentes señalando la corrida activa
(`RunBusyError` existe en los tres), configuración efectiva persistida por corrida.

#### Acciones

**A. Tabla 64 — filas.** Celdas cortas (D-P2-1); la justificación profunda va a la prosa de la acción C.

| Fila | Acción |
| --- | --- |
| Plano de medios — **fila nueva** tras `POST /api/runs` | `POST /api/runs/{id}/stop` → *"Detiene cooperativamente la corrida en curso; el cierre se propaga a los consumidores por el bus."* |
| Distribución `GET /api/runs/{id}` | → *"Consulta estado y conteos de entrega; determina cuándo consolidar artefactos."* |
| Distribución `POST /api/runs/{id}/cancel` | → *"Detiene cooperativamente una corrida de entrega en curso."* (mismo verbo que el stop de medios: es el mismo mecanismo) |
| Fila `Medios → control (:5557)` | → *"Transporta los eventos de percepción y el ciclo de vida de la corrida dentro del envoltorio versionado del bus."* |
| Fila `Control → distribución (:5558)` | → *"Transporta las alertas internas confirmadas hacia el módulo de distribución."* |
| Las demás filas | Sin cambios — `POST /api/runs` de los tres ya dice qué cruza; los `GET /api/config` y `GET /api/model` quedan, su propósito lo da la prosa. |

**B. Nota de la tabla — decir la verdad en vez de insinuarla:**

> **Nota.** La tabla resume las operaciones de gobierno principales; no es un inventario exhaustivo
> (listados, corrida actual, artefactos por corrida, comprobaciones de salud y limpieza del registro se
> omiten). La detención figura únicamente donde el servicio la expone: el plano de control no ofrece
> detención de una corrida en curso, y esa asimetría es deliberada (ver el texto).

**C. Prosa — reemplazar el párrafo final** (*"En una corrida live, la respuesta afirmativa del plano de
control implica que su consumidor ya está suscripto."*) por tres párrafos que justifican lo que la tabla
declara:

> Los tres servicios implementan el mismo contrato de gobierno: admiten una corrida activa por vez y
> rechazan solicitudes concurrentes señalando la corrida en curso; cada corrida declara su configuración al
> crearse y el servicio persiste la configuración efectiva utilizada. Las operaciones de consulta de
> configuración y de perfil de modelo permiten verificar, antes de disparar, que el servicio cargó lo que el
> experimento requiere: sin ellas, una discrepancia entre lo configurado y lo desplegado sólo se descubriría
> en los resultados.
>
> En una corrida en vivo, la respuesta afirmativa de cada consumidor del bus implica que su suscripción ya
> está establecida: la del plano de control sobre el canal de detecciones y la del módulo de distribución
> sobre el canal de alertas. De esa garantía se deriva el orden de disparo, inverso al flujo de datos:
> primero la distribución, después el control, por último el plano de medios. Un consumidor suscripto tarde
> perdería los eventos ya publicados sin ningún error observable; el orden de disparo excluye esa pérdida
> por construcción.
>
> La detención de corridas es cooperativa en los dos servicios que la exponen: la solicitud marca la corrida
> y el hilo de ejecución la observa entre unidades, sin cortes abruptos que dejarían artefactos a medio
> escribir. El plano de control no expone detención, y la asimetría es deliberada: su corrida en vivo se
> cierra con el evento de finalización que publica el plano de medios —la relación entre ambas corridas es
> uno a uno—, de modo que la intervención del operador se ejerce aguas arriba y el cierre llega por el mismo
> canal que los datos. El módulo de distribución, en cambio, requiere cancelación propia: una corrida de
> entrega puede permanecer a la espera de alertas y debe poder abortarse sin reiniciar el servicio.

**D. Tabla 69, fila "Dato adicional en la detección":** *"Evolución aditiva sin ruptura de
`media.detection.v1`"* → **"Evolución aditiva sin ruptura del contrato de percepción."**

**Corrección aritmética a E4-24:** su "Total resultante: 15" no contaba el identificador de su propia fila
nueva (*Cierre de corrida*); con ella son 16. Tras esta unidad quedan **12**: los 11 de la Tabla 63
(10 filas actuales + la nueva) y la glosa de §17.4.8 (E4-23). Con esto, la regla 2 de D-P2-6 pasa a
cumplirse literalmente: **ningún identificador vive fuera de la Tabla 63, salvo la excepción glosada.**

**Verificación al aplicar:** (a) en §17.4, ids `.vN` fuera de la Tabla 63 → sólo la glosa de §17.4.8;
(b) la Tabla 64 muestra detención en medios y distribución, y la Nota + prosa explican por qué el control
no; (c) el orden distribución → control → medios queda derivado en la prosa — es la misma advertencia de
cita que acompaña a la figura de arranque ("orden de arranque inverso al flujo de datos"), ahora con su
porqué en el cuerpo del informe.

### E4-26 · §17.4.6 — el núcleo no tiene UN modelo: tiene un catálogo que se ejerce entero

**Origen:** objeción del usuario sobre el tercer párrafo de §17.4.6 — *"no tenemos un solo modelo para el
núcleo; el perfil de modelo para el núcleo son todos los que probamos. Esto es experimental"*. La objeción
es doctrinaria y es correcta: la tesis no corona un modelo, muestra una plataforma que mide modelos de dos
familias bajo condiciones idénticas y da veredictos POR MODELO en §17.5. El texto vigente
—*"El perfil desplegado para el núcleo es grounding-dino/gdino-tiny-560, seleccionado en la comparación…"*—
promueve una decisión operativa de una corrida a identidad del sistema, que es exactamente el encuadre que
la defensa debe evitar (la plataforma es la tesis; el detector es la variable).

#### Hechos verificados (2026-08-22, contra el repositorio del plano de medios)

- **El catálogo vigente tiene NUEVE perfiles** más el mock: Grounding DINO tiny y base, cada uno en 800 y
  en 560 píxeles (4), y YOLOE en tamaños s/m/l/x (4). Cada perfil es un archivo del catálogo con su
  adaptador, umbrales y licencia.
- **MM-Grounding DINO NO está en el catálogo vigente**: sus tres perfiles están **archivados**
  (`configs/_archive/`, 2026-08-19), tras su descarte experimental. La frase del informe "incluye variantes
  … de MM-Grounding DINO" es **falsa en presente**; la familia se integró y se descartó — ese descarte es
  un RESULTADO que se informa en §17.5, no una fila del catálogo actual.
- **El despliegue integral materializa el catálogo entero como flota**: una instancia de servicio por
  perfil, orquestadas por la consola. "Comparar perfiles = disponer procesos con perfiles distintos"
  (§17.4.4) está implementado literalmente.
- Los valores citados del perfil `gdino-tiny-560` (umbral de caja 0,30, de texto 0,25, entrada 560) están
  confirmados contra su archivo de catálogo. No se cuestionan — se re-encuadran.
- Existen además dos perfiles de checkpoints de ajuste fino **no adoptados** (rama comparativa): no se
  enumeran en el catálogo del núcleo; su lugar es la fila de la Tabla 68 y §17.5.

#### Acciones

**A. Retitular §17.4.6:** "Configuración efectiva y modelo desplegado" → **"Configuración efectiva y
catálogo de modelos"**. El título vigente lleva el encuadre de modelo único. (Sin impacto: ninguna otra
sección referencia "17.4.6" por número.)

**B. Reemplazar el tercer párrafo** (los dos primeros —pattern set y estrategia perceptiva— no se tocan).
**Texto guía:**

> El catálogo de perfiles de modelo materializa la sustituibilidad prevista en el diseño: variantes de
> Grounding DINO —tiny y base, cada una con resolución de entrada de 800 y de 560 píxeles— y de YOLOE en
> cuatro tamaños, todas integradas mediante adaptadores sobre el mismo contrato de salida. Una tercera
> familia, MM-Grounding DINO, se integró por el mismo mecanismo y fue descartada durante la evaluación; su
> descarte se informa con los resultados y sus perfiles quedaron archivados fuera del catálogo activo.
>
> El núcleo no fija un modelo único. Cada instancia del servicio de medios carga un perfil al iniciarse, la
> comparación entre perfiles se materializa disponiendo instancias con perfiles distintos bajo la misma
> configuración de corrida, y el despliegue integral de la plataforma instancia un servicio por perfil del
> catálogo, orquestados desde la consola. Los perfiles vigentes se compararon sobre el banco de imágenes
> congelado; las campañas temporales y en vivo fijan un perfil por corrida, declarado en el manifiesto. Los
> resultados por modelo y por familia, y los criterios pre-registrados con que se seleccionó el perfil de
> cada campaña, se presentan en la sección 17.5.
>
> Cada perfil declara sus umbrales y su postproceso en el catálogo, y cada corrida persiste la configuración
> efectiva utilizada, sin constantes ocultas en el código. A título de ejemplo, el perfil fijado por
> criterio pre-registrado para las corridas en vivo declara umbral de caja de 0,30 y de texto de 0,25; su
> postproceso aplica confianza mínima de 0,25, supresión de solapamientos con IoU de 0,50 y área mínima de
> caja de 100 píxeles cuadrados; y el control de ritmo opera con selección determinista de paso 1 y una cola
> máxima de ocho unidades.

Qué cambia y por qué: (1) **MM-GDINO pasa de fila del catálogo a hecho histórico con remisión a §17.5** —
deja de ser falso y se vuelve evidencia de sustituibilidad (la familia entró y salió sin tocar el contrato);
(2) **"el perfil desplegado para el núcleo es X" desaparece** — lo reemplaza la regla general (un perfil por
instancia, un perfil por corrida, declarado en el manifiesto) y la flota que materializa el catálogo entero;
(3) los valores efectivos **se conservan todos** pero como *ejemplo* de la propiedad que importa (config
efectiva persistida), y el identificador `gdino-tiny-560` sale de la prosa — coherente con D-P2-6, el
manifiesto de cada corrida es quien lo declara; (4) la selección queda como **decisión operativa
pre-registrada por campaña**, con su criterio en §17.5, no como veredicto.

**C. Nota para la redacción de §17.5 (fuera del alcance de este pase, dejar constancia):** presentar los
resultados **por modelo y por familia**, cada combinación con su dato; la selección del perfil live se
presenta como decisión operativa con criterio pre-registrado sobre el banco de imágenes, incluyendo que la
misma comparación identificó a un perfil distinto como más fuerte en otra dimensión (recall de la condición
CR-01) — la evidencia de que el veredicto es por combinación, no único. Nunca la fórmula "el mejor modelo".

---

## C. Unidades opcionales — la regla de las dos columnas

Estas cuatro unidades **no eliminan contenido**: cambian el formato de tablas que, por D-P2-1, son listas.
Aplicarlas baja el conteo sin perder una palabra; no aplicarlas no rompe nada. Van separadas porque son
decisión de estilo, no de contenido.

### C-01 (opc) · Tablas 52, 59 y 60 — pasar a viñetas
Las tres son de dos columnas. **52** (hechos persistibles mínimos, 12 filas) es la más defendible: se
consulta como checklist. **59** (riesgos y mitigaciones, 9 filas) es la más prescindible: tres de sus filas
—pérdida silenciosa en el bus, relojes incompatibles, fuente no temporal— ya están en §17.3.13.3 con más
precisión, incluidos los códigos de causa. **60** (plan de materialización, 10 filas) tiene contenido
propio y es el puente a §17.4. En los tres casos: viñeta con el término en negrita y su explicación a
continuación.

### C-02 (opc) · §17.3.15, Tabla 58 — pasar a items
Cuatro filas, y viene inmediatamente después de una figura que ya muestra los mismos roles. Cuatro párrafos
breves (uno por rol) leen igual o mejor.

### C-03 (opc) · §17.3.14.5, Tabla 57 — pasar a items
Es la expansión de **una celda** de la Tabla 56 (la fila "Instrumentación adicional", que ya enumera
captura, profundidad de cola, descartes, jitter, reemplazo de frames y estado de fuente) y se solapa con la
Tabla 55 en descartes, timestamps y errores. Si se aplica esta unidad, la edición 5 de E3-28 sobre la Tabla
57 se absorbe acá.

### C-04 (opc) · §17.3.13.1, Tabla 53 — revisar contra la Tabla 54
Es la más floja de las que este pase conserva: su tercera columna nombra las métricas que la Tabla 54 define
dos párrafos después con `Métrica | Inicio | Cierre | Unidad`. Y §17.3.13 queda con tres tablas seguidas
(53, 54, 55). La 54 es la mejor tabla del capítulo y no se toca; si hace falta una cuarta baja, es la 53.

---

## D. Hechos verificados (2026-08-20) — NO "corregir" estos valores

Todo lo que sigue se contrastó contra los dos `.docx` vigentes. Procedimiento para re-verificar: los `.docx`
son ZIP; `word/document.xml` contiene el cuerpo, con `w:p` para párrafos y `w:tbl` para tablas. Los conteos
se obtuvieron extrayendo el texto de cada bloque en orden de aparición.

**Sobre `opt-in` y `fail-open`:**
- Apariciones en §17.3: `opt-in` **4** (Tabla 43/DA-11, §17.3.7.3, Tabla 57, Tabla 59) · `fail-open` **7**
  (las cuatro anteriores más §17.3.14.5, Tabla 58 y Tabla 61).
- Apariciones en §17.4: **0** de ambos. Búsqueda ampliada a `preselec`, `borde`, `OAK` y `EN` como rol:
  **0 resultados**.
- Apariciones en las secciones previas del informe (frontmatter/intro/objetivos/plan; §17.1 consolidación
  metodológica; estado del arte; marco teórico; cierre/anexos/referencias): **0 y 0**. Ambos términos nacen
  en §17.3.
- `fail-open` se glosa **dos veces** (§17.3.7.3 y §17.3.14.5); `opt-in`, **ninguna**.
- La preselección en el borde aparece **11 veces** en §17.3, en cuatro tablas distintas.

**Sobre tablas y columnas:**
- Tabla 67 (§17.4): la columna "Estado" dice "Verificada" en **7 de 7** filas.
- Tabla 68 (§17.4): **6 filas**; ninguna corresponde al rol de captura ni a la preselección.
- Tabla 65 (§17.4): **2 filas**.
- Tabla 51 (§17.3): **3 de 5** filas de la columna "Estado de diseño" empiezan con "Extensión prevista".
- Tablas 40 y 41 (§17.3): comparten la taxonomía de cinco tratamientos y sus Notas son la misma glosa
  redactada dos veces.
- Tabla 49 vs. Tabla 50 (§17.3): la columna "Contrato principal" de la 49 es el conjunto de la columna 1 de
  la 50.
- Métricas de forma (filas × columnas, mediana de caracteres por celda) de las tablas citadas: T39 6×3 med
  125 (máx 299) · T47 6×4 med 126 · T66 4×3 med 101 · T56 6×4 med 80 · T54 8×4 med 30 · T63 16×4 med 20 ·
  T55 9×3 med 26 · T45 13×4 med 26.

**Sobre referencias cruzadas (verificado antes de proponer cada eliminación):**
- **DA-03** no está citada en §17.4; la única fila del pase de decisiones citada allí es **DA-13**
  (§17.4.6).
- **§17.3.6.6** no está referenciada en ninguna prosa de §17.3 ni de §17.4.
- Referencias en prosa a tablas que este pase elimina: *"La Tabla 39 sintetiza…"* (§17.3.2), *"La Tabla 49
  resume…"* (§17.3.11.2) y *"La Tabla 51 explicita…"* (§17.3.11.4). Las tres se resuelven dentro de su
  unidad.
- §17.4.5 afirma: *"En los experimentos del presente trabajo, los servicios se ejecutaron co-ubicados en un
  único host con GPU."*

---

## E. Renumeración resultante (consecuencia de aplicar §A y §B)

Aplicando las unidades **no opcionales**: §17.3 pasa de 24 a **18 tablas** (fusión 40+41; bajas 39, 49, 51,
61 y 62) y §17.4 de 7 a **6** (baja 65). La numeración definitiva la fija el maestro al integrar; el mapa
esperado es:

**§17.3 — de 24 a 18 tablas**

| Actual | Contenido | Nuevo |
|---|---|---|
| 40 + 41 | Capacidades arquitectónicas y su tratamiento (fusionadas, §17.3.3.2) | **39** |
| 42 | Requisitos no funcionales de referencia | **40** |
| 43 | Decisiones arquitectónicas iniciales | **41** |
| 44 | Elementos mínimos de la configuración experimental | **42** |
| 45 | Vocabulario inicial de prompts por condición | **43** |
| 46 | Componentes mínimos de una definición de patrón | **44** |
| 47 | Diseño del motor de patrones según condición | **45** |
| 48 | Consumidores y salidas del tramo de distribución | **46** |
| 50 | Contratos mínimos para la ejecución experimental | **47** |
| 52 | Hechos persistibles mínimos | **48** |
| 53 | Métricas y evidencias por tramo | **49** |
| 54 | Diccionario de métricas | **50** |
| 55 | Señales observables del sistema | **51** |
| 56 | Comparación DBE / EBE | **52** |
| 57 | Condiciones observables para interpretar EBE | **53** |
| 58 | Roles funcionales y unidades desplegables | **54** |
| 59 | Riesgos arquitectónicos y mitigaciones | **55** |
| 60 | Plan de materialización del núcleo | **56** |

Bajas: **39** (→ viñetas, E3-22), **49** (→ prosa, E3-23), **51** (→ párrafo, E3-24), **61** (E3-25) y
**62** (E3-26).

**§17.4 — de 7 a 6 tablas**

| Actual | Contenido | Nuevo |
|---|---|---|
| 63 | Correspondencia contratos del diseño ↔ materialización | **57** |
| 64 | Interfaces principales de los servicios | **58** |
| 66 | Artefactos persistidos por componente | **59** |
| 67 | Evidencia de verificación técnica | **60** |
| 68 | Capacidades ejercidas, exclusiones y brechas | **61** |
| 69 | Puntos de extensión y costo técnico | **62** |

Baja: **65** (E4-20).

**Referencias en prosa a actualizar** — §17.3: *"las decisiones enumeradas en la Tabla 43"* (§17.3.4) →
**41**; *"La Tabla 44 resume…"* (§17.3.6.2) → **42**; *"La Tabla 45 organiza…"* (§17.3.6.4) → **43**;
*"…se sintetizan en la Tabla 46"* (§17.3.8.2) → **44**; *"La Tabla 48 distingue…"* (§17.3.10.2) → **46**;
*"La Tabla 56 resume…"* (§17.3.14.4) → **52**. §17.4: *"La Tabla 63 establece…"* (§17.4.2) → **57**;
*"La Tabla 68 evita…"* (§17.4.10) → **61**.

**Consecuencia aguas abajo:** **§17.5 pasa a numerar desde la Tabla 63** (hoy arrancaría en la 70). Por eso
D-P2-3: conviene resolver este pase antes de redactar §17.5 y §17.6. Si además se aplican las unidades
opcionales de §C, el mapa se corre otro tanto y debe recalcularse al integrar.

**Subsecciones** (✎ agregado 2026-08-22 — faltaba: dos unidades de este pase eliminan encabezados y §E sólo
cubría tablas). Dos corrimientos, en ramas distintas y por lo tanto independientes:

| Unidad | Encabezado que se elimina | Corrimiento |
|---|---|---|
| **E3-20** | §17.3.6.6 *Validaciones previas al inicio de la corrida* | §17.3.6.7 → **§17.3.6.6** |
| **E3-30** | §17.3.11.1 *Criterios de diseño de contratos* | §17.3.11.2 → **.1** · §17.3.11.3 → **.2** · §17.3.11.4 → **.3** |

**No hay referencias que se rompan** — verificado sobre ambos `.docx`: el par entero contiene sólo tres
referencias a subsecciones de §17.3 (§17.3.11 como padre, y "sección 17.3.8.2" y "sección 17.3.8.4" desde
§17.4), y **ninguna** apunta a un encabezado que se mueva. Sí quedan afectadas las referencias *internas de
este documento de correcciones*: **E3-23** apunta a "§17.3.11.2, Tabla 49" y **E3-24** a "§17.3.11.4,
Tabla 51"; con E3-30 aplicada pasan a §17.3.11.1 y §17.3.11.3. La enmienda de E3-28 usa ancla descriptiva y
no numérica justamente para no depender de este mapa.

**Figuras:** este pase no toca ninguna figura. El mapa de §E del pase 1 sigue vigente.

---

## F. Alcance sobre el resto del informe

Para que el criterio D-P2-1 no quede aplicado sólo donde se estaba trabajando, se relevó la forma de
**todas** las tablas del informe. Resultado:

**§17.3 es la anomalía del documento, no la norma.** Las secciones ya cerradas usan matrices densas —de 4 a
7 columnas con celdas de 7 a 47 caracteres de mediana (Tablas 23, 24, 26, 29, 33, 36)—, que es exactamente
el caso en que una tabla se justifica. §17.3, en cambio, usa 3 columnas con medianas de 30 a 126 caracteres:
grillas de prosa. Esa diferencia de forma explica por qué el capítulo se siente sobrecargado de tablas
aunque tenga menos que §17.1.

**Lo que el criterio marcaría fuera de §17.3/§17.4, si se aplicara de manera uniforme** (relevamiento de
forma, **sin** revisión de contenido — no se propone acción):

- **Celdas largas (prosa en grilla):** Tabla 13 (mediana **278** caracteres), Tabla 7 (**196**), Tabla 14
  (**190**), Tabla 12 (**116**), Tabla 5 y Tabla 15 (**122** cada una) — todas en estado del arte y marco
  teórico.
- **Dos columnas:** Tablas 19, 20 y 28 (§17.1), más varias tablas de anexo en el cierre. La Tabla 1 también
  es de dos columnas pero es un glosario de 61 entradas: ahí el formato es correcto.
- **Dos filas:** Tabla 30 (§17.1).

**Por qué no se propone tocarlas acá:** esas secciones están cerradas y su renumeración arrastraría todo el
informe — son **38 tablas numeradas** (Tablas 1 a 38) y **62 apariciones** de "Tabla N" entre rótulos y
referencias en prosa, que habría que recorrer una por una. Si se decide extender el criterio, corresponde un
pase propio y debe hacerse **antes** que este, no después, para renumerar una sola vez. Mi recomendación es
**no abrirlo**: el costo de renumeración supera la ganancia, y ninguna de esas tablas presenta el problema
que sí presenta §17.3 —duplicación entre tablas vecinas y columnas que no discriminan—.

**Lo que este pase sí verificó en todo el informe:** la trazabilidad terminológica de `opt-in` y
`fail-open` (§D), que era la pregunta de origen de E3-28.

---

## Fuente: `docs/informe/entregable/desarrollando/archivado/correcciones-etapa-3-4-5-pase-3.md`

> SHA-256 del bloque: `fb6ecd18525c80a73bb110e7c86f40a17ef888baeb2fc5dd883a3ac5eb75acb6`  
> Seleccion: pase de cierre 3 (2026-08-22): YA APLICADO Y VERIFICADO en el documento de trabajo (2026-08-23) - NO volver a aplicarlo; enmendo a E3-22 y E4-22, y su seccion D fija las restricciones de la etapa 5. Sus decisiones D-P3-1..6 siguen rigiendo.

# Correcciones — pase 3 sobre §17.3 (Diseño), §17.4 (Implementación) y restricciones para §17.5

**Fecha:** 2026-08-22 · **Insumos:** los **40 comentarios en 29 hilos** que quedaron en
`E-OVRT-VDP_Seccion_17.3_Diseno_Arquitectonico_v1.1.docx` (37 comentarios) y
`E-OVRT-VDP_Seccion_17.4_Implementacion_v1.2.docx` (3), extraídos de `word/comments.xml` con sus hilos,
anclajes y respuestas.
**Verificación:** cada afirmación de repetición, cada referencia cruzada y cada hecho técnico de este
documento fue contrastado el 2026-08-22 contra el texto extraído de ambos `.docx`, contra las secciones
cerradas del informe (`E-OVRT-VDP_v1.1_05062026-sin-etapa3.docx`) y contra el código de los cinco
repositorios. El procedimiento de re-verificación está en §E.

**Relación con los pases 1 y 2.** Este pase **continúa la numeración** (§17.3 desde **E3-32**, §17.4 desde
**E4-27**; con las adiciones del mismo día llega a **E3-42** y **E4-30**) y **no reabre** ninguna decisión
firmada. Siguen rigiendo D1–D4 y la regla de autocontención del
pase 1, y D-P2-1…D-P2-6 del pase 2. **Dos unidades del pase 2 se enmiendan** por hechos verificados en
este pase, no por cambio de criterio: **E3-22** (produciría una duplicación) y **E4-22** (afirma algo falso).
Las enmiendas están en §A y son parte de este pase; el texto del pase 2 no se reescribe.

**Numeración de tablas usada acá:** la **vigente en los `.docx`** (§17.3 = Tablas 39–62; §17.4 = 63–69).
El mapa resultante de aplicar los tres pases está en §G.

> ✎ **Dos defectos del propio kit, corregidos al abrir este pase (2026-08-22).**
> 1. `entregable/90-etapa3-texto-extraido.md` —el texto base de §17.3 que el generador entrega a la etapa 3—
>    era la extracción **v0.1**: 24.389 palabras contra las 20.622 de la v1.1 vigente, y decía "contratos
>    preliminares" donde el informe hoy dice "contratos versionados". **Regenerado** desde el `.docx` vigente
>    (regla D-C). Diferencia: 728 líneas fuera, 517 dentro.
> 2. La etapa 4 no tenía texto base extraído: el generador entregaba `borradores/17-4.md`, el borrador previo
>    al pegado y **anterior al pase 2**. Se agregó **`entregable/90b-etapa4-texto-extraido.md`** con la
>    extracción de la v1.2 vigente; el borrador se conserva como material, ya no como base.

---

## Decisiones que rigen este pase

- **D-P3-1 — Propósito por sección, y alineación entre secciones.** *(directiva del usuario, 2026-08-22)*
  Una subsección se justifica cuando **sostiene algo que ninguna otra sostiene**. El criterio se aplica en
  tres preguntas, en este orden:
  1. **¿Qué afirma que no esté afirmado antes?** Si la respuesta es "nada", la subsección se elimina y su
     aporte —si lo tiene— se reubica en la sección que ya es dueña del concepto.
  2. **¿Se pisa con otra?** Dos subsecciones que responden la misma pregunta desde ángulos distintos se
     funden o se reparten explícitamente el terreno.
  3. **¿Su título anuncia lo que hace?** Si no, se retitula. Un título que promete lo que la sección no
     entrega es una repetición encubierta.
- **D-P3-2 — Poda quirúrgica, no estructural.** *(decisión del usuario, 2026-08-22)* Se eliminan párrafos
  verificados como duplicado y se resumen las subsecciones huecas. **No** se colapsan bloques enteros de
  subsecciones para ahorrar numeración. Dos subsecciones desaparecen en este pase (§17.3.6.7 y §17.3.7.4)
  y lo hacen porque quedaron sin contenido propio, no por presupuesto de páginas.
- **D-P3-3 — Alcance: etapas 3, 4 y 5. Las etapas 1 y 2 al final.** *(decisión del usuario, 2026-08-22)*
  §17.5 todavía no está redactada: para ella este pase **no corrige, restringe** (§D). Corolario duro:
  **§17.3 y §17.4 no pueden depender de una edición futura en §17.1**. Donde el pase 1 había resuelto un
  problema de §17.3 mediante un ajuste en etapa 2, este pase lo resuelve **dentro de §17.3**, y el ajuste de
  etapa 2 pasa de obligatorio a armonizador (ver **E3-42**).
- **D-P3-4 — Un concepto se define donde se decide.** Extiende el criterio ya usado en la enmienda a E3-28:
  el término se nombra y se glosa **en prosa**, **en la subsección que es dueña de la decisión**, y los usos
  posteriores lo referencian sin redefinirlo. Nunca en una celda de tabla, nunca dos veces.
- **D-P3-5 — Un calco no es un término técnico.** Se normalizan (a) los calcos del inglés que tienen un
  equivalente castellano corriente y (b) los anglicismos crudos **que el propio informe ya normalizó en otro
  pasaje** —el defecto no es el anglicismo, es la inconsistencia—. **No** se persiguen los términos técnicos
  sin equivalente establecido ni los literales de configuración (ver la lista cerrada en **E3-33**).
- **D-P3-6 — §17.5 se organiza por pregunta de medición, no por cronología de campañas.** *(decisión del
  usuario, 2026-08-22.)* La sección es un **resumen de resultados**: reporta qué se midió y cuánto dio,
  organizado por la pregunta que cada medición responde — **nunca por el orden en que se experimentó**. Los
  identificadores de campaña (T1/G1/R1–R6/B1/D1/H1/I1/I2…) aparecen como **procedencia del dato**, jamás
  como estructura del texto: ningún título de subsección lleva nombre de campaña. La sección justifica
  **todos los caminos**: los adoptados (con su criterio pre-registrado), los probados y no adoptados (con
  el veredicto que los descartó) y los **no ejecutados o no implementados, con su factor de justificación**
  — la exclusión se lee como alcance declarado, no como omisión. El esquema concreto está en §D.0.
  ⚠ Trampa que la reorganización temática vuelve más peligrosa: la campaña "T1" del banco de clips y el
  tramo "T1" del ajuste fino **no son lo mismo** — al convivir en una sola sección, cada mención dice de
  cuál habla.
- **Heredadas:** regla de autocontención (el informe no referencia documentos locales, ADRs, fichas ni
  índices del repositorio; **sí** referencia sus propias secciones), carácter orientativo de los textos guía
  (reformulables conservando contenido y registro académico; decimales con coma, milisegundos como
  "4.000 ms"), y D-P2-1 (criterio de tabla), D-P2-5 y D-P2-6 (identificadores versionados).

---

## A. Enmiendas a dos unidades del pase 2

### ✎ ENMIENDA a E3-22 · §17.3.2 — las viñetas propuestas ya existen como prosa

**Por qué se enmienda.** E3-22 propone reemplazar la Tabla 39 por seis viñetas insumo → decisión. Verificado
contra el `.docx` v1.1: **esas seis viñetas ya están escritas**, como los seis párrafos que arrancan en
*"La arquitectura propuesta se deriva de las definiciones metodológicas consolidadas en las secciones
anteriores…"* y desarrollan uno por uno el marco teórico, el núcleo CR-01/CR-02, los escenarios, los roles,
el marco de métricas y los lineamientos ético-legales. Aplicar E3-22 tal cual dejaría **dos** enunciados del
mismo contenido donde hoy hay tres.

**El estado real de §17.3.2 (1.197 palabras) es una triplicación:**

| Bloque | Qué dice | Veredicto |
| --- | --- | --- |
| Cuatro párrafos introductorios | insumos, prioridad CR-01/CR-02, DBE/EBE, y el puente a la tabla | duplican tres de los seis párrafos de abajo, uno casi palabra por palabra |
| Tabla 39 (6 × 3) | insumo → criterio → decisión | mediana de 125 caracteres por celda; su columna del medio resume §17.1 |
| Seis párrafos desarrollados | el vínculo insumo → decisión, uno por insumo | **es el texto que se queda** |

La duplicación literal: ¶1 dice *"La arquitectura propuesta **se construye a partir de** las definiciones
metodológicas consolidadas en las secciones anteriores. En particular, toma como insumos el alcance
experimental…"* y ¶5 dice *"La arquitectura propuesta **se deriva de** las definiciones metodológicas
consolidadas en las secciones anteriores. El alcance experimental, las condiciones de riesgo…"*.

**Acción — tres ediciones.**

1. **Eliminar la Tabla 39, su Nota y la oración que la introduce** (*"La Tabla 39 sintetiza esta relación
   entre definiciones previas y decisiones arquitectónicas derivadas."*).
2. **No crear las viñetas de E3-22.** Esa acción queda derogada por esta enmienda.
3. **Reemplazar los cuatro párrafos introductorios por un párrafo de entrada.** Texto guía:

   > *"La arquitectura propuesta se deriva de las definiciones metodológicas ya consolidadas: el alcance
   > experimental del prototipo, el catálogo de condiciones de riesgo, los escenarios de evaluación, los
   > roles funcionales del entorno, el marco de métricas y los lineamientos ético-legales actúan como
   > restricciones de diseño. Lo que sigue no reitera el protocolo experimental: explicita qué consecuencia
   > arquitectónica se deriva de cada uno de esos insumos, de modo que ningún módulo, frontera o flujo del
   > sistema aparezca como una decisión aislada."*

4. Los seis párrafos desarrollados se conservan **menos el de CPN, EN y TN**, que pasa a **E3-34**.

**Resultado:** 1.197 → ~600 palabras. **−1 tabla, −4 párrafos, un solo enunciado del vínculo insumo → decisión.**

*Origen: hilo C0 de §17.3 (vos: "como para sacar la tabla y acortar" · "sí tiene sentido la sección…, lo que
quería sacar es la tabla") y las dos respuestas de Gabriel ("podría ser más resumido" · "lo que está después
va, esto lo volaría").*

---

### ✎ ENMIENDA a E4-22 · §17.4.10, Tabla 68 — la preselección en el borde **sí se ejerció**

**Por qué se enmienda.** E4-22 propone una fila que dice *"no ejercida"* y *"no puede reclamarse como
propiedad verificada del prototipo"*. **Ambas afirmaciones son falsas.** Verificado contra el código y contra
el registro operativo:

| Hecho | Evidencia |
| --- | --- |
| La preselección está **implementada** | Filtro de personas ejecutado en el propio dispositivo de captura, con umbral, ventana de evidencia, latido incondicional y apertura total ante silencio de la red neuronal; validación que impide configurar una apertura posterior al vencimiento de la evidencia. Deshabilitada por defecto. |
| Está implementada **sólo para la cámara propia** | El esquema de configuración la rechaza para cualquier otro tipo de fuente. Para las fuentes por red no existe. |
| Su efecto está **medido** | Comparación pareada contra el flujo completo con el mismo detector: **87 % de unidades descartadas en el dispositivo**. |
| Estuvo **apagada en todo lo evaluativo**, por decisión previa a los resultados | Un filtro de fotogramas sin persona suprime justamente las detecciones sostenidas que la tasa de falsos positivos por hora existe para medir; y agrega el error multiplicativo de un detector más débil sobre la cadena que se quiere caracterizar. |

Es decir: no es una brecha, es **una capacidad implementada y medida cuya exclusión de lo evaluativo es un
resultado metodológico**. La versión de E4-22 convierte un acierto del trabajo en un agujero.

**Acción — reemplazar la fila propuesta por E4-22 por ésta** (misma posición: después de *Condiciones de
riesgo de nivel 2 y 3*):

> **Preselección liviana en el rol de captura** ||
> *Implementada para la fuente de captura propia como filtro de personas ejecutado en el dispositivo, con
> criterio de degradación segura y deshabilitada por defecto; su reducción de carga se midió en una
> comparación pareada contra el flujo completo, con un 87 % de unidades descartadas antes de salir de la
> cámara. No existe para las fuentes por red. Permaneció deshabilitada en todas las corridas evaluativas.* ||
> *La exclusión de lo evaluativo es deliberada y anterior a los resultados: un filtro de fotogramas sin
> persona suprimiría las detecciones sostenidas que la tasa de falsos positivos por hora existe para medir, y
> superpondría el error de un detector auxiliar más débil sobre la cadena que se busca caracterizar.
> Habilitarlo cambiaría la procedencia de esas métricas en lugar de mejorarlas. La capacidad se reporta,
> entonces, como implementada y caracterizada fuera del régimen evaluativo.*

**Se conserva de E4-22:** el diagnóstico (once menciones en §17.3 contra cero en §17.4 era, efectivamente, un
agujero de rendición de cuentas) y el complemento recomendado de bajar la huella en §17.3.

**Consecuencia para §17.5:** si §17.5 vuelve a citar el 87 %, debe hacerlo con su denominador y su condición
de medición. Si no lo hace, esta celda es su único lugar en el informe y así queda declarado en §D.

*Origen: C20 de §17.3 ("esto en oakd lo hicimos. asegurarse que esté claro en etapa 4. RTSP no lo hicimos").*

---

## B. Correcciones nuevas a §17.3 — Diseño Arquitectónico

> **Dato que ordena todo este bloque:** §17.3 pesa **20.622 palabras** contra **5.477** de §17.4 — 3,8 a 1
> entre el diseño y su materialización. Las quince repeticiones que siguen fueron verificadas una por una
> contra el texto; ninguna se corrige por impresión de extensión.

### E3-33 · Calcos del inglés y anglicismos que el informe ya normalizó en otro pasaje

**Problema.** Dos comentarios apuntan a traducciones malas (*"traducción chotísima, mejorar o cambiar esa
palabra"* sobre **frescura**; *"otra traducción muy chota"* sobre **fuentes vivas**). Relevado el capítulo
completo, el defecto es más amplio y tiene dos formas distintas, que se tratan distinto.

**(a) Calcos con equivalente castellano corriente — se reemplazan.**

| Término | Apariciones | Reemplazo único | Nota |
| --- | --- | --- | --- |
| `frescura` | 5 | **actualidad** (en enumeraciones) · **actualidad de la unidad visual** (donde nombra la política) | Calco de *freshness*. La política que nombra es "preferir la unidad más reciente"; "frescura" no dice eso en castellano técnico. |
| `fuente viva` / `fuentes vivas` | 9, más una forma verbal (*"la fuente es viva"*) | **fuente en vivo** / **fuentes en vivo** | Calco de *live source*. El informe **ya dice "en vivo"** en §17.3.8.4 (*"una corrida viva"* → también se normaliza), en §17.4.4 y en §17.4.5 (*"corrida en vivo"*, *"camino de ejecución en vivo"*): el reemplazo alinea, no innova. Alcanza al título de §17.3.14.2, que pasa a **"EBE como escenario de fuente en vivo controlada"**. |
| `pulleable` | 1 (§17.3.7.3) | perífrasis | *"…o en general con **fuentes cuya lectura puede regularse** —conjuntos de imágenes, videos locales o archivos—"*. Nadie lo marcó, pero es el peor de los tres. |

**(b) Anglicismos crudos que el propio informe ya tradujo en otro lugar — se alinean.** El defecto acá no es
el anglicismo: es que el mismo capítulo usa las dos formas.

| Término | Dónde sobrevive tras los pases 1 y 2 | Forma ya usada en el informe |
| --- | --- | --- |
| `PUB/SUB` | §17.3.8.1, §17.3.8.4 | **publicador-suscriptor** (§17.3.5, §17.3.18) |
| `config-driven` | §17.3.18 | **gobernado por configuración** (§17.3.5, §17.4.4) — E3-19 ya lo saca de DA-03 |
| `outcome` | §17.3.10.2 (Tabla 48), §17.3.13.1 (Tabla 53), §17.3.13.3 (Tabla 55) | **resultado de entrega** / **resultado del canal** (§17.3.10.1, §17.3.10.3) |
| `backpressure` | §17.3.14.5 (Tabla 57) | **acumulación de atraso** (§17.3.7.3, §17.3.14.4) |
| `keep-up` | §17.3.16 (Tabla 59) | **capacidad de sostener el ritmo** |
| `letterbox` | §17.3.7.1 | **relleno de bordes** |

**(c) Lista cerrada de lo que NO se toca, con su razón** — para que no se "corrija" por las dudas en un pase
posterior: `checkpoint`, `ledger`, `frame`, `buffer`, `tracker`, `streaming`, `snapshot`, `bounding box`,
`jitter` (términos técnicos sin equivalente castellano establecido en la literatura del dominio);
`fail-open` (queda glosado una sola vez por la enmienda a E3-28, que es la doctrina D-P3-4 aplicada); y
`scene` / `subject` (son **valores literales de configuración**, no prosa: nombran lo que se escribe en el
archivo de patrones).

*Origen: C5 y C6 de §17.3.*

---

### E3-34 · CPN, EN y TN se explican **tres veces** en el informe

**Problema — verificado sobre el `.docx` maestro.** Los tres roles quedan definidos en la consolidación
metodológica (§17.1.4.2 y sus tres sub-apartados), con este texto:

> *"…el Central Processing Node (CPN) concentra la ejecución del pipeline principal, la inferencia, la
> evaluación de patrones, la medición de latencia y la consolidación de resultados experimentales. El Edge
> Node (EN) se ubica próximo a la fuente visual y se orienta a captura, transmisión de video y eventual
> preprocesamiento liviano. El Training Node (TN), cuando corresponda, se reserva para tareas de ajuste o
> preparación de variantes de modelo, sin sustituir la evaluación operativa sobre el CPN."*

§17.3 lo vuelve a decir **dos veces más**, casi con las mismas palabras: en §17.3.2 (*"El CPN concentra las
capacidades centrales de procesamiento y evaluación; el EN representa la captura o el procesamiento próximo
a la fuente; y el TN delimita las tareas de entrenamiento o adaptación cuando corresponden"*) y en la
apertura de §17.3.15. Es el mismo párrafo tres veces en el mismo documento.

**Acción — dos ediciones. En ninguna de las dos §17.3 redefine los roles.**

1. **§17.3.2 — reemplazar el párrafo de roles por su consecuencia arquitectónica**, que es lo único que
   corresponde a esta sección (la sección trata de qué se *deriva* de cada insumo, no de qué *es* cada insumo):

   > *"De los roles funcionales ya establecidos se deriva una restricción de diseño y no una nueva
   > definición: se adoptan como responsabilidades de referencia que permiten declarar dónde se captura,
   > dónde se ejecuta la inferencia y dónde se prepara una variante ajustada, sin que la distribución física
   > de componentes pase a formar parte de la semántica de los contratos."*

2. **§17.3.15 — reemplazar el primer párrafo por una entrada que remita y no repita.** El resto de la
   sección (topología de referencia, el TN fuera del camino de inferencia, el módulo de distribución como
   unidad desplegable) es contenido propio y se conserva:

   > *"Esta sección no redefine los roles funcionales ya establecidos en la consolidación metodológica: fija
   > la topología de referencia con la que se materializan en el prototipo y ubica en ella al módulo de
   > distribución. La única precisión que el diseño agrega es que ninguno de los tres roles equivale
   > necesariamente a una máquina dedicada."*

*Origen: C7 y el hilo C35/C36 de §17.3 ("esto ya está claro en etapa 2, no volver a explicar acá" · "o
introducir brevemente haciendo referencia a la sección de la etapa 2"). La remisión a una sección **propia**
del informe no viola la autocontención, que alcanza a documentos del repositorio.*

---

### E3-35 · §17.3.6.7 "Frontera con los planos de ejecución y el soporte experimental" — eliminar y reubicar

**Problema.** La subsección tiene tres párrafos y **dos de ellos ya están dichos**:

| Párrafo | Qué dice | Dónde ya está |
| --- | --- | --- |
| 1 | La configuración define los parámetros del plano de medios; el plano de medios los aplica pero no los diseña ni versiona. | §17.3.7, párrafo de apertura, con más precisión; y otra vez en §17.3.7.4 (que **E3-36** elimina por lo mismo). |
| 2 | Para el plano de control, la configuración define patrones, severidad, ventanas, histéresis. | Tabla 44, fila *Patrones activos*; y §17.3.8.3.1 completo. |
| 3 | Para el soporte experimental, la configuración es la clave de reconstrucción. | Es lo único propio, y aun así §17.3.12.1 lo repite (*"Toda alerta puede reconstruirse hasta la configuración efectiva…"*). |

Es exactamente el caso de §17.3.6.6, que **E3-20** ya resolvió con poda y reubicación, y por eso Gabriel pide
el mismo tratamiento.

**Acción — eliminar la subsección y rescatar una oración**, al cierre de §17.3.6.1 (*"Función arquitectónica
de la configuración experimental"*, que es la dueña del concepto):

> *"Esa función de gobierno se proyecta sobre los tres destinatarios de la configuración: el plano de medios
> recibe los parámetros que aplica sin diseñarlos ni versionarlos, el plano de control recibe los criterios
> con los que evalúa, y el soporte experimental la utiliza como clave de reconstrucción, de modo que todo
> evento, métrica, alerta o evidencia conservada pueda rastrearse hasta la corrida que le dio origen."*

⚠ **Consecuencia de numeración, encadenada con E3-20.** E3-20 elimina §17.3.6.6 y corre §17.3.6.7 → §17.3.6.6.
Con E3-35 esa subsección también desaparece: **§17.3.6 queda con cinco subsecciones (6.1 a 6.5)**, sin
renumeración adicional respecto de lo que ya fija E3-20.

*Origen: C15 de §17.3 ("ídem a lo anterior… es una sección que no tiene tanto propósito en sí misma, podría
rescatarse mucho más resumida entre 17.3.6.1 y 6.2").*

---

### E3-36 · §17.3.7.4 "Relación con configuración, modelos y prompts" — eliminar, salvo su último párrafo

**Problema — la subsección entera es eco, con una sola excepción.** Cuatro párrafos, 263 palabras:

| Párrafo | Veredicto |
| --- | --- |
| 1 — *"El Pipeline de Medios consume la configuración experimental definida para la corrida, pero no la gobierna…"* | **Duplicado casi literal** del párrafo de apertura de §17.3.7: *"La configuración experimental actúa como entrada transversal del Pipeline de Medios, pero no es una responsabilidad interna de este plano… sin convertirse en el módulo encargado de gobernarla o versionarla."* |
| 2 — prompts como contexto semántico | Ya está en §17.3.6.3 y en §17.3.7 (apertura). **Excepción:** la oración sobre reutilizar representaciones textuales precalculadas es un compromiso de diseño que no aparece en ningún otro lado — se rescata. |
| 3 — la salida debe incluir referencias suficientes para reconstruir el origen | Es el cuarto criterio de §17.3.7.2 (*"conservar la trazabilidad mínima del resultado perceptivo"*) y el cierre de §17.3.7.1. |
| 4 — la salida no se reduce a cajas y puntajes, pero tampoco incorpora severidad ni decisión de alerta | **Es el único aporte propio de la subsección.** |

**Acción — eliminar §17.3.7.4** y reubicar sus dos rescates:

1. **El párrafo 4 pasa a cerrar §17.3.7.1** (*"Flujo operativo del Pipeline de Medios"*), inmediatamente
   después del bloque **Publicación de evidencia perceptiva**, que es donde el tema es la salida:

   > *"En consecuencia, la salida del plano de medios no se reduce a cajas y puntajes sin contexto, pero
   > tampoco incorpora severidad, confirmación de patrón ni decisión de alerta. Su producto es evidencia
   > visual primaria, normalizada y trazable: la interpretación de esa evidencia corresponde al plano de
   > control, y la comparación entre configuraciones, modelos y prompts, al análisis experimental posterior."*

2. **La oración sobre representaciones precalculadas se anexa al bloque Inferencia open-vocabulary** de
   §17.3.7.1:

   > *"…según el formato propio del detector utilizado. Cuando el modelo lo permita, el adaptador puede
   > reutilizar representaciones textuales precalculadas o mecanismos equivalentes para reducir el costo de
   > inferencia, siempre que esa optimización no altere la trazabilidad de la corrida."*

⚠ **Consecuencia de numeración:** §17.3.7.5 pasa a **§17.3.7.4**. §17.3.7 queda con cuatro subsecciones.
Esto **afecta a la enmienda de E3-28**, cuya acción 3 reescribe el primer párrafo de "§17.3.7.5": la unidad
sigue siendo la misma —*"Capacidades opcionales sin desplazar el núcleo validable"*— y pasa a numerarse 7.4.
La enmienda a E3-28 ya previó este riesgo y por eso su ancla en §17.3.14.5 es descriptiva y no numérica.

*Origen: C18 y C19 de §17.3 ("esta sección es repetitiva, lo único rescatable es el último párrafo, reducir"
· "ya se dijo 20 veces").*

---

### E3-37 · §17.3.7.5 — los dos cierres que repiten la apertura del plano de medios

**Problema.** Dos pasajes concretos, ambos verificados:

1. **Última oración del segundo párrafo:** *"La decisión de que una detección persistió durante una ventana
   temporal sigue perteneciendo al motor de patrones."* Es el **quinto criterio de §17.3.7.2**, dos
   subsecciones antes: *"La persistencia temporal de un patrón, la histéresis, la severidad y el registro
   interno de alerta pertenecen al motor de patrones. El plano de medios… no debe decidir si una condición
   observada se convirtió en una situación de riesgo confirmada."*
2. **El párrafo de cierre completo** (*"Con esta delimitación, el Pipeline de Medios queda definido como una
   ruta de transformación acotada y medible: recibe entrada visual, controla el ritmo…"*) es la enumeración
   del **párrafo de apertura de §17.3.7**, que ya dijo *"Su alcance incluye ingesta, decodificación cuando
   corresponda, control de ritmo, normalización visual, inferencia open-vocabulary, postproceso y publicación
   no bloqueante"* y *"El Pipeline de Medios no confirma condiciones de riesgo, no asigna severidad, no
   ejecuta reglas de patrón, no genera alertas"*. Un cierre que repite la apertura no cierra: reinicia.

**Acción.**

1. Eliminar la oración del punto 1. El párrafo termina en *"…un identificador temporal no equivale a una
   condición de riesgo sostenida."*
2. Eliminar el párrafo de cierre completo. La subsección termina en el párrafo de variantes de eficiencia,
   cuya última oración ya cierra bien (*"…cualquier variante que altere la ruta frame-evento debe quedar
   declarada en la configuración de corrida"*).

⚠ **El primer párrafo de esta subsección lo reescribe la enmienda a E3-28** (ahí nace `fail-open`): esa
reescritura manda, y E3-37 no la toca. Resultado combinado: tres párrafos —el de E3-28, el de tracking sin
la oración repetida, y el de variantes de eficiencia—.

*Origen: C21 ("este tipo de aclaraciones repetitivas son una pija") y C22 ("esto ya se dijo antessss").*

---

### E3-38 · §17.3.8.3.1 — el mismo párrafo, dos párrafos después

**Problema.** La subsección dice lo mismo en el primer par de párrafos y en el tercero:

> **¶1:** *"Cada patrón referencia una condición del catálogo y define cómo esa condición debe ser evaluada
> durante la corrida."*
> **¶2:** *"…indica qué evidencia acepta, durante cuánto tiempo debe sostenerse, qué severidad tiene, qué
> histéresis aplica y qué evento debe emitirse cuando cambia de estado."*
> **¶3:** *"Cada patrón referencia una condición observable del catálogo CR-01 a CR-06 y define cómo esa
> condición será evaluada dentro del plano de control: evidencia requerida, ventana temporal, umbrales,
> histéresis, severidad y dependencias opcionales."*

Lo único que ¶3 agrega y no está en ningún otro lado es **la codificación PR-01 a PR-06** y su razón de ser.

**Acción — eliminar ¶3 y anexar su aporte al final de ¶2:**

> *"…y qué evento debe emitirse cuando cambia de estado. La codificación PR-01 a PR-06 identifica cada patrón
> y lo mantiene distinguible de la condición observable que evalúa (CR-01 a CR-06): una nombra el fenómeno,
> la otra la regla operativa que decide cuándo se lo considera sostenido."*

*Origen: C24 ("lo dijo literalmente en el párrafo anterior").*

---

### E3-39 · §17.3.8.3.4 — usar las siglas de métricas que la etapa 2 ya definió

**Problema.** El párrafo que vincula transiciones con métricas las nombra en castellano largo y no usa las
siglas, aunque **las tres están definidas con su sigla en la consolidación metodológica**: verificado en
§17.1.7.5.1 *Latencia de Alerta (t_alert-system)* —la sigla viaja como ecuación de Word, por eso no aparece
en las extracciones planas—, §17.1.7.5.2 *Tiempo a la Primera Detección (TTFD)* y §17.1.7.5.3 *Tasa de
Detección Sostenida (SDR)*. El resultado es que el lector no puede conectar este párrafo con la Tabla 54, que
las nombra por sigla cinco subsecciones más adelante.

**Acción — reescribir el tercer párrafo:**

> *"Las métricas operativas del plano de control se apoyan en estas transiciones: el tiempo hasta la primera
> detección (TTFD) se ancla en la primera evidencia perceptiva relevante; la latencia de alerta
> (t_alert-system) se cierra con el registro de la alerta interna que sigue a la transición a confirmado; la
> tasa de detección sostenida (SDR) se calcula sobre la continuidad del episodio; y los errores o descartes
> permiten distinguir una ausencia real de evidencia de una falla técnica o de una pérdida por muestreo."*

**No hay referencia hacia adelante:** las tres siglas nacen en §17.1, no en la Tabla 54. Al usarlas acá por
primera vez dentro de §17.3 se escribe el nombre completo delante, como en el texto guía; a partir de la
Tabla 53 el capítulo ya las usa solas.

*Origen: C26 ("usar siglas de las métricas que ya definimos").*

---

### E3-40 · §17.3.9 — la cadena condición → alerta se explica por cuarta vez

**Problema.** §17.3.9 llega después de que §17.3.7 y §17.3.8 ya recorrieron la cadena completa, y en vez de
aportar lo suyo —el **vínculo** entre condición metodológica y materialización, que sí es propio— vuelve a
narrar el funcionamiento del plano de control. Tres puntos verificados:

- **§17.3.9.1**, tercer párrafo: *"Allí se aplican criterios de persistencia, histéresis, severidad
  configurada… Sólo cuando el patrón alcanza una transición válida a confirmado se registra una alerta
  interna por episodio."* Ya dicho en §17.3.8 (apertura), §17.3.8.1, §17.3.8.2 y §17.3.8.3.
- **§17.3.9.2** repite dos veces dentro de sí misma: el primer párrafo dice *"El plano de medios consulta
  person, helmet y vest; el plano de control relaciona cada sujeto con la evidencia…"* y el segundo lo
  reformula como *"El plano de medios informa qué entidades observó… El plano de control decide si la
  evidencia de casco o chaleco se asocia al sujeto"*. Además el primero duplica §17.3.6.4.
- **§17.3.9.3**, segundo párrafo: *"La confirmación no es un hecho aislado: depende de detecciones
  acumuladas, criterios de persistencia, histéresis, severidad configurada y reglas activas. Por ello, la
  alerta interna debe poder reconstruirse desde la cadena completa…"* es §17.3.8.3.4, segundo párrafo.

**Decisión sobre §17.3.9.2 (era pregunta abierta en el hilo C28/C29).** **Se conserva**, podada. Es el único
lugar del informe donde la estrategia del núcleo está enunciada como **decisión adoptada** con su frontera
medios/control; borrarla dejaría a E-IND existiendo sólo dentro de celdas de tabla y de párrafos que la
mencionan de paso. Lo que se elimina es la reexplicación, no la decisión.

**Acción — tres ediciones.**

1. **§17.3.9.1 — reescribir el tercer párrafo** para que sea el eslabón y no el resumen del motor:

   > *"El plano de control evalúa esa evidencia mediante el patrón correspondiente y, cuando la evaluación
   > confirma el episodio, registra una alerta interna. Esa alerta es una salida asistiva del sistema: no
   > equivale a una notificación externa ni a una certificación normativa."*

2. **§17.3.9.2 — de cuatro párrafos a dos.** El primero enuncia la decisión y la frontera; el segundo, la
   razón y las ramas comparativas:

   > *"Para el núcleo validable se adopta la estrategia indirecta con inferencia espacial de ausencia
   > (E-IND). La frontera que esa elección fija es explícita: el plano de medios informa qué entidades
   > observó, dónde y con qué confianza; el plano de control decide si la evidencia del elemento de
   > protección se asocia al sujeto, construye el estado evaluable de la condición y lo estabiliza antes de
   > registrar una alerta."*
   >
   > *"La estrategia se adopta por auditabilidad: cada evaluación puede reconstruirse a partir de la caja del
   > sujeto, la región analizada, las detecciones de protección, los umbrales y la regla aplicada, de modo
   > que la ausencia no se presenta como una conclusión opaca del modelo. La detección directa (E-DIR) y las
   > variantes híbridas (E-HYB) se conservan como ramas comparativas configurables, con conjuntos de prompts
   > y reglas identificados por separado; comparten los contratos de publicación, evaluación temporal y
   > registro, de modo que la comparación no requiera alterar la arquitectura central."*

3. **§17.3.9.3 — retitular y reescribir.** Hoy se titula *"Trazabilidad de la cadena causal"* y se pisa con
   §17.3.8.3.4 y con §17.3.12 entera. Lo que **sólo ella** sostiene es otra cosa: que la variante de
   estrategia quede registrada en los eventos es lo que hace comparables dos corridas. El nuevo título es
   **"Comparabilidad entre estrategias"** y el cuerpo:

   > *"Para que la comparación entre variantes sea posible, cada evidencia publicada conserva el vínculo con
   > la condición que representa, la estrategia de detección utilizada y la configuración efectiva de la
   > corrida. Una misma condición puede evaluarse con distintas estrategias sin alterar la semántica del
   > sistema, siempre que la corrida declare la variante utilizada y los eventos resultantes conserven esa
   > referencia. Es esa referencia declarada, y no una reinterpretación posterior de los artefactos, la que
   > permite atribuir una diferencia de resultados a la estrategia evaluada y no a un cambio no declarado en
   > la cadena."*

**Resultado:** §17.3.9 pasa de 678 a ~400 palabras, conserva sus tres subsecciones y cada una responde una
pregunta distinta (cómo se traduce · qué se adoptó · por qué se puede comparar).

*Origen: C27 ("ya se dijo antes, no repetir huevadas"), el hilo C28/C29 ("¿la dejamos como constitución o la
borramos?" · "el fabio decide"), C30 y C31 ("esto ya está claro" · "esto también").*

---

### E3-41 · §17.3.10 — la sección no tiene entrada y su primera subsección la suple mal

**Problema.** §17.3.10 *"Distribución de alertas confirmadas"* es la **única sección de §17.3 con cero
palabras propias**: el título va directo a §17.3.10.1. Esa subsección termina haciendo dos trabajos y no hace
bien ninguno. Su arranque —*"La cadena descrita hasta aquí termina en un hecho interno… Falta el último
tramo: hacer llegar esa alerta a un canal externo sin comprometer al motor que la produjo"*— es narrativo,
está fuera del registro del resto del capítulo (*"falta el último tramo"*) y, sobre todo, **no enuncia la
función arquitectónica**, que es exactamente lo que su título promete.

**Acción — dos ediciones.**

1. **§17.3.10 recupera su párrafo de entrada** (dos oraciones, antes de la primera subsección):

   > *"La alerta interna es el hecho terminal del plano de control, pero todavía no es un aviso. Esta sección
   > define el tramo que la convierte en entregas observables sin incorporar la comunicación a la ruta que la
   > produjo."*

2. **§17.3.10.1 arranca por la función**, que es lo que su título anuncia:

   > *"La función arquitectónica de la distribución es transformar una alerta ya confirmada en intentos de
   > entrega registrados, sin participar del razonamiento que la produjo. El plano de control publica cada
   > alerta confirmada en un bus de alertas dedicado; el módulo de distribución la consume desde allí, aplica
   > la política de notificación y registra el resultado de cada intento. No constituye un tercer plano ni un
   > cuarto rol funcional: es un módulo desacoplado, y esa condición es la que impide que la indisponibilidad
   > de un canal externo se propague al motor de patrones."*

Los otros dos párrafos de §17.3.10.1 (pipeline de distribución; política ordinaria) se conservan.

*Origen: C32 ("malísima esta intro").*

---

### E3-42 · §17.3.6.4 — la remisión a §17.1.5.4.2 **es falsa hoy**, y §17.3 debe dejar de depender de ella

**Problema — es el único defecto duro de referencia cruzada del capítulo.** §17.3.6.4 dice:

> *"…se mantienen en conjuntos separados para las estrategias directa (E-DIR) e híbrida (E-HYB) **definidas
> en la consolidación metodológica (sección 17.1.5.4.2)**…"*

Verificado sobre el `.docx` maestro de las secciones cerradas: **`E-DIR`, `E-IND` y `E-HYB` aparecen cero
veces en todo el informe fuera de §17.3 y §17.4.** §17.1.5.4 sí distingue las familias en prosa ("estrategia
directa", 3 apariciones; "estrategia indirecta", 5; "híbrida", 4), pero **no las bautiza con esos códigos**,
y §17.1.5.4.2 se titula *"Estrategia de Variación Sistemática"*, que es otra cosa. La remisión envía al
lector a un lugar donde no está lo que se le promete.

**Por qué no alcanza con lo ya decidido.** El pase 1 previó exactamente esto (decisión D3 y ajuste C-1:
bautizar los tres códigos en §17.1.5.4.2). Pero C-1 es una edición de **etapa 2**, y por D-P3-3 la etapa 2 se
trabaja al final. §17.3 no puede quedar colgada de una edición futura.

**Acción — §17.3 se hace autosuficiente, en tres ediciones.**

1. **§17.3.2 — quitar el código del párrafo de condiciones de riesgo.** Hoy dice *"el flujo base prioriza la
   estrategia indirecta E-IND"*; pasa a *"el flujo base prioriza la estrategia indirecta"*. Motivo: tras la
   enmienda a E3-22 ésa sería la primera aparición del código en el informe, y §17.3.2 no es la sección
   dueña del concepto (D-P3-4).
2. **§17.3.6.4 — acá nacen los tres códigos**, en el párrafo que hoy hace la remisión falsa:

   > *"Las consultas negativas o de estado observable se mantienen en conjuntos separados para las
   > estrategias directa e híbrida ya distinguidas en la consolidación metodológica, de modo que sus
   > resultados sean atribuibles a una estrategia explícita y no a una mezcla informal de vocabularios. En el
   > diseño arquitectónico y en lo que sigue del trabajo, estas familias se identifican mediante un código:
   > estrategia directa (E-DIR), cuando el prompt intenta describir la condición de riesgo completa;
   > estrategia indirecta (E-IND), cuando el detector identifica entidades visibles por separado y la
   > condición se reconstruye mediante lógica externa al modelo; y estrategia híbrida (E-HYB), cuando se
   > combinan consultas de ambos tipos bajo una regla de composición explícita."*

3. **Verificar el orden al aplicar:** con estas dos ediciones, la primera aparición de cualquiera de los tres
   códigos en el informe es la glosa de §17.3.6.4, que **precede** a la Tabla 45 (dentro de la misma
   subsección), a §17.3.9.2, a la Tabla 60 y a §17.3.18. Ninguna aparición queda antes de su definición.

**Qué pasa con C-1 del pase 1.** Deja de ser obligatorio y **pasa a ser armonizador**: si al trabajar la
etapa 2 se aplica el bautismo en §17.1.5.4.2, entonces §17.3.6.4 recorta su glosa a la remisión (*"…para las
estrategias directa (E-DIR) e híbrida (E-HYB) definidas en la consolidación metodológica"*). Si no se aplica,
el informe queda igualmente correcto y autoconsistente. **Se anota en §I como dependencia inversa**, para que
al tocar etapa 2 no se dupliquen las dos glosas.

*Origen: C11 de §17.3 ("tienen que estar definidas. revisar esto en etapa 2").*

---

## C. Correcciones nuevas a §17.4 — Implementación

### E4-27 · §17.4.10, Tabla 68 — la fila de ajuste fino afirma algo **falso hoy**, y su marcador está vencido

**Nadie lo comentó; es un hallazgo de este pase y es el defecto más grave de §17.4.** La celda de estado dice:

> *"…El tramo exploratorio adicional **fue enviado y permanece en cola, sin haber iniciado**."*

y arrastra el marcador *[[PENDIENTE: resultado y veredicto del tramo exploratorio adicional · depende de
completar su ejecución y evaluación predefinidas]]*, más una oración en la Nota de la tabla que lo sostiene
(*"El marcador del tramo exploratorio adicional permanece visible hasta que exista un artefacto evaluado; su
envío y permanencia en cola no constituyen por sí mismos un resultado"*).

**Verificado: la escalera está completa y cerrada.** El tramo adicional dejó de estar en cola, corrió, se
evaluó una sola vez contra el banco congelado y produjo veredicto negativo; y el tercer tramo se cerró con
causa técnica. Los tres puntos de la escalera están cerrados, y el hallazgo de conjunto es más fuerte que
cualquiera de ellos por separado: el límite no es de capacidad del modelo sino **estructural**, porque el
corpus de ajuste disponible es de un orden que no alcanza a sostener el número de parámetros que se ajustan.
La causa técnica del tercer tramo también es declarable sin citar nada del repositorio: el único corpus
histórico de ese volumen **comparte fuentes con el banco de evaluación congelado** y, además, derivaba la
clase de cabeza descubierta de un modo que el vocabulario canónico vigente prohíbe.

**Acción — tres ediciones.**

1. **Reemplazar la celda de estado:**

   > *"Protocolo, procedencia, servicio de inferencia, evaluación y línea base quedaron congelados, y la
   > escalera de tramos pre-registrada se ejecutó completa. Los dos tramos entrenados se evaluaron una única
   > vez contra el banco congelado y ninguno superó los criterios de incorporación, firmados antes de que
   > existiera el checkpoint que se les aplicaría. El tercer tramo se cerró con causa técnica: el único
   > corpus disponible de ese volumen comparte fuentes con el banco de evaluación y deriva la clase de cabeza
   > descubierta de una forma que el vocabulario canónico vigente no admite."*

2. **Reemplazar la celda de consecuencia, eliminando el marcador `[[PENDIENTE]]`:**

   > *"Ningún checkpoint se incorporó como modelo de servicio. El resultado es un veredicto negativo
   > pre-registrado y no un tramo abierto: los criterios y los márgenes se firmaron antes de la evaluación, y
   > las tres expectativas registradas de antemano se confirmaron. Los valores por tramo y la lectura de la
   > curva se informan en la sección 17.5."*

3. **Eliminar de la Nota de la Tabla 68** la oración sobre el marcador. El resto de la Nota se conserva.

⚠ **El otro marcador de §17.4 no se toca.** El `[[PENDIENTE]]` de §17.4.8.1 —dirección de origen y fecha de
acceso por clip del lote de obra real— **sigue vigente y sigue siendo bloqueante para la versión final**. No
se elimina ni se relaja.

---

### E4-28 · §17.4.3 "Contratos de datos materializados" — la sección más densa del capítulo

**Problema.** 197 palabras y tres párrafos para cinco contratos, con estos defectos verificados:

1. **Anuncia cinco y no los enumera.** *"Cinco contratos concentran los hechos principales de la ejecución"*
   y arranca directo con el primero; el lector cuenta hacia atrás para saber cuáles fueron.
2. **La primera oración encadena nueve complementos** (*"…incluye identificación de corrida y unidad visual,
   descripción de la fuente, perfil de modelo, conjunto de prompts, detecciones con coordenadas en píxeles y
   normalizadas, y tiempos por unidad"*). Es un inventario disfrazado de oración.
3. **Reparto desparejo:** dos contratos en el primer párrafo, tres apretados en el segundo.
4. **Las propiedades técnicas —que son el aporte de la sección— quedan escondidas** al final de subordinadas:
   la secuencia monótona que vuelve detectable el hueco, el identificador determinista que permite deduplicar
   sin estado compartido, la evidencia que hace reconstruible la ausencia.

**Cuál es el propósito que sólo esta sección tiene** (D-P3-1): la Tabla 63 de §17.4.2 ya da la
correspondencia diseño → materialización, y §17.3.11.3 ya dio la información mínima de cada contrato. Lo que
falta y sólo acá cabe es **qué propiedad técnica habilita cada contrato materializado**. La reorganización se
hace alrededor de eso.

**Acción — cuatro párrafos, uno por función, cada uno cerrando en su propiedad.** Texto guía:

> *"Cinco contratos concentran los hechos principales de la ejecución: el evento de percepción, el envoltorio
> del bus, el contrato de ciclo de vida, el evento de transición de patrón y la alerta interna. Los cinco
> están declarados con su identificador en la tabla anterior; lo que sigue precisa qué lleva cada uno y qué
> propiedad técnica habilita."*
>
> *"El evento de percepción normaliza la salida del detector. Identifica la corrida y la unidad visual;
> describe la fuente, el perfil de modelo y el conjunto de prompts efectivos; y transporta las detecciones
> con sus coordenadas en píxeles y normalizadas, sus puntajes y los tiempos medidos por unidad. Esa
> composición es la que permite que una detección se atribuya después a una variable concreta de la corrida y
> no a una combinación desconocida."*
>
> *"El envoltorio del bus encapsula ese mismo contenido para transmitirlo y le agrega un número de secuencia
> monótono; el contrato de ciclo de vida delimita el inicio y el cierre de la corrida. Juntos habilitan dos
> propiedades que la persistencia sola no da: cualquier pérdida en el transporte se vuelve detectable como un
> hueco de secuencia en lugar de pasar por ausencia de evidencia, y el final lógico de la corrida se
> distingue de una interrupción, de modo que los consumidores puedan cerrarse y los artefactos consolidarse."*
>
> *"El evento de transición registra los cambios entre los estados del patrón —los mismos que fija la máquina
> de estados del diseño— junto con la evidencia y los hitos temporales que los motivaron; la alerta interna
> registra la confirmación del episodio con un identificador determinista, de modo que reprocesar la misma
> corrida produzca la misma identidad de alerta y la deduplicación no requiera estado compartido entre
> componentes. La alerta conserva además evidencia auditable: sujeto observado, detecciones de soporte, clase
> de protección ausente, región evaluada, puntaje y justificación legible. Por eso la ausencia no se presenta
> como una afirmación opaca del detector, sino como una inferencia del plano de control reconstruible sobre
> evidencia positiva."*

⚠ **Respeta E4-24 y D-P2-6:** ningún identificador literal aparece en esta prosa; los cinco quedan declarados
en la Tabla 63, que es su único punto de declaración. La referencia a la figura de la máquina de estados se
mantiene descriptiva, como pide la enmienda a E3-28.

*Origen: C0 de §17.4 ("difícil de leer, hay que mejorar la organización del desarrollo de esta sección").*

---

### E4-29 · §17.4.7 — el árbol de artefactos no muestra la plataforma completa

**Problema.** El árbol de la ejecución experimental lista `manifest.effective.yaml`, `media/`, `control/` y
`report/`, y deja la distribución fuera, en una oración suelta al pie: *"Cuando el tramo de distribución está
habilitado, su ledger y su reporte se consolidan del mismo modo."* Pero **esta es justamente la sección donde
se muestra cómo se consolida la evidencia de una corrida**: dejar un componente fuera del árbol sugiere que
se consolida distinto, cuando el argumento es el contrario. La condicionalidad es correcta —la plataforma es
modular y un tramo puede no estar habilitado—, pero ya hay una forma en el propio árbol de expresarla: dentro
de `control/` la evaluación temporal aparece con su condición entre paréntesis.

Defecto asociado, misma sección: la fila *Distribución* de la **Tabla 66** es la única de las cuatro que **no
nombra archivos** (*"Ledger de intentos y entregas; resultados de canal; reporte de distribución"*), mientras
las otras tres los nombran uno por uno. Verificado contra el módulo: los artefactos reales son
`notifications.jsonl` —el ledger de sólo agregado—, `distribution_summary.json` y `dead_letter.jsonl`, este
último el registro de los descartes definitivos por agotamiento de reintentos. **No** produce
`effective_config.yaml` por corrida: expone su configuración efectiva por interfaz, y esa asimetría con los
dos planos no debe insinuarse resuelta.

**Acción — tres ediciones.**

1. **Incorporar la distribución al árbol**, con su condición entre paréntesis, igual que la evaluación temporal:

   ```
   runs/<experiment_id>/                (repositorio del soporte experimental)
     manifest.effective.yaml
     media/           summary.json · metrics.jsonl · effective_config.yaml ·
                      detections.ref.json  (referencia al detections.jsonl del plano de medios)
     control/         alerts.jsonl · pattern_events.jsonl · metrics.jsonl ·
                      summary.json · effective_config.yaml
                      (y la evaluación temporal, cuando la corrida la habilita)
     distribution/    notifications.jsonl · distribution_summary.json · dead_letter.jsonl
                      (cuando la corrida habilita el tramo de distribución)
     report/          report.json · report.md
   ```

2. **Reemplazar la oración suelta** por una que cierre el argumento en lugar de excusarlo:

   > *"La ejecución experimental consolida así los cuatro componentes bajo una misma clave. La modularidad de
   > la plataforma se expresa en que un tramo pueda no estar habilitado, no en que su evidencia se consolide
   > de otro modo cuando lo está."*

3. **Tabla 66, fila *Distribución* — nombrar los artefactos** como en las otras tres filas:

   > *"notifications.jsonl (ledger de intentos y entregas, de sólo agregado); dead_letter.jsonl;
   > distribution_summary.json"* || *"Relaciona cada intento y resultado de entrega con la alerta interna
   > original sin reescribirla, y conserva por separado los descartes definitivos por agotamiento de
   > reintentos."*

*Origen: C2 de §17.4 ("agregar el módulo de distribución… la idea es mostrar la plataforma como un todo, y
más en esta parte que se habla de la consolidación de la evidencia de las corridas").*

---

### E4-30 · `PUB/SUB` en §17.4 — alinear con la normalización de E3-33 (✎ agregada el mismo día)

**Problema — desalineado entre secciones detectado en la verificación cruzada (§I).** E3-33 (b) alinea
§17.3 a la forma que el propio informe ya normalizó: **publicador-suscriptor** (§17.3.5, §17.3.18). Pero
§17.4 usa `PUB/SUB` crudo **cuatro veces**, y ninguna unidad lo tocaba. Aplicar E3-33 sin esto dejaría a
las dos secciones en formas distintas del mismo término — exactamente el defecto que D-P3-5 (b) corrige.

**Acción — tres ediciones (la cuarta aparición desaparece sola con E4-20, que elimina la Tabla 65):**

1. **Nota de la figura de §17.4.1** (*"…mediante buses ZeroMQ PUB/SUB con serialización msgpack…"*) →
   *"…mediante buses ZeroMQ de patrón publicador-suscriptor con serialización msgpack…"*.
2. **Tabla 64, fila del canal de detecciones:** celda de operación *"ZeroMQ PUB/SUB + msgpack"* →
   **"Bus ZeroMQ publicador-suscriptor (msgpack)"**.
3. **Tabla 64, fila del canal de alertas:** ídem.

**Verificación al aplicar:** `PUB/SUB` queda en **cero** apariciones en §17.4 (y en las dos que E3-33
conserva glosadas en §17.3 si las hubiera — el conteo final del par es el de E3-33).

---

## D. §17.5 — restricciones que este pase deja fijadas (no es corrección: §17.5 no está redactada)

Por D-P3-3 la etapa 5 entra en alcance. Como no hay texto que corregir, lo que se fija es el terreno, para
que §17.5 no repita §17.3/§17.4 ni contradiga lo que este pase acaba de resolver.

### D.0 — La organización de la sección (aplica D-P3-6; ✎ decisión del usuario, 2026-08-22)

**La sección se organiza por pregunta de medición, no por cronología.** El modelo estructural es el de la
síntesis de resultados vigente (pregunta → niveles de medición → tiempo real → caminos → limitaciones), que
ya demostró sostener el argumento sin narrar campañas. Esquema de referencia — los títulos definitivos los
fija la redacción, la **secuencia y el reparto** son lo decidido:

1. **Encuadre y reglas de lectura.** La pregunta de la sección, los **tres niveles de medición** (percepción
   por imagen · estado por sujeto · alerta por episodio), los estados de aplicabilidad, y de dónde sale cada
   cifra. Acá viven las reglas transversales: reportar por estrato además del agregado, no sumar percentiles
   entre tramos, re-alertas no son falsos positivos.
2. **Percepción sobre imágenes.** El banco de imágenes congelado: resultados **por modelo y por familia**,
   por estrato, con veredictos **por combinación** (rige E4-26: prohibida la fórmula "el mejor modelo"; la
   selección del perfil operativo se enuncia como criterio pre-registrado). Cierra con el costo medido de
   incorporar vocabulario nuevo (el piloto de clase nueva).
3. **Estado por sujeto (nivel intermedio).** La comparación de estrategias de detección sobre el estado
   "sin protección" por persona: la indirecta adoptada, la directa y la híbrida como ramas comparativas —
   los resultados que fundamentan el veredicto van acá, no en la narración de campañas.
4. **Alerta por episodio contra la referencia temporal humana — el resultado principal.** El banco temporal
   completo (47 clips: 32 positivos + 15 negativos), por estrato y por condición; la granularidad por
   sujeto como capacidad medida; la tasa de falsos positivos por hora (se reporta, no sostiene cota); la
   frontera de juzgabilidad del material de obra real (sin ranking sobre n = 2).
5. **Tiempo real.** Qué sobrevive a la restricción del camino en vivo: el costo de la densidad de
   procesamiento, la cadena de latencias **por tramos** (con la regla de relojes), y la latencia del tramo
   de distribución con su denominador.
6. **Caminos probados y no adoptados — con el veredicto que los descartó.** Una subsección propia, no notas
   dispersas: la estrategia directa (vetada por precisión), la híbrida (una variante ejecutada y refutada,
   una no ejecutable), la familia de modelos descartada en la comparación, y la **rama de ajuste fino como
   curva de capacidad de tres puntos** (dos veredictos negativos pre-registrados + un tramo cerrado con
   causa técnica; rige el punto 4 de abajo). El criterio de cada descarte precede al resultado que lo aplicó.
7. **Lo no ejecutado y lo no implementado — con su factor de justificación.** También subsección propia:
   condiciones de Nivel 2/3 (evaluabilidad: sin verdad de terreno ni evaluadores validables), métricas MOT
   (sin anotación de identidad), preselección en el borde (implementada y medida, excluida de lo evaluativo
   por decisión pre-registrada — rige la enmienda a E4-22), cota operativa de FAR (exposición insuficiente),
   y el ancla temporal para comparar EBE-desde-clip. Cada ítem con su justificación, nunca como lista de
   faltantes.
8. **Síntesis de la sección.** Qué queda afirmado con qué fuerza, y la remisión a las limitaciones
   declaradas. La **interpretación** (qué significa para la pregunta de la tesis) no vive acá: pertenece a
   las conclusiones.

**Reparto con las secciones vecinas, para no volver a pisarse:** §17.4 acredita que las capacidades
funcionan (verificación técnica); §17.5 reporta **cuánto dan** (medición); §18 dice **qué significa**
(interpretación y conclusiones). Un contenido que acredite funcionamiento no se repite en §17.5; un juicio
de valor no se adelanta desde §18.

### Restricciones puntuales

1. **Lo que §17.5 no vuelve a explicar.** La arquitectura, los contratos, los patrones de acople, los
   artefactos por corrida y el criterio de aplicabilidad de métricas ya están en §17.3 y §17.4. §17.5 los
   **usa**; no los reintroduce. Si un resultado necesita una condición de medición, se enuncia en una oración
   y se remite a la sección que la fijó.
2. **Herencia de E4-26 — no hay "mejor modelo".** Los resultados se presentan por modelo y por familia; la
   selección se enuncia como criterio operativo con base pre-registrada, y el veredicto es **por combinación**
   (un perfil puede ganar en precisión y otro en exhaustividad de una condición). Está prohibida la fórmula
   "el mejor modelo".
3. **Herencia de la enmienda a E4-22 — el 87 % de la preselección.** Si §17.5 lo cita, va con su denominador
   y su condición de medición, y aclarando que la capacidad estuvo deshabilitada en todo lo evaluativo. Si no
   lo cita, la celda de la Tabla 68 es su único lugar en el informe.
4. **Herencia de E4-27 — la rama de ajuste fino cierra en §17.5.** Los tres tramos y su lectura de conjunto
   (el límite es estructural, no de capacidad) se informan acá, con los márgenes firmados de antemano. Ningún
   pasaje del informe puede seguir describiendo el tramo adicional como pendiente.
5. **Las tres piezas de "listo para pegar" con contenido vencido** que ya identificó la revisión de cierre
   —la fila de ajuste fino que dice que resta la corrida (resuelta acá por **E4-27**), el identificador de un
   clip retirado del banco, y el redline de alcance sin anclar a su unidad— **se revisan antes de pegar
   §17.5**, no después.
6. **Criterio de tablas heredado.** Rige D-P2-1 y el resultado de la revisión de cierre para §17.5: siete
   tablas, seis a prosa, tres al Anexo D, una eliminada; y la tabla principal baja de trece a ocho columnas.
   Con los tres pases aplicados, **§17.5 arranca en la Tabla 61** (ver §G).
7. **Autocontención.** Igual que en §17.3 y §17.4: sin referencias a documentos del repositorio, decisiones
   internas, fichas ni índices. Las referencias a otras secciones del informe sí valen.

---

## E. Hechos verificados en este pase — NO "corregir" estos valores

| Hecho | Valor verificado | Cómo se re-verifica |
| --- | --- | --- |
| Peso de las dos secciones | §17.3 = **20.622** palabras · §17.4 = **5.477** (cuerpo extraído, sin el banner de la extracción) | `herramientas/extraer_informe.py` sobre cada `.docx`, después `wc -w` descartando el bloque anterior al primer `---` |
| Comentarios traídos | **40** en **29 hilos**: 37 en §17.3, 3 en §17.4 | `word/comments.xml` + `word/commentsExtended.xml` (hilos por `paraIdParent`) |
| CPN/EN/TN definidos en etapa 2 | §17.1.4.2 y sus tres sub-apartados | búsqueda de `CPN` en `entregable/96b-…-17-1-…md` |
| `E-DIR`/`E-IND`/`E-HYB` en secciones cerradas | **cero apariciones** | búsqueda sobre el XML de `entregable/E-OVRT-VDP_v1.1_05062026-sin-etapa3.docx` |
| Siglas de métricas definidas en etapa 2 | `t_alert-system` §17.1.7.5.1 (como ecuación OMML) · `TTFD` §17.1.7.5.2 · `SDR` §17.1.7.5.3 | ídem; la sigla de latencia **no** aparece en extracciones planas |
| Preselección en el borde: implementada | sólo para la cámara propia; deshabilitada por defecto; degradación segura con latido y apertura ante silencio | esquema de configuración del plano de medios (`config/schemas.py`) y la fuente del dispositivo |
| Preselección: efecto medido | **87 %** de unidades descartadas en el dispositivo, comparación pareada contra el flujo completo | registro de relevamiento de plataforma |
| Preselección: apagada en lo evaluativo | decisión previa a los resultados, con dos causas declaradas | registro de decisiones del banco en tiempo real |
| Ajuste fino: escalera completa | dos tramos entrenados y evaluados (ambos negativos) + tercero cerrado con causa técnica | cierres de jornada de los tres tramos |
| Artefactos del módulo de distribución | `notifications.jsonl`, `distribution_summary.json`, `dead_letter.jsonl`; **no** escribe `effective_config.yaml` por corrida | `out_dir / "…"` en `eovrt_distribution` |
| Valores del núcleo referenciados desde §17.3 | §17.4.6 **sí** los documenta (4.000/7.000 ms, 0,35, 400 px², 0,25, regiones 0–45 % y 25–85 %) | §17.4.6, primer párrafo |

---

## F. Mapa comentario → unidad — los 29 hilos, ninguno sin destino

**§17.3 (26 hilos)**

| Hilo | Sección | Destino |
| --- | --- | --- |
| C0 (+C1, C2, C3, C4) | 17.3.2 | **enmienda a E3-22** (§A) |
| C5 | 17.3.2 | **E3-33** (a) |
| C6 | 17.3.2 | **E3-33** (a) |
| C7 | 17.3.2 | **E3-34** |
| C8 (+C9) | 17.3.3.2 | **E3-21** (pase 2) fusiona las Tablas 40 y 41 — resuelve la duplicación medible. Lo que Gabriel además insinúa (que §17.3.3.1 y §17.3.3.2 comparten terreno en prosa) queda **diferido a la etapa 2** por decisión tuya en el hilo ("cuando se termine ahí vemos cómo enganchamos"). Ver §H. |
| C10 | 17.3.5 | **checkpoint de cierre, no unidad.** Dos de las siete figuras están producidas (la vista de procesos de §17.4.1 y la máquina de estados de §17.3.8.2, PNG 300 dpi y SVG, ancho 16 cm). Las cinco restantes de §17.3 son las tuyas y entran en el pase final de figuras. Ver §H. |
| C11 | 17.3.6.4 | **E3-42** |
| C12 (+C13, C14) | 17.3.6.6 | **E3-20** (pase 2) — sin cambios; es tu propio texto |
| C15 | 17.3.6.7 | **E3-35** |
| C16 (+C17) | 17.3.7.3 | **E3-28 + enmienda** (pase 2) — sin cambios |
| C18 | 17.3.7.4 | **E3-36** |
| C19 | 17.3.7.4 | **E3-36** |
| C20 | 17.3.7.5 | **enmienda a E4-22** (§A) |
| C21 | 17.3.7.5 | **E3-37** |
| C22 | 17.3.7.5 | **E3-37** |
| C23 | 17.3.8.2 | **verificado, sin cambio.** §17.4.6 sí documenta los valores del núcleo. La sección se retitula por E4-26 (*"…y catálogo de modelos"*) pero **no cambia de número**, así que la remisión sigue siendo válida. |
| C24 | 17.3.8.3.1 | **E3-38** |
| C25 | 17.3.8.3.1 | ídem C23 — verificado, sin cambio |
| C26 | 17.3.8.3.4 | **E3-39** |
| C27 | 17.3.9.1 | **E3-40** (1) |
| C28 (+C29) | 17.3.9.2 | **E3-40** (2) — decisión tomada: se conserva podada |
| C30 | 17.3.9.3 | **E3-40** (3) |
| C31 | 17.3.9.3 | **E3-40** (3) |
| C32 | 17.3.10.1 | **E3-41** |
| C33 (+C34) | 17.3.11.1 | **E3-30** (pase 2) — sin cambios; es tu propio texto |
| C35 (+C36) | 17.3.15 | **E3-34** (2) |

**§17.4 (3 hilos)**

| Hilo | Sección | Destino |
| --- | --- | --- |
| C0 | 17.4.3 | **E4-28** |
| C1 | 17.4.4 | **E4-25** (pase 2) — cubierto entero: propósito por endpoint, la asimetría de detención declarada y el orden de disparo derivado |
| C2 | 17.4.7 | **E4-29** |

**Sin comentario asociado, hallazgos de este pase:** **E4-27** (la fila de ajuste fino afirma algo falso),
**E3-33 (b) y (c)** (los anglicismos inconsistentes más allá de los dos marcados), y los dos defectos del kit
anotados en la cabecera.

---

## G. Numeración resultante, con los tres pases aplicados

**Subsecciones de §17.3**

| Cambio | Unidad | Efecto |
| --- | --- | --- |
| §17.3.6.6 eliminada | E3-20 (pase 2) | 6.7 → 6.6 |
| §17.3.6.6 (ex 6.7) eliminada | **E3-35** | §17.3.6 queda con **6.1 a 6.5** |
| §17.3.7.4 eliminada | **E3-36** | 7.5 → **7.4**; §17.3.7 queda con **7.1 a 7.4** |
| §17.3.9.3 retitulada | **E3-40** (3) | mismo número, nuevo título *"Comparabilidad entre estrategias"* |
| §17.3.11.1 eliminada | E3-30 (pase 2) | 11.2 → 11.1, 11.3 → 11.2, 11.4 → 11.3 |
| §17.3.14.2 retitulada | **E3-33** (a) | *"EBE como escenario de fuente en vivo controlada"* |

⚠ **Dependencia cruzada a respetar al aplicar:** la acción 3 de la enmienda a E3-28 apunta a "§17.3.7.5"; tras
E3-36 esa subsección es **§17.3.7.4**. Es la misma unidad (*"Capacidades opcionales sin desplazar el núcleo
validable"*) y sigue siendo donde nace `fail-open`.

**Tablas.** Este pase elimina **una** tabla más que el pase 2: la **Tabla 39**, que E3-22 ya sacaba —la
enmienda no cambia el conteo, sólo qué la reemplaza—. Las Tablas 64, 66, 68 y 69 reciben ediciones de celda o
de fila, no cambian de posición. ✎ **Mapa computado (2026-08-23; segunda corrección el mismo día — al aplicarse E3-27 la
Tabla 46 pasó a viñetas, así que §17.3 pierde SIETE tablas, no seis):** §17.3 pierde 39, 40, 46, 49, 51,
61 y 62, y queda con **17 = Tablas 39–55** (41→39, 42→40, 43→41, 44→42, 45→43, 47→44, 48→45, 50→46,
52→47, 53→48, 54→49, 55→50, 56→51, 57→52, 58→53, 59→54, 60→55); §17.4 pierde la 65 y queda con **6 =
Tablas 56–61** (63→56, 64→57, 66→58, 67→59, 68→60, 69→61); **§17.5 arranca en la Tabla 62**. ⚠ El mapa
vale si las opcionales C-01 a C-04 del pase 2 **no** se aplican (siguen sin decidirse); si alguna se
aplica, se recorre desde su posición.

---

## H. Verificación cruzada de alineación entre §17.3 y §17.4 (✎ 2026-08-22, directiva del usuario)

Cada tema que cruza la frontera diseño → implementación, con la unidad que lo fija de cada lado y el estado
verificado. **Esta tabla es la prueba de que las correcciones de ambas etapas no se contradicen**; si una
unidad futura toca uno de estos temas, tiene que actualizar la fila.

| Tema compartido | Lado §17.3 | Lado §17.4 | Verificado |
| --- | --- | --- | --- |
| Identificadores versionados (`.vN`, literales) | E3-31 (cero en §17.3) bajo D-P2-5 | E4-23 + E4-24 (Tabla 63 único punto de declaración; 1 glosa) bajo D-P2-6 | ✅ contrapartes explícitas; la fila *Cierre de corrida* de E4-24 recibe lo que E3-31 suelta |
| `fail-open` / `opt-in` | E3-28 + enmienda: nace y se glosa en "Capacidades opcionales…" (§17.3.7.4 tras E3-36); `opt-in` erradicado | Enmienda a E4-22: la fila de la Tabla 68 dice **"criterio de degradación segura"** — usa el término ya definido, no lo redefine | ✅ definición precede a todo uso |
| Preselección en el borde | Huella declarativa: DA-11, §17.3.7.4, §17.3.14.5, Tablas 57/58/59 | Enmienda a E4-22: implementada y medida (87 %), excluida de lo evaluativo con causa pre-registrada | ✅ el diseño la declara, la implementación rinde cuentas |
| Rama de ajuste fino | DA-07 y fila "Adaptación al dominio" (E3-21): condiciones de la rama (línea base congelada, partición disjunta, criterios previos) | E4-27: jornada completa, tres tramos cerrados, sin marcador | ✅ las condiciones del diseño son exactamente las que la jornada cumplió (pre-registración) |
| Duplicación DA-03 ↔ patrones de acople | E3-19 (la celda de DA-03 deja de enumerar tecnologías) | E4-20 (Tabla 65 eliminada: era el duplicado) | ✅ el par se resolvió de los dos lados |
| Anglicismos ya normalizados | E3-33 (a)(b)(c) — con lista cerrada de lo que NO se toca | **E4-30** — las 3 apariciones sobrevivientes de `PUB/SUB` | ✅ misma forma en ambas secciones |
| Códigos E-DIR / E-IND / E-HYB | E3-42: nacen glosados en §17.3.6.4 | §17.4.10 (Tabla 68) los usa después de esa definición | ✅ orden definición → uso verificado; §17.5 los hereda (D.0) |
| Valores efectivos del núcleo | §17.3.8.2 y Tabla 46 remiten a §17.4.6 (verificado en C23/C25) | E4-26 retitula §17.4.6 **sin cambiar su número** | ✅ la remisión sigue válida |
| Máquina de estados (FIG-E) | Vive en §17.3.8.2 (D2, excepción declarada) | §17.4.3 la referencia sin repetirla (texto guía de E4-28 mantiene la referencia descriptiva) | ✅ una sola figura, un solo dueño |
| Consolidación de evidencia por corrida | §17.3.10.2 / Tabla 48 (consumidores) y §17.3.12.1 (repositorio por `experiment_id`) | E4-29: `distribution/` entra al árbol con su condición entre paréntesis | ✅ el árbol muestra los cuatro componentes que el diseño promete |
| Cierre de corrida (`run_finished`) | §17.3.8.4 lo enuncia en abstracto (E3-31 suelta el literal) | Tabla 63, fila nueva de E4-24, lo declara | ✅ sin huérfanos |

---

## I. Diferidos y dependencias inversas

| Ítem | Por qué se difiere | Cuándo se retoma |
| --- | --- | --- |
| **C-1 del pase 1** — bautizar E-DIR/E-IND/E-HYB en §17.1.5.4.2 | Es edición de etapa 2, y **E3-42** ya dejó §17.3 autosuficiente | Al trabajar etapa 2. **Dependencia inversa:** si se aplica, hay que recortar la glosa de §17.3.6.4 a una remisión, o el informe la dirá dos veces |
| **Solape §17.3.3.1 ↔ §17.3.3.2 en prosa** (hilo C8/C9) | Depende de qué quede en §17.1 tras la etapa 2 | Al cerrar etapa 2, con E3-21 ya aplicada |
| **Pase de figuras** (C10) | Las cinco figuras de §17.3 son originales del autor | Pase final de figuras, junto con la inserción de las dos producidas |
| **`[[PENDIENTE]]` de §17.4.8.1** — origen y fecha de acceso por clip del lote de obra real | Insumo del usuario, sigue abierto | **Bloqueante para la versión final**; no se relaja |
| **Unidades opcionales C-01 a C-04 del pase 2** | Decisión no tomada | Antes de fijar la numeración final de tablas (§G) |
| **Anomalía observada en §17.1.7.5.1** (fuera de alcance) | La sigla de la latencia de alerta viaja como ecuación de Word y desaparece en toda extracción plana: los títulos quedan como *"Latencia de Alerta ()"* | Al trabajar etapa 2, verificar que la sigla se lea bien en el `.docx` final y no sólo en pantalla |

---

## Fuente: `docs/informe/entregable/90-etapa3-texto-extraido.md`

> SHA-256 del bloque: `644e246b50406582ab036ef4c023563114d21b2094aec175633ee7e3fbf4eebf`  
> Seleccion: TEXTO BASE VIGENTE de la seccion 17.3: extraido del documento de trabajo v1.4 (2026-08-23), con los tres pases YA aplicados y verificados. Es el texto sobre el que se revisa y se sigue trabajando.

# 90 — Texto extraído del documento de trabajo: §17.3 Diseño Arquitectónico (v1.4)

> **Extracción derivada (2026-08-23)** del `.docx`
> `informe/entregable/E-OVRT-VDP_Seccion_17.3_Diseno_Arquitectonico_v1.4.docx`, **solo para búsqueda y cita**
> (mismo estatuto que el doc 90): al editar, se edita el `.docx`/Google Docs, nunca
> este archivo. Tablas y figuras pueden haber perdido formato; las figuras no se
> extraen y las ecuaciones no se convierten — quedan `⟦FIGURA: no extraída — ver el .docx⟧` y
> `⟦ECUACIÓN: no extraída — ver el .docx⟧` donde estaban. Regenerado con
> `herramientas/extraer_informe.py` (regla D-C del manual de aplicación).

---

#### 17.3.1. Introducción y propósito del capítulo

El presente capítulo desarrolla el diseño arquitectónico de la plataforma experimental E-OVRT-VDP, tomando como punto de partida el alcance metodológico, las condiciones de riesgo, los escenarios de evaluación y las métricas definidas en las secciones anteriores. Su propósito es transformar esas definiciones en una organización técnica capaz de orientar la implementación de la plataforma experimental, manteniendo coherencia con los criterios de modularidad, trazabilidad, medición y control de alcance ya establecidos.

La arquitectura se estructura alrededor de una separación entre el procesamiento visual en tiempo real y la lógica de interpretación posterior. Para ello, se distinguen dos planos principales: el plano de medios, encargado de la ingesta, normalización, inferencia y publicación de resultados perceptivos; y el plano de control, responsable de evaluar patrones de riesgo, registrar alertas asistivas, conservar eventos y producir evidencia reconstruible. Esta división permite proteger la ruta crítica de vídeo y, al mismo tiempo, sostener la trazabilidad experimental necesaria para analizar cada corrida.

El capítulo describe las responsabilidades de los componentes principales, los flujos de información, las fronteras entre módulos, los contratos versionados, las interfaces de gobierno y transporte, los escenarios experimentales DBE y EBE, y los criterios de observabilidad que deberán acompañar la implementación. Su finalidad es consolidar una base arquitectónica que permita materializar el prototipo experimental de manera incremental, medible y trazable dentro del alcance experimental definido.

La pregunta que orienta el capítulo puede sintetizarse del siguiente modo: ¿qué arquitectura permite materializar una plataforma experimental de detección open-vocabulary en video en tiempo real, manteniendo modularidad, desacoplamiento, trazabilidad y evaluabilidad dentro del alcance metodológico ya definido?

#### 17.3.2. Insumos metodológicos y decisiones derivadas

La arquitectura propuesta se deriva de las definiciones metodológicas ya consolidadas: el alcance experimental del prototipo, el catálogo de condiciones de riesgo, los escenarios de evaluación, los roles funcionales del entorno, el marco de métricas y los lineamientos ético-legales actúan como restricciones de diseño. Lo que sigue no reitera el protocolo experimental: explicita qué consecuencia arquitectónica se deriva de cada uno de esos insumos, de modo que ningún módulo, frontera o flujo del sistema aparezca como una decisión aislada.

La arquitectura propuesta se deriva de las definiciones metodológicas consolidadas en las secciones anteriores. El alcance experimental, las condiciones de riesgo seleccionadas, los escenarios de evaluación, los roles funcionales del entorno, el framework de métricas y los lineamientos ético-legales actúan como restricciones de diseño. En consecuencia, los módulos, las fronteras y los flujos del sistema no se establecen como decisiones aisladas, sino como una traducción técnica de las condiciones necesarias para sostener la evaluabilidad, la trazabilidad y el control de alcance del prototipo.

El marco teórico de detección open-vocabulary, seguimiento temporal y procesamiento continuo de vídeo exige integrar percepción visión-lenguaje, tratamiento de fuentes audiovisuales y persistencia temporal cuando la condición evaluada lo requiera. De esta exigencia se deriva una arquitectura modular, con separación entre el plano de medios y el plano de control, una ruta crítica instrumentable y modelos sustituibles mediante adaptadores. La inferencia queda así desacoplada de la interpretación temporal, de modo que la incorporación o sustitución de un modelo no obligue a redefinir el resto de la cadena.

El núcleo validable se concentra en CR-01 y CR-02. Ambas condiciones se evalúan mediante evidencia positiva de persona y elementos de protección personal, seguida de una inferencia espacial de ausencia y de su estabilización temporal. Por esta razón, el flujo base prioriza la estrategia indirecta y comprende detección de entidades, asociación espacial por sujeto, evaluación de regiones relevantes y confirmación temporal del patrón. Las zonas externas, las relaciones contextuales complejas y las métricas formales de seguimiento multiobjeto se conservan como capacidades extensibles, pero no se convierten en dependencias del núcleo.

La coexistencia de los escenarios DBE y EBE introduce requisitos temporales diferentes. Las fuentes basadas en archivos pueden regular su ritmo de lectura, repetirse y detenerse sin alterar el contenido observado; las fuentes en vivo, en cambio, continúan evolucionando aunque el procesamiento no alcance la cadencia de captura. La arquitectura abstrae ambos tipos de fuente mediante contratos comunes, pero distingue para cada uno las políticas de reproducibilidad, actualidad, omisión, descarte y trazabilidad temporal. Esta separación permite compartir el pipeline sin ocultar las diferencias que afectan la interpretación experimental de cada corrida.

De los roles funcionales ya establecidos se deriva una restricción de diseño y no una nueva definición: se adoptan como responsabilidades de referencia que permiten declarar dónde se captura, dónde se ejecuta la inferencia y dónde se prepara una variante ajustada, sin que la distribución física de componentes pase a formar parte de la semántica de los contratos.

Finalmente, el framework de métricas y los lineamientos ético-legales condicionan la observabilidad y la persistencia desde el diseño. Cada corrida debe registrar su configuración efectiva, marcas de tiempo por tramo, métricas técnicas, eventos reconstruibles, descartes y errores, de manera que una alerta pueda vincularse con la evidencia que la produjo. Al mismo tiempo, el carácter asistivo del prototipo, la exclusión del reconocimiento de identidad personal y el criterio de minimización visual orientan la trazabilidad ordinaria hacia eventos, metadatos y referencias controladas. La conservación de clips, capturas o recortes queda limitada a los casos justificados por validación, auditoría técnica o comunicación académica.

#### 17.3.3. Alcance, requisitos y decisiones arquitectónicas iniciales

El diseño arquitectónico se formula para un prototipo experimental ejecutado en un entorno local y controlado. En consecuencia, la arquitectura debe orientar la implementación, la medición y la reconstrucción de resultados sin asumir responsabilidades propias de una solución productiva. La sección delimita el alcance efectivo del núcleo validable, las extensiones previstas, las capacidades requeridas, las cualidades no funcionales relevantes y las decisiones iniciales que deberán conservarse durante el desarrollo del prototipo experimental.

##### 17.3.3.1. Alcance del núcleo y extensiones

El alcance arquitectónico se organiza alrededor del núcleo validable definido en la consolidación metodológica. Sobre ese núcleo, la plataforma debe demostrar un flujo completo, medible y trazable desde una fuente visual hasta una alerta asistiva registrada. El objetivo no es ampliar prematuramente la cantidad de condiciones cubiertas, sino asegurar una base suficientemente sólida para procesar evidencia visual, publicar eventos, evaluar patrones, registrar alertas y reconstruir resultados experimentales.

El núcleo incluye las capacidades necesarias para operar sobre fuentes controladas, ejecutar inferencia open-vocabulary, versionar prompts, normalizar detecciones, aplicar reglas temporales simples, registrar eventos y producir métricas comparables. Las capacidades de mayor complejidad —seguimiento multiobjeto formal, reglas espaciales, zonas parametrizadas, preselección liviana en borde o adaptación al dominio— quedan previstas como extensiones condicionadas, siempre que no desplacen la validación inicial ni agreguen dependencias innecesarias al flujo base.

La inclusión de la gestión de prompts dentro del núcleo responde a la naturaleza open-vocabulary de la plataforma: cada resultado debe poder asociarse con una formulación, una estrategia de detección y un vocabulario activo registrados. Del mismo modo, la separación entre DBE y EBE permite distinguir la evaluación reproducible de la validación con captura continua, evitando mezclar variabilidad de cámara, iluminación, códec o red con el desempeño propio del detector.

En relación con la evidencia visual, el diseño retoma los criterios ya definidos de minimización, uso asistivo y ausencia de reconocimiento de identidad. La trazabilidad ordinaria se apoya en eventos, metadatos, identificadores, métricas y referencias controladas. Los clips, snapshots o recortes anotados sólo se consideran artefactos complementarios cuando resulten necesarios para validación, revisión técnica o defensa académica.

##### 17.3.3.2. Capacidades arquitectónicas requeridas

A partir del alcance definido, la arquitectura debe habilitar un conjunto mínimo de capacidades que permitan desarrollar un prototipo experimental medible, trazable y extensible. Estas capacidades no describen todavía componentes de implementación, sino responsabilidades que el diseño debe contemplar para que el sistema pueda procesar fuentes visuales, ejecutar inferencia open-vocabulary, evaluar patrones, registrar alertas y producir evidencia experimental.

La clasificación distingue capacidades del núcleo, capacidades asociadas a la evaluación controlada, capacidades complementarias previstas, extensiones condicionadas y ramas comparativas. Esta separación permite ordenar el desarrollo sin convertir funcionalidades deseables en dependencias obligatorias del flujo base.

**Tabla 39**

*Capacidades arquitectónicas y su tratamiento en el diseño*

| **Capacidad requerida** | **Compromiso** | **Lectura de diseño** |
| --- | --- | --- |
| Gestión de corrida reproducible | Núcleo | Cada ejecución debe asociarse a una configuración explícita de fuente, modelo, prompts, umbrales, entorno y versiones. |
| Procesamiento DBE | Núcleo de evaluación | Debe operar sobre imágenes, datasets o videos locales para estabilizar inferencia, contratos, eventos y métricas bajo condiciones reproducibles. |
| Procesamiento EBE | Complementario previsto | Debe admitir captura o streaming en entorno controlado para observar el comportamiento operativo del sistema. |
| Normalización de entrada visual | Núcleo | Cada frame debe representarse con metadatos de corrida, fuente, orden temporal, resolución y política de muestreo. |
| Inferencia OVD configurable | Núcleo | La arquitectura debe permitir integrar modelos de detección open-vocabulary sin acoplar el sistema a una única alternativa. |
| Gestión de prompts y vocabulario activo | Núcleo | Debe versionar formulaciones, aliases, estrategias de detección, vocabulario activo y umbrales asociados. |
| Normalización de detecciones | Núcleo | Las salidas heterogéneas de los modelos deben transformarse en detecciones comparables, trazables y aptas para evaluación posterior. |
| Evaluación de patrones de Nivel 1 | Núcleo | Las detecciones positivas deben asociarse espacialmente por sujeto, transformarse en un estado de ausencia evaluable y estabilizarse mediante persistencia temporal e histéresis. |
| Registro de alertas asistivas | Núcleo | Las alertas deben registrarse cuando un patrón alcanza estado confirmado, sin constituir un juicio normativo automático. |
| Publicación y persistencia de eventos | Núcleo | La arquitectura debe desacoplar la producción de evidencia perceptiva y conservar un historial reconstruible de eventos relevantes. |
| Observabilidad y métricas | Núcleo | Debe medir FPS, latencias por tramo, uso de recursos, estados de patrón, alertas, descartes y errores. |
| Reporte experimental | Núcleo | Debe sintetizar configuración, resultados, métricas, alertas, errores y limitaciones por corrida. |
| Inspección mínima de resultados | Núcleo | Debe permitir revisar corridas, alertas, métricas y evidencia asociada sin convertirse en un tablero operativo avanzado. |
| Gestión de evidencia visual controlada | Complementario previsto | Debe admitir clips, snapshots o recortes justificados para validación, revisión técnica o comunicación académica. |
| Video crudo continuo | Fuera del comportamiento ordinario | La trazabilidad principal se apoya en eventos, metadatos, métricas y referencias controladas. |
| Condiciones de riesgo de Nivel 2 y Nivel 3 | Extensión condicionada | Requieren capacidades adicionales de contexto, razonamiento espacial, zonas, proximidad o relaciones entre entidades. |
| Capacidades contextuales y relacionales | Extensión condicionada | Zonas y evaluadores relacionales quedan previstos sin bloquear CR-01 y CR-02; su habilitación requiere evidencia e instrumentación adecuadas. |
| Identidad temporal de sujeto y métricas MOT | Capacidad opcional; métricas fuera del núcleo | La arquitectura admite granularidad por sujeto mediante una identidad temporal válida. Las métricas MOT no condicionan la evaluación del núcleo ni deben confundirse con la capacidad de mantener identidad. |
| Adaptación al dominio (fine-tuning) | Rama comparativa condicionada | Sólo corresponde bajo una línea base preentrenada congelada, datos suficientes, partición disjunta y criterios de escalamiento definidos con anterioridad a los resultados. |

**Nota**. El compromiso “núcleo” identifica capacidades necesarias para el flujo base; “núcleo de evaluación” refiere a capacidades que sostienen la evaluación controlada; “complementario previsto” agrupa capacidades útiles para validación, revisión o comunicación académica; “extensión condicionada” identifica capacidades previstas pero no obligatorias; y “rama comparativa condicionada” refiere a variantes que sólo deben incorporarse si se cumplen las condiciones metodológicas correspondientes.

##### 17.3.3.3. Requisitos no funcionales de referencia

Las cualidades no funcionales condicionan directamente la validez experimental del prototipo. No alcanza con detectar una condición de riesgo si el sistema no registra la configuración de la corrida, no mide latencia, no conserva trazabilidad suficiente o no controla la evidencia visual generada. Por esta razón, la reproducibilidad, la observabilidad, la privacidad, la modularidad, la integridad de eventos y el control de complejidad se consideran condiciones arquitectónicas del diseño.

**Tabla 40**

*Requisitos no funcionales de referencia*

| **Dimensión** | **Requisito de diseño** | **Implicación arquitectónica** |
| --- | --- | --- |
| Latencia | Acotar la ruta crítica desde la lectura o captura hasta la publicación de eventos de percepción. | El plano de medios no debe depender de reportes, inspección, persistencia pesada ni notificaciones externas para continuar procesando frames. |
| Reproducibilidad | Registrar la configuración efectiva de cada corrida. | Cada ejecución debe conservar fuente, modelo, prompts, umbrales, entorno, versiones y políticas de muestreo. |
| Modularidad | Permitir la sustitución de fuentes, modelos, prompts, postproceso y motor de patrones. | Los componentes deben comunicarse mediante contratos explícitos y no mediante estructuras internas acopladas. |
| Trazabilidad | Reconstruir una alerta a partir de configuración, detecciones, patrón, métricas y evidencia asociada. | Los eventos, identificadores y relaciones causales deben conservar información suficiente para revisión posterior. |
| Integridad de eventos | Evitar pérdida, duplicación o ambigüedad en eventos relevantes. | Los eventos deben incluir identificadores, versión de esquema, orden lógico y asociación con la corrida correspondiente. |
| Privacidad y minimización | Proteger configuraciones, métricas, eventos y artefactos visuales conservados. | La trazabilidad ordinaria debe apoyarse en eventos y metadatos; los artefactos visuales sólo deben conservarse cuando estén justificados. |
| Observabilidad | Medir tiempos, FPS, errores, descartes y uso de recursos desde las primeras corridas. | La instrumentación debe formar parte del diseño del pipeline y no quedar como una actividad posterior. |
| Robustez experimental | Registrar fallas y anomalías sin ocultar su impacto sobre la corrida. | Los errores de fuente, inferencia, publicación, persistencia o medición deben producir registros interpretables. |

**Nota**. Los requisitos no funcionales expresan cualidades necesarias para preservar la validez experimental del prototipo. Su finalidad es asegurar comparabilidad entre corridas, trazabilidad de resultados y control de decisiones que puedan afectar la latencia, privacidad, reproducibilidad u observabilidad.

##### 17.3.3.4. Decisiones arquitectónicas iniciales

Además de delimitar alcance, capacidades y cualidades no funcionales, el diseño debe explicitar un conjunto de decisiones arquitectónicas iniciales. Estas decisiones no fijan tecnologías concretas, pero establecen reglas estructurales que deberán preservarse durante el desarrollo del prototipo experimental para mantener coherencia con el alcance metodológico, la trazabilidad y la medición de resultados.

**Tabla 41**

*Decisiones arquitectónicas iniciales*

| **ID** | **Decisión** | **Justificación** |
| --- | --- | --- |
| DA-01 | Separar plano de medios y plano de control. | Protege la ruta crítica de vídeo y desacopla la inferencia de la lógica de interpretación. |
| DA-02 | Publicar evidencia perceptiva como eventos de percepción normalizados. | Permite desacoplar detecciones, patrones, métricas, alertas y persistencia. |
| DA-03 | Separar el gobierno de las corridas, el transporte de eventos durante la ejecución y el repositorio persistente de hechos. | Cada preocupación tiene un régimen propio: el gobierno es puntual y de solicitud–respuesta, el transporte es continuo y no debe bloquear la ruta crítica, y la persistencia debe sobrevivir a la corrida para habilitar su relectura. Mantenerlas separadas permite sustituir el mecanismo de transporte sin alterar el gobierno ni la evidencia, y reevaluar cualquier corrida sin depender de la mensajería. |
| DA-04 | Confirmar patrones mediante persistencia temporal e histéresis. | Reduce alertas generadas por detecciones aisladas, inestables o de corta duración. |
| DA-05 | Integrar modelos OVD mediante adaptadores. | Permite comparar modelos o variantes sin rediseñar la arquitectura general. |
| DA-06 | Admitir granularidad por sujeto mediante identidad temporal opcional, sin convertir las métricas MOT en requisito del núcleo. | Permite evaluar persistencia por persona cuando existe identidad válida y conserva la granularidad de escena como configuración independiente. |
| DA-07 | Tratar la adaptación al dominio como rama comparativa separada y condicionada por datos y protocolo. | Preserva una línea base zero-shot congelada y evita mezclar resultados de una variante ajustada con el núcleo sin entrenamiento. |
| DA-08 | Adoptar minimización visual como criterio ordinario de trazabilidad. | Evita que el almacenamiento indiscriminado de video crudo sea parte del comportamiento base. |
| DA-09 | Separar trazabilidad ordinaria de evidencia visual controlada. | Permite conservar clips, capturas o recortes sólo cuando estén justificados por validación, revisión técnica o comunicación académica. |
| DA-10 | Priorizar DBE antes de EBE. | Estabiliza contratos, inferencia, eventos y métricas antes de incorporar captura continua. |
| DA-11 | Permitir preselección liviana en el rol de captura como variante opcional, conservadora y deshabilitada por defecto, que conserva la unidad en el flujo principal ante falla o incertidumbre del preselector. | La variante puede reducir carga sin transformar el borde en fuente de verdad ni ocultar descartes, porque el flujo base continúa disponible y comparable. |
| DA-12 | Versionar prompts y vocabulario activo por corrida. | Garantiza la reproducibilidad y comparación entre formulaciones. |
| DA-13 | Registrar toda alerta interna antes de aplicar políticas de supresión o entrega externa. | Preserva la semántica y la medición del episodio; el cooldown, la limitación de tasa y la idempotencia pertenecen al tramo de distribución. |

**Nota.** Las decisiones fijan reglas estructurales adoptadas para el diseño del prototipo experimental. Su materialización y verificación se documentan en la sección 17.4.

Las decisiones DA-08 y DA-09 deben leerse de manera conjunta. La plataforma no utiliza el almacenamiento continuo de video crudo como mecanismo ordinario de trazabilidad; la reconstrucción experimental se apoya principalmente en eventos, metadatos, identificadores, métricas y referencias controladas. Sin embargo, la validación con captura continua, la revisión técnica o la defensa académica pueden requerir evidencia visual demostrativa. Por ello, se admite la generación de clips breves, snapshots o recortes anotados, siempre que estén justificados y cuenten con criterios explícitos de acceso, retención y anonimización.

La DA-13 complementa esta separación: para el núcleo del prototipo experimental, la alerta válida es el evento interno registrado por la plataforma. Cualquier notificación externa debe tratarse como una salida derivada, no bloqueante y medible por separado.

A estas decisiones se agregan tres precisiones de lectura arquitectónica: DBE y EBE se tratan como escenarios experimentales y no como topologías físicas; la diferencia entre fuentes reproducibles y fuentes en vivo condiciona los criterios de control de ritmo y trazabilidad temporal; y la distribución física de componentes no forma parte del compromiso conceptual de esta etapa.

#### 17.3.4. Principios arquitectónicos adoptados

Las decisiones enumeradas en la Tabla 41 se articulan alrededor de cuatro principios que orientarán la lectura del diseño en las secciones siguientes.

El primero es la **separación entre ruta crítica y lógica de control**: la inferencia y la publicación de evidencia perceptiva (DA-01, DA-02) deben mantenerse desacopladas de la evaluación de patrones, la persistencia, los reportes y las notificaciones externas, de modo que ninguna tarea posterior pueda bloquear el procesamiento visual.

El segundo es la **modularidad por contratos**: fuentes, modelos, prompts, detecciones, patrones y métricas deben intercambiarse mediante estructuras explícitas (DA-05, DA-12), evitando dependencias internas que dificulten la sustitución o la evaluación comparativa.

El tercero es la trazabilidad experimental: toda alerta debe poder reconstruirse a partir de la configuración de corrida, los eventos de percepción, el patrón evaluado y las métricas registradas (DA-03, DA-04, DA-13).

El cuarto es la **medición desde el diseño**: tiempos, FPS, descartes, errores y estados de patrón deben instrumentarse desde las primeras corridas, dado que forman parte de la validez experimental del prototipo.

A estos principios se suma el criterio transversal de **evolución incremental**: las capacidades condicionadas (DA-06, DA-07, DA-11) deben incorporarse sin desplazar el núcleo de Nivel 1 ni convertirse en dependencias del flujo base.

#### 17.3.5. Vista general de la arquitectura propuesta

La plataforma E-OVRT-VDP se organiza como una arquitectura lógica por bloques, orientada a procesar fuentes de video, generar evidencia perceptiva, evaluar patrones de riesgo y conservar resultados reconstruibles. Esta vista no representa una distribución obligatoria en procesos, servicios o nodos físicos independientes, sino una separación de responsabilidades que permite mantener el sistema modular, medible y trazable.

La arquitectura distingue un flujo principal y un conjunto de capacidades de soporte. La configuración experimental actúa de forma transversal sobre ese flujo: define las condiciones de cada corrida —escenario, modelo, prompts activos, umbrales, políticas de evidencia y parámetros de ejecución— para asegurar reproducibilidad sin intervenir directamente en el procesamiento frame a frame.

El flujo principal parte de fuentes visuales externas, como datasets, vídeos locales, cámaras o flujos de streaming. El plano de medios comienza en el adaptador de ingesta visual, que encapsula los distintos orígenes bajo una representación común. Desde ese punto se concentra la ruta crítica: lectura o captura, decodificación cuando corresponde, control de ritmo, normalización, inferencia open-vocabulary, postproceso y publicación de evidencia perceptiva normalizada. El plano no depende de tareas posteriores para continuar procesando unidades visuales.

A partir de los eventos publicados, el plano de control interpreta la evidencia producida por el plano de medios: evalúa patrones, administra estados de corrida y registra alertas asistivas internas cuando se confirma una condición de riesgo. Las alertas confirmadas se publican por un bus dedicado hacia el módulo de distribución, que aplica la política de notificación y registra los resultados de entrega sin bloquear al motor de patrones. El ciclo de vida de ambos planos y del módulo de distribución se gobierna mediante interfaces HTTP independientes; la interfaz de inspección y el orquestador experimental gobiernan el ciclo de vida mediante las interfaces de gobierno de cada módulo y no consumen directamente los buses.

Finalmente, la trazabilidad, la observabilidad y la inspección se agrupan en el bloque de soporte experimental, que no constituye una etapa lineal del flujo frame a frame sino una capacidad transversal. Este bloque conserva evidencia reconstruible, consolida telemetría técnica y permite revisar corridas, métricas, alertas y resultados experimentales sin interferir con la ruta crítica del plano de medios.

**Figura 4.1**

*Vista conceptual de la arquitectura E-OVRT-VDP*

⟦FIGURA: no extraída — ver el .docx⟧

*Nota.* La figura presenta una vista lógica de alto nivel. Las flechas sólidas representan el flujo principal de datos y eventos; las flechas punteadas representan influencia de configuración o capacidades de soporte. La figura no debe interpretarse como una distribución física obligatoria ni como una asignación definitiva a tecnologías específicas.

La materialización de esta vista distingue dos patrones de acople complementarios. El gobierno de las corridas se realiza mediante interfaces HTTP gobernadas por configuración en los tres módulos ejecutables. Se adopta HTTP porque el ciclo de vida de una corrida —crear, consultar, cancelar y cerrar— tiene semántica de solicitud y respuesta, admite múltiples clientes sin acoplarlos entre sí y permite disponer los módulos en un mismo host o en hosts distintos sin modificar su lógica; el gobierno por configuración garantiza que cada corrida declare sus parámetros en lugar de heredarlos de constantes ocultas. El intercambio de datos en ejecución se realiza mediante un bus ZeroMQ con patrón publicador-suscriptor y serialización binaria msgpack: un canal de detecciones entre los planos y un canal de alertas hacia la distribución. Se adopta ZeroMQ porque ofrece transporte de baja latencia sin requerir un broker como dependencia adicional del prototipo, y el patrón publicador-suscriptor desacopla al productor de sus consumidores sin bloquear la ruta crítica; msgpack reduce el costo de serialización respecto del texto plano conservando estructuras autodescriptivas. La durabilidad no se le exige al canal: cada hecho se persiste en archivos JSONL de sólo adición antes de publicarse, de modo que la evidencia pueda releerse y reevaluarse sin depender de la mensajería. La persistencia JSONL cumple esa función de durabilidad y relectura —inspeccionable, de sólo adición y sin introducir una base de datos como dependencia del núcleo— y no constituye un tercer patrón de acople. HTTP gobierna configuración y ciclo de vida; el bus transporta hechos de ejecución.

En conjunto, esta organización permite que el procesamiento de video, la interpretación de patrones, la distribución de alertas y el análisis experimental se mantengan separados y coordinados mediante contratos explícitos, favoreciendo la reproducibilidad y la evaluación controlada del prototipo.

#### 17.3.6. Configuración experimental y diseño de prompts

La configuración experimental concentra las decisiones que gobiernan una corrida de evaluación de la plataforma experimental. Su función es declarar, de manera explícita y reproducible, el escenario, la fuente visual, el modelo OVD, los prompts activos, los umbrales, la política de muestreo, los módulos habilitados, los criterios de patrón, la política de evidencia y la instrumentación de métricas.

Esta sección materializa, en términos arquitectónicos, definiciones establecidas en la consolidación metodológica. Las condiciones de riesgo, los escenarios, las métricas y los criterios de prompting pasan a expresarse como parámetros ejecutables que condicionan al plano de medios y al plano de control. De este modo, cada detección, transición de patrón, alerta interna, métrica o evidencia conservada puede asociarse con una configuración efectiva de corrida.

Dentro de esa configuración, los prompts se tratan como parte del vocabulario activo del experimento. En un sistema open-vocabulary, la consulta textual incide sobre la evidencia perceptiva generada; por lo tanto, debe registrarse, versionarse y mantenerse trazable hasta los resultados que contribuye a producir.

##### 17.3.6.1. Función arquitectónica de la configuración experimental

La configuración experimental actúa como punto de gobierno de la corrida. Antes de iniciar la ejecución, define qué se evaluará, con qué fuente, con qué modelo, con qué vocabulario activo y bajo qué criterios de interpretación. Esta función separa la definición de condiciones de ejecución del procesamiento efectivo de frames y eventos.

La separación protege la ruta crítica del plano de medios. Una vez iniciada la corrida, el pipeline debe disponer de la configuración efectiva sin depender de consultas externas bloqueantes para decidir qué modelo ejecutar, qué prompts utilizar o qué política de muestreo aplicar. La configuración gobierna la ejecución, pero no debe introducir latencia durante el procesamiento continuo.

También delimita la interpretación posterior de resultados. Una detección sólo es experimentalmente útil si puede relacionarse con su fuente, modelo, prompt, umbral, postproceso y patrón evaluado. Sin esa asociación, no sería posible atribuir diferencias de desempeño a una variable concreta de la corrida.

Esa función de gobierno sólo se sostiene si la configuración se resuelve y se valida antes de iniciar la ejecución: una corrida cuya declaración esté incompleta debe fallar al crearse y no producir artefactos que luego resulten inatribuibles. La función se proyecta además sobre los tres destinatarios de la configuración: el plano de medios recibe los parámetros que aplica sin diseñarlos ni versionarlos, el plano de control recibe los criterios con los que evalúa, y el soporte experimental la utiliza como clave de reconstrucción, de modo que todo evento, métrica, alerta o evidencia conservada pueda rastrearse hasta la corrida que le dio origen.

##### 17.3.6.2. Configuración de corrida como artefacto de reproducibilidad

La configuración de corrida se materializa como un manifiesto de experimento que referencia y congela las configuraciones efectivas de cada componente. Esta separación responde a que el plano de medios, el plano de control y el tramo de distribución poseen ciclos de vida y destinatarios distintos; una configuración monolítica no tendría un único consumidor ni permitiría reconstruir con precisión qué versión recibió cada servicio.

En este trabajo, se denomina ejecución experimental a la unidad lógica que agrupa las ejecuciones independientes de los componentes que participan en una misma instancia del experimento. Esta unidad se identifica mediante un experiment_id, mientras que cada componente conserva su propio identificador de corrida. La separación entre ambos niveles permite correlacionar configuraciones, eventos, métricas, alertas, entregas y artefactos bajo una clave común, sin imponer un ciclo de vida único ni una configuración monolítica a los servicios participantes.

El manifiesto declara un experiment_id, las referencias a las configuraciones de cada plano, el orden de disparo y los artefactos congelados —modelo, conjunto de prompts, conjunto de patrones y política de distribución—. Dos corridas sólo son comparables cuando se conoce qué variable cambió y cuáles permanecieron constantes. La Tabla 42 resume los elementos mínimos de este gobierno reproducible.

**Tabla 42**

*Elementos mínimos de la configuración experimental*

| **Elemento configurable** | **Contenido esperado** | **Función arquitectónica** |
| --- | --- | --- |
| Manifiesto de experimento | Versión del manifiesto, fecha, objetivo y referencias a las configuraciones efectivas del plano de medios, del plano de control y del módulo de distribución cuando se habilita. | Gobierna una ejecución experimental sin imponer una configuración monolítica a servicios con ciclos de vida independientes. |
| Identificador de experimento | experiment_id, junto con los identificadores de corrida de cada componente. | Vincula eventos, métricas, errores, alertas, entregas y artefactos de todos los componentes bajo una clave común. |
| Escenario y fuente visual | DBE o EBE; dataset, vídeo local, imagen, cámara o stream; naturaleza temporal; resolución, ritmo esperado, duración y restricciones conocidas. | Distingue fuentes reproducibles, fuentes temporales y fuentes en vivo sin confundir escenario con topología física. |
| Parámetros del pipeline | Resolución de procesamiento, selección o muestreo, criterios de omisión o descarte, tamaño de cola, ritmo esperado y calentamiento. | Condiciona latencia, cobertura temporal, unidades procesadas y lectura de descartes. |
| Modelo OVD | Modelo, versión, checkpoint, backend, precisión numérica, dispositivo y adaptador. | Permite sustituir o comparar modelos sin acoplar el resto de la arquitectura. |
| Prompts y vocabulario activo | Conjunto versionado, condición asociada, rol de cada clase, estrategia de formulación y umbral vinculado. | Garantiza trazabilidad entre consulta textual, evidencia producida y configuración. |
| Umbrales y postproceso | Confianza mínima, IoU/NMS, filtros por clase, tamaño, región y normalización de coordenadas. | Define qué salidas crudas se transforman en evidencia perceptiva normalizada. |
| Patrones activos | Condición, severidad, granularidad scene\|subject, ventana de confirmación, histéresis de resolución y criterio de evidencia. | Transforma evidencia puntual en estados y alertas internas por episodio. El cooldown no integra este contrato. |
| Capacidades habilitadas y evidencia | Identidad de sujeto, zonas, preselección en borde, inspección, distribución y política de evidencia visual. | Evita capacidades implícitas y preserva la comparabilidad entre corridas. |
| Política de distribución | Canal, calidad de servicio, idempotencia, supresión de re-notificación, limitación de tasa y retención del ledger. | Ubica cooldown y controles de comunicación aguas abajo de la alerta interna. |
| Instrumentación y entorno | Timestamps por tramo, métricas esperadas, estado de aplicabilidad, causa, entorno, librerías y runtime. | Permite calcular o rechazar métricas de forma explícita y reconstruir condiciones de ejecución. |

Nota. La tabla presenta los elementos mínimos del manifiesto y de las configuraciones referenciadas. Los contratos concretos se desarrollan en §17.3.11.

##### 17.3.6.3. Diseño de prompts y vocabulario activo

El diseño de prompts materializa la forma en que las condiciones de riesgo se expresan como consultas consumibles por un modelo OVD. En la metodología previa se trató la sensibilidad de estos modelos a la formulación de la consulta y se reconoció que el prompt no es un detalle accesorio, sino una variable de ingeniería que puede alterar detecciones, falsos positivos, falsos negativos y estabilidad temporal (Du et al., 2022; Zhou et al., 2022).

Para el prototipo, los prompts primarios se formulan en inglés. Esta decisión se apoya en la centralidad de ese idioma en los corpus y modelos visión-lenguaje utilizados como base, como CLIP, Conceptual Captions y CC12M, entrenados o construidos principalmente a partir de pares imagen-texto y recursos web en inglés (Changpinyo et al., 2021; Radford et al., 2021; Sharma et al., 2018). En consecuencia, el documento puede describir las condiciones en español, pero la capa de consulta del detector se diseña en inglés para favorecer la alineación con los patrones lingüísticos dominantes del preentrenamiento.

Cada prompt debe asociarse a una condición de riesgo, un texto de consulta, una estrategia de formulación, una versión y un conjunto de prompts activos. Una modificación de redacción debe registrarse como variante experimental, no como reemplazo informal. Esto permite explicar qué formulación produjo una detección y comparar resultados sin perder vínculo con la condición original.

El vocabulario activo representa el conjunto de prompts habilitados en una corrida. Su tamaño y composición afectan el comportamiento semántico del detector y, según el modelo, el costo de inferencia. Por ello, el núcleo validable debe trabajar con un vocabulario reducido y controlado: suficiente para evaluar sensibilidad de formulación, pero sin habilitar listas amplias que dificulten atribuir resultados.

También debe distinguirse entre prompt y estrategia de detección. Un prompt es una consulta semántica; una estrategia puede combinar prompts, postproceso, evidencia indirecta o reglas espaciales. Esta sección define el diseño y versionado de prompts. La integración entre condición, estrategia de detección, patrón y alerta se desarrolla posteriormente.

##### 17.3.6.4. Diseño inicial de prompts para el catálogo de condiciones

El diseño inicial distingue el vocabulario positivo del núcleo, los conjuntos correspondientes a ramas comparativas y el vocabulario condicionado de las condiciones de mayor complejidad. Para CR-01 y CR-02, el núcleo utiliza person, helmet y vest: la primera categoría identifica la entidad sujeto y las restantes representan los elementos de protección cuya presencia se evalúa espacialmente respecto de cada persona.

La ausencia de casco o chaleco no se formula como consulta principal del núcleo. Se infiere en el plano de control cuando existe evidencia suficiente de una persona y no se encuentra evidencia del EPP correspondiente dentro de la región configurada. Las consultas negativas o de estado observable se mantienen en conjuntos separados para las estrategias directa e híbrida ya distinguidas en la consolidación metodológica, de modo que sus resultados sean atribuibles a una estrategia explícita y no a una mezcla informal de vocabularios. En el diseño arquitectónico y en lo que sigue del trabajo, estas familias se identifican mediante un código: estrategia directa (E-DIR), cuando el prompt intenta describir la condición de riesgo completa; estrategia indirecta (E-IND), cuando el detector identifica entidades visibles por separado y la condición se reconstruye mediante lógica externa al modelo; y estrategia híbrida (E-HYB), cuando se combinan consultas de ambos tipos bajo una regla de composición explícita.

CR-03 y CR-04 conservan consultas compuestas y descompuestas de carácter condicionado, porque su confirmación requiere contexto espacial adicional. CR-05 y CR-06 se expresan mediante entidades componentes, ya que la condición completa depende de proximidad, seguimiento o zonas declaradas externamente. La Tabla 43 organiza estos vocabularios y su uso previsto.

**Tabla 43**

*Vocabulario inicial de prompts en inglés por condición de riesgo*

| **Condición y estrategia** | **Rol de la consulta** | **Consulta o categoría candidata** | **Uso previsto** |
| --- | --- | --- | --- |
| CR-01 y CR-02 — núcleo E-IND | Entidad sujeto | person | Localizar las personas sobre las cuales se evalúa la presencia o ausencia espacial del EPP. |
| CR-01 — núcleo E-IND | Evidencia positiva de EPP | helmet | Detectar casco asociable a una persona. La ausencia se infiere en el plano de control. |
| CR-02 — núcleo E-IND | Evidencia positiva de EPP | vest | Detectar chaleco asociable a una persona. La ausencia se infiere en el plano de control. |
| CR-01 — rama E-DIR | Ausencia o estado observable | bare_head; “person without hard hat”; “construction worker without safety helmet”; “person with bare head on construction site” | Comparar formulaciones directas bajo una configuración independiente del núcleo. |
| CR-02 — rama E-DIR | Ausencia o descripción visual | “person without reflective vest”; “worker without high-visibility vest”; “person without bright colored safety clothing” | Comparar formulaciones directas o atributivas bajo una configuración independiente del núcleo. |
| CR-03 — condicionada | Consulta compuesta | “person on scaffolding without harness”; “worker at height without fall protection equipment” | Explorar evidencia parcial; la confirmación requiere contexto espacial y observabilidad suficiente. |
| CR-03 — condicionada | Consulta descompuesta | “person on scaffolding”; “person on elevated platform”; “safety harness”; “fall arrest harness” | Detectar por separado persona en altura y elementos de protección para evaluación posterior. |
| CR-04 — condicionada | Consulta compuesta | “unprotected edge with person nearby”; “elevated platform without guardrail near workers” | Explorar evidencia parcial; la confirmación requiere proximidad y validación espacial. |
| CR-04 — condicionada | Consulta descompuesta | “platform edge”; “open edge”; “guardrail”; “safety railing”; “person near edge” | Detectar borde, protección colectiva y persona próxima como entidades independientes. |
| CR-05 — condicionada | Entidades de maquinaria | “excavator”; “backhoe loader”; “dump truck”; “crane”; “heavy machinery” | Producir evidencia para evaluar proximidad y persistencia con personas. |
| CR-05 — condicionada | Entidades humanas | person; “construction worker”; “pedestrian” | Producir evidencia humana para la evaluación relacional. |
| CR-06 — condicionada | Entidad persona | person; “worker”; “pedestrian” | Comparar la posición del sujeto con una zona declarada externamente. |
| CR-06 — condicionada | Elementos auxiliares | “restricted area sign”; “caution tape”; “warning tape”; “barrier”; “safety cone” | Aportar referencias visuales sin reemplazar la definición externa de la zona. |

Nota. El vocabulario del núcleo validable está compuesto por person, helmet y vest. Las formulaciones directas pertenecen a ramas comparativas independientes. Cada corrida conserva prompt_set_id, de modo que toda detección pueda atribuirse al conjunto que la produjo.

##### 17.3.6.5. Reglas de comparabilidad entre configuraciones

La configuración debe permitir comparar variantes sin producir conclusiones ambiguas. Al comparar prompts, deben mantenerse constantes modelo, fuente visual, resolución, política de muestreo, umbrales, postproceso y criterios de patrón. Así, una variación de desempeño puede atribuirse razonablemente a la formulación evaluada.

Al comparar modelos OVD, debe conservarse el mismo conjunto de prompts y condiciones equivalentes de fuente, resolución y postproceso. Si un modelo requiere umbrales distintos por la escala de sus puntajes, esa diferencia debe declararse como parte de la configuración y no ocultarse como detalle de implementación.

Al comparar DBE y EBE, debe declararse que cambia la naturaleza temporal de la fuente. En EBE intervienen captura continua, variabilidad de iluminación, codificación o decodificación cuando corresponda, continuidad temporal, omisiones, descartes y disponibilidad efectiva de frames. Por lo tanto, las diferencias observadas no deben atribuirse automáticamente al detector OVD.

Por la misma razón, ningún módulo opcional —evidencia visual, identidad temporal, zonas, preselección en el rol de captura o distribución externa— puede operar como comportamiento implícito: su habilitación se declara en la configuración de la corrida, porque una activación silenciosa alteraría la interpretación de latencia, cobertura temporal, privacidad y aplicabilidad de métricas, es decir, la base misma de la comparación.

#### 17.3.7. Diseño conceptual del plano de medios

El plano de medios se materializa en el componente lógico Pipeline de Medios de la plataforma experimental. Este componente concentra la ruta sensible a latencia: inicia cuando el adaptador de ingesta visual recibe, lee o decodifica una unidad visual proveniente de una fuente externa, y finaliza cuando se publica evidencia perceptiva normalizada hacia la frontera de integración. Su alcance incluye ingesta, decodificación cuando corresponda, control de ritmo, normalización visual, inferencia open-vocabulary, postproceso y publicación no bloqueante.

El límite del componente es estricto. El Pipeline de Medios no confirma condiciones de riesgo, no asigna severidad, no ejecuta reglas de patrón, no genera alertas y no depende de persistencia pesada para continuar procesando frames. Su salida representa evidencia perceptiva primaria asociada a una corrida, una fuente, una referencia temporal, un modelo y una configuración de procesamiento. La interpretación de esa evidencia corresponde al plano de control.

La separación protege la ruta frame-evento frente a tareas que pueden introducir bloqueo o variabilidad, como la evaluación de patrones, la reconstrucción histórica, la generación de reportes, la inspección visual o la distribución de notificaciones externas. La sección precisa cómo debe comportarse el componente que transforma entrada visual en evidencia perceptiva utilizable por el resto del sistema.

Las fuentes utilizadas en DBE y EBE ingresan al Pipeline de Medios mediante una misma frontera conceptual: el adaptador de ingesta visual. La diferencia entre ambos escenarios se resuelve en la forma de lectura, disponibilidad del frame, metadatos temporales y control de ritmo, no en la salida del plano. En DBE predomina la lectura reproducible; en EBE puede aparecer irregularidad temporal, atraso acumulado, variabilidad de captura o disponibilidad de frames recientes. En ambos casos, la salida debe conservar trazabilidad suficiente para reconstruir qué se procesó, bajo qué configuración y con qué resultado.

La configuración experimental actúa como entrada transversal del Pipeline de Medios, pero no es una responsabilidad interna de este plano. Fuente, resolución, política conceptual de selección o muestreo, modelo, prompts activos, umbrales y modo de inferencia son definidos por la configuración de corrida. El plano de medios debe consumir esa configuración, aplicarla durante la ejecución y propagar sus identificadores en la evidencia publicada, sin convertirse en el módulo encargado de gobernarla o versionarla.

**Figura 4.2**

*Flujo conceptual del Pipeline de Medios*

⟦FIGURA: no extraída — ver el .docx⟧

Nota. La figura representa el flujo interno del plano de medios. Las fuentes visuales son externas al plano; el plano comienza en el adaptador de ingesta visual, responsable de recibir, leer o decodificar la fuente y transformarla en una unidad visual procesable. La configuración de corrida parametriza la ejecución como entrada transversal, sin formar parte del procesamiento frame a frame. El evento de percepción normalizado se ubica por fuera del recuadro para señalar la frontera de salida hacia el bus interno de eventos y el plano de control.

##### 17.3.7.1. Flujo operativo del Pipeline de Medios

El flujo interno del Pipeline de Medios se organiza como una cadena de transformación progresiva. Cada etapa recibe una representación visual o perceptiva, aplica una operación acotada y entrega una salida que mantiene relación con la corrida y con la referencia temporal original. Esta organización permite sustituir fuentes, modelos o políticas de procesamiento sin modificar la responsabilidad general del plano.

**Ingesta y decodificación. La primera responsabilidad interna del plano de medios es recibir la entrada visual desde fuentes externas, como datasets, imágenes, videos locales, cámaras o streams. La fuente queda encapsulada por un adaptador de ingesta visual que oculta diferencias de formato sin eliminar información relevante para la evaluación. Cuando la entrada proviene de vídeo codificado o streaming, la decodificación convierte el flujo en frames procesables y registra la información necesaria para distinguir disponibilidad, recepción, orden lógico y referencia temporal. En DBE suele alcanzar con conservar índice de secuencia y orden de lectura; en EBE puede ser necesario registrar además timestamps de captura o recepción, irregularidad temporal y eventuales descartes por atraso.**

**Control de ritmo y selección de unidades visuales. Antes de ingresar a inferencia, el pipeline debe decidir qué unidades visuales serán efectivamente procesadas. Esta decisión puede consistir en aceptar todos los frames, aplicar una selección determinista, reducir la frecuencia de procesamiento o priorizar unidades recientes cuando existe captura continua. Lo importante para el diseño no es imponer una política concreta, sino evitar decisiones invisibles: toda unidad omitida, reemplazada o descartada debe quedar asociada a una causa y a una política declarada en la corrida. Los detalles concretos de colas, buffers o algoritmos de descarte corresponden a la implementación.**

**Normalización visual. El frame aceptado se adapta a los requisitos del modelo seleccionado. Esta etapa puede modificar resolución, formato, espacio de color, disposición de tensores o escala de entrada. El diseño debe preservar la relación entre coordenadas originales y coordenadas de inferencia, porque esa relación permite interpretar cajas delimitadoras, revisar evidencia visual y comparar resultados entre configuraciones con distinta resolución. Reescalado, recortes o relleno de bordes no deben tratarse como operaciones invisibles.**

**Inferencia open-vocabulary.** La inferencia ejecuta el detector configurado sobre la entrada normalizada y el conjunto de prompts activos. El modelo se integra mediante un adaptador para evitar que el resto del plano dependa de una salida particular de Grounding DINO, YOLOE u otro candidato. Esta etapa produce resultados crudos: cajas, puntajes, etiquetas, frases asociadas o estructuras equivalentes, según el formato propio del detector utilizado. Cuando el modelo lo permita, el adaptador puede reutilizar representaciones textuales precalculadas o mecanismos equivalentes para reducir el costo de inferencia, siempre que esa optimización no altere la trazabilidad de la corrida.

**Postproceso y normalización de detecciones. Luego de la inferencia, el Pipeline de Medios aplica los filtros definidos por la configuración de corrida —umbrales, supresión de detecciones redundantes, normalización de etiquetas y remapeo de coordenadas— para convertir las salidas del modelo en evidencia perceptiva común. Esta salida queda asociada al frame, prompt, condición y nivel de confianza correspondiente, pero no interpreta riesgo ni genera alertas; sólo entrega evidencia normalizada al plano de control.**

**Publicación de evidencia perceptiva.** La publicación cierra el plano de medios. La evidencia normalizada se entrega como evento liviano hacia la frontera de integración, asociado a corrida, fuente, referencia temporal, modelo, prompts y timestamps relevantes. A partir de ese punto, la evidencia puede ser evaluada por el plano de control, persistida de manera reconstruible o inspeccionada por componentes de soporte; ninguna de esas tareas debe ser requisito para que el Pipeline de Medios continúe procesando la siguiente unidad visual.

En consecuencia, la salida del plano de medios no se reduce a cajas y puntajes sin contexto, pero tampoco incorpora severidad, confirmación de patrón ni decisión de alerta. Su producto es evidencia visual primaria, normalizada y trazable: la interpretación de esa evidencia corresponde al plano de control, y la comparación entre configuraciones, modelos y prompts, al análisis experimental posterior.

##### 17.3.7.2. Criterios de diseño aplicados al plano de medios

Los criterios de diseño del plano de medios no agregan nuevas decisiones generales respecto de la arquitectura ya definida; traducen esas decisiones al comportamiento específico de la ruta frame-evento. El objetivo es que el procesamiento visual sea medible, sustituible y defendible sin mezclarlo con lógica de patrones, persistencia pesada o salidas externas.

El primer criterio es **mantener una ruta no bloqueante**. La inferencia y la publicación de evidencia no deben esperar indefinidamente a consumidores posteriores. Si el bus interno, la persistencia, la inspección o una salida externa fallan o se saturan, esa condición debe registrarse como parte de la ejecución, pero no debe convertir a esos consumidores en dependencia directa del procesamiento visual.

El segundo criterio es hacer visible la variabilidad temporal. En video, una latencia aparentemente baja puede ocultar pérdida de frames, colas saturadas o reemplazo de frames antiguos por frames recientes. Por eso, el Pipeline de Medios debe registrar timestamps por tramo, profundidad de cola cuando corresponda, frames aceptados, frames omitidos y descartes. La pérdida de evidencia no puede quedar fuera de la interpretación experimental.

El tercer criterio es **encapsular la heterogeneidad de modelos**. Los detectores OVD pueden diferir en formato de entrada, tipo de prompt, estructura de salida, semántica de puntajes y costo de inferencia. El plano de medios debe absorber esa heterogeneidad mediante adaptadores y entregar una evidencia perceptiva estable. De ese modo, el plano de control no queda acoplado a un modelo específico ni a detalles internos de su implementación.

El cuarto criterio es **conservar la trazabilidad mínima del resultado perceptivo**. Cada evidencia publicada debe poder asociarse con la corrida, la fuente, la referencia temporal, el modelo utilizado, los prompts activos y la política de procesamiento aplicada. Esta trazabilidad no implica almacenar video crudo de manera continua ni resolver la reconstrucción histórica dentro del plano de medios; implica producir eventos suficientes para que el soporte experimental pueda reconstruir la corrida posteriormente.

El quinto criterio es **no trasladar responsabilidades del plano de control hacia el plano de medios**. La persistencia temporal de un patrón, la histéresis, la severidad y el registro interno de alerta pertenecen al motor de patrones. El plano de medios puede mejorar la calidad de la evidencia perceptiva, pero no debe decidir si una condición observada se convirtió en una situación de riesgo confirmada.

##### 17.3.7.3. Control de ritmo según tipo de fuente

La política de control de ritmo se define por corrida y afecta qué evidencia visual llega a inferencia. En el diseño del plano de medios, esta política no se trata como una optimización secundaria, sino como parte de la configuración que condiciona la lectura de resultados. Cambiar la selección de unidades visuales, la frecuencia de procesamiento o el criterio de omisión equivale a cambiar la variante experimental evaluada.

En corridas DBE, o en general con fuentes cuya lectura puede regularse —conjuntos de imágenes, videos locales o archivos—, el lector puede regularse sin pérdida temporal de evidencia. Por ello, la prioridad arquitectónica es preservar reproducibilidad, orden lógico y trazabilidad de las unidades visuales procesadas. Si no se procesan todos los frames, la selección debe ser determinista, declarada en la configuración y mantenida constante entre corridas comparables.

En corridas EBE, o en general con fuentes en vivo como cámaras, streams o capturas continuas, la escena evoluciona aunque la inferencia se retrase. Por ello, el diseño debe priorizar que el atraso acumulado no crezca indefinidamente y que toda omisión, irregularidad temporal o descarte quede registrado. La estrategia concreta de selección de unidades visuales se declara en la configuración efectiva de cada corrida; su efecto sobre latencia, cobertura temporal y evidencia disponible debe ser observable desde el diseño.

El resultado esperado de esta política no es maximizar FPS de forma aislada, sino hacer interpretable el comportamiento del pipeline. Un sistema que procesa menos frames puede ser válido para una corrida exploratoria o comparativa, pero esa reducción debe ser visible para no confundir rendimiento con cobertura temporal.

##### 17.3.7.4. Capacidades opcionales sin desplazar el núcleo validable

El núcleo validable del plano de medios debe poder operar sin exigir seguimiento multiobjeto formal, preselección en borde ni adaptación de modelos al dominio. Estas capacidades pueden incorporarse como variantes del flujo, pero no deben convertirse en requisitos para demostrar el procesamiento básico de CR-01 y CR-02, y su incorporación no modifica el contrato de salida del plano de medios. La preselección en borde se adopta además bajo un criterio de degradación segura, denominado fail-open: ante una falla o una decisión incierta del preselector, la unidad visual se conserva para el flujo principal. De ese modo la variante puede descartar carga, pero nunca convertirse en causa de pérdida de evidencia.

El tracking o MOT puede ubicarse después del postproceso cuando resulte necesario estabilizar entidades, reducir oscilaciones entre frames o entregar identificadores temporales al plano de control. Aun así, un identificador temporal no equivale a una condición de riesgo sostenida.

Las variantes de ejecución orientadas a eficiencia deben tratarse con el mismo criterio: pueden ser útiles durante la implementación, pero no deben ocupar el centro del diseño conceptual del plano de medios. Reducciones de resolución, cambios de modo de inferencia o exportaciones a motores optimizados corresponden a decisiones de implementación y evaluación posterior; en esta sección sólo interesa fijar que cualquier variante que altere la ruta frame-evento debe quedar declarada en la configuración de corrida.

#### 17.3.8. Diseño conceptual del plano de control

El plano de control concentra la interpretación de la evidencia perceptiva producida por el plano de medios. Su responsabilidad comienza cuando ingresa un evento de percepción normalizado y termina cuando el sistema registra estados de patrón, alertas internas, eventos persistibles, métricas y salidas de inspección o distribución desacopladas. A diferencia del Pipeline de Medios, no procesa frames crudos ni necesita operar al ritmo constante de captura; trabaja sobre eventos y sobre cambios de estado derivados de reglas configuradas.

La separación entre detección, patrón y alerta es la decisión arquitectónica central de esta sección. Una detección puntual expresa una observación del modelo sobre una unidad visual; un patrón confirmado expresa que esa evidencia fue evaluada durante una ventana temporal bajo criterios explícitos de persistencia, umbral e histéresis; una alerta interna registra un episodio asistivo generado por una transición válida del patrón. Por lo tanto, el plano de control no debe transformar cada detección en una alerta, sino estabilizar la evidencia antes de producir salidas operativas.

Esta organización evita que la variabilidad propia de la inferencia OVD —falsos positivos, falsos negativos, fluctuación de puntajes, sensibilidad al prompt u oclusiones parciales— se traslade directamente al sistema de alertas. También permite mantener al plano de medios aislado de consumidores lentos, persistencia histórica, reportes, notificaciones externas o interfaces de inspección. El plano de control puede ejecutar esas funciones de forma asíncrona sin bloquear la producción de evidencia perceptiva.

En el alcance del prototipo experimental, el plano de control se orienta principalmente al núcleo validable. Para CR-01 y CR-02, la evaluación puede resolverse mediante persistencia temporal simple y estados de patrón sin exigir seguimiento multiobjeto formal. El tracking, las zonas espaciales o las reglas relacionales pueden enriquecer escenarios posteriores, pero no deben convertirse en una dependencia del núcleo validable.

**Figura 4.3**

*Flujo conceptual del plano de control*

⟦FIGURA: no extraída — ver el .docx⟧

**Nota.** La figura representa el flujo conceptual del plano de control. La configuración de corrida parametriza la evaluación como entrada transversal, sin formar parte del procesamiento evento a evento. El evento de percepción normalizado ingresa desde el plano de medios como entrada externa; dentro del plano se evalúan patrones, se actualizan estados y se derivan registros persistibles y métricas. La alerta interna por episodio se muestra por fuera del recuadro para indicar la frontera de salida del plano de control, quedando disponible para consumidores o adaptadores posteriores.

##### 17.3.8.1. Flujo lógico y responsabilidades del plano de control

El plano de control recibe evidencia perceptiva normalizada, selecciona los patrones activos, evalúa la evidencia espacial y temporal, administra el estado de cada patrón y registra una alerta interna cuando se confirma un episodio. En paralelo, persiste transiciones, métricas y errores necesarios para reconstruir la decisión.

El bus interno cumple una función de integración y no de razonamiento. La arquitectura conserva el transporte como mecanismo sustituible, pero fija para el prototipo una publicación ZeroMQ con patrón publicador-suscriptor, serialización msgpack y un envoltorio versionado. El plano de control consume ese contrato por el canal de detecciones del bus; no interpreta formatos propios de un detector ni recibe frames crudos.

El gobierno de la corrida no viaja por el bus. El plano de control se configura y se inicia mediante su interfaz HTTP, mientras que el bus transporta los hechos de ejecución. Esta separación entre gobierno y datos permite disponer los componentes en un mismo host o en hosts distintos sin modificar su semántica.

La evaluación transforma evidencia puntual en estados operativamente interpretables. No ejecuta inferencia visual, no asigna identidad personal y no determina cumplimiento normativo: aplica reglas declaradas de asociación espacial, persistencia, granularidad e histéresis.

Cuando un patrón alcanza el estado confirmado se registra la alerta interna: es el hecho principal del sistema y precede a cualquier notificación. La persistencia y el soporte experimental se mantienen fuera de la ruta crítica del plano de medios.

##### 17.3.8.2. Evaluación de patrones y máquina de estados

La máquina de estados distingue inactive, candidate, confirmed, sustained y resolved. Una evidencia inicial abre el estado candidato; la confirmación sólo ocurre cuando la condición satisface la ventana temporal y los umbrales declarados; la continuidad mantiene el episodio; y la ausencia sostenida durante la histéresis lo resuelve.

La transición a confirmed registra una alerta interna por episodio. El estado sostenido actualiza duración y evidencia sin convertir cada frame positivo en una alerta nueva. Una nueva confirmación posterior se conserva como re-alerta y se evalúa por separado de los falsos positivos.

Las ventanas se expresan en milisegundos y no en frames, de modo que la semántica temporal no cambie con la cadencia de procesamiento. Los componentes de una definición de patrón, incluidos los criterios espaciales de CR-01 y CR-02, se presentan al describir el motor de evaluación (sección 17.3.8.3.1); los valores adoptados para el núcleo se documentan en la sección 17.4.6.

La confirmación representa el cumplimiento de una regla interna bajo la configuración de la corrida; no constituye certificación normativa ni decisión automática de intervención.

**Figura 4.4**

*Máquina de estados del motor de patrones*

⟦FIGURA: no extraída — ver el .docx⟧

Nota. La figura representa el ciclo de vida temporal de un patrón de riesgo en el plano de control. Una condición observada inicia el estado candidate; si la evidencia satisface la ventana de confirmación configurada, el patrón pasa a confirmed y se registra la alerta interna correspondiente. Mientras la condición permanece activa, el patrón evoluciona a sustained. Cuando la evidencia deja de sostenerse y se cumple la ventana de resolución, el episodio pasa a resolved y posteriormente retorna a inactive. Si la evidencia inicial resulta insuficiente o no persiste durante la ventana de confirmación, el patrón vuelve a inactive sin generar una alerta.

##### 17.3.8.3. Motor de evaluación de patrones de riesgo

El motor de evaluación de patrones de riesgo es el componente lógico del plano de control encargado de transformar evidencia perceptiva normalizada en estados de patrón, episodios y alertas internas. No procesa imágenes ni ejecuta inferencia OVD; consume los eventos publicados por el plano de medios, consulta las definiciones activas de patrón declaradas en la configuración experimental y actualiza el estado correspondiente dentro de la corrida.

Su función arquitectónica es cerrar la brecha entre detección visual y salida operativa asistiva. Una detección indica que el modelo observó una evidencia en un frame o instante determinado; un patrón confirmado indica que esa evidencia fue evaluada bajo criterios de persistencia, umbral, histéresis y, cuando corresponda, reglas espaciales o contextuales. Por lo tanto, el motor constituye la frontera donde la evidencia perceptiva deja de ser una salida aislada del detector y pasa a formar parte de una interpretación temporal trazable.

El motor se diseña para admitir el catálogo completo de patrones del prototipo, pero su activación efectiva depende de la configuración de corrida, los módulos habilitados y la disponibilidad de evidencia suficiente. De este modo, la arquitectura puede incorporar progresivamente patrones de mayor complejidad sin modificar la lógica central del plano de control.

###### 17.3.8.3.1. Patrón de riesgo como unidad evaluable

El motor no evalúa condiciones de riesgo sueltas, sino patrones de riesgo activos. Cada patrón referencia una condición del catálogo y define cómo esa condición debe ser evaluada durante la corrida. De este modo, la condición conserva el significado semántico del riesgo observado, mientras que el patrón agrega criterios operativos de activación, sostenimiento y cierre.

Esta separación evita que el sistema dependa de reglas rígidas incorporadas directamente en el código. Una misma condición puede evaluarse mediante distintas estrategias de evidencia, umbrales, ventanas temporales o dependencias opcionales, siempre que la configuración experimental lo declare. El patrón funciona, por lo tanto, como una definición evaluable: indica qué evidencia acepta, durante cuánto tiempo debe sostenerse, qué severidad tiene, qué histéresis aplica y qué evento debe emitirse cuando cambia de estado. La codificación PR-01 a PR-06 identifica cada patrón y lo mantiene distinguible de la condición observable que evalúa (CR-01 a CR-06): una nombra el fenómeno, la otra la regla operativa que decide cuándo se lo considera sostenido.

• **Identificación del patrón**. Código, condición asociada y versión.

• Evidencia requerida. Detecciones o relaciones necesarias. En el núcleo: person y evidencia positiva de helmet o vest.

• Granularidad. Por escena (scene) o por sujeto (subject).

• **Criterio temporal**. Ventana de confirmación expresada en milisegundos, declarada por patrón.

• **Histéresis y cierre**. Ventana de resolución expresada en milisegundos, declarada por patrón.

• **Umbrales y precondiciones de evidencia**. Confianza mínima del sujeto y del EPP, y área mínima del sujeto, declaradas por patrón; umbrales de postproceso declarados en la configuración del plano de medios.

• **Región de evaluación**. Franja vertical y margen lateral relativos a la caja del sujeto, declarados por patrón (región cefálica para PR-01; torso para PR-02).

• **Severidad configurada**. Severidad conceptual asignada por patrón desde el catálogo metodológico.

• **Dependencias opcionales**. Identidad temporal, zonas y relaciones entre entidades.

• **Salida esperada**. Transición de estado, alerta interna y eventos asociados.

**Nota.** La tabla define los componentes de una definición de patrón de riesgo. Los valores adoptados para el núcleo validable se documentan junto a la configuración efectiva en la sección 17.4.6. Los tiempos se expresan en milisegundos para conservar su significado ante distintas cadencias de procesamiento.

En particular, la severidad no debe derivarse de una detección aislada en un frame, sino de la definición del patrón y del catálogo metodológico consolidado. En el núcleo del prototipo, este valor es estático por corrida: orienta la interpretación de prioridad y latencia esperada, pero no se recalcula frame a frame ni depende de la inferencia OVD, de la publicación de evidencia perceptiva ni de los mecanismos de distribución externa. Cualquier ajuste posterior de severidad por zona, proximidad, persistencia o combinación de condiciones corresponde a extensiones condicionadas y debe declararse explícitamente en la configuración de corrida.

###### 17.3.8.3.2. Memoria temporal y ciclo de evaluación

La granularidad de la memoria temporal es un parámetro explícito de la definición de patrón. Bajo granularidad de escena, el estado se indexa por (patrón, fuente) y evalúa la continuidad de la condición en la escena. Bajo granularidad de sujeto, se indexa por (patrón, fuente, identidad) y exige una identidad temporal válida.

El identificador de detección es local a una unidad visual y no constituye identidad entre frames. La granularidad de sujeto sólo puede utilizar una identidad producida por un componente de seguimiento o por un decorador equivalente del plano de control. La capacidad puede habilitarse por configuración sin modificar el contrato de percepción; la identidad resultante se conserva en los artefactos del control, no en el JSONL ordinario del plano de medios.

La granularidad de escena sostiene una afirmación precisa: la condición persiste en la escena. No permite concluir que el mismo sujeto sostuvo el riesgo durante toda la ventana, porque una rotación de personas podría mantener la condición de forma continua. Esa segunda afirmación requiere granularidad de sujeto.

La exclusión de métricas MOT no elimina esta capacidad. La arquitectura separa la identidad necesaria para indexar el estado del patrón de la evaluación formal del desempeño de seguimiento.

El ciclo de evaluación selecciona evidencias, actualiza la memoria, aplica la ventana de confirmación y la histéresis, registra la transición y conserva la causa. Los descartes de fuente, huecos temporales y pérdida de identidad se distinguen de la ausencia real de evidencia.

###### 17.3.8.3.3. Evaluación según niveles de complejidad del catálogo

El motor debe respetar la clasificación metodológica de condiciones por nivel de complejidad ya definida en el desarrollo metodológico. Desde el diseño arquitectónico, esa clasificación se traduce en distintos requisitos de evaluación: algunos patrones pueden resolverse con evidencia perceptiva y persistencia temporal simple, mientras que otros sólo deben activarse cuando la corrida habilite insumos adicionales como tracking, zonas parametrizadas o reglas espaciales.

Esta diferenciación permite diseñar un motor único sin sobredimensionar el prototipo experimental. La arquitectura mantiene una lógica común de evaluación, pero adapta sus entradas y criterios según el patrón activo y la configuración de corrida. De este modo, el plano de control puede incorporar condiciones más complejas sin rediseñarse, siempre que existan los insumos necesarios para evaluarlas de manera trazable.

**Tabla 44**

*Diseño del motor de patrones según condición de riesgo*

| **Patrón y condición asociada** | **Evidencia y regla de evaluación** | **Dependencias arquitectónicas** | **Tratamiento en el prototipo** |
| --- | --- | --- | --- |
| PR-01 / CR-01 — Persona sin casco | Detecciones positivas de person y helmet. Para cada persona, el plano de control evalúa casco en la región cefálica y estabiliza la ausencia inferida mediante confianza, persistencia e histéresis. | Eventos de percepción, coordenadas comparables y referencia temporal. La granularidad de sujeto requiere identidad temporal válida; la de escena no. | Núcleo validable. Produce estados candidato, confirmado, sostenido y resuelto, además de una alerta interna trazable por episodio. |
| PR-02 / CR-02 — Persona sin chaleco reflectivo | Detecciones positivas de person y vest. Para cada persona, el plano de control evalúa chaleco en la región del torso y estabiliza la ausencia inferida mediante los criterios temporales configurados. | Eventos de percepción, coordenadas comparables y referencia temporal. Comparte la misma frontera contractual que PR-01. | Núcleo validable. Se evalúa mediante la misma cadena arquitectónica, con severidad y ventanas propias. |
| PR-03 / CR-03 — Trabajo en altura sin anticaídas visible | Evidencia de persona en altura o sobre estructura elevada, junto con ausencia o baja evidencia de sistema anticaídas visible. El motor requiere validar contexto espacial antes de confirmar. | OVD sobre entidades o atributos, reglas espaciales intra-frame y evidencia visual suficiente del escenario. | Extensión condicionada. No bloquea el núcleo; sólo debe activarse si existen datos o escenas que permitan evaluar la condición completa. |
| PR-04 / CR-04 — Borde elevado desprotegido con personas próximas | Evidencia de borde, plataforma o zona elevada, ausencia de baranda o protección colectiva y presencia de personas próximas. El motor evalúa proximidad y condición de protección. | OVD de entidades del entorno, reglas espaciales, posible parametrización de regiones y cámara con perspectiva adecuada. | Extensión condicionada. Puede reportarse parcialmente si sólo se detectan componentes visuales sin validar la condición completa. |
| PR-05 / CR-05 — Maquinaria cerca de peatones | Evidencia de maquinaria y personas con relación de proximidad sostenida. El motor evalúa distancia relativa, duración del acercamiento y persistencia del episodio. | OVD de entidades, seguimiento temporal o asociación equivalente, reglas de proximidad y métricas de continuidad. | Condicionado a módulo contextual. No pertenece al núcleo; requiere instrumentación temporal y control de falsos positivos relacionales. |
| PR-06 / CR-06 — Persona en zona restringida | Evidencia de persona dentro de un polígono o zona definida externamente. El motor evalúa permanencia, entrada, salida y cierre por ausencia sostenida. | Cámara fija o geometría controlada, polígono de zona, OVD de persona y, preferentemente, tracking o asociación temporal. | Condicionado a escenario EBE controlado o fuente fija. Requiere parametrización explícita de zona en la configuración de corrida. |

***Nota****.* La tabla diseña el comportamiento esperado del motor frente al catálogo completo de patrones. El tratamiento “núcleo validable” identifica patrones obligatorios para el prototipo experimental; el tratamiento “extensión condicionada” indica capacidades previstas que sólo deben habilitarse cuando existan datos, módulos e instrumentación suficientes.

###### 17.3.8.3.4. Salidas, episodios y trazabilidad del motor

La salida principal del motor no es una alerta aislada, sino una secuencia de eventos derivados que describen el ciclo de vida del patrón: inicio de candidato, confirmación, sostenimiento, resolución o descarte por evidencia insuficiente. La alerta interna se registra sólo cuando una transición válida confirma el patrón. Esta decisión evita que el sistema emita alertas por cada frame positivo y permite analizar episodios con inicio, duración, evidencia causal y cierre.

Cada transición debe conservar trazabilidad suficiente para explicar su origen: configuración de corrida, patrón evaluado, condición asociada, evidencia considerada, ventana temporal, umbrales aplicados, estado previo, estado nuevo y referencia temporal. Esta información permite reconstruir por qué una alerta fue generada, por qué un episodio se resolvió, qué evidencia fue descartada y qué parámetros condicionaron el resultado.

Las métricas operativas del plano de control se apoyan en estas transiciones: el tiempo hasta la primera detección (TTFD) se ancla en la primera evidencia perceptiva relevante; la latencia de alerta (t_alert-system) se cierra con el registro de la alerta interna que sigue a la transición a confirmado; la tasa de detección sostenida (SDR) se calcula sobre la continuidad del episodio; y los errores o descartes permiten distinguir una ausencia real de evidencia de una falla técnica o de una pérdida por muestreo.

De esta manera, el motor de evaluación de patrones permite que la arquitectura sostenga una cadena operativa completa: detección OVD, evidencia perceptiva normalizada, patrón candidato, patrón confirmado, alerta interna por episodio, sostenimiento, resolución y reconstrucción experimental. Con este diseño, CR-01 y CR-02 pueden implementarse como núcleo validable, mientras que los patrones más complejos permanecen incorporables sin alterar la separación entre plano de medios y plano de control.

##### 17.3.8.4. Transporte, persistencia y trazabilidad experimental

La arquitectura diferencia el canal de transporte del repositorio persistente. El canal desacopla productores y consumidores; el repositorio conserva los hechos necesarios para reconstruir la corrida. Esta separación evita atribuir durabilidad a un mecanismo de mensajería diseñado para baja latencia.

El repositorio es la fuente de verdad. Cada evento de percepción se escribe en un archivo JSONL de sólo adición antes de publicarse. Los cambios de estado, alertas, métricas y errores siguen la misma regla en sus componentes respectivos. Si el canal falla, el hecho persistido permanece disponible para relectura.

En el camino de ejecución en vivo correspondiente a EBE, el canal adopta ZeroMQ con patrón publicador-suscriptor, msgpack, tópicos por tipo de evento y un número de secuencia monótono dentro del envoltorio versionado del bus. El payload publicado corresponde al mismo contenido lógico persistido, de modo que la corrida pueda releerse posteriormente por el camino diferido sin redefinir la evidencia.

El consumidor debe suscribirse antes de que el productor publique. Por ello, una corrida en vivo se inicia primero en el plano de control y luego en el plano de medios. La respuesta de creación del control implica disponibilidad del consumidor y el orquestador verifica esa precondición.

La pérdida se detecta mediante huecos de secuencia. Un hueco incrementa bus_dropped_events, degrada la corrida y queda expuesto en el reporte; nunca se interpreta como ausencia de evidencia en la escena.

El cierre de la corrida se propaga mediante un evento de ciclo de vida cuyo hito de finalización delimita el final lógico y permite cerrar consumidores, consolidar artefactos y distinguir un fin normal de una interrupción.

La sustitución futura por un broker conserva la misma frontera contractual. La durabilidad, la re-evaluación y la causalidad no dependen de la tecnología del canal, sino de la regla persistir-primero y de los esquemas versionados.

#### 17.3.9. Integración entre condición, estrategia de detección, patrón y alerta

Esta sección precisa cómo las condiciones de riesgo definidas metodológicamente se materializan dentro de la arquitectura. Su finalidad es vincular la condición observable con una estrategia de detección, la evidencia perceptiva publicada por el plano de medios, la evaluación del patrón en el plano de control y el registro de una alerta interna por episodio. De este modo, la plataforma evita tratar los prompts como condiciones completas o las detecciones individuales como alertas directas, conservando una cadena causal trazable entre percepción, evaluación y salida asistiva.

##### 17.3.9.1. Cadena de traducción arquitectónica

La cadena de traducción comienza con una condición observable del catálogo metodológico. Esa condición define qué fenómeno se desea monitorear, pero no determina por sí misma cómo debe detectarse. La estrategia de detección cumple esa función: establece si la evidencia se buscará mediante un prompt directo, una combinación de consultas, evidencia auxiliar o reglas contextuales habilitadas por la configuración de corrida.

El plano de medios aplica la estrategia configurada y publica evidencia perceptiva normalizada. Esa evidencia queda asociada a la corrida, la fuente, el modelo, los prompts activos, los umbrales y la referencia temporal correspondiente. Sin embargo, todavía no constituye una alerta. Su función es alimentar al plano de control con información comparable y trazable.

El plano de control evalúa esa evidencia mediante el patrón correspondiente y, cuando la evaluación confirma el episodio, registra una alerta interna. Esa alerta es una salida asistiva del sistema: no equivale a una notificación externa ni a una certificación normativa.

**Figura 4.5**

*Cadena de traducción entre condición, estrategia, evidencia, patrón y alerta*

⟦FIGURA: no extraída — ver el .docx⟧

**Nota.** La figura muestra cómo una condición definida metodológicamente se materializa en la arquitectura. La estrategia orienta la producción de evidencia en el plano de medios; el patrón evalúa esa evidencia en el plano de control; y la alerta interna registra el episodio confirmado.

##### 17.3.9.2. Estrategia adoptada para el núcleo validable

Para el núcleo validable se adopta la estrategia indirecta con inferencia espacial de ausencia (E-IND). La frontera que esa elección fija es explícita: el plano de medios informa qué entidades observó, dónde y con qué confianza; el plano de control decide si la evidencia del elemento de protección se asocia al sujeto, construye el estado evaluable de la condición y lo estabiliza antes de registrar una alerta.

La estrategia se adopta por auditabilidad: cada evaluación puede reconstruirse a partir de la caja del sujeto, la región analizada, las detecciones de protección, los umbrales y la regla aplicada, de modo que la ausencia no se presenta como una conclusión opaca del modelo. La detección directa (E-DIR) y las variantes híbridas (E-HYB) se conservan como ramas comparativas configurables, con conjuntos de prompts y reglas identificados por separado; comparten los contratos de publicación, evaluación temporal y registro, de modo que la comparación no requiera alterar la arquitectura central.

##### 17.3.9.3. Comparabilidad entre estrategias

Para que la comparación entre variantes sea posible, cada evidencia publicada conserva el vínculo con la condición que representa, la estrategia de detección utilizada y la configuración efectiva de la corrida. Una misma condición puede evaluarse con distintas estrategias sin alterar la semántica del sistema, siempre que la corrida declare la variante utilizada y los eventos resultantes conserven esa referencia. Es esa referencia declarada, y no una reinterpretación posterior de los artefactos, la que permite atribuir una diferencia de resultados a la estrategia evaluada y no a un cambio no declarado en la cadena.

#### 17.3.10. Distribución de alertas confirmadas

La alerta interna es el hecho terminal del plano de control, pero todavía no es un aviso. Esta sección define el tramo que la convierte en entregas observables sin incorporar la comunicación a la ruta que la produjo.

##### 17.3.10.1. Función arquitectónica de la distribución

La función arquitectónica de la distribución es transformar una alerta ya confirmada en intentos de entrega registrados, sin participar del razonamiento que la produjo. El plano de control publica cada alerta confirmada en un bus de alertas dedicado; el módulo de distribución la consume desde allí, aplica la política de notificación y registra el resultado de cada intento. No constituye un tercer plano ni un cuarto rol funcional: es un módulo desacoplado, y esa condición es la que impide que la indisponibilidad de un canal externo se propague al motor de patrones.

El pipeline de distribución comprende una fuente de alertas, una política de notificación, un sobre versionado, un adaptador de canal y un ledger de entregas. La misma lógica admite relectura DBE desde artefactos persistidos y consumo EBE desde el bus de alertas, sin modificar la semántica de la alerta de entrada.

La política ordinaria prioriza trazabilidad, idempotencia y operación no bloqueante. Una falla del canal genera un resultado de entrega y un error interpretable, pero no invalida ni elimina la alerta interna.

##### 17.3.10.2. Consumidores, canales y control de ciclo de vida.

El tramo de distribución separa el dato del gobierno. Las alertas confirmadas llegan por el bus de alertas dedicado, en sentido único desde el plano de control. Las órdenes de ciclo de vida, en cambio, llegan por una interfaz de gobierno propia del módulo, que permite crear, consultar, cancelar y descartar corridas de entrega. La interfaz de inspección y el orquestador experimental lo gobiernan por esa vía —del mismo modo que a los otros módulos— y nunca consumen el bus directamente. Para la relectura DBE el módulo conserva una entrada offline sobre alertas persistidas. Ambos caminos utilizan los mismos contratos de alerta interna, sobre de notificación y registro de entrega, por lo que la modalidad de ejecución no modifica la semántica de la alerta ni del resultado de entrega.

La Tabla 45 distingue los consumidores del evento confirmado. Ninguno puede modificar retrospectivamente el patrón, la alerta interna o su referencia temporal.

**Tabla 45**

*Consumidores y salidas del tramo de distribución*

| **Consumidor o salida** | **Uso previsto** | **Tratamiento arquitectónico** |
| --- | --- | --- |
| MQTT QoS 1 | Publicar el sobre de notificación y esperar confirmación de entrega del broker. | Canal de entrega mediante adaptador; el resultado queda asentado como registro de entrega. |
| Interfaz de inspección | Mostrar alerta, política aplicada, intento y resultado de entrega. | Proyección de consulta; no consume el bus de percepción ni confirma patrones. |
| Reporte experimental | Consolidar conteos por resultado de entrega, errores y latencia del tramo. | Se calcula desde el ledger y se mantiene separado de las métricas de alerta interna. |
| Relectura DBE | Distribuir alertas ya persistidas de una corrida. | Debe ser idempotente: reprocesar el mismo evento no duplica entregas. |
| Canales adicionales | Correo, webhook u otras integraciones futuras. | Punto de extensión por adaptador; no forma parte del núcleo ni altera los contratos existentes. |

*Nota.* El módulo de distribución conserva su propio estado operativo y su ledger; no utiliza el almacenamiento continuo de video ni requiere acceso a frames crudos.

##### 17.3.10.3. Política, medición y límites de interpretación

El conjunto de patrones adoptado no suprime confirmaciones: cada alerta interna se registra para conservar la dinámica real del episodio. La decisión es deliberada —el motor dispone de control de re-confirmación por patrón y sujeto y el núcleo lo deja inactivo— porque un motor que suprimiera dejaría de reflejar la duración del episodio y no permitiría distinguir una condición que persiste de una que se resolvió.

La supresión de re-notificación se reubica en la política del módulo de distribución, y al reubicarse cambia de granularidad: el motor la aplicaría por patrón y sujeto, mientras que la política de entrega aplica una ventana de silencio por condición y fuente, porque para una notificación asistiva lo relevante es que esa condición en esa cámara ya fue avisada. La agrupación de avisos y la limitación de tasa quedan como punto de extensión de la política. Una alerta suprimida para comunicación existió y continúa siendo medible: las re-alertas de un episodio activo se informan por separado y no se computan como falsos positivos, de modo que una decisión de comunicación no altera la precisión del motor.

El ledger de entregas aplica una clave de idempotencia por notificación y canal, es de sólo agregado y acumula entre corridas: al reutilizar un directorio de salida la generación anterior se archiva íntegra y la deduplicación considera todas las generaciones, por lo que un reprocesamiento no vuelve a entregar lo ya entregado. Cada fila conserva número de intento, marca temporal, resultado, motivo de error y confirmación del canal, y distingue cinco resultados: entrega exitosa, supresión por política, descarte por duplicado, falla de un intento y descarte definitivo por agotamiento de reintentos. La unidad de conteo del tramo es la notificación y no la fila: una notificación no entregada deja una fila por cada intento más la del descarte definitivo.

Cada fila registra además la modalidad en que se midió t_alert-notification, y la latencia del tramo se informa siempre separada por modalidad: en relectura diferida el intervalo incorpora el ritmo de reinyección de las alertas persistidas, que es propiedad del reprocesamiento y no del canal.

#### 17.3.11. Contratos e interfaces internas

Los contratos estabilizan la semántica de intercambio entre componentes: definen qué información cruza cada frontera y bajo qué versión. En la arquitectura consolidada del núcleo se expresan como modelos de datos versionados, con serializaciones explícitas e interfaces concretas, y cada uno queda asociado a una corrida para que productores y consumidores puedan evolucionar de forma independiente. La versión viaja dentro del payload y no en el envoltorio de transporte: el canal puede cambiar sin que el hecho persistido pierda la identificación de su esquema. Las capacidades futuras deben evolucionar de forma aditiva sin romper la lectura de corridas históricas.

##### 17.3.11.1. Fronteras informacionales de intercambio

Cada frontera existe para proteger una decisión. La del gobierno del experimento evita una configuración monolítica y vincula ciclos de vida independientes. La de entrada visual unifica los dos escenarios sin ocultar su temporalidad. La de salida del plano de medios encapsula la heterogeneidad del detector. La de entrada del plano de control obliga a evaluar reglas sobre eventos y no sobre frames crudos. La de salida del plano de control diferencia detección, patrón y alerta. La de distribución mantiene la comunicación y la idempotencia aguas abajo de la alerta interna. Y la de referencia y soporte sostiene la medición y la reconstrucción con estados de aplicabilidad. Las fronteras son lógicas: no prescriben que cada responsabilidad se despliegue en una máquina, proceso o contenedor independiente.

##### 17.3.11.2. Contratos mínimos e interfaces

Todo contrato declara su identidad de esquema y su versión como primer elemento del payload.

**Tabla 46**

*Contratos mínimos para la ejecución experimental*

| **Contrato** | **Función arquitectónica** | **Información mínima** |
| --- | --- | --- |
| Manifiesto de experimento | Gobierna la ejecución experimental. | experiment_id, referencias de configuración, runs por componente, orden de inicio, modelo, prompt set, pattern set y versión. |
| SourceDefinition | Describe la fuente visual. | source_id, tipo, naturaleza temporal, ubicación o dispositivo, resolución, ritmo y restricciones. |
| ModelProfile | Define el adaptador y perfil de inferencia. | Modelo, checkpoint, backend, dispositivo, precisión y parámetros de entrada. |
| PromptDefinition | Versiona el vocabulario. | prompt_set_id, clase, texto, rol, estrategia y umbrales asociados. |
| FrameMetadata | Identifica la unidad visual. | unit_id, source_id, índice, timestamp, tamaño y transformaciones. |
| PerceptionEvent | Publica evidencia perceptiva normalizada. | run, unidad, fuente, modelo, prompts, detecciones y timing. |
| PatternDefinition | Declara la condición evaluable. | Patrón, condición, sujeto, EPP requerido, granularidad, región, umbrales, confirmación, resolución y severidad. |
| PatternStateChanged | Registra la transición del motor. | Estado anterior y nuevo, evidencia, sujeto o escena y tiempos. |
| AlertEvent | Registra la confirmación de un episodio. | Identificador determinista, patrón, fuente, evidencia, severidad y hito de registro. |
| MetricSample / ErrorEvent | Conserva observabilidad y fallas. | Nombre, valor, unidad, tramo, reloj, status, cause, error y contexto. |
| Referencia temporal de evaluación | Anota episodios por clip. | clip_id, condición, inicio y fin en ms, eventos subumbral, tolerancia, condición negativa y procedencia. |
| NotificationEnvelope | Prepara una alerta para entrega. | Alerta, política, canal, intento y clave de idempotencia. |
| DeliveryRecord | Registra el resultado del canal. | Resultado de entrega, timestamp, confirmación, error y latencia del tramo. |

*Nota.* Los contratos de referencia temporal y distribución tienen el mismo estatuto formal que los eventos de percepción y control: una medición o entrega no es reproducible si su entrada carece de versión y procedencia.

El evento central del sistema es el evento de percepción. Agrupa la identidad de esquema versionada, la corrida, la unidad visual, la fuente, el modelo, los prompts, las detecciones y los tiempos. Cada detección conserva etiqueta, prompt, confianza, caja en píxeles y normalizada y área. detection_id sólo identifica una detección dentro de la unidad visual; no constituye identidad entre frames. Los campos opcionales se incorporan de forma aditiva y se omiten cuando no están disponibles.

La referencia temporal de evaluación impone dos invariantes de validez. Primero, la identidad de la fuente de la corrida y la del clip anotado deben coincidir; para el banco temporal se utiliza source_id = clip_id. Segundo, la incertidumbre no fabrica una infracción: cuando el estado del EPP no es juzgable, el episodio no se extiende como violación.

La cadena temporal conserva cinco hitos por alerta: primera evidencia positiva —identificada por unit_id—, transición a candidato, transición a confirmado, registro de la alerta interna y, cuando existe distribución, confirmación de entrega. Estos hitos permiten medir cada tramo sin mezclar relojes ni poblaciones.

##### 17.3.11.3. Criterios de evolución durante la implementación experimental

La superficie de crecimiento del evento de percepción se mantiene acotada y separada de las reglas de riesgo. La identidad temporal de sujeto es un campo opcional y la única identidad válida entre frames: el contrato la admite y el plano de control puede materializarla por configuración, sin que el plano de medios necesite emitirla y sin mezclar esa capacidad con las métricas de seguimiento. Velocidad, dirección, puntos clave de pose y máscaras de segmentación quedan previstos como campos opcionales que no modifican la semántica mínima del evento ni desplazan al bounding box. Las relaciones entre sujeto, evidencia de soporte y clase ausente, en cambio, pertenecen al plano de control: el plano de medios publica detecciones individuales.

#### 17.3.12. Trazabilidad experimental y minimización de evidencia visual

La trazabilidad experimental permite reconstruir cómo una corrida produjo una alerta interna. Para ello, la arquitectura debe conservar la relación entre configuración de corrida, fuente visual, modelo utilizado, prompts activos, evidencia perceptiva, transición de estado del patrón, alerta registrada y métricas o errores asociados. Sin esa relación, una alerta pierde valor experimental porque no puede auditarse, compararse ni analizarse con suficiente rigor.

En continuidad con los contratos versionados definidos en la sección anterior, esta sección no vuelve a especificar estructuras de intercambio, sino que precisa qué hechos deben conservarse y bajo qué política se gestiona la evidencia visual. El objetivo es sostener la interpretación de resultados sin convertir la trazabilidad en almacenamiento indiscriminado de video ni ampliar el alcance del prototipo experimental.

##### 17.3.12.1. Repositorio de eventos para reconstrucción experimental

El repositorio utiliza archivos JSONL de sólo adición por corrida y por tipo de hecho. La decisión principal continúa siendo impedir la sobrescritura silenciosa; la materialización elegida agrega una representación simple, inspeccionable y re-evaluable sin introducir una base de datos como dependencia del núcleo.

Cada corrida conserva configuración efectiva, manifiesto, procedencia y versión de código junto a detecciones, métricas, errores, transiciones y alertas. El soporte experimental agrupa los runs de los componentes bajo experiment_id, copia los artefactos livianos y referencia los de mayor volumen.

Toda alerta puede reconstruirse hasta la configuración efectiva, el conjunto de prompts, el modelo, la fuente y la versión de código que la produjeron. La persistencia no requiere video crudo continuo y mantiene separados los hechos originales de sus proyecciones tabulares o reportes.

##### 17.3.12.2. Hechos persistibles mínimos

Los hechos persistibles mínimos representan aquello que debe conservarse para interpretar una corrida y reconstruir una alerta interna. No constituyen una nueva lista de contratos ni una especificación definitiva de base de datos. Mientras los contratos establecidos estabilizan el intercambio entre responsabilidades, los hechos persistibles establecen qué información debe quedar disponible para análisis posterior, comparación entre corridas y reconstrucción de evidencia. Dado que todos los elementos incluidos en la tabla forman parte del mínimo necesario, no se distingue un carácter obligatorio fila por fila.

**Tabla 47**

*Hechos persistibles mínimos para reconstrucción experimental*

| **Hecho persistible mínimo** | **Uso en reconstrucción** |
| --- | --- |
| Inicio y cierre de corrida | Delimita la ejecución y vincula los hechos a los identificadores de experimento y de corrida. |
| Manifiesto y configuraciones efectivas | Reconstruye escenario, fuente, modelo, prompts, patrones, módulos, versiones y políticas aplicadas. |
| Procedencia e identidad de fuente | Conserva dataset o clip, partición, huella y la invariante source_id = clip_id cuando existe referencia temporal. |
| Eventos de percepción | Permiten reconstruir detecciones, unidad visual, modelo, prompt, coordenadas, puntajes y tiempos del plano de medios. |
| Unidades omitidas o descartadas | Explican pérdida de cobertura temporal, control de ritmo, saturación o degradación. |
| Cambios de estado del patrón | Reconstruyen candidato, confirmado, sostenido y resuelto, con evidencia y tiempos. |
| Primera evidencia positiva | Registra unit_id y tiempo de la evidencia que inicia la cadena causal entre planos. |
| Alertas internas | Identifican episodio, patrón, severidad, sujeto o escena, evidencia causal y momento de registro. |
| Entregas de distribución | Conservan canal, resultado, intento, idempotencia y confirmación de entrega cuando el tramo está habilitado. |
| Métricas y estado de aplicabilidad | Distinguen valores calculados, no calculados, no aplicables o no interpretables, siempre con causa. |
| Errores y anomalías | Permiten explicar fallas de fuente, inferencia, transporte, persistencia, evaluación o entrega. |
| Referencias de evidencia visual controlada | Vinculan capturas o clips autorizados sin convertir el video crudo continuo en mecanismo ordinario de trazabilidad. |

**Nota.** La tabla expresa hechos mínimos necesarios para reconstrucción experimental, no servicios ni clases de implementación. Los hechos asociados a seguimiento temporal, zonas, distribución externa de alertas, adaptación de modelos o evidencia visual controlada se incorporan sólo cuando la corrida habilita esas capacidades; no forman parte del conjunto mínimo para CR-01 y CR-02.

Esta selección prioriza la reconstrucción de la cadena causal de la alerta. Una detección aislada no es suficiente para explicar un episodio; debe poder relacionarse con la configuración que la produjo, el patrón que la evaluó, la transición que confirmó la condición y las métricas o anomalías que condicionaron el resultado. Por esa razón, los errores y descartes relevantes tienen el mismo valor interpretativo que los eventos funcionales: permiten distinguir una ausencia real de evidencia de una falla técnica, un descarte por muestreo o una limitación de la fuente.

Las extensiones condicionadas deben mantener esta lógica. Si se incorpora seguimiento temporal, zonas, reglas espaciales, notificaciones externas o adaptación de modelos, esos hechos podrán persistirse como información adicional de la corrida. Sin embargo, no deben desplazar la cadena mínima de reconstrucción ni convertir capacidades exploratorias en requisitos del núcleo experimental.

##### 17.3.12.3. Política de evidencia visual mínima

La arquitectura adopta una política de minimización de evidencia visual. En el comportamiento ordinario del prototipo experimental, la trazabilidad se apoya en identificadores, metadatos, eventos, métricas, coordenadas, referencias temporales y relaciones causales entre hechos persistidos. El almacenamiento continuo de video crudo no forma parte del flujo base, porque aumenta volumen, complejidad y riesgo de privacidad sin ser necesario para reconstruir la mayoría de las decisiones experimentales.

Cuando se requiera evidencia visual para revisión técnica, validación o comunicación académica, ésta debe conservarse como artefacto controlado: snapshot, recorte anotado, clip breve, hash, referencia a archivo o vínculo asociado a una alerta o corrida específica. Su uso debe estar justificado por la finalidad experimental y no reemplaza métricas, eventos persistidos ni criterios explícitos de evaluación.

Esta decisión preserva el carácter asistivo y no identificatorio de la plataforma. El sistema no realiza reconocimiento facial, no identifica nominalmente a trabajadores, no extrae biometría y no emite decisiones normativas autónomas. La alerta interna sólo orienta la atención humana sobre una condición visualmente observable; la interpretación final y cualquier acción preventiva permanecen fuera del sistema automatizado.

#### 17.3.13. Observabilidad arquitectónica e instrumentación de métricas

La observabilidad forma parte del contrato experimental. Cada métrica debe declarar la señal que utiliza, el inicio y el cierre del reloj, la unidad, la población y la condición de aplicabilidad. Cuando una medición no tiene significado, la plataforma conserva la causa en lugar de publicar cero u omitir el campo.

##### 17.3.13.1. Materialización arquitectónica de las métricas

**Tabla 48**

*Métricas y evidencias por tramo arquitectónico*

| **Tramo** | **Punto de medición** | **Métricas o evidencias** |
| --- | --- | --- |
| Captura y host | Captura física, timestamp de fuente y dequeue en el host. | capture_to_host, jitter y disponibilidad temporal, cuando existe ancla compatible. |
| Plano de medios | Dequeue, normalización, inferencia, postproceso y publicación. | G2A, latencia de inferencia, FPS efectivo, throughput y descartes. |
| Bus media-control | Publicación, secuencia y recepción. | Huecos de seq, integridad, atraso y correlación por unit_id. |
| Plano de control | Primera evidencia, candidato, confirmado, alerta y resolución. | TTFD, t_alert-system, latencia interna, SDR, transiciones y re-alertas. |
| Distribución | Disponibilidad de alerta, intento y confirmación del canal. | t_alert-notification, resultados de entrega, supresiones, duplicados y errores. |
| Soporte experimental | Consolidación por corrida y entorno. | Recursos, estados de aplicabilidad, causas, robustez y reporte reconstruible. |

*Nota.* La cadena temporal completa se informa por tramos. Los percentiles de tramos diferentes no son aditivos y no deben sumarse para fabricar una latencia de extremo a extremo.

##### 17.3.13.2. Definiciones operacionales y criterio de relojes

**Tabla 49**

*Diccionario de métricas: definiciones operacionales*

| **Métrica** | **Inicio** | **Cierre** | **Unidad y aplicación** |
| --- | --- | --- | --- |
| capture_to_host | Captura física o timestamp equivalente de la fuente | Dequeue de la unidad en el host | ms; sólo sobre fuente en vivo con ancla temporal interpretable. |
| G2A | Dequeue de la unidad en el host de procesamiento | Resultado algorítmico o alerta asociada a esa unidad | ms, p50/p95/p99; exige un único dominio de reloj. No empieza en el fotón. |
| TTFD | Inicio anotado del episodio | Primera evidencia positiva | ms; requiere la referencia temporal anotada. Si no hay evidencia, es nulo con causa. |
| t_alert-system | Inicio anotado del episodio | Registro de la alerta interna | ms; se reporta por campaña y condición. |
| Latencia interna | Primera evidencia positiva | Registro de la alerta interna | ms; separa cómputo y espera deliberada por persistencia. |
| SDR | Episodio anotado | Cobertura positiva dentro del episodio | Proporción [0,1]; sólo comparable dentro de una misma cadencia. |
| Precisión / exhaustividad / F1 de alertas | Alertas y episodios evaluables | Matching por episodio | Proporción; los negativos no integran P/R/F1 y las re-alertas no son FP. |
| t_alert-notification | Alerta disponible en el bus de distribución | Confirmación de entrega del canal | ms; no aplica sin distribución y no se suma a t_alert-system. |

Las latencias intra-host utilizan reloj monotónico local. Los monotónicos de hosts distintos no se restan. Cuando un trayecto cruza dominios de reloj sin una sincronización válida, la métrica se declara not_interpretable con su causa.

El criterio de detección positiva se comparte con el motor de patrones. La evaluación no reimplementa una segunda definición de evidencia, lo que evita divergencias silenciosas entre el sistema que decide y el sistema que mide.

##### 17.3.13.3. Señales observables y estados de aplicabilidad

**Tabla 50**

*Señales observables del sistema*

| **Señal observable** | **Origen** | **Uso experimental** |
| --- | --- | --- |
| Timestamps por tramo | Fuente, media, control y distribución. | Calculan latencias y verifican el dominio de reloj. |
| Unidades aceptadas, omitidas o descartadas | Control de ritmo, cola y fuente. | Interpretan cobertura temporal y pérdida de evidencia. |
| Eventos de percepción | Plano de medios. | Correlacionan percepción con fuente, modelo, prompt y unidad. |
| Huecos de secuencia | Bus ZeroMQ. | Detectan pérdida silenciosa y degradan la corrida. |
| Transiciones de patrón | Plano de control. | Reconstruyen persistencia, confirmación y resolución. |
| Alertas y re-alertas | Plano de control. | Delimitan episodios y estabilidad sin confundir repetición con FP. |
| Entregas y resultados de entrega | Distribución. | Separan entrega exitosa, supresión, duplicado y error. |
| Muestras de recursos | Entorno y soporte. | Explican cuellos de botella y diferencias entre corridas. |
| Errores y causas | Instrumentación transversal. | Evitan interpretar una corrida degradada como ausencia de riesgo. |

Cada métrica incluye status y cause. Los estados admitidos son computed, applicable_not_computed, not_applicable y not_interpretable. La plataforma no publica un cero cuando lo correcto es declarar una causa.

Una fuente de imágenes independientes produce not_applicable/non_temporal_source para patrones temporales; un trayecto con monotónicos de dos hosts produce not_interpretable/cross_node_monotonic_clock; una corrida sin referencia produce not_applicable/no_ground_truth; y un TTFD sin detección positiva permanece nulo con causa.

##### 17.3.13.4. Registro de resultados por corrida

El reporte consolida manifiesto, configuraciones efectivas, métricas por tramo, estado de aplicabilidad, alertas, re-alertas, descartes, errores, recursos y limitaciones de interpretación. Cada valor mantiene la condición, el escenario y la población sobre la que se calculó.

t_alert-system integra el diccionario citable de la plataforma. Las métricas de precisión, exhaustividad y F1 de alertas se obtienen mediante el evaluador temporal que conserva denominadores por estrato; no se duplican mediante agregados sin procedencia en el reporte general.

El reporte constituye una proyección de hechos persistidos. Puede regenerarse sin modificar los eventos originales y no se utiliza como fuente de verdad cuando existe el artefacto primario.

#### 17.3.14. Escenarios experimentales DBE y EBE

La definición metodológica de ambos escenarios corresponde a la sección 17.1.4.4; aquí se conservan únicamente sus consecuencias arquitectónicas.

##### 17.3.14.1. DBE como escenario de estabilización reproducible

En DBE, la fuente es regulable y puede releerse bajo la misma configuración; por ello, la arquitectura prioriza identidad estable de unidades, orden lógico, persistencia previa y reconstrucción determinista de eventos, patrones y alertas. Esta propiedad permite estabilizar contratos y comparar configuraciones sin que la variabilidad de captura se convierta en una variable implícita.

##### 17.3.14.2. EBE como escenario de fuente en vivo controlada

En EBE, la fuente opera en vivo y la escena continúa evolucionando aunque el pipeline se retrase; por ello, la arquitectura instrumenta captura o recepción, colas, descartes, jitter, actualidad y dominio de reloj. La compatibilidad de contratos se conserva, pero la interpretación de latencia y cobertura temporal debe incluir los efectos propios de la fuente continua.

##### 17.3.14.3. Equivalencia arquitectónica entre escenarios

DBE y EBE deben converger en la misma arquitectura una vez normalizada la entrada visual. La diferencia entre escenarios se ubica antes y alrededor de la disponibilidad del frame: origen de la fuente, referencia temporal, política de muestreo, control de ritmo e instrumentación de omisiones o descartes. Después de esa frontera, la inferencia OVD, el postproceso, la publicación de evidencia perceptiva, la evaluación de patrones y el registro de alertas internas deben mantener la misma semántica.

Esta equivalencia evita construir dos flujos incompatibles. Si DBE y EBE produjeran contratos distintos o exigieran reglas de patrón diferentes, los resultados dejarían de ser comparables. En cambio, al conservar la misma estructura de eventos, métricas y hechos persistibles, la arquitectura permite analizar qué parte de la variación proviene de la fuente continua y qué parte corresponde al comportamiento del detector o de la evaluación de patrones.

La comparación entre escenarios debe declarar explícitamente qué variables cambiaron. Una corrida DBE y una corrida EBE pueden compartir modelo, prompts, umbrales y reglas de patrón, pero diferir en fuente, temporización, iluminación, compresión o criterio de descarte. Esas diferencias deben registrarse como parte de la configuración y de la observabilidad, no tratarse como detalles secundarios.

##### 17.3.14.4. Comparación arquitectónica entre DBE y EBE

La Tabla 51 resume las diferencias principales entre ambos escenarios desde una lectura arquitectónica. Su finalidad no es repetir la definición metodológica de DBE y EBE, sino mostrar qué decisiones de diseño se derivan de cada modo de evaluación y cómo deben interpretarse sus resultados.

**Tabla 51**

*Comparación arquitectónica entre escenarios DBE y EBE*

| **Dimensión** | **DBE** | **EBE** | **Implicancia arquitectónica** |
| --- | --- | --- | --- |
| Fuente de entrada | Imagen, dataset o vídeo local. | Cámara, RTSP, OAK-D o captura controlada. | La fuente se abstrae mediante metadatos comunes; su naturaleza temporal se declara por separado. |
| Control temporal | Alto; la secuencia puede repetirse bajo condiciones equivalentes. | Menor; intervienen captura, buffers, jitter, decodificación y disponibilidad del último frame. | EBE requiere instrumentar timestamps, colas, descartes y atraso acumulado. |
| Variabilidad externa | Baja o controlada, según cobertura del dataset. | Media o alta, según cámara, red local, códec, iluminación, movimiento, buffers y entorno. | Las diferencias de desempeño no deben atribuirse automáticamente al modelo OVD. |
| Instrumentación adicional | Orden lógico, referencia a dataset o archivo, política de muestreo y frames procesados. | Captura o recepción, profundidad de cola, descartes, jitter, reemplazo de frames y estado de fuente. | La observabilidad debe registrar diferencias temporales para interpretar latencia y cobertura. |
| Métricas prioritarias | Percepción; asociación espacial; y, sólo sobre vídeo temporal, patrones y alertas. | Integridad, capture_to_host, G2A, descartes, alertas y estado de entrega cuando corresponda. | Cada métrica debe declarar su punto de inicio, cierre, reloj y condición de aplicación. |
| Condición de comparabilidad | Misma configuración lógica y fuente reproducible; ground truth cuando corresponda. | Misma configuración lógica, con variabilidad temporal y condiciones de captura documentadas. | La comparación DBE/EBE requiere declarar qué variables permanecen constantes y cuáles cambian. |

***Nota.*** *DBE y EBE se interpretan como escenarios experimentales de una misma arquitectura. La diferencia principal se ubica en la fuente visual, la temporalidad y la instrumentación requerida; los contratos de evidencia, patrón, alerta, métricas y errores deben mantenerse compatibles para preservar comparabilidad experimental.*

Con esta organización, DBE funciona como escenario de estabilización y comparación controlada, mientras que EBE permite observar la integración con fuente en vivo bajo condiciones instrumentadas. La arquitectura no debe privilegiar un escenario mediante contratos diferentes, sino conservar una frontera común de entrada visual normalizada y registrar explícitamente las condiciones que afectan la interpretación de cada corrida.

##### 17.3.14.5. Alcance arquitectónico de EBE

EBE admite cámaras IP por RTSP, la OAK-D Pro PoE y otras fuentes continuas declaradas mediante el mismo adaptador conceptual. La arquitectura contempla tanto el dispositivo candidato como la contingencia con cámara IP convencional; ninguna alternativa modifica los contratos de percepción y control.

El rol EN puede operar como captura, preprocesamiento no semántico o preselección conservadora. La variante de preselección liviana en el borde es opcional, está deshabilitada por defecto y opera con el criterio de degradación segura fijado para las capacidades opcionales del plano de medios: una falla o incertidumbre del preselector no elimina la unidad del flujo principal. Toda transformación, descarte o cambio de resolución se registra.

La comparación entre una corrida DBE sobre archivo y una corrida EBE del mismo contenido exige una ancla común entre tiempo de medio y reloj de pared. Sin esa ancla, el matching temporal contra la referencia temporal se declara no interpretable; la integridad del bus y la relectura offline continúan siendo evaluables por separado.

**Tabla 52**

*Condiciones observables para interpretar EBE*

| **Condición** | **Registro mínimo** | **Impacto** |
| --- | --- | --- |
| Fuente continua | Tipo de cámara o stream, adaptador, source_id y naturaleza temporal. | Distingue captura local, red y participación del EN. |
| Conectividad y transporte | LAN, RTSP u otro mecanismo, codificación y buffering. | Condiciona jitter, atraso y disponibilidad de frames. |
| Timestamps y reloj | Captura, recepción, dequeue y dominio de reloj. | Determina qué latencias son calculables o interpretables. |
| Colas y control de ritmo | Tamaño, profundidad, reemplazos y política de actualidad. | Explica acumulación de atraso, pérdida de continuidad y capacidad de sostener el ritmo. |
| Descartes | Cantidad, causa y unidad afectada. | Evita confundir omisión del pipeline con ausencia de evidencia. |
| Preselección en el borde | Estado de habilitación, criterio, comportamiento fail-open y ledger de decisiones. | Permite comparar preselección contra flujo completo sin ocultar falsos negativos. |
| Degradación | Cortes, jitter, saturación, reloj inválido o fuente irregular. | Obliga a marcar métricas limitadas o no interpretables. |

*Nota.* EBE es un escenario experimental y no una topología fija. La ubicación de servicios y dispositivos se declara por corrida.

##### 17.3.14.6. Naturaleza temporal de la fuente y aplicabilidad

La procedencia DBE o EBE no determina por sí sola si una fuente sostiene razonamiento temporal. Un vídeo de archivo y un stream vivo son temporales; un conjunto de imágenes independientes no lo es. La configuración deriva esta propiedad del tipo de fuente y no permite que el operador la contradiga.

Aplicar una ventana de persistencia sobre imágenes independientes produciría cero alertas por construcción, un resultado indistinguible de la ausencia real de riesgo. Para evitar ese cero silencioso, la evaluación de patrones se declara not_applicable/non_temporal_source. La corrida conserva valor para percepción y asociación espacial, pero no para continuidad o alerta temporal.

Las imágenes permiten afirmar sobre percepción; los clips temporales, sobre estado y episodios; y las fuentes en vivo, además, sobre transporte, actualidad y comportamiento operativo. Cada reporte debe limitar sus conclusiones al régimen que la fuente permite observar.

#### 17.3.15. Roles funcionales y unidades desplegables de referencia

Esta sección no redefine los roles funcionales ya establecidos en la consolidación metodológica: fija la topología de referencia con la que se materializan en el prototipo y ubica en ella al módulo de distribución. La única precisión que el diseño agrega es que ninguno de los tres roles equivale necesariamente a una máquina dedicada.

La topología de referencia dispone un nodo de borde para captura y un nodo central con GPU para procesamiento. El TN permanece fuera del camino operativo de inferencia: cualquier adaptación produce un checkpoint candidato que debe evaluarse posteriormente sobre el CPN y mantenerse como rama comparativa separada. El módulo de distribución no constituye un tercer plano ni un cuarto rol funcional: se modela como una unidad desplegable propia, gobernada por su propia interfaz HTTP y consumidora del bus de alertas. Puede co-ubicarse con el CPN o separarse sin modificar los contratos de alerta interna, notificación y entrega.

**Figura 4.6**

*Roles funcionales CPN, EN y TN*

⟦FIGURA: no extraída — ver el .docx⟧

*Nota.* Las flechas representan transferencia de vídeo, metadatos y checkpoints. No prescriben una cantidad de hosts ni incorporan el TN al trayecto de alerta.

**Tabla 53**

*Correspondencia de diseño entre roles funcionales y unidades desplegables de referencia*

| **Rol o unidad desplegable** | **Materialización de referencia** | **Responsabilidades** |
| --- | --- | --- |
| EN (modo base de captura) | Nodo de captura o unidad de ejecución de borde, sin GPU requerida. | Ingesta, control de ritmo, timestamps, healthcheck y normalización no semántica. La preselección liviana es opcional, fail-open y deshabilitada por defecto. |
| CPN | Nodo central o unidad de ejecución con GPU. | Inferencia OVD, postproceso, publicación, evaluación de patrones, alertas internas, persistencia, observabilidad y reporte. |
| TN | Clúster Mendieta u otro recurso de entrenamiento separado. | Preparación de checkpoints de una rama comparativa bajo datos, protocolo y criterios de escalamiento predefinidos; no sustituye la evaluación sobre el CPN. |
| Módulo de distribución | Servicio gobernado por configuración con interfaz HTTP propia, co-ubicable con el CPN o desplegable por separado. | Consumo de la alerta interna desde el bus de alertas, política de notificación, ledger de idempotencia, entrega MQTT y registro del sobre de notificación y del resultado de entrega. |

*Nota.* Las métricas se atribuyen al rol y al despliegue efectivamente declarados en la corrida. No se extrapolan entre CPN, EN y TN.

#### 17.3.16. Riesgos arquitectónicos y mitigaciones de diseño

Los riesgos arquitectónicos se formulan como modos de falla observables y se vinculan con una mitigación concreta. La arquitectura no presupone que una mitigación elimina el riesgo: exige instrumentarlo y declarar su efecto sobre la interpretación de la corrida.

**Tabla 54**

*Riesgos arquitectónicos y mitigaciones de diseño*

| **Riesgo arquitectónico** | **Mitigación de diseño** |
| --- | --- |
| Conflicto entre calidad perceptiva y cadencia. | Separar selección de modelo, densidad de procesamiento y patrón; medir percepción, G2A y capacidad de sostener el ritmo por configuración sin asumir que un único modelo satisface todos los objetivos. |
| Identidad de detección interpretada como identidad temporal. | Declarar detection_id local al frame; utilizar granularidad de escena o una identidad temporal válida para subject. |
| Pérdida silenciosa en publicador-suscriptor. | Persistir antes de publicar, transportar seq, contar huecos y degradar explícitamente la corrida. |
| Relojes incompatibles entre hosts. | Medir cada tramo en un único dominio o declarar not_interpretable/cross_node_monotonic_clock. |
| Fuente no temporal evaluada con patrones. | Derivar naturaleza temporal y declarar not_applicable/non_temporal_source en lugar de cero alertas. |
| Preselección en borde descarta evidencia. | Mantener la preselección liviana como variante opcional y fail-open, con ledger por unidad y comparación contra el flujo completo. |
| Notificación externa altera la métrica del sistema. | Registrar primero la alerta interna; ubicar cooldown, idempotencia y fallas en distribución. |
| Trazabilidad o privacidad insuficientes. | Conservar manifiesto, JSONL y procedencia; minimizar evidencia visual y controlar acceso y retención. |
| Extensiones desplazan el núcleo. | Separar condiciones configurables de nuevas familias de evaluadores y exigir que cada capacidad opcional se declare por corrida. |

*Nota.* La materialización y la verificación de estos riesgos se documentan en las secciones de implementación y evaluación; aquí se conserva su tratamiento de diseño.

#### 17.3.17. Plan de materialización y criterios de avance

El plan de materialización ordena dependencias de diseño y no reemplaza el registro de implementación. El núcleo se construye primero sobre DBE para estabilizar contratos, evidencia, patrones y reporte; luego se incorporan EBE y capacidades opcionales sin modificar la semántica del flujo base.

El estado ejecutado de cada ítem corresponde a §17.4. En esta sección se conservan únicamente el entregable arquitectónico y el criterio que permite decidir si el incremento es verificable.

**Tabla 55**

*Plan de materialización del núcleo*

| **Incremento** | **Criterio de avance** |
| --- | --- |
| Manifiesto y configuración por componente | Una corrida puede reconstruirse mediante experiment_id, configs efectivas y versiones. |
| Fuentes DBE | Imágenes y vídeos ingresan con identidad, orden y naturaleza temporal declarados. |
| Vocabulario E-IND | Cada detección se atribuye a prompt_set_id y al rol de la clase. |
| Adaptador OVD | El modelo puede sustituirse sin modificar el contrato de percepción. |
| Normalización y postproceso | Las detecciones conservan coordenadas originales, normalizadas y filtros declarados. |
| Persistencia y bus | El hecho se persiste antes de publicarse y toda pérdida resulta detectable. |
| Patrones CR-01/CR-02 | La configuración fija región, granularidad, severidad y ventanas en milisegundos. |
| Alertas internas | Cada episodio confirmado produce una alerta idempotente y auditable. |
| Observabilidad | Cada métrica declara tramo, reloj, unidad, status y cause. |
| Reporte | La salida puede regenerarse desde los artefactos primarios. |

*Nota.* El núcleo no requiere canales externos, métricas MOT ni condiciones de Nivel 2 o 3 para sostener su cadena experimental.

La frontera de extensibilidad distingue tres clases de cambio. Una condición nueva del tipo «sujeto sin EPP» requiere una definición declarativa de patrón y vocabulario, sin modificar contratos ni reentrenar el modelo. Una familia relacional, zonal o de trayectoria requiere un evaluador nuevo en el plano de control. Un modelo, una fuente o un canal nuevos requieren sus respectivos adaptadores, manteniendo estables los contratos centrales. El costo medido de incorporar extensiones se documenta en las secciones de implementación y evaluación.

#### 17.3.18. Cierre del diseño arquitectónico

El diseño define una plataforma experimental compuesta por plano de medios, plano de control, soporte experimental y un tramo desacoplado de distribución. La organización protege la ruta crítica, separa evidencia de interpretación y conserva una cadena causal reconstruible desde la fuente hasta la entrega.

El núcleo de CR-01 y CR-02 utiliza evidencia positiva de person, helmet y vest, inferencia espacial de ausencia y estabilización temporal por patrón. La granularidad de escena y la granularidad de sujeto se tratan como configuraciones semánticamente distintas; la identidad personal permanece fuera del alcance.

La arquitectura fija contratos versionados, JSONL de sólo adición y dos patrones de acople: gobierno mediante HTTP, gobernado por configuración, para medios, control y distribución; y transporte ZeroMQ con patrón publicador-suscriptor y msgpack para detecciones y alertas. La naturaleza temporal de la fuente, los dominios de reloj y los estados de aplicabilidad forman parte de la validez de cada métrica.

Las extensiones se clasifican por su costo arquitectónico: una condición del mismo tipo se incorpora por configuración; una familia nueva requiere un evaluador; y nuevos modelos, fuentes o canales requieren adaptadores. Esta frontera evita presentar la extensibilidad open-vocabulary como una capacidad ilimitada.

La sección deja preparado el paso a la implementación sin anticipar sus resultados. §17.4 documenta qué componentes se materializaron y cómo se verificaron; §17.5 concentra las mediciones y su interpretación experimental.

El diseño se considera completo cuando cada una de estas decisiones —separación de responsabilidades, estrategia perceptiva, configuración reproducible, contratos versionados, persistencia y transporte diferenciados, temporalidad declarada, alerta interna protegida y extensibilidad delimitada— posee un criterio verificable en la implementación.

---

## Fuente: `docs/informe/ajustes/03-etapa-3-diseno-arquitectonico.md`

> SHA-256 del bloque: `7635ae3d9e9bb2ae167d3528a30a0314238da47139142cc0598842f663cf8584`  
> Seleccion: documento completo.

# Etapa 3 — ajustes al diseño arquitectónico (§17.3)

> ✅ **Estado (✎ 2026-08-28): §17.3 está en v1.4 con sus tres pases E3 aplicados y verificados**
> (`correcciones-etapa-3-4*.md`, E3-01…E3-42; `00-el-informe-hoy` 08-28). La decisión por
> redline **se resolvió dentro de esos pases**; las 53 casillas del `93` **no se marcaron una a
> una** — el ✎ 08-28 en la cabecera del `93` vale como constancia, y el mapeo redline→E3-xx
> queda como deuda de trazabilidad. Pendiente: D-E2-2 recorta la glosa de §17.3.6.4 a una
> remisión (v1.4 → v1.5) cuando la Etapa 2 bautice E-DIR/E-IND/E-HYB en §17.1.5.4.2
> (`operacion/130` §6). **Lo que sigue es registro histórico.**
>
> **Estado (2026-08-10):** es el **único frente con hoja de trabajo formal y casillas de
> decisión**. Las 26 redlines viven en `material-etapa-3/93-redlines-etapa3.md` (v2,
> 2026-07-12) y **ninguna está aplicada al `.docx`**: las casillas `[ ]` del tablero
> siguen vacías.
>
> **Este documento no reemplaza al 93 ni lo resume "por si acaso": lo enruta.** La ficha
> de cada redline —qué dice hoy, qué debe decir, por qué— está en el 93 y solo ahí. Acá
> está el mapa, el estado y las tres cosas que hay que saber antes de abrirlo.

| Dónde | Qué |
|---|---|
| Texto actual | `entregable/90-etapa3-texto-extraido.md` (§17.3.1–§17.3.18) y el `.docx` de Etapa 3 |
| **Las 26 redlines** | **`material-etapa-3/93-redlines-etapa3.md`** ← la hoja de trabajo |
| Texto largo ya redactado | `material-etapa-3/94-secciones-nuevas-etapa3.md` (§1–§9, cubre 9 redlines) |
| El análisis que las originó | `material-etapa-3/91-relevamiento-etapa3-vs-implementacion.md` |
| Material verificado contra código | `material-etapa-3/92-anexo-concrecion-tecnica.md` |
| §17.3.10 (distribución de alertas) | `material-etapa-3/92b-concrecion-distribucion-alertas.md` |

---

## 1. Lo que hay que saber antes de abrir el 93

**Son 26, no 24.** `R-25` y `R-26` se agregaron en la v2 del 2026-07-12, tras auditoría
adversarial. **`R-26` es, según la propia auditoría, "la más valiosa" de todas**
(extensibilidad medida: cuánto cuesta agregar una condición nueva). Un pase que se
detenga en R-24 se pierde justo la mejor.

**La remisión de cifras del 93 está derogada.** El 93 dice "todas las cifras remiten a
la tabla canónica del doc 92 §10". Ese `informe/92` §10 **quedó derogado como fuente de
números el 2026-08-05**. Al transcribir cualquier redline, **las cifras se toman de los
cuatro índices de `e-ovrt_experimental-setup/results/`** (verificables con
`operacion/datos/96-verificar-indices.py`). El 93 ya lleva el banner de esta corrección.

**Numeración de tablas nuevas.** El capítulo cierra en la **Tabla 60**; las tablas nuevas
del doc 94 están numeradas **61 a 67**. Al transcribir hay que verificar que no colisionen
con las que se agreguen en el camino.

---

## 2. El tablero, con lo que cambió desde que se escribió

Prioridad y sección salen del tablero del 93; la última columna es el estado a hoy.

| # | § | Tipo | Pri | Título | Texto listo | Novedad desde 2026-07-12 |
|---|---|---|---|---|---|---|
| R-01 | 17.3.9.2 | CONTRADICE | 🔴 | La estrategia del núcleo es E-IND, no la directa | — | reforzada: E-DIR quedó vetada por precisión (AF-2) |
| R-02 | Tabla 44 | CONTRADICE | 🔴 | El `cooldown` no es parámetro de patrón | — | **atendida por `92b`**, que fija la frontera (ADR-011) |
| R-03 | Tabla 44 / 17.3.6.2 | CONTRADICE | 🔴 | `RunConfig` es un manifiesto + configs por plano | — | |
| R-04 | 17.3.8.3.2 | PRECISA | 🔴 | Granularidad `scene\|subject` + caveat semántico de escena | — | reforzada: G1 (sujeto) terminó siendo **el mejor resultado del banco** |
| R-05 | Tabla 45 / 17.3.6.4 | CONTRADICE | 🔴 | El vocabulario del núcleo es positivo (person/helmet/vest) | — | |
| R-06 | 17.3.11 | CONCRETA | 🔴 | Partir el hedge en dos + tabla de correspondencia | **94 §1** | |
| R-07 | 17.3.11.4 | CONCRETA | 🔴 | Regla de evolución del evento (el pedido del tutor) | **94 §2** | ✎ **08-12: la fila de identidad de sujeto estaba vieja y se corrigió** — ver §3c |
| R-08 | 17.3.8.1 / .4 | CONCRETA | 🟠 | El bus existe y tiene tecnología: ZeroMQ + msgpack | **94 §3** | |
| R-09 | 17.3.5 | CONCRETA | 🟠 | Figura nueva: vista de procesos (dos servicios HTTP) | **94 §4** | es la **FIG-A** del inventario de cierre |
| R-10 | 17.3.13 | CONCRETA | 🟠 | Diccionario de métricas con t0/t1 + criterio de relojes | **94 §5** | cruza con `AJ-2.03` (§17.1) |
| R-11 | 17.3.14 (nueva .6) | PRECISA | 🟠 | Temporalidad de la fuente y el "cero silencioso" | **94 §6** | formalizada en ADR-013 |
| R-12 | cierre (nueva) | EVIDENCIA | 🟠 | Verificación: qué funciona y cómo se midió | **94 §7** | insumo completo: `operacion/97` |
| R-13 | cierre (nueva) | EVIDENCIA | 🟠 | Registro del alcance efectivo y brechas | **94 §8** | ✎ actualizado post ADR-016/017 y `operacion/114`; no usar la tabla preimplementación |
| R-14 | 17.3.8.2 / Tabla 46 | PRECISA | 🟠 | Ventanas efectivas: 4000 / 7000 ms; severidades `high`/`medium` | — | ficha canónica de los valores; cruza con `AJ-2.01` |
| R-15 | 17.3.12.1 | CONCRETA | 🟡 | El repositorio es JSONL append-only, con layout | — | |
| R-16 | 17.3.13.3 | PRECISA | 🟡 | La aplicabilidad es un campo literal (`status` + `cause`) | — | ADR-006/013; cruza con `AJ-2.12` |
| R-17 | 17.3.15 | CONCRETA | 🟡 | Tabla rol → contenedor (Nodo A ≈ EN-1, Nodo B ≈ CPN) | — | |
| R-18 | Tabla 43 (DA-01…13) | PRECISA | 🟡 | Actualizar el estado de las decisiones condicionadas | — | **no confundir con T-81** (ADR → informe), que es otra tabla |
| R-19 | Tabla 50 | ERRATA | 🟡 | `PatternDefinition` es huérfano: falta su fila | — | |
| R-20 | Tabla 57 | PRECISA | 🟡 | Riesgos: los que se materializaron y cómo se mitigaron | — | |
| R-21 | Tablas 58/59 | EVIDENCIA | 🟠 | Backlog: estado real de los 16 ítems | — | **desbloqueada por ADR-015**, y tiene **un punto falso** (ver §3) |
| R-22 | 17.3.14.5 | PRECISA | 🟡 | EBE: la cámara IP real ya se usó; la brecha que queda | — | cruza con `AJ-2.10` |
| R-23 | varias | ERRATA | 🟢 | Figuras sin numerar y vacías, títulos pegados, duplicados | — | |
| R-24 | fuera de 17.3 | PRECISA | 🟡 | Inventario de datasets desactualizado | — | enrutada también desde `AJ-0.05` |
| R-25 | 17.3.11 / 17.3.13 | CONCRETA | 🟠 | Contrato de GT temporal + identidad + los 5 hitos | — | cruza con `AJ-2.09` |
| R-26 | 17.3.17 / 17.3.18 | CONCRETA | 🟠 | **Extensibilidad medida: cuánto cuesta una condición nueva** | **94 §9** | **la más valiosa**; su cifra es la tabla **T-77** |

**Recuento:** 26 redlines — **7 🔴 crítica · 10 🟠 alta · 8 🟡 media · 1 🟢 baja**.
**9 tienen el texto completo ya redactado** en el doc 94 (§1–§9).

---

## 3. Las dos correcciones que ADR-015 dejó pendientes de anotar

ADR-015 (aceptado 2026-08-05) desbloqueó dos redlines que lo estaban esperando, y al
hacerlo dejó dos anotaciones que **hay que aplicar antes de transcribir**:

- **R-13 (registro del alcance efectivo):** la versión inicial quedó superada dos veces.
  `94` §8 ya debe registrar como ejercidos G1, la comparación E-DIR/E-IND/E-HYB, la
  paridad DBE/EBE y la distribución funcional; conserva como límites las métricas MOT,
  las condiciones de nivel 2/3 y las brechas de integración declaradas.
- **R-21 (backlog, Tablas 58/59):** tiene **un punto falso** — dice *"MOT ✗ tracker no
  implementado"*. Lo excluido son las **métricas** MOT (exclusión E-10), **no la
  capacidad**: el tracker existe y la granularidad por sujeto (G1) es el mejor resultado
  del banco.

Ambas anotaciones ya están escritas en el propio 93, en las fichas de R-13 y R-21.

---

## 3b. ✎ 2026-08-11 — la regla de no-anacronismo y las redlines "al cierre"

**La regla** (mapa, regla 5): una etapa temprana no menciona resultados de etapas
posteriores. El §17.3 es Etapa 3 — **recibe correcciones de diseño y decisiones**
(R-01…R-11, R-14…R-19, R-24, R-25: todas son eso), pero **no números de verificación**.
Cuatro redlines quedan tocadas:

- **R-12** ("verificación: qué funciona y cómo se midió") y **R-13** ("registro de lo no
  implementado") fueron concebidas como *secciones nuevas al cierre* del §17.3 — cuando
  §17.4/§17.5 no existían como plan. Hoy existen, y **ese material aterriza en §17.4**
  (así lo enruta el doc de Etapa 4: `AJ-4.10` y `AJ-4.11` usan `94` §7–§8). El §17.3
  queda, a lo sumo, con un puntero de una línea. El texto del `94` §7–§8 sirve igual —
  cambia la sección de destino, no el contenido.
- **R-20** (riesgos que se materializaron) y **R-22** (la cámara IP real ya se usó): la
  parte *retrospectiva* ("cómo resultó") va como **nota fechada o remisión a §17.4**,
  no como prosa del diseño reescrita en pasado profético.

La decisión formal de cada caso queda donde siempre: en la casilla de la redline.

## 3c. ✎ 2026-08-12 — R-07: la fila de identidad de sujeto había envejecido mal

**R-07 es la redline que contesta el punto que el tutor técnico marcó como "muy
importante"**: que el evento de inferencia dé soporte a datos que hoy no están —tracking,
velocidad, dirección, pose, segmentación—. Su texto (doc `94` §2, Tabla 63) declaraba
para identidad de sujeto que *"el componente que lo puebla no está implementado"*. **Era
cierto el 12/07 y es falso desde el 2026-08-04.** El glosario (`13`, entrada `track_id`)
ya llevaba la corrección desde el 08-10; el material de Etapa 3 no la había recibido.

Corregido el 2026-08-12 en `94` §2 y en `92` §4.2 (con recuadro y ruta:línea), y la
corrección **refuerza** la respuesta al tutor en lugar de debilitarla: de las cinco
extensiones que él nombró, **una se recorrió de punta a punta, por configuración y sin
tocar el contrato**, y quedó medida. El reparto entre etapas respeta la regla de
no-anacronismo:

- **§17.3.11.4** (acá): el mecanismo y el estado del contrato, **sin cifra**.
- **§17.4**: la cifra y la comparación pareada (`AJ-4.12`, ampliado el mismo día).

Dos honestidades que viajan con el dato y no se pueden recortar al transcribir: el
`track_id` **no queda en el JSONL del plano de medios** sino en los artefactos del
control, y **lo excluido por E-10 son las métricas MOT, no la capacidad**.

## 4. Cómo se trabaja este frente

El 93 fue escrito para operarse ítem por ítem, con casilla de decisión por redline:

```
DECISIÓN → [ ] acepto   [ ] modifico   [ ] rechazo
```

El orden sugerido está al final del 93 (§*Orden sugerido de trabajo*). El criterio
razonable: **las 7 🔴 primero** (4 son contradicciones, que no son opinables), después
las 🟠 que ya tienen texto en el doc 94 —son transcripción, no redacción—, y al final las
🟡/🟢 de forma.

**El `.docx` no se toca desde el 93.** El 93 produce la instrucción; la edición se hace
en el documento, y la casilla queda como registro de la decisión tomada.

---

## 5. §17.3.10 — el caso especial de la distribución de alertas

`material-etapa-3/92b-concrecion-distribucion-alertas.md` es el diseño completo de esa
subsección, y **`nucleo/19`** es el cierre arquitectónico del ciclo de vida de la alerta
(dónde viven cooldown, supresión y re-notificación — consolida `nucleo/06`, ADR-005,
ADR-011, la spec 45 y el propio `92b`).

**El estatuto lo fija ADR-016 y el estado ejecutado lo fija `operacion/114`.** El módulo
pasó de exclusión a trabajo comprometido y hoy está **funcionalmente implementado**: DBE,
EBE, cooldown, idempotencia, MQTT QoS 1 y reporte consolidado fueron verificados. ✎ **2026-08-14:** las
tres brechas que este párrafo declaraba —vista de webconsole, orquestación y un repo sin
commits— se cerraron el 2026-08-13 (`13c801e`, `42529e2`; repo con `c9903cc` y `1e6d8fa`).

El §17.3.10 describe arquitectura y contratos; las mediciones de verificación del canal no
se convierten automáticamente en resultados de desempeño. El publisher
`control.alert.v1` continúa desactivado por defecto y `AlertEvent` no tiene
`confirmed_at_ms` (detalle corregido por `92b`).

[Enmienda 2026-08-14] §17.3.10 tiene UNA pieza de evidencia en el inventario de cierre:
T-85 (`gobierno/99` §1), la latencia de notificación medida por la campaña del doc 118.

## 6. Fuentes

`material-etapa-3/93` (tablero y las 26 fichas) · `94` (§1–§9, el texto) · `91` (el
relevamiento y el pedido del tutor técnico) · `92` (concreción verificada contra código)
· `92b` (§17.3.10) · `nucleo/19` (ciclo de vida de la alerta) · `gobierno/95` (la
auditoría adversarial que produjo la v2 y agregó R-25/R-26) ·
`decisiones/adr-015-cierre-de-alcance.md` + `adr-016-reapertura-acotada-distribucion.md`.

---

## Fuente: `docs/informe/ajustes/material-etapa-3/92-anexo-concrecion-tecnica.md`

> SHA-256 del bloque: `01be478d08ee54ad68e58ec58caef393156622059cd29194e18436333950c7db`  
> Seleccion: documento completo.

# Anexo de concreción técnica — material listo para inyectar en el capítulo

- **Fecha:** 2026-07-12
- **Para qué sirve:** es la respuesta material a la observación del tutor técnico
  ("se definen contratos y módulos pero no siempre se evidencia cómo se implementan concretamente:
  clases, APIs, servicios"). Todo lo de acá está **verificado contra el código y contra artefactos
  reales en disco**, con ruta y línea. Nada está inventado ni idealizado.
- **Cómo usarlo:** cada sección corresponde a un redline del plan de `91-relevamiento-etapa3-vs-implementacion.md`
  (bloque B). El texto está escrito para poder pasarse al `.docx` con edición mínima.
- **Regla de oro al copiar:** si un campo no está en el código, **no va al informe**. La única forma de
  que este anexo envejezca mal es que alguien "mejore" un esquema al transcribirlo.

> ✎ **2026-08-12 — tres correcciones de propagación.** Este anexo estaba congelado en el 12/07 y el
> sistema siguió andando. Antes de transcribir nada:
>
> 1. **La §10 quedó derogada como fuente de números el 2026-08-05.** Las cifras salen de los **cuatro
>    índices de `e-ovrt_experimental-setup/results/`** (verificables con `operacion/datos/96-verificar-indices.py`).
>    La §10 sirve todavía para saber **qué corrida produjo qué**, no para citar el valor.
> 2. **La fila de tracking de la §4.2 decía que nadie puebla `track_id`. Es falso desde el 2026-08-04**
>    (el glosario ya está corregido; este anexo no lo estaba). Corregida en su lugar — y la corrección
>    **juega a favor**: es la única extensión del evento que se recorrió de punta a punta y se midió.
> 3. **La distribución de alertas ya no es "exclusión declarada"**: ADR-016 (2026-08-10) la reabrió como
>    **trabajo comprometido** antes de la defensa. Se redacta describiendo el diseño y **declarando el
>    estado real al momento de la entrega**, nunca en presente como si funcionara. Filas afectadas: la
>    última de la §1 y la última de la §9.

---

## 1. Tabla de correspondencia: contrato preliminar (Etapa 3) ↔ artefacto real

Esta tabla es la bisagra del capítulo. Convierte los diez nombres conceptuales de la Tabla 50 en
artefactos verificables, sin traicionar la lógica del diseño original.

| Contrato preliminar (Tabla 49/50) | Artefacto real | Tipo / esquema | Dónde vive |
|---|---|---|---|
| `RunConfig` | **Manifiesto de experimento** + configs por plano (referenciadas) | `experiment.manifest.v1` | `e-ovrt_experimental-setup/experiments/` |
| `SourceDefinition` | Sección `source` de la run config + **registro de plugins de ingesta** | `SourceSection` | `media-plane/config/schemas.py:141` |
| `ModelProfile` | Catálogo de modelos por archivo + `EOVRT_MODEL_REF` | `ModelSection` | `media-plane/configs/models/<familia>/<variante>.yaml` |
| `PromptDefinition` | Prompt set versionado | `PromptSet` / `PromptClass` | `experimental-setup/prompts/cr01_cr02_v2_short.yaml` |
| `FrameMetadata` | `VisualUnit` (interno) + bloque `source` del evento publicado | `VisualUnit` | `media-plane/contracts/visual_unit.py:11` |
| **`PerceptionEvent`** | **`DetectionEvent`** | **`media.detection.v1`** | `media-plane/contracts/events.py:44` |
| `PatternDefinition` | Definición declarativa dentro del pattern set | `PatternDefinition` | `control-plane/config.py:91` |
| `PatternStateChanged` | `PatternStateChanged` | `control.pattern_state.v1` | `control-plane/contracts/pattern.py:31` |
| `AlertEvent` | `AlertEvent` (`alert_id` uuid5 determinista ⇒ idempotente) | `control.alert.v1` | `control-plane/contracts/alerts.py:10` |
| `MetricSample` | `MetricSample` (medios) / `ControlMetricSample` (control) | `media.metric.v2` / `control.metric.v1` | `media-plane/contracts/metrics.py:8` · `control-plane/contracts/metrics.py:18` |
| `ErrorEvent` | `errors.jsonl` por corrida | — | ambos planos |
| Repositorio de eventos (§17.3.12) | **JSONL append-only por corrida** | `runs/<run_id>/*.jsonl` | cada plano |
| Bus interno de eventos (§17.3.8.4) | **ZeroMQ XPUB/SUB + msgpack** | `bus.envelope.v1` | `media-plane/transport/bus.py:19` |
| Reporte experimental (§17.3.13.4) | Reporte consolidado | `report.json` / `report.md` | `experimental-setup/runs/<experiment_id>/report/` |
| Alerta distribuida (§17.3.10) | `NotificationEnvelope` / `DeliveryRecord` | `control.notification.v1` / `control.delivery.v1` | **Implementada y verificada** (`operacion/114`): DBE/EBE, política, ledger, MQTT QoS 1 y reporte; ~~pendientes webconsole, orquestación y commits~~ ✎ cerrados 2026-08-13 (doc 119); ✎ 2026-08-18: además servicio HTTP propio `:8082` (ADR-019, doc 124) |

> **Frase para el capítulo:** *"Los contratos definidos en la Etapa 3 dejaron de ser denominaciones
> preliminares para el núcleo validable: se materializaron como modelos de datos versionados, con
> serialización explícita y esquema verificable. La tabla siguiente establece la correspondencia. Los
> contratos del tramo de distribución también se materializaron; sus brechas de integración
> se declaran por separado, sin confundirlas con la existencia del módulo."*

---

## 2. El evento de detección: clase, esquema y serialización

Es el contrato central del sistema (el `PerceptionEvent` del capítulo). El tutor pidió literalmente ver
"una clase" y "un DTO". Acá están las dos cosas.

### 2.1 La clase (Python / Pydantic)

`e-ovrt_media-plane/src/eovrt_media/contracts/events.py:44`

```python
class DetectionEvent(BaseModel):
    schema_version: str = "media.detection.v1"
    event_type: str = "detection_event"
    run_id: str
    unit_id: str                      # identificador de la unidad visual (frame)
    source: DetectionEventSource      # source_id, source_type, frame_index, timestamp_ms, width, height
    model: DetectionEventModel        # name, model_id, device
    prompts: DetectionEventPrompts    # prompt_set_id
    detections: list[Detection]
    timing: DetectionEventTiming      # normalize_ms, inference_ms, postprocess_ms, write_ms, total_ms


class Detection(BaseModel):           # contracts/detection.py:28
    detection_id: str | None = None
    label: str
    prompt_id: str | None = None
    source_prompt: str | None = None
    strategy: str | None = None       # declarado en el modelo; NO se serializa hoy (vale None)
    condition_id: str | None = None   # ídem
    confidence: float
    bbox_xyxy: list[float]            # píxeles, sistema de la imagen original
    bbox_norm_xyxy: list[float]       # normalizado [0,1]
    area_px: float | None = None
    model_name: str | None = None
```

> ⚠️ **Corregido tras auditoría (2026-07-12).** Los campos opcionales son opcionales **de verdad**: no
> los muestres como requeridos. Y `strategy` / `condition_id` **existen en el modelo pero valen `None` y
> no aparecen en el JSONL** de las corridas actuales (el escritor omite los nulos). Si querés mostrarlos
> en el informe, hay que **poblarlos primero**; hasta entonces, no van al DTO de ejemplo.

### 2.2 El DTO serializado — **línea literal**, verificada carácter por carácter

> ⚠️ **La versión anterior de este bloque estaba fabricada** (una detección `helmet` que no existía en esa
> línea, y tiempos de postproceso/escritura inventados). La regla desde la auditoría del 2026-07-12:
> **transcripción literal — no se agrega, no se mejora, no se completa nada.**
>
> ✅ **✎ 2026-08-22 — RESUELTO el clip retirado (opción (a) de `94` §1.3, re-transcripción).** El ejemplo
> anterior salía de `cb_b01_p7`, retirado del banco el 2026-08-03. Lo que sigue es la **transcripción
> literal** de
> `e-ovrt_media-plane/runs/run_20260803_211225_dbe_grounding_dino_1e06f3/detections.jsonl`
> (corrida real de la campaña del banco congelado sobre **`a_p1_c02`**, clip VIGENTE del rodaje, P1/CR-01),
> unidad `frame_000229` — **la unidad en la que el sistema confirma CR-01**, exactamente **4.000 ms** después
> de la primera evidencia (`frame_000109`, 3.633,33 ms → 7.633,33 ms). La confirmación se reprodujo por
> replay del control-plane el 2026-08-22 y quedó archivada:
> `operacion/datos/129-2026-08-22-bench-a_p1_c02-gdino-alerts.jsonl` (+ `…-summary.json`).
> **Sin recorte:** la unidad tiene 3 detecciones y se muestran las 3.

```json
{
  "schema_version": "media.detection.v1",
  "event_type": "detection_event",
  "run_id": "run_20260803_211225_dbe_grounding_dino_1e06f3",
  "unit_id": "frame_000229",
  "source":  { "source_id": "a_p1_c02", "source_type": "video_frame",
               "frame_index": 229, "timestamp_ms": 7633.33,
               "width": 1920, "height": 1080 },
  "model":   { "name": "grounding_dino",
               "model_id": "IDEA-Research/grounding-dino-tiny", "device": "cuda" },
  "prompts": { "prompt_set_id": "cr01_cr02_v2_short" },
  "detections": [
    { "detection_id": "det_000001", "label": "person",
      "prompt_id": "person", "source_prompt": "person", "confidence": 0.88,
      "bbox_xyxy": [1239.8, 149.8, 1503.2, 861.9],
      "bbox_norm_xyxy": [0.6457, 0.1387, 0.7829, 0.7981],
      "area_px": 187612.4, "model_name": "grounding_dino" },
    { "detection_id": "det_000002", "label": "vest",
      "prompt_id": "vest", "source_prompt": "vest", "confidence": 0.8755,
      "bbox_xyxy": [1286.5, 235.3, 1459.3, 487.0],
      "bbox_norm_xyxy": [0.67, 0.2179, 0.76, 0.4509],
      "area_px": 43490.1, "model_name": "grounding_dino" },
    { "detection_id": "det_000003", "label": "helmet",
      "prompt_id": "helmet", "source_prompt": "helmet", "confidence": 0.456,
      "bbox_xyxy": [1519.0, 432.5, 1648.1, 521.3],
      "bbox_norm_xyxy": [0.7911, 0.4005, 0.8584, 0.4827],
      "area_px": 11463.6, "model_name": "grounding_dino" }
  ],
  "timing": { "normalize_ms": 8.06, "inference_ms": 491.17,
              "postprocess_ms": 0.08, "write_ms": 0.0, "total_ms": 491.27 }
}
```

**Tres cosas que esta línea literal enseña, y que un ejemplo fabricado ocultaría:**

1. **`strategy` y `condition_id` no aparecen.** Existen en el modelo Pydantic, pero valen `None` y el
   escritor omite los nulos. El evento **no lleva hoy la condición de riesgo asociada**: la asociación
   condición ↔ evidencia la hace el plano de control. Si se quiere que el evento la lleve, hay que
   poblarla (es aditivo y barato) — pero **no se puede escribir en el informe que ya la lleva**.
2. **La unidad TIENE un `helmet` (0,456) y aun así CR-01 confirma.** El casco detectado está fuera de la
   región cefálica del sujeto (`det_000001`) — cae a su derecha, más allá del margen lateral configurado.
   Es E-IND funcionando a la vista: la ausencia se infiere **por sujeto y por región**, no por presencia de
   la clase en el frame. El `rationale` de la alerta archivada lo dice: *"No se encontro evidencia 'helmet'
   en region 'upper_body' de 1 sujeto(s)"* — con `vest` (0,8755) como positivo simultáneo del mismo sujeto,
   por eso CR-02 no abre episodio.
3. **El conjunto de prompts va por referencia a catálogo (`cr01_cr02_v2_short`)**, el set congelado de las
   campañas — a diferencia del ejemplo anterior, que llevaba el sufijo `_inline` de un disparo con el set
   embebido. Ambas formas son trazables; ésta además ancla la corrida al artefacto congelado.

### 2.3 Dónde se publica

El mismo payload viaja por dos caminos, **byte-idénticos**:

- **DBE (offline):** se escribe append-only en `runs/<run_id>/detections.jsonl`. El control-plane lo relee.
- **EBE (live):** se publica en el bus dentro de un envelope msgpack.

```python
# media-plane/transport/bus.py:19
ENVELOPE_SCHEMA_VERSION  = "bus.envelope.v1"
DETECTION_TOPIC_PREFIX   = "media.detection.v1."      # topic: media.detection.v1.<media_run_id>
LIFECYCLE_TOPIC_PREFIX   = "run.lifecycle.v1."
```
```jsonc
// envelope (msgpack) — el payload es la MISMA línea que va al JSONL
{ "schema_version": "bus.envelope.v1",
  "topic": "media.detection.v1.run_20260803_211225_...",
  "key": "a_p1_c02",           // source_id
  "seq": 41,                   // monótono: el hueco de seq es la ÚNICA señal de pérdida
  "ts_publish_ms": 1783804607379.2,
  "payload": <bytes de la línea JSONL> }
```

> **Frase para el capítulo:** *"El evento de percepción se persiste primero y se publica después. El
> payload publicado en el bus es byte-idéntico a la línea persistida, de modo que toda corrida en vivo es
> re-evaluable offline y produce artefactos idénticos (verificado)."*

---

## 3. Las APIs: el sistema es ejecutable por HTTP

El capítulo no tiene una sola interfaz. El sistema tiene dos servicios HTTP config-driven (✎ 2026-08-28: **tres** desde ADR-019 — `:8080/:8081/:8082`; `operacion/130` §2). Esta es la
tabla mínima que responde al "una API: `POST /events/detection`" del tutor.

✎ **2026-08-18 (ADR-019 + ADR-020): son TRES servicios HTTP config-driven** — el módulo
de distribución sumó el suyo (`eovrt-distribute serve`, `:8082`, espejo del control-plane:
`POST /api/runs` 201/409/422, `GET /api/runs/{id}`, `POST /api/runs/{id}/cancel`,
`DELETE`, `/healthz`/`readyz`/`config`; doc `operacion/124`). **ADR-020 derogó a ADR-018**:
el runner del BFF le habla por HTTP **por default**, igual que a los otros dos planos, y
el subproceso quedó como fallback operativo fuera del relato arquitectónico. Al citar "el
sistema es ejecutable por HTTP", son **tres** servicios y **un** patrón de acople HTTP
para los tres.

### 3.1 Plano de medios — `:8080` (FastAPI; `service/app.py:64`)

| Método | Path | Request | Respuesta |
|---|---|---|---|
| `GET` | `/healthz` · `/readyz` | — | `{"status":"ok"}` · `{"status":"ready","model":"<ref>"}` o 503 |
| `GET` | `/api/model` | — | modelo cargado, device, umbrales |
| **`POST`** | **`/api/runs`** | **`RunRequest`** | **201 `{"run_id": "..."}`** · 409 si hay corrida activa · 422 config inválida |
| `GET` | `/api/runs/{run_id}` | — | estado + `summary` |
| `POST` | `/api/runs/{run_id}/stop` | — | 202 |
| `GET` | `/api/runs/{run_id}/detections` | `page`, `page_size` | página de `DetectionEvent` |
| `POST` | `/api/runs/{run_id}/evaluate` | — | `EvalPerceptionResults` (AP@0.5 por clase, `mAP50`, recall CR-01) |
| `WS` | `/api/runs/{run_id}/stream` | — | eventos de la corrida en curso |

```python
# service/run_request.py:49 — el contrato de disparo de una corrida
class RunRequest(BaseModel, extra="forbid"):
    ingest:  IngestSpec           # {plugin: "video_file"|"image_folder"|"rtsp", config: {...}}
    prompts: PromptsSpec          # {set_inline: {...}, active_ids: [...]}
    run:     RunParams            # {stride, max_units, save_annotated_video, save_previews, name}
    bus:     BusSpec | None       # {enabled, endpoint, hwm, wait_for_subscriber_ms}
    experiment_id: str | None     # clave de trazabilidad de la corrida paraguas
```

**Decisión de diseño citable:** el modelo **nunca viaja en el request**. Se carga una vez al arranque del
servicio desde `EOVRT_MODEL_REF`. Un servicio = un modelo cargado; comparar modelos = levantar servicios
distintos. Esto mantiene la ruta crítica libre del costo de carga de pesos (que es de decenas de segundos).

### 3.2 Plano de control — `:8081` (FastAPI; `service/app.py:30`)

| Método | Path | Request | Respuesta |
|---|---|---|---|
| `GET` | `/healthz` · `/readyz` | — | `{"status":"ok"}` |
| **`POST`** | **`/api/runs`** | **`ControlRunRequest`** | **201 `{"control_run_id": "..."}`** · 409 busy |
| `GET` | `/api/runs/current` · `/api/runs/{id}` | — | estado + `summary` |
| `GET` | `/api/runs/{id}/alerts` | `limit` | lista de `AlertEvent` |
| `GET` | `/api/config` | — | config efectiva de la corrida |

```python
# control-plane/service/run_request.py:10
class ControlRunRequest(BaseModel):
    mode: Literal["replay", "live"]
    config_path: str | None       # por referencia
    config: dict | None           # por payload (ADR-009) — exactamente uno de los dos
    experiment_id: str | None
```

**Invariante no negociable, y hay que escribirlo:** el `201` de un `POST` con `mode: live` **implica que el
consumidor del bus ya está suscripto**. ZeroMQ PUB/SUB **pierde todo lo publicado antes de la
suscripción**; por eso el orden de disparo es **control primero, medios después**. El runner lo verifica
antes de disparar el media-plane (`SubscriptionNotConfirmed` bloquea la corrida).

### 3.3 Orquestación

Un tercer componente (runner CLI / webconsole, en `e-ovrt_experimental-setup`) dispara la corrida paraguas
por HTTP contra ambos servicios, propaga el `experiment_id` y consolida los resultados. **La webconsole no
consume el bus**: habla con las APIs (patrón BFF). El bus es interno de la plataforma.

---

## 4. Extensibilidad del evento de inferencia — la respuesta a T3

Este es el punto más sustantivo de la observación del tutor:

> *"Es muy importante ser muy claro en la definición de eventos tipo inferencias para que den soporte a
> datos que a lo mejor hoy no están, pero mañana sí: agregar a las detecciones detecciones asociadas,
> datos de tracking, velocidad, dirección, eventualmente pose o segmentación."*

### 4.1 La regla de evolución (adoptada, spec 40 §1)

1. **Los cambios son siempre aditivos.** Un campo nuevo entra como **opcional con default**, nunca como
   requerido.
2. **Un cambio aditivo no bumpea `schema_version`.** `media.detection.v1` sigue siendo `v1` cuando gana
   `track_id`. Un consumidor viejo ignora el campo nuevo; un consumidor nuevo lo encuentra ausente y usa
   su default.
3. **Cambiar el significado de un campo, o eliminarlo, es ruptura contractual** ⇒ obliga a `v2`.
4. **La versión viaja en el payload**, no en el transporte (`schema_version` es un campo del evento, tanto
   en la línea JSONL como dentro del envelope msgpack). Un artefacto guardado es autodescriptivo: se puede
   releer años después sin conocer el canal por el que viajó.
5. El consumidor tolera artefactos viejos: `DetectionEvent` del control-plane tiene un
   `model_validator(mode="before")` (`contracts/media.py:87`) que absorbe eventos con campos planos legacy.

### 4.2 El camino concreto de cada extensión que el tutor nombró

| Extensión | Camino en el contrato | Estado hoy |
|---|---|---|
| **Tracking (`track_id`)** | Campo opcional de `Detection`, **presente en AMBOS contratos** desde 2026-07-13: del lado consumidor (`control-plane/contracts/media.py:15`, el motor lo usa como identidad en `state_key()`, `spatial_absence.py:144`) y del lado productor (`media-plane/contracts/detection.py:38`, commit `0133d38`, con tests que fijan que ausente no se serializa —byte-compat— y presente sí). | ✎ **2026-08-12 — CORREGIDO. Decía "ningún componente lo puebla todavía"; es falso desde el 2026-08-04.** Ver el recuadro de abajo: la extensión **se recorrió y se midió**. Lo que sigue siendo cierto es que **el productor no lo emite**: en `detections.jsonl` el campo no aparece. |
| **Velocidad y dirección** | Campos opcionales derivados (`velocity_px_s`, `heading_deg`). No requieren cambiar el evento: requieren `track_id` + los timestamps **que ya viajan** (`source.timestamp_ms`, `capture_monotonic_ns`, `capture_wallclock_ms`). | Especificado; no implementado. |
| **Pose** | Campo opcional (`keypoints`). ⚠️ **Corregido:** el motor **no tiene soporte de pose**. Lo que tiene es una **heurística geométrica**: la región de búsqueda de EPP se ensancha a altura completa cuando la relación de aspecto del bbox sugiere un sujeto no erguido (`full_height_aspect_ratio`, `PatternRegionConfig`, usado en `spatial_absence.py:58`). Decirle "costura de pose" invita a que te pidan el keypoint. | Heurística de aspecto en el evaluador; el evento no lleva keypoints. |
| **Segmentación** | Campo opcional (`mask_rle` / `polygon`), junto al bbox, no en lugar de él. | Especificado; no implementado. |
| **Detecciones asociadas** | Ya modelado, pero **en el plano de control, no en el evento de percepción**: `PatternEvidence` liga el sujeto con sus detecciones de soporte (`supporting[]`) y la clase ausente (`missing_class`). Esa es, por diseño, la capa que asocia detecciones entre sí. | **Implementado.** |

> ✎ **2026-08-12 — la extensión de tracking dejó de ser hipotética, y es el mejor material que tenemos
> para el tutor.** El pedido fue: *"que den soporte a datos que hoy no están, pero mañana sí"*. Para
> identidad de sujeto, **ese mañana ya pasó y quedó medido**:
>
> - **Se implementó como decorador de FUENTE en el plano de control** —`sources/tracking.py::TrackingSource`,
>   opt-in por `input.track_persons` (default `false`)—, no como paso del plano de medios. Decora cualquier
>   `MediaEventSource`, así que **sirve igual para DBE (archivo) y para EBE (bus)**, y vuelve innecesario el
>   port del `SimpleIoUTracker` que ADR-002 preveía (spec 42 §3).
> - **Resultado medido (campaña G1, `operacion/89`): F1 0,789 → 0,930 con las MISMAS detecciones bit a bit.**
>   La ganancia es 100% del motor: cambió la identidad, no la percepción. Es **el mejor resultado del banco**.
>   Se verificó que el camino config-driven reproduce la campaña exacto ⇒ el 0,930 es lo que rinde la
>   plataforma por YAML, no un script suelto.
> - **Trade-off declarado, y hay que escribirlo:** el `track_id` **no queda en `detections.jsonl`** (la fuente
>   de verdad del plano de medios) sino en los artefactos del control (`subject_key` de `pattern_events.jsonl`).
>   La trazabilidad se conserva porque el tracker es determinista y el stream ordenado: un replay reproduce
>   las mismas identidades. Quien necesite el artefacto con `track_id` embebido lo genera con
>   `python -m eovrt_control.tools.track_detections`.
> - **Lo que sigue sin existir:** las **métricas MOT** (exclusión E-10, ADR-015) y el port al pipeline online.
>   No confundir una cosa con la otra: **lo excluido son las métricas, no la capacidad.**
> - **El núcleo validable sigue siendo escena (G0)** por decisión (D-90.3): G1 se reporta como **capacidad
>   medida**, no como configuración del núcleo.
>
> **Dónde va cada cosa (regla de no-anacronismo):** en **§17.3.11.4** (Etapa 3) va el **estado del contrato**
> —completo en ambos planos, productor no emisor, identidad resuelta en el consumidor— **sin la cifra**. El
> **0,930 y la comparación pareada van a §17.4/§17.5**, que es donde vive la verificación.

### 4.3 El evento, mostrado con su superficie de crecimiento

> ⚠️ **Corregido tras auditoría.** La versión anterior de este bloque mezclaba valores de tres artefactos
> distintos. La detección **emitida hoy** es la línea literal de `frame_000229` (la misma de §2.2,
> re-transcripta el 2026-08-22 sobre el clip vigente `a_p1_c02`), y lo **previsto** va claramente
> separado, en comentarios, sin fingir que existe.

```jsonc
{
  "schema_version": "media.detection.v1",     // aditivo ⇒ NO cambia al agregar campos nuevos
  "run_id": "run_20260803_211225_dbe_grounding_dino_1e06f3",
  "unit_id": "frame_000229",
  "source":  { "source_id": "a_p1_c02", "source_type": "video_frame",
               "frame_index": 229, "timestamp_ms": 7633.33, "width": 1920, "height": 1080 },
  "model":   { "name": "grounding_dino",
               "model_id": "IDEA-Research/grounding-dino-tiny", "device": "cuda" },
  "prompts": { "prompt_set_id": "cr01_cr02_v2_short" },
  "detections": [
    {
      // ================= EMITIDO HOY (línea literal del artefacto) =================
      "detection_id": "det_000001",           // índice por frame: NO es identidad entre frames
      "label": "person", "confidence": 0.88,
      "bbox_xyxy":      [1239.8, 149.8, 1503.2, 861.9],
      "bbox_norm_xyxy": [0.6457, 0.1387, 0.7829, 0.7981],
      "prompt_id": "person", "source_prompt": "person",
      "area_px": 187612.4, "model_name": "grounding_dino"

      // ============ PREVISTO: aditivo, opcional, sin bump de versión ==============
      // "track_id":      "trk_017",      // única identidad válida entre frames (spec 42 §3)
      // "velocity_px_s": [12.4, -3.1],   // derivable de track_id + timestamps ya presentes
      // "heading_deg":   104.2,
      // "keypoints":     [ ... ],        // pose
      // "mask_rle":      "...",          // segmentación
      //
      // "strategy" y "condition_id" existen en el modelo pero hoy valen null y no se
      // serializan. Poblarlos es aditivo y barato — pero HOY NO ESTÁN EN EL EVENTO.
    }
  ],
  "timing": { "normalize_ms": 8.06, "inference_ms": 491.17,
              "postprocess_ms": 0.08, "write_ms": 0.0, "total_ms": 491.27 }
}
```

> **Frase para el capítulo (la que responde al tutor):** *"El contrato del evento de percepción está
> diseñado para crecer sin romperse: los campos nuevos entran como opcionales con valor por defecto y no
> bumpean la versión del esquema, de modo que un consumidor escrito contra `media.detection.v1` sigue
> siendo válido cuando el evento incorpora identidad de sujeto, cinemática, pose o segmentación. La
> identidad de sujeto (`track_id`) ya está prevista en el contrato y consumida por el motor de patrones;
> el plano de medios no la emite, de modo que la identidad se resuelve como capacidad del consumidor y el
> núcleo validable se define sobre granularidad de escena. Se declara explícitamente: `detection_id` es un
> índice por frame y **no** una identidad entre
> frames — usarlo como identidad produce aliasing medible: sobre una corrida de vídeo real, la etiqueta
> `det_000001` recorre 1831 px del ancho del cuadro (de 1920 px) a lo largo de la corrida, con saltos de
> hasta ~1750 px entre cuadros consecutivos."*

> ⚠️ **Corregido tras auditoría.** La formulación anterior decía "recorre 1831 px **entre frames
> consecutivos**", y eso es **falso**: los 1831 px son el **rango total** recorrido a lo largo de la
> corrida; el **salto máximo entre cuadros consecutivos es ~1749 px**. Ambos números destruyen la
> hipótesis de identidad, así que el argumento no se debilita — pero la afirmación original era
> verificable y falsa, que es la peor combinación posible en una defensa.

Ese dato es el que convierte una limitación en un argumento: no elegimos escena por comodidad,
elegimos escena porque **medimos** que la alternativa disponible era identidad falsa.

---

## 5. El plano de control: los otros dos eventos

### 5.1 `PatternStateChanged` — `control.pattern_state.v1`

```python
# control-plane/contracts/pattern.py:31
class PatternStateChanged(BaseModel):
    schema_version: str = "control.pattern_state.v1"
    control_run_id: str
    media_run_id: str
    unit_id: str
    source_id: str
    pattern_id: str
    condition_id: str
    subject_key: str                  # "CR-01:a_p1_c02" bajo escena
    previous_state: str               # inactive | candidate | confirmed | sustained | resolved
    state: str
    severity: str                     # high | medium
    evidence: PatternEvidence
    first_evidence_ms: float          # hito 1 de los cinco obligatorios
    first_evidence_unit_id: str       # clave de join con las métricas del plano de medios
    experiment_id: str | None
```

`subject_key` merece una línea en el capítulo, porque materializa ADR-002:
`f"{pattern_id}:{source_id}"` bajo `granularity: scene`, `f"{pattern_id}:{source_id}:{track_id}"` bajo
`subject`. El docstring del evaluador lo dice sin ambigüedad: *"`detection_id` NO se usa como identidad,
nunca"*.

### 5.2 `AlertEvent` — `control.alert.v1` (la alerta del **benchmark**, no de un smoke)

> ⚠️ **Corregido tras auditoría; ✎ re-transcripta el 2026-08-22 sobre clip VIGENTE.** La primera versión
> mostraba la alerta de una corrida **mock**; la segunda, la del benchmark del 2026-07-12 sobre
> `cb_b01_p7`, clip después **retirado del banco**. La alerta de abajo es la del **replay real con
> GDINO-tiny sobre `a_p1_c02`** (banco vigente, campaña del banco congelado), reproducido y archivado en
> `operacion/datos/129-2026-08-22-bench-a_p1_c02-gdino-alerts.jsonl`. La cadena temporal se lee entera:
> primera evidencia en `frame_000109` (3.633,33 ms de video) → confirmación en `frame_000229`
> (7.633,33 ms) = **los 4.000 ms exactos de la ventana de CR-01**; contra el inicio anotado del episodio,
> el `t_alert-system` de este clip es **4.600,33 ms** (TTFD 600,33 + 4.000 de espera deliberada) — la
> descomposición que separa cómputo de persistencia, con la re-alerta posterior en `frame_000764`.

```json
{ "schema_version": "control.alert.v1", "event_type": "alert_event",
  "control_run_id": "bench_a_p1_c02_gdino_20260822_20260822T225536Z",
  "media_run_id":   "run_20260803_211225_dbe_grounding_dino_1e06f3",
  "alert_id": "394c9116-a38d-568d-b620-20d147c4cac9",
  "pattern_id": "CR-01", "condition_id": "CR-01",
  "subject_key": "CR-01:a_p1_c02", "source_id": "a_p1_c02",
  "severity": "high", "state": "open",
  "unit_id": "frame_000229", "frame_index": 229, "timestamp_ms": 7633.33,
  "evidence": {
    "subject": { "detection_id": "det_000001", "label": "person", "confidence": 0.88,
                 "bbox_xyxy": [1239.8, 149.8, 1503.2, 861.9] },
    "missing_class": "helmet",
    "supporting": [],
    "score": 0.88, "subjects_in_evidence": 1,
    "rationale": "No se encontro evidencia 'helmet' en region 'upper_body' de 1 sujeto(s)." },
  "subjects_in_evidence_max": 1,
  "first_evidence_ms": 41990631.527, "first_evidence_unit_id": "frame_000109",
  "first_evidence_frame_index": 109,
  "alert_registered_ms": 41990642.511,
  "experiment_id": null }
```

Cuatro cosas para señalar en el texto:

1. **`alert_id` es un uuid5 determinista** (`pattern_engine.py:517`) ⇒ la alerta es **idempotente**:
   reprocesar la misma corrida produce el mismo identificador, y un consumidor aguas abajo puede
   deduplicar sin estado compartido.
2. **`rationale` en lenguaje natural + `subject` + `supporting[]` + `missing_class`**: la evidencia de la
   ausencia es **auditable**. Es el argumento a favor de E-IND frente al prompt de negación, hecho
   artefacto. Esto es lo que un prompt de negación **no puede darte**.
3. **La confirmación cae exactamente 4.000 ms después de la primera evidencia** —
   `frame_000109` (3.633,33 ms) → `frame_000229` (7.633,33 ms): la ventana de persistencia
   configurada para CR-01, al milisegundo. El sistema hace lo que su configuración declara,
   y los hitos `first_evidence_*` del propio evento permiten verificarlo sin salir del artefacto.
4. **`experiment_id: null`**: esta corrida se disparó por CLI, sin manifiesto paraguas. Es honesto y vale
   la pena verlo — el campo existe y viaja; en esta corrida puntual no se lo pobló.

---

## 6. Configuración: los valores efectivos (que el capítulo nunca da)

El capítulo no contiene **una sola cifra**. Estos son los valores que gobiernan el núcleo validable hoy.

### 6.1 Pattern set oficial — `control-plane/configs/patterns/cr01_cr02_v2.yaml`

```yaml
pattern_set:
  id: cr01_cr02_v2
  patterns:
    - id: CR-01                       # persona sin casco
      severity: high
      subject_class: person
      required_absent_class: helmet
      granularity: scene              # ADR-002 — G0 es el núcleo
      region:   { type: upper_body, y_min_ratio: 0.0, y_max_ratio: 0.45, x_margin_ratio: 0.12 }
      evidence: { min_subject_confidence: 0.35, min_absent_class_confidence: 0.25,
                  min_subject_area_px: 400.0 }
      timing:   { confirm_after_ms: 4000.0, resolve_after_ms: 2000.0 }

    - id: CR-02                       # persona sin chaleco
      severity: medium
      required_absent_class: vest
      granularity: scene
      region:   { type: torso, y_min_ratio: 0.25, y_max_ratio: 0.85, x_margin_ratio: 0.08 }
      timing:   { confirm_after_ms: 7000.0, resolve_after_ms: 3000.0 }
```

**El pattern set oficial no configura `cooldown`** ni memoria de cobertura.

> ⚠️ **Matiz obligatorio (corregido tras auditoría).** No escribas "el cooldown no existe en el motor":
> **sí existe** — `PatternTimingConfig.realert_cooldown_ms` / `realert_cooldown_frames`
> (`control-plane/config.py:82-83`) y `PatternEngine._cooldown_ok()` (`engine/pattern_engine.py:477-499`).
> Lo que ocurre es que **el pattern set oficial lo deja sin configurar (`None` ⇒ desactivado)**, y ADR-011
> §3 lo declara literalmente *"capacidad no usada por la plataforma"*: la política de supresión vive en el
> tramo de distribución. La formulación correcta para el informe es **"el motor no suprime: emite en cada
> confirmación, porque el conjunto de patrones adoptado no configura supresión"**, no "el motor no puede
> suprimir". Si alguien abre `pattern_engine.py` y encuentra un cooldown que el informe negaba, el daño es
> mayor que el beneficio de la frase simple.

Y **sin memoria de cobertura** (ADR-012: inaplicable bajo escena — la histéresis subsume el parpadeo del
detector).

**Alineación con el informe:** CR-01 → `high`, persistencia 4000 ms (banda del informe: alto, 3–5 s ✓).
CR-02 → `medium`, persistencia 7000 ms (banda: medio, 5–10 s ✓). La persistencia se expresa **en
milisegundos, no en frames**, como exige §17.1.5.3.3.

### 6.2 Umbrales del plano de medios (`config/schemas.py`)

`box_threshold 0.35` · `text_threshold 0.25` · `confidence_threshold 0.25` · `iou_threshold 0.50` ·
postproceso `min_confidence 0.25`, `min_box_area_px 100.0` · `rate_control.stride 1`, `max_queue_size 8`.

> ✎ **2026-08-19 — estos son los DEFAULTS del schema, NO la configuración efectiva del campeón.**
> El perfil desplegado `grounding-dino/gdino-tiny-560` sobreescribe `box_threshold` a **0.30**
> (`configs/models/grounding-dino/gdino-tiny-560.yaml`), y las campañas oficiales corrieron con
> 0.30 (los `model_note` de `experimental-setup/results/` lo consignan textualmente). Además,
> `confidence_threshold` es un campo del carril YOLOE: para GDINO el gate efectivo es
> `box_threshold` + `postprocess.min_confidence`. **Al informe va 0.30** — el 0.35 de la línea
> de arriba ya contaminó el borrador de §17.4.6 (corregido en
> `entregable/desarrollando/correcciones-etapa-3-4.md`, ítem E4-12).

### 6.3 Prompt set del núcleo (E-IND) — `experimental-setup/prompts/cr01_cr02_v2_short.yaml`

`person` (rol: entidad) · `helmet`, `vest` (rol: EPP). Evidencia **positiva**: la ausencia no se pregunta
al modelo, se **infiere** en el plano de control. Es la materialización de ADR-001.

---

## 7. Cómo se mide (definiciones operacionales)

El tutor pidió "cómo se mide para saber si funciona bien". Estas son las definiciones **implementadas**,
no las deseadas. Cada una tiene t0, t1 y su condición de aplicabilidad.

| Métrica | t0 | t1 | Implementación |
|---|---|---|---|
| **G2A** | captura de la unidad (`capture_monotonic_ns`) | fin de la inferencia | `MetricSample.g2a_ms` por unidad + `G2ASummary` p50/p95/p99 + `p95_within_budget: bool`. Presupuesto declarado: **50–250 ms**. |

> 🔴 **HALLAZGO CORREGIDO — leer antes de escribir una sola línea sobre G2A.**
> El número que veníamos citando (**p50 14,7 ms / p95 31,8 ms, "dentro de presupuesto"**) es de una corrida
> con **detector `mock`** (doc 39: `EOVRT_MODEL_REF=mock`, 20 unidades). **No es evidencia de que el sistema
> cumpla el presupuesto.**
>
> La corrida **real** con GDINO-tiny dice lo contrario. Sobre el clip vigente `a_p1_c02`
> (`run_20260803_211225…`, 1.123 unidades, `summary.json` archivado en
> `operacion/datos/129-2026-08-22-bench-a_p1_c02-gdino-summary.json` junto a las alertas):
> **`g2a: p50 1473,1 ms · p95 4953,9 ms · p95_within_budget: false`** — un orden de magnitud **por encima**
> del presupuesto 50–250 ms. (La corrida histórica del 07-12 sobre el clip luego retirado decía lo mismo:
> p95 2604,1 ms, `false`.)
>
> **No lo escondas: convertilo en hallazgo.** Es exactamente el mismo resultado que el conflicto
> CR-01 ↔ tiempo real del doc 31 (GDINO sostiene CR-01 pero sólo sigue el 14–22 % del ritmo de cámara), y
> refuerza la tesis en vez de debilitarla: *la instrumentación **funciona** — mide, compara contra el
> presupuesto y **declara el incumplimiento sola** (`p95_within_budget: false`)*. Un instrumento que sólo
> devuelve verdes no es un instrumento.
>
> Formulación correcta para el informe: *"la instrumentación de G2A opera y detecta el incumplimiento: con
> detector de referencia el p95 es de 31,8 ms (dentro del presupuesto), mientras que con el detector
> open-vocabulary evaluado el p95 asciende a 4.953,9 ms y el sistema lo declara fuera de presupuesto. La
> latencia del detector, y no la instrumentación, es la restricción operativa."*
| **TTFD** | inicio del episodio en el GT | primera detección positiva dentro del episodio | `_ttfd_for_episode` (`evaluation/temporal.py:438`). Si no hay ninguna: **`None` + `no_positive_detected`** — nunca 0.0 por defecto. |
| **`t_alert-system`** | inicio anotado del episodio | alerta interna registrada | `avg_latency_ms_from_episode_start`. |
| **TTFA interna** | `first_evidence_ms` | `alert_registered_ms` | percentiles en `RunSummary.ttfa_internal_ms_percentiles`. |
| **SDR** | — | — | fracción del episodio `[start,end]` cubierta por detección positiva continua; tramos con hueco ≤ paso nominal se fusionan; clampeado a `[0,1]` (`_sdr_for_episode`, `:457`). |
| **Precision / Recall / F1** | — | — | a **nivel episodio**, con ventana de matching en ms. `precision = matched / (matched + unexpected)`: las **re-alertas no entran al denominador** (ADR-011), y los `sub_threshold_events` tampoco. |
| **`t_capture→alert`** *(derivada propia)* | captura del frame de primera evidencia | alerta registrada | Join entre planos por `first_evidence_unit_id`. **Identidad declarada:** `t_alert-system = TTFD + t_capture→alert`. |

**Criterio de detección positiva** (y esto es importante, porque cierra el círculo): el evaluador **no
reimplementa** el criterio — reusa el evaluador real del motor
(`evaluate_spatial_absence(event, pattern).evidences != []`). El artefacto lo declara literalmente:
`"positive_criterion": "spatial_absence(cr01_cr02_v2) >=1 evidencia"`. No hay dos definiciones de "positivo"
que puedan divergir en silencio.

**Criterio de relojes** (el hueco de la Etapa 3): las latencias intra-nodo usan reloj monotónico local; las
end-to-end se miden **en un solo reloj**. **Los monotónicos de dos hosts no se restan** — en two-node, G2A
se declara `not_interpretable / cross_node_monotonic_clock` y `g2a_ms` va `null`. No se publica un número
que no significa nada.

**Estados de aplicabilidad** (§17.3.13.3, hecho campo literal):
`computed | applicable_not_computed | not_applicable | not_interpretable`, siempre con `cause`. Ejemplos
reales del `report.json`: `t_alert→notification` → `not_applicable / no_distribution` (no hay canal);
`t_capture→alert` → `not_interpretable / dbe_media_time` (reloj de medio, no de pared).

---

## 8. Artefactos de una corrida (el "sistema ejecutable y verificable")

```
media-plane   runs/<run_id>/
              ├── detections.jsonl        # media.detection.v1, append-only
              ├── metrics.jsonl           # media.metric.v2 (incluye g2a_ms por unidad)
              ├── errors.jsonl
              ├── summary.json            # media.summary.v2
              ├── effective_config.yaml   # config efectiva (credenciales redactadas)
              ├── run_manifest.json       # incluye code_version: "<git sha>"
              └── run_provenance.json     # dataset, split, vocabulario, fingerprint de la fuente

control-plane runs/<control_run_id>/
              ├── pattern_events.jsonl    # control.pattern_state.v1
              ├── alerts.jsonl            # control.alert.v1
              ├── alerts.csv              # proyección tabular de las alertas
              └── metrics.jsonl · errors.jsonl · summary.json · effective_config.yaml
              #  temporal_evaluation.json NO vive acá por defecto: lo escribe `evaluate-alerts`
              #  donde apunte su flag -o (normalmente, bajo el run de experimental-setup).

experimental- runs/<experiment_id>/       # la corrida paraguas (ADR-014)
setup         ├── manifest.effective.yaml    # experiment.manifest.v1 (+ clip_id, ground_truth)
              ├── media/    …  control/   …  # lo liviano se copia
              ├── media/detections.ref.json  # lo pesado se REFERENCIA: {run_id, path}
              └── report/{report.json, report.md}
```

**`run_manifest.json` lleva el `code_version` (SHA de git).** Junto con `effective_config.yaml` y el
`run_provenance.json`, cierra la promesa de trazabilidad del §17.3.11.1: **toda alerta se reconstruye hasta
la configuración, el prompt set, el modelo y el commit que la produjeron.**

---

## 9. Puntos de extensión del sistema (el "cómo agrego X")

| Extender con… | Qué hay que tocar |
|---|---|
| **Una fuente nueva** | Implementar `BaseSource` (yield de `VisualUnit`) + una entrada en `PLUGINS` (`sources/registry.py:25`). Hoy: `image_folder`, `video_file`, `rtsp`, `oak_d` (implementado 2026-07-13; `available` refleja si el SDK DepthAI está instalado, y una build sin él sigue dando 4xx explícito, no 500). |
| **Un modelo nuevo** | Subclase de `BaseDetectorAdapter` + rama en `create_adapter()` + un YAML en `configs/models/`. Hoy: `grounding_dino`, `yoloe`, `mock`. |
| **Una condición de riesgo nueva** | **Sólo configuración**, si la condición es del tipo "sujeto sin EPP": una entrada declarativa en el pattern set (clase sujeto, clase ausente, región, umbrales, tiempos) + los prompts. **Cero código.** Este es el mini-experimento A1 (costo marginal de una condición nueva) y es un resultado de tesis en sí mismo. |
| **Un tipo de patrón nuevo** (p. ej. relacional o zonal) | Un evaluador nuevo en `engine/evaluators/`. Hoy sólo existe `spatial_absence`. |
| **Un canal de notificación** | Implementar `Channel` contra `NotificationEnvelope`. El canal MQTT existe y está verificado; agregar otro canal queda fuera del recorte ADR-005/E-06. |

El contraste entre las filas 3 y 4 es, en sí, un argumento de la tesis: **agregar una condición del núcleo
cuesta configuración; agregar una familia nueva de condiciones cuesta un evaluador.** Esa es la frontera
real de la extensibilidad por lenguaje, y conviene medirla y declararla en vez de prometer que "todo es
configurable".

---

## 10. Números canónicos — ~~la única fuente de verdad para citar cifras~~ **DEROGADA como fuente**

> 🚨 **✎ 2026-08-12 — esta sección quedó DEROGADA como fuente de números el 2026-08-05. No cites de acá.**
> Las cifras del informe salen de los **cuatro índices de `e-ovrt_experimental-setup/results/`**
> (`bench_imagenes/`, `bench_nivel_a/`, `clip_bench/`, `realtime/`), verificables con
> `operacion/datos/96-verificar-indices.py`. La tabla de abajo es de **julio**, corrió sobre **GT
> preliminar** y quedó ampliamente superada por el banco de 34 clips con GT humano.
>
> **Para qué sigue sirviendo:** para saber **qué corrida y qué detector produjeron un artefacto** — que es
> el problema que esta sección vino a resolver. Esa función se conserva; la de citar valores, no.

> **Regla original, tras la auditoría del 2026-07-12:** ninguna cifra entra a los docs 91/93/94 —ni al
> `.docx`— si no está en esta tabla. Cada fila dice **qué corrida** la produjo y **con qué detector**, porque
> la mitad de los errores encontrados venían de citar un número de una corrida y atribuirlo a otra.
> *(El espíritu sigue vigente con la fuente cambiada: si una cifra no está en un índice verificable, no
> entra.)*

| Cifra | Valor | Corrida / detector | Artefacto |
|---|---|---|---|
| **Benchmark contra GT temporal** (el número estrella) | **P 0,50 · R 1,00 · F1 0,667 · t_alert-system 4000,0 ms · TTFD 0,0 ms · SDR 0,9986** | `cb_b01_p7`, **GDINO-tiny**, DBE replay, GT **preliminar** | `operacion/datos/95-2026-07-12-bench-cb_b01_p7-gdino-temporal_evaluation.json` ✅ **reproducido y archivado el 2026-07-12** |
| Alertas del benchmark | 2 (CR-01 `high` @ 4000,0 ms · CR-02 `medium` @ 7000,0 ms). 1 TP + 1 FP; `re_alerts: 0` | ídem | `…-gdino-alerts.jsonl` |
| Percepción sobre vídeo real | 733 unidades · **0 fallos** · 15.914 detecciones · p50 220,2 ms · p95 266,8 ms · **4,39 fps** · VRAM 1745 MB | `run_20260711_211647`, **GDINO-tiny**, clip `cb_b01_p7` | `…-gdino-media-summary.json` |
| **G2A con detector real** | **p50 2214,2 ms · p95 2604,1 ms · `p95_within_budget: false`** | ídem (**GDINO-tiny**) | ídem |
| G2A con detector de referencia | p50 14,7 ms · p95 31,8 ms (dentro de 50–250 ms) | doc 39, **mock**, 20 unidades | `operacion/datos/39-…-g2a-video-summary.json` |
| Byte-identidad replay ≡ live | artefactos idénticos; **40/40** unidades, 0 pérdidas | doc 37, **mock** | `operacion/datos/37-…` |
| Cadena live completa por bus | **300/300** unidades, 0 pérdidas, 2 alertas, cierre por `run_finished` | doc 51, **mock** | `operacion/datos/51-…` |
| Gate de granularidad | **F1 = 1,0** en escena y sujeto; 141 personas ⇒ 77 alertas, Σ`subjects_in_evidence_max` = 141 | doc 34, BENCH imágenes | doc 34 |
| "Cero silencioso" sobre imágenes | **77 pattern_events · 0 alertas**, `not_applicable / non_temporal_source` | `bench_images_persistence_probe_20260710` | run del control-plane |
| Aliasing de `detection_id` | rango total **1831 px** de 1920; salto máx. entre cuadros consecutivos **~1749 px** | `run_20260710_011320` | doc 35 |
| Benchmark de modelos OVD | **6 modelos**. GDINO-tiny mAP@0.5 **0,4577**; GDINO-base recall CR-01 **0,586**; YOLOE recall CR-01 **0,000–0,014** (0–1 `bare_head` sobre 69 de GT) | doc 31 | doc 31 (⚠️ sin artefacto primario) |
| Keep-up RTSP | GDINO **14–22 %** · YOLOE **58–69 %** | doc 31 | ídem |
| Suites de test | datasets 102 · media-plane 520 · control-plane 212 · exp-setup 247 | 2026-07-12 | recolectadas |

**Cifras retiradas por la auditoría (NO usar):**
- ~~"137 eventos de patrón / 0 alertas"~~ → el run fue podado. El equivalente vivo da **77 / 0**.
- ~~"G2A p95 31,8 ms ⇒ el sistema cumple el presupuesto"~~ → era **mock**. Con GDINO **no cumple**.
- ~~"1831 px entre frames consecutivos"~~ → 1831 px es el **rango total**.
- ~~"los 5 modelos evaluados"~~ → son **6**.
- ~~SDR 0,803~~ → ese es el **smoke con mock**, no el benchmark. El benchmark da **0,999**.

---

## 11. Checklist de transcripción al `.docx`

- [ ] §17.3.11 — reemplazar el hedge por la tabla de correspondencia (§1) y los tres contratos concretos (§2, §5).
- [ ] §17.3.11.4 — regla de evolución aditiva + evento con superficie de crecimiento (§4). **Es el pedido T3 del tutor.**
- [ ] §17.3.5 — figura nueva: vista de procesos (dos servicios HTTP + bus + orquestador + webconsole). (✎ 2026-08-28: **FIG-A tiene destino único §17.4.1** desde el 08-19 (`08-manual` §6), son **tres** servicios HTTP, y el orden de arranque dibujado es **control → distribución → medios** (`operacion/130` R-01); producida el 08-21 y regenerada el 08-28 en `informe/figuras/`.)
- [ ] §17.3.8.1 y §17.3.8.4 / §17.3.12 — bus concreto (§2.3) y layout del repositorio (§8).
- [ ] §17.3.6 / Tabla 44 — configuración con **valores efectivos** (§6), y el matiz correcto del `cooldown`.
- [ ] §17.3.13 — diccionario de métricas con t0/t1 (§7), criterio de relojes y estados de aplicabilidad.
- [ ] §17.3.15 — tabla rol → contenedor (Nodo A ≈ EN-1, Nodo B ≈ CPN).
- [ ] §17.3.17/18 — puntos de extensión (§9): **el costo marginal de una condición nueva es configuración**.
- [ ] Sección de verificación — números de la §10 (y sólo esos) + registro de lo no hecho.

---

## Fuente: `docs/informe/ajustes/material-etapa-3/92b-concrecion-distribucion-alertas.md`

> SHA-256 del bloque: `f22b60bacda8f19af4bdac970d130e2a1034e4462c2e0c7bf8f02f68023a8f7b`  
> Seleccion: documento completo.

# 92b — Concreción técnica: módulo de distribución de alertas

- **Fecha:** 2026-08-10
- **Qué es esto:** la descripción completa del **módulo de distribución de alertas**
  (`e-ovrt_alert-distribution`) a nivel de concreción técnica — frontera, arquitectura,
  contratos serializados, política, configuración, salidas e integración. Es el material
  del que se escribe **§17.3.10** del informe, en el mismo registro que el `informe/92`
  (contratos y rutas, no cifras).
- **Estado de implementación:** ✎ **2026-08-12 — funcionalmente implementado y
  verificado.** El pipeline completo existe en `e-ovrt_alert-distribution` y cerró los
  seis criterios de spec 45: replay DBE idempotente, consumo EBE desde el publisher real,
  cooldown, deduplicación, MQTT QoS 1 contra broker real e integración en `report.json`.
  Evidencia y salvedades: `operacion/114`. ✎ **2026-08-14:** la vista de outcomes en la
  webconsole, la orquestación integral y el versionado del repo —que este encabezado daba
  por pendientes— se cerraron el 2026-08-13 (`13c801e`, `42529e2`; repo con `c9903cc` y
  `1e6d8fa`). **E-06 sigue excluida.** Las latencias de smoke/loopback no se citan como resultado de desempeño.
  *Decía “diseñado y especificado; implementación pendiente” y luego “trabajo
  comprometido” por ADR-016.*
- **Normativa que lo gobierna** (todos de la **serie del proyecto**, `ADR-001…018` —
  no confundir con la serie interna del control-plane, `ADR-0001…0013` de 4 dígitos):
  **ADR-016** (reapertura acotada: el estatuto vigente del módulo), ADR-005 (recorte,
  canal MQTT, repo propio), ADR-011 (frontera de la política: el motor
  emite siempre, la supresión es de distribución), ADR-004 (`experiment_id`),
  ADR-006/013 (aplicabilidad y relojes), ADR-007 (semántica 1:1), spec 45 (spec
  recortada), `nucleo/06` (anexo de diseño completo, E-06) y **`nucleo/19`** (el cierre
  arquitectónico del ciclo de vida de la alerta, que consolida todo lo anterior).
- **Redlines que alimenta:** **R-02** — su "DEBE DECIR" pide exactamente el párrafo de
  §17.3.10.3 sobre dónde vive la política de notificación y por qué las re-alertas no
  son falsos positivos (desarrollado en §5 de este doc) — y **R-13**, que lista la
  distribución entre los límites que sobreviven y hay que declarar.

---

## 1. Qué es, y sobre todo qué no es

Consumidor **desacoplado** de alertas **ya confirmadas** por el control-plane. Las
recibe (del bus en vivo o de `alerts.jsonl` en diferido), decide **cuáles se convierten
en notificación**, las entrega por **MQTT** y registra el intento y su resultado.

**La frontera es estricta y es la razón de ser del módulo** (§17.3.10.1, DA-13): el
distribuidor **nunca** recalcula severidad, **nunca** muta el estado de un patrón y
**nunca** crea alertas. Solo consume, decide notificación y registra. Que viva en un
**repo hermano propio** —y no dentro del control-plane— materializa esa frontera en la
estructura misma del sistema (ADR-005, que supera la ubicación propuesta en `nucleo/06`
§4).

La cadena conceptual completa, y cada eslabón con su dueño:

| Eslabón | Qué decide | Dónde vive |
|---|---|---|
| **Detección** | qué hay en el frame | media-plane |
| **Patrón** | si la condición se sostiene en el tiempo | control-plane (motor) |
| **Alerta** | que el patrón se confirmó | control-plane (`control.alert.v1`) |
| **Notificación** | si a esta alerta hay que avisarle a alguien, y por dónde | **este módulo** |

El **recorte** respecto del diseño completo del `nucleo/06` (lo excluido queda como
E-06, anexo): **un solo canal** (MQTT; sin Telegram ni webhook), **sin dashboard propio**
(la webconsole muestra los resultados), **retry mínimo** (N intentos fijos, sin backoff
exponencial) y **dead-letter simple** (archivo de agotadas, sin comando de reproceso).

---

## 2. Arquitectura: un pipeline de cinco etapas

```
                    ┌───────────── e-ovrt_alert-distribution ─────────────┐
                    │                                                     │
  control-plane     │  ┌────────┐   ┌────────┐   ┌────────┐   ┌────────┐  │
  ───────────────►  │  │ SOURCE │──►│ POLICY │──►│ LEDGER │──►│ CHANNEL│──┼──► MQTT
   control.alert.v1 │  └────────┘   └────────┘   └────────┘   └────────┘  │    (broker)
   ó alerts.jsonl   │      │            │            │            │       │
                    │      │            │            │            │       │
                    │      └────────────┴────────────┴────────────┘       │
                    │                        │                            │
                    │                   DeliveryRecord                    │
                    │       notifications.jsonl · dead_letter.jsonl       │
                    │              distribution_summary.json              │
                    └─────────────────────────────────────────────────────┘
```

Una alerta atraviesa las etapas **en este orden**, y sale del pipeline en la primera que
la resuelva. Cada salida produce un `DeliveryRecord` — **ninguna alerta desaparece en
silencio**, que es la propiedad de observabilidad que el módulo garantiza:

1. **Source** — entrega la alerta cruda, venga del archivo o del bus.
2. **Policy** — cooldown de notificación (ADR-011). Si suprime → `suppressed_cooldown`.
3. **Ledger** — idempotencia. Si ya se entregó → `skipped_duplicate`.
4. **Channel** — entrega con reintentos. Éxito → `delivered`; cada intento fallido →
   `failed`; agotados → `dead_letter`.
5. **Records** — todo lo anterior se escribe append-only y se agrega en el summary.

**Policy y Ledger son capas distintas y las dos hacen falta** — es la distinción que más
se confunde al leer el módulo: el **ledger deduplica exactos** (la *misma* alerta
reprocesada, p. ej. porque MQTT QoS 1 reentregó o porque se re-corrió el replay); el
**cooldown suprime semánticos** (alertas *distintas*, de la misma condición y cámara,
demasiado seguidas).

---

## 3. Contratos serializados

### 3.1 Entrada: `control.alert.v1` (del control-plane)

El módulo no define este contrato, lo consume. Campos que usa:

| Campo | Uso en distribución |
|---|---|
| `alert_id` | identidad; deriva el `notification_id` |
| `control_run_id`, `media_run_id` | trazabilidad de corrida |
| `pattern_id`, `condition_id` | qué se confirmó |
| `source_id` | qué cámara — **parte de la clave de cooldown** |
| `subject_key` | qué sujeto (bajo G1 incluye `track_id`) |
| `severity` | enruta el topic MQTT |
| `state` | estado del episodio al distribuir |
| `timestamp_ms` | tiempo **de media** — base temporal del cooldown |
| `evidence` | referencias mínimas, se propagan sin interpretarse |
| `experiment_id` | ADR-004; viaja hasta el reporte |

> **Precisión sobre `nucleo/06` §6.1:** aquel diseño preveía un `confirmed_at_ms` en el
> envelope. El `AlertEvent` real **no tiene ese campo**: el tiempo de media es
> `timestamp_ms`, y el instante de pared solo existe en vivo, donde lo aporta el
> `ts_publish_ms` del envelope del bus. El contrato de abajo refleja el evento real.

### 3.2 `NotificationEnvelope` — `control.notification.v1`

Evento **derivado** con contexto mínimo (§17.3.10.1): no reemplaza a la alerta interna,
la referencia.

```python
class NotificationEnvelope(BaseModel):
    schema_version: str = "control.notification.v1"
    event_type: str = "notification_envelope"
    notification_id: str            # sha1(alert_id)[:16] — determinista
    control_run_id: str
    media_run_id: str
    alert_id: str                   # referencia, no reemplazo
    pattern_id: str
    condition_id: str
    source_id: str
    subject_key: str
    severity: str
    episode_state: str
    media_timestamp_ms: float | None = None   # tiempo de media
    confirmed_wall_ms: float | None = None    # ts_publish_ms del bus; None en replay
    evidence_ref: dict | None = None
    summary_text: str               # texto humano breve, para mensajería
    experiment_id: str | None = None
```

**`notification_id` determinista** (`sha1(alert_id)[:16]`) es lo que vuelve la
idempotencia una propiedad *por construcción* y no un cuidado del operador: reprocesar
la misma alerta produce siempre la misma clave, así que el ledger la reconoce.

### 3.3 `DeliveryRecord` — `control.delivery.v1`

Observabilidad del tramo (§17.3.10.3): separa **alerta confirmada**, **intento** y
**resultado**, sin tocar la semántica del evento interno.

```python
Outcome = Literal["delivered", "failed", "skipped_duplicate",
                  "dead_letter", "suppressed_cooldown"]

class DeliveryRecord(BaseModel):
    schema_version: str = "control.delivery.v1"
    event_type: str = "delivery_record"
    control_run_id: str
    notification_id: str
    alert_id: str
    channel: str                    # "mqtt" en esta iteración
    mode: Literal["dry_run", "live"]
    attempt: int                    # 0 para supresiones/duplicados; 1..N para envíos
    outcome: Outcome
    error: str | None = None
    talert_notification_ms: float | None = None
    latency_mode: Literal["live", "wall_clock_dbe"] | None = None
    attempted_at: str               # ISO-8601 UTC
    delivered_at: str | None = None
    experiment_id: str | None = None
```

Los cinco `outcome` y qué significa cada uno:

| Outcome | Significa | ¿Es un error? |
|---|---|---|
| `delivered` | entregada y confirmada por el broker | no |
| `suppressed_cooldown` | la condición en esa cámara ya se avisó dentro de la ventana | **no** — es la política funcionando |
| `skipped_duplicate` | esa alerta exacta ya se había entregado | **no** — es la idempotencia funcionando |
| `failed` | un intento falló; quedan reintentos | parcial |
| `dead_letter` | se agotaron los intentos | sí |

---

## 4. Fuentes: el mismo distribuidor para DBE y EBE

| Fuente | Camino | Uso |
|---|---|---|
| `JsonlReplaySource` | **DBE** | relee `runs/<id>/alerts.jsonl` de una corrida del control-plane. Post-run, idempotente, re-ejecutable |
| `ZmqSource` | **EBE** | suscripta a `control.alert.v1.*` en el bus, **con backfill** desde `alerts.jsonl` al conectar |
| `DirectSource` | tests | iterable en memoria, sin sockets |

Las tres entregan `SourcedAlert(alert: dict, ts_publish_ms: float | None)` y alimentan
**el mismo `Distributor`**: el camino de distribución es idéntico en los dos escenarios,
y lo único que cambia es de dónde llegan las alertas. Es la misma propiedad de paridad
DBE↔EBE que sostiene el resto de la plataforma.

**El backfill no es un detalle de implementación, es la corrección de un defecto
estructural del bus**: PUB/SUB pierde todo lo publicado antes de que el consumidor se
suscriba. Como el JSONL del control-plane es la verdad, `ZmqSource` lo lee al conectar y
deduplica por `alert_id` contra lo que después llegue por el stream — de modo que una
alerta emitida antes de la suscripción se notifica igual.

Reglas del bus que el módulo respeta (spec 40 §3.2):

- Envelope `bus.envelope.v1`, dos frames: `[topic-utf8, msgpack{...}]`, con el
  `AlertEvent` serializado como `payload`.
- Suscripción a los prefijos `control.alert.v1.` y `run.lifecycle.v1.`; el
  `run_finished` del lifecycle **cierra la corrida de distribución** (semántica 1:1,
  ADR-007).
- **Los huecos de `seq` se cuentan** (`bus_dropped_events`) y degradan la corrida;
  nunca se silencian.
- **Parada cooperativa**, no cierre desde otro hilo: `request_stop()` levanta un flag y
  el socket se cierra en el mismo hilo que hace `recv` — cerrarlo desde afuera con un
  `recv` en curso aborta el proceso con `SIGABRT` (trampa de libzmq, no negociable en
  todo el workspace).

---

## 5. Política de notificación: dónde vive el cooldown, y por qué

**ADR-011 es la decisión que da forma a este módulo.** El control-plane emite un
`AlertEvent` **cada vez** que un patrón se confirma, sin supresión: `alerts.jsonl` es el
registro fiel de la dinámica del patrón. Quién decide cuántas veces molestar a un
consumidor es el distribuidor.

```yaml
notification_policy:
  cooldown_ms: 30000                 # ventana de supresión
  key: [condition_id, source_id]     # sobre qué se suprime
```

La clave es `(condition_id, source_id)` —no el sujeto— porque para notificación
asistiva lo relevante es *"esta condición en esta cámara ya fue avisada"*. Una ráfaga de
tres personas sin casco en la misma cámara en diez segundos es **un aviso**, no tres.
La base temporal es `media_timestamp_ms` (coherente entre replay y vivo), con fallback a
reloj de pared si la alerta no trae tiempo de media.

Esta ubicación tiene tres consecuencias que el informe declara:

1. **Frontera limpia:** detección ≠ patrón ≠ alerta ≠ notificación.
2. **Métricas más honestas:** con la supresión en el motor, la tasa de re-alertas
   —que es señal de estabilidad perceptual— quedaba oculta. Emitiendo siempre, esa señal
   se mide; suprimirla es decisión del consumidor. Es también la razón por la que
   **`re_alerts` no se cuentan como falsos positivos** en la evaluación.
3. **Corrige dos defectos** detectados al revisar el cooldown del motor: quedaba inerte
   frente a las ventanas del informe (ciclo de re-alerta 6–10 s > cooldown de 5 s), y
   bajo granularidad de escena cambiaba de significado por accidente de la clave de
   estado (*"mismo trabajador"* pasaba a *"misma cámara"*). Acá la ventana se define
   explícitamente sobre `(condición, fuente)`, que es lo correcto.

Toda supresión **queda registrada** (`suppressed_cooldown`) y contada en el summary: la
política es auditable, no invisible.

---

## 6. Ledger de idempotencia

Clave `(notification_id, channel)`. El respaldo es el propio `notifications.jsonl`
append-only: al construirse, el ledger se rehidrata leyendo los registros `delivered`
previos. **Solo `delivered` marca como visto** — un `failed` o un `suppressed_cooldown`
no bloquean un intento posterior.

[Enmienda 2026-08-14] Al reabrir un directorio ya usado, la generación anterior se
conserva íntegra como `notifications.<n>.jsonl` (y `dead_letter.<n>.jsonl`): el archivo
vigente corresponde a la ejecución en curso y ninguna fila se pierde.

Esto da dos garantías operativas:

- **Re-ejecutar el replay es seguro:** la segunda corrida sobre la misma entrada produce
  `skipped_duplicate` en el 100% de los casos, sin re-entregar nada.
- **MQTT QoS 1 puede duplicar** (garantiza *al menos una* entrega): el ledger no es
  opcional, es la contraparte obligatoria de haber elegido QoS 1.

---

## 7. Canal MQTT

Único canal de esta iteración (ADR-005). Elegido por tres razones defendibles: peso
mínimo (Mosquitto en el compose de la plataforma), es **estándar de integración IoT**, y
permite medir `t_alert-notification` limpio, sin la variabilidad de una API externa
ajena al sistema.

| Aspecto | Definición |
|---|---|
| Topic | `eovrt/alerts/<severity>` |
| Payload | el `NotificationEnvelope` serializado a JSON |
| QoS | **1** (al menos una entrega) ⇒ el ledger deduplica |
| Modo `dry_run` | **default**: construye el payload y lo registra **sin I/O** — la CI cubre el pipeline entero sin broker |
| Modo `live` | `paho-mqtt` (extra opcional `[mqtt]`), conexión lazy, `publish` + espera de PUBACK |
| Credenciales | **solo por entorno** (`EOVRT_MQTT_USERNAME` / `EOVRT_MQTT_PASSWORD`) — jamás en configs versionadas ni en artefactos |

Que `dry_run` sea el default no es comodidad: es lo que permite que el módulo completo
sea testeable y reproducible sin infraestructura, igual que el resto de la plataforma.

**Retry:** `max_attempts: 3` con espera fija (`wait_ms: 500`). Agotados los intentos, la
notificación va a `dead_letter.jsonl` con `outcome: dead_letter`. Sin backoff
exponencial ni reproceso automático — eso queda en E-06.

---

## 8. Salidas por corrida, y la métrica

```
runs/<experiment_id>/distribution/
├── notifications.jsonl        # un DeliveryRecord por evento (append-only); generaciones previas como notifications.<n>.jsonl
├── dead_letter.jsonl          # solo las agotadas; generaciones previas como dead_letter.<n>.jsonl
└── distribution_summary.json  # agregado de la corrida
```

> Ejemplo ILUSTRATIVO con valores ficticios: no constituye una medición. La cifra real
> vive en `results/realtime/t_alert_notification/metrics.json` y en el doc 118
> (p95 = 64,534 ms).

```json
{
  "schema_version": "control.distribution_summary.v1",
  "channel": "mqtt",
  "mode": "live",
  "counts": {"delivered": 3, "suppressed_cooldown": 2},
  "skipped_invalid_alerts": 0,
  "source_stats": {"...": "..."},
  "talert_notification_ms": {
    "live": {"count": 3, "min": 31.2, "mean": 41.0, "p95": 58.7}
  }
}
```

### `t_alert-notification`: la métrica del tramo, y su caveat

Latencia desde la confirmación de la alerta hasta la entrega efectiva por el canal. Se
registra por notificación y se agrega (min / mean / p95). **Se mide por separado de la
alerta interna**: una demora o un fallo de distribución no contamina la métrica
principal de alerta.

**El caveat va declarado siempre, porque la métrica no significa lo mismo en los dos
caminos** (política de spec 40 §5):

| `latency_mode` | Cómo se calcula | Qué mide de verdad |
|---|---|---|
| `live` | `puback_wall_ms − ts_publish_ms` | latencia real del tramo de distribución |
| `wall_clock_dbe` | duración del envío en replay | **reloj de pared de un reproceso**, no el tiempo del episodio |

Reportar un `wall_clock_dbe` como si fuera latencia operativa sería un error de la misma
familia que el ya declarado para G2A (que se mide desde el *dequeue*, no desde el
fotón): el número existe, pero no dice lo que parece decir.

---

## 9. Configuración y operación

```yaml
# configs/example.yaml — sin credenciales: van por entorno
notification_policy:
  cooldown_ms: 30000
  key: [condition_id, source_id]
channel:
  mode: dry_run          # live requiere el extra [mqtt] y un broker Mosquitto
  host: 127.0.0.1
  port: 1883
  topic_prefix: eovrt/alerts
  qos: 1
retry:
  max_attempts: 3
  wait_ms: 500
```

```bash
# DBE — sobre una corrida ya persistida del control-plane
eovrt-distribute replay --alerts <control-run>/alerts.jsonl --out-dir runs/d1

# EBE — consumiendo el bus, con backfill de lo publicado antes de suscribirse
eovrt-distribute live --endpoint tcp://127.0.0.1:5558 \
                      --backfill <control-run>/alerts.jsonl --out-dir runs/d2
```

En EBE rige el **mismo orden no negociable** que el resto de la plataforma: el
consumidor se suscribe **antes** de que se dispare la corrida; el backfill cubre lo que
aun así se haya perdido.

---

## 10. Integración con el resto de la plataforma

| Con | Interfaz |
|---|---|
| **control-plane** (spec 41) | consume su publisher `control.alert.v1.*` y su `alerts.jsonl`. **No toca el motor**: el control-plane no conoce canales ni ledger |
| **experimental-setup** (spec 44) | el broker Mosquitto va en el compose; el generador de reporte incorpora `distribution_summary.json` al `report.json` de la corrida |
| **webconsole** | muestra los `outcome` de entrega en la vista de alertas — **no hay dashboard propio** (recorte de ADR-005) |
| **`experiment_id`** (ADR-004) | viaja desde el `AlertEvent` hasta el `DeliveryRecord` y el summary, de modo que la distribución queda atada a la corrida paraguas |

Para la **demostración de defensa**: `mosquitto_sub` suscrito en vivo mostrando las
notificaciones llegar, más la vista de la webconsole. Sin canal externo, justamente para
no exhibir la latencia de una API de terceros como si fuera del sistema.

---

## 11. Criterios de terminado

Lo que hay que poder mostrar para dar el módulo por cerrado (spec 45 §7):

- [x] `replay` sobre una corrida real y re-ejecución idempotente — ver `operacion/114`
      y regresiones `test_cli.py`/`test_ledger.py`.
- [x] Modo `live` con backfill de alertas previas — ver `operacion/114` y
      `test_zmq_source.py`.
- [x] Entrega MQTT real y p95 en summary — campaña doc 118: **64,534 ms (n = 460)**,
      testigo MQTT 100 %.
- [x] Duplicado QoS 1 deduplicado — `notification_id = sha1(alert_id)[:16]` y
      regresiones de `test_ledger.py`.
- [x] Ráfaga condición-fuente suprimida — clave `(condition_id, source_id)` y **376
      `suppressed_cooldown`** en la campaña del doc 118.
- [x] `experiment_id` presente en envelope, records y `report.json` — ver
      `operacion/114` y tests de consolidación/reporte del backend.

---

## 12. Qué queda fuera, y con qué causa

Excluido en **E-06** (`nucleo/10`), diseñado en `nucleo/06` como anexo: canales
adicionales (Telegram, webhook), dashboard dedicado, backoff exponencial y reproceso de
la dead-letter. La incorporación futura de cualquiera de ellos **no altera la semántica
de la alerta** (DA-13) — entra como un canal más detrás de la misma interfaz, que es
precisamente lo que la frontera del §1 protege.

---

## Fuente: `docs/informe/ajustes/material-etapa-3/93-redlines-etapa3.md`

> SHA-256 del bloque: `cb61dd3a2433e746813cc1b39ec88fcea338f1ca0ab979f779ad0b156cd47137`  
> Seleccion: documento completo.

# Redlines de Etapa 3 — hoja de trabajo para revisión

- **Fecha:** 2026-07-12

> ✎ **2026-08-28 — estado de esta hoja (`operacion/130` §5 / `datos/130-relevamiento-pre-etapa-2/docs-set.md` #10 y #32).**
> **(1) Método:** "resolverlo directo en el Google Docs" quedó **superado por el régimen 08-23/27**:
> cada sección se trabaja en su `.docx` de `informe/entregable/desarrollando/`, no en Drive; el
> circuito vigente es el de `00-contexto-base` §Cómo se trabaja. Este 93 es la **hoja de
> decisiones**, no el circuito de edición. **(2) Estado de las 26 redlines:** la decisión por
> redline **se resolvió dentro de los pases E3-01…E3-42** ya aplicados y verificados en §17.3
> **v1.4** (`correcciones-etapa-3-4*.md`, `00-el-informe-hoy` 08-28); las 53 casillas
> `[ ]` de abajo **no se marcaron una a una** — **este ✎ vale como constancia** de que el
> tablero está superado por los pases y queda como registro histórico. El mapeo
> redline→E3-xx queda como **deuda de trazabilidad** (no bloquea nada).
> **(3) Correcciones de contenido del 08-28:** R-24 (b) — el fine-tuning excluyó `chv` (ver ✎ en el ítem).

- **Qué es esto:** la lista **completa y accionable** de ajustes al capítulo 17.3, uno por uno, en orden
  del documento. **No se toca el `.docx` desde acá.** Cada ítem está redactado para que vos lo analices,
  lo critiques y lo resuelvas directo en el Google Docs.
- **Insumos:** `91-relevamiento-etapa3-vs-implementacion.md` (el análisis) y
  `92-anexo-concrecion-tecnica.md` (el material verificado contra código).
- **Texto nuevo largo:** los ítems marcados con **→ doc 94** tienen la prosa completa ya redactada en
  `94-secciones-nuevas-etapa3.md`. Acá va la instrucción; allá va el texto para copiar.

## Cómo leer cada ítem

```
R-nn · §sección · [TIPO] · PRIORIDAD
DICE HOY  →  cita literal del capítulo, o síntesis marcada como tal (o "no dice nada")
DEBE DECIR →  la instrucción concreta, o el texto propuesto
POR QUÉ   →  la evidencia que lo respalda (código, ADR, corrida medida) — cuando aporta algo
DECISIÓN  →  [ ] acepto   [ ] modifico   [ ] rechazo        ← tu casilla
```

**Tipos:** `CONTRADICE` (el capítulo dice lo contrario de lo que el sistema hace — no es opinable) ·
`CONCRETA` (falta el "cómo está hecho" que pide el tutor) · `PRECISA` (el capítulo no se equivoca, se
queda corto) · `EVIDENCIA` (falta el número medido) · `ERRATA` (forma).

**Los bloques (1–4) son temáticos, no de prioridad.** La prioridad de cada ítem está en su encabezado y en
el tablero; hay ítems críticos en bloques "medios" y viceversa.

**Numeración de tablas y figuras nuevas.** El capítulo cierra en la Tabla 60. Las tablas nuevas están
numeradas **61 a 67** en el doc 94; al transcribir, verificá que no colisionen con las que agregues vos.

> ⚠️ **v2 — 2026-07-12, tras auditoría adversarial.** Se corrigieron tres citas que no eran literales
> (R-01, R-04, R-15), el matiz del `cooldown` (R-02), y se agregaron **R-25** y **R-26**. Todas las cifras
> remiten ahora a la tabla canónica del doc 92 §10. Detalle en `95-auditoria-y-plan-de-cierre.md`.
>
> ✎ **2026-08-06 — sobre esa remisión:** "doc 92 §10" es **`informe/92`** (serie del
> informe, no `operacion/92`) y quedó **derogado como fuente de números el
> 2026-08-05**: al transcribir un redline, las cifras se toman de los **4 índices de
> `e-ovrt_experimental-setup/results/`** (verificados con
> `operacion/datos/96-verificar-indices.py`) vía el brief `informe/97` §5.

---

## Tablero de control

| # | § | Tipo | Prioridad | Título | Decisión |
|---|---|---|---|---|---|
| R-01 | 17.3.9.2 | CONTRADICE | 🔴 crítica | La estrategia del núcleo es E-IND, no la directa | [ ] |
| R-02 | Tabla 44 | CONTRADICE | 🔴 crítica | El `cooldown` no es parámetro de patrón | [ ] |
| R-03 | Tabla 44 / 17.3.6.2 | CONTRADICE | 🔴 crítica | `RunConfig` es un manifiesto + configs por plano | [ ] |
| R-04 | 17.3.8.3.2 | PRECISA | 🔴 crítica | Granularidad `scene\|subject` + caveat semántico de escena | [ ] |
| R-05 | Tabla 45 / 17.3.6.4 | CONTRADICE | 🔴 crítica | El vocabulario del núcleo es positivo (person/helmet/vest) | [ ] |
| R-06 | 17.3.11 | CONCRETA | 🔴 crítica | Partir el hedge en dos + tabla de correspondencia | → doc 94 §1 · [ ] |
| R-07 | 17.3.11.4 | CONCRETA | 🔴 crítica | Regla de evolución del evento (el pedido del tutor) | → doc 94 §2 · [ ] |
| R-08 | 17.3.8.1 / .4 | CONCRETA | 🟠 alta | El bus existe y tiene tecnología: ZeroMQ + msgpack | → doc 94 §3 · [ ] |
| R-09 | 17.3.5 | CONCRETA | 🟠 alta | Figura nueva: vista de procesos (dos servicios HTTP) | → doc 94 §4 · [ ] |
| R-10 | 17.3.13 | CONCRETA | 🟠 alta | Diccionario de métricas con t0/t1 + criterio de relojes | → doc 94 §5 · [ ] |
| R-11 | 17.3.14 (nueva .6) | PRECISA | 🟠 alta | Temporalidad de la fuente y el "cero silencioso" | → doc 94 §6 · [ ] |
| R-12 | cierre (nueva) | EVIDENCIA | 🟠 alta | Sección de verificación: qué funciona y cómo se midió | → doc 94 §7 · [ ] |
| R-13 | cierre (nueva) | EVIDENCIA | 🟠 alta | Registro de lo no implementado | → doc 94 §8 · [ ] |
| R-14 | 17.3.8.2 / Tabla 46 | PRECISA | 🟠 alta | Ventanas efectivas: 4000 / 7000 ms; severidades `high`/`medium` | [ ] |
| R-15 | 17.3.12.1 | CONCRETA | 🟡 media | El repositorio es JSONL append-only, con layout | [ ] |
| R-16 | 17.3.13.3 | PRECISA | 🟡 media | La aplicabilidad es un campo literal (`status` + `cause`) | [ ] |
| R-17 | 17.3.15 | CONCRETA | 🟡 media | Tabla rol → contenedor (Nodo A ≈ EN-1, Nodo B ≈ CPN) | [ ] |
| R-18 | Tabla 43 (DA-01…13) | PRECISA | 🟡 media | Actualizar el estado de las decisiones condicionadas | [ ] |
| R-19 | Tabla 50 | ERRATA | 🟡 media | `PatternDefinition` es huérfano: falta su fila | [ ] |
| R-20 | Tabla 57 | PRECISA | 🟡 media | Riesgos: los que se materializaron y cómo se mitigaron | [ ] |
| R-21 | Tablas 58/59 | EVIDENCIA | 🟠 alta | Backlog: estado real de los 16 ítems | [ ] |
| R-22 | 17.3.14.5 | PRECISA | 🟡 media | EBE: la cámara IP real ya se usó; la brecha que queda | [ ] |
| R-23 | varias | ERRATA | 🟢 baja | Figuras sin numerar y vacías, títulos pegados, duplicados | [ ] |
| R-24 | fuera de 17.3 | PRECISA | 🟡 media | Inventario de datasets desactualizado | [ ] |
| R-25 | 17.3.11 / 17.3.13 | CONCRETA | 🟠 alta | Contrato de GT temporal + convención de identidad + los 5 hitos | [ ] |
| R-26 | 17.3.17 / 17.3.18 | CONCRETA | 🟠 alta | **Extensibilidad medida: cuánto cuesta una condición nueva** | → doc 94 §9 · [ ] |

---

# 🔴 Bloque 1 — Contradicciones (no son opinables)

## R-01 · §17.3.9.2 · CONTRADICE · crítica
### La estrategia adoptada para el núcleo es E-IND, no la detección directa

**DICE HOY** — cita **literal** (líneas 623 y 627), corregida tras auditoría:
> *"Para el núcleo validable, la estrategia adoptada es la detección directa de condiciones de EPP mediante
> prompts configurados para CR-01 y CR-02."*
>
> *"[Las consultas auxiliares positivas] pueden habilitarse con finalidad diagnóstica o comparativa. Su uso
> permite analizar falsos positivos… pero no reemplaza la estrategia directa ni confirma por sí mismo una
> ausencia."*

**DEBE DECIR** — invertir la adopción. Texto propuesto para reemplazar el párrafo central:

> La estrategia adoptada para el núcleo validable es la **detección indirecta por evidencia positiva con
> inferencia espacial de ausencia (E-IND)**. El plano de medios consulta al detector open-vocabulary por
> **entidades presentes y observables** —persona, casco, chaleco— y el plano de control infiere la
> ausencia del elemento de protección evaluando su presencia dentro de una región derivada del bounding
> box del sujeto. La ausencia, por lo tanto, no se consulta al modelo: se **deriva** de evidencia
> perceptiva positiva.
>
> Esta adopción responde a tres razones. Primero, una razón metodológica: la consolidación metodológica
> de este trabajo (§17.1.5.4.2) exige comparar estrategias directas e indirectas **sin presuponer la
> superioridad de ninguna**, de modo que adoptar la estrategia directa como núcleo por definición sería
> incompatible con el propio protocolo. Segundo, una razón empírica: la evaluación comparativa de modelos
> sobre el conjunto BENCH muestra que el estado observable que sostiene la estrategia directa
> (`bare_head`) es débil en todos los modelos evaluados, al punto de que una de las familias evaluadas
> detecta entre 0 y 1 instancias sobre 69 presentes en la referencia. Tercero, una razón de auditabilidad:
> la evidencia producida por E-IND es **inspeccionable** —el bounding box del sujeto, la región evaluada y
> la ausencia verificable dentro de ella—, mientras que un prompt de negación produce una decisión opaca,
> no reconstruible.
>
> La **detección directa (E-DIR)** y las **estrategias híbridas (E-HYB)** se conservan como **ramas
> comparativas** del protocolo experimental, no como diagnóstico subordinado. La comparación cuantitativa
> entre estrategias queda **especificada** como protocolo, y su ejecución se declara conforme al alcance
> final del trabajo.

> 🔴 **DECISIÓN TUYA, Y ES URGENTE.** El último párrafo tiene dos versiones posibles y **no podés
> postergarla**:
>
> - **(a) Comprometida:** *"la comparación entre estrategias es, en sí misma, uno de los resultados
>   previstos del trabajo"*. Suena mucho mejor — **pero promete un resultado que hoy no existe**: los
>   evaluadores E-DIR/E-HYB no están implementados y están **bloqueados esperando que firmes el acta del
>   catálogo de prompts (`edir_v1`)**. Si escribís esto y D1 no corre, el tribunal va a pedir esa tabla.
> - **(b) Prudente** (la que dejé arriba): la comparación queda **especificada**, y su ejecución depende
>   del alcance final.
>
> **Regla:** si firmás el acta esta semana y D1 entra en la campaña, poné (a). Si no, poné (b) y dormí
> tranquilo. Lo que **no** se puede es escribir (a) y no correrlo.

**POR QUÉ** — ADR-001; §17.1.5.4.2 del propio informe (que exige comparar directas contra indirectas "sin
presuponer la superioridad de ninguna"); doc 31 (benchmark de **6** modelos: YOLOE recall CR-01
0.000–0.014, con 0–1 detecciones de `bare_head` sobre 69 de referencia); el evaluador implementado es
`spatial_absence` y es el único que existe.

**OJO — efecto dominó.** Este redline arrastra a **R-05** (el vocabulario de la Tabla 45) y toca el
encuadre del capítulo de resultados. Es el ajuste más importante de todo el documento.

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

## R-02 · Tabla 44 · CONTRADICE · crítica
### El `cooldown` no es un parámetro de la evaluación de patrones

**DICE HOY** (Tabla 44, fila "Patrones activos", línea 287):
> *"…ventana de persistencia, histéresis, **cooldown** y criterio de confirmación."*
(Es la única mención en todo el capítulo: nunca se explica.)

**DEBE DECIR** — dos cambios:

1. **Sacar `cooldown` de la Tabla 44.** La fila queda: *"ventana de persistencia, histéresis y criterio de
   confirmación."*
2. **Agregar en §17.3.10.3** (distribución) el párrafo:

> El motor de patrones **registra una alerta interna en cada confirmación de episodio, sin supresión**: el
> registro de alertas es el reflejo fiel de la dinámica del patrón y no debe ser filtrado por
> consideraciones de comunicación. Las políticas de **supresión de re-notificación** —cooldown por
> condición y fuente, agrupación, limitación de tasa— pertenecen al **tramo de distribución**, aguas abajo
> de la alerta interna, y se declaran como parámetros de la política de notificación. Esta separación
> preserva la métrica principal: una alerta suprimida por política de notificación **existió**, fue
> registrada y es medible, aunque no se haya comunicado.
>
> En consecuencia, las alertas sucesivas correspondientes a un mismo episodio confirmado se contabilizan
> como **re-alertas**, un indicador de estabilidad temporal del patrón, y **no se computan como falsos
> positivos** en la evaluación.

**POR QUÉ** — ADR-011. El conjunto de patrones adoptado **no configura cooldown**; el evaluador excluye
explícitamente las re-alertas del denominador de la precisión.

> ⚠️ **Matiz que encontró la auditoría, y que hay que respetar al redactar.** El cooldown **sí existe en el
> motor** (`PatternTimingConfig.realert_cooldown_ms` + `PatternEngine._cooldown_ok()`): lo que ocurre es
> que **el conjunto de patrones adoptado lo deja sin configurar**, y ADR-011 lo declara literalmente
> "capacidad no usada por la plataforma". Redactá *"el motor no suprime, porque el conjunto de patrones
> adoptado no configura supresión"* — **nunca** *"el motor no puede suprimir"*. Si alguien abre el código y
> encuentra un cooldown que el informe negaba, el daño supera al beneficio de la frase simple.

**Impacto en resultados:** sin este párrafo, la tabla de precisión del capítulo de resultados es
ininterpretable (el lector no sabe qué entra en el denominador).

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

## R-03 · Tabla 44 y §17.3.6.2 · CONTRADICE · crítica
### `RunConfig` no es un artefacto único: es un manifiesto que referencia configuraciones por plano

**DICE HOY** — la Tabla 44 y toda la §17.3.6 tratan la configuración de corrida como **un** artefacto que
gobierna la corrida completa, del que cuelgan fuente, modelo, prompts, umbrales, patrones y evidencia.

**DEBE DECIR** — reencuadrar §17.3.6.2 con este párrafo antes de la Tabla 44:

> La configuración de corrida se materializa como un **manifiesto de experimento**, que no contiene la
> configuración completa sino que **referencia** la configuración efectiva de cada plano y las **congela**
> bajo un identificador común. La razón es estructural: los planos se ejecutan como servicios
> independientes, cada uno con su propio ciclo de vida y su propia configuración efectiva, de modo que una
> configuración monolítica no tendría un único destinatario.
>
> El manifiesto declara: un **identificador de experimento** (`experiment_id`) que se propaga a todos los
> eventos y resúmenes de **ambos** planos; las referencias a la configuración de cada plano; el orden de
> disparo; y el conjunto de artefactos congelados de la corrida (conjunto de prompts, conjunto de patrones,
> referencia del modelo). Ese identificador es la **clave de trazabilidad** que permite reconstruir una
> alerta hasta la configuración, el conjunto de prompts, el modelo y la versión de código que la
> produjeron —la promesa formulada en §17.3.11.1—, y sin él la cadena causal se cortaría en la frontera
> entre planos.

Y **agregar una fila a la Tabla 44**: *"Identificador de experimento — clave común que vincula las corridas
de ambos planos y todos sus artefactos."*

**POR QUÉ** — ADR-004, ADR-009, ADR-014. Artefacto real: `manifest.effective.yaml` (`experiment.manifest.v1`),
con `experiment_id` presente en `pattern_events.jsonl`, `alerts.jsonl` y los `summary.json` de ambos planos.

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

## R-04 · §17.3.8.3.2 · PRECISA (pero es crítica) · crítica
### La granularidad es un parámetro del patrón — y la de escena tiene un caveat que hay que declarar

**DICE HOY** — cita **literal** (línea 547), corregida tras auditoría:
> *"Para los patrones del núcleo validable, esta memoria puede organizarse **por fuente y condición**, sin
> exigir identidad persistente de persona."*

Es correcto, pero se queda a mitad de camino: hoy eso es un **parámetro explícito** del patrón, y su
elección tiene una **consecuencia semántica** sobre la afirmación central del trabajo.

**DEBE DECIR** — reemplazar el párrafo por:

> La granularidad de la memoria temporal es un **parámetro explícito de la definición de patrón**, con dos
> valores posibles. Bajo granularidad de **escena** (el núcleo validable), el estado se indexa por
> `(patrón, fuente)` y la persistencia se evalúa sobre la condición observada en la escena, sin exigir
> identidad persistente de persona. Bajo granularidad de **sujeto**, el estado se indexa por
> `(patrón, fuente, identidad)` y requiere que el plano de medios emita una identidad estable entre frames.
>
> El núcleo adopta la granularidad de escena por una razón medida, no por conveniencia: el identificador de
> detección que produce el detector es un **índice por frame**, no una identidad temporal, y utilizarlo como
> tal produce aliasing verificable —sobre una corrida de vídeo real, la detección identificada como
> `det_000001` recorre 1831 píxeles del ancho del cuadro, de 1920 píxeles, a lo largo de la corrida, con
> desplazamientos de hasta 1749 píxeles entre cuadros consecutivos—. Se declara, en consecuencia, que **el
> identificador de detección no constituye identidad entre frames** y que la única identidad válida es la
> emitida por un componente de seguimiento.
>
> Esta elección tiene una **consecuencia semántica que debe explicitarse**. Bajo granularidad de escena, la
> persistencia no mide que *el mismo sujeto* sostenga la condición de riesgo, sino que *la escena exhiba la
> condición de forma continua*. Una escena con rotación de personas —cada una brevemente descubierta— puede
> confirmar un episodio sin que ningún individuo haya estado persistentemente en riesgo. La afirmación que
> el sistema sostiene bajo el núcleo validable es, por lo tanto, **"la condición de riesgo persiste en la
> escena"**, y no "un sujeto persiste en riesgo". La segunda afirmación requiere granularidad de sujeto, que
> el diseño prevé y el prototipo deja especificada como extensión.

**POR QUÉ** — ADR-002, ADR-012; doc 34 §3 (el caveat, demostrado en fixture: un sujeto transitorio adelanta
el reloj del episodio); doc 35 §1.1 (el aliasing, medido — ojo con la formulación: los 1831 px son el
**rango total** de la corrida, no un salto entre dos cuadros; el salto máximo consecutivo es ~1749 px).

**Este es el ítem que más protege la defensa.** Escrito por nosotros es rigor metodológico; encontrado por
el tribunal es un agujero en la afirmación central.

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

## R-05 · Tabla 45 y §17.3.6.4 · CONTRADICE · crítica
### El vocabulario activo del núcleo es positivo

**DICE HOY** — la Tabla 45 presenta como formulaciones principales de CR-01/CR-02 los prompts de ausencia
(`"person without hard hat"`, `"person without reflective vest"`) y relega a auxiliares los positivos
(`"person"`, `"hard hat"`, `"safety helmet"`, `"reflective vest"`).

**DEBE DECIR** — invertir la jerarquía de la tabla, **coherentemente con R-01**:

- **Vocabulario activo del núcleo (E-IND):** `person`, `helmet`, `vest`. Es el conjunto efectivamente
  ejecutado (`cr01_cr02_v2_short`), con las clases tipificadas por rol: `person` como **entidad sujeto**,
  `helmet` y `vest` como **elementos de protección**.
- **Vocabulario de la rama comparativa (E-DIR):** las formulaciones de ausencia y de estado observable, que
  pasan a ser el objeto del experimento de sensibilidad al prompt, no el núcleo.
- Conservar el resto de la tabla (CR-03…CR-06) tal como está: son condiciones no implementadas y su
  vocabulario sigue siendo candidato.

**Nota importante que conviene agregar bajo la tabla:** el conjunto de formulaciones se **versiona** y la
corrida registra el identificador del conjunto activo (`prompt_set_id`), de modo que toda detección es
atribuible a la formulación exacta que la produjo.

**POR QUÉ** — ADR-001; el prompt set real es `cr01_cr02_v2_short.yaml` (`person` / `helmet` / `vest`);
`prompt_set_id` viaja en cada `DetectionEvent`.

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

# 🟠 Bloque 2 — Concreción técnica (la observación del tutor)

## R-06 · §17.3.11 · CONCRETA · crítica → **texto completo en doc 94 §1**
### Partir el hedge en dos: lo implementado se muestra; lo pendiente sigue preliminar

**DICE HOY** (línea 699) — el párrafo que el tutor citó textualmente:
> *"…los nombres utilizados en esta sección, como RunConfig, FrameMetadata, PerceptionEvent o AlertEvent,
> deben interpretarse como denominaciones contractuales preliminares. **No imponen una tecnología, un
> formato de serialización ni una estructura de código específica.**"*

**DEBE DECIR** — este párrafo **era verdadero el 6 de julio y hoy es falso para el núcleo**. No hay que
borrarlo: hay que **partirlo**.

- Para el **núcleo validable**: los contratos ya no son preliminares. Son modelos de datos versionados, con
  serialización explícita, esquema verificable y corridas que los ejercitan. Se muestran con su artefacto
  real (clase, DTO serializado, endpoint).
- Para lo **no implementado** (los contratos del tramo de distribución): el estatus preliminar **se
  conserva y se declara como tal**.

Concretamente, la sección debe incorporar: **(a)** la tabla de correspondencia contrato preliminar ↔
artefacto real; **(b)** el contrato central (`PerceptionEvent` → `DetectionEvent` / `media.detection.v1`)
mostrado como **clase** y como **DTO serializado**; **(c)** los dos contratos del plano de control
(`PatternStateChanged`, `AlertEvent`); **(d)** las **APIs** de los dos servicios.

**→ El texto completo, con la tabla, los DTO y los endpoints, está en `94-secciones-nuevas-etapa3.md` §1.**

**POR QUÉ** — es el pedido literal del tutor ("no espero un detalle extremo, pero sí algo como un DTO, una
API, o una clase"). Todo el material existe y está verificado con ruta:línea en el doc 92.

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

## R-07 · §17.3.11.4 · CONCRETA · crítica → **texto completo en doc 94 §2**
### La regla de evolución del evento de inferencia (el pedido más profundo del tutor)

**DICE HOY** (líneas 785–797) — la sección existe y es correcta en espíritu ("cambios aditivos aceptables;
cambiar o eliminar significado = ruptura contractual → nueva versión"), pero es **abstracta**: no muestra el
evento, no nombra un solo campo, no dice qué se emite hoy y qué no.

**DEBE DECIR** — el tutor pidió esto con nombre y apellido:
> *"Es muy importante ser muy claro en la definición de eventos tipo inferencias para que den soporte a
> datos que a lo mejor hoy no están, pero mañana sí: tracking, velocidad, dirección, pose, segmentación."*

La sección debe: **(a)** enunciar las cuatro reglas de evolución (aditivo, sin bump de versión, la versión
viaja en el payload, ruptura sólo por cambio de significado); **(b)** **mostrar el evento con su superficie
de crecimiento** —los campos futuros como opcionales, explícitos en el esquema—; **(c)** declarar
**honestamente** el estado de cada extensión.

**El hallazgo que hay que contar (y que juega a favor):** `track_id` existe **en ambos contratos** —el
consumidor lo usa como identidad en el motor de patrones desde antes; el productor lo incorporó el
2026-07-13 (commit `0133d38` del media-plane, como campo aditivo con tests de serialización)— pero **nadie
lo puebla todavía**: el tracker no está implementado, el campo vale `None` y no aparece en los artefactos.
La distinción para el informe es exactamente esa: **el contrato está completo; la capacidad que lo
alimenta, no**. Decirlo así demuestra lo que el tutor quiere ver: que el contrato fue **diseñado para
crecer** (y se puede mostrar el esquema, no prometerlo), y que sabemos dónde está parado hoy.

**→ Texto completo en `94-secciones-nuevas-etapa3.md` §2.**

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

## R-08 · §17.3.8.1 y §17.3.8.4 · CONCRETA · alta → **texto completo en doc 94 §3**
### El bus tiene tecnología, y sus trampas están medidas

**DICE HOY** (línea 477):
> *"El diseño **no exige una tecnología específica de mensajería** en esta instancia."*

**DEBE DECIR** — ya la exige. Está elegida (ZeroMQ PUB/SUB + msgpack), implementada, medida, y tiene
**reglas de operación que se descubrieron corriéndola** y que un capítulo de arquitectura debería contener:

- El envelope versionado y su relación con el JSONL (el payload publicado es **byte-idéntico** a la línea
  persistida ⇒ toda corrida en vivo es re-evaluable offline).
- **El orden de arranque es control-primero**, y no es negociable: PUB/SUB **pierde todo lo publicado antes
  de la suscripción**.
- **Persistir primero, publicar después**: el repositorio es la verdad, el bus sólo transporta (DA-03).
- **La pérdida se detecta por hueco de número de secuencia** — un publicador ZeroMQ descarta en silencio al
  llenarse su cola, sin señalar error. Un hueco degrada la corrida; nunca se silencia.
- El broker (Kafka/RabbitMQ) queda **fuera de alcance con la costura documentada**.

**→ Texto completo en `94-secciones-nuevas-etapa3.md` §3.**

**POR QUÉ** — ADR-003, spec 40 §3, doc 37 (40/40 unidades, 0 perdidas, artefactos byte-idénticos).

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

## R-09 · §17.3.5 · CONCRETA · alta → **especificación de figura en doc 94 §4**
### Falta la vista de procesos: el sistema son dos servicios HTTP

> ✎ **2026-08-19 — aplicada con destino ENMENDADO.** La vista de procesos (FIG-A) va en
> **§17.4.1, destino único**: la doctrina del pase de cierre
> (`entregable/desarrollando/correcciones-etapa-3-4.md`, decisión firmada por el usuario)
> dejó a §17.3 sin puertos ni vista de procesos. En §17.3.5 la necesidad que este redline
> señalaba la cubren la Figura 4.1 conceptual más la justificación de tecnologías nueva
> (ítem E3-04). El cuerpo de abajo se conserva como historia; su "segunda figura en
> §17.3.5" ya no va.

**DICE HOY** — la Figura 4.1 es una **vista lógica** de bloques (fuentes → adaptador → plano de medios → bus
→ plano de control → distribución), con la nota de que "no debe interpretarse como una distribución física".

**DEBE DECIR** — la vista lógica **se conserva** (es correcta y es la que ordena el capítulo). Lo que falta
es una **segunda figura**: la vista de **procesos/despliegue real**, que es literalmente el "cómo está
hecho" que reclama el tutor. *(✎ 2026-08-18, ADR-019: al dibujar FIG-A, el módulo de
distribución va con **línea continua** y, si se muestran puertos, con su `:8082` — ya no
es "capacidad especificada": es el tercer servicio HTTP, y el orquestador lo dispara por
HTTP igual que a los otros dos (ADR-020; el subproceso quedó como fallback operativo y no
va a la figura). Ver la nota al pie REEMPLAZADA en el doc 94 §4.)*
Debe mostrar: los dos servicios HTTP (`:8080` y `:8081`), el bus ZeroMQ entre
ellos, el orquestador que dispara la corrida paraguas por HTTP, la webconsole como cliente de ambas APIs
(**no consume el bus**), el repositorio JSONL por corrida, y el módulo de distribución como consumidor
externo del bus de alertas.

**→ Especificación de la figura (cajas, flechas, etiquetas) en `94-secciones-nuevas-etapa3.md` §4.**

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

## R-10 · §17.3.13 · CONCRETA · alta → **texto completo en doc 94 §5**
### Diccionario de métricas con definiciones operacionales, y el criterio de relojes

**DICE HOY** — §17.3.13.1 nombra TTFD, SDR y la latencia de alerta, y los vincula a tramos ("TTFD se vincula
con la primera evidencia perceptiva"). No define t0, t1, unidad ni condición de aplicación de ninguna.
Y **no menciona el problema de los relojes**.

**DEBE DECIR** — una tabla de diccionario con `t0 / t1 / unidad / condición de aplicabilidad` por métrica, y
tres cosas que hoy faltan:

1. **El criterio de relojes** (el hueco más caro): las latencias intra-nodo usan reloj monotónico local; las
   end-to-end se miden **en un solo reloj**. **Los relojes monotónicos de dos hosts no se restan** — en la
   topología de dos nodos, la métrica correspondiente se declara *no interpretable* con su causa, en lugar
   de publicar un número sin significado.
2. **Las dos métricas derivadas propias** (`t_capture→alert` y `t_compute-budget`), con su **estatus
   epistemológico declarado**: son un aporte instrumental de este trabajo, **no** reemplazan la métrica
   oficial — la **descomponen**. Identidad declarada: `t_alert-system = TTFD + t_capture→alert`.
3. **El criterio de detección positiva no se reimplementa**: el evaluador reutiliza el evaluador real del
   motor, de modo que no puede haber dos definiciones de "positivo" divergiendo en silencio.

**→ Texto completo, con la tabla del diccionario, en `94-secciones-nuevas-etapa3.md` §5.**

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

## R-11 · §17.3.14 (subsección nueva) · PRECISA · alta → **texto completo en doc 94 §6**
### Temporalidad de la fuente: el "cero silencioso"

**DICE HOY** — nada. El capítulo distingue DBE de EBE por el **origen** de la fuente (dataset vs entorno),
pero no por su **naturaleza temporal**.

**DEBE DECIR** — es una dimensión de aplicabilidad que el capítulo no contempla y que produce un **modo de
falla silencioso**:

> Un conjunto de patrones con persistencia temporal, evaluado sobre una fuente **no temporal** (un dataset
> de imágenes independientes), produce **cero alertas por construcción** — un resultado indistinguible de
> "no hubo riesgo en los datos". Se midió: **77 transiciones de patrón y 0 alertas**.

La plataforma hoy **detecta la temporalidad de la fuente y lo declara sola** (`no aplicable / fuente no
temporal`), en lugar de reportar un cero engañoso. Es la política de aplicabilidad del §17.3.13.3 haciendo
exactamente el trabajo para el que fue diseñada, y conviene mostrarlo como tal.

**→ Texto completo en `94-secciones-nuevas-etapa3.md` §6.**

**POR QUÉ** — ADR-013. ⚠️ **Ojo con la cifra:** el run original de los "137 eventos / 0 alertas" (doc 33 §4)
**fue podado y ya no existe**. El equivalente vivo, con el motor actual, da **77 transiciones / 0 alertas** —
y ese artefacto **sí** está en disco, con `not_applicable / non_temporal_source` declarado. Usá 77.

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

# 🟠 Bloque 3 — Evidencia ("qué funciona y cómo se mide")

## R-12 · Sección nueva al cierre · EVIDENCIA · alta → **texto completo en doc 94 §7**
### Verificación: el sistema es ejecutable, y estos son los números

**DICE HOY** — nada. El capítulo **no contiene una sola cifra medida**.

**DEBE DECIR** — una sección de verificación con la evidencia ya producida: 733 unidades sin fallos sobre
vídeo real; el bus y el repositorio transportando lo mismo (artefactos byte-idénticos); CR-01 confirmando en
t=4000 ms exacto; F1=1.0 en el gate de granularidad; y **las cinco métricas contra referencia temporal
anotada sobre un clip de obra real** (P=0,50 · R=1,00 · F1=0,67 · t_alert-system=4000 ms · TTFD=0 ms ·
SDR=0,999).

> 🔴 **TRES CORRECCIONES DE LA AUDITORÍA — sin esto, la tabla es indefendible.**
>
> 1. **G2A: el número que veníamos citando era de una corrida MOCK.** "p95 = 31,8 ms, dentro de presupuesto"
>    sale de una corrida con detector simulado. **Con GDINO real, el p95 es 2604 ms** y el propio sistema
>    marca `p95_within_budget: false` — diez veces por encima del presupuesto. **No lo escondas: es un
>    hallazgo.** La instrumentación funciona *porque* detecta el incumplimiento, y coincide con el conflicto
>    CR-01 ↔ tiempo real del doc 31. Reformulado así en el doc 94 §7.
> 2. **Las cinco métricas son una VERIFICACIÓN DE INSTRUMENTO, no un resultado.** Salen de **un clip**, con
>    **dos alertas observadas** y **GT preliminar**. Una "precisión de 0,50" derivada de dos eventos invita
>    a la pregunta *"¿su precisión es una moneda al aire?"*. Hay que decir **n = 1 clip, 2 alertas** y
>    llamarlo verificación, no medición de desempeño.
> 3. **No fusiones corridas distintas.** La byte-identidad se verificó sobre una corrida de **40 unidades**;
>    las **300 unidades** son otra corrida. Y **ambas usaron detector mock**. Van en filas separadas.

**Y contarlo con honestidad**: el único falso positivo de ese benchmark es **un hallazgo sobre el modelo, no
un bug** (el detector pierde el chaleco de un trabajador), y el GT de ese clip es **preliminar** hasta la
pasada humana en CVAT. Decir ambas cosas **fortalece** el resultado; ocultarlas lo destruye si alguien
pregunta.

**→ Texto completo, con la tabla de evidencia ya corregida, en `94-secciones-nuevas-etapa3.md` §7.**
**→ Todas las cifras, con su corrida y su detector, en `92-anexo-concrecion-tecnica.md` §10** (tabla canónica).

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

## R-13 · Sección nueva al cierre · EVIDENCIA · alta → **texto completo en doc 94 §8**
### Registro de lo no implementado

> ✎ **2026-08-05 — DESBLOQUEADO, y la lista de abajo quedó vieja.** Este ítem esperaba
> ADR-015 (doc 95 §5.3), que ya está escrito:
> `decisiones/adr-015-cierre-de-alcance.md` (fuente: `docs/decisiones/adr-015-cierre-de-alcance.md`)
> (✅ aceptada el 2026-08-05). **De los 8 ítems de abajo, 5 están resueltos**
> — auditados uno por uno contra artefacto en el **ADR-015 §3**, que es de donde hay que
> redactar: `track_id` (G1 es capacidad operativa medida), evaluadores de D1 (corrió: veto
> de precisión), GT preliminar (el banco está `gt_ready`), matching greedy (es bipartito
> desde la enmienda A4) e inventario de datasets (al día, `operacion/99`).
> **Sobreviven 3**: distribución no implementada, brecha del ancla EBE (precisada) y G2A
> no computable entre dos hosts (ahora agravada por F-101.8). **Y el tramo experimental
> agregó 9 límites nuevos** (L1–L8 + el registro de licencias de video). Publicar la lista
> de abajo tal cual sería declarar como límites cosas ya resueltas.

**DECÍA (julio 2026, superado)** — un capítulo "verificable" también declara sus límites, **antes** de que los encuentre el
tribunal. Ocho ítems: sin productor de `track_id`; distribución no implementada; evaluadores de D1
pendientes; GT preliminar; brecha de sincronización en EBE-desde-clip; G2A no computable en dos nodos;
matching greedy que puede deflacionar recall; inventario de datasets desactualizado.

Cada uno **anclado a su regla de exclusión** (doc 10, E-01…E-13), para que se lea como alcance declarado y
no como omisión.

> ✎ **2026-08-22 — CÓMO QUEDÓ SALDADO EL ANCLAJE (hallazgo §3.3 de la revisión de cierre).** La revisión
> observó que la tabla integrada (Tabla 68 de §17.4.10 en el `.docx` v1.2) **no contiene ningún código
> E-xx**, y que eso dejaba el redline sin saldar. La resolución es **sustantiva, no por código**, y es la
> única compatible con la regla de autocontención (el informe no puede citar `doc 10` ni sus códigos):
> cada fila de la Tabla 68 lleva su fundamento de exclusión escrito en la columna de consecuencia, la
> prosa de §17.4.10 desarrolla el porqué del núcleo-solo por evaluabilidad (D4/E4-17), y el pase 3 lo
> completa — la **enmienda a E4-22** deja la exclusión de la preselección declarada con su causa
> pre-registrada, y **E4-27** hace lo mismo con la rama de ajuste fino. El mapa código ↔ fila (E-xx ↔
> Tabla 68) queda como trazabilidad **interna** en doc 10 y en ADR-015 §3; al informe no entra. Con eso
> este redline se considera **saldado**: el anclaje existe, expresado como fundamento y no como código.

**→ Texto completo en `94-secciones-nuevas-etapa3.md` §8** (✎ 2026-08-22: superado como texto guía por la
Tabla 68 del `.docx` v1.2 + pase 3 — ver el banner de ese §8).

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

## R-14 · §17.3.8.2 y Tabla 46 · PRECISA · alta
### Los valores efectivos: 4000 / 7000 ms, `high` / `medium`

**DICE HOY** — el capítulo declara la severidad "estática por corrida" pero **nunca enumera los niveles**, y
no da **ningún** valor de ventana temporal (no hay una sola cifra en todo el capítulo).

**DEBE DECIR** — agregar los valores efectivos del núcleo, y su justificación contra las bandas del informe:

| Patrón | Condición | Severidad | Persistencia (confirmación) | Histéresis (resolución) | Banda del informe (Tabla 24) |
|---|---|---|---|---|---|
| PR-01 | Persona sin casco | `high` | **4000 ms** | 2000 ms | alto · 3–5 s ✓ |
| PR-02 | Persona sin chaleco | `medium` | **7000 ms** | 3000 ms | medio · 5–10 s ✓ |

Y una frase que conviene incluir porque responde a una pregunta previsible: la persistencia se expresa **en
milisegundos, no en frames**, tal como exige §17.1.5.3.3 — de otro modo la ventana temporal dependería de la
tasa de muestreo y dejaría de ser comparable entre corridas.

**Y los umbrales efectivos** (que tampoco están en el capítulo, y el tutor los va a buscar):

| Parámetro | Valor | Dónde |
|---|---|---|
| Umbral de caja / de texto / de confianza / IoU | 0,35 / 0,25 / 0,25 / 0,50 | Inferencia |
| Confianza mínima de postproceso · área mínima | 0,25 · 100 px² | Postproceso |
| Confianza mínima del sujeto · del elemento ausente · área mínima del sujeto | 0,35 · 0,25 · 400 px² | Evidencia de patrón |
| Región de búsqueda CR-01 (casco) | franja superior del sujeto: 0–45 % de su altura, margen lateral 12 % | Evaluador espacial |
| Región de búsqueda CR-02 (chaleco) | franja media: 25–85 % de la altura, margen lateral 8 % | Evaluador espacial |

**POR QUÉ** — `cr01_cr02_v2.yaml`. Verificado: CR-01 confirma en t=4000 ms exacto sobre video real (doc 35);
con ~1 s de video no hay alertas y con ~10 s aparecen (doc 51) — la ventana **hace** lo que dice.

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

# 🟡 Bloque 4 — Precisiones y forma

## R-15 · §17.3.12.1 · CONCRETA · media
### El repositorio de eventos es JSONL append-only, y tiene un layout

**DICE HOY** — cita **literal y completa** (línea 809). La versión anterior de este redline recortaba la
frase de un modo que **cambiaba su sentido**: omitía la subordinada que la salva. El original dice:
> *"…alcanza con una persistencia simple y verificable […] La decisión arquitectónica relevante **no es la
> tecnología concreta de almacenamiento, sino la imposibilidad de sobrescribir silenciosamente los hechos
> que explican una corrida**."*

O sea: el capítulo **no está indeciso**, está priorizando bien. El redline no es "el capítulo se lava las
manos", es "el capítulo tiene razón y además ya podemos decir qué elegimos".

**DEBE DECIR** — el principio es correcto y se conserva; lo que falta es decir **qué se eligió**: un archivo
**JSONL append-only por corrida y por tipo de evento**, con la configuración efectiva, el manifiesto (que
incluye el **SHA de git del código que produjo la corrida**) y la procedencia de los datos junto a los
eventos. Conviene mostrar el layout de artefactos (está en el doc 92 §8) y cerrar con la frase que hace
verdadera la promesa de §17.3.11.1:

> Toda alerta se reconstruye hasta la configuración efectiva, el conjunto de prompts, el modelo y la versión
> de código que la produjeron.

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

## R-16 · §17.3.13.3 · PRECISA · media
### La política de aplicabilidad ya no es una política: es un campo

**DICE HOY** — describe los cuatro estados de una métrica (calculada / aplicable no calculada / no aplicable /
no interpretable) como criterio de interpretación.

**DEBE DECIR** — agregar que se **materializó como campo literal** del reporte (`status` + `cause`), con
ejemplos reales:

- `t_alert→notification` → **no aplicable** / *no hay canal de distribución*.
- `t_capture→alert` → **no interpretable** / *reloj de medio, no de pared*.
- G2A en dos nodos → **no interpretable** / *relojes monotónicos de hosts distintos*.
- TTFD sin detección positiva en el episodio → **nulo** con causa, **nunca 0.0 por defecto**.

Esta es una de las fortalezas diferenciales del trabajo y hoy está subvendida: el capítulo la enuncia como
criterio y no muestra que **el sistema se niega a publicar un número que no significa nada**. Vale una frase
explícita: *"la plataforma no publica un cero cuando lo correcto es declarar una causa"*.

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

## R-17 · §17.3.15 · CONCRETA · media
### Tabla rol → contenedor

**DICE HOY** — CPN/EN/TN son roles lógicos, "no implican necesariamente máquinas físicas separadas". (Correcto,
**no tocar el principio**.)

**DEBE DECIR** — aterrizarlo con la correspondencia real, que existe y está verificada en la topología de dos
nodos:

| Rol | Materialización en el prototipo | Responsabilidades ejercidas |
|---|---|---|
| **EN** (modo EN-1) | Nodo A (contenedor de borde, sin GPU) | Ingesta, control de ritmo, normalización visual. **Sin semántica**: no ejecuta inferencia. |
| **CPN** | Nodo B (contenedor con GPU) | Inferencia OVD, postproceso, publicación, evaluación de patrones, alertas, persistencia, observabilidad. |
| **TN** | No materializado aún — jornada comprometida (ADR-017) | Rol previsto: se ejerce en la jornada de fine-tuning comprometida (clúster Mendieta como TN, E-04). El estado a la entrega se declara con causa técnica (puertas del doc 100 §6), nunca temporal. *(✎ 2026-08-11 — decía "no ejercido, exclusión declarada E-04, por presupuesto de tiempo".)* *(✎ 2026-08-17: el TN se EJERCIÓ — la jornada T1 corrió en Mendieta y cerró con veredicto pre-registrado, doc 123.)* |
| **Módulo de distribución** *(✎ fila agregada 2026-08-18, ADR-019)* | Junto al CPN en el prototipo; **unidad desplegable propia** desde ADR-019 (servicio HTTP `:8082`) — puede co-ubicarse o separarse sin cambiar contratos | Consumo del bus de alertas, política de notificación, ledger de idempotencia, entrega MQTT QoS 1. Dos modos de ejecución equivalentes: proceso lanzado por el orquestador (default) o servicio propio; la selección es de despliegue, no de diseño |

Agregar también el hallazgo de relojes que surge de esta topología (ver R-10).

**Y de paso, la errata:** en §17.3.15 la oración *"La definición de estos roles no implica…"* aparece
**duplicada** con variantes.

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

## R-18 · Tabla 43 (DA-01…DA-13) · PRECISA · media
### Actualizar el estado de las decisiones

Varias decisiones "condicionadas" ya se resolvieron y algunas "adoptadas" cambiaron de contenido. Revisión
sugerida (a validar una por una):

| DA | Dice | Estado real | Acción |
|---|---|---|---|
| DA-03 | canal ≠ repositorio; tecnología diferida | **Tecnología fijada**: ZeroMQ + msgpack; broker excluido con costura documentada | Actualizar |
| DA-06 | MOT opcional | **Acotada**: granularidad de sujeto especificada, tracker **no implementado** | Precisar |
| DA-07 | fine-tuning condicionado | **Comprometida (ADR-017)** — y la razón importa: rama condicionada **por datos y protocolo** (F-100.1, regla Tabla 37), no por falta de recursos (split generado, Mendieta disponible, costo T1 por extrapolación medida: ≈16 min centrales —prudente 30–45 min; walltime 2 h—, `operacion/100` adenda; la cifra histórica “≈1 GPU-h” quedó superada); **se ejerce como jornada experimental completa**. *(✎ 2026-08-11 — decía "no ejercida por presupuesto de tiempo". ✎ 2026-08-14 — el costo decía “≈1 GPU-h medido”; reemplazado por la extrapolación medida de `operacion/100`, adenda 2026-08-13.)* | Reencuadrar conforme ADR-017 |
| DA-11 | preselección en borde condicionada | **No ejercida** (E-07) | Confirmar |
| DA-13 | alerta interna antes que notificación | **Adoptada y reforzada** por ADR-011 (el motor no suprime; la política vive aguas abajo) | Reforzar |

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

## R-19 · Tabla 50 · ERRATA · media
### `PatternDefinition` es huérfano

`PatternDefinition` aparece en la **Tabla 49** (como contrato de entrada al plano de control) pero **no tiene
fila en la Tabla 50**, que es la única tabla que da contenido a los contratos. Falta agregarla:

> **PatternDefinition** — *Define la condición evaluable y su criterio temporal.* Información mínima:
> identificador de patrón, condición asociada, clase del sujeto, clase de protección requerida, **granularidad**,
> región de evaluación, umbrales de evidencia, ventana de confirmación, histéresis de resolución y severidad
> configurada.

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

## R-20 · Tabla 57 (riesgos) · PRECISA · media
### Los riesgos que se materializaron

La tabla de riesgos es prospectiva. Hoy sabemos **cuáles se materializaron**, y contarlo con la mitigación
efectiva es más fuerte que la previsión original. Los tres principales:

1. **Riesgo materializado: no hay un modelo que haga las dos cosas.** Los modelos capaces de sostener CR-01
   no siguen el ritmo de la cámara (14–22 % de keep-up en RTSP); los que sí lo siguen son ciegos al estado
   observable de CR-01. Es un hallazgo del trabajo, no una falla.
2. **Riesgo materializado: identidad de detección inestable** ⇒ mitigado con granularidad de escena (R-04).
3. **Riesgo materializado: pérdida silenciosa en el transporte** ⇒ mitigado con numeración de secuencia y
   degradación explícita de la corrida (R-08).

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

## R-21 · Tablas 58 y 59 (backlog) · EVIDENCIA · alta
### El backlog ya no es un backlog: es un estado

> ✎ **2026-08-05 — DESBLOQUEADO, con una corrección sustantiva.** Este ítem esperaba
> ADR-015 (doc 95 §5.3), ya escrito:
> `decisiones/adr-015-cierre-de-alcance.md` (fuente: `docs/decisiones/adr-015-cierre-de-alcance.md`)
> (✅ aceptada el 2026-08-05). **El resumen de estado de abajo tiene un punto FALSO al cierre:** dice
> *"MOT ✗ (especificado, tracker no implementado, E-03)"*. La granularidad por sujeto **sí
> está implementada y medida** — es el mejor resultado del banco (F1 0,930 sobre 34 clips,
> más verificación en vivo). Lo excluido son las **métricas** MOT (E-10, "no aplicable"),
> no la capacidad. Corregir esa fila al transcribir; el resto del resumen (11/11 del
> núcleo, EBE ✅, rol EN ✅, inspección ✅) se sostiene. (✎ 2026-08-11: la fila
> "fine-tuning ✗ E-04" **cambió por ADR-017** — jornada experimental comprometida, se
> transcribe con su estado a la entrega, con causa técnica.) Estado
> completo por exclusión: **ADR-015 §2a** + **ADR-017** para E-04.

Los 16 ítems del backlog tienen hoy un estado real y verificable. Propuesta: **convertir las Tablas 58/59 en
una tabla de estado** (ítem → entregable → **estado** → evidencia), que es exactamente el tipo de tabla que
el tutor espera encontrar en un capítulo de concreción.

Resumen del estado (a transcribir ítem por ítem): **de los 11 ítems del núcleo, 11 están construidos**
(configuración, lectura DBE, prompts versionados, adaptador OVD, postproceso, instrumentación de medios,
publicación y persistencia, evaluación de patrones, alertas por episodio, instrumentación de control,
reporte consolidado). De las 5 extensiones: EBE ✅ (two-node dockerizado, verificado con cámara IP real),
rol EN ✅ (Nodo A), inspección ✅ (webconsole), fine-tuning → **jornada experimental comprometida**
(E-04, ADR-017 — se transcribe con su estado a la entrega), MOT ✗ (especificado,
tracker no implementado, E-03).

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

## R-22 · §17.3.14.5 · PRECISA · media
### EBE: lo que ya se hizo y la brecha que queda

**DEBE DECIR** — dos precisiones honestas:

1. **La fuente viva ya se ejercitó realmente**: cámara IP por RTSP, con timestamps de reloj de pared
   verificados. El EN candidato del informe (OAK-D Pro PoE) no estuvo disponible al inicio y se ejerció la
   **contingencia oficial ya prevista** en §17.1.4.2.4 (cámara IP convencional). **Update 2026-07-13: el
   hardware llegó y quedó integrado y verificado E2E como fuente `oak_d`** — la narrativa para el informe
   es doble y más fuerte: la contingencia estaba escrita antes de necesitarla, Y el EN candidato terminó
   funcionando como estaba previsto (captura en la OAK, inferencia en el host). **Update 2026-07-15/18:
   además, EN-2 quedó implementada como variante opcional on-device** (gate de personas en la cámara,
   fail-open, default off; A/B real con GDINO: 87 % de drop on-device) — ver nucleo/10 E-07 y doc 56 §2.1;
   la afirmación previa "EN-2 sigue fuera de alcance" quedó superada.
2. **Queda una brecha declarada**: comparar DBE y EBE **sobre la misma fuente** (reproducir un clip anotado
   como stream) requiere un ancla de sincronización entre el reloj de pared del stream y el tiempo de medio
   del ground truth. Está identificada, no resuelta.

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

## R-23 · varias · ERRATA · baja
### Erratas de forma

- **Las seis figuras están vacías** en el documento y **cinco no tienen número** ("Figura x"). Hay que
  dibujarlas: vista lógica (4.1), pipeline de medios, plano de control, máquina de estados, cadena de
  traducción, roles. **Más la vista de procesos nueva** (R-09).
- Títulos de tabla pegados al número: "Tabla 44Elementos…", "Tabla 45Vocabulario…", "Tabla 51Hechos…",
  "Tabla 58Backlog…", "Tabla 59Backlog…".
- Oración **duplicada** en §17.3.15 (ver R-17).
- Frases pegadas sin espacio tras el punto en §17.3.15 y §17.3.18 ("…condicionadas.La arquitectura…").
- Errata de puntuación en §17.3.5, línea 235: "…o flujos de streaming**, El** plano de medios…".
- **NO son erratas** (verificar sólo visualmente al exportar a PDF): los "nombres de métrica vacíos" de la
  §17.3.13.1 y la Tabla 52 son **objetos de ecuación de Word** que la extracción automática no captura.
  En el documento original casi con seguridad se ven bien.

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

## R-24 · fuera del §17.3 · PRECISA · media
### Inventario de datasets desactualizado

> ✎ **2026-08-06 — el insumo ya existe (escritura pura):** el inventario quedó **al
> día el 2026-08-05** (`operacion/99` — relevamiento completo de datasets de imágenes,
> registry actualizado), como ya lo registró la anotación de R-13. El redline sigue
> siendo transcribir la selección efectiva al informe; la evidencia está lista.

El inventario del informe (SH17, SHEL5K, CHV, Pictor-PPE, Construction-PPE, GDUT-HWD, SHWD, SODA, MOCS) es
**anterior a la selección efectiva**. Los tres conjuntos realmente utilizados son
`construction_site_safety`, `chv` y `ppe_siabar`. El documento final debe declarar **qué candidatos se
retuvieron y por qué** — no dejar la lista larga como si todos se hubieran usado.

*(Este ítem vive fuera del capítulo 17.3, pero se registra acá para no perderlo.)*

> ✎ **2026-08-18 — precisión del usuario: son DOS catálogos, y hay que separarlos.**
> El párrafo de arriba resuelve solo uno. La sección de datasets **utilizados** (distinta
> de la de **candidatos evaluados**) tiene que distinguir tres cosas:
>
> **(a) Catálogo de candidatos evaluados** — la lista larga del informe (SH17, Pictor-PPE,
> GDUT-HWD, SHWD, SODA, MOCS…), con **por qué cada uno no se retuvo**. Es trabajo de
> relevamiento y vale declararlo; lo que no se puede es dejarla como si todos se hubieran
> usado.
>
> **(b) Catálogo de datasets utilizados para ENTRENAMIENTO/adaptación** (rol TRAIN):
> `construction_site_safety`, `chv`, `ppe_siabar`.
> (✎ 2026-08-28 — **corregido contra código, `operacion/130` R-02:** ése es el rol TRAIN
> **histórico** (`train_v2`, archivado en `legacy/` el 08-15). El entrenamiento **efectivo**
> (`finetuning_v1`, T1/T2) fue `construction_site_safety` 2.203 + `ppe_siabar` 743 = **2.946
> train / 483 val**, con **`chv` EXCLUIDO** por anti-leakage: el 100 % de sus 1.330 imágenes es
> estrato del banco. El informe declara (b) como css + ppe_siabar, nunca con chv.)
>
> **(c) Catálogo de FUENTES del banco de evaluación de imágenes (`bench_v3`)**, que **no
> es el mismo conjunto**: `construction_site_safety` (CC BY 4.0), `chv` y `shel5k`
> (CC BY 4.0). `ppe_siabar` **no** aporta al banco; `shel5k` **no** se usa para entrenar.
> Confundir (b) con (c) es el error fácil, porque comparten dos nombres de tres.
>
> **La trampa concreta, que ya se coló una vez en el material:** el banco se describe como
> *"6.477 imágenes de tres fuentes independientes"* y sus estratos se llaman `bench_obra`,
> `chv` y `shel5k`. **`bench_obra` NO es una cuarta fuente ni un dataset externo**: es el
> **subconjunto curado internamente** de los splits `valid` (114) + `test` (82) de
> `construction_site_safety` v27. Cadena: **196** imágenes → auditoría de dominio del
> 2026-07-23 → se excluyen **49 imágenes** fuera del dominio de obra (selfies con barbijo,
> PASCAL VOC, aeropuerto, casino, librería, karting) y **4 cajas `bare_head` < 9 px²** →
> **147** (85 val + 62 test). Dentro del banco, `bench_obra_val` y `bench_obra_test` son
> **un solo estrato de 147**, no dos.
>
> Redacción sugerida para el catálogo de utilizados: *"`bench_obra` es el núcleo interno
> curado del BENCH de Construction Site Safety v27: conserva 147 de las 196 imágenes
> originales de validación y prueba, tras excluir contaminación fuera del dominio de obra
> y anotaciones subpíxel."* Procedencia verificable:
> `datasets/scripts/curate/build_bench_obra.py` y `datasets/registry/curation_bench_obra.md`
> (conteos por clase antes/después: `bare_head` 110 → 61, casi la mitad era contaminación
> o sub-píxel — eso cambia cómo se lee la debilidad de esa clase).

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

## R-25 · §17.3.11 (Tabla 50) y §17.3.13 · CONCRETA · alta
### El contrato de ground truth temporal y la convención de identidad de fuente

**DICE HOY** — nada. El capítulo define contratos para la corrida, pero **ninguno para la referencia contra
la que se evalúa**. Sin embargo, la evaluación de alertas —de donde salen P/R/F1, TTFD y SDR— depende de un
contrato de anotación tan formal como los otros.

**DEBE DECIR** — agregar el contrato a la tabla:

> **Referencia temporal de evaluación** (`clip_gt.v2`) — *Anota, por clip, los episodios en que una
> condición de riesgo está efectivamente presente.* Información mínima: identificador de clip, episodios
> con inicio y fin en milisegundos y condición asociada, eventos por debajo del umbral de persistencia,
> tolerancia de frontera, procedencia de la anotación (anotador, doble anotación, coeficiente de acuerdo) y
> las ventanas de persistencia del conjunto de patrones con el que se comparará.

Y declarar **dos invariantes** que no son detalle de implementación —son condiciones de validez de la
medición— y que se descubrieron por las malas:

1. **La identidad de la fuente y la del clip anotado son la misma.** El emparejamiento entre una alerta y un
   episodio anotado es, literalmente, una comparación de identificadores de fuente. Si la corrida etiqueta
   la fuente de un modo y la anotación de otro, **el emparejamiento falla en silencio y la exhaustividad da
   cero** sin ningún error visible. Es una convención de contrato, no una preferencia.
2. **La incertidumbre nunca fabrica una infracción.** Cuando el estado de un elemento de protección no puede
   determinarse en la anotación, el episodio **no se declara**: un atributo desconocido corta la corrida de
   violación en lugar de extenderla. La referencia se construye para ser conservadora.

**Y los cinco hitos por alerta** (que hoy tampoco están, y son los que hacen computable la cadena): primera
evidencia positiva —con su unidad visual, que es la clave de unión entre planos—, transición a candidato,
transición a confirmado, registro de la alerta y, cuando exista canal, confirmación de entrega.

**POR QUÉ** — spec 43 (`clip_gt.v2`), doc 54 §5 (la convención de identidad: sin ella, recall 0 en silencio),
spec 40 §5.4 (los cinco hitos).

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

## R-26 · §17.3.17 / §17.3.18 · CONCRETA · **alta (y es la más valiosa)** → **texto en doc 94 §9**
### Extensibilidad medida: cuánto cuesta agregar una condición nueva

**DICE HOY** — nada. Y es, probablemente, el hueco más caro de todo el capítulo.

**DEBE DECIR** — tu tesis **no** es "OVD detecta mejor". Es *"qué se logra con una plataforma que expresa
condiciones en lenguaje, sin entrenar"*. Todo el resto del capítulo mide latencias, pérdidas y ventanas —
cosas que un sistema de vocabulario cerrado también podría medir. **Esta sección mide lo único que un
detector cerrado no puede hacer**, y hoy no está escrita en ningún lado.

La tabla de costos de extensión, con su frontera declarada:

- Una **condición nueva del mismo tipo** (sujeto sin elemento de protección) → **sólo configuración**: una
  entrada declarativa en el conjunto de patrones + las formulaciones de prompt. **Cero código, cero
  reentrenamiento.**
- Una **familia nueva** de condiciones (relacional, zonal, de trayectoria) → **un evaluador nuevo**.
- Un **modelo nuevo** → un adaptador. Una **fuente nueva** → un adaptador.

**El contraste entre las dos primeras filas es la contribución arquitectónica del trabajo**: delimita la
frontera real de la extensibilidad por lenguaje, en vez de prometer que "todo es configurable".

> ✎ **2026-08-06 — DESBLOQUEADO: A1 YA CORRIÓ (2026-08-05, `operacion/94`).** El
> condicional de abajo quedó viejo — el número existe y es AF-4 del doc 98:
> **0 entrenamientos · 1 archivo de 48 líneas · 9 minutos · 0 GT nuevo anotado**,
> `machinery` **AP@0.5 0,662 zero-shot** (n=99 cajas), por encima del agregado del
> campeón con las clases configuradas. Con el contrapeso obligatorio **F-94.1**
> (validar la palabra: `vehicle` junto a `machinery` = 0 detecciones; el bench lo
> expone en ~3 min). Cifras: `results/bench_imagenes/index.md` §4.

Si el **mini-experimento A1** (costo marginal de una condición nueva, doc 10 ítem 8) llega a correrse, su
número va acá: *N líneas de configuración, T minutos, una corrida registrada*. Vale más, en la defensa, que
media docena de latencias.

**→ Texto completo en `94-secciones-nuevas-etapa3.md` §9.**

**DECISIÓN:** [ ] acepto  [ ] modifico  [ ] rechazo
**Notas:**

---

## Orden sugerido de trabajo

1. **R-01 y R-05 juntos** (van de la mano: estrategia + vocabulario). Es el ajuste que más cambia el capítulo.
   *Antes de escribirlo, decidí el punto (a)/(b) de R-01: compromete o no el experimento comparativo.*
2. **R-02, R-03, R-04** (las otras contradicciones). Con esto el capítulo deja de contradecir al sistema.
3. **R-06, R-07 y R-25** (contratos concretos + evolución del evento + contrato de la referencia). Con esto
   el capítulo deja de ser conceptual: es la respuesta al tutor.
4. **R-26** (extensibilidad medida). Barato de escribir y es el argumento central de la tesis.
5. **R-12 y R-13** (evidencia + límites). Con esto el capítulo es *verificable*, que es la palabra que usó él.
6. El resto, en orden de prioridad de la tabla.

---

## Fuente: `docs/informe/ajustes/material-etapa-3/94-secciones-nuevas-etapa3.md`

> SHA-256 del bloque: `f75c33fe8fc65b0187c2e8f2c9815b440d2919d83c7d1a283d9bf59b53b9273f`  
> Seleccion: documento completo.

# Secciones nuevas para Etapa 3 — texto redactado, listo para copiar

- **Fecha:** 2026-07-12 · **v2, tras auditoría adversarial** (ver `95-auditoria-y-plan-de-cierre.md`)
- **Qué es esto:** el **texto en prosa** de los redlines que requieren escritura extensa, redactado en el
  registro del informe (impersonal, académico) para que lo revises, lo corrijas y lo **pegues en el Google
  Docs**. Cada sección corresponde a un ítem de `93-redlines-etapa3.md`.
- **Convención:** el texto que se copia va en **bloques de cita** (`>`). Lo que está fuera son **notas para
  vos**, no van al informe.
- **Regla de números, no negociable:** toda cifra de este documento sale de la **tabla canónica**
  (`92-anexo-concrecion-tecnica.md` §10), que dice qué corrida y qué detector la produjo. La v1 de este
  documento tenía cifras mal atribuidas y un JSON fabricado; la auditoría los encontró. **Si una cifra no
  está en la §10 del doc 92, no entra acá.**

> ✎ **2026-08-12 — dos correcciones antes de transcribir.**
>
> 1. **La regla de números de arriba está derogada en su parte de fuente.** Desde el 2026-08-05 las cifras
>    salen de los **cuatro índices de `e-ovrt_experimental-setup/results/`** (verificables con
>    `operacion/datos/96-verificar-indices.py`); la §10 del doc 92 sirve para saber **qué corrida produjo
>    qué**, no para citar el valor. El espíritu de la regla no cambia: **si una cifra no está en un índice
>    verificable, no entra acá.**
> 2. **La fila de identidad de sujeto de la Tabla 63 (§2) estaba desactualizada y se corrigió.** Decía que
>    el componente que puebla `track_id` no está implementado: es falso desde el 2026-08-04. La corrección
>    está aplicada en su lugar, con el reparto de contenido entre §17.3 y §17.4 que exige la regla de
>    no-anacronismo. Contexto completo: `92` §4.2.
> 3. **La distribución de alertas ya no se redacta como exclusión** (§1.1 y Tabla 61): ADR-016 la reabrió
>    como **trabajo comprometido**. Aplicado abajo.

| § de este doc | Redline | Destino en el capítulo |
|---|---|---|
| §1 | R-06 | §17.3.11 — contratos concretos |
| §2 | R-07 | §17.3.11.4 — evolución del contrato (**el pedido del tutor**) |
| §3 | R-08 | §17.3.8.1 y §17.3.8.4 — transporte concreto |
| §4 | R-09 | §17.3.5 — figura nueva (vista de procesos) |
| §5 | R-10 | §17.3.13 — diccionario de métricas |
| §6 | R-11 | §17.3.14 — temporalidad de la fuente |
| §7 | R-12 | sección nueva de verificación |
| §8 | R-13 | sección nueva de límites |
| §9 | R-26 | §17.3.17/18 — extensibilidad medida |

---

# §1 — Contratos concretos (R-06 → §17.3.11)

**Nota:** el orden importa. Primero se **conserva** el principio original (los contratos estabilizan
semántica, no tecnología); después se declara que **para el núcleo eso ya se materializó**; recién ahí se
muestra. Así no parece que nos desdecimos: parece que cumplimos.

## 1.1 Párrafo de apertura — reemplaza el hedge actual

> Los contratos definidos en esta sección cumplen la función de **estabilizar la semántica de intercambio**
> entre componentes: acuerdan qué información cruza cada frontera, no cómo se codifica. Esa función se
> mantiene. Sin embargo, a diferencia de la formulación inicial del diseño, **los contratos del núcleo
> validable ya no son denominaciones preliminares**: se materializaron durante la implementación como
> modelos de datos versionados, con serialización explícita, esquema verificable e interfaces de servicio
> concretas, y existen corridas registradas que los ejercitan de extremo a extremo.
>
> En consecuencia, esta sección presenta cada contrato del núcleo en dos planos: su **función
> arquitectónica** —qué acuerda y entre qué componentes— y su **materialización efectiva** —qué estructura
> de datos, qué versión de esquema y qué interfaz lo realizan—. Los contratos correspondientes a
> capacidades **aún no materializadas**, en particular los del tramo de distribución de alertas, conservan
> su carácter preliminar, y su estado de implementación se declara explícitamente en cada caso.

*(✎ 2026-08-12 — la frase final decía "capacidades **no implementadas** … se declaran explícitamente como
tales", redacción heredada de cuando la distribución era exclusión ejercida. **ADR-016 la reabrió como
trabajo comprometido**: el contrato sigue siendo preliminar, pero el texto no puede clausurar la
implementación. Al transcribir, ajustar según el estado real a la entrega — ver `03-etapa-3` §5.)*

## 1.2 Tabla de correspondencia — contrato preliminar ↔ artefacto real

> **Tabla 61**
> *Correspondencia entre los contratos preliminares del diseño y su materialización efectiva*
>
> | Contrato del diseño | Materialización | Versión de esquema | Componente |
> |---|---|---|---|
> | RunConfig | Manifiesto de experimento + configuraciones efectivas por plano | `experiment.manifest.v1` | Soporte experimental |
> | SourceDefinition | Sección de fuente de la configuración + registro de adaptadores de ingesta | — | Plano de medios |
> | ModelProfile | Catálogo de perfiles de modelo (un archivo por variante) | — | Plano de medios |
> | PromptDefinition | Conjunto de prompts versionado, identificado en cada evento | — | Soporte experimental |
> | FrameMetadata | Unidad visual interna + bloque de fuente del evento publicado | — | Plano de medios |
> | **PerceptionEvent** | **DetectionEvent** | **`media.detection.v1`** | Plano de medios |
> | PatternDefinition | Definición declarativa dentro del conjunto de patrones | — | Plano de control |
> | PatternStateChanged | PatternStateChanged | `control.pattern_state.v1` | Plano de control |
> | AlertEvent | AlertEvent (identificador determinista, idempotente) | `control.alert.v1` | Plano de control |
> | MetricSample | MetricSample / ControlMetricSample | `media.metric.v2` / `control.metric.v1` | Ambos planos |
> | ErrorEvent | Registro de errores por corrida | — | Ambos planos |
> | Bus interno de eventos | Publicación ZeroMQ con envoltorio versionado | `bus.envelope.v1` | Frontera entre planos |
> | Repositorio de eventos | Archivos de sólo adición por corrida | — | Ambos planos |
> | Referencia temporal de evaluación | Anotación de episodios por clip | `clip_gt.v2` | Soporte experimental |
> | Reporte experimental | Reporte consolidado de corrida | — | Soporte experimental |
> | Alerta distribuida | Notificación entregada por MQTT con confirmación y registro idempotente | `control.notification.v1` | Módulo de distribución |
>
> *Nota.* Los contratos con versión de esquema declarada están implementados y verificados en corridas
> registradas.

✎ **2026-08-18:** la fila "Alerta distribuida" decía *"(preliminar — pendiente de
materialización)"* y la nota le reservaba "carácter preliminar" — quedó superado (la
cabecera de este doc ya lo anticipaba: ADR-016 la reabrió como trabajo comprometido, y
se materializó). El contrato `control.notification.v1` está **implementado y verificado**
(docs `operacion/114`/`118`; entrega MQTT QoS 1 con ledger de idempotencia), y el módulo
se dispara por HTTP desde el orquestador, igual que los otros dos servicios (ADR-019 +
ADR-020, doc 124); el subproceso quedó como fallback operativo, fuera del relato.

## 1.3 El contrato central, mostrado

> El contrato de mayor centralidad arquitectónica es el **evento de percepción**, que traduce la salida
> heterogénea del detector en evidencia perceptiva común. Se materializa como una estructura de datos
> validada, identificada por la versión de esquema `media.detection.v1`, que agrupa: la identificación de
> la corrida y de la unidad visual; la descripción de la fuente; el modelo y el conjunto de prompts
> efectivamente utilizados; el conjunto de detecciones normalizadas; y la instrumentación temporal de la
> unidad.
>
> El fragmento siguiente reproduce un evento **real** de una corrida de la campaña sobre el banco
> congelado: la unidad visual en la que el sistema confirma la condición CR-01, exactamente a los
> 4.000 ms de persistencia configurados desde la primera evidencia. La unidad contiene tres detecciones
> y se muestran las tres.

**Nota:** presentalo como *Figura N — Evento de percepción (extracto de artefacto real)*, en monoespaciado.
Es lo que el tutor pidió con nombre propio ("un DTO"). **Este JSON es literal** — verificado contra
`detections.jsonl`, unidad `frame_000229`. No lo "mejores" al pegarlo.

> ✅ **✎ 2026-08-22 — RESUELTO por la opción (a), re-transcripción sobre clip vigente.** La versión
> anterior de este ejemplo salía de `cb_b01_p7`, retirado del banco el 2026-08-03. El JSON de abajo
> es la **transcripción literal** de la unidad `frame_000229` de
> `run_20260803_211225_dbe_grounding_dino_1e06f3` — corrida real de la campaña del banco congelado
> sobre **`a_p1_c02`** (clip vigente del rodaje, escenario P1, CR-01). La confirmación se reprodujo
> por replay del control-plane y quedó archivada en
> `operacion/datos/129-2026-08-22-bench-a_p1_c02-gdino-alerts.jsonl` (+ `…-summary.json`).
> Bonus pedagógico de esta unidad: **contiene un `helmet` (0,456) y aun así CR-01 confirma**, porque
> el casco está fuera de la región cefálica del sujeto — la inferencia de ausencia es por sujeto y
> por región, no por presencia de la clase en el frame.

> ```json
> {
>   "schema_version": "media.detection.v1",
>   "event_type": "detection_event",
>   "run_id": "run_20260803_211225_dbe_grounding_dino_1e06f3",
>   "unit_id": "frame_000229",
>   "source":  { "source_id": "a_p1_c02", "source_type": "video_frame",
>                "frame_index": 229, "timestamp_ms": 7633.33,
>                "width": 1920, "height": 1080 },
>   "model":   { "name": "grounding_dino",
>                "model_id": "IDEA-Research/grounding-dino-tiny", "device": "cuda" },
>   "prompts": { "prompt_set_id": "cr01_cr02_v2_short" },
>   "detections": [
>     { "detection_id": "det_000001", "label": "person",
>       "prompt_id": "person", "source_prompt": "person", "confidence": 0.88,
>       "bbox_xyxy":      [1239.8, 149.8, 1503.2, 861.9],
>       "bbox_norm_xyxy": [0.6457, 0.1387, 0.7829, 0.7981],
>       "area_px": 187612.4, "model_name": "grounding_dino" },
>     { "detection_id": "det_000002", "label": "vest",
>       "prompt_id": "vest", "source_prompt": "vest", "confidence": 0.8755,
>       "bbox_xyxy":      [1286.5, 235.3, 1459.3, 487.0],
>       "bbox_norm_xyxy": [0.67, 0.2179, 0.76, 0.4509],
>       "area_px": 43490.1, "model_name": "grounding_dino" },
>     { "detection_id": "det_000003", "label": "helmet",
>       "prompt_id": "helmet", "source_prompt": "helmet", "confidence": 0.456,
>       "bbox_xyxy":      [1519.0, 432.5, 1648.1, 521.3],
>       "bbox_norm_xyxy": [0.7911, 0.4005, 0.8584, 0.4827],
>       "area_px": 11463.6, "model_name": "grounding_dino" }
>   ],
>   "timing": { "normalize_ms": 8.06, "inference_ms": 491.17,
>               "postprocess_ms": 0.08, "write_ms": 0.0, "total_ms": 491.27 }
> }
> ```
>
> El evento se **persiste antes de publicarse**: la línea escrita en el repositorio de la corrida y el
> mensaje transmitido por el bus contienen exactamente el mismo contenido. Esta propiedad, verificada, es
> la que garantiza que toda corrida ejecutada en vivo sea **re-evaluable de forma offline** produciendo
> artefactos idénticos.

## 1.4 Los contratos del plano de control

> El plano de control produce dos contratos. El **cambio de estado de patrón**
> (`control.pattern_state.v1`) registra cada transición de la máquina de estados, junto con la evidencia
> que la motivó y los hitos temporales del episodio. La **alerta interna** (`control.alert.v1`) registra la
> confirmación de un episodio de riesgo. El fragmento siguiente reproduce la alerta **real** del replay
> sobre el mismo clip del banco vigente que el evento de percepción anterior (`a_p1_c02`), archivada el
> 2026-08-22.

> ```json
> {
>   "schema_version": "control.alert.v1",
>   "event_type": "alert_event",
>   "control_run_id": "bench_a_p1_c02_gdino_20260822_20260822T225536Z",
>   "media_run_id":   "run_20260803_211225_dbe_grounding_dino_1e06f3",
>   "alert_id": "394c9116-a38d-568d-b620-20d147c4cac9",
>   "pattern_id": "CR-01", "condition_id": "CR-01",
>   "subject_key": "CR-01:a_p1_c02", "source_id": "a_p1_c02",
>   "severity": "high", "state": "open",
>   "unit_id": "frame_000229", "frame_index": 229, "timestamp_ms": 7633.33,
>   "evidence": {
>     "subject": { "detection_id": "det_000001", "label": "person", "confidence": 0.88,
>                  "bbox_xyxy": [1239.8, 149.8, 1503.2, 861.9] },
>     "missing_class": "helmet",
>     "supporting": [],
>     "score": 0.88, "subjects_in_evidence": 1,
>     "rationale": "No se encontro evidencia 'helmet' en region 'upper_body' de 1 sujeto(s)."
>   },
>   "first_evidence_ms": 41990631.527, "first_evidence_unit_id": "frame_000109",
>   "first_evidence_frame_index": 109,
>   "alert_registered_ms": 41990642.511
> }
> ```
>
> Cuatro propiedades de estos contratos merecen ser señaladas, porque sostienen afirmaciones del diseño.
>
> **La identidad del sujeto de estado es explícita.** La clave de estado se compone como
> `(patrón, fuente)` bajo granularidad de escena, y como `(patrón, fuente, identidad)` bajo granularidad de
> sujeto. El identificador de detección **no se utiliza como identidad en ningún caso**, por las razones
> expuestas en §17.3.8.3.2.
>
> **La alerta es idempotente.** Su identificador se deriva de forma determinista del episodio que la
> origina, de modo que reprocesar una misma corrida produce el mismo identificador. Los consumidores aguas
> abajo pueden deduplicar sin necesidad de estado compartido.
>
> **La evidencia de la ausencia es auditable.** La alerta transporta el sujeto detectado, las detecciones
> de soporte, la clase de protección ausente, la región evaluada y una justificación legible. La ausencia
> no es una afirmación opaca del modelo: es una inferencia reconstruible. Este es, en términos prácticos,
> el argumento principal a favor de la estrategia indirecta adoptada en §17.3.9.2 — un prompt de negación
> produce una decisión, pero no produce esta evidencia.
>
> **El sistema confirma cuando su configuración lo prescribe.** La primera evidencia cae en
> `frame_000109` (3.633,33 ms de video) y la confirmación en `frame_000229` (7.633,33 ms): exactamente
> los 4.000 ms de la ventana de persistencia configurada para CR-01, verificables desde los hitos
> `first_evidence_*` que la propia alerta transporta.

## 1.5 Las interfaces de servicio

> Los dos planos se ejecutan como **servicios independientes gobernados por configuración**, expuestos
> mediante interfaces HTTP. Esta materialización no estaba fijada en el diseño inicial —que deliberadamente
> difería la distribución de componentes— y se adoptó para permitir que ambos planos se dispongan en el
> mismo host o en hosts distintos sin modificar su lógica, y para que el soporte experimental pueda
> orquestar corridas de forma reproducible.
>
> **Tabla 62**
> *Interfaces principales de los servicios de la plataforma*
>
> | Servicio | Operación | Función |
> |---|---|---|
> | Plano de medios | `POST /api/runs` | Dispara una corrida. Recibe fuente, conjunto de prompts, parámetros de corrida, configuración de bus e identificador de experimento. Devuelve el identificador de corrida. |
> | | `GET /api/runs/{id}` | Estado y resumen de la corrida. |
> | | `GET /api/runs/{id}/detections` | Evidencia perceptiva paginada. |
> | | `POST /api/runs/{id}/evaluate` | Evaluación de percepción contra el conjunto de referencia. |
> | | `GET /readyz` | Disponibilidad del modelo cargado. |
> | Plano de control | `POST /api/runs` | Dispara una corrida en modo diferido o en vivo. |
> | | `GET /api/runs/{id}/alerts` | Alertas internas registradas. |
> | | `GET /api/config` | Configuración efectiva de la corrida. |
>
> Dos decisiones de diseño se materializan en estas interfaces. Primero, **el modelo no viaja en la
> petición**: se carga una única vez al iniciar el servicio, de modo que el costo de carga de pesos —del
> orden de decenas de segundos— queda fuera de la ruta crítica de la corrida; comparar modelos implica
> disponer servicios distintos, no reconfigurar uno. Segundo, **la respuesta afirmativa a una corrida en
> vivo del plano de control implica que su consumidor de eventos ya está suscripto al bus**, invariante que
> el orquestador verifica antes de disparar el plano de medios, por las razones expuestas en §17.3.8.4.

---

# §2 — Evolución del contrato de inferencia (R-07 → §17.3.11.4)

**Nota:** esta es **la** sección que responde al tutor. No promete: muestra la regla, muestra el campo, y
declara qué falta. Esa honestidad **es** el argumento.

> ## Evolución del contrato de evidencia perceptiva
>
> El evento de percepción es el contrato con mayor superficie de cambio previsible del sistema: es el punto
> por el que ingresan las capacidades perceptivas que el prototipo no ejerce —identidad persistente de
> sujeto, cinemática, pose, segmentación— y las que aún no se han considerado. Un contrato que deba
> reescribirse cada vez que el sistema aprende algo nuevo sobre la escena no es un contrato: es un cuello
> de botella. Por esa razón su regla de evolución se define explícitamente y forma parte del diseño.
>
> **Primera regla: la evolución es aditiva.** Toda capacidad nueva se incorpora como **campo opcional con
> valor por defecto**, nunca como campo requerido. Un productor que aún no computa la capacidad omite el
> campo; un consumidor que no la conoce lo ignora.
>
> **Segunda regla: un cambio aditivo no incrementa la versión del esquema.** El evento conserva su versión
> `media.detection.v1` cuando incorpora identidad de sujeto o cinemática, porque ningún consumidor escrito
> contra esa versión deja de ser válido. La versión se incrementa **únicamente** cuando cambia el
> significado de un campo existente o cuando un campo se elimina, es decir, cuando la compatibilidad se
> rompe de verdad.
>
> **Tercera regla: la versión viaja dentro del evento, no en el transporte.** El identificador de esquema
> es un campo del propio evento, tanto en su forma persistida como en su forma publicada. Un artefacto
> almacenado es, por lo tanto, **autodescriptivo**: puede releerse e interpretarse sin conocer el canal por
> el que viajó ni la versión del código que lo produjo, lo cual es una condición necesaria de la
> reproducibilidad experimental.
>
> **Cuarta regla: los consumidores toleran lo antiguo.** El plano de control acepta artefactos producidos
> por versiones anteriores del plano de medios, de modo que las corridas históricas permanecen evaluables.
>
> La tabla siguiente detalla el camino previsto para cada una de las extensiones perceptivas contempladas,
> y declara su estado efectivo en el prototipo.
>
> **Tabla 63**
> *Superficie de crecimiento del evento de percepción*
>
> | Capacidad | Materialización prevista en el contrato | Estado en el prototipo |
> |---|---|---|
> | **Identidad de sujeto** (seguimiento) | Campo opcional de identidad en la detección. Es la **única identidad válida entre frames**. | **Contrato completo en ambos planos**: el campo está definido en el esquema del productor —opcional, con la propiedad verificada de que su ausencia no altera la serialización— y el motor de patrones lo utiliza como clave de estado bajo granularidad de sujeto. **Es, además, la única extensión de esta tabla efectivamente ejercida**: la identidad se materializó como decorador de la fuente de eventos en el plano de control, activable por configuración y aplicable por igual al acople por archivo y al acople por bus, **sin modificar el contrato ni el plano de medios**. El plano de medios no emite el campo, de modo que la evidencia perceptiva persistida permanece inalterada; el núcleo validable se define sobre granularidad de escena y la granularidad de sujeto se reporta como capacidad medida (§17.4). |
> | **Velocidad y dirección** | Campos opcionales derivados. No requieren información nueva del detector: se derivan de la identidad de sujeto y de las marcas temporales **que el evento ya transporta**. | Especificado, no implementado. |
> | **Pose** | Campo opcional de puntos clave. | No implementado. El evaluador de patrones **sí parametriza la región de búsqueda según la geometría del sujeto** —la región se extiende a altura completa cuando la relación de aspecto sugiere una postura no erguida—, pero se trata de una heurística geométrica y **no de información de pose**. |
> | **Segmentación** | Campo opcional de máscara, **junto** al bounding box y no en su reemplazo, para no invalidar a los consumidores existentes. | Especificado, no implementado. |
> | **Detecciones asociadas** | Ya modelado, pero en el **plano de control**: la evidencia de patrón vincula el sujeto con sus detecciones de soporte y con la clase de protección ausente. | **Implementado.** |
>
> Este último punto expresa una frontera del diseño que conviene hacer explícita: **el plano de medios no
> asocia detecciones entre sí**. Publica evidencia perceptiva individual, normalizada y trazable; toda
> relación entre detecciones —espacial, temporal o de identidad— pertenece al plano de control. Esta
> separación es la que permite que el mismo evento de percepción sirva simultáneamente a la evaluación de
> patrones, a la evaluación de percepción contra el conjunto de referencia y a la reconstrucción
> experimental, sin que ninguna de esas lecturas contamine a las otras.
>
> Finalmente, se declara una restricción semántica que el contrato hace explícita porque su violación
> produce un error silencioso: **el identificador de detección es un índice dentro del frame y no
> constituye identidad entre frames**. Su uso como identidad temporal genera aliasing verificable: sobre
> una corrida de vídeo real, la detección identificada como `det_000001` recorre 1831 píxeles del ancho del
> cuadro —de 1920 píxeles— a lo largo de la corrida, con desplazamientos de hasta 1749 píxeles entre
> cuadros consecutivos. Es esa medición, y no una preferencia de diseño, la que fundamenta la adopción de
> la granularidad de escena para el núcleo validable.

**✎ 2026-08-12 — nota para el redactor sobre la fila de identidad de sujeto (leer antes de transcribir).**
La versión anterior de esa fila decía *"el componente que lo puebla no está implementado"*. **Era cierta el
12/07 y es falsa desde el 2026-08-04**, y da la casualidad de que es **la fila que más le importa al
tutor**: él preguntó si el evento puede sostener datos que hoy no están —tracking el primero de su lista—.
La respuesta honesta hoy es más fuerte que la que teníamos: **esa extensión se recorrió de punta a punta y
se midió**, y salió el mejor resultado del banco (identidad de sujeto contra escena, **con las mismas
detecciones bit a bit**: la ganancia es íntegramente del motor, no de la percepción).

Cómo se reparte, por la **regla de no-anacronismo**:

- **Acá (§17.3.11.4, Etapa 3)** va el **estado del contrato y el mecanismo**, sin cifra: contrato completo
  en ambos planos, productor no emisor, identidad resuelta como capacidad del consumidor por configuración.
  Eso es diseño, y corresponde a esta etapa.
- **La cifra, la comparación pareada y el trade-off van a §17.4** (`AJ-4.12`) **y §17.5**. Ahí se cita desde
  el índice de `results/`, y ahí se dice que el `track_id` **no queda en el JSONL del plano de medios** sino
  en los artefactos del control, con la trazabilidad sostenida por el determinismo del seguidor.
- **No confundir con la exclusión E-10:** lo excluido son las **métricas MOT**, no la capacidad.

Insumo verificado contra código, con ruta y línea: `92` §4.2 y su recuadro.

---

# §3 — El transporte, concreto (R-08 → §17.3.8.1 y §17.3.8.4)

**Nota:** el primer párrafo reemplaza la frase de **§17.3.8.1** ("el diseño no exige una tecnología
específica de mensajería"); el resto reemplaza **§17.3.8.4**.

> **[Reemplazo del párrafo de §17.3.8.1]** El bus interno cumple una función de **integración, no de
> razonamiento**: desacopla al productor de evidencia perceptiva de sus consumidores. El diseño no ata esa
> función a una tecnología —el mecanismo es deliberadamente sustituible—, pero el prototipo **sí adopta
> una**, y su elección, junto con las reglas de operación que se derivan de ella, se detalla en §17.3.8.4.

> ## Transporte y persistencia
>
> El diseño distingue el **canal de transporte** del **repositorio de eventos** (DA-03): el primero
> desacopla productores de consumidores; el segundo conserva los hechos para su reconstrucción. Esa
> distinción se mantiene, y la implementación la materializa de la siguiente manera.
>
> **El repositorio es la fuente de verdad.** Cada corrida escribe archivos de **sólo adición**, uno por
> tipo de hecho —evidencia perceptiva, cambios de estado, alertas, muestras de métricas, errores—, junto
> con la configuración efectiva, la procedencia de los datos y un manifiesto que registra la **versión de
> código** que produjo la corrida. El evento **se persiste antes de publicarse**: si el canal falla, el
> hecho no se pierde.
>
> **El canal transporta, y puede perder.** Se adoptó una publicación con patrón publicador/suscriptor sobre
> ZeroMQ, con serialización binaria compacta, envoltorio versionado y tópicos jerárquicos por corrida. La
> elección responde a tres criterios: no introducir un servicio intermediario pesado en el prototipo; no
> bloquear nunca la ruta crítica de inferencia; y conservar la capacidad de sustituir el mecanismo por un
> intermediario de mensajería (*broker*) sin modificar los planos, dado que la durabilidad la aporta el
> repositorio y no el canal.
>
> De la operación efectiva del canal se derivan tres reglas que forman parte del diseño y no de su
> implementación, porque su violación produce corridas inválidas.
>
> **El consumidor debe suscribirse antes de que el productor publique.** El patrón publicador/suscriptor
> **no retiene** los mensajes emitidos antes de que exista una suscripción. En consecuencia, el orden de
> disparo de una corrida en vivo es **primero el plano de control y después el plano de medios**, y el
> orquestador verifica la suscripción efectiva antes de continuar. No es una precaución: es una condición
> de corrección, y el prototipo la hace verificable — el publicador notifica las suscripciones activas, de
> modo que el sistema **comprueba** que hay un consumidor escuchando en lugar de suponerlo.
>
> **La pérdida se detecta, no se supone.** Un publicador con cola acotada **descarta mensajes en silencio**
> al saturarse, sin señalar error al emisor. Por esa razón cada mensaje transporta un **número de secuencia
> monótono**, y el consumidor contabiliza los huecos: una corrida con huecos se marca **degradada**, con su
> causa registrada. La corrida degradada no se descarta ni se silencia: se declara, y sus métricas se
> interpretan a la luz de esa declaración.
>
> **El canal no frena la percepción.** La publicación es no bloqueante: ante saturación, el sistema
> prefiere **descartar y declarar** antes que introducir contrapresión sobre la ruta crítica de vídeo, en
> coherencia con el principio de protección de la ruta crítica (§17.3.4).
>
> Como consecuencia de estas reglas se verifica una propiedad que sostiene la comparabilidad entre
> escenarios: **una corrida ejecutada en vivo y la relectura offline de sus artefactos producen resultados
> idénticos**. El escenario EBE no constituye, por lo tanto, un régimen de medición distinto, sino la misma
> cadena alimentada por una fuente de naturaleza temporal diferente.
>
> Finalmente, se registra una frontera de consumo: **el bus es interno a la plataforma**. La interfaz de
> inspección no consume el canal de eventos, sino las interfaces de servicio de ambos planos. Esto evita
> que una herramienta de observación introduzca acoplamiento con el mecanismo de transporte, que es
> deliberadamente sustituible.

---

# §4 — Figura nueva: vista de procesos (R-09 → §17.3.5)

**Nota:** esto **no** es texto para pegar: es la especificación de la figura. La Figura 4.1 actual se
**conserva** (es la vista lógica). Ésta es la segunda: la que muestra "cómo está hecho".

**Título propuesto:** *Figura N — Vista de procesos de la plataforma experimental*

**Cajas (procesos reales):**

| Caja | Etiqueta | Contenido |
|---|---|---|
| 1 | **Servicio de medios** | Ingesta → control de ritmo → normalización → inferencia OVD → postproceso → publicación. Modelo cargado al arranque. |
| 2 | **Servicio de control** | Consumo de eventos → motor de patrones → alertas internas → persistencia → métricas. |
| 3 | **Orquestador experimental** | Manifiesto de experimento; dispara ambos servicios; consolida artefactos; genera el reporte. |
| 4 | **Interfaz de inspección** | Cliente de las interfaces de servicio de ambos planos. |
| 5 | **Módulo de distribución** | Consumidor externo funcional: política, ledger, MQTT y registros. Marcar por separado las integraciones pendientes. |
| 6 | **Repositorio de corrida** | Archivos de sólo adición, uno por plano. |

**Flechas:**

- Orquestador **→** Servicio de control (corrida en vivo) — **1º**; su respuesta afirmativa implica suscripción activa.
- Orquestador **→** Servicio de medios (con bus habilitado) — **2º**. *Etiquetar el orden: es una regla de corrección, no un detalle de implementación.*
  (✎ 2026-08-28 — con la distribución como servicio, el orden **real** del runner es
  **① control → ② distribución → ③ medios** (`operacion/130` R-01, `runner.py:1095-1149`): la
  distribución va segunda porque necesita el `control_run_id`; los medios, últimos. La
  no-pérdida en el bus de alertas `:5558` la garantiza el **handshake XPUB** del control
  (`wait_for_subscriber_ms ≥ 10 s`), **no el orden**. Nunca "distribución primero" ni
  "inverso del flujo de datos". FIG-A regenerada con este orden el 2026-08-28.)
- Servicio de medios **→ bus →** Servicio de control. Etiqueta: evento de percepción + ciclo de vida de corrida.
- Servicio de medios **→** Repositorio, con la flecha **numerada antes** que la del bus (persiste primero, publica después).
- Servicio de control **→** Repositorio.
- Servicio de control **→ canal de alertas →** Módulo de distribución. La flecha es
  efectiva; anotar que su lanzamiento todavía no forma parte de la orquestación integral.
  ✎ **2026-08-18: la segunda cláusula quedó superada** — el lanzamiento SÍ forma parte de
  la orquestación integral desde el 2026-08-13, y desde ADR-019/ADR-020 **el orquestador
  lo dispara por HTTP** contra su propio servicio (`:8082`), igual que a los otros dos.
  En la figura, el módulo va con **línea continua** y flecha del orquestador hacia él,
  idéntica a las de medios y control.
- Interfaz de inspección **→** ambos servicios. **No hay flecha del bus a la interfaz de inspección**: esa ausencia comunica una frontera de diseño.
- Repositorio **→** Orquestador (consolidación y reporte).

**Nota al pie de la figura (esto sí va al informe):**

> *Nota.* La figura representa la disposición efectiva de procesos del prototipo, complementaria de la
> vista lógica de la Figura 4.1. Los dos planos se ejecutan como servicios independientes gobernados por
> configuración, y pueden disponerse en un mismo host o en hosts distintos sin modificar su lógica. El
> módulo de distribución se representa en línea punteada por corresponder a una capacidad especificada y no
> implementada dentro del alcance del prototipo.

✎ **2026-08-18 — REEMPLAZO de la nota al pie (la de arriba quedó falsa; usar esta):**

> *Nota.* La figura representa la disposición efectiva de procesos del prototipo, complementaria de la
> vista lógica de la Figura 4.1. Los tres módulos de la cadena se ejecutan como servicios independientes
> gobernados por configuración, y pueden disponerse en un mismo host o en hosts distintos sin modificar
> su lógica. El módulo de distribución admite dos modos de ejecución equivalentes en semántica: como
> proceso lanzado y supervisado por el orquestador experimental, o como servicio propio con interfaz
> de red; la selección es una decisión de despliegue, no de diseño.

---

# §5 — Diccionario de métricas (R-10 → §17.3.13)

> ## Definiciones operacionales de las métricas
>
> Las métricas del framework metodológico se instrumentan sobre las señales observables descritas en la
> sección anterior. Para que una medición sea reproducible e interpretable no basta con nombrarla: es
> necesario declarar **qué evento la inicia, qué evento la cierra, en qué unidad se expresa y bajo qué
> condiciones es aplicable**. La tabla siguiente cumple esa función.
>
> **Tabla 64**
> *Diccionario de métricas: definiciones operacionales*
>
> | Métrica | Inicio (t₀) | Cierre (t₁) | Unidad | Condición de aplicabilidad |
> |---|---|---|---|---|
> | **G2A** | Captura de la unidad visual | Fin de la inferencia | ms (p50/p95/p99) | Requiere reloj único. **No interpretable** cuando el trayecto atraviesa dos hosts (relojes monotónicos no comparables). Presupuesto declarado: 50–250 ms. |
> | **TTFD** | Inicio anotado del episodio | Primera detección positiva dentro del episodio | ms | Requiere referencia temporal anotada. Si no hay detección positiva en el episodio, se declara **nula con causa**, nunca cero. |
> | **t_alert-system** | Inicio anotado del episodio | Registro de la alerta interna | ms | Requiere referencia temporal anotada. |
> | **Latencia de alerta interna** | Primera evidencia perceptiva del episodio | Registro de la alerta interna | ms (p50/p95/p99) | Calculable sobre toda fuente temporal; **no requiere anotación**. |
> | **SDR** | — | — | proporción [0,1] | Fracción del episodio anotado cubierta por detección positiva continua. Requiere referencia temporal anotada. |
> | **Precisión / Exhaustividad / F1** | — | — | proporción | Evaluadas **a nivel de episodio**, no de frame. Las alertas sucesivas de un mismo episodio no se computan como falsos positivos. |
> | **t_alert-notification** | Registro de la alerta interna | Confirmación de entrega | ms | **No aplicable** si no hay canal de distribución habilitado. |
> | **t_capture→alert** *(derivada)* | Captura del frame que aporta la primera evidencia | Registro de la alerta interna | ms | Requiere reloj de pared en la fuente. **No interpretable** sobre fuentes de archivo (tiempo de medio). |
>
> Tres precisiones metodológicas acompañan a este diccionario.
>
> **Criterio de relojes.** Las latencias internas a un nodo se miden con un reloj monotónico local. Las
> latencias de extremo a extremo se miden **en un único reloj**. Cuando el trayecto atraviesa dos hosts,
> los relojes monotónicos respectivos **no son comparables entre sí** y su diferencia carece de
> significado; en esa situación la métrica se declara **no interpretable**, con su causa registrada, en
> lugar de publicar un valor. Esta regla es la razón por la cual la instrumentación de la topología de dos
> nodos reporta una ausencia declarada y no un número.
>
> **Una métrica derivada, declarada como tal.** La instrumentación incorpora la magnitud
> `t_capture→alert`, que mide el trayecto desde la captura del frame que aporta la primera evidencia hasta
> el registro de la alerta. **No forma parte del framework metodológico original** y se declara como
> instrumento auxiliar de este trabajo: su función no es sustituir a la métrica oficial de latencia de
> alerta, sino **descomponerla**, separando el tiempo que el sistema consume del tiempo que el sistema
> *espera por diseño* —la ventana de persistencia exigida por el patrón—.[^1]
>
> **El criterio de detección positiva no se reimplementa.** La evaluación de alertas contra la referencia
> anotada reutiliza el **mismo evaluador** que emplea el motor de patrones en tiempo de corrida, en lugar
> de redefinir qué constituye una detección positiva. Esta decisión elimina una fuente de error silencioso:
> la divergencia entre el criterio con el que el sistema decide y el criterio con el que el sistema es
> evaluado.
>
> [^1]: Descontando de `t_capture→alert` la persistencia efectivamente exigida se obtiene el tiempo de
> cómputo real del trayecto. Ambas magnitudes son auxiliares y se reportan junto a la métrica oficial,
> nunca en su lugar.

**Nota:** bajé deliberadamente el tono del pasaje de las métricas derivadas. En la v1 las presentaba como
"aporte instrumental propio" con una identidad algebraica — sonaba lindo y **te invitaba a que el tribunal
lo auditara**. El diccionario y el criterio de relojes son lo valioso; `t_compute-budget` va a nota al pie
y no se vende como contribución.

---

# §6 — Temporalidad de la fuente (R-11 → §17.3.14, subsección nueva)

> ## Naturaleza temporal de la fuente y aplicabilidad de la evaluación de patrones
>
> La distinción entre DBE y EBE se formula en términos del **origen** de la fuente visual. Existe, sin
> embargo, una segunda distinción, independiente de la anterior y con consecuencias directas sobre la
> interpretación de los resultados: la **naturaleza temporal** de la fuente.
>
> Una fuente de vídeo —un archivo o un flujo en vivo— produce unidades visuales **ordenadas en el tiempo**,
> sobre las cuales la noción de persistencia tiene sentido. Un conjunto de imágenes independientes, en
> cambio, produce unidades **sin relación temporal entre sí**: la persistencia de una condición no es una
> propiedad observable, porque no hay continuidad que observar.
>
> Esta diferencia genera un **modo de falla silencioso** que conviene documentar. Un conjunto de patrones
> configurado con una ventana de persistencia, evaluado sobre un conjunto de imágenes independientes,
> produce **cero alertas por construcción**: ningún episodio puede sostenerse porque no hay sucesión
> temporal que lo sostenga. El resultado —cero alertas— es **indistinguible** de la conclusión legítima "no
> hubo condiciones de riesgo en los datos". Se verificó empíricamente: sobre el conjunto de referencia, la
> evaluación registró **77 transiciones de patrón y ninguna alerta**.
>
> La plataforma **deriva la naturaleza temporal de la fuente** a partir del tipo de fuente declarado —no
> es un parámetro que el operador pueda contradecir— y, cuando la fuente no es temporal, declara la
> evaluación de patrones como **no aplicable, con su causa**, en lugar de reportar un cero interpretable
> como ausencia de riesgo. La corrida no se rechaza: conserva su valor como verificación del contrato entre
> planos y como diagnóstico de la asociación espacial, pero **sus alertas no se interpretan como una
> medición de persistencia**.
>
> En términos del framework de evaluación, esto significa que **cada tipo de fuente sostiene un tipo
> distinto de afirmación**: los conjuntos de imágenes permiten medir percepción y asociación espacial; los
> clips de vídeo con anotación temporal permiten medir patrones, latencia de alerta y continuidad; las
> fuentes en vivo permiten, además, medir el comportamiento de extremo a extremo bajo condiciones de
> transmisión continua. Confundir estos regímenes no produce un error visible, sino un número correctamente
> calculado sobre una pregunta equivocada — que es precisamente el tipo de error que la política de
> aplicabilidad de métricas (§17.3.13.3) fue diseñada para impedir.

---

# §7 — Verificación: qué funciona y cómo se midió (R-12 → sección nueva)

**Nota — leé esto antes de copiar.** La v1 de esta tabla tenía tres problemas que la auditoría encontró y
que en una defensa hubieran sido letales: (a) atribuía cifras a la corrida equivocada; (b) presentaba como
"dentro de presupuesto" una latencia medida **con detector simulado**, cuando el detector real está diez
veces por encima; y (c) llamaba "métricas" a lo que es una verificación de instrumento sobre **un solo
clip con dos alertas**. La v2 dice la verdad — y la verdad, contada así, **es más fuerte**.

> ## Verificación del diseño sobre el sistema implementado
>
> El criterio de cierre adoptado (§17.3.17) establece que una unidad se considera completa **cuando produce
> evidencia verificable dentro de una corrida experimental**. Esta sección presenta esa evidencia. Todas
> las mediciones proceden de corridas ejecutadas sobre la plataforma implementada, con sus artefactos
> conservados y reproducibles. Se indica en cada caso el detector utilizado, dado que la naturaleza del
> detector condiciona la interpretación de las latencias.
>
> **Tabla 65**
> *Evidencia de verificación del núcleo validable*
>
> | Propiedad verificada | Condiciones | Resultado |
> |---|---|---|
> | El pipeline de percepción opera sobre vídeo real de obra | Clip de 733 unidades, detector open-vocabulary en GPU | **0 fallos**, 15.914 detecciones, latencia de inferencia p50 220 ms / p95 267 ms, 4,39 fps efectivos |
> | El repositorio y el canal transportan lo mismo | Corrida en vivo por bus, releída de forma offline (detector de referencia) | Artefactos **idénticos**; ninguna unidad perdida |
> | La cadena completa cierra en vivo | Corrida en vivo de 300 unidades (detector de referencia) | 300/300 unidades, **0 pérdidas**, dos alertas registradas, cierre por evento de fin de corrida |
> | Las ventanas temporales operan según su configuración | Corrida sobre vídeo con persistencia declarada | CR-01 confirma en **t = 4000 ms**; CR-02 en **t = 7000 ms** (valores configurados) |
> | La granularidad de escena no degrada la evaluación | Comparación de granularidades sobre el mismo corpus | **F1 = 1,0** en ambas; invariante de conteo de sujetos verificada |
> | La instrumentación de latencia **detecta el incumplimiento** | Presupuesto declarado 50–250 ms | Con detector de referencia: p95 = **31,8 ms** (dentro). Con el detector open-vocabulary evaluado: p95 = **2604 ms**, y el sistema lo **declara fuera de presupuesto** |
> | La cadena completa computa las cinco métricas del framework sobre referencia temporal anotada | **Verificación de instrumento**: 1 clip de obra real, GT preliminar, 2 alertas observadas | Precisión 0,50 · Exhaustividad 1,00 · F1 0,67 · t_alert-system 4000 ms · TTFD 0 ms · SDR 0,999 |
>
> Tres comentarios acompañan a esta tabla, y son parte del resultado.
>
> **La instrumentación se cumple; el detector no.** La medición de latencia captura-a-resultado opera
> correctamente y compara contra el presupuesto declarado. Con el detector open-vocabulary evaluado, ese
> presupuesto **no se cumple**, y el sistema lo señala. Este resultado es consistente con la evaluación
> comparativa de modelos: los detectores capaces de sostener CR-01 no siguen el ritmo de una cámara, y los
> que lo siguen no sostienen CR-01. **La restricción operativa está en el detector, no en la plataforma**, y
> el instrumento sirve precisamente para localizarla. Un instrumento que sólo devolviera resultados
> favorables no sería un instrumento.
>
> **La verificación de instrumento no es un resultado experimental.** Las cinco métricas de la última fila
> se computaron sobre **un solo clip**, con una anotación de referencia **preliminar** —revisión visual
> asistida, pendiente de validación humana definitiva— y sobre **dos alertas observadas**. Demuestran que
> la cadena de medición está completa y es correcta; **no** constituyen una medición del desempeño del
> sistema, que requiere el banco completo de clips anotados. Se reportan aquí como cierre del diseño, no
> como resultado.
>
> **El falso positivo es información.** La única alerta no esperada corresponde a una condición CR-02
> emitida cuando el detector pierde transitoriamente el elemento de protección de un trabajador que sí lo
> porta. No es un defecto de la plataforma ni un error de la evaluación: es exactamente el tipo de
> comportamiento que el instrumento fue construido para **medir**.

---

# §8 — Registro del alcance efectivo y brechas (R-13 → sección nueva)

**Nota:** ✎ **actualizada el 2026-08-12** contra los resultados cerrados y
`operacion/114`. La versión inicial mezclaba capacidades aún no ejercidas con exclusiones;
varias se implementaron después. Esta tabla registra el estado final sin borrar esa
cronología.

> 🔴 **✎ 2026-08-22 — ESTA TABLA YA FUE INTEGRADA Y QUEDÓ SUPERADA COMO TEXTO GUÍA.** El
> `.docx` v1.2 la materializó como la **Tabla 68 de §17.4.10**, y sobre esa tabla mandan las
> unidades del **pase 3**: la **enmienda a E4-22** (fila de preselección en el borde:
> implementada y medida, excluida de lo evaluativo — NO "no ejercida") y **E4-27** (fila de
> ajuste fino: jornada COMPLETA, escalera de tres tramos cerrada, sin marcador pendiente).
> No pegar desde acá: usar el texto base `90b` + pases 2 y 3. Las dos filas de abajo que
> quedaron vencidas se reescribieron el 2026-08-22 sólo para que este material no vuelva a
> introducir una afirmación falsa (hallazgos §3.1 de la revisión de cierre).

> ## Alcance efectivo: capacidades no ejercidas
>
> El diseño distingue desde su formulación entre el **núcleo validable** y las **extensiones
> condicionadas**. Cerrado el ciclo de implementación, corresponde declarar con precisión qué capacidades
> fueron efectivamente ejercidas y cuáles permanecen especificadas sin materializar. Esta declaración no
> constituye una enumeración de faltantes, sino el registro del alcance conforme a las reglas de exclusión
> establecidas **con anterioridad a la obtención de resultados**.
>
> **Tabla 66**
> *Capacidades ejercidas, exclusiones y brechas de integración*
>
> | Capacidad | Estado | Consecuencia declarada |
> |---|---|---|
> | **Identidad persistente de sujeto** | **Implementada y medida** como decorador de fuente del control-plane; el media-plane no la persiste en su JSONL | G1 se reporta como capacidad medida; el núcleo validable conserva G0. Las métricas MOT continúan excluidas. |
> | **Comparación de estrategias de detección** (directa, indirecta, híbrida) | **Implementada y evaluada** | E-IND queda como núcleo; E-DIR fue vetada por precisión y E-HYB-or fue ejecutada y refutada. Las cifras pertenecen a §17.5, no a esta sección de diseño. |
> | **Distribución de alertas** (canal de notificación) | **Implementada, verificada e integrada** | DBE/EBE, cooldown, idempotencia, MQTT QoS 1 y reporte fueron verificados; la vista de webconsole y la orquestación quedaron integradas y el repositorio está versionado (✎ 2026-08-22 — antes decía que quedaban pendientes). Canales adicionales y un tablero operativo propio siguen fuera del alcance. |
> | **Latencia captura-a-resultado en topología de dos nodos** | Instrumentada; **no computable** | Los relojes monotónicos de hosts distintos no son comparables: la métrica se declara **no interpretable**, con causa, en lugar de publicarse. |
> | **Comparación con modelo adaptado** (ajuste fino) | **Jornada experimental COMPLETA (✎ 2026-08-22; antes esta fila decía que restaba el RUN): escalera de tres tramos cerrada** — T1 NO-GO (doc 123) · T2 NO-GO (doc 127) · T3 cerrado con causa técnica (doc 117 §2) | La curva de capacidad de tres puntos es el valor declarado del tramo. T1 (10 épocas): rescata `bare_head` de 0,0000 a 0,0455 pero queda a 0,0045 del umbral de ganancia y rompe la retención de `person` (−11,62 %, tope 10 %). T2 (D-FT-16, SGD lr0=0,01): la ganancia PASA (`bare_head` 0 → 0,0909) pero la retención in-domain FALLA ×4 (person −49,7 %) y la open-vocabulary FALLA (COCO −71,3 %); colapsó en entrenamiento (early stop 16/60, mejor época = 1). **F-127.1: el fallo es ESTRUCTURAL (2.946 imgs vs 10,35M parámetros), no de capacidad.** Márgenes y expectativas pre-registrados antes de cada evaluación; las 3 expectativas se confirmaron; ningún checkpoint se adoptó. Trampa de cita: T1 gana por recall CR-01, T2 por AP — no hay una métrica única. Nunca "por tiempo" (ADR-017). |
> | **Métricas de seguimiento multiobjeto** | **No aplicables** | No se dispone de anotación de identidades; su cómputo carecería de referencia. Caso ejemplar de la política de aplicabilidad. |
> | **Condiciones de riesgo de nivel 2 y 3** | Especificadas, no implementadas | Excluidas conforme al núcleo validable declarado. Se conservan la definición de sus patrones y su vocabulario. |
> | **Comparación DBE / EBE sobre fuente idéntica** | Paridad de transporte y de reparto **VERIFICADA** | Replay/live producen artefactos de distribución idénticos. El anclaje de sincronización entre reloj de captura y tiempo de media para EBE-desde-clip sigue **NO implementado** (`operacion/97`): la paridad plena queda acotada a lo verificado. |
>
> Se registran, además, dos limitaciones conocidas del procedimiento de evaluación. Primera: el
> emparejamiento entre alertas observadas y episodios anotados se resuelve de forma voraz, lo cual puede
> subestimar la exhaustividad en escenarios con múltiples episodios simultáneos de una misma condición y
> ventanas solapadas; la solución correcta —emparejamiento bipartito óptimo— está identificada y su efecto
> se acota a los escenarios de ese tipo. Segunda: el GT temporal vigente es humano y está
> congelado, pero no tuvo una segunda anotación independiente ni estadístico de acuerdo;
> esa limitación se declara como L2.

---

# §9 — Extensibilidad medida (R-26 → §17.3.17 / §17.3.18)

**Nota:** esta sección **no estaba** en la v1 y es, probablemente, la más valiosa de todas para tu defensa.
Tu tesis no es "OVD detecta mejor" — es **"qué se logra con condiciones en lenguaje, sin entrenar"**. Todo
lo demás del capítulo mide latencias y pérdidas: **esto mide lo único que un detector cerrado no puede
hacer.** El mini-experimento A1 se ejecutó y verificó: acá queda el mecanismo y su costo
de cambio; la cifra medida corresponde a §17.4/§17.5 por no-anacronismo.

> ## Extensibilidad de la plataforma: costo de incorporar una condición nueva
>
> Una arquitectura orientada a la detección open-vocabulary sólo resulta justificada si la incorporación de
> una condición de riesgo nueva es efectivamente más barata que en una arquitectura de vocabulario cerrado.
> Esa afirmación no debe postularse: debe **medirse**. La tabla siguiente declara el costo real de cada
> tipo de extensión sobre el sistema implementado.
>
> **Tabla 67**
> *Costo de extensión de la plataforma*
>
> | Extensión | Qué requiere | Costo |
> |---|---|---|
> | Una **condición nueva del mismo tipo** (sujeto sin elemento de protección) | Una entrada declarativa en el conjunto de patrones —clase del sujeto, clase ausente, región, umbrales, ventana temporal— y las formulaciones de prompt correspondientes | **Sólo configuración. Sin reentrenamiento y sin código.** |
> | Una **familia nueva de condiciones** (relacional, zonal, de trayectoria) | Un evaluador nuevo en el motor de patrones | Código acotado al evaluador; el resto de la cadena no se modifica |
> | Un **modelo de detección nuevo** | Un adaptador que normalice su salida al contrato de evidencia perceptiva | Código acotado al adaptador |
> | Una **fuente visual nueva** | Un adaptador de ingesta que produzca unidades visuales normalizadas | Código acotado al adaptador |
> | Un **canal de notificación nuevo** | Un consumidor del contrato de alerta | Externo a los dos planos |
>
> El contraste entre la primera y la segunda fila delimita, con precisión, **la frontera real de la
> extensibilidad por lenguaje**: una condición expresable como ausencia de un elemento observable sobre un
> sujeto observable se incorpora por configuración; una condición que requiere una relación nueva entre
> entidades requiere un evaluador. Declarar esa frontera —en lugar de afirmar genéricamente que "todo es
> configurable"— es la contribución arquitectónica que este trabajo sostiene.

---

## Fuente: `docs/informe/ajustes/07-critica-extension-y-poda.md`

> SHA-256 del bloque: `9f37e8d3d7031027be13b5d20c87e7398ca89598351c05fcae0d977aff6e099e`  
> Seleccion: podas 15 y 16 aplicables a la seccion 17.3.

## 6. §17.3 Diseño arquitectónico (24.389 palabras)

**Acá opera el `93` (26 redlines), no esta crítica** — podar §17.3 por extensión
mientras se le aplican redlines de corrección es operar dos veces el mismo texto. Solo
dos ítems son de pura longitud:

### PODA-15 · §17.3.15 Roles CPN/EN/TN (1.319) · C1 parcial · 🟡
**R-17 ya pide** convertir esto en tabla rol→contenedor. El TN (nodo de entrenamiento)
aún no se materializó — lo ejerce la jornada de fine-tuning comprometida (E-04,
ADR-017), y su estado se declara a la entrega. Al aplicar R-17, dejar la tabla + ~300
palabras, no la prosa completa. **Ahorro: ~700** · DECISIÓN → [ ]

### PODA-16 · §17.3.17 Backlog (1.101) · C5 · 🟡
**R-21 ya reescribe** el estado de los 16 ítems. Al aplicarlo, comprimir las Tablas
58/59 al estado final con referencia, sin la prosa de justificación ítem por ítem.
**Ahorro: ~500** · DECISIÓN → [ ]

---

