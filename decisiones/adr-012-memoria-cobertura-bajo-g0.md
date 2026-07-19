# ADR-012 — Memoria de cobertura bajo G0: inaplicable sin identidad; la histéresis la subsume

> **✎ Estado de implementación (2026-07-18):** implementado y **falsación SUPERADA**
> (2026-07-10, doc 34): los dos tests condición-de-merge pasaron (gate F1=1.0
> verificado significativo + test de parpadeo) y un par discriminante confirmó la
> decisión; la reversión prevista no se activó. Detalle:
> [`estado-de-implementacion-adrs.md`](estado-de-implementacion-adrs.md).

- **Fecha:** 2026-07-09
- **Estado:** Aceptada — **sujeta a falsación por test** (ver §"Criterio de falsación")
- **Decisión que atiende:** hueco detectado al bajar el spec 41 §2 a plan de
  implementación. No estaba resuelto en ADR-002 (que llama al cambio "refactor menor
  de clave de estado"), ni en spec 41, ni en el doc 07.
- **Decisor:** usuario, 2026-07-09 (delegó la elección y pidió documentarla y
  asegurarla con tests)

## El hueco

Spec 41 §2.1 establece que bajo `granularity: scene` (G0) la clave de estado pasa a
`(pattern_id, source_id)`, que la evidencia por unidad se computa "igual que hoy (por
persona: matching 1:1, región, **memoria de cobertura**)" y luego se agrega, y que
"**`detection_id` deja de usarse como identidad, siempre**".

Las tres afirmaciones no son simultáneamente satisfacibles. La memoria de cobertura
(`coverage_memory_ms/frames`) es, por construcción, **estado por sujeto sostenido a
través de frames**: "este sujeto tuvo el EPP asociado hace menos de N ms, seguí
tratándolo como cubierto". Bajo G0 no hay `track_id` y `detection_id` queda prohibido
como identidad. **No queda ninguna identidad a la cual colgar esa memoria.**

`subject_absent_timeout_*` tiene la misma forma pero sí admite una traducción natural
a escena; la memoria de cobertura no.

## Decisión

1. **Bajo `granularity: scene`, la memoria de cobertura no se aplica.** El motor
   ignora `coverage_memory_ms/frames` para patrones de escena. No es un error de
   configuración (`field_v1` la trae y debe seguir cargando): el motor la ignora y
   **declara la degradación con causa `coverage_memory_unsupported_scene`**, del mismo
   modo que G1 sin `track_id` declara `no_track_id` (spec 41 §2.1). La causa entra en
   `degradation_causes[]` del `summary.json` (spec 41 §4).

2. **La memoria de cobertura sobrevive únicamente bajo `granularity: subject` con
   `track_id` presente**, que es el único régimen donde hay identidad de sujeto. Es
   decir: es una capacidad de G1. No se elimina código — coherente con ADR-011 §3,
   que ya trata `realert_cooldown_*` como capacidad del motor no usada por la
   plataforma.

3. **`subject_absent_timeout_*` sí se reinterpreta a nivel escena** bajo G0: si no se
   observó **ningún** sujeto de la clase del patrón durante la ventana, el episodio de
   escena resuelve. La traducción es exacta porque "no hay sujetos" no requiere saber
   quiénes eran.

4. **El pattern set de plataforma `cr01_cr02_v2` deja `coverage_memory_*` sin
   configurar** (None), consistente con (1). `field_v1` la conserva como perfil de
   diagnóstico/labs, documentado como tal.

## Fundamento

1. **A la escala temporal de la plataforma, la memoria es redundante.** El pattern set
   v2 (spec 41 §7) fija `confirm_after_ms` 4000 (PR-01) y 7000 (PR-02), con histéresis
   de resolución de 2000 y 3000 ms. La memoria de cobertura fue diseñada para amortiguar
   **parpadeo del detector**, que ocurre a escala de frames (decenas de ms). La
   histéresis de `resolve_after_ms` ya absorbe ese ruido con dos a tres órdenes de
   magnitud de margen: un EPP que parpadea 100 ms no acerca la condición a resolver
   cuando resolver exige 2000 ms continuos de cobertura.

