# E-OVRT-VDP - paquete de etapa 5

> Generado el 2026-08-19. Etapa 5: seccion 17.5, evaluacion y validacion.

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

- **Etapa activa:** 5 - Etapa 5: seccion 17.5, evaluacion y validacion.
- Este archivo contiene el texto vigente que se modifica y sus insumos de ajuste.
- No se trasladan resultados propios hacia secciones cronologicamente anteriores.
- Nombre propio de esta etapa (01-etapa-5-activa.md): regenerarla no pisa el paquete de ninguna otra etapa.

---

## Fuente: `docs/informe/entregable/96e-informe-v11-cierre-anexos-referencias.md`

> SHA-256 del bloque: `3e2abeb147d1a11e40d229753a6266af93231295b7dd966989486855c438b2f1`  
> Seleccion: placeholder vigente de la seccion 17.5.

### 17.5. Evaluación y validación del prototipo

[Agregado futuro correspondiente a la Etapa 5]

---

## Fuente: `docs/informe/ajustes/05-etapa-5-evaluacion-y-validacion.md`

> SHA-256 del bloque: `5b27b997ac2737feb5aa1eed847571c2c9cc32706874479b80b04401c4b957a3`  
> Seleccion: documento completo.

# Etapa 5 — §17.5 Evaluación y validación del prototipo

> *Gantt ID 4 — "Evaluación y validación", 12/06/26 – 10/07/26.*
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
| **AJ-5.13** | EVIDENCIA | 🟠 | ✎ **08-17 — DESBLOQUEADA en T1: la jornada cerró NO-GO** (`operacion/123`). T1 se escribe como hallazgo con cifra (`bare_head` 0,0000 → 0,0455, faltaron 0,0045; `person` −11,62 % > tope 10 %; checkpoint no adoptado; márgenes pre-firmados, sin renegociar). **T2 sigue reservado**: tier exploratorio por enmienda D-FT-14 posterior al veredicto, márgenes D-FT-15 firmados por adelantado, **enviado y en cola, sin cifra** → `[[PENDIENTE: …]]`. *(cuerpo previo ⏳ 08-12: histórico)* |

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

### AJ-5.13 · 🟠 — ⏳ PENDIENTE: la rama comparativa de fine-tuning (E-04)

> **Estado: jornada EN CURSO desde el 2026-08-12.** Este es el único contenido abierto del
> §17.5. Se actualiza acá cuando cierre; hasta entonces, la subsección **se reserva**.

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

---

## Fuente: `docs/informe/entregable/borradores/vara-15.md`

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

> SHA-256 del bloque: `88f991e2f6a5bb1588b5d0a2fd91c9e9d70091b504318fc691259fba1361fbea`  
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

**Regla al llenarlas:** ninguna tabla se transcribe desde este inventario ni desde el
§5 del doc 97 — se transcribe **desde el artefacto**, y el inventario solo dice cuál es.
Toda tabla de resultados lleva, en su nota al pie, el `campaign_id` o el sha256 del
banco: es lo que la hace verificable por un tercero.

**Las tres reglas de lectura que ninguna tabla puede violar** (F-EV1, L5, F-96.6):
los clips negativos (✎ 08-10: hoy son **15** — 4 del Bloque A + 11 del estrato B) **no**
entran a P/R/F1, su métrica son los FP · se reporta **por estrato y por escenario**,
nunca solo el agregado · el **SDR no se compara entre cadencias**.

---

