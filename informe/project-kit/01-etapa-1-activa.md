# E-OVRT-VDP - paquete de etapa 1

> Generado el 2026-09-01. Etapa 1: secciones 15 y 16 (CERRADA 2026-08-28; el Anexo A corregido vive en 90e).

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
   con sus tres pases APLICADOS Y VERIFICADOS (textos base `90` / `90b` / `90c`) · **§17.1 v1.7
   (Etapa 2) CERRADA el 2026-09-01 con SEIS pases aplicados y verificados (el 5:
   poda por aporte, cero bajas de referencias; el 6: desacople normativo del 09-01 —
   severidad metodologica, sin articulos legales; extension justificada en
   justificacion-extension-17-1.md), y los
   Anexos C y D finales AL FINAL del propio documento** (texto base `90f`; documento limpio —
   cambios aceptados y 27 comentarios resueltos; siguen los handoffs hacia
   17.3/17.4/17.5) · §17.6, §18 y §19 sin redactar. El texto base vigente de cada etapa es SIEMPRE su extraccion
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

- **Etapa activa:** 1 - Etapa 1: secciones 15 y 16 (CERRADA 2026-08-28; el Anexo A corregido vive en 90e).
- Este archivo contiene el texto vigente que se modifica y sus insumos de ajuste.
- No se trasladan resultados propios hacia secciones cronologicamente anteriores.
- Nombre propio de esta etapa (01-etapa-1-activa.md): regenerarla no pisa el paquete de ninguna otra etapa.
- **Restriccion propia de esta etapa: el estado del arte tiene que quedar alineado con la plataforma que efectivamente se construyo.** Un modelo, metodo o protocolo se desarrolla si tiene rol en el trabajo; y todo resultado que el informe reporte mas adelante necesita aca su **vara** (cifra publicada) o su **brecha** declarada. Ese es el criterio que ordena tanto las adiciones como las podas.
- La seccion 1 del pase de alineacion describe la plataforma construida. Es el blanco de la alineacion y **no se cita**: en las secciones 15 y 16 no entra ningun numero propio, ningun experimento y ninguna eleccion de diseno del proyecto.
- Estado del trabajo (✎ 2026-08-27, cierre): **el CONTENIDO de la etapa 1 esta CERRADO.** Los pases 1, 2 y 3 estan APLICADOS Y VERIFICADOS sobre las tres piezas -seccion 15, seccion 16 y Anexo A-, los 16 `AJ-1.xx` estan resueltos y las podas 01-11 aplicadas. **NO reaplicar nada de eso, ni volver a redactar.**
- **ETAPA 1 CERRADA (✎ 2026-08-28): los cinco pases estan aplicados y verificados.** Documento final: `E-OVRT-VDP_Secciones_15_y_16_Estado_del_Arte_y_Marco_Teorico_v1.0.docx` (secciones 15 y 16). **No hay trabajo pendiente de redaccion, formato ni terminologia.** Si este paquete se abre para otra cosa, no rehacer nada de lo hecho; cualquier cambio sobre la etapa 1 requiere un pase nuevo, explicito.
- **El entregable de la etapa es SOLO el desarrollo (secciones 15 y 16).** Sin Anexo A, sin Anexo B y sin listado de Referencias: los arma el equipo. El Anexo A y las referencias ya corregidos estan en `90e` para la seccion 19, porque el cuerpo cita las Tablas A.1 y A.2.
- **No se trabaja sobre Drive ni editando el documento en la nube.** El texto vigente completo de la etapa esta en este paquete (`90d`: secciones 15 y 16), asi que ir a buscar el documento afuera es innecesario y ademas lo daña: los dos defectos que quedan aparecieron exactamente asi. El detalle del circuito de entrega esta en la seccion 'Como se trabaja y como se entrega' del contexto base y en la seccion 2 del pase 4.
- Queda **una decision del equipo, no del redactor**: D-E1-11, la aplicabilidad de la inscripcion ante la AAIP al contexto experimental. Esta correctamente marcada en el texto con `[[PENDIENTE: ...]]` y **ese marcador debe viajar**: no se completa con una estimacion ni se borra.

---

## Fuente: `docs/informe/entregable/desarrollando/archivado/correcciones-etapa-1.md`

> SHA-256 del bloque: `0942b5f992b600a2a7b4b70ed52d77ecf3095bfb566d6ab0f7ca6fcbd19fd78e`  
> Seleccion: pase 1 de alineacion de la etapa 1 (2026-08-27): YA APLICADO Y VERIFICADO en el documento de trabajo - NO volver a aplicarlo. Sus comentarios E1-01 a E1-12 y sus decisiones D-E1-1 a D-E1-6 siguen rigiendo como criterio de lectura; su seccion 1 (la plataforma efectivamente construida) sigue siendo el blanco de la alineacion y NO se cita en el informe.

# Correcciones a la Etapa 1 — §15 Estado del Arte

- **Fecha:** 2026-08-27 · **Sobre:** `Etapa 1.docx` (§15 completo, 22.169 palabras).
- **Para quién:** el redactor de la Etapa 1. El equipo de plataforma **no edita** esta
  sección; este documento dice **qué ajustar y contra qué**.
- **Objetivo del pase:** que el estado del arte quede **alineado con el proyecto que se
  construyó** — que cada modelo, método y protocolo que el §15 desarrolla tenga un rol en la
  tesis, y que cada resultado que el informe va a reportar más adelante (§17.5) tenga en el
  §15 su **vara** de literatura o su **brecha** declarada.
- **Regla que gobierna todo el pase — no-anacronismo:** el §15 narra el estado del arte
  *antes* del proyecto. **No entra ningún número medido por nosotros, ningún experimento
  propio, ninguna elección de diseño.** El §15 deja la vara (cifra publicada) o la brecha
  (lo que la literatura no responde); el cruce con lo medido se escribe en §17.5 y §18.
  Cuando abajo se cita una cifra del proyecto, es solo para explicar *qué vara falta* — esa
  cifra **no** va al §15.
- **IDs:** `E1-nn` comentarios (con prioridad 🔴 alta · 🟠 media · 🟡 baja) ·
  `PODA-nn` remite a la crítica de extensión ya existente (`ajustes/07`).

---

## 0. Alcance del archivo

**`Etapa 1.docx` cubre 1 de las 3 piezas de la Etapa 1.** La Etapa 1 del informe es
**§15 + §16 (Marco Teórico) + Anexo A**. El archivo trae §15 completo, nada de §16 y ninguna
tabla del Anexo A (las cita: "Tabla A.1", "Tabla A.3"). Tres consecuencias:

1. **§16 y Anexo A deben llegar como Etapa 1**, no como parte de la etapa siguiente
   (§17.1). El §16 todavía no fue relevado (`AJ-1.16`).
2. La corrección de licencias de GDINO 1.5 / DINO-X (`AJ-1.09`) quedó bien **en la prosa**
   del §15, pero la **Tabla A.1**, donde estaba la errata, no se puede verificar desde este
   archivo. Confirmar que también se corrigió.
3. El §15 apunta hacia adentro del §16 tres veces ("sección 16.5.1", "16.5.2.3 y 16.5.2.5")
   y una vez a algo que no existe en el §15 ("el modelado de apariencia descrito en el
   análisis del modelado de apariencia", §15.3.1.2). El §16.5 va a reestructurarse
   (PODA-06…09): **cerrar §15 y §16 juntos** para que estos punteros no queden rotos.

---

## 1. Qué es la plataforma (el blanco de la alineación)

Descripción en llano de lo que se construyó y midió, para decidir qué del §15 sostiene algo
y qué no. Todo esto está verificado en el código de los repositorios.

| Componente | Lo que se implementó | Lo que **no** se implementó |
|---|---|---|
| **Detectores** | Grounding DINO en dos backbones — **Swin-T** (campeón, a 560 px) y **Swin-B** (especialista en `bare_head`, a 560 px) — y **YOLOE-26** en tallas s/m/l/x (release de Ultralytics posterior al paper). MM-Grounding-DINO se evaluó y se descartó. | Ningún otro modelo del catálogo (OmDet-Turbo, OWL, Detic, Florence-2, APE, LLMDet, T-Rex2, Grounded SAM…). Sin segmentación. |
| **Uso de los modelos** | **Zero-shot** con calibración operativa: resolución, vocabulario (prompt sets congelados), umbrales, estabilización temporal. | — |
| **Fine-tuning** | Jornada experimental cerrada sobre **YOLOE-26s**, con las **dos recetas estándar de Ultralytics**: *linear probing* (solo la proyección de clases) y *full tuning*. Se **midió** la retención in-domain y la retención open-vocabulary. Ningún checkpoint se adoptó. | No se ajustó Grounding DINO. |
| **Identidad por sujeto (tracking)** | Tracker **propio y mínimo**: asociación por IoU entre cuadros, **sin filtro de Kalman ni modelo de apariencia**, determinista. Su valor se mide por su efecto en las alertas, **no con MOTA/IDF1/HOTA** (métricas MOT excluidas del alcance con causa). | Ni ByteTrack, ni OC-SORT, ni DeepSORT, ni end-to-end en la plataforma. (ByteTrack se usó solo como herramienta de preanotación de ground truth.) |
| **Ingesta de video** | **RTSP** (cámaras IP) y **captura por SDK** de una cámara inteligente (OAK-D, con prefiltrado en el dispositivo). Servidor de medios (`mediamtx`) solo como herramienta de desarrollo. | Ni WebRTC, ni HLS/DASH, ni RTMP, ni SRT, ni RIST, ni servidor de medios en producción. Sin inferencia en el borde. |
| **Interior del sistema** | Bus de eventos publish/subscribe entre el plano de detección y el motor de reglas (condiciones CR-01 sin casco / CR-02 sin chaleco, con histéresis temporal). | — |
| **Salida** | Alertas confirmadas distribuidas por **MQTT QoS 1** con idempotencia; consola web. | — |
| **Evaluación** | Benchmark de imágenes propio y congelado (3 fuentes, 6.477 imgs), benchmark de clips con GT humano, latencia extremo a extremo (G2A), tasa de falsas alarmas, persistencia mínima. | Métricas MOT. Benchmarks generales (COCO/LVIS) solo como referencia externa. |

---

## 2. Alineación: qué ajustar en cada bloque

### 2.1 §15.2 Detección OVD — bien encuadrado, con huecos de vara

El §15.2 ya dejó bien puestas la vara supervisada de EPP (YOLOR 0,883 SHEL5K con `head`
0,907; YOLOv5x 0,866 CHV; YOLOv9-e ≈0,71 SH17), la vara zero-shot OVD×EPP (Choi & Greer
2024; Chen & Zou 2025), la caída COCO→ODinW de GDINO, la convención de métricas
(AP 0,50:0,95 vs mAP@0,5, nunca en la misma columna) y la distinción "calibración operativa
vs adaptación paramétrica". Eso **no se toca**. Lo que falta:

**E1-01 · 🟠 · Swin-B no tiene vara.** El proyecto despliega **dos** backbones de Grounding
DINO y el §17.5 reportará ambos. El §15 da la cifra zero-shot de Swin-L (52,5 COCO) y de
Swin-T (≈48,4) pero **no menciona Swin-B**. Ojo con la trampa: la cifra publicada del
GroundingDINO-B en el README oficial (~56,7 AP COCO) **no es zero-shot** — COCO figura entre
sus datos de preentrenamiento (verificar en la fuente). Pedido: una oración en §15.2.1.1.3
que diga que la variante Swin-B se distribuye con pesos abiertos pero **sin cifra zero-shot
comparable**, y por qué. Sin esa oración, el §17.5 no tiene vara honesta para el
especialista.

**E1-02 · 🟡 · YOLOE-v8 (paper) vs YOLOE-26 (plataforma).** El §15 cita YOLOE-v8-S/L
(Wang et al., 2025). La plataforma corre **YOLOE-26**, release posterior de Ultralytics
sobre YOLO26 sin paper propio. Pedido: decir que la familia tiene variantes v8/11/26 y que
las cifras publicadas corresponden a v8; si no, el §17.5 compara `yoloe-26s` contra la vara
de v8-S sin aviso.

**E1-03 · 🟠 · Tabla 4, fila YOLOE — contradicción latente con §17.5.** La fila dice:
*Transferring (linear probing / full tuning) → Retención OVD "No" → "Modelo reparametrizado
como YOLO estándar"*. El proyecto ejerció **exactamente esas dos recetas** y **midió** la
retención open-vocabulary como un número. Si el §15 afirma "No" absoluto por
reparametrización, el §17.5 va a reportar una retención medida y el lector verá una
contradicción (¿cómo se mide lo que no existe?). Reformular, sin adelantar nada: *"No
evaluada por los autores; la receta estándar produce un modelo de vocabulario fijo; la
retención debe medirse re-inyectando el vocabulario abierto sobre el modelo ajustado."* Ese
enunciado es el que el §17.5 puede confirmar o refutar.

**E1-04 · 🟡 · §15.2.4.5 pesa donde no se ejerció.** ~60 % del texto de fine-tuning
desarrolla recetas para Grounding DINO (las tres estrategias de MM-GDINO, LoRA en imagen
médica). La jornada fue sobre YOLOE. No es un error — GDINO es el campeón y la brecha se
declara — pero la vara que el §17.5 va a citar es la del Bloque B (YOLOE), que hoy tiene
menos desarrollo. Equilibrar. Además, el resultado del fine-tuning se va a explicar por la
relación entre **tamaño del conjunto de ajuste y parámetros entrenables**; hoy la única
frase que lo ancla es "PEFT relevante para datasets de dominio reducidos". Agregar una
oración con fuente sobre esa relación como condición de la retención. *(Sin cifras
nuestras.)*

**E1-05 · 🟠 · El Bloque D está mal rotulado.** Título: "Modelos generativos guiados por
instrucciones". De sus 4 modelos, **3 no son generativos en inferencia**, y el propio texto lo
dice: APE "no depende de decodificación autoregresiva, produciendo predicciones estructuradas
de manera directa"; LLMDet "en inferencia opera como un detector OVD convencional sin LLM";
T-Rex2 "entra en el Bloque D por su foco en prompting generalista multimodal". La Tabla 2 lo
agrava: fila "Generativo guiado por instrucciones" con mecanismo "APE: predicción directa con
alineamiento por producto punto". Un jurado atento lo ve. Renombrar el bloque (por ejemplo
*"Modelos guiados por prompts generalistas: generativos e híbridos"*) y corregir la fila de
la Tabla 2; alternativa: mover APE/T-Rex2 al Bloque A y LLMDet a la ficha de MM-GDINO.

**E1-06 · 🟡 · Duplicación interna (es la superficie de PODA-01/02).** La introducción de
§15.2.1 (párrafos 2–8) ya describe GDINO, OmDet-Turbo, YOLO-World, YOLOE, OWL-ViT y Florence-2
con las mismas cifras que sus fichas de más abajo (52,5 AP; 35,9 AP a 102,5 FPS; etc.).
Criterio: los paradigmas en la introducción; **fichas completas solo para los modelos con rol
en la tesis** (Grounding DINO y MM-GDINO · YOLO-World y YOLOE · OWLv2 como único comparable
externo zero-shot sobre obra · GDINO 1.5/DINO-X como techo de API cerrada). El resto, una
línea en la Tabla A.1. La Tabla 3 se reduce a esas filas — y con ella se van las cifras aún
sin verificar de OmDet-Turbo (ver §3).

### 2.2 §15.3 Seguimiento multiobjeto — la recomendación del texto no es lo que se construyó

**E1-07 · 🟠 · §15.3.2.1 recomienda un método que el diseño no adoptó.** El cierre dice que
"ByteTrack y OC-SORT representan alternativas particularmente equilibradas" y que "la
familia SORT extendida se presenta como la opción más adecuada". La plataforma usa algo
**más simple que SORT** (asociación IoU, sin modelo de movimiento) y lo mide por alertas.
Cuando el §17.3 lo describa, el lector que vuelva al §15 verá que el estado del arte
"recomendaba otra cosa". El §15 no debe elegir método (eso es del diseño): reescribir el
cierre en clave de **criterios** — independencia respecto del detector, determinismo y
reproducibilidad, costo nulo de entrenamiento, transparencia para auditoría — que son los
que fundan lo construido, sin nombrar ganador. La ficha de SORT (tracking-by-detection +
IoU + asignación) es la vara conceptual que queda; los demás métodos, comprimidos en la
Tabla 6.

Erratas del bloque: "FairMOT" aparece en §15.3.2.1 sin haber sido introducido (la sección
presenta TrackFormer/MOTR) · §15.3.1.2 refiere a "el análisis del modelado de apariencia",
que no existe en el §15.

**E1-08 · 🟡 · §15.3.3 métricas MOT — comprimir, no eliminar (matiz a PODA-03).** PODA-03
pide eliminar §15.3.3 entero. Matiz: la tesis **excluye** MOTA/IDF1/HOTA con causa, y para
que el §17.1/§17.5 justifiquen esa exclusión el lector tiene que saber qué miden esas
métricas y por qué no capturan valor operativo. Ese argumento (último párrafo de §15.3.3.3)
es el que motiva medir por alerta. Dejar ~120 palabras: las tres métricas en una oración
cada una + ese párrafo. La ecuación (1) y las tres subsecciones sobran.

**E1-09 · 🟡 · Tabla 7.** La fila "ausencia de datasets de construcción con anotaciones de
tracking → protocolo propio con datos del proyecto" está **alineada** (el proyecto construyó
ese GT) — se queda. La fila "ausencia de semántica en identificadores… correlación
inter-cámara" está fuera del alcance (una cámara) — podable.

### 2.3 §15.4 Streaming — comprimir fuerte, con una excepción

**E1-10 · 🔴 · Aplicar PODA-04, conservando RTSP/RTP íntegro y §15.4.3 entero.** El §15.4
tiene **8.068 palabras** (protocolos 4.054 · servidores de medios 2.616) para una ingesta que
es **solo RTSP + SDK de cámara**. Ni WebRTC, ni HLS/DASH/CMAF, ni RTMP, ni SRT, ni RIST, ni
Janus/Kurento/OME/SRS sostienen una decisión del sistema construido. **Excepción, que la
crítica de extensión no había marcado:** el párrafo de RTSP/RTP (latencia ~200–800 ms en
condiciones favorables, dominada por el *play-out buffer* del receptor — Axis 2015) es la
**única vara de literatura** para la latencia de captura que el §17.5 va a reportar y para la
regla de que la latencia extremo a extremo se descompone en captura + procesamiento. **Ese
párrafo se queda entero.** Y **§15.4.3 (brechas) se queda entero**: §15.4.3.1 "ausencia de
benchmarks end-to-end integrados para pipelines OVD" es exactamente la brecha que la
medición de latencia del proyecto ocupa — es de las mejores piezas del §15. Todo lo demás se
comprime a una tabla-mapa de protocolos de ingesta (la Tabla 8 ya casi lo es) más un párrafo
de criterios. La *justificación* de la elección (RTSP en la entrada, bus de eventos adentro)
no va acá: es del §17.1/§17.3.

**E1-11 · 🟠 · Falta la vara de dos cosas que sí se construyeron.**
(a) **Ingesta por SDK de cámara inteligente** (OAK-D, prefiltrado en el dispositivo): el
§15.4 solo conoce protocolos de red. Si la cobertura vive en §16.5.4 (borde), el §15.4 debe
al menos nombrar la captura por SDK como alternativa al stream de red.
(b) **Distribución de alertas por mensajería pub/sub (MQTT QoS 1)**: es un componente
implementado y medido y **no tiene una sola línea de estado del arte** — ni protocolos de
mensajería IoT, ni garantías de entrega, ni idempotencia. §15.4.3.4 habla de "la
notificación al operador" sin fuente. Un párrafo con fuente, o dejar declarado que lo cubre
el §16/§17.3. Sin vara, la latencia de distribución que reporte el §17.5 queda flotando.

**E1-12 · 🔴 · Texto de instrucción colado al informe.** §15.4.1.2 (RTMP): *"Esto es clave
para la plantilla: cuando el documento menciona latencias, debe quedar claro que…"*. Es una
directiva de redacción, no prosa del informe. Eliminar. Es 🔴 no por gravedad técnica sino
porque delata el proceso ante el jurado.

Erratas del bloque: "jitter en el receptor.." (doble punto) · "Ahmad et al., 2005" es un
paper de **transcodificación** y está citado para "el comportamiento bajo carga" de Janus
(§15.4.2.5) — atribución errónea; bastan Amirante 2014/2015 · Tabla 8 rotula RTSP/RTP como
"Pull" mientras §15.4.1.1 alinea RTP con *push* (RTSP controla, RTP empuja: decirlo así o
unificar).

### 2.4 Lo que está bien alineado — no tocar

- §15.2.5.1 contextualización limitada → justifica un motor de reglas sobre las detecciones. ✔
- §15.2.5.2 sin consistencia temporal nativa → justifica estabilización temporal e identidad
  por sujeto. ✔
- §15.2.5.3 sensibilidad al prompt → justifica prompt sets congelados; y Choi & Greer
  (asociación jerárquica: `head` 0,1024 vs `hardhat` 0,6493) es la vara natural para
  comparar formulaciones directas e indirectas del vocabulario. ✔
- §15.2.5.4 / §15.2.5.5 → baseline zero-shot propia, test congelado, latencia de alerta,
  tasa de falsas alarmas, persistencia mínima: es exactamente el protocolo que se ejerció. ✔
- §15.2.2 composición de pipelines → la arquitectura **es** composición (detector + tracker
  + motor de reglas + distribución). ✔ El ejemplo es Grounded SAM y no hay segmentación en la
  tesis: podable a la mitad, conservando la idea.
- §15.2.6 calibración operativa vs adaptación paramétrica → el encuadre correcto. ✔

---

## 3. Pendientes del pase de corrección anterior

Del tablero `AJ-1.01…1.16` quedaron **12 resueltos**. Falta:

| ID | Qué falta |
|---|---|
| AJ-1.04 | OmDet-Turbo-Tiny "30,3 AP LVIS-minival" (Tabla 3 y ficha): probable *mislabel* de ODinW-13. Verificar contra el paper y corregir o anotar. (Si se aplica E1-06, la fila se va.) |
| AJ-1.05 | OmDet-Turbo-Base "53,4 AP COCO bajo evaluación zero-shot": verificar que sea zero-shot; si no, etiquetar. |
| AJ-1.09 | Confirmar la Tabla A.1 del Anexo A (la prosa ya está bien). |
| AJ-1.16 | Relevar el §16 — llega con la segunda pieza de la Etapa 1. |
| Cifra nueva | "Grounding DINO Swin-L alcanza 63,0 AP en COCO tras fine-tuning closed-set" (§15.2.4.5) entró sin pasar el filtro de verificación. Plausible (paper: 62,6 val / 63,0 test-dev): declarar el split. |

---

## 4. Poda: el pase no se aplicó

La crítica de extensión (`ajustes/07`) fijó que la poda se aplica **en el mismo pase** que las
correcciones. Ese pase no vino:

| Bloque | Palabras hoy | Poda propuesta | Aplicada |
|---|---:|---|---|
| §15 total | 22.169 | ~−11.900 | no |
| §15.2.1 catálogo de modelos | 4.777 | PODA-01 −2.000 (ver E1-06) | no |
| §15.2.3 + §15.2.4 síntesis duplicada | 3.877 | PODA-02 fusionar en una, −1.500 | no |
| §15.3 MOT | 2.530 | PODA-03 −1.600 (ver matiz E1-08) | no |
| §15.4 streaming y servidores | 8.068 | **PODA-04 −6.800** (ver excepción E1-10) | **no** |

El criterio de poda **no es cuota, es aporte**: una sección se queda si sostiene un
resultado, una decisión de diseño o un argumento de defensa. Las adiciones de vara
(AJ-1.01/1.13, E1-01/02/11) mandan sobre las podas: la poda les hace lugar.

---

## 5. Decisiones del equipo (marcar antes de enviar)

| ID | Decisión | Recomendación | ✔ |
|---|---|---|---|
| D-E1-1 | ¿La poda de §15 se aplica **en este pase** o en un pase transversal al final? | En este pase. §16 es Etapa 1 también y trae PODA-05…11; los punteros §15→§16.5 se arreglan una sola vez. | [ ] |
| D-E1-2 | ¿§16 y Anexo A llegan como **Etapa 1**, antes de §17.1? | Sí, en un `.docx` propio. | [ ] |
| D-E1-3 | Excepción a PODA-04: conservar RTSP/RTP íntegro y §15.4.3 entero. | Sí. Anotar la enmienda en `ajustes/07`. | [ ] |
| D-E1-4 | Tabla A.1: confirmar licencias corregidas y resolver PODA-17. | Migrar la Tabla A.1 corregida al Anexo B; eliminar el resto del Anexo A. | [ ] |
| D-E1-5 | Bloque D: renombrar vs mover modelos. | Renombrar y corregir la fila de la Tabla 2 — menor cirugía. | [ ] |
| D-E1-6 | Al cerrar el pase: re-extraer el §15 a `entregable/` y fechar en `00-el-informe-hoy.md` (regla D-C); versionar el `.docx` como los demás (`…Seccion_15_Estado_del_Arte_v1.x.docx`). | Hacerlo al cerrar, no antes. | [ ] |

---

## 6. Orden sugerido

1. **Erratas duras** (sin decisión): E1-12 · Ahmad 2005 · doble punto · FairMOT · referencia
   colgada §15.3.1.2 · Tabla 8 push/pull · split del 63,0 · AJ-1.04/1.05.
2. **Alineación**: E1-01 Swin-B · E1-02 YOLOE-26 · E1-03 Tabla 4 · E1-05 Bloque D ·
   E1-07 cierre de §15.3.2.1 · E1-11 SDK + MQTT.
3. **Poda** (con D-E1-1/D-E1-3): PODA-01/02 (E1-06) · PODA-03 con E1-08 · PODA-04 con E1-10 ·
   E1-09.
4. **§16 y Anexo A** como Etapa 1 (D-E1-2): AJ-1.16 · PODA-05…11 · D-E1-4 · reparar los
   punteros desde §15.
5. **Cierre**: D-E1-6.

---

## Fuente: `docs/informe/entregable/desarrollando/archivado/correcciones-etapa-1-pase-2.md`

> SHA-256 del bloque: `3b045781d1eab95f146589b17e8ff81db96b018db5829f40ac023a7887c1bc89`  
> Seleccion: pase 2 (2026-08-27): revision de la primera iteracion y E1-13 a E1-23. YA APLICADO Y VERIFICADO (su seccion 6) salvo tres RESIDUALES que SI son trabajo pendiente: R1 (una fila de la Tabla 4 sin sostener en prosa), R2 (formato de la ficha de Florence-2) y R3 (delta de referencias: altas Kumar 2022, Lee 2023, OASIS 2019, Ultralytics 2026; Luxonis lleva letra s. f.-b; bajas de PODA-18). Sus decisiones D-E1-7 (la Tabla A.1 se conserva y corrige: PODA-17 invertida) y D-E1-8 rigen.

# Correcciones a la Etapa 1 — pase 2: revisión de la iteración de GPT sobre §15

- **Fecha:** 2026-08-27 · **Sobre:** `desarrollando/Etapa 1 — copia ajustada E1 2026-08-27.docx`
  (10.870 palabras; sin control de cambios ni comentarios).
- **Contra qué se revisa:** el texto base `90d` (22.266 palabras) y el pase 1
  (`correcciones-etapa-1.md`: E1-01…E1-12, AJ- abiertos, podas con dos enmiendas, guardrails).
- **Tres preguntas que ordenan la revisión:** (1) ¿cumplió lo pedido? (2) ¿la reducción a la
  mitad está justificada por aporte, o hubo poda por poda? (3) ¿sigue siendo un estado del
  arte de tesis, o quedó un texto acomodado a nuestro diseño?
- **IDs:** los comentarios nuevos continúan la serie: **E1-13…E1-23**. Las decisiones nuevas:
  **D-E1-7, D-E1-8**. Nada de esto está aplicado.

---

## 0. Veredicto en cuatro líneas

1. **Cumplimiento: alto.** 11 de los 12 `E1-` están aplicados; el que falta (E1-06) es el de
   menor peso. Los `AJ-` abiertos quedaron resueltos (dos de ellos por eliminación). Cero
   fugas de andamiaje, cero resultados propios: la regla de no-anacronismo se respetó.
2. **Extensión: justificada en el agregado.** 22.266 → 10.870 palabras (−51 %). La poda
   pre-autorizada (`ajustes/07`, PODA-01…04 con las enmiendas del pase 1) proyectaba
   ~10.300. GPT cortó **lo que se le dijo que cortara y conservó lo que se le dijo que
   conservara** (§15.2.5 brechas 0 % · §15.4.3 brechas 0 % · RTSP/RTP · Tabla 8 · las 7
   tablas). No hay poda por poda **en el qué**; hay daño colateral **en el cómo**.
3. **Daño colateral: seis puntos concretos**, todos de una misma clase — *la prosa se
   comprimió más rápido que lo que dependía de ella*: tablas que quedaron con filas que el
   texto ya no explica, una brecha que cita un análisis borrado, numeración con huecos, un
   paradigma sin ficha, citas huérfanas en notas, y la síntesis de licencias perdida.
4. **Registro de tesis: se sostiene, con dos correcciones.** Dos pasajes nuevos afirman en
   voz normativa —y sin fuente— criterios que son *nuestros* (los tres niveles de evaluación
   del proyecto; los criterios de selección del tracker). Un jurado los leería como "el
   autor decide y lo disfraza de literatura". Se corrigen convirtiéndolos en brecha con cita.

---

## 1. Cumplimiento del pase 1

| Unidad | Estado | Dónde / observación |
|---|---|---|
| E1-01 Swin-B sin vara | ✅ | §15.2.1.1.3, párrafo nuevo: pesos públicos, sin cifra zero-shot comparable porque COCO está en su entrenamiento. **Pero** se asentó como hecho lo que el pase 1 marcó **[R] a verificar**, y cita "(IDEA-Research, 2024)" **sin letra**, colisionando con 2024a/b/c → E1-21 |
| E1-02 YOLOE-v8 vs YOLOE-26 | ✅ | §15.2.1.2.2: "los resultados publicados para YOLOE-v8 no deben utilizarse como si fueran una medición de las variantes YOLOE-26" (Ultralytics, 2026) |
| E1-03 Tabla 4 fila YOLOE | ✅ | Fila reescrita: "No evaluada por los autores · la receta estándar produce vocabulario fijo; la retención requiere reinyectar y evaluar vocabulario abierto". La prosa (§15.2.4 ¶4) lo acompaña |
| E1-04 equilibrar fine-tuning | ✅ parcial | Se sumó la vara tamaño-de-datos/parámetros (Kumar et al., 2022; Lee et al., 2022) y YOLOE ganó peso. El costo: la Tabla 4 quedó sin sostén → E1-14 |
| E1-05 Bloque D mal rotulado | ✅ | Renombrado "Modelos guiados por prompts generalistas: generativos e híbridos"; fila de Tabla 2 corregida. El costo: el bloque quedó **sin ninguna ficha** → E1-13 |
| E1-06 duplicación intro/fichas | ❌ | Los párrafos 2–8 de §15.2.1 están **idénticos** al base: siguen dando 52,5 AP, 35,9 AP @102,5 FPS, etc., que las fichas repiten → E1-19 |
| E1-07 cierre de §15.3.2.1 | ✅ | Reescrito en criterios, "no una elección anticipada de un tracker particular". FairMOT y la referencia colgada desaparecieron. **Pero** el párrafo quedó **sin una sola cita** → E1-16 |
| E1-08 métricas MOT comprimir | ✅ | 126 palabras, una oración por métrica + el argumento del valor operativo. Ecuación fuera |
| E1-09 Tabla 7 | ✅ | Fila inter-cámara eliminada; fila de datasets conservada |
| E1-10 PODA-04 con excepción | ✅ | RTSP/RTP íntegro en lo esencial (200–800 ms, play-out buffer, Axis 2015, ONVIF); **§15.4.3 intacta (0 %)**; Tabla 8 completa |
| E1-11a ingesta por SDK | ✅ | §15.4.2 ¶2 (Luxonis, s. f.), sin equipararla a inferencia en el borde |
| E1-11b MQTT / pub-sub | ✅ | §15.4.2 ¶4 (OASIS, 2019): QoS 1, PUBACK, reentregas, idempotencia |
| E1-12 texto de plantilla | ✅ | Desapareció con el párrafo de RTMP |
| Erratas: Ahmad 2005 · ".." · FairMOT · Tabla 8 push/pull · split del 63,0 | ✅ | Ahmad 2005 ahora sostiene *transcodificación* (uso correcto); Tabla 8: "RTSP controla la sesión; RTP transporta el flujo"; "62,6 AP en COCO val y 63,0 AP en test-dev" |
| AJ-1.04 / AJ-1.05 (OmDet-Turbo) | ✅ por eliminación | Ficha y filas de Tabla 3 eliminadas. Queda una cita huérfana en la Fuente de Tabla 3 → E1-20 |
| AJ-1.09 Tabla A.1 · AJ-1.16 §16 | — | Fuera de este `.docx`. Ver D-E1-7 |

---

## 2. La extensión: qué se cortó y si estaba justificado

| Bloque | Base | GPT | Δ | Qué salió | Juicio |
|---|---:|---:|---:|---|---|
| §15.1 alcance | 181 | 181 | 0 % | — | ✅ |
| §15.2.1 paradigmas y fichas | 4.641 | 2.070 | −55 % | Fichas de GLIP/GLIPv2, OV-DETR, OV-DINO, OmDet-Turbo, Detic, DetCLIP; las 4 del Bloque D colapsadas a un párrafo; **Bloque E completo** (Grounded SAM, OVTrack, Roboflow Rapid) | ✅ es exactamente PODA-01 (quedan los modelos con rol + techo de API cerrada). Tres pérdidas a reparar: numeración (E1-13), paradigma 4 sin ficha (E1-13), genealogía GLIP (E1-18) |
| §15.2.2 composición | 665 | 128 | −81 % | La descripción larga de Grounded SAM/SAM 2 | ✅ la idea (desacoplar etapas, costo del pipeline completo) sobrevive y es la que la plataforma necesita; no hay segmentación en la tesis |
| §15.2.3 síntesis + Tabla 2/3 | 1.129 | 1.088 | −4 % | Filas de OmDet en Tabla 3 | ✅ |
| ex-§15.2.4 ventajas/limitaciones (.1–.4) | ~1.000 | 0 | −100 % | Eficiencia (duplicaba 15.2.3) · generalización · **licencias y riesgo de adopción** · segmentación (duplicaba 15.2.2) | ⚠ tres de las cuatro eran duplicación (PODA-02). **La de licencias no**: es criterio de selección declarado y se perdió su síntesis → E1-17 |
| §15.2.4 fine-tuning (ex-.5) | 2.688 | 885 | −67 % | Las recetas de MM-GDINO en detalle, LoRA médico (Rasaee), el hallazgo del text encoder frágil de YOLO-World, OWL-ST/n-gramas, Florence-2 LoRA (Ucar/Skalski), *catastrophic forgetting* (Kirkpatrick) | ⚠ la compresión es defendible, pero **la Tabla 4 conserva 11 filas que nombran esas recetas** y la prosa ya no las presenta → E1-14 |
| **§15.2.5 brechas + Tabla 5** | 1.737 | 1.737 | **0 %** | — | ✅ **el núcleo, intacto** |
| §15.2.6 cierre | 161 | 161 | 0 % | — | ✅ |
| §15.3.1 métodos MOT | 806 | 277 | −66 % | Fichas de DeepSORT/ByteTrack/OC-SORT/BoT-SORT → un párrafo de contraste | ✅ PODA-03; Tabla 6 conserva la comparativa completa |
| §15.3.2 síntesis + Tabla 6 | 554 | 436 | −21 % | — | ✅ (ver E1-16 por las citas) |
| §15.3.3 métricas | 373 | 126 | −66 % | Tres subsecciones y la ecuación | ✅ E1-08 (ver E1-16 por el cierre) |
| §15.3.4 brechas + Tabla 7 | 633 | 567 | −10 % | Fila inter-cámara | ✅ |
| §15.4.1 protocolos | 4.025 | 1.039 | −74 % | RTMP, HLS/DASH/CMAF, WebRTC, SRT, RIST en prosa (→ un párrafo en 15.4.2) | ✅ PODA-04 con la excepción cumplida: criterios de clasificación + RTSP/RTP íntegros |
| §15.4.2 servidores → "alternativas complementarias" | 2.544 | 322 | −87 % | Roles del servidor en detalle, observabilidad, edge/cloud/híbrido, Janus/Kurento/MediaMTX/OME/SRS | ✅ nada de eso sostiene una decisión; el reemplazo trae lo que faltaba (SDK, MQTT). Una consecuencia sin reparar → E1-15 |
| **§15.4.3 brechas** | 737 | 737 | **0 %** | — | ✅ **intacta, como se pidió** |
| §15.4.4 síntesis + Tabla 8 | 589 | 594 | +1 % | — | ✅ |
| **Total** | **22.266** | **10.870** | **−51 %** | | **Dentro del 5 % de lo pre-autorizado (~10.300)** |

**Lectura:** la mitad que se fue es la mitad que el `07` había identificado hace dos
semanas como *survey de tecnologías no usadas* (16 % del informe entre §15.4 y §15.3) y
*catálogo sin uso posterior* (25 modelos para 3 familias evaluadas). Lo que sostiene un
argumento de defensa —las brechas, las varas, las tablas de síntesis— está **palabra por
palabra**. La reducción de páginas está justificada. Lo que hay que arreglar es el
**acabado**: seis lugares donde el texto comprimido dejó colgando algo que dependía de él.

---

## 3. Lo que no cumplió o hay que mejorar

### 3.1 Consecuencias de la compresión (acabado)

**E1-13 · 🟠 · Numeración con huecos y un paradigma sin ficha.** Al borrar fichas se
conservaron los números viejos: el Bloque A pasa de su título a **15.2.1.1.3** (Grounding
DINO) y **15.2.1.1.5** (DINO-X) — faltan .1, .2 y .4, y se ve en el índice. Renumerar
(.1 y .2). Además, el **Bloque D quedó sin ninguna ficha** mientras A, B y C conservan el
formato *Arquitectura · Mecanismo · Resultados · Licencia*: el paradigma 4 de la
introducción (generativo, Florence-2) es el único de los cuatro **sin desarrollo propio**.
Restituir una ficha breve de Florence-2 (~120 palabras: seq2seq, DaViT, FLD-5B, 37,5 mAP
COCO zero-shot, MIT) — es el representante declarado del paradigma y aparece en Tabla 2,
Tabla 4 y §15.2.5.2.

**E1-14 · 🟠 · Tabla 4 quedó sin sostén en la prosa.** De sus 11 filas, **7 nombran recetas
que el texto ya no presenta**: "MixedGroundingDataset", "MultiModalDataset",
"Reparametrización eficiente (sin RepVL-PAN)", "Adaptación LoRA", "Self-training (OWL-ST)
con pseudo-anotaciones / n-gramas", "Florence-2 fine-tuning con LoRA". Su Fuente cita a
Rasaee (2025) y Ucar (2025), que no aparecen en ningún párrafo. Una tabla con términos que
el lector no encontró antes es indefendible. Dos salidas, elegir una: (a) restituir **una
oración por familia** que nombre la receta (≈150 palabras en total), o (b) reducir la
Tabla 4 a las filas que la prosa sostiene (GDINO closed/open-set, YOLO-World con/sin
encoder, YOLOE transferring, OWL-ST). Recomendación: (a) — la tabla es el resumen que
§17.5 va a citar. Errata en el mismo bloque: dos oraciones seguidas anuncian la tabla
("La Tabla 4 resume…" / "La Tabla 4 sintetiza…"); dejar una.

**E1-15 · 🟠 · §15.4.3.3 cita un análisis que fue borrado.** Dice: *"Si bien se estableció
un mapa de roles potenciales por familia de protocolos y se analizaron las capacidades de
interoperabilidad de servidores de medios de código abierto…"*. Ese análisis (ex-§15.4.2.5)
ya no existe. Reescribir el arranque: *"Aun cuando la literatura describe los roles del
servidor de medios (§15.4.2), no ofrece evidencia consolidada sobre el overhead real…"*.

**E1-17 · 🟡 · Se perdió la síntesis de licencias.** La ex-§15.2.4.3 ("Licencias y riesgo
de adopción") no era duplicación: reunía GPL-3.0 (YOLO-World) / AGPL-3.0 (YOLOE) /
CC BY-NC-SA (OV-DETR) frente a Apache-2.0 (GDINO, OmDet, LLMDet) y la API cerrada de
1.5/DINO-X, y cerraba con *"el régimen de disponibilidad se mantiene como criterio técnico
de evaluación"* — que es un criterio de selección que §17.1 usa. Hoy la información quedó
dispersa en las líneas "Licencia" de cada ficha y la Tabla A.1. Restituir **un párrafo**
(~100 palabras) en §15.2.3, después de la Tabla 2.

**E1-18 · 🟡 · Genealogía y vocabulario estándar.** Con GLIP eliminado, Grounding DINO
aparece sin su antecedente directo (el preentrenamiento por *grounding* región–palabra que
GDINO hereda). Una oración en §15.2.1.1.3 basta: *"Grounding DINO extiende la formulación
de detección como phrase grounding introducida por GLIP (Li et al., 2021)…"*. Del mismo
modo, el término *catastrophic forgetting* (Kirkpatrick et al., 2017) —el nombre estándar
del fenómeno que §15.2.4 describe— desapareció; conviene una mención, porque es el
vocabulario con el que el jurado va a preguntar.

**E1-19 · 🟡 · E1-06 sigue sin aplicar.** Los párrafos 2–8 de §15.2.1 son idénticos al
texto base y repiten las cifras de las fichas (52,5 AP Swin-L; 35,9 AP @102,5 FPS; OWL-ST
"más de mil millones"). Dos opciones: dejar la introducción **sin cifras** (solo el
mecanismo de cada paradigma) y que las cifras vivan en las fichas; o al revés. Recomendación:
la primera — la introducción explica *qué* es cada paradigma, las fichas *cuánto* rinden.

**E1-20 · 🟡 · Citas huérfanas en notas de tabla.** Tabla 3: la Fuente cita "T. Zhao et al.
(2024)" (OmDet-Turbo) y ya no hay fila de OmDet. Tabla 5: la Fuente cita "Zhou et al.
(2022a" (Detic, eliminado); las filas solo usan 2022b. Corregir las dos Fuentes. La Fuente
de la Tabla 8 cita ~12 obras que ya no aparecen en prosa (Pantos, DASH-IF, Roy, Sonono,
VSF, W3C…): APA lo admite —una tabla es una cita válida— pero hay que **decidirlo
conscientemente** (D-E1-8), porque esas entradas van a sobrevivir en la lista de
referencias sostenidas solo por una nota.

### 3.2 Registro de tesis (la pregunta 3)

Verificado: **no hay ningún resultado propio, ningún nombre de configuración, ningún
identificador de la plataforma** en el texto (`bench_v3`, E-IND, 560 px, ZeroMQ,
histéresis, umbrales: cero apariciones). Las brechas se cierran con *"la respuesta
experimental corresponde a las secciones posteriores"*. En eso el texto es un estado del
arte y no una justificación del diseño. Pero hay **dos pasajes nuevos** donde nuestro
marco se cuela en voz normativa y sin fuente:

**E1-16 · 🟠 · Dos párrafos prescriben criterios nuestros como si fueran literatura.**
(a) §15.3.3 cierra: *"la evaluación del seguimiento debe distinguirse de la evaluación del
**estado por persona** y de la **alerta temporal producida por la plataforma**"*. Esos son
los tres niveles de evaluación del proyecto (§17.1), enunciados aquí como conclusión del
estado del arte, sin cita. (b) §15.3.2.1 enumera como criterios *"independencia respecto
del detector, determinismo y reproducibilidad, ausencia de entrenamiento adicional y
transparencia de las reglas de asociación"* — que son exactamente las propiedades de
nuestro tracker — y el párrafo **no tiene una sola cita** (el original citaba a Adžemović,
2025, para la compatibilidad de los métodos geométricos con OVD). Un jurado lee: *"el
autor eligió y lo disfrazó de literatura"*. Corrección para (a): formularlo como **brecha**
—*"estas métricas caracterizan al tracker pero no miden el valor temporal de una alerta;
la evaluación de un sistema asistivo exige niveles adicionales, cuya definición
corresponde al protocolo experimental"*— sin los términos propios. Para (b): restituir la
cita de Adžemović (2025) y anclar los criterios en el hecho publicado (los métodos sin
apariencia no dependen de un dominio de entrenamiento), no en su deseabilidad.

**El resto del texto nuevo pasa la prueba.** El párrafo de MQTT (OASIS, 2019) describe
QoS 1 y la idempotencia como propiedades del estándar, no como nuestra política. El de SDK
(Luxonis, s. f.) evita explícitamente equipararlo a inferencia en el borde. El de Swin-B se
limita al régimen de la cifra. Los de Kumar/Lee traen literatura general de fine-tuning
que no conocía el texto y que es la vara correcta para lo que §17.5 va a decir.

### 3.3 Referencias y trazabilidad

**E1-21 · 🟠 · Seis referencias nuevas sin entrada verificable, y una colisión.** El pase
introdujo: *IDEA-Research (2024)* —**sin letra**, en un informe que ya tiene 2024a/b/c—,
*Ultralytics (2026)*, *Kumar et al. (2022)*, *Lee et al. (2022)*, *Luxonis (s. f.)*,
*OASIS (2019)*. Ninguna está en el `96e` actual. Pedir el **delta de referencias** (altas
completas en APA 7 con DOI/URL, y las bajas que PODA-18 arrastra: GLIP, OV-DETR, OV-DINO,
OmDet, Detic, DetCLIP, APE, T-Rex2, Grounded SAM, Roboflow, servidores de medios, RTMP/
HLS/SRT/RIST en prosa…). Dos verificaciones puntuales antes de que queden: (1) la
afirmación sobre GroundingDINO-B (COCO en su entrenamiento) se asentó **como hecho** y el
pase 1 la marcó **[R]**: confirmar contra el README oficial y citar esa entrada concreta;
(2) *Lee et al.* ("Surgical fine-tuning") es arXiv 2022 pero **ICLR 2023** — fijar el año
según la versión que se cite.

**E1-22 · 🟡 · El cuerpo ahora depende de la Tabla A.1.** §15.2.3 remite a *"la Tabla A.1
del Anexo A… matriz ampliada… modelos representativos según familia, mecanismo, métricas,
rendimiento y licenciamiento"* — y con las fichas podadas, **esa tabla es el único lugar
donde el estado del arte conserva su amplitud** (los ~25 modelos). PODA-17 proponía
eliminar el Anexo A. Ya no se puede: hay que **invertir PODA-17** — la Tabla A.1 se
conserva, se corrige (AJ-1.09, licencias de 1.5/DINO-X) y se le agregan las filas de los
modelos que salieron del cuerpo si no las tiene. → D-E1-7.

**E1-23 · proceso · El `.docx` llegó sin control de cambios ni bloque de trazabilidad.**
No hay forma de auditar qué se movió sin la extracción y el diff que hizo esta revisión.
Para la próxima iteración pedir **una de dos**: cambios controlados de Word, o el bloque
*diagnóstico · texto propuesto · trazabilidad* por unidad que INSTRUCCIONES exige.

---

## 4. Decisiones del equipo

| ID | Decisión | Recomendación | ✔ |
|---|---|---|---|
| D-E1-7 | PODA-17 (eliminar Anexo A) queda **invertida**: la Tabla A.1 se conserva y corrige, porque el cuerpo podado depende de ella para la amplitud del catálogo. Actualizar `ajustes/07` y la D-E1-4 del pase 1. | Sí. Es la forma de podar el cuerpo sin achicar el estado del arte. | [ ] |
| D-E1-8 | Referencias sostenidas solo por notas de tabla (Tabla 8: ~12 obras). ¿Se aceptan o se poda la Tabla 8 a las filas con prosa? | Aceptar: la Tabla 8 es la síntesis que §15.4.4 comenta, y APA admite la cita en tabla. Dejarlo declarado. | [ ] |

---

## 5. Instrucciones para la próxima iteración de GPT (en orden)

1. **Acabado de la poda** (sin cambiar el alcance de lo cortado): E1-13 renumerar y ficha
   breve de Florence-2 · E1-14 una oración por receta de la Tabla 4 y borrar la oración
   duplicada · E1-15 reescribir el arranque de §15.4.3.3 · E1-20 corregir las Fuentes de
   Tablas 3 y 5.
2. **Registro de tesis:** E1-16 (a) y (b) — brecha con cita, sin términos propios.
3. **Restituciones cortas:** E1-17 párrafo de licencias en §15.2.3 · E1-18 una oración de
   genealogía (GLIP) y una mención de *catastrophic forgetting*.
4. **E1-19** (E1-06 pendiente): introducción de §15.2.1 sin cifras.
5. **E1-21** delta de referencias completo + las dos verificaciones.
6. **Entregar con cambios controlados** (E1-23).

**Lo que NO hay que hacer:** volver a alargar. Ninguna de estas correcciones supera las
~600 palabras en total; el texto debe quedar en el orden de las 11.500. Y no volver a
aplicar E1-01…E1-12 ni los AJ- ya resueltos: están hechos.

---

## 6. ✎ Verificación de la nueva versión (2026-08-27, segunda iteración de GPT)

Se re-extrajo `Etapa 1 — copia ajustada E1 2026-08-27.docx` (segunda versión, 05:01) y se
hizo diff contra la primera. **10.870 → 10.725 palabras (−145): no volvió a alargar**, y
las restituciones pedidas se pagaron con la compresión de la introducción (E1-19).

| Unidad | Estado | Verificación |
|---|---|---|
| E1-13 numeración · ficha Florence-2 | ✅ | Bloque A renumerado **.1/.2**; Bloque D gana **15.2.1.4.1 Florence-2** (DaViT, seq2seq, FLD-5B 126 M imgs / 5,4 mil M anotaciones, 37,5 mAP COCO zero-shot, MIT — cifras correctas) |
| E1-14 Tabla 4 sin sostén | ✅ 10/11 | La prosa ya nombra MixedGroundingDataset, MultiModalDataset, reparametrización sin RepVL-PAN, LoRA (Rasaee), OWL-ST/n-gramas, Florence-2 LoRA (Ucar). Oración duplicada eliminada. **Residual R1** abajo |
| E1-15 §15.4.3.3 | ✅ | Arranca "Aun cuando la literatura describe los roles del servidor de medios… (§15.4.2)" |
| E1-16 registro de tesis | ✅ | (a) §15.3.3 cierra "la evaluación de un sistema asistivo exige niveles adicionales, cuya definición corresponde al protocolo experimental" — sin "estado por persona" ni "alerta temporal producida por la plataforma". (b) §15.3.2.1 cita Adžemović (2025) y Wojke et al. (2017), ya no enumera nuestros criterios, y cierra "por sí sola, no determina la elección de un tracker" |
| E1-17 licencias | ✅ | Párrafo nuevo en §15.2.3: GPL/AGPL vs Apache vs API cerrada; "distinguir entre licencia del código, licencia de los pesos y condiciones del servicio" — con 6 citas |
| E1-18 genealogía · término | ✅ | "Grounding DINO extiende la formulación de detección como phrase grounding introducida por GLIP (Li et al., 2021)"; "olvido catastrófico (catastrophic forgetting)… (Kirkpatrick et al., 2017)" |
| E1-19 (ex E1-06) intro sin cifras | ✅ | Los cuatro párrafos de paradigmas reescritos **sin ninguna cifra**; las cifras viven solo en las fichas |
| E1-20 Fuentes de Tablas 3 y 5 | ✅ | T. Zhao fuera de Tabla 3; Zhou 2022a fuera de Tabla 5 |
| E1-21 citas nuevas | ✅ parcial | IDEA-Research pasa a **2024c** — correcto: por orden APA de títulos, 2024a = DINO-X-API, 2024b = Grounded-SAM-2, 2024c = GroundingDINO. Lee → **2023** ✓. **La afirmación sobre Swin-B se verificó contra el README oficial** (`IDEA-Research/GroundingDINO`, tabla de checkpoints): fila GroundingDINO-B → Data `COCO,O365,GoldG,Cap4M,OpenImage,ODinW-35,RefCOCO`, box AP `56.7`; la T → `O365,GoldG,Cap4M`, `48.4 (zero-shot)`. **Exacto: deja de ser [R], es [P].** El delta de referencias sigue pendiente → R3 |
| E1-23 cambios controlados | ❌ | De nuevo cero `w:ins`/`w:del`, cero comentarios |
| No-anacronismo / fugas | ✅ | Cero identificadores de plataforma, cero andamiaje |

### Residuales (lo único que queda sobre el texto)

- **R1 · 🟡 · Tabla 4, fila "OWL-ViT/OWLv2 · Fine-tuning end-to-end con regularización · Parcial".** Es la única fila que la prosa ya no sostiene: "regularización" aparece solo en la tabla. Una oración en el párrafo de dual-encoders (*"el ajuste sobre datasets cerrados exige regularizar para no colapsar el espacio de embeddings compartido, Minderer et al., 2022"*) o eliminar la fila.
- **R2 · 🟡 · Formato de la ficha nueva.** Florence-2 lleva el rótulo "Arquitectura, entrenamiento y disponibilidad." **sin negrita**; las demás fichas usan rótulos en negrita. Y el punto quedó inconsistente entre fichas ("**Arquitectura base.**" vs "**Arquitectura base**."). Unificar al aplicar al maestro.
- **R3 · 🟠 · Delta de referencias, todavía no entregado.** Verificado contra `96e`: **existen** AILab-CVC 2024, Google 2022/2023, Kirkpatrick 2017, Li L. H. 2021 (GLIP), Microsoft 2024, THU-MIG 2025, IDEA-Research 2024a/c, Adžemović, Rasaee, Ucar. **No existen** y hay que darlas de alta en APA 7: *Kumar et al. (2022)* · *Lee et al. (2023)* · *OASIS (2019)* · *Ultralytics (2026)*. **Corregir** *Luxonis (s. f.)* → la entrada de `96e` es **"Luxonis. (s. f.-b). OAK-D Pro PoE"** — lleva letra. Y las **bajas** de PODA-18 (todo lo que dejó de citarse: OV-DETR, OV-DINO, OmDet, Detic, DetCLIP, Grounded SAM/SAM 2, OVTrack, Roboflow, Janus/Kurento/OME/SRS, RTMP/HLS/SRT/RIST en prosa, MEC…) — cuidando que lo citado solo en la nota de la Tabla 8 **se conserva** (D-E1-8).
- **R4 · proceso ·** tercera entrega sin cambios controlados. Si la próxima vuelve sin ellos, el equipo audita por extracción y diff como hasta ahora — funciona, pero cuesta una pasada.

**Estado del §15 al 2026-08-27 (noche): pase 1 y pase 2 APLICADOS Y VERIFICADOS**, salvo
R1–R3. El texto base del kit se re-extrajo de esta versión (`90d`). Lo que sigue de la Etapa
1 es **§16 y el Anexo A** (D-E1-2, D-E1-7).

---

## 7. Fuentes de esta revisión

Extracción de ambos `.docx` con `herramientas/extraer_informe.py` (2026-08-27); conteo de
palabras por encabezado numerado; diff textual por sección; búsqueda de identificadores de
plataforma y de andamiaje (cero hallazgos); verificación de citas nuevas contra los títulos
publicados. Pase 1: `correcciones-etapa-1.md`. Crítica de extensión: `ajustes/07`.

---

## Fuente: `docs/informe/entregable/desarrollando/archivado/correcciones-etapa-1-pase-5.md`

> SHA-256 del bloque: `057da506c6cf463d87626c5ba8ddc401d60165d2785ef335f74adddc32c9cff2`  
> Seleccion: pase 5 (2026-08-27/28): **YA APLICADO Y VERIFICADO** - NO volver a aplicarlo. Fue el pase de formato y terminologia (F1-F6); la entrega de GPT llego con cambios controlados y cumplio los seis. Su seccion de verificacion registra ademas E1-57 (una capacidad no implementada descrita como el sistema, corregida) y E1-58 (formato roto en mitad de palabra heredado del pase 3, reparado). **Con esto la ETAPA 1 queda CERRADA.**.

# Etapa 1 — pase 5: unificación de formato y terminología (versión final)

- **Fecha:** 2026-08-27 · **Sobre:** `Etapa 1 — final 2026-08-27.docx` (§15 y §16; 22.800
  palabras; 92 títulos; 13 tablas). **Es el archivo que se te entrega junto con este brief.**
- **Qué es este pase:** el último. **El contenido está cerrado y verificado** — cuatro pases
  aplicados y comprobados unidad por unidad (64 de 64). Lo que queda es que el documento
  quede **uniforme en formato y en terminología**, alineado a la convención de las secciones
  ya cerradas del informe (§17.3, §17.4, §17.5). Nada más.
- **Cómo trabajar:** dentro del Project, sobre el `.docx` entregado, **sin Drive**. El texto
  vigente también está en el knowledge (`90d`), pero **el entregable se construye editando
  este `.docx`**, no regenerándolo.

---

## 0. Límites — leer antes de tocar nada

Este pase **no es de redacción**. Se corrige formato; el texto queda como está.

**Prohibido:**
- Reescribir, resumir, ampliar, reordenar o "mejorar" párrafos. Ni uno.
- Tocar cifras, citas, años, nombres de modelos, filas o celdas de tablas (salvo los cambios
  de rótulo indicados abajo).
- Agregar o quitar párrafos, secciones, tablas, notas o referencias.
- Reaplicar cualquier corrección anterior: **ya están todas** (E1-01 a E1-56, las 16 `AJ-`,
  las 11 podas). Si algo parece faltar, **no lo agregues**: anótalo en el registro de cambios.
- Agregar Anexo A, Anexo B o listado de Referencias: **el entregable es solo el desarrollo**.
- Borrar o completar el marcador `[[PENDIENTE: … AAIP …]]` de §16.6.2.2: **viaja tal cual**.
- Cambiar el estilo de encabezado de ningún título (los 92 tienen su `Heading N` correcto).

**Criterio de aceptación:** el diff entre el archivo entregado y tu versión debe mostrar
**únicamente** los cambios de las secciones 1 a 6. El conteo de palabras debe quedar en
22.800 ± 60 (los cambios de terminología mueven unas pocas decenas, nada más).

---

## 1. Títulos: tipo frase (F1)

**Vara:** las secciones cerradas del informe usan títulos **tipo frase** — solo mayúscula
inicial, más nombres propios y siglas (85 de 86 títulos en §17.3/§17.4/§17.5). En Etapa 1
**39 de los 92 títulos** están en Title Case. Ejemplos:

| Hoy | Debe quedar |
|---|---|
| 15.2.1. Paradigmas Arquitectónicos y Modelos Representativos | 15.2.1. Paradigmas arquitectónicos y modelos representativos |
| 15.2.3. Síntesis Comparativa y Trade-Offs para Tiempo Real | 15.2.3. Síntesis comparativa y *trade-offs* para tiempo real |
| 16.2. Condiciones de Riesgo Observables | 16.2. Condiciones de riesgo observables |
| 16.5.2. Descomposición Instrumental de Glass-to-Algorithm | 16.5.2. Descomposición instrumental de Glass-to-Algorithm |

**Conservan mayúscula:** nombres propios y de modelos (Grounding DINO, DINO-X, YOLO-World,
YOLOE, OWL-ViT, OWLv2, Florence-2, SORT, CLIP), siglas (OVD, MOT, DETR, DINO, EPP, IoU),
Glass-to-Algorithm / Glass-to-Glass como denominaciones, y "Ley", "Decreto", "Resolución",
"ISO 45001".

**Los cuatro títulos de bloque** usan hoy dos separadores distintos ("Bloque A —" y
"Bloque B:", con un doble dos-puntos en el D). Unificar con **raya**:
- 15.2.1.1. Bloque A — Detectores end-to-end tipo DETR/DINO con fusión visión–lenguaje en el decoder
- 15.2.1.2. Bloque B — Detectores one-stage tipo YOLO con puntuación región–texto
- 15.2.1.3. Bloque C — Detectores basados en dual-encoders (CLIP-like) y matching por similitud
- 15.2.1.4. Bloque D — Modelos guiados por prompts generalistas: generativos e híbridos

Cambiar **solo las mayúsculas y el separador**: ni una palabra del título.

## 2. Rótulo de tabla: negrita simple (F2)

**Vara:** `**Tabla N**` en negrita, y el título de la tabla debajo **en itálica** (así están
las 29 tablas de §17.3–§17.5). En Etapa 1, las Tablas **2 a 8** llevan el rótulo en
negrita+itálica (`***Tabla 2***`) y las 9 a 12 en negrita simple. Pasar las siete a negrita
simple. Los títulos ya están en itálica: no tocar.

## 3. Rótulo de nota: *Nota.* en itálica (F3)

**Vara:** APA 7 — *Nota.* en itálica, con el punto dentro de la itálica, y el resto del
párrafo en redonda (es la forma de las seis notas de §17.5, la sección más reciente). Hoy
conviven cuatro variantes: `**Nota.**` (×5), `*Nota.*` (×4), `**Nota**.` (×1) y una
malformada `**Nota***.*` (Tabla 8). Unificar las 11 a *Nota.* itálica. La "Fuente: …" sigue
dentro del mismo párrafo, como está.

## 4. Rótulos de párrafo: negrita con el punto dentro (F4)

Las fichas usan `**Arquitectura base.**` (punto dentro de la negrita) en 24 de 28 casos.
Cuatro lo llevan fuera: `**Convención de lectura**.`, `**Alta latencia (>~3 s)**.`,
`**Latencia media (~0,5 a 3 s)**.` y `**Baja latencia (<~500 ms)**.` → mover el punto
dentro. Nada más en esos párrafos.

## 5. Terminología: una palabra por concepto (F5)

El documento debe ser **internamente consistente**; la convención para todo el informe se
fija en la integración, pero la Etapa 1 no puede usar tres palabras para lo mismo.

| Concepto | Hoy en el texto | Usar | Excepción que se conserva |
|---|---|---|---|
| unidad de video | **cuadro** (21) · fotograma (7) · *frame* (15) | **cuadro** | ninguna — "frame-a-frame", "frame-to-frame" y "frame-by-frame" pasan a **"cuadro a cuadro"** o "entre cuadros consecutivos" |
| latencia de punta a punta | **extremo a extremo** (4) · end-to-end (3) · E2E (2) | **extremo a extremo** | **"arquitecturas end-to-end"** (DETR) es término de arte: **se conserva** |
| asociación temporal | **seguimiento** (20) · tracking (19) | **seguimiento** en prosa | **"tracking-by-detection"** y "seguimiento multiobjeto (MOT)" se conservan como términos de arte |

**Se conservan tal como están** (son el vocabulario canónico del informe y de su glosario):
*open-vocabulary*, *zero-shot*, *fine-tuning*, *prompt*, *pipeline*, *benchmark*, *linear
probing*, *full tuning*, *phrase grounding*, *tracking-by-detection*, *ground truth*. No
traducirlos ni ponerlos en itálica donde no la tengan.

**Prueba de aceptación de F5:** al terminar, "fotograma" = 0, "frame" = 0 fuera de nombres
propios, "end-to-end" solo junto a "arquitecturas", "E2E" = 0, "tracking" solo dentro de
"tracking-by-detection".

## 6. Siglas: definir la primera vez (F6)

El glosario del informe (§11) ya define OVD, EPP, AP, FPS y MOT: **no se redefinen**. Faltan
tres, todas de una sola intervención:

- **IoU** — primera aparición en la "Convención de lectura" de §15.2.1: *"…AP promediado entre
  umbrales IoU de 0,50 a 0,95"* → *"…umbrales de intersección sobre unión (IoU) de 0,50 a
  0,95"*.
- **SFU** y **NACK** — aparecen solo en la Tabla 8 (fila WebRTC). Agregar a la Nota de esa
  tabla, junto a las siglas que ya define: *"SFU = Selective Forwarding Unit. NACK = Negative
  Acknowledgement."*
- **E2E** — desaparece con F5 (cabecera "Latencia típica E2E" → "Latencia típica extremo a
  extremo", y la Nota de la Tabla 8).

---

## 7. Lo que está bien y **no se toca**

- Los 92 títulos tienen su estilo `Heading N` correcto y la numeración es contigua.
- Las 13 tablas tienen columnas uniformes, título en itálica, nota y fuente, y mención en prosa.
- La ecuación (1) de §16.5.2 está centrada e introducida en prosa.
- Las 83 obras citadas están todas en el listado global (que **no** va en este archivo).
- El `[[PENDIENTE: …]]` de la AAIP.
- Los separadores decimales: **coma** decimal y **punto** de miles (19.587 y 25.326 son
  números de ley; 5.210, 1.000, 2.000 y 50.000 son miles). Todos correctos.
- Cero identificadores internos, cero resultados propios, cero andamiaje.

---

## 8. Forma de la entrega

1. **Un `.docx`**, construido editando el archivo entregado — no un documento regenerado.
2. **Con cambios controlados activados**, para que cada cambio de F1–F6 sea visible.
3. **Estilos intactos**: mismo `Heading N` en cada título; sin negrita imitando títulos; sin
   markdown crudo (`###`, `|---|`).
4. **Un registro de cambios** al pie del chat (no dentro del documento), con el conteo por
   ítem: títulos cambiados (esperado 39 + 4 de bloque) · rótulos de tabla (7) · notas (11)
   · rótulos de párrafo (4) · reemplazos de terminología por palabra · siglas (3). Si algún
   conteo difiere de lo esperado, decir cuál y por qué.
5. **Sin** Anexo A, Anexo B ni Referencias.

## ✎ Verificación de la entrega (2026-08-28)

**Entrega:** `Etapa_1_final_ajustada_pase_5.docx` (22.846 palabras; **con cambios controlados:
173 inserciones / 170 borrados — la primera entrega que los trae**).

| Ítem | Resultado |
|---|---|
| F1 títulos tipo frase | ✅ 39 → 0 (el único "Title Case" residual es *Glass-to-Algorithm*, nombre propio) · los cuatro Bloques con raya |
| F2 rótulo de tabla | ✅ 11 × `**Tabla N**`, ninguno en negrita+itálica |
| F3 rótulo de nota | ✅ 11 × `*Nota.*`, una sola variante |
| F4 punto dentro del rótulo | ✅ 0 casos con el punto fuera |
| F5 terminología | ✅ fotograma 0 · frame 0 · E2E 0 · "end-to-end" solo en "arquitecturas end-to-end" (×2 + título del Bloque A) · "tracking" solo en *tracking-by-detection* y en el nombre de SORT |
| F6 siglas | ✅ IoU definida en la Convención de lectura · SFU y NACK en la Nota de la Tabla 8 |
| Contenido | ✅ las 26 líneas de prosa que cambiaron son todas terminología o rótulo; 22.798 → 22.846 palabras (+48, dentro del ± 60) |
| Verificador | ✅ OK, exit 0 |

**Lectura completa de punta a punta** (las 22.800 palabras, contra el diseño y la
implementación de la plataforma). Dos cosas que ningún pase anterior había visto:

- **E1-57 · 🟠 · una capacidad no implementada descrita como el sistema.** §15.4.3.1 decía que
  la brecha impide predecir *"el desempeño de un sistema que combina **ingesta
  multi-protocolo, decodificación acelerada**, inferencia OVD y emisión de eventos"*. La
  plataforma no tiene ni lo uno ni lo otro (ingesta RTSP + SDK; decodificación por software).
  Texto heredado del v1.1 que PODA-04 conservó al proteger §15.4.3. Corregido a *"ingesta de
  video, inferencia OVD y emisión de eventos"*.
- **E1-58 · 🟠 · formato roto en mitad de palabra.** Tres frases de §16.5.2, §16.5.4 y §16.5.5
  llevaban runs en **negrita+itálica que empezaban y terminaban dentro de una palabra**
  (*"pro|tocolo reproducible sin anticipar la s|elección"*): en Word se ven letras sueltas en
  cursiva negrita. Más el título §16.6.2.1 con negrita parcial a nivel de run. **Venía desde
  la entrega del pase 3** (verificado en las cuatro versiones), no es de esta pasada. Los
  cuatro casos se repararon quitando el formato de run; el estilo del párrafo gobierna.

Ambos arreglos se aplicaron de forma determinista sobre el `.docx`, con validación XML
previa. **Diff contra la entrega: solo los cuatro párrafos afectados.** Verificador OK.

**Documento final de la Etapa 1: `E-OVRT-VDP_Secciones_15_y_16_Estado_del_Arte_y_Marco_Teorico_v1.0.docx`.** La entrega de GPT y el
final previo quedaron en `archivado/`.

**Tres frases que NO se tocaron y conviene saber que existen:** *"sin anticipar la estrategia
que adopte el diseño"* (§16.3.4), *"sin anticipar la selección del stack"* (§16.5.5) y *"no se
anticipa en esta sección"* (§16.7.3). Son la regla de no-anacronismo **filtrándose a la prosa**
como comentario del autor sobre su propio texto. Correctas, pero un jurado las lee como
meta-texto. Si se quiere pulir, es borrar la cláusula final de cada una — tres tijeretazos que
pueden hacerse al integrar al maestro.

## 9. Cómo se va a verificar

El equipo corre `verificar_entregable.py` (debe dar **OK**) y un diff palabra por palabra
contra el archivo entregado. **Cualquier cambio fuera de F1–F6 hace rechazar la entrega
entera**, aunque sea una mejora. Si algo del contenido te parece incorrecto, **no lo
corrijas**: anótalo en el registro de cambios y el equipo lo evalúa.

---

## Fuente: `docs/informe/entregable/desarrollando/archivado/correcciones-etapa-1-pase-4.md`

> SHA-256 del bloque: `e43847e0116fba2c3ec40c0d5520519fa4e7dc50ecf780b92b858e86fcdf0820`  
> Seleccion: pase 4 (2026-08-27): **YA APLICADO Y VERIFICADO** - E1-52 y E1-53 se repararon de forma deterministica sobre el .docx (estilos de encabezado trasplantados de hermanas sanas y renumeracion 16.7.6 a 16.7.3), con prueba de no-regresion: el texto quedo identico. **El CONTENIDO de la etapa 1 esta CERRADO; el unico trabajo activo es el pase 5 (formato y terminologia).** Su seccion 0 certifica que entro el pase 3 completo y su seccion 2 fija el flujo obligatorio: **se trabaja dentro del Project, NO sobre Drive**.

# Correcciones a la Etapa 1 — pase 4: cierre de formato y flujo de trabajo

- **Fecha:** 2026-08-27 · **Sobre:** `Etapa 1 — copia ajustada E1 2026-08-27 (2).docx`
  (26.685 palabras: §15 + §16 + Anexo A + Referencias).
- **Qué es:** el pase más corto de la serie. **El contenido de la Etapa 1 está cerrado.** Lo
  que queda son **dos defectos de formato** y una **regla de flujo de trabajo** para que no
  vuelvan a aparecer.
- **IDs:** **E1-52** y **E1-53**.

---

## 0. Veredicto: el pase 3 se aplicó, y bien

Verificado por diff contra la entrega anterior y por extracción. **Todo lo sustantivo entró:**

| Unidad | Estado | Verificación |
|---|---|---|
| **E1-25** el mecanismo central de la tesis | ✅ **lo mejor del pase** | §16.3.4 nueva: *"Composicionalidad, Negación y Condiciones Definidas por Ausencia"*, con ARO (Yuksekgonul et al., 2023) y Winoground (Thrush et al., 2022), y las **dos formulaciones** enunciadas como alternativas conceptuales sin decir cuál eligió el proyecto. Exactamente lo pedido |
| **E1-24** la contradicción con §15 | ✅ | La afirmación sobre familias arquitectónicas desapareció de §16.3.5 **y** de §16.7; el puntero roto "§15.2.4.5" también |
| **E1-36** la ecuación vacía | ✅ | `t_G2A = t_capture + t_transport + t_preprocess + t_inference (1)` |
| **E1-37** descomposición de 4 componentes | ✅ | §16.5.2 reescrita como *"Descomposición Instrumental de Glass-to-Algorithm"*, con `t_preprocess` definido y su fila propia |
| **E1-38** productor/consumidor y pub-sub | ✅ | §16.5.3 *"Separación de Planos y Flujo Productor-Consumidor"*; MQTT ×3, Cugola ×3, contrapresión presente |
| **E1-26** las cuatro secciones de criterios | ✅ | §16.3.6 pasó a *"Dimensiones de Comparación de Modelos OVD"*; §16.4.4, §16.5.5 y §16.7.4 eliminadas o reconvertidas |
| **E1-44 / E1-45** §16.7.4 y §16.7.5 | ✅ | Ambas eliminadas; *"event sourcing"* ya no aparece |
| **E1-46** Tabla 12 | ✅ | Columna renombrada a *"Restricción que impone…"*; *"Decisión de diseño implicada"* desapareció |
| **E1-47** la obligación AAIP | ✅ | Resuelta **como corresponde**: `[[PENDIENTE: definir con el equipo la aplicabilidad de esta inscripción al contexto experimental y documentar el recaudo adoptado en §17.1 y §17.4]]`. No la inventó: la marcó |
| **E1-33 / E1-34** Anexo A | ✅ | Licencias corregidas (*"API cerrada; Apache-2.0 aplica al SDK, no a los pesos"*) y la matriz pasó de **12 a 20 filas**, ahora **con Grounding DINO Swin-T/Swin-L y MM-Grounding-DINO** |
| **E1-35 / D-E1-9** tablas huérfanas | ✅ | Tabla A.3 (servidores) eliminada; A.2 reescrita en términos de límites frente a la alerta |
| **E1-40** letras de cita falsas | ✅ | `Jeong` y `X. Wang 2020` desaparecieron con las subsecciones duplicadas; `Shi et al., 2016` quedó sin letra |
| **R1 / R2 / R3** residuales de §15 | ✅ | Regularización ahora en prosa · rótulo de la ficha en negrita · **las cuatro altas de referencias están** (Kumar, Lee 2023, OASIS, Ultralytics) y Luxonis con su letra |
| Referencias | ✅ | 83 entradas · **cero huérfanas** · cero citas sin entrada |
| No-anacronismo | ✅ | Cero identificadores de plataforma, cero resultados propios, cero andamiaje |

**Extensión:** §16 pasó de 30.749 a **11.563** palabras y el Anexo A creció de 771 a **3.945**
(la inversión de PODA-17). §15 quedó en 10.399. Total de la Etapa 1: **26.685**.

---

## 1. Lo que falta

### E1-52 · 🔴 · Cinco encabezados perdieron su estilo de título

Son **contiguos**, lo que delata que se pegó texto plano sobre esa región:

| Sección | Título |
|---|---|
| §16.5.3 | Separación de Planos y Flujo Productor-Consumidor |
| §16.5.4 | Computación en el Borde y Filtrado Cercano al Origen |
| §16.5.5 | Brecha de Evaluación Integrada |
| **§16.6** | **Marco Ético-Legal para el Análisis Automatizado de Video en Entornos Laborales** |
| §16.6.1 | Encuadre ético-legal y carácter asistivo |

**El texto está y es correcto** — el problema es que esos párrafos son prosa común con
aspecto de título. Consecuencias: **no aparecen en el índice automático**, no entran en la
numeración de campos de Word, y §16.6 —una sección de primer nivel— queda visualmente colgada
dentro de §16.5.

**Arreglo:** aplicarles el estilo de encabezado correcto (`Heading 3` a §16.5.3/.4/.5 y
§16.6.1; `Heading 2` a §16.6), del mismo nivel que sus hermanas. No hay que tocar una palabra
del contenido.

### E1-53 · 🟡 · Hueco de numeración en §16.7

Quedó **§16.7.1 · §16.7.2 · §16.7.6**: la subsección sobreviviente conservó su número viejo
tras eliminarse las tres del medio. Se ve en el índice. **Renumerar a §16.7.3**, y verificar
que las remisiones a las preguntas rectoras sigan resolviendo (§17.1 las invoca por número).

### Y una decisión del equipo, no del redactor

**D-E1-11** sigue abierta y ahora está correctamente marcada en el texto: la aplicabilidad de
la inscripción ante la AAIP al contexto experimental, y qué recaudo se documenta en
§17.1/§17.4. El marcador `[[PENDIENTE]]` viaja hasta que el equipo lo resuelva.

---

## 2. Flujo de trabajo: por qué no hay que usar Drive

Los dos defectos que quedan **no son errores de redacción: son daño de transporte**. Aparecieron
al conectar el Project a una unidad de Drive y editar el documento allí. Ninguno se ve leyendo
el texto, y ambos son invisibles para quien revisa contenido.

**El punto de fondo: ir a Drive era innecesario.** El paquete de la etapa que está cargado en
el Project **ya contiene el texto vigente completo** — la extracción `90d`. El documento nunca
hizo falta como fuente; conectarlo solo agregó una copia peor.

### Cómo se trabaja de ahora en más

1. **Todo dentro del Project.** Knowledge = `00-contexto-base.md` + `01-etapa-N-activa.md`.
   Sin conectores de Drive, sin editar en la nube. El texto vigente de la sección está en el
   paquete.
2. **La entrega es un `.docx` por sección**, armado sobre una **copia** del DOCX base de
   formato, nunca sobrescribiéndolo.
3. **Cada título con su estilo de encabezado real.** Nunca negrita imitando un título. Si se
   elimina una subsección, **renumerar sus hermanas**.
4. **Con cambios controlados activados** — o, en su defecto, con el bloque de trazabilidad por
   unidad. Las tres entregas anteriores llegaron sin ellos y auditar qué se movió costó
   reconstruir el diff cada vez.
5. **Sin markdown crudo** (`###`, `|---|`) y **sin identificadores internos** (`AJ-`, `R-`,
   `PODA-`, `E1-`, líneas `SHA-256`, cabeceras `> Seleccion:`). Los `P-E1-xx` de las preguntas
   rectoras **sí** son parte del informe.
6. **Los marcadores `[[…]]` viajan.** No se completan con estimaciones ni se borran.
7. **Delta de referencias explícito**: altas en APA 7 con DOI/URL, y bajas de lo que dejó de
   citarse.

Estas siete reglas quedaron escritas **dentro del propio kit** (sección *"Cómo se trabaja y
cómo se entrega"* del contexto base), así que viajan con el knowledge y no dependen de que
alguien las recuerde.

### Verificación mecánica, del lado del equipo

Se agregó `herramientas/verificar_entregable.py`. Sobre cualquier entrega:

```bash
python3 herramientas/verificar_entregable.py "<entrega>.docx" --seccion 15 --seccion 16 --seccion 19
```

**Falla** (y hay que corregir) con: títulos numerados sin estilo de encabezado · huecos y
desórdenes de numeración · fugas de andamiaje interno · markdown pegado sin convertir · citas
sin entrada en referencias.
**Informa** (para revisar): referencias que el cuerpo ya no cita · la misma autoría citada con
años distintos · inventario de marcadores · si faltan los cambios controlados.

Sobre esta entrega reporta exactamente los dos defectos de arriba, y nada más. Los dos habrían
aparecido en un segundo en vez de requerir una lectura completa.

---

## 3. ✎ Resuelto el 2026-08-27 — **no hizo falta ChatGPT**

E1-52 y E1-53 eran dos arreglos mecánicos sobre un documento **cuyo contenido ya estaba
correcto**. Devolvérselo a ChatGPT habría significado regenerar 26.685 palabras para cambiar
cinco estilos de párrafo: mucho riesgo de regresión de contenido, y una verificación completa
más, a cambio de nada. Se resolvieron de forma determinista sobre el `.docx`.

**Documento final: `Etapa 1 — final 2026-08-27.docx`** (la entrega original no se sobrescribió).

| Qué se hizo | Cómo |
|---|---|
| §16.5.3, §16.5.4, §16.5.5, §16.6.1 → `Heading3` | Se les trasplantó el `w:pPr` y el `w:rPr` de **§16.5.2**, una hermana sana del mismo nivel |
| §16.6 → `Heading2` | Donante: **§16.5**, hermana sana del mismo nivel |
| §16.7.6 → **§16.7.3** | Reemplazo del número en el texto del título |

El mapeo no tuvo margen de decisión: **37 hermanas de nivel 3 usan `Heading3` y 12 de nivel 2
usan `Heading2`**. Los marcadores de posición del donante se eliminaron (llevan identificador
único) y cada párrafo conservó el suyo. Solo cambió `word/document.xml` (+797 bytes); el resto
del paquete quedó byte a byte.

**Prueba de no-regresión:** extraído el documento reparado y comparado con el anterior, la
**única diferencia de texto en las 26.685 palabras es la renumeración intencional**. Los
encabezados markdown pasaron de 90 a 95 — los cinco restaurados—, que es lo que explica el
+5 en el conteo de palabras.

**Verificación:** `verificar_entregable.py` pasa de 6 problemas duros a **OK — ningún problema
duro** (código de salida 0). El paquete abre correctamente (zip íntegro, XML válido).

### E1-54 y E1-55 · verificación exhaustiva de contenido y formato

Se pasó el documento por una revisión completa —no solo el verificador— y aparecieron **dos
incumplimientos de la regla de la casa** (*"Tablas y figuras: número y título arriba, notas y
fuente debajo, mencionadas en el texto"*). Ambos corregidos:

- **E1-54** — la **Tabla 5** era la única de las 13 sin frase que la anunciara en prosa: la
  introducía solo el título de su subsección. Se agregó, con el formato del párrafo que
  anuncia la Tabla 10: *"La Tabla 5 organiza las brechas identificadas en las subsecciones
  precedentes con su descripción técnica y su implicación específica para el proyecto."*
- **E1-55** — la **Tabla 9** era la única sin Nota ni Fuente. **Es un defecto heredado del
  informe v1.1**, no introducido en esta entrega. Se agregó, clonando el formato de la Nota de
  la Tabla 10 (su vecina en §16): *"Nota. Cada dominio se corresponde con una sección de este
  capítulo; la columna «Contribución al proyecto» indica qué aporta al desarrollo posterior, no
  un resultado alcanzado. Fuente: elaboración propia."*

**Lo que la revisión confirmó como correcto:**

| Dimensión | Resultado |
|---|---|
| Estilos de encabezado | **94 títulos, todos con `Heading<nivel>` exacto** — cero desviaciones |
| Defecto inverso | Ningún párrafo de prosa lleva estilo de encabezado |
| Numeración de secciones | Sin huecos ni desórdenes en ningún nivel |
| Remisiones internas | **Todas resuelven, y apuntan al lugar semánticamente correcto** — incluida la de zero-shot, que se actualizó a §16.3.5 al insertarse la sección nueva |
| Tablas | 13, estructuralmente sanas (columnas uniformes), numeración contigua 2–12 + A.1/A.2 |
| Tablas: nota, fuente y mención | **Las 13 completas** tras E1-54/E1-55 |
| Ecuación (1) | Centrada, introducida en prosa y con sus cuatro términos explicados |
| Referencias | 83 entradas · cero huérfanas · cero citas sin entrada |
| Andamiaje / anacronismo | Cero identificadores internos, cero resultados propios, cero markdown crudo |
| Marcadores | 1 `[[PENDIENTE]]` — el de la AAIP, que **debe viajar** |

**Un hallazgo que NO se corrigió, a propósito.** El rótulo de las notas aparece con cinco
variantes tipográficas (`**Nota.**`, `*Nota.*`, `Nota.`, y una malformada `**Nota***.*`). **No
es un problema de la Etapa 1: es de todo el informe** — §17.3 tiene seis variantes, §17.5 usa
`*Nota.*` y §17.1 usa `Nota.` sin formato. Unificarlo solo en este capítulo lo dejaría
inconsistente con el resto. **Corresponde al pase de integración final**, sobre el documento
maestro completo.

### E1-56 · precisión sobre YOLOE-11 (2026-08-27, revisión final a pedido)

Al revisar cómo quedó nombrado YOLOE-26 (E1-02), apareció una imprecisión factual en la
oración que lo introduce (§15.2.1.2.2): *"La familia fue extendida **posteriormente en
implementaciones de Ultralytics sobre YOLO11 y YOLO26**"*. **Verificado contra el repositorio
oficial del paper (THU-MIG/yoloe): las variantes YOLOE-11-S/M/L son del trabajo original**, no
de una extensión posterior — solo YOLOE-26 lo es. Corregido a: *"…variantes YOLOE-v8 evaluadas
en el trabajo original, que también publica variantes construidas sobre YOLO11 (YOLOE-11) con
resultados equivalentes (Wang et al., 2025). Las variantes sobre YOLO26 (YOLOE-26) son una
extensión posterior de Ultralytics, sin evaluación en el trabajo original; por lo tanto, los
resultados publicados para YOLOE-v8 no deben utilizarse como si fueran una medición de
YOLOE-26 (Ultralytics, 2026)."* Único cambio (diff verificado); `Wang et al., 2025` ya estaba
en el listado. De paso se confirmó que las cifras de la Tabla 3 para YOLOE-v8-S/L (305,8 FPS ·
27,9 AP · 102,5 FPS · 35,9 AP) coinciden con la tabla oficial.

### Lo que queda, y no es redacción

1. **D-E1-11 — decisión del equipo, y así queda.** La aplicabilidad de la inscripción ante la
   AAIP al contexto experimental. **Se deja como pendiente en el documento**, marcada con
   `[[PENDIENTE: …]]`, hasta que el equipo la resuelva y se documente el recaudo en §17.1/§17.4.
2. **Dependencia hacia la Etapa 2** *(anotada, se corrige después — no bloquea)*. §17.1
   (`96b`, línea 589) remite a "la sección **16.7.6**", que tras la renumeración es §16.7.3.
3. **Abrir el `.docx` en Word una vez** y actualizar el índice (F9) para confirmar que las
   seis entradas aparecen donde corresponde. Es una comprobación visual, no un arreglo.

**Lo que NO hay que hacer:** volver a redactar nada · tocar el contenido de §15, §16 o el
Anexo A · reaplicar ningún pase anterior · devolver el documento a ChatGPT.

---

## 4. Fuentes

Entrega verificada: `desarrollando/Etapa 1 — copia ajustada E1 2026-08-27 (2).docx`,
extraída con `herramientas/extraer_informe.py` y contrastada por diff contra la entrega
previa. Verificación mecánica: `herramientas/verificar_entregable.py` (26 tests). Pases
anteriores: `correcciones-etapa-1.md`, `-pase-2.md`, `-pase-3.md`.

---

## Fuente: `docs/informe/entregable/desarrollando/archivado/correcciones-etapa-1-pase-3.md`

> SHA-256 del bloque: `fff5c0a3d73948fba931b67ebad07bb6622eef02d4c0015f0742ef49c0ba663c`  
> Seleccion: pase 3 (2026-08-27): **YA APLICADO Y VERIFICADO** (constancia en la seccion 0 del pase 4) - NO volver a aplicarlo. Fue el relevamiento que AJ-1.16 declaraba pendiente: cubrio la seccion 16 y el Anexo A, que nunca habian recibido pase. Sus comentarios E1-24 a E1-51 y sus decisiones D-E1-9 a D-E1-12 siguen rigiendo como criterio de lectura -en particular la inversion de la poda 17 y las enmiendas a las podas 06, 07 y 11-. **D-E1-11 sigue ABIERTA y es del equipo**: la aplicabilidad de la inscripcion ante la AAIP, hoy marcada en el texto con un [[PENDIENTE]] que debe viajar.

# Correcciones a la Etapa 1 — pase 3: §16 Marco Teórico, Anexo A y cierre de §15

- **Fecha:** 2026-08-27 · **Para:** el redactor de la Etapa 1.
- **Qué cubre:** las **dos piezas de la Etapa 1 que nunca recibieron un pase** — §16 Marco
  Teórico (30.749 palabras) y el Anexo A — más los tres residuales que dejó el pase 2 sobre
  §15. Con esto la Etapa 1 queda completa.
- **Por qué existe:** `AJ-1.16` declaraba un hueco: *"el §16 no fue relevado contra el estado
  actual del proyecto… es un hueco de relevamiento, **no** una afirmación de que el §16 esté
  bien"*. Este documento **es** ese relevamiento.
- **IDs:** continúan la serie — comentarios **E1-24…E1-4x**, decisiones **D-E1-9…**.
- **Estado de §15:** pases 1 y 2 **aplicados y verificados**; no se vuelve a tocar salvo R1–R3.

---

## 0. Veredicto

**§16 está en peor estado que §15 antes del pase 1**, por tres razones que no se pisan:

1. **Nunca se le aplicó ningún pase.** Las erratas de cita que `AJ-1.10` corrigió en §15
   siguen enteras acá, y ahora **producen contradicciones entre secciones del mismo
   informe**: la misma obra citada con dos años distintos en §15 y en §16.
2. **Una afirmación de §16 quedó refutada por el §15 corregido.** §16.3.5.1 sostiene que la
   retención open-vocabulary depende de la familia arquitectónica; §15.2.3 y §15.2.4, tras
   el pase, dicen exactamente lo contrario y con fundamento. Si se entregan así, el informe
   se contradice a sí mismo en una página.
3. **Falta el fundamento conceptual del mecanismo central de la tesis.** La palabra
   *negación* aparece **cero veces** en §16 — y §16.3 es, por guardrail, "el corazón
   conceptual". Eso es una **adición**, no una poda, y manda sobre las podas.

Además, §16 repite el patrón que el pase 2 corrigió en §15, pero **peor**: tiene **cuatro**
secciones "Criterios orientadores para la selección de X" (3.628 palabras) que enuncian, en
voz normativa, requisitos que son decisiones del proyecto — **§16.4.4 y §16.7.4 no tienen ni
una sola cita**, y varias exigen capacidades que el trabajo nunca ejerció (prompts visuales,
segmentación, multi-protocolo, multi-flujo, jornadas de 8–10 h). Y hay un dato que ordena
todo el capítulo: **§16.7 y §16.8 suman 4.790 palabras con cero referencias** — la única masa
de texto de ese tamaño sin literatura en todo el marco teórico, y justo donde más prescribe.

**Sobre la extensión:** §16 tiene 30.749 palabras y las podas autorizadas (PODA-05…11)
proyectan **≈−16.500**. Igual que en §15, la reducción está justificada **en el agregado**:
§16.5 solo (12.926 palabras, el 42 % del capítulo) desarrolla códecs acelerados, frameworks,
nube y niebla que la plataforma no usa, y contiene **1.425 palabras que son la misma
subsección escrita dos veces**. Pero hay dos advertencias que cambian cómo se aplica:

- **PODA-06 y PODA-07 no son recortes, son reescrituras:** lo que mandan conservar **hoy no
  está escrito o está mal**. La ecuación que define la latencia extremo a extremo **está
  vacía** en el archivo; la descomposición de §16.5 tiene **seis** componentes y la que usa el
  resto del informe tiene **cuatro** (y le falta `t_preprocess`); y el patrón
  productor/consumidor que PODA-07 manda conservar **no aparece en el capítulo**.
- **§16 no debe salir solo más corto: debe salir con el mecanismo de la tesis fundado**, que
  hoy no está (E1-25).

---

## 1. Residuales de §15 (cierre del pase 2)

Rápidos y acotados; ninguno supera las 150 palabras.

**R1 · 🟡 · Tabla 4, fila OWL-ViT/OWLv2 "Fine-tuning end-to-end con regularización".** Es la
única fila que la prosa ya no sostiene: la palabra "regularización" aparece **solo dentro de
la tabla**. Agregar una oración en el párrafo de dual-encoders de §15.2.4 —*"el ajuste sobre
datasets cerrados exige estrategias de regularización para no colapsar el espacio de
embeddings compartido del que depende la capacidad abierta (Minderer et al., 2022)"*— o
eliminar la fila.

**R2 · 🟡 · Formato de la ficha de Florence-2.** Su rótulo ("Arquitectura, entrenamiento y
disponibilidad.") va **sin negrita**, mientras las demás fichas usan rótulos en negrita.
Unificar también la puntuación del rótulo, que quedó inconsistente entre fichas
(`**Arquitectura base.**` vs `**Arquitectura base**.`).

**R3 · 🟠 · Delta de referencias.** Verificado contra el listado vigente:
- **Dar de alta** (no existen): *Kumar et al. (2022)* · *Lee et al. (2023)* · *OASIS (2019)*
  · *Ultralytics (2026)*.
- **Corregir**: la cita dice *Luxonis (s. f.)* y la entrada del listado es
  **`Luxonis. (s. f.-b). OAK-D Pro PoE`** — lleva letra.
- **Ya existen y están bien** (no tocar): AILab-CVC 2024 · Google 2022/2023 · Kirkpatrick 2017
  · Li, L. H. 2021 (GLIP) · Microsoft 2024 · THU-MIG 2025 · IDEA-Research 2024a/2024c ·
  Adžemović · Rasaee · Ucar.
- **Bajas** que arrastra la poda de §15: OV-DETR, OV-DINO, OmDet-Turbo, Detic, DetCLIP,
  Grounded SAM / SAM 2, OVTrack, Roboflow/RF-DETR, Janus, Kurento, MediaMTX, OvenMediaEngine,
  SRS, y las obras de RTMP/HLS/DASH/CMAF/WebRTC/SRT/RIST **que ya no se citan en prosa**.
  ⚠ **Cuidado:** lo que sobreviva citado **solo en la nota de la Tabla 8 se conserva**
  (decisión D-E1-8). Verificar fuente por fuente antes de dar de baja.

---

## 2. §16 — hallazgos transversales

Estos cuatro valen para todo el capítulo y conviene resolverlos en una sola pasada.

### E1-24 · 🔴 · §16 contradice al §15 corregido sobre retención y fine-tuning

**Dice hoy** (§16.3.5.1, criterio "Independencia de entrenamiento específico por dominio"):

> *"la evidencia analizada en la sección 15.2.4.5 muestra que la capacidad de una
> arquitectura para preservar su generalización open-vocabulary durante el fine-tuning varía
> sustancialmente entre familias de modelos. Los detectores con fusión visión-lenguaje
> profunda y no removible exhiben mayor resiliencia frente al ajuste de dominio, mientras que
> aquellos con módulos de texto reparametrizables o desacoplables tienden a converger hacia un
> comportamiento closed-set."*

**Por qué está mal.** El §15, ya corregido, sostiene lo contrario y lo argumenta: *"La
evidencia revisada **no permite atribuir** la retención open-vocabulary a una familia
arquitectónica por sí sola, porque las comparaciones utilizan datos, módulos entrenables y
protocolos diferentes. La retención depende de la receta aplicada… **no debe inferirse de la
profundidad o removibilidad de la fusión**"* (§15.2.3), y §15.2.4 cierra: *"no corresponde
afirmar que una familia tolere mejor el ajuste completo"*. Son dos afirmaciones incompatibles
en el mismo informe, separadas por unas páginas.

**Encima, el puntero está roto:** cita **"sección 15.2.4.5"**, que tras la reorganización de
§15 ya no existe (el fine-tuning es ahora **§15.2.4**).

**Qué hacer.** Reescribir el criterio alineado al §15: la retención se describe **por receta
concreta** (qué parámetros se actualizan o congelan, si se conserva supervisión lingüística
amplia, si se evalúan categorías no vistas) y **no se infiere de la arquitectura**. Corregir
el puntero a §15.2.4. Es la corrección más urgente del capítulo.

### E1-25 · 🔴 · Falta el fundamento conceptual del mecanismo central de la tesis

**Qué pasa hoy.** En las 30.749 palabras de §16, la palabra **"negación" aparece cero veces**;
**"bolsa de palabras" / *bag-of-words*, cero**. §16.3 —que el guardrail protege como *"el
corazón conceptual de la tesis"*— explica qué es OVD, cómo alinea visión y lenguaje y que los
prompts son sensibles a la redacción, pero **nunca explica por qué una condición formulada
como negación puede fallar**, ni qué alternativa conceptual existe.

**Por qué importa.** Ese es el mecanismo que la tesis ejerce: el sistema **no le pide al
modelo la infracción como frase**, sino evidencia positiva, e **infiere la ausencia por
relación espacial**. El §15 ya trae la evidencia empírica de la dificultad (Chen y Zou 2025:
IoU < 20 % con restricciones de atributo; Choi y Greer 2024: `head` 0,1024 frente a `hardhat`
0,6493 sobre las mismas imágenes) — **pero la evidencia no es el fundamento**. Hoy el lector
llega a §17 sin haber leído nunca por qué el sistema razona la ausencia en vez de pedirla.

**Qué hacer.** Un bloque nuevo en §16.3 (≈400–500 palabras, entre §16.3.3 y §16.3.4), con dos
piezas y **sin un solo dato propio**:

1. **Por qué la composición y la negación son difíciles para un encoder contrastivo.** El
   entrenamiento contrastivo optimiza la correspondencia global imagen–texto y no obliga a
   representar la estructura de la frase; en consecuencia estos modelos se comportan, en
   buena medida, como *bolsa de palabras*: la representación de una frase con modificador
   queda dominada por sus sustantivos. Literatura verificada y directamente aplicable:
   - **Yuksekgonul, M., Bianchi, F., Kalluri, P., Jurafsky, D., & Zou, J.** — *"When and why
     vision-language models behave like bags-of-words, and what to do about it?"*
     (arXiv:2210.01936). Introduce el benchmark **ARO** (Attribution, Relation, Order,
     >50.000 casos) y muestra el desempeño pobre de VLMs de referencia en relación y
     atribución. **Es la cita canónica del mecanismo.**
   - **Thrush, T., Jiang, R., Bartolo, M., Singh, A., Williams, A., Kiela, D., & Ross, C.** —
     *"Winoground: Probing Vision and Language Models for Visio-Linguistic Compositionality"*
     (arXiv:2204.03162): con captions de **palabras idénticas y distinto orden**, los modelos
     evaluados no superan el azar. Aísla la composición del contenido léxico.
2. **La consecuencia de diseño, enunciada como alternativa conceptual y no como decisión
   nuestra:** si el modelo resuelve mejor "qué hay" que "qué falta", una condición definida
   por ausencia admite dos formulaciones —pedir la ausencia al modelo, o pedir la evidencia
   positiva y derivar la ausencia mediante razonamiento espacial sobre las detecciones—, y
   **cuál rinde mejor es una pregunta empírica que el estado del arte no responde**. Eso
   enlaza limpio con §15.2.5.1 (contextualización semántica limitada) y deja la brecha
   abierta para que §17.5 la conteste.

**Redacción, sin violar el no-anacronismo:** describir el problema y las dos formulaciones
posibles. **No** escribir que el proyecto eligió una, ni nombrar `E-IND`/`E-DIR`, ni dar
umbrales, regiones anatómicas ni resultados.

### E1-26 · 🟠 · Las cuatro secciones "Criterios orientadores": el mismo fallo que el pase 2 corrigió en §15

§16 tiene **cuatro** secciones de criterios de selección: **§16.3.5** (modelos OVD, 1.135 w),
**§16.4.4** (métodos MOT, 340 w), **§16.5.5** (protocolos y stack, 1.343 w) y **§16.7.4**
(selección tecnológica, 810 w) — **3.628 palabras**. Enuncian en voz normativa ("el modelo
**debe** sostener…", "**resultan preferibles** modelos que…") requisitos que son las
decisiones del proyecto. Es exactamente lo que en §15.3.2.1 hubo que reescribir (E1-16).

Tres agravantes concretos, verificados:

- **§16.4.4.1 no tiene ni una cita.** Sus cinco criterios ("Compatibilidad con detección
  open-vocabulary", "Latencia compatible con tiempo real", "Desacoplamiento arquitectónico",
  "Independencia de entrenamiento específico", "Robustez operativa suficiente") son las
  propiedades exactas del tracker que se construyó, presentadas como conclusión de la
  literatura. El último llega a justificar la elección de antemano: *"aun cuando no alcance el
  máximo rendimiento en benchmarks académicos"*.
- **Dos criterios exigen capacidades que el trabajo nunca ejerció.** §16.3.5.1 declara que
  *"el modelo **debe** permitir… ejemplos visuales de referencia (visual prompts)"* — la
  plataforma nunca usó prompts visuales; y §16.3.5.2 propone *"capacidad de extensión hacia
  segmentación"* — no hay segmentación en la tesis. Por la **regla de honestidad** (lo
  pre-registrado y no ejercido no se borra en silencio), o se baja de requisito a dimensión
  descrita en la literatura, o se declara con su causa. Lo que **no** puede quedar es un
  "debe" que el trabajo incumple sin decirlo.
- **§16.3.5.2 propone una arquitectura que el proyecto probó y descartó:** *"Configuraciones
  híbridas —donde diferentes modelos se ejecutan según la complejidad de la consulta o el
  contexto operativo— emergen como alternativas viables"*. Es especulación no fundada, y
  además anticipa un camino cuyo resultado se relata en §17.5.

**Qué hacer con las cuatro.** El §16 debe dejar **dimensiones de comparación con cita**, no
requisitos. Fórmula: *"la literatura permite comparar los métodos a lo largo de N ejes —
X (fuente), Y (fuente), Z (fuente)—; qué peso recibe cada eje es una decisión del diseño, que
se toma y se justifica en el protocolo experimental"*. Con eso las cuatro secciones se
comprimen fuerte y dejan de invadir a §17.1. PODA-09 y PODA-05 ya autorizan comprimir dos de
ellas; E1-26 extiende el criterio a las cuatro.

### E1-27 · 🟠 · Erratas de cita: `AJ-1.10` nunca se aplicó a §16, y ahora contradice a §15

`AJ-1.10` unificó las citas inconsistentes **solo en §15**. En §16 siguen, y el contraste
entre secciones es verificable por cualquiera:

| Obra | §16 cita | §15 (corregido) cita | Problema |
|---|---|---|---|
| Grounding DINO (Liu et al.) | **2023** | **2024** | misma obra, dos años, en el mismo informe |
| Florence-2 (Xiao et al.) | **2023** | **2024** | ídem |
| MS COCO (Lin et al.) | **2014 y 2015** (ambos, en §16) | **2014** | ídem, y ya inconsistente dentro de §16 |
| CoOp / prompt learning (Zhou et al.) | **2021, 2022a, 2022b** *(y 2019)* | **2022b** | la **misma obra citada como 2021 y como 2022a en párrafos contiguos** (§16.3.3) |
| Ren et al. | 2024, 2024a, 2024b, 2024c | "Ren, Jiang / Ren, Chen / Ren, Liu, et al." | dos convenciones distintas para desambiguar |
| Minderer et al. | 2022 | 2022 y 2023 | falta OWLv2 en §16 |

**Qué hacer.** Unificar §16 **contra §15**, que es el que ya pasó verificación, y adoptar en
todo el capítulo la convención de desambiguación por apellido de segundo autor que §15 usa
para Ren.

### E1-28 · 🟠 · Tres referencias cruzadas colgadas o hacia adelante

- **§16.4.2.3:** *"En sistemas que incorporan apariencia **(el análisis del modelado de
  apariencia)**, la asociación se beneficia…"* — paréntesis que perdió su destino. **Es
  literalmente el mismo defecto que se corrigió en §15.3.1.2**: viene del documento fuente y
  hay que buscarlo en todo el capítulo, no solo acá. Reemplazar por "(§16.4.2.4)".
- **§16.4.3:** *"…mantiene la separabilidad entre el **plano de medios** —ingesta y
  procesamiento de video— y el **plano de control** —gestión de eventos y alertas—, de acuerdo
  con **la arquitectura modular definida**"*. Doble problema: nombra **nuestra** arquitectura
  con **nuestros** nombres, y remite a una sección posterior. Es anacronismo. Reescribir en
  términos genéricos ("separación entre la etapa de percepción y la de razonamiento sobre
  eventos") y quitar el reenvío.
- **§16.2.2.2:** *"…asegurando coherencia con el marco de evaluación **definido para el
  proyecto**"* — reenvío hacia adelante. Basta con "que se define en el protocolo
  experimental".

---

## 3. §16 — hallazgos por bloque

### 3.1 §16.1 Organización (474 w) y §16.2 Condiciones de riesgo (3.008 w) — **el ancla, se conserva**

Guardrail 1 protege §16.2: es lo que ancla las condiciones a la normativa; sin esto, las
condiciones que el sistema detecta son arbitrarias. **Está bien construido y se conserva**: la
cadena Ley 19.587 → Decreto 351/79 → Decreto 911/96 → Resoluciones SRT → ISO 45001 es sólida,
y la **Tabla 10** (obligación normativa → evidencia visual → condición detectable en video) es
el artefacto que justifica todo el dominio de aplicación. Su nota ya aclara que no constituye
selección de prompts. Correcto que liste ocho categorías aunque el trabajo ejerza dos: es el
universo normativo, no el alcance.

**E1-29 · 🟠 · §16.2.3 describe nuestra arquitectura de eventos.** El último párrafo dice:

> *"esta integración puede modelarse mediante una arquitectura orientada a eventos (EDA), en
> la cual cada evidencia visual detectada se materializa como un evento estructurado —por
> ejemplo, `persona_sin_casco_detectada`— que es publicado por el módulo de análisis de video
> y consumido por componentes especializados en evaluación de patrones, generación de alertas
> y registro de trazabilidad… la detección visual constituye la fuente primaria de eventos
> dentro del **plano de control** del sistema"*.

Eso no es marco teórico: es el diseño del sistema (§17.3), con su vocabulario. Además es
justo lo que PODA-10 autoriza a recortar de §16.2.3 (~300 palabras). **Eliminar el párrafo**;
el concepto que sí vale —que la prevención es un proceso continuo y que la alerta es insumo
de supervisión humana, no decisión autónoma— ya está dicho en los párrafos anteriores y en
§16.2.1.7.

### 3.2 §16.3 Percepción visión-lenguaje (2.542 w) — **el corazón, hay que reforzarlo**

Se conserva por guardrail. §16.3.1 (closed-set → open-vocabulary), §16.3.2 (alineación
contrastiva, CLIP) y §16.3.4 (zero-shot y long-tail) están bien y son el fundamento correcto.
Sobre esta sección operan **E1-25** (la adición del mecanismo de negación/composicionalidad —
lo más importante del pase) y **E1-24/E1-26** (§16.3.5).

**E1-30 · 🟠 · §16.3.3 dice tres veces lo mismo, con tres citas distintas de la misma obra.**
La subsección (589 w) tiene **tres párrafos consecutivos** que repiten el mismo contenido —
sensibilidad del prompt → *prompt learning* con tokens aprendibles → la optimización
automática supera al diseño manual (Du et al., 2022)— citando a Zhou como **2022a**, como
**2021** y de nuevo como **2021**. Consolidar en **un** párrafo (~250 w) con una sola cita
correcta. Es, además, el punto donde §16 duplica a §15.2.5.3, que ya trata la sensibilidad al
prompt: dejar en §16 el **fundamento** (por qué el texto es una especificación y por qué su
forma importa) y en §15 la **brecha** documentada.

### 3.3 §16.4 Persistencia temporal y MOT (2.684 w) — PODA-05

**Se conserva** lo que funda el trabajo: **§16.4.1** (la limitación del fotograma: por qué una
detección que no persiste no puede sostener una alerta — es el fundamento de la histéresis
temporal) y **§16.4.3** (integración OVD+MOT, que funda la identidad por sujeto). Ambos están
bien escritos y son de los mejores pasajes del capítulo.

**E1-31 · 🟡 · §16.4.2 (1.551 w) comprimir a ~700, como manda PODA-05.** Es un tratado de
fundamentos MOT: formulación del problema, filtro de Kalman y estimación de estado, LAP y
algoritmo húngaro con su complejidad O(n³), *gating*, distancia de Mahalanobis, ReID y
DeepSORT, oclusiones. La plataforma usa asociación **geométrica sin filtro de movimiento ni
apariencia**, y las métricas MOT están excluidas del alcance. Conservar: la formulación del
problema (predicción · similitud · asignación), IoU como métrica de similitud, y el
desacoplamiento *tracking-by-detection* —que es lo que permite integrar un detector OVD sin
reentrenar nada—. Comprimir fuerte Kalman, Mahalanobis, ReID/DeepSORT y complejidad
algorítmica: son correctos pero no sostienen ninguna decisión ni ningún resultado.
**Errata de paso:** §16.4.2.3 y §16.4.2.4 **explican IoU dos veces**, casi con las mismas
palabras.

**E1-32 · 🟠 · §16.4.4 (340 w): PODA-05 la elimina; aplicar con el criterio de E1-26.** No
hubo selección de método de catálogo, y sus cinco criterios no tienen citas. Si se prefiere
conservar algo, que sea **una** oración de dimensiones con cita dentro de §16.4.3.

### 3.4 Anexo A — la pieza que D-E1-7 rescató

**E1-33 · 🔴 · La Tabla A.1 conserva la errata de licencias que §15 ya corrigió.** Lista
**DINO-X**, **G-DINO 1.5 Pro** y **G-DINO 1.5 Edge** como **"Apache-2.0"**. El §15, corregido,
dice: *"se ofrecen mediante API y no publican pesos abiertos; la licencia Apache-2.0
corresponde al SDK de acceso y no al modelo"*. Es `AJ-1.09` sin aplicar, y hoy **contradice
frontalmente al cuerpo**. Corregir a "API cerrada — Apache-2.0 aplica al SDK, no a los pesos".

**E1-34 · 🔴 · Grounding DINO no está en la Tabla A.1.** La matriz tiene 12 filas —DINO-X,
G-DINO 1.5 Pro, G-DINO 1.5 Edge, LLMDet, OV-DINO, DetCLIPv3, OWLv2 L/14, YOLOE-v8-L,
YOLO-World-L, OmDet-Turbo, YOLOE-v8-S, Florence-2-L— y **falta el Grounding DINO original**
(y MM-Grounding-DINO). Es el modelo sobre el que se construyó el trabajo. Con **D-E1-7** la
Tabla A.1 pasó a ser el lugar que conserva la amplitud del catálogo que salió del cuerpo, así
que el hueco es doblemente grave. **Agregar las filas de Grounding DINO (Swin-T y Swin-L, con
sus regímenes) y MM-Grounding-DINO**, y las de los modelos cuyas fichas se podaron del cuerpo
y no estén ya (GLIP, OV-DETR, Detic, APE, T-Rex2).

**E1-35 · 🟠 · Las Tablas A.2 y A.3 quedaron huérfanas.** Tras la poda, el §15 **solo** cita
la Tabla A.1: la **A.2** (limitaciones de MOTA/IDF1/HOTA) y la **A.3** (comparativa de
servidores de medios) ya no las llama nadie. Decidir explícitamente → **D-E1-9**. Recomendación:
**conservar la A.2** citándola desde §15.3.3 (sostiene la exclusión de las métricas MOT con un
argumento que hoy está comprimido en tres líneas) y **eliminar la A.3**, porque los servidores
de medios ya no sostienen ninguna decisión ni aparecen en el cuerpo.

---

## 4. Podas de §16 — qué se conserva, y con qué criterio

Las podas están autorizadas desde `ajustes/07` §4. El criterio es **aporte, no cuota**: una
subsección se queda si sostiene un concepto que el resto del informe usa. Y rige el
**guardrail 6**: las adiciones mandan sobre las podas — E1-25 (el mecanismo de negación)
**entra** aunque el capítulo esté adelgazando.

| Poda | Sobre | Hoy | Acción | Enmienda de este pase |
|---|---|---:|---|---|
| PODA-05 | §16.4 MOT | 2.684 | conservar 16.4.1 y 16.4.3; comprimir 16.4.2 → ~700; eliminar 16.4.4 | E1-31, E1-32 |
| **PODA-06** | §16.5.2 descomposición | 4.881 | conservar solo lo que define la latencia y sus componentes | ⚠ **es REESCRITURA**: la ecuación está vacía y la descomposición no coincide con la del informe (E1-36, E1-37) |
| **PODA-07** | §16.5.3 arquitecturas | 3.604 | comprimir a ~600 con el patrón productor/consumidor | ⚠ **es REDACCIÓN NUEVA**: ese patrón no está escrito, y hay que **agregar publish/subscribe** o el bus y MQTT quedan sin fundamento (E1-38) |
| PODA-08 | §16.5.4 borde | 2.741 | comprimir a ~700 | salvar **sí o sí** el filtrado cerca del origen y la convención borde/niebla/nube (E1-39 y tabla de §5) |
| PODA-09 | §16.5.5 criterios de stack | 1.437 | párrafo puente | aplicar con el criterio de E1-26; **no reciclar** el criterio multi-protocolo |
| PODA-10 | §16.6 ético-legal | 4.266 | conservar 16.6.2 y 16.6.6; podar 16.6.4/16.6.5; comprimir 16.6.7 | rescatar **una frase** de cada podada; E1-46, E1-47 |
| **PODA-11** | §16.7 + §16.8 | 4.790 | fusionar en un cierre de ~1.000; rescatar el mapa de brechas | ⚠ **el mapa está 5/6 duplicado con §15** (E1-51): se rescata **una** fila, no la tabla |
| — | §16.5.1 latencia como restricción | 503 | **NO TOCAR** (guardrail 3) | — |
| — | §16.2, §16.3 | 5.550 | **NO TOCAR** (guardrail 1) | salvo E1-29, E1-30 y **la adición E1-25** |

**Resultado esperado:** de 30.749 a **≈14.000 palabras**, con el mecanismo central de la tesis
fundado por primera vez. La cifra es consecuencia, no meta.

---

## 5. §16.5 — Operación en tiempo real (12.926 w, el 42 % del capítulo)

Aquí operan PODA-06 a PODA-09. Pero **dos de las cuatro no son recortes: son reescrituras**,
porque lo que mandan conservar hoy no está escrito o está mal.

### E1-36 · 🔴 · La ecuación que define la latencia extremo a extremo **está vacía**

En §16.5.2 (líneas 373–375) la ecuación **(1)** —la que descompone la latencia en sus
componentes— quedó como una tabla de dos celdas vacías: `|  | (1) |`. Se perdió al exportar
el documento. Lo mismo pasó con los símbolos en la nota de la Tabla 11 y, fuera de §16, en
§17.1.7 (*"no corresponde reportar ."*, *"G2A abarca , , y ."*).

Es **exactamente el contenido que PODA-06 manda conservar**, y hoy no existe. Reponer la
ecuación **antes** de podar nada; si no, la poda deja la sección sin su único aporte.

### E1-37 · 🔴 · La descomposición de §16.5 no coincide con la que usa el resto del informe

§16.5.2 descompone el pipeline en **seis** componentes (captura · codificación · transporte ·
decodificación · **renderizado** · inferencia). El §17.1.7 formaliza la latencia
extremo a extremo con **cuatro**: `t_capture`, `t_transport`, **`t_preprocess`**,
`t_inference`. Consecuencias:

- **`t_preprocess`** —redimensionado, normalización, copia de memoria hacia el acelerador—
  **no existe en §16.5.2**, y es el término que usan §17.1.7, §17.5 y las figuras.
- **Codificación, decodificación y renderizado no son componentes** de la latencia que el
  informe define y mide.
- La **Tabla 11** se titula *"Componentes de latencia del pipeline glass-to-algorithm"* pero
  incluye una fila *"Renderizado / Jitter Buffer ~10–120 ms"*, que por la propia definición de
  §16.5.1 pertenece al recorrido **hasta el vidrio**, no hasta el algoritmo. **La tabla mide
  una cosa y se llama por otra.**

**Por eso PODA-06 es una reescritura.** El bloque de ~1.400 palabras que se conserva debe
**establecer la descomposición de cuatro componentes** con la notación de §17.1.7, no podar
la de seis. Rehacer la Tabla 11 a cuatro filas o sustituirla por prosa.

### E1-38 · 🟠 · Lo que PODA-07 manda conservar tampoco está escrito

PODA-07 dice comprimir §16.5.3 "a ~600: el patrón productor/consumidor como fundamento
conceptual". **Ese patrón no aparece en §16.5**: la pareja "productor/consumidor" no está
escrita en ninguna parte del capítulo, y *backpressure* aparece dos veces, una en un párrafo
de meta-texto y otra dentro de una advertencia sobre un decodificador de hardware. Hay que
**redactar** esas ~200 palabras, no comprimirlas.

**Y hay un riesgo peor.** La plataforma acopla sus planos con un **bus publish/subscribe** y
distribuye alertas por **MQTT**. En todo el marco teórico, MQTT se menciona **una sola vez**,
de refilón, dentro del párrafo sobre un framework de terceros — **que es justamente uno de los
párrafos que PODA-07 elimina**. Aplicada tal cual, la poda dejaría al informe sin ningún
fundamento conceptual para el bus de eventos ni para la mensajería de alertas, que son dos
piezas centrales del sistema. El bloque comprimido debe incluir **publish/subscribe
desacoplado** como patrón, con cita (Cugola y Margara 2012 ya está citado en §16.5.3.1 y
sirve para ambos).

### E1-39 · 🟠 · Prescripciones de diseño y promesas incumplidas dentro de §16.5

- **§16.5.5 completa (1.437 w) es un pliego de requisitos del prototipo, no marco teórico.**
  Ejemplo: *"resulta conveniente que el framework… permita modificar parámetros de códec…
  **priorizando la flexibilidad de configuración sobre la portabilidad multiplataforma, que
  excede el alcance del prototipo**"* — una decisión de alcance del proyecto, sin cita,
  presentada como conclusión del análisis. La sección incluso **se autodesmiente**: abre
  diciendo *"La formulación de criterios no anticipa decisiones de diseño"* y a continuación
  las anticipa. → cae con PODA-09 (ver E1-26).
- **Promete evaluación multi-protocolo que nunca ocurrió** (§16.5.5.1.2: *"El soporte
  multi-protocolo… habilitar roles diferenciados según el tramo del pipeline"*). La ingesta
  construida es RTSP + SDK, y nada más. No reciclar ese criterio en el párrafo puente.
- **Promete un plano de control en la nube** (§16.5.3.1): *"escalabilidad distribuida, que
  habilita la ejecución del plano de medios en un nodo edge y el de control **en la nube**"*,
  y en la misma oración *"permite evaluar alternativas como GStreamer versus FFmpeg"*. Ni lo
  uno ni lo otro existió: un solo host, sin nube, y esa comparación nunca se hizo. §16.5.3.1
  **se conserva** (es el fundamento de la separación de planos, y está bien citado), pero
  **con esas dos cláusulas borradas**.
- **Tres subsecciones abren diciendo que analizan alternativas "para E-OVRT-VDP"** (códecs
  acelerados, mecanismos de comunicación entre procesos): ninguna de esas tecnologías entró al
  sistema. Caen con PODA-07.
- **La Tabla 11 receta protocolos que no se usaron**: *"SRT con latency budget ajustado"*,
  *"inferencia por GPU (TensorRT)"*. Al rehacerla, dejar solo estrategias documentadas sin
  nombrar stacks que el informe no vuelve a mencionar.

### E1-40 · 🟠 · Duplicación masiva, con prueba forense de que el material se escribió dos veces

- **§16.5.3.5 y §16.5.4.4 son la misma subsección escrita dos veces** (532 + 893 = 1.425 w):
  ambas sobre plataformas de hardware para el borde, ambas con Jetson, ambas argumentando que
  la métrica TOPS no es comparable, ambas remitiendo al mismo benchmark.
  **La prueba:** el mismo trabajo aparece como `Jeong et al., 2022a` en una y
  `Jeong et al., 2022b` en la otra, **con una sola entrada en el listado de referencias**.
  Idéntico patrón con `Shi et al., 2016a/2016b` y `X. Wang et al., 2020a/2020b`.
  **Las letras de desambiguación son falsas** y hay que corregirlas donde el texto sobreviva.
- **El umbral perceptual de interacción humana aparece cuatro veces**, siempre con las mismas
  dos citas: en §16.5.1, dos veces en §16.5.2.7 y otra en §16.5.5.1.1 (más una quinta vez en
  §15.4). Sobrevive **solo** el de §16.5.1, que es el que el guardrail protege.
- **Codificación y decodificación se explican dos veces** (I/P/B-frames, GOP, buffer de
  imágenes decodificadas), y el propio texto lo admite: *"Como se describió al tratar las
  configuraciones de codificación…"*. Ambas caen con PODA-06.

### E1-41 · 🟡 · Meta-texto y un anuncio que describe una estructura inexistente

Cuatro pasajes anuncian lo que viene en vez de decir algo. Uno es defectuoso además de
inútil: *"Las subsecciones siguientes caracterizan en detalle la latencia de inferencia…"* —
y **no hay subsecciones**: lo que sigue son párrafos. Otro cierra con una promesa sin destino:
*"Este concepto será ampliado en secciones posteriores"*, sin puntero ni sección
identificable. Eliminar los cuatro.

### E1-42 · 🟡 · Un encabezado con nivel equivocado

§16.5.2.5 ("Latencia de Renderizado") está un nivel más abajo que sus hermanas 16.5.2.1–.4,
así que hoy renderiza como hija de §16.5.2.4. Si se regenera la numeración automáticamente,
"16.5.2.5" pasa a ser "16.5.2.4.3". Como PODA-06 elimina esa subsección, el punto se resuelve
solo — pero **conviene verificar que no haya más encabezados con nivel mal puesto** antes de
regenerar la numeración del capítulo.

> ✅ **Un riesgo que ya está resuelto.** El §15 anterior remitía a "las secciones 16.5.2.3 y
> 16.5.2.5", que PODA-06 elimina. **El §15 vigente ya no contiene ningún puntero hacia §16**
> (desaparecieron al podar §15.4). Verificado: cero coincidencias. No hay nada que arreglar
> de ese lado; el trabajo pendiente es solo el inverso, los punteros de §16 hacia §15
> (E1-24, E1-28).

### Qué se conserva de §16.5, en concreto

| Bloque | Se conserva | Se va |
|---|---|---|
| **§16.5.1** (503 w) | **Íntegra** (guardrail 3): la latencia como restricción, la distinción entre el recorrido hasta el vidrio y hasta el algoritmo, el umbral perceptual y el principio de **presupuestar** el buffer en vez de eliminarlo | — |
| **§16.5.2** (4.881 → ~1.400) | Un bloque único que **define la latencia y sus cuatro componentes** con la notación de §17.1.7 + la ecuación repuesta (E1-36) · captura acotada por el período de cuadro · el transporte como el componente de mayor variabilidad externa, y que **lo que compromete el tiempo real es su cola, no su media** (funda el reporte por percentiles) · **párrafo nuevo de `t_preprocess`** · dos rangos de referencia de inferencia | codificación · decodificación · **renderizado** (no es parte de la latencia que se mide) · el catálogo de técnicas de optimización · §16.5.2.7 (duplica §16.5.1) |
| **§16.5.3** (3.604 → ~600) | **§16.5.3.1 separación de planos** casi íntegra, menos las dos cláusulas de E1-39 · **~200 w nuevos**: productor/consumidor con cola acotada y contrapresión, y **publish/suscripción** como patrón de notificación desacoplada (E1-38) | intro (meta-texto normativo) · códecs acelerados por hardware · comunicación entre procesos · frameworks de terceros · plataformas de borde (duplica §16.5.4.4) |
| **§16.5.4** (2.741 → ~700) | Las tres tensiones que motivan el borde · **la convención terminológica borde/niebla/nube y los tres patrones de despliegue** (permite entender, en §17.3, que se ejerció el prefiltrado en el dispositivo y se excluyó la inferencia en el borde) · **el punto de que filtrar cerca del origen reduce el consumo aguas abajo** — *es el fundamento conceptual del prefiltrado y lo único que PODA-08 debe salvar sí o sí* · opcional: que la latencia en el borde se juzga por percentiles | taxonomías de nube y niebla · geo-distribución y ciudades inteligentes · catálogo de aceleradores y métricas de hardware |
| **§16.5.5** (1.437 → ~120) | **Nada de los siete criterios.** Un párrafo que enuncie **la brecha**: la literatura evalúa por separado protocolos, stacks de códec y modelos, y no ofrece un marco integrado para presupuestar latencia extremo a extremo en un pipeline con inferencia open-vocabulary. Como esa brecha **ya está en §15.4.3.1**, el puente debe remitir sin repetirla | los siete criterios y las consideraciones complementarias |

**Ahorro de §16.5: ≈9.800 palabras** (de 12.926 a ~3.100).

---

## 6. §16.6 ético-legal, §16.7 convergencias y §16.8 (9.056 w)

### E1-43 · 🔴 · §16.7 y §16.8 suman **4.790 palabras con cero citas**

Es la única masa de texto de ese tamaño en todo el marco teórico que no se apoya en
literatura — y es justamente donde el capítulo prescribe con más fuerza. El **62 % de §16.7**
es literalmente recapitulación de §16.2–§16.6 o anticipo de §17: 1.393 palabras de resumen,
455 que describen la arquitectura del sistema y 838 de proyección metodológica. PODA-11 tenía
razón en llamarlo "meta-texto puro".

### E1-44 · 🔴 · §16.7.4: los "siete criterios orientadores" son el diseño del proyecto, sin una sola fuente

La subsección abre diciendo *"El análisis del estado del arte no selecciona tecnologías:
establece los criterios que deben orientar esa selección"* —es decir, se declara derivada de
la literatura— y a continuación desarrolla 810 palabras y una tabla **sin ninguna referencia**.
Cuatro de los siete criterios son el sistema construido, escrito en futuro:

- *"El flujo de video… y la lógica de negocio… **deben operar en planos arquitectónicamente
  separados**"*, evaluable por *"posibilidad de sustituir el modelo sin modificar el sistema
  de alertas"*. Eso **es** la arquitectura de dos planos, no un criterio de la literatura.
- *"Latencia de alerta medida en percentiles (P50, P95, P99)…"* — es el protocolo de medición
  propio.
- **El criterio 3 repite la afirmación que E1-24 refuta**: *"la preservación de esta capacidad
  **varía significativamente entre familias arquitectónicas**"*, otra vez sin fuente. Es la
  **segunda** aparición de la afirmación incompatible con el §15 corregido: al aplicar E1-24
  hay que corregir **las dos**.

Agravante: §16.8.2 presenta esos siete criterios como un **logro** del capítulo, así que el
problema es estructural. **Acción:** §16.7.4 completa se va (PODA-11). Lo que se quiera
conservar, va a §17.1 como decisión metodológica propia y declarada — que es donde
corresponde—, no a §16 como derivación del estado del arte.

### E1-45 · 🔴 · §16.7.5 describe la arquitectura implementada dentro del marco teórico

455 palabras, cero citas: *"El plano de medios… se estructura en cuatro etapas secuenciales:
ingesta… normalización… inferencia… tracking"*; *"Todos los eventos… se registran de manera
inmutable en el repositorio de event sourcing"*; *"La ruta crítica de latencia del sistema pasa
íntegramente por este plano"*. **El propio texto admite el origen**: *"coherente con la
arquitectura de dos planos planteada en el anteproyecto del proyecto"* — o sea, viene del
anteproyecto, no del estado del arte. Es anacronismo puro e invade §17.3. **Eliminar íntegra.**
Si algo se salva, una línea diciendo que la separación entre plano de medios y plano de
control es un patrón documentado — y eso ya vive, **con citas**, en §16.5.3.1.

### E1-46 · 🔴 · La Tabla 12 llama "decisiones de diseño" a controles que nunca se implementaron

§16.6.6 es **núcleo vivo** y la única tabla densamente citada del tramo (21 citas), pero su
columna se titula **"Decisión de diseño implicada"** y lista, entre otros: *"control de acceso
basado en roles con principio de mínimo privilegio; cifrado de flujos de video en tránsito;
registros de auditoría de acceso"*, *"señalización visible en obra; mecanismo de contacto con
el responsable del tratamiento"*, *"política explícita de retención y borrado seguro"*. En un
prototipo académico de un solo host, **leídas como decisiones tomadas son falsas**.

**El arreglo es de una palabra y salva la subsección entera:** renombrar la columna a
**"Restricción que impone al diseño"** y pasar a voz de exigencia las tres o cuatro celdas
que hoy están en presente descriptivo. Con eso dejan de ser falsas y quedan correctas.

### E1-47 · 🟠 · Una obligación legal abierta que el informe nunca cierra

§16.6.7 afirma: *"Cualquier validación experimental del prototipo que involucre personas en el
campo visual de las cámaras requiere evaluar la obligación de inscripción ante la AAIP y la
elaboración previa del manual de tratamiento… deberán definirse en la etapa 2."* **El proyecto
sí grabó personas.** Hoy queda una obligación planteada, remitida a una etapa, y nunca cerrada
— exactamente el hilo del que un jurado tira.

Además, esa fila **no es una brecha**: la inscripción es un requisito explícito y vigente,
resuelto en la norma; está en la tabla equivocada. **Acción:** sacarla de la tabla de brechas
e integrarla como una frase en §16.6.2.2, donde el requisito ya se enuncia; y **cerrar el
punto en §17.1/§17.4** (por qué el contexto controlado y académico no dispara la inscripción,
qué recaudo se tomó). → **D-E1-11**.

### E1-48 · 🟠 · Se promete razonamiento relacional multi-entidad; el trabajo entregó atributo por entidad

§16.7.3 y su párrafo de desarrollo concluyen que *"la arquitectura **debe** incluir una capa de
razonamiento contextual sobre las trayectorias… capaz de evaluar condiciones que involucren
**múltiples entidades y su relación espacial**"*, con ejemplos como *"persona en zona
restringida sin señalero visible"*. Las condiciones que el sistema evalúa son de **entidad
única más atributo**, con persistencia temporal. **No hay razonamiento relacional
multi-entidad**, y §17.5 no puede satisfacer esa expectativa.

Conservar la **brecha conceptual** (la detección por fotograma no modela relaciones — eso sí
es literatura y §15.2.5.1 ya lo dice con citas) y **borrar la prescripción arquitectónica**, o
declarar explícitamente que queda fuera del alcance. Mismo criterio para la enumeración
"arnés, chaleco reflectivo y señalero" cuando solo se ejercieron casco y chaleco.

### E1-49 · 🟠 · Dos preguntas rectoras quedaron huérfanas

§16.7.6 plantea ocho preguntas rectoras con código propio. Verificado sobre todo el
entregable: seis se retoman en §17.1, pero **dos no se retoman en ninguna parte** — la de
condiciones experimentales y la de recaudos ético-legales (que incluye *"consentimiento
informado… protocolo de anonimización"*, y es justo la que conecta con E1-47). O se eliminan
de la lista, o §17.1 las responde. No pueden quedar planteadas y sin retomar.

⚠ **Dependencia a vigilar:** §17.1 cita **"la sección 16.7.6" por su número** y usa los
códigos de esas preguntas nueve veces. Si §16.7.6 desaparece como subsección numerada al
fusionar, hay que actualizar esa remisión y las nueve invocaciones.

### E1-50 · 🟡 · Duplicación en §16.6 y §16.8

- **La introducción de §16.6 y §16.6.1 son el mismo texto dos veces** (249 + 243 w): ambas
  abren con la asimetría entre el trabajador y el sistema y con que *"esa asimetría no se
  resuelve declarando que el propósito es preventivo"*. Hay incluso un tercer párrafo que
  repite el encuadre. Las 492 palabras se comprimen a ~150.
- **§16.8 (429 w) no aporta nada que §16.7 no diga**, salvo tres líneas: las **tres
  limitaciones del propio marco teórico** de §16.8.2 (evolución acelerada del campo; datos de
  rendimiento obtenidos en condiciones no operativas; dinamismo del marco regulatorio). Eso
  se rescata; el resto —incluida la autoevaluación *"permitieron alcanzar los objetivos
  propuestos"*— se va. *(Al citarlas: no confundir con las limitaciones numeradas del
  proyecto, que son otra serie.)*
- **Tautologías** para eliminar de paso: *"deben utilizarse en la instancia de diseño
  arquitectónico para estructurar las decisiones de diseño arquitectónico"* · *"El diseño de
  esta capa es una decisión arquitectónica de la instancia de diseño arquitectónico"*. Y
  §16.7.2 es un título con 29 palabras de cuerpo, cuyo nombre es indistinguible del de
  §16.7.1.

### E1-51 · 🟠 · Corrección a PODA-11: el "mapa de brechas" que mandaba rescatar está 5/6 duplicado

PODA-11 designa el mapa de brechas transversales de §16.7.3 como *"lo único que se rescata"*.
**Verificado: cinco de sus seis filas ya están en §15**, algunas por triplicado:

| Fila de §16.7.3 | Ya está en |
|---|---|
| Ausencia de benchmarks para construcción | §15.2.5.4 · §15.3.4 · §15.4.3.1 |
| Métricas académicas no alineadas con el valor operativo | §15.2.5.5 · §15.3.4 · §15.4.3.4 — **triplicada** |
| Integración del pipeline no caracterizada | §15.4.3.1 · §15.4.3.2 |
| Condiciones composicionales | §15.2.5.1 |
| Sensibilidad al diseño de prompts | §15.2.5.3, casi textual |
| **Marco normativo-ético como restricción arquitectónica** | **única genuinamente nueva** |

**Lo transversal de verdad es una sola fila.** El cierre debe conservarla en prosa y
reemplazar las otras cinco por **una frase de remisión** a las tablas de §15 — no re-tabularlas.

### Qué se conserva de §16.6–§16.8, en concreto

| Bloque | Se conserva | Se va |
|---|---|---|
| **§16.6** (4.266 → ~2.850) | **§16.6.2 completa** (imagen como dato personal, etapas del tratamiento, roles, régimen argentino, identificabilidad indirecta, los tres ejes de la disposición aplicable): es lo que sostiene la minimización de evidencia visual efectivamente implementada · **§16.6.3** (seguridad de la información y retención) · **§16.6.6 con la Tabla 12 intacta**, aplicando E1-46 · **§16.6.7 comprimida a ~400 w en prosa**: las cuatro brechas legítimas con sus citas, sin la columna de implicaciones · **un solo párrafo** de encuadre (E1-50) | §16.6.4 referentes comparados — **rescatando una frase**: la distinción entre captación de video e identificación biométrica, que es lo que fundamenta excluir el reconocimiento facial · §16.6.5 gobernanza — **rescatando una frase** que sostenga las dos filas de la Tabla 12 que dependen de esas fuentes · el párrafo duplicado del encuadre · la fila de la AAIP (E1-47) |
| **§16.7 + §16.8** (4.790 → ~950) | Un cierre único, en cuatro bloques: **(1)** interdependencia de los dominios, ~200 w, sin "event sourcing" · **(2)** la única brecha genuinamente transversal, ~200 w (E1-51) · **(3)** las preguntas rectoras **como lista**, ~350 w, resolviendo las dos huérfanas (E1-49) · **(4)** cierre con la viabilidad teórica y **las tres limitaciones del marco** de §16.8.2, ~200 w | §16.7.2 y sus tres subsecciones (recapitulación) · la Tabla 14 como tabla · **§16.7.4 completa** (E1-44) · **§16.7.5 completa** (E1-45) · introducción de §16.8, la autoevaluación y la transición |

**Ahorro de §16.6–§16.8: ≈5.240 palabras** (algo más que las ~4.800 previstas, porque el mapa
de brechas resulta redundante y §16.8.3 también cae).

---

## 7. Acciones previas obligatorias

Estas cuatro van **antes** de aplicar cualquier poda; si se podan primero, se pierde material
que hay que reponer igual.

1. **Reponer la ecuación (1)** de §16.5.2, hoy vacía, con la notación de cuatro términos que
   usa §17.1.7 — y revisar los símbolos perdidos en §17.1.7 (*"G2A abarca , , y ."*). Es el
   contenido que PODA-06 debe conservar (E1-36).
2. **Fijar la descomposición en cuatro componentes** (E1-37), incluida la definición nueva de
   `t_preprocess`, antes de recortar la de seis.
3. **Redactar** el patrón productor/consumidor y publish/subscribe (E1-38) **antes** de
   eliminar §16.5.3.2–.3.5, o el bus de eventos y MQTT se quedan sin fundamento.
4. **Corregir las citas con letra de desambiguación falsa** —`Jeong 2022a/b`, `Shi 2016a/b`,
   `X. Wang 2020a/b`, una sola entrada cada una— dondequiera que el texto sobreviva (E1-40).

---

## 8. Orden de trabajo sugerido

1. **§15, residuales:** R1, R2, R3 (§1). Cierra la sección.
2. **§16, contradicciones y erratas duras** (una pasada, sin decisión previa): **E1-24** (las
   **dos** apariciones: §16.3.5.1 y §16.7.4) · E1-27 citas · E1-28 referencias colgadas ·
   E1-36 ecuación · E1-40 letras falsas · E1-50 tautologías.
3. **§16, la adición:** **E1-25** — el mecanismo de negación y composicionalidad en §16.3. Es
   lo más valioso del pase; hacerlo antes de podar, para que no se pierda en el ajetreo.
4. **§16, alineación:** E1-26 (las cuatro secciones de criterios) · E1-29 · E1-30 · E1-37 ·
   E1-38 · E1-39 · E1-44 · E1-45 · E1-46 · E1-47 · E1-48 · E1-49.
5. **§16, podas** con las enmiendas de §4: PODA-05…11, en ese orden.
6. **Anexo A:** E1-33 licencias · E1-34 filas faltantes · E1-35 tablas huérfanas.
7. **Delta de referencias** del capítulo entero (altas de E1-25, bajas de las podas).

**Lo que NO hay que hacer:** volver a tocar §15 más allá de R1–R3 · reaplicar E1-01…E1-23 ·
podar §16.2, §16.3 o §16.5.1 · dejar §16 más corto pero sin el fundamento de E1-25.

---

## 9. Decisiones del equipo

| ID | Decisión | Recomendación | ✔ |
|---|---|---|---|
| D-E1-9 | Tablas A.2 y A.3 quedaron sin quien las cite (E1-35). | Conservar **A.2** y citarla desde §15.3.3; **eliminar A.3**. | [ ] |
| D-E1-10 | La adición E1-25 suma ~450 palabras a un capítulo que se está podando. | Aceptar: es el fundamento del mecanismo central y rige el guardrail 6. | [ ] |
| D-E1-11 | La obligación de inscripción ante la AAIP (E1-47) queda planteada en §16 y nunca cerrada, y el proyecto sí grabó personas. | Sacarla de la tabla de brechas **y cerrarla en §17.1/§17.4** con el recaudo efectivamente tomado. **Requiere una definición del equipo, no del redactor.** | [ ] |
| D-E1-12 | Dos preguntas rectoras quedaron huérfanas (E1-49): condiciones experimentales y recaudos ético-legales. | Eliminarlas de la lista, salvo que §17.1 vaya a responderlas. Ligada a D-E1-11. | [ ] |

---

## 10. Fuentes de esta revisión

Texto de §16: `entregable/96d`. Anexo A: `entregable/96e` §19.1. Tablero original:
`ajustes/01` (`AJ-1.16`). Podas y guardrails: `ajustes/07` §4 y §9. Teoría vigente del
trabajo, contra la que `AJ-1.16` pide contrastar: `sintesis/fundamentos-teoricos.md`.
Citas nuevas verificadas contra arXiv (lista de autores exacta): **arXiv:2210.01936** (ARO) y
**arXiv:2204.03162** (Winoground). Estado de §15: `correcciones-etapa-1.md` y
`correcciones-etapa-1-pase-2.md`.

---

## Fuente: `docs/informe/entregable/90d-etapa1-texto-extraido.md`

> SHA-256 del bloque: `1f7281bdd1666c319042c8dabb54e1d9e288fd0b1250534d039a595eb0782855`  
> Seleccion: TEXTO BASE FINAL DE LA ETAPA 1 - **el DESARROLLO: seccion 15 y seccion 16**, extraido de 'E-OVRT-VDP_Secciones_15_y_16_Estado_del_Arte_y_Marco_Teorico_v1.0.docx', con los **cinco pases YA APLICADOS Y VERIFICADOS**, los 16 AJ-1.xx resueltos, las podas 01-11 aplicadas, formato y terminologia unificados (el verificador da OK). **SUPERA al 96c y al 96d** del informe v1.1, que por eso ya no forman parte de este paquete. **El entregable de la etapa es SOLO el desarrollo**: el Anexo A y el listado de referencias salieron del documento por decision del usuario -los arma el equipo- y quedaron en `90e`. **La etapa esta CERRADA: no queda trabajo de contenido, formato ni terminologia** sobre este texto; no cambiar una palabra de fondo. Lo unico abierto de fondo es D-E1-11, que decide el equipo y viaja como [[PENDIENTE]].

# 90d — Texto extraído del documento de trabajo: §15 Estado del Arte y §16 Marco Teórico (v1.0)

> **Extracción derivada (2026-08-28)** del `.docx`
> `informe/entregable/desarrollando/E-OVRT-VDP_Secciones_15_y_16_Estado_del_Arte_y_Marco_Teorico_v1.0.docx`, **solo para búsqueda y cita**
> (mismo estatuto que el doc 90): al editar, se edita el `.docx`/Google Docs, nunca
> este archivo. Tablas y figuras pueden haber perdido formato; las figuras no se
> extraen y las ecuaciones no se convierten — quedan `⟦FIGURA: no extraída — ver el .docx⟧` y
> `⟦ECUACIÓN: no extraída — ver el .docx⟧` donde estaban. Regenerado con
> `herramientas/extraer_informe.py` (regla D-C del manual de aplicación).

---

## 15. Estado del arte

El estado del arte reúne los antecedentes técnicos y metodológicos necesarios para contextualizar el desarrollo de una plataforma experimental de detección open-vocabulary en video en tiempo real. Su propósito es revisar los enfoques, modelos y arquitecturas que permiten comprender el alcance actual de la detección visual guiada por lenguaje natural, así como sus limitaciones cuando se la traslada a escenarios dinámicos, con restricciones temporales y requerimientos de seguridad laboral.

### 15.1. Alcance del estado del arte y propósito de la fundamentación teórica

El análisis se organiza en torno a los dominios que condicionan la viabilidad del sistema: la detección open-vocabulary como alternativa frente a los enfoques de vocabulario cerrado, los modelos visión-lenguaje y sus principales familias arquitectónicas, el seguimiento multiobjeto como mecanismo de persistencia temporal, y las tecnologías de transmisión y procesamiento de vídeo necesarias para operar con baja latencia. De manera complementaria, se consideran las brechas que aparecen al aplicar estas tecnologías al dominio de la construcción civil, especialmente en relación con la detección de condiciones de riesgo, la estabilidad temporal de las predicciones, la sensibilidad a los prompts, la disponibilidad de datos y la evaluación de alertas en tiempo real.

Esta revisión no tiene por finalidad elegir de forma aislada un modelo, protocolo o herramienta, sino establecer un marco crítico para distinguir qué capacidades se encuentran suficientemente maduras, qué aspectos requieren validación experimental y qué limitaciones deben ser consideradas durante el diseño e implementación del prototipo. A partir de esta base se derivan criterios para la selección tecnológica, la definición del alcance experimental y la construcción posterior del protocolo de evaluación.

### 15.2. Detección open-vocabulary: modelos, paradigmas y brechas del estado del arte

#### 15.2.1. Paradigmas arquitectónicos y modelos representativos

El estado del arte en OVD no constituye una solución homogénea, sino que se organiza en familias arquitectónicas con compromisos claramente diferenciados entre expresividad semántica, complejidad computacional y eficiencia temporal. A partir de un relevamiento exhaustivo realizado durante la investigación bibliográfica, se identificaron cuatro paradigmas dominantes, de los cuales se presentan a continuación los aspectos y modelos representativos más relevantes para el contexto de sistemas de video en tiempo real.

El primer paradigma extiende arquitecturas end-to-end basadas en Transformers —derivadas de DETR y DINO (Carion et al., 2020; H. Zhang et al., 2022)— e incorpora el lenguaje dentro de la predicción mediante fusión multimodal. Grounding DINO (Liu et al., 2024) organiza esa integración en un Feature Enhancer que alinea representaciones visuales y textuales, una selección de consultas guiada por lenguaje y un decoder de modalidad cruzada que refina cajas y las vincula con fragmentos del prompt. La fusión profunda favorece expresiones referenciales y consultas con atributos, aunque incrementa el costo computacional y la complejidad de despliegue.

El segundo paradigma adapta detectores one-stage de la familia YOLO para puntuar regiones frente a representaciones textuales. YOLO-World (Cheng et al., 2024) incorpora interacción visión-lenguaje en su neck y permite reutilizar un vocabulario precomputado; YOLOE (A. Wang et al., 2025) amplía la reparametrización para admitir prompts textuales, visuales y un modo sin prompt. Esta familia prioriza eficiencia y compatibilidad con pipelines de baja latencia, a cambio de una expresividad más acotada ante consultas relacionales o altamente composicionales.

Una tercera familia deriva la detección del paradigma dual-encoder de CLIP: imagen y texto se proyectan en un espacio compartido y la clase de cada región se obtiene por compatibilidad semántica, no mediante logits fijos. OWL-ViT y OWLv2 (Minderer et al., 2022, 2023) representan este enfoque y muestran cómo el autoentrenamiento puede escalar la supervisión sin alterar el mecanismo de consulta. Su principal ventaja es la modularidad: el vocabulario cambia con los prompts; su costo depende del número de consultas y puede mitigarse mediante el cacheo de embeddings cuando el vocabulario permanece estable.

El cuarto paradigma agrupa modelos guiados por prompts generalistas, generativos e híbridos. Florence-2 (Xiao et al., 2024) formula las tareas como traducción secuencia-a-secuencia y genera representaciones textuales de cajas, etiquetas u otras salidas estructuradas; APE, LLMDet y T-Rex2 adoptan prompting generalista sin compartir necesariamente una decodificación autoregresiva (Shen et al., 2023; Fu et al., 2025; Jiang et al., 2024). Esta flexibilidad amplía la variedad de tareas y modalidades de consulta, pero en los modelos generativos introduce latencia variable y menor paralelismo que la predicción directa.

A continuación, se revisan modelos representativos de cada paradigma, enfocando el análisis en: (i) decisiones arquitectónicas, (ii) mecanismo de fusión/compatibilidad visión–lenguaje, (iii) régimen de entrenamiento y tipo de supervisión, y (iv) resultados en benchmarks estándar (COCO, LVIS), junto con consideraciones prácticas de inferencia relevantes para aplicaciones en vídeo.

**Convención de lectura.** Salvo indicación expresa, las cifras de COCO y LVIS corresponden a AP promediado entre umbrales de intersección sobre unión (IoU) de 0,50 a 0,95; en LVIS se conserva el protocolo Fixed AP cuando así lo informa la fuente. Los resultados de literatura supervisada de EPP se presentan como mAP@0,5 o AP@0,5 en una serie separada y no deben compararse numéricamente con COCO/LVIS AP.

##### 15.2.1.1. Bloque A — Detectores end-to-end tipo DETR/DINO con fusión visión–lenguaje en el decoder

###### 15.2.1.1.1. Grounding DINO

**Arquitectura base.** Grounding DINO extiende la formulación de detección como phrase grounding introducida por GLIP (L. H. Li et al., 2021) y la integra en la línea DETR/DINO. El modelo emplea una arquitectura dual-encoder/single-decoder: un backbone visual —frecuentemente Swin Transformer— extrae características multiescala y un backbone textual BERT codifica el prompt; un Transformer produce predicciones condicionadas por ambas modalidades (Liu et al., 2024).

**Mecanismo visión–lenguaje.** La contribución central es una fusión multimodal profunda basada en atención cruzada en distintas etapas. Grounding DINO divide la fusión en tres componentes: Feature Enhancer (interacciones imagen–texto para alinear semántica y regiones), Language-guided Query Selection (inicializa consultas del decoder condicionadas por texto), y Cross-modality Decoder (agrega atención cruzada con texto para refinar cajas y asociar predicciones a fragmentos del prompt). Esto hace que el modelo sea especialmente efectivo con expresiones referenciales o frases con atributos (Liu et al., 2024).

**Resultados reportados.** En configuración zero-shot, Grounding DINO con backbone Swin-L reporta 52,5 AP en COCO y 26,1 mean AP en ODinW; la variante Swin-T reporta aproximadamente 48,4 AP en COCO bajo el mismo protocolo (Liu et al., 2024).

La variante GroundingDINO-B con backbone Swin-B dispone de pesos públicos, pero su checkpoint declara COCO entre los datos de entrenamiento, junto con O365, GoldG, Cap4M, OpenImages, ODinW-35 y RefCOCO. Por ello, el 56,7 AP publicado en COCO no constituye una cifra zero-shot directamente comparable con la variante Swin-T entrenada sin COCO (IDEA-Research, 2024c).

**Evolución Grounding DINO 1.5.** La versión 1.5 Pro, orientada a máxima generalización, entrena con Grounding-20M (más de 20 millones de imágenes) y logra 54,3 AP en COCO y 55,7 AP en LVIS-minival en zero-shot transfer. La versión 1.5 Edge, orientada a despliegue eficiente, reporta 75,2 FPS y 36,2 AP en LVIS-minival con TensorRT, y despliegue en NVIDIA Orin NX con más de 10 FPS (Ren, Jiang, et al., 2024).

**Licencia y disponibilidad.** El repositorio del Grounding DINO original se distribuye bajo licencia Apache-2.0. Las variantes Grounding DINO 1.5 Pro y Grounding DINO 1.5 Edge se ofrecen mediante API y no publican pesos abiertos; la licencia Apache-2.0 corresponde al SDK de acceso y no al modelo (IDEA-Research, 2024c; Ren, Jiang, et al., 2024).

**Implementación MM-Grounding-DINO.** MM-Grounding-DINO proporciona una tubería unificada de grounding y detección sobre la familia Grounding DINO. Sus variantes Tiny reportan entre 50,4 y 50,6 AP@[0,50:0,95] en COCO zero-shot y entre 35,7 y 41,4 AP@[0,50:0,95] en LVIS-minival, según la configuración y el backbone evaluados (X. Zhao et al., 2024).

###### 15.2.1.1.2. DINO-X

**Arquitectura base.** DINO-X es un modelo unificado y object-centric para detección open-world/open-vocabulary, desarrollado como evolución directa de Grounding DINO 1.5, manteniendo un esquema Transformer encoder–decoder orientado a representaciones a nivel objeto. A diferencia de detectores OV que dependen estrictamente de listas de clases, DINO-X soporta múltiples tipos de prompt: texto, prompts visuales y prompts personalizados (Ren, Chen, et al., 2024).

**Mecanismo visión–lenguaje.** La idea distintiva de DINO-X es combinar flexibilidad de entrada con un mecanismo prompt-free mediante un Universal Object Prompt que permite "detectar cualquier cosa" sin definir clases específicas (Ren, Chen, et al., 2024).

**Entrenamiento.** El trabajo construye y utiliza Grounding-100M, un conjunto con más de 100 millones de muestras de grounding de alta calidad para preentrenamiento (Ren, Chen, et al., 2024).

**Resultados reportados.** DINO-X Pro alcanza 56,0 AP en COCO, 59,8 AP en LVIS-minival y 63,3 AP en clases raras de LVIS-minival, estableciendo un nuevo estado del arte en detección abierta (Ren, Chen, et al., 2024).

**Licencia.** DINO-X se ofrece mediante API y no publica pesos abiertos; la licencia Apache-2.0 corresponde al SDK o cliente de acceso y no a los pesos del modelo (IDEA-Research, 2024a; Ren, Chen, et al., 2024).

##### 15.2.1.2. Bloque B — Detectores one-stage tipo YOLO con puntuación región–texto

###### 15.2.1.2.1. YOLO-World

**Arquitectura base.** YOLO-World adapta un detector one-stage de la familia YOLO al escenario open-vocabulary manteniendo predicción densa y diseño orientado a despliegue. Su contribución arquitectónica central es RepVL-PAN (Re-parameterizable Vision-Language Path Aggregation Network), un neck multiescala que incorpora interacción visión–lenguaje sin abandonar la estructura backbone–PAN–head propia de YOLO (Cheng et al., 2024).

**Mecanismo visión–lenguaje.** El modelo puntúa regiones mediante similitud en un espacio compartido región–texto. RepVL-PAN implementa esta interacción con Text-guided CSPLayer para inyectar guía textual en las features visuales e Image Pooling Attention para enriquecer embeddings textuales con contexto visual. En despliegue, YOLO-World opera con vocabulario offline y habilita una reparametrización que permite prescindir del encoder textual durante inferencia (Cheng et al., 2024).

**Resultados reportados.** YOLO-World-L reporta 35,4 AP en LVIS-minival con 52,0 FPS en NVIDIA V100 (sin TensorRT), mostrando un punto de operación competitivo para aplicaciones con restricción de latencia (Cheng et al., 2024).

**Licencia.** El repositorio declara licencia GPL-3.0, con posibilidad de gestionar licencia alternativa para uso comercial (AILab-CVC, 2024).

###### 15.2.1.2.2. YOLOE

**Arquitectura base.** YOLOE, presentado como "Real-Time Seeing Anything", propone un modelo one-stage que unifica detección y segmentación manteniendo el esquema backbone–PAN–heads típico de YOLO. Sus módulos de alineamiento se diseñan para que, tras reparametrización, el grafo de inferencia quede equivalente al de un YOLO cerrado (A. Wang et al., 2025).

**Mecanismo visión–lenguaje.** YOLOE integra tres modalidades: prompts de texto mediante RepRTA (Re-parameterizable Region-Text Alignment), prompts visuales mediante SAVPE (Semantic-Activated Visual Prompt Encoder), y modo prompt-free mediante LRPC (Lazy Region-Prompt Contrast) que reformula la asignación como retrieval evitando dependencia de modelos de lenguaje en inferencia (A. Wang et al., 2025).

**Resultados reportados.** En LVIS-minival zero-shot, YOLOE-v8-S reporta 27,9 AP con 305,8 FPS (NVIDIA T4, TensorRT) y YOLOE-v8-L alcanza 35,9 AP con 102,5 FPS, superando a YOLO-Worldv2-S por +3,5 AP con mayor velocidad (A. Wang et al., 2025).

Las cifras anteriores corresponden a las variantes YOLOE-v8 evaluadas en el trabajo original, que también publica variantes construidas sobre YOLO11 (YOLOE-11) con resultados equivalentes (Wang et al., 2025). Las variantes sobre YOLO26 (YOLOE-26) son una extensión posterior de Ultralytics, sin evaluación en el trabajo original; por lo tanto, los resultados publicados para YOLOE-v8 no deben utilizarse como si fueran una medición de YOLOE-26 (Ultralytics, 2026).

**Licencia.** El repositorio declara licencia AGPL-3.0, lo que introduce requisitos copyleft que pueden condicionar adopción en integraciones propietarias (THU-MIG, 2025).

##### 15.2.1.3. Bloque C — Detectores basados en dual-encoders (CLIP-like) y matching por similitud

###### 15.2.1.3.1. OWL-ViT y OWLv2

**Arquitectura base.** OWL-ViT propone una receta directa para llevar modelos visión–lenguaje a detección open-vocabulary usando un Vision Transformer (ViT) encoder-only con modificaciones mínimas. Se mantienen los tokens espaciales y se agregan cabezales livianos que predicen, por token, una caja y un embedding de compatibilidad. La clasificación abierta se logra reemplazando un clasificador cerrado por embeddings derivados del texto (Minderer et al., 2022).

**Entrenamiento.** OWLv2 escala mediante self-training (OWL-ST): usa un modelo OWL-ViT como annotator para generar pseudo-cajas sobre datos web a gran escala (WebLI). OWLv2 introduce mejoras de eficiencia de entrenamiento: un objectness head para entrenar pérdidas solo sobre un subconjunto de tokens más plausibles como objeto, y token dropping durante entrenamiento (Minderer et al., 2023).

**Resultados reportados.** OWL-ViT L/14 alcanza 34,6 AP y 31,2 AP en clases raras en LVIS. OWLv2 L/14 con OWL-ST reporta 44,6 AP en clases raras zero-shot en LVIS-val, y la variante G/14 alcanza 47,2 AP en clases raras (Minderer et al., 2022, 2023).

**Licencia.** Los pesos se distribuyen bajo Apache-2.0 (Google, 2022; Google, 2023).

##### 15.2.1.4. Bloque D — Modelos guiados por prompts generalistas: generativos e híbridos

Esta familia reúne modelos que amplían el tipo de consulta o la variedad de tareas sin compartir necesariamente un mecanismo generativo en inferencia. Florence-2 constituye el caso propiamente secuencia-a-secuencia: interpreta instrucciones de tarea y genera una representación textual de cajas, etiquetas u otras salidas estructuradas, con la flexibilidad y el costo temporal propios de la decodificación autoregresiva (Xiao et al., 2024). APE, en cambio, utiliza prompting generalista pero produce predicciones estructuradas de forma directa; LLMDet incorpora conocimiento de un LLM durante el entrenamiento y descarta ese componente en inferencia; T-Rex2 combina prompts textuales y visuales mediante una formulación multimodal (Shen et al., 2023; Fu et al., 2025; Jiang et al., 2024). En conjunto, estos trabajos muestran que el prompting generalista constituye una dimensión transversal y no equivale, por sí mismo, a generación autoregresiva.

###### 15.2.1.4.1. Florence-2

**Arquitectura, entrenamiento y disponibilidad.** Florence-2 utiliza un encoder visual DaViT y un Transformer encoder-decoder multimodal bajo una formulación secuencia-a-secuencia: recibe una imagen y una instrucción de tarea, y genera texto o tokens de localización que representan cajas, regiones y otras salidas estructuradas. El modelo se preentrenó sobre FLD-5B, un banco de 126 millones de imágenes con 5,4 mil millones de anotaciones, y la variante large reporta 37,5 mAP en detección zero-shot sobre COCO. Esta unificación evita cabezales específicos por tarea, pero la generación autoregresiva introduce un costo temporal distinto del de los detectores de predicción directa. Los pesos publicados por Microsoft se distribuyen bajo licencia MIT (Xiao et al., 2024; Microsoft, 2024).

#### 15.2.2. Composición de modelos y pipelines de percepción

Los detectores OVD pueden integrarse en pipelines que combinan capacidades complementarias. Grounded SAM ejemplifica esta composición al encadenar detección condicionada por texto con segmentación universal, mientras que OVTrack formaliza una extensión temporal mediante tracking-by-detection en vocabulario abierto (Ren, Liu, et al., 2024; S. Li et al., 2023). El aporte conceptual de estos enfoques no es un modelo aislado, sino la posibilidad de desacoplar etapas con responsabilidades distintas.

La modularidad permite sustituir componentes y ampliar capacidades, pero también acumula latencia, dependencias de integración y fuentes de variabilidad. Para sistemas de video en tiempo real, la evaluación debe considerar el pipeline completo y no sólo la precisión de cada modelo por separado; este criterio enlaza la detección con el seguimiento temporal y con las etapas posteriores de generación de eventos.

#### 15.2.3. Síntesis comparativa y trade-offs para tiempo real

La Tabla 2 sintetiza las características fundamentales de los cuatro paradigmas arquitectónicos analizados, con énfasis en las dimensiones más relevantes para la viabilidad del sistema E-OVRT-VDP en un contexto de vídeo en tiempo real.

**Tabla 2**

*Síntesis comparativa de paradigmas arquitectónicos OVD según dimensiones relevantes para sistemas de video en tiempo real*

| **Paradigma** | **Modelo(s) representativos** | **Mecanismo visión-lenguaje** | **Fortaleza principal** | **Limitación para tiempo real** |
| --- | --- | --- | --- | --- |
| DETR/DINO + fusión profunda | Grounding DINO, MM-Grounding-DINO, DINO-X | Fusión multimodal en decoder mediante atención cruzada visión-lenguaje | Alta precisión semántica; manejo de expresiones referenciales complejas | Costo computacional elevado; requiere optimización explícita para tiempo real |
| One-stage YOLO + puntuación región-texto | YOLO-World, YOLOE | Alineamiento región-texto reparametrizable; reducción progresiva del overhead de fusión mediante reparametrización | Alta velocidad de inferencia; compatible con hardware de borde | Menor expresividad semántica frente a consultas complejas o con atributos compuestos |
| Dual-encoder CLIP-like + matching por similitud | OWL-ViT, OWLv2 | Matching por similitud en espacio de embeddings compartido; reutilización directa de preentrenamiento contrastivo | Modularidad; cambio de vocabulario sin modificar el modelo | latencia variable según tamaño del vocabulario; requiere caching para vocabularios estables; requiere cómputo de embeddings por consulta |
| Prompts generalistas: generativo e híbrido | Florence-2, APE, LLMDet, T-Rex2 | Mecanismos heterogéneos: generación autoregresiva en Florence-2; predicción directa o integración híbrida en APE, LLMDet y T-Rex2 | Flexibilidad multitarea; soporte para prompts complejos y multimodales | Florence-2: latencia de inferencia variable e inestabilidad temporal por decodificación autoregresiva; APE: costo de prompting masivo escalable pero sin garantías de tiempo real estricto |

*Nota.* La columna “Limitación para tiempo real” describe el principal factor restrictivo de cada paradigma en escenarios de monitoreo continuo. Los modelos listados son representativos de cada familia; no constituyen una lista exhaustiva. Las métricas de velocidad son contextuales al hardware y configuración de inferencia reportados en la literatura primaria. Fuente: Elaboración propia basada en las fuentes mencionadas (Cheng et al., 2024; Liu et al., 2024; Minderer et al., 2022, 2023; A. Wang et al., 2025; Xiao et al., 2024).

El régimen de disponibilidad constituye una dimensión independiente del rendimiento. YOLO-World y YOLOE se publican bajo GPL-3.0 y AGPL-3.0, respectivamente, mientras que el Grounding DINO original y OWLv2 utilizan licencias permisivas Apache-2.0; por otra parte, Grounding DINO 1.5 y DINO-X se ofrecen mediante API sin pesos abiertos. Estas diferencias afectan la reproducción independiente, la redistribución de artefactos y la continuidad tecnológica, aun en un prototipo académico. Por ello, la comparación de alternativas debe distinguir entre licencia del código, licencia de los pesos y condiciones del servicio de acceso (AILab-CVC, 2024; Google, 2022, 2023; IDEA-Research, 2024a, 2024c; THU-MIG, 2025).

Como complemento a esta síntesis por paradigmas, en la Tabla A.1 del Anexo A se incluye una matriz ampliada orientada a prototipado, donde se comparan modelos representativos según familia arquitectónica, mecanismo visión-lenguaje, métricas reportadas, rendimiento y licenciamiento. Dicha matriz conserva el detalle técnico necesario para respaldar la selección posterior de alternativas, sin sobrecargar el cuerpo principal del estado del arte.

Del análisis comparativo emergen tres tensiones técnicas que deben considerarse como criterios de selección. La primera es la tensión entre precisión semántica y latencia de inferencia: los modelos con fusión visión-lenguaje más profunda suelen ofrecer mayor capacidad frente a consultas complejas, pero con un costo computacional que puede reducir la tasa de procesamiento. La segunda es la tensión entre generalización zero-shot y especialización de dominio: los benchmarks generales no representan por sí mismos las condiciones visuales de una obra civil. Esta tensión se extiende al fine-tuning. La evidencia revisada no permite atribuir la retención open-vocabulary a una familia arquitectónica por sí sola, porque las comparaciones utilizan datos, módulos entrenables y protocolos diferentes. La retención depende de la receta aplicada: qué parámetros se ajustan o congelan, si se conserva supervisión lingüística amplia y si se evalúan categorías no vistas (Cheng et al., 2024; Minderer et al., 2023; X. Zhao et al., 2024). Por ello, debe describirse para cada configuración y no inferirse de la profundidad o removibilidad de la fusión. La tercera es la tensión entre expresividad semántica y simplicidad del prompt: las consultas más precisas exigen mayor control de formulación, introduciendo una variable de diseño ausente en sistemas closed-set.

Una observación transversal es que, en los modelos que permiten reutilizar la representación textual, el cacheo de embeddings entre cuadros reduce el costo recurrente cuando el vocabulario permanece estable (A. Wang et al., 2025; T. Zhao et al., 2024). Dado que las condiciones de riesgo se definen al inicio de la sesión y se mantienen constantes, esta estrategia resulta directamente aplicable al escenario considerado.

Adicionalmente, la tendencia hacia pipelines composicionales descrita en esta sección introduce una cuarta tensión que opera en un plano distinto a las anteriores: la tensión entre modularidad e integrabilidad. Los enfoques que ensamblan múltiples modelos foundation —como la combinación de un detector OVD con un segmentador universal— ofrecen mayor flexibilidad para sustituir componentes y abordar tareas compuestas, pero acumulan latencia de inferencia por la ejecución secuencial de etapas y aumentan la complejidad de integración entre formatos de entrada y salida. Esta tensión no invalida el patrón composicional, pero señala que la evaluación de alternativas en etapas posteriores deberá considerar no solo el rendimiento de cada modelo de forma aislada, sino el costo total del pipeline resultante bajo las restricciones temporales del escenario de aplicación.

##### 15.2.3.1. Análisis de rendimiento para tiempo real

Desde el punto de vista del desempeño temporal, varios de los modelos analizados presentan características compatibles con aplicaciones de análisis de vídeo en tiempo real. La Tabla 3 resume puntos de operación publicados para modelos representativos y calcula, a partir de sus FPS, una latencia teórica por cuadro; estos valores no constituyen mediciones homogéneas de latencia.

**Tabla 3**

*Análisis comparativo de rendimiento de modelos OVD para tiempo real*

| **Modelo** | **Hardware** | **Framework** | **FPS** | **Latencia derivada (ms/cuadro)** | **LVIS-minival AP@[0,50:0,95]** |
| --- | --- | --- | --- | --- | --- |
| YOLOE-v8-S | T4 | TensorRT | 305,8 | 3,3 ms | 27,9 |
| YOLOE-v8-L | T4 | TensorRT | 102,5 | 9,8 ms | 35,9 |
| G-DINO 1.5 Edge | A100 | TensorRT | 75,2 | 13,3 ms | 36,2 |
| YOLO-World-L | V100 | PyTorch | 52,0 | 19,2 ms | 35,4 |

*Nota.* La columna «Latencia derivada» se calculó como 1000/FPS y expresa milisegundos por cuadro inferidos de la tasa publicada; no corresponde a una medición independiente de latencia. Los valores de FPS y AP provienen de trabajos originales con hardware, resolución, batch size y runtime no homogéneos. Por ello, la tabla muestra puntos de operación indicativos, no benchmarks normalizados ni latencia extremo a extremo. Fuente: elaboración propia basada en A. Wang et al. (2025), Ren, Jiang, et al. (2024) y Cheng et al. (2024).

Los puntos de operación de la tabla describen rendimiento publicado sobre benchmarks generales y no constituyen una predicción del desempeño sobre condiciones de EPP en construcción. La brecha entre benchmark general y condición de dominio se desarrolla en la sección 15.2.5.4.

#### 15.2.4. Adaptabilidad mediante fine-tuning y preservación de capacidad open-vocabulary

El ajuste de un modelo preentrenado introduce un compromiso entre especialización de dominio y preservación de las representaciones adquiridas. La literatura muestra que actualizar todos los parámetros puede mejorar el desempeño in-domain y, al mismo tiempo, deteriorar la generalización fuera de distribución frente a estrategias que congelan la mayor parte del modelo; este fenómeno se vincula con el olvido catastrófico (catastrophic forgetting) y exige medir la retención de forma explícita (Kirkpatrick et al., 2017; Kumar et al., 2022). Cuando la evidencia del dominio es limitada, la cantidad y ubicación de los parámetros actualizados también importan: el ajuste selectivo de capas puede preservar mejor información preentrenada que el ajuste completo (Lee et al., 2023).

En Grounding DINO se documentan fine-tuning closed-set, preentrenamiento continuado open-set y ajuste open-vocabulary; MM-Grounding-DINO muestra que la retención depende de mantener supervisión y evaluación sobre categorías no vistas (X. Zhao et al., 2024). La adaptación con LoRA constituye una variante de actualización acotada en la que se conservan congelados los backbones y se entrenan adaptadores de bajo rango (Rasaee et al., 2025). Como referencia de especialización, Grounding DINO con Swin-L reporta 62,6 AP en COCO val y 63,0 AP en test-dev tras fine-tuning closed-set, frente a 52,5 AP en su evaluación zero-shot; los regímenes no son equivalentes y no deben confundirse (Liu et al., 2024).

Para YOLO-World, la documentación distingue el ajuste con MixedGroundingDataset, que conserva textos y tareas de grounding, del ajuste closed-set con MultiModalDataset y vocabulario fijo. La variante reparametrizada elimina RepVL-PAN y el encoder textual, con lo cual prioriza eficiencia a costa de cerrar el vocabulario. El ajuste del encoder textual puede degradar la generalización, mientras que congelarlo o conservar supervisión abierta reduce ese riesgo (AILab-CVC, 2024; Cheng et al., 2024).

YOLOE ofrece linear probing y full tuning para transferencia a un dominio. La receta estándar produce un modelo de vocabulario fijo después del ajuste; los autores no reportan una métrica de retención open-vocabulary para ese camino. Evaluarla exige reinyectar vocabulario abierto y aplicar un protocolo explícito, de modo que especialización in-domain y capacidad abierta permanezcan como dimensiones separadas (A. Wang et al., 2025).

En los dual-encoders, el ajuste de extremo a extremo sobre datasets cerrados requiere estrategias de regularización para evitar el colapso del espacio de embeddings compartido del que depende la capacidad abierta (Minderer et al., 2022). OWLv2 aporta además la receta OWL-ST de autoentrenamiento con pseudoanotaciones; el uso de un vocabulario diverso derivado de n-gramas preserva mejor la generalización que un espacio de etiquetas estrecho (Minderer et al., 2023). En Florence-2, el ajuste mediante LoRA modifica una fracción acotada de parámetros, aunque la retención de clases base se informa como parcial y dependiente de la configuración (Ucar et al., 2025; Xiao et al., 2024).

En síntesis, no existe una jerarquía universal de familias frente al fine-tuning. La comparación defendible se realiza por receta concreta, distinguiendo parámetros actualizados, datos de adaptación y evaluación posterior de generalización. La Tabla 4 resume las estrategias documentadas y sus condiciones de retención.

**Tabla 4**

*Estrategias de fine-tuning documentadas y retención OVD reportada por familia arquitectónica*

| **Familia / Modelo** | **Estrategia de fine-tuning** | **Retención OVD reportada** | **Condición clave** |
| --- | --- | --- | --- |
| Grounding DINO | Fine-tuning closed-set | No | Vocabulario restringido post-ajuste |
| Grounding DINO | Preentrenamiento continuado open-set | Sí | LR reducido; módulos congelados; datos mixtos |
| Grounding DINO | Fine-tuning open-vocabulary (base a novel) | Sí | Evaluación explícita en categorías no vistas |
| Grounding DINO | Adaptación LoRA | Sí | Backbones congelados; solo adapters entrenables |
| YOLO-World | Fine-tuning con MixedGroundingDataset | Parcial | Depende de capas ajustadas; text encoder frágil |
| YOLO-World | Fine-tuning closed-set (MultiModalDataset) | No | Vocabulario fijo en JSON |
| YOLO-World | Reparametrización eficiente (sin RepVL-PAN) | No | Text encoder removido; equivale a YOLOv8 |
| YOLOE | Transferring (linear probing / full tuning) | No evaluada por los autores | La receta estándar produce vocabulario fijo; la retención requiere reinyectar y evaluar vocabulario abierto |
| OWL-ViT / OWLv2 | Fine-tuning de extremo a extremo con regularización | Parcial | Requiere estrategias de regularización |
| OWL-ViT / OWLv2 | Self-training (OWL-ST) con pseudo-anotaciones | Sí | Vocabulario diverso (n-gramas) preserva OVD |
| Florence-2 | Fine-tuning con LoRA | Parcial | Retención parcial de clases base; encoder congelado recomendado |

*Nota.* “Retención OVD reportada” resume el comportamiento informado para la receta y el protocolo indicados; no constituye una propiedad universal de la familia arquitectónica. “Parcial” indica una retención dependiente de la configuración específica —capas congeladas, tasa de aprendizaje, datos de entrenamiento y evaluación sobre categorías no vistas—. Fuente: elaboración propia basada en AILab-CVC (2024), Cheng et al. (2024), Liu et al. (2024), Minderer et al. (2022, 2023), Rasaee et al. (2025), Ucar et al. (2025), A. Wang et al. (2025), Xiao et al. (2024) y X. Zhao et al. (2024).

La evidencia sintetizada en la Tabla 4 permite identificar tres factores recurrentes: qué parámetros se ajustan o congelan, la amplitud y diversidad del vocabulario utilizado durante el entrenamiento, y la existencia de una evaluación explícita sobre categorías no vistas. Estos factores interactúan con la arquitectura, pero los trabajos revisados no aíslan sus efectos mediante un protocolo común. Por ello, no corresponde afirmar que una familia tolere mejor el ajuste completo; corresponde describir qué receta retuvo capacidad OVD, bajo qué datos y con qué protocolo de evaluación.

#### 15.2.5. Brechas identificadas en el dominio de la construcción civil

A partir de la revisión y síntesis de los enfoques presentados, se pone de manifiesto un conjunto de limitaciones estructurales que no quedan plenamente resueltas por los modelos actuales de detección *open-vocabulary*. Estas brechas delinean líneas de trabajo relevantes para etapas posteriores del proyecto y permiten anticipar desafíos técnicos que deberán abordarse durante el diseño arquitectónico y la implementación del prototipo.

##### 15.2.5.1. Contextualización semántica limitada

La mayoría de los detectores OVD actuales resuelven la detección como una combinación de localización espacial y compatibilidad textual evaluada de manera independiente para cada región candidata (Zareian et al., 2021; Liu et al., 2024). Este enfoque, aunque efectivo para identificar objetos individuales, no garantiza consistencia contextual entre múltiples entidades detectadas ni permite razonar sobre relaciones espaciales o semánticas entre ellas.

En entornos industriales y de construcción, muchos conceptos relevantes para la seguridad son inherentemente composicionales y dependen del contexto espacial. Condiciones como "persona sin casco cerca de excavación", "operario en zona de tránsito vehicular" o "escalera bloqueando salida de emergencia" requieren no solo detectar cada elemento de manera aislada, sino también evaluar sus relaciones geométricas y semánticas. Esta limitación impide dar por resueltas las condiciones relacionales a partir de la salida local del detector y exige que cualquier tratamiento adicional se defina y valide de forma explícita.

##### 15.2.5.2. Ausencia de consistencia temporal nativa

Los modelos de detección open-vocabulary operan predominantemente sobre imágenes estáticas, procesando cada cuadro de manera independiente sin mantener memoria de estados previos ni modelar explícitamente la evolución temporal de las detecciones. Esta característica introduce variabilidad entre cuadros consecutivos que puede manifestarse como fluctuaciones en los puntajes de confianza, apariciones y desapariciones espurias de detecciones, e inconsistencias en la asignación de etiquetas entre cuadros consecutivos.

En aplicaciones de vídeo, particularmente aquellas orientadas a monitoreo continuo, esta variabilidad temporal resulta problemática. Los enfoques generativos, como Florence-2, tienden a exhibir mayor inestabilidad debido a la naturaleza autoregresiva de su decodificación (Xiao et al., 2024). La literatura reciente sugiere que la integración con módulos de seguimiento multi-objeto (MOT) constituye una estrategia efectiva para mitigar este problema, permitiendo que el tracker aporte coherencia temporal a las detecciones semánticamente ricas del OVD (S. Li et al., 2023). No obstante, esta integración introduce complejidad arquitectónica adicional y requiere considerar la compatibilidad entre el detector y el método de seguimiento seleccionado.

##### 15.2.5.3. Sensibilidad a la formulación del prompt

La flexibilidad semántica que caracteriza a la detección open-vocabulary introduce una dependencia significativa respecto de la formulación exacta de las consultas textuales. Investigaciones en modelos visión-lenguaje han demostrado que pequeños cambios en la redacción de las consultas pueden producir diferencias significativas en el desempeño, incluso cuando diferentes formulaciones refieren al mismo concepto subyacente (Zhou et al., 2022b). Esta sensibilidad tiene implicancias directas para la usabilidad del sistema: usuarios con diferentes niveles de experiencia o distintas convenciones lingüísticas pueden obtener resultados heterogéneos ante objetivos de detección equivalentes.

Esta observación motivó el desarrollo de técnicas de prompt learning, donde los tokens de contexto se reemplazan por vectores aprendibles que se optimizan con datos etiquetados del dominio objetivo (Zhou et al., 2022b; Khattak et al., 2023). Sin embargo, las estrategias desarrolladas para clasificación de imágenes no se transfieren directamente al contexto de detección. Se demostró que la optimización automática de representaciones de prompts —específicamente diseñada para tareas de detección— supera consistentemente a los prompts elaborados mediante ingeniería manual, evidenciando la necesidad de enfoques especializados para el dominio OVD (Du et al., 2022). Adicionalmente, algunos modelos recientes abordan parcialmente esta limitación mediante el soporte de prompts visuales que permiten anclar la detección a ejemplos concretos en lugar de depender exclusivamente de descripciones textuales (Jiang et al., 2024).

##### 15.2.5.4. Sensibilidad al dominio de aplicación

Los benchmarks estándar utilizados para evaluar modelos OVD —como MS COCO con 80 categorías de objetos cotidianos (Lin et al., 2014) o LVIS con más de 1200 categorías de distribución long-tail (Gupta et al., 2019)— no representan plenamente las condiciones visuales y semánticas de entornos industriales especializados. En el contexto específico de obras de construcción, factores como iluminación extrema, oclusiones frecuentes por maquinaria y estructuras, indumentaria especializada de protección, y presencia de equipamiento industrial introducen distribuciones visuales que difieren significativamente de los datos de preentrenamiento.

Los resultados publicados en benchmarks generales no predicen por sí mismos el desempeño sobre una condición de dominio específica. Grounding DINO con backbone Swin-L pasa de 52,5 AP en COCO a 26,1 mean AP sobre los 35 conjuntos de ODinW. En consecuencia, la transferencia al dominio de construcción debe verificarse mediante una línea base zero-shot propia y un conjunto de prueba congelado, sin asumir equivalencia entre COCO o LVIS y la condición objetivo (Liu et al., 2024).

Como referencia supervisada in-domain, YOLOR alcanzó un mAP@0,5 de 0,883 sobre SHEL5K y un AP@0,5 de 0,907 para la clase head; YOLOv5x alcanzó un mAP@0,5 de 0,866 sobre CHV; y YOLOv9-e reportó un mAP@0,5 aproximado de 0,71 sobre SH17, con valores entre 0,58 y 0,69 para las variantes de YOLOv8 (Otgonbold et al., 2022; Wang et al., 2021; Ahmad & Rahimi, 2025).

Estas cifras corresponden a detectores entrenados sobre taxonomías específicas de EPP y no constituyen una comparación directa con los resultados de COCO o LVIS. En particular, el AP@0,5 de 0,907 para la clase *head* muestra que un detector supervisado puede alcanzar un desempeño alto sobre esa categoría en SHEL5K. La cifra no permite inferir una dificultad intrínseca universal, pero sí establece una referencia in-domain para analizar el costo de formular la condición sin entrenamiento específico.

La evidencia ubicada específicamente en el cruce entre vocabulario abierto y EPP es todavía limitada. Choi y Greer (2024) evaluaron OWLv2 zero-shot sobre 5.210 imágenes: obtuvieron AP@IoU>0,5 de 0,6767 para *person* y 0,6493 para detección directa de *hardhat*. Al introducir asociación jerárquica, la clase *head* —cabeza sin casco— alcanzó 0,1024 AP y la cascada multietapa obtuvo 0,2699 AP para detección de casco. Estas cifras no equivalen a una métrica de condición o alerta, pero muestran que la asociación persona–cabeza–EPP agrega dificultad respecto de detectar los componentes por separado.

Como evidencia adyacente, Chen y Zou (2025) evaluaron modelos visión-lenguaje generativos en una tarea de visual grounding y observaron IoU total inferior al 20 % para objetivos con restricciones de atributo, como trabajadores con casco blanco. El resultado no constituye un benchmark de detectores OVD, pero respalda la dificultad de localizar condiciones visuales finamente especificadas mediante lenguaje natural.

El relevamiento de publicaciones entre 2023 y 2026 no identificó evaluaciones de Grounding DINO o YOLO-World zero-shot sobre SHEL5K o CHV, ni un benchmark multi-fuente de EPP bajo protocolo COCO. Esta ausencia constituye una brecha del estado del arte: los benchmarks generales no resuelven la evaluación de una condición de dominio expresada mediante lenguaje natural, por lo que se requiere una línea base zero-shot propia y un conjunto de prueba congelado. La respuesta experimental a esta brecha corresponde a las secciones posteriores.

##### 15.2.5.5. Protocolos de evaluación específicos para seguridad industrial

Las métricas de evaluación predominantes en la literatura OVD —como Average Precision (AP) en COCO o LVIS— constituyen indicadores generales de rendimiento que no capturan adecuadamente el valor operativo de un sistema de detección en el contexto de seguridad industrial (Gupta et al., 2019). Estas métricas evalúan la precisión de localización y clasificación cuadro a cuadro, sin considerar aspectos temporales ni el impacto diferenciado de distintos tipos de error en escenarios de monitoreo de riesgos.

Para validar la plataforma en su dominio de aplicación, resulta necesario diseñar métricas y protocolos de evaluación alineados con los objetivos de seguridad en construcción. Esto incluye considerar la tasa de eventos de riesgo detectados correctamente a lo largo de secuencias de video, el tiempo transcurrido entre el inicio de una condición de riesgo y su detección (latencia de alerta), la tasa de falsas alarmas por unidad de tiempo de monitoreo, y la persistencia mínima requerida para considerar válida una detección.

##### 15.2.5.6. Tabla comparativa de brechas identificadas

La Tabla 5 organiza las brechas identificadas en las subsecciones precedentes con su descripción técnica y su implicación específica para el proyecto.

**Tabla 5**

*Brechas identificadas en la aplicación de modelos OVD al dominio de seguridad en construcción civil*

| **Brecha identificada** | **Descripción** | **Implicación para el proyecto** |
| --- | --- | --- |
| Contextualización semántica limitada | Los modelos OVD detectan entidades localmente pero no infieren relaciones espaciales complejas entre ellas (p. ej., “persona dentro de zona restringida” requiere razonamiento relacional) | Las condiciones composicionales no pueden evaluarse a partir de la salida local del detector sin una estrategia adicional explícitamente definida y validada. |
| Ausencia de consistencia temporal nativa | La detección cuadro a cuadro introduce variabilidad en puntajes de confianza, apariciones y desapariciones espurias entre cuadros consecutivos | Necesidad de integración con módulo MOT para aportar coherencia temporal a las detecciones semánticas (S. Li et al., 2023) |
| Sensibilidad a la formulación del prompt | Pequeños cambios en la redacción producen diferencias significativas en el desempeño, incluso para conceptos equivalentes (Zhou et al., 2022b) | El diseño de prompts para condiciones de riesgo requiere un proceso sistemático; la selección informal puede comprometer la robustez del sistema |
| Brecha de dominio con benchmarks estándar | Los resultados en COCO o LVIS no garantizan transferencia al dominio objetivo. Grounding DINO con backbone Swin-L pasa de 52,5 AP en COCO a 26,1 mean AP en ODinW. | El protocolo debe incorporar una línea base zero-shot propia y un conjunto de prueba de dominio congelado; los benchmarks generales funcionan únicamente como referencia externa. |
| Ausencia de protocolos de evaluación específicos para seguridad industrial | Las métricas AP en COCO/LVIS (Gupta et al., 2019; Lin et al., 2014) no capturan el valor operativo del sistema: no consideran latencia de alerta, persistencia de la detección ni impacto diferenciado de falsos positivos/negativos. | El protocolo experimental debe definir métricas alineadas con el valor operativo de la alerta, incluyendo persistencia temporal, latencia y tratamiento diferenciado de falsos positivos y falsos negativos. |
| Escasez de evaluación OVD × EPP | La literatura ofrece evidencia directa limitada. Choi y Greer (2024) reportan AP@IoU>0,5 de 0,6767 para *person*, 0,6493 para detección directa de *hardhat*, 0,1024 para la clase *head* y 0,2699 para la cascada multietapa. El relevamiento no identificó evaluaciones de Grounding DINO o YOLO-World zero-shot sobre SHEL5K o CHV, ni un benchmark de EPP multi-fuente bajo protocolo COCO. | Se requiere una línea base zero-shot propia y un conjunto de prueba congelado; la respuesta experimental se presenta fuera del estado del arte. |

*Nota.* Las brechas listadas delimitan problemas técnicos que el protocolo y la arquitectura deben abordar; no se presentan como limitaciones insalvables. Fuente: elaboración propia basada en Choi y Greer (2024), Chen y Zou (2025), Gupta et al. (2019), S. Li et al. (2023), Lin et al. (2014), Liu et al. (2024), Zareian et al. (2021) y Zhou et al. (2022b).

#### 15.2.6. Síntesis de la sección y avance al seguimiento multi-objeto

El análisis de los paradigmas OVD evidencia que la viabilidad de su integración en sistemas de monitoreo continuo está condicionada por cuatro factores: balance entre expresividad semántica y eficiencia de inferencia, diseño sistemático de prompts para el dominio específico, mecanismos de compensación de la variabilidad temporal cuadro a cuadro, y evaluación empírica en condiciones visuales de construcción civil. Los dos últimos factores remiten directamente al problema de persistencia temporal: dado que la OVD produce observaciones instantáneas sin identidad ni continuidad, la sección siguiente analiza los métodos de seguimiento multiobjeto como mecanismo para sostener esas detecciones a lo largo del tiempo.

En las secciones posteriores se distinguirá entre calibración operativa y adaptación paramétrica. La primera comprende cambios de resolución de entrada, formulación del vocabulario, umbrales, postproceso y estabilización temporal sin modificar los pesos del modelo; la segunda refiere exclusivamente al ajuste de parámetros mediante fine-tuning u otras técnicas de entrenamiento. Con esta distinción se evita presentar configuraciones de plataforma como si fueran modelos reentrenados.

### 15.3. Seguimiento multiobjeto: métodos, métricas y brechas del estado del arte

El seguimiento multiobjeto (MOT) constituye el mecanismo que transforma las detecciones instantáneas producidas por el sistema OVD en trayectorias persistentes a lo largo del tiempo, habilitando la agregación temporal de evidencias necesaria para la generación de alertas operativas. En esta sección se analizan los métodos representativos del estado del arte en MOT para sistemas de video en tiempo real, las métricas de evaluación relevantes para el contexto del proyecto y las brechas identificadas en la intersección entre MOT y detección open-vocabulary.

#### 15.3.1. Métodos representativos

El estado del arte en MOT para sistemas de video en tiempo real está dominado por la familia SORT extendida, cuya evolución refleja el progreso en el manejo de oclusiones, la explotación de detecciones de baja confianza y la eliminación de dependencias de entrenamiento específico por dominio.

##### 15.3.1.1. SORT

SORT (Simple Online and Realtime Tracking) establece el esquema de referencia del paradigma tracking-by-detection moderno. Combina el filtro de Kalman para el modelado del movimiento con el algoritmo Húngaro para la asignación óptima de detecciones a trayectorias, utilizando IoU como única métrica de similitud. Su diseño minimalista prescinde de cualquier modelado de apariencia, lo que resulta en latencia muy baja —capacidad de operar a tasas superiores a 200 FPS— y ausencia total de dependencias de entrenamiento. La principal limitación de SORT es su baja robustez ante oclusiones: cuando un objeto no es detectado durante varios cuadros consecutivos, la trayectoria se termina y la re-asociación posterior puede producir un cambio de identificador (ID switch), fragmentando la trayectoria en múltiples segmentos (Bewley et al., 2016).

##### 15.3.1.2. Contraste con variantes posteriores

Las extensiones de tracking-by-detection introducen distintos mecanismos para mejorar la continuidad: DeepSORT agrega apariencia mediante ReID (Wojke et al., 2017); ByteTrack reutiliza detecciones de baja confianza para sostener trayectorias (Y. Zhang et al., 2022); y OC-SORT corrige la estimación de movimiento durante oclusiones sin requerir apariencia (Cao et al., 2023). En el extremo de mayor complejidad, BoT-SORT combina movimiento y ReID, mientras que TrackFormer y MOTR aprenden detección y asociación de manera conjunta. Estas variantes permiten contrastar robustez, dependencia de entrenamiento y costo computacional, pero no establecen por sí mismas un método preferente para una plataforma OVD modular; la síntesis comparativa se conserva en la Tabla 6.

#### 15.3.2. Síntesis comparativa de métodos MOT

La Tabla 6 sintetiza las características principales de los métodos MOT analizados, con énfasis en las dimensiones más relevantes para su integración en el sistema E-OVRT-VDP: paradigma, modelo de movimiento, estrategia de asociación, robustez ante oclusiones, latencia y dependencias de entrenamiento.

**Tabla 6**

*Síntesis comparativa de métodos MOT representativos según dimensiones relevantes para sistemas de video en tiempo real con detección open-vocabulary*

| **Método** | **Paradigma** | **Modelo de movimiento** | **Asociación de datos** | **Robustez a oclusiones** | **Latencia / FPS** | **Dependencia de entrenamiento** |
| --- | --- | --- | --- | --- | --- | --- |
| SORT | Tracking-by-detection | Kalman lineal | IoU + Húngaro | Baja | Muy alta (>200 FPS) | Ninguna |
| DeepSORT | Tracking-by-detection | Kalman lineal | Cascada: movimiento + apariencia | Media-Alta | Media | Modelo ReID preentrenado |
| ByteTrack | Tracking-by-detection | Kalman lineal | Jerárquica: alta/baja confianza + IoU | Alta | Muy alta (>170 FPS) | Ninguna |
| OC-SORT | Tracking-by-detection | Kalman + correcciones OC | IoU + consistencia de momento (OCM) | Media-Alta | Muy alta | Ninguna |
| BoT-SORT | Tracking-by-detection | Kalman mejorado + CMC | Fusión IoU-ReID | Alta | Media | Modelo ReID preentrenado |
| TrackFormer / MOTR | End-to-end (Transformer) | Atención temporal aprendida | Mecanismo de atención global | Muy alta | Baja | Entrenamiento conjunto requerido |

*Nota.* CMC = Compensación de Movimiento de Cámara (Camera Motion Compensation). OC = Observation-Centric. La columna 'Dependencia de entrenamiento' refiere a componentes adicionales al detector base que requieren entrenamiento supervisado. FPS estimados corresponden a las configuraciones reportadas en los trabajos originales sobre hardware de referencia; pueden variar significativamente según el hardware y la resolución de entrada. Fuente: Elaboración propia basada en las fuentes citadas (Adžemović, 2025; Aharon et al., 2022; Bewley et al., 2016; Cao et al., 2023; Wojke et al., 2017; Y. Zhang et al., 2022).

##### 15.3.2.1. Observaciones críticas sobre la comparativa

La literatura comparativa muestra que los métodos de seguimiento difieren no sólo en sus resultados agregados, sino también en las dependencias que introducen. Los enfoques geométricos sin modelos de apariencia pueden acoplarse a detectores externos sin requerir entrenamiento adicional de ReID, mientras que las variantes basadas en apariencia o entrenamiento conjunto dependen de datos y componentes específicos (Adžemović, 2025; Wojke et al., 2017). Esta diferencia delimita un compromiso entre simplicidad de integración y robustez de asociación; por sí sola, no determina la elección de un tracker para una plataforma OVD.

#### 15.3.3. Métricas de evaluación para MOT

MOTA resume falsos negativos, falsos positivos y cambios de identidad respecto del ground truth, aunque su lectura está fuertemente condicionada por los errores de detección (Bernardin & Stiefelhagen, 2008). IDF1 enfatiza la consistencia de identidad a lo largo de la secuencia (Ristani et al., 2016), mientras que HOTA separa y combina calidad de detección, asociación y localización (Luiten et al., 2021). Estas métricas caracterizan al tracker, pero no miden el valor temporal de una alerta; la evaluación de un sistema asistivo exige niveles adicionales, cuya definición corresponde al protocolo experimental. Una comparación ampliada de estas métricas y de sus limitaciones se presenta en la Tabla A.2 del Anexo A.

#### 15.3.4. Brechas identificadas y desafíos para el prototipo

El análisis del estado del arte en MOT revela un conjunto de brechas que condicionan el diseño del prototipo y las decisiones metodológicas de la consolidación metodológica posterior. La Tabla 7 organiza estas brechas con su descripción técnica y su implicación específica para el proyecto.

**Tabla 7**

*Brechas identificadas en la aplicación de métodos MOT al contexto de seguridad en construcción civil en combinación con detección open-vocabulary*

| **Brecha identificada** | **Descripción** | **Implicación para el proyecto** |
| --- | --- | --- |
| Dependencia de la calidad del detector subyacente | El rendimiento del MOT está fuertemente acoplado al desempeño del detector. Errores de detección —FP, FN, bounding boxes inestables— se propagan al seguimiento, produciendo fragmentación de trayectorias, pérdidas de identidad y asociaciones erróneas (S. Li et al., 2025) | En el pipeline OVD + MOT, la variabilidad inherente de la detección open-vocabulary puede amplificar errores de asociación; el diseño del sistema debe contemplar estrategias de filtrado y umbralización que reduzcan el ruido de entrada al tracker |
| Fragilidad ante oclusiones prolongadas | Aunque los métodos modernos manejan oclusiones breves, las oclusiones de larga duración producen terminación prematura de trayectorias, re-asociaciones inciertas y aumento de ID switches (Du et al., 2024) | En entornos de obra civil con alta densidad de obstrucciones (andamios, maquinaria, materiales), la robustez ante oclusiones es una restricción de diseño relevante que debe evaluarse empíricamente |
| Métricas estándar no alineadas con objetivos operativos de seguridad | Las métricas MOTA, IDF1 y HOTA evalúan el desempeño del seguimiento cuadro a cuadro sin considerar el impacto operativo diferenciado de distintos tipos de error en el contexto de seguridad laboral (Luiten et al., 2021) | Se deben definir criterios de evaluación del componente MOT alineados con el dominio: persistencia mínima para disparar alertas, penalización diferenciada de ID switches en condiciones de riesgo, y tolerancia ante falsos positivos por oclusión |
| Ausencia de datasets de construcción con anotaciones de seguimiento | Los benchmarks estándar de MOT (MOT17, MOT20, DanceTrack) no contemplan el dominio de obras civiles; la evaluación del tracker en condiciones representativas requiere datos del dominio específico (Dendorfer et al., 2020; Milan et al., 2016) | La validación del componente MOT en el prototipo no puede apoyarse en benchmarks estándar; se requiere la definición de un protocolo de evaluación propio con datos recopilados en el contexto del proyecto |

*Nota.* Las brechas listadas definen el espacio de problemas abiertos que deben abordarse en el diseño experimental (etapa 2) y en la implementación del prototipo (etapa 4). Fuente: Elaboración propia basada en las fuentes citadas (Adžemović, 2025; Dendorfer et al., 2020; Du et al., 2024; S. Li et al., 2025; Luiten et al., 2021; Milan et al., 2016).

La brecha de ausencia de datasets de construcción con anotaciones de seguimiento merece una consideración adicional. Los benchmarks estándar de MOT —MOT17, MOT20, DanceTrack— fueron diseñados para escenarios de peatones en entornos urbanos y eventos de danza respectivamente, con distribuciones visuales que difieren significativamente de una obra civil: densidad de cámara fija en planos elevados, entidades heterogéneas (personas, maquinaria, materiales), indumentaria de protección que puede confundir a los modelos de apariencia, y configuraciones de oclusión determinadas por la geometría de la obra. Esta brecha no puede resolverse mediante adaptación de los benchmarks existentes; requiere la definición de un protocolo de evaluación propio que se apoyará en los datos recopilados durante la fase experimental del proyecto.

### 15.4. Video en tiempo real y streaming: protocolos, servidores y brechas del estado del arte

#### 15.4.1. Protocolos de transmisión de video de baja latencia

Los protocolos de transmisión de vídeo constituyen un componente relevante dentro del análisis de sistemas de vídeo en tiempo real, debido a que condicionan la forma en que los flujos provenientes de cámaras o fuentes de vídeo son transportados hacia los módulos de procesamiento, visualización o almacenamiento. En el contexto del presente proyecto, su estudio resulta necesario porque la detección open-vocabulary no opera sobre imágenes aisladas, sino sobre secuencias continuas que deben ser recibidas, decodificadas y procesadas con una latencia compatible con la generación oportuna de alertas.

Desde una perspectiva general, los protocolos de streaming pueden diferenciarse por dimensiones como el modelo de entrega, el esquema de distribución, la tolerancia a pérdidas, los mecanismos de buffering y el orden de magnitud de latencia que suelen alcanzar bajo determinadas condiciones de red y configuración. Sin embargo, estos valores no deben interpretarse como propiedades absolutas de cada protocolo, ya que la latencia final depende del pipeline completo: captura, codificación, transporte, decodificación, inferencia, evaluación de patrones y comunicación de resultados. Estos componentes serán retomados con mayor detalle en el marco teórico y en la descripción técnica del sistema, donde se analizará su impacto dentro de la arquitectura experimental.

En esta sección, el análisis se limita a revisar los protocolos y familias de transmisión más relevantes para aplicaciones de baja latencia, identificando sus características principales, sus restricciones prácticas y su grado de compatibilidad con un sistema de análisis automatizado de vídeo. Esta revisión permite establecer criterios preliminares para la selección posterior del stack de medios, sin definir todavía una implementación definitiva.

##### 15.4.1.1. Criterios de clasificación de protocolos

**Modelo de entrega push.** En el modelo push, una vez establecida la sesión, el emisor entrega el flujo de manera continua hacia el receptor (típicamente sobre UDP o sobre una sesión persistente), minimizando esperas asociadas a la solicitud de unidades discretas de contenido. Protocolos de tiempo real, como RTP y flujos interactivos como WebRTC, se alinean más naturalmente con push (ISO/IEC, 2022; May, 2017).

**Modelo de entrega pull.** En el modelo pull, el control de la entrega reside principalmente en el cliente: el receptor solicita (por HTTP) segmentos o partes de segmentos en forma sucesiva, habilitando escalabilidad y cacheo, pero introduciendo buffering y latencias asociadas a segmentación y recarga. Los esquemas adaptativos sobre HTTP, como HLS y MPEG-DASH, responden al patrón pull (cliente-driven).

**Esquema de distribución unicast.** En unicast, cada cliente mantiene una conexión individual y recibe un flujo dedicado, lo que simplifica control por receptor (adaptación, seguridad, métricas), pero escala el consumo de ancho de banda en el emisor.

**Esquema de distribución multicast.** En multicast, el emisor envía un único flujo a un grupo multicast y la red replica hacia múltiples receptores, siendo eficiente en redes administradas. Protocolos basados en RTP pueden operar sobre unicast o multicast; sin embargo, el multicast IP no es viable en Internet abierta (en general no es ruteable extremo-a-extremo y complica control de congestión por receptor).

**Orden de magnitud de latencia.** Otra forma práctica de categorizar protocolos es por la latencia extremo a extremo típica que habilitan bajo configuraciones habituales. En términos operativos pueden distinguirse tres rangos:

**Alta latencia (>~3 s).** Protocolos orientados a distribución masiva y robustez. Aquí se ubican implementaciones “clásicas” de HLS y MPEG-DASH con segmentos de varios segundos. Al apoyarse en HTTP/HTTPS y CDN, priorizan escalabilidad y tolerancia a fallos, usualmente con latencias del orden de varios segundos a decenas de segundos (ISO/IEC, 2022; May, 2017).

**Latencia media (~0,5 a 3 s).** Incluye protocolos como RTMP (en ingesta), RTSP cuando se opera con buffers conservadores o sobre TCP, y variantes de baja latencia de HLS/DASH basadas en segmentación fina y entrega parcial.

**Baja latencia (<~500 ms).** Protocolos diseñados para interactividad estricta y respuesta casi en tiempo real: WebRTC, SRT, RIST y flujos RTP con mínima capa de sesión. En general emplean UDP para evitar la penalidad de retransmisiones fuera de plazo y operan con buffers pequeños, compensando la pérdida con estrategias específicas (p. ej., ARQ “dentro de un presupuesto de tiempo” en SRT/ RIST). En WebRTC, además, la conectividad extremo-a-extremo depende de mecanismos de traversal NAT como ICE, que influyen en la latencia efectiva según el tipo de red (Keranen et al., 2018; Nakagawa et al., 2021; Schulzrinne et al., 2003; Sharabayko et al., 2024; Video Services Forum, 2020).

##### 15.4.1.2. Mapa de familias de protocolos según los criterios de clasificación

En esta sección, se analizan los protocolos más relevantes aplicando sistemáticamente (i) modelo de entrega, (ii) esquema de distribución y (iii) latencia típica, además de consideraciones prácticas pertinentes a cada protocolo (NAT, resiliencia, seguridad, tooling).

RTSP/RTP: el estándar de cámaras IP industriales. El Real-Time Streaming Protocol (RTSP) es un protocolo de capa de aplicación orientado al control de sesiones de streaming. Fue especificado inicialmente en el RFC 2326 (Schulzrinne et al., 1998) y posteriormente revisado en RTSP 2.0 mediante el RFC 7826 (Schulzrinne et al., 2016). RTSP opera como plano de control: el cliente describe la sesión, negocia parámetros y ejecuta acciones de control, mientras que el audio y el video suelen transportarse mediante un protocolo de medios separado.

En este esquema, el transporte de medios suele realizarse con Real-time Transport Protocol (RTP), definido en el RFC 3550, acompañado por RTCP para informar pérdida y jitter (Schulzrinne et al., 2003). RTP se encapsula típicamente sobre UDP e incorpora timestamps y números de secuencia para facilitar la reconstrucción temporal y el manejo del jitter. RTSP/RTP se adoptó ampliamente en videovigilancia y cámaras IP por su madurez y compatibilidad; ONVIF Profile S lo utiliza como mecanismo central de consumo y control de streams (ONVIF, 2019). En redes controladas puede utilizar UDP para el transporte, mientras que RTP/RTCP interleaved sobre la conexión TCP de RTSP simplifica el cruce de firewalls a costa de los compromisos propios de TCP (Schulzrinne et al., 1998, 2016).

En cuanto a latencia, los valores reportados para un protocolo son rangos típicos y no compromisos del estándar. La latencia extremo a extremo depende de captura, codificación, red, decodificación y, de manera marcada, del buffer del receptor. Axis Communications AB (2015) identifica el play-out buffer como un componente que puede dominar el retardo cuando se prioriza estabilidad frente a jitter. Bajo condiciones favorables, RTSP/RTP puede operar en el orden de cientos de milisegundos —aproximadamente 200–800 ms—; configuraciones de videovigilancia con buffering conservador pueden elevar ese valor a 1.000–2.000 ms o más (Axis Communications AB, 2015).

#### 15.4.2. Alternativas complementarias de ingesta, transporte y distribución

Además de RTSP/RTP, la literatura de transmisión de baja latencia comprende familias con compromisos diferentes. Los esquemas HTTP adaptativos —HLS y MPEG-DASH, incluidas sus extensiones de baja latencia— priorizan escalabilidad y robustez mediante segmentación; WebRTC integra negociación, transporte y control de congestión para interacción sub-segundo; y SRT/RIST agregan recuperación selectiva de pérdidas sobre UDP para enlaces variables. Estas alternativas no son directamente equivalentes: la latencia observada depende del códec, los buffers, la red y la implementación, por lo que su comparación debe interpretarse como un mapa de propiedades y no como un ranking universal. La Tabla 8 resume estas diferencias.

La captura mediante SDK constituye una alternativa distinta del consumo de un stream ya codificado. En cámaras inteligentes, el host puede gobernar un pipeline ejecutado en el dispositivo y recibir las unidades visuales o salidas requeridas para el procesamiento posterior. Esta modalidad permite desplazar operaciones acotadas de adquisición o preprocesamiento hacia la fuente sin equipararla a inferencia OVD en el borde (Luxonis, s. f.-b).

Los servidores de medios implementan combinaciones de retransmisión, pasarela, reempaquetamiento o transcodificación. Su aporte a la latencia depende de si transforman el contenido o sólo lo reenvían: la transcodificación incorpora decodificación y recodificación, mientras que un relay agrega principalmente un salto de red y gestión de colas. Para un pipeline de analítica visual, esta distinción resulta más relevante que un catálogo extenso de productos, porque permite separar el costo del transporte del costo de transformación multimedia (Ahmad et al., 2005; Amirante et al., 2014, 2015).

En la salida del pipeline, los patrones publicador-suscriptor permiten desacoplar la generación de eventos de sus consumidores. MQTT formaliza distintos niveles de calidad de servicio; QoS 1 garantiza entrega al menos una vez mediante confirmación PUBACK, por lo que una aplicación debe tolerar posibles reentregas y controlar idempotencia cuando un mismo evento no deba producir efectos duplicados (OASIS, 2019). Esta propiedad permite distinguir la generación interna de una alerta de su distribución posterior.

#### 15.4.3. Brechas del estado del arte en el streaming/OVD

Las tecnologías y arquitecturas actuales de streaming presentan un conjunto de limitaciones que condicionan directamente el diseño del pipeline experimental.

##### 15.4.3.1. Ausencia de benchmarks extremo a extremo integrados para pipelines OVD

La literatura revisada evidencia una fragmentación sistemática en la evaluación de desempeño: los benchmarks de inferencia de modelos OVD (p. ej., AP en COCO/LVIS, FPS en GPU aislada) operan de forma independiente respecto de los benchmarks de streaming (latencia de transporte, throughput de protocolo) y de las métricas de plataformas de edge computing (TOPS, FPS bajo carga térmica). Para una plataforma como E-OVRT-VDP el criterio de selección debe basarse en mediciones reproducibles del pipeline completo, y no extrapolarse directamente de métricas parciales o aisladas.

Esta brecha implica que no existen referentes directos en la literatura que permitan predecir con confianza el desempeño de un sistema que combina ingesta de video, inferencia OVD y emisión de eventos bajo restricciones de latencia propias de operación en tiempo real. En consecuencia, la validación empírica del pipeline completo constituye una contribución necesaria del proyecto, y la definición de protocolos de medición reproducibles deberá abordarse como parte del diseño experimental en la etapa 2.

##### 15.4.3.2. Integración de modelos OVD dentro de pipelines de streaming optimizados

Los frameworks de streaming más maduros para video analytics en tiempo real, como NVIDIA DeepStream, han sido históricamente diseñados y optimizados para detectores de clases fijas con arquitecturas convolucionales estándar, cuyos patrones de integración asumen una entrada de imagen y un conjunto predefinido de clases de salida (NVIDIA, 2024). Si bien el ecosistema ha comenzado a incorporar soporte para modelos open-vocabulary —por ejemplo, NVIDIA TAO Toolkit incluye flujos de exportación y despliegue para Grounding DINO (NVIDIA, s. f.-g)—, la integración de estos modelos en pipelines de streaming presenta desafíos técnicos que no se resuelven con la misma inmediatez que los detectores convencionales.

En particular, la conversión de modelos OVD a formatos optimizados como TensorRT puede requerir adaptaciones no triviales cuando la arquitectura incluye operadores no soportados nativamente o componentes dinámicos asociados a la codificación de prompts textuales. Dado que TensorRT no admite entradas de tipo texto, la etapa de tokenización debe separarse del grafo del modelo y gestionarse externamente (NVIDIA, s. f.-g), lo que introduce complejidad adicional en el diseño del pipeline. Más ampliamente, la arquitectura multi-modal que caracteriza a los modelos OVD —con un encoder visual y un encoder textual que interactúan mediante mecanismos de fusión— no se alinea directamente con los patrones de integración nativos de los plugins de inferencia estándar de estos frameworks, aunque rutas alternativas como la integración con Triton Inference Server ofrecen mayor flexibilidad al soportar modelos en múltiples formatos y frameworks (NVIDIA, s. f.-h). Esta brecha, si bien se está reduciendo, sugiere que la integración de modelos OVD dentro del pipeline de streaming requerirá capas de adaptación específicas cuya complejidad y costo deberán evaluarse empíricamente.

##### 15.4.3.3. Interoperabilidad efectiva entre protocolos heterogéneos

Aun cuando la literatura describe los roles del servidor de medios y las funciones de pasarela, reempaquetamiento y transcodificación (§15.4.2), no ofrece evidencia consolidada sobre el overhead real introducido por las conversiones entre protocolos —por ejemplo, de RTSP a WebRTC o de RTMP a SRT— en condiciones de operación representativas. La transcodificación, el reempaquetamiento entre contenedores de medios —como MPEG-TS, FLV o fMP4— y la adaptación entre pilas de transporte pueden agregar latencia y puntos de fallo que no quedan reflejados en las especificaciones de cada protocolo por separado.

Esta brecha resulta relevante en el contexto de E-OVRT-VDP, dado que en entornos reales de obra el parque de cámaras puede exponer flujos mediante protocolos diversos. Si bien el prototipo experimental operará previsiblemente con un conjunto acotado de fuentes y protocolos, la identificación de este vacío en la literatura permite anticipar un factor de complejidad para escenarios de despliegue más amplios y orienta el diseño hacia soluciones que no introduzcan dependencias rígidas con un único protocolo de ingesta.

##### 15.4.3.4. Métricas de evaluación alineadas con objetivos de seguridad laboral

Las métricas estándar de evaluación de sistemas de streaming, tales como latencia media, throughput, tasa de pérdida de paquetes y calidad visual (PSNR/SSIM), no capturan adecuadamente el valor operativo de un sistema orientado a la detección asistiva de riesgos en obra. De manera análoga a lo identificado en la sección de OVD respecto de las métricas de detección, las métricas de streaming convencionales no consideran aspectos como el tiempo transcurrido entre el inicio de una condición de riesgo y la notificación al operador, la continuidad de detección bajo variaciones de calidad del stream, o el impacto diferenciado de artefactos de compresión sobre la detectabilidad de elementos de protección personal.

#### 15.4.4. Síntesis comparativa de protocolos

La Tabla 8 sintetiza las características principales de los protocolos analizados, con énfasis en las dimensiones de mayor relevancia para el diseño del sistema E-OVRT-VDP.

**Tabla 8**

*Comparativa de protocolos de transmisión de video de baja latencia para sistemas de video analítico en tiempo real*

| **Protocolo** | **Latencia típica extremo a extremo** | **Transporte base** | **Modelo de entrega** | **Resiliencia a pérdida** | **Cifrado nativo** | **Caso de uso principal** |
| --- | --- | --- | --- | --- | --- | --- |
| RTSP/RTP | ~200–800 ms | UDP (o TCP) | RTSP controla la sesión; RTP transporta el flujo | Media (con RTCP) | Opcional (RTSPS) | Cámaras IP industriales, CCTV, entornos LAN controlados |
| RTMP | ~2–5 s | TCP | Push | Alta (TCP garantiza entrega) | Sí (RTMPS/TLS) | Ingesta a plataformas de streaming; encoders hacia servidores |
| HLS / MPEG-DASH | ~5–45 s (LL: ~2–10 s) | HTTP/TCP | Pull (segmentado) | Alta (CDN + HTTP) | Sí (HTTPS) | Distribución masiva de contenido; viewers simultáneos elevados |
| WebRTC | < 500 ms | UDP (SRTP sobre DTLS) | Push/Pull (P2P o SFU) | Media (con NACK/FEC) | Sí (DTLS-SRTP, obligatorio) | Interactividad ultra-baja latencia; videoconferencia; monitoreo P2P |
| SRT | ~120–500 ms (configurable) | UDP + ARQ selectivo | Push o Pull | Alta (ARQ con presupuesto de tiempo) | Sí (AES-128/256) | Contribución broadcast; enlaces WAN no confiables; 4G/5G |
| RIST | ~120–500 ms | RTP + ARQ (RTCP FB) | Push o Pull (multicast posible) | Alta (ARQ + FEC) | Sí (DTLS) | Broadcast profesional; distribución multicast en redes gestionadas |

*Nota.* Los rangos de latencia extremo a extremo reportados son valores típicos dependientes de configuración, no compromisos de los estándares. La latencia final está determinada por el pipeline completo (captura, codificación, transporte, decodificación, inferencia), no únicamente por el protocolo. HLS/DASH LL = Low-Latency HLS / DASH. DTLS-SRTP = combinación de Datagram TLS y Secure RTP (cifrado obligatorio en WebRTC). ARQ = Automatic Repeat reQuest. FEC = Forward Error Correction. SFU = Selective Forwarding Unit. NACK = Negative Acknowledgement. Fuente: Elaboración propia basada en Axis Communications AB (2015), DASH Industry Forum (2020), ISO/IEC (2022), Keranen et al. (2018), May (2017), Pantos (2025), Parmar y Thornburgh (2012), Roy (2024), Schulzrinne et al. (1998, 2003, 2016), Sharabayko et al. (2024), Sonono (2019), Video Services Forum (2020, 2024) y World Wide Web Consortium (2025).

La tabla muestra que no existe un protocolo que maximice simultáneamente latencia mínima, alta resiliencia a pérdidas y escalabilidad, lo cual es coherente con el enfoque de diseño de cada estándar, orientado a prioridades diferentes según el contexto de aplicación. En arquitecturas comúnmente adoptadas, esta situación suele abordarse mediante esquemas híbridos que emplean protocolos distintos por tramo del flujo de video: uno para ingesta y transporte desde el origen hacia un servidor o plataforma de medios (en entornos LAN o WAN con distintos niveles de control), y otro para distribución/visualización hacia clientes finales, donde los requerimientos de interactividad, número de usuarios y compatibilidad con navegadores influyen de manera determinante. De forma complementaria, también es habitual que los protocolos HTTP adaptativos (HLS/DASH) se reserven para consumo masivo, reproducción diferida o escenarios donde la prioridad sea la escalabilidad y la tolerancia a variaciones de red, más que la inmediatez. En consecuencia, la evidencia comparativa respalda que la selección de protocolos debe abordarse como una decisión dependiente del escenario y de la infraestructura, y suele validarse mediante pruebas empíricas sobre el pipeline completo (captura, codificación, transporte, decodificación e integración con analítica), antes de su adopción en un sistema específico.

## 16. Marco teórico

El marco teórico concentra los conceptos, categorías normativas y fundamentos técnicos que sostienen el diseño posterior del prototipo. A diferencia del Estado del arte, no funciona como un inventario exhaustivo de modelos o herramientas, sino como base conceptual para justificar qué se detecta, cómo se interpreta, bajo qué restricciones opera el sistema y qué condiciones ético-legales delimitan su uso.

### 16.1. Organización interna del marco teórico

El marco teórico se organiza a partir de los dominios conceptuales que sustentan el diseño y la evaluación de la plataforma experimental. Cada dominio responde a una pregunta central del proyecto y permite delimitar, desde una perspectiva técnica o normativa, las condiciones bajo las cuales resulta posible construir un sistema de detección open-vocabulary aplicado al monitoreo de seguridad en construcción civil.

En primer lugar, se aborda el dominio de aplicación, vinculado con la seguridad laboral en obras y con la identificación de condiciones de riesgo observables mediante análisis visual. Luego se desarrollan los fundamentos de la detección open-vocabulary, el seguimiento multiobjeto, la transmisión de video en tiempo real y las restricciones ético-legales asociadas al uso de sistemas de visión por computadora en contextos laborales. Esta organización permite que las decisiones posteriores de diseño, implementación y evaluación no aparezcan como elecciones aisladas, sino como consecuencia de un conjunto articulado de criterios técnicos, metodológicos y normativos.

La Tabla 9 resume la relación entre cada dominio del marco teórico, la pregunta que orienta su desarrollo y su contribución dentro del proyecto.

**Tabla 9**

*Correspondencia entre dominios del marco teórico, preguntas articuladoras y contribución al proyecto*

| **Dominio del marco teórico** | **Pregunta articuladora** | **Contribución al proyecto** |
| --- | --- | --- |
| Seguridad laboral y condiciones de riesgo observables | ¿Qué condiciones debe poder identificar el sistema? | Define el dominio de aplicación y traduce obligaciones preventivas en evidencias visuales detectables. |
| Detección open-vocabulary y modelos visión-lenguaje | ¿Cómo puede el sistema interpretar descripciones abiertas en lenguaje natural? | Fundamenta el uso de modelos capaces de detectar conceptos no restringidos a un vocabulario cerrado. |
| Seguimiento multiobjeto | ¿Cómo se mantiene la continuidad temporal de las detecciones? | Justifica la incorporación de mecanismos de seguimiento para reducir inestabilidad entre cuadros consecutivos y evaluar persistencia. |
| Video en tiempo real, streaming y latencia | ¿Qué restricciones impone el procesamiento continuo de video? | Delimita los componentes del pipeline, las fuentes de latencia y los criterios para operar en tiempo real. |
| Marco ético-legal y privacidad | ¿Bajo qué condiciones es legítimo aplicar visión computacional en entornos laborales? | Establece límites de uso responsable, minimización de datos, carácter asistivo y ausencia de identificación personal. |
| Convergencias y preguntas rectoras | ¿Qué brechas atraviesan los dominios y qué debe definir el protocolo experimental? | Integra restricciones, explicita límites y formula las preguntas que guían la consolidación metodológica. |

*Nota.* Cada dominio se corresponde con una sección de este capítulo; la columna «Contribución al proyecto» indica qué aporta al desarrollo posterior, no un resultado alcanzado. Fuente: elaboración propia.

El punto de partida del análisis es el dominio de aplicación. Antes de evaluar qué puede detectar el sistema, es necesario precisar qué debe detectar y por qué, definiendo así qué condiciones de riesgo son relevantes en una obra de construcción, qué las hace observables visualmente y qué obligación normativa impone su prevención. Sin esa delimitación, cualquier evaluación del desempeño técnico del sistema carecería de criterio de referencia.

### 16.2. Condiciones de riesgo observables

La viabilidad técnica de un sistema de detección visual depende, en primer lugar, de una definición precisa de su objeto: qué condiciones deben ser detectadas, bajo qué criterio se las considera riesgosas y por qué son observables mediante visión por computadora. En el contexto de la construcción civil, esa definición no es arbitraria. Emerge de un marco normativo consolidado que establece, con carácter obligatorio, cuáles son las obligaciones del empleador en materia de prevención y qué condiciones físicas en la obra constituyen incumplimiento de esas obligaciones. Las siguientes secciones sistematizan ese marco y lo traducen al plano de los observables visuales que el sistema deberá identificar.

El sector de la construcción combina tareas simultáneas, entornos cambiantes y una elevada interacción entre personas, maquinaria y estructuras temporales. En este contexto, la regulación en materia de seguridad y salud en el trabajo cumple un rol ordenatorio: define obligaciones mínimas y mecanismos de control que orientan la prevención, y establece un lenguaje común para evaluar condiciones de riesgo.

Para un proyecto que analiza video en obra y emite alertas asistivas, la normativa no debe interpretarse como una lista de verificación aislada, sino como el fundamento que permite traducir riesgos típicos (por ejemplo, trabajo en altura sin protección colectiva o sin anclaje, presencia de personas en zonas de exclusión de equipos móviles o izajes, o interacción peatón-vehículo fuera de circuitos señalizados) en criterios observables y verificables. Esta sección desarrolla el marco normativo argentino aplicable y propone una articulación conceptual entre las obligaciones legales y las evidencias susceptibles de detección automatizada.

#### 16.2.1. La normativa como fuente de condiciones de riesgo

La seguridad laboral en la industria de la construcción civil se organiza a partir de un conjunto de instrumentos normativos que prescriben obligaciones concretas para empleadores, trabajadores y empresas. Una distinción metodológica relevante separa la normativa de cumplimiento obligatorio —leyes, decretos reglamentarios y resoluciones técnicas con fuerza vinculante— de los estándares voluntarios de gestión, que no generan exigibilidad legal por sí mismos, pero aportan marcos conceptuales útiles para organizar la prevención de manera sistemática. Ambos tipos de instrumentos resultan pertinentes para este análisis, siendo la normativa obligatoria la que define qué condiciones deben cumplirse y en consecuencia qué incumplimientos constituyen riesgo, y los estándares de gestión, en cambio, ofrecen un marco para comprender cómo se monitorea y verifica ese cumplimiento en la práctica operativa.

##### 16.2.1.1. Normativa de cumplimiento obligatorio

En Argentina, el sistema normativo de higiene y seguridad laboral se estructura jerárquicamente a partir de la Ley 19.587, reglamentada con carácter general por el Decreto 351/79 y con especificidad sectorial por el Decreto 911/96 para la industria de la construcción. Este cuerpo normativo se complementa con resoluciones técnicas emitidas por la Superintendencia de Riesgos del Trabajo, que operacionalizan los mecanismos de control y coordinación preventiva.

##### 16.2.1.2. Ley 19.587 y el principio de prevención

La Ley 19.587 de Higiene y Seguridad en el Trabajo establece el marco general aplicable a todo el territorio nacional y fija como eje conceptual el principio de prevención: las condiciones laborales deben ajustarse a normas técnicas destinadas a prevenir daños a la salud y a la integridad de las personas (Ley 19.587, 1972). Su alcance no se limita a un sector específico, sino que delimita obligaciones generales vinculadas al ambiente de trabajo, las instalaciones, los procesos productivos y la organización preventiva.

La contribución conceptual de esta ley para el presente análisis reside en instalar el deber de anticipación como componente central de la gestión de seguridad. La prevención no se concibe como respuesta reactiva a incidentes, sino como identificación y control sistemático de condiciones que preceden al daño. En una obra civil, por ejemplo, donde el riesgo se reconfigura constantemente con el avance de los trabajos, este principio implica que el sistema de monitoreo debe orientarse a detectar condiciones de riesgo antes de que se materialicen en accidentes, y no únicamente a registrar eventos ya ocurridos.

##### 16.2.1.3. Decreto 351/79: reglamentación general

El Decreto 351/79 aprueba la reglamentación de la Ley 19.587 y desarrolla un conjunto de exigencias técnicas que permiten trasladar el deber general de prevención a requisitos operativos verificables (Decreto 351/79, 1979). Organiza aspectos como condiciones edilicias, instalaciones, señalización, iluminación, ventilación, protecciones de máquinas, orden y limpieza, y la estructuración de servicios especializados en higiene y seguridad.

El aporte conceptual de este decreto para el análisis es la noción de condición controlable, ya que muchos riesgos se expresan como estados observables del entorno —ausencia de resguardos, obstrucciones en vías de circulación, falta de señalización, desorden en zonas de trabajo—, lo que habilita estrategias de verificación sistemática basadas en la observación del espacio físico. El decreto consolida la idea de que la seguridad puede monitorearse a partir de indicadores verificables en el lugar de trabajo, idea que resulta directamente relevante para un sistema de monitoreo visual.

##### 16.2.1.4. Decreto 911/96: reglamento específico de construcción

El Decreto 911/96 aprueba el Reglamento de Higiene y Seguridad específico para la industria de la construcción, atendiendo a particularidades que distinguen a este sector de otros entornos laborales, definiendo cuestiones del contexto de la obra como establecimiento temporal con geometría cambiante, la coexistencia simultánea de múltiples contratistas y subcontratistas, la presencia de estructuras provisorias en permanente transformación, y la exposición a riesgos que varían día a día con el avance de los trabajos (Decreto 911/96, 1996).

Este reglamento aborda de manera específica los riesgos más frecuentes y graves de la actividad: trabajos en altura con andamios y plataformas, excavaciones, instalaciones eléctricas provisorias, movimiento de materiales y operación de equipos pesados. Su contribución conceptual es doble. Por un lado, explicita que el riesgo en construcción no depende únicamente del comportamiento individual del trabajador, sino también del diseño del entorno físico —protecciones colectivas, delimitación de áreas, condiciones de acceso y circulación—. Por otro lado, vincula la seguridad a la gestión integral de la obra como sistema, donde la coordinación entre empleadores concurrentes y la planificación preventiva son tan relevantes como las medidas individuales de protección.

##### 16.2.1.5. Resoluciones SRT: programas y coordinación preventiva

La Resolución SRT 51/97 y la Resolución SRT 35/98 completan el marco normativo estableciendo la dimensión organizacional de la prevención. La primera fija la obligación de comunicar el inicio de obra y de elaborar programas de seguridad específicos para cada proyecto, con intervención verificadora de las ART mediante visitas sistemáticas (SRT, 1997). La segunda regula los casos de concurrencia de múltiples empleadores imponiendo la coordinación de esos programas y su verificación conjunta (SRT, 1998).

En el ámbito de la construcción, el cumplimiento normativo se articula con instrumentos operativos impulsados por la Superintendencia de Riesgos del Trabajo (SRT) y por las Aseguradoras de Riesgos del Trabajo (ART). De forma complementaria, el Programa de Construcción difundido por la SRT explicita como objetivo el establecimiento de mecanismos de adopción de medidas preventivas, correctivas y de control, incluyendo la verificación de avisos de obra y la coordinación de programas (SRT, s. f.).

Estas resoluciones refuerzan la concepción de la prevención como proceso continuo y organizado, no como conjunto de medidas puntuales. En este contexto, su relevancia conceptual reside en que sitúan la detección de condiciones de riesgo en un marco institucional más amplio, dado que las alertas generadas por un sistema de monitoreo asistivo no son decisiones autónomas, sino insumos para los mecanismos de supervisión humana y gestión preventiva previstos por la normativa vigente.

##### 16.2.1.6. Estándares voluntarios de gestión

Los estándares internacionales de gestión constituyen herramientas complementarias al marco legal. Si bien su adopción no es obligatoria, proporcionan estructuras sistemáticas para organizar la prevención de riesgos en torno a procesos definidos, responsabilidades asignadas y ciclos de mejora continua. En proyectos que integran tecnología al monitoreo de seguridad, estos estándares ofrecen un marco conceptual para situar las herramientas dentro de un sistema de gestión más amplio.

##### 16.2.1.7. ISO 45001 y sistemas de gestión de SST

La norma ISO 45001:2018 constituye el estándar internacional de referencia para sistemas de gestión de seguridad y salud en el trabajo. Si bien su adopción no es obligatoria bajo la normativa argentina, su marco conceptual resulta relevante para comprender cómo se organiza la prevención como sistema gestionable y auditable (ISO, 2018). El estándar integra identificación de peligros, evaluación de riesgos, control operacional, preparación ante emergencias y revisión del desempeño mediante auditorías y acciones correctivas, todo ello estructurado en el ciclo Planificar-Hacer-Verificar-Actuar (PDCA).

Su valor para el presente análisis reside en que convierte el cumplimiento normativo en una práctica gestionable y verificable: la organización no solo debe cumplir las obligaciones legales, sino demostrar que identifica peligros, implementa controles, verifica resultados y mejora sistemáticamente. Esta perspectiva permite ubicar un sistema de monitoreo asistivo como componente de un sistema de gestión más amplio, evitando interpretarlo como sustituto de la supervisión humana o del control institucional. Las alertas generadas por el sistema son insumos para ese ciclo de gestión, no reemplazos de ninguna de sus etapas.

#### 16.2.2. Operacionalización: prescripción normativa y observable visual

El propósito de las secciones anteriores fue establecer el marco legal y conceptual que define qué condiciones deben cumplirse en una obra civil. Sin embargo, para que este marco resulte operativo en un sistema de monitoreo visual, es necesario traducir las obligaciones normativas a condiciones físicamente observables que puedan ser identificadas en imágenes o video. Este proceso constituye lo que en metodología de investigación se denomina operacionalización, es decir, el proceso de traducción de un concepto abstracto o normativo en indicadores concretos y verificables (Decreto 351/79, 1979; Decreto 911/96, 1996).

La operacionalización aplicada en este capítulo parte de las obligaciones tipificadas en el marco normativo y las transforma en evidencias visuales que manifiestan, de manera observable, el cumplimiento o incumplimiento de cada obligación. Una prescripción como “el empleador debe proveer elementos de protección personal adecuados” (Ley 19.587, 1972) se traduce, por ejemplo, en la evidencia observable “presencia de casco en la región cefálica del trabajador”. Esta traducción no implica equiparar la observación visual con la certificación del cumplimiento normativo —una cuestión que requiere evaluación técnica en terreno y decisión humana—, sino construir un conjunto de señales de atención alineadas con categorías regulatorias reconocidas, que un sistema asistivo puede detectar y reportar para su posterior evaluación por los responsables.

Es importante señalar que esta operacionalización tiene limitaciones inherentes. La visión por computadora captura información visual bidimensional proyectada desde ángulos específicos, lo que puede generar ambigüedades de interpretación. Por ejemplo, un casco que en realidad está siendo transportado en la mano puede proyectarse de manera similar a uno que está siendo usado correctamente desde ciertos ángulos de cámara. Estas ambigüedades no invalidan el valor asistivo del sistema, pero refuerzan la necesidad de que las alertas generadas sean interpretadas por supervisores humanos con capacidad de contextualización, y no como determinaciones definitivas de cumplimiento o incumplimiento normativo.

##### 16.2.2.1. Taxonomía de categorías de riesgo

Para que la operacionalización sea sistemática y trazable al marco normativo, es necesario organizar el análisis en categorías de riesgo que agrupen obligaciones de naturaleza similar. En la construcción civil, las categorías de riesgo más relevantes para este proyecto son aquellas que combinan tres condiciones: presencia normativa, criticidad preventiva y posibilidad de observación visual.

Bajo ese criterio, se consideran principalmente las siguientes categorías: incumplimiento en el uso de equipos de protección personal (EPP), condiciones inseguras en trabajos en altura, acceso no autorizado o desprotegido a zonas restringidas, coexistencia riesgosa entre peatones y maquinaria, y condiciones inadecuadas del entorno físico de trabajo, como desorden, obstrucciones, instalaciones provisorias o ausencia de señalización.

Esta taxonomía no pretende agotar el universo de riesgos en obra. Su función es construir un puente entre obligaciones legales y evidencias verificables en video, de modo que las condiciones priorizadas puedan justificarse tanto desde el marco normativo como desde su factibilidad técnica de detección visual.

##### 16.2.2.2. Matriz de evidencias visuales

La Tabla 10 presenta la operacionalización del marco normativo en términos de evidencias visuales y condiciones detectables en video. Cada fila articula una obligación normativa tipificada, la evidencia física que la materializa, y la condición de riesgo observable que correspondería a su incumplimiento o ausencia. Esta tabla constituye el artefacto analítico central de este capítulo y funciona como insumo conceptual para las etapas posteriores del proyecto en las que se definirán los patrones de consulta del sistema.

**Tabla 10**

*Correspondencia entre obligaciones normativas, evidencias visuales y condiciones de riesgo detectables en video*

| **Categoría de riesgo** | **Prescripción normativa** | **Evidencia operativa / visual** | **Condición detectable en video** |
| --- | --- | --- | --- |
| Uso de EPP — casco | Ley 19.587, arts. 8-9; Dec. 911/96, arts. 98-115 | Casco de seguridad en región cefálica | Persona sin casco; persona en borde elevado sin protección cefálica visible |
| Uso de EPP — chaleco reflectivo | Ley 19.587, arts. 8-9; Dec. 911/96, arts. 98-115 | Chaleco de alta visibilidad en torso | Persona sin chaleco reflectivo en zona de tráfico o maquinaria |
| Uso de EPP — calzado de seguridad | Ley 19.587, arts. 8-9; Dec. 911/96, arts. 98-115 | Calzado con puntera reforzada o bota de seguridad | Persona con calzado inadecuado visible en zonas de riesgo de aplastamiento |
| Protección contra caídas en altura | Ley 19.587, arts. 8-9; Dec. 911/96, arts. 52-57, 98-115 | Arnés con línea de vida; barandas, redes y protecciones perimetrales | Trabajo en altura sin sistema anticaídas visible; borde desprotegido con personas próximas |
| Delimitación de áreas de riesgo | Dec. 351/79, cap. 12; Dec. 911/96, arts. 47, 61-62, 66-69 | Cintas, vallados, cartelería, zonas restringidas demarcadas | Persona dentro de zona restringida; cruce peligroso peatón-maquinaria; ausencia de segregación visible |
| Control de circulación y coexistencia con maquinaria | Dec. 911/96, arts. 47, 70-71 | Rutas separadas, balizamiento, señalero presente | Maquinaria circulando cerca de peatones; ausencia de separación; maniobras en zonas congestionadas |
| Orden, limpieza y gestión de obstáculos | Dec. 351/79, cap. 5; Dec. 911/96, arts. 46-47 | Superficies libres; materiales apilados; escombros contenidos | Pasillos obstruidos; materiales inestables; riesgo de tropiezo por desorden visible |
| Instalaciones eléctricas provisorias | Dec. 911/96, arts. 74-87 | Tableros protegidos; cables con doble aislación; disyuntores | Cableado expuesto en zonas de tránsito; conexiones improvisadas visibles |

*Nota.* La columna “Condición detectable en video” describe situaciones susceptibles de ser identificadas por análisis visual, no determinaciones de cumplimiento normativo. La tabla no constituye selección de prompts ni especificación de sistema; es un artefacto analítico conceptual cuya elaboración es independiente de la tecnología de detección que se adopte en etapas posteriores. Fuente: Elaboración propia basada en las fuentes citadas (Decreto 351/79, 1979; Decreto 911/96, 1996; Ley 19.587, 1972).

Para que las evidencias visuales sistematizadas en la tabla precedente resulten operativas en el contexto del sistema propuesto, es necesario establecer criterios de evaluabilidad que permitan valorar su detección de manera objetiva y reproducible. En este sentido, cada condición observable debe poder vincularse a métricas de desempeño del modelo —tales como precisión, exhaustividad (recall) y tasa de falsos positivos— así como a indicadores de rendimiento en tiempo real, entre los que se incluyen la latencia de inferencia y la tasa de cuadros procesados por segundo. Esta formalización permite no solo validar el comportamiento del sistema en escenarios controlados, sino también comparar configuraciones y arquitecturas de detección alternativas, asegurando coherencia con el marco de evaluación que se define en el protocolo experimental. Cabe señalar que los umbrales específicos y las expresiones formales de estos criterios constituyen decisiones de implementación que se abordarán en etapas posteriores del trabajo.

#### 16.2.3. Integración con sistemas de monitoreo asistivo

De las secciones anteriores, es posible apreciar que el marco normativo de la construcción civil genera un conjunto definido y justificado de condiciones de riesgo que son, en principio, observables en el espacio físico de la obra. Esta observabilidad no es un hallazgo trivial, sino que implica la existencia de una correspondencia estructural entre las obligaciones legales y las señales visuales que un sistema de monitoreo puede capturar, lo que fundamenta la viabilidad conceptual del proyecto como herramienta de apoyo a la prevención.

Sin embargo, esta correspondencia tiene límites que deben quedar explícitos. En primer lugar, no todas las obligaciones normativas tienen correlatos visuales directos. Por ejemplo, prescripciones como la correcta certificación de los EPP según norma IRAM, el ajuste técnico de un arnés o la altura reglamentaria de una baranda son condiciones que, aun manifestándose en el espacio físico, no pueden determinarse con certeza a partir de la imagen. El sistema puede señalar la presencia o ausencia de un elemento, pero no verificar su conformidad técnica. En segundo lugar, la observabilidad visual de una condición no garantiza que el sistema la detecte con precisión en todas las circunstancias, ya que elementos como la iluminación, los ángulos de cámara y las oclusiones introducen variabilidad que el análisis conceptual no puede anticipar completamente.

La integración de estas condiciones en un sistema de este tipo tiene coherencia con el enfoque de la normativa vigente, que concibe la prevención como un proceso continuo de verificación y corrección (ISO, 2018; SRT, 1997, 1998). Un sistema que detecta señales de riesgo a modo de asistencia puede contribuir a sostener la continuidad del control en entornos con múltiples frentes de trabajo simultáneos, complementando la capacidad de observación de los supervisores humanos sin desplazar sus responsabilidades legales ni sustituir los mecanismos institucionales de fiscalización.

Esta lectura es coherente con el enfoque de las resoluciones de la SRT relativas a programas de seguridad, coordinación entre empleadores y verificación en obra, que conciben la prevención como un proceso continuo y organizado (SRT, 1997, 1998). La tecnología no sustituye la evaluación técnica en terreno ni el rol de las ART o de los responsables de seguridad, sino que puede integrarse como un soporte instrumental para fortalecer la detección, la trazabilidad y la respuesta ante condiciones de riesgo observables.

### 16.3. Percepción visión-lenguaje: fundamentos conceptuales de la detección open-vocabulary

Como se mencionó anteriormente, la detección de objetos en imágenes ha sido históricamente un problema de clasificación cerrada, donde los sistemas reconocen únicamente las categorías para las que fueron entrenados. Este supuesto es incompatible con el dominio de seguridad laboral, donde las condiciones de riesgo son heterogéneas, cambian según la etapa de la obra y pueden formularse con precisión en lenguaje natural pero difícilmente acotarse en un conjunto fijo de clases predefinidas. El paradigma de detección de vocabulario abierto (OVD) rompe esa restricción al incorporar un encoder de lenguaje que permite guiar la detección mediante descripciones textuales arbitrarias.

La presente sección caracteriza los fundamentos conceptuales de la detección open-vocabulary, con énfasis en la transición desde los enfoques de vocabulario cerrado hacia modelos capaces de vincular información visual y lenguaje natural. En particular, se desarrollan los principios de alineación visión-lenguaje, el rol del prompt como mecanismo de especificación dinámica y las condiciones que hacen posible formular consultas abiertas sobre escenas visuales.

#### 16.3.1. Del closed-set al open-vocabulary

En la detección de objetos tradicional, el modelo aprende a localizar instancias en una imagen y a clasificarlas dentro de un vocabulario fijo, establecido de antemano y sin posibilidad de expansión en tiempo de inferencia. Esta formulación permite optimizar el rendimiento sobre benchmarks bien delimitados, como MS COCO con 80 categorías (Lin et al., 2014) o PASCAL VOC (Everingham et al., 2010), pero introduce una dependencia estructural entre el dominio de entrenamiento y el dominio de aplicación, siendo que el sistema solo puede detectar lo que fue explícitamente contemplado en el diseño.

La detección open-vocabulary supera esta restricción al separar el espacio semántico del conjunto de categorías de entrenamiento. En lugar de aprender representaciones para clases discretas y fijas, los modelos OVD aprenden a alinear regiones visuales con descripciones lingüísticas en un espacio de embeddings compartido. La noción de clase deja de ser un identificador discreto y pasa a representarse como una entidad semántica continua, definida dinámicamente por el contenido de la consulta (Zareian et al., 2021). En consecuencia, una categoría expresada en lenguaje natural durante la inferencia puede ser reconocida aunque el modelo nunca la haya visto etiquetada durante el entrenamiento, siempre que su representación semántica sea coherente con el espacio aprendido.

Esta capacidad no es absoluta. La calidad de la generalización zero-shot —ampliada en la sección 16.3.5— depende de la calidad y amplitud del preentrenamiento multimodal, y el desempeño sobre categorías muy específicas o visualmente inusuales puede ser significativamente inferior al observado sobre categorías cotidianas bien representadas en los datos de entrenamiento. Reconocer la potencia del paradigma OVD sin ignorar sus condiciones y límites es el propósito de las secciones que siguen.

#### 16.3.2. Mecanismos de alineación visión-lenguaje

El pilar técnico central de OVD es el uso de representaciones conjuntas de visión y lenguaje. Estas representaciones se obtienen mediante modelos multimodales entrenados para proyectar imágenes, regiones visuales y textos en un espacio latente compartido, donde la proximidad geométrica refleja afinidad semántica. El trabajo seminal en esta dirección es CLIP (Contrastive Language–Image Pre-training), que demostró la viabilidad de entrenar modelos con cientos de millones de pares imagen-texto recopilados de la web para aprender representaciones visuales altamente transferibles, alineadas con descripciones en lenguaje natural (Radford et al., 2021).

El entrenamiento contrastivo opera sobre la base de maximizar la compatibilidad entre pares imagen-texto correctos y minimizar entre pares incorrectos, produciendo un encoder visual y un encoder textual que proyectan imagen y texto a un espacio semántico compartido (Minderer et al., 2022, 2023; Radford et al., 2021). El proceso de detección resultante puede describirse en tres etapas conceptuales, donde 1) a partir de una imagen, el backbone visual genera representaciones asociadas a regiones candidatas, 2) a partir de una consulta textual (prompt), el encoder de lenguaje obtiene una representación semántica y finalmente, 3) la detección se resuelve evaluando la compatibilidad entre ambas representaciones mediante funciones de similitud, atención cruzada u otros mecanismos de alineación, aplicando non-maximum suppression sobre las regiones con mayor compatibilidad semántica. Este esquema introduce una separación conceptual entre localización espacial y reconocimiento semántico, lo que permite evaluar nuevas descripciones en tiempo de inferencia sin modificar los parámetros del modelo (Minderer et al., 2022).

#### 16.3.3. Rol del lenguaje natural como especificación dinámica

En detección open-vocabulary, el lenguaje funciona como una especificación de inferencia: la consulta textual define qué concepto debe localizarse sin modificar el clasificador ni volver a entrenar el modelo. Esta propiedad permite expresar entidades, atributos y relaciones mediante vocabulario natural, pero introduce una variable ausente en los detectores closed-set: formulaciones semánticamente cercanas no necesariamente producen representaciones equivalentes. La sensibilidad depende del encoder textual, del contexto léxico y del régimen de alineación empleado durante el preentrenamiento (Zhou et al., 2022b).

La literatura aborda este problema mediante ingeniería sistemática de prompts, prompt learning con tokens de contexto aprendibles y, en algunas arquitecturas, prompts visuales que anclan la consulta a un ejemplo (Du et al., 2022; Jiang et al., 2024; Khattak et al., 2023). Estas alternativas son modalidades de consulta documentadas, no requisitos universales. Para evaluar una condición de dominio, la formulación textual debe tratarse como parte del protocolo experimental: deben compararse variantes bajo los mismos datos, umbrales y métricas, evitando atribuir al modelo diferencias producidas únicamente por la redacción.

#### 16.3.4. Composicionalidad, negación y condiciones definidas por ausencia

El aprendizaje contrastivo aproxima representaciones globales de imágenes y textos al recompensar la compatibilidad entre pares correctos y separar pares incorrectos. Ese objetivo no obliga a codificar de manera explícita quién realiza una acción, qué atributo modifica a cada entidad ni en qué orden aparecen los términos. Esto no significa que los modelos ignoren las palabras, sino que un buen desempeño de recuperación puede coexistir con baja sensibilidad a la estructura relacional de la frase.

Yuksekgonul et al. (2023) estudian esta limitación mediante ARO, un benchmark con más de 50.000 casos organizados en atribución, relación y orden. Los resultados muestran que modelos visión-lenguaje de referencia pueden apoyarse fuertemente en el inventario léxico y resolver coincidencias globales sin representar con igual robustez los vínculos entre sustantivos, atributos y relaciones. El comportamiento se aproxima así a una bolsa de palabras: los conceptos dominantes conservan gran peso aunque se intercambien modificadores o cambie la estructura que determina el significado.

Winoground aísla la composicionalidad con pares de captions que contienen exactamente las mismas palabras en distinto orden y se asocian con dos imágenes diferentes. Los modelos evaluados no superaron de manera consistente el azar al vincular cada caption con la imagen correcta (Thrush et al., 2022). La prueba elimina la ventaja del contenido léxico compartido y muestra que la alineación global no garantiza razonamiento visio-lingüístico sobre roles y relaciones.

En detección y phrase grounding, la asociación entre tokens y regiones aporta localización más fina que la recuperación global, pero la negación mantiene una dificultad conceptual. Una frase como «persona sin casco» contiene el concepto positivo casco; sin embargo, la ausencia no constituye una región visible que pueda recibir una caja. Además, el solapamiento léxico puede hacer que el sustantivo positivo conserve influencia aun cuando el modificador cambie la condición solicitada (Liu et al., 2024). Evaluar ausencia exige definir qué región de la persona resulta pertinente, qué evidencia positiva debería encontrarse y bajo qué relación espacial se considera asociada.

Por ello, una condición definida por ausencia admite al menos dos formulaciones conceptuales: solicitar directamente al modelo que localice la infracción completa, o solicitar evidencia positiva —persona y elemento de protección— y derivar la ausencia mediante razonamiento sobre las detecciones. La primera delega composición y negación al modelo; la segunda separa percepción y relación, pero introduce reglas y posibles errores de asociación. La literatura no establece una alternativa universalmente superior. Su desempeño depende del modelo, del prompt, de la granularidad espacial y del dominio, por lo que la comparación debe permanecer como pregunta empírica. Esta limitación enlaza con la brecha de contextualización semántica de la sección 15.2.5.1 sin anticipar la estrategia que adopte el diseño.

#### 16.3.5. Generalización zero-shot y el problema del long-tail semántico

Un concepto estrechamente vinculado a la OVD es la generalización zero-shot, siendo esta la capacidad de reconocer conceptos no observados explícitamente durante el entrenamiento supervisado. Esta propiedad resulta especialmente relevante en dominios caracterizados por distribuciones de clases desbalanceadas o por una fuerte presencia de categorías poco frecuentes, denominadas en la literatura como long-tail semántico.

Los modelos OVD no eliminan por completo las limitaciones impuestas por los datos de preentrenamiento: categorías visualmente inusuales o semánticamente distantes de los conceptos mejor representados pueden exhibir un desempeño inferior al observado en categorías frecuentes. En construcción civil, esto afecta especialmente a categorías especializadas del dominio —incluidos determinados EPP y roles operativos— cuya representación en los datos generalistas puede ser limitada. Por ello, su desempeño zero-shot debe verificarse en material de dominio y no inferirse desde benchmarks generales.

La ampliación de datos y el autoentrenamiento mejoran la cobertura de categorías raras, pero no eliminan la brecha entre benchmarks generalistas y dominios especializados (Minderer et al., 2023).

#### 16.3.6. Dimensiones de comparación de modelos OVD

La literatura permite comparar modelos OVD a lo largo de dimensiones distintas: capacidad de generalización zero-shot y transferencia de dominio; expresividad frente a atributos y relaciones; latencia y dependencia del hardware; modalidad de consulta; disponibilidad de código y pesos; y posibilidades de adaptación paramétrica. Ninguna dimensión determina por sí sola la adecuación de una alternativa, y los resultados de benchmarks no son directamente transferibles entre hardware, resoluciones y regímenes de evaluación diferentes (Cheng et al., 2024; Liu et al., 2024; Minderer et al., 2022, 2023).

La retención open-vocabulary después del fine-tuning tampoco puede atribuirse a la familia arquitectónica. Como se sintetiza en la sección 15.2.4, depende de la receta concreta: qué parámetros se actualizan o congelan, si se conserva supervisión lingüística amplia y si el protocolo evalúa categorías no vistas (A. Wang et al., 2025; X. Zhao et al., 2024). Los prompts visuales, la segmentación o la ejecución híbrida entre modelos pueden describirse como capacidades presentes en parte de la literatura, pero no constituyen requisitos generales. El peso asignado a cada dimensión pertenece a la metodología y al diseño posterior, donde debe justificarse con relación al alcance experimental.

### 16.4. Persistencia temporal de entidades y fundamentos conceptuales del seguimiento multiobjeto

Una detección aislada no basta para sustentar una alerta temporal. Para distinguir entre una aparición breve y una condición que permanece, se requiere continuidad entre cuadros, una propiedad que la detección por cuadro no provee. El seguimiento multiobjeto (MOT) cumple esa función al asignar identificadores temporales internos a las entidades detectadas, estimar sus trayectorias cuadro a cuadro y sostener la continuidad ante omisiones breves. La presente sección caracteriza los fundamentos técnicos de ese mecanismo, sus métodos representativos y los compromisos relevantes para integrarlo en un sistema de monitoreo.

#### 16.4.1. La limitación temporal de la detección por cuadro

Un detector de objetos —incluyendo los modelos OVD— opera de manera fundamentalmente estática: dada una imagen, produce un conjunto de regiones detectadas con sus etiquetas semánticas y puntajes de confianza. Esta operación se realiza de manera independiente para cada cuadro del flujo de video, sin memoria ni referencia a los cuadros anteriores. En consecuencia, el mismo objeto físico presente en dos cuadros consecutivos es tratado como dos entidades sin relación; no existe ningún mecanismo que les asigne una identidad común ni que modele su trayectoria a lo largo del tiempo (Bewley et al., 2016; Luo et al., 2021).

Esta limitación tiene consecuencias operativas directas para el sistema de monitoreo. En primer lugar, la variabilidad cuadro a cuadro que caracteriza a los modelos OVD —fluctuaciones en puntajes de confianza, apariciones y desapariciones espurias e inconsistencias entre cuadros consecutivos (Xiao et al., 2024)— no puede filtrarse ni estabilizarse sin una capa que integre información temporal. En segundo lugar, muchas condiciones de riesgo no son eventos instantáneos, sino estados que deben persistir durante un intervalo mínimo para resultar operativamente significativos: una presencia sostenida en una zona restringida no equivale a una detección espuria de un único cuadro (Du et al., 2024). En tercer lugar, las alertas basadas en evidencia sostenida —y no en detecciones aisladas— pueden reducir la carga cognitiva y la fatiga de alerta asociada con falsos positivos frecuentes (Du et al., 2024).

El seguimiento multiobjeto aporta la capa de integración temporal que la detección por cuadro no ofrece: asigna identificadores temporales internos a las entidades detectadas, modela su estado y trayectoria a lo largo de la secuencia y produce trayectorias estructuradas sobre las que puede agregarse evidencia temporal (Du et al., 2024; Milan et al., 2016).

#### 16.4.2. Fundamentos del MOT y del paradigma tracking-by-detection

El seguimiento multiobjeto estima trayectorias a partir de detecciones ruidosas e incompletas. En el paradigma tracking-by-detection, un detector externo localiza objetos en cada cuadro y el tracker mantiene un estado temporal para cada trayectoria activa. Este desacoplamiento permite integrar detectores con vocabularios y arquitecturas diferentes sin reentrenar necesariamente el componente temporal, aunque conserva una dependencia inevitable: toda trayectoria se origina en las observaciones entregadas por el detector (Adžemović, 2025; Bewley et al., 2016).

El estado de una trayectoria resume información acumulada dentro de la secuencia: identificador temporal, última caja observada, antigüedad y número de cuadros sin asociación, entre otros atributos posibles. Ese identificador sólo organiza observaciones dentro del flujo; no representa identidad personal ni garantiza continuidad entre cámaras, sesiones o reinicios. Una trayectoria puede encontrarse en estado tentativo, activo o perdido según la evidencia disponible, pero la terminología concreta depende del método y no constituye un requisito universal (Milan et al., 2016).

El ciclo de seguimiento comprende tres operaciones conceptuales. La predicción estima dónde debería encontrarse una trayectoria en el cuadro siguiente; puede utilizar el último estado observado o un modelo de movimiento. La similitud cuantifica la compatibilidad entre una predicción y una detección. La intersección sobre unión (IoU) divide el área de intersección de dos cajas por el área de su unión y ofrece una señal geométrica interpretable, sin parámetros aprendidos. Su principal límite aparece cuando el desplazamiento, la oclusión o la inestabilidad de las cajas reducen la superposición aun cuando ambas observaciones correspondan a la misma entidad (Bewley et al., 2016).

La asignación convierte la matriz de similitudes en correspondencias globales. Habitualmente se formula como un problema bipartito entre trayectorias y detecciones y se resuelve con el algoritmo húngaro. Los mecanismos de gating descartan pares incompatibles antes de asignar; los umbrales controlan qué costo resulta aceptable. Las detecciones no asignadas pueden iniciar trayectorias nuevas y las trayectorias sin observación pueden conservarse durante una ventana limitada. Esta memoria tolera omisiones breves, pero incrementarla también aumenta el riesgo de reasociar una detección a la trayectoria equivocada.

La apariencia agrega embeddings de reidentificación a la evidencia geométrica y puede mejorar la reasociación durante cruces u oclusiones. A cambio, introduce cómputo, parámetros entrenados y sensibilidad al dominio visual (Wojke et al., 2017). Los métodos puramente geométricos reducen esas dependencias, pero son más frágiles cuando varias personas ocupan posiciones cercanas o desaparecen por intervalos prolongados. Ningún mecanismo recupera información que el detector nunca observó: falsos negativos, cajas inestables y detecciones espurias pueden fragmentar trayectorias o producir cambios de identificador.

Por ello, el aporte del tracker debe interpretarse como organización temporal de evidencia, no como corrección semántica automática. La evaluación del seguimiento distingue localización, asociación y continuidad; la evaluación de una alerta agrega otras decisiones —persistencia mínima, reglas de estado y tratamiento de episodios— que pertenecen al protocolo experimental. Esta separación evita trasladar métricas MOT a la plataforma completa cuando no existen anotaciones ni objetivos específicos para ese problema.

#### 16.4.3. Integración conceptual entre OVD y MOT

Un detector OVD produce cajas, etiquetas abiertas y puntajes condicionados por el prompt; un tracker opera principalmente sobre geometría, movimiento y continuidad temporal. La identidad de seguimiento es, por lo tanto, un identificador interno y efímero dentro de un flujo, no una identidad personal ni un mecanismo de reconocimiento. Esta separación permite agregar evidencia por entidad a lo largo de una secuencia sin atribuir nombre o identidad civil a la persona observada.

La integración básica encadena percepción y asociación: las detecciones de cada cuadro alimentan al tracker, que actualiza trayectorias; sobre esas trayectorias pueden agregarse puntajes, evaluar persistencia y reconocer cambios de estado. El tracker aporta continuidad, pero no resuelve por sí mismo la incertidumbre semántica. Si la etiqueta o el puntaje del detector fluctúan, el sistema necesita una regla separada de agregación temporal para decidir qué evidencia conserva y durante cuánto tiempo.

La literatura muestra que el seguimiento puede reducir la sensibilidad a detecciones aisladas y sostener evidencia durante omisiones breves, aunque su calidad continúa limitada por la estabilidad del detector y por las oclusiones (S. Li et al., 2023, 2025). Una asociación geométricamente correcta no implica que la condición semántica esté bien interpretada; de manera inversa, una detección semánticamente correcta puede asignarse a una trayectoria equivocada. Esta distinción justifica evaluar percepción y persistencia como niveles relacionados pero no equivalentes.

Los métodos sin apariencia reducen dependencias de entrenamiento, mientras que los métodos con ReID pueden mejorar la reasociación a costa de modelos y datos adicionales (Adžemović, 2025; Wojke et al., 2017). La selección del mecanismo, las ventanas de vida de las trayectorias y las reglas de estabilización pertenecen al protocolo y al diseño posterior.

### 16.5. Operación en tiempo real, transmisión y procesamiento cercano a la fuente

Un sistema de percepción puede ser preciso y, aun así, resultar operativamente inadecuado si la evidencia llega después del margen disponible para interpretarla. La latencia es una propiedad acumulativa del pipeline completo y no del modelo o del protocolo por separado. Esta sección delimita los tramos temporales relevantes, una descomposición instrumental de Glass-to-Algorithm y los patrones arquitectónicos que permiten sostener flujos continuos sin confundir transporte, inferencia, confirmación temporal y notificación.

#### 16.5.1. La latencia extremo a extremo como restricción de diseño

En sistemas de video analítico, la expresión latencia extremo a extremo sólo resulta interpretable cuando se declara el punto inicial y el punto final. Glass-to-Glass (G2G) abarca desde la captura hasta la presentación del contenido en una interfaz; Glass-to-Algorithm (G2A) termina cuando el resultado algorítmico asociado a un cuadro queda disponible (Axis Communications AB, 2015; Bachhuber et al., 2018). En una plataforma de alertas, G2A caracteriza un subtramo instrumental por cuadro: no incluye por sí solo la asociación temporal, la ventana necesaria para confirmar una condición, el registro de la alerta ni su distribución.

La percepción humana aporta una referencia, no una cota universal. Retardos alrededor de 100 ms comienzan a afectar la sensación de inmediatez en tareas interactivas, y diferencias de decenas de milisegundos pueden percibirse en tareas de manipulación directa (Card et al., 2008; Deber et al., 2015). Un sistema de supervisión puede admitir presupuestos mayores según el perfil temporal del riesgo, el tipo de intervención y el papel del operador. La magnitud admisible debe fijarse en el protocolo experimental y relacionarse con la condición evaluada.

La latencia total es acumulativa. Captura, suministro de la fuente, transformaciones, copias de memoria e inferencia aportan retardos de naturaleza diferente. Optimizar un componente no garantiza una reducción equivalente del total si otro domina la ruta crítica. Además, una tasa media compatible con tiempo real puede ocultar colas crecientes o episodios de saturación; por eso la medición debe considerar percentiles, backlog y comportamiento sostenido, no sólo el promedio.

El buffering ilustra el compromiso central. Una cola o jitter buffer absorbe variaciones y desacopla ritmos entre productor y consumidor, pero cada unidad retenida incrementa el retardo. El diseño debe presupuestar los buffers y declarar sus políticas: eliminarlos indiscriminadamente puede producir pérdidas e inestabilidad, mientras sobredimensionarlos convierte un déficit de throughput en latencia acumulada (Axis Communications AB, 2015; Gettys & Nichols, 2012).

#### 16.5.2. Descomposición instrumental de Glass-to-Algorithm

Para mantener una notación consistente con el protocolo experimental, el subtramo G2A se descompone en cuatro componentes observables:

t_G2A = t_capture + t_transport + t_preprocess + t_inference (1)

t_capture representa la adquisición o lectura del cuadro hasta su disponibilidad para el host o consumidor instrumentado. t_transport comprende el suministro efectivo de la fuente —red, stream o lectura local—, incluidos los buffers y operaciones de entrada/salida que correspondan. t_preprocess agrupa decodificación cuando aplique, conversión de formato, redimensionado, normalización y transferencias de memoria. t_inference mide la ejecución del modelo hasta producir su salida algorítmica. La separación evita introducir renderizado o notificación en una métrica que termina antes de la interfaz (Bachhuber et al., 2018; H. Wang et al., 2022).

La Tabla 11 sintetiza los cuatro componentes instrumentales y los criterios necesarios para interpretar cada uno.

**Tabla 11**

*Componentes instrumentales del subtramo Glass-to-Algorithm*

| **Componente** | **Definición operativa** | **Fuentes principales de variabilidad** | **Criterio de interpretación** |
| --- | --- | --- | --- |
| t_capture | Captura, lectura o dequeue del cuadro en el punto temporal definido por la instrumentación | Período de cuadro, exposición, ISP y buffering de la fuente | Debe declararse el origen exacto del timestamp; a 30 fps, un período de cuadro es ≈33,3 ms |
| t_transport | Entrega del cuadro desde la fuente al consumidor del pipeline, por red, stream o I/O local | Jitter, colas, pérdida, retransmisiones, buffers y ritmo de lectura | La cola y los percentiles describen mejor la estabilidad que la media aislada |
| t_preprocess | Preparación de la entrada del modelo | Decodificación, formato de píxel, resize, normalización y movimiento CPU–GPU | Debe medirse por configuración porque las copias de memoria pueden dominar en pipelines acelerados |
| t_inference | Ejecución del modelo hasta obtener detecciones o resultados equivalentes | Arquitectura, resolución, vocabulario, runtime y hardware | La literatura reporta órdenes de 10–30 ms para alternativas one-stage optimizadas y 50–150 ms para Transformers sin optimización equivalente |

*Nota.* Los rangos son referencias contextuales y no garantías. G2A no equivale a latencia de alerta: el seguimiento, el razonamiento, la ventana de persistencia y la distribución pertenecen a tramos posteriores. Fuente: elaboración propia basada en Axis Communications AB (2015), Bachhuber et al. (2018), Cheng et al. (2024), H. Wang et al. (2022) y Ren, Jiang, et al. (2024).

La captura está condicionada por el ritmo de origen. A 30 fps, el período entre cuadros es de aproximadamente 33,3 ms, aunque el punto de observación puede encontrarse después de exposición, procesamiento interno o buffers de cámara. Por ello, “captura” no debe suponerse equivalente al instante físico en que la luz alcanza el sensor: la instrumentación debe declarar si comienza en el sensor, en la recepción, en la lectura o en el dequeue de la aplicación.

El transporte es el componente más expuesto a variación externa. Propagación y procesamiento de red suelen ser relativamente estables; el encolado, el jitter y las retransmisiones dependen de la carga. En una fuente local, el término sigue existiendo como costo de lectura, demultiplexado o buffering. Lo que compromete el tiempo real no es sólo un valor medio elevado, sino una cola que crece porque el consumidor procesa por debajo del ritmo de entrada. Percentiles y ocupación de cola permiten distinguir un episodio aislado de un déficit sostenido (Gettys & Nichols, 2012; Kurose & Ross, 2021).

El preprocesamiento debe incluir todas las transformaciones efectivamente ejecutadas antes del modelo. La decodificación, la conversión de color, el redimensionado, la normalización y las transferencias CPU–GPU pueden constituir una fracción relevante, especialmente cuando se introducen copias intermedias. Agruparlas bajo un término explícito evita atribuir a la inferencia demoras que pertenecen a la preparación de datos.

La inferencia depende de arquitectura, resolución, número de consultas, runtime y hardware. Los rangos publicados para alternativas one-stage optimizadas y Transformers no optimizados son órdenes de magnitud obtenidos en configuraciones heterogéneas; no deben trasladarse como predicción. La medición por componentes permite identificar si una configuración está limitada por el modelo, por la fuente o por el movimiento de datos, y separa el costo por cuadro de la confirmación temporal de una alerta.

La instrumentación debe fijar límites observables y utilizar un dominio temporal coherente. Cuando el origen no expone el instante físico de captura —situación habitual en streams, archivos o SDK de cámara—, t_capture comienza en el punto más temprano que la aplicación puede medir y esa convención debe declararse. Los timestamps de CPU y acelerador tampoco son intercambiables sin sincronización: una operación asíncrona puede parecer concluida antes de que el dispositivo haya terminado el trabajo. Por ello, los límites de t_preprocess y t_inference deben definirse con las barreras o sincronizaciones que correspondan al runtime (H. Wang et al., 2022).

La ecuación expresa el recorrido temporal de una unidad, pero no implica que la tasa de procesamiento sea el inverso de esa latencia. En un pipeline, distintas etapas pueden solaparse: mientras un cuadro se infiere, otro puede estar siendo capturado o preparado. El throughput describe cuántas unidades se completan por unidad de tiempo; la latencia describe cuánto tarda una unidad desde su origen hasta su salida. Para localizar cuellos de botella deben medirse ambos y evitarse sumas de promedios obtenidos sobre corridas o poblaciones diferentes (Bachhuber et al., 2018; Bass et al., 2022).

Un reporte reproducible debe declarar período de calentamiento, tamaño de lote, resolución, vocabulario o número de consultas, precisión numérica, runtime, fuente de video y política de colas. Además del tamaño muestral y la tendencia central, conviene informar percentiles de latencia, cuadros descartados, ocupación máxima de cola y throughput sostenido. Estas variables permiten distinguir variación ocasional de saturación sistemática y vincular el resultado global con el componente que la produce (Gettys & Nichols, 2012).

#### 16.5.3. Separación de planos y flujo productor-consumidor

En sistemas de análisis continuo resulta útil distinguir una ruta de datos —captura, transformación e inferencia— de una ruta de control que administra configuración, eventos y coordinación. La separación deriva de patrones de planos de datos y control y permite optimizar el flujo continuo sin bloquearlo con operaciones discretas de gobierno o notificación (Kreutz et al., 2015). No prescribe una distribución física ni una tecnología particular: ambos planos pueden coexistir en un host o distribuirse cuando el diseño lo justifique.

La ruta de datos prioriza throughput sostenido, latencia acotada y un orden definido de transformaciones. La ruta de control procesa comandos, cambios de configuración y eventos a ritmos no necesariamente ligados a la tasa de cuadros. Mantener responsabilidades diferenciadas facilita aislar cuellos de botella y evita que una operación de registro o notificación bloquee la recepción del siguiente cuadro (Bass et al., 2022). Esta separación es conceptual: no convierte por sí sola al sistema en distribuido ni exige una nube.

La ruta crítica puede modelarse como una cadena productor-consumidor. Cada etapa produce unidades que la siguiente consume; cuando el productor supera sostenidamente la capacidad del consumidor, una cola sin límite convierte el déficit de throughput en latencia creciente. Las colas acotadas, la contrapresión y las políticas explícitas de descarte, muestreo o sustitución permiten mantener el sistema observable. La política adecuada depende de la semántica: conservar todas las unidades puede ser necesario para relectura reproducible, mientras que una ruta viva puede priorizar evidencia reciente para evitar procesar cuadros obsoletos.

El desacoplamiento no elimina la necesidad de medir. Deben observarse ritmo de producción, ritmo de consumo, ocupación de cola, unidades descartadas y tiempo de residencia. Un sistema que reporta FPS aceptables pero acumula backlog no opera en tiempo real; simplemente procesa con retraso.

Para eventos discretos, el patrón publish/subscribe separa productores y consumidores: el emisor publica sin conocer todos los destinos y cada suscriptor procesa los tipos de evento pertinentes. Conviene distinguir tres responsabilidades: el transporte en ejecución entrega eventos a consumidores activos; la persistencia conserva hechos para relectura o auditoría; y la distribución externa comunica una alerta. Un bus puede desacoplar componentes, pero no garantiza por sí mismo que los eventos sobrevivan a una desconexión; la durabilidad requiere un repositorio o una política de retención independiente de la mensajería en vivo (Cugola & Margara, 2012).

Las garantías de entrega también forman parte del contrato conceptual. Una entrega al menos una vez puede producir reenvíos y, por lo tanto, duplicados; una entrega como máximo una vez puede perder mensajes; y exactamente una vez exige coordinación adicional. Cuando una alerta no debe producir efectos repetidos, el evento necesita una identidad estable y el consumidor debe procesarlo de manera idempotente. MQTT QoS 1 ejemplifica la primera semántica mediante confirmación, sin convertirla en una garantía de ausencia de duplicados (OASIS, 2019). Estas propiedades fundamentan la evaluación de mensajería sin prescribir una tecnología arquitectónica concreta.

#### 16.5.4. Computación en el borde y filtrado cercano al origen

La literatura utiliza edge, fog y cloud con fronteras variables. En este trabajo, edge designa cómputo en el dispositivo, gateway inmediato o servidor próximo a la fuente; fog, una capa intermedia de agregación cercana o regional; y cloud, centros de datos centralizados (Iorga et al., 2018; Yousefpour et al., 2019). La convención permite describir tres patrones: procesamiento en el dispositivo, procesamiento en un nodo cercano y partición colaborativa entre niveles (Chen & Ran, 2019).

Acercar cómputo al origen puede reducir ida y vuelta de red, ancho de banda y exposición de video crudo, pero introduce límites de memoria, energía y temperatura (Satyanarayanan, 2017; Shi et al., 2016). La nube ofrece elasticidad y recursos centralizados, aunque depende de conectividad y amplía el recorrido del dato. Una capa fog puede agregar varias fuentes, aplicar políticas o resumir información antes de enviarla a niveles superiores. Ningún nivel es intrínsecamente superior: su conveniencia depende del tramo que se desplace y de la carga sostenida.

No toda operación cercana al sensor equivale a inferencia completa en el borde. Una cámara inteligente puede ejecutar adquisición, filtrado, selección de cuadros, conversión o preprocesamiento y enviar sólo las unidades necesarias al consumidor principal. Este reparto reduce el consumo aguas abajo sin atribuir al dispositivo capacidades de detección que no ejecuta. La distinción es importante para analizar gateways y cámaras programables sin confundir prefiltrado con despliegue integral del modelo.

En video analytics, filtrar o resumir cerca del origen disminuye tráfico y carga posterior. Ananthanarayanan et al. (2017) muestran que procesar cerca de las cámaras permite reducir ancho de banda y distribuir recursos en cargas de video a escala. En un prototipo, el mismo principio puede evaluarse de forma acotada: cuánto trabajo se ejecuta antes del host, qué evidencia se descarta y qué impacto tiene esa decisión sobre calidad y latencia.

El punto de partición debe evaluarse por latencia, throughput, privacidad, capacidad sostenida y reproducibilidad. Métricas nominales como TOPS no bastan para anticipar el comportamiento de una aplicación. Bajo carga prolongada, límites térmicos, memoria compartida y variaciones del runtime pueden degradar el ritmo; por ello, los percentiles de latencia, el uso de memoria, el throughput efectivo y los eventos de saturación resultan más informativos que un máximo instantáneo (Satyanarayanan, 2017; Shi et al., 2016). La decisión de ejecutar inferencia en el borde, en un host cercano o en infraestructura remota debe mantenerse separada de la decisión de filtrar cerca del origen.

El filtrado cercano al origen introduce, a su vez, un compromiso metodológico. Seleccionar cuadros, reducir resolución, limitar regiones o descartar unidades disminuye carga y ancho de banda, pero modifica la evidencia que recibe el detector y puede afectar la continuidad temporal. Por ello, la política de prefiltrado debe declararse junto con la fuente y conservar parámetros suficientes para reproducirla; dos configuraciones sólo son comparables si procesan materiales y reglas de selección equivalentes.

Desplazar procesamiento hacia la fuente puede reducir la transmisión de video crudo, pero no elimina por sí mismo el tratamiento de datos personales. Metadatos temporales, zonas, trayectorias y recortes pueden mantener capacidad de identificación indirecta, por lo que la minimización debe evaluarse sobre el conjunto de datos producido y no únicamente sobre la ubicación física del cómputo (European Data Protection Board, 2020).

#### 16.5.5. Brecha de evaluación integrada

La literatura caracteriza por separado protocolos, códecs, hardware y modelos de inferencia, pero no ofrece un marco universal para presupuestar la latencia extremo a extremo de un pipeline que integra detección open-vocabulary. Los resultados aislados sólo funcionan como referencias externas; la adecuación debe verificarse mediante instrumentación del sistema completo y una definición explícita del tramo medido. Esta brecha se corresponde con la identificada en la sección 15.4.3.1 y fundamenta la necesidad de un protocolo reproducible sin anticipar la selección del stack.

### 16.6. Marco ético-legal para el análisis automatizado de video en entornos laborales

#### 16.6.1. Encuadre ético-legal y carácter asistivo

El análisis automatizado de video en el trabajo involucra una asimetría entre quienes controlan el sistema y las personas captadas. El propósito preventivo no basta para legitimar el tratamiento: deben delimitarse finalidad, proporcionalidad, seguridad, transparencia, supervisión humana y responsabilidades sobre el ciclo de vida de los datos (Organisation for Economic Co-operation and Development, 2019; UNESCO, 2021). Esta sección caracteriza el régimen aplicable y las restricciones que impone al diseño, sin convertir observaciones visuales en determinaciones normativas ni habilitar identificación personal.

#### 16.6.2. Delimitación del tratamiento de datos en sistemas de visión por computadora

Los sistemas de visión por computadora aplicados a entornos laborales suelen apoyarse en flujos continuos de imágenes para identificar objetos, personas y condiciones de trabajo. Desde una perspectiva jurídico-técnica, este tipo de información no se agota en su dimensión “visual”: en muchos escenarios, una imagen constituye un dato personal en la medida en que permite identificar, directa o indirectamente, a una persona o hacerla identificable a partir de asociaciones razonables con otros datos disponibles (Agencia de Acceso a la Información Pública, s. f.-a; Argentina, 2000). En consecuencia, aun cuando el objetivo operativo del sistema sea la prevención de riesgos, la captación y el análisis de video pueden configurar un tratamiento de datos personales sujeto a obligaciones específicas.

En un caso de uso típico de obra —videovigilancia con analítica basada en IA— el tratamiento involucra, como mínimo, (i) la recolección (captura por cámaras), (ii) el almacenamiento o transmisión del flujo, (iii) el análisis automatizado (inferencia) y (iv) la generación de salidas (alertas, registros, reportes). Cada una de estas etapas puede incrementar o reducir el impacto sobre la privacidad, según se adopten medidas de minimización, segmentación funcional y control de acceso. Este encuadre es relevante porque la protección de datos personales se estructura en torno a la finalidad y a la proporcionalidad del tratamiento: no basta con que el objetivo sea legítimo, sino que el diseño del sistema debe evitar captaciones y usos innecesarios o excesivos para el fin perseguido (Argentina, 2000; European Data Protection Board, 2020).

En el plano organizacional, el régimen de protección de datos distingue roles con responsabilidades diferenciadas. Quien determina los fines y medios del tratamiento asume el carácter de responsable del banco de datos, mientras que terceros que procesan información por cuenta del responsable actúan como encargados o prestadores de servicios. Esta distinción resulta central en soluciones tecnológicas que integran proveedores de infraestructura, plataformas de análisis o servicios en la nube, ya que exige definir obligaciones contractuales, medidas de seguridad y límites de uso coherentes con la finalidad declarada (Argentina, 2000, 2001).

##### 16.6.2.1. Régimen argentino de protección de datos aplicable a imágenes y videovigilancia

En Argentina, el tratamiento de datos personales se rige por la Ley 25.326 de Protección de los Datos Personales y su reglamentación mediante el Decreto 1558/2001 (Argentina, 2000, 2001). El marco establece que los datos deben ser recolectados para fines determinados, explícitos y legítimos, y que su tratamiento no puede desviarse de esos fines. Los principios de calidad y proporcionalidad imponen que la información sea adecuada, pertinente y no excesiva en relación con la finalidad declarada (Argentina, 2000).

La Ley 25.326 define como dato personal toda información referida a personas determinadas o determinables (Argentina, 2000). Esta definición tiene implicaciones operativas directas: una imagen puede identificar a una persona de manera directa por sus rasgos físicos, o de manera indirecta por la combinación con metadatos como hora, zona de obra, turno de trabajo o secuencia de posiciones. De allí que, aun cuando el sistema excluya explícitamente el reconocimiento facial, el análisis de impacto sobre la privacidad no puede limitarse a las salidas directas del modelo: debe considerar la identificabilidad global que emerge del ecosistema de datos que el sistema genera y almacena (Agencia de Acceso a la Información Pública, s. f.-a; Argentina, 2000).

El régimen también garantiza derechos de los titulares —como acceso, rectificación, actualización y supresión— y prevé la vía constitucional del habeas data para proteger la intimidad y controlar el uso de la información personal. Estas garantías son relevantes en escenarios de videovigilancia, donde el titular puede desconocer el alcance de la captación, la duración de conservación o los destinatarios de la información. Por ello, la transparencia y la trazabilidad del tratamiento se vuelven condiciones prácticas para que los derechos no queden meramente formales (Agencia de Acceso a la Información Pública, s. f.-a; Argentina, 2000).

##### 16.6.2.2. Disposición 10/2015

La Disposición 10/2015 de la Dirección Nacional de Protección de Datos Personales —hoy bajo la órbita de la Agencia de Acceso a la Información Pública (AAIP)— constituye el principal instrumento reglamentario específico para sistemas de videovigilancia en Argentina. Su función es operacionalizar los principios generales de la Ley 25.326 en el contexto de la captación sistemática de imágenes, traduciendo los principios de licitud, finalidad, proporcionalidad, transparencia y seguridad en criterios prácticos de diseño e implementación (Argentina, 2015).

Las condiciones de licitud más relevantes que establece la Disposición 10/2015 se organizan en tres ejes. El primero es el requisito de información previa al titular del dato, que puede cumplirse mediante cartelería visible que informe la existencia de dispositivos de captación, la finalidad del tratamiento y los datos de contacto del responsable para el ejercicio de derechos (Argentina, 2015). El segundo es la exigencia de contar con un manual o política de tratamiento de datos personales que defina finalidades, responsables, procedimientos de gestión, mecanismos de seguridad, criterios de conservación y pautas de acceso y divulgación (Argentina, 2015); este manual opera como el instrumento que vincula el diseño técnico del sistema con el cumplimiento normativo. El tercero es la obligación de inscribir las bases de datos de videovigilancia ante la AAIP, acompañando la solicitud con el manual de tratamiento (Agencia de Acceso a la Información Pública, s. f.-b).

[[PENDIENTE: definir con el equipo la aplicabilidad de esta inscripción al contexto experimental y documentar el recaudo adoptado en §17.1 y §17.4.]]

Este requerimiento no se reduce a una formalidad administrativa: contribuye a que la videovigilancia sea gestionada como un tratamiento regulado, con trazabilidad, y no como un recurso técnico difuso susceptible de ampliarse por inercia a nuevos fines.

#### 16.6.3. Medidas de seguridad y protección de la información

Una vez establecidos los requisitos de licitud, transparencia y delimitación de finalidades en el tratamiento de imágenes, adquiere centralidad el plano de la protección efectiva de la información. En los sistemas de videovigilancia —y, en particular, en aquellos que incorporan procesamiento automatizado—, el cumplimiento normativo no se agota en la legitimidad de la captación, sino que exige la adopción de medidas técnicas y organizativas orientadas a prevenir accesos indebidos, usos no autorizados y pérdidas de información. La seguridad de los datos visuales se convierte así en un componente estructural del tratamiento, en tanto condiciona la posibilidad real de garantizar la confidencialidad, la integridad y la disponibilidad de la información, y de sostener en la práctica los principios de protección de datos personales frente a riesgos operativos y de privacidad.

La Disposición 11/2006 establece medidas de seguridad aplicables a archivos y bases de datos de carácter privado, orientadas a preservar la confidencialidad, integridad y disponibilidad de la información (Argentina, 2006). Si bien no prescribe una arquitectura tecnológica específica, fija un estándar de diligencia: el responsable debe adoptar controles proporcionales a la naturaleza de los datos y a los riesgos del tratamiento.

En el contexto de un sistema de análisis de video con inferencia por IA, este estándar se traduce en cuatro dimensiones de control: gestión de accesos bajo el principio de mínimo privilegio, registros de auditoría que permitan reconstruir quién accedió a qué información y cuándo, cifrado en tránsito para los flujos de video y las alertas generadas, y segregación de entornos que impida el acceso lateral desde componentes no críticos hacia el repositorio de video o el historial de alertas (Argentina, 2000, 2006). En sistemas con componente de IA, estos controles deben complementarse con mecanismos de trazabilidad del modelo: versiones, configuraciones de prompts, umbrales de decisión y criterios de actualización deben estar documentados para permitir la auditoría del comportamiento del sistema ante resultados inesperados (ISO, 2023).

La seguridad también se vincula con la temporalidad del tratamiento. En contextos preventivos, la conservación indefinida de video suele resultar difícil de justificar bajo parámetros de proporcionalidad. Por ello, los criterios de retención, borrado seguro y gestión de copias se integran naturalmente a la estrategia de minimización: conservar lo estrictamente necesario para el fin de seguridad y por el tiempo necesario para cumplirlo, evitando acumulaciones que aumenten el impacto ante incidentes o accesos indebidos (European Data Protection Board, 2020).

#### 16.6.4. Referentes comparados y distinción respecto de la biometría

Los marcos comparados sobre videovigilancia refuerzan los principios de finalidad, minimización, transparencia y retención limitada. Las Directrices 3/2019 del EDPB distinguen la captación de video del tratamiento biométrico: una imagen puede ser dato personal sin que exista reconocimiento facial, y el tratamiento se vuelve biométrico cuando se procesan rasgos con la finalidad de identificar de manera unívoca (European Data Protection Board, 2020). Esta distinción fundamenta separar analítica orientada a condiciones observables de mecanismos de identificación personal.

#### 16.6.5. Gobernanza de IA y carácter asistivo

Los principios de gobernanza de IA agregan obligaciones de supervisión humana, trazabilidad, rendición de cuentas y comunicación comprensible de limitaciones. En un sistema asistivo, la salida algorítmica funciona como señal para revisión humana y no como decisión autónoma sobre una persona. El versionado de modelos y configuraciones, la documentación de errores y la posibilidad de reconstruir el comportamiento del sistema son condiciones de auditabilidad, no garantías de corrección (ISO, 2023; Organisation for Economic Co-operation and Development, 2019; UNESCO, 2021).

#### 16.6.6. Implicaciones para el diseño responsable del sistema

El marco normativo y ético opera como condición de contorno sobre la arquitectura y los procedimientos. La Tabla 12 organiza los principios aplicables y los expresa como restricciones que deben considerarse; no afirma que todos los controles se encuentren implementados en el prototipo.

**Tabla 12**

*Principios normativos y éticos y restricciones aplicables al diseño de sistemas de análisis automatizado de video*

| **Principio normativo / ético** | **Fuente** | **Aplicación** | **Restricción que impone al diseño** |
| --- | --- | --- | --- |
| Licitud y finalidad determinada | Ley 25.326 (Argentina, 2000); Disposición 10/2015 (Argentina, 2015) | El tratamiento de imágenes debe limitarse a la detección de condiciones de riesgo laboral y no desviarse hacia control de desempeño, disciplina o vigilancia generalizada | Excluir mecanismos orientados a la identificación individual y documentar la finalidad de cada tratamiento |
| Proporcionalidad y minimización | Ley 25.326 (Argentina, 2000); Directrices 3/2019 (European Data Protection Board, 2020) | La captación y el procesamiento deben limitarse a lo necesario para el fin preventivo | Reducir datos, metadatos y evidencias visuales; no incorporar reconocimiento facial o biométrico |
| Transparencia e información al titular | Ley 25.326 (Argentina, 2000); Disposición 10/2015 (Argentina, 2015) | Las personas captadas deben conocer la existencia, finalidad y responsable del tratamiento | Prever información accesible, señalización y un canal para ejercer derechos |
| Seguridad de la información | Disposición 11/2006 (Argentina, 2006); Ley 25.326 (Argentina, 2000) | Los controles técnicos deben ser proporcionales al riesgo | Aplicar control de acceso, protección en tránsito, segregación de entornos y registro de accesos cuando correspondan |
| Supervisión humana | UNESCO (2021); OECD (Organisation for Economic Co-operation and Development, 2019) | Las alertas son insumos y no determinaciones definitivas | Mantener revisión humana antes de cualquier intervención y evitar acciones autónomas sobre personas |
| Rendición de cuentas y trazabilidad | ISO/IEC 42001:2023 (ISO, 2023); OECD (Organisation for Economic Co-operation and Development, 2019) | El comportamiento del sistema debe ser documentable y revisable | Conservar versiones, configuraciones, métricas y registros suficientes para reconstruir decisiones técnicas |
| Temporalidad y retención mínima | Directrices 3/2019 (European Data Protection Board, 2020); Ley 25.326 (Argentina, 2000) | La conservación debe limitarse al tiempo necesario | Definir retención y borrado seguro conforme a finalidad, proporcionalidad y contexto del tratamiento |

*Nota.* Las normas argentinas citadas tienen carácter obligatorio; los marcos internacionales aportan buenas prácticas de gobernanza. La tabla expresa restricciones, no un inventario de controles implementados. Fuente: elaboración propia basada en Argentina (2000, 2006, 2015), European Data Protection Board (2020), ISO (2023), Organisation for Economic Co-operation and Development (2019) y UNESCO (2021).

#### 16.6.7. Brechas identificadas y tensiones no resueltas

El derecho argentino regula datos personales y videovigilancia, pero no desarrolla de manera específica la analítica visual basada en IA en entornos laborales. Los marcos de gobernanza amplían la discusión hacia supervisión y rendición de cuentas, sin reemplazar las obligaciones legales vigentes (ISO, 2023; Organisation for Economic Co-operation and Development, 2019; UNESCO, 2021).

Persisten tres tensiones principales. Primero, una persona puede resultar indirectamente identificable mediante la combinación de imágenes, tiempo, zona y trayectoria aun sin reconocimiento facial (Agencia de Acceso a la Información Pública, s. f.-a; Argentina, 2000). Segundo, la utilidad de conservar evidencias para analizar riesgos entra en tensión con la minimización y la retención limitada (Argentina, 2000; European Data Protection Board, 2020). Tercero, no existen criterios operativos estandarizados para comunicar la incertidumbre de las alertas a operadores no especializados, por lo que la transparencia debe incluir límites y posibilidad de error.

A estas tensiones se agrega la ausencia de pautas sectoriales específicas para sistemas de IA que analizan video en relaciones laborales. La frontera entre asistencia preventiva y vigilancia de las personas no depende sólo de la capacidad técnica, sino de la finalidad declarada, la información brindada, la posibilidad de revisión humana y la prohibición de convertir una alerta probabilística en una determinación automática sobre un trabajador. La gobernanza debe contemplar además mecanismos para impugnar resultados, documentar límites y revisar usos secundarios que puedan emerger durante la operación (Organisation for Economic Co-operation and Development, 2019; UNESCO, 2021).

### 16.7. Convergencias, brecha transversal y preguntas rectoras

#### 16.7.1. Interdependencia de los dominios

La viabilidad no depende de un detector aislado. La calidad de la percepción condiciona la asociación temporal; la fuente y el transporte delimitan el presupuesto disponible para el cómputo; y el tratamiento de imágenes impone restricciones sobre qué se conserva y cómo se comunica. Por ello, las métricas parciales deben interpretarse dentro de la cadena completa y bajo las condiciones del dominio. Esta interdependencia no determina una arquitectura concreta, pero explica por qué precisión, latencia, persistencia y trazabilidad no pueden evaluarse como problemas independientes (Bass et al., 2022; Cugola & Margara, 2012).

#### 16.7.2. Restricción ético-normativa como brecha transversal

Las brechas técnicas de datasets, prompts, integración y métricas ya fueron sistematizadas en el estado del arte. La brecha genuinamente transversal que agrega este marco es que la legitimidad del tratamiento condiciona simultáneamente percepción, persistencia, almacenamiento y distribución. Una mejora técnica que incremente la identificabilidad o la retención puede ser incompatible con los principios de finalidad y minimización; del mismo modo, una alerta operativamente útil debe conservar revisión humana y trazabilidad. El marco ético-legal actúa así como restricción arquitectónica y procedimental, no como módulo agregado al final (Argentina, 2000, 2015; European Data Protection Board, 2020).

#### 16.7.3. Preguntas rectoras para la consolidación metodológica

El marco teórico delimita las siguientes preguntas, que requieren definición metodológica y evidencia experimental. Los códigos se conservan para mantener la trazabilidad con las secciones posteriores.

**P-E1-01. Presupuesto temporal.** ¿Qué presupuesto de latencia es admisible para el subtramo G2A y para la confirmación de una alerta, sin confundir el cómputo por cuadro con la persistencia temporal? La respuesta debe declarar el origen y el final de cada timestamp, el comportamiento por percentiles y el margen asignado a seguimiento y razonamiento.

**P-E1-02. Condiciones nucleares.** ¿Qué conjunto mínimo de condiciones de riesgo permite evaluar la factibilidad de expresar observables en lenguaje natural, estabilizar evidencia y producir alertas trazables, sin pretender cubrir el catálogo normativo completo? La selección debe distinguir complejidad semántica, evidencia disponible y perfil temporal, pero no asumir que una condición multi-entidad sea obligatoria para demostrar factibilidad.

**P-E1-03. Materiales y anotaciones.** ¿Qué datos públicos y propios ofrecen anotaciones suficientes para evaluar percepción, continuidad temporal y episodios, y cuáles son además aptos para adaptación paramétrica? La respuesta debe separar material de entrenamiento, validación y prueba y evitar reutilizaciones que comprometan la independencia del protocolo.

**P-E1-04. Restricciones de ejecución.** ¿Qué hardware, fuentes de video, resolución, runtime y presupuesto de procesamiento condicionan las configuraciones comparables? La caracterización debe incluir memoria, ritmo efectivo, latencia sostenida y límites de los entornos de inferencia y entrenamiento, que no necesariamente coinciden.

**P-E1-06. Framework de métricas.** ¿Qué métricas y niveles de análisis permiten separar calidad de detección, estado por entidad y comportamiento de la alerta temporal, y qué umbrales se fijan antes de medir? Las métricas de seguimiento sólo resultan aplicables si existen anotaciones y objetivos MOT explícitos; no deben trasladarse automáticamente a la evaluación de alertas.

**P-E1-08. Adaptación paramétrica.** ¿En qué condiciones un ajuste fino ligero mejora el dominio objetivo sin degradar la capacidad open-vocabulary, y cómo se mide esa retención con categorías no vistas? La respuesta exige una receta reproducible, datos diferenciados y una comparación que mantenga separadas especialización y generalización.

Las preguntas se condicionan mutuamente: las condiciones evaluables determinan los datos; el hardware limita configuraciones; y las métricas deben distinguir calidad semántica, rendimiento y confirmación temporal. Su resolución corresponde al protocolo experimental y no se anticipa en esta sección.

### 16.8. Conclusiones parciales de la fundamentación teórica

El marco teórico sostiene la factibilidad conceptual de una plataforma asistiva que recibe video, interpreta observables expresados mediante lenguaje, mantiene continuidad temporal y produce alertas para revisión humana. Esa factibilidad no implica superioridad de OVD frente a detectores supervisados ni capacidad para fiscalizar cumplimiento. Depende de la formulación de las condiciones, del comportamiento en el dominio, de la latencia acumulada y de las restricciones ético-legales.

La revisión también delimita qué no puede inferirse desde la teoría. Los benchmarks generales no predicen por sí solos el rendimiento en construcción; una detección por cuadro no equivale a una alerta; un identificador de seguimiento no es identidad personal; y una capacidad descrita en la literatura no constituye una función implementada. Estas separaciones permiten que el diseño posterior declare alcance y evidencia sin convertir objetivos en resultados.

Se reconocen tres limitaciones del propio marco. El campo OVD evoluciona con rapidez y puede modificar el conjunto de alternativas disponibles; los datos de rendimiento publicados provienen de hardware y condiciones que no representan por sí mismos una obra; y el marco regulatorio de IA y protección de datos puede incorporar nuevas exigencias durante el ciclo de vida del sistema. Estas limitaciones refuerzan la necesidad de decisiones trazables y de validación empírica, sin invalidar la base conceptual desarrollada.

---

## Fuente: `docs/informe/entregable/90e-etapa1-anexo-a-y-referencias.md`

> SHA-256 del bloque: `e44e3a8b5e8872eb1b24786ca361532ce922e9dbdf85fcf2e7aee338568d7142`  
> Seleccion: Anexo A y listado de Referencias, ya corregidos en los cuatro pases pero FUERA del entregable de la etapa: el Anexo A pertenece a la seccion 19 y las referencias son globales del informe, y los arma el equipo. Se conserva porque **el cuerpo de la seccion 15 cita la Tabla A.1 y la 15.3.3 cita la Tabla A.2**: si esas tablas no llegan a la seccion 19, quedan dos remisiones colgadas. NO se redacta desde aca.

# 90e — Anexo A y Referencias de la Etapa 1 (material para §19 y para el listado global)

> **Extracción derivada (2026-08-27).** Este material **salió del entregable de la Etapa 1**
> por decisión del usuario: el `.docx` de la etapa contiene **solo el desarrollo** (§15 y §16).
> El Anexo A pertenece a §19 y el listado de referencias es global del informe — los arma el
> equipo, no el redactor de la etapa.
>
> **No se descarta, y hay una razón dura:** el cuerpo de §15 **cita la Tabla A.1**
> («en la Tabla A.1 del Anexo A se incluye una matriz ampliada…», §15.2.3) y §15.3.3 **cita la
> Tabla A.2**. Si esas tablas no llegan a §19, quedan dos remisiones colgadas en el informe.
>
> Lo que este material aporta, ya corregido en los cuatro pases:
> - **Tabla A.1** pasó de 12 a **20 filas** e incorpora **Grounding DINO Swin-T/Swin-L y
>   MM-Grounding-DINO**, que faltaban pese a ser los modelos del trabajo (E1-34).
> - Sus **licencias están corregidas** (E1-33/`AJ-1.09`): DINO-X y Grounding DINO 1.5 figuran
>   como «API cerrada; Apache-2.0 aplica al SDK, no a los pesos», no como Apache-2.0 a secas.
> - **Tabla A.2** reescrita en términos del límite de cada métrica frente a la alerta; la
>   antigua Tabla A.3 (servidores de medios) se eliminó por quedar sin uso (D-E1-9).
> - **83 entradas de referencia**, sin huérfanas y sin citas sin entrada, con las altas de los
>   cuatro pases (Kumar 2022, Lee 2023, OASIS 2019, Ultralytics 2026, Yuksekgonul 2023,
>   Thrush 2022) y `Luxonis` con su letra.

---

## 19. Anexos

### 19.1. Anexo A - Comparativas técnicas y estado del arte complementario

El Anexo A reúne comparativas complementarias que respaldan el estado del arte sin sobrecargar el cuerpo principal. La Tabla A.1 amplía el catálogo de alternativas de detección open-vocabulary y modelos relacionados; la Tabla A.2 sintetiza el alcance y las limitaciones de las métricas MOT tratadas en la sección 15.3.3.

**Tabla A.1**

*Matriz ampliada de alternativas de detección open-vocabulary y modelos relacionados*

| **Modelo** | **Familia** | **Mecanismo visión-lenguaje** | **AP zero-shot reportado** | **Rendimiento reportado** | **Licencia / disponibilidad** |
| --- | --- | --- | --- | --- | --- |
| DINO-X | Transformer | Universal Object Prompt | 59,8 (LVIS-minival) | N/D | API cerrada; Apache-2.0 aplica al SDK, no a los pesos |
| G-DINO 1.5 Pro | Transformer | Fusión cross-modal profunda | 55,7 (LVIS-minival) | N/D | API cerrada; Apache-2.0 aplica al SDK, no a los pesos |
| G-DINO 1.5 Edge | Transformer | Fusión cross-modal optimizada | 36,2 (LVIS-minival) | 75,2 FPS (A100, TensorRT) | API cerrada; Apache-2.0 aplica al SDK, no a los pesos |
| Grounding DINO Swin-L | Transformer | Feature Enhancer, selección de consultas guiada y decoder cross-modal | 52,5 (COCO); 26,1 mean AP (ODinW-35) | N/D | Apache-2.0 |
| Grounding DINO Swin-T | Transformer | Feature Enhancer, selección de consultas guiada y decoder cross-modal | 48,4 (COCO) | N/D | Apache-2.0 |
| MM-Grounding-DINO Tiny | Transformer | Pipeline unificado de grounding y detección | 50,4–50,6 (COCO); 35,7–41,4 (LVIS-minival) | N/D | Apache-2.0 |
| GLIP | Dynamic Head + Swin | Alineamiento región-palabra con fusión profunda | 49,8 (COCO); 26,9 (LVIS) | N/D | MIT |
| OV-DINO | Transformer | LASF + UniDI | 50,6 (COCO) | N/D | Apache-2.0 |
| OV-DETR | Deformable DETR | Matching condicional binario con prompts textuales o visuales | 17,4 novel (OV-LVIS); 29,4 AP50 novel (OV-COCO) | N/D | CC BY-NC-SA 4.0 |
| APE-L (D) | Transformer | Alineamiento por producto punto y encoder cross-modal | 59,6 caja (LVIS); 58,3 caja (COCO) | N/D | Apache-2.0 |
| LLMDet | Transformer + LLM | Coentrenamiento con LLM; LLM descartado en inferencia | 51,1 (LVIS-minival) | N/D | Apache-2.0 |
| DetCLIPv3 | Transformer | Formulación generativa con VLLM | 48,8 (LVIS-minival) | N/D | N/D |
| OWLv2 L/14 | ViT dual-encoder | Autoentrenamiento escalable | 44,6 (LVIS rare) | N/D | Apache-2.0 |
| Detic | Two-stage | Embeddings CLIP como pesos del clasificador de regiones | 17,8 rare (OV-LVIS); 27,8 novel AP50 (OV-COCO) | N/D | Apache-2.0 |
| T-Rex2 Swin-L | Transformer multimodal | Prompts textuales y visuales con fusión tardía | 46,7 texto / 46,8 visual (LVIS-minival) | N/D | IDEA License 1.0; uso no comercial |
| YOLOE-v8-L | One-stage | RepRTA + SAVPE + LRPC | 35,9 (LVIS-minival) | 102,5 FPS (T4, TensorRT) | AGPL-3.0 |
| YOLO-World-L | One-stage | RepVL-PAN contrastivo | 35,4 (LVIS-minival) | 52,0 FPS (V100, PyTorch) | GPL-3.0 |
| OmDet-Turbo-Base | Transformer para tiempo real | EFH + caché textual | 34,7 (LVIS-minival) | 100,2 FPS (A100, TensorRT + caché textual) | Apache-2.0 |
| YOLOE-v8-S | One-stage | RepRTA reparametrizable | 27,9 (LVIS-minival) | 305,8 FPS (T4, TensorRT) | AGPL-3.0 |
| Florence-2-L | Seq2Seq | Generación condicionada por instrucciones | 37,5 (COCO) | Variable | MIT |

Nota. Las cifras conservan el protocolo, el conjunto de evaluación y el hardware informados por cada fuente; por ello, no constituyen un benchmark homogéneo. N/D indica información no reportada o no comparable. En DINO-X y Grounding DINO 1.5, la licencia Apache-2.0 corresponde al SDK de acceso y no a pesos abiertos. Fuente: elaboración propia basada en Cheng et al. (2024), Fu et al. (2025), Jiang et al. (2024), L. H. Li et al. (2021), Liu et al. (2024), Minderer et al. (2023), Ren, Chen, et al. (2024), Ren, Jiang, et al. (2024), Shen et al. (2023), A. Wang et al. (2025), H. Wang et al. (2024), Xiao et al. (2024), Yao et al. (2024), Zang et al. (2022), T. Zhao et al. (2024), X. Zhao et al. (2024) y X. Zhou et al. (2022).

**Tabla A.2**

*Comparación conceptual de métricas MOT y sus límites para evaluar alertas temporales*

| **Métrica** | **Qué caracteriza** | **Sesgo principal** | **Límite respecto de las alertas** |
| --- | --- | --- | --- |
| MOTA | Errores acumulados de detección y cambios de identidad | Está fuertemente condicionada por falsos positivos y falsos negativos del detector | No mide persistencia, oportunidad ni resolución de episodios de alerta |
| IDF1 | Consistencia de identidad a lo largo de una secuencia | Privilegia la correspondencia de identidad y exige anotaciones de trayectorias | No mide la condición semántica ni el comportamiento temporal de la alerta |
| HOTA | Calidad combinada de detección, asociación y localización | Resume componentes del tracker y requiere referencia MOT explícita | No sustituye la evaluación por persona ni la evaluación por episodio temporal |

Nota. MOTA resume errores de detección y cambios de identidad; IDF1 enfatiza la continuidad de identidad; HOTA separa y combina detección, asociación y localización. Las tres caracterizan el seguimiento, pero no miden por sí mismas el estado semántico ni el episodio de alerta. Fuente: elaboración propia basada en Bernardin y Stiefelhagen (2008), Ristani et al. (2016) y Luiten et al. (2021).

## Referencias

Adžemović, M. (2025). Deep Learning-Based Multi-Object Tracking: A Comprehensive Survey from Foundations to State-of-the-Art (arXiv:2506.13457). arXiv. https://doi.org/10.48550/arXiv.2506.13457

Agencia de Acceso a la Información Pública. (s. f.-a). Conocé tus derechos respecto a tus datos personales. Argentina.gob.ar. Recuperado el 12 de enero de 2026, de https://www.argentina.gob.ar/aaip/datospersonales/derechos

Agencia de Acceso a la Información Pública. (s. f.-b). Videovigilancia: ¿Por qué hay que registrar bases de datos de videovigilancia y presentar el manual de tratamiento? Argentina.gob.ar. Recuperado el 12 de enero de 2026, de https://www.argentina.gob.ar/aaip/datospersonales/responsables/videovigilancia

Aharon, N., Orfaig, R., & Bobrovsky, B.-Z. (2022). BoT-SORT: Robust Associations Multi-Pedestrian Tracking (arXiv:2206.14651). arXiv. https://doi.org/10.48550/arXiv.2206.14651

Ahmad, H. M., y Rahimi, A. (2025). SH17: A dataset for human safety and personal protective equipment detection in manufacturing industry. Journal of Safety Science and Resilience, 6(2), 175–185. https://doi.org/10.1016/j.jnlssr.2024.09.002

Ahmad, I., Xiaohui Wei, Yu Sun, & Ya-Qin Zhang. (2005). Video transcoding: An overview of various techniques and research issues. IEEE Transactions on Multimedia, 7(5), 793–804. https://doi.org/10.1109/TMM.2005.854472

AILab-CVC. (2024, January 30). YOLO-World. GitHub. Retrieved January 21, 2026, from https://github.com/AILab-CVC/YOLO-World

Amirante, A., Castaldi, T., Miniero, L., & Romano, S. P. (2014). Janus: A general purpose WebRTC gateway. Proceedings of the Conference on Principles, Systems and Applications of IP Telecommunications, 1–8. https://doi.org/10.1145/2670386.2670389

Amirante, A., Castaldi, T., Miniero, L., & Romano, S. P. (2015). Performance analysis of the Janus WebRTC gateway. Proceedings of the 1st Workshop on All-Web Real-Time Systems, 1–7. https://doi.org/10.1145/2749215.2749223

Ananthanarayanan, G., Bahl, P., Bodik, P., Chintalapudi, K., Philipose, M., Ravindranath, L., & Sinha, S. (2017). Real-Time Video Analytics: The Killer App for Edge Computing. Computer, 50(10), 58–67. https://doi.org/10.1109/MC.2017.3641638

Argentina. (2000). Ley N.º 25.326: Ley de Protección de los Datos Personales. Infoleg. https://servicios.infoleg.gob.ar/infolegInternet/anexos/60000-64999/64790/texact.htm

Argentina. (2001, noviembre 29). Decreto 1558/2001: Ley 25.326—Reglamentación. Argentina.gob.ar. https://www.argentina.gob.ar/normativa/nacional/decreto-1558-2001-70368

Argentina. (2006, septiembre 19). Disposición 11/2006: Medidas de seguridad para el tratamiento y conservación de los datos personales. Argentina.gob.ar. https://www.argentina.gob.ar/normativa/nacional/disposici%C3%B3n-11-2006-120120

Argentina. (2015, febrero 24). Disposición 10/2015: Condiciones de licitud para las actividades de recolección y posterior tratamiento de imágenes digitales de personas con fines de seguridad. Argentina.gob.ar. https://www.argentina.gob.ar/normativa/nacional/disposici%C3%B3n-10-2015-243335

Axis Communications AB. (2015). Latency in live network video surveillance (63380/EN/R1/1504) [White paper]. https://www.axis.com/dam/public/9d/e4/5d/latency-in-live-network-video-surveillance-en-US-190945.pdf

Bachhuber, C., Steinbach, E., Freundl, M., & Reisslein, M. (2018). On the Minimization of Glass-to-Glass and Glass-to-Algorithm Delay in Video Communication. IEEE Transactions on Multimedia, 20(1), 238–252. https://doi.org/10.1109/TMM.2017.2726189

Bass, L., Clements, P., & Kazman, R. (2022). Software architecture in practice (Fourth edition). Addison-Wesley.

Bernardin, K., & Stiefelhagen, R. (2008). Evaluating multiple object tracking performance: The CLEAR MOT metrics. EURASIP Journal on Image and Video Processing, 2008(1), 1-10. https://doi.org/10.1155/2008/246309

Bewley, A., Ge, Z., Ott, L., Ramos, F., y Upcroft, B. (2016). Simple online and realtime tracking. En 2016 IEEE International Conference on Image Processing (ICIP) (pp. 3464-3468). IEEE. https://doi.org/10.1109/ICIP.2016.7533003

Cao, J., Pang, J., Weng, X., Khirodkar, R., & Kitani, K. (2023). Observation-Centric SORT: Rethinking SORT for Robust Multi-Object Tracking. 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 9686–9696. https://doi.org/10.1109/CVPR52729.2023.00934

Card, S. K., Moran, T. P., & Newell, A. (2008). The psychology of human-computer interaction (Repr). Erlbaum.

Carion, N., Massa, F., Synnaeve, G., Usunier, N., Kirillov, A., & Zagoruyko, S. (2020). End-to-End Object Detection with Transformers (arXiv:2005.12872). arXiv. https://doi.org/10.48550/arXiv.2005.12872

Chen, J., & Ran, X. (2019). Deep Learning With Edge Computing: A Review. Proceedings of the IEEE, 107(8), 1655–1674. https://doi.org/10.1109/JPROC.2019.2921977

Chen, X., & Zou, Z. (2025). Are large pre-trained vision language models effective construction safety inspectors? (arXiv:2508.11011). arXiv. https://doi.org/10.48550/arXiv.2508.11011

Cheng, T., Song, L., Ge, Y., Liu, W., Wang, X., & Shan, Y. (2024). YOLO-World: Real-time open-vocabulary object detection. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 16901–16911). https://doi.org/10.1109/CVPR52733.2024.01599

Choi, L., & Greer, R. (2024). Evaluating cascaded methods of vision-language models for zero-shot detection and association of hardhats for increased construction safety (arXiv:2410.12225). arXiv. https://doi.org/10.48550/arXiv.2410.12225

Cugola, G., & Margara, A. (2012). Processing flows of information: From data stream to complex event processing. ACM Computing Surveys, 44(3), 1–62. https://doi.org/10.1145/2187671.2187677

DASH Industry Forum. (2020, marzo 27). Low-latency Modes for DASH. CR-Low-Latency-Live-r8. https://dashif.org/docs/CR-Low-Latency-Live-r8.pdf

Deber, J., Jota, R., Forlines, C., & Wigdor, D. (2015). How Much Faster is Fast Enough?: User Perception of Latency & Latency Improvements in Direct and Indirect Touch. Proceedings of the 33rd Annual ACM Conference on Human Factors in Computing Systems, 1827–1836. https://doi.org/10.1145/2702123.2702300

Decreto 351/79 de 1979. Reglamentación de la Ley 19.587 de Higiene y Seguridad en el Trabajo. (1979, febrero 5). Infoleg. https://servicios.infoleg.gob.ar/infolegInternet/anexos/30000-34999/32030/dto351-1979-anexo1.htm

Decreto 911/96 de 1996. Reglamento de Higiene y Seguridad para la Industria de la Construcción. (1996, 5 de agosto). Infoleg. https://servicios.infoleg.gob.ar/infolegInternet/anexos/35000-39999/38568/texact.htm

Dendorfer, P., Rezatofighi, H., Milan, A., Shi, J., Cremers, D., Reid, I., Roth, S., Schindler, K., & Leal-Taixé, L. (2020). MOT20: A benchmark for multi object tracking in crowded scenes (arXiv:2003.09003). arXiv. https://doi.org/10.48550/arXiv.2003.09003

Du, C., Lin, C., Jin, R., Chai, B., Yao, Y., & Su, S. (2024). Exploring the State-of-the-Art in Multi-Object Tracking: A Comprehensive Survey, Evaluation, Challenges, and Future Directions. Multimedia Tools and Applications, 83(29), 73151–73189. https://doi.org/10.1007/s11042-023-17983-2

Du, Y., Wei, F., Zhang, Z., Shi, M., Gao, Y., & Li, G. (2022). Learning to prompt for open-vocabulary object detection with vision-language model. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 14084-14093). https://doi.org/10.1109/CVPR52688.2022.01369

European Data Protection Board. (2020, enero 30). Guidelines 3/2019 on processing of personal data through video devices (Version 2.0). EDPB. https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-32019-processing-personal-data-through-video_en

Everingham, M., Van Gool, L., Williams, C. K. I., Winn, J., & Zisserman, A. (2010). The Pascal Visual Object Classes (VOC) Challenge. International Journal of Computer Vision, 88(2), 303–338. https://doi.org/10.1007/s11263-009-0275-4

Fu, S., Yang, Q., Mo, Q., Yan, J., Wei, X., Meng, J., Xie, X., & Zheng, W.-S. (2025, January 31). [2501.18954] LLMDet: Learning Strong Open-Vocabulary Object Detectors under the Supervision of Large Language Models. arXiv. Retrieved January 21, 2026, from https://arxiv.org/abs/2501.18954

Gettys, J., & Nichols, K. (2012). Bufferbloat: Dark buffers in the internet. Communications of the ACM, 55(1), 57–65. https://doi.org/10.1145/2063176.2063196

Google. (2022, May). owlvit-large-patch14. Hugging Face. https://huggingface.co/google/owlvit-large-patch14

Google. (2023, June). owlv2-base-patch16-ensemble. Hugging Face. https://huggingface.co/google/owlv2-base-patch16-ensemble

Gupta, A., Dollár, P., & Girshick, R. (2019). LVIS: A Dataset for Large Vocabulary Instance Segmentation (arXiv:1908.03195). arXiv. https://doi.org/10.48550/arXiv.1908.03195

IDEA-Research. (2024a, noviembre 20). DINO-X-API: A unified vision model for open-world object detection and understanding [Repositorio de código]. GitHub. https://github.com/IDEA-Research/DINO-X-API

IDEA-Research. (2024c, mayo 18). GroundingDINO: Official implementation of “Grounding DINO: Marrying DINO with grounded pre-training for open-set object detection” [Repositorio de código]. GitHub. https://github.com/IDEA-Research/GroundingDINO

Iorga, M., Feldman, L., Barton, R., Martin, M. J., Goren, N., & Mahmoudi, C. (2018). Fog computing conceptual model (NIST SP 500-325; p. NIST SP 500-325). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.500-325

ISO. (2018). ISO 45001:2018 Occupational health and safety management systems—Requirements with guidance for use. ISO. https://www.iso.org/standard/63787.html

ISO. (2023). ISO/IEC 42001:2023—Artificial intelligence management system. ISO. https://www.iso.org/standard/42001

ISO/IEC. (2022). Information technology—Dynamic adaptive streaming over HTTP (DASH)—Part 1: Media presentation description and segment formats. ISO/IEC 23009-1:2022. https://www.iso.org/standard/83314.html

Jiang, Q., Li, F., Zeng, Z., Ren, T., Liu, S., & Zhang, L. (2024). T-Rex2: Towards Generic Object Detection via Text-Visual Prompt Synergy (arXiv:2403.14610). arXiv. https://doi.org/10.48550/arXiv.2403.14610

Keranen, A., Holmberg, C., & Rosenberg, J. (2018). Interactive Connectivity Establishment (ICE): A Protocol for Network Address Translator (NAT) Traversal (No. RFC8445; p. RFC8445). RFC Editor. https://doi.org/10.17487/RFC8445

Khattak, M. U., Rasheed, H., Maaz, M., Khan, S., & Khan, F. S. (2023). MaPLe: Multi-modal Prompt Learning (arXiv:2210.03117). arXiv. https://doi.org/10.48550/arXiv.2210.03117

Kirkpatrick, J., Pascanu, R., Rabinowitz, N., Veness, J., Desjardins, G., Rusu, A. A., Milan, K., Quan, J., Ramalho, T., Grabska-Barwinska, A., Hassabis, D., Clopath, C., Kumaran, D., & Hadsell, R. (2017). Overcoming catastrophic forgetting in neural networks. Proceedings of the National Academy of Sciences, 114(13), 3521-3526. https://doi.org/10.1073/pnas.1611835114

Kreutz, D., Ramos, F. M. V., Esteves Verissimo, P., Esteve Rothenberg, C., Azodolmolky, S., & Uhlig, S. (2015). Software-Defined Networking: A Comprehensive Survey. Proceedings of the IEEE, 103(1), 14–76. https://doi.org/10.1109/JPROC.2014.2371999

Kumar, A., Raghunathan, A., Jones, R. M., Ma, T., & Liang, P. (2022). Fine-tuning can distort pretrained features and underperform out-of-distribution. International Conference on Learning Representations. https://arxiv.org/abs/2202.10054

Kurose, J. F., & Ross, K. W. (2021). Computer networking: A top-down approach (Eighth edition). Pearson.

Lee, Y., Chen, A. S., Tajwar, F., Kumar, A., Yao, H., Liang, P., & Finn, C. (2023). Surgical fine-tuning improves adaptation to distribution shifts. International Conference on Learning Representations. https://arxiv.org/abs/2210.11466

Ley 19.587 de 1972. Ley de Higiene y Seguridad en el Trabajo. (1972). Infoleg. https://servicios.infoleg.gob.ar/infolegInternet/anexos/15000-19999/17612/norma.htm

Li, L. H., Zhang, P., Zhang, H., Yang, J., Li, C., Zhong, Y., Wang, L., Yuan, L., Zhang, L., Hwang, J.-N., Chang, K.-W., & Gao, J. (2021). Grounded language-image pre-training (arXiv:2112.03857). arXiv. https://doi.org/10.48550/arXiv.2112.03857

Li, S., Fischer, T., Ke, L., Ding, H., Danelljan, M., & Yu, F. (2023). OVTrack: Open-Vocabulary Multiple Object Tracking. 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 5567–5577. https://doi.org/10.1109/CVPR52729.2023.00539

Li, S., Ren, H., Xie, X., & Cao, Y. (2025). A Review of Multi‐Object Tracking in Recent Times. IET Computer Vision, 19(1), e70010. https://doi.org/10.1049/cvi2.70010

Lin, T.-Y., Maire, M., Belongie, S., Hays, J., Perona, P., Ramanan, D., Dollar, P. y Zitnick, C. L. (2014). Microsoft COCO: Common objects in context. En D. Fleet, T. Pajdla, B. Schiele y T. Tuytelaars (Eds.), Computer Vision - ECCV 2014 (Vol. 8693, pp. 740-755). Springer. https://doi.org/10.1007/978-3-319-10602-1_48

Liu, S., Zeng, Z., Ren, T., Li, F., Zhang, H., Yang, J., Jiang, Q., Li, C., Yang, J., Su, H., Zhu, J., & Zhang, L. (2024). Grounding DINO: Marrying DINO with grounded pre-training for open-set object detection. In Computer Vision - ECCV 2024 (pp. 38-55). Springer. https://doi.org/10.1007/978-3-031-72970-6_3

Luiten, J., Os̆ep, A., Dendorfer, P., Torr, P., Geiger, A., Leal-Taixé, L., & Leibe, B. (2021). HOTA: A Higher Order Metric for Evaluating Multi-object Tracking. International Journal of Computer Vision, 129(2), 548–578. https://doi.org/10.1007/s11263-020-01375-2

Luo, W., Xing, J., Milan, A., Zhang, X., Liu, W., & Kim, T.-K. (2021). Multiple object tracking: A literature review. Artificial Intelligence, 293, 103448. https://doi.org/10.1016/j.artint.2020.103448

Luxonis. (s. f.-b). OAK-D Pro PoE [Documentación de hardware]. Luxonis Docs. https://docs.luxonis.com/hardware/products/OAK-D%20Pro%20PoE

May, W. (2017). HTTP Live Streaming (R. Pantos, Ed.; No. RFC8216; p. RFC8216). RFC Editor. https://doi.org/10.17487/RFC8216

Microsoft. (2024, June). Florence-2-large. Hugging Face. https://huggingface.co/microsoft/Florence-2-large

Milan, A., Leal-Taixe, L., Reid, I., Roth, S., & Schindler, K. (2016). MOT16: A Benchmark for Multi-Object Tracking (arXiv:1603.00831). arXiv. https://doi.org/10.48550/arXiv.1603.00831

Minderer, M., Gritsenko, A., & Houlsby, N. (2023). Scaling open-vocabulary object detection (arXiv:2306.09683). arXiv. https://doi.org/10.48550/arXiv.2306.09683

Minderer, M., Gritsenko, A., Stone, A., Neumann, M., Weissenborn, D., Dosovitskiy, A., Mahendran, A., Arnab, A., Dehghani, M., Shen, Z., Wang, X., Zhai, X., Kipf, T., & Houlsby, N. (2022). Simple open-vocabulary object detection with vision transformers. In Computer Vision – ECCV 2022 (pp. 728–755). Springer. https://doi.org/10.1007/978-3-031-20080-9_42

Nakagawa, K., Tsukada, M., Shima, K., & Esaki, H. (2021). WebRTC-based measurement tool for peer-to-peer applications and preliminary findings with real users. Asian Internet Engineering Conference, 1–8. https://doi.org/10.1145/3497777.3498544

NVIDIA. (2024). DeepStream SDK 8.0 for NVIDIA dGPU/X86 and Jetson—DeepStream documentation. https://docs.nvidia.com/metropolis/deepstream/dev-guide/text/DS_Release_notes.html

NVIDIA. (s. f.-g). Grounding DINO. NVIDIA TAO Toolkit Documentation. Recuperado el 27 de agosto de 2026, de https://docs.nvidia.com/tao/tao-toolkit/latest/text/cv_finetuning/pytorch/object_detection/grounding_dino.html

NVIDIA. (s. f.-h). NVIDIA Triton Inference Server. Recuperado el 27 de agosto de 2026, de https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/index.html

OASIS. (2019). MQTT Version 5.0. OASIS Standard. https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html

ONVIF. (2019). ONVIF Profile S Specification (ONVIF Profile S). ONVIF. https://www.onvif.org/wp-content/uploads/2019/12/ONVIF_Profile_-S_Specification_v1-3.pdf

Organisation for Economic Co-operation and Development. (2019, mayo 1). OECD AI Principles overview. OECD. https://oecd.ai/en/ai-principles

Otgonbold, M.-E., Gochoo, M., Alnajjar, F. S., Ali, L., Tan, T.-H., Hsieh, J.-W., y Chen, P.-Y. (2022). SHEL5K: An extended dataset and benchmarking for safety helmet detection. Sensors, 22(6), 2315. https://doi.org/10.3390/s22062315

Pantos, R. (2025). HTTP Live Streaming 2nd Edition (Internet-Draft). Internet Engineering Task Force. https://datatracker.ietf.org/doc/draft-pantos-hls-rfc8216bis/18/

Parmar, H., & Thornburgh, M. (2012). Adobe’s Real Time Messaging Protocol. Adobe. https://ptacts.uspto.gov/ptacts/public-informations/petitions/1557060/download-documents?artifactId=CX29dwexemvGTAgu1npsGb4QtKzyjACHSNYXLhjJp5m1SpQS4AAf-3A

Radford, A., Kim, J. W., Hallacy, C., Ramesh, A., Goh, G., Agarwal, S., Sastry, G., Askell, A., Mishkin, P., Clark, J., Krueger, G., & Sutskever, I. (2021). Learning Transferable Visual Models From Natural Language Supervision (arXiv:2103.00020). arXiv. https://doi.org/10.48550/arXiv.2103.00020

Rasaee, H., Koleilat, T., & Rivaz, H. (2025). Grounding DINO-US-SAM: Text-Prompted Multi-Organ Segmentation in Ultrasound with LoRA-Tuned Vision-Language Models. IEEE Transactions on Ultrasonics, Ferroelectrics, and Frequency Control, 72(10), 1414-1425. https://doi.org/10.1109/TUFFC.2025.3605285

Ren, T., Chen, Y., Jiang, Q., Zeng, Z., Xiong, Y., Liu, W., Ma, Z., Shen, J., Gao, Y., Jiang, X., Chen, X., Song, Z., Zhang, Y., Huang, H., Gao, H., Liu, S., Zhang, H., Li, F., Yu, K., & Zhang, L. (2024). DINO-X: A unified vision model for open-world object detection and understanding (arXiv:2411.14347). arXiv. https://doi.org/10.48550/arXiv.2411.14347

Ren, T., Jiang, Q., Liu, S., Zeng, Z., Liu, W., Gao, H., Huang, H., Ma, Z., Jiang, X., Chen, Y., Xiong, Y., Zhang, H., Li, F., Tang, P., Yu, K., & Zhang, L. (2024). Grounding DINO 1.5: Advance the “Edge” of Open-Set Object Detection (Versión 2). arXiv. https://doi.org/10.48550/ARXIV.2405.10300

Ren, T., Liu, S., Zeng, A., Lin, J., Li, K., Cao, H., Chen, J., Huang, X., Chen, Y., Yan, F., Zeng, Z., Zhang, H., Li, F., Yang, J., Li, H., Jiang, Q., & Zhang, L. (2024). Grounded SAM: Assembling Open-World Models for Diverse Visual Tasks (arXiv:2401.14159). arXiv. https://doi.org/10.48550/arXiv.2401.14159

Ristani, E., Solera, F., Zou, R., Cucchiara, R., & Tomasi, C. (2016). Performance Measures and a Data Set for Multi-target, Multi-camera Tracking. En G. Hua & H. Jégou (Eds.), Computer Vision – ECCV 2016 Workshops (Vol. 9914, pp. 17–35). Springer International Publishing. https://doi.org/10.1007/978-3-319-48881-3_2

Roy (Whalen), S. (2024, julio 18). RTMP vs. RTSP: Which Protocol Should You Choose? (Update). Wowza Media Systems. Wowza Blog. https://www.wowza.com/blog/rtmp-vs-rtsp-which-protocol-should-you-choose

Satyanarayanan, M. (2017). The Emergence of Edge Computing. Computer, 50(1), 30–39. https://doi.org/10.1109/MC.2017.9

Schulzrinne, H., Casner, S., Frederick, R., & Jacobson, V. (2003). RTP: A Transport Protocol for Real-Time Applications (No. RFC3550; p. RFC3550). RFC Editor. https://doi.org/10.17487/rfc3550

Schulzrinne, H., Rao, A., & Lanphier, R. (1998). Real Time Streaming Protocol (RTSP) (No. RFC2326; p. RFC2326). RFC Editor. https://doi.org/10.17487/rfc2326

Schulzrinne, H., Rao, A., Lanphier, R., & Westerlund, M. (2016). Real-Time Streaming Protocol Version 2.0 (M. Stiemerling, Ed.; No. RFC7826; p. RFC7826). RFC Editor. https://doi.org/10.17487/RFC7826

Sharabayko, M. P., Sharabayko, M. A., Dube, J., Kim, J., & Kim, J. (2024). The SRT Protocol (Internet-Draft (working copy)). Internet Engineering Task Force. https://haivision.github.io/srt-rfc/draft-sharabayko-srt.html

Shen, Y., Fu, C., Chen, P., Zhang, M., Li, K., Sun, X., Wu, Y., Lin, S., & Ji, R. (2023, December 4). Aligning and Prompting Everything All at Once for Universal Visual Perception. arXiv. https://arxiv.org/abs/2312.02153

Shi, W., Cao, J., Zhang, Q., Li, Y., & Xu, L. (2016). Edge Computing: Vision and Challenges. IEEE Internet of Things Journal, 3(5), 637–646. https://doi.org/10.1109/JIOT.2016.2579198

Sonono, T. (2019). Interoperable Retransmission Protocols with Low Latency and Constrained Delay: A Performance Evaluation of RIST and SRT [Master’s thesis, KTH Royal Institute of Technology]. https://www.diva-portal.org/smash/get/diva2:1335907/FULLTEXT01.pdf

SRT. (1997, julio 7). Resolución SRT 51/97 de 1997. Mecanismo Preventivo de Control en Obras de Construcción. Infoleg. https://servicios.infoleg.gob.ar/infolegInternet/anexos/40000-44999/44588/norma.htm

SRT. (1998, marzo 31). Resolución SRT 35/98 de 1998. Coordinación de Programas de Seguridad en Obras de Construcción. Infoleg. https://servicios.infoleg.gob.ar/infolegInternet/anexos/50000-54999/50188/norma.htm

SRT. (s. f.). Programa de Construcción. Argentina.gob.ar. Recuperado el 12 de enero de 2026, de https://www.argentina.gob.ar/srt/prevencion/programas/construccion

THU-MIG. (2025). THU-MIG / yoloe: YOLOE: Real-Time Seeing Anything. GitHub. https://github.com/THU-MIG/yoloe

Thrush, T., Jiang, R., Bartolo, M., Singh, A., Williams, A., Kiela, D., & Ross, C. (2022). Winoground: Probing vision and language models for visio-linguistic compositionality (arXiv:2204.03162). arXiv. https://doi.org/10.48550/arXiv.2204.03162

Ucar, A., Ro, S., Satwika, S., Gayathri, P. Y., & Balsha, M. G. (2025). Fine-Tuning Florence2 for Enhanced Object Detection in Un-constructed Environments: Vision-Language Model Approach (arXiv:2503.04918). arXiv. https://doi.org/10.48550/arXiv.2503.04918

Ultralytics. (2026). Ultralytics YOLO26. https://docs.ultralytics.com/models/yolo26/

UNESCO. (2021). Recommendation on the ethics of artificial intelligence. https://unesdoc.unesco.org/ark:/48223/pf0000380455

Video Services Forum. (2020). Reliable Internet Stream Transport (RIST) protocol specification – Simple profile. Video Services Forum. https://static.vsf.tv/download/technical_recommendations/VSF_TR-06-1_2020_06_25.pdf

Video Services Forum. (2024). Reliable Internet Stream Transport (RIST) Protocol Specification – Main Profile. Video Services Forum. https://static.vsf.tv/download/technical_recommendations/VSF_TR-06-2_2024_06_12.pdf

Wang, A., Liu, L., Chen, H., Lin, Z., Han, J., & Ding, G. (2025). YOLOE: Real-Time Seeing Anything (arXiv:2503.07465). arXiv. https://doi.org/10.48550/arXiv.2503.07465

Wang, H., Ren, P., Jie, Z., Dong, X., Feng, C., Qian, Y., Ma, L., Jiang, D., Wang, Y., Lan, X., & Liang, X. (2024). OV-DINO: Unified open-vocabulary detection with language-aware selective fusion (arXiv:2407.07844). arXiv. https://doi.org/10.48550/arXiv.2407.07844

Wang, H., Zhang, X., Chen, H., Xu, Y., & Ma, Z. (2022). Inferring End-to-End Latency in Live Videos. IEEE Transactions on Broadcasting, 68(2), 517–529. https://doi.org/10.1109/TBC.2021.3071060

Wang, Z., Wu, Y., Yang, L., Thirunavukarasu, A., Evison, C., y Zhao, Y. (2021). Fast personal protective equipment detection for real construction sites using deep learning approaches. Sensors, 21(10), 3478. https://doi.org/10.3390/s21103478

Wojke, N., Bewley, A., & Paulus, D. (2017). Simple online and realtime tracking with a deep association metric. 2017 IEEE International Conference on Image Processing (ICIP), 3645–3649. https://doi.org/10.1109/ICIP.2017.8296962

World Wide Web Consortium. (2025). WebRTC: Real-Time Communication in Browsers (W3C Recommendation). World Wide Web Consortium. https://www.w3.org/TR/webrtc/

Xiao, B., Wu, H., Xu, W., Dai, X., Hu, H., Lu, Y., Zeng, M., Liu, C., & Yuan, L. (2024). Florence-2: Advancing a unified representation for a variety of vision tasks. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 4818–4829). https://doi.org/10.1109/CVPR52733.2024.00461

Yao, L., Pi, R., Han, J., Liang, X., Xu, H., Zhang, W., Li, Z., & Xu, D. (2024). DetCLIPv3: Towards versatile generative open-vocabulary object detection (arXiv:2404.09216). arXiv. https://doi.org/10.48550/arXiv.2404.09216

Yousefpour, A., Fung, C., Nguyen, T., Kadiyala, K., Jalali, F., Niakanlahiji, A., Kong, J., & Jue, J. P. (2019). All one needs to know about fog computing and related edge computing paradigms: A complete survey. Journal of Systems Architecture, 98, 289–330. https://doi.org/10.1016/j.sysarc.2019.02.009

Yuksekgonul, M., Bianchi, F., Kalluri, P., Jurafsky, D., & Zou, J. (2023). When and why vision-language models behave like bags-of-words, and what to do about it? International Conference on Learning Representations. https://arxiv.org/abs/2210.01936

Zang, Y., Li, W., Zhou, K., Huang, C., & Loy, C. C. (2022, March 22). [2203.11876] Open-Vocabulary DETR with Conditional Matching. arXiv. https://arxiv.org/abs/2203.11876

Zareian, A., Rosa, K. D., Hu, D. H., & Chang, S.-F. (2021). Open-Vocabulary Object Detection Using Captions (arXiv:2011.10678). arXiv. https://doi.org/10.48550/arXiv.2011.10678

Zhang, H., Zhang, P., Hu, X., Chen, Y.-C., Li, L. H., Dai, X., Wang, L., Yuan, L., Hwang, J.-N., & Gao, J. (2022). GLIPv2: Unifying Localization and Vision-Language Understanding (arXiv:2206.05836). arXiv. https://doi.org/10.48550/arXiv.2206.05836

Zhang, Y., Sun, P., Jiang, Y., Yu, D., Weng, F., Yuan, Z., Luo, P., Liu, W., & Wang, X. (2022). ByteTrack: Multi-object Tracking by Associating Every Detection Box. En S. Avidan, G. Brostow, M. Cissé, G. M. Farinella, & T. Hassner (Eds.), Computer Vision – ECCV 2022 (Vol. 13682, pp. 1–21). Springer Nature Switzerland. https://doi.org/10.1007/978-3-031-20047-2_1

Zhao, T., Liu, P., He, X., Zhang, L., & Lee, K. (2024). Real-time Transformer-based Open-Vocabulary Detection with Efficient Fusion Head (arXiv:2403.06892). arXiv. https://doi.org/10.48550/arXiv.2403.06892

Zhao, X., Chen, Y., Xu, S., Li, X., Wang, X., Li, Y., & Huang, H. (2024). An Open and Comprehensive Pipeline for Unified Object Grounding and Detection (arXiv:2401.02361). arXiv. https://doi.org/10.48550/arXiv.2401.02361

Zhou, K., Yang, J., Loy, C. C., & Liu, Z. (2022b). Learning to Prompt for Vision-Language Models. International Journal of Computer Vision, 130(9), 2337–2348. https://doi.org/10.1007/s11263-022-01653-1

Zhou, X., Girdhar, R., Joulin, A., Krähenbühl, P., & Misra, I. (2022). Detecting twenty-thousand classes using image-level supervision (arXiv:2201.02605). arXiv. https://doi.org/10.48550/arXiv.2201.02605

---

## Fuente: `docs/informe/ajustes/01-etapa-1-fundamentacion-teorica.md`

> SHA-256 del bloque: `844a02caad39f12c623f26e930747ec99ee741304e6c37c992a3dee0345191cd`  
> Seleccion: tablero ORIGINAL AJ-1.01 a AJ-1.16 (2026-08-10), con el relevamiento que dio origen a la etapa y las cifras de vara con su marca de confianza. **Los 16 estan RESUELTOS** -AJ-1.04 y AJ-1.05 por eliminacion de las fichas, AJ-1.09 en el Anexo A, AJ-1.16 por el pase 3-. Se conserva como historia y como fuente de las cifras: NO es una lista de tareas.

# Etapa 1 — ajustes a la fundamentación teórica (§15 Estado del Arte, §16 Marco Teórico)

> ✅ **Estado (✎ 2026-08-28): Etapa 1 CERRADA** — §15+§16 **v1.0** en `entregable/desarrollando/`,
> con **cinco pases** E1 aplicados y verificados (`verificar_entregable.py`), los 16 `AJ-1.xx`
> resueltos y las podas 01–11 aplicadas; el Anexo A salió a `90e` (decisión del usuario, 08-27).
> Única decisión de fondo abierta: `D-E1-11` (AAIP, `[[PENDIENTE]]`). Constancia:
> `informe/entregable/00-el-informe-hoy.md`. **Lo que sigue abajo es registro histórico** del
> relevamiento del 08-10, conservado como criterio de lectura — no es una lista de tareas.
>
> **Estado (2026-08-10):** relevado, **sin pase de correcciones aplicado**. El
> relevamiento salió de contrastar el §15 del informe contra fuentes primarias
> fetcheadas y contra nuestra propia evidencia medida (`sintesis/resultados-y-conclusiones.md`
> §7, relevamiento del 2026-08-06). El §16 (Marco Teórico) **no fue relevado todavía**
> — es `AJ-1.16`, y es un hueco declarado, no un "no hay nada que cambiar".
>
> **Marca de confianza de las cifras externas**, tal como la fija la fuente:
> **[P]** verificada en fuente primaria · **[S]** fuente secundaria oficial ·
> **[R]** circulante sin verificar.

| Dónde | Qué |
|---|---|
| Texto actual | `entregable/96c` (§15 Estado del Arte) · `entregable/96d` (§16 Marco Teórico) · `entregable/96e` §19.1 (Anexo A, Tabla A.1) |
| Fuente del relevamiento | `sintesis/resultados-y-conclusiones.md` §7.1–§7.4 |
| Teoría de apoyo para redactar | `sintesis/fundamentos-teoricos.md` |

---

## 1. Por qué esta etapa no se puede saltear

El §17.5 (Etapa 5) va a reportar **mAP@0,5 0,551 agregado** sobre `bench_v3`. Un número
así, sin vara, no significa nada para un jurado — y hoy **el §15 no da la vara**: cita
SHEL5K, CHV y SH17 únicamente como datasets, sin reportar ni una cifra de mAP de la
literatura supervisada. Toda la defensa pivotea sobre ese contraste ("~63% del techo
sin entrenar"). **La vara se construye acá; el contraste se hace en §17.5/§18** — el
§15 no cita resultados propios (regla de no-anacronismo, mapa regla 5).

Los dos primeros ajustes son, por eso, los únicos 🔴 de esta etapa.

---

## 2. Tablero de ajustes

| ID | Sección | Tipo | Pri | Enunciado |
|---|---|---|---|---|
| **AJ-1.01** | §15 | CONCRETA | 🔴 | **Hueco 1: falta la línea base de EPP supervisado.** Incorporar la Vara 1 con cifras, o declarar la ausencia como brecha. |
| **AJ-1.02** | §15 / Tabla 3 | CONCRETA | 🔴 | **Hueco 2: el §15 no deja declarada la brecha que motiva el bench propio** — y la brecha se sostiene con literatura, sin adelantar resultados. |
| **AJ-1.03** | §15 | ERRATA | 🟠 | El 52,5 AP de GDINO es del backbone **Swin-L** y el informe nunca lo declara; lo desplegado acá es **Swin-T**. |
| **AJ-1.04** | §15 / tablas | ERRATA | 🟡 | OmDet-Turbo-Tiny "30,3 LVIS" (probable *mislabel* de ODinW-13) y 34,0 vs 34,7 entre tablas. |
| **AJ-1.05** | §15 | ERRATA | 🟡 | El 53,4 COCO de OmDet-Turbo probablemente **no es zero-shot**. |
| **AJ-1.06** | §15 | ERRATA | 🟡 | LLMDet "51,1–52,4": el 52,4 no tiene origen. |
| **AJ-1.07** | §15 | ERRATA | 🟡 | El caching "ahorra ≈40 ms" en un modelo al que la misma tabla asigna **7,1 ms totales**. |
| **AJ-1.08** | Tabla 3 | PRECISA | 🟡 | La columna Latencia es **1000/FPS**: derivada, no medida. Declararlo. |
| **AJ-1.09** | Anexo A / Tabla A.1 | ERRATA | 🟠 | GDINO 1.5 y DINO-X figuran como "Apache-2.0" siendo **API cerrada sin pesos abiertos** (la licencia es del SDK). |
| **AJ-1.10** | §15 / Referencias | ERRATA | 🟡 | Citas inconsistentes: Liu 2023/2024, Minderer, Xiao, Lin 2014/2015, Ren a/b/c. |
| **AJ-1.11** | §15 | CONCRETA | 🟡 | **MM-Grounding-DINO no tiene ninguna cifra en el informe**, y el proyecto lo evaluó y lo descartó. |
| **AJ-1.12** | §15 | PRECISA | 🟠 | **Advertencia de métrica**: AP 0,50:0,95 (COCO/LVIS) y mAP@0,5 (EPP y nuestro bench) **nunca en la misma columna**. |
| **AJ-1.13** | §15 | CONCRETA | 🟠 | Incorporar la **Vara 3** — el cruce OVD×EPP está casi vacío en la literatura: la brecha se declara acá; quién la ocupa se relata en §17.5. |
| **AJ-1.14** | §15 | PRECISA | 🟠 | Corregir el uso de **Abdalwhab 2025**: es evidencia de brecha de vocabulario zero-shot, **no** del efecto de ajustar un OVD. |
| **AJ-1.15** | §15 → §17.5 | PRECISA | 🟠 | Fijar la **regla de tres tiempos** para presentar conclusiones, y usar "adaptación" con precisión. |
| **AJ-1.16** | **§16** | EVIDENCIA | 🟡 | **Hueco: el §16 Marco Teórico no fue relevado** contra lo que hoy sabemos. |

---

## 3. Los ajustes, desarrollados

### AJ-1.01 · §15 · CONCRETA · 🔴 — la vara supervisada in-domain

**Qué pasa hoy.** El informe **no reporta ni una cifra de mAP** de la literatura de
detección de EPP con modelos entrenados. SHEL5K, CHV y SH17 aparecen solo como
datasets.

**Qué debe decir.** La Vara 1, en **mAP@0,5** [P/S]:

| Dataset (paper) | Mejor modelo entrenado | mAP@0,5 | Dato fino que importa |
|---|---|---|---|
| SHEL5K (Otgonbold 2022, *Sensors* 22(6):2315) | YOLOR | **0,883** | `head` (cabeza sin casco) **0,907** — supervisada, la clase **no** es difícil |
| CHV (Wang 2021, *Sensors* 21(10):3478) | YOLOv5x | **0,866** | 6 clases (person, vest, 4 colores de casco) |
| SH17 (2024; 17 clases, industrial) | YOLOv9-e | **≈0,71** | YOLOv8 n→x: 0,58–0,69 — con vocabulario grande el techo baja |

El dato de `head` 0,907 es el fundamento externo de dos conclusiones propias (AF-5 y
F-88.3): **la clase `bare_head` no es difícil; lo difícil es alcanzarla por vía
léxico-conceptual sin entrenar.**

**Alternativa admisible** si no se quiere ampliar el §15: declarar explícitamente la
ausencia como brecha del estado del arte. Lo que **no** es admisible es dejar el 0,551
sin vara.

---

### AJ-1.02 · §15 y Tabla 3 · CONCRETA · 🔴 — declarar la brecha que motiva el bench propio (sin adelantar resultados)

> ✎ **2026-08-11 — reescrito por la regla de no-anacronismo** (mapa, regla 5). La
> versión anterior de este ajuste pedía meter en §15 el cruce con la evidencia propia
> (YOLOE recall 0,000; G2A live; keep-up del Sprint 2) — **datos de Etapa 4/5 que el
> §15, siendo Etapa 1, no puede conocer**. El cruce se hace en §17.5/§18 (`AJ-5.11`,
> `AJ-6.01`); acá queda solo lo que la literatura sostiene.

**Qué pasa hoy.** El §15 cataloga modelos por sus cifras COCO/LVIS y no deja escrita la
pregunta que esas cifras no responden: **¿predicen los benchmarks generales el
rendimiento sobre una condición de dominio específica?**

**Qué debe decir — y todo se sostiene con literatura, sin un solo número propio:**

- **ODinW**: GDINO-L cae de ~52 AP en COCO a **26,1 mean AP** sobre los 35 datasets de
  ODinW [P] — la referencia publicada de cuánto colapsa un OVD fuera de distribución.
- **Chen 2025** (arXiv:2508.11011): grounding con atributo/negación → **IoU <20%** [P]
  — la evidencia publicada de que la composición léxica fina no la resuelve el
  preentrenamiento.
- Conclusión que el §15 puede firmar en su tiempo narrativo: *los benchmarks generales
  no garantizan la condición de dominio, y no existe benchmark publicado del cruce
  OVD×EPP* (→ AJ-1.13) — **esa brecha es la que justifica que el protocolo (§17.1.9.2)
  exija baseline zero-shot propia y test congelado**.

**Dónde queda el resto:** la *confirmación medida* de esta brecha (el caso YOLOE:
35,9 AP LVIS publicado vs recall CR-01 = 0,000 acá; los G2A medidos en nuestro hardware
vs la columna Latencia derivada de la Tabla 3) es material de **§17.5**, escrito en tres
tiempos contra esta vara. El §15 planta la pregunta; el §17.5 la responde.

---

### AJ-1.03 · §15 · ERRATA · 🟠 — declarar el backbone de cada cifra de GDINO

El **52,5 AP COCO zero-shot corresponde a Swin-L**, y el informe no lo declara. Lo
desplegado en este trabajo es **Swin-T**, cuyo zero-shot COCO publicado es **≈48,4**
[S]. Regla a aplicar en todo el §15: **ninguna cifra de GDINO sin su backbone al lado.**

---

### AJ-1.04 a AJ-1.08 · erratas y precisiones verificables contra los papers

Se agrupan porque se corrigen en una sola pasada, todas contra fuente:

- **AJ-1.04** — OmDet-Turbo-Tiny aparece con "30,3 LVIS", que es un *mislabel* probable
  de **ODinW-13**; y el mismo modelo figura con **34,0 en una tabla y 34,7 en otra**.
- **AJ-1.05** — el **53,4 COCO** de OmDet-Turbo probablemente **no es zero-shot**;
  verificar y etiquetar.
- **AJ-1.06** — LLMDet "51,1–52,4": el **52,4 no tiene origen** rastreable.
- **AJ-1.07** — se afirma que el caching **"ahorra ≈40 ms"** en un modelo al que la
  misma tabla asigna **7,1 ms totales**. Es aritméticamente imposible.
- **AJ-1.08** — la **columna Latencia de la Tabla 3 es 1000/FPS**: es una derivación, no
  una medición. Declararlo en la nota de la tabla (y es la bisagra para introducir
  nuestras latencias medidas, AJ-1.02).

---

### AJ-1.09 · Anexo A / Tabla A.1 · ERRATA · 🟠 — la licencia de GDINO 1.5 y DINO-X

La Tabla A.1 las lista como **"Apache-2.0"**. Son **API cerrada sin pesos abiertos**:
lo Apache-2.0 es el **SDK**, no el modelo [S]. Es una errata con consecuencia — una
afirmación de licencia incorrecta en un anexo de comparación técnica es exactamente el
tipo de cosa que un jurado verifica.

---

### AJ-1.10 · Referencias · ERRATA · 🟡

Citas inconsistentes a lo largo del §15: **Liu 2023/2024** (misma obra, dos años),
**Minderer**, **Xiao**, **Lin 2014/2015**, **Ren a/b/c**. Unificar contra el listado de
referencias del `96e`.

---

### AJ-1.11 · §15 · CONCRETA · 🟡 — MM-Grounding-DINO

El informe **no trae ninguna cifra publicada** de MM-Grounding-DINO, siendo un candidato
de la misma familia. Publicadas: **tiny 50,4–50,6 COCO zero-shot / 35,7–41,4 LVIS**
[P/S]. **Al §15 va solo la cifra publicada** (es literatura); el descarte empírico del
proyecto (bboxes roto en MM-GDINO-tiny) es un resultado y se relata en §17.5 — pero sin
la cifra en el §15, ese relato posterior queda sin contexto.

---

### AJ-1.12 · §15 · PRECISA · 🟠 — la advertencia de métrica (la trampa del jurado)

Las cifras COCO/LVIS de los papers OVD son **AP promediado sobre IoU 0,50:0,95** (LVIS
además con protocolo *Fixed AP*). Los papers de EPP y nuestro bench reportan
**mAP@0,5**, que da numéricamente más alto para el mismo detector.

**Nunca poner las dos series en la misma columna.** El error previsible del jurado es
*"GDINO da 48–52 en COCO y ustedes 0,55 — rinde igual"*. No: en mAP@0,5 sobre COCO
estaría muy por encima; **nuestra caída es real y es el costo de dominio**. Esta
advertencia tiene que estar escrita en el informe, no solo entendida.

---

### AJ-1.13 · §15 · CONCRETA · 🟠 — la Vara 3: el cruce OVD×EPP

Es el hueco que el trabajo ocupa, y hay que decirlo con las tres piezas:

- **OWLv2 zero-shot sobre obra** (Choi & Greer 2024, arXiv:2410.12225): AP@IoU>0,5
  **0,649 hardhat** y **0,677 person** sobre 5.210 imágenes [P] — la **única** cifra
  publicada directamente comparable con nuestro AP@0,5 por clase.
- **VLMs con atributo/negación** (Chen 2025, arXiv:2508.11011): *"workers wearing white
  hard hats"* → **IoU <20%** [P] — la literatura confirma la "ceguera al atributo" de
  E-DIR que medimos.
- **No existe paper 2023–2026** con GDINO o YOLO-World zero-shot medido sobre
  SHEL5K/CHV, ni sobre un bench de EPP multi-fuente con protocolo COCO. **Esa es la
  brecha, y el §15 la deja declarada como brecha** — que `bench_v3` la ocupa es la
  lectura de §17.5/§18, no de acá (regla de no-anacronismo).

Las fuentes externas verificadas el 2026-08-06 están listadas al final de
`sintesis/resultados-y-conclusiones.md` §7.4 — reusar ese listado, no rearmarlo.

---

### AJ-1.14 · §15 · PRECISA · 🟠 — Abdalwhab 2025 está mal usado

El paper compara **YOLO11 fine-tuned vs OVD zero-shot** en componentes MEP. Eso es
**evidencia de brecha de vocabulario zero-shot**, no evidencia del efecto de ajustar un
OVD. Como está citado hoy, sostiene una conclusión que el paper no sostiene.

---

### AJ-1.15 · §15 → §17.5 · PRECISA · 🟠 — la regla de tres tiempos, y "adaptación"

**Regla de redacción** (fijada 2026-08-06): cada conclusión se escribe en tres tiempos —
*qué dice la literatura* (cifra de la Vara) → *qué medimos nosotros* (cifra de
`results/`) → *qué tipo de aporte queda*. **Nunca al revés**: empezar por el número
propio sin vara es exactamente lo que hoy le pasa al §15.

**Dónde opera la regla (no-anacronismo):** los tres tiempos se escriben **en §17.5 y
§18**, que sí conocen los resultados. El rol del §15 en esta regla es pasivo: dejar la
vara y la brecha listas para que el tercer capítulo las cite — **al §15 no entra ningún
número propio**.

**Y una precisión de vocabulario que hay que cuidar ante el jurado:** el núcleo medido
de la tesis **no adapta los pesos**. Adapta los modelos **operativamente**: resolución
(560), formulación del vocabulario (prompt sets congelados) y las capas de plataforma
alrededor (histéresis temporal, identidad por sujeto, política de alerta). **Medir
cuánto rinde ese stack de adaptación sin entrenar es la perspectiva nueva** — decirlo
así, y no "adaptamos los modelos". El fine-tuning (E-04) es una **rama experimental
aparte, comprometida como jornada (ADR-017)**: sus resultados, si existen a la entrega,
se rotulan como rama comparativa y nunca se funden con el núcleo zero-shot.

---

### AJ-1.16 · §16 Marco Teórico · EVIDENCIA · 🟡 — hueco declarado

**El §16 no fue relevado contra el estado actual del proyecto.** Todo el relevamiento
de Etapa 1 se concentró en el §15 y en el Anexo A. Antes de dar la etapa por cerrada
hay que pasar el §16 (`entregable/96d`) contra `sintesis/fundamentos-teoricos.md`, que
es la versión hoy vigente de la teoría del trabajo, y anotar acá lo que aparezca.

Esto es un hueco de relevamiento, **no** una afirmación de que el §16 esté bien.

---

## 4. 🚫 Lo que no hay que tocar en esta etapa

- **Las cifras ancla verificadas.** La verificación externa **confirmó** GDINO 52,5 AP
  COCO / 26,1 mean AP ODinW [P]; YOLO-World-L 35,4 AP LVIS @ 52 FPS [P]; YOLOE-v8-S/L
  27,9/35,9 AP LVIS @ 305,8/102,5 FPS T4-TensorRT [P/S]; GDINO 1.5 Pro 54,3/55,7 y Edge
  36,2 @ 75,2 FPS [S]. Están bien: lo que falta es el backbone (AJ-1.03) y el cruce
  (AJ-1.02).
- **La estructura del §15** (4 paradigmas · ~25 modelos · Tabla 3 · Tabla A.1) y los
  criterios de selección de §17.1.9.2, que fundan el par GDINO+YOLOE como polos del
  trade-off expresividad semántica ↔ latencia. El encuadre es correcto y sobrevive.

## 5. Fuentes

`sintesis/resultados-y-conclusiones.md` §7.1–§7.4 (relevamiento y verificación externa
del 2026-08-06, con el listado completo de arXiv/DOI consultados) ·
`sintesis/fundamentos-teoricos.md` · `entregable/96c`, `96d`, `96e` §19.1.

---

## Fuente: `docs/informe/entregable/borradores/vara-15.md`

> SHA-256 del bloque: `d82aac011a58729e9bf7aeae19bf8147734f7704b635b7140ec18d7c4ba0d496`  
> Seleccion: borrador historico (2026-08-16) de la vara del 15: YA INTEGRADO al texto base (AJ-1.01/1.02/1.13 estan aplicados). Material de consulta para las cifras y sus marcas de confianza, NO redactar desde aca.

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

## Fuente: `docs/informe/ajustes/07-critica-extension-y-poda.md`

> SHA-256 del bloque: `9c0b3b926be0d2b4353c0cbde4b308b556a269914460edb2c61f3eb1c046c3c6`  
> Seleccion: encuadre de la crítica de extension: la regla de gobierno (no hay limite de extension y no se poda por cuota, se poda por APORTE) y los cinco criterios C1 a C5 que cada PODA cita por su sigla. Sin esto, las fichas de poda no se pueden leer.

# Crítica de extensión — qué podar del informe, sección por sección

- **Fecha:** 2026-08-11
- **Qué es esto:** la crítica de **extensión** del informe v1.1, medida y sección por
  sección: qué eliminar porque **ya no se alinea con la plataforma que se construyó**, y
  qué comprimir porque **no suma** al argumento. No existía: el `93` audita *corrección*
  (26 redlines), `nucleo/historicos/02` auditó *contenido* de Etapa 3, y el "orden de
  sacrificio" del `95` era de redlines contra tiempo. Ninguno mide longitud.
- **Método:** conteo de palabras por sección sobre el texto extraído (`entregable/90`,
  `96a`–`96e`), contrastado contra lo que la plataforma **es** (E-IND · GDINO-560 ·
  dos planos servicios HTTP · bus ZeroMQ · bench_v3 · clip bench · sin fine-tuning ·
  sin métricas MOT · sin inferencia en borde · distribución como trabajo comprometido).
- **Serie de IDs: `PODA-nn`** (prefijo verificado libre). Ortogonal a `AJ-`/`R-`: un
  mismo pase por sección aplica los dos. Cada ítem lleva casilla de decisión, como el 93.
- **La decisión final es tuya**: esto propone; ninguna poda se aplica desde acá.

> **✅ Regla de gobierno fijada por el usuario (2026-08-11): no hay límite institucional
> de extensión, y no se poda por cuota — se poda por aporte.** *"Todo lo que tenemos que
> desarrollar tiene que sumar."* Consecuencias operativas:
> 1. **El filtro único es el aporte**: una sección se queda si sostiene un resultado,
>    una decisión de diseño o un argumento de defensa. Si no sostiene nada, no va — sin
>    importar cuánto costó escribirla.
> 2. **No existe "segunda vuelta" sobre §17.1.5/§17.1.7**: bajo este criterio no se
>    comprime prosa del protocolo ejercido para llegar a un número. Las 18 podas de este
>    documento se justifican todas por desalineación o no-aporte, ninguna por cuota.
> 3. **La misma vara gobierna lo que falta escribir**: §17.4, §17.5 y §17.6 se redactan
>    al largo que su contenido exige y ni una palabra más — los insumos ya están
>    inventariados (T-68…T-84, FIG-A…F), y relleno alrededor de una tabla verificable
>    es dilución, no desarrollo.

---

## 1. El diagnóstico en números

**El informe ya tiene ~127.000 palabras** (≈280+ páginas de cuerpo) **y las tres
secciones más importantes todavía no existen** (§17.4, §17.5, §17.6, que van a sumar
15–20k más). El problema no es solo estético: un tribunal que atraviesa 60 páginas de
surveys de tecnologías no usadas llega cansado a los resultados.

| Bloque | Palabras | % | Estado de alineación |
|---|---:|---:|---|
| §2–§14 frontmatter (`96a`) | 4.530 | 3,6% | OK — se corrige (AJ-0.x), no se poda |
| §15 Estado del Arte (`96c`) | 21.575 | 17,0% | **8.000 de streaming/servidores** para una decisión que colapsó |
| §16 Marco Teórico (`96d`) | 31.732 | 25,0% | **13.285 en §16.5** (transmisión/aceleración/arquitecturas/borde) |
| §17.1 Consolidación (`96b`) | 32.222 | 25,4% | protocolo ejercido (se queda) + **5.054 de catálogo de datasets** viejo |
| §17.3 Diseño (`90`) | 24.389 | 19,2% | lo opera el `93`; acá solo 2 ítems de longitud |
| §18–§19 + Referencias (`96e`) | 12.339 | 9,7% | anexos se completan; Anexo A pierde función |
| **Total escrito** | **≈126.800** | 100% | |

**El titular, y es uno solo:** los dos temas **más desalineados** con la plataforma
final están cubiertos **dos veces** — una en el estado del arte y otra en el marco
teórico:

- **MOT / seguimiento multiobjeto:** §15.3 (2.484) + §16.4 (2.769) = **5.253 palabras**
  — para un proyecto que **excluyó las métricas MOT** (E-10, con fundamento medido:
  F-89.1, las detecciones son bit a bit las mismas) y cuya ganancia por sujeto se mide
  en la métrica de la plataforma, no en MOTA/IDF1.
- **Streaming / arquitecturas de video / borde:** §15.4 (7.998) + §16.5.3–16.5.5
  (8.009) = **16.007 palabras** — para una plataforma cuyo espacio de decisión colapsó a
  *"RTSP de entrada, bus ZeroMQ adentro, archivo como verdad"*, que usa mediamtx solo
  como herramienta de desarrollo, y que **excluyó la inferencia en borde** (EN-3; lo
  ejercido es el prefilter EN-2).

Juntos: **~21.200 palabras — el 17% del informe — dedicadas a los dos temas que menos
sostienen el trabajo.** Mientras tanto, el §15 no tiene ni una cifra de la vara
supervisada de EPP (`AJ-1.01`, el hueco que sí importa).

---

## 2. Los cinco criterios de poda

| # | Criterio | Acción |
|---|---|---|
| C1 | **Desalineado**: describe una capacidad/tecnología que la plataforma final no usa, excluyó o refutó | ELIMINAR o comprimir a decisión declarada |
| C2 | **Espacio de decisión colapsado**: survey amplio de opciones cuando la decisión final fue una y está justificada en una página | COMPRIMIR al camino tomado + por qué |
| C3 | **Doble cobertura**: el mismo tema desarrollado en §15 y §16 (o §16 y §17.1) | FUSIONAR — una sola casa por tema |
| C4 | **Meta-texto**: secciones que resumen, anticipan o "proyectan" otras secciones del mismo documento | ELIMINAR — el índice ya hace ese trabajo |
| C5 | **Catálogo sin uso posterior**: listas/tablas de ítems que ninguna sección vuelve a citar | COMPRIMIR a los ítems con rol en el trabajo |

**Regla de honestidad (no negociable, `gobierno/97` §3):** lo **pre-registrado y no
ejercido no se borra en silencio** — se comprime a decisión declarada con su causa y su
costo (caso testigo histórico: el fine-tuning E-04 mientras estuvo no ejercido, con su
costo T1 por extrapolación medida: ≈16 min centrales (prudente 30–45 min; walltime
2 h) — `operacion/100` adenda; la cifra histórica “≈1 GPU-h” quedó superada. ✎
2026-08-11: E-04 es hoy **jornada comprometida** — ADR-017 — y el
ejemplo vigente de la regla pasa a ser kappa/doble anotación, L2). Podar no es ocultar.

---

---

## Fuente: `docs/informe/ajustes/07-critica-extension-y-poda.md`

> SHA-256 del bloque: `dff0978660e1e7ef4cda6d3a620d38c9774e9a4a2d396f06e270df2fff846c59`  
> Seleccion: podas 01 a 11 aplicables a las secciones 15 y 16: YA APLICADAS Y VERIFICADAS (etapa 1 CERRADA 2026-08-28) - se conservan solo como criterio de lectura, NO reaplicar. Dos enmiendas del pase de alineacion: la poda 04 se aplica CON la excepcion E1-10 (el parrafo de RTSP/RTP y la seccion 15.4.3 completa se conservan) y la poda 03 CON el matiz E1-08 (las metricas MOT se comprimen, no se eliminan).

## 3. §15 Estado del Arte (21.575 palabras)

> ✎ **2026-08-28 — estado del tablero de podas (`00-el-informe-hoy` 08-28; `operacion/130` §5 /
> `docs-set.md` #30):** **PODA-01…11 APLICADAS el 2026-08-27** en §15/§16 **v1.0** (22.266 →
> 10.870 palabras, con las enmiendas E1-10/E1-08) — marcadas abajo. **PODA-12…14** (§17.1)
> esperan el pase de la **Etapa 2**, que arranca (PODA-14 acotada por D-E2-8: sólo recorta
> §17.1.4 y verifica que lo recortado esté en B.1–B.7). **PODA-15/16** (§17.3) pendientes
> con causa. **PODA-17/18**: el Anexo A y las referencias salieron del entregable a `90e`
> (decisión del usuario 08-27), donde se resuelven para el equipo.

### PODA-01 · §15.2.1 Paradigmas y modelos (4.530) · C5 · 🟠
El catálogo trae **~25 modelos con cifras COCO/LVIS**; el trabajo evaluó **tres familias**
(GDINO, MM-GDINO, YOLOE) y tiene **un** comparable externo (OWLv2). Comprimir a: los 4
paradigmas en un párrafo cada uno + ficha solo de los modelos con rol en el trabajo
(GDINO/MM-GDINO/YOLO-World/YOLOE/OWLv2 · GDINO 1.5/DINO-X como techo de API cerrada) +
la Tabla 3 reducida a esas filas. Beneficio doble: **menos superficie de erratas** — las
AJ-1.04…08 viven justo en las filas que se van (OmDet-Turbo, LLMDet, el caching de 40 ms).
**Ahorro: ~2.000** · DECISIÓN → [x] ✎ 2026-08-28: APLICADA el 2026-08-27 en §15/§16 v1.0 (`00-el-informe-hoy`) · [ ] acepto [ ] modifico [ ] rechazo

### PODA-02 · §15.2.4 Ventajas/limitaciones/trade-offs (2.764) · C3/C4 · 🟠
Solapa con §15.2.3 (síntesis comparativa, 1.153) y con §16.7. Fusionar 15.2.3+15.2.4 en
una sola síntesis de ~1.200 con tabla. **Ahorro: ~1.500** · DECISIÓN → [x] ✎ 2026-08-28: APLICADA el 2026-08-27 en §15/§16 v1.0 (`00-el-informe-hoy`) · [ ]

### PODA-03 · §15.3 MOT completo (2.484) · C1 · 🟠
La plataforma **no evalúa MOT**: E-10 excluye MOTA/IDF1 con causa medida, y el tracker
que existe se mide por alertas. Mantener ~800: tracking-by-detection en un párrafo (es lo
que fundamenta G1) + la brecha. **Eliminar §15.3.3 entero** (métricas MOT, 385 — no se
usa ni una) y podar el catálogo de métodos (§15.3.1–15.3.2) a los dos que expliquen el
approach del tracker propio. **Ahorro: ~1.600** · DECISIÓN → [x] ✎ 2026-08-28: APLICADA el 2026-08-27 en §15/§16 v1.0 (`00-el-informe-hoy`) · [ ]

### PODA-04 · §15.4 Streaming y servidores de medios (7.998) · C1/C2 · 🔴 la mayor
**La sección más desalineada del informe.** 4.041 palabras de protocolos (WebRTC, HLS,
SRT, …) + 2.594 de comparativa de servidores de medios open source + criterios — y la
decisión final fue: **RTSP como ingesta, ZeroMQ+msgpack como bus interno (ADR-003),
mediamtx solo como herramienta de desarrollo, archivo JSONL como verdad**. Ni WebRTC ni
HLS ni la comparativa de servidores sostienen una sola decisión del sistema construido.
Comprimir a ~1.200: panorama mínimo de protocolos de **ingesta** + la brecha
streaming×OVD (§15.4.3, que sí vale). La *justificación de la decisión tomada*
(RTSP en la entrada, bus de eventos adentro) no va acá: es material de §17.1/§17.3
(regla de no-anacronismo — el §15 no relata elecciones del proyecto).
**Ahorro: ~6.800** · DECISIÓN → [x] ✎ 2026-08-28: APLICADA el 2026-08-27 en §15/§16 v1.0 (`00-el-informe-hoy`) · [ ]

**Lo que el §15 GANA mientras pierde esto:** la vara supervisada (AJ-1.01), el cruce con
la evidencia propia (AJ-1.02) y la Vara 3 OVD×EPP (AJ-1.13). La poda no deja al §15 más
flaco de contenido útil — lo deja con el contenido que la defensa necesita.

---

## 4. §16 Marco Teórico (31.732 palabras)

### Lo que NO se toca (y por qué)
- **§16.3 Percepción visión-lenguaje (2.594)** — es el **corazón conceptual de la
  tesis** (el lenguaje como especificación dinámica; sostiene AF-2/AF-5 y toda la
  narrativa léxico-conceptual). Intacta.
- **§16.2 Condiciones de riesgo observables (3.100)** — es lo que ancla CR-01/CR-02 a la
  normativa; sin esto las condiciones son arbitrarias. A lo sumo podar §16.2.3 (~300).
- **§16.5.1 Latencia end-to-end como restricción (494)** — el eje de tiempo real ES
  central a los resultados (G2A, densidad live). La poda de §16.5 es de *surveys*, no
  del concepto.

### PODA-05 · §16.4 MOT teórico (2.769) · C1/C3 · 🟠
Segunda casa del MOT. Mantener §16.4.1 (la limitación del fotograma — motiva la
histéresis) y §16.4.3 (integración OVD+tracking — motiva G1); comprimir §16.4.2
(fundamentos MOT, 1.600 → ~700) y **eliminar §16.4.4** (criterios de selección de
métodos MOT, 487 — no hubo selección de método de catálogo). **Ahorro: ~1.400** ·
DECISIÓN → [x] ✎ 2026-08-28: APLICADA el 2026-08-27 en §15/§16 v1.0 (`00-el-informe-hoy`) · [ ]

### PODA-06 · §16.5.2 Descomposición del pipeline (4.874) · C3 · 🔴
Mantener lo que **define G2A y sus componentes** (t_capture/t_transport/t_preprocess/
t_inference — es vocabulario que §17.1.7 y los resultados usan): ~1.400. El resto
duplica lo que §17.1.7 ya formaliza como framework de métricas. **Ahorro: ~3.400** ·
DECISIÓN → [x] ✎ 2026-08-28: APLICADA el 2026-08-27 en §15/§16 v1.0 (`00-el-informe-hoy`) · [ ]

### PODA-07 · §16.5.3 Arquitecturas de procesamiento de video (3.594) · C1/C2 · 🔴
Survey de frameworks/arquitecturas de video analytics — y la plataforma es **un pipeline
Python propio de dos servicios config-driven**. Comprimir a ~600: el patrón
productor/consumidor como fundamento conceptual; la elección concreta (pipeline propio,
no framework) se justifica en §17.3, no en el marco teórico. **Ahorro: ~3.000** ·
DECISIÓN → [x] ✎ 2026-08-28: APLICADA el 2026-08-27 en §15/§16 v1.0 (`00-el-informe-hoy`) · [ ]

### PODA-08 · §16.5.4 Computación en el borde (2.729) · C1 · 🔴
**EN-3 (inferencia en borde) está excluida.** Lo ejercido es el prefilter EN-2 on-device
(87% de descarte medido) y la OAK-D como fuente. Comprimir a ~700: el fundamento
**conceptual** del prefiltrado en el borde; la decisión de dónde vive la inferencia (y su
resultado medido) pertenecen a §17.3 y §17.5. **Ahorro: ~2.000** · DECISIÓN → [x] ✎ 2026-08-28: APLICADA el 2026-08-27 en §15/§16 v1.0 (`00-el-informe-hoy`) · [ ]

### PODA-09 · §16.5.5 Criterios para protocolos y stacks de streaming (1.686) · C2 · 🔴
Criterios de selección para una selección que ya ocurrió y colapsó (ver PODA-04). Un
párrafo puente a la decisión tomada. **Ahorro: ~1.400** · DECISIÓN → [x] ✎ 2026-08-28: APLICADA el 2026-08-27 en §15/§16 v1.0 (`00-el-informe-hoy`) · [ ]

### PODA-10 · §16.6 Marco ético-legal (4.364) · C5 parcial · 🟠
Tiene núcleo vivo: §16.6.2 (delimitación del tratamiento de datos — **implementada** en
§17.3.12, minimización de evidencia visual) y §16.6.6 (implicaciones de diseño). Podar lo
genérico: §16.6.4 referentes comparados (422), §16.6.5 gobernanza de IA (499), y
comprimir §16.6.7 (955 → ~400). **Ahorro: ~1.400** · DECISIÓN → [x] ✎ 2026-08-28: APLICADA el 2026-08-27 en §15/§16 v1.0 (`00-el-informe-hoy`) · [ ]

### PODA-11 · §16.7 Convergencias y brechas transversales (4.429) · C4 · 🔴
**Meta-texto puro**: seis subsecciones que re-resumen el propio §16 y anticipan §17.1
("convergencias del análisis", "lectura arquitectónica integrada", "proyección hacia la
consolidación"). El lector ya leyó el §16 y va a leer el §17.1; este puente de 4.400
palabras no aporta contenido nuevo. Fusionar con §16.8 en un cierre único de ~1.000
(el mapa de brechas de §16.7.3 es lo único que se rescata, comprimido). **Ahorro:
~3.400** · DECISIÓN → [x] ✎ 2026-08-28: APLICADA el 2026-08-27 en §15/§16 v1.0 (`00-el-informe-hoy`) · [ ]

---

---

## Fuente: `docs/informe/ajustes/07-critica-extension-y-poda.md`

> SHA-256 del bloque: `44cc87962e89066323feb695800b7b2c3c61a1fa07ff69bb42b3e58abafc900a`  
> Seleccion: de este bloque, a la etapa 1 le tocan la poda 17 (Anexo A, que es su tercera pieza: decision D-E1-4) y la poda 18 (Referencias, que se poda sola al caer secciones y con el pase de AJ-1.10); las demas son de otras etapas. Incluye ademas el tablero completo y, sobre todo, los GUARDRAILS: su punto 1 protege 16.2 y 16.3 —el corazon conceptual de la tesis— de las podas 05 a 11, y su punto 6 fija que las adiciones de vara mandan sobre las podas (la poda les hace lugar, no compite con ellas).

## 7. §18, §19 y Referencias (12.339 palabras)

### PODA-17 · §19.1 Anexo A — comparativas técnicas (749) · C3 · 🟡
Con la vara supervisada dentro del §15 (AJ-1.01/1.13), el anexo de "estado del arte
complementario" pierde su función. Rescatar lo vivo (la Tabla A.1 con las licencias
**corregidas** — AJ-1.09) hacia §15 o Anexo B, y eliminar el resto. **Ahorro: ~500** ·
DECISIÓN → [ ]

### PODA-18 · Referencias (5.886) · consecuencia · 🟡
Se poda sola al caer las secciones (los ~25 modelos, los protocolos, los servidores de
medios arrastran decenas de entradas), y el pase de AJ-1.10 unifica duplicados
(Liu 2023/2024, Lin 2014/2015, Ren a/b/c). **Ahorro estimado: ~800** · DECISIÓN → [ ]

**Anexos B/C/D: no se podan** — son el destino natural de lo que sale del cuerpo
(PODA-14) y del anexo de reproducibilidad (`AJ-6.02`).

---

## 8. Tablero de poda

| ID | Sección | Hoy | Acción | Ahorro | Pri |
|---|---|---:|---|---:|---|
| PODA-01 | §15.2.1 catálogo de modelos | 4.530 | comprimir a modelos con rol | ~2.000 | 🟠 |
| PODA-02 | §15.2.3+.4 síntesis duplicada | 3.917 | fusionar en una | ~1.500 | 🟠 |
| PODA-03 | §15.3 MOT | 2.484 | comprimir; eliminar métricas MOT | ~1.600 | 🟠 |
| PODA-04 | §15.4 streaming/servidores | 7.998 | **comprimir a decisión tomada** | **~6.800** | 🔴 |
| PODA-05 | §16.4 MOT teórico | 2.769 | mantener lo que motiva G1/histéresis | ~1.400 | 🟠 |
| PODA-06 | §16.5.2 pipeline | 4.874 | mantener solo definición de G2A | ~3.400 | 🔴 |
| PODA-07 | §16.5.3 arquitecturas de video | 3.594 | comprimir a patrón usado | ~3.000 | 🔴 |
| PODA-08 | §16.5.4 borde | 2.729 | comprimir a EN-2 + exclusión EN-3 | ~2.000 | 🔴 |
| PODA-09 | §16.5.5 criterios streaming | 1.686 | párrafo puente | ~1.400 | 🔴 |
| PODA-10 | §16.6 ético-legal | 4.364 | podar genérico, mantener lo implementado | ~1.400 | 🟠 |
| PODA-11 | §16.7 convergencias | 4.429 | **fusionar con 16.8, es meta-texto** | ~3.400 | 🔴 |
| PODA-12 | §17.1.6.2 catálogo datasets | 5.054 | comprimir a usados + descartes (con R-24) | ~3.000 | 🔴 |
| PODA-13 | §17.1.10 proyección | 637 | párrafo puente | ~450 | 🟡 |
| PODA-14 | §17.1.4 infra | 3.252 | detalle al Anexo B | ~1.000 | 🟡 |
| PODA-15 | §17.3.15 roles | 1.319 | con R-17: tabla, no prosa | ~700 | 🟡 |
| PODA-16 | §17.3.17 backlog | 1.101 | con R-21: estado final | ~500 | 🟡 |
| PODA-17 | §19.1 Anexo A | 749 | eliminar tras AJ-1.01/1.09 | ~500 | 🟡 |
| PODA-18 | Referencias | 5.886 | consecuencia + AJ-1.10 | ~800 | 🟡 |
| **Total** | | | | **~34.900 (~27%)** | |

**Resultado esperado (consecuencia, no meta):** de ~127k a **~92k escritas**; con
§17.4/§17.5/§17.6 sumadas (15–20k), el informe final queda en ~110k en lugar de ~145k.
✎ 2026-08-11 — **no hay objetivo numérico** (regla de gobierno del encabezado): estas
cifras miden el efecto de podar lo que no aporta, no un tope a alcanzar. No hay segunda
vuelta sobre §17.1.5/§17.1.7.

**Orden recomendado:** los ocho 🔴 primero (son el 65% del ahorro y tienen el riesgo
argumental más bajo: nada de lo que eliminan sostiene un resultado ni un argumento de
defensa). Los 🟠 en el pase de cada sección junto a sus AJ-. Los 🟡 al final.

---

## 9. Guardrails — lo que esta crítica NO autoriza a tocar

1. **§16.3** (visión-lenguaje) y **§16.2** (normativa→condiciones): el corazón
   conceptual y el ancla de CR-01/CR-02.
2. **§17.1.5 y §17.1.7**: el protocolo ejercido y el framework de métricas — son la
   columna vertebral metodológica que §17.5 va a citar.
3. **La latencia como restricción** (§16.5.1) y la definición de G2A: el eje de tiempo
   real es un resultado central, no un survey.
4. **Nada pre-registrado se borra en silencio**: fine-tuning, kappa, TN — se comprimen a
   decisión declarada con causa (regla `97` §3; los textos de declaración ya existen:
   `94` §8, AJ-2.06, AJ-2.11). (✎ 2026-08-11: el fine-tuning dejó de ser caso
   "no ejercido" — ADR-017 lo compromete como jornada; `94` §8 y AJ-2.11 ya están
   reescritos con ese encuadre.)
5. **Ningún texto que un redline necesita como ancla**: antes de eliminar un párrafo de
   §17.3, verificar que ningún R-xx lo cita como "DICE HOY".
6. **Las adiciones mandan sobre las podas**: AJ-1.01/1.02/1.13 (la vara y el cruce)
   *agregan* al §15 — la poda les hace lugar, no compite con ellas.

## 10. Fuentes

Conteos: medidos el 2026-08-11 sobre `entregable/90` y `96a`–`96e` (por encabezado,
`wc -w` por sección). Alineación: `nucleo/10` (exclusiones E-01…E-13) · ADR-002/003/015/016 ·
`nucleo/14`–`19` (los relevamientos vigentes) · `operacion/97` (la plataforma verificada) ·
`sintesis/resultados-y-conclusiones.md` §7 (lo que el §15 debe ganar) ·
`material-etapa-3/93` (los redlines con los que esta poda se coordina).

---

## Fuente: `docs/sintesis/fundamentos-teoricos.md`

> SHA-256 del bloque: `3262cdc570ee5c9bfbde7f01eea642bf6b90790d7155698d31cf1317aa28de02`  
> Seleccion: documento completo.

# Fundamentos teóricos — entender la plataforma y sus resultados de punta a punta

- **Fecha:** 2026-08-06 · **Rol:** documento de estudio, **100% teórico-conceptual**.
- **Para qué existe:** poder explicar ante el jurado *qué* se construyó, *por qué* se
  construyó así, *cómo* se midió y *por qué* los resultados dan lo que dan. Cada
  sección desarrolla la teoría mínima y la conecta con la decisión o el resultado
  concreto del proyecto.
- **Compañeros de lectura:** los números viven en
  `resultados-y-conclusiones.md` (fuente: `docs/sintesis/resultados-y-conclusiones.md`) (mismo directorio) y
  en los 4 índices de `e-ovrt_experimental-setup/results/`; las siglas, en el
  glosario (`docs/13`). Acá no hay cifras nuevas: hay **conceptos**.

> ✎ **2026-08-12 — puesto al día al mundo post-estrato-B. Leer esto antes que el cuerpo.**
> Este documento se escribió el **2026-08-06**, o sea **antes** del cierre del lote de
> internet y de la **revisión ciega del GT** (`operacion/109`–`113`). Los conceptos no se
> movieron —es lo que se esperaba de un documento teórico—, pero **tres estados sí**, y las
> tres correcciones ya están aplicadas en el cuerpo:
>
> | Decía | Vigente |
> |---|---|
> | El clip bench es de **34 clips** | **47 clips** = 32 positivos / 15 negativos / **37 episodios**, en dos bloques: **A** rodaje guionado (34) y **B** lote de obra real (13). Los denominadores de 34 siguen siendo correctos **cuando se dicen del Bloque A** |
> | **FAR/hora NO es métrica de este trabajo** | **Se mide y se reporta**, pero **no sostiene una cota** (limitación **L1**). Desde el 08-07 el banco tiene un clip de soak, así que la tasa **es computable** — y sigue faltando ~un orden de magnitud de exposición para afirmar nada operativo |
> | **L4 la levanta el lote de internet** | **L4 se precisó, no se levantó** (D-113.1, firmada): hay medición en obra real no guionada, y su aporte es **caracterizar dónde el sistema deja de ser evaluable**, no validarlo sobre obra real |
>
> Estas tres son, literalmente, tres de las siete trampas de `GUIA-REDACTORES.md` §4. Si
> encontrás una cuarta formulación vieja acá, gana el banner y hay que corregir el cuerpo.

---

## Parte I — El problema y el enfoque

### 1. El problema: condiciones de riesgo en obra, expresadas como percepción + tiempo

La seguridad en construcción tiene reglas del tipo *"ninguna persona debe permanecer
sin casco en la zona de trabajo"*. Una regla así tiene **dos mitades**:

1. **Una mitad perceptiva** — ver personas y ver (o no ver) su equipo de protección
   personal (EPP) en la imagen. Es un problema de **detección de objetos**.
2. **Una mitad temporal** — "permanecer": una condición de riesgo no es un frame, es
   un **estado que se sostiene en el tiempo**. Un casco que desaparece un frame por
   oclusión no es una infracción; una persona 10 segundos sin casco, sí.

El proyecto operacionaliza dos condiciones del catálogo del informe:
**CR-01 = persona sin casco** (severidad alta) y **CR-02 = persona sin chaleco
reflectante** (severidad media). Todo lo demás del catálogo (reglas espaciales,
zonas, maquinaria) quedó excluido con registro formal (doc 10).

La consecuencia arquitectónica de las dos mitades es la decisión más importante del
diseño: **separar el plano que percibe del plano que decide** (§10).

### 2. Detección de objetos: de vocabulario cerrado a vocabulario abierto

**Detección clásica (closed-set).** Un detector tradicional (Faster R-CNN, YOLO)
aprende un conjunto **fijo** de clases: la última capa es un clasificador con N
salidas, una por clase del dataset de entrenamiento. Detecta "casco" solo si fue
entrenado con miles de cascos anotados. Agregar una clase nueva = **re-anotar y
re-entrenar**.

**Detección open-vocabulary (OVD).** Un detector OVD reemplaza el clasificador fijo
por una **comparación entre embeddings**: el modelo proyecta cada región de la imagen
y cada **texto** (el *prompt*) a un mismo espacio vectorial, y una región "es" la
clase cuyo texto tiene mayor similitud. Las clases dejan de estar horneadas en los
pesos: **son un parámetro de entrada en lenguaje natural**. Esto viene de la línea de
modelos visión-lenguaje entrenados contrastivamente (la idea de CLIP: acercar en el
espacio de embeddings las imágenes y sus descripciones) llevada a detección
(*grounding*: no solo decir qué hay, sino **dónde** está lo que el texto nombra).

**Zero-shot** significa usar el modelo **sin ningún entrenamiento adicional** sobre
el dominio propio: se le da la imagen de obra y el texto "person. helmet. vest." y se
mide qué devuelve. Todo el trabajo experimental del proyecto es zero-shot — esa es la
pregunta de la tesis (§4).

**El trade-off estructural:** lo que se gana en flexibilidad se paga en dos monedas —
(a) **exactitud sobre clases raras o finas** (un detector cerrado entrenado con miles
de "bare heads" le gana a uno abierto que nunca vio el dominio), y (b) **costo
computacional** (procesar texto e imagen juntos es más caro que un clasificador
fijo). Los resultados del proyecto son, en buena parte, la **medición honesta de ese
trade-off**.

### 3. Los modelos concretos

**Grounding DINO (GDINO)** — el caballo de batalla del proyecto. Arquitectura
conceptual:

- Un **backbone visual** tipo transformer (Swin) extrae features multi-escala de la
  imagen; un **encoder de texto** tipo BERT procesa el *caption* (la lista de clases
  concatenada: `"person. helmet. vest."`).
- Un módulo de **fusión cross-modal** hace que las features de imagen "miren" al
  texto y viceversa (atención cruzada), de modo que la representación visual ya está
  condicionada por lo que se busca.
- La selección de queries del decoder está **guiada por el lenguaje**: el modelo
  propone regiones candidatas relevantes *para ese texto*.
- La salida son **cajas + un score de similitud contra los tokens/frases del
  caption**: umbralizar ese score da las detecciones por clase.

Variantes usadas: `tiny` (backbone chico, más rápido) y `base` (más grande, mejor en
clases difíciles). El sufijo `-560` es la **resolución de entrada** (560 px en vez de
800): menos píxeles ⇒ menos tokens visuales ⇒ menos cómputo. El hallazgo de la Fase S
fue que 560 px da −24% de latencia con igual o mejor mAP — la información que las
condiciones necesitan sobrevive a la resolución menor.

**YOLOE** — el otro polo del trade-off: una familia YOLO (one-stage, tiempo real) con
vocabulario abierto vía embeddings de texto pre-computables (y prompts visuales). Al
poder pre-computar el embedding de las clases, en inferencia corre casi como un YOLO
cerrado (~43 ms). El resultado del proyecto: es **rápido pero ciego a `bare_head`**
(AP 0,000), la clase que sostiene CR-01 — el ejemplo perfecto de que "entra en el
presupuesto de latencia" no sirve si no ve la condición (F-RT2).

**MM-Grounding-DINO** — reimplementación de GDINO del ecosistema MMDetection; quedó
descartada en dos pasos (tiny con cajas degeneradas; large con mAP 0,017).

**Por qué importa la elección por *variante* y no solo por familia:** el proyecto no
compara "GDINO vs YOLO" en abstracto; congela una **combinación** concreta (modelo +
resolución + prompt set + umbrales) y la mide. El "campeón" (`gdino-tiny-560`) y el
"especialista" (`gdino-base-560`) son variantes de la misma familia con roles
distintos medidos por estrato.

### 4. Qué defiende la tesis (y qué NO)

**La tesis NO es "OVD detecta mejor que un modelo cerrado".** Esa afirmación es
indefendible (un detector cerrado bien entrenado en el dominio gana en su clase) y no
es la pregunta. La tesis es:

> Una **plataforma** donde las condiciones de riesgo se expresan **en lenguaje**
> permite (a) **medir** qué se logra hoy sin entrenar, con qué latencia y bajo qué
> límites — declarados, no disimulados —, y (b) **extender** el sistema a condiciones
> nuevas por configuración, en minutos, sin re-anotar ni re-entrenar.

De ahí los dos tipos de resultado: los **números del banco** (qué se logra hoy: F1
0,789 núcleo / 0,930 con identidad) y el **número de extensibilidad** (A1: una clase
jamás configurada, con AP mejor que el agregado, en 9 minutos y 48 líneas de YAML —
con el contrapeso F-94.1: la palabra hay que validarla contra la taxonomía). El
contraste entre combinaciones **es** el experimento; ningún número es una nota de
aprobación.

---

## Parte II — Del píxel a la alerta: la cadena conceptual

### 5. Los tres niveles de medición

El error clásico es medir todo junto. El proyecto separa **tres niveles**, cada uno
con su GT y su métrica, porque responden preguntas distintas:

| Nivel | Unidad | Pregunta | Métrica | Banco |
|---|---|---|---|---|
| **Imagen** (percepción espacial) | caja | ¿el detector ve personas/EPP? | AP@0.5, mAP50, recall | `bench_v3` (6.477 imgs) |
| **Persona** (Nivel A) | persona-estado | ¿esta persona está "sin casco"? | P/R/F1 por violador | `person_gt` (atributos `has_helmet`/`has_vest`) |
| **Alerta** (Nivel B) | episodio temporal | ¿la plataforma alertó cuando y donde debía? | recall/precision/F1 de episodios, t_alert, TTFD, SDR | clip bench (**47 clips**, GT temporal humano: 34 del rodaje + 13 de obra real) |

La lógica de la cadena: un modelo puede ver bien (nivel imagen) y aun así razonar mal
el estado (nivel persona); y un estado bien razonado puede producir malas alertas si
el motor temporal se equivoca (nivel alerta). **Cada capa se aísla para poder
atribuir el error** — y la atribución es lo que hace defendibles las conclusiones
(p. ej.: la ganancia de G1 es 100% del motor porque las detecciones son idénticas).

### 6. El prompt como interfaz: las estrategias de formulación

En OVD el prompt no es cosmético: **es la especificación ejecutable de la
condición**. El experimento D1 (la única dimensión empírica del tablero de
decisiones) compara dos filosofías:

- **E-IND (indirecta):** pedirle al modelo solo **evidencia positiva** — `person`,
  `helmet`, `vest` — y razonar la **ausencia** por geometría (§7). El modelo hace lo
  que mejor sabe (detectar cosas que existen); la negación la pone el sistema.
- **E-DIR (directa):** pedirle la **infracción como frase** — "person without
  helmet", "worker with bare head" — en tres ejes de formulación: negación
  sintáctica, especificidad, estado observable.
- **E-HYB (híbrida):** correr ambas y fusionar (unión `or` / corroboración `and`,
  con gating por persona).

**Por qué era esperable que E-DIR sufriera (y por qué había que medirlo igual):** los
encoders de texto entrenados contrastivamente tienden a comportarse como "bolsa de
palabras": la representación de *"person **without** helmet"* queda dominada por
"person" y "helmet", y el modificador de negación pesa poco. El resultado empírico
lo confirmó con mecanismo: la falla dominante de E-DIR es la **ceguera al atributo**
(54% de sus FP) — devuelve cajas de "person without helmet" sobre personas **con**
casco. No es que no vea: es que **la frase no significa para el modelo lo que
significa para nosotros**.

Dos matices que los resultados obligan a sostener:

- **E-DIR no es un detector, pero es un recuperador (F-83.6):** recupera ~18,5% de lo
  que E-IND no ve, a costo de precisión. Por eso la fusión era una hipótesis
  razonable — y por eso su refutación (F-87.2, §20) es un hallazgo y no un descuido.
- **Lo que manda es la formulación, no el mecanismo (F-88.3):** la etiqueta corta
  (`helmet`) activa mejor el encoder que la frase compuesta ("safety helmet") — de
  ahí el prompt set congelado `cr01_cr02_v2_short`. Y B1 mostró que hasta el
  vocabulario "nativo" (`bare_head` como clase directa, que `shel5k` anota) rinde
  menos que la ausencia espacial sobre las mismas detecciones.

### 7. Inferencia espacial de ausencia: cómo se razona "sin casco" sin pedir "sin casco"

E-IND operacionalizada (evaluador `spatial_absence` del control-plane): para cada
**persona** detectada se define una **región anatómica esperada** del EPP, por
proporciones de la caja de la persona:

- CR-01: región `upper_body` — la franja superior de la caja (0–45% del alto, con
  margen lateral del 12%): ahí debería haber un `helmet`.
- CR-02: región `torso` — la franja media (25–85% del alto, margen 8%): ahí debería
  haber un `vest`.

La regla: si hay una persona con confianza ≥0,35 y área ≥400 px², y **ninguna**
detección del EPP con confianza ≥0,25 cae en su región ⇒ esa persona está **en
evidencia de infracción** en ese frame. Los umbrales bajos para el EPP son
deliberados: para *descartar* una infracción alcanza evidencia débil del casco (es
mejor perdonar de más a nivel frame — el filtro fuerte lo pone el tiempo, §8).

Este razonamiento geométrico es la mitad "sistema" de E-IND: convierte detecciones
(qué hay y dónde) en **estados por frame** (quién está sin qué). Es simple a
propósito: 2D, por proporciones, sin pose — sus límites (personas agachadas,
oclusiones) los absorbe la capa temporal o quedan declarados.

### 8. El motor de patrones temporal: la histéresis como filtro de verdad

El estado por frame es ruidoso: la percepción **parpadea** (un chaleco se detecta 1
de cada 6 frames; un casco desaparece al agacharse). El motor de patrones convierte
ese parpadeo en decisiones estables con una **máquina de estados con histéresis**,
por patrón y por clave de granularidad:

```
inactive → candidate → confirmed → sustained → resolved
```

- **inactive → candidate:** aparece evidencia de infracción.
- **candidate → confirmed:** la evidencia se **sostiene** `confirm_after_ms`
  (CR-01: 4.000 ms; CR-02: 7.000 ms — más tiempo porque la percepción de chaleco es
  más ruidosa). Al confirmar, se **emite la alerta**.
- **confirmed/sustained → resolved:** la evidencia **falta** durante
  `resolve_after_ms` (2.000/3.000 ms). Ojo con la asimetría: no hace falta evidencia
  continua para sostener — hace falta que los **huecos** sean menores que la ventana
  de resolución.

Esa asimetría es la clave teórica de dos resultados:

- **F-81.1 (el rescate):** una percepción con SDR 0,281 (evidencia en ~1 de cada 6
  frames) igual confirma 7/7 episodios de CR-02, porque los huecos entre detecciones
  son más cortos que `resolve_after_ms`. La histéresis **integra** evidencia
  intermitente. El precio es tiempo: t_alert sube.
- **F-RT2 (el límite):** el mismo mecanismo exige que los huecos sean < ventana. Un
  modelo rápido pero con detecciones muy espaciadas (YOLOE) no llega a confirmar:
  entra en presupuesto de latencia y no sirve para la condición.

**Decisiones de frontera que hay que poder explicar:**

- **El motor emite en CADA confirmación (ADR-011).** Si una condición se resuelve y
  reaparece, hay una alerta nueva (`re_alert`). La supresión/cooldown/agrupación es
  **política de notificación** del distribuidor —no del motor—; por eso el evaluador
  cuenta los `re_alerts` aparte y **no** los castiga como FP. El distribuidor aplica y
  registra esa política en el tramo mínimo verificado por spec 45.
- **Sin memoria de cobertura bajo G0 (ADR-012):** recordar "esta persona tenía casco
  hace 3 s" exige identidad; bajo escena no la hay, y la histéresis subsume el
  parpadeo. Decisión falsable por test — la falsación se corrió y quedó superada.

### 9. Granularidad: por qué "por sujeto" cambia todo sin cambiar la percepción

**G0 (escena):** el estado del patrón se indexa por `(pattern_id, source_id)` — hay
**un solo** CR-01 por cámara. **G1 (sujeto):** se indexa además por `subject_key` —
hay un CR-01 **por persona**.

El tracker que sostiene G1 es deliberadamente simple: **asociación por IoU** frame a
frame (una detección de persona continúa el track con el que más se solapa;
expiración si desaparece). Se implementó como **decorador de la fuente en el
control-plane** (adenda ADR-002): lee las detecciones, les agrega `track_id`, y el
motor ni se entera — por eso G1 corre sobre **exactamente las mismas detecciones**
que G0 (bit a bit), sin GPU.

**El mecanismo de la mejora (F-89.1/89.2)** — esto es lo que hay que saber explicar,
porque es el mejor resultado del banco (+0,141 de F1, 100% del motor):

- Bajo escena, el estado es **compartido**: la persona A (con casco) y la persona B
  (sin casco) alimentan el mismo acumulador. La evidencia de B puede confirmar una
  alerta "de la escena" que el matching temporal atribuye mal (alertas **cruzadas de
  condición**), y la evidencia del pre-roll (antes del episodio GT) puede dejar el
  acumulador "caliente" y confirmar **prematuro**.
- Bajo sujeto, cada persona tiene su acumulador: la evidencia de B confirma **sobre
  B**, alineada con su episodio. Las prematuras de pre-roll caen de 5 a 1; P7 (el
  escenario multi-persona) pasa de 0,400 a 1,000.

**Por qué las métricas MOT "no aplican" y eso es correcto (E-10):** MOTA/IDF1 miden
calidad de **identidades** contra un GT de identidades persistentes — que no existe
en el banco. Y no haría falta: como las detecciones son idénticas, la ganancia de G1
**no es de percepción ni de tracking fino**: es de **atribución de estado**, y se
expresa (y se mide) en alertas. Ese es el fundamento *medido* de la exclusión, no una
excusa.

---

## Parte III — La plataforma como sistema

### 10. Tres servicios HTTP config-driven, eventos normalizados

**Arquitectura:** tres servicios HTTP config-driven — los dos planos más el módulo
de distribución (ADR-019/020).

- **media-plane (:8080)** — el plano de medios: ingesta de fuentes (carpeta de
  imágenes, archivo de video, RTSP, OAK-D), normalización, inferencia OVD (el modelo
  se carga una vez al arranque), y emisión de **eventos normalizados**
  `media.detection.v1` (cajas, clases, scores, `unit_id`, timestamps). Escribe
  `runs/<id>/detections.jsonl`.
- **control-plane (:8081)** — el plano de control: consume esos eventos, corre el
  motor de patrones (§8), emite alertas, y trae el **evaluador** contra GT.
- **distribución (:8082)** — el módulo de salida: consume las **alertas confirmadas**
  y las entrega hacia afuera por **MQTT (QoS 1)**, con un **ledger de idempotencia**
  para que un reintento nunca duplique una notificación. Escribe
  `notifications.jsonl` y su `distribution_summary.json`.

Las decisiones arquitectónicas que lo gobiernan (DA-01/02/03): separar percepción de
decisión, publicar la evidencia como **eventos normalizados** (el motor no sabe qué
modelo corre — puede cambiarse el detector sin tocar una línea del motor), y separar
**transporte** de **persistencia**: el bus mueve, el **JSONL persiste y es la fuente
de verdad**.

**Dos patrones de acople, y solo dos.** (1) **HTTP config-driven**: los tres
servicios se operan igual —`POST /api/runs`, estado por polling— y la webconsole y
el runner son **clientes de los tres**, nunca del bus. (2) **Bus ZeroMQ PUB/SUB**:
`:5557` mueve las detecciones (media → control) y `:5558` las alertas confirmadas
(control → distribución); ambos exigen suscribirse **antes** de disparar. MQTT no es
un tercer patrón: es la **salida** de la plataforma hacia el receptor, no un acople
interno.

**Config-driven:** no hay rutas ni umbrales hardcodeados. Una corrida se define por
YAMLs versionados (modelo+resolución, prompt set, pattern set, fuente); los catálogos
de experimento (prompt sets congelados, manifiestos) viven en `experimental-setup`,
que también trae el **runner** (orquesta los servicios por HTTP en el orden correcto)
y la **webconsole** (React + BFF FastAPI). Esto es lo que vuelve **reproducible por
configuración** cada campaña, y lo que hace barato el experimento A1 (una condición
nueva = un YAML).

### 11. DBE vs EBE: los dos escenarios de evaluación

- **DBE (Dataset-Based Evaluation, offline):** el media-plane escribe
  `detections.jsonl`; el control-plane lo **relee** (replay). Determinista,
  re-corrible infinitas veces, ideal para comparar combinaciones (todas las campañas
  del banco son DBE a 30 fps de evidencia).
- **EBE (Environment-Based Evaluation, live):** acople por **bus ZeroMQ PUB/SUB con
  msgpack** (envelope `bus.envelope.v1`). Conceptos clave:
  - **`seq` monotónico por publicador**, que se incrementa **aunque el envío se
    descarte**: así un hueco de `seq` en el consumidor delata pérdida — se cuenta
    como `bus_dropped_events` y degrada la corrida, nunca se silencia. (Teoría:
    PUB/SUB no tiene entrega garantizada; la integridad no se supone, se
    **instrumenta**.)
  - **PUB/SUB pierde lo publicado antes de suscribirse** ⇒ orden de arranque no
    negociable: primero el control-plane (su `201` implica suscripto), después el
    media-plane.
  - **Corrida 1:1** (ADR-007): un run de control por run de media, cierre por
    `run_finished`.
- **El puente entre ambos:** toda corrida live es **re-evaluable offline** — el JSONL
  que produjo el camino live, releído por replay, da artefactos **byte-idénticos**
  (verificado con un gate que falla si se muta 1 píxel). Esto es lo que permite decir
  que los números DBE hablan del camino live, con la densidad de evidencia como la
  diferencia a medir (§17).

### 12. Reproducibilidad como diseño, no como promesa

Cadena de trazabilidad de cualquier número: `metrics.json` (forma única
`clip_campaign_metrics.v1`) ← `evals/` por clip ← alertas del run ← `campaign.yaml`
(la combinación declarada + **sha256 del prompt set congelado y del manifest del
banco**) ← `provenance.json` (apunta a los runs del media-plane, que no se copian —
DA-03). Congelar con hash y verificar con script (`96-verificar-indices.py`) es lo
que convierte "confía en mí" en "corré esto".

---

## Parte IV — Cómo se mide (la teoría de las métricas)

### 13. Nivel imagen: IoU, AP y por qué el agregado engaña

- **IoU (Intersection over Union):** solapamiento entre caja predicha y caja GT
  (área de intersección / área de unión). El umbral estándar **IoU ≥ 0,5** define
  qué cuenta como acierto (por eso "AP@0.5").
- **Matching:** cada predicción se asigna a lo sumo a un GT (greedy por score, 1:1);
  predicción sin GT = FP, GT sin predicción = FN.
- **Precision / Recall:** P = TP/(TP+FP) — de lo que dije, cuánto era cierto;
  R = TP/(TP+FN) — de lo que había, cuánto encontré. Todo detector intercambia una
  por otra moviendo el umbral de confianza.
- **AP (Average Precision):** el área bajo la curva precision-recall al barrer el
  umbral — resume el trade-off completo en un número por clase. **mAP50** = promedio
  de AP@0.5 entre clases.
- **Estratificación (regla L5):** `bench_v3` junta 3 fuentes con estilos y
  anotaciones distintas, y el 77% de las imágenes es de una sola (`shel5k`). Un
  agregado puede mejorar mientras el estrato que importa empeora (la lógica de la
  paradoja de Simpson). Por eso la regla no negociable: **reportar por estrato,
  siempre** — y por eso "campeón robusto a la fuente" significa "gana en las dos
  escalas", no "gana en el promedio".

### 14. Nivel persona: calibración/test y por qué se parte la muestra

Nivel A pregunta por el **estado** ("esta persona está sin casco"), que exige elegir
umbrales de confianza. Elegir el umbral y medir **sobre los mismos datos** infla el
resultado (el umbral se sobreajusta a la muestra). Protocolo del proyecto:
**calibrar en la mitad A, medir solo en la mitad B** — la forma mínima de un
train/test split, aplicada a hiperparámetros de decisión. Los IC por bootstrap (§16)
acompañan cada F1; "IC no solapados" entre E-IND y E-DIR en `shel5k` es lo que
permite hablar de diferencia real y no de ruido.

### 15. Nivel alerta: episodios, matching temporal y las métricas de la plataforma

El GT temporal define **episodios**: intervalos [inicio, fin] por condición dentro de
cada clip ("de 00:05 a 00:31 la persona está sin casco"). El evaluador matchea
alertas contra episodios (misma fuente — convención `source_id = clip_id` —, misma
condición, dentro de la ventana derivada de la persistencia nominal):

- **Recall (micro, por episodio):** episodios con alerta / episodios evaluables.
- **Precision:** alertas que corresponden a un episodio / alertas totales.
- **t_alert:** cuánto tardó el sistema desde que la condición se sostiene hasta
  confirmar. Su valor **ideal** no es 0: es el umbral de la política (4.000/7.000
  ms) — un t_alert de 4.100 ms es un motor puntual, no lento.
- **TTFD:** cuánto tardó la **percepción** en ver la primera evidencia del episodio.
  Separa el costo del detector (TTFD) del costo de la política (t_alert).
- **SDR:** fracción del episodio cubierta por detecciones — la densidad de la
  percepción. (Con la trampa F-96.6: su cálculo funde huecos menores al paso
  nominal, así que **no se compara entre cadencias**.)
- **Censura:** un episodio más corto que la ventana necesaria para confirmar
  (`clip_too_short_for_t_alert_window`) **no puede** medirse — sale del denominador
  con causa, en vez de contarse como fallo. De ahí el denominador citable: **34
  evaluables sobre 35 en el bloque del rodaje** (el calificador no es opcional: 34 es el
  Bloque A, no el banco). (Teoría: análisis de datos censurados — excluir con registro
  es honesto; contar como miss sería sesgar en contra; contar como hit, a favor.)
- **Negativos:** los clips de cumplimiento no entran a P/R/F1 (no hay episodios que
  recuperar) — su métrica son los **FP en negativos**, el control de falsas alarmas.
  Promediar su "F1" hundiría el agregado contando aciertos como catástrofes (F-EV1).

**Por qué FAR/hora se reporta pero no sostiene una cota (limitación L1):** una tasa de
falsas alarmas por hora es estadística de **eventos raros**: para afirmar
"FAR ≤ 1/hora" observando 0 eventos hace falta una exposición de ~3 horas de
cumplimiento anotado (regla de 3: con 0 eventos en T horas, el IC 95% superior de la
tasa es ≈3/T). El banco junta 0,10–0,26 h ⇒ cualquier cota honesta (11–30 FA/h) no
sostiene ninguna afirmación operativa. Por eso el peso lo lleva el **control comparativo
de negativos**, que sí discrimina entre combinaciones (0 FP vs 2–3 FP sobre los mismos
4 clips).

> ✎ **2026-08-12 — precisión, y no es cosmética.** La formulación anterior decía que
> *"FAR/hora NO es métrica de este trabajo"*, y de ahí salió una de las siete trampas de la
> guía de redactores. **La tasa se mide y se reporta**: desde el 08-07 el banco tiene un
> clip de soak (`v06_c01`, 0,1027 h), así que es computable. Lo que no cambia es la
> conclusión —**no sostiene una cota**, faltan casi dos órdenes de magnitud de exposición—,
> y ese es el contenido de **L1**. Al citarla nunca va la tasa desnuda: va el conteo de
> falsos positivos con su duración observada, y la tasa horaria como derivada
> (`GUIA-REDACTORES` §3).

### 16. La estadística de las comparaciones: bootstrap pareado e IC

Comparar dos campañas por su F1 global esconde que ambas corrieron **sobre los mismos
34 clips del Bloque A** — y que los clips varían muchísimo en dificultad. El método:

- **Bootstrap pareado por clip:** remuestrear clips con reposición (10.000 veces),
  recalculando el delta de F1 **entre las dos campañas sobre la misma muestra**. El
  pareo cancela la dificultad del clip (el factor común) y deja la diferencia entre
  combinaciones.
- **IC 95% que excluye el cero** ⇒ la diferencia sobrevive al remuestreo ⇒ se puede
  afirmar. **IC que cruza el cero** ⇒ estimación puntual: se reporta como
  observación consistente, **no** como hallazgo.
- **La regla de degradación (doc 98):** cuando la estimación era vistosa pero el IC
  cruzaba el cero, la afirmación se degradó (caso testigo: "G1 a 4,29 fps supera a
  T1 a 30 fps"). Esta regla es la espina dorsal de la **escala AF**: no todo lo
  medido tiene el mismo estatuto — establecida / direccional (n chico) / tendencia
  con mecanismo / no cerrada / limitación — y decirlo explícitamente es más fuerte
  ante un tribunal que aplanarlo.

**Pre-registro:** los criterios de decisión del eje D1 (el gate de Nivel A, el veto
de precisión < 0,5 a Nivel B, el umbral de adopción de la fusión) se fijaron **antes
de correr** (`nucleo/04` §8). Eso convierte "descartamos E-DIR" de opinión en
resultado, y hace que la refutación de la predicción propia (E-HYB-or) sume
credibilidad en vez de restarla.

---

## Parte V — El tiempo real

### 17. Densidad de evidencia: el puente DBE↔EBE

El banco corre offline a **30 fps de evidencia**; el camino live entrega **1,16–4,42
fps** (el resto de los frames se descarta porque la inferencia no llega). ¿Cuánto de
la calidad medida sobrevive a esa dieta? El experimento: re-correr el banco
**decimando** las detecciones con un `stride` (tomar 1 de cada 7 ≈ 4,29 fps; 1 de
cada 26 ≈ 1,15 fps) — la variable única es la cadencia.

**La objeción teórica y su cierre (doc 101):** el decimado regular es un muestreo
determinista; el descarte real del live es **irregular** (jitter — se midió su
coeficiente de variación: CV 0,22–0,36). ¿Invalida eso el proxy? Se verificó
empíricamente: re-correr con decimado **empírico** (huecos muestreados de la
distribución real, 3 semillas) no produce ningún contraste detectable contra el
regular (12/12 IC cruzan el cero) y la ganancia de la identidad conserva el signo en
6/6 realizaciones. Por eso la formulación obligatoria de AF-1 dice "bajo decimado
regular, conservando la dirección bajo el descarte irregular medido".

**Los dos artefactos de instrumento que había que cazar antes de reportar:**

- **F-96.6:** el SDR "mejora" al bajar la densidad — 100% artefacto (el cálculo funde
  huecos ≤ paso nominal, y el paso crece con el stride). Regla: SDR no se compara
  entre cadencias.
- **F-96.5 (sesgo de supervivencia):** el t_alert agregado parecía no empeorar al
  bajar densidad — porque los episodios **lentos mueren como missed** y salen del
  promedio justo cuando el costo sube. Entre supervivientes comunes, el costo real es
  +0,7 a +1,3 s. Regla: t_alert no se compara entre densidades sin control de
  supervivencia.

### 18. Latencia: qué mide G2A y qué no (F-101.8)

**G2A ("glass-to-algorithm")** = tiempo desde la captura hasta el resultado
algorítmico, con presupuesto de diseño 50–250 ms. El hallazgo fino que el informe
debe declarar: la estampa de "captura" del pipeline se toma en el **dequeue** (cuando
el frame sale de la cola interna), **no en el fotón**. Entre el mundo físico y esa
estampa hay un tramo (`capture_to_host`: driver, red, cola) de 202–217 ms medianos en
el rodaje — y hasta 1,6 s con el host degradado. Se validó **contra el mundo físico**
con una claqueta (evento audiovisual sincronizado + reloj externo): el ancla física
tono→fotón→estampa dio +1.066 ms en la toma medida. Moral teórica: toda cadena de
latencia se cita **declarando desde dónde se mide**; "vidrio→alerta = capture_to_host
+ G2A + política".

También se verificó la **política contra reloj externo**: confirmación a 4.142 ms con
umbral de 4.000 (el motor es puntual: el exceso es la cadencia de muestreo), y el
residuo entre relojes fue de 4 ms.

### 19. El techo de fps: por qué era el GIL y no la GPU ni el calor

El live entregaba pocos fps con la GPU subutilizada. Diagnóstico por descarte
instrumentado (docs 73/74):

- **No es la GPU:** triple verificación (CUDA activo, VRAM del proceso, `dmon` con
  SM 6–41%).
- **No es térmico:** la hipótesis del "correlato de temperatura" se refutó con los
  propios datos (corridas lentas y rápidas intercaladas en el tiempo; lo que separa
  poblaciones es la **fuente**: archivo vs cámara).
- **Es contención de GIL (F-RT3):** en CPython un solo hilo ejecuta bytecode a la
  vez. La inferencia libera el GIL mientras corre en CUDA, pero todo el pre/post
  procesamiento en Python (decodificación, conversiones de imagen, serialización)
  compite por él en un proceso con productor + consumidor + publicador. La firma:
  perfil "bursty" con GPU ociosa.
- **La palanca que lo demuestra (F-RT5):** sacar un round-trip PIL innecesario del
  productor dio +18% de fps y −14,4% de latencia (p=0,0195, 11 pares pareados).
  Lección metodológica: palancas <20% exigen ~10 pares intra-campaña para
  distinguirse de la deriva (±150 ms) — y el profiler (py-spy) infla 2× en WSL, así
  que se mide con el instrumento apagado.

El complemento de borde: el prefilter **EN-2** corre un detector de personas liviano
**dentro de la cámara** (OAK-D) y descarta on-device el 87% de los frames sin
personas — menos presión sobre el host sin tocar el modelo principal. Opcional,
apagado por defecto, fail-open (si falla, deja pasar todo: pierde eficiencia, no
evidencia).

---

## Parte VI — Leer los resultados: los mecanismos, traducidos

La fuerza del trabajo no es que los números sean altos — es que **cada falla y cada
ganancia tiene mecanismo identificado**. Los que hay que poder contar de memoria:

| Hallazgo | El mecanismo, en una frase |
|---|---|
| **F-81.1** (histéresis rescata) | La máquina de estados integra evidencia intermitente: mientras los huecos < `resolve_after_ms`, el episodio no se cae — se paga en t_alert. |
| **F-85.3** (doble filo) | El mismo integrador que rescata evidencia verdadera intermitente también **acumula evidencia falsa** intermitente: la histéresis amplifica lo que le den (D1: 35 FP). |
| **F-87.2** (la unión no es monótona) | En un clasificador estático, unir evidencia solo puede subir el recall. En un **motor temporal**, evidencia extra más temprana **adelanta** la confirmación — y una alerta adelantada cae fuera de su ventana de matching: cuenta como FP *y* deja el episodio sin alerta. Más evidencia ⇒ menos recall. Es el resultado más contraintuitivo del banco y por eso se pre-registró la predicción contraria. |
| **F-88.1** (costo del caption) | Cada clase extra en el caption compite por la atención del encoder: una palabra más costó 0,082 de F1 con todo lo demás igual. El prompt es un presupuesto, no una lista de deseos. |
| **F-88.3** (formulación > mecanismo) | Ordena el eje la *forma* del texto (etiqueta corta > frase negada), no la vía (directa/indirecta/nativa). |
| **F-89.1/89.2** (identidad) | Separar acumuladores por sujeto elimina las alertas cruzadas y las prematuras de pre-roll: misma percepción, mejor atribución (§9). |
| **F-94.1** (validar la palabra) | La clase nueva rinde solo si la palabra significa en el modelo lo que significa en la taxonomía del despliegue (`vehicle` murió por solapamiento semántico con `machinery`; `gloves` detectó 252 veces cualquier cosa menos guantes). |
| **F-96.1** (redistribución oculta) | Un agregado plano puede esconder que unos escenarios caen y otros suben: el promedio no es el fenómeno. |
| **F-RT1** (sobre-marca de `vest`) | El modelo "ve chalecos" en texturas de alta visibilidad (campera a franjas) ⇒ suprime CR-02 en silencio. La falsa evidencia positiva es más peligrosa que la ausencia: apaga la alarma. |
| **F-83.6** (recuperador) | Una vía con precisión inservible puede aportar recall complementario — por eso se probó la fusión (y falló por F-87.2, no porque la idea fuera absurda). |

## Parte VII — El cierre metodológico

### 21. Alcance por registro, exclusiones con causa, limitaciones con código

Tres instrumentos que conviene poder explicar como *metodología* (no como burocracia):

- **ADRs (Architecture Decision Records):** cada decisión con su contexto,
  alternativas y consecuencias; no se re-litigan sin causa registrada. Dos series:
  ADR-001…015 del proyecto y ADR-0001…0013 internos del control-plane (citar siempre
  la serie). **ADR-015** es el cierre: registra que el alcance **creció** con
  evidencia (G1 de demostrativa a capacidad medida; E-HYB-or ejercida y refutada),
  cierra la puerta a capacidad nueva y declara MQTT no implementada — exclusión
  ejercida, no deuda.
- **Exclusiones E-01…E-13 (doc 10):** cada cosa que NO se hizo, con la regla del
  informe que la ampara, su rastro y su frase de declaración. La declaración clave:
  las decisiones se tomaron **antes** de los resultados — eso las vuelve metodología
  y no excusa.
- **Limitaciones L1–L8:** con código y citables ("limitación L4"), porque una
  limitación declarada es un resultado sobre el instrumento, no una vergüenza. Las
  dos que más preguntas atraen: **L4** (un solo bloque guionado — ✎ el lote de obra real
  la **precisó, no la levantó**: aporta medición no guionada y, sobre todo, caracteriza
  **dónde el sistema deja de ser evaluable**) y **L2** (sin doble anotación/kappa —
  decisión declarada de presupuesto de anotación).

### 22. Mapa mental para la defensa (una frase por eslabón)

1. **Qué construimos:** una plataforma de dos planos donde la condición de riesgo es
   *configuración en lenguaje* — percibir (media-plane) y decidir en el tiempo
   (control-plane), acoplados por eventos.
2. **Qué preguntamos:** cuánto rinde eso HOY sin entrenar, y qué aporta la
   plataforma alrededor del modelo.
3. **Qué encontramos:** el detector sostiene CR-01 y no CR-02 (asimetría
   estructural); la formulación indirecta gana con veto pre-registrado; **la palanca
   más grande no fue el modelo sino el motor** (identidad: 0,789→0,930 con las
   mismas detecciones); y esa ganancia es la única que sobrevive con significancia a
   la densidad del tiempo real.
4. **Qué declaramos:** los límites con código (L1–L8), las exclusiones con causa, y
   una escala explícita de cuánta fuerza tiene cada afirmación (AF-1…AF-11).
5. **Qué demostramos de extensibilidad:** una condición nueva cuesta minutos y un
   YAML — y validar la palabra contra la taxonomía es parte del costo (F-94.1).

**Las preguntas hostiles previsibles y su eje de respuesta:** *"¿por qué no
fine-tuning?"* → la pregunta parte de una premisa vieja: el fine-tuning **es una rama
experimental del proyecto y se ejerce como jornada completa** (✎ 2026-08-11, ADR-017)
— condicionada desde el diseño por la regla metodológica (Tabla 37: baseline primero)
y por datos/protocolo, no por falta de cómputo ni por tiempo. F-100.1, freeze/smoke técnico,
dual gate y serving real ya quedaron resueltos; el estado vigente es NO-GO T1 full por
~~D-FT-08/T-FT-005,~~ evaluación T-FT-031 y baseline 26s T-FT-032. La procedencia
T-FT-023 quedó CERRADA el 2026-08-13 (snapshot tar `639e60df…`). ✎ **2026-08-15:
D-FT-08/T-FT-005, D-FT-12 y D-FT-13 firmadas por el usuario, y T-FT-031/T-FT-032 cerradas
la misma jornada** con la baseline YOLOE-26s one-shot ejecutada (doc 120) — el NO-GO quedó
en su último eslabón: `full-authorization.json` + `RUN` manual. La
baseline zero-shot era el prerequisito y ES la pregunta central; los resultados y
limitaciones de la jornada se documentan con su estado a la entrega.
✎ **2026-08-28 — este bloque quedó en el 08-15; la jornada E-04 está COMPLETA y CERRADA**
(acta `operacion/128` §1; `operacion/130` §5 / `docs-set.md` #1): **T1 NO-GO** el 08-17
(`operacion/123`: `bare_head` AP50 0,0000→0,0455, recall CR-01 0,0002→0,2089, falla el gain
gate por 0,0045 y la retención por `person` −11,62 %); **T2 NO-GO** el 08-21 (`operacion/127`:
colapso en entrenamiento, ganancia PASA en `bare_head` 0→0,0909 pero retención in-domain
FALLA ×4 —`person` −49,7 %— y OV FALLA —COCO −71,3 %—); **T3 cerrado con causa técnica**
(✎ 09-01, `operacion/131`: la formulación precisa es — sin baseline de la **variante a
tunear**: la `tiny` tiene cajas degeneradas **del checkpoint publicado**, verificado con
`transformers` puro y hash del hub; `base` es sana pero mediocre. Encabezar siempre por
**linaje** —lo tuneado no sería el campeón desplegado— **+ escalera**, F-131.4). La respuesta hostil se arma con la **curva
de 3 puntos** (baseline / T1 / T2) y **F-127.1**: el fallo no era capacidad sino
**estructural** (2.946 imágenes vs 10,35 M parámetros); T1 gana por recall CR-01 y T2 por
AP — no es una métrica única. Ningún checkpoint adoptado; no hay más brazos contra `bench_v3`.
Nunca "falta de tiempo" (ADR-017). *"¿un YOLO
entrenado no haría esto mejor?"* → en su clase sí; la tesis mide otra cosa:
condiciones en lenguaje, extensibilidad y el aporte de la capa temporal/identidad,
que es agnóstica al detector. *"¿cuál es el FAR/hora?"* → se mide y se reporta, pero
**no sostiene una cota**: afirmarla sin ~3 h de cumplimiento anotado sería fabricarla.
Está declarada como limitación L1, y el peso lo lleva el control comparativo de negativos. *"¿el tracker no necesita métricas MOT?"* →
no hay GT de identidades y la ganancia es de atribución de alertas — F-89.1 lo
fundamenta con detecciones bit a bit idénticas.

---

**Ruta de profundización, en orden:** este doc → `resultados-y-conclusiones.md`
(los números) → `results/index.md` y sus 4 índices (las tablas con artefacto) →
`operacion/98` (la escala AF) → los docs de campaña (81, 83–89, 96, 101) para cada
mecanismo → `nucleo/04`/`12` (el pre-registro) y `nucleo/09` (la defensa de OVD).

