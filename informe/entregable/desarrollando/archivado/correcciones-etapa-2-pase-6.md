# Correcciones a la Etapa 2 — pase 6: desacople normativo de §17.1

> ✅ **ACTA DE APLICACIÓN (2026-09-01, misma jornada): APLICADO Y VERIFICADO — NO volver a
> aplicarlo.** Los **35 reemplazos** (los 19 ítems E2-68…E2-88, opcionales incluidos, más
> **E2-75c** agregado durante la aplicación: el residuo de "categoría normativa" en p0015 /
> 17.1.2.2 que la compuerta `--post` detectó — la fila "17.1.2.2" del veredicto de GPT era
> correcta, existían AMBOS sitios) se aplicaron sobre el XML de la v1.6 canónica con
> `herramientas/aplicar_pase6.py` (edición byte a byte solo de los `<w:t>` que solapan cada
> ancla; conteos esperados con aborto ante desvío). **Resultado: `…_v1.7.docx`.**
> Verificación: compuerta `herramientas/verificar_anclas_pase6.py` `--pre` verde sobre la
> v1.6 (33/33 anclas) y `--post` verde sobre la v1.7 — greps prohibidos en 0, guardrails
> presentes, invariantes exactos (**76 ecuaciones OMML · 27 comentarios resueltos · 0 marcas
> · 1 sola cita a Disposición 10/2015, en 17.1.10.1 · marcador AAIP intacto · tablas 16–35**).
> Diff íntegro v1.6→v1.7 atribuido: **22 hunks = exactamente las líneas de los 35
> reemplazos, cero daño colateral**; −192 palabras (26.632 → **26.440**, mismo instrumento).
> `90f` re-extraído de la v1.7; la v1.6 quedó en `archivado/`.

- **Fecha:** 2026-09-01 · **Sobre:** `desarrollando/E-OVRT-VDP_Seccion_17.1_Consolidacion_Metodologica_v1.6.docx`
  (canónica: 0 cambios controlados, 27 comentarios resueltos, 76 ecuaciones OMML, tablas 16–35).
  El resultado de aplicar este pase es la **v1.7**.
- **Origen:** el criterio editorial firmado el 2026-09-01 para las nuevas §16.2/§16.6 de la
  Etapa 1 v1.1 (normativa = marco conceptual, nunca especificación; prohibido derivar
  taxonomías, severidades o ventanas de artículos legales) y su cláusula de consecuencia:
  *"cualquier sección posterior —especialmente §17.1— que todavía hable de una taxonomía
  normativa, de condiciones derivadas directamente de artículos legales, de cobertura
  normativa, o que utilice artículos del Decreto 911/96 para asignar severidades o ventanas
  temporales, debe revisarse"*.
- **Insumo:** doble auditoría independiente (Claude + GPT) sobre la v1.6; la tabla de GPT
  (17 filas) fue verificada sitio por sitio contra el texto real — ninguna fila fabricada.
  Este documento consolida ambas en un único mapa de reemplazos con anclas exactas.
- **IDs:** continúan la serie — comentarios **E2-68…E2-88**, decisiones **D-P6-1…D-P6-3**.
- **Qué NO hace este pase:** no reabre ninguna decisión de la v1.6 (PODA-C/MOT intacta), no
  toca cifras, ecuaciones, pre-registro, catálogos CR/PR ni la estructura de tablas 16–35.
  Es un desacople de fundamentación: lo normativo deja de fundar lo metodológico.

---

## 0. Decisiones

**D-P6-1 — Citas legales directas dentro de §17.1: una sola, en 17.1.10.1.** La cita
`(Argentina, 2000; Disposición 10/2015, 2015)` de la política de minimización (p0405) se
conserva como ancla operacional del régimen; **todos los demás sitios** de §17.1 que hoy
citan Ley 25.326 / Disposición 10/2015 (Tabla 18, Tabla 19 y su nota) pasan a remitir a la
sección 16.6 o a la Sección 17.1.10.1. *(Adoptada el 2026-09-01 con la recomendación de
Claude; reversible a "full-remisión" antes de aplicar — en ese caso E2-87 también
reemplaza la cita de p0405 por una remisión a §16.6.)*

