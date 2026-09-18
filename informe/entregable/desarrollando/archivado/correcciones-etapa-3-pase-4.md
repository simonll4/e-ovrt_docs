# Correcciones — pase 4 sobre §17.3 (Diseño arquitectónico): consolidación narrativa

> ✅ **APLICADO Y VERIFICADO el 2026-09-03.** Base **v1.5** → salida
> ✎ **2026-09-04: el usuario aceptó esta entrega, y más tarde el pase de la Etapa 4 obligó a
> corregir un token —la remisión de §17.3.6.1 pasa de «sección 17.4.6» a «17.4.4»—, que se aplicó en
> limpio. El documento vigente es hoy `…_17.3_…_v1.7.docx`; la estructura de este acta no cambia.**
>
> **`E-OVRT-VDP_Seccion_17.3_Diseno_Arquitectonico_v1.6 (sugerencias sin aceptar).docx`**,
> con control de cambios sin aceptar. Compuerta de verificación **verde: 0 fallas, 0 avisos**
> (`herramientas/verificar_v16_17_3.py`). Aplicador: `herramientas/aplicar_v16_17_3.py`.
> Diagnóstico previo: `desarrollando/analisis-17-3-etapa-3.md`.
> Traducción de la numeración vieja: **`desarrollando/mapa-secciones-17-3-v1-6.md`** (obligatoria
> para leer las actas E3-01…E3-42 y las 26 redlines, que citan la numeración de la v1.4/v1.5).
>
> Unidades de este pase: **E3-43 … E3-62**. Decisiones: **D-A … D-M** del análisis, con dos
> enmiendas declaradas (D-D y D-H). No reabre ninguna decisión firmada: siguen rigiendo D1–D4 y
> la regla de autocontención del pase 1, D-P2-1…D-P2-6 del pase 2 y D-P3-1…D-P3-9 del pase 3.

---

## A. Qué cambió, en una tabla

| Métrica (vista aceptada) | v1.5 | v1.6 | Δ |
|---|---:|---:|---:|
| Palabras de prosa | 13.174 | **10.075** | **−24 %** |
| Palabras en tablas | 4.278 | 3.323 | −22 % |
| Títulos totales | 61 | **30** | −51 % |
| · nivel 3 · nivel 4 · nivel 5 | 18 · 39 · **4** | 11 · 19 · **0** | −7 · −20 · **−100 %** |
| Tablas | 17 | **14** | −3 |
| Figuras | 6 | **4** | −2 |
| Dos puntos en prosa | 73 | **0** | −100 % |
| Punto y coma en prosa | 86 | **0** | −100 % |
| Rayas en prosa | 32 | **2** | −94 % |
| «debe/deben» | 87 | **9** | −90 % |
| Metadiscurso | 10 | **0** | −100 % |
| Futuro de obligación («deberá») | 3 | **0** | −100 % |
| Párrafos de más de 150 palabras | 2 | **0** | −100 % |
| Pares de oraciones repetidas entre secciones | 16 | **3** | −81 % |
| Oración media | 22,4 palabras | 22,2 | igual |

Los tres pares que sobreviven son falsos positivos del detector: dos enumeran los mismos
componentes desde ángulos distintos y el tercero es la fórmula de remisión «se documenta en la
sección 17.4», usada dos veces con contenidos distintos.

**Sobre la extensión.** El análisis estimó ~8.800 palabras de prosa (−32 %) *antes* de escribir.
Al aplicar la regla de cero pérdida de información (D-P4-1, del usuario), la poda posible sin
sacrificar contenido se detiene en **10.075 (−24 %)**: lo que quedaba después de eliminar la
repetición era contenido, no grasa. La diferencia entre −24 % y −32 % es exactamente lo que en la
Etapa 2 se resolvió con un **pase de poda por aporte aparte** (pase 5), decidido por el usuario
sobre cifras y no sobre estimaciones. Ese pase queda disponible, no ejecutado.

---

