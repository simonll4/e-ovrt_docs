# Lectura transversal de las Etapas 1–5 tras la ronda en Google Docs (2026-09-07)

> **Qué es.** Auditoría de alineación, coherencia y cobertura sobre las cinco versiones que el
> usuario bajó de Google Docs el 2026-09-06 (§15/16 v1.2 · §17.1 v1.16 · §17.3 v1.8 · §17.4 v1.8 ·
> §17.5 v1.5). Objetivo declarado: **cerrar cada sección por separado** antes de integrar el
> informe final. Método: diff palabra a palabra contra la versión anterior de cada una, censo
> mecánico (numeración, referencias cruzadas, terminología, fugas de andamiaje, trazado de cifras
> a `results/`), verificador mecánico del `.docx`, lectura completa de §17.4 y §17.5, y dos
> lecturas independientes de las cadenas §16 → §17.1 → §17.5 y §17.3 → §17.4 → §17.5, cuyos
> hallazgos se verificaron uno por uno contra los textos y el XML de los `.docx`
> (varios resultaron falsas alarmas del extractor; están declarados en el §7).
>
> **Cómo leerlo.** El §1 dice qué cambió en cada versión. El §2 da el veredicto por etapa. Los
> §3–§5 listan los hallazgos por severidad: **BLOQUEANTE** (impide cerrar la sección),
> **IMPORTANTE** (incoherencia entre secciones, promesa incumplida, hueco de cobertura),
> **MENOR** (estilo). El §8 es la lista de trabajo por documento, en el orden en que conviene
> aplicarla en Google Docs. Las referencias «L…» son líneas de los textos base re-extraídos hoy
> (`90f`, `90`, `90b`, `90c`, sin contar el banner de 11 líneas) o del texto extraído de la
> Etapa 1 (`e1`, extracción de trabajo de esta lectura); una línea = un párrafo del `.docx`.

---

## 1. Qué cambió en cada versión

| Sección | Versión previa → nueva | Texto | Comentarios | Figuras | Verificador mecánico |
|---|---|---|---|---|---|
| §15 + §16 | v1.1 (colega, 09-01) → **v1.2** | **+1 párrafo** (intro a las métricas MOT, 15.3.3, responde al comentario del colega); el resto **idéntico a la v1.1**: persisten los 6 typos y la oración rota señalados el 09-01 | 10 → **11** (4 del colega resueltos; 5 nuevos del usuario, 3 de ellos son el análisis D-E1-11 pegado como respuesta) | 0 | ❌ **falla**: «16. Marco teórico» perdió el estilo Título 1 |
| §17.1 | v1.15 (FINAL 09-03) → **v1.16** | **idéntico** (0 hunks) | 1 → **0** (resuelto) | 0 | ✅ |
| §17.3 | v1.7 (cerrada 09-04) → **v1.8** | **40 hunks, −189 palabras**: notas de las 4 figuras absorbidas en el párrafo previo; glosas en español de los 5 estados; identificadores en itálica; 7 viñetas → párrafos; 7 notas u oraciones de cierre eliminadas; 3 cambios de redacción (2 con problema, ver E3) | 4 → **0** (resueltos) | 4 (mismas imágenes) | ✅ |
| §17.4 | v1.7 con sugerencias → **v1.8** (aceptada y editada) | **17 hunks, −68 palabras**: se borraron las oraciones que llamaban a las Tablas 57 y 59 y dos notas; caption de la Figura 4.5 eliminado y la imagen quedó dentro de una oración; «la Etapa 4» → «la implementación»; ajustes menores | 7 → **6** (2 del usuario siguen; 4 nuevos del colega) | 1 (**imagen del 08-23, no la de `figuras/`**) | falla sólo por ser sección suelta (arranca en 17.4) |
| §17.5 | v1.4 con sugerencias → **v1.5** (aceptada y editada) | **12 hunks, −114 palabras**: **se eliminó el párrafo de las ocho limitaciones**; se borraron las oraciones que llamaban a las Tablas 62 y 63; se movió la nota de la Tabla 62 al párrafo (queda una oración duplicada); «juzgabilidad» → «de de juicio»; título 17.5.7 acortado | 0 | **0 (FIG-B, FIG-C y FIG-F sin pegar)** | falla sólo por ser sección suelta |

