# Análisis exhaustivo de §17.3 Diseño Arquitectónico (v1.5) — para el pase de consolidación de la Etapa 3

> **Estatuto.** Diagnóstico previo a la escritura, mismo formato que el que cerró la Etapa 2
> (`archivado/analisis-17-1-8-anexos.md`). No modifica el `.docx`. La vara es **§17.1 v1.15**
> (último documento cerrado) y, para la voz, **§17.5 v1.3**. Fecha: 2026-09-03.
>
> **Insumos medidos:** `desarrollando/E-OVRT-VDP_Seccion_17.3_Diseno_Arquitectonico_v1.5.docx`
> (vista aceptada, extraída fresca); `90f` (§17.1 v1.15), `90g` (Anexos C/D), `90d` (§15/16 v1.1),
> `90b` (§17.4 v1.6), `90c` (§17.5 v1.3); actas `archivado/correcciones-etapa-3-4*.md`;
> `00-lo-que-resta.md` §3.2. Script y salidas crudas en el scratchpad de la sesión
> (`analisis_173.py`, `analisis_173.md`, `texto_173.md`).

---

## 0. Veredicto en seis líneas

1. **La v1.5 es byte a byte la v1.4** (sha256 `6905b2a0…` idéntico). El handoff registrado en
   `00-lo-que-resta.md` §3.2 —E3-42 (recorte de la glosa E-DIR/E-IND/E-HYB), 3 sitios de voz D-P3-9,
   11 metadiscursos, 2 párrafos gordos— **sigue sin aplicar**. Este pase lo absorbe.
2. **El capítulo pesa 17.857 palabras** (13.031 de prosa + 4.826 en 17 tablas) repartidas en **61 títulos**
   (18 de nivel 3, 39 de nivel 4, **4 de nivel 5**). §17.1 v1.15, más largo en alcance, quedó en 35 títulos
   para 11.153 palabras de prosa. §17.3 tiene **214 palabras por título contra 319**: está
   sobre-estructurado, no sobre-argumentado.
3. **La grasa es de repetición, no de ideas.** Detecté **14 ideas que aparecen entre 3 y 13 veces** dentro
   del capítulo (§3) y **9 bloques que re-argumentan lo que §17.1 v1.15 ya fijó** con las mismas citas
   (§4). Los dos colegas lo marcaron en los comentarios ("muy repetitivo", "lo dijimos arriba").
4. **Puntuación:** 72 dos puntos y 86 puntos y coma en prosa (5,5 y 6,6 por mil palabras). §17.1 v1.15
   quedó en 0,4 y 2,4. Además 32 rayas, 87 "debe/deben" (6,7 por mil; §17.1 3,6; §17.5 0,8) y siete
   párrafos del tipo "El primero es… El segundo es…".
5. **Lo que no se toca es poco y está claro** (§6): las cinco tablas que son interfaz con §17.4 (39, 41, 46,
   54, 55), la definición de patrón, la máquina de cinco estados, fail-open, persistir-primero, los
   invariantes de referencia temporal y la regla del cero silencioso.
6. **Objetivo razonable:** 13.031 → ~8.800 palabras de prosa (−32 %), 61 → ~28 títulos, cero nivel 5,
   17 → 14–15 tablas, dos puntos ≤ 15 y punto y coma ≤ 20 en prosa, cero metadiscurso, cero "deberá".
   **Habilitante verificado:** ninguna otra sección del informe cita subsecciones ni tablas de §17.3 por
   número (cero apariciones en §15/16, §17.1, §17.4 y §17.5), así que renumerar por dentro es gratis.

---

## 1. Estado del artefacto

| Ítem | Estado |
|---|---|
| Archivo | `E-OVRT-VDP_Seccion_17.3_Diseno_Arquitectonico_v1.5.docx` (5.895.406 bytes, 2026-09-03 03:51) |
| Igual a v1.4 | **Sí**, sha256 idéntico. Los 61 títulos coinciden con la extracción `90` (v1.4, 08-23) |
| Cambios controlados | 0 inserciones, 0 borrados |
| Comentarios | **7** (3 del colega G. G., 4 del usuario), ver §1.1 |
| Tablas | 17, numeradas **39–55** contiguas. **11 no se citan en prosa por número** (40, 44, 46, 47, 48, 49, 50, 52, 53, 54, 55): se introducen por adyacencia. La regla de §17.1 (E2-47, cada tabla citada exactamente una vez) no se cumple |
| Figuras | 6 embebidas (PNG 1.400–2.000 px), numeradas **Figura 4.1–4.6** (esquema del capítulo standalone, no global). **Ninguna se cita en prosa por número.** Ver §1.2 |
| Ecuaciones | 0 |
| Estilos | Heading3/4/5 (17.3 = H2 implícito por la numeración escrita) |
| Autocontención | **Limpia**: 0 menciones a ADR, rutas, códigos E-/R-/AJ-/F- |
| Anacronismos | **Limpio**: ninguna cifra de verificación (el único hit del patrón es "F1", nombre de métrica) |
| Remisiones | `sección 17.1.4.4` (en 17.3.14) **no existe en §17.1 v1.15**: los escenarios están en **17.1.4.2** (y 17.1.3.3 con el mismo título). `17.4.6` (×2) y `17.3.11`, `17.3.8.3.1`, `17.3.8.3.2` existen |
| Erratas | Título "17.3.10.2. …control de ciclo de vida**.**" (punto final); "reconstuir" en la viñeta 7 de 17.3.8.3.1; "vídeo"/"video" mezclados a lo largo del capítulo |

### 1.1 Los siete comentarios (se informan, no se tocan — el usuario decide cuándo)

| id | Autor · fecha | Ancla | Texto | Lectura para este pase |
|---|---|---|---|---|
| 0 | G. G. · 08-26 | 17.3.1 párr. 2 (los dos planos) | Propone reemplazar el párrafo por una oración que remite a "Secciones 16.5.3.1 y 16.7.5" para acortar y evitar redundancia | **Correcto en el fondo**: los dos planos ya están fundamentados en la Etapa 1. **Los números están vencidos**: en §16 v1.1 el tema vive en **16.5.3** "Separación de planos y flujo productor-consumidor" y las preguntas rectoras en **16.7.3**; 16.5.3.1 y 16.7.5 no existen |
| 1 | G. G. · 08-26 | 17.3.2 párr. 1 | "todo esto me parece al re pedo, lo dijimos arriba" | Coincide con el diagnóstico de §2.2: 17.3.2 es un índice razonado que anticipa todo el capítulo |
| 2 | G. G. · 08-26 | 17.3.2 párr. 2 | "mucho texto al pedo tambien, es muy repetitivo todo esto" | Ídem |
| 3 | usuario · 08-24 | título 17.3.3.2 | "esta seccion se ajusto completa, asegurarse que las demas 17.3.3.x quedaron alineadas con esta" | Verificado: 17.3.3.1 y la prosa post-tabla de 17.3.3.4 repiten a la Tabla 39 en vez de alinearse con ella (§2.3). El pase lo resuelve fundiendo |
| 4 | usuario · 08-24 | Tabla 41, celda DA-03 (justificación, 70 w) | "mucho texto" | Acortar la celda a una oración (§2.3) |
| 5 | usuario · 08-24 | Tabla 41, celda DA-11 (decisión, 35 w) | "mucho texto" | Ídem: la decisión en una oración, el fail-open ya se define en 17.3.7.4 |
| 6 | usuario · 08-24 | 17.3.6.4 párr. 2 (glosa E-DIR/E-IND/E-HYB) | "revisar que este esto desarrolado en etapa2" | **Sí está**: §17.1.5.3 v1.15 bautiza los tres códigos y la Tabla C.1 del Anexo C trae el catálogo. Es exactamente E3-42/D-E2-2: la glosa baja a remisión |

