# Etapa 2 — resumen de los ajustes: del documento inicial al final

- **Comparación:** `17.1.docx` (inicial, 2026-08-28 02:48 — renombrado a
  `…Seccion_17.1_Consolidacion_Metodologica_v1.0.docx`) →
  `E-OVRT-VDP_Seccion_17.1_Consolidacion_Metodologica_v1.3.docx` (final, misma jornada).
- **Qué era el inicial:** el §17.1 del informe **v1.1 tal cual**, sin ninguna corrección aplicada.
  Verificado antes de empezar: 664 párrafos idénticos a la foto `96b`, cero `AJ-2.xx` aplicados,
  sin comentarios ni cambios controlados.
- **Recorrido:** un pase de contenido ([`correcciones-etapa-2.md`](desarrollando/archivado/correcciones-etapa-2.md),
  unidades **E2-01…E2-26** y decisiones **D-E2-1…9**) más el pase de formato F1–F6, que ChatGPT
  aplicó en una sola entrega (v1.2); y una verificación de cierre
  ([`correcciones-etapa-2-pase-2.md`](desarrollando/archivado/correcciones-etapa-2-pase-2.md)) que
  reparó tres defectos de forma sobre el XML y produjo la v1.3.
- **Lo que gobernó el pase:** §17.1 es **el protocolo**. Entran decisiones, definiciones y criterios;
  **no entran resultados medidos** (regla de no-anacronismo). Lo que el protocolo prescribió y no se
  ejerció **no se borra**: queda escrito, y §17.5 reporta que no se ejerció.
- ✎ **2026-08-31 — existe un PASE 3 (NO aplicado):**
  [`desarrollando/correcciones-etapa-2-pase-3.md`](desarrollando/correcciones-etapa-2-pase-3.md)
  (E2-30…E2-50, D-P3-1…9), disparado por la revisión crítica del usuario sobre la v1.3 (27
  comentarios). Desduplicación (guardrail 2 enmendado por D-P3-1), Tablas 17/22 fuera con
  renumeración 16–36 (verificado: cero refs numéricas aguas abajo — supera al "sin renumerar" del
  §1 de este resumen), anexos C/D → `90g`, y defectos verificados en el XML. La salida será la
  **v1.4**; este resumen documenta v1.0→v1.3 y no se reescribe.
  **✅ mismo día: APLICADO — la v1.4 es la vigente** (28.730 palabras con los Anexos C y D al
  final · 109 títulos · 21 tablas 16–36 · 78 ecuaciones · verificación de §G completa, un defecto
  E2-50.12 reparado sobre el XML). Acta en el banner del pase
  ([`archivado/correcciones-etapa-2-pase-3.md`](desarrollando/archivado/correcciones-etapa-2-pase-3.md));
  v1.0→v1.4 completo = este resumen + esa acta.

---

## 1. La cifra global

| | Inicial (v1.0) | Final (v1.3) | Cambio |
|---|---:|---:|---:|
| Palabras | 32.669 | **28.534** | **−12,7 %** |
| Párrafos | 667 | 629 | −38 |
| Títulos numerados | 122 | 118 | −4 |
| Tablas | 23 (16–38) | 23 (16–38) | **sin renumerar** |
| Ecuaciones de Word | 85 | 85 | intactas |
| Marcadores `[[…]]` | 0 | 1 | el espejo de la AAIP |
| Citas bibliográficas | — | — | **13 bajas, 0 altas** |

**Movimiento real del texto:** 59 párrafos nuevos (1.948 palabras) · 97 eliminados (5.402) · 113
modificados, de los cuales 35 son sólo terminología. No es una compresión pareja: **se podó donde
sobraba y se agregó donde faltaba**.