Los `.docx` nuevos están limpios (0 cambios controlados). Las versiones superadas se movieron a
`desarrollando/archivado/` con su motivo en el nombre; los textos base `90f`, `90`, `90b` y `90c`
se re-extrajeron hoy de las versiones nuevas (regla D-C) y el kit se regeneró (`--check` OK, 63 tests).

---

## 2. Veredicto por etapa

| Etapa | ¿Cierra tal como está? | Por qué |
|---|---|---|
| **1** · §15 + §16 v1.2 | **No** | Título de §16 sin estilo (desaparece del índice); oración rota que mezcla E-DIR con E-IND; párrafo y marcador AAIP que D-E1-11 mandó borrar y que prometen algo que §17.1 ya no contiene; los typos del 09-01 intactos; 11 comentarios abiertos. |
| **2** · §17.1 v1.16 | **Sí como texto**, con 4 ajustes de coherencia hacia adelante | El texto es el cerrado el 09-03. Pero lo que §17.5 reporta y §17.4 hizo contradice tres reglas escritas en §17.1 (fuente única ajuste/banco, banco fuera de la calibración, métricas obligatorias con estado) y el banco temporal que sostiene el resultado principal no está fijado como decisión. Son decisiones de diseño: pueden ir hacia atrás. |
| **3** · §17.3 v1.8 | **Sí**, con retoques | Dos cambios de redacción del usuario alteraron el sentido (E3-1, E3-2); tres notas eliminadas eran guardarraíles que conviene evaluar; dos promesas hacia §17.4 quedaron sin cumplir ítem por ítem. Nada bloqueante. |
| **4** · §17.4 v1.8 | **No** | Figura 4.5 rota (dentro de una oración, sin caption, imagen vieja); Tablas 57 y 59 sin llamada; «cuarto componente funcional» contradice a §17.3; el perfil operativo no se nombra; causa del tercer tramo de ajuste fino distinta a la de las actas; compose en presente. |
| **5** · §17.5 v1.5 | **No** | Sin limitaciones declaradas; sin figuras; «23 episodios confirmados» no cierra con la Tabla 63; Tablas 62 y 63 sin llamada; términos y nombres de métricas distintos a los de §17.1; métricas obligatorias sin estado. **Todas las cifras rastrean a los índices** (169 de 169): el cierre es de completar y explicar, no de re-medir. |

---

## 3. Hallazgos BLOQUEANTES

### Etapa 1 — §15/§16 v1.2

- **E1-B1 · Título «16. Marco teórico» sin estilo de encabezado.** En la v1.1 era `Heading1`; en la v1.2 es un párrafo normal en negrita (`pStyle` ausente). Desaparece del índice automático y rompe la numeración de campos de Word. Es exactamente el defecto para el que existe `verificar_entregable.py` (caso del 08-27). **Arreglo:** en Google Docs, aplicar «Título 1» a ese párrafo.
- **E1-B2 · Oración rota en §16.3.4 que invierte las dos formulaciones** (`e1` L481): «En primer lugar, solicitar directamente al modelo que localice la infracción completa, o solicitar evidencia positiva.Segundo, derivar la ausencia…». El «o solicitar evidencia positiva» pertenece a la segunda formulación; tal como está, E-DIR absorbe E-IND y contradice la oración siguiente. Señalado el 09-01; sigue igual. **Arreglo:** «Primera, pedir al modelo que localice la infracción completa. Segunda, pedir evidencia positiva y derivar la ausencia mediante razonamiento sobre las detecciones.»
- **E1-B3 · AAIP: párrafo «decisión pendiente» + marcador `[[PENDIENTE…]]` en §16.6.1** (`e1` L628–630), que promete «documentar el recaudo adoptado en §17.1 y §17.4». D-E1-11 (firmada el 09-01) decidió **borrar** ese párrafo y su espejo; el espejo de §17.1 ya se borró (la v1.16 no menciona la inscripción), así que hoy §16 promete algo que §17.1 no contiene. El colega también lo marcó («yo lo sacaría»). **Arreglo:** borrar el párrafo y el marcador; conservar la Disposición 10/2015 en el párrafo anterior (es marco, no especificación).

