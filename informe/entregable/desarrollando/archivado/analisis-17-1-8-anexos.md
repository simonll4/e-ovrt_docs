# Análisis de §17.1.8 → §17.1.11 y Anexos C/D (v1.14, vista aceptada) — para cerrar la Etapa 2

> ✅ **CERRADO el 2026-09-03 — el pase se aplicó y el usuario aceptó la v1.15.** El acta de
> aplicación es el §8 de este mismo documento. Medición final contra el punto de partida del ciclo
> (**v1.8**, la del pase 6): 23.906 → **15.464 palabras (−35,3 %)**, 109 → **37 títulos** (cero de
> nivel 5), 26 → **22 tablas**, 76 → **4 ecuaciones**, cero bajas de referencias y dos altas
> (Milan et al., 2016; Liang y Han, 2024). Este documento **ya no se edita**. Documento vigente:
> `desarrollando/E-OVRT-VDP_Seccion_17.1_Consolidacion_Metodologica_v1.15.docx`.

> **Qué es.** Diagnóstico previo al pase de reescritura del tramo final de §17.1, con los mismos
> criterios que se aplicaron a §17.1.5, §17.1.6 y §17.1.7: menos repetición de lo ya dicho, sin
> nivel 5, prosa continua de TFG, menos dos puntos y punto y coma, sin sacrificar ideas ni
> pre-registro. Medido sobre la vista aceptada de la v1.14 (todas las sugerencias aceptadas),
> cotejado contra §17.1.1–17.1.7 de la misma versión, contra §15/16 v1.1, contra las actas de los
> pases 3–6 y contra `archivado/analisis-poda-17-1.md` §4.9 (que calificó este tramo como "dejar").
> **No se modifica nada en este documento**: es el insumo para decidir cómo seguir.

## 0. Veredicto en cuatro líneas

1. El tramo es **el más denso del capítulo** (1.390 palabras de prosa para 8 títulos y 9 tablas) y
   casi todo su contenido es defensa pura. No hay grasa argumental que podar; **hay grasa
   estructural y de cierre**.
2. **Estructura:** 8 títulos para 1.390 palabras. §17.1.8 tiene un único hijo (17.1.8.1); cuatro
   subsecciones miden 70–91 palabras (17.1.9.1, 17.1.10.1, 17.1.11.1) o son una tabla con dos
   párrafos. Todo eso puede ser prosa continua bajo el título de nivel 3.
3. **Repetición:** el capítulo enumera sus mismos seis pilares tres veces (17.1.1 §2, 17.1.11.1,
   17.1.11.2 §2); "baseline zero-shot primero" aparece **6 veces** en §17.1, 3 de ellas acá; el
   "sistema asistivo" 5 veces; "condición base → barridos → prueba de mayor exigencia" 3 veces
   (17.1.3.3, Tabla 35, nota C.2); el registro mínimo por corrida dos veces (17.1.7.6 §1 y Tabla D.3).
4. **Puntuación:** 8 dos puntos y 12 punto y coma en la prosa (las dos oraciones-lista de §17.1.11
   concentran 2 y 8). Los `;` dentro de las celdas de la Tabla C.1 son notación de consultas
   separadas, no prosa, y **no se tocan**.

Estimación si se toma todo: prosa **1.390 → ~950 palabras (−30 %)**, títulos **8 → 3** (44 → 39 en
el documento), `:` en prosa 8 → ≤ 2, `;` 12 → ≤ 2, **cero tablas menos, cero ideas menos**.

## 1. Medición

| Sección | prosa (w) | tablas (w) | párr. | oraciones | w/oración | `:` prosa | `;` prosa |
|---|---:|---:|---:|---:|---:|---:|---:|
| 17.1.8.1 Secuencia general del protocolo | 189 | 217 | 3 | 9 | 21,0 | 0 | 2 |
| 17.1.9.1 Criterio metodológico general | 70 | — | 1 | 3 | 23,3 | 0 | 1 |
| 17.1.9.2 Candidatos y condiciones de decisión | 154 | 166 | 3 | 6 | 25,7 | 1 | 3 |
| 17.1.10.1 Política de minimización y uso asistivo | 91 | — | 1 | 3 | 30,3 | 0 | 1 |
| 17.1.10.2 Supuestos de interpretación | 208 | 183 | 3 | 10 | 20,8 | 2 | 1 |
| 17.1.11.1 Cierre del alcance metodológico | 91 | — | 1 | 2 | **45,5** | 1 | **5** |
| 17.1.11.2 Articulación con diseño e implementación | 197 | — | 3 | 6 | 32,8 | 2 | 3 |
| Anexo C (notas) | 277 | 756 | 3 | 17 | 16,3 | 2 | 3 |
| Anexo D (notas) | 113 | 772 | 3 | 12 | 9,4 | 0 | 0 |
| **Total** | **1.390** | **2.094** | 21 | 68 | 20,4 | **8** | **19** |

