# E-OVRT-VDP - paquete de etapa 6

> Generado el 2026-09-08. Etapa 6: secciones 17.6, 18 y 19.

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

- **Etapa activa:** 6 - Etapa 6: secciones 17.6, 18 y 19.
- Este archivo contiene el texto vigente que se modifica y sus insumos de ajuste.
- No se trasladan resultados propios hacia secciones cronologicamente anteriores.
- Nombre propio de esta etapa (01-etapa-6-activa.md): regenerarla no pisa el paquete de ninguna otra etapa.
- **Restriccion propia de esta etapa (✎ 2026-09-08): las cinco secciones del desarrollo estan CERRADAS** — §15/16 v1.4 (en revision final de los colegas) · §17.1 v1.21 · §17.3 v1.12 · §17.4 v1.15 · §17.5 (archivo «v1.5», contenido de la v1.9), bajadas del 09-08 con los pases 5/5b/5c/5d/5e ACEPTADOS por el usuario. Sus textos viajan en este paquete para LEERLOS y citarlos. **No se reabren, no se reescriben y no se les 'corrige' nada desde §17.6/§18/§19**: si algo de ellas parece mal, se anota como hallazgo para un pase explicito, nunca se edita.
- **§18 interpreta lo que §17.5 reporta.** Cada conclusion nace de una cifra o de un veredicto de §17.5 (con su n y su estrato) y declara su fuerza con la escala AF-1…AF-11 de la sintesis; el circulo se cierra con las preguntas rectoras de §16.7.3, las conclusiones parciales de §17.1.11 y los objetivos de §13. Las ocho limitaciones viven en §17.5.7: §18 las hereda y las lee, no las repite. **Nunca 'OVD detecta mejor'**: la tesis es la plataforma y la medicion sin entrenar; el ajuste fino (T1/T2 NO-GO, T3 cerrado por linaje) es un resultado declarado, no un fracaso a esconder ni una promesa.
- **§17.6 es repositorio y evidencias de cierre** (AJ-6.04): lo construido segun §17.4, los artefactos por corrida de 17.4.5 y las pruebas automatizadas de cada modulo, sin conteos que envejecen. **§19** reune el anexo de reproducibilidad (AJ-6.02), licencias, consentimientos y citas obligatorias (AJ-6.03), el Anexo A de `90e` (§19.1) y los Anexos C y D que hoy viajan al final del .docx de §17.1 (§19.3/§19.4). El trabajo futuro (AJ-6.05) sale de las exclusiones EJERCIDAS (ADR-015), no de deseos.
- **Autocontencion:** el informe NUNCA cita documentos locales, ADRs por numero, fichas ni indices del repositorio; las cifras se citan por combinacion + material + n y salen SOLO de los cuatro indices de results/ ya volcados en el contexto base. Un marcador [[PENDIENTE]] solo para datos que no existen todavia (hoy queda uno, en §17.4.6, con su oracion de reemplazo propuesta: la ficha por video del lote de obra real depende de C1).
- **El listado de referencias de §19 arranca por una fusion, no por una redaccion.** La auditoria bibliografica de este paquete lo demuestra: el listado del maestro (242 entradas) es anterior a las correcciones de la Etapa 1 y le faltan DOCE entradas que si estan en el listado de 90e, entre ellas las dos unicas fuentes que aplican modelos vision-lenguaje a seguridad en obra y la fuente de una fila entera de la Tabla A.1. **Primero se fusiona 90e en el listado del maestro; recien despues se decide que dar de baja** (hay 104 huerfanas) y se reemplazan los 21 preprints que ya tienen version publicada. Once citas del informe hoy no resuelven contra ninguna entrada: eso es lo primero que prueba un jurado.
- **Las figuras se producen con `informe/figuras/GUIA-DE-FIGURAS.md`**, que se sube como quinto archivo cuando toca. Define el sistema visual unico de las seis figuras y las especifica una por una. Dos reglas de esa guia que conviene tener presentes desde aca: **se piden como codigo vectorial (SVG o script de graficacion), nunca como imagen de un modelo de imagen**, que deforma los rotulos; y **la Figura 4.3 dibuja hoy dos transiciones que el sistema no hace**, con el mismo error arrastrado en el texto de 17.3.6.1.
- **Integracion (dueño: el equipo, DESPUES de §17.6/§18/§19; no es tarea de esta etapa):** numeracion global de tablas con 14 numeros libres (12–15, 18–19, 31–32, 36–38, 53–55), titulo '17.3. Diseño arquitectonico' ausente del .docx de esa seccion, rotulos 'Nota' con tres formatos distintos entre secciones, altas bibliograficas Milan et al. 2016 y Liang y Han 2024, baja de 'AAIP, s. f.-b'. Numerar con campos de Word al integrar; no renumerar antes.

---

## Fuente: `docs/informe/entregable/96e-informe-v11-cierre-anexos-referencias.md`

> SHA-256 del bloque: `3d054514a734cf944d87341e6f10df53d8bb128bd08741ccc4ecebdede898b44`  
> Seleccion: secciones 17.6, 18, 19 y referencias vigentes del informe v1.1: §17.6 vacia, §18 y §19 escritos ANTES de los resultados (se reescriben, no se retocan).

### 17.6. Documentación técnica, repositorio y evidencias de cierre

[Agregado futuro correspondiente a la Etapa 6]


## 18. Cierre del Proyecto

[Agregado futuro]


## 19. Anexos


### 19.1. Anexo A - Comparativas técnicas y estado del arte complementario

Tabla A. 1

Síntesis de modelos OVD orientada a prototipado


| Modelo | Familia | Mecanismo V-L | AP Zero-shot | FPS | Licencia |
| --- | --- | --- | --- | --- | --- |
| DINO-X | Transformer | Universal Object Prompt | 59.8 (LVIS) | N/D | Apache-2.0 |
| G-DINO 1.5 Pro | Transformer | Fusión cross-modal profunda | 55.7 (LVIS) | N/D | Apache-2.0 |
| G-DINO 1.5 Edge | Transformer | Fusión cross-modal optimizada | 36.2 (LVIS) | 75.2 (TRT) | Apache-2.0 |
| LLMDet | Transformer+LLM | Co-entrenamiento con LLM | 51.1–52.4 (LVIS) | N/D | Apache-2.0 |
| OV-DINO | Transformer | LASF + UniDI | 50.6 (COCO) | N/D | Apache-2.0 |
| DetCLIPv3 | Transformer | Generativo + VLLM | 48.8 (LVIS) | N/D | N/D |
| OWLv2 L/14 | ViT | Self-training escalable | 44.6 (LVIS rare) | N/D | Apache-2.0 |
| YOLOE-v8-L | One-stage | RepRTA + SAVPE + LRPC | 35.9 (LVIS) | 102.5 (TRT) | AGPL-3.0 |
| YOLO-World-L | One-stage | RepVL-PAN contrastivo | 35.4 (LVIS) | 52.0 (V100) | GPLv3 |
| OmDet-Turbo | Transformer RT | EFH + caching texto | 34.0 (LVIS) | 100.2 (TRT) | Apache-2.0 |
| YOLOE-v8-S | One-stage | RepRTA reparametrizable | 27.9 (LVIS) | 305.8 (TRT) | AGPL-3.0 |
| Florence-2-L | Seq2Seq | Generación condicionada | 37.5 (COCO) | Variable | MIT |

Nota: Las velocidades citadas indican condiciones específicas (hardware GPU: V100, T4 o A100; uso de TensorRT; batch size 1; FP16 y/o caching de texto). Las licencias GPL/AGPL requieren derivar código abierto, limitando la adopción industrial. N/D indica no reportado o no optimizado para tiempo real. Fuente: elaboración propia basada en Ren et al. (2024a, 2024b), Fu et al. (2025), Wang et al. (2024, 2025), Yao et al. (2024), Minderer et al. (2023), Cheng et al. (2024), Zhao et al. (2024) y Xiao et al. (2023).

Tabla A. 2

Métricas de evaluación estándar en seguimiento multi-objeto: características y limitaciones


| Métrica | Qué mide | Fortaleza principal | Limitación principal |
| --- | --- | --- | --- |
| MOTA | Precisión global: penaliza FP, FN e ID switches ponderados sobre el total de ground truth (Bernardin & Stiefelhagen, 2008) | Métrica clásica, simple y ampliamente adoptada para medir el desempeño de detección | Sesgada hacia errores de detección; subestima errores de asociación |
| IDF1 | Consistencia de identidad: F1-score sobre detecciones que mantienen el identificador correcto a lo largo del tiempo (Ristani et al., 2016) | Captura la estabilidad de las identidades asignadas | Ignora mejoras en detección (Ristani et al., 2016); no considera localización espacial (Luiten et al., 2021) |
| HOTA | Balance explícito entre precisión de detección (DetA) y precisión de asociación (AssA), con componente de localización (Luiten et al., 2021) | Métrica integral adoptada por MOTChallenge como estándar de referencia | Mayor complejidad conceptual respecto a MOTA/IDF1, al requerir la interpretación conjunta de sus componentes DetA, AssA y LocA para el diagnóstico de fallos (Luiten et al., 2021) |

Nota. MOTA = Multiple Object Tracking Accuracy. IDF1 = Identification F1-Score. HOTA = Higher Order Tracking Accuracy. DetA = Detection Accuracy. AssA = Association Accuracy. FP = Falsos Positivos. FN = Falsos Negativos. IDSW = ID Switches. GT = Ground Truth. Fuente: Elaboración propia basada en las fuentes citadas (Bernardin & Stiefelhagen, 2008; Luiten et al., 2021; Ristani et al., 2016).

Tabla A. 3

Comparativa de servidores de medios de código abierto


| Servidor | Lenguaje | Rol principal | Protocolos | Transcode | Fortaleza |
| --- | --- | --- | --- | --- | --- |
| Janus | C | SFU/Gateway | WebRTC, SIP | Plugins | Modularidad, documentación académica |
| Kurento | C++ | MCU/ Procesamiento | WebRTC, RTSP, RTP | Sí (integrado) | Integración OpenCV, pipelines |
| MediaMTX | Go | Router/Proxy | RTSP, RTMP, WebRTC, SRT, HLS | No | Ligereza, multi-protocolo |
| OvenMediaEngine | C++ | Origin-Edge | WebRTC, LL-HLS, RTMP | Sí (GPU) | Escalabilidad, baja latencia |
| SRS | C++ | Streaming | RTMP, WebRTC, SRT, HLS | Limitado | Eficiencia, cloud-native |

Nota. Elaboración propia basada en las fuentes tratadas en la sección (Ahmad et al., 2005; AirenSoft, s/f-a, s/f-b; Amirante et al., 2014, 2015; bluenviron, s/f; Garcia et al., 2017; Li et al., 2019; López et al., 2016; Meetecho, s/f; OSSRS, s/f; Žádník et al., 2022).


### 19.2. Anexo B - Infraestructura, nodos y parámetros experimentales

Tabla B. 1

Especificaciones técnicas del Central Processing Node (CPN)


| Componente | Especificación |
| --- | --- |
| Modelo | HP Victus 15 Gaming Laptop 15-FB2024LA (2024) |
| CPU | AMD Ryzen 5 8645HS — arquitectura Zen 4; 6 núcleos / 12 hilos; frecuencia base 4.3 GHz, turbo 5.0 GHz |
| GPU dedicada | NVIDIA GeForce RTX 4060 Laptop — chip AD107; 3072 núcleos CUDA; 96 Tensor Cores (4.ª gen.); 8 GB GDDR6; 128-bit; TGP estimado 75 W |
| Decodificación de video | NVIDIA NVDEC de 5.ª generación integrado en la RTX 4060; soporte por hardware para H.264, H.265/HEVC y AV1 |
| Memoria RAM | 32 GB DDR5-5600 (2 × 16 GB SO-DIMM, Dual Channel) |
| Almacenamiento | 1 TB M.2 PCIe NVMe SSD |
| Sistema operativo | Windows 11 Home Single Language |

Nota. Basado en HP Inc. para la identificación del modelo del equipo, y en Advanced Micro Devices, Inc. y NVIDIA Corporation para las especificaciones de CPU y GPU (Advanced Micro Devices, Inc., s. f.; HP Inc., s. f.; NVIDIA Corporation, s. f.-a, s. f.-b).

Tabla B. 2

Especificaciones técnicas del Edge Node candidato (Luxonis OAK-D Pro PoE)


| Componente | Especificación |
| --- | --- |
| Modelo | Luxonis OAK-D Pro PoE (Series 2) |
| Procesador de visión | RVC2 — 4 TOPS totales de procesamiento (1.4 TOPS para AI) |
| Sensor RGB | Sony IMX378, hasta 12 MP (4056 × 3040), rolling shutter, 78° DFOV / 66° HFOV / 54° VFOV, auto-focus, hasta 60 FPS |
| Sensores estéreo | 2 × OV9282, 1 MP (1280 × 800), global shutter, 89.5° DFOV / 80° HFOV / 55° VFOV, hasta 255 FPS |
| Codificación de video | H.264, H.265 y MJPEG por hardware — hasta 4K/30 FPS y 1080p/60 FPS |
| Percepción IR | IR dot projector para estéreo activo + IR illumination LED para operación en baja o nula iluminación |
| IMU | BNO085, 9 ejes, integrada |
| Conectividad | PoE 802.3af Class 3, 1000BASE-T (1 Gbps); conector M12 para alimentación/datos y M8 para IO auxiliar |
| Consumo máximo | Base + streaming 2.5–3 W, más 0.5 W de circuito PoE; consumo total hasta aproximadamente 7.5 W según carga y subsistemas activos |
| Framework de desarrollo | DepthAI |
| Rango de profundidad | Rango ideal 70 cm–12 m; MinZ ~20 cm en 400P + extended disparity; error absoluto < 2 % por debajo de 4 m, < 4 % entre 4 m y 7 m y < 6 % entre 7 m y 10 m |

Nota. Basado en la página oficial del producto y en la documentación de hardware de OAK-D Pro PoE (Luxonis, s. f.-a, s. f.-b). La cámara utiliza PoE para alimentación y conectividad Gigabit Ethernet, dispone de percepción estéreo activa, iluminación IR y capacidades de procesamiento embebido sobre RVC2. La definición del rol exacto del EN en la topología del Escenario B —captura exclusiva, preprocesamiento o captura con inferencia ligera— se determinará en la Et apa 3.

Tabla B. 3

Stack de software candidato del CPN


| Componente | Especificación | Justificación |
| --- | --- | --- |
| Sistema operativo | Windows 11 Home | Plataforma nativa del CPN; compatibilidad con drivers NVIDIA para arquitectura Ada Lovelace. |
| CUDA / cuDNN | CUDA 12.x — cuDNN 9.x (stack candidato, a confirmar) | Combinación compatible con GPUs NVIDIA Ada Lovelace y con los frameworks de inferencia previstos; las versiones exactas se fijarán durante el setup del entorno. |
| Framework de deep learning | PyTorch | Framework oficial de referencia para Grounding DINO y YOLOE; compatibilidad directa con checkpoints preentrenados y ajustados al dominio. |
| Runtime de optimización (primario) | TensorRT | Runtime candidato de optimización para GPU NVIDIA, pertinente para evaluar configuraciones de baja latencia en el CPN. |
| Runtime de optimización (alternativo) | ONNX Runtime (proveedor CUDA) | Alternativa portable para exportar modelos en formato ONNX y contrastar su desempeño frente a TensorRT. |
| Framework de pipeline (a evaluar) | NVIDIA DeepStream vía WSL2 | Framework candidato, basado en GStreamer y documentado por NVIDIA para ejecución sobre Windows 11 mediante WSL2 con GPUs GeForce/Quadro en modo WDDM; su adopción efectiva se evaluará en la instancia de análisis y diseño arquitectónico frente a otras alternativas del plano de medios. |
| Gestión de entorno | conda o venv (a definir) | Aislamiento de dependencias entre modelos con distintos requisitos de versión. |

Nota. La configuración propuesta debe interpretarse como stack candidato del CPN y no como decisión de implementación ya cerrada. La selección final de versiones, runtimes y framework de pipeline corresponde a la instancia de análisis y diseño arquitectónico, en tanto forma parte del diseño arquitectónico del sistema. La instalación efectiva, integración y verificación de funcionamiento del stack sobre el hardware del CPN corresponden a la implementación del prototipo experimental. La selección de Grounding DINO y YOLOE como modelos candidatos se encuentra alineada con el análisis de modelos OVD, que los ubica como alternativas representativas de distintos compromisos entre expresividad semántica y eficiencia computacional. Asimismo, la separación entre PyTorch nativo, TensorRT y ONNX Runtime resulta consistente con el flujo de transferencia previsto entre el TN y el CPN, donde los checkpoints ajustados se exportan al formato requerido por el runtime de inferencia finalmente adoptado. La mención de DeepStream vía WSL2, TensorRT y ONNX Runtime se apoya en la documentación oficial correspondiente (NVIDIA Corporation, 2026a, 2026b; ONNX Runtime, s. f.).

Tabla B. 4

Especificaciones técnicas del Training Node (TN)


| Componente | Especificación |
| --- | --- |
| Tipo de recurso | Cluster de cómputo institucional (Mendieta, CCAD-UNC) |
| Nodos disponibles | 19 nodos de cómputo con GPU |
| GPU por nodo | 2 × NVIDIA A30 — 24 GB HBM2 cada una; arquitectura Ampere; soporte TF32, FP16, BF16 e INT8 |
| CPU por nodo | 20 núcleos / 20 hilos — Intel Xeon E5-2680 v2 |
| Memoria RAM por nodo | 64 GB |
| Almacenamiento local | 400 GB SSD SATA por nodo |
| Interconexión | 40 Gbps Infiniband QDR |
| Asignación mínima | 1/2 nodo (10 cores, 1 GPU) |
| Rol en el proyecto | Fine-tuning de modelos OVD candidatos sobre datos del dominio de construcción civil |
| Disponibilidad | Acceso institucional asignado al proyecto |

Nota. Especificaciones verificadas para el clúster Mendieta en la tabla oficial de infraestructura de CCAD-UNC, y complementadas con la ficha técnica oficial de NVIDIA A30 para las características de la GPU (Centro de Computación de Alto Desempeño, 2026; NVIDIA Corporation, 2022). La asignación mínima validada explícitamente por la fuente institucional es 1/2 nodo (10 cores, 1 GPU). Los clústeres Mulatona, Eulogia, Serafín y Boogie no presentan GPUs en la tabla comparativa oficial del CCAD, por lo que no son considerados para utilizar en el proyecto.

Tabla B. 5

Stack de software candidato del TN


| Componente | Especificación | Justificación |
| --- | --- | --- |
| Sistema operativo | Linux (distribución del cluster) | Entorno estándar para entrenamiento de modelos sobre GPU en infraestructura HPC. |
| CUDA / cuDNN | CUDA 12.x — cuDNN 9.x (stack candidato, a confirmar) | Combinación compatible con la arquitectura Ampere de las NVIDIA A30 y con frameworks de entrenamiento basados en PyTorch. |
| Framework de entrenamiento | PyTorch + bibliotecas de fine-tuning de cada modelo | Grounding DINO y YOLOE publican sus implementaciones oficiales en PyTorch, lo que favorece compatibilidad con checkpoints y rutinas de ajuste fino. |
| Multi-GPU | DistributedDataParallel (DDP) o equivalente (si la asignación efectiva lo permite) | Las 2 A30 por nodo habilitan entrenamiento distribuido para reducir tiempos de convergencia |

Nota. La configuración consignada debe interpretarse como stack candidato del TN y no como entorno de entrenamiento ya validado. La definición del procedimiento de fine-tuning —incluyendo esquema de ajuste, congelamiento de capas, tasa de aprendizaje, número de épocas y uso o no de entrenamiento distribuido— corresponde a la instancia de análisis y diseño arquitectónico como parte del diseño experimental. La instalación efectiva, integración y verificación de funcionamiento del entorno sobre el clúster corresponden a la implementación del prototipo experimental. Asimismo, cualquier comparación entre variantes zero-shot y fine-tuned exige mantener una baseline explícita y una partición train/eval estrictamente disjunta. Fuentes: Liu et al. (2023); Wang et al. (2025); NVIDIA Corporation (2022); Meta AI (2019).

Tabla B. 6

Parámetros de referencia orientativos del pipeline


| Parámetro | Valor de referencia |
| --- | --- |
| Resolución de captura | 1280 × 720 px (HD). Resolución de referencia del sensor o fuente de video. El pipeline incluye una etapa de preprocesamiento que adapta los frames a la resolución de entrada requerida por el modelo seleccionado; para los modelos actualmente priorizados, ello puede implicar configuraciones del orden de 640 × 640 px en variantes tipo YOLOE y 800 × 1333 px en variantes tipo Grounding DINO. |
| Framerate de captura de referencia | 30 FPS (estimativo). Valor orientativo para la fuente de video; no equivale a los FPS efectivos del pipeline, que dependerán de la latencia de inferencia, del presupuesto G2A y de la configuración de ejecución. |
| Presupuesto de latencia G2A | 50 ms - 250 ms. Presupuesto de referencia definido en el framework de métricas; véase allí su formalización y descomposición operativa. |

Nota. Valores orientativos sujetos a validación experimental en la validación experimental. La distinción entre resolución de captura y resolución de entrada del modelo es relevante: el pipeline incluye una etapa de redimensionamiento que adapta los frames al formato esperado por cada modelo OVD candidato. Elaboración propia.

Tabla B. 7

Topología de red del Escenario B


| Aspecto | Descripción |
| --- | --- |
| Topología | LAN. |
| Protocolo de transmisión | RTSP/RTP sobre UDP como protocolo de referencia para cámaras IP y flujos de video sobre red local; la decisión definitiva de transporte y topología interna corresponde a la instancia de análisis y diseño arquitectónico. |
| Acceso a internet | No disponible durante las pruebas. |
| Restricciones de red | Sin restricciones externas previstas; la configuración efectiva de buffering, transporte y eventual intermediación se definirá en la etapa de diseño. |

Nota. En el marco del proyecto, RTSP/RTP se adopta como referencia por su amplia compatibilidad con cámaras IP y por su adecuación a entornos LAN de videovigilancia y streaming controlado. Esta elección no implica fijar de manera anticipada la topología interna definitiva del pipeline ni descartar otras alternativas de transporte que pudieran resultar pertinentes según la arquitectura que se defina en la instancia de análisis y diseño arquitectónico.


### 19.3. Anexo C - Prompts, datos, datasets, benchmarks y logística

Tabla C. 1

Catálogo de prompts candidatos por condición de riesgo


| Código | Eje de variación | Prompt candidato (inglés) | Estrategia |
| --- | --- | --- | --- |
| CR-01 | Sintáctica | person without hard hat | Frase nominal con negación explícita |
| CR-01 | Especificidad | construction worker without safety helmet | Términos específicos del dominio |
| CR-01 | Estado observable | person with bare head on construction site | Estado resultante, sin negación directa |
| CR-01 | Template | a photo of a hard hat | Template estándar CLIP para detección de presencia |
| CR-01 | Indirecta | hard hat ; person | Detección separada de entidades; relación evaluada externamente |
| CR-02 | Sintáctica | person without reflective vest | Frase nominal con negación |
| CR-02 | Especificidad | worker without high-visibility vest | Vocabulario técnico de seguridad |
| CR-02 | Descripción visual | person without bright colored safety clothing | Descripción visual del atributo ausente |
| CR-02 | Template | a photo of a reflective safety vest | Template estándar CLIP |
| CR-02 | Indirecta | reflective vest ; person | Detección separada de entidades |
| CR-03 | Sintáctica | person on scaffolding without harness | Contexto espacial + negación |
| CR-03 | Especificidad | worker at height without fall protection equipment | Vocabulario técnico ampliado |
| CR-03 | Descompuesta | person on scaffolding ; safety harness ; fall arrest harness | Detección separada de persona en altura y elementos de protección |
| CR-03 | Estado observable | unprotected worker on elevated platform | Estado resultante sin negación explícita del EPP |
| CR-04 | Sintáctica | unprotected edge with person nearby | Entidad compuesta: borde + persona |
| CR-04 | Especificidad | elevated platform without guardrail near workers | Términos de protección colectiva |
| CR-04 | Descompuesta | platform edge ; guardrail ; safety railing ; person at height | Detección de borde, protección colectiva y persona |
| CR-05 (a) | Entidades maquinaria | excavator ; backhoe loader ; dump truck ; crane ; heavy machinery | Entidades de maquinaria a detectar individualmente |
| CR-05 (b) | Entidades humanas | person ; construction worker ; pedestrian | Entidades humanas a detectar individualmente |
| CR-06 (a) | Entidad persona | person ; worker ; pedestrian | Entidad cuya posición se evalúa contra el polígono |
| CR-06 (b) | Elementos auxiliares | restricted area sign ; caution tape ; warning tape ; barrier ; safety cone | Elementos delimitadores de referencia visual |

Nota. Las estrategias “Indirecta” y “Descompuesta” utilizan el separador “;” como notación analítica para indicar consultas independientes al modelo OVD; su materialización concreta depende de la sintaxis admitida por cada detector. Las variaciones “Template” utilizan formulaciones tipo “a photo of a [CLASS]”, alineadas con prácticas habituales de uso de modelos visión-lenguaje preentrenados como CLIP. Para CR-05 y CR-06, al tratarse de condiciones de Nivel 3, no se formulan prompts integrados sino prompts de entidades componentes; la evaluación de la condición completa se realiza en el módulo de razonamiento contextual. En particular, los elementos auxiliares de CR-06 no reemplazan la definición externa del polígono de zona restringida, sino que pueden funcionar como referencias visuales complementarias para experimentos o análisis cualitativo. Fuente: Elaboración propia basada en los ejes de variación de la Sección 17.1.5.4.2 y en los hallazgos de Zhou et al. (2022), Du et al. (2022), Gu et al. (2021) y Radford et al. (2021).

Tabla C. 2 Variables de sensibilidad candidatas para el Environment-Based Evaluation


| Variable | Niveles o condiciones retenidas | Uso dentro del protocolo |
| --- | --- | --- |
| Iluminación | Controlada; mixta; natural cuando el entorno lo permita. | Define condición base y barridos univariados de sensibilidad. |
| Resolución de fuente | 1280 × 720 como base; 1920 × 1080 como variante de sensibilidad si la configuración lo permite. | Estima el costo-beneficio entre visibilidad, carga computacional y estabilidad del pipeline. |
| Distancia cámara-sujeto | Rangos a cerrar en instancia de análisis y diseño arquitectónico según campo visual y tamaño aparente; guía inicial: 5-10 m y 10-20 m. | Permite observar el efecto de escala de objeto sin fijar una geometría de cámara antes del diseño del EBE. |
| Oclusión | Baja y media; la oclusión severa no se adopta como obligación de aceptación. | Tensiona la robustez sin convertir la campaña en irreproducible. |
| Tracker | Deshabilitado y habilitado cuando aplique. | Permite medir el aporte del tracking a estabilidad, persistencia y reducción de falsas alarmas. |
| Matriz de prompts | Conjunto acotado de variantes por condición. | Permite seleccionar y congelar el prompt primario antes de las corridas comparativas finales. |
| Composición del vocabulario activo | Configuraciones pequeñas y medianas, explícitamente documentadas. | Permite medir si la cantidad y tipo de consultas activas impacta precisión, latencia o ambas. |

Nota. El EBE se organiza de manera secuencial: condición base, barridos de sensibilidad y prueba de mayor exigencia sobre la mejor configuración retenida. Los niveles consignados son candidatos de diseño y deberán cerrarse al definir la topología y el espacio físico de prueba.

Tabla C. 3

Síntesis de cobertura conjunta por condición de riesgo


| Condición de riesgo | Nivel de cobertura | N.º de fuentes | Observación |
| --- | --- | --- | --- |
| CR-01 — Persona sin casco | Sólida | 7 | Redundancia alta para casco y ausencia de casco. La cobertura proviene de SH17, SHEL5K, CHV, Pictor-PPE, Construction-PPE, GDUT-HWD y SHWD. |
| CR-02 — Persona sin chaleco | Adecuada | 4 | Cobertura suficiente para evaluación, aunque menos redundante que CR-01. La cobertura principal proviene de SH17, CHV, Pictor-PPE y Construction-PPE. |
| CR-03 — Trabajo en altura sin anticaídas | BRECHA | 0 directas | No se identificó una fuente que combine persona en altura, ausencia de sistema anticaídas y anotación aprovechable de la condición completa. |
| CR-04 — Borde elevado desprotegido | BRECHA | 0 directas | No se identificó una fuente con anotaciones de borde elevado, ausencia de protección colectiva y proximidad de personas. |
| CR-05 — Maquinaria cerca de peatones | Parcial | 1 confirmada + 1 condicionada | SODA aporta entidades y contexto de obra. MOCS también aportaría trabajadores, maquinaria y vehículos. La condición completa requiere razonamiento espacial y, eventualmente, temporal. |
| CR-06 — Persona en zona restringida | Parcial | 1 | SODA aporta elementos contextuales útiles para delimitar zonas o barreras. MOCS podría aportar trabajadores y contexto dinámico. La condición requiere polígono externo y regla espacial. |

Nota. Elaboración propia basada en el mapeo de la Tabla 27. El nivel de cobertura refleja la disponibilidad de clases, entidades o contexto útil dentro del inventario, no la dificultad intrínseca de detección ni la complejidad del razonamiento posterior. El conteo de fuentes distingue entre cobertura directa de la condición, cobertura parcial de entidades o contexto, y apoyo contextual insuficiente para constituir por sí solo una etiqueta nativa del patrón de riesgo.

Tabla C. 4

Compatibilidad de formato de anotación entre datasets candidatos y modelos OVD priorizados


| Dataset | Formato nativo | Grounding DINO (ODVG) | YOLOE / pipeline Ultralytics |
| --- | --- | --- | --- |
| SH17 | YOLO; Pascal VOC a verificar | Medio. Desde YOLO requiere conversión YOLO→COCO→ODVG. Si se confirma Pascal VOC, la ruta alternativa sería VOC→COCO→ODVG.. | Nulo/Bajo. Nulo si se usa el formato YOLO disponible; Bajo sólo si se parte de una versión Pascal VOC verificada. |
| SHEL5K | Pascal VOC | Medio. Requiere conversión VOC→COCO→ODVG. | Bajo. Requiere conversión directa VOC→YOLO. |
| CHV | Formato nativo no validado | Medio. Requiere inspección del paquete y normalización previa a COCO/ODVG. | Medio. Requiere inspección del paquete y eventual conversión a YOLO. |
| Pictor-PPE | Formato nativo no validado | Medio. Requiere inspección de la versión pública disponible y normalización a COCO/ODVG. | Medio. Requiere inspección previa y eventual conversión a YOLO. |
| Construction-PPE | YOLO | Medio. Requiere conversión YOLO→COCO→ODVG. | Nulo. Ya se encuentra en formato nativo del pipeline Ultralytics. |
| GDUT-HWD | Formato nativo a verificar; cajas + label en benchmark SSD/Caffe | Medio. Requiere verificar la estructura efectiva de cajas/labels y normalizar a COCO/ODVG. | Medio. Requiere verificar la estructura efectiva de cajas/labels y convertir a YOLO. |
| SHWD | Pascal VOC | Medio. Requiere conversión VOC→COCO→ODVG. | Bajo. Requiere conversión directa VOC→YOLO. |
| SODA | Pascal VOC | Medio. Requiere conversión VOC→COCO→ODVG. | Bajo. Requiere conversión directa VOC→YOLO. |
| MOCS | Multi-type annotation / formato a verificar | Medio condicionado. Requiere acceso efectivo, inspección del paquete y normalización a COCO/ODVG. | Medio condicionado. Requiere acceso efectivo, inspección del paquete y eventual conversión a YOLO. |

Nota. El esfuerzo se clasifica como Nulo —sin conversión—, Bajo —conversión directa o adaptación menor— o Medio —inspección previa del paquete y/o conversión en dos pasos—. La categoría “Medio condicionado” indica que el esfuerzo técnico no puede cerrarse hasta verificar acceso efectivo, estructura del paquete y términos de uso. Cuando la fuente visible no permite confirmar el formato nativo del dataset, el esfuerzo incluye una etapa previa de inspección antes de la normalización al formato de trabajo.

Tabla C. 5

Estimación de volumen de almacenamiento por dataset candidato


