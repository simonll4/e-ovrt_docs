# E-OVRT-VDP - paquete de etapa 2

> Generado el 2026-08-28. Etapa 2: seccion 17.1 (los Anexos C y D se corrigen aparte, D-E2-1).

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

- **Etapa activa:** 2 - Etapa 2: seccion 17.1 (los Anexos C y D se corrigen aparte, D-E2-1).
- Este archivo contiene el texto vigente que se modifica y sus insumos de ajuste.
- No se trasladan resultados propios hacia secciones cronologicamente anteriores.
- Nombre propio de esta etapa (01-etapa-2-activa.md): regenerarla no pisa el paquete de ninguna otra etapa.
- **Restriccion propia de esta etapa: §17.1 se corrige COMO PROTOCOLO** (regla de no-anacronismo, mapa regla 5). Entran decisiones, definiciones, criterios y valores de configuracion elegidos dentro de rangos declarados; **NO entran resultados medidos ni estados de implementacion**: eso se declara en §17.4/§17.5. Lo que el protocolo prescribio y no se ejercio (templates de prompt, vocabulario aislado-vs-completo cruzado, espanol, doble anotacion/kappa, MOT17/OVT-B y metricas MOT, NVDEC) **NO se borra ni se 'corrige' en §17.1**: queda como protocolo y §17.5 lo reporta como no ejercido.
- **Texto base = `90f` = §17.1 v1.3 (28.534 palabras, 118 titulos, Tablas 16–38), con el pase `correcciones-etapa-2.md` (E2-01..E2-26: las 12 fichas AJ-2.xx, la AJ-2.13, las podas 12–14 y los handoffs de las etapas 1 y 3) y el pase de formato F1–F6 YA APLICADOS Y VERIFICADOS el 2026-08-28. **La seccion esta CERRADA en contenido; no reaplicar nada.** Lo que queda de la etapa es externo al .docx: `90g` (Anexos C y D) y los handoffs hacia 17.3/17.4/17.5. **Guardrails:** §17.1.5 y §17.1.7 no se comprimen (no hay 'segunda vuelta'); los nombres de metrica que se ven vacios o como ⟦ECUACIÓN⟧ son objetos de ecuacion de Word, NO erratas; CPN/EN/TN y las siglas t_alert-system/TTFD/SDR nacen aca y §17.3/§17.4 las usan — no renombrar.
- **Decisiones firmadas (2026-08-28):** D-E2-1 el .docx es SOLO §17.1 (Anexos C y D aparte, en 90g) · D-E2-2 los codigos E-DIR/E-IND/E-HYB se bautizan en §17.1.5.4.2 y §17.3.6.4 recorta su glosa a una remision · D-E2-5 el nivel intermedio 'estado observable por persona' se declara en §17.1.7.3.1 (AJ-2.13) · D-E2-6 MOT17/OVT-B y metricas MOT intactos con ⊘ explicito · D-E2-3 la regla 're-alerta ≠ FP' va en §17.1.7.8.3 · D-E2-4 los 4.000/7.000 ms entran como decision dentro del rango de la Tabla 24, sin la palabra 'efectivos' · D-E2-7 marcador espejo de la AAIP en §17.1.11 · D-E2-8 PODA-14 solo recorta §17.1.4.
- **Formato:** el documento hereda del maestro un defecto que el pase corrige: §17.1.1 esta en estilo Heading 2 (el nivel de §17.1) con tabulador tras el numero — debe ser Heading 3 con espacio, como sus hermanas §17.1.2…§17.1.12. La remision a 'la seccion 16.7.6' es hoy §16.7.3. Verificacion: `verificar_entregable.py <entrega.docx> --seccion 17.1`.

---

## Fuente: `docs/informe/entregable/desarrollando/archivado/correcciones-etapa-2.md`

> SHA-256 del bloque: `482bb8e3839a11f4e2627e892256c90b44c4497ae8916b7662e19a527eb9be46`  
> Seleccion: EL PASE DE LA ETAPA 2 (2026-08-28): comentarios E2-01..E2-26 y decisiones D-E2-1..9. **YA APLICADO Y VERIFICADO** en el documento de trabajo v1.3 (misma jornada; constancia en `correcciones-etapa-2-pase-2.md`) - **NO volver a aplicarlo**. Sigue rigiendo como criterio de lectura y manda sobre las fichas AJ-2.xx donde las precisa o corrige.

# Correcciones de la Etapa 2 — §17.1 Consolidación Metodológica (pase 1, 2026-08-28)

> **Estado: NO aplicado — es el trabajo a hacer.** Texto base: `90f-etapa2-texto-extraido.md`
> (extracción del documento de trabajo
> `desarrollando/E-OVRT-VDP_Seccion_17.1_Consolidacion_Metodologica_v1.0.docx`, que es el §17.1
> del informe v1.1 **sin ninguna corrección**: 32.669 palabras, 122 títulos, Tablas 16–38, 85
> ecuaciones de Word). Este pase **integra y precisa** las 12 fichas `AJ-2.xx` de `ajustes/02`,
> agrega la ficha **AJ-2.13**, aplica las podas **PODA-12/13/14** y resuelve los handoffs que
> dejaron las Etapas 1 y 3. Donde este pase y una ficha difieren, **manda este pase** (las fichas
> se escribieron el 08-10 con la plataforma a medio construir; el relevamiento `operacion/130`
> del 08-28 verificó cada afirmación contra los repos).
>
> **Regla de lectura de §17.1 (no-anacronismo, mapa regla 5):** §17.1 es el **protocolo**. Entran
> decisiones, definiciones, criterios y valores de configuración elegidos dentro de rangos
> declarados. **No entran** resultados medidos, cifras propias ni estados de implementación —
> eso vive en §17.4/§17.5. Lo que el protocolo prescribió y no se ejerció **no se borra ni se
> "corrige" acá**: queda como protocolo (con su criterio de aplicabilidad, si hace falta) y
> §17.5 lo reporta como no ejercido. Guardrails: **§17.1.5 y §17.1.7 no se comprimen** (`07` §9);
> los nombres de métrica que se ven como `⟦ECUACIÓN⟧` o vacíos son objetos de ecuación de Word,
> **no erratas** (mapa `00` §7).
>
> **Autocontención:** nada de lo que sigue —códigos `E2-`, `AJ-`, `D-E2-`, `R-`, `F-`, rutas,
> ADRs, docs de `operacion/`— aparece en el texto del informe. Los únicos identificadores que el
> informe usa son los que define para sí: CR-xx, PR-xx, E-DIR/E-IND/E-HYB (desde este pase),
> P-E1-xx, L1–L8, nombres de configuración.

---

## A. Decisiones que gobiernan el pase

| ID | Decisión | Firma |
|---|---|---|
| **D-E2-1** | El `.docx` de la etapa es **sólo §17.1**. Los Anexos C y D se corrigen en este mismo pase (§E) pero **fuera** del documento: quedan en `90g-etapa2-anexos-c-y-d.md` para que el equipo los arme en §19 (mismo mecanismo que el Anexo A en `90e`). | usuario · 2026-08-28 |
| **D-E2-2** | Los códigos **E-DIR / E-IND / E-HYB se bautizan en §17.1.5.4.2** (E2-09). **Dependencia inversa:** §17.3.6.4 (v1.4) debe recortar su glosa a una remisión → handoff a la Etapa 3 (§F). | usuario · 2026-08-28 |
| **D-E2-5** | Ficha nueva **AJ-2.13**: el nivel intermedio **"estado observable por persona"** se declara en §17.1.7.3.1 como nivel de análisis (E2-18), sin cifras. | usuario · 2026-08-28 |
| **D-E2-6** | MOT17/OVT-B (§17.1.6.3) y métricas MOT (§17.1.7.4.2) **intactos**, con ⊘ explícito (E2-16). Las dos métricas derivadas de la plataforma (`t_capture→alert`, `t_compute-budget`) **no se declaran** en §17.1: ninguna sección del informe las usa. | usuario · 2026-08-28 (bis: recomendación adoptada) |
| D-E2-3 | AJ-2.02 se resuelve como **regla de conteo** en §17.1.7.8.3 (E2-22), no como corrección de una política que §17.1 nunca describió. | recomendación adoptada |
| D-E2-4 | Los 4.000/7.000 ms entran en §17.1.5.3.3 como **decisión de protocolo dentro del rango de la Tabla 24**, sin tocar la tabla y sin la palabra "efectivos" (E2-07). | recomendación adoptada |
| D-E2-7 | AAIP: marcador **espejo** en §17.1.11.1 (E2-25). | recomendación adoptada |
| D-E2-8 | PODA-14 **sólo recorta §17.1.4**; lo recortado se verifica contra las Tablas B.1–B.7 y lo que falte se lista como alta al Anexo B (E2-06). | recomendación adoptada |
| D-E2-9 | Duplicación Tabla 35 ↔ Anexo D: se conserva **la de §17.1.7.7.6** (donde se decide el criterio, D-P3-4) y la del Anexo D se reduce a las filas que agrega más una remisión (E2-20, se resuelve en `90g`). | recomendación — **confirmar al aplicar** |

---

## B. Unidades del pase — por orden de aparición en §17.1

Formato de cada unidad: **qué dice hoy** · **qué está mal o qué falta** (con la fuente verificada) ·
**acción** · texto guía cuando corresponde. Prioridad: 🔴 falso o contradictorio · 🟠 hueco de
concreción · 🟡 precisión / higiene · ⊘ no se aplica (con causa).

### E2-01 · 🔴 · Formato heredado — §17.1.1 con estilo de nivel equivocado
**Hoy:** el título *17.1.1. Función y Alcance…* está en estilo `Heading 2` (el nivel de §17.1) y
lleva un **tabulador** tras el número; sus hermanas §17.1.2…§17.1.12 son `Heading 3` con espacio.
Heredado del maestro v1.1. El verificador lo reporta como *"numeración: §17.1. arranca en 2"*.
**Acción:** aplicar `Heading 3` y reemplazar el tabulador por un espacio. Sin cambio de texto.

### E2-02 · 🔴 · §17.1.6.1.1 — remisión rota a "la sección 16.7.6"
**Hoy:** *"…preguntas rectoras P-E1-03 y P-E1-08 formuladas en la sección 16.7.6…"*. Tras la
Etapa 1, esa subsección es **§16.7.3** (E1-53). Las seis preguntas que §17.1 invoca (P-E1-01, 02,
03, 04, 06, 08) son exactamente las seis que sobrevivieron: **no hay nada más que reponer**.
**Acción:** `16.7.6` → `16.7.3` (única aparición). No tocar los códigos P-E1-xx.

### E2-03 · 🟡 · §17.1.4.2.1 — sistema operativo del CPN
**Hoy:** el CPN candidato se describe con **Windows 11**. **Verificado:** la plataforma corre en
**Linux (WSL2)** y en contenedores Ubuntu; no existe rama Windows. Es una decisión de entorno, va
hacia atrás. **Acción:** una frase: *"El entorno de ejecución adoptado fue Linux (WSL2 sobre el
equipo descrito) y contenedores Linux, por compatibilidad del stack de inferencia y del bus."*
Si la mención a Windows 11 está en el Anexo B (Tabla B.x) y no en el cuerpo, corregir allí (→ 90g).

### E2-04 · 🟠 · §17.1.4.2.3–.4 — la fuente del escenario EBE (AJ-2.10)
**Hoy:** OAK-D Pro PoE *candidata preferente*; cámara IP convencional como *plan de contingencia*.
**Verificado:** la OAK-D está integrada como fuente `oak_d` del plano de medios y **la contingencia
(RTSP) se ejerció primero**; el RTSP sintético (mediamtx + ffmpeg) es herramienta de desarrollo y
vía de reproducibilidad DBE↔EBE con fuente idéntica, no fuente experimental. **Acción:** en
§17.1.4.2.4 declarar la prioridad como decisión: ambas fuentes se integran; la cámara IP por RTSP
se adopta primero por disponibilidad y la OAK-D después; la fuente sintética se declara como
herramienta. **Sin resultados** (los fps reales, las corridas y el rodaje son de §17.4/§17.5).

### E2-05 · 🟡 · §17.1.4.5.1 — resolución de referencia
**Hoy:** parámetros de referencia ≈640 px (Tabla B.6). **Verificado:** la resolución es parámetro
del **perfil de modelo** (YOLOE 640; Grounding DINO 800 por default y 560 como variante), y el
propio §17.1.7.7.5 ya exige recalibrar umbrales si la resolución difiere de 640. **Acción:** una
frase que declare que la resolución de inferencia es un parámetro del perfil de modelo, fijado por
la selección de modelos con umbrales recalibrados por perfil. Sin valores de resultado.

### E2-06 · 🟠 · PODA-14 — §17.1.4 Entorno (3.261 palabras) → detalle al Anexo B (D-E2-8)
**Qué se poda:** el detalle de hardware/stack que **ya está** en las Tablas B.1–B.7 (§17.1.4.2.1
CPN, .2.2 NVDEC, .2.5 stack CPN, .3.1–.3.3 TN, .4.5 parámetros/transporte). **Qué se conserva
íntegro:** §17.1.4.1, la definición de roles CPN/EN/TN (dos o tres frases: §17.3 y §17.4 se apoyan
en que **nacen acá**), §17.1.4.2.3–.4 (E2-04), §17.1.4.4 escenarios DBE/EBE (§17.3.3.3 y §17.4
remiten a **17.1.4.4** por número: no renumerar), §17.1.4.6 restricciones y §17.1.4.7 lectura.
**Ahorro esperado ~1.000 palabras.** Cada dato que se saque debe estar en B.1–B.7; lo que no esté
se lista al final del entregable como *"altas al Anexo B"* (no se edita el Anexo B acá).
**NVDEC (§17.1.4.2.2):** conservar como opción del protocolo; **no** afirmar que se usó.

### E2-07 · 🟠 · §17.1.5.3.3 y Tabla 24 — los valores de persistencia como decisión (AJ-2.01, D-E2-4)
**Hoy:** PR-01 alto **3–5 s**, PR-02 medio **5–10 s**; persistencia en segundos, no en frames;
histéresis activación ≠ desactivación ya pedida. **Verificado:** el conjunto de patrones adoptó
CR-01 confirmación **4.000 ms** / resolución 2.000 ms y CR-02 **7.000 ms** / 3.000 ms —
**dentro de los rangos**. **Acción:** **no tocar la Tabla 24**; agregar al final de §17.1.5.3.3
una frase de decisión: *"Como valores de protocolo dentro de esos rangos se fijan 4.000 ms de
persistencia para la confirmación de PR-01 y 7.000 ms para PR-02, con umbrales de desactivación
de 2.000 y 3.000 ms respectivamente, expresados en milisegundos para independizarlos del ritmo de
cuadro efectivo."* **Prohibido:** "valores efectivos", "configurados", cualquier cifra medida
(la casa de los valores efectivos es §17.4).

### E2-08 · 🟡 · §17.1.5.3.3–.4 — "evita alertas repetidas sobre una misma situación"
**Hoy:** la histéresis *"reduce oscilaciones de estado y evita alertas repetidas sobre una misma
situación"*. **Verificado:** dentro de un episodio no hay repetición (el estado `sustained` no
emite); pero **tras la resolución el motor vuelve a alertar** si la condición reaparece, y la
supresión de re-notificación es política del tramo de distribución, no del motor (decisión de
diseño). **Acción:** precisar la frase: *"…evita oscilaciones y alertas repetidas **dentro de un
mismo episodio**; la reaparición de la condición tras su resolución constituye un episodio nuevo,
y la eventual supresión de notificaciones repetidas se define fuera del motor de patrones."*
Esto deja **coherente** la regla de conteo de E2-22.

### E2-09 · 🔴 · §17.1.5.4.2 — bautizar E-DIR / E-IND / E-HYB (D-E2-2; C-1 del pase 1)
**Hoy:** el eje *"Estrategia de detección"* distingue formulaciones **directas** e **indirectas o
descompuestas** en prosa; los códigos no existen en todo el informe fuera de §17.3/§17.4/§17.5,
y §17.3.6.4 (v1.4) los hace nacer con una glosa porque la remisión a §17.1.5.4.2 era falsa (E3-42).
**Acción:** al final del párrafo *"Estrategia de detección…"* insertar el texto guía de C-1:

> *"En este trabajo estas familias se identifican con un código: estrategia directa (E-DIR),
> cuando el prompt intenta describir la condición de riesgo completa; estrategia indirecta
> (E-IND), cuando el detector identifica entidades visibles por separado y la condición se
> reconstruye mediante lógica externa al modelo; y estrategia híbrida (E-HYB), cuando se combinan
> consultas de ambos tipos bajo una regla de composición explícita. Los códigos identifican las
> variantes en el diseño arquitectónico y en la evaluación experimental."*

**Verificar al aplicar:** que ninguna aparición de los códigos quede *antes* de esta glosa dentro
de §17.1 (hoy hay cero). **Handoff a la Etapa 3 (§F):** §17.3.6.4 recorta su glosa a *"…para las
estrategias directa (E-DIR) e híbrida (E-HYB) definidas en la consolidación metodológica"*.

