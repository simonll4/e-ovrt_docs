# Lo que resta del informe — foto al 2026-09-18 (quinta pasada: el informe está completo)

> **Para qué existe este documento.** Después del 08-31 (Etapa 2 con cinco pases), del 09-01
> (Etapa 1 v1.1 del colega + pase 6 de desacople normativo), del **09-03 (§17.1 reestructurada y
> cerrada en la v1.15; §17.3 consolidada en la v1.6)** y del **09-04 (§17.3 v1.6 aceptada; análisis
> exhaustivo de §17.4/§17.5 escrito)**, el estado real quedó repartido entre varios banners. Esta es la
> lista única de lo que falta, con dueño y bloqueo, verificada contra los archivos —no contra la
> memoria— el 2026-09-04.
>
> **Qué NO es:** no reemplaza al tablero
> [`00-el-informe-hoy.md`](00-el-informe-hoy.md) (que narra la historia por jornada) ni al
> acta [`operacion/128`](../../operacion/128-acta-cierre-programa-experimental.md) (que
> cerró el programa experimental). Es el índice de pendientes; cuando un ítem cierra, se
> tacha acá y su constancia vive en el banner que corresponda.

---

## 0. Dónde estamos en una línea

> ✎ **2026-09-18 — EL INFORME ESTÁ COMPLETO: `desarrollando/E-OVRT-VDP_Informe_Final_2026-09-16_v0.1.docx`.**
> Portada, §2–§19, Anexos A–F y Referencias; 82k palabras; 73 tablas; 8 figuras; 0 comentarios, 0
> cambios rastreados. Leído de punta a punta; foto en `90-informe-final-2026-09-16-v0.1-texto-extraido.md`.
> **Todos los ítems de las pasadas anteriores (§1–§8 de abajo) quedan cerrados o absorbidos por la
> integración**: §17.6/§18/§19 redactadas; §11–§14 con Resumen/Abstract escritos; costos integrados
> en §14.4 y §17.2; C1 cerrado en el Anexo F (lista de reproducción citada, consultada el 15-sep).
>
> **Lo que RESTA es formal, en la v0.1** (verificado contra el texto extraído el 09-18):
>
> | # | Pendiente | Dónde | Dueño |
> |---|---|---|---|
> | P-1 | Placeholders «[se completará más adelante]» en §2 Hoja de aceptación, §3 Dedicatoria y §4 Agradecimientos | front matter | usuario |
> | P-2 | «Tabla de contenido» sin el número 8 (§9 y §10 sí lo tienen) | §8 | usuario (Google Docs) |
> | P-3 | Numeración de figuras heredada: Figura 1 + Figura 4.1–4.6 | §9, §14.3, §17.3–17.5 | usuario |
> | P-4 | Título «14. Plan De Trabajo De Proyecto Integrador» con mayúsculas en preposiciones | §14 | usuario |
> | P-5 | P-E1-05 y P-E1-07 ausentes de §16.7.3 sin nota que diga qué eran | §16.7.3 | usuario |
> | P-6 | Estatuto de la distribución inconsistente: §12.4 «la plataforma incluye», Tabla 32 «capacidad opcional», §17.4.1 «módulo desacoplado, implementado» | §12.4 / §17.3.2 / §17.4.1 | usuario |
> | P-7 | Previsualización habilitada por defecto (17.4.7 la declara) no figura entre las 8 limitaciones de 17.5.7 ni en 18.6; 18.5 dice «CHV se excluyó» sin la desviación de `construction_site_safety` que 17.4.7 sí declara | §17.5.7 / §18.5 / §18.6 | usuario |
> | P-8 | Bibliografía: falta la entrada de **DINO** (15.2.1 cita «H. Zhang et al., 2022», que en la lista es GLIPv2); «Axis Communications AB, s. f.» (17.1.7.5), «Luxonis s. f.-a/-b», «AAIP s. f.-a», NVIDIA «s. f.-c…f» sin entrada; ~8 entradas no citadas (ISO 45001, Grounded-SAM-2, TET, Li X. 2022, DetCLIP, CoCoOp, Zou X., Zou Z.); erratas «Zhang, Y.-Q..», «Latency y Latency», entrada de Iorga truncada | Referencias | usuario |
> | P-9 | Los ítems de fondo de la revisión externa de la v0.6 (redundancia §15↔§16, §17.1↔§17.3↔§17.4, disclaimers repetidos, tono «no constituye» ×32, notación AP@0,5/AP50, fps/FPS, sólo ×84 / solo ×12; Etapa 5 del plan promete una comparación con el estado del arte que no se hizo y nadie explica) — decisión del usuario. Revisión: `desarrollando/revision-informe-final-v0.6-2026-09-15.md`; **verificación mecánica ítem por ítem contra la v0.1**: `desarrollando/verificacion-revision-v0.6-vs-v0.1-2026-09-18.md` (RESUELTO: Resumen/Abstract, `[[PENDIENTE]]` del Anexo F, 14.4 como «previsto», cronología del GT; ABIERTO: casi todo lo demás) | todo el documento | usuario |
> | P-10 | 14 tablas que sólo existen como caption, sin ninguna llamada en prosa: 1, 12, 13, 18, 20, 21, 31 y B.1–B.7 (verificado 1 a 1) | §11, §17.1, §17.2, Anexo B | usuario |
> | **P-11** | ⚠ **SE PERDIÓ EN LA INTEGRACIÓN: el informe no cita el repositorio público del proyecto.** `https://github.com/simonll4/e-ovrt-vdp` no aparece en ninguna parte de la v0.1 (ni en el texto, ni entre los 157 hipervínculos del `.docx`, ni en Referencias), pero **sí estaba en la Etapa 6 desde la v1.3 (09-12), y sobrevivió en la v1.4 y la v1.5**. Ver el detalle abajo | §17.6.1 + Referencias | usuario |
>
> ### P-11 en detalle — la única referencia externa propia del informe
>
> **Qué falta.** El párrafo 1 de §17.6.1 termina hoy en «…la persistencia de sus resultados.». Las tres
> últimas versiones de la Etapa 6 cerraban ese mismo párrafo con una oración más, que la integración no
> trasladó (texto exacto de la v1.5, verificado en `desarrollando/archivado/`):
>
> > Los cinco repositorios de código son públicos y se reúnen, junto con los resultados, sus artefactos y
> > las figuras, en el repositorio público de documentación del proyecto,
> > https://github.com/simonll4/e-ovrt-vdp (Carrizo, Guillaumet y Llamosas, 2026), que es la vía de acceso
> > a todo el material que este informe identifica.
>
> **Falta también su entrada en Referencias**, que nunca llegó a existir en el `.docx` de sección porque la
> lista es global del maestro; el acta `desarrollando/archivado/pase-etapa-6-v1.3-2026-09-12.md` §3 la dejó
> redactada para pegarla en su lugar alfabético al integrar:
>
> > Carrizo, M. L., Guillaumet, G. A., y Llamosas, S. (2026). *E-OVRT-VDP: Plataforma experimental de
> > detección open-vocabulary en video en tiempo real para monitoreo asistivo de riesgos en construcción*
> > [Repositorio de documentación]. GitHub. https://github.com/simonll4/e-ovrt-vdp
>
> **Por qué importa más que los otros pendientes.** No es una errata de forma: §14.2.6 promete como
> resultado de la Etapa 6 una «entrega académica completa: informe PDF, anexos, **repositorio** y
> presentación», y §17.6.1 describe seis repositorios sin decir dónde están ni que sean públicos. Tal como
> está, el jurado lee que existen y no tiene forma de llegar a ellos, y los Anexos E y F —que delimitan el
> camino de reproducción y las condiciones de acceso— quedan sin punto de entrada. Era además **la única
> referencia externa propia** que la regla de autocontención admite (decisión H01/H05 de la Etapa 6: se
> cita una sola vez, en §17.6.1).
>
> **Antes de reponerlo, una precondición que sigue abierta:** la rama por defecto de `e-ovrt_datasets` y
> `e-ovrt_control-plane` (los dos repos de Pandulc) sigue en `main` de junio, y el paraguas los enlaza por
> nombre de rama. Ver `project_repo_publico_e_ovrt_vdp` en la memoria de Claude.
>
> **Fuera del informe (no lo modifican):** Drive de evidencia (`_evidencia-drive/` + `scripts/armar_evidencia_drive.sh`),
> videos de defensa, build + smoke del compose integral (el informe lo declara **no verificado**, §17.6.4 y Tabla B.3),
> tags/Release del repo público `e-ovrt-vdp`. **Defensa prevista: fines de septiembre de 2026** (§17.2.2, §18.6).
>
> ✎ **2026-09-08 — KIT DE LA ETAPA 6 LISTO PARA CARGAR, y una guía nueva para producir las figuras.**
> Se destrabó la carga: el README mandaba subir un `.docx` de formato que se había archivado el 09-07,
> así que **el paso 3 apuntaba a una ruta vacía y la carga no se podía completar**. Ahora la autoridad
> de formato es el maestro del 09-08, con la variante archivada como alternativa liviana si 12 MB no
> entran. El paquete de la Etapa 6 sumó dos piezas que le faltaban para escribir §19: el **Anexo A y
> el listado de la Etapa 1** (`90e`) y la **auditoría bibliográfica**; su contrato de uso ahora ordena
> **fusionar antes de redactar** el listado. **Se sube: contexto base, paquete de etapa 6, el maestro,
> y la guía de figuras cuando toque.**
> **Guía nueva: [`figuras/GUIA-DE-FIGURAS.md`](../figuras/GUIA-DE-FIGURAS.md)** — un sistema visual
> único para las seis figuras (hoy conviven dos lenguajes distintos), la especificación de cada una
> con sus rótulos exactos, y la regla de pedirlas como **código vectorial y nunca como imagen
> generada**, que deforma los rótulos.
> ⚠ **Al escribirla apareció un error de fondo: la Figura 4.3 dibuja dos transiciones que el sistema
> no hace** (`candidate → inactive` y `resolved → inactive`; verificado contra el motor de patrones,
> nada vuelve nunca a `inactive`), y le faltan el salto directo a `confirmed`, la reapertura desde
> `resolved` y los dos caminos a `resolved`. **El texto de 17.3.6.1 arrastra el mismo error.** §17.3
> está cerrada: **lo decide el usuario**.
>
> ✎ **2026-09-08 — AUDITORÍA BIBLIOGRÁFICA: el listado del maestro quedó desincronizado.** Se cruzaron
> las 242 entradas del listado global contra las citas de las diez piezas vigentes, y se leyó el uso de
> cada cita con cinco auditorías en paralelo. **Hallazgo de raíz: el listado del maestro es anterior a
> las correcciones de la Etapa 1, y le faltan doce entradas que sí están en `90e`** — entre ellas Choi y
> Greer (2024) y Chen y Zou (2025), las dos únicas fuentes que aplican modelos visión-lenguaje a
> seguridad en obra, y Detic, que sostiene una fila entera de la Tabla A.1. Eso explica **once citas que
> hoy no resuelven** y se arregla fusionando, no investigando. Los otros dos frentes: **§17.5 no invoca
> ninguna de las varas que §15 ya tiene relevadas** (0,883 y 0,907 sobre SHEL5K, 0,866 sobre CHV, 0,1024
> de la clase *head* zero-shot) y **§11–§14 no tiene una sola cita**, incluida la premisa que justifica
> el trabajo. **104 de 242 entradas quedaron huérfanas (43 %)**, sobre todo de streaming y de borde, tras
> las podas. **El paper viejo es Kuhn (1955)**, el método húngaro: está huérfano y el algoritmo se nombra
> dos veces sin atribuir. Sin fraude ni transcripción literal: los defectos son de aparato y se corrigen
> en una pasada. Informe completo con el plan por retorno:
> [`desarrollando/auditoria-bibliografica-2026-09-08.md`](desarrollando/archivado/auditoria-bibliografica-2026-09-08.md).
> **Es el documento de ajustes vigente**; el acta de los pases 5 a 5e pasó a `archivado/`.
>
> ✎ **2026-09-08, cierre de la jornada — CUATRO SECCIONES CERRADAS Y EL MAESTRO EN POSICIÓN.** El usuario
> aceptó las tres sugerencias del pase 5e y bajó las cinco renumeradas: §15/16 **v1.4** · §17.1 **v1.21** ·
> §17.3 **v1.12** · §17.4 **v1.15** · §17.5 **«v1.5»** (⚠ el número retrocede y choca con una v1.5 histórica
> distinta; §15/16, §17.3 y §17.5 son byte a byte las anteriores, sólo cambió el nombre). Lo que volvió
> coincide exactamente con la vista aceptada de lo entregado. **CERRADAS §17.1, §17.3, §17.4 y §17.5.**
> El maestro (`desarrollando/E-OVRT-VDP_v1.1_05062026-sin-indice.docx`, export del 09-08) ya está en
> posición para la integración, con un detalle que costaba caro descubrir tarde: **nombra sus estilos de
> título `Ttulo1`…`Ttulo5`**, así que el extractor veía cero títulos y el verificador daba 420 fallas
> falsas. Las tres herramientas ya reconocen las dos familias, con pruebas. Textos base re-extraídos, kit
> regenerado, superadas archivadas, `borradores/` vacía otra vez.
> **Frente activo: la Etapa 6.** Del usuario: cerrar §15/16 con los colegas, C1, y las 15 decisiones
> editoriales del acta §12 que siguen abiertas.
>
> ✎ **2026-09-08 — LAS CINCO SECCIONES ACEPTADAS; EL FRENTE PASA A LA ETAPA 6.** El usuario aceptó en
> Google Docs todo lo de los pases 5/5b/5c/5d y bajó §15/16 v1.3 · §17.1 v1.19 · §17.3 v1.11 · §17.4 v1.13 ·
> §17.5 v1.9. El pase 5e reparó tres defectos del viaje (la última línea de tres bloques de código de §17.4,
> repuesta en limpio; título fantasma y cursiva en 17.1.11, como sugerencias) y resolvió el marcador de
> procedencia del lote con la lista pública que el usuario indicó en un comentario → **§17.4 v1.14 ·
> §17.1 v1.20**. **CERRADAS: §17.1, §17.3, §17.4, §17.5.** §15/16 sigue en revisión del colega (9
> comentarios, 1 sugerencia del pase 5 sin resolver, un «puede puede» que se corrige allá). Textos base
> `90*` re-extraídos; kit regenerado con la **Etapa 6 activa** y los cinco textos cerrados adentro.
> **Lo que queda, en orden:** (1) escribir §17.6, §18 y §19 (Etapa 6; kit listo); (2) la integración al
> maestro (§4 de este documento); (3) la Etapa 0 (§11–§14); (4) del usuario: cerrar la revisión de §15/16,
> aceptar las tres sugerencias del 5e, la ficha por video del lote (C1) y las decisiones editoriales del
> acta §12 que siguen abiertas (Tabla 46, consentimiento del rodaje, matriz de prompts, IC bootstrap,
> métricas sin estado, OAK-D sin nombrar, DELETE en la Tabla 57, «prerregistrado», Figura 4.6 a 6,4 s vs
> 7,3 s, horas de anotación). **Todo lo que sigue debajo de este banner es historia.**
>
> ✎ **2026-09-07 — ronda de Google Docs del 09-06 y lectura transversal de las Etapas 1–5.** El usuario
> aceptó y editó en Google Docs las cinco secciones (§15/16 v1.2 · §17.1 v1.16 · §17.3 v1.8 · §17.4 v1.8 ·
> §17.5 v1.5) y bajó los `.docx` limpios. La lectura transversal está en
> [`desarrollando/lectura-transversal-etapas-1-5-2026-09-07.md`](desarrollando/archivado/lectura-transversal-etapas-1-5-2026-09-07.md) (§8 = lista de trabajo por documento). **Veredicto:** Etapa 1 NO cierra (título
> de §16 sin estilo, oración rota en §16.3.4, párrafo AAIP que D-E1-11 mandó borrar) · Etapa 2 sí como texto, con
> 4 decisiones hacia atrás (X-1 fuente única ajuste/banco, X-6, X-7, X-8) · Etapa 3 sí con retoques · Etapa 4 NO
> (Figura 4.5 dentro de una oración y sin caption, Tablas 57/59 sin llamada, «cuarto componente», perfil sin
> nombrar) · Etapa 5 NO (**se borró el párrafo de las ocho limitaciones**, 0 figuras, «23 episodios» no cierra,
> Tablas 62/63 sin llamada). Todas las cifras rastrean a `results/`. **Falsas alarmas corregidas en la
> herramienta:** la celda «CR-02 en vivo» de la Tabla 64 SIEMPRE dijo «3 alertas: ≥ 7,1 s» y las Tablas 28/29/30
> de §17.1 existen: el extractor no atravesaba los `w:sdt` de Google Docs (parchado, 63 tests). Textos base
> `90`/`90b`/`90c`/`90f` re-extraídos de las versiones nuevas; superadas → `archivado/`; kit regenerado. Lo que
> sigue abajo (§1, §3.7) es la foto del 09-04 y queda como historia; el estado vigente es este banner + §3.8.
>
> ✎ **2026-09-07 — un solo documento de ajustes vigente:** el acta del pase 5. Las tres actas del pase 4 y
> la lectura transversal pasaron a `desarrollando/archivado/`; los mapas de secciones se quedan.
>
> ✎ **2026-09-07 — archivado.** Las cinco bases del pase 5, los dos análisis ya absorbidos, tres fotos del
> informe v1.1 y once guiones de pases cerrados pasaron a las carpetas `archivado/`, cada una con su
> `00-que-hay-aca.md`. Lo que se queda: los `.docx` vigentes, las actas de pase, los mapas de secciones y
> las herramientas de la cadena viva.
>
> ✎ **2026-09-07, misma jornada — PASE 5 APLICADO sobre las cinco secciones, todo como sugerencias y
> comentarios.** Entregadas: **§15/16 v1.3 · §17.1 v1.17 · §17.3 v1.9 · §17.4 v1.9 · §17.5 v1.6**, las
> cinco con «(sugerencias sin aceptar)» en el nombre. ✎ **Cuarta vuelta, PASE 5b:** §17.4 pasó a la
> **v1.10** y §17.5 a la **v1.7**, con la configuración del entrenamiento en §17.4.7 y la remisión
> ampliada en §17.5.6. Es un pase **incremental** sobre las versiones vigentes, no desde la base.
> ✎ **Quinta vuelta, PASE 5c:** §17.4 → **v1.11**, con la **baja de la fila «Pruebas automatizadas» de
> la Tabla 59** (el conteo de 2.203 no resistía el detalle y ya había envejecido) y una cláusula sin
> número en la nota. **Cierra la deuda R-12 en el informe.**
> ✎ **Sexta vuelta, PASE 5d — revisión completa a pedido del usuario:** cinco auditorías cruzadas
> sobre la vista aceptada (protocolo↔resultados, diseño↔implementación, §17.4↔código, §17.5↔índices,
> §15/16↔vocabulario + 52 comentarios). Corregidas como sugerencias 13 contradicciones de §17.5 contra
> `results/`, 9 imprecisiones de §17.4 contra el código y la coherencia protocolo↔resultados;
> **§17.1 → v1.18 · §17.3 → v1.10 · §17.4 → v1.12 · §17.5 → v1.8**. Veinte decisiones quedan
> listadas para el usuario y su colega en el acta, §12. Acta: [`desarrollando/correcciones-pase-5-etapas-1-5.md`](desarrollando/archivado/correcciones-pase-5-etapas-1-5.md).
> Las cuatro decisiones del usuario (D5-A a D5-D) fueron todas la recomendación. **§17.5 recupera las ocho
> limitaciones; §17.4 rehace la Figura 4.5 con la imagen vigente.** ✎ **Segunda vuelta del mismo día:
> §17.5 no lleva figuras de datos.** Las dos que se habían insertado se descartaron por decisión del
> usuario y su contenido volvió a tabla y a prosa, de modo que queda sólo el fotograma, como Figura 4.6.
> Compuerta verde en las cinco: rechazar todo devuelve el documento de partida, paquete OPC íntegro, y
> §15/16 pasa el verificador por primera vez. **Del usuario: revisar en Google Docs, y cuatro comentarios
> piden una confirmación que el repositorio no puede dar.** Al aceptar: re-extraer los textos base y
> regenerar el kit.