Los siete quedan **resueltos de facto** si se aplica lo que sigue. Por la regla de casa, el cierre formal de
los comentarios lo indica el usuario.

### 1.2 Las seis figuras (vistas una por una)

| Figura | Sección | Contenido | Observación |
|---|---|---|---|
| 4.1 | 17.3.5 | Vista conceptual: fuentes → medios → bus → control → distribución → consumidores; configuración arriba, soporte abajo | **Ancla del capítulo.** Se queda. Su nota repite el párrafo 1 de 17.3.5 ("no representa distribución física obligatoria", dicho dos veces) |
| 4.2 | 17.3.7 | Flujo del plano de medios en 6 etapas | Buena. Trae rótulos de implementación en inglés ("RawFrame / VisualUnit", "backpressure") y una fuente "Sim: video sintético" que el texto no menciona. Revisar rótulos o declarar la fuente |
| 4.3 | 17.3.8 | Plano de control: evento de percepción → evaluación → estado → alerta interna | **Baja información** (tres cajas). Candidata a eliminar: la Figura 4.4 y la 4.5 ya muestran lo mismo con más contenido |
| 4.4 | 17.3.8.2 | Máquina de estados: inactive, candidate, confirmed, sustained, resolved; ventanas de confirmación y resolución; registro de alerta | Es la **FIG-E de diseño** (E3-08). **No es la FIG-E producida el 08-21** en `informe/figuras/` (PNG 300 dpi con la reapertura a `candidate` que su README advierte). La embebida no dibuja esa reapertura. Pendiente de pegado (integración), no de este pase |
| 4.5 | 17.3.9.1 | Cadena condición → estrategia → evidencia → patrón → alerta | Buena síntesis. Si 17.3.9 se funde (§5), migra con su texto |
| 4.6 | 17.3.15 | EN → CPN ← TN | **Trivial**: repite la Tabla 53. Candidata a eliminar |

Numeración global de figuras y pegado de FIG-E: trabajo de integración, fuera de este pase.

---

## 2. Medición

### 2.1 La vara

| Documento | Prosa (w) | Tablas (w) | Oraciones | w/oración | `:` prosa (‰) | `;` prosa (‰) | `—` | Metadiscurso | deberá/futuro | Párr. >150 w | Títulos (‰) | Nivel 5 |
|---|---:|---:|---:|---:|---|---|---:|---:|---:|---:|---|---:|
| **§17.3 v1.5** | **13.031** | **4.826** | 566 | 23,0 | **72 (5,5)** | **86 (6,6)** | **32** | **10** | **3** | 2 | **61 (4,7)** | **4** |
| §17.1 v1.15 | 11.153 | 4.336 | 453 | 24,6 | 5 (0,4) | 27 (2,4) | 6 | 3 | 4* | 13 | 35 (3,1) | 0 |
| §17.4 v1.6 | 5.238 | 1.776 | 166 | 31,6 | 105 (20,0) | 30 (5,7) | 28 | 1 | 0 | 9 | 16 (3,1) | 0 |
| §17.5 v1.3 | 2.539 | 1.009 | 112 | 22,7 | 15 (5,9) | 16 (6,3) | 0 | 1 | 0 | 0 | 9 (3,5) | 0 |
| §15/16 v1.1 | 19.280 | 2.722 | 660 | 29,2 | 102 (5,3) | 170 (8,8) | 70 | 19 | 13 | 4 | 92 (4,8) | 0 |

\* Los "deberá" de §17.1 son prescripción normativa del protocolo (no se tocan por D-P3-9). El conteo de metadiscurso usa
el patrón estricto ("esta sección", "el presente capítulo", "cabe destacar"…); la medición del pase 4 dio 11 con un
patrón más amplio. En las celdas de tabla hay además 60 `;` que son notación de listas y se toleran.

Voz, en prosa de §17.3 contra la vara: **debe/deben 87** (6,7 ‰; §17.1 3,6; §17.5 0,8) · **mediante 32** (2,5 ‰) ·
**"no X, sino Y" 14** · **"no constituye" 9** · **"El primero/segundo/… es" 7** · **"de modo que" 11** · **"por ello" 7** ·
"de este modo" 5 · "por lo tanto" 4 · "en consecuencia" 3.

### 2.2 Peso por sección (nivel 3, hijos incluidos)

