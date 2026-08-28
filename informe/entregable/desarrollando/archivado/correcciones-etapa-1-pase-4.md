# Correcciones a la Etapa 1 — pase 4: cierre de formato y flujo de trabajo

- **Fecha:** 2026-08-27 · **Sobre:** `Etapa 1 — copia ajustada E1 2026-08-27 (2).docx`
  (26.685 palabras: §15 + §16 + Anexo A + Referencias).
- **Qué es:** el pase más corto de la serie. **El contenido de la Etapa 1 está cerrado.** Lo
  que queda son **dos defectos de formato** y una **regla de flujo de trabajo** para que no
  vuelvan a aparecer.
- **IDs:** **E1-52** y **E1-53**.

---

## 0. Veredicto: el pase 3 se aplicó, y bien

Verificado por diff contra la entrega anterior y por extracción. **Todo lo sustantivo entró:**

| Unidad | Estado | Verificación |
|---|---|---|
| **E1-25** el mecanismo central de la tesis | ✅ **lo mejor del pase** | §16.3.4 nueva: *"Composicionalidad, Negación y Condiciones Definidas por Ausencia"*, con ARO (Yuksekgonul et al., 2023) y Winoground (Thrush et al., 2022), y las **dos formulaciones** enunciadas como alternativas conceptuales sin decir cuál eligió el proyecto. Exactamente lo pedido |
| **E1-24** la contradicción con §15 | ✅ | La afirmación sobre familias arquitectónicas desapareció de §16.3.5 **y** de §16.7; el puntero roto "§15.2.4.5" también |
| **E1-36** la ecuación vacía | ✅ | `t_G2A = t_capture + t_transport + t_preprocess + t_inference (1)` |
| **E1-37** descomposición de 4 componentes | ✅ | §16.5.2 reescrita como *"Descomposición Instrumental de Glass-to-Algorithm"*, con `t_preprocess` definido y su fila propia |
| **E1-38** productor/consumidor y pub-sub | ✅ | §16.5.3 *"Separación de Planos y Flujo Productor-Consumidor"*; MQTT ×3, Cugola ×3, contrapresión presente |
| **E1-26** las cuatro secciones de criterios | ✅ | §16.3.6 pasó a *"Dimensiones de Comparación de Modelos OVD"*; §16.4.4, §16.5.5 y §16.7.4 eliminadas o reconvertidas |
| **E1-44 / E1-45** §16.7.4 y §16.7.5 | ✅ | Ambas eliminadas; *"event sourcing"* ya no aparece |
| **E1-46** Tabla 12 | ✅ | Columna renombrada a *"Restricción que impone…"*; *"Decisión de diseño implicada"* desapareció |
| **E1-47** la obligación AAIP | ✅ | Resuelta **como corresponde**: `[[PENDIENTE: definir con el equipo la aplicabilidad de esta inscripción al contexto experimental y documentar el recaudo adoptado en §17.1 y §17.4]]`. No la inventó: la marcó |
| **E1-33 / E1-34** Anexo A | ✅ | Licencias corregidas (*"API cerrada; Apache-2.0 aplica al SDK, no a los pesos"*) y la matriz pasó de **12 a 20 filas**, ahora **con Grounding DINO Swin-T/Swin-L y MM-Grounding-DINO** |
| **E1-35 / D-E1-9** tablas huérfanas | ✅ | Tabla A.3 (servidores) eliminada; A.2 reescrita en términos de límites frente a la alerta |
| **E1-40** letras de cita falsas | ✅ | `Jeong` y `X. Wang 2020` desaparecieron con las subsecciones duplicadas; `Shi et al., 2016` quedó sin letra |
| **R1 / R2 / R3** residuales de §15 | ✅ | Regularización ahora en prosa · rótulo de la ficha en negrita · **las cuatro altas de referencias están** (Kumar, Lee 2023, OASIS, Ultralytics) y Luxonis con su letra |
| Referencias | ✅ | 83 entradas · **cero huérfanas** · cero citas sin entrada |
| No-anacronismo | ✅ | Cero identificadores de plataforma, cero resultados propios, cero andamiaje |

