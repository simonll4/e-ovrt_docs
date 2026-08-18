# E-OVRT-VDP - contexto base para redaccion

> Generado el 2026-08-18. Archivo estable del knowledge; se usa junto al paquete de la etapa activa.

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
- **La plataforma tiene TRES patrones de acople, no dos** (ADR-018, aceptada 2026-08-15):
  HTTP config-driven a los dos planos, bus ZeroMQ, y **BFF-subproceso** para el modulo de
  distribucion, que es CLI y no servicio. El dato de distribucion igual viaja por el bus
  (`:5558`); lo propio del tercer patron es el control del ciclo de vida.
  **✎ 2026-08-18 — LA VIÑETA DE ARRIBA QUEDO SUPERADA POR COMPLETO. ADR-020 derogo a
  ADR-018: los patrones de acople son DOS, no tres.** Secuencia del dia: ADR-019 le dio al
  distribuidor servicio HTTP propio (`eovrt-distribute serve`, `:8082`, espejo del
  control-plane, verificado en vivo con camara real) y ADR-020 **invirtio el default** —
  HTTP paso a ser el acople normal y el subproceso bajo a **fallback operativo**
  (`EOVRT_CONSOLE_DISTRIBUTION_TRANSPORT=subprocess`), dejando de ser un patron.
  **Al redactar, la descripcion vigente es esta y no otra:**
  **(a) HTTP config-driven en los TRES modulos** (`:8080` medios, `:8081` control,
  `:8082` distribucion), con la webconsole y el runner como clientes; **(b) bus ZeroMQ
  PUB/SUB + msgpack** para el dato (detecciones `:5557`, alertas `:5558`).
  **NO escribir "BFF-subproceso" ni contar un tercer patron**: el fallback por subproceso
  es un detalle de operacion, no arquitectura, y no va al informe. Tampoco escribir "el
  modulo es una CLI y no un servicio": es servicio, y ademas conserva su CLI para el
  camino offline (igual que el control-plane).
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

---

## Fuente: `docs/GUIA-REDACTORES.md`

> SHA-256 del bloque: `74b2f5eff5a83f9a006075c384cbc8769e3b25592dd70c900504059b73f2a69c`  
> Seleccion: documento completo.

# Guía para redactar el informe — para quien NO participó del trabajo experimental

**Vos sos el lector previsto de este documento.** Todo el resto del set `docs/` está
escrito como memoria de trabajo de quienes hicieron los experimentos: usa voseo, da por
sabido el contexto y cita códigos sin definirlos. Este archivo es la única puerta de
entrada pensada para alguien que llega de cero y tiene que escribir el capítulo de
resultados.

- **Fecha:** 2026-08-10 · ✎ **act. 2026-08-13** · **Estado:** tramo experimental **cerrado y
  verificado**, con **una excepción declarada**: la **jornada de fine-tuning (E-04) está en
  curso** y corre en paralelo. Por ADR-017 §2f **no bloquea la redacción**; su subsección de
  resultados queda reservada (`informe/ajustes/05` → `AJ-5.13`). Todo lo demás está congelado.
- **Qué NO vas a encontrar acá:** cifras. Las cifras tienen una sola fuente y está más
  abajo. Si un número aparece en este documento es como ejemplo de cómo citarlo, no como
  fuente.

---

## 1. El proyecto en cinco minutos

Se construyó una **plataforma de detección de riesgos de seguridad en obra** que usa
modelos de **detección open-vocabulary** (OVD): modelos a los que se les describe en
**lenguaje natural** qué buscar, en vez de entrenarlos con ejemplos etiquetados.

Se detectan dos condiciones de riesgo:

- **CR-01** — una persona **sin casco**.
- **CR-02** — una persona **sin chaleco** reflectivo.

**La tesis NO es "OVD detecta mejor que un modelo entrenado".** Eso sería perder: un
modelo entrenado para cascos detecta cascos mejor. La tesis es:

> *¿Qué rendimiento se obtiene **hoy**, en construcción civil, expresando las condiciones
> de riesgo **en lenguaje** y **sin entrenar el modelo**, y qué aporta la **plataforma**
> construida alrededor del modelo?*

Esa distinción gobierna todo el capítulo. **Cada número es el rendimiento medido de una
combinación concreta, no una nota de aprobación.** Un recall de 0,40 en multitud no es un
fracaso del proyecto: es el dato. **El contraste entre filas ES el experimento.**

### Las tres piezas de software

| Pieza | Qué hace |
|---|---|
| **media-plane** | Recibe video (archivo o cámara), corre el modelo OVD y emite **detecciones** |
| **control-plane** | Consume detecciones y decide si hay que **alertar**, aplicando una ventana temporal (no alerta con un solo frame: exige que la condición persista) |
| **experimental-setup** | La consola web y el runner de experimentos; también guarda los **resultados** |

> **Hay un cuarto repo, y no es un tercer plano.** `e-ovrt_alert-distribution` consume
> alertas ya confirmadas, aplica cooldown e idempotencia, entrega por MQTT y registra cada
> resultado. ✎ **Estado verificado 2026-08-11:** está **funcionalmente implementado** y
> cumple los seis criterios de spec 45: replay DBE idempotente, camino EBE desde el
> publisher real, MQTT QoS 1 contra broker real y reporte consolidado. Su suite cerró con
> 39 tests unitarios más la integración MQTT.
>
> **Qué falta, y no hay que ocultarlo:** E-06 (canales adicionales y dashboard propio)
> permanece excluida. ✎ **2026-08-14:** los tres pendientes que este párrafo listaba —vista
> de outcomes en la webconsole, orquestación integral del distribuidor y versionar el
> repo— se cerraron el 2026-08-13 (commits `13c801e` y `42529e2` en
> `e-ovrt_experimental-setup`; el repo `e-ovrt_alert-distribution` ya tiene historia propia,
> `c9903cc` y `1e6d8fa`). El diseño y los contratos
> se redactan desde `informe/92b`; el estado ejecutado y sus salvedades, desde
> `operacion/114`. Las latencias de loopback usadas para verificar el canal no se convierten
> en una cifra de desempeño de la tesis.

La cifra citable del tramo de distribución es **`t_alert-notification` p95 =
64,534 ms (n = 460 entregas live)** (`results/realtime/t_alert_notification/metrics.json`;
protocolo y contención en `operacion/118`). Mide **bus de alertas → PUBACK MQTT**, no
captura, inferencia ni evaluación del patrón. Para operación continua citar también el
régimen sostenido: entregas 2.ª+ **p95 = 102,025 ms (n = 104)**; las primeras entregas
dan 49,869 ms (n = 356). El smoke de loopback no es desempeño; la campaña del doc 118 sí.

### Dos escenarios de despliegue

- **DBE** — todo en un host, sobre archivos de video. Es el modo con el que se midió casi
  todo, porque es **reproducible**: la misma entrada da la misma salida.
- **EBE** — en vivo, con cámara, y los dos planos comunicándose por un bus. Es el modo que
  demuestra que funciona en tiempo real.

### Tres niveles de medición — **no los confundas, es el error más caro**

| Nivel | Qué mide | Unidad | Dónde |
|---|---|---|---|
| **Percepción (imágenes)** | ¿El modelo ve las cosas? AP por clase | una imagen | `bench_imagenes/` |
| **Nivel A** | ¿Determina bien el **estado de cada persona** (con/sin casco)? Sin tiempo | una persona | `bench_nivel_a/` |
| **Nivel B** | ¿La **plataforma entera** emite la alerta correcta? Con motor temporal | un episodio de video | `clip_bench/` |

Nivel B es **el resultado principal de la tesis**, porque es el único que mide la
plataforma y no solo el modelo.

---

## 2. Orden de lectura — cinco pasos, en este orden

1. **Este documento**, hasta el final. Incluye las trampas; saltearlas cuesta caro.
2. **`docs/sintesis/fundamentos-teoricos.md`** — la teoría, sin cifras. Es lo más
   pedagógico del set y explica por qué el diseño experimental es el que es.
3. **`docs/13-glosario-y-convenciones-de-lectura.md`** — siglas, las reglas de oro de
   lectura y (en §4.1–4.3) los códigos, los IDs de campaña y las colisiones de símbolos.
4. **`docs/sintesis/resultados-y-conclusiones.md`** — la narrativa completa con cifras.
   **Es el documento central para escribir el capítulo.** Su §8 trae la escala
   **AF-1…AF-11**: qué se afirma y **con qué fuerza**.
5. **`e-ovrt_experimental-setup/results/index.md`** y sus cuatro índices — **la única
   fuente de cifras**. Cada tabla de ahí tiene su artefacto en disco.

Cuando ya entendiste el trabajo y vas a **escribir**, el sexto paso es
**`docs/informe/ajustes/00-mapa-de-ajustes.md`**: te dice, etapa por etapa (1 → 6), qué hay
que corregir del texto que ya existe y qué hay que escribir desde cero. **Tres secciones del
informe están vacías —§17.4 Implementación, §17.5 Evaluación y §17.6 Cierre—**, y ese mapa
es el que dice qué va en cada una y de dónde sale.

> **Las etapas son seis, y son la guía de desarrollo del proyecto** (Gantt del §14.3 =
> §14.2): 1 investigación bibliográfica · 2 análisis metodológico · 3 diseño arquitectónico ·
> 4 implementación MVP · 5 evaluación y validación · 6 documentación y defensa. **El informe
> está ordenado por sección, no por etapa**, así que la correspondencia etapa → sección la
> tenés en el §0 del mapa. Ojo con un detalle: **el Gantt numera las tareas 0–5 y el §14.2
> numera las etapas 1–6** — misma secuencia, corrida en uno.
>
> **Y la regla que gobierna el tiempo narrativo (no-anacronismo, mapa regla 5): una etapa
> temprana no menciona resultados de etapas posteriores.** §15/§16 dejan la brecha con
> literatura; §17.1 deja decisiones y criterios; **todo número propio vive en §17.5/§18**.
> Si al corregir §15 te ves escribiendo una cifra medida por el proyecto, estás en la
> sección equivocada.

Recién después, y solo si necesitás el detalle de un experimento puntual, vas al documento
de `docs/operacion/NN` que la síntesis te indique.

### Qué **no** abrir

| No abras | Por qué |
|---|---|
| `docs/GUIA-CIERRE.md` y `docs/operacion/113` | Son el checklist operativo **del equipo experimental**, no material de redacción |
| `docs/informe/92` y `docs/operacion/56` y `92` | **Derogados como fuente de cifras** |
| `docs/operacion/32`, `36`, `50` | Estado de plataforma superado por `operacion/97` |
| `../informe-project-kit/` | Kit aplanado externo **eliminado**. Para ChatGPT usar `docs/informe/project-kit/README.md`: cuatro archivos de knowledge — dos `.md` generados por etapa + dos DOCX del entregable (✎ 2026-08-16) |
| Cualquier doc de `operacion/` con banner ⚠️ | Los banners dicen qué quedó superado. **Leé el banner antes que el cuerpo, siempre** |

**Regla general del set:** un documento con banner de corrección **manda por el banner, no
por el cuerpo**. Los cuerpos se conservan a propósito, para trazabilidad.

---

## 3. Cómo citar una cifra — ejemplos pareados

Estas fórmulas no son estilo: son **precisión**. Cada una existe porque la versión de la
izquierda ya se escribió mal alguna vez.

| ❌ Así NO | ✅ Así SÍ | Por qué |
|---|---|---|
| "El sistema alcanza F1 0,930" | "La mejor combinación medida (**G1**: identidad por sujeto) alcanza **F1 0,930** sobre el banco del rodaje, contra 0,789 de la línea de base" | Un número sin su combinación y su banco no significa nada |
| "El banco tiene 34 clips" | "El banco tiene **47 clips** (32 positivos / 15 negativos, **37 episodios**), en dos bloques: **A**, el rodaje guionado (34), y **B**, el lote de obra real (13)" | 34 es el **Bloque A**, no el banco |
| "34 episodios evaluables sobre 35" *(como denominador del banco)* | "34 evaluables sobre 35 **en el bloque del rodaje**" | Es el denominador de un bloque, no del banco |
| "El FAR es de 29,2 falsas alarmas por hora" | "**3 falsos positivos en 6:09,6** del único clip de soak; la tasa horaria derivada es 29,2 FA/h, sobre un denominador de 0,1027 h" | La tasa desnuda sugiere una hora observada que **no existe** |
| "El sistema cumple ≤1 FA/hora" | *(no se puede afirmar)* — "para sostener una cota harían falta ~3 h de cumplimiento anotado; el banco llega a 0,1027 h" | **Limitación L1** |
| "A nivel de escena (0,333) el sistema supera al de sujeto (0,190)" | "En el estrato B, con **solo 2 episodios evaluables**, la diferencia de F1 **no es interpretable**. Lo robusto es la **asimetría de falsos positivos**: 26 contra 323 sobre 11 clips negativos (**12×**)" | Con n=2 eso es ruido |
| "El lote de internet valida el sistema en obra real" | "El lote aporta medición en obra real **acotada**, y su aporte principal es **caracterizar dónde el sistema deja de ser evaluable**" | **Limitación L4, precisada** |
| "mAP50 0,551" | "mAP50 **0,551** sobre `bench_v3` (6.477 imágenes de **3 fuentes independientes**), con el desglose por estrato" | **Nunca solo el agregado** (limitación L5) |
| "Los clips negativos bajan el F1" | "Los clips negativos **no entran** a precision/recall/F1: su métrica son los falsos positivos" | Promediarlos cuenta aciertos como catástrofes |
| "El sistema emitió 12 falsos positivos" *(contando re-alertas)* | "…sin contar `re_alerts`, que son re-confirmaciones con la infracción **todavía activa**" | Una re-alerta no es un error |
| "La latencia de vidrio a alerta es de 14,7 ms" | "El tramo medido G2A es de 14,7 ms **desde el dequeue**; de vidrio a alerta hay que sumarle la captura (202–217 ms en el rodaje)" | Se mide desde el dequeue, no desde el fotón |
| "El SDR mejora al bajar la densidad" | *(no se compara)* — "el SDR **solo es comparable dentro de una misma cadencia**" | Es artefacto del instrumento |

**Regla que resume todas:** un número va siempre con **(a)** qué combinación lo produjo,
**(b)** sobre qué material, y **(c)** con qué `n`.

### 3.1 ✎ Qué NO se referencia jamás en el texto del informe (regla del usuario, 2026-08-16)

**El informe es autocontenido.** Toda esta documentación —los docs de `operacion/`, los
ADRs (de cualquier serie), las specs, las fichas `AJ-`/`R-`/`PODA-`, los IDs internos
(`F-xx.x`, `D-xx.x`, `T-FT-xxx`), las rutas del repo y los índices de `results/`— es
**andamiaje local para guiar el desarrollo**, y el informe **no la menciona nunca**: ni
como cita, ni como paréntesis de procedencia, ni como nota al pie. En el texto del
informe una afirmación se sostiene por el propio informe (§), por la bibliografía, o por
la combinación experimental declarada (la regla (a)(b)(c) de arriba) — sin decir de qué
archivo interno salió el número. La procedencia interna vive en los borradores como
notas al integrador (bloques `> ✎`, que no se pegan) y en el tablero del manual `08`.
Sí se usan los identificadores que el informe define para sí: condiciones CR-01/CR-02,
contratos (`media.detection.v1`), limitaciones L1–L8, nombres de configuración.

---

## 4. Las siete trampas que más caro salen

> **Trampa del banco de clips:** 47 = 34 rodaje + 13 internet (bloques A/B del
> manifest) y, por otra partición, 32 positivos + 15 negativos. Nunca mezclar ambas
> descomposiciones en una misma frase.

**1. Escribir el capítulo sobre el banco de 34 clips.** Es el error más probable, porque
varios documentos del kit fueron escritos cuando ese era el banco. **Vigente: 47 clips,
37 episodios.** Si un documento dice 34 sin aclarar "bloque A", está desactualizado.

