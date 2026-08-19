# E-OVRT-VDP - paquete de etapa 3

> Generado el 2026-08-19. Etapa 3: seccion 17.3, diseno arquitectonico.

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

- **Etapa activa:** 3 - Etapa 3: seccion 17.3, diseno arquitectonico.
- Este archivo contiene el texto vigente que se modifica y sus insumos de ajuste.
- No se trasladan resultados propios hacia secciones cronologicamente anteriores.
- Nombre propio de esta etapa (01-etapa-3-activa.md): regenerarla no pisa el paquete de ninguna otra etapa.

---

## Fuente: `docs/informe/entregable/desarrollando/correcciones-etapa-3-4.md`

> SHA-256 del bloque: `65b07f50c50fddcfd4512416d2cc6763402e4c8eaf42a65d32a8c931022e29f1`  
> Seleccion: pase de cierre 2026-08-19: manda sobre el resto del material de esta etapa.

# Correcciones para cerrar §17.3 (Diseño Arquitectónico) y §17.4 (Implementación)

**Fecha:** 2026-08-19 · **Insumos:** `E-OVRT-VDP_Seccion_17.3_Diseno_Arquitectonico_v0.1.docx`,
`E-OVRT-VDP_Seccion_17.4_Implementacion_v0.1.docx`, `observaciones-etapa-3-4.txt` (41 comentarios, todos resueltos acá).
**Verificación:** todos los valores citados fueron contrastados contra los repos el 2026-08-19 (ver §D).
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

## Fuente: `docs/informe/entregable/90-etapa3-texto-extraido.md`

> SHA-256 del bloque: `3ce6c5fbaab79d820f7ad36af890730f3269e54ffc4e3f083b3ecb0578fea777`  
> Seleccion: documento completo.

### 17.3.1. Introducción y propósito del capítulo

El presente capítulo desarrolla el diseño arquitectónico de la plataforma experimental E-OVRT-VDP, tomando como punto de partida el alcance metodológico, las condiciones de riesgo, los escenarios de evaluación y las métricas definidas en las secciones anteriores. Su propósito es transformar esas definiciones en una organización técnica capaz de orientar la implementación de la plataforma experimental, manteniendo coherencia con los criterios de modularidad, trazabilidad, medición y control de alcance ya establecidos.

La arquitectura se estructura alrededor de una separación entre el procesamiento visual en tiempo real y la lógica de interpretación posterior. Para ello, se distinguen dos planos principales: el plano de medios, encargado de la ingesta, normalización, inferencia y publicación de resultados perceptivos; y el plano de control, responsable de evaluar patrones de riesgo, registrar alertas asistivas, conservar eventos y producir evidencia reconstruible. Esta división permite proteger la ruta crítica de vídeo y, al mismo tiempo, sostener la trazabilidad experimental necesaria para analizar cada corrida.

El capítulo describe las responsabilidades de los componentes principales, los flujos de información, las fronteras entre módulos, los contratos preliminares, los escenarios experimentales DBE y EBE, y los criterios de observabilidad que deberán acompañar la implementación. Su finalidad es consolidar una base arquitectónica que permita materializar el prototipo experimental de manera incremental, medible y trazable dentro del alcance experimental definido.

La pregunta que orienta el capítulo puede sintetizarse del siguiente modo: ¿qué arquitectura permite materializar una plataforma experimental de detección open-vocabulary en video en tiempo real, manteniendo modularidad, desacoplamiento, trazabilidad y evaluabilidad dentro del alcance metodológico ya definido?

### 17.3.2. Insumos metodológicos y decisiones derivadas

La arquitectura propuesta se construye a partir de las definiciones metodológicas consolidadas en las secciones anteriores. En particular, toma como insumos el alcance experimental del prototipo, el catálogo de condiciones de riesgo, los escenarios de evaluación, la infraestructura disponible, la estrategia de datos, el framework de métricas y los lineamientos ético-legales. Por lo tanto, los módulos, flujos y límites del sistema no se definen como decisiones aisladas, sino como consecuencia directa del protocolo experimental ya establecido.

En continuidad con el núcleo validable definido previamente, el diseño prioriza las condiciones de Nivel 1, correspondientes a CR-01 y CR-02. Esta decisión permite concentrar la arquitectura inicial en un flujo completo de percepción, publicación de eventos, evaluación de patrones, registro de alertas y medición, sin incorporar como dependencias obligatorias capacidades más complejas como razonamiento espacial, calibración de zonas o seguimiento multiobjeto formal. Las condiciones de mayor complejidad permanecen previstas como extensiones condicionadas, pero no determinan el cierre del primer ciclo funcional del prototipo experimental.

Del mismo modo, la distinción metodológica entre DBE y EBE condiciona la arquitectura desde el inicio. DBE se mantiene como escenario principal para estabilizar la evaluación sobre fuentes controladas y reproducibles, mientras que EBE se incorpora como escenario complementario para observar el comportamiento del sistema con captura o streaming en un entorno controlado. Esta separación obliga a abstraer las fuentes visuales, normalizar la entrada al pipeline y conservar métricas comparables entre escenarios, sin confundir la naturaleza de la fuente con una topología física de despliegue.

A partir de estos insumos, la arquitectura debe asegurar que cada decisión de diseño pueda vincularse con una necesidad metodológica concreta: reproducibilidad de corridas, trazabilidad de eventos, medición de latencia, control de evidencia visual, modularidad de componentes y preservación del alcance experimental. La Tabla 39 sintetiza esta relación entre definiciones previas y decisiones arquitectónicas derivadas.

Tabla 39

Insumos metodológicos y decisiones arquitectónicas derivadas

| Insumo metodológico consolidado | Criterio ya definido | Decisión arquitectónica derivada |

| Marco teórico de OVD, MOT y streaming | El sistema debe integrar percepción visión-lenguaje, procesamiento de video y persistencia temporal cuando resulte necesaria. | Diseñar una arquitectura modular, con separación de planos, ruta crítica medible y modelos sustituibles mediante adaptadores. |

| Condiciones de riesgo seleccionadas | El núcleo evaluativo se concentra en condiciones visuales directas, mientras que las condiciones contextuales o relacionales quedan condicionadas. | Priorizar el flujo completo para detección de EPP y mantener reglas espaciales, zonas y tracking como extensiones no bloqueantes. |

| Escenarios DBE y EBE | La evaluación combina fuentes controladas reproducibles y fuentes continuas o de captura en entorno controlado. Esta diferencia implica naturalezas temporales distintas: las fuentes de archivo pueden regularse durante la lectura, mientras que las fuentes vivas no detienen la evolución de la escena. | Abstraer las fuentes visuales para que ambos escenarios ingresen al pipeline mediante contratos comunes, distinguiendo criterios de reproducibilidad, frescura, omisión, descarte y trazabilidad temporal según la naturaleza de la fuente. |

| Roles funcionales CPN, EN y TN | La arquitectura distingue responsabilidades lógicas de procesamiento central, captura y soporte de adaptación, sin asumir que cada rol corresponda necesariamente a un nodo físico independiente. | Definir CPN, EN y TN como roles funcionales de referencia permite organizar el diseño, interpretar corridas y delimitar responsabilidades sin fijar una distribución obligatoria en hardware, procesos o contenedores. |

| Framework de métricas | La evaluación requiere medir detección, rendimiento, latencia, persistencia temporal, alertas y uso de recursos. | Instrumentar timestamps, configuración de corrida, métricas por tramo y eventos reconstruibles desde el inicio del diseño. |

| Lineamientos ético-legales | El sistema opera como herramienta asistiva, sin reconocimiento de identidad y bajo criterios de minimización visual. | Priorizar eventos, metadatos y referencias controladas; conservar evidencia visual sólo cuando esté justificada por validación, auditoría o comunicación académica. |



Nota. La tabla sintetiza cómo las definiciones metodológicas ya establecidas condicionan las principales decisiones de diseño arquitectónico. No reitera el protocolo experimental, sino que explicita sus consecuencias sobre la organización del sistema.

### 17.3.3. Alcance, requisitos y decisiones arquitectónicas iniciales

El diseño arquitectónico se formula para un prototipo experimental ejecutado en un entorno local y controlado. En consecuencia, la arquitectura debe orientar la implementación, la medición y la reconstrucción de resultados sin asumir responsabilidades propias de una solución productiva. La sección delimita el alcance efectivo del núcleo validable, las extensiones previstas, las capacidades requeridas, las cualidades no funcionales relevantes y las decisiones iniciales que deberán conservarse durante el desarrollo del prototipo experimental.

#### 17.3.3.1. Alcance del núcleo y extensiones

El alcance arquitectónico se organiza alrededor del núcleo validable definido en la consolidación metodológica. Sobre ese núcleo, la plataforma debe demostrar un flujo completo, medible y trazable desde una fuente visual hasta una alerta asistiva registrada. El objetivo no es ampliar prematuramente la cantidad de condiciones cubiertas, sino asegurar una base suficientemente sólida para procesar evidencia visual, publicar eventos, evaluar patrones, registrar alertas y reconstruir resultados experimentales.

El núcleo incluye las capacidades necesarias para operar sobre fuentes controladas, ejecutar inferencia open-vocabulary, versionar prompts, normalizar detecciones, aplicar reglas temporales simples, registrar eventos y producir métricas comparables. Las capacidades de mayor complejidad —seguimiento multiobjeto formal, reglas espaciales, zonas parametrizadas, preselección liviana en borde o adaptación al dominio— quedan previstas como extensiones condicionadas, siempre que no desplacen la validación inicial ni agreguen dependencias innecesarias al flujo base.

Tabla 40

Alcance del núcleo validable y extensiones condicionadas

| Capacidad | Tratamiento en Etapa 3 | Justificación |

| Detección de condiciones de Nivel 1 | Núcleo validable | Permite evaluar el flujo completo sobre condiciones visuales directas y medibles. |

| Gestión de prompts y vocabulario activo | Núcleo validable | Garantiza trazabilidad entre formulaciones, estrategias de detección, umbrales y resultados. |

| Reglas temporales de patrón | Núcleo validable | Transforman detecciones puntuales en evidencia sostenida antes de registrar alertas. |

| Registro persistente de eventos y trazabilidad | Núcleo validable | Permite reconstruir corridas, patrones, alertas, métricas y errores relevantes. |

| DBE | Núcleo de evaluación | Estabiliza inferencia, contratos, eventos y métricas bajo condiciones reproducibles. |

| EBE | Complementario previsto | Permite observar el comportamiento del sistema con captura o streaming en entorno controlado. |

| Condiciones de Nivel 2 y Nivel 3 | Extensiones condicionadas | Requieren capacidades adicionales de contexto, razonamiento espacial, zonas, proximidad o relaciones entre entidades. |

| MOT formal | Extensión condicionada | Puede aportar persistencia temporal y soporte para reglas relacionales, pero no es dependencia del núcleo. |

| Adaptación al dominio (Fine-tuning) | Rama comparativa condicionada | Sólo corresponde si existe baseline preentrenado, datos suficientes y partición experimental válida. |

| Interfaz de inspección | Mínima en el núcleo | Debe permitir revisar corridas, alertas y métricas sin convertirse en un tablero productivo. |

| Evidencia visual controlada | Complementario previsto | Se admite sólo cuando esté justificada por validación, auditoría técnica o comunicación académica. |

| Video crudo continuo | Fuera del comportamiento ordinario | La trazabilidad principal se apoya en eventos, metadatos, métricas y referencias controladas. |



Nota. El tratamiento "núcleo validable" identifica capacidades necesarias para el flujo base; "núcleo de evaluación" refiere a la evaluación sobre fuentes controladas; "complementario previsto" agrupa capacidades útiles pero no obligatorias; "extensión condicionada" identifica capacidades previstas sujetas a disponibilidad de datos y módulos; y "rama comparativa condicionada" refiere a variantes que requieren condiciones metodológicas específicas para su incorporación.

La inclusión de la gestión de prompts dentro del núcleo responde a la naturaleza open-vocabulary de la plataforma: cada resultado debe poder asociarse con una formulación, una estrategia de detección y un vocabulario activo registrados. Del mismo modo, la separación entre DBE y EBE permite distinguir la evaluación reproducible de la validación con captura continua, evitando mezclar variabilidad de cámara, iluminación, códec o red con el desempeño propio del detector.

En relación con la evidencia visual, el diseño retoma los criterios ya definidos de minimización, uso asistivo y ausencia de reconocimiento de identidad. La trazabilidad ordinaria se apoya en eventos, metadatos, identificadores, métricas y referencias controladas. Los clips, snapshots o recortes anotados sólo se consideran artefactos complementarios cuando resulten necesarios para validación, revisión técnica o defensa académica.

#### 17.3.3.2. Capacidades arquitectónicas requeridas

A partir del alcance definido, la arquitectura debe habilitar un conjunto mínimo de capacidades que permitan desarrollar un prototipo experimental medible, trazable y extensible. Estas capacidades no describen todavía componentes de implementación, sino responsabilidades que el diseño debe contemplar para que el sistema pueda procesar fuentes visuales, ejecutar inferencia open-vocabulary, evaluar patrones, registrar alertas y producir evidencia experimental.

La clasificación distingue capacidades del núcleo, capacidades asociadas a la evaluación controlada, capacidades complementarias previstas, extensiones condicionadas y ramas comparativas. Esta separación permite ordenar el desarrollo sin convertir funcionalidades deseables en dependencias obligatorias del flujo base.

Tabla 41

Capacidades arquitectónicas requeridas

| Capacidad requerida | Compromiso | Lectura de diseño |

| Gestión de corrida reproducible | Núcleo | Cada ejecución debe asociarse a una configuración explícita de fuente, modelo, prompts, umbrales, entorno y versiones. |

| Procesamiento DBE | Núcleo de evaluación | Debe operar sobre imágenes, datasets o videos locales para estabilizar inferencia, contratos, eventos y métricas bajo condiciones reproducibles. |

| Procesamiento EBE | Complementario previsto | Debe admitir captura o streaming en entorno controlado para observar el comportamiento operativo del sistema. |

| Normalización de entrada visual | Núcleo | Cada frame debe representarse con metadatos de corrida, fuente, orden temporal, resolución y política de muestreo. |

| Inferencia OVD configurable | Núcleo | La arquitectura debe permitir integrar modelos de detección open-vocabulary sin acoplar el sistema a una única alternativa. |

| Gestión de prompts y vocabulario activo | Núcleo | Debe versionar formulaciones, aliases, estrategias de detección, vocabulario activo y umbrales asociados. |

| Normalización de detecciones | Núcleo | Las salidas heterogéneas de los modelos deben transformarse en detecciones comparables, trazables y aptas para evaluación posterior. |

| Evaluación de patrones de Nivel 1 | Núcleo | Las detecciones deben transformarse en patrones confirmados mediante criterios de persistencia temporal e histéresis. |

| Registro de alertas asistivas | Núcleo | Las alertas deben registrarse cuando un patrón alcanza estado confirmado, sin constituir un juicio normativo automático. |

| Publicación y persistencia de eventos | Núcleo | La arquitectura debe desacoplar la producción de evidencia perceptiva y conservar un historial reconstruible de eventos relevantes. |

| Observabilidad y métricas | Núcleo | Debe medir FPS, latencias por tramo, uso de recursos, estados de patrón, alertas, descartes y errores. |

| Reporte experimental | Núcleo | Debe sintetizar configuración, resultados, métricas, alertas, errores y limitaciones por corrida. |

| Inspección mínima de resultados | Núcleo | Debe permitir revisar corridas, alertas, métricas y evidencia asociada sin convertirse en un tablero operativo avanzado. |

| Gestión de evidencia visual controlada | Complementario previsto | Debe admitir clips, snapshots o recortes justificados para validación, revisión técnica o comunicación académica. |

| Capacidades contextuales y relacionales | Extensión condicionada | MOT, zonas y reglas espaciales deben quedar previstas para condiciones de Nivel 2 y Nivel 3, sin bloquear el flujo base. |

| Comparación de variantes de modelo | Rama comparativa condicionada | Debe permitir registrar y comparar checkpoints, optimizaciones o variantes ajustadas sólo bajo condiciones experimentales válidas. |



Nota. El compromiso “núcleo” identifica capacidades necesarias para el flujo base; “núcleo de evaluación” refiere a capacidades que sostienen la evaluación controlada; “complementario previsto” agrupa capacidades útiles para validación, revisión o comunicación académica; “extensión condicionada” identifica capacidades previstas pero no obligatorias; y “rama comparativa condicionada” refiere a variantes que sólo deben incorporarse si se cumplen las condiciones metodológicas correspondientes.

#### 17.3.3.3. Requisitos no funcionales de referencia

Las cualidades no funcionales condicionan directamente la validez experimental del prototipo. No alcanza con detectar una condición de riesgo si el sistema no registra la configuración de la corrida, no mide latencia, no conserva trazabilidad suficiente o no controla la evidencia visual generada. Por esta razón, la reproducibilidad, la observabilidad, la privacidad, la modularidad, la integridad de eventos y el control de complejidad se consideran condiciones arquitectónicas del diseño.

Tabla 42

Requisitos no funcionales de referencia

| Dimensión | Requisito de diseño | Implicación arquitectónica |

| Latencia | Acotar la ruta crítica desde la lectura o captura hasta la publicación de eventos de percepción. | El plano de medios no debe depender de reportes, inspección, persistencia pesada ni notificaciones externas para continuar procesando frames. |

| Reproducibilidad | Registrar la configuración efectiva de cada corrida. | Cada ejecución debe conservar fuente, modelo, prompts, umbrales, entorno, versiones y políticas de muestreo. |

| Modularidad | Permitir la sustitución de fuentes, modelos, prompts, postproceso y motor de patrones. | Los componentes deben comunicarse mediante contratos explícitos y no mediante estructuras internas acopladas. |

| Trazabilidad | Reconstruir una alerta a partir de configuración, detecciones, patrón, métricas y evidencia asociada. | Los eventos, identificadores y relaciones causales deben conservar información suficiente para revisión posterior. |

| Integridad de eventos | Evitar pérdida, duplicación o ambigüedad en eventos relevantes. | Los eventos deben incluir identificadores, versión de esquema, orden lógico y asociación con la corrida correspondiente. |

| Privacidad y minimización | Proteger configuraciones, métricas, eventos y artefactos visuales conservados. | La trazabilidad ordinaria debe apoyarse en eventos y metadatos; los artefactos visuales sólo deben conservarse cuando estén justificados. |

| Observabilidad | Medir tiempos, FPS, errores, descartes y uso de recursos desde las primeras corridas. | La instrumentación debe formar parte del diseño del pipeline y no quedar como una actividad posterior. |

| Robustez experimental | Registrar fallas y anomalías sin ocultar su impacto sobre la corrida. | Los errores de fuente, inferencia, publicación, persistencia o medición deben producir registros interpretables. |



Nota. Los requisitos no funcionales expresan cualidades necesarias para preservar la validez experimental del prototipo. Su finalidad es asegurar comparabilidad entre corridas, trazabilidad de resultados y control de decisiones que puedan afectar latencia, privacidad, reproducibilidad u observabilidad.

#### 17.3.3.4. Decisiones arquitectónicas iniciales

Además de delimitar alcance, capacidades y cualidades no funcionales, el diseño debe explicitar un conjunto de decisiones arquitectónicas iniciales. Estas decisiones no fijan tecnologías concretas, pero establecen reglas estructurales que deberán preservarse durante el desarrollo del prototipo experimental para mantener coherencia con el alcance metodológico, la trazabilidad y la medición de resultados.

Tabla 43

Decisiones arquitectónicas iniciales

| ID | Decisión | Estado | Justificación |

| DA-01 | Separar plano de medios y plano de control. | Adoptada | Protege la ruta crítica de vídeo y desacopla la inferencia de la lógica de interpretación. |

| DA-02 | Publicar evidencia perceptiva como eventos de percepción normalizados. | Adoptada | Permite desacoplar detecciones, patrones, métricas, alertas y persistencia. |

| DA-03 | Diferenciar el canal de eventos del repositorio persistente de eventos. | Adoptada | Separa la integración en ejecución de la reconstrucción experimental posterior. |

| DA-04 | Confirmar patrones mediante persistencia temporal e histéresis. | Adoptada | Reduce alertas generadas por detecciones aisladas, inestables o de corta duración. |

| DA-05 | Integrar modelos OVD mediante adaptadores. | Adoptada | Permite comparar modelos o variantes sin rediseñar la arquitectura general. |

| DA-06 | Mantener MOT como módulo opcional. | Condicionada | Puede aportar persistencia temporal o soporte relacional, pero no es dependencia del núcleo de Nivel 1. |

