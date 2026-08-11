# Etapa 1 — ajustes a la fundamentación teórica (§15 Estado del Arte, §16 Marco Teórico)

> **Estado (2026-08-10):** relevado, **sin pase de correcciones aplicado**. El
> relevamiento salió de contrastar el §15 del informe contra fuentes primarias
> fetcheadas y contra nuestra propia evidencia medida (`sintesis/resultados-y-conclusiones.md`
> §7, relevamiento del 2026-08-06). El §16 (Marco Teórico) **no fue relevado todavía**
> — es `AJ-1.16`, y es un hueco declarado, no un "no hay nada que cambiar".
>
> **Marca de confianza de las cifras externas**, tal como la fija la fuente:
> **[P]** verificada en fuente primaria · **[S]** fuente secundaria oficial ·
> **[R]** circulante sin verificar.

| Dónde | Qué |
|---|---|
| Texto actual | `entregable/96c` (§15 Estado del Arte) · `entregable/96d` (§16 Marco Teórico) · `entregable/96e` §19.1 (Anexo A, Tabla A.1) |
| Fuente del relevamiento | `sintesis/resultados-y-conclusiones.md` §7.1–§7.4 |
| Teoría de apoyo para redactar | `sintesis/fundamentos-teoricos.md` |

---

## 1. Por qué esta etapa no se puede saltear

