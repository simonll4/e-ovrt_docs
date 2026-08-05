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
y la literatura específica de PPE. Fuentes en §8.

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

> **✎ Enmienda 2026-08-04 a la fila G1 (doc 90 D-90.1 + registry `clip_bench.md` L1).**
> Dos correcciones medidas en la práctica: **(1)** la estimación de esfuerzo
> *"≈0 anotación"* del material soak es **falsa** — un soak de obra en cumplimiento
> tiene gente en cuadro, y certificar que *nadie* viola exige trackear a todos frame a
> frame (el clip de 6,2 min llevó más de una jornada; el `--allow-empty` de
> `derive_clip_gt` cubre el caso contrario, clips *sin* personas). **(2)** Con el
> material alcanzable (0,10–0,26 h) la cota superior de FAR/hora queda en 11–30 FA/h,
> que no sostiene ninguna afirmación operativa → **FAR/hora se declara limitación
> (L1) y no se reporta como métrica de rendimiento**; la evidencia de falsas alarmas
> del informe es el **control de negativos por campaña** (evidencia comparativa
> pareada entre combinaciones, no una tasa absoluta). La mecánica pre-registrada no
> cambia: el agregador ya emitía `far_per_hour: null` sin soak, con la base declarada.

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
| Clips de ausencia | ≥1 P3, ≥1 P5 (=V3) | ~15 s | precision (FP verdadero vs sub-umbral) |
| Clips confusables (P9) | 1–2 | **18–20 s** (rige el floor de episodio CR-01: 3+10+2+2=17 s) | **recall bajo estrés semántico** — ✎ corrección 07-19: gorra sin casco / campera naranja sin chaleco **SON infracciones reales** (GT con episodio); el confusable testea si el modelo **pierde** la alerta (falso cumplimiento), no FP |
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
   **Implementado (A1, 2026-07-19):** `dimensioning_warnings(gt)` en
   `derive_clip_gt.py` computa el floor **por episodio** — cada episodio con su
   propio `start_ms` y el `target_upper`/`resolve` de *su* condición — no un único
   floor sobre `episodes[0]`. Es estrictamente más estricto (nunca omite un caso
   que la fórmula de un solo floor marcaría, porque `episodes[0].start_ms` es el
   mínimo) y atribuye la advertencia al episodio afectado, alineado con el
   `metric_censored` per-episodio del evaluador (A2). Va en
   `provenance.dimensioning_warnings` + aviso en el timeline impreso.

### 6.6 Conclusión operativa para el banco

- **Grabar** cada escena de alerta como toma de **~30–35 s**; recortar al objetivo
  del escenario (**20 s** alto / **30 s** medio); onset en **t=3–4 s** siempre.
- **Clips de ausencia a ~15 s; confusables (P9) a 18–20 s** (✎ 07-19: P9 es
  infracción real, rige su floor). **Sumar 1–2 clips soak de 5–10 min.**
- Esta receta hace que las 5 métricas sean **no-censuradas** (buen sistema se ve
  bien) y **no-sesgadas** (FP medibles) — que es la única forma de "mostrar buenos
  resultados" que sobrevive a la defensa.

### 6.7 Banco estratificado: mezcla de duraciones y censura por métrica

**Contexto real (2026-07-18):** los videos públicos de obra disponibles rondan los
12 s; los >20 s escasean. **Esto no compromete el banco**, por dos razones:

1. **Los largos no dependen de internet.** El núcleo de veredicto temporal es el
   Bloque A (grabación propia, §6.3) — ahí la duración la controlamos nosotros.
   Internet/Intel es el Bloque B, cuyo rol declarado es *complementar* con
   diversidad, no sostener veredictos temporales.
2. **La censura es por métrica y por patrón, no por clip.** Un clip corto no es
   inválido: es válido para un subconjunto de métricas. Lo que aporta un 12 s
   re-ventaneado (onset en t≈2–3 s):

