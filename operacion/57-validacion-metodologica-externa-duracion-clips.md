# Validación metodológica externa — duración de clips y evaluación temporal por episodio

> **Origen (2026-07-18):** dos preguntas del director del proyecto —
> (a) ¿un dataset de clips de 12 s perjudica la estrategia de patrones de riesgo,
> o da lo mismo porque "se procesan todos los frames"?; (b) ¿30 s es una buena
> duración? — derivaron en un análisis integral de dimensionamiento y, luego, en
> una **crítica del diseño contrastada con la práctica externa** (estándares de
> videovigilancia y literatura de detección temporal). Este documento consolida
> las tres cosas: la física del problema, la duración ideal por escenario, y el
> veredicto de validez con los gaps accionables.
>
> **Insumos internos:** spec 43 (§3 matriz P1–P8, §4 `clip_gt.v2`),
> spec 41 §7 (pattern set `cr01_cr02_v2`), `docs/nucleo/08` §2.1 (severidades,
> ventanas, Tabla 35), `docs/operacion/52` (matching `evaluate-alerts` v2, bug A),
> `docs/operacion/54` (contrato GT), estado real del banco (Bloque B: 7 clips de
> 12.000 s exactos; GT de `video16_clip10` con episodio `0→11933 ms`).

---

## 1. El punto de partida: qué limita, los frames o el tiempo

Que el pipeline **procese todos los frames no rescata un clip corto**. Los frames
dan densidad de detección *espacial* (cuántas muestras del riesgo hay); las
métricas objetivo del tramo plataforma son *temporales* y se miden en segundos de
wall-clock, no en cantidad de frames. Además el **rate-gate** del media-plane
decide el FPS efectivo por corrida, así que la densidad de muestras es
independiente de la duración: lo único que compra un clip más largo es **ventana
temporal**, que es exactamente lo que las métricas consumen.

Un clip de 12 s a 30 fps tiene 360 frames pero **solo 12 s de presupuesto de
evidencia**, y ese presupuesto se gasta en serie.

### 1.1 Constantes que gobiernan el problema

| Constante | Valor | Fuente |
|---|---|---|
| Confirmación PR-01 (sin casco, alto) | 4 s (banda 3–5) | spec 41 §7 |
| Confirmación PR-02 (sin chaleco, medio) | 7 s (banda 5–10) | spec 41 §7 |
| Resolve / histéresis | 2 s (PR-01) / 3 s (PR-02) | spec 41 §7 |
| Target `t_alert-system` | 5–10 s (alto) / **10–20 s** (medio) | Tabla 35 (nucleo/08) |
| Target TTFD | < 3 s / < 10 s | Tabla 35 |
| Evento mínimo guionado | ≥ 8 s (P1) / ≥ 12 s (P2) | spec 43 §3.1 |

### 1.2 La fórmula de dimensionamiento

Todo clip que evalúa un patrón **end-to-end** debe alojar en serie:

```
D = pre-roll + evento + cola

pre-roll ≥ 3–4 s   → sin esto TTFD degenera a 0 y no se mide el onset
                     (es lo que pasa hoy en video16_clip10: episodio en t=0)
evento   ≥ lo que exija el veredicto (ver 1.3)
cola     ≥ resolve + 2 s → observar el cierre del episodio y descartar
                           alertas tardías espurias
```

### 1.3 La restricción fuerte (censura temporal)

Más restrictiva que la confirmación: para poder emitir el veredicto
"cumple/no cumple el target de `t_alert-system`", el clip debe permitir que una
**alerta lenta-pero-válida** ocurra *dentro* del clip. Si el clip termina antes de
`onset + target_superior`, no se distingue "alertó a los 18 s (pasa)" de "no
alertó nunca (falla)": el clip **censura** la medición. Eso fija el piso duro:

- **PR-01:** `onset + 10 s` dentro del clip → con pre-roll 3–4 s ⇒ **≥ 14–15 s**
- **PR-02:** `onset + 20 s` dentro del clip → con pre-roll 3–4 s ⇒ **≥ 23–24 s**

---

## 2. Duración ideal por escenario (respuesta integral)