| DA-07 | Tratar la adaptación al dominio como rama comparativa condicionada. | Condicionada | Debe preservar un baseline preentrenado, datos suficientes y particiones experimentales válidas. |

| DA-08 | Adoptar minimización visual como criterio ordinario de trazabilidad. | Adoptada | Evita que el almacenamiento indiscriminado de video crudo sea parte del comportamiento base. |

| DA-09 | Separar trazabilidad ordinaria de evidencia visual controlada. | Adoptada | Permite conservar clips, capturas o recortes sólo cuando estén justificados por validación, revisión técnica o comunicación académica. |

| DA-10 | Priorizar DBE antes de EBE. | Adoptada | Estabiliza contratos, inferencia, eventos y métricas antes de incorporar captura continua. |

| DA-11 | Permitir preselección liviana en la ingesta visual como variante condicionada de EBE. | Condicionada | Puede reducir carga sobre el flujo principal de procesamiento, siempre que sea conservadora, explícita y no descarte evidencia crítica sin trazabilidad. |

| DA-12 | Versionar prompts y vocabulario activo por corrida. | Adoptada | Garantiza la reproducibilidad y comparación entre formulaciones. |

| DA-13 | Registrar la alerta interna antes de cualquier notificación externa. | Adoptada | Evita que canales externos afecten la medición de la alerta del sistema. |



Nota. Las decisiones adoptadas fijan reglas estructurales del diseño. Las decisiones condicionadas representan capacidades previstas, sujetas a validación y a que no comprometan el núcleo de Nivel 1 del prototipo experimental.

Las decisiones DA-08 y DA-09 deben leerse de manera conjunta. La plataforma no utiliza el almacenamiento continuo de video crudo como mecanismo ordinario de trazabilidad; la reconstrucción experimental se apoya principalmente en eventos, metadatos, identificadores, métricas y referencias controladas. Sin embargo, la validación con captura continua, la revisión técnica o la defensa académica pueden requerir evidencia visual demostrativa. Por ello, se admite la generación de clips breves, snapshots o recortes anotados, siempre que estén justificados y cuenten con criterios explícitos de acceso, retención y anonimización.

La DA-13 complementa esta separación: para el núcleo del prototipo experimental, la alerta válida es el evento interno registrado por la plataforma. Cualquier notificación externa debe tratarse como una salida derivada, no bloqueante y medible por separado.

A estas decisiones se agregan tres precisiones de lectura arquitectónica: DBE y EBE se tratan como escenarios experimentales y no como topologías físicas; la diferencia entre fuentes reproducibles y fuentes vivas condiciona los criterios de control de ritmo y trazabilidad temporal; y la distribución física de componentes no forma parte del compromiso conceptual de esta etapa.

### 17.3.4. Principios arquitectónicos adoptados

Las decisiones enumeradas en la Tabla 43 se articulan alrededor de cuatro principios que orientarán la lectura del diseño en las secciones siguientes.

El primero es la separación entre ruta crítica y lógica de control: la inferencia y la publicación de evidencia perceptiva (DA-01, DA-02) deben mantenerse desacopladas de la evaluación de patrones, la persistencia, los reportes y las notificaciones externas, de modo que ninguna tarea posterior pueda bloquear el procesamiento visual.

El segundo es la modularidad por contratos: fuentes, modelos, prompts, detecciones, patrones y métricas deben intercambiarse mediante estructuras explícitas (DA-05, DA-12), evitando dependencias internas que dificulten la sustitución o la evaluación comparativa.

El tercero es la trazabilidad experimental: toda alerta debe poder reconstruirse a partir de la configuración de corrida, los eventos perceptivos, el patrón evaluado y las métricas registradas (DA-03, DA-04, DA-13).

El cuarto es la medición desde el diseño: tiempos, FPS, descartes, errores y estados de patrón deben instrumentarse desde las primeras corridas, dado que forman parte de la validez experimental del prototipo.

A estos principios se suma el criterio transversal de evolución incremental: las capacidades condicionadas (DA-06, DA-07, DA-11) deben incorporarse sin desplazar el núcleo de Nivel 1 ni convertirse en dependencias del flujo base.

### 17.3.5. Vista general de la arquitectura propuesta

La plataforma E-OVRT-VDP se organiza como una arquitectura lógica por bloques, orientada a procesar fuentes de video, generar evidencia perceptiva, evaluar patrones de riesgo y conservar resultados reconstruibles. Esta vista no representa una distribución obligatoria en procesos, servicios o nodos físicos independientes, sino una separación de responsabilidades que permite mantener el sistema modular, medible y trazable.

La arquitectura distingue un flujo principal y un conjunto de capacidades de soporte. La configuración experimental actúa de forma transversal sobre ese flujo: define las condiciones de cada corrida —escenario, modelo, prompts activos, umbrales, políticas de evidencia y parámetros de ejecución— para asegurar reproducibilidad sin intervenir directamente en el procesamiento frame a frame.

El flujo principal parte de fuentes visuales externas, como pueden ser datasets, videos locales, cámaras o flujos de streaming, El plano de medios, por su parte, comienza en el adaptador de ingesta visual, el cual encapsula distintos orígenes de entrada bajo una representación común, de modo que el resto de la arquitectura pueda procesarlos de manera uniforme. Desde este punto se concentra la ruta crítica de procesamiento visual. Aquí se realizan la lectura o captura lógica, la decodificación cuando corresponda, el control de ritmo, la normalización, la inferencia open-vocabulary y el postprocesamiento, con el objetivo de producir evidencia perceptiva normalizada de forma continua y sin dependencia de tareas posteriores. Esa evidencia se publica hacia el bus interno de eventos, que actúa como mecanismo de integración desacoplada entre productores y consumidores, separando el procesamiento visual de la evaluación de patrones, el soporte experimental y las salidas derivadas.

A partir de los eventos publicados, el plano de control interpreta la evidencia producida por el plano de medios: evalúa patrones, administra estados de corrida y registra alertas asistivas internas cuando se confirma una condición de riesgo. Las alertas ya confirmadas se exponen mediante la distribución de alertas confirmadas, un canal de salida desacoplado que permite publicarlas hacia los consumidores desacoplados —interfaces de inspección, adaptadores de notificación u otras integraciones— sin bloquear al motor de patrones ni modificar la lógica central del sistema.

Finalmente, la trazabilidad, la observabilidad y la inspección se agrupan en el bloque de soporte experimental, que no constituye una etapa lineal del flujo frame a frame sino una capacidad transversal. Este bloque conserva evidencia reconstruible, consolida telemetría técnica y permite revisar corridas, métricas, alertas y resultados experimentales sin interferir con la ruta crítica del plano de medios.

Figura 4.1

Vista conceptual de la arquitectura E-OVRT-VDP

Nota. La figura presenta una vista lógica de alto nivel. Las flechas sólidas representan el flujo principal de datos y eventos; las flechas punteadas representan influencia de configuración o capacidades de soporte. La figura no debe interpretarse como una distribución física obligatoria ni como una asignación definitiva a tecnologías específicas.

En conjunto, esta organización permite que el procesamiento de video, la interpretación de patrones, la distribución de alertas y el análisis experimental se mantengan separados y coordinados mediante contratos explícitos, favoreciendo la reproducibilidad y la evaluación controlada del prototipo.

### 17.3.6. Configuración experimental y diseño de prompts

La configuración experimental concentra las decisiones que gobiernan una corrida de evaluación de la plataforma experimental. Su función es declarar, de manera explícita y reproducible, el escenario, la fuente visual, el modelo OVD, los prompts activos, los umbrales, la política de muestreo, los módulos habilitados, los criterios de patrón, la política de evidencia y la instrumentación de métricas.

Esta sección materializa, en términos arquitectónicos, definiciones establecidas en la consolidación metodológica. Las condiciones de riesgo, los escenarios, las métricas y los criterios de prompting pasan a expresarse como parámetros ejecutables que condicionan al plano de medios y al plano de control. De este modo, cada detección, transición de patrón, alerta interna, métrica o evidencia conservada puede asociarse con una configuración efectiva de corrida.

Dentro de esa configuración, los prompts se tratan como parte del vocabulario activo del experimento. En un sistema open-vocabulary, la consulta textual incide sobre la evidencia perceptiva generada; por lo tanto, debe registrarse, versionarse y mantenerse trazable hasta los resultados que contribuye a producir.

#### 17.3.6.1. Función arquitectónica de la configuración experimental

La configuración experimental actúa como punto de gobierno de la corrida. Antes de iniciar la ejecución, define qué se evaluará, con qué fuente, con qué modelo, con qué vocabulario activo y bajo qué criterios de interpretación. Esta función separa la definición de condiciones de ejecución del procesamiento efectivo de frames y eventos.

La separación protege la ruta crítica del plano de medios. Una vez iniciada la corrida, el pipeline debe disponer de la configuración efectiva sin depender de consultas externas bloqueantes para decidir qué modelo ejecutar, qué prompts utilizar o qué política de muestreo aplicar. La configuración gobierna la ejecución, pero no debe introducir latencia durante el procesamiento continuo.

También delimita la interpretación posterior de resultados. Una detección sólo es experimentalmente útil si puede relacionarse con su fuente, modelo, prompt, umbral, postproceso y patrón evaluado. Sin esa asociación, no sería posible atribuir diferencias de desempeño a una variable concreta de la corrida.

#### 17.3.6.2. Configuración de corrida como artefacto de reproducibilidad

Una corrida reproducible requiere que sus condiciones queden registradas antes de procesar la fuente visual. La finalidad no es anticipar una especificación de producto, sino asegurar que el prototipo produzca evidencia interpretable y comparable.

Dos corridas sólo son comparables si se conoce qué variable cambió y cuáles permanecieron constantes. Por ejemplo, al comparar dos prompts para CR-01, deben preservarse fuente visual, resolución, modelo, umbral, postproceso, política de muestreo, ventana de persistencia y entorno de ejecución. La Tabla 44 resume los elementos mínimos de esta configuración.

Tabla 44Elementos mínimos de la configuración experimental

| Elemento configurable | Contenido esperado | Función arquitectónica |

| Identificación de corrida | Identificador de corrida, fecha, objetivo, responsable o referencia interna. | Asocia eventos, métricas, errores, alertas y reportes a una ejecución concreta. |

| Escenario y fuente visual | DBE o EBE; dataset, video local, imagen, cámara o stream; naturaleza temporal de la fuente —reproducible/regulable o viva/continua—; resolución, FPS esperado, duración y restricciones conocidas. | Distingue evaluaciones reproducibles de pruebas con captura o streaming en entorno controlado, sin definir por sí misma una topología física de despliegue. |

| Parámetros del pipeline | Resolución de procesamiento, política conceptual de selección o muestreo, criterios de omisión o descarte, ritmo esperado de procesamiento cuando aplique y período de calentamiento. | Condiciona latencia, cobertura temporal, unidades visuales procesadas y lectura de omisiones o descartes. |

| Modelo OVD | Modelo, versión, checkpoint, backend de inferencia, precisión numérica, dispositivo y adaptador asociado. | Permite sustituir o comparar modelos sin acoplar la arquitectura a una implementación específica. |

| Prompts y vocabulario activo | Conjunto de prompts en inglés, condición asociada, variante, versión, estrategia de formulación y umbral vinculado cuando corresponda. | Garantiza trazabilidad entre consulta textual, detección producida y resultado experimental. |

| Umbrales y postproceso | Confianza mínima, IoU/NMS, filtros por clase, tamaño, región o política de normalización. | Define qué salidas crudas del detector se transforman en evidencia perceptiva normalizada. |

| Patrones activos | Condición evaluada, severidad configurada, ventana de persistencia, histéresis, cooldown y criterio de confirmación. | Permite que el plano de control transforme evidencia puntual en estados de patrón y alertas internas por episodio. |

| Capacidades habilitadas y evidencia | Tracker, zonas, preselección en borde, inspección, distribución externa y política de evidencia visual. | Evita capacidades implícitas y sostiene la minimización visual de la corrida. |

| Instrumentación y entorno | Timestamps por tramo, métricas esperadas, criterios de no aplicación, entorno experimental declarado, librerías y runtime cuando correspondan. | Permite calcular métricas, interpretar diferencias de rendimiento y reproducir corridas equivalentes sin cerrar todavía el despliegue físico definitivo. |



Nota. La tabla presenta los elementos mínimos que deben declararse para una corrida experimental. No constituye una especificación cerrada de implementación; los contratos técnicos se refinan en la sección correspondiente a contratos preliminares.

#### 17.3.6.3. Diseño de prompts y vocabulario activo

El diseño de prompts materializa la forma en que las condiciones de riesgo se expresan como consultas consumibles por un modelo OVD. En la metodología previa se trató la sensibilidad de estos modelos a la formulación de la consulta y se reconoció que el prompt no es un detalle accesorio, sino una variable de ingeniería que puede alterar detecciones, falsos positivos, falsos negativos y estabilidad temporal (Du et al., 2022; Zhou et al., 2022).

Para el prototipo, los prompts primarios se formulan en inglés. Esta decisión se apoya en la centralidad de ese idioma en los corpus y modelos visión-lenguaje utilizados como base, como CLIP, Conceptual Captions y CC12M, entrenados o construidos principalmente a partir de pares imagen-texto y recursos web en inglés (Changpinyo et al., 2021; Radford et al., 2021; Sharma et al., 2018). En consecuencia, el documento puede describir las condiciones en español, pero la capa de consulta del detector se diseña en inglés para favorecer la alineación con los patrones lingüísticos dominantes del preentrenamiento.

Cada prompt debe asociarse a una condición de riesgo, un texto de consulta, una estrategia de formulación, una versión y un conjunto de prompts activos. Una modificación de redacción debe registrarse como variante experimental, no como reemplazo informal. Esto permite explicar qué formulación produjo una detección y comparar resultados sin perder vínculo con la condición original.

El vocabulario activo representa el conjunto de prompts habilitados en una corrida. Su tamaño y composición afectan el comportamiento semántico del detector y, según el modelo, el costo de inferencia. Por ello, el núcleo validable debe trabajar con un vocabulario reducido y controlado: suficiente para evaluar sensibilidad de formulación, pero sin habilitar listas amplias que dificulten atribuir resultados.

También debe distinguirse entre prompt y estrategia de detección. Un prompt es una consulta semántica; una estrategia puede combinar prompts, postproceso, evidencia indirecta o reglas espaciales. Esta sección define el diseño y versionado de prompts. La integración entre condición, estrategia de detección, patrón y alerta se desarrolla posteriormente.

#### 17.3.6.4. Diseño inicial de prompts para el catálogo de condiciones

El diseño inicial de prompts contempla el catálogo completo de condiciones de riesgo, pero diferencia su tratamiento experimental. CR-01 y CR-02 conforman el vocabulario principal del núcleo validable. CR-03 y CR-04 se mantienen como candidatos condicionados para explorar evidencia visual parcial. Para CR-05 y CR-06 no se definen prompts integrados de la condición completa, sino consultas sobre entidades o elementos componentes, ya que su evaluación depende de reglas relacionales, zonas parametrizadas, tracking o contexto externo al prompt.

Esta organización permite que la configuración experimental sea completa sin sobredimensionar el prototipo experimental. El vocabulario activo de una corrida puede incluir sólo los prompts del núcleo validable o incorporar consultas adicionales cuando la corrida busque diagnóstico, comparación o evaluación parcial de condiciones condicionadas. En todos los casos, cada prompt debe quedar asociado a una condición de riesgo, una estrategia de formulación, una versión de configuración y un uso previsto.

La Tabla 45 presenta un vocabulario inicial en inglés alineado con el catálogo preliminar de prompts definido en la etapa metodológica. Las formulaciones candidatas no constituyen alertas por sí mismas: sólo producen evidencia perceptiva que el plano de control podrá evaluar como patrón cuando la configuración de corrida habilite los insumos necesarios.

Tabla 45Vocabulario inicial de prompts en inglés por condición de riesgo

| Condición | Eje de consulta | Formulaciones candidatas | Uso previsto |

| CR-01 — Persona sin casco | Prompt directo de ausencia | “person without hard hat”; “construction worker without safety helmet”. | Vocabulario principal del núcleo validable para producir evidencia sobre ausencia visible de casco. |

| CR-01 — Persona sin casco | Estado observable | “person with bare head on construction site”. | Variante sin negación directa, útil para contrastar sensibilidad del modelo frente al concepto de ausencia. |

| CR-01 — Persona sin casco | Consulta positiva auxiliar | “person”; “worker”; “hard hat”; “safety helmet”. | Diagnóstico opcional de presencia de entidad o EPP; no confirma ausencia ni genera alerta por sí sola. |

| CR-02 — Persona sin chaleco reflectivo | Prompt directo de ausencia | “person without reflective vest”; “worker without high-visibility vest”. | Vocabulario principal del núcleo validable para producir evidencia sobre ausencia visible de chaleco. |

| CR-02 — Persona sin chaleco reflectivo | Descripción visual | “person without bright colored safety clothing”. | Variante orientada a atributos visuales de alta visibilidad. |

| CR-02 — Persona sin chaleco reflectivo | Consulta positiva auxiliar | “person”; “worker”; “reflective vest”; “safety vest”; “high visibility vest”. | Diagnóstico opcional de presencia de entidad o EPP; no confirma ausencia ni genera alerta por sí sola. |

| CR-03 — Trabajo en altura sin anticaídas visible | Consulta candidata compuesta | “person on scaffolding without harness”; “worker at height without fall protection equipment”. | Exploración condicionada; requiere contexto espacial y evidencia suficiente para evaluar el patrón completo. |

| CR-03 — Trabajo en altura sin anticaídas visible | Consulta descompuesta | “person on scaffolding”; “person on elevated platform”; “safety harness”; “fall arrest harness”. | Detección separada de persona en altura y elementos de protección para diagnóstico o evaluación parcial. |

| CR-04 — Borde elevado desprotegido con personas próximas | Consulta candidata compuesta | “unprotected edge with person nearby”; “elevated platform without guardrail near workers”. | Exploración condicionada; requiere proximidad, validación espacial y evidencia suficiente del entorno. |

| CR-04 — Borde elevado desprotegido con personas próximas | Consulta descompuesta | “platform edge”; “open edge”; “guardrail”; “safety railing”; “person near edge”. | Detección separada de borde, protección colectiva y persona próxima; no confirma el patrón completo por sí sola. |

| CR-05 — Maquinaria cerca de peatones | Entidades de maquinaria | “excavator”; “backhoe loader”; “dump truck”; “crane”; “heavy machinery”. | Detección de entidades componentes; la condición completa requiere proximidad y persistencia temporal entre entidades. |

| CR-05 — Maquinaria cerca de peatones | Entidades humanas | “person”; “construction worker”; “pedestrian”. | Detección de entidades humanas para evaluación relacional posterior. |

| CR-06 — Persona en zona restringida | Entidad persona | “person”; “worker”; “pedestrian”. | Entidad cuya posición se evalúa contra una zona o polígono declarado en la configuración de corrida. |

| CR-06 — Persona en zona restringida | Elementos auxiliares de entorno | “restricted area sign”; “caution tape”; “warning tape”; “barrier”; “safety cone”. | Referencias visuales complementarias; no reemplazan la definición externa de la zona restringida. |



Nota. Las formulaciones son candidatas iniciales y deben registrarse por versión. Las consultas indirectas, descompuestas o auxiliares son entradas independientes al detector y su uso depende del modelo y de la configuración de corrida. CR-01 y CR-02 integran el vocabulario principal; CR-03 a CR-06 se mantienen como vocabulario condicionado, ya que su confirmación requiere reglas relacionales, zonas, tracking o contexto externo al prompt.

#### 17.3.6.5. Reglas de comparabilidad entre configuraciones

La configuración debe permitir comparar variantes sin producir conclusiones ambiguas. Al comparar prompts, deben mantenerse constantes modelo, fuente visual, resolución, política de muestreo, umbrales, postproceso y criterios de patrón. Así, una variación de desempeño puede atribuirse razonablemente a la formulación evaluada.

Al comparar modelos OVD, debe conservarse el mismo conjunto de prompts y condiciones equivalentes de fuente, resolución y postproceso. Si un modelo requiere umbrales distintos por la escala de sus puntajes, esa diferencia debe declararse como parte de la configuración y no ocultarse como detalle de implementación.

Al comparar DBE y EBE, debe declararse que cambia la naturaleza temporal de la fuente. En EBE intervienen captura continua, variabilidad de iluminación, codificación o decodificación cuando corresponda, continuidad temporal, omisiones, descartes y disponibilidad efectiva de frames. Por lo tanto, las diferencias observadas no deben atribuirse automáticamente al detector OVD.

