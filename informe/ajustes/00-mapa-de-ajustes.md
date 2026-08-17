# Mapa de ajustes del informe — de la Etapa 1 a la Etapa 6

> **Qué es esto (2026-08-10).** El punto de entrada único a **todo lo que hay que
> cambiar, precisar o escribir en el informe** como consecuencia de lo que se
> implementó y se midió. Antes de este documento los ajustes estaban repartidos entre
> `informe/93` (solo Etapa 3), `nucleo/08`, `sintesis/resultados-y-conclusiones.md`,
> `informe/99` y los índices de `results/`. Acá quedan **ordenados por etapa**, en el
> orden en que se leen: 1 → 2 → 3 → 4 → 5 → 6.
>
> **Esto es un enrutador con enunciados, no una copia de contenido.** Cada ajuste dice
> *qué está mal o falta* y *de qué documento sale el texto o la cifra*. El texto y los
> números viven en su fuente y no se duplican acá: es la única forma de que este mapa
> no se desactualice.
>
> ✎ **2026-08-12 — este mapa dice QUÉ cambiar; el CÓMO aplicarlo está en
> [`08-manual-de-aplicacion.md`](08-manual-de-aplicacion.md)**: la superficie de edición
> (dónde se escribe cada cosa y por qué), el reparto entre las cuatro manos, el orden con
> su única dependencia dura resuelta, el loop repetible por sección, las cuatro puertas de
> cierre y **el tablero de estado de las 109 unidades**. **Es el documento del día 1** — el
> §6 de acá sigue siendo el orden recomendado, y el manual lo aterriza.

---

## 0. Las seis etapas, y a qué sección del informe corresponde cada una

**Las etapas son las seis del diagrama de Gantt (Figura 1 del §14.3), que coinciden 1:1
con las del §14.2.** Son la **guía de desarrollo** del proyecto: dicen en qué orden se
hizo y se cierra el trabajo.

| ID | Tarea del Gantt | Fechas planificadas | §14.2 | **Sección del informe** |
|---|---|---|---|---|
| **0** | Investigación bibliográfica | 31/10/25 – 28/11/25 | Etapa 1 | **§15** Estado del Arte · **§16** Marco Teórico · Anexo A |
| **1** | Análisis metodológico | 05/12/25 – 09/01/26 | Etapa 2 | **§17.1** Consolidación Metodológica · Anexos C y D |
| **2** | Diseño arquitectónico | 16/01/26 – 06/03/26 | Etapa 3 | **§17.3** (§17.3.1–17.3.18) |
| **3** | Implementación MVP | 20/03/26 – 29/05/26 | Etapa 4 | **§17.4** — *vacía* |
| **4** | Evaluación y validación | 12/06/26 – 10/07/26 | Etapa 5 | **§17.5** — *vacía* |
| **5** | Documentación y defensa | 17/07/26 – 21/08/26 | Etapa 6 | **§17.6** *(vacía)* · **§18** Cierre · **§19** Anexos |

> **Ojo con el desfasaje de numeración:** el Gantt numera las tareas **0–5**, el §14.2
> numera las etapas **1–6**. Es la misma secuencia corrida en uno. En este mapa y en los
> documentos por etapa se usa siempre la numeración del §14.2 (**Etapa 1 … Etapa 6**),
> que es la que aparece en el texto del informe.

**Y el punto de fondo: el informe está ordenado por sección, no por etapa, y casi no las
menciona.** Las etapas no son una estructura del documento — por eso este mapa existe,
para tener la correspondencia a mano, y por eso hay un ajuste (`AJ-0.06`) que propone
hacerla explícita dentro del propio informe.

**Las fechas del Gantt están vencidas** y eso es un ajuste en sí mismo (`AJ-0.03`).

---

## 1. Las cuatro reglas de este mapa

1. **Etapa 3 conserva su numeración `R-01…R-26`.** Es la única serie que ya estaba
   citada afuera (11 referencias). No se renumera ni se reescribe: este mapa la enruta.
