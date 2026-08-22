# E-OVRT-VDP - paquete de etapa 4

> Generado el 2026-08-22. Etapa 4: seccion 17.4, implementacion del prototipo.

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
5. Rama de ajuste fino, **brazo T1: CERRADO con veredicto NO-GO** (2026-08-17). Los
   margenes se firmaron **antes** de la linea base, la corrida se ejecuto una vez y se
   evaluo una vez, y **el checkpoint ajustado no se adopta como modelo de servicio**.
   Tiene cifra medida y se escribe como **hallazgo, no como fracaso**: el ajuste rescata
   `bare_head` del cero absoluto (AP50 0,0000 -> 0,0455) pero **no alcanza el umbral**
   (faltaron 0,0045) y **rompe la retencion de `person`** (-11,62 %, tope 10 %). Va en
   tabla propia, por estrato, nunca mezclada con el nucleo zero-shot.

**ABIERTO — no se afirma; se marca:**

1. **Resultado del brazo T2**: no existe. T2 se reabrio como tier **exploratorio** por
   enmienda posterior al NO-GO (D-FT-14) y esta **enviado y en cola, sin empezar**; sus
   margenes ya estan firmados por adelantado (D-FT-15). No hay ninguna cifra de ese
   checkpoint y no la habra hasta que corra y se evalue: esa subseccion queda reservada
   con marcador. **T1 ya no es un hueco**: tiene resultado y se afirma (ver CERRADO 5).
2. **Cinco figuras sin producir** (vista de procesos, maquina de estados del motor,
   calidad frente a densidad, cuadro con alerta superpuesta y frontera de juzgabilidad).
   Se mencionan en el texto con marcador; no se describen como si existieran.
3. **Procedencia de origen del lote de obra real** (direccion y fecha de acceso por
   clip): pendiente. No bloquea redactar; si bloquea cerrar la version final.

### Convencion de marcadores (obligatoria)

Todo hueco se deja con doble corchete, de modo que sea localizable con una busqueda:

- `[[PENDIENTE: que falta · de que depende]]`
- `[[CIFRA: que cifra hace falta · de que indice saldria]]`
- `[[FIGURA: cual]]`