2. **Elevarla a nivel escena cambia su significado y produce falsos negativos.** Una
   memoria de escena diría "la escena estuvo sin evidencia hace poco, tratá esto como
   cobertura". Pero la escena no distingue personas: si el trabajador A está cubierto y
   el trabajador B se saca el casco dentro de la ventana, **la violación de B queda
   suprimida**. Es el mismo defecto de accidente-de-clave que ADR-011 §3(b) señaló para
   el cooldown ("mismo trabajador" → "misma cámara"), y se rechaza por la misma razón.

3. **La alternativa de reintroducir identidad débil (asociación por IoU intra-escena)
   se descarta:** es un tracker de facto, no está en ninguna spec, y reemplaza una
   identidad frágil prohibida (`detection_id`) por otra identidad frágil implícita, sin
   GT de identidades con el cual validarla — exactamente lo que ADR-002 excluyó al
   declarar G1 demostrativa.

4. **Coherencia con ADR-011.** ADR-011 §1 ubica la memoria de cobertura del lado del
   motor (semántica de patrón, absorbe ruido perceptual) frente a la política de
   notificación. Este ADR no la mueve de lado: la deja en el motor y establece que
   **su régimen de aplicabilidad es G1**. Son dos fronteras distintas — motor↔distribución
   (ADR-011) y qué-sostiene-G0 (este ADR).

## Criterio de falsación (exigido por el usuario)

Esta decisión es una **apuesta empírica**: que la histéresis subsume el parpadeo. Se
declara falsable y se verifica con dos tests, ambos condición de merge del motor:

1. **Gate de regresión (spec 41 §2.2):** F1 = 1.0 en ambas granularidades sobre el
   fixture `cr01_cr02_temporal` regenerado a `clip_gt.v2`, con `coverage_memory`
   desactivada bajo escena. Si el fixture pierde F1 = 1.0 por parpadeo del detector que
   la memoria antes tapaba, **la decisión está mal** y se revisa este ADR.

2. **Test de parpadeo dedicado:** un fixture donde un EPP desaparece y reaparece dentro
   de una ventana menor que `resolve_after_ms`, con la condición NO debiendo resolver ni
   re-alertar. Si la histéresis no lo absorbe sin memoria de cobertura, **la decisión
   está mal**.

Si cualquiera de los dos falla, la opción viva es (2) del §Fundamento —memoria a nivel
escena— asumiendo explícitamente el falso negativo de la alternancia de personas, que el
doc 07 D2.2 ya declara como limitación conocida de G0.

## Impacto

- **Motor (spec 41 §2):** `_memory_covers` se aplica solo bajo `granularity: subject`
  con `track_id`; bajo escena se ignora y se declara `coverage_memory_unsupported_scene`.
  `_expire_absent_subjects` se reinterpreta a nivel escena.
- **Spec 41 §7:** corregir "memoria de cobertura y expiración de sujetos — semántica de
  patrón que SE CONSERVA" → la expiración se conserva (reinterpretada a escena); la
  memoria de cobertura queda como capacidad de G1.
- **Spec 41 §4:** `degradation_causes[]` suma `coverage_memory_unsupported_scene`.
- **`cr01_cr02_v2`:** `coverage_memory_*` sin configurar.
- **Ninguno sobre contratos:** el campo sigue existiendo en `PatternTimingConfig`.

## Referencias

ADR-002 (G0 núcleo / G1 demostrativa), ADR-011 §1 y §3(b) (frontera motor↔distribución;
el precedente del cooldown que cambia de significado bajo G0), spec 41 §2/§4/§7,
doc 07 D2.2 (alternancia de personas dentro de un episodio de escena), doc 01 §12.1
(origen de la memoria de cobertura en la rama `mati`).