2. **Las etapas 1, 2, 4, 5 y 6 usan la serie nueva `AJ-<etapa>.<nn>`** (`AJ-1.01`,
   `AJ-2.03`, …), y la **crítica de extensión** usa `PODA-nn` (✎ 2026-08-11 —
   [`07-critica-extension-y-poda.md`](07-critica-extension-y-poda.md): qué eliminar o
   comprimir; se aplica **en el mismo pase por sección** que los `AJ-`/`R-`). El
   prefijo `AJ-` estaba libre; se eligió justamente para no chocar con
   `A1–A5` (argumentos de `nucleo/09`), `AF-1…AF-11` (escala de conclusiones),
   `L1–L8` (limitaciones), `E-01…` (exclusiones) ni `T-68…T-84` (tablas).
3. **Hay una etapa 0**, que no es una etapa: son los ajustes transversales del
   frontmatter (§11–§14), que no pertenecen a ninguna. Están en el §3.
4. **Ningún número se cita desde acá.** Las cifras salen de los cuatro índices de
   `e-ovrt_experimental-setup/results/`; el texto largo, de `94` y `92`/`92b`.
5. **Regla de no-anacronismo (fijada por el usuario, 2026-08-11).** El informe narra
   etapas en orden: **una etapa temprana no menciona resultados ni experimentos de
   etapas posteriores** — sería adivinar el futuro. La frontera exacta:
   **decisiones y correcciones de diseño SÍ se aplican hacia atrás** (un redline que
   corrige §17.3 a "la estrategia es E-IND" corrige una decisión, no anticipa un
   resultado); **resultados medidos, refutaciones empíricas y artefactos de evaluación
   NO** — §15/§16 dejan la *brecha* declarada con literatura, §17.1 deja el *criterio*
   o la *decisión* declarada, y **el cruce con lo medido vive en §17.5 y §18**
   (la regla de tres tiempos, `AJ-1.15`/`AJ-5.11`, opera ahí y solo ahí). Caso testigo
   que motivó la regla: el borrador de `AJ-1.02` pedía meter en §15 el keep-up del
   Sprint 2 y los G2A live — datos de Etapa 4/5. Corregido.

---

## 2. El mapa, en una tabla

| Etapa | Sección del informe | Texto actual | Ajustes | Archivo |
|---|---|---|---|---|
| **0** *(transversal)* | §11–§14 | `entregable/96a` | 7 (`AJ-0.x`) | §4 de este documento |
| **1** Investigación del arte y marco teórico | §15 · §16 · Anexo A | `entregable/96c`, `96d`, `96e` §19.1 | 16 (`AJ-1.x`) | [`01-etapa-1-fundamentacion-teorica.md`](01-etapa-1-fundamentacion-teorica.md) |
| **2** Análisis | §17.1 · Anexos C y D | `entregable/96b`, `96e` §19.3–19.4 | 12 (`AJ-2.x`) | [`02-etapa-2-consolidacion-metodologica.md`](02-etapa-2-consolidacion-metodologica.md) |
| **3** Diseño | §17.3 | `entregable/90` | 26 (`R-01…R-26`) | [`03-etapa-3-diseno-arquitectonico.md`](03-etapa-3-diseno-arquitectonico.md) → `material-etapa-3/93` |
| **4** Implementación del prototipo | **§17.4** — *hoy vacía* | — | 12 (`AJ-4.x`) | [`04-etapa-4-implementacion.md`](04-etapa-4-implementacion.md) |
| **5** Evaluación y validación | **§17.5** — *hoy vacía* | — | 13 (`AJ-5.x`) | [`05-etapa-5-evaluacion-y-validacion.md`](05-etapa-5-evaluacion-y-validacion.md) |
| **6** Documentación y cierre | **§17.6** *(vacía)* · §18 · §19 | `entregable/96e` (§18 y §19) | 5 (`AJ-6.x`) | [`06-etapa-6-documentacion-y-cierre.md`](06-etapa-6-documentacion-y-cierre.md) |
| **PODA** *(transversal)* | §15, §16, §17.1, §17.3, §19 | todo lo escrito (~127k palabras) | 18 (`PODA-nn`, ahorro ~34.900 ≈ 27%) | [`07-critica-extension-y-poda.md`](07-critica-extension-y-poda.md) |

