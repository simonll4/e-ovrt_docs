# Correcciones de la Etapa 2 — §17.1 Consolidación Metodológica (pase 1, 2026-08-28)

> **Estado: NO aplicado — es el trabajo a hacer.** Texto base: `90f-etapa2-texto-extraido.md`
> (extracción del documento de trabajo
> `desarrollando/E-OVRT-VDP_Seccion_17.1_Consolidacion_Metodologica_v1.0.docx`, que es el §17.1
> del informe v1.1 **sin ninguna corrección**: 32.669 palabras, 122 títulos, Tablas 16–38, 85
> ecuaciones de Word). Este pase **integra y precisa** las 12 fichas `AJ-2.xx` de `ajustes/02`,
> agrega la ficha **AJ-2.13**, aplica las podas **PODA-12/13/14** y resuelve los handoffs que
> dejaron las Etapas 1 y 3. Donde este pase y una ficha difieren, **manda este pase** (las fichas
> se escribieron el 08-10 con la plataforma a medio construir; el relevamiento `operacion/130`
> del 08-28 verificó cada afirmación contra los repos).
>
> **Regla de lectura de §17.1 (no-anacronismo, mapa regla 5):** §17.1 es el **protocolo**. Entran
> decisiones, definiciones, criterios y valores de configuración elegidos dentro de rangos
> declarados. **No entran** resultados medidos, cifras propias ni estados de implementación —
> eso vive en §17.4/§17.5. Lo que el protocolo prescribió y no se ejerció **no se borra ni se
> "corrige" acá**: queda como protocolo (con su criterio de aplicabilidad, si hace falta) y
> §17.5 lo reporta como no ejercido. Guardrails: **§17.1.5 y §17.1.7 no se comprimen** (`07` §9);
> los nombres de métrica que se ven como `⟦ECUACIÓN⟧` o vacíos son objetos de ecuación de Word,
> **no erratas** (mapa `00` §7).
>
> **Autocontención:** nada de lo que sigue —códigos `E2-`, `AJ-`, `D-E2-`, `R-`, `F-`, rutas,
> ADRs, docs de `operacion/`— aparece en el texto del informe. Los únicos identificadores que el
> informe usa son los que define para sí: CR-xx, PR-xx, E-DIR/E-IND/E-HYB (desde este pase),
> P-E1-xx, L1–L8, nombres de configuración.

---

## A. Decisiones que gobiernan el pase

| ID | Decisión | Firma |
|---|---|---|
| **D-E2-1** | El `.docx` de la etapa es **sólo §17.1**. Los Anexos C y D se corrigen en este mismo pase (§E) pero **fuera** del documento: quedan en `90g-etapa2-anexos-c-y-d.md` para que el equipo los arme en §19 (mismo mecanismo que el Anexo A en `90e`). | usuario · 2026-08-28 |
| **D-E2-2** | Los códigos **E-DIR / E-IND / E-HYB se bautizan en §17.1.5.4.2** (E2-09). **Dependencia inversa:** §17.3.6.4 (v1.4) debe recortar su glosa a una remisión → handoff a la Etapa 3 (§F). | usuario · 2026-08-28 |
| **D-E2-5** | Ficha nueva **AJ-2.13**: el nivel intermedio **"estado observable por persona"** se declara en §17.1.7.3.1 como nivel de análisis (E2-18), sin cifras. | usuario · 2026-08-28 |
| **D-E2-6** | MOT17/OVT-B (§17.1.6.3) y métricas MOT (§17.1.7.4.2) **intactos**, con ⊘ explícito (E2-16). Las dos métricas derivadas de la plataforma (`t_capture→alert`, `t_compute-budget`) **no se declaran** en §17.1: ninguna sección del informe las usa. | usuario · 2026-08-28 (bis: recomendación adoptada) |
| D-E2-3 | AJ-2.02 se resuelve como **regla de conteo** en §17.1.7.8.3 (E2-22), no como corrección de una política que §17.1 nunca describió. | recomendación adoptada |
| D-E2-4 | Los 4.000/7.000 ms entran en §17.1.5.3.3 como **decisión de protocolo dentro del rango de la Tabla 24**, sin tocar la tabla y sin la palabra "efectivos" (E2-07). | recomendación adoptada |
| D-E2-7 | AAIP: marcador **espejo** en §17.1.11.1 (E2-25). | recomendación adoptada |
| D-E2-8 | PODA-14 **sólo recorta §17.1.4**; lo recortado se verifica contra las Tablas B.1–B.7 y lo que falte se lista como alta al Anexo B (E2-06). | recomendación adoptada |
| D-E2-9 | Duplicación Tabla 35 ↔ Anexo D: se conserva **la de §17.1.7.7.6** (donde se decide el criterio, D-P3-4) y la del Anexo D se reduce a las filas que agrega más una remisión (E2-20, se resuelve en `90g`). | recomendación — **confirmar al aplicar** |