El **programa experimental está cerrado** (acta 128) y **los insumos del informe están
todos cerrados** (datos, decisiones, 17 tablas, 6 figuras). Lo único activo es el **pase de
redacción**. **§17.1 (Etapa 2) quedó cerrada con seis pases**, **§17.3 (Etapa 3) quedó cerrada
con cuatro** (v1.6 aceptada el 09-04), **§15/§16 (Etapa 1) está en ciclo de revisión con el
colega**, y **§17.4/§17.5 recibieron su pase de consolidación el 09-04** (§3.7), entregado con
sugerencias sin aceptar. Lo que falta se divide en cuatro frentes: terminar la Etapa 1, que el
usuario acepte las tres entregas de la jornada, la integración al maestro, y las tres secciones que
no existen (§17.6, §18, §19).

**Estado por sección** (documento vigente en `desarrollando/`):

| Sección | Documento vigente | Pases | Estado |
|---|---|---|---|
| §15 + §16 Estado del arte y Marco teórico | `…Secciones_15_y_16_…_v1.4.docx` | 5 + revisión del colega + ronda del usuario + pase 5 **aceptado** | ⏳ **en revisión de los colegas**: 9 comentarios abiertos (uno reabierto: no nombrar CR-01/CR-02 en §15 antes de §16), 1 sugerencia del pase 5 sin resolver, «puede puede» en 15.2.4 |
| §17.1 Consolidación metodológica | `…Seccion_17.1_…_v1.21.docx` | 6 + reestructuración + pases 5/5d/5e **aceptados** | ✅ **CERRADA**, limpia (sin comentarios ni marcas) |
| §17.3 Diseño arquitectónico | `…Seccion_17.3_…_v1.12.docx` | 4 + ronda del usuario + pases 5/5d **aceptados** | ✅ **CERRADA**, limpia |
| §17.4 Implementación | `…Seccion_17.4_…_v1.15.docx` | 4 + ronda + pases 5/5b/5c/5d/5e **aceptados** | ✅ **CERRADA**, sin marcas; 3 comentarios abiertos (dos míos explicando la reparación, uno del usuario sobre la URL). La ficha por video del lote depende de C1 |
| §17.5 Evaluación y validación | `…Seccion_17.5_…_v1.5.docx` ⚠ contenido de la v1.9 | 4 + ronda + pases 5/5b/5d **aceptados** | ✅ **CERRADA**, limpia |
| §17.6 · §18 · §19 | — | — | ❌ **sin redactar — FRENTE ACTIVO (Etapa 6, kit regenerado el 09-08)** |
| Maestro para integrar | `desarrollando/E-OVRT-VDP_v1.1_05062026-sin-indice.docx` | export del 09-08 | 📥 **en posición**; estilos de título `Ttulo1`…`Ttulo5`, ya contemplados por las herramientas |