### Etapa 4 — §17.4 v1.8

- **E4-B1 · Figura 4.5 rota** (`90b` L15): la imagen quedó **dentro de la última oración** de §17.4.1 («El repositorio por ejecución experimental conserva los ⟦imagen⟧ artefactos persistentes de cada corrida»), el caption «**Figura 4.5**» y su título en itálica se borraron, y la imagen sigue siendo la del 08-23 (sha `1474…`, la que deja a la distribución fuera del orden), **no** `informe/figuras/fig-a-vista-de-procesos.png` (pendiente desde el 09-04). Además hay dos llamadas («La Figura 4.5 muestra» en L7 y «La figura 4.5 representa» en L15, una con minúscula). **Arreglo:** sacar la imagen de la oración, restituir «**Figura 4.5**» + «*Vista de procesos y patrones de acople de la plataforma experimental*» + imagen nueva, dejar una sola llamada con mayúscula.

### Etapa 5 — §17.5 v1.5

- **E5-B1 · Las ocho limitaciones desaparecieron.** El párrafo «Ocho limitaciones acotan la lectura de todo lo anterior…» (135 palabras, final de 17.5.7 en la v1.4) se eliminó. Hoy §17.5 no declara ninguna limitación, pese a que AJ-5.05 y la decisión D-H del 09-04 exigían traerlas y a que §17.1.10 las anticipa (cinco supuestos, cinco riesgos). Con él se fue la única mención a la doble anotación/acuerdo entre anotadores. **Arreglo (decisión del usuario):** restaurarlo (el texto está en `archivado/…17.5…v1.4 (sugerencias…)`) o registrar un handoff explícito a §18 con la lista L1–L8; sin una de las dos, la Etapa 5 no cierra.
- **E5-B2 · Cero figuras.** FIG-B (calidad vs densidad), FIG-C (alerta confirmada) y FIG-F (frontera de juzgabilidad) siguen sin pegar; §17.5 no tiene ninguna `⟦FIGURA⟧`. Existen en `informe/figuras/`.
- **E5-B3 · «medida sobre 23 episodios confirmados» no cierra** (`90c` L76): la línea de base de la Tabla 63 declara t_alert 5.327 ms con **n = 28** episodios confirmados; CR-02 confirmó sus 7, así que CR-01 son 21, no 23. El único «23» de los índices es otra cosa («23 clips cuyo GT es solo CR-01»). Los 4.314 y 8.572 ms sí rastrean a la campaña de línea de base. **Arreglo:** verificar en el índice del banco temporal y corregir a 21 (y nombrar la combinación en esa oración).

---

## 4. Hallazgos IMPORTANTES

### Coherencia entre etapas (decisiones del usuario)

