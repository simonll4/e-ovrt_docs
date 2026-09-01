# Lo que resta del informe — foto al 2026-09-01

> **Para qué existe este documento.** Después de la jornada del 08-31 (Etapa 2 cerrada con
> cinco pases) y del 09-01 (Etapa 1 v1.1 del colega + pase 6 de desacople normativo), el
> estado real quedó repartido entre varios banners. Esta es la lista única de lo que falta,
> con dueño y bloqueo, verificada contra los archivos —no contra la memoria— el 2026-09-01.
>
> **Qué NO es:** no reemplaza al tablero
> [`00-el-informe-hoy.md`](00-el-informe-hoy.md) (que narra la historia por jornada) ni al
> acta [`operacion/128`](../../operacion/128-acta-cierre-programa-experimental.md) (que
> cerró el programa experimental). Es el índice de pendientes; cuando un ítem cierra, se
> tacha acá y su constancia vive en el banner que corresponda.

---

## 0. Dónde estamos en una línea

El **programa experimental está cerrado** (acta 128) y **los insumos del informe están
todos cerrados** (datos, decisiones, 17 tablas, 6 figuras). Lo único activo es el **pase de
redacción**. De las tres secciones que estaban en juego, **§17.1 (Etapa 2) quedó cerrada
con seis pases** y **§15/§16 (Etapa 1) está en ciclo de revisión con el colega**. Lo que
falta se divide en cuatro frentes: terminar la Etapa 1, dos handoffs de voz, la
integración al maestro, y las tres secciones que no existen (§17.6, §18, §19).

**Estado por sección** (documento vigente en `desarrollando/`):

| Sección | Documento vigente | Pases | Estado |
|---|---|---|---|
| §15 + §16 Estado del arte y Marco teórico | `…Secciones_15_y_16_…_v1.1.docx` | 5 + revisión del colega | 🔄 **frente activo** |
| §17.1 Consolidación metodológica | `…Seccion_17.1_…_v1.7.docx` | **6** (el 6.º: desacople normativo, 09-01) | ✅ cerrada |
| §17.3 Diseño arquitectónico | `…Seccion_17.3_…_v1.4.docx` | 3 | ⚠ handoff pendiente → v1.5 |
| §17.4 Implementación | `…Seccion_17.4_…_v1.6.docx` | 3 | ✅ cerrada (1 `[[PENDIENTE]]`) |
| §17.5 Evaluación y validación | `…Seccion_17.5_…_v1.3.docx` | 3 | ✅ cerrada |
| §17.6 · §18 · §19 | — | — | ❌ **sin redactar** |

---

## 1. Frente activo — cerrar la Etapa 1 (§15/§16)

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
| **C9** | inscripción AAIP: "yo lo sacaría" | ⚠ **No sacar sin cerrar D-E1-11** (ver §3.1). Si se borra solo acá, el espejo de §17.1 queda huérfano |

### 1.4. Efecto bibliográfico de la Etapa 1 (para la integración)

Si la poda se confirma —ya está firmada—, salen del listado global: **Decreto 351/79 ·
Res. SRT 51/97 · Res. SRT 35/98 · ISO 45001 (ISO 2018) · Decreto 1558/2001**. Ley 19.587,
Dec. 911/96, Ley 25.326 y Disp. 10/2015 **se quedan** (las sostienen las nuevas §16.2/§16.6).

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
  [`justificacion-extension-17-1.md`](desarrollando/justificacion-extension-17-1.md). Lo
  descartado (~3.100 w) se paga en defensa, no se vuelve a discutir.

---

## 3. Handoffs abiertos

### 3.1. D-E1-11 — inscripción ante la AAIP · **dueño: el equipo**

Es el único pendiente que **atraviesa dos secciones** y el más sensible ante el jurado (el
pase 3 lo llamó "exactamente el hilo del que un jurado tira": el proyecto **sí** grabó
personas).

- **Estado:** marcador `[[PENDIENTE]]` en **§16.6.1** (Etapa 1 v1.1) y su **espejo** en
  **§17.1.10.1** (v1.7, párrafo p0405-406). Ambos intactos y alineados: la v1.7 ya dice
  "requisitos administrativos… cuya aplicabilidad debe determinarse", igual que §16.6.
- **Qué hace falta:** una decisión de una oración del equipo — por qué el contexto
  experimental acotado y académico no dispara la inscripción, y qué recaudo se tomó.
- **Cierre:** los **dos** marcadores a la vez (§16.6 y §17.1), más lo que corresponda en
  §17.4. Si se borra uno solo, el otro queda prometiendo algo que no llega.

### 3.2. §17.3 → v1.5 · **dueño: el redactor de la etapa 3**

