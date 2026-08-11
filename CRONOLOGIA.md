# Cronología de jornadas — el día a día del set documental

- **Qué es esto:** el registro jornada por jornada que hasta el 2026-08-10 vivía
  comprimido en una sola línea en la cabecera de `00-indice.md` (llegó a ~9 KB en un
  solo bullet). Acá se conserva completo y legible; el índice mantiene solo la fecha de
  la última actualización y el estado vigente.
- **Cómo se lee:** cada sección es una jornada, la más nueva arriba. El texto se
  conserva tal como se escribió al cierre de cada jornada — **es registro, no
  síntesis**: puede contener afirmaciones que una jornada posterior corrigió (la
  corrección aparece en la jornada más nueva). Para el estado VIGENTE, entrar por
  `GUIA-CIERRE.md` (qué falta), `sintesis/resultados-y-conclusiones.md` (resultados) y
  `operacion/97` (plataforma).
- **Jornadas anteriores al 2026-08-04:** no estaban en el changelog del índice; su
  registro son los propios docs de `operacion/` — ver el **mapa por tramos** en
  `00-indice.md` §`operacion/`.

---

## 2026-08-10/11 — ADR-016 (distribución reabierta) + serie de relevamientos 14–19 + `nucleo/` partida por vigencia

**El disparador:** el usuario encontró que `nucleo/01` §10 citaba como "pendientes" cinco
ítems superados desde el 2026-07-29 — el relevamiento del control-plane era una foto del
07-06 con **siete de once secciones vencidas** (la peor trampa: §8 daba como vigente el
pattern set `v1`, deprecado por F-DR9). Auditado el set: `nucleo/11` (media-plane) estaba
igual, y tres decisiones ya escritas eran inencontrables (la regla de archivado de
`_archived/README.md`, la frontera de ADR-011, el "sube a Drive a mano" de
`datasets-videos/README.md`) — el síntoma que la serie nueva viene a curar.

**Tres frentes ejecutados:**

1. **ADR-016 — reapertura acotada de la distribución.** El usuario decidió implementar el
   módulo de distribución **antes de la defensa** para cerrar la arquitectura (dónde vive
   el ciclo de vida de la alerta: cooldown, re-notificación, supresión). Colisionaba con
   ADR-015 §2c/§6; ADR-016 deroga **puntualmente** §2b/§2c/§6 y ratifica §2a/§3/§4/§5
   (la lista L1–L8 se sigue citando desde ahí). E-06 sigue excluida; **no bloquea el
   informe** (si el módulo no llega, se declara como estaba). Propagado a 9 lugares
   (ADR-005/015, README y estado de decisiones, `nucleo/10`, `informe/99`,
   `GUIA-REDACTORES`).
2. **Serie `nucleo/14–19`** — relevamientos por servicio, **contra git y código** (suites
   corridas: control 312 · media 641 · datasets 418 · BFF 586), **cero cifras de
   resultado** (las cifras siguen en `results/`; capacidades en `operacion/97`). `14`
   mapa de la cadena · `15` setup · `16` datasets · `17` media (reemplaza al 11) · `18`
   control (reemplaza al 01) · `19` **cierre de la arquitectura: el ciclo de vida de la
   alerta** (consolida 06/ADR-005/ADR-011/spec 45/92b; deja anotado el desfase
   `confirmed_at_ms` que el implementador va a chocar).
3. **`nucleo/` partida por vigencia** (criterio del usuario: histórico = todo lo no
   actualizado a lo implementado): raíz = `10` + `14`–`19`; **`nucleo/historicos/`** =
   `01`–`09`, `11`, `12` (ninguno posterior al 07-13), con banner cada uno y `README.md`
   con punteros. `04`/`12` marcados **"no se toca"** (pre-registro de D1, valen por no
   actualizarse). **Hallazgo:** `09` (los argumentos A1–A5 de la defensa) quedó histórico
   por el criterio — no incorpora los números medidos después (A1 se midió en
   `operacion/94`); amerita sucesor. 25 rutas reescritas, enlaces verificados (73/73),
   verificadores 96 y 109 **verdes** (el 96 ajustado para buscar también en
   `historicos/`). De paso: 4 enlaces rotos preexistentes de la reorg de `informe/`
   corregidos.