Reglas: nunca completar un marcador con una estimacion, un valor probable ni una
redaccion evasiva; nunca borrarlo para que el texto "fluya"; el marcador viaja hasta el
entregable y recien lo remueve quien aporta el dato. Un capitulo con marcadores visibles
es honesto; un capitulo que rellena huecos es indefendible.

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
- E-04/fine-tuning es una **rama comparativa separada y en curso**. F-100.1 esta
  resuelta. `1166583` cerro freeze/smoke tecnico con 12 tensores/3.096 parametros y
  optimizer 12/12; dual gate, serving real y **procedencia T-FT-023 (cerrada el
  2026-08-13, snapshot tar `639e60df...`)** estan verdes. **El 2026-08-15 el usuario firmo
  D-FT-08 (contrato de serving), D-FT-12 (objetivo y margenes go/no-go, firmada ANTES de
  la baseline) y D-FT-13 (derogacion de la sonda `machinery` solo para T1)**, T-FT-005
  quedo `done` y **no queda ninguna decision humana pendiente**. La misma jornada se
  cerraron **T-FT-031** (comando de evaluacion congelado + enforcement canonico v2 en
  config + catalogo finetuned) y **T-FT-032**: la **baseline YOLOE-26s corrio UNA vez
  sobre las 6.477 imagenes de `bench_v3`** (doc 120) — `bare_head` AP50 **0,000**
  (6.181 GT / 10 detecciones), recall CR-01 0,0167/0,0000 por fuente y **0,0002
  agregado**; retencion a proteger person 0,7843 / helmet 0,6286 / vest 0,2642. Estas
  cifras son **de la rama comparativa**: van SIEMPRE en tablas propias, por estrato, y
  NO se promueven a `results/` hasta cerrar la jornada; **no hay cifra del checkpoint
  ajustado** (no existe todavia) ✎ *superado el 2026-08-17: el checkpoint T1 SI tiene
  cifra — ver la enmienda al pie de esta vineta; el que sigue sin cifra es T2*.
  F-120.1: las latencias de ese run NO se citan (cambio
  de energia en curso); el gate de latencia se mide pareado aparte.
  **✎ 2026-08-15 (noche) — T1 full ENVIADO: T-FT-043 esta CERRADA.** La autorizacion se
  emitio y verifico en el cluster con sus 7 gates, el ensayo `--test-only` paso, y el
  `RUN` quedo **encolado como job `1167640`** (1 GPU / 10 CPU / 60 GB / 2 h). Al encolar
  figuraba en espera, con inicio estimado por el planificador el 2026-08-17; una
  estimacion del planificador **no es reserva ni promesa**, y el envio **no es un
  resultado**. Lo que sigue abierto es la corrida en si y, despues, la promocion del
  checkpoint por hash, su evaluacion unica y el veredicto go/no-go contra los margenes ya
  firmados. **Hasta que eso ocurra no existe ninguna cifra del modelo ajustado**: la
  subseccion correspondiente se deja con `[[PENDIENTE: ...]]`, jamas con un valor
  estimado ni con una redaccion que sugiera que la comparacion ya se hizo.
  La sonda de clase nueva (`machinery`) quedo **derogada para T1 y reasignada a T2/T3**
  por D-FT-13; en T2/T3, de vocabulario abierto, sigue siendo exigible.
  **✎ 2026-08-17 — la jornada T1 CERRO: veredicto NO-GO.** El job `1167640` corrio el
  16/08, el checkpoint se promovio por hash y se evaluo **una sola vez** contra
  `bench_v3`: `bare_head` AP50 **0,0000 -> 0,0455** (gate A pedia >= 0,05: **faltaron
  0,0045**) y la retencion de `person` cayo **0,7843 -> 0,6932 (-11,62 %, tope 10 %)**.
  **El checkpoint no se adopta.** Los margenes (D-FT-12) estaban firmados desde el 15/08,
  antes de la baseline, y **no se renegociaron**: eso es lo que hace al resultado
  defendible. La cifra **existe y es citable**, en tabla propia por estrato; el gate de
  latencia **no se midio** y se dice explicito (F-123.1), no se omite.
  **La misma jornada, DESPUES del veredicto, el usuario firmo la enmienda D-FT-14**: T2
  se reabre como tier **exploratorio** —para separar si el fallo fue de capacidad o
  estructural—, no como reintento de T1, y **T3 queda cerrado como trabajo futuro con
  causa tecnica** (sin baseline MM-GDINO geometricamente sana el delta es
  ininterpretable), **jamas por "falta de tiempo"**. **D-FT-15** fijo los margenes de T2
  **antes de todo resultado T2**, con la retencion de vocabulario abierto sobre COCO
  val2017 congelada en mAP50 **0,434676 => umbral NO-GO 0,391208**, y con la expectativa
  **pre-registrada** de que T2 tambien de NO-GO. **T2 esta enviado y en cola, sin
  empezar**: no tiene ni una cifra. Al redactar, la secuencia se cuenta completa y en ese
  orden —veredicto, enmienda posterior, margenes firmados por adelantado—: **la
  transparencia de la secuencia ES el argumento**, y suavizarla la destruye.
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
- **La containerizacion SI se puede mencionar en el informe** (✎ 2026-08-18, precision del
  usuario — antes esto se leia como "no mencionarla"). Esta **diferida con causa**
  (ADR-019 §4): se va a hacer **despues** de cerrar la redaccion, su razon de ser es la
  **reproducibilidad** de la plataforma —que un tercero pueda levantarla en otra maquina—
  y **no** cerrar el informe, y su **documentacion operativa vive en los repositorios**
  (`infra/`, READMEs), no en la tesis. **Como escribirla:** como **trabajo comprometido
  con su causa**, en el cierre (§17.6/§18) y en el camino de reproducibilidad (§19).
  **Como NO escribirla:** en presente, como capacidad existente, o con instrucciones de
  despliegue — el informe no es un manual. La frase que gobierna: *describir el compromiso
  y su fundamento es correcto; describir un despliegue que no corrio es falso.*
- **Metricas de `report.json`**: `t_alert-system` es **citable** (esta en el diccionario de
  la spec 40 §5.1 y siempre debio figurar; dejo de estar clavada en `not_applicable`).
  `precision_alertas` / `recall_alertas` / `F1_alertas` **existen pero NO son citables**:
  duplican cifras que ya se reportan via `evaluate-alerts` con denominadores por estrato.
  **La citabilidad esta materializada**: `t_alert-system` ES la columna `t_alert` del
  clip bench (campo `t_alert_system_ms` de cada `metrics.json`) — citable por campana y
  por condicion, nunca promediada entre campanas. NO confundir con `t_alert-notification`
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
> Seleccion: pase de cierre 1 (2026-08-19): sus decisiones D1-D4 y la regla de autocontención SIGUEN RIGIENDO.

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

