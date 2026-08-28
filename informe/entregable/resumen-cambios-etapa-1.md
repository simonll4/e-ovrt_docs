# Etapa 1 — resumen de los ajustes: del documento inicial al final

- **Comparación:** `Etapa 1.docx` (inicial, 2026-08-27) → `E-OVRT-VDP_Secciones_15_y_16_Estado_del_Arte_y_Marco_Teorico_v1.0.docx`.
- **Una asimetría que hay que saber:** el documento inicial traía **solo §15** (Estado del arte,
  21.600 palabras). El final trae **§15 + §16** (Marco teórico). Para §16 el punto de partida
  es el texto del informe v1.1, que nunca había recibido ningún pase.
- **Recorrido:** cinco pases de corrección, cada uno documentado en
  `desarrollando/archivado/correcciones-etapa-1*.md` (E1-01…E1-58, D-E1-1…13). Este resumen
  explica **qué cambió y por qué**, no repite el detalle.

---

## 1. La cifra global

| | Inicial | Final | Cambio |
|---|---:|---:|---:|
| §15 Estado del arte | 21.613 palabras | 10.474 | −52 % |
| §16 Marco teórico *(desde v1.1)* | 30.749 | 11.598 | −62 % |
| **Desarrollo completo** | **52.362** | **22.072** | **−58 %** |
| Títulos numerados | 188 | 92 | −96 |
| Tablas | 14 | 11 | −3 |
| Modelos con ficha propia en §15 | 18 | 6 | los que tienen rol en el trabajo |
| Fuentes citadas | ~200 | ~85 | salen las de lo podado; entran 7 nuevas |

**La mitad que se fue no se fue por larga: se fue porque no sostenía nada.** El criterio de
todo el recorrido fue uno solo — *una sección se queda si sostiene un resultado, una decisión
de diseño o un argumento de defensa* — y la decisión final del equipo (D-E1-13) fue **no
recortar más**: lo que queda está justificado.

---

## 2. Los seis tipos de ajuste

### A. Alinear el texto con la plataforma que efectivamente se construyó

El problema de fondo del documento inicial era que describía —a veces prescribía— cosas que el
proyecto no hizo, y omitía la vara de otras que sí hizo. Se verificó contra el código, no
contra la memoria:

| El texto decía o suponía | La plataforma es | Ajuste |
|---|---|---|
| Recomendaba ByteTrack/OC-SORT, "la familia SORT extendida es la más adecuada" | Tracker propio, **IoU puro sin Kalman ni apariencia**, medido por su efecto en alertas | El cierre de §15.3 se reescribió en **criterios con cita**, sin elegir método |
| Criterios "el modelo **debe** soportar prompts visuales", "extensión hacia segmentación", "multi-protocolo", "multi-flujo", "jornadas de 8–10 h" | Nada de eso se ejerció | Cuatro secciones de "criterios orientadores" (3.600 palabras, dos sin ninguna cita) → **dimensiones de comparación** con fuente; el peso de cada una es del diseño |
| §16.7.5 describía la arquitectura de dos planos "coherente con el anteproyecto"; §16.2.3 nuestra arquitectura de eventos con nuestros nombres | Es diseño, no marco teórico | Eliminados: el marco teórico no adelanta el sistema |
| Tabla de principios ético-legales con columna **"Decisión de diseño implicada"** y controles nunca implementados (RBAC, cifrado, auditoría) | Prototipo académico, un host | Columna renombrada **"Restricción que impone al diseño"**; las celdas en voz de exigencia |
| Latencia descompuesta en **6** componentes (incluía renderizado) y la ecuación **vacía** en el archivo | El informe mide **4**: captura · transporte · preprocesamiento · inferencia | Reescrita con la notación del protocolo; ecuación repuesta; `t_preprocess` definido |
| Sistema de "ingesta multi-protocolo, decodificación acelerada" (§15.4.3.1) | Ingesta RTSP + SDK; decodificación por software | "ingesta de video" |
| Prometía "plano de control en la nube" y comparación "GStreamer versus FFmpeg" | Un host, sin nube; esa comparación nunca ocurrió | Cláusulas eliminadas |
| Sin una palabra sobre **MQTT** ni sobre ingesta por **SDK de cámara** | Ambas implementadas y medidas | Agregadas con fuente (OASIS 2019; Luxonis) |