- **X-1 · Regla de fuente única ajuste/banco (§17.1.6.3) vs. práctica (§17.4.7).** `90f` L285: «Una fuente destinada al ajuste no integra el banco de evaluación de la comparación principal, aun cuando sus particiones nominales sean disjuntas». El ajuste fino entrenó con `construction_site_safety` (2.203) y el **núcleo curado de 147 imágenes del banco deriva de esa misma fuente** (registro `bench_v3.md`); §17.4.7 L201 dice que se excluyó «la fuente que el banco de evaluación comparte» (sólo `chv`, que está al 100 % en el banco). Es una contradicción protocolo ↔ práctica que un jurado puede leer. **Opciones:** (a) precisar la regla en §17.1.6.3 a lo que se aplicó (exclusión íntegra de fuentes que están enteras en el banco + particiones disjuntas + deduplicación perceptual), o (b) declararlo como desviación y limitación en §17.4.7/§17.5.6 (la retención in-domain del ajuste se midió en parte sobre material de la misma fuente).
- **X-2 · G2A: §16 lo define con captura y transporte adentro; §17.1 y §17.5 lo miden desde el dequeue.** `e1` L551: «t_G2A = t_capture + t_transport + t_preprocess + t_inference (1)»; `90f` Tabla D.1: «Intervalo entre el dequeue de la unidad visual y la disponibilidad del resultado de inferencia»; `90c` L107: «El tramo desde el retiro de la unidad comienza en el dequeue, no en la captura de la escena». La Tabla 11 de §16 ya admite «captura, lectura o dequeue … en el punto definido por la instrumentación». **Arreglo:** una oración en §16.5.2 que fije el origen instrumentado de este trabajo en el dequeue y nombre a los dos primeros términos como el tramo de captura que se reporta aparte (202–217 ms).
- **X-3 · «Cuarto componente funcional» (`90b` L11) contradice a §17.3.7** (`90` L355: «No constituye un tercer plano ni un cuarto rol funcional, sino un módulo desacoplado»). **Arreglo:** en §17.4.1, «es un módulo funcional desacoplado de los dos planos».
- **X-4 · El perfil operativo no se nombra en §17.4.4** (`90b` L120: «El perfil fijado por criterio pre-registrado para las corridas en vivo declara umbral de caja de 0,30 y de texto de 0,25…»); `gdino-tiny-560` aparece por primera vez en la Tabla 61 de §17.5, y §17.5 no repite su par (560 px / 0,30 / 0,25 / NMS 0,50). **Arreglo:** nombrarlo en §17.4.4 con su resolución; en §17.5.2 remitir a 17.4.4.
- **X-5 · Causa del tercer tramo de ajuste fino.** `90b` L199: «El tercer tramo se cerró con causa técnica, porque el único corpus disponible de ese volumen comparte fuentes con el banco de evaluación». Las actas registran otra causa (la diferencia no era interpretable sin una línea base MM-Grounding DINO sana; la justificación vigente es «linaje + escalera») y la Tabla 65 dice «cerrado con causa técnica antes de producir una comparación interpretable». **Arreglo:** una sola causa, la misma en §17.4.7 y en la Tabla 65.
- **X-6 · Métricas que §17.1 declara obligatorias y §17.5 no reporta ni declara con estado**: AP@[0,50:0,95], TTFD, P99, uso de VRAM/GPU/RAM (Tabla D.1 «obligatorio»), confianza media de los TP, kappa/doble anotación al 20 %, MOT17 y OVT-B como benchmarks, y tres de los cuatro ejes del protocolo de prompts (sintaxis, especificidad, template). `90f` L338: «Cada métrica debe acompañarse de un estado explícito». **Arreglo:** un párrafo o tabla en §17.5.7 «métricas aplicables no computadas» con estado y causa (varios ya se resolvieron en diseño: remitir a §17.3.4).
- **X-7 · Banco fuera de la calibración (Tabla 26, `90f` L301) vs. §17.5.3** («La calibración se realizó sobre una mitad del material y las métricas sobre la otra»). **Arreglo:** una oración que explique la mitad predeclarada y disjunta, en §17.1.6.3 o en §17.5.3.
- **X-8 · El banco temporal propio no está fijado como decisión en §17.1.6** (sólo «material controlado del EBE», `90f` L281), y es el material del resultado principal. **Arreglo:** una oración de decisión, sin cifras.
- **X-9 · §17.5 no usa DBE/EBE** (0 ocurrencias) mientras §17.1 organiza todo por escenario. **Arreglo:** en 17.5.1, «17.5.2–17.5.4 corresponden al camino diferido; 17.5.5, al camino en vivo».
- **X-10 · Nombres de métricas distintos entre §17.1 y §17.5**: `t_alert-system` / «latencia de alerta»; `FAR/hora` / «falsas alarmas por hora»; `t_G2A` (§17.5 nunca escribe G2A); `ΔFP_tracking` / «asimetría de falsos positivos»; «SDR» nunca se expande; AP@0,5 / mAP50 / AP50. **Arreglo:** una frase de equivalencias en 17.5.1.
- **X-11 · Dos materiales con casi el mismo nombre**: «video de obra real» = 17 clips de la campaña de estado por persona (17.5.3) y «obra real no guionada» = 13 clips del estrato B del banco temporal (17.5.4). **Arreglo:** nombrarlos distinto y decir que son materiales distintos.
- **X-12 · Promesas de §17.3 hacia §17.4 sin cumplir ítem por ítem**: nota de la Tabla 41 («Su materialización y verificación se documentan en la sección 17.4»: §17.4 sólo cita DA-13) y Tabla 52 («El estado ejecutado de cada ítem corresponde a la sección 17.4»). **Arreglo:** suavizar las notas («en conjunto») o agregar en §17.4.7 el mapeo decisión → dónde se materializa.
- **X-13 · Capacidad «Gestión de evidencia visual controlada»** (Tabla 39, complementario previsto; DA-09) **sin destino en §17.4.** **Arreglo:** una línea de estado en §17.4.7.
- **X-14 · MM-Grounding DINO**: §17.4.4 remite a §17.5 por su resultado; §17.5.6 sólo dice «se evaluó y se archivó». **Arreglo:** una cifra y la causa (sin atribuirla a cajas degeneradas: la memoria del 09-01 lo prohíbe).

