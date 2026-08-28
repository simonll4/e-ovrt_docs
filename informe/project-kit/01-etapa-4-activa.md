# E-OVRT-VDP - paquete de etapa 4

> Generado el 2026-08-28. Etapa 4: seccion 17.4, implementacion del prototipo.

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

- **Etapa activa:** 4 - Etapa 4: seccion 17.4, implementacion del prototipo.
- Este archivo contiene el texto vigente que se modifica y sus insumos de ajuste.
- No se trasladan resultados propios hacia secciones cronologicamente anteriores.
- Nombre propio de esta etapa (01-etapa-4-activa.md): regenerarla no pisa el paquete de ninguna otra etapa.

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

## Fuente: `docs/informe/entregable/96e-informe-v11-cierre-anexos-referencias.md`

> SHA-256 del bloque: `6b1d8f4b631dc608b001d500a4eea6e9e439d42022a38bf05f984a963eb921a6`  
> Seleccion: placeholder vigente de la seccion 17.4.

### 17.4. Implementación del prototipo experimental

[Agregado futuro correspondiente a la Etapa 4]

---

## Fuente: `docs/informe/ajustes/04-etapa-4-implementacion.md`

> SHA-256 del bloque: `2e14a84aa8aa60447b25f27514e0a69f70a21bc277b4e70b1604c7296b7cca96`  
> Seleccion: documento completo.

# Etapa 4 — §17.4 Implementación del prototipo experimental

> ✅ **Estado (✎ 2026-08-23): la sección está REDACTADA y sus tres pases de corrección
> están APLICADOS Y VERIFICADOS** — documento de trabajo `§17.4 v1.5` (✎ 2026-08-28: vigente **v1.6**, `00-el-informe-hoy`) en
> `entregable/desarrollando/`, texto base extraído en `entregable/90b-etapa4-texto-extraido.md`.
> Lo que queda: revisión del autor, las URLs del lote (C1) y la integración al maestro. Las
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

---

## Fuente: `docs/informe/entregable/90b-etapa4-texto-extraido.md`

> SHA-256 del bloque: `eb527c3a4d6bf7615d0852e23304e0ce5f9d3a4f12634c49451d644daf6b80da`  
> Seleccion: TEXTO BASE VIGENTE de la seccion 17.4: extraido del documento de trabajo v1.6 (re-extraido 2026-08-28), con los tres pases YA aplicados y verificados. Es el texto sobre el que se revisa y se sigue trabajando. Pendiente detectado por operacion/130 R-01: su parrafo sobre el orden de disparo con distribucion debe decir control -> distribucion -> medios.

# 90b — Texto extraído del documento de trabajo: §17.4 Implementación (v1.6)

> **Extracción derivada (2026-08-28)** del `.docx`
> `informe/entregable/E-OVRT-VDP_Seccion_17.4_Implementacion_v1.6.docx`, **solo para búsqueda y cita**
> (mismo estatuto que el doc 90): al editar, se edita el `.docx`/Google Docs, nunca
> este archivo. Tablas y figuras pueden haber perdido formato; las figuras no se
> extraen y las ecuaciones no se convierten — quedan `⟦FIGURA: no extraída — ver el .docx⟧` y
> `⟦ECUACIÓN: no extraída — ver el .docx⟧` donde estaban. Regenerado con
> `herramientas/extraer_informe.py` (regla D-C del manual de aplicación).

---

### 17.4. Implementación del prototipo experimental

La presente sección documenta la materialización del diseño arquitectónico desarrollado en la sección 17.3. Su propósito es establecer qué componentes fueron construidos, cómo se concretaron los contratos e interfaces previstos, qué mecanismos de acople y persistencia se implementaron y mediante qué evidencia se verificó el funcionamiento técnico del prototipo experimental.

La descripción se concentra en la implementación y en su verificabilidad. Los resultados comparativos de desempeño del detector, del motor temporal y de la plataforma completa se presentan en la sección 17.5, donde se declaran las combinaciones experimentales, los materiales, los denominadores y las limitaciones de cada medición. Esta separación evita confundir la existencia de una capacidad con su rendimiento cuantitativo.

#### 17.4.1. Componentes construidos y cadena de datos

El prototipo se materializó en tres componentes de plataforma, un módulo funcional de distribución y una cadena de datos externa a la plataforma que produce los insumos experimentales.

El plano de medios implementa el pipeline de inferencia open-vocabulary. Se ejecuta como un servicio gobernado por configuración, carga el modelo una única vez al iniciar y expone una interfaz HTTP para disparar una corrida por vez. El plano de control implementa el motor de patrones de riesgo que consume evidencia de percepción, mantiene estado temporal y registra alertas internas. También se ejecuta como servicio HTTP. El soporte experimental no constituye un plano de ejecución: reúne los catálogos de prompts y experimentos, el runner u orquestador reproducible, la consolidación de artefactos y la webconsole con su backend intermediario.

El módulo de distribución de alertas constituye un cuarto componente funcional y no un tercer plano. Al igual que los dos planos, se ejecuta como un servicio gobernado por configuración con interfaz HTTP propia. Consume las alertas confirmadas desde el bus de alertas, aplica la política de notificación, controla idempotencia y supresión, entrega por MQTT con confirmación de calidad de servicio y conserva un registro de entregas de sólo adición (ledger). La vista de resultados de entrega y el lanzamiento desde la orquestación quedaron integrados.

La **cadena de datos** comprende adquisición, validación, conversión y congelamiento de datasets y bancos de evaluación. Para el banco temporal de video esa cadena comprende la adquisición y curación del material, la preparación y segmentación temporal de los clips, la anotación asistida con revisión humana y la derivación, validación y congelamiento de la referencia; su construcción se documenta en la sección 17.4.8. Alimenta a la plataforma, pero no forma parte de su cadena operativa: su función es producir material reproducible y con procedencia para entrenamiento, selección y evaluación.

**Figura 4.7**

*Vista de procesos y patrones de acople de la plataforma experimental*

⟦FIGURA: no extraída — ver el .docx⟧

*Nota.* La figura representa la materialización efectiva de los dos patrones de acople de la plataforma experimental. El gobierno de las corridas se realiza mediante interfaces HTTP en el plano de medios (:8080), el plano de control (:8081) y el módulo de distribución (:8082), con el runner y la webconsole como clientes de los tres servicios. El flujo de datos se desacopla mediante buses ZeroMQ de patrón publicador-suscriptor con serialización msgpack: eventos de percepción desde medios hacia control (:5557) y alertas confirmadas desde control hacia distribución (:5558). El repositorio por ejecución experimental conserva los artefactos persistentes y el orden live inicia el control, confirma la suscripción y recién entonces habilita los medios.

#### 17.4.2. Correspondencia entre el diseño y los artefactos implementados

Los contratos preliminares definidos durante el diseño se materializaron como modelos de datos, configuraciones versionadas, esquemas serializables, servicios ejecutables y artefactos persistentes. La Tabla 56 establece la correspondencia entre cada denominación conceptual y su realización efectiva.

**Tabla 56**

*Correspondencia entre los contratos del diseño y su materialización efectiva*

| **Contrato del diseño** | **Materialización efectiva** | **Versionado y trazabilidad** | **Componente** |
| --- | --- | --- | --- |
| RunConfig | Manifiesto de experimento y configuraciones efectivas por plano | experiment.manifest.v1 | Soporte experimental |
| SourceDefinition | Sección de fuente de la configuración y registro de adaptadores de ingesta | Esquema de configuración; congelado por el manifiesto | Plano de medios |
| ModelProfile | Catálogo de perfiles de modelo, con un archivo por variante | Catálogo versionado; un archivo por variante | Plano de medios |
| PromptDefinition | Conjunto de prompts versionado e identificado en cada corrida | prompt_set_id registrado en cada corrida | Soporte experimental |
| FrameMetadata | Unidad visual y unidad preparada internas, y bloque de fuente del evento publicado | Contrato interno; viaja dentro del evento publicado | Plano de medios |
| PerceptionEvent | Evento de percepción normalizado | media.detection.v1 | Plano de medios |
| PatternDefinition | Definición declarativa dentro del conjunto de patrones | Conjunto de patrones versionado (pattern set) | Plano de control |
| PatternStateChanged | Evento de transición del patrón | control.pattern_state.v1 | Plano de control |
| AlertEvent | Alerta interna con identificador determinista e idempotente | control.alert.v1 | Plano de control |
| MetricSample | Muestras de métricas de medios y control | media.metric.v2 / control.metric.v1 | Ambos planos |
| ErrorEvent | Registro de errores y anomalías por corrida | Esquema por componente, registrado por corrida | Ambos planos |
| Bus interno de eventos | Publicación ZeroMQ con envoltorio versionado | bus.envelope.v1 | Frontera entre planos |
| Cierre de corrida | Evento de finalización publicado al cerrar la corrida | run.lifecycle.v1 (evento run_finished) | Plano de medios |
| Repositorio de eventos | Archivos JSONL de sólo adición por corrida | Esquemas de cada evento persistido | Ambos planos |
| Referencia temporal | Anotación humana de episodios por clip | clip_gt.v2 | Soporte experimental |
| Reporte experimental | Reporte consolidado report.json y por experimento | Proyección regenerable de los artefactos primarios | Soporte experimental |
| Alerta distribuida | NotificationEnvelope y DeliveryRecord | control.notification.v1 / control.delivery.v1 | Módulo de distribución |

**Nota.** La tabla documenta la correspondencia semántica entre el diseño y la implementación. El versionado se materializa mediante esquemas explícitos, catálogos, conjuntos de configuración y artefactos congelados por el manifiesto de cada ejecución experimental.

La correspondencia permite verificar que la implementación no sustituyó silenciosamente las fronteras arquitectónicas. El plano de medios continúa produciendo evidencia perceptiva, el plano de control conserva la interpretación temporal y la alerta interna, el soporte experimental gobierna y consolida corridas, y la distribución opera como tramo posterior desacoplado.

#### 17.4.3. Contratos de datos materializados

Cinco contratos concentran los hechos principales de la ejecución: el evento de percepción, el envoltorio del bus, el contrato de ciclo de vida, el evento de transición de patrón y la alerta interna. Los cinco están declarados con su identificador en la tabla anterior; lo que sigue precisa cómo se materializan, qué lleva cada uno y qué propiedad técnica habilita.

La materialización no es una denominación conceptual. Cada contrato es una clase de modelo declarada en el módulo de contratos de su componente, con tipos y campos obligatorios explícitos, validada en la frontera de entrada, persistida como un objeto JSON por línea en los artefactos de sólo adición —omitiendo los campos sin valor— y transportada por el bus dentro de un envoltorio serializado en formato binario compacto. Dentro del plano de medios la evidencia atraviesa además una cadena interna de contratos antes de publicarse: la unidad visual normaliza la lectura de la fuente, la unidad preparada transporta los píxeles junto con la transformación espacial que permite volver del espacio del modelo al de la imagen original, la detección cruda recoge la salida del adaptador y la detección normalizada es la que finalmente se persiste. Esa cadena es la que hace que la reproyección de coordenadas sea una operación declarada y no un ajuste disperso en el código.

El evento de percepción, DetectionEvent, normaliza la salida del detector. Identifica la corrida y la unidad visual, y agrupa en bloques estructurados la fuente, el perfil de modelo, el conjunto de prompts efectivo, las detecciones y los tiempos medidos por unidad. Cada detección lleva su etiqueta, el identificador del prompt que la originó, el puntaje, la caja en píxeles y su equivalente normalizado. Esa composición es la que permite que una detección se atribuya después a una variable concreta de la corrida y no a una combinación desconocida. La forma efectiva del evento, tal como se persiste, es la siguiente:

{   "schema_version": "media.detection.v1",   "event_type": "detection_event",   "run_id": "run_20260805_033712_dbe_grounding_dino_53cb6f",   "unit_id": "frame_000000",   "source":  { "source_id": "a_p1_c02", "source_type": "video_frame",                "frame_index": 0, "timestamp_ms": 0.0,                "width": 1920, "height": 1080 },   "model":   { "name": "grounding_dino",                "model_id": "IDEA-Research/grounding-dino-tiny",                "device": "cuda" },   "prompts": { "prompt_set_id": "cr01_cr02_v2_short" },   "detections": [     { "detection_id": "det_000001", "label": "person", "prompt_id": "person",       "confidence": 0.8784,       "bbox_xyxy": [1027.3, 105.5, 1340.8, 1083.9],       "bbox_norm_xyxy": [0.5351, 0.0977, 0.6983, 1.0],       "area_px": 306732.1, "model_name": "grounding_dino" },     { "detection_id": "det_000002", "label": "helmet", "prompt_id": "helmet",       "confidence": 0.8387,       "bbox_xyxy": [1098.1, 106.5, 1255.8, 217.3],       "bbox_norm_xyxy": [0.5719, 0.0986, 0.6541, 0.2012],       "area_px": 17475.1, "model_name": "grounding_dino" }   ],   "timing": { "normalize_ms": 11.53, "inference_ms": 445.76,               "postprocess_ms": 0.11, "write_ms": 0.0, "total_ms": 445.88 } }

El envoltorio del bus no reempaqueta ese contenido: transporta como carga la misma cadena que se escribió en el artefacto —la persistencia ocurre primero y la publicación después— y le agrega cuatro campos propios del transporte: el tópico, la clave de particionado, un número de secuencia monótono por publicador y el instante de publicación en reloj de pared, que es el que el módulo de distribución conserva luego como marca de confirmación. El número de secuencia se consume incluso cuando el envío se descarta por saturación del canal, de modo que la pérdida se vuelva observable como un hueco del lado del consumidor en lugar de pasar por ausencia de evidencia. El contrato de ciclo de vida, por su parte, no delimita el inicio de la corrida —eso lo establece la respuesta afirmativa de la operación de creación en el servicio— sino su cierre: publica un único evento de finalización con el identificador de corrida y su estado, de modo que el final lógico se distinga de una interrupción y los consumidores puedan cerrarse y consolidar sus artefactos. Ambos contratos se emplean sin variantes en los dos buses de la plataforma, el de detecciones y el de alertas: el publicador de alertas del plano de control es un espejo deliberado del publicador de medios, con el mismo envoltorio y las mismas garantías.

El evento de transición, PatternStateChanged, registra los cambios entre los estados del patrón —los mismos que fija la máquina de estados del diseño— junto con la evidencia y los hitos temporales que los motivaron, e incorpora el instante y la unidad de la primera evidencia positiva del episodio, que es el punto de partida de la medición de latencia. Un contrato hermano registra el progreso parcial mientras la condición está en curso y no ha sido confirmada todavía.

La alerta interna, AlertEvent, registra la confirmación del episodio. Su identificador no es un valor aleatorio: se deriva como un identificador único universal de versión 5 —un resumen determinista— sobre la cadena que concatena el identificador de corrida de control, el de corrida de medios, la unidad, el patrón y la clave de sujeto, donde esa clave adopta la forma CR-01:a_p1_c08 cuando el patrón opera con granularidad de escena y CR-01:a_p1_c08:subject_001 cuando opera con identidad de sujeto. La identidad de la alerta es entonces una función pura de esa quíntupla, con tres consecuencias verificables. Primero, reprocesar la misma evidencia bajo el mismo identificador de corrida de control reproduce exactamente los mismos identificadores de alerta. Segundo, la deduplicación no requiere estado compartido entre componentes: el módulo de distribución construye su clave de idempotencia como un resumen criptográfico del identificador de alerta y la asienta en un registro de sólo agregado, sin consultar al plano de control. Tercero, la identidad se asigna por confirmación y no por episodio, de modo que una confirmación posterior sobre el mismo sujeto recibe identidad propia; esto es coherente con la decisión de no suprimir dentro del motor (DA-13) y evita que el mecanismo de idempotencia oculte reincidencias reales. La alerta conserva además evidencia auditable: sujeto observado, detecciones de soporte, clase de protección ausente, región evaluada, puntaje y justificación legible. Por eso la ausencia no se presenta como una afirmación opaca del detector, sino como una inferencia del plano de control reconstruible sobre evidencia positiva.

Los contratos se diseñaron para admitir información que la implementación actual no produce, y esa capacidad fue ejercida antes de declararse. La detección normalizada incluye hoy un campo de identidad de sujeto entre fotogramas que ningún productor emite:

class Detection(BaseModel):          # media.detection.v1     detection_id:   str | None = None     track_id:       str | None = None   # identidad entre fotogramas; hoy sin productor     label:          str     prompt_id:      str | None = None     confidence:     float     bbox_xyxy:      list[float]         # píxeles [x1, y1, x2, y2]     bbox_norm_xyxy: list[float]         # normalizado [0, 1]     area_px:        float | None = None     model_name:     str | None = None

El campo se declara como opcional con valor por defecto, se omite al serializar cuando no tiene valor —de modo que su presencia en el contrato no altera un solo byte de los artefactos existentes— y, sin embargo, el plano de control ya lo consume como clave de estado cuando opera con granularidad por sujeto. El contrato conservó su versión: la extensión no exigió un cambio incompatible ni la coordinación de un despliegue conjunto. Tres decisiones de implementación sostienen esa propiedad. Los campos nuevos se agregan como opcionales con valor por defecto; los consumidores validan contra su propia declaración del contrato y descartan sin error los campos que no conocen, en lugar de rechazar el mensaje; y la frontera de la distribución declara explícitamente que admite campos adicionales. El plano de control mantiene por eso su propia declaración espejo del evento de percepción, no una biblioteca compartida con el plano de medios: la frontera entre planos es el esquema serializado y no una dependencia de código, lo que permite versionarlos y desplegarlos por separado. Éste es el mecanismo por el cual velocidad, dirección, pose, segmentación o detecciones asociadas podrían incorporarse a la evidencia perceptiva; su costo se detalla en la sección 17.4.11, donde también se declara que hoy no están implementadas.

#### 17.4.4. Interfaces de servicio y gobierno por configuración

Los dos planos se implementaron como servicios independientes gobernados por configuración y expuestos mediante HTTP. Esta concreción permite disponerlos en un mismo host o en hosts distintos sin modificar su lógica y habilita que el soporte experimental orqueste corridas de manera reproducible. Rutas, fuentes, umbrales, ventanas temporales y opciones de instrumentación se declaran en configuración; cada corrida persiste la configuración efectiva utilizada.

**Tabla 57**

*Interfaces principales de los servicios de la plataforma*