---

## 1. Frente activo — cerrar la Etapa 1 (§15/§16)

> ✎ **2026-09-07:** la v1.2 del usuario es la v1.1 más un párrafo (intro a métricas MOT) y con el título «16.
> Marco teórico» sin estilo de encabezado; los defectos del 09-01 (§1.1) siguen todos. Ver la lectura transversal,
> hallazgos E1-B1…B3, E1-I1…I2 y X-2. Lo de abajo es la foto del 09-04.

El colega entregó la **v1.1** (18.657 palabras, −4.400 contra la v1.0; 71 títulos, 10
tablas, 10 comentarios C0–C9, sin cambios controlados). La crítica completa se entregó el
09-01. Lo que resta se divide en tres clases.

### 1.1. Defectos de edición — reparación mecánica, no requieren decisión

| # | Sitio | Qué pasa | Peso |
|---|---|---|---|
| 1 | **16.3.4** (párrafo "Por ello, una condición definida por ausencia…") | La reescritura **corrompió la frase de las dos formulaciones**: *"solicitar directamente… la infracción completa, o solicitar evidencia positiva.Segundo, derivar la ausencia…"* — la evidencia positiva quedó pegada a la opción 1. Es el **fundamento de E-DIR/E-IND**, el mecanismo central de la tesis | 🔴 **el más importante** |
| 2 | varios | Typos introducidos: `puede puede` (15.2.4) · `servicio.QoS` (15.4.2) · `positiva.Segundo` (16.3.4) · `midiendocuánto` (16.5.4) · falta un "que" en la nota de la Tabla 7 | 🟠 |
| 3 | ~6 sitios | **"donde" como conector comodín** (resto del pase de estilo). El peor: 16.4.3 *"…condicionados por el prompt, donde un tracker opera…"* — el contraste detector/tracker se volvió subordinada sin sentido | 🟠 |
| 4 | ×3 | `siendo que` / `siendo esta` — registro coloquial | 🟡 |
| 5 | 15.2.5 y 15.4.1 | **Voz D-P3-9**: dos futuros que pasan a presente ("deberán abordarse durante el diseño", "serán retomados… se analizará") | 🟡 |
| 6 | **16.5.2** | Ecuación (1) `t_G2A = …` es **texto plano** (lo era también en la v1.0) → pasar a objeto de ecuación de Word. ⚠ nunca con LibreOffice | 🟠 (C7) |
| 7 | 15.2.1 | Redundancia nueva: la intro de 15.2.1 repite ~70 % de las cuatro subsecciones que le siguen | 🟡 (C0) |
| 8 | 15.3.3 | Entra en seco a las métricas MOT: falta una oración de intro | 🟡 (C2) |