| Dataset | Imágenes | Vol. est. (GB) | Formato destino | Observación |
| --- | --- | --- | --- | --- |
| SH17 | 8.099 | ~3–5 | Nativo: YOLO; Pascal VOC a verificar. Destino: COCO/ODVG y/o YOLO. | Descarga desde repositorio/Kaggle del autor. |
| SHEL5K | 5.000 | ~0,5–1 | Nativo: Pascal VOC. Destino: COCO/ODVG y/o YOLO. | Disponible en Mendeley Data. |
| CHV | 1.330 | ~0,5–1 | Formato nativo a verificar. Destino: COCO/ODVG y/o YOLO. | Revisar estructura del paquete y términos de uso al descargar. |
| Pictor-PPE | 1.472 nominales; ~770–780 públicas | ~0,2–0,5 | Formato nativo a verificar. Destino: COCO/ODVG y/o YOLO. | Verificar alcance exacto de la versión pública antes de descargar. |
| Construction-PPE | 1.416 | ~0,18–0,3 | Nativo: YOLO. Destino: YOLO y, si corresponde, COCO/ODVG. | Disponible vía Ultralytics. |
| GDUT-HWD | 3.174 | ~0,5–1,5 | Formato nativo a verificar. Destino: COCO/ODVG y/o YOLO. | Confirmar estructura efectiva de cajas/labels y alcance de licencia sobre datos descargables. |
| SHWD | 7.581 | ~1–3 | Nativo: Pascal VOC. Destino: COCO/ODVG y/o YOLO. | Requiere conversión para ambos pipelines priorizados. |
| SODA | 19.846 | ~8–12 | Nativo: Pascal VOC. Destino: COCO/ODVG y/o YOLO. | Mayor volumen entre los datasets de acceso directo; filtrar según condición objetivo. |
| MOCS | 41.668 | ~15–25 | Multi-type annotation / formato a verificar. Destino condicionado a inspección del paquete. | Acceso por solicitud previa; no debe computarse como volumen operativo automático hasta confirmar acceso y términos. |
| Total estimado | ~88,9–89,6 mil | ~35–55 | — | Escenario condicionado por acceso efectivo, licencia y tamaño real del paquete entregado. |

Nota. Las estimaciones de almacenamiento son aproximadas y dependen de la resolución de las imágenes, la estructura del paquete descargado, la presencia de máscaras u otros tipos de anotación, y los formatos derivados que se generen en la instancia de análisis y diseño arquitectónico. La columna de imágenes se conserva con finalidad logística, ya que permite dimensionar almacenamiento, descarga, conversión y transferencia, sin reemplazar el análisis de cobertura y aptitud desarrollado en las secciones anteriores.


### 19.4. Anexo D - Métricas, instrumentación y bitácora experimental

Tabla D. 1

Métricas de detección OVD adoptadas para el prototipo experimental


| Métrica | Justificación de adopción | Fuente de referencia | Compromiso |
| --- | --- | --- | --- |
| AP@0.5 | Métrica base e interpretable para comparar variantes zero-shot y ajustadas al dominio; tolera errores moderados de localización y cuenta con soporte extendido en herramientas de evaluación. | Everingham et al. (2010) | Obligatorio |
| AP@[0.5:0.95] | Mantiene comparabilidad con el protocolo COCO-style al promediar AP sobre múltiples umbrales de IoU entre 0.50 y 0.95, pero no condiciona por sí sola las decisiones del prototipo experimental. | Lin et al. (2014) | Deseable |
| NMS-AP | Útil como referencia metodológica para análisis fino de OVD con etiquetas o prompts detallados y negativos duros, donde el AP convencional puede inflarse; excede el alcance operativo del prototipo experimental. | Yao et al. (2024) | Conceptual |
| Precision / Recall | Permite analizar el balance entre falsos positivos y falsos negativos con lectura operativa y desagregación por severidad, siempre que se declare explícitamente el punto operativo o criterio de reporte. | Everingham et al. (2010) | Obligatorio |

Nota. AP = Average Precision. NMS = Non-Maximum Suppression. AP@0.5 y Precision/Recall deben reportarse, como mínimo, para la baseline zero-shot y, cuando exista una variante ajustada al dominio metodológicamente comparable, para dicha variante. Precision/Recall deberá reportarse con el punto operativo o criterio de reporte explícitamente declarado. AP@[0.5:0.95] mantiene comparabilidad académica con el protocolo COCO-style y NMS-AP se conserva como referencia metodológica.

Tabla D. 2

Métricas de seguimiento multiobjeto adoptadas para el prototipo experimental


| Métrica | Justificación de adopción | Fuente de referencia | Compromiso |
| --- | --- | --- | --- |
| HOTA | Métrica integral de MOT valiosa para diagnóstico académico, pero costosa por requerir identidades persistentes. | Luiten et al. (2021) | Deseable |
| DetA / AssA | Submétricas útiles para desagregar si las fallas provienen de detección o asociación, siempre que se calcule HOTA. | Luiten et al. (2021) | Deseable |
| IDF1 | Métrica centrada en consistencia de identidad; útil como contraste complementario sobre subsets MOT bien anotados. | Ristani et al. (2016) | Deseable |
| MOTA | Comparabilidad con literatura legacy de tracking; valor diagnóstico complementario. | Bernardin y Stiefelhagen (2008) | Deseable |
| IDSW / Frag | Indicadores de estabilidad del tracker aplicables sólo sobre subsets con identidades consistentes. | Bernardin y Stiefelhagen (2008) | Deseable |
|  | Mide la reducción de falsas alarmas aportada por el tracking; exige declarar previamente cómo se cuenta un falso positivo. | Operacionalización propia | Obligatorio(*) |

Nota. HOTA = Higher Order Tracking Accuracy. DetA = Detection Accuracy. AssA = Association Accuracy. IDF1 = Identification F1. MOTA = Multiple Object Tracking Accuracy. IDSW = ID switches. Frag = fragmentación de trayectorias. = diferencia de falsos positivos entre corridas equivalentes con y sin tracker. Las métricas MOT basadas en identidades se ejecutarán sólo sobre subsets anotados para ese fin. Si no existe ground truth suficiente o no puede declararse una unidad estable de falso positivo —por frame, por track, por evento o por alerta—, no debe calcularse como métrica cuantitativa. En ese caso, sólo podrá reportarse como análisis exploratorio de estabilidad o como conteo descriptivo de activaciones espurias. (*) Si hay tracker y existe unidad de falso positivo comparable entre corridas.

Tabla D. 3

Métricas de rendimiento del pipeline y uso de recursos


| Métrica | Definición operativa | Formato de reporte | Compromiso | Criterio de estabilidad |
| --- | --- | --- | --- | --- |
| FPS efectivos | Cuadros completamente procesados por segundo al final del pipeline. | Media, P50, P95, P99 y variación | Obligatorio | Período de calentamiento previo y corrida sostenida |
| Latencia G2A | Intervalo entre captura o lectura del frame y disponibilidad del resultado de inferencia. | ms (P50, P95, P99) | Obligatorio | Timestamps monotónicos |
| Jitter | Variabilidad de la latencia entre cuadros consecutivos. | ms (desv. est. / coef. variación) | Deseable | Reportar junto con G2A |
| Uso de VRAM | Memoria de video ocupada por modelo, tensores y buffers. | MB y % | Obligatorio | Sin crecimiento monótono |
| Utilización GPU | Porcentaje de ocupación de la GPU durante la corrida. | % | Deseable | Registrar media y picos |
| Uso de RAM/CPU | Consumo de memoria del sistema y presión sobre CPU del proceso completo. | MB/GB y %CPU | Deseable | Registrar serie temporal |

Nota. G2A = Glass-to-Algorithm. FPS = Frames Per Second. VRAM = Video Random Access Memory. El reporte obligatorio mínimo incluye FPS efectivos, latencia G2A y uso de VRAM. Cuando sea posible, conviene registrar además GPU, RAM y CPU con muestreo periódico durante una corrida sostenida.

Tabla D. 4

Umbrales orientativos por severidad para la lectura operativa de la alerta


| Severidad | máx. orient. | TTFD máx. | SDR mín. orient. | Persistencia orient. | Prioridad FP/FN | Observación |
| --- | --- | --- | --- | --- | --- | --- |
| Crítica | 3-5 s | < 1 s | >= 0.50 | 2-4 s | Minimizar FN | Ventana corta; se prioriza no omitir eventos críticos |
| Alta | 5-10 s | < 3 s | >= 0.60 | 3-5 s | Balance FP/FN | Compromiso entre rapidez de respuesta y estabilidad |
| Media | 10-20 s | < 10 s | >= 0.70 | 5-10 s | Minimizar FP | Puede exigirse mayor evidencia antes de confirmar |

Nota. Los valores indicados son orientativos y se alinean con la lógica de persistencia definida en la taxonomía de condiciones de riesgo, patrones y prompts. La columna máx. orient. refiere al tiempo hasta la alerta confirmada dentro del sistema. Ese valor incluye la ventana funcional de persistencia más el presupuesto computacional del pipeline; por esa razón, excede necesariamente a la persistencia orient. La traducción de persistencia a fotogramas dependerá del throughput efectivo del sistema. La calibración empírica final corresponde a la validación experimental.

Tabla D. 5

Insumos mínimos requeridos antes de iniciar una campaña de medición


| Familia de métricas | Ground truth o insumo | Instrumentación mínima | Herramientas o artefactos | Salida mínima |
| --- | --- | --- | --- | --- |
| Detección (AP, P/R) | Bounding boxes y etiquetas por imagen o frame. | Export de predicciones por corrida. | pycocotools o conversión COCO equivalente. | AP y P/R por variante, con punto operativo o criterio de reporte explícitamente declarado. |
| Tracking (HOTA, DetA / AssA, IDF1, MOTA, IDSW / Frag) | Boxes y track_id persistente por frame. | Export MOT-compatible sobre subset anotado. | TrackEval u otra implementación equivalente. | Métricas MOT sobre subset, con declaración explícita de qué métricas fueron ejecutadas y cuáles no. |
| Pipeline (FPS, , jitter) | No requiere GT semántico. | Timestamps por etapa del pipeline. | Logs internos y scripts de agregación. | P50/P95/P99, promedio y variación. |
| Alerta y patrón (, TTFD, SDR, si aplica) | Inicio anotado de la condición de riesgo, duración o intervalo temporal del evento y criterio de activación del patrón. | Logs con timestamps de primera evidencia positiva, inicio de patrón candidato si corresponde, patrón confirmado, alerta registrada y disponibilidad/notificación si aplica. | Event log del pipeline, bitácora de corrida, export de eventos de patrón y scripts de agregación temporal. | TTFD, SDR y cuando exista evaluación de patrón y alerta registrada; sólo si existe trayecto instrumentado. |
| Recursos (VRAM, GPU, RAM, CPU) | No requiere GT semántico. | Muestreo periódico durante la corrida. | nvidia-smi, psutil u otras herramientas del sistema. | Series temporales y resumen. |
| Alerta (, si aplica, TTFD, SDR) | Inicio del evento, duración, severidad y criterio de activación del patrón. | Logs de detección, evaluación de patrón, confirmación de patrón, alerta registrada y consulta o notificación si aplica. | Motor de evaluación de patrones instrumentado; registro interno de alertas; logs del trayecto de consulta o notificación si aplica. | Tiempos y proporciones por evento, con declaración de métricas no aplicables cuando falte instrumentación. |
| Fine-tuning | Split train/eval disjunto y baseline zero-shot explícita. | Registro de entrenamiento y evaluación. | Logs de entrenamiento y scripts comparativos. | Deltas y costo de entrenamiento, cuando aplique. |

Nota. La ausencia de cualquiera de los insumos requeridos para una familia de métricas debe declararse antes de planificar la campaña experimental. En particular, no corresponde reemplazar ground truth inexistente por estimaciones informales ni interpretar logs incompletos como evidencia suficiente de desempeño. Toda métrica sin insumos mínimos deberá registrarse como no ejecutada o no aplicable, según corresponda.

Tabla D. 6

Campos mínimos recomendados para la bitácora experimental


| Campo | Contenido mínimo recomendado | Uso en la interpretación |
| --- | --- | --- |
| Identificación | Fecha, nombre de la corrida, responsable y objetivo. | Permite rastrear la prueba. |
| Modelo | Nombre, versión, checkpoint y variante zero-shot o fine-tuned. | Vincula resultados con artefactos concretos. |
| Entrada | Dataset o clip, resolución, FPS de origen y protocolo de video. | Contextualiza comparaciones. |
| Parámetros | Umbral, vocabulario activo, NMS, tracker on/off, ventana de persistencia, criterio de activación/desactivación del patrón e histéresis si aplica. | Hace reproducible la corrida y permite interpretar la confirmación o descarte de patrones. |
| Hardware | CPU, GPU, VRAM, RAM y equipo o nodo utilizado. | Permite interpretar latencia y uso de recursos. |
| Entorno de software | Sistema operativo, versiones de runtime, framework, librerías críticas y herramientas de instrumentación. | Permite reproducir la corrida y contextualizar diferencias de rendimiento o compatibilidad. |
| Temporalidad y logs | Fuente temporal declarada, período de calentamiento, duración efectiva de la corrida, ubicación de logs crudos y artefactos de evaluación. | Permite validar trazabilidad temporal y auditar métricas derivadas del pipeline y de alerta. |
| Eventos de patrón y alerta | Timestamps de primera evidencia positiva, inicio de patrón candidato si corresponde, patrón confirmado, alerta registrada y notificación o consulta si aplica; identificador del patrón y regla aplicada. | Permite reconstruir por qué y cuándo una detección se transformó en patrón confirmado y alerta registrada. |
| Resultados | Métricas calculadas, unidades y métricas no ejecutadas. | Consolida la salida cuantitativa. |
| Observaciones | Errores, cuellos de botella y cambios no planificados. | Evita lecturas descontextualizadas. |

Nota. Una métrica sin contexto de corrida pierde interpretabilidad y trazabilidad.


## Referencias

Abdalwhab, A. B. M., Imran, A., Heydarian, S., Iordanova, I., & St-Onge, D. (2025). Are open-vocabulary models ready for detection of MEP elements on construction sites? In Proceedings of the 42nd International Symposium on Automation and Robotics in Construction (pp. 1421–1424). International Association for Automation and Robotics in Construction. https://doi.org/10.22260/ISARC2025/0184

Active Silicon Ltd. (2025). Obtaining the lowest latency from your Harrier AF-Zoom IP camera (Technical Report Technical Note 015 (TN015)). Active Silicon. https://www.activesilicon.com/wp-content/uploads/TECH-NOTE-Harrier-IP-Lowest-Latency-Guide.pdf

Adobe. (2021, enero 13). Adobe Flash Player EOL General Information. https://www.adobe.com/hk_en/products/flashplayer/end-of-life-alternative.html

Advanced Micro Devices, Inc. (s. f.). AMD Ryzen 5 8645HS. https://www.amd.com/en/products/processors/laptop/ryzen/8000-series/amd-ryzen-5-8645hs.html

Adžemović, M. (2025). Deep Learning-Based Multi-Object Tracking: A Comprehensive Survey from Foundations to State-of-the-Art (arXiv:2506.13457). arXiv. https://doi.org/10.48550/arXiv.2506.13457

Agencia de Acceso a la Información Pública. (s. f.-a). Conocé tus derechos respecto a tus datos personales. Argentina.gob.ar. Recuperado el 12 de enero de 2026, de https://www.argentina.gob.ar/aaip/datospersonales/derechos

Agencia de Acceso a la Información Pública. (s. f.-b). Videovigilancia: ¿Por qué hay que registrar bases de datos de videovigilancia y presentar el manual de tratamiento? Argentina.gob.ar. Recuperado el 12 de enero de 2026, de https://www.argentina.gob.ar/aaip/datospersonales/responsables/videovigilancia

Aharon, N., Orfaig, R., & Bobrovsky, B.-Z. (2022). BoT-SORT: Robust Associations Multi-Pedestrian Tracking (arXiv:2206.14651). arXiv. https://doi.org/10.48550/arXiv.2206.14651

Ahmad, H. M., y Rahimi, A. (2025). SH17: A dataset for human safety and personal protective equipment detection in manufacturing industry. Journal of Safety Science and Resilience, 6(2), 175–185. https://doi.org/10.1016/j.jnlssr.2024.09.002

Ahmad, I., Xiaohui Wei, Yu Sun, & Ya-Qin Zhang. (2005). Video transcoding: An overview of various techniques and research issues. IEEE Transactions on Multimedia, 7(5), 793–804. https://doi.org/10.1109/TMM.2005.854472

AILab-CVC. (2024, January 30). YOLO-World. GitHub. Retrieved January 21, 2026, from https://github.com/AILab-CVC/YOLO-World

AirenSoft. (s. f.-a). Low-Latency HLS. AirenSoft. OvenMediaEngine Documentation. Recuperado el 8 de enero de 2026, de https://docs.ovenmediaengine.com/streaming/low-latency-hls

AirenSoft. (s. f.-b). OvenMediaEngine: Introduction. AirenSoft. OvenMediaEngine Documentation. Recuperado el 8 de enero de 2026, de https://docs.ovenmediaengine.com/

Amirante, A., Castaldi, T., Miniero, L., & Romano, S. P. (2014). Janus: A general purpose WebRTC gateway. Proceedings of the Conference on Principles, Systems and Applications of IP Telecommunications, 1–8. https://doi.org/10.1145/2670386.2670389

Amirante, A., Castaldi, T., Miniero, L., & Romano, S. P. (2015). Performance analysis of the Janus WebRTC gateway. Proceedings of the 1st Workshop on All-Web Real-Time Systems, 1–7. https://doi.org/10.1145/2749215.2749223

Ananthanarayanan, G., Bahl, P., Bodik, P., Chintalapudi, K., Philipose, M., Ravindranath, L., & Sinha, S. (2017). Real-Time Video Analytics: The Killer App for Edge Computing. Computer, 50(10), 58–67. https://doi.org/10.1109/MC.2017.3641638

Andre, E., Le Breton, N., Lemesle, A., Roux, L., & Gouaillard, A. (2018). Comparative Study of WebRTC Open Source SFUs for Video Conferencing. 2018 Principles, Systems and Applications of IP Telecommunications (IPTComm), 1–8. https://doi.org/10.1109/IPTCOMM.2018.8567642

Apple Developer. (2019). Introducing Low-Latency HLS [Video]. https://developer.apple.com/videos/play/wwdc2019/502/

Apple Developer. (s. f.). Enabling Low-Latency HTTP Live Streaming (HLS). Recuperado https://developer.apple.com/documentation/http-live-streaming/enabling-low-latency-http-live-streaming-hls

Argentina. (2000). Ley N.º 25.326: Ley de Protección de los Datos Personales. Infoleg. https://servicios.infoleg.gob.ar/infolegInternet/anexos/60000-64999/64790/texact.htm

Argentina. (2001, noviembre 29). Decreto 1558/2001: Ley 25.326—Reglamentación. Argentina.gob.ar. https://www.argentina.gob.ar/normativa/nacional/decreto-1558-2001-70368

Argentina. (2006, septiembre 19). Disposición 11/2006: Medidas de seguridad para el tratamiento y conservación de los datos personales. Argentina.gob.ar. https://www.argentina.gob.ar/normativa/nacional/disposici%C3%B3n-11-2006-120120

Argentina. (2015, febrero 24). Disposición 10/2015: Condiciones de licitud para las actividades de recolección y posterior tratamiento de imágenes digitales de personas con fines de seguridad. Argentina.gob.ar. https://www.argentina.gob.ar/normativa/nacional/disposici%C3%B3n-10-2015-243335

Axis Communications AB. (2015). Latency in live network video surveillance (63380/EN/R1/1504) [White paper]. https://www.axis.com/dam/public/9d/e4/5d/latency-in-live-network-video-surveillance-en-US-190945.pdf

Bachhuber, C., Steinbach, E., Freundl, M., & Reisslein, M. (2018). On the Minimization of Glass-to-Glass and Glass-to-Algorithm Delay in Video Communication. IEEE Transactions on Multimedia, 20(1), 238–252. https://doi.org/10.1109/TMM.2017.2726189

Badidi, E., Moumane, K., & Ghazi, F. E. (2023). Opportunities, Applications, and Challenges of Edge-AI Enabled Video Analytics in Smart Cities: A Systematic Review. IEEE Access, 11, 80543–80572. https://doi.org/10.1109/ACCESS.2023.3300658

Bar-Shalom, Y., Fortmann, T. E., & Cable, P. G. (1990). Tracking and Data Association. The Journal of the Acoustical Society of America, 87(2), 918–919. https://doi.org/10.1121/1.398863

Bar-Shalom, Y., Willett, P. K., & Tian, X. (2011). Tracking and data fusion: A handbook of algorithms. YBS Publishing.

Bass, L., Clements, P., & Kazman, R. (2022). Software architecture in practice (Fourth edition). Addison-Wesley.

Bentaleb, A., Taani, B., Begen, A. C., Timmerer, C., & Zimmermann, R. (2019). A Survey on Bitrate Adaptation Schemes for Streaming Media Over HTTP. IEEE Communications Surveys & Tutorials, 21(1), 562–585. https://doi.org/10.1109/COMST.2018.2862938

Bernardin, K., & Stiefelhagen, R. (2008). Evaluating multiple object tracking performance: The CLEAR MOT metrics. EURASIP Journal on Image and Video Processing, 2008(1), 1-10. https://doi.org/10.1155/2008/246309

Bewley, A., Ge, Z., Ott, L., Ramos, F., y Upcroft, B. (2016). Simple online and realtime tracking. En 2016 IEEE International Conference on Image Processing (ICIP) (pp. 3464-3468). IEEE. https://doi.org/10.1109/ICIP.2016.7533003

Bianchi, L., Carrara, F., Messina, N., Gennaro, C., & Falchi, F. (2024). The devil is in the fine-grained details: Evaluating open-vocabulary object detectors for fine-grained understanding. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 22520-22529). https://doi.org/10.1109/CVPR52733.2024.02125

bluenviron. (s. f.). MediaMTX [Software]. GitHub. Recuperado el 8 de enero de 2026, de https://github.com/bluenviron/mediamtx

Bonomi, F., Milito, R., Zhu, J., & Addepalli, S. (2012). Fog computing and its role in the internet of things. Proceedings of the First Edition of the MCC Workshop on Mobile Cloud Computing, 13–16. https://doi.org/10.1145/2342509.2342513

Bossen, F., Bross, B., Suhring, K., & Flynn, D. (2012). HEVC Complexity and Implementation Analysis. IEEE Transactions on Circuits and Systems for Video Technology, 22(12), 1685–1696. https://doi.org/10.1109/TCSVT.2012.2221255

Buslaev, A., Iglovikov, V. I., Khvedchenya, E., Parinov, A., Druzhinin, M., y Kalinin, A. A. (2020). Albumentations: Fast and flexible image augmentations. Information, 11(2), 125. https://doi.org/10.3390/info11020125

Cao, J., Pang, J., Weng, X., Khirodkar, R., & Kitani, K. (2023). Observation-Centric SORT: Rethinking SORT for Robust Multi-Object Tracking. 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 9686–9696. https://doi.org/10.1109/CVPR52729.2023.00934

Card, S. K., Moran, T. P., & Newell, A. (2008). The psychology of human-computer interaction (Repr). Erlbaum.

Carion, N., Massa, F., Synnaeve, G., Usunier, N., Kirillov, A., & Zagoruyko, S. (2020). End-to-End Object Detection with Transformers (arXiv:2005.12872). arXiv. https://doi.org/10.48550/arXiv.2005.12872

Centro de Computación de Alto Desempeño. (2026, 10 de abril). Clusters disponibles. UNC Supercómputo. https://wiki.ccad.unc.edu.ar/infra/clusters.html

Changpinyo, S., Sharma, P., Ding, N., & Soricut, R. (2021). Conceptual 12M: Pushing web-scale image-text pre-training to recognize long-tail visual concepts. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 3557–3567). https://doi.org/10.1109/CVPR46437.2021.00356

Chen, J., & Ran, X. (2019). Deep Learning With Edge Computing: A Review. Proceedings of the IEEE, 107(8), 1655–1674. https://doi.org/10.1109/JPROC.2019.2921977

Cheng, T., Song, L., Ge, Y., Liu, W., Wang, X., & Shan, Y. (2024). YOLO-World: Real-time open-vocabulary object detection. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 16901–16911). https://doi.org/10.1109/CVPR52733.2024.01599

Clark, A., Singh, V., & Wu, Q. (2013). RTP Control Protocol (RTCP) Extended Report (XR) Block for De-Jitter Buffer Metric Reporting (No. RFC7005; p. RFC7005). RFC Editor. https://doi.org/10.17487/rfc7005

Cohen, J. (1960). A coefficient of agreement for nominal scales. Educational and Psychological Measurement, 20(1), 37–46. https://doi.org/10.1177/001316446002000104

Cugola, G., & Margara, A. (2012). Processing flows of information: From data stream to complex event processing. ACM Computing Surveys, 44(3), 1–62. https://doi.org/10.1145/2187671.2187677

Dalvi, M., Singh, N., Bhingarde, S., & Chalke, K. (2025). Construction-PPE: Personal Protective Equipment Detection Dataset (Versión 1.0.0) [Dataset]. Ultralytics. https://docs.ultralytics.com/datasets/detect/construction-ppe/

DASH Industry Forum. (2020, marzo 27). Low-latency Modes for DASH. CR-Low-Latency-Live-r8. https://dashif.org/docs/CR-Low-Latency-Live-r8.pdf

Deber, J., Jota, R., Forlines, C., & Wigdor, D. (2015). How Much Faster is Fast Enough?: User Perception of Latency & Latency Improvements in Direct and Indirect Touch. Proceedings of the 33rd Annual ACM Conference on Human Factors in Computing Systems, 1827–1836. https://doi.org/10.1145/2702123.2702300

Decreto 351/79 de 1979. Reglamentación de la Ley 19.587 de Higiene y Seguridad en el Trabajo. (1979, febrero 5). Infoleg. https://servicios.infoleg.gob.ar/infolegInternet/anexos/30000-34999/32030/dto351-1979-anexo1.htm

Decreto 911/96 de 1996. Reglamento de Higiene y Seguridad para la Industria de la Construcción. (1996, 5 de agosto). Infoleg. https://servicios.infoleg.gob.ar/infolegInternet/anexos/35000-39999/38568/texact.htm

Dendorfer, P., Rezatofighi, H., Milan, A., Shi, J., Cremers, D., Reid, I., Roth, S., Schindler, K., & Leal-Taixé, L. (2020). MOT20: A benchmark for multi object tracking in crowded scenes (arXiv:2003.09003). arXiv. https://doi.org/10.48550/arXiv.2003.09003

Deschere, P. (2025, December 9). Introducing Roboflow Rapid: Text prompt to vision model in minutes. Roboflow Blog. Retrieved January 21, 2026, from https://blog.roboflow.com/roboflow-rapid/

Ding, M., Xiao, B., Codella, N., Luo, P., Wang, J., & Yuan, L. (2022, April 7). [2204.03645] DaViT: Dual Attention Vision Transformers. arXiv. Retrieved January 21, 2026, from https://arxiv.org/abs/2204.03645

Du, C., Lin, C., Jin, R., Chai, B., Yao, Y., & Su, S. (2024). Exploring the State-of-the-Art in Multi-Object Tracking: A Comprehensive Survey, Evaluation, Challenges, and Future Directions. Multimedia Tools and Applications, 83(29), 73151–73189. https://doi.org/10.1007/s11042-023-17983-2

Du, Y., Wei, F., Zhang, Z., Shi, M., Gao, Y., & Li, G. (2022). Learning to prompt for open-vocabulary object detection with vision-language model. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 14084-14093). https://doi.org/10.1109/CVPR52688.2022.01369

Duan, R., Deng, H., Tian, M., Deng, Y., y Lin, J. (2022). SODA: A large-scale open site object detection dataset for deep learning in construction. Automation in Construction, 142, 104499. https://doi.org/10.1016/j.autcon.2022.104499

Emami, P., Pardalos, P. M., Elefteriadou, L., & Ranka, S. (2021). Machine Learning Methods for Data Association in Multi-Object Tracking. ACM Computing Surveys, 53(4), 1–34. https://doi.org/10.1145/3394659

Erfanian, A., Amirpour, H., Tashtarian, F., Timmerer, C., & Hellwagner, H. (2021). LwTE: Light-Weight Transcoding at the Edge. IEEE Access, 9, 112276–112289. https://doi.org/10.1109/ACCESS.2021.3102633

European Data Protection Board. (2020, enero 30). Guidelines 3/2019 on processing of personal data through video devices (Version 2.0). EDPB. https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-32019-processing-personal-data-through-video_en

European Parliament & Council of the European Union. (2016, abril 27). Regulation (EU) 2016/679 (General Data Protection Regulation). EUR-Lex. https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng

Everingham, M., Van Gool, L., Williams, C. K. I., Winn, J., & Zisserman, A. (2010). The Pascal Visual Object Classes (VOC) Challenge. International Journal of Computer Vision, 88(2), 303–338. https://doi.org/10.1007/s11263-009-0275-4

Filali, A., Abouaomar, A., Cherkaoui, S., Kobbane, A., & Guizani, M. (2020). Multi-Access Edge Computing: A Survey. IEEE Access, 8, 197017–197046. https://doi.org/10.1109/ACCESS.2020.3034136

Fu, S., Yang, Q., Mo, Q., Yan, J., Wei, X., Meng, J., Xie, X., & Zheng, W.-S. (2025, January 31). [2501.18954] LLMDet: Learning Strong Open-Vocabulary Object Detectors under the Supervision of Large Language Models. arXiv. Retrieved January 21, 2026, from https://arxiv.org/abs/2501.18954

Garcia, B., Lopez-Fernandez, L., Gallego, M., & Gortazar, F. (2017). Kurento: The Swiss Army Knife of WebRTC Media Servers. IEEE Communications Standards Magazine, 1(2), 44–51. https://doi.org/10.1109/MCOMSTD.2017.1700006

Gettys, J., & Nichols, K. (2012). Bufferbloat: Dark buffers in the internet. Communications of the ACM, 55(1), 57–65. https://doi.org/10.1145/2063176.2063196

Go Packages. (s. f.). Mediamtx Command. Recuperado el 8 de enero de 2026, de https://pkg.go.dev/github.com/bluenviron/mediamtx

Google. (2022, May). owlvit-large-patch14. Hugging Face. https://huggingface.co/google/owlvit-large-patch14

Google. (2023, June). owlv2-base-patch16-ensemble. Hugging Face. https://huggingface.co/google/owlv2-base-patch16-ensemble

GStreamer. (s. f.-a). GStreamer application development manual. Recuperado el 12 de febrero de 2026, de https://gstreamer.freedesktop.org/documentation/?gi-language=c

GStreamer. (s. f.-b). shmsink: GStreamer Bad Plugins 1.0 Plugins Reference Manual. Recuperado el 12 de febrero de 2026, de https://www.manpagez.com/html/gst-plugins-bad-plugins-1.0/gst-plugins-bad-plugins-1.0-1.10.0/gst-plugins-bad-plugins-shmsink.php

Gu, X., Lin, T.-Y., Kuo, W., & Cui, Y. (2021). Open-vocabulary object detection via vision and language knowledge distillation. arXiv. https://doi.org/10.48550/arXiv.2104.13921

Gupta, A., Dollár, P., & Girshick, R. (2019). LVIS: A Dataset for Large Vocabulary Instance Segmentation (arXiv:1908.03195). arXiv. https://doi.org/10.48550/arXiv.1908.03195

HP Inc. (s. f.). Victus Gaming Laptop 15-fb2024la (A14LSLA): Todas las especificaciones técnicas. https://www.hp.com/py-es/products/laptops/product-details/product-specifications/2102249493

Hugging Face. (2024, September 25). OmDet-Turbo. Hugging Face. Retrieved January 21, 2026, from https://huggingface.co/docs/transformers/en/model_doc/omdet-turbo

IDEA-Research. (2023, April 6). IDEA-Research / Grounded-Segment-Anything: Grounded-Segment-Anything. GitHub. Retrieved January 21, 2026, from https://github.com/IDEA-Research/Grounded-Segment-Anything

IDEA-Research. (2024, August 1). IDEA-Research/Grounded-SAM-2: Grounded SAM 2: Ground and Track Anything in Videos. GitHub. Retrieved January 21, 2026, from https://github.com/IDEA-Research/Grounded-SAM-2

IDEA-Research. (2024, May 18). IDEA-Research/GroundingDINO: [ECCV 2024] Official implementation of the paper "Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection". GitHub. Retrieved January 21, 2026, from https://github.com/IDEA-Research/GroundingDINO