**D-P6-2 — La severidad es una categoría metodológica de prioridad temporal.** Ningún
nivel de severidad ni ventana de persistencia se fundamenta en artículos legales. La
lógica pasa de `severidad → legislación → artículos → obligación → ventana` a
`severidad metodológica → perfil temporal de la condición → prioridad de respuesta →
ventana de evidencia`. La relevancia preventiva de las condiciones vive en §16.2 y se
remite, no se reconstruye. *(Deriva directa del criterio firmado; se registra para
trazabilidad.)*

**D-P6-3 — Resolución SRT 299/2011: baja del informe.** Su única aparición está en
17.1.5.3.2 (E2-79). Tras el pase desaparece de §17.1 y no queda citada en ninguna otra
sección (verificado en §15/16 v1.1, §17.3 v1.4, §17.4 v1.6, §17.5 v1.3) → **se da de baja
del listado global de referencias** en la integración. Ley 19.587, Decreto 911/96,
Ley 25.326 y Disposición 10/2015 permanecen en el listado: las dos primeras quedan
sostenidas por §16.2, las dos últimas por §16.6 y por p0405 (D-P6-1).

---

## 1. Advertencias al aplicador (leer antes de tocar el XML)

1. **Aplicar sobre el archivo canónico** de `desarrollando/` (0 marcas). Si se trabajó
   sobre una copia con cambios controlados, descartarla: las anclas de este documento
   están verificadas contra la canónica.
2. **Ecuaciones OMML inline:** §17.1 tiene 76 `m:oMath`, varias **inline dentro de
   párrafos y celdas** (p. ej. `t_alert-system` como ecuación). En una extracción de texto
   plano aparecen como huecos (": , Tiempo…", "ni  sobre imágenes"). **No son defectos**:
   no "repararlos", no tocar ningún run adyacente a un `m:oMath`. Invariante: 76 antes,
   76 después.
3. **Rangos de comentario:** E2-73 edita texto **dentro del rango del comentario C12**
   (resuelto). Editar los runs interiores preservando `commentRangeStart/End` id=12 y la
   `commentReference`. Invariante: 27 comentarios antes y después, todos resueltos.
4. **El marcador `[[PENDIENTE: …inscripción…]]` (p0406) no se toca** — ni el texto ni su
   posición. E2-87 edita únicamente la oración final del párrafo anterior.
5. Nunca abrir/guardar con LibreOffice (rompe las ecuaciones). Edición por XML o Word.

---

## 2. Mapa de reemplazos — obligatorios

Las anclas son texto vigente verbatim de la v1.6 (**verificadas 32/32 el 2026-09-01 con
`verify_anchors_p6.py`, cada una con ocurrencia única en el texto extraído**). `→`
introduce el texto nuevo.

### E2-68 · 17.1.2.1 (p0011) — CR-01/02 "derivadas del marco" con cita legal

- **Ancla:** `derivadas del marco de seguridad laboral y construcción (Decreto N.º 911/1996, 1996; Ley N.º 19.587, 1972).`
- → `cuya relevancia preventiva, observabilidad y evaluabilidad están fundamentadas en la sección 16.2.`

### E2-69 · Tabla 18, fila Participantes — "infracción deliberada"

- **Ancla:** `configuración de escenas con y sin infracción deliberada.`
- → `configuración de escenas con y sin las condiciones observables objetivo.`
- *Motivo: una imagen no demuestra una infracción (§16.2.3); el rodaje simula condiciones
  observables, no ilícitos.*

### E2-70 · Tabla 18, fila Limitación principal — recaudo con desarrollo jurídico

- **Ancla:** `requiere gestión de consentimiento libre, expreso e informado e información previa a los participantes, conforme al régimen de protección de datos personales y videovigilancia aplicable (Argentina, 2000; Disposición 10/2015, 2015).`
- → `requiere gestión de consentimiento informado e información previa a los participantes, conforme a las salvaguardas de la Sección 17.1.10.1.`
- *El consentimiento queda como recaudo experimental adoptado, no como conclusión
  jurídica (D-P6-1).*

