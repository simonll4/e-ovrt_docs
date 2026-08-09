# 93 — Relevamiento: qué resultados están cerrados y qué falta para cerrar

- **Fecha:** 2026-08-05.
- **Qué es:** el inventario honesto del estado de **los resultados** (no del informe),
  pedido antes de pasar a redacción. Cubre los dos frentes que el usuario señaló —
  **anotaciones del lote de internet** y **la parte real-time** — más todo lo demás que
  quede abierto. Para cada ítem: qué hay, qué falta, quién lo destraba y **qué se cae
  si no se hace**.
- **Regla que gobierna el cierre** (doc 57 §7.6, decisión del usuario): *el núcleo
  validable se cierra con las métricas que el material efectivamente cubra; lo no
  cubierto se declara con causa, nunca se fabrica ni bloquea.*

---

## 1. Tablero de una mirada

| Frente | Estado | Falta | Quién |
|---|---|---|---|
| Fase S — selección de modelos (imágenes) | ✅ **CERRADO** | — | — |
| Fase D Nivel A — E-DIR vs E-IND por persona | ✅ **CERRADO** | CR-02 con IC solapados (declarado) | — |
| Fase T/P — Nivel B, 6 campañas sobre 34 clips | ✅ **CERRADO** | — | — |
| Fase L — EBE live | ✅ **CERRADO sin opcionales** | — (la re-toma P2 quedó cumplida por el humo del doc 91: 2 CR-02 live limpias, 0 sobre-marcas en 309 frames) | — |
| **Lote de internet** | 🔴 **ABIERTO** — 0/14 con GT ✎ 2026-08-06: **3/14 con GT humano, promovidos — banco 34→37 (doc 102)**; runs I1/I2 armados sin correr | corrección CVAT de 14 clips | **usuario** |
| Videos V1–V3 de defensa | 🟡 scopeado, sin construir | 2 preguntas de alcance + renderer | usuario decide, yo implemento |
| FAR/hora | ⚫ **cerrado como limitación** (D-90.1) | nada — no se reporta | — |

---

## 2. Lote de internet (el frente que señalaste)

### Estado real de la cadena

| Etapa | Estado |
|---|---|
| Clips preparados (`clips/v*.mp4`) | ✅ **14/14** |
| Pre-anotación automática (`preann/v*.xml`) | ✅ **14/14** (GDINO-base + ByteTrack) |
| **Corrección humana en CVAT (`corrected/v*.xml`)** | 🔴 **0/14** ✎ 08-06: **3/14** (`v04_c01`, `v06_c01`, `v10_c01` — doc 102) |
| GT derivado (`gt/v*.json`) | 🔴 **0/14** ✎ 08-06: **3/14**, validados y promovidos |

O sea: **todo lo automatizable está hecho y lo que falta es exclusivamente trabajo
humano de CVAT.** Del lado de la plataforma no hay nada pendiente — cuando existan los
XML corregidos, la cadena es un comando y la campaña son minutos de CPU (ya está
probada 34 veces sobre el rodaje).

### Qué aporta, y qué NO aporta

**Aporta (y es lo único que lo aporta):**
- **L4 — generalización a material NO guionado.** Hoy el banco entero es Bloque A:
  un escenario controlado, mismos actores, misma locación. Es la limitación más
  citable del trabajo y la única que este lote levanta.
- **Control de FP sobre material real**: 13 de los 14 son P5 (cumplimiento), o sea
  material donde el sistema **no debería** alertar, en obra real y no guionada. Es un
  análisis de sensibilidad del resultado de negativos que hoy vive en 4 clips
  guionados de 2,1 min.

**NO aporta (importante, para no sobre-esperar):**
- **FAR/hora no se reporta igual** — D-90.1 lo determinó: ninguna cota alcanzable
  sostiene una afirmación. Este lote no cambia eso.
- **Casi nada del lado detección**: 13 de 14 son negativos; solo `v04_c01` (P8) es
  positivo. Sirve para precision, no para recall.

### Recomendación de alcance (para que no cueste más de lo que rinde)

Anotar los 14 completos es caro y el retorno es marginal después de los primeros.
**Sugerencia: priorizar por lo que cada clip destraba.**

1. **`v06_c01` (6,2 min)** — ya en curso. Es el único que da denominador temporal y el
   ancla del análisis de FP sobre material real. **Terminarlo, como ya decidiste.**
2. **`v04_c01` (P8, positivo)** — el único con episodio de infracción: es el que puede
   dar un dato de **recall en material no guionado**, que hoy no existe en ninguna
   parte del trabajo. Alto valor por unidad de esfuerzo.
3. **El resto (12 clips P5, ~9 min)** — aportan tiempo de cumplimiento adicional.
   Marginal: se pueden anotar si sobra tiempo, o declararse fuera de alcance sin que
   se caiga ninguna conclusión.