**Extensión:** §16 pasó de 30.749 a **11.563** palabras y el Anexo A creció de 771 a **3.945**
(la inversión de PODA-17). §15 quedó en 10.399. Total de la Etapa 1: **26.685**.

---

## 1. Lo que falta

### E1-52 · 🔴 · Cinco encabezados perdieron su estilo de título

Son **contiguos**, lo que delata que se pegó texto plano sobre esa región:

| Sección | Título |
|---|---|
| §16.5.3 | Separación de Planos y Flujo Productor-Consumidor |
| §16.5.4 | Computación en el Borde y Filtrado Cercano al Origen |
| §16.5.5 | Brecha de Evaluación Integrada |
| **§16.6** | **Marco Ético-Legal para el Análisis Automatizado de Video en Entornos Laborales** |
| §16.6.1 | Encuadre ético-legal y carácter asistivo |

**El texto está y es correcto** — el problema es que esos párrafos son prosa común con
aspecto de título. Consecuencias: **no aparecen en el índice automático**, no entran en la
numeración de campos de Word, y §16.6 —una sección de primer nivel— queda visualmente colgada
dentro de §16.5.

**Arreglo:** aplicarles el estilo de encabezado correcto (`Heading 3` a §16.5.3/.4/.5 y
§16.6.1; `Heading 2` a §16.6), del mismo nivel que sus hermanas. No hay que tocar una palabra
del contenido.

### E1-53 · 🟡 · Hueco de numeración en §16.7

Quedó **§16.7.1 · §16.7.2 · §16.7.6**: la subsección sobreviviente conservó su número viejo
tras eliminarse las tres del medio. Se ve en el índice. **Renumerar a §16.7.3**, y verificar
que las remisiones a las preguntas rectoras sigan resolviendo (§17.1 las invoca por número).

### Y una decisión del equipo, no del redactor

**D-E1-11** sigue abierta y ahora está correctamente marcada en el texto: la aplicabilidad de
la inscripción ante la AAIP al contexto experimental, y qué recaudo se documenta en
§17.1/§17.4. El marcador `[[PENDIENTE]]` viaja hasta que el equipo lo resuelva.

---

## 2. Flujo de trabajo: por qué no hay que usar Drive

Los dos defectos que quedan **no son errores de redacción: son daño de transporte**. Aparecieron
al conectar el Project a una unidad de Drive y editar el documento allí. Ninguno se ve leyendo
el texto, y ambos son invisibles para quien revisa contenido.

**El punto de fondo: ir a Drive era innecesario.** El paquete de la etapa que está cargado en
el Project **ya contiene el texto vigente completo** — la extracción `90d`. El documento nunca
hizo falta como fuente; conectarlo solo agregó una copia peor.

### Cómo se trabaja de ahora en más

1. **Todo dentro del Project.** Knowledge = `00-contexto-base.md` + `01-etapa-N-activa.md`.
   Sin conectores de Drive, sin editar en la nube. El texto vigente de la sección está en el
   paquete.
2. **La entrega es un `.docx` por sección**, armado sobre una **copia** del DOCX base de
   formato, nunca sobrescribiéndolo.
3. **Cada título con su estilo de encabezado real.** Nunca negrita imitando un título. Si se
   elimina una subsección, **renumerar sus hermanas**.
4. **Con cambios controlados activados** — o, en su defecto, con el bloque de trazabilidad por
   unidad. Las tres entregas anteriores llegaron sin ellos y auditar qué se movió costó
   reconstruir el diff cada vez.
5. **Sin markdown crudo** (`###`, `|---|`) y **sin identificadores internos** (`AJ-`, `R-`,
   `PODA-`, `E1-`, líneas `SHA-256`, cabeceras `> Seleccion:`). Los `P-E1-xx` de las preguntas
   rectoras **sí** son parte del informe.
6. **Los marcadores `[[…]]` viajan.** No se completan con estimaciones ni se borran.
7. **Delta de referencias explícito**: altas en APA 7 con DOI/URL, y bajas de lo que dejó de
   citarse.