El §17.5 (Etapa 5) va a reportar **mAP@0,5 0,551 agregado** sobre `bench_v3`. Un número
así, sin vara, no significa nada para un jurado — y hoy **el §15 no da la vara**: cita
SHEL5K, CHV y SH17 únicamente como datasets, sin reportar ni una cifra de mAP de la
literatura supervisada. Toda la defensa pivotea sobre ese contraste ("~63% del techo
sin entrenar"), y el contraste se construye acá.

Los dos primeros ajustes son, por eso, los únicos 🔴 de esta etapa.

---

## 2. Tablero de ajustes

| ID | Sección | Tipo | Pri | Enunciado |
|---|---|---|---|---|
| **AJ-1.01** | §15 | CONCRETA | 🔴 | **Hueco 1: falta la línea base de EPP supervisado.** Incorporar la Vara 1 con cifras, o declarar la ausencia como brecha. |
| **AJ-1.02** | §15 / Tabla 3 | CONCRETA | 🔴 | **Hueco 2: el estado del arte y la evidencia propia no se cruzan nunca.** |
| **AJ-1.03** | §15 | ERRATA | 🟠 | El 52,5 AP de GDINO es del backbone **Swin-L** y el informe nunca lo declara; lo desplegado acá es **Swin-T**. |
| **AJ-1.04** | §15 / tablas | ERRATA | 🟡 | OmDet-Turbo-Tiny "30,3 LVIS" (probable *mislabel* de ODinW-13) y 34,0 vs 34,7 entre tablas. |
| **AJ-1.05** | §15 | ERRATA | 🟡 | El 53,4 COCO de OmDet-Turbo probablemente **no es zero-shot**. |
| **AJ-1.06** | §15 | ERRATA | 🟡 | LLMDet "51,1–52,4": el 52,4 no tiene origen. |
| **AJ-1.07** | §15 | ERRATA | 🟡 | El caching "ahorra ≈40 ms" en un modelo al que la misma tabla asigna **7,1 ms totales**. |
| **AJ-1.08** | Tabla 3 | PRECISA | 🟡 | La columna Latencia es **1000/FPS**: derivada, no medida. Declararlo. |
| **AJ-1.09** | Anexo A / Tabla A.1 | ERRATA | 🟠 | GDINO 1.5 y DINO-X figuran como "Apache-2.0" siendo **API cerrada sin pesos abiertos** (la licencia es del SDK). |
| **AJ-1.10** | §15 / Referencias | ERRATA | 🟡 | Citas inconsistentes: Liu 2023/2024, Minderer, Xiao, Lin 2014/2015, Ren a/b/c. |
| **AJ-1.11** | §15 | CONCRETA | 🟡 | **MM-Grounding-DINO no tiene ninguna cifra en el informe**, y el proyecto lo evaluó y lo descartó. |
| **AJ-1.12** | §15 | PRECISA | 🟠 | **Advertencia de métrica**: AP 0,50:0,95 (COCO/LVIS) y mAP@0,5 (EPP y nuestro bench) **nunca en la misma columna**. |
| **AJ-1.13** | §15 | CONCRETA | 🟠 | Incorporar la **Vara 3** — el cruce OVD×EPP, que está casi vacío y es el hueco que ocupa `bench_v3`. |
| **AJ-1.14** | §15 | PRECISA | 🟠 | Corregir el uso de **Abdalwhab 2025**: es evidencia de brecha de vocabulario zero-shot, **no** del efecto de ajustar un OVD. |
| **AJ-1.15** | §15 → §17.5 | PRECISA | 🟠 | Fijar la **regla de tres tiempos** para presentar conclusiones, y usar "adaptación" con precisión. |
| **AJ-1.16** | **§16** | EVIDENCIA | 🟡 | **Hueco: el §16 Marco Teórico no fue relevado** contra lo que hoy sabemos. |

---

## 3. Los ajustes, desarrollados

### AJ-1.01 · §15 · CONCRETA · 🔴 — la vara supervisada in-domain

**Qué pasa hoy.** El informe **no reporta ni una cifra de mAP** de la literatura de
detección de EPP con modelos entrenados. SHEL5K, CHV y SH17 aparecen solo como
datasets.

**Qué debe decir.** La Vara 1, en **mAP@0,5** [P/S]:

| Dataset (paper) | Mejor modelo entrenado | mAP@0,5 | Dato fino que importa |
|---|---|---|---|
| SHEL5K (Otgonbold 2022, *Sensors* 22(6):2315) | YOLOR | **0,883** | `head` (cabeza sin casco) **0,907** — supervisada, la clase **no** es difícil |
| CHV (Wang 2021, *Sensors* 21(10):3478) | YOLOv5x | **0,866** | 6 clases (person, vest, 4 colores de casco) |
| SH17 (2024; 17 clases, industrial) | YOLOv9-e | **≈0,71** | YOLOv8 n→x: 0,58–0,69 — con vocabulario grande el techo baja |

El dato de `head` 0,907 es el fundamento externo de dos conclusiones propias (AF-5 y
F-88.3): **la clase `bare_head` no es difícil; lo difícil es alcanzarla por vía
léxico-conceptual sin entrenar.**

**Alternativa admisible** si no se quiere ampliar el §15: declarar explícitamente la
ausencia como brecha del estado del arte. Lo que **no** es admisible es dejar el 0,551
sin vara.

---

### AJ-1.02 · §15 y Tabla 3 · CONCRETA · 🔴 — cruzar el estado del arte con la evidencia propia

**Qué pasa hoy.** El dato más contundente del proyecto no está escrito en el §15:
**YOLOE publica 35,9 AP en LVIS y acá midió recall CR-01 = 0,000.** Tampoco está el
trade-off de latencia: §17.1.9.2 lo justifica con GPUs ajenas cuando ya existe medido
en nuestro hardware (**G2A live 630–890 ms** GDINO vs **225–249 ms** YOLOE; keep-up
**22%** vs **63–69%**, Sprint 2).

**Qué debe decir.** Que los benchmarks generales **no predicen la condición de
dominio** — y por eso la selección de modelo se hizo sobre un bench propio y no sobre
LVIS. Es el argumento metodológico más fuerte del capítulo, y hoy no está.

---

### AJ-1.03 · §15 · ERRATA · 🟠 — declarar el backbone de cada cifra de GDINO

El **52,5 AP COCO zero-shot corresponde a Swin-L**, y el informe no lo declara. Lo
desplegado en este trabajo es **Swin-T**, cuyo zero-shot COCO publicado es **≈48,4**
[S]. Regla a aplicar en todo el §15: **ninguna cifra de GDINO sin su backbone al lado.**

---

### AJ-1.04 a AJ-1.08 · erratas y precisiones verificables contra los papers

Se agrupan porque se corrigen en una sola pasada, todas contra fuente:

- **AJ-1.04** — OmDet-Turbo-Tiny aparece con "30,3 LVIS", que es un *mislabel* probable
  de **ODinW-13**; y el mismo modelo figura con **34,0 en una tabla y 34,7 en otra**.
- **AJ-1.05** — el **53,4 COCO** de OmDet-Turbo probablemente **no es zero-shot**;
  verificar y etiquetar.
- **AJ-1.06** — LLMDet "51,1–52,4": el **52,4 no tiene origen** rastreable.
- **AJ-1.07** — se afirma que el caching **"ahorra ≈40 ms"** en un modelo al que la
  misma tabla asigna **7,1 ms totales**. Es aritméticamente imposible.
- **AJ-1.08** — la **columna Latencia de la Tabla 3 es 1000/FPS**: es una derivación, no
  una medición. Declararlo en la nota de la tabla (y es la bisagra para introducir
  nuestras latencias medidas, AJ-1.02).

---

### AJ-1.09 · Anexo A / Tabla A.1 · ERRATA · 🟠 — la licencia de GDINO 1.5 y DINO-X

La Tabla A.1 las lista como **"Apache-2.0"**. Son **API cerrada sin pesos abiertos**:
lo Apache-2.0 es el **SDK**, no el modelo [S]. Es una errata con consecuencia — una
afirmación de licencia incorrecta en un anexo de comparación técnica es exactamente el
tipo de cosa que un jurado verifica.

---

### AJ-1.10 · Referencias · ERRATA · 🟡

Citas inconsistentes a lo largo del §15: **Liu 2023/2024** (misma obra, dos años),
**Minderer**, **Xiao**, **Lin 2014/2015**, **Ren a/b/c**. Unificar contra el listado de
referencias del `96e`.

---

### AJ-1.11 · §15 · CONCRETA · 🟡 — MM-Grounding-DINO

El proyecto lo **evaluó y lo descartó empíricamente** (bboxes roto en MM-GDINO-tiny), y
el informe **no trae ninguna cifra suya**. Publicadas: **tiny 50,4–50,6 COCO zero-shot
/ 35,7–41,4 LVIS** [P/S]. Sin la cifra, el descarte queda sin contexto.

---

### AJ-1.12 · §15 · PRECISA · 🟠 — la advertencia de métrica (la trampa del jurado)

Las cifras COCO/LVIS de los papers OVD son **AP promediado sobre IoU 0,50:0,95** (LVIS
además con protocolo *Fixed AP*). Los papers de EPP y nuestro bench reportan
**mAP@0,5**, que da numéricamente más alto para el mismo detector.

**Nunca poner las dos series en la misma columna.** El error previsible del jurado es
*"GDINO da 48–52 en COCO y ustedes 0,55 — rinde igual"*. No: en mAP@0,5 sobre COCO
estaría muy por encima; **nuestra caída es real y es el costo de dominio**. Esta
advertencia tiene que estar escrita en el informe, no solo entendida.

---

### AJ-1.13 · §15 · CONCRETA · 🟠 — la Vara 3: el cruce OVD×EPP

Es el hueco que el trabajo ocupa, y hay que decirlo con las tres piezas:

- **OWLv2 zero-shot sobre obra** (Choi & Greer 2024, arXiv:2410.12225): AP@IoU>0,5
  **0,649 hardhat** y **0,677 person** sobre 5.210 imágenes [P] — la **única** cifra
  publicada directamente comparable con nuestro AP@0,5 por clase.
- **VLMs con atributo/negación** (Chen 2025, arXiv:2508.11011): *"workers wearing white
  hard hats"* → **IoU <20%** [P] — la literatura confirma la "ceguera al atributo" de
  E-DIR que medimos.
- **No existe paper 2023–2026** con GDINO o YOLO-World zero-shot medido sobre
  SHEL5K/CHV, ni sobre un bench de EPP multi-fuente con protocolo COCO. **`bench_v3`
  está esencialmente solo en ese cruce.**

Las fuentes externas verificadas el 2026-08-06 están listadas al final de
`sintesis/resultados-y-conclusiones.md` §7.4 — reusar ese listado, no rearmarlo.

---

### AJ-1.14 · §15 · PRECISA · 🟠 — Abdalwhab 2025 está mal usado

El paper compara **YOLO11 fine-tuned vs OVD zero-shot** en componentes MEP. Eso es
**evidencia de brecha de vocabulario zero-shot**, no evidencia del efecto de ajustar un
OVD. Como está citado hoy, sostiene una conclusión que el paper no sostiene.

---

### AJ-1.15 · §15 → §17.5 · PRECISA · 🟠 — la regla de tres tiempos, y "adaptación"

**Regla de redacción** (fijada 2026-08-06): cada conclusión se escribe en tres tiempos —
*qué dice la literatura* (cifra de la Vara) → *qué medimos nosotros* (cifra de
`results/`) → *qué tipo de aporte queda*. **Nunca al revés**: empezar por el número
propio sin vara es exactamente lo que hoy le pasa al §15.

**Y una precisión de vocabulario que hay que cuidar ante el jurado:** la tesis **no
adapta los pesos** — el fine-tuning es E-04, no ejercida, con costo medido. Adapta los
modelos **operativamente**: resolución (560), formulación del vocabulario (prompt sets
congelados) y las capas de plataforma alrededor (histéresis temporal, identidad por
sujeto, política de alerta). **Medir cuánto rinde ese stack de adaptación sin entrenar
es la perspectiva nueva** — decirlo así, y no "adaptamos los modelos".

---

### AJ-1.16 · §16 Marco Teórico · EVIDENCIA · 🟡 — hueco declarado

**El §16 no fue relevado contra el estado actual del proyecto.** Todo el relevamiento
de Etapa 1 se concentró en el §15 y en el Anexo A. Antes de dar la etapa por cerrada
hay que pasar el §16 (`entregable/96d`) contra `sintesis/fundamentos-teoricos.md`, que
es la versión hoy vigente de la teoría del trabajo, y anotar acá lo que aparezca.

Esto es un hueco de relevamiento, **no** una afirmación de que el §16 esté bien.

---

## 4. 🚫 Lo que no hay que tocar en esta etapa

- **Las cifras ancla verificadas.** La verificación externa **confirmó** GDINO 52,5 AP
  COCO / 26,1 mean AP ODinW [P]; YOLO-World-L 35,4 AP LVIS @ 52 FPS [P]; YOLOE-v8-S/L
  27,9/35,9 AP LVIS @ 305,8/102,5 FPS T4-TensorRT [P/S]; GDINO 1.5 Pro 54,3/55,7 y Edge
  36,2 @ 75,2 FPS [S]. Están bien: lo que falta es el backbone (AJ-1.03) y el cruce
  (AJ-1.02).
- **La estructura del §15** (4 paradigmas · ~25 modelos · Tabla 3 · Tabla A.1) y los
  criterios de selección de §17.1.9.2, que fundan el par GDINO+YOLOE como polos del
  trade-off expresividad semántica ↔ latencia. El encuadre es correcto y sobrevive.

## 5. Fuentes

`sintesis/resultados-y-conclusiones.md` §7.1–§7.4 (relevamiento y verificación externa
del 2026-08-06, con el listado completo de arXiv/DOI consultados) ·
`sintesis/fundamentos-teoricos.md` · `entregable/96c`, `96d`, `96e` §19.1.