| Escenario (spec 43 §3.1) | Presupuesto interno | **Duración ideal** | ¿12 s alcanza? |
|---|---|---|---|
| **P1** CR-01 persistente | 3 pre + 12–14 evento + 3 cola | **18–20 s** | Marginal: confirma, pero censura `t_alert>8s` y sin pre-roll real |
| **P2** CR-02 persistente | 4 pre + 18–22 evento + 3–4 cola | **25–30 s** | **No** — censura el target de 20 s |
| **P3** Transitorio no alertable | 3 pre + 2 sub-umbral + (7+2) post | **15 s** | Casi (12 s deja solo 7 s post: al límite) |
| **P4** Resolución | 3 pre + 10 evento + 10 en cuadro resuelto | **22–25 s** | **No** |
| **P5** Cumplimiento total (negativo) | ≥ ventana máx (7 s) con margen amplio | **15–20 s** | Válido pero flojo |
| **P6** Doble condición | gobierna PR-02: como P2 | **25–30 s** | **No** |
| **P7** Multi-persona (G1-demo) | coreografía de cruces + evento ≥8 s/sujeto | **25–30 s** | **No** — los cruces solos comen ~10 s |
| **P8** Entrada/salida | 3 pre + 8 ep.1 + 5 ausencia (>resolve) + 8 ep.2 + 2 cola | **26–30 s** | **No** — estructuralmente imposible en 12 s |

**Síntesis — la duración perfecta es bimodal:**

- **~15 s** para clips cuyo veredicto es *ausencia* de alerta (P3, P5).
- **~25–30 s** para clips cuyo veredicto es una alerta *medida* (P1 entra cómodo
  en 20; unificar en 25–30 simplifica el guion y no cuesta nada).

**Regla de grabación:** tomas de ~30–35 s y recorte al presupuesto del escenario.
Un solo largo de grabación, dos largos de clip. El **onset guionado en t≈3–4 s,
nunca en t=0.**

---

## 3. Validación contra la práctica externa

Se contrastó el diseño contra el único estándar gubernamental/industrial de
evaluación de sistemas de alarma por video (**i-LIDS**, UK Home Office),
**TRECVID SED** (NIST), la literatura de detección temporal de acciones
(THUMOS/ActivityNet), la de detección de inicio de acción en streaming (**ODAS**),
y la literatura específica de PPE. Fuentes en §6.

### 3.1 Lo que la práctica externa VALIDA

1. **Evaluación por episodio con matching por ventana temporal = lo que hace
   i-LIDS.** Su protocolo: una intrusión cuenta como detectada si hay **≥1 alarma
   dentro de 10 s del inicio del evento**; las alarmas extra se ignoran (se toma
   la primera). Nuestro `evaluate-alerts` v2 replica esto con la ventana
   `[start_ms + persistencia_min, start_ms + t_alert_max]` + `re_alerts`.

2. **`re_alerts` (ADR-011) corrige el defecto documentado de i-LIDS.** La crítica
   académica central a i-LIDS (survey Sensors 2022) es que **penaliza como FP toda
   alarma posterior a 10 s aunque caiga dentro de la intrusión**. Su "edge-level
   evaluation" parametrizable —propuesta como corrección— es estructuralmente
   nuestro esquema. No estamos al nivel del estándar: estamos en su versión
   corregida.

3. **Borde inferior de la ventana (excluir alarmas pre-persistencia) es una
   mejora.** i-LIDS no lo tiene → una alarma espuria justo antes del evento cuenta
   como TP. Nuestro test de gate que protege ese borde está bien puesto.

4. **Persistencia en segundos, no frames** (nucleo/08 §2.1): i-LIDS, TRECVID y
   toda evaluación por evento operan en tiempo; el survey resamplea a 5 FPS sin
   cambiar conclusiones.

5. **Negativos y sub-umbral anotados con causa:** i-LIDS estructura su librería
   con eventos "alarm" + "non-alarm" (distractores). Nuestro `sub_threshold_events`
   con `reason` es incluso más rico.