Estas siete reglas quedaron escritas **dentro del propio kit** (sección *"Cómo se trabaja y
cómo se entrega"* del contexto base), así que viajan con el knowledge y no dependen de que
alguien las recuerde.

### Verificación mecánica, del lado del equipo

Se agregó `herramientas/verificar_entregable.py`. Sobre cualquier entrega:

```bash
python3 herramientas/verificar_entregable.py "<entrega>.docx" --seccion 15 --seccion 16 --seccion 19
```

**Falla** (y hay que corregir) con: títulos numerados sin estilo de encabezado · huecos y
desórdenes de numeración · fugas de andamiaje interno · markdown pegado sin convertir · citas
sin entrada en referencias.
**Informa** (para revisar): referencias que el cuerpo ya no cita · la misma autoría citada con
años distintos · inventario de marcadores · si faltan los cambios controlados.

Sobre esta entrega reporta exactamente los dos defectos de arriba, y nada más. Los dos habrían
aparecido en un segundo en vez de requerir una lectura completa.

---

## 3. ✎ Resuelto el 2026-08-27 — **no hizo falta ChatGPT**

E1-52 y E1-53 eran dos arreglos mecánicos sobre un documento **cuyo contenido ya estaba
correcto**. Devolvérselo a ChatGPT habría significado regenerar 26.685 palabras para cambiar
cinco estilos de párrafo: mucho riesgo de regresión de contenido, y una verificación completa
más, a cambio de nada. Se resolvieron de forma determinista sobre el `.docx`.

**Documento final: `Etapa 1 — final 2026-08-27.docx`** (la entrega original no se sobrescribió).

| Qué se hizo | Cómo |
|---|---|
| §16.5.3, §16.5.4, §16.5.5, §16.6.1 → `Heading3` | Se les trasplantó el `w:pPr` y el `w:rPr` de **§16.5.2**, una hermana sana del mismo nivel |
| §16.6 → `Heading2` | Donante: **§16.5**, hermana sana del mismo nivel |
| §16.7.6 → **§16.7.3** | Reemplazo del número en el texto del título |

El mapeo no tuvo margen de decisión: **37 hermanas de nivel 3 usan `Heading3` y 12 de nivel 2
usan `Heading2`**. Los marcadores de posición del donante se eliminaron (llevan identificador
único) y cada párrafo conservó el suyo. Solo cambió `word/document.xml` (+797 bytes); el resto
del paquete quedó byte a byte.

**Prueba de no-regresión:** extraído el documento reparado y comparado con el anterior, la
**única diferencia de texto en las 26.685 palabras es la renumeración intencional**. Los
encabezados markdown pasaron de 90 a 95 — los cinco restaurados—, que es lo que explica el
+5 en el conteo de palabras.

**Verificación:** `verificar_entregable.py` pasa de 6 problemas duros a **OK — ningún problema
duro** (código de salida 0). El paquete abre correctamente (zip íntegro, XML válido).

### E1-54 y E1-55 · verificación exhaustiva de contenido y formato

Se pasó el documento por una revisión completa —no solo el verificador— y aparecieron **dos
incumplimientos de la regla de la casa** (*"Tablas y figuras: número y título arriba, notas y
fuente debajo, mencionadas en el texto"*). Ambos corregidos:

- **E1-54** — la **Tabla 5** era la única de las 13 sin frase que la anunciara en prosa: la
  introducía solo el título de su subsección. Se agregó, con el formato del párrafo que
  anuncia la Tabla 10: *"La Tabla 5 organiza las brechas identificadas en las subsecciones
  precedentes con su descripción técnica y su implicación específica para el proyecto."*
- **E1-55** — la **Tabla 9** era la única sin Nota ni Fuente. **Es un defecto heredado del
  informe v1.1**, no introducido en esta entrega. Se agregó, clonando el formato de la Nota de
  la Tabla 10 (su vecina en §16): *"Nota. Cada dominio se corresponde con una sección de este
  capítulo; la columna «Contribución al proyecto» indica qué aporta al desarrollo posterior, no
  un resultado alcanzado. Fuente: elaboración propia."*

**Lo que la revisión confirmó como correcto:**

| Dimensión | Resultado |
|---|---|
| Estilos de encabezado | **94 títulos, todos con `Heading<nivel>` exacto** — cero desviaciones |
| Defecto inverso | Ningún párrafo de prosa lleva estilo de encabezado |
| Numeración de secciones | Sin huecos ni desórdenes en ningún nivel |
| Remisiones internas | **Todas resuelven, y apuntan al lugar semánticamente correcto** — incluida la de zero-shot, que se actualizó a §16.3.5 al insertarse la sección nueva |
| Tablas | 13, estructuralmente sanas (columnas uniformes), numeración contigua 2–12 + A.1/A.2 |
| Tablas: nota, fuente y mención | **Las 13 completas** tras E1-54/E1-55 |
| Ecuación (1) | Centrada, introducida en prosa y con sus cuatro términos explicados |
| Referencias | 83 entradas · cero huérfanas · cero citas sin entrada |
| Andamiaje / anacronismo | Cero identificadores internos, cero resultados propios, cero markdown crudo |
| Marcadores | 1 `[[PENDIENTE]]` — el de la AAIP, que **debe viajar** |

**Un hallazgo que NO se corrigió, a propósito.** El rótulo de las notas aparece con cinco
variantes tipográficas (`**Nota.**`, `*Nota.*`, `Nota.`, y una malformada `**Nota***.*`). **No
es un problema de la Etapa 1: es de todo el informe** — §17.3 tiene seis variantes, §17.5 usa
`*Nota.*` y §17.1 usa `Nota.` sin formato. Unificarlo solo en este capítulo lo dejaría
inconsistente con el resto. **Corresponde al pase de integración final**, sobre el documento
maestro completo.

### E1-56 · precisión sobre YOLOE-11 (2026-08-27, revisión final a pedido)

Al revisar cómo quedó nombrado YOLOE-26 (E1-02), apareció una imprecisión factual en la
oración que lo introduce (§15.2.1.2.2): *"La familia fue extendida **posteriormente en
implementaciones de Ultralytics sobre YOLO11 y YOLO26**"*. **Verificado contra el repositorio
oficial del paper (THU-MIG/yoloe): las variantes YOLOE-11-S/M/L son del trabajo original**, no
de una extensión posterior — solo YOLOE-26 lo es. Corregido a: *"…variantes YOLOE-v8 evaluadas
en el trabajo original, que también publica variantes construidas sobre YOLO11 (YOLOE-11) con
resultados equivalentes (Wang et al., 2025). Las variantes sobre YOLO26 (YOLOE-26) son una
extensión posterior de Ultralytics, sin evaluación en el trabajo original; por lo tanto, los
resultados publicados para YOLOE-v8 no deben utilizarse como si fueran una medición de
YOLOE-26 (Ultralytics, 2026)."* Único cambio (diff verificado); `Wang et al., 2025` ya estaba
en el listado. De paso se confirmó que las cifras de la Tabla 3 para YOLOE-v8-S/L (305,8 FPS ·
27,9 AP · 102,5 FPS · 35,9 AP) coinciden con la tabla oficial.

### Lo que queda, y no es redacción

1. **D-E1-11 — decisión del equipo, y así queda.** La aplicabilidad de la inscripción ante la
   AAIP al contexto experimental. **Se deja como pendiente en el documento**, marcada con
   `[[PENDIENTE: …]]`, hasta que el equipo la resuelva y se documente el recaudo en §17.1/§17.4.
2. **Dependencia hacia la Etapa 2** *(anotada, se corrige después — no bloquea)*. §17.1
   (`96b`, línea 589) remite a "la sección **16.7.6**", que tras la renumeración es §16.7.3.
3. **Abrir el `.docx` en Word una vez** y actualizar el índice (F9) para confirmar que las
   seis entradas aparecen donde corresponde. Es una comprobación visual, no un arreglo.

**Lo que NO hay que hacer:** volver a redactar nada · tocar el contenido de §15, §16 o el
Anexo A · reaplicar ningún pase anterior · devolver el documento a ChatGPT.

---

## 4. Fuentes

Entrega verificada: `desarrollando/Etapa 1 — copia ajustada E1 2026-08-27 (2).docx`,
extraída con `herramientas/extraer_informe.py` y contrastada por diff contra la entrega
previa. Verificación mecánica: `herramientas/verificar_entregable.py` (26 tests). Pases
anteriores: `correcciones-etapa-1.md`, `-pase-2.md`, `-pase-3.md`.