| **Servicio** | **Operación** | **Función** |
| --- | --- | --- |
| Plano de medios (:8080) | GET /api/model | Expone el perfil de modelo, dispositivo y umbrales efectivos. |
| Plano de medios (:8080) | POST /api/runs | Dispara una corrida con fuente, prompts, parámetros, configuración de bus e identificador de experimento. |
| Plano de medios (:8080) | POST /api/runs/{id}/stop | Detiene cooperativamente la corrida en curso; el cierre se propaga a los consumidores por el bus. |
| Plano de medios (:8080) | GET /api/runs/{id} | Consulta estado y resumen de la corrida. |
| Plano de medios (:8080) | GET /api/runs/{id}/detections | Recupera evidencia perceptiva paginada. |
| Plano de medios (:8080) | POST /api/runs/{id}/evaluate | Ejecuta la evaluación de percepción cuando existe referencia aplicable. |
| Plano de control (:8081) | POST /api/runs | Dispara una corrida en modo replay o live. |
| Plano de control (:8081) | GET /api/runs/{id}/alerts | Recupera las alertas internas registradas. |
| Plano de control (:8081) | GET /api/config | Expone la configuración efectiva de control. |
| Módulo de distribución (:8082) | POST /api/runs | Inicia una corrida de entrega con fuente de alertas, política, canal e identificador de experimento. |
| Módulo de distribución (:8082) | GET /api/runs/{id} | Consulta estado y conteos de entrega; determina cuándo consolidar artefactos. |
| Módulo de distribución (:8082) | POST /api/runs/{id}/cancel | Detiene cooperativamente una corrida de entrega en curso. |
| Módulo de distribución (:8082) | GET /api/config | Expone la configuración efectiva de distribución. |
|  | Bus ZeroMQ publicador-suscriptor (msgpack) | Transporta los eventos de percepción y el ciclo de vida de la corrida dentro del envoltorio versionado del bus. |
|  | Bus ZeroMQ publicador-suscriptor (msgpack) | Transporta las alertas internas confirmadas hacia el módulo de distribución. |
| Runner y webconsole | Clientes HTTP de los tres servicios | Gobiernan corridas y consolidan artefactos; no consumen los buses de datos. |

*Nota.* La tabla resume las operaciones de gobierno principales; no es un inventario exhaustivo (listados, corrida actual, artefactos por corrida, comprobaciones de salud y limpieza del registro se omiten). La detención figura únicamente donde el servicio la expone: el plano de control no ofrece detención de una corrida en curso, y esa asimetría es deliberada (ver el texto).

El modelo no se transmite en la solicitud de corrida. Se carga una sola vez al iniciar el servicio de medios; por ello, comparar perfiles de modelo implica disponer procesos con perfiles distintos y no reconfigurar pesos dentro de una corrida. Esta decisión mantiene el costo de carga fuera de la ruta crítica y evita estados ambiguos del servicio.

Los tres servicios implementan el mismo contrato de gobierno: admiten una corrida activa por vez y rechazan solicitudes concurrentes señalando la corrida en curso; cada corrida declara su configuración al crearse y el servicio persiste la configuración efectiva utilizada. Las operaciones de consulta de configuración y de perfil de modelo permiten verificar, antes de disparar, que el servicio cargó lo que el experimento requiere: sin ellas, una discrepancia entre lo configurado y lo desplegado sólo se descubriría en los resultados.

En una corrida en vivo, la respuesta afirmativa de cada consumidor del bus implica que su suscripción ya está establecida: la del plano de control sobre el canal de detecciones y la del módulo de distribución sobre el canal de alertas. De esa garantía se deriva el orden de disparo, inverso al flujo de datos: primero la distribución, después el control, por último el plano de medios. Un consumidor suscripto tarde perdería los eventos ya publicados sin ningún error observable; el orden de disparo excluye esa pérdida por construcción.

La detención de corridas es cooperativa en los dos servicios que la exponen: la solicitud marca la corrida y el hilo de ejecución la observa entre unidades, sin cortes abruptos que dejarían artefactos a medio escribir. El plano de control no expone detención, y la asimetría es deliberada: su corrida en vivo se cierra con el evento de finalización que publica el plano de medios —la relación entre ambas corridas es uno a uno—, de modo que la intervención del operador se ejerce aguas arriba y el cierre llega por el mismo canal que los datos. El módulo de distribución, en cambio, requiere cancelación propia: una corrida de entrega puede permanecer a la espera de alertas y debe poder abortarse sin reiniciar el servicio.

#### 17.4.5. Patrones de acople y caminos experimentales

La implementación distingue dos patrones técnicos de acople y dos caminos experimentales. Los patrones describen cómo se coordinan los componentes; los caminos DBE y EBE describen cómo circula la evidencia entre los planos según la naturaleza de la ejecución. Mantener ambas clasificaciones separadas evita reducir la plataforma a una dicotomía incompleta.

En el camino **DBE** el acople entre planos se realiza por archivo. El plano de medios persiste detections.jsonl y el plano de control lo relee. El repositorio de corrida constituye la fuente de verdad y permite repetir el procesamiento bajo condiciones controladas. En el camino **EBE** la evidencia se transmite por el bus ZeroMQ dentro del envoltorio versionado del bus; la relación entre una corrida de medios y una de control es uno a uno y el cierre se comunica mediante el evento de finalización del contrato de ciclo de vida.

El orden de disparo implementado sigue la regla definida en la sección 17.3.8.4: primero se inicia el plano de control y se confirma su suscripción; después se inicia el plano de medios. Cada mensaje incluye un número de secuencia, y cualquier hueco se contabiliza como pérdida del bus y degrada la corrida en lugar de ocultarse.

La evidencia se persiste antes de publicarse. El contenido lógico de la línea JSONL y del payload transmitido es el mismo, lo que permite reevaluar offline una corrida live y reproducir sus artefactos. En los experimentos del presente trabajo, los servicios se ejecutaron co-ubicados en un único host con GPU. Los contratos entre módulos no fijan esa topología, y la configuración de cada corrida registra la disposición efectiva.

#### 17.4.6. Configuración efectiva y catálogo de modelos

El conjunto de patrones efectivo del núcleo es cr01_cr02_v2. CR-01, persona sin casco, se configuró con severidad alta, confirmación a los 4.000 ms y resolución a los 2.000 ms. CR-02, persona sin chaleco reflectivo, se configuró con severidad media, confirmación a los 7.000 ms y resolución a los 3.000 ms. Las precondiciones de evidencia exigen confianza mínima de 0,35 y área mínima de 400 píxeles cuadrados para el sujeto, y confianza mínima de 0,25 para el elemento de protección. La región de búsqueda se define de forma relativa a la caja del sujeto: para CR-01, la franja superior entre el 0 % y el 45 % de la altura con margen lateral del 12 %; para CR-02, la franja del torso entre el 25 % y el 85 % con margen lateral del 8 %.

El conjunto de patrones oficial opera con granularidad de escena. En coherencia con la decisión de diseño que separa la alerta interna de su comunicación (DA-13), el motor registra cada confirmación sin supresión: el cooldown, la agrupación y la limitación de tasa pertenecen a la política del módulo de distribución. La identidad por sujeto se implementó como capacidad activable por configuración del plano de control y se trata en la sección 17.4.11.

La estrategia perceptiva del núcleo utiliza evidencia positiva: person como entidad y helmet y vest como elementos de protección. La ausencia se infiere en el plano de control y no se consulta como una negación opaca al detector.

El catálogo de perfiles de modelo materializa la sustituibilidad prevista en el diseño: variantes de Grounding DINO —tiny y base, cada una con resolución de entrada de 800 y de 560 píxeles— y de YOLOE en cuatro tamaños, todas integradas mediante adaptadores sobre el mismo contrato de salida. Una tercera familia, MM-Grounding DINO, se integró por el mismo mecanismo y fue descartada durante la evaluación; su descarte se informa con los resultados y sus perfiles quedaron archivados fuera del catálogo activo.

El núcleo no fija un modelo único. Cada instancia del servicio de medios carga un perfil al iniciarse, la comparación entre perfiles se materializa disponiendo instancias con perfiles distintos bajo la misma configuración de corrida, y el despliegue integral de la plataforma instancia un servicio por perfil del catálogo, orquestados desde la consola. Los perfiles vigentes se compararon sobre el banco de imágenes congelado; las campañas temporales y en vivo fijan un perfil por corrida, declarado en el manifiesto. Los resultados por modelo y por familia, y los criterios pre-registrados con que se seleccionó el perfil de cada campaña, se presentan en la sección 17.5.

Cada perfil declara sus umbrales y su postproceso en el catálogo, y cada corrida persiste la configuración efectiva utilizada, sin constantes ocultas en el código. A título de ejemplo, el perfil fijado por criterio pre-registrado para las corridas en vivo declara umbral de caja de 0,30 y de texto de 0,25; su postproceso aplica confianza mínima de 0,25, supresión de solapamientos con IoU de 0,50 y área mínima de caja de 100 píxeles cuadrados; y el control de ritmo opera con selección determinista de paso 1 y una cola máxima de ocho unidades.

#### 17.4.7. Artefactos y trazabilidad por corrida

Cada ejecución produce un repositorio de artefactos de sólo adición. La organización por componente conserva la evidencia necesaria para reproducir el flujo, analizar fallas y reconstruir una alerta desde su configuración hasta su salida distribuida.

**Tabla 58**

*Artefactos persistidos por componente y experimento*

| **Tramo** | **Artefactos principales** | **Función de trazabilidad** |
| --- | --- | --- |
| Plano de medios | detections.jsonl; metrics.jsonl; errors.jsonl; summary.json; effective_config.yaml; run_manifest.json; run_provenance.json | Reconstruye fuente, unidades procesadas, detecciones, tiempos, errores, configuración, procedencia y versión de código. |
| Plano de control | pattern_events.jsonl; alerts.jsonl; alerts.csv; metrics.jsonl; errors.jsonl; summary.json; effective_config.yaml | Reconstruye transiciones del patrón, alertas internas, evidencia causal, métricas y configuración del motor. |
| Soporte experimental | manifest.effective.yaml; copias de artefactos livianos; referencias a artefactos pesados; report.json; | Agrupa las corridas de ambos planos bajo un experiment_id y consolida el resultado de la ejecución experimental. |
| Distribución | notifications.jsonl (ledger de intentos y entregas, de sólo agregado); dead_letter.jsonl; distribution_summary.json | Relaciona cada intento y resultado de entrega con la alerta interna original sin reescribirla, y conserva por separado los descartes definitivos por agotamiento de reintentos. |

**Nota.** Los nombres de archivo corresponden a los artefactos implementados. Los artefactos pesados se referencian en la ejecución experimental para evitar duplicación, mientras que las configuraciones y reportes se conservan junto al experimento.

Cada plano conserva su repositorio completo por corrida: el plano de medios registra detecciones, métricas, errores, resumen, configuración efectiva, manifiesto y procedencia; el plano de control registra transiciones, alertas, métricas, errores, resumen y configuración efectiva. El soporte experimental consolida la ejecución experimental copiando los artefactos livianos y referenciando los pesados:

runs/<experiment_id>/                (repositorio del soporte experimental)   manifest.effective.yaml   media/           summary.json · metrics.jsonl · effective_config.yaml ·                    detections.ref.json  (referencia al detections.jsonl del plano de medios)   control/         alerts.jsonl · pattern_events.jsonl · metrics.jsonl ·                    summary.json · effective_config.yaml                    (y la evaluación temporal, cuando la corrida la habilita)   distribution/    notifications.jsonl · distribution_summary.json · dead_letter.jsonl                    (cuando la corrida habilita el tramo de distribución)   report/          report.json · report.md

La ejecución experimental consolida así los cuatro componentes bajo una misma clave. La modularidad de la plataforma se expresa en que un tramo pueda no estar habilitado, no en que su evidencia se consolide de otro modo cuando lo está.

El manifiesto de corrida registra la versión de código que produjo los artefactos. Junto con la configuración efectiva, el conjunto de prompts y la procedencia de la fuente, este dato permite reconstruir cada alerta hasta el modelo y el commit que intervinieron. El reporte consolidado declara el estado de aplicabilidad de cada métrica como computada, aplicable no computada, no aplicable o no interpretable, siempre con una causa explícita.

#### 17.4.8. Construcción del banco temporal y de la referencia humana de evaluación

La evaluación temporal se apoya en una referencia humana de episodios por clip, materializada mediante el esquema clip_gt.v2, segunda versión de la referencia: la primera generación registraba alertas esperadas por sujeto y fue reemplazada por episodios a nivel de escena y condición con tiempos en milisegundos, junto con estados de aplicabilidad por clip. Su construcción comprendió la adquisición y conformación del material audiovisual, la preparación y segmentación temporal de los clips, la anotación asistida con revisión humana y la derivación, validación, promoción y congelamiento de la referencia. Para la anotación se seleccionó CVAT, una herramienta de código abierto con soporte de interpolación temporal y exportación estructurada.

##### 17.4.8.1. Adquisición y conformación del material audiovisual

El material del banco proviene de dos fuentes con procedencia y grado de control experimental distintos, y esa diferencia se conserva como atributo de cada clip. La primera fuente es un rodaje guionado ejecutado con el hardware real de captura del prototipo: cada escenario se diseñó en función de una condición de riesgo del núcleo, con un guion segundo a segundo que fija la entrada del sujeto en cumplimiento, el inicio diferido de la infracción y su persistencia sostenida durante lapsos muy superiores a las ventanas de confirmación de los patrones, e incluye escenas negativas y escenas deliberadamente por debajo del umbral de confirmación. Las tomas se registraron con margen temporal adicional respecto del clip previsto, para que el recorte fino fuera una operación posterior y controlada; la grabación y el recorte se realizaron desde la propia consola del prototipo, que incorpora esa capacidad. La segunda fuente es un lote de obra real no guionada obtenido de videos públicos de internet, incorporado como bloque separado con criterios de selección definidos de antemano: material de obra en cumplimiento destinado a medir especificidad y falsos positivos —no sensibilidad—, prohibición de concatenar segmentos cortos para fabricar unidades largas, y exclusiones declaradas con causa y firma en lugar de descartes silenciosos.

*[[PENDIENTE: dirección de origen y fecha de acceso por clip del lote de obra real · depende de completar la ficha de procedencia primaria antes del cierre final del informe]]*

##### 17.4.8.2. Preparación y segmentación temporal de los clips

Los videos maestros se conservaron sin modificación y las unidades de evaluación se generaron como clips derivados, con criterios temporales explícitos fijados antes de ejecutar las campañas y aplicados como reglas ejecutables, no como juicio caso por caso. Cada clip del rodaje se recortó con un preludio fijo de 3,5 s antes del inicio de la condición —el inicio nunca coincide con el primer fotograma, porque un episodio que arranca en el origen impide medir el tiempo hasta la primera detección—, una cola posterior al cierre del episodio de entre 3 y 10 s según el escenario, y un piso de duración que garantiza que una alerta válida pero lenta pueda ocurrir dentro del clip: el inicio del episodio más el techo del objetivo de latencia de alerta de su patrón, más la ventana de resolución y un margen final. Ese piso se verifica mediante un control automático durante la derivación de la referencia, y el clip que no lo alcanza no se vuelve a recortar: sus métricas de latencia y sensibilidad quedan censuradas y así se declaran. El fundamento del dimensionamiento es bidireccional: un clip demasiado corto subestima al sistema, porque produce latencias artefactuales y cuenta como omisión una alerta que no tuvo tiempo de ocurrir; un clip sin tiempo muerto sobreestima la precisión, porque elimina los tramos donde aparecen los falsos positivos. El dimensionamiento correcto elimina ambos artefactos, de modo que cada métrica resulte atribuible al sistema y no al recorte. La selección de tomas se realizó por criterio visual de calidad de la escena, no por duración, y los límites de todos los clips quedaron congelados bajo control de versiones antes de ejecutar las campañas que los evalúan. Los clips del lote de internet no se segmentaron: cada uno es el video original completo, porque recortarlos alteraría precisamente el tiempo negativo que ese bloque aporta a la medición de falsos positivos.

##### 17.4.8.3. Preanotación asistida y revisión humana en CVAT

La anotación no partió de video crudo. Cada clip se preanotó automáticamente con un detector de vocabulario abierto de mayor capacidad que el modelo evaluado —elección deliberada para evitar circularidad entre el sistema medido y su referencia— acoplado a un algoritmo de seguimiento que propone trayectorias por sujeto, con los atributos de protección inicializados por asociación espacial. Sobre esa propuesta se realizó la pasada humana en CVAT: revisión y corrección de cajas y trayectorias, verificación de identidades a lo largo de la secuencia, asignación de los atributos observables por tramo, marcación explícita como estado desconocido de los tramos donde el atributo no resulta observable —en lugar de forzar un valor—, y fijación de los límites temporales de cada episodio. La interpolación temporal y la preanotación redujeron las operaciones repetitivas, pero no sustituyeron la revisión humana de las trayectorias, los atributos ni los límites de cada episodio: la construcción de la referencia fue una actividad intensiva en revisión, no un etiquetado manual fotograma por fotograma ni una validación automática.

##### 17.4.8.4. Derivación, validación, promoción y congelamiento

La salida de la anotación se procesa mediante una cadena reproducible de separación, derivación, validación, promoción y agregación. La cadena valida la estructura de cada exportación antes de derivar, y la derivación clasifica los episodios con las mismas ventanas de confirmación que utiliza el motor de patrones —4.000 ms para CR-01 y 7.000 ms para CR-02—, de modo que la referencia y el sistema evaluado apliquen un criterio temporal idéntico; una divergencia entre ambos produciría omisiones ficticias. Las correcciones humanas posteriores a la derivación se aplican como registros firmados sobre los artefactos versionados —nunca editando la herramienta de anotación— y un control automático falla cuando una corrección firmada no aparece en la referencia derivada. Las anotaciones promovidas quedan congeladas bajo control de versiones, con huella criptográfica por clip y un manifiesto agregado del banco. CVAT funciona así como instrumento de captura: la referencia experimental es la versión promovida en el repositorio, no el estado mutable de la herramienta.

#### 17.4.9. Verificación técnica de la implementación

El criterio de cierre de la implementación exigió que cada unidad funcional produjera evidencia verificable dentro de una corrida y que su comportamiento pudiera repetirse mediante pruebas automatizadas o artefactos persistidos. La verificación se concentró en corrección de contratos, cierre de corridas, paridad entre caminos, determinismo y funcionamiento de la integración, sin sustituir la evaluación de desempeño de la sección 17.5.

**Tabla 59**

*Evidencia de verificación técnica del prototipo*

| **Propiedad verificada** | **Evidencia de implementación** |
| --- | --- |
| Servicios ejecutables y gobernados por configuración | Los endpoints de salud, disponibilidad, creación y consulta de corridas operan sobre configuraciones validadas; cada plano limita la concurrencia de corridas activas. |
| Cadena DBE de extremo a extremo | La relectura por archivo produce detecciones, transiciones, alertas, métricas, resumen y configuración efectiva; repetir el camino conserva los artefactos deterministas. |
| Cadena EBE y cierre de ciclo de vida | El consumidor confirma la suscripción antes del productor, la corrida cierra con el evento de finalización y los huecos de secuencia se registran como degradación. |
| Paridad entre repositorio y bus | La evidencia persistida y la transmitida conservan el mismo contenido lógico; una corrida live puede reevaluarse offline. |
| Motor temporal e idempotencia | Las transiciones respetan las ventanas configuradas y la alerta usa un identificador determinista, estable ante el reprocesamiento de la misma corrida. |
| Distribución de alertas | Se verificaron replay DBE, consumo EBE, supresión, idempotencia, entrega MQTT QoS 1 contra un broker real, ledger y reporte; la consola y la orquestación quedaron integradas. |
| Pruebas automatizadas | El relevamiento integral registró 2.203 pruebas aprobadas, sin fallos, en cinco suites de la plataforma; el módulo de distribución añadió posteriormente su suite propia, también verificada. |