## B. Estructura nueva

Once secciones de nivel 3 y diecinueve de nivel 4. Cero nivel 5.

| Nueva | Título | Viene de |
|---|---|---|
| 17.3.1 | Propósito y pregunta rectora | 17.3.1 + 17.3.2 |
| 17.3.2 | Alcance, capacidades y decisiones arquitectónicas | 17.3.3 + 17.3.4 |
| 17.3.3 | Vista general y patrones de acople | 17.3.5 |
| 17.3.4 | Configuración experimental, vocabulario y estrategia del núcleo | 17.3.6 + 17.3.9.2 |
| 17.3.5 | Diseño conceptual del plano de medios | 17.3.7 |
| 17.3.6 | Diseño conceptual del plano de control | 17.3.8 + 17.3.9.1 |
| 17.3.7 | Distribución de alertas confirmadas | 17.3.10 |
| 17.3.8 | Contratos, trazabilidad y evidencia visual | 17.3.11 + 17.3.12 |
| 17.3.9 | Observabilidad y aplicabilidad de métricas | 17.3.13 |
| 17.3.10 | Escenarios experimentales y topología de referencia | 17.3.14 + 17.3.15 |
| 17.3.11 | Riesgos, plan de materialización y cierre | 17.3.16 + 17.3.17 + 17.3.18 |

Prosa por sección: 197 · 658 · 600 · 1.396 · 1.468 · 2.193 · 680 · 1.109 · 495 · 821 · 410.

---

## C. Las unidades

### E3-43 · §17.3.2 «Insumos metodológicos» se funde en la introducción (D-B)
Los seis párrafos «de X se deriva Y» anticipaban, uno por uno, el alcance, la estrategia del
núcleo, los escenarios, los roles y la política de evidencia. Su idea rectora —los insumos
metodológicos operan como restricciones y cada módulo se deriva de una decisión previa— pasa al
primer párrafo de §17.3.1. Cierra los comentarios 1 y 2 del colega, que se **re-anclan** a ese
párrafo. 506 palabras fuera.

### E3-44 · §17.3.1 se reescribe alrededor de la pregunta rectora
Los párrafos 1 y 3 decían lo mismo. El párrafo de los dos planos se reduce a una oración con
remisión a **§16.5.3**, que es lo que pedía el comentario 0 (sus números —16.5.3.1 y 16.7.5— no
existen en §16 v1.1; los correctos son 16.5.3 y 16.7.3). La pregunta rectora encabeza en vez de
cerrar. Primer sitio de voz D-P3-9: «criterios de observabilidad que **deberán acompañar**» →
«que **acompañan**». 259 → 197 palabras.

### E3-45 · §17.3.3.1 «Alcance del núcleo» se funde en la entrada de su sección
Sus cuatro párrafos parafraseaban la Tabla 39, el diseño de prompts, los escenarios y la política
de evidencia visual. Quedan dos párrafos en la entrada de la nueva §17.3.2. Cierra el comentario 3
(«asegurarse que las demás 17.3.3.x quedaron alineadas»): ya no hay 17.3.3.x desalineadas porque
la subsección desaparece. Segundo sitio de voz D-P3-9 («decisiones que deberán conservarse»).

### E3-46 · §17.3.4 «Principios» se convierte en la entrada de la Tabla 41
Las cinco oraciones «El primero es X: …» reformulaban las decisiones DA. Pasan a un párrafo que
presenta la tabla, conservando los cuatro ejes en negrita y sus referencias (DA-01…DA-13). El
criterio transversal de evolución incremental cierra el bloque después de la tabla. Cinco dos
puntos y cinco fórmulas «El primero es» fuera. Tercer sitio de voz D-P3-9 («reglas que deberán
preservarse»). 201 + 254 → 208 palabras.

### E3-47 · Tabla 41, dos celdas (comentarios 4 y 5 del usuario)
La justificación de **DA-03** pasa de 70 palabras a una oración. La decisión **DA-11** se reduce a
la decisión propiamente dicha, porque el criterio *fail-open* se define en §17.3.5.2. Los dos
comentarios conservan su ancla dentro de la celda.