Metadiscurso casi nulo (2 "en particular"). Ningún párrafo supera las 140 palabras. Referencias
externas: **§17.3, §17.4 y §17.5 no citan ninguna subsección de 17.1.8–17.1.11 ni la Tabla C.2**
(sólo el kit, que se regenera después). Internamente el cuerpo cita "Sección 17.1.10.1" ×3
(17.1.6.2, 17.1.6.5, Tabla 35), "17.1.9" ×3 y "17.1.8" ×1.

## 2. Diagnóstico por sección

### 17.1.8 Protocolo experimental integrado (189 w + Tabla 33)

- **Único hijo.** 17.1.8 → 17.1.8.1 es un título de más. La prosa puede ir directo bajo 17.1.8.
- **§1 (regla de congelamiento previo)** es única y buena. Se conserva.
- **§2 (métricas aplicables definidas antes de la corrida)** repite 17.1.7.1 §3 (estados) y 17.1.7.6
  §4 (aplicabilidad). Basta una oración de remisión ("el conjunto de métricas aplicables se fija
  antes de la corrida con las reglas de 17.1.7.6").
- **Tabla 33** se conserva entera: es el único lugar donde vive la secuencia de fases y §17.5
  reporta contra ella. Dos retoques de celda: "métricas obligatorias" ya está; "tG2A" y
  "talert-system" aparecen sin guion bajo, distinto del "t_G2A"/"t_alert-system" del resto del
  documento (verificar en Word si es subíndice o falta el guion; unificar).
- **Nota**: su primera oración (la baseline como base de discusión) repite casi textualmente a
  17.1.3.4 (ratio 0,74). Se conserva sólo "la secuencia expresa dependencias, no un calendario",
  que es la que protege el no-anacronismo.

### 17.1.9 Estrategia de adaptación al dominio (224 w + Tabla 34)

- **Dos subsecciones para 70 y 154 palabras.** Se funden bajo 17.1.9.
- **Ideas únicas que hay que preservar textualmente:** la adaptación como rama condicionada y no
  como requisito ("convertiría una hipótesis todavía no probada en un supuesto metodológico"); la
  rama como **jornada completa pre-registrada** con una única baseline, márgenes fijados antes y
  veredicto por reglas declaradas; la habilitación "de datos y de protocolo, no de disponibilidad
  de cómputo" (encuadre ADR-017); los dos candidatos y por qué (expresividad vs eficiencia).
- **Repeticiones:** baseline-primero (17.1.9.1 y fila 1 de la Tabla 34, además de 17.1.3.4,
  17.1.7.4 y la nota de la Tabla 33); "se priorizan CR-01 y CR-02" (17.1.6.3 §2); "test set
  compartido y congelado" (Tabla 26). La Tabla 34 es la casa canónica de la regla: se conservan
  sus cinco filas y se sacan los duplicados de la prosa, no al revés.
- **Ambigüedad:** "mejora operativamente significativa y no una ventaja marginal" no dice quién fija
  el margen ni cuándo. La prosa ya lo resuelve ("márgenes fijados antes de evaluar"); la fila debe
  decir lo mismo ("mejora superior al margen fijado antes de evaluar").
- **Tabla 34, columna "Sentido metodológico":** cinco celdas que reformulan la columna anterior.
  Se pueden acortar a la mitad sin perder una idea.

### 17.1.10 Supuestos, riesgos de validez y consideraciones ético-legales (299 w + Tabla 35)

- **17.1.10.1 (91 w).** Primera oración: declara la política. Segunda: licencias y uso académico
  de datasets públicos — **repite 17.1.6.5 §1–2**, que ya es la casa de las licencias. Tercera: las
  salvaguardas para material propio con la cita legal — **ésta es la que importa** y la que
  17.1.6.2, 17.1.6.5 y la Tabla 35 remiten. **D-P6-1 (2026-09-01) decidió conservar acá la única
  cita legal directa de §17.1** como ancla operacional: no se toca la cita.
  Dos ajustes de coherencia con la Etapa 1: (a) §16.6 v1.1 cita la Disposición como
  `(Argentina, 2000, 2015)` y 17.1.10.1 como `(Argentina, 2000; Disposición 10/2015, 2015)` — dos
  formas para la misma obra en el listado global; unificar con la de §16.6; (b) §16.6 habla de
  "finalidad determinada" y 17.1.10.1 de "finalidad explícita"; alinear el vocabulario. El
  "conforme al régimen argentino…" roza la especificación normativa que el criterio del 09-01
  quiso sacar (normativa = marco); "en línea con los principios de la sección 16.6" lo resuelve
  sin perder la cita. Decisión del usuario.
- **17.1.10.2 (208 w).** Los cinco supuestos son "cinco respuestas pre-escritas a objeciones del
  jurado" (`analisis-poda` §6.5) y **se conservan los cinco**, en especial el quinto (filtración de
  preentrenamiento no inspeccionable: es el que blinda las cifras zero-shot). Lo que cambia es la
  forma: "Primero… Segundo… Quinto" con dos puntos es la enumeración típica de IA; se reescribe
  como prosa continua. El "Cuarto" (EBE no es despliegue real) ya está en 17.1.3.3, Tabla 16 y
  17.1.4.2: puede quedar en media oración. La frase-escudo "una alerta no equivale a una sanción…"
  la protegió el pase 6 (§4, p0408): **se conserva**.