**Nota.** La tabla acredita funcionamiento técnico y reproducibilidad. No presenta métricas de desempeño del banco experimental, que se informan con sus denominadores y condiciones en la sección 17.5.

La verificación también confirmó que las fallas instrumentales no se convierten en ceros silenciosos. Una pérdida de bus degrada la corrida, una métrica sin reloj comparable se declara no interpretable y un canal no habilitado se declara no aplicable. Esta política preserva la diferencia entre ausencia de capacidad, ausencia de datos y resultado desfavorable.

#### 17.4.10. Alcance efectivo, límites y brechas

El cierre de la implementación requiere declarar con precisión qué capacidades fueron ejercidas, cuáles permanecen fuera del núcleo y qué resultados continúan abiertos. La Tabla 60 evita tratar todas las brechas como si tuvieran el mismo estatuto.

La concentración del prototipo en el núcleo validable no responde a una reducción tardía del alcance, sino a las condiciones de evaluabilidad de cada condición del catálogo. Las condiciones de Nivel 1 cuentan con datasets públicos y bancos de evaluación con verdad de terreno para persona y elementos de protección personal, lo que permite medir percepción, estado temporal y alerta con denominadores declarados. Las condiciones de Nivel 2 y Nivel 3, en cambio, exigen insumos que el material disponible no provee: verdad de terreno de andamios, arneses, bordes desprotegidos o zonas restringidas; definiciones externas de zona y geometría de cámara controlada; y evaluadores relacionales o de trayectoria cuya validación requeriría bancos propios que no existen en el dominio. Incorporarlas sin esa base habría producido capacidades no medibles, contrarias al criterio metodológico de no convertir extensiones en dependencias del flujo base. El esfuerzo experimental se concentró, en cambio, en llevar el núcleo a capacidad medida: la misma decisión que limitó la cantidad de condiciones cubiertas es la que permite reportar cada resultado con su evidencia.

**Tabla 60**

*Capacidades ejercidas, exclusiones y brechas de implementación*

| **Capacidad** | **Estado de implementación** | **Consecuencia para el informe** |
| --- | --- | --- |
| Identidad persistente de sujeto | Implementada y ejercida como decorador configurable de la fuente del plano de control. | La granularidad por sujeto constituye una capacidad medida. Las métricas MOT permanecen excluidas por falta de anotaciones de identidad. |
| Estrategias directa (E-DIR), indirecta (E-IND) e híbrida (E-HYB) | Las variantes se implementaron y la comparación prevista se ejecutó. | La estrategia indirecta integra el núcleo; los resultados y los veredictos comparativos se presentan en la sección 17.5. |
| Distribución de alertas | Implementada, verificada e integrada a la consola y a la orquestación. | MQTT constituye el canal ejercido. Los canales adicionales y un tablero operativo propio permanecen fuera del alcance. |
| Rama comparativa de ajuste fino | Protocolo, procedencia, servicio de inferencia, evaluación y línea base quedaron congelados, y la escalera de tramos pre-registrada se ejecutó completa. Los dos tramos entrenados se evaluaron una única vez contra el banco congelado y ninguno superó los criterios de incorporación, firmados antes de que existiera el checkpoint que se les aplicaría. El tercer tramo se cerró con causa técnica: el único corpus disponible de ese volumen comparte fuentes con el banco de evaluación y deriva la clase de cabeza descubierta de una forma que el vocabulario canónico vigente no admite. | Ningún checkpoint se incorporó como modelo de servicio. El resultado es un veredicto negativo pre-registrado y no un tramo abierto: los criterios y los márgenes se firmaron antes de la evaluación, y las tres expectativas registradas de antemano se confirmaron. Los valores por tramo y la lectura de la curva se informan en la sección 17.5. |
| Condiciones de riesgo de nivel 2 y 3 | Especificadas, pero no implementadas en el prototipo. | No forman parte del núcleo validable; su incorporación requiere evaluadores relacionales, zonales o de trayectoria y evidencia adecuada. |
| Preselección liviana en el rol de captura | Implementada para la fuente de captura propia como filtro de personas ejecutado en el dispositivo, con criterio de degradación segura y deshabilitada por defecto; su reducción de carga se midió en una comparación pareada contra el flujo completo, con un 87 % de unidades descartadas antes de salir de la cámara. No existe para las fuentes por red. Permaneció deshabilitada en todas las corridas evaluativas. | La exclusión de lo evaluativo es deliberada y anterior a los resultados: un filtro de fotogramas sin persona suprimiría las detecciones sostenidas que la tasa de falsos positivos por hora existe para medir, y superpondría el error de un detector auxiliar más débil sobre la cadena que se busca caracterizar. Habilitarlo cambiaría la procedencia de esas métricas en lugar de mejorarlas. La capacidad se reporta, entonces, como implementada y caracterizada fuera del régimen evaluativo. |
| Paridad DBE/EBE sobre fuente equivalente | La paridad de transporte y relectura fue verificada. | La reevaluación offline de una corrida live produce artefactos equivalentes; la paridad de transporte y relectura queda verificada. |

**Nota.** Los estados distinguen capacidad implementada, capacidad medida, exclusión metodológica y resultado todavía abierto.

El prototipo conserva su carácter experimental y asistivo. No implementa reconocimiento de identidad personal, no determina incumplimientos normativos y no reemplaza la supervisión de seguridad. Las alertas son registros no vinculantes producidos bajo una configuración explícita y sujetos a revisión humana.

#### 17.4.11. Extensibilidad implementada y costo de extensión

La extensibilidad se verificó en dos dimensiones: la incorporación de nuevas capacidades mediante puntos de extensión acotados y la evolución aditiva del evento de percepción. La plataforma no sostiene que toda condición pueda incorporarse sólo con lenguaje; delimita qué cambios requieren configuración y cuáles requieren código nuevo.

**Tabla 61**

*Puntos de extensión y costo técnico de incorporación*

| **Extensión** | **Intervención requerida** | **Costo técnico esperado** |
| --- | --- | --- |
| Condición del mismo tipo: sujeto sin EPP | Entrada declarativa en el conjunto de patrones y formulaciones de prompt: clase del sujeto, clase ausente, región, umbrales y ventanas. | Sólo configuración; sin reentrenamiento ni cambios en el motor. |
| Familia nueva de condiciones | Nuevo evaluador para relaciones, zonas, trayectorias u otra semántica no cubierta por spatial_absence. | Código acotado al evaluador; los contratos y el resto de la cadena se conservan. |
| Modelo de detección | Adaptador que normalice la salida y perfil de modelo en el catálogo. | Código acotado al adaptador y configuración. |
| Fuente visual | Adaptador de ingesta que produzca unidades visuales normalizadas. | Código acotado al adaptador y su validación. |
| Canal de notificación | Implementación de un consumidor del contrato de notificación y su integración de ciclo de vida. | Fuera de los dos planos; no modifica la alerta interna. |
| Dato adicional en la detección | Campo opcional con valor por defecto y consumidor tolerante a su ausencia. | Evolución aditiva sin ruptura del contrato de percepción. |

**Nota.** La frontera entre la primera y la segunda fila delimita la extensibilidad por configuración: una ausencia de EPP sobre un sujeto observable reutiliza el evaluador existente; una relación nueva entre entidades requiere lógica de evaluación específica.

El costo de incorporar vocabulario nuevo se midió en un piloto sobre la clase machinery: no requirió entrenamiento, demandó 48 líneas de configuración y nueve minutos de trabajo. El ejercicio mostró también que la extensión no termina al obtener detecciones; la alineación entre el término elegido y el concepto visual debe validarse, porque una palabra puede producir cajas plausibles sobre objetos distintos del objetivo. El desempeño cuantitativo de ese piloto se presenta en la sección 17.5.

La identidad de sujeto recorrió el segundo camino de extensión. Se implementó como un decorador configurable de la fuente de eventos del plano de control, desactivado por defecto y utilizable tanto en DBE como en EBE. La incorporación no exigió modificar el plano de medios ni romper el contrato de percepción. El identificador se conserva en los artefactos de control; no se persiste en detections.jsonl, pero el seguidor y el orden del flujo son deterministas, por lo que una relectura reproduce las mismas identidades. Su efecto cuantitativo se informa en la sección 17.5.

Lo excluido son las métricas formales de seguimiento multiobjeto, no la capacidad de asociar sujetos. De manera análoga, velocidad, dirección, pose y segmentación permanecen previstos como campos opcionales o artefactos complementarios, pero no se presentan como implementados. Esta distinción conserva la compatibilidad del contrato sin convertir previsiones de evolución en capacidades inexistentes.

En conjunto, la Etapa 4 materializó la cadena video-evento de percepción-patrón-alerta-distribución como un prototipo ejecutable, configurable, reproducible y auditable. La implementación conserva la separación entre planos, permite operar por archivo o por bus, registra la configuración y la procedencia de cada corrida, y explicita sus brechas. Sobre esta base, la sección 17.5 evalúa el rendimiento de la percepción, del estado por persona y de la alerta temporal por episodio sin atribuir a la arquitectura capacidades que no fueron medidas.

---

## Fuente: `docs/informe/entregable/borradores/17-4.md`

> SHA-256 del bloque: `db563af1cd76d10538ab45680bd3c3dc0f939bbef729b74051577d6913562e96`  
> Seleccion: borrador historico (2026-08-20), ANTERIOR a los pases 2 y 3 y ya superado por el documento de trabajo v1.6: material de consulta, NO redactar desde aca.

# Borrador — §17.4 Implementación del prototipo experimental

> 🔴 **✎ 2026-08-22 — SUPERADO: este borrador ya se pegó y el texto vigente es otro.** La
> sección §17.4 vive en el `.docx` v1.2 (extraído en `entregable/90b-etapa4-texto-extraido.md`)
> y las correcciones pendientes de aplicar son los **pases 2 y 3**. Este archivo queda como
> material de consulta histórico: **no redactar desde acá**. Sus dos advertencias internas
> (clip retirado en el DTO; fila de verificación sobre `cb_b01_p7`) quedaron resueltas el
> 2026-08-22 — ejemplo re-transcripto sobre `a_p1_c02` (ver `92` §2.2 y `94` §1.3) y fila
> integrada sin cifras ni identificador en la Tabla 67 del `.docx`.

> **Qué es esto (2026-08-16).** Borrador de la sección §17.4 del informe (hoy un
> placeholder: `[Agregado futuro correspondiente a la Etapa 4]`), redactado según las 12
> fichas `AJ-4.01…AJ-4.12` (`ajustes/04-etapa-4-implementacion.md`) sobre los insumos
> verificados: `material-etapa-3/92` (concreción contra código), `94` §1–§9 (prosa ya
> redactada), `operacion/97` (plataforma) y `operacion/114` (distribución). Patrón D-A:
> se revisa acá y **se pega una sola vez** en Google Docs cuando la sección cierra.
>
> **Convención de este archivo:** el cuerpo es el texto del informe; los bloques `> ✎/⚠️`
> son notas al integrador y **no se pegan**.
>
> ✎ **2026-08-19 — ESTE BORRADOR FUE SUPERADO.** El texto vigente de §17.4 vive en el
> `.docx` de trabajo `entregable/desarrollando/E-OVRT-VDP_Seccion_17.4_Implementacion_v0.1.docx`
> (ya comentado por el usuario), y el pase de cierre
> `entregable/desarrollando/correcciones-etapa-3-4.md` (ítems E4-01…E4-19; ✎ 08-20: E4-19
> enmienda a E4-14 y amplía §17.4.8 en cuatro subsecciones) **manda sobre
> lo que diga este archivo**. Cambios que este borrador NO refleja: término único "evento
> de percepción" (sin DetectionEvent) · `box_threshold` efectivo **0.30** (no 0.35) ·
> "ejecución experimental" en lugar de "corrida paraguas" · sin menciones de CLI
> preliminares ni de "dos nodos" · FIG-E se produce en **§17.3.8.2** (P4 de §17.4 = solo
> FIG-A) · Tablas 61/62 viven SOLO en §17.4 y §17.3 queda sin puertos · fila de ajuste
> fino actualizada (T1 evaluado, no superó los gates; T2 exploratorio en ejecución).
> El cuerpo se conserva como historia y no se re-edita.
>
> **Coordinación con la Etapa 3 (leer antes de integrar):** este borrador **absorbe la
> prosa de los redlines R-12 (verificación), R-13 (límites) y R-26 (extensibilidad)** tal
> como mandan las fichas AJ-4.10/4.11/4.12 — al hacer el pase de redlines de §17.3, esas
> tres se resuelven acá (anotarlo en `material-etapa-3/93`). La tabla de correspondencia
> (Tabla 61) la piden R-06 (§17.3.11) **y** AJ-4.02 (§17.4): si el pase de R-06 ya la
> colocó en §17.3.11, acá se **referencia** en lugar de duplicarla — decisión al integrar.
>
> **Pendientes marcados en el texto:** `[FIG-A]` y `[FIG-E]` (figuras aún no producidas,
> specs en `94` §4 y contrato `pattern_events`); un `[[PENDIENTE: …]]` en la Tabla 66
> (estado del segundo nivel de la rama de ajuste al cierre — ✎ 2026-08-18: la fila se
> actualizó, T1 ya cerró con veredicto pre-registrado y eso se afirma; lo abierto es T2);
> una `[DECISIÓN AL INTEGRAR]` sobre la fila de verificación de
> instrumento (clip retirado). Los números de tabla (61–67) son los propuestos por el
> doc `94`; la numeración final la fija el documento.
>
> **Puertas antes de dar la sección por cerrada** (manual `08` §7): P1 verificador 96 en
> verde · P2 lista NO-TOCAR · P3 las seis trampas de `GUIA-REDACTORES` §4 · P4 las figuras
> existen. **P4 hoy NO pasa** (FIG-A y FIG-E sin producir).
>
> **Regla de autocontención (usuario, 2026-08-16 — `GUIA-REDACTORES` §3.1):** el cuerpo
> de este borrador no referencia documentación local (docs, ADRs, fichas, índices, IDs
> internos) — toda la procedencia vive en los bloques `> ✎`, que no se pegan. Los
> marcadores `[FIG-x]` se resuelven a "Figura N" con la numeración del documento.

---

## 17.4. Implementación del prototipo experimental

### 17.4.1. Componentes construidos y cadena de datos

El prototipo se materializó en tres componentes de plataforma y un módulo funcional de
distribución, cada uno en un repositorio propio, más una cadena de datos que no forma
parte de la plataforma pero la alimenta.

El **plano de medios** es el pipeline de inferencia open-vocabulary. Desde su primera
fase de servicio dejó de ser una herramienta de línea de comandos: es un **servicio
gobernado por configuración** que carga el modelo una única vez al arranque y expone una
interfaz HTTP por la que se dispara una corrida por vez; las utilidades históricas de
línea de comandos se conservan como herramientas auxiliares, no como interfaz. El
**plano de control** es el motor de patrones de riesgo que consume la evidencia
perceptiva y produce las alertas internas; se ejecuta igualmente como servicio HTTP, y
conserva una interfaz de línea de comandos únicamente para el camino de relectura
offline. El **soporte experimental** no es un plano: reúne los catálogos de experimento
(conjuntos de prompts y manifiestos de corrida), el orquestador reproducible y la
consola de inspección (interfaz web con backend intermediario), que es cliente HTTP de
ambos planos.

El **módulo de distribución de alertas** es el cuarto componente funcional, y no un
tercer plano: consume las alertas confirmadas que publica el plano de control, aplica la
política de notificación, entrega por MQTT con confirmación de calidad de servicio y
conserva un registro de entregas de sólo adición. Sus contratos
(`control.notification.v1`, `control.delivery.v1`) y su verificación se detallan en
§17.4.10, porque su estatuto —trabajo comprometido con estado declarado a la entrega—
es distinto del estatuto del núcleo.

A estos componentes se suma la **cadena de datos** (adquisición, validación y conversión
de datasets), que produce los conjuntos de entrenamiento y evaluación y el benchmark de
imágenes congelado. No es plataforma: es la infraestructura de datos sobre la que la
plataforma se evalúa.

`[FIG-A — Vista de procesos de la plataforma experimental: los tres servicios (medios,
control y distribución), el orquestador, la consola y el repositorio de corrida, con el
orden de disparo y la frontera del bus. Especificación caja por caja en 94 §4 (✎ 2026-08-18:
el módulo de distribución va con línea continua — es servicio propio desde ADR-019, con
el orquestador como cliente HTTP, igual que con los otros dos servicios — ADR-020).]`

### 17.4.2. Correspondencia entre el diseño y el artefacto construido

Los contratos definidos en la Etapa 3 dejaron de ser denominaciones preliminares para el
núcleo validable: se materializaron como modelos de datos versionados, con serialización
explícita, esquema verificable e interfaces de servicio concretas, y existen corridas
registradas que los ejercitan de extremo a extremo. La tabla siguiente establece la
correspondencia entre cada contrato preliminar del diseño y el artefacto que lo realiza.

**Tabla 61** — *Correspondencia entre los contratos preliminares del diseño y su
materialización efectiva*

| Contrato del diseño | Materialización | Versión de esquema | Componente |
|---|---|---|---|
| RunConfig | Manifiesto de experimento + configuraciones efectivas por plano | `experiment.manifest.v1` | Soporte experimental |
| SourceDefinition | Sección de fuente de la configuración + registro de adaptadores de ingesta | — | Plano de medios |
| ModelProfile | Catálogo de perfiles de modelo (un archivo por variante) | — | Plano de medios |
| PromptDefinition | Conjunto de prompts versionado, identificado en cada evento | — | Soporte experimental |
| FrameMetadata | Unidad visual interna + bloque de fuente del evento publicado | — | Plano de medios |
| **PerceptionEvent** | **DetectionEvent** | **`media.detection.v1`** | Plano de medios |
| PatternDefinition | Definición declarativa dentro del conjunto de patrones | — | Plano de control |
| PatternStateChanged | PatternStateChanged | `control.pattern_state.v1` | Plano de control |
| AlertEvent | AlertEvent (identificador determinista, idempotente) | `control.alert.v1` | Plano de control |
| MetricSample | MetricSample / ControlMetricSample | `media.metric.v2` / `control.metric.v1` | Ambos planos |
| ErrorEvent | Registro de errores por corrida | — | Ambos planos |
| Bus interno de eventos | Publicación ZeroMQ con envoltorio versionado | `bus.envelope.v1` | Frontera entre planos |
| Repositorio de eventos | Archivos de sólo adición por corrida | — | Ambos planos |
| Referencia temporal de evaluación | Anotación de episodios por clip | `clip_gt.v2` | Soporte experimental |
| Reporte experimental | Reporte consolidado de corrida | — | Soporte experimental |
| Alerta distribuida | NotificationEnvelope / DeliveryRecord | `control.notification.v1` / `control.delivery.v1` | Módulo de distribución |