### E3-48 · La prosa posterior a la Tabla 41 se elimina
La glosa conjunta de DA-08/DA-09 vive ahora en §17.3.8.3 (evidencia visual, con los criterios de
acceso, retención y anonimización incorporados), la de DA-13 en §17.3.7 y las «tres precisiones de
lectura» en §17.3.10. 179 palabras fuera, cero contenido perdido.

### E3-49 · §17.3.3 se vuelve la única casa de los dos patrones de acople
El párrafo de 254 palabras se parte en tres. El primero fija el gobierno por interfaces
gobernadas por configuración, el segundo el bus con publicador-suscriptor y serialización binaria,
y el tercero la regla de persistir antes de publicar, con la afirmación de que la persistencia **no
constituye un tercer patrón de acople**. A cambio, §17.3.6.1, §17.3.6.3, §17.3.7, §17.3.8.2 y el
cierre dejan de re-explicarlos. Cero párrafos de más de 150 palabras en el capítulo.

### E3-50 · §17.3.4 concentra configuración, prompts y estrategia
La entrada de la sección y §17.3.6.1 decían tres veces que la configuración gobierna la corrida,
se resuelve antes de ejecutar y permite atribuir resultados. Quedan tres párrafos. El título de
nivel 4 «Función arquitectónica de la configuración experimental» desaparece.

### E3-51 · §17.3.6.3 remite a §17.1.5.3 en lugar de re-argumentar (D-J)
Los dos primeros párrafos repetían el argumento de la sensibilidad al prompt y del inglés como
idioma primario **con las mismas cinco citas** que §17.1.5.3 (Du et al., 2022; Zhou et al., 2022;
Changpinyo et al., 2021; Radford et al., 2021; Sharma et al., 2018). Pasan a una remisión y §17.3
queda **sin citas bibliográficas**. La lista global no cambia: §17.1 conserva las cinco.

### E3-52 · §17.3.6.4 recorta la glosa de E-DIR/E-IND/E-HYB a una remisión (**E3-42 / D-E2-2**)
Es el handoff que estaba abierto desde el pase 3. La Etapa 2 bautizó los tres códigos en
**§17.1.5.3** de la v1.15, de modo que la glosa de 70 palabras se convierte en la remisión prevista
(«las estrategias directa (E-DIR) e híbrida (E-HYB) definidas en la consolidación metodológica»).
Cierra el comentario 6 («revisar que esté esto desarrollado en etapa 2»), que conserva su ancla
sobre el texto nuevo. El párrafo baja de 153 a 87 palabras.

### E3-53 · La estrategia del núcleo se muda a su sección dueña (D-P3-4)
§17.3.9.2 —la adopción de E-IND por auditabilidad y la conservación de E-DIR/E-HYB como ramas
comparativas— pasa a §17.3.4.3, que es la sección dueña del concepto. §17.3.9.1 y §17.3.9.3 se
eliminan por repetición y la sección §17.3.9 desaparece.

### E3-54 · Tabla 43 se reduce al núcleo y a las ramas comparativas (D-C)
Las ocho filas de CR-03…CR-06 son literalmente el contenido de la Tabla C.1 del Anexo C, y §17.3
no las diseña (núcleo-solo, D4). La tabla queda en **6 filas** (encabezado, tres del núcleo y dos
de rama E-DIR) y su leyenda pasa a «Vocabulario de prompts en inglés del núcleo validable y de las
ramas comparativas». La prosa y la nota remiten al Anexo C. 414 → 176 palabras de tabla.