### 1.2. Pérdidas finas a evaluar — recomendadas, no obligatorias

- **16.5.2:** restituir la enumeración *"si comienza en el sensor, en la recepción, en la
  lectura o en el **dequeue**"*. Es una línea y es la que conecta con cómo el proyecto
  efectivamente mide G2A (**F-101.8**: se mide desde el dequeue).
- Dos frases-escudo perdidas: *"esta separación es conceptual: no convierte al sistema en
  distribuido ni exige una nube"* (16.5.3) y *"dos configuraciones sólo son comparables si
  procesan materiales y reglas de selección equivalentes"* (16.5.4).

### 1.3. Los 10 comentarios — decisión del usuario, no del redactor

> **Regla vigente:** los comentarios de un `.docx` se informan una vez como estado y
> **viajan**; el usuario indica cuándo y sobre cuáles se actúa.

| Comentario | Tema | Recomendación de la crítica |
|---|---|---|
| **C0** | catálogo 15.2.1 reestructurado | Validado. Solo desduplicar la intro (ítem 1.1.7) |
| **C1 · C3** | "Revisar anexo" (Tablas A.1 y A.2) | **Nada que tocar**: el Anexo A vive sano en `90e` (A.1 con 20 filas, licencias corregidas; A.2 reescrita) y pertenece a §19. Las remisiones son intencionales |
| **C2** | 15.3.3 sin intro | Aceptada → ítem 1.1.8 |
| **C4** | 15.4.1.1 sin catálogo | **Validado: la reescritura es mejor que el original.** Nada que restituir |
| **C5** | poda de 16.2 | Criterio firmado; nada que restituir (ver §2 de este documento) |
| **C6** | "Yuksekgonul me suena a que es nueva" | **Es nueva y es deliberada** (alta del pase 3, E1-25). Funda por qué "persona sin casco" es difícil. **No sacarla** |
| **C7** | ecuación a fórmula | Aceptada → ítem 1.1.6 |
| **C8** | poda de 16.6 | Criterio firmado; lo esencial sobrevive (verificado contra la v1.0) |
| **C9** | inscripción AAIP: "yo lo sacaría" | ✅ **D-E1-11 CERRADA el 09-01: sí, se borra** (párrafo + marcador, retirando el rango de C9). El espejo de §17.1 ya está borrado (v1.8). Ver §3.1 y `desarrollando/archivado/cierre-d-e1-11-aaip.md` |

### 1.4. Efecto bibliográfico de la Etapa 1 (para la integración)

Si la poda se confirma —ya está firmada—, salen del listado global: **Decreto 351/79 ·
Res. SRT 51/97 · Res. SRT 35/98 · ISO 45001 (ISO 2018) · Decreto 1558/2001**. Ley 19.587,
Dec. 911/96, Ley 25.326 y Disp. 10/2015 **se quedan** (las sostienen las nuevas §16.2/§16.6).
Con el cierre de D-E1-11 (09-01) se suma una baja: **AAIP, s. f.-b** (su única cita en la
v1.1 era el párrafo borrado; la otra "s. f.-b" del documento es Luxonis). Si para la AAIP
queda solo la s. f.-a, re-letrar a "s. f." (entrada y citas en el texto).

**Cómo se puede ejecutar 1.1 y 1.2:** el mismo mecanismo que funcionó en el pase 6 —
especificación con anclas verificadas + aplicación directa sobre el XML + compuerta
reproducible. Requiere primero la decisión del usuario sobre 1.3.

---

## 2. Lo que quedó firmado el 2026-09-01 (no reabrir sin decisión nueva)

- **Criterio normativo (9 reglas).** La normativa fundamenta **relevancia preventiva y
  límites de uso**; nunca deriva taxonomías, severidades, ventanas ni requisitos técnicos.
  §16 explica; §17.1 operacionaliza sin reconstruir leyes.
- **Las dos tablas eliminadas de la Etapa 1 no se restituyen**: la matriz normativa (vieja
  Tabla 10, 8 categorías con artículos) y la Tabla 12 de principios ético-legales. Esta
  decisión **supera los guardrails del pase 3** en esos dos puntos, a conciencia.
- **D-P6-1:** una sola cita legal directa en §17.1, en 17.1.10.1. El resto, remisiones.
- **D-P6-2:** la severidad es una **categoría metodológica de prioridad temporal**, no una
  clase jurídica.