*Nota.* Los contratos con versión de esquema declarada están implementados y verificados
en corridas registradas. Los contratos del tramo de distribución también se
materializaron; su estatuto y su estado de integración se declaran por separado
(§17.4.10), sin confundirlos con la existencia del módulo.

> ✎ La fila de alerta distribuida del doc `94` §1.2 decía "*(preliminar — pendiente de
> materialización)*": quedó vieja el 2026-08-13 (implementación verificada, `operacion/114`
> y cierres del 13). Actualizada acá; si el pase de R-06 usa la versión del `94`,
> corregirla igual.

### 17.4.3. Los contratos de datos, materializados

Cinco contratos transportan los hechos del sistema. El **evento de percepción**
(`media.detection.v1`) traduce la salida heterogénea del detector en evidencia
perceptiva común: identificación de corrida y unidad visual, descripción de la fuente,
modelo y conjunto de prompts efectivos, detecciones normalizadas (con caja en píxeles y
normalizada) e instrumentación temporal por unidad. El **envoltorio de bus**
(`bus.envelope.v1`) encapsula ese mismo payload para su publicación, con un número de
secuencia monótono cuya única función es hacer detectable la pérdida. El **ciclo de vida
de corrida** (`run.lifecycle.v1`) delimita la corrida y la cierra con un evento de fin.
El **cambio de estado de patrón** (`control.pattern_state.v1`) registra cada transición
de la máquina de estados del motor —`inactive → candidate → confirmed → sustained →
resolved`— junto con la evidencia que la motivó y los hitos temporales del episodio. La
**alerta interna** (`control.alert.v1`) registra la confirmación de un episodio de
riesgo, con identificador determinista —reprocesar la misma corrida produce el mismo
identificador, de modo que cualquier consumidor puede deduplicar sin estado compartido—
y con evidencia auditable: el sujeto detectado, las detecciones de soporte, la clase de
protección ausente, la región evaluada y una justificación legible. La ausencia no es
una afirmación opaca del modelo: es una inferencia reconstruible.

`[FIG-E — Máquina de estados del motor de patrones (inactive → candidate → confirmed →
sustained → resolved), con las ventanas de confirmación y resolución. Se genera desde el
contrato pattern_events.]`

> ✎ Los esquemas concretos (clase Pydantic, DTO literal, envoltorio msgpack) están en
> `92` §2 y §5 con ruta y línea, y el doc `94` §1.3–§1.4 trae su prosa. Si el pase de
> R-06 ya los colocó en §17.3.11, acá basta esta síntesis; si no, evaluar traerlos.
> ⚠️ El DTO literal de ejemplo lleva `source_id` de un clip retirado del banco
> (`cb_b01_p7`) — resolver por la opción (a) del `94` §1.3 (re-transcribir desde un clip
> vigente) antes de pegar cualquier JSON.

### 17.4.4. Dos servicios gobernados por configuración

Los dos planos se ejecutan como **servicios independientes gobernados por
configuración**, expuestos mediante interfaces HTTP. Esta materialización no estaba
fijada en el diseño inicial —que deliberadamente difería la distribución de componentes—
y se adoptó para permitir que ambos planos se dispongan en el mismo host o en hosts
distintos sin modificar su lógica, y para que el soporte experimental pueda orquestar
corridas de forma reproducible. Ningún parámetro operativo está codificado en el
programa: rutas, umbrales, ventanas temporales y fuentes se declaran en configuración, y
cada corrida persiste su configuración efectiva.

**Tabla 62** — *Interfaces principales de los servicios de la plataforma*

| Servicio | Operación | Función |
|---|---|---|
| Plano de medios | `POST /api/runs` | Dispara una corrida. Recibe fuente, conjunto de prompts, parámetros de corrida, configuración de bus e identificador de experimento. Devuelve el identificador de corrida. |
| | `GET /api/runs/{id}` | Estado y resumen de la corrida. |
| | `GET /api/runs/{id}/detections` | Evidencia perceptiva paginada. |
| | `POST /api/runs/{id}/evaluate` | Evaluación de percepción contra el conjunto de referencia. |
| | `GET /readyz` | Disponibilidad del modelo cargado. |
| Plano de control | `POST /api/runs` | Dispara una corrida en modo diferido o en vivo. |
| | `GET /api/runs/{id}/alerts` | Alertas internas registradas. |
| | `GET /api/config` | Configuración efectiva de la corrida. |

Dos decisiones de diseño se materializan en estas interfaces. Primero, **el modelo no
viaja en la petición**: se carga una única vez al iniciar el servicio, de modo que el
costo de carga de pesos —del orden de decenas de segundos— queda fuera de la ruta
crítica de la corrida; comparar modelos implica disponer servicios distintos, no
reconfigurar uno. Segundo, **la respuesta afirmativa a una corrida en vivo del plano de
control implica que su consumidor de eventos ya está suscripto al bus**, invariante que
el orquestador verifica antes de disparar el plano de medios (§17.4.5).

La consola de inspección y el orquestador son **clientes HTTP de ambos planos y no
consumen el bus en ningún caso**: el bus es interno a la plataforma. Esa frontera es la
que permite que la consola siga operando sin modificación cuando los planos se despliegan
en dos nodos.

### 17.4.5. Los dos caminos de acople y sus reglas de corrección

Los planos se acoplan por dos caminos, según el escenario de despliegue.

En el **escenario diferido (DBE)** el acople es por archivo: el plano de medios escribe
su evidencia perceptiva en el repositorio de corrida —un archivo de sólo adición por
tipo de hecho— y el plano de control la relee. El repositorio es la fuente de verdad.

En el **escenario en vivo (EBE)** el acople es por bus: publicación
publicador/suscriptor sobre ZeroMQ con serialización binaria compacta, envoltorio
versionado y tópicos jerárquicos por corrida. La corrida es uno a uno y cierra con el
evento de fin de corrida. La elección del mecanismo respondió a tres criterios: no
introducir un intermediario pesado en el prototipo, no bloquear nunca la ruta crítica de
inferencia, y conservar la capacidad de sustituir el mecanismo sin modificar los planos,
dado que la durabilidad la aporta el repositorio y no el canal.

De la operación efectiva del canal se derivan tres reglas que forman parte del diseño,
porque su violación produce corridas inválidas.

**El consumidor se suscribe antes de que el productor publique.** El patrón
publicador/suscriptor no retiene los mensajes emitidos antes de que exista una
suscripción. El orden de disparo de una corrida en vivo es, por lo tanto, **primero el
plano de control y después el plano de medios**, y el orquestador verifica la
suscripción efectiva antes de continuar. No es una precaución: es una condición de
corrección, y el prototipo la hace verificable — el publicador notifica las
suscripciones activas, de modo que el sistema comprueba que hay un consumidor escuchando
en lugar de suponerlo.

**La pérdida se detecta, no se supone.** Un publicador con cola acotada descarta
mensajes en silencio al saturarse. Cada mensaje transporta un número de secuencia
monótono y el consumidor contabiliza los huecos: una corrida con huecos se marca
**degradada**, con su causa registrada, y sus métricas se interpretan a la luz de esa
declaración. La corrida degradada no se descarta ni se silencia.

**La parada es cooperativa.** Cerrar un socket del canal desde un hilo distinto del que
lo creó, mientras otro hilo está bloqueado en recepción, aborta el proceso a nivel de la
biblioteca de transporte. Las fuentes de red exponen por eso una operación de parada
cooperativa, que solicita la detención y deja que el hilo propietario cierre sus
recursos. Es el tipo de restricción de implementación que condiciona el diseño de todo
componente que consuma el bus.

El evento **se persiste antes de publicarse**: la línea escrita en el repositorio de la
corrida y el mensaje transmitido por el bus contienen exactamente el mismo contenido.
Esta propiedad, verificada, es la que garantiza que **toda corrida ejecutada en vivo sea
re-evaluable de forma offline produciendo artefactos idénticos**: el escenario EBE no
constituye un régimen de medición distinto, sino la misma cadena alimentada por una
fuente de naturaleza temporal diferente. Nada de lo que el capítulo de resultados
reporta depende de haber estado presente cuando la cámara filmaba.

El despliegue del escenario en vivo sobre **dos nodos** —un nodo de ingesta y
normalización y un nodo de inferencia con GPU— está contenedorizado y verificado, con
imágenes separadas por rol.

### 17.4.6. Configuración efectiva y modelo desplegado

El capítulo de diseño declara estructuras; el de implementación debe declarar valores.
El conjunto de patrones oficial del núcleo validable es `cr01_cr02_v2`: CR-01 (persona
sin casco) con severidad alta y ventana de confirmación de 4.000 ms, y CR-02 (persona
sin chaleco) con severidad media y ventana de 7.000 ms — dentro de las bandas que el
plan de trabajo fijó para el nivel alto (3–5 s) y medio (5–10 s), y expresadas en
milisegundos y no en cuadros, como exige el marco metodológico. Ambos patrones operan
bajo granularidad de escena, con región de búsqueda parametrizada (torso superior para
el casco, torso para el chaleco) y umbrales declarados de confianza y área mínima del
sujeto.

El conjunto de patrones oficial **no configura supresión de re-alertas**: el motor emite
en cada confirmación, porque la capacidad de supresión existe pero el conjunto adoptado
la deja desactivada — la política de supresión pertenece al tramo de distribución, no al
motor. La formulación importa: el motor *no suprime porque su configuración no lo
prescribe*, no porque no pueda hacerlo.

El conjunto de prompts del núcleo es la estrategia indirecta: `person` como entidad,
`helmet` y `vest` como elementos de protección. La evidencia es **positiva**: la
ausencia no se le pregunta al modelo; se infiere en el plano de control. El modelo
desplegado como campeón de la selección es **`grounding-dino/gdino-tiny-560`**, la
variante de 560 píxeles de entrada del catálogo, seleccionada por benchmark propio; los
umbrales efectivos del plano de medios (confianza, IoU, área mínima, control de ritmo)
están declarados en su configuración y persisten con cada corrida.

### 17.4.7. Artefactos y trazabilidad por corrida

Cada corrida produce un repositorio de artefactos de sólo adición: evidencia perceptiva,
muestras de métricas, errores, resumen, configuración efectiva (con credenciales
suprimidas), manifiesto de corrida y procedencia de los datos. El manifiesto registra la
**versión de código** (el identificador del commit) que produjo la corrida; junto con la
configuración efectiva y la procedencia, cierra la promesa de trazabilidad del diseño:
**toda alerta se reconstruye hasta la configuración, el conjunto de prompts, el modelo y
el commit que la produjeron.**

Las corridas se agrupan bajo una **corrida paraguas** identificada por experimento: el
orquestador dispara ambos planos con el mismo identificador, copia los artefactos
livianos, referencia los pesados y consolida un reporte por experimento. El reporte
declara cada métrica con su **estado de aplicabilidad** —computada, aplicable no
computada, no aplicable o no interpretable, siempre con causa— de modo que una métrica
ausente nunca es un cero silencioso sino una ausencia explicada.

### 17.4.8. Construcción de la referencia temporal de evaluación

La evaluación de patrones exige una referencia temporal anotada por humanos (episodios
de riesgo por clip, esquema `clip_gt.v2`). Su construcción siguió una cadena
reproducible: **separación del export de anotación → derivación del GT → validación →
promoción → agregación**, con cada paso como herramienta verificable y con las
anotaciones bajo control de versiones.

Dos reglas de método de esa cadena merecen registro en el informe, porque su violación
cambia el resultado en silencio. La primera: el nivel del export de la herramienta de
anotación **no es un detalle**. Un export a nivel proyecto procesado como si fuera de
tarea produce una referencia temporal **negativa sin aviso** (ningún episodio, como si
no hubiera riesgo); un export a nivel tarea procesado con la separación de proyecto
habría producido el error simétrico. La cadena verifica el nivel del export antes de
decidir el primer paso. La segunda: **el repositorio manda sobre la herramienta de
anotación**. Las correcciones firmadas viven en el repositorio y un guardián automático
falla si una corrección firmada falta en la referencia derivada; la herramienta de
anotación es un instrumento de captura, no la fuente de verdad.

### 17.4.9. Verificación: el sistema es ejecutable y verificable

El criterio de cierre adoptado en el diseño establece que una unidad se considera
completa cuando produce evidencia verificable dentro de una corrida experimental. Esta
sección presenta esa evidencia. Todas las mediciones proceden de corridas ejecutadas
sobre la plataforma implementada, con sus artefactos conservados y reproducibles. Se
indica en cada caso el detector utilizado, dado que la naturaleza del detector
condiciona la interpretación de las latencias.

**Tabla 65** — *Evidencia de verificación del núcleo validable*

| Propiedad verificada | Condiciones | Resultado |
|---|---|---|
| El pipeline de percepción opera sobre vídeo real de obra | Clip de 733 unidades, detector open-vocabulary en GPU | **0 fallos**, 15.914 detecciones, latencia de inferencia p50 220 ms / p95 267 ms, 4,39 fps efectivos |
| El repositorio y el canal transportan lo mismo | Corrida en vivo por bus, releída de forma offline (detector de referencia) | Artefactos **idénticos**; ninguna unidad perdida |
| La cadena completa cierra en vivo | Corrida en vivo de 300 unidades (detector de referencia) | 300/300 unidades, **0 pérdidas**, dos alertas registradas, cierre por evento de fin de corrida |
| Las ventanas temporales operan según su configuración | Corrida sobre vídeo con persistencia declarada | CR-01 confirma en **t = 4.000 ms**; CR-02 en **t = 7.000 ms** (los valores configurados) |
| La granularidad de escena no degrada la evaluación | Comparación de granularidades sobre el mismo corpus | **F1 = 1,0** en ambas; invariante de conteo de sujetos verificada |
| La instrumentación de latencia **detecta el incumplimiento** | Presupuesto declarado 50–250 ms | Con detector de referencia: p95 = **31,8 ms** (dentro). Con el detector open-vocabulary evaluado: p95 = **2.604 ms**, y el sistema lo **declara fuera de presupuesto** |
| La cadena completa computa las cinco métricas del marco sobre referencia temporal anotada | **Verificación de instrumento**: 1 clip de obra real, referencia preliminar, 2 alertas observadas | La cadena de medición opera completa: precisión, exhaustividad, F1, latencia de alerta y cobertura del episodio, cada una con su estado de aplicabilidad |

> ⚠️ `[DECISIÓN AL INTEGRAR]` La última fila corresponde a la verificación de instrumento
> del 2026-07-12 sobre `cb_b01_p7`, un clip **después retirado del banco** (licencia +
> GT por IA). Dos opciones: (a) dejarla como está —sin cifras y sin identificador, como
> quedó redactada arriba— porque lo afirmado es "la cadena computa", no un valor; o
> (b) re-ejecutar la verificación de instrumento sobre un clip del banco vigente y
> restituir las cifras. La medición de desempeño real vive en §17.5 sobre el banco
> congelado con GT humano, así que (a) no debilita nada.

Tres comentarios acompañan a esta tabla, y son parte del resultado.

**La instrumentación se cumple; el detector no.** La medición de latencia
captura-a-resultado opera correctamente y compara contra el presupuesto declarado. Con
el detector open-vocabulary evaluado, ese presupuesto no se cumple, y el sistema lo
señala por sí mismo. Este resultado es consistente con la evaluación comparativa de
modelos (§17.5): la restricción operativa está en el detector, no en la plataforma, y el
instrumento sirve precisamente para localizarla. Un instrumento que sólo devolviera
resultados favorables no sería un instrumento.

**La verificación de instrumento no es un resultado experimental.** Demuestra que la
cadena de medición está completa y es correcta; la medición del desempeño del sistema
corresponde al banco completo de clips con anotación humana congelada, y se presenta en
§17.5.

**El estado de la plataforma es verificable en cualquier momento.** Al último
relevamiento integral de la plataforma (agosto de 2026), las cinco suites de prueba
automatizadas sumaban **2.203 pruebas en verde, con cero fallos**; el módulo de
distribución incorporó posteriormente su propia suite, también verificada sobre
corridas registradas.

> ✎ Procedencia (no se pega): la cifra 2.203 es del relevamiento `operacion/97`
> (2026-08-05, 5 suites); la suite de distribución, de `operacion/114`.

### 17.4.10. Alcance efectivo, límites y brechas

El diseño distingue desde su formulación entre el núcleo validable y las extensiones
condicionadas. Cerrado el ciclo de implementación, corresponde declarar con precisión
qué capacidades fueron efectivamente ejercidas y cuáles permanecen especificadas sin
materializar. Esta declaración no constituye una enumeración de faltantes, sino el
registro del alcance conforme a reglas de exclusión establecidas con anterioridad a la
obtención de resultados.

**Tabla 66** — *Capacidades ejercidas, exclusiones y brechas*

| Capacidad | Estado | Consecuencia declarada |
|---|---|---|
| **Identidad persistente de sujeto** | **Implementada y medida** como decorador de fuente del plano de control; el plano de medios no la persiste en su evidencia | La granularidad de sujeto se reporta como capacidad medida (§17.4.11); el núcleo validable conserva la granularidad de escena. Las métricas MOT continúan excluidas. |
| **Comparación de estrategias de detección** (directa, indirecta, híbrida) | **Implementada y evaluada** | La estrategia indirecta queda como núcleo; la directa fue vetada por precisión y la híbrida ejecutada y refutada. Las cifras pertenecen a §17.5. |
| **Distribución de alertas** (canal de notificación) | **Funcionalmente implementada y verificada** contra los seis criterios de terminado definidos en su especificación; integrada a la consola y a la orquestación | Escenarios diferido y en vivo, política de supresión, idempotencia, entrega MQTT con confirmación y reporte verificados en corridas registradas. Su estatuto es el de trabajo comprometido con estado declarado a la entrega, conforme a una decisión registrada previa; los canales de notificación adicionales y un tablero propio permanecen fuera del alcance. |
| **Latencia captura-a-resultado en topología de dos nodos** | Instrumentada; **no computable** | Los relojes monotónicos de hosts distintos no son comparables: la métrica se declara **no interpretable**, con causa, en lugar de publicarse. |
| **Comparación con modelo adaptado** (ajuste fino) | Rama experimental ejecutada como jornada, con puertas de decisión pre-registradas antes de ver resultado alguno | El primer nivel de la comparación (ajuste mínimo de sesgos de clasificación) **corrió y se evaluó una única vez** contra el banco congelado: el veredicto, negativo conforme a los márgenes firmados por adelantado, se reporta como resultado en la sección de evaluación — un negativo pre-registrado es un dato, no un fracaso. `[[PENDIENTE: estado del segundo nivel (ajuste completo, exploratorio) al cierre del informe — al 2026-08-18 está enviado al clúster y en cola, sin resultado; se declara con su estado real y causa, nunca en presente mientras no haya corrida verificada]]` |
| **Métricas de seguimiento multiobjeto** | **No aplicables** | No se dispone de anotación de identidades; su cómputo carecería de referencia. Lo excluido son las **métricas**, no la capacidad de seguimiento (§17.4.11). |
| **Condiciones de riesgo de nivel 2 y 3** | Especificadas, no implementadas | Excluidas conforme al núcleo validable declarado. Se conservan la definición de sus patrones y su vocabulario. |
| **Comparación entre escenarios diferido y en vivo sobre fuente idéntica** | Paridad de transporte y de reparto **verificada** | La relectura offline y la corrida en vivo producen artefactos idénticos. El anclaje de sincronización entre reloj de captura y tiempo de medio para el escenario en vivo alimentado desde archivo sigue no implementado: la paridad plena queda acotada a lo verificado. |