| Métrica | PR-01 (alto) | PR-02 (medio) |
|---|---|---|
| TTFD (<3 s / <10 s) | ✅ sobra ventana | ⚠️ marginal (~9–10 s post-onset) |
| t_alert-system (≤10 / ≤20 s) | ⚠️ marginal (observa hasta onset+9–10 s) | ❌ censurado |
| SDR | ✅ sobre el intervalo anotado | ⚠️ intervalo corto ⇒ ruidoso |
| Recall/precision de alertas | ⚠️ solo si la alerta cabe | ❌ un miss no es concluyente |
| Negativos / P3 | ✅ | ✅ |
| Diversidad C.2 | ✅ | ✅ |

**El mecanismo que evita la contaminación ya existe:** los estados de
aplicabilidad de `evaluate-alerts` (ADR-006). Extensión propuesta: estado
**`metric_censored`** — el clip es demasiado corto para que el veredicto de esa
métrica/patrón sea concluyente ⇒ el episodio **sale del denominador** de esa
métrica en vez de contarse como `missed`. La condición es computable con el mismo
gate de §6.5.3 evaluado **por métrica** (`duration_ms ≥ start_ms + target_upper +
resolve + 2000`, con el `target_upper` de cada métrica). El reporte declara el n
por métrica: *"t_alert PR-02: n=X episodios evaluables (clips ≥29 s)"*.

**Dos reglas duras:** (a) **no concatenar cortos** para fabricar un largo — el
corte de escena crea onsets artificiales y rompe la semántica del episodio;
(b) **P2/P4/P6/P8 no se rellenan con cortos**: si faltan, se graban (Bloque A).

Resultado: 10 largos + relleno de cortos no es un banco degradado sino
**estratificado** — largos para veredictos temporales, cortos para diversidad y
especificidad, denominadores limpios por aplicabilidad.

### 6.8 Dimensionamiento del banco para el equipo real (3 personas, defensa ~sept)

La cantidad óptima se fija por **episodios evaluables por patrón** (~8–10 por
patrón para que mediana+rango sea defendible), no por cantidad de videos. El
recurso escaso son los **episodios PR-02-evaluables** (exigen clips ≥29 s).

| Bloque | Contenido | Cant. | Duración | Origen |
|---|---|---|---|---|
| A — núcleo guionado | 2 P1, **3 P2**, 1 P3, 1 P4, 1 P5(=V3), 1 P6, 2 P7, 1 P8, 1 P9 | **13** | 15–30 s según rol | grabación propia, **una jornada** |
| C — defensa | V1, V2 (V3=P5) | 2 | 20–30 s | misma sesión |
| B — relleno | P1-diagnóstico, negativos, diversidad | 5–8 | 12–15 s re-ventaneados | internet/Intel |
| Soak (G1) | obra normal en cumplimiento | 1–2 | **5–10 min** | trípode y dejar correr |

**Total ≈ 21–25 clips**, que rinden: PR-01 ~9–10 episodios (P1×2 + P4 + P6 +
P7×2 + P8×2 — P8 aporta 2 porque la salida/reentrada corta el episodio), PR-02
~4–5 (P2×3 + P6 — por eso P2 sube de 2 a 3: es el denominador más flaco y la toma
extra cuesta 2 min de rodaje), TTFD n≈15+, precision/FAR de ausencia+soak.

**Esfuerzo para 3 personas:** rodaje = media jornada (1 cámara/director con el
timeline planificado, 2 actores; P7 necesita 2–3 en cuadro — rotan). **Grabar 2
tomas por guion** y promover la mejor (toma de respaldo para la demo, doc 09).
Anotación = 2–3 tardes (GT temporal por episodio ~10–15 min/clip salvo los P7
subject-level); la doble anotación ≥20% (mín. 3 clips) sale cruzándose entre dos
con el tercero de árbitro.

