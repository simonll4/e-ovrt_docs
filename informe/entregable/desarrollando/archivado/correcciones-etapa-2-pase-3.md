# Correcciones de la Etapa 2 — §17.1 (pase 3: desduplicación, anexos y defectos — 2026-08-31)

> ✅ **APLICADO Y VERIFICADO — 2026-08-31 (misma jornada): la entrega de ChatGPT es la v1.4**
> (`desarrollando/E-OVRT-VDP_Seccion_17.1_Consolidacion_Metodologica_v1.4.docx`). Resultado de la
> verificación completa de §G:
> - **Targets, todos dentro**: 28.730 palabras (documento entero; desarrollo ~26,4k) · **109
>   títulos numerados exacto** · **21 tablas 16–36 contiguas** · anexos C (3 tablas) y D (3)
>   anexados al final con encabezados sin número en `Heading2` (el estilo exacto del título 17.1)
>   · **78 ecuaciones exacto** (las 7 muertes declaradas) · 1 `[[PENDIENTE]]` (AAIP) ·
>   **los 17 greps en cero** · `todavía` = 7 intacto · verificador OK sin problemas duros.
> - **Diff párrafo a párrafo contra `90f` v1.3**: 27 eliminados + 66 modificados + 1 nuevo — cada
>   bloque atribuido a su unidad, **cero cambios fuera del pase**. Fidelidad de anexos contra
>   `90g`: fila "Alerta" única, "por cuadro" en Tracking, C.3 con las 4 retenidas, sin descartados.
> - La entrega **trajo cambios controlados** (521 ins / 343 del, sin aceptar — se aceptan en
>   Word/Docs) y **conservó los 27 comentarios** (se resuelven con el mapa §F).
> - **Un (1) defecto: E2-50 sitio 12 no aplicado** — reparado de forma determinista sobre el XML
>   (reemplazo de run único validado con `ET.fromstring`; respaldo en
>   `archivado/…v1.4 (entrega GPT, antes de E2-50.12).docx`).
> - **Dos notas de auditoría**: (a) el sitio 3 de E2-50 quedó absorbido por E2-38, que eliminaba
>   el párrafo entero que aquel reescribía — solapamiento de autoría del pase, resultado correcto;
>   (b) **la guarda "deberá nunca <30" estaba mal calibrada**: no contaba los `deberá` dentro de
>   párrafos que E2-36/E2-37 eliminaban legítimamente (2+1). El valor final correcto es **28 en el
>   desarrollo** (30 en el documento con los 2 de las notas del Anexo D) y las 12 desapariciones
>   fueron auditadas una por una: **ninguna prescripción normativa tocada**.
> - `90f` re-extraído de la v1.4 (la extracción corta en los anexos por ser encabezados sin
>   número: contiene solo el desarrollo — los anexos viven en el `.docx` y en `90g`).
> ✅ **CIERRE (misma jornada, a pedido del usuario): cambios ACEPTADOS y 27 comentarios RESUELTOS
> sobre el XML.** El `.docx` v1.4 quedó limpio: **0 marcas de revisión** (521 `w:ins` desenvueltas,
> 343 `w:del` eliminadas, 11 filas y 2 tablas borradas retiradas, 95 párrafos vacíos desaparecidos,
> 21 `*Change` quitados) · **78 ecuaciones intactas** · 27 tablas (21 numeradas 16–36 + 6 de anexo)
> · **109 títulos** · los 27 comentarios **conservados y marcados `done`** (con sus anclas: 27
> `commentRangeStart` + 27 `commentReference`) · todas las partes XML validadas · verificador OK.
> Respaldo previo: `archivado/…v1.4 (con cambios controlados y comentarios sin resolver).docx`.
>
> ⚠ **DEFECTO ENCONTRADO AL ACEPTAR (y corregido): E2-31 se aplicó DOS VECES.** GPT reescribió el
> párrafo de §17.1.2.2 (borró el original e insertó la versión correcta con la frase al final y
> "Tabla 21"), pero **dejó una inserción huérfana con la numeración vieja** —" …se presenta en la
> **Tabla 23** (Sección 17.1.5.2.3)"— dentro del párrafo borrado y con la marca de párrafo borrada,
> de modo que al aceptar se habría fusionado hacia adelante y el informe habría quedado con **la
> frase duplicada y una remisión a la tabla equivocada**. Se rechazó esa única inserción antes de
> aceptar. Verificado: la frase aparece **una sola vez**, al final del párrafo, con "Tabla 21";
> `"Tabla 23 (Sección"` = 0.
> **Lección para el próximo pase:** cuando una unidad **agrega texto** y otra **renumera**, verificar
> también que **no sobreviva una copia con el número viejo** — el chequeo `count==1` de la variante
> nueva no lo detecta, y el filtro de atribución del diff tampoco si la oración figura entre las
> "conocidas". Este era el **único** párrafo del documento con el patrón "marca de párrafo borrada +
> texto vivo": ese chequeo (1 caso en 95) es el que lo destapó y conviene repetirlo siempre.
>
> **Queda para el usuario**: git (nada más — cambios y comentarios ya cerrados). **Queda para la
> integración**: mudar anexos a §19.3/§19.4 · hueco global de tablas 37–38 · unificación de nombres
> de métrica del anexo con objetos de ecuación.
>
> ~~**Estado: NO aplicado — es el trabajo a entregar a ChatGPT.**~~ Texto base:
> `90f-etapa2-texto-extraido.md` (extracción 2026-08-31 del documento de trabajo
> `desarrollando/E-OVRT-VDP_Seccion_17.1_Consolidacion_Metodologica_v1.3- a revisar.docx`, que es
> la **v1.3 + las 2 ediciones del 2026-08-30**: §17.1.4.2.4 "fuente RTSP sintética" eliminada con
> renumeración, y el quinto supuesto agregado a §17.1.10.2). Cifras de partida verificadas:
> **28.564 palabras · 117 títulos numerados · 23 tablas (16–38) · 85 ecuaciones OMML · verificador
> OK, sin problemas duros · 1 marcador `[[PENDIENTE]]` (AAIP)**. La salida esperada es la **v1.4**.
>
> **Origen del pase:** la revisión crítica del usuario (27 comentarios en el `.docx`, mapeados en
> §F) más la auditoría del 2026-08-31, que verificó cada propuesta contra los extractos de
> §16/§17.3/§17.4/§17.5, el XML del `.docx` y los Anexos B/C/D reales. Tres hechos verificados
> habilitan este pase:
> 1. **§17.3, §17.4 y §17.5 no citan ninguna tabla de §17.1 por número** (cero apariciones;
>    referencian "la consolidación metodológica" por nombre). La única remisión numérica externa
>    hacia §17.1 en todo el informe es `17.1.4.4` (una vez, y este pase no la renumera).
>    → renumerar tablas y títulos dentro de §17.1 sólo obliga a actualizar referencias internas.
> 2. **El Anexo C contradice al desarrollo v1.3** (su Tabla C.3 cuenta 7 fuentes para CR-01
>    incluyendo descartadas y su nota cita una tabla que hoy es otra) y **el Anexo D duplica** las
>    Tablas 34/35 y la prosa de §17.1.7.4/§17.1.7.8 → se resuelve en `90g` (D-E2-1, ahora ejecutada).
> 3. Los defectos de gramática y la cifra 50–250 ms de la Tabla 21 están **en el XML del `.docx`**,
>    no son artefactos de extracción.
>
> **Reglas que siguen rigiendo, sin cambios:** no-anacronismo (mapa regla 5) — nada se corrige
> "contra lo implementado"; lo prescripto y no ejercido no se borra, lo reporta §17.5.
> Autocontención — ningún código `E2-`/`D-P3-`/`AJ-`/ruta aparece en el texto del informe.
> Las ecuaciones de Word (`⟦ECUACIÓN⟧` en la extracción) **no son erratas** (mapa `00` §7).
>
> **⚠ ENMIENDA AL GUARDRAIL 2 (`ajustes/07` §9), firmada por el usuario (D-P3-1):** el guardrail
> "§17.1.5 y §17.1.7 no se comprimen; no existe segunda vuelta" queda enmendado para este pase:
> **se consolidan explicaciones repetidas de lo mismo; ninguna definición, umbral, regla ni
> contenido de tabla cambia**. La enmienda la disparó la propia revisión del usuario (sus
> comentarios piden comprimir §17.1.5.1 y §17.1.5.3.3). Fuera de las unidades listadas acá, los
> dos apartados siguen intocables.