| Rama | Inicial | Final | Qué pasó |
|---|---:|---:|---|
| §17.1.6.2 Datasets de gestión directa | 4.856 | **1.375** | **−72 %** — la poda grande (PODA-12) |
| §17.1.10 Proyección hacia instancias posteriores | 647 | **0** | eliminada; reemplazada por un párrafo puente (PODA-13) |
| §17.1.4 Entorno e infraestructura | 3.138 | 2.666 | −15 % — detalle al Anexo B (PODA-14) |
| §17.1.5 Condiciones, patrones y prompts | 9.317 | **9.483** | **+1,8 %** — sólo inserciones |
| §17.1.7 Framework de métricas | 6.514 | **6.792** | **+4,3 %** — sólo inserciones |

Las dos ramas que crecen son exactamente las dos que los guardrails protegen: el protocolo que sí se
ejerció y el framework de métricas del que cuelga todo §17.5.

---

## 2. Los cinco tipos de ajuste

### A. Alinear el protocolo con lo que efectivamente se decidió

No con lo que se midió — eso es §17.4/§17.5. Entran decisiones de entorno y de configuración.

| Antes | Después |
|---|---|
| *"Windows 11 como SO base del CPN… las versiones de CUDA, cuDNN, TensorRT deben ser compatibles con Windows"* | *"Linux mediante WSL2 y contenedores Linux en el CPN… deben ser compatibles con el entorno Linux adoptado y quedar congeladas por corrida"* (4 menciones a Windows → **0**) |
| §17.1.4.2.4 *"Plan de contingencia para el EN"*: la OAK-D como *"candidata preferente"* y la cámara IP como contingencia ante *"limitaciones técnicas no previstas"* | Reescrito en **§17.1.4.2.3**: **dos fuentes integrables**, la vía RTSP priorizada por disponibilidad e interoperabilidad y la OAK-D incorporada después. ✎ **2026-08-30: §17.1.4.2.4 ELIMINADA.** El pase 2 la había dejado como *"Criterio de prioridad y fuente RTSP sintética"* con la fuente sintética declarada herramienta de desarrollo; se borró entera por **vestigial** — su "criterio de prioridad" ya estaba completo en §17.1.4.2.3, no tenía referencias cruzadas desde §17.3/§17.4/§17.5, y el párrafo presentaba una herramienta sólo para aclarar que no contaba. `§17.1.4.2.5 Stack de software` pasa a `.2.4`. Motivos completos: nota en **AJ-2.10** (`ajustes/02`) |
| §17.1.4.5.1: parámetros de referencia con una resolución única | *"La resolución de inferencia es un parámetro del perfil de modelo y debe fijarse junto con los umbrales recalibrados para ese perfil"* |
| §17.1.5.3.3: sólo los rangos de la Tabla 24 (3–5 s / 5–10 s) | + *"Como valores de protocolo dentro de esos rangos se fijan **4.000 ms** para PR-01 y **7.000 ms** para PR-02, con umbrales de desactivación de 2.000 y 3.000 ms"* — **la Tabla 24 no se tocó** y no aparece la palabra "efectivos" (esa casa es §17.4) |
| §17.1.9.2: la rama de ajuste fino sin encuadre de ejecución | + *"jornada experimental completa con criterios prerregistrados: una única baseline, márgenes fijados antes de evaluar… Sus condiciones de habilitación son **de datos y de protocolo, no de disponibilidad de cómputo**"*. "Presupuesto de tiempo", "cronograma" y "plazo": **0 apariciones** |

### B. Poner nombre a lo que el protocolo usaba sin definir

Lo que §17.3, §17.4 y §17.5 ya necesitaban y no tenían de dónde colgar.

- **Los códigos de estrategia nacen acá.** §17.1.5.4.2 bautiza **E-DIR** (directa), **E-IND**
  (indirecta) y **E-HYB** (híbrida). Antes aparecían **cero veces** en todo el informe fuera de
  §17.3/§17.4/§17.5, que los usaban como si estuvieran definidos. *(Consecuencia: §17.3.6.4 debe
  recortar su glosa a una remisión — ver §5.)*