#### 17.3.6.6. Validaciones previas al inicio de la corrida

La configuración debe validarse antes de iniciar la ejecución. No debería comenzar una corrida sin fuente visual, modelo OVD seleccionado, vocabulario activo, umbrales mínimos y política básica de registro. Tampoco debería evaluarse una alerta si no existe al menos un patrón activo con criterio de confirmación definido.

Las métricas deben declararse según sus condiciones de aplicación. Una métrica temporal requiere continuidad suficiente y eventos instrumentados; una métrica de tracking requiere tracker habilitado y, si corresponde, anotaciones de identidad; una métrica de distribución externa sólo aplica si la corrida habilita ese canal.

La evidencia visual y los módulos opcionales deben quedar explícitamente habilitados. Snapshots, clips, recortes, tracker, zonas, preselección en el rol de captura/ingesta o distribución externa no deben operar como comportamientos implícitos, porque modifican la interpretación de latencia, cobertura temporal, privacidad o aplicabilidad de métricas.

#### 17.3.6.7. Frontera con los planos de ejecución y el soporte experimental

La configuración define los parámetros que consume el plano de medios: fuente visual, resolución, política de muestreo, modelo OVD, vocabulario activo, umbrales y postproceso. El plano de medios no diseña ni versiona estos elementos; los aplica para producir evidencia perceptiva normalizada y propaga sus referencias en los eventos publicados.

Para el plano de control, la configuración define patrones activos, severidad conceptual, ventanas temporales, histéresis y criterios de confirmación. El plano de control no debe convertir detecciones en alertas por reglas locales no documentadas, sino evaluar la evidencia de acuerdo con lo declarado para la corrida.

Para el soporte experimental, la configuración funciona como clave de reconstrucción. Eventos, métricas, errores, descartes, alertas internas, reportes y evidencia visual asociada deben poder rastrearse hasta la configuración que les dio origen. Con esta delimitación, cada resultado queda asociado a una corrida, cada prompt conserva trazabilidad y cada comparación declara sus variables principales.

### 17.3.7. Diseño conceptual del plano de medios

El plano de medios se materializa en el componente lógico Pipeline de Medios de la plataforma experimental. Este componente concentra la ruta sensible a latencia: inicia cuando el adaptador de ingesta visual recibe, lee o decodifica una unidad visual proveniente de una fuente externa, y finaliza cuando se publica evidencia perceptiva normalizada hacia la frontera de integración. Su alcance incluye ingesta, decodificación cuando corresponda, control de ritmo, normalización visual, inferencia open-vocabulary, postproceso y publicación no bloqueante.

El límite del componente es estricto. El Pipeline de Medios no confirma condiciones de riesgo, no asigna severidad, no ejecuta reglas de patrón, no genera alertas y no depende de persistencia pesada para continuar procesando frames. Su salida representa evidencia perceptiva primaria asociada a una corrida, una fuente, una referencia temporal, un modelo y una configuración de procesamiento. La interpretación de esa evidencia corresponde al plano de control.

La separación protege la ruta frame-evento frente a tareas que pueden introducir bloqueo o variabilidad, como la evaluación de patrones, la reconstrucción histórica, la generación de reportes, la inspección visual o la distribución de notificaciones externas. La sección precisa cómo debe comportarse el componente que transforma entrada visual en evidencia perceptiva utilizable por el resto del sistema.

Las fuentes utilizadas en DBE y EBE ingresan al Pipeline de Medios mediante una misma frontera conceptual: el adaptador de ingesta visual. La diferencia entre ambos escenarios se resuelve en la forma de lectura, disponibilidad del frame, metadatos temporales y control de ritmo, no en la salida del plano. En DBE predomina la lectura reproducible; en EBE pueden aparecer irregularidad temporal, atraso acumulado, variabilidad de captura o disponibilidad de frames recientes. En ambos casos, la salida debe conservar trazabilidad suficiente para reconstruir qué se procesó, bajo qué configuración y con qué resultado.

La configuración experimental actúa como entrada transversal del Pipeline de Medios, pero no es una responsabilidad interna de este plano. Fuente, resolución, política conceptual de selección o muestreo, modelo, prompts activos, umbrales y modo de inferencia son definidos por la configuración de corrida. El plano de medios debe consumir esa configuración, aplicarla durante la ejecución y propagar sus identificadores en la evidencia publicada, sin convertirse en el módulo encargado de gobernarla o versionarla.

Figura x

Flujo conceptual del Pipeline de Medios

Nota. La figura representa el flujo interno del plano de medios. Las fuentes visuales son externas al plano; el plano comienza en el adaptador de ingesta visual, responsable de recibir, leer o decodificar la fuente y transformarla en una unidad visual procesable. La configuración de corrida parametriza la ejecución como entrada transversal, sin formar parte del procesamiento frame a frame. El evento de percepción normalizado se ubica por fuera del recuadro para señalar la frontera de salida hacia el bus interno de eventos y el plano de control.

#### 17.3.7.1. Flujo operativo del Pipeline de Medios

El flujo interno del Pipeline de Medios se organiza como una cadena de transformación progresiva. Cada etapa recibe una representación visual o perceptiva, aplica una operación acotada y entrega una salida que mantiene relación con la corrida y con la referencia temporal original. Esta organización permite sustituir fuentes, modelos o políticas de procesamiento sin modificar la responsabilidad general del plano.

Ingesta y decodificación. La primera responsabilidad interna del plano de medios es recibir la entrada visual desde fuentes externas, como datasets, imágenes, videos locales, cámaras o streams. La fuente queda encapsulada por un adaptador de ingesta visual que oculta diferencias de formato sin eliminar información relevante para la evaluación. Cuando la entrada proviene de vídeo codificado o streaming, la decodificación convierte el flujo en frames procesables y registra la información necesaria para distinguir disponibilidad, recepción, orden lógico y referencia temporal. En DBE suele alcanzar con conservar índice de secuencia y orden de lectura; en EBE puede ser necesario registrar además timestamps de captura o recepción, irregularidad temporal y eventuales descartes por atraso.

Control de ritmo y selección de unidades visuales. Antes de ingresar a inferencia, el pipeline debe decidir qué unidades visuales serán efectivamente procesadas. Esta decisión puede consistir en aceptar todos los frames, aplicar una selección determinista, reducir la frecuencia de procesamiento o priorizar unidades recientes cuando existe captura continua. Lo importante para el diseño no es imponer una política concreta, sino evitar decisiones invisibles: toda unidad omitida, reemplazada o descartada debe quedar asociada a una causa y a una política declarada en la corrida. Los detalles concretos de colas, buffers o algoritmos de descarte corresponden a la implementación.

Normalización visual. El frame aceptado se adapta a los requisitos del modelo seleccionado. Esta etapa puede modificar resolución, formato, espacio de color, disposición de tensores o escala de entrada. El diseño debe preservar la relación entre coordenadas originales y coordenadas de inferencia, porque esa relación permite interpretar cajas delimitadoras, revisar evidencia visual y comparar resultados entre configuraciones con distinta resolución. Reescalado, recortes o letterbox no deben tratarse como operaciones invisibles.

Inferencia open-vocabulary. La inferencia ejecuta el detector configurado sobre la entrada normalizada y el conjunto de prompts activos. El modelo se integra mediante un adaptador para evitar que el resto del plano dependa de una salida particular de Grounding DINO, YOLOE u otro candidato. Esta etapa produce resultados crudos: cajas, puntajes, etiquetas, frases asociadas o estructuras equivalentes, según el formato propio del detector utilizado.

Postproceso y normalización de detecciones. Luego de la inferencia, el Pipeline de Medios aplica los filtros definidos por la configuración de corrida —umbrales, supresión de detecciones redundantes, normalización de etiquetas y remapeo de coordenadas— para convertir las salidas del modelo en evidencia perceptiva común. Esta salida queda asociada al frame, prompt, condición y nivel de confianza correspondiente, pero no interpreta riesgo ni genera alertas; sólo entrega evidencia normalizada al plano de control.

Publicación de evidencia perceptiva. La publicación cierra el plano de medios. La evidencia normalizada se entrega como evento liviano hacia la frontera de integración, asociado a corrida, fuente, referencia temporal, modelo, prompts y timestamps relevantes. A partir de ese punto, la evidencia puede ser evaluada por el plano de control, persistida de manera reconstruible o inspeccionada por componentes de soporte; ninguna de esas tareas debe ser requisito para que el Pipeline de Medios continúe procesando la siguiente unidad visual.

#### 17.3.7.2. Criterios de diseño aplicados al plano de medios

Los criterios de diseño del plano de medios no agregan nuevas decisiones generales respecto de la arquitectura ya definida; traducen esas decisiones al comportamiento específico de la ruta frame-evento. El objetivo es que el procesamiento visual sea medible, sustituible y defendible sin mezclarlo con lógica de patrones, persistencia pesada o salidas externas.

El primer criterio es mantener una ruta no bloqueante. La inferencia y la publicación de evidencia no deben esperar indefinidamente a consumidores posteriores. Si el bus interno, la persistencia, la inspección o una salida externa fallan o se saturan, esa condición debe registrarse como parte de la ejecución, pero no debe convertir a esos consumidores en dependencia directa del procesamiento visual.

El segundo criterio es hacer visible la variabilidad temporal. En video, una latencia aparentemente baja puede ocultar pérdida de frames, colas saturadas o reemplazo de frames antiguos por frames recientes. Por eso, el Pipeline de Medios debe registrar timestamps por tramo, profundidad de cola cuando corresponda, frames aceptados, frames omitidos y descartes. La pérdida de evidencia no puede quedar fuera de la interpretación experimental.

El tercer criterio es encapsular la heterogeneidad de modelos. Los detectores OVD pueden diferir en formato de entrada, tipo de prompt, estructura de salida, semántica de puntajes y costo de inferencia. El plano de medios debe absorber esa heterogeneidad mediante adaptadores y entregar una evidencia perceptiva estable. De ese modo, el plano de control no queda acoplado a un modelo específico ni a detalles internos de su implementación.

El cuarto criterio es conservar la trazabilidad mínima del resultado perceptivo. Cada evidencia publicada debe poder asociarse con la corrida, la fuente, la referencia temporal, el modelo utilizado, los prompts activos y la política de procesamiento aplicada. Esta trazabilidad no implica almacenar video crudo de manera continua ni resolver la reconstrucción histórica dentro del plano de medios; implica producir eventos suficientes para que el soporte experimental pueda reconstruir la corrida posteriormente.

El quinto criterio es no trasladar responsabilidades del plano de control hacia el plano de medios. La persistencia temporal de un patrón, la histéresis, la severidad y el registro interno de alerta pertenecen al motor de patrones. El plano de medios puede mejorar la calidad de la evidencia perceptiva, pero no debe decidir si una condición observada se convirtió en una situación de riesgo confirmada.

#### 17.3.7.3. Control de ritmo según tipo de fuente

La política de control de ritmo se define por corrida y afecta qué evidencia visual llega a inferencia. En el diseño del plano de medios, esta política no se trata como una optimización secundaria, sino como parte de la configuración que condiciona la lectura de resultados. Cambiar la selección de unidades visuales, la frecuencia de procesamiento o el criterio de omisión equivale a cambiar la variante experimental evaluada.

En corridas DBE, o en general con fuentes pulleables como datasets, imágenes, videos locales o archivos, el lector puede regularse sin pérdida temporal de evidencia. Por ello, la prioridad arquitectónica es preservar reproducibilidad, orden lógico y trazabilidad de las unidades visuales procesadas. Si no se procesan todos los frames, la selección debe ser determinista, declarada en la configuración y mantenida constante entre corridas comparables.

En corridas EBE, o en general con fuentes vivas como cámaras, streams o capturas continuas, la escena evoluciona aunque la inferencia se retrase. Por ello, el diseño debe priorizar que el atraso acumulado no crezca indefinidamente y que toda omisión, irregularidad temporal o descarte quede registrado. La estrategia concreta de selección de unidades visuales se declara en la configuración efectiva de cada corrida; su efecto sobre latencia, cobertura temporal y evidencia disponible debe ser observable desde el diseño.

La preselección liviana en el rol de captura o ingesta sólo debe considerarse como una variante de EBE cuando exista una justificación experimental clara. Puede reducir carga sobre el flujo central, pero introduce riesgo de descartar evidencia antes de la inferencia OVD. Si se utiliza, el criterio debe ser conservador, explícito y registrado; de lo contrario, no debe formar parte del flujo base del núcleo validable.

El resultado esperado de esta política no es maximizar FPS de forma aislada, sino hacer interpretable el comportamiento del pipeline. Un sistema que procesa menos frames puede ser válido para una corrida exploratoria o comparativa, pero esa reducción debe ser visible para no confundir rendimiento con cobertura temporal.

#### 17.3.7.4. Relación con configuración, modelos y prompts

El Pipeline de Medios consume la configuración experimental definida para la corrida, pero no la gobierna. Al iniciar la ejecución, recibe los parámetros necesarios para procesar la fuente visual: política de muestreo, resolución de procesamiento, modelo OVD seleccionado, vocabulario activo, umbrales de inferencia y criterios de postproceso. Esta configuración debe permanecer estable durante la corrida, salvo que se registre una nueva configuración experimental.

Los prompts activos funcionan como contexto semántico de la inferencia. El plano de medios no diseña ni valida metodológicamente las formulaciones lingüísticas; utiliza el conjunto declarado en la configuración y conserva su referencia en la evidencia perceptiva publicada. Cuando el modelo lo permita, puede reutilizar representaciones textuales precalculadas o mecanismos equivalentes para reducir costo de inferencia, siempre que esa optimización no altere la trazabilidad de la corrida.

La salida del Pipeline de Medios debe incluir referencias suficientes para reconstruir el origen de cada evidencia: configuración de corrida, fuente, frame o timestamp, modelo utilizado, conjunto de prompts, prompt asociado cuando corresponda, umbrales aplicados y versión del esquema de salida. Esta información no agrega interpretación de riesgo; sólo permite que el plano de control evalúe patrones sobre evidencia trazable y que el soporte experimental explique resultados, omisiones, errores o variaciones de latencia.

En consecuencia, la salida del plano de medios no debe reducirse a cajas y puntajes sin contexto, pero tampoco debe incorporar severidad, confirmación de patrón o decisión de alerta. Su producto es evidencia visual primaria, normalizada y trazable. La interpretación de esa evidencia corresponde al plano de control; la comparación entre configuraciones, modelos y prompts corresponde al análisis experimental posterior.

#### 17.3.7.5. Capacidades opcionales sin desplazar el núcleo validable

El núcleo validable del plano de medios debe poder operar sin exigir seguimiento multiobjeto formal, preselección en borde ni adaptación de modelos al dominio. Estas capacidades pueden incorporarse como variantes del flujo, pero no deben convertirse en requisitos para demostrar el procesamiento básico de CR-01 y CR-02.

El tracking o MOT puede ubicarse después del postproceso cuando resulte necesario estabilizar entidades, reducir oscilaciones entre frames o entregar identificadores temporales al plano de control. Aun así, un identificador temporal no equivale a una condición de riesgo sostenida. La decisión de que una detección persistió durante una ventana temporal sigue perteneciendo al motor de patrones.

Las variantes de ejecución orientadas a eficiencia deben tratarse con el mismo criterio: pueden ser útiles durante la implementación, pero no deben ocupar el centro del diseño conceptual del plano de medios. Reducciones de resolución, cambios de modo de inferencia o exportaciones a motores optimizados corresponden a decisiones de implementación y evaluación posterior; en esta sección sólo interesa fijar que cualquier variante que altere la ruta frame-evento debe quedar declarada en la configuración de corrida.

Con esta delimitación, el Pipeline de Medios queda definido como una ruta de transformación acotada y medible: recibe entrada visual, controla el ritmo de procesamiento, ejecuta inferencia OVD, normaliza resultados y publica evidencia perceptiva. La confirmación de patrones, el registro de alertas y la distribución posterior de salidas quedan fuera de su responsabilidad directa, preservando la separación entre baja latencia y lógica de control.

### 17.3.8. Diseño conceptual del plano de control

El plano de control concentra la interpretación de la evidencia perceptiva producida por el plano de medios. Su responsabilidad comienza cuando ingresa un evento de percepción normalizado y termina cuando el sistema registra estados de patrón, alertas internas, eventos persistibles, métricas y salidas de inspección o distribución desacopladas. A diferencia del Pipeline de Medios, no procesa frames crudos ni necesita operar al ritmo constante de captura; trabaja sobre eventos y sobre cambios de estado derivados de reglas configuradas.

La separación entre detección, patrón y alerta es la decisión arquitectónica central de esta sección. Una detección puntual expresa una observación del modelo sobre una unidad visual; un patrón confirmado expresa que esa evidencia fue evaluada durante una ventana temporal bajo criterios explícitos de persistencia, umbral e histéresis; una alerta interna registra un episodio asistivo generado por una transición válida del patrón. Por lo tanto, el plano de control no debe transformar cada detección en una alerta, sino estabilizar la evidencia antes de producir salidas operativas.

Esta organización evita que la variabilidad propia de la inferencia OVD —falsos positivos, falsos negativos, fluctuación de puntajes, sensibilidad al prompt u oclusiones parciales— se traslade directamente al sistema de alertas. También permite mantener al plano de medios aislado de consumidores lentos, persistencia histórica, reportes, notificaciones externas o interfaces de inspección. El plano de control puede ejecutar esas funciones de forma asíncrona sin bloquear la producción de evidencia perceptiva.

En el alcance del prototipo experimental, el plano de control se orienta principalmente al núcleo validable. Para CR-01 y CR-02, la evaluación puede resolverse mediante persistencia temporal simple y estados de patrón sin exigir seguimiento multiobjeto formal. El tracking, las zonas espaciales o las reglas relacionales pueden enriquecer escenarios posteriores, pero no deben convertirse en una dependencia del núcleo validable.

Figura x

Flujo conceptual del plano de control

Nota. La figura representa el flujo conceptual del plano de control. La configuración de corrida parametriza la evaluación como entrada transversal, sin formar parte del procesamiento evento a evento. El evento de percepción normalizado ingresa desde el plano de medios como entrada externa; dentro del plano se evalúan patrones, se actualizan estados y se derivan registros persistibles y métricas. La alerta interna por episodio se muestra por fuera del recuadro para indicar la frontera de salida del plano de control, quedando disponible para consumidores o adaptadores posteriores.

#### 17.3.8.1. Flujo lógico y responsabilidades del plano de control

El flujo lógico del plano de control puede describirse como una cadena de interpretación sobre eventos. Primero, se recibe evidencia perceptiva normalizada desde el bus interno de eventos. Luego, la evaluación de patrones determina si esa evidencia contribuye a una condición configurada. Si la evidencia acumulada supera los criterios definidos, se produce una transición de estado. Cuando esa transición alcanza el estado confirmado, se registra una alerta interna como episodio asistivo. En paralelo, la persistencia de eventos y la recolección de métricas permiten reconstruir la corrida y analizar su comportamiento.

El bus interno de eventos cumple una función de integración, no de razonamiento. Su tarea es desacoplar productores y consumidores: el plano de medios publica eventos de percepción, mientras que el plano de control los consume para evaluación, persistencia, métricas o inspección. El diseño no exige una tecnología específica de mensajería en esta instancia; exige, en cambio, que el intercambio sea explícito, trazable y no bloquee la ruta crítica de procesamiento visual.

Sobre esa entrada opera la evaluación de patrones, responsable de interpretar la evidencia perceptiva de acuerdo con definiciones de patrón, ventanas temporales, umbrales e histéresis. Esta responsabilidad no ejecuta inferencia visual ni certifica cumplimiento normativo; su función es transformar detecciones puntuales en estados de patrón operativamente interpretables.

Cuando un patrón alcanza una transición válida a estado confirmado, el plano de control registra una alerta interna. Esta alerta no equivale a una notificación externa ni a una acción automática sobre la obra, sino a un evento asistivo trazable que indica que la condición configurada alcanzó los criterios definidos para la corrida. Para evitar duplicaciones, la generación de alertas debe operar por episodios o transiciones de estado, no por cada frame con evidencia positiva.

La trazabilidad se sostiene mediante un repositorio de eventos con escritura append-only, orientado a conservar los hechos relevantes de la ejecución: eventos de percepción consumidos, cambios de estado, alertas internas, resoluciones y referencias a la configuración de corrida. Este repositorio no reemplaza al bus interno ni debe participar en la ruta crítica del plano de medios; su función es permitir reconstrucción experimental, auditoría técnica y análisis posterior de resultados. De manera complementaria, la recolección de métricas y la interfaz mínima de inspección derivan reportes, conteos, estados y evidencia de corrida sin modificar la lógica de activación ni decidir estados de patrón.