---

## A. Decisiones que gobiernan el pase

⚠ *Serie de IDs: estas D-P3-x son de la **etapa 2** (este pase). No confundir con las D-P3-1…6 del
pase 3 de §17.3/§17.4/§17.5 (`archivado/correcciones-etapa-3-4-5-pase-3.md`) — al citar, nombrar
el pase.*

| ID | Decisión | Firma |
|---|---|---|
| **D-P3-1** | **Enmienda del guardrail 2**: en §17.1.5 y §17.1.7 se consolidan repeticiones (unidades E2-33/34/35/37/38/39/40); prohibido tocar definiciones, umbrales, reglas o contenido de tablas. | usuario · 2026-08-31 |
| **D-P3-2** | **Las Tablas 17 y 22 se eliminan** (contenido 100 % duplicado) y las tablas de §17.1 se **renumeran contiguas 16–36** (E2-48). Verificado: cero referencias numéricas aguas abajo. La renumeración **global** del informe (el hueco 37–38 antes de las tablas 39–55 de §17.3) queda como handoff al pase de integración (§H). | usuario · 2026-08-31 |
| **D-P3-3** | El comentario del usuario sobre fine-tuning en EBE se resuelve **condicionando, no restringiendo** (E2-46): la promesa pre-registrada no se reescribe para que encaje con el resultado (misma doctrina que preservó el rango 500–2.000 de la Tabla 28); la no-ejecución la declara §17.5. | usuario · 2026-08-31 |
| D-P3-4 | **La Tabla C.1 se queda en el Anexo C** (ancla del prompt set, AJ-2.07); no sube al desarrollo — subirla insertaría una tabla y renumeraría sin necesidad. | recomendación adoptada |
| D-P3-5 | **Composición final de los anexos** (ejecuta y refina D-E2-1): Anexo C 5→3 tablas · Anexo D 6→3 tablas · Anexo B intacto. El contenido vive en `90g-etapa2-anexos-c-y-d.md`; las remisiones del cuerpo las actualiza E2-47. El refinamiento sobre D-E2-1: la ex-D.4 se **elimina** (no se "reduce a lo que agrega") porque lo que agrega ya está en la Tabla 24 y en la prosa de §17.1.7.7.6. | recomendación adoptada |
| D-P3-6 | La estimación orientativa de latencia (§17.1.7.7.5) **se mantiene como está** (protocolo ex-ante correcto); sólo se parte el párrafo (E2-45) y se corrige la cifra huérfana de la Tabla 21 (E2-43) por **coherencia interna** — nunca contra lo medido. | recomendación adoptada |
| D-P3-7 | El catálogo CR-01…CR-06 **no se poda**: núcleo/extensión es el aporte metodológico de la tesis. Sólo cae el detalle de materialización que invade la casa de §17.3 (E2-39). | recomendación adoptada |
| **D-P3-8** | **Los Anexos C y D viajan AL FINAL del documento de la etapa** (E2-49): ChatGPT los anexa en su composición final (contenido completo en `90g`), y al integrar al maestro el equipo los muda a §19.3/§19.4. Supersede la mitad "quedan fuera del `.docx`" de D-E2-1; la constancia de corrección sigue siendo `90g`. | usuario · 2026-08-31 |
| **D-P3-9** | **Voz del documento (E2-50):** lo que remite a una sección que **existe** deja de enmarcarse como obligación futura y pasa a presente ("…deberá materializar" → "…materializa"). **Sólo eso**: la prescripción normativa del protocolo ("toda corrida deberá declarar…") NO se toca, y lo pre-registrado y **no ejercido** NO se convierte en "se define más adelante" (sería falso; lo reporta §17.5). Criterio traído por el equipo desde la Etapa 1 y adoptado para todo el informe. | usuario · 2026-08-31 |

## B. NO TOCAR (lista cerrada)

1. **Tablas 24, 28, 36 y 37: contenido intacto** (sólo cambia su número por E2-48). En particular
   el rango **500–2.000** de la Tabla 28 y los rangos de persistencia de la Tabla 24.
2. **§17.1.6.3 (MOT17/OVT-B) y §17.1.7.4.2 (métricas MOT): intactos** (D-E2-6 sigue firmada).
   E2-47 sólo elimina una frase de remisión al anexo en §17.1.7.4.2 — el resto del apartado no se toca.
3. **El `[[PENDIENTE]]` de la AAIP en §17.1.10.1**: viaja tal cual.
4. **Las ecuaciones OMML**: quedan **78** tras el pase (85 − 7 declaradas en §G). Jamás convertir
   una ecuación a texto plano ni "reconstruir" una que se vea vacía.
5. **§17.1.7.7.1 (descomposición de latencia)**: intacta — §16.5.2 usa su notación
   (`t_capture + t_transport + t_preprocess + t_inference`).
6. **Las definiciones de CPN/EN/TN** (§17.1.4.2 y §17.1.4.3): la prosa se conserva **verbatim**
   cuando E2-41 la reubica — §17.3 depende de que nazcan acá.
7. **Los 4.000/7.000 ms de §17.1.5.3.3** (decisión de protocolo, pase 2) y la palabra "efectivos"
   sigue prohibida en §17.1.
8. **Los 27 comentarios del `.docx`**: no se eliminan, no se responden, no se resuelven — los
   resuelve el usuario en Google Docs con el mapa de §F.
9. **La Tabla 23 no se toca salvo su nota** (E2-31 le agrega una frase).
10. Los residuales ya fichados para el pase de integración **quedan como están**: "Versión
    registrada" ×2 en la Tabla 26 · `t_alert-system` como texto plano en §17.1.7.2 · el rótulo
    global de "Nota.".

**Orden de aplicación: E2-30 … E2-47 y E2-50 primero (todas citan la numeración VIEJA de tablas y
títulos); después E2-48 (renumeración) sobre el texto ya podado; y E2-49 (anexado de los Anexos C
y D) como último paso.**

---

## C. Unidades del pase

### E2-30 · §17.1.4.7 — eliminar la sección entera (la peor redundancia del documento)

Las specs y la lectura del CPN/EN/TN aparecen cuatro veces en §17.1.4 (§17.1.4.2.1, Tabla 21,
prosa de §17.1.4.7 y Tabla 22). Comentario C11 del usuario.

- **Eliminar** el título *"17.1.4.7. Lectura metodológica de la infraestructura operativa y sus
  restricciones"* y todo su contenido: los dos párrafos ("La infraestructura del proyecto se
  organiza…" y "La consecuencia metodológica es que las conclusiones…"), la **Tabla 22** completa
  con su nota, y el párrafo final ("El entorno impone restricciones explícitas…").