Se registran, además, dos limitaciones conocidas del procedimiento de evaluación.
Primera: el emparejamiento entre alertas observadas y episodios anotados se resuelve de
forma voraz, lo cual puede subestimar la exhaustividad en escenarios con múltiples
episodios simultáneos de una misma condición y ventanas solapadas; la solución correcta
—emparejamiento bipartito óptimo— está identificada y su efecto se acota a los
escenarios de ese tipo. Segunda: la referencia temporal vigente es humana y está
congelada, pero no tuvo una segunda anotación independiente ni estadístico de acuerdo;
esa limitación se declara como L2.

> ✎ El módulo de distribución se lanza desde la orquestación como **subproceso local**
> del backend de la consola — patrón registrado como nota operativa (no cubierto por
> ADR-008/009, que gobiernan a los dos planos). Mencionarlo solo si el integrador
> considera que la sección de despliegue lo necesita; los planos no se acoplan a él.
> ⛔ ✎ 2026-08-18: **esta nota completa quedó superada — NO incluirla.** ADR-019 le dio
> servicio HTTP propio al módulo (`:8082`) y ADR-020 derogó a ADR-018: el orquestador le
> habla **por HTTP**, igual que a los otros dos servicios, y el subproceso quedó como
> fallback operativo que **no se describe en el capítulo**. La sección de despliegue dice
> tres servicios y un patrón de acople HTTP, sin excepciones que explicar.

### 17.4.11. Extensibilidad medida

Una arquitectura orientada a la detección open-vocabulary sólo resulta justificada si la
incorporación de una condición de riesgo nueva es efectivamente más barata que en una
arquitectura de vocabulario cerrado. Esa afirmación no debe postularse: debe medirse.
La extensibilidad del prototipo se declara en tres planos: los puntos de extensión del
sistema, el costo medido de incorporar una condición nueva, y la extensión del evento de
percepción efectivamente ejercida.

**Los puntos de extensión.**

**Tabla 67** — *Costo de extensión de la plataforma*

| Extensión | Qué requiere | Costo |
|---|---|---|
| Una **condición nueva del mismo tipo** (sujeto sin elemento de protección) | Una entrada declarativa en el conjunto de patrones —clase del sujeto, clase ausente, región, umbrales, ventana temporal— y las formulaciones de prompt correspondientes | **Sólo configuración. Sin reentrenamiento y sin código.** |
| Una **familia nueva de condiciones** (relacional, zonal, de trayectoria) | Un evaluador nuevo en el motor de patrones | Código acotado al evaluador; el resto de la cadena no se modifica |
| Un **modelo de detección nuevo** | Un adaptador que normalice su salida al contrato de evidencia perceptiva | Código acotado al adaptador |
| Una **fuente visual nueva** | Un adaptador de ingesta que produzca unidades visuales normalizadas | Código acotado al adaptador |
| Un **canal de notificación nuevo** | Un consumidor del contrato de alerta | Externo a los dos planos |

El contraste entre la primera y la segunda fila delimita, con precisión, **la frontera
real de la extensibilidad por lenguaje**: una condición expresable como ausencia de un
elemento observable sobre un sujeto observable se incorpora por configuración; una
condición que requiere una relación nueva entre entidades requiere un evaluador.
Declarar esa frontera —en lugar de afirmar genéricamente que "todo es configurable"— es
la contribución arquitectónica que este trabajo sostiene.

**El costo medido de una condición nueva.** La primera fila de la tabla no es una
promesa: se ejecutó. La incorporación de una condición nueva sobre una clase jamás
configurada (`machinery`) costó **cero entrenamientos, 48 líneas de configuración y
9 minutos de trabajo**, y la clase alcanzó **AP@0,5 = 0,662 en régimen zero-shot**
sobre el benchmark de imágenes congelado (6.477 imágenes; 99 cajas de referencia de la
clase nueva). El resultado lleva su contrapeso, y va escrito junto: el mismo ejercicio
mostró que **una clase puede parecer detectada sin estarlo** —las detecciones caían
sobre otro objeto—, de modo que validar visualmente la palabra elegida es parte del
costo real de extensión, no un opcional.

> ✎ Procedencia (no se pega): cifras del índice `results/bench_imagenes/` (piloto A1,
> tabla T-77, conclusión AF-4); el contrapeso es el hallazgo F-94.1.

**La extensión del evento de percepción, ejercida.** El contrato del evento está
diseñado para crecer sin romperse (regla de evolución aditiva, §17.3.11.4). De las
extensiones previstas —identidad de sujeto, cinemática, pose, segmentación—, la
identidad de sujeto **se recorrió de punta a punta**: se materializó **por
configuración**, como decorador de la fuente de eventos del plano de control (activable
por parámetro, desactivado por defecto), **sin tocar el contrato ni el plano de
medios**, y sirve por igual al acople por archivo y al acople por bus. Su efecto se
midió en condiciones pareadas: sobre el banco de clips del rodaje con referencia
temporal humana (34 clips evaluables), la granularidad de sujeto elevó el F1 de episodio
de **0,789 a 0,930 con las mismas detecciones bit a bit**. La única variable entre ambas
mediciones fue la granularidad, de modo que la ganancia es íntegramente del motor de
patrones y no de la percepción; y el camino gobernado por configuración reproduce la
medición de forma exacta: el número es lo que rinde la plataforma declarada en
configuración, no un script suelto.

> ✎ Procedencia (no se pega): índice `results/clip_bench/` — campaña G1 (sujeto) contra
> su línea de base de escena. Ojo con el id corto de la línea de base ("T1" del banco):
> colisiona con la tarea T1 de fine-tuning; en el informe no se usa ninguno de los dos
> identificadores internos.

El resultado lleva dos honestidades. Primera: el identificador de identidad **no queda
en la evidencia persistida del plano de medios** sino en los artefactos del plano de
control; la trazabilidad se conserva porque el seguidor es determinista y el flujo está
ordenado —una relectura reproduce las mismas identidades—, y quien necesite el artefacto
con la identidad embebida lo genera con una herramienta auxiliar. Segunda: lo excluido
del alcance son las **métricas** de seguimiento multiobjeto, no la capacidad; el núcleo
validable sigue definido sobre granularidad de escena por decisión registrada, y la
granularidad de sujeto se reporta como capacidad medida.

Esto convierte la regla de evolución del contrato —que en §17.3.11.4 se enuncia sin
cifra, por corresponder al diseño— en **capacidad verificada**: el evento de percepción
sostuvo, sin modificación alguna, la incorporación del primer dato de la lista de
extensiones previstas, y esa incorporación produjo la mejor configuración medida del
banco.

---

> ✎ **Checklist de cierre de la sección** (no se pega):
>
> - [ ] Producir **FIG-A** (spec `94` §4) y **FIG-E** (contrato `pattern_events`) — P4.
> - [ ] Resolver la `[DECISIÓN AL INTEGRAR]` de la Tabla 65 (fila de verificación de instrumento).
> - [x] ~~Actualizar el `[ACTUALIZAR A LA ENTREGA]` de la Tabla 66 con el estado real de la jornada T1~~ ✎ 2026-08-18: hecho — T1 cerrado (veredicto pre-registrado, se afirma); queda el `[[PENDIENTE: …]]` de esa fila con el estado de T2 al cierre del informe.
> - [ ] Verificar las tres cifras citadas contra sus índices (`0,662` bench_imagenes · `0,789/0,930` clip_bench · `2.203` operacion/97) y correr `96-verificar-indices.py` — P1.
> - [ ] Revisar contra la lista NO-TOCAR (`00` §7) y las seis trampas (`GUIA-REDACTORES` §4) — P2/P3.
> - [ ] Al pegar en Google Docs: marcar `AJ-4.01…AJ-4.12` en el tablero del manual `08` §5, anotar R-12/R-13/R-26 como absorbidas en `93`, y re-extraer la foto (D-C).

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

## Fuente: `docs/operacion/130-relevamiento-plataforma-pre-etapa-2.md`

> SHA-256 del bloque: `350389b72f505617d701c5826ea1e9edbed93c8e40b971cb8a44aa32039cd560`  
> Seleccion: FOTO VIGENTE de la plataforma (2026-08-28): estado de los seis repos, hechos citables por modulo con ruta:linea en datos/130-…, divergencias doc<->codigo y la tabla protocolo 17.1 vs construido. Manda sobre operacion/97 en todo lo que difieran.

# 130 — Relevamiento exhaustivo de la plataforma antes de la Etapa 2 (2026-08-28)

> **Qué es.** El relevamiento que pidió el usuario antes de tocar §17.1: los **cinco repos de
> código** leídos contra lo que el set documental afirma de ellos y contra lo que el protocolo
> del informe (§17.1) prescribe, más una auditoría **documento contra documento** del propio
> set. Objetivo: que la alineación de punta a punta, el kit regenerado desde cero y el pase de
> §17.1 partan de una base verificada hoy, no de fotos del 08-05/08-15.
>
> **Cómo se hizo.** Seis agentes de solo lectura en paralelo (uno por repo + uno para `docs/`),
> cada uno con la lista de afirmaciones a verificar y el texto extraído de §17.1. Ningún
> servicio se levantó, ningún test pesado se corrió (WSL con 7,4 GiB); los conteos de tests son
> por `--collect-only` o por `grep "def test_"` según el repo. Los **cinco informes completos**
> (con tabla afirmación → veredicto → `ruta:línea`) están en
> `datos/130-relevamiento-pre-etapa-2/` (fuente: `docs/operacion/datos/130-relevamiento-pre-etapa-2`) y son la
> evidencia; este documento consolida y decide.
>
> **Qué manda.** Sobre cualquier cifra o afirmación de estado anterior al 2026-08-28, manda
> este documento; donde este documento diga "declarar", el informe declara y no maquilla.
> Reemplaza como foto de plataforma a `operacion/97` (2026-08-05) en todo lo que difieren.

---

## 0. Veredicto en cinco líneas

1. **La plataforma está donde los docs dicen que está, en lo estructural.** Los seis repos
   tienen el árbol limpio (salvo `docs`, con el trabajo 08-25→08-28 sin commitear); los tres
   servicios HTTP + el bus, el pattern set `cr01_cr02_v2` (4.000/7.000 ms, `high`/`medium`,
   histéresis 2.000/3.000), el campeón `gdino-tiny-560` a `box_threshold 0,30`, `bench_v3`
   congelado (sha256 idéntico, `--verify` PASS byte a byte) y **las 26 cifras de los cuatro
   índices verifican contra sus `metrics.json`** (`96-verificar-indices.py` EXIT 0).
2. **Hay una afirmación ancla confundida**: la comparación `gdino-tiny` 800 px vs 560 px **no
   está a umbral igual** (0,35 vs 0,30). El campeón sigue siendo el campeón (0,551 es el dato
   de la combinación 560·0,30, y el par `base`/`base-560` sí está a 0,30 en ambos), pero "560 no
   degrada mAP respecto de 800" no puede afirmarse para tiny sin ese caveat.
3. **Tres desvíos de doc que llegarían al informe si no se corrigen**: el orden de arranque live
   real es **control → distribución → medios** (no "distribución primero"); el fine-tuning
   **excluyó `chv`** (2.203 css + 743 ppe_siabar = 2.946) y varias fichas dicen que entrenó con
   él; y el rango 500–2.000 imágenes de la Tabla 28 de §17.1 **se desvió a 2.946 sin
   justificación escrita**.
4. **Lo que §17.1 prescribió y no se ejerció está identificado, ítem por ítem** (§4): variantes
   template, vocabulario aislado-vs-completo cruzado, español, doble anotación/kappa, MOT17/OVT-B,
   NVDEC, Precision/Recall por severidad en el evaluador, percentiles de `t_alert-system` en
   `evaluate-alerts`, hardware/entorno en el manifiesto de corrida, warm-up de unidades. Nada de
   eso se "corrige" en §17.1: se **declara** donde corresponde (§17.4/§17.5) y §17.1 se ajusta
   sólo en lo que es decisión de protocolo.
5. **Conteos vencidos por todos lados** (tests 643/646/641/668, "39 tests", "16 campañas",
   "19 cifras", "4 estados", "11 endpoints"): ninguno llega al informe, pero todos viven en
   docs que el kit reparte. Se corrigen en este pase (§7).

---

## 1. Estado de los seis repos al 2026-08-28

| Repo | Rama | HEAD | Árbol | Tests medidos hoy | Nota |
|---|---|---|---|---|---|
| `e-ovrt_media-plane` | `feature/inference-service` | `f439db2` (08-22) | limpio | **643** `def test_` (grep; docs decían 646 y 641+5) | venv 3.12.13; Dockerfile CUDA 12.4 con ruedas cu13 pineadas — build nunca ejecutado |
| `e-ovrt_control-plane` | `feature/control-service` | `64cc976` (08-19) | limpio | **312** (collect-only, sin `tests/labs`) + 22 labs | venv 3.14.4 (`requires-python >=3.11`); 12 endpoints en `:8081` |
| `e-ovrt_alert-distribution` | `main` | `f9447a1` (08-19) | limpio | **133** + 1 integración MQTT deseleccionada por default | venv 3.11.15; Dockerfile 3.11-slim |
| `e-ovrt_experimental-setup` | `feature/webconsole-consola-tesis` | `2bfb268` (08-22) | limpio | `tests/` **88** · `finetuning/tests` **46** · BFF **668** (docs decían 643) | compose 13 servicios válido por lectura; `results/finetuning/` no existe (cifras FT en `finetuning/manifests/`) |
| `e-ovrt_datasets` | `feature/datasets-v2-setup` | `6524e21e` (08-20) | limpio | **431 passed** (1,6 s) | `build_bench_strata.py --verify` **PASS ×2**; sha256 `bench_v3.json` = manifiesto |
| `docs` | `main` | `8a0b74a` (08-23) | **57 cambios sin commitear** (08-25→08-28) | `herramientas/tests` 62 + 51 subtests | deuda git del usuario, anotada |

---

## 2. Lo que se confirmó — hechos citables por módulo

*(cada uno con `ruta:línea` en el informe del agente correspondiente)*

**Plano de medios.** Campeón `IDEA-Research/grounding-dino-tiny` a **560×560, `box_threshold`
0,30, `text_threshold` 0,25, NMS IoU 0,50, fp16**, warm-up de modelo al cargar + `prepare_run`
por corrida. G2A se mide **desde el dequeue** (el proceso ya leyó el frame) **hasta el fin de la
inferencia**; presupuesto 50–250 ms evaluado sobre P95; `capture_to_host` (sensor → dequeue)
existe **sólo para OAK-D** — en RTSP ese tramo no se midió. Bus XPUB `:5557`, msgpack
`bus.envelope.v1`, `seq` monótono aunque se descarte, payload byte-idéntico al JSONL, cierre
`run.lifecycle.v1/run_finished`. Un modelo por proceso (`EOVRT_MODEL_REF`), un run activo (409;
**una preview también bloquea**). Fuentes: `image_folder` (no recursivo), `video_file`, `rtsp`,
`oak_d`; preselección EN-2 default off, fail-open, sólo `oak_d`. Artefactos por run:
`effective_config.yaml`, `run_manifest.json`, `detections.jsonl`, `metrics.jsonl`,
`summary.json` (`media.summary.v2`), `run_provenance.json`, `dropped_units.jsonl` — **no existen
`report.json` ni `metrics.json` en este plano** (son del control-plane / experimental-setup).
El campo `run.scenario` **no clasifica nada** (los 472 runs locales dicen `DBE`, incluidos 73
`oak_d` y 21 `rtsp` live): DBE/EBE se distingue por `source_type` + `bus.enabled`.

**Plano de control.** Máquina de **cinco** estados `inactive → candidate → confirmed →
sustained → resolved`; alerta sólo al entrar a `confirmed`; reapertura `resolved → candidate`,
nunca a `inactive`. `cr01_cr02_v2`: CR-01 `high` 4.000/2.000 ms, CR-02 `medium` 7.000/3.000 ms,
escena, **sin cooldown ni memoria** (la capacidad existe en el código, desactivada y no
configurada). Umbrales en ms rigen cuando hay `timestamp_ms`; frames sólo fallback declarado
inerte sobre imágenes (ADR-013). ADR-011 cableado: el motor emite en cada confirmación; el
evaluador cuenta `re_alerts` fuera del denominador de precisión; FP = evento de alerta fuera de
toda ventana de episodio y sub-umbral; ventanas CR-01 [t0+4 s, t0+10 s], CR-02 [t0+7 s, t0+20 s].
Persistencia implementada como **duración desde la primera evidencia con tolerancia a huecos**
(< `resolve_after_ms`), no como proporción de frames positivos. Hitos persistidos **4 de 5**:
`first_evidence_ms` y `alert_registered_ms` monotónicos; candidato/confirmado en
`pattern_events.jsonl` con tiempo de fuente; notificación fuera del repo. `t_alert-system` cierra
en `alert.timestamp_ms` (reloj de fuente del frame que confirmó), no en el registro interno. G1
= `input.track_persons` decora la fuente con un tracker IoU por `source_id`; sin `track_id`
degrada a escena con causa `no_track_id`; verificado en live.

**Distribución.** `t_alert-notification = puback_wall_ms − ts_publish_ms` (**bus de alertas →
PUBACK QoS 1**, dos relojes de pared del mismo host, no monotónico, declarado): p95 **64,534 ms
n=460**; sostenido (2.ª+) **102,025 ms n=104**; 1.ª entrega 49,869 n=356. **No arranca en la
confirmación del patrón** sino en la publicación en el bus. Idempotencia por
**(`notification_id`, `channel`)**, `notification_id = sha1(alert_id)[:16]`; **cinco outcomes**
`delivered / failed / skipped_duplicate / dead_letter / suppressed_cooldown`; `dead_letter` tras 3
intentos con 500 ms fijos. **QoS 1 es el único valor admitido**; topic `eovrt/alerts/<severity>`.
El **cooldown es política de re-notificación del distribuidor** (clave `(condition_id,
source_id)`, 30 s, en memoria; en la campaña 118: 376/836 suprimidas = 44,98 %). Broker de la
**medición** = `amqtt 0.11.3`; Mosquitto es el broker del **despliegue** (compose, sin build).
Runner: HTTP por default; subproceso sólo con `EOVRT_CONSOLE_DISTRIBUTION_TRANSPORT=subprocess`, y
ese fallback no funciona en el compose.

