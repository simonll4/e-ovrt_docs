# Borrador — la vara del §15 (AJ-1.01 · AJ-1.02 · AJ-1.13)

> **Qué es esto (2026-08-16).** Borrador *texto listo para copiar* (patrón del doc `94`)
> redactado según el ✎ 2026-08-16 del manual `ajustes/08` §2: la vara del §15 se adelanta
> como borrador para desbloquear el §17.5; **los colegas la revisan e integran en Google
> Docs** (D-A híbrida: la §15 existe, así que la edición final es en el documento). La
> decisión fina de anclaje es de quien integra; acá va la propuesta.
>
> **Regla cumplida:** cero cifras propias del proyecto (no-anacronismo, mapa `00` regla 5).
> Todo lo que sigue es literatura, con la métrica de cada cifra declarada al lado
> (evita de paso la trampa de AJ-1.12: nunca mezclar AP 0,50:0,95 con mAP@0,5).
>
> **Al integrar:** marcar `AJ-1.01`/`AJ-1.02`/`AJ-1.13` en el tablero (manual `08` §5),
> anotar cualquier desvío como ✎ en la ficha (`ajustes/01`), sumar las referencias del
> §4 de este borrador al listado del `96e`, y re-extraer la foto de §15
> (`herramientas/extraer_informe.py`, regla D-C).

---

## 1. Dónde ancla cada bloque

| Bloque | Ajuste | Punto de inserción propuesto |
|---|---|---|
| Bloque A — Vara 1, la línea base supervisada | `AJ-1.01` 🔴 | **§15.2.5**, al comienzo: antes de declarar brechas, fijar qué logra lo supervisado in-domain |
| Bloque B — la pregunta que los benchmarks generales no responden | `AJ-1.02` 🔴 | **§15.2.5**, a continuación del Bloque A · más la **nota al pie de la Tabla 3** (§15.2.3) |
| Bloque C — Vara 3, el cruce OVD×EPP | `AJ-1.13` 🟠 | **§15.2.5**, cierre de la subsección: la brecha queda declarada |

Los tres bloques forman una secuencia narrativa única dentro de §15.2.5 (vara supervisada
→ pregunta de generalización → brecha del cruce), así que conviene integrarlos en un solo
pase. La subsección existente se conserva; esto se intercala donde hoy la brecha se
menciona sin cifras.

---

## 2. Los tres bloques, texto listo para copiar

### Bloque A — la línea base supervisada in-domain (AJ-1.01)

La detección de EPP con modelos supervisados entrenados in-domain constituye una línea
base madura, con cifras publicadas sobre los mismos conjuntos de datos que este trabajo
adopta como fuentes. Sobre SHEL5K, Otgonbold et al. (2022) reportan para YOLOR un
mAP@0,5 de **0,883**, con **0,907** para la clase *head* (cabeza sin casco); sobre CHV,
Wang et al. (2021) reportan para YOLOv5x un mAP@0,5 de **0,866** sobre seis clases
(persona, chaleco y cuatro colores de casco). En conjuntos de mayor vocabulario el techo
desciende: en SH17 (2024; 17 clases de entorno industrial), YOLOv9-e alcanza
aproximadamente **0,71** de mAP@0,5, y la familia YOLOv8 (variantes n a x) se ubica entre
**0,58 y 0,69**.

Dos lecturas de esta vara importan para lo que sigue. Primero, la detección supervisada
de EPP es un problema esencialmente resuelto en su formulación estándar: con
entrenamiento in-domain, las clases centrales superan 0,85 de mAP@0,5. Segundo — y es el
dato fino que esta vara deja establecido —, la clase *cabeza sin casco*, que podría
suponerse difícil por su granularidad semántica, **no lo es para un detector
supervisado**: 0,907 en SHEL5K, por encima incluso del promedio del conjunto. Cualquier
dificultad que aparezca sobre esa clase por otras vías de detección no podrá atribuirse,
entonces, a la clase en sí.

### Bloque B — la pregunta que los benchmarks generales no responden (AJ-1.02)

Los modelos open-vocabulary del presente capítulo se comparan habitualmente por sus
cifras sobre benchmarks generales (COCO, LVIS; Tabla 3). Esas cifras responden cuánto
generaliza el modelo *sobre la distribución de esos benchmarks*, pero dejan sin
responder la pregunta que este trabajo necesita: **¿predicen los benchmarks generales el
rendimiento sobre una condición de dominio específica?** La evidencia publicada sugiere
que no. El propio equipo de Grounding DINO reporta que su variante grande, con ~52 AP
(COCO, 0,50:0,95) en el benchmark general, cae a **26,1 de mean AP sobre los 35
datasets de ODinW** (Liu et al., 2023) — la referencia publicada de cuánto colapsa un
detector open-vocabulary fuera de distribución. Y cuando la consulta exige composición
léxica fina — atributo o negación, del tipo *"trabajadores con casco blanco"* —, Chen
et al. (2025) miden sobre escenas de construcción que los modelos de
grounding quedan por debajo de **20% de IoU**: el preentrenamiento no resuelve por sí
solo la composición.

