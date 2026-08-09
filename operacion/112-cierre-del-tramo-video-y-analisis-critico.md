# 112 — Cierre del tramo de video: qué se hizo, qué salió, y una lectura crítica

**Fecha:** 2026-08-09. **Qué es:** el registro completo del tramo que arrancó cuando
llegaron las anotaciones de CVAT del lote de internet y termina con la campaña gen. 3
corrida y propagada — **10 documentos (102→111), 4 jornadas**. La primera mitad es
descriptiva y verificable contra artefactos; **la segunda (§7 en adelante) es una
lectura crítica y opinada**, marcada como tal.

**Para quién:** para vos, antes de decidir cómo se cuenta esto en el informe. No es un
doc de procedencia (esos son el 109 y el 111): es el que dice **qué significa lo que
salió y dónde están los riesgos**.

---

## 1. El arco, en una línea

Llegaron 7 anotaciones → el GT desmintió la mitad de las etiquetas de curación → las
campañas mostraron un doble colapso → el diagnóstico por capas encontró la **frontera de
juzgabilidad** → se probaron todas las palancas de configuración y **ninguna alcanzó** →
un clip fresco **refutó la mejor palanca** → llegaron 8 clips más → se reorganizó todo
con fuente única → y la corrida final **encontró un bug de métrica que ya estaba
publicado**.

## 2. Lo que se hizo, por jornada

| doc | qué produjo |
|---|---|
| **102** | GT de los 3 primeros clips del lote + rescate de los 4 pilotos del 18-07. Banco 34→37 |
| **103** | I1/I2 corridas: el doble colapso (`scene` recall 0,000 / `subject` precision 0,010) + §7 diagnóstico por capas |
| **104** | 3 ajustes probados **solo con configuración**: gate re-calibrado, `base-560` refutado, escena irreparable en denso |
| **105** | Los 4 pilotos recuperados de CVAT → **Nivel A sobre video**, primera vez |
| **106** | Relevamiento y plan de continuación |
| **107** | Matriz de knobs completa (los 3 restantes) + mecanismos + tests del scorer |
| **108** | `v04_c02` (2º nocturno) + **control out-of-sample que refutó la palanca ganadora** + corrección firmada de `v06_c01` |
| **109** | **Reorganización**: 3 estratos × 2 niveles, campaña citable vs evidencia exploratoria, fuente única |
| **110** | `v03_c02` + primera corrección hacia `unknown` |
| **111** | **Cierre del lote (13/14)** + política de fuente de verdad + gen. 3 corrida + bug de FAR |

**Material final:** banco **47 clips** (34 rodaje + 13 internet), 40 episodios, 13
negativos, **1 soak**, `v08_c01` excluido con causa firmada, 4 pilotos en `_retired/`
para Nivel A.

**Herramientas nuevas** (todas medición, ADR-015 intacto): `score_clip_person_state.py`
(Nivel A sobre video, 8 tests) · `apply_attribute_corrections.py` (correcciones firmadas
con `previous_value`, `track_id` y `--check`, 16 tests) · `109-verificar-organizacion.py`
(auditoría reejecutable de 6 reglas) · runners y barridos.

## 3. Los resultados

### 3.1 Nivel B — estrato B (13 clips, gen. 3)

| | `scene` | `subject` | rodaje T1 / G1 |
|---|---|---|---|
| recall | 0,750 | **1,000** | 0,824 / 0,971 |
| precision | **0,375** | 0,111 | 0,757 / 0,892 |
| **F1** | **0,500** | 0,200 | **0,789 / 0,930** |
| FAR/hora (soak) | **29,2** | 1.850,8 | — (no había soak) |

### 3.2 Nivel A — 17 clips de video

| material | CR-01 F1 | CR-02 F1 |
|---|---|---|
| imágenes (`bench_obra`) | **0,408** | **0,479** |
| video (17 clips) | **0,039** | **0,020** |

El derrumbe es **de precision**: el recall se sostiene en 0,37 / 0,27.

### 3.3 Los hallazgos con nombre

| | qué dice |
|---|---|
| **F-103.1/2** | El doble colapso tiene mecanismo: `scene` queda capturada por evidencia perpetua en multitud; `subject` fragmenta identidades (182 con FP > 127 personas reales) |
| **F-104.1** | El "gate de juzgabilidad" **ya existía** como config (`min_subject_area_px`) en 400 px²: no faltaba capacidad, faltaba re-calibrar fuera de su régimen |
| **F-104.2** | El bajo conteo de FP de `scene` era el **latch** de la escena capturada, no discriminación |
| **F-104.3/4** | `base-560` refutado; y la alucinación de la clase de evidencia **suprime** alertas (el error de un lado enmascara el del otro) |
| **F-105.2/3/4** | La juzgabilidad tiene **tres ejes** (escala × iluminación × oclusión); el `unknown` del anotador **no** predice el F1 del modelo — la brecha es el contexto temporal |
| **F-107.1/2/3** | Matriz de knobs: la confianza del sujeto es la mejor palanca (−48% FP), la de evidencia no es accionable, la persistencia cuesta latencia |
| **F-108.1/2** | No hay "mejor granularidad", hay una correcta por densidad; y **la mejor palanca in-sample costó un episodio real fuera de muestra** |
| **F-109.1** | El pipeline DBE es **determinista**, verificado dos veces |
| **F-111.1/2** | Con el lote completo `scene` le gana a `subject`; y el FAR/hora corregido es estable entre generaciones |