**Si el tiempo aprieta, con (1) y (2) el lote ya cumple su función**: L4 queda
levantada con material real —un clip de cumplimiento largo y uno con infracción— y el
resto se declara como cobertura no ejecutada con causa.

### Runbook para cuando salgan de CVAT (tu parte termina en el paso 1)

> ✎ **2026-08-06 — ejecutado para los 3 primeros (doc 102), con una corrección al
> paso 2:** los exports llegaron a nivel **TASK**, no proyecto, así que
> `split_cvat_project.py` NO se aplica (habría sido el error simétrico). La regla
> queda: **mirar `meta/task` vs `meta/project` en el XML antes de decidir**. El resto
> de la cadena corrió tal cual está escrita. Runner del estrato B:
> `datos/102-ciclo-internet-runner.py` + `datos/102-cerrar-campanas-internet.sh`.

1. **Corregir en CVAT** (`GUIA-CVAT.md` en `datasets-videos/`) y **exportar como
   "CVAT for video 1.1"**. Recordar la trampa madre (doc 80): el export de proyecto
   numera frames en espacio GLOBAL — nunca alimentarlo directo.
2. Avisarme. De ahí en adelante es mi cadena, ya probada 34 veces:
   `split_cvat_project.py` → `derive_clip_gt` (mismos umbrales 4000/7000) →
   `validate_clip_gt` → `promote_clip` → campaña DBE (runner tipo 81 apuntado a los
   `v*`, ajuste de un glob) → `aggregate_clip_campaign` → fila nueva en
   `results/clip_bench/index.md` como estrato B con desglose (D-90.6).
3. Los clips soak/negativos que resulten `negative: true` entran al análisis de
   sensibilidad del control de FP (D-90.1 punto 4).

---

## 3. Real-time / EBE live (el otro frente que señalaste)

**Está más cerrado de lo que parece.** El relevamiento:

### Lo que YA está medido y es citable

| Qué | Dónde | Estado |
|---|---|---|
| L0 — ensayo pre-rodaje 1:1 con cámaras | docs 65, 67 | ✅ verde, `bus_dropped=0` |
| **L1 — EBE del día del rodaje: 6 corridas** | doc 71 | ✅ **completo** |
| **7 confirmaciones CR-01 live** con GDINO | doc 71 §7.2 | ✅ deltas **4,1–4,6 s** sobre umbral 4,0 |
| 1 confirmación CR-02 live legítima | doc 71 (15:47) | ✅ delta **7,1 s** |
| Acople EBE, jornada entera | doc 71 | ✅ **0 eventos perdidos** |
| `t_capture→alert` / G2A live | doc 71 §2 | ✅ medido (GDINO 630–890 ms p95, fuera del budget 250; YOLOE 225–249 ✓) |
| Paridad live↔offline | doc 37 | ✅ verificada: toda corrida live es re-evaluable offline con artefactos idénticos |
| Diagnóstico del techo de fps | docs 73/74 | ✅ **F-RT3 = contención de GIL** (no térmico, no la rama de texto) |
| Palanca de fps implementada | F-RT5 | ✅ **+18% fps, −14,4% latencia, p=0,0195** |
| **Regresión live tras TODOS los cambios** | doc 91 | ✅ **verde 2026-08-05** |
| G1 (identidad) en vivo | doc 91 | ✅ verde |

**El veredicto del doc 71 §7.2 sigue vigente y lo confirmo tras revisarlo:** *"para el
cierre de la tesis, SÍ alcanza"*. Y las dos observaciones negativas son **resultados de
primera línea**, no fallas: **F-RT1** (la sobre-marca de `vest` suprime CR-02) y
**F-RT2** (la ventana temporal exige estabilidad perceptual con huecos <
`resolve_after_ms` — GDINO la cumple, YOLOE no). Eso último es una **condición de
validez descubierta**, exactamente el tipo de aporte que la tesis argumenta.

### ~~Lo único que faltaba (opcional): la re-toma P2~~ → **YA SE CUMPLIÓ (2026-08-05, verificado a posteriori)**

La re-toma buscaba *una CR-02 live limpia adicional* (la del rodaje a las 15:47 era la
única legítima; F-RT1 mostró que la sobre-marca de `vest` sobre ropa la suprime). Al
revisar los humos del doc 91 contra ese objetivo: **CR-02 confirmó en vivo en las DOS
fases** (frames 225 y 217, deltas por encima del piso de 7 s), y el `summary` de los
runs del media-plane muestra **cero detecciones de `vest` en 309 frames** — sin
sobre-marca, confirmación limpia. Es incluso un caso más fuerte que el que la re-toma
pedía: la especificación sugería "remera lisa clara, no negra" por miedo a la
sobre-marca sobre ropa oscura, y **con remera negra no hubo ni una marca falsa**.