**Orden de arranque live REAL** (runner `runner.py:1095-1149`): **control** (con
`alert_bus.enabled` y `wait_for_subscriber_ms ≥ 10 s`) → **distribución** (necesita
`control_run_id`) → **medios**. La no-pérdida en `:5558` la garantiza el handshake XPUB del
publicador, **no el orden**. El orden "medios ← control ← distribución" que dicen el `CLAUDE.md`
raíz, el README de FIG-A y la nota de `128` §4 **es falso**.

**Datos.** `bench_v3.json`: 6.477 imágenes / 55.165 anotaciones; `stratum` con **cuatro**
valores (`shel5k` 5.000 · `chv` 1.330 · `bench_obra_val` 85 · `bench_obra_test` 62 — el
informe habla de tres estratos fusionando los dos de obra); anotaciones `person` 24.172 ·
`helmet` 22.949 · `bare_head` 6.181 · `vest` 1.863. GT persona CR-01: bench_obra 60 + shel5k
5.248 = **5.308 con el GT vigente**; el **n=5.313** que citan CLAUDE.md, contexto base, los
índices y los docs 64/66 es el del GT del 23-jul (65 en bench_obra, antes del fix del 29-jul):
es el n de aquella medición y se cita así, fechado. CR-02: **142** violadores, sólo en
`bench_obra`. Fine-tuning efectivo (`finetuning_v1`): **`construction_site_safety` 2.203 +
`ppe_siabar` 743 = 2.946 train / 483 val; `chv` excluido** (100 % de sus 1.330 imágenes es
estrato del banco). De los 9 datasets de la Tabla 26 de §17.1, **2 se usaron** (SHEL5K y CHV,
ambos sólo como fuentes del banco), 1 tuvo uso lateral (MOCS, en copia Roboflow de 1.471
imágenes, no el original de 41.668), 6 se descartaron; **los dos datasets que se entrenaron y
la fuente de `bench_obra` no figuran en la Tabla 26** (investigación Roboflow del 06-17).

**Índices de resultados.** `96-verificar-indices.py`: ✅ 1.452 enlaces / 0 rotos · 26 cifras
sobre 17 campañas · 3 deltas bootstrap · 35 docs de procedencia. Todas las cifras del "Estado
vigente" del kit y de los "cuatro números" coinciden con los `metrics.json` (47/32/15/37,
manifiesto `3f14f50a…`; 0,789 / 0,930 / 0,146; T1 y T2 con todas sus cifras). Única no
verificable mecánicamente: mAP50 0,551 (sin `metrics.json` en el repo; remite al doc 64).

---

## 3. Divergencias doc ↔ código, consolidadas

Severidad: 🔴 llegaría al informe como afirmación falsa · 🟠 contradicción entre documentos o
cifra vencida que el kit reparte · 🟡 higiene. "Dueño" = dónde se corrige. Estado al cierre de
este pase en §7.

| ID | Sev. | Hallazgo | Dueño / dónde corregir |
|---|---|---|---|
| **R-01** | 🔴 | **Orden de arranque live**: docs dicen distribución → control → medios; el runner hace **control → distribución → medios** y la garantía es el handshake XPUB (≥10 s), no el orden. | `CLAUDE.md` raíz ("Acople entre planos" y párrafo de alert-distribution) · `figuras/README.md` FIG-A (nota + revisar el SVG/PNG) · `128` §4 nota de figuras · `experimental-setup/infra/platform/README.md:69-70` y `docs/experiments.md:93-96` (repo del usuario) · glosario `13:109` ("distribución posterior" → concurrente) |
| **R-02** | 🔴 | **Fine-tuning con `chv`**: AJ-2.07 ✎08-18 (b), R-24 (b), glosario §5, doc 99 §2 y `datasets_metadata.yaml` dicen que se entrenó con css+chv+ppe_siabar; el FT real excluyó `chv` (anti-leakage). Copiarlo al informe violaría la propia Tabla 28. | `ajustes/02` AJ-2.07 · `93` R-24 · glosario `13` §5 · `99` §2 · registry (repo datasets, del usuario) |
| **R-03** | 🔴 | **Tabla 28 de §17.1: rango 500–2.000 imgs** vs 2.946 train, sin justificación en ADR-017 / doc 100 / README de finetuning. | Declarar en §17.4/§17.5 (fila FT) con causa (100 % de linajes elegibles tras dedup y exclusión del banco; F-127.1 muestra que aun así es insuficiente). Anotar en `ajustes/02` AJ-2.11 y `ajustes/05` AJ-5.13. |
| **R-04** | 🔴 | **`gdino-tiny` 800 px corrió a `box_threshold` 0,35 y `gdino-tiny-560` a 0,30** en todas las corridas (07-23 incluidas); doc 64 no lo registra. "560 = igual o mejor mAP que 800" está confundido en el par tiny (el par base sí está a 0,30 en ambos: 0,453 vs 0,401). | `64` ✎ (declarar el umbral por brazo; reescribir como "560 @0,30 ≥ 800 @0,35") · `CLAUDE.md` raíz (párrafo del campeón) · `results/bench_imagenes/index.md` (repo del usuario) · kit: citar siempre el par (resolución, umbral) |
| **R-05** | 🟠 | **`evaluate-alerts` sólo produce promedios** de `t_alert`/TTFD/SDR y no persiste latencias por episodio ⇒ los P50/P95/P99 de §17.1.7.8.1 no salen del evaluador; el kit declara `t_alert-system` citable sin decir que es un promedio por campaña. | kit "Estado vigente" (precisar "promedio por campaña; percentiles sólo del tramo de plataforma en `summary.json`") · §17.4 declara PARCIAL |
| **R-06** | 🟠 | **Precision/Recall por severidad (§17.1.7.5.5) no existe en el evaluador**; sólo el desglose por condición aguas abajo (1:1 con severidad). | §17.4/§17.5: citar P/R por condición y decir que equivale a severidad porque cada CR tiene una sola |
| **R-07** | 🟠 | Glosario `13` §3 y contexto base (`:729`) dicen **4 estados** del motor; son **5** (`sustained`), como el propio kit dice más abajo y FIG-E. | glosario `13` §3 · generador del kit |
| **R-08** | 🟠 | Causa two-node: docs dicen `cross_node_monotonic_clock`; el código emite **`clock_skew`** (control-plane y experimental-setup). ADR-0006 local atribuye `not_applicable:no_ground_truth` al control-plane; lo emite `report.py` del experimental-setup. "11 endpoints" → 12. | glosario `13` · `estado-de-implementacion-adrs.md` (ADR-0006/0008 de la serie de 4 dígitos) · ADRs locales (repo control-plane, del usuario) |
| **R-09** | 🟠 | **Containerización "diferida / fuera de alcance"** en ADR-019 §4, spec 45 §9.8, 124, 125, kit y GUIA — pero Dockerfiles ×3 + compose de 13 servicios existen desde 08-19/20. Lo diferido es **build + smoke**. | ADR-019 ✎ · spec 45 ✎ · `124`/`125` ✎ · generador del kit · GUIA |
| **R-10** | 🟠 | **Broker de la medición 118 = `amqtt`**, no Mosquitto (nucleo/19 §5, spec 45 §5). Además `t_alert-notification` **arranca en `ts_publish_ms` del bus**, no en `confirmed_at_ms` como aún discuten spec 45 §3 y nucleo/19 §6.1. | nucleo/19 ✎ · spec 45 ✎ · kit |
| **R-11** | 🟠 | **`n=5.313`** (CLAUDE.md, contexto base ×4, índices, docs 64/66) es el GT del 23-jul; el vigente da 5.308. | Citar fechado: "n=5.313 (GT del 23-jul; 5.308 con el GT vigente)". `CLAUDE.md` raíz · generador del kit · índice (repo del usuario) |
| **R-12** | 🟠 | **Conteos de tests vencidos**: BFF 643→668; media-plane 646/641→643 (grep); distribución "39"/"37"→133+1; "2.203 tests" (op97) es foto del 08-05. | `CLAUDE.md` raíz · generador del kit · `114` · README/requirements del experimental-setup (usuario) |
| **R-13** | 🟠 | **Tabla 26 de §17.1** vs registry: GDUT-HWD "Apache-2.0" / SHWD "MIT" → "verificar" (nunca descargados); CHV "CC BY 4.0" es del **paper**, el dataset no tiene licencia (L7); MOCS descrito como original (41.668, NC) → lo usado es copia Roboflow 1.471. **Omite** css y ppe_siabar. | Es material del pase de §17.1 (AJ-2.07 / PODA-12): la Tabla 26 se comprime a "utilizados + descartados con causa" y las licencias se escriben como están en el registry |
| **R-14** | 🟠 | **Auditoría humana del GT (Task 4.3)**: `bench_gt_audit.md` §4–6 vacíos y docs 75/78 "sin ejecutar", pero `estado_avance.md` y el README de documentation la dan por ejecutada (sólo se generó el kit). | repo datasets (usuario); en el informe **no afirmar** que hubo auditoría humana del GT de imágenes |
| **R-15** | 🟠 | `CLAUDE.md` raíz: bloque "emits… `train_v2`/`bench_v2`/`demo_v2`" vencido (archivadas 08-15, el propio archivo lo dice más abajo); no lista `download_shel5k.sh`; "las fuentes exponen `request_stop()`" (es `RunControl.request_stop()` en medios; `BusSource.request_stop()` en control). | `CLAUDE.md` raíz |
| **R-16** | 🟠 | `report.json`/`metrics.json` citados como artefactos del media-plane (AJ-2.09) — no existen ahí (`summary.json` + `metrics.jsonl`). `effective_config.yaml` imprime campos inertes de la otra familia (`confidence_threshold 0,25` en GDINO; `box_threshold 0,35` en YOLOE): trampa de cita. | `ajustes/02` AJ-2.09 · glosario `13` §4 (regla de lectura: GDINO = `box`+`text`+`iou`; YOLOE = `confidence`+`iou`) |
| **R-17** | 🟠 | G2A del código **no incluye sensor ni red** (dequeue → fin de inferencia); declarado como F-101.8 para OAK-D, pero para **RTSP el tramo faltante no se midió** (no sólo "sumar 202–217 ms"). | kit / GUIA trampa · §17.4/§17.5 |
| **R-18** | 🟠 | `finetuning/README.md` cierra en T1 (08-17), sin T2 NO-GO; manifiestos de `experiments/` que ya no resuelven (`mock_chv`, `video_annotated*`, 4 `mmgdino`); README raíz con estados de prompt sets vencidos. | repo experimental-setup (usuario) |
| **R-19** | 🟡 | Glosario `13` §6 omite `e-ovrt_alert-distribution` en "Repos de código" (y lista `:8082`); §4.2 "16 campañas" → 17; GUIA §7 "19 cifras / 16 campañas" → 26 / 17. | glosario `13` · GUIA |
| **R-20** | 🟡 | `114` §4 brechas cerradas sin ✎ (ledger por generaciones, venv 3.11, Dockerfile, runner orquesta, layout `runs/exp_<id>/distribution/`); `114`/`118` puertos sin `:8082`; nucleo/19 §4.6 omite `latency_mode`/`experiment_id`; "el ledger es obligatorio porque QoS 1 duplica" mezcla dedup del publicador con re-entregas broker→suscriptor. | `114` · `118` · nucleo/19 |
| **R-21** | 🟡 | Percentiles del media-plane con método mixto (p50 mediana interpolada; p95/p99 por índice), `capture_to_host` sin p99; `run_manifest.json` sin hardware/SO/versiones (§17.1.7.8.1 lo exige); `warmup_units` = 0 en los 472 runs (warm-up de **modelo** sí; de **unidades** no). | §17.4 declara; kit trampa |
| **R-22** | 🟡 | Datasets: "3 estratos" vs `manifest.strata` = 4; shel5k "416×416 uniforme" (real 416×415/416×416/415×416/415×415); `bench_v3.md` no cita `person_gt_bench_obra_v2.json` (CR-02, 142); `ppe_siabar` con dos `source_url`; `construction_ppe_skcet` fuera de `datasets_metadata.yaml`; `bench_v3.py` no chequea duplicados **entre** estratos (verificado ad hoc: 0 basenames repetidos). | repo datasets (usuario) · glosario §4.4 ya explica la fusión |
| **R-23** | 🟡 | Manifiesto del clip bench con `annotator: null` en los 34 clips del Bloque A (los 13 del B: `simon`). No contradice "GT humano"; procedencia por clip incompleta. | repo experimental-setup (usuario) |

---

## 4. Protocolo §17.1 vs lo construido — la tabla que alimenta el pase de la Etapa 2

Leyenda: **✅ CUMPLIDA** · **◐ PARCIAL** · **⊘ NO EJERCIDA** · **↯ DESVIADA** (se hizo distinto,
con causa). Regla de uso: lo ✅ y lo ↯ que sea *decisión* puede reflejarse en §17.1 como protocolo
ajustado; lo ⊘ y lo ◐ que sea *resultado de ejecución* **se declara en §17.4/§17.5**, nunca se
borra de §17.1 (guardrail `07` §9; mapa regla 5).

### 4.1 Entorno (§17.1.4)

| Prescripción | Estado | Evidencia / qué declarar |
|---|---|---|
| CPN: HP Victus, RTX 4060 Laptop 8 GB, **Windows 11** | ↯ | Corre en **Linux (WSL2)** y Docker Ubuntu; el repo no registra el SO en los artefactos. §17.1.4.2.1 puede seguir describiendo el hardware; el SO se corrige como decisión. |
| NVDEC para decodificar en GPU (§17.1.4.2.2) | ⊘ | `cv2.VideoCapture` software; 0 referencias a nvdec/cudacodec. Declarar en §17.4. |
| EN = OAK-D Pro PoE; inferencia en borde sólo como variante condicionada | ✅ | `oak_d_source.py` (DepthAI v2); EN-2 default off, medida aparte (87 % drop). |
| Contingencia: cámara IP por RTSP (§17.1.4.2.4) | ✅ (y **se ejerció primero**) | `rtsp_source.py`; 21 runs `rtsp`. → AJ-2.10. |
| Stack oficial GDINO/YOLOE, GPU NVIDIA | ✅ | Transformers + Ultralytics; torch 2.12.1. |
| Exportación PyTorch / TensorRT / ONNX (§17.1.4.3.3) | ◐ | Sólo PyTorch nativo. |
| Escenarios A (DBE) y B (EBE) | ✅ | Por fuente + `bus.enabled`; **no por el campo `scenario`**. |
| Parámetros de referencia ≈640 px (Tabla B.6) | ↯ | YOLOE 640; GDINO **560** (campeón) y 800; el propio §17.1.7.7.5 exige recalibrar si difiere de 640 → se cumplió por selección S1/S2 (con el caveat R-04). |
| Restricción VRAM 8 GB | ✅ | `gpu_memory_peak_mb`, fp16 default. |

### 4.2 Condiciones, patrones y prompts (§17.1.5)

| Prescripción | Estado | Evidencia / qué declarar |
|---|---|---|
| Tres niveles de severidad | ◐ | `high`/`medium` ejercidos; `critical` no (PR-03…06 excluidos, E-01/E-02). |
| Persistencia en segundos (3–5 / 5–10) | ✅ | 4.000 / 7.000 ms dentro del rango. → AJ-2.01 como **decisión dentro del rango**. |
| "Sostenida o con proporción mínima de positivos" | ↯ (variante declarada) | Duración desde primera evidencia con tolerancia a huecos < `resolve_after_ms`. Declarar en §17.3/§17.4. |
| Histéresis activación ≠ desactivación | ✅ | 4.000/2.000 y 7.000/3.000. Ya pedida por §17.1.5.3.3 — no es agregado. |
| Calibración empírica FP vs ventana | ⊘ | Umbrales fijados por Tabla 24/D.4; sin barrido. Declarar en §17.5. |
| Estados inactivo/candidato/confirmado/resuelto | ✅ (+`sustained`) | Cinco estados; FIG-E. |
| "Evita alertas repetidas sobre una misma situación" | ↯ deliberada (ADR-011) | El motor re-alerta tras resolver (`re_alerts`); la supresión es del distribuidor. → AJ-2.02 se resuelve como **regla de conteo** (D-E2-3), no como "el §17.1 arrastra el cooldown" (no lo menciona). |
| Estrategias directa vs indirecta comparadas | ✅ | D1 Nivel A (2 estratos) + Nivel B con veto pre-registrado. → **D-E2-2: bautismo E-DIR/E-IND/E-HYB en §17.1.5.4.2**. |
| Eje "contexto de vocabulario": cada prompt **aislado y en vocabulario completo** | ↯ | Régimen asimétrico declarado (E-DIR aislada, E-IND conjunta); ningún prompt en ambos; sustituido por un control único (B1 vs T2: +1 palabra = −0,082 F1). → AJ-2.04.1 se escribe como **decisión de protocolo** y §17.5 reporta el control. |
| Variantes con template ("a photo of a [CLASS]") | ⊘ (definidas, no medidas) | `cr01_template`/`cr02_template` con `enabled_by_default: false`, excluidas de D1. → AJ-2.04.2: §17.1 las mantiene como eje; §17.5 declara no ejercidas. |
| Hiperparámetros congelados entre variantes | ✅ (con matiz) | `box 0,30 / text 0,25` idénticos en todos los brazos; umbrales operativos calibrados por brazo con grid idéntico y reportados como variable (permitido). |
| Especificidad / estructura sintáctica | ◐ | Sólo dentro de E-DIR (`cr01_spec`); E-IND siempre `person`. |
| Idioma inglés; español complementario | ✅ / ⊘ | Todos los sets `language: en`; español = E-09 excluida. |
| Catálogo de candidatos (Tabla C.1) | ✅ | `prompts/_archive/*candidates.yaml` → finalistas `edir_v1` (8 formulaciones, acta doc 76). → AJ-2.07. |
| Piso ~200 positivos por condición o n + IC | ◐ | CR-01 shel5k 2.487 ✅; CR-01 bench_obra 28 y CR-02 82 ✗ → IC95 bootstrap (vía prevista) → **L8**. → AJ-2.05 (la vía se declara en §17.1; el n en §17.5). |
| Doble anotación ≥20 % + kappa + IoU | ⊘ (declarada **L2**) | `double_annotation_ratio 0.0`; en imágenes se reutilizó GT existente; la auditoría humana Task 4.3 **no se ejecutó** (R-14). → AJ-2.06. |
| Matriz (modelo × condición × prompt × contexto) | ◐ | `tiny-560` + réplica `base-560`; CR-01/CR-02; 6 variantes E-DIR + E-IND; **un régimen por brazo**. |
| Confianza media de los TP por formulación | ⊘ | No figura en `metrics.json`. → AJ-2.07 la pide: queda como criterio en §17.1, no ejercido en §17.5. |
| Métricas por entidad componente (indirecta) | ✅ | AP por clase/estrato + Nivel A por persona. |

