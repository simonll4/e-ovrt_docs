# 103 — Corrieron I1/I2: ninguno de los dos "gana", y por qué eso es el hallazgo

**Fecha:** 2026-08-06. **Insumo:** el GT del estrato B (doc 102) + las dos campañas
armadas ese mismo día. **Salida:** I1 y I2 corrieron de punta a punta contra los
3 clips del lote de internet — GPU real, sin fixtures. Este doc dice qué salió y por
qué **los números NO se leen como otra fila de la tabla de T1/G1**: revelan, amplificado
al extremo, un mecanismo que el banco del rodaje solo había mostrado en miniatura.

**No confundir con el doc 102** (que cerró el GT y armó las campañas, sin correrlas).
Este es el que corre y audita los resultados.


> ## ⚠️ CORRECCIÓN POSTERIOR — leer antes que nada (2026-08-07, doc 108 §6)
>
> Este documento se escribió cuando el GT de **`v06_c01` tenía un episodio CR-02**
> (342.400–355.533 ms). La revisión visual en CVAT determinó que **era un error de
> anotación: la persona SÍ llevaba chaleco**. El episodio **no existe**; `v06_c01` es
> **negativo** (P5) y pasó a ser **el primer clip soak del banco**.
>
> **Qué NO cambia (todo el análisis de mecanismo de este doc):** la evidencia perpetua
> del modo escena, la fragmentación del tracker, el colapso de la asociación de `vest`
> con la escala, el acople alucinación↔supresión. Todo eso se midió sobre las
> **detecciones**, que no cambiaron.
>
> **Qué SÍ cambia:** los conteos que tratan a `v06_c01` como clip positivo. Sus alertas
> ya no son "el episodio que el motor no encontró" sino **falsas alarmas sobre un
> negativo**. Cifras vigentes: `results/clip_bench/index.md` y doc 108 §6.


---

## 1. Los números, tal como salieron

| | I1 (scene) | I2 (subject) |
|---|---|---|
| recall (2 episodios) | **0,000** (2/2 missed) | **1,000** (2/2 matched) |
| precision | 0,000 | **0,010** |
| F1 | — | 0,020 |
| FP (positivos) | 5 | **196** |
| FP (negativo, `v10_c01`) | 2 | 20 |
| re_alerts | 0 | 7 |
| SDR | 0,997 | 0,997 (idéntico — mismas cajas) |
| duración | 32,7 min GPU | 24,8 s (sin GPU) |

Ninguna de las dos filas es "el resultado". Publicar solo I1 diría "el sistema no
detecta nada en obra real" (falso: el modelo SÍ percibe, SDR 0,997). Publicar solo I2
diría "la identidad recupera el 100% del recall" y ocultaría que **precision 0,01
significa que 99 de cada 100 alertas son ruido**. Las dos juntas son el hallazgo.

## 2. Por qué — verificado en los `alerts.jsonl` y `pattern_events.jsonl` crudos, no supuesto

### F-103.1 — Escena: la alerta del violador real cae DENTRO de la ventana de tiempo pero FUERA de la máquina de estados

`v06_c01` tiene 127 tracks en el GT — el clip más denso de todo el banco (el rodaje
nunca superó 14). El motor de escena confirma su **primera** alerta CR-02 a `t=7.000 ms`,
con evidencia acumulada **desde `t=0`** de **8 sujetos simultáneos** sin chaleco
(`subjects_in_evidence: 8`, verificado en `pattern_events.jsonl`). En una obra real con
decenas de personas cruzando el plano, alguien sin chaleco detectado —cierto o
falso— casi siempre desde el primer segundo.

Consecuencia: la condición CR-02 a nivel escena **nunca vuelve a "cumplimiento"** durante
los 6:09 del clip — siempre hay evidencia de ALGUIEN sin chaleco en alguna parte del
plano. El motor queda en un único estado "en violación" continuo desde `t=7.000 ms` en
adelante. Cuando el violador real empieza su infracción a `342.400 ms`, el motor **no
tiene un onset fresco que confirmar**: ya estaba alertado por otra persona, y no vuelve
a alertar por la misma condición hasta que la evidencia se **agote por completo**. La
única otra alerta CR-02 de todo el clip es esa primera, a `t=7.000 ms` — la del
violador real **no aparece en ningún lado del `alerts.jsonl`**.