6. **El pre-roll tiene respaldo triple:** (a) i-LIDS descarta los primeros **5
   minutos** de cada video como warm-up; (b) ODAS/streaming miden latencia de
   onset con offsets temporales — imposible si el evento arranca en t=0; (c) la
   literatura de acción temporal trabaja con video *untrimmed* donde el evento es
   una fracción del clip (THUMOS: acciones de ~4–5 s en videos de ~233 s) para
   evitar sesgo. Nuestro `video16_clip10` con episodio `0→11933 ms` en clip de
   12 s es el caso de libro de ese sesgo — el **TTFD=0 ms del smoke es un
   artefacto de recorte**, no una medición.

7. **Que la literatura de PPE NO tenga nada de esto es un punto a favor de la
   tesis.** Los benchmarks de PPE (SHEL5k, GDUT-HWD, Construction-PPE, trabajos
   con YOLOv5/v10) evalúan **solo mAP/F1 por imagen y FPS** — ninguno mide
   time-to-alert, persistencia ni evaluación por episodio. Nuestro banco importa
   la metodología de los estándares de videovigilancia al dominio PPE: **aporte
   metodológico citable** (citar i-LIDS como precedente en Etapa 4).

### 3.2 Lo que la práctica externa CUESTIONA (gaps accionables)

| # | Gap | Evidencia externa | Corrección propuesta | Costo |
|---|---|---|---|---|
| **G1** | **No se puede medir tasa de falsas alarmas por tiempo (FAR/hora).** n≈12 clips de 30 s (~6 min, casi todo con evento activo) da un estimador de FP sesgado a favor: poco tiempo "aburrido", que es donde viven los FP reales. | TRECVID NDCR = P(miss) + **FA rate por unidad de tiempo**; i-LIDS evalúa sobre horas de video con distractores. | Agregar **1–2 clips "soak" de 5–10 min** de obra en cumplimiento/actividad normal (`negative: true`) y reportar **FAR/hora** como métrica separada. | ≈0 anotación; **mayor retorno del banco** |
| **G2** | **P50/P95/P99 no cierran con el n del banco** para métricas por-episodio: ~10–14 episodios totales ⇒ un P95 es el máximo de la muestra disfrazado. | Estadística básica; los percentiles de la Tabla 35 tienen sentido para métricas por-frame (G2A), no por-episodio. | Declarar el régimen: **percentiles solo para métricas por-frame/por-unidad**; para las por-episodio, **mediana + rango + listado completo** de la muestra. | Redacción |
| **G3** | **Distractores/confusables semánticos casi ausentes** de la matriz C.2 (solo variables de captura: resolución, distancia, luz, oclusión). | i-LIDS guiona fuentes de confusión (animales, sombras). Para OVD la confusión semántica es más crítica: gorra≠casco, campera naranja≠chaleco, casco en la mano. | Agregar escenario **P9 "confusables"**; alimenta además los argumentos A1–A5 de la defensa (nucleo/09). | 1–2 clips |
| **G4** | **Bug A del matching greedy** (deflación de recall en P8 con ventanas solapadas) pasa de "pendiente" a **bloqueante** al scorear P8 reales. | El fix correcto (matching bipartito óptimo) es literalmente cómo TRECVID alinea alarma↔evento. | Implementar matching bipartito antes de scorear P8 reales (ya identificado en operacion/52 §bug A). | Implementación acotada |

**Nota (a favor):** la tolerancia de borde de anotación que el survey agrega
(npre/npost de 1–5 frames, porque marcar el frame exacto de inicio es imposible)
en nuestro caso está **absorbida** por el borde inferior `start_ms +
persistencia_min`: con ventanas de 3000+ ms, un jitter de ±2 frames es ruido. No
hace falta agregar nada; conviene **declararlo explícitamente** en el contrato GT
para mostrar que se consideró.

---

## 4. Implicancias para el banco actual (Bloque B, los 12 s)

1. **Los 7 clips de 12 s no están mal: están mal *ubicados*.** Sirven como
   P1-marginales, P3 y P5/negativos. **No** pueden sostener P2, P4, P6, P8.
2. **El defecto real hoy no es la duración sino el recorte sin pre-roll:**
   `video16_clip10` tiene el evento en `0→11933 ms` ⇒ TTFD=0 por construcción.
   **Regla de recorte del Bloque B:** ventanear el corte del video fuente para que
   el **onset caiga en t≈3–4 s**, y estirar a 20–25 s donde la fuente lo permita.