### E3-55 · §17.3.7 se reordena alrededor del flujo y absorbe sus criterios
El flujo operativo pasa a ser el eje. «Criterios de diseño aplicados al plano de medios» (cinco
párrafos «El primer criterio…») y «Control de ritmo según tipo de fuente» desaparecen como
títulos. Lo que aportaban —ruta no bloqueante, variabilidad temporal visible, adaptadores que
absorben la heterogeneidad, no trasladar responsabilidades del control— queda en dos párrafos de
cierre del flujo, y la política de ritmo se integra a su etapa. 1.969 → 1.468 palabras, dos títulos
de nivel 4 menos.

### E3-56 · §17.3.8.3 pierde sus cuatro títulos de nivel 5
El motor de evaluación pasa a **una sola subsección en prosa continua**: qué es, la definición de
patrón con sus **siete elementos** (que se conservan íntegros, incluidas la región cefálica para
PR-01 y el torso para PR-02), la granularidad, los niveles del catálogo y las salidas. Se elimina
el párrafo que resumía las siete viñetas, la tercera formulación de «detección ≠ patrón» y el
párrafo de la «cadena operativa completa», que es la Tabla 16 de §17.1. El ciclo de evaluación se
reubica en §17.3.6.1, junto a la máquina de estados. Se repara «reconstuir». Cuatro títulos de
nivel 5 fuera, que eran los únicos del capítulo.

### E3-57 · Tabla 44 deja de repetir la Tabla 21 de §17.1 (D-D, **enmendada**)
La columna «Evidencia y regla de evaluación» reproducía las reglas de activación que fija
§17.1.5.2. Sus seis celdas se acortan a la dependencia arquitectónica, y la nota remite a
§17.1.5.2 para severidad, evidencia y persistencia. **Enmienda a D-D:** la columna **no se
suprime**. Borrar una columna con control de cambios es frágil y el objetivo —quitar la
duplicación— se cumple igual acortando las celdas. 457 → 232 palabras de tabla.

### E3-58 · §17.3.8.4 enuncia la regla de arranque en vez de un orden incompleto
Decía que «una corrida en vivo se inicia primero en el plano de control y luego en el plano de
medios». Es verdadero pero incompleto, porque el orden efectivo incluye al módulo de distribución
entre ambos. Pasa a la regla general —todo consumidor se suscribe antes de que su productor
publique, y el orquestador verifica esa precondición— con remisión a §17.4 para el orden efectivo.

### E3-59 · §17.3.10 y §17.3.11 se funden y pierden su prosa defensiva (D-E)
«Fronteras informacionales de intercambio» recapitulaba en ocho oraciones fronteras ya explicadas
y queda en una sola, la que afirma que las fronteras son lógicas. La **Tabla 47** (hechos
persistibles) se elimina: solapaba con la Tabla 46 y su contenido cabe en un párrafo, porque con la
regla de persistir antes de publicar lo que se intercambia es lo que se persiste. El tramo de
distribución pierde sus tres títulos de nivel 4 y el detalle operativo del ledger baja a §17.4
(**D-I**, ver §E). La política de evidencia visual queda como única casa de la minimización.

### E3-60 · §17.3.13 pierde la Tabla 49 y sus cinco títulos (D-F)
El «Diccionario de métricas» reproducía definiciones de §17.1.7.3, §17.1.7.5, la Tabla 29 y el
Anexo D. Se elimina con remisión, y lo que §17.1 **no** tiene se conserva en prosa: los cuatro
estados de aplicabilidad con sus causas típicas, el criterio de relojes y el anclaje de las
métricas en las transiciones del motor. La nota de la Tabla 47 (antes 48) incorpora que la medición
del plano de medios **empieza en el ingreso de la unidad al host y no en la captura física**.
Se eliminan las reglas de reporte que pertenecen a §17.5. Cinco títulos → ninguno.

### E3-61 · §17.3.14 y §17.3.15 se funden, y la Tabla 51 se elimina (D-G)
La remisión rota **«sección 17.1.4.4»** se corrige a **§17.1.4.2**, que es donde viven los
escenarios en la v1.15. Las subsecciones de DBE y EBE, de 54 y 56 palabras, se funden en la
entrada. La **Tabla 51** duplicaba la Tabla 17 de §17.1 salvo su última columna, cuyo contenido
pasa a prosa. Los roles funcionales se vuelven subsección y remiten a §17.1.4.1. Siete títulos de
nivel 4 → tres.