### E2-71 · Tabla 19, fila "Recaudos ético-legales en el Escenario B"

- **Ancla (celda origen):** `Ley N.º 25.326 y Disposición 10/2015`
- → `Criterios ético-legales de la sección 16.6`
- **Ancla (celda implicación):** `Las pruebas con personas en el campo visual requieren consentimiento informado e información previa. El carácter académico y controlado del prototipo atenúa el perfil de riesgo, pero no elimina las obligaciones de resguardo y minimización.`
- → `Las pruebas con personas en el campo visual requieren consentimiento informado e información previa, finalidad explícita, minimización, acceso restringido y retención acotada, conforme a la Sección 17.1.10.1.`
- *La frase "atenúa el perfil de riesgo" contradice la nueva §16.6, donde la finalidad no
  elimina exigencias. Se elimina entera.*

### E2-72 · Nota de la Tabla 19 (p0073)

- **Ancla:** `y el marco normativo argentino aplicable a protección de datos personales y videovigilancia.`
- → `y los criterios ético-legales establecidos en la sección 16.6 y operacionalizados en la Sección 17.1.10.1.`

### E2-73 · 17.1.5.1 (p0076) — "identificación normativa" ⚠ dentro del rango C12

- **Ancla:** `la brecha entre la identificación normativa de condiciones de riesgo y su traducción en consultas textuales`
- → `la brecha entre la identificación de condiciones de riesgo preventivamente relevantes y su traducción en consultas textuales`

### E2-74 · 17.1.5.2.1 (p0081) — reconstruye el catálogo normativo eliminado de §16.2

- **Ancla (oración completa):** `El universo de condiciones de riesgo identificado en el análisis normativo de la fundamentación teórica abarca categorías como uso de EPP (casco, chaleco, calzado), protección contra caídas en altura, delimitación de áreas de riesgo, control de circulación con maquinaria, orden y limpieza e instalaciones eléctricas provisorias.`
- → `La fundamentación teórica delimita las condiciones de riesgo observables por su relevancia preventiva, su evidencia visual anotable y su formulación evaluable (sección 16.2), y señala como posibles extensiones situaciones como el trabajo en altura, las zonas restringidas o la interacción con maquinaria.`
- *Doble efecto: elimina la enumeración del catálogo que ya no existe y repara la
  referencia colgante "análisis normativo de la fundamentación teórica". El resto del
  párrafo ("El prototipo experimental no pretende cubrir la totalidad de ese espacio…")
  se conserva, reemplazando "la totalidad de ese espacio" por "ese espacio de manera
  exhaustiva" si se prefiere fluidez; opcional.*

### E2-75 · 17.1.2.2 + 17.1.5.2.3 (p0092) + Tabla 20 — "categoría normativa" / "Cat. normativa"

- **Ancla (prosa, p0092):** `la categoría normativa de origen` → `el tipo de condición`
- **Ancla (encabezado de tabla):** `Cat. normativa` → `Tipo de condición`
- **Ancla (prosa, p0015 / 17.1.2.2):** `con su categoría normativa, componente evaluador` → `con su tipo de condición, componente evaluador`
  *(✎ agregada durante la aplicación: la compuerta `--post` detectó el residuo; la fila
  "17.1.2.2" del veredicto de GPT era correcta — existen AMBOS sitios, p0015 y p0092.)*
- *Los valores de las celdas (EPP — casco, Protección contra caídas, etc.) ya son
  familias preventivas descriptivas, no citas legales: **no se tocan**.*

### E2-76 · 17.1.5.3.2 (p0109–p0110) — cabecera de severidad

