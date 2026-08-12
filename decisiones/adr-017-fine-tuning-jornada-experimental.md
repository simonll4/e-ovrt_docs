# ADR-017 — El fine-tuning (E-04) se ejerce: jornada experimental completa, y el encuadre nunca fue "falta de tiempo"

> **Deroga puntualmente la mención a E-04 en la cláusula (b) de [ADR-016](adr-016-reapertura-acotada-distribucion.md)**
> (que sigue vigente y cumpliendo su función de freno para EN-3, E-10, E-06 y toda
> condición CR nueva) **y la fila E-04 de ADR-015 §2a** en cuanto declara la rama "no
> ejercida por secuenciación". **Ratifica** todo lo demás de ADR-015 que ADR-016 ya
> ratificó (§3 límites L1–L8, §4, §5).

- **Fecha:** 2026-08-11
- **Estado:** Aceptada (usuario, 2026-08-11)
- **Decisión que atiende:** el encuadre del fine-tuning en el informe y su ejercicio.
  La documentación de redacción venía declarando E-04 como exclusión "por presupuesto
  de tiempo" (texto de julio), luego enmendado a "por secuenciación" (ADR-015). El
  usuario rechaza ambas lecturas como encuadre del informe: **el cronograma lo define
  el propio proyecto** — no hay plazo externo que lo corra — y el fine-tuning fue,
  desde el planteo inicial, una **rama experimental condicionada** (Tabla 37) cuyas
  restricciones reales son **de datos y de protocolo**, no de cómputo ni de plazo.
  Decisión: se lleva a cabo una **jornada completa de fine-tuning** y se documenta lo
  que produzca — resultados y limitaciones.
- **Decisor:** usuario, 2026-08-11
- **Serie:** proyecto (`ADR-001…017`, tres dígitos). No confundir con la serie local
  del control-plane (`ADR-0001…0013`, cuatro dígitos).

---

## 1. Contexto

El encuadre experimental-condicionado está en el informe **desde el diseño
metodológico**, no es una reinterpretación tardía: la Tabla 37 dice que la regla *"no
prescribe que el fine-tuning deba ejecutarse; define cuándo vale la pena hacerlo sin
distorsionar el objetivo principal del prototipo experimental"*, y fija el orden —
baseline zero-shot primero, ajuste después. Ese prerequisito está cumplido: la
baseline quedó establecida y el benchmarking está cerrado.

El camino está preparado y con costo medido (doc 100): splits materializados sin
leakage (train ∩ `bench_v3` = 0 intersección verificada), escalera T1–T3 con
criterios go/no-go pre-registrados (`contingencia/20`), loop de linear probing con
smoke verde end-to-end, costo dimensionado **≤1 GPU-h en A30 para T1**, y el clúster
**Mendieta (CCAD-UNC, 2×A30 por nodo, Slurm)** disponible como Training Node. El
cómputo, entonces, **no es la restricción**.

Las restricciones reales — las que la jornada tiene que atravesar y el informe tiene
que contar — son:

1. **Datasets de entrenamiento y validación.** F-100.1: no existe un split de
   validación con `bare_head` que no sea estrato del bench congelado (solo `shel5k`
   trae la clase nativa, y `shel5k` *es* parte de `bench_v3`) — el monitoreo del
   entrenamiento quedaría ciego en la clase central de la hipótesis. El doc 100 §4
   deja **tres enmiendas posibles**, ninguna ejecutada; la decisión es previa a
   correr T1.
2. **Licencias y transporte.** *Entrenar en el clúster, evaluar local*: al clúster
   solo sube material CC BY 4.0 (`construction_site_safety`, `ppe_siabar`); las
   imágenes de `chv` y `shel5k` no salen de la máquina (doc 100 §6.3).
3. **Protocolo.** Los go/no-go de la Tabla 37 (ganancia exigible, retención
   generalista) y el riesgo documentado de **erosión de la capacidad
   open-vocabulary** (§15.2.4.5) que motiva el enfoque.
4. **Logística del clúster.** Entorno reproducible (CUDA/torch), transporte del
   subset, y el puente de evaluación del modelo ajustado contra `bench_v3`, que
   falta armar (doc 100 §6.2).

En el repo convivían dos capas de causa para el no-ejercicio: *"presupuesto de
tiempo del proyecto"* (julio) y *"secuenciación"* (enmienda ADR-015, 2026-08-06).
**Ninguna de las dos es el encuadre que el informe debe dar**: la primera es falsa
como causa (el tiempo lo administra el proyecto) y ambas dan la impresión de un
descarte por cronograma que nunca fue la naturaleza de la rama.

## 2. Decisión

**(a) Se ejerce E-04 como jornada experimental completa, con todo lo que conlleva:**
preparación de datos y entorno, entrenamiento en Mendieta, evaluación contra
`bench_v3` y documentación. La forma es la **escalera pre-registrada**
(`contingencia/20` §6): **T1 (linear probing) es la entrada**; el escalamiento a
T2/T3 lo gobiernan los go/no-go pre-registrados y la Tabla 37 — se documenta hasta
dónde llegó la escalera y por qué, sin prometer tiers por adelantado. El objeto
documentable es la jornada entera: qué se logra, qué no, y con qué causa.

**(b) El encuadre del informe cambia de "exclusión" a "rama experimental ejercida".**
Desde las etapas iniciales el fine-tuning fue una rama comparativa condicionada por
la regla metodológica y por la disponibilidad de datos — **nunca un descarte**.
Queda **prohibida la causa "falta de tiempo" / "presupuesto de tiempo"** en todo
texto del informe y de sus materiales de redacción. "Secuenciación" solo sobrevive
como descripción del **orden metodológico** (baseline primero, que es lo que la
Tabla 37 exige), nunca como causa de no-ejecución.