- **Rescatar una sola idea** (la única no cubierta por la Tabla 21): agregar al final del segundo
  párrafo de §17.1.4.2 ("Bajo este criterio, el Central Processing Node (CPN) concentra…") la
  frase: *"Las conclusiones sobre viabilidad operativa —tiempo real, latencia y uso de recursos—
  se anclan en el CPN."*
- Sin ecuaciones en la zona. §17.1.4.7 es el último hijo de §17.1.4: **no hay renumeración de
  títulos** por esta unidad. La Tabla 22 muere → su renumeración la absorbe E2-48.
- Verificación: `17.1.4.7` = 0 apariciones; "Lectura metodológica de la infraestructura" = 0.

### E2-31 · §17.1.2.2 — eliminar la Tabla 17 (catálogo duplicado con la Tabla 23)

Las Tablas 17 y 23 llevan las mismas seis filas con columnas complementarias; la prosa de
§17.1.2.1/.2.2 ya dice todo lo que la Tabla 17 agrega.

- **Eliminar** el rótulo "Tabla 17", el título *"Catálogo consolidado de condiciones de riesgo y
  rol experimental"*, la tabla completa y su nota.
- Agregar al final del segundo párrafo de §17.1.2.2 ("El catálogo completo conserva valor
  directivo…"): *"El catálogo completo, con su categoría normativa, componente evaluador y
  dificultad estimada, se presenta en la Tabla 23 (Sección 17.1.5.2.3)."*
- Agregar al **final de la nota de la Tabla 23**: *"CR-01 y CR-02 constituyen el núcleo
  obligatorio del prototipo experimental; las restantes condiciones operan como extensiones
  condicionadas que no bloquean la aceptación del núcleo."*
- Sin ecuaciones. Verificación: una sola tabla-catálogo de seis condiciones en todo §17.1.

### E2-32 · §17.1.7.7.3 — eliminar la subsección (re-explica lo que §17.1.7.7.1 y la Tabla 33 ya dicen) · ⚠ 5 ecuaciones mueren

- **Eliminar** el título *"17.1.7.7.3. Consideración sobre el razonamiento temporal"* y su único
  párrafo ("El componente ⟦…⟧ debe distinguirse explícitamente de ⟦…⟧…"). El párrafo contiene
  **5 objetos de ecuación** que mueren con él (contabilizados en §G).
- **Renumerar títulos**: 17.1.7.7.4 → **17.1.7.7.3** · 17.1.7.7.5 → **17.1.7.7.4** ·
  17.1.7.7.6 → **17.1.7.7.5**.
- **Actualizar la única referencia interna**: en el primer párrafo de la estimación orientativa,
  *"interpretar los umbrales de la Sección 17.1.7.7.6"* → *"…de la Sección 17.1.7.7.5"*.
- Verificación: "razonamiento temporal" no aparece como título; "17.1.7.7.6" = 0 apariciones.

### E2-33 · Distinción G2A / alerta / persistencia — dejar UNA casa canónica (§17.1.7.2) · ⚠ 1 ecuación muere

La distinción está explicada en §17.1.7.2, §17.1.7.7.1, la nota de la Tabla 33, §17.1.7.7.3
(muere por E2-32) y §17.1.7.7.4. Quedan: §17.1.7.2 (definición) + §17.1.7.7.1 (descomposición,
intocable) + §17.1.7.7.4 (cierre operativo con símbolos).

- **Eliminar el quinto párrafo de §17.1.7.2** completo: *"Bajo esta convención, G2A se entiende
  como el subtramo instrumental… de la interpretación humana."* (párrafo de texto plano, sin
  ecuaciones — el cierre operativo de §17.1.7.7.4 hace ese trabajo en el lugar correcto).
- **Eliminar la última oración de la nota de la Tabla 33**: *"La inclusión explícita de ⟦…⟧
  responde a que la latencia de alerta confirmada no se reduce al costo computacional del
  pipeline, sino que incorpora además la ventana funcional necesaria para acumular evidencia
  suficiente antes de registrar una alerta interna."* (⚠ contiene **1 ecuación**, muere con ella;
  la idea ya está en la fila de la propia tabla y en §17.1.7.7.1).
- El resto de §17.1.7.2 (párrafos 1–4) **no se toca**.

### E2-34 · §17.1.3.2 — el motor de patrones se cuenta una vez

El segundo párrafo de §17.1.3.2 describe entradas y funciones del motor casi igual que
§17.1.5.3.4 (su casa de desarrollo).