#### 17.3.8.2. Evaluación de patrones y máquina de estados

La evaluación de patrones materializa la transición entre evidencia perceptiva y situación operativamente relevante. El plano de control no trabaja sobre frames crudos, sino sobre eventos de percepción normalizados, asociados a una corrida, fuente, referencia temporal, modelo, prompts activos y política de procesamiento. A partir de esa evidencia, evalúa si una condición de riesgo alcanza los criterios definidos en la configuración experimental.

Para CR-01 y CR-02, la evaluación puede mantenerse deliberadamente simple. La evidencia positiva se acumula dentro de una ventana temporal configurable y se contrasta contra criterios de persistencia, confianza mínima e histéresis. El patrón se confirma sólo cuando la evidencia alcanza el umbral definido para la corrida; luego se mantiene activo mientras la señal continúa y se resuelve cuando la ausencia se sostiene durante el margen configurado. Esta estrategia permite estabilizar detecciones sin exigir seguimiento multiobjeto formal en el núcleo validable.

La máquina de estados propuesta distingue cinco momentos conceptuales: sin evidencia, candidato, confirmado, sostenido y resuelto. Esta separación permite evitar que una observación aislada produzca una alerta directa y, al mismo tiempo, permite modelar episodios de riesgo con inicio, confirmación, duración y cierre. La transición a confirmado habilita el registro de una alerta interna por episodio; los estados posteriores actualizan duración, evidencia y métricas sin duplicar la alerta principal.

La confirmación del patrón no debe interpretarse como certificación normativa ni como decisión automática de intervención. Significa que, bajo la configuración de corrida y la evidencia disponible, el sistema alcanzó las condiciones internas de activación. La evaluación final sobre cumplimiento, prioridad de acción o medida preventiva permanece fuera del sistema automatizado y corresponde a la supervisión humana.

Figura xMáquina de estados conceptual del patrón de riesgo

Nota. La transición a confirmado registra la alerta interna asistiva. Mientras el patrón permanece sostenido, el sistema actualiza el episodio y sus métricas sin generar alertas principales repetidas. La resolución cierra el episodio y habilita futuras activaciones independientes si vuelve a acumularse evidencia suficiente.

En la lectura de la máquina de estados, el estado sin evidencia representa la ausencia de señales suficientes para activar un patrón. El estado candidato aparece cuando existe evidencia inicial compatible con la condición, pero todavía no se alcanza persistencia o confianza agregada suficiente. El estado confirmado se alcanza cuando la evidencia supera el criterio configurado y habilita el registro de una alerta interna por episodio. Luego, el estado sostenido mantiene activo el episodio mientras la evidencia continúa, actualizando duración, métricas y evidencia asociada sin duplicar la alerta principal. Finalmente, el estado resuelto cierra el episodio cuando la ausencia se mantiene durante el margen definido o se cumple la condición de histéresis, habilitando futuras activaciones independientes.

#### 17.3.8.3. Motor de evaluación de patrones de riesgo

El motor de evaluación de patrones de riesgo es el componente lógico del plano de control encargado de transformar evidencia perceptiva normalizada en estados de patrón, episodios y alertas internas. No procesa imágenes ni ejecuta inferencia OVD; consume los eventos publicados por el plano de medios, consulta las definiciones activas de patrón declaradas en la configuración experimental y actualiza el estado correspondiente dentro de la corrida.

Su función arquitectónica es cerrar la brecha entre detección visual y salida operativa asistiva. Una detección indica que el modelo observó una evidencia en un frame o instante determinado; un patrón confirmado indica que esa evidencia fue evaluada bajo criterios de persistencia, umbral, histéresis y, cuando corresponda, reglas espaciales o contextuales. Por lo tanto, el motor constituye la frontera donde la evidencia perceptiva deja de ser una salida aislada del detector y pasa a formar parte de una interpretación temporal trazable.

El motor se diseña para admitir el catálogo completo de patrones del prototipo, pero su activación efectiva depende de la configuración de corrida, los módulos habilitados y la disponibilidad de evidencia suficiente. De este modo, la arquitectura puede incorporar progresivamente patrones de mayor complejidad sin modificar la lógica central del plano de control.

##### 17.3.8.3.1. Patrón de riesgo como unidad evaluable

El motor no evalúa condiciones de riesgo sueltas, sino patrones de riesgo activos. Cada patrón referencia una condición del catálogo y define cómo esa condición debe ser evaluada durante la corrida. De este modo, la condición conserva el significado semántico del riesgo observado, mientras que el patrón agrega criterios operativos de activación, sostenimiento y cierre.

Esta separación evita que el sistema dependa de reglas rígidas incorporadas directamente en el código. Una misma condición puede evaluarse mediante distintas estrategias de evidencia, umbrales, ventanas temporales o dependencias opcionales, siempre que la configuración experimental lo declare. El patrón funciona, por lo tanto, como una definición evaluable: indica qué evidencia acepta, durante cuánto tiempo debe sostenerse, qué severidad tiene, qué histéresis aplica y qué evento debe emitirse cuando cambia de estado.

El motor opera sobre patrones de riesgo configurados. Cada patrón referencia una condición observable del catálogo CR-01 a CR-06 y define cómo esa condición será evaluada dentro del plano de control: evidencia requerida, ventana temporal, umbrales, histéresis, severidad y dependencias opcionales. En este sentido, la codificación PR-01 a PR-06 se utiliza como recurso de trazabilidad arquitectónica para distinguir la condición observada de la regla operativa que la evalúa.

Tabla 46

Componentes mínimos de una definición de patrón de riesgo

| Componente | Contenido esperado | Función en el motor |

| Identificación del patrón | Código del patrón, condición de riesgo asociada y versión de definición. | Permite rastrear qué regla evaluó la evidencia y bajo qué configuración. |

| Evidencia requerida | Tipo de detecciones, prompts, entidades o relaciones que pueden alimentar el patrón. | Define qué eventos de percepción son relevantes y cuáles deben descartarse para ese patrón. |

| Criterio temporal | Ventana de evaluación, duración mínima, frecuencia o proporción de evidencia positiva. | Evita que una detección aislada active una alerta y permite medir persistencia. |

| Umbrales de activación | Confianza mínima, cantidad mínima de evidencias o criterio agregado de suficiencia. | Determina cuándo el patrón pasa de candidato a confirmado. |

| Histéresis y cierre | Condición de ausencia sostenida, margen de tolerancia o criterio de resolución. | Evita oscilaciones por oclusiones breves, caídas de confianza o pérdidas momentáneas. |

| Severidad configurada | Nivel conceptual de severidad asociado al patrón dentro de la corrida. | Permite interpretar prioridad, latencia esperada y reporte de episodios sin automatizar decisiones humanas. |

| Dependencias opcionales | Tracking, zonas, reglas espaciales, polígonos, relaciones entre entidades o preselección. | Habilita extensiones condicionadas sin convertirlas en dependencia del núcleo validable. |

| Salida esperada | Transición de estado, alerta interna por episodio, métrica o evento de descarte. | Conecta evaluación lógica, persistencia de eventos y reconstrucción experimental. |



Nota. La tabla presenta componentes lógicos de diseño, no una especificación cerrada de implementación. Los nombres concretos de campos o estructuras se refinan en los contratos preliminares de la arquitectura.

En particular, la severidad no debe derivarse de una detección aislada en un frame, sino de la definición del patrón y del catálogo metodológico consolidado. En el núcleo del prototipo, este valor es estático por corrida: orienta la interpretación de prioridad y latencia esperada, pero no se recalcula frame a frame ni depende de la inferencia OVD, de la publicación de evidencia perceptiva ni de los mecanismos de distribución externa. Cualquier ajuste posterior de severidad por zona, proximidad, persistencia o combinación de condiciones corresponde a extensiones condicionadas y debe declararse explícitamente en la configuración de corrida.

##### 17.3.8.3.2. Memoria temporal y ciclo de evaluación

Durante una corrida, el motor mantiene una memoria temporal asociada a la fuente, la condición evaluada y el patrón activo. Para los patrones del núcleo validable, esta memoria puede organizarse por fuente y condición, sin exigir identidad persistente de persona. Cuando una corrida habilite tracking, zonas o relaciones espaciales, la memoria del motor deberá incorporar esos insumos para diferenciar episodios simultáneos, sostener relaciones entre entidades o aplicar reglas dependientes del contexto.

El ciclo de evaluación se inicia cuando ingresa un evento de percepción normalizado. El motor selecciona las detecciones relevantes para los patrones activos, las agrupa dentro de la ventana temporal configurada y determina si la evidencia acumulada alcanza el criterio definido. Si la evidencia positiva supera el umbral de activación, el patrón puede pasar de candidato a confirmado; si la evidencia continúa, el episodio se mantiene sostenido; y si la ausencia se conserva durante el margen de cierre, el episodio se resuelve.

La histéresis cumple una función central en este ciclo. Un patrón no debe activarse por una detección aislada ni cerrarse por una pérdida momentánea del detector, una oclusión breve o una caída puntual de confianza. Por ello, el motor debe distinguir entre ausencia real de evidencia, descarte por política de muestreo, falla de fuente, pérdida de track cuando corresponda, oscilación del modelo y cierre válido del episodio.

##### 17.3.8.3.3. Evaluación según niveles de complejidad del catálogo

El motor debe respetar la clasificación metodológica de condiciones por nivel de complejidad ya definida en el desarrollo metodológico. Desde el diseño arquitectónico, esa clasificación se traduce en distintos requisitos de evaluación: algunos patrones pueden resolverse con evidencia perceptiva y persistencia temporal simple, mientras que otros sólo deben activarse cuando la corrida habilite insumos adicionales como tracking, zonas parametrizadas o reglas espaciales.

Esta diferenciación permite diseñar un motor único sin sobredimensionar el prototipo experimental. La arquitectura mantiene una lógica común de evaluación, pero adapta sus entradas y criterios según el patrón activo y la configuración de corrida. De este modo, el plano de control puede incorporar condiciones más complejas sin rediseñarse, siempre que existan los insumos necesarios para evaluarlas de manera trazable.

Tabla 47

Diseño del motor de patrones según condición de riesgo

| Patrón y condición asociada | Evidencia y regla de evaluación | Dependencias arquitectónicas | Tratamiento en el prototipo |

| PR-01 / CR-01 — Persona sin casco | Evidencia OVD directa de persona sin casco o evidencia auxiliar de persona y casco. El motor acumula evidencia positiva por fuente y ventana temporal, aplica confianza mínima, persistencia e histéresis. | Plano de medios con prompts activos, postproceso normalizado y timestamps. No requiere MOT formal para el núcleo. | Núcleo validable obligatorio. Debe producir patrón candidato, confirmado, sostenido, resuelto y alerta interna por episodio. |

| PR-02 / CR-02 — Persona sin chaleco reflectivo | Evidencia OVD directa de persona sin chaleco reflectivo o evidencia auxiliar de persona y chaleco. El motor evalúa persistencia temporal bajo umbral y cierre configurado. | Plano de medios con prompts activos, postproceso normalizado y timestamps. No requiere MOT formal para el núcleo. | Núcleo validable obligatorio. Se evalúa con la misma lógica base que PR-01, ajustando prompts y umbrales por condición. |

| PR-03 / CR-03 — Trabajo en altura sin anticaídas visible | Evidencia de persona en altura o sobre estructura elevada, junto con ausencia o baja evidencia de sistema anticaídas visible. El motor requiere validar contexto espacial antes de confirmar. | OVD sobre entidades o atributos, reglas espaciales intra-frame y evidencia visual suficiente del escenario. | Extensión condicionada. No bloquea el núcleo; sólo debe activarse si existen datos o escenas que permitan evaluar la condición completa. |

| PR-04 / CR-04 — Borde elevado desprotegido con personas próximas | Evidencia de borde, plataforma o zona elevada, ausencia de baranda o protección colectiva y presencia de personas próximas. El motor evalúa proximidad y condición de protección. | OVD de entidades del entorno, reglas espaciales, posible parametrización de regiones y cámara con perspectiva adecuada. | Extensión condicionada. Puede reportarse parcialmente si sólo se detectan componentes visuales sin validar la condición completa. |

| PR-05 / CR-05 — Maquinaria cerca de peatones | Evidencia de maquinaria y personas con relación de proximidad sostenida. El motor evalúa distancia relativa, duración del acercamiento y persistencia del episodio. | OVD de entidades, seguimiento temporal o asociación equivalente, reglas de proximidad y métricas de continuidad. | Condicionado a módulo contextual. No pertenece al núcleo; requiere instrumentación temporal y control de falsos positivos relacionales. |

| PR-06 / CR-06 — Persona en zona restringida | Evidencia de persona dentro de un polígono o zona definida externamente. El motor evalúa permanencia, entrada, salida y cierre por ausencia sostenida. | Cámara fija o geometría controlada, polígono de zona, OVD de persona y, preferentemente, tracking o asociación temporal. | Condicionado a escenario EBE controlado o fuente fija. Requiere parametrización explícita de zona en la configuración de corrida. |



Nota. La tabla diseña el comportamiento esperado del motor frente al catálogo completo de patrones. El tratamiento “núcleo validable” identifica patrones obligatorios para el prototipo experimental; el tratamiento “extensión condicionada” indica capacidades previstas que sólo deben habilitarse cuando existan datos, módulos e instrumentación suficientes.

##### 17.3.8.3.4. Salidas, episodios y trazabilidad del motor

La salida principal del motor no es una alerta aislada, sino una secuencia de eventos derivados que describen el ciclo de vida del patrón: inicio de candidato, confirmación, sostenimiento, resolución o descarte por evidencia insuficiente. La alerta interna se registra sólo cuando una transición válida confirma el patrón. Esta decisión evita que el sistema emita alertas por cada frame positivo y permite analizar episodios con inicio, duración, evidencia causal y cierre.

Cada transición debe conservar trazabilidad suficiente para explicar su origen: configuración de corrida, patrón evaluado, condición asociada, evidencia considerada, ventana temporal, umbrales aplicados, estado previo, estado nuevo y referencia temporal. Esta información permite reconstruir por qué una alerta fue generada, por qué un episodio se resolvió, qué evidencia fue descartada y qué parámetros condicionaron el resultado.

Las métricas operativas del plano de control se apoyan en estas transiciones. El tiempo hasta la primera detección se vincula con la primera evidencia perceptiva relevante; la latencia de alerta interna se vincula con la transición a confirmado; la tasa de detección sostenida se vincula con la continuidad del episodio; y los errores o descartes permiten distinguir una ausencia real de evidencia de una falla técnica o una pérdida por muestreo.

De esta manera, el motor de evaluación de patrones permite que la arquitectura sostenga una cadena operativa completa: detección OVD, evidencia perceptiva normalizada, patrón candidato, patrón confirmado, alerta interna por episodio, sostenimiento, resolución y reconstrucción experimental. Con este diseño, CR-01 y CR-02 pueden implementarse como núcleo validable, mientras que los patrones más complejos permanecen incorporables sin alterar la separación entre plano de medios y plano de control.

#### 17.3.8.4. Transporte, persistencia y trazabilidad experimental

El diseño distingue el transporte de eventos de la persistencia histórica. El bus interno de eventos permite que productores y consumidores intercambien eventos durante la ejecución; el repositorio de eventos conserva una secuencia inmutable de hechos relevantes para reconstrucción experimental. Confundir ambas responsabilidades conduciría a dos riesgos opuestos: convertir la ruta de ejecución en una operación dependiente de almacenamiento pesado o, en sentido contrario, perder trazabilidad al tratar el bus como si fuera un registro histórico suficiente.

El repositorio de eventos debe funcionar bajo una lógica append-only. En lugar de sobrescribir estados, conserva hechos: evidencia recibida, patrón candidato, patrón confirmado, alerta interna registrada, episodio sostenido, episodio resuelto, errores de publicación, descartes relevantes y métricas de ejecución. Esta estructura permite reconstruir por qué una alerta ocurrió, qué evidencia la sostuvo, bajo qué configuración se ejecutó y qué condiciones de ausencia permitieron resolverla.

La trazabilidad es especialmente importante en un prototipo experimental. Permite comparar corridas con modelos, prompts, umbrales o políticas de muestreo diferentes; analizar falsos positivos y falsos negativos; justificar métricas temporales; y revisar decisiones sin depender de memoria volátil ni de capturas informales. En consecuencia, la persistencia no se incorpora como una función administrativa secundaria, sino como parte de la validez experimental del diseño.

Sobre los eventos persistidos pueden construirse proyecciones consultables para inspección, métricas o reportes. Estas proyecciones no reemplazan al historial append-only: funcionan como vistas derivadas que facilitan la lectura del estado actual, el resumen de episodios, el cálculo de indicadores o la revisión posterior de una corrida. Si una proyección se descarta o se recalcula, la secuencia causal de eventos debe seguir disponible en el repositorio.

Los adaptadores externos, cuando existan, deben ubicarse por fuera del plano de control y de su ruta crítica. Su función es consumir salidas ya producidas por el plano —por ejemplo, alertas internas o estados derivados— y transformarlas en notificaciones, integraciones o mensajes hacia otros canales. No definen la semántica de la alerta, no condicionan la evaluación de patrones y no participan en la persistencia principal de la corrida. De este modo, un consumidor lento, fallido o no instrumentado no afecta la activación interna, la conservación de la evidencia ni la reconstrucción experimental.

### 17.3.9. Integración entre condición, estrategia de detección, patrón y alerta

Esta sección precisa cómo las condiciones de riesgo definidas metodológicamente se materializan dentro de la arquitectura. Su finalidad es vincular la condición observable con una estrategia de detección, la evidencia perceptiva publicada por el plano de medios, la evaluación del patrón en el plano de control y el registro de una alerta interna por episodio. De este modo, la plataforma evita tratar los prompts como condiciones completas o las detecciones individuales como alertas directas, conservando una cadena causal trazable entre percepción, evaluación y salida asistiva.

#### 17.3.9.1. Cadena de traducción arquitectónica

La cadena de traducción comienza con una condición observable del catálogo metodológico. Esa condición define qué fenómeno se desea monitorear, pero no determina por sí misma cómo debe detectarse. La estrategia de detección cumple esa función: establece si la evidencia se buscará mediante un prompt directo, una combinación de consultas, evidencia auxiliar o reglas contextuales habilitadas por la configuración de corrida.

El plano de medios aplica la estrategia configurada y publica evidencia perceptiva normalizada. Esa evidencia queda asociada a la corrida, la fuente, el modelo, los prompts activos, los umbrales y la referencia temporal correspondiente. Sin embargo, todavía no constituye una alerta. Su función es alimentar al plano de control con información comparable y trazable.

El plano de control evalúa esa evidencia mediante el patrón de riesgo correspondiente. Allí se aplican criterios de persistencia, histéresis, severidad configurada y, cuando corresponda, reglas espaciales o temporales adicionales. Sólo cuando el patrón alcanza una transición válida a confirmado se registra una alerta interna por episodio. Esta alerta es una salida asistiva del sistema y no equivale a una notificación externa ni a una certificación normativa.

Figura x

Cadena de traducción entre condición, estrategia, evidencia, patrón y alerta

Nota. La figura muestra cómo una condición definida metodológicamente se materializa en la arquitectura. La estrategia orienta la producción de evidencia en el plano de medios; el patrón evalúa esa evidencia en el plano de control; y la alerta interna registra el episodio confirmado.

#### 17.3.9.2. Estrategia adoptada para el núcleo validable

Para el núcleo validable, la estrategia adoptada es la detección directa de condiciones de EPP mediante prompts configurados para CR-01 y CR-02. Esta decisión permite evaluar si un modelo OVD preentrenado produce evidencia suficiente sobre ausencia visible de casco o chaleco reflectivo, utilizando formulaciones controladas como parte del vocabulario activo de la corrida. La salida esperada de esta estrategia no es una alerta, sino evidencia perceptiva normalizada que será evaluada posteriormente por el motor de patrones.

La estrategia directa se adopta como punto de partida porque reduce dependencias arquitectónicas y permite cerrar una primera cadena experimental trazable. No requiere tracking formal, definición de zonas, reglas espaciales ni composición de múltiples entidades. Su función es producir evidencia mínima suficiente para que el plano de control evalúe persistencia, histéresis y confirmación del episodio.