**No ir más allá de ~25:** de 22 a 35 clips ninguna conclusión cambia (la mediana
sobre n=15 vs n=25 episodios se mueve poco) pero la anotación se duplica — y el
cuello real del proyecto es la pasada humana en CVAT (todo el GT sigue
`gt_preliminary`). **Piso de seguridad:** el spec 43 declara n≥8 válido con A+C
solamente — el plan tolera ~40% de caída del rodaje sin comprometer validez.

### 6.9 Rol de los videos de internet: especificidad sí, recall no

Si los videos públicos muestran obras **en cumplimiento** (todos con casco y
chaleco), **no sirven para recall**: recall = episodios detectados / episodios
existentes, y un video en cumplimiento tiene **0 episodios** — no aporta al
numerador ni al denominador. La sensibilidad solo se mide con eventos; la
especificidad solo con no-eventos; ningún clip paga por el otro lado.

Pero NO se descartan — son exactamente **la mitad del banco que no se puede
guionar fácil**:

| Aporte | Métrica que alimenta |
|---|---|
| P5/negativos | precision (¿alucina `bare_head` donde no hay?) |
| **Soak / FAR-hora (G1)** | el denominador temporal de FP — lo más caro de conseguir actuado |
| Confusables naturales (gorras, camperas naranjas, cascos colgados) | material P9 gratis |
| Diversidad C.2 | robustez visual que el rodaje único no tiene |

División limpia y defendible del banco: **positivos guionados y controlados
(Bloque A) / negativos reales y salvajes (internet)** — los negativos salvajes son
más duros contra el sistema que negativos actuados.

**Minado de positivos con la propia plataforma:** antes de rendirse con los
positivos de internet, pasar los videos largos por el media-plane con prompts
`bare_head`/sin-chaleco como **prefiltro** y revisar a ojo solo los segmentos
candidatos. Una infracción real no actuada vale oro (episodio de validación
externa, no guionado); si no aparece ninguna, el costo fue casi nulo.

---

## 7. Frontera de atribución: métricas de la detección vs métricas del sistema completo

> **Análisis 2026-07-19.** El diccionario de métricas (spec 40 §5.1, del informe
> §17.1.7 + Tablas 35/D.4) define bien cada métrica pero **nunca declara a qué
> componente se atribuye cada una**. Sin esa atribución, un resultado malo no dice
> *qué* arreglar y un resultado bueno no dice *qué* defender. Esta sección traza
> la frontera, critica el uso que el informe insinúa y fija la decisión.

### 7.1 La frontera ya está trazada — solo hay que declararla

La identidad del spec 40 §5.2.2 **es** la frontera:

```
t_alert-system  =  TTFD  +  t_capture→alert
                   ─────    ────────────────
                 DETECCIÓN     PLATAFORMA
              (media-plane +  (bus + persistencia
               prompt/modelo)  + motor + registro)
```

El punto de corte es **el frame de primera evidencia positiva** (el `t1` de TTFD
se define en su instante de captura — spec 40 §5.2.2). Todo lo que ocurre *antes*
de que ese frame exista (que el modelo vea la condición, con qué prompt, cuán
rápido, cuán sostenido) se atribuye a la **detección**; todo lo que ocurre
*después* (bus, ventana de persistencia, motor, registro) se atribuye a la
**plataforma**. La identidad hace la frontera verificable numéricamente.

### 7.2 Decisión: tres canastas

**Nivel A — Detección (media-plane + estrategia de prompts):**

| Métrica | Banco | Qué mide |
|---|---|---|
| AP@0.5 por clase, recall CR-01 | BENCH imágenes (196) | calidad espacial zero-shot (gate; ya corrido en Sprint 2) |
| **TTFD** | banco temporal | reactividad de la detección al onset |
| **SDR** | banco temporal | sostenimiento de la detección en el episodio |
| G2A + sub-etapas (P50/P95/P99), FPS efectivo, drops, drop-rate prefilter EN-2 | toda corrida | costo computacional |