- **Reemplazar** el segundo párrafo de §17.1.3.2 ("En términos operativos, esta evaluación
  corresponde al motor de patrones… puede registrarse una alerta interna dentro del sistema.")
  por: *"En términos operativos, esta evaluación corresponde al motor de patrones, entendido como
  una abstracción lógica del plano de control que aplica criterios de persistencia, severidad,
  histéresis y lógica espacial o contextual sobre los eventos de detección. Sólo cuando un patrón
  alcanza el estado confirmado puede registrarse una alerta interna dentro del sistema; su
  operacionalización se desarrolla en la Sección 17.1.5.3.4."*
- Los párrafos primero y tercero de §17.1.3.2 y la Tabla 18 **no se tocan**.

### E2-35 · §17.1.5.3.2 — comprimir las enumeraciones normativas (los artículos ya viven en la Tabla 24) · ⚠ conservar la frase final del párrafo crítico

Los tres párrafos de nivel repiten en prosa los artículos del Decreto 911/96 que la columna
"Perfil temporal del riesgo" de la Tabla 24 ya lleva por patrón. **Las definiciones de cada nivel
(primera oración) y las frases de cierre quedan verbatim; sólo se comprime la narración de
artículos.**

- Párrafo del **nivel crítico**: conservar la primera oración y la última (*"En ambos casos, la
  exposición observada… dentro del framework evaluativo."* — ⚠ esta última contiene **un objeto de
  ecuación** entre "TTFD y" y "dentro": se conserva tal cual). Reemplazar el tramo intermedio por:
  *"El Decreto 911/96 establece las medidas de prevención frente al riesgo de caída de personas y
  los trabajos con riesgo de caída a distinto nivel (arts. 52 a 57), y regula la operación de
  vehículos y maquinaria automotriz junto con la protección frente a la circulación vehicular
  —señalización, vallado, equipos de alta visibilidad, vigías— (arts. 246 a 249)."*
- Párrafo del **nivel alto**: conservar primera oración y las dos últimas ("La ausencia de casco…"
  y "En esa misma lógica…"). Reemplazar el tramo intermedio por: *"El Decreto 911/96 regula la
  provisión, uso, condiciones y vida útil de los equipos de protección personal y la vestimenta de
  trabajo (arts. 98 a 106), y la provisión de casco de seguridad para tareas con riesgos
  específicos (art. 107)."*
- Párrafo del **nivel medio**: conservar primera y última oración. Reemplazar el tramo intermedio
  por: *"La obligación de emplear elementos reflectivos o de alta visibilidad se vincula con los
  trabajos nocturnos y con la construcción de carreteras en uso (Decreto 911/96, arts. 63 y 70), y
  puede complementarse con la Resolución SRT 299/2011 sobre registración y constancia de entrega
  de ropa de trabajo y EPP."*
- El párrafo introductorio, el segundo párrafo y el párrafo final de la subsección no se tocan.

### E2-36 · §17.1.11.2 — eliminar los seis párrafos en negrita (la articulación está contada tres veces)

Tabla 16, §17.1.11.1 y §17.1.11.2 narran lo mismo. Quedan: el primer párrafo de §17.1.11.2 y el
párrafo puente ("Esta consolidación distribuye sus salidas…" — ⚠ contiene 2 ecuaciones, **no se
toca**).

- **Eliminar** los seis párrafos que arrancan en negrita: **Alcance experimental consolidado** ·
  **Escenarios e infraestructura** · **Estrategia de datos y partición** · **Framework de métricas
  y registro** · **Regla de adaptación al dominio** · **Supuestos y riesgos de validez** (desde
  *"**Alcance experimental consolidado**. Establece la frontera inicial…"* hasta *"…sin reemplazar
  la supervisión humana ni asumir decisiones operativas automáticas."*).
- **Rescatar el cierre** agregando como párrafo final de §17.1.11.2: *"Estas definiciones
  preservan el carácter experimental del trabajo y mantienen la orientación central del proyecto:
  evaluar si la detección open-vocabulary puede integrarse como herramienta asistiva útil para el
  monitoreo de condiciones de riesgo en construcción civil, sin reemplazar la supervisión humana
  ni asumir decisiones operativas automáticas."*
- Sin ecuaciones en lo eliminado.

### E2-37 · Síntesis parciales — que sinteticen, no que re-desarrollen · ⚠ 1 ecuación muere

**En §17.1.6.5** (comentario C20):
- Reemplazar el párrafo *"La partición de datos se rige por cinco reglas obligatorias…"* por la
  frase: *"La partición de datos se rige por las condiciones metodológicas obligatorias de la
  Tabla 28."*
- **Eliminar** el párrafo *"Para las condiciones brechadas, la política de datos complementarios
  sigue un orden de preferencia conservador…"* (duplica §17.1.6.2.6 completo).
- El primer párrafo, la Tabla 31 con su nota y los párrafos de benchmarks y de sobre-declaración
  **quedan**.

**En §17.1.7.9**:
- Reemplazar el segundo párrafo (*"La jerarquía de métricas no implica…"*) por: *"La jerarquía no
  implica ejecución universal: cada métrica queda subordinada a los criterios de ejecutabilidad de
  la Sección 17.1.7.3.3, por lo que el protocolo distingue entre métricas definidas, métricas
  efectivamente medibles y métricas no aplicables."*
- Del párrafo posterior a la Tabla 34 (*"La latencia operativa principal es ⟦…⟧, definida como el
  intervalo…"*): **conservar sólo la primera oración** (hasta *"…registrada dentro del sistema."*)
  y eliminar el resto (⚠ el resto contiene **1 ecuación**, muere; su contenido está en
  §17.1.7.5.1).
- **Eliminar** el párrafo siguiente completo (*"TTFD mide el tiempo hasta la primera detección
  positiva válida… sin continuidad temporal."* — re-define lo que §17.1.7.5.2/.5.3 ya definieron).
- **Eliminar** el último párrafo de la subsección (*"Además del framework de métricas, cada
  ejecución deberá conservar una bitácora mínima…"* — duplica §17.1.7.8.4). El párrafo anterior
  ("Finalmente, todo reporte experimental deberá conservar trazabilidad mínima…") **queda**.
- El primer párrafo (con las citas Everingham/Lin/Bernardin/Ristani/Luiten/Yao) **queda intacto**:
  tras la baja de las ex-tablas D.1/D.2 es la casa de esas citas.

### E2-38 · Disclaimers repetidos — dos recortes quirúrgicos

- §17.1.5.3.3, cuarto párrafo (*"Conviene precisar que estos rangos tienen carácter analítico y
  orientativo…"*): reemplazar el párrafo completo por la frase *"Estos rangos tienen carácter
  analítico; los valores definitivos se calibran empíricamente durante la validación experimental,
  una vez conocido el throughput efectivo."*
- §17.1.5.3.4, última oración del último párrafo (*"Con esta delimitación, se busca cerrar la
  brecha entre patrón conceptual y evaluación en runtime, hasta que queden completamente definidas
  en el diseño arquitectónico."* — además de repetida, es agramatical): reemplazar por *"Con esta
  delimitación se cierra la brecha entre el patrón conceptual y su evaluación en runtime."*
- La declaración general de §17.1.5.3 (intro) y la de la apertura de §17.1 **quedan**: son las
  casas del disclaimer.

### E2-39 · §17.1.5.3.6 — PR-05/PR-06 a criterios conceptuales (el detalle de materialización es de la instancia de diseño, como declara §17.1.5.3.7)

- **Reemplazar** el párrafo de PR-05 (*"PR-05 — maquinaria en proximidad a peatones. La activación
  requiere…"*) por: *"PR-05 — maquinaria en proximidad a peatones. La activación requiere la
  detección simultánea de al menos una entidad clasificable como maquinaria de obra —por ejemplo,
  excavadora, retroexcavadora, camión volquete o grúa— y al menos una persona, cuyas detecciones
  presenten una relación de proximidad inferior a un umbral configurable. Toda métrica de
  proximidad calculada en coordenadas de imagen debe interpretarse como una medida geométrica 2D
  aproximada y no como una distancia física real, dado que la perspectiva de cámara altera las
  distancias aparentes. La evaluación debe sostenerse durante el intervalo de persistencia
  definido para el patrón, lo que exige trayectorias suficientemente estables de las entidades
  involucradas. La selección de puntos representativos de las detecciones y de la métrica
  geométrica concreta corresponde a la instancia de análisis y diseño arquitectónico."*
- **Reemplazar** el párrafo de PR-06 (*"PR-06 — persona en zona restringida. La activación
  requiere…"*) por: *"PR-06 — persona en zona restringida. La activación requiere la detección de
  al menos una persona cuya posición representativa se encuentre contenida dentro de un polígono
  predefinido que representa la zona restringida. El polígono forma parte de la parametrización
  del sistema —configurable por el operador, externo al prompt OVD— y presupone una cámara fija,
  supuesto adoptado para el alcance del prototipo experimental. La permanencia debe sostenerse
  durante el intervalo de persistencia, lo que implica seguimiento temporal cuando la persistencia
  se compute por entidad individual. El mecanismo de definición de polígonos y la lógica de
  contención corresponden a la instancia de análisis y diseño arquitectónico."*
- El párrafo introductorio y el párrafo final (dependencia del MOT, ID switches) **quedan**.

### E2-40 · §17.1.5.1 — introducción sin re-desarrollo (comentario C12)

- **Reemplazar los dos primeros párrafos** por uno solo: *"La presente sección responde a la
  pregunta rectora P-E1-02 definida en la fundamentación teórica, que dejó abierta la brecha entre
  la identificación normativa de condiciones de riesgo y su traducción en consultas textuales
  evaluables por modelos de detección open-vocabulary, y señaló que la formulación del prompt no
  es un detalle accesorio sino una variable capaz de alterar significativamente el desempeño del
  detector en dominios especializados. Sobre esa base, la sección define la taxonomía de
  condiciones de riesgo del prototipo experimental, establece los patrones de riesgo asociados con
  severidad y persistencia orientativa, y fija un protocolo sistemático para el diseño y la
  evaluación de prompts OVD. En articulación con el framework de métricas, delimita además cómo
  esas definiciones deben leerse respecto de la latencia de alerta, las métricas operativas y los
  criterios de aplicación del framework evaluativo."*
- El tercer párrafo ("El alcance de la sección es metodológico…") **queda intacto**.

### E2-41 · §17.1.4 — fusionar los seis títulos-muñón (comentarios C0–C4, C6–C9) · ⚠ prosa verbatim

Seis subsecciones de 1–2 líneas cuyo único cuerpo es la remisión al Anexo B. **La prosa se mueve
sin cambiar una palabra; sólo desaparecen los títulos.** Las remisiones a las Tablas B.1–B.7
quedan inline (el Anexo B no se toca).

- Título *"17.1.4.2.4. Stack de software de inferencia (CPN)"*: mover su párrafo al final de
  §17.1.4.2.1 (tras la remisión a B.1/B.3) y eliminar el título.
- Títulos *"17.1.4.3.1. Training Node (TN)"*, *"17.1.4.3.2. Stack de software de entrenamiento
  (TN)"* y *"17.1.4.3.3. Flujo de transferencia y evaluación"*: mover sus tres párrafos, en ese
  orden, como párrafos 3–5 del cuerpo de §17.1.4.3 y eliminar los tres títulos.
- Títulos *"17.1.4.5.1. Parámetros de referencia del pipeline"* y *"17.1.4.5.2. Transporte de
  video en el escenario B"*: mover sus dos párrafos como párrafos 2–3 del cuerpo de §17.1.4.5 y
  eliminar ambos títulos.
- **Ningún otro número de sección cambia** (`17.1.4.4` y `17.1.4.6` conservan su número).
- Verificación: −6 títulos; "17.1.4.2.4" = 0 · "17.1.4.3.1" = 0 · "17.1.4.5.1" = 0; las 7
  remisiones a B.1–B.7 siguen presentes.

### E2-42 · Gramática — seis reparaciones exactas (verificadas en el XML)

| # | Dónde | Buscar | Reemplazar por |
|---|---|---|---|
| 1 | §17.1.5.3.3 | "una vez conocido el tasa de cuadros real" | "una vez conocida la tasa de cuadros real" |
| 2 | Nota de la Tabla 24 | "basada en el análisis normativo de la el Decreto 911/96 y la Ley 19.587" | "basada en el análisis normativo del Decreto 911/96 y la Ley 19.587" |
| 3 | §17.1.6.1.2 | "corresponde al análisis de el análisis de modelos OVD" | "corresponde al análisis de modelos OVD" |
| 4 | §17.1.7.4.2 | "desarrolladas en la el análisis de seguimiento multiobjeto" | "desarrolladas en el análisis de seguimiento multiobjeto" |
| 5 | §17.1.7.7.5 | "Por un lado, la el análisis de operación en tiempo real identifica" | "Por un lado, el análisis de operación en tiempo real identifica" |
| 6 | §17.1.7.7.5 | "por otro, la el análisis de modelos OVD documenta" | "por otro, el análisis de modelos OVD documenta" |

Verificación: `" la el "` = 0 · `"de el análisis"` = 0 · `"el tasa"` = 0.

### E2-43 · Tabla 21 — la cifra 50–250 ms no sale de ninguna suma del propio documento

La fila atribuye "50–250 ms" al framework de métricas, pero el framework deriva 30–220 ms para
G2A estricto y 35–250 ms para el tramo captura→evidencia utilizable (§17.1.7.7.5). El 50–250 no
existe en ningún otro lugar del informe (verificado). Se alinea a la banda que el framework sí
deriva:

- Fila de la Tabla 21: celda 1 *"Presupuesto de latencia G2A de 50–250 ms"* → *"Presupuesto de
  latencia por cuadro, desde la captura hasta la evidencia utilizable para alerta, del orden de
  35–250 ms"*; celda 2 *"el framework de métricas"* → *"El framework de métricas (Sección
  17.1.7.7)"*. La celda de implicación no cambia.
- Verificación: "50–250" = 0 apariciones.

### E2-44 · §17.1.5.5 — quitar la meta-referencia al versionado del propio documento

- *"Esta aclaración reemplaza formulaciones más difusas de la versión anterior y deja explícito
  qué variable se está midiendo cuando se habla del “tamaño” o de la “composición” del
  vocabulario."* → *"Esta aclaración deja explícito qué variable se mide cuando se habla del
  “tamaño” o de la “composición” del vocabulario."*
- Verificación: "versión anterior" = 0.

### E2-45 · §17.1.7.7.5 (renumerada .4 por E2-32) — partir el párrafo de ~450 palabras · ⚠ SOLO saltos de párrafo

Insertar tres saltos de párrafo, **sin cambiar ni una palabra ni tocar ecuaciones**, antes de:
1. *"Para ⟦…⟧, un rango de 5 a 20 ms constituye una estimación de ingeniería **razonable** para
   operaciones de redimensionado…"* (el tramo de preprocesamiento).
2. *"Para ⟦…⟧, conviene tratar el rango de 15 a 150 ms como una banda orientativa…"* (el tramo de
   inferencia).
3. *"Para ⟦…⟧, un rango de 5 a 20 ms constituye una estimación **conservadora y plausible** para
   trackers ligeros…"* (el tramo de seguimiento — ojo: hay dos oraciones que empiezan con "un
   rango de 5 a 20 ms"; se distinguen por "razonable" vs. "conservadora").

### E2-46 · Fine-tuning en los escenarios — condicionar, no restringir (D-P3-3; comentario C5)

- §17.1.4.4, última oración del párrafo introductorio: *"En ambos escenarios, la evaluación
  contempla la ejecución tanto de modelos preentrenados (baseline) como de modelos ajustados
  mediante fine-tuning en el TN (Sección 17.1.9), permitiendo una comparación directa del impacto
  de la adaptación al dominio."* → *"En ambos escenarios, la evaluación contempla la ejecución de
  los modelos preentrenados (baseline) y, cuando una variante ajustada haya sido adoptada conforme
  a las condiciones de la Sección 17.1.9, de los modelos ajustados mediante fine-tuning en el TN,
  permitiendo una comparación directa del impacto de la adaptación al dominio."*
- §17.1.4.4.2, última oración del párrafo: *"Al igual que en el Escenario A, se ejecutan las
  variantes preentrenada y fine-tuned de cada modelo candidato seleccionado tras la evaluación del
  Escenario A."* → *"Al igual que en el Escenario A, se ejecuta la variante preentrenada y, cuando
  haya sido adoptada conforme a la Sección 17.1.9, la variante fine-tuned del modelo candidato
  seleccionado tras la evaluación del Escenario A."*
- Tabla 20, fila "Modelos evaluados": *"Variante preentrenada (baseline) y variante fine-tuned,
  sobre el modelo o combinación seleccionada tras el Escenario A."* → *"Variante preentrenada
  (baseline) y, cuando corresponda conforme a la Sección 17.1.9, variante fine-tuned, sobre el
  modelo o combinación seleccionada tras el Escenario A."*
- La fila equivalente de la Tabla 19 ya dice "cuando aplique": **no se toca**.

### E2-47 · Remisiones a los Anexos C y D — actualizar a la composición final (D-P3-5; el contenido está en `90g`)

Numeración final de anexos: **Anexo C = C.1 (prompts) · C.2 (variables EBE) · C.3 (logística,
ex-C.5 reescrita)** · **Anexo D = D.1 (ex-D.3, pipeline) · D.2 (ex-D.5, insumos) · D.3 (ex-D.6,
bitácora)**.

| Dónde | Acción |
|---|---|
| §17.1.7.4.1 | **Eliminar** la oración *"Pueden verse estas métricas en la Tabla D.1 del Anexo D."* (la ex-D.1 se elimina; su único aporte —las citas— vive en el primer párrafo de §17.1.7.9). |
| §17.1.7.4.2 | **Eliminar** la oración *"El análisis de las métricas de seguimiento multiobjeto puede verse en la Tabla D.2 del Anexo D."* (ídem; el resto del apartado NO se toca). |
| §17.1.7.4.3 | *"…queda desarrollado en la Tabla D.3 del Anexo D."* → *"…queda desarrollado en la Tabla D.1 del Anexo D."* |
| §17.1.7.7.6 (→.5) | *"Una lista de los umbrales orientativos por severidad puede verse en la Tabla D.4 del Anexo D."* → *"Los umbrales orientativos consolidados se presentan en la Tabla 35 (Sección 17.1.7.9)."* (E2-48 renumera "Tabla 35" junto con todo lo demás). |
| §17.1.7.8.1 | *"Esto se desarrolla de manera más sintética en la Tabla D.5 del Anexo D."* → *"Los insumos mínimos por familia de métricas se consolidan en la Tabla D.2 del Anexo D."* |
| §17.1.7.8.4 | Agregar al final del primer párrafo: *"El detalle de campos recomendados se consolida en la Tabla D.3 del Anexo D."* (la ex-D.6 estaba huérfana). |
| §17.1.6.4.2 | *"Esto puede verse en detalle en la Tabla C.5 del Anexo C."* → *"La logística de conversión y acceso por fuente se detalla en la Tabla C.3 del Anexo C."* |
| §17.1.4.4.2 | Agregar al final del párrafo (tras la oración condicionada por E2-46): *"Las variables de sensibilidad candidatas para este escenario se catalogan en la Tabla C.2 del Anexo C."* (la C.2 estaba huérfana). |
| §17.1.5.4.4 | La remisión al *"Anexo C (Tabla C.1)"* **queda tal cual**. |

Verificación: "Tabla D.4" = 0 · "Tabla D.5" = 0 · "Tabla D.6" = 0 · "Tabla C.5" = 0 · "Tabla C.4"
= 0; "Tabla C.1" … "Tabla D.3" = 1 remisión cada una en el cuerpo (tras E2-49 cada nombre queda
2 veces en el documento: la remisión + su rótulo en el anexo).

### E2-48 · Renumeración final de tablas — 16–36 contiguas (D-P3-2) · SE APLICA AL FINAL

Con las Tablas 17 y 22 eliminadas, renumerar **rótulos y referencias textuales**:

| Vieja | Nueva | · | Vieja | Nueva | · | Vieja | Nueva |
|---|---|---|---|---|---|---|---|
| 16 | 16 | | 25 | 23 | | 32 | 30 |
| 18 | 17 | | 26 | 24 | | 33 | 31 |
| 19 | 18 | | 27 | 25 | | 34 | 32 |
| 20 | 19 | | 28 | 26 | | 35 | 33 |
| 21 | 20 | | 29 | 27 | | 36 | 34 |
| 23 | 21 | | 30 | 28 | | 37 | 35 |
| 24 | 22 | | 31 | 29 | | 38 | 36 |

Referencias textuales a actualizar (además de los 21 rótulos):
- *"Las restricciones detalladas en la Tabla 21"* (§17.1.4.6) → Tabla 20.
- *"La Tabla 23 presenta las seis condiciones…"* (§17.1.5.2.3) → Tabla 21.
- *"del catálogo (Tabla 23)"* (§17.1.5.4.2) → (Tabla 21).
- *"el catálogo de condiciones de riesgo clasificado por niveles de complejidad (Tabla 23)"* y
  *"el catálogo de patrones con severidad y persistencia temporal orientativa (Tabla 24)"*
  (§17.1.5.3.7) → (Tabla 21) y (Tabla 22).
- *"La Tabla 24 presenta el catálogo de patrones…"* (§17.1.5.3.5) → Tabla 22.
- *"conserva el estatuto y la causa resumidos en la Tabla 27"* (§17.1.6.4.1) → Tabla 25.
- *"La Tabla 29 sintetiza la aptitud metodológica…"* (§17.1.6.2.8) → Tabla 27.
- Las frases **nuevas** de E2-31 ("…Tabla 23 (Sección 17.1.5.2.3)"), E2-37 ("…Tabla 28") y E2-47
  ("…Tabla 35 (Sección 17.1.7.9)") se renumeran igual que todo lo demás → Tabla 21, Tabla 26 y
  Tabla 33 respectivamente.

Verificación: rótulos contiguos "Tabla 16" … "Tabla 36" sin huecos; "Tabla 37" = 0 y "Tabla 38" =
0; ninguna referencia textual apunta a un número sin rótulo.

### E2-50 · Voz del documento: lo que remite a una sección que existe deja de sonar "a definir" (D-P3-9) · SE APLICA ANTES DE E2-48

**El problema, medido.** §17.1 se escribió cuando §17.3/§17.4/§17.5 no existían, y arrastra 15
pasajes que enmarcan como *obligación futura* algo que hoy vive en una sección escrita del mismo
informe ("la instancia de análisis y diseño arquitectónico **deberá** materializar…"). Leído junto
con §17.4/§17.5 —que tienen **cero** de estas formulaciones (verificado)— el capítulo suena a
trabajo sin terminar. El propio documento ya usa la forma correcta **6 veces**
("*corresponde a* la instancia de análisis y diseño arquitectónico"), así que esto es **unificar
una voz que ya convive**, no inventar una nueva.

**⚠ La regla NO es "sacar todo lo que remita a etapas posteriores".** Hay tres tipos de futuro en
§17.1 y **sólo uno se toca**:

| Tipo | Ejemplo | Qué se hace |
|---|---|---|
| **A. Remisión a algo que sí se desarrolla después** | "la instancia … **deberá** traducir esta definición en componentes" | ✅ **Presente**: "…traduce esta definición en componentes". Se cambia el **tiempo verbal y el encuadre**, nunca se agrega el contenido de la definición (eso sería anacronismo). |
| **B. Prescripción normativa del protocolo** | "Toda corrida **deberá** declarar modelo, versión, checkpoint…" · "toda métrica no ejecutada **deberá** declararse con su causa" | ⛔ **NO SE TOCA.** Son ~25 de los 41 `deberá`: es la voz de un protocolo, no una promesa pendiente. Tocarlas destruye §17.1.7.8. |
| **C. Diferido a algo que nunca ocurrió** | "Su análisis de cobertura queda **diferido a etapas posteriores**" (calzado, guantes, gafas) | ⚠ **No** convertir en "se ve más adelante" —sería **falso**—: se convierte en **delimitación de alcance**. |

**Reemplazos exactos (12 sitios):**

| # | § | Ahora | Queda |
|---|---|---|---|
| 1 | 17.1.1.1 | "la transición entre la fundamentación teórica y las instancias posteriores de diseño, implementación y validación" | "la transición entre la fundamentación teórica y las instancias de diseño, implementación y validación" |
| 2 | 17.1.4.6 | "condicionan las decisiones de diseño de etapas posteriores y deben tenerse presentes" | "condicionan las decisiones del diseño arquitectónico y de la implementación, y deben tenerse presentes" |
| 3 | 17.1.5.3.3 | "La instancia de análisis y diseño arquitectónico tomará estos rangos como referencia para diseñar los mecanismos computacionales de evaluación de persistencia." | "Estos rangos son la referencia con la que la instancia de análisis y diseño arquitectónico define los mecanismos computacionales de evaluación de persistencia." |
| 4 | 17.1.5.3.3 | "Un aspecto adicional que la instancia de análisis y diseño arquitectónico deberá considerar es el comportamiento de histéresis" | "Un aspecto adicional, que se retoma en la instancia de análisis y diseño arquitectónico, es el comportamiento de histéresis" |
| 5 | 17.1.5.3.4 | "La instancia de análisis y diseño arquitectónico deberá traducir esta definición en componentes, contratos, eventos y configuraciones concretas; la implementación del prototipo deberá materializarla; y la validación experimental deberá calibrar empíricamente sus umbrales, ventanas e histéresis." | "La instancia de análisis y diseño arquitectónico traduce esta definición en componentes, contratos, eventos y configuraciones concretas; la implementación del prototipo la materializa; y la validación experimental calibra empíricamente sus umbrales, ventanas e histéresis." |
| 6 | 17.1.5.3.7 | "Sobre esa base, la instancia de análisis y diseño arquitectónico deberá materializar el esquema declarativo de patrones" | "Sobre esa base, la instancia de análisis y diseño arquitectónico materializa el esquema declarativo de patrones" |
| 7 | 17.1.5.3.7 | "En particular, deberá definir cómo se traducen los criterios conceptuales en reglas operativas configurables" | "En particular, allí se define cómo se traducen los criterios conceptuales en reglas operativas configurables" |
| 8 | 17.1.5.4.2 | "La instancia de análisis y diseño arquitectónico deberá materializar la lógica de asociación espacial requerida por la estrategia indirecta y determinar si su costo" | "La instancia de análisis y diseño arquitectónico materializa la lógica de asociación espacial requerida por la estrategia indirecta y determina si su costo" |
| 9 | 17.1.5.5 | "Por ello, la instancia de análisis y diseño arquitectónico deberá contrastar familias de prompts antes de congelar la configuración comparativa final." | "Por ello, el contraste entre familias de prompts precede al congelamiento de la configuración comparativa final en la instancia de análisis y diseño arquitectónico." |
| 10 | 17.1.6.1.2 | "Su análisis de cobertura queda diferido a etapas posteriores, en caso de que se decida ampliar el conjunto de condiciones evaluadas." | "Su análisis de cobertura queda fuera del alcance de esta instancia y sólo correspondería si se ampliara el conjunto de condiciones evaluadas." |
| 11 | 17.1.6.4.1 | "En consecuencia, la instancia de análisis y diseño arquitectónico deberá verificar manualmente los términos efectivos de cada fuente" | "En consecuencia, la instancia de análisis y diseño arquitectónico verifica manualmente los términos efectivos de cada fuente" |
| 12 | 17.1.6.3.2 | "la validación del dominio específico se mantiene separada y deberá realizarse sobre los datos del proyecto" | "la validación del dominio específico se mantiene separada y se realiza sobre los datos del proyecto" |

⚠ **Coordinación con otras unidades**: el sitio 5 está en el mismo párrafo que E2-38 (que reescribe
su **última** oración) — son oraciones distintas, se aplican las dos. Los sitios 2 y 10 citan
"Tabla 21" y texto que E2-48 renumera: **por eso E2-50 se aplica ANTES de E2-48**. El párrafo de
PR-06 que contenía "debe diseñar tanto el mecanismo de definición de polígonos" ya lo reescribe
**E2-39** con la forma neutra ("corresponden a"): **no se toca dos veces**.

**Deliberadamente NO se tocan** (son correctos y su cambio introduciría falsedad o rompería la voz
del protocolo): los ~25 `deberá`/`deberán` cuyo sujeto es una corrida, un reporte, una métrica, la
instrumentación o la bitácora · los `podrá` que expresan **permiso** del protocolo ("podrá
apartarse de ese esquema si justifica la decisión", "podrá establecer valores iniciales
configurables") · los `todavía` que expresan correctamente que **esta** instancia no decide algo
("la retención no asigna **todavía** un rol definitivo", "sin asignar **todavía** un rol efectivo",
"No define **todavía** la combinación definitiva de datasets") · el condicional de lo
**pre-registrado y no ejercido** (MOT17/OVT-B, prompts en español, doble anotación y kappa, datos
complementarios para CR-03/CR-04): **no puede decirse que "se define más adelante", porque no
ocurrió** — se mantiene como protocolo y §17.5 lo reporta como no ejercido (D-E2-6) · el
`[[PENDIENTE]]` de la AAIP, que **sí** es una decisión abierta del equipo (D-E2-7).

**Verificación:** "etapas posteriores" = 0 · "instancias posteriores" = 0 · "queda diferido" = 0 ·
las apariciones de `deberá` (que incluyen `deberán`) bajan de **41 a ~33**: caen sólo las de
remisión — **si baja de 30, se tocó prescripción normativa y hay que revisar** · "corresponde/n a
la instancia de análisis" ≥ 6 · los `todavía` siguen siendo **7**.

### E2-49 · Anexar los Anexos C y D al final del documento (D-P3-8) · ÚLTIMO PASO

El contenido completo y final está en **`90g-etapa2-anexos-c-y-d.md`** (adjunto junto con este
pase), secciones *"Contenido final del Anexo C (pegar tal cual)"* y *"Contenido final del Anexo D
(pegar tal cual)"*.

- **Dónde**: después del último párrafo de §17.1.11.2 (tras el párrafo de cierre agregado por
  E2-36).
- **Encabezados**: *"Anexo C — Prompts, datos, datasets, benchmarks y logística"* y *"Anexo D —
  Métricas, instrumentación y bitácora experimental"*, **sin número** y con el **mismo estilo de
  encabezado que el título "17.1. Consolidación metodológica del protocolo experimental"** (la
  numeración 19.3/19.4 es del maestro y se asigna al integrar).
- **Contenido**: 3 tablas en C (C.1 · C.2 · C.3) y 3 en D (D.1 · D.2 · D.3), exactamente como
  vienen en `90g` — rótulo `**Tabla C.1**` en negrita, título de tabla en itálica, `*Nota.*` en
  itálica. Los nombres de métrica dentro de las tablas del anexo van como **texto plano**
  (t_alert-system, latencia G2A…), igual que TTFD y SDR — la unificación con los objetos de
  ecuación del cuerpo es del pase de integración.
- ⚠ **No inventar ni completar nada**: si algo del `90g` no puede reproducirse tal cual, se
  reporta en la entrega en lugar de improvisar.
- Verificación: el documento cierra con los dos anexos; 3 rótulos `Tabla C.x` + 3 `Tabla D.x`;
  cada tabla de anexo queda con exactamente 2 apariciones de su nombre en el documento (la
  remisión de E2-47 en el cuerpo + su rótulo en el anexo); cero `Tabla C.4`/`C.5`/`D.4`/`D.5`/
  `D.6`; `bench_obra` = 0.

---

## D. Lo que este pase deliberadamente NO hace

- **No** poda el catálogo CR-01…CR-06 ni ninguna condición (D-P3-7).
- **No** corrige el protocolo contra lo implementado: el rango 500–2.000, MOT17/OVT-B, la
  estimación de latencia y las promesas no ejercidas quedan como protocolo; §17.5 las reporta.
- **No** fusiona las Tablas 23 y 24 ni toca su contenido.
- **No** edita el Anexo B (sano: 7/7 tablas referenciadas, verificado pieza a pieza en PODA-14).
- **No** resuelve el `[[PENDIENTE]]` de la AAIP (decisión del equipo, D-E1-11).
- **No** toca los comentarios del `.docx` (los resuelve el usuario con el mapa §F).

## E. Anexos C y D

El contenido final completo, con las tablas reescritas y las razones de cada baja, está en
**`90g-etapa2-anexos-c-y-d.md`** (D-E2-1 ejecutada y refinada; D-P3-5). Por **D-P3-8**, los
anexos **se anexan al final del documento de la etapa** (unidad E2-49, con el `90g` adjunto);
al integrar al maestro, el equipo los muda a §19.3/§19.4. A ChatGPT le corresponden E2-47
(remisiones del cuerpo) y E2-49 (anexado).

## F. Mapa de los 27 comentarios del usuario en el `.docx` → resolución

| Comentario (ancla) | Resolución |
|---|---|
| C0, C1 (Tablas B.1/B.2/B.3, §17.1.4.2.1/.2.3) | Anexo B queda como está; remisiones inline tras E2-41. |
| C2, C3, C4, C6, C7 (Tablas B.3–B.7, muñones) | **E2-41** — los títulos-muñón se fusionan; las remisiones quedan. |
| C5 (limitar FT a datasets) | **E2-46** (D-P3-3): se condiciona a la adopción conforme a §17.1.9; no se restringe a DBE (no-anacronismo). |
| C8, C9 (subsecciones chicas / qué vuelve del anexo) | **E2-41** + veredicto D-P3-5/D-P3-8: del Anexo B no vuelve nada; los Anexos C y D se reducen y viajan al final del documento (90g + E2-49). |
| C10 (presupuesto G2A vs implementado) | **E2-43**: se corrige la incoherencia **interna** (50–250 no suma con el propio framework). La confrontación con lo medido es de §17.5. |
| C11 (§17.1.4.7 repetitivo) | **E2-30** — la sección se elimina entera. |
| C12 (§17.1.5.1 más breve) | **E2-40**. |
| C13 (§17.1.5.3.3 más breve) | **E2-38** (y E2-33 quita una repetición vecina). |
| C14, C15 (Tabla C.1 / Anexo C) | **90g + E2-49** + D-P3-4: C.1 queda como ancla del Anexo C reducido, que ahora viaja al final del documento; §17.1.5.4.4 la sigue citando. |
| C16, C17, C18 (anacronismos en §17.1.6) | Verificado: sin anacronismos duros; el pase 2 ya blindó la rama. Residual "Versión registrada" queda fichado para la integración. **Sin unidad.** |
| C19 (Tabla C.5) | **90g** (C.5 → C.3, reescrita para las 4 retenidas) + **E2-47/E2-49**. |
| C20 (síntesis §17.1.6.5) | **E2-37** — la Tabla 31 queda; la prosa duplicada cae. |
| C21, C22 (Tablas D.1/D.2) | **90g** (se eliminan) + **E2-47**. |
| C23 (Tabla D.3) | **90g** (se conserva como D.1) + **E2-47/E2-49**. |
| C24 (¿estimación válida?) | **D-P3-6**: se mantiene — es protocolo ex-ante con sus disclaimers correctos; sólo se parte el párrafo (**E2-45**). |
| C25 (Tabla D.4) | **90g** (se elimina: ≡ Tabla 35) + **E2-47**. |
| C26 (Tabla D.5) | **90g** (fila "Alerta" duplicada fusionada; queda como D.2) + **E2-47/E2-49**. |

## G. Verificación de cierre (targets de la v1.4)

| Métrica | Partida | Target | Cómo |
|---|---|---|---|
| Palabras | 28.564 | **~28.400–29.000** = ~26,0–26,5k del desarrollo (sin cuota: si una unidad no cierra limpia, se deja constancia y no se fuerza) + ~2,4k de los anexos (E2-49) | verificador |
| Títulos numerados | 117 | **109** (−8: §17.1.4.7, §17.1.7.7.3 y los 6 muñones; los 2 encabezados de anexo van SIN número y no cuentan) | verificador |
| Tablas | 23 (16–38) | **21 numeradas (16–36 contiguas) + 6 de anexo (C.1–C.3, D.1–D.3)** | grep de rótulos |
| Ecuaciones OMML | 85 | **78** (−7: 5 en E2-32, 1 en E2-33, 1 en E2-37 — ninguna otra unidad puede matar una ecuación; los anexos usan nombres en texto, no agregan objetos) | conteo `m:oMath` en el XML |
| Marcadores | 1 (`[[PENDIENTE]]` AAIP) | 1 | grep |
| Greps en cero | — | `" la el "` · `"de el análisis"` · `"el tasa"` · `"50–250"` · `"versión anterior"` · `"17.1.7.7.6"` · `"Tabla 37"` · `"Tabla 38"` · `"Tabla C.4"` · `"Tabla C.5"` · `"Tabla D.4"` · `"Tabla D.5"` · `"Tabla D.6"` · **`"etapas posteriores"` · `"instancias posteriores"` · `"queda diferido"`** | extracción |
| Voz (E2-50) | `deberá` 41 · `todavía` 7 | **`deberá` ~33** (no menos de 30: por debajo se tocó prescripción normativa) · **`todavía` 7 intacto** | grep |
| Verificador | OK | OK, sin problemas duros | `verificar_entregable.py --seccion 17.1` |
| Diff | — | párrafo a párrafo contra `90f` (2026-08-31): cada bloque cambiado se atribuye a una unidad E2-30…E2-50 | como en el pase 2 |

## H. Handoffs que este pase deja registrados

1. **Pase de integración final**: renumeración **global** de tablas del informe — §17.1 entrega
   16–36, así que las tablas de §17.3 en adelante (hoy 39–55) corren −2 al integrar. Nada que
   hacer ahora; queda anotado.
2. **§17.3 v1.4 → v1.5**: sigue pendiente el recorte de la glosa de §17.3.6.4 (E3-42, ya
   registrado). Este pase **no agrega** ningún handoff numérico hacia §17.3/§17.4/§17.5
   (verificado: cero acoplamiento por número de tabla).
2-bis. **D-P3-9 aplicada al resto del informe** (medido el 2026-08-31, es un criterio de casa, no
   sólo de §17.1): **§15+§16 = 7 sitios** — "deberán abordarse durante el diseño", "deberá
   abordarse como parte del diseño experimental en la etapa 2", "se abordarán en etapas
   posteriores", "etapas posteriores del proyecto en las que se definirán los patrones de
   consulta"; el colega que trabaja la Etapa 1 ya lo detectó y es su pase. **§17.3 = 3 sitios**
   (`deberá`), a resolver cuando se abra la v1.5. **§17.4 y §17.5 = 0** (verificado): ya están
   escritas en la voz correcta, y por eso el desfase se nota al leer el capítulo completo.
   La excepción de la regla vale igual en todas: no convertir en "se define más adelante" lo que
   nunca se ejerció.
3. **Equipo**: al integrar al maestro, **mudar los Anexos C y D del final del documento a
   §19.3/§19.4** (el contenido ya queda final por E2-49; sólo cambia de lugar y recibe la
   numeración del maestro). D-E1-11/AAIP sigue abierta.
4. **Usuario**: resolver los 27 comentarios en Google Docs con el mapa §F, una vez aplicado el
   pase; nombrar la salida **v1.4** y archivar la v1.3.
5. **Derivados, tras aplicar** (misma rutina que el cierre del pase 2): re-extraer `90f` de la
   v1.4 · regenerar el kit y actualizar en el generador (a) los conteos del texto base y (b) las
   menciones del estado vigente a la **numeración vieja de tablas** ("Tabla 28 de §17.1" → 26;
   "Tabla 26 de §17.1" → 24) · actualizar la lista de `.docx` vigentes en
   `INSTRUCCIONES-PROJECT.md` (hoy dice "§17.1 v1.3") · escribir el resumen del pase en
   `resumen-cambios-etapa-2.md` o su hermano.