**El corte que importa.** Las etapas 1, 2 y 3 son **corrección de texto que ya existe**;
las etapas 4, 5 y 6 son, en su mayor parte, **redacción desde cero sobre secciones
vacías**. En el informe v1.1 los tres placeholders están literalmente escritos así
(`entregable/96e`):

```
### 17.4. Implementación del prototipo experimental
[Agregado futuro correspondiente a la Etapa 4]

### 17.5. Evaluación y validación del prototipo
[Agregado futuro correspondiente a la Etapa 5]

### 17.6. Documentación técnica, repositorio y evidencias de cierre
[Agregado futuro correspondiente a la Etapa 6]
```

---

## 3. Taxonomía y prioridad (la misma del doc 93, sin agregados)

| Tipo | Qué significa |
|---|---|
| **CONTRADICE** | el informe dice algo que la implementación desmiente. No es opinable. |
| **PRECISA** | el informe no está mal, está impreciso o hedgeado donde ya hay certeza. |
| **CONCRETA** | falta material que existe y hay que inyectar (tabla, figura, definición). |
| **EVIDENCIA** | falta declarar qué funciona, cómo se midió, o qué **no** se hizo. |
| **ERRATA** | error de forma o de dato verificable contra la fuente. |

Prioridad: 🔴 crítica · 🟠 alta · 🟡 media · ⚪ baja.

Además hay una categoría que este mapa introduce y que conviene respetar:
**🚫 NO-TOCAR** — cosas que *parecen* errores y no lo son (ver §7). Corregirlas
empeora el informe.

---

## 4. Etapa 0 — ajustes transversales del frontmatter (§11–§14)

Van acá porque no pertenecen a ninguna etapa: son el encuadre del documento.