IDEA-Research. (2024, November 20). IDEA-Research / DINO-X-API: A Unified Vision Model for Open-World Object Detection and Understanding. GitHub. https://github.com/IDEA-Research/DINO-X-API

Intel. (2021). Upgrading from Intel® Media SDK to Intel® oneAPI Video Processing... https://www.intel.com/content/www/us/en/docs/onevpl/upgrade-from-msdk/2021-3/overview.html

Intel. (2022). H.265/HEVC Hardware Encoding and Decoding Support. https://www.intel.com/content/www/us/en/support/articles/000037112.html

Intel. (s. f.-a). Intel® Video Processing Library: Video Codecs. Recuperado https://www.intel.com/content/www/us/en/developer/tools/vpl/overview.html

Intel. (s. f.-b). Intel oneAPI Video Processing Library (oneVPL). Recuperado https://www.intel.com/content/www/us/en/docs/oneapi/programming-guide/2023-1/intel-oneapi-video-processing-library-onevpl.html

Intel. (s. f.-c). Media Capabilities Supported by Intel Hardware. Recuperado https://www.intel.com/content/www/us/en/docs/onevpl/developer-reference-media-intel-hardware/1-1/overview.html

Intel. (s. f.-d). VA-API: Video Acceleration (VA) API. Recuperado https://intel.github.io/libva/

Internet Assigned Numbers Authority. (s. f.). Service Name and Transport Protocol Port Number Registry. Recuperado el 9 de enero de 2026, de https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml

Iorga, M., Feldman, L., Barton, R., Martin, M. J., Goren, N., & Mahmoudi, C. (2018). Fog computing conceptual model (NIST SP 500-325; p. NIST SP 500-325). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.500-325

iSEE-Laboratory. (2025, January 31). iSEE-Laboratory/LLMDet: (CVPR 2025 highlight✨) Official repository of paper "LLMDet: Learning Strong Open-Vocabulary Object Detectors under the Supervision of Large Language Models". GitHub. Retrieved January 21, 2026, from https://github.com/iSEE-Laboratory/LLMDet

ISO. (2018). ISO 45001:2018 Occupational health and safety management systems—Requirements with guidance for use. ISO. https://www.iso.org/standard/63787.html

ISO. (2023). ISO/IEC 42001:2023—Artificial intelligence management system. ISO. https://www.iso.org/standard/42001

ISO/IEC. (2022). Information technology—Dynamic adaptive streaming over HTTP (DASH)—Part 1: Media presentation description and segment formats. ISO/IEC 23009-1:2022. https://www.iso.org/standard/83314.html

Jeong, E., Kim, J., & Ha, S. (2022). TensorRT-Based Framework and Optimization Methodology for Deep Learning Inference on Jetson Boards. ACM Transactions on Embedded Computing Systems, 21(5), 1–26. https://doi.org/10.1145/3508391

Jiang, K., Huang, J., Xie, W., Lei, J., Li, Y., Shao, L., & Lu, S. (2024). Domain adaptation for large-vocabulary object detectors. In Advances in Neural Information Processing Systems, 37 (pp. 75422–75453). https://doi.org/10.52202/079017-2401

Jiang, Q., Li, F., Zeng, Z., Ren, T., Liu, S., & Zhang, L. (2024). T-Rex2: Towards Generic Object Detection via Text-Visual Prompt Synergy (arXiv:2403.14610). arXiv. https://doi.org/10.48550/arXiv.2403.14610

Keranen, A., Holmberg, C., & Rosenberg, J. (2018). Interactive Connectivity Establishment (ICE): A Protocol for Network Address Translator (NAT) Traversal (No. RFC8445; p. RFC8445). RFC Editor. https://doi.org/10.17487/RFC8445

Khan, M. A., Baccour, E., Chkirbene, Z., Erbad, A., Hamila, R., Hamdi, M., & Gabbouj, M. (2022). A Survey on Mobile Edge Computing for Video Streaming: Opportunities and Challenges. IEEE Access, 10, 120514–120550. https://doi.org/10.1109/ACCESS.2022.3220694

Khattak, M. U., Rasheed, H., Maaz, M., Khan, S., & Khan, F. S. (2023). MaPLe: Multi-modal Prompt Learning (arXiv:2210.03117). arXiv. https://doi.org/10.48550/arXiv.2210.03117

Kim, J., Cho, E., Kim, S., & Kim, H. J. (2024). Retrieval-augmented open-vocabulary object detection. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 17427–17436). https://doi.org/10.1109/CVPR52733.2024.01650

Kirillov, A., Mintun, E., Ravi, N., Mao, H., Rolland, C., Gustafson, L., Xiao, T., Whitehead, S., Berg, A. C., Lo, W.-Y., Dollár, P., & Girshick, R. (2023). Segment Anything (arXiv:2304.02643). arXiv. https://doi.org/10.48550/arXiv.2304.02643

Kirkpatrick, J., Pascanu, R., Rabinowitz, N., Veness, J., Desjardins, G., Rusu, A. A., Milan, K., Quan, J., Ramalho, T., Grabska-Barwinska, A., Hassabis, D., Clopath, C., Kumaran, D., & Hadsell, R. (2017). Overcoming catastrophic forgetting in neural networks. Proceedings of the National Academy of Sciences, 114(13), 3521-3526. https://doi.org/10.1073/pnas.1611835114

Kreutz, D., Ramos, F. M. V., Esteves Verissimo, P., Esteve Rothenberg, C., Azodolmolky, S., & Uhlig, S. (2015). Software-Defined Networking: A Comprehensive Survey. Proceedings of the IEEE, 103(1), 14–76. https://doi.org/10.1109/JPROC.2014.2371999

Kuhn, H. W. (1955). The Hungarian method for the assignment problem. Naval Research Logistics Quarterly, 2(1–2), 83–97. https://doi.org/10.1002/nav.3800020109

Kurose, J. F., & Ross, K. W. (2021). Computer networking: A top-down approach (Eighth edition). Pearson.

Law, W. (2020). Meeting live broadcast requirements – the latest on DASH Low Latency [Presentation]. DVB World Online Presentation. https://dvb.org/wp-content/uploads/2020/03/Latest-on-DASH-low-latency.pdf

Ley 19.587 de 1972. Ley de Higiene y Seguridad en el Trabajo. (1972). Infoleg. https://servicios.infoleg.gob.ar/infolegInternet/anexos/15000-19999/17612/norma.htm

Li, L. H., Zhang, P., Zhang, H., Yang, J., Li, C., Zhong, Y., Wang, L., Yuan, L., Zhang, L., Hwang, J.-N., Chang, K.-W., & Gao, J. (2021, December 7). [2112.03857] Grounded Language-Image Pre-training. arXiv. Retrieved January 21, 2026, from https://arxiv.org/abs/2112.03857

Li, S., Danelljan, M., Ding, H., Huang, T. E., & Yu, F. (2022, July 26). Tracking Every Thing in the Wild. arXiv. https://arxiv.org/abs/2207.12978

Li, S., Fischer, T., Ke, L., Ding, H., Danelljan, M., & Yu, F. (2023). OVTrack: Open-Vocabulary Multiple Object Tracking. 2023 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 5567–5577. https://doi.org/10.1109/CVPR52729.2023.00539

Li, S., Ren, H., Xie, X., & Cao, Y. (2025). A Review of Multi‐Object Tracking in Recent Times. IET Computer Vision, 19(1), e70010. https://doi.org/10.1049/cvi2.70010

Li, X., Cho, B., & Xiao, Y. (2022). Balancing Latency and Accuracy on Deep Video Analytics at the Edge. 2022 IEEE 19th Annual Consumer Communications & Networking Conference (CCNC), 299–306. https://doi.org/10.1109/CCNC49033.2022.9700636

Li, X., Salehi, M. A., Joshi, Y., Darwich, M. K., Landreneau, B., & Bayoumi, M. (2019). Performance Analysis and Modeling of Video Transcoding Using Heterogeneous Cloud Services. IEEE Transactions on Parallel and Distributed Systems, 30(4), 910–922. https://doi.org/10.1109/TPDS.2018.2870651

Lin, T.-Y., Maire, M., Belongie, S., Hays, J., Perona, P., Ramanan, D., Dollar, P. y Zitnick, C. L. (2014). Microsoft COCO: Common objects in context. En D. Fleet, T. Pajdla, B. Schiele y T. Tuytelaars (Eds.), Computer Vision - ECCV 2014 (Vol. 8693, pp. 740-755). Springer. https://doi.org/10.1007/978-3-319-10602-1_48

Liu, L., Li, H., & Gruteser, M. (2019). Edge Assisted Real-time Object Detection for Mobile Augmented Reality. The 25th Annual International Conference on Mobile Computing and Networking, 1–16. https://doi.org/10.1145/3300061.3300116

Liu, S., Zeng, Z., Ren, T., Li, F., Zhang, H., Yang, J., Jiang, Q., Li, C., Yang, J., Su, H., Zhu, J., & Zhang, L. (2024). Grounding DINO: Marrying DINO with grounded pre-training for open-set object detection. In Computer Vision - ECCV 2024 (pp. 38-55). Springer. https://doi.org/10.1007/978-3-031-72970-6_3

Long, Z., y Li, W. (2023). Open-GroundingDino [Repositorio de código]. GitHub. https://github.com/longzw1997/Open-GroundingDino

López, L., París, M., Carot, S., García, B., Gallego, M., Gortázar, F., Benítez, R., Santos, J. A., Fernández, D., Vlad, R. T., Gracia, I., & López, F. J. (2016). Kurento: The WebRTC Modular Media Server. Proceedings of the 24th ACM International Conference on Multimedia, 1187–1191. https://doi.org/10.1145/2964284.2973798

Luiten, J., Os̆ep, A., Dendorfer, P., Torr, P., Geiger, A., Leal-Taixé, L., & Leibe, B. (2021). HOTA: A Higher Order Metric for Evaluating Multi-object Tracking. International Journal of Computer Vision, 129(2), 548–578. https://doi.org/10.1007/s11263-020-01375-2

Luo, W., Xing, J., Milan, A., Zhang, X., Liu, W., & Kim, T.-K. (2021). Multiple object tracking: A literature review. Artificial Intelligence, 293, 103448. https://doi.org/10.1016/j.artint.2020.103448

Luxonis. (s. f.-b). OAK-D Pro PoE [Documentación de hardware]. Luxonis Docs. https://docs.luxonis.com/hardware/products/OAK-D%20Pro%20PoE

Mach, P., & Becvar, Z. (2017). Mobile Edge Computing: A Survey on Architecture and Computation Offloading. IEEE Communications Surveys & Tutorials, 19(3), 1628–1656. https://doi.org/10.1109/COMST.2017.2682318

Magalhães, S. C., Santos, F. N., Machado, P., Moreira, A. P., & Dias, J. (2023). Benchmarking Edge Computing Devices for Grape Bunches and Trunks Detection using Accelerated Object Detection Single Shot MultiBox Deep Learning Models. Engineering Applications of Artificial Intelligence, 117, 105604. https://doi.org/10.1016/j.engappai.2022.105604

Mahmud, R., Kotagiri, R., & Buyya, R. (2018). Fog Computing: A Taxonomy, Survey and Future Directions. En B. Di Martino, K.-C. Li, L. T. Yang, & A. Esposito (Eds.), Internet of Everything (pp. 103–130). Springer Singapore. https://doi.org/10.1007/978-981-10-5861-5_5

Mahy, R., Matthews, P., & Rosenberg, J. (2010). Traversal Using Relays around NAT (TURN): Relay Extensions to Session Traversal Utilities for NAT (STUN) (No. RFC5766; p. RFC5766). RFC Editor. https://doi.org/10.17487/rfc5766

Mallick, S. (2025, 3 de junio). Fine-tuning Grounding DINO: Open-vocabulary object detection. LearnOpenCV. https://learnopencv.com/fine-tuning-grounding-dino/

May, W. (2017). HTTP Live Streaming (R. Pantos, Ed.; No. RFC8216; p. RFC8216). RFC Editor. https://doi.org/10.17487/RFC8216

Mazor, M., Moran, R., & Fleming, S. M. (2021). Stage 2 registered report: Metacognitive asymmetries in visual perception. Neuroscience of Consciousness, 2021(1), niab025. https://doi.org/10.1093/nc/niab025

Meetecho. (s. f.). VideoRoom plugin documentation. Meetecho. Janus WebRTC Server Documentation. Recuperado el 8 de enero de 2026, de https://janus.conf.meetecho.com/docs/videoroom

Meinhardt, T., Kirillov, A., Leal-Taixe, L., & Feichtenhofer, C. (2022). TrackFormer: Multi-Object Tracking with Transformers. 2022 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 8834–8844. https://doi.org/10.1109/CVPR52688.2022.00864

Mell, P. M., & Grance, T. (2011). The NIST definition of cloud computing (NIST SP 800-145; 0 ed., p. NIST SP 800-145). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-145

Mesa. (2025). Mesa 25.1.0 Release Notes / 2025-05-07—The Mesa 3D Graphics Library latest documentation. https://docs.mesa3d.org/relnotes/25.1.0.html

Meta AI. (2019). PyTorch [Software]. https://pytorch.org

Microsoft. (2024, June). Florence-2-large. Hugging Face. https://huggingface.co/microsoft/Florence-2-large

Milan, A., Leal-Taixe, L., Reid, I., Roth, S., & Schindler, K. (2016). MOT16: A Benchmark for Multi-Object Tracking (arXiv:1603.00831). arXiv. https://doi.org/10.48550/arXiv.1603.00831

Minderer, M., Gritsenko, A., & Houlsby, N. (2024). Scaling Open-Vocabulary Object Detection (arXiv:2306.09683). arXiv. https://doi.org/10.48550/arXiv.2306.09683

Minderer, M., Gritsenko, A., Stone, A., Neumann, M., Weissenborn, D., Dosovitskiy, A., Mahendran, A., Arnab, A., Dehghani, M., Shen, Z., Wang, X., Zhai, X., Kipf, T., & Houlsby, N. (2022). Simple open-vocabulary object detection with vision transformers. In Computer Vision – ECCV 2022 (pp. 728–755). Springer. https://doi.org/10.1007/978-3-031-20080-9_42

Minott, D., Siddiqui, S., & Haddad, R. J. (2025). Benchmarking Edge AI Platforms: Performance Analysis of NVIDIA Jetson and Raspberry Pi 5 with Coral TPU. SoutheastCon 2025, 1384–1389. https://doi.org/10.1109/SoutheastCon56624.2025.10971592

MLCommons. (2024, marzo 27). New MLPerf Inference Benchmark Results Highlight The Rapid Growth of Generative AI Models. MLCommons. https://mlcommons.org/2024/03/mlperf-inference-v4/

MLCommons. (s. f.-a). Benchmark MLPerf Inference: Datacenter | MLCommons V3.1. MLCommons. Recuperado https://mlcommons.org/benchmarks/inference-datacenter/

MLCommons. (s. f.-b). MLPerf Inference: Edge. MLCommons. MLCommons Benchmarks. Recuperado https://mlcommons.org/benchmarks/inference-edge/

Nakagawa, K., Tsukada, M., Shima, K., & Esaki, H. (2021). WebRTC-based measurement tool for peer-to-peer applications and preliminary findings with real users. Asian Internet Engineering Conference, 1–8. https://doi.org/10.1145/3497777.3498544

Nath, N. D., Behzadan, A. H., y Paal, S. G. (2020). Deep learning for site safety: Real-time detection of personal protective equipment. Automation in Construction, 112, 103085. https://doi.org/10.1016/j.autcon.2020.103085

NVIDIA Corporation. (2022, marzo). NVIDIA A30 data sheet. https://www.nvidia.com/content/dam/en-zz/Solutions/data-center/products/a30-gpu/pdf/a30-datasheet.pdf

NVIDIA Corporation. (2026a). DeepStream on WSL. https://docs.nvidia.com/metropolis/deepstream/dev-guide/text/DS_on_WSL2.html

NVIDIA Corporation. (2026b). Installing TensorRT. https://docs.nvidia.com/deeplearning/tensorrt/latest/installing-tensorrt/installing.html

NVIDIA Corporation. (s. f.-a). Compare GeForce RTX laptops. https://www.nvidia.com/en-us/geforce/laptops/compare/

NVIDIA Corporation. (s. f.-b). NVIDIA Video Codec SDK. https://developer.nvidia.com/video-codec-sdk

NVIDIA. (2022). NVIDIA Jetson AGX Orin series technical brief. NVIDIA. https://www.nvidia.com/content/dam/en-zz/Solutions/gtcf21/jetson-orin/nvidia-jetson-agx-orin-technical-brief.pdf

NVIDIA. (2024). DeepStream SDK 8.0 for NVIDIA dGPU/X86 and Jetson—DeepStream documentation. https://docs.nvidia.com/metropolis/deepstream/dev-guide/text/DS_Release_notes.html

NVIDIA. (2025). Welcome to the DeepStream documentation (DeepStream SDK overview). NVIDIA. NVIDIA DeepStream SDK Developer Guide. https://docs.nvidia.com/metropolis/deepstream/dev-guide/text/DS_Overview.html

NVIDIA. (s. f.-a). Installing PyTorch for Jetson platform. NVIDIA. NVIDIA Deep Learning Frameworks Documentation. Recuperado https://docs.nvidia.com/deeplearning/frameworks/install-pytorch-jetson-platform/index.html

NVIDIA. (s. f.-b). Interprocess Communication—CUDA Programming Guide. Recuperado https://docs.nvidia.com/cuda/cuda-programming-guide/04-special-topics/inter-process-communication.html

NVIDIA. (s. f.-c). JetPack software stack for NVIDIA Jetson. NVIDIA. NVIDIA Developer. Recuperado https://developer.nvidia.com/embedded/jetpack

NVIDIA. (s. f.-d). NVDEC Video Decoder API Programming Guide. Recuperado https://docs.nvidia.com/video-technologies/video-codec-sdk/13.0/nvdec-video-decoder-api-prog-guide/index.html

NVIDIA. (s. f.-e). NVENC Application Note. Recuperado https://docs.nvidia.com/video-technologies/video-codec-sdk/13.0/nvenc-application-note/index.html

NVIDIA. (s. f.-f). Using FFmpeg with NVIDIA GPU Hardware Acceleration. Recuperado https://docs.nvidia.com/video-technologies/video-codec-sdk/13.0/ffmpeg-with-nvidia-gpu/index.html

om-ai-lab. (2024, March 11). OmDet. GitHub. https://github.com/om-ai-lab/OmDet

ONNX Runtime. (s. f.). CUDA Execution Provider. https://onnxruntime.ai/docs/execution-providers/CUDA-ExecutionProvider.html

ONVIF. (2019). ONVIF Profile S Specification (ONVIF Profile S). ONVIF. https://www.onvif.org/wp-content/uploads/2019/12/ONVIF_Profile_-S_Specification_v1-3.pdf

OpenFog Consortium. (2017). OpenFog Reference Architecture for Fog Computing. Industrial Internet Consortium. https://www.iiconsortium.org/pdf/OpenFog_Reference_Architecture_2_09_17.pdf

Organisation for Economic Co-operation and Development. (2019, mayo 1). OECD AI Principles overview. OECD. https://oecd.ai/en/ai-principles

OSSRS. (s. f.). Introduction (SRS documentation). OSSRS. SRS Documentation (v6). Recuperado el 9 de enero de 2026, de https://ossrs.net/lts/en-us/docs/v6/doc/introduction

Otgonbold, M.-E., Gochoo, M., Alnajjar, F. S., Ali, L., Tan, T.-H., Hsieh, J.-W., y Chen, P.-Y. (2022). SHEL5K: An extended dataset and benchmarking for safety helmet detection. Sensors, 22(6), 2315. https://doi.org/10.3390/s22062315

Pantos, R. (2025). HTTP Live Streaming 2nd Edition (Internet-Draft). Internet Engineering Task Force. https://datatracker.ietf.org/doc/draft-pantos-hls-rfc8216bis/18/

Parmar, H., & Thornburgh, M. (2012). Adobe’s Real Time Messaging Protocol. Adobe. https://ptacts.uspto.gov/ptacts/public-informations/petitions/1557060/download-documents?artifactId=CX29dwexemvGTAgu1npsGb4QtKzyjACHSNYXLhjJp5m1SpQS4AAf-3A

Pereira, R., Carvalho, G., Garrote, L., & Nunes, U. J. (2022). Sort and Deep-SORT Based Multi-Object Tracking for Mobile Robotics: Evaluation with New Data Association Metrics. Applied Sciences, 12(3), 1319. https://doi.org/10.3390/app12031319

Pham, H. V., Tran, T. G., Le, C. D., Le, A. D., & Vo, H. B. (2024). Benchmarking Jetson Edge Devices with an End-to-End Video-Based Anomaly Detection System. En K. Arai (Ed.), Advances in Information and Communication (Vol. 920, pp. 358–374). Springer Nature Switzerland. https://doi.org/10.1007/978-3-031-53963-3_25

Potluri, S., Wang, H., Bureddy, D., Singh, A. K., Rosales, C., & Panda, D. K. (2012). Optimizing MPI Communication on Multi-GPU Systems Using CUDA Inter-Process Communication. 2012 IEEE 26th International Parallel and Distributed Processing Symposium Workshops & PhD Forum, 1848–1857. https://doi.org/10.1109/IPDPSW.2012.228

Radford, A., Kim, J. W., Hallacy, C., Ramesh, A., Goh, G., Agarwal, S., Sastry, G., Askell, A., Mishkin, P., Clark, J., Krueger, G., & Sutskever, I. (2021). Learning Transferable Visual Models From Natural Language Supervision (arXiv:2103.00020). arXiv. https://doi.org/10.48550/arXiv.2103.00020

Rakai, L., Song, H., Sun, S., Zhang, W., & Yang, Y. (2022). Data association in multiple object tracking: A survey of recent techniques. Expert Systems with Applications, 192, 116300. https://doi.org/10.1016/j.eswa.2021.116300

Rasaee, H., Koleilat, T., & Rivaz, H. (2025). Grounding DINO-US-SAM: Text-Prompted Multi-Organ Segmentation in Ultrasound with LoRA-Tuned Vision-Language Models. IEEE Transactions on Ultrasonics, Ferroelectrics, and Frequency Control, 72(10), 1414-1425. https://doi.org/10.1109/TUFFC.2025.3605285

Ravi, N., Gabeur, V., Hu, Y.-T., Hu, R., Ryali, C., Ma, T., Khedr, H., Rädle, R., Rolland, C., Gustafson, L., Mintun, E., Pan, J., Alwala, K. V., Carion, N., Wu, C.-Y., Girshick, R., Dollár, P., & Feichtenhofer, C. (2024). SAM 2: Segment Anything in Images and Videos (arXiv:2408.00714). arXiv. https://doi.org/10.48550/arXiv.2408.00714

Reddi, V. J., Cheng, C., Kanter, D., Mattson, P., Schmuelling, G., Wu, C.-J., Anderson, B., Breughe, M., Charlebois, M., Chou, W., Chukka, R., Coleman, C., Davis, S., Deng, P., Diamos, G., Duke, J., Fick, D., Gardner, J. S., Hubara, I., … Zhou, Y. (2020). MLPerf Inference Benchmark (arXiv:1911.02549). arXiv. https://doi.org/10.48550/arXiv.1911.02549

Ren, T., Chen, Y., Jiang, Q., Zeng, Z., Xiong, Y., Liu, W., Ma, Z., Shen, J., Gao, Y., Jiang, X., Chen, X., Song, Z., Zhang, Y., Huang, H., Gao, H., Liu, S., Zhang, H., Li, F., Yu, K., & Zhang, L. (2024, November 21). [2411.14347] DINO-X: A Unified Vision Model for Open-World Object Detection and Understanding. arXiv. Retrieved January 21, 2026, from https://arxiv.org/abs/2411.14347

Ren, T., Jiang, Q., Liu, S., Zeng, Z., Liu, W., Gao, H., Huang, H., Ma, Z., Jiang, X., Chen, Y., Xiong, Y., Zhang, H., Li, F., Tang, P., Yu, K., & Zhang, L. (2024). Grounding DINO 1.5: Advance the “Edge” of Open-Set Object Detection (Versión 2). arXiv. https://doi.org/10.48550/ARXIV.2405.10300

Ren, T., Liu, S., Zeng, A., Lin, J., Li, K., Cao, H., Chen, J., Huang, X., Chen, Y., Yan, F., Zeng, Z., Zhang, H., Li, F., Yang, J., Li, H., Jiang, Q., & Zhang, L. (2024). Grounded SAM: Assembling Open-World Models for Diverse Visual Tasks (arXiv:2401.14159). arXiv. https://doi.org/10.48550/arXiv.2401.14159

Ristani, E., Solera, F., Zou, R., Cucchiara, R., & Tomasi, C. (2016). Performance Measures and a Data Set for Multi-target, Multi-camera Tracking. En G. Hua & H. Jégou (Eds.), Computer Vision – ECCV 2016 Workshops (Vol. 9914, pp. 17–35). Springer International Publishing. https://doi.org/10.1007/978-3-319-48881-3_2

Robicheaux, P., Gallagher, J., Nelson, J., & Robinson, I. (2025, March 20). RF-DETR: A SOTA Real-Time Object Detection Model. Roboflow Blog. Retrieved January 26, 2026, from https://blog.roboflow.com/rf-detr/

Roboflow. (2023). Autodistill [Software]. GitHub. https://github.com/autodistill/autodistill

Roboflow. (2025, November 14). Build a Rapid Model | Roboflow Docs. Roboflow Documentation. Retrieved January 26, 2026, from https://docs.roboflow.com/rapid/build-a-rapid-model

Roboflow. (2025, November 14). What is Roboflow Rapid? Roboflow Docs. https://docs.roboflow.com/rapid/what-is-roboflow-rapid

Roy (Whalen), S. (2024, julio 18). RTMP vs. RTSP: Which Protocol Should You Choose? (Update). Wowza Media Systems. Wowza Blog. https://www.wowza.com/blog/rtmp-vs-rtsp-which-protocol-should-you-choose

Satyanarayanan, M. (2017). The Emergence of Edge Computing. Computer, 50(1), 30–39. https://doi.org/10.1109/MC.2017.9

Schulzrinne, H., Casner, S., Frederick, R., & Jacobson, V. (2003). RTP: A Transport Protocol for Real-Time Applications (No. RFC3550; p. RFC3550). RFC Editor. https://doi.org/10.17487/rfc3550

Schulzrinne, H., Rao, A., & Lanphier, R. (1998). Real Time Streaming Protocol (RTSP) (No. RFC2326; p. RFC2326). RFC Editor. https://doi.org/10.17487/rfc2326

Schulzrinne, H., Rao, A., Lanphier, R., & Westerlund, M. (2016). Real-Time Streaming Protocol Version 2.0 (M. Stiemerling, Ed.; No. RFC7826; p. RFC7826). RFC Editor. https://doi.org/10.17487/RFC7826

Sharabayko, M. (2022, marzo 14). Improving SRT Retransmissions—Experiments with Simulated Live Streaming. Innovation Labs Blog (Medium). https://medium.com/innovation-labs-blog/improving-srt-retransmissions-experiments-with-simulated-live-streaming-part-1-7d192483bba4

Sharabayko, M. P., Sharabayko, M. A., Dube, J., Kim, J., & Kim, J. (2024). The SRT Protocol (Internet-Draft (working copy)). Internet Engineering Task Force. https://haivision.github.io/srt-rfc/draft-sharabayko-srt.html

Sharma, P., Ding, N., Goodman, S., & Soricut, R. (2018). Conceptual captions: A cleaned, hypernymed, image alt-text dataset for automatic image captioning. In Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (pp. 2556–2565). https://doi.org/10.18653/v1/P18-1238

Shen, Y., Fu, C., Chen, P., Zhang, M., Li, K., Sun, X., Wu, Y., Lin, S., & Ji, R. (2023, December 4). Aligning and Prompting Everything All at Once for Universal Visual Perception. arXiv. https://arxiv.org/abs/2312.02153

Shi, W., Cao, J., Zhang, Q., Li, Y., & Xu, L. (2016). Edge Computing: Vision and Challenges. IEEE Internet of Things Journal, 3(5), 637–646. https://doi.org/10.1109/JIOT.2016.2579198

Shim, I., Oh, T.-H., Lee, J.-Y., Choi, J., Choi, D.-G., & Kweon, I. S. (2019). Gradient-Based Camera Exposure Control for Outdoor Mobile Platforms. IEEE Transactions on Circuits and Systems for Video Technology, 29(6), 1569–1583. https://doi.org/10.1109/TCSVT.2018.2846292

Shuvo, Md. M. H., Islam, S. K., Cheng, J., & Morshed, B. I. (2023). Efficient Acceleration of Deep Learning Inference on Resource-Constrained Edge Devices: A Review. Proceedings of the IEEE, 111(1), 42–91. https://doi.org/10.1109/JPROC.2022.3226481

Silvano, C., Ielmini, D., Ferrandi, F., Fiorin, L., Curzel, S., Benini, L., Conti, F., Garofalo, A., Zambelli, C., Calore, E., Schifano, S., Palesi, M., Ascia, G., Patti, D., Petra, N., De Caro, D., Lavagno, L., Urso, T., Cardellini, V., … Perri, S. (2025). A Survey on Deep Learning Hardware Accelerators for Heterogeneous HPC Platforms. ACM Computing Surveys, 57(11), 1–39. https://doi.org/10.1145/3729215

Sonono, T. (2019). Interoperable Retransmission Protocols with Low Latency and Constrained Delay: A Performance Evaluation of RIST and SRT [Master’s thesis, KTH Royal Institute of Technology]. https://www.diva-portal.org/smash/get/diva2:1335907/FULLTEXT01.pdf

SRT. (1997, julio 7). Resolución SRT 51/97 de 1997. Mecanismo Preventivo de Control en Obras de Construcción. Infoleg. https://servicios.infoleg.gob.ar/infolegInternet/anexos/40000-44999/44588/norma.htm

SRT. (1998, marzo 31). Resolución SRT 35/98 de 1998. Coordinación de Programas de Seguridad en Obras de Construcción. Infoleg. https://servicios.infoleg.gob.ar/infolegInternet/anexos/50000-54999/50188/norma.htm

SRT. (s. f.). Programa de Construcción. Argentina.gob.ar. Recuperado el 12 de enero de 2026, de https://www.argentina.gob.ar/srt/prevencion/programas/construccion

Stephen. (2026). elFarto/nvidia-vaapi-driver [C]. https://github.com/elFarto/nvidia-vaapi-driver (Obra original publicada en 2021)

Sullivan, G. J., Ohm, J.-R., Han, W.-J., & Wiegand, T. (2012). Overview of the High Efficiency Video Coding (HEVC) Standard. IEEE Transactions on Circuits and Systems for Video Technology, 22(12), 1649–1668. https://doi.org/10.1109/TCSVT.2012.2221191

Swaminathan, T. P., Silver, C., & Akilan, T. (2024). Benchmarking Deep Learning Models on NVIDIA Jetson Nano for Real-Time Systems: An Empirical Investigation (Versión 1). arXiv. https://doi.org/10.48550/ARXIV.2406.17749

SysCV. (2023, June 18). ovtrack. GitHub. https://github.com/SysCV/ovtrack

The FFmpeg developers. (s. f.-a). Documentación FFmpeg. Recuperado https://ffmpeg.org/about.html

The FFmpeg developers. (s. f.-b). FFmpeg Protocols Documentation. Recuperado https://ffmpeg.org/ffmpeg-protocols.html

The FFmpeg developers. (s. f.-c). HWAccelIntro – FFmpeg. Recuperado el 12 de febrero de 2026, de https://trac.ffmpeg.org/wiki/HWAccelIntro

The Linux Kernel. (s. f.). Buffer Sharing and Synchronization (dma-buf)—The Linux Kernel documentation. Recuperado https://docs.kernel.org/driver-api/dma-buf.html

THU-MIG. (2025). THU-MIG / yoloe: YOLOE: Real-Time Seeing Anything. GitHub. https://github.com/THU-MIG/yoloe

Twitch Developers. (s. f.). Video Broadcast. Twitch Developers. Recuperado el 11 de febrero de 2026, de https://dev.twitch.tv/docs/video-broadcast/

Ucar, A., Ro, S., Satwika, S., Gayathri, P. Y., & Balsha, M. G. (2025). Fine-Tuning Florence2 for Enhanced Object Detection in Un-constructed Environments: Vision-Language Model Approach (arXiv:2503.04918). arXiv. https://doi.org/10.48550/arXiv.2503.04918