---

## B. Unidades del pase — por orden de aparición en §17.1

Formato de cada unidad: **qué dice hoy** · **qué está mal o qué falta** (con la fuente verificada) ·
**acción** · texto guía cuando corresponde. Prioridad: 🔴 falso o contradictorio · 🟠 hueco de
concreción · 🟡 precisión / higiene · ⊘ no se aplica (con causa).

### E2-01 · 🔴 · Formato heredado — §17.1.1 con estilo de nivel equivocado
**Hoy:** el título *17.1.1. Función y Alcance…* está en estilo `Heading 2` (el nivel de §17.1) y
lleva un **tabulador** tras el número; sus hermanas §17.1.2…§17.1.12 son `Heading 3` con espacio.
Heredado del maestro v1.1. El verificador lo reporta como *"numeración: §17.1. arranca en 2"*.
**Acción:** aplicar `Heading 3` y reemplazar el tabulador por un espacio. Sin cambio de texto.

### E2-02 · 🔴 · §17.1.6.1.1 — remisión rota a "la sección 16.7.6"
**Hoy:** *"…preguntas rectoras P-E1-03 y P-E1-08 formuladas en la sección 16.7.6…"*. Tras la
Etapa 1, esa subsección es **§16.7.3** (E1-53). Las seis preguntas que §17.1 invoca (P-E1-01, 02,
03, 04, 06, 08) son exactamente las seis que sobrevivieron: **no hay nada más que reponer**.
**Acción:** `16.7.6` → `16.7.3` (única aparición). No tocar los códigos P-E1-xx.

### E2-03 · 🟡 · §17.1.4.2.1 — sistema operativo del CPN
**Hoy:** el CPN candidato se describe con **Windows 11**. **Verificado:** la plataforma corre en
**Linux (WSL2)** y en contenedores Ubuntu; no existe rama Windows. Es una decisión de entorno, va
hacia atrás. **Acción:** una frase: *"El entorno de ejecución adoptado fue Linux (WSL2 sobre el
equipo descrito) y contenedores Linux, por compatibilidad del stack de inferencia y del bus."*
Si la mención a Windows 11 está en el Anexo B (Tabla B.x) y no en el cuerpo, corregir allí (→ 90g).

### E2-04 · 🟠 · §17.1.4.2.3–.4 — la fuente del escenario EBE (AJ-2.10)
**Hoy:** OAK-D Pro PoE *candidata preferente*; cámara IP convencional como *plan de contingencia*.
**Verificado:** la OAK-D está integrada como fuente `oak_d` del plano de medios y **la contingencia
(RTSP) se ejerció primero**; el RTSP sintético (mediamtx + ffmpeg) es herramienta de desarrollo y
vía de reproducibilidad DBE↔EBE con fuente idéntica, no fuente experimental. **Acción:** en
§17.1.4.2.4 declarar la prioridad como decisión: ambas fuentes se integran; la cámara IP por RTSP
se adopta primero por disponibilidad y la OAK-D después; la fuente sintética se declara como
herramienta. **Sin resultados** (los fps reales, las corridas y el rodaje son de §17.4/§17.5).

### E2-05 · 🟡 · §17.1.4.5.1 — resolución de referencia
**Hoy:** parámetros de referencia ≈640 px (Tabla B.6). **Verificado:** la resolución es parámetro
del **perfil de modelo** (YOLOE 640; Grounding DINO 800 por default y 560 como variante), y el
propio §17.1.7.7.5 ya exige recalibrar umbrales si la resolución difiere de 640. **Acción:** una
frase que declare que la resolución de inferencia es un parámetro del perfil de modelo, fijado por
la selección de modelos con umbrales recalibrados por perfil. Sin valores de resultado.