### Etapa 1

- **E1-I1 · Nota de la Tabla 7 rota** (`e1` L282): «…problemas abiertos se abordan en las siguientes etapas» (falta «que»).
- **E1-I2 · 11 comentarios abiertos**, todos decisiones del usuario. Del colega (6): «Revisar anexo» (Tabla A.1), «validar, me suena a que es nueva» (Yuksekgonul: **sí es alta del pase 3, no sacar**), «Esto me parece muy de más» (AAIP: coincide con E1-B3), «pasar a formula» (ecuación 1), «varias cosas volaron de acá» (§16.6), «revisar» (Tabla A.2). Del usuario (5): «validar a qué referencia» (Luxonis s. f.-b), «¿está bien nombrar CR-01/CR-02 acá?» (§16.2: sí, si remite a 17.1.5), y los tres del análisis D-E1-11.

### Etapa 3

- **E3-1 · Cambio de sentido** (`90` L126): «artefactos **inatribuibles**» → «artefactos **sin atributos**». Lo que se quería decir es que no puedan atribuirse a una configuración declarada. **Arreglo:** «artefactos que no puedan atribuirse a una configuración».
- **E3-2 · Gramática rota** (`90` L172): «La frontera **que** esa elección fija es explícita» → «La frontera **de** esa elección fija es explícita». **Arreglo:** volver a «que».
- **E3-3 · Tres notas eliminadas que eran guardarraíles**: «EBE es un escenario experimental y no una topología fija…» (ex nota de la tabla de topologías), «Las métricas se atribuyen al rol y al despliegue efectivamente declarados… No se extrapolan entre CPN, EN y TN», «El núcleo no requiere canales externos, métricas MOT ni condiciones de Nivel 2 o 3…». **Decisión:** si vuelven, como oración en el párrafo previo (el estilo que el usuario adoptó para las figuras).

### Etapa 4