Las consultas auxiliares positivas, como persona, casco o chaleco, pueden habilitarse con finalidad diagnóstica o comparativa. Su uso permite analizar falsos positivos, falsos negativos o ambigüedades visuales, pero no reemplaza la estrategia directa ni confirma por sí mismo una ausencia. Si se utilizan, deben declararse en la configuración de corrida y mantenerse separadas de la evidencia principal que alimenta el patrón.

Las estrategias indirectas, combinadas o contextuales quedan previstas como variantes configurables. Su incorporación sólo corresponde cuando la corrida habilite los insumos necesarios, como reglas espaciales, zonas, tracking o relaciones entre entidades. En todos los casos se conserva la misma cadena arquitectónica: la estrategia produce evidencia, el patrón evalúa relevancia operativa y la alerta interna registra el episodio confirmado.

#### 17.3.9.3. Trazabilidad de la cadena causal

Para que la integración sea reconstruible, cada evidencia publicada debe conservar vínculo con la condición que intenta representar, la estrategia de detección utilizada y la configuración efectiva de corrida. Esta relación permite explicar por qué una evidencia fue producida, omitida, descartada o incorporada a la evaluación de un patrón.

Del mismo modo, cada transición de patrón debe poder vincularse con la evidencia que la originó. La confirmación no es un hecho aislado: depende de detecciones acumuladas, criterios de persistencia, histéresis, severidad configurada y reglas activas. Por ello, la alerta interna debe poder reconstruirse desde la cadena completa: condición observable, estrategia de detección, evidencia perceptiva, patrón evaluado y transición a confirmado.

Esta trazabilidad permite comparar variantes sin alterar la semántica del sistema. Una misma condición puede evaluarse con distintas estrategias, siempre que la corrida declare la variante utilizada y los eventos resultantes conserven esa referencia.

### 17.3.10. Distribución de alertas confirmadas

La distribución de alertas confirmadas es el bloque que expone una alerta interna ya registrada hacia consumidores de inspección, reporte o integración experimental. Su importancia es operativa: permite que el resultado asistivo llegue a una interfaz, canal o sistema externo sin alterar la cadena causal que lo originó.

En la arquitectura propuesta, la unidad distribuida no debe tratarse como una nueva alerta, sino como un evento derivado de la alerta interna. Esta decisión permite distinguir tres hechos: la confirmación del episodio dentro del plano de control, el intento de distribución y el resultado de entrega o falla del canal habilitado.

La distribución se habilita por configuración de corrida y se mide como trayecto posterior. Una demora, error o ausencia de consumidor externo puede afectar la comunicación de la alerta, pero no modifica la validez del episodio confirmado ni la métrica principal de alerta interna.

#### 17.3.10.1. Función arquitectónica de la distribución

La distribución se activa a partir de una alerta interna confirmada. Toma el evento de alerta y construye una salida con contexto mínimo: corrida, patrón, condición asociada, severidad configurada, instante de confirmación, estado del episodio y referencias de evidencia cuando existan. Su función es comunicar o exponer un hecho ya producido por el plano de control, no volver a evaluarlo.

El diseño debe preservar una frontera estricta, primero se confirma el patrón y luego se distribuye la alerta. Un canal de mensajería, una interfaz de inspección o un adaptador externo no debe recalcular severidad, modificar estados de patrón ni crear alertas principales independientes. Si un consumidor falla, la arquitectura debe registrar la anomalía de distribución y mantener intacto el evento interno original.

Bajo esta delimitación, la distribución cumple una función asistiva y experimental. Puede orientar la atención humana, facilitar revisión de resultados o alimentar integraciones controladas, pero no constituye una decisión normativa ni una acción automática sobre la obra.

#### 17.3.10.2. Consumidores y adaptadores de salida

Las alertas confirmadas pueden exponerse hacia consumidores desacoplados. La arquitectura no impone un único canal ni convierte la notificación externa en requisito del núcleo validable. Cada consumidor debe declararse en la configuración de corrida, operar sobre alertas ya confirmadas y conservar la relación con el evento interno que le dio origen.

Los consumidores pueden cumplir finalidades distintas: inspección, reporte, comunicación asistiva o integración con herramientas externas. En todos los casos, deben trabajar con información controlada y no requerir acceso directo a frames crudos ni a estructuras internas del motor de patrones.

Tabla 48

Tipos de consumidores para alertas confirmadas

| Consumidor o adaptador | Uso previsto | Tratamiento arquitectónico |

| Interfaz de inspección | Visualizar alertas confirmadas, estado de episodio, métricas y evidencia asociada cuando exista. | Consumidor derivado; no modifica patrones ni confirma alertas. |

| Reporte experimental | Incorporar alertas confirmadas en el resumen de corrida, junto con configuración, métricas, errores y límites de interpretación. | Proyección posterior basada en eventos persistidos y señales observables. |

| Mensajería asistiva | Enviar una notificación breve a un canal humano configurado, como soporte de revisión o atención. | Adaptador opcional; su latencia y errores se miden por separado de la alerta interna. |

| MQTT o integración IoT | Publicar una alerta confirmada hacia un broker o sistema experimental externo. | Canal de integración; no debe accionar automáticamente sin supervisión humana ni alterar la semántica de la alerta. |

| Webhook o salida técnica | Integrar pruebas con otros componentes, herramientas de validación o servicios experimentales. | Extensión opcional sujeta a configuración, observabilidad y control de errores. |



Nota. La tabla presenta consumidores de alertas confirmadas, no componentes obligatorios del núcleo validable. Cada canal debe habilitarse por configuración de corrida y medirse como salida posterior a la alerta interna del sistema.

#### 17.3.10.3. Medición, errores y límites de interpretación

Cuando una corrida habilita distribución, la arquitectura debe registrar eventos de intento y resultado de entrega. Este registro no constituye un consumidor de alertas sino un mecanismo de observabilidad propio del tramo de distribución: permite diferenciar alerta confirmada, intento de distribución y entrega efectiva sin alterar la semántica del evento interno que le dio origen. A su vez, cada registro debe conservar la relación con la alerta interna original, el canal utilizado, el timestamp, el estado de entrega, los reintentos y el error producido si corresponde. Esta información permite reconstruir qué ocurrió después de la confirmación del patrón sin confundirlo con la activación interna del sistema.

La métrica principal de alerta corresponde al tiempo hasta la alerta interna confirmada. La latencia de distribución pertenece a un tramo posterior y sólo aplica cuando existe un consumidor habilitado. Si no se configura un canal externo, esa métrica debe declararse no aplicable; si el canal falla, la alerta interna sigue siendo válida y la entrega se registra como fallida o limitada.

Los reintentos de envío deben asociarse a la misma alerta interna y no generar nuevos episodios. Del mismo modo, una demora de notificación no debe reinterpretarse como demora del motor de patrones. La arquitectura debe conservar la diferencia entre alerta registrada, intento de distribución, entrega confirmada, entrega fallida y canal no habilitado.

Con este tratamiento, la distribución conecta el prototipo experimental con revisión humana, inspección e integraciones controladas sin ampliar la semántica de la alerta. El sistema conserva como hito principal la alerta interna y trata cualquier comunicación posterior como trayecto derivado, observable y opcional.

### 17.3.11. Contratos preliminares e interfaces internas

La arquitectura propuesta requiere que las responsabilidades definidas en el plano de medios, el plano de control y el soporte experimental se comuniquen mediante estructuras de intercambio explícitas. En este capítulo, esas estructuras se denominan contratos preliminares. Un contrato no representa todavía una clase definitiva, una API cerrada ni un esquema completo de validación; representa un acuerdo arquitectónico mínimo sobre qué información se intercambia, con qué significado y bajo qué condiciones puede ser interpretada por otra responsabilidad del sistema.

La función principal de estos contratos es proteger el desacoplamiento entre módulos sin anticipar una ingeniería de producto. El plano de medios debe poder sustituir una fuente, una política de muestreo, un adaptador de modelo o un postproceso sin obligar al plano de control a conocer detalles internos de implementación. Del mismo modo, la evaluación de patrones debe operar sobre evidencia perceptiva normalizada y no sobre frames crudos, salidas internas del detector o estructuras específicas de un modelo OVD particular.

La sección no busca definir una especificación técnica exhaustiva. Su objetivo es fijar las fronteras informacionales que deberán respetarse durante la implementación del prototipo experimental: configuración de corrida, fuente visual, metadatos de frame, perfil de modelo, definición de prompts, evento de percepción, cambio de estado de patrón, alerta interna, muestra de métrica y evento de error. Estos contratos constituyen una base común para implementar el prototipo de manera incremental, medirlo y reconstruir sus resultados experimentales.

En consecuencia, los nombres utilizados en esta sección, como RunConfig, FrameMetadata, PerceptionEvent o AlertEvent, deben interpretarse como denominaciones contractuales preliminares. No imponen una tecnología, un formato de serialización ni una estructura de código específica. Su utilidad reside en estabilizar la semántica de intercambio antes de que se definan detalles de implementación.

#### 17.3.11.1. Criterios de diseño de contratos

El primer criterio es la asociación obligatoria con la corrida experimental. Todo contrato relevante debe poder vincularse, directa o indirectamente, con un identificador de corrida. Esta asociación permite reconstruir qué fuente se utilizó, qué modelo estuvo activo, qué prompts y umbrales participaron, qué política de muestreo se aplicó y bajo qué configuración se generó cada evento. Sin esta relación, una detección o una alerta pierde valor experimental porque no puede explicarse ni compararse con otras ejecuciones.

El segundo criterio es el versionado explícito. Los contratos deben incluir una versión de esquema o, al menos, una convención documentada para registrar cambios durante la implementación. La razón es que el prototipo incorporará ajustes progresivos: nuevos campos de métricas, variantes de modelos, referencias opcionales a evidencia visual controlada o extensiones vinculadas con capacidades posteriores. Si esos cambios no se documentan, los reportes y repositorios históricos pueden volverse ambiguos.

El tercer criterio es la estabilidad semántica. Un campo o concepto contractual debe conservar su significado aunque cambie el componente que lo produce. Por ejemplo, una caja delimitadora normalizada no debe significar algo distinto si proviene de Grounding DINO, YOLOE u otro modelo candidato. Las diferencias internas de cada detector deben resolverse dentro del adaptador y el postproceso, no trasladarse al plano de control.

El cuarto criterio es el payload mínimo suficiente. Cada contrato debe transportar la información necesaria para su consumidor inmediato y para la reconstrucción posterior, evitando cargar datos pesados o no utilizados. Esta decisión es especialmente importante en el plano de medios, donde exponer imágenes completas, tensores o salidas crudas del modelo como contrato estable aumentaría acoplamiento y riesgo de latencia. La evidencia visual, cuando se conserve, debe referenciarse de manera controlada y no transformarse en el mecanismo ordinario de comunicación entre planos.

El quinto criterio es la extensibilidad controlada. Los contratos deben dejar margen para capacidades previstas en secciones posteriores sin convertirlas en dependencias del núcleo experimental. La incorporación futura de continuidad temporal, reglas espaciales, evidencia visual asociada o distribución externa deberá realizarse mediante extensiones explícitas, manteniendo intacta la semántica mínima de los eventos de percepción, los cambios de estado de patrón y las alertas internas.

Finalmente, los contratos deben favorecer la observabilidad desde el diseño. Cada intercambio relevante debe permitir medir tiempos, descartes, errores, cambios de estado o resultados agregables. La medición no se agrega al final del sistema; forma parte de la forma en que los componentes intercambian información y dejan evidencia reconstruible.

#### 17.3.11.2. Fronteras informacionales de intercambio

Las fronteras contractuales no se definen para enumerar cada intercambio interno del sistema, sino para establecer qué información puede atravesar los límites entre responsabilidades sin trasladar detalles de implementación. En la arquitectura propuesta, la frontera más relevante separa el plano de medios del plano de control: el primero produce evidencia perceptiva normalizada, mientras que el segundo evalúa esa evidencia en términos de persistencia temporal, estado de patrón y alerta interna.

Esta separación evita que la evaluación de patrones dependa de frames crudos, tensores, logits, estructuras internas del detector o políticas de postproceso propias de un modelo OVD específico. Del mismo modo, impide que la ruta crítica de vídeo quede acoplada a reglas de negocio, persistencia histórica, reportes o mecanismos de distribución externa. La Tabla 49 sintetiza estas fronteras desde una lectura funcional de la arquitectura, no como servicios definitivos ni como clases de implementación.

Tabla 49

Fronteras informacionales principales de la arquitectura

| Frontera informacional | Información que cruza la frontera | Contrato principal | Decisión arquitectónica protegida |

| Configuración experimental de la corrida | Parámetros que gobiernan la ejecución: escenario, fuente, modelo, prompts, umbrales, política de muestreo, módulos habilitados y política de evidencia. | RunConfig | Evita configuraciones implícitas en el código y permite reconstruir cada corrida experimental. |

| Entrada visual al plano de medios | Descripción de la fuente visual y metadatos de las unidades visuales aceptadas, omitidas o descartadas. | SourceDefinition; FrameMetadata | Permite que DBE y EBE ingresen al pipeline mediante una representación común, aunque difieran en lectura, captura o recepción. |

| Salida del plano de medios | Detecciones normalizadas asociadas a corrida, fuente, frame, modelo, prompt, coordenadas, puntajes y referencia temporal. | PerceptionEvent | Encapsula la heterogeneidad de los modelos OVD y evita exponer salidas crudas del detector al plano de control. |

| Entrada al plano de control | Evidencia perceptiva normalizada y definición del patrón que debe evaluarse. | PerceptionEvent; PatternDefinition | Permite evaluar patrones sobre eventos y reglas configuradas, no sobre frames crudos ni detalles internos de inferencia. |

| Salida del plano de control | Cambios de estado del patrón y alertas internas registradas por episodio confirmado. | PatternStateChanged; AlertEvent | Diferencia detección puntual, patrón sostenido y alerta asistiva, evitando generar alertas por cada frame. |

| Soporte experimental y reconstrucción | Métricas, errores, descartes, referencias de evidencia visual controlada y datos necesarios para reporte. | MetricSample; ErrorEvent | Separa la observabilidad y la trazabilidad experimental de la lógica funcional del flujo principal. |



Nota. La tabla presenta fronteras informacionales de la arquitectura, no una distribución física en servicios ni una especificación definitiva de clases. Los contratos asociados a seguimiento temporal, zonas, reglas espaciales o distribución externa de alertas se consideran extensiones condicionadas y deben incorporarse sin alterar la semántica mínima de los contratos base.

Esta lectura resume el flujo informacional central del prototipo experimental. La configuración define bajo qué condiciones se ejecuta la corrida; la fuente visual entrega unidades procesables al plano de medios; el plano de medios publica evidencia perceptiva normalizada; el plano de control transforma esa evidencia en estados de patrón y alertas internas; y el soporte experimental conserva métricas, errores y referencias necesarias para reconstruir los resultados. De este modo, la sección mantiene continuidad con el diseño del plano de medios, el diseño del plano de control y la integración entre condición, estrategia de detección, patrón y alerta desarrolladas en las secciones anteriores.

#### 17.3.11.3. Contratos mínimos para la ejecución experimental

A partir de las fronteras informacionales definidas, el prototipo experimental requiere un conjunto reducido de contratos mínimos que estabilicen la ejecución, la publicación de evidencia perceptiva, la evaluación de patrones, el registro de alertas internas, la medición del comportamiento y la documentación de fallas. Estos contratos no modelan la totalidad de capacidades futuras de la plataforma; delimitan la información necesaria para sostener el núcleo experimental asociado a CR-01 y CR-02.

Tabla 50

Contratos mínimos para la ejecución experimental

| Contrato preliminar | Función arquitectónica | Información mínima esperada |

| RunConfig | Define la configuración efectiva de la corrida experimental. | Identificador de corrida, escenario DBE/EBE, entorno experimental, fuente activa, perfil de modelo, conjunto de prompts, umbrales, política de muestreo, módulos habilitados y política de evidencia. |

| SourceDefinition | Describe la fuente visual antes de ingresar al plano de medios. | Identificador de fuente, tipo de fuente, referencia o ubicación, modo temporal, resolución esperada, criterio de secuenciación temporal y restricciones conocidas. |

| ModelProfile | Describe el modelo OVD o variante de inferencia utilizada. | Identificador del perfil de modelo, nombre del modelo, checkpoint o versión utilizada, entorno de ejecución, tamaño de entrada, umbrales base, adaptador asociado y notas de licencia o restricción. |

| PromptDefinition | Versiona las formulaciones de consulta vinculadas con condiciones de riesgo. | Identificador de prompt, condición asociada, texto del prompt, idioma, aliases, estrategia de detección, umbral asociado y versión del conjunto de prompts. |

| FrameMetadata | Acompaña cada unidad visual aceptada o descartada por el plano de medios. | Identificador de corrida, identificador de fuente, identificador de frame, índice o timestamp, instante de captura o recepción cuando aplique, resolución original, transformaciones aplicadas, política de muestreo y motivo de descarte si corresponde. |

| PerceptionEvent | Publica evidencia perceptiva normalizada desde el plano de medios. | Identificador de evento, versión de esquema, identificador de corrida, identificador de fuente, identificador de frame, timestamp, modelo utilizado, prompt asociado, cajas normalizadas, puntajes, etiquetas, sistema de coordenadas y referencias a evidencia visual controlada si existe. |

| PatternStateChanged | Registra una transición relevante del patrón de riesgo. | Identificador de evento, identificador de patrón, condición asociada, estado previo, estado nuevo, ventana temporal evaluada, evidencia que motivó el cambio, criterio aplicado y timestamps de inicio o cierre. |

| AlertEvent | Registra una alerta interna por episodio confirmado. | Identificador de alerta, identificador de patrón, condición asociada, severidad configurada, instante de confirmación, estado del episodio, fuente, referencias a evidencia y relación con eventos de patrón. |

| MetricSample | Registra mediciones técnicas o experimentales agregables. | Identificador de métrica, identificador de corrida, tramo o componente medido, nombre de métrica, valor, unidad, timestamp, ventana de agregación y etiquetas de contexto. |

| ErrorEvent | Documenta fallas, descartes o anomalías relevantes para la interpretación experimental. | Identificador de error, identificador de corrida, componente, categoría, severidad, mensaje resumido, referencia a fuente, frame o evento, recuperabilidad y efecto esperado sobre la corrida. |



Nota. La información mínima indicada no constituye un esquema cerrado. Cada contrato deberá refinarse durante la implementación, manteniendo asociación con corrida, versionado, trazabilidad y compatibilidad con el núcleo experimental CR-01 y CR-02. Los contratos asociados a seguimiento temporal, zonas, reglas espaciales o distribución externa no forman parte de este conjunto mínimo y deberán incorporarse como extensiones condicionadas.

El contrato PerceptionEvent ocupa una posición central porque traduce la salida heterogénea del detector en evidencia perceptiva común. Su contenido debe ser suficiente para que el plano de control evalúe patrones, pero no tan amplio como para exponer detalles internos del modelo. Por esa razón, los resultados crudos de inferencia no se consideran contrato estable: deben quedar encapsulados por el adaptador y el postproceso del plano de medios.

PatternStateChanged cumple una función distinta: no informa que el modelo observó una caja, sino que un patrón cambió de estado como resultado de una evaluación temporal. Esta diferencia evita que una detección puntual se interprete como alerta. AlertEvent, por su parte, registra el episodio asistivo cuando el patrón alcanza una condición de confirmación. Esta separación sostiene la trazabilidad desde la evidencia perceptiva hasta la alerta interna sin duplicar alertas por cada frame.

MetricSample y ErrorEvent completan la base contractual porque permiten analizar el comportamiento del sistema más allá del resultado funcional. Una corrida puede producir detecciones correctas y, al mismo tiempo, presentar latencia elevada, descartes frecuentes, errores de fuente o fallas de publicación. Registrar esas condiciones es necesario para interpretar los resultados del prototipo con rigor experimental.

#### 17.3.11.4. Criterios de evolución durante la implementación experimental

Dado que la plataforma se desarrolla como prototipo experimental, los contratos no deben rigidizar prematuramente la implementación. Su función no es congelar una API estable de producto, sino preservar la interpretación de los resultados entre corridas. Por ello, los cambios son aceptables e incluso esperables durante la implementación, siempre que queden documentados en la configuración de corrida y no alteren de manera silenciosa el significado de los eventos ya registrados.

La regla práctica es priorizar cambios aditivos cuando sea posible. Agregar un campo opcional, una etiqueta contextual o una referencia adicional resulta aceptable si los consumidores existentes pueden ignorarlo sin romper su funcionamiento. En cambio, cambiar el significado de un campo, eliminarlo o reutilizarlo para otro propósito debe considerarse una ruptura contractual y requerir una nueva versión de esquema o una aclaración explícita en el registro de corrida.

