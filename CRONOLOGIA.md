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