- **E4-I1 · Tablas 57 y 59 sin llamada en la prosa** (se borraron «La Tabla 57 reúne sus operaciones de gobierno» y «La Tabla 59 reúne esa evidencia…»). Toda tabla debe nombrarse en el texto.
- **E4-I2 · Tabla 56**: fila «RunConfig» → §17.3 llama a ese contrato «Manifiesto de experimento»; fila «Alerta distribuida» tiene las columnas invertidas (el contrato del diseño es `NotificationEnvelope`/`DeliveryRecord`).
- **E4-I3 · Compose en presente** (`90b` L118): «el despliegue integral instancia un servicio por perfil del catálogo». El compose de 13 servicios está definido y validado, pero **nunca se construyó ni se probó** (acta 128 §4). **Arreglo:** «define un servicio por perfil».
- **E4-I4 · «2.203 pruebas» sin fecha** (R-12 del relevamiento 130): la cifra es real (05-08, cinco suites), pero hay que fecharla («agosto de 2026») o re-medirla.
- **E4-I5 · Cobertura**: las fuentes en vivo (cámara OAK-D / RTSP) y el rol de borde no se nombran en §17.4 (sólo «hardware real de captura»); «QoS 1» no aparece (dice «confirmación de calidad de servicio»).
- **E4-I6 · 6 comentarios abiertos**: del usuario «agregar los DTO fue algo que nos marcó Mariano» (Tabla 56, párrafo de los cinco contratos) y «agregar hs de anotación» (**el dato no existe en el repositorio**; sólo el usuario puede aportarlo o cerrar el comentario); del colega «ver» (sobre el `[[PENDIENTE]]` de C1: legítimo hasta la versión final), «no sé bien qué formato va acá» (sobre `cr01_cr02_v2`: escribirlo como «el conjunto de patrones *cr01_cr02_v2*», en itálica como los demás identificadores), «esto no sé si lo hizo el colega» y «no sé a qué hace referencia esto o si ya lo hizo el claude» (sobre los cinco contratos y sobre la preanotación: ambos párrafos describen trabajo hecho y verificado; responder y resolver).

### Etapa 5

- **E5-I1 · Tablas 62 y 63 sin llamada en la prosa** (se borraron «La Tabla 62 reúne los resultados» y «La Tabla 63 reúne las combinaciones ejecutadas…»).
- **E5-I2 · «La misma frontera de de juicio dominó el resultado»** (Tabla 62): typo, y el término cambió: «juzgabilidad» ya no aparece en ningún documento del informe, mientras FIG-F se llama «frontera de juzgabilidad» y L55 sigue diciendo «no juzgables». **Arreglo:** «frontera de juzgabilidad» en la celda.
- **E5-I3 · Oración duplicada en 17.5.3** (L39): «La calibración se realizó sobre una mitad del material y las métricas sobre la otra…» y, tres oraciones después, «La medición sobre imágenes utilizó calibración en una mitad y evaluación en la otra» (efecto de mover la nota al párrafo). Dejar una.
- **E5-I4 · fps mezclados** (L88 vs Tabla 64): «el camino en vivo entregó entre 1,16 y 4,42 fps en cuatro densidades» vs «techo ≈ 4,29 / peor caso ≈ 1,15». Verificado: el vivo dio 1,16–4,42 fps; las cuatro densidades de remuestreo fueron 30 / 4,29 / 2,00 / 1,15. Separar las dos cosas.
- **E5-I5 · Tabla 61 sin mAP50 por los tres estratos** (sólo agregado y núcleo; `chv` y `shel5k` como rangos en prosa); regla del proyecto: «por estrato y agregado, nunca sólo el agregado». Y «n+ = 5.313» sin decir que es la referencia del 23-jul (la vigente tiene 5.308).
- **E5-I6 · Términos usados sin introducción**: granularidad de escena / por sujeto (definida en §17.3.6: remitir), «censurado con causa», «detector de referencia», «remuestreo pareado», «revisión ciega», «perfil operativo», «banco generalista».

---

## 5. MENORES (estilo y formato)