United Nations Educational, Scientific and Cultural Organization. (2021, noviembre 1). Recommendation on the Ethics of Artificial Intelligence. UNESCO. https://unesdoc.unesco.org/ark:/48223/pf0000380455

Video Services Forum. (2020). Reliable Internet Stream Transport (RIST) protocol specification – Simple profile. Video Services Forum. https://static.vsf.tv/download/technical_recommendations/VSF_TR-06-1_2020_06_25.pdf

Video Services Forum. (2024). Reliable Internet Stream Transport (RIST) Protocol Specification – Main Profile. Video Services Forum. https://static.vsf.tv/download/technical_recommendations/VSF_TR-06-2_2024_06_12.pdf

Viitanen, M., Vanne, J., Hamalainen, T. D., Gabbouj, M., & Lainema, J. (2012). Complexity analysis of next-generation HEVC decoder. 2012 IEEE International Symposium on Circuits and Systems, 882–885. https://doi.org/10.1109/ISCAS.2012.6272182

Wang, A., Liu, L., Chen, H., Lin, Z., Han, J., & Ding, G. (2025). YOLOE: Real-Time Seeing Anything (arXiv:2503.07465). arXiv. https://doi.org/10.48550/arXiv.2503.07465

Wang, H., Hao, F., Zhu, C., Rodrigues, J. J. P. C., & Yang, L. T. (2012). An Android Multimedia Framework Based on Gstreamer. En J. J. P. C. Rodrigues, L. Zhou, M. Chen, & A. Kailas (Eds.), Green Communications and Networking (Vol. 51, pp. 51–62). Springer Berlin Heidelberg. https://doi.org/10.1007/978-3-642-33368-2_5

Wang, H., Ren, P., Jie, Z., Dong, X., Feng, C., Qian, Y., Ma, L., Jiang, D., Wang, Y., Lan, X., & Liang, X. (2024, July 10). OV-DINO: Unified Open-Vocabulary Detection with Language-Aware Selective Fusion. arXiv. https://arxiv.org/abs/2407.07844

Wang, H., Zhang, X., Chen, H., Xu, Y., & Ma, Z. (2022). Inferring End-to-End Latency in Live Videos. IEEE Transactions on Broadcasting, 68(2), 517–529. https://doi.org/10.1109/TBC.2021.3071060

Wang, X., Han, Y., Leung, V. C. M., Niyato, D., Yan, X., & Chen, X. (2020). Convergence of Edge Computing and Deep Learning: A Comprehensive Survey. IEEE Communications Surveys & Tutorials, 22(2), 869–904. https://doi.org/10.1109/COMST.2020.2970550

Wang, Z., Wu, Y., Yang, L., Thirunavukarasu, A., Evison, C., y Zhao, Y. (2021). Fast personal protective equipment detection for real construction sites using deep learning approaches. Sensors, 21(10), 3478. https://doi.org/10.3390/s21103478

Wiegand, T., Sullivan, G. J., Bjontegaard, G., & Luthra, A. (2003). Overview of the H.264/AVC video coding standard. IEEE Transactions on Circuits and Systems for Video Technology, 13(7), 560–576. https://doi.org/10.1109/TCSVT.2003.815165

Wojke, N., Bewley, A., & Paulus, D. (2017). Simple online and realtime tracking with a deep association metric. 2017 IEEE International Conference on Image Processing (ICIP), 3645–3649. https://doi.org/10.1109/ICIP.2017.8296962

World Wide Web Consortium. (2025). WebRTC: Real-Time Communication in Browsers (W3C Recommendation). World Wide Web Consortium. https://www.w3.org/TR/webrtc/

Xiao, B., Wu, H., Xu, W., Dai, X., Hu, H., Lu, Y., Zeng, M., Liu, C., & Yuan, L. (2024). Florence-2: Advancing a unified representation for a variety of vision tasks. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (pp. 4818–4829). https://doi.org/10.1109/CVPR52733.2024.00461

Yao, L., Han, J., Liang, X., Xu, D., Zhang, W., Li, Z., & Xu, H. (2023, April 10). [2304.04514] DetCLIPv2: Scalable Open-Vocabulary Object Detection Pre-training via Word-Region Alignment. arXiv. Retrieved January 29, 2026, from https://arxiv.org/abs/2304.04514

Yao, L., Han, J., Wen, Y., Liang, X., Xu, D., Zhang, W., Li, Z., Xu, C., & Xu, H. (2022, September 20). [2209.09407] DetCLIP: Dictionary-Enriched Visual-Concept Paralleled Pre-training for Open-world Detection. arXiv. Retrieved January 29, 2026, from https://arxiv.org/abs/2209.09407

Yao, L., Pi, R., Han, J., Liang, X., Xu, H., Zhang, W., Li, Z., & Xu, D. (2024, April 14). [2404.09216] DetCLIPv3: Towards Versatile Generative Open-vocabulary Object Detection. arXiv. https://arxiv.org/abs/2404.09216

Yao, Y., Liu, P., Zhao, T., Zhang, Q., Liao, J., Fang, C., Lee, K., & Wang, Q. (2024). How to evaluate the generalization of detection? A benchmark for comprehensive open-vocabulary detection. Proceedings of the AAAI Conference on Artificial Intelligence, 38(7), 6630-6638. https://doi.org/10.1609/aaai.v38i7.28485

Yousefpour, A., Fung, C., Nguyen, T., Kadiyala, K., Jalali, F., Niakanlahiji, A., Kong, J., & Jue, J. P. (2019). All one needs to know about fog computing and related edge computing paradigms: A complete survey. Journal of Systems Architecture, 98, 289–330. https://doi.org/10.1016/j.sysarc.2019.02.009

Žádník, J., Mäkitalo, M., Vanne, J., & Jääskeläinen, P. (2022). Image and Video Coding Techniques for Ultra-low Latency. ACM Computing Surveys, 54(11s), 1–35. https://doi.org/10.1145/3512342

Zang, Y., Li, W., Zhou, K., Huang, C., & Loy, C. C. (2022, March 22). [2203.11876] Open-Vocabulary DETR with Conditional Matching. arXiv. https://arxiv.org/abs/2203.11876

Zareian, A., Rosa, K. D., Hu, D. H., & Chang, S.-F. (2021). Open-Vocabulary Object Detection Using Captions (arXiv:2011.10678). arXiv. https://doi.org/10.48550/arXiv.2011.10678

Zhang, H., Ananthanarayanan, G., Bodik, P., Philipose, M., Bahl, P., & Freedman, M. J. (2017). Live Video Analytics at Scale with Approximation and Delay-Tolerance. 377–389. https://www.usenix.org/system/files/conference/nsdi17/nsdi17-zhang.pdf

Zhang, H., Zhang, P., Hu, X., Chen, Y.-C., Li, L. H., Dai, X., Wang, L., Yuan, L., Hwang, J.-N., & Gao, J. (2022). GLIPv2: Unifying Localization and Vision-Language Understanding (arXiv:2206.05836). arXiv. https://doi.org/10.48550/arXiv.2206.05836

Zhang, Y., Sun, P., Jiang, Y., Yu, D., Weng, F., Yuan, Z., Luo, P., Liu, W., & Wang, X. (2022). ByteTrack: Multi-object Tracking by Associating Every Detection Box. En S. Avidan, G. Brostow, M. Cissé, G. M. Farinella, & T. Hassner (Eds.), Computer Vision – ECCV 2022 (Vol. 13682, pp. 1–21). Springer Nature Switzerland. https://doi.org/10.1007/978-3-031-20047-2_1

Zhao, T., Liu, P., He, X., Zhang, L., & Lee, K. (2024). Real-time Transformer-based Open-Vocabulary Detection with Efficient Fusion Head (arXiv:2403.06892). arXiv. https://doi.org/10.48550/arXiv.2403.06892

Zhao, X., Chen, Y., Xu, S., Li, X., Wang, X., Li, Y., & Huang, H. (2024). An Open and Comprehensive Pipeline for Unified Object Grounding and Detection (arXiv:2401.02361). arXiv. https://doi.org/10.48550/arXiv.2401.02361

Zhou, K., Yang, J., Loy, C. C., & Liu, Z. (2022a). Conditional Prompt Learning for Vision-Language Models. IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2022). https://www.computer.org/csdl/proceedings-article/cvpr/2022/694600q6795/1H0OnmbArsY

Zhou, K., Yang, J., Loy, C. C., & Liu, Z. (2022b). Learning to Prompt for Vision-Language Models. International Journal of Computer Vision, 130(9), 2337–2348. https://doi.org/10.1007/s11263-022-01653-1

Zhou, Z., Chen, X., Li, E., Zeng, L., Luo, K., & Zhang, J. (2019). Edge Intelligence: Paving the Last Mile of Artificial Intelligence With Edge Computing. Proceedings of the IEEE, 107(8), 1738–1762. https://doi.org/10.1109/JPROC.2019.2918951

Zhu, X., Su, W., Lu, L., Li, B., Wang, X., & Dai, J. (2020, October 8). [2010.04159] Deformable DETR: Deformable Transformers for End-to-End Object Detection. arXiv. Retrieved January 29, 2026, from https://arxiv.org/abs/2010.04159

Zou, X., Dou, Z.-Y., Yang, J., Gan, Z., Li, L., Li, C., Dai, X., Behl, H., Wang, J., Yuan, L., Peng, N., Wang, L., Lee, Y. J., & Gao, J. (2023). Generalized Decoding for Pixel, Image, and Language (arXiv:2212.11270). arXiv. https://arxiv.org/abs/2212.11270

Zou, Z., Chen, K., Shi, Z., Guo, Y., & Ye, J. (2023). Object Detection in 20 Years: A Survey. Proceedings of the IEEE, 111(3), 257–276. https://doi.org/10.1109/JPROC.2023.3238524

---

## Fuente: `docs/informe/entregable/96a-informe-v11-frontmatter-intro-objetivos-plan.md`

> SHA-256 del bloque: `040f740c01fc99048af4698388ed55a1e30d9c7c1ecbc46751284197ffa6e016`  
> Seleccion: §12 Introduccion (hipotesis de trabajo, alcance) y §13 Objetivos del informe v1.1: §18 tiene que responderlos uno por uno; se citan, no se reescriben (son Etapa 0).

## 12. Introducción


### 12.1. Motivación y contexto del proyecto

La seguridad laboral en la industria de la construcción civil constituye un problema de alta relevancia técnica, social y organizacional. Se trata de un sector caracterizado por entornos dinámicos, tareas simultáneas, circulación de personas y maquinaria, estructuras temporales, cambios frecuentes en la disposición del espacio de trabajo y exposición permanente a condiciones de riesgo. En este contexto, la supervisión visual cumple un papel preventivo relevante, pero también presenta limitaciones cuando depende exclusivamente de la observación humana continua sobre múltiples cámaras o frentes de obra.

El presente Proyecto Integrador surge de la necesidad de explorar una alternativa tecnológica capaz de complementar la supervisión tradicional mediante una plataforma experimental de detección open-vocabulary en video en tiempo real. La motivación central no consiste en reemplazar al supervisor humano ni en automatizar decisiones de cumplimiento normativo, sino en investigar si los modelos actuales de visión-lenguaje pueden contribuir a identificar de manera flexible señales visuales asociadas a condiciones de riesgo en entornos de construcción. De esta forma, el proyecto se ubica en la intersección entre inteligencia artificial, visión por computadora, procesamiento de video en tiempo real, seguridad laboral y diseño responsable de sistemas asistivos.

La elección del tema se fundamenta en una brecha concreta. Los sistemas tradicionales de detección de objetos operan, en general, bajo un paradigma de vocabulario cerrado, es decir, solo reconocen categorías previstas durante su entrenamiento. Esta característica resulta problemática en obras civiles, donde los riesgos no siempre pueden anticiparse como una lista fija de objetos o clases. Una condición como "persona sin casco cerca de una excavación", "material obstruyendo un pasillo de circulación" o "trabajador en zona de tránsito vehicular" combina objetos, atributos, relaciones espaciales, contexto operativo y persistencia temporal. Por ello, un sistema cerrado puede resultar insuficiente si no fue entrenado explícitamente para cada combinación posible.

Frente a esta limitación, los enfoques de detección de vocabulario abierto permiten formular consultas mediante lenguaje natural o, eventualmente, imágenes de referencia. Esta capacidad habilita un modo de interacción más flexible: el usuario puede definir condiciones de interés sin depender exclusivamente de un conjunto rígido de etiquetas preestablecidas. En consecuencia, el proyecto propone evaluar la factibilidad técnica y académica de una plataforma que procese video, interprete consultas open-vocabulary, detecte entidades o condiciones observables, aplique criterios de persistencia o patrones de riesgo y genere alertas asistivas trazables.


### 12.2. Problema identificado

El problema que orienta el trabajo puede expresarse como una discontinuidad entre la naturaleza dinámica y semánticamente abierta de los riesgos en obra y la naturaleza estática de los sistemas de detección visual basados en vocabularios cerrados. Mientras que el entorno de construcción introduce situaciones variables, dependientes del contexto y difíciles de reducir a categorías fijas, muchos sistemas de visión computacional requieren que las clases detectables hayan sido definidas, anotadas y entrenadas previamente.

Esta restricción genera consecuencias prácticas. En primer lugar, una condición no contemplada durante el diseño del sistema puede quedar fuera de su capacidad de detección, aunque sea relevante para la seguridad. En segundo lugar, incorporar nuevas clases o combinaciones suele exigir procesos de recolección de datos, anotación, entrenamiento y validación que pueden ser costosos en tiempo y recursos. En tercer lugar, la detección por fotograma aislado no basta para representar situaciones de riesgo que dependen de duración, reiteración o trayectoria, por lo que el análisis de video requiere además mecanismos de persistencia temporal y criterios operativos para distinguir detecciones aisladas de eventos significativos.

A esta problemática técnica se suma una dimensión operativa: el monitoreo de múltiples cámaras o zonas de trabajo impone una carga cognitiva elevada sobre los responsables de seguridad. La observación humana continua puede verse afectada por fatiga, distracciones, simultaneidad de eventos o limitaciones propias de la atención sostenida. Por ello, una herramienta de detección asistiva puede funcionar como una capa adicional de apoyo, siempre que se mantenga dentro de un marco responsable, trazable y no vinculante.

El proyecto no parte de la premisa de que la inteligencia artificial pueda resolver por sí sola la seguridad en obra. Por el contrario, reconoce que una alerta visual no equivale a una determinación jurídica ni técnica de incumplimiento. La función del sistema propuesto es detectar indicios observables, registrar evidencia, activar patrones previamente definidos y asistir a la supervisión humana. Esta delimitación resulta central para sostener el carácter experimental del trabajo y evitar una interpretación excesiva de las capacidades del prototipo.


### 12.3. Enfoque propuesto e hipótesis de trabajo

La hipótesis de trabajo sostiene que los modelos de detección open-vocabulary, al permitir expresar condiciones de interés mediante lenguaje natural en tiempo de inferencia, constituyen un habilitador tecnológico viable para superar parte de la rigidez de los sistemas closed-set en el contexto del monitoreo visual de seguridad en construcción. Bajo esta hipótesis, una plataforma experimental podría recibir consultas o patrones como "persona sin casco", "persona sin chaleco reflectivo" o "maquinaria cerca de peatones" y transformarlos en eventos analizables dentro de un flujo de video.

Sin embargo, esta hipótesis se formula de manera condicionada. La viabilidad de la solución no depende únicamente de que un modelo pueda detectar objetos en imágenes estáticas, sino de la integración de múltiples dimensiones: selección de modelos visión-lenguaje, rendimiento en hardware disponible, estabilidad temporal de las detecciones, estrategia de prompts, disponibilidad de datasets, presupuesto de latencia, arquitectura de streaming, trazabilidad de eventos y restricciones ético-legales asociadas al tratamiento de vídeo en contextos laborales.

Por este motivo, el proyecto se estructura como una plataforma experimental y no como un producto industrial terminado. El objetivo es construir un prototipo experimental que permita evaluar el comportamiento del enfoque bajo condiciones controladas y reproducibles. La solución esperada se organiza alrededor de una cadena operativa mínima: ingesta o lectura de video, inferencia open-vocabulary, eventual seguimiento temporal, evaluación de patrones de riesgo, registro de eventos y generación de alertas asistivas. Esta cadena permite analizar no sólo la precisión de detección, sino también la oportunidad, estabilidad y utilidad operativa de las alertas generadas.

La propuesta también contempla la comparación entre una línea base zero-shot y eventuales estrategias de adaptación al dominio únicamente cuando existan datos, soporte metodológico e infraestructura suficientes. De esta forma, el ajuste de modelos no se asume como punto de partida, sino como posibilidad condicionada a la evidencia disponible. Esta decisión preserva el sentido open-vocabulary del proyecto y evita convertir la adaptación al dominio en un requisito previo de factibilidad.


### 12.4. Alcance, límites y condiciones de trabajo

El alcance del trabajo se circunscribe al desarrollo y evaluación de una plataforma experimental de detección open-vocabulary en video en tiempo real aplicada al dominio de seguridad en construcción civil. El prototipo se orienta a condiciones observables visualmente, especialmente aquellas vinculadas con uso de elementos de protección personal, presencia de personas en zonas de riesgo, interacción entre peatones y maquinaria, obstrucciones del entorno y otros patrones que puedan formularse como consultas o reglas evaluables.

No se busca construir un sistema de fiscalización automática ni una herramienta de certificación normativa. Las alertas generadas por el prototipo se interpretan como señales asistivas destinadas a apoyar la supervisión humana. En consecuencia, el sistema no sustituye la evaluación técnica en terreno, no define responsabilidades legales, no toma decisiones operativas autónomas y no activa medidas físicas de control. Su valor se analiza como instrumento de apoyo, trazabilidad y experimentación académica.

El prototipo no incluirá reconocimiento de identidad personal. La detección se limitará a entidades y condiciones observables, tales como "persona", "casco", "chaleco", "maquinaria" o "zona restringida", sin asociar individuos a nombres, credenciales o perfiles personales. Esta restricción responde tanto a criterios ético-legales como al alcance técnico del trabajo. Del mismo modo, la versión experimental no contempla integración completa con sistemas externos de gestión de seguridad ni con infraestructura física de alarmas, aunque podrá prever mecanismos básicos de notificación o registro para demostrar interoperabilidad futura.

También se asumen condiciones experimentales controladas. El trabajo prioriza escenarios reproducibles, datasets de referencia y, cuando corresponda, un entorno simulado o representativo de obra. La evaluación se organizará en dos planos complementarios: una evaluación basada en datasets, orientada a comparabilidad, control de variables y repetibilidad; y una evaluación basada en entorno, orientada a observar el comportamiento del pipeline sobre captura continua y variables visuales realistas. La disponibilidad de datos, hardware y tiempo de desarrollo condicionará el grado de profundidad de cada escenario.

El proyecto utilizará, prioritariamente, modelos preentrenados y herramientas disponibles, evitando el entrenamiento desde cero por exceder el alcance académico y computacional previsto. Las decisiones sobre fine-tuning, prompts, tracking, servidores de medios o frameworks de inferencia deberán justificarse según criterios de viabilidad técnica, reproducibilidad, licenciamiento, desempeño y compatibilidad con el hardware disponible. En este sentido, el trabajo no se mide por alcanzar una solución industrial completa, sino por construir evidencia suficiente para evaluar la factibilidad del enfoque.


### 12.5. Enfoque metodológico general

El desarrollo del proyecto adopta un enfoque progresivo e iterativo. En primer lugar, se construye una fundamentación teórica orientada a delimitar el problema, revisar el estado del arte y establecer criterios conceptuales. Esta instancia permite responder qué debe detectar el sistema, cómo pueden interpretarse consultas de lenguaje natural, qué restricciones impone el video en tiempo real, qué papel cumple el seguimiento temporal y bajo qué condiciones ético-legales puede analizarse video en contextos laborales.

En segundo lugar, la fundamentación se traduce en una consolidación metodológica que define condiciones de riesgo, patrones, escenarios de evaluación, infraestructura disponible, estrategia de datos, protocolo de prompts, métricas y presupuesto de latencia. Esta etapa cumple una función de puente entre el análisis conceptual y la implementación, ya que transforma criterios generales en decisiones operativas evaluables.

Posteriormente, el trabajo avanza hacia el diseño arquitectónico de la plataforma, donde se definirán los módulos, flujos de datos, contratos de interfaz, separación entre plano de medios y plano de control, mecanismos de registro y criterios de integración. La implementación del prototipo materializará esas decisiones en una versión mínima reproducible. Finalmente, la validación experimental permitirá medir el comportamiento del sistema, identificar dificultades, discutir limitaciones y proponer líneas futuras.

La metodología se orienta a la trazabilidad. Cada decisión técnica relevante deberá poder vincularse con una necesidad del problema, un criterio derivado del marco teórico, una restricción metodológica o una condición experimental. Por ello, las matrices comparativas extensas, catálogos completos de prompts, inventarios de datasets, detalles de infraestructura y registros de medición se conservarán como anexos o evidencia complementaria, mientras que el cuerpo principal mantendrá únicamente la información relevante para sostener la argumentación central del proyecto.


## 13. Objetivo Del Proyecto


### 13.1. Objetivo general

Diseñar, implementar y evaluar la factibilidad técnica de una plataforma experimental de detección open-vocabulary en video en tiempo real, orientada a la identificación asistiva de condiciones de riesgo en obras de construcción civil, mediante la integración de modelos de visión-lenguaje, procesamiento de video de baja latencia, seguimiento temporal, patrones de riesgo y mecanismos de alerta evaluables bajo condiciones controladas.


### 13.2. Objetivos específicos

Analizar el estado del arte y los fundamentos técnicos, metodológicos, normativos y ético-legales vinculados con la detección open-vocabulary, el seguimiento multiobjeto, la transmisión de video en tiempo real y la seguridad laboral en construcción civil, a fin de establecer criterios de diseño y evaluación para la plataforma experimental.

Definir y operacionalizar un conjunto de condiciones de riesgo visualmente observables en entornos de obra, vinculándolas con patrones de riesgo, niveles de severidad, criterios de persistencia temporal y formulaciones de consulta compatibles con modelos de detección open-vocabulary.

Diseñar una arquitectura modular de procesamiento de video en tiempo real que distinga el plano de medios y el plano de control, permitiendo integrar de manera desacoplada componentes de ingesta, inferencia, seguimiento temporal, evaluación de patrones, registro de eventos y generación de alertas.

Implementar un prototipo experimental capaz de ejecutar el flujo experimental previsto, incorporando ingesta o lectura de video, inferencia open-vocabulary, evaluación de patrones de riesgo, registro de eventos, alertas internas e instrumentación de métricas técnicas y operativas.

Evaluar el desempeño del prototipo mediante un protocolo experimental reproducible, considerando escenarios basados en datasets y escenarios controlados representativos, con métricas de detección, seguimiento, rendimiento del pipeline, latencia de alerta y utilidad operativa de las notificaciones generadas.

Incorporar lineamientos de ética, privacidad y seguridad de la información acordes con el uso responsable de sistemas de análisis automatizado de video en contextos laborales, manteniendo el carácter asistivo de las alertas y evitando mecanismos de reconocimiento de identidad personal.

Documentar las decisiones técnicas, metodológicas y experimentales adoptadas durante el desarrollo del proyecto, junto con sus resultados, limitaciones, evidencias generadas y posibles líneas de continuidad o mejora futura.

---

## Fuente: `docs/informe/entregable/90c-etapa5-texto-extraido.md`

> SHA-256 del bloque: `11fc4c6636e1c6573a8ddeac918ec8691485a006a147b0eae7a4892abf13ea09`  
> Seleccion: §17.5 CERRADA (bajada del 2026-09-08): lo que §18 interpreta. Cada conclusion de §18 nace de una cifra o de un veredicto de esta seccion, con su n y su estrato; las ocho limitaciones viven al final de 17.5.7 y §18 las hereda y las lee, no las repite.

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

## Fuente: `docs/informe/entregable/90b-etapa4-texto-extraido.md`

> SHA-256 del bloque: `51d89e555269aa5286f466ede903249078ef1af7e931d4a91e561005bdb76e61`  
> Seleccion: §17.4 CERRADA (v1.15, 2026-09-08): lo construido, los artefactos por corrida (17.4.5) y las brechas declaradas (17.4.7). Es la fuente de §17.6 (repositorio y evidencias de cierre) y del anexo de reproducibilidad de §19.

# 90b — Texto extraído del documento de trabajo: §17.4 Implementación (v1.15, bajada del 2026-09-08 con los pases 5, 5b, 5c, 5d y 5e aceptados; sin marcas, 3 comentarios abiertos. ETAPA 4 CERRADA)

> **Extracción derivada (2026-09-08)** del `.docx`
> `informe/entregable/E-OVRT-VDP_Seccion_17.4_Implementacion_v1.15.docx`, **solo para búsqueda y cita**
> (mismo estatuto que el doc 90): al editar, se edita el `.docx`/Google Docs, nunca
> este archivo. Tablas y figuras pueden haber perdido formato; las figuras no se
> extraen y las ecuaciones no se convierten — quedan `⟦FIGURA: no extraída — ver el .docx⟧` y
> `⟦ECUACIÓN: no extraída — ver el .docx⟧` donde estaban. Regenerado con
> `herramientas/extraer_informe.py` (regla D-C del manual de aplicación).

---

### 17.4. Implementación del prototipo experimental

La implementación materializa el diseño arquitectónico de la sección 17.3 en componentes construidos, contratos e interfaces concretados, mecanismos de acople y persistencia, y evidencia de verificación del funcionamiento técnico del prototipo.

#### 17.4.1. Componentes construidos y cadena de datos

El prototipo se materializó en tres componentes de plataforma, un módulo funcional de distribución y una cadena de datos externa a la plataforma que produce los insumos experimentales. La Figura 4.5 muestra esa organización con sus dos patrones de acople.

El plano de medios implementa la cadena de inferencia de vocabulario abierto, desde la ingesta hasta la publicación de evidencia perceptiva normalizada. El plano de control implementa el motor de patrones de riesgo, que consume esa evidencia, mantiene estado temporal y registra alertas internas. El soporte experimental no es un plano de ejecución. Reúne los catálogos de prompts y de experimentos, el orquestador reproducible de corridas, la consolidación de artefactos y la consola de inspección con su servicio intermediario.

El módulo de distribución de alertas es un módulo desacoplado y no un tercer plano de ejecución. Consume las alertas confirmadas desde el bus de alertas, aplica la política de notificación, controla idempotencia y supresión, entrega por MQTT en el nivel de calidad de servicio 1, con confirmación por mensaje y conserva un ledger de entregas de sólo adición. Su vista de resultados y su lanzamiento desde la orquestación quedaron integrados a la consola.

La cadena de datos comprende adquisición, validación, conversión y congelamiento de datasets y bancos de evaluación, y la sección 17.4.6 documenta cómo se construyó la del banco temporal de video. Alimenta a la plataforma pero no forma parte de su cadena operativa, porque su función es producir material reproducible y con procedencia para entrenamiento, selección y evaluación.

**Figura 4.5**

*Vista de procesos y patrones de acople de la plataforma experimental*

⟦FIGURA: no extraída — ver el .docx⟧

**Nota.** La figura representa la materialización efectiva de los dos patrones de acople. El gobierno de las corridas ocurre por interfaces HTTP en el plano de medios, el plano de control y el módulo de distribución, con el orquestador y la consola como clientes de los tres. El flujo de datos se desacopla mediante buses ZeroMQ de patrón publicador-suscriptor con serialización msgpack, uno para los eventos de percepción entre medios y control y otro para las alertas confirmadas entre control y distribución. El repositorio por ejecución experimental conserva los artefactos persistentes de cada corrida.

#### 17.4.2. Correspondencia y contratos materializados

Los contratos mínimos definidos durante el diseño se materializaron como modelos de datos, configuraciones versionadas, esquemas serializables, servicios ejecutables y artefactos persistentes. La Tabla 56 establece la correspondencia entre cada denominación conceptual y su realización efectiva.

**Tabla 56**

*Correspondencia entre los contratos del diseño y su materialización efectiva*

| **Elemento del diseño** | **Materialización efectiva** | **Versionado y trazabilidad** | **Componente** |
| --- | --- | --- | --- |
| Manifiesto de experimento | Archivo de manifiesto del experimento y configuraciones efectivas por plano | experiment.manifest.v1 | Soporte experimental |
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
| Repositorio de hechos | Archivos JSONL de sólo adición por corrida | Esquemas de cada evento persistido | Ambos planos |
| Referencia temporal | Anotación humana de episodios por clip | clip_gt.v2 | Soporte experimental |
| Reporte experimental | Reporte consolidado por experimento, report.json y report.md | Proyección regenerable de los artefactos primarios | Soporte experimental |
| NotificationEnvelope y DeliveryRecord | Envoltorio de notificación y registro de entrega en el ledger | control.notification.v1 / control.delivery.v1 | Módulo de distribución |

**Nota.** La tabla documenta la correspondencia semántica entre el diseño y la implementación. El versionado se materializa mediante esquemas explícitos, catálogos, conjuntos de configuración y artefactos congelados por el manifiesto de cada ejecución experimental.

Cinco de esos contratos concentran los hechos principales de la ejecución, y son el evento de percepción, el envoltorio del bus, el contrato de ciclo de vida, el evento de transición de patrón y la alerta interna. La tabla anterior los declara con su identificador de esquema.

Cada contrato es una clase de modelo declarada en el módulo de contratos de su componente, con tipos y campos obligatorios explícitos, validada en la frontera de entrada y persistida como un objeto JSON por línea, omitiendo los campos sin valor. Dentro del plano de medios la evidencia atraviesa además una cadena interna de contratos antes de publicarse. La unidad visual normaliza la lectura de la fuente, y la unidad preparada transporta los píxeles junto con la transformación espacial que devuelve del espacio del modelo al de la imagen original. La detección cruda recoge la salida del adaptador y la detección normalizada es la que se persiste. Esa cadena hace de la reproyección de coordenadas una operación declarada.

El evento de percepción normaliza la salida del detector. Identifica la corrida y la unidad visual, y agrupa en bloques estructurados la fuente, el perfil de modelo, el conjunto de prompts efectivo, las detecciones y los tiempos medidos por unidad. Cada detección lleva su etiqueta, el identificador del prompt que la originó, el puntaje, la caja en píxeles y su equivalente normalizado. Esa composición permite que una detección se atribuya después a una variable concreta de la corrida y no a una combinación desconocida. La forma efectiva del evento, tal como se persiste, es la siguiente.

{   "schema_version": "media.detection.v1",   "event_type": "detection_event",   "run_id": "run_20260803_211225_dbe_grounding_dino_1e06f3",   "unit_id": "frame_000229",   "source":  { "source_id": "a_p1_c02", "source_type": "video_frame",                "frame_index": 229, "timestamp_ms": 7633.33,                "width": 1920, "height": 1080 },   "model":   { "name": "grounding_dino",                "model_id": "IDEA-Research/grounding-dino-tiny", "device": "cuda" },   "prompts": { "prompt_set_id": "cr01_cr02_v2_short" },   "detections": [     { "detection_id": "det_000001", "label": "person",       "prompt_id": "person", "source_prompt": "person", "confidence": 0.88,       "bbox_xyxy":      [1239.8, 149.8, 1503.2, 861.9],       "bbox_norm_xyxy": [0.6457, 0.1387, 0.7829, 0.7981],       "area_px": 187612.4, "model_name": "grounding_dino" },     { "detection_id": "det_000002", "label": "vest",       "prompt_id": "vest", "source_prompt": "vest", "confidence": 0.8755,       "bbox_xyxy":      [1286.5, 235.3, 1459.3, 487.0],       "bbox_norm_xyxy": [0.67, 0.2179, 0.76, 0.4509],       "area_px": 43490.1, "model_name": "grounding_dino" },     { "detection_id": "det_000003", "label": "helmet",       "prompt_id": "helmet", "source_prompt": "helmet", "confidence": 0.456,       "bbox_xyxy":      [1519.0, 432.5, 1648.1, 521.3],       "bbox_norm_xyxy": [0.7911, 0.4005, 0.8584, 0.4827],       "area_px": 11463.6, "model_name": "grounding_dino" }   ],   "timing": { "normalize_ms": 8.06, "inference_ms": 491.17,               "postprocess_ms": 0.08, "write_ms": 0.0, "total_ms": 491.27 } }

La misma estructura se declara en el código como modelo de datos con tipos explícitos. El campo de identidad entre fotogramas aparece aquí como opcional y con valor nulo por defecto, que es el mecanismo con el que un dato todavía no producido puede incorporarse sin cambiar la versión del esquema ni alterar los artefactos ya escritos.