### E2-06 · 🟠 · PODA-14 — §17.1.4 Entorno (3.261 palabras) → detalle al Anexo B (D-E2-8)
**Qué se poda:** el detalle de hardware/stack que **ya está** en las Tablas B.1–B.7 (§17.1.4.2.1
CPN, .2.2 NVDEC, .2.5 stack CPN, .3.1–.3.3 TN, .4.5 parámetros/transporte). **Qué se conserva
íntegro:** §17.1.4.1, la definición de roles CPN/EN/TN (dos o tres frases: §17.3 y §17.4 se apoyan
en que **nacen acá**), §17.1.4.2.3–.4 (E2-04), §17.1.4.4 escenarios DBE/EBE (§17.3.3.3 y §17.4
remiten a **17.1.4.4** por número: no renumerar), §17.1.4.6 restricciones y §17.1.4.7 lectura.
**Ahorro esperado ~1.000 palabras.** Cada dato que se saque debe estar en B.1–B.7; lo que no esté
se lista al final del entregable como *"altas al Anexo B"* (no se edita el Anexo B acá).
**NVDEC (§17.1.4.2.2):** conservar como opción del protocolo; **no** afirmar que se usó.

### E2-07 · 🟠 · §17.1.5.3.3 y Tabla 24 — los valores de persistencia como decisión (AJ-2.01, D-E2-4)
**Hoy:** PR-01 alto **3–5 s**, PR-02 medio **5–10 s**; persistencia en segundos, no en frames;
histéresis activación ≠ desactivación ya pedida. **Verificado:** el conjunto de patrones adoptó
CR-01 confirmación **4.000 ms** / resolución 2.000 ms y CR-02 **7.000 ms** / 3.000 ms —
**dentro de los rangos**. **Acción:** **no tocar la Tabla 24**; agregar al final de §17.1.5.3.3
una frase de decisión: *"Como valores de protocolo dentro de esos rangos se fijan 4.000 ms de
persistencia para la confirmación de PR-01 y 7.000 ms para PR-02, con umbrales de desactivación
de 2.000 y 3.000 ms respectivamente, expresados en milisegundos para independizarlos del ritmo de
cuadro efectivo."* **Prohibido:** "valores efectivos", "configurados", cualquier cifra medida
(la casa de los valores efectivos es §17.4).

### E2-08 · 🟡 · §17.1.5.3.3–.4 — "evita alertas repetidas sobre una misma situación"
**Hoy:** la histéresis *"reduce oscilaciones de estado y evita alertas repetidas sobre una misma
situación"*. **Verificado:** dentro de un episodio no hay repetición (el estado `sustained` no
emite); pero **tras la resolución el motor vuelve a alertar** si la condición reaparece, y la
supresión de re-notificación es política del tramo de distribución, no del motor (decisión de
diseño). **Acción:** precisar la frase: *"…evita oscilaciones y alertas repetidas **dentro de un
mismo episodio**; la reaparición de la condición tras su resolución constituye un episodio nuevo,
y la eventual supresión de notificaciones repetidas se define fuera del motor de patrones."*
Esto deja **coherente** la regla de conteo de E2-22.

### E2-09 · 🔴 · §17.1.5.4.2 — bautizar E-DIR / E-IND / E-HYB (D-E2-2; C-1 del pase 1)
**Hoy:** el eje *"Estrategia de detección"* distingue formulaciones **directas** e **indirectas o
descompuestas** en prosa; los códigos no existen en todo el informe fuera de §17.3/§17.4/§17.5,
y §17.3.6.4 (v1.4) los hace nacer con una glosa porque la remisión a §17.1.5.4.2 era falsa (E3-42).
**Acción:** al final del párrafo *"Estrategia de detección…"* insertar el texto guía de C-1:

> *"En este trabajo estas familias se identifican con un código: estrategia directa (E-DIR),
> cuando el prompt intenta describir la condición de riesgo completa; estrategia indirecta
> (E-IND), cuando el detector identifica entidades visibles por separado y la condición se
> reconstruye mediante lógica externa al modelo; y estrategia híbrida (E-HYB), cuando se combinan
> consultas de ambos tipos bajo una regla de composición explícita. Los códigos identifican las
> variantes en el diseño arquitectónico y en la evaluación experimental."*

**Verificar al aplicar:** que ninguna aparición de los códigos quede *antes* de esta glosa dentro
de §17.1 (hoy hay cero). **Handoff a la Etapa 3 (§F):** §17.3.6.4 recorta su glosa a *"…para las
estrategias directa (E-DIR) e híbrida (E-HYB) definidas en la consolidación metodológica"*.