**2. Decir que no se midieron falsas alarmas** (porque un doc viejo dice que FAR/hora "no
es una métrica de este trabajo"). **Se mide y se reporta**, pero no sostiene una cota. Ver
la tabla de arriba.

**3. Rankear granularidades en el estrato B.** Con 2 episodios evaluables no sale ningún
ranking. Lo publicable de ese estrato es la asimetría de falsos positivos y la frontera de
juzgabilidad.

**4. Decir que el lote de internet "levanta" la limitación L4.** La decisión firmada dice
**precisada, no levantada**. Varios documentos viejos usan "levanta".

**5. Citar el "BENCH de 196 imágenes" o el clip `cb_b01_p7`.** Los dos están **retirados**:
el primero por estar 20–25 % fuera de dominio, el segundo por licencia sin registrar y GT
generado por IA. Si los ves citados en un doc, ese doc es viejo.

**6. Encuadrar el fine-tuning como "descartado por falta de tiempo"** (o "por
presupuesto de tiempo", o "por secuenciación" — la enmienda intermedia). Documentos
viejos del kit lo dicen; **esa causa está prohibida (ADR-017)**. Vigente: el
fine-tuning (E-04) es una **rama experimental condicionada por datos y protocolo desde
el planteo** (Tabla 37: baseline primero; F-100.1 ya resuelta; gates vigentes de freeze,
serving/evaluación y procedencia) — el cómputo nunca fue la causa de descarte (Mendieta
disponible y envelope T1 acotado) — y está
**comprometida como jornada completa**, que se documenta con sus resultados,
limitaciones y estado a la entrega, con causa técnica.

> ✎ **2026-08-13 — estado operativo:** `1166583` cerró freeze/smoke técnico en A30 con
> 12 tensores/3.096 parámetros y optimizer 12/12; dual gate y serving real están verdes.
> T1 full sigue en NO-GO por contrato de serving (D-FT-08/T-FT-005), evaluación
> (T-FT-031) y baseline YOLOE-26s (T-FT-032). La procedencia (T-FT-023) quedó
> **CERRADA** el 2026-08-13 (snapshot tar `639e60df…`).
> ✎ **2026-08-15 — el contrato de serving quedó CERRADO, y la misma jornada cerraron
> T-FT-031 y T-FT-032.** El usuario firmó D-FT-08 (T-FT-005 `done`), D-FT-12 y D-FT-13,
> y después se ejecutó todo lo técnico: comando de evaluación congelado, enforcement
> canónico v2 y **baseline YOLOE-26s one-shot sobre `bench_v3`** (doc 120: `bare_head`
> AP50 0,000; recall CR-01 agregado 0,0002; retención a proteger person 0,7843 /
> helmet 0,6286 / vest 0,2642 — cifras de la RAMA, tablas propias, por estrato).
> **El NO-GO de T1 full quedó en su último eslabón**: emitir `full-authorization.json` y
> el `RUN` manual (T-FT-043). Al redactar: no listar decisiones NI gates técnicas
> pendientes en E-04; ~~**no hay cifra del checkpoint ajustado** (no existe)~~ **← SUPERADO
> el 2026-08-17, ver la adenda al final de este bloque: la cifra existe** y la baseline
> no se compara con la tabla histórica del doc 64 (doc 120 §2.5). **D-FT-12 se firmó
> antes de la baseline**: pre-registración estricta. La negativa sin auth dejó cero
> full. La proyección Slurm 2026-08-18 no es
> promesa. No hay cifra científica citable ni job full enviado.
>
> ✎ **2026-08-15 (noche) — T-FT-043 CERRADA: el job full se envió.** La autorización se
> emitió y verificó en el clúster con sus 7 gates, el ensayo `--test-only` pasó y el
> `RUN` quedó **encolado (job `1167640`)**. Lo de arriba —"último eslabón", "cero jobs
> full", "ni job full enviado"— queda **superado**: ya no hay ninguna tarea previa
> pendiente. **Lo que sigue abierto es otra cosa: la corrida en sí y su evaluación.**
> Enviar no es medir: **sigue sin existir cifra del modelo ajustado**, así que en el
> informe esa subsección va reservada con `[[PENDIENTE: …]]`, nunca con un valor
> estimado ni con una redacción que sugiera que la comparación ya se hizo.
>
> ✎ **2026-08-17 — LA JORNADA CERRÓ Y LA CIFRA YA EXISTE: veredicto D-FT-12 = NO-GO**
> (`operacion/123` (fuente: `docs/operacion/123-cierre-jornada-t1-no-go.md`)). **La subsección deja de ir
> reservada: se redacta con estos números** — `bare_head` AP50 **0,0000 → 0,0455** y recall
> CR-01 **0,0002 → 0,2089** (de 1 violador detectado en todo el banco a 1.109), `vest`
> 0,2642 → **0,3292**, contra `person` 0,7843 → 0,6932 y mAP50 0,4193 → 0,4171. **NO-GO**
> porque el gain gate pedía +0,05 (faltaron **0,0045**) o recall >0,5, y la retención de
> `person` cayó **−11,62 %** sobre un tope de 10 %.
>
> **Cómo redactarlo, sin margen:** es un **negativo pre-registrado** — los márgenes se
> firmaron el 15/08 antes de existir baseline y checkpoint — así que **es un resultado, no un
> fracaso**, y **jamás** se atribuye a falta de tiempo (criterio de invalidación 1 de
> ADR-017). Reportar **siempre por estrato además del agregado**: en `bench_obra_val` el
> ajuste **mejora** (mAP50 +0,0828, `bare_head` 0,000 → 0,2614) y son `chv`/`shel5k` los que
> bajan, por `helmet`. Estas cifras son de la **rama comparativa**: no se funden con el
> núcleo zero-shot, no van a `results/` y **no se comparan con la tabla del doc 64**
> (protocolo distinto). El gate de latencia **no se midió** y eso se dice explícito (F-123.1),
> no se omite.
>
> **T2 (si su jornada corre antes del cierre del informe) se redacta con esta secuencia
> exacta, sin suavizarla:** tras el NO-GO de T1 la escalera cerró la rama; una **enmienda
> explícita (D-FT-14, 2026-08-17)** reabrió T2 como tier **exploratorio** para descartar que
> el fallo fuera artefacto de capacidad, **con márgenes propios firmados antes de cualquier
> resultado T2** (D-FT-15) y expectativa pre-registrada (NO-GO probable). Nunca presentarlo
> como reintento de T1 ni omitir que la enmienda fue posterior al veredicto — la transparencia
> de la secuencia ES el argumento. **T3 no corre**: trabajo futuro con causa técnica (sin
> baseline MM-GDINO geométricamente sana), jamás "falta de tiempo".

**7. Describir la plataforma con DOS patrones de acople.** Son **tres**, y el tercero está
registrado en **ADR-018 (fuente: `docs/decisiones/adr-018-acople-bff-subproceso-distribucion.md`)** desde
el 2026-08-15: **(a)** HTTP config-driven — la webconsole y el runner son clientes de los
dos planos (ADR-008/009); **(b)** bus ZeroMQ PUB/SUB + msgpack, media→control (ADR-003);
**(c)** **BFF-subproceso** — el runner de la webconsole lanza `eovrt-distribute` como
proceso hijo local, porque el repo de distribución es una CLI y **no** un servicio HTTP.
Dos precisiones que se pierden fácil: el *dato* de distribución igual viaja por el bus
(`:5558`), así que lo propio del tercer patrón es el **control del ciclo de vida**, no el
transporte; y el requisito `EOVRT_DISTRIBUTION_EXECUTABLE` de la consola dockerizada es
parte de la decisión, no una nota de operación. Documentos anteriores al 08-15 describen
sólo dos acoples: están viejos.

> ⛔ **✎ 2026-08-18 — TODA LA TRAMPA 7 DE ARRIBA QUEDÓ SUPERADA. ADR-020 derogó a ADR-018
> y los patrones de acople volvieron a ser DOS.** El párrafo original (y su primera
> corrección del mismo día, que hablaba de tres) se conservan como cuerpo histórico, pero
> **no describen el sistema entregado**.
>
> **Lo vigente, y lo único que va al informe:**
> **(a) HTTP config-driven en los TRES módulos** — medios `:8080`, control `:8081` y
> **distribución `:8082`**; la webconsole y el runner son clientes de los tres y **ninguno
> consume el bus**. **(b) bus ZeroMQ PUB/SUB + msgpack** para el dato: detecciones
> `:5557` (medios→control) y alertas `:5558` (control→distribución).
>
> **Qué NO escribir:** "BFF-subproceso", "tres patrones de acople", "el repo de
> distribución es una CLI y no un servicio". El camino por subproceso **sigue existiendo
> en el código** como **fallback operativo** detrás de una variable de entorno, pero eso
> es un detalle de operación, **no arquitectura**: no se cuenta como patrón ni se
> describe en el capítulo. Y ojo con el matiz simétrico: el distribuidor **conserva su
> CLI** para el camino offline, igual que el control-plane — decir "es solo un servicio"
> tampoco es exacto.
>
> **La trampa, reformulada:** el número de patrones cambió tres veces en cuatro días
> (dos → tres con ADR-018 → tres con ADR-019 → **dos** con ADR-020). Cualquier documento
> que no lleve enmienda del 2026-08-18 está describiendo un estado intermedio.
>
> **Sobre la containerización, que es una pregunta aparte y tiene respuesta propia
> (✎ 2026-08-18):** está **diferida con causa** y **sí se puede mencionar en el informe**.
> Se va a hacer **después** de cerrar la redacción; su razón de ser es la
> **reproducibilidad** (que un tercero levante la plataforma en otra máquina), no cerrar
> el capítulo; y su **documentación operativa vive en los repositorios**, no en la tesis.
> Escribila como **compromiso declarado con su fundamento**, en el cierre (§17.6/§18) y en
> el anexo de reproducibilidad (§19). **Nunca en presente, nunca como capacidad existente,
> nunca como instructivo de despliegue.** Regla corta: *describir el compromiso es
> correcto; describir un despliegue que no corrió es falso.*

> ⏳ **✎ 2026-08-12 — y la jornada ARRANCÓ.** Corre en paralelo a la redacción y **no la
> bloquea** (ADR-017 §2f). Para vos significa tres cosas concretas: **(1)** el §17.5 tiene
> una subsección **reservada** para esa rama (`informe/ajustes/05` → `AJ-5.13`) — no la
> borres ni la escribas como exclusión; **(2)** mientras no haya un artefacto en `results/`,
> **no hay cifra citable** de esa rama; **(3)** sus resultados, cuando existan, van
> **rotulados como rama comparativa y en tablas propias** — nunca fundidos con los del
> núcleo zero-shot, porque la pregunta de la tesis es justamente cuánto rinde el stack
> **sin entrenar**. Un desenlace negativo es un resultado documentable, no una omisión.

---

## 5. Cómo se decide qué se puede afirmar

No lo decidís vos ni lo decide el número: está pre-registrado en la escala
**AF-1…AF-11** (síntesis §8), que clasifica cada conclusión por **fuerza de evidencia**:

- **Establecida** — se afirma sin hedging.
- **Establecida direccionalmente** — se afirma el sentido, no la magnitud.
- **Tendencia con mecanismo** — se describe el mecanismo, se declara que no es efecto
  establecido.
- **No cerrada** — se declara como limitación, no se afirma.

**Consultá esa tabla antes de escribir cualquier afirmación.** Y las **limitaciones
L1–L8** (versión vigente en `results/index.md`) se declaran, no se esconden: en este
trabajo lo que no se pudo medir es parte del resultado.

Un principio que atraviesa el capítulo: **varias de las cosas más valiosas del trabajo son
refutaciones de predicciones propias** — hipótesis escritas *antes* de medir y que la
medición tumbó. Eso se cuenta como fortaleza metodológica, no se disimula.

---

## 6. Dónde vive cada cosa

| Necesitás | Está en |
|---|---|
| **Cifras de cualquier tipo** | `e-ovrt_experimental-setup/results/index.md` + sus 4 índices |
| La narrativa completa con contexto | `docs/sintesis/resultados-y-conclusiones.md` |
| Teoría, definiciones, por qué el diseño es así | `docs/sintesis/fundamentos-teoricos.md` |
| Qué calcula cada métrica | `docs/sintesis/inventario-de-metricas.md` |
| Cómo está implementada la plataforma (concreción técnica) | `docs/operacion/97-relevamiento-plataforma-2026-08-05.md` — la foto verificada contra código (2.203 tests verdes) |
| El módulo de **distribución de alertas** (§17.3.10) | `docs/informe/ajustes/material-etapa-3/92b-concrecion-distribucion-alertas.md` — diseño y contratos · **`operacion/114`** — implementación verificada, pruebas y brechas · **`nucleo/19`** — ciclo de vida y fronteras · **`operacion/124`** — servicio HTTP (ADR-019). Estado: funcional e integrado — ~~pendientes webconsole, orquestación y commits~~ ✎ cerrados el 2026-08-13; desde el 2026-08-18 corre además como servicio HTTP (`:8082`, subproceso sigue default) |
| El kit para trabajar en **ChatGPT Web** | `docs/informe/project-kit/README.md` — instrucciones + cuatro archivos de knowledge: contexto base, etapa activa y los dos DOCX del entregable (informe sin §17.3 + Etapa 3 vigente; ✎ 2026-08-16) |
| Siglas, códigos, colisiones de símbolos | `docs/13-glosario-y-convenciones-de-lectura.md` §3 y §4 |
| Reglas de estilo y honestidad al redactar | `docs/informe/97` §1–§3 (⚠️ **su §5 está superada**) |
| Qué figura/tabla va en cada sección | `docs/informe/ajustes/gobierno/99-materiales-de-cierre.md` §1 (✎ al día al 2026-08-10 — incluye el tramo de video, T-82…T-84/FIG-F) |
| **Qué hay que cambiarle al informe, etapa por etapa** | ✎ **`docs/informe/ajustes/00-mapa-de-ajustes.md`** — el mapa de Etapa 1 a Etapa 6, con un documento por etapa (`01`…`06`). **Empezá por acá y no por el 93**: el 93 cubre solo la Etapa 3 |
| **Cómo se aplica todo eso: dónde escribís, en qué orden, qué te toca** | ✎ **`docs/informe/ajustes/08-manual-de-aplicacion.md`** — **es el documento del día 1.** Trae el reparto de trabajo, el orden con su dependencia dura (la vara del §15 antes que el §17.5), el loop repetible por sección, las cuatro puertas de cierre y el tablero de las 109 unidades. **Leelo después de esta guía y antes de tocar nada** |
| Qué hay que corregir del **§17.3** (Etapa 3) | `docs/informe/93` — los **26 redlines** (R-01…R-26). Enrutados desde `informe/ajustes/03-etapa-3-diseno-arquitectonico.md` |
| Las secciones que hay que **escribir desde cero** | **§17.4, §17.5 y §17.6 están vacías** en el informe. Qué tiene que decir cada una: `informe/ajustes/04-etapa-4-implementacion.md`, `05-etapa-5-evaluacion-y-validacion.md` y `06-etapa-6-documentacion-y-cierre.md` |
| Qué **recortar** del informe (está muy extenso) | ✎ `docs/informe/ajustes/07-critica-extension-y-poda.md` — 18 podas medidas (`PODA-nn`, ~27% del texto), con guardrails de qué NO tocar. Se aplica junto con los `AJ-`/`R-` de cada sección |
| Texto ya redactado para adaptar | `docs/informe/94` (§1–§9: cubre 9 de los 26 redlines, y es el modelo de estilo) |
| Por qué se decidió algo | Los **ADR** (`docs/decisiones/`) + `docs/nucleo/10` (alcance y exclusiones) |
| El detalle de un experimento puntual | `docs/operacion/NN` — entrá por la síntesis, que te dice cuál |

---

## 7. Si algo no cierra

**El set es grande y tiene tres semanas de correcciones encima.** Si encontrás dos
documentos que se contradicen, la jerarquía es:

1. `results/index.md` y sus índices — para **cifras**, siempre gana.
2. `docs/sintesis/resultados-y-conclusiones.md` — para **interpretación**.
3. El banner ⚠️ o ✎ de un documento — gana sobre el cuerpo de ese documento.
4. La fecha — más nuevo gana, y las fechas están en la cabecera de cada doc.

**Y si aun así no cierra, preguntá antes de escribir.** Una contradicción que sobrevive a
esa jerarquía probablemente sea un error real que conviene arreglar en el repo, no algo
que haya que resolver escribiendo con ambigüedad.

**Verificación mecánica disponible:** `python3 docs/operacion/datos/96-verificar-indices.py`
comprueba que las cifras citadas en los índices coincidan con los artefactos en disco (19
cifras sobre las 16 campañas). Si dudás de un número, corrélo.

---

## Fuente: `docs/13-glosario-y-convenciones-de-lectura.md`

> SHA-256 del bloque: `e0d64b7b39b48f6802c3d82d640405e4af0648b430da90449fc2973567121b48`  
> Seleccion: documento completo.

# 13 — Glosario y convenciones de lectura del set documental

- **Fecha:** 2026-07-18 · **✎ Actualizado 2026-08-06** (relevamiento integral: se
  corrigieron las reglas 1/3/5/6/7 y las entradas G1, D1 y ADR-NNN que habían quedado
  pre-ADR-015, y se agregaron las convenciones **AF-x**, **limitación L1–L8 vs hito
  L0/L1** y **las dos series de ADR**)
- **Propósito:** definir en un solo lugar toda la sigla y jerga del proyecto, y las
  reglas para leer este set **sin contexto previo** (pensado para humanos que se suman
  y para LLMs que reciben los documentos fragmentados, p. ej. en un Project de
  claude.ai). Si un término aparece en cualquier doc sin definición, se define acá.

---

## 1. Convenciones de lectura (las reglas de oro)

1. **El número del documento es su identidad** ("doc 04", "doc 56"). Las carpetas
   agrupan por rol: `nucleo/` narrativa, `decisiones/` ADRs, `specs/` serie 40,
   `operacion/` series 30 y 50–101, `informe/` serie 90, `contingencia/` serie 20.
   **✎ 2026-08-10 — `nucleo/` está partida por vigencia:** en la raíz lo actualizado a
   lo implementado (`10` + la serie de relevamientos por servicio **`14`–`19`**); en
   **`nucleo/historicos/`** los docs `01`–`09`, `11` y `12` (ninguno posterior al
   2026-07-13), **con su número intacto** — una cita "nucleo/04" sigue siendo válida,
   solo que el archivo vive un nivel más abajo.
   **✎ 2026-08-06 — excepción que muerde:** desde el 90 las series de `operacion/` y
   de `informe/` **colisionan** (existen `operacion/93` ≠ `informe/93`,
   `operacion/95` ≠ `informe/95`, `operacion/92` ≠ `informe/92`…). Al citar un doc
   ≥90, **decir siempre la serie**: "operacion/95" o "informe/95", nunca "doc 95" a
   secas.
2. **El banner ✎ manda sobre el cuerpo.** Muchos docs son la foto de su fecha y llevan
   arriba banners de actualización posteriores. Si un fragmento del cuerpo contradice
   un banner (o un doc más nuevo), **vale el banner / el doc más nuevo**. Nunca citar
   el cuerpo de un doc histórico como estado actual sin verificar su banner.
3. **Jerarquía de verdad para el estado actual de la plataforma** (✎ actualizada
   2026-08-06; *decía doc 56 > … > doc 92*): **`operacion/97`** (foto integral
   2026-08-05, reemplaza al 56) > banners ✎ > **los 4 índices de
   `e-ovrt_experimental-setup/results/`** (cifras verificadas mecánicamente con
   `operacion/datos/96-verificar-indices.py`) > cuerpo de docs de operación > specs
   (lo *pedido*, no necesariamente lo *construido*). `informe/92` y `operacion/56`
   quedaron **derogados como fuente de números** (2026-08-05).
4. **Docs de registro histórico** (no describen el presente): 32, 36, 50 (reemplazados
   en cadena por el 56), los cuerpos de 33–39 (sus resultados siguen válidos como
   evidencia de esa fecha), y **todo `nucleo/historicos/`** (✎ 2026-08-10; su
   `README.md` dice qué conserva vigencia de cada uno — dos casos especiales: `04` y
   `12` valen **por** no haberse actualizado, son el pre-registro de D1).
5. **Los ADRs no se re-litigan.** Una decisión formalizada (ADR-001…**016**) solo se
   revisa con causa registrada. Si un texto propone reabrir una, es un error.
   **✎ 2026-08-10 — el ejemplo de cómo se hace bien:** ADR-016 reabrió la distribución
   derogando **puntualmente** ADR-015 §2b/§2c/§6 con causa firmada y ratificando el
   resto — sucesión explícita, nunca enmienda tácita.
   ADR-015 además **cierra la puerta**: ninguna capacidad nueva hasta la defensa.
6. **Ninguna cifra sin artefacto.** Todo número citable tiene su `metrics.json` (o
   artefacto equivalente) referenciado desde los 4 índices de
   `e-ovrt_experimental-setup/results/`, o su archivo en `operacion/datos/`. Un
   número sin artefacto no va al informe. (✎ 2026-08-06: *decía "o su ruta en el doc
   92"* — derogado como fuente de números.)
7. **El estatuto del GT depende del material** (✎ actualizado 2026-08-06; *decía "el
   GT de video es preliminar"*): el GT del **banco del rodaje** (34 clips, 35
   episodios) es **humano y `gt_ready` desde 2026-08-03** — sus métricas se reportan
   como **RESULTADO** de la tesis. La regla vieja ("solo verificación de mecánica")
   aplica únicamente a material cuyo GT siga `gt_preliminary` — ~~hoy, el lote de
   internet (14 clips, en anotación CVAT)~~.
   > ✎ **2026-08-10 — ya NO queda material en `gt_preliminary`: la regla vieja no aplica a
   > nada.** El lote de internet terminó su pasada humana (**13 de 14 con GT**, `v08_c01`
   > excluido con causa firmada), así que **sus métricas también se reportan como
   > RESULTADO**. Banco total: **47 clips / 37 episodios**.
   > **Y trajo un resultado propio que hay que contar, no esconder:** la **revisión ciega**
   > del GT (doc 113 §B) encontró que **5 de las 7 declaraciones de episodio del lote eran
   > errores de anotación**, todas sobre-declarando donde el estado **no era observable**.
   > ⇒ **la calidad del GT es un resultado en sí**, el estrato B quedó con **2 episodios
   > evaluables**, y de un n así **no sale ningún ranking** (ver regla 9 y síntesis §5.1).
8. **Registro:** los docs de operación usan voseo informal a propósito (son memoria de
   trabajo). El informe se redacta en registro formal impersonal — el modelo de estilo
   es el doc 94.
9. **El informe vive en `.docx`/Google Docs.** Los `9x-*-texto-extraido*` son
   extracciones derivadas solo para búsqueda y cita; nunca se editan. La Etapa 3
   vigente es el doc 90 (la embebida en el docx v1.1 está desactualizada).

## 2. El proyecto en tres frases

**E-OVRT-VDP** (Experimental Open-Vocabulary Real-Time Video Detection Platform) es el
proyecto integrador (TFG, defensa ~fines de septiembre 2026) de una **plataforma
experimental** que detecta condiciones de riesgo en obras de construcción usando
**detección open-vocabulary (OVD)**: las condiciones se expresan en lenguaje natural
(prompts) en vez de entrenar un modelo cerrado. La tesis **no** es "OVD detecta
mejor": es que una plataforma con condiciones en lenguaje permite **medir qué se logra
sin entrenar** y extender el sistema a condiciones nuevas sin re-entrenamiento
(argumentos A1–A5, doc 09). La plataforma son dos servicios HTTP config-driven
(media-plane :8080, control-plane :8081) orquestados por un runner y una consola web.
✎ 2026-08-18 (ADR-019 + **ADR-020**): **tres** servicios HTTP config-driven — el módulo de
distribución de alertas también expone el suyo (`:8082`) y **el runner le habla por HTTP
por default**. ADR-020 derogó a ADR-018: el subproceso quedó como fallback operativo y
dejó de ser patrón de acople ⇒ la plataforma tiene **dos** patrones (HTTP config-driven en
los tres módulos, y bus ZeroMQ), no tres.

## 3. Siglas y términos del dominio

| Término | Definición |
|---|---|
| **OVD** | Open-Vocabulary Detection: detección de objetos guiada por texto (prompts), sin conjunto de clases fijo. |
| **CR-01 / CR-02** | Las dos **condiciones de riesgo** del núcleo validable: persona sin casco (CR-01, severidad alta) y persona sin chaleco (CR-02, severidad media). "CR" = condición de riesgo del catálogo de la §17.1.5. |
| **PR-01 / PR-02** | Los **patrones de riesgo** que operacionalizan CR-01/CR-02 con persistencia temporal. Umbrales oficiales de plataforma (Tabla D.4 / pattern set `cr01_cr02_v2`): confirmación a los **4000 ms** (CR-01) y **7000 ms** (CR-02); resolución 2000/3000 ms. |
| **DBE** | Dataset-Based Evaluation: escenario offline; el media-plane escribe `detections.jsonl` y el control-plane lo relee (replay). El archivo es la fuente de verdad. |
| **EBE** | Environment-Based Evaluation: escenario live; acople por bus ZeroMQ PUB/SUB (`bus.envelope.v1`, msgpack), corrida 1:1 (ADR-007), cierre por `run_finished`. Toda corrida live es re-evaluable offline con artefactos byte-idénticos. |
| **media-plane** | El plano de medios/inferencia: servicio FastAPI :8080, carga un modelo OVD al arranque (`EOVRT_MODEL_REF`), ingiere fuentes visuales y emite `media.detection.v1`. Repo `e-ovrt_media-plane`. |
| **control-plane** | El plano de control: servicio FastAPI :8081, motor de patrones con histéresis (`inactive→candidate→confirmed→resolved`) que consume detecciones y emite alertas. Repo `e-ovrt_control-plane`. |
| **experimental-setup** | Repo `e-ovrt_experimental-setup`: config experimental centralizada (ADR-009), runner reproducible que orquesta ambos planos por HTTP (ADR-004), consolidación de artefactos (ADR-014), reporte, y la **webconsole**. |
| **webconsole / BFF** | Consola web de gestión: frontend React (Vite :5173) + backend FastAPI :8090 que actúa de Backend-For-Frontend proxy de ambos planos. Superficie de gestión primaria (ADR-009). |
| **runner** | CLI del experimental-setup que dispara una corrida en ambos planos en el orden correcto: live ⇒ control primero (su 201 garantiza suscripción al bus), replay ⇒ media primero. |
| **G0 / G1 / (G2)** | Granularidades del patrón (ADR-002): **G0 = escena** (sin identidad de personas; el núcleo validable), **G1 = sujeto** (con tracker IoU como decorador en el control-plane). ✎ 2026-08-06: G1 es **capacidad operativa medida** — F1 0,930 sobre los 34 clips **del Bloque A** (el rodaje; ✎ 08-12: decía "del banco", y el banco es de 47 — 34 es el bloque), el mejor resultado, con detecciones bit a bit idénticas a G0 (adenda ADR-002 + ADR-015 E-03; *decía "solo demostrativa"*). Siguen excluidas las métricas MOT (E-10). |
| **G2A** | "Glass-to-algorithm": latencia captura→resultado algorítmico en el media-plane (`g2a_ms` por unidad; presupuesto 50–250 ms). Parte de la métrica `t_capture→alert` (spec 40 §5.2.4). |
| **t_alert** | Latencia de alerta del sistema: desde que la condición se sostiene hasta que el patrón confirma. Con umbral 4000 ms, el valor ideal medido fue 4000,0 ms exactos. |
| **TTFD** | Time To First Detection: ms desde el inicio del episodio GT hasta la primera detección de la evidencia correspondiente. |
| **SDR** | Sustained Detection Rate: fracción del episodio GT cubierta por detecciones (clamp 0–1). |
| **re_alerts** | Alertas repetidas de un mismo episodio (el motor emite en cada confirmación, ADR-011); el evaluador las cuenta aparte y **no** las penaliza como falsos positivos. |
| **Estados de aplicabilidad** | ADR-006/013: cuando una métrica no corresponde, se declara con causa en vez de omitirse: `not_applicable/non_temporal_source` (imágenes), `not_interpretable/dbe_media_time` (video DBE), `not_interpretable/cross_node_monotonic_clock` (two-node), `not_applicable/no_ground_truth`, etc. |
| **D1…D6** | Las seis dimensiones de decisión del doc 03 (estrategia de detección, granularidad, bus, config paraguas, distribución, reporte), formalizadas en ADR-001…006. |
| **E-IND / E-DIR / E-HYB** | Estrategias de detección de D1: **E-IND** = indirecta (detectar persona + EPP y razonar la ausencia — la adoptada como encuadre, ADR-001), **E-DIR** = directa (prompt que describe la infracción, variantes negación/observable), **E-HYB** = fusión de ambas (dual-run con gating por persona). El experimento del doc 04/12 las comparó. ✎ 2026-08-06: **D1 corrió en los dos niveles** (acta firmada 2026-07-29, doc 76; *decía "bloqueada por el acta `edir_v1`"*): E-IND queda como núcleo (F1 0,789), E-DIR **vetada por precisión** (0,146 < 0,5) y E-HYB-or refutada (F-87.2); `hyb_and` no ejecutada con causa (D-90.4). |
| **E-01…E-13** | El registro de **exclusiones** de alcance del doc 10 (qué NO se implementa y bajo qué regla del informe). E-07 es el nodo de borde: OAK-D quedó integrada y EN-2 implementada opcional. |
| **EN / CPN / TN** | Nodos del entorno experimental (§17.1.4): Edge Node (captura; OAK-D Pro PoE), Central Processing Node (GPU de inferencia), Training Node (fine-tuning — clúster Mendieta; **jornada experimental comprometida, ADR-017**, siempre aparte del núcleo zero-shot medido). |
| **EN-2** | Variante de borde con **inferencia parcial en el dispositivo**: prefilter de personas corriendo EN la OAK-D (blob `person-detection-retail-0013`), fail-open, default off. Medido: 87 % de drop on-device en A/B real. |
| **R1…R4** | Los cuatro resultados defendibles del plan (doc 02): plataforma E2E, números DBE, números EBE/latencia, extensibilidad. |
| **A1…A5** | Los cinco argumentos de defensa de OVD del doc 09 (con videos V1–V4). **No confundir con AF-x** (fila siguiente). |
| **AF-1…AF-11** | Las once **afirmaciones** de la escala de conclusiones transversales (`operacion/98` §2), cada una con su fuerza declarada (establecida / direccional / tendencia / no cerrada / limitación). Prefijo **AF** justamente para no colisionar con los argumentos A1–A5 del doc 09. |
| **L1…L8 (limitaciones)** | La lista canónica de **limitaciones declaradas** del trabajo, cerrada el 2026-08-05; la referencia es `e-ovrt_experimental-setup/results/index.md` §Limitaciones. **Colisión a evitar:** la **Fase L** del plan maestro (doc 62) usa `L0`/`L1` para sus *hitos* (L0 = ensayo pre-rodaje, L1 = el rodaje). Al citar, escribir **"limitación L1"** para la lista y **"hito L1" / "el rodaje"** para la fase — nunca `L1` a secas. |
| **ADR-NNN (dos series)** | Architecture Decision Record. Hay **dos series que se confunden**: **`ADR-001…018`** del proyecto (3 dígitos, en `docs/decisiones/`; los ADRs existentes **no se reescriben** —sólo se anotan con ✎ y fecha— pero la serie **sí crece**: 016, 017 y 018 se agregaron después del "cierre" del 2026-07-18 — ver README de la carpeta y su companion `estado-de-implementacion-adrs.md`) y **`ADR-0001…0013`** internos del control-plane (4 dígitos, en `e-ovrt_control-plane/docs/decisions/`; el 0005 no existe). Se solapan en tema con número distinto (p. ej. aplicabilidad = ADR-006 del proyecto vs ADR-0006 del control-plane). **Al citar, decir siempre la serie** ("ADR-0003 del control-plane"). |
| **DA-01…DA-13** | Las **decisiones arquitectónicas iniciales** del capítulo de diseño del informe (§17.3.3.4, tabla completa en el doc 90). Las que más citan los ADRs: **DA-01** separar plano de medios y plano de control; **DA-02** publicar la evidencia perceptiva como eventos normalizados; **DA-03** diferenciar el canal de eventos del repositorio persistente (⇒ el JSONL del plano es la fuente de verdad); **DA-10** priorizar DBE antes de EBE; **DA-13** registrar la alerta interna antes de cualquier notificación externa. |
| **specs serie 40** | Los specs de Etapa 4 por módulo: 40 plataforma (normativa transversal), 41 control-plane, 42 media-plane, 43 clip bench/GT temporal, 44 experimental-setup, 45 distribución MQTT (para lo último). Escritos sin alternativas a partir de los ADRs. |
| **superpowers** | Metodología de trabajo con specs/planes/revisiones que usó Claude para implementar; sus artefactos viven en `docs/superpowers/` o `docs/_archive/superpowers/` de cada repo de código. No confundir con este repo `docs/`. |

## 4. Identificadores y contratos (trazabilidad)

| Término | Definición |
|---|---|
| **`unit_id`** | Identidad de una unidad visual (frame) dentro de un run. **La clave canónica de correlación** entre planos (la vista correlacionada de la consola une detecciones, descartes, progreso y alertas por `unit_id`; keyear por `frame_index` colapsa con `image_folder`). |
| **`run_id`** | Corrida de un plano (`runs/<run_id>/` en cada repo). La corrida EBE es 1:1: un run de control por run de media (ADR-007). |
| **`experiment_id`** | Corrida paraguas del experimental-setup (ADR-004): agrupa los runs de ambos planos y consolida artefactos en `runs/<experiment_id>/` (ADR-014: lo liviano se copia, `detections.jsonl` se referencia). |
| **`source_id` / `clip_id`** | Identidad de la fuente. Convención del clip bench: **`source_id = clip_id`** — así el matching de escena del evaluador une alerta↔episodio GT. |
| **`track_id`** | Identidad de sujeto (opcional en `Detection` desde 07-13). ✎ **2026-08-10 — corregido: decía "nadie lo produce aún, el modo `subject` está inerte". FALSO desde el 2026-08-04.** El modo `subject` **funciona y es el mejor resultado del banco**: la campaña **G1** llega a F1 **0,930** contra 0,789 de escena **con las mismas detecciones bit a bit** (la ganancia es 100% del motor). El `track_id` se produce **post-hoc** con `SimpleIoUTracker`, y el camino config-driven (`input.track_persons`) lo reproduce exacto. Lo que sigue sin existir son **métricas MOT** (E-10, excluida por ADR-015) y el port al pipeline online (decisión abierta, doc 89 §7). |
| **`media.detection.v1`** | Evento de detección del media-plane (JSONL y bus). Evolución **aditiva** (se agregan campos opcionales, no se rompen — regla pedida por el tutor, doc 92). |
| **`bus.envelope.v1`** | Envelope ZeroMQ (topic + `seq` monótono + payload msgpack). Huecos de `seq` = `bus_dropped_events` (degradan, nunca se silencian). |
| **`control.alert.v1`** | Alerta confirmada publicada por el control-plane (persiste-primero). |
| **`control.pattern_progress.v1`** | Progreso parcial 0–1 de un patrón en estado `candidate` (observabilidad; no toca la máquina de estados). |
| **`media.dropped_unit.v1`** | Ledger por-frame de descartes del media-plane (`rate_gate`, `queue_full`, `staleness_timeout`, `channel_closed`). |
| **`clip_gt.v2`** | Contrato de ground truth temporal de un clip: episodios por condición con ventanas en ms, flag `negative`, `sub_threshold_events`, `provenance`. |

### 4.1 Códigos que se citan en todo el set (✎ agregado 2026-08-10)

Estos prefijos aparecen cientos de veces y **hasta hoy no estaban definidos en ninguna
parte**. Sin esta tabla, un lector que no estuvo no puede resolver "F-113.1" ni "D-90.4".

| Código | Qué es | Cómo se lee |
|---|---|---|
| **`F-NN.N`** | **Hallazgo** (*finding*) con mecanismo explicado | El número antes del punto es **el documento de `operacion/` donde nació**; el de después, el hallazgo dentro de ese doc. `F-87.2` = segundo hallazgo del doc 87. Excepciones históricas con letras: `F-EV1/2/3` (fixes del evaluador), `F-RT1/2` (realtime), `F-GT1` (ground truth), `F-G2.1` (ensayo G2) |
| **`D-NNN.N`** | **Decisión firmada**, con causa y fecha | Misma convención: `D-90.4` = cuarta decisión del doc 90; `D-113.1` = primera del doc 113. **No se re-litigan al redactar: se declaran con su justificación** |
| **`AF-1…AF-11`** | La **escala de conclusiones**: qué se afirma y **con qué fuerza** (establecida / direccional / tendencia / no cerrada) | Vive en síntesis §8 y `operacion/98`. **Es la tabla que hay que consultar antes de afirmar cualquier cosa en el informe** |
| **`L1…L8`** | Las **limitaciones canónicas**, lista cerrada | Referencia vigente: **`results/index.md` §Limitaciones** (la de `informe/99` §4.1 y la de la síntesis §9 pueden estar atrás). ⚠️ **Colisión: la Fase L del plan maestro usa `L0`/`L1` para sus hitos.** Escribir **"limitación L1"** vs **"hito L1"** |
| **`E-01…E-13`** | **Exclusiones de alcance** declaradas (`nucleo/10`) | Cada una con su justificación; ADR-015 las cerró |
| **`DA-01…DA-13`** | **Decisiones de arquitectura** del set (distintas de los ADR) | — |
| **`R-01…R-26`** | Los **redlines** del informe: "dice hoy / debe decir / evidencia" (`informe/93`) | ⚠️ **Colisión triple, la peor del set** — ver abajo |

**⚠️ Las tres colisiones de símbolos. Un externo las pisa sí o sí si no se las avisan:**

| Símbolo | Significado 1 | Significado 2 | Significado 3 |
|---|---|---|---|
| **`R…`** | **`R1–R4`** = los cuatro **resultados defendibles** (`nucleo/02`) | **`R1–R6`** = las seis **campañas de densidad** del clip bench | **`R-01…R-26`** = los **redlines** del informe (`informe/93`) |
| **`D1`** | **Dimensión de decisión 1** del tablero | **Campaña de Nivel A** `d1_gdinotiny560_edir_vs_eind` | **Campaña de Nivel B** con `edir_v1` |
| **`A1`** | **Primer argumento de defensa** (`nucleo/09`) | El **piloto de clase nueva** (`machinery`, doc 94) | El **gate A1** de censura de episodios cortos |

**Al redactar: nunca usar estos símbolos desnudos.** Escribir "la campaña R1", "el redline
R-13", "el argumento A1", "el piloto A1 de clase nueva".

### 4.2 IDs de campaña (✎ agregado 2026-08-10)

Las tablas de resultados usan estos IDs como filas, sin leyenda. Son **16 campañas con
artefacto**; cada una es **una combinación concreta**, y el contraste entre filas *es* el
experimento.

| ID | Qué varía respecto de la línea de base | Nivel |
|---|---|---|
| **T1** | Nada — es la **línea de base** (`gdino-tiny-560` + `v2_short` + escena) | B |
| **T2** | El **modelo** (`gdino-base-560`) | B |
| **D1** | Los **prompts** (`edir_v1`, evidencia directa de ausencia) | B (y hay un **D1 de Nivel A**, otro experimento) |
| **H1** | La **fusión** de estrategias (`hyb_or`) | B |
| **G1** | La **granularidad** (por sujeto en vez de por escena) — **la mejor del banco** | B |
| **B1** | El **vocabulario** (`bare_head` directo) | B |
| **R1–R6** | La **densidad de evidencia** (`stride` 7/15/26 × escena/sujeto) | B |
| **I1 / I2** | El **material**: estrato B (obra real no guionada), escena y sujeto | B |
| **NA1** | Nivel A **sobre video** (17 clips) | A |

### 4.3 Estrato A / estrato B — y el otro "estrato" (✎ agregado 2026-08-10)

- **Estrato A (Bloque A)** = los **34 clips del rodaje guionado** del 2026-07-25. Es donde
  vive el resultado principal.
- **Estrato B (Bloque B)** = los **13 clips del lote de internet**, obra real **no
  guionada**. Se reporta **como fila aparte, nunca fusionado al agregado del rodaje**
  (D-90.6).
- ⚠️ **No confundir con "estrato" del bench de IMÁGENES**, que son las tres fuentes de
  `bench_v3` (`bench_obra` / `chv` / `shel5k`). Misma palabra, materiales distintos.

## 5. Datos, modelos y bancos

| Término | Definición |
|---|---|
| **canonical_v2** | Vocabulario canónico de clases compartido entre repos: `person`, `helmet`, `vest`, `bare_head` (+ atributos `has_helmet`/`has_vest` solo en BENCH). Las vistas `*_cr01_cr02` están **eliminadas**. |
| **TRAIN / BENCH / DEMO** | Splits v2 de imágenes: 5540 / 196 / 1064. El BENCH de imágenes mide percepción (AP por clase, recall CR-01). ⚠️ ✎ **2026-08-10 — el "BENCH de 196" NO es el banco vigente y no se cita**: se auditó como **20–25% fuera de dominio** (selfies de COVID, PASCAL VOC, aeropuerto — doc 63) y se conserva solo como artefacto histórico. **El banco de imágenes vigente es `bench_v3`: 6.477 imágenes en 3 fuentes independientes** (`bench_obra` 147 curadas · `chv` 1.330 · `shel5k` 5.000), congelado el 2026-07-23. **Reportar siempre por estrato Y agregado, nunca solo el agregado** (el agregado está dominado por `shel5k`, 77%). |
| **clip bench** | El banco de **video** con GT temporal (`processed/clip_bench/`, spec 43). ✎ **2026-08-10 — corregido: decía "1 clip promovido (`cb_b01_p7`) en `gt_preliminary`". Doblemente falso**: ese clip fue **RETIRADO** el 2026-08-03 (licencia sin registrar + GT generado por IA) y **no debe citarse**. **Hoy el banco tiene 47 clips con GT HUMANO** = 32 positivos / 15 negativos / **37 episodios**, manifest `3f14f50a…`, en dos bloques: **A** = rodaje guionado (34) y **B** = lote de internet (13). Es el escenario EBE oficial del informe. |
| **video-gt-lab** | El pipeline semiautomático de GT temporal: `prepare_clip` → preanotación (GDINO-**base** anti-circularidad + ByteTrack) → CVAT (humano) → `derive_clip_gt` → `validate` → `promote_clip`. |
| **`gt_preliminary`** | Estado de un GT sin pasada humana (anotador `claude-vision-preliminary`). Ver regla de oro #7. |
| **GDINO / MM-GDINO / YOLOE** | Las tres familias de modelos OVD evaluadas. ✎ **2026-08-10 — cifra actualizada: el campeón es `gdino-tiny-560` con mAP50 0,551 sobre `bench_v3` (6.477 imgs)**, no el 0,441 del BENCH viejo. Licencias: GDINO y MM-GDINO **Apache-2.0**, YOLOE **AGPL-3.0** (registro en `license_registry.md` §PESOS DE MODELO). Hallazgos clave: **YOLOE es ciego a `bare_head`** (recall CR-01 ≈ 0); MM-GDINO-tiny descartado (bboxes rotas). Pista doble del núcleo (doc 12 §3): GDINO-tiny primaria + YOLOE-26s réplica. |
| **OAK-D Pro PoE** | Cámara edge con NPU (DepthAI). Fuente viva `oak_d` del media-plane; trae IP estática de fábrica 169.254.1.222. |
| **prompt set** | Conjunto versionado de prompts con ciclo de vida (`exploratory` → `frozen`, con `frozen_sha256`). ✎ **2026-08-10 — corregido: `eind_v1` y `edir_v1` están `frozen` con sha256 desde el 2026-07-29 (acta del usuario, doc 76). Ya no esperan nada.** Texto anterior: `eind_v1` está `frozen_pending_review` (espera el **acta** del usuario que desbloquea D1). |
| **pattern set** | Conjunto versionado de patrones del control-plane. El oficial es **`cr01_cr02_v2`** (escena, 4000/7000 ms, sin cooldown ni memoria de cobertura). |

## 6. Nombres de repos y puertos

| Cosa | Valor |
|---|---|
| Repos de código | `e-ovrt_media-plane`, `e-ovrt_control-plane`, `e-ovrt_experimental-setup`, `e-ovrt_datasets` (hermanos en disco; el acople cross-repo asume esa disposición) |
| Este repo | `docs/` — git local **sin remote** (decisión del usuario) |
| Puertos | media :8080 · control :8081 · BFF webconsole :8090 · frontend dev :5173 |
| Entry points | `uvicorn --factory eovrt_media.service.app:create_app` · `eovrt-control serve` |

---

## Fuente: `docs/informe/ajustes/08-manual-de-aplicacion.md`

> SHA-256 del bloque: `b47dd0c2590f290c2f394e3bad38f76f56cb0eb44314adcf9e0189f8a1640325`  
> Seleccion: documento completo.

# Manual de aplicación — cómo se pasan los 109 ajustes al informe

> **Qué es esto (2026-08-12).** El mapa (`00`) dice **qué** hay que cambiar. Los documentos
> `01`–`07` dicen **qué dice cada ajuste**. Este dice **cómo se aplica**: en qué superficie
> se edita, en qué orden, quién hace qué, y cuándo una sección se puede dar por cerrada.
>
> **Es el documento que se abre el día 1**, y el único de la carpeta que se actualiza a
> diario (el tablero del §5).
>
> **No repite ningún enunciado ni ninguna cifra.** El contenido vive en su ficha; acá vive
> el procedimiento y el estado.

**Punto de partida:** 91 ajustes (`AJ-` + `R-`) + 18 podas (`PODA-`) = **109 unidades de
trabajo. Cero aplicadas.** Los insumos están completos y verificados; lo que falta es el
pase.

---

## 1. El problema que hay que resolver antes de escribir la primera línea

Cuatro hechos que, juntos, son un conflicto de edición esperando:

1. **El entregable es el `.docx` / Google Docs.** El repo no lo edita: produce la
   instrucción y el texto, y la edición se hace en el documento (regla del `93`, ratificada
   en `gobierno/97` §161).
2. **`entregable/*.md` es una foto, no un espejo.** Se extrajo una vez y **no se regenera**:
   si alguien edita el Word, esos `.md` quedan viejos en silencio. **No existe script de
   extracción** — se verificó: no hay ninguna herramienta en el repo que lo haga.
3. **Ahora hay cuatro manos** (los dos colegas que redactan, el usuario y Claude), donde
   antes había una.
4. **Tres secciones no son corrección, son capítulos nuevos** (§17.4, §17.5, §17.6).

Sin resolver esto, el día 1 produce ediciones pisadas y el día 10 nadie sabe cuál es la
versión buena. Las tres decisiones del §2 lo resuelven.

---

## 2. Las tres decisiones previas — con recomendación

Formato del tablero de decisiones (`operacion/90`): opciones, recomendación, qué desbloquea.
**Son del usuario.** Lo que sigue está escrito asumiendo la recomendación; si cambia una,
cambia el §3 y el §4 de este documento y nada más.

> ✎ **2026-08-16 — las tres decisiones FIRMADAS por el usuario, tal como estaban
> recomendadas**: D-A híbrida · D-B reparto por juicio experimental · D-C re-extracción al
> cerrar cada sección (con extractor, la opción barata). Ajuste operativo firmado el mismo
> día: **la vara del §15 (`AJ-1.01`/`AJ-1.02`/`AJ-1.13`) la redacta Claude como borrador**
> —en `entregable/borradores/`, patrón "texto listo para copiar" del `94`— para desbloquear
> §17.5 sin esperar; los colegas la revisan e integran en Google Docs. El día 1 del pase es
> este: T1 full quedó encolado en Mendieta (job 1167640, `operacion/120`) y la redacción
> arranca mientras se espera ese resultado (`AJ-5.13` sigue ⏳).
> ✎ **2026-08-17: ese resultado llegó — veredicto NO-GO (`operacion/123`), `AJ-5.13`
> desbloqueado y redactable con cifras.**
>
> ✎ **2026-08-16 (tercera pasada) — D-A ratificada con el carril ChatGPT**: el maestro
> sigue siendo **Google Docs**; los `.docx` que produce el Project de ChatGPT son **por
> sección, sobre copia del base, y se descartan tras integrarse al maestro**. Las
> instrucciones consensuadas del Project y el knowledge de 4 archivos (2 del kit + el
> informe sin §17.3 + la Etapa 3 standalone): `operacion/122` §6-ter.

### D-A · Dónde se escribe cada cosa → **recomendada: híbrida**

| Opción | Qué implica |
|---|---|
| (a) Todo directo en Google Docs | Simple, pero los tres capítulos nuevos se escriben sin control de versiones, sin revisión por diff y sin poder verificar cifras contra el repo |
| (b) Todo en markdown y una transcripción final | Control total, pero obliga a transcribir ~60 correcciones puntuales que sería trivial hacer en el documento |
| **(c) Híbrida** ✅ | **Corrección donde ya hay texto; redacción en el repo donde no lo hay** |

**La recomendada, en concreto:**

- **Secciones que ya existen** (§11–§14, §15, §16, §17.1, §17.3, §18, §19) → **se editan
  directo en Google Docs**, con la ficha del ajuste al lado. Es lo que ya preveían el `93`
  y el `97`, y es lo correcto: son correcciones puntuales sobre prosa existente.
- **Secciones vacías** (§17.4, §17.5, §17.6) → **se escriben en markdown en el repo**, se
  revisan ahí, y se pegan **una sola vez** cuando la sección está cerrada. Es exactamente el
  patrón con el que se escribió el doc `94` ("texto listo para copiar"), que ya funcionó.

**Dónde viven esos borradores:** `informe/entregable/borradores/17-4.md`, `17-5.md`,
`17-6.md`. El nombre dice *borrador* a propósito, para que nunca se confundan con la foto
extraída (`90`, `96a`–`96e`), que es otra cosa.

### D-B · Quién hace qué → **recomendada: por juicio experimental requerido, no por volumen**

Los dos colegas no participaron del trabajo experimental. `GUIA-REDACTORES.md` los habilita
y está bien hecha, pero el riesgo no es parejo entre secciones:

| Sección | Juicio experimental que exige | Riesgo de un error |
|---|---|---|
| **§17.5** resultados | máximo: escala `AF-1…AF-11`, limitaciones `L1–L8`, las 6 trampas, cada cifra con combinación + material + `n` | **error de fondo en la defensa** |
| **§17.4** implementación | bajo: es descriptiva, y los insumos están verificados con ruta:línea (`92`, `operacion/97`) | recuperable |
| **§15 / §16 / §17.1** | bajo: corrección de prosa y literatura; ahí vive además el 100% de la poda | recuperable |

**Reparto recomendado:**

| Quién | Qué | Por qué |
|---|---|---|
| **Los dos colegas** | Etapa 1 (§15, §16) · Etapa 2 (§17.1) · Etapa 0 (§11–§14), **con la poda de cada sección en el mismo pase** | Es el 60% del volumen y el 100% de la poda, con el juicio experimental más bajo. Y arranca por `AJ-1.01`/`AJ-1.02`/`AJ-1.13`, que es **lo único que bloquea el camino crítico** |
| **Usuario + Claude** | **§17.5**, después §17.4 y §17.6/§18 | Son las que exigen la escala `AF` y las cifras |
| **Usuario** | Etapa 3 — las 26 redlines | Tienen casilla de decisión: son **decisiones de diseño**, no redacción |

> **Si aun así los colegas van a tocar §17.5:** que **no escriban ninguna cifra**. Escriben
> estructura y narrativa y dejan marcado `[[CIFRA: qué hace falta acá]]`; el relleno lo hace
> quien tiene el contexto, contra los índices. Es más lento, pero no arriesga el fondo.

### D-C · Cuándo se re-extrae la foto → **recomendada: al cerrar cada sección**

El `.md` extraído lo citan otros documentos del set. Si queda meses viejo, todo lo que lo
cita empieza a mentir sin avisar. **Regla:** una sección cerrada en Google Docs ⇒ se
re-extrae su `.md` y se anota la fecha en `entregable/00-el-informe-hoy.md`.

**Ojo:** hoy no hay herramienta para hacerlo. O se escribe un extractor una vez (una hora de
trabajo, y sirve para siempre), o se acepta la deriva y se declara en el banner de
`entregable/`. **La primera es la barata.**

---

## 3. El orden de trabajo, resuelto

El mapa (`00` §6) da el orden recomendado. Lo que le falta es la dependencia dura, y con
ella el orden queda cerrado.

**Hay una sola dependencia real entre etapas**, y está declarada en `05` (`AJ-5.11`): el
§17.5 escribe cada conclusión en **tres tiempos** —*qué dice la literatura* → *qué medimos*
→ *qué aporte queda*—, y la vara de la literatura la construyen `AJ-1.01`, `AJ-1.02` y
`AJ-1.13` en el §15. **Hoy esa vara no existe**, así que el §17.5 no tiene contra qué
contrastar.

⇒ **No se empieza por el §17.5. Se empieza por esos tres ajustes del §15**, que son 3 de 16
y desbloquean el camino crítico.

| # | Tramo | Quién | Desbloquea |
|---|---|---|---|
| **0** | `AJ-1.01` · `AJ-1.02` · `AJ-1.13` — **la vara del §15** | colegas *(✎ 2026-08-16: borrador de Claude; colegas revisan e integran)* | **§17.5** |
| 1 | **§17.5** — evaluación y validación | usuario + Claude | §17.6 · §18 |
| 2 | **§17.4** — implementación *(en paralelo con 1)* | usuario + Claude | — |
| 3 | **§17.3** — las 26 redlines, las 7 🔴 primero *(en paralelo)* | usuario | — |
| 4 | **Etapa 1 restante** + poda de §15/§16 *(en paralelo)* | colegas | — |
| 5 | **§17.6 · §18 · §19** | usuario + Claude | — |
| 6 | **Etapa 2** (§17.1) + **Etapa 0** + poda restante | colegas | — |

**Los tramos 1–4 son paralelos de verdad**: tocan secciones distintas del documento y no se
pisan. Eso es lo que hace que cuatro manos rindan cuatro manos.

---

## 4. El pase por sección — el loop repetible

Se hace igual para toda sección, sea corrección o redacción nueva.

1. **Abrir las tres fuentes de esa sección**: la ficha del ajuste (su doc de etapa), la poda
   que le toca (`07` §8) y el inventario de figuras y tablas que aterrizan ahí
   (`gobierno/99` §1).
2. **Leer los banners antes que los cuerpos.** Regla general del set: un documento con ✎ o
   ⚠️ **manda por el banner**, no por el cuerpo. Los cuerpos se conservan para trazabilidad.
3. **Aplicar `AJ-`/`R-` y `PODA-` en el mismo pase.** No dos pasadas: la poda cambia qué hay
   que corregir, y corregir algo que después se elimina es trabajo tirado.
4. **Cada cifra sale de `results/`**, nunca de una tabla-atajo. El formato de cita es
   **combinación + material + `n`** (`GUIA-REDACTORES` §3, con los pares ❌/✅).
5. **Cada afirmación se declara con su fuerza** según la escala `AF-1…AF-11`. No se decide
   al escribir: está pre-registrada.
6. **Chequeo de no-anacronismo.** Si escribiendo §15, §16, §17.1 o §17.3 aparece una cifra
   medida por el proyecto, **estás en la sección equivocada** — eso vive en §17.5/§18.
   Decisiones y correcciones de diseño sí van hacia atrás; resultados no.
7. **Cerrar**: marcar el estado en el tablero (§5); si te apartaste de lo que decía la
   ficha, anotarlo como ✎ **en la ficha**; y re-extraer el `.md` si la sección se editó en
   Google Docs (D-C).

> ✎ **2026-08-16 — regla de autocontención (fijada por el usuario).** El texto del
> informe **no referencia jamás la documentación local de desarrollo**: ni docs de
> `operacion/`, ni ADRs, ni specs, ni fichas `AJ-`/`R-`/`PODA-`, ni IDs internos
> (`F-`, `D-`, `T-FT-`), ni rutas del repo o índices de `results/`. Todo eso guía el
> pase pero es andamiaje local; la procedencia va en las notas `> ✎` de los borradores
> (que no se pegan) y en este tablero. Formulación completa y qué identificadores SÍ
> se usan: `GUIA-REDACTORES` §3.1.

---

## 5. Tablero de aplicación

**Esto es estado, no contenido.** El enunciado de cada ajuste vive en su documento de etapa
y no se copia acá. Etapa 3 conserva además sus casillas granulares
(`acepto`/`modifico`/`rechazo`) en `material-etapa-3/93`, que es donde se registra la
**decisión**; acá solo se registra que el pase se hizo.

Marcá `[x]` al cerrar. `⊘` = resuelto como "no se aplica", con la causa anotada en la ficha.

**Etapa 0 · §11–§14 — 7 · responsable: colegas** *(sus fichas viven en `00` §4, no en un doc propio)*
```
[ ] AJ-0.01   [ ] AJ-0.02   [ ] AJ-0.03   [ ] AJ-0.04   [ ] AJ-0.05   [ ] AJ-0.06
[ ] AJ-0.07
```

**Etapa 1 · §15 · §16 · Anexo A — 16 · responsable: colegas** *(la vara ★: borrador de Claude, ✎ 2026-08-16)*
```
[ ] AJ-1.01 ★  [ ] AJ-1.02 ★  [ ] AJ-1.03   [ ] AJ-1.04   [ ] AJ-1.05   [ ] AJ-1.06
[ ] AJ-1.07    [ ] AJ-1.08    [ ] AJ-1.09   [ ] AJ-1.10   [ ] AJ-1.11   [ ] AJ-1.12
[ ] AJ-1.13 ★  [ ] AJ-1.14    [ ] AJ-1.15   [ ] AJ-1.16
```
★ = **la vara**. Son el tramo 0 del §3: se hacen primero y solos.

**Etapa 2 · §17.1 · Anexos C y D — 12 · responsable: colegas**
```
[ ] AJ-2.01   [ ] AJ-2.02   [ ] AJ-2.03   [ ] AJ-2.04   [ ] AJ-2.05   [ ] AJ-2.06
[ ] AJ-2.07   [ ] AJ-2.08   [ ] AJ-2.09   [ ] AJ-2.10   [ ] AJ-2.11   [ ] AJ-2.12
```

**Etapa 3 · §17.3 — 26 · responsable: usuario** *(la decisión se registra en el `93`)*
```
[ ] R-01 🔴  [ ] R-02 🔴  [ ] R-03 🔴  [ ] R-04 🔴  [ ] R-05 🔴  [ ] R-06 🔴  [ ] R-07 🔴
[ ] R-08     [ ] R-09     [ ] R-10     [ ] R-11     [ ] R-12     [ ] R-13     [ ] R-14
[ ] R-15     [ ] R-16     [ ] R-17     [ ] R-18     [ ] R-19     [ ] R-20     [ ] R-21
[ ] R-22     [ ] R-23     [ ] R-24     [ ] R-25     [ ] R-26
```

**Etapa 4 · §17.4 *(redacción)* — 12 · responsable: usuario + Claude**
```
[ ] AJ-4.01   [ ] AJ-4.02   [ ] AJ-4.03   [ ] AJ-4.04   [ ] AJ-4.05   [ ] AJ-4.06
[ ] AJ-4.07   [ ] AJ-4.08   [ ] AJ-4.09   [ ] AJ-4.10   [ ] AJ-4.11   [ ] AJ-4.12
```

**Etapa 5 · §17.5 *(redacción)* — 13 · responsable: usuario + Claude**
```
[ ] AJ-5.01   [ ] AJ-5.02   [ ] AJ-5.03   [ ] AJ-5.04   [ ] AJ-5.05   [ ] AJ-5.06
[ ] AJ-5.07   [ ] AJ-5.08   [ ] AJ-5.09   [ ] AJ-5.10   [ ] AJ-5.11   [ ] AJ-5.12
[ ] AJ-5.13 ✅ DESBLOQUEADO 2026-08-17 — la jornada CERRÓ: veredicto NO-GO (`operacion/123`)
```

**Etapa 6 · §17.6 · §18 · §19 *(redacción)* — 5 · responsable: usuario + Claude**
```
[ ] AJ-6.01   [ ] AJ-6.02   [ ] AJ-6.03   [ ] AJ-6.04   [ ] AJ-6.05
```

**Poda · transversal — 18 · se aplica con el pase de su sección**
```
[ ] PODA-01  [ ] PODA-02  [ ] PODA-03  [ ] PODA-04  [ ] PODA-05  [ ] PODA-06
[ ] PODA-07  [ ] PODA-08  [ ] PODA-09  [ ] PODA-10  [ ] PODA-11  [ ] PODA-12
[ ] PODA-13  [ ] PODA-14  [ ] PODA-15  [ ] PODA-16  [ ] PODA-17  [ ] PODA-18
```

---

## 6. Lo único que falta producir: cinco figuras

El inventario de `gobierno/99` §1 tiene 23 materiales. **Las 17 tablas (`T-68`…`T-84`) están
en disco y se llenan copiando**, igual que `FIG-D`. Lo que falta son **cinco figuras**, y
son trabajo real que conviene hacer **antes** de escribir la sección que las contiene —un
capítulo escrito sin sus figuras se reescribe.

| Figura | Qué es | Estado | Va en |
|---|---|---|---|
| **FIG-A** | Arquitectura de los dos planos — vista de procesos | 📐 **especificada, no dibujada** (`94` §4) | §17.3.5 (R-09) · §17.4 |
| **FIG-B** | Calidad vs densidad (F1 escena y sujeto contra fps) | ⚙ generar desde `results/clip_bench/r{1..6}_*/metrics.json` | §17.5 |
| **FIG-C** | Frame con overlay de alerta confirmada | ⚙ generar con el renderer de `experimental-setup/defensa/` | §17.5 |
| **FIG-E** | Máquina de estados del motor (`open → confirmed → resolved`) | ⚙ generar desde el contrato `pattern_events` | §17.4 |
| **FIG-F** | Frontera de juzgabilidad de 3 ejes (escala × iluminación × oclusión) | ⚙ generar | §17.5 |

**FIG-A es la más urgente de las cinco**: es la respuesta gráfica al *"cómo está hecho"* del
tutor técnico, ya está especificada caja por caja, y la piden dos secciones distintas.

---

## 7. Las cuatro puertas antes de dar una sección por cerrada

| Puerta | Qué se verifica | Cómo |
|---|---|---|
| **P1 · Cifras** | Toda cifra de la sección rastrea a un índice de `results/` | `python3 docs/operacion/datos/96-verificar-indices.py` en verde |
| **P2 · NO-TOCAR** | No se "corrigió" nada de la lista de falsos errores | `00` §7 — el que más muerde son las **ecuaciones de Word que la extracción no captura** y parecen campos vacíos |
| **P3 · Trampas** | Las seis de `GUIA-REDACTORES` §4 | banco **47** (no 34) · FAR se mide pero no sostiene cota · no rankear el estrato B · L4 **precisada**, no levantada · nada del bench de 196 ni de `cb_b01_p7` · fine-tuning **nunca** "por tiempo" (ADR-017) |
| **P4 · Figuras** | Las figuras de la sección **existen**, no están prometidas | §6 de este documento |

---

## 8. Lo que NO bloquea escribir

Por decisión de secuenciación del usuario (2026-08-10, `GUIA-CIERRE`), estos van en **carril
paralelo** y no detienen la redacción:

- **C1 — URL y fecha de acceso de los 18 `clip.yaml`** del lote de internet. Es procedencia
  de las citas del estrato B: **vuelve a ser bloqueante antes de cerrar la versión final**,
  no antes de escribir. Paso a paso en `operacion/113` §C1.
- **E — el video de defensa V2.** Material de defensa, no del informe.

---

## 9. Fuentes

`00-mapa-de-ajustes.md` (§0 correspondencia etapa→sección, §6 orden, §7 NO-TOCAR) ·
`01`…`07` (las fichas) · `material-etapa-3/93` (casillas de Etapa 3) ·
`gobierno/99` §1 (inventario de figuras y tablas, verificado contra disco el 2026-08-12) ·
`gobierno/97` §161 y `gobierno/98` §154 (el `.docx` no se edita desde el repo) ·
`entregable/00-el-informe-hoy.md` (la foto no es espejo) ·
`../../GUIA-REDACTORES.md` (§3 cómo citar, §4 las siete trampas) ·
`../../GUIA-CIERRE.md` (secuenciación del 2026-08-10) · `05` `AJ-5.11` (la única dependencia
entre etapas).

---

## Fuente: `docs/sintesis/resultados-y-conclusiones.md`

> SHA-256 del bloque: `e1395434638bebdce569173bdc726a328f827b2c6b70d5533e192f4754372020`  
> Seleccion: documento completo.

# Síntesis de resultados y conclusiones — E-OVRT-VDP

> ## ✎ ESTADO AL 2026-08-09 — el cuerpo está AL DÍA
>
> Este documento se escribió el **08-06**, cuando el estrato B eran **3 clips**. El
> tramo de video **se cerró** desde entonces: lote **13/14 con GT** (banco **47**, doc
> `operacion/111`), campañas **re-corridas en gen. 3**, balance con lectura crítica
> (`operacion/112`) y revisión de ese balance (`operacion/113`, que ejecutó las
> correcciones documentales y lista lo que falta).
>
> **✎ 08-09, noche — el estrato B ya está INTEGRADO AL CUERPO**, no solo a este banner:
> **§4.1** (Nivel A sobre video) y **§5.1** (Nivel B sobre obra real no guionada y la
> frontera de juzgabilidad) son secciones nuevas con las cifras vigentes. Este banner
> queda como resumen de qué cambió y por qué; **ya no hay que leer el cuerpo "con la
> fecha del 08-06 en mente"**.
>
> **Cifras vigentes del estrato B (tras la revisión CIEGA del GT, doc 113 §B, 08-09
> noche):** Nivel B `scene` F1 **0,333** / `subject` **0,190** sobre **2 episodios
> evaluables**; Nivel A sobre 17 clips de video CR-01 **0,031** / CR-02 **0,018**; y
> **FAR/hora computable por primera vez** — 29,2 y 1.850,8, que son **3 y 190 FP en
> 6:09,6 del único clip soak**. La asimetría de FP entre granularidades es lo robusto:
> 26 vs 323 sobre 11 negativos (12×).
>
> **El resultado más fuerte de la revisión ciega: 5 de las 7 declaraciones de episodio
> que produjo el lote eran errores de anotación (~71%)** — v06_c01, v03_c02, v04_c02×2
> y v01_c01, TODAS sobre-declarando violación donde el estado no era observable (cabina
> de máquina, contraluz, borde del plano). Es la frontera de juzgabilidad medida
> también en el anotador, y convierte la calidad del GT en un resultado auditado: los
> 2 episodios que sobreviven están verificados a ciegas con evidencia de frame.
>
> **Cuatro cosas del cuerpo que ya no son ciertas:** (1) `v06_c01` **sí es negativo** —su
> episodio CR-02 era error de anotación (doc 108 §6)— y es **el clip soak del banco**,
> así que **L1 se precisa** en vez de quedar igual; (2) su escenario **P5 era correcto**,
> el error estaba en la anotación y no en la curación — y lo mismo terminó valiendo para
> `v04_c02` y `v01_c01`; (3) "ninguna lectura de cuál gana es válida" **sigue siendo
> cierto**, hoy con más fuerza: `n` = **2 episodios** — F-111.1 quedó enmendado; (4)
> `v04_c02` ya NO es "el único caso limpio del estrato": sus 2 episodios eran error y el
> clip es negativo (banner del doc 108).
>
> **§4.1, §5.1 y §11 son posteriores a la revisión ciega y mandan sobre cualquier cifra
> de estrato B anterior al 08-09.** El resto del cuerpo (imágenes, rodaje, tiempo real)
> no se vio afectado por la revisión: esas mediciones son del Bloque A y no cambiaron.

- **Fecha:** 2026-08-06 · **Estado del proyecto:** tramo experimental **COMPLETO**
  sobre el banco del rodaje; ✎ mismo día, más tarde: **llegaron las anotaciones CVAT
  del lote de internet, el GT del estrato B se derivó y promovió (banco 34→37, doc
  `operacion/102`), y las dos campañas I1/I2 CORRIERON.** El resultado no es una fila
  más: `v06_c01` (127 personas GT, el clip más denso del banco) rompió el mecanismo de
  las dos formas que la teoría del rodaje predecía en miniatura — `scene` recall
  0,000 (F-81.2(a) llevado al extremo: evidencia perpetua por multitud) vs `subject`
  recall 1,000 pero precision 0,010 (el tracker fragmenta identidades en escenas
  densas: 182 identidades con FP, más que las 127 personas reales). Detalle completo
  y por qué ninguna lectura de "cuál gana" es válida con n=1 clip así: `operacion/103`.
  **Mismo día, después:** los ajustes probados solo con configuración (`operacion/104`
  — el gate `min_subject_area_px` YA EXISTÍA en 400 px², recalibrado FP −32% con recall
  intacto; `base-560` REFUTADO, no transfiere a sujetos chicos) y la recuperación de
  los 4 clips piloto desde CVAT con **Nivel A sobre video** (`operacion/105` — el
  derrumbe confirmado con la métrica canónica; la juzgabilidad tiene TRES ejes: escala ×
  iluminación × oclusión; y la brecha humano/modelo es el contexto temporal, F-105.4).
  *(✎ las cifras de Nivel A sobre video de ese doc —CR-02 F1 0,154 piloto / 0,002
  estrato B— son de la gen. 2 y quedaron **supersedidas**; las vigentes, re-puntuadas
  el 08-09 sobre los 17 clips, son **CR-01 0,031 / CR-02 0,018** contra 0,408/0,479 en
  imágenes: `results/bench_nivel_a/`.)*
  **✎ 08-07/09:** artefactos reorganizados con fuente única (`operacion/109`),
  `v03_c02` integrado tras corrección a `unknown` (`operacion/110`) y **el lote de
  internet CERRADO: 13 de 14 con GT, banco 47 clips** (`operacion/111` — `v08_c01`
  excluido con causa; anotaciones del repo = fuente de verdad, guard `--check`).
  **✎ 08-09: las campañas gen. 3 CORRIERON** sobre los 13 clips, y después vino la
  **revisión ciega del GT** (`operacion/113` §B) que tiró 3 de los 5 episodios del
  estrato y obligó a re-derivar y re-evaluar. El banco quedó en **47 clips = 32
  positivos / 15 negativos / 37 episodios** (manifest `3f14f50a…`) y las cifras
  vigentes del estrato B son las del banner de arriba — **ninguna cifra de estrato B
  anterior al 08-09 sigue en pie**.
- **Qué es:** el "pasado en limpio" de todo lo medido y concluido, con el camino
  experimental que respalda cada número. Nace del **relevamiento integral de
  consistencia del 2026-08-06** (5 auditorías paralelas sobre conclusiones, redlines,
  kit de informe, alcance/ADRs e índices de resultados; los desfases encontrados se
  corrigieron en sus docs — ver §10).
- **Qué NO es:** una fuente primaria. **Ante cualquier conflicto mandan los 4 índices
  de `e-ovrt_experimental-setup/results/`** (verificados mecánicamente con
  `docs/operacion/datos/96-verificar-indices.py` — última corrida 2026-08-06, todo
  verde) y los docs de procedencia. Toda cifra de esta página fue relevada contra esos
  índices en la fecha de arriba.

---

## 1. La pregunta del trabajo, y la respuesta en una línea

> *¿Qué rendimiento se obtiene hoy, en construcción civil, con detección
> open-vocabulary **sin entrenar**, expresando las condiciones de riesgo en lenguaje —
> y qué aporta la plataforma alrededor del modelo?*

**Respuesta corta (doc `operacion/98` §1):** la detección zero-shot alcanza para
sostener una condición de riesgo (CR-01, sin casco) y no alcanza para la otra (CR-02,
sin chaleco), pero **la plataforma alrededor del modelo cambia el resultado más que
cualquier elección de modelo o de prompt** — y esa ganancia sobrevive a la restricción
del tiempo real.

**La cifra que lo condensa:** sobre el mismo banco, con **las mismas detecciones bit a
bit**, cambiar la granularidad del motor de escena a sujeto lleva el F1 de alertas de
**0,789 a 0,930**. Ninguna de las cuatro palancas de percepción o formulación probadas
(modelo, prompts, fusión, vocabulario nativo) se acercó.

**Marco de lectura (doc 81 §1, no negociable):** cada número es el rendimiento medido
de UNA combinación, no una nota de aprobación. El contraste entre filas ES el
experimento.

## 2. El recorrido del argumento, en cuatro números

1. **Qué ve el detector sin entrenar** — `gdino-tiny-560`, mAP50 **0,551** sobre 6.477
   imágenes de 3 fuentes independientes (robusto a la fuente). → §3
2. **Cómo conviene expresar la condición** — E-IND (evidencia positiva + inferencia)
   gana a E-DIR (prompts de ausencia) en los dos niveles; a Nivel B el **veto
   pre-registrado de precisión (0,146 < 0,5)** descarta a E-DIR como núcleo. → §4–5
3. **Qué agrega la plataforma sobre la detección cruda** — la histéresis rescata
   percepción intermitente (CR-02 recall 1,000 con SDR 0,281) y **la capa que más
   agrega es la identidad**: F1 0,789 → **0,930** con detecciones idénticas. → §5
4. **Qué sobrevive al tiempo real** — la ganancia de la identidad **excluye el cero en
   las cuatro densidades medidas** (bajo decimado regular; conserva la dirección bajo
   el descarte irregular medido del live, 6/6 — doc 101). → §6

## 3. Percepción sobre imágenes — selección de modelos y extensibilidad

**Banco:** `bench_v3`, congelado 2026-07-23 — **6.477 imágenes / 55.165 anotaciones,
3 estratos independientes**: `bench_obra` (147, núcleo curado y spot-checkeado), `chv`
(1.330, mejor AP de `vest`), `shel5k` (5.000, `bare_head` nativo). El agregado está
dominado por `shel5k` (77%) ⇒ **reportar siempre por estrato** (limitación L5). El
BENCH original de 196 imgs quedó como histórico (~20–25% fuera de dominio, doc 63).
Freeze verificable por sha256 (`4557024e…`).

**Camino experimental:** Fase S del plan maestro (doc 62) — S1/S2 sobre el núcleo
curado (docs 61/64) + confirmación B5 sobre `bench_v3` completo (doc 66).

| Modelo | mAP50 `bench_v3` (6.477) | mAP50 `bench_obra` (147) | recall CR-01 (n=5.313) |
|---|---|---|---|
| **`gdino-tiny-560`** (campeón) | **0,551** | **0,503** | 0,308 |
| `gdino-base-560` (especialista) | 0,525 | 0,474 | **0,599** |
| `yoloe-26x` | 0,442 | 0,405 | 0,000 |

- **Campeón `gdino-tiny-560`**: gana mAP50 en las dos escalas — robusto a la fuente.
  La resolución 560 da −24% de latencia batch con igual o mejor mAP que 800 (doc 61;
  no es medición live).
- **`gdino-base-560` es el especialista en dos ejes**: `bare_head` (evidencia de
  CR-01: recall 0,599 vs 0,308) y `vest`/CR-02 (AP 0,582 vs 0,520; en video, SDR
  CR-02 0,281→0,920). Candidato secundario cuando el foco sea esa condición.
- **La asimetría es estructural**: `person`/`helmet` sólidas (0,70–0,89 por estrato),
  `vest` débil (0,55–0,58), `bare_head` fuerte solo en el especialista (0,399 vs
  0,133 en `shel5k`). YOLOE es rápida (43 ms) pero ciega a `bare_head` (AP 0,000 en
  las cuatro variantes) ⇒ inservible para CR-01.

**Extensibilidad — el costo de una clase nueva, medido (A1, doc 94 → AF-4):**
**0 entrenamientos · 1 archivo de 48 líneas · 9 minutos · 0 GT nuevo anotado**, y
`machinery` (jamás configurada) da **AP@0.5 0,662 zero-shot** (n=99 cajas) — por
encima del agregado del campeón con las clases configuradas. **Contrapeso obligatorio
F-94.1:** la palabra tiene que alinear con la taxonomía (`vehicle` junto a `machinery`
= 0 detecciones; `gloves` = 252 detecciones y ninguna sobre un guante) — agregar la
clase cuesta minutos **y validar la palabra también** (el bench lo expone en ~3 min).

## 4. Nivel A — el estado "sin EPP" por persona (E-DIR vs E-IND)

**Camino experimental:** campaña D1 `d1_gdinotiny560_edir_vs_eind` (doc 83), con
prompt sets congelados por acta del usuario (2026-07-29, doc 76, sha256), umbrales
calibrados en mitad A y métricas solo sobre mitad B (anti-leakage), matching IoU≥0,5.

| Corte | E-IND F1 | mejor E-DIR | ratio E-DIR/E-IND |
|---|---|---|---|
| CR-01 `shel5k` (n+=2.487) | **0,546** | 0,188 (`obs`) | 0,34 (IC no solapados) |
| CR-01 `bench_obra` (n+=28) | **0,408** | 0,189 (`spec`) | 0,46 |
| CR-02 `bench_obra` (n+=82) | **0,479** | 0,418 (`obs`) | 0,87 |

- El **gate pre-registrado** (`nucleo/04` §8) exigía ambas condiciones <50% y **no se
  disparó** (0,87 en chaleco) ⇒ E-DIR pasó a Fase 2 (Nivel B), donde la decidió el
  veto de precisión (§5).
- **F-83.6 — E-DIR no es detector, es recuperador:** con F1 0,188 y 8.212 FP igual
  recupera el **18,5%** de lo que E-IND no ve (155/840 en `shel5k`). Su costo es
  precision, no recall.
- **F-83.4/83.5:** la formulación mueve el rendimiento y el eje ganador cambia con la
  condición; la negación sintáctica pura es siempre la más débil.
- **F-83.7 (versión corregida 2026-08-04):** la corroboración discrimina **en CR-01**
  (2,4×; réplica con `base-560`: 3,0×). En CR-02 no hay evidencia concluyente.
- **Limitación L8:** CR-02 a Nivel A **no está cerrado** (un solo estrato, n+=82, IC
  solapados). Declarado, no disimulado.

### 4.1 El mismo Nivel A, sobre VIDEO — el derrumbe, y de qué está hecho

**Camino experimental:** campaña `na1_gdinotiny560_v2short_video` (docs 105/111),
**17 clips** (13 del lote de internet + 4 del piloto), re-puntuada el 2026-08-09 tras la
revisión ciega del GT. Es la MISMA métrica de arriba —estado por persona, sin motor
temporal— aplicada a obra real en movimiento.

| Condición | Precision | Recall | **F1** | vs imágenes (`bench_obra`) |
|---|---|---|---|---|
| CR-01 (n+ = 92 de 10.356 person-frames) | 0,016 | 0,467 | **0,031** | 0,408 |
| CR-02 (n+ = 170 de 10.361 person-frames) | 0,009 | 0,318 | **0,018** | 0,479 |

- **El derrumbe es de PRECISION, no de recall.** El recall se sostiene en un rango
  reconocible (0,47 / 0,32); lo que se hunde es la precisión, dos órdenes de magnitud.
  El sistema **sigue viendo** lo que tiene que ver: lo que no puede es dejar de afirmar
  sobre personas cuyo estado no es determinable.
- **Regla declarada del scorer (D-113.2):** las person-frames que el anotador marcó
  `unknown` **salen del denominador** (1.414 y 1.409 excluidas), pero la predicción del
  modelo sobre esa persona **sí cuenta como FP** — "la alerta suena igual". Es una
  decisión firmada, no un artefacto: inflar el denominador con lo no juzgable sería
  premiar al sistema por acertar donde nadie puede verificar.
- **Mecanismo, no anécdota:** esto es la **frontera de juzgabilidad** (§5.1) medida sin
  motor temporal — el mismo fenómeno que a Nivel B, aislado de la histéresis y de la
  identidad. Por eso las dos capas se leen juntas.

## 5. Nivel B — alertas contra GT temporal humano (el resultado principal)

**Banco:** 34 clips del rodaje (2026-07-25), **35 episodios (28 CR-01 / 7 CR-02), 34
evaluables** (1 censurado con causa — denominador citable: **"34 evaluables sobre
35"**). GT **humano en CVAT, `gt_ready` desde 2026-08-03** (doc 80) ⇒ estas métricas
se reportan como **RESULTADO** de la tesis. Escenarios P1–P9; los 4 clips negativos
quedan fuera de P/R/F1 y son el **control de falsas alarmas** (F-EV1).

**Camino experimental:** GT (doc 80) → línea de base y fixes del evaluador (doc 81) →
campañas de combinación T2/D1/H1/B1/G1 (docs 84/85/87/88/89) → cierre (doc 92) →
conclusiones (doc 98). Seis campañas, mismo banco/GT/motor, variable única por fila:

| # | Combinación | Recall | Prec. | **F1** | t_alert | SDR | FP neg |
|---|---|---|---|---|---|---|---|
| **T1** | tiny-560 + `v2_short` + escena (**núcleo E-IND**) | 0,824 | 0,757 | **0,789** | 5.327 ms | 0,698 | 0/4 |
| T2 | base-560 (contraste de modelo) | 0,735 | 0,676 | 0,704 | 4.899 ms | 0,819 | 0/4 |
| D1 | `edir_v1` (E-DIR de punta a punta) | 0,176 | **0,146** | 0,160 | 6.611 ms | 0,210 | 2/4 |
| H1 | fusión `hyb_or` | 0,353 | 0,255 | 0,296 | 6.956 ms | 0,738 | 2/4 |
| **G1** | T1 + granularidad **por sujeto** | **0,971** | **0,892** | **0,930** | 5.236 ms | 0,698 | 0/4 |
| B1 | base-560 + `bare_head` directo | 0,382 | 0,371 | 0,377 | 3.919 ms | 0,940 | 3/4 |

**Veredicto del eje D1 (pre-registrado en `nucleo/04` §8):** E-IND **0,789 = núcleo**
· E-DIR 0,160, **descartada por veto de precisión (0,146 < 0,5)** · E-HYB-or 0,296,
**predicción refutada** (el recall se derrumba 0,824→0,353; **F-87.2**: la unión de
evidencia NO es monótona en un motor temporal — evidencia más temprana corre las
alertas fuera de su ventana) · **`hyb_and` no ejecutada con causa** (D-90.4: no
medible contra este banco sin romper la comparabilidad de las 6 campañas). Las tres
fallas están **explicadas por mecanismo**, no solo cuantificadas. La brecha E-DIR se
**agranda** al pasar por la plataforma (ratio 0,20 a Nivel B vs 0,34–0,46 a Nivel A).

**Los dos aportes medidos de la plataforma:**

- **La histéresis rescata percepción intermitente (F-81.1):** en T1, CR-02 confirma
  **7/7 = recall 1,000 con SDR 0,281** (evidencia en ~1 de cada 6 frames), pagando
  t_alert (8.572 vs 4.314 ms de CR-01). Es palanca de doble filo (F-85.3: en D1
  también amplifica los FP) y tiene límite de cadencia (F-96.2, §6).
- **La identidad es la capa que más agrega (F-89.1/89.2):** G1 usa **las mismas
  detecciones bit a bit** que T1 (SDR y TTFD idénticos) ⇒ los **+0,141 de F1 vienen
  100% del motor**, cero de percepción. P7 pasa de 0,400 a 1,000; prematuras de
  pre-roll 5→1. Corre sin GPU (0,4 min) y el camino config-driven la reproduce exacto.
  Por eso E-10 (métricas MOT) sigue "no aplicable" con fundamento **medido**: la
  ganancia se expresa en alertas, no en MOTA/IDF1.

Sobre el sub-banco CR-01 puro (23 clips / 25 episodios): T1 0,731 · T2 0,615 ·
B1-eind 0,582 · B1 `bare_head` directo 0,480 (**F-88.2**: la vía del vocabulario
nativo tampoco alcanza, sobre las mismas detecciones) · D1 0,231. **F-88.1**: una
clase más en el caption cuesta 0,082 de F1 (costo medido del caption). **F-88.3**: lo
que ordena el eje es la formulación (etiqueta corta > frase negada), no el mecanismo.

### 5.1 Estrato B — obra real NO guionada, y la frontera de juzgabilidad

Todo lo de arriba es el **rodaje guionado**. El lote de internet es el contraste que
faltaba: **13 clips de obra real** (uno de 14 excluido con causa), GT humano, la misma
combinación intacta — la única variable es el material. Se reporta como **fila aparte,
nunca fusionado al agregado del rodaje** (D-90.6). Banco resultante: **47 clips = 32
positivos / 15 negativos / 37 episodios**.

**Antes de las cifras, el resultado que las condiciona.** Una **revisión ciega** de los
episodios del estrato (doc 113 §B) encontró que **5 de las 7 declaraciones de episodio
que el lote produjo eran errores de anotación** (~71%), **todas sobre-declarando donde
el estado no era observable**: el ex "caso limpio" `v04_c02` tenía a su único sujeto
dentro de la cabina de una máquina, y `v01_c01` estaba a contraluz. **La calidad del GT
es acá un resultado en sí, no un detalle de método**: la misma frontera que derrota al
modelo derrota al anotador humano. Quedan **2 episodios evaluables**.

| | I1 `scene` | I2 `subject` |
|---|---|---|
| recall (2 episodios) | 0,500 | **1,000** |
| precision | **0,250** | 0,105 |
| **F1** | **0,333** | 0,190 |
| FP sobre los 11 negativos | **26** | **323** |

- **La ganancia de la identidad NO se reproduce en este régimen.** G1 fue la mejor
  combinación del banco del rodaje (+0,141 de F1); acá `subject` compra el episodio que
  `scene` pierde (recall 0,500 → 1,000) pagando **un orden de magnitud más FP**: ~6× en
  positivos y **12× en los negativos** (323 vs 26). **F-108.1: no hay una granularidad
  mejor, hay una correcta para cada régimen de densidad.** El mecanismo es el de L6 —
  el tracker fragmenta identidades en escena densa (182 identidades con FP contra 127
  personas reales en `v06_c01`).
- **Con n = 2, ningún ranking por F1 sale de acá** (F-111.1, enmendado). Lo robusto es
  la **asimetría de FP**, que son conteos grandes y sobrevivió intacta a la corrección
  del GT. Quien cite "0,333 le gana a 0,190" está leyendo ruido.
- **Falsas alarmas, dicho con el denominador a la vista:** el clip soak `v06_c01`
  (6:09,6 de obra real donde nadie infringe) da **3 FP en `scene` y 190 en `subject`**.
  Las tasas derivadas (29,2 y 1.850,8 FA/hora) **se reportan pero no sostienen una
  cota** — 0,1027 h están a dos órdenes de magnitud de las 3 h que exigiría afirmarla
  (**limitación L1, precisada**). Ninguna configuración probada cruza a operable
  (doc 107).
- **Qué queda entonces, y es lo valioso:** la limitación **L4 se precisó, no se
  levantó** (D-113.1). Hay medición en obra real, y su aporte es **caracterizar por
  mecanismo dónde el sistema deja de ser evaluable** — tres ejes medidos (**escala ×
  iluminación × oclusión**) y una propiedad negativa verificada: **el `unknown` del
  anotador no predice la juzgabilidad** (F-105.2/3/4). No existe un índice escalar
  barato para saber de antemano si el material es juzgable. Eso es un aporte
  metodológico, no un número de rendimiento.

## 6. Tiempo real — qué sobrevive a la restricción del camino live

**Camino experimental:** rodaje EBE (docs 71/73) → diagnóstico del techo (docs 73/74)
→ eje de densidad R1–R6 (doc 96) → blindaje y verificación adversarial (doc 101).

- **Integridad del acople (cerrada):** paridad replay↔stream **byte-idéntica**;
  6 corridas del rodaje con `bus_dropped_events = 0`; corrida 1:1 (ADR-007).
- **Densidad de evidencia (R1–R6, doc 96):** el banco corre a 30 fps de evidencia; el
  live entrega 1,16–4,42 fps. A densidad del techo live (≈4,29 fps): escena 0,794,
  sujeto 0,866. Al peor caso (≈1,15): escena 0,646, sujeto 0,742. **F-96.4 (el
  central): la ganancia de la identidad excluye el cero en las CUATRO densidades**
  (+0,141 / +0,072 / +0,137 / +0,096, bootstrap pareado por clip) — única palanca del
  banco significativa bajo esa restricción. Los deltas del agregado **de escena** no
  excluyen el cero; bajo sujeto el peor caso sí (R6−G1 = −0,188 [−0,334, −0,040]).
  "G1 a 4,29 fps > T1 a 30 fps" es **estimación puntual** (IC [−0,071, +0,229]), se
  reporta como consistente, no como hallazgo.
- **Trampas de instrumento (cazadas antes de reportar):** el **SDR no se compara
  entre cadencias** (F-96.6, ~100% artefacto) y el **t_alert agregado no se compara
  entre densidades sin control de supervivencia** (F-96.5: el costo real entre
  supervivientes es +0,7 a +1,3 s sobre políticas de 4–7 s).
- **Blindaje EBE (doc 101 — EBE CERRADO SIN PENDIENTES, no se re-rueda):** el
  descarte live irregular quedó **medido** (CV 0,22 hoy / 0,36 rodaje) y el eje de
  densidad **verificado por decimado empírico** (12/12 IC jitter−regular cruzan el
  cero; la identidad conserva el signo en 6/6 realizaciones). La claqueta cerró con
  hardware real y reloj externo: política 4.142 ms vs umbral 4.000, residuo de
  relojes 4 ms, **ancla física tono→fotón +1.066 ms**.
- **Latencia (con la advertencia obligatoria F-101.8):** G2A single-host p50
  **14,7 ms** / p95 31,8 (dentro del presupuesto 50–250 ms); live sobre OAK-D:
  GDINO tiny-560 p95 630–890 ms (fuera), YOLOE 225–249 ms (dentro **pero inservible
  para la condición** — F-RT2). **F-101.8: el G2A se mide desde el dequeue, no desde
  el fotón** — vidrio→alerta suma `capture_to_host` (202–217 ms en el rodaje; hasta
  1,6 s degradado), y el informe debe decirlo. `base-560` no tiene latencia live
  medida (declarado).
- **Techo de fps y su causa:** el techo es **contención de GIL** (F-RT3), no térmico
  (la hipótesis térmica del rodaje fue refutada por doc 73: lo que separa las
  poblaciones es la fuente). Palanca aplicada F-RT5: sacar el round-trip PIL del
  productor = **3,75→4,42 fps (+18%), −14,4% latencia, p=0,0195** (rama
  `perf/producer-pil-roundtrip`, merge = decisión del usuario). Prefilter EN-2
  on-device: **87% de descarte** medido A/B, opcional, default off.
- **Patrones en vivo (rodaje + smoke doc 91):** CR-01 7 confirmaciones legítimas
  (4,1–4,6 s sobre umbral de 4,0), CR-02 3 (7,1 s+ sobre 7,0); G1 verificado en vivo
  (`subject_key` por sujeto, 0 dropped). F-RT1: la sobre-marca de `vest` puede
  suprimir CR-02 en silencio (vestuario a franjas).

## 7. El estado del arte como vara — qué dice el informe, qué dice la literatura, y dónde quedan nuestros números (PRELIMINAR)

> **Estatuto de esta sección (2026-08-06):** relevamiento del §15 del informe +
> verificación independiente contra fuentes externas (web, fuentes primarias
> fetcheadas) + contraste con nuestros números actuales. Es **preliminar en los dos
> extremos**: el §15 del informe todavía se va a corregir en el pase de redlines, y
> nuestro agregado puede moverse cuando entre el estrato B (lote de internet). Las
> cifras nuestras salen de `results/`; las externas llevan marca de confianza:
> **[P]** = verificada en fuente primaria, **[S]** = fuente secundaria oficial,
> **[R]** = circulante sin verificar en esta pasada.

### 7.1 Lo que el informe desarrolló (preliminarmente) — y qué le encontró la verificación

El §15 del informe (`informe/96c`) trae un estado del arte OVD extenso: 4 paradigmas
(DETR/DINO con fusión profunda · one-stage YOLO · dual-encoder CLIP-like ·
generativos), ~25 modelos con cifras COCO/LVIS, la Tabla 3 de "OVD para tiempo real"
y la Tabla A.1 de prototipado (`informe/96e`). Los criterios de selección
(§17.1.9.2) fundan el par GDINO+YOLOE como "polos del trade-off expresividad
semántica ↔ latencia de inferencia", con reglas pre-registradas (baseline zero-shot
obligatoria, test congelado, ganancia exigible).

**La verificación externa confirma las cifras ancla** (GDINO 52,5 AP COCO zero-shot
y 26,1 mean AP ODinW [P]; YOLO-World-L 35,4 AP LVIS @ 52 FPS [P]; YOLOE-v8-S/L
27,9/35,9 AP LVIS @ 305,8/102,5 FPS T4-TensorRT [P/S]; GDINO 1.5 Pro 54,3/55,7 y
Edge 36,2 @ 75,2 FPS [S]) — **pero encontró dos huecos estructurales y una lista de
erratas** que el pase de redlines debe atacar:

- **Hueco 1 — no hay línea base de EPP supervisado.** El informe **no reporta ni una
  cifra de mAP** de la literatura de detección de EPP con modelos entrenados
  (SHEL5K/CHV/SH17 se citan solo como datasets). Sin eso, el lector no tiene contra
  qué leer nuestro 0,551 — y toda la defensa pivotea sobre ese contraste.
- **Hueco 2 — el estado del arte y la evidencia propia no se cruzan nunca.** El dato
  más contundente del proyecto (YOLOE con 35,9 AP en LVIS publicado pero **recall
  CR-01 = 0,000** medido acá) no está escrito en §15; ídem el trade-off de latencia,
  que §17.1.9.2 justifica con GPUs ajenas cuando ya existe medido en nuestro hardware
  (G2A live 630–890 ms GDINO vs 225–249 ms YOLOE; keep-up 22% vs 63–69% en Sprint 2).
- **Erratas duras a corregir** (verificables contra los papers): el 52,5 AP de GDINO
  **es del backbone Swin-L y el informe nunca lo declara** — lo desplegado acá es
  Swin-T, cuyo zero-shot COCO publicado es ≈48,4 [S]; OmDet-Turbo-Tiny "30,3 LVIS"
  (probable mislabel de ODinW-13) y 34,0 vs 34,7 entre tablas; LLMDet "51,1–52,4"
  con el 52,4 sin origen; el caching "ahorra ≈40 ms" en un modelo al que la misma
  tabla asigna 7,1 ms totales; la columna Latencia de la Tabla 3 es 1000/FPS
  (derivada, no medida); el 53,4 COCO de OmDet-Turbo probablemente no es zero-shot;
  citas inconsistentes (Liu 2023/2024, Minderer, Xiao, Lin 2014/2015, Ren a/b/c);
  y la Tabla A.1 lista GDINO 1.5/DINO-X como "Apache-2.0" cuando son **API cerrada
  sin pesos abiertos** (la licencia es del SDK, no del modelo) [S].
- Además, MM-Grounding-DINO —que el proyecto evaluó y descartó empíricamente— no
  tiene ninguna cifra de benchmark en el informe (publicadas: tiny 50,4–50,6 COCO
  zero-shot / 35,7–41,4 LVIS [P/S]).

### 7.2 El estado del arte verificado — las tres varas que importan

**⚠ Advertencia de métrica antes de comparar nada:** las cifras COCO/LVIS de los
papers OVD son **AP promediado sobre IoU 0,50:0,95** (LVIS además con protocolo
Fixed AP); los papers de EPP y nuestro bench reportan **mAP@0,5**, que da
numéricamente más alto para el mismo detector. **Nunca poner las dos series en la
misma columna.** El error previsible del jurado: "GDINO da 48–52 en COCO y ustedes
0,55 — rinde igual". No: en mAP@0,5 sobre COCO estaría muy por encima; nuestra caída
es real y es el costo de dominio.

**Vara 1 — el techo supervisado in-domain (mAP@0,5)** [P/S]:

| Dataset (paper) | Mejor modelo entrenado | mAP@0,5 | Dato fino |
|---|---|---|---|
| SHEL5K (Otgonbold 2022, Sensors) | YOLOR | **0,883** | `head` (cabeza sin casco) **0,907** — supervisada NO es difícil |
| CHV (Wang 2021, Sensors) | YOLOv5x | **0,866** | 6 clases (person, vest, 4 colores de casco) |
| SH17 (2024; 17 clases, industrial) | YOLOv9-e | **≈0,71** | YOLOv8 n→x: 0,58–0,69 — con vocabulario grande el techo baja |

**Vara 2 — OVD fuera de dominio (lo publicado):** GDINO-L cae a **26,1 mean AP**
(0,5:0,95) sobre los 35 datasets de ODinW [P] — la referencia de "cuánto colapsa un
OVD fuera de su distribución".

**Vara 3 — el cruce OVD×EPP (casi vacío, y eso es el hueco que ocupamos):**
- **OWLv2 zero-shot sobre obra** (Choi & Greer 2024, arXiv:2410.12225): AP@IoU>0,5
  **0,649 para hardhat** y **0,677 para person** sobre 5.210 imágenes [P] — la única
  cifra publicada directamente comparable con nuestro AP@0,5 por clase.
- **VLMs grounding con atributo/negación** (Chen 2025, arXiv:2508.11011): "workers
  wearing white hard hats" → **IoU <20%** [P] — la literatura confirma nuestra
  "ceguera al atributo" de E-DIR.
- **No existe paper 2023–2026 con GDINO/YOLO-World zero-shot medido sobre
  SHEL5K/CHV** ni sobre un bench de EPP multi-fuente con protocolo COCO — `bench_v3`
  está esencialmente solo en ese cruce.

### 7.3 Nuestros números contra esas varas — ¿tienen sentido?

**Sí: caen exactamente en la banda que la literatura predice, y en dos puntos quedan
por encima del único comparable directo.** Todo en mAP@0,5 / AP@0,5:

| Qué | Nuestro (zero-shot, preliminar) | Vara externa | Lectura |
|---|---|---|---|
| Agregado 3 fuentes | **0,551** (`gdino-tiny-560`, n=6.477) | techo supervisado in-domain 0,86–0,88 | **≈63% del techo sin entrenar** — la banda esperable; lejos del colapso tipo ODinW |
| `person` | 0,77–0,86 por estrato | OWLv2 zero-shot 0,677 | **por encima** del único zero-shot publicado |
| `helmet` | 0,71–0,89 por estrato | OWLv2 hardhat 0,649 | **por encima**, mismo orden de métrica |
| `vest` | ~0,55 | **sin cifra zero-shot publicada** | dato genuinamente nuevo; su brecha vs ~0,87 supervisado es coherente (menor presencia léxica en el preentrenamiento) |
| `bare_head` | 0,13 (tiny) / 0,40 (base) | **0,907 supervisado** (SHEL5K) | **LA historia**: la clase no es difícil — el zero-shot léxico-conceptual sí (lo respaldan el propio paper de GDINO en clases raras y el <20% de Chen 2025). Es el fundamento externo de AF-5 y de F-88.3 |
| YOLOE-26x | 0,442 agregado, `bare_head` 0,000, recall CR-01 0,000 | YOLOE26-L **36,8 AP LVIS** publicado (serie récord en su benchmark) | **los benchmarks generales no predicen la condición de dominio** — el argumento medido de por qué la selección se hizo sobre bench propio y no sobre LVIS |
| A1 `machinery` | 0,662 zero-shot jamás configurada | — | consistente con que GDINO rinde mejor en objetos "gruesos" y frecuentes que en atributos finos |
| Nivel B (F1 0,789 escena / 0,930 sujeto) | — | **sin vara externa**: la literatura no publica F1 de alertas contra GT temporal humano en obra | no se puede rankear afuera — se sostiene por mecanismo + IC internos, y es parte de la contribución (la capa que la literatura no mide) |

**Tres frases para la defensa que salen de esta sección:** (1) *"zero-shot logramos
~63% del techo que la literatura reporta entrenando en el dominio — y medimos
exactamente dónde se pierde el resto: en las clases léxico-conceptualmente débiles"*;
(2) *"en las clases comparables quedamos por encima del único zero-shot publicado
sobre obra (OWLv2)"*; (3) *"el cruce que nuestro bench mide —OVD zero-shot,
multi-fuente, protocolo COCO, sobre EPP— no existe publicado: no hay tabla de la
cual copiarse, por eso construimos la nuestra"*.

### 7.4 Orientación de las conclusiones: qué aporta cada una frente al estado del arte

La dirección para la redacción (fijada 2026-08-06): **cada conclusión se presenta
posicionada contra la literatura**, de modo que el aporte de la tesis quede leído
como *nueva perspectiva y adaptación de estos modelos*. La palabra "adaptación" hay
que usarla con precisión ante el jurado: **el núcleo medido NO adapta los pesos** —
adapta los modelos **operativamente**: resolución (560), formulación del vocabulario
(prompt sets congelados), y las capas de plataforma alrededor (histéresis temporal,
identidad por sujeto, política de alerta). Medir cuánto rinde ese "stack de
adaptación sin entrenar" ES la perspectiva nueva. El fine-tuning (E-04) es una
**rama experimental aparte, comprometida como jornada** (✎ 2026-08-11, ADR-017):
sus resultados, si existen a la entrega, se rotulan como rama comparativa y no se
funden con el núcleo zero-shot.

| Conclusión / resultado | Frente al estado del arte | Tipo de aporte |
|---|---|---|
| AF-3 — campeón `tiny-560` sobre `bench_v3` | El cruce "OVD zero-shot, multi-fuente, protocolo COCO, sobre EPP" **no existe publicado** (§7.2); la selección por benchmark propio en vez de LVIS quedó justificada por el caso YOLOE (35,9 AP LVIS → recall CR-01 0,000) | **Hueco ocupado** + dato metodológico (los benchmarks generales no predicen la condición de dominio) |
| Resolución 560 (−24% latencia, igual mAP) | La literatura OVD reporta a resolución de paper; el ajuste de resolución como palanca dominio-específica no está caracterizado para EPP | **Adaptación operativa medida** (sin tocar pesos) |
| AF-5 — especialización por clase (`base-560` en `bare_head`/`vest`) | No hay cifras zero-shot publicadas por clase de EPP; `vest` ~0,55 es la **primera cifra zero-shot de chaleco** y `bare_head` 0,13–0,40 vs 0,907 supervisado **cuantifica la brecha léxico-conceptual** | **Dato nuevo** |
| AF-2 — E-DIR vetada (0,146 < 0,5) + mecanismo (ceguera al atributo, 54% FP) | La literatura VLM reporta el fenómeno cualitativamente (grounding con atributo <20% IoU, Chen 2025; comportamiento bag-of-words de encoders contrastivos) | **Confirmación cuantificada con veto pre-registrado**, y elevada de percepción a **nivel sistema** (Nivel B) |
| F-83.6 — E-DIR como recuperador (18,5%) | No reportado en la literatura del cruce | **Dato nuevo** (matiza la conclusión anterior) |
| AF-9 — E-HYB-or refutada (F-87.2: la unión no es monótona en un motor temporal) | La literatura de fusión/ensambles es frame-level, donde unir evidencia solo puede subir recall; **nadie mide fusión a nivel de alerta temporal** | **Perspectiva nueva** — un resultado imposible de ver sin la capa temporal |
| AF-6/AF-7 — la histéresis rescata (recall 1,000 con SDR 0,281) y su límite de cadencia | Los papers de EPP miden mAP por frame; **qué agrega una capa temporal sobre percepción intermitente no está benchmarkeado** | **Perspectiva nueva** — el aporte de plataforma que la métrica estándar no captura |
| AF-1 — identidad: 0,789→0,930 con detecciones idénticas, sobrevive a las 4 densidades | La literatura MOT mide la identidad **como fin** (MOTA/IDF1, GT de identidades); acá se mide **como medio** para atribución de alertas, con la percepción controlada bit a bit | **Perspectiva nueva** — la contribución central; agnóstica al detector |
| AF-4 — extensibilidad medida (48 líneas, 9 min, AP 0,662) + F-94.1 | El argumento clásico pro-OVD ("agregar clases es barato") se **afirma** en la literatura pero no se **mide** como costo marginal end-to-end; F-94.1 agrega el contrapeso (validar la palabra es parte del costo) | **Dato nuevo** — el argumento A1 con número y con su letra chica |
| AF-8/AF-10/AF-11 + L1–L8 | Los trabajos aplicados rara vez declaran qué NO pueden afirmar | **Aporte metodológico** — la escala de fuerza y las limitaciones codificadas |

Regla de redacción que sale de esta tabla: en el informe, cada conclusión se escribe
en tres tiempos — *qué dice la literatura* (con la cifra de §7.2) → *qué medimos
nosotros* (con la cifra de `results/`) → *qué tipo de aporte queda* (columna 3).
Nunca al revés (empezar por el número propio sin vara es lo que hoy le pasa al §15).

**Pendiente que esta sección deja planteado (para el pase de redlines del informe):**
incorporar la Vara 1 con cifras al §15 (o declarar la ausencia como brecha),
declarar el backbone de cada cifra de GDINO, corregir las erratas de 7.1, cruzar la
Tabla 3 con la evidencia propia (YOLOE 0,000; G2A medidos), y corregir el uso de
Abdalwhab 2025 (compara YOLO11 fine-tuned vs OVD zero-shot en componentes MEP — es
evidencia de brecha de vocabulario zero-shot, no del efecto de ajustar OVD).

**Fuentes externas de esta sección** (verificadas 2026-08-06): Grounding DINO
arXiv:2303.05499 · MM-GDINO arXiv:2401.02361 · YOLO-World arXiv:2401.17270 (CVPR'24)
· YOLOE arXiv:2503.07465 (ICCV'25) + docs Ultralytics YOLOE26 · GDINO 1.5
arXiv:2405.10300 · DINO-X arXiv:2411.14347 · SHEL5K Sensors 22(6):2315 · CHV Sensors
21(10):3478 · SH17 arXiv:2407.04590 · OWLv2-hardhat arXiv:2410.12225 ·
ConstructionSite 10k arXiv:2508.11011.

## 8. La escala de conclusiones — qué se afirma y con qué fuerza (doc 98 §2)

**No todo lo medido tiene el mismo estatuto, y decirlo es más fuerte que aplanarlo.**
Regla aplicada: si la estimación puntual era vistosa pero el IC no excluía el cero,
**se degradó la afirmación** (caso testigo: la cruzada G1@4,29 > T1@30).

| # | Afirmación | Respaldo | Fuerza |
|---|---|---|---|
| AF-1 | La granularidad por sujeto mejora el F1 de alertas | ΔF1 +0,141 [+0,032, +0,258]; excluye el cero en las 4 densidades (bajo decimado regular; dirección conservada bajo descarte irregular, 6/6 — doc 101) | **Establecida** |
| AF-2 | E-DIR no sirve como núcleo | Veto pre-registrado de precisión (0,146 < 0,5); brecha F1 0,63; mecanismo: ceguera al atributo (54% de los FP) | **Establecida** (criterio fijado antes de correr) |
| AF-3 | `gdino-tiny-560` es el campeón | mAP50 1º en las dos escalas (147 y 6.477 imgs, 3 fuentes) | **Establecida** (robusta a la fuente) |
| AF-4 | Agregar una condición nueva no cuesta entrenar | 0 entrenamientos, 48 líneas, 9 min, `machinery` AP 0,662 zero-shot (+ contrapeso F-94.1) | **Establecida** (medida, no afirmada) |
| AF-5 | `gdino-base-560` es el especialista (en `bare_head`/CR-01 y en `vest`/CR-02) | recall CR-01 0,599 vs 0,308 (n=5.313); vest AP 0,582 vs 0,520; CR-02 SDR 0,281→0,920 | **Establecida** |
| AF-6 | La histéresis temporal rescata percepción intermitente | CR-02 recall 1,000 con SDR 0,281, pagando t_alert | **Establecida**, con límite (AF-7) |
| AF-7 | Ese rescate tiene un límite de cadencia | P2 cae 1,00 → 0,60 → 0,20 al bajar la densidad | **Establecida direccionalmente** (n=5 episodios) |
| AF-8 | El costo del tiempo real sobre el agregado | Estimaciones puntuales +0,005 / −0,050 / −0,143, decrecientes; ningún IC del agregado de escena excluye el cero | **Tendencia con mecanismo**, no efecto establecido |
| AF-9 | La fusión E-HYB-or no ayuda | Predicción pre-registrada refutada (recall 0,824→0,353), mecanismo F-87.2; `hyb_and` no ejecutada con causa (D-90.4) | **Establecida** (refutación de predicción propia) |
| AF-10 | CR-02 a Nivel A | Un solo estrato (n+=82), IC solapados | **No cerrada** — declarado (L8) |
| AF-11 | FAR/hora | Ninguna cota alcanzable sostiene afirmación (harían falta 3 h anotadas; el banco llega a 0,1027 h de soak sobre 0,2725 h negativas) | **Limitación L1, precisada — no derogada** (✎ 08-09): la métrica **se computa y se reporta** (29,2 escena / 1.850,8 sujeto), pero no sostiene una cota. Citar como **"3 y 190 FP en 6:09,6 del único clip soak"**, con la tasa horaria como derivada. La evidencia principal de FP sigue siendo el control de negativos |

*(La escala usa prefijo **AF** para no confundirse con los argumentos de defensa
A1–A5 de `nucleo/09` — convención en el glosario, doc 13.)*

## 9. Alcance, limitaciones y reglas de lectura

**ADR-015 (aceptado 2026-08-05) — cierre de alcance:** la premisa del "recorte" se
invirtió: **el alcance CRECIÓ con evidencia** — E-03 (G1 de demostrativa a capacidad
operativa medida en 34/34), E-07 parcial (OAK-D + EN-2 87%), E-13 (E-HYB-or ejecutada
y refutada). Desbloqueó R-13 y R-21. Sus cláusulas de puerta cerrada fueron derogadas
después por dos ADRs firmados: ✎ **ADR-016 (2026-08-10)** — la **distribución de
alertas** se reabre con el recorte exacto de ADR-005 y queda **funcionalmente
implementada y verificada** (seis criterios de spec 45; quedan webconsole,
orquestación y primer commit; E-06 sigue excluida) — y ✎ **ADR-017 (2026-08-11)** — el **fine-tuning
(E-04)** pasa de "no ejercida por secuenciación" a **jornada experimental
comprometida** (escalera T1→T2/T3 con go/no-go y Mendieta). ✎ **Adenda 2026-08-13:**
F-100.1 quedó resuelta por `finetuning_v1`; `1166583` cerró freeze/smoke técnico con 12
tensores/3.096 parámetros y optimizer 12/12, y dual gate/serving real están verdes. El full
sigue en NO-GO por ~~contrato de serving D-FT-08/T-FT-005,~~ evaluación T-FT-031 y baseline
26s T-FT-032. La procedencia T-FT-023 quedó CERRADA el 2026-08-13 (snapshot tar
`639e60df…`). ✎ **2026-08-15: el contrato de serving quedó firmado** (D-FT-08, junto con
D-FT-12 y D-FT-13) **y T-FT-031/T-FT-032 cerraron la misma jornada** — baseline YOLOE-26s
one-shot ejecutada y evaluada (doc 120: `bare_head` AP50 0,000, recall CR-01 agregado
0,0002; cifras de la rama comparativa, nunca fundidas con el núcleo). El NO-GO quedó en su
último eslabón: `full-authorization.json` + `RUN` manual del usuario. La
rama permanece condicionada **por datos y protocolo**, nunca por tiempo; la proyección Slurm
2026-08-18 es coyuntural y no una promesa.
✎ **2026-08-15 (noche): ese último eslabón se cerró — T-FT-043 CERRADA.** La autorización
se emitió y verificó en el clúster (7 gates) y el `RUN` quedó **encolado (job `1167640`)**.
Ya no queda tarea previa pendiente; lo abierto es **la corrida y su evaluación**. Enviar no
es medir: **no existe cifra del modelo ajustado** y la subsección correspondiente se
redacta reservada.
✎ **2026-08-17: la jornada CERRÓ — veredicto D-FT-12 = NO-GO**
(`operacion/123` (fuente: `docs/operacion/123-cierre-jornada-t1-no-go.md`)). **La cifra ya existe y la
subsección deja de ir reservada**: `bare_head` AP50 **0,0000 → 0,0455**, recall CR-01
**0,0002 → 0,2089**, `vest` 0,2642 → **0,3292**, contra `person` 0,7843 → 0,6932 y mAP50
0,4193 → 0,4171. Falla el gain gate por **0,0045** y la retención por `person`
(**−11,62 %**, tope 10 %). Checkpoint **no adoptado**. Márgenes firmados antes de la
baseline ⇒ **negativo pre-registrado: es resultado, no fracaso**. Rama comparativa: **no se
funde con el núcleo zero-shot ni va a `results/`**, y no se compara con el doc 64.
Ambos frentes se declaran con su **estado a la entrega**
y no bloquean el informe. Todo lo demás sigue cerrado (EN-3, E-10, E-06, CR nuevas).

**Limitaciones canónicas L1–L8** (lista cerrada 2026-08-05; referencia =
`results/index.md`; citar como "limitación Lx"): L1 FAR/hora se reporta pero no
sostiene una cota operativa · L2 sin
doble anotación ni kappa (decisión declarada) · L3 bordes adjudicados en 6 clips ·
L4 medición de obra real acotada que caracteriza la frontera de juzgabilidad, sin
validar el sistema en obra real · L5 escenarios desbalanceados ⇒ reportar por
estrato/escenario · L6 tracker medido en multitud, con fragmentación y costo de FP.
**Sigue en pie: no hay métricas MOT (E-10) y el `track_id` es post-hoc.** · L7 licencia parcial de `chv` ·
L8 CR-02 a Nivel A no cerrada.

**Reglas de lectura no negociables** (familia F-EV, doc 81 §3): reportar por estrato
y escenario, nunca solo agregado · clips negativos fuera de P/R/F1 (su métrica son
los FP) · `re_alerts` ≠ FP (ADR-011) · SDR no comparable entre cadencias · t_alert no
comparable entre densidades sin control de supervivencia · métricas que no aplican
con estado `not_applicable:<causa>` (ADR-006/013).

## 10. Qué encontró y corrigió el relevamiento del 2026-08-06

El relevamiento verificó que **ningún número de los índices está inventado** (todas
las tablas coinciden con sus `metrics.json` y artefactos de bootstrap) y que la
escala AF, los 26 redlines y las cifras canónicas del brief son consistentes.
Los desfases corregidos fueron de **propagación y redacción**, no de datos:

- **ADR-015 aplicado a medias al doc 10** (lo más serio): el ítem 5 (MQTT) seguía
  "dentro del alcance" y las frases de declaración de E-03/E-04/E-06/E-10/E-13 —las
  que van literales al informe— tenían el texto pre-ADR-015. Corregido, junto con
  `estado-de-implementacion-adrs` (filas 001/002/005) y el glosario (doc 13).
- **Derogaciones sin banner**: `operacion/92` no avisaba que ya no es fuente de
  números (el 56 sí lo hacía). Banner agregado; `operacion/98` §8 y `informe/93/95`
  ahora remiten a `results/`.
- **Calificadores obligatorios ausentes en el doc rector de conclusiones**: AF-1 sin
  el "bajo decimado regular" (doc 101 §3) y el G2A sin la advertencia F-101.8.
  Agregados.
- **Índices de `results/`**: el denominador "34 de 35" no estaba escrito; faltaban las
  filas B1/G1/H1 en los desgloses (regla L5); un hallazgo retractado seguía vigente
  (F-83.7/CR-02); "ningún delta excluye el cero" sin el scope de escena (R6−G1 sí
  excluye); la etiqueta "especialista CR-02/`bare_head`" mezclaba los ejes; el soak
  se leía como si habilitara FAR/hora. Todo corregido.
- **Navegación**: doc 101 y ADR-015 no estaban en `00-indice.md`; `GUIA-CIERRE.md`
  describía el proyecto de hace 12 días; el glosario no tenía las convenciones AF-x,
  "limitación L vs hito L" ni las dos series de ADR (hallazgo 6 de `informe/99`,
  **cerrado** con esto). Actualizado.

## 11. Lo que queda (a la espera del equipo) — y qué NO cambia

| Pendiente | Quién | Qué habilita |
|---|---|---|
| ~~**CVAT del lote de internet**~~ ✎ **HECHO 2026-08-06 (doc `operacion/102`)**: llegaron 3 (`v04_c01`, `v06_c01`, `v10_c01`), GT humano derivado/validado/promovido — banco 34→37, **L4 parcialmente levantada** (n = 2 episodios ⇒ fila aparte, D-90.6). Ojo: la trampa del runbook NO aplicó — estos exports eran **task-level** (`split_cvat_project.py` habría sido el error simétrico; mirar `meta/task` vs `meta/project`). Dos escenarios corregidos contra el GT (`v04_c01` P8→P1, `v06_c01` P5→P2); `v06_c01` **no salió negativo** ⇒ sigue sin haber soak y **L1 no se mueve**. Los 11 restantes: marginales (doc 93). **✎ 2026-08-09 — CERRADO y con dos correcciones al registro de arriba** (docs `operacion/108` §6 y `111`): el lote quedó en **13 de 14 con GT** (banco **47**; `v08_c01` excluido con causa firmada), y de los dos escenarios que el GT parecía desmentir **solo `v04_c01` estaba mal** — el **P5 de `v06_c01` era correcto**: su episodio CR-02 era **error de anotación**, así que el clip **es negativo y es el único clip soak del banco** ⇒ **L1 sí se movió** (FAR/hora pasó a computable, aunque insuficiente para sostener una cota). Los "11 restantes" se anotaron salvo uno. Fuente de verdad del GT = las anotaciones versionadas del repo, no CVAT | ~~equipo~~ | — |
| ~~Runs/evals del estrato B~~ ✎ **HECHO 2026-08-06**: I1/I2 corrieron. **El resultado no cierra el banco con un número — abre un hallazgo nuevo** (doc `operacion/103`): en `v06_c01` (127 personas GT) `scene` recall 0,000 (F-81.2(a) extremo) y `subject` recall 1,000 / precision 0,010 (182 identidades del tracker con FP, más que las 127 reales). **Decisión pendiente del equipo:** si esto entra al informe como limitación nueva (densidad de escena) o como ampliación de L4/L6, y si vale anotar más clips en densidad intermedia. **✎ 2026-08-09 — la gen. 3 corrió sobre el lote completo** (doc `operacion/111` §6) **y esa misma noche la revisión CIEGA del GT tiró 3 de los 5 episodios** (doc 113 §B): cifras vigentes `scene` F1 **0,333** vs `subject` **0,190** sobre **2 episodios evaluables** — el mecanismo se confirmó a escala, pero **ese `n` no sostiene ningún ranking entre granularidades** (F-111.1 enmendado); lo robusto es la **asimetría de FP** (~6× en positivos, **12× en los 11 negativos**: 26 vs 323). Nivel A de video: CR-01 **0,031** / CR-02 **0,018**. **Las dos preguntas de esta fila quedaron CERRADAS el 08-09 (D-113.1):** anotar más clips **NO** (doc 112 §8) y el encuadre es **precisar L4** — el set L1–L8 de `informe/99` §6 sigue cerrado, no se crea `L9`. Celda vigente: `results/index.md` §L4; doc 103 §3 cerrado con la misma decisión | ~~Claude~~ / ~~equipo decide el encuadre~~ ✅ decidido | nombra el límite real de G1/scene, no solo "material no guionado" |
| **Videos V1–V3 de la defensa** (pausados; 2 preguntas de alcance, D-90.7) | usuario decide | material de defensa, no resultado |
| Redacción §17.x + regenerar `informe-project-kit` | después de lo anterior (orden 2026-08-05) | el informe |
| Corregir el §15 del informe (erratas + línea base EPP supervisada + backbone de cada cifra + cruce con evidencia propia — ver §7.1/§7.4 de este doc) | pase de redlines (misma puerta que §17.x) | estado del arte defendible |
| ~~Licencias de los catálogos de modelos~~ ✅ **CERRADO 2026-08-10** — y **la premisa era falsa**: los 11 catálogos ya declaraban `license:` y `source:`. Lo que faltaba era el registro, ya escrito: sección **"PESOS DE MODELO"** en `license_registry.md` (GDINO y MM-GDINO **Apache-2.0**, YOLOE **AGPL-3.0**, las tres verificadas contra evidencia independiente: model cards y la cadena embebida en el `.pt`), con la implicancia AGPL declarada. **Residual: los repos no tienen `LICENSE` propio** — decisión del usuario antes de publicar, no bloqueo de defensa | ~~verificar y registrar~~ ✅ | citar los modelos en el informe |
| URL + fecha de acceso por video del lote (evidencia perecedera) — ✎ **son 18 `clip.yaml` con `video_url: TODO`** (14 del lote + 4 del piloto) y **13 copias promovidas** que lo arrastran: se arregla re-promoviendo, no a mano (doc `operacion/113` §C1) | usuario | robustece la cita de la fuente |
| Consentimiento escrito del rodaje (resuelto por declaración; plantilla disponible) | equipo/facultad | formalidad administrativa |
| Backup de `docs/` a otro disco | usuario | redundancia (repo local sin remote) |

**Nada de lo pendiente cambia una conclusión** (doc 98 §7): los mecanismos (F-81.x,
F-87.2, F-88.x, F-89.x, F-96.x, F-101.x), el veredicto del eje y las cifras por
estrato ya publicadas no se mueven; el GT del lote solo puede mover el agregado del
clip bench, el texto de L4 y el contexto del control de FP.

---

**Cómo re-verificar esta página:** correr
`python3 docs/operacion/datos/96-verificar-indices.py` — desde el 2026-08-09 cubre
**19 cifras sobre las 16 campañas con artefacto** (incluidas I1/I2 del estrato B y el
Nivel A sobre video de §4.1/§5.1), los deltas de bootstrap, y un **guard de cobertura**
que falla si aparece una campaña sin cifra verificada. Comparar el resto contra los 4 índices de
`e-ovrt_experimental-setup/results/` — cada tabla de allá tiene su artefacto
(`metrics.json`, `campaign.yaml` con sha256, `evals/`) y su doc de procedencia.

---

## Fuente: `docs/decisiones/estado-de-implementacion-adrs.md`

> SHA-256 del bloque: `ff26c392641a3aecc61c9894979e579075d74948c6755870925ff90d47797ece`  
> Seleccion: encuadre y tabla resumen vigentes; el detalle historico queda fuera.

# ADRs — Estado de implementación (cierre de trazabilidad)

- **Fecha:** 2026-07-18 · **última actualización:** 2026-08-18
- **Propósito:** cerrar el loop **decisión → implementación** para cada ADR. Los ADRs
  se escribieron *antes* de implementar y expresan su impacto como trabajo futuro;
  este documento registra, con rutas reales, endpoints y evidencia medida, **cómo
  terminó implementada cada decisión** al 2026-07-18. Los ADRs no se editan (carpeta
  cerrada); este doc es su companion de cierre y se actualiza con causa.
- **Cómo leer:** siglas en el doc 13 (glosario). Para cada ADR: la decisión en una
  frase autocontenida, cómo quedó implementada, la evidencia, y lo pendiente.
  La foto de los tres componentes originales es `operacion/97`; el estado ejecutado de
  distribución está en `operacion/114` y sus banners de cierre del 2026-08-11.

---

## 0. Tabla resumen

| ADR | Decisión (una frase) | Estado de implementación |
|---|---|---|
| 001 | La estrategia de detección del núcleo es **indirecta** (detectar persona+EPP y razonar la ausencia), no prompts de infracción directa | **Implementada como encuadre y cerrada experimentalmente** (✎ 2026-08-06; *decía "pendiente del acta `edir_v1`"*): acta firmada 2026-07-29 (doc 76) y **D1 corrió en los dos niveles** — E-DIR vetada por precisión (0,146 < 0,5) |
| 002 | El patrón se evalúa **por escena (G0)**, sin identidad de personas; el modo por-sujeto (G1) es capacidad operativa medida (adenda 08-04 + ADR-015) | **G0 implementado y verificado** (gate F1=1.0); **G1 implementado y medido** (✎ 2026-08-06; *decía "no portado (deuda)"*): decorador de fuente en el control-plane, F1 0,930 en 34 clips — ver §1 (RESUELTO 2026-08-04) |
| 003 | El acople live media→control es **bus ZeroMQ PUB/SUB + msgpack**, broker diferido | **Implementado y demostrado** (paridad byte-idéntica replay↔stream) |
| 004 | La corrida experimental es un **manifiesto paraguas** con `experiment_id` propagado, orquestada por un runner HTTP | **Implementado** (runner + manifiesto + propagación a ambos planos) |
| 005 | La distribución de alertas se recorta a **un canal MQTT en repo propio** | **Funcionalmente implementado** (✎ 2026-08-12): seis criterios de spec 45 verificados, incluidos DBE/EBE, MQTT QoS 1 contra broker real y `report.json`. ✎ 2026-08-14: los pendientes del 08-12 (vista de outcomes en la **webconsole**, **orquestación** integral y versionar el repo) se cerraron el 2026-08-13 — `13c801e`, `42529e2`, y repo con `c9903cc`/`1e6d8fa` |
| 006 | El reporte consolidado junta ambos planos por `experiment_id` y **cada métrica declara su aplicabilidad** con causa | **Implementado** (report.json/md + estados en todos los evaluadores) |
| 007 | En vivo, la corrida del control-plane es **1:1** con el run del media-plane y cierra por `run_finished` | **Implementado y verificado E2E** |
| 008 | El control-plane se expone como **servicio HTTP mínimo** (:8081) | **Implementado y superado** (11 endpoints vs los 3 decididos) |
| 009 | La config experimental se **centraliza** en experimental-setup y la **webconsole es la superficie de gestión primaria** | **Implementación incompleta** [Enmienda 2026-08-14]: la UI está rediseñada, pero el historial durable y la promoción `runs/`→`results/` quedaron diferidos (doc 115 §2.2, frentes C/D, D-115.2). La calificación histórica “superado” describía la UI, no el ciclo de evidencia. |
| 010 | Se ejecuta **la plataforma primero**, la evaluación después; el clip bench se dispara al cierre del spec 44 | **Cumplida** (orden 40→41→42→44 ejecutado; tooling del 43 completo) |
| 011 | El motor **emite en cada confirmación**; cooldown y supresión son política de notificación (módulo de distribución) | **Implementado en ambos lados de la frontera**: el motor emite todo; el distribuidor aplica cooldown por `(condition_id, source_id)` y lo registra |
| 012 | Bajo G0 la memoria de cobertura EPP **se ignora con causa declarada** (la histéresis subsume el parpadeo) | **Implementado y FALSACIÓN SUPERADA** (los dos tests condición-de-merge pasaron) |
| 013 | La plataforma **detecta la temporalidad de la fuente** y declara sola la no-aplicabilidad de métricas temporales | **Implementado con evidencia medida** (137 eventos / 0 alertas sobre imágenes) |
| 014 | Los resultados de un run global se **consolidan con híbrido selectivo** (liviano copiado, crudo referenciado) | **Implementación parcial** [Enmienda 2026-08-14]: consolidación y reporte están ejercitados; el sellado opt-in, el índice durable y la promoción trazable a `results/` siguen diferidos (doc 115 §4, frentes C/D, D-115.2). |
| **015** | **El alcance creció** en E-03/E-07/E-13 y se registra; **no se agrega ninguna capacidad más**; MQTT queda declarada NO implementada | **Aceptada (usuario, 2026-08-05) y APLICADA al doc 10** (ítem 10 + filas E-03/E-04/E-07/E-13). No es un ADR de implementación: es el cierre del registro de alcance. **R-13 y R-21 desbloqueados**. ✎ **2026-08-10: §2b/§2c/§6 DEROGADOS por ADR-016**; §2a/§3/§4/§5 vigentes (la lista L1–L8 se sigue citando desde §3) |
| **016** | **Reapertura acotada de la distribución** para cerrar la arquitectura: recorte exacto de ADR-005, E-06 sigue excluida, nada más se reabre (✎ 2026-08-11: **E-04 sale del freno por ADR-017**; el freno sigue para EN-3/E-10/E-06/CR nuevas) | **Aceptada y materializada**: módulo funcional, reporte integrado y broker MQTT real verificado. La vista de webconsole y la orquestación siguen abiertas; el repo aún no tiene commits |
| **017** | **El fine-tuning (E-04) se ejerce como jornada experimental completa** (escalera T1→T2/T3 con go/no-go pre-registrados, Mendieta, eval contra `bench_v3`), y el encuadre del informe pasa a **rama experimental condicionada por datos y protocolo** — la causa temporal queda prohibida | **Aceptada; implementación en curso, NO-GO T1 full.** F-100.1, freeze/smoke, dual gate, serving real y procedencia T-FT-023 están cerrados (snapshot `639e60df…`). ✎ **2026-08-15: D-FT-08/T-FT-005, D-FT-12 y D-FT-13 firmadas por el usuario, y T-FT-031/T-FT-032 CERRADAS la misma jornada** (doc 120: comando de evaluación congelado + enforcement canónico v2 + **baseline YOLOE-26s one-shot**, `bare_head` AP50 0,000 / recall CR-01 agregado 0,0002). **Las 7 gates del full-authorization están cerradas**; restan emitirla y el `RUN` manual (T-FT-043). Cero full; **no bloquea el informe**. ✎ **2026-08-15 (noche): T-FT-043 CERRADA — autorización emitida y verificada (7 gates) y `RUN` encolado como job `1167640`.** Abierto: la corrida y su evaluación (T-FT-050→052); sin cifra del modelo ajustado. ✎ **2026-08-17: JORNADA CERRADA — T-FT-044/050/051/052 `done`, veredicto D-FT-12 = NO-GO** (doc 123): el job corrió (`COMPLETED`, 10/10 épocas), el checkpoint se promovió por hash y se evaluó una sola vez — `bare_head` AP50 **0,0000 → 0,0455**, recall CR-01 **0,0002 → 0,2089**, pero faltaron **0,0045** al umbral de ganancia y `person` cayó **−11,62 %** (tope 10 %). Checkpoint **no adoptado**. **ADR-017 pasa de "implementación en curso" a EJERCIDO Y CERRADO en su tramo T1**; ✎ misma fecha, la escalera de `contingencia/20` §6 se aplicó: **T2/T3 NO habilitados** (T1 sin ganancia exigible) — rama cerrada con evidencia, **trabajo futuro con causa técnica, no temporal**. ✎ más tarde ese día, **enmienda D-FT-14** (vía D-FT-03): **T2 reabierto como tier exploratorio** con pre-registración propia (D-FT-15 a firmar antes del RUN), T1 intacto, T2 = último brazo contra `bench_v3`; **T3 sigue cerrado** |

| **018** | **El tercer módulo se acopla por subproceso local, no por servicio HTTP**: el runner del BFF lanza `eovrt-distribute` como proceso hijo (el repo de distribución es CLI, sin FastAPI/uvicorn); el dato sigue viajando por el bus (`:5558`), lo nuevo es el control del ciclo de vida | **Aceptada (usuario, 2026-08-15) y ya implementada** — documenta código verificado, no agrega capacidad. Requisito de despliegue vinculante: la consola dockerizada exige `EOVRT_DISTRIBUTION_EXECUTABLE`. Preflight de binario + drenaje de `stderr` con cap de 1 MiB son propios de este patrón. ✎ **2026-08-18** (*esta fila decía "el repo de distribución es CLI, sin FastAPI/uvicorn"*): eso quedó **superado por ADR-019** — el repo SÍ expone servicio HTTP además del CLI (ver fila 019). Este patrón de subproceso **sigue vigente y sigue siendo el default** del runner de la webconsole; ADR-018 no queda derogada ⛔ **✎ 2026-08-18: DEROGADA por ADR-020** — el subproceso dejó de ser patrón de acople y bajó a fallback operativo; esta fila queda como registro histórico y **no se cita como arquitectura vigente** |
| **019** | **El distribuidor suma un servicio HTTP** (`eovrt-distribute serve`, FastAPI/uvicorn en `:8082`), espejo del control-plane, para ser una unidad desplegable propia; no deroga ADR-018 — el subproceso local sigue siendo el camino default del runner del BFF | **Aceptada (usuario, 2026-08-17) e implementada y verificada (2026-08-18)**, incluida una corrida en vivo con cámara real: `POST /api/runs` (201 + id, 409 si hay una activa), `GET /api/runs/{id}` (sirve el mismo `distribution_summary.json` del CLI), `POST /api/runs/{id}/cancel` (parada cooperativa vía `ZmqSource.request_stop()`), `GET /healthz`\/`readyz`\/`config` (spec 45 §9.2/9.3). El runner del BFF es cliente HTTP opcional vía `EOVRT_CONSOLE_DISTRIBUTION_TRANSPORT=http`, con preflight que sondea `/healthz` en vez de exigir el binario local en ese camino. Containerización (Dockerfile, `docker-compose.yml`) queda diferida con causa (ADR-019 §4), no es deuda de esta fila ✎ **2026-08-18: el default pasó a HTTP por ADR-020**; ya no es opt-in — el opt-in ahora es el fallback por subproceso |
| **020** | **HTTP es el acople de la distribución; el subproceso baja a fallback operativo** y deja de ser patrón. Deroga ADR-018 | **Aceptada (usuario, 2026-08-18) e implementada**: el runner del BFF habla por HTTP **por default**; `EOVRT_CONSOLE_DISTRIBUTION_TRANSPORT=subprocess` conserva el camino viejo como red de seguridad (sigue implementado y probado). Preflight: sondea `GET /healthz` del servicio por default; el chequeo de binario local sólo corre en el fallback. **Consecuencia para el informe: DOS patrones de acople** — (a) HTTP config-driven en los tres módulos (`:8080`/`:8081`/`:8082`), (b) bus ZeroMQ (`:5557` detecciones, `:5558` alertas). El fallback **no se describe**: es operación, no arquitectura. Costo declarado: la webconsole exige el servicio arriba cuando la distribución está habilitada |

> **✎ 2026-08-15 — la nota del 2026-08-14 sobre el patrón BFF-subprocess quedó
> promovida a ADR-018 (fuente: `docs/decisiones/adr-018-acople-bff-subproceso-distribucion.md`)**, firmada por el
> usuario. *Decía: "Si el patrón se consolida merece ADR propia; queda como propuesta
> abierta, no ejercida."* El informe debe describir **tres** patrones de acople, no dos.
>
> ⛔ **✎ 2026-08-18 — la frase anterior quedó superada: son DOS.**
> ADR-020 (fuente: `docs/decisiones/adr-020-http-como-unico-acople-de-distribucion.md`) derogó a la 018. Tras
> ADR-019 (fuente: `docs/decisiones/adr-019-servicio-http-distribucion.md`) el distribuidor tiene servicio HTTP
> propio (`:8082`) y la 020 invirtió el default: **HTTP es el acople**, el subproceso bajó
> a **fallback operativo** (`EOVRT_CONSOLE_DISTRIBUTION_TRANSPORT=subprocess`) y dejó de
> ser un patrón. El informe describe **(a)** HTTP config-driven en los **tres** módulos y
> **(b)** bus ZeroMQ. El fallback no se cuenta: es operación, no arquitectura.

---

## Fuente: `docs/nucleo/10-registro-alcance-y-exclusiones.md`

> SHA-256 del bloque: `23ba692eaeb2c3be23cb05af48460aff1a2c7dd1d70535c934cfd4c8239f74b9`  
> Seleccion: documento completo.

# Registro de alcance y exclusiones — cierre formal del "no se implementa"

> ✎ **2026-08-05 — el alcance final NO es exactamente el de este doc.** El tramo
> experimental completo (docs 61–101) movió cuatro exclusiones, y eso está registrado en
> **ADR-015 — Cierre de alcance (fuente: `docs/decisiones/adr-015-cierre-de-alcance.md`)**
> (✅ **aceptada el 2026-08-05, y ya aplicada abajo**: ítem 10 de la lista de alcance +
> filas E-03/E-04/E-07/E-13 de la tabla de exclusiones):
> **E-03** — G1 dejó de ser "demostrativa en 2–3 clips": es **capacidad operativa medida
> en 34/34 clips** (F1 0,930 vs 0,789 de G0) y verificada en vivo. Sigue excluido el GT de
> identidades y la validación MOT · **E-07** — parcial (OAK-D como fuente + EN-2 con 87%
> de descarte on-device) · **E-13** — E-HYB-or **ejecutada y refutada**; `hyb_and` no
> ejecutada con causa · **E-04** — *(⚠️ esta línea quedó **derogada por ADR-017**, ver el
> tercer banner: el encuadre por «secuenciación» está prohibido)* sigue no ejercida, pero por secuenciación, no por falta
> de preparación. **E-10 no cambia** (métricas MOT siguen "no aplicable"), y las otras
> ocho exclusiones tampoco. ADR-015 también registró un cierre de agenda y una decisión
> sobre MQTT que luego fueron sustituidos por ADR-016; se conservan en el ADR como
> trazabilidad, pero ya no describen el estado vigente.
>
> ✎ **2026-08-10 — esas dos últimas cláusulas están DEROGADAS por
> ADR-016 (fuente: `docs/decisiones/adr-016-reapertura-acotada-distribucion.md`).** El usuario decidió
> **implementar la distribución de alertas** para cerrar la arquitectura de la plataforma,
> con el recorte exacto de ADR-005 y nada más (**E-06 sigue excluida**). Nada más se
> reabre: E-04, EN-3, E-10 y las condiciones CR nuevas siguen cerradas. ✎ **Estado
> verificado 2026-08-11:** el módulo cumple los seis criterios de spec 45, incluido
> reporte consolidado y MQTT QoS 1 contra broker real. ✎ **2026-08-14:** la vista de
> outcomes en la webconsole, la orquestación integral y el versionado del repo —que este
> banner daba por pendientes— se cerraron el 2026-08-13 (`13c801e`, `42529e2`; repo con
> `c9903cc` y `1e6d8fa`). Ver el **ítem 5** más abajo.
>
> ✎ **2026-08-11 — E-04 sale de esa lista por
> ADR-017 (fuente: `docs/decisiones/adr-017-fine-tuning-jornada-experimental.md`).** El fine-tuning
> **se ejerce como jornada experimental completa** (escalera pre-registrada T1→T2/T3 con
> go/no-go, entrenamiento en Mendieta, evaluación contra `bench_v3`, documentación de
> resultados **y limitaciones**), y su encuadre pasa a **rama experimental condicionada
> por datos y protocolo desde el planteo inicial** — las causas "presupuesto de tiempo"
> (julio) y "secuenciación" (ADR-015) quedan **derogadas como lectura**: el cómputo no es
> la restricción (T1 tiene un envelope acotado y Mendieta disponible) y el cronograma
> lo define el proyecto. Ver la ficha
> **E-04**, ya actualizada. Siguen cerradas EN-3, E-10, E-06 y las condiciones CR nuevas.

- **Fecha:** 2026-07-07 · **Actualizado 2026-07-09:** decisiones formalizadas en
  `decisiones/` (ADR-001…011). Tres ADRs amplían el alcance de forma acotada y
  quedan registrados acá: **ADR-002** (G1 demostrativa — ítem 10, redefine E-03),
  **ADR-008** (control-plane como servicio mínimo — ítem 9) y **ADR-009** (config
  centralizada + webconsole — ítem 11). **ADR-010** fija el orden de ejecución
  (plataforma primero) y **ADR-011** la frontera de política de alertas (no
  cambian el alcance).
- **Decisión que registra:** el proyecto implementa el **núcleo validable y lo
  detiene ahí** (decisión del usuario, 2026-07-07). Todo lo demás queda **excluido de
  implementación pero cerrado documentalmente**: con justificación metodológica
  anclada en el propio informe, rastro documental verificable y frase de declaración
  para el texto final.
- **Principio rector:** una exclusión bien cerrada no es "no llegamos" — es una
  decisión de alcance tomada con las reglas que el informe fijó de antemano
  (núcleo obligatorio vs extensión condicionada §17.1.2.2, niveles de compromiso
  §17.1.7.3.2, regla de fine-tuning Tabla 37, política de aplicabilidad §17.3.13.3).
  El informe ya trae el lenguaje para esto; acá se aplica caso por caso.

## 1. Vocabulario de estados (usar siempre el mismo)

| Estado | Significado | Cómo se declara en el informe |
|---|---|---|
| **Implementado y validado** | Corre, tiene tests y produce evidencia en corridas registradas. | Resultados con métricas. |
| **Especificado, no implementado** | Existe definición operativa completa (patrones, prompts, contratos, criterios) lista para implementarse. | "Extensión condicionada especificada; su validación excede el alcance experimental." |
| **Diseñado, no implementado** | Existe diseño técnico detallado (documento de arquitectura/módulo). | "Diseño registrado como anexo; implementación diferida a trabajo futuro." |
| **Condicionado no ejercido** | El protocolo define cuándo ejecutarlo y las condiciones no se dieron o no se priorizaron. | "Rama condicionada no ejercida según la regla [X]; condiciones de habilitación documentadas." |
| **No aplicable** | Métricas/evaluaciones cuya condición de aplicación no se cumple. | Taxonomía de aplicabilidad (§17.3.13.3), con causa. |

## 2. Lo que SÍ se implementa (lista cerrada — definición de terminado)

1. **Cadena completa DBE para CR-01/CR-02** (núcleo obligatorio): media-plane →
   bus/replay → motor de patrones (pattern set v2 alineado a Tabla 24) → alerta
   interna → reporte consolidado con estados de aplicabilidad.
2. **Experimento D1** (protocolo de prompts §17.1.5.4 / Tabla C.1): estrategia
   directa vs indirecta, **con la híbrida simple (or/and) como rama experimental
   de primera clase en la Fase 2** (ajuste 2026-07-09, ADR-001; vote sigue E-13).
3. **Clip bench** con GT temporal (grabación escenificada) y evaluación de alertas
   contra umbrales Tabla D.4. (✎ 2026-08-06: el GT quedó `gt_ready` **sin doble
   anotación ni kappa** — es la **limitación L2**, decisión declarada y no omisión;
   *decía "doble anotación 20%+kappa"*, que volvía a L2 un incumplimiento de esta
   definición de terminado.)
4. **EBE complementario sobre la infraestructura two-node ya construida** (Nodo A =
   EN-0/EN-1, Nodo B = CPN) con fuente viva de contingencia oficial (cámara IP/webcam
   o RTSP simulado). Se implementa porque ya existe (Fase 2 verificada) y produce R4
   con costo marginal bajo — no es una ampliación de alcance sino capitalización de
   trabajo hecho.
5. **Distribución mínima — FUNCIONALMENTE IMPLEMENTADA Y VERIFICADA** (✎ estado
   2026-08-11 conforme **ADR-016** y `operacion/114`; sustituye los estados previos
   registrados por ADR-015/016): un canal
   **MQTT** + `NotificationEnvelope` + ledger de idempotencia + retry mínimo + **vista de
   alertas en la webconsole existente**, en repo propio, consumiendo el bus
   control→distribución (ADR-005). El condicional del ADR-005 quedó resuelto en **sí**,
   por un motivo **arquitectónico**: es donde se gestiona el ciclo de vida completo de la
   alerta y su distribución, incluidas las políticas que ADR-011 sacó del motor
   (cooldown, supresión por ventana, re-notificación, agrupación). Los seis criterios de
   spec 45 quedaron verificados, incluido reporte y broker MQTT real. **E-06 sigue
   excluida** (canales adicionales y dashboard dedicado). ✎ **2026-08-14:** la vista de
   outcomes en la webconsole, la orquestación integral y el versionado del repo —listados
   acá como pendientes— se cerraron el 2026-08-13 (`13c801e`, `42529e2`; repo con
   `c9903cc` y `1e6d8fa`).
6. **Bus ZeroMQ media→control** (necesario para el punto 4).
7. **Overlay renderer** offline (videos V1–V3 de la defensa + figuras del informe).
8. **Mini-experimento A1** (costo marginal de una condición nueva por configuración).
9. **Control-plane como servicio mínimo** (ADR-008, 2026-07-09): cáscara HTTP sobre
   el runtime live (disparo, estado, config efectiva) + webconsole como cliente de
   ambos planos. Sin sesiones/auth/concurrencia (E-12 sigue vigente).
10. **G1 — capacidad operativa medida** (ADR-002 + **ADR-015**, actualizado 2026-08-05;
    *decía "G1 demostrativa … demostrada en 2–3 clips"*): granularidad por sujeto
    **config-driven**, medida sobre **los 34 clips del banco** (F1 0,930 vs 0,789 de G0,
    con las detecciones bit a bit idénticas) y verificada en vivo. El tracker vive en el
    control-plane. Sin métricas MOT (E-10 sigue "no aplicable"). Redefine E-03.
11. **Config centralizada + webconsole como superficie de gestión** (ADR-009,
    2026-07-09): configuración experimental de ambos planos versionada en
    experimental-setup; webconsole gestiona configs y dispara corridas en los dos
    servicios, con mejora de UI/organización UX (navegación por experimento).

Nada fuera de esta lista entra a implementación. Si algo de la lista peligra por
tiempo, el orden de sacrificio es: **11-UX (la mejora visual; la centralización de
config no se sacrifica — la usa el runner) → 10 → 9 (queda el runner CLI; el
runtime live no se sacrifica) → 8 → 7 (se reemplaza por overlays simples) → 5 (se
reduce a `mosquitto_sub`)** — nunca 1, 2 ni 3.

> ✎ **2026-08-12 — el orden de sacrificio quedó obsoleto.** Los ítems 5 y 10 terminaron
> materializados y medidos. Se conserva como registro de cómo se priorizó; ya no es una
> lista de candidatos ni una descripción del estado actual.

## 3. Registro de exclusiones

Formato por entrada: qué es → justificación → rastro documental existente → frase de
declaración → condición de habilitación futura.

### E-01 — Condiciones CR-03 y CR-04 (Nivel 2: reglas espaciales intra-frame)

- **Justificación:** brecha de datos **total** — cero fuentes públicas con la
  condición completa anotada (Tabla C.3); dificultad OVD estimada "Alta" por
  visibilidad fina del EPP y ambigüedad geométrica 2D (§17.1.5.2.4, Bianchi et al.
  2024). El informe las clasifica extensión condicionada desde la consolidación
  (Tabla 17) y su regla de datos las deja "fuera del camino ordinario" (Tabla 37).
- **Rastro documental:** patrones PR-03/PR-04 especificados con severidad y
  persistencia (Tabla 24); prompts candidatos formulados (Anexo C, Tabla C.1);
  requisitos de módulo espacial descritos (§17.3.8.3.3).
- **Declaración:** "Especificadas, no validadas: su evaluación requiere datos que no
  existen públicamente (Tabla C.3) y cuya producción excedería el alcance del
  prototipo sin desplazar el núcleo (Tabla 38, riesgo 2)."
- **Habilitación futura:** dataset propio o público con la condición anotada +
  módulo de reglas espaciales intra-frame.

### E-02 — Condiciones CR-05 y CR-06 (Nivel 3: relacional / zonas)

- **Justificación:** requieren MOT + razonamiento contextual (CR-05) y cámara fija +
  polígono parametrizado externo (CR-06) — dependencias que el informe excluye del
  núcleo explícitamente (§17.1.5.2.4, Tabla 23). Cobertura de datos parcial.
- **Rastro documental:** criterios de activación combinada definidos conceptualmente
  (§17.1.5.3.6: métrica de proximidad, punto de apoyo, punto-en-polígono); prompts de
  entidades componentes (Tabla C.1, CR-05a/b, CR-06a/b); severidades asignadas
  (Tabla 24).
- **Declaración:** "Especificadas a nivel de criterios de activación; su validación
  requiere módulos (MOT, zonas) definidos como extensiones condicionadas que el
  núcleo no exige (DA-06)."
- **Habilitación futura:** E-03 + parametrización de zonas + escenas con maquinaria.

### E-03 — MOT formal en el flujo de plataforma / métricas MOT (REDEFINIDA 2026-07-09; acotada por ADR-002)

- **Cambio de situación (1):** la rama `mati` implementó un tracker IoU liviano con ids
  estables (`SimpleIoUTracker`, en `eovrt_labs`) y el motor ya opera por sujeto con
  expiración y cooldown (doc 01 §12).
- **Cambio de situación (2 — ADR-002, cierra D2):** el tracker **se porta al
  media-plane** como componente opcional post-normalización (`track_id` aditivo en
  `media.detection.v1`) y G1 entra al alcance como **capacidad demostrativa**
  (2–3 clips, comparación de episodios G0 vs G1). **Lo excluido queda acotado a:**
  (a) G1 como modo del núcleo (el núcleo evalúa en G0, escena/fuente), y (b) las
  métricas MOT estándar y el GT de identidades que exigirían (Tabla D.2 → E-10).
- **Cambio de situación (3 — adenda ADR-002 ratificada + ADR-015, 2026-08-05; ✎
  propagado acá 2026-08-06):** dos correcciones sobre el punto anterior. (a) El
  tracker **no** se portó al media-plane: se implementó **en el control-plane como
  decorador de fuente** (adenda ADR-002; la deuda del spec 42 §3 queda abierta pero
  no bloqueante). (b) G1 **dejó de ser demostrativa**: es capacidad operativa
  config-driven **medida sobre los 34 clips del banco** (F1 0,930 vs 0,789 de G0,
  con detecciones bit a bit idénticas — F-89.1) y verificada en vivo. Lo excluido no
  cambia: G1 como modo del núcleo, y las métricas MOT / GT de identidades (E-10).
- **Justificación (ajustada):** el núcleo sigue sin exigir identidad persistente por
  definición metodológica (§17.1.10.2); G1 se muestra como extensión operativa del
  contrato sin prometer atribución por sujeto validada — no requiere GT MOT.
  (✎ 2026-08-06: *decía además "la demo … es lo primero que se sacrifica si la
  agenda aprieta"* — obsoleto: ADR-015 §2b cerró la agenda y G1 terminó siendo el
  mejor resultado del banco.)
- **Rastro documental:** decisión D2 con análisis (doc 03 §3); contrato `track_id`
  opcional especificado (docs 03/05); métrica ΔFP_tracker definida y con regla de
  aplicación (Tabla D.2) para cuando se habilite; semántica G1 descrita (doc 04 §
  granularidad, doc 07 D2).
- **Declaración (✎ reescrita 2026-08-06 conforme ADR-015 E-03):** "El núcleo evalúa
  a nivel de patrón por fuente y condición, conforme §17.1.10.2. La atribución por
  sujeto individual se implementa como **capacidad operativa config-driven**
  (contrato `track_id` opcional, tracker IoU liviano como decorador en el
  control-plane), **medida sobre los 34 clips del banco** (F1 0,930) y verificada en
  vivo; su validación con métricas MOT y GT de identidades queda fuera del alcance
  conforme Tabla D.2 (E-10)." (*Decía: "…se implementa como capacidad demostrativa …
  y se ilustra sobre clips seleccionados; su validación rigurosa … queda fuera del
  alcance…"*)
- **Habilitación futura:** GT de identidad + ΔFP_tracker con unidad de FP declarada,
  solo si se exigen métricas MOT estándar (E-10).

### E-04 — Fine-tuning / adaptación al dominio / rol TN

- **Estado (✎ 2026-08-11, ADR-017 (fuente: `docs/decisiones/adr-017-fine-tuning-jornada-experimental.md`)):**
  **rama experimental comprometida — se ejerce como jornada completa de fine-tuning**:
  preparación de datos y entorno, entrenamiento en Mendieta, evaluación contra
  `bench_v3` y documentación de resultados **y limitaciones**. La forma es la escalera
  pre-registrada — **T1 (linear probing) como entrada**, escalamiento a T2/T3 gobernado
  por los go/no-go de la Tabla 37 y `contingencia/20` §6, sin prometer tiers por
  adelantado. Deja de ser exclusión.
- **Actualización operativa 2026-08-13:** F-100.1 quedó resuelta por `finetuning_v1`
  (2.946 train/483 val, `bare_head` cubierto, bench intacto), pero T1 completo está en
  **NO-GO**. `1166583` cerró freeze/smoke técnico con exactamente 12 tensores/3.096 parámetros
  sólo en `cv3`/`one2one_cv3` y optimizer 12/12; dual gate y serving con checkpoint real están
  verdes. Antes del full faltan contrato de serving D-FT-08/T-FT-005, evaluación T-FT-031 y baseline
  YOLOE-26s T032 sobre `bench_v3`. La negativa sin auth mantuvo cero jobs full.
  ✎ **2026-08-15: el contrato de serving quedó firmado** (D-FT-08 aprobada por el usuario,
  T-FT-005 `done`), junto con D-FT-12 y D-FT-13; **y la misma jornada cerraron T-FT-031 y
  T-FT-032** — comando de evaluación congelado y **baseline YOLOE-26s one-shot ejecutada**
  (`bare_head` AP50 0,000; recall CR-01 agregado 0,0002 — doc 120, cifras de la rama, por
  estrato). El NO-GO quedó en su último eslabón: `full-authorization.json` + `RUN` manual
  del usuario. Cero jobs full.
  ✎ **2026-08-15 (noche): T-FT-043 CERRADA — el job full se envió.** Autorización emitida
  y verificada en el clúster (7 gates), `--test-only` en verde y `RUN` **encolado como job
  `1167640`**. "Último eslabón" y "cero jobs full" quedan superados. Lo abierto pasa a ser
  **la corrida y su evaluación**: enviar no es medir, y **no hay cifra del modelo
  ajustado** hasta que se evalúe el checkpoint.
  ✎ **2026-08-17: la corrida y la evaluación se hicieron — JORNADA CERRADA, veredicto
  D-FT-12 = NO-GO** (`operacion/123` (fuente: `docs/operacion/123-cierre-jornada-t1-no-go.md`)). **Ya
  existe cifra del modelo ajustado**: `bare_head` AP50 **0,0000 → 0,0455** y recall CR-01
  **0,0002 → 0,2089**, pero el gain gate exigía +0,05 (faltaron **0,0045**) o recall >0,5, y
  `person` cayó **−11,62 %** sobre un tope de 10 %. El checkpoint **no se adopta**. Con esto
  **E-04 queda ejercida y documentada de punta a punta**; el encuadre sigue siendo causa
  técnica/protocolar y el negativo es **pre-registrado**, nunca "falta de tiempo".
  ✎ **Mismo día, enmienda D-FT-14** (doc 117 §3): **T2 reabierto como tier exploratorio**
  con pre-registración propia (D-FT-15, firma previa al RUN) para cerrar la objeción de
  capacidad contra el resultado T1 — T1 intacto, T2 último brazo contra `bench_v3`;
  **T3 = trabajo futuro con causa técnica** (sin baseline MM-GDINO sana). El alcance de E-04
  **no vuelve a crecer**: T2 pertenece a la misma jornada comprometida por ADR-017.
- **Justificación del encuadre:** la regla del informe es explícita: "no prescribe que
  el fine-tuning deba ejecutarse; define cuándo vale la pena" (Tabla 37) — la rama fue
  **experimental y condicionada desde el planteo inicial**, nunca un descarte. La
  baseline zero-shot —el prerequisito de la regla— se ejecutó (R1/Sprint 2) y el
  benchmarking cerró. Las condiciones reales que la jornada atraviesa son **de datos y
  de protocolo**: F-100.1 fue resuelta sin tocar el bench; siguen el alcance entrenable,
  integración/evaluación, procedencia, licencias y transporte (entrenar en el clúster,
  evaluar local — doc 100 §6.3), además del riesgo de erosión de la capacidad
  open-vocabulary (§15.2.4.5). **No son de falta de cómputo** (el TN/Mendieta existe
  y el envelope T1 es acotado) **ni de plazo** (el
  cronograma lo define el proyecto). (✎ histórico: esta ficha declaró primero
  "presupuesto de tiempo del proyecto" —julio— y luego "secuenciación" —ADR-015,
  2026-08-06—; **ADR-017 deroga ambas causas como encuadre del informe**.)
- **Rastro documental:** protocolo comparativo completo especificado (Tabla 32:
  ΔAP/ΔRecall/ΔPrecision/ΔSDR, retención generalista, costo de entrenamiento);
  particiones sin leakage definidas y **materializadas** (`finetuning_v1`; train/val/bench
  disjuntos por hash, linaje y componente); candidatos acotados (GDINO/YOLOE, §17.1.9.2); escalera
  T1–T3 con presupuestos GPU y go/no-go pre-registrados (`contingencia/20`); costo T1
  medido con smoke verde end-to-end (doc 100).
- **Declaración (✎ reescrita 2026-08-11 conforme ADR-017):** "Rama comparativa
  experimental, condicionada desde el diseño metodológico (Tabla 37: baseline
  zero-shot primero, ajuste cuando la regla lo amerita): la baseline fue establecida,
  el protocolo comparativo y las particiones quedaron especificados y materializados,
  el costo quedó dimensionado con envelope Slurm de 2 h y smoke A30 documentado
  (doc 100), y la jornada de
  fine-tuning se lleva a cabo documentando sus resultados y limitaciones — sin afectar
  la pregunta central, que evalúa precisamente el desempeño sin entrenamiento."
  (*Decía "no ejercida por secuenciación del tramo experimental"*, y antes *"se
  difirió por presupuesto del proyecto"*.)
- **Puertas previas a T1 completo (no se saltean):** F-100.1 ya está cerrada;
  freeze/smoke técnico, dual gate y serving real también están cerrados. Permanecen
  D-FT-08/T-FT-005, evaluación T-FT-031 y baseline 26s T-FT-032; la procedencia
  T-FT-023 quedó CERRADA el 2026-08-13 (snapshot tar `639e60df…`)
  (docs 100/116/117). ✎ **2026-08-15: D-FT-08/T-FT-005 quedó cerrada por firma del
  usuario** —igual que D-FT-12 y D-FT-13— **y T-FT-031/T-FT-032 cerraron la misma jornada**
  (doc 120: baseline 26s one-shot ejecutada y evaluada). **Las 7 gates del
  full-authorization están cerradas**; restan emitirla y el `RUN` manual. El estado de
  la jornada al momento de la entrega se declara tal cual, con causa técnica —
  nunca temporal (ADR-017 §2f).

### E-05 — Broker de eventos (Kafka/RabbitMQ/NATS)

- **Justificación:** DA-03 separa transporte de persistencia y fija el log como
  fuente de verdad; un broker aportaría durabilidad/replay que el JSONL ya provee, al
  costo de un servicio pesado en la ruta de la plataforma (WSL). ZeroMQ cubre el
  fan-out requerido con dependencia nula de infraestructura.
- **Rastro documental:** análisis comparativo con criterios (doc 05 §7); seam
  documentado (`BrokerSource`/`BrokerPublisher`, doc 06 §17); decisión D3 (doc 03 §4).
- **Declaración:** "El bus transporta y el log persiste (DA-03); la incorporación de
  un broker queda como implementación adicional del mismo contrato, sin cambios en
  productores ni consumidores (seam documentado)."

### E-06 — Canales de distribución adicionales y dashboard dedicado

- **Justificación:** la Etapa 3 solo exige consumidores desacoplados con registro de
  intento/resultado (§17.3.10.3); un canal (MQTT) basta para demostrar el tramo y
  medir t_alert-notification. El dashboard dedicado duplicaría la webconsole.
- **Rastro documental:** diseño completo del módulo (doc 06: 4 canales, retry,
  dead-letter, dashboard) conservado como anexo de diseño; recorte D5 con
  fundamentos (docs 02 §4.7, 03 §6).
- **Declaración (✎ vigente 2026-08-12, ADR-016 + `operacion/114`):** "El tramo mínimo
  de distribución está funcionalmente implementado con MQTT, ledger de idempotencia,
  cooldown, retry y reporte consolidado. E-06 excluye los canales adicionales y el
  dashboard dedicado; su incorporación futura no altera la semántica de la alerta
  (DA-13). Quedan abiertos la vista de outcomes, la orquestación integral y el
  versionado inicial del repo."

### E-07 — Inferencia en borde, preselección EN-2 y OAK-D Pro PoE

- **Justificación:** la inferencia OVD en borde está excluida del flujo base por el
  propio informe (§17.1.4.2.3: "no forma parte del flujo base"; EN limitado a 1.4
  TOPS); la preselección EN-2 es condicionada con riesgo de pérdida de evidencia
  (DA-11, Tabla 57). **Update 2026-07-13:** el hardware OAK-D Pro PoE ya está
  disponible e integrado al media-plane **como fuente RGB** (plugin `oak_d`,
  verificado E2E); la contingencia cámara IP (§17.1.4.2.4) se ejerció antes y
  sigue vigente como alternativa. Lo que sigue excluido es la **inferencia en el
  borde** (EN-2): la OAK solo captura, el modelo corre en el host. **Update
  2026-07-15:** la preselección EN-2 (que no es inferencia OVD, sino una
  compuerta con un detector cerrado liviano) dejó de ser condicionada-no-ejercida:
  se implementó como variante opcional de corrida sobre la OAK-D, apagada por
  defecto (`e-ovrt_media-plane/docs/superpowers/specs/2026-07-15-oak-d-prefilter-en2-design.md`),
  cumpliendo las tres condiciones de DA-11/Tabla 57 (criterio conservador
  fail-open, registro de descartes en `summary.json`, corrida A/B de
  comparación contra el flujo sin preselector). La inferencia OVD (EN-3) sigue
  sin ejercerse: el modelo de vocabulario abierto sigue corriendo en el CPN. En
  la topología two-node los contadores de descarte de EN-2 todavía no viajan al
  nodo de referencia y quedan declarados no disponibles (v1).
- **Rastro documental:** modos EN-0/1/2 especificados (Tabla 56); contingencia
  documentada en el informe; el two-node implementado ya materializa EN-0/EN-1;
  EN-2 implementada y documentada en el spec 2026-07-15 y en Tabla 56 actualizada
  del media-plane.
- **Declaración:** "El rol EN opera en modos EN-0/EN-1 (captura y preprocesamiento no
  semántico), materializados en la topología two-node, y EN-2 (preselección
  liviana conservadora), implementada como variante opcional apagada por
  defecto conforme DA-11 y Tabla 57; la inferencia en borde (EN-3) permanece
  fuera de alcance conforme §17.1.4.2.3."

### E-08 — Zonas, geofences y calibración de escena

- **Justificación:** dependencia exclusiva de CR-06 (excluida, E-02); presupone
  cámara fija y parametrización externa al prompt (§17.1.5.2.4).
- **Rastro documental:** lógica punto-en-polígono y requisitos especificados
  (§17.1.5.3.6).
- **Declaración:** incluida en la de E-02.

### E-09 — Prompts en español / evaluación multilingüe

- **Justificación:** el inglés como idioma primario está fundamentado (§17.1.5.4.3);
  la línea multilingüe es explícitamente complementaria y opcional en el informe.
- **Declaración:** "Línea complementaria prevista en §17.1.5.4.3, no ejercida;
  contribución adicional posible, sin impacto sobre las conclusiones del núcleo."

### E-10 — Métricas MOT estándar (HOTA, DetA/AssA, IDF1, MOTA, IDSW/Frag) y benchmarks MOT17/OVT-B

- **Justificación (✎ actualizada 2026-08-06 conforme ADR-015 §2e / R-21):**
  condicionadas a **GT con identidades persistentes**, que no existe (Tabla D.2,
  §17.1.7.8.2). El antecedente viejo ("sin E-03 son no aplicables") ya no corre: el
  tracker **está habilitado y medido** (G1, F1 0,930 en 34 clips). Lo excluido son
  las **métricas** MOT y el GT de identidades, **no la capacidad**. El fundamento
  ahora es medido, no solo definicional: la ganancia de G1 se mide en alertas porque
  las detecciones son bit a bit idénticas (F-89.1) — la mejora no es de percepción y
  no se expresaría en MOTA/IDF1.
- **Declaración (✎ reescrita 2026-08-06; la anterior es la formulación que ADR-015
  §2e marca como FALSA al cierre):** "No aplicables: no existe GT de identidades
  persistentes, condición de aplicación no satisfecha conforme §17.1.7.8.2; la
  granularidad por sujeto está implementada y medida a nivel de alertas (E-03,
  F-89.1), y su validación con métricas MOT queda fuera del alcance." (*Decía: "No
  aplicables: tracker no habilitado en el núcleo (§17.1.10.2)…"*. En el reporte
  consolidado deben figurar con estado `not_applicable:<causa>`, no omitirse.)

### E-11 — Evidencia visual automática por alerta (clips/snapshots en runtime)

- **Justificación:** la política de minimización (DA-08/09) hace de la *ausencia* de
  captura automática una decisión de diseño, no una carencia. La evidencia visual
  para el informe y la defensa se genera offline con el overlay renderer sobre
  material escenificado con consentimiento.
- **Declaración:** "La trazabilidad ordinaria se apoya en eventos y metadatos
  (DA-08); la evidencia visual se produce como artefacto controlado offline para
  comunicación académica (DA-09)."

### E-12 — Persistencia robusta (base de datos), multi-run concurrente, hardening de servicio

- **Justificación:** ADR-0003 del control-plane (JSONL append-only, "una base más
  robusta puede incorporarse cuando la lógica esté estabilizada"); el prototipo es
  experimental, no productivo (§17.3.3). Un run activo por vez es una simplificación
  declarada del media-plane.
- **Declaración:** "Persistencia experimental append-only conforme ADR-0003 (serie
  del control-plane, 4 dígitos);
  capacidades operacionales de producto (DB, concurrencia, autenticación, retención)
  fuera del alcance del prototipo experimental."

### E-13 — Modelos OVD adicionales (Florence-2, OWL-ViT, YOLO-World…) y E-HYB-vote

- **Justificación:** los candidatos de trabajo quedaron acotados a GDINO y YOLOE por
  el propio protocolo (§17.1.9.2) tras la comparación de 5 variantes en R1/Sprint 2
  (que ya cumplió el rol de barrido de modelos).
  > ✎ **2026-08-10 — trazabilidad de ese barrido, porque era la pata más débil de esta
  > exclusión.** El "R1/Sprint 2" no tiene documento propio en la serie `docs/`; el
  > artefacto **auditable** equivalente es **`operacion/31-benchmark-modelos-host-local.md`**
  > (2026-07-09), que mide calidad en BENCH v2 val + rendimiento live. Dos precisiones que
  > hay que hacer al citarlo: **(1)** el doc 31 barre **6 variantes**, no 5
  > (`gdino-tiny`, `gdino-base`, `yoloe-26s/m/l/x`) — el "5" viene de `nucleo/historicos/02` y del
  > ADR-001, y el propio ADR-001 los trata como artefactos distintos; **(2)** el doc 31 se
  > declara **posterior** a Sprint 2 (hace *cross-check* contra él), así que no ES Sprint 2:
  > es su reemplazo auditable. El barrido total sobre la familia OVD, sumando la selección
  > S1/S2 del doc 64, llega a **10 configuraciones**. **Nada de esto cambia la exclusión**
  > —Florence-2, OWL-ViT y YOLO-World nunca se probaron y siguen excluidos por alcance—,
  > pero sí cambia **qué documento se cita**: citar `operacion/31` + `operacion/64`, no
  > "Sprint 2" a secas, que remite a un artefacto fuera de esta serie. (✎ 2026-08-06, ADR-015 E-13: la
  condición sobre E-HYB **ya se resolvió por medición** — E-HYB-or se **ejecutó y
  quedó refutada** (recall 0,824→0,353; mecanismo F-87.2: la unión de evidencia no
  es monótona en un motor temporal) y **`hyb_and` no se ejecutó con causa** (D-90.4:
  no medible contra este banco sin romper la comparabilidad de las 6 campañas).
  *Decía en futuro: "evidencia de complementariedad que la Fase 1 de D1 debe
  mostrar"*.) E-HYB-vote (fusión ponderada) sigue fuera: sin complementariedad
  demostrada, agregarla sería complejidad sin retorno (Tabla 38, riesgo 4).
- **Declaración:** "El barrido de modelos se realizó en la baseline (R1); el
  protocolo concentra la comparación en dos candidatos que representan los polos del
  trade-off expresividad-latencia (§17.1.9.2)."

## 4. Tabla resumen (para pegar en Etapa 4 / anexo del informe)

| # | Capacidad | Estado | Regla del informe que la ampara | Rastro |
|---|---|---|---|---|
| E-01 | CR-03/CR-04 | Especificada, no implementada | Tabla 17; Tabla C.3 (0 fuentes); Tabla 38 | Tabla 24, Anexo C |
| E-02 | CR-05/CR-06 | Especificada (criterios de activación) | Tabla 23; §17.1.5.2.4 | §17.1.5.3.6, Anexo C |
| E-03 | G1 como modo del núcleo / GT de identidades | ✎ **Ampliada (ADR-015, 2026-08-05)**: G1 no es demostrativa — es **capacidad operativa medida en los 34 clips** (F1 0,930) y verificada en vivo. **Sigue excluido**: GT de identidades y validación MOT | DA-06; §17.1.10.2 | ADR-002 + adenda 08-04; **ADR-015**; doc 89; `results/clip_bench/g1_*` |
| E-04 | Fine-tuning / TN | ✎ **Rama experimental comprometida; T1 full en NO-GO (adenda ADR-017, 2026-08-13).** F-100.1 resuelta; `1166583` validó freeze/smoke técnico 12 tensores/3.096 parámetros y optimizer 12/12; dual gate y serving real verdes. Pendientes D-FT-08/T-FT-005, T-FT-031 y baseline T-FT-032; T-FT-023 quedó CERRADA el 2026-08-13 (snapshot tar `639e60df…`). Cero full. La proyección Slurm 2026-08-18 no es promesa. ✎ **2026-08-15: esos pendientes cerraron y el job full se ENVIÓ** (T-FT-043 cerrada; autorización 7 gates, `RUN` encolado como job `1167640`). Abierto queda **la corrida y su evaluación**: no hay cifra del modelo ajustado. ✎ **2026-08-17: EJERCIDA Y CERRADA — veredicto D-FT-12 = NO-GO** (doc 123): job `1167640` `COMPLETED` 10/10 épocas → promoción por hash → eval única. `bare_head` AP50 **0,0000 → 0,0455**, recall CR-01 **0,0002 → 0,2089**, `vest` 0,2642 → **0,3292**; contra `person` 0,7843 → 0,6932 y mAP50 0,4193 → 0,4171. Falla el gain gate por **0,0045** y la retención por `person` (−11,62 %, tope 10 %). **Ya hay cifra del modelo ajustado**; checkpoint no adoptado; negativo **pre-registrado**. Encuadre: causa técnica/protocolar, nunca temporal | Tabla 37; §15.2.4.5 | docs 100/116/117/**123**; `contingencia/20`; **ADR-017** |
| E-05 | Broker | Diseñada (seam) | DA-03 | docs 05 §7, 06 §17 |
| E-06 | Canales extra + dashboard | Diseñada (anexo) | §17.3.10.3; DA-13 | doc 06 completo |
| E-07 | Borde / EN-2 / OAK-D | Parcial: OAK-D como **fuente** ejercida (2026-07-13) y EN-2 (preselección) implementada opcional, default off (2026-07-15), con **87% de descarte on-device** medido A/B contra GDINO; inferencia en borde (EN-3) sigue no ejercida | DA-11; §17.1.4.2.3–4 | Tabla 56; two-node = EN-0/1/2; **ADR-015** |
| E-08 | Zonas / calibración | Especificada | §17.1.5.2.4 | §17.1.5.3.6 |
| E-09 | Prompts multilingües | Prevista no ejercida | §17.1.5.4.3 | — |
| E-10 | Métricas MOT estándar | ✎ **No aplicable, con fundamento medido (ADR-015)**: lo excluido son las **métricas** y el GT de identidades, no la capacidad (el tracker está medido — E-03); la ganancia de G1 se mide en alertas porque las detecciones son bit a bit idénticas (F-89.1) | Tabla D.2; §17.1.7.8.2 | reporte con estado; **ADR-015**; doc 89 |
| E-11 | Evidencia visual runtime | Excluida por diseño | DA-08/09 | overlay offline |
| E-12 | DB / hardening | Fuera de alcance de prototipo | ADR-0003; §17.3.3 | ADRs control-plane |
| E-13 | Modelos extra / E-HYB-vote | ✎ **Ejercida más de lo previsto (ADR-015)**: modelo especialista corrido (T2/B1) y **E-HYB-or ejecutada y REFUTADA** (F-87.2: la unión de evidencia no es monótona en un motor temporal). **`hyb_and` no ejecutada con causa** (D-90.4: no medible contra este banco sin romper la comparabilidad de las 6 campañas). E-HYB-vote sigue fuera | §17.1.9.2; Tabla 38 | R1/Sprint 2; doc 04 §5; docs 84/87/88; **ADR-015** |

## 5. Reglas de redacción para que el cierre no suene a deuda

1. **Cada exclusión se declara donde se define, no al final**: cuando el informe
   introduce la capacidad, en la misma sección dice su estado y su regla — el lector
   nunca descubre "faltantes" por su cuenta.
2. **Usar la taxonomía de aplicabilidad** para métricas (no aplicable ≠ no medido) y
   los estados del §1 para capacidades — vocabulario consistente en todo el texto.
3. **Toda exclusión cita su regla previa** (Tabla 17/37/D.2, DA-XX): la decisión se
   tomó *antes* de los resultados, no después — eso es lo que la vuelve metodología y
   no excusa.
4. **Mostrar el rastro**: "especificada" siempre con puntero al artefacto (tabla,
   anexo, contrato, split generado). Una exclusión con artefactos es trabajo hecho.
5. En la defensa oral, si preguntan por algo excluido: estado + regla + rastro +
   habilitación futura, en ese orden, 20 segundos. (Se suma al Q&A del doc 09.)

## 6. Ajustes que este registro aplica al resto del set

*(Vigentes al cierre de esta auditoría, 2026-07-07. **Superados por decisiones
posteriores del 2026-07-09** donde se indica — ver `decisiones/ADR-002` y
`ADR-001`/doc 12; se conservan como registro histórico de por qué se pensó así.)*

- **Doc 02 §5 (recorte):** G1/tracker sale de "should" y pasa a exclusión E-03
  (especificada); el "should" queda solo con refinamientos menores del motor
  (cooldown) y el segundo canal se elimina (E-06). ✎ Aplicado. **✎ Nota posterior:**
  el cooldown se implementó en `mati` y ADR-011 lo reubicó en distribución — ya no
  es refinamiento del motor.
- **Doc 03 (tablero):** sin cambios de decisiones; D2 queda reforzada (G0 sin
  vía G1 en este proyecto). **✎ Superado 2026-07-09 (ADR-002):** D2 se cerró
  como G0 núcleo **+ G1 demostrativa** (tracker portado al media-plane, 2–3
  clips, sin métricas MOT) — ver E-03 arriba (§3), ya redefinida en consecuencia.
- **Doc 04:** E-HYB limitada a or/and condicionada a complementariedad; vote → E-13.
  (Ya estaba condicionada así; sin edición necesaria.) **✎ Superado 2026-07-09
  (ADR-001, doc 12):** la condición de complementariedad se retira — E-HYB-or/and
  corre siempre en la Fase 2 como rama experimental de primera clase; vote sigue
  excluida (E-13, sin cambios).
- **Plan 12 semanas:** las semanas 7–8 pierden el ítem "G1 sobre 2–3 clips si sobra
  agenda" — ese margen se reasigna a overlay renderer + guion de grabación.
  **✎ Superado 2026-07-09 (ADR-002):** la demo G1 sobre 2–3 clips vuelve a las
  semanas 7–8 como ítem 10 del §2, primera en el orden de sacrificio tras 11-UX.

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

---

## Fuente: `docs/operacion/114-relevamiento-distribucion-alertas.md`

> SHA-256 del bloque: `f4a2108bd213444b66a907e0e1de4797b93bce85ad10efb243e2773560d02d01`  
> Seleccion: banners de actualizacion vigentes; el cuerpo inferior es la foto inicial.

# 114 — Relevamiento del módulo de distribución de alertas (estado, brechas y plan de infra)

- **Fecha:** 2026-08-11
- **Qué es esto:** relevamiento del repo `e-ovrt_alert-distribution` tras la
  implementación del grueso del módulo. Determina el estado real **verificado
  ejecutando**, lista las brechas, y define cómo incorporarlo al deploy local
  junto con los demás servicios para probarlo contra las corridas ya ejecutadas.
- **Normativa:** ADR-016 (fuente: `docs/decisiones/adr-016-reapertura-acotada-distribucion.md`)
  (estatuto vigente: trabajo comprometido, recorte de ADR-005, E-06 excluida) ·
  ADR-005 · ADR-011 · spec 45 (fuente: `docs/specs/45-distribucion-alertas.md`) ·
  `informe/ajustes/material-etapa-3/92b` (fuente: `docs/informe/ajustes/material-etapa-3/92b-concrecion-distribucion-alertas.md`)
  (concreción técnica: es el contrato contra el que se releva).
- **Evidencia:** `datos/114-relevamiento-distribucion/` (3 summaries, las 2 configs
  usadas, el broker stub y un mensaje MQTT publicado).

**✎ 2026-08-11, misma jornada — C1 y C3 CERRADOS con TDD.** El usuario pidió seguir
con el orden del §6. **C3**: `distribution_summary.json` ahora agrega
`talert_notification_ms` **por `latency_mode`** (`{"live": {...}, "wall_clock_dbe":
{...}}`), no un bloque ciego — resuelto agrupando en `Distributor.run()`; test nuevo
con alertas mixtas (`DirectSource` ahora acepta `SourcedAlert` con `ts_publish_ms`,
además de dicts). **C1**: una alerta con campo requerido faltante ya **no aborta la
corrida** — `NotificationEnvelope.from_alert` se envuelve en `try/except (KeyError,
ValidationError)`, se cuenta en `skipped_invalid_alerts` (nuevo campo del summary,
al lado de `source_stats`) y la corrida sigue. Re-corrido el fixture exacto que
disparó el `KeyError` original (`datos/114-.../` no lo persistía, se reconstruyó
igual): `exit 0`, `skipped_invalid_alerts: 1`, summary escrito, las otras 2 alertas
entregadas. Suite: **39 tests + 1 integración**, ruff limpio. Sin commitear (regla
del workspace). El §3.5 y §4 de abajo quedan como estaban **al momento del
relevamiento** — es lo que corresponde corregir con código, no reescribir el
registro; ver el veredicto actualizado en el §1.

**✎ 2026-08-11, misma jornada — A1 CERRADO con TDD (el 6º criterio de terminado).**
`report.py` de `experimental-setup` ya integra `distribution_summary.json` como
cuarto hermano `runs/exp_<id>/distribution/` (ADR-014). Diseño (mismo patrón que
`t_capture->alert` con `DBE_MEDIA_TIME`, y que `censored_episodes`): la métrica
`t_alert-notification` en `resultados` es `computed` (p95 del modo `live`) **solo**
si hay latencia `live`; si el summary **solo** trae `wall_clock_dbe`, es
`not_interpretable` / `distribution_wall_clock_dbe_only` — nunca se reporta un
reloj de pared de reproceso como si fuera la latencia real (exactamente el
caveat que 92b §8 exige). Sin `distribution/`, comportamiento intacto
(`not_applicable`/`no_distribution`, 0 reportes viejos rotos). El
`distribution_summary.json` completo (counts, `skipped_invalid_alerts`, la
latencia por modo) pasa verbatim en una sección nueva `report["distribucion"]`
— mismo patrón que el detalle de censura. El hito `notificacion_entregada`
—hardcodeado `False` desde que existía el campo— ahora refleja `delivered > 0`
real. Verificado contra una corrida consolidada real (`video16_clip10_gt`, 2
alertas, DBE puro): `not_interpretable`/`distribution_wall_clock_dbe_only`,
`notificacion_entregada: true`, sección `distribucion` completa, `report.md`
renderiza la fila sin romper. **28 tests nuevos/tocados en
`test_report_generator.py`, suite completa del backend 592 pasan, ruff limpio.**

**A3/B3 — resuelto sin Docker.** El usuario decidió NO dockerizar el broker:
**el bloque `mosquitto` queda escrito en el compose de `infra/platform`** (para
cuando el resto del deploy se dockerice) **pero sin verificar** — el camino
que corre HOY es un proceso común del host, igual que el control-plane. En vez
de Mosquitto (necesita `apt`/`sudo`, no disponible en esta sesión), se usó
**`amqtt`** — broker MQTT 3.1.1 puro Python, instalable con `pip` en un venv
aislado, sin tocar el sistema. Con `amqtt` corriendo y un **suscriptor
independiente** (equivalente exacto a `mosquitto_sub -t 'eovrt/alerts/#' -v`,
`datos/114-.../` script `mqtt_sub.py`), se re-corrió el replay de `v06_c01`
(193 alertas) en `channel.mode: live`: **23/23 mensajes recibidos por el
suscriptor, en vivo, contra un broker MQTT real** — no ya el stub de 80 líneas
de la primera pasada. Esto era la única parte del criterio 3 (spec 45 §7) que
seguía siendo un smoke; ahora es la demo real que pide 92b §7. Evidencia:
`datos/114-.../08-mqtt-real-broker-summary.json` y
`09-mqtt-real-broker-mensajes-recibidos.jsonl`. Documentado en
`infra/platform/README.md` (nueva sección) + `infra/platform/mosquitto/`
(`mosquitto.conf` para Docker, `amqtt.yaml` para el camino real de hoy).

Sin commitear.

---

---

## Fuente: `docs/informe/ajustes/gobierno/99-materiales-de-cierre.md`

> SHA-256 del bloque: `a041b5a5dde909e0bb42f6d217a575c5f92f0226501edd436c8552ba9a1f706c`  
> Seleccion: lista vigente de limitaciones L1-L8; la cronologia de ADRs queda fuera.

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

---

## Fuente: `e-ovrt_experimental-setup/results/index.md`

> SHA-256 del bloque: `13c63a9cd1e6c6d5a1d16085c6be3f0203a42c14978a182531974e6ea1497cf6`  
> Seleccion: argumento y reglas de lectura; L1-L8 se incorporan desde gobierno/99.

# Resultados del proyecto — punto de entrada

Todo lo medido, organizado por **material** (imágenes / video / tiempo real). Es el
insumo directo del capítulo de resultados del informe: cada tabla de acá tiene su
artefacto en disco y su doc de procedencia.

> **Estado: 2026-08-14.** El tramo experimental está **completo** — 17 campañas con
> artefacto (16 de video y la campaña de distribución), más el bench de imágenes.
> La última corrección de fondo fue la **revisión ciega del GT del estrato B**
> (doc `operacion/113` §B), ya propagada a los cuatro índices y a las limitaciones
> **L1 / L4 / L6**. Verificación mecánica al día: `96-verificar-indices.py` (26 cifras,
> cobertura 17/17) y `109-verificar-organizacion.py`, ambos verdes.
> **Lectura de una sola pasada:** `docs/sintesis/resultados-y-conclusiones.md`.

> **Marco de lectura, común a todo (doc 81 §1).** Cada número es el rendimiento medido
> de **una combinación concreta**, no una nota de aprobación. La pregunta del trabajo
> no es *"¿OVD detecta bien?"* sino *¿qué rendimiento se obtiene HOY en construcción
> civil con detección open-vocabulary **sin entrenar**, expresando las condiciones de
> riesgo en lenguaje, y qué aporta la plataforma alrededor del modelo?* **El contraste
> entre filas ES el experimento.** Un recall de 0,40 en multitud no es un fallo del
> proyecto: es el dato.

## Los cuatro índices

| Índice | Qué mide | Nivel |
|---|---|---|
| **`bench_imagenes/` (fuente: `e-ovrt_experimental-setup/results/bench_imagenes/index.md`)** | Selección de modelos, AP por clase y estrato sobre `bench_v3` (6.477 imgs, 3 fuentes), y el costo de agregar una clase nueva | percepción espacial |
| **`bench_nivel_a/` (fuente: `e-ovrt_experimental-setup/results/bench_nivel_a/index.md`)** | Estado "sin EPP" por persona: el nivel donde se decide entre estrategias de prompts (E-DIR vs E-IND) | percepción, por sujeto |
| **`clip_bench/` (fuente: `e-ovrt_experimental-setup/results/clip_bench/index.md`)** | Alertas contra GT temporal humano. Banco vigente **47 clips** (34 del rodaje + 13 del estrato B), 32 pos / 15 neg, **37 episodios**. **14 campañas: 6 de combinación + 6 de densidad + 2 de estrato B** | plataforma (Nivel B) |
| **`realtime/` (fuente: `e-ovrt_experimental-setup/results/realtime/index.md`)** | Camino en vivo: integridad del bus, latencia operativa, techo de fps y su causa, y calidad bajo restricción de tiempo real | operación (EBE) |

La campaña específica de distribución bajo `realtime/t_alert_notification/` (fuente: `e-ovrt_experimental-setup/results/realtime/t_alert_notification/README.md`)
cerró el tramo `bus de alertas -> PUBACK MQTT QoS 1`: **p95 64,534 ms (n=460)**. Esta cifra no
representa sensor -> notificación y se mantiene separada de las latencias de percepción y control.
Para operación continua se informa además el régimen sostenido: entregas 2.ª+ por corrida,
**p95 102,025 ms (n=104)**; las primeras entregas dan **49,869 ms (n=356)**.

### La cadena temporal completa se cita POR TRAMOS (✎ 2026-08-15)

Con la distribución medida, la plataforma tiene **toda la cadena instrumentada** — pero cada
tramo tiene su propio origen de reloj, su propio dueño y su propia cifra, y **no se suman
percentiles entre tramos** (los p95 no son aditivos). La formulación correcta para el informe:

| Tramo | Qué mide | Cifra citable | Fuente |
|---|---|---|---|
| `capture_to_host` | fotón → dequeue en el host (F-101.8: el G2A arranca en el dequeue, no en el fotón) | **202–217 ms** en las 6 corridas del rodaje; hasta ~1,6 s degradado | `realtime/` (fuente: `e-ovrt_experimental-setup/results/realtime/index.md`) §2 |
| **G2A** | captura (dequeue) → alerta, por frame | por contexto: 31,8 ms p95 single-host video · **630–890 ms** GDINO live · 225–249 ms YOLOE live | `realtime/` (fuente: `e-ovrt_experimental-setup/results/realtime/index.md`) §2 |
| **`t_alert-system`** | inicio anotado del episodio (GT) → alerta. **Otra referencia temporal**: está dominada por la persistencia del patrón (`confirm_after_ms` 4.000/7.000), no por el transporte — no se encadena aritméticamente con los tramos físicos | por campaña/condición, p. ej. T1 5.327 ms · G1 5.236 ms | `clip_bench/` (fuente: `e-ovrt_experimental-setup/results/clip_bench/index.md`), equivalencia de nombres allí |
| **`t_alert-notification`** | bus de alertas → PUBACK MQTT QoS 1 | **p95 64,534 ms (n=460)**; sostenido 102,025 ms (n=104) | `realtime/t_alert_notification/` (fuente: `e-ovrt_experimental-setup/results/realtime/t_alert_notification/README.md`) |

Lectura honesta de conjunto: **la distribución no es el cuello** — su p95 (≈65 ms) es un
orden de magnitud menor que el G2A live del modelo que detecta (630–890 ms) y dos órdenes
menor que la persistencia deliberada del patrón (4–7 s). La cadena vidrio→notificación de
un evento se describe cualitativamente con los cuatro tramos citados por separado.

## Runs de evidencia

El `inventario canónico generado` (fuente: `e-ovrt_experimental-setup/results/evidence-runs.md`) enumera, sin globs ni IDs abreviados,
todos los runs citados por estos resultados DBE y EBE. La copia versionable correspondiente vive
en `evidence-runs/` (fuente: `e-ovrt_experimental-setup/results/evidence-runs/README.md`): conserva únicamente artefactos textuales curados,
comprime los JSONL y excluye imágenes, video, previews, presets de cámara y secretos. Un run que
no figure en el inventario no pasa a ser evidencia canónica por el solo hecho de existir.

Desde la raíz de este repositorio, `python3 tools/evidence_runs.py sync` regenera ambos artefactos;
`python3 tools/evidence_runs.py --check` comprueba el catálogo contra los originales y
`python3 tools/evidence_runs.py --check --archive-only` valida la copia sin depender de ellos.

## El recorrido del argumento, en cuatro números

1. **Qué ve el detector sin entrenar** — `gdino-tiny-560`, campeón robusto a la fuente:
   **mAP50 0,551** sobre 6.477 imágenes de 3 fuentes independientes. La asimetría es
   estructural: `person`/`helmet` sólidas, `vest` débil, `bare_head` fuerte solo en el
   especialista. → `bench_imagenes/`
2. **Cómo conviene expresar la condición** — evidencia positiva + inferencia (E-IND)
   gana a los prompts directos de ausencia (E-DIR) en los dos niveles: a Nivel A por
   F1 con IC no solapados en `shel5k` (el gate pre-registrado **no se disparó** y
   E-DIR pasó a Fase 2), y a Nivel B decide el criterio pre-registrado — el **veto de
   precisión (0,146 < 0,5)** la descarta como núcleo. Lo que manda es la formulación,
   no el mecanismo (F-88.3). → `bench_nivel_a/` + `clip_bench/`
3. **Qué agrega la plataforma sobre la detección cruda** — la histéresis rescata
   percepción intermitente (CR-02 llega a recall 1,000 con SDR 0,281), pero es palanca
   de doble filo; y **la capa que más agrega es la identidad**: F1 0,789 → **0,930**
   con las detecciones bit a bit idénticas. El margen no estaba en el modelo. →
   `clip_bench/`
4. **Qué sobrevive al tiempo real** — la ganancia de la identidad **excluye el cero en
   las cuatro densidades medidas** (bajo decimado regular; conserva la dirección bajo
   el descarte irregular medido del live, 6/6 — doc 101), incluida el ancla del techo
   live de hoy (stride 7 ≈ 4,29 fps nominal; el live entrega 1,16–4,42 fps). Es la
   única palanca del banco significativa bajo esa restricción. → `realtime/` +
   `clip_bench/` § densidad

## Reglas de lectura que NO son negociables

Salieron de artefactos de medición cazados **antes** de reportar (familia F-EV1/2/3,
doc 81 §3). Ignorarlas produce conclusiones falsas con números correctos:

- **Reportar siempre por estrato y por escenario, nunca solo el agregado** (L5). El
  agregado de `bench_v3` está dominado por `shel5k` (77%); el del clip bench, por
  P1/P2. Y en el eje de densidad, un agregado plano escondía una redistribución
  completa (F-96.1).
- **Los clips negativos no entran a precision/recall/F1** — su métrica son los FP
  (F-EV1). Promediar su F1 hunde el agregado contando aciertos como catástrofes.
- **`re_alerts` no son falsos positivos** (ADR-011).
- **El SDR no se compara entre cadencias** (F-96.6): sube al bajar la densidad y es
  ~100% artefacto del instrumento, verificado por decimación de las mismas
  detecciones.
- **El `t_alert` agregado no se compara entre densidades sin control de
  supervivencia** (F-96.5): los episodios lentos mueren como `missed` y su salida baja
  el promedio justo cuando el costo sube.
- **FAR/hora se reporta, pero no sostiene ninguna cota** (D-90.1 **precisada**, no
  derogada — ver L1). Desde que existe el clip soak (`v06_c01`, 0,1027 h) la métrica es
  computable y se publica (**29,2** escena / **1.850,8** sujeto), pero el denominador
  está a dos órdenes de magnitud de las 3 h que exige la regla de 3: **citar siempre
  como "3 y 190 FP en 6:09,6 del único clip soak", con la tasa horaria como derivada**,
  nunca como "≤N FA/hora". La evidencia principal de falsas alarmas sigue siendo el
  **control de negativos**.
- **Las métricas que no aplican usan los estados del ADR-006/013**
  (`not_applicable:<causa>`), nunca frases vagas.

---

## Fuente: `e-ovrt_experimental-setup/results/index.md`

> SHA-256 del bloque: `35281c1cc623216dd469ed68386055d795af9c45656b91ca9dd00d1e8480536a`  
> Seleccion: verificacion, licencias y procedencia; omite el rotulo historico de L1.

## Verificación de estos índices

`docs/operacion/datos/96-verificar-indices.py` chequea mecánicamente que (a) los
enlaces markdown relativos resuelvan, (b) **26 cifras citadas** coincidan con el
`metrics.json` en disco, (c) **toda campaña con artefacto tenga al menos una cifra
verificada**, (d) los 3 deltas del bootstrap donde se afirma exclusión del cero
coincidan con su artefacto, y (e) todo doc referenciado exista. **Última corrida:
todo verde.**

✎ **2026-08-14 — alcance ampliado.** Antes cubría 8 F1 (T1, G1, R1–R6) y luego las
16 campañas de video. Hoy cubre **las 17 campañas con artefacto**: las 14 de
`clip_bench`, las 2 de `bench_nivel_a` y `realtime/t_alert_notification`, incluida
su cifra citable y el desglose first-delivery/steady-state. El chequeo **(c) es el
que impide que el script vuelva a envejecer en silencio**: si aparece una campaña
nueva sin fila en `CIFRAS`, falla en vez de reportar "todo verde" sobre un
subconjunto. El chequeo **(b) además cuenta ocurrencias con límites numéricos**: una
cifra puede declarar cuántas veces la cita su índice (p. ej. `64,534` y `n = 460` salen
**2 veces** en `realtime/index.md`), de modo que romper **una sola** de las dos ya falla,
y un entero desnudo como `104` no se da por citado por aparecer dentro de `1.104`.
Alcance que sigue **sin cubrir**: las cifras de `bench_imagenes/`, que
no tienen `metrics.json` en este repo y se verifican contra el doc 64.

Correrlo antes de volcar cifras al informe — la auditoría del informe
(`docs/informe/ajustes/gobierno/95-auditoria-y-plan-de-cierre.md` §2.1, serie distinta de
`operacion/95`) ya encontró una vez que *"el número estrella del TFG no tenía
respaldo en el repo"*.

## Licencias de los pesos de modelo (✎ 2026-08-10)

Los **11 catálogos** de `e-ovrt_media-plane/configs/models/**/*.yaml` declaran `license:` y
`source:` por variante, y el registro con la evidencia de verificación vive en
**`e-ovrt_datasets/datasets/registry/license_registry.md` §PESOS DE MODELO**:
**Grounding DINO** y **MM-Grounding-DINO** son **Apache-2.0** (verificado contra el
frontmatter de los model cards descargados), **YOLOE** es **AGPL-3.0** (verificado contra la
cadena embebida en el propio `.pt` y contra el paquete `ultralytics`). Al citar los modelos
en el informe hay que decir la licencia de las tres familias, y para YOLOE que se usó como
**contraste medido y descartado con causa**. No se redistribuyen pesos: `models/**` está
gitignoreado en el media-plane.

## Procedencia

Cada campaña trae `campaign.yaml` con la combinación declarada y los sha256 del prompt
set congelado y del manifest del banco; `metrics.json`; y **procedencia por corrida**
apuntando a los runs del media-plane, que son la fuente de verdad de las detecciones
(DA-03). Los originales permanecen fuera de este repo; el archivo común
`evidence-runs/` (fuente: `e-ovrt_experimental-setup/results/evidence-runs/README.md`) conserva la copia textual curada de los runs citados,
sin imágenes ni video procesados.

Alcance exacto, para no prometer de más (✎ 2026-08-09):

- **`clip_bench` (14 campañas)** — el caso completo: `metrics.json` con la **misma forma**
  para todas (`clip_campaign_metrics.v1`), `evals/` por clip, y `provenance.json`.
- **`bench_nivel_a` (2 campañas)** — otro esquema de métricas (es otro nivel) y
  procedencia con nombre propio en D1 (`provenance_runs.json`, indexado por corrida en
  vez de por clip). **Sin `evals/` por diseño**: a Nivel A no interviene el motor
  temporal, así que no existe la noción de "eval por clip".
- **`bench_imagenes`** — consolida mediciones cuyos artefactos viven en los repos
  hermanos y sus cifras se contrastan con el doc 64.
- **`realtime/t_alert_notification`** — tiene campaña propia, `metrics.json` y
  cobertura obligatoria en `96-verificar-indices.py`; los demás resultados live
  conservan la procedencia declarada en sus documentos operativos.

**Las 17 campañas con artefacto tienen hoy procedencia por corrida completa.** En las
**16 de video** eso no era cierto hasta el 08-09: I1/I2 declaraban 4 corridas para 13
clips y NA1 no tenía ninguna; hoy es regenerable y verificable con
`docs/operacion/datos/113-regenerar-provenance-estrato-b.py --check`. La 17.ª,
`realtime/t_alert_notification`, la declara en su propio `provenance.json` (intento
aceptado, fases y hashes) más `integrated-runs.json`, que enumera `media_run_id` y
`control_run_id` por corrida integrada.

---

## Fuente: `e-ovrt_experimental-setup/results/bench_imagenes/index.md`

> SHA-256 del bloque: `4a94dab6d80ae791f3ba23008a051ac822e49e877b6dbbf895c7dee4017e259f`  
> Seleccion: documento completo.

# Bench de imágenes — resultados consolidados

Índice de los resultados del **material de imágenes**: selección de modelos (Fase S),
caracterización del banco `bench_v3` y extensibilidad a clases nuevas. El estado por
persona (Nivel A, el nivel donde se decide entre estrategias de prompts) vive en
`results/bench_nivel_a/`; las alertas sobre video (Nivel B) en `results/clip_bench/`.

**Cómo leer estas tablas.** Cada fila es el rendimiento medido de una combinación
concreta, no una nota (marco del doc 81 §1). La pregunta del trabajo es *qué se
consigue hoy con OVD sin entrenar en construcción civil*; el contraste entre filas
**es** el experimento. Todo es **zero-shot**: ningún modelo vio una imagen de este
dominio en entrenamiento.

**Regla de reporte (`registry/bench_v3.md`):** las métricas se dan **por estrato y
agregadas, nunca solo el agregado.** El agregado de `bench_v3` está dominado por
`shel5k` (77% de las imágenes).

---

## 1. El banco: `bench_v3` (congelado 2026-07-23)

**6.477 imágenes, 3 fuentes independientes.** Manifest con sha256 por fuente
(`bench_v3_manifest.json`); procedencia y salvedades completas en
`e-ovrt_datasets/datasets/registry/bench_v3.md`.

| Estrato | Origen | Imágenes | Qué aporta |
|---|---|---|---|
| `bench_obra` | `construction_site_safety` curado (doc 63) | 147 | Núcleo con pasada visual muestral; todas las clases con negativos explícitos |
| `chv` | CHV (académico, cita obligatoria `wang2021ppe`) | 1.330 | 2ª fuente person/helmet/vest; **mejor AP de vest del proyecto** |
| `shel5k` | SHEL5K (Mendeley, CC BY 4.0) | 5.000 | 3ª fuente; **`bare_head` nativo** (6.120 instancias vs 61 del núcleo) + `person_gt_shel5k.json` (5.248 violadores CR-01) |
| **Total** | | **6.477** | |

> **Por qué existe `bench_v3` y no el BENCH original.** El split de 196 imgs de
> `construction_site_safety` resultó ~20–25% fuera de dominio (selfies COVID, PASCAL
> VOC, aeropuerto/casino — auditado en doc 63). Se conserva sin modificar como
> artefacto histórico; todo resultado reportable usa `bench_v3`.

## 2. Fase S — selección de modelos (docs 61/64/66)

### S1/S2 sobre el núcleo curado `bench_obra` (147 imgs)

| Configuración | mAP50 obra | recall CR-01 obra | vest AP obra |
|---|---|---|---|
| **`gdino-tiny-560`** | **0,503** | 0,369 | 0,520 |
| `gdino-tiny` (800) | 0,502 | 0,323 | 0,456 |
| `gdino-base-560` | 0,474 | **0,400** | **0,582** |
| `yoloe-26x` | 0,405 | 0,000 | 0,182 |

### Las 6 configuraciones que NO llegaron a `bench_obra` (✎ agregado 2026-08-10)

La tabla de arriba re-puntúa **4** configuraciones sobre el núcleo curado. La matriz S1
original (doc 64) midió **10**, y las 6 restantes se descartaron antes de esa re-puntuación.
Hasta hoy este índice nombraba solo a `mm-gdino-tiny` y `mm-gdino-large` en la prosa de
descartes, y **omitía a `mm-gdino-base` y a `gdino-base` (800)** — que sí se midieron. Van
acá con sus números, para que la exclusión no sea una afirmación sin dato:

> ⚠️ **Marco distinto: estas filas son BENCH v2 (196 imgs), no `bench_obra` (147).** No se
> comparan celda a celda con la tabla de arriba; se leen entre sí. Es la única escala en la
> que existen: nunca se re-puntuaron, precisamente porque quedaron fuera.

| Configuración (BENCH v2, 196 imgs) | mAP50 | recall CR-01 | vest AP | `bare_head` AP | inf p50 | Por qué no siguió |
|---|---|---|---|---|---|---|
| `gdino-base` (800) | 0,401 | 0,514 | 0,43 | 0,01–0,03 | 213 ms | **Dominada por su propia variante 560** (0,453 mAP, 146 ms): peor mAP y **+46% de latencia**. Misma regla que descartó `gdino-tiny` (800) |
| `mm-gdino-base` | 0,360 | 0,029 | 0,39 | **0,00** | 213 ms | **Mediocre sin ventaja en nada** (hallazgo 5 del doc 64): recall CR-01 0,029 y `bare_head` 0,00 |
| `mm-gdino-large` | 0,017 | — | — | — | 723 ms | **Roto**: reproduce el bug de bboxes degeneradas (sanity-check pre-planificado: 2–3 degeneradas) |
| `mm-gdino-tiny` | — | — | — | — | — | **Excluido a priori** en Sprint 2 por bboxes degeneradas; no se re-midió |
| `yoloe-26l` / `26m` / `26s` | 0,407 (26x, campeón de la familia) | 0,049 (`26s`) | — | **0,000 en las 4** | 43 ms (`26x`) | **La familia entera es ciega a la condición.** `26x` es el campeón YOLOE y **el único tabulado arriba** por eso: representa a la familia en su mejor talla, no en la más rápida |

Fuente: doc 64 (BENCH v2, 196 imgs — sin `metrics.json` mecánico; verificado a mano
2026-08-14).

**Lectura de esta tabla, en una línea:** de los 6 descartes, **3 son por dominancia
medida** dentro de su propia familia (las dos variantes 800 y las tallas menores de YOLOE),
**2 por defecto técnico verificado** (MM-GDINO large y tiny, bboxes degeneradas) y **1 por
mediocridad sin eje propio** (`mm-gdino-base`). Ninguno quedó afuera por no haberse
probado.

### Confirmación B5 sobre `bench_v3` completo (6.477 imgs)

| Modelo | mAP50 (n=6.477) | recall CR-01 (n=5.313) | inf p50 † |
|---|---|---|---|
| **`gdino-tiny-560`** | **0,551** (1º) | 0,308 | **129 ms** |
| `gdino-base-560` | 0,525 | **0,599** (1º) | 146 ms |
| `yoloe-26x` | 0,442 | 0,000 | 43 ms |

† Las latencias p50 provienen de la matriz sobre el BENCH v2 (196 imgs, doc 64), no
se re-midieron sobre `bench_v3`.

**El campeón se sostiene en las dos escalas** — `gdino-tiny-560` gana mAP50 tanto en
el núcleo curado (147) como en el bench completo (6.477): **es robusto a la fuente**,
no un artefacto del denominador chico.

### Por clase y por estrato (la asimetría es estructural)

| Modelo | Estrato | person | helmet | vest | bare_head | recall CR-01 |
|---|---|---|---|---|---|---|
| `gdino-tiny-560` | `shel5k` (n=5.000) | 0,770 | 0,707 | — | **0,133** | 0,308 |
| `gdino-tiny-560` | `chv` (n=1.330) | 0,862 | 0,886 | **0,553** | — | — |
| `gdino-base-560` | `shel5k` (n=5.000) | 0,693 | 0,415 | — | **0,399** | **0,602** |
| `gdino-base-560` | `chv` (n=1.330) | 0,783 | 0,453 | **0,576** | — | — |
| `yoloe-26x` | `shel5k` (n=5.000) | 0,785 | 0,715 | — | 0,000 | 0,000 |
| `yoloe-26x` | `chv` (n=1.330) | 0,785 | 0,888 | 0,243 | — | — |

### Decisiones S2 que salieron de acá

1. **Campeón: `gdino-tiny-560`.** La resolución 560 da **−24% de latencia con igual o
   mejor mAP que 800** (doc 61; el −24% es inferencia batch sobre el BENCH — D-61.4 —
   no una medición live: `base-560` quedó **sin latencia live medida**, doc 101 §1).
   La variante 800 quedó descartada por dominancia. ✎ **2026-08-10 — el corolario, que
   hasta hoy era inferencia del lector: por eso NINGUNA variante 800 px se llevó al banco
   temporal** (decisión declarada en doc 64 §Decisiones S2). No es un hueco de cobertura:
   correr 800 en los clips habría medido una configuración **dominada** y roto la variable
   única de las campañas. Sigue siendo **trabajo futuro con causa**: doc 103 §7.4 lista
   "800 px" entre las mitigaciones **no medidas** para el colapso de `vest` a distancia.
2. **`gdino-base-560` es el especialista, con rol acotado, en dos ejes:**
   **`bare_head` (evidencia de CR-01)** — casi empate en `bench_obra` (0,400 vs
   0,369, n=65) que **se separa con claridad al sumar `shel5k`** (0,599 vs 0,308,
   n=5.313): no era ruido de denominador chico, es un efecto real — **y `vest`
   (CR-02)** (0,582 vs 0,520 en `bench_obra`; en video, SDR CR-02 0,281→0,920 — T2).
   (✎ 2026-08-06: *la etiqueta anterior "especialista CR-02/`bare_head`" mezclaba
   los dos ejes* — `bare_head` es evidencia de CR-01, no de CR-02.)
3. **La familia YOLOE no sirve para CR-01**: AP 0,000 en `bare_head` en las cuatro
   variantes medidas (26x/26l/26s/26m); recall CR-01 0,000 en `26x` (0,049 en `26s`).
   Es rápida (43 ms) pero ciega a la condición que importa.
4. **MM-Grounding-DINO descartado — la familia COMPLETA, sus tres variantes** (✎ 2026-08-10:
   *antes esta línea decía "en dos pasos" y nombraba solo `tiny` y `large`, omitiendo a
   `mm-gdino-base`, que sí se midió*): `tiny` excluido en Sprint 2 por bboxes degeneradas;
   `large` **roto** (mAP 0,017 en S1, con el sanity-check de bboxes que estaba
   pre-planificado "por si la familia reincide"); **`base` medido y mediocre** (mAP 0,360,
   recall CR-01 0,029, `bare_head` 0,00 — "sin ventaja en nada", hallazgo 5 del doc 64).
   Números en la tabla de descartes de §2.

> **Salvedad de lectura.** `vest` no tiene AP en `shel5k` y `bare_head` no lo tiene en
> `chv`: ninguna de las dos fuentes anota esa clase. Las celdas `—` son ausencia de
> GT, no rendimiento nulo.

## 3. Nivel A — estado por persona

Vive en **`results/bench_nivel_a/index.md`** (campaña D1, E-DIR vs E-IND). Resumen del
veredicto: el gate pre-registrado de `nucleo/04` §8 **no se dispara** (CR-01 ratio
0,34–0,46 sí cumple, CR-02 0,87 no, y el gate exige ambas) ⇒ E-DIR pasó a Fase 2, donde
el veto de precisión de Nivel B la descartó como núcleo (D1, doc 85).

**CR-02 a Nivel A no está cerrado**: se mide en un solo estrato (`bench_obra`, **n=82
violadores en la mitad B de test** — el estrato completo trae 142, pero la mitad A se
consume en calibración) y con IC solapados. Declarado, no disimulado.

## 4. Extensibilidad — el costo de una clase nueva (A1, doc 94)

El argumento que `nucleo/09` llama *"el más cuantificable"* y que exige medir, medido
sobre material con clases que la plataforma **jamás configuró**:

| Costo de agregar clases nuevas | Medido |
|---|---|
| Entrenamientos | **0** |
| Artefacto de configuración | **1 archivo, 48 líneas** (`prompts/clase_nueva_v1.yaml`, 5 clases) |
| Tiempo de pared del piloto completo | **9 minutos** |
| GT nuevo anotado | **0** (se reutilizó GT que `canonical_v2` nunca usó) |

| Medición | Valor | n |
|---|---|---|
| **`machinery` AP@0.5, zero-shot, jamás configurada** | **0,662** | 99 cajas GT |
| `person` vs `Worker` en MOCS (ancla cross-dataset) | 0,610 | 507 cajas GT |
| `excavator` con det ≥0,5 en MOCS | 62/151 imgs | sin GT (visual) |

**`machinery` zero-shot (0,662) supera el mAP50 agregado del campeón con las clases
configuradas** — tanto el rango sobre el mismo núcleo curado (0,447–0,503, doc 64,
que es la comparación que hace la fuente, doc 94) como el agregado de `bench_v3`
(0,551).

> **F-94.1, el hallazgo honesto que acompaña al número:** la palabra tiene que alinear
> con la taxonomía del despliegue. `vehicle` junto a `machinery` en el mismo caption da
> **0 detecciones** (inanición por solapamiento semántico, caso extremo de F-88.1);
> aislada da 118 cajas pero AP 0,026 porque **el 67% cae sobre lo que ese GT llama
> `machinery`** — no es que no vea, es que la palabra significa otra cosa en esa
> taxonomía. Versión más fuerte de A1: agregar la clase cuesta minutos **y validar la
> palabra también** — el bench lo expone en ~3 min, mientras que con un detector
> cerrado ese error se descubre después de anotar y entrenar.

## 5. Qué NO cubre este material

- **Nada temporal.** Estas métricas son espaciales por imagen; el aporte de la
  plataforma (histéresis, identidad, política de alerta) solo se mide sobre video —
  `results/clip_bench/`.
- **CR-02 a Nivel A en un solo estrato**, con IC solapados (§3).
- **Licencia de `chv` parcial**: cita obligatoria, imágenes no redistribuibles. Es el
  20,5% del bench.
- **`bench_obra` con n<30 por condición** en varios cortes: los contrastes de ese
  estrato son direccionales, no cuantitativos.

## 6. Dónde está cada número

| Qué | Dónde |
|---|---|
| Banco, composición y salvedades | `e-ovrt_datasets/datasets/registry/bench_v3.md` |
| Benchmark de modelos (crudo) | `docs/operacion/datos/31-benchmark-modelos-host-local.*` |
| Selección S1/S2 + confirmación B5 | `docs/operacion/64` (+ doc 61 para latencia/resolución) |
| Ampliación del bench y por-estrato | `docs/operacion/66` |
| Auditoría del BENCH original | `docs/operacion/63` |
| Nivel A (estado por persona) | `results/bench_nivel_a/` + `docs/operacion/83`, `84` |
| Piloto de clase nueva | `docs/operacion/94` + `datos/94-piloto-clase-nueva/` |

---

## Fuente: `e-ovrt_experimental-setup/results/bench_nivel_a/index.md`

> SHA-256 del bloque: `f3b9a09eac21b362c4fa0b727b94f22d8416bc4aeed656113523ba9cc5b3ca38`  
> Seleccion: documento completo.

# Campañas de Nivel A (estado por persona) — sobre imágenes **y sobre video**

Nivel A = **percepción**: se puntúa el estado "sin EPP" de cada persona contra
`has_helmet` / `has_vest`, sin motor de patrones ni tiempo. Es el nivel donde se
decide entre estrategias de prompts (`nucleo/04` §8); el Nivel B (alertas sobre
clips, `results/clip_bench/`) mide la plataforma alrededor del modelo.

> **Dos materiales, misma métrica.** La primera mitad de esta página es Nivel A sobre
> el **bench de imágenes** (campaña D1 — el eje E-DIR vs E-IND). La segunda es la misma
> métrica sobre **video** (campaña NA1, 17 clips), y es donde se ve el derrumbe de
> precisión en obra real. No mezclar los agregados: son materiales distintos.

**Cómo leer esta tabla.** Cada fila es el rendimiento medido de una combinación, no
una nota (marco del doc 81 §1). Umbrales calibrados en la **mitad A** de cada estrato,
métricas reportadas **solo sobre la mitad B**. Matching persona↔predicción IoU≥0,5
codicioso 1:1; una predicción sin persona del GT es FP.

## D1 — E-DIR vs E-IND (`d1_gdinotiny560_edir_vs_eind`, 2026-08-03)

Modelo `grounding-dino/gdino-tiny-560`. Variable única: el prompt set. E-IND corre en
su forma desplegada (3 clases en un caption); cada variante E-DIR corre **aislada**
en su propio caption. Detalle y caveats: `docs/operacion/83`.

### CR-01 (casco)

| Estrato | Brazo | P | R | F1 | IC95 recall | n+ |
|---|---|---|---|---|---|---|
| `bench_obra` | **E-IND** | 0,476 | 0,357 | **0,408** | [0,179–0,556] | 28 |
| `bench_obra` | `cr01_spec` | 0,200 | 0,179 | 0,189 | [0,043–0,370] | 28 |
| `bench_obra` | `cr01_neg` | 0,160 | 0,143 | 0,151 | [0,028–0,333] | 28 |
| `bench_obra` | `cr01_obs` | 0,097 | 0,250 | 0,140 | [0,100–0,471] | 28 |
| `shel5k` | **E-IND** | 0,464 | 0,662 | **0,546** | [0,628–0,697] | 2487 |
| `shel5k` | `cr01_obs` | 0,119 | 0,445 | 0,188 | [0,420–0,472] | 2487 |
| `shel5k` | `cr01_neg` | 0,083 | 0,232 | 0,123 | [0,211–0,255] | 2487 |
| `shel5k` | `cr01_spec` | 0,061 | 0,234 | 0,097 | [0,215–0,255] | 2487 |

### CR-02 (chaleco) — solo `bench_obra`

| Brazo | P | R | F1 | IC95 recall | n+ |
|---|---|---|---|---|---|
| **E-IND** | 0,567 | 0,415 | **0,479** | [0,243–0,644] | 82 |
| `cr02_obs` | 0,434 | 0,402 | 0,418 | [0,259–0,592] | 82 |
| `cr02_neg` | 0,359 | 0,451 | 0,400 | [0,311–0,646] | 82 |
| `cr02_spec` | 0,298 | 0,341 | 0,318 | [0,220–0,568] | 82 |

`shel5k` y `chv` no aportan CR-02: SHEL5K no anota chaleco y CHV solo permitiría
derivarlo por geometría, que sería circular con E-IND (D10, doc 83 F-83.3).

### Veredicto del gate (`nucleo/04` §8)

| Estrato / condición | ratio F1 E-DIR / E-IND | ¿< 50%? |
|---|---|---|
| `bench_obra` / CR-01 | 0,46 | sí |
| `shel5k` / CR-01 | 0,34 | sí |
| `bench_obra` / CR-02 | 0,87 | **no** |

**El gate no se dispara** — exige estar por debajo del 50% en **ambas** condiciones.
**E-DIR pasa a la Fase 2** (cadena completa sobre clips).

### Complementariedad (predicción pre-registrada: >15% ⇒ margen para E-HYB)

| Estrato / condición | E-IND falla | recupera E-DIR | fracción |
|---|---|---|---|
| `shel5k` / CR-01 | 840 | 155 | **18,5%** |
| `bench_obra` / CR-02 | 48 | 9 | **18,8%** |
| `bench_obra` / CR-01 | 18 | 1 | 5,6% (n insuficiente) |

**Contrastada en las dos condiciones** cuando el n alcanza.

### E-HYB Fase 1 offline (doc 12 §4: dual-run, gating por persona, sin params propios)

| Corte | E-IND F1 | **E-HYB-or F1** | corrobora TPs | corrobora FPs |
|---|---|---|---|---|
| `bench_obra`/CR-01 | 0,408 | 0,293 | 50% | 64% |
| `bench_obra`/CR-02 | 0,479 | **0,473** | 71% | **88%** |
| `shel5k`/CR-01 | 0,546 | 0,333 | **58%** | **24%** |

-or no supera a E-IND en ningún corte de Nivel A (la adopción §8.3 se decide en Fase 2
sobre F1 de alertas). La corroboración (-and) **discrimina 2,4× en CR-01** (la réplica
con `base-560` la refuerza: **3,0×, 51% vs 17%** — doc 84). ✎ 2026-08-06: la parte
"se invierte en CR-02" **no replicó** (doc 83, corrección del 08-04: con `base-560`
la dirección es la correcta, 50% TP vs 36% FP) — **CR-02 no tiene evidencia
concluyente en ninguna dirección**; la derivación correcta no es "factor por
condición" sino **medir la corroboración por condición antes de fijar el factor**.

## Hallazgos vigentes

- **F-83.4 — la formulación mueve el rendimiento, y cuánto depende de la condición.**
  E-DIR queda en 0,34–0,46 del F1 de E-IND en casco (dos estratos independientes, IC
  no solapados en `shel5k`) y en 0,87 en chaleco. Coherente con el caveat C1 del acta
  (doc 76): la debilidad del encoder con la negación era la hipótesis del eje.
- **F-83.5 — el eje ganador cambia con la condición, y la negación pura nunca gana.**
  `specificity` y `observable_state` se reparten el primer puesto según estrato y
  condición; `syntactic_negation` es el eje más débil de los tres en todos los cortes.
- **F-83.6 — E-DIR no es un detector, pero es un recuperador.** `cr01_obs` en `shel5k`
  rinde F1 0,188 (precision 0,119, 8.212 FP) y aun así recupera el 18,5% de lo que
  E-IND no ve. El costo de E-DIR es precision, no recall.
- **F-83.7 — la corroboración discrimina en CR-01.** (✎ título vigente tras la
  corrección del 2026-08-04, doc 83 §✎; *decía "…y se invierte en CR-02"*, parte que
  **no replicó** con `base-560` y quedó sin evidencia concluyente.) Los FP de
  `cr01_obs` son 54% ceguera al atributo + 46% alucinación (el gating filtra solo lo
  segundo). En casco E-DIR corrobora aciertos 2,4× más que errores (réplica: 3,0×,
  51% vs 17% — doc 84). En chaleco, medir por condición antes de fijar cualquier
  `corroboration_factor`.

## Limitación abierta

**CR-02 no está cerrado.** Vive en un solo estrato con 82 positivos y sus IC se
solapan con los de E-IND: el 0,87 alcanza para que el gate no se dispare (es un
umbral, no una prueba de significancia) pero **no** para afirmar que las estrategias
empatan en chaleco. Haría falta otra fuente con negativos de chaleco explícitos.

## Campañas de Fase 2 que salieron de acá (todas resueltas — ver `results/clip_bench/`)

| Combinación | Resolución |
|---|---|
| ~~Fase 2 (Nivel B): E-DIR sobre el clip bench~~ | **HECHA (D1, doc 85)**: precision 0,146 < 0,5 ⇒ **veto del §8, E-DIR descartada como núcleo**; el ratio F1 cae de 0,34–0,46 (Nivel A) a 0,20 — la brecha se agranda con la plataforma (F-85.4: el ranking de Nivel A no transfiere) |
| ~~Fase 2: fusión `hyb_or`~~ | **HECHA (H1, doc 87)**: predicción refutada — recall 0,824→0,353; F-87.2: la unión de evidencia NO es monótona en un motor temporal |
| ~~Fase 2: fusión `hyb_and`~~ | **No ejecutada CON CAUSA (D-90.4)**: no es medible contra este banco sin romper la comparabilidad de las 6 campañas (el evaluador deriva la ventana de la persistencia nominal del GT); predicción y condición de medición escritas (doc 87 §5) |
| ~~`gdino-base-560` réplica Nivel A + T2 clips~~ | **HECHA (doc 84)**: F-84.1 estructural, F-84.5/F-84.6 en clips |
| ~~`bare_head` como evidencia directa × base-560 (Nivel B)~~ | **HECHA (B1, doc 88)**: F-88.2 — tampoco alcanza (0,480 vs 0,582 sobre las mismas detecciones); de yapa F-88.1 (costo del caption: 0,082 de F1 por una palabra) y F-88.3 (la etiqueta corta gana a la frase negada) |

## Nivel A sobre CLIPS de video — `na1_gdinotiny560_v2short_video` (gen. 3, 2026-08-09)

Nivel A sobre **video real**, contra el GT humano de CVAT. Consolida los **17 clips de
video con GT**: los **13 del estrato B** (lote de internet CERRADO, doc `operacion/111`)
y los **4 del piloto** del 2026-07-18. Artefactos en
`na1_gdinotiny560_v2short_video/metrics.json`.

**NO es comparable fila a fila con D1**: acá NO hay calibración de umbrales (punto de
operación **desplegado**: person ≥ 0,35, evidencia ≥ 0,25), el material es video
sub-muestreado a 2 Hz, y las **person-frames con `unknown` se excluyen del denominador**
— el ratio de exclusión se reporta y es un resultado en sí.

> **⚠️ REGLA DECLARADA (fijada 2026-08-09, decisión D-113.2, doc `operacion/113` §D):**
> la persona `unknown` sale del **denominador** (no es evaluable, no hay estado que
> juzgar), pero **si el modelo predice una violación sobre esa misma persona, esa
> predicción SÍ cuenta como FP en el numerador**. Es una decisión deliberada, no una
> asimetría accidental: **la alerta sobre una persona no juzgable suena igual** — un
> supervisor la recibiría como una falsa alarma real, independientemente de que el
> anotador no haya podido determinar el estado. Medido sobre los 4 clips piloto (mismas
> detecciones, mismo GT, única variable la regla): **48% de los FP de CR-01 (91/190) y
> 22% de los de CR-02 (77/346)** son predicciones sobre personas `unknown`. La regla
> alternativa (excluir también del numerador, simétrica al denominador) subiría la
> precision CR-01 de 0,0052 a 0,0100 con el recall intacto — **se evaluó y se descartó**:
> las cifras de esta tabla y de la fila de arriba del piloto (doc `operacion/105`) usan
> la regla declarada, no la alternativa.

> **✎ 2026-08-09 — RE-PUNTUADO tras la revisión ciega del GT (doc `operacion/113` §B).**
> Las correcciones firmadas de `v04_c02` (ambos atributos del sujeto en cabina →
> `unknown`) y `v01_c01` (casco a contraluz → `unknown`) cambian el GT de atributos.
> Mismas detecciones, mismo stride; solo se re-corrió el scorer. **El recall SUBE**
> (los violadores no observables salieron del denominador) **y la precision baja** (las
> predicciones sobre esas personas ahora-`unknown` cuentan como FP, regla D-113.2).
> Cifras anteriores (0,039 / 0,020) supersedidas; evidencia en
> `docs/operacion/datos/113-nivel-a-consolidado-post-revision.json`.

| material | CR-01 P / R / F1 | CR-02 P / R / F1 | unknown | n eval |
|---|---|---|---|---|
| `bench_obra` (imágenes, referencia de arriba) | 0,476 / 0,357 / **0,408** | 0,567 / 0,415 / **0,479** | — | — |
| **video, agregado (17 clips)** | 0,016 / 0,467 / **0,031** | 0,009 / 0,318 / **0,018** | 12,0% / 12,0% | 10.356 / 10.361 |
| — solo estrato B (13) | 0,017 / 0,472 / 0,032 | 0,003 / 0,300 / 0,006 | 11,6% / 11,3% | 9.650 / 9.682 |

### Las celdas que se destacan

| clip | cond | violadores | P | R | **F1** | por qué |
|---|---|---|---|---|---|---|
| `video15_clip01` | CR-02 | 49 | 0,312 | 0,490 | **0,381** | el mejor del conjunto — **0% unknown**, material plenamente juzgable |
| `v01_c02` | CR-01 | 32 | 0,216 | 0,594 | **0,317** | el mejor del estrato B |
| `v04_c01` | CR-01 | 28 | 0,132 | 0,714 | 0,223 | **el recall más alto** (0,714), con 55% de unknown |
| `v06_c01` | CR-02 | 10 | 0,001 | 0,300 | **0,002** | el peor — 3.173 FP sobre 6.442 person-frames |

> ✎ **2026-08-09:** la fila de `v01_c01` CR-01 (recall 0,846 con 13 violadores) salió
> de esta tabla: la corrección firmada del track 9 (casco a contraluz → `unknown`) dejó
> al clip con **2 person-frames violadoras residuales de tracks fugaces** (0 tp, 109 fp)
> — su "recall altísimo" medía en gran parte al sujeto que resultó no juzgable.

**Lectura (docs 103/104/105/108/111):** el mismo E-IND que da F1 0,41–0,55 en imágenes
se derrumba en video far-field **por precision, no por recall** (el recall agregado se
sostiene en 0,47 / 0,32 tras la revisión del GT — de hecho SUBIÓ al salir del
denominador los violadores no observables). Es la medición canónica del mecanismo "ausencia de evidencia =
evidencia de ausencia" fuera del régimen de juzgabilidad. Hallazgos: **F-105.3** — la
juzgabilidad tiene tres ejes (escala × iluminación × **oclusión**) — y **F-105.4** — el
`unknown` del anotador **no** predice el F1 del modelo: el humano usa continuidad
temporal que el modelo por frame no tiene, y esa brecha señala **agregación temporal de
evidencia para determinar estado** como vía de mejora.

## Artefactos y procedencia de esta familia (✎ declarados 2026-08-09)

| Campaña | Artefactos | Nota |
|---|---|---|
| `d1_gdinotiny560_edir_vs_eind` | `metrics.json` · **`metrics_base560_replica.json`** · `provenance_runs.json` (18 corridas) | La réplica **está VIGENTE**, no es una generación supersedida: es la misma corrida (seed `20260803`, misma partición y grids) repetida con **`gdino-base-560`** — doc `operacion/84`, sostiene F-84.3/84.4 y la corrección a F-83.7. **Ojo: el JSON no declara su modelo por dentro** (claves raíz `seed`/`strata`/`gate`/`complementarity`); la atribución vive en el bloque `replica_secundaria` de su `campaign.yaml`. Cifras ancla: `shel5k` CR-01 **0,4958**, `bench_obra` CR-02 **0,5828** |
| `na1_gdinotiny560_v2short_video` | `metrics.json` · `provenance.json` (17 corridas) | **✎ `provenance.json` se generó el 08-09** (`docs/operacion/datos/113-regenerar-provenance-estrato-b.py`): antes esta campaña era la única sin procedencia por corrida. **No tiene `evals/` por diseño**: a Nivel A no interviene el motor temporal, así que no hay "eval por clip" — el detalle vive en `metrics.json/por_clip` |

> **`provenance.json` y `provenance_runs.json` son el mismo artefacto con distinto
> nombre** (`informe/99` §2.4 los pone en la misma fila): cambia la unidad que indexan
> — un clip en `clip_bench`, una corrida de inferencia en `d1`.

---

## Fuente: `e-ovrt_experimental-setup/results/clip_bench/index.md`

> SHA-256 del bloque: `cf55f1c60e9674432a06a28e54134012c43a11af8e6501aecf0e30d5e5aa534f`  
> Seleccion: documento completo.

# Campañas sobre el banco de clips — tabla comparativa

Banco: **34 clips** del rodaje (Bloque A, 2026-07-25), 35 episodios (CR-01 28 /
CR-02 7), P1–P9, `manifest.yaml` sha256 `cef5082e…` — **ese sha es el freeze de 34
que usaron todas las campañas de esta tabla**, recuperable en el commit `f7a27fe6` de
`e-ovrt_datasets`. El banco **vigente** (✎ 2026-08-09) tiene **47 clips** — 34 del
rodaje (Bloque A) + **13** del estrato B (Bloque B), **32 positivos / 15 negativos /
37 episodios** (CR-01 30 / CR-02 7), manifest `manifest.yaml` sha256 `3f14f50a…`.
**Las filas del rodaje nunca cambiaron**: tanto las altas del estrato B como la
revisión ciega del GT del 08-09 (doc `operacion/113` §B) ocurrieron enteramente en el
Bloque B. El estrato B tiene su propia sección al final. **Denominador citable: 34
episodios evaluables sobre 35** — 1 censurado con causa
(`clip_too_short_for_t_alert_window`, un CR-01 de P1; enmienda A2): todos los
recall de esta página son sobre 34 (T1 28/34 = 0,824; G1 33/34 = 0,971 — quien
recomponga 28/35 no reproduce la tabla). Limitaciones comunes a todas las
campañas: `e-ovrt_datasets/datasets/registry/clip_bench.md` (L1–L5).

**Cómo leer esta tabla.** Cada fila es el rendimiento medido de UNA combinación,
no una nota. La pregunta de la tesis es *qué se consigue hoy con OVD sin
entrenar en construcción civil* — el contraste entre filas **es** el
experimento. Recall/precision son **micro** (por episodio) sobre episodios
evaluables; los clips negativos quedan fuera y se reportan como control de FP.

| # | `campaign_id` | Modelo | Prompts | Gran. | Recall | Prec. | F1 | t_alert | TTFD | SDR | FP neg. | Hallazgo |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| T1 | `t1_gdinotiny560_v2short_scene` | gdino-tiny-560 | `v2_short` | scene | **0,824** | **0,757** | **0,789** | 5.327 ms | 168 ms | 0,698 | **0/4** | Línea de base. P1/P2/P4/P6 recall 1,000 con 1 FP; P7/P8/P9 concentran 6 missed y 8/9 FP |
| T2 | `t2_gdinobase560_v2short_scene` | **gdino-base-560** | `v2_short` | scene | 0,735 | 0,676 | 0,704 | **4.899 ms** | 221 ms | **0,819** | **0/4** | Contraste de modelo. **F-81.2b REFUTADA**: el especialista no recupera P7 (0,400=) ni P8 (0,500=) y empeora P9 (0,600→0,400). **Pero CR-02 SDR 0,281→0,920** y su t_alert −2,2 s |
| D1 | `d1_gdinotiny560_edirpair_scene` | gdino-tiny-560 | **`edir_v1` (par)** | scene | **0,176** | **0,146** | **0,160** | 6.611 ms | 847 ms | 0,210 | **2/4** | **Fase 2 del eje: E-DIR de punta a punta.** Precision 0,146 < 0,5 → **veto del §8: E-DIR descartada como núcleo, E-IND confirmada.** Ratio F1 0,20 (vs 0,34–0,46 en Nivel A: la brecha se AGRANDA con la plataforma). CR-02 recall **0,000**. Único escenario donde gana: **P9 0,800 vs 0,600** |
| H1 | `h1_gdinotiny560_hybor_scene` | gdino-tiny-560 | **fusión dual-run T1+D1** | scene | 0,353 | 0,255 | 0,296 | 6.956 ms | **113 ms** | **0,738** | 2/4 | **E-HYB-or. Predicción pre-registrada REFUTADA**: el recall no sube, se derrumba (0,824→0,353). **F-87.2: la unión de evidencia NO es monótona en un motor temporal** — evidencia más temprana no agrega alertas, *corre* las que ya había fuera de su ventana. P1 pasa de 1,000/0 FP a **0,000/12 FP** con la percepción MEJORADA (SDR 0,738, TTFD 113 ms). **Sin GPU** |
| **G1** | `g1_gdinotiny560_v2short_subject` | gdino-tiny-560 | `v2_short` | **subject** | **0,971** | **0,892** | **0,930** | 5.236 ms | 168 ms | 0,698 | **0/4** | **La mejor combinación del banco.** Única variable vs T1: la granularidad — **SDR y TTFD idénticos** (las detecciones son bit a bit las de T1), así que los **+0,141 de F1 vienen enteros del motor**. **P7 de 0,400 a 1,000** (F-89.1 cierra F-81.2a); prematuras de pre-roll 5→1 (F-89.2). **Sin GPU**, 0,4 min. La identidad es capacidad de plataforma (`input.track_persons`, DBE+live): el camino config-driven reproduce esta campaña **exacto** |
| B1 | `b1_gdinobase560_barehead_scene` | gdino-base-560 | **`bench_v2` (4cl), `bare_head` directo** | scene | 0,382 | 0,371 | 0,377 | **3.919 ms** | **41 ms** | **0,940** | **3/4** | **F-88.2**: la vía que T2 no probó tampoco alcanza — 0,480 vs 0,582 de la ausencia espacial **sobre las mismas detecciones** (CR-01 puro). **F-88.1**: su control interno mide el **costo del caption** — una clase más cuesta **0,082 de F1** (T2 0,704 → 0,622). Mejor percepción del banco (SDR 0,940) y peores negativos |

## Detalle por escenario

| `campaign_id` | P1 | P2 | P3∅ | P4 | P5∅ | P6 | P7 | P8 | P9 |
|---|---|---|---|---|---|---|---|---|---|
| **G1** | 1,000 | 1,000 | 0 FP | 1,000 | 0 FP | 1,000 | **1,000** | **1,000** | **0,800** |
| T1 | 1,000 | 1,000 | 0 FP | 1,000 | 0 FP | 1,000 | **0,400** | **0,500** | **0,600** |
| T2 | 0,818 | 1,000 | 0 FP | 1,000 | 0 FP | 1,000 | **0,400** | **0,500** | **0,400** |
| D1 | 0,091 | 0,000 | 2 FP | 0,500 | 0 FP | 0,000 | 0,000 | 0,000 | **0,800** |
| H1 | **0,000** | 1,000 | 2 FP | 0,000 | 0 FP | 0,500 | 0,400 | 0,000 | 0,600 |
| B1 | 0,273 | 0,000 | 2 FP | 1,000 | 1 FP | 0,250 | 0,200 | 1,000 | 0,800 |

(∅ = escenario negativo: se reporta FP, no recall. Fila B1 agregada 2026-08-06 —
regla L5: ninguna campaña sin su desglose. Ojo con los `n` chicos: P2 = 5
episodios, P6 = 2 clips / 4 episodios, P8 = 1 clip.)

## Detalle por condición

| `campaign_id` | CR-01 SDR | CR-01 t_alert | CR-01 FP | CR-02 SDR | CR-02 t_alert | CR-02 FP |
|---|---|---|---|---|---|---|
| T1 | 0,805 | 4.314 ms | 8 | **0,281** | 8.572 ms | 1 |
| T2 | 0,804 | 4.364 ms | 11 | **0,920** | **6.417 ms** | 1 |
| D1 | 0,252 | 6.611 ms | **27** | **0,020** | — (recall 0) | **14** |
| H1 | 0,854 | 5.081 ms | 24 | 0,282 | 9.167 ms | 13 |
| G1 | 0,805 | 4.331 ms | **3** | **0,281** | 8.572 ms | 1 |
| B1 | 0,940 | 3.919 ms | 14 | 0,966 | 3.867 ms | 9 |

(CR-01 = 28 episodios / 25 clips; CR-02 = 7 episodios / 7 clips, en todas. Filas
H1/G1/B1 agregadas 2026-08-06 desde sus `metrics.json` — regla L5. **Dos
advertencias de lectura:** (1) los FP se imputan a las condiciones *presentes* en
el clip, con solapamiento — la suma por condición puede superar el total de la
campaña (D1: 27+14 = 41 vs 35 totales); (2) `by_condition` no trae recall — el
recall por condición vive en los docs de campaña: en T1 **CR-02 confirma 7/7 =
1,000 pese a SDR 0,281** (F-81.1, doc 81), la cifra que sostiene el argumento de
la histéresis.)

## `t_alert` = `t_alert-system` — equivalencia de nombres y regla de cita (✎ 2026-08-15)

La columna **`t_alert`** de las tablas de arriba **es la métrica `t_alert-system` del
diccionario de la spec 40 §5.1**: el mismo campo `t_alert_system_ms` de los `metrics.json`
de cada campaña (`positives`, `by_condition`, `by_clip`), que a su vez es passthrough de
`avg_latency_ms_from_episode_start` de `evaluate-alerts` (control-plane). Mide **desde el
inicio anotado del episodio en el GT hasta la alerta registrada** — o sea que incluye la
persistencia del patrón por diseño (`t_alert ≈ persistencia + TTFD + intermitencia`, F-81.3).

**Citabilidad, decidida el 2026-08-15 (doc `operacion/119` §7.3):**

- **Citable por campaña y por condición**, desde estas tablas o desde el `metrics.json`
  correspondiente. **Nunca** promediada entre campañas, y **nunca** comparada entre
  densidades sin control de supervivencia (F-96.5: el agregado esconde sesgo de
  supervivencia — al degradarse el recall, los episodios difíciles salen de la muestra).
- En `report.json` de corridas nuevas la métrica aparece como `t_alert-system`
  (`computed` cuando hay evaluación temporal con GT; estados con causa en el resto).
  Los 232 reports consolidados anteriores al 2026-08-13 la muestran `not_applicable`
  porque son previos al cambio: **la fuente citable para las campañas de este índice son
  estos `metrics.json`**, no aquellos reports.
- `precision_alertas` / `recall_alertas` / `F1_alertas` de `report.json` **no son
  citables**: duplican las cifras de `evaluate-alerts` que este índice ya publica con
  denominadores por estrato.

**No confundir los dos nombres del diccionario:** `t_alert-system` (este — episodio→alerta,
dentro de la plataforma) ≠ **`t_alert-notification`** (bus de alertas→PUBACK MQTT, el tramo
de distribución: campaña propia en
`../realtime/t_alert_notification/` (fuente: `e-ovrt_experimental-setup/results/realtime/t_alert_notification/README.md`), p95
64,534 ms n=460). Son tramos disjuntos de la cadena y no se suman percentiles entre ellos.

## Mecanismo de las alertas inesperadas (`datos/85-mecanismo-de-fallas.py`)

| Tipo | T1 | T2 | D1 | H1 | I1 † | I2 † |
|---|---|---|---|---|---|---|
| `prematura_pre_roll` | 5 | 6 | 14 | **20** | 2 | **117** |
| `cruzada_de_condicion` | 4 | 4 | 8 | **14** | 3 | 79 |
| `sin_episodio_activo` | 0 | 2 | **12** | 3 | 2 | 20 |
| `tardia` | 0 | 0 | 3 | 0 | 0 | 0 |
| adelanto mediano de prematuras | 0,5 s | 1,8 s | 2,5 s | **2,6 s** | 341,9 s | **221,2 s** |

† Columnas del estrato B agregadas 2026-08-06 — **NO comparar con las del rodaje sin
la nota F-107.4** (doc `operacion/107`): en clips largos la taxonomía satura — el
adelanto mediano de las "prematuras" de I2 es **221 s**, no medio segundo: la etiqueta
técnica aplica pero el mecanismo es *otra persona fabricando la misma condición
minutos antes del episodio*, la firma de la evidencia fabricada del doc 103.

## Hallazgos vigentes

- **F-81.1 — la histéresis del motor rescata una percepción intermitente.** CR-02
  llega a recall 1,000 con SDR 0,281 (0,160 en P2 puro): la evidencia de chaleco
  aparece en ~1 de cada 6 frames del episodio (F-G2.1 medido de punta a punta) y
  el patrón temporal la acumula igual, pagando tiempo (t_alert 8.572 vs 4.314 ms
  de CR-01). Argumento pro-plataforma medido — y a la vez el techo: con SDR ~0,16,
  exigir continuidad estricta rompería CR-02.
- **F-81.2 — dónde se rompe la combinación actual.** (a) Granularidad de escena
  vs GT por sujeto en multitud (P7): el GT exige que UN sujeto sostenga 4 s y el
  motor acumula "alguien sin casco"; es el costo de operar sin `track_id`, ahora
  medido → insumo directo del experimento G1 (doc 79). (b) Mis-detección de casco
  en el pre-roll (P7/P9): la alerta cae 0,7–2,4 s antes del episodio porque el
  modelo no ve el casco durante los ~3 s de cumplimiento inicial → candidato a
  prompts de Fase D o a `gdino-base-560` (especialista CR-01, doc 64).
- **F-81.3 — TTFD ~5 frames.** La latencia de la plataforma es la política de
  persistencia, no la percepción: `t_alert ≈ persistencia + TTFD + intermitencia`.
- **F-84.5 — F-81.2b refutada para la palanca "cambiar de modelo bajo `v2_short`".**
  El especialista no recupera el pre-roll: P7 0,400=, P8 0,500=, **P9 empeora**
  (0,600→0,400); mecanismo clasificado contra el GT (`datos/85-mecanismo-de-fallas.py`):
  las prematuras de pre-roll pasan de 5 a 6, pero **su adelanto mediano se triplica**
  (0,5 s → 1,8 s) — con tiny caían al filo del borde, con base caen adentro del tramo
  que el GT marca "cumple"; los FP cruzados de condición quedan idénticos en 4 (la
  granularidad no depende del modelo). **Alcance**: la "especialidad CR-01" del doc 64 se midió
  detectando **`bare_head`**, clase que `v2_short` no incluye — T2 nunca la ejercitó.
  La vía `bare_head`-como-evidencia-positiva (base: recall 0,599 vs 0,308 de tiny)
  sigue sin probar a Nivel B y requiere el evaluador `direct_evidence` — la misma
  pieza que la Fase 2 de E-DIR. Palancas restantes para P7–P9: `track_id`/G1 y
  evidencia directa.
- **F-84.6 — el modelo sí compra percepción de chaleco, y la plataforma cobra menos
  tiempo.** CR-02 pasa de SDR **0,281 → 0,920** (la evidencia intermitente de F-81.1,
  ~1 de cada 6 frames, se vuelve continua) y su `t_alert` baja **8.572 → 6.417 ms**.
  El recall de CR-02 ya era 1,000 en T1 gracias a la histéresis, así que la mejora no
  puede verse ahí: se ve en calidad de evidencia y en latencia. **Son dos palancas
  independientes** — la histéresis rescata la percepción pobre (F-81.1) y el modelo
  la elimina como problema. El precio es CR-01: recall global 0,824→0,735.

- **F-85.3 — la histéresis es una palanca de doble filo, medida en los dos sentidos.**
  F-81.1: el motor **rescata** percepción intermitente pero correcta (CR-02 con SDR
  0,16 llegaba a recall 1,000). D1: el motor **amplifica** percepción persistente pero
  equivocada — E-DIR dispara sobre gente que cumple, la evidencia errónea es sostenida
  y la persistencia la confirma: 35 FP contra 9, y **2 FP en negativos** (T1/T2 tenían
  0/4). La histéresis solo mide persistencia; no distingue "débil pero correcta" de
  "fuerte pero equivocada".
- **F-85.4 — el ranking de Nivel A no transfiere a Nivel B.** CR-02 era el punto
  **fuerte** de E-DIR en imágenes (ratio 0,87) y es donde **colapsa** en video (recall
  0,000, SDR 0,020); CR-01 al revés. Por eso el pre-registro exige las dos fases y
  decide en la segunda.
- **F-85.5 — P9 es la única victoria de E-DIR y está donde E-IND es más débil**
  (0,800 vs 0,600, con menos FP). Coherente con la complementariedad de Nivel A
  (18,5%): ubica a E-HYB en el pre-roll, no "en general".

- **F-87.2 — la unión de evidencia NO es monótona en un motor temporal.** En una
  clasificación por frame un OR solo puede agregar positivos. Acá no se clasifican
  frames: se **confirman episodios**, con ventana de persistencia y de matching.
  Evidencia más temprana no agrega una alerta — **corre la que ya existía**, y una
  alerta adelantada fuera de la ventana cuenta doble mal (missed + unexpected). Firma
  inequívoca: los 11 clips de P1 confirman en H1 a **~4,0 s exactos** = `confirm_after_ms`
  contado desde el frame 0, porque la evidencia directa está desde el primer frame; con
  E-IND sola confirmaban a `onset + 4,0 s` ≈ 7,6 s, dentro de la ventana. P1 pasa de
  1,000/0 FP a 0,000/12 FP **con la percepción mejorada** (SDR 0,698→0,738, TTFD
  168→113 ms). Es el tercer filo de F-85.3: la evidencia equivocada *temprana* no solo
  agrega falsas alarmas, **canibaliza las alertas correctas**.

- **F-88.1 — el caption tiene un costo medido, y responde una pregunta abierta del
  pre-registro.** T2 y el control interno de B1 comparten modelo, evaluador, pattern
  set, GT y timings; **difieren en una palabra del caption** (`bare head`) y eso cuesta
  **0,082 de F1** (0,704 → 0,622). El doc 12 §4.1 dejaba el pase único de vocabulario
  unión como "variante operativa condicionada si la interacción es despreciable":
  **no lo es**. La regla dual-run queda validada empíricamente y el atajo de un solo
  pase no es gratis.
- **F-88.3 — la etiqueta corta gana a la frase negada, y eso ordena el eje.** Sobre los
  23 clips de CR-01 puro: ausencia espacial con `helmet` **0,582–0,731**, `bare head`
  (evidencia directa pero **etiqueta corta**) **0,480**, frases negadas de E-DIR
  **0,231**. La ventaja de E-IND no es "inferir es mejor que detectar": es que su
  vocabulario está hecho de etiquetas cortas que el modelo entiende. `bare_head` cae en
  el medio exacto, y esa posición intermedia es la evidencia más limpia de que **lo que
  manda es cómo se expresa la condición, no si se infiere o se detecta**.

- **F-89.1 / F-89.2 — el margen que quedaba no estaba en el modelo ni en los prompts,
  estaba en la identidad del motor.** Cuatro palancas de percepción y formulación (D1
  0,160 / H1 0,296 / T2 0,704 / B1 0,377) no superaron a T1 (0,789); **la granularidad
  por sujeto sí: 0,930**, con **SDR y TTFD idénticos** a T1 porque las detecciones son
  bit a bit las mismas. P7 pasa de 0,400 a 1,000 (cierra F-81.2a) y las prematuras de
  pre-roll caen de 5 a 1 — lo que **refina F-81.2b**: bajo escena basta que CUALQUIER
  persona esté sin casco para que la escena entre en evidencia durante el pre-roll en
  que el sujeto objetivo sí cumple. No era que el modelo no viera el casco: **era que
  el motor miraba a otra persona**. Verificado que no es artefacto: en P7 ambas
  campañas emiten **las mismas 7 alertas**, pero G1 acierta 5 en vez de 2 y baja FP de
  5 a 1.

## Comparación restringida a CR-01 puro (23 clips, 25 episodios)

El agregado penalizaría a `bare_head` por episodios CR-02 que su pattern set no puede
detectar por diseño. Comparación justa:

| Campaña | recall | precision | F1 |
|---|---|---|---|
| **T1** (tiny, 3cl, E-IND) | **0,760** | **0,704** | **0,731** |
| T2 (base, 3cl, E-IND) | 0,640 | 0,593 | 0,615 |
| B1-eind (base, 4cl, E-IND) | 0,640 | 0,533 | 0,582 |
| B1 `bare_head` (base, 4cl, directo) | 0,480 | 0,480 | 0,480 |
| D1 (E-DIR frases) | 0,240 | 0,222 | 0,231 |
| H1 (hyb_or) | 0,200 | 0,185 | 0,192 |

## Veredicto del eje (nucleo/04 §8, criterios fijados antes de correr)

Las tres estrategias del pre-registro, corridas de punta a punta sobre el mismo banco,
GT, motor y timings:

| Estrategia | F1 de alertas | Veredicto |
|---|---|---|
| **E-IND** | **0,789** | **Núcleo** (ADR-001, confirmado por medición) |
| E-DIR | 0,160 | Descartada — **veto de precisión** del §8 (0,146 < 0,5) |
| E-HYB-or | 0,296 | No supera a la mejor individual (§8.3 exige ≥0,05 por encima) |

No hacen falta desempates: la brecha con E-IND es de 0,63 y 0,49 en F1. Las estrategias
no elegidas quedan documentadas con sus números (§8 criterio 4). **La brecha se agranda
al pasar por la plataforma**: E-DIR tiene ratio F1 0,20 a Nivel B contra 0,34–0,46 a
Nivel A. Y las tres fallas están **explicadas por mecanismo**, no solo cuantificadas:
ceguera al atributo (Nivel A), su amplificación por la histéresis (D1) y la no-monotonía
de la unión (H1).

`hyb_and` **no se implementó, con causa y predicción registrada**. La causa vigente es
**D-90.4** (2026-08-05, doc 90 §hyb_and): **no es medible contra este banco sin romper
la comparabilidad de las 6 campañas** — el evaluador deriva la ventana de la
persistencia nominal del GT, y `-and` la altera. El planteo original (doc 87 §5: su
único efecto declarado es *acelerar* la confirmación, y F-87.2 muestra que adelantar
es justamente el mecanismo de falla) queda archivado como predicción conservada.
Salida legítima del pre-registro (§6.2: "lo no corrido se reporta *no ejecutada con
causa*").

## Eje de densidad de evidencia — el costo del tiempo real (R1–R6, doc 96)

**Estas filas NO van en la tabla de arriba a propósito.** Aquélla compara combinaciones
a `stride: 1`; ésta varía la *cadencia*, y el SDR **no es comparable entre cadencias**
(F-96.6: la subida del SDR al bajar la densidad es ~100% artefacto del instrumento —
`_sdr_for_episode` funde huecos ≤ paso nominal, y el paso nominal crece con el stride).
Mezclarlas invitaría justo a esa lectura equivocada.

Las seis campañas del banco corrieron todas a 30 fps de evidencia; el camino live
entrega 1,16–4,42 fps (docs 71/73). Estas seis miden qué sobrevive a esa restricción.
Variable única contra T1/G1: el `stride`.

| # | `campaign_id` | Gran. | fps ev. | Ancla del live | Recall | Prec. | F1 | t_alert | TTFD | FP neg. |
|---|---|---|---|---|---|---|---|---|---|---|
| T1 | `t1_…_scene` | escena | 30,00 | (referencia DBE) | 0,824 | 0,757 | **0,789** | 5.327 ms | 168 ms | 0/4 |
| R1 | `r1_…_scene_s7` | escena | **4,29** | ancla del techo live (stride 7) | 0,794 | 0,794 | **0,794** | 5.623 ms | 572 ms | 0/4 |
| R3 | `r3_…_scene_s15` | escena | **2,00** | lo que corrió en el rodaje | 0,706 | 0,774 | **0,738** | 4.846 ms | 870 ms | 0/4 |
| R5 | `r5_…_scene_s26` | escena | **1,15** | ancla del peor caso (stride 26) | 0,618 | 0,677 | **0,646** | 5.360 ms | 1.463 ms | 0/4 |
| G1 | `g1_…_subject` | sujeto | 30,00 | (referencia DBE) | 0,971 | 0,892 | **0,930** | 5.236 ms | 168 ms | 0/4 |
| R2 | `r2_…_subject_s7` | sujeto | **4,29** | ancla del techo live (stride 7) | 0,853 | 0,879 | **0,866** | 5.635 ms | 572 ms | 0/4 |
| R4 | `r4_…_subject_s15` | sujeto | **2,00** | lo que corrió en el rodaje | 0,824 | 0,933 | **0,875** | 4.981 ms | 870 ms | 0/4 |
| R6 | `r6_…_subject_s26` | sujeto | **1,15** | ancla del peor caso (stride 26) | 0,676 | 0,821 | **0,742** | 5.577 ms | 1.463 ms | 0/4 |

Anclas: los strides son 30/7 ≈ 4,29 y 30/26 ≈ 1,15 fps **nominales** — el techo
medido fue 4,42 fps con F-RT5 (4,12 hoy, doc 101) y el peor caso medido 1,16 fps
(20:10). **R4 (0,875) > R2 (0,866) pese a tener la mitad de densidad: es ruido, no
una inversión — se declara, no se explica (doc 96 §7).**

**Lo que dicen estas filas (verificadas con bootstrap pareado por clip, doc 96 §4.1):**

- **F-96.4 (el central): la ganancia de la identidad sobrevive al tiempo real y
  excluye el cero en las CUATRO densidades** — sujeto−escena: +0,141 [+0,032,+0,258]
  a 30 fps, +0,072 [+0,013,+0,145] a 4,29, +0,137 [+0,032,+0,258] a 2,00, +0,096
  [+0,011,+0,202] a 1,15. Es la única palanca del banco significativa a la densidad
  del live de hoy. El tracker NO se fragmenta (tracks 154→103/91/105). La comparación
  cruzada "R2 (0,866) > T1 con 30 fps (0,789)" es **estimación puntual** (IC
  [−0,071,+0,229]), se reporta como consistente, no como hallazgo.
- **F-96.1: a ~4 fps el agregado no se degrada de forma detectable** (+0,005
  [−0,120,+0,132]), pero esconde una redistribución: P2 cae 1,00→0,60 y P6 1,00→0,50,
  mientras **P9 sube 0,60→1,00 con 2 FP menos**. Los deltas de densidad del agregado
  **de escena** NO excluyen el cero (ni R5−T1 −0,143); bajo **sujeto** el peor caso
  **sí**: R6−G1 = −0,188 [−0,334, −0,040] es el único costo de densidad
  individualmente significativo (doc 96 §4.1). Para escena, el costo queda como
  tendencia monótona con mecanismo identificado, no como efecto establecido.
- **F-96.2: lo primero que se rompe es el rescate de F-81.1.** CR-02 vive de que la
  histéresis acumule percepción intermitente (SDR 0,281); P2 pasa a 0,600 y luego a
  0,200. Límite declarado de F-81.1: la histéresis rescata mientras la cadencia
  alcance para muestrear. La identidad no lo arregla — es percepción, no atribución.
- **F-96.5 (✎ corregido en revisión adversarial): el `t_alert` agregado quieto era
  un artefacto de supervivencia** — los episodios lentos mueren como `missed` y su
  salida baja el promedio. Entre supervivientes comunes, t_alert crece **+0,7 a
  +1,3 s**. El costo real es acotado (~1 s sobre políticas de 4–7 s) y `t_alert` no
  se compara entre densidades sin control de supervivencia.
- **F-96.7: 0 FP en negativos en las ocho campañas.** Con 4 clips es control
  comparativo, no cota — el tiempo real no introduce falsas alarmas en cumplimiento.

> **Guards de esta campaña.** (a) `run_descriptor.rate_control.stride` + conteo de
> unidades contra `ceil(n/stride)`, por clip: 34/34 en las seis. (b) Comparabilidad
> con las referencias verificada, no supuesta: re-correr replay + `evaluate-alerts`
> con el código de hoy sobre las detecciones de T1 reprodujo sus **34 evals idénticos
> campo a campo** (`datos/96-verificar-comparabilidad-t1.py`).

> **Qué NO miden.** No son corridas por el bus: miden densidad de evidencia sobre el
> camino DBE. Integridad del acople y latencia operativa siguen viniendo de los humos
> EBE (docs 37/65/67/91). El decimado es regular; el descarte live es irregular —
> **límite cerrado por el doc 101**: la irregularidad real se midió (CV 0,22 hoy /
> 0,36 rodaje) y el eje se re-corrió con decimado empírico (3 semillas, equivalencia
> decimado≡re-inferencia verificada 34/34 contra R1): ningún contraste
> jitter−regular detectable y la ganancia de la identidad conserva el signo en 6/6
> realizaciones (F-101.3/4, con matiz declarado a 2,5 fps).

## Campañas candidatas (el contraste que falta)

| Prioridad | Combinación a variar | Qué pregunta responde | Estado |
|---|---|---|---|
| ~~1~~ | ~~Prompts `edir_v1` / `eind_v1`~~ | **RESUELTO**: Nivel A (doc 83) + Nivel B (D1, doc 85) → veto de precisión, E-IND es el núcleo | **cerrado** |
| ~~2~~ | ~~Modelo `gdino-base-560`~~ | **HECHO** (T2, doc 84): F-81.2b refutada bajo `v2_short`; CR-02 SDR 0,281→0,920 | **cerrado** |
| ~~1~~ | ~~E-HYB `hyb_or`~~ | **HECHO (H1, doc 87)**: predicción refutada, F-87.2 | **cerrado** |
| ~~2~~ | ~~E-HYB `hyb_and`~~ | **No ejecutada CON CAUSA** — la vigente es D-90.4: no medible contra este banco sin romper la comparabilidad de las 6 campañas (el planteo original de doc 87 §5 queda archivado como predicción) | trabajo futuro con predicción escrita |
| ~~1~~ | ~~`bare_head` × `gdino-base-560`~~ | **HECHO (B1, doc 88)**: F-88.2 tampoco alcanza (0,480 vs 0,582); de yapa F-88.1 (costo del caption) y F-88.3 | **cerrado** |
| ~~1~~ | ~~Granularidad `subject` (G1)~~ | **HECHO (G1, doc 89)**: F1 0,930, la mejor del banco. `track_id` post-hoc, sin GPU | **cerrado** |
| ~~1~~ | ~~Densidad de evidencia del camino live~~ | **HECHO (R1–R6, doc 96)**: F-96.4 — la ganancia de la identidad excluye el cero en las 4 densidades; los deltas de densidad del agregado no | **cerrado** |
| ~~1~~ | ~~Lote de internet sumado al banco~~ | **HECHO (I1/I2, gen. 3, docs 109–113)**: 13 clips con GT humano en el banco, soak incorporado, y el análisis de sensibilidad del control de FP dio la asimetría 26 vs 323. De yapa, la revisión ciega del GT (**5 de 7 declaraciones eran errores de anotación**) convirtió la calidad del GT en un resultado. Ver la sección del estrato B | **cerrado** |
| ~~2~~ | ~~Campaña EBE de punta a punta por el bus sobre los 34 clips~~ | Integridad del acople y latencia operativa CONTRA GT, no en humos. Hoy el eje se cubre por densidad (R1–R6) + humos verdes (37/65/67/91). ✎ **2026-08-15 — evaluada y DESCARTADA CON CAUSA (F-121.1)**: no daría resultado nuevo. El pipeline DBE es determinista (F-109.1) y el bus publica el evento **byte-idéntico** al del JSONL (paridad verificada por mutación, doc 37 §3) ⇒ **el resultado sería idéntico a T1 por construcción**. La única divergencia posible (pérdida en el bus) ya se cuenta y degrada la corrida | **declarada con causa — no pendiente** |
| ~~2~~ | ~~Port de `track_id` al pipeline online (spec 42 §3)~~ | ✎ **2026-08-15 — esta fila estaba STALE y se corrige.** *Decía: "solo si se decide llevar G1 a producción: hoy el `track_id` es post-hoc. Decisión de ADR-002, ver doc 89 §7 — decisión del usuario".* **El planteo lo reencuadró la implementación** (doc 89 §6 bis) y la **adenda de ADR-002 quedó RATIFICADA el 2026-08-05**: la identidad se implementó como **decorador de fuente en el control-plane** (`sources/tracking.py`, `input.track_persons`), cableado en los **dos** runtimes ⇒ **G1 ya está disponible en DBE y en EBE/live**, sin que el media-plane emita `track_id`. Verificado en vivo con la OAK-D (doc 91: clave `CR-01:smoke_ebe:subject_001`, sin `no_track_id`). El port del spec 42 §3 **dejó de ser el camino obligatorio**; sería sólo una decisión de arquitectura (mover el tracker al media-plane para embeber `track_id` en `detections.jsonl`), **no un pendiente de resultados** | **cerrado — ya no es decisión pendiente** |
| ~~2~~ | ~~Resolución 800 px sobre el banco temporal~~ | ✎ **Fila agregada 2026-08-10 para que la palanca no falte del tablero. NO ejecutada CON CAUSA:** 560 domina a 800 en el bench de imágenes (igual o mejor mAP con **−24% de latencia**, D-61.4), así que correrla habría medido una configuración dominada y roto la variable única de las campañas. Declarado en doc 64 §Decisiones S2 | **no ejecutada con causa** — trabajo futuro con predicción escrita (doc 103 §7.4 la lista entre las mitigaciones no medidas para `vest` a distancia) |

**Todas las palancas del banco están agotadas.** Formulación (D1), fusión (H1), modelo
(T2), vocabulario nativo (B1), granularidad (G1) y **densidad de evidencia (R1–R6)**.
La única que **no** se ejercitó es la **resolución** (800 px), y está declarada como no
ejecutada con causa en la fila de arriba — no se cuenta entre las agotadas a propósito.
✎ **2026-08-09: el material que faltaba también entró.** El video no guionado (L4,
precisada) y el soak llegaron con el estrato B: el banco quedó en 47 clips con 0,2725 h
de tiempo negativo total, de las cuales 0,1027 h son soak citable. Eso **no convierte a
FAR/hora en una cota** (L1 sigue en pie por el denominador: hacen falta 3 h), pero sí la
hizo computable y reportada. ~~Lo que queda abierto no es material del banco sino los dos
ejes ubicados y no ejecutados de la tabla de arriba (campaña EBE por el bus, port del
`track_id` al pipeline online).~~ ✎ **2026-08-15 — no queda ninguno de los dos:** el port
del `track_id` **nunca fue un pendiente** (G1 ya corre en DBE y EBE/live como decorador
del control-plane; ADR-002 adenda ratificada el 08-05, verificada en vivo en el doc 91) y
la campaña EBE por el bus quedó **declarada con causa** tras evaluarla (F-121.1: daría el
resultado idéntico por construcción). **El banco no tiene frentes abiertos.**

### Estrato B — lote de internet (13 clips, obra real NO guionada) · gen. 3, 2026-08-09

**El lote cerrado y medido de punta a punta.** 13 de los 14 clips con GT humano
(`v08_c01` excluido con causa, doc `operacion/111`); inferencia fresca de los 13 en
**una sola sesión** de 72 min de GPU. Procedencia única. Las gen. 1 y 2 (3 y 4 clips)
quedan supersedidas — `metrics.gen2.json` preservado al lado.

> **✎ 2026-08-09, RE-EVALUADO tras la revisión ciega del GT (doc `operacion/113` §B).**
> La revisión visual a ciegas de los 5 episodios del estrato — disparada por el patrón
> de sobre-declaración que ya habían mostrado `v06_c01` y `v03_c02` — **tiró 3 de los
> 5**: los dos de `v04_c02` (el sujeto está en la cabina de una máquina: estado no
> observable) y el de `v01_c01` (contraluz; ya estaba censurado). Correcciones firmadas
> en los `clip.yaml`, GT re-derivado, banco regenerado (**32 positivos / 15 negativos /
> 37 episodios**). MISMAS detecciones y alertas (determinismo verificado: 11/11 clips
> sin cambio de GT dieron evals idénticos); se re-corrió solo `evaluate-alerts` +
> agregación, y los **13 evals quedaron archivados** en `evals/` de cada campaña.
> Las cifras de abajo son las VIGENTES; las de la gen. 3 original (F1 0,500/0,200
> sobre 4 evaluables) quedaron supersedidas y viven en el git y en la evidencia de
> `docs/operacion/datos/110-estrato-b-gen3/`.

**El material (post-revisión):** 2 clips positivos (**2 episodios evaluables, 0
censurados**) y **11 negativos** (14,2 min = 0,2367 h), de los cuales **1 es soak**
(`v06_c01`, 6:09,6 = 0,1027 h, el único denominador temporal del banco). Un positivo
nocturno (`v04_c01`) y dos negativos nocturnos (`v04_c02`, `v04_c03`).

| | I1 `scene` | I2 `subject` |
|---|---|---|
| recall (2 eps evaluables) | 0,500 | **1,000** |
| precision | **0,250** | 0,105 |
| **F1** | **0,333** | 0,190 |
| matched / missed / FP | 1 / 1 / 3 | 2 / 0 / 17 |
| t_alert | 4.000 ms (n=1) | 4.133 ms (n=2) |
| SDR · TTFD | 0,959 · 16,5 ms (n=2) | idénticos (mismas detecciones) |
| FP sobre los 11 negativos | **26** | **323** |
| **FAR/hora** (soak, 0,1027 h) | **29,2** | **1.850,8** |

**Por escenario:**

| | P1 (2 clips, 2 eps) | P5∅ (11 clips) |
|---|---|---|
| `scene` | recall 0,500 · 3 FP | 26 FP |
| `subject` | recall 1,000 · 17 FP | 323 FP |

### Cómo se lee — y confirma lo que la gen. 2 insinuaba

1. **En este régimen, la ventaja de la identidad que G1 mostró en el rodaje NO se
   reproduce, y `subject` paga un costo de FP un orden de magnitud mayor**: ~6× más FP
   en positivos (17 vs 3) y **12× más en negativos** (323 vs 26) — esa asimetría es lo
   robusto (conteos grandes) y **sobrevivió intacta a la revisión del GT**. `subject`
   compra el episodio que falta (recall 0,500→1,000) pagándola. **No hay una
   granularidad mejor: hay una correcta para cada régimen de densidad** (F-108.1).
   *(✎ el ranking por F1 que una versión anterior afirmaba quedó enmendado — F-111.1,
   doc 111 — y con n=2 menos sostenible aún.)*
2. **Ya NO hay ningún "caso limpio" en el estrato.** `v04_c02` (ex-P6, recall 1,000 y
   0 FP en ambas) lo era — hasta que la revisión ciega mostró que su único sujeto está
   en la cabina de una máquina y su estado **no es observable**: sus 2 episodios eran
   sobre-declaración del anotador, el clip es **negativo**, y las mismas alertas que
   antes "acertaban" son ahora **3 FP (`scene`) / 4 FP (`subject`)**. Es el ejemplo más
   crudo de la frontera de juzgabilidad: **ni el anotador ni el motor podían juzgar, y
   los dos declararon violación.**
3. **El episodio que `scene` pierde** es el CR-01 de `v04_c01`, por alerta prematura
   (confirma a los 4,0 s; la ventana abre a los 7,97 s).
4. **FAR/hora: 29,2 FA/hora en el mejor caso** — que son **3 FP en 6:09,6** del único
   clip soak, obra real donde nadie infringe (`subject`: 190 FP ⇒ 1.850,8). La tasa
   horaria es una derivada sobre 0,1027 h, no una hora observada. Ver el bloque de L1
   abajo.
5. **n = 2 episodios evaluables en 13 clips** (eran 4 antes de la revisión ciega; **5 de
   las 7 declaraciones de episodio que el lote produjo resultaron errores de
   anotación**, todas sobre-declarando donde el estado no era observable). El estrato
   describe un régimen y la calidad de su GT es un resultado en sí; **ninguna
   comparación por F1 sale de acá**.

**Determinismo re-confirmado (F-109.1).** Los 4 clips que ya se habían inferido en la
gen. 2 dieron detecciones **idénticas** al re-inferirlos (572 / 840 / 11.087 / 1.771
frames, mismas cajas). El pipeline DBE es reproducible entre sesiones.

**⚠️ Corrección de métrica que afecta cifras publicadas antes (doc 111 §6).** El
agregador calculaba `far_per_hour` con el numerador de **todos** los negativos y el
denominador de **solo los soak** — dos bases distintas. El factor de inflación es
`FP de todos los negativos / FP del soak`, así que varía por generación y granularidad:
**lo que llegó a publicarse (gen. 2) estaba inflado 1,67× en escena y 1,11× en sujeto**;
en la gen. 3 el mismo bug habría impreso 204,6 en escena (**7×** — el número absurdo que
lo delató antes de publicarse) y 2.961,3 en sujeto (1,60×). Corregido con test de
regresión: ahora numerador y denominador salen del mismo conjunto. **Las cifras de FAR
de la gen. 2 que circularon (48,7 y 2.045,6) eran incorrectas; las correctas son 29,2 y
1.850,8** — y son las mismas en gen. 2 y gen. 3, porque dependen solo del clip soak,
que es determinista. El `metrics.json` expone además `far_per_hour_all_negatives`
como base informativa (**109,8 / 1.364,4** tras la revisión del GT: los negativos
pasaron de 9 a 11 y suman 0,2367 h).

**Advertencias de lectura que salieron de este estrato** (valen para toda la página):

- **F-104.2** — en `scene`, subir el gate de área **empeora** los FP porque el conteo
  bajo era el latch de la escena capturada. **El conteo de FP no compara `scene` contra
  `subject` cuando la escena está capturada.**
- **F-104.4** — en `v10_c01` (fachada en altura: arnés, **no** chalecos) el GT humano
  dice `unknown` en ~85% de los frames-sujeto y el motor alerta igual. **El conteo de FP
  se mueve por alucinación de la clase ausente, no por acertar.**
- **F-108.2** — la mejor palanca de configuración medida in-sample
  (`min_subject_confidence` 0,50) corrió la alerta de `v04_c02` fuera de su ventana en
  el control out-of-sample. *(✎ 2026-08-09: el "episodio real" que esa prueba usaba
  cayó después en la revisión ciega — el sujeto no era juzgable — así que el costo
  medido ya no es "un missed", pero la lección operativa queda: la palanca calibrada
  in-sample cambió el comportamiento sobre el primer material fresco de manera no
  anticipada.)* Ninguna configuración sale recomendada de este estrato.

**Nivel A del mismo material** (estado por persona, sin motor temporal), consolidado con
los 4 clips piloto: `results/bench_nivel_a/na1_gdinotiny560_v2short_video/`.

**✎ 2026-08-07 — L1 cambió de naturaleza: FAR/hora pasó a ser MEDIBLE, y el dato la
refuta.** Con la corrección del GT, `v06_c01` es negativo de 6:09,6 ⇒ **el primer clip
soak del banco** ⇒ denominador **0,1027 h** (era 0,0 h). El agregador ya no devuelve
`None`: devuelve **29,2 FA/hora en escena y 1.850,8 FA/hora por sujeto** (cifras
corregidas el 08-09 — las que circularon antes, 48,7 y 2.045,6, salían de un cálculo
que mezclaba bases; ver la sección del estrato B).

**D-90.1 no queda derogada, queda precisada.** Su argumento era que ningún denominador
alcanzable permite afirmar *"≤1 FA/hora"* — y sigue siendo cierto: con 0,1027 h y la
regla de 3 harían falta 3,0 h. Lo que cambió es que **ya no hace falta ese argumento**:
no se declara "no medible" una métrica cuando el dato medido la refuta de frente. El
banco pasó de 0,0358 h a **0,2725 h de tiempo negativo total** (`clip_bench_manifest.json`;
✎ 08-09: incluye los ex-positivos `v01_c01` y `v04_c02` tras la revisión ciega),
de los cuales 0,1027 h son soak citable.

> **~~FAR/hora no es una métrica de este trabajo~~ — lo derogado el 2026-08-07 es esa
> REGLA DE REPORTE; D-90.1 queda PRECISADA, no derogada** (bloque de arriba, y
> limitación **L1** en `results/index.md`, que es la formulación canónica: se computa y
> se reporta, no sostiene una cota). Se conserva el texto original por trazabilidad: *"(D-90.1,
> 2026-08-04) Para afirmar 'FAR ≤ 1 FA/hora' con 0 FP harían falta 3 h de video en
> cumplimiento anotado; el banco alcanza 0,101 h con el clip soak previsto y 0,263 h
> como techo. Una cota de 11–30 FA/h no sostiene ninguna afirmación operativa."*
> **Lo que cambió:** el clip soak existe y FAR/hora se mide (**29,2** y **1.850,8** FA/hora).
> El argumento del denominador sigue en pie —no alcanza para afirmar una cota— pero ya
> no se declara la métrica no medible. **La evidencia de falsas alarmas del rodaje
> sigue siendo la columna "FP neg." de la tabla de arriba**: T1/T2/G1 dan 0 FP de 4;
> D1, H1 y B1 dan 2–3.

> **Comparabilidad:** T1 se evaluó con los fixes F-EV1/2/3 del evaluador
> (control-plane `c1cbb56`). Cualquier campaña anterior a ese commit **no es
> comparable** sin re-evaluar — se re-evalúa barato desde los artefactos
> guardados (`docs/operacion/datos/81-reevaluar.py`), la inferencia no se repite.
>
> Después vino `5327080` (08-04), que cambió el despacho de evaluadores y toca
> `_positive_flags_for_source` (el que deriva SDR/TTFD). **Verificado que NO afecta a
> las campañas `eind`**: el código de hoy reproduce los 34 evals de T1 idénticos campo
> a campo (`datos/96-verificar-comparabilidad-t1.py`, 2026-08-05). Las filas de arriba
> son comparables entre sí sin re-evaluar.

## Artefactos secundarios de esta familia (✎ declarados 2026-08-09)

Tres campañas guardan un `.json` **además** de su `metrics.json`. Hasta hoy ninguno
estaba nombrado en un índice, y un archivo de métricas sin etiqueta al lado del
principal es una invitación a citar el número equivocado. Qué es cada uno:

| Archivo | Qué es | Estado | Doc |
|---|---|---|---|
| `i1_…_internet/metrics.gen2.json` | Generación 2 de I1: **4 clips**, banco de 38, manifest `4437eb6d…`. F1 0,571 | **SUPERSEDIDO** por `metrics.json` (gen. 3, 13 clips) | `operacion/109`–`111` |
| `i2_…_internet/metrics.gen2.json` | Ídem, brazo `subject`. F1 0,400 | **SUPERSEDIDO** | Ídem |
| `b1_…_barehead_scene/metrics_eind_mismo_caption.json` | **Control interno de B1**, no una generación vieja: las MISMAS detecciones de `gdino-base-560` con caption de 4 clases, evaluadas con **E-IND** en vez de `bare_head` directo. **F1 0,622 y 0 FP en negativos** (contra 0,377 y 3 FP del principal) | **VIGENTE** — es la mitad (a) del diseño "una inferencia, dos evaluadores" y sostiene **F-88.1** (el costo del caption: 0,704 → 0,622, −0,082) | `operacion/88` |

> ⚠️ **Los dos `metrics.gen2.json` NO se editan** (doc 113 §D3): conservan el valor
> incorrecto de `far_per_hour` (48,7 / 2.045,6) junto a un `far_basis` que describe la
> fórmula **corregida** y no la que produjo ese número. Se congelan a propósito, como
> registro de lo que la gen. 2 produjo; lo que se corrige es el registry y la
> procedencia, nunca el artefacto histórico.

> **El SDR no se compara entre cadencias (F-96.6).** Vale dentro de un mismo `stride`.
> Las seis campañas de la tabla principal comparten `stride: 1`, así que ninguna
> conclusión previa se ve afectada; para el eje de densidad, ver la sección R1–R6.

---

## Fuente: `e-ovrt_experimental-setup/results/realtime/index.md`

> SHA-256 del bloque: `df4a7ba15e745db5787059ea0f5eac1b9cb1ffe2d7f8aa461a5f5e394dffb706`  
> Seleccion: documento completo.

# Real-time / EBE — resultados consolidados

Índice de lo medido sobre el **camino en vivo** (EBE: cámara → bus ZeroMQ →
control-plane) y sobre el comportamiento temporal de la plataforma. Complementa a
`results/bench_imagenes/` (percepción espacial) y `results/clip_bench/` (alertas
contra GT temporal).

**Cómo leer esto.** El eje real-time se cubre en **cuatro planos distintos**, y
conviene no confundirlos porque miden cosas diferentes:

| Plano | Qué responde | Estado |
|---|---|---|
| **Integridad del acople** | ¿el bus pierde eventos? ¿la corrida cierra 1:1? | ✅ cerrado |
| **Latencia operativa** | ¿cuánto tarda de captura a alerta? ¿entra en presupuesto? | ✅ medido (GDINO fuera de budget, con causa) |
| **Techo de throughput** | ¿cuántos fps sostiene esta máquina y por qué? | ✅ diagnosticado + una palanca aplicada |
| **Calidad bajo restricción de tiempo real** | ¿qué rendimiento sobrevive a ver menos frames? | ✅ **medido 2026-08-05 (doc 96)** |
| **Distribución de alertas** | ¿cuánto tarda el bus de alertas en obtener PUBACK MQTT QoS 1? | ✅ **p95 64,534 ms (n = 460)** |

La campaña `t_alert_notification` (fuente: `e-ovrt_experimental-setup/results/realtime/t_alert_notification/README.md`) mide exclusivamente
`bus de alertas → PUBACK MQTT QoS 1`. El agregado principal da **p95 = 64,534 ms
(n = 460)**. En régimen sostenido (entregas 2.ª+ de cada corrida), el p95 es
**102,025 ms (n = 104)**; las primeras entregas dan **49,869 ms (n = 356)**.
Ambas lecturas proceden del mismo `outcomes.csv`, sin re-corrida.

---

## 1. Integridad del acople EBE

| Evidencia | Resultado |
|---|---|
| Gate de paridad replay↔stream (`test_bus_parity.py`) | **Artefactos idénticos**; un bbox corrido 1 px hace fallar el gate (compara contenido, no contadores) |
| Corrida live E2E (doc 37) | Replay del `detections.jsonl` de una corrida live produce artefactos **byte-idénticos** (15 `pattern_events`, 6 alertas, iguales módulo `control_run_id`/`alert_id`) |
| Rodaje completo, 6 corridas (doc 71) | **`bus_dropped_events = 0`** y `degraded = false` en las 6, y también en las de la tarde |
| L0 ensayo 1:1 (doc 65) | Verde, 30/30 unidades, `bus_dropped_events = 0` |
| Regresión post-cambios (doc 91) | **0 eventos perdidos** en ambas fases, `units_failed = 0` |

**Este subsistema está cerrado.** El JSONL sigue siendo la verdad en los dos caminos:
toda corrida live es re-evaluable offline y produce artefactos idénticos (verificado).

> **Trampa no negociable (docs 37/68):** nunca cerrar un socket ZeroMQ desde un hilo
> distinto del que lo creó mientras otro está en `recv_multipart` — libzmq aborta el
> proceso con `SIGABRT`. Por eso las fuentes de red exponen `request_stop()`.
>
> **Orden de arranque EBE:** control-plane **primero** (`POST :8081/api/runs`,
> `mode: live`, cuyo 201 implica suscripción activa) y media-plane **después** con
> `bus.enabled: true`. PUB/SUB pierde lo publicado antes de la suscripción.
>
> **Tres trampas más, medidas el 2026-08-05 (doc 101 §5.2):** **F-101.5** la fuente
> OAK-D no cierra cooperativamente y depthai tira `std::system_error` desde un hilo
> no-Python → **SIGABRT del media-plane** (misma familia que la de ZeroMQ, otro
> culpable) ⇒ **una sola corrida OAK-D por vida del servicio**; los artefactos se
> salvan porque se escriben incrementalmente. **F-101.6** el device crashea y
> reconecta **mientras el ping ICMP da 0% de pérdida** (la pila de red del PoE
> responde con la aplicación caída) ⇒ el ping no descarta nada, el remedio es
> power-cycle. **F-101.7** el status en vivo del media-plane **no trae
> `units_processed`** (aparece recién en el `summary`): esperar frames leyéndolo de
> ahí reporta "la cámara no entregó frames" con la cámara funcionando.

## 2. Latencia operativa (G2A: captura → alerta)

| Contexto | G2A p50 | G2A p95 | Presupuesto 50–250 ms |
|---|---|---|---|
| Single-host, video (doc 39) | **14,7 ms** | **31,8 ms** | ✅ dentro |
| GDINO (`tiny-560`) live sobre OAK-D (doc 71) | — | **630–890 ms** | ❌ fuera |
| YOLOE live sobre OAK-D (doc 71) | — | **225–249 ms** | ✅ dentro |

**El resultado incómodo, y es un resultado, no una falla:** el único modelo que entra
en presupuesto temporal (YOLOE) es el que **no sirve para la condición** (recall
`bare_head` 0,000 en el bench de imágenes, y en vivo produjo una CR-02 falsa al 100% y
dos alertas con tiempo corrompido). El que detecta (GDINO) no entra en presupuesto.
Esa tensión calidad↔latencia es un hallazgo de primera línea del trabajo.

> **F-101.8 — el G2A se mide desde el DEQUEUE, no desde el fotón, y el informe debe
> decirlo.** `capture_wallclock_ms` se estampa cuando el host saca el frame de la
> cola; el wallclock del fotón es `capture_wallclock_ms − capture_to_host_ms`. O sea
> que **la latencia vidrio→alerta es `capture_to_host` + G2A**, y ese término varía
> un orden de magnitud con el estado de la fuente (medianas por corrida):
> **202–217 ms en las 6 corridas del rodaje**, **169 ms** en el humo del doc 91 y
> **1.600 ms** en las tomas del 08-05 (cola estacionaria, huecos regulares de
> 275 ms — consistente con el doc 61 hallazgo 5: el cuello es la fuente, no el
> modelo). Está instrumentado por frame, así que es **declarable, no un hueco**, y
> quedó **validado contra el mundo físico** por la toma anclada del doc 101 §5.4
> (tono → fotón = +1.066 ms). **Los números de la tabla de arriba son G2A y su
> lectura no cambia**: en el rodaje el término era ~0,21 s estable.

## 3. Techo de throughput y su diagnóstico

### Lo que efectivamente corrió en el rodaje (doc 71 §2.1)

| Corrida | proc/drop | fps_eff | inf p50 | G2A p95 |
|---|---|---|---|---|
| GDINO P1 | 47/767 (**94% drop**) | **1,16** | 567 ms | 890 ms ✗ |
| GDINO P2 | 93/1115 (92%) | 1,76 | 439 ms | 665 ms ✗ |
| GDINO P3 | 55/629 (92%) | 1,51 | 432 ms | 630 ms ✗ |
| YOLOE P1 | 254/615 (71%) | **5,55** | 116 ms | 232 ms ✓ |
| YOLOE P2 | 295/710 (71%) | 5,98 | 118 ms | 225 ms ✓ |
| YOLOE P3 | 152/322 (68%) | 5,12 | 112 ms | 249 ms ✓ |

**Variación a lo largo de la jornada**: la misma configuración rindió **2,62 fps a
las 13:33 y 1,16 fps a las 20:10 (2,26×)**. ✎ 2026-08-06: *la lectura original
("degradación monótona, correlato térmico 41 °C vs 55–61 °C", doc 71) fue refutada
por doc 73 §0.3 con los datos del propio rodaje*: 17:50 rindió 201 ms y 17:58
445 ms (2,2× en 8 min), y la corrida de las 13:33 es más lenta que la de las 17:50
— lo que separa las poblaciones es **la fuente** (`video_file` 306 ms vs `oak_d`
426 ms, intercaladas en el tiempo), no el calor. Coherente con F-RT3 (abajo): el
techo es contención de GIL, no térmico.

### Causa raíz y palanca aplicada (docs 73/74)

- **F-RT3 — el techo es contención de GIL**, no térmico ni la rama de texto.
  Verificado que la GPU sí se usa (triple chequeo: `torch.cuda`, 1,6 GB VRAM del
  proceso, `dmon` con SM 6–41%); el perfil "bursty" es la firma de un transformer a
  batch=1, no ociosidad.
- **F-RT5 — palanca aplicada y significativa**: sacar el round-trip PIL del productor
  da **+18% de fps (3,75 → 4,42) y −14,4% de latencia**, p = 0,0195 con 11 pares
  pareados. Commit `3deb64c` en `perf/producer-pil-roundtrip` (merge = decisión del
  usuario). Salida byte a byte idéntica: no requiere re-validar mAP.
- **Las tres palancas que sí estaban planificadas** (cachear texto, 480 px, térmica)
  sumaban <15% y **quedaron descartadas con números**.

> **Higiene de medición (doc 74), aprendida a los golpes:** `py-spy` en WSL infla la
> medición 2×; cualquier palanca de menos del 20% necesita **~10 pares pareados
> intra-campaña** para separarse del ruido del host (F-RT4, deriva ±150 ms). Protocolo:
> reinicio de WSL + verificación de p50 < 300 ms antes de medir.

### Prefilter EN-2 on-device (doc 10 E-07)

Gate de personas **en la cámara** (OAK-D, blob `person-detection-retail-0013`),
fail-open estructural: A/B real con GDINO da **87% de drop on-device**. Solo aplica a
`source.type = oak_d`.

## 4. Calidad bajo restricción de tiempo real (doc 96 — el plano que faltaba)

Hasta 2026-08-05 los tres planos anteriores estaban medidos pero **ninguna métrica de
calidad contra GT** existía para el camino live: las 6 campañas del banco corrieron
todas a `stride: 1` = **30 fps de evidencia**, mientras el live entrega **1,16–4,42
fps**. Las campañas R1–R6 cierran ese hueco.

**Tabla completa y hallazgos: `results/clip_bench/index.md` § "Eje de densidad de
evidencia".** Lo esencial:

- **F-96.4 (verificado con bootstrap pareado por clip):** la ganancia de la
  granularidad por sujeto **excluye el cero en las cuatro densidades** (+0,141 a 30
  fps, +0,072 a 4,29, +0,137 a 2,00, +0,096 a 1,15). Es la única palanca del banco
  significativa a la densidad que el live entrega hoy — y el tracker **no se
  fragmenta** (154 → 103/91/105 tracks).
- **F-96.2:** lo primero que se rompe bajo tiempo real es el rescate de la histéresis
  (F-81.1): CR-02/P2 cae 1,00 → 0,60 → 0,20. Límite de cadencia declarado.
- **F-96.5:** el costo real en tiempo de alerta es **+0,7 a +1,3 s** entre
  supervivientes comunes, sobre políticas de 4–7 s. Acotado y declarable.
- **Ningún delta de densidad del agregado de escena excluye el cero** — ahí el costo
  del tiempo real es tendencia monótona con mecanismo identificado, no efecto
  establecido. Bajo **sujeto**, el peor caso **sí es individualmente significativo**:
  R6−G1 = −0,188 [−0,334, −0,040] (doc 96 §4.1).

> **Dos reglas de lectura que salieron de acá y el informe debe llevar:** el **SDR no
> se compara entre cadencias** (F-96.6: la subida es ~100% artefacto del instrumento) y
> el **`t_alert` agregado no se compara entre densidades sin control de
> supervivencia** (F-96.5).

**Verificación posterior (doc 101, 2026-08-05).** El límite declarado del doc 96
("el decimado es regular; el descarte live es irregular") quedó **medido y
verificado**: la irregularidad real es CV 0,22 (estado actual, media 7,28 frames@30
= 4,12 fps — que además **valida empíricamente el ancla stride 7** de R1/R2) y CV
0,36 (rodaje); re-corriendo el eje con decimado **empírico** (huecos muestreados de
esas distribuciones, 3 semillas, guard de equivalencia decimado≡re-inferencia verde
en 34/34 contra R1), **ningún contraste jitter−regular es detectable** (12/12 IC
cruzan el cero, t_alert +11 ms entre supervivientes comunes, 0 FP en negativos en
las 16 variantes) y **la ganancia de la identidad conserva el signo en 6/6
realizaciones** (F-101.3/4; matiz declarado a 2,5 fps en doc 101 §3).

## 5. Confirmaciones de patrones en vivo (evidencia contra reloj real)

| Condición | Confirmaciones live legítimas | Deltas medidos | Umbral |
|---|---|---|---|
| CR-01 | **7** (rodaje: 18:30, 19:21, 19:43, 20:10 + humos) | 4,1–4,6 s | 4,0 s |
| CR-02 | **3** (rodaje 15:47 + humo fase A + humo fase B) | 7,1 s y superiores | 7,0 s |

**Verificación con reloj EXTERNO (doc 101 §5.4, toma anclada del 2026-08-05).** Lo
anterior compara los relojes del sistema contra sí mismos; esta toma ancla la cadena
a un instante físico conocido (tono generado por el host, cuyo wallclock real se
mide, y el sujeto entra a cuadro en ese instante). Las cuatro patas cierran:
**ancla física→estampa +1.066 ms**; **onset observado = 1ª evidencia del motor**
(mismo frame, con confirmación visual del hombro entrando al cuadro); **política
4.142 ms** contra 4.000; **relojes de los dos procesos con 4 ms de residuo**; y la
**cadena completa tono→alerta = 7.045 ms = 2.716 + 4.329**. Cierra el stretch que el
doc 58 había declarado diferible. Cadencia de esa corrida: 3,60 fps, CV **0,016**.

La aritmética cierra contra la política, que es lo que había que demostrar del motor
temporal en vivo. El caso de las 19:21 además demostró la resolución con histéresis:
17 s de `sustained` con 17 "brillos de pelada" (helmet 0,25–0,46 intermitente) que
**no** resolvieron el episodio.

### G1 (identidad) verificado en vivo (doc 91)

| | Fase A (escena) | Fase B (sujeto) |
|---|---|---|
| Unidades | 150 | 160 |
| `bus_dropped_events` | **0** | **0** |
| Alertas | 2 (CR-01 + CR-02) | 2 (CR-01 + CR-02) |
| **`subject_key`** | `CR-01:smoke_ebe` | **`CR-01:smoke_ebe:subject_001`** |

El contraste de la última fila es toda la evidencia: bajo sujeto la clave incorpora el
`track_id` que el decorador de fuente produce **sobre el bus**, sin que el media-plane
emita nada nuevo. Y `no_track_id` **no** aparece en las causas de degradación — si
apareciera, el motor habría degradado a escena y la fase B habría medido G0 creyendo
medir G1.

## 6. Hallazgos negativos que son resultados, no fallas

- **F-RT1 — la sobre-marca de `vest` suprime CR-02.** Es dependiente de la vestimenta,
  documentado con su caso positivo y su caso negativo: campera a franjas conf 0,54 /
  torso liso 0,31 (ambos ≥ umbral 0,25) suprimen o retrasan; con remera negra lisa
  hubo **0 detecciones de `vest` en 309 frames** y CR-02 confirmó limpia.
- **F-RT2 — la ventana temporal exige estabilidad perceptual** con huecos <
  `resolve_after_ms`. GDINO la cumple; YOLOE no. Es una **condición de validez
  descubierta**, exactamente el tipo de aporte que el trabajo argumenta.

## 7. Qué NO está medido

- **Campaña EBE de punta a punta por el bus sobre los 34 clips.** El eje de calidad se
  cubre hoy por proxy de densidad sobre DBE (doc 96) + integridad verificada en humos,
  y el proxy quedó verificado también contra el descarte irregular (doc 101) — la
  prioridad de esta campaña baja aún más. Bloqueo técnico: el ancla wallclock↔media
  (ingeniería, no material). ~~Trabajo ubicado, no ejecutado.~~ ✎ **2026-08-15 —
  DECLARADA CON CAUSA, no pendiente (F-121.1, `operacion/121` §2.2).** Se evaluó
  ejecutarla y **no produciría ningún resultado nuevo**: el pipeline DBE es determinista
  (F-109.1) y el bus publica el evento **byte-idéntico** al del JSONL (gate de paridad
  verificado por mutación, doc 37 §3) ⇒ **el resultado sería idéntico a T1 por
  construcción**. La única divergencia posible es pérdida en el bus, que se cuenta
  (`bus_dropped_events`) y degrada la corrida — y en DBE la presión sobre el bus es
  **menor** que en vivo, o sea un test más flojo que los humos que ya dieron 0. No es un
  experimento: es un guard de un modo de falla que ya tiene detector.
- ~~La irregularidad del descarte live~~ → **MEDIDA Y VERIFICADA (doc 101)**: CV
  0,22–0,36 según estado del host, sin efecto detectable sobre el eje de densidad.
  Residuo de segundo orden declarado: el jitter muestreado es i.i.d.; el real puede
  correlacionar con el contenido de la escena.
- **El tracker en obra real con multitud.** G1 se verificó en vivo con pocos sujetos.
- **`gdino-base-560` no tiene latencia live medida** (doc 101 §1): lo medido en vivo
  fue `gdino-base` a **800 px** (G2A p50 311–388 / p95 446–614 ms); el −24% de la
  resolución 560 es inferencia batch sobre el BENCH (D-61.4), no una medición live.
  T2 y B1 quedan sin costo operativo live declarado.
- **Ancla de sincronización para EBE-desde-clip**, lo que impediría hoy alimentar el
  banco por el bus con correspondencia exacta al GT temporal.
- **FAR/hora**: limitación declarada (D-90.1), no métrica. La evidencia de falsas
  alarmas es el control de negativos del clip bench.

## 8. Dónde está cada número

| Qué | Dónde |
|---|---|
| Bus, runtime live y paridad | `docs/operacion/37` + `datos/37-*` |
| Servicio del control-plane | `docs/operacion/38` |
| G2A single-host | `docs/operacion/39` + `datos/39-2026-07-10-g2a-video-summary.json` |
| Benchmark realtime por modelo/fuente | `docs/operacion/61` |
| L0 ensayo EBE 1:1 | `docs/operacion/65` |
| **Rodaje: las 6 corridas live** | `docs/operacion/71` |
| Diagnóstico del techo de fps (GIL) | `docs/operacion/73` |
| Protocolo de higiene de medición | `docs/operacion/74` |
| Regresión live post-cambios + G1 en vivo | `docs/operacion/91` |
| **Calidad bajo densidad del live** | `docs/operacion/96` + `results/clip_bench/` |
| **Irregularidad del descarte live + verificación por decimado empírico** | `docs/operacion/101` + `datos/101-*` |
| Manual de arranque y trampas operativas | `docs/operacion/68` |