Los consumidores no deben depender de campos internos de modelos específicos. Si un detector entrega frases, logits, tokens, máscaras, embeddings o estructuras particulares, esa información puede conservarse como evidencia diagnóstica o como detalle interno, pero no debe convertirse en requisito para la evaluación de patrones del núcleo. La frontera estable debe ser la detección normalizada, con coordenadas, puntaje, etiqueta o prompt asociado y referencias temporales.

Las capacidades previstas deben incorporarse sin modificar el flujo base. Si se habilita seguimiento temporal, zonas o reglas espaciales, esas capacidades deberán enriquecer los contratos existentes o agregar estructuras complementarias sin reemplazar PerceptionEvent como evidencia perceptiva primaria ni trasladar al plano de medios la interpretación del riesgo. Si se instrumenta distribución externa de alertas, los adaptadores deberán consumir AlertEvent como salida derivada, no acceder directamente al estado interno de la evaluación de patrones.

También debe mantenerse una lectura común entre DBE y EBE. En DBE bastará, en muchos casos, con índice de frame, orden de lectura, referencia al archivo o dataset y criterio determinista de selección. En EBE podrán aparecer timestamps de captura o recepción, irregularidad temporal, unidades omitidas o descartadas y atraso acumulado. Esas diferencias deben expresarse como campos opcionales o métricas asociadas, no como contratos separados que obliguen a duplicar la lógica de procesamiento.

Por último, los contratos deben preservar la minimización visual. La referencia a clips, snapshots o recortes anotados puede incorporarse cuando la corrida lo justifique, pero el contenido visual no debe convertirse en payload ordinario de los eventos. La reconstrucción experimental debe apoyarse principalmente en identificadores, metadatos, eventos, métricas y referencias controladas.

### 17.3.12. Trazabilidad experimental y minimización de evidencia visual

La trazabilidad experimental permite reconstruir cómo una corrida produjo una alerta interna. Para ello, la arquitectura debe conservar la relación entre configuración de corrida, fuente visual, modelo utilizado, prompts activos, evidencia perceptiva, transición de estado del patrón, alerta registrada y métricas o errores asociados. Sin esa relación, una alerta pierde valor experimental porque no puede auditarse, compararse ni analizarse con suficiente rigor.

En continuidad con los contratos preliminares definidos en la sección anterior, esta sección no vuelve a especificar estructuras de intercambio, sino que precisa qué hechos deben conservarse y bajo qué política se gestiona la evidencia visual. El objetivo es sostener la interpretación de resultados sin convertir la trazabilidad en almacenamiento indiscriminado de video ni ampliar el alcance del prototipo experimental.

#### 17.3.12.1. Repositorio de eventos para reconstrucción experimental

El soporte experimental requiere un repositorio de eventos de sólo adición, orientado a conservar los hechos relevantes de la corrida sin interferir con la ruta crítica del plano de medios. Este repositorio no reemplaza al bus interno de eventos: el bus cumple una función de integración durante la ejecución, mientras que el repositorio conserva una secuencia histórica suficiente para reconstrucción posterior, auditoría técnica, reporte experimental y comparación entre variantes.

La adopción de una lógica append-only no implica implementar una plataforma empresarial de event sourcing ni un almacén analítico de gran escala. Para el prototipo experimental, alcanza con una persistencia simple y verificable, siempre que preserve orden lógico, identificadores, timestamps, versiones de esquema, relación con la configuración de corrida y payloads consistentes con los contratos definidos. La decisión arquitectónica relevante no es la tecnología concreta de almacenamiento, sino la imposibilidad de sobrescribir silenciosamente los hechos que explican una corrida.

Sobre el repositorio pueden construirse vistas derivadas para inspección, métricas o reportes. Estas vistas no sustituyen el historial persistido: funcionan como proyecciones consultables que facilitan revisar el estado de una corrida, resumir episodios, calcular indicadores o preparar evidencia para análisis académico. Si una proyección se recalcula o se descarta, la secuencia de hechos persistidos debe seguir permitiendo reconstruir la cadena causal de una alerta.

Esta separación protege la baja latencia. La publicación de evidencia perceptiva desde el plano de medios no debe quedar condicionada por operaciones pesadas de almacenamiento, generación de reportes, interfaces de inspección o notificaciones externas. Si la persistencia se retrasa, falla o se satura, esa situación debe registrarse como anomalía experimental, pero no debe convertir al repositorio en una dependencia bloqueante del procesamiento visual.

#### 17.3.12.2. Hechos persistibles mínimos

Los hechos persistibles mínimos representan aquello que debe conservarse para interpretar una corrida y reconstruir una alerta interna. No constituyen una nueva lista de contratos ni una especificación definitiva de base de datos. Mientras los contratos establecidos estabilizan el intercambio entre responsabilidades, los hechos persistibles establecen qué información debe quedar disponible para análisis posterior, comparación entre corridas y reconstrucción de evidencia. Dado que todos los elementos incluidos en la tabla forman parte del mínimo necesario, no se distingue un carácter obligatorio fila por fila.

Tabla 51Hechos persistibles mínimos para reconstrucción experimental

| Hecho persistible mínimo | Uso en reconstrucción |

| Inicio y cierre de corrida | Delimita la ejecución, el conjunto de eventos asociados, la configuración efectiva y los resultados interpretables. |

| Configuración efectiva de corrida | Permite interpretar escenario, fuente, modelo, prompts, umbrales, política de muestreo, módulos habilitados y política de evidencia. |

| Metadatos de unidades visuales procesadas | Permiten reconstruir qué frames o unidades visuales fueron aceptadas, omitidas o descartadas, bajo qué política de muestreo y con qué referencia temporal. |

| Definición de prompts cargados | Vincula las detecciones y alertas con las formulaciones consultadas, el idioma, las variantes y la estrategia de detección utilizada. |

| Definición de patrones cargados | Permite interpretar qué condición se evaluó, con qué ventana temporal, umbrales, histéresis, severidad configurada y criterio de activación. |

| Evidencia perceptiva normalizada | Relaciona frame, fuente, modelo, prompt, coordenadas, puntajes, etiquetas y referencia temporal sin exponer salidas internas del detector. |

| Cambio de estado de patrón | Explica cómo la evidencia acumulada modificó el estado del patrón bajo una ventana temporal, umbrales e histéresis configurados. |

| Alerta interna confirmada | Registra el episodio asistivo, la condición asociada, la severidad configurada, el instante de confirmación y la evidencia causal. |

| Muestras de métricas | Permiten interpretar latencias, FPS, uso de recursos, tiempos de alerta, descartes y comportamiento operativo de la corrida. |

| Errores y descartes relevantes | Explican fallas de fuente, inferencia, publicación, persistencia, pérdida de evidencia o limitaciones que afectan la validez de la corrida. |



Nota. La tabla expresa hechos mínimos necesarios para reconstrucción experimental, no servicios ni clases de implementación. Los hechos asociados a seguimiento temporal, zonas, distribución externa de alertas, adaptación de modelos o evidencia visual controlada se incorporan sólo cuando la corrida habilita esas capacidades; no forman parte del conjunto mínimo para CR-01 y CR-02.

Esta selección prioriza la reconstrucción de la cadena causal de la alerta. Una detección aislada no es suficiente para explicar un episodio; debe poder relacionarse con la configuración que la produjo, el patrón que la evaluó, la transición que confirmó la condición y las métricas o anomalías que condicionaron el resultado. Por esa razón, los errores y descartes relevantes tienen el mismo valor interpretativo que los eventos funcionales: permiten distinguir una ausencia real de evidencia de una falla técnica, un descarte por muestreo o una limitación de la fuente.

Las extensiones condicionadas deben mantener esta lógica. Si se incorpora seguimiento temporal, zonas, reglas espaciales, notificaciones externas o adaptación de modelos, esos hechos podrán persistirse como información adicional de la corrida. Sin embargo, no deben desplazar la cadena mínima de reconstrucción ni convertir capacidades exploratorias en requisitos del núcleo experimental.

#### 17.3.12.3. Política de evidencia visual mínima

La arquitectura adopta una política de minimización de evidencia visual. En el comportamiento ordinario del prototipo experimental, la trazabilidad se apoya en identificadores, metadatos, eventos, métricas, coordenadas, referencias temporales y relaciones causales entre hechos persistidos. El almacenamiento continuo de video crudo no forma parte del flujo base, porque aumenta volumen, complejidad y riesgo de privacidad sin ser necesario para reconstruir la mayoría de las decisiones experimentales.

Cuando se requiera evidencia visual para revisión técnica, validación o comunicación académica, ésta debe conservarse como artefacto controlado: snapshot, recorte anotado, clip breve, hash, referencia a archivo o vínculo asociado a una alerta o corrida específica. Su uso debe estar justificado por la finalidad experimental y no reemplaza métricas, eventos persistidos ni criterios explícitos de evaluación.

Esta decisión preserva el carácter asistivo y no identificatorio de la plataforma. El sistema no realiza reconocimiento facial, no identifica nominalmente a trabajadores, no extrae biometría y no emite decisiones normativas autónomas. La alerta interna sólo orienta la atención humana sobre una condición visualmente observable; la interpretación final y cualquier acción preventiva permanecen fuera del sistema automatizado.

### 17.3.13. Observabilidad arquitectónica e instrumentación de métricas

La observabilidad arquitectónica permite explicar el comportamiento técnico de una corrida sin interferir en la ruta crítica del procesamiento visual. Su función no es volver a definir el framework de métricas, sino asegurar que la plataforma produzca señales suficientes para calcular, interpretar o declarar no aplicables las métricas previstas.

En este sentido, la sección establece primero la materialización de métricas por tramo arquitectónico y precisa luego qué señales deben generarse durante la ejecución para que esas mediciones sean trazables, comparables y defendibles.

Cada medición debe quedar asociada a una corrida, un tramo de ejecución, una ventana temporal o evento de referencia, una unidad de medida y una condición de aplicación. De este modo, la observabilidad no se reduce a almacenar logs, sino que se convierte en un mecanismo de interpretación experimental del sistema.

#### 17.3.13.1. Materialización arquitectónica de las métricas

El framework de métricas definido en la consolidación metodológica se materializa en la arquitectura mediante puntos de instrumentación distribuidos a lo largo del flujo completo del sistema. Para preservar la validez experimental, las métricas no se incorporan como una actividad posterior a la ejecución, sino como parte del diseño observable del prototipo: cada medición debe asociarse a un tramo del pipeline, a un evento registrado, a una configuración de corrida y a un criterio explícito de inicio, cierre o no aplicación.

La instrumentación debe cubrir el recorrido que va desde la disponibilidad de la fuente de video hasta la generación de evidencia perceptiva, la evaluación del patrón, el registro interno de la alerta y, cuando corresponda, su distribución posterior hacia consumidores o adaptadores externos. Todas las métricas deben quedar asociadas a la configuración de corrida correspondiente, incluyendo escenario, fuente, modelo, prompts, umbrales, entorno, hardware, política de muestreo y módulos habilitados.

La Tabla 52 sintetiza esta materialización desde una perspectiva de tramos arquitectónicos. El objetivo no es reemplazar el framework metodológico ni detallar una especificación exhaustiva de logging, sino mostrar en qué puntos del diseño se observan, registran o cierran las métricas principales de la plataforma.

Tabla 52

Materialización arquitectónica del framework de métricas

| Tramo arquitectónico | Punto de medición arquitectónico | Métricas o evidencias materializadas |

| Plano de medios | Registro de lectura o recepción del frame, ingesta, muestreo, normalización, inferencia OVD, postproceso y emisión de detecciones normalizadas. | FPS, throughput, descartes, latencias por tramo, latencia de inferencia, métricas de detección OVD, base temporal para TTFD y reconstrucción de secuencia. |

| Publicación de evidencia perceptiva | Publicación en el bus interno de eventos de detecciones normalizadas asociadas a corrida, condición y referencia temporal. | TTFD y trazabilidad de evidencia perceptiva. |

| Plano de control | Evaluación de patrones, transición de estados, confirmación de episodios y registro de alertas internas. | SDR, estados de patrón, estabilidad temporal,  y trazabilidad de confirmación. |

| Distribución de alertas confirmadas | Publicación, despacho o entrega hacia consumidores externos, sólo cuando la corrida lo instrumente. | y comportamiento de salidas externas, medidos por separado de la alerta interna. |

| Soporte experimental | Consolidación transversal de telemetría, errores, descartes, evidencia asociada, condiciones no aplicables y reporte. | Uso de recursos, robustez experimental, diagnóstico de cuellos de botella y resultado reconstruible por corrida. |



Nota. Todas las métricas deben quedar asociadas a la configuración de corrida correspondiente, incluyendo escenario, fuente, modelo, prompts, umbrales, entorno, hardware, política de muestreo y módulos habilitados. Las métricas condicionadas sólo se aplican cuando la configuración de corrida habilita los módulos, datos y ground truth requeridos. La alerta válida para la métrica principal corresponde al registro interno de la alerta confirmada; la distribución posterior hacia consumidores externos se mide, si corresponde, como trayecto separado. Las métricas asociadas a tracking o persistencia de identidad quedan condicionadas a la habilitación de dicha extensión y a la disponibilidad de anotaciones temporales suficientes.

En esta organización, TTFD, SDR y  quedan asociados a hitos distintos del flujo: primera evidencia perceptiva publicada, persistencia durante la evaluación del patrón y alerta interna registrada. La distribución externa sólo se considera  cuando la corrida instrumenta consumidores o adaptadores externos, y se mide como trayecto posterior.

#### 17.3.13.2. Señales observables del sistema

Las señales observables son los rastros técnicos que la arquitectura debe producir para que las métricas puedan calcularse con sentido. No equivalen todavía a resultados agregados: son timestamps, contadores, eventos, cambios de estado, muestras de recursos y anomalías que permiten explicar qué ocurrió durante una corrida.

Estas señales deben originarse en los puntos donde el sistema ya produce información relevante: plano de medios, frontera de publicación de evidencia perceptiva, plano de control y soporte experimental. La Tabla 53 resume las señales mínimas que conviene instrumentar para sostener la evaluación del prototipo sin repetir el catálogo metodológico de métricas.

Tabla 53

Señales observables e instrumentación mínima

| Señal observable | Origen arquitectónico | Uso experimental |

| Timestamps por tramo | Lectura o captura, normalización, inferencia, postproceso y publicación de evidencia perceptiva. | Permiten calcular latencias por tramo, FPS efectivo, atraso acumulado y tiempo hasta hitos relevantes. |

| Unidades visuales aceptadas, omitidas o descartadas | Control de ritmo, muestreo y gestión de cola del plano de medios. | Permiten interpretar cobertura temporal, pérdida de evidencia, política de descarte y diferencias entre DBE y EBE. |

| Estado de control de ritmo y disponibilidad temporal | Captura, decodificación, control de ritmo y publicación de eventos. | Permite interpretar atraso acumulado, saturación, reemplazo de frames, pérdida de continuidad temporal y diferencias de comportamiento entre DBE y EBE. |

| Descartes de postproceso perceptivo | Postproceso del plano de medios. | Permiten interpretar el efecto de umbrales, filtrado, NMS o normalización sobre la evidencia finalmente publicada. |

| Eventos de percepción publicados | Frontera de salida del plano de medios hacia el bus interno de eventos. | Permiten relacionar detecciones con fuente, modelo, prompt, frame y referencia temporal, y sostener métricas de primera evidencia. |

| Transiciones de estado de patrón | Evaluación de patrones en el plano de control. | Permiten interpretar persistencia, confirmación, sostenimiento, resolución y latencia de alerta interna. |

| Alertas internas por episodio | Registro de alerta interna del plano de control. | Permiten delimitar episodios asistivos, evitar duplicación por frame y asociar evidencia causal con métricas operativas. |

| Muestras de recursos de ejecución | Entorno de ejecución y soporte experimental. | Permiten analizar uso de CPU, GPU, memoria, VRAM y posibles cuellos de botella durante la corrida. |

| Errores y anomalías instrumentadas | Instrumentación transversal del sistema. | Permiten explicar fallas de fuente, inferencia, publicación, persistencia, medición o corridas degradadas. |



Nota. La tabla presenta señales observables, no métricas finales. Una misma señal puede alimentar varias métricas, y una métrica puede requerir combinar señales de distintos tramos de la arquitectura.

#### 17.3.13.3. Aplicabilidad y no aplicabilidad de métricas

La arquitectura debe permitir distinguir entre una métrica calculada, una métrica aplicable pero no calculada y una métrica no aplicable. Esta distinción evita interpretar la ausencia de un valor como resultado nulo, falla del sistema o evidencia de desempeño. En un prototipo experimental, declarar correctamente la no aplicabilidad es tan importante como registrar una métrica calculada.

La aplicabilidad depende de la configuración de corrida, los datos disponibles, los módulos habilitados y la instrumentación efectivamente activa. Una métrica de detección, por ejemplo, requiere ground truth suficiente y un punto operativo declarado; una métrica de tracking requiere seguimiento habilitado y, si se evalúa identidad, anotaciones temporales; una métrica de notificación externa sólo corresponde si la corrida instrumenta un canal de salida posterior a la alerta interna. Del mismo modo, métricas temporales como TTFD, SDR o latencia de alerta interna necesitan eventos de inicio, transición o confirmación claramente identificables.

Cuando existen datos, eventos e instrumentación suficientes, la métrica debe registrarse con valor, unidad, tramo, ventana temporal y contexto de corrida. Si la métrica corresponde al alcance de la corrida pero no puede calcularse por falla de instrumentación o ausencia de un dato operativo, debe quedar registrada como aplicable no calculada, indicando la causa y excluyéndola de comparaciones cuantitativas directas. En cambio, si la métrica no corresponde por falta de ground truth, anotación temporal, módulo habilitado o criterio de evaluación, debe declararse como no aplicable y justificarse como límite metodológico o arquitectónico, no como falla del sistema.

También pueden existir métricas no interpretables por degradación de la corrida. Esto ocurre cuando errores de fuente, descartes excesivos, saturación de colas, fallas de publicación o problemas de persistencia alteran la validez de la medición. En esos casos, la arquitectura debe conservar las anomalías asociadas y marcar la métrica como limitada o no interpretable. Esta política permite distinguir ausencia de medición, límite metodológico, fallo instrumental y resultado válido, preservando la comparabilidad entre corridas.

#### 17.3.13.4. Registro de resultados por corrida

El registro de resultados por corrida funciona como una proyección interpretable de los hechos persistidos y de las señales observables. No reemplaza al repositorio de eventos ni a los contratos mínimos: resume la ejecución para análisis comparativo, revisión técnica y comunicación académica.

Cada corrida debe consolidar, como mínimo, la identificación y objetivo de la ejecución, la configuración resumida, las métricas calculadas con sus unidades y ventanas, las métricas no aplicadas o no calculadas con su causa, y las anomalías que condicionen la interpretación. Esta salida permite comparar variantes sin depender de la inspección manual de eventos crudos.

El registro de resultados también debe preservar la separación entre métricas internas del sistema y salidas externas derivadas. La alerta válida para el prototipo experimental es la alerta interna registrada por episodio; cualquier medición asociada a notificaciones o adaptadores externos debe declararse como trayecto posterior e independiente. De este modo, la observabilidad sostiene la evaluación del prototipo sin ampliar su alcance ni introducir dependencias sobre consumidores externos.

### 17.3.14. Escenarios experimentales DBE y EBE

La arquitectura propuesta contempla dos escenarios experimentales principales: Dataset-Based Evaluation (DBE) y Environment-Based Evaluation (EBE). Estos escenarios no representan arquitecturas distintas ni topologías físicas de despliegue; describen la naturaleza de la fuente visual y el tipo de evaluación experimental. Ambos conservan la separación entre plano de medios, plano de control y soporte experimental; lo que cambia es la forma en que ingresa la fuente visual, el grado de control temporal y las señales adicionales necesarias para interpretar la corrida.

DBE se orienta a estabilizar el núcleo experimental bajo condiciones reproducibles. EBE, en cambio, incorpora una fuente viva o continua para observar el comportamiento integrado del sistema frente a variabilidad temporal, decodificación, irregularidades de captura o disponibilidad de frames recientes. Esta diferencia no debe alterar la semántica de los contratos ni la lógica de evaluación de patrones; debe expresarse mediante metadatos, configuración de corrida e instrumentación observable.

Por esta razón, DBE debe implementarse antes que EBE. La prioridad de DBE no reduce el valor de EBE, sino que protege la validez experimental: antes de atribuir un problema a captura, iluminación, compresión, temporización o control de ritmo, conviene estabilizar inferencia, postproceso, publicación de eventos, evaluación de patrones, alertas internas, métricas y reporte sobre fuentes controladas.

