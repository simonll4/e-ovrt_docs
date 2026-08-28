# El informe tal como está hoy

> **Esta carpeta es el entregable, no una fuente.** Es el TFG en sí (`.docx`) más su texto
> extraído para poder leerlo, buscarlo y citarlo desde el resto del set documental.
> **Ningún ajuste se aplica desde acá** — para eso está
> [`../ajustes/00-mapa-de-ajustes.md`](../ajustes/00-mapa-de-ajustes.md).
>
> ⚠️ **El texto extraído es una foto, no un espejo.** Se extrajo del `.docx` en su
> momento y **no se regenera automáticamente**: si alguien edita el Word, estos `.md`
> quedan viejos. Sirven para leer y ubicar secciones, no para verificar el estado actual
> del documento.

---

## Los dos entregables

| Archivo | Qué es | Fecha |
|---|---|---|
| `E-OVRT-VDP_v1.1_05062026-sin-indice.docx` | **El informe completo, v1.1** | 05/06/2026 |
| `E-OVRT-VDP_Etapa_3_Diseno_Arquitectonico.docx` | El capítulo de **Etapa 3** (Diseño arquitectónico) | — |

> ✎ **2026-08-22 — regla D-C aplicada sobre las dos secciones en desarrollo.** Se re-extrajeron
> ambos textos base desde los `.docx` vigentes, porque el kit estaba entregando material viejo:
> - `90-etapa3-texto-extraido.md` — **regenerado** desde §17.3 **v1.1**. Lo que había era la
>   extracción v0.1: 24.389 palabras contra las **20.622** actuales, y decía "contratos
>   preliminares" donde el informe hoy dice "contratos versionados".
> - `90b-etapa4-texto-extraido.md` — **nuevo**, desde §17.4 **v1.2** (**5.477** palabras). Antes
>   la etapa 4 no tenía texto base extraído y el kit entregaba `borradores/17-4.md`, que es el
>   borrador previo al pegado y anterior al pase 2.