3. **Costo de pasar de 12→30 s es bajo:** el GT v2 es *temporal por episodio*
   (start/end ms), no cajas por frame; el costo por-frame solo pega en los P7
   subject-level (2–3 clips). El extra real es inferencia (~2.5× frames/clip),
   despreciable a la escala del banco (n≈12).

---

## 5. Recomendación cerrada

- **Bloque A (grabación propia):** tomas de ~30–35 s; clips finales de **25–30 s**
  (P1, P2, P4, P6, P7, P8) y **15 s** (P3, P5). **Onset guionado en t=3–4 s,
  siempre.**
- **Bloque B (recortes Intel):** re-ventanear con onset en t≈3–4 s; estirar a
  20–25 s donde la fuente lo permita; los que queden en 12 s se etiquetan solo
  como P1-diagnóstico / negativos.
- **Regla declarable en el contrato GT (una línea, falsable por el validador de
  `clip_gt.v2`):**
  > *duración del clip ≥ pre-roll (3 s) + (onset→target superior de
  > `t_alert-system` del patrón más lento presente) + resolve + 2 s; el onset del
  > primer episodio nunca en t=0.*

  Chequeo automático: `episodes[0].start_ms ≥ 2000` **y**
  `duration_ms ≥ episodes[0].start_ms + target_upper + resolve + 2000`.
- **Cuatro correcciones metodológicas, por retorno decreciente:** (1) clips soak
  para FAR/hora [G1]; (2) declarar régimen estadístico por métrica [G2];
  (3) re-ventanear Bloque B [banco]; (4) escenario P9 confusables [G3]. Más el fix
  bipartito [G4] cuando toque P8.

### 5.1 Veredicto de validez

Lo desarrollado **es válido y tiene sentido**: la estructura
episodio/ventana/`re_alerts`/sub-umbral reproduce (y en dos puntos **mejora**) el
único estándar industrial existente (i-LIDS), y las duraciones 15 / 25–30 s
derivadas son coherentes con la restricción de censura temporal que ese estándar
también encierra. El diseño está **mejor alineado con la práctica de estándares de
videovigilancia que la propia literatura de PPE**, que ignora la dimensión
temporal. Las debilidades son las cuatro de §3.2, todas corregibles a bajo costo.

---

## 6. Guía de generación del banco E-OVRT — duración óptima para métricas concluyentes

> Esta sección baja todo lo anterior a **nuestra** situación concreta: estamos
> **grabando/recortando el dataset ahora**, con nuestro pattern set
> `cr01_cr02_v2` (PR-01 = 4000 ms, PR-02 = 7000 ms) y nuestras 5 métricas
> (spec 43 §10). La pregunta operativa es: **¿qué duración hace que el banco
> produzca métricas buenas, medibles y defendibles para cerrar el trabajo?**

### 6.1 Principio rector: la duración correcta no infla resultados, los hace *justos*

Un clip mal dimensionado **distorsiona la métrica en las dos direcciones**, y
ninguna de las dos sirve para concluir:

- **Demasiado corto ⇒ subestima un buen sistema.** Si el evento arranca en t=0 no
  hay onset que medir y el **TTFD colapsa a 0** (artefacto — es literalmente lo que
  pasó en `video16_clip10`). Si el clip termina antes de `onset + target_superior`,
  una alerta válida-pero-lenta se cuenta como `missed` ⇒ **recall artificialmente
  bajo**. Mostraríamos números peores que el sistema real.
- **Demasiado "limpio"/sin tiempo muerto ⇒ sobreestima.** Casi todo el clip con el
  evento activo deja **poco tiempo "aburrido"**, que es justo donde aparecen los FP
  ⇒ **precision artificialmente alta**. Mostraríamos números mejores que los
  operativos, y un tribunal atento lo desarma.

La duración óptima es la que **elimina ambos artefactos**: entonces cada número que
mostramos es atribuible al sistema, no al recorte. Ese es el sentido de "buenas
métricas para concluir": **métricas no-censuradas y no-sesgadas**, no métricas
maquilladas.

### 6.2 Qué exige cada una de nuestras 5 (+1) métricas

