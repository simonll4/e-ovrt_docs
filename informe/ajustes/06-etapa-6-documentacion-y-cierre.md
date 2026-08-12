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
- **Que `docs/` es un repo git local sin remote**, por decisión del proyecto, y que el
  respaldo es copia a otro disco.
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

- **El fine-tuning dejó de ser trabajo futuro** ✎ 2026-08-11: **ADR-017 lo puso en
  alcance como jornada experimental comprometida** — escalera T1→T2/T3 con go/no-go
  pre-registrados, **≈1 GPU-h medido** para T1 y nodo de entrenamiento disponible
  (Mendieta, CCAD-UNC). Si a la entrega la jornada produjo resultados, se reportan como
  rama comparativa con sus limitaciones; si quedó a medias, **lo pendiente se declara
  como estado con causa técnica, no como promesa** — y lo que sí sigue siendo trabajo
  futuro son los tiers que los go/no-go no habiliten (T2/T3 sin ganancia exigible
  previa). *Decía "no ejercido por secuenciación; la continuación más obvia"*.
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
| 5 | El módulo de distribución como funcionando | Mientras no haya código verificado: es **trabajo comprometido** (ADR-016) que se reporta con su estado a la entrega. |
| 6 | "L4 se levantó" | Se **precisó** (D-113.1). |

## 4. Fuentes

`gobierno/99` §2–§4 · `sintesis/resultados-y-conclusiones.md` §1, §2, §8, §9, §11 ·
`nucleo/10-registro-alcance-y-exclusiones.md` · `nucleo/19` (ciclo de vida de la alerta) ·
`decisiones/adr-005`, `adr-015`, `adr-016`, `adr-017` ·
`operacion/100` §6 (costo del fine-tuning), `operacion/113` §C1 (el residuo de licencias) ·
`e-ovrt_datasets/datasets/registry/license_registry.md`.