> ✎ **2026-08-19 — pase de cierre de §17.3/§17.4 en curso.** Las versiones de trabajo
> VIGENTES de ambas secciones son los `.docx` de [`desarrollando/`](desarrollando/) —hoy
> **§17.3 v1.1** y **§17.4 v1.2**, con los comentarios del autor—. El standalone
> `E-OVRT-VDP_Etapa_3_Diseno_Arquitectonico.docx` (16-08) queda como versión PREVIA de
> §17.3. Al cerrar cada sección en el maestro: re-extraer su `.md` y fechar acá (regla D-C).
>
> ✅ **✎ 2026-08-23 — ENTREGA: los tres `.docx` FINALES están en `desarrollando/`, listos
> para integrar al maestro** (desarrollados por ChatGPT bajo las
> `instrucciones-correccion-gpt-2026-08-23.md` y verificados mecánicamente sección por
> sección; las versiones intermedias quedaron en `archivado/`):
> - **§17.3 v1.4** — pases 2 y 3 aplicados completos; 17 tablas renumeradas **39–55**;
>   subsecciones renumeradas (la ex 7.5 es 7.4; las ex 11.2/11.3/11.4 son 11.1/11.2/11.3).
> - **§17.4 v1.5** — pases 2 y 3 aplicados; 6 tablas renumeradas **56–61**; identificadores
>   versionados solo en la tabla de correspondencia (única excepción glosada: la referencia
>   temporal en §17.4.8); conserva el `[[PENDIENTE]]` de URLs del lote (C1).
> - **§17.5 v1.3** — redactada bajo D-P3-6 (8 bloques, por pregunta de medición); tablas
>   **62–67**; 185 cifras verificadas contra la hoja de datos, cero inventadas; **cero
>   `[[CIFRA]]`**: los 4 denominadores restantes se resolvieron el 2026-08-23 contra
>   artefactos primarios — G2A en vivo n = 47/93/55 y captura n = 47–295 por corrida
>   (tabla de corridas del rodaje en el índice de tiempo real), supervivientes por densidad
>   n = 21/20/16 (computados de las campañas de densidad; reproducen exactos los
>   +1.251/+685/+1.175 ms publicados) y preselección 206 de 236 unidades vistas (rama sin
>   filtro 277; tabla A/B de `oak-d-integration.md` del plano de medios). Solo quedan los
>   `[[FIGURA]]` y el `[[PENDIENTE]]` de URLs, que resuelve el usuario.
>
> ✎ **Decisión del usuario (2026-08-23): cada sección se cierra en SU PROPIO documento; la
> integración al maestro se resuelve después.** Consecuencias ya aplicadas: los tres textos
> base del kit se re-extrajeron de los documentos de trabajo (**`90`** ← §17.3 v1.4 ·
> **`90b`** ← §17.4 v1.5 · **`90c`** ← §17.5 v1.3, nuevo), y las notas del generador
> pasaron de "pases 2 y 3 PENDIENTES de aplicar" a **"YA APLICADOS Y VERIFICADOS"** — los
> pases entran al kit como criterio de lectura, no como lista de tareas. Re-aplicarlos sobre
> texto ya corregido es la falla que costó la pasada del 08-23.
>
> **El maestro sigue con §17.3/§17.4 en su versión previa y §17.5 vacía.** Cuando cada
> sección cierre y se integre, re-extraer su `.md` y fechar acá (regla D-C).
>
> ✎ **2026-08-27 — la Etapa 1 entra al mismo régimen: §15 pasa a tener documento de trabajo
> propio.** Se incorporó `desarrollando/Etapa 1.docx` (§15 completo, 22.169 palabras, con
> **12 de los 16 `AJ-1.xx` ya aplicados**) y se re-extrajo por regla D-C a
> **`90d-etapa1-texto-extraido.md`** — que **supera al `96c`** como texto base de §15. El
> `96c` queda como foto histórica del informe v1.1. **§16 sigue en `96d` y el Anexo A en
> `96e` §19.1: ninguno recibió pase todavía** (`AJ-1.16` abierto). Se escribió el pase de
> alineación [`desarrollando/archivado/correcciones-etapa-1.md`](desarrollando/archivado/correcciones-etapa-1.md)
> — comentarios **E1-01…E1-12** y decisiones **D-E1-1…D-E1-6**, **NO aplicado: es el trabajo
> a hacer** — y el kit se regeneró con las tres piezas. Su criterio rector: el §15 se alinea
> con **la plataforma que se construyó**, y toda poda de §15 sigue sin aplicarse (con dos
> enmiendas: PODA-04 conserva RTSP/RTP y §15.4.3; PODA-03 comprime las métricas MOT en vez
> de eliminarlas).
>
> ✎ **2026-08-27 (noche) — §15: pases 1 y 2 APLICADOS Y VERIFICADOS.** GPT iteró dos veces sobre
> `desarrollando/Etapa 1 — copia ajustada E1 2026-08-27.docx`: la primera aplicó E1-01…E1-12
> y la poda (22.266 → 10.870 palabras, dentro del 5 % de lo pre-autorizado en `ajustes/07`;
> las brechas §15.2.5 y §15.4.3, RTSP/RTP y las 7 tablas quedaron intactas); la revisión
> [`desarrollando/archivado/correcciones-etapa-1-pase-2.md`](desarrollando/archivado/correcciones-etapa-1-pase-2.md)
> (E1-13…E1-23, D-E1-7/8) encontró seis daños colaterales de la compresión y dos pasajes que
> prescribían criterios nuestros como literatura; la segunda iteración los resolvió (verificado
> por diff, §6 del pase 2; 10.725 palabras). La afirmación sobre GroundingDINO-B (COCO en su
> entrenamiento, 56,7 AP) se verificó contra el README oficial. **Quedan R1–R3** (una fila de
> Tabla 4, formato de una ficha, **delta de referencias**: altas Kumar 2022 · Lee 2023 · OASIS 2019
> · Ultralytics 2026; Luxonis → s. f.-b; bajas de PODA-18). **`90d` re-extraído de esta versión**
> (regla D-C). **D-E1-7: PODA-17 invertida — la Tabla A.1 se conserva y corrige**, porque el
> cuerpo podado depende de ella. Falta de la Etapa 1: **§16 y Anexo A**.
>
> ✎ **2026-08-27 (cierre) — PASE 3 ESCRITO: el relevamiento de §16 que `AJ-1.16` declaraba
> pendiente.** [`desarrollando/archivado/correcciones-etapa-1-pase-3.md`](desarrollando/archivado/correcciones-etapa-1-pase-3.md)
> — **E1-24…E1-51** y **D-E1-9…12**, NO aplicado. Cubre las dos piezas de la Etapa 1 que nunca
> recibieron pase (§16 y Anexo A) y cierra los residuales de §15. Hallazgos que mandan:
> **(a)** §16.3.5.1 y §16.7.4 afirman que la retención OVD depende de la familia arquitectónica
> — lo que el §15 corregido **refuta**: el informe se contradice a sí mismo, y el puntero
> "§15.2.4.5" ya no existe. **(b)** *"negación"* aparece **cero veces** en las 30.749 palabras
> de §16: falta el fundamento conceptual del mecanismo central de la tesis — se repone con ARO
> (arXiv:2210.01936) y Winoground (arXiv:2204.03162), **ambas verificadas**. **(c)** §16.7+§16.8
> = **4.790 palabras con cero citas**, y §16.7.4/§16.7.5 prescriben la arquitectura construida
> (el texto admite que viene "del anteproyecto"). **(d)** La **ecuación que define G2A está
> VACÍA** en el archivo, y §16.5 descompone en 6 componentes mientras §17.1.7 usa 4 (sin
> `t_preprocess`) ⇒ **PODA-06 y PODA-07 son reescrituras, no recortes**. **(e)** PODA-11
> rescataba un mapa de brechas **5/6 duplicado con §15**. **(f)** Tabla A.1: conserva la errata
> de licencias `AJ-1.09` y **no incluye a Grounding DINO**. **(g)** Tres citas con letra de
> desambiguación **falsa** (Jeong 2022a/b · Shi 2016a/b · X. Wang 2020a/b, una sola entrada
> cada una): prueba de que el material se escribió dos veces.
> **D-E1-11 requiere decisión del equipo**: §16 deja abierta la obligación de inscripción ante
> la AAIP y el proyecto sí grabó personas. Kit regenerado con el pase 3 rotulado **NO aplicado**.
>
> ✎ **2026-08-27 (cierre 2) — CONTENIDO DE LA ETAPA 1 CERRADO; queda solo formato.** El pase 3
> se aplicó completo: la entrega trae **§15 + §16 + Anexo A + Referencias, 26.685 palabras**
> (§16 de 30.749 → 11.563 · Anexo A de 771 → **3.945**, la inversión de PODA-17). Entró lo
> difícil: **§16.3.4 nueva — *"Composicionalidad, Negación y Condiciones Definidas por
> Ausencia"*** con ARO y Winoground (E1-25, el fundamento del mecanismo central, que faltaba);
> la ecuación `t_G2A = t_capture + t_transport + t_preprocess + t_inference`; §16.5.3 con
> productor-consumidor y pub/sub; Tabla A.1 de 12 a **20 filas, ahora con Grounding DINO**;
> la contradicción sobre familias arquitectónicas eliminada de sus **dos** apariciones; 83
> referencias **sin huérfanas**. La AAIP quedó bien resuelta: **marcada con `[[PENDIENTE]]`**,
> no inventada (D-E1-11 sigue siendo del equipo).
> ✎ **Cerrado el mismo día:** los dos defectos de formato se repararon de forma determinista
> sobre el `.docx`: estilos trasplantados de hermanas sanas y renumeración §16.7.6 → **§16.7.3**.
> Y una **revisión exhaustiva** posterior encontró dos incumplimientos más de la regla de la
> casa sobre tablas, también corregidos: **E1-54** (la Tabla 5 era la única sin frase que la
> anunciara en prosa) y **E1-55** (la Tabla 9 era la única sin Nota ni Fuente — defecto
> heredado del v1.1). **Documento final: `Etapa 1 — final 2026-08-27.docx`**, sin sobrescribir
> ninguna entrega. Verificado: 94 títulos con estilo exacto · sin huecos de numeración · todas
> las remisiones internas resuelven **y apuntan al lugar correcto** · **las 13 tablas con nota,
> fuente y mención en prosa** · 83 referencias sin huérfanas · cero andamiaje. Verificador en
> **OK**. **La Etapa 1 queda cerrada.**
> **Se corrigió a propósito solo lo de esta etapa:** el rótulo de las notas tiene cinco
> variantes tipográficas, pero **es un problema de todo el informe** (§17.3 tiene seis, §17.1
> otra) — va al pase de integración final, no acá.
> Quedan dos cosas que no son redacción: **D-E1-11** (decisión del equipo, **queda marcada con
> `[[PENDIENTE]]` en el documento**, como se pidió) y una **dependencia hacia la Etapa 2**:
> §17.1 (`96b` L589) remite a "la sección 16.7.6", hoy §16.7.3 — se corrige al trabajar esa
> etapa, no bloquea.
>
> **Los dos defectos de FORMATO que se detectaron**, en
> [`desarrollando/archivado/correcciones-etapa-1-pase-4.md`](desarrollando/archivado/correcciones-etapa-1-pase-4.md):
> **E1-52** — cinco encabezados **contiguos** perdieron su estilo de título (§16.5.3, §16.5.4,
> §16.5.5, **§16.6** y §16.6.1): no entran al índice automático, y el texto es correcto —
> **E1-53** — hueco de numeración (§16.7.6 → §16.7.3).
> ✎ **Causa y remedio del flujo:** los dos defectos son **daño de transporte**, no de
> redacción — aparecieron al conectar el Project a Drive y editar ahí. Ir a Drive era
> **innecesario**: el paquete de la etapa ya contiene el texto vigente completo. Se agregó
> **`herramientas/verificar_entregable.py`** (26 tests) que detecta títulos sin estilo, huecos
> de numeración, fugas de andamiaje, markdown crudo y citas sin referencia — reporta los dos
> defectos y nada más. Y el kit incorporó la sección **"Cómo se trabaja y cómo se entrega"**
> (siete reglas, incluida *no Drive*), que viaja con el knowledge. **`90d` re-extraído: ahora
> es la Etapa 1 completa y SUPERA a `96c`, `96d` y al Anexo A de `96e`**, que salieron del
> paquete.
>
>
> ✎ **2026-08-27 (cierre real) — el entregable de la Etapa 1 es SOLO EL DESARROLLO.** Decisión
> del usuario: el `.docx` de la etapa lleva **§15 y §16, sin Anexo A y sin listado de
> referencias** — el Anexo A pertenece a §19 y las referencias son globales del informe, y los
> arma el equipo. **`Etapa 1 — final 2026-08-27.docx` quedó en 22.772 palabras ≈ 104 páginas**
> (antes 26.727 ≈ 121). El corte no tocó una palabra del desarrollo, verificado por diff.
> **De dónde salían las páginas** (el arranque tenía ~90 y eran de §15 SOLO): §15 bajó de 22.169
> a 10.791 palabras —**la mitad**—, y lo que agregó volumen fue **§16 entero (11.981 palabras,
> ≈54 páginas), que nunca había estado en este documento** y era la pieza que faltaba de la
> etapa. Es decir: **dos capítulos hoy pesan lo que pesaba uno solo al empezar.**
> El Anexo A y las Referencias corregidos **no se descartaron**: quedaron en
> **`90e-etapa1-anexo-a-y-referencias.md`**, porque el cuerpo de §15 **cita la Tabla A.1** y
> §15.3.3 **cita la Tabla A.2** — si no llegan a §19, quedan dos remisiones colgadas.
>
> 📁 **2026-08-28 — nomenclatura y limpieza final de la Etapa 1.** El documento pasó a seguir la
> convención de las demás secciones en desarrollo:
> **`E-OVRT-VDP_Secciones_15_y_16_Estado_del_Arte_y_Marco_Teorico_v1.0.docx`** (antes
> `Etapa 1 — final 2026-08-28.docx`). Se archivó el `Etapa 1.docx` original que había reaparecido
> en la carpeta —duplicado en contenido del que ya estaba en `archivado/`—. **En
> `desarrollando/` quedan solo los cuatro documentos vigentes**, uno por sección en trabajo:
> §15+§16 v1.0 · §17.3 v1.4 · §17.4 v1.6 · §17.5 v1.3. Las cinco referencias al nombre anterior
> (generador del kit, resumen de cambios, este archivo, pase 5 y el banner de `90d`) se
> actualizaron **en el mismo movimiento**; `90d` re-extraído; kit regenerado y verificado.
>
> ⚠✅ **2026-08-28 (noche) — pase de formato de tablas: bueno, pero venía de una base vieja.**
> `Etapa_1_final_definitiva.docx` mejoró las tablas de verdad — **corrigió un defecto real: TODAS
> las filas estaban marcadas como cabecera** (Word las repetía al cortar página) y ahora solo la
> primera; anchos unificados; 6 tablas ganaron encabezado en negrita. **Pero se construyó sobre la
> entrega del pase 5, no sobre el final**, así que revirtió cuatro correcciones posteriores:
> **E1-57** volvió *"ingesta multi-protocolo, decodificación acelerada"* (capacidad que no existe);
> **E1-58** volvieron los 3 runs en negrita+itálica que **parten palabras** y la negrita parcial del
> título §16.6.2.1; y se perdieron las **itálicas de `person`/`hardhat`/`head`** en la celda de la
> Tabla 5. Las cuatro se re-aplicaron sobre la definitiva (validación XML previa), conservando sus
> mejoras. **Final vigente: `E-OVRT-VDP_Secciones_15_y_16_Estado_del_Arte_y_Marco_Teorico_v1.0.docx`** — verificador OK, 11 tablas con
> columnas uniformes y cabecera repetida solo en la 1ª fila, cero formatos partiendo palabras,
> `[[PENDIENTE]]` intacto. Versiones previas en `archivado/`.
> **Lección de proceso:** al pedir un pase nuevo hay que entregar **el último final**, no la entrega
> anterior — si no, se pierden las correcciones aplicadas después.
>
> 📄 **2026-08-28 — [`resumen-cambios-etapa-1.md`](resumen-cambios-etapa-1.md):** comparación del
> `Etapa 1.docx` inicial (solo §15) y el v1.1 de §16 contra el final — 52.362 → 22.072 palabras,
> los seis tipos de ajuste con ejemplos, antes/después por sección, qué salió del entregable sin
> descartarse (`90e`), qué queda abierto y cómo se verificó. Es el documento para leer primero.
>
> ✎ **2026-08-28 — D-E1-13 (usuario): la extensión de la Etapa 1 queda como está.** ~100 páginas
> (§15 10.800 w + §16 12.000 w) se aceptan por aporte; el segundo nivel de poda identificado
> (Tabla 8 → solo RTSP · genealogía legal de §16.2.1 · régimen de datos de §16.6.2) **se descarta**:
> cada corte sacaba una vara o un ancla. Regla que rige: *no se recorta por recortar; siempre
> justificado.* No reabrir.
>
> ✅ **2026-08-28 — ETAPA 1 CERRADA. Documento final: `desarrollando/E-OVRT-VDP_Secciones_15_y_16_Estado_del_Arte_y_Marco_Teorico_v1.0.docx`
> (§15 + §16, 22.946 palabras).** La entrega del pase 5 (`Etapa_1_final_ajustada_pase_5.docx`)
> cumplió F1–F6 completos y **vino con cambios controlados** (173 ins / 170 del — la primera):
> 39 títulos a tipo frase, 11 rótulos `**Tabla**`, 11 notas `*Nota.*`, terminología unificada
> (fotograma 0 · frame 0 · E2E 0), IoU/SFU/NACK definidas; las 26 líneas de prosa cambiadas son
> todas terminología. **Lectura completa de punta a punta contra la implementación** dejó dos
> hallazgos, corregidos de forma determinista sobre el `.docx`: **E1-57** §15.4.3.1 describía el
> sistema como de *"ingesta multi-protocolo, decodificación acelerada"* (no tiene ninguna de las
> dos; heredado del v1.1) → *"ingesta de video"*; **E1-58** tres frases de §16.5 con runs en
> **negrita+itálica que partían palabras** (*"pro|tocolo … la s|elección"*) más un título con
> negrita parcial — **heredado del pase 3**, invisible en la extracción salvo por los asteriscos.
> Verificador OK · diff vs entrega = solo esos cuatro párrafos · `90d` re-extraído. La entrega y el
> final previo quedaron en `archivado/`. Constancia completa en el ✎ del pase 5. Quedan solo
> D-E1-11 (`[[PENDIENTE]]` AAIP, del equipo) y la remisión 16.7.6→16.7.3 de §17.1 (Etapa 2).
>
> ✎ **2026-08-27 — PASE 5 ESCRITO: el último, solo formato y terminología.**
> [`desarrollando/archivado/correcciones-etapa-1-pase-5.md`](desarrollando/archivado/correcciones-etapa-1-pase-5.md)
> es el brief que se le entrega a GPT **junto con el `.docx`** (esta vez sin Drive: se edita el
> archivo entregado, con cambios controlados). El contenido está cerrado (64/64 unidades
> verificadas); lo que falta para que quede al formato de §17.3–§17.5 son seis cosas medidas
> sobre el texto: **F1** 39 títulos en Title Case → tipo frase (la vara: 85 de 86 títulos de
> §17.x son tipo frase) y los cuatro "Bloque X" con el mismo separador · **F2** 7 rótulos
> `***Tabla N***` → `**Tabla N**` · **F3** 11 notas en 4 variantes → *Nota.* itálica (APA 7,
> como §17.5) · **F4** 4 rótulos de párrafo con el punto fuera de la negrita · **F5**
> terminología: cuadro (no fotograma/frame) · extremo a extremo (no end-to-end/E2E, salvo
> "arquitecturas end-to-end") · seguimiento (no tracking, salvo tracking-by-detection) · **F6**
> definir IoU, SFU y NACK la primera vez (OVD/EPP/AP/FPS/MOT ya están en el glosario §11).
> Criterio de aceptación escrito en el brief: el diff debe mostrar **solo** F1–F6 y el conteo
> quedar en 22.800 ± 60; cualquier cambio de contenido rechaza la entrega. Kit regenerado con
> el pase 5 como único **NO aplicado**.
>
> ✎ **2026-08-27 — E1-56, precisión YOLOE-11.** Al verificar el nombrado de YOLOE-26 (E1-02) se
> detectó que la oración atribuía las variantes sobre YOLO11 a "implementaciones posteriores de
> Ultralytics"; **contra el repo oficial THU-MIG/yoloe, YOLOE-11 es del paper original** — solo
> YOLOE-26 es la extensión posterior. Corregido en el `.docx` (único cambio, diff verificado);
> respaldo previo en `archivado/`. `90d` re-extraído; verificador OK.
>
> ✎ **2026-08-27 — `desarrollando/` limpio.** Al cerrar la Etapa 1 se archivó todo lo superado:
> las **cuatro versiones previas del `.docx`** (`Etapa 1.docx`, las dos `copia ajustada` y
> `formato corregido`) y los **cuatro pases ya aplicados** (`correcciones-etapa-1*.md`), todos a
> `desarrollando/archivado/`. En `desarrollando/` quedan **solo los documentos vigentes**: el
> final de la Etapa 1 y los tres `.docx` en desarrollo de §17.3, §17.4 y §17.5. Las referencias
> del generador del kit y los enlaces de este archivo se actualizaron **en el mismo movimiento**
> — la vez anterior, archivar sin actualizar dejó el kit roto para tres etapas.
>
> ⚠ **Deuda detectada el 2026-08-27, no resuelta:** el documento de trabajo de §17.4 avanzó a
> **v1.6** y `90b` sigue extraído de **v1.5**. Antes de volver a trabajar la etapa 4, re-extraer.
>
> ✎ **Las correcciones firmadas son TRES pases, y hay que leer los tres** (✎ 2026-08-22):
> - [`desarrollando/archivado/correcciones-etapa-3-4.md`](desarrollando/archivado/correcciones-etapa-3-4.md)
>   — **pase 1**, ítems E3-01…E3-18 y E4-01…E4-19. Sus decisiones **D1–D4** y la regla de
>   autocontención **siguen rigiendo**. (Se movió a `archivado/` el 2026-08-20; el enlace
>   anterior desde este archivo apuntaba a la ruta vieja.)
> - [`desarrollando/archivado/correcciones-etapa-3-4-pase-2.md`](desarrollando/archivado/correcciones-etapa-3-4-pase-2.md)
>   — **pase 2**, ítems E3-19…E3-31, E4-20…E4-23 y opcionales C-01…C-04. Continúa la
>   numeración del pase 1, **no reabre** sus decisiones y agrega **D-P2-1…D-P2-6**. Manda
>   sobre el resto del material de estas dos etapas.
> - [`desarrollando/archivado/correcciones-etapa-3-4-5-pase-3.md`](desarrollando/archivado/correcciones-etapa-3-4-5-pase-3.md)
>   — **pase 3** (2026-08-22), sobre los 40 comentarios traídos en los dos `.docx`. Ítems
>   **E3-32…E3-42** y **E4-27…E4-30**, decisiones **D-P3-1…D-P3-6**, y **dos enmiendas que
>   MANDAN sobre el pase 2**: a **E3-22** (las viñetas que proponía ya existen como prosa) y a
>   **E4-22** (afirmaba que la preselección en el borde no se ejerció, y es falso). Su §D fija
>   las restricciones de redacción de la **etapa 5** — con el esquema temático de organización
>   del §17.5 en **§D.0** (D-P3-6: por pregunta de medición, nunca por cronología de campañas)
>   — y su **§H** es la tabla de verificación cruzada de alineación entre §17.3 y §17.4.
>
> Los tres entran al project-kit: los pases 1 y 2 en las etapas 3 y 4; el pase 3 también en la 5.
>
> ✎ **2026-08-20 — enmienda E4-19 (a E4-14) en el mismo doc de correcciones:** §17.4.8 se
> amplía a cuatro subsecciones ("Construcción del banco temporal y de la referencia humana
> de evaluación": adquisición/rodaje · segmentación con criterios ex-ante · preanotación y
> revisión en CVAT · derivación y congelamiento), con ajuste breve en §17.4.1. Al aplicar
> las correcciones de §17.4, usar E4-19 y NO el texto guía original de E4-14 (quedó
> marcado como enmendado). Kit regenerado ese día.
>
> ✎ **2026-08-22 — cuatro unidades nuevas y una decisión nueva en el pase 2.** **E3-29**
> (§17.3.10.3 reescrita: dos afirmaciones falsas sobre el ledger de entregas y dos límites
> de interpretación ausentes), **E3-30** (§17.3.11.1 se elimina y se absorbe en el
> párrafo introductorio de §17.3.11), **E3-31** + **E4-23** y la decisión **D-P2-5**: los
> identificadores versionados de contrato (`media.detection.v1`, `clip_gt.v2`, …) y los
> literales de protocolo **salen de §17.3 y se declaran en §17.4**, donde la Tabla 63 ya es
> su punto de declaración; §17.3 conserva el versionado como compromiso abstracto. Además,
> **enmienda a E3-28**: `fail-open` pasa a definirse en prosa en §17.3.7.5 en vez de en una
> celda de tabla. Al aplicar §17.3, usar **E3-31 y la enmienda**, no sus versiones previas.
>
> ✎ **2026-08-22 (cont.) — D-P2-6 y E4-24: un identificador se declara UNA vez.** Medido: de
> los 11 identificadores del par, **9 son `.v1`**, así que el sufijo casi nunca informa y sólo
> quiebra el registro del texto. Regla: la **prosa se lee en castellano** ("evento de
> percepción", "alerta interna", "envoltorio del bus") y un identificador literal **nunca es
> sujeto gramatical**; cada uno aparece **una sola vez, en la Tabla 63** de §17.4.2, único
> punto de declaración. Única excepción: la referencia temporal en §17.4.8, donde la versión
> *es* el argumento. El **CamelCase** (`PerceptionEvent`) **no se persigue**: es la
> denominación de diseño de D1 y aparece sólo en celdas de tabla (cero en prosa, verificado).
>
> 🔎 **2026-08-28 — ETAPA 2 ARRANCA: revisión previa, sin nada aplicado.** Entró
> `desarrollando/17.1.docx` (§17.1 exportado del maestro; 32.669 palabras, 122 títulos, 85
> ecuaciones OMML). **Es el §17.1 del v1.1 sin ninguna corrección**: 664 párrafos idénticos a `96b`
> salvo el espaciado de `Nota.`; cero `AJ-2.xx` aplicados, sin comentarios ni cambios controlados.
> La revisión completa de alineación está en
> [`desarrollando/archivado/revision-previa-etapa-2.md`](desarrollando/archivado/revision-previa-etapa-2.md):
> doctrina vigente y 9 handoffs hacia §17.1 (§2), **12 desvíos del set a corregir antes de armar el
> paquete** (§3; dos 🔴: el kit redacta desde `96b` en vez de una extracción propia, y el preámbulo
> del kit sigue diciendo que la Etapa 1 está "a mitad de camino" y §17.4 en v1.5) y **8 decisiones
> D-E2-1…8 del usuario** (§4; entre ellas el bautismo E-DIR/E-IND/E-HYB con la dependencia inversa de
> E3-42, el nivel "estado por persona" que §17.5 usa y §17.1 no pre-registra, y qué hacer con
> AJ-2.02, cuya premisa es falsa: §17.1 no menciona cooldown). Verificador sobre el `.docx`: FALLA 1
> — §17.1.1 en `Heading 2` con tabulador, **heredado del maestro**. El documento todavía no tiene
> nombre de convención ni `90f`; el pre-flight está en §5 de la revisión.
>
> ✅ **2026-08-28 — RELEVAMIENTO EXHAUSTIVO DE LA PLATAFORMA + ALINEACIÓN DE PUNTA A PUNTA + KIT
> DESDE CERO.** Constancia: [`operacion/130`](../../operacion/130-relevamiento-plataforma-pre-etapa-2.md)
> (seis agentes de sólo lectura: los cinco repos contra los docs y contra §17.1, más el set contra sí
> mismo; informes con `ruta:línea` en `operacion/datos/130-relevamiento-pre-etapa-2/`). Veredicto: la
> plataforma está donde los docs dicen en lo estructural (árboles limpios, 26 cifras verificadas,
> `bench_v3` byte a byte), pero **23 divergencias doc↔código (R-01…R-23, cuatro 🔴)** y **37 hallazgos
> doc↔doc** estaban vivos: el orden de arranque live real es **control → distribución → medios** (FIG-A y
> el `CLAUDE.md` raíz decían lo contrario); el fine-tuning **excluyó `chv`** (varias fichas decían que lo
> entrenó); `gdino-tiny` 800 px corrió a `box_threshold` 0,35 y el 560 a 0,30 (comparación confundida);
> el rango 500–2.000 de la Tabla 28 se desvió a 2.946 sin justificar. **Todo corregido en el set con ✎**
> (130 §7 lista los archivos) y en los READMEs de los repos hermanos. **Kit regenerado desde cero**: la
> etapa 2 redacta desde `90f` (no `96b`), su paquete trae el pase `correcciones-etapa-2.md`, el
> contrato de etapa y la tabla protocolo-vs-construido de 130 §4; el preámbulo ya no dice que la
> Etapa 1 está "a mitad de camino"; `--check --etapa all` OK, 62 tests. **Decisiones firmadas para la
> Etapa 2: D-E2-1/2/5/6** (sólo §17.1 · bautismo E-DIR/E-IND/E-HYB en §17.1.5.4.2 · AJ-2.13 nivel
> "estado por persona" · MOT intacto ⊘); D-E2-3/4/7/8/9 por recomendación. El documento de trabajo
> pasó a `desarrollando/E-OVRT-VDP_Seccion_17.1_Consolidacion_Metodologica_v1.0.docx`. **Lo que
> sigue: ChatGPT aplica `correcciones-etapa-2.md` sobre ese `.docx`** (pase 1 de contenido, después
> pase 2 de formato F1–F6), y se verifica con `verificar_entregable.py --seccion 17.1`.
>
> ✅ **2026-08-28 (noche) — §17.1 CERRADA EN CONTENIDO: v1.3.** ChatGPT entregó la v1.2 (pase E2 +
> formato en una pasada, sin cambios controlados). Revisión de pie a cabeza contra `90f` v1.0 y contra
> el pase: **59 párrafos nuevos, 97 eliminados, 113 modificados** (35 sólo terminología); las 26
> unidades E2 aplicadas o resueltas como ⊘ según el pase; Tablas 24/28/36/37 intactas; §17.1.6.3 y
> §17.1.7.4.2 (MOT) intactos; **cero fugas de andamiaje, cero cifras propias**, un solo `[[PENDIENTE]]`
> (AAIP); 85 ecuaciones conservadas; sin runs partiendo palabras; remisiones al Anexo B verificadas
> contra B.1–B.7. Podas: §17.1.6.2 4.856 → 1.375 palabras · §17.1.10 eliminada · §17.1.4 −472 (PODA-14
> parcial). **Tres defectos de forma reparados de manera determinista sobre el XML → v1.3** (E2-27
> rótulos `Tabla`/`Nota` en negrita+itálica → `**Tabla N**` / `*Nota.*` como §15–§16 y §17.5 · E2-28
> frase de anclaje antes del marcador AAIP, que decía "esta inscripción" sin antecedente · E2-29 el
> párrafo puente de PODA-13 había caído dentro de §17.1.9.2 → movido a §17.1.11.2). Verificador **OK**
> (28.534 palabras, 118 títulos). **13 citas dieron de baja** con PODA-12 (lista en la constancia) —
> delta para las Referencias globales del equipo. Constancia:
> [`desarrollando/archivado/correcciones-etapa-2-pase-2.md`](desarrollando/archivado/correcciones-etapa-2-pase-2.md).
> `90f` re-extraído de la v1.3; kit regenerado con el pase rotulado **YA APLICADO**; v1.0 y v1.2 en
> `archivado/`.
> 📄 Resumen legible de qué cambió respecto del inicial:
> [`resumen-cambios-etapa-2.md`](resumen-cambios-etapa-2.md) (hermano del de la Etapa 1). **Queda de la etapa (fuera del `.docx`):** `90g` (Anexos C y D) y los handoffs a
> §17.3 (recorte de §17.3.6.4), §17.4 (orden de disparo, desviación 500–2.000) y §17.5.

## El texto extraído

| Archivo | Qué contiene | Etapa del plan |
|---|---|---|
| `96a-informe-v11-frontmatter-intro-objetivos-plan.md` | frontmatter, §11 Glosario, §12 Introducción, §13 Objetivos, §14 Plan de trabajo (**§14.2 define las etapas**) | transversal |
| **`90d-etapa1-texto-extraido.md`** | **§15 + §16 (Etapa 1, CERRADA 2026-08-28)** — texto base FINAL, extraído de `desarrollando/E-OVRT-VDP_Secciones_15_y_16_…_v1.0.docx`, cinco pases aplicados | **1** ✅ |
| `96c-informe-v11-estado-del-arte.md` | §15 del informe v1.1 — **SUPERADO por `90d`**, foto histórica | — |
| `96d-informe-v11-marco-teorico.md` | §16 del informe v1.1 — **SUPERADO por `90d`** (✎ 2026-08-28; antes decía "texto base vigente sin pase"), foto histórica | — |
| **`90f-etapa2-texto-extraido.md`** | **§17.1 Consolidación Metodológica (Etapa 2)** — texto base VIGENTE, extraído de `desarrollando/E-OVRT-VDP_Seccion_17.1_Consolidacion_Metodologica_v1.3.docx` con el pase `correcciones-etapa-2.md` y el de formato **APLICADOS Y VERIFICADOS** (✎ 2026-08-28 noche) | **2** ✅ |
| `96b-informe-v11-17-1-consolidacion-metodologica.md` | §17.1 + §17.2 del informe v1.1 — **SUPERADO por `90f`** (mismo contenido; foto histórica) | — |
| `90-etapa3-texto-extraido.md` | **§17.3 Diseño arquitectónico** (v1.4), §17.3.1 a §17.3.18 | **3** |
| `90b-etapa4-texto-extraido.md` | **§17.4 Implementación** — extraído de **v1.6** (re-extraído 2026-08-28; antes v1.5) | **4** |
| `90c-etapa5-texto-extraido.md` | **§17.5 Evaluación y validación** (v1.3) | **5** |
| `96e-informe-v11-cierre-anexos-referencias.md` | §17.4–§17.6 (**los tres placeholders**), §18 Cierre, §19 Anexos A–D, Referencias | 4, 5, 6 |

---

## Lo que está vacío, y es lo que importa

> ✎ **2026-08-28 — esta sección describe el MAESTRO, no el estado del trabajo.** En el maestro
> §17.4/§17.5/§17.6 siguen siendo placeholders, pero §17.4 (v1.6) y §17.5 (v1.3) **ya están
> redactadas** en `desarrollando/` con sus pases aplicados; lo que falta es integrarlas. Sin
> redactar de verdad: §17.6, §18 y §19. El estado por etapa manda desde el kit (`00-contexto-base`,
> "Qué está CERRADO y qué está ABIERTO") y desde `operacion/130`.

En `96e`, las tres secciones finales del capítulo 17 son placeholders literales:

```
### 17.4. Implementación del prototipo experimental
[Agregado futuro correspondiente a la Etapa 4]

### 17.5. Evaluación y validación del prototipo
[Agregado futuro correspondiente a la Etapa 5]

### 17.6. Documentación técnica, repositorio y evidencias de cierre
[Agregado futuro correspondiente a la Etapa 6]
```

**Ese es el estado del informe hoy:** las etapas 1 a 3 están escritas y necesitan
correcciones; las etapas 4 a 6 no existen todavía. El trabajo experimental que las
sostiene está cerrado y verificado — lo que falta es escribirlas.

## De acá salen los ajustes

| Sección | Ajustes | Documento |
|---|---|---|
| §11–§14 | 7 (`AJ-0.x`) | [`../ajustes/00-mapa-de-ajustes.md`](../ajustes/00-mapa-de-ajustes.md) §4 |
| §15, §16, Anexo A | 16 (`AJ-1.x`) | [`../ajustes/01-etapa-1-fundamentacion-teorica.md`](../ajustes/01-etapa-1-fundamentacion-teorica.md) |
| §17.1, Anexos C y D | 12 (`AJ-2.x`) | [`../ajustes/02-etapa-2-consolidacion-metodologica.md`](../ajustes/02-etapa-2-consolidacion-metodologica.md) |
| §17.3 | 26 (`R-01…R-26`) | [`../ajustes/03-etapa-3-diseno-arquitectonico.md`](../ajustes/03-etapa-3-diseno-arquitectonico.md) |
| §17.4 | 12 (`AJ-4.x`) | [`../ajustes/04-etapa-4-implementacion.md`](../ajustes/04-etapa-4-implementacion.md) |
| §17.5 | 13 (`AJ-5.x`) | [`../ajustes/05-etapa-5-evaluacion-y-validacion.md`](../ajustes/05-etapa-5-evaluacion-y-validacion.md) |
| §17.6 · §18 · §19 | 5 (`AJ-6.x`) | [`../ajustes/06-etapa-6-documentacion-y-cierre.md`](../ajustes/06-etapa-6-documentacion-y-cierre.md) |