- **Tabla 35** se conserva. Fila 4 ("condición base, barridos acotados y prueba de mayor
  exigencia") es la tercera copia de 17.1.3.3; puede remitir. Fila 1 repite la fila "Costo
  operativo" de la Tabla 34 desde el lado del riesgo — aceptable, son lecturas distintas.
- **Estructura:** dos opciones. (A) Conservar 17.1.10.1 como subsección porque tres sitios del
  capítulo la citan por número, y reescribir. (B) Fundir en 17.1.10 con dos párrafos y una tabla, y
  cambiar las tres remisiones a "sección 17.1.10" (ninguna es externa). Recomiendo **B**: es lo
  que pide el criterio de este pase y el costo son tres reemplazos internos.

### 17.1.11 Conclusiones parciales (288 w)

- **Es el espejo de 17.1.1.** 17.1.1 §2 anuncia "comparación primaria en DBE, validación
  complementaria en EBE, reglas de partición sin leakage, política de prompts, jerarquía de
  métricas orientada al valor operativo de alerta y criterios para habilitar fine-tuning";
  17.1.11.1 cierra con **los mismos seis** ("núcleo obligatorio…; separación DBE/EBE…; estrategia
  de datos sin leakage…; framework centrado en valor operativo…; regla de adaptación…;
  proyección…"); y 17.1.11.2 §2 los reparte por tercera vez ("la caracterización del entorno
  restringe…; las condiciones de riesgo determinan…; la estrategia de datos gobierna…; el
  framework define…").
- **Las dos oraciones-lista** (17.1.11.1, 45 palabras con dos puntos y cinco punto y coma;
  17.1.11.2 §2, dos puntos y tres punto y coma) son el patrón que se quiere eliminar.
- **Lo que sí es propio de la conclusión y se conserva:** "deberá declararse qué elementos del
  catálogo fueron implementados, cuáles no aplicaron y cuáles permanecieron condicionados" (es la
  regla que §17.4/§17.5 cumplen) y la trazabilidad definición → diseño → implementación →
  validación como resultado principal. El cierre "sin reemplazar la supervisión humana ni asumir
  decisiones operativas automáticas" repite 17.1.10.2 y la Tabla 16; una vez alcanza.
- **Propuesta:** una sola sección 17.1.11 de dos párrafos (~120 palabras), sin subsecciones, sin
  la lista de seis. Los dos símbolos OMML de 17.1.11.2 pueden quedar o pasar a texto plano como en
  el resto del capítulo (hoy conviven las dos notaciones).

### Anexo C (3 tablas, 277 w de notas)

- **Tabla C.1 se conserva íntegra**: es pre-registro (templates, formulaciones en inglés,
  descompuestas). Los `;` de sus celdas son notación, no prosa. Su nota tiene cinco oraciones:
  la de los templates "a photo of a [CLASS]" ya está explicada en 17.1.5.3; la de "en particular,
  los elementos auxiliares de CR-06…" es análisis, no nota de tabla. Queda en dos oraciones
  (separador `;` como notación; Nivel 3 sin prompts integrados). La línea "Fuente: Elaboración
  propia basada en…" es la **única** "Fuente:" del documento (todas las demás tablas son
  elaboración propia sin decirlo): quitarla o normalizarla al estilo de las demás notas.