- **El nivel intermedio de análisis.** §17.1.7.3.1 abre declarando **tres niveles**: percepción por
  imagen · **estado observable por persona** · alerta temporal por episodio. §17.5 organiza sus
  resultados con ese eje y el protocolo no lo pre-registraba.
- **La regla de conteo que protege toda la precisión reportada.** §17.1.7.8.3: *"Una re-alerta o
  reconfirmación asociada al mismo episodio **no se computa como falso positivo**; se registra y se
  reporta por separado"*.
- **Las reglas de lectura, como criterio pre-registrado:** reportar por estrato y escenario y nunca
  sólo el agregado · los materiales sin la condición objetivo no entran en precision/recall/F1 (su
  métrica es el conteo de falsos positivos) · la SDR sólo se compara entre corridas de la misma
  cadencia · la latencia de alerta no se compara entre densidades sin controlar qué episodios siguen
  siendo evaluables.
- **Estados de aplicabilidad** (§17.1.7.8.2): *"Una métrica que no corresponde medir se reporta con
  su estado y su causa… **nunca como cero ni por omisión**"*.
- **La vía de escape del piso muestral** (§17.1.5.4.5): cuando una condición no llegue a ~200
  positivos, *"reportar el n efectivo con intervalos de confianza al 95 % obtenidos por **bootstrap**…
  y abstenerse de ordenar variantes cuyos intervalos se superpongan"*.
- **Cuándo la doble anotación no aplica:** *"cuando la referencia se reutilice de anotaciones de
  fuente sin reanotación, la doble anotación no aplica y la ausencia de una medida de acuerdo debe
  declararse como limitación del material"*. El requisito de ≥20 % + kappa **se conserva**.
- **El catálogo de prompts tiene fuente:** el conjunto se construye desde el **Anexo C (Tabla C.1)**
  y las formulaciones finalistas se congelan **con acta previa** a la evaluación.

### C. Lo que era falso, ambiguo o quedaba colgado

| Dónde | Qué pasaba | Cómo quedó |
|---|---|---|
| §17.1.6.1.1 | Remitía a *"la sección **16.7.6**"*, que tras el cierre de la Etapa 1 ya no existe | *"la sección **16.7.3**"* (las seis preguntas rectoras que §17.1 invoca son exactamente las que sobrevivieron) |
| §17.1.5.3.4 | *"…evita alertas repetidas sobre una misma situación"* — falso en cuanto la condición reaparece | *"…dentro de un mismo episodio; la reaparición de la condición después de su resolución **constituye un episodio nuevo**, y la eventual supresión de notificaciones repetidas se define **fuera del motor de patrones**"* |
| §17.1.6.4.1 | Licencias afirmadas sin verificar (Apache-2.0, MIT) y la del *paper* de CHV atribuida al dataset | Licencias como figuran en el registro; **CHV "sin licencia formal; cita obligatoria"**; *"la licencia del artículo asociado no se transfiere por inferencia al dataset"* |
| §17.1.10.1 | El marcador de la AAIP quedó bajo un párrafo que no menciona ninguna inscripción: *"esta inscripción"* sin antecedente | Frase de anclaje antes del marcador (**E2-28**). El `[[PENDIENTE]]` **no se tocó**: es decisión del equipo y viaja |
| §17.1.9.2 | El párrafo puente de la poda cayó dentro de *Candidatos de comparación*, fuera de tema | Movido a §17.1.11.2 *Articulación con las instancias de diseño e implementación* (**E2-29**) |

### D. Poda por aporte