**(c) Los resultados se leen como el resto del tramo experimental:** son EL DATO de
una combinación, con sus limitaciones — los go/no-go son criterios de lectura y de
escalamiento, no una vara de aprobado/fallado. Un desenlace negativo (sin ganancia
exigible, o con erosión open-vocabulary medida) es un **resultado documentable**,
no un fracaso ni una omisión.

**(d) Las puertas técnicas previas no se saltean.** Antes de pedir turno en
Mendieta: decidir F-100.1 (decisión del usuario entre las tres enmiendas del doc
100 §4), entorno reproducible, transporte, y el puente de evaluación — la checklist
completa es doc 100 §6 y sigue siendo **la puerta**.

**(e) No se reabre nada más.** EN-3, E-10, E-06 y toda condición CR nueva siguen
cerradas con el fundamento que ya tenían. La cláusula (b) de ADR-016 sigue vigente
para todo lo que no sea E-04.

**(f) La jornada no bloquea el informe** (mismo patrón que ADR-016 §2c/§2d): la
redacción no espera al clúster. La sección comparativa se escribe con lo que la
jornada haya producido al momento de la entrega, y ese estado se declara tal cual —
con causa técnica, nunca temporal.

## 3. Fundamento

**Por qué la causa temporal es inaceptable.** Nadie externo fija el plazo: el
proyecto define su propio cronograma y ya excede en volumen a un trabajo final de
grado típico — la decisión de acotar es soberana, no una carrera perdida. Declarar
"tiempo" como causa sería falso, y además la posición defensiva más débil posible
ante el tribunal, cuando la causa verdadera — regla metodológica + disponibilidad
de datos de validación (F-100.1) + licencias — es más fuerte y está documentada.

**Por qué ahora sí se ejerce.** El prerequisito metodológico (baseline zero-shot,
benchmarking completo) está cerrado; el costo está medido y es chico (≤1 GPU-h para
T1); y el riesgo que justificaba el orden — que la rama compitiera con el cierre de
resultados del núcleo — desapareció: el tramo experimental core está cerrado y no
se re-corre.

**Por qué no toca ninguna cifra.** Igual que ADR-015 y ADR-016: ningún número
medido se modifica ni se re-corre. La jornada agrega una rama comparativa nueva
sobre particiones disjuntas ya verificadas (0 intersección con `bench_v3`), y sus
deltas se reportan contra la baseline congelada según el protocolo ya especificado
(Tabla 32).

## 4. Impacto

- **`nucleo/10`:** la ficha E-04 y su fila en la tabla resumen pasan de
  *"condicionada no ejercida"* a **"rama experimental comprometida (jornada), con
  estado a la entrega"**. El banner remite acá.
- **`contingencia/20`:** deja de ser contingencia *"si sobra tiempo"* — pasa a ser
  **el plan pre-registrado de la jornada**. Sus recetas, presupuestos y go/no-go
  siguen vigentes como regla de escalamiento. Su §7 ("el won't se sigue declarando
  por presupuesto de tiempo") queda **derogado**.
- **ADR-015:** fila E-04 de §2a anotada (remite acá). **ADR-016:** cláusula (b)
  anotada — E-04 sale de su lista de frenos; el freno sigue para el resto.
- **Materiales de redacción del informe:** AJ-2.11 (`ajustes/02`), AJ-6.05
  (`ajustes/06`), el estado E-04 de `ajustes/04`, y las filas TN/DA-07 de los
  redlines (`material-etapa-3/93` y la prosa de `94` §8) se reescriben con el
  encuadre nuevo. El texto del informe entregable no contenía la causa temporal
  (verificado 2026-08-11) — el riesgo entraba por estos materiales.
- **`operacion/100`:** sin cambios de contenido — sigue siendo la puerta técnica.
  Su D-100.2 ("va al final") queda **satisfecha**, no derogada: el "final" llegó.
- **Kit (`informe-project-kit/`):** se regenera tras la propagación.

## 5. Criterio de invalidación

Este ADR queda violado si ocurre cualquiera de estas cosas:

1. **Reaparece la causa temporal** — "falta de tiempo", "presupuesto de tiempo" o
   equivalentes — como causa del estado de E-04 en cualquier texto nuevo del
   informe o de sus materiales.
2. **La jornada saltea una puerta técnica** — se pide turno con F-100.1 sin
   decidir o con la checklist del doc 100 §6 incompleta. Gastar el turno entrenando
   algo cuya clase central no se puede monitorear es exactamente lo que la puerta
   existe para impedir.
3. **Se escala a T2/T3 sin cumplir los go/no-go pre-registrados** (Tabla 37 y
   `contingencia/20` §6).
4. **La jornada bloquea el informe.** Si la redacción se detiene por esperar al
   clúster, se aplica §2f: se escribe el estado real a la entrega y se sigue.

## Referencias

Tabla 37 (`informe/entregable/96b` §17.1.9, la regla condicionada) · §15.2.4.5
(erosión open-vocabulary) · `operacion/100` (§3 costo medido, §4 F-100.1, §6
checklist de la puerta) · `contingencia/20` (escalera T1–T3, go/no-go
pre-registrados, presupuestos GPU) · `nucleo/10` E-04 · ADR-015 §2a ·
ADR-016 cláusula (b) · `informe/ajustes/02` AJ-2.11 · `informe/ajustes/06` AJ-6.05 ·
`informe/ajustes/material-etapa-3/93` (TN, DA-07) y `94` §8 · doc 20 §2 (Mendieta
como TN presupuestado).
