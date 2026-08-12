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
> [`06-etapa-6-documentacion-y-cierre.md`](06-etapa-6-documentacion-y-cierre.md). El §17.5
> reporta **qué se midió y cuánto dio**; qué significa es la etapa siguiente.

> ⏳ **2026-08-12 — hay UN contenido de esta sección que está abierto: la rama comparativa
> de fine-tuning (`AJ-5.13`).** La jornada de E-04 arrancó (ADR-017) y corre **en paralelo
> a la redacción**: por ADR-017 §2f **no bloquea el informe**. Todo el resto de los insumos
> del §17.5 sigue cerrado y congelado. **Mientras la jornada esté en curso, esa subsección
> se deja reservada con su estado declarado** — no se escribe como exclusión, no se escribe
> como hecha, y no se le pone un número que no salga de un artefacto.

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
| **AJ-5.13** | EVIDENCIA | 🟠 | ⏳ **PENDIENTE — la rama comparativa de fine-tuning (E-04)**, jornada **en curso**. La sección se reserva y se escribe con el estado a la entrega. ✎ 08-12 |

El **anexo de reproducibilidad** (§19), del que el §17.5 depende para ser auditable, es
`AJ-6.02` en la Etapa 6.

---

## 2. Los contenidos, desarrollados

### AJ-5.01 · 🟠 — tres niveles de medición, y no confundirlos

Es **el error más caro** de todo el set documental, y el §17.5 tiene que estar organizado
de modo que no se pueda cometer:

| Nivel | Qué mide | Sobre qué | Índice |
|---|---|---|---|
| **Imágenes** | detección por clase (mAP@0,5, AP por clase) | `bench_v3`, 3 fuentes independientes | `results/bench_imagenes/` |
| **Nivel A** | el **estado "sin EPP" por persona** (E-DIR vs E-IND) | imágenes y también video | `results/bench_nivel_a/` |
| **Nivel B** | **alertas confirmadas contra GT temporal humano** — el resultado principal | el banco de clips | `results/clip_bench/` |
| *(transversal)* | latencia, cadencia, integridad del acople | corridas live y single-host | `results/realtime/` |

Un mismo modelo tiene números muy distintos en cada nivel, y eso **no es una
inconsistencia: es el hallazgo**. El caso más elocuente es Nivel A sobre video, donde el
derrumbe respecto de imágenes es **de precisión, no de recall** (tabla T-83).

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

**Las tres cosas que no se pueden escribir, y por qué cada una:**

| 🚫 | Por qué |
|---|---|
| La causa **"falta de tiempo"** / "presupuesto de tiempo" / "secuenciación" como motivo de no-ejecución | **Prohibida por ADR-017 §2b.** El encuadre correcto: rama comparativa **condicionada desde el planteo por datos y protocolo** (Tabla 37: baseline primero; F-100.1; licencias). El cómputo nunca fue la restricción — Mendieta disponible, ≈1 GPU-h medido para T1. "Secuenciación" sobrevive **solo** como descripción del orden metodológico |
| Fundir sus cifras con las del **núcleo zero-shot** | Es **otra rama**. Se rotula como comparativa y va en su propia subsección y sus propias tablas. Fundirlas destruye la pregunta de la tesis, que es cuánto rinde el stack **sin entrenar** |
| Leer los go/no-go como **aprobado/fallado** | Son criterios de lectura y escalamiento (ADR-017 §2c). **Un desenlace negativo —sin ganancia exigible, o con erosión open-vocabulary medida— es un resultado documentable**, y de los valiosos: mediría el costo de adaptar |

**De dónde saldrán las cifras cuando existan:** de un artefacto en
`e-ovrt_experimental-setup/results/`, igual que todo el resto — **nunca de las notas de
trabajo de la jornada**. Mientras no haya índice verificable, no hay cifra citable.

**Puertas previas (son del tramo experimental, no de la redacción):** decisión del usuario
sobre **F-100.1** y la checklist de `operacion/100` §6. No bloquean escribir el resto
del §17.5.

**Se lee junto a:** `decisiones/adr-017-fine-tuning-jornada-experimental.md` (§2 completo)
· `contingencia/20` §6 (la escalera) · `01` (el encuadre en §15: rama comparativa, nunca
descarte) · `02` (la escalera en §17.1) · `06` (cómo entra en las conclusiones: rotulada
como rama comparativa, nunca fundida) · `operacion/100` §4/§6.

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