**Relevamiento de consistencia de `informe/` (2026-08-11, tras ADR-016):** los siete docs
de `informe/ajustes/` se pusieron al día con el estatuto nuevo de la distribución — AJ-0.01,
el §5 del `03`, AJ-4.01/4.11 del `04` y AJ-6.04/6.05 del `06` dejaron de citar ADR-015 §2c
(derogada) y dicen **trabajo comprometido con estado a la entrega**; en el `06`, la
distribución **salió del trabajo futuro** (queda E-06). Se reparó además lo que la jornada
de ADR-016 dejó a medio propagar: el **encabezado del `92b`** (todavía decía "coherente con
ADR-015… no ejercida"), el rango de serie **`ADR-001…016`** en seis lugares (mapa AJ-0.02,
`99` §4.2 y §6, `98` §2 ×2, glosario 13), el "15 ADRs" del `98` §1 y del índice (fila del 99
y §decisiones), e insumos nuevos en el `04` (`nucleo/14`–`19`). Verificación: 0 links rotos
en `informe/` completo, IDs `AJ-` 7+16+12+12+12+5 sin duplicados, verificadores 96/109
verdes. **Kit refrescado**: 36 copias re-sincronizadas + 7 agregadas (`adr-016`,
`nucleo-14…19`) — nivel1 55 / nivel2 17 / nivel3 21.

**Crítica de extensión del informe (2026-08-11, pedido del usuario):** nuevo
`informe/ajustes/07-critica-extension-y-poda.md` — no existía nada que midiera longitud
(el 93 audita corrección, el 95 sacrificaba redlines contra tiempo). Medición por sección
(`wc -w` por encabezado sobre los extractos): **~126.800 palabras escritas** con
§17.4/17.5/17.6 aún vacías. Titular: **21.260 palabras (17%) cubren DOS VECES los dos
temas menos alineados** — MOT (§15.3 2.484 + §16.4 2.769, con E-10 excluyendo las
métricas) y streaming/arquitecturas/borde (§15.4 7.998 + §16.5.3–5 8.009, con la decisión
colapsada a RTSP+ZeroMQ y EN-3 excluida). Otros hallazgos: §16.7 = 4.429 de meta-texto ·
§17.1.6.2 = 5.054 de catálogo de datasets pre-`bench_v3` (se poda junto con R-24) ·
§16.5.2 duplica el framework de métricas de §17.1.7. **18 podas `PODA-nn`** (serie
verificada libre) con casilla de decisión, 5 criterios, **ahorro ~34.900 (~27%)**, orden
recomendado (los 8 🔴 = 65% del ahorro) y 6 guardrails (16.2/16.3/17.1.5/17.1.7 intactas;
lo pre-registrado no ejercido se comprime a decisión declarada, no se borra). Cableada en
mapa (§1/§2), índices, GUIA-REDACTORES y kit.

**Auditoría de material (mismo tramo):** clasificador de runs contra-verificado (4
pasadas hasta converger): 670 runs, 434 citados, **236 no citados = solo 0,26 GiB**, cero
huérfanos. Lo pesado está todo gitignoreado — lo que recibe quien clona son ~17.600
archivos versionados (354 MB). `scripts/` (5,7 G, raíz del workspace) confirmado huérfano
del intento inicial de descarga (0 de 16 IDs citados). El respaldo del material
irremplazable (`datasets-videos/`, 8,4 G) a Drive **lo maneja el usuario** (carpeta
privada, sin link público — de eso depende el "sin redistribución" del informe). Queda
del usuario: C1 (URLs de los 18 `clip.yaml` — no reconstruible desde disco) y la decisión
sobre la vista YOLO (6.338 archivos, sostiene el argumento de E-04). Spec del tramo:
`herramientas/2026-08-10-relevamientos-por-servicio-design.md`.

---

## 2026-08-10 — kit de redacción reparado para externos + reorganización del set