> Esto **es exactamente el mecanismo (a) de F-81.2** (doc 81/89: *"bajo escena el
> motor acumula 'alguien sin casco', pero el GT exige que un sujeto individual
> sostenga la violación; en multitud los sujetos se relevan y la escena nunca deja
> de estar en evidencia"*) — descubierto en el rodaje sobre P7 (2 personas) y
> **corregido con G1**. Acá, con 127 personas reales en vez de 2 guionadas, el mismo
> mecanismo no atenúa la alerta: la **elimina por completo**. La miniatura del
> rodaje predijo la dirección; la magnitud real es otra categoría.

### F-103.2 — Sujeto: recupera el recall, pero el tracker del modelo multiplica el ruido por la multitud

Bajo `subject`, el violador real SÍ confirma (`matched_alerts_count: 1` en cada clip
positivo) — la identidad resuelve exactamente el problema de F-103.1, igual que hizo
G1 en el rodaje (F-89.1). Pero el precio escala con la escena, no con el modelo:

- `v06_c01`: **182 identidades distintas** del tracker (`SimpleIoUTracker` post-hoc,
  sobre las MISMAS cajas de I1) dispararon al menos una alerta falsa — **más que los
  127 tracks que el GT humano contó**. El tracker del modelo fragmenta identidades
  reales en varias más cortas (oclusión, distancia, resolución) y cada fragmento que
  acumula ≥7 s de "sin chaleco" continuo confirma su propia alerta independiente.
- `v04_c01` (1 solo violador real, 6 tracks en el GT): **9 alertas falsas**, de **8
  identidades distintas** del tracker — más identidades falsas que personas reales
  en el clip. Nocturno, poca luz: el mismo mecanismo, a menor escala.
- `v10_c01` (negativo, 6 tracks GT): 2 FP a escena, **20 FP a sujeto** — la misma
  multiplicación en un clip sin ninguna infracción real.

**La conclusión no es "el tracker es malo".** Es que el mecanismo de identidad
(`subject`) evalúa a **cada entidad rastreada** de forma independiente, así que su
superficie de falsos positivos escala con **cuántas entidades hay en cuadro** — y
"cuántas entidades" incluye tanto a las personas reales como a los fragmentos que el
tracker crea por su cuenta. El rodaje nunca lo expuso porque su clip más poblado tenía
14 tracks reales (rango típico 1–5); acá hay 127.

## 3. Qué dice esto de la tesis, con cuidado

**No es una contradicción de G1 en el rodaje — es su límite de aplicabilidad, medido.**
La ganancia de la identidad (doc 89, F1 0,789→0,930) es real y quedó re-confirmada acá
en el eje de recall (2/2 vs 0/2). Lo que este estrato agrega, que el rodaje no podía
medir por construcción (máximo 14 personas por clip, guionadas y controladas), es que
**la ganancia tiene un costo que crece con la densidad de la escena**, y a partir de
cierta densidad ese costo es catastrófico para precision. `v06_c01`, con 127 personas
reales, es el primer punto del banco fuera del rango de densidad que el rodaje ejerció.

**Tampoco es un fracaso de `scene`.** F-103.1 muestra que la escena, lejos de "fallar
sin motivo", queda **capturada por un mecanismo específico y explicable** (evidencia
perpetua por multitud) — no es ruido, es el resultado predicho por F-81.2(a) llevado a
su extremo.

**Dos lecturas posibles para el capítulo, ninguna descartada acá:**
1. La densidad real de una obra activa (decenas de personas) está **fuera del régimen
   de operación validado** de esta plataforma con esta configuración — es una
   limitación nueva, más específica que L4, y hay que nombrarla.
2. El banco tiene **n=1 clip** en ese régimen de densidad — no alcanza para
   generalizar "la plataforma no sirve con multitudes", solo para decir "con ESTE
   clip, con AMBAS granularidades, el resultado es inutilizable operativamente".

La decisión de cuál lectura (o ambas) entra al informe, y con qué nombre de
limitación, es del equipo — no la tomo acá.

## 4. Lo que esto NO permite hacer

- **No comparar `v04_c01`/`v06_c01`/`v10_c01` fila a fila contra T1/G1** como si fueran
  3 clips más del mismo régimen — la tabla de `results/clip_bench/index.md` ya
  advertía esto (D-90.6) antes de correr, y el resultado lo confirma con más fuerza de
  la esperada.
- **No promediar `v06_c01` con `v04_c01`/`v10_c01`** en ningún agregado que se vaya a
  citar: mezclaría un clip de densidad extrema (127 personas) con dos de densidad
  normal (6 personas cada uno) y el agregado no significaría nada. `aggregate_clip_campaign`
  ya lo hizo bien (micro sobre 2 episodios, con el desglose por escenario que aísla
  P1/P2), pero el punto es no ir un paso más allá al citarlo.