## Fuente: `docs/informe/entregable/desarrollando/correcciones-etapa-3-4-pase-2.md`

> SHA-256 del bloque: `df5544cc0cbf7db188107f34d01de3b8cbdb47489227133bbc53e513fd978d62`  
> Seleccion: pase de cierre 2 (2026-08-20): continua la numeracion del pase 1 y manda sobre el resto del material de esta etapa.

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

> ⚠ **Nota operativa (no es contenido del informe).** El generador del project-kit
> (`herramientas/generar_project_kit.py`, líneas 135 y 153) sigue apuntando a
> `informe/entregable/desarrollando/correcciones-etapa-3-4.md`, que el 2026-08-20 pasó a `archivado/`.
> Hoy `--check --etapa all` falla. Al decidir si este archivo entra al kit, corregir esas dos rutas.

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

## Fuente: `docs/informe/entregable/96e-informe-v11-cierre-anexos-referencias.md`

> SHA-256 del bloque: `6b1d8f4b631dc608b001d500a4eea6e9e439d42022a38bf05f984a963eb921a6`  
> Seleccion: placeholder vigente de la seccion 17.4.

### 17.4. Implementación del prototipo experimental

[Agregado futuro correspondiente a la Etapa 4]

---

## Fuente: `docs/informe/ajustes/04-etapa-4-implementacion.md`

> SHA-256 del bloque: `ad1e9ea5d9f22449b2e6c54ac170f9488aeae008e5f7554f256cff7e9ef3920d`  
> Seleccion: documento completo.

# Etapa 4 — §17.4 Implementación del prototipo experimental

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

- **Distribución de alertas por MQTT** — **funcionalmente implementada y verificada**.
  Lo pendiente es su acople operativo: vista de outcomes en la webconsole, lanzamiento
  desde la orquestación y commits del repo. E-06 (canales extra y dashboard propio)
  sigue excluida. Diseño y contratos: `92b`; evidencia ejecutada: `operacion/114`.
- **Métricas MOT** (exclusión E-10). Atención al matiz de R-21: lo excluido son las
  **métricas**, no la capacidad — el tracker existe y la granularidad por sujeto es el
  mejor resultado del banco.
- **Fine-tuning** (E-04) — ✎ 2026-08-11 su estatuto cambió: **ADR-017 la puso en
  alcance como jornada experimental comprometida** (escalera T1→T2/T3 con go/no-go y
  Mendieta). ✎ **2026-08-13:** F-100.1 está resuelta; `1166583` cerró freeze/smoke técnico,
  dual gate y serving real. T1 full sigue en NO-GO por D-FT-08/T-FT-005, T-FT-031 y
  T-FT-032; la procedencia T-FT-023 quedó CERRADA el 2026-08-13 (snapshot tar `639e60df…`),
  evaluación T031 y baseline 26s T032. ✎ **2026-08-15: D-FT-08/T-FT-005, D-FT-12 y D-FT-13
  firmadas, y T-FT-031/032 cerradas la misma jornada** (doc 120: baseline 26s one-shot,
  `bare_head` AP50 0,000) — el NO-GO quedó en `full-authorization.json` + `RUN` manual.
  Se redacta como **rama condicionada por datos y protocolo** y
  **declarando el estado real de la jornada al momento de la entrega**, con causa
  técnica — nunca "por tiempo", y nunca en presente mientras no haya corrida
  verificada. *Decía "no ejercida por secuenciación"*.

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
   `operacion/114`/`118`), el runner lo orquesta (ADR-018) y expone servicio HTTP propio
   (ADR-019, doc 124). **Se escribe en presente y como capacidad existente**, con su
   estatuto: trabajo comprometido por ADR-016, entregado y verificado. Lo que sigue
   estando prohibido: citar cifras de la verificación funcional del servicio HTTP (n=2,
   doc 124 — no citables) en lugar de las de la campaña (doc 118), y presentar la
   containerización como hecha (diferida con causa, ADR-019 §4).
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