| Métrica (spec 43 §10) | Qué necesita del clip | Piso de duración | Riesgo si el clip es corto |
|---|---|---|---|
| **Recall** (episodio detectado) | que la alerta quepa: `onset + t_alert_max` dentro del clip | PR-01: onset+10 s · PR-02: onset+20 s | `missed` espurio ⇒ recall bajo falso |
| **Precision / FP** | tiempo sin evento donde el sistema *podría* equivocarse | cola ≥ resolve+2 s **y** clips soak (§3.2 G1) | sin tiempo muerto ⇒ precision alta falsa |
| **TTFD** (onset→1ª detección) | **pre-roll real** (evento NO en t=0) + margen hasta el target | pre-roll ≥ 3 s + TTFD_max (3 s alto / 10 s medio) | TTFD=0 artefacto; no se mide latencia |
| **SDR** (proporción del intervalo con detección sostenida) | un **intervalo de evento largo** para que la proporción sea estable | evento ≥ 8 s (alto) / ≥ 12 s (medio) | SDR ruidoso: 1–2 frames mueven el valor |
| **t_alert-system** (onset→alerta registrada) | que la alerta más lenta admisible ocurra dentro del clip | = recall (onset + target_superior) | censura: no se distingue "lento OK" de "nunca" |
| **FAR/hora** (propuesta G1) | **volumen de tiempo en cumplimiento** | clips soak 5–10 min | sin soak, no hay denominador temporal |

Lectura directa: el par **(SDR, TTFD)** empuja el evento a ser **largo y con
pre-roll**; el par **(recall, t_alert-system)** fija el **piso duro** de
`onset + target_superior`; **(precision, FAR)** exige **cola + clips soak**. Las
tres presiones combinadas dan la duración bimodal de §2, ahora justificada
métrica-por-métrica.

### 6.3 Plantillas de clip (timeline para grabar/recortar)

Dos plantillas cubren el 90 % del banco. Los tiempos son del **timeline real del
video** (spec 43 §3.3: el GT sale del video, no del plan); el operador guiona
contra estos marcadores.

**Plantilla ALTA — PR-01 sin casco (P1), duración objetivo 20 s**

```
0–3 s    pre-roll: persona en cumplimiento (con casco) → mide baseline, habilita TTFD
3 s      ONSET: se quita el casco  ────────────────────────┐  episodio CR-01 start_ms≈3000
3–4 s    (media-plane confirma a onset+4000 = t≈7 s)       │
3–17 s   infracción sostenida (≥14 s) → SDR estable,       │  evento ≥ 8 s exigido; 14 s cómodo
         alerta lenta admisible cabe (onset+10 s = t≈13 s) │
17 s     END: vuelve a ponerse el casco  ─────────────────┘  episodio end_ms≈17000
17–20 s  cola: en cumplimiento (>resolve 2 s) → cierre por resolve, sin alertas tardías
```

**Plantilla MEDIA — PR-02 sin chaleco (P2), duración objetivo 30 s**

```
0–4 s    pre-roll: persona con chaleco → baseline + TTFD
4 s      ONSET: se quita el chaleco  ───────────────────────┐  episodio CR-02 start_ms≈4000
4–11 s   (media-plane confirma a onset+7000 = t≈11 s)        │
4–26 s   infracción sostenida (≥22 s) → SDR estable,         │  evento ≥ 12 s exigido; 22 s cómodo
         alerta lenta admisible cabe (onset+20 s = t≈24 s)   │
26 s     END: se pone el chaleco  ──────────────────────────┘  episodio end_ms≈26000
26–30 s  cola: en cumplimiento (>resolve 3 s) → cierre por resolve
```

Los demás escenarios se derivan de estas dos: **P3/P5** (negativos/transitorio) se
recortan a **~15 s** (no hay alerta que medir, solo hay que observar ≥1 ventana de
confirmación completa post-estímulo); **P4** alarga la cola a ≥10 s; **P6** usa la
plantilla MEDIA con dos episodios solapados; **P7** parte de MEDIA y suma la
coreografía de cruces; **P8** inserta una ausencia de >resolve entre dos eventos.

### 6.4 Composición del banco para que el n dé conclusiones

No alcanza con la duración por clip; el **número de episodios** decide si las
métricas concluyen (§3.2 G2). Objetivo mínimo defendible:

| Bloque | Contenido | Duración/clip | Aporte a métricas |
|---|---|---|---|
| Clips de alerta | ≥2 P1, ≥2 P2, 1 P4, 1 P6, 2–3 P7, 1 P8 | 20–30 s | recall, t_alert, SDR, TTFD (n≈12–15 episodios) |
| Clips de ausencia | ≥1 P3, ≥1 P5 (=V3), 1 P9 confusables | ~15 s | precision (FP verdadero vs sub-umbral) |
| **Clips soak** (G1) | 1–2 tomas de obra normal en cumplimiento | **5–10 min** | **FAR/hora** (denominador temporal real) |

Con esto: las métricas por-episodio se reportan como **mediana + rango + muestra
completa** (no P95, §3.2 G2); FAR/hora sale de los soak; precision sale de
ausencia+soak, no de los clips de alerta.

### 6.5 Dónde se juega la duración en el pipeline de generación

Los puntos del pipeline del video-gt-lab (doc 54) donde esto se materializa:

1. **`prepare_clip.sh` (recorte a CFR):** es acá donde se fija el pre-roll. **Regla
   de recorte: elegir el corte del fuente para que el onset del evento caiga en
   t≈3–4 s, y no antes.** Para el Bloque B (recortes Intel de 12 s), re-ventanear
   estirando a 20–25 s donde la fuente lo permita.
2. **CVAT (anotación):** el anotador marca `start_ms`/`end_ms` **reales** contra el
   video. El jitter de anotación (±1–2 frames) queda **absorbido** por el borde
   inferior `start_ms + persistencia_min` de la ventana de matching — declararlo en
   el contrato GT.
3. **`derive_clip_gt.py` + validate:** agregar el **chequeo de dimensionamiento**
   como gate del `clip_gt.v2` (falsable):
   `episodes[0].start_ms ≥ 2000` **y**
   `duration_ms ≥ episodes[0].start_ms + target_upper(patrón) + resolve + 2000`.
   Un clip que no lo cumple se marca `dimensioning_warning` en `provenance` (no
   bloquea, pero queda auditado).

### 6.6 Conclusión operativa para el banco

- **Grabar** cada escena de alerta como toma de **~30–35 s**; recortar al objetivo
  del escenario (**20 s** alto / **30 s** medio); onset en **t=3–4 s** siempre.
- **Clips de ausencia/confusables a ~15 s.** **Sumar 1–2 clips soak de 5–10 min.**
- Esta receta hace que las 5 métricas sean **no-censuradas** (buen sistema se ve
  bien) y **no-sesgadas** (FP medibles) — que es la única forma de "mostrar buenos
  resultados" que sobrevive a la defensa.

---

## 7. Fuentes

- Perimeter Intrusion Detection by Video Surveillance: A Survey (Sensors 2022) —
  protocolo i-LIDS (TP dentro de 10 s, warm-up 5 min, crítica al conteo de FP),
  edge-level evaluation. https://pmc.ncbi.nlm.nih.gov/articles/PMC9104546/
- i-LIDS User Guide (UK Home Office).
  https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/143875/ilids-user-guide.pdf
  · https://www.gov.uk/guidance/imagery-library-for-intelligent-detection-systems
  · https://ieeexplore.ieee.org/document/4105319/
- TRECVID Surveillance Event Detection (NIST) — NDCR con FA rate por unidad de
  tiempo. https://www.nist.gov/itl/iad/mig/trecvid-surveillance-event-detection-evaluation-track
- Online Detection of Action Start in Untrimmed, Streaming Videos (ECCV 2018) —
  latencia de onset con mAP por offset temporal.
  https://openaccess.thecvf.com/content_ECCV_2018/papers/Zheng_Shou_Online_Detection_of_ECCV_2018_paper.pdf
- Automated non-PPE detection… (Scientific Reports 2025)
  https://www.nature.com/articles/s41598-025-12468-8 · Nath et al., Deep learning
  for site safety (Automation in Construction 2020)
  https://www.sciencedirect.com/science/article/abs/pii/S0926580519308325 —
  evaluación PPE limitada a mAP/FPS, sin métricas temporales.