- **D-P6-3:** **Res. SRT 299/2011 se da de baja del informe** (ver §3.3).
- **PODA-C / MOT (D-P5-3):** no se reabre. El MOT queda intacto en §17.1.
- **La extensión de §17.1 (~140 pág) está justificada por escrito** en
  [`justificacion-extension-17-1.md`](desarrollando/archivado/justificacion-extension-17-1.md). Lo
  descartado (~3.100 w) se paga en defensa, no se vuelve a discutir.

---

## 3. Handoffs abiertos

### 3.1. D-E1-11 — inscripción ante la AAIP · ✅ **CERRADA el 2026-09-01**

**Decisión del usuario (converge con C9): el informe NO adjudica el trámite** — se borran
el párrafo indeciso y los dos marcadores; las salvaguardas de §16.6 (finalidad, acceso
restringido, retención acotada, sin biometría) son el recaudo documentado, y la respuesta
sobre la inscripción se prepara **para la defensa** (sigue siendo "el hilo del que un
jurado tira": el proyecto sí grabó personas). Constancia, fundamento y anclas por versión:
[`desarrollando/archivado/cierre-d-e1-11-aaip.md`](desarrollando/archivado/cierre-d-e1-11-aaip.md).

- **§17.1: HECHO** — v1.7 → **v1.8** (oración de anclaje de §17.1.10.1 + marcador espejo
  fuera; compuerta verde, 76 ecuaciones, 27 comentarios, 0 marcas, verificador OK).
- **§16: viaja con el pase de la Etapa 1** (v1.1 → v1.2): borrar el párrafo "La normativa
  específica contempla…" + marcador, retirando el rango del comentario C9.
- **§17.4:** nada que tocar (verificado: cero menciones).
- La obligación de inscripción sigue *descripta como marco* donde la sección presenta la
  Disposición 10/2015 — eso no se toca.

### 3.2. ✅ §17.3 → v1.6 · **APLICADO el 2026-09-03 y ACEPTADO por el usuario el 2026-09-04 — CERRADO**

El handoff que venía del pase 4 de la Etapa 2 (**E3-42** + 3 sitios de voz D-P3-9 + 11
metadiscursos + 2 párrafos gordos) **se aplicó dentro del pase 4 de la Etapa 3**, junto con la
consolidación narrativa completa del capítulo: **61 → 30 títulos** (cero de nivel 5), **prosa
13.174 → 10.075 (−24 %)**, 17 → 14 tablas, 6 → 4 figuras, dos puntos **73 → 0**, punto y coma **86 → 0**.
Compuerta verde, 0 fallas. Acta:
[`desarrollando/correcciones-etapa-3-pase-4.md`](desarrollando/archivado/correcciones-etapa-3-pase-4.md).
⚠ **La numeración de subsecciones cambió**: toda acta E3-01…E3-42 y las 26 redlines se leen con
[`desarrollando/mapa-secciones-17-3-v1-6.md`](desarrollando/archivado/mapa-secciones-17-3-v1-6.md).

Cierre del frente (✎ 2026-09-04):

1. ✅ **El usuario aceptó las sugerencias** y guardó `…_v1.6.docx` (14.220 palabras, 30 títulos, 0
   marcas, `verificar_entregable.py` OK). Quedan **4 comentarios abiertos** (2 del colega y 2
   respuestas ancladas); cuándo se cierran lo decide el usuario. Las versiones superadas (v1.5 y
   la v1.6 con sugerencias) pasaron a `desarrollando/archivado/`.
2. ✅ `90-etapa3-texto-extraido.md` **re-extraído de la v1.6** (regla D-C) y kit de la Etapa 3
   regenerado (`--check --etapa all` OK).
3. **Handoff a la Etapa 4 (`E4-31`)** — el detalle operativo del ledger — queda **absorbido por el
   análisis de §3.7**, junto con H2-01 y H2-02.
4. **Decisión disponible, no ejecutada:** un pase de **poda por aporte**, como el pase 5 de la
   Etapa 2. El análisis estimaba −32 % y la poda sin pérdida de contenido llegó a −24 %.

### 3.3. Bibliografía y numeración global · **dueño: la integración**

- **Baja:** Res. SRT 299/2011 (D-P6-3) — verificado: cero apariciones en §15/§16 v1.1,
  §17.1 v1.8, §17.3, §17.4 y §17.5.
- **Bajas de la Etapa 1:** las cinco de §1.4, más **AAIP s. f.-b** por el cierre de
  D-E1-11 (con re-letrado de la s. f.-a si queda sola).
- **Listado global:** `90e` tiene **83 entradas**; hay que aplicarle las bajas y confirmar
  que no queden huérfanas ni citas sin entrada.

### 3.5. ✅ `AJ-5.14` — §17.5 reporta el costo del vocabulario activo · **APLICADO el 2026-09-04**

> Resuelto dentro del pase 4 de la Etapa 5 (unidad **E5-05**): el contraste de variable única
> (0,704 → 0,622) entra en §17.5.4 y la no ejecución del sub-experimento formal, en §17.5.7. §17.1
> no se tocó. Lo que sigue es el planteo original, conservado como registro.

Descubierto el **2026-09-02** al reestructurar §17.1.5. Su eje de composición del
vocabulario activo **promete** que cada prompt se evalúa en aislamiento y dentro del
vocabulario completo, y el diseño de prompts formalizó un sub-experimento aislado-vs-completo
sobre las finalistas. **Ese sub-experimento no se corrió, y §17.5 v1.3 no lo reporta ni como
resultado ni como no-ejecución** (verificado: `0,622` y `0,082` aparecen cero veces).

La medición **existe** y es buena para la defensa. F-88.1: mismo modelo, evaluador, pattern
set, GT y timings, **una palabra más en el caption** cuesta **0,082 de F1** (0,704 → 0,622).
F-94.1 es el caso extremo, con una clase solapada que borra a la otra.

Dos inserciones, más una opcional. Ficha completa con cifras, artefactos y la trampa de cita
de F-94.1 ("aislada" = sin `machinery` al lado, **no** sola):
[`../ajustes/05-etapa-5-evaluacion-y-validacion.md`](../ajustes/05-etapa-5-evaluacion-y-validacion.md)
§AJ-5.14. **No se toca §17.1**: la promesa es pre-registro y D-P3-3 prohíbe reescribirla
para que encaje con el resultado.

### 3.6. Marcador de procedencia en §17.4 · **dueño: el usuario**

`[[PENDIENTE: dirección de origen y fecha de acceso por clip del lote de obra real]]` —
depende de **C1** (§5), que está diferido a post-entrega. Es el mismo dato.

### 3.7. ✅ Etapas 4 y 5 — pase de consolidación **APLICADO el 2026-09-04; falta que el usuario acepte**

Mismo encargo que en las Etapas 1–3 (menos repetición, coherencia con lo ya fijado, cero nivel 5,
menos `:` y `;`, voz de TFG). Diagnóstico en
[`desarrollando/archivado/analisis-17-4-17-5-etapas-4-5.md`](desarrollando/archivado/analisis-17-4-17-5-etapas-4-5.md),
con las **15 decisiones D-A…D-O firmadas por el usuario** ese mismo día, todas en la recomendación.
Actas: [`correcciones-etapa-4-pase-4.md`](desarrollando/archivado/correcciones-etapa-4-pase-4.md) (E4-32…E4-57)
y [`correcciones-etapa-5-pase-4.md`](desarrollando/archivado/correcciones-etapa-5-pase-4.md) (E5-01…E5-11).
Compuerta `herramientas/verificar_pase_17_4_17_5.py` **verde, 0 fallas**, con la propiedad que hace
segura la entrega: **rechazar todos los cambios devuelve exactamente el documento de partida**.

⚠ **La numeración de subsecciones de §17.4 cambió** (16 → 9 títulos): toda unidad E4-01…E4-31, las
fichas `AJ-4.x` y la extracción `90b` se leen con
[`desarrollando/mapa-secciones-17-4-v1-7.md`](desarrollando/archivado/mapa-secciones-17-4-v1-7.md). §17.5
conserva su numeración de subsecciones; sólo cambian las tablas.

**Resultado.** §17.4: prosa y tablas 6.375 → 5.493 w (−13,8 %), 16 → 9 títulos, cero de nivel 4,
6 → 5 tablas (56–60), dos puntos 55 → 1, punto y coma 29 → 0, rayas 28 → 0, párrafos de más de 150
palabras 9 → 0, oraciones de más de 45 palabras 27 → 0. §17.5: 9 → 8 títulos, 6 → 5 tablas (61–65),
dos puntos 15 → 0, punto y coma 16 → 0, y **suma** AJ-5.14 y las ocho limitaciones.

Lo que el análisis encontró y el pase absorbió, además de la poda:

- 🔴 **§17.4.4 afirma un orden de arranque falso** («primero la distribución, después el control, por
  último medios»); §17.4.5 da otro orden incompleto citando **17.3.8.4, que ya no existe**; la nota y
  la figura embebida (que **no es** la FIG-A producida) dan un tercero. Real: **control → distribución →
  medios**, garantía = *handshake* del publicador (**H2-01**). §17.3.6.3 v1.6 remite a §17.4 para esto.
- 🔴 **Tabla 66, fila «CR-02 en vivo»: celda de resultado vacía** en la exportación del 08-27 (la v1.3
  del 08-23 decía «3 alertas: ≥ 7,1 s»).
- 🟠 Cuatro handoffs registrados y ausentes: **H2-01**, **H2-02** (2.946 imágenes vs rango 500–2.000,
  causa anti-*leakage*), **E4-31** (ledger), **AJ-5.14** (0,704 → 0,622 y el sub-experimento no corrido).
- 🟠 **L1–L8 se citan en §17.5.8 y no se declaran en ninguna sección vigente**; el usuario anotó
  «borrar» sobre §17.5.8 y AJ-5.05 exige que §17.5 las traiga (decisión D-H).
- ✅ «2.203 pruebas» era foto del 08-05 (R-12) — **la fila se borró en el pase 5c del 09-07**; Tabla 60 → prosa (comentario del usuario); Tabla 65
  (dos filas) → prosa (D-P2-1); nueve temas contados con cifras en §17.4 y en §17.5.
- 🟡 Comentario «agregar hs de anotación»: **el dato no existe en el repositorio**; sólo el usuario.

**Del usuario:** aceptar las dos entregas con sugerencias (§17.4 v1.7 y §17.5 v1.4). La de §17.3 ya
no requiere aceptación: su único cambio, la remisión «17.4.6» → «17.4.4» que la renumeración obliga,
**se aplicó en limpio sobre la v1.6 y quedó como `…_17.3_…_v1.7.docx`**; **reemplazar la
imagen de la Figura 4.5** por la producida en `informe/figuras/`; **pegar las tres figuras de
§17.5**; decidir si aporta las horas de anotación; git. **Al aceptar:** re-extraer `90b` y `90c`
(regla D-C) y regenerar el kit. Los **ocho comentarios quedan abiertos con su ancla** (D-M); los
siete cuyo párrafo desapareció fueron re-anclados al texto que los absorbe.

### 3.8. Ronda de Google Docs del 09-06 — lectura transversal **HECHA el 2026-09-07; falta que el usuario aplique la lista**

Documento: [`desarrollando/lectura-transversal-etapas-1-5-2026-09-07.md`](desarrollando/archivado/lectura-transversal-etapas-1-5-2026-09-07.md). Qué cambió, veredicto por etapa, hallazgos por severidad, lo que quedó bien, las
falsas alarmas descartadas y la lista de trabajo por documento (§8). Resumen de lo que bloquea:

- **§17.5 v1.5:** el párrafo de las **ocho limitaciones fue eliminado** (decidir: restaurar desde la v1.4 archivada
  o handoff explícito a §18); **cero figuras** (FIG-B/C/F sin pegar); «medida sobre 23 episodios confirmados» no
  cierra con n = 28 de la Tabla 63 (→ 21); Tablas 62 y 63 sin llamada en prosa; «frontera de de juicio».
- **§17.4 v1.8:** Figura 4.5 **dentro de la última oración de 17.4.1, sin caption y con la imagen del 08-23**;
  Tablas 57 y 59 sin llamada; «cuarto componente funcional» contradice §17.3.7; `gdino-tiny-560` no se nombra en
  17.4.4; causa del tercer tramo de ajuste fino distinta a las actas; «el despliegue integral instancia» en presente.
- **§15/16 v1.2:** «16. Marco teórico» sin estilo Título 1; oración rota de §16.3.4 (E-DIR/E-IND); párrafo y
  marcador AAIP (D-E1-11 mandó borrarlos y §17.1 ya no los espeja); typos del 09-01; 11 comentarios.
- **Transversal (decisiones del usuario):** X-1 regla de fuente única ajuste/banco (§17.1.6.3) vs práctica (FT con
  `construction_site_safety`, cuyo núcleo curado de 147 está en el banco); X-2 G2A con captura y transporte adentro
  en §16 vs desde el dequeue en §17.1/§17.5; X-6 métricas obligatorias sin estado en §17.5.7; X-7 calibración en
  mitad vs Tabla 26; X-8 banco temporal sin decisión en §17.1.6.

**Hecho el 09-07:** extractor corregido (`w:sdt`), `90`/`90b`/`90c`/`90f` re-extraídos, versiones superadas
archivadas, kit regenerado. **Del usuario:** aplicar la lista §8 en Google Docs (primero §17.5 y §17.4), bajar los
`.docx`, y se repite la lectura sobre las versiones corregidas antes de declarar cerrada cada sección. Git.

### 3.9. ✅ Pase 5 sobre las cinco secciones — **APLICADO el 2026-09-07; ACEPTADO por el usuario el 2026-09-08** (bajada + pase 5e: banner de §0 y acta §14)

Todo entró **como sugerencias y comentarios**, por indicación del usuario: nada en limpio.

**Lo que cierra:** las ocho limitaciones de §17.5 · la Figura 4.6 de §17.5 y la 4.5 de §17.4, insertadas
por XML y verificadas por huella contra `informe/figuras/` · el título de §16 recupera su estilo
y §15/16 pasa el verificador por primera vez · la oración de §16.3.4 · el borrado del AAIP (D-E1-11) · el
origen instrumentado de G2A · las llamadas de las Tablas 57, 59, 62 y 63 · «cuarto componente funcional» ·
el perfil operativo nombrado en §17.4.4 · la causa del tercer tramo de ajuste fino corregida contra las
actas · las tres precisiones de §17.1 · dos sentidos restituidos en §17.3.

**Dos correcciones de cifra que sólo aparecieron yendo al artefacto de la campaña:** «medida sobre 23
episodios confirmados» era el conteo de clips con CR-01 confirmado y no el denominador de la media, que es
**21** para CR-01 y **7** para CR-02; y la columna de latencia de la Tabla 63 declara episodios confirmados
mientras la media se promedia **por clip**, que es un conteo menor cuando un clip trae las dos condiciones.

**Segunda vuelta del mismo día — §17.5 sin figuras de datos.** Tras revisar la primera entrega, el usuario
descartó las dos figuras de datos que se habían insertado. La de calidad contra densidad era una tabla de
cuatro filas dibujada como curva, con seis de sus ocho valores ya en la Tabla 64, que ahora completa la serie
con las densidades de 30 y 2,00 fps. La de la frontera de juzgabilidad mezclaba dos cosas distintas, porque
juzgabilidad es si el anotador humano puede determinar el estado y lo que graficaba era rendimiento del
sistema, y además tomaba cuatro clips de una foto anterior al cierre de la campaña de diecisiete, omitía un
clip con dato medido y dejaba afuera la variable que define el fenómeno. **Sus tres ejes pasaron a prosa en
17.5.3** con las cifras exactas, incluida la caída nocturna. Queda una sola figura en §17.5, el fotograma con
la alerta confirmada, renumerado como 4.6. Las dos descartadas siguen produciéndose y publicadas en el
repositorio público, así que no se archivan: cambia su destino, no su validez.

**Tercera vuelta — un fotograma de CR-02, intentado y descartado.** Se produjo con el mismo pipeline que la
figura 4.6 y quedó inservible: el detector dibuja una caja de chaleco sobre la ropa oscura del actor, así que la
imagen muestra la alerta de «sin chaleco» junto a un chaleco sobre esa persona. En los siete clips del rodaje con
episodio de esa condición el detector propone chaleco en el 70 % al 96 % de los cuadros, de modo que **ninguno da
un fotograma limpio**. El fenómeno ya estaba documentado. Constancia en el README de los videos de defensa.

**Compuerta verde en las cinco**: rechazar todas las sugerencias devuelve el documento de partida, el
paquete OPC está íntegro y el verificador mecánico no encuentra problemas duros sobre el resultado aceptado.

**Del usuario:** revisar en Google Docs. **Cuatro comentarios piden una confirmación que el repositorio no
puede dar**: las mitades de calibración del banco de imágenes, la formulación de la evidencia visual
controlada, si el borrado de las tres notas de §17.3 fue deliberado, y si las limitaciones quedan en §17.5
o viajan a §18. **Al aceptar:** re-extraer `90d`, `90f`, `90`, `90b` y `90c` (regla D-C) y regenerar el kit.

---

## 4. La integración al documento maestro

El maestro (`E-OVRT-VDP_v1.1_05062026-sin-indice.docx`) todavía tiene §17.3/§17.4 en
versión previa y §17.5 vacía. Cada sección se trabajó **en su propio `.docx`**; falta
juntarlas. Lo que hay que resolver al integrar:

**4.1. Numeración global de tablas — verificada el 09-01, ✎ re-verificada el 09-07 sobre las
cinco versiones vigentes (vista aceptada):**

| Tramo | Tablas | Observación |
|---|---|---|
| §11–§14 | 1 | frontmatter/plan |
| §15 + §16 | **2–11** | 10 tablas (la vieja Tabla 12 se eliminó en la v1.1) |
| *hueco* | **12–15** | ⚠ **4 números libres** — §17.2 (Costos asociados) no tiene tablas |
| §17.1 | **16–35** | ⚠ **16 tablas numeradas en 20 números**: caen 18, 19, 31 y 32 (v1.11 y v1.14). Vigentes 16, 17, 20–30, 33–35; los anexos C y D suman 6 tablas con numeración propia. ✎ 09-07: **16, 17, 24, 26 y 27 existen pero ninguna oración las llama por número** |
| *hueco* | **36–38** | ⚠ 3 números libres |
| §17.3 | **39–52** | ✎ 14 tablas (el pase 4 bajó de 17 a 14 y renumeró; antes 39–55) |
| *hueco* | **53–55** | ⚠ ✎ 3 números libres que dejó esa baja: §17.4 ya estaba numerada desde 56 |
| §17.4 | **56–60** | ✎ 5 tablas (el pase 4 fundió una; antes 56–61) |
| §17.5 | **61–65** | ✎ 5 tablas (antes 62–67) |

**Catorce números libres en total** (12–15, 18–19, 31–32, 36–38, 53–55), todos con causa
documentada en los mapas de secciones. Hay que decidir si se renumera todo de corrido o se
documentan los huecos. **No se toca ahora**: es trabajo de integración, y renumerar antes de tiempo
rompe las remisiones internas de cada documento. Lo razonable al integrar es numerar con campos
de Word, como ya se anotó para las figuras.

**4.1.b. Título de §17.3.** El `.docx` de §17.3 arranca en «17.3.1. Propósito y pregunta rectora»
y **no trae el título «17.3. Diseño arquitectónico»** (ya era así en la v1.6 aceptada). §17.1,
§17.4 y §17.5 sí traen el suyo. Al integrar hay que agregarlo en el maestro.

**4.2. Anexos:** los **Anexos C y D** viajan al final del propio `.docx` de §17.1 (D-P3-8)
y hay que mudarlos a **§19.3/§19.4**; el **Anexo A** (Tablas A.1 y A.2) vive en `90e` y va
a **§19.1** — si no llega, quedan **dos remisiones colgadas** en §15.2.3 y §15.3.3.

**4.3. Nombres de métrica:** ✅ **resuelto en la v1.15** — todo el capítulo usa texto plano
(`t_alert-system`, `t_G2A`) y sólo quedan **4 objetos de ecuación**: las dos definiciones por
hitos de §17.1.7.5 y las dos del modelo de presupuesto. Nada que unificar.

**4.5. §17.1 después de la reestructuración (09-03):** la numeración de subsecciones cambió
(109 → 37 títulos) y toda acta anterior cita números que ya no existen —
[`desarrollando/mapa-secciones-17-1-v1-15.md`](desarrollando/archivado/mapa-secciones-17-1-v1-15.md) es la
traducción obligatoria y lleva además los siete residuales del capítulo. Dos entran en la
bibliografía global: **Milan et al. (2016)** para MOT17 y **Liang y Han (2024)** para OVT-B
(verificadas en arXiv, altas nuevas). Otros dos son de estilo: *baseline* sobrevive en celdas de
las Tablas 16, 33 y 34 mientras la prosa dice *línea base*, y la única *"Fuente: elaboración
propia."* del capítulo quedó en la nota de la Tabla 21. Y uno es de fondo: §17.1 declara **35–250 ms**
para el tramo previo a la acumulación, mientras el doc 39, el inventario de métricas y
`results/realtime` verifican G2A contra **50–250 ms** — §17.4 y §17.5 deben mapear una cifra a la
otra al reportar.

**4.4. Las figuras:** las **cinco** que faltaban están producidas en `informe/figuras/`
(PNG a 300 dpi + SVG donde aplica; ancho de diseño **16 cm** — insertar a ese ancho y **no
reescalar**, que es donde se eligieron los tamaños de letra), y **FIG-D** ya estaba en
disco. Pero **pegarlas sigue pendiente** en todos los casos. Destinos: **FIG-A → §17.4.1**
· **FIG-E → §17.3.6.1** (ex 17.3.8.2) · **FIG-B, FIG-C, FIG-F → §17.5**. Tres advertencias de cita
del README: la distribución en línea es **continua** · el orden de arranque es **control →
distribución → medios y la garantía es el *handshake* del publicador, nunca «inverso al flujo de
datos»** (✎ 09-04: la advertencia vieja era la falsa, corregida en el README el 08-28) · la máquina es
de **5 estados con reapertura a `candidate`**. ~~⚠ La Figura 4.7 embebida hoy en §17.4.1 **no es la
FIG-A producida** (es la versión del 08-23 con el orden incompleto): hay que reemplazarla.~~ ✎ **09-08:
resuelto** — la Figura 4.5 de §17.4 v1.13 **es la FIG-A vigente** (1926×1684 px a 16 cm; Google Docs
re-codifica el PNG al exportar, así que la huella ya no coincide con `figuras/` pero las dimensiones sí)
y la Figura 4.6 de §17.5 v1.9 es el fotograma. **FIG-A y FIG-C: pegadas y aceptadas.** FIG-B y FIG-F no
van al informe (09-07). FIG-E: verificar en el `.docx` de §17.3 (trae 4 imágenes) al integrar.
Pendiente de integración además: los rótulos «Nota» tienen tres formatos entre secciones (cursiva en
§17.1, negrita en §17.3, negrita+cursiva mezclada en §15/16 y en tres tablas de §17.1 que el usuario
tocó el 09-08): unificar al integrar, no antes.

---

## 5. Lo que se decidió NO hacer antes de entregar (acta 128 §4)

Nada de esto bloquea el informe. Orden vigente: **el informe primero**.

| # | Ítem | Dueño | Nota |
|---|---|---|---|
| 2 | **Builds + smoke integral** de `infra/platform` (13 servicios) | usuario + sesión conjunta | ⚠ daemon Docker apagado; disciplina de disco del doc 126 — **nunca Capa 3 autónoma** |
| 3 | **C1** — URLs y licencias de los 18 `clip.yaml` | usuario | ⚠ **no borrar `scripts/downloads/`** antes de cerrarlo. Bloquea la versión final y el marcador de §3.4 |
| 4 | **V2** — video de defensa | usuario | ⚠ mi intento anterior con `gloves` era falso: auditar visualmente la clase antes de afirmar |
| 5 | Latencia pareada de los 3 brazos de fine-tuning | usuario decide | descriptivo y **opcional**; no cambia ningún veredicto |

**Reabrir experimentos exige pre-registración nueva** (acta 128 §5).

---

## 6. Deuda git — **dueño exclusivo: el usuario**

> El usuario maneja todo el git. **El merge a `main` no se ofrece ni se lista como
> pendiente.**

Verificado el 2026-09-01:

| Repo | Rama | Sin commitear | Sin pushear |
|---|---|---|---|
| **`docs`** | `main` | **37 archivos** | 0 |
| `e-ovrt_datasets` | `feature/datasets-v2-setup` | 0 | 0 |
| `e-ovrt_media-plane` | `feature/inference-service` | 0 | 0 |
| `e-ovrt_control-plane` | `feature/control-service` | 0 | 0 |
| `e-ovrt_experimental-setup` | `feature/webconsole-consola-tesis` | 0 | 0 |
| `e-ovrt_alert-distribution` | `main` | 0 | 0 |

Los de `docs` son el trabajo del **08-31, 09-01 y 09-03**: la §17.1 hasta la **v1.15 final** y
todo su historial en `archivado/` (v1.0–v1.15-sin-aceptar, los pases 3 a 6 y las cinco constancias
del ciclo), la Etapa 1 v1.1 del colega, `90f` re-extraído y `90g` con banner histórico, el nuevo
`mapa-secciones-17-1-v1-15.md`, el kit regenerado con `INSTRUCCIONES`, el generador, el tablero,
`ajustes/02` y las herramientas de los pases (`aplicar_pase6.py`, `verificar_anclas_pase6.py`,
`aplicar_v112_17_1.py`, `aplicar_v113_17_1.py`, `aplicar_v114_17_1.py`, `aplicar_v115_17_1.py`).
El conteo de abajo es del 09-01 y quedó corto: **`git status` manda**.

⚠ Recordatorio del doc 126: **la raíz del workspace `/home/simonll4/projects` NO es un repo
git** (`CLAUDE.md`, `AGENTS.md`, `_archived/`, `scripts/` no están respaldados por ningún
remoto) — va a la capa de evidencia del backup.

---

## 7. Herramientas disponibles para lo que queda

Construidas en esta jornada y reutilizables (`docs/herramientas/`, stdlib puro — el entorno
no tiene `lxml`, `python-docx` ni `pandoc`):

- **`aplicar_pase6.py`** — aplica un mapa de reemplazos sobre un `.docx` editando byte a
  byte **solo los `<w:t>` que solapan cada ancla**: no re-serializa el XML, así que
  ecuaciones, rangos de comentario y formato quedan intactos. Aborta ante cualquier conteo
  inesperado. **Es la plantilla para el pase de la Etapa 1** (cambiar la tabla `REEMPLAZOS`).
- **`verificar_anclas_pase6.py`** — compuerta `--pre` / `--post`: anclas, greps prohibidos,
  guardrails que deben sobrevivir e invariantes (ecuaciones, comentarios, marcas, marcadores).
- `extraer_informe.py` (regla D-C: re-extraer el `.md` al cerrar una sección) ·
  `verificar_entregable.py` · `generar_project_kit.py --check --etapa all` (62 tests + 51
  subtests; **correr pytest desde `docs/`, no desde `herramientas/`**).

**Trampas registradas que valen para el próximo pase:**
1. Los "huecos" en el texto extraído de §17.1 (`": , Tiempo…"`, `"ni  sobre imágenes"`) son
   **ecuaciones OMML inline**, no defectos. No "repararlos".
2. Al limpiar marcadores de comentario de una extracción, usar un regex de **tokens**
   (`⟦C\d+▶|◀C\d+⟧|⟦ref C\d+⟧`), no `⟦[^⟧]*⟧`: el genérico se come el texto anclado.
3. No "corregir" el anclaje de otro auditor sin grep exhaustivo del término pelado — en el
   pase 6, GPT tenía razón sobre 17.1.2.2 y existían **ambos** sitios.
4. Nunca abrir/guardar estos `.docx` con LibreOffice: rompe las ecuaciones.

---

## 8. Orden sugerido

> ✎ **2026-09-07 — orden vigente:** primero la lista de trabajo del §8 de [`desarrollando/lectura-transversal-etapas-1-5-2026-09-07.md`](desarrollando/archivado/lectura-transversal-etapas-1-5-2026-09-07.md) (§17.5 → §17.4 →
> §15/16 → decisiones X-1/X-7/X-8 sobre §17.1 → retoques de §17.3), después los puntos 5–7 de abajo. Los puntos
> 1–4 quedaron absorbidos (el 4 se aceptó el 09-06).
>
> ✎ **2026-09-07:** esa lista se aplicó entera en el pase 5 (§3.9) y las cinco secciones están entregadas con
> sugerencias. El orden vigente es: **revisar las cinco en Google Docs** → responder los cuatro comentarios que
> piden confirmación → aceptar → re-extraer y regenerar el kit → puntos 5, 6 y 7 de abajo (§17.6, §18, §19 y la
> integración).

1. **Decidir los 10 comentarios de la Etapa 1** (§1.3) — es lo único que bloquea el frente
   activo. Con eso escribo el pase y lo aplico con la misma cadena del pase 6.
2. ✅ ~~Firmar D-E1-11 (AAIP)~~ — **firmada y con el lado §17.1 aplicado el 09-01** (§3.1);
   el lado §16 viaja dentro del pase del punto 1.
3. ✅ ~~Aplicar el handoff de §17.3~~ — **hecho el 09-03 dentro del pase 4 de la Etapa 3** y
   **v1.6 aceptada el 09-04** (§3.2). Cerrado.
4. **Decidir D-A…D-O del análisis de §17.4/§17.5** (§3.7) y aplicar el pase de las Etapas 4 y 5;
   absorbe `AJ-5.14` (§3.5), H2-01/H2-02 y E4-31.
5. **Escribir §17.6, §18 y §19** — las tres que no existen.
6. **Integración al maestro** (§4): anexos, numeración de tablas, figuras, bibliografía.
7. Post-entrega (§5), mientras se esperan correcciones del jurado.
