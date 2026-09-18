# E-OVRT-VDP - paquete de etapa 5

> Generado el 2026-09-08. Etapa 5: seccion 17.5, evaluacion y validacion.

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
   verificados; texto base `90d`; el marcador D-E1-11 se borra en el proximo pase) · **§17.3 v1.4 · §17.4 v1.6 · §17.5 v1.3**
   con sus tres pases APLICADOS Y VERIFICADOS (textos base `90` / `90b` / `90c`) · **§17.1 v1.15
   (Etapa 2) CERRADA el 2026-09-03 con los SEIS pases mas el ciclo de reestructuracion 09-01/09-03
   (109 -> 37 titulos, -35,3 % de palabras, cero bajas de referencias; la numeracion de subsecciones
   CAMBIO — traducir con desarrollando/mapa-secciones-17-1-v1-15.md), y los
   Anexos C y D finales AL FINAL del propio documento** (texto base `90f`; documento limpio, con un
   comentario abierto del colega en 17.1.6; siguen los handoffs hacia
   17.3/17.4/17.5) · §17.6, §18 y §19 sin redactar. El texto base vigente de cada etapa es SIEMPRE su extraccion
   (`90d`/`90f`/`90`/`90b`/`90c`), nunca el placeholder del maestro, los borradores ni las fotos
   `96x` del informe v1.1 (superadas para §15, §16 y §17.1).
4. **D-E1-11 — inscripcion ante la AAIP: CERRADA el 2026-09-01** (decision del usuario,
   converge con el comentario C9 de la Etapa 1 v1.1): el informe NO adjudica el tramite de
   inscripcion — las salvaguardas de §16.6 son el recaudo documentado y la respuesta se
   prepara para la defensa. El espejo de §17.1 (D-E2-7) ya esta borrado (v1.8); el marcador
   de §16.6 se borra en el proximo pase de la Etapa 1. No reintroducir el tema en el texto.
   Constancia: `desarrollando/cierre-d-e1-11-aaip.md`.

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

- **Etapa activa:** 5 - Etapa 5: seccion 17.5, evaluacion y validacion.
- Este archivo contiene el texto vigente que se modifica y sus insumos de ajuste.
- No se trasladan resultados propios hacia secciones cronologicamente anteriores.
- Nombre propio de esta etapa (01-etapa-5-activa.md): regenerarla no pisa el paquete de ninguna otra etapa.

---

## Fuente: `docs/informe/entregable/desarrollando/archivado/correcciones-etapa-3-4-5-pase-3.md`

> SHA-256 del bloque: `fb6ecd18525c80a73bb110e7c86f40a17ef888baeb2fc5dd883a3ac5eb75acb6`  
> Seleccion: pase de cierre 3 (2026-08-22): su seccion D fija las restricciones que rigen la redaccion de la etapa 5.

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

## Fuente: `docs/informe/ajustes/09-pase-de-tablas-y-lectura-de-cierre.md`

> SHA-256 del bloque: `6bb3053b0b9e750faebf4ae48f0e5d2bf821647136bd3e5f3b79906440a224d3`  
> Seleccion: revision de cierre (2026-08-21/22): su seccion 2 es el plan de tablas del 17.5 (7 quedan, 6 a prosa, 3 al Anexo D, 1 fuera) y sus hallazgos de la seccion 3 estan RESUELTOS.

# 09 — Pase de tablas y lectura de cierre (2026-08-21)

- **Qué es:** una revisión de punta a punta del informe pedida por el usuario, con dos
  encargos: (a) confirmar que **todo está listo para redactar y cerrar**, y (b) sacar las
  tablas que no aportan y dejar **las justas y necesarias**.
- **Método:** relevamiento del entregable completo (las 81 tablas), del set de ajustes, de
  los redlines y del gobierno, más verificación por comando de lo que se afirma acá.
  Ninguna fila de este documento se escribió sin mirar el archivo.
- **Estatuto:** este documento **propone**; nada se aplica desde acá. Cada bloque tiene su
  casilla de decisión, como el doc 07.

---

## 0. El hallazgo que reencuadra el pedido

El informe tiene hoy **81 tablas numeradas** (61 en el cuerpo, 21 en los anexos, más el
glosario). Y de esas 81, **ninguna contiene un resultado medido por este proyecto**: son
literatura citada, inventario de datos o artefactos de diseño.

> **Todo el tramo experimental llega al informe sin una sola tabla previa.** Las 17 tablas
> de §17.5 —las que el pedido invita a recortar— serían **las primeras del documento que
> muestran lo que el trabajo midió**.

Eso invierte el problema. La sobrecarga de tablas es real, pero **no está donde parece**:
está en §15, §16, §17.1, §17.3 y los anexos, que acumulan 81 tablas de contexto y diseño.
La sección de resultados todavía no existe. Recortar ahí sería recortar la tesis.

**Criterio que se sigue en todo este documento, y que no invento — ya está firmado**
(D-P2-1, pase 2 de §17.3/§17.4, 2026-08-20):

> Una tabla se justifica cuando **se consulta, no se lee**: filas estrictamente paralelas
> sobre los mismos atributos, celdas cortas, y el valor está en comparar *entre* filas.
> Dos columnas = una lista con bordes · dos filas = una oración · una columna que dice lo
> mismo en todas las celdas sobra · celdas de más de ~120 caracteres = prosa en grilla.

Lo que este pase agrega es **aplicarlo donde todavía no se aplicó**: al resto del informe
y a las tablas de resultados que aún no se escribieron.

---

## 1. Veredicto de aptitud: ¿está todo listo para redactar?

**Sí para los insumos. No para el estado del documento.** El detalle importa porque los
dos bloques se confunden fácil.

### Listo y verificado hoy

| Insumo | Estado | Cómo se verificó |
|---|---|---|
| Datos experimentales | cerrados, sin frentes abiertos | acta `operacion/128` |
| Cifras citables | los 4 índices verifican | `96-verificar-indices.py` → «Todo verificado» |
| Materiales | 17 tablas + 6 figuras, todas con artefacto | figuras producidas 08-21 |
| Decisiones de redacción | D-A/B/C, D-P2-1, D1–D4 firmadas | docs 122, pase 1 y 2 |
| Aparato bibliográfico | **sano** — 144 referencias, 407 citas APA autor-año en el cuerpo | conteo sobre §15/§16 |
| Kit para los redactores externos | vigente y regenerable | `--check --etapa all` (arreglado hoy, ver §4) |

### No listo — y es el trabajo que falta

1. **Cero de las 109 unidades está aplicada al `.docx`.** Existe el relevamiento completo
   y, en varios casos, el texto listo para pegar; no existe la aplicación. §17.3 y §17.4
   son la excepción parcial: tienen el pase 1 aplicado (v1.1 / v1.2) y el **pase 2 escrito
   y sin aplicar**.
2. **§17.4, §17.5, §17.6 y §18 están vacías.** Es el 100 % del tramo experimental y el
   cierre. Es la mayor parte del trabajo de redacción que queda.

> ✎ **2026-08-28 — los puntos 1 y 2 son la foto del 08-21/22 y están VENCIDOS** (fuente
> `00-el-informe-hoy` 08-28; `operacion/130` §5): el 08-23 se aplicaron los **tres pases** a
> §17.3 (**v1.4**), §17.4 (**v1.6**) y §17.5 (**v1.3**, redactada bajo D-P3-6); el 08-28 cerró
> la **Etapa 1** (§15+§16 v1.0, 16 `AJ-1` + podas 01–11). Siguen vacías **sólo §17.6, §18 y
> §19**; la Etapa 2 (§17.1) arranca. El resto de este §1 (insumos listos) sigue vigente.
3. **Hay material "listo para pegar" con contenido vencido** (§3). Si se pega tal cual,
   entra al informe una afirmación falsa.
4. **Un redline no está saldado** por la tabla que debía saldarlo (§3).

---

## 2. §17.5 — las 17 tablas de resultados, una por una

Aplicación mecánica de D-P2-1 al inventario de `gobierno/99` §1. **Saldo: de 17
propuestas, 7 quedan como tabla en el cuerpo, 6 pasan a prosa, 3 van al Anexo D y 1 se
elimina.**

### 2.1 Quedan como tabla — son el capítulo