- **No usar `precision=0,010` de I2 como "la precision de G1"** en ningún lado — es la
  precision de G1 **específicamente contra un clip de densidad extrema que el rodaje
  nunca ejerció**, no una medición de la técnica en general.

## 5. Estado de los artefactos

Ambas campañas cerradas y agregadas (`aggregate_clip_campaign`, reglas con test:
negativos fuera de P/R/F1, `re_alerts` no son FP, desglose por escenario). Artefactos en
`results/clip_bench/{i1,i2}_gdinotiny560_*_internet/` (`campaign.yaml` completo,
`metrics.json`, `evals/`, `provenance.json`). Verificado antes de escribir este doc:
`alerts.jsonl` y `pattern_events.jsonl` crudos de los 6 runs de control (3 clips × 2
granularidades), no solo los `metrics.json` agregados.

**Pendiente, a decisión del equipo:**
1. Si esto entra al informe como limitación nueva (densidad de escena) o como
   ampliación de L4/L6, y con qué nombre.
2. Si vale la pena anotar más clips del lote de internet buscando densidad
   intermedia (entre 6 y 127 personas) para saber si el quiebre es gradual o abrupto
   — hoy el banco tiene un solo punto de dato ahí.
3. La fila en `results/clip_bench/index.md` (§6 abajo) queda escrita con este marco;
   revisarla si el equipo decide otra lectura.

> ✎ **CERRADO 2026-08-09 (D-113.1, doc `operacion/113` §A5) — los dos ítems.**
> **(1) Se precisa L4, no se crea `L9`**: el set L1–L8 de `informe/99` §6 sigue
> cerrado; la frontera de juzgabilidad (tres ejes: escala × iluminación × oclusión,
> F-105.2/3/4) es el contenido nuevo de L4, no una etiqueta aparte. Celda vigente:
> `results/index.md` §L4. **(2) NO se anota más material en densidad intermedia** —
> el lote se cerró en 13/14 (docs 109–111) y el doc 112 §8 lo ratifica: el material
> dice lo que tiene para decir, y más clips es retorno decreciente sobre redacción
> pendiente. El quiebre gradual-vs-abrupto queda **fuera de alcance de esta tesis**.

## 6. Fila para `results/clip_bench/index.md`

Ya integrada (ver el índice) con el mismo encuadre de este doc: números completos +
la explicación de mecanismo, no una fila numérica sola.

---

## ✎ §7 — Addendum (mismo día, más tarde): diagnóstico por capas — ¿plataforma o naturaleza del modelo?

Tres mediciones nuevas sobre artefactos ya existentes (cero GPU, cero inferencia
nueva; scripts `datos/103-diagnostico-juzgabilidad.py` y `datos/103-gate-sim.py`,
salida en `datos/103-gate-sim/`), más auditoría visual de frames reales de los 3
clips. Refinan la atribución del §2 — y **corrigen el nombre del eje**: la variable
raíz no es la densidad sino la **juzgabilidad del sujeto (escala × iluminación)**;
la densidad multiplica la superficie de FP y produce la captura del modo escena,
pero no es necesaria para el FP (v10, con 6 personas, generó 20).

### 7.1 La evidencia de ausencia es mayormente fallo de percepción a escala chica — MEDIDO

Asociación de `vest` a cada detección `person` (proxy: centro del vest dentro del
torso del person), sobre las detecciones crudas de I1:

| altura del sujeto (px @1080p) | v06 (127 pers., diurno) | v10 (diurno) | v04 (**nocturno**) |
|---|---|---|---|
| < 80 | 0,0% | 0,0% | 0,0% |
| 80–120 | 10,8% | 9,1% | 0,0% |
| 120–160 | 16,8% | 14,1% | 6,1% |
| 160–220 | 57,0% | 51,9% | **8,7%** |
| 220–320 | 73,2% | 62,9% | **13,2%** |
| ≥ 320 | (n=526) 41,4% | — | **55,1%** |

Contraste con el rodaje (T1, mismas clases, mismo modelo): `a_p1_c02`/`a_p7_c01`/
`a_p5_c01` tienen **mediana de altura de person 716–839 px** y asociación de vest
**96–100%**. Los clips de internet: mediana 188–340 px. **El rodaje validó la
plataforma en un régimen (≥320 px, diurno) donde la heurística de ausencia es
confiable; el estrato B vive fuera de ese régimen.** Auditoría visual: en los frames
de v06 prácticamente TODOS llevan chaleco naranja visible al ojo humano — la
"evidencia de ausencia" del motor es el detector no viendo chalecos chicos, no gente
sin EPP. Y v04 muestra el segundo eje: **de noche la asociación colapsa a cualquier
tamaño** (55% incluso en sujetos ≥320 px).