## 4. Lo que se corrigió (y estuvo mal publicado)

Tres cosas se midieron mal antes de detectarse. Las tres están corregidas, con banner en
los docs originales:

1. **El GT de `v06_c01`** tenía un episodio CR-02 que era **error de anotación**
   (revisión visual del usuario). Al corregirlo, el clip pasó a negativo y se volvió el
   **primer clip soak del banco** — habilitando FAR/hora.
2. **El GT de `v03_c02`** tenía un episodio CR-01 de 4.000 ms **exactos** sostenido por
   atributos no observables (operador en cabina). Corregido a `unknown`.
3. **`far_per_hour` estaba mal calculado** en el agregador: numerador de todos los
   negativos, denominador de solo los soak. Inflaba **7×** con 9 negativos. Las cifras
   publicadas (48,7 y 2.045,6) eran incorrectas; las correctas son **29,2 y 1.850,8**.

---

# LECTURA CRÍTICA

*Lo que sigue es opinión fundamentada, no registro. Está separado a propósito.*

## 5. Lo que este tramo hizo bien, y conviene defender

**El rigor metodológico es el activo más fuerte del trabajo, más que cualquier número.**
En cuatro jornadas: correcciones de GT con firma y `previous_value` verificado;
exclusiones declaradas con causa en vez de silencio; separación explícita entre campaña
citable y evidencia exploratoria; freezes verificables; determinismo comprobado dos
veces; y —lo más difícil— **una refutación voluntaria de la propia mejor palanca**
(F-108.2). Muy poco trabajo experimental se somete a un control out-of-sample cuando el
resultado in-sample ya es favorable.

**Los hallazgos son mecanicistas, no descriptivos.** Ninguno dice "salió mal": todos
dicen *por qué*, verificado en `alerts.jsonl` crudos. Eso es lo que hace que el capítulo
sea defendible aunque los números sean malos.

**La frontera de juzgabilidad es una contribución real.** No estaba en el plan: salió de
mirar por qué fallaba. Que tenga tres ejes medidos (escala × iluminación × oclusión) y
que se haya refutado el atajo obvio (el `unknown` del anotador como índice) le da
solidez.

## 6. El riesgo grande: cómo se enmarcan estos números

**Los resultados del estrato B son malos.** F1 0,500 en el mejor caso contra 0,789/0,930
del rodaje; Nivel A 0,039/0,020 contra 0,41/0,48 en imágenes; 29 falsas alarmas por hora
en el mejor caso. Hay dos maneras de contarlos y **solo una es honesta**:

- ❌ *"Validamos la plataforma sobre obra real"* — falso. No se validó: se midió, y la
  medición dice que fuera del régimen del rodaje el sistema no es operable.
- ✅ *"Medimos el borde del sobre de operación y lo caracterizamos por mecanismo"* — eso
  es lo que se hizo, y es una contribución legítima.

**Mi recomendación:** el capítulo del estrato B se titula por lo que mide (la frontera),
no por el material. Si se presenta como "generalización a obra real" invita exactamente
la pregunta que no tiene buena respuesta.

## 7. Cinco cosas que me preocupan

### 7.1 El `n` es diminuto, y mi propia redacción lo estira

**4 episodios evaluables en 13 clips.** F-111.1 —"`scene` le gana a `subject` y la brecha
se agranda"— descansa sobre eso. Lo escribí con más énfasis del que el `n` aguanta: la
diferencia entre F1 0,500 y 0,200 sobre 4 episodios y 5 vs 32 FP no tiene intervalo de
confianza que la sostenga como ranking. **Es una observación, no un resultado
comparativo.** Si en la defensa alguien pregunta "¿con cuántos episodios?", la respuesta
—cuatro— desarma la afirmación fuerte. **Sugiero bajarle el tono en el informe**: decir
que en este régimen la ventaja de la identidad *no se reproduce*, sin afirmar el orden
inverso.

### 7.2 El GT tiene un sesgo en la misma dirección que el error del modelo

