# Revisión del Informe Final E-OVRT-VDP (v0.6, 2026-09-15)

Evaluación de coherencia, cohesión, repeticiones y redundancia sobre el PDF
`E-OVRT-VDP_Informe_Final_2026-09-15_v0.6_Revision_Tramos_sugerencias.docx.pdf` (414 pp, ~80.500 palabras).

## 1. Valoración general

El documento es sólido en el fondo: la cadena problema → hipótesis → protocolo → diseño → implementación → evaluación → cierre está bien trabada, las cifras son internamente consistentes (47 clips = 34 + 13; 37 episodios = 35 + 2; 32/15 positivos/negativos; 336 h = 42 sem × 8 h; latencias en vivo coherentes con las ventanas de 4 s y 7 s) y no hay referencias cruzadas rotas a secciones ni a tablas. El problema principal es de forma: extensión excesiva sostenida por redundancia estructural (estado del arte vs marco teórico; consolidación metodológica vs diseño vs implementación), disclaimers repetidos decenas de veces, un tono defensivo uniforme ("no equivale", "no constituye") y varias inconsistencias de numeración, notación y citas heredadas de versiones anteriores.

Extensión por sección (páginas): Glosario 12 · Introducción 6 · Objetivos 2 · Plan 8 · Estado del arte 50 · Marco teórico 34 · **Desarrollo 221** (17.1 = 70, 17.2 = 11, 17.3 = 73, 17.4 = 37, 17.5 = 25, 17.6 = 5) · Cierre 10 · Anexos 64.

## 2. Coherencia (fondo)

### 2.1 Objetivos y plan vs. lo ejecutado
- **Objetivo específico 5** promete "métricas de detección, seguimiento, rendimiento del pipeline, latencia de alerta y utilidad operativa de las notificaciones". Ni las métricas MOT ni la utilidad operativa se evaluaron (17.5.7 y 18.6 lo reconocen sólo en parte). Reformular el objetivo o cerrarlo ítem por ítem en 18.6.
- **Etapa 5 del plan (14.2.5)** anuncia "análisis comparativo con resultados del estado del arte" y "entorno simulado de obra civil". En 17.5 no hay comparación con el estado del arte (18.1 sólo explica por qué no es comparable). Aclarar en 18.6 o en 17.5.7.
- **14.4 Costos** está redactado en presente como si fuera lo ejecutado ("Movilidad. Un único traslado…") y luego 17.2 lo repite en tablas. Reducir 14.4 a una síntesis de lo *previsto* y remitir a 17.2, o marcar explícitamente previsto/ejecutado.

### 2.2 Estatuto de la distribución de alertas
- 12.4: "La plataforma incluye además la distribución de alertas confirmadas… mediante MQTT" (alcance).
- Tabla 32: "Capacidad opcional".
- 17.3.7 y 17.4.1: "módulo desacoplado", implementado y ejercido.
Unificar el régimen (núcleo, opcional o complementario) en un solo lugar.

### 2.3 Preguntas rectoras con huecos
16.7.3 enumera P-E1-01, 02, 03, 04, 06 y 08. Faltan 05 y 07. El texto dice que "los códigos se conservan para mantener la trazabilidad con las secciones posteriores", pero el lector del informe final no tiene el documento previo y sólo ve un salto. Renumerar, o añadir una nota que diga qué eran 05 y 07 y por qué se retiraron.

### 2.4 Cronología de la referencia temporal
- 17.5.1: la referencia humana "quedó congelada antes del reporte".
- 17.5.4: una "revisión ciega" posterior descartó 5 de 7 episodios del estrato de obra real.
- Nota de Tabla 51: una corrección posterior de la referencia (5.313 → 5.308) no se re-ejecutó.
Los conteos de 17.5.1 (37 episodios, 32/15) ya son post-revisión, pero eso no se dice. Ordenar: qué se congeló, cuándo se revisó, y que las cifras reportadas corresponden a la versión revisada.

### 2.5 Contradicciones diseño ↔ implementación declaradas pero no cerradas
- Previsualización "habilitada por defecto" (17.4.7) contradice DA-11 y 17.3.4.4 ("ningún módulo opcional opera como comportamiento implícito"). Está señalado, pero no aparece en la lista de ocho limitaciones de 17.5.7 ni en 18.6. Cambiar el default o registrarlo como desviación.
- Regla de partición (17.1.6.3: una fuente de ajuste no integra el banco) vs. desviación con `construction_site_safety` (17.4.7). En 18.5 se dice "CHV se excluyó para proteger la separación" sin mencionar la desviación. El Cierre debería conservarla.

