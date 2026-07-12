# Auditoría adversarial de los docs 91–94, y plan de cierre a 11 semanas

- **Fecha:** 2026-07-12 · **Defensa:** ~fin de septiembre 2026 (**quedan ~11 semanas**)
- **Qué es esto:** el resultado de auditar **con hostilidad** todo lo que se generó en el relevamiento del
  informe (docs 91–94): verificación factual contra código y artefactos, consistencia interna entre los
  cuatro documentos, y alineación con el alcance cerrado (doc 10) y con el plazo.
- **Por qué existe:** porque la primera versión de esos documentos tenía **un JSON fabricado presentado como
  artefacto real**, **una cifra falsa**, **un número sobrevendido** y **una cifra estrella sin respaldo en el
  repo**. Todo eso ya está corregido. Este documento deja el rastro, porque un error corregido en silencio
  vuelve.

---

## 1. Veredicto

**Lo bueno:** ningún redline expande el alcance. Los cuatro documentos están *cerrando* el proyecto, no
abriéndolo. De los 26 redlines, **22 son escritura pura** sobre evidencia que ya existe. El riesgo que se
temía —"reabrir alcance a 11 semanas de la defensa"— **no se materializó**.

**Lo malo:** la auditoría factual encontró **diez afirmaciones incorrectas** en lo que yo mismo escribí, y
tres de ellas hubieran sido letales en una defensa. La ironía es evidente: el trabajo consistía en auditar
un capítulo por falta de rigor, y el material de la auditoría tenía sus propios agujeros. **Están todos
reparados** (§2), y ahora hay una regla estructural para que no vuelvan (§3).

**Lo que sigue:** tres acciones esta semana, y el resto es escritura (§5).

---

## 2. Lo que la auditoría encontró — y cómo quedó

### 2.1 🔴 El número estrella del TFG no tenía respaldo en el repo

Las cinco métricas que íbamos a poner en el informe (**P 0,50 · R 1,00 · F1 0,67 · t_alert-system 4000 ms ·
TTFD 0 ms · SDR 0,999**) **no tenían artefacto archivado**. Lo único que existía en disco era un
`temporal_evaluation.json` con **SDR 0,803** — que pertenece al **smoke de plomería corrido con detector
`mock`**, no al benchmark. Cualquiera que auditara el repositorio hubiera encontrado 0,803 y concluido que
el número del informe estaba inflado.

**Resuelto.** Se **re-corrió el benchmark real** (replay de las detecciones de GDINO-tiny sobre `cb_b01_p7`
contra la referencia anotada, con el conjunto de patrones oficial) y **se archivaron los artefactos**:

```
docs/operacion/datos/95-2026-07-12-bench-cb_b01_p7-gdino-temporal_evaluation.json
                     95-2026-07-12-bench-cb_b01_p7-gdino-alerts.jsonl
                     95-2026-07-12-bench-cb_b01_p7-gdino-control-summary.json
                     95-2026-07-12-bench-cb_b01_p7-gdino-media-summary.json
                     95-2026-07-12-bench-cb_b01_p7-gdino.replay-config.yaml
```

Reproduce **exactamente** los números: precisión 0,5 · exhaustividad 1,0 · F1 0,667 · **SDR 0,998635** ·
TTFD 0,0 ms · alerta CR-01 a los **4000,0 ms exactos** (unidad `frame_000120`) y CR-02 a los 7000,0 ms.
El número era correcto; **lo que faltaba era la evidencia**. Ahora está.

### 2.2 🔴 El DTO que iba al informe estaba fabricado

El bloque JSON que el doc 94 presentaba como "una línea real de `detections.jsonl`" —**la pieza que el tutor
pidió con nombre propio**— era un **híbrido**: mezclaba valores de tres artefactos distintos, incluía una
detección `helmet` que no existía en esa línea, un *bounding box* que no existe en ninguna línea de la
corrida, campos (`strategy`, `condition_id`) **que el sistema no serializa**, y tiempos de postproceso
inventados.

Es el peor error posible del conjunto: un dato falso, verificable, en el lugar exacto donde el tutor pidió
concreción. **Resuelto:** los docs 92 y 94 ahora transcriben la línea **literal** de `frame_000120` —la
unidad en la que confirma la alerta—, con el recorte de detecciones **declarado**.