### 7.2 El tracker fragmenta 11–15× — multiplicador, no raíz

`SimpleIoUTracker` produjo **1.474 tracks para 127 personas** en v06 (11,6×), 90
para 6 en v10 (15×), 37 para 6 en v04. Es la explicación de "182 identidades con FP
> 127 personas". Mejorable barato (ByteTrack ya está en el toolchain de
pre-anotación; gating por edad de track). Pero es multiplicador: con tracker
perfecto, la asociación de vest al 57–73% en el rango 160–320 px seguiría
sosteniendo ausencias de ≥4/7 s en decenas de sujetos reales.

### 7.3 Gate de juzgabilidad simulado post-hoc: ayuda mucho, NO alcanza

Filtrando del stream trackeado de I2 los `person` con altura < H y re-corriendo
replay+evaluate (mismas cajas, `datos/103-gate-sim.py`):

| H (px) | matched | missed | FP total | Δ FP |
|---|---|---|---|---|
| 0 (control = I2) | 2 | 0 | 216 | — |
| 120 | 2 | 0 | 166 | −23% |
| 160 | 2 | 0 | 128 | −41% |
| 200 | 2 | 0 | **84** | **−61%** |

Los 2 episodios reales sobreviven hasta H=200 — pero **no hay margen para subir
más: el violador real de v06 mide 216 px de mediana** (GT humano, ventana del
episodio; el de v04, 401 px). **El violador vive en la misma escala que el ruido.**
Y los 9 FP de v04 no se mueven con ningún H: son de iluminación, no de tamaño.
El gate convierte "inutilizable" (precision 0,010) en "malo" (~0,024), no en
"bueno".

**Advertencia metodológica:** la simulación es ajuste *in-sample* sobre el mismo
clip que motivó la hipótesis — atribuye mecanismo, no elige umbral. Cualquier gate
real se valida con clips frescos.

### 7.4 Veredicto por capas

| capa | atribución | ¿ajustable? |
|---|---|---|
| Percepción: recall de `vest` colapsa con escala e iluminación | **naturaleza del modelo en su config actual** (`tiny`, 560 px, zero-shot) — no exclusivo de OVD (cualquier detector real-time sufre a esa escala) pero el zero-shot lo agrava | mitigable con costo: `base` (T2 ya midió SDR CR-02 0,920 vs 0,281), 800 px, tiling — todos pagan latencia (ADR-013). **Piso físico: un chaleco de ~20 px de noche no se detecta con nada de esta familia** |
| Estrategia E-IND: "no vi el chaleco" ⇒ "sin chaleco" | **plataforma — asimetría epistémica con su propio GT**: `derive_clip_gt` defiende "la incertidumbre NUNCA fabrica una violación" y el anotador marcó `unknown` masivamente en estos mismos sujetos (track 0 de v06: 10.528/11.087 frames), pero el motor no tiene estado unknown: para él la ausencia de evidencia ES evidencia de ausencia | **sí, y es la palanca principal**: gate de juzgabilidad en runtime (simulado: −61% FP) + candidatos no simulados (latch de cumplimiento: si el track mostró chaleco hace <N s, sostener compliance — mataría los FP por miss correlacionado; confianza mínima del sujeto). Ninguno elimina el piso de la capa 1 |
| Tracker: fragmentación 11–15× | **plataforma** | sí, barato (ByteTrack / edad mínima de track) — multiplicador, no raíz |
| Modo escena: captura por evidencia perpetua | **plataforma, pero semánticamente irreparable en escenas densas** — responde "¿hay alguien en violación?" que siempre es sí con 127 personas | el fix ES `subject` (G1) + las capas de arriba; no invertir en re-arme de escena |

**La lectura que queda para el informe:** el sobre de operación validado tiene una
frontera **medible en px-de-sujeto × iluminación** (≥~320 px diurno: asociación
96–100% y F1 0,93 con G1; por debajo o de noche: la lógica de ausencia se
invierte y fabrica violaciones). La respuesta operativa primaria no es algorítmica
sino **de despliegue**: cámara por zona de trabajo a distancia juzgable — que es
exactamente el régimen del rodaje. La mejora algorítmica honesta es sumar el estado
`unknown` al runtime (el principio que el GT ya defiende), y se puede presentar
con esta simulación como evidencia de dirección.