## Fuente: `docs/informe/entregable/borradores/17-4.md`

> SHA-256 del bloque: `2d8a2ffa4cd51667216e67b27c7e573ca641bac2bb8d7e5d7db9b806c03b8d5a`  
> Seleccion: borrador completo de la seccion 17.4, listo para revision.

# Borrador — §17.4 Implementación del prototipo experimental

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

> SHA-256 del bloque: `55795252e41c480e61854300db20e32b81c008845424c91ff9c5ea8779a8e5d4`  
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
> línea, y tiempos de postproceso/escritura inventados). Lo que sigue es la **transcripción literal** de
> `e-ovrt_media-plane/runs/run_20260711_211647_dbe_grounding_dino_6114c6/detections.jsonl`, unidad
> `frame_000120` — la unidad en la que el sistema confirma la alerta de CR-01, a los 4000 ms exactos.
> **Único recorte:** de las 22 detecciones de esa unidad se muestran 2, y se indica el recorte.
> **Regla: no se agrega, no se mejora, no se completa nada.**
>
> ⚠️ **✎ 2026-08-12 — el `source_id` de esta línea es `cb_b01_p7`, un clip RETIRADO del banco**
> el 2026-08-03 (licencia sin registrar + GT por IA). Como ejemplo de **esquema** la línea es
> válida —no se cita ningún resultado suyo—, pero **no debe entrar al informe con ese
> identificador**. Se resuelve re-transcribiendo un replay sobre un clip del banco vigente, o
> declarando la omisión del identificador. **No se edita a mano**: eso reintroduciría el
> problema que la auditoría del 12/07 vino a cerrar. Detalle y opciones: `94` §1.3.

```json
{
  "schema_version": "media.detection.v1",
  "event_type": "detection_event",
  "run_id": "run_20260711_211647_dbe_grounding_dino_6114c6",
  "unit_id": "frame_000120",
  "source":  { "source_id": "cb_b01_p7", "source_type": "video_frame",
               "frame_index": 120, "timestamp_ms": 4000.0,
               "width": 1920, "height": 1080 },
  "model":   { "name": "grounding_dino",
               "model_id": "IDEA-Research/grounding-dino-tiny", "device": "cuda" },
  "prompts": { "prompt_set_id": "cr01_cr02_v2_short_inline" },
  "detections": [
    { "detection_id": "det_000001", "label": "person",
      "prompt_id": "person", "source_prompt": "person", "confidence": 0.8257,
      "bbox_xyxy": [1734.6, 300.9, 1838.2, 525.8],
      "bbox_norm_xyxy": [0.9034, 0.2786, 0.9574, 0.4869],
      "area_px": 23291.6, "model_name": "grounding_dino" },
    { "detection_id": "det_000002", "label": "person",
      "prompt_id": "person", "source_prompt": "person", "confidence": 0.837,
      "bbox_xyxy": [159.5, 402.2, 253.4, 639.8],
      "bbox_norm_xyxy": [0.0831, 0.3724, 0.132, 0.5924],
      "area_px": 22312.3, "model_name": "grounding_dino" }
    // … 20 detecciones más (person / helmet / vest) omitidas por legibilidad
  ],
  "timing": { "normalize_ms": 8.25, "inference_ms": 214.37,
              "postprocess_ms": 0.2, "write_ms": 0.0, "total_ms": 214.59 }
}
```

**Dos cosas que esta línea literal enseña, y que el ejemplo fabricado ocultaba:**

1. **`strategy` y `condition_id` no aparecen.** Existen en el modelo Pydantic, pero valen `None` y el
   escritor omite los nulos. El evento **no lleva hoy la condición de riesgo asociada**: la asociación
   condición ↔ evidencia la hace el plano de control. Si se quiere que el evento la lleve, hay que
   poblarla (es aditivo y barato) — pero **no se puede escribir en el informe que ya la lleva**.
2. **El identificador del conjunto de prompts es `cr01_cr02_v2_short_inline`**, no `cr01_cr02_v2_short`:
   el sufijo `_inline` registra que el conjunto viajó embebido en el disparo de la corrida, no por
   referencia a catálogo. Es trazabilidad real, y conviene no "limpiarla" al transcribir.

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
  "topic": "media.detection.v1.run_20260711_211647_...",
  "key": "cb_b01_p7",          // source_id
  "seq": 41,                   // monótono: el hueco de seq es la ÚNICA señal de pérdida
  "ts_publish_ms": 1783804607379.2,
  "payload": <bytes de la línea JSONL> }