- **Ancla (p0109):** `que refleja el perfil temporal del riesgo, entendido como` → `que refleja el perfil temporal de la condición, entendido como`
- **Ancla (p0110, oración completa):** `La fundamentación de cada nivel se apoya en la normativa argentina aplicable y en el perfil temporal de consecuencias asociado a cada tipo de exposición.`
- → `Cada nivel se define como una categoría metodológica de prioridad temporal, fundamentada en el perfil temporal de consecuencias asociado a cada tipo de exposición; la relevancia preventiva de las condiciones subyacentes está establecida en la sección 16.2. La severidad ordena prioridades temporales del protocolo y no constituye una calificación normativa de la situación observada.`

### E2-77 · 17.1.5.3.2 (p0111) — nivel crítico fundado en arts. 52–57 y 246–249

- **Ancla (oración completa):** `El Decreto 911/96 establece las medidas de prevención frente al riesgo de caída de personas y los trabajos con riesgo de caída a distinto nivel (arts. 52 a 57), y regula la operación de vehículos y maquinaria automotriz junto con la protección frente a la circulación vehicular —señalización, vallado, equipos de alta visibilidad, vigías— (arts. 246 a 249). En ambos casos, la exposición observada`
- → `Es el caso de la exposición en altura sin protección visible y de la interacción próxima entre peatones y maquinaria en operación: en ambos, la exposición observada`
- *El resto de la oración ("puede transformarse con rapidez en un incidente severo, lo que
  justifica…") se conserva tal cual.*

### E2-78 · 17.1.5.3.2 (p0112) — nivel alto fundado en arts. 98–106 y 107

- **Ancla (oración completa):** `El Decreto 911/96 regula la provisión, uso, condiciones y vida útil de los equipos de protección personal y la vestimenta de trabajo (arts. 98 a 106), y la provisión de casco de seguridad para tareas con riesgos específicos (art. 107). La ausencia de casco`
- → `La ausencia de casco`
- *La justificación por eliminación de barrera preventiva ("no produce por sí misma el
  incidente, pero elimina una barrera de protección…") ya está en el párrafo y es
  autosuficiente.*

### E2-79 · 17.1.5.3.2 (p0113) — nivel medio fundado en arts. 63/70 y SRT 299/2011

- **Ancla (oración completa):** `La obligación de emplear elementos reflectivos o de alta visibilidad se vincula con los trabajos nocturnos y con la construcción de carreteras en uso (Decreto 911/96, arts. 63 y 70), y puede complementarse con la Resolución SRT 299/2011 sobre registración y constancia de entrega de ropa de trabajo y EPP. La ausencia de chaleco`
- → `La ausencia de chaleco`
- *Ejecuta D-P6-3 (única aparición de SRT 299/2011 en el informe).*

### E2-80 · Tabla 21 (p0131 + encabezado + 6 filas) — citas de artículos por fila

- **Ancla (p0131):** `el perfil temporal del riesgo que fundamenta la asignación de severidad` → `el perfil temporal de la condición que fundamenta la asignación de severidad`
- **Ancla (encabezado):** `Perfil temporal del riesgo` → `Perfil temporal de la condición`
- **Eliminar de las celdas, verbatim (la prosa de perfil de riesgo se conserva):**
  - PR-01: ` (Decreto 911/96, arts. 50, 98–102 y 107)`
  - PR-02: ` (Decreto 911/96, arts. 47, 63 y 70)`
  - PR-03: ` (Decreto 911/96, arts. 52, 54–56 y 112)`
  - PR-04: ` (Decreto 911/96, arts. 52 y 54–56)`
  - PR-05: ` (Decreto 911/96, arts. 47, 61, 70, 71 y 246–249; Ley 19.587, arts. 8 y 9)`
  - PR-06: ` (Decreto 911/96, arts. 66–69, 95(a), 139, 140(e)–(f), 156 y 176)`

### E2-81 · Nota de la Tabla 21 (p0134) — la nota declara que los artículos fundamentan la severidad

- **Ancla (tramo completo):** `Los artículos normativos referenciados en la columna “Perfil temporal del riesgo” fundamentan la severidad asignada a cada patrón a partir del tipo de exposición, la barrera preventiva omitida y la potencialidad de daño; no definen por sí mismos los umbrales computacionales de activación, distancia, persistencia o latencia del sistema. Fuente: Elaboración propia basada en el análisis normativo del Decreto 911/96 y la Ley 19.587.`
- → `La severidad es una clasificación interna del protocolo, fundamentada en el perfil temporal de la condición; no constituye una calificación normativa de la situación observada ni define por sí misma los umbrales computacionales de activación, distancia, persistencia o latencia del sistema. La relevancia preventiva de las condiciones se fundamenta en la sección 16.2. Fuente: elaboración propia.`

### E2-82 · 17.1.6.1.2 (p0200) — referencia colgante a la "taxonomía normativa"

- **Ancla:** `aunque presentes en la taxonomía normativa de la fundamentación teórica, no integran`
- → `aunque preventivamente relevantes, no integran`
- *La taxonomía referida se eliminó de §16.2 en la v1.1; además, calzado/guantes/gafas no
  figuran ni siquiera como extensiones en la nueva §16.2 — no se puede afirmar presencia.*

### E2-83 · 17.1.6.1.3 (p0202) + Tabla 22 — criterio C2 "Cobertura normativa"

- **Ancla (p0202):** `y la cobertura normativa (C2)` → `y la cobertura del catálogo experimental (C2)`
- **Ancla (fila C2, celda nombre):** `Cobertura normativa` → `Cobertura del catálogo experimental`
- **Ancla (fila C2, celda definición):** `Proporción de categorías anotadas que se corresponden con alguna condición de riesgo de la taxonomía operacionalizada en la taxonomía de condiciones de riesgo, patrones y prompts, derivada del marco normativo argentino.`
- → `Proporción de categorías anotadas que se corresponden con alguna condición de riesgo del catálogo experimental (CR-01 a CR-06) definido en la Sección 17.1.5.2.`
- *De paso repara la redacción circular "taxonomía operacionalizada en la taxonomía". El
  identificador C2 se conserva: los puntajes de los datasets no se recalculan.*

### E2-87 · 17.1.10.1 (p0405) — oración previa al marcador AAIP

- **Ancla:** `Ese régimen prevé, además, la inscripción de las bases de datos con datos personales ante la autoridad de aplicación (AAIP); su aplicabilidad al material experimental del proyecto y el recaudo adoptado se documentan a continuación.`
- → `Ese régimen contempla, además, requisitos administrativos asociados a las bases de datos con datos personales ante la autoridad de aplicación (AAIP), cuya aplicabilidad al contexto experimental debe determinarse; la decisión y el recaudo adoptado se documentan a continuación.`
- *Alinea el estatuto con la nueva §16.6 ("no corresponde asumirla ni descartarla"). La
  cita legal del mismo párrafo se conserva (D-P6-1). El marcador p0406 queda intacto.*

---

## 3. Mapa de reemplazos — opcionales (consolidación, aplicar si el pase ya está abierto)

### E2-84 · 17.1.6.2.6 (p0225)

- **Ancla:** `producción de material controlado en el EBE bajo consentimiento y minimización.`
- → `producción de material controlado en el EBE bajo las salvaguardas de la Sección 17.1.10.1.`

### E2-85 · 17.1.6.4.1 (p0250)

- **Ancla:** `rigen las salvaguardas de minimización, consentimiento y ausencia de tratamiento biométrico de la Sección 17.1.10.1.`
- → `rigen las salvaguardas de la Sección 17.1.10.1.`

### E2-86 · 17.1.7.7.5 (p0347) — redacción circular *(recomendado)*

- **Ancla:** `La taxonomía de severidad definida en la taxonomía de condiciones de riesgo, patrones y prompts exige`
- → `La clasificación de severidad definida en la Sección 17.1.5.3.2 exige`

### E2-88 · Tabla 35, fila de privacidad

- **Ancla (celda mitigación):** `Aplicar minimización, acceso restringido y registro explícito de finalidad y condiciones de captura.`
- → `Aplicar las salvaguardas de la Sección 17.1.10.1, con registro explícito de finalidad y condiciones de captura.`

---

## 4. Qué se conserva a propósito (guardrails — no caen por arrastre)

- **CR-01…CR-06 y PR-01…PR-06 completos**, con sus severidades, ventanas y criterios de
  activación: cambia la fundamentación, no el esquema metodológico.
- **Ventanas de persistencia (p0118):** ya están fundadas en el análisis cualitativo de
  velocidad de escalada — no se tocan.
- **Valores de la columna renombrada de la Tabla 20** (EPP — casco, etc.): descriptivos.
- **Licencias de datasets (p0251–p0252) y de software/modelos:** reproducibilidad, no
  ornamento normativo.
- **p0249:** la remisión genérica al "principio de minimización desarrollado en el marco
  ético-legal de la fundamentación teórica" es exactamente el patrón correcto.
- **p0405:** la única cita legal directa de §17.1 (D-P6-1) y toda la política de
  minimización y uso asistivo.
- **p0406:** el marcador `[[PENDIENTE]]` de la inscripción AAIP — decisión abierta del
  equipo, espejo en §17.4.
- **p0408 (17.1.10.2):** *"una alerta no equivale a una sanción ni a una determinación
  automática de incumplimiento normativo"* — frase-escudo, alineada con las nuevas
  §16.2/§16.6. Ídem §17.3 ("la incertidumbre no fabrica una infracción") y §17.4 ("no
  determina incumplimientos normativos"), que este pase no toca.

---

## 5. Verificación post-aplicación (extraer texto de la v1.7 y correr en cero)

**Compuerta automatizada** (cubre anclas, greps prohibidos, guardrails e invariantes;
sale 0 sólo si todo pasa):

```bash
python3 docs/herramientas/verificar_anclas_pase6.py --pre  <v1.6.docx>   # antes: 32/32 anclas ✅ (verificado 2026-09-01)
python3 docs/herramientas/verificar_anclas_pase6.py --post <v1.7.docx>   # después: todo en cero + invariantes
```

Greps que deben dar **0** sobre el texto extraído de §17.1:

```
911/96 · 19.587 · SRT 299 · "arts." · "art. " (citas a nivel de artículo)
normativa argentina aplicable · taxonomía normativa · análisis normativo
[Cc]obertura normativa · Cat. normativa · categoría normativa · infracción deliberada
atenúa el perfil · identificación normativa · Perfil temporal del riesgo
```

Invariantes que deben conservarse exactos:

| Invariante | Valor v1.6 | Valor esperado v1.7 |
|---|---|---|
| Ecuaciones `m:oMath` | 76 | 76 |
| Comentarios (todos resueltos) | 27 | 27 |
| `Disposición 10/2015` | 3 | **1** (solo p0405) |
| `Argentina, 2000` | (en p0405) | 1 (solo p0405) |
| `[[PENDIENTE` | 1 | 1 (intacto, p0406) |
| Tablas numeradas | 16–35 (20) | 16–35 (20) |
| `incumplimiento normativo` (escudo p0408) | 1 | 1 |
| Cambios controlados | 0 | 0 |

Además: diff íntegro atribuible a E2-68…E2-88; ningún run adyacente a `m:oMath`
modificado; rango del comentario C12 conservado.

---

## 6. Consecuencias fuera de §17.1 (bookkeeping, no son parte del pase)

- **Listado global de referencias (90e / §19):** baja de Resolución SRT 299/2011
  (D-P6-3). Las bajas de la Etapa 1 v1.1 (Decreto 351/79, Res. SRT 51/97 y 35/98,
  ISO 45001/ISO 2018, Decreto 1558/2001) corren por cuenta de esa etapa, no de este pase.
- **Kit del proyecto:** regenerar tras aplicar (el texto base 90f quedará desactualizado
  en las zonas E2-76…E2-81).
- **§17.4:** el espejo del marcador AAIP se resuelve cuando el equipo firme D-E1-11; este
  pase no lo toca.