### 2.6 Numeración y estructura
- Secciones **8, 9 y 10 no existen** (salto de "7. Palabras clave" a "11. Glosario"); presumiblemente índices pendientes.
- **Figuras**: "Figura 1" (Gantt) y luego "Figura 4.1 … 4.6" en la sección 17. Numeración heredada de un "capítulo 4" que ya no existe. Unificar (Figura 1–7 o 17.1–17.6).
- Título "14. Plan De Trabajo De Proyecto Integrador" con mayúsculas en preposiciones; el resto usa minúsculas.
- 14 tablas nunca se mencionan en el texto (sólo tienen título): 1, 12, 13, 18, 20, 21, 31 y B.1–B.7. Añadir una llamada a cada una.

## 3. Cohesión y redundancia

### 3.1 Solapamiento entre secciones
- **Estado del arte (15) y Marco teórico (16)** repiten contenido: fundamentos OVD (15.2.1 ↔ 16.3.1–16.3.2), inconsistencia temporal (15.2.5.2 ↔ 16.4.1), MOT/tracking-by-detection (15.3.1 ↔ 16.4.2), latencia y protocolos (15.4.1 ↔ 16.5.1), brecha de evaluación integrada (15.4.3.1 ↔ 16.5.5, reconocida). Recomendación: que 16 conserve lo normativo (16.2), lo conceptual no cubierto en 15 (16.3.4 composicionalidad, 16.5.2 descomposición G2A, 16.6 ético-legal) y las preguntas rectoras, y remita a 15 para el resto.
- **15.2.1**: los cuatro párrafos introductorios describen cada paradigma (Feature Enhancer, Language-guided Query Selection, RepVL-PAN, cacheo de embeddings, Florence-2 seq2seq) y 15.2.1.1–15.2.1.4 vuelven a describirlos con las mismas frases. Dejar la intro en un párrafo de mapa.
- **Catálogo de condiciones** presentado tres veces: 17.1.2.1, 17.1.5.1 (ambas remiten a Tabla 14) y Tabla 37. **Motor de patrones** definido en 17.1.3.2, 17.1.5.2 y 17.3.6.2. **DBE/EBE** definidos en 12.4, 17.1.3.3, 17.1.4.2 (Tabla 13), 17.3.10 y 17.3.10.1.
- **17.1 (70 pp) y 17.3 (73 pp)** son prescriptivos y buena parte se vuelve a contar en 17.4 como "materializado". Se puede podar 17.3 (p. ej. 17.3.5.1, 17.3.6.2, 17.3.8.2 repiten lo que 17.4.2–17.4.5 muestran con artefactos reales).
- **Introducción**: 12.1 párrafos 3 y 4 y 12.2 párrafo 1 dicen tres veces lo mismo (closed-set vs open-vocabulary, ejemplo "persona sin casco"). 12.2 y 12.4 repiten casi textualmente "no se evalúa la carga cognitiva ni la incidencia de accidentes"; en 12.4 además con un "porque" circular ("no evalúa X principalmente porque X no forma parte de sus resultados").

### 3.2 Disclaimers y fórmulas repetidas (conteos en el cuerpo)
- "alerta asistiva / no vinculante / no reconoce identidad / no certifica cumplimiento": 12.2, 12.4, 16.2.3, 16.6.2–16.6.3, Tabla 12, 17.1.10, 17.3.6, 17.3.8.3, 17.4.7 (final), 18.6. "identidad personal" ×10; "certificación/determinación/juicio normativo" ×5.
- "persistir antes de publicar": 17.3.3, 17.3.6.3, 17.3.8.2, Tabla 44, Tabla 45, 17.4.3, 17.6.2, Tabla B.7.
- "los percentiles de tramos distintos no se suman": 16.5.2, nota Tabla 40, 17.5.5, nota Tabla 54, 18.4, Anexo E.
- "no se publica un cero / not_applicable con causa": 17.1.7.1, 17.3.9, 17.3.10.2, Tabla 44, 17.4.5, 17.4.7, 17.5.1.
- "un identificador de seguimiento no es identidad personal": 16.4.2, 16.4.3, 16.6.2, 17.3.6.2, 17.3.8.1, 17.6.4.
Sugerencia: un único apartado "Alcance y salvaguardas" (en 12.4 o 17.1.10) y remisiones breves.

### 3.3 Estilo
- Tono defensivo constante: "no constituye" ×29, "no equivale" ×21, "no implica" ×14, "no sustituye" ×10, "no reemplaza" ×9, "sin confundir" ×8; 69 oraciones empiezan con "No". El patrón "X establece A; no establece B" se usa en casi todos los párrafos de 18. Reservarlo para los casos en que la sobreinterpretación es plausible.
- Conectores: "de modo que" ×53, "por ello" ×21, "de manera" ×41, "de forma" ×29; "declara/declarada/declarado" ×133.
- "sólo" con tilde ×84 y "solo" sin tilde ×10 (mezcla). La RAE recomienda sin tilde; elegir uno.
- 42 oraciones de más de 60 palabras fuera de tablas; media general 20 palabras, adecuada.

## 4. Terminología y notación