De ambas evidencias queda una conclusión que este capítulo puede firmar: **los
benchmarks generales no garantizan el rendimiento sobre la condición de dominio, y no
existe benchmark publicado del cruce entre detección open-vocabulary y EPP** (§15.2.5,
cierre). Esa brecha es la que justifica la decisión metodológica, adoptada en el
protocolo experimental (§17.1.9.2), de exigir una línea base zero-shot propia sobre un
conjunto de evaluación congelado, en lugar de seleccionar modelos por sus cifras
publicadas.

**Nota al pie propuesta para la Tabla 3 (§15.2.3):** *Las cifras de precisión de esta
tabla corresponden a benchmarks generales (COCO/LVIS, AP 0,50:0,95 salvo indicación) y
no son directamente trasladables a una condición de dominio específica; la validez de
esa extrapolación se discute en §15.2.5.*

### Bloque C — la Vara 3: el cruce OVD×EPP está casi vacío (AJ-1.13)

El cruce entre detección open-vocabulary y EPP en obra cuenta con una única cifra
publicada directamente comparable con una evaluación por clase a AP@0,5: Choi y Greer
(2024) miden OWLv2 zero-shot sobre 5.210 imágenes de obra y reportan **0,649 para
*hardhat*** y **0,677 para *person*** (AP a IoU>0,5). Sobre la composición con atributo,
la evidencia citada arriba (Chen et al., 2025; IoU <20%) confirma que la vía léxica fina
está lejos de resuelta. Fuera de esas dos piezas, la revisión efectuada no encontró
**ningún trabajo publicado entre 2023 y 2026 que mida Grounding DINO ni YOLO-World
zero-shot sobre SHEL5K o CHV, ni sobre un benchmark de EPP multi-fuente con protocolo
COCO**. La comparación entre la vara supervisada del Bloque A (mAP@0,5 ≥ 0,86 con
entrenamiento in-domain) y la única cifra zero-shot disponible (0,649 en la clase más
favorable) queda, por lo tanto, sin un puente publicado: **esa es la brecha que el
estado del arte deja declarada**.

---

## 3. Qué NO va acá (y dónde vive)

- La confirmación **medida** de la brecha (el caso YOLOE: 35,9 AP LVIS publicado vs el
  recall propio; los G2A medidos vs la columna de latencia derivada) es material de
  **§17.5**, escrito en tres tiempos contra esta vara (`AJ-5.11`).
- Que `bench_v3` **ocupa** la brecha declarada es lectura de §17.5/§18, no del §15.
- La lectura de la clase `bare_head` contra la vía léxico-conceptual (AF-5) también:
  acá queda solo el fundamento externo (head 0,907 supervisado).

## 4. Referencias a incorporar al listado del `96e`

Verificadas 2026-08-06 (listado de `sintesis/resultados-y-conclusiones.md` §7.4):

- Otgonbold, M.-E. et al. (2022). *SHEL5K: An Extended Dataset and Benchmarking for
  Safety Helmet Detection*. **Sensors 22(6):2315**.
- Wang, Z. et al. (2021). *Fast Personal Protective Equipment Detection for Real
  Construction Sites Using Deep Learning Approaches*. **Sensors 21(10):3478** (dataset CHV).
- SH17 (2024). *Dataset for human safety and PPE detection in manufacturing industry*.
  **arXiv:2407.04590**.
- Liu, S. et al. (2023). *Grounding DINO: Marrying DINO with Grounded Pre-Training for
  Open-Set Object Detection*. **arXiv:2303.05499** (cifra ODinW-35).
- Choi, J. & Greer, R. (2024). *Language-guided zero-shot object detection: OWLv2 sobre
  hardhat en obra*. **arXiv:2410.12225**.
- Chen et al. (2025). *ConstructionSite-10k: grounding con atributo y negación en escenas
  de construcción*. **arXiv:2508.11011**.

> ⚠️ Al integrar en el `96e`, unificar el formato con el listado existente (AJ-1.10:
> hoy conviven Liu 2023/2024 y variantes). Los títulos de Choi & Greer y Chen 2025
> están parafraseados acá — **verificar el título exacto contra el arXiv al citarlos**.