| ID | Sección | Tipo | Pri | Enunciado | Fuente del texto |
|---|---|---|---|---|---|
| **AJ-0.01** | §12.4 Alcance, límites y condiciones | CONTRADICE | 🔴 | El alcance declarado quedó viejo: **ADR-015 registra que el alcance CRECIÓ**, no que se recortó (E-03 pasó de demostrativa a capacidad operativa medida; E-07 parcial; E-13 ejecutada y refutada). ✎ 2026-08-10: sobre la **distribución MQTT** manda **ADR-016** — dejó de ser exclusión cerrada y es **trabajo comprometido**, se declara con su estado al momento de la entrega (E-06 sigue excluida). ✎ 2026-08-11: sobre el **fine-tuning** manda **ADR-017** — E-04 dejó de ser exclusión y es **jornada experimental comprometida**, encuadrada como rama condicionada por datos y protocolo (nunca "por tiempo"). | `decisiones/adr-015-cierre-de-alcance.md` (§2a/§3/§4/§5 ratificados) + `adr-016-reapertura-acotada-distribucion.md` + `adr-017-fine-tuning-jornada-experimental.md` + `nucleo/10-registro-alcance-y-exclusiones.md` |
| **AJ-0.02** | §11 Glosario y símbolos | PRECISA | 🟠 | El vocabulario canónico vigente es **`person`, `helmet`, `vest`, `bare_head`** (`canonical_v2`); `canonical_cr01_cr02` está deprecado. Y hay que declarar las **colisiones de etiquetas**: "limitación L1" ≠ `L1` de la Fase L · `AF-1…AF-11` ≠ `A1–A5` · **dos series de ADR** (`ADR-001…018` del proyecto vs `ADR-0001…0013` del control-plane, 4 dígitos). | `13-glosario-y-convenciones-de-lectura.md` §4.1–4.3 · `gobierno/99` §4.1–4.2 |
| **AJ-0.03** | §14.3 Cronograma · Figura 1 (Gantt) | ERRATA | 🟡 | **El Gantt está vencido.** Sus seis filas dan: investigación 31/10/25–28/11/25 · análisis 05/12/25–09/01/26 · diseño 16/01/26–06/03/26 · **implementación MVP 20/03/26–29/05/26** · evaluación 12/06/26–10/07/26 · **documentación y defensa 17/07/26–21/08/26**. La implementación siguió hasta agosto, el tramo experimental cerró el 2026-08-09 y la defensa es ~fin de septiembre. Hay que regenerar la figura o declarar la desviación. *(Verificado extrayendo la imagen del `.docx`, 2026-08-10.)* | Figura 1 del `96a` |
| **AJ-0.04** | §14.2 Etapas | PRECISA | 🟡 | Las semanas del plan **no se leen literalmente** (ADR-010 reordenó: plataforma primero, dataset/GT de evaluación al final). Lo que sí vale y conviene explicitar es la **correspondencia 1:1 con las fases de la Tabla 36** — es coherencia metodológica gratis en la defensa. | `nucleo/08` §2.4 + `decisiones/adr-010-secuenciacion-plataforma-primero.md` |
| **AJ-0.05** | §17.2 Costos asociados · §14.4 | EVIDENCIA | 🟡 | **Hueco abierto, no relevado.** Nadie contrastó todavía los costos declarados contra lo efectivamente gastado. Para T1, la extrapolación medida da ≈16 min centrales (prudente 30–45 min; walltime 2 h), `operacion/100` adenda; la cifra histórica “≈1 GPU-h” quedó superada. | a relevar — insumo parcial en `operacion/100` §6 |
| **AJ-0.06** | §14.2 · introducción de §17 | CONCRETA | 🟠 | **El informe está ordenado por sección y casi no menciona las etapas.** Las etapas son la **guía de desarrollo** del proyecto, no una estructura del documento, y hoy el lector no tiene forma de saber qué sección corresponde a qué etapa. Agregar la **tabla de correspondencia etapa → sección** (la del §0 de este mapa): cierra el círculo entre el plan de trabajo declarado en §14 y el desarrollo del producto en §17. | §0 de este documento |
| **AJ-0.07** | fuera de §17.3 | PRECISA | 🟡 | Inventario de datasets desactualizado. **Ya tiene ID propio en Etapa 3: es `R-24`** — se enruta desde acá para que no se pierda, pero su ficha canónica está en `material-etapa-3/93`. | `material-etapa-3/93` · R-24 |

---

## 5. Tablero global

| Etapa | Ajustes | 🔴 | 🟠 | 🟡/🟢 | Con texto ya redactado | Estado del frente |
|---|---:|---:|---:|---:|---|---|
| 0 (transversal) — §11–§14 | 7 | 1 | 2 | 4 | — | relevado acá por primera vez |
| 1 — investigación bibliográfica | 16 | 2 | 6 | 8 | no | relevado (`sintesis` §7), **sin pase de redlines hecho** |
| 2 — análisis metodológico | 12 | 1 | 5 | 6 | parcial (`94` §5) | relevado (`nucleo/08`), sin pase hecho |
| 3 — diseño arquitectónico | 26 | 7 | 10 | 9 | **9 de 26** (`94` §1–§9) | el único frente con hoja de trabajo y casillas |
| 4 — implementación MVP | 12 | — | 8 | 4 | insumos completos (`92`, `92b`, `94` §7–§9) | **§17.4 vacía**: es redacción |
| 5 — evaluación y validación | 13 | — | 10 | 3 | insumos completos (`99` §1, 4 índices); ⏳ `AJ-5.13` abierto (jornada E-04 en curso) | **§17.5 vacía**: es redacción |
| 6 — documentación y cierre | 5 | — | 3 | 2 | insumos completos (`99` §2–§4) | **§17.6 vacía**; §18 escrito pre-resultados |
| **Total** | **91** | **11** | **44** | **36** | 9 | |