**Nivel B — Sistema completo (por episodio, contra GT temporal):**

| Métrica | Qué mide |
|---|---|
| P/R/F1 de alertas + re-alertas / inesperadas / sub-umbral alertadas | corrección end-to-end (análisis de errores R3) |
| **t_alert-system** (principal, vs Tabla D.4) | latencia end-to-end oficial |
| t_capture→alert / t_compute-budget (derivadas propias) | descomposición: cuánto es plataforma, cuánto persistencia |
| **FAR/hora** (sobre soak, §3.2 G1) | tasa de falsas alarmas operativa |

**Condicionales / excluidas (ADR-006 — con estado y causa, nunca omitidas):**
`t_alert-notification` → solo con spec 45 implementado (para lo último);
`ΔFP_tracker` → solo labs G1 con tracker (en la plataforma G0: excluida con
causa); TTFA interna → diagnóstico, no se reporta como resultado.

**Regímenes de reporte (cierra G2):** Nivel A por-frame/por-unidad ⇒ percentiles
P50/P95/P99; TTFD/SDR y todo Nivel B son por-episodio ⇒ **mediana + rango +
muestra completa**, con n declarado por métrica (§6.7). Gate de validez de
corrida (no son métricas): `bus_dropped_events`, warm-up declarado,
`source_clock`.

### 7.3 Crítica al informe (correcciones para Etapa 4)

1. **`t_alert-system` NO sirve para comparar modelos/estrategias (D1)** — y el
   informe no lo advierte. Está dominada por la constante de persistencia
   (4000/7000 ms), idéntica entre corridas comparadas: dos modelos con TTFD 0.5 s
   vs 2.5 s dan t_alert ~4.5 vs ~6.5 s — la diferencia relativa se aplasta. **El
   discriminante de D1 es TTFD/SDR/AP (Nivel A); `t_alert-system` valida la
   plataforma con modelo fijo (Nivel B).** Cruzarlos es un error metodológico
   señalable por el jurado.
2. **La matriz diagnóstica SDR×recall es el retorno de la separación** (hoy no
   escrita en ningún lado):

   | | recall alto | recall bajo |
   |---|---|---|
   | **SDR alto** | ✅ todo sano | ⚠️ **plomería**: bus/matching/motor pierde lo que la detección ve |
   | **SDR bajo** | ✅ **motor robusto a huecos** de detección (resultado defendible) | ❌ la detección no ve la condición (modelo/prompt) |

   Más: TTFD alto ⇒ modelo/prompt lento en ver; t_compute-budget alto ⇒ overhead
   de plataforma. Cuatro diagnósticos distintos, **cero instrumentación extra**
   (todo sale de `detections.jsonl` + `alerts.jsonl`, que ya son la verdad).
3. **No mezclar bancos:** AP@0.5 vive en el BENCH de imágenes; TTFD/SDR/t_alert
   viven en el banco temporal. Datasets distintos, roles distintos (gate espacial
   vs evaluación temporal); el informe debe presentarlos como niveles, no como un
   pool único de métricas.

### 7.4 Definición cerrada (2026-07-19) y protocolo de dos etapas

Formulación definitiva de los dos niveles — **Nivel A responde "¿el modelo OVD ve
la condición?"; Nivel B responde "¿la plataforma alerta cuando debe y calla
cuando debe?"**:

**Nivel A — Rendimiento de los modelos OVD (media-plane).**

| Métrica | Banco | Qué responde del modelo |
|---|---|---|
| AP@0.5 por clase (`person`,`helmet`,`vest`,`bare_head`) | BENCH imágenes (196) | ¿localiza bien las clases? |
| Recall espacial CR-01 | BENCH imágenes | ¿ve la condición cuando está en el frame? |
| TTFD | banco temporal | ¿cuánto tarda en verla desde el onset? |
| SDR | banco temporal | ¿la sigue viendo sostenido o parpadea? |
| G2A, FPS efectivo, drops | toda corrida | ¿a qué costo? |