- **Convención de «Nota.» mezclada** en los cinco documentos (`*Nota.*`, `**Nota.**`, `***Nota.***`; en §17.5 tres de cuatro quedaron como «***Nota****.*» tras la edición). Elegir una para la integración.
- §17.4: «suscri**to**» (1) y «suscri**pto**» (5) en el mismo párrafo; «guión» y «guion» en oraciones contiguas (L149).
- §17.3: en las Figuras 4.1 y 4.2 la imagen quedó en el mismo párrafo que el título en itálica; en 4.3 y 4.4 tiene párrafo propio. Unificar. El documento arranca en 17.3.1 sin el título «17.3.» (verificar en el maestro).
- §17.5: «La asimetría no tuvo su dependencia de una única fuente» (antes «no dependió de»); «Sin ninguna corrida de entrenamiento alcanzó AP50 de 0,662» (sujeto elidido); «Video de obra real - CR-01» con guion frente a «Imágenes, CR-01» con coma; «dos órdenes de magnitud por debajo» (3 h vs 0,1027 h ≈ 29×, un orden y medio); «37 episodios» (explicitar 35 + 2); «las seis combinaciones» (son las filas de la Tabla 63).
- §15/16: «puede puede» (L119), «servicio.QoS 1» (L326), «midiendocuánto» (L606), «siendo que» (L453, L590), doble espacio (L469); intro de 15.2.1 repite sus subsecciones; «52,5 → 26,1» tres veces; P-E1 salta 05 y 07; citas «Zhou et al., 2022b» (§15) vs «Zhou et al., 2022» (§17.1), «A. Wang et al., 2025» vs «Wang et al., 2025».
- §17.1: «temporales, Por último, la alerta» (L31); Tablas 16, 17, 24, 26 y 27 sin llamada en prosa (preexistente a la v1.15).
- §17.4: el JSON del evento y el árbol de `runs/` salen aplanados en la extracción: verificar en el `.docx` que sigan en fuente monoespaciada con saltos de línea.

---

## 6. Lo que la ronda dejó bien (verificado)

- **Orden de arranque** control → distribución → medios, con la garantía en el publicador (§17.4.3 L98). Correcto.
- **Umbrales de §17.4.4 = configuración real** del conjunto de patrones `cr01_cr02_v2` (0,35 / 0,25 / 400 px²; 4.000 / 2.000 ms; 7.000 / 3.000 ms; márgenes 12 % / 8 %; franjas 0–45 % y 25–85 %). El **ejemplo JSON del evento** coincide campo por campo con `media.detection.v1` tal como se persiste.
- **Cifras**: 169 de 169 tokens numéricos de §17.5 y 38 de 38 de §17.4 rastrean a los índices de `results/`, las actas o las configuraciones. El banco temporal está bien descompuesto (47 = 34 + 13 = 32 positivos / 15 negativos / 37 episodios). Los 17 clips de estado por persona en video son la campaña NA1. «2.946 imágenes > rango 500–2.000» está justificado en §17.4.7 (H2-02 aterrizado). El ledger (E4-31) y el costo del vocabulario (AJ-5.14) están.
- **Autocontención**: sin fugas de identificadores internos en los cinco documentos (`P-E1-0x` y `DA-xx` son identificadores del informe). Dos marcadores `[[PENDIENTE]]`: el de C1 en §17.4.6 (legítimo hasta la versión final) y el de AAIP en §16.6.1 (a borrar, E1-B3).
- **No-anacronismo**: ninguna cifra medida por el proyecto en §15, §16 ni §17.1.
- **Referencias cruzadas**: todas las secciones citadas existen con la numeración vigente (17.1.4.1, 17.1.7.3, 17.1.10, 17.4.4, 17.4.6, 17.4.8, 17.5.2, 17.5.6, 17.5.7). Numeración de tablas sin choques: 2–11 · 16–35 · 39–52 · 56–60 · 61–65 (12–15, 18–19, 31–32, 36–38 y 53–55 viven fuera de este lote).
- Buenas ediciones del usuario en §17.3: glosas en español de los cinco estados, identificadores en itálica, notas de figura absorbidas en el párrafo, «debe preservar» → «preserva» (voz D-P3-9). En §17.4: «la Etapa 4» → «la implementación».

---

## 7. Falsas alarmas descartadas (y lo que se corrigió en las herramientas)

Cuatro hallazgos que parecían del documento eran del **extractor** `herramientas/extraer_informe.py`, que no atravesaba los controles de contenido `w:sdt` que Google Docs exporta en algunas celdas, filas y tablas enteras. **Corregido hoy** (dos parches, 63 tests en verde):