**Ninguno de los ajustes está aplicado al `.docx`.** Lo que existe es el relevamiento y, en
9 casos de Etapa 3, el texto listo para pegar.

---

## 6. Orden de trabajo recomendado

El orden de *lectura* es 1 → 6. El orden de *trabajo* no es el mismo, porque las
secciones vacías son el camino crítico y las correcciones de texto no bloquean a nadie:

1. **Etapa 5 — el §17.5** primero. Es la sección que sostiene la defensa y la que tiene
   todos los insumos verificados en disco (T-68…T-84, FIG-A…FIG-F, los 4 índices).
2. **Etapa 4 — el §17.4** en paralelo o inmediatamente después: es descriptiva y sus
   insumos también están completos (`92`, `92b`, `operacion/97`).
3. **Etapa 3 — el §17.3**: el pase de las 26 redlines, empezando por las 7 🔴 (de las
   cuales 4 son contradicciones, que no son opinables). Nueve ya tienen el texto escrito
   en `material-etapa-3/94`.
4. **Etapa 1 — el §15**: los dos huecos estructurales (`AJ-1.01`, `AJ-1.02`) y las erratas
   duras. Se puede hacer último **pero no se puede saltar**: el §17.5 cita al §15 como
   vara, y hoy la vara no está.
5. **Etapa 6 — §17.6/§18/§19**: sale casi solo una vez que están el §17.5 y el §15, porque
   las conclusiones se escriben con la escala `AF` y contra la vara de la literatura.
6. **Etapa 2 — el §17.1** y **Etapa 0**: el resto, mayormente precisiones.

**Lo único que sigue abierto del lado de los materiales** (`gobierno/99` §6, y no bloquea
redactar): anotar **URL + fecha de acceso por video** en los 18 `clip.yaml` del lote de
internet (evidencia perecedera; paso a paso en `operacion/113` §C1, y es del usuario). De
los seis hallazgos del cierre, los otros cinco están cerrados.

---

## 7. 🚫 Lo que NO hay que tocar

| # | Parece un error | Por qué no lo es |
|---|---|---|
| 1 | Nombres de métrica que aparecen **vacíos** en §17.1.5.3.2, §17.1.7 y Tabla 33 | Son **objetos de ecuación de Word** (`t_alert-system`, `t_alert-notification`, `G2A`, `T_persistencia`, `ΔFP_tracker`) que la extracción XML no captura. En el Word original se ven bien. Verificar visualmente, **no** "corregir". (`nucleo/08` §3.) |
| 2 | El pattern set `cr01_cr02_v1` | No se corrige: queda documentado como **configuración de diagnóstico** DBE-imágenes. El oficial es `cr01_cr02_v2`. Citar `v1` como si fuera vigente produce falsos `missed` (F-DR9). |
| 3 | Las `re_alerts` del motor | **No son falsos positivos.** Por ADR-011 el motor emite en cada confirmación y la supresión es política del tramo de distribución. |
| 4 | El BENCH original de 196 imágenes | Se conserva **sin modificar** como artefacto histórico, aunque ~20–25% sea fuera de dominio. El benchmark vigente es `bench_v3` (6.477 imgs). |
| 5 | Los números de documento de `docs/` | El archivado es **lógico**: hay ~2.800 referencias por número. Nunca renumerar ni mover un `operacion/NN`. |

---

## 8. Fuentes de este mapa

Relevamiento propio (2026-08-10) sobre: `entregable/96a` §14.2 (definición de las
etapas), `entregable/96e` (los placeholders de §17.4–17.6), `material-etapa-3/93`
(las 26 redlines), `material-etapa-3/94` (los 9 textos listos), `nucleo/08` §2–§4 (hoy en
`nucleo/historicos/`)
(Etapa 2), `sintesis/resultados-y-conclusiones.md` §7–§9 (Etapa 1 y 5),
`gobierno/99` §1/§4/§6 (materiales de cierre), `decisiones/adr-015`, `specs/40–45`,
`operacion/97` y los cuatro índices de `e-ovrt_experimental-setup/results/`.