- **Tabla C.2 está huérfana**: ninguna sección la cita (regla E2-47: cada tabla de anexo citada
  exactamente una vez). Su lugar natural es 17.1.4.2 (donde se listan "iluminación, oclusiones,
  escala y transporte") o la fila "EBE complementario" de la Tabla 33. Su nota repite la secuencia
  "condición base → barridos → prueba de mayor exigencia" de 17.1.3.3 y de la Tabla 35.
  Contenido de la tabla: candidatos de diseño ex ante (1280×720, 5–10 m…), se conservan.
- **Tabla C.3**: la tabla se conserva (rutas de conversión VOC→COCO→ODVG que el cuerpo no lleva). Su
  nota repite la secuencia de gestión de 17.1.6.5 y remite a 17.1.6.4.2 y 17.1.6.2.1, que ya no
  existen (mecánico pendiente desde el relevamiento). Queda una oración: la clasificación del
  esfuerzo de conversión en un paso o dos, con remisión a 17.1.6.5 y 17.1.6.2.

### Anexo D (3 tablas, 113 w de notas)

- **D.1** alineada con la Tabla 29 en la v1.14. Sin cambios.
- **D.2** se conserva; la fila "Alerta y patrón" tiene celdas de 30–40 palabras que se pueden
  apretar sin perder insumos.
- **D.3 duplica 17.1.7.6 §1**: el cuerpo enumera identificación, modelo, checkpoint, variante,
  resolución, precisión, hardware, software, fuente, cadencia, umbrales, NMS, vocabulario,
  ventanas, identidad temporal, semilla, partición, composición, procedimiento — y la Tabla D.3
  lista lo mismo en tres columnas. Hay que elegir casa. Recomiendo **la tabla** (formato de
  checklist, con la columna "uso en la interpretación" que la prosa no tiene) y reducir 17.1.7.6
  §1 a dos oraciones con la remisión que ya se insertó en E4. Es el único efecto de este pase
  fuera del rango 17.1.8+ (−55 palabras en 17.1.7.6).

## 3. Mapa de repeticiones dentro del capítulo (para decidir la casa de cada idea)

| Idea | Apariciones | Casa propuesta | Sale de |
|---|---|---|---|
| Baseline zero-shot primero / obligatoria | 17.1.3.4 (fila + prosa) · 17.1.7.4 · nota Tabla 33 · 17.1.9.1 · Tabla 34 fila 1 | Tabla 16 (decisión) + Tabla 34 (regla FT) | nota Tabla 33, prosa de 17.1.9 |
| Sistema asistivo / no sustituye al supervisor | 17.1.3.2 · Tabla 16 · 17.1.10.1 · 17.1.10.2 (escudo) · 17.1.11.2 | Tabla 16 + escudo de 17.1.10.2 | 17.1.10.1 (queda "uso asistivo" en el título), 17.1.11.2 |
| EBE = entorno controlado, no despliegue | 17.1.3.3 · Tabla 16 · 17.1.4.2 · 17.1.10.2 "cuarto" | 17.1.4.2 | 17.1.10.2 (media oración) |
| Condición base → barridos → exigencia | 17.1.3.3 · Tabla 35 fila 4 · nota C.2 | 17.1.3.3 | nota C.2; fila 4 remite |
| Salvaguardas para material propio | 17.1.10.1 · 17.1.6.5 (remite) · 17.1.6.2 (remite) · Tabla 35 (remite) | 17.1.10 | — (las remisiones están bien) |
| Licencias y uso académico | 17.1.6.5 · 17.1.10.1 | 17.1.6.5 | 17.1.10.1 |
| Registro mínimo por corrida | 17.1.7.6 §1 · Tabla D.3 | Tabla D.3 | 17.1.7.6 §1 (a dos oraciones) |
| Secuencia de gestión de datos | 17.1.6.5 · nota C.3 | 17.1.6.5 | nota C.3 |
| Los seis pilares / cuatro dimensiones | 17.1.1 §2 · 17.1.11.1 · 17.1.11.2 §2 | 17.1.1 (anuncia) + 17.1.11 (cierra en prosa, sin lista) | 17.1.11.2 §2 |
| Prioridad CR-01/CR-02 para el ajuste | 17.1.6.3 · Tabla 34 fila 2 · Tabla 25 | Tabla 34 (regla) + Tabla 25 (cobertura) | prosa de 17.1.6.3 ya lo dice una vez; sin cambio |

## 4. Coherencia con la Etapa 1 (§15/16 v1.1)

- **D-E1-11**: cero menciones a la AAIP en el tramo ✓. El lado §16 (comentario C9) viaja con la
  Etapa 1.
- **Cita legal**: §16.6 usa `(Argentina, 2000, 2015)`; 17.1.10.1 usa `(Argentina, 2000;
  Disposición 10/2015, 2015)`. Unificar a la forma de §16.6 (una entrada "Argentina (2015)" en
  Referencias, no una entrada "Disposición 10/2015").
- **Vocabulario de principios**: §16.6 "finalidad determinada, minimización, seguridad,
  transparencia, ausencia de identificación biométrica, supervisión humana, trazabilidad";
  17.1.10.1 "finalidad explícita, acceso restringido, retención acotada, ausencia de reconocimiento
  de identidad o tratamiento biométrico". Son principios vs salvaguardas operativas: compatible,
  pero "finalidad determinada" debería ser la misma palabra en ambos.
- **Criterio normativo del 09-01** (normativa = marco, nunca especificación): "conforme al régimen
  argentino" es el único sitio del tramo con voz de cumplimiento. D-P6-1 conservó la cita a
  propósito; el verbo se puede suavizar sin tocarla.
- §16.7.3 (preguntas rectoras) no se cita en este tramo y no hace falta.

## 5. Propuesta de reestructuración (a decidir)

| Bloque | Hoy | Propuesta | Prosa estimada |
|---|---|---|---|
| 17.1.8 | 17.1.8 + 17.1.8.1 (189 w) | **17.1.8** sin hijo: 2 párrafos + Tabla 33 + nota de una oración | ~140 w |
| 17.1.9 | .1 + .2 (224 w) | **17.1.9** sin hijos: 2 párrafos + Tabla 34 (celdas "Sentido" a la mitad) + nota | ~170 w |
| 17.1.10 | .1 + .2 (299 w) | **B:** 17.1.10 sin hijos: salvaguardas (1 párrafo, sin licencias) + supuestos en prosa continua (1–2 párrafos) + Tabla 35; remisiones "17.1.10.1" → "17.1.10" (×3) · **A:** conservar .1 y .2 y sólo reescribir | ~220 w |
| 17.1.11 | .1 + .2 (288 w) | **17.1.11** sin hijos: 2 párrafos, sin la lista de seis, sin la tercera enumeración | ~120 w |
| Anexo C | 3 tablas + notas (277 w) | Tablas intactas; nota C.1 a 2 oraciones sin "Fuente:"; **C.2 citada desde 17.1.4.2**; nota C.3 a 1 oración con remisiones vivas | ~150 w |
| Anexo D | 3 tablas + notas (113 w) | Intacto; D.2 fila "Alerta y patrón" apretada; **17.1.7.6 §1 a 2 oraciones** (efecto fuera de rango) | ~110 w |
| **Total** | 1.390 w · 8 títulos | **~950 w · 3 títulos** (17.1.8, 17.1.9, 17.1.10, 17.1.11 sin subsecciones) | −30 % |

Puntuación esperada en la prosa nueva: 0 dos puntos y 0 punto y coma, como en los pases previos.
Las celdas de tabla conservan su puntuación (los `;` de C.1 son notación).

## 6. Lo que NO se toca (con nombre)

1. **Las cinco filas de la Tabla 33, las cinco reglas de la Tabla 34 y las cinco filas de la
   Tabla 35** (fila 4 sólo remite). Son lo que §17.5 reporta "prescripto vs ejercido".
2. **Los cinco supuestos de 17.1.10.2**, en especial el quinto (filtración de preentrenamiento) y
   la frase-escudo "una alerta no equivale a una sanción" (guardrail del pase 6).
3. **La rama de fine-tuning como jornada única pre-registrada**, "de datos y de protocolo, no de
   cómputo" (ADR-017; T1/T2 NO-GO se reportan contra esto).
4. **La cita legal de 17.1.10.1** (D-P6-1). Se unifica su forma, no su existencia.
5. **Tabla C.1 completa** (templates, inglés, descompuestas = pre-registro no ejercido), **C.2
   y C.3 completas**, **D.1–D.3 completas**.
6. **Cero bajas de referencias**: Liu 2024, Wang 2025, Argentina 2000/2015, Zhou 2022, Du 2022,
   Gu 2021, Radford 2021 siguen todas.

## 7. Decisiones para el usuario antes de escribir

- **D-A** Fundir subsecciones: 17.1.8.1, 17.1.9.1/.2 y 17.1.11.1/.2 (sin costo externo) — sí/no.
- **D-B** 17.1.10: opción B (fundir, tres remisiones internas cambian) u opción A (conservar .1/.2).
- **D-C** Casa del registro mínimo: Tabla D.3 (y 17.1.7.6 §1 se acorta) o la prosa (y D.3 cae).
  Recomiendo la tabla.
- **D-D** Cita legal: unificar a `(Argentina, 2000, 2015)` y "en línea con los principios de la
  sección 16.6" en vez de "conforme al régimen" — sí/no.
- **D-E** Dónde se cita la Tabla C.2: 17.1.4.2 (recomendado) o fila "EBE complementario" de la
  Tabla 33.
- **D-F** Incluir en este mismo pase los mecánicos de §17.1.6 que quedaron "para el final" (fila
  truncada de la Tabla 26, los tres `[[PENDIENTE]]`, nota C.3), porque este pase **es** el final de
  la Etapa 2. Recomiendo sí.
- **D-G** Notación: unificar "t_alert-system"/"t_G2A" en texto plano en todo el capítulo (hoy
  conviven texto plano, "talert-system" y dos OMML inline en 17.1.11.2).

Instrumento previsto: el mismo (edición byte a byte de `document.xml`, cambios controlados sin
aceptar, autor "Claude"), partiendo de la v1.14 aceptada o de la v1.11 con el conjunto completo,
según el estado del archivo en ese momento.

## 8. Acta de aplicación (2026-09-03) — v1.15 (sugerencias sin aceptar), cierra el pase de la Etapa 2

**Decisiones del usuario:** D-A…D-G aprobadas con las opciones recomendadas ("cierran por todos
lados"). Archivo: `E-OVRT-VDP_Seccion_17.1_Consolidacion_Metodologica_v1.15 (sugerencias sin
aceptar).docx`. Instrumento: `herramientas/aplicar_v115_17_1.py`. Parte de la v1.11 con el conjunto
acumulado (la v1.14 no había sido modificada): **rechazar todo devuelve la v1.11 exacta**. La v1.14
queda superada. Autor de las marcas "Claude".

**Regla de oficio que gobernó la reescritura:** en el tramo final **no se insertó ningún párrafo
nuevo y no se borró ningún párrafo que lleve salto de sección**. Cada tabla apaisada cuelga del
párrafo que la precede (`sectPr` vertical) y de su nota (`sectPr` apaisado); esos párrafos se
reescribieron por dentro (runs borrados + run insertado, misma `pPr`). Se borraron como párrafo
completo sólo los siete títulos de nivel 4 y los dos últimos párrafos de 17.1.11.2 (uno con las
dos ecuaciones inline).

| Bloque | Qué se hizo |
|---|---|
| **17.1.8** | Cae 17.1.8.1. §1 reescrito (regla de congelamiento previo, remite a la Tabla 33). §2 a dos oraciones (aplicabilidad por remisión a 17.1.7.6). Nota a "dependencias, no calendario". Tabla 33: "test set congelado" → "banco de evaluación congelado", "tG2A" → "t_G2A", "test compartido" → "banco de evaluación compartido", "primarias" → "obligatorias". |
| **17.1.9** | Caen 17.1.9.1 y 17.1.9.2. Tres párrafos reescritos: rama condicionada (hipótesis → supuesto, habilitación de datos y protocolo, TN/CPN) · candidatos y factibilidad · jornada única prerregistrada + lead a la Tabla 34. Tabla 34: fila 1 "mismo banco de evaluación", fila 2 sin punto y coma y "Sentido" a la mitad, fila 3 "banco de evaluación", fila 4 "superar el margen fijado antes de evaluar". Nota sin punto y coma. |
| **17.1.10** | Caen 17.1.10.1 y 17.1.10.2. Tres párrafos: salvaguardas (sin la oración de licencias, que es de 17.1.6.5; "finalidad determinada" como §16.6; "en línea con los principios de la sección 16.6"; cita `(Argentina, 2000, 2015)`) · supuestos uno a cuatro en prosa continua · quinto supuesto + lead a la Tabla 35. Tabla 35 fila 4 remite a 17.1.3.3; fila 5 "sección 17.1.10". Remisiones de 17.1.6.2 y 17.1.6.5 → "sección 17.1.10". |
| **17.1.11** | Caen 17.1.11.1 y 17.1.11.2. Dos párrafos: cierre en prosa sin lista de seis · articulación con las instancias siguientes, regla "implementado / no aplicó / condicionado", t_G2A y t_alert-system en texto plano. Caen la tercera enumeración de las cuatro dimensiones y la repetición del "asistivo". |
| **Anexo C** | Nota C.1 a dos oraciones sin "Fuente:" (Zhou, Du, Gu y Radford siguen citados en 17.1.5.3). **C.2 citada desde 17.1.4.2.** Nota C.2 remite a 17.1.3.3. Nota C.3 remite a 17.1.6.5 y a la Tabla 23 (las dos referencias muertas desaparecen). |
| **Anexo D** | Fila "Alerta y patrón" de D.2 sin punto y coma ("por episodio"). D.1 y D.3 intactas. **17.1.7.6 §1** pasa de la enumeración de 19 campos a "…reproducirla con los campos mínimos consolidados en la Tabla D.3 del Anexo D" (D-C). |
| **Mecánicos §17.1.6 (D-F)** | Tabla 23: "Roboflow Universe, versión 27" y "versión 1" (`download_log.md`, 2026-06-18; la fecha va a §17.4). Nota 23 sin marcador. Nota 24: marcador → regla de licencia del paquete vs copia/código. SH17 "CC BY-NC-SA 4.0" (`license_registry.md`). Tabla 26 fila "Deduplicación cruzada" completada. Nota 27: marcador → "Milan et al. (2016) para MOT17 y Liang y Han (2024) para OVT-B" (**verificadas en arXiv 1603.00831 y 2410.17534**; las cifras de OVT-B de la tabla coinciden con el abstract). |
| **v1.14 (conservado)** | E1' compromiso · T33 · E2' B/W + puente · E2b' · E3 · E4 (D.1 y D.2) · E5 · E6 · B-2' · B-3 (ahora dentro de la nota 27 reescrita) · T30 "Máximo orientativo". |

**Medición (vista aceptada):** 15.464 palabras · **37 títulos** (44 → 37; nivel 4 en 17.1.8+ = 0) ·
22 tablas · 4 ecuaciones (2 formales + 2 del modelo B/W; caen las 2 inline) · 38 saltos de sección ·
3 comentarios intactos · 893 párrafos con texto (897 + 5 − 9) · **tramo 17.1.8+ y notas de anexos:
1.390 → 1.059 palabras (−24 %), 0 dos puntos y 0 punto y coma** fuera de citas · 59 `w:ins` + 74
`w:del`, ids únicos · 17 partes del zip idénticas byte a byte · **citas 27 → 29, cero bajas**, dos
altas (Milan et al., 2016; Liang y Han, 2024) que **hay que dar de alta en el listado global de
Referencias** en la integración. 22 comprobaciones automáticas en verde.

**Quedan para la integración (no son de este pase):** huecos de numeración de tablas 18/19 y 31/32
(renumerar 33–35 → 31–33 de una sola vez) · "baseline" en celdas de Tablas 16/33/34 vs "línea base"
en la prosa · la única "Fuente: elaboración propia." que sobrevive (nota de la Tabla 21, §17.1.5.2,
sección cerrada) · reconciliar 50–250 ms (doc 39, inventario) con 35–250 ms (§17.1) · 26
comentarios de la v1.8 (A-1) · re-extraer `90f`, kit y nota D-E2-2 del generador **después** de que el
usuario acepte la v1.15 · archivar v1.10–v1.14.