#### 17.3.14.1. DBE como escenario de estabilización reproducible

El escenario DBE utiliza imágenes, datasets o videos locales como fuente de entrada. Su función principal es estabilizar el flujo arquitectónico bajo condiciones repetibles, reduciendo la variabilidad externa que podría ocultar problemas propios del modelo, del postproceso, de los contratos o de la evaluación de patrones.

En este escenario, la fuente visual debe ingresar al plano de medios mediante el adaptador de ingesta visual utilizado por el resto del sistema. La lectura puede conservar índice de imagen, índice de frame, referencia al archivo, orden lógico y metadatos de resolución. Si se aplica una política de muestreo, salto de frames o reducción de resolución, esa decisión debe declararse en la configuración de corrida para que los resultados sean comparables.

DBE resulta especialmente adecuada para comparar modelos OVD, formulaciones de prompts, umbrales, estrategias de postproceso, reglas temporales y criterios de alerta interna. También permite repetir corridas equivalentes para analizar sensibilidad a la formulación del prompt, variación de umbrales o cambios de configuración. Su límite es que no representa por sí sola las condiciones de captura continua; por ello, no debe utilizarse para concluir sobre problemas de streaming, jitter, buffers o operación con cámara.

#### 17.3.14.2. EBE como escenario de fuente viva controlada

El escenario EBE incorpora una fuente viva o continua desde cámara, stream o captura controlada. Su finalidad es observar la integración de la arquitectura bajo condiciones más próximas a una operación sostenida, sin convertir esa observación en reemplazo de la evaluación reproducible de DBE.

En EBE aparecen elementos que no son centrales en DBE: timestamps de captura o recepción, decodificación, variabilidad de framerate, irregularidad temporal, atraso acumulado, reemplazo de unidades visuales antiguas por unidades recientes y descartes por control de latencia. Estos elementos no deben modificar la salida conceptual del plano de medios, pero sí deben quedar instrumentados para interpretar el comportamiento de la corrida.

La incorporación de una fuente continua aumenta la ambigüedad diagnóstica. Una disminución de desempeño puede originarse en iluminación, compresión, movimiento, pérdida de frames, saturación de colas, atraso de decodificación, costo de inferencia, sensibilidad del prompt o reglas de patrón. Por ello, EBE debe evaluarse como escenario complementario de plausibilidad operativa y no como sustituto del escenario controlado de comparación.

#### 17.3.14.3. Equivalencia arquitectónica entre escenarios

DBE y EBE deben converger en la misma arquitectura una vez normalizada la entrada visual. La diferencia entre escenarios se ubica antes y alrededor de la disponibilidad del frame: origen de la fuente, referencia temporal, política de muestreo, control de ritmo e instrumentación de omisiones o descartes. Después de esa frontera, la inferencia OVD, el postproceso, la publicación de evidencia perceptiva, la evaluación de patrones y el registro de alertas internas deben mantener la misma semántica.

Esta equivalencia evita construir dos flujos incompatibles. Si DBE y EBE produjeran contratos distintos o exigieran reglas de patrón diferentes, los resultados dejarían de ser comparables. En cambio, al conservar la misma estructura de eventos, métricas y hechos persistibles, la arquitectura permite analizar qué parte de la variación proviene de la fuente continua y qué parte corresponde al comportamiento del detector o de la evaluación de patrones.

La comparación entre escenarios debe declarar explícitamente qué variables cambiaron. Una corrida DBE y una corrida EBE pueden compartir modelo, prompts, umbrales y reglas de patrón, pero diferir en fuente, temporización, iluminación, compresión o criterio de descarte. Esas diferencias deben registrarse como parte de la configuración y de la observabilidad, no tratarse como detalles secundarios.

#### 17.3.14.4. Comparación arquitectónica entre DBE y EBE

La Tabla 54 resume las diferencias principales entre ambos escenarios desde una lectura arquitectónica. Su finalidad no es repetir la definición metodológica de DBE y EBE, sino mostrar qué decisiones de diseño se derivan de cada modo de evaluación y cómo deben interpretarse sus resultados.

Tabla 54

Comparación arquitectónica entre escenarios DBE y EBE

| Dimensión | DBE | EBE | Implicancia arquitectónica |

| Fuente de entrada | Dataset, imágenes o video local. | Cámara, stream o captura controlada. | La fuente debe abstraerse para que ambas topologías ingresen al plano de medios mediante metadatos comunes. |

| Control temporal | Alto; la secuencia puede repetirse bajo condiciones equivalentes. | Menor; intervienen captura, buffers, jitter, decodificación y disponibilidad del último frame. | EBE requiere instrumentar timestamps, colas, descartes y atraso acumulado. |

| Objetivo experimental | Estabilizar inferencia, contratos, eventos, métricas, patrones y alertas internas. | Observar comportamiento integrado con fuente continua. | DBE debe preceder a EBE para aislar fallas del modelo y de la arquitectura base. |

| Variabilidad externa | Baja o controlada, según cobertura del dataset. | Media o alta, según cámara, red local, códec, iluminación, movimiento, buffers y entorno. | Las diferencias de desempeño no deben atribuirse automáticamente al modelo OVD. |

| Instrumentación adicional | Orden lógico, referencia a dataset o archivo, política de muestreo y frames procesados. | Captura o recepción, profundidad de cola, descartes, jitter, reemplazo de frames y estado de fuente. | La observabilidad debe registrar diferencias temporales para interpretar latencia y cobertura. |

| Métricas prioritarias | Detección, latencias por etapa, FPS efectivo, estados de patrón y alertas internas. | Latencia de ingesta, estabilidad temporal, descartes, FPS efectivo, alertas internas y errores de fuente. | Las métricas pueden compartir contratos, pero se interpretan con condiciones de aplicación diferentes. |

| Riesgo principal | Sesgo, cobertura limitada o falta de representatividad del dataset. | Confundir fallas de captura, streaming o condiciones ambientales con fallas de inferencia o patrones. | El reporte debe registrar contexto de fuente, anomalías y variables cambiadas entre corridas. |

| Condición de comparabilidad | Misma configuración lógica y fuente reproducible; ground truth cuando corresponda. | Misma configuración lógica, con variabilidad temporal y condiciones de captura documentadas. | La comparación DBE/EBE requiere declarar qué variables permanecen constantes y cuáles cambian. |



Nota. DBE y EBE se interpretan como escenarios experimentales de una misma arquitectura. La diferencia principal se ubica en la fuente visual, la temporalidad y la instrumentación requerida; los contratos de evidencia, patrón, alerta, métricas y errores deben mantenerse compatibles para preservar comparabilidad experimental.

Con esta organización, DBE funciona como escenario de estabilización y comparación controlada, mientras que EBE permite observar la integración con fuente viva bajo condiciones instrumentadas. La arquitectura no debe privilegiar un escenario mediante contratos diferentes, sino conservar una frontera común de entrada visual normalizada y registrar explícitamente las condiciones que afectan la interpretación de cada corrida.

#### 17.3.14.5. Alcance arquitectónico de EBE

EBE se incorpora como escenario experimental basado en una fuente visual viva o continua. Su finalidad es observar el comportamiento de la arquitectura cuando la entrada visual no proviene de una secuencia completamente regulable, sino de una escena que evoluciona independientemente del ritmo de procesamiento del sistema.

Desde el punto de vista arquitectónico, EBE no modifica la organización lógica de la plataforma. Las fuentes vivas deben ingresar al plano de medios mediante el adaptador de ingesta visual, conservar metadatos temporales suficientes, registrar omisiones o descartes relevantes y producir eventos de percepción normalizados compatibles con los generados en DBE. De este modo, la diferencia entre escenarios queda representada en la fuente, la temporalidad y la observabilidad, no en contratos incompatibles ni en reglas de evaluación distintas.

La incorporación de fuentes vivas introduce condiciones que no aparecen con la misma intensidad en DBE: variabilidad de captura, disponibilidad efectiva de unidades visuales, continuidad temporal, atraso acumulado, omisiones, descartes y posibles pérdidas de evidencia. Estas condiciones no deben atribuirse automáticamente al modelo OVD ni al motor de patrones; deben registrarse como parte de la corrida para interpretar correctamente latencia, cobertura temporal y comportamiento de las alertas internas.

La configuración de corrida debe declarar el modo conceptual de entrada utilizado en EBE, como cámara, stream, captura controlada o mecanismo equivalente; la temporalidad esperada de la fuente; el criterio de selección u omisión de unidades visuales; y las señales observables necesarias para analizar continuidad, latencia y pérdida de evidencia. Los aspectos físicos o tecnológicos concretos de transmisión, distribución de componentes, protocolos, buffers o payloads no forman parte de esta delimitación arquitectónica.

Tabla 55

Condiciones observables de fuente viva para EBE

| Condición observable | Registro mínimo esperado | Impacto sobre la interpretación |

| Modo de fuente continua | Cámara directa, stream local, EN de captura o mecanismo equivalente declarado en la configuración de corrida. | Permite distinguir captura local, transmisión y participación de un nodo externo. |

| Medio de conectividad | LAN cableada o inalámbrica controlada, según disponibilidad de la corrida. | Afecta estabilidad, jitter, pérdida potencial de frames y continuidad temporal. |

| Protocolo o mecanismo de transporte | RTSP, WebRTC, HTTP, archivo simulado como stream u otro mecanismo declarado. | Condiciona latencia, buffering y comportamiento de recepción. |

| Timestamps de captura o recepción | Marca temporal disponible por frame o unidad visual recibida. | Permite estimar el atraso acumulado, ordenar eventos visuales y diferenciar captura de recepción. |

| Colas y buffers | Tamaño configurado, profundidad observada, descartes y reemplazos de frame. | Permite interpretar backpressure, pérdida de continuidad y latencia efectiva. |

| Descartes o pérdidas | Cantidad y causa de frames omitidos, descartados, reemplazados o no recibidos. | Evita confundir ausencia de detección con ausencia real de evidencia visual. |

| Condición de degradación | Cortes de fuente, saturación, jitter elevado, recepción irregular o pérdida sostenida de continuidad. | Permite marcar métricas como limitadas o no interpretables cuando la corrida resulte degradada. |



Nota. La tabla presenta condiciones observables para interpretar corridas EBE con fuente viva. No constituye un diseño de infraestructura, una topología física ni una especificación cerrada de protocolos; los valores concretos se declaran durante la implementación del prototipo.

Bajo esta delimitación, EBE no se interpreta como infraestructura definitiva de despliegue, sino como escenario experimental para incorporar una fuente viva de manera medible. Su función es ampliar la evaluación después de DBE manteniendo contratos, métricas y trazabilidad comunes.

### 17.3.15. Roles funcionales previstos: CPN, EN y TN

La arquitectura distingue tres roles funcionales previstos: Central Processing Node (CPN), Edge Node (EN) y Training Node (TN). En esta etapa, estos nombres no implican necesariamente máquinas físicas separadas ni una topología definitiva de despliegue; funcionan como roles lógicos para ordenar responsabilidades y evitar conclusiones no respaldadas por la configuración evaluada.

La sección complementa los escenarios DBE y EBE desarrollados previamente. DBE puede operar dentro del rol de procesamiento de referencia utilizando fuentes locales; EBE puede incorporar el rol EN como origen de captura o preparación liviana de una fuente viva; y el rol TN queda reservado para preparación de datos o adaptación condicionada.La definición de estos roles no implica una asignación física obligatoria; su finalidad es ordenar responsabilidades arquitectónicas, delimitar la interpretación de corridas y evitar que captura, procesamiento y adaptación de modelos se confundan como una única responsabilidad.

La decisión central es preservar al CPN como rol de referencia operativa del prototipo experimental. El EN puede aportar fuente continua o reducción conservadora de carga, y el TN puede generar variantes de modelo; sin embargo, ninguna de esas funciones sustituye la medición integrada del flujo donde se ejecutan inferencia, plano de control, persistencia experimental, métricas y reportes.

La Figura x sintetiza la relación lógica entre los roles EN, CPN y TN. El EN se vincula operativamente con el CPN mediante el aporte de stream, frames o metadatos de captura, mientras que el TN intercambia de manera condicionada datos, resultados y checkpoints candidatos con el rol de referencia. El resultado experimental —corridas, alertas internas y reportes— se consolida en el flujo de referencia, que funciona como punto de integración y evaluación.

Figura x

Roles funcionales CPN, EN y TN

Nota. El esquema presenta roles funcionales de la plataforma experimental, no máquinas físicas ni una topología definitiva de despliegue. No representa DBE y EBE como nodos, ya que corresponden a escenarios experimentales. Toda variante generada fuera del flujo de referencia debe volver a evaluarse bajo una corrida registrada para sostener comparabilidad.

#### 17.3.15.1. CPN como rol de referencia operativa

El CPN representa el rol de referencia del prototipo experimental. En él se ubican conceptualmente la inferencia OVD, el postproceso de detecciones, la publicación de evidencia perceptiva, la evaluación de patrones, el registro de alertas internas, la persistencia experimental, la observabilidad y la generación de reportes. Esta concentración no busca diseñar una arquitectura monolítica de producto ni fijar una máquina física, sino establecer un flujo medible para evaluar la plataforma de extremo a extremo.

Toda afirmación sobre viabilidad operativa debe apoyarse principalmente en el comportamiento observado en el flujo de referencia. Si un modelo alcanza buen rendimiento durante entrenamiento o preparación, pero no puede ejecutarse con latencia aceptable en la corrida integrada, ese resultado no demuestra viabilidad para el prototipo experimental. Del mismo modo, si una fuente se captura correctamente mediante el rol EN, ello no implica que la inferencia OVD pueda desplazarse a ese rol sin una evaluación específica.

El rol CPN funciona además como punto de comparación entre variantes. Cambios de modelo, prompts, umbrales, resolución, política de muestreo, postproceso o reglas de patrón deben registrarse por corrida y evaluarse sobre el flujo de referencia para mantener comparabilidad. De este modo, cualquier diferencia observada puede relacionarse con la variante evaluada y no con cambios no declarados en el entorno de ejecución.

#### 17.3.15.2. EN como rol de captura y preprocesamiento condicionado

El rol EN se incorpora principalmente en EBE como rol de captura, ingesta o preparación liviana de la fuente visual. Su función base consiste en entregar video, frames o stream hacia el flujo de referencia, conservando referencias temporales y condiciones de origen suficientes para interpretar la corrida. En este modo, el EN no decide condiciones de riesgo, no confirma patrones y no genera alertas internas.

De la misma manera, puede operar en distintos modos de intervención sobre la fuente. El modo base es la captura sin análisis local, donde el rol entrega la señal visual con la menor transformación posible. También puede incorporar preprocesamiento no semántico, como agregado de timestamps, healthcheck de fuente, resize, estabilización mínima o adecuación de codificación/transporte. Estas operaciones son admisibles si quedan registradas cuando alteran resolución, framerate, calidad visual o disponibilidad temporal.

Como variante condicionada, puede considerarse una preselección liviana y conservadora cuando exista una justificación experimental clara. Por ejemplo, un criterio de movimiento o un detector cerrado liviano podrían utilizarse para priorizar segmentos candidatos antes de la inferencia OVD. Esta variante introduce riesgo de falsos negativos antes de la inferencia principal; por ello, debe declararse en la configuración de corrida, instrumentar descartes y compararse, cuando corresponda, contra un flujo sin preselector.

En el alcance conceptual de esta etapa, el rol EN no ejecuta inferencia open-vocabulary como parte del núcleo. Aunque la inferencia OVD fuera del flujo de referencia puede considerarse una posibilidad arquitectónica en sistemas con hardware específico, su incorporación introduciría restricciones adicionales de latencia, consumo, compatibilidad contractual y validación comparativa. Por ello, la detección OVD permanece asociada al flujo de referencia del prototipo experimental.

Tabla 56

Modos arquitectónicos previstos para el EN

| Modo | Descripción | Tratamiento en el prototipo experimental |

| EN-0: captura sin análisis local | El EN entrega video, frames o stream sin análisis visual ni filtrado semántico. | Modo base recomendado para EBE, porque minimiza ambigüedad sobre pérdida de evidencia. |

| EN-1: preprocesamiento no semántico | El EN agrega timestamps, healthcheck, resize, estabilización mínima o adecuación de codificación/transporte. | Permitido si se registra cualquier cambio que afecte resolución, framerate, calidad visual o referencia temporal. |

| EN-2: preselección liviana conservadora | El EN utiliza criterios simples, movimiento o un modelo cerrado liviano para priorizar segmentos candidatos. | Condicionado; debe ser conservador, registrar descartes y considerar falsos negativos potenciales antes de la inferencia OVD. |



Nota. Los modos del EN deben declararse por corrida. La inferencia OVD fuera del flujo de referencia no se incorpora como modo previsto para este prototipo experimental. La preselección liviana no reemplaza la evaluación de referencia y no debe incorporarse si compromete la trazabilidad o descarta evidencia crítica sin registro.

#### 17.3.15.3. TN como soporte de adaptación condicionada

El rol TN cumple un rol separado de la operación del prototipo experimental. Se reserva para preparación de datos, entrenamiento, fine-tuning o generación de checkpoints candidatos cuando la estrategia de adaptación al dominio esté justificada por datos suficientes, particiones válidas y comparación contra una baseline preentrenada.

El hecho de que un modelo pueda entrenarse o ajustarse en el TN no constituye evidencia de que pueda inferir en tiempo compatible con el prototipo experimental. Todo checkpoint producido o ajustado en ese rol debe volver a evaluarse en una corrida integrada registrada, para que sus resultados sean comparables con las variantes preentrenadas. Esta separación evita confundir capacidad de entrenamiento con viabilidad de inferencia.

El TN tampoco debe incorporarse como dependencia del núcleo CR-01 y CR-02. La arquitectura debe poder cerrar el flujo base con modelos preentrenados, prompts versionados, detecciones normalizadas, evaluación de patrones y alertas internas antes de habilitar ramas de adaptación al dominio. De este modo, la adaptación permanece como posibilidad comparativa y no como condición de funcionamiento.

La interpretación de resultados debe asociarse siempre con el rol efectivamente utilizado y con la configuración de corrida. Una medición obtenida durante preparación o entrenamiento no demuestra viabilidad operativa; una captura exitosa desde el rol EN no demuestra inferencia en borde; y una corrida integrada en el flujo de referencia constituye la base principal para evaluar latencia, patrones, alertas y reporte del prototipo experimental.

Con esta delimitación, la lectura por roles funcionales preserva una interpretación experimental controlada: el CPN representa la evaluación defendible del prototipo, el EN aporta fuente continua o preprocesamiento condicionado, y el TN queda reservado para adaptación de modelos sin sustituir la validación operativa. La distribución física concreta de estos roles queda diferida a la implementación, permitiendo incorporar complejidad de manera progresiva sin alterar el núcleo arquitectónico ni sobredimensionar el alcance del prototipo experimental.

### 17.3.16. Riesgos arquitectónicos y mitigaciones de diseño

El diseño arquitectónico del prototipo experimental no elimina todos los riesgos técnicos, pero debe hacerlos explícitos y vincularlos con decisiones de mitigación. Esta sección no constituye una matriz general de gestión del proyecto; sintetiza los riesgos que pueden afectar la validez experimental, la trazabilidad de las corridas y la interpretación de las alertas internas. La Tabla 57 resume esos riesgos y las decisiones de diseño que los contienen dentro del alcance definido.

Dentro de estos riesgos se incluye también la confusión entre escenario experimental y despliegue físico. Para mitigarla, DBE y EBE se tratan como escenarios de evaluación, mientras que la cantidad de hosts, la distribución real de componentes y los mecanismos concretos de comunicación no forman parte del compromiso arquitectónico de este capítulo. Del mismo modo, se evita sobredetallar en esta etapa decisiones propias de Etapa 4, como protocolos, payloads, colas o parámetros operativos.

Tabla 57

Riesgos arquitectónicos y mitigaciones de diseño

| Riesgo arquitectónico | Mitigación de diseño |

| Latencia excesiva en la ruta crítica: reduce FPS efectivo y aumenta el tiempo hasta la alerta interna. | Separar plano de medios y plano de control; medir timestamps; parametrizar muestreo, colas y descartes; estabilizar primero en DBE. |

| Acoplamiento entre inferencia OVD y lógica de negocio: reduce sustituibilidad y filtra detalles internos del detector. | Encapsular modelos mediante adaptadores; publicar evidencia perceptiva normalizada; evitar dependencia de frames crudos, tensores o logits. |