- "AP@0.5" (×2, en 17.1.5.4 y 17.2.5) vs "AP@0,5" (×9) vs "AP50/mAP50" (×22). 17.5.1 declara la equivalencia AP50 = AP@0,5, pero la coma/punto decimal debe unificarse.
- "fps" (×7) vs "FPS" (×35).
- "multiobjeto" (×23) vs "multi-objeto" (×2, incluido el título de 15.2.6).
- "fine-tuning" (×13) vs "ajuste fino" (×17); "checkpoint" (×23) vs "punto de control" (×4, ambos en el mismo párrafo de 17.4.7); "tracker" (×19) vs "seguidor" (×1); "dataset" (×27) vs "conjunto de datos" (×2).
- "modelo campeón" (17.2.4 nota, 17.2.5) vs "perfil operativo" en el resto.
- "Escenario A/B" (12.4, 17.5.1) vs DBE/EBE en el resto; ambos están en el glosario, pero conviene usar siempre el par completo la primera vez y luego una sola forma.

## 5. Citas y referencias

### 5.1 Errores
- **DINO mal referenciado**: 15.2.1 cita "H. Zhang et al., 2022" para DINO, pero la única entrada Zhang, H. (2022) en la lista es *GLIPv2* (Zhang, Zhang, Hu, … Gao). Falta la referencia de DINO (Zhang, Li, Liu, Zhang, Su, Zhu, Ni y Shum, ICLR 2023 / arXiv 2022).
- "Axis Communications AB, **s. f.**" (17.1.7.5): la lista sólo tiene Axis (2015).
- "Luxonis, s. f.-**a**" (17.1.4.1, Tabla 13) y "s. f.-**b**" (15.4.2, 17.1.4.1) vs una sola entrada "Luxonis (s. f.)" en la lista; Anexo B cita "Luxonis (s. f.)".
- "Agencia de Acceso a la Información Pública, s. f.-**a**" (16.6.1) vs entrada "(s. f.)".
- NVIDIA: sufijos s. f.-a, -b (NVIDIA Corporation), -g y -h; faltan c–f. Restos de una versión anterior; renumerar a-d.

### 5.2 Entradas de la lista no citadas en el cuerpo
ISO (2018) 45001 · IDEA-Research (2024b) Grounded-SAM-2 · Li, S. et al. (2022) TET · Li, X., Cho y Xiao (2022) · Yao et al. (2022) DetCLIP · Zhou et al. (2022a) CoCoOp · Zou, X. et al. (2023) · Zou, Z. et al. (2023) · Zhang, H. et al. (2022) GLIPv2 (citada por error para DINO). Eliminarlas o citarlas.

### 5.3 Ambigüedad de iniciales (APA exige inicial cuando hay homónimos)
- "Wang et al., 2025" sin inicial ×10 (en 17.x) vs "A. Wang et al., 2025" ×8 (en 15–16); hay A. Wang, H. Wang y Z. Wang.
- "Zhang et al., 2022" sin inicial ×4 vs "Y. Zhang" ×2; hay H. Zhang y Y. Zhang.
- "Jiang et al., 2024" ×5 sin inicial; hay K. Jiang (domain adaptation) y Q. Jiang (T-Rex2).
- "Yao et al., 2024" ×4; hay L. Yao (DetCLIPv3) y Y. Yao (OVDEval).
- "Li et al., 2023" ×4 sin inicial vs "S. Li et al." ×4.
- "Zhou et al., 2022" sin letra (17.1.5.3) vs "2022b" en el resto.

## 6. Pendientes formales
- Placeholders "[se completará más adelante]": Hoja de aceptación, Dedicatoria, Agradecimientos, Resumen y Abstract.
- "[[PENDIENTE: completar la dirección de origen y la fecha de acceso de cada video…]]" en Anexo F.
- Secciones 8–10 (índices) ausentes.
- Tabla B.6 y 17.4.4 repiten los mismos parámetros; una de las dos puede remitir a la otra.

## 7. Recomendaciones priorizadas
1. Corregir la referencia de DINO, las citas "s. f.-a/-b" sin entrada, y las iniciales ambiguas (Wang, Zhang, Jiang, Yao, Li, Zhou). Eliminar las 9 entradas no citadas.
2. Unificar numeración de figuras y añadir secciones 8–10; completar placeholders.
3. Cerrar en 18.6 la correspondencia objetivo por objetivo (especialmente el 5) y etapa por etapa del plan.
4. Fijar el estatuto de la distribución de alertas (12.4 vs Tabla 32).
5. Renumerar o explicar P-E1-05 y P-E1-07.
6. Podar redundancia: 15.2.1 intro; 16 vs 15; 17.1 vs 17.3 vs 17.4; introducción 12.1–12.2; 14.4 vs 17.2. Concentrar salvaguardas en un apartado.
7. Unificar notación (AP@0,5 / AP50, FPS, multiobjeto, ajuste fino, checkpoint, sólo/solo) y reducir el patrón "no constituye / no equivale".
8. Registrar en 17.5.7 o 18.6 las dos desviaciones diseño-implementación (previsualización por defecto; fuente compartida ajuste/banco).