*Regla de uso:* comparar **modelos/estrategias de prompts** (D1: E-DIR vs E-IND;
GDINO-tiny vs base) con la **plataforma congelada** (umbrales 4000/7000, motor y
clips idénticos). Solo varía el modelo/prompt.

**Nivel B — Comportamiento de alertado de la plataforma.**

| Métrica | Qué responde de la plataforma |
|---|---|
| Recall de episodios | ¿alerta cuando debe? |
| Precision + FAR/hora (soak) | ¿da falsas alertas? (conteo y tasa operativa) |
| P3/P5 en cero alertas | ¿calla cuando debe? — **P3 es la prueba pura de la lógica de persistencia**: el modelo VE la infracción sub-umbral y la plataforma igual NO debe alertar (✎ 07-19: P9 salió de esta fila — es infracción real, mide recall bajo confusables, Nivel A) |
| t_alert-system (vs Tabla D.4) | ¿alerta a tiempo para la severidad? |
| t_compute-budget | ¿cuánto es overhead nuestro vs persistencia declarada? |
| re_alerts / inesperadas / sub-umbral alertadas | análisis de errores R3 |

*Regla de uso:* validar la **plataforma** con el **modelo fijo** (el ganador del
Nivel A). Solo varía la configuración de plataforma.

**Protocolo de dos etapas (decisión operativa):**

1. **Etapa A — elegir el modelo:** correr candidatos sobre ambos bancos; comparar
   por AP/TTFD/SDR/G2A; sale un ganador o el trade-off explícito (calidad vs FPS).
2. **Etapa B — validar la plataforma:** congelar ese modelo; correr banco completo
   + soak; reportar recall/precision/FAR/t_alert contra Tabla 35/D.4.

**Valor para la defensa:** ante el ataque "el modelo detecta mal" (p. ej.
`bare_head` débil, conocido del Sprint 2), la respuesta es: *eso es Nivel A,
medido y declarado; la tesis se juzga en Nivel B — la plataforma alerta
correctamente dado lo que el modelo ve (matriz SDR×recall, §7.3.2)*. La
separación convierte la debilidad conocida del modelo en un **resultado medido**
en vez de una vulnerabilidad.

### 7.5 Alineación con el informe: dependencia métrica↔material y qué debe declarar Etapa 4

**Principio explícito: cada métrica depende del material que el banco consiga.**

| Métrica | Material del que depende | Escasez real |
|---|---|---|
| AP@0.5 / recall espacial | BENCH imágenes (196) | ✅ ya existe |
| TTFD, SDR | clips con pre-roll + evento largo | media (rodaje propio) |
| Recall, t_alert PR-01 | episodios en clips ≥17–20 s | media |
| Recall, t_alert **PR-02** | episodios en clips **≥29 s** | 🔴 la más escasa — solo rodaje propio |
| Precision | negativos + confusables + cola | baja (internet ayuda) |
| **FAR/hora** | tiempo soak (5–10 min obra normal) | 🔴 hoy **cero material** |

El seguro ante material insuficiente: aplicabilidad + `metric_censored` (§6.7) —
una métrica con poco material se reporta con n reducido o censurada, **nunca se
fabrica**.

**Veredicto de alineación (chequeado contra nucleo/08, 2026-07-19): sin
contradicciones.** Todo el doc 57 se *deriva* de las constantes del informe
(Tablas 24/35/D.4, t0=inicio anotado, C.2, doble anotación); el informe **nunca
fijó duraciones de clips ni composición del banco** — este doc llena un hueco, no
pisa una definición. Pero Etapa 4 debe hacer **cinco declaraciones**:

1. **FAR/hora** es derivada propia (no del §17.1.7) — declararla con el mismo
   estatuto epistemológico que `t_capture→alert` (spec 40 §5.2: "no sustituye,
   descompone/complementa"). Motivación citable: TRECVID NDCR / i-LIDS.
2. **Régimen estadístico (G2):** el "P50/P95/P99 + promedio" del informe se
   cumple para métricas por-frame; para las por-episodio (n≈10–15) rige
   mediana+rango+muestra — amparado por la **cláusula del propio informe**
   (§17.1.5.4.2: piso ~200 instancias *o* "tamaño efectivo + intervalos de
   confianza"). Citar la cláusula, no pedir perdón.
3. **`metric_censored`** — extensión de ADR-006; el informe no contempla censura
   por duración porque no fijó duraciones.
4. **P9 confusables + clips soak** — adiciones a la matriz C.2 (que solo tiene
   variables de captura), declaradas como extensión de la campaña EBE.
5. **"t_alert-system no compara modelos"** (§7.3.1) es crítica nuestra, no está
   en el informe — escribirla. Chequeo asociado: verificar que el pre-registro D1
   (doc 04) no la use como criterio de comparación **antes de correr D1** (por
   nucleo/08 §2.3 el protocolo D1 trabaja con métricas espaciales y ejes de
   prompts, así que probablemente ya está bien — verificar igual).

**Lo que el desarrollo preliminar no había registrado (honesto):**

- **El piso de ~200 instancias positivas** (§17.1.5.4.2) nunca se cruzó con el
  banco de video. Resolución: el piso aplica a evaluación **espacial/de prompts**
  (instancias por frame — lo cubren el BENCH de imágenes y los miles de frames de
  los clips), **no** a episodios; las por-episodio van por la vía "n efectivo +
  IC". Sin esta distinción explícita, se podría leer que el banco necesita 200
  episodios — inviable y falso.
- **El Bloque B se recortó a 12 s sin pre-roll** antes de que existiera la regla
  de dimensionamiento (de ahí el TTFD=0 artefactual). La regla ahora existe y el
  gate la hace falsable.
- **El denominador FAR quedó en cero** porque nadie derivó que precision sobre
  clips guionados no alcanza — hasta la validación externa (§3.2 G1).

### 7.6 Principio rector del cierre (decisión del equipo, 2026-07-19)

**El núcleo validable se cierra con las métricas que el material efectivamente
cubra — la cobertura decide el conjunto final de métricas reportadas, no al
revés.** En concreto:

1. **Ninguna métrica bloquea el cierre.** Una métrica cuyo material no se
   consiguió (o quedó corto) se reporta con su estado de aplicabilidad y causa
   (ADR-006 + `metric_censored`, §6.7) — jamás detiene la entrega ni se fabrica.
2. **La dirección del ajuste es material→métrica, no métrica→material.** Primero
   se releva qué clips/escenas se pudieron obtener (tabla §7.5); recién entonces
   se fija qué métricas entran al reporte final con qué n. Todo lo que choque
   entre lo planeado y lo implementado **se corrige ahora, en este cierre** — no
   se arrastra.
3. **La prioridad de adquisición se ordena por métricas desbloqueadas por unidad
   de esfuerzo:** hoy eso significa (a) tomas P2 largas (desbloquean el
   denominador PR-02 completo: recall + t_alert + SDR medio) y (b) footage soak
   (desbloquea FAR/hora, la única métrica con material en cero). Un clip que no
   desbloquea ninguna métrica nueva no se prioriza.
4. **El reporte declara la cobertura como resultado, no como disculpa:** "estas
   métricas se cierran con este n y este material; estas otras quedan declaradas
   `censored`/`not_applicable` con causa" — formato ya soportado por el evaluador
   (ADR-006) y coherente con la cláusula "n efectivo + IC" del informe
   (§17.1.5.4.2, cuyo piso de ~200 aplica a **instancias/imágenes** del plano
   espacial, no a episodios).

Este principio gobierna las decisiones de banco y reporte de aquí al cierre; los
docs 55/56 (guía de desarrollo) lo referencian.

---

## 8. Fuentes

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