Handoff vivo desde el pase 4 de la Etapa 2, sin aplicar: **E3-42** (hacer nacer
E-DIR/E-IND/E-HYB en §17.3.6.4, porque la cita a etapa 2 era falsa) + **3 sitios de voz
D-P3-9** + **11 metadiscursos** + **2 párrafos gordos**.

### 3.3. Bibliografía y numeración global · **dueño: la integración**

- **Baja:** Res. SRT 299/2011 (D-P6-3) — verificado: cero apariciones en §15/§16 v1.1,
  §17.1 v1.7, §17.3, §17.4 y §17.5.
- **Bajas de la Etapa 1:** las cinco de §1.4.
- **Listado global:** `90e` tiene **83 entradas**; hay que aplicarle las bajas y confirmar
  que no queden huérfanas ni citas sin entrada.

### 3.4. Marcador de procedencia en §17.4 · **dueño: el usuario**

`[[PENDIENTE: dirección de origen y fecha de acceso por clip del lote de obra real]]` —
depende de **C1** (§5), que está diferido a post-entrega. Es el mismo dato.

---

## 4. La integración al documento maestro

El maestro (`E-OVRT-VDP_v1.1_05062026-sin-indice.docx`) todavía tiene §17.3/§17.4 en
versión previa y §17.5 vacía. Cada sección se trabajó **en su propio `.docx`**; falta
juntarlas. Lo que hay que resolver al integrar:

**4.1. Numeración global de tablas — verificada el 09-01:**

| Tramo | Tablas | Observación |
|---|---|---|
| §11–§14 | 1 | frontmatter/plan |
| §15 + §16 | **2–11** | 10 tablas (la vieja Tabla 12 se eliminó en la v1.1) |
| *hueco* | **12–15** | ⚠ **4 números libres** — §17.2 (Costos asociados) no tiene tablas |
| §17.1 | **16–35** | 20 tablas, contiguas |
| *hueco* | **36–38** | ⚠ 3 números libres |
| §17.3 | **39–55** | 17 tablas |
| §17.4 | **56–61** | 6 tablas |
| §17.5 | **62–67** | 6 tablas |

Hay que decidir si se renumera todo de corrido o se documentan los dos huecos. **No se
toca ahora**: es trabajo de integración, y renumerar antes de tiempo rompe las remisiones
internas de cada documento.

**4.2. Anexos:** los **Anexos C y D** viajan al final del propio `.docx` de §17.1 (D-P3-8)
y hay que mudarlos a **§19.3/§19.4**; el **Anexo A** (Tablas A.1 y A.2) vive en `90e` y va
a **§19.1** — si no llega, quedan **dos remisiones colgadas** en §15.2.3 y §15.3.3.

**4.3. Nombres de métrica:** en el cuerpo de §17.1 son objetos de ecuación de Word (76) y
en las tablas de los anexos son texto plano. Unificar al integrar.

**4.4. Las figuras:** las **cinco** que faltaban están producidas en `informe/figuras/`
(PNG a 300 dpi + SVG donde aplica; ancho de diseño **16 cm** — insertar a ese ancho y **no
reescalar**, que es donde se eligieron los tamaños de letra), y **FIG-D** ya estaba en
disco. Pero **pegarlas sigue pendiente** en todos los casos. Destinos: **FIG-A → §17.4.1**
· **FIG-E → §17.3.8.2** · **FIG-B, FIG-C, FIG-F → §17.5**. Tres advertencias de cita del
README: la distribución en línea es **continua** · el orden de arranque es **inverso al
flujo de datos** · la máquina es de **5 estados con reapertura a `candidate`**.

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

Los 37 de `docs` son el trabajo del **08-31 y 09-01**: la §17.1 v1.7 y su historial en
`archivado/` (v1.0–v1.6 y los pases 3 a 6), la Etapa 1 v1.1 del colega, `90f` y `90g`, el
kit regenerado con `INSTRUCCIONES`, el generador, el tablero, `ajustes/02` y las dos
herramientas nuevas (`aplicar_pase6.py`, `verificar_anclas_pase6.py`).

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

1. **Decidir los 10 comentarios de la Etapa 1** (§1.3) — es lo único que bloquea el frente
   activo. Con eso escribo el pase y lo aplico con la misma cadena del pase 6.
2. **Firmar D-E1-11 (AAIP)** (§3.1) — una oración, y cierra los dos marcadores juntos.
3. **Aplicar el handoff de §17.3 → v1.5** (§3.2).
4. **Escribir §17.6, §18 y §19** — las tres que no existen.
5. **Integración al maestro** (§4): anexos, numeración de tablas, figuras, bibliografía.
6. Post-entrega (§5), mientras se esperan correcciones del jurado.