class DetectionEvent(BaseModel):     schema_version: str = "media.detection.v1"     event_type: str = "detection_event"     run_id: str     unit_id: str     source: DetectionEventSource     model: DetectionEventModel     prompts: DetectionEventPrompts     detections: list[Detection]     timing: DetectionEventTiming  class Detection(BaseModel):     detection_id: str | None = None     track_id: str | None = None        # aditivo: identidad entre fotogramas     label: str     prompt_id: str | None = None     source_prompt: str | None = None     strategy: str | None = None     condition_id: str | None = None     confidence: float     bbox_xyxy: list[float]             # coordenadas en la imagen original     bbox_norm_xyxy: list[float]        # coordenadas normalizadas     area_px: float | None = None     model_name: str | None = None

El envoltorio del bus no reempaqueta ese contenido. Transporta como carga la misma cadena que ya se escribió en el artefacto y le agrega cuatro campos propios del transporte, que son el tópico, la clave de particionado, un número de secuencia monótono por publicador y el instante de publicación en reloj de pared. El módulo de distribución conserva ese instante como marca de confirmación. El número de secuencia se consume incluso cuando el envío se descarta por saturación del canal, de modo que la pérdida se vuelva un hueco observable del lado del consumidor.

El contrato de ciclo de vida no delimita el inicio de la corrida sino su cierre, y publica un único evento de finalización con el identificador de corrida y su estado, para que el final lógico se distinga de una interrupción. Ambos contratos se emplean sin variantes en los dos buses, porque el publicador de alertas del plano de control es un espejo deliberado del publicador de medios.

El evento de transición registra los cambios entre los estados del patrón que fija la máquina de estados del diseño, junto con la evidencia y los hitos temporales que los motivaron. Incorpora además el instante y la unidad de la primera evidencia positiva del episodio, que es el punto de partida de la medición de latencia. Un contrato hermano registra el progreso parcial mientras la condición está en curso y todavía no fue confirmada.

La alerta interna registra la confirmación del episodio, y su identificador no es un valor aleatorio. Se deriva de forma determinista sobre la cadena que concatena el identificador de corrida de control, el de corrida de medios, la unidad, el patrón y la clave de sujeto, que incorpora el identificador del sujeto sólo cuando el patrón opera con esa granularidad. La alerta conserva además el sujeto observado, las detecciones de soporte, la clase de protección ausente, la región evaluada, el puntaje y una justificación legible. El fragmento siguiente reproduce la alerta registrada sobre el mismo clip y la misma unidad que el evento anterior, y permite verificar la ventana de confirmación. La alerta transporta el fotograma de la primera evidencia, el 109, y el de la confirmación, el 229. A los 30 cuadros por segundo del clip, esos fotogramas corresponden a 3.633 y 7.633 ms de video, exactamente los 4.000 ms configurados para la condición. Los dos instantes en milisegundos que la alerta también conserva pertenecen al reloj del equipo de control y no al tiempo de video.

{   "schema_version": "control.alert.v1",   "event_type": "alert_event",   "control_run_id": "bench_a_p1_c02_gdino_20260822_20260822T225536Z",   "media_run_id":   "run_20260803_211225_dbe_grounding_dino_1e06f3",   "alert_id": "394c9116-a38d-568d-b620-20d147c4cac9",   "pattern_id": "CR-01", "condition_id": "CR-01",   "subject_key": "CR-01:a_p1_c02", "source_id": "a_p1_c02",   "severity": "high", "state": "open",   "unit_id": "frame_000229", "frame_index": 229, "timestamp_ms": 7633.33,   "evidence": {     "subject": { "detection_id": "det_000001", "label": "person", "confidence": 0.88,                  "bbox_xyxy": [1239.8, 149.8, 1503.2, 861.9] },     "missing_class": "helmet",     "supporting": [],     "score": 0.88, "subjects_in_evidence": 1,     "rationale": "No se encontro evidencia 'helmet' en region 'upper_body' de 1 sujeto(s)."   },   "first_evidence_ms": 41990631.527, "first_evidence_unit_id": "frame_000109",   "first_evidence_frame_index": 109,   "alert_registered_ms": 41990642.511 }

La identidad de la alerta es entonces una función pura de esa quíntupla, con tres consecuencias verificables. Reprocesar la misma evidencia bajo el mismo identificador de corrida reproduce exactamente los mismos identificadores de alerta. La deduplicación no requiere estado compartido entre componentes, porque el módulo de distribución construye su clave de idempotencia a partir del identificador de alerta y la asienta en su propio registro sin consultar al plano de control. Y la identidad se asigna por confirmación y no por episodio, de modo que una confirmación posterior sobre el mismo sujeto recibe identidad propia y la idempotencia no oculta reincidencias reales.

Los contratos admiten además información que la implementación actual no produce, y la sección 17.4.8 informa cómo se ejerció esa capacidad sin romper la compatibilidad.

#### 17.4.3. Servicios, gobierno por configuración y acople

Los tres módulos de la cadena se implementaron como servicios independientes, gobernados por configuración y expuestos mediante HTTP. Cada uno carga su configuración al iniciarse, admite una corrida activa por vez, rechaza las solicitudes concurrentes señalando la que está en curso y los dos planos persisten además la configuración efectiva que utilizaron, que el módulo de distribución expone por su interfaz. El plano de medios carga además el modelo una sola vez al arrancar. Rutas, fuentes, umbrales, ventanas temporales y opciones de instrumentación se declaran en configuración, sin constantes ocultas en el código. La Tabla 57 reúne sus operaciones de gobierno.

**Tabla 57**

*Interfaces principales de los servicios de la plataforma*

| **Servicio** | **Operación** | **Función** |
| --- | --- | --- |
| Plano de medios (:8080) | GET /api/model | Expone el perfil de modelo, dispositivo y umbrales efectivos. |
|  | POST /api/runs | Dispara una corrida con fuente, prompts, parámetros, configuración de bus e identificador de experimento. |
|  | POST /api/runs/{id}/stop | Detiene cooperativamente la corrida en curso y el cierre se propaga a los consumidores por el bus. |
|  | GET /api/runs/{id} | Consulta estado y resumen de la corrida. |
|  | GET /api/runs/{id}/detections | Recupera evidencia perceptiva paginada. |
|  | POST /api/runs/{id}/evaluate | Ejecuta la evaluación de percepción cuando existe referencia aplicable. |
| Plano de control (:8081) | POST /api/runs | Dispara una corrida en modo diferido o en vivo. |
|  | GET /api/runs/{id}/alerts | Recupera las alertas internas registradas. |
|  | GET /api/config | Expone la configuración efectiva de control. |
| Módulo de distribución (:8082) | POST /api/runs | Inicia una corrida de entrega con fuente de alertas, política, canal e identificador de experimento. |
|  | GET /api/runs/{id} | Consulta estado y conteos de entrega; determina cuándo consolidar artefactos. |
|  | POST /api/runs/{id}/cancel | Detiene cooperativamente una corrida de entrega en curso. |
|  | GET /api/config | Expone la configuración efectiva de distribución. |
| Medios → control (:5557) | Bus ZeroMQ publicador-suscriptor (msgpack) | Transporta los eventos de percepción y el ciclo de vida de la corrida dentro del envoltorio versionado del bus. |
| Control → distribución (:5558) | Bus ZeroMQ publicador-suscriptor (msgpack) | Transporta las alertas internas confirmadas hacia el módulo de distribución. |
| Orquestador y consola | Clientes HTTP de los tres servicios | Gobiernan corridas y consolidan artefactos, sin consumir los buses de datos. |

El modelo no se transmite en la solicitud de corrida, de modo que comparar perfiles implica disponer procesos con perfiles distintos en lugar de reconfigurar pesos dentro de una corrida. La decisión mantiene el costo de carga fuera de la ruta crítica y evita estados ambiguos del servicio.

Las operaciones de consulta de configuración y de perfil de modelo permiten verificar antes de disparar que el servicio cargó lo que el experimento requiere. Sin ellas, una discrepancia entre lo configurado y lo desplegado sólo se descubriría en los resultados.

En una corrida en vivo el orquestador inicia primero el plano de control, después el módulo de distribución y por último el plano de medios. El control arranca primero porque debe quedar suscripto al canal de detecciones antes de que los medios publiquen, y la distribución va después porque su corrida se declara contra la corrida de control ya creada. La no pérdida en el canal de alertas no depende de ese orden sino del publicador, configurado por el orquestador para esperar a que haya un suscriptor antes de emitir. Un consumidor suscripto tarde perdería los eventos ya publicados sin ningún error observable, y las dos garantías juntas excluyen esa pérdida por construcción.

La detención de corridas es cooperativa en los dos servicios que la exponen. La solicitud marca la corrida y el hilo de ejecución la observa entre unidades, sin cortes abruptos que dejarían artefactos a medio escribir. El plano de control no expone detención y la asimetría es deliberada, porque su corrida en vivo se cierra con el evento de finalización que publica el plano de medios, con el que mantiene una relación uno a uno. El módulo de distribución sí requiere cancelación propia, porque una corrida de entrega puede quedar a la espera de alertas y debe poder abortarse sin reiniciar el servicio.

Sobre esos servicios se materializan los dos caminos experimentales, que describen cómo circula la evidencia entre los planos según la naturaleza de la ejecución.

En el camino DBE el acople entre planos se realiza por archivo. El plano de medios persiste su registro de detecciones y el plano de control lo relee, de modo que el repositorio de corrida es la fuente de verdad y permite repetir el procesamiento bajo condiciones controladas. En el camino EBE la evidencia se transmite por el bus dentro del envoltorio versionado.

La evidencia se persiste antes de publicarse, y el contenido lógico de la línea persistida y del mensaje transmitido es el mismo, lo que permite reevaluar una corrida en vivo por el camino diferido y reproducir sus artefactos. En los experimentos, los tres servicios se ejecutaron en un mismo equipo con unidad de procesamiento gráfico, el nodo central de procesamiento que describe la sección 17.1.4.1. Los contratos entre módulos no fijan esa topología, y la configuración de cada corrida registra la disposición efectiva.

#### 17.4.4. Configuración efectiva y catálogo de modelos

El conjunto de patrones efectivo del núcleo es el que el catálogo de configuración identifica como cr01_cr02_v2. CR-01, persona sin casco, se configuró con severidad alta, confirmación a los 4.000 ms y resolución a los 2.000 ms. CR-02, persona sin chaleco reflectivo, se configuró con severidad media, confirmación a los 7.000 ms y resolución a los 3.000 ms. Las precondiciones de evidencia exigen confianza mínima de 0,35 y área mínima de 400 píxeles cuadrados para el sujeto, y confianza mínima de 0,25 para el elemento de protección. La región de búsqueda se define de forma relativa a la caja del sujeto. Para CR-01 es la franja superior entre el 0 % y el 45 % de la altura con margen lateral del 12 %, y para CR-02 la franja del torso entre el 25 % y el 85 % con margen lateral del 8 %.

El conjunto opera con granularidad de escena y el motor registra cada confirmación sin supresión, conforme a la decisión de diseño DA-13. La identidad por sujeto se implementó como capacidad activable por configuración del plano de control y se trata en la sección 17.4.8.

El vocabulario activo del núcleo se compone de person como entidad y de helmet y vest como elementos de protección.

El catálogo de perfiles de modelo materializa la sustituibilidad prevista en el diseño. Reúne variantes de Grounding DINO en sus versiones tiny y base, que corresponden a los backbones Swin-T y Swin-B que presenta la sección 15.2.1.1, cada una con resolución de entrada de 800 y de 560 píxeles, y YOLOE-26 en cuatro tamaños, s, m, l y x, todas integradas mediante adaptadores sobre el mismo contrato de salida. Una tercera familia, MM-Grounding-DINO, se integró por el mismo mecanismo y se archivó fuera del catálogo activo tras la evaluación, cuyo resultado informa la sección 17.5.

El núcleo no fija un modelo único. Cada instancia del servicio de medios carga un perfil al iniciarse, de modo que comparar perfiles equivale a disponer instancias distintas bajo la misma configuración de corrida, y el despliegue integral define un servicio por cada uno de los nueve perfiles de servicio del catálogo, y deja fuera los dos perfiles de ajuste fino que se conservan sólo para reproducir su evaluación. Las campañas temporales y en vivo fijan un perfil por corrida, declarado en el manifiesto.

Cada perfil declara sus umbrales y su postproceso en el catálogo. El perfil operativo, fijado por criterio pre-registrado para las campañas temporales y en vivo, es la variante tiny de Grounding DINO con resolución de entrada de 560 píxeles, identificada en el catálogo como gdino-tiny-560, y declara umbral de caja de 0,30 y de texto de 0,25. Su postproceso aplica confianza mínima de 0,25, supresión de solapamientos con IoU de 0,50 y área mínima de caja de 100 píxeles cuadrados, y el control de ritmo opera con selección determinista de paso 1 y una cola máxima de ocho unidades. La inferencia corre en coma flotante de 16 bits sobre la unidad gráfica, una opción de la corrida y no del perfil, y la variante base de 560 píxeles, gdino-base-560, comparte resolución, umbrales y postproceso.

#### 17.4.5. Artefactos y trazabilidad por corrida

Cada ejecución produce un repositorio de artefactos de sólo adición. La organización por componente que reúne la Tabla 58 conserva la evidencia necesaria para reproducir el flujo, analizar fallas y reconstruir una alerta desde su configuración hasta su salida distribuida.

**Tabla 58**

*Artefactos persistidos por componente y experimento*

| **Tramo** | **Artefactos principales** | **Función de trazabilidad** |
| --- | --- | --- |
| Plano de medios | detections.jsonl; metrics.jsonl; errors.jsonl; summary.json; effective_config.yaml; run_manifest.json; run_provenance.json | Reconstruye fuente, unidades procesadas, detecciones, tiempos, errores, configuración, procedencia y versión de código. |
| Plano de control | pattern_events.jsonl; alerts.jsonl; alerts.csv; metrics.jsonl; errors.jsonl; summary.json; effective_config.yaml | Reconstruye transiciones del patrón, alertas internas, evidencia causal, métricas y configuración del motor. |
| Soporte experimental | manifest.effective.yaml; copias de artefactos livianos; referencias a artefactos pesados; report.json; report.md | Agrupa las corridas de ambos planos bajo un experiment_id y consolida el resultado de la ejecución experimental. |
| Distribución | notifications.jsonl (ledger de intentos y entregas, de sólo agregado); dead_letter.jsonl; distribution_summary.json | Relaciona cada intento y resultado de entrega con la alerta interna original sin reescribirla, y conserva por separado los descartes definitivos por agotamiento de reintentos. |

**Nota.** Los nombres de archivo corresponden a los artefactos implementados. Los artefactos pesados se referencian en la ejecución experimental para evitar duplicación, mientras que las configuraciones y reportes se conservan junto al experimento.

La disposición del repositorio del soporte experimental es la siguiente.

runs/<experiment_id>/  (repositorio del soporte experimental)   manifest.effective.yaml   media/    summary.json · metrics.jsonl · effective_config.yaml             detections.ref.json             (referencia al detections.jsonl del plano de medios)   control/  alerts.jsonl · pattern_events.jsonl · metrics.jsonl             summary.json · effective_config.yaml             (y la evaluación temporal, cuando la corrida la habilita)   distribution/  notifications.jsonl · distribution_summary.json                  dead_letter.jsonl               (cuando la corrida habilita el tramo de distribución)   report/   report.json · report.md

La ejecución experimental consolida así los cuatro componentes bajo una misma clave. El manifiesto de corrida registra la versión de código que produjo los artefactos. Junto con la configuración efectiva, el conjunto de prompts y la procedencia de la fuente, ese dato permite reconstruir cada alerta hasta el modelo y la revisión de código que intervinieron. El reporte consolidado declara el estado de aplicabilidad de cada métrica como computada, aplicable no computada, no aplicable o no interpretable, siempre con una causa explícita.

El ledger de entregas del módulo de distribución registra una fila por intento y una más por el descarte definitivo cuando se agotan los reintentos, de modo que la unidad de conteo del tramo es la notificación y no la fila. Al reutilizar un directorio de salida, la generación anterior se archiva íntegra y la deduplicación considera todas las generaciones, para que un reprocesamiento no vuelva a entregar lo ya entregado ni pierda la traza de lo entregado antes.

#### 17.4.6. Banco temporal y referencia humana de evaluación

La evaluación temporal se apoya en una referencia humana de episodios por clip, materializada mediante el esquema clip_gt.v2. La primera generación registraba alertas esperadas por sujeto y fue reemplazada por episodios a nivel de escena y condición, con tiempos en milisegundos y estados de aplicabilidad por clip. Para la anotación se seleccionó CVAT, una herramienta de código abierto con soporte de interpolación temporal y exportación estructurada.

**Adquisición del material.** El banco proviene de dos fuentes con procedencia y grado de control experimental distintos, y esa diferencia se conserva como atributo de cada clip. La primera es un rodaje guionado ejecutado con el hardware real de captura del prototipo. Cada escenario se diseñó en función de una condición de riesgo del núcleo. Un guion segundo a segundo fija la entrada del sujeto en cumplimiento, el inicio diferido de la infracción y su persistencia sostenida durante lapsos muy superiores a las ventanas de confirmación. El guion incluye además escenas negativas y escenas deliberadamente por debajo de ese umbral. Las tomas se registraron con margen temporal adicional respecto del clip previsto, y tanto la grabación como el recorte se hicieron desde la propia consola del prototipo.

La segunda fuente es un lote de obra real no guionada, obtenido de videos públicos e incorporado como bloque separado con criterios de selección definidos de antemano. Reúne material de obra en cumplimiento destinado a medir especificidad y falsos positivos, no sensibilidad, prohíbe concatenar segmentos cortos para fabricar unidades largas y exige que toda exclusión se declare con causa y firma en lugar de descartarse en silencio.