### E3-62 · Figuras: caen dos, se renumeran las cuatro que quedan (D-H, **enmendada**)
La **Figura 4.3** (plano de control, tres cajas) y la **Figura 4.6** (EN→CPN←TN) no agregaban
información sobre la prosa y la tabla que acompañaban. Las cuatro restantes se renumeran **4.1
(vista conceptual) · 4.2 (flujo del plano de medios) · 4.3 (máquina de estados) · 4.4 (cadena de
traducción)** y **cada una se cita en prosa**, cosa que ninguna hacía. **Enmienda a D-H:** la
cadena de traducción cierra el plano de control en vez de abrirlo, en una subsección propia
(§17.3.6.4); así la figura no se mueve dentro del documento y el orden de lectura mejora, porque
la cadena se resume después de haber descrito los dos planos.

### E3-63 · Las notas de tabla y de figura entran en la misma vara
Cuatro notas que el pase no había tocado conservaban los últimos dos puntos y punto y coma del
capítulo. Se reescriben sin ellos, y §17.3 queda en **cero dos puntos y cero punto y coma en toda
su prosa**, notas incluidas.

---

## D. Lo que este pase NO tocó

- Las filas de las Tablas **39, 41, 46, 51 (antes 54) y 52 (antes 55)**, que son la interfaz de
  verificación con §17.4 y §17.5.
- La definición de patrón en siete elementos, la máquina de cinco estados, *fail-open*,
  persistir antes de publicar, los huecos de secuencia, los invariantes `source_id = clip_id` y
  «la incertidumbre no fabrica una infracción», los cinco hitos, escena contra sujeto, la
  exclusión de métricas MOT sin excluir la identidad, el cero silencioso, los cuatro estados de
  aplicabilidad, el cooldown fuera del motor, las re-alertas que no son falsos positivos y el
  carácter asistivo y no identificatorio.
- Los **7 comentarios**: se conservan con su ancla. Dos (1 y 2) se re-anclan al párrafo que
  absorbe el material que comentaban. **Ninguno se marca resuelto**: cuándo y sobre qué documento
  se cierran lo indica el usuario.
- **Autocontención y no-anacronismo**: verificados en cero, como estaban.

---

## E. Handoffs que este pase abre

| # | Qué | Dueño |
|---|---|---|
| **E4-31** | El detalle operativo del ledger que sale de §17.3 (**D-I**) debe aterrizar en §17.4: la unidad de conteo del tramo es la notificación y no la fila, y una notificación no entregada deja una fila por intento más la del descarte definitivo; al reutilizar un directorio de salida la generación anterior se archiva íntegra y la deduplicación considera todas las generaciones. **§17.4 v1.6 hoy no lo dice.** §17.3 conserva la clave de idempotencia, los cinco resultados de entrega y la latencia por modalidad | Etapa 4 |
| **INT-1** | Pegar la **FIG-E producida** (`informe/figuras/`, PNG 300 dpi) en lugar de la imagen embebida de la máquina de estados: la embebida no dibuja la reapertura a `candidate` que advierte el README de las figuras | Integración |
| **INT-2** | Numeración global de figuras: §17.3 usa el esquema 4.x del documento standalone | Integración |
| **INT-3** | Numeración global de tablas: §17.3 queda en **39–52** (antes 39–55); con la renumeración 16–36 de §17.1 el corrimiento se resuelve en la integración | Integración |
| **INT-4** | «Evento de detección» en la Tabla 16 de §17.1 v1.15 contra «evento de percepción», que es el término firmado en el pase 1 de la Etapa 3 | Integración |
| **RES-1** | Residuo tipográfico de todo el capítulo: la fuente monoespaciada quedó aplicada dentro de palabras («frame»work, «person»al) en los párrafos que este pase no reescribió. Se corrige donde se toque texto, no en un pase propio | Integración |
| **RES-2** | «vídeo» y «video» conviven en el capítulo. Los párrafos reescritos usan «video» | Integración |