**Y el hallazgo colateral vale más que la corrección:** al transcribir de verdad, se ve que **el evento no
lleva hoy `strategy` ni `condition_id`** (existen en el modelo, valen `null`, no se serializan). Es decir:
**el evento de percepción no transporta la condición de riesgo asociada**. Es aditivo y barato de poblar —
pero no se puede escribir en el informe que ya la lleva.

### 2.3 🔴 G2A: presentábamos como "dentro de presupuesto" un número medido con detector simulado

El doc 94 decía: *"La instrumentación temporal opera dentro de presupuesto → G2A p50 14,7 ms / p95 31,8 ms"*.
Esa corrida usó **`EOVRT_MODEL_REF=mock`**. Con el detector real:

> **G2A p50 = 2214 ms · p95 = 2604 ms · `p95_within_budget: false`** — un orden de magnitud por encima del
> presupuesto declarado (50–250 ms).

Poner el número del mock en un capítulo de verificación, sin decir que es un mock, es exactamente el tipo de
cosa que un tribunal encuentra.

**Resuelto, y convertido en hallazgo.** La formulación nueva es más fuerte que la vieja:

> *La instrumentación de G2A opera y **detecta el incumplimiento**: con detector de referencia el p95 es de
> 31,8 ms (dentro del presupuesto); con el detector open-vocabulary evaluado asciende a 2604 ms y el sistema
> lo declara fuera de presupuesto. **La restricción operativa está en el detector, no en la plataforma.**
> Un instrumento que sólo devuelve resultados favorables no es un instrumento.*

Y encaja con el hallazgo del doc 31: *no hay un modelo que haga las dos cosas* — los que sostienen CR-01 no
siguen el ritmo de la cámara (14–22 % de keep-up), y los que lo siguen son ciegos a CR-01.

### 2.4 Las otras siete correcciones

| # | Estaba mal | Está bien |
|---|---|---|
| 1 | "`det_000001` recorre 1831 px **entre frames consecutivos**" | 1831 px es el **rango total** de la corrida; el salto máximo entre cuadros consecutivos es **~1749 px**. (El argumento se sostiene igual — pero la cifra era falsa y verificable.) |
| 2 | "137 eventos de patrón, 0 alertas" (el cero silencioso) | El run **fue podado**. El equivalente vivo da **77 / 0**, y ese sí está en disco. |
| 3 | "los **cinco** modelos evaluados" | Son **seis**. |
| 4 | "El cooldown **no existe** en el motor" | **Sí existe** (`realert_cooldown_ms`, `_cooldown_ok()`). Lo correcto: *"el conjunto de patrones adoptado no lo configura"*. Si alguien abre el código y encuentra lo que el informe negaba, el daño es peor. |
| 5 | Byte-identidad "300 unidades" | Son **dos corridas distintas**: la byte-identidad se verificó con **40** unidades; las 300 son otra corrida. **Ambas con detector mock.** |
| 6 | "El motor ya tiene una **costura de pose**" | Es una **heurística de relación de aspecto**, no soporte de pose. Llamarla "pose" invita a que te pidan el keypoint. |
| 7 | Cifras de percepción atribuidas al doc 35 | Son de **otra corrida** (la del clip `cb_b01_p7`). Dos corridas de 733 unidades con números distintos: había que aclarar cuál. |

### 2.5 Consistencia interna

También se corrigieron: tres **citas del capítulo que no eran literales** (R-01, R-04 y R-15 — esta última
con una elisión que **cambiaba el sentido** de la frase original), una referencia rota (R-08 apuntaba a dos
secciones y el texto sólo cubría una), la lista de "lo no implementado" (el doc 91, el redline y el texto
listaban **cosas distintas** — justamente ahí), y la contradicción `no aplicable` / `no interpretable` en la
métrica G2A, que es precisamente la distinción que el trabajo vende como diferencial.

**Se agregaron dos redlines que faltaban:**
- **R-25** — el contrato de la **referencia temporal** (`clip_gt.v2`), la convención de identidad
  fuente↔clip (sin la cual el emparejamiento **da cero en silencio**) y los cinco hitos por alerta.
- **R-26** — la **extensibilidad medida**. Ver §4: es, probablemente, lo más valioso de todo esto.

---

## 3. La regla que evita que esto vuelva a pasar

Los diez errores tienen **una sola causa**: números y ejemplos copiados de un documento a otro, cada copia
perdiendo el contexto de qué corrida y qué detector los produjo. La solución es estructural, no de esfuerzo:

> **Una sola fuente de verdad por tipo de contenido.**
>
> | Documento | Rol | Puede contener |
> |---|---|---|
> | **92** | **Fuente de verdad verificada** | Rutas, líneas de código, artefactos literales, y la **tabla canónica de cifras** (§10) con la corrida y el detector de cada una. |
> | **91** | Diagnóstico | **Cita** cifras del 92. No las re-tabula. |
> | **93** | Hoja de redlines | Cita el 92 y remite al 94. |
> | **94** | Texto para el informe | **Ninguna cifra que no esté en el 92 §10.** Ningún JSON que no sea transcripción literal. |
>
> Y la regla de oro, que ya estaba escrita y se violó: **si un campo no está en el código, no va al
> informe.** La única forma de que este material envejezca mal es que alguien "mejore" un esquema al
> transcribirlo.

---

## 4. Lo que la auditoría encontró **de más** — y que es lo mejor de todo

El capítulo, incluso corregido, mide **latencias, pérdidas y ventanas temporales**. Todo eso lo podría medir
un sistema de vocabulario cerrado. **No mide lo único que un detector cerrado no puede hacer.**

Tu tesis no es "OVD detecta mejor" — es *"qué se logra con una plataforma que expresa condiciones en
lenguaje, sin entrenar"*. El resultado más defendible que tenés, y que **no estaba escrito en ninguna parte**,
es el **costo marginal de incorporar una condición de riesgo nueva**:

- Una **condición nueva del mismo tipo** (sujeto sin elemento de protección) → **sólo configuración**: una
  entrada declarativa en el conjunto de patrones + las formulaciones de prompt. **Cero código, cero
  reentrenamiento.**
- Una **familia nueva** de condiciones (relacional, zonal, de trayectoria) → **un evaluador nuevo**.

Ese contraste **delimita la frontera real de la extensibilidad por lenguaje**, en lugar de prometer que
"todo es configurable". Es una contribución arquitectónica, es barata de escribir, y si el mini-experimento
A1 (doc 10, ítem 8) llega a correrse, su número va ahí. **Vale más, en la defensa, que media docena de
latencias.** Quedó como **R-26** y su texto está en el doc 94 §9.

---

## 5. Plan de cierre a 11 semanas

### 5.1 Tres cosas que dependen de vos, esta semana

| # | Decisión | Por qué no puede esperar |
|---|---|---|
| **1** | **Firmar (o no) el acta del catálogo de prompts (`edir_v1`)** | Es **el único bloqueo de código que depende de vos**. De esto depende si el redline R-01 puede prometer la comparación de estrategias como *resultado del trabajo* (opción a) o sólo como *protocolo especificado* (opción b). **Escribir (a) y no correrlo es la peor opción.** |
| **2** | **ADR-015 — recorte final de alcance** | Los docs 94/91 declaran como "no implementados" el **tracker/G1** y la **distribución MQTT**… pero el **doc 10 los tiene DENTRO del alcance** (ítems 10 y 5). Son, literalmente, los dos primeros de tu propio orden de sacrificio — pero un sacrificio ejecutado en el informe **sin actualizar doc 10** deja tres documentos diciendo cosas distintas. **1 hora de trabajo.** |
| **3** | **Empezar a grabar el banco de clips** | Es **la única tarea con lead time irreductible** y la única que no puedo hacer yo. Todo R3, la campaña de estrategias y los videos de la defensa dependen de clips que **todavía no existen**. Si esto se corre más allá de la semana 4, la defensa está en riesgo. |

### 5.2 Una decisión de código, chica y de alto rendimiento

**Agregar `track_id` (y un bolsillo `attributes`) al contrato del plano de medios: media jornada.**

Hoy la situación es asimétrica y débil: el contrato del **consumidor** tiene `track_id` y el motor lo usa,
pero el contrato del **productor** no tiene **ningún** campo opcional ni bolsillo de extensión. El redline
R-07 —la respuesta al pedido más profundo del tutor— enuncia la regla *"las capacidades nuevas entran como
campo opcional"* y **no puede mostrarla del lado que importa**.

Con el campo presente (aditivo, sin bump de versión, **sin implementar el tracker**), la afirmación pasa de
*"prometemos que el contrato crece"* a *"mirá el esquema"*. Es la diferencia entre una promesa y una
demostración, y cuesta una línea. **Recomendado. Decidilo vos.**

### 5.3 Qué se puede escribir YA (no depende de datos): ~85 % de los redlines