### B. Fundar lo que faltaba

Lo más importante que **entró** — la poda le hizo lugar, no compitió con esto:

- **La vara supervisada de EPP** que el 0,551 del §17.5 necesita para significar algo: YOLOR
  0,883 sobre SHEL5K (`head` 0,907), YOLOv5x 0,866 sobre CHV, YOLOv9-e ≈0,71 sobre SH17.
- **La vara zero-shot OVD×EPP**, la única publicada (Choi & Greer 2024: `hardhat` 0,649 pero
  `head` 0,102 con asociación jerárquica), y la evidencia de que la composición con atributo
  falla (Chen & Zou 2025: IoU < 20 %).
- **El fundamento del mecanismo central de la tesis.** En 30.700 palabras de marco teórico, la
  palabra *"negación"* aparecía **cero veces**. Ahora §16.3.4 explica por qué un encoder
  contrastivo se comporta como bolsa de palabras ante atributos y negación (ARO — Yuksekgonul
  et al.; Winoground — Thrush et al., ambos verificados en arXiv) y deja planteadas las **dos
  formulaciones** de una condición definida por ausencia — pedirla al modelo, o pedir evidencia
  positiva y derivarla — **sin decir cuál eligió el proyecto**. Sin esto, el lector llegaba a
  §17 sin haber leído nunca por qué el sistema razona la ausencia en vez de pedirla.
- **Swin-B con su régimen.** El proyecto despliega dos backbones y el texto solo daba la cifra
  de Swin-T y Swin-L. Se agregó que la cifra pública de Swin-B **no es zero-shot** (COCO está
  en su entrenamiento) — verificado contra la tabla del repositorio oficial.
- **YOLOE-v8 (paper) ≠ YOLOE-26 (plataforma)**, y la precisión de que YOLOE-11 es del paper
  original, no de Ultralytics — verificado contra el repositorio oficial.
- Genealogía (Grounding DINO extiende a GLIP), *catastrophic forgetting* como término
  estándar, la vara tamaño-de-datos/parámetros para el fine-tuning (Kumar 2022; Lee 2023), la
  síntesis de licencias como criterio de selección, productor/consumidor y publish/subscribe.

### C. Contradicciones internas que un jurado hubiera encontrado

- §16 afirmaba, **en dos lugares**, que la retención open-vocabulary tras fine-tuning "varía
  entre familias arquitectónicas"; §15, ya corregido, argumenta lo contrario. Y el puntero
  citaba "§15.2.4.5", que ya no existía. Corregido a: la retención se describe **por receta**.
- La Tabla 4 decía de YOLOE "Retención OVD: **No** — modelo reparametrizado"; el proyecto
  ejerció esas dos recetas y **midió** la retención. Reformulada: *"No evaluada por los autores;
  la retención requiere reinyectar vocabulario abierto"* — lo que §17.5 puede confirmar.
- El Bloque D se llamaba "Modelos generativos" y 3 de sus 4 modelos no lo eran — el propio
  texto lo decía. Renombrado.
- La misma obra citada con años distintos entre §15 y §16 (Liu 2023/2024, Xiao 2023/2024, Lin
  2014/2015, Zhou 2021/2022a/2022b). Unificadas.
- Tres citas con letra de desambiguación **falsa** (`Jeong 2022a/b`, `Shi 2016a/b`, `X. Wang
  2020a/b`, una sola entrada cada una): la prueba de que 1.400 palabras estaban escritas dos
  veces. Salieron con la duplicación.

### D. Erratas de dato y de forma