1. **Tabla 64, fila «CR-02 en vivo», celda vacía** — el `.docx` v1.5 dice «3 alertas: ≥ 7,1 s». También era una falsa alarma el 🔴 del tablero del 09-04 («la exportación del 08-27 perdió la celda»): la celda estuvo siempre; el pase 4 la «reparó» insertando un duplicado, que la aceptación en Google Docs resolvió en un solo valor.
2. **Tablas 28, 29 y 30 de §17.1 «sin cuerpo»** — están completas en el `.docx` (16, 20 y 8 filas); ahora `90f` las trae (22 tablas, antes 19).
3. **Tabla 57 de §17.4 «filas del bus atribuidas a la distribución»** — el `.docx` tiene «Medios → control (:5557)» y «Control → distribución (:5558)» en su propia columna.
4. **Tabla 11 de §16, celda `t_capture` vacía** — está completa.

Además, mi hoja de hechos decía «15 clips de internet»; el número correcto es **13** (15 son los negativos del banco). El informe estaba bien. Y «2.203 pruebas» es un conteo real (05-08), no un cruce con las 2.203 imágenes de ajuste.

---

## 8. Lista de trabajo por documento (para aplicar en Google Docs)

**§17.5 (Etapa 5)** — 1) decidir E5-B1 (restaurar las ocho limitaciones o handoff a §18); 2) pegar FIG-B, FIG-C, FIG-F con caption; 3) corregir «23» → «21» tras verificar y nombrar la combinación (E5-B3); 4) restituir las llamadas «La Tabla 62…» y «La Tabla 63…»; 5) «frontera de juzgabilidad» en la Tabla 62; 6) borrar la oración duplicada de 17.5.3; 7) separar fps del vivo y densidades de remuestreo (E5-I4); 8) nombrar distinto los dos «obra real»; 9) en 17.5.1: mapeo diferido/en vivo + equivalencias de nombres de métricas; 10) en 17.5.7: métricas aplicables no computadas con estado; 11) Tabla 61: columnas por estrato y fecha del GT; 12) menores del §5.

**§17.4 (Etapa 4)** — 1) rehacer la Figura 4.5 (sacarla de la oración, caption + título, imagen de `figuras/`, una sola llamada) (E4-B1); 2) restituir las llamadas a las Tablas 57 y 59; 3) «módulo funcional desacoplado» en vez de «cuarto componente» (X-3); 4) nombrar `gdino-tiny-560` con 560 px en 17.4.4 (X-4); 5) una sola causa para el tercer tramo (X-5); 6) Tabla 56: «Manifiesto de experimento» y columnas de «Alerta distribuida»; 7) «define un servicio por perfil» (E4-I3); 8) fechar «2.203 pruebas»; 9) precisar «la fuente que el banco comparte» según lo que se decida en X-1; 10) responder/resolver los 6 comentarios; 11) suscripto/guion/Nota.

**§15/16 (Etapa 1)** — 1) Título 1 a «16. Marco teórico» (E1-B1); 2) reescribir la oración de §16.3.4 (E1-B2); 3) borrar párrafo y marcador AAIP (E1-B3); 4) oración en §16.5.2 sobre el origen instrumentado de G2A (X-2); 5) nota de la Tabla 7; 6) los seis typos del 09-01; 7) decidir los 11 comentarios.

**§17.1 (Etapa 2)** — sólo decisiones que van hacia atrás: X-1 (regla de fuente única), X-7 (mitad de calibración), X-8 (banco temporal como decisión) y, si se prefiere fijarlos ahí, los umbrales pre-registrados (veto de precisión 0,5; tope de retención 10 %). Sin esas decisiones, el texto queda como está.

**§17.3 (Etapa 3)** — E3-1, E3-2, decidir E3-3, suavizar las notas de las Tablas 41 y 52 (X-12), estado de la evidencia visual controlada en §17.4.7 (X-13), estructura de figuras 4.1/4.2.

**Después de cada ronda:** bajar el `.docx`, correr `verificar_entregable.py`, re-extraer el texto base (regla D-C) y regenerar el kit. Esta lectura se repite sobre las versiones corregidas antes de declarar cerrada cada sección.