### E2-10 · ⊘ · AJ-2.04 — los "ejes que faltaban" ya están en el protocolo
**Verificado sobre `90f`:** §17.1.5.4.2 ya trae el eje de **contexto de vocabulario** (*"cada
prompt … en aislamiento y en contexto completo"*, e *"Implicancias del tamaño del vocabulario
activo"*), la **variante con template** (*"a photo of a [CLASS]"*) y §17.1.5.4.5 Fase 2 ya exige
**hiperparámetros constantes** entre variantes. La ficha AJ-2.04 apuntaba a nuestro diseño de
campañas, no al informe. **No se edita §17.1.** Lo que se ejerció de cada eje (vocabulario en
régimen asimétrico sustituido por un control único; templates definidas y no medidas;
hiperparámetros congelados con umbrales operativos calibrados por brazo) **se declara en §17.5**
(handoff §F).

### E2-11 · 🟡 · §17.1.5.4.5 Fase 1 — el piso muestral y la vía elegida (AJ-2.05)
**Hoy:** *"~200 instancias positivas por condición, o bien reportar el tamaño efectivo con
intervalos de confianza"*. **Acción:** declarar la vía como decisión de protocolo: *"Cuando una
condición o un estrato no alcance ese piso, el protocolo exige reportar el n efectivo con
intervalos de confianza al 95 % obtenidos por bootstrap sobre las unidades de evaluación, y
abstenerse de ordenar variantes cuyos intervalos se superpongan."* **Sin n**: los n por
condición y estrato son de §17.5 (limitación L8).

### E2-12 · 🟠 · §17.1.5.4.5 Fase 1 — doble anotación y kappa: criterio de aplicabilidad (AJ-2.06)
**Hoy:** *"≥20 % doblemente anotado, kappa de Cohen para etiquetas e IoU para cajas"*, aplicable
a toda anotación de estado EPP. **Verificado:** no se ejerció (limitación L2): en imágenes se
**reutilizó** la anotación de las fuentes (negativos explícitos) sin anotación nueva; en video la
anotación fue humana pero sin doble anotador; la auditoría humana del GT de imágenes **no se
ejecutó** (sólo su kit). **Acción:** el requisito **se conserva** y se le agrega su criterio de
aplicabilidad, que es protocolo: *"El requisito rige para toda anotación producida por el
proyecto; cuando la referencia se reutilice de anotaciones de fuente sin re-anotación, la doble
anotación no aplica y la ausencia de una medida de acuerdo debe declararse como limitación del
material."* **Prohibido:** escribir "no se hizo" (eso es §17.5).

### E2-13 · 🟠 · §17.1.5.4.4–.5 — el catálogo de candidatos y las métricas por formulación (AJ-2.07)
**Acción (a)** §17.1.5.4.4: declarar que el prompt set se construye **desde el catálogo del
Anexo C (Tabla C.1)** y que las formulaciones finalistas se seleccionan con acta previa a la
evaluación. **(b)** §17.1.5.4.5 Fase 4: sumar **confianza media de los verdaderos positivos** como
indicador de estabilidad por formulación y, para la estrategia indirecta, **métricas por entidad
componente** (`person`, `helmet`, `vest`) para atribuir la degradación. Son criterios: si alguno no
se ejerció, lo dice §17.5. **(c)** El catálogo de **datasets** del Anexo C se corrige en `90g` (§E).

### E2-14 · 🔴 · PODA-12 — §17.1.6.2 Datasets de gestión directa (5.062 palabras) y Tabla 26
**Hoy:** inventario de 9 datasets (SH17, SHEL5K, CHV, Pictor-PPE, Construction-PPE, GDUT-HWD,
SHWD, SODA, MOCS) escrito **antes** de la selección efectiva, con **licencias que el registro no
confirma** (GDUT-HWD "Apache-2.0" y SHWD "MIT" → nunca verificadas; CHV "CC BY 4.0" es la licencia
del *paper*, el dataset no declara licencia — limitación L7; MOCS descrito como el original de
41.668 imágenes con acceso por solicitud, cuando lo evaluado fue una copia pública de 1.471
imágenes). **Omite** `construction_site_safety` y `ppe_siabar`, incorporados al inventario después
del protocolo (junio de 2026) y que resultaron ser la fuente del núcleo curado del banco y del
entrenamiento. **Acción:** comprimir §17.1.6.2 a **(i)** los criterios C1–C7 (intactos), **(ii)**
una **ficha breve por dataset retenido** (SHEL5K, CHV, `construction_site_safety`, `ppe_siabar` —
como candidatos incorporados al inventario, con su licencia tal como figura en el registro) y
**(iii)** una **tabla de descartados con causa en una línea** (SH17: CC BY-NC-SA; Pictor-PPE:
licencia no verificable; Construction-PPE: AGPL-3.0; GDUT-HWD/SHWD: licencia sin verificar y
condición ya cubierta; SODA: cubre condiciones fuera del núcleo; MOCS: copia pública parcial, uso
sólo exploratorio). **Prohibido:** decir cuál se usó para entrenar y cuál para el banco con
cifras — eso es §17.4/§17.5. **Sí** puede decirse, como decisión de diseño, que **una fuente no
puede ser a la vez material de entrenamiento y estrato del banco** (es la Tabla 28 aplicada).
Ahorro esperado ~3.000 palabras. Las Tablas 27/29/31 se recortan a los retenidos.

### E2-15 · ⊘ · Tabla 28 — rango de entrenamiento 500–2.000 imágenes
**Verificado:** el entrenamiento efectivo usó 2.946 imágenes: **desviación no justificada en
ninguna bitácora**. **No se toca §17.1** (la nota de la Tabla 28 ya exige *"justificarse
explícitamente"*). **Handoff a §17.4/§17.5:** declarar la desviación y su causa (se tomó el 100 %
de los linajes elegibles tras deduplicación y exclusión de las fuentes del banco).

### E2-16 · ⊘ · §17.1.6.3 (MOT17 / OVT-B) y §17.1.7.4.2 (métricas MOT) — intactos (D-E2-6)
Pre-registradas y no ejercidas (exclusión de las métricas MOT con fundamento medido; no hay GT de
identidades). El texto **ya está en condicional** (*"deseables sobre subsets específicamente
preparados"*, *"función acotada de verificación"*). **No se edita, no se poda, no se "corrige".**
§17.5 las reporta en su bloque de caminos no ejecutados.

### E2-17 · 🟡 · §17.1.8 y Tabla 36 — las fases y el orden (AJ-2.08)
**Acción:** conservar los nombres de fase de la Tabla 36 y agregar una nota de protocolo: *"La
secuencia expresa dependencias entre fases, no un calendario: el orden y las fechas efectivas de
ejecución se documentan en la implementación."* Nada más — el orden real (EBE antes que la
sensibilidad de prompts; ajuste fino al final) es de §17.4.

### E2-18 · 🟠 · §17.1.7.3.1 — el nivel intermedio "estado observable por persona" (AJ-2.13, D-E2-5)
**Hoy:** la jerarquía distingue métricas primarias/secundarias/conceptuales y familias (detección
OVD, seguimiento, pipeline, operativas), pero **no nombra el nivel intermedio** entre la percepción
por imagen y la alerta temporal por episodio, que §17.5 usa como eje. **Acción:** agregar al
comienzo de §17.1.7.3.1 un párrafo de decisión:

> *"El framework distingue tres niveles de análisis, cada uno con su unidad de evaluación. El
> nivel de percepción evalúa las detecciones por imagen contra las anotaciones de referencia. El
> nivel de estado observable por persona evalúa, para cada persona detectada, si el estado
> derivado —presencia o ausencia del elemento de protección— coincide con la referencia,
> componiendo geométricamente las entidades detectadas sin requerir identidades persistentes ni
> seguimiento. El nivel de alerta temporal evalúa la alerta confirmada por episodio contra una
> referencia temporal anotada. Las métricas de detección alimentan el primero; precision y recall
> por persona el segundo; las métricas operativas del apartado 17.1.7.5, el tercero."*

**Opcional:** una fila en la Tabla 34 para *"Precision/Recall de estado por persona"* (nivel
secundario u obligatorio, a criterio). Sin cifras.

### E2-19 · 🟡 · §17.1.7 — diccionario de métricas y reparto con el diseño (AJ-2.03, D-P3-4)
**Verificado:** §17.1.7 **ya define** G2A (*Glass-to-Algorithm*, subtramo), el tramo
*Glass-to-Alert*, `t_alert-system`, `t_alert-notification`, TTFD, SDR y ΔFP_tracker, con la
Tabla 34 y los umbrales de la Tabla 35; §17.3.13 (v1.4) trae la **materialización** (relojes,
señales, estados de aplicabilidad). El reparto vigente es correcto: **§17.1 = nombres,
definiciones y criterios; §17.3 = materialización; §17.4 = valores efectivos.** **Acción:** sólo
verificar consistencia terminológica (G2A siempre *Glass-to-Algorithm*; el tramo hasta la alerta
siempre *Glass-to-Alert*; `t_alert-notification` "complementaria, sólo con trayecto instrumentado")
y que las **siglas nazcan con su nombre completo la primera vez** (TTFD, SDR y `t_alert-system`
nacen acá y §17.3 las usa). **No agregar** `t_capture→alert` ni `t_compute-budget` (D-E2-6 bis).

### E2-20 · 🟡 · §17.1.7.7.6 Tabla 35 ↔ Anexo D — la duplicación verificada (D-E2-9)
La tabla *"Umbrales orientativos por severidad"* aparece **dos veces** (mismo título, mismas
filas, mismos valores; la del Anexo D es superconjunto). **Acción:** conservar la Tabla 35 en
§17.1.7.7.6 (es donde se decide el criterio) y, en `90g`, reducir la del Anexo D a las filas que
agrega más una remisión a la Tabla 35. Las otras dos duplicaciones 🟡 de `ajustes/09` (Tabla 31 ↔
Anexo C; Tabla 34 ↔ detalle del Anexo D) se **confirman al aplicar** y se resuelven con el mismo
criterio.

### E2-21 · ⊘ · §17.1.7.8 — instrumentación: el protocolo no cambia (AJ-2.09)
El apartado **ya exige** los cinco hitos por alerta, P50/P95/P99 + promedio, warm-up, timestamps
monotónicos con fuente declarada y la bitácora mínima. **No se edita.** Lo que se cumplió y lo
que quedó parcial (cuatro de cinco hitos en el plano de control; percentiles del tramo de
plataforma sí, del evaluador de alertas sólo promedio; hardware y entorno no registrados por
corrida; warm-up de modelo sí, de unidades no) **se declara en §17.4** (handoff §F). La ficha
AJ-2.09 nombraba `report.json`/`metrics.json` como artefactos del plano de medios: no existen ahí
(`summary.json` + `metrics.jsonl`); corregido en la ficha, no afecta a §17.1.

### E2-22 · 🟠 · §17.1.7.8.2–.3 — estados de aplicabilidad y reglas de lectura (AJ-2.12, D-E2-3)
**Acción (a)** §17.1.7.8.2: agregar la regla de **estado de aplicabilidad**: *"Una métrica que no
corresponde medir se reporta con su estado y su causa (no aplicable por ausencia de referencia,
por fuente sin temporalidad, por trayecto no instrumentado), nunca como cero ni por omisión."*
**(b)** §17.1.7.8.3, junto a la unidad de conteo del falso positivo, la **regla de conteo**:
*"La re-emisión de una alerta por reconfirmación del mismo patrón tras su resolución no se
computa como falso positivo; se registra y se reporta por separado."* **(c)** §17.1.7.8.3, las
**reglas de lectura** como criterios: reportar **por estrato y escenario**, nunca sólo el agregado;
los materiales sin condición (negativos) **no entran** en precision/recall/F1 — su métrica es el
conteo de falsos positivos; la **SDR no se compara entre cadencias** de muestreo distintas; la
latencia de alerta **no se compara entre densidades** de evidencia sin controlar qué episodios
sobreviven. Todas son criterios pre-registrables; ninguna trae cifra.

### E2-23 · 🟠 · §17.1.9 y Tabla 37 — el encuadre del ajuste fino (AJ-2.11)
**Hoy:** la Tabla 37 ya dice *"la regla no prescribe que el fine-tuning deba ejecutarse; define
cuándo vale la pena"*. **Acción:** conservar la tabla y agregar, como decisión de protocolo, que la
rama **se ejerce como jornada experimental completa con criterios pre-registrados** (baseline
única, márgenes firmados antes de evaluar, veredicto por gate) y que sus condiciones son **de
datos y de protocolo, no de cómputo** (el nodo de entrenamiento existe: §17.1.4.3.1). **Buscar y
eliminar** cualquier formulación del tipo "según presupuesto de tiempo" o "si el cronograma lo
permite" en §17.1.9/§17.1.10. **Prohibido:** T1/T2/T3, cifras, veredictos (§17.4/§17.5).

### E2-24 · 🟡 · PODA-13 — §17.1.10 Proyección (659 palabras) → párrafo puente
Las "instancias posteriores" ya ocurrieron (§17.3–§17.5). **Acción:** reemplazar las cuatro
subsecciones por **un párrafo** que diga qué toma cada instancia posterior de esta consolidación
(entorno → diseño; condiciones y prompts → diseño y evaluación; datos → implementación; métricas →
evaluación), sin adelantar resultados. Renumerar: §17.1.11 → §17.1.10 y §17.1.12 → §17.1.11 **sólo
si** ninguna otra sección remite a ellas por número (verificar en `90`, `90b`, `90c`: hoy no hay
remisiones a 17.1.11/17.1.12). Ahorro ~450 palabras.

### E2-25 · 🟠 · §17.1.11.1 — el marcador espejo de la AAIP (D-E2-7, handoff de D-E1-11)
**Acción:** en la política de minimización y uso asistivo, insertar el marcador con el texto
exacto de §16.6.2.2: `[[PENDIENTE: definir con el equipo la aplicabilidad de esta inscripción al
contexto experimental y documentar el recaudo adoptado en §17.1 y §17.4.]]`. **No redactar** una
respuesta: es decisión del equipo y el marcador viaja.

### E2-26 · ⊘ · AJ-2.02 — premisa falsa
La ficha decía que *"el §17.1 también describe la política de alerta y arrastra el mismo error"*
(cooldown en el motor). **Verificado:** §17.1 no menciona cooldown, supresión, re-alertas ni
re-notificación (cero apariciones; ya lo había verificado el pase 2 de la Etapa 3). Lo único
cercano es la frase de la histéresis, precisada en E2-08. La regla `re-alerta ≠ FP` entra por
E2-22. **Se cierra como ⊘.**

---

## C. Pase 2 — formato y terminología (después del contenido, como en la Etapa 1)

Se aplica **sobre la entrega del pase 1**, nunca sobre el documento inicial (lección del 08-28:
entregar siempre el último final). Mismas seis reglas F1–F6 del pase 5 de la Etapa 1:
**F1** títulos en tipo frase (hoy §17.1 está en Title Case: *"Función y Alcance de la
Consolidación Metodológica"* → *"Función y alcance de la consolidación metodológica"*), respetando
las siglas; **F2** rótulos `**Tabla N**` (hoy `***Tabla N***`); **F3** notas `*Nota.*` (hoy `Nota.`
sin formato y una variante `**Nota***.*`); **F4** rótulos de párrafo con el punto dentro de la
negrita; **F5** terminología: *cuadro* (no frame/fotograma, salvo "frame-a-frame" si se conserva
como término técnico → preferir *cuadro a cuadro*), *extremo a extremo*, *seguimiento* (no
tracking, salvo tracking-by-detection); **F6** siglas definidas en su primera aparición. **Las
ecuaciones de Word no se tocan.** Verificación: `verificar_entregable.py <entrega.docx> --seccion
17.1` en OK, cero `[[…]]` salvo el de la AAIP, cero andamiaje.

---

## D. Lo que NO hay que tocar en este pase

1. **§17.1.5** (9.426 palabras) y **§17.1.7** (6.605): protocolo ejercido y framework de métricas —
   sólo las inserciones puntuales listadas (E2-07…E2-13, E2-18…E2-22). Sin compresión.
2. **Los objetos de ecuación** (`t_alert-system`, `t_alert-notification`, `G2A`, `T_persistencia`,
   `ΔFP_tracker` y los 85 restantes): se ven como `⟦ECUACIÓN⟧` en la extracción y vacíos en las
   tablas. **Verificar en el `.docx` final que la sigla de §17.1.7.5.1 se lea** (pase 3 §I).
3. **Tabla 24** (ventanas y trade-off por severidad): §17.3.10.3 la cita y no la toca.
4. **CPN / EN / TN** (§17.1.4.2) y las siglas **TTFD / SDR / `t_alert-system`** (§17.1.7.5): nacen
   acá; §17.3 y §17.4 las usan sin redefinir. No renombrar, no mover.
5. **§17.1.4.4** (escenarios): única remisión numérica desde §17.3/§17.4. No renumerar.
6. **P-E1-xx**: los seis códigos que §17.1 invoca son parte del informe (excepción de la regla de
   andamiaje).
7. Todo el §1 de `nucleo/historicos/08` — lo que el informe **valida**.

---

## E. Anexos C y D — se corrigen aparte (D-E2-1) → `90g-etapa2-anexos-c-y-d.md`

Texto base: `96e` §19.3–§19.4. Correcciones: **(a)** Anexo C, catálogo de datasets: separar
**candidatos evaluados** de **retenidos**, y dentro de los retenidos distinguir **material de
entrenamiento** de **fuentes del banco de imágenes** — **sin** afirmar que `chv` se entrenó (el
entrenamiento efectivo lo excluyó; el rol "TRAIN" que las fichas viejas le daban era histórico);
`bench_obra` **no es un dataset** sino el estrato curado a partir de `construction_site_safety`;
licencias como en el registro (E2-14). **(b)** Anexo C, Tabla C.1: es la fuente declarada del
prompt set (E2-13). **(c)** Anexo D: tabla de umbrales reducida a lo que agrega + remisión a la
Tabla 35 (E2-20); confirmar las otras dos duplicaciones. **(d)** Anexo B: **no se edita**; recibe la
lista de "altas" que produzca E2-06. El equipo integra los anexos en §19.

---

## F. Handoffs que salen de esta etapa

| Hacia | Qué | Origen |
|---|---|---|
| **Etapa 3 (§17.3 v1.4 → v1.5)** | Recortar la glosa de §17.3.6.4 a la remisión *"…estrategias directa (E-DIR) e híbrida (E-HYB) definidas en la consolidación metodológica"*; revisar el solape §17.3.3.1 ↔ §17.3.3.2 con lo que quede en §17.1 (pase 3 §I). | E2-09 · D-E2-2 |
| **Etapa 4 (§17.4 v1.6)** | Declarar: orden de disparo real **control → distribución → medios** (hoy §17.4 dice "inverso al flujo de datos"); desviación del rango 500–2.000 (2.946) con causa; artefactos del plano de medios (`summary.json`/`metrics.jsonl`, no `report.json`); 4/5 hitos; percentiles sólo del tramo de plataforma; hardware/entorno no registrados por corrida; warm-up de unidades = 0; SO Linux/WSL2; G2A desde el dequeue y sin tramo sensor/red en RTSP. | E2-15 · E2-21 · `operacion/130` §4 |
| **Etapa 5 (§17.5 v1.3)** | Reportar como no ejercidos: templates de prompt, vocabulario aislado-vs-completo cruzado (sustituido por el control B1 vs T2), español, doble anotación/kappa (L2), MOT17/OVT-B y métricas MOT, confianza media de TP; piso de 200 positivos sólo en CR-01/shel5k (L8); citar `n=5.313` **fechado** (GT del 23-jul; 5.308 con el vigente); comparación tiny 800 vs 560 con el caveat del umbral (0,35 vs 0,30); `t_alert-system` del banco es promedio por campaña. | E2-10 · E2-12 · E2-16 · `operacion/130` R-04/R-05/R-11 |
| **Anexos (§19, equipo)** | `90g` con Anexos C y D corregidos; altas al Anexo B. | E2-06 · §E |
| **Equipo** | D-E1-11 (AAIP) sigue abierta; el espejo viaja en §17.1.11.1. | E2-25 |

---

## G. Hechos verificados que este pase usa — NO "corregir" estos valores

| Hecho | Valor | Dónde se re-verifica |
|---|---|---|
| Texto base | 32.669 palabras · 122 títulos · 664 párrafos idénticos al `96b` · 85 ecuaciones OMML | `extraer_informe.py` + diff normalizado (`revision-previa-etapa-2.md` §1) |
| Persistencia adoptada | CR-01 4.000/2.000 ms · CR-02 7.000/3.000 ms · escena · sin cooldown | `e-ovrt_control-plane/configs/patterns/cr01_cr02_v2.yaml` |
| Códigos E-DIR/E-IND/E-HYB en §17.1 | **0** apariciones | `grep -c E-DIR 90f-…md` |
| Cooldown / re-alertas en §17.1 | **0** apariciones | `grep -ciE 'cooldown|re-?alert|supresi' 90f-…md` |
| P-E1 invocados por §17.1 | 01, 02, 03, 04, 06, 08 (9 veces) = los seis de §16.7.3 | `grep -o 'P-E1-[0-9]*' 90f 90d` |
| Remisión rota | `16.7.6` ×1 (§17.1.6.1.1) | `grep -n '16\.7\.6' 90f-…md` |
| Remisiones desde §17.3/§17.4 a §17.1 | sólo `17.1.4.4` ×1 | `grep -ohE '17\.1\.[0-9.]+' 90 90b` |
| Fine-tuning efectivo | css 2.203 + ppe_siabar 743 = 2.946 train / 483 val; `chv` excluido | `finetuning/manifests/finetuning_v1.summary.json` |
| Anexo B | Tablas B.1–B.7 existen en `96e` §19.2 | `grep -oE 'Tabla B\. ?[0-9]' 96e` |

---

## Fuente: `docs/informe/entregable/desarrollando/archivado/correcciones-etapa-2-pase-2.md`

> SHA-256 del bloque: `cac9961a4248a07dd082885d8213e1244318a65cb6e7fb5183143b47d83788cc`  
> Seleccion: pase 2 de la etapa 2 (2026-08-28, noche): la VERIFICACION de la entrega v1.2 y el cierre en v1.3 - estado por unidad E2, los tres arreglos de forma E2-27..E2-29, los residuales que NO se corrigen, el delta de referencias (13 bajas) y lo que queda fuera del .docx (90g y handoffs).

# Etapa 2 — pase 2: verificación de la entrega v1.2 y cierre en v1.3 (2026-08-28, noche)

> **Qué es.** La revisión "de pie a cabeza" de la entrega de ChatGPT sobre §17.1
> (`E-OVRT-VDP_Seccion_17.1_Consolidacion_Metodologica_v1.2.docx`, 16:07) contra el texto base
> `90f` v1.0 y contra el pase `correcciones-etapa-2.md` (fuente: `docs/informe/entregable/desarrollando/archivado/correcciones-etapa-2.md`). Resultado: **el
> contenido está bien y completo**; tres defectos de **forma** se repararon de manera determinista
> sobre el XML y el resultado es la **v1.3**, que pasa a ser el documento vigente de la etapa. La
> v1.0 (base) y la v1.2 (entrega) quedaron en `archivado/`.
>
> **Estado: APLICADO Y VERIFICADO. No hay trabajo de redacción pendiente sobre §17.1.** Lo que queda de
> la etapa es externo al `.docx` (§5).

---

## 1. Verificación mecánica

| Chequeo | v1.2 (entrega) | v1.3 (final) |
|---|---|---|
| `verificar_entregable.py --seccion 17.1` | **OK** (28.499 palabras · 118 títulos · `[[PENDIENTE]]`×1) | **OK** (28.534 · 118 · ×1) |
| Estilos de título | `Heading1` 1 · `Heading2` 1 · `Heading3` 11 · `Heading4` 41 · `Heading5` 65 — **§17.1.1 corregido** (E2-01) | ídem |
| Numeración | sin huecos; §17.1.10 (proyección) eliminada y §17.1.11/12 → §17.1.10/11 (E2-24) | ídem |
| Ecuaciones OMML | **85** (todas conservadas) | 85 |
| Runs que partan palabras con cambio de formato | **0** | 0 |
| Comentarios / cambios controlados | ninguno (la entrega vino sin cambios controlados; el diff se hizo contra `90f`) | — |
| Andamiaje (`AJ-`/`E2-`/`D-E2`/`R-`/rutas/ADR) | **0** (sólo los `P-E1-xx`, permitidos) | 0 |
| Cifras propias (no-anacronismo) | **0** — los únicos números nuevos son tamaños de dataset (SHEL5K 5.000, CHV 1.330), que son hechos de las fuentes | 0 |
| Marcadores | 1: el espejo de la AAIP (E2-25) | 1 |
| Referencias | avisos iguales a la v1.0 (Liu 2023/2024 · Wang 2021/2025: autores homónimos, no error) | ídem |

**Diff v1.0 → v1.2 (párrafos normalizados):** 667 → 629 párrafos · **59 nuevos** (1.948 palabras) ·
**97 eliminados** (5.402) · **113 modificados** (35 de ellos sólo terminología F5). Palabras:
32.669 → 28.499 (−12,8 %). Por sección: §17.1.6.2 **4.856 → 1.375** (PODA-12) · §17.1.10 eliminada
(PODA-13, 647 → párrafo puente) · §17.1.4 **3.138 → 2.666** (PODA-14, parcial: −472 contra ~1.000
esperadas; el detalle removido remite a las Tablas B.1–B.7, cuya correspondencia se verificó: B.1
CPN · B.2 EN/OAK-D · B.3 stack CPN · B.4 TN · B.5 stack TN · B.6 parámetros · B.7 topología) ·
§17.1.5 9.317 → 9.483 y §17.1.7 6.514 → 6.792 (**sólo inserciones**, guardrail respetado).
**Intactas** (filas idénticas): Tablas 24, 28, 36 y 37. **Intactos** (sólo el título a tipo frase):
§17.1.6.3 MOT17/OVT-B y §17.1.7.4.2 métricas MOT (D-E2-6).

## 2. Unidad por unidad

| Unidad | Estado | Evidencia en la v1.2 |
|---|---|---|
| E2-01 §17.1.1 estilo | ✅ | `Heading3`, sin tabulador |
| E2-02 16.7.6 → 16.7.3 | ✅ | §17.1.6.1.1, única aparición |
| E2-03 SO del CPN | ✅ | "El entorno de ejecución adoptado es Linux mediante WSL2 sobre el equipo descrito y contenedores Linux…"; `Windows` 4 → 0 (también en §17.1.4.6/.7) |
| E2-04 fuente EBE | ✅ | §17.1.4.2.3 reescrita (dos fuentes integrables; RTSP priorizada por disponibilidad; OAK-D posterior; ninguna presupone inferencia en borde); §17.1.4.2.4 retitulada *"Criterio de prioridad y fuente RTSP sintética"* |
| E2-05 resolución por perfil | ✅ | §17.1.4.5.1 |
| E2-06 PODA-14 | ◐ | −472 palabras; remisiones a B.1–B.7 correctas; sin "altas al Anexo B" (nada quedó sin destino) |
| E2-07 valores de persistencia | ✅ | frase exacta del texto guía al final de §17.1.5.3.3; Tabla 24 intacta; sin "efectivos" |
| E2-08 histéresis / episodio nuevo | ✅ | §17.1.5.3.4 |
| E2-09 bautismo E-DIR/E-IND/E-HYB | ✅ | glosa en §17.1.5.4.2; **primera y única aparición** de los tres códigos |
| E2-10 AJ-2.04 | ⊘ | sin cambios, como pedía |
| E2-11 piso muestral / bootstrap | ✅ | §17.1.5.4.5 Fase 1 |
| E2-12 criterio de aplicabilidad de la doble anotación | ✅ | §17.1.5.4.5 Fase 1 |
| E2-13 Tabla C.1 + acta · confianza media de TP · por entidad | ✅ | §17.1.5.4.4 y Fase 4 |
| E2-14 PODA-12 / Tabla 26 | ✅ | 4 retenidos (SHEL5K · CHV "sin licencia formal; cita obligatoria" · construction site safety · ppe siabar), Tabla 27 = descartados con causa en una línea, Tabla 29 aptitud de los 4, §17.1.6.4.1 licencias como el registro; Nota: "la retención expresa aptitud como candidato y no asignación efectiva" |
| E2-15 rango 500–2.000 | ⊘ ✅ | la regla se conserva en §17.1.6.2.4 ("justificarse si se apartan") |
| E2-16 MOT intacto | ✅ | ver §1 |
| E2-17 nota Tabla 36 | ✅ | "La secuencia expresa dependencias entre fases, no un calendario…" |
| E2-18 nivel "estado observable por persona" (AJ-2.13) | ✅ | párrafo de apertura de §17.1.7.3.1 |
| E2-19 diccionario / reparto | ✅ | frase nueva en §17.1.7.2 fijando `t_alert-system` y `t_alert-notification` (como texto, no como ecuación — ver §4) |
| E2-20 Tabla 35 | ✅ | conservada en §17.1.7.7.6 (el Anexo D se resuelve en `90g`) |
| E2-21 instrumentación | ⊘ | sin cambios de fondo; F5 en §17.1.7.8.1 |
| E2-22 aplicabilidad · regla de conteo · reglas de lectura | ✅ | §17.1.7.8.2 y §17.1.7.8.3 (por estrato y escenario · negativos fuera de P/R/F1 · SDR misma cadencia · latencia y episodios evaluables) |
| E2-23 ajuste fino como jornada | ✅ | párrafo en §17.1.9.2 ("criterios prerregistrados… de datos y de protocolo, no de disponibilidad de cómputo"); "presupuesto de tiempo/cronograma/plazo" 0 apariciones; §17.1.4.6 "sin convertir cómputo en criterio metodológico" |
| E2-24 PODA-13 párrafo puente | ✅ (reubicado, E2-29) | ver §3 |
| E2-25 marcador AAIP | ✅ (anclado, E2-28) | ver §3 |
| E2-26 AJ-2.02 | ⊘ | sin cambios, como pedía |
| Pase de formato F1–F6 | ✅ salvo F2/F3 (E2-27) | F1 títulos tipo frase ✓ · F4 puntos dentro de la negrita ✓ · F5 `cuadro` 4 → 44, `fotograma` 9 → 0, `tracking` 15 → 3 (`tracking-by-detection`, `TrackingNet`, *Multiple Object Tracking*), `end-to-end/E2E` 1 → 0 ✓ · F6 ✓ |

## 3. Tres defectos de forma, reparados sobre el XML → v1.3

| ID | Defecto en la v1.2 | Reparación (determinista, `document.xml`, validado con `ElementTree`) |
|---|---|---|
| **E2-27** | Los 23 rótulos `Tabla N` y las 21 notas venían en **negrita + itálica** (`***Tabla N***`, `***Nota***.`), contra la convención ya fijada en §15–§16 v1.0 y §17.5 v1.3 (`**Tabla N**` en negrita · `*Nota.*` en itálica; regla F2/F3 del pase 5 de la Etapa 1) | quitar `<w:i/>` de los runs de los 23 rótulos; quitar `<w:b/>` de los runs "Nota" y "." de las 21 notas. Resultado: 23 `**Tabla N**` · 21 `*Nota.*` |
| **E2-28** | El marcador `[[PENDIENTE: … aplicabilidad de esta inscripción …]]` quedó debajo de un párrafo que **no menciona ninguna inscripción** (habla de minimización y del régimen de datos personales): "esta inscripción" no tenía antecedente | se agregó al final del párrafo previo: *"Ese régimen prevé, además, la inscripción de las bases de datos con datos personales ante la autoridad de aplicación (AAIP); su aplicabilidad al material experimental del proyecto y el recaudo adoptado se documentan a continuación."* (+35 palabras). El marcador **no se tocó** y sigue viajando |
| **E2-29** | El párrafo puente de PODA-13 (*"Esta consolidación distribuye sus salidas hacia las instancias siguientes…"*) quedó **dentro de §17.1.9.2** (*Candidatos de comparación*), después de la nota de la Tabla 37 — fuera de tema | movido tal cual a **§17.1.11.2** (*Articulación con las instancias de diseño e implementación*), como segundo párrafo: es exactamente el tema de esa subsección y complementa su primer párrafo con qué toma cada instancia |

Diff v1.2 → v1.3 verificado por extracción: **sólo** esos tres cambios (un párrafo movido, una frase
agregada, formato de 44 rótulos). Verificador OK.

## 4. Residuales que NO se corrigen acá (anotados)

1. **PODA-14 parcial** (−472 palabras de ~1.000 estimadas). Lo removido quedó cubierto por B.1–B.7;
   no se fuerza más recorte: el guardrail es no cortar por cuota.
2. **`t_alert-system` / `t_alert-notification` en §17.1.7.2** están escritos como texto (con
   subíndice tipográfico) mientras en el resto del capítulo la sigla es un objeto de ecuación. Es
   legible (justo lo que pedía el pase 3 §I) y no se unifica: convertirlo a OMML a mano es más
   riesgoso que el beneficio. Se revisa en la integración final junto con los rótulos de nota del
   maestro.
3. Tabla 26: las filas de `construction site safety` y `ppe siabar` dicen *"Versión registrada"* en
   la columna de volumen. Es correcto pero pobre; si el equipo quiere el volumen, son hechos de
   las fuentes (2.799 y 1.607 imágenes) y pueden agregarse sin violar el no-anacronismo.
4. Los nombres de dataset se escriben con espacios (*construction site safety*, *ppe siabar*) y no
   como identificadores (`construction_site_safety`). §17.4/§17.5 deben usar la misma forma — se
   verifica en la integración.

## 5. Delta de referencias (para las Referencias globales del equipo)

**Bajas** por PODA-12/13/14 (ya no se citan en §17.1; **antes de sacarlas del listado global hay
que confirmar que ninguna otra sección las cite**): Ahmad y Rahimi, 2025 (SH17) · An et al., 2021
(MOCS) · Buslaev et al., 2020 (Albumentations) · Dalvi et al., 2025 (Construction-PPE) · Duan et
al., 2022 (SODA) · Ley 25.326, 2000 (sigue citada como *Argentina, 2000*) · Long y Li, 2023 · Mallick,
2025 · NJVisionPower, 2019 (SHWD) · Nath et al., 2020 y CIBER Lab, 2020 (Pictor-PPE) · Wu et al.,
2019 (GDUT-HWD). **Altas:** ninguna.

## 6. Lo que queda de la Etapa 2 — fuera del `.docx`

| Qué | Dónde | Estado |
|---|---|---|
| `90g-etapa2-anexos-c-y-d.md`: Anexos C y D corregidos (candidatos vs retenidos sin `chv` como entrenado; `bench_obra` no es dataset; Tabla C.1 fuente del prompt set; Anexo D → filas extra + remisión a Tabla 35) | texto base `96e` §19.3–19.4 | **pendiente** (D-E2-1) |
| Recortar la glosa de §17.3.6.4 a la remisión (dependencia inversa de E3-42) | §17.3 v1.4 → v1.5 | handoff Etapa 3 |
| Orden de disparo real (control → distribución → medios) y desviación 500–2.000 → 2.946 con causa | §17.4 v1.6 | handoff Etapa 4 |
| Declarar lo no ejercido del protocolo (templates, vocabulario cruzado, español, kappa/L2, MOT, confianza media de TP), `n=5.313` fechado, caveat del umbral tiny 800/560, `t_alert-system` = promedio | §17.5 v1.3 | handoff Etapa 5 |
| D-E1-11 (AAIP) | equipo | marcador viaja en §16.6.2.2 y §17.1.10.1 |

## 7. Cómo se re-verifica

```
python3 herramientas/verificar_entregable.py informe/entregable/desarrollando/E-OVRT-VDP_Seccion_17.1_Consolidacion_Metodologica_v1.3.docx --seccion 17.1
python3 herramientas/extraer_informe.py <v1.3> --out /tmp/v13.md ; python3 herramientas/extraer_informe.py desarrollando/archivado/<v1.2> --out /tmp/v12.md
diff <(sed -E 's/[*]+//g' /tmp/v12.md) <(sed -E 's/[*]+//g' /tmp/v13.md)      # sólo E2-28 y E2-29
grep -oE '^\**Tabla [0-9]+\**' /tmp/v13.md | sort | uniq -c ; grep -oE '^\**\*?Nota\*?\**\.?\**\*?' /tmp/v13.md | sort | uniq -c
grep -cE 'E-DIR|16\.7\.3|4\.000|estado observable por persona|bootstrap|re-alerta' /tmp/v13.md
```

---

## Fuente: `docs/informe/entregable/90f-etapa2-texto-extraido.md`

> SHA-256 del bloque: `9ee4291e50bf6eb74d688bdb0764a35ac082502db0734dc539386f75f06b12b6`  
> Seleccion: TEXTO BASE VIGENTE de la seccion 17.1: extraido del documento de trabajo `E-OVRT-VDP_Seccion_17.1_Consolidacion_Metodologica_v1.3.docx` (2026-08-28), con el pase E2-01..E2-26 y el pase de formato F1-F6 **YA APLICADOS Y VERIFICADOS** (28.534 palabras, 118 titulos, verificador OK). No cambiar una palabra de fondo sin un pase nuevo explicito. El 96b (v1.1 sin correcciones) queda como foto historica fuera del paquete. Las ecuaciones de Word aparecen como ⟦ECUACIÓN⟧: no son erratas.

# 90f — Texto extraído del documento de trabajo: §17.1 Consolidación Metodológica (v1.3)

> **Extracción derivada (2026-08-28)** del `.docx`
> `informe/entregable/E-OVRT-VDP_Seccion_17.1_Consolidacion_Metodologica_v1.3.docx`, **solo para búsqueda y cita**
> (mismo estatuto que el doc 90): al editar, se edita el `.docx`/Google Docs, nunca
> este archivo. Tablas y figuras pueden haber perdido formato; las figuras no se
> extraen y las ecuaciones no se convierten — quedan `⟦FIGURA: no extraída — ver el .docx⟧` y
> `⟦ECUACIÓN: no extraída — ver el .docx⟧` donde estaban. Regenerado con
> `herramientas/extraer_informe.py` (regla D-C del manual de aplicación).

---

## 17. Desarrollo del producto

### 17.1. Consolidación metodológica del protocolo experimental

La consolidación metodológica transforma el marco teórico construido previamente en un protocolo experimental utilizable. Para ello fija decisiones sobre alcance, escenarios, infraestructura, datos, prompts, métricas y criterios de aceptación, integrando los desarrollos metodológicos en una secuencia coherente con el objetivo del prototipo experimental.

El referente experimental resultante delimita qué condiciones de riesgo integran el núcleo del prototipo, cómo se estructuran los escenarios de evaluación, con qué reglas se gestionan los datos, qué métricas deben producirse y cómo debe interpretarse la evidencia obtenida.

Esta instancia no implementa el pipeline ni reporta resultados empíricos. Establece las condiciones de comparabilidad, medición e interpretación necesarias para que el prototipo pueda desarrollarse y evaluarse sobre bases explícitas, trazables y defendibles.

#### 17.1.1. Función y alcance de la consolidación metodológica

##### 17.1.1.1. Función metodológica dentro del trabajo

La función principal de esta parte del trabajo es ordenar la transición entre la fundamentación teórica y las instancias posteriores de diseño, implementación y validación. Para ello, la consolidación metodológica no se limita a enumerar componentes técnicos, sino que define el modo en que esos componentes serán evaluados, comparados e interpretados dentro del alcance experimental declarado.

El criterio rector prioriza la validez experimental, la trazabilidad y la correspondencia entre alcance, datos disponibles e instrumentación efectiva. El núcleo obligatorio del prototipo se ubica en las condiciones de Nivel 1 —CR-01 y CR-02—, donde convergen observabilidad visual, cobertura de datos, estrategias de evaluación defendibles y métricas aplicables con el hardware disponible. Las condiciones de Niveles 2 y 3 se conservan como extensiones condicionadas, debido a brechas de datos, visibilidad y razonamiento contextual.

A partir de ese criterio, se fija una secuencia experimental integrada: comparación primaria en Dataset-Based Evaluation (DBE), validación complementaria en Environment-Based Evaluation (EBE), reglas de partición sin leakage, política de formulación y congelamiento de prompts, jerarquía de métricas orientada al valor operativo de alerta y criterios para habilitar una rama comparativa de fine-tuning.

El resultado es un marco de trabajo que ordena el diseño, la implementación y la validación del prototipo, y que permite comparar variantes, medir desempeño e interpretar la evidencia bajo criterios consistentes.

##### 17.1.1.2. Articulación entre los desarrollos metodológicos

La consolidación metodológica se apoya en cuatro dimensiones temáticas. La primera caracteriza la infraestructura, los escenarios y las restricciones de ejecución; la segunda define el catálogo de condiciones, sus niveles de complejidad y la política de prompts; la tercera establece cobertura, brechas y reglas de partición de datos; y la cuarta organiza la evidencia mínima que el prototipo deberá producir.

La integración de estas dimensiones permite ordenar una cadena de decisión: primero se delimita qué debe construir el prototipo y bajo qué restricciones; luego se establece cómo será medido; finalmente se fijan los criterios de interpretación de la evidencia. Esta lógica evita tratar los componentes por separado y concentra las definiciones metodológicas que estructuran la continuidad del proyecto.

**Tabla 16**

*Articulación entre las dimensiones metodológicas de la consolidación experimental*

| **Dimensión metodológica** | **Aporte principal** | **Decisión consolidada** |
| --- | --- | --- |
| Entorno experimental | Define CPN, EN, TN, escenarios DBE y EBE, y restricciones de hardware y software. | Ubica la viabilidad operativa en el CPN, separa entrenamiento de inferencia y formaliza el rol metodológico de cada escenario. |
| Condiciones de riesgo y prompts | Organiza las condiciones de riesgo por niveles de complejidad y fija el protocolo de prompts. | Delimita el núcleo obligatorio del prototipo en condiciones de detección directa de Nivel 1 y ordena el resto del catálogo como extensión condicionada. |
| Datasets y benchmarks | Elabora un inventario de datasets, benchmarks, cobertura por condición y reglas de partición. | Determina qué condiciones tienen soporte suficiente para evaluación directa, qué módulos requieren benchmarks externos y qué brechas exigen prudencia metodológica. |
| Framework de métricas | Jerarquiza métricas, define latencia de alerta, fija niveles de compromiso y establece criterios de ejecutabilidad experimental. | Establece la evidencia mínima del prototipo y separa métricas obligatorias, deseables y conceptuales según el alcance implementado. |

*Nota.* La tabla resume cómo cada dimensión metodológica aporta una parte del protocolo experimental integrado y qué decisión transversal queda consolidada para la continuidad del proyecto.

#### 17.1.2. Alcance experimental consolidado del prototipo

##### 17.1.2.1. Delimitación del catálogo de condiciones de riesgo

El catálogo retenido comprende seis condiciones de riesgo organizadas en tres niveles de complejidad. La decisión principal es distinguir entre el catálogo metodológico completo y el núcleo obligatorio de validación: CR-01 y CR-02 constituyen el plano mínimo del prototipo, porque son condiciones de detección directa de Nivel 1 derivadas del marco de seguridad laboral y construcción (Decreto N.º 911/1996, 1996; Ley N.º 19.587, 1972).

Esa priorización se justifica porque ambas reúnen observabilidad visual relativa, estrategias de detección directa o indirecta ya definidas, cobertura de datos suficiente y métricas aplicables sin depender de módulos todavía no implementados. CR-03 y CR-04 conservan relevancia, pero dependen de visibilidad fina, ausencia visual y datos complementarios; CR-05 y CR-06 orientan la arquitectura relacional, aunque su evaluación completa requiere persistencia temporal, regiones externas o razonamiento contextual. Esta cautela es consistente con la evidencia sobre dificultades de los modelos OVD ante atributos finos y dominios especializados de construcción (Bianchi et al., 2024; Abdalwhab et al., 2025).

##### 17.1.2.2. Núcleo obligatorio y extensiones condicionadas

La distinción entre núcleo obligatorio y extensión condicionada no elimina condiciones del catálogo. Explicita el nivel de compromiso que esta instancia puede sostener con los datos, la instrumentación y la complejidad disponible. En consecuencia, la aceptación mínima del prototipo no depende de un desempeño uniforme sobre las seis condiciones, sino de demostrar funcionamiento defendible sobre el núcleo obligatorio y de producir evidencia parcial o exploratoria sobre las extensiones condicionadas cuando la arquitectura y los datos lo permitan.

El catálogo completo conserva valor directivo, pero la validación se concentra en aquello que puede medirse con rigor. Esta decisión permite preservar la coherencia entre objetivo experimental, cobertura de datos, complejidad técnica y capacidad real de instrumentación.

**Tabla 17**

*Catálogo consolidado de condiciones de riesgo y rol experimental*

| **Código y condición** | **Nivel** | **Evidencia visual dominante** | **Módulos requeridos** | **Rol metodológico** |
| --- | --- | --- | --- | --- |
| CR-01 - Persona sin casco | 1 | Presencia o ausencia de casco en región cefálica. | OVD cuadro a cuadro; estrategia directa o indirecta. | Núcleo obligatorio del prototipo experimental; condición prioritaria para comparación y aceptación. |
| CR-02 - Persona sin chaleco reflectivo | 1 | Presencia o ausencia de prenda de alta visibilidad en torso. | OVD cuadro a cuadro; estrategia directa o indirecta. | Núcleo obligatorio del prototipo experimental; condición prioritaria para comparación y aceptación. |
| CR-03 - Persona en posición elevada sin sistema anticaídas visible | 2 | Persona sobre estructura elevada y ausencia visible de arnés o línea de vida. | OVD + reglas espaciales intracuadro. | Condición exploratoria y condicionada a datos complementarios y visibilidad suficiente. |
| CR-04 - Borde elevado desprotegido con personas próximas | 2 | Borde sin protección colectiva y proximidad humana. | OVD + reglas espaciales intracuadro. | Condición exploratoria y condicionada; no bloquea la aceptación del núcleo del prototipo. |
| CR-05 - Maquinaria en operación cerca de peatones | 3 | Co-ocurrencia de maquinaria y personas bajo distancia de seguridad. | OVD + MOT + razonamiento contextual. | Extensión condicionada a módulo relacional y datos contextuales adecuados. |
| CR-06 - Persona dentro de zona restringida | 3 | Persona dentro de un área previamente parametrizada como restringida. | OVD + MOT + región de interés fija. | Extensión condicionada; requiere cámara fija o parametrización espacial externa al prompt. |

*Nota.* La distinción entre núcleo obligatorio y extensión condicionada no elimina condiciones del catálogo. Explicita el nivel de compromiso que esta instancia puede sostener con los datos, la instrumentación y la complejidad disponible.

#### 17.1.3. Diseño metodológico general y lógica de escenarios

##### 17.1.3.1. Patrón de riesgo como unidad de análisis

El protocolo adopta como unidad de análisis el patrón de riesgo confirmado y no la detección aislada. Esta decisión evita reducir el problema a la mera producción de cajas por cuadro. En el proyecto, la condición de riesgo constituye la unidad semántica de entrada; el patrón de riesgo incorpora severidad, persistencia y, cuando corresponde, relaciones espaciales o temporales; y la alerta constituye la salida operativa trazable del sistema. Esta distinción ordena la relación entre detector, tracker, lógica contextual y backend de eventos.

##### 17.1.3.2. Cadena operativa mínima y motor de patrones

A partir de esa unidad de análisis, el protocolo asume una cadena operativa mínima entre percepción, evaluación y respuesta asistiva. En dicha cadena, las detecciones producidas por el modelo OVD funcionan como evidencia primaria, pero no constituyen por sí mismas una alerta. Para que una alerta sea considerada válida dentro del sistema, la evidencia debe ser agrupada, evaluada y confirmada como patrón de riesgo según los criterios definidos para cada condición.

En términos operativos, esta evaluación corresponde al motor de patrones, entendido en esta instancia como una abstracción lógica del plano de control. Este componente recibe eventos de detección normalizados, información de seguimiento cuando exista, configuración de prompts y reglas de patrón; aplica criterios de persistencia, severidad, histéresis y lógica espacial o contextual; y emite cambios de estado del patrón. Sólo cuando un patrón alcanza el estado confirmado puede registrarse una alerta interna dentro del sistema.

De manera sintética, el flujo operativo se organiza como detección OVD, publicación de evento de detección, evaluación por el motor de patrones, confirmación del patrón, registro de alerta, disponibilidad de la alerta para consulta o notificación, e interpretación por parte del supervisor humano. Esta secuencia permite vincular la medición experimental con una lógica de ejecución trazable, sin atribuir al sistema una capacidad autónoma de decisión sobre el cumplimiento normativo o la gestión efectiva de la obra.

##### 17.1.3.3. Escenarios de evaluación

Sobre esa base, la evaluación se organiza en dos escenarios complementarios. El Escenario A, o Dataset-Based Evaluation (DBE), funciona como ámbito primario de comparación controlada, repetible y cuantificable. El Escenario B, o Environment-Based Evaluation (EBE), añade una validación de plausibilidad operativa sobre captura continua en entorno simulado o controlado. La relación entre ambos no es de reemplazo: el DBE aporta comparabilidad metodológica, mientras que el EBE permite observar el comportamiento integrado del pipeline en condiciones más próximas al uso previsto.

La secuencia de pruebas se estructura de manera progresiva. Parte de una condición base controlada, continúa con barridos univariados o de baja combinación sobre la configuración retenida y culmina con una prueba de mayor exigencia aplicada a la mejor configuración disponible. Este esquema permite acotar la complejidad experimental, evitar un diseño factorial inmanejable y, al mismo tiempo, conservar capacidad analítica para observar la sensibilidad del sistema frente a variables relevantes.

##### 17.1.3.4. Decisiones estructurales del diseño metodológico

**Tabla 18**

*Decisiones estructurales del diseño metodológico*

| **Decisión** | **Formulación adoptada** | **Implicación para el protocolo** |
| --- | --- | --- |
| Unidad de análisis | Patrón de riesgo confirmado y alerta asociada, no detección aislada. | Obliga a medir persistencia, tiempo de respuesta y estabilidad además de precisión de detección. |
| Cadena operativa mínima | Detección OVD, evento de detección, evaluación de patrón, patrón confirmado, alerta registrada, disponibilidad para consulta o notificación, e interpretación humana. | Conecta la evidencia perceptiva con una salida operativa trazable y evita tratar la alerta como una detección aislada. |
| Motor de patrones | Abstracción lógica del plano de control que evalúa eventos de detección, trayectorias cuando existan y configuración de patrones contra reglas de persistencia, severidad, histéresis y lógica espacial o contextual. | Define dónde se transforma la evidencia perceptiva en patrón candidato, confirmado o resuelto, y evita tratar la alerta como salida directa del detector OVD. |
| Carácter asistivo de la alerta | La alerta informa un patrón de riesgo confirmado según los criterios operativos del prototipo, pero no sustituye la decisión del supervisor humano. | Preserva el alcance experimental, ético y operativo del prototipo. |
| Escenario primario | DBE sobre datasets y benchmarks retenidos. | Asegura comparabilidad, control de variables y repetibilidad de las mediciones. |
| Escenario complementario | EBE en entorno simulado o controlado. | Permite observar el comportamiento del pipeline sobre captura continua y variables visuales realistas. |
| Baseline obligatoria | Toda variante se mide primero en zero-shot. | Protege la comparación entre modelos y evita atribuir al ajuste mejoras que dependen de cambios de evaluación. |
| Comparación entre variantes | Fine-tuning sólo cuando existe soporte metodológico suficiente. | Evita convertir la adaptación al dominio en supuesto previo de viabilidad. |

*Nota.* DBE = Dataset-Based Evaluation. EBE = Environment-Based Evaluation. La baseline zero-shot constituye la referencia mínima a partir de la cual recién puede discutirse el valor de prompts, seguimiento o fine-tuning. La cadena operativa mínima fija el recorrido lógico de la alerta dentro del protocolo experimental. El motor de patrones explicita el componente lógico que transforma evidencia perceptiva en patrón confirmado y opera como criterio de diseño para su instrumentación arquitectónica posterior.

#### 17.1.4. Entorno experimental, infraestructura y escenarios de evaluación

##### 17.1.4.1. Introducción y alcance

La presente sección documenta el entorno experimental sobre el cual se desarrolla y evalúa la plataforma E-OVRT-VDP. Su función es caracterizar de manera integrada la infraestructura de cómputo disponible para inferencia y entrenamiento, el stack probable de software asociado, los escenarios de evaluación definidos para el proyecto y las condiciones operativas propias de cada escenario. La información aquí formalizada responde a la pregunta rectora P-E1-04 definida en la fundamentación teórica, que indaga por las restricciones del entorno de ejecución —capacidad computacional, protocolos de transmisión y presupuesto de procesamiento— que condicionan las decisiones arquitectónicas del prototipo. Asimismo, la definición de los escenarios de evaluación establece las condiciones concretas bajo las cuales se ejercitará el prototipo y delimita el referente experimental de la presente sección.

##### 17.1.4.2. Infraestructura de evaluación

La infraestructura de evaluación se organiza a partir de nodos funcionales. En este trabajo, un nodo representa un rol dentro del entorno experimental: procesamiento central, captura en borde o entrenamiento/adaptación de modelos. Cada rol puede materializarse mediante uno o más dispositivos concretos según la disponibilidad, el escenario de evaluación y la configuración efectiva de la corrida.

Bajo este criterio, el Central Processing Node (CPN) concentra la ejecución del pipeline principal, la inferencia, la evaluación de patrones, la medición de latencia y la consolidación de resultados experimentales. El Edge Node (EN) se ubica próximo a la fuente visual y se orienta a captura, transmisión de video y eventual preprocesamiento liviano. El Training Node (TN), cuando corresponda, se reserva para tareas de ajuste o preparación de variantes de modelo, sin sustituir la evaluación operativa sobre el CPN.

###### 17.1.4.2.1. Central Processing Node (CPN)

El CPN concentra la lectura o recepción de cuadros, la inferencia open-vocabulary, el postproceso, la evaluación de patrones, el registro de alertas internas y la instrumentación técnica y operativa.

Este rol se materializa sobre una laptop HP Victus 15 Gaming 15-FB2024LA con GPU NVIDIA GeForce RTX 4060 Laptop y 8 GB de VRAM, recurso que delimita el tamaño de modelo, la resolución de inferencia, la precisión numérica y el presupuesto de latencia. El entorno de ejecución adoptado es Linux mediante WSL2 sobre el equipo descrito y contenedores Linux, por compatibilidad con el stack de inferencia y el bus de datos (HP Inc., s. f.).

Las especificaciones completas del CPN y del entorno de software se presentan en las Tablas B.1 y B.3 del Anexo B.

###### 17.1.4.2.2. Implicancias del NVDEC para el pipeline de medios

La decodificación acelerada mediante NVDEC se conserva como alternativa del protocolo para flujos H.264 o H.265 del EBE. Su eventual uso debe declararse por corrida y contrastarse con la decodificación por software, porque modifica el reparto de carga entre CPU y GPU y, por lo tanto, la interpretación del presupuesto temporal (NVIDIA Corporation, s. f.-b).

###### 17.1.4.2.3. Edge Node (EN) y dispositivo de captura candidato

El EN cumple la función de captura, recepción o transmisión de video hacia el CPN, según la topología definida para cada corrida. Dentro del núcleo experimental, su responsabilidad se limita a captura, transmisión y, eventualmente, preprocesamiento liviano. La inferencia open-vocabulary en borde no forma parte del flujo base; su eventual incorporación corresponde a una variante condicionada, sujeta a medición independiente.

El protocolo contempla dos fuentes integrables para este rol: una cámara IP mediante RTSP y la cámara Luxonis OAK-D Pro PoE mediante su interfaz de captura. La vía RTSP se prioriza inicialmente por disponibilidad e interoperabilidad; la OAK-D se incorpora como fuente posterior para capturas controladas y capacidades sensoriales complementarias. Ninguna de las dos decisiones presupone inferencia OVD en el borde (Luxonis, s. f.-a, s. f.-b).

Ambas fuentes deben producir unidades visuales comparables para el CPN y registrar su procedencia, resolución, tasa de captura y temporalidad. La elección entre ellas depende del escenario y no altera la unidad de evaluación del protocolo.

Las especificaciones del dispositivo de captura y su conectividad se detallan en la Tabla B.2 del Anexo B.

###### 17.1.4.2.4. Criterio de prioridad y fuente RTSP sintética

La fuente RTSP sintética, generada a partir de material pregrabado mediante un servidor de medios, se reserva para desarrollo, pruebas de integración y reproducción controlada de una misma entrada por las rutas DBE y EBE. No constituye una fuente experimental independiente ni sustituye la captura del entorno físico.

###### 17.1.4.2.5. Stack de software de inferencia (CPN)

El stack del CPN debe ser compatible con los frameworks oficiales de Grounding DINO y YOLOE, con aceleración sobre GPU NVIDIA y con rutas reproducibles de inferencia. Las librerías, versiones y runtimes candidatos se documentan en la Tabla B.3 del Anexo B (Liu et al., 2023; Wang et al., 2025).

##### 17.1.4.3. Adaptación de modelos al dominio

Los modelos OVD candidatos se evalúan tanto en su variante preentrenada (baseline zero-shot) como en una variante ajustada mediante fine-tuning supervisado sobre datos del dominio de construcción o similar. El fine-tuning es un proceso preparatorio previo a la ejecución de los escenarios de evaluación; los pesos resultantes se transfieren al CPN para su evaluación bajo las mismas condiciones de hardware, garantizando una comparación justa.

La incorporación del fine-tuning como experimento comparativo responde a la pregunta rectora P-E1-08. El alcance del prototipo experimental excluye el entrenamiento desde cero; el fine-tuning supervisado sobre un subconjunto acotado de datos del dominio es una forma de adaptación compatible con esta restricción.

###### 17.1.4.3.1. Training Node (TN)

El TN se materializa mediante el clúster institucional Mendieta del CCAD-UNC, reservado para preparación y ajuste de variantes. Su capacidad no sustituye la evaluación operativa sobre el CPN; las especificaciones del recurso se presentan en la Tabla B.4 del Anexo B (Centro de Computación de Alto Desempeño, 2026).

###### 17.1.4.3.2. Stack de software de entrenamiento (TN)

El entorno del TN debe permitir preparación de datos, entrenamiento reproducible, conservación de checkpoints y exportación hacia el runtime del CPN. La configuración candidata se resume en la Tabla B.5 del Anexo B.

###### 17.1.4.3.3. Flujo de transferencia y evaluación

El TN queda fuera del camino de inferencia evaluado. Prepara variantes sobre particiones previamente definidas, exporta los checkpoints en un formato compatible y entrega esos artefactos al CPN, donde deben compararse con la baseline bajo el mismo material y la misma configuración experimental, salvo la variable aislada.

##### 17.1.4.4. Escenarios de evaluación

Se definen dos escenarios de evaluación complementarios. El primero permite la evaluación controlada y reproducible del pipeline mediante datasets de referencia públicos; el segundo expone el sistema a condiciones visuales representativas del dominio real mediante video en tiempo real captado en un entorno físico. Ambos escenarios son necesarios dado que el primero habilita la comparación cuantitativa entre variantes de modelo y, cuando el dataset y el protocolo lo permitan, el contraste con métricas reportadas en la literatura, mientras que el segundo valida la viabilidad operativa bajo condiciones que ningún dataset puede replicar completamente. En ambos escenarios, la evaluación contempla la ejecución tanto de modelos preentrenados (baseline) como de modelos ajustados mediante fine-tuning en el TN (Sección 17.1.9), permitiendo una comparación directa del impacto de la adaptación al dominio.

###### 17.1.4.4.1. Escenario A - Dataset-Based Evaluation (DBE)

En este escenario el pipeline procesa material de imagen o video proveniente de datasets públicos de referencia. La ausencia de condiciones en tiempo real permite reproducibilidad exacta, aislamiento de variables y, cuando el dataset y el protocolo de evaluación coincidan con los de la fuente de referencia, contraste con métricas reportadas en la literatura. Constituye el escenario primario para la evaluación cuantitativa de los componentes OVD y MOT del pipeline, tanto en su variante preentrenada como en la variante ajustada por fine-tuning. Los datasets candidatos se documentan en la estrategia de datos, benchmarks y partición.

**Tabla 19**

*Características del Escenario A - Dataset-Based Evaluation (DBE)*

| **Aspecto** | **Descripción** |
| --- | --- |
| Tipo de entrada | Imágenes y secuencias de video provenientes de datasets anotados |
| Fuente | Colección de datasets candidatos (la estrategia de datos, benchmarks y partición) |
| Nodo de ejecución | CPN para toda la inferencia y evaluación |
| Modelos evaluados | Variante preentrenada (baseline) y variante fine-tuned, cuando aplique, para los modelos candidatos seleccionados |
| Conectividad | No aplica; procesamiento off-line sobre archivos locales |
| Ventaja principal | Reproducibilidad exacta; comparación directa con benchmarks de la literatura; aislamiento del efecto del fine-tuning |
| Limitación principal | Existen datasets públicos de construcción civil para detección, pero no benchmarks del dominio con seguimiento anotado; la evaluación MOT requiere benchmarks generales complementarios y un protocolo propio de transferencia al dominio. |

###### 17.1.4.4.2. Escenario B - Environment-Based Evaluation (EBE)

En este escenario el pipeline opera sobre video en tiempo real captado en un espacio de obra simulado. Este escenario valida la viabilidad operativa del sistema bajo condiciones visuales y de conectividad representativas del dominio real, incluyendo variaciones de iluminación, oclusiones y densidad de personas en escena. A diferencia del Escenario A, el pipeline se ejercita de extremo a extremo, incluyendo las etapas de captura y transporte de video, y permite evaluar el comportamiento del motor de razonamiento temporal bajo condiciones de operación continua. Al igual que en el Escenario A, se ejecutan las variantes preentrenada y fine-tuned de cada modelo candidato seleccionado tras la evaluación del Escenario A.

**Tabla 20**

*Características del Escenario B - Environment-Based Evaluation (EBE)*

| **Aspecto** | **Descripción** |
| --- | --- |
| Tipo de entrada | Video en vivo desde el EN mediante cámara IP por RTSP o captura directa con OAK-D Pro PoE. La fuente RTSP sintética se reserva para desarrollo y reproducibilidad. |
| Espacio físico | Espacio de obra simulado. |
| Participantes | Personas reales portando EPP (casco, chaleco reflectante, entre otros); configuración de escenas con y sin infracción deliberada. |
| Condiciones visuales | Variables según la configuración de prueba prevista para la validación experimental, definidas en función del diseño experimental del escenario y de las condiciones operativas que se establezcan para su evaluación. |
| Nodo de ejecución | CPN para inferencia central; EN para captura y, sólo como variante condicionada, preprocesamiento liviano. |
| Modelos evaluados | Variante preentrenada (baseline) y variante fine-tuned, sobre el modelo o combinación seleccionada tras el Escenario A. |
| Conectividad | Red LAN. |
| Ventaja principal | Validación operativa bajo condiciones del dominio; ejercita el pipeline completo de extremo a extremo incluyendo transporte de video y motor de razonamiento temporal. |
| Limitación principal | Menor reproducibilidad que el Escenario A; requiere gestión de consentimiento libre, expreso e informado e información previa a los participantes, conforme al régimen de protección de datos personales y videovigilancia aplicable (Argentina, 2000; Disposición 10/2015, 2015). |

##### 17.1.4.5. Parámetros operativos de referencia

Los parámetros operativos de referencia establecen una base inicial para orientar la evaluación del pipeline experimental. No constituyen valores definitivos de configuración, sino condiciones de partida que permiten delimitar resolución, tasa de cuadros, modalidad de transporte, procesamiento esperado y restricciones generales de ejecución. Su función es ofrecer un marco común para comparar pruebas posteriores y evitar que cada experimento se defina de manera aislada.

###### 17.1.4.5.1. Parámetros de referencia del pipeline

Los parámetros operativos se documentan por perfil. En particular, la resolución de inferencia es un parámetro del perfil de modelo y debe fijarse junto con los umbrales recalibrados para ese perfil; no se adopta una resolución única para todas las familias. Los restantes valores orientativos se presentan en la Tabla B.6 del Anexo B.

###### 17.1.4.5.2. Transporte de video en el escenario B

En el EBE, la captura y el procesamiento pueden ubicarse en nodos distintos. El protocolo exige declarar fuente, transporte, buffering y anclas temporales para distinguir la latencia de adquisición de la latencia algorítmica. La topología de referencia se presenta en la Tabla B.7 del Anexo B.

##### 17.1.4.6. Restricciones y condicionantes del entorno experimental

Las restricciones detalladas en la Tabla 21 condicionan las decisiones de diseño de etapas posteriores y deben tenerse presentes al interpretar los resultados experimentales.

**Tabla 21**

*Restricciones y condicionantes del entorno experimental*

| **Restricción** | **Origen** | **Implicación para el diseño** |
| --- | --- | --- |
| VRAM de 8 GB en el CPN | Hardware — RTX 4060 Laptop (8 GB VRAM) | Limita el tamaño de los modelos ejecutables sin cuantización y condiciona la resolución de entrada, el batch efectivo y la elección de runtime en inferencia. |
| Capacidad de inferencia del EN limitada a 1.4 TOPS para AI | Hardware — OAK-D Pro PoE / RVC2 | Restringe la complejidad de los modelos que pueden ejecutarse localmente; el uso del EN debe considerarse, en principio, para captura inteligente, preprocesamiento o inferencia ligera en borde. |
| Linux mediante WSL2 y contenedores Linux en el CPN | Entorno de ejecución — CPN | Las versiones de CUDA, bibliotecas, runtimes y bus deben ser compatibles con el entorno Linux adoptado y quedar congeladas por corrida. |
| Cobertura limitada del dominio para evaluación de seguimiento | Datasets públicos analizados en la estrategia de datos, benchmarks y partición | La evaluación MOT requiere benchmarks generales complementarios y la formalización de un protocolo de transferencia al dominio, dado que la cobertura específica del dominio para seguimiento anotado es insuficiente. |
| Presupuesto de latencia G2A de 50–250 ms | el framework de métricas | Condiciona la selección de modelos, la resolución de entrada y la configuración de runtimes. |
| Acceso al clúster sujeto a disponibilidad institucional del recurso | Infraestructura institucional — CCAD-UNC | La planificación del ajuste debe contemplar la cola institucional, sin convertir la disponibilidad de cómputo en criterio metodológico de aceptación o descarte. |
| Necesidad de split train/eval disjunto | Principio metodológico | Los datos utilizados para fine-tuning no pueden formar parte del conjunto de evaluación. La partición debe documentarse explícitamente. |
| Recaudos ético-legales en el Escenario B | Ley N.º 25.326 y Disposición 10/2015 | Las pruebas con personas en el campo visual requieren consentimiento informado e información previa. El carácter académico y controlado del prototipo atenúa el perfil de riesgo, pero no elimina las obligaciones de resguardo y minimización. |

*Nota.* Elaboración propia basada en las especificaciones del hardware disponible, la caracterización del TN y del EN en la presente sección, los criterios metodológicos fijados en la estrategia de datos, benchmarks y partición y el marco normativo argentino aplicable a protección de datos personales y videovigilancia.

##### 17.1.4.7. Lectura metodológica de la infraestructura operativa y sus restricciones

La infraestructura del proyecto se organiza en tres nodos con roles diferenciados. El Central Processing Node (CPN) es la plataforma donde debe probarse la viabilidad operativa. El Training Node (TN), correspondiente al clúster institucional Mendieta, cumple una función acotada de entrenamiento o exportación de variantes ajustadas. El Edge Node (EN) aporta captura continua para el EBE y, sólo si la arquitectura lo justifica, preprocesamiento o inferencia ligera.

La consecuencia metodológica es que las conclusiones sobre tiempo real, latencia, uso de recursos y sostenibilidad del pipeline deben anclarse en el CPN: una HP Victus 15 con RTX 4060 Laptop de 8 GB de VRAM y entorno Linux mediante WSL2 y contenedores Linux. Esta restricción orienta la selección de modelos, la resolución, la composición del vocabulario y el runtime de inferencia.

**Tabla 22**

*Infraestructura experimental y función metodológica de cada nodo*

| **Nodo** | **Configuración relevante** | **Función metodológica** | **Lectura correcta dentro del protocolo** |
| --- | --- | --- | --- |
| CPN | HP Victus 15; RTX 4060 Laptop de 8 GB; 32 GB de RAM; Linux mediante WSL2 y contenedores Linux. | Inferencia, evaluación del pipeline y medición de recursos y latencia. | Es el punto donde debe defenderse la viabilidad operativa del prototipo experimental. |
| TN | Clúster Mendieta; nodos con 2 × NVIDIA A30; Linux institucional. | Entrenamiento supervisado o exportación de variantes ajustadas, si aplica. | No sustituye la prueba operativa sobre el CPN ni redefine el presupuesto real del sistema. |
| EN | Fuentes integrables para el EBE: cámara IP por RTSP y OAK-D Pro PoE. | Suministro de video continuo y eventual preprocesamiento o inferencia ligera. | Su función base es captura y transmisión; la inferencia liviana en borde requiere una evaluación independiente. |

*Nota.* La separación entre CPN, TN y EN no es organizativa sino metodológica: define dónde se entrena, dónde se ejecuta y dónde debe interpretarse la capacidad real del prototipo.

El entorno impone restricciones explícitas. La VRAM de 8 GB limita el tamaño de los modelos y el margen para lotes o vocabularios extensos; la capacidad del EN no permite suponer inferencia OVD principal sin simplificaciones; y la combinación de Linux mediante WSL2, CUDA, contenedores y runtimes acelerados introduce dependencias que deben quedar registradas en la bitácora experimental.

#### 17.1.5. Condiciones de riesgo, patrones y protocolo de prompts

##### 17.1.5.1. Introducción y alcance

La fundamentación teórica del proyecto E-OVRT-VDP dejó abierta una brecha metodológica entre la identificación normativa de condiciones de riesgo relevantes para seguridad laboral y su traducción en consultas textuales evaluables por modelos de detección open-vocabulary. Junto con esa brecha, el análisis previo señaló que la formulación del prompt no constituye un detalle accesorio, sino una variable que puede alterar de manera significativa el desempeño del detector en dominios especializados.

En ese marco, la presente sección responde a la pregunta rectora P-E1-02 definida en la fundamentación teórica. Define la taxonomía de condiciones de riesgo que integran el alcance del prototipo experimental, establece los patrones de riesgo asociados con severidad y persistencia orientativa, y fija un protocolo sistemático para el diseño y la evaluación de prompts OVD. En articulación con el framework de métricas, la sección delimita además cómo esas definiciones conceptuales deben leerse respecto de la latencia de alerta, las métricas operativas y los criterios de aplicación del framework evaluativo.

El alcance de la sección es metodológico. Establece qué condiciones deben detectarse, cómo se agrupan en patrones de riesgo, con qué severidad conceptual y criterios analíticos de persistencia se interpretan, y con qué formulaciones textuales se evaluarán. Además, incorpora una operacionalización preliminar del motor de patrones como componente lógico responsable de transformar detecciones y trayectorias en patrones candidatos, confirmados o resueltos. Esta definición no constituye todavía una implementación de software ni fija contratos técnicos finales, pero sí delimita la estructura mínima de ejecución que deberá materializarse en la instancia de análisis y diseño arquitectónico. Los umbrales cuantitativos finales de aceptación y la calibración empírica de ventanas, reglas e histéresis corresponden al framework de métricas y a la validación experimental.

##### 17.1.5.2. Taxonomía de condiciones de riesgo para el prototipo

El primer paso consiste en delimitar el subconjunto de condiciones de riesgo que el prototipo experimental debe ser capaz de detectar. Para ello se explicitan los criterios de selección aplicados sobre el universo relevado en la fundamentación teórica, se presenta la clasificación en tres niveles de complejidad según las capacidades del sistema requeridas para su evaluación y, finalmente, se consolida el catálogo de condiciones seleccionadas junto con sus consideraciones de evaluabilidad. El resultado constituye el insumo directo tanto para la definición de patrones de riesgo como para el diseño de prompts OVD.

###### 17.1.5.2.1. Criterios de selección del subconjunto del prototipo experimental

El universo de condiciones de riesgo identificado en el análisis normativo de la fundamentación teórica abarca categorías como uso de EPP (casco, chaleco, calzado), protección contra caídas en altura, delimitación de áreas de riesgo, control de circulación con maquinaria, orden y limpieza e instalaciones eléctricas provisorias. El prototipo experimental no pretende cubrir la totalidad de ese espacio, sino seleccionar un subconjunto acotado que permita demostrar la viabilidad técnica del concepto. Con ese fin se aplican tres criterios de selección, calibrados a las restricciones reales de recursos y al contexto académico del proyecto.

**Representatividad de niveles de complejidad**. El subconjunto debe incluir al menos una condición de cada nivel de complejidad definido en la clasificación de la sección 17.1.5.2.2, de modo que la evaluación ejercite las capacidades del pipeline en sus distintas configuraciones. Este criterio es viable porque los niveles corresponden a capacidades del sistema que deben evaluarse independientemente de la cantidad de condiciones seleccionadas.

**Factibilidad de detección visual**. Las condiciones seleccionadas deben tener correlatos visuales suficientemente diferenciados como para ser evaluables mediante análisis de imagen en las resoluciones y ángulos de cámara típicos de un entorno de laboratorio o simulado. Esto excluye condiciones cuya manifestación visual depende de detalles de difícil resolución (por ejemplo, la distinción entre calzado de seguridad y calzado común), así como condiciones sin correlato visual directo (por ejemplo, “capacitación insuficiente” o “plan de seguridad no elaborado”). La exclusión deliberada de condiciones de baja observabilidad evita comprometer la validez de los resultados experimentales del prototipo con limitaciones ajenas al sistema. La pertinencia de este criterio se ve reforzada por evidencia empírica reciente que muestra, por un lado, que los modelos OVD preentrenados pueden presentar limitaciones importantes para discriminar detalles finos y atributos visuales sutiles (Bianchi et al., 2024) y, por otro, que en tareas de dominio especializado en construcción su desempeño puede caer marcadamente frente a detectores ajustados al dominio (Abdalwhab et al., 2025).

**Viabilidad de evaluación con recursos disponibles**. Las condiciones seleccionadas deben poder evaluarse con alguna combinación de datasets públicos existentes, subconjuntos anotados de los mismos o datos generados en entorno controlado, sin exigir campañas extensivas de recolección o anotación incompatibles con un proyecto académico. Este criterio no presupone cobertura perfecta desde el inicio, pero sí exige que la brecha entre lo disponible y lo necesario sea acotada y metodológicamente manejable.

###### 17.1.5.2.2. Clasificación por niveles de complejidad

La clasificación de las condiciones de riesgo en tres niveles de complejidad responde a una distinción funcional sobre las capacidades que el sistema debe desplegar para evaluarlas. Esta tipología tiene consecuencias directas tanto sobre la arquitectura del pipeline como sobre el protocolo de evaluación aplicable a cada condición.

**Condiciones de Nivel 1: Entidad simple.** Involucran la detección de un único objeto o atributo sobre una entidad. Su evaluación es resoluble, en principio, mediante una única consulta OVD sobre un cuadro individual, sin requerir información temporal ni relacional. Un ejemplo representativo es la detección de casco de seguridad sobre una persona, donde el modelo OVD recibe un prompt como “person with hard hat” o “hard hat” y debe localizar las instancias correspondientes en la imagen. La evaluación de la condición de riesgo asociada (presencia o ausencia del EPP) admite dos estrategias diferenciadas que se analizan en la Sección 17.1.5.4.

**Condiciones de Nivel 2: Entidad con atributo contextual.** Estas involucran entidades sobre las cuales debe verificarse un atributo que depende de información espacial dentro del mismo cuadro. A diferencia del Nivel 1, la condición no se reduce a la detección aislada de un objeto, sino que requiere evaluar la relación espacial entre la entidad y su contexto visual inmediato. Un ejemplo es la presencia de una persona sobre una estructura elevada (andamio, plataforma), donde el modelo OVD puede detectar individualmente a la persona y a la estructura, pero la determinación de que la persona se encuentra sobre la estructura requiere un análisis de las relaciones geométricas entre las detecciones, como la superposición vertical de bounding boxes. Este análisis puede implementarse mediante lógica de post-detección que opere sobre las salidas del modelo en el mismo cuadro, por ejemplo a través de reglas geométricas de solapamiento, proximidad o posicionamiento relativo entre regiones detectadas. A diferencia del Nivel 3, este tipo de condición no exige aún persistencia temporal ni mantenimiento de identidad entre cuadros, pero sí introduce una capa adicional de razonamiento espacial intracuadro. En consecuencia, las condiciones de Nivel 2 representan un escalón intermedio de complejidad, en el que la evaluabilidad depende tanto de la calidad de la detección de entidades como de la solidez de las reglas espaciales definidas para interpretar su relación contextual.

**Condiciones de Nivel 3: Relación entre entidades.** Por último, estas condiciones involucran dos o más entidades independientes cuya co-ocurrencia espacial o temporal constituye la condición de riesgo. Estas condiciones exceden la capacidad del detector OVD operando cuadro a cuadro, ya que requieren tanto la detección individual de cada entidad como un módulo de razonamiento que evalúe relaciones geométricas entre ellas (distancia, contención) y las estabilice temporalmente. El tracker MOT interviene en este nivel para preservar la identidad de cada objeto rastreado a lo largo de los cuadros consecutivos que abarca el intervalo de evaluación. Un ejemplo es la co-ocurrencia de maquinaria pesada y peatones por debajo de una distancia de seguridad, donde ambas entidades son detectables individualmente por el OVD, pero la evaluación de proximidad peligrosa requiere calcular distancias entre detecciones y sostener esa evaluación durante un intervalo temporal.

###### 17.1.5.2.3. Catálogo de condiciones de riesgo seleccionadas

La Tabla 23 presenta las seis condiciones de riesgo seleccionadas para el prototipo experimental, organizadas por nivel de complejidad. Para cada condición se indica su código identificador, la categoría normativa de origen, la descripción operativa, el componente del sistema responsable de su evaluación y una estimación cualitativa de la dificultad de detección OVD.

**Tabla 23**

*Catálogo de condiciones de riesgo seleccionadas para el prototipo experimental*

| **Código** | **Nivel** | **Cat. normativa** | **Condición de riesgo** | **Evidencia visual** | **Componente evaluador** | **Dificultad OVD estimada** |
| --- | --- | --- | --- | --- | --- | --- |
| CR-01 | 1 | EPP — casco | Persona sin casco de seguridad en zona de obra | Presencia o ausencia de casco en región cefálica de la persona | OVD cuadro a cuadro | Media |
| CR-02 | 1 | EPP — chaleco | Persona sin chaleco reflectivo en zona de tráfico o maquinaria | Presencia o ausencia de prenda de alta visibilidad en torso | OVD cuadro a cuadro | Media-Baja |
| CR-03 | 2 | Protección contra caídas | Persona en posición elevada sin sistema anticaídas visible | Persona sobre andamio o plataforma sin arnés o línea de vida visible | OVD + contexto espacial intracuadro | Alta |
| CR-04 | 2 | Protección contra caídas | Borde elevado desprotegido con personas próximas | Borde de plataforma o losa sin baranda o red perimetral, con presencia humana | OVD + contexto espacial intracuadro | Alta |
| CR-05 | 3 | Coexistencia peatón-maquinaria | Maquinaria en operación en proximidad a peatones sin separación | Co-ocurrencia de maquinaria pesada y personas por debajo de distancia de seguridad | OVD + MOT + razonamiento contextual | Media |
| CR-06 | 3 | Delimitación de áreas | Persona dentro de zona restringida o delimitada | Presencia de persona en área demarcada como prohibida o restringida | OVD + MOT + razonamiento contextual | Media |

*Nota.* La columna “Componente evaluador” indica qué módulos del sistema participan en la evaluación de cada condición. “OVD cuadro a cuadro” significa que la condición es resoluble con una o más consultas al detector por cuadro. “OVD + contexto espacial intracuadro” indica que se requiere evaluar relaciones geométricas entre detecciones dentro del mismo cuadro (por ejemplo, superposición vertical de bounding boxes entre persona y andamio en CR-03, o proximidad entre persona y borde desprotegido en CR-04). “OVD + MOT + razonamiento contextual” indica que la evaluación requiere persistencia temporal de trayectorias y lógica de evaluación relacional cuyo diseño corresponde a la instancia de análisis y diseño arquitectónico. La columna “Dificultad OVD estimada” refleja una valoración cualitativa basada en la degradación documentada de modelos OVD ante atributos de granularidad fina (Bianchi et al., 2024), en las dificultades asociadas a la discrepancia de distribución y vocabulario cuando detectores de gran vocabulario se trasladan a dominios downstream o especializados (Jiang et al., 2024), y en evidencia reciente sobre el menor desempeño de modelos vision-language/open-vocabulary preentrenados frente a detectores ajustados al dominio en entornos de construcción (Abdalwhab et al., 2025). De manera únicamente conceptual, se considera además la asimetría entre juicios de presencia y ausencia observada en la percepción visual humana, invocada aquí como analogía metodológica y no como propiedad demostrada de los detectores OVD (Mazor et al., 2021). No se pondera en esta columna la dificultad propia del razonamiento contextual.

###### 17.1.5.2.4. Consideraciones sobre evaluabilidad y limitaciones

La selección prioriza condiciones con alta observabilidad visual y disponibilidad plausible de datos de evaluación. Aun así, presenta particularidades que conviene explicitar.

La condición CR-04 —borde desprotegido— presenta dos particularidades relevantes. La primera concierne a la naturaleza negativa de la evidencia visual de la condición de riesgo. Dado que esta condición se define por la ausencia de un elemento de protección —baranda o red perimetral—, su evaluación resulta conceptualmente más exigente que en condiciones basadas en la presencia explícita de objetos. En este sentido, la literatura sobre percepción visual humana sugiere asimetrías entre juicios de presencia y ausencia, con respuestas más lentas y menor confianza ante ciertos juicios de ausencia; sin embargo, esta evidencia proviene de tareas perceptuales humanas y no de evaluación automática en visión por computadora, por lo que se invoca aquí únicamente como analogía metodológica (Mazor et al., 2021). La segunda particularidad es geométrica: la determinación de si un borde es efectivamente elevado depende de información tridimensional que la proyección bidimensional de la cámara no preserva completamente. Por ello, la ambigüedad asociada a altura, profundidad, perspectiva y oclusión debe asumirse desde el diseño experimental.

La condición CR-03 también exige cautela. La evidencia visual relevante no es solo la presencia de una persona en altura, sino la ausencia visible de un sistema anticaídas, lo que depende fuertemente de la escala del objeto en imagen, el ángulo de cámara, la oclusión y la resolución disponible. En consecuencia, su dificultad no proviene únicamente del razonamiento espacial intracuadro, sino también de la visibilidad efectiva del EPP que debería observarse.

Las condiciones de Nivel 3 —CR-05 y CR-06— no son evaluables mediante prompts integrados de OVD, sino mediante la detección de entidades componentes más razonamiento contextual. En CR-06, además, la evaluabilidad presupone cámaras fijas y una parametrización espacial externa al prompt —por ejemplo, un polígono de zona restringida definido por el operador—. Este supuesto debe quedar explícito desde esta etapa, ya que condiciona tanto el diseño experimental como la futura implementación del módulo de razonamiento contextual.

En un escenario real, múltiples condiciones pueden co-ocurrir sobre la misma persona y el sistema las tratará como unidades de detección ortogonales. Esta decisión simplifica el diseño y la evaluación del prototipo experimental, pero también implica que la correlación entre condiciones no se explota como señal de refuerzo. A ello se suman factores contextuales transversales —resolución, ángulo de cámara, iluminación y oclusión— que deberán documentarse como variables experimentales para interpretar correctamente el desempeño observado.

##### 17.1.5.3. Definición conceptual de patrones de riesgo

Esta sección define conceptualmente los patrones de riesgo que constituyen la unidad operativa de análisis del sistema E-OVRT-VDP. Para ello articula tres componentes: la definición del patrón como abstracción que integra condiciones detectadas con criterios de persistencia y severidad; la delimitación de los niveles de severidad que ordenan la urgencia de respuesta; y los criterios de activación. Todas las definiciones tienen carácter conceptual y analítico; los valores numéricos propuestos son orientativos y quedan sujetos a calibración empírica durante las etapas de implementación y validación.

###### 17.1.5.3.1. El patrón de riesgo como unidad de análisis

En el contexto del proyecto, se define patrón de riesgo como la especificación declarativa de una situación de seguridad relevante que combina una o más condiciones de riesgo detectadas con criterios de persistencia temporal y un nivel de severidad asignado. El patrón opera como unidad de transición entre el plano de medios (que produce detecciones y trayectorias) y el plano de control (que evalúa situaciones y genera alertas). Su función es transformar las detecciones instantáneas —inherentemente ruidosas y variables entre cuadros— en eventos operativamente significativos cuya confirmación justifique la generación de una alerta asistiva.

La distinción entre condición de riesgo y patrón de riesgo es funcional y tiene consecuencias arquitectónicas directas. La condición de riesgo es la unidad semántica que el plano de medios detecta (vía OVD y, cuando corresponde, MOT). El patrón de riesgo es la unidad que el plano de control evalúa, agregando criterios de persistencia temporal, severidad y, en los casos composicionales, lógica de activación combinada. La interfaz entre ambos planos se establece en la publicación de detecciones y trayectorias etiquetadas semánticamente como eventos, según la arquitectura event-driven.

###### 17.1.5.3.2. Niveles de severidad

Cada patrón de riesgo se asocia a un nivel de severidad que refleja el perfil temporal del riesgo, entendido como la velocidad con la que la condición observable puede escalar hacia un incidente y la gravedad potencial de sus consecuencias. En articulación con el framework de métricas, la severidad orienta la urgencia operativa del patrón, las ventanas funcionales de persistencia y los objetivos de TTFD y talert-system; no fija por sí sola el costo computacional del pipeline, que debe distinguirse del tramo Glass-to-Algorithm (G2A).

Se distinguen tres niveles de severidad, cuya granularidad se considera suficiente para el alcance del prototipo experimental. La fundamentación de cada nivel se apoya en la normativa argentina aplicable y en el perfil temporal de consecuencias asociado a cada tipo de exposición.

El **nivel crítico** corresponde a condiciones con potencial de escalada rápida hacia daño grave o fatal. Los artículos 52 a 57 del Decreto 911/96 establecen medidas de prevención frente al riesgo de caída de personas y trabajos con riesgo de caída a distinto nivel, incluyendo protecciones colectivas, provisión de EPP acorde al riesgo y medidas mínimas para tareas de corta duración. Asimismo, para riesgos asociados a la interacción entre personas, vehículos y maquinaria, el Decreto 911/96 regula la operación de vehículos y maquinaria automotriz en los artículos 246 a 249, y prevé medidas de protección frente a la circulación vehicular en contextos específicos, como la señalización, vallado o cercado de áreas de trabajo en vía pública, la provisión de equipos de alta visibilidad y la protección mediante vallados, señales, luces, vigías u otras medidas eficaces. En ambos casos, la exposición observada puede transformarse con rapidez en un incidente severo, lo que justifica asociar estos patrones con ventanas de persistencia más cortas y objetivos más exigentes de TTFD y dentro del framework evaluativo.

El **nivel alto** corresponde a condiciones cuya exposición sostenida incrementa de forma significativa el riesgo, aunque con mayor margen de intervención que en el nivel crítico. El Decreto 911/96 regula en los artículos 98 a 102 la provisión, uso, condiciones y vida útil de los equipos y elementos de protección personal; en los artículos 103 a 106, las características generales de la vestimenta de trabajo; y en el artículo 107, la provisión de casco de seguridad para trabajadores que desarrollen tareas en obras de construcción o dependencias con riesgos específicos de accidentes. La ausencia de casco en zona activa de obra no produce por sí misma el incidente, pero elimina una barrera de protección frente a eventos plausibles durante la operación. En esa misma lógica, la permanencia en una zona restringida implica una exposición acumulativa a peligros específicos del sector delimitado.

El **nivel medio** corresponde a condiciones con riesgo latente o de escalada relativamente más lenta, donde puede exigirse mayor evidencia antes de confirmar la alerta. La obligación de emplear elementos reflectivos o de alta visibilidad en contextos de circulación vehicular se vincula en el Decreto 911/96 con los artículos 63 y 70, referidos respectivamente a trabajos nocturnos y a trabajadores ocupados en la construcción de carreteras en uso. Esta obligación puede complementarse con la Resolución SRT 299/2011, que establece criterios de registración y constancia de entrega de ropa de trabajo y elementos de protección personal. La ausencia de chaleco reflectivo o indumentaria de alta visibilidad reduce la visibilidad del trabajador ante operadores de vehículos o maquinaria, pero la escalada hacia un incidente depende del movimiento efectivo de esos equipos en la zona, lo que justifica ventanas funcionales más largas que en los niveles precedentes.

Si durante la evaluación experimental se identificara la necesidad de niveles adicionales de granularidad, la taxonomía podría extenderse; sin embargo, para el alcance del prototipo experimental, tres niveles proporcionan un balance adecuado entre expresividad y manejabilidad.

###### 17.1.5.3.3. Criterios de persistencia temporal

La persistencia temporal es el mecanismo analítico que define en qué condiciones una detección instantánea se considera un evento confirmado. Su propósito es reducir la tasa de falsas alarmas derivada de la variabilidad inherente a la detección cuadro a cuadro. Como se documentó en el análisis de modelos OVD, el componente OVD introduce variabilidad en los puntajes de confianza y puede producir apariciones espurias entre cuadros consecutivos, por lo que la confirmación temporal constituye una necesidad operativa.

El criterio de persistencia se conceptualiza como una ventana temporal mínima durante la cual la condición debe observarse de manera sostenida —o con una proporción mínima de detecciones positivas dentro de la ventana— antes de que el patrón se considere activo. La presente sección define estos criterios en términos de duración temporal (segundos) y no de número de cuadros, dado que la conversión depende del throughput efectivo del pipeline, que a su vez está condicionado por el hardware de inferencia. Esta parametrización en unidades temporales permite que la instancia de análisis y diseño arquitectónico realice la conversión una vez conocido el tasa de cuadros real del sistema. En congruencia con el framework de métricas, esta ventana expresa y no debe confundirse ni con —subtramo computacional por cuadro— ni con, que integra además la confirmación operativa del patrón.

Los rangos de persistencia propuestos se derivan del análisis cualitativo de la velocidad de escalada de cada tipo de riesgo y se fijan de modo compatible con los umbrales orientativos del framework de métricas. Para las condiciones de severidad crítica, se proponen ventanas de 2 a 4 segundos, buscando confirmar la exposición con mínima acumulación de evidencia sin sacrificar la capacidad de alerta temprana. Para condiciones de severidad alta, se proponen ventanas de 3 a 5 segundos, que ofrecen mayor evidencia acumulada para reducir falsos positivos sin perder capacidad de respuesta ante una exposición sostenida. Para condiciones de severidad media, se proponen ventanas de 5 a 10 segundos, admitiendo mayor acumulación de evidencia para controlar falsas alarmas en una condición cuya urgencia operativa es relativamente menor.

Conviene precisar que estos rangos tienen carácter analítico y orientativo. Los valores definitivos se calibrarán empíricamente durante la validación experimental, una vez que el pipeline completo esté operativo y se conozca el throughput efectivo. La instancia de análisis y diseño arquitectónico tomará estos rangos como referencia para diseñar los mecanismos computacionales de evaluación de persistencia.

Un aspecto adicional que la instancia de análisis y diseño arquitectónico deberá considerar es el comportamiento de histéresis en la activación y desactivación de patrones. En sistemas de alarmas industriales es habitual que el umbral de activación de una alerta difiera del umbral de desactivación, de modo que una interrupción momentánea de la detección —por oclusión parcial, variabilidad del puntaje de confianza o pérdida temporal del track— no desactive prematuramente un patrón recién confirmado. Esta definición queda planteada como criterio de diseño para la etapa arquitectónica.

Existe una tensión inherente entre la severidad del patrón y la confiabilidad de su activación. Algunos patrones críticos requieren ventanas de persistencia más cortas para responder con la urgencia que su perfil de riesgo demanda. Sin embargo, ventanas más cortas implican menos evidencia acumulada, lo que incrementa la probabilidad de falsos positivos. Este trade-off no tiene resolución analítica a priori y constituye uno de los ejes centrales de calibración empírica de la validación experimental, donde deberá evaluarse la curva de tasa de falsos positivos en función de la duración de la ventana de persistencia para cada patrón.

Como valores de protocolo dentro de esos rangos se fijan 4.000 ms de persistencia para la confirmación de PR-01 y 7.000 ms para PR-02, con umbrales de desactivación de 2.000 y 3.000 ms, respectivamente. Los tiempos se expresan en milisegundos para conservar su significado ante distintos ritmos efectivos de cuadro.

###### 17.1.5.3.4. Operacionalización preliminar del motor de patrones

La definición conceptual de patrones de riesgo requiere una traducción operativa mínima que permita explicar cómo una detección aislada puede convertirse, en tiempo de ejecución, en una alerta asistiva trazable. Para ello, se introduce el motor de patrones como abstracción lógica del sistema, responsable de evaluar la evidencia visual producida por el detector y determinar el estado de cada patrón definido.

El motor de patrones no se entiende como un modelo de visión ni como parte del detector OVD. Su función es posterior a la inferencia: recibe detecciones normalizadas, timestamps, configuración de prompts, reglas del patrón y, cuando corresponda, información de seguimiento o de regiones parametrizadas. A partir de esos insumos, aplica criterios de persistencia, severidad, histéresis y relaciones espaciales para decidir si un patrón permanece inactivo, pasa a estado candidato, se confirma o se considera resuelto.

Esta distinción evita tratar una detección puntual como una alerta automática. Una detección indica evidencia visual en un cuadro o instante determinado; un patrón candidato indica que esa evidencia comenzó a sostenerse o a cumplir una condición contextual; un patrón confirmado indica que se alcanzaron los criterios definidos para generar una alerta registrada; y un patrón resuelto indica que la evidencia dejó de sostenerse durante el intervalo de cierre establecido. De este modo, la alerta queda asociada a una evaluación lógica sobre evidencia acumulada y no a una única salida del modelo.

Para los patrones de Nivel 1, como PR-01 y PR-02, la evaluación puede apoyarse en ventanas temporales de evidencia sin requerir obligatoriamente MOT. En ese caso, la persistencia puede estimarse por proporción de cuadros positivos, duración mínima de evidencia o continuidad aproximada de detecciones relevantes. Si se requiere atribuir la condición a una persona individual durante toda la secuencia, será necesario incorporar MOT o un mecanismo equivalente de asociación temporal. Para los patrones de Nivel 2, la evaluación agrega reglas espaciales intracuadro, como proximidad, solapamiento o relación vertical entre entidades. Para los patrones de Nivel 3, la evaluación exige relaciones sostenidas entre entidades o entre una entidad y una zona parametrizada, por lo que el seguimiento temporal adquiere mayor importancia metodológica.

La histéresis forma parte del comportamiento esperado del motor. Un patrón no debería activarse por una detección espuria ni cerrarse por una pérdida momentánea del detector, una oclusión breve o una caída puntual de confianza. Por ello, los criterios de activación y desactivación pueden utilizar ventanas diferentes: la activación exige evidencia suficiente para confirmar el patrón, mientras que la desactivación puede requerir ausencia sostenida de evidencia durante un intervalo mínimo. Esta separación reduce oscilaciones y alertas repetidas dentro de un mismo episodio; la reaparición de la condición después de su resolución constituye un episodio nuevo, y la eventual supresión de notificaciones repetidas se define fuera del motor de patrones.

En esta etapa, el motor de patrones queda definido como una estructura lógica preliminar y no como una implementación cerrada. La instancia de análisis y diseño arquitectónico deberá traducir esta definición en componentes, contratos, eventos y configuraciones concretas; la implementación del prototipo deberá materializarla; y la validación experimental deberá calibrar empíricamente sus umbrales, ventanas e histéresis. Con esta delimitación, se busca cerrar la brecha entre patrón conceptual y evaluación en runtime, hasta que queden completamente definidas en el diseño arquitectónico.

###### 17.1.5.3.5. Catálogo de patrones de riesgo

La Tabla 24 presenta el catálogo de patrones de riesgo asociados a las condiciones seleccionadas. Para cada patrón se especifica la condición o condiciones de activación, el nivel de severidad, el rango de persistencia temporal orientativo, el perfil temporal del riesgo que fundamenta la asignación de severidad y el trade-off de falsos positivos asociado.

**Tabla 24**

*Catálogo de patrones de riesgo del prototipo E-OVRT-VDP*

| **Patrón** | **Cond.** | **Severidad** | **Persistencia** | **Criterio de activación** | **Perfil temporal del riesgo** | **Trade-off FP** |
| --- | --- | --- | --- | --- | --- | --- |
| PR-01 | CR-01 | Alto | 3–5 s | Persona detectada sin casco durante el intervalo mínimo | Exposición sostenida a caída de objetos o impactos en zona activa de obra; incidente posible ante evento desencadenante (Decreto 911/96, arts. 50, 98–102 y 107). | Moderado |
| PR-02 | CR-02 | Medio | 5–10 s | Persona detectada sin chaleco o indumentaria de alta visibilidad en zona de circulación durante el intervalo | Riesgo de atropello o interferencia operacional por baja visibilidad; escalada dependiente del movimiento efectivo de vehículos o maquinaria (Decreto 911/96, arts. 47, 63 y 70). | Bajo |
| PR-03 | CR-03 | Crítico | 2–4 s | Persona en posición elevada sin sistema anticaídas durante el intervalo | Caída a distinto nivel con consecuencia potencialmente fatal; requiere respuesta temprana ante exposición en altura sin protección suficiente (Decreto 911/96, arts. 52, 54–56 y 112). | Elevado |
| PR-04 | CR-04 | Crítico | 2–4 s | Persona próxima a borde desprotegido durante el intervalo | Caída a distinto nivel desde abertura, borde o plataforma sin protección colectiva eficaz (Decreto 911/96, arts. 52 y 54–56). | Elevado |
| PR-05 | CR-05 | Crítico | 2–4 s | Maquinaria y peatón co-detectados por debajo del umbral de distancia mínima durante el intervalo | Atropello, aplastamiento o contacto peligroso por interacción próxima entre peatones, vehículos y maquinaria de obra (Decreto 911/96, arts. 47, 61, 70, 71 y 246–249; Ley 19.587, arts. 8 y 9). | Elevado |
| PR-06 | CR-06 | Alto | 3–5 s | Persona detectada dentro del polígono de zona restringida durante el intervalo | Exposición sostenida a riesgos propios de una zona señalizada, delimitada, de exclusión, de seguridad o de acceso restringido (Decreto 911/96, arts. 66–69, 95(a), 139, 140(e)–(f), 156 y 176). | Moderado |

*Nota.* Los rangos de persistencia temporal son orientativos y quedan sujetos a calibración empírica durante la validación experimental, una vez conocido el throughput efectivo del pipeline. La columna “Trade-off FP” indica cualitativamente el riesgo de falsos positivos asociado a la brevedad de la ventana de persistencia. Los artículos normativos referenciados en la columna “Perfil temporal del riesgo” fundamentan la severidad asignada a cada patrón a partir del tipo de exposición, la barrera preventiva omitida y la potencialidad de daño; no definen por sí mismos los umbrales computacionales de activación, distancia, persistencia o latencia del sistema. Fuente: Elaboración propia basada en el análisis normativo de la el Decreto 911/96 y la Ley 19.587.

###### 17.1.5.3.6. Criterios de activación combinada para condiciones de nivel 3

Los patrones PR-05 y PR-06, asociados a condiciones composicionales de Nivel 3, requieren criterios de activación que evalúen relaciones espaciales o de contención entre entidades detectadas independientemente. Los criterios se definen a continuación a nivel conceptual; su materialización en reglas computacionales evaluables corresponde a la instancia de análisis y diseño arquitectónico.

PR-05 — maquinaria en proximidad a peatones. La activación requiere la detección simultánea de al menos una entidad clasificable como maquinaria de obra —por ejemplo, excavadora, retroexcavadora, camión volquete, grúa u otra maquinaria pesada— y al menos una persona, cuyas detecciones presenten una relación de proximidad inferior a un umbral configurable. Como aproximación inicial para el prototipo, puede evaluarse la distancia euclidiana entre puntos representativos de las detecciones en coordenadas de imagen, tales como centroides de bounding boxes o puntos medios inferiores. Sin embargo, esta métrica debe interpretarse como una medida geométrica 2D aproximada y no como una distancia física real, dado que la perspectiva de cámara altera las distancias aparentes en la imagen. Durante la implementación podrán evaluarse métricas alternativas, como la distancia mínima entre bordes de bounding boxes, la distancia entre puntos de apoyo proyectados al plano de suelo o, cuando la cámara lo permita, una distancia corregida mediante calibración u homografía. La evaluación debe sostenerse durante el intervalo de persistencia definido para el patrón, lo que implica que el módulo MOT mantenga trayectorias suficientemente estables de las entidades involucradas a lo largo de los cuadros consecutivos.

PR-06 — persona en zona restringida. La activación requiere la detección de al menos una persona cuya posición representativa se encuentre contenida dentro de un polígono predefinido que represente la zona restringida. Para zonas definidas sobre el plano del suelo, resulta preferible utilizar el punto medio inferior del bounding box como aproximación del punto de apoyo de la persona, en lugar del centroide de la caja, aunque ambas alternativas podrán compararse durante la implementación. El polígono debe ser configurable por el operador como parte de la parametrización del sistema, no como parte del prompt OVD. La definición de zonas restringidas mediante polígonos en coordenadas de imagen presupone una cámara fija o, en su defecto, algún mecanismo de recalibración o compensación de movimiento de cámara. Para el alcance del prototipo experimental, se asume el uso de cámaras fijas. La condición requiere que la permanencia dentro del polígono se sostenga durante el intervalo de persistencia, lo cual implica seguimiento temporal mediante el módulo MOT cuando la persistencia se compute por entidad individual. La instancia de análisis y diseño arquitectónico debe diseñar tanto el mecanismo de definición de polígonos como la lógica de evaluación de contención punto-en-polígono.

Ambos patrones dependen del módulo MOT en la medida en que la evaluación de relaciones sostenidas en el tiempo requiere trayectorias estables de los objetos rastreados durante el intervalo de persistencia. Los ID switches, pérdidas temporales de trayectoria y reasociaciones erróneas pueden generar interrupciones espurias en la evaluación del patrón o reinicios indebidos de la ventana de persistencia. Por ello, estos errores deben contemplarse en el diseño del módulo de razonamiento contextual durante la instancia de análisis y diseño arquitectónico y cuantificarse en la evaluación experimental de la validación experimental.

###### 17.1.5.3.7. Frontera explícita con la instancia de análisis y diseño arquitectónico

El desarrollo de esta sección deja tres insumos directos para la instancia de análisis y diseño arquitectónico: el catálogo de condiciones de riesgo clasificado por niveles de complejidad (Tabla 23), el catálogo de patrones con severidad y persistencia temporal orientativa (Tabla 24), y los criterios conceptuales de activación combinada para PR-05 y PR-06. Estos últimos incluyen el supuesto de cámara fija para la evaluación de zonas restringidas, la necesidad de definir métricas de proximidad y contención espacial, y la conveniencia de incorporar mecanismos de histéresis para evitar activaciones o desactivaciones espurias ante detecciones intermitentes.

Sobre esa base, la instancia de análisis y diseño arquitectónico deberá materializar el esquema declarativo de patrones, el motor de evaluación, la parametrización de zonas restringidas, la lógica de proximidad entre entidades, la lógica de contención punto-en-polígono, los mecanismos computacionales de persistencia temporal y el tratamiento de errores asociados al seguimiento, como pérdidas temporales de trayectoria o cambios de identidad. En particular, deberá definir cómo se traducen los criterios conceptuales en reglas operativas configurables, incluyendo la selección de puntos representativos de las detecciones, las métricas geométricas aplicables en coordenadas de imagen y, si correspondiera, mecanismos de calibración o compensación de perspectiva.

La instancia de análisis y diseño arquitectónico podrá establecer valores iniciales configurables para umbrales espaciales, ventanas temporales y criterios de activación/desactivación, con el fin de implementar y ensayar el sistema. Sin embargo, la calibración empírica final de esos umbrales y ventanas corresponde a la validación experimental, bajo el framework cuantitativo definido en el framework de métricas.

##### 17.1.5.4. Protocolo de diseño y evaluación de prompts OVD

Esta sección establece el marco metodológico para el diseño, la variación sistemática y la evaluación empírica de los prompts textuales que operan como interfaz de consulta del modelo OVD. Se apoya en la evidencia sobre sensibilidad a la formulación del prompt documentada en el análisis de modelos OVD y en antecedentes de la literatura que muestran que el desempeño de modelos visión-lenguaje y detectores open-vocabulary puede verse afectado por la redacción de la consulta textual y por la forma en que esta se transforma en representaciones textuales para la detección (Du et al., 2022; Zhou et al., 2022). Asimismo, toma como referencia protocolos de evaluación recientes orientados a examinar limitaciones de los detectores OVD ante atributos de granularidad fina, vocabularios dinámicos, negativos difíciles, comprensión posicional y relaciones entre objetos (Bianchi et al., 2024; Yao et al., 2024). Su objetivo es sistematizar el proceso de selección de prompts, reducir la arbitrariedad y dejar documentadas las decisiones de formulación con evidencia empírica. El protocolo se articula con el framework definido en el framework de métricas, de la cual toma las métricas de evaluación y los criterios operativos aplicables al componente OVD.

###### 17.1.5.4.1. Sensibilidad a la formulación del prompt como variable del sistema

El análisis de modelos OVD documentó que los modelos de detección open-vocabulary presentan sensibilidad a variaciones en la formulación de las consultas textuales. Esta observación es consistente con antecedentes de la literatura sobre modelos visión-lenguaje, que muestran que cambios leves en la redacción del prompt pueden producir variaciones importantes en el desempeño, especialmente en modelos que operan mediante alineación entre representaciones visuales y textuales (Zhou et al., 2022). En OVD, esta sensibilidad se vincula con el hecho de que las categorías pueden consultarse mediante embeddings textuales generados por el encoder de un modelo visión-lenguaje preentrenado, que luego se alinean o comparan con representaciones visuales de regiones o propuestas de objetos (Gu et al., 2021). En este marco, la formulación del prompt no constituye un detalle accesorio: se ha mostrado que el class text embedding puede generarse a partir de prompts ingresados al encoder textual, que el diseño del prompt requiere ajuste cuidadoso, y que estrategias de prompt learning desarrolladas para clasificación de imágenes pueden resultar subóptimas cuando se trasladan directamente a la detección de objetos, por lo que la optimización de prompts requiere evaluación específica para la tarea de detección (Du et al., 2022).

Investigaciones recientes muestran además que la evaluación de detectores OVD se vuelve especialmente exigente cuando intervienen atributos de granularidad fina, vocabularios dinámicos y clases negativas semánticamente cercanas. El benchmark FG-OVD evalúa la capacidad de los detectores para detectar, distinguir y asignar descripciones finas a objetos en presencia de hard-negative classes, considerando propiedades como color, patrón y material, y evidencia que muchos modelos OVD presentan dificultades para capturar y diferenciar detalles finos (Bianchi et al., 2024). Por su parte, OVDEval documenta limitaciones en comprensión de atributos, posición y relaciones entre objetos, y propone NMS-AP como métrica complementaria para evitar resultados engañosos del AP tradicional en evaluaciones con etiquetas de granularidad fina (Yao et al., 2024). De manera complementaria, trabajos recientes muestran que la incorporación de clases negativas semánticamente relacionadas durante el entrenamiento puede mejorar la discriminación del detector; aunque esta técnica excede el alcance del presente proyecto —que trabaja con modelos preentrenados y sin reentrenamiento específico—, su hallazgo refuerza indirectamente la hipótesis de que la composición semántica del vocabulario considerado por el modelo puede influir sobre su desempeño (Kim et al., 2024).

En conjunto, estas evidencias justifican tratar el diseño de prompts como una variable de ingeniería del sistema, que debe gestionarse con un rigor comparable al de las decisiones de arquitectura, selección de modelos o definición de métricas. El protocolo que se presenta a continuación busca ordenar ese proceso para el dominio específico de detección de condiciones de riesgo en construcción civil.

###### 17.1.5.4.2. Estrategia de variación sistemática

Para cada condición de riesgo del catálogo (Tabla 23) se diseñan múltiples variaciones de prompt que difieren a lo largo de ejes controlados. La variación sistemática permite identificar qué formulaciones logran la mejor alineación semántica con las características visuales del dominio y documenta las decisiones de selección con evidencia reproducible. Se definen cuatro ejes principales.

**Estructura sintáctica.** El primer eje comprende variaciones en la organización de los elementos de la consulta, incluyendo frases nominales simples, oraciones descriptivas con contexto y variaciones en el uso de artículos, preposiciones o modificadores. Por ejemplo, para la detección de casco, las formulaciones “hard hat”, “person wearing hard hat” y “safety helmet on worker” difieren en estructura gramatical, aunque refieren a conceptos visualmente relacionados. Los encoders textuales utilizados por modelos visión-lenguaje y detectores OVD pueden producir representaciones distintas ante formulaciones diferentes, incluso cuando estas remiten a una misma categoría o atributo visual. Esta sensibilidad ha sido documentada en modelos visión-lenguaje, donde cambios leves en la redacción del prompt pueden impactar significativamente el desempeño (Zhou et al., 2022), y también en el contexto de OVD, donde el embedding textual de clase depende de los prompts ingresados al encoder textual y requiere ajuste específico para la tarea de detección (Du et al., 2022).

Se incluyen además variaciones con template, como “a photo of a [CLASS]”. Esta decisión se fundamenta en el uso habitual de templates en modelos tipo CLIP, donde transformar una etiqueta aislada en una descripción textual breve puede reducir la brecha entre nombres de clase y textos naturales observados durante el preentrenamiento, y mejorar el desempeño frente al uso de la etiqueta sin contexto (Radford et al., 2021). En consecuencia, el protocolo compara prompts con y sin template, sin presuponer a priori cuál formulación resultará superior para el dominio específico de seguridad en construcción.

**Nivel de especificidad del vocabulario.** El segundo eje comprende variaciones en la granularidad de los términos utilizados, desde vocabulario genérico hasta terminología específica del dominio de construcción. Por ejemplo, “person”, “worker” y “construction worker” representan distintos niveles de especificidad semántica para referirse a entidades humanas observables en una escena de obra. La hipótesis metodológica es que términos más específicos pueden mejorar la precisión en el dominio al reducir la ambigüedad de la consulta y aproximarla al contexto visual de obra. Sin embargo, también pueden reducir el recall si la formulación elegida resulta demasiado restrictiva o menos compatible con las representaciones textuales aprendidas por el modelo durante el preentrenamiento. Por ello, la selección entre vocabulario genérico y vocabulario específico no se asume como una decisión evidente, sino como una variable experimental del diseño de prompts. Esta expectativa se fundamenta en que, en los modelos OVD, las categorías consultadas dependen de representaciones textuales generadas a partir del prompt y alineadas con representaciones visuales del detector (Gu et al., 2021). Asimismo, la literatura sobre prompt learning para OVD muestra que la formulación textual de las clases requiere ajuste específico para la tarea de detección, por lo que variaciones léxicas aparentemente menores pueden afectar el desempeño y deben evaluarse empíricamente (Du et al., 2022).

**Estrategia de detección.** El tercer eje distingue entre formulaciones directas y formulaciones indirectas o descompuestas. En las formulaciones directas, el prompt intenta describir la condición de riesgo completa, incluyendo presencia o ausencia del elemento relevante; en las indirectas, el detector identifica entidades visibles por separado y la evaluación de la condición se reconstruye mediante lógica externa al modelo OVD. Esta distinción no es meramente terminológica: define dos modos de consulta con implicancias diferentes sobre precisión, costo computacional y complejidad de integración en el pipeline. La distinción resulta pertinente porque los modelos OVD permiten consultar categorías o descripciones mediante entradas textuales, pero no necesariamente resuelven de forma robusta todos los atributos, posiciones y relaciones espaciales implicados en una condición compuesta (Gu et al., 2021; Yao et al., 2024).

En este trabajo estas familias se identifican con un código: estrategia directa (E-DIR), cuando el prompt intenta describir la condición de riesgo completa; estrategia indirecta (E-IND), cuando el detector identifica entidades visibles por separado y la condición se reconstruye mediante lógica externa al modelo; y estrategia híbrida (E-HYB), cuando se combinan consultas de ambos tipos bajo una regla de composición explícita. Los códigos identifican las variantes en el diseño arquitectónico y en la evaluación experimental.

La elección entre ambas estrategias está condicionada por la dificultad práctica de evaluar condiciones formuladas en términos de ausencia visible. Mientras la estrategia directa intenta describir de manera íntegra la condición de riesgo, la indirecta opera con prompts de presencia pura —por ejemplo, “person” y “hard hat” como consultas separadas— y traslada al sistema la responsabilidad de asociar detecciones y verificar relaciones geométricas. El beneficio potencial en robustez semántica se compensa, sin embargo, con mayor complejidad de razonamiento y una posible carga adicional de inferencia por cuadro, cuya magnitud deberá verificarse frente al presupuesto de latencia definido en el framework de métricas. La estrategia indirecta resulta especialmente pertinente para condiciones cuya evidencia visual es la ausencia de un EPP —CR-01, CR-02, CR-03— y para condiciones que requieren evaluación de relaciones espaciales intracuadro —CR-03, CR-04—.

El protocolo de evaluación de la Sección 17.1.5.4.5 compara empíricamente ambas estrategias para todas las condiciones en que sean aplicables, sin presuponer la superioridad de ninguna. La instancia de análisis y diseño arquitectónico deberá materializar la lógica de asociación espacial requerida por la estrategia indirecta y determinar si su costo computacional adicional es compatible con las restricciones operativas del sistema.

**Composición del vocabulario activo.** El cuarto eje evalúa cómo el conjunto de prompts simultáneamente activos en el vocabulario del detector afecta el desempeño de cada prompt individual. El benchmark FG-OVD muestra que la evaluación de detectores open-vocabulary se vuelve especialmente exigente cuando el vocabulario incluye clases negativas de granularidad fina, es decir, descripciones semánticamente cercanas al prompt objetivo pero referidas a categorías o atributos distintos. En ese escenario, varios modelos OVD presentan dificultades para detectar, distinguir y asignar correctamente descripciones finas en presencia de hard-negative classes (Bianchi et al., 2024).

En el contexto de E-OVRT-VDP, donde el sistema busca simultáneamente múltiples condiciones y entidades —por ejemplo, “hard hat”, “person”, “reflective vest” y “scaffolding”—, se plantea la hipótesis de que prompts semánticamente próximos pueden competir entre sí y generar confusiones de clasificación. Por ello, este eje propone evaluar el desempeño de cada prompt tanto en aislamiento como dentro del vocabulario completo del sistema.

**Implicancias del tamaño del vocabulario activo.** El número total de prompts simultáneamente activos en el vocabulario del detector puede tener consecuencias tanto sobre la latencia de inferencia como sobre la precisión de la detección. Desde la perspectiva computacional, los modelos difieren en la forma en que procesan el vocabulario textual, por lo que el impacto del tamaño del vocabulario no debe asumirse uniforme entre arquitecturas. Esto puede observarse con dos ejemplos: por un lado, los modelos de la familia YOLO orientados a detección open-vocabulary adoptan estrategias de precomputación o reparametrización de embeddings textuales para favorecer una inferencia eficiente. YOLO-World utiliza un paradigma prompt-then-detect, en el que los prompts definidos por el usuario pueden codificarse previamente como un vocabulario offline y luego reparametrizarse como pesos del modelo para el despliegue (Cheng et al., 2024). En una línea similar, YOLOE propone una estrategia de alineación región-texto reparametrizable —RepRTA— que refina embeddings textuales preentrenados mediante una red auxiliar liviana y permite reparametrizar esa información en la cabeza de clasificación durante la inferencia, reduciendo el costo asociado al procesamiento textual en tiempo de ejecución (Wang et al., 2025). Esto no implica necesariamente que el costo total de inferencia sea completamente independiente del tamaño del vocabulario, ya que pueden existir efectos residuales asociados a la cabeza de predicción, el número de categorías activas, el postprocesamiento o la implementación concreta. Sin embargo, estas arquitecturas desplazan una parte relevante del costo textual fuera del ciclo de inferencia por imagen o cuadro, lo que resulta particularmente pertinente para un sistema orientado a tiempo real. Por otro lado, Grounding DINO recibe como entrada un par imagen-texto y, para tareas de detección de objetos, concatena los nombres de categorías como texto de entrada. Su arquitectura incluye un backbone textual —por ejemplo, BERT—, módulos de fusión imagen-texto, selección de consultas guiada por lenguaje y decodificación cross-modal. En consecuencia, cuando el vocabulario activo crece, aumenta también la longitud/tokenización de la entrada textual y el costo asociado al procesamiento y fusión de esas representaciones, salvo que se implementen mecanismos específicos de precomputación o caché de embeddings (Liu et al., 2024).

Estas diferencias arquitectónicas tienen consecuencias directas sobre cuántos prompts pueden mantenerse activos simultáneamente dentro del presupuesto de latencia del sistema. Por ello, la selección del vocabulario activo deberá evaluarse junto con el modelo OVD elegido, la sintaxis concreta de los prompts, la resolución de entrada y el hardware de inferencia disponible.

###### 17.1.5.4.3. Consideraciones sobre el idioma de los prompts

Los modelos OVD candidatos analizados en el análisis de modelos OVD —Grounding DINO, YOLO-World, YOLOE, Florence-2 y OWL-ViT— se apoyan en arquitecturas visión-lenguaje donde la entrada textual cumple un rol central. Grounding DINO procesa pares imagen-texto y utiliza un backbone textual basado en BERT; YOLO-World emplea un encoder textual tipo CLIP; YOLOE utiliza MobileCLIP-B(LT) para codificar prompts textuales; OWL-ViT transfiere modelos imagen-texto preentrenados a detección open-vocabulary; y Florence-2 opera mediante una representación unificada basada en prompts para múltiples tareas de visión y visión-lenguaje (Liu et al., 2024; Cheng et al., 2024; Wang et al., 2025; Minderer et al., 2022; Xiao et al., 2024).

La decisión de formular los prompts primarios en inglés se fundamenta en la centralidad de ese idioma en varios de los modelos y corpus visión-lenguaje utilizados como base. CLIP fue entrenado sobre pares imagen-texto recolectados de la web y se utiliza ampliamente mediante prompts textuales en inglés; Conceptual Captions se construyó a partir de páginas web en inglés y filtros lingüísticos basados en vocabulario de Wikipedia en inglés; y CC12M amplía la escala de esa línea de recolección para preentrenamiento visión-lenguaje (Radford et al., 2021; Sharma et al., 2018; Changpinyo et al., 2021). Aunque no todos los modelos candidatos publican una caracterización lingüística equivalente de sus datos de entrenamiento, la evidencia disponible justifica utilizar el inglés como idioma primario de consulta para favorecer la compatibilidad con los patrones lingüísticos dominantes del preentrenamiento. Esta decisión tiene una implicación práctica relevante: la plataforma se desarrolla en un contexto académico argentino y constituye un prototipo experimental, no un sistema productivo. En consecuencia, el idioma natural de trabajo de operadores e investigadores es el español, mientras que la capa de consulta del detector se formulará primariamente en inglés para favorecer la alineación con los modelos candidatos. En el prototipo experimental, la traducción de las descripciones de condiciones de riesgo al inglés se realiza manualmente durante la fase de diseño de prompts.

Como línea complementaria de evaluación, podrá explorarse la ejecución de prompts formulados directamente en español o mediados por traducción automatizada, con el fin de cuantificar la eventual degradación asociada a la brecha lingüística y documentar si alguno de los modelos candidatos ofrece soporte multilingüe funcional para el dominio. De realizarse, estas pruebas corresponderán a la validación experimental y constituirán una contribución adicional al análisis de viabilidad del sistema.

###### 17.1.5.4.4. Catálogo de prompts candidatos

El catálogo de prompts candidatos define las formulaciones previstas para evaluar las condiciones de riesgo seleccionadas. Para las condiciones de Nivel 1 y Nivel 2 se contemplan formulaciones directas, variantes léxicas y estrategias indirectas o descompuestas, según el tipo de evidencia visual que se busca activar en el modelo. Por ejemplo, una condición como ausencia de casco puede evaluarse mediante consultas directas orientadas a identificar una “persona sin casco” o mediante variantes que busquen evidencias positivas de “casco de seguridad” sobre la región cefálica. De forma similar, una condición asociada al chaleco reflectivo puede abordarse mediante prompts como “persona con chaleco de seguridad” o formulaciones equivalentes vinculadas a ropa de alta visibilidad.

En el caso de las condiciones de nivel 3, no se proponen prompts integrados como una única consulta OVD, dado que su evaluación requiere razonamiento contextual sobre múltiples entidades o relaciones espaciales. Por ello, se consideran prompts orientados a detectar las entidades componentes, cuyos resultados podrán ser utilizados posteriormente por el motor de patrones. El conjunto de candidatos se construye a partir del catálogo del Anexo C (Tabla C.1), y las formulaciones finalistas deben quedar seleccionadas y congeladas mediante un acta previa a la evaluación comparativa.

La inclusión de prompts candidatos para CR-03 y CR-04 no implica que ambas condiciones dispongan de soporte completo de evaluación en datasets públicos. En estos casos, los prompts permiten explorar formulaciones posibles y detectar entidades o estados visuales parciales, pero la validación del patrón completo depende de contar con datos que representen la condición operacionalizada. Por ello, los resultados sobre CR-03 y CR-04 deberán distinguir explícitamente entre desempeño del prompt sobre componentes visuales y evaluación integral de la condición de riesgo.

###### 17.1.5.4.5. Protocolo de evaluación de prompts

El protocolo de evaluación tiene por objetivo determinar, para cada condición de riesgo y cada modelo OVD candidato, qué formulación de prompt ofrece el mejor desempeño dentro del framework adoptado para el componente OVD, con lectura prioritaria sobre AP@0.5 y Precision/Recall en el punto operativo declarado. Su diseño se fundamenta en prácticas de evaluación documentadas en la literatura reciente, particularmente FG-OVD y OVDEval (Bianchi et al., 2024; Yao et al., 2024), adaptadas al alcance y los recursos de un proyecto académico. Las métricas, los criterios de reporte y los umbrales orientativos se definen en el framework de métricas; el presente protocolo describe la estructura procedural de las pruebas de prompts dentro de ese marco. Se organiza en cinco fases.

**Fase 1 - Preparación del dataset de evaluación.** Para cada condición de riesgo, se selecciona un subconjunto del inventario de datasets documentado en la estrategia de datos, benchmarks y partición que contenga imágenes o cuadros con anotaciones de verdad fundamental o ground truth relevantes para la condición evaluada. La selección sigue el principio de representatividad, de modo que el subconjunto incluya variación en iluminación, ángulo de cámara, grado de oclusión y escala de los objetos de interés, dentro de lo que los datos disponibles permitan.

Cuando el ground truth existente no cubra directamente la condición —por ejemplo, si el dataset anota “casco” pero no “persona sin casco”—, se generarán anotaciones complementarias sobre un conjunto acotado de imágenes, garantizando acuerdo interanotador mediante doble anotación independiente sobre al menos un 20% del conjunto. Para etiquetas categóricas sobre unidades previamente definidas se calculará el coeficiente kappa de Cohen como indicador de confiabilidad interanotador (Cohen, 1960); cuando la anotación involucre localización espacial mediante bounding boxes, el acuerdo se evaluará además mediante criterios de solapamiento geométrico, como IoU promedio o proporción de coincidencias por encima de un umbral IoU predefinido. El requisito rige para toda anotación producida por el proyecto; cuando la referencia se reutilice de anotaciones de fuente sin reanotación, la doble anotación no aplica y la ausencia de una medida de acuerdo debe declararse como limitación del material.

Como objetivo operativo se procurará contar con al menos 200 instancias positivas anotadas por condición, complementadas con casos negativos cuando resulten necesarios para estimar precisión y falsos positivos. Cuando una condición o un estrato no alcance ese piso, el protocolo exige reportar el n efectivo con intervalos de confianza al 95 % obtenidos por bootstrap sobre las unidades de evaluación y abstenerse de ordenar variantes cuyos intervalos se superpongan.

**Fase 2 - Definición de la matriz experimental.** Se construye la matriz de combinaciones a evaluar, donde cada celda corresponde a una tupla (modelo OVD, condición de riesgo, variación de prompt, contexto de vocabulario). El último término responde al eje de composición de vocabulario definido en la Sección 17.1.5.4.2, y distingue dos condiciones experimentales por prompt: evaluación en aislamiento, donde el prompt —o el conjunto mínimo de prompts requerido por la estrategia indirecta o descompuesta— es el único vocabulario activo del modelo, y evaluación en contexto completo, donde el prompt opera junto con los demás prompts activos del sistema.

Los hiperparámetros del modelo —umbral de confianza, umbral de NMS— se fijan a valores constantes durante toda la evaluación para garantizar comparabilidad entre variaciones de prompt. Si se evalúan múltiples umbrales, estos se documentan como variable adicional de la matriz.

**Fase 3 - Ejecución sistemática.** Para cada combinación de la matriz, se ejecuta la inferencia sobre el dataset de evaluación correspondiente, registrando para cada imagen las detecciones producidas con sus coordenadas de bounding box, puntaje de confianza y etiqueta asignada por el modelo. La ejecución se realiza en condiciones controladas, manteniendo constantes el hardware, la resolución de entrada y la configuración de preprocesamiento. Los resultados se almacenan en formato estructurado que permita el cálculo posterior de métricas y la reproducción de los experimentos.

**Fase 4 - Cálculo de métricas.** Para cada tupla (modelo, condición, prompt, contexto de vocabulario), se calculan las métricas definidas en el framework de métricas para el componente OVD. Se registra también el puntaje de confianza medio de las detecciones verdaderas positivas como indicador complementario de la estabilidad de la respuesta del modelo ante cada formulación de prompt.

Para las condiciones evaluadas con estrategia indirecta o descompuesta, se calculan también las métricas de cada entidad componente por separado, de modo que pueda identificarse si la degradación proviene de la detección de las entidades individuales, del atributo visual evaluado o de la lógica de asociación.

**Fase 5 - Análisis comparativo y selección.** Se construye una matriz de resultados que permite identificar, para cada condición, la combinación (modelo, prompt) que maximiza el criterio de selección definido en el framework de métricas. Los resultados se analizan tanto por condición individual como de manera transversal, identificando patrones sistemáticos —por ejemplo, si los prompts con template superan consistentemente a los prompts sin template, o si la estrategia indirecta supera a la directa para condiciones de EPP—. Se documenta también la sensibilidad de cada modelo al contexto de vocabulario, cuantificando la diferencia de desempeño entre aislamiento y contexto completo.

El protocolo produce como salida un registro estructurado de métricas por combinación, que alimenta directamente las decisiones de la instancia de análisis y diseño arquitectónico —selección de prompts primarios para la configuración del sistema— y las conclusiones de la validación experimental —análisis de sensibilidad y robustez frente a variaciones de formulación—. Este registro, junto con los scripts de ejecución y los datasets utilizados, constituye el artefacto de reproducibilidad del protocolo.

##### 17.1.5.5. Síntesis parcial de condiciones, prompts y variantes de prueba

La formulación del prompt se asume como variable experimental del sistema. En OVD, cambios de sintaxis, especificidad o selección léxica pueden modificar el comportamiento del detector, especialmente cuando la condición se formula por ausencia de un elemento, por atributos finos o por composición contextual (Du et al., 2022; Bianchi et al., 2024). Por ello, la instancia de análisis y diseño arquitectónico deberá contrastar familias de prompts antes de congelar la configuración comparativa final.

Para evitar ambigüedades terminológicas, esta sección adopta dos definiciones operativas. La primera es matriz de prompts, entendida como el conjunto acotado de formulaciones alternativas que se ensayan para una misma condición. La segunda es la composición del vocabulario activo, entendida como el conjunto de descripciones, etiquetas o consultas que el modelo evalúa en simultáneo dentro de una corrida determinada. Esta aclaración reemplaza formulaciones más difusas de la versión anterior y deja explícito qué variable se está midiendo cuando se habla del “tamaño” o de la “composición” del vocabulario.

El desarrollo completo de las matrices de prompts, sus variantes y los criterios de prueba se presenta en el Anexo C.

#### 17.1.6. Estrategia de datos, benchmarks y partición

##### 17.1.6.1. Introducción y alcance

###### 17.1.6.1.1. Propósito y preguntas rectoras

La presente sección responde a las preguntas rectoras P-E1-03 y P-E1-08 formuladas en la sección 16.7.3 de la fundamentación teórica. En relación con P-E1-03, construye un inventario crítico de datasets públicos potencialmente utilizables para evaluar el prototipo experimental sobre las condiciones de riesgo definidas en la taxonomía de condiciones de riesgo, patrones y prompts, documentando cobertura, formato, acceso, licencia y restricciones operativas. En relación con P-E1-08, analiza qué colecciones pueden funcionar como insumo de un experimento comparativo acotado de fine-tuning, bajo las condiciones metodológicas fijadas por el framework de métricas para preservar la validez de la comparación entre baseline zero-shot y variante ajustada al dominio.

El propósito operativo de esta sección es cuádruple. Primero, construir un inventario sistematizado de datasets públicos relevantes para detección open-vocabulary en entornos de construcción civil, documentando para cada uno los atributos técnicos, de acceso y de licencia que condicionan su viabilidad. Segundo, establecer un mapeo explícito entre cada dataset candidato y las condiciones de riesgo CR-01 a CR-06 definidas en la taxonomía de condiciones de riesgo, patrones y prompts. Tercero, evaluar la aptitud de cada colección para su eventual uso en experimentos comparativos de ajuste de dominio, si ello resulta metodológicamente viable. Cuarto, fijar las condiciones metodológicas mínimas que cualquier estrategia de partición deberá satisfacer para sostener una comparación válida entre baseline zero-shot y variante fine-tuned, cuando esa comparación aplique.

El análisis parte del reconocimiento, establecido en la fundamentación teórica, de que los modelos OVD preentrenados en colecciones generalistas presentan una brecha de dominio respecto de la construcción civil. Esa brecha no se resuelve únicamente con mayor volumen: también exige distinguir entre condiciones con evidencia visual directa —como CR-01 y CR-02—, condiciones espaciales o de ausencia visual fina —como CR-03 y CR-04— y condiciones relacionales o dependientes de parametrización externa —como CR-05 y CR-06—. En consecuencia, la aptitud de un dataset no se agota en la presencia de una clase aislada, sino que debe leerse en articulación con la taxonomía y el protocolo de evaluación definidos por la taxonomía de condiciones de riesgo, patrones y prompts y el framework de métricas.

El alcance de la sección es metodológico. Elabora un inventario de datasets, explicita criterios de inclusión y exclusión, mapea cobertura contra CR-01–CR-06, analiza compatibilidad con los pipelines de ajuste priorizados y fija condiciones mínimas para su eventual partición y uso experimental. No define todavía la combinación definitiva de datasets, no ejecuta particiones ni campañas de curación o anotación complementaria y no implementa mediciones; esas decisiones corresponden a la instancia de análisis y diseño arquitectónico y su validación empírica a la validación experimental.

###### 17.1.6.1.2. Criterios de categorización y exclusión

El inventario de esta sección se organiza en dos categorías con criterio de pertenencia explícito. La primera agrupa los datasets sobre los cuales se ejecutan operaciones directas (descarga, procesamiento, partición y uso experimental). La segunda comprende benchmarks establecidos cuyas particiones de test se emplean para medir el rendimiento de módulos específicos del sistema en condiciones comparables con la literatura. Toda colección que no satisfaga al menos uno de estos dos criterios queda fuera del alcance de la sección.

**Categoría 1 — Datasets de gestión directa.** Un dataset pertenece a esta categoría si se descarga, procesa y utiliza directamente para evaluación del pipeline OVD en el dominio de construcción civil y/o como insumo del experimento comparativo de fine-tuning. La pertenencia a esta categoría no implica decisión de uso; la confirmación de qué datasets se gestionan efectivamente corresponde a la instancia de análisis y diseño arquitectónico. Los datasets listados en la Sección 17.1.6.2 constituyen el conjunto de candidatos analizados en esta sección.

**Categoría 2 — Benchmarks de evaluación de referencia.** Un dataset pertenece a esta categoría si es un benchmark establecido cuyas particiones de test se emplearán para medir el rendimiento de módulos específicos del sistema bajo condiciones comparables con la literatura. Cada benchmark incluido debe tener una función explícita dentro del protocolo de evaluación, indicando qué módulo se evalúa con él, en qué etapa se utiliza y qué métricas se obtienen.

**Alcance y exclusiones explícitas.** Quedan fuera del alcance de la presente sección las colecciones generalistas de gran escala sobre las cuales los modelos OVD fueron preentrenados por sus autores, tales como Visual Genome, LVIS v1.0, Objects365 v2, Open Images V7, entre otras. Estas colecciones no constituyen datos gestionados por el proyecto: no se descargan, procesan ni particionan, sino que se aprovechan indirectamente a través de los pesos públicos de los modelos candidatos. Su documentación corresponde al análisis de el análisis de modelos OVD, donde se describe la procedencia de las capacidades open-vocabulary de cada modelo y las restricciones de licencia asociadas.

También quedan fuera del inventario las colecciones que no satisfacen los criterios mínimos de selección definidos en la Sección 17.1.6.1.3, en particular aquellas sin disponibilidad pública verificable, sin condiciones de uso suficientemente documentadas, con baja pertinencia respecto del dominio de construcción civil, con cobertura insuficiente de las condiciones de riesgo CR-01 a CR-06, o con anotaciones incompletas que impidan su conversión o evaluación bajo el protocolo del proyecto. De igual modo, se excluyen como fuente principal de evaluación los datasets compuestos exclusivamente por imágenes sintéticas sin validación manual o sin contraste documentado con escenas reales, dado que no permiten caracterizar adecuadamente el sesgo de dominio respecto de entornos reales de construcción y podrían comprometer la validez ecológica del protocolo experimental.

Las condiciones de calzado inadecuado, ausencia de guantes o gafas de protección, y obstrucción de pasillos o materiales inestables, aunque presentes en la taxonomía normativa de la fundamentación teórica, no integran el alcance experimental definido en la taxonomía de condiciones de riesgo, patrones y prompts para la Etapa 2. Su análisis de cobertura queda diferido a etapas posteriores, en caso de que se decida ampliar el conjunto de condiciones evaluadas.

###### 17.1.6.1.3. Criterios metodológicos de selección y evaluación

La evaluación de cada dataset candidato se realiza sobre siete dimensiones que derivan del análisis teórico de la fundamentación teórica y de las necesidades operativas del proyecto. Estas dimensiones no tienen pesos fijos a priori; su ponderación relativa depende de la función que la instancia de análisis y diseño arquitectónico asigne al dataset dentro de la estrategia combinatoria. Un dataset orientado a ajuste de dominio priorizaría la pertinencia al dominio (C1) y la cobertura normativa (C2), mientras que uno orientado a preservar capacidades open-vocabulary priorizaría la compatibilidad semántica (C3) y la posibilidad de conversión o integración en los pipelines efectivamente seleccionados.

**Tabla 25**

*Criterios de evaluación para la selección de datasets candidatos*

| **#** | **Dimensión** | **Descripción operativa** |
| --- | --- | --- |
| C1 | Pertinencia al dominio | Presencia de escenas de construcción, industria o trabajadores con EPP. Se valoran entornos realistas con variaciones de iluminación, ángulo de cámara y condiciones climáticas. |
| C2 | Cobertura normativa | Proporción de categorías anotadas que se corresponden con alguna condición de riesgo de la taxonomía operacionalizada en la taxonomía de condiciones de riesgo, patrones y prompts, derivada del marco normativo argentino. |
| C3 | Compatibilidad OV | Amplitud del vocabulario, presencia de anotaciones en lenguaje natural o descripciones que permitan consultas semánticas. |
| C4 | Soporte temporal | Existencia de secuencias con entidades persistentes (IDs de trayectoria) o anotaciones cuadro a cuadro, necesarias para la integración con módulos de seguimiento multi-objeto (MOT). |
| C5 | Calidad de anotación | Exhaustividad y consistencia de las anotaciones (cajas delimitadoras, máscaras, relaciones). Se prefieren anotaciones manuales con protocolos de control de calidad documentados. |
| C6 | Condiciones desafiantes | Presencia de oclusiones, escenas nocturnas o de baja iluminación, movimiento, multitudes o cambios de escala que permitan evaluar robustez en condiciones realistas de obra. |
| C7 | Viabilidad técnico-legal | Formato estandarizado o convertible; disponibilidad pública verificada; licencia explícita o declaración pública de uso académico compatible. Cuando la fuente sólo indique “free use” o la licencia no sea visible, el dataset se mantiene como candidato condicional y requiere verificación manual antes de su gestión efectiva. |

*Nota.* Los criterios C1 a C7 no tienen pesos fijos; su ponderación relativa dependerá de la función asignada al dataset en la instancia de análisis y diseño arquitectónico. Elaboración propia basada en el análisis metodológico de la Etapa 2.

##### 17.1.6.2. Datasets de gestión directa (categoría 1)

La selección se concentra en cuatro colecciones retenidas como candidatas de gestión directa por su pertinencia para CR-01 y CR-02, su disponibilidad y su viabilidad de integración. La retención no asigna todavía un rol definitivo: entrenamiento, evaluación y banco deben definirse mediante particiones disjuntas y con trazabilidad de licencia y procedencia.

###### 17.1.6.2.1. Datasets retenidos como candidatos

**Tabla 26**

*Datasets retenidos como candidatos de gestión directa*

| **Dataset** | **Volumen o versión** | **Contenido relevante** | **Formato** | **Licencia** | **Cobertura** | **Lectura metodológica** |
| --- | --- | --- | --- | --- | --- | --- |
| SHEL5K (Otgonbold et al., 2022) | 5.000 imágenes | Casco, cabeza y persona con o sin casco | Pascal VOC | CC BY 4.0 | CR-01 directa | Fuente sólida para evaluar presencia y ausencia de casco; no cubre chaleco ni relaciones contextuales. |
| CHV (Wang et al., 2021) | 1.330 imágenes | Persona, chaleco y cascos por color | Formato nativo a inspeccionar | Sin licencia formal; cita obligatoria | CR-01 y CR-02 | Condicionado a verificar términos de uso y redistribución. |
| construction_site_safety | Versión registrada | Escenas de construcción con anotaciones de EPP | YOLO / Roboflow | CC BY 4.0 | CR-01 y CR-02 | Candidato de dominio; exige separar linajes de entrenamiento y evaluación. |
| ppe_siabar | Versión registrada | Anotaciones de EPP en dominio afín | YOLO / Roboflow | CC BY 4.0 | CR-01 y CR-02 | Candidato para adaptación; aptitud sujeta a curación y partición. |

*Nota.* La retención expresa aptitud metodológica como candidato y no asignación efectiva. El rol de cada fuente debe quedar congelado antes de cualquier entrenamiento, sin solapamiento entre material de ajuste y estratos de evaluación.

###### 17.1.6.2.2. Datasets descartados y causa metodológica

Las colecciones restantes se descartan del núcleo de gestión directa cuando su licencia, acceso, dominio o cobertura no permiten sostener un uso principal dentro del protocolo. El descarte no niega su valor académico; delimita por qué no integran la combinación retenida.

**Tabla 27**

*Datasets descartados y causa metodológica*

| **Dataset** | **Causa principal** | **Consecuencia para el protocolo** | **Estatuto** |
| --- | --- | --- | --- |
| SH17 | Licencia CC BY-NC-SA y dominio predominantemente industrial. | No se adopta como fuente principal del núcleo. | Descartado. |
| Pictor-PPE | Licencia no verificable y versión pública parcial. | No permite asegurar gestión y redistribución reproducibles. | Descartado. |
| Construction-PPE | Licencia AGPL-3.0 y cobertura ya atendida por fuentes retenidas. | Se evita introducir obligaciones adicionales sin aporte diferencial suficiente. | Descartado. |
| GDUT-HWD y SHWD | Licencia del paquete sin verificar y condición principal ya cubierta. | Pueden conservarse como referencia, pero no como insumo gestionado. | Descartados. |
| SODA | Cobertura orientada a contexto y condiciones fuera del núcleo CR-01/CR-02. | No resuelve de forma nativa los patrones priorizados. | Descartado del núcleo. |
| MOCS | Copia pública parcial y utilidad principalmente exploratoria para maquinaria. | No se adopta para evaluación principal ni ajuste de EPP. | Uso exploratorio solamente. |

*Nota.* Las causas de descarte se aplican al uso principal dentro de este protocolo; no constituyen una evaluación general de la calidad científica de cada colección.

###### 17.1.6.2.3. Síntesis de cobertura conjunta y brechas

La cobertura retenida es suficiente para concentrar el núcleo en CR-01 y CR-02. CR-01 dispone de evidencia directa sobre casco y ausencia de casco; CR-02 cuenta con fuentes que combinan persona y chaleco. CR-03 y CR-04 conservan una brecha directa, mientras que CR-05 y CR-06 requieren datos relacionales, regiones externas o material controlado. La presencia de entidades auxiliares no se interpreta como anotación del patrón completo.

###### 17.1.6.2.4. Viabilidad para el ajuste fino

La rama de ajuste fino se limita a CR-01 y CR-02 y utiliza únicamente fuentes cuya cobertura, licencia y formato permitan construir un conjunto curado y disjunto del test. La comparación no presupone que el ajuste deba superar a la baseline: exige observar la ganancia en el dominio y la retención de capacidades fuera de las clases ajustadas bajo el framework de métricas.

El protocolo conserva un máximo de dos familias candidatas y un rango orientativo de 500 a 2.000 imágenes para el split de entrenamiento. La cantidad concreta, la conversión de formato y la selección de capas o parámetros deben quedar predefinidas y justificarse si se apartan de ese rango.

###### 17.1.6.2.5. Transferibilidad y límites de interpretación

La transferibilidad se interpreta de forma cualitativa según proximidad visual al dominio, cobertura de EPP, diversidad de escala y posibilidad de conservar negativos explícitos. Las cuatro fuentes retenidas sostienen el núcleo, pero ninguna habilita por sí sola conclusiones sobre condiciones relacionales, altura, zonas restringidas o desempeño en obra real no controlada.

###### 17.1.6.2.6. Datos complementarios para condiciones brechadas

Cuando una condición brechada permanezca dentro del alcance exploratorio, el orden de preferencia es: curación de fuentes públicas con licencia compatible; anotación complementaria acotada con control de calidad; y producción de material controlado en el EBE bajo consentimiento y minimización. La ampliación sólo se justifica si aporta evidencia interpretable sin desplazar la evaluación del núcleo.

###### 17.1.6.2.7. Condiciones para la partición de datos

La evaluación comparativa zero-shot vs. fine-tuned requiere que los conjuntos de entrenamiento y evaluación sean estrictamente disjuntos, tal como exige el framework de métricas para sostener la validez de la comparación. El diseño concreto de la partición —qué proporciones se asignan a entrenamiento, validación y evaluación, qué datasets alimentan el subset de entrenamiento y qué colecciones se reservan para test— corresponde a la instancia de análisis y diseño arquitectónico, una vez definidos los modelos seleccionados y la estrategia de adaptación de dominio. La presente sección documenta sólo las condiciones metodológicas que cualquier esquema de partición deberá satisfacer. Una misma fuente no puede utilizarse simultáneamente como material de entrenamiento y como estrato del banco de evaluación; cualquier excepción invalidaría la independencia de la comparación.

**Tabla 28**

*Condiciones metodológicas para la partición de datos*

| **Condición** | **Descripción** |
| --- | --- |
| Disyunción estricta | Ninguna imagen del split de test debe aparecer en el split de entrenamiento, ni directamente ni mediante data augmentation aplicada sobre imágenes de test. El incumplimiento de esta condición invalidaría la comparación pretrained vs. fine-tuned. |
| Test set compartido | El split de evaluación debe ser idéntico para la línea base pretrained y los modelos fine-tuned, a fin de garantizar comparabilidad directa. |
| Semilla reproducible | Cuando la partición sea aleatoria, debe documentarse la semilla utilizada, de modo que el split pueda regenerarse y verificarse independientemente. |
| Splits oficiales | Cuando exista un split publicado por la fuente (p. ej., CHV en el paper o Construction-PPE en Ultralytics), conviene revisarlo antes de redefinirlo. La instancia de análisis y diseño arquitectónico podrá apartarse de ese esquema si justifica la decisión. |
| Rango de entrenamiento | El split de entrenamiento para fine-tuning se acota a 500–2.000 imágenes, conforme al análisis de suficiencia desarrollado en la sección 17.1.6.2.4. La baseline zero-shot se evalúa siempre sobre el test set congelado. |
| No solapamiento cruzado | Si se combinan múltiples datasets para formar un split unificado, debe verificarse la ausencia de imágenes duplicadas entre colecciones, especialmente entre datasets de PPE web-mined o crowd-sourced que podrían compartir fuentes de origen. |
| Congelamiento previo | El test set debe quedar definido y congelado antes del inicio de cualquier entrenamiento, incluida la aplicación de data augmentation sobre el split de entrenamiento, para evitar data leakage inadvertido. |

*Nota.* Estas condiciones son requisitos metodológicos; las proporciones concretas de partición y la composición final del subset de entrenamiento corresponden a la instancia de análisis y diseño arquitectónico. Cuando exista una divergencia entre el split publicado por una fuente y las necesidades experimentales del proyecto, la desviación deberá justificarse explícitamente en la bitácora.

###### 17.1.6.2.8. Evaluación de aptitud por propósito

La Tabla 29 sintetiza la aptitud metodológica de las cuatro fuentes retenidas para ajuste y evaluación, sin asignar todavía un rol efectivo.

La valoración considera cobertura, proximidad de dominio, formato, licencia y necesidad de mantener fuentes independientes para el test.

**Tabla 29**

*Aptitud de cada dataset candidato para fine-tuning y evaluación*

| **Dataset** | **Aptitud FT** | **Aptitud eval.** | **Justificación** |
| --- | --- | --- | --- |
| SHEL5K | Media | Alta para CR-01 | Cobertura sólida de casco y ausencia de casco; alcance limitado fuera de CR-01. |
| CHV | Media condicionada | Alta para CR-01/CR-02 | Pertinencia de dominio, con términos de uso del dataset que deben verificarse. |
| construction_site_safety | Alta potencial | Alta condicionada | Escenas de construcción y anotaciones de EPP; exige disyunción por linaje entre ajuste y evaluación. |
| ppe_siabar | Alta potencial | Media condicionada | Aporta EPP en dominio afín; requiere una fuente independiente para evaluar generalización. |

*Nota.* “Condicionada” indica que el rol depende de la verificación de términos, de la curación y de una partición estrictamente disjunta.

##### 17.1.6.3. Benchmarks de evaluación de referencia (categoría 2)

Tal como establece el framework de métricas, las métricas MOT basadas en identidades persistentes sólo resultan metodológicamente defendibles cuando se dispone de secuencias o benchmarks específicamente anotados con IDs de trayectoria. Por ello, los benchmarks de esta categoría no sustituyen la evaluación del dominio del proyecto: cumplen una función acotada de verificación de implementación y comparación de referencia para el módulo de seguimiento.

**Tabla 30**

*Benchmarks de evaluación de referencia para módulos de seguimiento*

| **Dataset** | **Características** | **Licencia** | **Métricas** | **Aptitud en el proyecto** | **Limitaciones** |
| --- | --- | --- | --- | --- | --- |
| MOT17 | 14 secuencias reales; benchmark operacionalizado como 42 entradas al considerar tres sets públicos de detecciones por secuencia: DPM, Faster R-CNN y SDP. | CC BY-NC-SA 3.0 | MOTA, IDF1, HOTA | Adecuado para verificar que la implementación del tracker reproduce resultados comparables a trackers de referencia bajo un protocolo conocido. | Benchmark centrado en seguimiento de peatones; no representa el dominio construcción. |
| OVT-B | 1.973 videos; 637.608 anotaciones de bounding boxes; 1.048 categorías. | Apache-2.0 visible en el repositorio oficial | TETA como métrica principal; LocA, ClsA y AssA como componentes. | Adecuado para evaluar la integración OVD+MOT bajo vocabulario abierto extenso y múltiples categorías. | No declara cobertura específica del dominio construcción. |

*Nota.* TETA = Track Every Thing Accuracy; LocA = Localization Accuracy; ClsA = Classification Accuracy; AssA = Association Accuracy. MOTA = Multiple Object Tracking Accuracy; IDF1 = ID F1 Score; HOTA = Higher Order Tracking Accuracy. TrackingNet y LaSOT se descartan por corresponder a benchmarks de single-object seguimiento; OV-TAO se descarta porque OVT-B ofrece mayor escala y una adecuación más directa al problema open-vocabulary multi-object seguimiento del proyecto.

###### 17.1.6.3.1. MOT17 — justificación de uso

MOT17 no representa el dominio de construcción civil. Su inclusión responde a una razón de ingeniería específica: constituye un benchmark de referencia ampliamente utilizado para evaluar trackers multiobjeto bajo un protocolo conocido. En particular, permite contrastar la implementación local del módulo de seguimiento con resultados públicos de trackers de referencia, como ByteTrack y OC-SORT, antes de trasladar el análisis al dominio del proyecto. Por lo tanto, la evaluación sobre MOT17 responde a una pregunta de corrección de implementación y reproducibilidad técnica, no de validez operativa en obra.

###### 17.1.6.3.2. OVT-B — justificación de uso

OVT-B es el benchmark más cercano a la arquitectura conceptual del proyecto, porque evalúa explícitamente el seguimiento multiobjeto en régimen open-vocabulary. Su utilidad no reside en representar el dominio de construcción civil, sino en evaluar la integración OVD+MOT bajo un vocabulario extenso y trayectorias de múltiples categorías. Por ello, OVT-B se interpreta como benchmark de referencia para robustez semántica y asociación temporal, mientras que la validación del dominio específico se mantiene separada y deberá realizarse sobre los datos del proyecto o sobre el escenario complementario que se defina en la instancia de análisis y diseño arquitectónico.

##### 17.1.6.4. Consideraciones transversales

Las secciones precedentes analizaron los datasets desde una perspectiva técnica y metodológica. La presente sección documenta dos dimensiones que atraviesan el inventario completo con independencia de la categoría o del propósito asignado a cada dataset: las condiciones éticas y de licencia que enmarcan el uso de los datos, y las restricciones logísticas que condicionan su gestión operativa. Ambas dimensiones son insumos directos para la planificación de la instancia de análisis y diseño arquitectónico.

###### 17.1.6.4.1. Consideraciones éticas sobre los datos

Los datasets retenidos reúnen imágenes procedentes de repositorios públicos y escenas de construcción o dominios afines centrados en EPP. Su uso previsto se limita a investigación académica, sin reconocimiento facial, identificación individual ni tratamiento biométrico. Las anotaciones consideradas son principalmente cajas delimitadoras y etiquetas de objetos, en concordancia con el principio de minimización desarrollado en el marco ético-legal de la fundamentación teórica.

Para cualquier dato generado ad hoc conforme a las alternativas de la Sección 17.1.6.2.6, se aplicará un protocolo específico de consentimiento informado, anonimización de rostros y minimización de datos personales, sin retención de identificadores biométricos. Este criterio se adopta en consonancia con la normativa argentina vigente de protección de datos personales, en particular la Ley 25.326.

Las condiciones de uso no son homogéneas. SHEL5K, construction_site_safety y ppe_siabar se registran bajo CC BY 4.0; CHV no presenta una licencia formal para el paquete de datos, por lo que su eventual utilización exige citar la fuente y verificar los términos aplicables. La licencia del artículo asociado no se transfiere por inferencia al dataset. Las colecciones descartadas conservan el estatuto y la causa resumidos en la Tabla 27, sin atribuirles licencias no verificadas.

En consecuencia, la instancia de análisis y diseño arquitectónico deberá verificar manualmente los términos efectivos de cada fuente antes de descargar, fusionar, redistribuir o publicar derivados de los datos. La gestión del corpus deberá conservar trazabilidad por dataset de origen, registrar licencias y condiciones aplicables, y evitar que la combinación de colecciones con licencias heterogéneas genere obligaciones incompatibles con el alcance académico del proyecto.

###### 17.1.6.4.2. Logística de datos

El pipeline de gestión de datos comprende cinco pasos secuenciales: descarga o solicitud de acceso desde las fuentes de origen, verificación de integridad, inspección del formato nativo y conversión al formato de trabajo requerido por cada pipeline, partición conforme a las condiciones metodológicas definidas anteriormente, y transferencia del subset de entrenamiento y, cuando corresponda, del conjunto de validación al clúster de cómputo de alto rendimiento Mendieta para el experimento de fine-tuning. La evaluación e inferencia operativa se ejecutarán en el hardware local, manteniendo la separación funcional entre entrenamiento y despliegue documentada en la sección de entorno experimental, infraestructura y escenarios de evaluación. Esto puede verse en detalle en la Tabla C.5 del Anexo C.

##### 17.1.6.5. Síntesis parcial de la estrategia de datos, benchmarks y partición

La estrategia de datos, benchmarks y partición muestra una cobertura desigual respecto del catálogo retenido. Las condiciones de EPP poseen el soporte más sólido: CR-01 cuenta con múltiples fuentes centradas en casco o ausencia de casco, y CR-02 dispone de cobertura adecuada para chaleco, aunque menos redundante. En cambio, CR-03 y CR-04 mantienen brechas directas de cobertura, mientras que CR-05 y CR-06 dependen de entidades auxiliares y contexto parcial, no de etiquetas nativas del patrón de riesgo completo.

**Tabla 31**

*Cobertura de datos por condición y consecuencia metodológica*

| **Condición** | **Nivel de cobertura** | **Fuentes retenidas o apoyo** | **Uso metodológico definido** |
| --- | --- | --- | --- |
| CR-01 - Persona sin casco | Sólida | SHEL5K, CHV, construction_site_safety y ppe_siabar. | Integra el núcleo obligatorio y admite evaluación directa o composición por persona. |
| CR-02 - Persona sin chaleco reflectivo | Adecuada | CHV, construction_site_safety y ppe_siabar. | Integra el núcleo obligatorio, con menor redundancia que CR-01. |
| CR-03 - Trabajo en altura sin anticaídas | Brecha directa | Sin fuente retenida con la condición completa. | Sólo admite evidencia exploratoria sobre componentes o material complementario controlado. |
| CR-04 - Borde elevado desprotegido | Brecha directa | Sin fuente retenida con la condición completa. | Se mantiene como extensión condicionada y no bloquea la aceptación del núcleo. |
| CR-05 - Maquinaria cerca de peatones | Sin cobertura directa retenida | Requiere entidades relacionales y temporalidad. | Su evaluación depende de material específico y lógica contextual. |
| CR-06 - Persona en zona restringida | Sin cobertura directa retenida | Requiere polígono externo y cámara fija. | Su evaluación depende de parametrización espacial externa al prompt. |

*Nota.* La cobertura se refiere a la posibilidad de evaluar la condición operativa completa y no sólo a la presencia de algunas de sus entidades en una colección de imágenes.

Los benchmarks de referencia cumplen un papel más acotado. MOT17 puede utilizarse para verificar instrumentación y cálculo de métricas de seguimiento bajo un protocolo ampliamente conocido; OVT-B puede servir para observar integración entre open vocabulary y seguimiento. Ninguno de los dos se interpretará como evidencia directa de desempeño en construcción civil. Su valor es instrumental: permiten auditar módulos del sistema antes de reinsertarlos en el dominio objetivo.

Esta clasificación evita una sobre-declaración del alcance experimental. En particular, la presencia de entidades relacionadas con CR-03 o CR-04 en una colección de imágenes no habilita por sí sola la validación de la condición completa. Para esas condiciones, el protocolo sólo podrá reportar resultados completos cuando exista evidencia anotada sobre la combinación operativa requerida; de lo contrario, deberá distinguir entre detección de componentes visuales, prueba exploratoria de reglas espaciales y validación efectiva del patrón de riesgo.

La partición de datos se rige por cinco reglas obligatorias: el test set debe congelarse antes de cualquier entrenamiento o augmentation; la baseline zero-shot y toda variante fine-tuned deben evaluarse sobre el mismo conjunto de test; los splits deben ser estrictamente disjuntos; la semilla y el procedimiento de partición deben registrarse; y toda anotación complementaria debe separar material de desarrollo y material de evaluación. Estas reglas sostienen la comparabilidad del protocolo.

Para las condiciones brechadas, la política de datos complementarios sigue un orden de preferencia conservador: primero curación y conversión de fuentes públicas compatibles; después anotación complementaria acotada sobre material estrictamente necesario; y sólo en último término producción específica de material controlado en el EBE. El objetivo es evitar que la expansión del corpus consuma el tiempo y la capacidad que el proyecto necesita reservar para integración, instrumentación y validación del sistema.

#### 17.1.7. Framework de métricas, viabilidad operativa y presupuesto de latencia

##### 17.1.7.1. Introducción y alcance

###### 17.1.7.1.1. Propósito y preguntas rectoras

La fundamentación teórica del proyecto E-OVRT-VDP identificó una brecha persistente entre las métricas académicas estándar y la evidencia operativa que debe ofrecer un sistema de alerta asistiva orientado a seguridad laboral. Aunque métricas como AP, HOTA y los indicadores convencionales de rendimiento del pipeline resultan necesarias para la comparabilidad técnica, por sí solas no permiten establecer si el sistema detecta, sostiene y transforma una condición de riesgo en una alerta con la oportunidad, la estabilidad y la trazabilidad requeridas por el dominio.

En ese marco, la presente sección responde a dos de las preguntas rectoras formuladas en la fundamentación teórica. En relación con P-E1-06, define el framework de métricas para evaluar de manera integral detección OVD, seguimiento multiobjeto, rendimiento del pipeline y desempeño operativo de alerta, junto con umbrales orientativos diferenciados por severidad. En relación con P-E1-01, operacionaliza el presupuesto de latencia admisible mediante una descomposición en componentes medibles y una estimación orientativa compatible con el perfil de hardware de referencia.

El alcance de la sección es metodológico. Define métricas, niveles de compromiso, criterios de aplicación, umbrales orientativos y requisitos mínimos de instrumentación y reporte, pero no implementa la medición en código ni ejecuta campañas experimentales. Esas tareas corresponden, respectivamente, a la instancia de análisis y diseño arquitectónico y a la validación experimental. Las definiciones formales de las métricas estándar pueden consultarse en las secciones correspondientes de la fundamentación teórica.

En consecuencia, el framework no debe interpretarse como una promesa de ejecución uniforme de todas las métricas definidas, sino como una matriz metodológica de aplicación condicionada. Cada métrica sólo será exigible cuando existan los datos, módulos, referencias de evaluación e instrumentación necesarios para calcularla de manera trazable. Cuando esas condiciones no se cumplan, la salida metodológicamente correcta será declararla como no ejecutada o no aplicable, indicando la causa.

##### 17.1.7.2. Alcance evaluativo y definición operativa de la latencia de alerta

A efectos evaluativos, se distinguen tres tramos temporales que no deben confundirse. El primero es Glass-to-Algorithm (G2A), que mide el intervalo entre la captura o lectura de un cuadro y la disponibilidad del resultado algorítmico asociado a ese cuadro. El segundo es Glass-to-Alert, que mide el intervalo entre el inicio anotado de una condición de riesgo y la generación de una alerta confirmada y registrada dentro del sistema. El tercero es glass-to-glass, que extiende la cadena hasta la visualización remota del video procesado (Axis Communications AB, s. f.; Bachhuber et al., 2018).

La presente sección concentra su validación primaria en el tramo Glass-to-Alert hasta la alerta confirmada y registrada dentro del sistema. En consecuencia, la métrica operativa principal es ⟦ECUACIÓN: no extraída — ver el .docx⟧, entendida como el tiempo entre el inicio anotado del evento y la generación de una alerta registrada luego de la evaluación del patrón correspondiente. Esta definición distingue la alerta de una detección aislada y la ubica como salida operativa trazable del sistema.

En las configuraciones que incluyan un trayecto instrumentado de consulta o notificación, se reportará adicionalmente ⟦ECUACIÓN: no extraída — ver el .docx⟧ como medida complementaria. Esta métrica extiende la medición hacia la disponibilidad de la alerta en el canal definido, pero no forma parte del núcleo evaluativo mínimo.

En este trabajo, la latencia interna hasta el registro de la alerta se identifica como t_alert-system; la extensión hasta un canal instrumentado se identifica como t_alert-notification. Ambas denominaciones deben conservarse sin intercambiar sus hitos de inicio y cierre.

Bajo esta convención, G2A se entiende como el subtramo instrumental del pipeline que va desde la captura o lectura del cuadro hasta la disponibilidad del resultado algorítmico. El tramo Glass-to-Alert integra, además de ese subtramo, los módulos de seguimiento y razonamiento que correspondan y, sobre todo, la ventana funcional de persistencia requerida para confirmar el patrón de riesgo. Esta delimitación permite separar con claridad la latencia estrictamente computacional de las demoras asociadas al trayecto de consulta, notificación, distribución o interpretación humana.

##### 17.1.7.3. Estructura del framework y criterios de viabilidad

El framework se organiza en torno a una jerarquía de métricas y a niveles de compromiso que permiten priorizar evidencia sin sobredimensionar el alcance experimental. La combinación de ambos ejes preserva el rigor metodológico y, al mismo tiempo, reconoce que no todas las métricas útiles son igualmente ejecutables dentro del prototipo experimental.

###### 17.1.7.3.1. Jerarquía de métricas

El framework distingue tres niveles de análisis, cada uno con su unidad de evaluación. El nivel de percepción evalúa detecciones por imagen contra las anotaciones de referencia. El nivel de estado observable por persona determina, para cada persona detectada, si el estado derivado —presencia o ausencia del elemento de protección— coincide con la referencia, componiendo geométricamente las entidades sin requerir identidades persistentes. El nivel de alerta temporal evalúa la alerta confirmada por episodio contra una referencia temporal anotada. Las métricas de detección alimentan el primer nivel; precision y recall por persona, el segundo; y las métricas operativas del apartado 17.1.7.5, el tercero.

La jerarquía del framework se organiza en tres niveles. El nivel primario reúne las métricas que capturan valor operativo directo para el prototipo: ⟦ECUACIÓN: no extraída — ver el .docx⟧, Tiempo a la Primera Detección (TTFD), Tasa de Detección Sostenida (SDR) y Precision/Recall por severidad. El nivel secundario reúne las métricas que explican el comportamiento del detector, del tracker y del pipeline sin constituir por sí mismas evidencia suficiente de valor operativo: AP@0.5, AP@[0.5:0.95], HOTA y los indicadores complementarios de MOT y desempeño computacional. El nivel transversal reúne las métricas de comparación entre variantes zero-shot y fine-tuned, siempre que existan baseline explícita, particiones disjuntas y soporte de datos suficiente.

La pertenencia de una métrica al nivel primario expresa su prioridad interpretativa, no su aplicabilidad automática. Una métrica primaria puede no ejecutarse si el escenario evaluado no dispone de eventos anotados, persistencia temporal, motor de patrones, severidad asignada o logs suficientes. En esos casos, la métrica conserva su rol dentro del framework, pero debe reportarse como no aplicable para esa corrida o condición específica.

Esta jerarquía tiene una consecuencia práctica: si los recursos experimentales no permitieran ejecutar todo el repertorio con la misma profundidad, el núcleo evaluativo del prototipo estará dado por las métricas primarias y por los diagnósticos mínimos del pipeline. Las métricas deseables o conceptuales conservan valor analítico y comparativo, pero no deben desplazar la evidencia central sobre capacidad de alerta.

###### 17.1.7.3.2. Niveles de compromiso

No todas las métricas definidas en esta sección asumen el mismo nivel de compromiso. Obligatorio designa métricas que el núcleo del prototipo experimental debe reportar para sostener sus conclusiones; deseable designa métricas que enriquecen el análisis, pero cuya omisión no invalida el experimento si se explicita la razón; conceptual designa tratamientos o extensiones metodológicas cuya formulación analítica es pertinente, aunque su evaluación empírica completa exceda el alcance experimental del prototipo.

El nivel de compromiso también depende del alcance efectivamente implementado. Una métrica puede ser obligatoria para condiciones evaluables mediante detección directa o indirecta ya instrumentada, y no resultar exigible allí donde todavía falten módulos de razonamiento contextual, anotación especializada o trayectos completos de notificación.

###### 17.1.7.3.3. Criterios de factibilidad experimental

Una métrica sólo se asumirá como obligatoria cuando cumpla simultáneamente cinco condiciones: necesidad operativa para responder la pregunta de validación del prototipo experimental; disponibilidad de ground truth o referencia verificable; existencia del módulo que produce la señal evaluada; instrumentación suficiente mediante timestamps, logs o exportación de resultados; y costo de anotación o procesamiento compatible con el proyecto. Bajo estos criterios, una métrica puede estar correctamente definida en el framework y, aun así, no corresponder en una corrida concreta. Esta distinción evita validar el prototipo con indicadores que los datos, el entorno o la implementación no permiten sostener.

##### 17.1.7.4. Métricas adoptadas

Las secciones siguientes presentan las familias de métricas seleccionadas para los tres planos del sistema evaluable: detección OVD, seguimiento multiobjeto (MOT) y rendimiento del pipeline. La selección no pretende agotar la literatura, sino establecer un conjunto defendible de métricas candidatas y niveles de compromiso coherentes con el alcance del prototipo.

###### 17.1.7.4.1. Métricas de detección OVD

La evaluación del componente de detección open-vocabulary adopta un subconjunto de las métricas estándar revisadas en el análisis de modelos OVD. AP@0.5 y Precision/Recall constituyen el núcleo mínimo por su interpretabilidad, su disponibilidad en herramientas de evaluación consolidadas y su utilidad para contrastar variantes zero-shot y fine-tuned. AP@[0.5:0.95] se conserva como métrica deseable de comparabilidad académica, mientras que NMS-AP permanece en plano conceptual por su valor analítico sobre vocabularios extensos y su menor prioridad operativa en el prototipo experimental. Pueden verse estas métricas en la Tabla D.1 del Anexo D.

###### 17.1.7.4.2. Métricas de seguimiento multiobjeto

La evaluación MOT recupera como base las métricas estándar desarrolladas en la el análisis de seguimiento multiobjeto, pero recalibra su nivel de compromiso según el alcance efectivo del prototipo experimental. En ese marco, HOTA se conserva como métrica de referencia académica, aunque su cálculo riguroso —al igual que DetA, AssA e IDF1— exige anotaciones cuadro a cuadro con identidades persistentes, por lo que estas métricas quedan como deseables sobre subsets específicamente preparados para MOT. MOTA, IDSW y fragmentación conservan valor diagnóstico complementario en esos mismos subsets.

Para el núcleo del prototipo experimental, la métrica más útil es ⟦ECUACIÓN: no extraída — ver el .docx⟧, incorporada en esta etapa como operacionalización propia y entendida como la diferencia de falsos positivos observada entre corridas equivalentes con y sin tracker habilitado. Su valor metodológico reside en estimar si el seguimiento reduce detecciones espurias o falsas alertas sin exigir ground truth de identidades. No obstante, su interpretación sólo es válida si la unidad de conteo del falso positivo se declara previamente y se mantiene constante durante la comparación.

El análisis de las métricas de seguimiento multiobjeto puede verse en la Tabla D.2 del Anexo D.

###### 17.1.7.4.3. Métricas de rendimiento del pipeline

El rendimiento del pipeline integrado constituye una familia de métricas propia, porque la utilidad del sistema no depende sólo de la calidad semántica de detección o seguimiento, sino también del comportamiento sostenido de la cadena completa. FPS efectivos, latencia G2A y consumo de recursos permiten interpretar cuellos de botella, estabilidad temporal y margen operativo del hardware disponible. El análisis de las métricas de rendimiento del pipeline queda desarrollado en la Tabla D.3 del Anexo D.

##### 17.1.7.5. Métricas operativas específicas del dominio

Las métricas estándar de detección, seguimiento y rendimiento aportan comparabilidad técnica, pero no alcanzan por sí solas para describir el valor operativo del sistema en seguridad laboral. En este dominio, no interesa únicamente si el modelo detecta objetos o atributos en un cuadro, sino si el prototipo puede reaccionar frente a una condición de riesgo, sostener evidencia temporal suficiente y transformar esa evidencia en una alerta trazable cuando corresponda.

Por ello, esta sección incorpora métricas operativas específicas del dominio: latencia de alerta, tiempo a la primera detección, tasa de detección sostenida y evaluación diferenciada por severidad. Su aplicación queda condicionada por la disponibilidad de secuencias temporales, eventos anotados, criterios de detección positivos previamente definidos e instrumentación suficiente. En consecuencia, estas métricas no deben interpretarse como aplicables a toda corrida experimental, sino como métricas ejecutables sólo cuando los datos y el alcance implementado permiten calcularlas de manera válida.

###### 17.1.7.5.1. Latencia de alerta (⟦ECUACIÓN: no extraída — ver el .docx⟧)

La latencia de alerta se evalúa principalmente mediante ⟦ECUACIÓN: no extraída — ver el .docx⟧. Esta métrica no mide una detección aislada, sino la capacidad del prototipo para transformar evidencia visual en una alerta confirmada y registrada dentro del sistema.

Por lo tanto, ⟦ECUACIÓN: no extraída — ver el .docx⟧ sólo corresponde cuando la corrida incluye, como mínimo, detección OVD, evaluación de patrón, confirmación del patrón y registro interno de la alerta. Una detección temprana puede contribuir a la alerta, pero no la constituye por sí misma si no satisface los criterios de persistencia, severidad o activación definidos para el patrón evaluado.

En pruebas puramente cuadro a cuadro, donde sólo se evalúa la salida del detector OVD sin evaluación de patrón ni alerta registrada, no corresponde reportar ⟦ECUACIÓN: no extraída — ver el .docx⟧. En esos casos, el análisis debe limitarse a métricas de detección, rendimiento del pipeline o latencia Glass-to-Algorithm (G2A), declarando explícitamente la no aplicación de métricas de alerta.

Cuando la configuración evaluada incluya un trayecto instrumentado de consulta, exposición o notificación, se reportará adicionalmente ⟦ECUACIÓN: no extraída — ver el .docx⟧ como medida complementaria. Esta métrica no forma parte del núcleo mínimo de validación de la alerta, porque depende de componentes de interfaz o comunicación que pueden variar según el diseño arquitectónico adoptado.

###### 17.1.7.5.2. Tiempo a la primera detección (TTFD)

El Tiempo a la Primera Detección, o TTFD, mide el tiempo transcurrido entre el inicio anotado de una condición de riesgo y la primera detección positiva válida producida por el sistema, según el criterio declarado para la corrida. A diferencia de ⟦ECUACIÓN: no extraída — ver el .docx⟧, esta métrica no requiere confirmación por persistencia, evaluación completa del patrón ni generación de alerta. Su función es medir la rapidez con la que el sistema produce la primera evidencia perceptiva asociada a una condición nueva.

TTFD debe interpretarse como una métrica de reacción inicial y no como una métrica de alerta. Una primera detección temprana puede ser útil para reducir la latencia operativa posterior, pero no implica por sí sola que exista un patrón de riesgo confirmado ni una alerta válida dentro del sistema. La transición desde TTFD hacia ⟦ECUACIÓN: no extraída — ver el .docx⟧ depende de que las detecciones posteriores satisfagan los criterios de persistencia, severidad o activación definidos para la condición evaluada.

Esta métrica resulta especialmente informativa en eventos de severidad crítica o alta, donde interesa conocer cuánto tarda el sistema en producir la primera señal visual relevante. Sin embargo, su aplicación requiere que el evento tenga un inicio temporal anotado y que el criterio de detección positiva esté definido previamente. En datasets estáticos de imágenes, o en evaluaciones sin secuencia temporal ni inicio de evento identificable, TTFD no corresponde como métrica operativa y debe declararse como no aplicable.

###### 17.1.7.5.3. Tasa de detección sostenida (SDR)

La Tasa de Detección Sostenida, o SDR, mide la proporción del intervalo anotado de una condición de riesgo durante la cual el sistema mantiene detecciones positivas, según el criterio definido para la corrida. Su función es evaluar la estabilidad temporal de la evidencia, no la generación de una alerta.

En el protocolo, SDR permite distinguir entre una detección puntual y una condición sostenida. Una detección aislada puede no ser suficiente para confirmar un patrón de riesgo; por eso, esta métrica aporta evidencia sobre la persistencia necesaria para alimentar la lógica de confirmación del patrón.

SDR sólo corresponde cuando existe una secuencia temporal con inicio y duración anotados de la condición evaluada. En datasets estáticos de imágenes, o en evaluaciones sin ventana temporal identificable, la métrica no resulta aplicable y debe declararse como tal.

###### 17.1.7.5.4. Condición de aplicación de métricas temporales

Las métricas ⟦ECUACIÓN: no extraída — ver el .docx⟧, TTFD y SDR sólo son ejecutables sobre secuencias temporales donde pueda identificarse el inicio de la condición de riesgo, su duración efectiva y la respuesta temporal del sistema. No corresponde calcularlas sobre datasets compuestos únicamente por imágenes estáticas no ordenadas temporalmente.

En esos casos, la evaluación debe limitarse a métricas de detección por imagen o por cuadro, como AP@0.5 y Precision/Recall, además de métricas de rendimiento del pipeline cuando exista instrumentación suficiente. Las métricas temporales quedan reservadas para clips, secuencias anotadas o corridas EBE con eventos definidos.

###### 17.1.7.5.5. Evaluación diferenciada por severidad

No todos los errores del sistema tienen el mismo impacto operativo. Por ello, el framework adopta como obligación mínima el reporte de Precision y Recall por severidad, o por grupos de condiciones con severidad homogénea, acompañado por el tamaño muestral correspondiente.

Esta evaluación sólo corresponde cuando la severidad haya sido asignada previamente a la condición, patrón o evento evaluado. Si la severidad no fue definida de forma explícita, Precision y Recall podrán reportarse por condición de riesgo, pero no como métricas diferenciadas por severidad.

La asignación formal de pesos distintos a falsos positivos y falsos negativos se mantiene en plano conceptual. Aunque puede ser metodológicamente útil para reflejar diferencias de impacto operativo, depende de criterios de política de riesgo que exceden el alcance del prototipo experimental.

##### 17.1.7.6. Protocolo comparativo entre variantes preentrenada y ajustada al dominio

La comparación entre la variante preentrenada y la variante ajustada al dominio (fine-tuned) debe entenderse como un protocolo evaluativo condicionado, no como un resultado garantizado. Su finalidad es determinar si el ajuste al dominio aporta mejoras medibles sin comprometer la validez experimental ni degradar de manera no controlada la capacidad open-vocabulary del modelo. En ese marco, toda variante ajustada al dominio requiere una baseline zero-shot explícita, evaluada previamente sobre el conjunto de evaluación reservado. Esa baseline constituye el punto de referencia mínimo de toda comparación. En ausencia de baseline zero-shot, soporte de datos suficiente o separación estricta entre entrenamiento y evaluación, el contraste entre variantes no corresponde como evidencia metodológicamente válida. La separación estricta entre datos de entrenamiento y evaluación es condición de validez experimental y deberá quedar formalizada en la estrategia de datos, benchmarks y partición. Asimismo, la selección de checkpoints no debe hacerse sobre el conjunto de evaluación ni sobre clips o cuadros reutilizados en la línea base o baseline. Toda corrida comparativa deberá conservar el mismo conjunto de evaluación y la misma configuración experimental, salvo la variable que se busque aislar. Cuando exista una variante ajustada y soporte de datos suficiente para una condición de riesgo determinada, se reportarán los deltas ΔAP, ΔRecall, ΔPrecision y ΔSDR respecto de la baseline zero-shot. Los deltas sobre ⟦ECUACIÓN: no extraída — ver el .docx⟧ y TTFD se consideran deseables cuando la condición evaluada permita medirlos con trazabilidad suficiente. Del mismo modo, resulta deseable verificar si el ajuste al dominio degrada la capacidad open-vocabulary sobre categorías externas al entrenamiento mediante un subset generalista separado del dominio específico.

Toda ejecución de ajuste al dominio debe documentar horas-GPU, tiempo total, horas-persona, cantidad de imágenes y criterios de selección del checkpoint. Sin ese contexto, la ganancia observada pierde interpretabilidad como insumo para decisiones metodológicas.

**Tabla 32**

*Métricas y criterios de reporte para la comparación entre variantes*

| **Métrica** | **Qué captura** | **Relación con métricas estándar** | **Compromiso** | **Nivel** |
| --- | --- | --- | --- | --- |
| ΔAP, ΔRecall, ΔPrecision, ΔSDR por CR-XX | Ganancia del fine-tuning respecto de la baseline zero-shot. | Diferencia entre variantes | Obligatorio si aplica | Transversal |
| Δtalert, ΔTTFD | Verifica que el ajuste al dominio no degrade ⟦ECUACIÓN: no extraída — ver el .docx⟧ ni la respuesta inicial. | Diferencia entre variantes | Deseable | Transversal |
| AP generalista post fine-tuning | Retención de capacidad abierta fuera del dominio de entrenamiento. | Comparación sobre subset generalista | Deseable | Transversal |
| Costo de entrenamiento | Horas-GPU, tiempo total, horas-persona e imágenes utilizadas. | Registro documental | Obligatorio si hay fine-tuning | Transversal |

*Nota.* Δ = diferencia respecto de la baseline zero-shot. La expresión «si aplica» indica que la métrica sólo se exige cuando existe una variante ajustada al dominio, una baseline zero-shot explícita, soporte de datos suficiente y partición estrictamente disjunta entre entrenamiento y evaluación. AP generalista post fine-tuning refiere a la retención de capacidad open-vocabulary fuera del dominio de ajuste.

##### 17.1.7.7. Presupuesto de latencia y componentes medibles

La latencia de alerta se trata aquí como un presupuesto descomponible en componentes observables. En este marco, G2A representa el subtramo instrumental del pipeline por cuadro, mientras que ⟦ECUACIÓN: no extraída — ver el .docx⟧ operacionaliza la latencia de alerta hasta su confirmación interna. En las configuraciones que incluyan un trayecto instrumentado de notificación, se considerará además ⟦ECUACIÓN: no extraída — ver el .docx⟧.

###### 17.1.7.7.1. Descomposición operativa

La descomposición temporal adoptada es la siguiente:

⟦ECUACIÓN: no extraída — ver el .docx⟧

⟦ECUACIÓN: no extraída — ver el .docx⟧

⟦ECUACIÓN: no extraída — ver el .docx⟧

Aquí, ⟦ECUACIÓN: no extraída — ver el .docx⟧ representa la ventana funcional de persistencia necesaria para confirmar el evento, no un costo de cómputo en sentido estricto. El modelo es deliberadamente aditivo y conservador: aunque en una implementación real pueden existir solapamientos, buffering o paralelismo, la descomposición lineal sigue siendo útil para instrumentar mediciones, detectar cuellos de botella y comparar configuraciones.

###### 17.1.7.7.2. Componentes medibles y adscripción por tramo

La descomposición temporal presentada en la subsección anterior sólo resulta metodológicamente útil si cada componente queda adscrito a un tramo evaluativo preciso. En ese marco, la presente tabla no fija valores cerrados por componente, sino que organiza qué partes del retardo pertenecen al subtramo instrumental G2A, cuáles integran la confirmación interna de la alerta operacionalizada como ⟦ECUACIÓN: no extraída — ver el .docx⟧ y cuál corresponde, cuando exista, al trayecto adicional de notificación expresado por ⟦ECUACIÓN: no extraída — ver el .docx⟧. Su función es guiar la instrumentación mínima del sistema efectivamente implementado y evitar que se mezclen costos computacionales, ventanas funcionales de evidencia y demoras externas de interfaz o distribución.

**Tabla 33**

*Componentes del presupuesto de latencia y adscripción a G2A,* ⟦ECUACIÓN: no extraída — ver el .docx⟧ *y* ⟦ECUACIÓN: no extraída — ver el .docx⟧

| **Componente** | **Criterio orientativo** | **Variables dominantes** | **Tramo** | **Compromiso** |
| --- | --- | --- | --- | --- |
| ⟦ECUACIÓN: no extraída — ver el .docx⟧ | Debe medirse como parte del origen temporal de la corrida. | Sensor, buffer de captura, FPS de origen. | G2A | Obligatorio |
| ⟦ECUACIÓN: no extraída — ver el .docx⟧ | Debe medirse sobre el mecanismo de suministro efectivamente utilizado, ya sea red, stream o lectura local instrumentada. | RTSP/WebRTC, RTT, buffering, codificación/decodificación e I/O de lectura. | G2A | Obligatorio |
| ⟦ECUACIÓN: no extraída — ver el .docx⟧ | Incluye transformaciones de entrada y, cuando corresponda, transferencias entre CPU y GPU. | Resize, normalización y movimiento CPU-GPU. | G2A | Obligatorio |
| ⟦ECUACIÓN: no extraída — ver el .docx⟧ | Debe medirse por modelo y resolución; suele concentrar la mayor carga computacional. | Arquitectura OVD, resolución, caching de embeddings. | G2A | Obligatorio |
| ⟦ECUACIÓN: no extraída — ver el .docx⟧ | Corresponde a la ventana funcional de persistencia necesaria para confirmar el evento; no debe confundirse con un costo de cómputo. | Severidad, regla de persistencia, duración mínima del evento y frecuencia de muestreo. | ⟦ECUACIÓN: no extraída — ver el .docx⟧ | Obligatorio cuando exista confirmación por persistencia |
| ⟦ECUACIÓN: no extraída — ver el .docx⟧ | Sólo corresponde si hay tracker. | Método MOT, matching, cantidad de objetos. | ⟦ECUACIÓN: no extraída — ver el .docx⟧ | Obligatorio si hay tracker |
| ⟦ECUACIÓN: no extraída — ver el .docx⟧ | Debe distinguirse de ⟦ECUACIÓN: no extraída — ver el .docx⟧ y medirse como costo computacional de las reglas aplicadas. | Reglas de persistencia, lógica espacial, patrones activos. | ⟦ECUACIÓN: no extraída — ver el .docx⟧ | Obligatorio si existe |
| ⟦ECUACIÓN: no extraída — ver el .docx⟧ | Sólo aplica en configuraciones que incluyan un trayecto instrumentado de notificación hacia interfaz, cliente o canal externo. | MQTT/HTTP/WebSocket, cola de eventos, cliente e interfaz. | ⟦ECUACIÓN: no extraída — ver el .docx⟧ | Deseable |

*Nota.* La tabla organiza los componentes del presupuesto y explicita a qué tramo pertenece cada uno: G2A, ⟦ECUACIÓN: no extraída — ver el .docx⟧ o ⟦ECUACIÓN: no extraída — ver el .docx⟧. No fija valores cerrados por componente; su función es guiar la instrumentación y la interpretación del retardo sobre el sistema efectivamente implementado. La inclusión explícita de ⟦ECUACIÓN: no extraída — ver el .docx⟧ responde a que la latencia de alerta confirmada no se reduce al costo computacional del pipeline, sino que incorpora además la ventana funcional necesaria para acumular evidencia suficiente antes de registrar una alerta interna.

###### 17.1.7.7.3. Consideración sobre el razonamiento temporal

El componente ⟦ECUACIÓN: no extraída — ver el .docx⟧ debe distinguirse explícitamente de ⟦ECUACIÓN: no extraída — ver el .docx⟧. El primero corresponde al costo computacional asociado a la evaluación de reglas de persistencia, asociaciones espaciales y patrones activos una vez disponibles las detecciones. El segundo corresponde al tiempo funcional que el sistema requiere para acumular evidencia suficiente antes de confirmar una alerta. Esta distinción es metodológicamente central, porque evita interpretar la latencia de alerta confirmada como si fuera únicamente un problema de rendimiento computacional: ⟦ECUACIÓN: no extraída — ver el .docx⟧ integra el presupuesto computacional del sistema, mientras que ⟦ECUACIÓN: no extraída — ver el .docx⟧ integra el presupuesto operativo de confirmación que queda absorbido por ⟦ECUACIÓN: no extraída — ver el .docx⟧.

###### 17.1.7.7.4. Cierre operativo del presupuesto

En términos operativos, G2A abarca ⟦ECUACIÓN: no extraída — ver el .docx⟧, ⟦ECUACIÓN: no extraída — ver el .docx⟧, ⟦ECUACIÓN: no extraída — ver el .docx⟧ y ⟦ECUACIÓN: no extraída — ver el .docx⟧. La latencia de alerta hasta su confirmación interna, operacionalizada mediante ⟦ECUACIÓN: no extraída — ver el .docx⟧, agrega, según la configuración evaluada, ⟦ECUACIÓN: no extraída — ver el .docx⟧, ⟦ECUACIÓN: no extraída — ver el .docx⟧ y la ventana funcional ⟦ECUACIÓN: no extraída — ver el .docx⟧. El trayecto de notificación hacia interfaz, cliente o canal externo debe tratarse como una extensión adicional del sistema, expresada mediante ⟦ECUACIÓN: no extraída — ver el .docx⟧, y no como condición para validar el núcleo del prototipo experimental.

###### 17.1.7.7.5. Estimación orientativa del presupuesto de latencia

La descomposición presentada permite construir una estimación orientativa del presupuesto de latencia sin confundir el rendimiento por cuadro del subtramo G2A con la latencia de alerta confirmada expresada por ⟦ECUACIÓN: no extraída — ver el .docx⟧. Esta estimación no reemplaza la calibración empírica de la validación experimental, sino que funciona como referencia de plausibilidad para interpretar los umbrales de la Sección 17.1.7.7.6 y verificar que las metas de ⟦ECUACIÓN: no extraída — ver el .docx⟧ resulten consistentes con el hardware de referencia.

Tomando como perfil de referencia el hardware de inferencia documentado en el entorno experimental, infraestructura y escenarios de evaluación, puede asumirse como orientación inicial un rango de 10 a 50 ms para ⟦ECUACIÓN: no extraída — ver el .docx⟧ + ⟦ECUACIÓN: no extraída — ver el .docx⟧ en una LAN controlada y configurada para baja latencia. Ese orden de magnitud es consistente con la literatura relevada en el análisis de operación en tiempo real, donde la captura a 30 fps impone un piso del orden de un período de cuadro y los protocolos orientados a entornos IP controlados —en particular RTSP/RTP— se presentan como alternativas operativamente convenientes en redes locales cuando el buffering se mantiene acotado (Axis Communications AB, s. f.; Bachhuber et al., 2018). Para ⟦ECUACIÓN: no extraída — ver el .docx⟧, un rango de 5 a 20 ms constituye una estimación de ingeniería razonable para operaciones de redimensionado, normalización y, cuando corresponda, transferencia entre CPU y GPU sobre cuadros de 640 px; no debe interpretarse como una banda cerrada directamente respaldada por un benchmark único, sino como una aproximación plausible para el perfil experimental adoptado. Para ⟦ECUACIÓN: no extraída — ver el .docx⟧, conviene tratar el rango de 15 a 150 ms como una banda orientativa de ingeniería para inferencia local acelerada, apoyada en dos referencias complementarias. Por un lado, la el análisis de operación en tiempo real identifica un rango de 10–30 ms por cuadro asociado a modelos ligeros optimizados y otro de 50–150 ms característico de arquitecturas transformer sin optimización específica para edge; por otro, la el análisis de modelos OVD documenta ejemplos concretos dentro de la familia OVD eficiente, como YOLOE-v8-S (3,3 ms) y YOLOE-v8-L (9,8 ms) sobre T4 con TensorRT, YOLO-World-L (19,2 ms) sobre V100 sin TensorRT, y variantes optimizadas como OmDet-Turbo-Base (10 ms) y G-DINO 1.5 Edge (13,3 ms) sobre A100 con TensorRT (Cheng et al., 2024; Wang et al., 2025). En este punto, la mención de YOLO-World debe leerse únicamente como referencia comparativa dentro de la subfamilia eficiente de detectores OVD, no como modelo priorizado del protocolo experimental de E2, cuyos candidatos de trabajo siguen siendo YOLOE y Grounding DINO. Para ⟦ECUACIÓN: no extraída — ver el .docx⟧, un rango de 5 a 20 ms constituye una estimación conservadora y plausible para trackers ligeros de familia tracking-by-detection. En la literatura de referencia del proyecto, SORT se presenta como un método orientado a muy baja carga computacional y ByteTrack como una alternativa que preserva viabilidad en tiempo real dentro de sistemas de seguimiento más completos (Bewley et al., 2016; Zhang et al., 2022); sin embargo, esos valores no deben interpretarse como una cota universal del tracker aislado, sino como órdenes de magnitud útiles para un presupuesto experimental favorable. Para ⟦ECUACIÓN: no extraída — ver el .docx⟧ con reglas simples de persistencia y lógica espacial, un valor menor a 10 ms sigue siendo una estimación de ingeniería plausible, sujeta a verificación empírica.

Bajo estos supuestos, el tramo estrictamente computacional desde la captura hasta la disponibilidad de evidencia utilizable para alerta puede ubicarse orientativamente en el orden de 35 a 250 ms por cuadro cuando se emplean OVD eficientes, red local de baja latencia, tracker ligero y reglas simples. ⟦ECUACIÓN: no extraída — ver el .docx⟧, sin embargo, incorpora además ⟦ECUACIÓN: no extraída — ver el .docx⟧: para severidad crítica, una persistencia orientativa de 2 a 4 s combinada con ese presupuesto computacional vuelve metodológicamente coherente el objetivo de 3 a 5 s; para severidad alta y media, ventanas funcionales más largas hacen igualmente plausibles objetivos orientativos de 5 a 10 s y 10 a 20 s, respectivamente.

El presupuesto precedente corresponde, por tanto, a un escenario favorable de inferencia local sin cuello de botella severo de red y con una familia de modelos optimizada para tiempo real. En este marco, los rangos asignados a ⟦ECUACIÓN: no extraída — ver el .docx⟧ y ⟦ECUACIÓN: no extraída — ver el .docx⟧ deben interpretarse como estimaciones de ingeniería plausibles, pero no como bandas cerradas directamente respaldadas por la bibliografía citada; su validación definitiva corresponde a la calibración empírica de la validación experimental. Si el hardware efectivo difiriera significativamente del perfil de referencia —por ejemplo, por el uso de modelos más pesados, resolución de entrada superior a 640 px o protocolos de transporte con mayor latencia—, los umbrales de la siguiente sección deberán recalibrarse antes de operar como criterio de aceptación.

###### 17.1.7.7.6. Umbrales orientativos por nivel de severidad

La taxonomía de severidad definida en la taxonomía de condiciones de riesgo, patrones y prompts exige interpretar los umbrales de aceptación de manera diferenciada según la urgencia de la condición, la persistencia requerida para confirmarla y la tolerancia relativa a falsos positivos y falsos negativos. Los valores que siguen son orientativos: ordenan la evaluación del prototipo y deberán recalibrarse en la validación experimental con el throughput efectivo del pipeline. Los umbrales de TTFD se fijan por debajo de las ventanas orientativas de persistencia para preservar su función como métrica de responsividad inicial y evitar que quede absorbida por el tiempo total de confirmación de la alerta.

**Severidad crítica.** Corresponde a condiciones con potencial de escalada rápida hacia daño grave. Se prioriza minimizar falsos negativos y, por lo tanto, sostener ventanas cortas de confirmación y tiempos exigentes tanto para TTFD como para ⟦ECUACIÓN: no extraída — ver el .docx⟧.

**Severidad alta.** Corresponde a condiciones donde la exposición sostenida incrementa de forma significativa el riesgo, aunque con un margen de intervención algo mayor. Se admite un compromiso intermedio entre rapidez, estabilidad y control de falsas alarmas.

**Severidad media**. Corresponde a condiciones con riesgo latente o de escalada más lenta. En este nivel puede exigirse mayor evidencia antes de confirmar la alerta, con menor tolerancia a falsos positivos y ventanas funcionales de persistencia más largas.

Una lista de los umbrales orientativos por severidad puede verse en la Tabla D.4 del Anexo D.

##### 17.1.7.8. Operacionalización de la medición y condiciones de no aplicación

Para que el framework sea ejecutable y no meramente declarativo, la presente sección traduce las métricas anteriores a requisitos mínimos de instrumentación, preparación y registro. Su propósito no es redefinir las métricas, sino fijar las condiciones bajo las cuales su medición resulta metodológicamente defendible.

###### 17.1.7.8.1. Reglas generales de instrumentación

Toda corrida debe declarar, como mínimo, modelo, versión, checkpoint, variante, resolución de entrada, hardware, entorno de software, protocolo o mecanismo de suministro de video, umbral de confianza, configuración de NMS, vocabulario activo, ventana de persistencia y presencia o ausencia de tracker. Las corridas comparativas deben ejecutarse sobre el mismo conjunto de clips o cuadros y con igual configuración experimental, salvo la variable que se busque aislar. En las corridas que involucren fine-tuning, la semilla de partición, el identificador del split y la composición del corpus deberán quedar registrados de manera explícita para permitir regeneración y auditoría del contraste experimental. Las métricas temporales deben usar timestamps monotónicos, consistentes a lo largo del pipeline y con fuente temporal explícitamente declarada.

En las corridas integradas que reporten métricas de alerta, la instrumentación deberá registrar además los hitos temporales asociados a la evaluación del patrón. Como mínimo, deberán conservarse el timestamp de la detección o evidencia positiva inicial, el timestamp de inicio del patrón candidato cuando corresponda, el timestamp de confirmación del patrón, el timestamp de registro interno de la alerta y, si aplica, el timestamp de disponibilidad, consulta o notificación externa. Estos hitos deben provenir de logs trazables y utilizar una fuente temporal coherente con el resto del pipeline. Sin estos registros, no corresponde reportar ⟦ECUACIÓN: no extraída — ver el .docx⟧ ni ⟦ECUACIÓN: no extraída — ver el .docx⟧; sólo podrán reportarse métricas de detección, rendimiento o reacción inicial, según corresponda.

Toda medición debe incluir un período de calentamiento previo. Las métricas temporales se reportarán, como mínimo, con P50, P95 y P99, además del promedio, salvo que el tamaño muestral no lo permita. Si una métrica depende de ground truth específico inexistente o insuficiente, la salida correcta es declararla no ejecutada, no improvisar una aproximación. Esto se desarrolla de manera más sintética en la Tabla D.5 del Anexo D.

###### 17.1.7.8.2. Alcance efectivo y casos en los que no corresponde medir

El compromiso efectivo de cada métrica depende de la condición de riesgo, del escenario de evaluación y de los módulos realmente implementados e instrumentados. En el alcance metodológico ya consolidado del prototipo experimental, CR-01 y CR-02 constituyen el núcleo evaluativo obligatorio por su cobertura de datos y operacionalización directa, mientras que CR-03 a CR-06 permanecen condicionadas a la disponibilidad de evidencia visual, razonamiento contextual e instrumentación suficiente. En consecuencia, las métricas asociadas a condiciones condicionadas podrán ejecutarse de manera parcial o declararse no aplicables sin comprometer la validez del núcleo del prototipo experimental, siempre que esa decisión quede explícitamente justificada en el reporte.

No corresponde medir HOTA, DetA / AssA, IDF1, MOTA, IDSW ni fragmentación sin ground truth con identidades persistentes. Tampoco corresponde comparar variantes zero-shot y fine-tuned si no existe baseline zero-shot explícita o si la partición train/eval no es estrictamente disjunta. En esos casos, la métrica o comparación debe declararse como no aplicable, no como resultado omitido.

En el caso de las métricas de alerta, no corresponde medir ⟦ECUACIÓN: no extraída — ver el .docx⟧ si la configuración evaluada no incluye evaluación de patrón ni registro interno de alerta confirmada. En pruebas puramente cuadro a cuadro, donde sólo se evalúa la salida del detector OVD, las métricas aplicables son las de detección, rendimiento del pipeline o latencia algorítmica. La ausencia de una cadena operativa instrumentada debe declararse explícitamente como condición de no aplicación de las métricas de alerta.

Del mismo modo, no corresponde medir ⟦ECUACIÓN: no extraída — ver el .docx⟧ si la configuración evaluada no incluye un trayecto instrumentado de consulta o notificación, o si dicho trayecto no genera timestamps confiables. Esta métrica sólo debe reportarse cuando la alerta registrada pueda vincularse con un hito posterior verificable de disponibilidad, entrega o consulta en el canal definido.

Tampoco corresponde medir TTFD, SDR ni ⟦ECUACIÓN: no extraída — ver el .docx⟧ sobre imágenes estáticas, datasets sin continuidad temporal o corridas donde no se haya anotado el inicio y fin del evento. No corresponde medir Precision/Recall por severidad si la severidad no fue asignada previamente por condición o evento. No corresponde reportar deltas de fine-tuning si la baseline zero-shot no fue ejecutada sobre el mismo conjunto de evaluación o si existe filtración entre entrenamiento y test. Estas restricciones no reducen el valor del framework; delimitan su aplicación válida.

Una métrica que no corresponde medir se reporta con su estado y su causa —por ausencia de referencia, por fuente sin temporalidad o por trayecto no instrumentado—, nunca como cero ni por omisión.

###### 17.1.7.8.3. Precisiones operativas sobre métricas críticas

En ⟦ECUACIÓN: no extraída — ver el .docx⟧, la unidad de conteo del falso positivo deberá declararse antes de medir —detección por cuadro, evento de alerta o sesión consolidada— y mantenerse idéntica en ambas corridas comparativas. Además, ambas corridas deberán conservar igual configuración experimental, salvo la activación o desactivación del tracker.

Una re-alerta o reconfirmación asociada al mismo episodio no se computa como falso positivo; se registra y se reporta por separado para no confundir repetición de salida con una detección espuria.

En TTFD, la primera evidencia positiva no se confunde con la alerta confirmada. Debe declararse explícitamente qué cuenta como primera evidencia positiva —umbral de confianza, criterio de matching y cualquier filtro previo aplicado—. La definición elegida para la corrida debe permanecer estable y quedar registrada en la bitácora.

En ⟦ECUACIÓN: no extraída — ver el .docx⟧ y ⟦ECUACIÓN: no extraída — ver el .docx⟧, el hito temporal de cierre debe quedar definido antes de medir. En el primer caso, corresponde al registro interno de la alerta generado luego de la confirmación del patrón evaluado; en el segundo, a la emisión, disponibilidad o consulta verificable de la notificación en el trayecto instrumentado. Para que la medición sea válida, los logs deben permitir reconstruir la secuencia mínima entre primera evidencia positiva, patrón candidato si corresponde, patrón confirmado y alerta registrada. Si alguno de estos hitos no se instrumenta de manera confiable, la métrica de alerta debe declararse no aplicable.

En SDR, el criterio de cálculo —tiempo o cuadros válidos— debe declararse explícitamente. Si el throughput resulta inestable, conviene privilegiar el cálculo en tiempo por sobre el conteo puro de cuadros.

En Precision/Recall por severidad, los resultados deben acompañarse del tamaño muestral utilizado, del criterio de agrupamiento aplicado y del punto operativo o umbral con el que fueron calculados, evitando mezclar severidades en una misma lectura agregada.

Los resultados se reportan por estrato y escenario, nunca únicamente como agregado. Los materiales sin la condición objetivo no ingresan en precision, recall ni F1; su métrica es el conteo de falsos positivos. La SDR sólo se compara entre corridas con la misma cadencia de muestreo. La latencia de alerta no se compara entre densidades de evidencia distintas sin controlar qué episodios continúan siendo evaluables.

###### 17.1.7.8.4. Registro mínimo por corrida y reporte

Todo reporte deberá conservar contexto experimental suficiente para reproducir e interpretar la corrida. Como mínimo, la bitácora debe registrar identificación, modelo, entrada, parámetros, hardware y entorno de software, temporalidad y logs, resultados y observaciones.

Antes del reporte final debe verificarse que cada métrica corresponda al alcance implementado, que las corridas comparativas usen el mismo conjunto de evaluación y que la instrumentación incluya período de calentamiento previo, duración suficiente y conservación y trazabilidad de logs crudos y artefactos de evaluación. Asimismo, toda métrica no ejecutada deberá declararse junto con la razón metodológica o instrumental de su omisión.

##### 17.1.7.9. Síntesis parcial del framework de métricas

La evidencia central del prototipo no puede reducirse a métricas académicas de detección o seguimiento. Debe mostrar si el sistema detecta una condición relevante, la sostiene durante el tiempo requerido y la transforma en una alerta dentro de un margen compatible con su severidad. Por eso el protocolo diferencia métricas obligatorias, deseables y conceptuales: AP y Precision/Recall se conservan como base de detección, HOTA, IDF1 y CLEAR MOT como métricas de seguimiento cuando exista anotación suficiente, y NMS-AP como referencia conceptual para evaluaciones OVD de vocabulario fino (Everingham et al., 2010; Lin et al., 2014; Bernardin & Stiefelhagen, 2008; Ristani et al., 2016; Luiten et al., 2021; Yao et al., 2024).

La jerarquía de métricas no implica que todas deban ejecutarse en todos los escenarios ni sobre todas las condiciones de riesgo. Cada métrica queda subordinada a un criterio de ejecutabilidad experimental: debe existir una referencia de evaluación suficiente, el módulo que produce la señal correspondiente, instrumentación confiable mediante logs o timestamps, y una salida exportable para análisis posterior. Por esta razón, el protocolo diferencia entre métricas definidas, métricas efectivamente medibles y métricas no aplicables.

**Tabla 34**

*Jerarquía de métricas adoptadas para el prototipo experimental*

| **Plano** | **Métricas obligatorias** | **Métricas deseables o conceptuales** | **Condición de aplicación** |
| --- | --- | --- | --- |
| OVD | AP@0.5; Precision/Recall con criterio de reporte explícito. | AP@[0.5:0.95] como deseable; NMS-AP como conceptual. | Aplicable a toda condición efectivamente evaluada con ground truth de detección. |
| MOT | ⟦ECUACIÓN: no extraída — ver el .docx⟧ cuando el tracker esté integrado. | HOTA, DetA, AssA, IDF1, MOTA, IDSW y Frag sobre subsets anotados. | Sólo aplica cuando exista tracker y, para las métricas estándar, anotación temporal suficiente. |
| Pipeline | FPS efectivos; ⟦ECUACIÓN: no extraída — ver el .docx⟧; uso de VRAM. | Jitter; uso de GPU, RAM y CPU. | Obligatorio en toda corrida integrada. |
| Alerta | ⟦ECUACIÓN: no extraída — ver el .docx⟧; TTFD; SDR; Precision/Recall por severidad cuando exista evento anotado. | ⟦ECUACIÓN: no extraída — ver el .docx⟧, si existe trayecto instrumentado de consulta o notificación. | Obligatorio cuando exista evento anotado, criterio de activación definido, evaluación de patrón y alerta registrada dentro del sistema. |

*Nota.* ⟦ECUACIÓN: no extraída — ver el .docx⟧= Glass-to-Algorithm. TTFD = Time to First Detection. SDR = Sustained Detection Rate. Lo no implementado o no instrumentado debe declararse como no aplicable y no quedar implícitamente omitido.

La latencia operativa principal es ⟦ECUACIÓN: no extraída — ver el .docx⟧, definida como el intervalo entre el inicio anotado de la condición de riesgo y la generación de una alerta confirmada y registrada dentro del sistema. Esta métrica integra la inferencia, la persistencia requerida y la evaluación del patrón. No corresponde reportarla en pruebas puramente cuadro a cuadro donde sólo se evalúa la salida del detector OVD. En esos casos, el análisis debe limitarse a métricas de detección, rendimiento del pipeline o latencia Glass-to-Algorithm. Cuando exista un trayecto instrumentado hacia consulta, interfaz o notificación, podrá reportarse adicionalmente ⟦ECUACIÓN: no extraída — ver el .docx⟧ como métrica complementaria.

TTFD mide el tiempo hasta la primera detección positiva válida desde el inicio anotado del evento. SDR mide la proporción del intervalo del evento durante la cual el sistema sostiene detecciones positivas. Ambas métricas sólo corresponden sobre secuencias temporales con inicio y duración anotados. No deben calcularse sobre datasets de imágenes estáticas sin continuidad temporal.

**Tabla 35**

*Umbrales orientativos por severidad para la lectura operativa de la alerta*

| **Severidad** | ⟦ECUACIÓN: no extraída — ver el .docx⟧ **máximo orientativo** | **TTFD máximo** | **SDR mínima orientativa** | **Lectura operativa** |
| --- | --- | --- | --- | --- |
| Crítica | 3-5 s | < 1 s | >= 0.50 | Se prioriza no omitir eventos críticos y se admite menor estabilidad inicial. |
| Alta | 5-10 s | < 3 s | >= 0.60 | Se busca equilibrio entre rapidez de respuesta y estabilidad. |
| Media | 10-20 s | < 10 s | >= 0.70 | Puede exigirse mayor evidencia antes de confirmar la alerta, con mayor tolerancia temporal. |

*Nota.* Los valores son orientativos y deberán calibrarse con la evidencia de validación experimental. En consolidación metodológica su función es ordenar prioridades y criterios de lectura, no fijar universales del dominio.

Finalmente, todo reporte experimental deberá conservar trazabilidad mínima de la corrida: modelo, prompts, dataset o fuente de video, parámetros, módulos habilitados, hardware, timestamps, métricas calculadas y métricas no aplicadas con su causa. Esto permite distinguir entre resultado negativo, falta de instrumentación y no aplicabilidad por alcance experimental.

Además del framework de métricas, cada ejecución deberá conservar una bitácora mínima: identificación de corrida, modelo y checkpoint, dataset o clip utilizado, resolución efectiva, parámetros relevantes, timestamps de etapas críticas, consumo de recursos y observaciones. Esta bitácora garantiza que la evidencia de validación experimental pueda reconstruirse, auditarse y discutirse.

#### 17.1.8. Protocolo experimental integrado

##### 17.1.8.1. Secuencia general del protocolo

La secuencia experimental busca evitar que decisiones tardías alteren la validez comparativa del estudio. Ninguna fase que modifique el estado del modelo o del conjunto de datos debe ejecutarse antes de congelar el software relevante, los checkpoints retenidos, el test set y la estructura mínima de bitácora. Sobre esa base, el protocolo se ordena en fases sucesivas y no como un conjunto abierto de ensayos sin jerarquía.

En cada corrida, el conjunto de métricas aplicables deberá definirse antes de la ejecución según el tipo de evidencia disponible. En DBE sobre imágenes estáticas se priorizarán métricas de detección por imagen o cuadro; las métricas temporales —TTFD, SDR y talert-system— quedarán reservadas para secuencias o corridas con eventos anotados e instrumentación suficiente. Del mismo modo, las métricas de seguimiento sólo serán exigibles sobre subconjuntos con identidades persistentes o en análisis ablativos previamente definidos.

**Tabla 36**

*Fases del protocolo experimental integrado*

| **Fase** | **Objetivo** | **Salida esperada** | **Criterio de cierre** |
| --- | --- | --- | --- |
| Preparación | Congelar entorno, versiones, checkpoints, datasets retenidos y estructura mínima de bitácora. | Artefactos y configuración de corrida documentados. | Reproducibilidad básica garantizada. |
| Baseline DBE | Medir cada modelo candidato en zero-shot sobre el test set congelado. | Línea base por condición, prompt y métrica obligatoria. | Predicciones exportadas y métricas primarias calculadas. |
| Sensibilidad de prompts | Comparar familias de prompts y congelar la formulación primaria por condición. | Matriz comparativa y selección justificada. | Prompt principal y variantes de contraste definidos. |
| Pipeline y seguimiento | Medir tG2A, FPS, recursos y aporte del tracker. | Diagnóstico del comportamiento integrado. | Logs temporales y métricas de estabilidad disponibles. |
| Fine-tuning condicionado | Ejecutar adaptación al dominio sólo si se cumplen las condiciones metodológicas fijadas. | Variante comparativa exportada al CPN. | Comparación válida respecto de baseline y test compartido. |
| EBE complementario | Ejecutar captura continua en entorno controlado o simulado. | Evidencia de plausibilidad operativa y latencia integrada. | Eventos, timestamps y alertas registradas. |
| Reporte | Integrar métricas aplicadas, métricas no aplicables y causas de exclusión. | Informe de resultados trazable y replicable. | Se explicitan alcance, límites y condiciones de interpretación. |

*Nota.* La baseline zero-shot y el test congelado constituyen la base sobre la que recién puede discutirse el valor de prompts, seguimiento o ajuste al dominio. La secuencia expresa dependencias entre fases, no un calendario; el orden y las fechas efectivas de ejecución se documentan en la implementación.

#### 17.1.9. Estrategia de adaptación al dominio

##### 17.1.9.1. Criterio metodológico general

La adaptación al dominio se mantiene como una rama comparativa progresiva y condicionada. No se adopta como requisito previo para demostrar la viabilidad del enfoque OVD, porque eso convertiría una hipótesis todavía no probada en un supuesto metodológico. La baseline zero-shot es el punto de partida obligatorio; el fine-tuning sólo se habilita cuando existe soporte de datos suficiente y cuando la comparación puede sostenerse sin romper la integridad del protocolo.

##### 17.1.9.2. Candidatos de comparación y condiciones de decisión

En términos operativos, la comparación se concentrará como máximo en dos candidatos principales —Grounding DINO y YOLOE— por representar compromisos distintos entre expresividad semántica y eficiencia de inferencia (Liu et al., 2024; Wang et al., 2025). La decisión final sobre cuál o cuáles serán ajustados dependerá de la factibilidad real de integración, exportación y ejecución sobre el CPN, y no sólo de su rendimiento reportado en benchmarks generales.

La rama se define para su ejecución como una jornada experimental completa con criterios prerregistrados: una única baseline, márgenes fijados antes de evaluar y un veredicto determinado por reglas de aceptación previamente declaradas. Sus condiciones de habilitación son de datos y de protocolo, no de disponibilidad de cómputo; el TN constituye el recurso de entrenamiento y el CPN conserva la referencia operativa.

**Tabla 37**

*Regla metodológica de decisión para la adaptación al dominio*

| **Regla** | **Decisión adoptada** | **Sentido metodológico** |
| --- | --- | --- |
| Existencia de baseline | Ningún ajuste se evalúa sin baseline zero-shot previa sobre el mismo test. | Sin baseline explícita no existe comparación defendible. |
| Disponibilidad de datos | Se priorizan CR-01 y CR-02; CR-03 y CR-04 quedan fuera del camino ordinario mientras no exista cobertura suficiente. | El ajuste debe concentrarse donde puede producir evidencia útil y comparaciones metodológicamente válidas. |
| Integridad comparativa | El test set debe ser compartido y permanecer congelado. | Evita leakage y falsas mejoras por cambio de evaluación. |
| Ganancia exigible | La variante ajustada debe mostrar una mejora operativamente significativa y no una ventaja marginal difícil de sostener. | Protege al protocolo de ciclos costosos de ajuste con retorno metodológico débil. |
| Costo operativo | La variante ajustada no debe comprometer materialmente la latencia ni el presupuesto de recursos del CPN. | Una mejora semántica que destruye la viabilidad operativa no fortalece al prototipo. |

*Nota.* La regla no prescribe que el fine-tuning deba ejecutarse; define cuándo vale la pena hacerlo sin distorsionar el objetivo principal del prototipo experimental.

#### 17.1.10. Supuestos, riesgos de validez y consideraciones ético-legales

##### 17.1.10.1. Política de minimización y uso asistivo

El marco ético-legal del proyecto se apoya en una política de minimización de datos y de uso asistivo del sistema. Cuando la evaluación utilice datasets públicos o material pregrabado sin nuevas capturas, el requisito central será respetar licencias, condiciones de acceso y límites de uso académico. Cuando el proyecto genere material propio para el EBE, deberán adoptarse salvaguardas de finalidad explícita, acceso restringido, retención acotada y ausencia de reconocimiento de identidad personal o tratamiento biométrico, conforme al régimen argentino de protección de datos personales y videovigilancia (Argentina, 2000; Disposición 10/2015, 2015). Ese régimen prevé, además, la inscripción de las bases de datos con datos personales ante la autoridad de aplicación (AAIP); su aplicabilidad al material experimental del proyecto y el recaudo adoptado se documentan a continuación.

[[PENDIENTE: definir con el equipo la aplicabilidad de esta inscripción al contexto experimental y documentar el recaudo adoptado en §17.1 y §17.4.]]

##### 17.1.10.2. Supuestos de interpretación

También conviene fijar con claridad los supuestos de interpretación. Primero, el prototipo es un sistema asistivo: una alerta no equivale a una sanción ni a una determinación automática de incumplimiento normativo. Segundo, la evaluabilidad de varias condiciones depende de variables no controlables del todo por el detector, como escala aparente, ángulo de cámara, oclusión o iluminación. Tercero, CR-06 presupone una parametrización espacial externa al prompt y no debe evaluarse como si el lenguaje por sí solo definiera la zona restringida. Cuarto, el EBE constituye una validación en entorno simulado o controlado, no un despliegue real en obra.

**Tabla 38**

*Riesgos metodológicos y operativos relevantes para las instancias siguientes*

| **Riesgo** | **Impacto probable** | **Mitigación adoptada** |
| --- | --- | --- |
| La configuración retenida excede el presupuesto de VRAM o rompe la latencia esperada del CPN. | Alto | Priorizar variantes ejecutables en la laptop, ajustar resolución y composición del vocabulario activo y justificar toda optimización sobre el CPN. |
| Persisten brechas de datos para condiciones de Niveles 2 y 3. | Alto | Mantener esas condiciones como extensiones condicionadas y producir datos complementarios sólo si no desplazan el núcleo del prototipo experimental. |
| El tracker agrega complejidad sin reducir falsas alarmas. | Medio | Medir primero ΔFPtracking y sólo exigir métricas MOT completas en subsets donde el costo de anotación esté justificado. |
| El diseño experimental se vuelve inmanejable por exceso de variables combinadas. | Alto | Sostener un diseño reducido con condición base, barridos acotados y prueba de mayor exigencia sólo sobre la configuración retenida. |
| La generación de material propio introduce dudas de privacidad o de consentimiento. | Medio | Aplicar minimización, acceso restringido y registro explícito de finalidad y condiciones de captura. |

*Nota.* La mitigación forma parte del diseño metodológico. En varios casos, preservar validez implica acotar el alcance antes que incrementar complejidad sin evidencia suficiente.

#### 17.1.11. Conclusiones parciales de la consolidación metodológica

##### 17.1.11.1. Cierre del alcance metodológico

La consolidación metodológica queda cerrada con un protocolo experimental integrado, consistente con las dimensiones desarrolladas y ajustado al alcance real del prototipo. Ese cierre se expresa en seis definiciones principales: núcleo obligatorio centrado en condiciones de detección directa de Nivel 1; separación entre comparación controlada en DBE y plausibilidad operativa en EBE; estrategia de datos y partición orientada a evitar leakage; framework de métricas centrado en valor operativo de alerta; regla explícita para habilitar o descartar adaptación al dominio; y proyección metodológica que ordena el pasaje hacia diseño, implementación y validación.

##### 17.1.11.2. Articulación con las instancias de diseño e implementación

Las definiciones consolidadas en esta instancia orientan directamente las etapas siguientes del trabajo. El análisis y diseño arquitectónico transforma el protocolo metodológico en una organización técnica consistente, mientras que la validación experimental produce resultados sobre las condiciones, escenarios y métricas fijadas. En todos los casos, deberá declararse qué elementos del catálogo fueron implementados, cuáles no aplicaron y cuáles permanecieron condicionados. Esa trazabilidad entre definición metodológica, diseño, implementación y validación constituye el principal resultado de esta parte del proyecto.

Esta consolidación distribuye sus salidas hacia las instancias siguientes sin anticipar resultados: la caracterización del entorno restringe la arquitectura y sus perfiles de ejecución; las condiciones de riesgo y el protocolo de prompts determinan configuraciones y comparaciones; la estrategia de datos gobierna la curación, la partición y la trazabilidad durante la implementación; y el framework de métricas define la instrumentación de ⟦ECUACIÓN: no extraída — ver el .docx⟧, ⟦ECUACIÓN: no extraída — ver el .docx⟧ y los criterios con los que se interpreta la evaluación.

**Alcance experimental consolidado**. Establece la frontera inicial del prototipo experimental y permite priorizar el núcleo obligatorio sin convertir las extensiones condicionadas en requisitos bloqueantes. En la etapa de diseño, orienta qué capacidades deben implementarse primero y cuáles deben quedar previstas como ampliaciones posibles. En la validación, define qué condiciones integran el plano principal de evaluación y evita interpretar capacidades exploratorias como resultados plenamente validados.

**Escenarios e infraestructura**. Fijan el marco operativo en el que deberá interpretarse la viabilidad del sistema. Para el diseño arquitectónico, esto implica organizar la captura, el procesamiento y el eventual entrenamiento alrededor de los roles funcionales CPN, EN y TN. Para la validación, permite diferenciar la lectura de resultados entre DBE y EBE, evitando mezclar la estabilidad de una evaluación basada en datos controlados con la variabilidad propia de una captura o transmisión continua.

**Estrategia de datos y partición**. Condiciona la selección de datasets, la construcción de particiones experimentales y el uso de datos complementarios. Su función es sostener la comparabilidad entre la línea base preentrenada y cualquier variante ajustada al dominio, evitando contaminación entre entrenamiento, validación y prueba. De esta manera, los resultados obtenidos podrán interpretarse como evidencia experimental y no como consecuencia de una partición inconsistente.

**Framework de métricas y registro**. Define qué evidencia mínima deberá producir el prototipo. En la etapa de diseño, guía la instrumentación de timestamps, logs, eventos, métricas por tramo y salidas del pipeline. En la validación, establece qué debe reportarse para analizar detección, rendimiento, latencia, persistencia temporal y alertas. Las métricas se reportarán cuando existan datos, módulos e instrumentación suficientes, y se declararán no aplicables cuando esas condiciones no estén presentes.

**Regla de adaptación al dominio**. Ordena la posible incorporación de fine-tuning o variantes ajustadas. Esta adaptación no constituye un punto de partida obligatorio, sino una comparación condicionada a la existencia de datos suficientes, partición válida y una línea base preentrenada previamente evaluada. Su propósito es permitir una lectura controlada de mejoras o degradaciones frente al enfoque zero-shot, sin sobredimensionar el alcance real del prototipo experimental.

**Supuestos y riesgos de validez**. Delimitan cómo deben interpretarse los resultados futuros. En el diseño, obligan a construir módulos y pruebas dentro del alcance declarado. En la validación, evitan extrapolar evidencia parcial como si constituyera una validación plena del sistema. Esta precaución preserva el carácter experimental del trabajo y mantiene la orientación central del proyecto: evaluar si la detección open-vocabulary puede integrarse como herramienta asistiva útil para el monitoreo de condiciones de riesgo en construcción civil, sin reemplazar la supervisión humana ni asumir decisiones operativas automáticas.

---

## Fuente: `docs/informe/entregable/96e-informe-v11-cierre-anexos-referencias.md`

> SHA-256 del bloque: `400305128d8f6cb5f6e208294f5089eedb182dc557fe109e803ed90adb08fde7`  
> Seleccion: Anexos C y D del informe v1.1 (texto vigente). Por D-E2-1 NO van en el .docx de la etapa: se corrigen aparte (AJ-2.07, duplicaciones de ajustes/09) y quedan en 90g para la seccion 19.

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

---

## Fuente: `docs/operacion/130-relevamiento-plataforma-pre-etapa-2.md`

> SHA-256 del bloque: `5f898b630cde3c9d490fd6c12c4272806695acd22111a47ef41e1a4a51505ae6`  
> Seleccion: relevamiento de la plataforma del 2026-08-28: la tabla prescripcion -> CUMPLIDA/PARCIAL/NO EJERCIDA/DESVIADA por subseccion de 17.1 (lo que se declara en 17.4/17.5 y lo que se ajusta como protocolo en 17.1) y las decisiones D-E2 firmadas.

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

## 5. Set documental — auditoría documento contra documento

Informe completo: `datos/130-relevamiento-pre-etapa-2/docs-set.md` (fuente: `docs/operacion/datos/130-relevamiento-pre-etapa-2/docs-set.md`)
(37 hallazgos nuevos además de los 12 de `revision-previa-etapa-2.md` §3: **6 🔴 · 13 🟠 · 18 🟡**;
26 llegan al kit porque su archivo es fuente del generador). Los 🔴:

| # | Dónde | Qué decía | Qué manda |
|---|---|---|---|
| 1 | `sintesis/fundamentos-teoricos.md` ~L605-616 | E-04 "NO-GO T1… último eslabón: full-authorization + RUN manual" | jornada cerrada (`123`/`127`/`128`) |
| 2 | `operacion/97` (foto 08-05) vendido como "ESTADO VIGENTE" por `00-indice` y GUIA | "4 repos", "dos servicios HTTP", "distribución MQTT no implementada"; sin un solo ✎ | 5 repos, tres servicios, distribución implementada y medida (118); superado por este doc |
| 3 | `informe/project-kit/README.md` | cuarto archivo de knowledge = `…17.3…v1.1.docx` / `…17.4…v1.2.docx` (no existen); tabla de estado con §17.4 v1.5; orden 6→1→2→0 | knowledge = contexto base + paquete de etapa + DOCX base de formato + `.docx` vigente de la sección (v1.0 / v1.0 / v1.4 / v1.6 / v1.3) |
| 4 | `generar_project_kit.py` L183 vs L143/`STAGE_CONTRACTS[1]` | "podas 01 a 11: NINGUNA aplicada" y "podas 01-11 aplicadas" en el mismo paquete | aplicadas (Etapa 1 cerrada) |
| 5 | `GUIA-REDACTORES.md` ~L117, ~L397 | "§17.4, §17.5 y §17.6 están vacías / desde cero" | 17.4 v1.6 y 17.5 v1.3 existen; falta 17.6 |
| 6 | `informe/ajustes/08-manual` L13 + tablero §5 + L26 + L129 | "109 unidades. Cero aplicadas", 100 % `[ ]`, "no existe script de extracción", "la vara no existe" | Etapa 1 cerrada con 16 AJ-1 + podas 01–11; 17.3/17.4/17.5 con pases aplicados; extractor y verificador existen; la vara está escrita |

**Contradicciones doc↔doc (mismo hecho, dos versiones)** — resueltas en §7: qué son los "cuatro
archivos" de knowledge · dónde nacen E-DIR/E-IND/E-HYB (D3/C-1 vs E3-42 → cerrado por D-E2-2) ·
estado del kit vs sus fuentes (generador "aplicado" vs tableros "cero") · podas 01–11 · containerización
"diferida" vs "definida" · verificador "19 cifras/16 campañas" vs 26/17 · acople de la distribución
(ADR-018 vs ADR-020 en `ajustes/04`) · plan de tablas de §17.5 (7 vs 6) · alcance de la Etapa 1 ("con
Anexo A" vs "sólo desarrollo") · banco "34 clips = resultado principal" vs 47/Bloque A. Enlaces
rotos: `00-el-informe-hoy` L223 (pase 5 → `archivado/`), `08-manual` L271, `project-kit/README`.

**Coinciden sin fisuras (no tocar):** campeón y `bench_v3`; 47/32/15/37; jornada E-04 cerrada (salvo
los dos ecos); cifras sólo de los 4 índices; L1–L8; G1 medida / MOT excluida; dos patrones / tres
servicios (salvo `operacion/97`); distribución verificada (p95 64,534 ms); autocontención y
marcadores; 17 tablas + 6 figuras; versiones vigentes v1.0/v1.4/v1.6/v1.3.

---

## 6. Decisiones firmadas hoy para la Etapa 2

| ID | Decisión | Firma |
|---|---|---|
| **D-E2-1** | El documento de trabajo de la etapa es **sólo §17.1**; los Anexos C y D se corrigen aparte y quedan en `90g` para el equipo (como el Anexo A en `90e`). | usuario, 2026-08-28 |
| **D-E2-2** | **Bautismo E-DIR / E-IND / E-HYB en §17.1.5.4.2** (C-1 del pase 1) y **recorte de la glosa de §17.3.6.4 a una remisión** (dependencia inversa de E3-42; §17.3 v1.4 → v1.5). | usuario, 2026-08-28 |
| **D-E2-5** | **Ficha nueva AJ-2.13**: el nivel intermedio "estado observable por persona" se declara en §17.1.7.3.1 como nivel de análisis (criterio de diseño, sin cifras), para que §17.5 tenga de dónde colgarlo. | usuario, 2026-08-28 |
| **D-E2-6** | MOT17/OVT-B (§17.1.6.3) y métricas MOT (§17.1.7.4.2) **intactos, con ⊘ explícito** en el pase; lo no ejercido se reporta en §17.5 bloque 7. | usuario, 2026-08-28 |
| D-E2-3 | AJ-2.02 se resuelve como **regla de conteo** en §17.1.7.8.3 (la re-emisión por confirmación repetida no cuenta como FP); §17.1 no menciona cooldown, la ficha tenía premisa falsa. | recomendación adoptada |
| D-E2-4 | AJ-2.01: los 4.000/7.000 ms entran en §17.1.5.3.3 como **decisión de protocolo dentro del rango de la Tabla 24**, sin tocar la tabla y sin la palabra "efectivos" (casa única de los valores efectivos: §17.4). | recomendación adoptada |
| D-E2-7 | AAIP: `[[PENDIENTE]]` espejo en §17.1.11.1 con el mismo texto de D-E1-11. | recomendación adoptada |
| D-E2-8 | PODA-14 sólo recorta §17.1.4 y verifica que lo recortado esté en B.1–B.7; lo que falte se lista como alta al Anexo B para el equipo. | recomendación adoptada |

---

---

## Fuente: `docs/informe/entregable/desarrollando/archivado/correcciones-etapa-3-4-5-pase-3.md`

> SHA-256 del bloque: `c93c9ad9419c3debd61a71f8cae6ed6fb14cef79d2a4154ee85a6e24e6dff812`  
> Seleccion: hechos del pase 3 que dependen de la etapa 2: CPN/EN/TN y las siglas t_alert-system/TTFD/SDR NACEN en 17.1 (17.3 las usa sin redefinir) - no moverlas ni renombrarlas.

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

---

## Fuente: `docs/informe/entregable/desarrollando/archivado/correcciones-etapa-3-4-5-pase-3.md`

> SHA-256 del bloque: `f6a1d8528fd9171a198d810b2d594fa61128021e2b67ac96b50eb0b64f077000`  
> Seleccion: dependencias inversas hacia la etapa 2: C-1 (bautismo E-DIR/E-IND/E-HYB, ahora firmado por D-E2-2), el solape 17.3.3.1/17.3.3.2 y la anomalia de la sigla OMML en 17.1.7.5.1.

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

## Fuente: `docs/informe/ajustes/02-etapa-2-consolidacion-metodologica.md`

> SHA-256 del bloque: `602bf6c6faca134a37359d0a681eaa44e46f354842a7a5e14e2fb3fd44efd44d`  
> Seleccion: documento completo.

# Etapa 2 — ajustes a la consolidación metodológica (§17.1) y a los Anexos C y D

> **Estado (2026-08-10):** relevado, **sin pase de correcciones aplicado**. El
> relevamiento es `nucleo/historicos/08-alineacion-consolidacion-metodologica.md`, que leyó el
> §17.1 completo contra lo que el proyecto construyó. Su §1 registra lo que el informe
> **valida y refuerza** (no se toca); su §2 las **desalineaciones**; su §4 las acciones.
> Este documento las convierte en ajustes con ID y las cruza con el estado real de hoy.
>
> **Particularidad de esta etapa:** varias desalineaciones **ya se resolvieron en el
> código** (el pattern set `cr01_cr02_v2` existe y es el oficial). Lo que queda
> pendiente es que **el informe lo diga** — el ajuste es documental, no de
> implementación. Están marcados 🛠️ *ya resuelto en código*.
>
> ✎ **2026-08-11 — regla de no-anacronismo (mapa, regla 5), aplicada a esta etapa:**
> el §17.1 es Etapa 2 y **se corrige como protocolo** — entran decisiones, definiciones
> y criterios (valores de configuración elegidos dentro de rangos declarados incluidos);
> **no entran resultados medidos** ni estados de implementación, que se reportan en
> §17.4/§17.5. Los ajustes AJ-2.05, AJ-2.09 y AJ-2.11 se reescribieron para respetar
> esa frontera.
>
> ✎ **2026-08-28 — LA ETAPA 2 ARRANCA. Este documento queda como tablero histórico; el pase que
> se aplica es `entregable/desarrollando/archivado/correcciones-etapa-2.md` (fuente: `docs/informe/entregable/desarrollando/archivado/correcciones-etapa-2.md`)
> (E2-01…E2-26, decisiones D-E2-1…9), que integra estas 12 fichas, agrega **AJ-2.13** y las
> podas 12–14, y MANDA donde difiera.** Texto base vigente: `entregable/90f` (el §17.1 del v1.1 sin
> correcciones, en su propio `.docx`); el `96b` queda como foto histórica. Fuente de los hechos:
> `operacion/130` (relevamiento de los cinco repos, 2026-08-28) y `revision-previa-etapa-2.md`.
> Cambios de estado de las fichas: **AJ-2.02 → ⊘** (premisa falsa: §17.1 no menciona cooldown ni
> re-alertas; la regla de conteo entra por AJ-2.12) · **AJ-2.04 → ⊘ para §17.1** (los tres ejes ya
> están en el protocolo; la ficha apuntaba a nuestro diseño de campañas) · **AJ-2.11 con el ✎
> vencido corregido** · **AJ-2.07 corregido** (el fine-tuning NO usó `chv`) · **AJ-2.09** (nombres de
> artefactos). Decisiones firmadas por el usuario: D-E2-1 (sólo §17.1 en el `.docx`), D-E2-2
> (bautismo E-DIR/E-IND/E-HYB en §17.1.5.4.2), D-E2-5 (AJ-2.13), D-E2-6 (MOT intacto con ⊘).
>
> ✅ **2026-08-28 (noche) — PASE APLICADO Y VERIFICADO: §17.1 v1.3** (`desarrollando/E-OVRT-VDP_Seccion_17.1_Consolidacion_Metodologica_v1.3.docx`,
> 28.534 palabras, verificador OK). Las 12 fichas + AJ-2.13 + podas 12–14 quedaron resueltas (⊘ para
> AJ-2.02 y AJ-2.04). Constancia y residuales: `desarrollando/archivado/correcciones-etapa-2-pase-2.md`.
> **No reaplicar nada de este tablero.**

| Dónde | Qué |
|---|---|
| Texto actual | `entregable/96b` (§17.1 Consolidación Metodológica + §17.2 Costos) · `entregable/96e` §19.3–19.4 (Anexos C y D) |
| Fuente del relevamiento | `nucleo/08` §1–§5 |
| Texto ya redactado | `material-etapa-3/94` §5 (diccionario de métricas, cubre `AJ-2.03`) |

---

## 1. Tablero de ajustes

| ID | Sección | Tipo | Pri | Enunciado |
|---|---|---|---|---|
| **AJ-2.01** | §17.1.5.3.3 / Tabla 24 | PRECISA | 🟠 | Severidades y ventanas: reportar los **valores efectivos** (`high`/4000 ms, `medium`/7000 ms) y que la persistencia se parametriza **en ms, no en frames**. 🛠️ |
| **AJ-2.02** | §17.1 (política de alerta) | CONTRADICE | 🔴 | El **cooldown no es del motor**: por ADR-011 la supresión de re-notificación es política del tramo de distribución. Y **`re_alerts` ≠ FP**. |
| **AJ-2.03** | §17.1.7 / Tabla 35 | CONCRETA | 🟠 | Diccionario de métricas con nombres, definiciones operacionales y umbrales — **más** las dos métricas derivadas propias, declaradas como descomposición. |
| **AJ-2.04** | §17.1.5.4.2/.5 | PRECISA | 🟠 | Ejes del protocolo de prompts que el diseño original no tenía: **vocabulario aislado vs completo**, variantes **template**, **hiperparámetros congelados**. |
| **AJ-2.05** | §17.1.5.4 | PRECISA | 🟡 | Piso muestral: **~200 instancias positivas por condición** o tamaño efectivo + IC. Declarar por cuál vía se cumplió. |
| **AJ-2.06** | §17.1.5.4.5 | EVIDENCIA | 🟠 | **Doble anotación ≥20% + kappa de Cohen: NO se hizo.** Hay que declararlo como decisión, y es la **limitación L2**. |
| **AJ-2.07** | §17.1.5.4 / Anexo C | PRECISA | 🟡 | El prompt set debe declararse construido desde el **Anexo C (Tabla C.1)**; sumar **confianza media de los TP** y **métricas por entidad componente**. |
| **AJ-2.08** | §17.1.6 / Tabla 36 | PRECISA | 🟡 | Usar los **nombres de fase de la Tabla 36** y declarar la correspondencia 1:1 con lo ejecutado (con la nota ADR-010). |
| **AJ-2.09** | §17.1.7.8 | CONCRETA | 🟠 | Instrumentación: los **cinco hitos por alerta**, **P50/P95/P99**, warm-up declarado por corrida, bitácora mínima. |
| **AJ-2.10** | §17.1.4.2.4 | PRECISA | 🟡 | Fuente EBE (H4): la **contingencia oficial se ejerció primero**; la OAK-D está integrada; el RTSP sintético es herramienta, no fuente experimental. |
| **AJ-2.11** | §17.1 / Tabla 37 | PRECISA | 🟡 | Reencuadrar el **fine-tuning (I1)** conforme **ADR-017**: rama experimental condicionada (Tabla 37) que **se ejerce como jornada completa**; condiciones de datos y protocolo, no de cómputo — la causa "presupuesto de tiempo" queda **prohibida**. |
| **AJ-2.12** | §17.1.7 | PRECISA | 🟠 | Declarar los **estados de aplicabilidad** (`not_applicable:<causa>`, ADR-006/013) y las **reglas de lectura** que ninguna métrica puede violar. ✎ 08-28: + la regla de conteo `re-alerta ≠ FP` (D-E2-3, E2-22). |
| **AJ-2.13** | §17.1.7.3.1 | CONCRETA | 🟠 | ✎ **2026-08-28 (D-E2-5, nueva):** declarar el **nivel intermedio de análisis "estado observable por persona"** entre la percepción por imagen y la alerta temporal por episodio — §17.5 lo usa como eje y §17.1 no lo pre-registraba (0 apariciones). Texto guía en E2-18. Sin cifras. |

---

## 2. Los ajustes, desarrollados

### AJ-2.01 · §17.1.5.3.3 y Tabla 24 · PRECISA · 🟠 · 🛠️ ya resuelto en código

**Qué pedía el informe.** La Tabla 24 fija PR-01 (CR-01, sin casco) severidad **Alto**,
persistencia **3–5 s**; PR-02 (CR-02, sin chaleco) severidad **Medio**, persistencia
**5–10 s**. Y §17.1.5.3.3 exige parametrizar la persistencia **en segundos, no en
frames** (la conversión depende del throughput).

**Qué había.** El control-plane usaba severidad `medium` para ambos y
`confirm_after_frames: 1`.

**Qué hay hoy.** El pattern set oficial **`cr01_cr02_v2`**: CR-01 `high` /
`confirm_after_ms: 4000`, CR-02 `medium` / `7000`, con histéresis
activación≠desactivación (`resolve_after_*`). El set con `confirm=1 frame` quedó como
**configuración de diagnóstico DBE-imágenes**, documentada como tal.

**El ajuste, entonces, es documental:** el §17.1 debe reportar los **valores efectivos**
y que caen dentro de los rangos declarados. Cruza con **R-14** en Etapa 3 (§17.3.8.2 y
Tabla 46), que es la ficha canónica de esos valores.

> ✎ **2026-08-28 (D-E2-4, E2-07):** en §17.1 los 4.000/7.000 ms (y 2.000/3.000 de desactivación)
> entran como **decisión de protocolo dentro del rango de la Tabla 24**, sin tocar la tabla y **sin
> la palabra "efectivos"**: por la doctrina de reparto (08-19) los valores efectivos viven sólo en
> §17.4 (`90b` los tiene; §17.3 v1.4 ya no). El puntero "Tabla 46" es de la numeración vieja de
> §17.3 (v1.4 renumeró a 39–55).

---

### AJ-2.02 · §17.1 · CONTRADICE · 🔴 — el cooldown no vive en el motor

**Por ADR-011 el motor emite en cada confirmación**; la supresión de re-notificación es
política del **tramo de distribución de alertas**, no de la evaluación de patrones.
Corolario que hay que escribir: **las `re_alerts` no son falsos positivos** — contarlas
como FP degrada artificialmente toda la precisión reportada.

Su ficha canónica es **R-02** (Tabla 44) en Etapa 3; acá se registra porque el §17.1
también describe la política de alerta y arrastra el mismo error.

> ⊘ **2026-08-28 — PREMISA FALSA (E2-26):** §17.1 **no menciona** cooldown, supresión, re-alertas ni
> re-notificación (0 apariciones en `90f`; el pase 2 de la Etapa 3 ya lo había verificado: *"cero
> apariciones en todo el capítulo de Etapa 2"*). Lo único cercano es la frase de la histéresis
> (§17.1.5.3.3, *"evita alertas repetidas"*), que E2-08 precisa. El corolario `re_alerts ≠ FP` entra
> como **regla de conteo** en §17.1.7.8.3 vía AJ-2.12/E2-22 (D-E2-3). Esta ficha se cierra como ⊘.

---

### AJ-2.03 · §17.1.7 y Tabla 35 · CONCRETA · 🟠 — el diccionario de métricas

**Adoptar los nombres del informe, textuales** — no hay que inventar nada, es
transcribir §17.1.7 + Tabla 35:

| Métrica | Definición | Nota |
|---|---|---|
| **G2A** (Glass-to-Algorithm) | captura/lectura del frame → resultado algorítmico. Componentes: `t_capture` + `t_transport` + `t_preprocess` + `t_inference` | presupuesto **50–250 ms** |
| **t_alert-system** | **inicio anotado del evento** → alerta confirmada y registrada. Integra G2A + `t_track` + `t_reasoning` + `T_persistencia` | métrica operativa **principal** |
| **t_alert-notification** | complementaria; solo con trayecto instrumentado | |
| **TTFD** | inicio anotado → primera detección positiva válida (criterio declarado) | |
| **SDR** | proporción del intervalo anotado con detecciones positivas sostenidas | |
| **ΔFP_tracker** | delta de FP con/sin tracker, unidad de conteo declarada | |

Reporte temporal mínimo: **P50/P95/P99 + promedio**, con warm-up previo declarado y
timestamps monotónicos de fuente explícita.

**Y hay que declarar las dos métricas derivadas propias** (spec 40 §5.2), que **no son
del informe**: `t_capture→alert` (captura del frame de primera evidencia → alerta
registrada) y `t_compute-budget` (= `t_capture→alert` − `T_persistencia_efectiva`).
**No sustituyen a `t_alert-system`: la descomponen.** Existen porque son las únicas
métricas end-to-end computables **sin GT**, lo que permitió validar el tramo plataforma
antes de que existiera el clip bench (ADR-010).

**El texto para esto ya está escrito**: `material-etapa-3/94` §5 (redline R-10).

> ✎ **2026-08-28 (E2-19, D-P3-4):** el reparto vigente es **§17.1 = nombres, definiciones y criterios**
> (ya están: G2A, Glass-to-Alert, `t_alert-system`, `t_alert-notification`, TTFD, SDR, ΔFP_tracker,
> Tablas 34/35) · **§17.3.13 (v1.4) = materialización** (relojes, señales, estados de aplicabilidad) ·
> **§17.4 = valores**. En §17.1 sólo se verifica consistencia terminológica. Las dos métricas
> derivadas (`t_capture→alert`, `t_compute-budget`) **NO se declaran**: ninguna sección del informe
> las usa (0 apariciones en `90`/`90b`/`90c`) — regla del aporte (D-E2-6 bis). El texto de `94` §5
> se escribió para §17.3.13, no para acá.

---

### AJ-2.04 · §17.1.5.4.2/.5 · PRECISA · 🟠 — los ejes del protocolo de prompts

El protocolo del informe (5 fases) exige tres cosas que el diseño de prompts original no
contemplaba:

1. **Contexto de vocabulario como variable**: cada prompt se evalúa **en aislamiento y
   en vocabulario completo**, porque prompts semánticamente próximos compiten. Aplicar
   al menos a las formulaciones finalistas.
2. **Variantes con template** (*"a photo of a [CLASS]"*) como eje de estructura
   sintáctica: sumar 1–2 variantes template al prompt set.
3. **Hiperparámetros congelados** (confianza y NMS constantes entre variantes de
   prompt): explicitarlo en la configuración de las corridas.

> ⊘ **2026-08-28 para §17.1 (E2-10):** verificado sobre `90f`, **los tres ejes ya están en el
> protocolo** (§17.1.5.4.2 "en aislamiento y en contexto completo", "a photo of a [CLASS]";
> §17.1.5.4.5 Fase 2 "hiperparámetros constantes"). La ficha apuntaba a lo que le faltaba a nuestro
> diseño de campañas (`nucleo/08` §2.3), no al informe. §17.1 no se edita; **§17.5 declara** lo
> ejercido: vocabulario en régimen asimétrico (E-DIR aislada, E-IND conjunta) sustituido por un
> control único (B1 vs T2); templates definidas (`cr01_template`/`cr02_template`) y **no medidas**;
> hiperparámetros `box 0,30 / text 0,25` idénticos en todos los brazos, umbrales operativos
> calibrados por brazo con grid idéntico (`operacion/130` §4.2).
>
> ✎ **2026-08-28 (D-E2-2, E2-09) — el bautismo E-DIR/E-IND/E-HYB SÍ va en §17.1.5.4.2**, en el
> párrafo "Estrategia de detección", con el texto guía de C-1 del pase 1 de la Etapa 3. **Dependencia
> inversa** (E3-42, pase 3 §I): §17.3.6.4 v1.4 debe recortar su glosa a una remisión; si no, el
> informe define los códigos dos veces.

---

### AJ-2.05 · §17.1.5.4 · PRECISA · 🟡 — el piso muestral

El protocolo pide **~200 instancias positivas por condición**, o bien reportar tamaño
efectivo **+ intervalos de confianza**. En **§17.1** el ajuste es declarar la vía
elegida como decisión de protocolo (IC por bootstrap) — **el n efectivo contra ese piso
se reporta en §17.5**, que es donde el n existe (regla de no-anacronismo, mapa regla 5).

---

### AJ-2.06 · §17.1.5.4.5 · EVIDENCIA · 🟠 — la doble anotación que no se hizo

El protocolo pide **≥20% doblemente anotado, kappa de Cohen para etiquetas e IoU para
cajas**, aplicable al clip bench y a cualquier anotación nueva de estado EPP.

**No se hizo.** Es la **limitación L2** de la lista canónica, y hay que escribirla como
decisión declarada, no omitirla. Hay un contrapeso que sí conviene reportar: la
**revisión ciega del GT del lote de internet** (2026-08-09) encontró que **5 de 7
declaraciones de episodio eran errores de anotación (~71%)** — evidencia directa, y
medida en el propio trabajo, de por qué el protocolo pedía doble anotación. Eso vive en
Etapa 5 como `AJ-5.07` y como tabla **T-84**.

> ✎ **2026-08-28 (E2-12):** en §17.1 el requisito **se conserva** y gana su **criterio de
> aplicabilidad** (cuando la referencia se reutiliza de anotaciones de fuente sin re-anotación, la
> doble anotación no aplica y la ausencia de acuerdo se declara como limitación del material);
> "no se hizo" es de §17.5. Dato nuevo del relevamiento: la **auditoría humana del GT de imágenes
> (Task 4.3) tampoco se ejecutó** — sólo su kit; `bench_gt_audit.md` §4–6 vacíos (`operacion/130`
> R-14). El informe **no debe afirmar** que hubo auditoría humana del GT de imágenes.

---

### AJ-2.07 · §17.1.5.4 y Anexo C · PRECISA · 🟡

- El catálogo de formulaciones candidatas vive en el **Anexo C (Tabla C.1)** del propio
  informe: el prompt set debe declararse **construido desde ahí**.
- Sumar **confianza media de los TP** como indicador de estabilidad por formulación.
- Para la estrategia indirecta, **métricas por entidad componente** (`person`, `helmet`,
  `vest` por separado) para atribuir la degradación — el bench ya las produce.

> ✎ **2026-08-18 — el Anexo C también trae el catálogo de DATASETS, y ahí hay dos
> precisiones que no son de esta ficha pero se escriben en la misma sección:**
> **(1)** hay que separar **candidatos evaluados** (la lista larga: SH17, Pictor-PPE,
> GDUT-HWD, SHWD, SODA, MOCS…, con por qué no se retuvieron) de **utilizados**, y dentro
> de utilizados distinguir los de **entrenamiento** (`construction_site_safety`, `chv`,
> `ppe_siabar`) de las **fuentes del banco de imágenes** (`construction_site_safety`,
> `chv`, `shel5k`) — comparten dos nombres de tres, y confundirlos es el error fácil.
>
> ⚠ ✎ **2026-08-28 — CORRECCIÓN (`operacion/130` R-02):** la lista de "entrenamiento" de arriba es
> el rol TRAIN **histórico** (`train_v2`, archivado el 08-15). El **entrenamiento efectivo**
> (`finetuning_v1`, T1 y T2) usó `construction_site_safety` 2.203 + `ppe_siabar` 743 = **2.946 / 483**
> y **EXCLUYÓ `chv`** por anti-leakage: el 100 % de sus 1.330 imágenes es estrato de `bench_v3`.
> Copiar la lista vieja al informe violaría su propia Tabla 28 (disyunción estricta). También:
> las licencias de la Tabla 26 se escriben **como están en el registro** (GDUT-HWD/SHWD "verificar";
> CHV sin licencia del dataset — L7; MOCS = copia pública de 1.471 imgs), y css/ppe_siabar entran al
> inventario como candidatos incorporados después del protocolo (E2-13/E2-14; anexos en `90g`).
> **(2)** `bench_obra` **no es un dataset**: es el estrato curado internamente a partir de
> `construction_site_safety`. Guía completa con la cadena de procedencia y una frase lista
> para el informe: **redline R-24** (`material-etapa-3/93`) y glosario `13` §4.4.

---

### AJ-2.08 · §17.1.6 y Tabla 36 · PRECISA · 🟡 — las fases

Usar los **nombres de fase de la Tabla 36** (Preparación · Baseline DBE zero-shot ·
Sensibilidad de prompts · Pipeline y tracking · Fine-tuning condicionado · EBE
complementario · Reporte) y declarar la correspondencia con lo ejecutado. Es coherencia
metodológica gratis.

**Con la nota de ADR-010:** las semanas del plan **no se leen literalmente** — vale la
correspondencia de fases y sus dependencias. Cruza con `AJ-0.03` (§14.2/§14.3).

---

### AJ-2.09 · §17.1.7.8 · CONCRETA · 🟠 — instrumentación

El informe exige, por alerta, cinco hitos con timestamp: **primera evidencia positiva ·
patrón candidato · confirmado · alerta registrada · notificación**. Estado real:

- El control-plane **persiste candidate/confirmed/alert** (`pattern_events.jsonl`) ✓
- **Falta explicitar la primera evidencia positiva** — es derivable del primer hit;
  dejarlo como campo del episodio.
- **Percentiles P50/P95/P99** en las métricas del control-plane (hoy solo promedio).
- **Warm-up declarado por corrida** (verificar en media-plane; N/A en replay).
- **Bitácora mínima por corrida** ≈ `report.json` consolidado + `effective_config`, ya
  cubierta. ✎ 2026-08-28: en el plano de medios los artefactos son `summary.json` +
  `metrics.jsonl` + `run_manifest.json` + `run_provenance.json` (**no** `report.json`/`metrics.json`,
  que son del consolidado del experimento). Estado real verificado (`operacion/130` §4.4): hitos
  **4 de 5** en el control (notificación en el distribuidor); percentiles P50/P95/P99 en
  `summary.json` de medios y control **pero `evaluate-alerts` sólo produce promedios**; hardware,
  SO y versiones **no se registran** por corrida; `warmup_units = 0` en todas las corridas
  (warm-up de modelo sí). Todo eso se declara en §17.4 (E2-21); §17.1.7.8 no cambia.

**Dónde aterriza cada cosa (no-anacronismo):** el §17.1.7.8 **ya exige** los cinco
hitos — como protocolo casi no se edita. Los bullets de "estado real" de arriba son el
**cumplimiento**, y eso se escribe en **§17.4** (qué se instrumentó, con sus huecos:
percentiles solo promedio, primera evidencia derivable). Su ficha canónica en Etapa 3 es
**R-25** (§17.3.11 Tabla 50 y §17.3.13), que trae el contrato de GT temporal y los cinco
hitos juntos — a nivel de *diseño*, que sí corresponde a esa etapa.

---

### AJ-2.10 · §17.1.4.2.4 · PRECISA · 🟡 — la fuente del escenario EBE

El informe define el nodo de captura candidato (**OAK-D Pro PoE**, integrada como fuente
`oak_d` del media-plane desde 2026-07-13) **con plan de contingencia oficial: cámara IP
convencional**. En la práctica **la contingencia se ejerció primero**. Actualizar la
prioridad declarada: contingencia oficial primero, y el **RTSP sintético
(mediamtx+ffmpeg) como herramienta de desarrollo y vía de reproducibilidad DBE↔EBE con
fuente idéntica** — no como fuente experimental.

---

### AJ-2.11 · §17.1 y Tabla 37 · PRECISA · 🟡 — el encuadre del fine-tuning

> ✎ **2026-08-11 — reescrito conforme
> ADR-017 (fuente: `docs/decisiones/adr-017-fine-tuning-jornada-experimental.md`)**; *decía "la
> exclusión es por presupuesto de tiempo y por secuenciación"* — esa causa queda
> **prohibida** en el informe.

Reformular citando la Tabla 37 **tal como está escrita**: la regla *"no prescribe que
el fine-tuning deba ejecutarse; define cuándo vale la pena"* — es decir, la rama es
**experimental y condicionada desde el diseño metodológico**, no una exclusión ni un
descarte. Aclarar que **el nodo de entrenamiento existe** (clúster Mendieta, CCAD-UNC)
y que las condiciones que gobiernan la rama son **de datos y de protocolo**. ✎ **Estado
2026-08-13:** F-100.1, freeze/smoke técnico, dual gate y serving real están cerrados;
permanecen D-FT-08/T-FT-005, evaluación T-FT-031 y baseline T-FT-032. La procedencia
T-FT-023 quedó CERRADA el 2026-08-13 (snapshot tar `639e60df…`). ✎ **2026-08-15:
D-FT-08/T-FT-005, D-FT-12 y D-FT-13 firmadas; T-FT-031 y T-FT-032 cerradas la misma jornada
(doc 120, baseline 26s one-shot). Resta sólo `full-authorization.json` + `RUN` manual.** Son gates
técnicos, **no una falta de cómputo ni de plazo**. La rama **se ejerce como jornada
completa** (ADR-017): escalera T1→T2/T3 con
sus criterios pre-registrados, documentando resultados y limitaciones. **En §17.1 va
la regla y su criterio**; la jornada, el **costo T1 por extrapolación medida: ≈16 min
centrales (prudente 30–45 min; walltime 2 h) — `operacion/100` adenda; la cifra
histórica “≈1 GPU-h” quedó superada**
y sus resultados son datos posteriores y se citan donde corresponde: §17.4 (estado a
la entrega), la sección comparativa de resultados (si la jornada produjo datos a la
entrega) y §18 (`AJ-6.05`: lo que quede más allá de la escalera) — regla de
no-anacronismo.

> ✎ **2026-08-28 — los ✎ del 08-13/08-15 de arriba están VENCIDOS** ("resta sólo
> `full-authorization.json` + RUN"): la jornada está **COMPLETA y CERRADA** — T1 NO-GO (08-17,
> `operacion/123`), T2 NO-GO (08-21, `127`), T3 cerrado con causa técnica; acta `128`. En §17.1 va
> **la regla y su criterio** (E2-23): la rama se ejerce como jornada completa con criterios
> pre-registrados, condicionada por datos y protocolo, nunca por cómputo ni plazo. Dos hechos
> nuevos para §17.4/§17.5 (no para §17.1): el split de entrenamiento fue de **2.946** imágenes contra
> el rango 500–2.000 de la Tabla 28 (**desviación sin justificar en ninguna bitácora**, E2-15), y los
> checkpoints ajustados **sólo se evaluaron en imágenes**, nunca en clips ni en EBE.

---

### AJ-2.12 · §17.1.7 · PRECISA · 🟠 — aplicabilidad y reglas de lectura

Dos cosas que el §17.1 no declara y que gobiernan todo el §17.5:

- **Estados de aplicabilidad**: una métrica que no aplica se reporta como
  `not_applicable:<causa>`, nunca como 0 ni omitida (ADR-006 / ADR-013).
- **Reglas de lectura no negociables** (familia F-EV): reportar **por estrato y
  escenario**, nunca solo el agregado · los clips negativos **no** entran a P/R/F1 (su
  métrica son los FP) · `re_alerts` ≠ FP · el **SDR no se compara entre cadencias** ·
  `t_alert` no se compara entre densidades sin control de supervivencia.

---

## 3. 🚫 Lo que no hay que tocar

1. **Los "nombres de métrica vacíos"** de §17.1.5.3.2, §17.1.7 y Tabla 33 **no son una
   errata del documento**: son objetos de ecuación de Word que la extracción XML no
   captura. En el Word original casi seguro se ven bien. **Verificar visualmente, no
   corregir.** (Esta es una autocorrección: se había reportado como errata en `nucleo/02`
   §4.8 y `nucleo/07`, y se retiró — `nucleo/08` §3.)
2. **Todo el §1 de `nucleo/08`** — lo que el informe **valida y refuerza**. El §17.1 es
   metodológicamente sólido; lo que tiene son desalineaciones puntuales y huecos de
   concreción, no un problema de fondo.
3. **La histéresis activación≠desactivación** ya estaba pedida por §17.1.5.3.3 y ya está
   soportada. No es un agregado nuestro: es cumplimiento.
4. ✎ 2026-08-28 — **§17.1.6.3 (MOT17/OVT-B) y §17.1.7.4.2 (métricas MOT)**: pre-registradas y no
   ejercidas; quedan **intactas con ⊘ explícito** (D-E2-6, E2-16). Lo no ejercido lo reporta §17.5.
5. ✎ 2026-08-28 — **CPN/EN/TN, TTFD/SDR/`t_alert-system` y §17.1.4.4**: nacen acá y §17.3/§17.4 los
   usan por nombre o por número. No renombrar, no renumerar (`correcciones-etapa-2.md` §D).

## 4. Fuentes

`nucleo/historicos/08-alineacion-consolidacion-metodologica.md` (§1 lo validado · §2.1–2.6 las
desalineaciones · §3 la autocorrección · §4 las acciones · §5 adenda de Anexos C y D,
leídos 2026-07-07) · `decisiones/adr-006`, `adr-010`, `adr-011`, `adr-013`, `adr-015` ·
`specs/40` §5.2 · `material-etapa-3/94` §5 · `gobierno/99` §4.1 (limitación L2).

---

## Fuente: `docs/informe/ajustes/07-critica-extension-y-poda.md`

> SHA-256 del bloque: `9eac33b95dff535adc583f1a881d979a6a456c996fb6c3035bc6d79e2342f474`  
> Seleccion: podas 12 a 14 aplicables a la seccion 17.1.

## 5. §17.1 Consolidación Metodológica (32.222 palabras)

**Advertencia previa:** este es el capítulo **mejor alineado** del informe — el
protocolo que describe se ejerció casi completo, y `nucleo/historicos/08` §1 documenta
que valida lo construido. La poda acá es quirúrgica, no estructural.

### PODA-12 · §17.1.6.2 Datasets de gestión directa (5.054) · C5 · 🔴
Un catálogo de 5.000 palabras de datasets, escrito **antes** de que la selección
colapsara a **3 datasets TRAIN** (`construction_site_safety`, `chv`, `ppe_siabar`) y un
benchmark (`bench_v3`, 3 fuentes) — y es exactamente lo que **R-24** marca como
inventario desactualizado. Comprimir a: ficha de los efectivamente usados + tabla de
descartados con causa (una línea cada uno). Se corrige y se poda en el mismo pase.
**Ahorro: ~3.000** · DECISIÓN → [ ]

### PODA-13 · §17.1.10 Proyección hacia instancias posteriores (637) · C4 · 🟡
Las "instancias posteriores" **ya ocurrieron** — son §17.4 y §17.5. Reemplazar por un
párrafo puente. **Ahorro: ~450** · DECISIÓN → [ ]

### PODA-14 · §17.1.4 Entorno e infraestructura (3.252) · C5 parcial · 🟡
Parámetros y detalle de infraestructura que el **Anexo B ya existe para alojar**
(1.792). Mover el detalle al anexo, dejar en el cuerpo el diseño de escenarios DBE/EBE.
**Ahorro neto: ~1.000** · DECISIÓN → [ ]

**Lo que NO se toca en §17.1:** §17.1.5 (9.426 — condiciones, patrones y protocolo de
prompts: es el protocolo que SÍ se ejerció; lo no ejercido de adentro —kappa/doble
anotación— se **declara**, AJ-2.06, no se borra) · §17.1.7 (6.605 — el framework de
métricas es la fuente del diccionario y de todo §17.5).

---