| Degradación temporal en EBE: introduce jitter, atraso acumulado, backpressure o pérdida de continuidad visual. | Instrumentar unidades visuales aceptadas, omitidas y descartadas; registrar estado de colas, buffers, referencias temporales y anomalías. |

| Pérdida de evidencia por preselección en EN: puede descartar una condición real antes de la inferencia OVD. | Mantener EN-2 como variante condicionada; exigir criterios conservadores, registro de descartes y comparación contra flujo sin preselector. |

| Trazabilidad insuficiente: impide reconstruir por qué se generó una alerta y qué evidencia la sostuvo. | Persistir configuración efectiva, prompts, patrones, evidencia perceptiva, transiciones de estado, alertas internas, métricas, errores y descartes. |

| Interpretación incorrecta de métricas: confunde ausencia de valor con cero, éxito o falla del sistema. | Registrar métricas calculadas, aplicables no calculadas, no aplicables y no interpretables por corrida degradada, junto con su causa. |

| Sobredimensionamiento del alcance experimental: convierte extensiones condicionadas en dependencias del núcleo. | Mantener CR-01 y CR-02 como núcleo; declarar por corrida tracking, zonas, notificaciones, adaptación o preselección; validar checkpoints en CPN. |

| Exposición visual innecesaria: aumenta almacenamiento, complejidad operativa y riesgo de privacidad. | Aplicar minimización de evidencia visual; usar eventos y metadatos como trazabilidad ordinaria; conservar capturas o clips sólo como artefactos controlados. |



Nota. La tabla sintetiza riesgos derivados del diseño arquitectónico, no riesgos generales de planificación. Las mitigaciones se formulan como decisiones de arquitectura, criterios de instrumentación o límites de alcance del prototipo experimental.

En conjunto, estos riesgos confirman que la arquitectura debe proteger la ruta crítica, desacoplar percepción y control, conservar evidencia reconstruible, evitar almacenamiento visual innecesario, diferenciar escenarios de despliegue físico y sostener un alcance experimental defendible. Los riesgos no desaparecen, pero quedan delimitados y observables para la implementación y la validación posteriores.

### 17.3.17. Backlog de implementación y criterios de avance

El backlog de implementación traduce el diseño arquitectónico en una secuencia concreta de trabajo para construir el prototipo experimental. Su finalidad no es describir funcionalidades de un producto final, sino ordenar los incrementos necesarios para alcanzar una corrida experimental validable, trazable y comparable.

El primer objetivo de implementación es cerrar el núcleo validable sobre DBE para CR-01 y CR-02. Ese núcleo debe permitir configurar una corrida, procesar una fuente visual controlada, ejecutar inferencia OVD, normalizar detecciones, registrar eventos, evaluar patrones, generar alertas internas y producir un reporte experimental. Las extensiones asociadas a EBE, rol EN, adaptación de modelos, inspección avanzada, MOT o zonas sólo deben incorporarse después de estabilizar ese flujo base.

La priorización del backlog se organiza en tres niveles. El nivel de núcleo validable reúne las capacidades sin las cuales no puede obtenerse evidencia experimental defendible. El nivel de extensión condicionada incorpora capacidades que agregan realismo, comparación o inspección, pero que no deben bloquear el flujo base. Finalmente, el nivel exploratorio agrupa capacidades de mayor complejidad que sólo tienen sentido si existen datos, instrumentación y beneficio analítico suficiente.

Tabla 58Backlog de implementación del núcleo validable

| Orden | Ítem de backlog | Prioridad | Entregable esperado | Criterio de aceptación |

| 1 | Configuración de corrida experimental | Núcleo validable | Mecanismo para registrar identificador de corrida, escenario, fuente visual, modelo, prompts, umbrales, módulos habilitados y política de evidencia. | Una corrida puede repetirse e interpretarse a partir de su configuración efectiva registrada. |

| 2 | Lectura de fuentes DBE | Núcleo validable | Lectura de imágenes, videos o datasets locales con orden temporal controlado. | El sistema procesa una fuente DBE y conserva metadatos de fuente, unidad visual, timestamps y política de muestreo. |

| 3 | Registro de prompts para CR-01 y CR-02 | Núcleo validable | Conjunto inicial de prompts versionados para condiciones de EPP, incluyendo idioma, variante y estrategia de detección. | Cada detección puede vincularse con el prompt y la configuración que la originaron. |

| 4 | Integración del modelo OVD baseline | Núcleo validable | Adaptador para ejecutar un modelo OVD preentrenado bajo un perfil sustituible. | El modelo ejecuta inferencia sobre CR-01 y CR-02 sin exponer salidas internas al plano de control. |

| 5 | Postproceso y normalización de detecciones | Núcleo validable | Conversión de salidas del modelo en evidencia perceptiva normalizada. | Las detecciones quedan expresadas con fuente, unidad visual, modelo, prompt, coordenadas, etiqueta, puntaje y referencia temporal. |

| 6 | Instrumentación del plano de medios | Núcleo validable | Registro de FPS, latencia por tramo, descartes, errores, anomalías y uso básico de recursos. | La corrida permite interpretar rendimiento, pérdidas de evidencia y comportamiento temporal del pipeline. |

| 7 | Publicación y persistencia experimental de eventos | Núcleo validable | Publicación de eventos internos y conservación append-only de la evidencia mínima. | La evidencia perceptiva puede reconstruirse sin depender de frames crudos ni de estructuras internas del detector. |

| 8 | Evaluación de patrones CR-01 y CR-02 | Núcleo validable | Lógica de evaluación temporal con ventana, umbrales, persistencia e histéresis. | El sistema distingue detecciones puntuales, patrones candidatos, patrones confirmados y resolución de patrón. |

| 9 | Registro de alertas internas | Núcleo validable | Registro de alertas asistivas por episodio, vinculadas con condición, patrón, severidad y evidencia causal. | Una alerta interna no se duplica por frame y puede reconstruirse desde la evidencia que la originó. |

| 10 | Instrumentación del plano de control | Núcleo validable | Registro de evaluaciones de patrón, transiciones de estado, conteos de alertas internas, latencia de confirmación y comportamiento de histéresis por corrida. | La corrida permite reconstruir el comportamiento del plano de control: qué patrones se evaluaron, cuándo transitaron a estado confirmado y qué evidencia originó cada alerta interna. |

| 11 | Reporte experimental de corrida | Núcleo validable | Salida consolidada con configuración, métricas, alertas internas, errores, descartes y límites de interpretación. | La corrida queda lista para análisis comparativo y defensa experimental. |



Nota. El núcleo validable no representa todas las capacidades posibles de la plataforma, sino el mínimo necesario para producir una corrida DBE defendible sobre CR-01 y CR-02.

Tabla 59Backlog de extensiones condicionadas

| Orden | Ítem de backlog | Prioridad | Entregable esperado | Criterio de aceptación |

| 12 | Ejecución EBE básica con fuente viva controlada | Extensión condicionada | Integración de una fuente continua con timestamps, control de ritmo conceptual, omisiones, descartes y métricas. | EBE se incorpora sin modificar los contratos del núcleo ni reemplazar DBE como escenario de estabilización. |

| 13 | Participación del rol EN como captura o ingesta | Extensión condicionada | Captura, ingesta, preprocesamiento no semántico o preselección conservadora declarada por corrida. | El rol EN no ejecuta inferencia OVD en el núcleo y cualquier descarte o transformación queda instrumentado. |

| 14 | Inspección mínima de resultados | Extensión condicionada | Consulta básica de corridas, alertas internas, métricas, errores, eventos y evidencia asociada. | Los resultados pueden revisarse sin alterar el flujo experimental ni introducir lógica de producto final. |

| 15 | Comparación con variante ajustada al dominio | Extensión condicionada | Evaluación de un checkpoint candidato frente a la baseline zero-shot. | La comparación sólo se considera válida si la baseline permanece congelada, las particiones son consistentes y la evaluación se realiza en el flujo de referencia. |

| 16 | Incorporación de MOT, zonas o reglas espaciales | Exploratoria | Módulos de seguimiento temporal, zonas o relaciones espaciales para condiciones de mayor complejidad. | La extensión sólo se habilita si aporta valor analítico y no bloquea la validación de CR-01 y CR-02. |



Nota. Las extensiones no forman parte del núcleo validable. Su incorporación debe declararse en la configuración de corrida y no debe alterar la comparabilidad de los resultados obtenidos con el flujo base.

El avance de implementación queda condicionado por criterios de cierre. Una unidad no se considera completada sólo por disponer de código funcional, sino cuando produce evidencia verificable dentro de una corrida experimental. En consecuencia, antes de avanzar hacia EBE, EN, adaptación de modelos o MOT, debe existir al menos una corrida DBE reportable para CR-01 y CR-02.

Con esta organización, el backlog evita sobredimensionar el alcance del prototipo experimental. La prioridad no se define por atractivo funcional ni por cantidad de hosts, sino por dependencia respecto de la evidencia: primero se construye una cadena mínima reproducible, medible y reconstruible; luego se incorporan extensiones que aumentan realismo o capacidad analítica sin comprometer trazabilidad, comparabilidad ni control de alcance.

### 17.3.18. Cierre del diseño arquitectónico

El diseño desarrollado en este capítulo define una arquitectura modular, desacoplada, trazable y medible para la plataforma experimental. Su propósito es orientar la construcción incremental del prototipo, sin fijar una implementación definitiva ni ampliar el alcance experimental previamente delimitado.

La arquitectura separa responsabilidades entre configuración experimental, fuentes visuales externas, plano de medios, plano de control, distribución de alertas y soporte experimental. Esta organización permite distinguir la ingesta y normalización de evidencia visual, la inferencia OVD, la evaluación de patrones, la generación de alertas y el registro de eventos, métricas y evidencias mínimas para reconstrucción posterior.

El núcleo validable se concentra en CR-01 y CR-02, asociadas a condiciones visuales directas de EPP. A partir de ellas se establece una primera cadena experimental completa: configuración de corrida, fuente DBE, prompts versionados, inferencia OVD, normalización de detecciones, publicación de eventos, evaluación de patrones, alerta interna, observabilidad y reporte. Las condiciones de mayor complejidad quedan previstas como extensiones condicionadas, sujetas a reglas espaciales, zonas parametrizadas, seguimiento temporal, fuentes fijas o datos suficientes para interpretación contextual.

Tabla 60

Criterios de cierre del diseño arquitectónico

| Criterio de cierre | Implicancia para la implementación |

| Arquitectura general definida | Permite iniciar el desarrollo con responsabilidades diferenciadas y sin acoplar inferencia, patrones, reportes o salidas externas. |

| Configuración experimental materializada | Cada corrida puede ejecutarse, repetirse y compararse bajo parámetros explícitos. |

| Plano de medios delimitado | La ruta crítica de vídeo queda acotada, medible y separada de la interpretación de riesgo. |

| Plano de control definido | Las detecciones puntuales pueden transformarse en episodios trazables sin generar alertas por frame. |

| Cadena condición-estrategia-patrón-alerta integrada | El sistema conserva una lectura causal desde la definición metodológica hasta la salida asistiva interna. |

| Distribución de alertas confirmadas separada | Las notificaciones o integraciones externas no alteran la semántica de la alerta ni la métrica principal del sistema. |

| Contratos preliminares identificados | La implementación puede avanzar sobre estructuras de intercambio comunes sin fijar todavía una API definitiva. |

| Trazabilidad y minimización visual establecidas | Las alertas pueden reconstruirse sin depender del almacenamiento continuo de video crudo. |

| Observabilidad e instrumentación definidas | Las métricas pueden calcularse, declararse no aplicables o marcarse como limitadas según la configuración y la calidad de la corrida. |

| Topologías y nodos delimitados | Las conclusiones de latencia, inferencia, patrones y alertas quedan ancladas al escenario y nodo efectivamente evaluados. |

| Riesgos y backlog preparados | La etapa queda preparada para una implementación incremental centrada primero en una corrida DBE defendible. |



Nota. La tabla resume criterios de cierre del diseño arquitectónico. No constituye una lista de pruebas de implementación, sino una verificación de que el capítulo deja definidas las responsabilidades, fronteras, decisiones y evidencias necesarias para iniciar la construcción incremental del prototipo experimental.

Con estos criterios, la Etapa 3 queda cerrada y habilita el paso a la implementación incremental del prototipo. La prioridad inmediata será construir y medir el núcleo validable bajo una corrida DBE reproducible para CR-01 y CR-02. Una vez estabilizada esa cadena mínima, podrán incorporarse EBE, roles EN/TN, distribución externa, MOT, zonas o adaptación al dominio como variantes condicionadas.La arquitectura queda definida en términos de responsabilidades, contratos, escenarios y criterios de observabilidad, sin fijar una distribución física obligatoria de componentes.

La arquitectura propuesta deja establecido el marco técnico necesario para construir, probar y analizar el prototipo experimental con rigor ingenieril, preservando modularidad, trazabilidad, medición y control de alcance.

---

## Fuente: `docs/informe/ajustes/03-etapa-3-diseno-arquitectonico.md`

> SHA-256 del bloque: `a2bc9f430a060c95d0ad78627f3455fbf152cf3b506bdf32ae5efbdd3baa9ba2`  
> Seleccion: documento completo.

# Etapa 3 — ajustes al diseño arquitectónico (§17.3)

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

## Fuente: `docs/informe/ajustes/material-etapa-3/93-redlines-etapa3.md`

> SHA-256 del bloque: `a35a849f558adac2b2b4837f32c976a4a24e3d0dd6a12abda72847cb9acdcd87`  
> Seleccion: documento completo.

# Redlines de Etapa 3 — hoja de trabajo para revisión

- **Fecha:** 2026-07-12
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

**→ Texto completo en `94-secciones-nuevas-etapa3.md` §8.**

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

> SHA-256 del bloque: `cde39a522f0a2ec8cfcb6f5b260242b51ce0c2909151f04ad8011fd87c0e0235`  
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
> El fragmento siguiente reproduce un evento **real** de la corrida de evaluación: la unidad visual en la
> que el sistema confirma la condición CR-01, a los 4000 ms de persistencia configurados. De las
> veintidós detecciones que contiene la unidad se muestran dos.

**Nota:** presentalo como *Figura N — Evento de percepción (extracto de artefacto real)*, en monoespaciado.
Es lo que el tutor pidió con nombre propio ("un DTO"). **Este JSON es literal** — verificado contra
`detections.jsonl`, unidad `frame_000120`. No lo "mejores" al pegarlo.

> ⚠️ **2026-08-12 — RESOLVER ANTES DE PEGAR: el `source_id` es de un clip retirado.**
> La corrida de la que sale esta línea se hizo el 2026-07-11 sobre **`cb_b01_p7`**, y ese clip
> fue **retirado del banco el 2026-08-03** (licencia sin registrar + GT generado por IA;
> `datasets/processed/clip_bench/_retired/cb_b01_p7/MOTIVO.md`). El JSON es impecable como
> **ejemplo de esquema** —no se está citando ningún resultado suyo—, pero **mete en el informe
> el identificador de un clip que no existe en el banco congelado**, y es exactamente lo que la
> trampa 5 de `GUIA-REDACTORES` §4 manda no hacer.
>
> **No se arregla editando el identificador a mano**: eso rompería la garantía de transcripción
> literal que costó una auditoría establecer (la v1 de este documento tenía un JSON fabricado).
> Las dos salidas honestas:
>
> | Opción | Qué implica |
> |---|---|
> | **(a) Re-transcribir** ✅ recomendada | Correr un replay DBE sobre un clip **del banco vigente**, y transcribir esa línea literalmente. Es barato (replay, sin GPU nueva) y deja el ejemplo por encima de toda sospecha |
> | (b) Redactar el identificador | Conservar la línea real y sustituir el `source_id` por `"<clip_id>"`, **declarando en el pie que el identificador fue omitido**. Sigue siendo honesto porque la omisión se declara, pero pierde el "esto salió tal cual de un artefacto" |
>
> Lo que **no** es opción: pegarlo tal cual y esperar que nadie pregunte qué es `cb_b01_p7`.

> ```json
> {
>   "schema_version": "media.detection.v1",
>   "event_type": "detection_event",
>   "run_id": "run_20260711_211647_dbe_grounding_dino_6114c6",
>   "unit_id": "frame_000120",
>   "source":  { "source_id": "cb_b01_p7", "source_type": "video_frame",
>                "frame_index": 120, "timestamp_ms": 4000.0,
>                "width": 1920, "height": 1080 },
>   "model":   { "name": "grounding_dino",
>                "model_id": "IDEA-Research/grounding-dino-tiny", "device": "cuda" },
>   "prompts": { "prompt_set_id": "cr01_cr02_v2_short_inline" },
>   "detections": [
>     { "detection_id": "det_000001", "label": "person",
>       "prompt_id": "person", "source_prompt": "person", "confidence": 0.8257,
>       "bbox_xyxy":      [1734.6, 300.9, 1838.2, 525.8],
>       "bbox_norm_xyxy": [0.9034, 0.2786, 0.9574, 0.4869],
>       "area_px": 23291.6, "model_name": "grounding_dino" },
>     { "detection_id": "det_000002", "label": "person",
>       "prompt_id": "person", "source_prompt": "person", "confidence": 0.837,
>       "bbox_xyxy":      [159.5, 402.2, 253.4, 639.8],
>       "bbox_norm_xyxy": [0.0831, 0.3724, 0.132, 0.5924],
>       "area_px": 22312.3, "model_name": "grounding_dino" }
>   ],
>   "timing": { "normalize_ms": 8.25, "inference_ms": 214.37,
>               "postprocess_ms": 0.2, "write_ms": 0.0, "total_ms": 214.59 }
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
> confirmación de un episodio de riesgo. El fragmento siguiente reproduce la alerta **real** emitida por la
> corrida de evaluación sobre el clip de obra.

> ```json
> {
>   "schema_version": "control.alert.v1",
>   "event_type": "alert_event",
>   "control_run_id": "bench_cb_b01_p7_gdino_20260712_20260712T232146Z",
>   "media_run_id":   "run_20260711_211647_dbe_grounding_dino_6114c6",
>   "alert_id": "ff1ffb62-60a9-5e19-a7b8-42d076864f14",
>   "pattern_id": "CR-01", "condition_id": "CR-01",
>   "subject_key": "CR-01:cb_b01_p7", "source_id": "cb_b01_p7",
>   "severity": "high", "state": "open",
>   "unit_id": "frame_000120", "frame_index": 120, "timestamp_ms": 4000.0,
>   "evidence": {
>     "subject": { "detection_id": "det_000013", "label": "person", "confidence": 0.502,
>                  "bbox_xyxy": [1065.4, 1005.4, 1185.9, 1081.2] },
>     "missing_class": "helmet",
>     "supporting": [ { "detection_id": "det_000021", "label": "person", "confidence": 0.4016 },
>                     { "detection_id": "det_000022", "label": "person", "confidence": 0.4147 } ],
>     "score": 0.502, "subjects_in_evidence": 3,
>     "rationale": "No se encontró evidencia de 'helmet' en la región 'upper_body' de 3 sujeto(s)."
>   },
>   "first_evidence_ms": 230525124.622, "first_evidence_unit_id": "frame_000000",
>   "alert_registered_ms": 230525159.420
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
> **El sistema confirma cuando su configuración lo prescribe.** La alerta se registra en la unidad visual
> correspondiente a `timestamp_ms = 4000,0`, que es exactamente la ventana de persistencia configurada
> para CR-01.

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
> | **Distribución de alertas** (canal de notificación) | **Funcionalmente implementada** | DBE/EBE, cooldown, idempotencia, MQTT QoS 1 y reporte fueron verificados. Quedan la vista de webconsole, la orquestación y versionar el repo. |
> | **Latencia captura-a-resultado en topología de dos nodos** | Instrumentada; **no computable** | Los relojes monotónicos de hosts distintos no son comparables: la métrica se declara **no interpretable**, con causa, en lugar de publicarse. |
> | **Comparación con modelo adaptado** (ajuste fino) | Rama experimental comprometida; **T1 full en NO-GO técnico** (adenda ADR-017, 2026-08-13) | F-100.1, freeze/smoke, dual gate, serving y procedencia T-FT-023 están cerrados (snapshot `639e60df…`). ✎ **2026-08-15: D-FT-08/T-FT-005, D-FT-12 y D-FT-13 firmadas, y T-FT-031/032 cerradas la misma jornada** (doc 120: baseline 26s one-shot — `bare_head` AP50 0,000, recall CR-01 agregado 0,0002); resta `full-authorization.json` + `RUN` manual. La causa es técnica/protocolar, nunca temporal; se declarará el estado real a la entrega. |
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