- **PODA-12 — el catálogo de datasets (−3.481 palabras, el 84 % de la poda total).** Eran nueve
  fichas largas escritas antes de que la selección se cerrara, con licencias sin verificar y con
  estimaciones de horas-persona de anotación que nunca se usaron. Quedó: **cuatro fuentes retenidas**
  con ficha breve (Tabla 26, retitulada *"Datasets retenidos como candidatos de gestión directa"*) y
  una **tabla de descartados con la causa en una línea** (Tabla 27, antes *"Mapeo de condiciones de
  riesgo a datasets candidatos"*). Menciones: MOCS 14 → 1 · SODA 15 → 1 · Pictor-PPE 12 → 1 ·
  SH17 9 → 1 · GDUT-HWD 8 → 1 · SHWD 8 → 1. Entran al inventario `construction site safety` y
  `ppe siabar` (0 → 5 menciones cada uno), que el protocolo original no listaba.
  **Nota que se agregó y que importa:** *"la retención expresa aptitud metodológica como candidato y
  no asignación efectiva… sin solapamiento entre material de ajuste y estratos de evaluación"*, y
  *"una misma fuente no puede utilizarse simultáneamente como material de entrenamiento y como
  estrato del banco de evaluación"*.
- **PODA-13 — la proyección hacia instancias posteriores (−647).** Las "instancias posteriores" ya
  ocurrieron: cuatro subsecciones de anticipación se comprimieron a **un párrafo** que dice qué toma
  cada una. Renumeración: §17.1.11 → **§17.1.10** y §17.1.12 → **§17.1.11**.
- **PODA-14 — infraestructura al Anexo B (−472).** El detalle de hardware y stack se reemplazó por
  remisiones; se verificó una por una que lo removido esté en **B.1–B.7** (CPN · EN/OAK-D · stack CPN
  · TN · stack TN · parámetros · topología). Es la única poda que quedó por debajo de lo estimado
  (~1.000): no se forzó, porque el guardrail es no recortar por cuota.

### E. Formato y terminología

- **F1** los 118 títulos pasaron de Title Case a tipo frase (*"Función y Alcance de la Consolidación
  Metodológica"* → *"Función y alcance…"*).
- **F5** terminología unificada con §15–§16 y §17.5: `cuadro` 4 → **44** · `fotograma` 9 → **0** ·
  `frame` 76 → 37 (queda sólo dentro de *framework*) · `tracking` 15 → **3** (sólo
  `tracking-by-detection`, `TrackingNet` y *Multiple Object Tracking*) · `end-to-end`/`E2E` 1 → **0**
  · `intra-frame` → `intracuadro`.
- **F2/F3 (E2-27, reparado en la v1.3).** La entrega trajo los 23 rótulos de tabla y las 21 notas en
  **negrita + itálica**; la convención de la casa —ya aplicada en §15–§16 y §17.5— es `**Tabla N**`
  en negrita y `*Nota.*` en itálica. Corregido sobre el XML: 23 + 21.

---

## 3. Lo que NO se tocó, y por qué

1. **§17.1.5 y §17.1.7 no se comprimieron.** Son el protocolo que sí se ejerció y el framework del
   que cuelga §17.5; el guardrail lo prohíbe y de hecho **crecieron**.
2. **MOT17/OVT-B (§17.1.6.3) y las métricas MOT (§17.1.7.4.2), intactos.** Están pre-registrados y no
   se ejercieron; el texto ya estaba en condicional. Lo no ejercido lo reporta §17.5, no se borra de
   donde se prometió.
3. **Tablas 24 (patrones), 28 (partición), 36 (fases) y 37 (regla de ajuste fino): filas idénticas.**
   La 28 conserva su rango de 500–2.000 imágenes de entrenamiento **a propósito**: la desviación real
   se declara en §17.4/§17.5, no se reescribe la regla para que encaje.
4. **Las 85 ecuaciones de Word.** Los nombres de métrica que se ven vacíos en cualquier extracción
   plana son objetos de ecuación, no erratas.
5. **La numeración de tablas.** 23 antes y 23 después, mismos números: nada aguas abajo se rompe.
6. **CPN/EN/TN y las siglas `t_alert-system` / TTFD / SDR.** Nacen acá y §17.3/§17.4 las usan sin
   redefinir; no se renombraron ni se movieron.

---

## 4. Delta de referencias — 13 bajas, 0 altas

Dejaron de citarse en §17.1 al caer el catálogo largo: **Ahmad y Rahimi, 2025** (SH17) · **An et al.,
2021** (MOCS) · **Buslaev et al., 2020** (Albumentations) · **Dalvi et al., 2025** (Construction-PPE)
· **Duan et al., 2022** (SODA) · **Ley 25.326, 2000** (sigue citada como *Argentina, 2000*) · **Long y
Li, 2023** · **Mallick, 2025** · **NJVisionPower, 2019** (SHWD) · **Nath et al., 2020** y **CIBER Lab,
2020** (Pictor-PPE) · **Wu et al., 2019** (GDUT-HWD).

> ⚠️ **Antes de sacarlas del listado global hay que confirmar que ninguna otra sección las cite.** El
> listado de Referencias es del informe completo, no de §17.1.

---

## 5. Lo que queda abierto — y no es redacción de esta sección

| Qué | Dónde |
|---|---|
| **Anexos C y D corregidos** (`90g`): candidatos vs retenidos, `bench_obra` no es un dataset, Tabla C.1 como fuente del prompt set, tabla de umbrales del Anexo D reducida a lo que agrega + remisión a la Tabla 35 | ✎ 2026-08-31: **ESCRITO Y LISTO PARA PEGAR** — [`90g-etapa2-anexos-c-y-d.md`](90g-etapa2-anexos-c-y-d.md) (C: 5→3 · D: 6→3; la ex-D.4 se **elimina**, refinando D-E2-1). Por **D-P3-8** los anexos van **al final del documento de la etapa** (unidad E2-49 del pase 3, aplicada por ChatGPT); al integrar, el equipo los muda a §19.3/§19.4. Las remisiones del cuerpo las actualiza E2-47 |
| **§17.3 v1.4 → v1.5:** recortar la glosa de §17.3.6.4 a una remisión, ahora que los códigos nacen en §17.1.5.4.2 | handoff a la Etapa 3 |
| **§17.4:** orden de disparo real (control → distribución → medios) y la desviación del rango 500–2.000 → 2.946 imágenes, con su causa | handoff a la Etapa 4 |
| **§17.5:** declarar lo no ejercido (variantes con template, vocabulario aislado-vs-completo cruzado, español, kappa/L2, MOT, confianza media de los TP), citar `n = 5.313` fechado y el caveat del umbral 800/560 | handoff a la Etapa 5 |
| **D-E1-11 — AAIP:** decisión del equipo; el marcador viaja en §16.6.2.2 y §17.1.10.1 | equipo |
| **Residuales de forma, para la integración final:** `t_alert-system` escrito como texto en §17.1.7.2 mientras el resto del capítulo usa el objeto de ecuación; *"Versión registrada"* en dos celdas de la Tabla 26; nombres de dataset con espacios vs. identificadores | pase de integración |

---

## 6. Cómo se verificó

- **Diff párrafo a párrafo** de la extracción v1.0 contra la v1.3, normalizando markdown y ecuaciones:
  cada uno de los 269 bloques que cambiaron se clasificó (nuevo / eliminado / modificado / sólo
  terminología) y se contrastó contra la unidad E2 que lo pedía.
- **Unidad por unidad:** las 26 unidades E2 quedaron ✅ aplicadas o ⊘ resueltas como "no se aplica",
  con la evidencia textual anotada en `correcciones-etapa-2-pase-2.md` §2.
- **Verificador mecánico:** `verificar_entregable.py --seccion 17.1` → **OK**, sin problemas duros.
- **Contra la implementación**, no contra documentos: los hechos que el pase usó (persistencias del
  conjunto de patrones, entorno real de ejecución, fuentes de ingesta integradas, composición del
  entrenamiento) salieron del relevamiento de los cinco repositorios del 2026-08-28.
- **Higiene del informe:** cero identificadores internos, cero rutas, cero cifras propias, un solo
  marcador, sin runs de formato partiendo palabras.