> ✎ **2026-08-28 — cómo quedó en §17.5 v1.3 (constancia, `docs-set.md` #29):** la sección
> tiene **6 tablas (62–67)**, organizadas **por pregunta de medición** (D-P3-6), no 1:1 con las
> 7 de esta lista: **62** selección de modelos sobre `bench_v3` (≈T-72) · **63** resultados de
> estado por persona (≈T-74) · **64** alerta por episodio en el Bloque A (≈T-68, ya a 8
> columnas) · **65** falsos positivos en el estrato B · **66** camino en vivo por densidad,
> integridad y tramo temporal (≈T-75, con T-85 absorbida) · **67** curva de capacidad del
> ajuste fino. **T-73** (AP por clase y estrato), **T-78** y **T-79** (composiciones) **no
> aparecen como tablas separadas** en v1.3 — sus cifras van en prosa o en la hoja de datos.
> Se deja constancia; no reabre el pase.

| Tabla | Por qué se queda | Ajuste que necesita |
|---|---|---|
| **T-68** campañas de Nivel B | Es *la* tabla del capítulo: el contraste entre filas **es** el experimento | ⚠ **recortar de 13 a ~8 columnas** (ver 2.5) |
| **T-72** selección de modelos sobre `bench_v3` | Sostiene la elección del campeón; matriz modelo × estrato genuina | — |
| **T-73** AP por clase y por estrato | La asimetría estructural es un hallazgo, no un anexo | — |
| **T-74** Nivel A: E-DIR vs E-IND con IC | Matriz de comparación con intervalos: se consulta | — |
| **T-75** latencia y tiempo real | Sostiene la afirmación de tiempo real | **absorber T-85** como una fila más |
| **T-78** composición del banco de clips | Metodología que el lector consulta al leer cualquier cifra | — |
| **T-79** composición de `bench_v3` por estrato | Ídem | — |

### 2.2 Pasan a prosa — por corolario 2 de D-P2-1 ("dos filas = una oración")

| Tabla | Qué contiene realmente | Qué gana en prosa |
|---|---|---|
| **T-76** integridad del acople EBE | tres hechos binarios (0 huecos de secuencia, paridad idéntica, cierre 1:1) | una oración afirmativa pesa más que tres celdas que dicen «sí» |
| **T-77** costo de una clase nueva | cuatro números (0 entrenamientos · 48 líneas · 9 minutos · AP 0,662) | es el argumento de extensibilidad: en prosa se lee como afirmación, en tabla como dato suelto |
| **T-83** Nivel A sobre video | cuatro números cuyo valor es el **contraste** (F1 0,031/0,018 en video contra 0,408/0,479 en imágenes) | el contraste se enuncia; una tabla de 2×2 lo esconde |
| **T-84** revisión ciega del GT | una proporción (5 de 7 declaraciones eran error de anotación) | **es un resultado de calidad de la referencia humana**, no una nota al pie: merece párrafo propio |
| **T-85** latencia de notificación | un solo número (p95 64,534 ms, n = 460) | una tabla de un dato no es una tabla; va como fila de T-75 |
| **T-82** estrato B (I1/I2) | dos episodios evaluables | 🔴 **el argumento más fuerte del pase**: la regla prohíbe rankear con n = 2, y **una tabla comparativa invita exactamente a ese error**. En prosa se enuncia lo robusto —la asimetría de falsos positivos 26 vs 323 (12×)— sin ofrecer un ranking que no se sostiene |

### 2.3 Van al Anexo D — el detalle exhaustivo, que ya tiene su lugar

El Anexo D («Métricas, instrumentación y bitácora experimental») existe y es el destino
natural. Mover ahí no es esconder: es separar lo que se **argumenta** de lo que se
**consulta**.

| Tabla | Por qué al anexo |
|---|---|
| **T-69** desglose por escenario P1–P9 | 9 filas × métricas: es material de consulta, no de lectura |
| **T-70** desglose por condición CR-01/CR-02 | dos filas; o se funde como agrupación dentro de T-68, o acompaña a T-69 |
| **T-71** eje de densidad R1–R6 | **FIG-B ya lo muestra**: la figura da la forma, el anexo los valores exactos |

> ⚠ **La regla que gobierna este movimiento, y que no se puede violar:** «se reporta por
> estrato y por escenario, nunca sólo el agregado» (limitación L5). Mover la tabulación
> exhaustiva al anexo la respeta **sólo si** en el cuerpo queda enunciado, en prosa, todo
> contraste por estrato que cambie una conclusión. Criterio explícito a aplicar:
> **si el estrato cambia la lectura, va al cuerpo; si sólo agrega precisión, va al anexo.**

### 2.4 Se elimina del informe

**T-81 — «ADR → dónde se declara en el informe»**. Es una tabla de navegación interna, y
los ADRs **no se mencionan en el informe** por la regla de autocontención. Es material de
trabajo del equipo, no del entregable. Se conserva donde está; no entra al capítulo.

### 2.5 El defecto de forma que hay que arreglar sí o sí

La tabla fuente de T-68 tiene **13 columnas** (`#` · `campaign_id` · Modelo · Prompts ·
Gran. · Recall · Prec. · F1 · `t_alert` · TTFD · SDR · FP neg. · Hallazgo). **A 16 cm de
ancho eso es ilegible.** Recorte propuesto, sin perder un dato:

- `campaign_id` → **a la nota al pie** (es donde la regla de verificabilidad lo pide).
- `Hallazgo` → **a la prosa** que rodea la tabla; es una columna de texto largo, o sea
  prosa en grilla por corolario 4.
- `Modelo` + `Prompts` → una sola columna «variante», porque sólo dos campañas se apartan
  de la combinación base.
- `SDR` y `TTFD` → **al Anexo D**. El SDR además arrastra la advertencia de que no se
  compara entre cadencias; sacarlo del cuerpo elimina de raíz la tentación.

Queda: **campaña · variante · granularidad · R · P · F1 · `t_alert` · FP negativos** — ocho
columnas, publicable, y el contraste entre filas sigue intacto.

```
DECISIÓN §2 → [x] acepto — ✎ 2026-08-28: EJECUTADA en §17.5 v1.3 (pase 3, 2026-08-23; ver ✎ en §2.1)  [ ] modifico  [ ] rechazo
```

---

## 3. Lo que no se puede pegar tal como está

Tres cosas que se filtrarían al informe si el material se usa sin revisar. **Esto es lo
que el pedido "que no se nos pase nada" tenía que encontrar.**

1. 🔴 **Contenido vencido en una tabla lista para pegar.** La tabla de capacidades y
   brechas del material de Etapa 3 declara, en su fila de fine-tuning, que «resta emitir
   la autorización y el RUN manual». Eso era cierto el 2026-08-13. Hoy **la jornada
   completa cerró**: T1 NO-GO, T2 NO-GO, T3 con causa técnica. Pegar esa fila mete una
   afirmación falsa en el informe. **Reescribirla con la curva de tres puntos.**
   ✅ **RESUELTO 2026-08-22:** la fila del `94` §8 se reescribió con la curva de tres
   puntos y ese §8 lleva banner de superado-como-texto-guía; para el `.docx` manda
   **E4-27** (pase 3), que además elimina el `[[PENDIENTE]]` de la Tabla 68. También se
   actualizaron los ecos en `05` (AJ-5.13), `04` (bullet E-04), `gobierno/99` (filas
   `ppe_siabar` y ADR-017) y `estado-de-implementacion-adrs` (fila 016).
2. 🔴 **Un identificador de clip retirado.** El ejemplo de evento de percepción del mismo
   material usa como `source_id` un clip que fue **retirado del banco**. El propio
   material lo marca con una advertencia sin resolver. Cambiar el ejemplo por un clip
   vigente antes de pegarlo.
   ✅ **RESUELTO 2026-08-22 por la opción (a) del `94` §1.3 (re-transcripción):** los
   ejemplos de `92` §2.2/§4.3/§5.2 y `94` §1.3/§1.4 ahora transcriben literalmente la
   unidad `frame_000229` de la corrida real de la campaña sobre **`a_p1_c02`** (clip
   vigente) y su alerta, reproducida por replay del control-plane y archivada en
   `operacion/datos/129-2026-08-22-bench-a_p1_c02-gdino-alerts.jsonl` (+ summary). Bonus:
   la unidad nueva contiene un `helmet` fuera de la región del sujeto — muestra la
   inferencia espacial de ausencia con mejor pedagogía que la anterior.
3. 🟠 **Un redline sin saldar.** El redline de registro de alcance exige que cada capacidad
   quede **anclada a su regla de exclusión**, «para que se lea como alcance declarado y no
   como omisión». La tabla que debía saldarlo **no contiene ni un solo código de
   exclusión**. O se agrega la columna, o se declara explícitamente que el anclaje se
   resolvió en otra sección — pero no puede quedar como está y darse por cerrado.
   ✅ **RESUELTO 2026-08-22 por la segunda vía, declarado en `93` R-13:** el anclaje es
   **sustantivo, no por código** — la columna de E-xx es imposible bajo la regla de
   autocontención (el informe no puede citar el doc 10). Cada fila de la Tabla 68 lleva
   su fundamento de exclusión en la columna de consecuencia, la prosa de §17.4.10
   desarrolla el núcleo-solo por evaluabilidad (D4/E4-17), y el pase 3 completa las dos
   filas que faltaban (enmienda a E4-22 y E4-27). El mapa código↔fila queda como
   trazabilidad interna en doc 10 / ADR-015 §3.

```
DECISIÓN §3 → [x] acepto — resuelto el 2026-08-22 (los tres ítems, ver las notas ✅ de arriba)
```

---

## 4. Las 81 tablas existentes: dónde está la grasa de verdad

Un pase anterior relevó la **forma** de todas las tablas y recomendó **no abrir** este
frente, con dos argumentos: que el costo de renumerar supera la ganancia, y que fuera de
§17.3 «ninguna de esas tablas presenta el problema de duplicación entre tablas vecinas».

**El segundo argumento no se sostiene, y el primero cambió de signo.** Aquel relevamiento
declaraba explícitamente ser «de forma, **sin** revisión de contenido». Hecha la revisión
de contenido, aparecen duplicaciones reales:

| Duplicación | Estado |
|---|---|
| «Umbrales orientativos por severidad» aparece **dos veces**, en §17.1.7.9 y en el Anexo D — mismo título, mismas filas, mismos valores; la del anexo es superconjunto | ✅ **verificado por comando** |
| Los dos backlogs de §17.3.17 comparten **esquema idéntico** de cinco columnas, y su propia columna `Prioridad` ya distingue lo que la partición en dos tablas pretende distinguir | ✅ **verificado por comando** |
| Cobertura por condición (§17.1.6.5) contra su gemela del Anexo C | 🟡 relevado, confirmar al aplicar |
| Síntesis de modelos OVD de §15.2.3.1 ⊂ la del Anexo A (6 filas contra 12) | 🟡 relevado, confirmar al aplicar |
| Jerarquía de métricas de §17.1.7.9 contra las tres tablas de detalle del Anexo D | 🟡 relevado, confirmar al aplicar |

Y el argumento del costo se invirtió: aquel pase dijo que, de abrirse, **debía hacerse
antes** que él para renumerar una sola vez. **Ese pase todavía no se aplicó.** La ventana
que se daba por cerrada sigue abierta, y es hoy.

### Pero la mayor parte se resuelve sola

**No hace falta un pase de tablas dedicado para §15 y §16.** Las unidades de poda ya
programadas eliminan o comprimen las secciones que contienen las tablas problemáticas: al
podar el bloque de streaming y servidores, el de MOT y el de convergencias, **sus tablas
caen con ellas**. Duplicar el trabajo en dos pases sería exactamente el error que el
manual advierte: corregir algo que después se elimina.

**Recomendación:** no abrir un pase de tablas separado. En cambio:

- **(a)** Incorporar D-P2-1 como criterio explícito **dentro de cada pase de sección**, que
  es como ya se aplican las podas y los ajustes.
- **(b)** Tratar aparte **sólo las duplicaciones verificadas**, porque no las resuelve
  ninguna poda: son tablas que sobreviven en dos lugares distintos. Eliminar una copia no
  pierde ningún dato y es la ganancia más barata del documento.
- **(c)** Proteger intactos los catálogos y contratos que el resto del documento referencia
  por número: matriz de evidencias normativas, catálogos de condiciones y patrones,
  decisiones arquitectónicas, fronteras informacionales, contratos mínimos, catálogo de
  prompts.

```
DECISIÓN §4 → [ ] acepto  [ ] modifico  [ ] rechazo
✎ 2026-08-28: la duplicación **Tabla 35 ↔ Anexo D** (y el criterio de tablas de §15/§16/§17.1/§17.3)
pasa al **pase de la Etapa 2** (`correcciones-etapa-2.md`, en preparación); §15/§16 ya se podaron en v1.0.
```

---

## 5. Ideas que nadie pidió y conviene considerar

1. **El desbalance tabla/figura es de 81 a 2.** El informe tiene ochenta y una tablas y
   **dos figuras**. Eso, más que la cantidad de tablas, explica por qué se lee denso: no
   hay ningún respiro visual en 127.000 palabras. Las seis figuras nuevas mejoran el
   tramo experimental, pero §15/§16/§17.1 siguen sin una sola. **Antes de sacar tablas de
   esas secciones, vale preguntarse cuál de ellas quiere ser una figura** — un esquema de
   la brecha entre literatura y problema, por ejemplo, resuelve en una imagen lo que hoy
   son cuatro tablas de «brechas» con el mismo encabezado.
2. **Las cuatro tablas de brechas son una sola tabla.** Hay cuatro tablas distintas con el
   encabezado «brecha · descripción · implicación» (OVD, seguimiento, ético-legal,
   transversal), 21 filas entre todas, y una de ellas ya se declara la integradora.
   Consolidarlas en una matriz con columna de dominio ahorra tres tablas y **mejora** el
   argumento: la convergencia de brechas es justamente lo que justifica el trabajo.
3. **La regla de estilo choca con la salida propuesta, y hay que elegir.** El brief dice
   «no usar viñetas donde el informe usa prosa; el capítulo 17 es mayormente prosa con
   tablas numeradas». Varias unidades del pase 2 convierten tablas **a viñetas**. Con el
   brief en la mano, la conversión por defecto debería ser **a prosa**, y las viñetas
   reservarse para enumeraciones genuinamente cortas y paralelas. Conviene decidirlo una
   vez, no tabla por tabla.
4. **El orden de aplicación importa más que la lista.** Aplicar el pase 2 de §17.3/§17.4
   antes de resolver §4 obliga a renumerar dos veces. Y aplicar cualquier poda de §15/§16
   después de escribir §17.5 obliga a revisar las referencias cruzadas. El orden barato es:
   duplicaciones verificadas → pase 2 → podas por sección → escritura de §17.4/§17.5/§17.6.
5. **La numeración conviene congelarla al final.** Con ~17 tablas saliendo y ~13 entrando,
   cualquier número escrito en prosa hoy se rompe. Mientras dure el pase, referirse a las
   tablas por su **título**, no por su número, y numerar en una única pasada al cierre.

```
DECISIÓN §5 → [ ] acepto  [ ] modifico  [ ] rechazo
```

---

## 6. Ejecutado hoy (no requiere decisión)

- **Arreglado el generador del kit.** Apuntaba a un archivo movido a `archivado/` y
  `--check --etapa all` fallaba, con lo que la puerta de cierre del kit no podía correrse.
  Ahora incluye el pase 1 (cuyas decisiones siguen rigiendo) **y** el pase 2, y verifica en
  verde con los ocho archivos de knowledge.
- **Aclarada la aparente contradicción entre dos reglas** que hoy pueden frenar a un
  redactor externo: la autocontención prohíbe mencionar documentación interna, y otra regla
  exige que toda tabla de resultados lleve su identificador de campaña o el digest del
  banco al pie. **No se contradicen:** la nota al pie identifica el *artefacto* (qué
  corrida, qué digest), nunca *dónde vive el archivo*. Queda registrado en el documento de
  Etapa 5.

---

## 7. Qué verifiqué corriendo el comando

| Afirmación | Verificación |
|---|---|
| 126.787 palabras escritas | `wc -w` sobre los seis archivos del entregable |
| 81 tablas, ninguna de resultados propios | relevamiento fila por fila del entregable completo |
| 2 figuras referenciadas en todo el informe | conteo de referencias «Figura N» |
| Aparato bibliográfico sano | 144 referencias · 407 citas autor-año en §15 y §16 |
| «Umbrales por severidad» duplicada | comparación de ambas tablas: mismo título y mismos valores |
| Los dos backlogs comparten esquema | encabezados idénticos de cinco columnas |
| T-68 tendría 13 columnas | encabezado de la tabla fuente |
| Las cifras citables verifican | verificador de índices en verde |
| El kit vuelve a verificar | `--check --etapa all` en verde tras el arreglo |

---

## Fuente: `docs/informe/entregable/90c-etapa5-texto-extraido.md`

> SHA-256 del bloque: `11fc4c6636e1c6573a8ddeac918ec8691485a006a147b0eae7a4892abf13ea09`  
> Seleccion: TEXTO BASE VIGENTE de la seccion 17.5: extraido el 2026-09-08 de la bajada del 09-08 con los pases 5, 5b y 5d ACEPTADOS por el usuario. ⚠ El archivo se llama **v1.5** pero su contenido es el de la v1.9: al renumerar, el numero retrocedio, y existe ademas una v1.5 historica DISTINTA (la base del pase 5). Citar la seccion por su estado, no por ese numero. Sin comentarios ni marcas: 4.913 palabras, 8 titulos, 5 tablas (61-65) y UNA sola figura (4.6, el fotograma con la alerta confirmada; §17.5 NO lleva figuras de datos por decision del usuario del 09-07). Redactada bajo D-P3-6 (por pregunta de medicion), con las ocho limitaciones restauradas al final de 17.5.7, las cifras verificadas contra los indices de results/ en la revision 5d (13 contradicciones corregidas) y los denominadores reales de las medias de latencia (21 clips para CR-01 y 7 para CR-02). **LA ETAPA 5 ESTA CERRADA**; §18 interpreta lo que esta seccion reporta, no la reescribe. No cambiar una palabra de fondo sin un pase nuevo explicito.

# 90c — Texto extraído del documento de trabajo: §17.5 Evaluación y Validación (bajada del 2026-09-08, nombrada v1.5 pero con el contenido de la v1.9: el número retrocedió al renumerar. Limpia, sin comentarios. ETAPA 5 CERRADA)

> **Extracción derivada (2026-09-08)** del `.docx`
> `informe/entregable/E-OVRT-VDP_Seccion_17.5_Evaluacion_y_Validacion_v1.5.docx`, **solo para búsqueda y cita**
> (mismo estatuto que el doc 90): al editar, se edita el `.docx`/Google Docs, nunca
> este archivo. Tablas y figuras pueden haber perdido formato; las figuras no se
> extraen y las ecuaciones no se convierten — quedan `⟦FIGURA: no extraída — ver el .docx⟧` y
> `⟦ECUACIÓN: no extraída — ver el .docx⟧` donde estaban. Regenerado con
> `herramientas/extraer_informe.py` (regla D-C del manual de aplicación).

---

### 17.5. Evaluación y validación del prototipo

#### 17.5.1. Encuadre y reglas de lectura

La evaluación informa cuánto produjo el prototipo bajo las condiciones experimentales definidas. Los resultados se organizan por pregunta de medición y distinguen tres niveles. La percepción sobre imágenes caracteriza al detector, el estado observable por persona evalúa la reconstrucción de una condición por sujeto, y la alerta temporal por episodio representa a la plataforma completa. Las mediciones de percepción, estado por persona y alerta por episodio pertenecen al Escenario A, sobre material congelado y relectura por archivo, y las de tiempo real al Escenario B, sobre captura continua.

Rigen las reglas de lectura fijadas en la sección 17.1.7.3. Cada cifra se acompaña de la combinación que la produjo, del material o estrato sobre el que se calculó y de su denominador. Precisión, recall y F1 se calcularon sólo sobre casos positivos con referencia aplicable, los materiales negativos se analizaron por conteo de falsos positivos, las re-alertas se contabilizaron aparte y los percentiles de tramos con relojes distintos no se sumaron. Los nombres abreviados de esta sección siguen al marco de métricas, con dos equivalencias. AP50 y mAP50 designan la precisión media a solapamiento 0,5 que el marco escribe AP@0,5, y la latencia de alerta es el intervalo que el marco llama t_alert-system. La latencia de alerta mide el intervalo entre el inicio del episodio anotado y su alerta confirmada, y la cobertura del episodio, que las tablas abrevian SDR, expresa qué proporción del tiempo con la condición activa mantuvo evidencia correcta.

El banco temporal congelado comprendió 47 clips, distribuidos en 32 positivos y 15 negativos, con 37 episodios de referencia. Lo integran 34 clips de un bloque de rodaje guionado y 13 de un estrato de obra real no guionada. El estrato de obra real no guionada se mantuvo separado y no se utilizó para ordenar granularidades cuando su denominador efectivo fue insuficiente. La referencia temporal fue humana y quedó congelada antes del reporte.

Una métrica se trató como computable sólo cuando existieron referencia, reloj e instrumentación compatibles con su definición. Cuando faltó alguno de esos elementos, el resultado se declaró no aplicable o no interpretable en lugar de convertir la ausencia de medición en un cero.

#### 17.5.2. Percepción sobre imágenes

La primera pregunta examinó la capacidad perceptiva de las combinaciones sobre un banco congelado de 6.477 imágenes y 55.165 anotaciones. El material se dividió en tres estratos independientes de 147, 1.330 y 5.000 imágenes, correspondientes a obra curada, a obra con mayor cobertura de chaleco y a una fuente con clase nativa de cabeza descubierta. El tercero aportó el 77 % del banco, de modo que el agregado se leyó siempre junto con el desglose por estrato.

La Tabla 61 muestra que la combinación gdino-tiny-560 alcanzó el mAP50 más alto en el agregado y en el núcleo curado, mientras que gdino-base-560 produjo el recall más alto de CR-01 por evidencia directa. El veredicto se formuló entonces por combinación. El primer perfil se retuvo como configuración operativa por un criterio fijado antes de leer los resultados, y el segundo como contraste especializado para cabeza descubierta y chaleco. No se estableció una jerarquía universal entre modelos. Las dos comparten resolución de entrada y umbrales, que declara la sección 17.4.4, y difieren en el tamaño del perfil.

**Tabla 61**

*Resultados de percepción por combinación en el banco congelado*

| **Combinación** | **mAP50 agregado (n = 6.477 imágenes)** | **mAP50 obra curada (n = 147 imágenes)** | **Recall de CR-01 por evidencia directa (n+ = 5.313)** | **Veredicto por combinación** |
| --- | --- | --- | --- | --- |
| gdino-tiny-560 | 0,551 | 0,503 | 0,308 | Retenida como perfil operativo por liderar el mAP50 en las dos escalas reportadas. |
| gdino-base-560 | 0,525 | 0,474 | 0,599 | Retenida como contraste de mayor cobertura de cabeza descubierta y chaleco. |
| yoloe-26x | 0,442 | 0,405 | 0,000 | Ciega a la cabeza descubierta, de modo que no sostiene la formulación directa. Su límite para el núcleo es el chaleco, con AP 0,182 en obra curada frente a 0,520 del perfil operativo. |

***Nota****.* El denominador del agregado es el banco completo. El recall de CR-01 se informa sobre 5.313 positivos, el conteo de la referencia con la que se ejecutó la campaña. Una corrección posterior de esa referencia lo dejó en 5.308 y la medición no se repitió. Esa columna cuenta sólo detecciones de cabeza descubierta, de modo que mide la formulación directa. El núcleo opera con la indirecta, que deriva la ausencia desde persona y casco, y su capacidad para la condición no se lee en esta columna.

La especialización del perfil base también apareció en chaleco, con AP 0,582 frente a 0,520 del perfil operativo sobre el estrato de obra curada. Para el perfil operativo, persona y casco se mantuvieron entre 0,70 y 0,89 de AP en los dos estratos públicos, mientras que chaleco quedó en 0,553 y 0,520 en los dos estratos que anotan esa clase. La asimetría no dependió de una única fuente, porque se sostuvo en ambos.

La familia YOLOE presentó una limitación distinta. Sus cuatro variantes produjeron AP 0,000 para bare_head, la clase de cabeza descubierta, sobre el banco anterior al congelado, y la variante mayor repitió el cero sobre el estrato que anota esa clase de forma nativa. Aunque resultó adecuada para rutas de mayor velocidad, esa ceguera la volvió inservible para la formulación directa de CR-01 en la configuración evaluada.

La extensibilidad semántica se ejerció sobre una clase nueva, cuyo costo de incorporación informa la sección 17.4.8. La clase alcanzó AP50 de 0,662 sobre 99 cajas de referencia sin ninguna corrida de entrenamiento. El costo reducido no eliminó la necesidad de validación semántica. Sobre el mismo material, la palabra vehicle no produjo ninguna detección cuando acompañó a machinery en el vocabulario y, aislada, produjo 118 cajas con AP 0,026, porque el modelo la resolvió sobre la maquinaria misma.

#### 17.5.3. Estado por persona

El nivel intermedio evaluó si la evidencia perceptiva permitía determinar el estado observable de cada persona. La calibración se realizó sobre una mitad del material y las métricas sobre la otra, con IoU mayor o igual que 0,5. La partición en mitades se registró con su semilla y fue la misma para todos los brazos, de modo que ninguna imagen que ajustó un umbral entró después en la medición. Se compararon E-IND, la estrategia indirecta que reconstruye la ausencia desde evidencia positiva, y E-DIR, la formulación directa retenida para el contraste. La medición sobre video abarcó 17 clips de obra real, los 13 del estrato de obra real del banco temporal y 4 de un piloto anterior, evaluados al nivel del estado por persona sobre su referencia de atributos, submuestreados a 2 Hz y sin calibración de umbrales, con el punto de operación desplegado, y no incluyó el motor de patrones. La Tabla 62 reúne los resultados.

**Tabla 62**

*Resultados de estado por persona*

| **Material y condición** | **Resultado E-IND** | **Contraste E-DIR** | **Denominador** | **Lectura** |
| --- | --- | --- | --- | --- |
| Imágenes, CR-01 | F1 0,546 | F1 0,188 | n+ = 2.487 | Los intervalos de confianza no se solaparon. |
| Núcleo curado, CR-01 | F1 0,408 | F1 0,189 | n+ = 28 | La ventaja se conservó en el estrato objetivo. |
| Imágenes, CR-02 | F1 0,479 | F1 0,418 | n+ = 82 | Un único estrato; el resultado no cerró la condición. |
| Video de obra real - CR-01 | P 0,016 · R 0,467 · F1 0,031 | No corresponde a esta medición | n+ = 92 de 10.356 cuadros con persona | La caída provino de precisión, no de recall. |
| Video de obra real - CR-02 | P 0,009 · R 0,318 · F1 0,018 | No corresponde a esta medición | n+ = 170 de 10.361 cuadros con persona | La misma frontera de juzgabilidad dominó el resultado. |

La estrategia directa no se comportó como un detector estable del estado, sino como un recuperador de casos omitidos por la estrategia indirecta. Recuperó el 18,5 % de esos casos, equivalentes a 155 de 840, pero lo hizo a costa de precisión. Esa relación explica por qué la estrategia no se adoptó aunque aportara evidencia complementaria en un subconjunto.

La medición sobre 17 clips de obra real mostró un cambio de régimen. La caída del F1 provino de la precisión y no del recall, por acumulación de falsos positivos sobre personas cuyo estado no podía determinarse visualmente. El evaluador excluyó del denominador 1.414 cuadros con persona no juzgables para CR-01, aquellos en los que el anotador no pudo determinar el estado, y 1.409 para CR-02, y contabilizó como falso positivo cualquier predicción emitida sobre ellos.

Esa frontera tiene al menos tres ejes y ninguno de los tres, por sí solo, anticipa si el material es evaluable. La escala ordena dentro de un mismo régimen de luz. En los clips diurnos del estrato de obra real, la proporción de sujetos detectados a los que se asocia un chaleco pasa de alrededor del 10 % en la banda de 80 a 120 píxeles de altura a entre 63 y 73 % en la banda de 220 a 320, y en el bloque de rodaje, con medianas de altura por encima de 700 píxeles, esa misma asociación se sostuvo entre 96 y 100 %. La iluminación desplaza la curva entera, porque en el clip nocturno del estrato la banda de 80 a 120 píxeles cae a 0 % y las siguientes, hasta 320, quedan entre 6 y 13 %. Y la oclusión invierte el orden de los dos ejes anteriores, ya que el clip con los sujetos más grandes del conjunto, con mediana de 370 píxeles, quedó entre los peores resultados con F1 0,084 sobre una cuadrilla apiñada en la que el 58,5 % de las personas aparece solapada con otra. Tampoco la juzgabilidad humana anticipa el rendimiento del sistema, porque el clip con la segunda proporción más baja de cuadros no observables para el anotador rindió el peor F1 del conjunto.

#### 17.5.4. Alerta por episodio contra la referencia temporal humana

La alerta por episodio constituyó el resultado principal porque integra percepción, asociación, histéresis, estado temporal y registro de alerta. El bloque de rodaje guionado reunió 34 clips y 35 episodios de referencia, 28 de CR-01 y 7 de CR-02. Treinta y cuatro episodios resultaron evaluables y uno quedó censurado con causa declarada, porque su duración no permitía que una alerta lenta ocurriera dentro del clip, y cuatro clips fueron negativos. La Tabla 63 reúne las combinaciones ejecutadas sobre ese material, cada una con una sola variable cambiada respecto de la línea de base.

**Tabla 63**

*Alerta por episodio en el bloque de rodaje guionado*

| **Combinación** | **Recall** | **Precisión** | **F1** | **t_alert en ms (n de episodios confirmados)** | **SDR** | **FP en 4 negativos** | **Veredicto local** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Núcleo E-IND, escena | 0,824 | 0,757 | 0,789 | 5.327 (n = 28) | 0,698 | 0/4 | Línea de base de la plataforma. |
| Contraste base-560 | 0,735 | 0,676 | 0,704 | 4.899 (n = 25) | 0,819 | 0/4 | Mayor SDR, menor F1 que el perfil operativo. |
| E-DIR de extremo a extremo | 0,176 | 0,146 | 0,160 | 6.611 (n = 6) | 0,210 | 2/4 | Vetada por precisión. |
| E-HYB por disyunción | 0,353 | 0,255 | 0,296 | 6.956 (n = 12) | 0,738 | 2/4 | Ejecutada y refutada. |
| Núcleo E-IND, sujeto | 0,971 | 0,892 | 0,930 | 5.236 (n = 33) | 0,698 | 0/4 | La identidad elevó F1 sin cambiar las detecciones. |
| Vocabulario nativo bare_head | 0,382 | 0,371 | 0,377 | 3.919 (n = 13) | 0,940 | 3/4 | Alerta temprana, con mayor costo en falsos positivos. |

***Nota****.* Las métricas temporales se calcularon sobre 34 episodios evaluables de 35 en el bloque de rodaje, y el número entre paréntesis de la columna de latencia es la cantidad de episodios confirmados, mientras que la media se promedia por clip con alerta confirmada, un conteo menor cuando un mismo clip contiene las dos condiciones. Los falsos positivos se cuentan sobre los cuatro clips negativos y no incluyen re-alertas.

La histéresis rescató evidencia intermitente. CR-02 confirmó sus 7 episodios, con recall 1,000 y SDR 0,281, aunque requirió una latencia de alerta de 8.572 ms frente a 4.314 ms para CR-01. Las dos medias se promediaron por clip con alerta confirmada, siete en CR-02 y veintiuno en CR-01. La diferencia fue coherente con ventanas de confirmación de 7,0 y 4,0 s. Una detección sostenida sólo durante una fracción del episodio pudo producir una alerta correcta cuando acumuló evidencia suficiente dentro de la ventana. La Figura 4.6 muestra un fotograma con la alerta ya confirmada. Las referencias por severidad de la sección 17.1.7.5 no se usaron como criterio de aceptación, porque el propio protocolo las condiciona a una recalibración previa que esta evaluación no realizó, y sus valores se leen como dato.

**Figura 4.6**

*Fotograma con alerta confirmada de CR-01*

⟦FIGURA: no extraída — ver el .docx⟧

**Nota.** Fotograma del clip a_p1_c04 del bloque de rodaje a los 8,5 s, en la corrida de línea de base, con la alerta emitida a los 7,3 s y el motor en estado sostenido. El casco visible sobre la mesa, que el detector marca en cuadros vecinos, no suprime la condición, porque CR-01 se evalúa sobre la región del sujeto y no sobre la escena.

La identidad temporal fue la capa con mayor aporte medido dentro del banco. Con las mismas detecciones, la granularidad por sujeto elevó el F1 de 0,789 a 0,930, una diferencia de 0,141 sobre los 34 episodios evaluables. En el escenario de mayor dificultad el resultado pasó de 0,400 a 1,000, es decir de dos episodios confirmados sobre cinco a los cinco. La mejora no provino del detector, sino de evitar que la evidencia de personas distintas se mezclara dentro de un mismo estado de escena.

El vocabulario activo también se comportó como una variable experimental. Sobre la combinación de contraste base-560, un ensayo posterior mantuvo fijos el modelo, el evaluador, el conjunto de patrones, la referencia y los tiempos, y sumó al vocabulario una sola palabra, la de cabeza descubierta. El F1 por episodio bajó de 0,704 a 0,622, el recall de 0,735 a 0,676 y la precisión de 0,676 a 0,575. La interacción entre términos de un mismo vocabulario no resultó despreciable, de modo que dos configuraciones sólo son comparables cuando declaran el vocabulario completo que vieron.

El estrato de obra real no guionada se informó por separado y comprendió 13 clips. Una revisión ciega encontró que 5 de las 7 declaraciones de episodio eran errores de anotación por sobre-declarar estados que no resultaban observables, y dejó 2 episodios evaluables y 11 clips negativos. Ese denominador impidió ordenar granularidades. El resultado robusto del estrato fue la asimetría de falsos positivos, 26 con granularidad de escena frente a 323 con granularidad por sujeto sobre los mismos 11 clips negativos. Esa asimetría es el ΔFP_tracking que adopta el marco de métricas de la sección 17.1.7, y su signo es el contrario al del riesgo que la sección 17.1.10 anticipaba, que el seguimiento agregara complejidad sin reducir falsas alarmas.

Sobre el único tramo continuo de cumplimiento, de 6 minutos y 9,6 segundos, los conteos fueron 3 falsos positivos con granularidad de escena y 190 con granularidad por sujeto. Las tasas de 29,2 y 1.850,8 falsas alarmas por hora se derivan de esa exposición de 0,1027 h y se informan como magnitudes derivadas, nunca como cota operativa, porque la exposición disponible estuvo casi treinta veces por debajo de la necesaria para sostener una.

#### 17.5.5. Tiempo real

La evaluación en vivo examinó qué parte del resultado temporal sobrevivía cuando la densidad de procesamiento descendía respecto de la evidencia disponible. El banco se representó a 30 fps, mientras que el camino en vivo entregó entre 1,16 y 4,42 fps. Para cubrir esa franja, los 34 clips del bloque de rodaje se remuestrearon de manera pareada a cuatro densidades, de 30 a 1,15 cuadros por segundo. La Tabla 64 reúne esas mediciones junto con las de integridad y latencia por tramo.

**Tabla 64**

*Resultados del camino en vivo por densidad, integridad y tramo temporal*

| **Eje** | **Condición o material** | **Resultado** | **Denominador** | **Lectura** |
| --- | --- | --- | --- | --- |
| Densidad | Referencia del banco, 30 fps | Escena 0,789 · sujeto 0,930 | n = 34 episodios evaluables | Punto de partida de la comparación. |
|  | Techo en vivo, aproximadamente 4,29 fps | Escena 0,794 · sujeto 0,866 | n = 34 episodios evaluables | La ganancia por identidad se conservó. |
|  | Intermedia, aproximadamente 2,00 fps | Escena 0,738 · sujeto 0,875 | n = 34 episodios evaluables | La pérdida no avanza de manera uniforme. |
|  | Peor caso, aproximadamente 1,15 fps | Escena 0,646 · sujeto 0,742 | n = 34 episodios evaluables | La restricción redujo ambos resultados sin invertir el orden. |
| Identidad | Cuatro densidades medidas | Ganancias de F1 +0,141 · +0,072 · +0,137 · +0,096 | n = 4 densidades sobre 34 clips; remuestreo pareado por clip | El intervalo empírico excluyó el cero en las cuatro condiciones. |
| Integridad | Relectura frente a transmisión | 0 eventos perdidos · paridad byte a byte verificada en una corrida y protegida por prueba automatizada | n = 6 corridas del rodaje para los eventos. n = 1 corrida para la paridad | El transporte no alteró la evidencia. |
| Latencia | Sobrecarga de la plataforma con detector simulado, en diferido | p50 14,7 - p95 31,8 ms | n = 20 unidades | Costo propio de la cadena sin inferencia, dentro del presupuesto de la sección 17.1.7. |
| Latencia | Detector open-vocabulary en vivo | p95 630–890 ms | n = 47, 93 y 55 unidades procesadas en las tres corridas en vivo | Fuera del presupuesto; la corrida lo declaró. |
| Captura | Antes del retiro de la unidad | 202–217 ms | medianas por corrida; n = 47 a 295 unidades procesadas en cada una de las seis corridas | No está incluida en el tramo anterior. |
| Alerta | CR-01 en vivo | 7 alertas: 4,1–4,6 s | n = 7 confirmaciones | Ventana: 4,0 s. |
| Alerta | CR-02 en vivo | 3 alertas: ≥ 7,1 s | n = 3 confirmaciones | Ventana: 7,0 s. |
| Canal | Bus de alertas a confirmación del canal | p95 64,534 ms · sostenido 102,025 ms | n = 460 · sostenido n = 104 | Tramo separado; no se suma a la alerta del sistema. |

*Nota.* Los percentiles pertenecen a tramos con relojes distintos y no se suman. El tramo desde el retiro de la unidad comienza en el dequeue, no en la captura de la escena.

La cobertura del episodio no se comparó entre cadencias porque depende de cuántas unidades sobreviven al muestreo. Tampoco se comparó la latencia agregada entre densidades sin controlar la supervivencia, porque los episodios que no alcanzan a confirmar desaparecen del promedio y lo sesgan. Entre los episodios supervivientes, el costo de bajar la densidad fue de 0,7 a 1,3 s sobre ventanas de 4 a 7 s, medido sobre 21, 20 y 16 episodios comunes a las cadencias comparadas. Entre la densidad del banco y el techo del camino en vivo el resultado por escena no cambió de manera apreciable y el resultado por sujeto perdió 0,064, mientras que en la densidad más baja la caída ya alcanza 0,143 y 0,188 respectivamente. Con 34 episodios evaluables, las diferencias del orden de un episodio, 0,029 de recall, quedan dentro de la resolución del banco y no se leen como orden.

La medición confirmó además la separación entre captura, procesamiento y distribución. Los tres tramos corresponden a relojes distintos y por eso sus percentiles no se suman. El del tramo de distribución describe el intervalo desde el bus de alertas hasta la confirmación del canal, y no la latencia completa de la plataforma.

#### 17.5.6. Caminos probados y no adoptados

Los caminos no adoptados se evaluaron contra criterios fijados antes de leer sus resultados. La estrategia directa quedó descartada por un veto de precisión, cuyo umbral de 0,5 se fijó de antemano en el pre-registro de la comparación de estrategias y quedó muy por encima del valor obtenido. La brecha que ya mostraba en el estado por persona se amplió al atravesar el motor de patrones.

La fusión híbrida por disyunción fue ejecutada y refutada, porque el recall descendió respecto del núcleo indirecto en lugar de crecer. La unión de evidencia no resultó monótona dentro del motor de patrones, ya que las detecciones más tempranas desplazaron confirmaciones fuera de la ventana de referencia. La variante por conjunción no se ejecutó, porque no podía medirse contra el banco sin romper la comparabilidad de las seis combinaciones. La familia MM-Grounding-DINO se integró por el mismo mecanismo de adaptación y se archivó durante la selección de modelos, sobre el banco anterior al congelado, de modo que no tiene cifra comparable en esta sección. Una de sus variantes no aportó ventaja en ninguna dimensión evaluada, otra entregó cajas degeneradas con origen en el punto de control publicado y no en el adaptador que las integró, y la tercera localizó mal con geometría normal.

La rama comparativa de ajuste fino se cerró como una curva de capacidad, con criterios y expectativas registrados antes de cada evaluación, y sus cifras se mantuvieron separadas de las del núcleo sin entrenamiento. La Tabla 65 recorre sus tres puntos.

**Tabla 65**

*Curva de capacidad de la rama comparativa de ajuste fino*

| **Punto o tramo** | **Resultado de ganancia** | **Retención y comportamiento** | **Veredicto** |
| --- | --- | --- | --- |
| Línea base sin ajuste | AP50 bare_head 0,0000 · recall de CR-01 por evidencia directa 0,0002 | Referencia previa a los tramos entrenados. | Punto de partida. |
| Primer tramo entrenado | AP50 bare_head 0,0455 · recall de CR-01 por evidencia directa 0,2089 | Quedó a 0,0045 del umbral de AP50 0,05 y redujo person de 0,7843 a 0,6932 (−11,62 %), con tope de 10 %. | Veredicto negativo pre-registrado; checkpoint no adoptado. |
| Segundo tramo entrenado | AP50 bare_head 0,0909 | Detención temprana 16/60, mejor época 1; person de 0,7843 a 0,3943 (−49,7 %) y mAP50 en dominio de 0,4193 a 0,2374 (−43,4 %); retención open-vocabulary 0,4347 a 0,1247 (−71,3 %) · n = 5.000 imágenes de validación de COCO 2017. | Veredicto negativo pre-registrado; checkpoint no adoptado. |
| Tramo adicional | No corresponde | Cerrado con causa técnica antes de producir una comparación interpretable. | Sin checkpoint y sin nuevo brazo contra el banco. |

***Nota****.* Los puntos medidos pertenecen a una rama comparativa separada. Las métricas en dominio de la línea base y de los dos tramos entrenados se calcularon sobre el banco congelado de 6.477 imágenes. El primer tramo agregó principalmente recall y el segundo, AP, de modo que no existe una combinación ajustada universalmente superior. Los tres puntos corresponden a la variante s de YOLOE-26. El primer tramo entrenó sólo la proyección de clases, 3.096 parámetros, y el segundo el detector completo con las rutas de prompt congeladas, 10,35 millones. La retención open-vocabulary se midió sobre un material ajeno al dominio, distinto del estrato de 5.000 imágenes del banco.

El segundo tramo duplicó el AP50 de cabeza descubierta respecto del primero, pero colapsó durante el entrenamiento y falló las dos retenciones. El patrón conjunto mostró que el límite no fue capacidad de cómputo sino estructura experimental, con 2.946 imágenes de ajuste frente a 10,35 millones de parámetros, un conjunto cuya composición, regla de partición y configuración de entrenamiento declara la sección 17.4.7. Ningún checkpoint se adoptó como modelo de servicio, y los veredictos negativos se conservaron como resultados pre-registrados y no como trabajo pendiente.

#### 17.5.7. Lo no ejecutado y lo no implementado

Las condiciones de Nivel 2 y Nivel 3 no se implementaron en el núcleo evaluativo porque el material disponible no aportaba verdad de terreno del dominio ni evaluadores relacionales, zonales o de trayectoria que pudieran validarse. Incorporarlas habría producido capacidades sin medición defendible y habría confundido extensión arquitectónica con resultado experimental.

Las métricas formales de seguimiento multiobjeto tampoco se calcularon, porque faltó una referencia de identidad apta para ese propósito. La exclusión no alcanzó a la capacidad de identidad temporal, que sí fue implementada y medida por su efecto sobre la alerta. La ganancia informada más arriba y su persistencia en las cuatro densidades pertenecen a esa capacidad y no a una métrica de seguimiento.

La preselección liviana en el dispositivo de captura fue implementada para la fuente propia y caracterizada mediante una comparación pareada. Descartó el 87 % de las unidades antes de abandonar el dispositivo, 206 de las 236 que vio la compuerta, frente a las 277 que procesó la rama sin preselección, y permaneció deshabilitada en todas las corridas evaluativas. La exclusión fue deliberada, porque un filtro de cuadros sin persona habría suprimido la evidencia sostenida que la medición de falsas alarmas debía observar y habría superpuesto el error de un detector auxiliar sobre la cadena evaluada.

Tampoco se sostuvo una cota operativa de falsas alarmas. Para hacerlo se requerían aproximadamente 3 h de cumplimiento anotado, mientras que la exposición continua disponible fue de 0,1027 h. La tasa horaria se reportó como derivación observacional, pero el material no habilitó una afirmación poblacional.

Finalmente, la comparación temporal directa entre una fuente en vivo y su reproducción desde clip se declaró no interpretable. Sin un ancla común entre el reloj de pared y el tiempo del medio, el emparejamiento habría mezclado desfases instrumentales con el comportamiento de la plataforma.

El sub-experimento formal que evaluaba cada prompt en aislamiento y dentro del vocabulario completo no se ejecutó sobre las combinaciones finalistas. La pregunta que lo motivaba quedó respondida por el contraste de variable única informado más arriba, que midió el costo de sumar un término al vocabulario activo.

El marco de métricas admite además medidas que esta evaluación no reporta, y su estado se declara en lugar de omitirse. El tiempo hasta la primera detección se computó en todas las campañas y no se informa aquí, porque la comparación entre combinaciones se resolvió con la latencia de alerta, que es la que integra el motor de patrones. La precisión media promediada sobre el rango de umbrales de solapamiento quedó sin computar, porque la lectura se fijó en un único umbral. El percentil 99 de latencia se computó por corrida y no se consolidó como resultado comparativo, porque las corridas en vivo procesaron entre 30 y 295 unidades, muy por debajo de lo que ese percentil requiere. El consumo de memoria del acelerador se registró por corrida y no se consolidó como resultado comparativo, porque describe al perfil cargado y no a la combinación evaluada. Los benchmarks públicos de seguimiento multiobjeto previstos en la estrategia de datos no se ejecutaron, por la misma falta de referencia de identidad que excluyó a sus métricas. La curva de falsos positivos en función de la duración de la ventana, que la sección 17.1.5.2 prevé como eje de la calibración empírica, no se ejecutó, y las ventanas se usaron con sus valores de protocolo.

Ocho limitaciones acotan la lectura de todo lo anterior. La tasa de falsas alarmas por hora no sostiene una cota operativa. La referencia temporal no tuvo doble anotación ni medida de acuerdo entre anotadores. Los bordes de episodio se adjudicaron por criterio único en seis clips. El material guionado proviene de un solo bloque de rodaje, y la medición sobre obra real precisó esa limitación sin levantarla, porque caracteriza por mecanismo dónde el sistema deja de ser evaluable en lugar de validarlo sobre obra real. Los escenarios quedaron desbalanceados, de modo que todo resultado se reporta por estrato además del agregado. El seguimiento no tiene métricas formales en obra real con multitud, aunque un clip con 127 personas mostró la fragmentación de identidades que explica la precisión por sujeto de ese estrato. Una de las fuentes de imágenes conserva licencia parcial. Y la condición de chaleco no quedó cerrada al nivel del estado por persona.

---

## Fuente: `docs/informe/entregable/96e-informe-v11-cierre-anexos-referencias.md`

> SHA-256 del bloque: `3e2abeb147d1a11e40d229753a6266af93231295b7dd966989486855c438b2f1`  
> Seleccion: placeholder de la seccion 17.5 en el maestro: sigue vacio porque el documento de trabajo todavia no se integro.

### 17.5. Evaluación y validación del prototipo

[Agregado futuro correspondiente a la Etapa 5]

---

## Fuente: `docs/informe/ajustes/05-etapa-5-evaluacion-y-validacion.md`

> SHA-256 del bloque: `8253b49a08b0910fe426794431c5a79660fc812b45e0d57364b5e25ba2c1dfd6`  
> Seleccion: documento completo.

# Etapa 5 — §17.5 Evaluación y validación del prototipo

> ✅ **Estado (✎ 2026-09-04): CUATRO pases. §17.5 v1.4 entregada con sugerencias, a aceptar por el
> usuario.** El pase 4 (`entregable/desarrollando/correcciones-etapa-5-pase-4.md` (fuente: `docs/informe/entregable/desarrollando/archivado/correcciones-etapa-5-pase-4.md`),
> E5-01…E5-11) consolidó el capítulo sin recalcular ninguna de las 185 cifras verificadas: 9 → 8
> títulos, 6 → 5 tablas renumeradas **61–65**, dos puntos 15 → 0 y punto y coma 16 → 0.
> **`AJ-5.14` quedó APLICADA** (el contraste 0,704 → 0,622 en §17.5.4 y la no ejecución del
> sub-experimento en §17.5.7), **§17.5.8 se eliminó** por pedido del usuario y **las ocho
> limitaciones pasaron a declararse** al cierre de §17.5.7, que es lo que `AJ-5.05` exigía y ninguna
> sección hacía. Dos reparaciones de hecho: la celda vacía de la tabla de tiempo real y el
> presupuesto de latencia, que ahora remite a §17.1.7 en vez de declarar una cifra propia.
> **Lo que sigue es registro histórico.**
>
> *Gantt ID 4 — "Evaluación y validación", 12/06/26 – 10/07/26.*
>
> ✅ **Estado (✎ 2026-08-23): la sección está REDACTADA bajo el esquema temático de D-P3-6
> y verificada** (185 cifras contra la hoja de datos, cero inventadas, cero marcadores de
> cifra) — documento de trabajo `§17.5 v1.3` en `entregable/desarrollando/`, texto base en
> `entregable/90c-etapa5-texto-extraido.md`, tablas 62–67. Lo que queda: revisión del autor,
> insertar las figuras y la integración al maestro. Las fichas `AJ-5.x` ya fueron
> incorporadas; se conservan como criterio de lectura.
>
> ⏳ **2026-09-02 — SE REABRE UN CONTENIDO: `AJ-5.14`.** Al reestructurar §17.1.5 (Etapa 2)
> apareció que su eje de composición del vocabulario activo **promete un contraste que §17.5
> no reporta**, y que la medición existe. La ficha está desarrollada abajo con sus cifras
> verificadas contra el artefacto. **No bloquea nada de lo ya escrito**: son dos inserciones
> (§17.5.4 y §17.5.7) más una opcional. Constancia del hallazgo:
> `../entregable/desarrollando/archivado/validacion-reestructuracion-17-1-5.md` (fuente: `docs/informe/entregable/desarrollando/archivado/validacion-reestructuracion-17-1-5.md`).
>
> *Lo que sigue es el encuadre del 2026-08-10, conservado como registro histórico:*
>
> **Estado (2026-08-10):** la sección **está vacía** (`[Agregado futuro correspondiente a
> la Etapa 5]`). Es **redacción desde cero**, y es el **camino crítico**: es la sección
> que sostiene la defensa.
>
> **Los insumos están completos, verificados y congelados.** El tramo experimental cerró:
> 17 tablas y 6 figuras inventariadas con su artefacto en disco (`gobierno/99` §1), cuatro
> índices de resultados verificados mecánicamente, GT humano del banco de clips, y la
> escala de conclusiones con su nivel de fuerza. No falta ningún experimento para escribir
> el §17.5 — con **una excepción declarada**, la rama comparativa de fine-tuning (`AJ-5.13`),
> que corre en paralelo y no bloquea al resto.
>
> **Lo que NO va acá:** las conclusiones (§18), el anexo de reproducibilidad y las
> licencias (§19) y el repositorio (§17.6) son **Etapa 6** →
> `06-etapa-6-documentacion-y-cierre.md` (fuente: `docs/informe/ajustes/06-etapa-6-documentacion-y-cierre.md`). El §17.5
> reporta **qué se midió y cuánto dio**; qué significa es la etapa siguiente.

> ⏳ **2026-08-12 — hay UN contenido de esta sección que está abierto: la rama comparativa
> de fine-tuning (`AJ-5.13`).** La jornada de E-04 arrancó (ADR-017) y corre **en paralelo
> a la redacción**: por ADR-017 §2f **no bloquea el informe**. Todo el resto de los insumos
> del §17.5 sigue cerrado y congelado. **Mientras la jornada esté en curso, esa subsección
> se deja reservada con su estado declarado** — no se escribe como exclusión, no se escribe
> como hecha, y no se le pone un número que no salga de un artefacto.
>
> ✎ **2026-08-17 — `AJ-5.13` está DESBLOQUEADA en su brazo T1: la jornada cerró con
> veredicto NO-GO** (constancia `operacion/123`). El párrafo de arriba queda como cuerpo
> histórico: **ya no rige para T1**, que tiene cifra medida y se escribe como hallazgo
> —`bare_head` AP50 0,0000 → 0,0455, faltaron 0,0045 para el umbral; retención de
> `person` −11,62 % contra un tope de 10 %; **el checkpoint no se adopta**—, con los
> márgenes firmados **antes** de la línea base y **sin renegociar**. **Sigue reservado
> el brazo T2**: reabierto como tier *exploratorio* por la enmienda D-FT-14 —posterior
> al veredicto—, con márgenes propios firmados por adelantado (D-FT-15) y **enviado a la
> cola sin empezar**, así que no tiene ni una cifra: ahí sí va `[[PENDIENTE: …]]`. Al
> redactar se cuenta la secuencia completa y en orden (veredicto → enmienda → márgenes
> pre-firmados): suavizarla destruye lo único que la hace defendible.
>
> ✅ **✎ 2026-08-22 — LA JORNADA ESTÁ COMPLETA EN SUS TRES TRAMOS: `AJ-5.13` quedó
> TOTALMENTE desbloqueada y ya no hay `[[PENDIENTE]]` que dejar.** T2 corrió el 20/08 y
> cerró **NO-GO** el 21/08 (`operacion/127`); T3 quedó cerrado con causa técnica
> (`operacion/117` §2). La subsección del §17.5 se escribe entera como **curva de
> capacidad de tres puntos** — es el valor declarado del tramo (F-127.1: el fallo es
> **estructural**, 2.946 imágenes contra 10,35M de parámetros, no de capacidad). Cifras
> canónicas de T2 (job `1167982`, D-FT-16): ganancia PASA (`bare_head` 0,0000 → **0,0909**,
> sólo en `shel5k`) · retención in-domain FALLA ×4 (`person` −49,7 %; mAP50 protegido
> −43,4 %) · retención open-vocabulary FALLA (COCO 0,4347 → 0,1247, **−71,3 %**) · colapso
> en entrenamiento (early stop 16/60, mejor época = 1). Las 3 expectativas pre-registradas
> (firmadas el 17/08, con cero cifras tuned) se confirmaron una por una. Ningún checkpoint
> se adoptó; no hay más brazos contra `bench_v3` — reabrir exige pre-registración nueva
> (acta `operacion/128` §5). **Trampa de cita: T1 gana por recall CR-01, T2 por AP — no
> hay una métrica única "mejor tuned".** En §17.4 la fila de la Tabla 68 la fija **E4-27**
> (pase 3); acá rige este bloque para el §17.5.

> ⚠️ **Los pocos números que aparecen en esta página son anclas de navegación, no fuente
> de cita.** Toda cifra que entre al informe se transcribe **desde el artefacto** que
> indica `gobierno/99` §1. Esta página existió antes en forma de tabla-atajo y esa forma
> **quedó derogada** justamente por desactualizarse (ver `AJ-5.03`).

| Dónde | Qué |
|---|---|
| Texto actual | `entregable/96e` — placeholder vacío |
| **La única fuente de cifras** | `e-ovrt_experimental-setup/results/` — cuatro índices: `bench_imagenes/`, `bench_nivel_a/`, `clip_bench/`, `realtime/` |
| Inventario de tablas y figuras | `gobierno/99` §1 — **T-68…T-84** y **FIG-A…FIG-F**, cada una con su artefacto |
| La narrativa completa con cifras | `sintesis/resultados-y-conclusiones.md` — **el documento central para escribir esta sección** |
| Fuerza de cada afirmación | `sintesis/…` §8 — escala **AF-1…AF-11** |
| Limitaciones y reproducibilidad | `gobierno/99` §2 (sha256 y comandos), §3 (licencias), §4 (L1–L8) |
| Reglas de honestidad al redactar | `gobierno/97` §3 |

---

## 0. La organización de la sección — decisión del usuario (D-P3-6, ✎ 2026-08-22)

**El §17.5 se organiza por pregunta de medición, no por cronología de campañas.** La sección es un
**resumen de resultados**: qué se midió, cuánto dio y con qué fuerza — nunca la narración del orden en que
se experimentó. Los identificadores de campaña (T1/G1/R1–R6/B1/D1/H1/I1/I2…) son **procedencia del dato**,
no estructura: ningún título de subsección lleva nombre de campaña. Y la sección justifica **todos los
caminos**: los adoptados (criterio pre-registrado), los probados y no adoptados (el veredicto que los
descartó) y los no ejecutados o no implementados (**su factor de justificación** — alcance declarado, no
omisión). El esquema completo, con el reparto §17.4/§17.5/§18, está en el **pase 3, §D.0** (incluido en
este kit); el modelo estructural es la síntesis de resultados vigente.

**Esquema de referencia y qué ficha alimenta cada bloque** (las fichas AJ-5.x siguen siendo las unidades de
contenido; este esquema fija su orden y su lugar):

| # | Bloque | Fichas y contenidos que lo alimentan |
| --- | --- | --- |
| 1 | Encuadre y reglas de lectura | AJ-5.01 (tres niveles) · AJ-5.03 (de dónde salen las cifras) · AJ-5.06 (reglas no negociables) · AJ-5.08 (dónde arranca el reloj) |
| 2 | Percepción sobre imágenes | AJ-5.02 (tablas/figuras del banco de imágenes) · veredictos por combinación (E4-26) · piloto de clase nueva |
| 3 | Estado por sujeto (nivel intermedio) | comparación de estrategias sobre el estado por persona (los resultados; los descartes van al bloque 6) |
| 4 | Alerta por episodio — el resultado principal | **AJ-5.14** (costo medido del caption: 0,704 → 0,622) · banco 47 clips por estrato y condición · granularidad por sujeto medida · AJ-5.09 (FAR: se reporta, sin cota) · AJ-5.07 (estrato B y frontera de juzgabilidad, sin ranking n = 2) |
| 5 | Tiempo real | AJ-5.10 (eje de densidad y sus trampas) · cadena de latencias por tramos · latencia del tramo de distribución |
| 6 | Caminos probados y no adoptados | AJ-5.14 (el sub-experimento aislado-vs-completo que no se corrió) · AJ-5.12 (híbrida: refutada / no ejecutable) · directa vetada por precisión · familia de modelos descartada · AJ-5.13 (ajuste fino: curva de tres puntos) |
| 7 | Lo no ejecutado / no implementado, con su justificación | **AJ-5.14** (el sub-experimento aislado-vs-completo, no corrido) · Nivel 2/3 (evaluabilidad) · métricas MOT (sin anotación de identidad) · preselección en el borde (excluida de lo evaluativo, pre-registrado) · cota FAR · ancla EBE-desde-clip |
| 8 | Síntesis de la sección | AJ-5.05 (limitaciones L1–L8, remisión) · AJ-5.11 (círculo con §15) — la interpretación y la escala de conclusiones (AJ-5.04) pertenecen al §18 |

⚠ Con la organización temática, la campaña "T1" del banco de clips y el tramo "T1" del ajuste fino conviven
en la misma sección: **cada mención dice de cuál habla**.

---

## 1. Tablero de contenidos a escribir

| ID | Tipo | Pri | Qué tiene que decir el §17.5 |
|---|---|---|---|
| **AJ-5.01** | CONCRETA | 🟠 | La **estructura en tres niveles de medición**, sin confundirlos. |
| **AJ-5.02** | CONCRETA | 🟠 | Las **17 tablas y 6 figuras**, transcriptas desde el artefacto y verificables. |
| **AJ-5.03** | PRECISA | 🟠 | **De dónde salen las cifras** — y qué fuentes quedaron derogadas. |
| **AJ-5.04** | EVIDENCIA | 🟠 | La **escala de conclusiones AF-1…AF-11**: qué se afirma y con qué fuerza. |
| **AJ-5.05** | EVIDENCIA | 🟠 | Las **limitaciones L1–L8**, con la formulación exacta de L4. |
| **AJ-5.06** | PRECISA | 🟠 | Las **reglas de lectura** que ninguna tabla puede violar. |
| **AJ-5.07** | EVIDENCIA | 🟠 | El **estrato B** (obra real no guionada) y la **frontera de juzgabilidad**. |
| **AJ-5.08** | PRECISA | 🟠 | **Dónde arranca el reloj** del tiempo real — y por qué no es el fotón. |
| **AJ-5.09** | EVIDENCIA | 🟠 | **FAR/hora**: se reporta, pero no sostiene una cota — y cómo se cita. ✎ 08-12 |
| **AJ-5.10** | PRECISA | 🟡 | El **eje de densidad** y sus dos trampas de instrumento. |
| **AJ-5.11** | PRECISA | 🟡 | El **cierre del círculo con el §15**: la regla de tres tiempos. |
| **AJ-5.12** | EVIDENCIA | 🟡 | La **estrategia híbrida**: una rama refutada y una no ejecutable. |
| **AJ-5.13** | EVIDENCIA | 🟠 | ✎ **08-22 — JORNADA COMPLETA, TOTALMENTE desbloqueada: T1 NO-GO (`operacion/123`) · T2 NO-GO (`operacion/127`) · T3 causa técnica (`operacion/117` §2).** Se escribe como **curva de capacidad de tres puntos** con márgenes y expectativas pre-registrados: T1 `bare_head` 0,0000 → 0,0455 (faltaron 0,0045) y `person` −11,62 %; T2 ganancia PASA (`bare_head` → 0,0909) pero retención in-domain −49,7 % (`person`) y OV −71,3 % (COCO), colapso early-stop 16/60. **F-127.1: fallo estructural (datos), no de capacidad.** Ningún checkpoint adoptado; sin `[[PENDIENTE]]`. Trampa: T1 gana por recall, T2 por AP. *(notas 08-12/08-17: históricas)* |
| **AJ-5.14** | EVIDENCIA | 🟠 | ✎ **09-02 — NUEVA.** El **costo medido del vocabulario activo** (F-88.1 / F-94.1) y el sub-experimento aislado-vs-completo que **no se corrió**: hoy §17.5 no reporta ninguno de los dos, y §17.1.5.3 los promete. |

El **anexo de reproducibilidad** (§19), del que el §17.5 depende para ser auditable, es
`AJ-6.02` en la Etapa 6.

---

## 2. Los contenidos, desarrollados

### AJ-5.01 · 🟠 — tres niveles de medición, y no confundirlos

Es **el error más caro** de todo el set documental, y el §17.5 tiene que estar organizado
de modo que no se pueda cometer:

| Nivel | Qué mide | Sobre qué | Índice |
|---|---|---|---|
| **Imágenes** | detección por clase (mAP@0,5, AP por clase) | `bench_v3`, 3 fuentes independientes (`construction_site_safety`, CHV, SHEL5K) — ver la nota de abajo | `results/bench_imagenes/` |
| **Nivel A** | el **estado "sin EPP" por persona** (E-DIR vs E-IND) | imágenes y también video | `results/bench_nivel_a/` |
| **Nivel B** | **alertas confirmadas contra GT temporal humano** — el resultado principal | el banco de clips | `results/clip_bench/` |
| *(transversal)* | latencia, cadencia, integridad del acople | corridas live y single-host | `results/realtime/` |

Un mismo modelo tiene números muy distintos en cada nivel, y eso **no es una
inconsistencia: es el hallazgo**. El caso más elocuente es Nivel A sobre video, donde el
derrumbe respecto de imágenes es **de precisión, no de recall** (tabla T-83).

> ⚠️ **✎ 2026-08-18 — `estrato` ≠ `fuente` al reportar el bench de imágenes.** Los
> estratos de `bench_v3` se llaman `bench_obra` (147) · `chv` (1.330) · `shel5k` (5.000),
> pero **`bench_obra` no es una fuente ni un dataset externo**: es el subconjunto **curado
> internamente** de `construction_site_safety` v27 (196 → 147, tras excluir 49 imágenes
> fuera del dominio de obra y 4 cajas `bare_head` sub-píxel). Las **tres fuentes
> independientes** son `construction_site_safety`, **CHV** y **SHEL5K**. Al reportar por
> estrato se usan los nombres de estrato; al hablar de *fuentes*, los de dataset —
> mezclarlos le atribuye al trabajo una cuarta fuente inexistente. Detalle y cadena de
> procedencia: glosario `13` §4.4.

---

### AJ-5.02 · 🟠 — las tablas y figuras, con su artefacto

`gobierno/99` §1 tiene el inventario completo: **T-68 a T-84** (campañas de Nivel B,
desgloses por escenario y condición, eje de densidad, selección de modelos, AP por clase
y estrato, Nivel A con IC, latencia y tiempo real, integridad del acople EBE, costo de una
clase nueva, composición del banco y de `bench_v3`, limitaciones, ADRs, estrato B, Nivel A
sobre video, calidad del GT) y **FIG-A a FIG-F** (arquitectura, calidad vs densidad, frame
con overlay, montaje escena|sujeto, máquina de estados, frontera de juzgabilidad).

**Dos reglas al llenarlas, del propio inventario:**

1. **Ninguna tabla se transcribe desde el inventario** — el inventario solo dice **cuál es
   el artefacto**; la transcripción se hace desde el artefacto.
2. **Toda tabla de resultados lleva, en su nota al pie, el `campaign_id` o el sha256 del
   banco.** Es lo que la hace verificable por un tercero, y es la diferencia entre un
   capítulo de resultados y una lista de números.
   ✎ **2026-08-21 — compatible con la autocontención (`GUIA-REDACTORES` §3.1), y conviene
   decirlo porque las dos reglas juntas frenan a un redactor externo:** el pie identifica
   el **artefacto** —qué campaña (T1, G1, I1…), qué digest del banco o del prompt set
   congelado, con qué `n` y sobre qué material—, y **nunca dice dónde vive el archivo**.
   Van al pie el identificador de campaña, el sha256 y la remisión a otra sección del
   propio informe; no van la ruta del artefacto, los índices de `results/`, los ADRs, las
   specs ni las fichas `AJ-`/`R-`/`PODA-`.

Estado de los materiales: la mayoría **✅ en disco**; FIG-A es **📐 spec** (su
especificación está en `material-etapa-3/94` §4) y FIG-B, FIG-C, FIG-E y FIG-F están
**⚙ a generar** desde artefactos que ya existen.

---

### AJ-5.03 · 🟠 — de dónde salen las cifras (y qué está derogado)

**Las cifras salen únicamente de los cuatro índices de `results/`**, verificables con
`operacion/datos/96-verificar-indices.py`.

**Quedaron derogadas como fuente de números** — y es importante, porque siguen existiendo
en el repositorio y parecen citables: `informe/92` §10 ("números canónicos"),
`gobierno/97` §5 (tabla de referencia rápida), `operacion/92` y `operacion/56`. Todas eran
tablas-atajo, y todas se desactualizaron. **La regla que quedó: las cifras salen de
índices verificables, nunca de tablas-atajo** — incluida esta página.

---

### AJ-5.04 · 🟠 — la escala AF-1…AF-11

**No todo lo medido tiene el mismo estatuto, y decirlo es más fuerte que aplanarlo.** La
escala vive en `sintesis/resultados-y-conclusiones.md` §8: cada afirmación con su respaldo
y su fuerza (*establecida* / con límite / degradada).

**La regla que la gobierna, y que conviene escribir explícitamente en el informe:** si la
estimación puntual era vistosa pero **el intervalo de confianza no excluía el cero, la
afirmación se degradó**. El caso testigo es la comparación cruzada G1@4,29 fps > T1@30 fps,
que quedó como estimación puntual y no como afirmación.

**Cuidado con el prefijo:** `AF-1…AF-11` son las **afirmaciones** de la escala. **No son
los argumentos `A1–A5`** de `nucleo/09` (la defensa de OVD; hoy en `nucleo/historicos/`,
con la advertencia de que no incorpora los números medidos después). Son dos series
distintas.

---

### AJ-5.05 · 🟠 — las limitaciones L1–L8

Lista **canónica y cerrada** (2026-08-05), con `results/index.md` §Limitaciones como
versión de referencia: **L1** FAR/hora no sostiene una cota · **L2** sin doble anotación
ni kappa · **L3** bordes adjudicados en 6 clips · **L4** un solo bloque guionado ·
**L5** escenarios desbalanceados ⇒ reportar por estrato · **L6** tracker no medido en obra
real con multitud · **L7** licencia parcial de `chv` · **L8** CR-02 a Nivel A no cerrada.

**Dos cosas que hay que respetar al escribirlas:**

- **Se escribe "limitación L1", nunca `L1` a secas**, porque la Fase L del plan de
  experimentos usa `L0`/`L1` para sus hitos. Es una colisión de etiquetas asumida a
  conciencia (se mantuvo el prefijo `L` porque ya estaba citado).
- **La formulación de L4 es exacta y está firmada** (D-113.1): *"L4 se **precisó**, no se
  levantó"* — existe medición en obra real no guionada, y esa medición **caracteriza por
  mecanismo dónde el sistema deja de ser evaluable; no lo valida sobre obra real**. No se
  creó una L9: la frontera de juzgabilidad es el contenido nuevo de L4.

---

### AJ-5.06 · 🟠 — las reglas de lectura no negociables

Familia F-EV. Ninguna tabla ni párrafo del §17.5 puede violarlas:

- **Reportar por estrato y por escenario, nunca solo el agregado.**
- **Los clips negativos no entran a P/R/F1** — su métrica son los FP.
- **`re_alerts` ≠ FP** (ADR-011).
- **El SDR no se compara entre cadencias.**
- **`t_alert` no se compara entre densidades** sin control de supervivencia.
- Una métrica que no aplica se reporta **`not_applicable:<causa>`** (ADR-006/013), nunca
  como 0 ni omitida.

---

### AJ-5.07 · 🟠 — el estrato B y la frontera de juzgabilidad

El banco vigente tiene **dos bloques**: el rodaje guionado (Bloque A) y el **lote de
internet** (Bloque B), obra real **no guionada**. El Bloque B produjo el resultado
conceptualmente más interesante del tramo final, y hay que escribirlo con cuidado:

- **No se rankea con ese n.** Los episodios evaluables del estrato B son **2**. Lo que sí
  es robusto es la **asimetría de falsos positivos** entre configuraciones sobre los
  negativos, y el FAR del único clip *soak*, que **se cita como recuento sobre su duración
  ("3 y 190 FP en 6:09,6"), no como tasa por hora** — la tasa derivada infla por
  extrapolación desde ~0,10 h.
- **La frontera de juzgabilidad tiene tres ejes**: **escala × iluminación × oclusión**. Es
  la figura **FIG-F**, y es lo que convierte un mal resultado agregado en una
  caracterización útil: *dónde* el material deja de ser evaluable, y por qué.
- **La revisión ciega del GT es un resultado, no una nota al pie.** Al re-revisar a ciegas
  las declaraciones de episodio del lote, **5 de 7 eran errores de anotación (~71%)**,
  todas **sobre-declarando donde el estado no era observable** — *el mismo modo de falla
  que el motor*. Es la tabla **T-84**, y es el argumento empírico más honesto que tiene el
  trabajo sobre calidad de GT. También es el contrapeso de la limitación L2 (`AJ-2.06`).

La lección de método asociada merece una línea: **los "person N" de la interfaz de CVAT no
coinciden con los `track_id` del XML** — hay que verificar dibujando la caja sobre el
frame.

---

### AJ-5.08 · 🟠 — dónde arranca el reloj (y por qué no es el fotón)

**El G2A se mide desde el *dequeue*, no desde el fotón** (F-101.8). Consecuencia directa
que **el informe tiene que decir explícitamente**:

```
vidrio → alerta  =  capture_to_host  +  G2A
```

`capture_to_host` fue medido en el rodaje y se degrada de forma importante en condiciones
adversas. Reportar solo G2A como "latencia de punta a punta" sería sobrevender el sistema
por omisión del primer tramo. Esto se cerró con hardware real y ancla física, y está
documentado con sus cuatro patas.

---

### AJ-5.09 · 🟠 — FAR/hora: se reporta, pero no sostiene una cota

> ✎ **2026-08-12 — corregido: este ajuste decía "no se reporta FAR/hora" y se contradecía
> con su propio párrafo final.** La formulación vigente es la de `gobierno/99` §4 (L1,
> precisada el 08-10) y la de `results/index.md`.

**Se mide y se reporta.** Desde el 08-07 el banco tiene un clip de *soak* (`v06_c01`,
0,1027 h), así que la tasa **es computable** — y por eso mismo hay que citarla bien.

**Lo que no se puede hacer es sostener una cota:** harían falta ~3 h de cumplimiento
anotado y el banco llega a ~0,10–0,26 h. Esa es la **limitación L1**, declarada **con
causa cuantificada** (D-90.1, precisada por D-113.1).

**Cómo se cita, sin excepción:** el **recuento de falsos positivos sobre su duración
observada**, con el denominador a la vista, y la tasa horaria **como derivada** — nunca la
tasa desnuda, que sugiere una hora observada que no existe (`GUIA-REDACTORES` §3).

**Dónde va el peso de la evidencia:** en el **control comparativo de negativos**, que sí
discrimina entre configuraciones sobre el mismo material (ver `AJ-5.07`).

---

### AJ-5.10 · 🟡 — el eje de densidad y sus trampas de instrumento

Las campañas R1–R6 miden el banco a las densidades del camino live (frente a 30 fps). Dos
precauciones de instrumento que hay que declarar antes de mostrar la curva (es la
**FIG-B**):

- **El SDR no se compara entre cadencias.**
- **El `t_alert` agregado no se compara entre densidades sin control de supervivencia** —
  los episodios que no llegan a confirmar no están en el promedio, y eso sesga.

La ganancia de la granularidad por sujeto **excluye el cero en las cuatro densidades**;
la comparación cruzada entre densidades distintas, en cambio, es estimación puntual (ver
`AJ-5.04`).

---

### AJ-5.11 · 🟡 — cerrar el círculo con el §15

Cada conclusión se escribe en **tres tiempos**: *qué dice la literatura* (la vara del §15)
→ *qué medimos nosotros* (la cifra de `results/`) → *qué tipo de aporte queda*. Nunca al
revés.

Esto **depende de que la Etapa 1 se haga** (`AJ-1.01`, `AJ-1.02`, `AJ-1.13`): hoy el §15
no tiene la vara supervisada, así que el §17.5 no tiene contra qué contrastar. Es la única
dependencia real entre etapas del pase de ajustes.

Y la precisión de vocabulario que se arrastra desde `AJ-1.15`: **no se adaptaron los
pesos** — se adaptó operativamente (resolución, formulación del vocabulario, capas de
plataforma). Medir cuánto rinde ese stack sin entrenar es la contribución.

---

### AJ-5.12 · 🟡 — la estrategia híbrida: una rama refutada, una no ejecutable

Hay que declarar las dos con precisión distinta:

- **E-HYB-or**: ejecutada y **refutada** (exclusión E-13, registrada en ADR-015). Una
  refutación medida es resultado, no fracaso.
- **`hyb_and`**: **no ejecutable por fundamento** — no es que no se llegó a correr, es que
  la conjunción no tiene sentido en el diseño. Hay que decir *por qué*, no dejarlo como
  pendiente.

---

### AJ-5.13 · 🟠 — ✅ CERRADA: la rama comparativa de fine-tuning (E-04)

> ✅ **✎ 2026-08-22 — Estado: jornada COMPLETA en sus tres tramos; NO queda contenido
> abierto en el §17.5.** El cierre y las cifras canónicas están en la nota de cabecera de
> esta página (bloque ✎ 2026-08-22) y en `sintesis/resultados-y-conclusiones.md`; los
> artefactos, en los índices de `results/`. La subsección se escribe como curva de
> capacidad de tres puntos, en su propia subsección y sus propias tablas, nunca fundida
> con el núcleo zero-shot. **Lo que sigue abajo es el protocolo de redacción original
> (08-12): sus reglas de encuadre siguen valiendo; sus menciones de "jornada en curso",
> "estado a la entrega" y "cuando existan cifras" quedaron superadas por el cierre.**

**Por qué existe la subsección aunque no haya resultados.** ADR-017 sacó a E-04 de las
exclusiones y la puso en alcance como **jornada experimental comprometida**. Un §17.5 que
no la mencione la volvería a leer como exclusión, que es exactamente lo que la ADR derogó.

**Cómo se escribe mientras la jornada corre** (ADR-017 §2f — *la jornada no bloquea el
informe*):

1. **Se declara el diseño, que ya está fijado**: escalera pre-registrada **T1 (linear
   probing) → T2/T3**, con los go/no-go y la Tabla 37 gobernando el escalamiento;
   entrenamiento en Mendieta; evaluación contra **`bench_v3`**. Eso se puede escribir hoy,
   porque es diseño, no resultado.
2. **Se declara el estado a la entrega, tal cual sea**, con **causa técnica**.
3. **No se promete ningún tier** al que la escalera no haya llegado. Lo que los go/no-go no
   habiliten es trabajo futuro y se dice así.
4. **Se declara la restricción de ejecución de Mendieta y su efecto real:** conexión sin
   límite operativo, jobs de hasta **48 h** y posibilidad de pedir múltiples nodos/GPU. La
   subsección informa allocation y duración; después clasifica el walltime como vinculante
   o no vinculante, nunca lo deja implícito.

**Limitación operativa pre-registrada — walltime de Mendieta.** Cada corrida está limitada
a 2 días, aunque no existe el mismo límite para el tiempo de conexión ni para el ancho de
la asignación: pueden pedirse, por ejemplo, 8 nodos de 2 GPU. Esta condición entra al
informe de una de dos formas, según la evidencia al cierre:

- **Si limitó:** declarar `walltime_binding` como limitación técnica específica de E-04 y
  explicar si hubo interrupción, reanudación, schedule incompleto o tier no alcanzado.
- **Si no limitó:** declarar `walltime_not_binding`, informar nodos/GPU y duración real, y
  explicar al final de la subsección que el máximo de 48 h **no condicionó el resultado**.

La ficha se completa con partición, recursos solicitados/asignados, timestamps, motivo de
cierre de Slurm, checkpoint final y cantidad de reanudaciones. La fuente operativa de esta
regla es `operacion/100` §6.5 (F-100.3).

**Las tres cosas que no se pueden escribir, y por qué cada una:**

| 🚫 | Por qué |
|---|---|
| La causa **"falta de tiempo"** / "presupuesto de tiempo" / "secuenciación" como motivo de no-ejecución | **Prohibida por ADR-017 §2b.** El encuadre correcto: rama comparativa **condicionada desde el planteo por datos y protocolo**. F-100.1, freeze/smoke, dual gate, serving y procedencia T-FT-023 están cerrados (snapshot tar `639e60df…`); el NO-GO actual responde a D-FT-08/T-FT-005, evaluación T-FT-031 y baseline T-FT-032. Una proyección de cola solo se cita como estimación puntual, nunca como falta de tiempo del proyecto |
| Fundir sus cifras con las del **núcleo zero-shot** | Es **otra rama**. Se rotula como comparativa y va en su propia subsección y sus propias tablas. Fundirlas destruye la pregunta de la tesis, que es cuánto rinde el stack **sin entrenar** |
| Leer los go/no-go como **aprobado/fallado** | Son criterios de lectura y escalamiento (ADR-017 §2c). **Un desenlace negativo —sin ganancia exigible, o con erosión open-vocabulary medida— es un resultado documentable**, y de los valiosos: mediría el costo de adaptar |

**De dónde saldrán las cifras cuando existan:** de un artefacto en
`e-ovrt_experimental-setup/results/`, igual que todo el resto — **nunca de las notas de
trabajo de la jornada**. Mientras no haya índice verificable, no hay cifra citable.

**Puertas previas (son del tramo experimental, no de la redacción):** F-100.1,
freeze/smoke técnico, dual gate y serving real ya están cerrados. El full continúa en NO-GO
por D-FT-08/T-FT-005, evaluación T-FT-031 y baseline YOLOE-26s T-FT-032 sobre
`bench_v3` (`operacion/100/116/117`). No bloquean escribir el resto del §17.5.

✎ **2026-08-15 — las decisiones quedaron firmadas y hay tres cosas que decir en el informe.**
D-FT-08/T-FT-005, D-FT-12 y D-FT-13 fueron aprobadas por el usuario, **y la misma jornada
cerraron T-FT-031 y T-FT-032** (doc 120): el NO-GO de T1 full quedó en su último eslabón
(`full-authorization.json` + `RUN` manual). Primero: **D-FT-12 se firmó ANTES de la
baseline**, con cero jobs full — los márgenes go/no-go (ΔAP50 ≥ +0,05 o rescate de recall
<0,1→>0,5; retención in-domain ≤10 %; latencia ≤5 %) y la clase objetivo `bare_head` son
**pre-registración en sentido estricto**. Segundo: **la baseline YOLOE-26s ya existe, medida
una sola vez bajo el protocolo congelado** — `bare_head` AP50 0,000 (6.181 GT / 10 det),
recall CR-01 0,0167/0,0000 por fuente y 0,0002 agregado, retención a proteger person
0,7843 / helmet 0,6286 / vest 0,2642 (doc 120, con estratos). Son cifras **de la rama
comparativa**: tablas propias, por estrato, sin fundirse con el núcleo, y **sin comparación
con la tabla histórica del doc 64** (protocolos distintos — doc 120 §2.5). Tercero:
**F-120.1** — las latencias de ese run no se citan (cambio de energía durante la corrida);
el gate de latencia se medirá pareado cuando exista el checkpoint.

Si T1 se reporta en el informe, la retención OV generalista se declara **NO MEDIDA por
diseño** (contrato de vocabulario fijo), nunca como casilla verde.

**Se lee junto a:** `decisiones/adr-017-fine-tuning-jornada-experimental.md` (§2 completo)
· `contingencia/20` §6 (la escalera) · `01` (el encuadre en §15: rama comparativa, nunca
descarte) · `02` (la escalera en §17.1) · `06` (cómo entra en las conclusiones: rotulada
como rama comparativa, nunca fundida) · `operacion/100` §4/§6, en particular §6.5 para la
clasificación `walltime_binding` / `walltime_not_binding`.

---

### AJ-5.14 · 🟠 — el costo del vocabulario activo: una promesa de §17.1 que hoy §17.5 no reporta

**El problema.** §17.1.5.3 pre-registra el eje de composición del vocabulario activo y
promete que *"cada prompt se evalúa tanto en aislamiento como dentro del vocabulario
completo del sistema"*. El diseño de prompts (`nucleo/historicos/12` §4.1) lo formalizó
como un **sub-experimento aislado-vs-completo acotado a las finalistas**, listado como
corridas extra del media-plane. **Ese sub-experimento nunca se corrió.** Y §17.5 v1.3 no
dice nada al respecto: ni como resultado, ni en §17.5.6, ni en §17.5.7. Verificado sobre la
extracción — `0,622` y `0,082` aparecen **cero veces**; los índices de resultados y la
síntesis tampoco nombran el sub-experimento. Queda una promesa de pre-registro sin
contraparte, que es exactamente lo que la doctrina del pase 3 manda evitar (*"lo prescripto
y no ejercido no se borra, lo reporta §17.5"*).

**Lo que sí se midió, y es mejor que un "no se ejerció".** La pregunta de fondo quedó
respondida dos veces, como subproducto de otras campañas.

| Hallazgo | Contraste | Cifra | Artefacto |
|---|---|---|---|
| **F-88.1** (`operacion/88` §2) | T2 (`v2_short`, 3 clases) contra el **control interno de B1** (`bench_v2`, 4 clases): mismo modelo `gdino-base-560`, mismo evaluador E-IND, mismo pattern set, mismo GT, mismos timings, **una sola palabra de diferencia en el caption** (`bare head`) | F1 **0,704 → 0,622** (−0,082); recall 0,735 → 0,676; precisión 0,676 → 0,575 | `clip_bench/b1_gdinobase560_barehead_scene/metrics_eind_mismo_caption.json` |
| **F-94.1** (`operacion/94` §3) | `vehicle` junto a `machinery` en el mismo caption, contra el mismo caption sin `machinery` | **0 detecciones** contra **118 detecciones, AP 0,026** (el 67 % de las cajas cae sobre lo que el GT llama `machinery`) | `bench_imagenes/clase_nueva` · runs `vehiculo_aislado` |

⚠ **Precisión obligatoria al citar F-94.1:** "aislada" ahí significa **sin `machinery` al
lado**, no sola. El caption de esas corridas seguía siendo `person. helmet. vest. vehicle.`
(verificado en el `effective_config.yaml` de ambos runs). Escribirlo como "prompt aislado"
sería falso.

**La conclusión que habilita.** `operacion/88` §2 lo dice textualmente: la interacción
**no es despreciable**, así que el atajo del pase único con vocabulario unión no es gratis y
**la regla dual-run queda validada empíricamente, no sólo por argumento**. Hay además una
tercera confirmación indirecta, F-83.1: la composición del caption invalidó un atajo que el
propio pre-registro autorizaba, porque las 28 corridas de Sprint 2 que se iban a reusar como
brazo E-IND habían visto 4 clases mientras `eind_v1` declara 3 — el adaptador arma **un
caption único**, de modo que el vocabulario activo es literalmente una cadena de texto.

**Qué escribir, y dónde.**

1. **§17.5.4** (alerta por episodio — es Nivel B, ahí viven T2 y B1): un párrafo con el par
   0,704 contra 0,622 y su lectura. **No es una excusa, es un resultado**, y de los buenos
   para la defensa: sostiene con número el argumento central de que el vocabulario es una
   variable experimental y no una lista de deseos. Se cita como contraste de variable única,
   nombrando las cinco cosas que se mantuvieron fijas.
2. **§17.5.7** (lo no ejecutado): una oración que declare que el sub-experimento formal
   aislado-vs-completo sobre las finalistas **no se corrió**, y que la pregunta quedó
   respondida por la vía de arriba. Sin esa oración, la promesa de §17.1 queda huérfana.
3. **Opcional, §17.5.2**: F-94.1 como el caso extremo del mismo mecanismo, si el bloque del
   piloto de clase nueva no lo cubre ya.

**Lo que NO hay que hacer.** No tocar §17.1. La promesa se mantiene tal cual está redactada
—es pre-registro, y la doctrina D-P3-3 prohíbe reescribirla para que encaje con el
resultado—. El arreglo es de §17.5, y por eso esta ficha vive acá.

---

## 3. 🚫 Lo que no hay que escribir en el §17.5

| # | No escribir | Por qué |
|---|---|---|
| 1 | Solo el agregado | Viola L5 y F-EV1. Siempre por estrato y escenario. |
| 2 | FAR/hora como cota | El banco no lo sostiene: es la limitación L1. |
| 3 | `re_alerts` contadas como FP | ADR-011. Degrada artificialmente toda la precisión. |
| 4 | Rankings sobre el estrato B | n = 2 episodios evaluables. Lo robusto es la asimetría de FP y el mecanismo. |
| 5 | "L4 se levantó" | Se **precisó** (D-113.1). Y "34 clips" es el Bloque A, **no el banco**. |
| 6 | Cifras tomadas de `informe/92` §10, `gobierno/97` §5, `operacion/92` o `operacion/56` | Derogadas como fuente de números. |
| 7 | G2A presentado como latencia vidrio→alerta | Falta `capture_to_host` (F-101.8). |

## 4. Fuentes

`sintesis/resultados-y-conclusiones.md` (§1–§11; §8 la escala AF, §9 alcance y
limitaciones) · `gobierno/99` §1–§4 · `gobierno/97` §3 (reglas de honestidad) ·
`e-ovrt_experimental-setup/results/` y sus cuatro índices · `operacion/96` (costo del
tiempo real), `98` (conclusiones), `101` (claqueta y blindaje EBE), `109`/`111`/`112`/`113`
(el tramo de video y su cierre) · `13-glosario-y-convenciones-de-lectura.md` §4.
**✎ 09-02, para `AJ-5.14`:** `operacion/88` §2 (F-88.1) · `operacion/94` §3
(F-94.1) · `operacion/83` (F-83.1) · `nucleo/historicos/12` §4.1 (el sub-experimento
pre-registrado) · `results/clip_bench/index.md` §F-88.1 y su artefacto
`b1_gdinobase560_barehead_scene/metrics_eind_mismo_caption.json`.

---

## Fuente: `docs/informe/entregable/archivado/borrador-vara-15.md`

> SHA-256 del bloque: `d82aac011a58729e9bf7aeae19bf8147734f7704b635b7140ec18d7c4ba0d496`  
> Seleccion: la vara de literatura: sin ella no se puede escribir en tres tiempos.

# Borrador — la vara del §15 (AJ-1.01 · AJ-1.02 · AJ-1.13)

> **Qué es esto (2026-08-16).** Borrador *texto listo para copiar* (patrón del doc `94`)
> redactado según el ✎ 2026-08-16 del manual `ajustes/08` §2: la vara del §15 se adelanta
> como borrador para desbloquear el §17.5; **los colegas la revisan e integran en Google
> Docs** (D-A híbrida: la §15 existe, así que la edición final es en el documento). La
> decisión fina de anclaje es de quien integra; acá va la propuesta.
>
> **Regla cumplida:** cero cifras propias del proyecto (no-anacronismo, mapa `00` regla 5).
> Todo lo que sigue es literatura, con la métrica de cada cifra declarada al lado
> (evita de paso la trampa de AJ-1.12: nunca mezclar AP 0,50:0,95 con mAP@0,5).
>
> **Al integrar:** marcar `AJ-1.01`/`AJ-1.02`/`AJ-1.13` en el tablero (manual `08` §5),
> anotar cualquier desvío como ✎ en la ficha (`ajustes/01`), sumar las referencias del
> §4 de este borrador al listado del `96e`, y re-extraer la foto de §15
> (`herramientas/extraer_informe.py`, regla D-C).

---

## 1. Dónde ancla cada bloque

| Bloque | Ajuste | Punto de inserción propuesto |
|---|---|---|
| Bloque A — Vara 1, la línea base supervisada | `AJ-1.01` 🔴 | **§15.2.5**, al comienzo: antes de declarar brechas, fijar qué logra lo supervisado in-domain |
| Bloque B — la pregunta que los benchmarks generales no responden | `AJ-1.02` 🔴 | **§15.2.5**, a continuación del Bloque A · más la **nota al pie de la Tabla 3** (§15.2.3) |
| Bloque C — Vara 3, el cruce OVD×EPP | `AJ-1.13` 🟠 | **§15.2.5**, cierre de la subsección: la brecha queda declarada |

Los tres bloques forman una secuencia narrativa única dentro de §15.2.5 (vara supervisada
→ pregunta de generalización → brecha del cruce), así que conviene integrarlos en un solo
pase. La subsección existente se conserva; esto se intercala donde hoy la brecha se
menciona sin cifras.

---

## 2. Los tres bloques, texto listo para copiar

### Bloque A — la línea base supervisada in-domain (AJ-1.01)

La detección de EPP con modelos supervisados entrenados in-domain constituye una línea
base madura, con cifras publicadas sobre los mismos conjuntos de datos que este trabajo
adopta como fuentes. Sobre SHEL5K, Otgonbold et al. (2022) reportan para YOLOR un
mAP@0,5 de **0,883**, con **0,907** para la clase *head* (cabeza sin casco); sobre CHV,
Wang et al. (2021) reportan para YOLOv5x un mAP@0,5 de **0,866** sobre seis clases
(persona, chaleco y cuatro colores de casco). En conjuntos de mayor vocabulario el techo
desciende: en SH17 (2024; 17 clases de entorno industrial), YOLOv9-e alcanza
aproximadamente **0,71** de mAP@0,5, y la familia YOLOv8 (variantes n a x) se ubica entre
**0,58 y 0,69**.

Dos lecturas de esta vara importan para lo que sigue. Primero, la detección supervisada
de EPP es un problema esencialmente resuelto en su formulación estándar: con
entrenamiento in-domain, las clases centrales superan 0,85 de mAP@0,5. Segundo — y es el
dato fino que esta vara deja establecido —, la clase *cabeza sin casco*, que podría
suponerse difícil por su granularidad semántica, **no lo es para un detector
supervisado**: 0,907 en SHEL5K, por encima incluso del promedio del conjunto. Cualquier
dificultad que aparezca sobre esa clase por otras vías de detección no podrá atribuirse,
entonces, a la clase en sí.

### Bloque B — la pregunta que los benchmarks generales no responden (AJ-1.02)

Los modelos open-vocabulary del presente capítulo se comparan habitualmente por sus
cifras sobre benchmarks generales (COCO, LVIS; Tabla 3). Esas cifras responden cuánto
generaliza el modelo *sobre la distribución de esos benchmarks*, pero dejan sin
responder la pregunta que este trabajo necesita: **¿predicen los benchmarks generales el
rendimiento sobre una condición de dominio específica?** La evidencia publicada sugiere
que no. El propio equipo de Grounding DINO reporta que su variante grande, con ~52 AP
(COCO, 0,50:0,95) en el benchmark general, cae a **26,1 de mean AP sobre los 35
datasets de ODinW** (Liu et al., 2023) — la referencia publicada de cuánto colapsa un
detector open-vocabulary fuera de distribución. Y cuando la consulta exige composición
léxica fina — atributo o negación, del tipo *"trabajadores con casco blanco"* —, Chen
et al. (2025) miden sobre escenas de construcción que los modelos de
grounding quedan por debajo de **20% de IoU**: el preentrenamiento no resuelve por sí
solo la composición.

De ambas evidencias queda una conclusión que este capítulo puede firmar: **los
benchmarks generales no garantizan el rendimiento sobre la condición de dominio, y no
existe benchmark publicado del cruce entre detección open-vocabulary y EPP** (§15.2.5,
cierre). Esa brecha es la que justifica la decisión metodológica, adoptada en el
protocolo experimental (§17.1.9.2), de exigir una línea base zero-shot propia sobre un
conjunto de evaluación congelado, en lugar de seleccionar modelos por sus cifras
publicadas.

**Nota al pie propuesta para la Tabla 3 (§15.2.3):** *Las cifras de precisión de esta
tabla corresponden a benchmarks generales (COCO/LVIS, AP 0,50:0,95 salvo indicación) y
no son directamente trasladables a una condición de dominio específica; la validez de
esa extrapolación se discute en §15.2.5.*

### Bloque C — la Vara 3: el cruce OVD×EPP está casi vacío (AJ-1.13)

El cruce entre detección open-vocabulary y EPP en obra cuenta con una única cifra
publicada directamente comparable con una evaluación por clase a AP@0,5: Choi y Greer
(2024) miden OWLv2 zero-shot sobre 5.210 imágenes de obra y reportan **0,649 para
*hardhat*** y **0,677 para *person*** (AP a IoU>0,5). Sobre la composición con atributo,
la evidencia citada arriba (Chen et al., 2025; IoU <20%) confirma que la vía léxica fina
está lejos de resuelta. Fuera de esas dos piezas, la revisión efectuada no encontró
**ningún trabajo publicado entre 2023 y 2026 que mida Grounding DINO ni YOLO-World
zero-shot sobre SHEL5K o CHV, ni sobre un benchmark de EPP multi-fuente con protocolo
COCO**. La comparación entre la vara supervisada del Bloque A (mAP@0,5 ≥ 0,86 con
entrenamiento in-domain) y la única cifra zero-shot disponible (0,649 en la clase más
favorable) queda, por lo tanto, sin un puente publicado: **esa es la brecha que el
estado del arte deja declarada**.

---

## 3. Qué NO va acá (y dónde vive)

- La confirmación **medida** de la brecha (el caso YOLOE: 35,9 AP LVIS publicado vs el
  recall propio; los G2A medidos vs la columna de latencia derivada) es material de
  **§17.5**, escrito en tres tiempos contra esta vara (`AJ-5.11`).
- Que `bench_v3` **ocupa** la brecha declarada es lectura de §17.5/§18, no del §15.
- La lectura de la clase `bare_head` contra la vía léxico-conceptual (AF-5) también:
  acá queda solo el fundamento externo (head 0,907 supervisado).

## 4. Referencias a incorporar al listado del `96e`

Verificadas 2026-08-06 (listado de `sintesis/resultados-y-conclusiones.md` §7.4):

- Otgonbold, M.-E. et al. (2022). *SHEL5K: An Extended Dataset and Benchmarking for
  Safety Helmet Detection*. **Sensors 22(6):2315**.
- Wang, Z. et al. (2021). *Fast Personal Protective Equipment Detection for Real
  Construction Sites Using Deep Learning Approaches*. **Sensors 21(10):3478** (dataset CHV).
- SH17 (2024). *Dataset for human safety and PPE detection in manufacturing industry*.
  **arXiv:2407.04590**.
- Liu, S. et al. (2023). *Grounding DINO: Marrying DINO with Grounded Pre-Training for
  Open-Set Object Detection*. **arXiv:2303.05499** (cifra ODinW-35).
- Choi, J. & Greer, R. (2024). *Language-guided zero-shot object detection: OWLv2 sobre
  hardhat en obra*. **arXiv:2410.12225**.
- Chen et al. (2025). *ConstructionSite-10k: grounding con atributo y negación en escenas
  de construcción*. **arXiv:2508.11011**.

> ⚠️ Al integrar en el `96e`, unificar el formato con el listado existente (AJ-1.10:
> hoy conviven Liu 2023/2024 y variantes). Los títulos de Choi & Greer y Chen 2025
> están parafraseados acá — **verificar el título exacto contra el arXiv al citarlos**.

---

## Fuente: `docs/informe/ajustes/gobierno/99-materiales-de-cierre.md`

> SHA-256 del bloque: `24dcad1f3e6610145ff2138777fbf1c06df9f051cc5abb74431ada9371cad0ca`  
> Seleccion: figuras y tablas aplicables a resultados.

## 1. Inventario de figuras y tablas, con su artefacto de origen

**Numeración.** El capítulo cierra en la **Tabla 60**; el doc 94 ya ocupa **61–67**. Las
de acá se proponen desde **68**, y el doc 93 advierte verificar colisiones al
transcribir. Los identificadores `T-nn`/`FIG-x` son **de trabajo**, no del informe.

**Columna «insumo»** — verificada contra disco el 2026-08-05 (✎ filas del tramo de
video T-82…T-84 y FIG-F agregadas y verificadas el 2026-08-10):
`✅ en disco` = el artefacto existe y la tabla se llena copiando · `⚙ generar` = hay que
correr un script sobre artefactos que existen · `📐 spec` = está especificada pero no
producida.

**Columna «redline» — tentativa.** Sale del *encabezado* de cada redline en el doc 93, no
de su cuerpo. Los marcados con `?` son inferencia mía y hay que confirmarlos leyendo el
"DEBE DECIR" antes de darlos por saldados. Los seguros son R-09 (que es literalmente una
especificación de figura, doc 94 §4), R-12 y R-13 (ambos "Sección nueva al cierre ·
EVIDENCIA") y R-26 (§17.3.17/18, extensibilidad).

| ID | Tabla / figura | Artefacto de origen | Redline | Insumo |
|---|---|---|---|---|
| T-68 | **Campañas de Nivel B sobre el banco del rodaje (Bloque A)** (T1, T2, G1, D1, H1, B1: R/P/F1, `t_alert`, TTFD, SDR, FP neg) — ✎ 08-10: el censo vigente de `clip_bench` es de **14 campañas** (estas 6 + R1–R6 de T-71 + I1/I2 de T-82) | `results/clip_bench/index.md` + `*/metrics.json` | R-12/R-13 | ✅ en disco |
| T-69 | Desglose **por escenario** P1–P9 | `results/clip_bench/index.md` §Detalle por escenario | R-12 | ✅ en disco |
| T-70 | Desglose **por condición** CR-01 / CR-02 | idem §Detalle por condición + `metrics.json → by_condition` | R-12 | ✅ en disco |
| T-71 | **Eje de densidad** R1–R6 (30 / 4,29 / 2,0 / 1,15 fps × escena/sujeto) | `results/clip_bench/index.md` §Eje de densidad + `operacion/96` | R-13 | ✅ en disco |
| T-72 | **Selección de modelos** sobre `bench_v3` (mAP50 por modelo × estrato) | `results/bench_imagenes/index.md` §2 + `operacion/64` | R-13? | ✅ en disco |
| T-73 | **AP por clase y por estrato** (la asimetría estructural) | idem §Por clase y por estrato + `operacion/66` | R-13? | ✅ en disco |
| T-74 | **Nivel A**: E-DIR vs E-IND por condición y estrato, con IC | `results/bench_nivel_a/d1_*/metrics.json` | R-12 | ✅ en disco |
| T-75 | **Latencia y tiempo real**: G2A single-host, G2A live por modelo, presupuesto | `results/realtime/index.md` §2/§3 + `operacion/39`, `71` | R-05?/R-14? | ✅ en disco |
| T-76 | **Integridad del acople EBE**: paridad, `bus_dropped_events`, 1:1 | `results/realtime/index.md` §1 + `operacion/37`, `65`, `91` | R-04? | ✅ en disco |
| T-77 | **A1 — costo de una clase nueva** (0 entrenamientos / 48 líneas / 9 min / AP 0,662) | `operacion/datos/94-piloto-clase-nueva/resultados.json` | R-26 | ✅ en disco |
| T-78 | **Composición del banco de clips** — ✎ 08-10: **47 clips en dos bloques** (A rodaje 34 · B lote de internet 13), **32 positivos / 15 negativos, 37 episodios**; evaluables **34/35 en el Bloque A** (1 censurado con causa) y **2/2 en el B** (post-revisión ciega); 1 clip soak (`v06_c01`, 6:09,6). *(Decía "34 clips, 35 episodios" — eso es el Bloque A, no el banco.)* | `datasets/processed/clip_bench/manifest.yaml` (sha `3f14f50a…`, freeze 2026-08-09) + `meta/*.clip.yaml` | R-12 | ✅ en disco |
| T-79 | **Composición de `bench_v3`** por estrato (6.477 / 55.165 / sha256) | `bench_v3_manifest.json` + `registry/bench_v3.md` | R-21 | ✅ en disco |
| T-80 | **Limitaciones declaradas** (§4 de este doc) | `operacion/98` §6 + `results/index.md` | R-13 | ✅ en disco |
| T-81 | **ADR → dónde se declara en el informe** (§4 de este doc) | `decisiones/` + `estado-de-implementacion-adrs.md` | — (R-18 es la Tabla 43 DA-01…DA-13, **no** esta) | ✅ en disco |
| T-82 | **Estrato B (obra real no guionada) — I1/I2** (✎ 08-10): F1 0,333 (`scene`) / 0,190 (`subject`) sobre **2 episodios evaluables — no rankear con ese n**; lo robusto es la **asimetría de FP: 26 vs 323 sobre 11 negativos (12×)** y el FAR del único soak, citado como **"3 y 190 FP en 6:09,6"** (tasas derivadas 29,2 / 1.850,8 FA/h, denominador 0,1027 h) | `results/clip_bench/{i1,i2}_gdinotiny560_*_internet/metrics.json` + índice | R-13 | ✅ en disco |
| T-83 | **Nivel A sobre video (NA1, 17 clips)** (✎ 08-10): CR-01 F1 0,031 / CR-02 0,018 contra 0,408/0,479 en imágenes (`bench_obra`) — el derrumbe es de **precision**, el recall se sostiene | `results/bench_nivel_a/na1_gdinotiny560_v2short_video/metrics.json` | R-13 | ✅ en disco |
| T-84 | **Revisión ciega del GT del lote como resultado de calidad de GT** (✎ 08-10): **5 de 7 declaraciones de episodio eran errores de anotación (~71%)**, todas sobre-declarando donde el estado no era observable — el mismo modo de falla que el motor | constancia en `operacion/113` §B + correcciones firmadas en los `clip.yaml` | R-13 | ✅ en disco |
| T-85 | **Latencia de notificación (distribución): p95 64,534 ms (n=460) + régimen sostenido** | `results/realtime/t_alert_notification/metrics.json` + `operacion/118` | §17.3.10 | ✅ en disco |
| FIG-A | **Arquitectura de los dos planos** (DBE / EBE, corte tras normalización) (✎ 08-19: destino único **§17.4.1** — §17.3 quedó sin vista de procesos por la doctrina del pase de cierre) | especificación en **doc 94 §4** | R-09 | 📐 spec |
| FIG-B | **Curva calidad vs densidad** (F1 escena y sujeto contra fps) | `results/clip_bench/r{1..6}_*/metrics.json` | R-13 | ⚙ generar |
| FIG-C | **Frame con overlay de alerta confirmada** | renderer en `experimental-setup/defensa/` + `runs/*/previews/` | R-12 | ⚙ generar |
| FIG-D | **Montaje lado a lado escena \| sujeto** (el mecanismo de F-89.1 en una imagen) | `experimental-setup/defensa/` (VG1 lado a lado, ya renderizado) | R-26 | ✅ en disco |
| FIG-E | **Máquina de estados del motor** (`inactive → candidate → confirmed → sustained → resolved`, con `confirm_after_ms`) (✎ 08-19: destino **§17.3.8.2** y CINCO estados — el rótulo de tres estados era una simplificación incorrecta) | contrato `pattern_events` del control-plane | R-06/R-07 | ⚙ generar |
| FIG-F | **Frontera de juzgabilidad de 3 ejes** (escala × iluminación × oclusión) — dónde el material deja de ser evaluable (✎ 08-10) | mediciones en `operacion/103` §7 y `operacion/105` (F-105.3) | R-13 | ⚙ generar |

> ✎ **2026-08-21 — LAS CINCO FIGURAS PENDIENTES ESTÁN PRODUCIDAS.** `FIG-A`, `FIG-B`,
> `FIG-C`, `FIG-E` y `FIG-F` dejaron de ser `📐 spec` / `⚙ generar`: viven en
> `informe/figuras/` (fuente: `docs/informe/figuras/README.md`) en PNG 300 dpi + SVG, con generadores
> reproducibles y notas al pie redactadas. **El inventario de materiales del informe
> queda completo** — 17 tablas + 6 figuras, todas con artefacto de origen. Tres
> advertencias de cita, en el README de esa carpeta: el módulo de distribución va en
> línea **continua** (la nota al pie de `94` §4 quedó falsa y está reemplazada allí), el
> **orden de arranque es el inverso del flujo de datos**, y la máquina de estados tiene
> **cinco** estados con la reapertura hacia `candidate`, no hacia `inactive`.

**Regla al llenarlas:** ninguna tabla se transcribe desde este inventario ni desde el
§5 del doc 97 — se transcribe **desde el artefacto**, y el inventario solo dice cuál es.
Toda tabla de resultados lleva, en su nota al pie, el `campaign_id` o el sha256 del
banco: es lo que la hace verificable por un tercero.

**Las tres reglas de lectura que ninguna tabla puede violar** (F-EV1, L5, F-96.6):
los clips negativos (✎ 08-10: hoy son **15** — 4 del Bloque A + 11 del estrato B) **no**
entran a P/R/F1, su métrica son los FP · se reporta **por estrato y por escenario**,
nunca solo el agregado · el **SDR no se compara entre cadencias**.

---