### E2-10 · ⊘ · AJ-2.04 — los "ejes que faltaban" ya están en el protocolo
**Verificado sobre `90f`:** §17.1.5.4.2 ya trae el eje de **contexto de vocabulario** (*"cada
prompt … en aislamiento y en contexto completo"*, e *"Implicancias del tamaño del vocabulario
activo"*), la **variante con template** (*"a photo of a [CLASS]"*) y §17.1.5.4.5 Fase 2 ya exige
**hiperparámetros constantes** entre variantes. La ficha AJ-2.04 apuntaba a nuestro diseño de
campañas, no al informe. **No se edita §17.1.** Lo que se ejerció de cada eje (vocabulario en
régimen asimétrico sustituido por un control único; templates definidas y no medidas;
hiperparámetros congelados con umbrales operativos calibrados por brazo) **se declara en §17.5**
(handoff §F).

### E2-11 · 🟡 · §17.1.5.4.5 Fase 1 — el piso muestral y la vía elegida (AJ-2.05)
**Hoy:** *"~200 instancias positivas por condición, o bien reportar el tamaño efectivo con
intervalos de confianza"*. **Acción:** declarar la vía como decisión de protocolo: *"Cuando una
condición o un estrato no alcance ese piso, el protocolo exige reportar el n efectivo con
intervalos de confianza al 95 % obtenidos por bootstrap sobre las unidades de evaluación, y
abstenerse de ordenar variantes cuyos intervalos se superpongan."* **Sin n**: los n por
condición y estrato son de §17.5 (limitación L8).

### E2-12 · 🟠 · §17.1.5.4.5 Fase 1 — doble anotación y kappa: criterio de aplicabilidad (AJ-2.06)
**Hoy:** *"≥20 % doblemente anotado, kappa de Cohen para etiquetas e IoU para cajas"*, aplicable
a toda anotación de estado EPP. **Verificado:** no se ejerció (limitación L2): en imágenes se
**reutilizó** la anotación de las fuentes (negativos explícitos) sin anotación nueva; en video la
anotación fue humana pero sin doble anotador; la auditoría humana del GT de imágenes **no se
ejecutó** (sólo su kit). **Acción:** el requisito **se conserva** y se le agrega su criterio de
aplicabilidad, que es protocolo: *"El requisito rige para toda anotación producida por el
proyecto; cuando la referencia se reutilice de anotaciones de fuente sin re-anotación, la doble
anotación no aplica y la ausencia de una medida de acuerdo debe declararse como limitación del
material."* **Prohibido:** escribir "no se hizo" (eso es §17.5).

### E2-13 · 🟠 · §17.1.5.4.4–.5 — el catálogo de candidatos y las métricas por formulación (AJ-2.07)
**Acción (a)** §17.1.5.4.4: declarar que el prompt set se construye **desde el catálogo del
Anexo C (Tabla C.1)** y que las formulaciones finalistas se seleccionan con acta previa a la
evaluación. **(b)** §17.1.5.4.5 Fase 4: sumar **confianza media de los verdaderos positivos** como
indicador de estabilidad por formulación y, para la estrategia indirecta, **métricas por entidad
componente** (`person`, `helmet`, `vest`) para atribuir la degradación. Son criterios: si alguno no
se ejerció, lo dice §17.5. **(c)** El catálogo de **datasets** del Anexo C se corrige en `90g` (§E).

### E2-14 · 🔴 · PODA-12 — §17.1.6.2 Datasets de gestión directa (5.062 palabras) y Tabla 26
**Hoy:** inventario de 9 datasets (SH17, SHEL5K, CHV, Pictor-PPE, Construction-PPE, GDUT-HWD,
SHWD, SODA, MOCS) escrito **antes** de la selección efectiva, con **licencias que el registro no
confirma** (GDUT-HWD "Apache-2.0" y SHWD "MIT" → nunca verificadas; CHV "CC BY 4.0" es la licencia
del *paper*, el dataset no declara licencia — limitación L7; MOCS descrito como el original de
41.668 imágenes con acceso por solicitud, cuando lo evaluado fue una copia pública de 1.471
imágenes). **Omite** `construction_site_safety` y `ppe_siabar`, incorporados al inventario después
del protocolo (junio de 2026) y que resultaron ser la fuente del núcleo curado del banco y del
entrenamiento. **Acción:** comprimir §17.1.6.2 a **(i)** los criterios C1–C7 (intactos), **(ii)**
una **ficha breve por dataset retenido** (SHEL5K, CHV, `construction_site_safety`, `ppe_siabar` —
como candidatos incorporados al inventario, con su licencia tal como figura en el registro) y
**(iii)** una **tabla de descartados con causa en una línea** (SH17: CC BY-NC-SA; Pictor-PPE:
licencia no verificable; Construction-PPE: AGPL-3.0; GDUT-HWD/SHWD: licencia sin verificar y
condición ya cubierta; SODA: cubre condiciones fuera del núcleo; MOCS: copia pública parcial, uso
sólo exploratorio). **Prohibido:** decir cuál se usó para entrenar y cuál para el banco con
cifras — eso es §17.4/§17.5. **Sí** puede decirse, como decisión de diseño, que **una fuente no
puede ser a la vez material de entrenamiento y estrato del banco** (es la Tabla 28 aplicada).
Ahorro esperado ~3.000 palabras. Las Tablas 27/29/31 se recortan a los retenidos.

### E2-15 · ⊘ · Tabla 28 — rango de entrenamiento 500–2.000 imágenes
**Verificado:** el entrenamiento efectivo usó 2.946 imágenes: **desviación no justificada en
ninguna bitácora**. **No se toca §17.1** (la nota de la Tabla 28 ya exige *"justificarse
explícitamente"*). **Handoff a §17.4/§17.5:** declarar la desviación y su causa (se tomó el 100 %
de los linajes elegibles tras deduplicación y exclusión de las fuentes del banco).

### E2-16 · ⊘ · §17.1.6.3 (MOT17 / OVT-B) y §17.1.7.4.2 (métricas MOT) — intactos (D-E2-6)
Pre-registradas y no ejercidas (exclusión de las métricas MOT con fundamento medido; no hay GT de
identidades). El texto **ya está en condicional** (*"deseables sobre subsets específicamente
preparados"*, *"función acotada de verificación"*). **No se edita, no se poda, no se "corrige".**
§17.5 las reporta en su bloque de caminos no ejecutados.

### E2-17 · 🟡 · §17.1.8 y Tabla 36 — las fases y el orden (AJ-2.08)
**Acción:** conservar los nombres de fase de la Tabla 36 y agregar una nota de protocolo: *"La
secuencia expresa dependencias entre fases, no un calendario: el orden y las fechas efectivas de
ejecución se documentan en la implementación."* Nada más — el orden real (EBE antes que la
sensibilidad de prompts; ajuste fino al final) es de §17.4.

### E2-18 · 🟠 · §17.1.7.3.1 — el nivel intermedio "estado observable por persona" (AJ-2.13, D-E2-5)
**Hoy:** la jerarquía distingue métricas primarias/secundarias/conceptuales y familias (detección
OVD, seguimiento, pipeline, operativas), pero **no nombra el nivel intermedio** entre la percepción
por imagen y la alerta temporal por episodio, que §17.5 usa como eje. **Acción:** agregar al
comienzo de §17.1.7.3.1 un párrafo de decisión:

> *"El framework distingue tres niveles de análisis, cada uno con su unidad de evaluación. El
> nivel de percepción evalúa las detecciones por imagen contra las anotaciones de referencia. El
> nivel de estado observable por persona evalúa, para cada persona detectada, si el estado
> derivado —presencia o ausencia del elemento de protección— coincide con la referencia,
> componiendo geométricamente las entidades detectadas sin requerir identidades persistentes ni
> seguimiento. El nivel de alerta temporal evalúa la alerta confirmada por episodio contra una
> referencia temporal anotada. Las métricas de detección alimentan el primero; precision y recall
> por persona el segundo; las métricas operativas del apartado 17.1.7.5, el tercero."*

**Opcional:** una fila en la Tabla 34 para *"Precision/Recall de estado por persona"* (nivel
secundario u obligatorio, a criterio). Sin cifras.

### E2-19 · 🟡 · §17.1.7 — diccionario de métricas y reparto con el diseño (AJ-2.03, D-P3-4)
**Verificado:** §17.1.7 **ya define** G2A (*Glass-to-Algorithm*, subtramo), el tramo
*Glass-to-Alert*, `t_alert-system`, `t_alert-notification`, TTFD, SDR y ΔFP_tracker, con la
Tabla 34 y los umbrales de la Tabla 35; §17.3.13 (v1.4) trae la **materialización** (relojes,
señales, estados de aplicabilidad). El reparto vigente es correcto: **§17.1 = nombres,
definiciones y criterios; §17.3 = materialización; §17.4 = valores efectivos.** **Acción:** sólo
verificar consistencia terminológica (G2A siempre *Glass-to-Algorithm*; el tramo hasta la alerta
siempre *Glass-to-Alert*; `t_alert-notification` "complementaria, sólo con trayecto instrumentado")
y que las **siglas nazcan con su nombre completo la primera vez** (TTFD, SDR y `t_alert-system`
nacen acá y §17.3 las usa). **No agregar** `t_capture→alert` ni `t_compute-budget` (D-E2-6 bis).

### E2-20 · 🟡 · §17.1.7.7.6 Tabla 35 ↔ Anexo D — la duplicación verificada (D-E2-9)
La tabla *"Umbrales orientativos por severidad"* aparece **dos veces** (mismo título, mismas
filas, mismos valores; la del Anexo D es superconjunto). **Acción:** conservar la Tabla 35 en
§17.1.7.7.6 (es donde se decide el criterio) y, en `90g`, reducir la del Anexo D a las filas que
agrega más una remisión a la Tabla 35. Las otras dos duplicaciones 🟡 de `ajustes/09` (Tabla 31 ↔
Anexo C; Tabla 34 ↔ detalle del Anexo D) se **confirman al aplicar** y se resuelven con el mismo
criterio.

### E2-21 · ⊘ · §17.1.7.8 — instrumentación: el protocolo no cambia (AJ-2.09)
El apartado **ya exige** los cinco hitos por alerta, P50/P95/P99 + promedio, warm-up, timestamps
monotónicos con fuente declarada y la bitácora mínima. **No se edita.** Lo que se cumplió y lo
que quedó parcial (cuatro de cinco hitos en el plano de control; percentiles del tramo de
plataforma sí, del evaluador de alertas sólo promedio; hardware y entorno no registrados por
corrida; warm-up de modelo sí, de unidades no) **se declara en §17.4** (handoff §F). La ficha
AJ-2.09 nombraba `report.json`/`metrics.json` como artefactos del plano de medios: no existen ahí
(`summary.json` + `metrics.jsonl`); corregido en la ficha, no afecta a §17.1.

### E2-22 · 🟠 · §17.1.7.8.2–.3 — estados de aplicabilidad y reglas de lectura (AJ-2.12, D-E2-3)
**Acción (a)** §17.1.7.8.2: agregar la regla de **estado de aplicabilidad**: *"Una métrica que no
corresponde medir se reporta con su estado y su causa (no aplicable por ausencia de referencia,
por fuente sin temporalidad, por trayecto no instrumentado), nunca como cero ni por omisión."*
**(b)** §17.1.7.8.3, junto a la unidad de conteo del falso positivo, la **regla de conteo**:
*"La re-emisión de una alerta por reconfirmación del mismo patrón tras su resolución no se
computa como falso positivo; se registra y se reporta por separado."* **(c)** §17.1.7.8.3, las
**reglas de lectura** como criterios: reportar **por estrato y escenario**, nunca sólo el agregado;
los materiales sin condición (negativos) **no entran** en precision/recall/F1 — su métrica es el
conteo de falsos positivos; la **SDR no se compara entre cadencias** de muestreo distintas; la
latencia de alerta **no se compara entre densidades** de evidencia sin controlar qué episodios
sobreviven. Todas son criterios pre-registrables; ninguna trae cifra.

### E2-23 · 🟠 · §17.1.9 y Tabla 37 — el encuadre del ajuste fino (AJ-2.11)
**Hoy:** la Tabla 37 ya dice *"la regla no prescribe que el fine-tuning deba ejecutarse; define
cuándo vale la pena"*. **Acción:** conservar la tabla y agregar, como decisión de protocolo, que la
rama **se ejerce como jornada experimental completa con criterios pre-registrados** (baseline
única, márgenes firmados antes de evaluar, veredicto por gate) y que sus condiciones son **de
datos y de protocolo, no de cómputo** (el nodo de entrenamiento existe: §17.1.4.3.1). **Buscar y
eliminar** cualquier formulación del tipo "según presupuesto de tiempo" o "si el cronograma lo
permite" en §17.1.9/§17.1.10. **Prohibido:** T1/T2/T3, cifras, veredictos (§17.4/§17.5).

### E2-24 · 🟡 · PODA-13 — §17.1.10 Proyección (659 palabras) → párrafo puente
Las "instancias posteriores" ya ocurrieron (§17.3–§17.5). **Acción:** reemplazar las cuatro
subsecciones por **un párrafo** que diga qué toma cada instancia posterior de esta consolidación
(entorno → diseño; condiciones y prompts → diseño y evaluación; datos → implementación; métricas →
evaluación), sin adelantar resultados. Renumerar: §17.1.11 → §17.1.10 y §17.1.12 → §17.1.11 **sólo
si** ninguna otra sección remite a ellas por número (verificar en `90`, `90b`, `90c`: hoy no hay
remisiones a 17.1.11/17.1.12). Ahorro ~450 palabras.

### E2-25 · 🟠 · §17.1.11.1 — el marcador espejo de la AAIP (D-E2-7, handoff de D-E1-11)
**Acción:** en la política de minimización y uso asistivo, insertar el marcador con el texto
exacto de §16.6.2.2: `[[PENDIENTE: definir con el equipo la aplicabilidad de esta inscripción al
contexto experimental y documentar el recaudo adoptado en §17.1 y §17.4.]]`. **No redactar** una
respuesta: es decisión del equipo y el marcador viaja.

### E2-26 · ⊘ · AJ-2.02 — premisa falsa
La ficha decía que *"el §17.1 también describe la política de alerta y arrastra el mismo error"*
(cooldown en el motor). **Verificado:** §17.1 no menciona cooldown, supresión, re-alertas ni
re-notificación (cero apariciones; ya lo había verificado el pase 2 de la Etapa 3). Lo único
cercano es la frase de la histéresis, precisada en E2-08. La regla `re-alerta ≠ FP` entra por
E2-22. **Se cierra como ⊘.**

---

## C. Pase 2 — formato y terminología (después del contenido, como en la Etapa 1)

Se aplica **sobre la entrega del pase 1**, nunca sobre el documento inicial (lección del 08-28:
entregar siempre el último final). Mismas seis reglas F1–F6 del pase 5 de la Etapa 1:
**F1** títulos en tipo frase (hoy §17.1 está en Title Case: *"Función y Alcance de la
Consolidación Metodológica"* → *"Función y alcance de la consolidación metodológica"*), respetando
las siglas; **F2** rótulos `**Tabla N**` (hoy `***Tabla N***`); **F3** notas `*Nota.*` (hoy `Nota.`
sin formato y una variante `**Nota***.*`); **F4** rótulos de párrafo con el punto dentro de la
negrita; **F5** terminología: *cuadro* (no frame/fotograma, salvo "frame-a-frame" si se conserva
como término técnico → preferir *cuadro a cuadro*), *extremo a extremo*, *seguimiento* (no
tracking, salvo tracking-by-detection); **F6** siglas definidas en su primera aparición. **Las
ecuaciones de Word no se tocan.** Verificación: `verificar_entregable.py <entrega.docx> --seccion
17.1` en OK, cero `[[…]]` salvo el de la AAIP, cero andamiaje.

---

## D. Lo que NO hay que tocar en este pase

1. **§17.1.5** (9.426 palabras) y **§17.1.7** (6.605): protocolo ejercido y framework de métricas —
   sólo las inserciones puntuales listadas (E2-07…E2-13, E2-18…E2-22). Sin compresión.
2. **Los objetos de ecuación** (`t_alert-system`, `t_alert-notification`, `G2A`, `T_persistencia`,
   `ΔFP_tracker` y los 85 restantes): se ven como `⟦ECUACIÓN⟧` en la extracción y vacíos en las
   tablas. **Verificar en el `.docx` final que la sigla de §17.1.7.5.1 se lea** (pase 3 §I).
3. **Tabla 24** (ventanas y trade-off por severidad): §17.3.10.3 la cita y no la toca.
4. **CPN / EN / TN** (§17.1.4.2) y las siglas **TTFD / SDR / `t_alert-system`** (§17.1.7.5): nacen
   acá; §17.3 y §17.4 las usan sin redefinir. No renombrar, no mover.
5. **§17.1.4.4** (escenarios): única remisión numérica desde §17.3/§17.4. No renumerar.
6. **P-E1-xx**: los seis códigos que §17.1 invoca son parte del informe (excepción de la regla de
   andamiaje).
7. Todo el §1 de `nucleo/historicos/08` — lo que el informe **valida**.

---

## E. Anexos C y D — se corrigen aparte (D-E2-1) → `90g-etapa2-anexos-c-y-d.md`

Texto base: `96e` §19.3–§19.4. Correcciones: **(a)** Anexo C, catálogo de datasets: separar
**candidatos evaluados** de **retenidos**, y dentro de los retenidos distinguir **material de
entrenamiento** de **fuentes del banco de imágenes** — **sin** afirmar que `chv` se entrenó (el
entrenamiento efectivo lo excluyó; el rol "TRAIN" que las fichas viejas le daban era histórico);
`bench_obra` **no es un dataset** sino el estrato curado a partir de `construction_site_safety`;
licencias como en el registro (E2-14). **(b)** Anexo C, Tabla C.1: es la fuente declarada del
prompt set (E2-13). **(c)** Anexo D: tabla de umbrales reducida a lo que agrega + remisión a la
Tabla 35 (E2-20); confirmar las otras dos duplicaciones. **(d)** Anexo B: **no se edita**; recibe la
lista de "altas" que produzca E2-06. El equipo integra los anexos en §19.

---

## F. Handoffs que salen de esta etapa

| Hacia | Qué | Origen |
|---|---|---|
| **Etapa 3 (§17.3 v1.4 → v1.5)** | Recortar la glosa de §17.3.6.4 a la remisión *"…estrategias directa (E-DIR) e híbrida (E-HYB) definidas en la consolidación metodológica"*; revisar el solape §17.3.3.1 ↔ §17.3.3.2 con lo que quede en §17.1 (pase 3 §I). | E2-09 · D-E2-2 |
| **Etapa 4 (§17.4 v1.6)** | Declarar: orden de disparo real **control → distribución → medios** (hoy §17.4 dice "inverso al flujo de datos"); desviación del rango 500–2.000 (2.946) con causa; artefactos del plano de medios (`summary.json`/`metrics.jsonl`, no `report.json`); 4/5 hitos; percentiles sólo del tramo de plataforma; hardware/entorno no registrados por corrida; warm-up de unidades = 0; SO Linux/WSL2; G2A desde el dequeue y sin tramo sensor/red en RTSP. | E2-15 · E2-21 · `operacion/130` §4 |
| **Etapa 5 (§17.5 v1.3)** | Reportar como no ejercidos: templates de prompt, vocabulario aislado-vs-completo cruzado (sustituido por el control B1 vs T2), español, doble anotación/kappa (L2), MOT17/OVT-B y métricas MOT, confianza media de TP; piso de 200 positivos sólo en CR-01/shel5k (L8); citar `n=5.313` **fechado** (GT del 23-jul; 5.308 con el vigente); comparación tiny 800 vs 560 con el caveat del umbral (0,35 vs 0,30); `t_alert-system` del banco es promedio por campaña. | E2-10 · E2-12 · E2-16 · `operacion/130` R-04/R-05/R-11 |
| **Anexos (§19, equipo)** | `90g` con Anexos C y D corregidos; altas al Anexo B. | E2-06 · §E |
| **Equipo** | D-E1-11 (AAIP) sigue abierta; el espejo viaja en §17.1.11.1. | E2-25 |

---

## G. Hechos verificados que este pase usa — NO "corregir" estos valores

| Hecho | Valor | Dónde se re-verifica |
|---|---|---|
| Texto base | 32.669 palabras · 122 títulos · 664 párrafos idénticos al `96b` · 85 ecuaciones OMML | `extraer_informe.py` + diff normalizado (`revision-previa-etapa-2.md` §1) |
| Persistencia adoptada | CR-01 4.000/2.000 ms · CR-02 7.000/3.000 ms · escena · sin cooldown | `e-ovrt_control-plane/configs/patterns/cr01_cr02_v2.yaml` |
| Códigos E-DIR/E-IND/E-HYB en §17.1 | **0** apariciones | `grep -c E-DIR 90f-…md` |
| Cooldown / re-alertas en §17.1 | **0** apariciones | `grep -ciE 'cooldown|re-?alert|supresi' 90f-…md` |
| P-E1 invocados por §17.1 | 01, 02, 03, 04, 06, 08 (9 veces) = los seis de §16.7.3 | `grep -o 'P-E1-[0-9]*' 90f 90d` |
| Remisión rota | `16.7.6` ×1 (§17.1.6.1.1) | `grep -n '16\.7\.6' 90f-…md` |
| Remisiones desde §17.3/§17.4 a §17.1 | sólo `17.1.4.4` ×1 | `grep -ohE '17\.1\.[0-9.]+' 90 90b` |
| Fine-tuning efectivo | css 2.203 + ppe_siabar 743 = 2.946 train / 483 val; `chv` excluido | `finetuning/manifests/finetuning_v1.summary.json` |
| Anexo B | Tablas B.1–B.7 existen en `96e` §19.2 | `grep -oE 'Tabla B\. ?[0-9]' 96e` |