**Contexto que cambió el requisito:** el informe lo redactan los otros dos integrantes
del equipo, que **no participaron del tramo experimental**. El kit de redacción no
estaba listo para externos: los documentos que se autodeclaraban canónicos describían
el mundo **pre-estrato-B** (banco de 34 clips, 12 campañas, "lote sin GT", "FAR/hora no
es una métrica") con etiqueta de "verificado contra disco".

- **`informe/97` reparado** — banner de cabecera con tabla "dice / vigente" (banco
  34→47, 12→16 campañas, lote con GT, FAR/hora precisada, cobertura del verificador);
  §5.1 acotada al Bloque A; §3 corregida; **puerta de redacción LEVANTADA** (la
  redacción está habilitada y es el carril principal).
- **`informe/98` reparado** — custom instructions reescritas (banco 47 en dos bloques,
  prohibición de rankear con n=2, regla del FAR); manifiesto ampliado con `sintesis/`
  (faltaba entero) y `operacion/109/111/112/113`; aviso de que `informe-project-kit/`
  estaba viejo.
- **Glosario `13` purgado** — 5 filas muertas eliminadas + §4.1/4.2/4.3 nuevas: códigos
  `F-NN.N`/`D-NNN.N` (no estaban definidos en ninguna parte), IDs de campaña, estratos
  A/B, y las tres colisiones de símbolos (`R1–R4`/`R1–R6`/`R-01…R-26` · `D1` ·
  `A1`).
- **`GUIA-REDACTORES.md` creada** — el único documento del set cuyo lector previsto es
  un externo: proyecto en 5 minutos, orden de lectura en 5 pasos, qué NO abrir, cómo
  citar una cifra (12 ejemplos pareados), las 5 trampas, escala AF y dónde vive cada
  cosa.
- **Hallazgo 3 de `informe/99` §6 CERRADO — y la premisa era falsa:** los 11 catálogos
  de modelos **sí** declaran `license:` y `source:`; lo que faltaba era el registro —
  nueva sección "PESOS DE MODELO" en `license_registry.md` (GDINO/MM-GDINO Apache-2.0,
  YOLOE AGPL-3.0, verificados contra evidencia independiente).

**Segunda pasada de la jornada — reorganización del set para el equipo** (validación
previa: verificadores 96 y 109 corridos en verde):

- **`00-indice.md` reestructurado**: el changelog de ~9 KB en una sola línea se movió a
  este archivo (`CRONOLOGIA.md`, nuevo); se agregaron el **modelo de tres capas**
  (entrada/canónico/bitácora), el **mapa por tramos** de los 75 docs de `operacion/`,
  la sección de `sintesis/` que faltaba, la fila del **doc 108** (no estaba indexado),
  y se eliminó la fila duplicada del 102. Decisión de diseño: **el archivado es lógico
  (índice + banners), no físico** — mover/renumerar es prohibitivo (~2.800 referencias
  por número de doc, 7 scripts con rutas absolutas, y artefactos de `results/` que
  citan `docs/operacion/…` como procedencia).
- **`informe/99` puesto al día al mundo post-estrato-B**: banco 47 (T-78), filas nuevas
  T-82…T-84/FIG-F, freeze vigente `3f14f50a…` (189/189), alcance real de los dos
  verificadores en §2.2, L1/L4/L6 en su formulación vigente, bloque nuevo de mecanismos
  del tramo de video (F-103.2…D-113.2) y puerta de redacción levantada en §6.
- **`informe-project-kit/` REGENERADO** (76 archivos: 44+17+15) según `informe/98` §1,
  con `GUIA-REDACTORES.md` agregada al Nivel 1 del manifiesto; el paquete del
  2026-07-18 quedó descartado.
- **Higiene del repo `docs/`**: se eliminó `informe/desarrollo-docs/` — una
  re-exportación de los dos `.docx` (verificado: **mismo texto exacto**, 169.583 y
  870.920 caracteres, y el mismo conjunto de imágenes; solo cambiaba la numeración
  interna de los `media/`), sin una sola referencia en los 5 repos. Y se **empaquetó el
  repo por primera vez** (`git gc`: 3.272 objetos sueltos, `size-pack: 0`) ⇒ **`.git` de
  102 MB a 69 MB**, sin tocar la historia ni el árbol de trabajo (`fsck` limpio). **No
  se reescribió la historia** y es decisión deliberada: recuperaría solo 13,4 MB y
  cambiaría todos los hashes de commit, y hay **5 citas de hashes del repo `docs/`** en
  la propia documentación (`571652c` baseline, `924f972`, `a256250`).

**Tercera pasada — `informe/` partida en dos, y los ajustes ordenados por etapa.** Hasta
acá los ajustes al informe estaban dispersos: el `93` cubría **solo la Etapa 3** (26
redlines), los de Etapa 2 vivían en `nucleo/08` §2, los de Etapa 1 en
`sintesis/resultados-y-conclusiones.md` §7, y los de Etapa 5 en `informe/99` §1. **Nadie
tenía la lista completa, y nadie había mirado las etapas 4 y 5 como frente propio.**

- **La carpeta se partió en `entregable/` y `ajustes/`.** Los 17 archivos se movieron con
  `git mv`; **ningún número cambió** (se sigue citando "el doc 93", "informe/99"), y las
  ~30 referencias por ruta completa se corrigieron en `00-indice.md`, `GUIA-REDACTORES.md`,
  `adr-015`, `operacion/92`, el `97`, el `91` y `results/index.md`. No había ningún link
  markdown apuntando a esas rutas (verificado), así que no quedó nada roto.
- **Hallazgo que ordenó todo el diseño:** cada etapa tiene una **sección exacta** del
  informe, y **§17.4, §17.5 y §17.6 están literalmente vacías**
  (`[Agregado futuro correspondiente a la Etapa 4/5/6]` en el `96e`). Eso parte el trabajo
  en dos naturalezas distintas: etapas 1–3 son **corrección de texto existente**, etapas
  4–5 son **redacción desde cero** — y son el camino crítico.
- **Las etapas son seis, y se verificaron contra el Gantt.** Hubo un ida y vuelta: se
  planteó que eran cinco (con "conclusiones" como última), y **la verificación lo resolvió**
  — se extrajo `word/media/image5.jpg` del `.docx` y el **Gantt de la Figura 1 muestra seis
  tareas con sus fechas**, coincidiendo 1:1 con §14.2.1–14.2.6 (y con el §14.3, que dice
  textualmente *"las seis etapas descritas"*). El mapa quedó ordenado por las seis, con la
  tabla del Gantt como lista canónica. **Detalle que conviene recordar: el Gantt numera las
  tareas 0–5 y el §14.2 numera las etapas 1–6** — misma secuencia corrida en uno; en el set
  se usa siempre la del §14.2.
- **`AJ-0.06` nuevo:** **el informe está ordenado por sección y casi no menciona las
  etapas**, así que el lector no puede mapear el plan de trabajo (§14) con el desarrollo del
  producto (§17). Hay que meterle la tabla de correspondencia.
- **El Gantt aportó un ajuste propio (`AJ-0.03`, ERRATA):** sus fechas están vencidas —
  implementación MVP 20/03/26–29/05/26 y documentación/defensa 17/07/26–**21/08/26**,
  cuando la implementación siguió hasta agosto, el tramo experimental cerró el 08-09 y la
  defensa es ~fin de septiembre.
- **7 documentos nuevos**: el `00-mapa-de-ajustes.md` (maestro) y uno por etapa (`01`–`06`).
  Total relevado: **90 ajustes — 11 🔴 / 43 🟠 / 36 🟡-🟢**, con serie nueva `AJ-<etapa>.<nn>`
  (prefijo elegido por estar libre y no chocar con `A1–A5`, `AF-1…AF-11`, `L1–L8`, `E-01…`
  ni `T-68…T-84`). **`R-01…R-26` de Etapa 3 no se renumera**: se enruta.
- **Dos huecos de relevamiento que aparecieron al hacer el mapa**, y quedaron declarados
  como tales en vez de tapados: **`AJ-1.16`** — el **§16 Marco Teórico nunca se relevó**
  contra el estado actual del proyecto (todo el pase de Etapa 1 fue sobre el §15 y el
  Anexo A); y **`AJ-0.04`** — los **costos** (§17.2/§14.4) no se contrastaron nunca contra
  lo efectivamente gastado.
- **Categoría nueva de ajuste: 🚫 NO-TOCAR** — cinco cosas que *parecen* errores y
  corregirlas empeora el informe (la más traicionera: los nombres de métrica que aparecen
  vacíos en §17.1.7 y Tabla 33 **no** son una errata, son objetos de ecuación de Word que
  la extracción XML no captura).
- **Kit**: se sincronizaron las copias afectadas y se sumaron los 6 documentos nuevos al
  Nivel 1 (`informe/98` §1 actualizado con las rutas nuevas y con el aviso de que los
  nombres aplanados no cambian).

---

## 2026-08-09 — cierre del tramo de video: gen. 3, revisión ciega y sincronización

### Cierre de jornada: pase de sincronización de índices y procedencia (doc `operacion/113` §G)

Relevamiento completo de `results/` pedido por el usuario: los datos estaban sólidos,
la presentación no —la revisión ciega se había propagado al fondo de los docs pero no a
sus bordes—. Cerradas **6 contradicciones** (encabezado de `clip_bench` con banco de
38 → **47**; censo raíz 34 clips/12 campañas → **47 y 14**; las **tres** formulaciones
divergentes de FAR/hora unificadas en la de **L1**; `realtime/index.md` §7 que
contradecía a L1 y L6; cuerpo de la síntesis con cifras muertas; `GUIA-CIERRE.md` tres
jornadas atrás). **F-113.1, el hallazgo del pase y es de REPRODUCIBILIDAD:** los
`metrics.json` de I1/I2 traían las cifras post-revisión pero declaraban el **freeze
pre-corrección** (`299ccc19…`) ⇒ quien reprodujera obtenía 0,500 en vez de 0,333 —
causa: el agregador copia `campaign.yaml` adentro, así que **re-evaluar sin re-agregar
congela la procedencia**; corregido y regenerado **sin mover ninguna cifra**. Misma
familia: `provenance.json` de I1/I2 declaraba 4 corridas para 13 clips y NA1 no tenía
ninguna ⇒ regenerados con `datos/113-regenerar-provenance-estrato-b.py` (idempotente,
`--check`), **las 16 campañas con artefacto tienen hoy procedencia completa**.
`96-verificar-indices.py` pasó de 8 cifras a **19, cobertura 16/16, con guard que falla
si aparece una campaña sin verificar**. Los 4 artefactos secundarios quedaron
declarados (**solo 2 son supersedidos**; el control de B1 y la réplica base-560 están
VIGENTES). **El estrato B quedó integrado al CUERPO de la síntesis, §4.1 y §5.1.**
Verificadores 96/109/113 y suite datasets 418: verdes. Nada commiteado.

### Misma noche: REVISIÓN CIEGA DEL GT EJECUTADA

El resultado más fuerte del tramo de video: **5 de las 7 declaraciones de episodio del
lote eran ERRORES de anotación (~71%)**, todas sobre-declarando donde el estado no era
observable. Cayeron los 2 episodios de `v04_c02` —el ex "caso limpio"— y el de
`v01_c01`; estrato B vigente: **2 evaluables, `scene` F1 0,333 / `subject` 0,190,
Nivel A 0,031/0,018**, FAR sin cambio (3 y 190 FP en 0,1027 h). **Banco 47 = 32
positivos / 15 negativos / 37 episodios, manifest `3f14f50a…`.** Cadena completa:
correcciones firmadas → re-derivación → re-evaluación determinista (11/11) →
propagación con banners (111, 108) y notas (110, 112, índices de `results/`).
Decisiones firmadas D-113.1 (precisar L4, no L9) y D-113.2 (regla `unknown` del
scorer, declarada). CONSTANCIA citable en el doc 113 §B. **ENTRAR POR EL 113.**

### Mismo día

Gen. 3 corrida (doc 111), balance crítico (112), manual de cierre (113).

---

## 2026-08-07 (noche) — el CVAT llegando por goteo

Doc **109** = fuente única del material de video y de las campañas citables; doc
**110** = último clip integrado, `v03_c02`, banco **39 clips** — y la gen. 3 de las
campañas del estrato B **lista para correr, sin correr**, con la recomendación de
esperar los 9 clips que faltaban.

---

## 2026-08-06 — llegada del lote de internet + relevamiento integral de consistencia

**El día del CVAT del lote** (docs 102–107, con el 108 al cierre): GT del estrato B
(102, banco 34→37), campañas I1/I2 corridas (103, el hallazgo de densidad real),
ajustes probados solo con config (104), Nivel A sobre video con los 4 pilotos
recuperados (105), inventario y cómo continuar (106), matriz de knobs completa (107) —
el frente de clips quedó sin pendientes de plataforma esa misma noche.

**Y el relevamiento integral de consistencia:** se auditó todo el set — conclusiones
AF, redlines, kit de informe, alcance/ADRs, índices de `results/` (verificador
mecánico: todo verde) — y se corrigieron los desfases encontrados: **doc 10 con
ADR-015 propagado completo** (ítem 5/MQTT, cuerpos E-03/E-04/E-10/E-13, L2),
`estado-de-implementacion-adrs` (filas 001/002/005 + condicional ADR-005), glosario
doc 13 (jerarquía de verdad → 97 + `results/`, estatuto del GT, convenciones AF-x /
limitación-L vs hito-L / dos series de ADR), banner de derogación en `operacion/92`,
R-24/R-26 anotados en `informe/93`, y el índice. **Síntesis consolidada de resultados
y conclusiones: `sintesis/resultados-y-conclusiones.md`** — nuevo punto de entrada
para leer el estado del trabajo de una sola pasada.

---

## 2026-08-05 — cierre de resultados + relevamiento de datasets

Docs 92–98 cerraron el capítulo de resultados —entrar por el **98** (conclusiones
transversales) y por `results/index.md`—, el **99** relevó y ordenó los datasets de
imágenes con el registry al día y la limpieza ejecutada, y el **100** midió por
primera vez el costo de E-04/T1 (**≈1 h de GPU**, confirma el rango pre-registrado)
dejando **F-100.1 como el único bloqueo para ejercerlo**. Estado de plataforma
vigente = doc **97** (reemplaza al 56).

---

## 2026-08-04 — el tramo experimental sobre el banco del rodaje COMPLETO

**El eje de la tesis RESUELTO.** Jornada 83–90: Fase D Nivel A (gate no se dispara) →
réplica base-560 (F-84.1: la debilidad de E-DIR es estructural) → evaluador
`direct_evidence` (285 passed) → campaña D1 (**veto de precisión: E-IND confirmada
núcleo por medición**) → H1 E-HYB-or (predicción refutada; F-87.2: la unión no es
monótona en un motor temporal) → B1 bare_head (F-88.1: el caption tiene costo medido,
0,082 F1 por una palabra; F-88.3: etiqueta corta > frase negada ordena el eje) →
**G1 granularidad por sujeto = 0,930, el mejor resultado del banco** (+0,141 sobre T1
con las MISMAS detecciones; P7 0,400→1,000). Veredicto: E-IND 0,789 núcleo / E-DIR
0,160 descartada / E-HYB-or 0,296 no supera; las tres fallas explicadas POR MECANISMO.
FAR/hora declarado LIMITACIÓN, no métrica (D-90.1). Primera tanda commiteada y
pusheada (datasets `7ae79b2e`, control `5327080`, exp-setup `6f0391a`, media
`94660e6`, docs `924f972` local); segunda tanda (87–90) SIN COMMITEAR (✎ commiteada al
cierre del 08-05 — deuda git 0 en los 5 repos). **Punto de entrada: doc 90 (tablero de
decisiones) + `results/clip_bench/index.md` (tabla del informe)**. Suites:
control-plane 293 / datasets 283.