Cifras sin verificar de OmDet-Turbo (eliminadas con su ficha), un "ahorro de 40 ms" en un
modelo de 7,1 ms totales, un 52,4 sin origen, Abdalwhab 2025 usado para sostener algo que el
paper no sostiene, la columna "Latencia" sin declarar que era 1000/FPS, licencias "Apache-2.0"
en modelos de API cerrada, **un texto de instrucción de redacción colado al informe** (*"Esto
es clave para la plantilla: cuando el documento menciona latencias…"*), referencias colgadas
("el análisis del modelado de apariencia"), Ahmad 2005 citado para algo que no trata, y —en
la última pasada— **runs en negrita+itálica que partían palabras** en §16.5 (*"pro|tocolo
reproducible sin anticipar la s|elección"*), heredados de una entrega intermedia e invisibles
salvo por los asteriscos en la extracción.

### E. Poda por aporte

Qué salió y por qué — nunca por cuota:

| Salió | Palabras | Razón |
|---|---:|---|
| Fichas de GLIP, OV-DETR, OV-DINO, OmDet-Turbo, Detic, DetCLIP, APE, LLMDet, T-Rex2, Grounded SAM, OVTrack, Roboflow | ~2.700 | Catálogo sin uso posterior: el trabajo evaluó 3 familias. Quedan los 6 con rol; el resto vive en la Tabla A.1 (para §19) |
| §15.4: RTMP, HLS/DASH/CMAF, WebRTC, SRT, RIST en prosa; roles del servidor; edge/cloud; Janus, Kurento, MediaMTX, OME, SRS | ~5.200 | La ingesta es RTSP + SDK. **Se conservó RTSP/RTP íntegro** (única vara del `capture_to_host` medido) y **§15.4.3 entero** (la brecha que el proyecto ocupa) |
| §16.5: códecs acelerados, IPC, frameworks, taxonomías de nube y niebla, catálogo de aceleradores | ~10.500 | Nada de eso sostiene una decisión; y 1.400 palabras estaban escritas dos veces |
| §16.7: recapitulaciones, criterios sin cita, arquitectura del anteproyecto, mapa de brechas | ~3.800 | 4.790 palabras con **cero citas**; el mapa de brechas estaba 5/6 duplicado con §15 |
| §16.4: tratado de Kalman/Mahalanobis/ReID; criterios de selección MOT | ~1.550 | La plataforma usa IoU puro y no evalúa métricas MOT |
| Anexo A y Referencias | — | **No se descartaron: salieron del entregable** (§4) |

Lo que se conservó **a propósito** aunque la poda original lo marcaba: las métricas MOT
(comprimidas, no eliminadas — sin ellas no se justifica excluirlas), el párrafo de RTSP/RTP, y
todo §16.2 y §16.3 (el ancla normativa de CR-01/CR-02 y el corazón conceptual).

### F. Formato y terminología

Alineado a la convención de las secciones ya cerradas del informe (§17.3–§17.5): 39 títulos de
Title Case a tipo frase; rótulo `**Tabla N**` en negrita simple; `*Nota.*` en itálica (APA 7)
unificando cuatro variantes; una palabra por concepto — **cuadro** (no fotograma/frame),
**extremo a extremo** (no end-to-end/E2E, salvo "arquitecturas end-to-end"), **seguimiento**
(no tracking, salvo *tracking-by-detection*); IoU, SFU y NACK definidas la primera vez;
cinco encabezados que habían perdido su estilo de título restaurados; hueco de numeración
cerrado; las 13 tablas con número y título arriba, nota y fuente debajo, y mención en prosa.

---

## 3. Antes y después, por sección

| Sección | Inicial | Final | Qué pasó |
|---|---:|---:|---|
| §15.2.1 paradigmas y fichas | 4.641 | 1.932 | 18 fichas → 6; introducción sin cifras; Bloque D renombrado; Florence-2 con ficha |
| §15.2.2 composición | 665 | 128 | La idea (desacoplar etapas) sin el desarrollo de Grounded SAM |
| §15.2.3 síntesis | 1.129 | 1.182 | + párrafo de licencias como criterio |
| §15.2.4 fine-tuning | 2.688 | 909 | Reescrito por receta; Tabla 4 corregida; + Kumar/Lee, LoRA, OWL-ST |
| §15.2.5 brechas | 1.737 | 1.763 | **Intacto** — es el núcleo; + vara EPP y OVD×EPP |
| §15.3 MOT | 2.447 | 1.451 | Fichas → un párrafo de contraste; cierre en criterios; métricas comprimidas |
| §15.4 streaming | 7.895 | 2.696 | Solo RTSP + criterios + brechas + SDK + MQTT |
| §16.2 condiciones de riesgo | 3.008 | 2.866 | **Intacto** salvo el párrafo que describía nuestra arquitectura |
| §16.3 visión-lenguaje | 2.542 | 1.633 | + §16.3.4 negación (nuevo); criterios → dimensiones; triple repetición → una |
| §16.4 persistencia temporal | 2.684 | 1.133 | Fundamentos comprimidos; 16.4.1 y 16.4.3 conservados |
| §16.5 tiempo real | 12.926 | 2.424 | Ecuación repuesta, 4 componentes, productor/consumidor, pub/sub, borde = prefiltrado |
| §16.6 ético-legal | 4.266 | 2.214 | 16.6.2 y 16.6.6 vivas; Tabla 12 como restricciones; AAIP marcada pendiente |
| §16.7 + §16.8 cierre | 4.790 | 761 | Una brecha transversal + preguntas rectoras + tres limitaciones del marco |

---

## 4. Lo que salió del entregable pero no se descartó

Por decisión del equipo, el `.docx` de la etapa es **solo el desarrollo**. El Anexo A y el
listado de Referencias, ya corregidos, quedaron en `90e-etapa1-anexo-a-y-referencias.md`
para §19 y para el listado global — y **hacen falta**: el cuerpo cita la Tabla A.1 y la A.2.

- **Tabla A.1:** de 12 a **20 filas**; ahora incluye **Grounding DINO Swin-T/Swin-L y
  MM-Grounding-DINO** (faltaban, siendo los modelos del trabajo); licencias corregidas.
- **Tabla A.2:** métricas MOT en términos de su límite frente a la alerta. La A.3 (servidores)
  se eliminó por quedar sin uso.
- **Referencias:** 83 entradas, sin huérfanas. **Siete altas** que el listado global aún no tiene:
  Kumar 2022 · Lee 2023 · OASIS 2019 · Ultralytics 2026 · Yuksekgonul 2023 · Thrush 2022 · y
  Luxonis con su letra (`s. f.-b`).

---

## 5. Lo que queda abierto — y no es de esta etapa

1. **D-E1-11 — AAIP.** §16.6.2.2 deja marcado `[[PENDIENTE: definir con el equipo la
   aplicabilidad de esta inscripción al contexto experimental y documentar el recaudo adoptado
   en §17.1 y §17.4.]]`. Decisión del equipo; el marcador viaja hasta resolverla.
2. **Etapa 2:** §17.1 remite a "la sección 16.7.6", que tras la renumeración es §16.7.3.
3. **Integración final:** el rótulo "Nota" tiene variantes en las *otras* secciones del
   informe; unificar sobre el maestro completo. Tres cláusulas meta ("sin anticipar la
   estrategia que adopte el diseño") pueden cortarse ahí si molestan.

---

## 6. Cómo se verificó

- **Cada pase, por diff** contra la versión anterior: se comprobó que cambiara solo lo pedido.
- **Contra la implementación**, no contra documentos: catálogo de modelos, código del tracker,
  configuraciones de fine-tuning, fuentes de ingesta.
- **Contra fuentes externas** cuando una cifra o atribución lo exigía: README oficial de
  Grounding DINO (Swin-B), repositorio de YOLOE (variantes 11 vs 26), arXiv (ARO, Winoground).
- **Verificador mecánico** (`herramientas/verificar_entregable.py`): estilos de título,
  numeración, andamiaje interno, markdown crudo, citas sin entrada. El final da **OK**.
- **Regla de no-anacronismo** respetada de punta a punta: cero identificadores de la
  plataforma, cero resultados propios, cero decisiones de diseño en §15/§16. El texto deja
  varas y brechas; el cruce con lo medido es de §17.5.