```

> **Frase para el capítulo:** *"El evento de percepción se persiste primero y se publica después. El
> payload publicado en el bus es byte-idéntico a la línea persistida, de modo que toda corrida en vivo es
> re-evaluable offline y produce artefactos idénticos (verificado)."*

---

## 3. Las APIs: el sistema es ejecutable por HTTP

El capítulo no tiene una sola interfaz. El sistema tiene dos servicios HTTP config-driven. Esta es la
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
> distintos. Ahora la detección **emitida hoy** es la línea literal de `frame_000120` (la misma de §2.2),
> y lo **previsto** va claramente separado, en comentarios, sin fingir que existe.

```jsonc
{
  "schema_version": "media.detection.v1",     // aditivo ⇒ NO cambia al agregar campos nuevos
  "run_id": "run_20260711_211647_dbe_grounding_dino_6114c6",
  "unit_id": "frame_000120",
  "source":  { "source_id": "cb_b01_p7", "source_type": "video_frame",
               "frame_index": 120, "timestamp_ms": 4000.0, "width": 1920, "height": 1080 },
  "model":   { "name": "grounding_dino",
               "model_id": "IDEA-Research/grounding-dino-tiny", "device": "cuda" },
  "prompts": { "prompt_set_id": "cr01_cr02_v2_short_inline" },
  "detections": [
    {
      // ================= EMITIDO HOY (línea literal del artefacto) =================
      "detection_id": "det_000002",           // índice por frame: NO es identidad entre frames
      "label": "person", "confidence": 0.837,
      "bbox_xyxy":      [159.5, 402.2, 253.4, 639.8],
      "bbox_norm_xyxy": [0.0831, 0.3724, 0.132, 0.5924],
      "prompt_id": "person", "source_prompt": "person",
      "area_px": 22312.3, "model_name": "grounding_dino"

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
  "timing": { "normalize_ms": 8.25, "inference_ms": 214.37,
              "postprocess_ms": 0.2, "write_ms": 0.0, "total_ms": 214.59 }
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
    subject_key: str                  # "CR-01:cb_b01_p7" bajo escena
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

> ⚠️ **Corregido tras auditoría.** La versión anterior mostraba la alerta de la corrida **mock** (el smoke
> de plomería de `clip_id`), que confirma en 4033,33 ms. La alerta de abajo es la del **benchmark real con
> GDINO-tiny** sobre `cb_b01_p7`, reproducido y archivado el 2026-07-12 en
> `operacion/datos/95-2026-07-12-bench-cb_b01_p7-gdino-alerts.jsonl`. Confirma en **4000,0 ms exactos**.
> Si vas a poner un JSON al lado del número `t_alert-system = 4000 ms`, tiene que ser **este**.

```json
{ "schema_version": "control.alert.v1", "event_type": "alert_event",
  "control_run_id": "bench_cb_b01_p7_gdino_20260712_20260712T232146Z",
  "media_run_id":   "run_20260711_211647_dbe_grounding_dino_6114c6",
  "alert_id": "ff1ffb62-60a9-5e19-a7b8-42d076864f14",
  "pattern_id": "CR-01", "condition_id": "CR-01",
  "subject_key": "CR-01:cb_b01_p7", "source_id": "cb_b01_p7",
  "severity": "high", "state": "open",
  "unit_id": "frame_000120", "frame_index": 120, "timestamp_ms": 4000.0,
  "evidence": {
    "subject": { "detection_id": "det_000013", "label": "person", "confidence": 0.502,
                 "bbox_xyxy": [1065.4, 1005.4, 1185.9, 1081.2] },
    "missing_class": "helmet",
    "supporting": [ { "detection_id": "det_000021", "label": "person", "confidence": 0.4016 },
                    { "detection_id": "det_000022", "label": "person", "confidence": 0.4147 } ],
    "score": 0.502, "subjects_in_evidence": 3,
    "rationale": "No se encontro evidencia 'helmet' en region 'upper_body' de 3 sujeto(s)." },
  "frame_index": 120, "timestamp_ms": 4000.0, "subjects_in_evidence_max": 6,
  "first_evidence_ms": 230525124.622, "first_evidence_unit_id": "frame_000000",
  "alert_registered_ms": 230525159.420,
  "experiment_id": null }
```

Cuatro cosas para señalar en el texto:

1. **`alert_id` es un uuid5 determinista** (`pattern_engine.py:517`) ⇒ la alerta es **idempotente**:
   reprocesar la misma corrida produce el mismo identificador, y un consumidor aguas abajo puede
   deduplicar sin estado compartido.
2. **`rationale` en lenguaje natural + `subject` + `supporting[]` + `missing_class`**: la evidencia de la
   ausencia es **auditable**. Es el argumento a favor de E-IND frente al prompt de negación, hecho
   artefacto. Esto es lo que un prompt de negación **no puede darte**.
3. **La alerta confirma en `timestamp_ms: 4000.0`** — exactamente la ventana de persistencia configurada
   para CR-01. El sistema hace lo que su configuración declara, al milisegundo.
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
> La corrida **real** con GDINO-tiny sobre `cb_b01_p7` (`summary.json` archivado) dice:
> **`g2a: p50 2214,2 ms · p95 2604,1 ms · p95_within_budget: false`** — un orden de magnitud **por encima**
> del presupuesto 50–250 ms.
>
> **No lo escondas: convertilo en hallazgo.** Es exactamente el mismo resultado que el conflicto
> CR-01 ↔ tiempo real del doc 31 (GDINO sostiene CR-01 pero sólo sigue el 14–22 % del ritmo de cámara), y
> refuerza la tesis en vez de debilitarla: *la instrumentación **funciona** — mide, compara contra el
> presupuesto y **declara el incumplimiento sola** (`p95_within_budget: false`)*. Un instrumento que sólo
> devuelve verdes no es un instrumento.
>
> Formulación correcta para el informe: *"la instrumentación de G2A opera y detecta el incumplimiento: con
> detector de referencia el p95 es de 31,8 ms (dentro del presupuesto), mientras que con el detector
> open-vocabulary evaluado el p95 asciende a 2604 ms y el sistema lo declara fuera de presupuesto. La
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
- [ ] §17.3.5 — figura nueva: vista de procesos (dos servicios HTTP + bus + orquestador + webconsole).
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

## Fuente: `docs/operacion/97-relevamiento-plataforma-2026-08-05.md`

> SHA-256 del bloque: `13e72b30b70e9a9bc7a640bf2d65fd34286cdfed4de6ab2c84711fbb23623513`  
> Seleccion: documento completo.

# 97 — Relevamiento integral de la plataforma (2026-08-05)

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

> SHA-256 del bloque: `6fcff2323b871885bb8a176d4dd8a0b67e2599b7f01f04b9590c70a5aafed403`  
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
y `delivered_at`.

**Salidas por corrida:** `notifications.jsonl`, `dead_letter.jsonl` y
`distribution_summary.json` (conteos por outcome + agregados de `t_alert-notification`).

## 5. Por qué MQTT, y por qué es un ejemplo

MQTT es el canal **elegido para demostrar el mecanismo**, no una integración con un sistema
real de obra. El fundamento (doc 07 D5):

- **Peso mínimo** — un Mosquitto en el compose, sin infraestructura adicional.
- **Estándar de integración IoT** — es la respuesta defendible a "¿cómo se conecta esto con
  el mundo?".
- **Medición limpia** — `t_alert-notification` sin la variabilidad de una API externa. Un
  canal tipo Telegram habría medido la latencia de un servicio ajeno al sistema.

**Y una consecuencia que no es opcional:** MQTT QoS 1 puede **duplicar entregas**. Por eso
el ledger no es un lujo de diseño — es requisito del canal elegido. Lo mismo valdría para
cualquier broker at-least-once.

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

### 6.1 Un desfase que quien implemente va a chocar

El diseño de `historicos/06` §6.1 asume que el `NotificationEnvelope` se arma con un
**`confirmed_at_ms`** tomado de la alerta. **`control.alert.v1` no tiene ese campo.** Lo que
sí tiene es `timestamp_ms` (del evento que confirmó), `alert_registered_ms` y
`first_evidence_ms`. Al construir el envelope hay que decidir cuál de los tres es el
instante de confirmación —y esa decisión afecta directamente a `t_alert-notification`, que
es la métrica del tramo. Queda anotado acá para que se resuelva con criterio y no por
descarte.

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

