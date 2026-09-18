# El informe tal como está hoy

> 📋 **Lo que FALTA está en [`00-lo-que-resta.md`](00-lo-que-resta.md)** (✎ 2026-09-01): la
> lista única de pendientes con dueño y bloqueo. Este archivo narra la historia por jornada;
> ese otro es el índice de lo que queda por hacer.
>
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

## El entregable (✎ 2026-09-18)

| Archivo | Qué es | Fecha |
|---|---|---|
| **`desarrollando/E-OVRT-VDP_Informe_Final_2026-09-16_v0.1.docx`** | **EL INFORME FINAL, COMPLETO** — portada, §2–§19, Anexos A–F y Referencias; 82k palabras, 73 tablas, 8 figuras; sin comentarios ni cambios rastreados. Leído de punta a punta el 09-18. | 16/09/2026 |
| `90-informe-final-2026-09-16-v0.1-texto-extraido.md` | Su foto de texto (regla D-C), regenerable con `herramientas/extraer_informe.py` | 18/09/2026 |
| `desarrollando/revision-informe-final-v0.6-2026-09-15.md` | Revisión externa de coherencia/cohesión sobre la v0.6 (414 pp); su verificación mecánica contra la v0.1 está en `00-lo-que-resta.md` §0 | 15/09/2026 |

> ✎ **2026-09-18 — EL INFORME ESTÁ COMPLETO. Todo lo que sigue abajo es historia del camino.** La
> v0.1 del 09-16 integra las secciones cerradas (§15/16 v1.4, §17.1 v1.21, §17.3 v1.12, §17.4 v1.15,
> §17.5 «v1.5»), la Etapa 6 (§17.6/§18/§19, v1.5 con Figura 4.7 → aquí 4.6), las secciones iniciales
> hasta §14 (v1.1) y los costos (§14.4/§17.2). Superados y **movidos a `desarrollando/archivado/`**:
> todos esos `.docx` por sección, el maestro `E-OVRT-VDP_v1.1_05062026-sin-indice.docx`, las actas
> de los pases, los mapas de secciones y los análisis de sugerencias. **Movidos a `archivado/`**: las
> fotos por sección `90`/`90b`–`90g`/`96a`/`96e`, los resúmenes de cambios y `borradores/`. La tabla
> de "los dos entregables" que estaba acá se reemplazó por la de arriba.
> **Pendientes formales de la v0.1** → `00-lo-que-resta.md` (foto 2026-09-18).