### 4.3 Datos (§17.1.6)

| Prescripción | Estado | Evidencia / qué declarar |
|---|---|---|
| Inventario Tabla 26 (SH17, SHEL5K, CHV, Pictor-PPE, Construction-PPE, GDUT-HWD, SHWD, SODA, MOCS) | ↯ | Usados: SHEL5K y CHV (sólo banco); lateral: MOCS (copia Roboflow, piloto A1); descartados: 6. **Entrenaron css + ppe_siabar, ausentes de la tabla.** → PODA-12 + AJ-2.07: comprimir a utilizados + descartados con causa; licencias como en el registry (R-13). |
| Tabla 28: disyunción · test compartido · semilla · splits oficiales · congelamiento previo | ✅ | `finetuning_v1.summary.json` (overlap 0, seed 42, `bench_v3_sha256`); bench congelado 07-23, FT 08-15+. |
| Tabla 28: **rango 500–2.000** | ↯ **sin justificar** | 2.946 train. → R-03: declarar en §17.4/§17.5. |
| Tabla 28: no solapamiento cruzado | ✅ train / ◐ bench | Dedup perceptual en train; sin chequeo inter-estrato en bench (ad hoc: 0 repetidos). |
| MOT17 / OVT-B (Tabla 30) | ⊘ (E-10, ADR-015) | 0 menciones en el repo. → **D-E2-6: intacto con ⊘ explícito**. |
| Contraste con métricas de la literatura sobre el mismo dataset (§17.1.4.4.1) | ⊘ | Ningún índice compara con cifras publicadas de SHEL5K/CHV; `bench_v3` es composición propia. |
| Consideraciones éticas / AAIP | — | `[[PENDIENTE]]` de D-E1-11 viaja en espejo a §17.1.11 (D-E2-7). |

### 4.4 Métricas e instrumentación (§17.1.7)

| Prescripción | Estado | Evidencia / qué declarar |
|---|---|---|
| G2A = t_capture + t_transport + t_preprocess + t_inference | ↯ (declarada) | Código: dequeue → fin de inferencia; sensor→dequeue sólo OAK-D (`capture_to_host` 202–217 ms); **RTSP sin ese tramo**. §17.1.7.7 conserva la descomposición (§16.5 la cita); §17.4 declara qué tramo se midió. |
| Presupuesto 50–250 ms sobre P95 | ✅ instrumentado | `p95_within_budget`; live GDINO fuera de presupuesto (630–890 ms). |
| `t_alert-system` = inicio anotado → alerta registrada | ✅ (reloj de fuente) | Cierra en `alert.timestamp_ms`, no en `alert_registered_ms`. Declarar. |
| `t_alert-notification` complementaria, sólo con trayecto instrumentado | ✅ | Tramo bus→PUBACK; **no arranca en la confirmación**; no llega a interfaz/cliente (◐ Tabla 33). |
| TTFD y SDR | ✅ | En tiempo (ms); criterio declarado; no aplicable declarado. |
| Métricas temporales sólo sobre secuencias | ✅ | ADR-013; `not_applicable:non_temporal_source`. |
| **P/R por severidad** | ◐ | No en el evaluador; por condición aguas abajo (1:1). → R-06. |
| Cinco hitos por alerta | ◐ 4/5 | Notificación fuera del control-plane; candidato/confirmado con reloj de fuente. → AJ-2.09: §17.1 no cambia; §17.4 lo dice. |
| **P50/P95/P99 + promedio** | ◐ | Media: `summary.json` ✅ (método por índice, p50 interpolada). Control: `summary.json` ✅ / `evaluate-alerts` **sólo promedios**. Distribución: `metrics.json` ✅ / summary por corrida sólo min/mean/p95. → R-05. |
| Warm-up previo declarado | ◐ | Modelo sí (carga + `prepare_run`); `warmup_units` = 0 en todos los runs; control sin warm-up (0,2 ms/unidad, irrelevante); distribución no declarado (1.ª entrega más rápida, no infla). |
| Timestamps monotónicos con fuente declarada | ✅ / ↯ distribución | Medios y control monotónicos + `source_clock`; distribución con dos wall-clocks del mismo host (declarado). |
| Declarar hardware y entorno por corrida | ◐ | `effective_config` + `run_provenance` ✅; **GPU/torch/driver/SO/hostname no se registran**. |
| Unidad de conteo del FP declarada e invariante | ✅ | Evento de alerta fuera de ventanas; `re_alerts` fuera del denominador. → D-E2-3 escribe la regla en §17.1.7.8.3. |
| GT inexistente ⇒ no aproximar | ✅ | `not_applicable:*`, censura, clip negativo no evaluable. → AJ-2.12. |
| Métricas MOT (HOTA, IDF1…) | ⊘ (E-10) | Sin GT de identidades. → D-E2-6. |
| Protocolo comparativo preentrenada vs ajustada (§17.1.7.6): ΔAP, ΔRecall ✅ · ΔPrecision, ΔSDR, Δt_alert, ΔTTFD ⊘ · retención OV ✅ T2 / no medible T1 · latencia ⊘ · horas-persona ⊘ | ◐ | Los checkpoints ajustados **sólo se evaluaron en DBE-imágenes**, nunca en clips ni EBE. §17.1 conserva el protocolo; §17.5 fila FT lo declara. |
| Fases de la Tabla 36 | ✅ (orden ↯ declarable) | Orden real: Preparación → Baseline DBE imágenes (07-23) → **EBE rodaje (07-25)** → GT video → Nivel B base → sensibilidad de prompts (08-03/04) → tracking/densidad → EBE blindado → Reporte → estrato B → distribución → **fine-tuning último (08-15→21)**. La formulación primaria se congeló **antes** del estudio de sensibilidad. → AJ-2.08: nombres de fase sí; el orden se declara en §17.4. |
| Adaptación: máx. 2 candidatos GDINO y YOLOE (§17.1.9.2) | ◐ | Sólo YOLOE-26s ajustado (T1 lineal, T2 completo); GDINO no (T3 diferido con causa técnica). → AJ-2.11: regla y criterio en §17.1; la jornada en §17.4/§17.5. |

---

---

## Fuente: `docs/operacion/97-relevamiento-plataforma-2026-08-05.md`

> SHA-256 del bloque: `8ebd3688ab3ed92a5a6e79e20155c2f7fba3e164359eb09e7eb4699e8bde2ee7`  
> Seleccion: FOTO HISTORICA del 2026-08-05, SUPERADA por operacion/130: decia 4 repos, dos servicios HTTP y distribucion no implementada. Solo para trazabilidad; no citar su estado.

# 97 — Relevamiento integral de la plataforma (2026-08-05)

> ⚠️ ✎ **2026-08-28 — SUPERADO por `operacion/130` (fuente: `docs/operacion/130-relevamiento-plataforma-pre-etapa-2.md`)
> en todo lo que difieran.** Este documento es la **foto al 2026-08-05**, válida como **memoria
> de implementación** (los bloques nuevos, las trampas operativas y el "cómo quedó" de cada
> módulo siguen siendo lectura útil). Lo que ya no describe el estado: hoy son **5 repos de
> código** (se sumó `e-ovrt_alert-distribution`), **tres servicios HTTP config-driven**
> (`:8080/:8081/:8082`, ADR-019; **dos** patrones de acople con ADR-020, que derogó ADR-018), la
> **distribución de alertas por MQTT está implementada, verificada y medida** (docs 114/118/124/125;
> `t_alert-notification` p95 64,534 ms n=460 — la tabla de §0 que dice "no implementada" y el §4
> "especificada, no construida" quedaron falsos), el deploy integral de 13 servicios está definido
> (doc 126; build+smoke post-entrega) y **los conteos de tests son los de `130` §1** (media 643 ·
> control 312+22 · distribución 133+1 · exp-setup 88/46/668 · datasets 431), no los 2.203 de acá.
> El kit de redacción reparte este documento a la Etapa 4 con esa advertencia.

- **Fecha:** 2026-08-05.
- **Tipo:** relevamiento consolidado / memoria de implementación.
- **Reemplaza como punto de entrada a:** **doc 56** (foto del 2026-07-18), que pasa a
  ser artefacto histórico. **Este documento es la foto completa y verificada de la
  plataforma al 2026-08-05** — insumo directo para el capítulo de concreción técnica
  del informe.
- **Método:** relevamiento contra **git y código**, no contra memoria: `git log` desde
  el 2026-07-18 en los 4 repos (85 commits), verificación por lectura de los módulos
  citados, y ejecución real de las 5 suites. Ninguna afirmación de acá sale de un
  mensaje de commit sin haber mirado el código.

---

## 0. Resumen ejecutivo

Desde el doc 56 la plataforma **no cambió de arquitectura**: sigue siendo dos servicios
HTTP config-driven (media-plane `:8080`, control-plane `:8081`) con dos caminos de
acople (DBE por archivo, EBE por bus ZeroMQ), más la webconsole como superficie de
gestión primaria (ADR-009). Lo que cambió es que **dejó de ser una plataforma probada
en laboratorio y pasó a ser una plataforma que produjo el tramo experimental completo**:
13 campañas sobre GT humano, un rodaje con hardware real y una jornada de operación en
vivo.

Seis bloques de capacidad que el doc 56 no cubre:

1. **Identidad por sujeto como capacidad de plataforma** (control-plane `b0ba763`):
   `sources/tracking.py` produce `track_id` como **decorador de fuente**, en DBE y en
   EBE/live por igual, activable con `input.track_persons`. Es la palanca que dio el
   mejor resultado del banco.
2. **Estrategias de evidencia por patrón** (`5327080`): el motor despacha entre
   `eind` (ausencia espacial), `edir` (evidencia directa gateada por persona),
   `hyb_or` y `hyb_and` — este último **rechazado en validación** hasta el tramo de
   fusiones, para que no falle en silencio comportándose como `eind`.
3. **Evaluador temporal maduro**: `evaluate-alerts` v2 (censura por dimensionamiento,
   FAR/hora con base declarada, matching bipartito) más los **3 fixes F-EV1/2/3** que
   subestimaban la plataforma.
4. **Grabación y recorte de clips desde la consola** con hardware real (F-DR2..F-DR10),
   y el **video-gt-lab** cerrando GT temporal humano de 34 clips.
5. **Modelos con `image_size`** y los catálogos `gdino-tiny-560` / `gdino-base-560`,
   más `prepare_run` (pre-flight por corrida que resolvió el misterio de latencia 20×).
6. **Consola rediseñada de raíz** (tokens, primitivas, 11 pantallas) como evidencia de
   tesis, con preflight de plataforma y lanzamiento gateado.

**Estado de suites: las 5 verdes, 2.203 tests** (medidas hoy, no supuestas).

## 1. Suites, medidas hoy

| Repo / módulo | Comando | Resultado |
|---|---|---|
| media-plane | `.venv/bin/python -m pytest -q` | **641 passed**, 5 skipped |
| control-plane | `pytest tests/ -q --ignore=tests/labs` | **312 passed** |
| datasets | `python3 -m pytest datasets/tests/ -q` | **283 passed** |
| webconsole backend | `.venv/bin/python -m pytest -q` | **586 passed** |
| webconsole frontend | `npm test` (vitest) | **381 passed** (55 archivos) |
| **Total** | | **2.203 tests, 0 fallos** |

## 2. Qué se sumó desde el doc 56, por repo

### 2.1 control-plane (9 commits)

| Commit | Fecha | Qué |
|---|---|---|
| `b0ba763` | 08-05 | **Identidad por sujeto como capacidad de plataforma** + endurecimiento del camino live |
| `5327080` | 08-04 | **Evaluador `direct_evidence` + estrategias de evidencia por patrón** (spec 41 §6) |
| `c1cbb56` | 08-03 | **3 artefactos de medición** que subestimaban la plataforma (F-EV1/2/3) |
| `03ee8b0` | 07-29 | Deprecación del pattern set v1 (migrar `replay_dbe` a v2), ADRs 0006–0013 materializados |
| `5fcea11` | 07-26 | Patrones activos expuestos por HTTP en vivo y en la traza |
| `ef001ff` | 07-23 | La corrida live usa v2, no v1 (**F-DR9**) |
| `b3c6cc8` | 07-19 | `evaluate-alerts` v2: censura por dimensionamiento, FAR/hora, matching bipartito |
| `a53e95e` | 07-18 | `DELETE /api/runs/{id}` |

**Verificado en código:**