| Sección | Prosa | Tablas | Títulos | `:` | `;` | Meta | Lectura |
|---|---:|---:|---:|---:|---:|---:|---|
| 17.3.1 Introducción | 259 | — | 1 | 2 | 1 | 1 | Dos párrafos dicen lo mismo; el de los dos planos repite §16.5.3 |
| 17.3.2 Insumos | 506 | — | 1 | 3 | 1 | 0 | **Índice razonado del capítulo**: cada párrafo se repite después en su sección |
| 17.3.3 Alcance, requisitos, DA | 964 | 1.373 | 5 | 4 | 7 | 0 | Tres tablas ancla + prosa que las parafrasea |
| 17.3.4 Principios | 201 | — | 1 | **5** | 0 | 0 | Cinco oraciones "El primero es X:" que reformulan las DA |
| 17.3.5 Vista general | 700 | — | 1 | 5 | 5 | 0 | Párrafo de **254 w** (patrones de acople) que luego se repite en 17.3.8.1, 17.3.8.4, 17.3.12.1, 17.3.18 |
| 17.3.6 Configuración y prompts | 1.467 | 805 | 6 | 6 | 8 | 2 | Intro + 17.3.6.1 + 17.3.6.2 dicen tres veces "la configuración gobierna"; 17.3.6.3 re-argumenta §17.1.5.3 con sus 5 citas |
| 17.3.7 Plano de medios | 1.969 | — | 5 | 7 | 9 | 1 | El flujo (17.3.7.1) es el núcleo; intro, criterios y control de ritmo lo parafrasean |
| 17.3.8 Plano de control | **2.619** | 457 | **9** | **10** | **23** | 1 | La más pesada y la única con nivel 5 (4 títulos para 1.229 w) |
| 17.3.9 Integración | 534 | — | 4 | 4 | 4 | 1 | Tres hijos de 200/155/94 w; la estrategia E-IND ya se decide en 17.3.6.4 |
| 17.3.10 Distribución | 735 | 153 | 4 | 8 | 2 | 1 | 17.3.10.3 (346 w) es detalle de implementación del ledger |
| 17.3.11 Contratos | 566 | 274 | 4 | 8 | 2 | 0 | 17.3.11.1 recapitula fronteras ya explicadas |
| 17.3.12 Trazabilidad | 704 | 251 | 4 | 2 | 4 | 1 | Tabla 47 solapa con Tabla 46; minimización dicha por 5.ª vez |
| 17.3.13 Observabilidad | 316 | 545 | 5 | 0 | 4 | 0 | **5 títulos para 316 w**; Tabla 49 duplica §17.1.7.3/17.1.7.5 |
| 17.3.14 DBE/EBE | 795 | 418 | 7 | 2 | 9 | 0 | **7 títulos**, dos hijos de 54 y 56 w; Tabla 51 duplica la Tabla 17 de §17.1 |
| 17.3.15 Roles | 198 | 166 | 1 | 3 | 0 | 1 | Repite §17.1.4.1 y una oración literal de 17.3.10.1 |
| 17.3.16 Riesgos | 64 | 224 | 1 | 1 | 1 | 0 | Tabla que recapitula reglas ya escritas; se queda por R-20 |
| 17.3.17 Plan | 173 | 160 | 1 | 0 | 1 | 1 | Bien; las tres clases de extensión se repiten en 17.3.18 |
| 17.3.18 Cierre | 261 | — | 1 | 2 | 5 | 0 | Resumen que repite literalmente 17.3.5 y 17.3.17 |

Estructura: **contenedores casi vacíos** 17.3.10 (38 w) y 17.3.14 (18 w); **subsecciones de nivel ≥ 4 con
menos de 120 palabras**: 17.3.3.3, 17.3.9.3, 17.3.11.3, 17.3.13.1 (29 w), 17.3.13.2, 17.3.13.3, 17.3.13.4,
17.3.14.1, 17.3.14.2. Cada una es un párrafo con título.

---

## 3. Mapa de repeticiones dentro del capítulo (idea → dónde aparece → casa propuesta)

