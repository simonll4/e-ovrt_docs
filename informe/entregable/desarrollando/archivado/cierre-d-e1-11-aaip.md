# Cierre de D-E1-11 — inscripción ante la AAIP: la decisión y sus cuatro sitios

> ✅ **CERRADO — verificado sobre la v1.15 final (2026-09-03): cero apariciones de "AAIP" en §17.1.**
> El lado §16 sigue viajando con el pase de la Etapa 1. Ya no se edita.

> **Decisión FIRMADA por el usuario el 2026-09-01** (converge con el comentario C9 de la
> Etapa 1 v1.1): **el informe no adjudica el trámite de inscripción ante la AAIP** — se
> borran el párrafo de "decisión pendiente del equipo" y los dos marcadores
> `[[PENDIENTE]]`. Las salvaguardas sustantivas de §16.6 (finalidad explícita, acceso
> restringido, retención acotada, sin reconocimiento de identidad ni tratamiento
> biométrico) **son el recaudo documentado**; la respuesta sobre la inscripción se
> prepara para la defensa, no para el texto.
>
> **Estado:** lado §17.1 **APLICADO Y VERIFICADO el 2026-09-01** (v1.7 → v1.8, acta en
> §3). Lado §16: **viaja con el pase de la Etapa 1** (v1.1 → v1.2), especificado en §2.

## 1. Por qué borrar (y no responder ni dejar el pendiente)

- Un entregable final no puede llevar un `[[PENDIENTE: definir con el equipo…]]`: la
  pregunta nunca fue "¿se queda?" sino "¿cómo se cierra?".
- Un párrafo que declara la aplicabilidad "pendiente" **planta la pregunta del jurado sin
  responderla** ("¿y al final, inscribieron la base?") — peor que el silencio.
- Afirmar "no corresponde inscribir" sería un juicio legal que nadie del equipo puede
  respaldar. La opción defendible es documentar las salvaguardas (ya está hecho) y no
  adjudicar el trámite.
- Coherencia con el criterio editorial firmado el 09-01: **normativa = marco conceptual,
  nunca especificación**. La obligación de inscripción sigue *descripta como marco* donde
  la sección describe la Disposición 10/2015; lo que se va es la *postura indecisa del
  proyecto*.
- Nota de procedimiento: la crítica a C9 ("no borrar sin cerrar D-E1-11") era
  **procedimental** — que no cayera en silencio como efecto colateral de la poda. Esta
  decisión del usuario **es** el cierre de D-E1-11 y supera el "AAIP queda
  `[[PENDIENTE]]`" del criterio del 09-01 en ese único punto.

## 2. Sitios en §16 — dueño: el pase de la Etapa 1 (v1.1 → v1.2)

Las anclas difieren por versión; el pase se escribe sobre la que el equipo adopte.

**Sobre la v1.1 (la esperable — C9 apunta acá):**
- **B1** · borrar el párrafo entero (§16.6.1):
  `La normativa específica contempla además requisitos administrativos asociados a las bases de datos de videovigilancia. Su aplicabilidad al contexto experimental se mantiene como una decisión pendiente del equipo, por lo que no corresponde asumirla ni descartarla en esta instancia (Agencia de Acceso a la Información Pública, s. f.-b).`
- **B2** · borrar el párrafo marcador que le sigue:
  `[[PENDIENTE: definir con el equipo la aplicabilidad de esta inscripción al contexto experimental y documentar el recaudo adoptado en §17.1 y §17.4.]]`
- ⚠ **El comentario C9 ancla EN estos dos párrafos** (commentRangeStart en B1;
  commentRangeEnd + commentReference en B2). Al borrarlos hay que retirar también el
  rango y la referencia de C9 — C9 queda resuelto por esta decisión, no huérfano.
- **Efecto bibliográfico (para la integración):** esa era la ÚNICA cita a
  *Agencia de Acceso a la Información Pública, s. f.-b* en la v1.1 (la otra "s. f.-b" es
  Luxonis) ⇒ **baja de la entrada s. f.-b** y, si para esa autora solo queda la s. f.-a,
  **re-letrado APA**: "s. f.-a" → "s. f." (entrada y citas en el texto).

**Si en cambio se siguiera sobre la v1.0:** el único sitio es el párrafo marcador
`[[PENDIENTE…]]` de §16.6.2.2 (en la v1.0 no existe el párrafo de "decisión pendiente";
el marcador cuelga directo del párrafo de los tres ejes de la Disposición 10/2015, que es
marco y **no se toca** — ahí la cita s. f.-b sobrevive y no hay baja bibliográfica).

**En §17.4 no hay nada que tocar** (verificado 09-01: cero menciones a AAIP/inscripción —
el "documentar en §17.4" del marcador nunca se materializó).

## 3. Sitios en §17.1 — APLICADOS (v1.7 → v1.8) · acta

Documento: `desarrollando/E-OVRT-VDP_Seccion_17.1_Consolidacion_Metodologica_v1.8.docx`
(la v1.7 pasó a `archivado/`). Edición byte a byte sobre `word/document.xml` (mismo
mecanismo del pase 6); el resto de las entradas del zip, byte-idénticas. Ninguno de los
dos párrafos tenía anclas de comentario (verificado antes de tocar).

- **A1** · §17.1.10.1, párrafo p0405: borrada la oración final
  ` Ese régimen contempla, además, requisitos administrativos asociados a las bases de datos con datos personales ante la autoridad de aplicación (AAIP), cuya aplicabilidad al contexto experimental debe determinarse; la decisión y el recaudo adoptado se documentan a continuación.`
  El párrafo queda cerrando en "…(Argentina, 2000; Disposición 10/2015, 2015)." — sin
  impacto bibliográfico (la mención "(AAIP)" era sigla suelta, sin cita formal).
- **A2** · p0406: borrado entero el párrafo marcador `[[PENDIENTE: …]]` (idéntico a B2).

**Compuerta (verificada sobre la v1.8):** `AAIP` 0 · `[[PENDIENTE` 0 ·
"Ese régimen contempla" 0 · **76 oMath** · **27 commentReference** · **0 marcas de
revisión** (`w:ins`/`w:del`) · "Disposición 10/2015" conservada en p0405 ·
`verificar_entregable.py` OK · diff = exactamente los dos sitios.

⚠ `herramientas/verificar_anclas_pase6.py --post` queda **histórico**: sus invariantes
"1 PENDIENTE" y el ancla AAIP describían la v1.7; sobre la v1.8 fallan por diseño.

## 4. Derivados actualizados en el mismo movimiento

- `90f` re-extraído de la v1.8 · generador del kit e `INSTRUCCIONES-PROJECT.md` a v1.8
  (la nota "el marcador AAIP sigue [[PENDIENTE]]" del slice del pase 6 → "D-E1-11 cerrada
  el 09-01") · kit regenerado, `--check` OK · tests del generador en verde.
- Tablero (`00-el-informe-hoy.md`) y `00-lo-que-resta.md` (§1.3 fila C9 · §3.1 · §6.2):
  D-E1-11 pasa de "pendiente del equipo" a **cerrada**.