Los videos maestros del lote se obtuvieron de una lista de reproducción pública de YouTube compilada por el equipo (https://www.youtube.com/playlist?list=PLVG3-xIaXtKzAC9JJnZJUY4aBCg0BNPKV, consultada el 8 de septiembre de 2026) y no se redistribuyen. La dirección de origen y la fecha de acceso de cada video se consignan en el anexo de licencias y procedencia de la sección 19.

**Segmentación temporal.** Los videos maestros se conservaron sin modificación y las unidades de evaluación se generaron como clips derivados, con criterios temporales fijados antes de ejecutar las campañas y aplicados como reglas ejecutables. Cada clip del rodaje se recortó con un preludio fijo de 3,5 s antes del inicio de la condición, porque un episodio que arranca en el primer fotograma impide medir el tiempo hasta la primera detección. Lleva además una cola posterior al cierre del episodio de entre 3 y 10 s según el escenario, y un piso de duración que garantiza que una alerta válida pero lenta ocurra dentro del clip.

Ese piso resulta de sumar al inicio del episodio el techo del objetivo de latencia de alerta de su patrón, la ventana de resolución y un margen final, y se verifica mediante un control automático durante la derivación de la referencia. El clip que no lo alcanza no se vuelve a recortar, y sus métricas de latencia y sensibilidad quedan censuradas y así se declaran.

El fundamento del dimensionamiento es bidireccional. Un clip demasiado corto subestima al sistema, porque produce latencias artefactuales y cuenta como omisión una alerta que no tuvo tiempo de ocurrir. Un clip sin tiempo muerto sobreestima la precisión, porque elimina los tramos donde aparecen los falsos positivos. La selección de tomas se hizo por calidad visual de la escena y no por duración, y los límites de todos los clips quedaron congelados bajo control de versiones antes de ejecutar las campañas. Los clips del lote de obra real no se segmentaron, porque recortarlos alteraría el tiempo negativo que ese bloque aporta.

**Preanotación y revisión humana.** La anotación no partió de video crudo. Cada clip se preanotó automáticamente con un detector de vocabulario abierto de mayor capacidad que el modelo evaluado, elección deliberada para evitar circularidad entre el sistema medido y su referencia. Ese detector se acopló a un algoritmo de seguimiento que propone trayectorias por sujeto, con los atributos de protección inicializados por asociación espacial.

Sobre esa propuesta se realizó la pasada humana en CVAT. Esa revisión corrigió las cajas y las trayectorias de los 47 clips del banco, verificó la identidad de cada sujeto a lo largo de la secuencia y asignó los atributos observables tramo por tramo. Marcó como estado desconocido aquellos tramos donde el atributo no resulta observable, en lugar de forzar un valor, y fijó los límites temporales de los 37 episodios de referencia. La interpolación temporal y la preanotación redujeron las operaciones repetitivas, pero no sustituyeron ninguna de esas decisiones. La referencia experimental es el producto de esa revisión. Cuatro clips de un piloto anterior sobre video de obra real, anotados con la misma referencia de atributos y ajenos al banco temporal, se conservaron para la medición del estado por persona que informa la sección 17.5.3. La anotación la realizó un único anotador, sin la doble anotación sobre el 20 % del material que la sección 17.1.5.4 exige para la anotación propia, desviación que la sección 17.5.7 registra como limitación.

**Derivación y congelamiento.** La salida de la anotación se procesa mediante una cadena reproducible de separación, derivación, validación, promoción y agregación. La cadena valida la estructura de cada exportación antes de derivar. La derivación clasifica los episodios con las mismas ventanas de confirmación que utiliza el motor de patrones, de modo que la referencia y el sistema evaluado apliquen un criterio temporal idéntico. Una divergencia entre ambos produciría omisiones ficticias. Las correcciones humanas posteriores se aplican como registros firmados sobre los artefactos versionados, nunca editando la herramienta, y un control automático falla cuando una corrección firmada no aparece en la referencia derivada. Las anotaciones promovidas quedan congeladas bajo control de versiones, con huella criptográfica por clip y un manifiesto agregado del banco. La referencia experimental es la versión promovida en el repositorio y no el estado mutable de CVAT.

#### 17.4.7. Verificación, alcance efectivo y brechas

El criterio de cierre de la implementación exigió que cada unidad funcional produjera evidencia verificable dentro de una corrida y que su comportamiento pudiera repetirse mediante pruebas automatizadas o artefactos persistidos. La Tabla 59 reúne esa evidencia, concentrada en gobierno por configuración, cierre de corridas, paridad entre caminos, determinismo del motor y funcionamiento de la integración.

**Tabla 59**

*Evidencia de verificación técnica del prototipo*

| **Propiedad verificada** | **Evidencia de implementación** |
| --- | --- |
| Servicios ejecutables y gobernados por configuración | Las operaciones de salud, disponibilidad, creación y consulta de corridas operan sobre configuraciones validadas, y cada servicio limita la concurrencia de corridas activas. |
| Cadena DBE de extremo a extremo | La relectura por archivo produce detecciones, transiciones, alertas, métricas, resumen y configuración efectiva, y repetir el camino conserva los artefactos deterministas. |
| Cadena EBE y cierre de ciclo de vida | El consumidor confirma la suscripción antes del productor, la corrida cierra con el evento de finalización y los huecos de secuencia se registran como degradación. |
| Paridad entre repositorio y bus | La evidencia persistida y la transmitida conservan el mismo contenido lógico, y una corrida en vivo puede reevaluarse por el camino diferido. |
| Motor de patrones e idempotencia | Las transiciones respetan las ventanas configuradas y la alerta usa un identificador determinista, estable ante el reprocesamiento de la misma corrida. |
| Distribución de alertas | Se verificaron la relectura diferida, el consumo en vivo, la supresión, la idempotencia, la entrega MQTT con confirmación contra un broker real, el ledger y el reporte. |

**Nota.** La tabla acredita funcionamiento técnico y reproducibilidad. Cada módulo mantiene su propio conjunto de pruebas automatizadas, con el que estas propiedades se vuelven a verificar. No presenta métricas de desempeño del banco experimental, que se informan con sus denominadores y condiciones en la sección 17.5.

La verificación confirmó además que las fallas instrumentales no se convierten en ceros silenciosos, porque una pérdida de bus degrada la corrida, una métrica sin reloj comparable se declara no interpretable y un canal no habilitado se declara no aplicable.

El cierre de la implementación requiere declarar con precisión qué capacidades se ejercieron, cuáles permanecen fuera del núcleo y con qué estatuto, porque no todas las brechas son del mismo tipo.

La concentración del prototipo en el núcleo validable no responde a una reducción tardía del alcance sino a las condiciones de evaluabilidad de cada condición del catálogo. Las de Nivel 1 cuentan con datasets públicos y bancos con verdad de terreno para persona y elementos de protección, lo que permite medir percepción, estado temporal y alerta con denominadores declarados. Las de Nivel 2 y Nivel 3 exigen insumos que el material disponible no provee, y su justificación se desarrolla en la sección 17.5.7. Incorporarlas sin esa base habría producido capacidades no medibles, de modo que el esfuerzo se concentró en llevar el núcleo a capacidad medida. Las doce capacidades del núcleo y la operación sobre fuentes en vivo quedaron implementadas, se describen en las secciones 17.4.1 a 17.4.5 y se ejercieron en las campañas de la sección 17.5.

Dos capacidades opcionales de la Tabla 39 y dos propiedades del diseño quedaron implementadas y medidas. La identidad persistente de sujeto opera como decorador configurable de la fuente del plano de control y constituye una capacidad medida, aunque las métricas formales de seguimiento permanezcan excluidas por falta de anotación de identidad. Las tres estrategias de detección se implementaron y su comparación se ejecutó, con la salvedad de la variante híbrida por conjunción que declara la sección 17.5.6. La distribución de alertas quedó implementada, verificada e integrada a la consola y a la orquestación, con MQTT como canal ejercido. Y la paridad entre la relectura por archivo y el transporte por bus quedó verificada. Los valores de todas ellas se informan en la sección 17.5.

Una capacidad se implementó y se caracterizó fuera del régimen evaluativo. La preselección liviana en el rol de captura funciona como filtro de personas ejecutado en el dispositivo, con criterio de degradación segura y deshabilitada por defecto, y no existe para las fuentes por red. Permaneció deshabilitada en todas las corridas evaluativas, y esa exclusión es deliberada y anterior a los resultados, porque un filtro de cuadros sin persona suprimiría las detecciones sostenidas que la tasa de falsas alarmas existe para medir. La sección 17.5.7 informa su reducción de carga medida.

Las condiciones de riesgo de Nivel 2 y Nivel 3 quedaron especificadas y no implementadas. Su incorporación requiere evaluadores relacionales, zonales o de trayectoria y evidencia adecuada, y por eso no forman parte del núcleo validable.

La gestión de evidencia visual controlada quedó implementada como opción de corrida. El plano de medios puede conservar una previsualización por unidad procesada, con un tope configurable, y un video anotado de la corrida completa. La previsualización viene habilitada por defecto, un valor que invierte la regla de habilitación explícita que el diseño fija para los módulos opcionales, y el video anotado viene deshabilitado. Las campañas del banco declararon apagadas las dos, conforme a la política de minimización de evidencia visual, de modo que los artefactos evaluativos conservan identificadores, metadatos y coordenadas, y no imágenes.

La rama comparativa de ajuste fino se ejerció por completo. El protocolo, la procedencia, el servicio de inferencia, la evaluación y la línea base quedaron congelados, y la escalera de tres tramos, registrada antes de entrenar, se ejecutó entera. Los dos tramos entrenados se evaluaron una única vez contra el banco congelado, sin que ninguno superara los criterios de incorporación, que se firmaron antes de que existiera el punto de control al que se aplicarían. El tercer tramo, que habría ajustado MM-Grounding-DINO como linaje entrenable de Grounding DINO, se cerró con causa técnica por dos razones. La escalera lo condicionaba a que alguno de los dos tramos anteriores alcanzara sus criterios, y ninguno lo hizo. Y la variante que iba a ajustarse entregaba cajas degeneradas con origen en el punto de control publicado, verificado con la biblioteca de referencia sin código del proyecto, mientras que la variante sana de esa familia no había mostrado ventaja en ninguna dimensión evaluada, de modo que el linaje ajustado no habría sido el del perfil operativo. Ninguno se adoptó como modelo de servicio ni entró al despliegue, y sus perfiles permanecen en el catálogo sólo para reproducir la evaluación. Los valores por tramo se informan en la sección 17.5.6.

El subconjunto de ajuste reunió 2.946 imágenes, por encima del rango orientativo de 500 a 2.000 que fija el protocolo, y ese exceso es consecuencia de aplicar la regla de partición y no de apartarse de ella. Se tomó el total de los linajes elegibles después de excluir íntegramente la única fuente que el banco de evaluación incorpora completa y de deduplicar de forma perceptual contra él, sin submuestrear hasta el techo del rango. Los controles de solapamiento con el banco y de componentes compartidos entre entrenamiento y validación quedaron en cero, y la semilla de partición se registró con el resto de la configuración.

El cumplimiento de esa regla tuvo un límite que conviene declarar. Una de las dos fuentes retenidas para el ajuste aporta además el estrato curado del banco de imágenes, de modo que en ese punto la partición se apartó del protocolo, que reserva para el banco a toda fuente que lo integre aunque sus particiones nominales sean disjuntas. Excluirla habría reducido el conjunto de ajuste de 2.946 a 743 imágenes. La desviación se admitió con dos controles verificados, particiones disjuntas y deduplicación perceptual contra el banco en cero, y la retención medida sobre el banco, que incluye ese estrato, se lee con esa salvedad.

La asignación efectiva de las cuatro fuentes de la sección 17.1.6.2 fue la siguiente. SHEL5K y CHV integran el banco de evaluación como los estratos de 5.000 y 1.330 imágenes, y CHV es la fuente que quedó excluida íntegramente del ajuste. construction_site_safety aportó 2.203 imágenes al ajuste y es además el origen del estrato curado de obra, que es la desviación declarada arriba. ppe_siabar aportó las 743 restantes. La retención open-vocabulary se midió sobre las 5.000 imágenes de validación de COCO 2017, un material ajeno al dominio y distinto del estrato de 5.000 imágenes del banco.

El aumento de datos fue el conjunto por defecto de la biblioteca de entrenamiento, mosaico, variación de color, traslación, escala, volteo horizontal y borrado aleatorio, sin ajustes propios, y quedó registrado en la configuración efectiva de cada corrida. El costo fue de 7,7 minutos para el primer tramo y de 23,8 para el segundo, sobre una unidad gráfica NVIDIA A30 del clúster de cómputo.

Los dos tramos entrenados ajustaron la variante s de YOLOE-26 sobre la misma partición de 2.946 imágenes de ajuste y 483 de validación, con imágenes a 640 píxeles de lado, lotes de ocho, semilla fija y ejecución determinista, y en cada uno se conservó el punto de control de mejor mAP50-95 sobre las cuatro clases de validación y no el de la última época. Lo que la escalera varía es el alcance entrenable. El primer tramo entrenó sólo la proyección de clases, 3.096 parámetros, en la modalidad de linear probing que describe la sección 15.2.4. El segundo entrenó el detector completo con las rutas de prompt congeladas, 10,35 millones de parámetros, y modificó además su régimen de época y de optimización por una enmienda registrada antes de observar resultado alguno.

Ese régimen es la segunda diferencia entre ambos. El primer tramo recorrió 10 épocas completas con la selección automática de optimizador de la biblioteca de entrenamiento, y su detención temprana quedó inoperante porque la paciencia configurada superaba ese techo. El segundo fijó un techo de 60 épocas y una detención tras 15 sin mejora, ambos valores registrados antes de observar resultado alguno, y declaró el optimizador de forma explícita, por descenso de gradiente estocástico con tasa de aprendizaje inicial 0,01, momento 0,937 y tres épocas de calentamiento. La detención se activó en la época 16 y la mejor época fue la primera, que es el dato sobre el que se apoya la lectura de colapso durante el entrenamiento.

La declaración explícita del optimizador responde a un hallazgo de una corrida anterior del mismo tramo, descartada por esa causa. El modo automático de la biblioteca de entrenamiento deriva la tasa de aprendizaje del número de clases y no del alcance entrenable, de modo que asignaba el mismo valor a un tramo de 3.096 parámetros y a otro de 10,35 millones. Esa corrida se conservó como evidencia del hallazgo y no como candidata a incorporación.

El prototipo conserva su carácter experimental y asistivo. No implementa reconocimiento de identidad personal, no determina incumplimientos normativos y no reemplaza la supervisión de seguridad, conforme a las salvaguardas de la sección 17.1.10.

#### 17.4.8. Extensibilidad y costo de extensión

La extensibilidad se verificó en dos dimensiones, la incorporación de nuevas capacidades mediante puntos de extensión acotados y la evolución aditiva del evento de percepción. La plataforma no sostiene que toda condición pueda incorporarse sólo con lenguaje, y la Tabla 60 delimita qué cambios requieren configuración y cuáles requieren código nuevo.

**Tabla 60**

*Puntos de extensión y costo técnico de incorporación*

| **Extensión** | **Intervención requerida** | **Costo técnico esperado** |
| --- | --- | --- |
| Condición del mismo tipo: sujeto sin EPP | Entrada declarativa en el conjunto de patrones y formulaciones de prompt, con clase del sujeto, clase ausente, región, umbrales y ventanas. | Sólo configuración. Sin reentrenamiento ni cambios en el motor. |
| Familia nueva de condiciones | Nuevo evaluador para relaciones, zonas, trayectorias u otra semántica no cubierta por el evaluador de ausencia espacial. | Código acotado al evaluador, con los contratos y el resto de la cadena conservados. |
| Modelo de detección | Adaptador que normalice la salida y perfil de modelo en el catálogo. | Código acotado al adaptador y configuración. |
| Fuente visual | Adaptador de ingesta que produzca unidades visuales normalizadas. | Código acotado al adaptador y su validación. |
| Canal de notificación | Implementación de un consumidor del contrato de notificación y su integración de ciclo de vida. | Fuera de los dos planos; no modifica la alerta interna. |
| Dato adicional en la detección | Campo opcional con valor por defecto y consumidor tolerante a su ausencia. | Evolución aditiva sin ruptura del contrato de percepción. |

***Nota****.* La frontera entre la primera y la segunda fila delimita la extensibilidad por configuración. Una ausencia de EPP sobre un sujeto observable reutiliza el evaluador existente, mientras que una relación nueva entre entidades requiere lógica de evaluación específica.

El costo de incorporar vocabulario nuevo se midió en un piloto sobre la clase machinery. No requirió entrenamiento y demandó 48 líneas de configuración y nueve minutos de trabajo. El ejercicio mostró también que la extensión no termina al obtener detecciones, porque la alineación entre el término elegido y el concepto visual debe validarse. La sección 17.5.2 informa su desempeño y los dos fallos semánticos que aparecieron.

La identidad de sujeto recorrió el segundo camino de extensión. Se implementó como un decorador configurable de la fuente de eventos del plano de control, desactivado por defecto y utilizable tanto en el camino diferido como en el camino en vivo. La incorporación no exigió modificar el plano de medios ni romper el contrato de percepción. El identificador se conserva en los artefactos de control y no en los del plano de medios, pero el seguidor, que asocia cajas de persona por solapamiento entre cuadros consecutivos, y el orden del flujo son deterministas, de modo que una relectura reproduce las mismas identidades. Su efecto cuantitativo se informa en la sección 17.5.

El evento de percepción admite además información que la implementación actual no produce, y esa capacidad se ejerció antes de declararse. La detección normalizada incluye un campo de identidad entre fotogramas que ningún productor emite, declarado como opcional con valor por defecto y omitido al serializar cuando no tiene valor, de modo que su presencia no altera un solo byte de los artefactos existentes. El plano de control ya lo consume como clave de estado cuando opera con granularidad por sujeto, y el contrato conservó su versión.

Tres decisiones de implementación sostienen esa propiedad. Los campos nuevos se agregan como opcionales con valor por defecto, los consumidores validan contra su propia declaración del contrato y descartan sin error los campos que no conocen, y la frontera de la distribución admite explícitamente campos adicionales. Cada plano mantiene además su propia declaración del evento en lugar de una biblioteca compartida, de modo que la frontera entre ellos es el esquema serializado y no una dependencia de código, y ambos pueden versionarse y desplegarse por separado.

Lo excluido son las métricas formales de seguimiento multiobjeto y no la capacidad de asociar sujetos. De manera análoga, la velocidad, la dirección, la pose y la segmentación permanecen previstas como campos opcionales, sin presentarse como implementadas.

En conjunto, la implementación materializó la cadena que va del video a la alerta distribuida como un prototipo ejecutable, configurable, reproducible y auditable, que conserva la separación entre planos, opera por archivo o por bus y explicita sus brechas. Sobre esa base, la sección 17.5 evalúa su rendimiento sin atribuirle capacidades que no fueron medidas.

---

## Fuente: `docs/informe/entregable/90-etapa3-texto-extraido.md`

> SHA-256 del bloque: `7d05833d0737d5690c56794048205bebd255bad305352129423109d2f01e9173`  
> Seleccion: cierre de §17.3 (CERRADA, v1.12): los riesgos y el plan de materializacion que §17.4 y §17.5 ya resolvieron; §18 cierra el circulo con ellos.

#### 17.3.11. Riesgos, plan de materialización y cierre

Los riesgos arquitectónicos se formulan como modos de falla observables y se vinculan con una mitigación concreta. La arquitectura no presupone que una mitigación elimina el riesgo, sino que exige instrumentarlo y declarar su efecto sobre la interpretación de la corrida. La Tabla 51 reúne esos riesgos y sus mitigaciones de diseño.

**Tabla 51**

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

El plan de materialización ordena dependencias de diseño y no reemplaza el registro de implementación. El núcleo se construye primero sobre DBE para estabilizar contratos, evidencia, patrones y reporte, y luego se incorporan EBE y las capacidades opcionales sin modificar la semántica del flujo base. La Tabla 52 fija el entregable arquitectónico de cada incremento y el criterio que permite decidir si es verificable. El estado alcanzado por el conjunto de los incrementos corresponde a la sección 17.4.

**Tabla 52**

*Plan de materialización del núcleo*

| **Incremento** | **Criterio de avance** |
| --- | --- |
| Manifiesto y configuración | Una corrida puede reconstruirse mediante experiment_id, configs efectivas y versiones. |
| Fuentes DBE | Imágenes y videos ingresan con identidad, orden y naturaleza temporal declarados. |
| Vocabulario E-IND | Cada detección se atribuye a prompt_set_id y al rol de la clase. |
| Adaptador OVD | El modelo puede sustituirse sin modificar el contrato de percepción. |
| Normalización y postproceso | Las detecciones conservan coordenadas originales, normalizadas y filtros declarados. |
| Persistencia y bus | El hecho se persiste antes de publicarse y toda pérdida resulta detectable. |
| Patrones CR-01/CR-02 | La configuración fija región, granularidad, severidad y ventanas en milisegundos. |
| Alertas internas | Cada episodio confirmado produce una alerta idempotente y auditable. |
| Observabilidad | Cada métrica declara tramo, reloj, unidad, status y cause. |
| Reporte | La salida puede regenerarse desde los artefactos primarios. |

La frontera de extensibilidad distingue tres clases de cambio. Una condición nueva del tipo «sujeto sin EPP» requiere una definición declarativa de patrón y vocabulario, sin modificar contratos ni reentrenar el modelo. Una familia relacional, zonal o de trayectoria requiere un evaluador nuevo en el plano de control. Un modelo, una fuente o un canal nuevos requieren sus respectivos adaptadores y mantienen estables los contratos centrales. Esa frontera evita presentar la extensibilidad open-vocabulary como una capacidad ilimitada, y el costo medido de incorporar extensiones se documenta en las secciones de implementación y evaluación.

El diseño define una plataforma experimental compuesta por el plano de medios, el plano de control, el soporte experimental y un tramo desacoplado de distribución, que protege la ruta crítica, separa la evidencia de su interpretación y conserva una cadena causal reconstruible desde la fuente hasta la entrega. La granularidad de escena y la granularidad de sujeto se tratan como configuraciones semánticamente distintas, y la identidad personal permanece fuera del alcance.

El capítulo deja preparado el paso a la implementación. La sección 17.4 documenta qué componentes se materializaron y cómo se verificaron, y la sección 17.5 concentra las mediciones y su interpretación experimental.

---

## Fuente: `docs/informe/entregable/90f-etapa2-texto-extraido.md`

> SHA-256 del bloque: `e83394eabfd4bd2c6b52735d41c92495d439ee7caf1457bacba005f4f3958324`  
> Seleccion: conclusiones parciales de §17.1 (CERRADA, v1.21): las preguntas que el protocolo dejo planteadas y que §18 responde con lo medido.

#### 17.1.11. Conclusiones parciales de la consolidación metodológica

La consolidación metodológica cierra con un protocolo experimental integrado y ajustado al alcance real del prototipo. El núcleo obligatorio queda en las condiciones de detección directa de Nivel 1, la comparación controlada en DBE se separa de la plausibilidad operativa en EBE, la estrategia de datos evita la filtración entre entrenamiento y evaluación, el framework de métricas se centra en el valor operativo de la alerta y una regla explícita decide cuándo habilitar o descartar la adaptación al dominio.

Las instancias siguientes toman estas definiciones como referencia. El análisis y diseño arquitectónico las traduce en una organización técnica y la validación experimental produce resultados sobre las condiciones, los escenarios y las métricas fijadas, con la instrumentación de t_G2A y t_alert-system definida en la sección 17.1.7. En todos los casos debe declararse qué elementos del catálogo se implementaron, cuáles no aplicaron y cuáles permanecieron condicionados. Esa trazabilidad entre definición metodológica, diseño, implementación y validación es el principal resultado de esta parte del proyecto y sostiene su orientación central, que es evaluar si la detección open-vocabulary puede integrarse como herramienta asistiva para el monitoreo de condiciones de riesgo en construcción civil.

---

## Fuente: `docs/informe/entregable/90d-etapa1-texto-extraido.md`

> SHA-256 del bloque: `e34c1ab06c14bbc2a3e0daf3be80fef31fd0227932ec1cdcb759091b491ed5ff`  
> Seleccion: conclusiones parciales de §16 (v1.4, en revision de los colegas): la vara de literatura contra la que §18 lee los resultados propios. Nunca 'OVD detecta mejor': la tesis es la plataforma y la medicion sin entrenar.

### 16.8. Conclusiones parciales de la fundamentación teórica

El marco teórico sostiene la factibilidad conceptual de una plataforma asistiva que interpreta observables expresados mediante lenguaje sobre video, mantiene continuidad temporal y produce alertas trazables para revisión humana. Esta factibilidad no implica superioridad de OVD frente a detectores supervisados ni habilita conclusiones de cumplimiento desde una observación visual; depende de condiciones evaluables, del comportamiento en el dominio y de restricciones temporales explícitas.

La fundamentación delimita también qué debe resolverse empíricamente: los benchmarks generales no predicen el rendimiento en construcción; una detección por cuadro no equivale a una alerta; un identificador de seguimiento no representa identidad personal; y una capacidad de la literatura no constituye una función implementada. En un campo en evolución, estas separaciones exigen decisiones trazables y validación reproducible.

---

## Fuente: `docs/informe/entregable/desarrollando/auditoria-bibliografica-2026-09-08.md`

> SHA-256 del bloque: `22c8c3ead1f62abe28f482ee57cc2ec352deb54941028e0ccfbf10a61af28a06`  
> Seleccion: AUDITORIA BIBLIOGRAFICA (2026-09-08), insumo directo de §19: cruce de las 242 entradas del listado global contra las citas del texto vigente. **Hallazgo de raiz: el listado del maestro es anterior a las correcciones de la Etapa 1 y le faltan DOCE entradas que si estan en 90e**, lo que deja once citas sin resolver, entre ellas las dos unicas fuentes de vision-lenguaje aplicado a seguridad en obra y la fuente de una fila de la Tabla A.1. Antes de escribir el listado de §19 hay que fusionar 90e en el del maestro. Trae ademas: 104 de 242 entradas huerfanas con las bajas propuestas, 21 preprints que ya tienen version publicada, los defectos de APA del listado, y el plan de correccion ordenado por retorno.

# Auditoría bibliográfica del informe — 2026-09-08

> **Qué es.** Revisión de las citas y del listado de referencias del TFG. El listado global se
> tomó del maestro `desarrollando/E-OVRT-VDP_v1.1_05062026-sin-indice.docx` (export del 09-08);
> las citas válidas, de los cinco documentos de sección cerrados. Responde a seis preguntas: si la
> referencia está bien usada, si quedó huérfana, si está bien citada y sin riesgo de plagio, si es
> pertinente para un TFG, si conviene darla de baja, y qué más mirar antes de entregar.
>
> **Método, en dos capas.** Una **mecánica y reproducible**: se parsearon las 242 entradas y se
> extrajeron las citas de las diez piezas vigentes, y se cruzaron; todo número de este documento
> sale de ese cruce. Una **de lectura**: cinco auditorías en paralelo sobre el uso de cada cita en
> su contexto. **Cada hallazgo de la segunda capa se re-verificó contra el texto antes de entrar
> acá.** Los que no se pudieron confirmar no figuran.
>
> **Qué NO es.** No es un pase: no toca ningún `.docx`. Es el insumo para decidir qué corregir.

---

## 1. Veredicto en cinco líneas

El criterio bibliográfico del trabajo es maduro y en varios tramos ejemplar. No hay fraude, ni
apropiación, ni una sola transcripción literal sin atribuir. Lo que hay son tres cosas que un
jurado ve antes que el mérito. **La cadena entre la cita y la referencia está rota en trece
puntos**, y la causa es que el listado del maestro nunca se sincronizó con las correcciones de la
Etapa 1. **§17.5 reporta resultados sin invocar ninguna de las varas que §15 ya tiene relevadas.**
Y **§11–§14 no tiene una sola referencia**, incluida la premisa que justifica todo el trabajo.

Ninguno exige investigación nueva. Son fusiones, remisiones y citas puntuales, más una tanda de
higiene de formato. Sin esa pasada, el flanco más fácil de atacar es 15.2.5.4, porque es la
subsección que fundamenta por qué el trabajo existe y apoya sus cuatro cifras clave en una
referencia que el lector no puede encontrar.

---

## 2. Qué se comparó, y cuánto se cita

El listado global tiene **242 entradas**. Las citas se tomaron de las piezas que hoy son el
informe, no del cuerpo viejo del maestro, cuyas §15, §16, §17.1 y §17.3 quedaron superadas.

| Pieza | Palabras | Citas | Densidad |
|---|---:|---:|---|
| §11–§14 Glosario, Introducción, Objetivos y Plan (maestro) | 4.523 | **0** | — |
| §15 + §16 Estado del arte y Marco teórico (v1.4) | 18.670 | 169 | 1 cada 110 palabras |
| §17.1 Consolidación metodológica + Anexos C y D (v1.21) | 16.950 | 26 | 1 cada 651 |
| §17.3 Diseño arquitectónico (v1.12) | 14.128 | **0** | — |
| §17.4 Implementación (v1.15) | 7.483 | 1 | 1 cada 7.483 |
| §17.5 Evaluación y validación | 4.833 | **0** | — |
| Anexo A, matrices comparativas (90e) | 3.980 | 161 | 1 cada 24 |
| Anexo B, infraestructura (maestro) | 1.801 | 9 | 1 cada 200 |

Que §17.3 y §17.4 casi no citen **no es un defecto**: describen diseño y construcción propios. Que
§17.5 y §11–§14 no citen sí lo es, por razones distintas, y se tratan en los puntos 5 y 6.

---

## 3. Lo más grave, y su causa: el listado del maestro quedó viejo

Trece citas no resuelven contra el listado. Un lector busca la referencia y no la encuentra: en la
práctica es indistinguible de una cita inventada, y es lo primero que prueba un jurado.

**Pero la causa no es que falte investigar.** El listado corregido de la Etapa 1, que vive en
`90e-etapa1-anexo-a-y-referencias.md`, tiene **102 entradas**, y **doce de ellas no están en las
242 del maestro**. Verificado una por una:

> Chen y Zou (2025) · Choi y Greer (2024) · Kumar et al. (2022) · Lee et al. (2023) ·
> NVIDIA (s. f.-g), TAO Toolkit · NVIDIA (s. f.-h), Triton · OASIS (2019), MQTT 5.0 ·
> Thrush et al. (2022), Winoground · Ultralytics (2026), YOLO26 · UNESCO (2021) ·
> Yuksekgonul et al. (2023), ARO · Zhou et al. (2022), Detic

Es decir: **el listado global del maestro es anterior a las correcciones de la Etapa 1 y nunca se
sincronizó.** Diez de las once citas irresolubles se arreglan **fusionando `90e` en el listado del
maestro**, no buscando fuentes nuevas. Es la corrección más barata y más importante de toda esta
auditoría, y explica por qué las citas que faltan son justo las mejores: son las que la Etapa 1
agregó al corregirse.

**Las que quedan sin entrada aun después de fusionar** son dos, y sí requieren alta nueva:
**Liang y Han (2024)**, declarada «referencia primaria» de OVT-B en §17.1.6.4, y **Liu et al.
(2023)** del Anexo B, que además parece un error de año por Liu et al. (2024).

**El detalle de las citas irresolubles, con lo que sostiene cada una:**

| Cita | Dónde | Qué sostiene |
|---|---|---|
| **Choi y Greer (2024)** | §15.2.5.4 y Tabla 5 | las cuatro cifras del único antecedente OVD × EPP publicado |
| **Chen y Zou (2025)** | §15.2.5.4 | IoU bajo 20 % en objetivos con restricción de atributo |
| **Yuksekgonul et al. (2023)** | §16.3.4 | ARO, 50.000 casos |
| **Thrush et al. (2022)** | §16.3.4 | Winoground, desempeño no mejor que el azar |
| **Kumar et al. (2022)** | §15.2.4 | degradación fuera de distribución al ajustar |
| **Lee et al. (2023)** | §15.2.4 | ajuste selectivo de capas |
| **Ultralytics (2026)** | §15.2.1.2 | la advertencia que separa YOLOE-v8 de YOLOE-26 |
| **NVIDIA (s. f.-g) y (s. f.-h)** | §15.4.3.2 | TAO Toolkit y Triton; la serie del listado llega a `-f` |
| **OASIS (2019)** | §15.4.2 y §16.5.3 | MQTT, idempotencia y reentregas |
| **Liang y Han (2024)** | §17.1.6.4 | OVT-B, declarada «referencia primaria» |
| **Liu et al. (2023)** | Anexo B | ajuste fino y partición disjunta |

Las dos primeras y las dos de composicionalidad son las que más pesan: **Choi y Greer sostiene la
brecha que justifica el trabajo**, y Yuksekgonul y Thrush sostienen todo el argumento por el cual
CR-01 se formula por ausencia. Las cuatro están en `90e` y ninguna en el maestro.

El mismo desfase golpea a los anexos, y ahí rompe la cadena de verificación: la nota de la Tabla
A.1 cita a «X. Zhou et al. (2022)» para la fila de Detic, y esa entrada existe en `90e` pero no en
el maestro, de modo que **las cifras de Detic quedan sin fuente verificable en el documento
entregado**. La nota de la Tabla B.5 cita «Liu et al. (2023)», que no existe en ningún lado, y la
de la Tabla B.2 cita «Luxonis, s. f.-a», que tampoco.

**Con entrada, pero el año o el sufijo no coinciden.** Se corrige en un lado o en el otro:

| Cita | El listado tiene |
|---|---|
| Minderer et al. (2023), 4 apariciones | 2022 y **2024** para el mismo paper de OWLv2 |
| Axis Communications AB (s. f.), en §17.1.7.5 | 2015 |
| Luxonis (s. f.-a) | sólo `s. f.-b`, que además queda como «-b» sin «-a» |
| IDEA-Research (2024a) y (2024c) | tres entradas de 2024 **sin sufijo** |
| Zhou et al. (2022), en §17.1 | 2022a y 2022b |

Verificadas y **descartadas como falsas alarmas**: Agencia de Acceso a la Información Pública,
Advanced Micro Devices, DASH Industry Forum, ISO/IEC, UNESCO y NVIDIA Corporation resolvieron bien
contra el listado; eran artefactos de la extracción automática.

---

## 4. Citas mal usadas: un patrón, no casos sueltos

No son descuidos aislados. Hay una tendencia a **estirar la fuente** hasta la conclusión que el
párrafo necesita, y otra a **hacer cargar afirmaciones metodológicas a documentación comercial**.

**La fuente no trata el tema de la afirmación**

- §16.4.1: «pueden reducir la carga cognitiva y la fatiga de alerta asociada con falsos positivos
  frecuentes **(Du et al., 2024)**». Du et al. (2024) es *Exploring the State-of-the-Art in
  Multi-Object Tracking*, un survey técnico que no estudia fatiga de alerta.
- §15.2.5.2 y §16.4.1: la inestabilidad cuadro a cuadro atribuida a **Xiao et al. (2024)**, que es
  un paper de imagen estática y no mide estabilidad temporal. La segunda cita además generaliza a
  todos los OVD lo dicho de un modelo.
- §15.4.1.2: latencia, transporte seguro y control de congestión de WebRTC apoyados en
  **Keranen et al. (2018)**, que es el RFC de ICE y trata NAT traversal. La especificación de W3C
  está en el listado y no se cita ahí.
- §15.2.5.3 y §16.3.3: la sensibilidad del prompt **en detección** apoyada en **Zhou et al.
  (2022b)**, que es CoOp, sobre clasificación con CLIP. El propio informe advierte dos párrafos
  antes que lo de clasificación «no se transfiere directamente al contexto de detección».
- §15.2.5.1: «compatibilidad textual evaluada de manera independiente para cada región candidata
  (Zareian et al., 2021; **Liu et al., 2024**)». §15.2.1.1 describe a Grounding DINO como fusión
  profunda en el decoder, es decir lo contrario.
- §16.3.4: el solapamiento léxico y la negación atribuidos a **Liu et al. (2024)**, que no estudia
  ninguno de los dos.

**Cifra publicada atribuida a un repositorio o a una ficha de modelo**

- §15.2.1.1: los AP de MM-Grounding-DINO citados como «(IDEA-Research, 2024c; X. Zhao et al.,
  2024)». MM-Grounding-DINO es de OpenMMLab, y el paper está en la misma cita: alcanza con él.
- §15.2.1.3: los AP de OWLv2 **L/14 y G/14** citados con «(Google, 2022, 2023; …)», donde
  Google (2023) es la ficha de `owlv2-**base**-patch16-ensemble`, que no puede sostener cifras de
  las variantes grandes. Para la licencia de los pesos, en cambio, la ficha es la fuente correcta.

**Documentación de fabricante cargando una conclusión metodológica** (§17.1.4.1, cuatro casos):
HP Inc. sosteniendo que el hardware condiciona resolución, precisión numérica y elección de
runtime; Luxonis sosteniendo el reparto de roles entre borde y CPN; la página de producto del
Video Codec SDK de NVIDIA sosteniendo el efecto sobre el reparto CPU/GPU, cuando la guía de NVDEC,
que sí lo trata, ya está en el listado; y los papers de Grounding DINO y YOLOE sosteniendo
compatibilidad de frameworks y rutas de inferencia acelerada, que no es lo que esos papers tratan.

**Afirmación de consenso sobre una sola fuente, que es la proponente del método**: §15.2.5.3,
«Se demostró que la optimización automática de representaciones de prompts […] supera
consistentemente a los prompts elaborados mediante ingeniería manual (Du et al., 2022)».

---

## 5. Riesgo de plagio: dónde está y dónde no

**No hay transcripción literal sin atribuir.** En todo el informe hay sólo dos fragmentos
entrecomillados largos: una salida del propio sistema y el título de un paper. Tampoco se detectó
prosa que parezca traducida de un abstract. El riesgo formal más común no está presente.

El riesgo real es otro: **vocabulario y definiciones de terceros presentados en primera persona**.

**Definiciones de métricas y términos ajenos sin atribuir**

- §17.1.6.4: «**TETA** es Track Every Thing Accuracy y se descompone en LocA, ClsA y AssA». Es la
  definición de una métrica de terceros y su fuente, Li et al. (2022), **ya está en el listado**.
  Contrasta con MOTA, IDF1 y HOTA, que sí llevan sus tres fuentes en §17.1.7.3. Es el hueco de
  atribución más nítido del informe.
- §17.1.7.5 y Anexo D: «**G2A** = Glass-to-Algorithm», definido dos veces sin citar a Bachhuber et
  al. (2018), que acuñó el término, y además **con la frontera estrechada**: el original arranca en
  el vidrio y acá arranca en el `dequeue`. El texto es honesto en lo técnico, dice «No equivale a
  sensor → algoritmo»; le falta la atribución y una línea que declare el cambio de frontera.
- §17.1.5.4: intervalos de confianza «obtenidos por **bootstrap**», sin fuente, en un párrafo donde
  kappa sí está atribuida a Cohen.
- §15.3.1 y §16.4.2: **el algoritmo húngaro y el filtro de Kalman** se nombran sin cita. Ver el
  punto 8.

**Patrones y estilos de arquitectura descritos como acuñación propia** (§17.3): publicación-
suscripción y su semántica de pérdida por suscripción tardía, tubos y filtros («El flujo interno se
organiza como una cadena de transformación progresiva…»), el patrón adaptador —que es el mecanismo
de sustituibilidad de toda la arquitectura, en DA-05—, el registro de sólo adición, la clave de
idempotencia y el ledger de entregas, la taxonomía de requisitos no funcionales de la Tabla 40, y
`fail-open`, introducido con un «denominado» que lo presenta como acuñación del trabajo. El listado
ya tiene a Bass, Clements y Kazman (2022) y no se lo cita nunca.

**Tecnologías centrales sin ninguna entrada en las 242 referencias**, verificado uno por uno:

| Tecnología | Dónde carga peso |
|---|---|
| **ZeroMQ** | §17.3.3 justifica su adopción por latencia y ausencia de broker |
| **msgpack** | §17.3.3 afirma que «reduce el costo de serialización respecto del texto plano» |
| **MQTT** | §17.3.7 y §17.4.1; es el único canal de entrega ejercido del sistema |
| **CVAT** | §17.4.6; con ella se construyó toda la referencia humana de evaluación |
| **Swin Transformer** | §17.4.4 remite a §15.2.1.1 por los *backbones*, que no tienen fuente |

**Y el hallazgo más serio de §17.4**: el detector de vocabulario abierto y el algoritmo de
seguimiento que **preanotaron la verdad de terreno** no se nombran, ni con versión ni con cita
(«Cada clip se preanotó automáticamente con un detector de vocabulario abierto de mayor capacidad
que el modelo evaluado, elección deliberada para evitar circularidad»). Sin identificarlos, el
argumento de no circularidad no se puede auditar ni la referencia se puede reproducir. En la misma
línea, la biblioteca de entrenamiento cuyo comportamiento interno justifica descartar una corrida
entera tampoco se nombra, y ni la biblioteca de validación visible en el propio fragmento de código
ni el framework HTTP aparecen en ningún lado.

---

## 6. §17.5 reporta sin vara, teniendo la vara al lado

§17.5 tiene **cero citas** en 4.833 palabras. Que las cifras propias salgan de artefactos del
proyecto está bien. El problema es que **ninguna se lee contra una cifra publicada**, y §15 tiene
relevadas y citadas exactamente las que hacían falta. Verificado que existen en §15:

| Lo que §17.5 reporta | La vara que §15 ya tiene |
|---|---|
| mAP50 0,551, «el más alto en el agregado» | «YOLOR alcanzó un mAP@0,5 de 0,883 sobre SHEL5K»; «YOLOv5x alcanzó un mAP@0,5 de 0,866 sobre CHV» |
| recall de CR-01 por evidencia directa, 0,308 y 0,599 | «la clase *head* —cabeza sin casco— alcanzó 0,1024 AP» zero-shot, y «AP@0,5 de 0,907 para la clase head» supervisado |
| p95 de 630 a 890 ms, «fuera del presupuesto» | «La literatura reporta órdenes de 10–30 ms para alternativas one-stage optimizadas y 50–150 ms para Transformers» |
| 1,16 a 4,42 fps en vivo | la tabla de puntos de operación publicados de §15.2.3.1 |

Además, en §17.5 **los dos datasets que aportan el 98 % del banco no se nombran** («obra con mayor
cobertura de chaleco», «una fuente con clase nativa de cabeza descubierta» son CHV y SHEL5K, ambos
en el listado), el modelo campeón aparece sólo con su alias interno, Grounding DINO no se nombra ni
una vez, COCO 2017 se usa como material de retención sin citar a Lin et al. (2014), y las métricas
excluidas —las de seguimiento multiobjeto— se declaran no ejecutadas sin nombrarlas: una exclusión
sólo es defendible si el lector sabe qué se excluyó.

El arreglo no es investigación nueva. Es tejer §17.5 con §15 y §16 mediante remisiones y una docena
de citas que ya están en el listado. **Cuidado con una trampa**: la vara más pertinente, Choi y
Greer (2024), es una de las que no tienen entrada. Hay que darla de alta antes de apoyarse en ella.

---

## 7. §11 a §14: cuatro mil quinientas palabras sin una sola referencia

Ni una. El párrafo de apertura afirma que la seguridad laboral en la construcción «constituye un
problema de alta relevancia técnica, social y organizacional» y caracteriza la limitación del
vocabulario cerrado, todo sin fuente. Es el lugar donde un jurado pregunta «¿según quién?», y es lo
primero que se lee.

Hay una buena noticia dentro: **el informe no arriesga ninguna cifra de accidentología, costo ni
adopción sin respaldo.** No dice «el X % de los accidentes fatales en obra». Ese error clásico no
está. Lo que hay son tres afirmaciones sustantivas presentadas como sentido común:

- «Los sistemas tradicionales de detección de objetos operan, en general, bajo un paradigma de
  vocabulario cerrado». Es **la premisa que justifica el trabajo entero**, y Zareian et al., Gu et
  al. y Liu et al. están en el listado exactamente para eso.
- «La observación humana continua puede verse afectada por fatiga, distracciones, simultaneidad de
  eventos o limitaciones propias de la atención sostenida». Afirmación empírica sobre atención
  sostenida, sin fuente, y es la que sostiene la utilidad del sistema frente al supervisor humano.
- §14.2.1 anuncia una revisión de la normativa de seguridad en construcción y §13.2 fija como
  objetivo analizar los fundamentos normativos, sin nombrar ni una norma, teniendo el Decreto
  911/96, el Decreto 351/79, la Ley 19.587 y dos resoluciones de la Superintendencia en el listado.

En §11, el glosario define MOTA, IDF1 y HOTA sin atribución, cuando el Anexo A sí las cita. Es
incoherente hacia adentro.

El trabajo **tiene con qué responder**: todo está en §15, §16 y §16.2.1. Falta traerlo. Es la
corrección de mayor retorno de la auditoría: entre seis y diez citas bien puestas.

---

## 8. Huérfanas, bajas, y el paper de 1955

**104 de las 242 entradas están huérfanas: el 43 %.** Se verificó dos veces, por clave autor-año y
después buscando el apellido cerca del año; el segundo paso rescató 31 entradas que sí estaban
citadas. La causa es conocida: la Etapa 1 podó el estado del arte a menos de la mitad y la
reestructuración de §17.1 recortó otro 35 %. El texto se achicó; el listado no.

| Tema de las huérfanas | Cuántas |
|---|---:|
| Streaming y protocolos de transporte | 32 |
| Borde, niebla, nube y benchmarks de hardware | 21 |
| Documentación de producto: Intel, GStreamer, FFmpeg, Mesa, drivers | 33 |
| Seguimiento y asociación de datos | 9 |
| Detección, OVD y datasets | 9 |

**Bajas propuestas, en orden de seguridad.** Ninguna es obligatoria: una huérfana no invalida nada,
sólo infla el listado y delata que el texto se recortó sin revisar la bibliografía.

1. **Las 53 de streaming y de borde.** §15.4 y §16.5 siguen existiendo y siguen bien sostenidas,
   con 22 fuentes cada una y densidad de 1 cada 110 palabras. Se pueden dar de baja sin dejar
   ninguna afirmación sin respaldo.
2. **Las 33 de documentación de producto** que ya no sostienen nada. Son las que más bajan la
   proporción de literatura arbitrada del listado.
3. **Las 18 de seguimiento y detección, una por una**: son las más cercanas al núcleo. Varias
   conviene conservarlas **citándolas**, no dándolas de baja.
4. **Ninguna de normativa y legislación**, aunque quede huérfana: en un trabajo sobre seguridad
   laboral el marco legal completo tiene valor propio. Sí conviene verificar la vigencia de la
   Disposición 11/2006 frente a la normativa posterior de la AAIP.

**El paper viejo es Kuhn (1955)**, «The Hungarian method for the assignment problem», la entrada
más antigua del listado, y **está huérfana**. Pero la baja directa no es la respuesta, porque el
texto sí nombra el algoritmo dos veces sin atribuir, en §15.3.1 y en §16.4.2, y hay una asimetría:
el **filtro de Kalman se nombra y no tiene ninguna entrada**. Recomendación: citar a Kuhn donde el
algoritmo aparece por primera vez y dar de alta a Kalman (1960). Son los dos clásicos que sostienen
a SORT, y una fecha de 1955 no es un defecto cuando lo que se cita es el origen de un método
vigente. La alternativa, tratar ambos como conocimiento de manual y dar de baja a Kuhn, también es
defendible; lo que no se puede es dejarlo como está. Corregir además «Húngaro» a «húngaro».

**Cohen (1960), la segunda más antigua, está bien y no se toca**: §17.1 la cita para definir kappa
y §17.5 declara que «La referencia temporal no tuvo doble anotación ni medida de acuerdo entre
anotadores». El protocolo prescribe, el resultado informa que no se ejerció. Único retoque: §17.5
no nombra la métrica, así que el lazo queda implícito.

**Y al revés: cuatro entradas del listado que §15/§16 debería usar y no usa.** Abdalwhab et al.
(2025), sobre modelos open-vocabulary en obra, es exactamente el cruce que §15.2.5.4 declara vacío,
y sólo se cita en §17.1. Con Yao et al. (2024) sobre OVDEval, Nath et al. (2020) y Duan et al.
(2022) sobre SODA pasa algo parecido. Su ausencia es el flanco más fácil de atacar cuando se
declara una brecha.

**Una brecha declarada sin protocolo de búsqueda.** «El relevamiento de publicaciones entre 2023 y
2026 no identificó evaluaciones de Grounding DINO o YOLO-World zero-shot sobre SHEL5K o CHV» y tres
subsecciones enteras de §15.4.3 con cero citas afirman qué **no** existe en la literatura. Una
afirmación negativa sobre el estado del arte necesita decir cómo se buscó: bases, cadenas, ventana
y fecha de corte. Alcanza con una nota metodológica.

---

## 9. Defectos de forma

**Entradas que comparten autor y año sin distinguirse.** IDEA-Research (2024) ×3 sin sufijo, y el
texto cita 2024a y 2024c. Roboflow (2025) ×2, ambas del 14 de noviembre. **NVIDIA aparece con dos
nombres de organización**, «NVIDIA» y «NVIDIA Corporation», y eso produce **dos entradas «s. f.-a»,
dos «s. f.-b» y dos de 2022**: una cita a «NVIDIA, s. f.-a» hoy es irresoluble. Hay que unificar el
nombre y renumerar toda la serie. En cambio Ren, T. (2024) ×3 **no es un error**: el texto los
distingue con «Ren, Chen, et al.» y «Ren, Jiang, et al.», que es la forma prevista.

**Homónimos sin inicial.** APA pide la inicial cuando dos autores distintos comparten apellido y
año. El informe lo hace bien con Li y Zhao, y no lo hace en **Jiang et al. (2024)**, 6 citas, con
Jiang, K. y Jiang, Q. en el listado; **Yao et al. (2024)**, 5 citas, con Yao, L. y Yao, Y.; y
**Zhang et al. (2022)**, 3 citas con inicial y 1 sin ella. En el caso de Jiang la ambigüedad cambia
la fuente: sin inicial, la cita sobre prompts visuales resuelve al trabajo equivocado.

**Dos estilos de conjunción conviviendo.** El listado usa «&» en 129 entradas y « y » en 8; en el
texto, las nueve citas de dos autores usan «&» y ninguna usa « y ». Para un TFG en español bajo APA
corresponde « y » en los dos lados. Reemplazo mecánico, pero hay que hacerlo simultáneo.

**Idioma y formato de fecha mezclados**: «Retrieved» en 16 entradas y «Recuperado» en 30; meses en
inglés en 28, en español en 16, y un tercer formato «(1996, 5 de agosto)» en 3.

**Orden alfabético**: correcto salvo un par, que se resuelve al unificar el nombre de NVIDIA.

**«SRT» es ambiguo en un informe de streaming.** El listado usa la sigla como autor para las
resoluciones de la Superintendencia de Riesgos del Trabajo, sin desarrollarla, y a la vez cita el
protocolo Secure Reliable Transport. Una cita «(SRT, 1997)» no se lee. Desarrollar el organismo.

**Cuatro estilos distintos para la legislación argentina** conviven en el listado: autor-país
(«Argentina, 2000»), norma como autor con fecha duplicada («Decreto 911/96 de 1996… (1996, 5 de
agosto)»), «Ley 19.587 de 1972… (1972)» y sigla de organismo («SRT, 1997»). Elegir uno.

**Fechas de consulta donde no corresponden**: 7 entradas de arXiv y 7 de GitHub las llevan, y APA
las reserva para contenido diseñado para cambiar. Nueve entradas arrastran el identificador de
arXiv dentro del título, entre corchetes, y dieciséis dicen «Recuperado» seguido directamente de
la URL, sin fecha.

**Entradas puntuales que un jurado señalaría**: «Stephen. (2026)» como autoría por nombre de pila,
con la etiqueta de lenguaje de GitHub tomada por descriptor de medio; «Go Packages» como autor,
que es un índice autogenerado y cuya fuente real ya está en el listado; la especificación de RTMP
enlazada a un anexo de litigio de la oficina de patentes; una entrada de Intel con el título
truncado con puntos suspensivos; y un artículo con tres de sus cuatro autores sin invertir, que
además rompe el orden alfabético.

**Una entrada pide justificación explícita**: Mazor et al. (2021), un *registered report* de
neurociencia de la conciencia. Si el cuerpo no la ancla con precisión, es la primera que van a
preguntar.

**Una URL cruda en el cuerpo**: la lista de reproducción de §17.4.6 aparece como dirección entre
paréntesis. Debería ser entrada del listado, con el detalle por video en el anexo de licencias.

**Rangos de latencia de la Tabla 8 sostenidos en fuentes no arbitradas.** La nota atribuye los
rangos a quince fuentes, pero ninguna RFC ni especificación publica latencias extremo a extremo:
los números sólo pueden venir de Roy (2024), un post del blog de Wowza, y de Sonono (2019), una
tesis de maestría. Hay que declarar que el origen es industrial, o reemplazarlos. El mismo problema,
sin ninguna cita, en §15.4.1.2: «RTSP/RTP puede operar aproximadamente entre 200 y 800 ms […]
valores de entre 1.000 y 2.000 ms o más».

---

## 10. Lo que está bien, y conviene no tocar

- **Autocontención impecable en las cinco secciones.** Ni un ADR por número, ni una ficha, ni una
  ruta del repositorio, ni un guion propio citados como fuente. Verificado con búsqueda exhaustiva.
  Los nombres de archivo de §17.4 son artefactos de salida del sistema y su nota los legitima.
- **Las diez tablas de §15 y §16 declaran fuente y llevan nota.** La Tabla 3 aclara que su columna
  de latencia se derivó de la tasa publicada y «no corresponde a una medición independiente». Ese
  cuidado es lo que un jurado espera y rara vez encuentra.
- **§17.1 atribuye bien lo más expuesto**: AP@0,5 a Everingham y Lin, MOTA, IDF1 y HOTA a
  Bernardin, Ristani y Luiten, kappa a Cohen, el *template* a Radford, el costo del vocabulario a
  Cheng, Wang y Liu.
- **§17.5 es sobria y honesta**: declara denominadores, separa estratos, distingue no computable de
  cero, marca censuras y reporta veredictos negativos pre-registrados.
- **La composición del listado es defendible**: 90 entradas con DOI y 36 preprints suman más de la
  mitad. La documentación de fabricante está donde tiene que estar, en el Anexo B y en el capítulo
  de medios: no existe paper arbitrado que diga qué codecs soporta un decodificador de una placa
  concreta. Las entradas normativas **son** fuente primaria, no un sustituto de una.
- **La nota de la Tabla A.1 hace lo correcto con una matriz comparativa**: declara sus diecisiete
  fuentes, advierte que «las cifras conservan el protocolo, el conjunto de evaluación y el hardware
  informados por cada fuente; por ello, no constituyen un benchmark homogéneo» y marca N/D donde no
  hay dato. Verificadas las veinte filas: cada modelo tiene su fuente. Eso desactiva el riesgo real
  de plagio en el lugar donde más suele aparecer. Le falta sólo una cosa: la columna de licencias
  no tiene atribución propia, y no puede salir de los papers, que no declaran licencia de pesos.

---

## 11. Plan de corrección, por retorno

1. **Fusionar el listado de `90e` en el del maestro.** Doce entradas, ya redactadas y corregidas,
   que resuelven diez de las once citas irresolubles. Es media hora de trabajo y es lo que más
   cambia. Después, **dar de alta sólo dos**: Liang y Han (2024) para OVT-B, y corregir el «Liu et
   al. (2023)» del Anexo B.
2. **Unificar cinco años y sufijos**: Minderer, Axis, Luxonis, IDEA-Research y Zhou.
3. **Dar de alta las tecnologías que sostienen decisiones**: ZeroMQ, msgpack, CVAT y Swin
   Transformer, y nombrar el detector y el seguidor que preanotaron la verdad de terreno. MQTT ya
   queda cubierto por OASIS (2019) al fusionar `90e`.
3-bis. **Reemplazar veintiún preprints por su versión publicada.** DETR, CLIP, SAM, LVIS, GLIP y
   GLIPv2, la trilogía DetCLIP, OV-DETR, Deformable DETR, DaViT, MaPLe, X-Decoder, APE, OWLv2,
   TETA, MLPerf, LLMDet y las dos fundacionales de OVD, Zareian et al. y Gu et al., están
   publicados en CVPR, ECCV, ICCV, NeurIPS, ICML, ICLR e ISCA. El listado ya lo hace con Grounding
   DINO y con OWL-ViT, así que la inconsistencia es interna. **Sube la proporción de literatura
   arbitrada del 37 % al 46 % sin agregar una sola fuente.**
4. **Atribuir lo que ya tiene fuente en el listado**: TETA a Li et al. (2022), G2A a Bachhuber et
   al. (2018), los patrones de arquitectura a Bass, Clements y Kazman (2022).
5. **Poner citas en §11–§14**, trayendo las que ya están en §15, §16 y §16.2.1.
6. **Tejer §17.5 con las varas de §15**, con remisiones y una docena de citas ya disponibles.
7. **Desdoblar las siete citas estiradas** del punto 4, y degradar las cuatro fuentes de fabricante
   a lo que sí prueban.
8. **Agregar iniciales** a Jiang, Yao y Zhang; unificar «&» por « y »; unificar idioma de fechas.
9. **Declarar el protocolo de búsqueda** que sostiene las brechas.
10. **Decidir las bajas** del punto 8, empezando por las 53 de streaming y borde.

---

## 12. Hallazgo posterior, del mismo día: la Figura 4.3 contradice al sistema

No es bibliográfico, pero apareció al escribir la guía de figuras y es del mismo orden de gravedad,
porque **un lector confía en el dibujo más que en el párrafo**. Verificado contra el motor de
patrones del plano de control, leyendo el código, no la documentación.

| Lo que la Figura 4.3 dibuja hoy | Lo que hace el sistema |
|---|---|
| `candidate → inactive`, «evidencia insuficiente / no persiste» | desde `candidate` el patrón va a **`resolved`**, no a `inactive` |
| `resolved → inactive`, «cierre del episodio» | **no existe ninguna transición hacia `inactive`**: es sólo el estado inicial y nada vuelve a él |

Faltan además tres cosas que el sistema sí hace: el **salto directo a `confirmed`** cuando la
primera evidencia ya cumple la ventana; la **reapertura desde `resolved`**, que es la que produce
las re-alertas que §17.5 contabiliza aparte de los falsos positivos; y los **dos caminos distintos**
por los que se llega a `resolved`, despeje sostenido y ausencia por expiración.

**El texto de 17.3.6.1 arrastra el mismo error**, en dos oraciones: «el episodio pasa a resolved y
retorna a inactive» y «el patrón vuelve a inactive sin generar una alerta». §17.3 está cerrada, así
que la corrección la decide el autor. La versión correcta y completa, lista para dibujar, está en
la sección 5.3 de `../../figuras/GUIA-DE-FIGURAS.md` (fuente: `docs/informe/figuras/GUIA-DE-FIGURAS.md`).

---

## 13. Fuera de la bibliografía, para la entrega

- **§17.2 «Costos asociados» dice `[Pendiente]`**; §17.6 y §18 dicen `[Agregado futuro]`. Las tres
  últimas están previstas para la Etapa 6, pero **§17.2 no está en ningún plan**: hay que
  escribirla o sacarla del índice.
- **Catorce números de tabla libres** en la numeración global (12–15, 18–19, 31–32, 36–38, 53–55).
  Se resuelve al integrar, con campos de Word.
- **Cuatro entradas viven sólo en el Anexo A y cuatro sólo en el Anexo B.** Si esos anexos no
  llegan a §19, esas ocho quedan huérfanas y además dejan dos remisiones colgadas en §15.2.3 y
  §15.3.3.
- **Una baja pendiente ya anotada**: «AAIP, s. f.-b», cuyo párrafo se borró.
- **El typo «puede puede»** de §15.2.4 sigue ahí; se corrige en Google Docs.

---

## Fuente: `docs/informe/entregable/90e-etapa1-anexo-a-y-referencias.md`

> SHA-256 del bloque: `e44e3a8b5e8872eb1b24786ca361532ce922e9dbdf85fcf2e7aee338568d7142`  
> Seleccion: ANEXO A corregido (matrices comparativas de modelos, Tablas A.1 y A.2) y el LISTADO DE REFERENCIAS de la Etapa 1, con 102 entradas. Es insumo de §19.1 —el cuerpo de §15 cita la Tabla A.1 y §15.3.3 la A.2, asi que si el Anexo A no llega a §19 quedan dos remisiones colgadas— y es la fuente de las doce entradas que le faltan al listado del maestro (ver la auditoria).

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

## Fuente: `docs/informe/ajustes/06-etapa-6-documentacion-y-cierre.md`

> SHA-256 del bloque: `b2149f9007798b4fa1beabf75fb08cbee49cc2641b3120f12ac817619cd5b9ae`  
> Seleccion: documento completo.

# Etapa 6 — §17.6, §18 Cierre y §19 Anexos

> *Gantt ID 5 — "Documentación y defensa", 17/07/26 – 21/08/26.*
>
> **Estado (2026-08-10):** es la etapa del cierre documental. En el informe está repartida
> en tres lugares, con estados distintos:
>
> | Sección | Qué es | Estado |
> |---|---|---|
> | **§17.6** Documentación técnica, repositorio y evidencias de cierre | los repos y dónde vive cada evidencia | `[Agregado futuro correspondiente a la Etapa 6]` — **vacía** |
> | **§18** Cierre del Proyecto | **las conclusiones propiamente** | existe, pero se escribió **antes** de tener resultados |
> | **§19** Anexos A–D | reproducibilidad, licencias, métricas, infraestructura | existen; se completan |
>
> **Se escribe después del §17.5 y con el mismo material.** La división es: el §17.5
> reporta *qué se midió y cuánto dio*; el §18 dice *qué significa*, con qué fuerza, y qué
> queda afuera. Los insumos ya están armados en `gobierno/99` y en
> `sintesis/resultados-y-conclusiones.md`.

| Dónde | Qué |
|---|---|
| Texto actual | `entregable/96e` — §17.6 vacía · §18 y §19 escritos pre-resultados |
| Materiales de cierre | `gobierno/99` §2 (reproducibilidad), §3 (licencias y citas), §4 (limitaciones y ADRs) |
| Las conclusiones y su fuerza | `sintesis/resultados-y-conclusiones.md` §1–§2, §8 (escala **AF-1…AF-11**), §11 |
| Alcance y exclusiones | `nucleo/10` + `decisiones/adr-015-cierre-de-alcance.md` |

---

## 1. Tablero de contenidos a escribir

| ID | Sección | Tipo | Pri | Qué tiene que decir |
|---|---|---|---|---|
| **AJ-6.01** | §18 | EVIDENCIA | 🟠 | **Las conclusiones propiamente**, cada una con su fuerza declarada. |
| **AJ-6.02** | §19 | CONCRETA | 🟠 | El **anexo de reproducibilidad** — lo que hace auditable todo el capítulo. |
| **AJ-6.03** | §19 | EVIDENCIA | 🟠 | **Licencias, consentimientos y citas obligatorias.** |
| **AJ-6.04** | §17.6 | CONCRETA | 🟡 | **Repositorio y evidencias de cierre.** |
| **AJ-6.05** | §18 | CONCRETA | 🟡 | El **trabajo futuro**, que sale de las exclusiones ejercidas. |

---

## 2. Los contenidos, desarrollados

### AJ-6.01 · §18 Cierre del Proyecto · EVIDENCIA · 🟠 — las conclusiones propiamente

**El §18 existe pero fue escrito antes de tener resultados.** Hay que reescribirlo contra
lo medido, y hay una forma correcta de hacerlo:

- **Cada conclusión con su fuerza declarada**, usando la escala `AF-1…AF-11`
  (`sintesis/resultados-y-conclusiones.md` §8). Aplanar todo a "se logró" es más débil, no
  más fuerte: la regla aplicada fue **degradar la afirmación cuando el intervalo de
  confianza no excluía el cero**, y eso se sostiene mejor ante un jurado que una lista de
  éxitos.
- **En tres tiempos** (`AJ-5.11`, y viene de `AJ-1.15`): *qué dice la literatura* → *qué
  medimos nosotros* → *qué tipo de aporte queda*. Nunca al revés.
- **Las refutaciones son conclusiones.** E-DIR vetada por precisión con criterio
  pre-registrado, y E-HYB-or ejecutada y refutada, no son fracasos: son resultados.
- **Sin capacidades nuevas** fuera de las dos comprometidas por ADR firmado (016:
  distribución; 017: jornada de fine-tuning): el §18 no puede prometer ni insinuar
  nada más que no esté medido.
- **La precisión sobre "adaptación"**: el núcleo medido **no adapta los pesos** — se
  adaptó **operativamente** (resolución 560, prompt sets congelados, las capas de
  plataforma). Medir cuánto rinde ese stack sin entrenar **es** la contribución. La
  rama de fine-tuning (E-04) es una **jornada comprometida aparte** (ADR-017): sus
  resultados, si existen a la entrega, se rotulan como rama comparativa — nunca se
  mezclan con el núcleo zero-shot.

La narrativa de la que sale este texto: `sintesis/resultados-y-conclusiones.md` §1 (la
pregunta y la respuesta en una línea), §2 (el recorrido del argumento) y §11 (qué queda, y
qué **no** cambia).

---

### AJ-6.02 · §19 · CONCRETA · 🟠 — el anexo de reproducibilidad

Está armado en `gobierno/99` §2, y es **lo que convierte el capítulo de resultados en algo
auditable por un tercero**:

- **Huellas sha256** de los artefactos congelados (banco de clips con su freeze, `bench_v3`
  con su manifiesto por fuente).
- **Cadena de comandos por material**: reconstruir el banco, evaluar una corrida contra el
  bench, disparar una corrida — con la advertencia del export de CVAT a nivel PROYECTO vs
  TASK, que decide el primer paso.
- **Trazabilidad corrida → resultado**, y **los dos verificadores mecánicos**.

El §17.5 tiene que citarlo (es `AJ-5.02`: toda tabla lleva su `campaign_id` o el sha256 del
banco al pie).

---

### AJ-6.03 · §19 · EVIDENCIA · 🟠 — licencias, consentimientos y citas

Armado en `gobierno/99` §3, con dos reglas **no negociables**:

- **El lote de internet es *Standard YouTube License*.** Se cita el canal público como
  fuente y **nunca** se presenta como CC. *(Único residuo abierto del cierre: anotar URL +
  fecha de acceso por video en los 18 `clip.yaml` — `operacion/113` §C1.)*
- **El consentimiento del rodaje**: en los 34 clips del Bloque A aparecen los propios
  integrantes del proyecto, actuando según guion y sin terceros en cuadro; sujetos y
  responsables son los mismos. **La identificación del responsable va en el informe.**

Además: licencia por dataset —con la **limitación L7**, licencia parcial de `chv`— y los
**pesos de modelo**: Grounding DINO Apache-2.0, YOLOE AGPL-3.0, registrados en
`license_registry.md` §PESOS DE MODELO.

---

### AJ-6.04 · §17.6 · CONCRETA · 🟡 — repositorio y evidencias de cierre

Sección vacía. Qué tiene que decir:

- **Los cuatro repos del proyecto** y qué contiene cada uno, con sus ramas de trabajo — más
  el quinto, `e-ovrt_alert-distribution`: hoy un esqueleto sin implementación, ✎ 2026-08-10
  con estatuto de **trabajo comprometido** (ADR-016). Se reporta **con su estado real al
  momento de la entrega**, sea el que sea.
  ✎ **2026-08-18: ese estado real ya se conoce** — el módulo está **implementado, medido y
  verificado**, y es un **servicio HTTP** más de la plataforma (`:8082`), igual que los
  otros dos (docs `operacion/114`/`118`/`124`/`125`). Se escribe en presente.
- ✎ **2026-08-18 — LA CONTAINERIZACIÓN SÍ VA EN ESTA SECCIÓN, y así se escribe.** Es
  **trabajo comprometido para después de la entrega del informe**, cuya razón de ser es la
  **reproducibilidad de la plataforma** (que un tercero pueda levantarla en otra máquina),
  no cerrar el capítulo. Qué decir: que los tres servicios son config-driven y aptos para
  empaquetarse; que el empaquetado está **planificado y pendiente**, con su causa
  —diferido a conciencia, no por falta de tiempo—; y que **su documentación operativa vive
  en los repositorios** (`infra/`, READMEs), no en el informe, porque la tesis no es un
  manual de despliegue. **Cómo NO escribirlo:** en presente, ni como capacidad existente,
  ni con instrucciones de despliegue. La frase que gobierna: *describir el compromiso y su
  fundamento es correcto; describir un despliegue que no corrió es falso.*
- **Que `docs/` es un repo git propio**, con remote desde el 2026-08-10 (`e-ovrt_docs`,
  rama `main`) para el acceso del equipo, y que además se respalda con copia a otro disco.
  *(✎ 2026-08-18: decía "local sin remote" — esa era la decisión inicial del 2026-07-09,
  superada al sumar redactores externos.)*
- **Dónde vive cada evidencia**: `results/` (los índices y sus artefactos),
  `datasets/processed/clip_bench/` (el banco, con su freeze y sha256),
  `docs/operacion/datos/` (la evidencia cruda por campaña).
- **Los dos verificadores mecánicos** y qué cubre cada uno
  (`96-verificar-indices.py` para las cifras de los índices,
  `109-verificar-organizacion.py` para la organización del material).

---

### AJ-6.05 · §18 · CONCRETA · 🟡 — el trabajo futuro sale de las exclusiones

No hay que inventarlo: **el trabajo futuro son las exclusiones ejercidas, con su costo ya
medido**, y eso es mucho más sólido que una lista de deseos.

- **El fine-tuning ya no es trabajo futuro NI estado a declarar: es un RESULTADO cerrado**
  ✎ 2026-08-22 (las notas 08-11→08-15 que vivían acá quedaron como historia en
  `estado-de-implementacion-adrs.md`, fila 017). **La jornada se ejecutó completa en sus
  tres tramos** — T1 NO-GO (`operacion/123`) · T2 NO-GO (`operacion/127`) · T3 cerrado con
  causa técnica (`operacion/117` §2) — con márgenes y expectativas pre-registrados, y
  ningún checkpoint adoptado. En el §18 se cita como **curva de capacidad de tres puntos**
  cuyo hallazgo es F-127.1: el límite es **estructural (datos: 2.946 imágenes vs 10,35M
  parámetros), no de capacidad**. **Lo que SÍ es trabajo futuro** (acta de cierre,
  `operacion/128` §2): métodos de adaptación eficiente en parámetros (PEFT) y un corpus
  de ajuste que no comparta fuentes con el banco — siempre bajo pre-registración nueva;
  nunca "más épocas" ni "más brazos" contra el banco congelado. Jamás "por tiempo".
- **La distribución de alertas dejó de ser trabajo futuro** ✎ 2026-08-10: ADR-016 la puso
  en alcance como **trabajo comprometido** antes de la defensa. Si a la entrega está
  implementada, se reporta en §17.4; si quedó incompleta, **lo pendiente se declara como
  estado, no como promesa** — y lo que sí sigue siendo trabajo futuro es **E-06** (el
  dashboard de consumo), que ADR-016 mantiene excluida.
- **FAR/hora**: requiere ~3 h de cumplimiento anotado (**limitación L1**). Es un requisito
  de dato, no de software.
- **Las celdas de la frontera de juzgabilidad** que quedaron sin cruzar, y la **validación
  sobre obra real** que la limitación L4 caracteriza pero explícitamente **no** cierra.
- **Métricas MOT** (E-10) — recordando el matiz de R-21: lo excluido son las métricas, no
  el tracker.

---

## 3. 🚫 Lo que no hay que escribir en esta etapa

| # | No escribir | Por qué |
|---|---|---|
| 1 | Conclusiones sin su nivel de fuerza | La escala `AF` existe justamente para eso; aplanarla debilita el capítulo. |
| 2 | Capacidades o promesas nuevas | ADR-015 cerró el alcance hasta la defensa. |
| 3 | "Adaptamos los modelos" a secas | La adaptación del núcleo es **operativa**, sin tocar pesos. La rama de fine-tuning es una jornada aparte (ADR-017): si tiene resultados se rotulan como rama comparativa, nunca se funden con el núcleo. |
| 4 | El lote de internet como material CC | Es *Standard YouTube License*. |
| 5 | ~~El módulo de distribución como funcionando~~ ⛔ **✎ 2026-08-18: esta prohibición quedó INVERTIDA** | Ya hay código verificado y medido: el módulo **funciona, está integrado y es un servicio HTTP** (`:8082`). **Se escribe en presente.** Lo que sí sigue prohibido: fundir sus cifras con las del núcleo, y presentar la **containerización** como hecha. |
| 7 | ✎ **La containerización en presente, o como instructivo** | Es trabajo comprometido **posterior** a la entrega del informe, para **reproducibilidad**. Se **puede y conviene** mencionarla como compromiso declarado con su causa (§17.6/§18/§19), pero su documentación operativa vive en los repositorios, no acá: el informe no es un manual de despliegue. |
| 6 | "L4 se levantó" | Se **precisó** (D-113.1). |

## 4. Fuentes

`gobierno/99` §2–§4 · `sintesis/resultados-y-conclusiones.md` §1, §2, §8, §9, §11 ·
`nucleo/10-registro-alcance-y-exclusiones.md` · `nucleo/19` (ciclo de vida de la alerta) ·
`decisiones/adr-005`, `adr-015`, `adr-016`, `adr-017` ·
`operacion/100` §6 (costo del fine-tuning), `operacion/113` §C1 (el residuo de licencias) ·
`e-ovrt_datasets/datasets/registry/license_registry.md`.

---

## Fuente: `docs/informe/ajustes/07-critica-extension-y-poda.md`

> SHA-256 del bloque: `44cc87962e89066323feb695800b7b2c3c61a1fa07ff69bb42b3e58abafc900a`  
> Seleccion: podas 17 y 18, tablero y guardrails aplicables al cierre.

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

## Fuente: `docs/informe/ajustes/gobierno/99-materiales-de-cierre.md`

> SHA-256 del bloque: `151b39954b1cbf8cb9c1e9618e7cda16ae233ad1bd44214397f89aa786558983`  
> Seleccion: reproducibilidad, licencias, limitaciones y mecanismos.

## 2. Anexo de reproducibilidad

### 2.1 Huellas de los artefactos congelados (verificadas el 2026-08-05; ✎ re-verificadas el 2026-08-10 — cambió solo el manifest del banco de clips)

| Artefacto | sha256 | Verificación |
|---|---|---|
| `bench_v3.json` (banco de imágenes) | `4557024ecc4ee497…a4462` | `sha256sum` **coincide** con `bench_v3_manifest.json → bench_v3_sha256` |
| estrato `bench_obra_test` | `e82eed03469665a3…af61a` | coincide con `source_sha256` |
| estrato `bench_obra_val` | `b2326724b71e7776…4c58c` | coincide con `source_sha256` |
| estrato `chv` | `6d15ff9b46407511…39a7` | coincide con `source_sha256` |
| estrato `shel5k` | `bf35f63bcf726c1c…d1e0f` | coincide con `source_sha256` |
| `manifest.yaml` (banco de clips, **47 — vigente desde 2026-08-09**) | `3f14f50a53c0d6c57b429378544dcfb6ed87fc942640db302c53ba1470001a75` | `sha256sum` directo == `clip_bench_manifest.json`; freeze `clip_bench.sha256` **189/189 OK** (verificador 109) |
| `manifest.yaml` (freeze histórico del sub-banco del rodaje, 34) | `cef5082e1eb1981c…260e8` | commit `f7a27fe6` — es el freeze que citan T1/T2/D1/H1/G1/B1/R1–R6 |
| prompt set `cr01_cr02_v2_short` | `df81fd48b6daf892…b309a` | `frozen_sha256` en el YAML, acta doc 76 |
| prompt set `eind_v1` | `7a0126f45eb1362a…ed770` | idem |
| prompt set `edir_v1` | `a1278d0c34cd13be…43703` | idem |

> **Queda saldado un riesgo de la auditoría del doc 75**: decía que el sha256 de
> `bench_v3` **no era verificable con `sha256sum`**. Sí lo es — se verificó hoy, y los
> cuatro sha256 por estrato también. El manifest guarda exactamente el digest del
> archivo, sin canonicalización de por medio.

### 2.2 El verificador mecánico de cifras

```bash
cd docs && python3 operacion/datos/96-verificar-indices.py
```

✎ 2026-08-14 — **el alcance volvió a crecer** (docs 113 y 118). Corrido hoy:
**`✅ Todo verificado`** — **25 cifras** contra `metrics.json` (14 F1 de `clip_bench`,
5 de `bench_nivel_a` y 6 valores de `realtime/t_alert_notification`), **guard de
cobertura 17/17 campañas** (falla si aparece una campaña sin fila de verificación),
3 deltas de bootstrap con su IC, 1.447 enlaces y **35 docs de procedencia** (ninguno
faltante). *(Decía: 8 F1, 31 docs, "solo cubre T1, G1 y R1–R6" — ese hueco quedó
cerrado por el guard.)*

**Lo que sigue sin cubrir, y se chequea a mano:** `bench_imagenes/`; el descarte se
contrasta contra el doc 64. `realtime/t_alert_notification` ya tiene `metrics.json`,
prueba negativa obligatoria y cobertura mecánica.

**Segundo verificador** (✎ 08-10):
`python3 docs/operacion/datos/109-verificar-organizacion.py` — las 6 reglas de
organización del material de video: estratos en su lugar (34+13+4 retirados), campaña
citable vs evidencia exploratoria, anotaciones del repo como fuente de verdad
(correcciones firmadas con guard `--check`), integridad lab↔banco por sha256,
exclusiones firmadas (`v08_c01`), banco reportable con freeze 189/189.

### 2.3 Cadena de comandos por material

Los cuatro repos son hermanos en disco y las rutas relativas lo asumen.

**Banco de imágenes (`bench_v3`) y percepción**
```bash
# reconstruir el banco (idempotente, lee las 4 fuentes curadas)
python3 datasets/scripts/curate/build_bench_v3.py
# evaluar una corrida del media-plane contra el banco
cd e-ovrt_media-plane && .venv/bin/python -m eovrt_media.tools.evaluate \
    --run runs/<run_id> \
    --bench-coco ../e-ovrt_datasets/datasets/processed/coco/bench/curated/bench_v3.json
```

**Servicio del media-plane y disparo de una corrida**
```bash
cd e-ovrt_media-plane && EOVRT_MODEL_REF=grounding-dino/gdino-tiny-560 make serve  # :8080
curl -s localhost:8080/healthz localhost:8080/readyz          # = make smoke
# POST /api/runs con el run config (una corrida activa a la vez)
```

**Camino offline (DBE) y camino en vivo (EBE)**
```bash
cd e-ovrt_control-plane
.venv/bin/eovrt-control serve --port 8081                       # servicio
.venv/bin/eovrt-control replay   --config <cfg>                 # DBE: relee detections.jsonl
.venv/bin/eovrt-control live     --config <cfg>                 # EBE: consume el bus
.venv/bin/eovrt-control evaluate-alerts ...                     # 5 métricas contra GT temporal
```
> **EBE, orden no negociable:** primero `POST :8081/api/runs` con `mode: live` (su 201
> implica suscripción hecha), después `POST :8080/api/runs` con `bus.enabled: true`.
> PUB/SUB pierde todo lo publicado antes de la suscripción.

**Cadena de GT de video** (✎ 08-10: las anotaciones llegaron — docs 102–111 — y la
cadena quedó ejercitada de punta a punta sobre 13 clips)
```bash
# ¡verificar meta/task vs meta/project ANTES de decidir el primer paso! Un export a
# nivel PROYECTO exige el split (sin él el GT sale negativo EN SILENCIO); el lote llegó
# a nivel TASK y aplicárselo habría sido el error simétrico (doc 102).
python3 <video-gt-lab>/split_cvat_project.py ...
python3 <video-gt-lab>/derive_clip_gt.py ...
python3 <video-gt-lab>/validate_clip_gt.py ...
python3 <video-gt-lab>/promote_clip.py ...        # suma el clip al banco
python3 <video-gt-lab>/aggregate_clip_campaign.py ...   # métricas de campaña
# guard de correcciones firmadas (✎ 08-10): apply_attribute_corrections.py --check
# sale 1 si una corrección firmada del repo falta en el GT (doc 111)
```

**Piloto de clase nueva (A1)** — un solo archivo de config de 48 líneas, 0 entrenamientos;
procedencia de las 5 corridas en `operacion/datos/94-piloto-clase-nueva/resultados.json`.

### 2.4 Trazabilidad corrida→resultado

Cada campaña de `results/` trae su procedencia en disco, y es lo que hay que citar:

| Archivo | Qué garantiza |
|---|---|
| `campaign.yaml` | la definición de la campaña (modelo, prompt set, granularidad, pattern set) |
| `provenance.json` / `provenance_runs.json` | los `run_id` exactos del media-plane y del control-plane |
| `evals/eval_<clip>.json` | la evaluación por clip, uno por clip del banco |
| `metrics.json` | el agregado (`positives`, `negatives`, `by_condition`, `by_scenario`, `by_clip`) |

**Entorno:** media-plane Python 3.12 (`pip install -e ".[gpu,dev]"`), control-plane y BFF
Python 3.11, `datasets` sin paquete (scripts sueltos, requiere `Pillow`). Puertos 8080
(media) y 8081 (control). El JSONL es la verdad en los dos caminos: **toda corrida live
es re-evaluable offline y produce artefactos idénticos** (paridad verificada por mutación).

---

## 3. Licencias, consentimientos y citas obligatorias

### 3.1 Lo que efectivamente sostiene un resultado reportado

Solo estas fuentes aparecen en los números del capítulo. El resto del
`license_registry.md` (SH17, GDUT-HWD, SHWD, SODA, Pictor-PPE, Construction-PPE,
`construction_safety_hardhat`) **no se cita**: o quedó descartado o nunca entró.

| Fuente | Dónde entra | Licencia | Obligación en el informe |
|---|---|---|---|
| `construction_site_safety` (Roboflow) | estratos `bench_obra` (147 imgs) + split TRAIN | **CC BY 4.0** | atribución |
| `chv` (GitHub `ZijianWang-ZW/PPE_detection`) | estrato `chv`, **1.330 imgs = 20,5% de `bench_v3`** | **sin licencia formal** (SPDX: none); grant informal de los autores: *"open for free use"* | **cita obligatoria `wang2021ppe`** + declarar *"dataset académico de terceros usado para evaluación bajo el grant de uso libre de sus autores, con cita; imágenes no redistribuidas"*. Se cumple por construcción: raw gitignorado, solo se versionan anotaciones derivadas |
| **SHEL5K** (Mendeley) | estrato `shel5k`, **5.000 imgs (77% del agregado)** | **CC BY 4.0**, DOI `10.17632/9rcv8mm682.4` | atribución + DOI |
| `ppe_siabar` (Roboflow) | split TRAIN | CC BY 4.0 | atribución (✎ 2026-08-22: la jornada de fine-tuning **ya se ejecutó completa** — T1/T2 NO-GO, T3 causa técnica — así que no hay "estado a declarar a la entrega": se declara el cierre, con la curva de tres puntos, nunca "quedó fuera") |
| **MOCS** (copia Roboflow `mocs-bowib`) | piloto A1 (evidencia cualitativa + ancla `person`↔`Worker`) | CC BY 4.0 **declarada por el uploader de la copia**; el original de `anlab340` nunca se descargó ni se verificó | **citar el paper original de MOCS** + declarar que se usó una copia de terceros, sin redistribución |
| **Rodaje propio 2026-07-25** | **el banco de 34 clips = el resultado principal** (✎ 2026-08-28: regla del set — el banco es **47 = 32 positivos + 15 negativos, 37 episodios**; los **34 clips del rodaje son el Bloque A** (35 episodios, 34 evaluables), sobre el que se reporta el resultado principal. GUIA §4 trampa 1) | material propio | consentimientos de los participantes (ver §3.3) |
| **Lote de internet (14 clips — ✎ 08-10: 13 con GT humano, `v08_c01` excluido con causa firmada)** | estrato B del banco de clips (Bloque B); **precisa L4, no la levanta** (D-113.1) | ✎ **2026-08-05: origen registrado** — canal de YouTube **`@HospitalConstruction`** (https://www.youtube.com/@HospitalConstruction). **Es *Standard YouTube License*, no Creative Commons** ⇒ base de uso: **académico/evaluativo con cita y sin redistribución** (postura `chv`), **nunca presentado como licencia de libre uso** | **citar el canal como fuente de las escenas** + los caveats de §3.3 (no es cámara-nativo · caras difuminadas en figuras · velocidad real verificada) |

### 3.2 Licencias de los modelos: hueco abierto

Los catálogos de `e-ovrt_media-plane/configs/models/` (`grounding-dino/`,
`mm-grounding-dino/`, `yoloe/`) **no traen campo de licencia**. El informe cita tres
familias de pesos y hoy no hay registro de bajo qué términos se usan. **Hay que
verificarlo y registrarlo antes de citarlas** — mirar el `LICENSE` del repo de origen de
cada familia de pesos y anotarlo junto al catálogo. No lo doy por sabido acá: es
exactamente el tipo de dato que no se declara de memoria.

### 3.3 El lote de internet: origen registrado el 2026-08-05, con dos salvedades

> ✅ **RESUELTO en lo esencial el mismo día.** El usuario aportó la procedencia: las 14
> escenas salen del **canal público de YouTube `@HospitalConstruction`**
> (https://www.youtube.com/@HospitalConstruction), cuyas descripciones declaran que los
> videos son públicos. **Decisión: se cita el canal como fuente de las escenas.** Quedó
> registrado en `e-ovrt_datasets/datasets/registry/license_registry.md`, sección
> **"Material de VIDEO"** — que hasta hoy no existía —, junto con la entrada del rodaje
> propio. La base de uso declarada es la misma que ya se usa para `chv`: **uso
> académico/evaluativo con cita, sin redistribución** (los `.mp4` están gitignorados; solo
> se versionan anotaciones derivadas, previews y nombres de archivo).
>
> **Salvedad 1 — RESUELTA, y define cómo se redacta: es *Standard YouTube License*.** Se
> revisó la descripción: **no hay marcador de Creative Commons**, así que rige la licencia
> por defecto, que no concede reproducción ni obra derivada. La descripción sí declara que
> lo grabado son vistas y escenas visibles al público — pero eso dice **qué se filmó**, no
> otorga reuso. ⇒ El informe declara **uso académico/evaluativo con cita y sin
> redistribución** (postura `chv`), y **nunca** "licencia CC" ni "material de libre uso".
>
> **Salvedad 2 — personas identificables de terceros**, consentimiento no obtenible. La
> declaración del autor ayuda **acá**: respalda que no hay expectativa razonable de
> privacidad sobre lo filmado. Mitigaciones igual: no se redistribuye, sin datos personales
> en el repo (DA-08/09), E-11 intacta. **Regla: si un frame del lote se publica como
> figura, se difuminan las caras.**
>
> **Dos caveats metodológicos del estrato, que van declarados con él:**
> **(1) velocidad real verificada por dos vías ⇒ las métricas temporales aplican** — el
> canal publica sobre todo time-lapse, y un clip time-lapse volvería inservibles TTFD /
> `confirm_after_ms` / SDR; el autor declara velocidad original y además se **midió** sobre
> las pre-anotaciones de los 14 clips: **0,4–2,8 px/frame de mediana** (máx ~23), propio de
> 30 fps continuos. Los 14 masters son 1920×1080 @ 30 fps.
> **(2) el material no es cámara-nativo** — el autor declara corrección de color,
> estabilización y recortes. Preproceso ajeno que no controlamos: se declara. El rodaje sí
> es cámara-nativo, así que los dos estratos se leen por separado (L5).
>
> **Falta**: URL y fecha de acceso por video (hoy: el canal + un video de referencia,
> subido 2015-04-05, grabado 2015-03-28).
>
> Lo que sigue abajo es el diagnóstico original. **Se conserva solo como rastro**: explica
> por qué registrar la procedencia no era opcional y qué se verificó antes de tenerla. Los
> dos puntos que abría —licencia del lote y consentimiento del rodaje— están cerrados
> (este banner y §3.3 arriba, más el registry).

Verificado el 2026-08-05 (antes de que se aportara el origen), tres cosas independientes:

1. Los **14 `clip.yaml` del lote de internet no tienen cláusula de licencia** (a
   diferencia de `cb_b01_p7`, que sí llevaba la condición escrita). ✎ 08-06: los 3
   promovidos (`v04_c01`/`v06_c01`/`v10_c01`) **ya la llevan** (bloque `license:` con
   `video_url: TODO` — la URL por video sigue pendiente, hallazgo 2 de §6).
2. El `license_registry.md` **no tiene ninguna entrada de video** — ni rodaje, ni banco
   de clips, ni lote de internet.
3. **No hay URL de origen registrada** para los 14 masters (`raw/1.1.mp4` … `10.1.mp4`).

Y la regla que lo vuelve vinculante ya estaba escrita: **spec 43 §7, "Marco legal
(bloqueante de la grabación, no del diseño)"**, que exige dos cosas distintas:

- *"**Consentimiento libre, expreso e informado por escrito** de cada persona grabada
  (**Ley 25.326, Disposición 10/2015** — doc 08 §1.3), archivado y **referenciado en
  `license_registry.md`** (sin datos personales en el repo)"*.
- *"**Bloque B: registrar la licencia** del dataset antes de usar los videos **en
  resultados reportables**"*.

Su ítem de checklist **`[ ] Consentimientos y licencias en license_registry.md; sha256 en
manifest` sigue sin marcar** (spec 43 §9). Y es el motivo #1 por el que `cb_b01_p7` se
retiró, que cita esa misma sección: *"licencia/consentimiento sin registrar — motivo
vinculante… no se resuelve con una pasada de CVAT"*.

**La consecuencia práctica:** cuando lleguen las anotaciones, el lote **queda
igualmente inelegible para resultados reportables** hasta que su procedencia esté
registrada. Anotarlo no lo desbloquea. Es decidible **hoy**, en paralelo al CVAT, y solo
lo puede hacer quien sepa de dónde salieron los videos.

**Dos casos, severidades distintas — no confundirlos:**

- **Rodaje (34 clips, el resultado principal) (✎ 2026-08-28: = **Bloque A** del banco de **47** clips; ver §1): ✅ resuelto por declaración (2026-08-05).**
  Las personas que aparecen son **los propios integrantes del proyecto**, actuando según el
  guion del doc 69, **sin terceros en cuadro**: son a la vez los sujetos y los responsables
  del material, y las situaciones son actuadas — no documentan conducta laboral real de
  nadie. Eso es lo que se declara en el informe, y es una posición más fuerte que un
  formulario. Lo administrativo lo maneja el equipo por su cuenta; la identificación del
  responsable va en el informe, no en el registry. Queda disponible
  `registry/plantilla-consentimiento-audiovisual.md` por si la facultad pide el formulario.
- **Lote de internet (14 clips):** obra real de terceros, con personas identificables y
  **procedencia desconocida en el repo**. Riesgo alto: si no se puede acreditar el origen
  y sus términos, el material no entra al capítulo — exactamente como `cb_b01_p7`.

**Lo que se puede hacer sin esperar a nadie** (✎ 2026-08-06: la entrada de video **ya
se creó** ese mismo día — §3.3; lo que sigue faltando del bloque es solo **URL + fecha
de acceso por master**): completar en `license_registry.md` §Material de VIDEO la URL
de origen y términos por master, y el sha256 en el manifest. Si el lote no acredita, el capítulo **se sostiene
igual** con L4 declarada — es la regla del doc 57 §7.6: *el cierre lo decide la cobertura
del material; lo no cubierto se declara con causa, nunca se fabrica*.

---

## 4. Limitaciones y ADRs

### 4.1 Lista canónica de limitaciones: L1–L8 (cerrada 2026-08-05)

**Resuelto.** `results/index.md` definía **L1–L5** y `operacion/98` §6 listaba **7**
limitaciones con solo **4 etiquetadas** (L4, L1, L5, L2) — L3 no aparecía y tres iban
sueltas. Ahora las ocho tienen código en los dos lugares, con `results/index.md`
§Limitaciones declaradas como versión de referencia.

> **Colisión de etiquetas que hay que respetar al redactar:** la **Fase L** del doc 62 usa
> `L0`/`L1` para sus hitos (`L0` = ensayo pre-rodaje, `L1` = el rodaje). Se decidió
> **mantener el prefijo `L` para las limitaciones** (ya estaban citadas en varios docs) y
> desambiguar en prosa: escribir **"limitación L1"**, nunca `L1` a secas.

| ID | Limitación | Estado | Fuente |
|---|---|---|---|
| **L4** | **Un solo bloque guionado, sin obra real en video.** La más citable: mismos actores, misma locación, escenarios guionados | declarada; ✎ 08-06: licencia registrada y GT humano en marcha; **✎ 08-10 — formulación VIGENTE (D-113.1, firmada): "L4 se precisó, no se levantó** — existe medición en obra real no guionada (I1/I2, 13 clips, revisión ciega incluida) y esa medición **caracteriza por mecanismo dónde el sistema deja de ser evaluable; no lo valida sobre obra real**". No se crea L9: la frontera de juzgabilidad es el contenido nuevo de L4. Versión de referencia: `results/index.md` | `operacion/98` §6 + D-113.1 |
| **L1** | **FAR/hora no sostiene una cota.** Harían falta ~3 h de cumplimiento anotado; el control de negativos discrimina (T1/T2/G1: 0 FP de 4; D1/H1/B1: 2–3) | declarada con causa cuantificada (D-90.1) — **✎ 08-10: precisada**: desde el 08-07 hay un clip soak (`v06_c01`, 0,1027 h) y la tasa **es computable**; se cita como **"3 y 190 FP en 6:09,6 del único soak"** con la tasa horaria como derivada (29,2 / 1.850,8 FA/h). Sigue sin sostener una cota. Versión de referencia: `results/index.md` | `operacion/98` §6 |
| **L5** | **Escenarios desbalanceados** ⇒ obliga a reportar siempre por escenario y por estrato | declarada; es regla de lectura, no solo limitación | `results/index.md` |
| **L2** | **Sin doble anotación ni kappa** — decisión declarada, no omisión | declarada | `results/index.md` |
| **L3** | **Seis bordes adjudicados** en el GT del rodaje (oclusión, no cambio de estado), con firma en `clip.yaml` | declarada; trazable en `apply_adjudications.py` | `results/index.md` |
| **L6** | **El tracker no está medido en obra real con multitud** — G1 se verificó en vivo con pocos sujetos; el `track_id` es post-hoc/decorador | declarada y **etiquetada 2026-08-05** — **✎ 08-10: parcialmente levantada**: en `v06_c01` (127 personas reales) el tracker produjo **182 identidades con FP** — fragmenta en denso y el costo de G1 escala con la escena (F-103.2). Versión de referencia: `results/index.md` | `operacion/98` §6 |
| **L7** | **Licencia de `chv` parcial** (20,5% del bench de imágenes): uso permitido con cita, sin redistribución | declarada y **etiquetada 2026-08-05** | `operacion/98` §6 + §3.1 |
| **L8** | **CR-02 a Nivel A no cerrada** — un solo estrato, IC solapados | declarada y **etiquetada 2026-08-05** | `operacion/98` §6 |

**Y una que este armado agrega:** la latencia G2A **no es** vidrio→alerta (F-101.8). No
es una limitación del sistema sino del **instrumento**, y ya tiene su advertencia
obligatoria en el doc 97 §5.4. Decidir si entra a la lista con etiqueta propia o queda
solo como caveat de la tabla de latencia.

### 4.2 ADRs: dos series que se confunden

**Trampa de numeración, va al informe:** hay **dos** series de ADR y se confunden a
simple vista.

- `docs/decisiones/` → **ADR-001…ADR-019** (3 dígitos): las decisiones **del proyecto**
  (✎ 2026-08-06: *decía "…014"*; el 015 es el cierre de alcance. ✎ 2026-08-10: el 016 es
  la reapertura acotada de la distribución. ✎ 2026-08-18: *decía "…016"* — el 017 es la
  jornada de fine-tuning, el 018 el acople BFF-subproceso —**derogado el mismo 08-18 por
  el 020**—, el 019 el servicio HTTP del distribuidor y el **020** el cierre: HTTP es el
  acople, el subproceso baja a fallback ⇒ **dos** patrones de acople, no tres).
- `e-ovrt_control-plane/docs/decisions/` → **ADR-0001…ADR-0013** (4 dígitos, falta 0005):
  las decisiones **internas del control-plane**.

Se solapan en tema y difieren en número (p. ej. aplicabilidad de métricas es ADR-006 del
proyecto y ADR-0006 del control-plane). **Al citar, decir siempre la serie.**
✎ 2026-08-06: **la convención quedó fijada en el glosario (doc 13 §3, entrada
"ADR-NNN (dos series)")** y las citas sin serie de `nucleo/01` y `nucleo/10` fueron
aclaradas en el lugar.

> Queda saldado otro ítem del doc 75: reclamaba **8 ADRs inexistentes**
> (`ADR-0006..0013` del control-plane). **Existen los 8**, verificado hoy.

**Los del proyecto** (ADR-015 va en prosa aparte, §5/§6), con dónde aterrizan:

| ADR | Decisión | Dónde se declara |
|---|---|---|
| 001 | Estrategia del núcleo: **E-IND** (encuadre) | §17.3 estrategia + veredicto del eje (T-68) |
| 002 | Granularidad: G0 núcleo + G1 demostrativa | **Revisar el texto**: G1 dejó de ser demostrativa — es el mejor resultado del banco (F1 0,930) |
| 003 | Bus media→control: **ZeroMQ PUB/SUB**, broker diferido | arquitectura EBE (FIG-A, T-76) |
| 004 | Corrida paraguas y `experiment_id` | reproducibilidad (§2.4) |
| 005 | Distribución de alertas: recorte, canal MQTT, repo propio | ✎ **2026-08-12: funcionalmente implementada y verificada** — seis criterios de spec 45 cerrados, incluidos DBE/EBE, reporte y MQTT real. Quedan la vista de webconsole, la orquestación integral y el primer commit; E-06 sigue excluida. **✎ 2026-08-14: los tres pendientes del 08-12 quedaron cerrados el 2026-08-13** — vista de webconsole (`13c801e`, "feat(webconsole): mostrar outcomes de distribución") y orquestación integral (`42529e2`, "feat(experiments): orquestar distribución de alertas") en `e-ovrt_experimental-setup`; el repo `e-ovrt_alert-distribution` ya tiene historia propia (`c9903cc`, `1e6d8fa`). E-06 sigue excluida |
| **016** | **Reapertura acotada de la distribución** para cerrar la arquitectura | deroga ADR-015 §2b/§2c/§6; ratifica §2a/§3/§4/§5. E-06 sigue excluida |
| 006 | Reporte consolidado y **aplicabilidad de métricas** | lenguaje de estados: `not_applicable` / `non_temporal_source` |
| 007 | Semántica de corrida en EBE: **1:1** | T-76 |
| 008 | Control-plane como servicio mínimo | arquitectura |
| 009 | Config centralizada + webconsole como superficie de gestión | arquitectura + método |
| 010 | Secuenciación: plataforma primero, GT al final | método y cronología |
| 011 | Frontera de la política: el motor emite siempre; la supresión es de distribución | **`re_alerts` no son FP** |
| 012 | Sin memoria de cobertura bajo G0; la histéresis la subsume | mecanismo (F-81.1 / F-85.3) |
| 013 | Aplicabilidad por temporalidad de la fuente | estados de aplicabilidad |
| 014 | Layout y consolidación de artefactos por experimento | §2.4 |
| **017** *(✎ fila agregada 2026-08-18; actualizada 2026-08-22)* | El fine-tuning (E-04) se ejerce como jornada, nunca "falta de tiempo" | rama comparativa del §17.5 — **jornada COMPLETA en sus tres tramos, con veredictos pre-registrados**: T1 NO-GO (doc 123) · T2 NO-GO (doc 127) · T3 causa técnica (doc 117 §2); curva de capacidad de tres puntos, F-127.1 fallo estructural |
| ~~**018**~~ | ~~Tercer patrón de acople: BFF-subproceso~~ ⛔ **DEROGADA por 020** | **no va al informe** — registro histórico |
| **019** *(✎ fila agregada 2026-08-18)* | El distribuidor también como **servicio HTTP** (`:8082`) | §17.4 despliegue: los tres módulos son servicios HTTP config-driven; containerización diferida con causa (doc 124) |
| **020** *(✎ fila agregada 2026-08-18)* | **HTTP es el acople de la distribución**; el subproceso baja a fallback operativo y deja de ser patrón | §17.4/§17.3: **DOS patrones de acople** — (a) HTTP config-driven en los tres módulos, (b) bus ZeroMQ. El fallback **no se describe**: es operación, no arquitectura |

**ADR-015 — ✅ escrito y ACEPTADO el 2026-08-05.**
`decisiones/adr-015-cierre-de-alcance.md` (fuente: `docs/decisiones/adr-015-cierre-de-alcance.md`).
El doc 95 §5.1 lo pedía como *"recorte final de alcance"* porque los docs 91/94 declaraban
tracker/G1 como no implementado; **su premisa se invirtió** (G1 es el mejor resultado del
banco), así que no es un recorte: es el **registro de que el alcance creció, con
evidencia, y de qué sigue excluido**. Qué hace:

- **Registra los cuatro movimientos**: E-03 (G1 de demostrativa a capacidad operativa
  medida en 34/34), E-07 (parcial: OAK-D + EN-2 con 87% de descarte), E-13 (E-HYB-or
  ejecutada y refutada; `hyb_and` no ejecutada con causa), E-04 (no ejercida, pero por
  secuenciación — ✎ 2026-08-11: fila **superada por ADR-017**, E-04 es jornada
  experimental comprometida y la causa temporal está derogada). **E-10 y las otras
  ocho exclusiones no cambian.**
- **Cierra la puerta** (§2b): ninguna capacidad nueva de acá a la defensa — es la parte
  que *restringe*, y es el riesgo que el doc 95 realmente quería cubrir.
- **Registró un estado transitorio del condicional de ADR-005.** ADR-016 lo sustituyó:
  el condicional quedó resuelto en **sí** y el recorte mínimo fue implementado y
  verificado. §2b/§2c/§6 de ADR-015 quedaron derogados; §2a, §3, §4 y §5 —incluida
  **la lista de límites L1–L8**— siguen vigentes.
- **Desbloquea R-13** con una lista auditada ítem por ítem: **de los 8 límites de julio,
  5 estaban resueltos** (`track_id`, evaluadores de D1, GT preliminar, matching greedy,
  inventario de datasets) y sobreviven 3, uno de ellos agravado por F-101.8.
- **Desbloquea R-21 corrigiendo un punto falso**: su tabla dice *"MOT ✗ tracker no
  implementado"*; lo excluido son las **métricas** MOT (E-10), no la capacidad.

Integrado en `decisiones/README.md`, `estado-de-implementacion-adrs.md` (§0 y §1) y
anotaciones en R-13 y R-21 del doc 93. **Y aplicado al doc 10 el mismo día**: el ítem 10 de
la lista de alcance quedó reescrito (G1 = capacidad operativa medida en 34 clips, ya no
"demostrativa en 2–3") y las filas **E-03/E-04/E-07/E-13** de la tabla de exclusiones
llevan su estado real con evidencia. **Registro de alcance y resultados ya dicen lo mismo.**

*De yapa, en la misma pasada:* la fila del ADR-001 en `estado-de-implementacion-adrs.md`
§3 decía *"sigue abierto (acta `edir_v1` pendiente)"* — **el acta se firmó el 2026-07-29
(doc 76) y D1 corrió en los dos niveles**. Corregida.

---

## 5. Catálogo de mecanismos: lo que el CVAT no movió — y lo que agregó

Esta es la parte del capítulo que da credibilidad. La premisa original ("es inmune al
lote de internet: el GT nuevo puede mover un agregado, no un mecanismo medido") **quedó
verificada por los hechos** (✎ 2026-08-10): el CVAT llegó (docs 102–113), hubo
re-derivaciones y hasta una revisión ciega del GT, y el catálogo del Bloque A de abajo
sobrevivió intacto. El tramo de video **agregó mecanismos propios** — bloque nuevo al
final de esta sección. Texto fuente: los índices de `results/` (verificados
mecánicamente) — de ahí se transcribe, no de acá.

**Cómo la plataforma agrega sobre la detección cruda**
- **F-81.1** — la **histéresis rescata percepción intermitente**: CR-02 se detecta en ~1
  de cada 6 frames del episodio (F-G2.1) y el motor igual confirma.
- **F-85.3** — y es **palanca de doble filo, medida en los dos sentidos**: rescata lo
  intermitente-correcto y también sostiene lo intermitente-equivocado.
- **F-87.2** — **la unión de evidencia NO es monótona en un motor temporal**: sumar un
  brazo (`hyb_or`) no sube el recall, lo derrumba (0,824 → 0,353). Predicción
  pre-registrada **refutada**.
- **F-89.1 / F-89.2** — **el margen no estaba en el modelo ni en los prompts, sino en la
  identidad**: F1 0,789 → 0,930 con las detecciones **bit a bit las mismas** (SDR y TTFD
  idénticos). Es el hallazgo central del capítulo.
- **F-81.3** — TTFD ~5 frames: la latencia de la plataforma **es la política**, no el modelo.

**Cómo se expresa la condición en lenguaje (y su modo de falla propio)**
- **F-88.3** — **la etiqueta corta gana a la frase negada**, y eso ordena el eje.
- **F-88.1** — **el caption tiene costo medido**: 0,082 de F1 por una palabra.
- **F-88.2** — `bare_head` como evidencia directa **tampoco alcanza** (0,480 vs 0,582 de
  la ausencia espacial, **sobre las mismas detecciones**).
- **F-83.6** — **E-DIR no es un detector, es un recuperador**: recupera 18,5% de lo que
  E-IND no ve.
- **F-85.4** — **el ranking de Nivel A no transfiere a Nivel B**: la brecha se agranda
  con la plataforma.
- **F-85.5** — P9 es la única victoria de E-DIR, y está donde E-IND es más débil.
- **F-94.1** — **la palabra tiene que alinear con la taxonomía del despliegue**:
  `vehicle` junto a `machinery` da **0 detecciones**; aislada, AP 0,026 porque el 67% cae
  sobre lo que ese GT llama `machinery`. Segundo caso independiente el 2026-08-05
  (`gloves`: 252 detecciones, ninguna sobre un guante). **Va junto al número de A1, no
  después.**

**Qué sobrevive al tiempo real**
- **F-RT3** — el techo de fps es **contención de GIL**, no térmico ni la rama de texto.
- **F-RT5** — palanca aplicada y significativa: 3,75 → 4,42 fps, −14,4% latencia, p = 0,0195.
- **F-RT2** — la ventana temporal **exige estabilidad perceptual**: YOLOE entra en
  presupuesto y es inservible para la condición.
- **F-96.1** — a ~4 fps el agregado **no se degrada de forma detectable**, pero un
  agregado plano **escondía una redistribución completa**.
- **F-96.2** — **lo primero que se rompe bajo tiempo real es el rescate de F-81.1**:
  CR-02/P2 cae 1,00 → 0,60 → 0,20. Límite de cadencia declarado.
- **F-96.4** — **la ganancia de la identidad excluye el cero en las 4 densidades**
  (bootstrap pareado por clip). Formulación segura: doc 101 §3.
- **F-101.8** — **el G2A se mide desde el dequeue, no desde el fotón**: vidrio→alerta =
  `capture_to_host` (202–217 ms en el rodaje, 1.600 ms en tomas degradadas) **+ G2A**.

**Trampas de instrumento — se declaran o el número engaña**
- **F-EV1** — los clips negativos **no entran** a P/R/F1; su métrica son los FP.
- **F-96.6** — el **SDR no se compara entre cadencias**: sube al bajar la densidad, ~100%
  artefacto, verificado por decimación de las mismas detecciones.
- **F-96.5** — el **`t_alert` agregado no se compara entre densidades** sin control de
  supervivencia (corregido en revisión adversarial).
- **F-96.7** — 0 FP en negativos (✎ 08-10: acotado a las campañas del **Bloque A**): con
  4 clips es **control, no tasa**. El estrato B sí produce FP sobre sus 11 negativos —
  y ahí el conteo ES la métrica (ver el bloque del tramo de video).
- **F-RT1** — la sobre-marca de `vest` suprime CR-02 (dependiente de la vestimenta).
- **F-RT4** — deriva del host ±150 ms ⇒ las palancas <20% exigen ~10 pares **pareados
  intra-campaña** (protocolo doc 74).

**Qué agregó el tramo de video (estrato B) — ✎ 2026-08-10**
- **F-103.2** — bajo `subject` la identidad recupera el recall también en denso, **pero
  el tracker multiplica el ruido por la multitud**: en `v06_c01`, 182 identidades con FP
  contra 127 personas reales — el precio escala con la escena, no con el modelo.
- **F-105.2** — **la caída del estrato B queda confirmada a nivel PERSONA con el scorer
  oficial**: el mismo E-IND pasa de F1 0,41–0,55 en imágenes a ~0,15/0,01 sobre video
  real; **el recall se sostiene (~0,33), lo que se derrumba es la precision**.
- **F-105.3** — **la juzgabilidad NO se reduce a la escala**: `video02_clip07` tiene los
  sujetos más grandes del conjunto (370 px) y rinde F1 0,084 por oclusión mutua (58,5%
  de personas solapadas) — los ejes son **escala × iluminación × oclusión**.
- **F-105.4** — **el `unknown` del anotador mide la juzgabilidad HUMANA, no la del
  modelo**: el humano usa continuidad temporal (siguió a cada persona 6 minutos y
  determinó el 94%), el modelo decide frame a frame sin memoria — la vía de mejora
  señalada es **agregación temporal de evidencia para DETERMINAR estado**, no solo para
  confirmar.
- **F-108.1** — **la variable no era la granularidad: era la densidad** — `subject` solo
  hace falta cuando los sujetos se relevan; no existe "la mejor granularidad" del banco,
  existe la correcta para un régimen de densidad.
- **F-111.1 (enmendado — citar la versión enmendada)** — en obra real densa **la ventaja
  de la identidad que G1 mostró en el rodaje no se reproduce, y `subject` paga un orden
  de magnitud más FP** (asimetría 12× en negativos); el ranking por F1 **no se afirma**
  (n = 2 evaluables). La enmienda misma es citable como método.
- **F-113.1** — hallazgo de REPRODUCIBILIDAD: **re-evaluar sin re-agregar congela la
  procedencia** (el agregador copia `campaign.yaml` dentro de `metrics.json` — los
  `metrics.json` de I1/I2 declaraban el freeze pre-corrección); detectado y corregido
  **sin mover ninguna cifra**.
- **D-113.1** — decisión firmada: **se precisa L4, no se crea L9** — la frontera de
  juzgabilidad es el contenido nuevo de L4 (formulación de cita en §4.1).
- **D-113.2** — decisión firmada: la persona `unknown` **sale del denominador** del
  scorer de Nivel A, **pero una violación predicha sobre ella cuenta como FP** — "la
  alerta sobre una persona no juzgable suena igual"; la regla simétrica se evaluó y se
  descartó (medido: 48% de los FP de CR-01 en los pilotos caen sobre `unknown`).

**Resto del catálogo** (F-83.3/4/5/7, F-84.1/5/6, F-81.2, F-96.x restantes,
F-101.1/3/5/6/7/9, F-EV2/3, F-DR*, F-GT1): están en los índices de `results/` y en sus
docs de origen. **No los transcribo acá para no crear una segunda fuente**: el catálogo
vive en los índices verificados y este documento solo señala los que sostienen una
afirmación del capítulo.

---