**Balance CR-02 live: 3 confirmaciones legítimas** (rodaje 15:47 + humo fase A + humo
fase B) y F-RT1 queda como lo que es — un modo de falla **dependiente de la
vestimenta** (campera a franjas 0,54 / torso liso 0,31), documentado con su caso
positivo y su caso negativo. **No hace falta re-toma, ni cámara, ni casco/chaleco**:
CR-02 mide la *ausencia* de chaleco — una persona sin chaleco ES el caso de prueba.
**La Fase L queda cerrada sin ítems opcionales.**

### Un matiz que conviene declarar en el informe

Las mediciones live del rodaje se hicieron con el código del **2026-07-25**, y desde
entonces el control-plane cambió bastante. Verifiqué que eso **no las invalida**: los
deltas de confirmación dependen de `confirm_after_ms` (sin cambios) y las métricas
G2A/`t_capture→alert` son del media-plane; los fixes fueron del **evaluador**, que no
interviene en esas corridas (no tienen GT — doc 58: "cada plano mide lo suyo"). Y el
humo del doc 91 re-verificó el camino completo con el código actual. **No hace falta
re-tomar nada por este motivo.**

---

## 4. Lo demás que queda abierto en resultados

| Ítem | Estado | Qué falta | Se cae si no se hace |
|---|---|---|---|
| **CR-02 a Nivel A** | medido con IC solapados | otra fuente con negativos de chaleco explícitos | nada: está declarado como no cerrado |
| **`hyb_and`** | ⚫ cerrada con causa (D-90.4) | nada | nada — el fundamento es que no es medible contra este banco |
| **Videos V1–V3** | scopeado (doc 79) | 2 preguntas de alcance + renderer de composición | material de defensa, no resultado |
| ~~Mini-piloto de clase nueva~~ | ✅ **EJECUTADO 2026-08-05 (doc 94)** | — | A1 medido: 0 entrenamientos, 48 líneas, 9 min; `machinery` AP@0.5 **0,662** zero-shot + F-94.1 |
| Tracker en obra real | no medido | material real con multitud | declarado como límite de G1 |

### El hueco que apareció relevando: el mini-piloto de clase nueva (MOCS)

El doc 62 §7 lo lista como **complemento de la Fase D**. **No se ejecutó y no estaba en
ningún tablero de pendientes** — se perdió cuando la Fase D se reorganizó.

Su valor real es mayor de lo que sugiere su tamaño. El doc 62 lo asocia a A3, pero
leyendo `nucleo/09` el argumento que sostiene es sobre todo **A1 — "la economía del
catálogo"**, que ese doc llama *"el argumento cuantificable más fuerte"* y sobre el que
dice, textual: ***"este número — condición nueva: 0 entrenamientos, ~20 líneas de
configuración, minutos — debe medirse y reportarse como resultado, no solo
afirmarse"***.

Hoy **ese número no está medido en ninguna parte del trabajo.** Toda la evidencia
producida es sobre CR-01/CR-02, o sea el catálogo que ya existía. La afirmación central
de la defensa —que agregar una condición nueva cuesta editar dos YAML— **no tiene
evidencia propia**.

- **Qué es:** correr el detector sobre material con una clase que nunca se entrenó ni
  se pensó (MOCS tiene maquinaria, y `raw/` ya lo trae), con un prompt set nuevo, y
  **medir el costo real**: líneas de config, tiempo de humano, cero entrenamientos.
- **Costo:** bajo. MOCS ya está en disco, la cadena existe, y **no hace falta GT
  nuevo** si el resultado se reporta como el par (evidencia cualitativa de detección +
  costo de configuración medido).
- **Recomendación:** ejecutarlo. Es el ítem de **mejor relación valor/esfuerzo** que
  queda en resultados: cubre el argumento que el propio doc 09 marca como el más fuerte
  y que hoy está descubierto.

---

## 5. Qué haría yo, en orden

1. ~~Mini-piloto de clase nueva~~ — **EJECUTADO** (doc 94): A1 tiene su número.
2. **Terminar `v06_c01` + priorizar `v04_c01`** (CVAT, usuario) — con esos dos, L4
   queda levantada y el resto del lote pasa a opcional. Punto medio si se quiere
   robustecer el control de FP: +2–3 clips cortos **de videos fuente distintos** (la
   diversidad de fuentes vale más que los minutos). Runbook arriba.
3. ~~Re-toma P2 live~~ — **cumplida** (doc 91, verificado a posteriori). No hace falta
   volver a encender la cámara ni juntar gente para el tramo de resultados.
4. **La redacción del informe (doc 92 → §17.x) ya no espera nada**: el único insumo
   pendiente (lote de internet) se integra como sección incremental cuando llegue.

**Nada de lo abierto bloquea la escritura**: todo lo que falta se integra como sección
incremental o se declara con causa, que es la regla del §7.6.