Además, la **v1.4** se archivó: era **byte a byte idéntica a la v1.5** (mismo sha256), de modo que
en `desarrollando/` queda una sola versión previa.

---

## F. Verificación ejecutada

`herramientas/verificar_v16_17_3.py` — **0 fallas, 0 avisos**. Comprueba:

1. **Integridad.** XML bien formado. `comments.xml`, `commentsExtended.xml`, `styles.xml`,
   `numbering.xml` y `settings.xml` **idénticos** a la v1.5. Las 6 imágenes siguen en el paquete.
   Los **21 `w:sectPr`** se conservan (regla de oficio: los párrafos que los llevan nunca se
   borran, se les reemplaza el contenido). Las 17 tablas siguen en el XML, tres de ellas con todas
   sus filas marcadas como borradas. Los 7 comentarios conservan ancla y referencia.
2. **Reversibilidad.** Rechazar todos los cambios devuelve **exactamente** el texto de la v1.5.
3. **Estructura.** 11 secciones de nivel 3 con numeración contigua, 19 de nivel 4, **cero de
   nivel 5**, 30 títulos en total, ninguna sección como contenedor vacío.
4. **Estilo.** Prosa ≤ 10.100 palabras, dos puntos ≤ 2, punto y coma ≤ 2, rayas ≤ 10, cero
   párrafos de más de 150 palabras, cero metadiscurso, cero futuro de obligación.
5. **Tablas y figuras.** Leyendas contiguas 39–52 y 4.1–4.4, cada tabla y cada figura citada
   **exactamente una vez** en prosa, ninguna cita a una tabla inexistente.
6. **Remisiones.** Presentes 16.5.3, 17.1.4.1, 17.1.4.2, 17.1.5.2, 17.1.5.3, 17.1.7.3, 17.1.7.5,
   17.3.8, 17.4, 17.4.6, 17.5 y los Anexos C y D. Ausentes 17.1.4.4, 17.1.5.4.2 y toda remisión a
   la numeración interna vieja. Autocontención y no-anacronismo en cero.
7. **Contenido.** Veinte bloques imprescindibles verificados uno por uno (§D).
8. **Duplicación.** Ninguna oración de 12 o más palabras repetida. Cero citas bibliográficas.

### Un defecto del propio instrumental, reparado

`herramientas/verificar_entregable.py` informaba **«el documento NO trae cambios controlados»**
sobre un documento que traía 198 inserciones y 1.053 borrados. La comprobación corría sobre el XML
pasado por `ElementTree`, que reescribe el prefijo `w:` a `ns0:`, de modo que la búsqueda de
`w:ins` y `w:del` **nunca acertaba**: todo documento con cambios controlados se venía informando
como si no los trajera, incluidas las entregas de la Etapa 2. Se corrigió leyendo el XML crudo y se
agregó el test del caso positivo, que faltaba —el único que existía cubría el caso negativo, y por
eso el defecto sobrevivió—. `herramientas/tests/`: **63 tests en verde** (antes 62).

**Trampas que este pase encontró y que conviene recordar.** (1) El `w:sectPr` final del cuerpo no
pertenece a ningún párrafo: un troceado por unidades que sólo recorre `w:p` y `w:tbl` lo pierde en
silencio, y el documento queda sin su última sección. (2) Al calcular la vista aceptada o
rechazada, las marcas autocerradas (`<w:ins/>` y `<w:del/>` de la marca de párrafo) hay que
quitarlas **antes** que las emparejadas: si no, el patrón de la marca emparejada toma la
autocerrada como apertura y se come contenido válido. (3) Un párrafo borrado que contiene una
imagen deja la imagen viva si sólo se marcan los runs con texto.