> ✎ **2026-09-08 — AUDITORÍA BIBLIOGRÁFICA sobre el maestro y las cinco secciones cerradas.** Cruce
> mecánico de las 242 entradas del listado global contra las citas de las diez piezas vigentes, más cinco
> auditorías de lectura en paralelo, con cada hallazgo re-verificado contra el texto. **La causa de fondo
> es que el listado del maestro nunca se sincronizó con las correcciones de la Etapa 1: le faltan doce
> entradas que sí están en `90e`**, y eso explica once citas que no resuelven, incluidas las dos únicas
> fuentes sobre visión-lenguaje aplicado a seguridad en obra y la fuente de una fila de la Tabla A.1.
> Además: **§17.5 no invoca ninguna vara de §15**, **§11–§14 no cita nada**, **104 de 242 entradas están
> huérfanas** y **Kuhn (1955) es el paper viejo**, huérfano mientras el algoritmo húngaro se nombra sin
> atribuir. Veintiún preprints tienen versión publicada: citarlos bien sube la literatura arbitrada del
> 37 % al 46 % sin agregar una fuente. Sin fraude ni transcripción literal, y con la Tabla A.1 bien
> resuelta. Informe: [`desarrollando/auditoria-bibliografica-2026-09-08.md`](desarrollando/archivado/auditoria-bibliografica-2026-09-08.md),
> que pasa a ser el documento de ajustes vigente; el acta de los pases 5 a 5e se archivó.
>
> ✎ **2026-09-08, misma jornada — SEGUNDA BAJADA: el pase 5e ACEPTADO y CUATRO SECCIONES CERRADAS.**
> El usuario aceptó las tres sugerencias del 5e y bajó las cinco secciones renumeradas: §15/16 **v1.4** ·
> §17.1 **v1.21** · §17.3 **v1.12** · §17.4 **v1.15** · §17.5 **«v1.5»**. La vista aceptada de lo que entregué
> coincide **exactamente** con lo que volvió, sin una línea de más ni de menos. Tres de las cinco son sólo
> un cambio de número: §15/16, §17.3 y §17.5 son byte a byte idénticas a la v1.3, la v1.11 y la v1.9.
> ⚠ **El número de §17.5 retrocedió**: el archivo se llama v1.5 y existe una v1.5 histórica distinta, la base
> del pase 5. Citar esa sección por su estado, nunca por ese número, hasta que se renumere en Drive.
> **CERRADAS: §17.1, §17.3, §17.4 y §17.5.** §17.4 queda sin marcas y con 3 comentarios abiertos; §17.1,
> §17.3 y §17.5 quedan limpias. §15/16 sigue en revisión de los colegas (9 comentarios, la sugerencia del
> pase 5 sin resolver y el «puede puede» de 15.2.4).
>
> ✎ **2026-09-08 — EL MAESTRO VUELVE, Y CON UNA TRAMPA.** El usuario trajo un export nuevo de
> `E-OVRT-VDP_v1.1_05062026-sin-indice.docx` y lo puso en `desarrollando/`, que es donde vive ahora: es el
> destino de la integración. Sus 420 títulos son idénticos a los del export del 08-16, que quedó en
> `archivado/` con su paréntesis. **Lo que cambió es el nombre de los estilos**: el export nuevo trae
> `Ttulo1`…`Ttulo5` donde el viejo traía `Heading1`…`Heading5`, porque Google Docs los nombra según el
> idioma de la interfaz y les quita los acentos al normalizarlos. Con eso, `extraer_informe.py` veía **cero**
> títulos y `verificar_entregable.py` reportaba **420 problemas duros** falsos. Las tres herramientas
> reconocen ahora las dos familias (`pase_docx.py` además detecta cuál usa el documento antes de escribir un
> estilo), con dos pruebas nuevas que lo fijan. Sobre el maestro corregido quedan **4 observaciones reales**,
> todas suyas y esperadas: el salto de numeración de §8–§10, la §17.1 vieja empezando en 17.1.2, una fuga de
> andamiaje y 4 autorías sin entrada en Referencias.
>
> ✎ **2026-09-08 — BAJADA DEL USUARIO: las cinco secciones aceptadas; cuatro CERRADAS.** El usuario
> aceptó en Google Docs todas las sugerencias de los pases 5/5b/5c/5d y bajó §15/16 **v1.3** · §17.1
> **v1.19** · §17.3 **v1.11** · §17.4 **v1.13** · §17.5 **v1.9**. La vista aceptada de cada entrega
> comparada con su bajada coincide, salvo ediciones suyas (abreviatura en la Tabla 35, dos notas de
> §17.1 borradas, «Densidad» fusionada en la Tabla 64, negrita en rótulos «Nota») y **tres defectos del
> viaje por Google Docs**: los tres bloques de código insertados en §17.4 perdieron su última línea al
> aceptarse (dos llaves de cierre y `model_name`), quedó un título fantasma delante de 17.1.11 y un
> «puede puede» en §15.2.4. **Pase 5e** (`herramientas/pase5e_cierre.py`): §17.4 → **v1.14** (las tres líneas
> repuestas EN LIMPIO con comentario, y el único marcador `[[PENDIENTE]]` reemplazado como sugerencia por
> la lista pública de YouTube que el usuario dejó en un comentario) · §17.1 → **v1.20** (párrafo fantasma a
> Normal y título reescrito, como sugerencias; rechazar todo devuelve la v1.19). §15/16 **no se toca**: el
> colega sigue revisándolo (9 comentarios, 3 de un segundo colega que «llegó hasta» 16.2.2). **Vigentes:
> §15/16 v1.3 · §17.1 v1.20 · §17.3 v1.11 · §17.4 v1.14 · §17.5 v1.9.** Textos base re-extraídos por la
> regla D-C (`90d` ← v1.3 · `90f` ← v1.20 · `90` ← v1.11 · `90b` ← v1.14 · `90c` ← v1.9); kit regenerado
> con la **Etapa 6 como activa** y los cinco textos cerrados dentro de su paquete; entregas y bajadas
> superadas → `archivado/`. Acta: §14 de
> [`desarrollando/correcciones-pase-5-etapas-1-5.md`](desarrollando/archivado/correcciones-pase-5-etapas-1-5.md).
>
> ✎ **2026-09-07 — un solo documento de ajustes vigente.** En `desarrollando/` queda el acta del pase 5
> y nada más de ese tipo: las tres actas del pase 4 y la lectura transversal se archivaron. Los mapas de
> secciones se quedan porque son herramienta de lectura, no documento de un pase.
>
> ✎ **2026-09-07 — archivado de lo superado.** `desarrollando/` queda con los cinco `.docx` vigentes,
> las actas de pase, los tres mapas de secciones y la lectura transversal. Se archivaron **las cinco bases
> del pase 5** (§15/16 v1.2 · §17.1 v1.16 · §17.3 v1.8 · §17.4 v1.8 · §17.5 v1.5) y los **dos análisis**
> cuyo pase ya se aplicó y aceptó; los guiones `pase5_*.py` leen desde `archivado/` y los cinco pases se
> repiten con resultado idéntico parte por parte. En esta carpeta se archivaron `96b`, `96c` y `96d`
> (superados por `90f` y `90d`), el standalone de Etapa 3 y la variante `-sin-etapa3` del informe v1.1.
> En `herramientas/` se archivaron los once guiones de los pases 4 y 6, ya aceptados. Cada carpeta de
> archivado tiene su `00-que-hay-aca.md` con el criterio: entra lo superado, se queda lo que es
> constancia única o herramienta viva.
>
> ✎ **2026-09-07 — PASE 5: las cinco secciones entregadas con sugerencias y comentarios.**
> §15/16 **v1.3** · §17.1 **v1.17** · §17.3 **v1.9** · §17.4 **v1.9** · §17.5 **v1.6**, todas con
> «(sugerencias sin aceptar)». ✎ **Los pases 5b, 5c y 5d del mismo día** llevaron la configuración del
> entrenamiento a §17.4.7, bajaron la fila «Pruebas automatizadas» de la Tabla 59 y aplicaron la revisión
> completa (cinco auditorías cruzadas contra código e índices). **Vigentes: §15/16 v1.3 · §17.1 v1.18 ·
> §17.3 v1.10 · §17.4 v1.12 · §17.5 v1.8.** Veinte decisiones abiertas en el acta, §12. §17.5 recupera las ocho limitaciones y, tras la segunda vuelta del 07-09,
> **no lleva figuras de datos**: las dos insertadas se descartaron y su contenido volvió a tabla y a prosa,
> de modo que queda sólo el fotograma como Figura 4.6.
> §17.4 rehace la Figura 4.5 con la imagen vigente. Acta: [`desarrollando/correcciones-pase-5-etapas-1-5.md`](desarrollando/archivado/correcciones-pase-5-etapas-1-5.md).
> Compuerta verde en las cinco (rechazar todo devuelve el original · paquete OPC íntegro · verificador sin
> problemas duros). **Los textos base `90*` siguen siendo los del 09-06 y se re-extraen recién al aceptar**
> (regla D-C). Herramientas nuevas: `pase_docx.py` (edición quirúrgica, comentarios e imágenes),
> `rechazar_cambios.py` y `verificar_paquete.py`.
>
> ✎ **2026-09-07 — ronda de Google Docs del 09-06: cinco versiones nuevas en `desarrollando/`, lectura
> transversal escrita, extractor corregido.** Vigentes: §15/16 **v1.2** · §17.1 **v1.16** · §17.3 **v1.8** ·
> §17.4 **v1.8** · §17.5 **v1.5** (las anteriores, incluidas las dos «sugerencias sin aceptar» del 09-04, están en
> `archivado/`). Diagnóstico y lista de trabajo: [`desarrollando/lectura-transversal-etapas-1-5-2026-09-07.md`](desarrollando/archivado/lectura-transversal-etapas-1-5-2026-09-07.md). Regla D-C aplicada: `90f`, `90`, `90b` y
> `90c` re-extraídos de las versiones nuevas. **`extraer_informe.py` no atravesaba los controles de contenido
> `w:sdt` que exporta Google Docs**: por eso la celda «CR-02 en vivo» de la Tabla 64 salía vacía (el `.docx`
> siempre dijo «3 alertas: ≥ 7,1 s» — el 🔴 del 09-04 era del extractor) y las Tablas 28/29/30 de §17.1 salían
> sin cuerpo (existen: 16/20/8 filas). Parchado; 63 tests; `90f` pasa de 19 a 22 tablas.
>
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
> 📄 **2026-08-28 — [`resumen-cambios-etapa-1.md`](archivado/resumen-cambios-etapa-1.md):** comparación del
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
> [`resumen-cambios-etapa-2.md`](archivado/resumen-cambios-etapa-2.md) (hermano del de la Etapa 1). **Queda de la etapa (fuera del `.docx`):** `90g` (Anexos C y D) y los handoffs a
> §17.3 (recorte de §17.3.6.4), §17.4 (orden de disparo, desviación 500–2.000) y §17.5.
>
> 🔎 **2026-08-31 — LA ETAPA 2 SE REABRE CON UN PASE 3 (escrito, NO aplicado).** El usuario leyó la
> v1.3 de punta a punta y dejó **27 comentarios** en el `.docx`
> (`desarrollando/…v1.3- a revisar.docx` = v1.3 + las 2 ediciones del 08-30: §17.1.4.2.4 RTSP
> sintética eliminada y quinto supuesto en §17.1.10.2); la revisión crítica + auditoría verificada
> produjo [`desarrollando/correcciones-etapa-2-pase-3.md`](desarrollando/archivado/correcciones-etapa-2-pase-3.md)
> (**E2-30…E2-50**, decisiones **D-P3-1…9** de la etapa 2 — serie propia, no confundir con las
> D-P3 del pase 3 de §17.3; salida esperada: **v1.4**) y
> [`90g-etapa2-anexos-c-y-d.md`](archivado/90g-etapa2-anexos-c-y-d.md) (**D-E2-1 ejecutada**: Anexo C 5→3
> tablas, Anexo D 6→3; la ex-C.3 **contradecía** a la Tabla 31 del desarrollo). Lo estructural del
> pase: desduplicación (la peor: §17.1.4.7 contaba el CPN por cuarta vez; el cierre §17.1.11.2 lo
> contaba por tercera) con el **guardrail 2 enmendado por D-P3-1**; **Tablas 17 y 22 fuera** y
> renumeración interna 16–36 — habilitada porque se verificó que **§17.3/§17.4/§17.5 no citan
> ninguna tabla de §17.1 por número**; FT en EBE **condicionado** a §17.1.9 (no restringido — misma
> doctrina que la Tabla 28); 6 defectos de gramática y el 50–250 ms huérfano de la Tabla 21
> verificados **en el XML**. Targets v1.4: ~26,0–26,5k palabras · 109 títulos · 21 tablas ·
> **78 ecuaciones** (85−7 declaradas por unidad). `90f` **re-extraído el 08-31** del documento
> vigente (los derivados estaban 2 ediciones atrás — clase D2-01). ✎ **mismo día, D-P3-8
> (usuario): los Anexos C y D viajan AL FINAL del documento de la etapa** — el `90g` quedó
> reescrito como contenido completo listo para pegar (las 6 tablas finales; nombres de métrica en
> texto plano, unificación con ecuaciones → integración) y el pase ganó la unidad **E2-49**
> (anexado, último paso; encabezados sin número). ✎ **también 08-31 — D-P3-9, VOZ DEL DOCUMENTO
> (criterio traído por el equipo desde la Etapa 1)**: lo que remite a una sección que **existe**
> deja de sonar "a definir" y pasa a presente (unidad **E2-50**, 12 sitios). ⚠ Validado antes de
> adoptarlo: **la regla NO se aplica en bloque** — de los 41 `deberá` de §17.1, ~25 son
> prescripción normativa del protocolo y no se tocan, y lo **pre-registrado y no ejercido** no
> puede decir "se define más adelante" porque sería falso (lo reporta §17.5). Medido en el
> informe: **§15+§16 = 7 sitios** (pase del colega) · **§17.3 = 3** · **§17.4 y §17.5 = 0**, que
> es justo por qué el capítulo suena desparejo. Targets ajustados: ~28,4–29,0k palabras
> (desarrollo ~26,0–26,5k + anexos ~2,4k) · 109 títulos numerados · 21 tablas 16–36 + 6 de anexo
> · 78 ecuaciones · `deberá` de 41 a ~33 (nunca menos de 30). **Lo que sigue: ChatGPT aplica el pase 3 completo sobre el `.docx`** (los
> comentarios NO se tocan: los resuelve el usuario con el mapa §F del pase); al integrar, el
> equipo sólo muda los anexos a §19.3/§19.4; a la vuelta, verificación con los targets de §G y
> los greps en cero.
>
> ✅ **2026-08-31 (misma jornada) — §17.1 CERRADA EN CONTENIDO: v1.4, CON ANEXOS.** ChatGPT aplicó
> el pase 3 completo y la entrega pasó la verificación de §G **entera**: 28.730 palabras · **109
> títulos exacto** · **21 tablas 16–36 contiguas** · Anexos C (3 tablas) y D (3) al final con
> encabezados sin número en el estilo del título 17.1 · **78 ecuaciones exacto** · los 17 greps en
> cero · `todavía` = 7 · verificador OK. Diff párrafo a párrafo contra `90f`: 27 eliminados + 66
> modificados + 1 nuevo, **todos atribuidos a unidades del pase, cero cambios de afuera**; anexos
> fieles al `90g`. La entrega **trajo cambios controlados** (521 ins / 343 del, sin aceptar) y
> **conservó los 27 comentarios**. **Un solo defecto: E2-50 sitio 12** ("deberá realizarse sobre
> los datos del proyecto" en la justificación de OVT-B) — reparado determinísticamente sobre el
> XML (respaldo en `archivado/…(entrega GPT, antes de E2-50.12).docx`). Dos notas de auditoría en
> el banner del pase: E2-50.3 quedó absorbido por E2-38 (solapamiento de autoría, resultado
> correcto) y la guarda "deberá <30" estaba mal calibrada (valor final correcto: 28 en el
> desarrollo, las 12 desapariciones auditadas una por una — ninguna prescripción normativa
> tocada). **Derivados al día**: `90f` re-extraído de la v1.4 (la extracción corta en los anexos:
> viven en el `.docx` y en `90g`) · pase 3 → `archivado/` con acta en el banner · v1.3 y
> "a revisar" → `archivado/` · generador volteado a APLICADO · `INSTRUCCIONES-PROJECT` a v1.4 ·
> kit OK, 62 tests. **Handoffs vivos**: §17.3 v1.5 (recorte §17.3.6.4 +
> D-P3-9 ×3) · integración (anexos a §19.3/§19.4, hueco global de tablas 37–38, métricas del
> anexo a objetos de ecuación) · D-E1-11 AAIP.
>
> ✅ **2026-08-31 (cierre) — CAMBIOS ACEPTADOS Y 27 COMENTARIOS RESUELTOS: la v1.4 quedó limpia.**
> A pedido del usuario, ambas cosas se hicieron **sobre el XML** (abrir en LibreOffice reescribe
> el documento entero y arriesga las 78 ecuaciones; es la misma técnica de E1-52/53 y E1-56/58).
> Resultado: **0 marcas de revisión** (521 `w:ins` desenvueltas · 343 `w:del` fuera · 11 filas y
> las 2 tablas borradas retiradas · 95 párrafos vacíos desaparecidos · 21 `*Change`), **78
> ecuaciones**, 27 tablas, **109 títulos**, 28.628 palabras, todas las partes XML validadas,
> verificador OK; los 27 comentarios **se conservan con sus anclas y quedan marcados `done`**
> (`w15:done="1"` en `commentsExtended.xml`) — se borran en la integración final, no antes.
> ⚠ **Al aceptar apareció un defecto que la verificación por extracción no había detectado:
> E2-31 estaba aplicada DOS VECES** — GPT dejó una inserción huérfana con la numeración vieja
> ("…se presenta en la **Tabla 23**") dentro del párrafo borrado y con marca de párrafo borrada,
> que al aceptar habría duplicado la frase y remitido a la tabla equivocada. Se rechazó esa
> inserción antes de aceptar; verificado: la frase queda **una sola vez**, al final del párrafo,
> con "Tabla 21". **Lección (en el acta del pase):** cuando una unidad agrega texto y otra
> renumera, verificar que no sobreviva una copia con el número viejo; y correr siempre el chequeo
> "marca de párrafo borrada + texto vivo" (acá dio 1 de 95, y era exactamente el defecto).
> Respaldo: `archivado/…v1.4 (con cambios controlados y comentarios sin resolver).docx`.
> `90f` re-extraído del documento limpio; kit regenerado. **Queda del usuario: sólo git.**
>
> 🔎 **2026-08-31 (tarde) — PASE 4 DE LEGIBILIDAD ESCRITO (NO aplicado): la crítica del usuario,
> validada con datos.** Su impresión ("mucho desarrollo que pierde al lector, se puede desarrollar
> más simple sin perder robustez") se midió antes de actuar: la causa NO es la extensión del
> contenido sino **34 oraciones de metadiscurso** —el documento hablando de sí mismo— contra 11 en
> §17.3, **2 en §17.4 y 1 en §17.5**, más **14 párrafos de >150 palabras**; la oración media de
> §17.1 (24,1 palabras) es incluso más corta que la de §17.4 (26,0). El instrumento:
> [`desarrollando/correcciones-etapa-2-pase-4.md`](desarrollando/archivado/correcciones-etapa-2-pase-4.md)
> (**E2-51…E2-55**, D-P4-1/2; base v1.4 limpia → **salida v1.5**): reescribe en voz de sistema las
> cuatro "Introducción y alcance" y las aperturas de sección (conservando P-E1-xx con sus glosas,
> fronteras anti-anacronismo y TODAS las citas), y parte 12 párrafos gordos con 14 cortes
> especificados (la nota de la Tabla 21 no se parte; §17.1.5.4 se parte en su propia unidad). De
> paso repara la concordancia "de la cual toma" en §17.1.5.4. **Regla suprema D-P4-1: cero pérdida
> de información — "no reducir por reducir"** (pedido explícito del usuario). Targets v1.5:
> ~28.250–28.500 palabras · 109 títulos · tablas/ecuaciones/comentarios idénticos · metadiscurso
> ≤12 · párrafos gordos ≤2 · citas idénticas · chequeo anti-duplicación (lección del pase 3).
> **39/39 anclas verificadas** contra `90f`. Vara de voz del informe: **§17.5**. Handoffs: §17.3
> lleva 11 metadiscursos + 2 párrafos gordos a su v1.5; §15/§16 a medir (pase del colega).
>
> ✅ **2026-08-31 (cierre) — PASE 4 APLICADO: §17.1 v1.5 VIGENTE, aceptada y limpia.** ChatGPT
> entregó la v1.5 y pasó la verificación de §D **entera**: **metadiscurso 33 → 11** · **párrafos
> >150 palabras 14 → 2** · 28.418 palabras (en target) · 109 títulos · 21 tablas 16–36 + 6 de
> anexo · **78 ecuaciones** · **cero pérdida verificada** ("et al." 59→59, años citados idénticos
> —el −1 aparente era la fecha del banner de extracción—, `deberá` 28 y `todavía` 7 intactos,
> greps del pase 3 en cero) · **41/41 anclas** · **15/15 cortes de párrafo** · anti-duplicación
> limpio. Cambios controlados (37/22) **aceptados sobre el XML** (0 fusiones con texto — sin el
> patrón del defecto del pase 3); los 27 comentarios siguen resueltos e intactos. Respaldo:
> `archivado/…v1.5 (entrega GPT, cambios sin aceptar).docx`; v1.4 y el pase 4 → `archivado/` (acta
> en su banner). `90f` re-extraído de la v1.5 · generador y `INSTRUCCIONES-PROJECT` a v1.5 · kit
> OK, 62 tests. **LA ETAPA 2 QUEDA CERRADA: v1.5 con los cuatro pases** (contenido+formato ·
> verificación · desduplicación+anexos · legibilidad). Del usuario: **sólo git**. Handoffs vivos:
> §17.3 v1.5 (E3-42 + 3 sitios de voz D-P3-9 + 11 metadiscursos + 2 párrafos gordos) · Etapa 1:
> 7 sitios D-P3-9 (colega) · integración (anexos→§19.3/19.4, hueco tablas 37–38, métricas del
> anexo a ecuación) · D-E1-11 AAIP.
>
> 🔎 **2026-08-31 — ANÁLISIS DE EXTENSIÓN de la v1.5 (151 páginas): cuánto más se puede podar y a
> qué costo.** A pedido del usuario ("¿por qué no recortar más?"):
> [`desarrollando/archivado/analisis-poda-17-1.md`](desarrollando/archivado/analisis-poda-17-1.md) — peso medido por
> sección (17.1.5 = 35 % · 17.1.7 = 26 % · 17.1.6 = 16 %), veredicto 🟢/🟡/🔴 por bloque y menú de
> poda en tres niveles: **PODA-A segura ~1.200 w** (auto-presentación 17.1.1/17.1.3, nota de 261 w
> de la Tabla 21, no-aplicación duplicada del framework) · **PODA-B a criterio ~1.300 w**
> (re-argumentación bibliográfica de 17.1.5.4 que YA vive en §15/§16 — Du 5×, Bianchi 8× dentro
> del capítulo) · **PODA-C ~330 w** (exige reabrir D-E2-6/MOT — recomendado NO). **Total máximo
> responsable: ~2.700 w + 2–3 tablas = 151 → ~136 páginas (−10 %)**; el resto de las páginas es
> estructural (APA doble espacio + 27 tablas + protocolo completo; §15+§16 pesa 100 pág con
> 22,9k w). Acumulado ya podado: 32.669 → 26.376 (−19 %). Decisiones para abrir el pase 5:
> D-P5-1…4 al final del análisis. **Sin firmar, no se aplica nada.**
>
> ✎ **2026-08-31 (noche) — D-P5 FIRMADAS Y PASE 5 ESCRITO (NO aplicado).** El usuario autorizó
> "limpieza **sin perder defensa de plataforma**" → **PODA-A + PODA-B, PODA-C descartada** (MOT
> intacto, D-E2-6 no se reabre). Instrumento:
> [`desarrollando/correcciones-etapa-2-pase-5.md`](desarrollando/archivado/correcciones-etapa-2-pase-5.md)
> (**E2-56…E2-67**, base v1.5 → **v1.6**; 52/52 anclas verificadas; reglas duras: cero pérdida de
> defensa, **cero bajas de referencias**, comentarios intactos; cae la Tabla 16 con renumeración
> 16–35; targets: ~26,6–27,0k w · 106 títulos · 20+6 tablas · 76 ecuaciones). Y el registro de
> **por qué no se poda más**:
> [`desarrollando/archivado/justificacion-extension-17-1.md`](desarrollando/archivado/justificacion-extension-17-1.md)
> — historia de los 5 pases (−24 % acumulado), el piso honesto (~140 pág = APA doble espacio + 26
> tablas + protocolo completo/pre-registro), y la tabla de recortes descartados con su costo
> (~3.100 w que se pagan en defensa). Al Project: re-subir `00-contexto-base.md` +
> `01-etapa-2-activa.md`; al chat: el `.docx` v1.5 + el pase 5.
>
> ✅ **2026-08-31 (cierre definitivo) — PASE 5 APLICADO: §17.1 v1.6 VIGENTE Y DEFINITIVA, aceptada
> y limpia. LA ETAPA 2 CIERRA CON CINCO PASES.** Verificación de §D entera: **26.632 palabras**
> (target 26,6–27,0k) · **106 títulos** · **20 tablas 16–35 contiguas** + 6 de anexo, sin refs
> huérfanas · **76 ecuaciones** (las 2 muertes declaradas) · **cero bajas de referencias** (cotejo
> por apellido 32→32; el cotejo automático inicial marcó 3 falsas bajas por citas dentro de listas
> con punto y coma — trampa de regex anotada) · pre-registro intacto (MOT17, OVT-B, kappa,
> bootstrap, templates, español) · 37/37 anclas · anti-duplicación limpio · sin copias con
> numeración vieja · `deberá` 26, `todavía` 7. Cambios (44/114) aceptados sobre el XML (la Tabla
> 16 salió entera: 5 filas + cascarón; 0 fusiones con texto); 27 comentarios resueltos intactos.
> Respaldo: `archivado/…v1.6 (entrega GPT, cambios sin aceptar).docx`; v1.5 y pase 5 →
> `archivado/` (acta en el banner). `90f` re-extraído · generador/`INSTRUCCIONES` a v1.6 · kit OK,
> 62 tests. **Acumulado de la jornada: 32.669 (v1.1) → 26.632 (v1.6) = −18,5 % con los anexos
> ADENTRO del documento; el desarrollo solo: −24 % · −13 títulos · −8 tablas.** La extensión final
> (~140 pág) queda justificada por escrito en
> [`desarrollando/archivado/justificacion-extension-17-1.md`](desarrollando/archivado/justificacion-extension-17-1.md).
> **Del usuario: sólo git.** Handoffs vivos (sin cambios): §17.3 v1.5 · Etapa 1 (colega) ·
> integración (anexos→§19.3/19.4 · hueco global de tablas ahora **36–38** · métricas del anexo a
> ecuación) · D-E1-11 AAIP.

> 🔎 **2026-09-01 — LA ETAPA 2 SE REABRE CON UN PASE 6 (escrito, NO aplicado): desacople
> normativo de §17.1.** Origen: el colega entregó la **Etapa 1 v1.1** (§15/§16 con poda fuerte
> de 16.2/16.6 y 10 comentarios C0–C9) y el equipo **firmó el criterio editorial** — la normativa
> es marco conceptual, nunca especificación: prohibido derivar taxonomías, severidades o ventanas
> de artículos legales. La doble auditoría (Claude + GPT, cruzada y verificada sitio por sitio)
> encontró que **§17.1 v1.6 es la única sección en falta**: severidades fundadas en artículos del
> Decreto 911/96 (17.1.5.3.2), citas de artículos en las 6 filas de la Tabla 21, dos referencias
> colgantes a la "taxonomía normativa" que ya no existe en §16.2, criterio C2 "Cobertura
> normativa", y recaudos de las Tablas 18/19 con desarrollo jurídico (§17.3/§17.4/§17.5 limpias).
> El pase: [`desarrollando/correcciones-etapa-2-pase-6.md`](desarrollando/archivado/correcciones-etapa-2-pase-6.md)
> — **E2-68…E2-88** (15 obligatorios + 4 opcionales) y **D-P6-1…3** (una sola cita legal directa,
> en 17.1.10.1 · severidad = categoría metodológica de prioridad temporal · baja de la Res.
> SRT 299/2011 del informe). **32/32 anclas verificadas** con ocurrencia única; compuerta
> automatizada `docs/herramientas/verificar_anclas_pase6.py` (`--pre` verde sobre la v1.6;
> `--post` valida la futura v1.7: anclas en cero + 76 ecuaciones + 27 comentarios + marcador
> AAIP intacto + única cita a Disposición 10/2015). No toca cifras, ecuaciones, pre-registro ni
> los catálogos CR/PR. ⚠ El estado "Etapa 1 CERRADA con v1.0" de la tabla de abajo quedó
> **superado por la v1.1 en revisión** (crítica entregada, comentarios pendientes de decisión
> del usuario); la tabla se actualiza cuando cierre ese ciclo.

> ✅ **2026-09-01 (misma jornada) — PASE 6 APLICADO: §17.1 v1.7 VIGENTE, limpia. LA ETAPA 2
> QUEDA CON SEIS PASES.** Los **35 reemplazos** (19 ítems E2-68…E2-88 con opcionales, más
> E2-75c agregado en aplicación: el residuo de "categoría normativa" en 17.1.2.2 que detectó
> la compuerta — la fila 17.1.2.2 del veredicto de GPT era correcta, existían ambos sitios) se
> aplicaron sobre el XML con `docs/herramientas/aplicar_pase6.py` (edición byte a byte solo de
> los `<w:t>` que solapan cada ancla, conteos con aborto). Compuerta `--post` **verde**:
> greps prohibidos en 0 · guardrails presentes · **76 ecuaciones · 27 comentarios resueltos ·
> 0 marcas · 1 sola cita a Disposición 10/2015 (17.1.10.1) · marcador AAIP intacto · tablas
> 16–35**. Diff íntegro atribuido: 22 hunks = exactamente los 35 reemplazos, cero colateral;
> **26.632 → 26.440 palabras** (mismo instrumento). `90f` re-extraído de la v1.7 ·
> generador/`INSTRUCCIONES` a v1.7 · kit regenerado, `--check` OK, 62 tests + 51 subtests ·
> v1.6 y el pase 6 (acta en su banner) → `archivado/` · ✎ al acta del pase 5 ("v1.6
> definitiva" quedó superada). Baja bibliográfica pendiente de la integración: Res. SRT
> 299/2011 (D-P6-3). **Del usuario: sólo git.**
>
> ✅ **2026-09-01 (más tarde) — D-E1-11 CERRADA POR EL USUARIO: el informe NO adjudica la
> inscripción ante la AAIP** (converge con el comentario C9 de la Etapa 1 v1.1). Se borran
> el párrafo indeciso y los dos marcadores `[[PENDIENTE]]`; las salvaguardas de §16.6 son
> el recaudo documentado y la respuesta sobre la inscripción se prepara para la defensa.
> **Lado §17.1 APLICADO: v1.7 → v1.8** (borrados la oración de anclaje de §17.1.10.1 y el
> marcador espejo; compuerta verde: AAIP 0 · PENDIENTE 0 · 76 ecuaciones · 27 comentarios ·
> 0 marcas · Disposición 10/2015 conservada · verificador OK · 26.440 → **26.380 palabras**;
> diff = exactamente los dos sitios). Lado §16: **viaja con el pase de la Etapa 1**
> (v1.1 → v1.2) — en la v1.1 el borrado arrastra el rango del comentario C9 y da de baja la
> cita *AAIP, s. f.-b* (re-letrado de la s. f.-a en la integración); en la v1.0 el único
> sitio es el marcador de §16.6.2.2. En §17.4 no hay nada que tocar (verificado). `90f`
> re-extraído de la v1.8 · generador/`INSTRUCCIONES`/kit a v1.8 (`--check` OK, 62 tests) ·
> v1.7 → `archivado/`. Constancia y anclas:
> [`desarrollando/archivado/cierre-d-e1-11-aaip.md`](desarrollando/archivado/cierre-d-e1-11-aaip.md).
> ⚠ `verificar_anclas_pase6.py --post` queda histórico (sus invariantes "1 PENDIENTE" y el
> ancla AAIP describen la v1.7). **Del usuario: sólo git.**
>
> 🔎 **2026-09-02 — LA ETAPA 2 SE REABRE COMO REESTRUCTURACIÓN (GPT + validación): §17.1.2,
> §17.1.4 y §17.1.5 pasan de fragmentación a narrativa.** El usuario trajo una copia
> reestructurada por GPT (§17.1.2 → una subsección · §17.1.4 → dos) que **es un fork de la v1.7,
> no de la v1.8**: sin D-E1-11, **sin 26 de los 27 comentarios resueltos**, sin las Tablas 18/19
> (hueco de numeración), con un párrafo de cuerpo en estilo Heading 3 (§17.1.4.2) y tres celdas
> vaciadas en la Tabla C.3. La propuesta de GPT para §17.1.5 (21 → 4 subsecciones) se **validó
> entera** contra el `.docx`, §15/16, §17.3–17.5, el pattern set `cr01_cr02_v2` y las actas de
> los pases 3–6: estructura y diagnóstico correctos, **cuatro afirmaciones falsas o vencidas**
> (la corrección severidad↔§16.2 ya la hizo el pase 6 · §15/§16 NO citan FG-OVD/OVDEval/templates,
> remitir allí sería falso · §17.3 v1.4 ya no remite a §17.1.5.x · "composición del vocabulario
> activo" ya nacía en .4.2) y nueve huecos:
> [`desarrollando/archivado/validacion-reestructuracion-17-1-5.md`](desarrollando/archivado/validacion-reestructuracion-17-1-5.md).
> **Aplicado sobre la rama de GPT, por decisión del usuario:** (1) **v1.9** = copia de GPT +
> D-E1-11 (mismos dos sitios que la v1.8; §17.1.10.1 idéntico a la v1.8; 24.851 w, 0 marcadores);
> (2) **v1.10** = v1.9 + §17.1.5 reestructurada en cuatro subsecciones con las correcciones de la
> validación (doctrina de severidad del pase 6 literal · ancla FG-OVD/OVDEval conservada ·
> huecos de símbolos de .3.2/.3.3 restituidos como texto · motor sin nombrar estados · Tablas
> 20/21, notas y los 4 saltos a página apaisada intactos · 4 referencias cruzadas actualizadas ·
> **caen Mazor 2021 y Kim 2024**, reversibles): **21.779 w · 83 títulos · 76 ecuaciones ·
> §17.1.5 7.351 → 4.421 w de prosa (−40 %) · 0 dos puntos y 0 punto y coma en la prosa nueva**
> · verificador OK; acta en §G de la validación. **Archivado** (con nombres desambiguados): la
> copia de GPT como *v1.7 (base reestructurada por GPT, sin D-E1-11)*, la **v1.8** como *fuente
> de recuperación* (27 comentarios, §17.1.2/17.1.4 completas), §15/16 v1.0 y
> `analisis-poda-17-1.md`; enlaces a `archivado/` reparados (0 rotos en `entregable/`).
> **Vigentes en `desarrollando/`: §17.1 v1.9 (base) y v1.10 (a aceptar), §17.3 v1.4, §17.4 v1.6,
> §17.5 v1.3, §15/16 v1.1.** ⚠ La cadena derivada **sigue a v1.8** (`90f`, kit, generador con la
> nota D-E2-2 → §17.1.5.4.2, hoy §17.1.5.3): no se re-extrae hasta resolver A-1…A-4 de la rama de
> GPT (comentarios, Tablas 18/19, §17.1.4). **Del usuario: aceptar la v1.10 (→ v1.9 a
> `archivado/`), decidir A-1…A-4, git.**

> ✅ **2026-09-03 — LA ETAPA 2 CERRÓ: §17.1 v1.15, aceptada y limpia.** El usuario reestructuró
> §17.1.6 (19 → 5 títulos) y §17.1.7 (28 → 6) en la **v1.11**, con 76 → 4 ecuaciones. El relevamiento
> exhaustivo de esa versión ([`archivado/relevamiento-17-1-v1-11.md`](desarrollando/archivado/relevamiento-17-1-v1-11.md),
> §A a §L) confirmó la dirección y encontró tres pérdidas conceptuales y cinco defectos mecánicos;
> se repararon como sugerencias en las **v1.12 → v1.14** (niveles de compromiso obligatorio /
> deseable / conceptual · modelo de presupuesto con notación propia `B`/`W`, sin reusar
> `t_alert-system` en una suma · Anexo D citado y su fila G2A alineada al *dequeue* · Tabla 30
> "Máximo orientativo" · referencia colgante 17.1.4.4 → 17.1.4.2). **La contra-evaluación de GPT se
> cotejó una por una** (§I): tres criterios editoriales suyos se adoptaron y **cuatro premisas
> resultaron falsas o vencidas** — la más grave, pedir que volviera el marcador AAIP a §17.1.11.1,
> que **D-E1-11 había borrado el 09-01**. Después, con el mismo criterio, se reescribió el tramo
> final: **§17.1.8 a §17.1.11 quedaron sin subsecciones** (1.390 → 1.059 palabras, **0 dos puntos y
> 0 punto y coma**), se cerraron los Anexos C y D (nota C.1 sin *"Fuente:"*, **C.2 dejó de estar
> huérfana** — la cita §17.1.4.2 —, nota C.3 con remisiones vivas) y se resolvieron los **mecánicos
> de §17.1.6** con el registro del repo de datasets (Roboflow v27 y v1, SH17 CC BY-NC-SA 4.0, fila
> de deduplicación completa) más las dos referencias primarias verificadas en arXiv
> (**Milan et al., 2016** para MOT17 y **Liang y Han, 2024** para OVT-B). Acta del pase:
> [`archivado/analisis-17-1-8-anexos.md`](desarrollando/archivado/analisis-17-1-8-anexos.md) §8.
>
> **Contra la v1.8** (la del pase 6): **23.906 → 15.464 palabras (−35,3 %) · 109 → 37 títulos
> (cero de nivel 5) · 26 → 22 tablas · 76 → 4 ecuaciones · cero bajas de referencias** y dos altas.
> `verificar_entregable.py` OK, sin marcadores. Queda **un comentario abierto** del colega en
> §17.1.6, que la v1.15 responde con el registro. **⚠ La numeración de subsecciones cambió**: toda
> acta anterior cita números que ya no existen — traducción en
> [`desarrollando/mapa-secciones-17-1-v1-15.md`](desarrollando/archivado/mapa-secciones-17-1-v1-15.md), que
> además lleva el estado de las tablas (huecos 18/19 y 31/32) y los siete residuales de integración.
> **Cadena derivada al día:** `90f` re-extraído de la v1.15, `90g` con banner histórico, generador y
> kit regenerados (`--check` OK, 62 tests). **Archivado:** v1.9 a v1.15-sin-aceptar y las cinco
> constancias del ciclo. **Vigentes en `desarrollando/`: §17.1 v1.15, §17.3 v1.4, §17.4 v1.6,
> §17.5 v1.3, §15/16 v1.1.** Del usuario: **git**.

> ✅ **2026-09-03 (misma jornada, más tarde) — PASE 4 DE LA ETAPA 3 APLICADO: §17.3 v1.5 → v1.6,
> con sugerencias sin aceptar.** El pedido fue hacer con §17.3 lo mismo que se hizo con §17.1:
> bajar la verborragia, consolidar contra lo que las Etapas 1 y 2 ya fijaron, eliminar los títulos
> de nivel 5 y sacar los dos puntos y los punto y coma. Diagnóstico primero
> ([`desarrollando/archivado/analisis-17-3-etapa-3.md`](desarrollando/archivado/analisis-17-3-etapa-3.md), 13 decisiones
> D-A…D-M), aplicación después con las recomendaciones firmadas.
>
> **Hallazgo de entrada: la v1.5 era byte a byte la v1.4** (mismo sha256), así que el handoff
> registrado desde el pase 4 de la Etapa 2 —**E3-42**, 3 sitios de voz D-P3-9, 11 metadiscursos y
> 2 párrafos gordos— **nunca se había aplicado**. Este pase lo absorbe.
>
> **Resultado (vista aceptada):** prosa **13.174 → 10.075 (−24 %)** · títulos **61 → 30 (−51 %)**
> con **cero de nivel 5** (eran 4) · tablas **17 → 14**, renumeradas **39–52** · figuras **6 → 4**,
> renumeradas 4.1–4.4 · dos puntos **73 → 0** · punto y coma **86 → 0** · rayas **32 → 2** ·
> «debe/deben» **87 → 9** · metadiscurso **10 → 0** · «deberá» **3 → 0** · párrafos de más de 150
> palabras **2 → 0** · pares de oraciones repetidas entre secciones **16 → 3** (los tres son falsos
> positivos). **Cada tabla y cada figura se cita ahora exactamente una vez**; en la v1.5 once tablas
> y las seis figuras no se citaban.
>
> **Lo que se consolidó contra las etapas anteriores:** las cinco citas de prompts pasan a una
> remisión a §17.1.5.3 y §17.3 queda **sin bibliografía propia**; la Tabla 43 pierde las ocho filas
> que duplicaban el Anexo C; la Tabla 44 deja de repetir la Tabla 21; se eliminan las Tablas 47
> (hechos persistibles), 49 (diccionario de métricas) y 51 (DBE/EBE), las tres duplicadas de §17.1.
> Se corrigió la **remisión rota a «§17.1.4.4»**, que en la v1.15 es **§17.1.4.2**, y la afirmación
> incompleta sobre el orden de arranque, que pasa a enunciar la regla del consumidor antes que el
> productor. **Los 7 comentarios se conservan con su ancla** (dos re-anclados) y ninguno se marca
> resuelto: eso lo decide el usuario.
>
> Compuerta **`herramientas/verificar_v16_17_3.py` verde: 0 fallas, 0 avisos**, con la verificación
> de que **rechazar todos los cambios devuelve exactamente la v1.5**. Acta:
> [`desarrollando/correcciones-etapa-3-pase-4.md`](desarrollando/archivado/correcciones-etapa-3-pase-4.md)
> (**E3-43…E3-62**). ⚠ **La numeración de subsecciones cambió** — traducción obligatoria en
> [`desarrollando/mapa-secciones-17-3-v1-6.md`](desarrollando/archivado/mapa-secciones-17-3-v1-6.md).
> **Del usuario: aceptar la v1.6** (y git). Al aceptar: re-extraer `90` y regenerar el kit.
> Handoff nuevo **E4-31** hacia §17.4 (detalle operativo del ledger).

> ✅ **2026-09-04 — LA ETAPA 3 CERRÓ: el usuario aceptó la v1.6 de §17.3** («con sugerencias resueltas
> y unos mini ajustes»). Documento vigente `desarrollando/…_17.3_…_v1.6.docx`: 14.220 palabras, 30
> títulos, 0 marcas, `verificar_entregable.py` OK, **4 comentarios abiertos** (dos del colega en 17.3.2 y
> 17.3.6.2, y dos respuestas ancladas). Regla D-C aplicada: **`90` re-extraído de la v1.6** y kit
> regenerado; la v1.5 y la v1.6 con sugerencias pasaron a `archivado/`.
>
> 🔎 **Misma jornada — ANÁLISIS EXHAUSTIVO DE §17.4 v1.6 Y §17.5 v1.3, previo al pase de las Etapas 4 y
> 5** (mismo encargo que en las Etapas 1–3; nada aplicado todavía, el usuario decide cómo seguir):
> [`desarrollando/archivado/analisis-17-4-17-5-etapas-4-5.md`](desarrollando/archivado/analisis-17-4-17-5-etapas-4-5.md),
> con **15 decisiones D-A…D-O**. Lo que cambia la lectura de «§17.4 y §17.5 cerradas»: **§17.4.4 afirma
> un orden de arranque falso** (distribución → control → medios; el real es control → distribución →
> medios con la garantía del *handshake*, H2-01) y §17.4.5 cita **17.3.8.4, que ya no existe**; la
> Figura 4.7 embebida **no es la FIG-A producida**; **la Tabla 66 perdió una celda** en la exportación
> del 08-27 («3 alertas: ≥ 7,1 s»); cuatro handoffs registrados no están en los textos (H2-01, H2-02,
> E4-31, AJ-5.14); **L1–L8 se citan en §17.5.8 y no se declaran en ninguna sección**, y §17.5.8 tiene
> el comentario «borrar». En estilo: §17.4 tiene 27,4 palabras por oración, 54 dos puntos y nueve
> párrafos de más de 150 palabras; §17.5 repite «34 episodios evaluables» once veces. Propuesta:
> §17.4 a 8 secciones (−27 % de prosa, Tabla 60 a prosa por pedido del usuario) y §17.5 a 7 (sin la
> síntesis, con AJ-5.14 y L1–L8 adentro). Los **8 comentarios** (7 + 1) se informan y viajan.
> **Del usuario: decidir D-A…D-O** (y git).
>
> ✅ **2026-09-04 (misma jornada, más tarde) — PASE 4 DE LAS ETAPAS 4 Y 5 APLICADO: §17.4 v1.6 → v1.7
> y §17.5 v1.3 → v1.4, con sugerencias sin aceptar.** El usuario firmó las quince decisiones, las
> quince en la recomendación, y las cuatro que se preguntaron una por una quedaron así: **Opción A**
> para §17.4 (ocho secciones con renumeración interna), **las ocho limitaciones cierran §17.5.7**,
> **el esfuerzo de anotación se afirma sin inventar horas** y **los comentarios quedan abiertos con
> su ancla**.
>
> **§17.4:** 16 → 9 títulos y **cero de nivel 4**; prosa y tablas 6.375 → 5.493 palabras (−13,8 %);
> 6 → 5 tablas, renumeradas 56–60; dos puntos **55 → 1**, punto y coma **29 → 0**, rayas **28 → 0**;
> párrafos de más de 150 palabras **9 → 0** y oraciones de más de 45 **27 → 0**. Tres fusiones de
> secciones, la Tabla 60 a prosa por estatuto (pedido del usuario) y la figura renumerada a 4.5 y
> citada. **Aterrizaron los tres handoffs abiertos:** el orden de arranque real, que la v1.6
> afirmaba invertido y en tres versiones incompatibles; las 2.946 imágenes de ajuste con su causa;
> y el detalle operativo del ledger que §17.3 remite a este capítulo.
>
> **§17.5:** 9 → 8 títulos, 6 → 5 tablas renumeradas 61–65, dos puntos **15 → 0** y punto y coma
> **16 → 0**, **sin recalcular ninguna de las 185 cifras verificadas**. Suma lo que faltaba: el
> costo medido del vocabulario activo y su sub-experimento no ejecutado, y **las ocho limitaciones,
> que el informe citaba y ninguna sección declaraba**. Se restauró la celda que la exportación del
> 08-27 había perdido en la tabla de tiempo real.
>
> **§17.3 v1.7** se entrega con **un solo cambio controlado**: la remisión «sección 17.4.6» pasa a
> 17.4.4, porque la renumeración de §17.4 la dejaría rota.
>
> Compuerta `herramientas/verificar_pase_17_4_17_5.py` **verde, 0 fallas**, con la propiedad que
> hace segura la entrega: **rechazar todos los cambios devuelve exactamente el documento de
> partida**, verificado en los tres. Actas
> [`correcciones-etapa-4-pase-4.md`](desarrollando/archivado/correcciones-etapa-4-pase-4.md) y
> [`correcciones-etapa-5-pase-4.md`](desarrollando/archivado/correcciones-etapa-5-pase-4.md). ⚠ **La
> numeración de subsecciones de §17.4 cambió** — traducción obligatoria en
> [`mapa-secciones-17-4-v1-7.md`](desarrollando/archivado/mapa-secciones-17-4-v1-7.md). **Del usuario:**
> aceptar las dos entregas con sugerencias, reemplazar la imagen de la Figura 4.5 por la producida,
> pegar las tres figuras de §17.5, y git. Al aceptar: re-extraer `90b` y `90c` y regenerar el kit.
>
> ✎ **Misma jornada, cierre — §17.3 no necesita otra ronda de aceptación.** Por indicación del
> usuario, el token de la remisión se aplicó **en limpio** sobre el documento que él había pasado sin
> marcas, y el vigente pasa a ser **`…_17.3_…_v1.7.docx`**: mismo texto que la v1.6 con la misma
> longitud, sin cambios controlados, con los cuatro comentarios, los 21 saltos de sección y las
> cuatro figuras intactos. `90-etapa3-texto-extraido.md` se re-extrajo de esa v1.7 y el kit se
> regeneró. La v1.6 y la entrega con sugerencias quedaron en `archivado/`.

## El texto extraído

| Archivo | Qué contiene | Etapa del plan |
|---|---|---|
| `96a-informe-v11-frontmatter-intro-objetivos-plan.md` | frontmatter, §11 Glosario, §12 Introducción, §13 Objetivos, §14 Plan de trabajo (**§14.2 define las etapas**) | transversal |
| **`90d-etapa1-texto-extraido.md`** | **§15 + §16 (Etapa 1, CERRADA 2026-08-28)** — texto base FINAL, extraído de `desarrollando/E-OVRT-VDP_Secciones_15_y_16_…_v1.0.docx`, cinco pases aplicados | **1** ✅ |
| ~~`96c-informe-v11-estado-del-arte.md`~~ | **ARCHIVADO 2026-09-07** en [`archivado/`](archivado/00-que-hay-aca.md): foto del informe v1.1, superada | — |
| ~~`96d-informe-v11-marco-teorico.md`~~ | **ARCHIVADO 2026-09-07** en [`archivado/`](archivado/00-que-hay-aca.md): foto del informe v1.1, superada | — |
| **`90f-etapa2-texto-extraido.md`** | **§17.1 Consolidación Metodológica (Etapa 2, CERRADA 2026-09-03)** — texto base VIGENTE, re-extraído el 2026-09-07 de `desarrollando/E-OVRT-VDP_Seccion_17.1_Consolidacion_Metodologica_v1.16.docx` (texto idéntico a la v1.15, sin comentarios; **22 tablas**, antes 19 por el defecto `w:sdt` del extractor; 4 ecuaciones). Los Anexos C/D viven al final del `.docx` y la extracción los incluye. ⚠ numeración de subsecciones: [`mapa-secciones-17-1-v1-15.md`](desarrollando/archivado/mapa-secciones-17-1-v1-15.md) | **2** ✅ |
| ~~`96b-informe-v11-17-1-consolidacion-metodologica.md`~~ | **ARCHIVADO 2026-09-07** en [`archivado/`](archivado/00-que-hay-aca.md): foto del informe v1.1, superada | — |
| **`90-etapa3-texto-extraido.md`** | **§17.3 Diseño arquitectónico (Etapa 3, cerrada 2026-09-04; edición del usuario del 09-06 en revisión)** — texto base VIGENTE, re-extraído el 2026-09-07 de `desarrollando/E-OVRT-VDP_Seccion_17.3_Diseno_Arquitectonico_v1.8.docx` (14.126 palabras, 30 títulos, 14 tablas 39–52, 4 figuras, 0 comentarios). ⚠ numeración: [`mapa-secciones-17-3-v1-6.md`](desarrollando/archivado/mapa-secciones-17-3-v1-6.md), válido para la v1.8. Retoques pendientes: lectura transversal 09-07 (E3-1…E3-3) | **3** ✅ |
| **`90b-etapa4-texto-extraido.md`** | **§17.4 Implementación** — re-extraído el 2026-09-07 de `desarrollando/E-OVRT-VDP_Seccion_17.4_Implementacion_v1.8.docx` (pase 4 aceptado y editado por el usuario el 09-06; 6.067 palabras con tablas, 9 títulos, 5 tablas 56–60, 1 figura, 6 comentarios). ⚠ numeración: [`mapa-secciones-17-4-v1-7.md`](desarrollando/archivado/mapa-secciones-17-4-v1-7.md). **NO cierra todavía** (Figura 4.5 rota, Tablas 57/59 sin llamada): lectura transversal 09-07 | **4** 🔄 |
| **`90c-etapa5-texto-extraido.md`** | **§17.5 Evaluación y validación** — re-extraído el 2026-09-07 de `desarrollando/E-OVRT-VDP_Seccion_17.5_Evaluacion_y_Validacion_v1.5.docx` (pase 4 aceptado y editado por el usuario el 09-06; 3.391 palabras con tablas, 8 títulos, 5 tablas 61–65, 0 figuras). La celda «3 alertas: ≥ 7,1 s» de la Tabla 64 **siempre estuvo** (era el extractor). **NO cierra todavía** (ocho limitaciones borradas, 0 figuras, «23 episodios»): lectura transversal 09-07 | **5** 🔄 |
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