Arrancá en paralelo con la grabación: **R-01 a R-11, R-14 a R-20, R-22, R-24, R-25, R-26**. Todo el texto
está redactado en el doc 94 o instruido en el 93.

**Tiene que esperar:**
- **R-12** (verificación): escribí ya las filas de plataforma —todas tienen su número—; dejá la fila de las
  cinco métricas como **verificación de instrumento** hasta que llegue el GT humano y la campaña.
- **R-13 y R-21** (límites y estado del backlog): dependen de ADR-015.

### 5.4 Secuencia

| Sem | Vos | Yo |
|---|---|---|
| **1** (ahora) | CVAT: validar herramienta + **pasada humana sobre `cb_b01_p7`**. **Firmar acta `edir_v1`.** Empezar consentimientos. | ADR-015. Campo `track_id` aditivo (si lo aprobás). Redlines R-01…R-11, R-14…R-20, R-22, R-24, R-25, R-26 sobre el Google Docs. |
| **2–3** | 🔴 **GRABAR EL BANCO** (8–10 clips escenificados + los 3 de la defensa). | Evaluadores de la comparación de estrategias. Overlay renderer. Figuras. |
| **3–4** | Anotar los clips + doble anotación del 20 % con coeficiente de acuerdo. | **Mini-experimento A1** (condición nueva por configuración) — el número de R-26. |
| **5–6** | Revisar el capítulo redlineado. | **Campañas**: comparación de estrategias, banco de clips, EBE en dos nodos. |
| **6** | *Punto de decisión:* ¿distribución MQTT sí o no? | Si sí, 3–5 días. Si no, se cierra como exclusión y listo. |
| **7–8** | — | **Congelar.** Cero capacidades nuevas. Cerrar R-12/R-13/R-21 con números reales. |
| **9–10** | Videos de la defensa, ensayo. | Reporte consolidado, tablas y figuras finales. |
| **11** | Buffer. | Buffer. |

**Regla de oro (ya está en el doc 02 §7): después de la semana 8 no se agrega capacidad. Sólo se corre, se
mide y se escribe.**

### 5.5 Qué sacrificar, si hay que sacrificar

En orden, y **es tu propio orden de sacrificio del doc 10**:

1. **El tracker / G1 demostrativa.** Quedate **sólo con el campo opcional en el contrato**: rinde el 100 %
   del argumento del tutor ("el evento crece sin romperse") al 5 % del costo. El tracker corriendo no agrega
   un solo punto de defensa.
2. **La distribución MQTT.** Cuesta 3–5 días y su único rédito es una métrica que **queda mejor declarada
   como "no aplicable / no hay canal"** — porque ese "no aplicable" **es** tu diferencial metodológico.
   Sacrificarla no te resta: **te ilustra la política de aplicabilidad**.
3. **Las figuras.** Dibujá **tres** (vista lógica, vista de procesos, máquina de estados). Las otras, bloques
   de 20 minutos o nada. No inviertas cuatro días de dibujo con el banco sin grabar.
4. **Las métricas derivadas propias.** Ya bajé el tono en el doc 94: el diccionario y el criterio de relojes
   son imprescindibles; `t_compute-budget` va **a nota al pie** y no se vende como contribución. Reclamar un
   "aporte instrumental propio" es invitar a que lo auditen.

**Lo que NO se sacrifica bajo ninguna circunstancia:** R-01/R-05 (la contradicción de estrategia), R-04 (el
caveat de granularidad de escena), R-06/R-07 (el pedido literal del tutor) y R-13 (los límites declarados).

---

## 6. Estado de los cinco documentos

| Doc | Estado |
|---|---|
| **91** — relevamiento | ✅ v2, corregido. Ya no re-tabula cifras: cita el 92. Su plan de acción se eliminó (vivía duplicado con el 93 y ya había divergido). |
| **92** — anexo técnico | ✅ v2, corregido. DTOs literales, cooldown con su matiz, G2A con la verdad, y **§10: la tabla canónica de cifras**. |
| **93** — redlines | ✅ v2. Citas literales corregidas, **26 redlines** (se agregaron R-25 y R-26), casillas de decisión intactas. |
| **94** — texto para el informe | ✅ v2, reescrito completo. Sin un solo número mal atribuido. **§9 nueva: extensibilidad medida.** |
| **95** — este | ✅ Auditoría + plan. |

**Artefactos nuevos en el repo:** los cinco archivos del benchmark reproducido, en `operacion/datos/`.
**Nada commiteado** — está todo listo para que lo revises.
