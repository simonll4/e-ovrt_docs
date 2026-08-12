# ADR-016 — Reapertura acotada: la distribución de alertas se implementa, y la puerta se vuelve a cerrar detrás

> **Deroga puntualmente §2b, §2c y §6 de [ADR-015](adr-015-cierre-de-alcance.md).**
> **Ratifica expresamente §2a, §3, §4 y §5 de ADR-015**, que siguen vigentes y son la
> fuente de la sección de límites del informe.

- **Fecha:** 2026-08-10
- **Estado:** Aceptada (usuario, 2026-08-10)
- **Decisión que atiende:** cerrar la **arquitectura** de la plataforma. El sistema emite
  alertas y hoy no hay un lugar que explique dónde se gestiona el ciclo de vida completo
  de una alerta ni hacia dónde se distribuye. ADR-015 §2c había resuelto ese hueco
  declarando la distribución como exclusión cerrada; el usuario decide construirla.
- **Decisor:** usuario, 2026-08-10 (advertido de la colisión con ADR-015 §6, la ratificó)
- **Serie:** proyecto (`ADR-001…016`, tres dígitos). No confundir con la serie local del
  control-plane (`ADR-0001…0013`, cuatro dígitos).

---

## 1. Contexto

ADR-015 (2026-08-05) cerró el alcance al final del tramo experimental. Su §2c declaró:

> *"La distribución MQTT (ADR-005 / spec 45) queda declarada como NO implementada, **y no
> se reabre**. […] Se declara como exclusión ejercida con su justificación, **no como
> deuda**."*

Y su §6 fijó el criterio de invalidación: si entre esa fecha y la defensa se agregaba
cualquier capacidad nueva —nombrando explícitamente la distribución MQTT— el ADR quedaba
**violado**, y había que *"reemplazarlo, no enmendarlo"*.

El motivo declarado para reabrir **no es funcional sino arquitectónico**: la plataforma
tiene una frontera de salida (`control.alert.v1`) que no desemboca en ningún lado. Sin el
módulo, el informe describe una cadena que termina en el aire — y las políticas de
consumo que ADR-011 asignó a la distribución (cooldown, supresión por ventana,
re-notificación, agrupación) quedan sin implementación que las encarne.

## 2. Decisión

**(a) Se reabre la distribución de alertas, con el recorte exacto de ADR-005 y nada más.**
Un canal MQTT + `NotificationEnvelope` + ledger de idempotencia por
`(notification_id, channel)` + retry mínimo + vista en la webconsole existente.
**E-06 sigue excluida**: ni canales adicionales ni dashboard dedicado.

**(b) No se reabre nada más.** Siguen cerradas, con el fundamento que ya tenían:
fine-tuning (E-04), inferencia en borde (EN-3), métricas MOT (E-10) y toda condición CR
nueva. **Esta cláusula reemplaza a ADR-015 §2b y cumple su misma función de freno.**
(✎ 2026-08-11, [ADR-017](adr-017-fine-tuning-jornada-experimental.md): **E-04 sale de
esta lista** — el fine-tuning se ejerce como jornada experimental comprometida. El freno
sigue vigente para EN-3, E-10, E-06 y las condiciones CR nuevas.)

**(c) La implementación no bloquea el informe.** La redacción arranca de inmediato. El
cierre **arquitectónico** —que es el propósito declarado— lo entrega la documentación:
`nucleo/19` consolida la cadena, sus fronteras y el ciclo de vida de la alerta, y no
depende de que aterrice el código. La sección de resultados de distribución se escribe si
y cuando el módulo exista.

**(d) Si el módulo no llega a tiempo, se declara como estaba.** Volver a "exclusión
ejercida con causa" es un desenlace aceptable y previsto, no un fracaso: el registro de
alcance vuelve a la redacción de ADR-015 §2c y el informe no cambia de estructura.

## 3. Por qué derogación puntual y no reemplazo total

ADR-015 §6 pedía reemplazo, no enmienda. Se cumple su **propósito** por una vía que no
destruye lo que ese ADR sostiene:

- Su **§2a** (la tabla del alcance que creció: E-03, E-04, E-07, E-13) y su **§3** (la
  lista de límites que reemplaza a R-13, con las limitaciones L1–L8) son la fuente de la
  sección de límites del informe y están **citadas nominalmente** desde
  `informe/ajustes/gobierno/99-materiales-de-cierre.md` y desde el brief de redacción.
  Reemplazar el documento entero dejaría esas citas colgando y obligaría a re-apuntar
  referencias en cadena — el modo de falla que este proyecto ya pagó caro.
- El §6 fue escrito para impedir que la puerta se reabriera **en silencio**. Un ADR
  sucesor, firmado, que nombra exactamente qué cláusulas caen y cuáles siguen en pie,
  cumple ese propósito íntegramente. Lo que §6 prohibía era la enmienda tácita, no la
  sucesión explícita.

**Queda constancia de que esto es una interpretación**, no una aplicación literal de §6.
Si el tribunal la lee de otro modo, el hecho relevante está igualmente registrado: la
capacidad se agregó después del cierre, con fecha y con causa.

## 4. Fundamento

**Por qué vale la pena.** La cadena `detección → patrón → alerta → notificación → entrega`
es la columna de la arquitectura. Las tres primeras fronteras están implementadas y
medidas; la cuarta estaba solo diseñada. Un sistema que confirma alertas y no las entrega
a ningún lado deja al lector con la pregunta obvia sin responder, y deja a ADR-011 —que
sacó el cooldown del motor a propósito— sin el lugar donde esa política efectivamente vive.

**Por qué el riesgo es menor que en agosto.** ADR-015 §4 advertía contra agregar capacidad
cerca de la defensa. La advertencia sigue vigente y por eso están §2b y §2d. Lo que cambió
es que el recorte de ADR-005 ya está **especificado hasta el detalle** (doc 06 con 20
secciones, spec 45, `informe/92b`): no es diseño abierto, es ejecución de algo escrito.

**Por qué no toca ninguna cifra.** Igual que ADR-015, este ADR no modifica un solo número
medido. El tramo experimental está cerrado y no se re-corre.

## 5. Impacto

- **ADR-015:** §2b, §2c y §6 derogados. §2a, §3, §4 y §5 **vigentes y ratificados**. Su
  banner remite acá.
- **ADR-005:** su condicional deja de estar resuelto en "no". Pasa de *"NO implementado,
  exclusión ejercida y cerrada"* a **implementación comprometida**, con el alcance de §2a.
- **ADR-011:** sin cambios, y refuerza — la política de notificación que asignó al módulo
  de distribución pasa a tener implementación.
- **R-13** (lista de límites del informe): la fila *"Distribución no implementada — SIGUE,
  ahora como exclusión ejercida y cerrada, no como deuda"* se reescribe como **trabajo
  comprometido, con su estado al momento de la entrega**. El resto de la lista de
  ADR-015 §3 no cambia.
- **Informe:** la arquitectura cierra por `nucleo/19` con independencia del código. La
  sección de resultados de distribución es condicional.
- **`nucleo/10`:** el ítem de distribución y las referencias a ADR-015 se anotan.

## 6. Criterio de invalidación

Este ADR queda violado si ocurre cualquiera de estas dos cosas:

1. **El alcance de §2a se desborda** — aparece un segundo canal, un dashboard dedicado, o
   cualquier capacidad de E-06. La señal es simple: código de distribución que no esté en
   el recorte de ADR-005.
2. **La implementación compromete el cronograma del informe.** Si la redacción se detiene o
   se posterga por esperar al módulo, se aplica §2d: se revierte a exclusión declarada y
   se sigue. La distribución es el complemento de la arquitectura, no su condición.

## Referencias

ADR-015 §2a/§2b/§2c/§3/§4/§6 (cierre de alcance; qué se deroga y qué se ratifica) ·
ADR-005 (recorte, canal MQTT, repo propio) · ADR-011 (frontera de la política de alertas:
el motor emite siempre, la supresión es de distribución) · `nucleo/06` (diseño completo del
módulo) · `nucleo/19` (cierre de la arquitectura y ciclo de vida de la alerta) ·
`specs/45-distribucion-alertas.md` · `informe/ajustes/material-etapa-3/92b-concrecion-distribucion-alertas.md` ·
`nucleo/10` E-06 · `informe/ajustes/gobierno/99-materiales-de-cierre.md` (R-13).