- `sources/tracking.py` — `TrackingSource` es un **proxy transparente**: delega
  `close()`, `request_stop()` y `dropped_events` al inner source explícitamente, y el
  resto por `__getattr__`. El docstring registra por qué: *"un decorador en live
  silenciaría `bus_dropped_events` (violación de ADR-003)"*. `maybe_track(source,
  enabled, ...)` es el punto de entrada config-driven.
- `engine/evaluators/` — `spatial_absence.py` y `direct_evidence.py`, con despacho por
  `evidence.strategy`. El motor no conoce evaluadores concretos.
- `configs/patterns/` — 7 pattern sets. Oficial vigente: **`cr01_cr02_v2`**; la
  variante de granularidad es `cr01_cr02_v2_subject`; `cr01_cr02_v1` **deprecado**.

> **Trampa vigente (F-DR9):** `cr01_cr02_v1` produce falsos `missed` por umbrales
> incompatibles con `derive_clip_gt`. **Nunca usar v1.**

### 2.2 media-plane (12 commits)

| Commit | Fecha | Qué |
|---|---|---|
| `d4f9ef4` | 07-24 | Nombre opcional de run (`RunSummary.name`) expuesto en vivo y terminado |
| `c78bd16` | 07-23 | `evaluate` restringe el `person_gt` al run por default |
| `da44756` | 07-23 | **`image_size` en GDINO + catálogos `gdino-tiny-560` / `gdino-base-560`** |
| `b37d550` | 07-23 | **`prepare_run`**: pre-flight por corrida antes de abrir la fuente |
| `9ef144c` | 07-23 | Corrida con cero unidades termina `failed` con motivo explícito (**F-DR10**) |
| `eddeb89`, `cee8832`, `71bf0ac` | 07-18 | **Sesión de preview en vivo** para posicionar cámaras y probar prompts (sin backlog, con deletterbox) |
| `d9f21fa` | 07-18 | Warm-up de lente (descarte de frames iniciales) en fuentes vivas |

**Verificado en código:** `models/base.py::prepare_run`, `image_size` en el adaptador
de GDINO y en la fábrica de modelos, `service/preview_manager.py`.

**El hallazgo detrás de `prepare_run`** (doc 61): el binding lazy del modelo hacía que
el costo de warm-up cayera sobre los primeros frames de la corrida, produciendo una
latencia aparente 20× mayor. El pre-flight lo mueve fuera de la ventana de medición.

> **Nota de estado:** la palanca **F-RT5** (+18% fps, −14,4% latencia, p=0,0195) está
> commiteada en la rama **`perf/producer-pil-roundtrip`** (`3deb64c`) y **el merge es
> decisión del usuario** — no está en la línea principal. La salida es byte a byte
> idéntica, así que no requiere re-validar mAP.

### 2.3 experimental-setup (50 commits)

El repo que más se movió. Cuatro bloques:

- **Grabación de rodaje** (07-21 → 07-23): script standalone OAK-D, motor de
  grabación, API REST, panel en la ventana Cámaras, y los fixes del dry-run con
  hardware real (**F-DR2..F-DR8**).
- **Generación y recorte de clips desde la consola** (07-23 → 07-26): UI de clips,
  contrato `marks: list[float]`, `compute_window_multi` para P6/P8, piso de censura
  universal y cola por escenario.
- **Rediseño completo de la consola** (07-28): capa base (tokens, primitivas,
  glosario, gráficos), 4 pantallas de la defensa reconstruidas y las 7 restantes
  migradas al armazón compartido. **11 pantallas** en `frontend/src/pages/`.
- **Catálogos y resultados** (07-29 → 08-05): congelamiento de `edir_v1`/`eind_v1`
  (acta doc 76), estructura de campañas, y las **13 campañas** hoy en `results/`.

**Verificado:** las 11 pantallas existen; `results/` tiene los 4 índices por material
con punto de entrada en `results/index.md`.

### 2.4 datasets (14 commits)

- **`bench_v3` ensamblado y congelado** (6.477 imgs, 3 fuentes, sha256 por fuente) tras
  incorporar SHEL5K y curar `bench_obra` de forma reproducible **dejando el original
  intacto**.
- **GT temporal del rodaje**: fichas `.clip.yaml` de los 34 clips + GT derivado +
  banco reportable.
- **Agregador de campañas normalizado** (`aggregate_clip_campaign.py`) — la pieza que
  hace que comparar dos combinaciones sea leer dos archivos con la misma forma.
- **Scoring de estado por persona** para Fase D + GT de CR-02 desde negativos
  explícitos, y **fusión dual-run** para E-HYB.

## 3. La plataforma hoy, por capacidad

| Capacidad | Estado | Dónde vive |
|---|---|---|
| Servicio de inferencia OVD config-driven | ✅ | media-plane `:8080`, modelo por proceso (`EOVRT_MODEL_REF`) |
| Fuentes: archivo, carpeta, RTSP, OAK-D | ✅ | `sources/{video_file,image_folder,rtsp,oak_d}_source.py` |
| Prefilter EN-2 on-device | ✅ (opcional, fail-open) | solo `oak_d`; 87% drop medido |
| Preview en vivo para encuadre y prompts | ✅ | `service/preview_manager.py` |
| Motor de patrones temporal CR-01/CR-02 | ✅ | control-plane `:8081`, pattern set `cr01_cr02_v2` |
| Estrategias de evidencia (eind/edir/hyb_or) | ✅ | `engine/evaluators/`, despacho por `evidence.strategy` |
| `hyb_and` | ⚫ **rechazado en validación** con causa | declarado, no silencioso |
| Granularidad escena (G0) / sujeto (G1) | ✅ | `granularity` del patrón + `input.track_persons` |
| Acople DBE (archivo) | ✅ | `eovrt-control replay` |
| Acople EBE (bus ZeroMQ + msgpack) | ✅ | `bus.envelope.v1`, `bus_dropped_events=0` en todas las corridas |
| Evaluación temporal de alertas (5 métricas) | ✅ | `evaluate-alerts` v2 + SDR/TTFD |
| Laboratorio de GT temporal de video | ✅ | video-gt-lab, contrato `clip_gt.v2` |
| Banco de imágenes estratificado | ✅ | `bench_v3`, 6.477 imgs |
| Consola web (gestión + evidencia) | ✅ | 11 pantallas, preflight y lanzamiento gateado |
| Runner de experimentos reproducible | ✅ | manifiestos en `experiments/` |
| Distribución de alertas (MQTT, spec 45) | 🔴 **no implementada** | decisión: es lo último (ADR-005) |

## 4. Lo que NO está implementado (registro honesto)

- **Distribución de alertas por MQTT** (spec 45): especificada, no construida. Por
  decisión de orden (ADR-010: plataforma primero), no por bloqueo.
- **`track_id` producido por el pipeline online del media-plane** (spec 42 §3): hoy la
  identidad la produce el control-plane como decorador de fuente. **Funciona en DBE y
  en live** (verificado, doc 91), pero el productor de identidad no está en el plano
  de medios. Decisión de ADR-002 pendiente si se quisiera llevar a producción.
- **`hyb_and`**: rechazado en validación con causa escrita (doc 87 §5).
- **Ancla de sincronización para EBE-desde-clip**: impide hoy alimentar el banco por el
  bus con correspondencia exacta al GT temporal.
- **F-RT5 sin mergear** a la línea principal (§2.2).
- **Doble anotación / kappa** en el GT de video: decisión declarada (L2), no omisión.

## 5. Trampas operativas vigentes

Consolidadas del doc 68 §6 más las de esta jornada. Las que muerden en silencio:

1. **Levantar cada servicio desde la raíz de SU repo** — las rutas relativas de los
   configs resuelven contra el CWD.
2. **Orden EBE no negociable**: control-plane primero (confirmar `subscribed: true`),
   media-plane después. PUB/SUB pierde lo publicado antes de la suscripción.
3. **Nunca cerrar un socket ZeroMQ desde otro hilo** mientras uno está en
   `recv_multipart` — `SIGABRT`. Para eso existe `request_stop()`.
4. **Nunca usar el pattern set v1** (F-DR9).
5. **El `ping` a una cámara link-local desde WSL en modo NAT miente** — responde el
   gateway de Windows (`ttl=63`). Verificar con `ip route get` (sin `via`) y `ttl=64`.
   Requiere `networkingMode=mirrored` en `.wslconfig`.
6. **`ingest.config` de la OAK-D usa `url`, no `ip`** (con `ip` da 422).
7. **`outputs.base_dir` del control-plane resuelve relativo al archivo de config**, no
   al CWD del script que lo invoca.
8. **El modelo es del proceso, no del run** (`EOVRT_MODEL_REF` al arrancar).
9. **El summary de `/api/runs/{id}` viene anidado bajo `summary`** — leer el nivel de
   arriba devuelve `None` en silencio (mordió al runner del doc 81).
10. **Descubrir el run del control por diferencia de directorios, no por mtime** — el
    mtime cruza las alertas de un clip con el GT de otro sin avisar.
11. **El export de CVAT a nivel PROYECTO numera frames en espacio global** — sin
    `split_cvat_project.py` el GT sale negativo en silencio.
12. **`cameras/` está gitignorado** (credenciales RTSP en claro).

## 6. Estado de git

| Repo | Rama | Último commit | Sin commitear |
|---|---|---|---|
| media-plane | `feature/inference-service` | `94660e6` (08-04) | — |
| control-plane | `feature/*` | `b0ba763` (08-05) | — |
| datasets | `feature/*` | `6577d7b5` (08-05) | — |
| experimental-setup | `feature/*` | `ab2d809` (08-05) | los 4 índices de `results/`, las 6 campañas R1–R6, `prompts/clase_nueva_v1.yaml` |
| docs | local (sin remote por decisión) | `a256250` (08-04) | docs 93–97 + `datos/94-*`, `96-*` |

**Deuda declarada:** `main` desactualizado en los 4 repos con remote (el trabajo vive
en ramas `feature/*`); backup de `docs` a otro disco pendiente (no tiene remote por
decisión del proyecto).

## 7. Qué cambia respecto del doc 56

| Afirmación del doc 56 | Estado hoy |
|---|---|
| "Plataforma completa, integrada y probada E2E" | **Sigue vigente, y además produjo el tramo experimental completo** |
| GT de video `gt_preliminary` | **Superado: `gt_ready`** con adjudicación humana (doc 80) |
| Benchmark de imágenes = BENCH v2 (196 imgs) | **Superado: `bench_v3`** (6.477 imgs, 3 fuentes) |
| Métrica estrella = `cb_b01_p7` (1 clip) | **Superado: 34 clips, 13 campañas** |
| Granularidad: solo escena (G0) | **G1 por sujeto disponible y verificada en vivo** |
| Estrategia de evidencia: solo ausencia espacial | **4 estrategias, 3 implementadas** |

> **Para el informe:** las cifras del doc 56 §9 y de la tabla del brief de redacción
> (`informe/97` §5) están **superadas en su totalidad**. La fuente de cifras vigente es
> `e-ovrt_experimental-setup/results/index.md` y sus cuatro índices.

---

## Fuente: `docs/nucleo/14-mapa-de-la-cadena.md`

> SHA-256 del bloque: `0f97159e8f7c5db98e965180bfc78863a6e225442e33a45de20b93854ac39439`  
> Seleccion: documento completo.

# 14 — Mapa de la cadena: quién habla con quién

- **Fecha de relevamiento:** 2026-08-10
- **Qué es:** el prólogo de la serie de relevamientos por servicio (`14`–`19`). Da la vista
  de conjunto; el detalle de cada pieza está en su documento.
- **Regla de la serie:** **ningún relevamiento publica cifras de resultado.** Las cifras
  salen de los cuatro índices de `e-ovrt_experimental-setup/results/`; la historia de
  capacidades medidas, de `operacion/97`. Acá está **qué es cada pieza y cómo funciona**.

---

## 1. El workspace no es un repo

`/home/simonll4/projects` **no** es un repositorio: es un directorio de trabajo que
contiene **cinco repos git hermanos e independientes**, cada uno con su propio historial y
su propio remoto. Se commitean por separado.

Que sean hermanos **en disco** no es cosmético: varias configuraciones usan rutas relativas
cross-repo (`../e-ovrt_datasets/...`), así que mover un repo rompe al vecino.

## 2. La cadena

```
                        ┌──────────────────────────────┐
                        │   experimental-setup   (15)  │   consola + runner + catálogos
                        │   orquesta por HTTP los dos  │   y LOS ÍNDICES DE RESULTADOS
                        │   planos; nunca toca el bus  │
                        └───────┬──────────────┬───────┘
                                │ HTTP :8080   │ HTTP :8081
> ✎ **2026-08-18 — la caja "NO CONSTRUIDA" del diagrama quedó superada DOS veces.** El
> módulo de distribución está **implementado y verificado** desde el 2026-08-12/14
> (docs `operacion/114`/`118`: MQTT QoS 1, ledger de idempotencia, p95 64,534 ms n=460)
> y desde el 2026-08-17/18 **también expone servicio HTTP propio** (`:8082`, ADR-019,
> doc `operacion/124`) — ~~el subproceso del runner sigue siendo el default (ADR-018)~~
> ✎ 2026-08-19: **ADR-020 (2026-08-18) derogó a ADR-018 — HTTP es el default del
> runner** y el subproceso quedó como fallback operativo
> (`EOVRT_CONSOLE_DISTRIBUTION_TRANSPORT=subprocess`).
> El diagrama se conserva como cuerpo histórico por convención del set.

                                ▼              ▼
   ┌────────────┐  imágenes  ┌──────────────┐        ┌───────────────┐  control.alert.v1  ┌──────────────┐
   │ datasets   │  y video   │ media-plane  │ media. │ control-plane │ ─────────────────► │ distribución │
   │   (16)     │ ─────────► │    (17)      │ detec- │     (18)      │                    │     (19)     │
   │ vocabulario│            │  percepción  │ tion.v1│   patrones    │                    │ NO CONSTRUIDA│
   │ + bancos   │            │   OVD :8080  │ ─────► │   alertas     │                    │              │
   └────────────┘            └──────────────┘        └───────────────┘                    └──────────────┘

        insumos          →       detección       →        patrón → alerta      →        notificación → entrega
```

| # | Repo | Qué es | Documento |
|---|---|---|---|
| 1 | `e-ovrt_experimental-setup` | El centro operativo: consola, runner, catálogos y resultados | **`15`** |
| 2 | `e-ovrt_datasets` | Los insumos: vocabulario canónico, bancos de imágenes y de video | **`16`** |
| 3 | `e-ovrt_media-plane` | Percepción OVD, servicio `:8080` | **`17`** |
| 4 | `e-ovrt_control-plane` | Motor de patrones de riesgo, servicio `:8081` | **`18`** |
| 5 | `e-ovrt_alert-distribution` | Ciclo de vida y distribución de la alerta — ~~diseñado, no implementado~~ ✎ 2026-08-18: **implementado y verificado** (docs 114/118); ✎ 2026-08-19: **servicio HTTP `:8082`** (ADR-019, doc 124) como **acople default del runner** (ADR-020, deroga ADR-018); CLI para el camino offline; subproceso = fallback operativo | **`19`** |

Y un sexto repo que no es software: **`docs/`**, el set documental. Es un repo git propio.
~~local y sin remoto, por decisión del proyecto~~ ✎ 2026-08-18: desde el 2026-08-10, cuando
el equipo empezó a necesitar acceso, tiene remote propio (`e-ovrt_docs`, rama `main`).

## 3. Los dos caminos de acople

Media-plane y control-plane se acoplan de dos maneras según el escenario de despliegue.
**No son alternativas de implementación: son dos escenarios distintos, y los dos se
ejercieron.**

**DBE (offline, un host) — acople por archivo.** El media-plane escribe
`runs/<id>/detections.jsonl`; el control-plane lo relee. El repositorio es la fuente de
verdad, y **el pipeline es determinista** (verificado: re-inferir da detecciones idénticas
bit a bit).

**EBE (live, dos nodos) — acople por bus.** ZeroMQ PUB/SUB con msgpack y envelope
`bus.envelope.v1` (ADR-003). La corrida es **1:1** y cierra con
`run.lifecycle.v1/run_finished`.

> **El orden de disparo en live no es negociable.** PUB/SUB pierde todo lo publicado antes
> de que el consumidor se suscriba. Por eso va **primero** `POST :8081/api/runs` con
> `mode: live` —cuyo 201 implica que ya está suscripto— y **después** `POST :8080/api/runs`
> con `bus.enabled: true`. Los huecos de `seq` se cuentan como `bus_dropped_events` y
> **degradan la corrida; nunca se silencian**.

**La distribución cuelga del mismo esquema** *(✎ 2026-08-19)*: las alertas confirmadas
viajan por el **bus de alertas `:5558`** (control → distribución), con la misma regla de
suscripción previa que el bus de detecciones; y el acople del runner con el distribuidor
es **HTTP `:8082`** (ADR-019/020), igual que con los otros dos servicios.

**El JSONL es la verdad en los dos casos:** toda corrida live es re-evaluable offline y
produce artefactos idénticos. Eso está verificado, y es lo que hace auditable al camino en
vivo.

## 4. Las cuatro fronteras

La cadena tiene cuatro cortes, y cada uno es una decisión registrada:

| Frontera | Qué separa |
|---|---|
| detección → patrón | Ver algo no es que sea riesgo. El motor no ve imágenes |
| patrón → alerta | Una condición instantánea no es una alerta: hace falta persistencia confirmada |
| alerta → notificación | Una alerta confirmada no es algo que amerite molestar a un humano (ADR-011) |
| notificación → entrega | Decidir notificar no es haber entregado |

Las tres primeras están implementadas y medidas. **La cuarta está diseñada y no
construida** — su domicilio conceptual completo está en `19`, que es lo que cierra la
arquitectura con independencia de que el código exista.

> ✎ **2026-08-18:** el párrafo de arriba quedó superado — **las cuatro fronteras están
> implementadas y medidas**. La cuarta (notificación → entrega) se construyó y verificó
> el 2026-08-12/14 (docs 114/118) y desde ADR-019 el módulo además corre como servicio
> HTTP (doc 124). El `19` sigue siendo el domicilio conceptual; ahora con código real
> detrás.

## 5. El acople duro: el vocabulario canónico

`datasets` y `media-plane` comparten el **vocabulario canónico v2**: `person`, `helmet`,
`vest`, `bare_head` (más los atributos `has_helmet` / `has_vest` en la vista BENCH).

**Cambiar un nombre de clase o una condición obliga a mover los dos repos a la vez.** Es la
dependencia menos visible del proyecto y la que más fácil se rompe.

## 6. Cómo leer esta serie

1. **Este documento**, para la vista de conjunto.
2. **`15`** si vas a operar el sistema — desde ahí se dispara todo.
3. **`16` → `17` → `18`** para seguir el dato de punta a punta.
4. **`19`** para entender dónde termina la cadena y por qué esa parte no está construida.

**Para otras preguntas, otros documentos:**

| Pregunta | Dónde |
|---|---|
| ¿Cuánto dio? | Los cuatro índices de `e-ovrt_experimental-setup/results/` |
| ¿Qué capacidades se construyeron y con qué evidencia? | `operacion/97` |
| ¿Por qué se decidió así? | `decisiones/` + `decisiones/estado-de-implementacion-adrs.md` |
| ¿Qué está fuera de alcance? | `nucleo/10` |
| ¿Qué significa esta sigla? | `../13-glosario-y-convenciones-de-lectura.md` |

## 7. Dos convenciones que se confunden

**Las dos series de ADR.** `ADR-001…018` (tres dígitos) son del **proyecto**, en
`docs/decisiones/`. `ADR-0001…0013` (cuatro dígitos) son de la **serie local del
control-plane**, en `e-ovrt_control-plane/docs/decisions/`. **Al citar, decir la serie.**

**Los documentos históricos mandan por su banner, no por su cuerpo.** Un doc con banner ✎
o ⚠️ al tope se lee desde ahí: el banner dice qué quedó superado y qué conserva vigencia.
`historicos/01` y `historicos/11` son los relevamientos históricos que esta serie reemplaza —
siguen en su lugar con su número, porque moverlos rompería miles de referencias.

## Referencias

`15`, `16`, `17`, `18`, `19` (los cinco relevamientos) · `historicos/01` y `historicos/11` (históricos,
reemplazados) · `03-spec-plataforma-dos-caminos.md` · `05-integracion-media-control-bus-eventos.md` ·
`10` (alcance y exclusiones) · `13` (glosario) · `operacion/97` (capacidades) ·
`operacion/37` y `38` (bus y servicio del control-plane).

---

## Fuente: `docs/nucleo/19-cierre-arquitectura-ciclo-de-vida-alerta.md`

> SHA-256 del bloque: `4468e07e8c397994edcb9de2e0da7a499f029769ed856c7c5e50fe1e376be158`  
> Seleccion: documento completo.

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
>
> ✎ **2026-08-28 — cinco precisiones verificadas contra el código (`operacion/130` R-10 y R-20;
> informe `datos/130-relevamiento-pre-etapa-2/alert-distribution.md`), anotadas en sitio:**
> §4.6 (`DeliveryRecord` trae además `latency_mode` y `experiment_id`) · §5 (el broker de la
> **medición** del doc 118 fue **`amqtt 0.11.3`**; Mosquitto es el del **despliegue**; y el ledger
> deduplica del lado **publicador**, no las re-entregas broker→suscriptor) · §6 ("ninguna cifra
> sale de este módulo" está superado por el 118: p95 64,534 ms n=460) · §6.1 (el desfase está
> **resuelto**: el inicio de `t_alert-notification` es `ts_publish_ms` del envelope del bus).

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
y `delivered_at` (✎ 2026-08-28: también **`latency_mode`** y **`experiment_id`** — `operacion/130` R-20;
y los outcomes son **cinco**: `delivered / failed / skipped_duplicate / dead_letter / suppressed_cooldown`).

**Salidas por corrida:** `notifications.jsonl`, `dead_letter.jsonl` y
`distribution_summary.json` (conteos por outcome + agregados de `t_alert-notification`).

## 5. Por qué MQTT, y por qué es un ejemplo

MQTT es el canal **elegido para demostrar el mecanismo**, no una integración con un sistema
real de obra. El fundamento (doc 07 D5):

- **Peso mínimo** — un Mosquitto en el compose, sin infraestructura adicional. (✎ 2026-08-28:
  Mosquitto es el broker del **despliegue** (`infra/platform/`, sin build ejecutado); el broker
  con el que se **midió** la campaña del doc 118 fue **`amqtt 0.11.3`** — al citar la cifra,
  citar ese broker. `operacion/130` R-10.)
- **Estándar de integración IoT** — es la respuesta defendible a "¿cómo se conecta esto con
  el mundo?".
- **Medición limpia** — `t_alert-notification` sin la variabilidad de una API externa. Un
  canal tipo Telegram habría medido la latencia de un servicio ajeno al sistema.

**Y una consecuencia que no es opcional:** MQTT QoS 1 puede **duplicar entregas**. Por eso
el ledger no es un lujo de diseño — es requisito del canal elegido. Lo mismo valdría para
cualquier broker at-least-once.

> ✎ **2026-08-28 — precisión (`operacion/130` R-20):** el párrafo mezcla dos deduplicaciones.
> El **ledger deduplica del lado publicador** — la misma alerta procesada dos veces por el
> distribuidor (re-ejecución, replay) produce `skipped_duplicate`, con clave
> (`notification_id`, `channel`), `notification_id = sha1(alert_id)[:16]`. Las **re-entregas
> broker→suscriptor** propias de QoS 1 las deduplica **el consumidor** por `notification_id`
> del payload; el ledger no las ve. QoS 1 es el único valor admitido; topic `eovrt/alerts/<severity>`.

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
(✎ 2026-08-28: **superado** — el módulo está implementado, verificado (133 tests + 1 de
integración MQTT) y **medido**: `t_alert-notification` p95 **64,534 ms n=460** (doc 118), tramo
**bus de alertas → PUBACK QoS 1**, dos relojes de pared del mismo host; sostenido (2.ª+) 102,025
ms n=104; 1.ª entrega 49,869 ms n=356; cooldown del distribuidor 30 s, 376/836 suprimidas =
44,98 %. Sí sale una cifra del informe de este módulo. `operacion/130` §2.)

### 6.1 Un desfase que quien implemente va a chocar

El diseño de `historicos/06` §6.1 asume que el `NotificationEnvelope` se arma con un
**`confirmed_at_ms`** tomado de la alerta. **`control.alert.v1` no tiene ese campo.** Lo que
sí tiene es `timestamp_ms` (del evento que confirmó), `alert_registered_ms` y
`first_evidence_ms`. Al construir el envelope hay que decidir cuál de los tres es el
instante de confirmación —y esa decisión afecta directamente a `t_alert-notification`, que
es la métrica del tramo. Queda anotado acá para que se resuelva con criterio y no por
descarte.

> ✎ **2026-08-28 — RESUELTO (`operacion/130` §2 y R-10):** el instante inicial de
> `t_alert-notification` es **`ts_publish_ms` del envelope del bus de alertas** —el momento en
> que el control-plane publica la alerta confirmada—, y el final es `puback_wall_ms`:
> `t_alert-notification = puback_wall_ms − ts_publish_ms`. Por eso el tramo medido es
> **bus → PUBACK**, no "confirmación → PUBACK": **no arranca en la confirmación del patrón**
> ni usa `timestamp_ms`/`alert_registered_ms`/`first_evidence_ms`. Dos relojes de pared del
> mismo host, no monotónico, declarado. No se suma con otros tramos.

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