El detector de oraciones casi iguales dio 16 pares (dos literales: "La configuración de corrida parametriza la
ejecución/evaluación como entrada transversal" en las notas de las Figuras 4.2 y 4.3; "no constituye un tercer plano
ni un cuarto rol funcional" en 17.3.10.1 y 17.3.15). Lo grave no son las oraciones sino las **ideas** que se
re-explican con palabras distintas. Las catorce, ordenadas por cantidad de apariciones:

| # | Idea | Apariciones (sección o tabla) | Casa propuesta |
|---|---|---|---|
| 1 | Núcleo = CR-01/CR-02 con E-IND; las extensiones se declaran y no desplazan el flujo base | 17.3.2 · 17.3.3.1 · Tabla 39 (+nota) · 17.3.4 · 17.3.6.4 · 17.3.7.4 · 17.3.8 intro · 17.3.8.3 · 17.3.8.3.3 · 17.3.9.2 · nota T47 · nota T55 · Tabla 54 · 17.3.18 (**13**) | 17.3.3 (alcance) y 17.3.6.4 (estrategia). En el resto, una mención sin re-explicar |
| 2 | Descartes, huecos y pérdida de identidad no son ausencia de evidencia | 17.3.7.1 · 17.3.7.2 · 17.3.8.3.2 · 17.3.8.3.4 · 17.3.8.4 · 17.3.12.2 (×2) · Tabla 50 · Tabla 52 · 17.3.14.6 · Tabla 54 (**10**) | 17.3.13 (observabilidad) + 17.3.14.6 (cero silencioso) |
| 3 | Identidad temporal opcional; excluir métricas MOT no excluye la capacidad | 17.3.2 · Tabla 39 · DA-06 · 17.3.7.4 · 17.3.8 intro · 17.3.8.3.2 · 17.3.11.3 · Tabla 54 · 17.3.18 (**9**) | DA-06 + 17.3.8.3 (granularidad) |
| 4 | Dos planos y ruta crítica protegida de la interpretación | 17.3.1 · 17.3.2 · DA-01 · 17.3.4 · 17.3.5 · 17.3.7 intro · 17.3.8 intro · 17.3.18 (**8**) | DA-01 + 17.3.5. La fundamentación es de §16.5.3 (Etapa 1) |
| 5 | Configuración como entrada transversal que gobierna sin latencia; nada opcional es implícito | 17.3.5 · 17.3.6 intro · 17.3.6.1 · 17.3.6.5 · 17.3.7 intro · nota Fig. 4.2 · nota Fig. 4.3 · nota T39 · Tabla 42 (**9**) | 17.3.6 (una vez, en su intro) |
| 6 | Detección ≠ patrón ≠ alerta; la alerta no es certificación normativa | 17.3.8 intro · 17.3.8.2 · 17.3.8.3 · 17.3.9 intro · 17.3.9.1 · 17.3.12.3 · Tabla 39 (**7**) | Ya lo fija §17.1.3.1–17.1.3.2. En §17.3: 17.3.8 intro (una vez) y 17.3.12.3 (carácter asistivo) |
| 7 | HTTP gobierna, el bus transporta, JSONL persiste primero | 17.3.5 · 17.3.8.1 · 17.3.8.4 · 17.3.10.2 · 17.3.12.1 · Tabla 54 · 17.3.18 (**7**) | 17.3.5 (los dos patrones de acople) + 17.3.8.4 (mecánica: seq, ciclo de vida) |
| 8 | Minimización visual, sin identidad personal, artefactos visuales sólo justificados | 17.3.2 · 17.3.3.1 · DA-08/09 + glosa · Tabla 40 · 17.3.12.3 · Tabla 47 · Tabla 54 (**7**) | 17.3.12.3 (§17.1.10 es la base normativa) |
| 9 | fail-open del preselector | 17.3.7.4 (definición) · Tabla 39 · DA-11 · 17.3.14.5 · Tabla 52 · Tabla 53 · Tabla 54 (**7**) | Definición sólo en 17.3.7.4; las tablas nombran "fail-open" sin re-explicar |
| 10 | La ausencia de EPP se infiere en el control, no se consulta como negación opaca | 17.3.6.4 (prosa + 2 celdas T43) · Tabla 44 (×2) · viñeta 17.3.8.3.1 · 17.3.9.2 · 17.3.18 (**7**) | 17.3.6.4 |
| 11 | DBE/EBE no son topologías; la distribución física no es compromiso; fronteras lógicas | 17.3.3.4 · 17.3.5 (×2) · 17.3.11.1 · nota T52 · 17.3.15 (**6**) | 17.3.15 (topología de referencia) |
| 12 | Cooldown y supresión viven en distribución, no en el motor | Tabla 42 (×2 en la misma tabla) · DA-13 + glosa · 17.3.10.3 · Tabla 54 (**5**) | DA-13 + 17.3.10 |
| 13 | Ventanas en milisegundos, no en cuadros | 17.3.8.2 · 17.3.8.3.1 · Tabla 55 (+ §17.1.5.2) (**3**) | 17.3.8.2 |
| 14 | Tres clases de extensión (configuración / evaluador / adaptador) | 17.3.17 · 17.3.18 (**2**, literal) | 17.3.17 |

---

## 4. Coherencia con las Etapas 1 y 2 (lo que §17.3 re-argumenta y debería remitir)

Con §17.1 v1.15 cerrada, varios bloques de §17.3 quedaron **duplicando la casa metodológica**. El criterio del
pase 6 de la Etapa 2 (una idea vive en una casa; el resto remite) manda acá también.

| Bloque de §17.3 | Lo que ya establece la Etapa 1/2 | Acción |
|---|---|---|
| 17.3.6.3 párr. 1–2: sensibilidad al prompt (Du et al., 2022; Zhou et al., 2022) y prompts en inglés por CLIP/CC/CC12M (Changpinyo et al., 2021; Radford et al., 2021; Sharma et al., 2018) | **§17.1.5.3** lo argumenta con **las mismas cinco citas** (eco de 9 y 4 4-gramas) | Una oración con remisión. Las cinco citas salen de §17.3 (la lista global no cambia: §17.1 las conserva) |
| 17.3.6.4 párr. 2, glosa de E-DIR/E-IND/E-HYB (~70 w) | **§17.1.5.3** bautiza los tres códigos (D-E2-2 aplicada en v1.15) | **E3-42 / dependencia inversa**: la glosa baja a la remisión prevista en el pase 3 ("…para las estrategias directa (E-DIR) e híbrida (E-HYB) definidas en la consolidación metodológica"). Resuelve el comentario 6 |
| Tabla 43, filas CR-03…CR-06 (10 de 14 filas, 414 w) | **Tabla C.1 del Anexo C** trae el catálogo completo (dos celdas idénticas, ratio 1,00) | Ver D-C: reducir al núcleo y las ramas comparativas, remitir al Anexo C |
| 17.3.8.3.1 viñetas "Regla temporal e histéresis" y "Severidad"; Tabla 44 filas PR-03…PR-06 | **§17.1.5.2** fija severidad, ventanas, histéresis, ms, valores de protocolo (4.000/7.000 ms) y la **Tabla 21** con el catálogo PR-01…06 y criterios de activación de PR-05/06 | §17.3 conserva lo arquitectónico (qué campos declara un patrón, dependencias por nivel) y remite para los valores y la severidad. Ver D-D |
| 17.3.8 intro, 17.3.8.3 párr. 2, 17.3.8.3.4 último párr., 17.3.9 | **§17.1.3.1–17.1.3.2 y Tabla 16**: unidad de análisis, cadena operativa mínima, motor de patrones, carácter asistivo | Una sola formulación en 17.3.8 intro; el resto remite o desaparece |
| 17.3.15 + Tabla 53 + 17.3.14.5 (RTSP, OAK-D, Mendieta) | **§17.1.4.1** define CPN/EN/TN, sus equipos y el cluster | §17.3 sólo agrega la topología de referencia y el módulo de distribución (lo dice el propio texto). Tabla 53 se queda; prosa a la mitad |
| 17.3.14 + Tabla 51 | **§17.1.4.2 y Tabla 17** comparan DBE/EBE (entrada, propósito, distribución funcional, variables, limitación) | Corregir la remisión rota (17.1.4.4 → 17.1.4.2). Ver D-G sobre la Tabla 51 |
| Tabla 49 "Diccionario de métricas" + 17.3.13.2 prosa + 17.3.8.3.4 párr. 3 + "cinco hitos" de 17.3.11.2 | **§17.1.7.3, 17.1.7.5, Tabla 29 y Anexo D** definen t_alert-system, TTFD, SDR, capture_to_host, G2A, relojes y **§17.1.7.6 ya enumera los hitos** | Lo propio de §17.3 son los **cuatro estados de aplicabilidad literales** (computed, applicable_not_computed, not_applicable, not_interpretable: cero apariciones en §17.1) y la materialización por tramo (Tabla 48). Ver D-F |
| 17.3.12.3 | **§17.1.10** fija salvaguardas y carácter asistivo | Se queda como casa arquitectónica de la minimización; sus otras cuatro apariciones en §17.3 caen |
| Tabla 54, filas "Extensiones desplazan el núcleo" y "Preselección…" | **Tabla 35 de §17.1** trae dos riesgos equivalentes | Aceptable: la Tabla 54 es la interfaz de verificación con §17.4/§17.5 (R-20) |
| 17.3.1 párr. 2 y 17.3.2 párr. 2 (dos planos, productor-consumidor, borde) | **§16.5.3 y §16.5.4** (Etapa 1) | Oración con remisión a 16.5.3 (comentario 0, con los números corregidos) |

Terminología cruzada, para la integración y no para este pase: §17.3 usa "evento de percepción" (término
firmado en el pase 1 de la Etapa 3); la Tabla 16 de §17.1 v1.15 todavía dice "evento de detección".

---

## 5. Diagnóstico y propuesta por sección

Convención: **w** = palabras de prosa propias. "Casa" = dónde queda la idea. Objetivos indicativos.

### 17.3.1 Introducción (259 w) → ~120 w
Párrafos 1 y 3 dicen lo mismo (propósito, "transformar definiciones en organización técnica" /
"consolidar una base arquitectónica"). Párrafo 2 (dos planos) es Etapa 1: una oración con remisión a §16.5.3
(comentario 0). La pregunta rectora del párrafo 4 se conserva. "El presente capítulo desarrolla…" → voz de
sistema. "deberán acompañar la implementación" → presente (D-P3-9, sitio 1 de 3).

### 17.3.2 Insumos metodológicos y decisiones derivadas (506 w) → desaparece como sección
Seis párrafos "de X se deriva Y" que anticipan, uno por uno, 17.3.3.1, 17.3.6.4, 17.3.14, 17.3.15 y 17.3.12.3.
Comentarios 1 y 2 lo marcan. Su única idea rectora (la arquitectura se deriva de insumos metodológicos y cada
sección explicita la consecuencia) cabe en un párrafo de la introducción. Dos alternativas en D-B.

### 17.3.3 Alcance, requisitos y decisiones (72 + 964 w, Tablas 39–41) → ~550 w, tres tablas
- **17.3.3.1** (261 w): los cuatro párrafos parafrasean la Tabla 39 (núcleo/extensiones), 17.3.6 (prompts en el
  núcleo), 17.3.14 (DBE/EBE) y 17.3.12.3 (evidencia visual). **Se funde en la intro de 17.3.3** en dos
  párrafos y deja de existir como título. Resuelve el comentario 3.
- **17.3.3.2** (270 w + Tabla 39): la Tabla 39 es el ancla del capítulo y se queda entera. La prosa explica
  los cinco regímenes y la nota los explica otra vez: **una sola vez** (recomiendo la nota). Cae "la
  enumeración reúne únicamente responsabilidades: los criterios de exclusión… se tratan, respectivamente…"
  (organización interna). 270 → ~120.
- **17.3.3.3** (107 w + Tabla 40): la nota repite la prosa. La Tabla 40 solapa con 17.3.4 (cuatro principios =
  cuatro filas) y con tres filas de la Tabla 39 (observabilidad, reproducibilidad, modularidad); se queda porque
  es la única lista de cualidades. Nota a una oración.
- **17.3.3.4** (254 w + Tabla 41): la Tabla 41 (DA-01…13) es la interfaz con §17.4.2 y **no se toca en su
  contenido**; sí sus dos celdas gordas (DA-03 justificación 70 w → una oración; DA-11 decisión → "preselección
  liviana en el borde como variante opcional, deshabilitada por defecto y fail-open", comentarios 4 y 5). La
  prosa post-tabla cae entera: la glosa DA-08/09 vive en 17.3.12.3, la de DA-13 en 17.3.10, las "tres
  precisiones de lectura" en 17.3.15/17.3.14. "deberán preservarse" → presente (sitio 2). La intro de 17.3.3
  también tiene "deberán conservarse" (sitio 3).

### 17.3.4 Principios arquitectónicos (201 w) → desaparece como sección
Cinco oraciones con dos puntos ("El primero es la separación…: …") que reformulan las DA agrupándolas. El
aporte real es ese agrupamiento (13 decisiones en cuatro ejes más uno transversal). **Se convierte en el
párrafo que introduce la Tabla 41** (~90 w, sin la fórmula "El primero es"). Cinco dos puntos menos.

### 17.3.5 Vista general (700 w, Figura 4.1) → ~430 w
Párrafos 1–5 describen la Figura 4.1; el párrafo 3 enumera la ruta crítica que 17.3.7 vuelve a enumerar dos
veces, y el 4 anticipa 17.3.8 y 17.3.10. El **párrafo de 254 w** (patrones de acople HTTP + ZeroMQ/msgpack +
persistir-primero) es contenido propio y valioso: se parte en dos o tres párrafos, y **se vuelve la única casa
de esa explicación** (17.3.8.1, 17.3.8.4, 17.3.10.2, 17.3.12.1 y 17.3.18 dejan de re-explicarlo). Cae "y no
constituye un tercer patrón de acople" (defensa interna) y la duplicación entre párrafo 1 y nota de figura.

### 17.3.6 Configuración experimental y prompts (1.467 w, Tablas 42–43) → ~800 w
- **Intro + 17.3.6.1** (166 + 255 w): dicen tres veces que la configuración gobierna la corrida, se resuelve
  antes y permite atribuir. **Se funden en un bloque de ~200 w.** "Esta sección materializa…" cae.
- **17.3.6.2** (220 w + Tabla 42): la definición de *ejecución experimental* y `experiment_id` es propia y
  necesaria (la usan 17.3.11.2 y 17.3.12.1): se queda. Párrafos 1 y 3 repiten "configuraciones referenciadas
  con ciclos de vida distintos". En la Tabla 42 el cooldown se ubica fuera del motor **en dos filas**
  (patrones activos, política de distribución): una sola.
- **17.3.6.3** (329 w): párrafos 1–2 re-argumentan §17.1.5.3 con las mismas cinco citas → una remisión
  (D-J). Párrafos 3–4 (prompt asociado a condición, versión y variante; vocabulario activo reducido) son
  diseño y se quedan. Párrafo 5 ("Esta sección define… se desarrolla posteriormente") cae.
- **17.3.6.4** (299 w + Tabla 43): **E3-42**: la glosa E-DIR/E-IND/E-HYB baja a la remisión (~70 w menos; se
  resuelve el párrafo gordo de 153 w). Tabla 43: D-C.
- **17.3.6.5** (198 w): el párrafo DBE/EBE repite 17.3.14.3 y el de "ningún módulo opcional implícito" repite la
  nota de la Tabla 39. Dos párrafos (~100 w).

### 17.3.7 Plano de medios (1.969 w, Figura 4.2) → ~1.050 w, dos hijos o ninguno
- **Intro** (454 w): el alcance (párr. 1) se enumera otra vez en 17.3.7.1; el límite (párr. 2) vuelve en
  17.3.7.1 final y 17.3.7.2 criterio 5; "la sección precisa cómo debe comportarse…" es metadiscurso; DBE/EBE
  (párr. 4) vuelve en 17.3.7.1 "Ingesta" y 17.3.7.3; configuración (párr. 5) es la idea 5. → ~150 w.
- **17.3.7.1** (648 w): **el corazón del plano**, bien escrito, seis etapas con título en negrita. Se queda
  (~550 w) absorbiendo lo único nuevo de 17.3.7.3 (cambiar la selección de unidades cambia la variante; no
  maximizar FPS aislado) dentro de la etapa "Control de ritmo". Su último párrafo repite la intro.
- **17.3.7.2** (381 w, "El primer criterio… El quinto criterio"): cuatro de cinco criterios son DA-01/05 y
  filas de la Tabla 40; el propio (variabilidad temporal visible) pasa a un párrafo de cierre de 17.3.7.1.
  **Desaparece como título.**
- **17.3.7.3** (262 w): se funde en 17.3.7.1 (ver arriba). **Desaparece como título.**
- **17.3.7.4** (224 w): **casa del fail-open** (enmienda a E3-28). Se queda (~150 w) sin la oración "en esta
  sección sólo interesa fijar" y sin repetir MOT.

### 17.3.8 Plano de control (2.619 w, Tabla 44, Figuras 4.3–4.4) → ~1.450 w, cero nivel 5
- **Intro** (380 w): párr. 2 (detección/patrón/alerta) es la única casa de la idea 6 en §17.3; párr. 4
  (núcleo sin MOT) es la idea 3. → ~220 w. Figura 4.3: D-H.
- **17.3.8.1** (234 w): párr. 2–3 re-explican bus y HTTP (idea 7); párr. 5 habla de la ruta crítica del plano
  de **medios** (fuera de lugar). → un párrafo (~90 w) o se funde en la intro.
- **17.3.8.2** (277 w + Figura 4.4): contenido central. La nota de la figura repite la prosa (cinco estados
  dos veces). "No constituye certificación normativa" se dice acá, en 17.3.8.1, 17.3.9.1 y 17.3.12.3: queda en
  17.3.12.3. → ~220 w.
- **17.3.8.3 + 17.3.8.3.1–4** (200 + 1.229 w, **los cuatro títulos de nivel 5**): se reescribe como **una sola
  subsección de nivel 4 "Motor de evaluación de patrones"** en prosa continua: (a) qué es el motor (un
  párrafo, sin repetir la intro); (b) la **definición de patrón con sus siete elementos** (las viñetas se
  conservan: es el contenido más propio del capítulo; cae el párrafo "En conjunto, la definición reúne…" que
  las resume); (c) **granularidad** en un párrafo, conservando la afirmación fuerte ("escena sostiene que la
  condición persiste en la escena, no que el mismo sujeto la sostuvo"); (d) **niveles del catálogo** en un
  párrafo + Tabla 44 según D-D; (e) **salidas** en un párrafo: cae el que repite la máquina de estados, cae el de
  métricas ancladas en transiciones (§17.1.7.3 y Tabla 48) y cae "cadena operativa completa" (Tabla 16 de
  §17.1). 1.429 → ~700 w.
- **17.3.8.4** (299 w): se queda lo propio (consumidor antes que productor, huecos → `bus_dropped_events`,
  evento de ciclo de vida, broker futuro sin cambiar la frontera) y cae la re-explicación canal/repositorio.
  ⚠ Dice "una corrida en vivo se inicia primero en el plano de control y luego en el plano de medios": es
  verdadero pero incompleto (el orden real es control → distribución → medios, `operacion/130` R-01). Como
  §17.4 documenta el orden efectivo, §17.3 gana enunciando la regla ("todo consumidor se inicia antes que su
  productor") sin enumerar. → ~200 w.

### 17.3.9 Integración condición–estrategia–patrón–alerta (534 w, Figura 4.5) → se funde
La intro es metadiscurso; 17.3.9.1 repite la idea 6 y la Figura 4.5 lo dice sola; 17.3.9.2 (E-IND por
auditabilidad, E-DIR/E-HYB como ramas) es lo propio pero **la dueña del concepto es 17.3.6.4** (D-P3-4);
17.3.9.3 repite 17.3.6.5. Propuesta: 17.3.9.2 pasa a 17.3.6.4 (que se titula "Vocabulario y estrategia del
núcleo"); la Figura 4.5 migra con él o a la intro de 17.3.8 (D-H). **Desaparece como sección** (~180 w netos).

### 17.3.10 Distribución de alertas (735 w, Tabla 45) → ~380 w sin hijos
Intro de 38 w con "Esta sección define". 17.3.10.1 repite literalmente la oración de 17.3.15 (idea 11).
17.3.10.2 párr. 1 explica por tercera vez gobierno HTTP vs dato por bus; título con punto final. La Tabla 45
se queda. **17.3.10.3** (346 w) es la única prosa del capítulo con densidad de implementación (fila por
intento, cinco resultados, archivado de generaciones, unidad de conteo, modalidad de t_alert-notification).
Lo que es diseño: registrar-primero, supresión por condición y fuente aguas abajo, idempotencia por
notificación y canal, re-alertas medibles y no FP, latencia por modalidad → un párrafo (~120 w). Los literales
son de §17.4 (D-I; §17.4 v1.6 hoy no los tiene: si salen de acá hay que hacerlos aterrizar allá).

### 17.3.11 Contratos e interfaces (566 w, Tabla 46) → ~350 w sin hijos
Intro bien. **17.3.11.1** (125 w, un párrafo de ocho oraciones "La de X… La de Y…") recapitula fronteras ya
explicadas: cae o queda en una oración. **Tabla 46** es la interfaz con §17.4.3 y se queda. Prosa post-tabla:
el evento de percepción repite la fila y 17.3.7.1; los dos invariantes (`source_id = clip_id`; la incertidumbre
no fabrica infracción) y los cinco hitos son propios y se quedan (los hitos también están en §17.1.7.6 y en la
Tabla 47/48: acá se enuncian, en las tablas se nombran). **17.3.11.3** (117 w): identidad temporal por cuarta
vez; lo nuevo (campos opcionales de pose y máscara, relaciones en el control) es un párrafo.

### 17.3.12 Trazabilidad y evidencia visual (704 w, Tabla 47) → ~380 w
Intro con "esta sección no vuelve a especificar…". 17.3.12.1 repite JSONL (idea 7) y `experiment_id`; lo
propio es "reconstruir hasta la versión de código". 17.3.12.2: párrafo defensivo ("no constituyen una nueva
lista de contratos… no se distingue carácter obligatorio fila por fila") cae; la **Tabla 47 solapa con la 46**
(misma cadena de hechos, vista desde la persistencia) → D-E; los dos párrafos post-tabla repiten la nota y la
idea 2. **17.3.12.3 es la casa de la minimización** (idea 8): se queda ~150 w y sus otras cuatro apariciones
caen.

### 17.3.13 Observabilidad (316 w, Tablas 48–50) → ~450 w sin hijos, dos tablas
Cinco títulos para 316 palabras. Propuesta: intro (observabilidad como contrato) + los **cuatro estados de
aplicabilidad con sus causas típicas** (propio de §17.3) + criterio de relojes (una oración, §17.1.7.5 lo
fundamenta) + **Tabla 48** (métricas por tramo: es la materialización arquitectónica) + **Tabla 50** (señales).
**Tabla 49** duplica §17.1.7.3/17.1.7.5/Tabla 29/Anexo D → D-F. 17.3.13.4 ("t_alert-system integra el
diccionario citable", "F1 mediante el evaluador temporal con denominadores por estrato") son reglas de
reporte de §17.5, no diseño: caen; "el reporte es una proyección regenerable de hechos persistidos" se queda
en una oración.

### 17.3.14 Escenarios DBE y EBE (795 w, Tablas 51–52) → ~430 w, una tabla
Intro de 18 w con la **remisión rota** (17.1.4.4 → 17.1.4.2). 17.3.14.1 y 17.3.14.2 (54 y 56 w) son un
párrafo cada uno → se funden en la intro. 17.3.14.3 (equivalencia tras la frontera de entrada) es propio y se
queda; su párrafo 3 repite 17.3.6.5. **Tabla 51 duplica la Tabla 17 de §17.1** salvo la columna "Implicancia
arquitectónica" → D-G. 17.3.14.5: RTSP/OAK-D/EN son §17.1.4.1; fail-open por cuarta vez; el **ancla común
tiempo de medio ↔ reloj de pared** es propio y se queda; **Tabla 52** (condiciones observables EBE) se queda si
cae la 51. **17.3.14.6** (cero silencioso; imágenes/clips/vivo) es de lo mejor del capítulo: se queda entero.

### 17.3.15 Roles y unidades desplegables (198 w, Tabla 53, Figura 4.6) → ~110 w
"Esta sección no redefine…" cae; la oración literal de 17.3.10.1 queda en una sola casa; la Tabla 53 se queda
(fila EN sin re-explicar fail-open); Figura 4.6 → D-H.

### 17.3.16 Riesgos (64 w, Tabla 54) → se queda
Es una recapitulación en formato riesgo → mitigación, pero es la interfaz que §17.4/§17.5 verifican (R-20).
Sin cambios salvo la nota.

### 17.3.17 Plan de materialización (173 w, Tabla 55) → ~110 w
"El estado ejecutado corresponde a §17.4. En esta sección se conservan…" → una oración. Las tres clases de
extensión quedan acá y salen de 17.3.18.

### 17.3.18 Cierre (261 w) → ~110 w o desaparece (D-M)
Repite literalmente 17.3.5 (dos patrones de acople) y 17.3.17 (tres clases), más 17.3.6.4 y 17.3.8.3.2. Vale
conservar el último párrafo (el diseño se considera completo cuando cada decisión tiene criterio verificable
en la implementación) y la remisión a §17.4/§17.5.

---

## 6. Lo que NO se toca (con nombre)

- **Tabla 39** (capacidades y compromisos, 20 filas), **Tabla 41** (DA-01…13; sólo se acortan dos celdas),
  **Tabla 46** (contratos), **Tabla 54** (riesgos) y **Tabla 55** (plan): son las interfaces con §17.4.2,
  §17.4.3 y la verificación de R-20/R-26. Sus filas no cambian.
- **La definición de patrón en siete elementos** (17.3.8.3.1) y la **máquina de cinco estados** (17.3.8.2 +
  Figura 4.4).
- **fail-open** definido en prosa en 17.3.7.4 (enmienda a E3-28) y **DA-11**.
- **Persistir-primero**, huecos de secuencia → `bus_dropped_events`, consumidor antes que productor, evento
  de ciclo de vida (17.3.8.4).
- **Los invariantes** `source_id = clip_id` y "la incertidumbre no fabrica una infracción", y los **cinco
  hitos** (17.3.11.2).
- **Escena vs sujeto** ("la condición persiste en la escena" ≠ "el mismo sujeto") y la **exclusión de
  métricas MOT sin excluir la identidad** (una vez cada una).
- **Cero silencioso** `not_applicable/non_temporal_source` y los **cuatro estados de aplicabilidad**
  (17.3.14.6, 17.3.13.3).
- **Cooldown fuera del motor** (DA-13, sin nombrar ADR-011), re-alertas no son FP.
- **Figura 4.1** y **Figura 4.4**.
- **Autocontención y no-anacronismo**: hoy limpias; ninguna reescritura puede introducir códigos internos ni
  cifras de verificación.
- **Las decisiones D1–D4 del pase 1 y D-P2-x/D-P3-x** de la Etapa 3 (núcleo-solo, "evento de percepción",
  literales de protocolo en §17.4, fail-open en prosa) siguen rigiendo.

---

## 7. Propuesta de reestructuración (a decidir)

### Opción A — recomendada: 11 secciones, cero nivel 5, renumeración interna

Habilitada por el hecho verificado de que **nadie cita §17.3.x ni las Tablas 39–55 por número** desde §15/16,
§17.1, §17.4 o §17.5. Requiere un `mapa-secciones-17-3` como el de §17.1 para traducir las actas E3-xx.

| Nueva | Contenido (viene de) | Tablas / figuras | Prosa objetivo |
|---|---|---|---|
| 17.3.1 Propósito y pregunta rectora | 17.3.1 + idea rectora de 17.3.2 | — | ~200 |
| 17.3.2 Alcance, capacidades y decisiones arquitectónicas | 17.3.3 (+17.3.3.1 fundida) + 17.3.4 como intro de la Tabla 41. Hijos: capacidades / requisitos no funcionales / decisiones | T39, T40, T41 | ~600 |
| 17.3.3 Vista general y patrones de acople | 17.3.5 | Fig. 4.1 | ~430 |
| 17.3.4 Configuración experimental, vocabulario y estrategia del núcleo | 17.3.6 (intro+6.1 fundidas) + 17.3.9.2. Hijos: configuración de corrida / vocabulario y estrategia / comparabilidad | T42, T43 (reducida), Fig. 4.5 | ~950 |
| 17.3.5 Plano de medios | 17.3.7. Hijos: flujo (con control de ritmo y criterios) / capacidades opcionales y fail-open | Fig. 4.2 | ~1.050 |
| 17.3.6 Plano de control | 17.3.8. Hijos: máquina de estados / motor y definición de patrón / transporte y persistencia | T44 (según D-D), Fig. 4.4 (+4.3 según D-H) | ~1.450 |
| 17.3.7 Distribución de alertas confirmadas | 17.3.10 sin hijos | T45 | ~380 |
| 17.3.8 Contratos, trazabilidad y evidencia visual | 17.3.11 + 17.3.12. Hijos: contratos / hechos persistibles y evidencia visual | T46 (+T47 según D-E) | ~730 |
| 17.3.9 Observabilidad y aplicabilidad de métricas | 17.3.13 sin hijos | T48, T50 (T49 según D-F) | ~450 |
| 17.3.10 Escenarios DBE y EBE y topología de referencia | 17.3.14 + 17.3.15. Hijos: equivalencia y alcance de EBE / roles y unidades desplegables | T52, T53 (T51 según D-G; Fig. 4.6 según D-H) | ~540 |
| 17.3.11 Riesgos, plan de materialización y cierre | 17.3.16 + 17.3.17 + 17.3.18 | T54, T55 | ~330 |

Totales estimados: **~7.100–8.800 w de prosa** según las decisiones D-C…D-G (−32 % a −45 %), **~28 títulos**
(11 + ~17 de nivel 4), **cero nivel 5**, **14–15 tablas**, 4–6 figuras.

### Opción B — conservadora: 18 secciones, sin nietos

Se conservan los 18 títulos de nivel 3 y su numeración; se eliminan los 4 títulos de nivel 5 (17.3.8.3 en
prosa continua), se funden los hijos de un párrafo (17.3.13.x, 17.3.14.1–2, 17.3.9.x, 17.3.11.1/3) y se aplica
toda la poda de repeticiones de §3–§5. Resultado: ~9.500 w, ~40 títulos, cero nivel 5. Ventaja: cero
renumeración. Costo: 17.3.2, 17.3.4, 17.3.9 y 17.3.18 sobreviven como secciones de 100–200 palabras cuya
razón de ser es débil.

### Puntuación y estilo, cualquiera sea la opción

| Marcador | Hoy | Objetivo | Cómo |
|---|---:|---:|---|
| `:` en prosa | 72 | ≤ 15 | Las 71 oraciones están listadas en el script. Patrones dominantes: "El primero es X: …" (17.3.4, 17.3.7.2), "La frontera es explícita: …", enumeraciones introducidas por dos puntos. Se reescriben como dos oraciones o como oración con verbo |
| `;` en prosa | 86 | ≤ 20 | Casi todos separan enumeraciones de tres miembros con "; y". En celdas de tabla (60) se toleran como notación |
| `—` | 32 | ≤ 10 | §17.1 v1.15 quedó en 6 |
| Metadiscurso | 10 | 0 | Los diez sitios están identificados (nueve "esta sección", un "el presente capítulo") |
| "deberá(n)" | 3 | 0 | 17.3.1, 17.3.3 intro, 17.3.3.4 (D-P3-9) |
| Párrafos >150 w | 2 | 0 | 17.3.5 (254) se parte; 17.3.6.4 (153) se recorta con E3-42 |
| "El primero/segundo… es" | 7 | 0 | 17.3.4 y 17.3.7.2 desaparecen como tales |
| "debe/deben" | 87 | ~45 | Donde "debe" sólo re-enuncia una decisión tomada, indicativo ("la arquitectura separa…"). Donde es requisito de diseño, se queda (D-L) |
| Citas bibliográficas | 5 (Du, Zhou, Changpinyo, Radford, Sharma) | 0 o 5 | D-J |
| Erratas | 3 | 0 | punto final en título 17.3.10.2, "reconstuir", unificar "video" |

---

## 8. Decisiones para el usuario antes de escribir

| # | Decisión | Opciones | Recomendación |
|---|---|---|---|
| **D-A** | Profundidad de la reestructura | A (11 secciones, renumeración interna + mapa) / B (18 secciones, sin nietos) | **A**. El costo aguas abajo es cero (verificado) y §17.1 ya sentó el precedente |
| **D-B** | 17.3.2 Insumos metodológicos | Fundir su idea en 17.3.1 (un párrafo) / reducirla a una tabla insumo → consecuencia → sección | **Fundir**. Una tabla más iría contra la dirección del pase |
| **D-C** | Tabla 43 (vocabulario, 14 filas) | Reducir a núcleo + ramas E-DIR (5 filas) y remitir al Anexo C / eliminar y dejar `person`, `helmet`, `vest` en prosa / conservar | **Reducir a 5 filas**. Las 10 filas CR-03…06 son literalmente la Tabla C.1 y §17.3 no las diseña (núcleo-solo, D4) |
| **D-D** | Tabla 44 (motor por condición, 6 × 4) | Reducir a 3 columnas (patrón, dependencias arquitectónicas, tratamiento) / eliminar y dejar un párrafo / conservar | **Reducir a 3 columnas**: la columna "Evidencia y regla" repite la Tabla 21 de §17.1 y los criterios de PR-05/06 |
| **D-E** | Tabla 47 (hechos persistibles) | Eliminar y decir en prosa qué se persiste además de los contratos de la Tabla 46 / conservar | **Eliminar** (con persistir-primero, lo que se intercambia es lo que se persiste; lo adicional cabe en una oración) |
| **D-F** | Tabla 49 (diccionario de métricas) | Eliminar con remisión a §17.1.7.3, Tabla 29 y Anexo D / conservar reducida | **Eliminar**. §17.3 conserva en prosa lo que §17.1 no tiene (los cuatro estados de aplicabilidad) |
| **D-G** | Tabla 51 (DBE/EBE) | Eliminar con remisión a la Tabla 17 de §17.1 / reducir a dos columnas (dimensión → implicancia arquitectónica) | **Eliminar**; la Tabla 52 cubre lo arquitectónico de EBE |
| **D-H** | Figuras 4.3 (plano de control, tres cajas) y 4.6 (EN→CPN←TN); destino de la 4.5 si 17.3.9 se funde | Eliminar 4.3 y 4.6; 4.5 a la nueva 17.3.4 o a la intro de 17.3.6 | **Eliminar ambas**; 4.5 a la intro del plano de control (es su síntesis) |
| **D-I** | Detalle del ledger (17.3.10.3) | Conservar en diseño / dejar invariantes y mover literales (cinco resultados, fila por intento, generaciones, modalidad) a §17.4 | **Mover** con handoff E4 explícito: §17.4 v1.6 hoy no los tiene, y no pueden perderse |
| **D-J** | Cinco citas de 17.3.6.3 | Remitir a §17.1.5.3 y quitarlas / conservarlas | **Remitir**. Cero bajas en la lista global (§17.1 las mantiene) |
| **D-K** | Los 7 comentarios | Resolverlos en este pase (quedan atendidos de facto) / dejarlos viajar | Recomiendo resolverlos al aceptar la v1.6, con acta que los mapee a las unidades. Lo decide el usuario |
| **D-L** | Voz "debe/deben" | Reducir donde re-enuncia decisiones / dejar como modal de diseño | **Reducir a la mitad**, sin convertir requisitos de diseño en pasado |
| **D-M** | 17.3.18 Cierre | Conservar corto (~110 w, sin repeticiones) / eliminar | **Conservar corto**: §17.1 conservó sus conclusiones parciales |

---

## 9. Cómo se aplicaría (para cuando se decida)

1. **Base:** v1.5 (= v1.4). **Salida:** v1.6 con control de cambios, misma mecánica que la Etapa 2 (XML
   byte a byte; los párrafos con `sectPr` se reescriben por dentro, nunca se borran: hay **21** en el
   documento). Acta: `desarrollando/correcciones-etapa-3-pase-4.md` con unidades **E3-43…**, y
   `mapa-secciones-17-3-v1-6.md` si se elige la Opción A.
2. **Orden interno:** primero E3-42 y los tres sitios de voz (son los pendientes registrados), después la
   reestructura, después puntuación.
3. **Verificación §D del pase:** títulos por nivel (0 de nivel 5); tablas restantes citadas exactamente una
   vez en prosa; figuras citadas en prosa; greps en cero (metadiscurso, "deberá", `sección 17.1.4.4`, códigos
   internos, cifras); conteo de `:`/`;`/`—`; diff párrafo a párrafo contra `90` atribuido a unidades;
   **chequeo anti-duplicación** (ninguna oración ≥ 12 palabras repetida) y **el patrón "marca de párrafo borrada
   + texto vivo"** (lección del pase 3 de la Etapa 2); citas bibliográficas restantes idénticas a lo decidido
   en D-J; los 7 comentarios con sus anclas intactas.
4. **Al cerrar:** re-extraer `90` (regla D-C), fechar en `00-el-informe-hoy.md`, actualizar
   `00-lo-que-resta.md` §3.2 (cerrar el handoff), regenerar el kit (`generar_project_kit.py --check`).
5. **Handoffs que nacen acá (no son de este pase):** pegar la FIG-E producida en lugar de la Figura 4.4
   embebida; numeración global de figuras (hoy 4.x) y de tablas (39–55 corren con el hueco de §17.1);
   literales del ledger a §17.4 si D-I = mover; "evento de detección" en la Tabla 16 de §17.1 (integración).