De los **5 episodios positivos** que el lote produjo, **2 resultaron errores de
anotación** (`v06_c01` y `v03_c02`), ambos detectados por revisión visual **después** de
haber producido resultados, y ambos en sujetos difíciles de juzgar (persona al borde del
plano; operador en cabina). En los dos casos la corrección **eliminó** una violación.

Eso es un patrón, no dos casualidades: **el anotador sobre-declaró violaciones justamente
donde el estado no era observable** — el mismo error que comete el motor. Es coherente
con la tesis de juzgabilidad, pero tiene una consecuencia incómoda: **el GT no es un
árbitro independiente del fenómeno que mide**. Y queda uno pendiente: el episodio de
`v01_c01` está marcado para revisión por la misma causa (sujeto a contraluz dentro del
edificio). **Si también es error, el estrato B se queda con 3 episodios evaluables.**

**Sugerencia:** revisar `v01_c01` antes de escribir, y declarar en el informe que 2 de 5
episodios del estrato fueron corregidos tras revisión visual — es un dato de calidad del
GT que fortalece, no debilita, si se dice de frente.

### 7.3 El bug de `far_per_hour` es una señal, no un incidente aislado

Estuvo mal, se publicó en tres documentos, y **se detectó de casualidad**: porque al
pasar de 2 a 9 clips negativos el número quedó raro. Con la composición anterior la
distorsión era 1,2× y era invisible. El agregador **tenía tests** y el bug pasó igual,
porque ninguno ejercitaba la combinación "varios negativos + un solo soak".

La pregunta que deja abierta: **¿qué otra métrica tiene una inconsistencia latente que
la composición actual de datos no estresa?** Candidatas por la misma familia: los
promedios de `t_alert`/TTFD/SDR sobre conjuntos heterogéneos, y la imputación de FP por
condición (que ya sabemos que solapa). No digo que estén mal; digo que **nadie las
sometió a un cambio de composición que las rompa**.

**Sugerencia concreta y barata:** antes de citar cifras en el informe, correr cada
métrica del agregador contra una fixture sintética con composición extrema (1 clip, 100
clips, todos negativos, todos positivos). Es media jornada y protege el capítulo entero.

### 7.4 La documentación puede estar sustituyendo a la tesis

**10 documentos operativos en 4 jornadas.** Son buenos y están verificados — pero el
informe sigue sin arrancar, la defensa es a fines de septiembre, y tu propio orden del
05-08 ponía la redacción tercera. El patrón que veo: **cada clip nuevo abre hallazgos, y
los hallazgos generan documentación, que a su vez sugiere más experimentos.** Ya lo
señalé una vez ("el efecto imán") y volvió a pasar.

Lo digo derecho: **el trabajo experimental de video está terminado y bien terminado.**
Seguir midiendo tiene retorno decreciente; escribir tiene retorno alto y es lo único que
no se puede delegar al final. La tentación va a reaparecer con los videos V1–V3.

### 7.5 Dos deudas administrativas que pueden morder tarde

- **La URL por video del lote sigue en `TODO`** en los 14 `clip.yaml`. Es evidencia
  perecedera (los videos de YouTube se borran) y es lo que sostiene la cita de la fuente
  de todo el estrato B. **Es media hora de trabajo y no la hizo nadie en 4 días.**
- **Deuda git: 172 archivos sin commitear** (docs 61, datasets 96, exp-setup 12,
  control-plane 3). Cuatro jornadas de trabajo verificado viven solo en el working tree,
  y `docs` no tiene remoto por decisión del proyecto. **El backup a otro disco sigue
  pendiente desde el 05-08.**

## 8. Qué haría yo, en orden

1. **Revisar `v01_c01`** (15 min): define si el estrato tiene 4 o 3 episodios.
2. **Anotar las URLs** de los 13 videos (30 min): cierra la deuda de evidencia perecedera.
3. **Commitear y hacer backup** (30 min): 4 jornadas sin respaldo es riesgo puro.
4. **Stress-test del agregador** con fixtures de composición extrema (media jornada):
   protege todas las cifras del informe.
5. **Videos V1–V3** — con una caja de tiempo dura, y sin abrir frentes nuevos.
6. **Redacción §17.x.** Con el material que hay, alcanza.

**Lo que NO haría:** anotar `v08_c01`, buscar más clips, ni correr más barridos. El
material dice lo que tiene para decir.

## 9. Balance

El tramo de video entregó **más de lo que el plan pedía**: no solo levantó L4, sino que
produjo una caracterización mecanística de dónde y por qué el sistema deja de funcionar
— que es un resultado más interesante que un F1 alto sobre material fácil.

El riesgo no está en los datos ni en el método: **está en el calendario y en el
encuadre.** Los números son malos y hay que contarlos como lo que son —una frontera
medida— antes de que alguien los lea como una validación fallida.
