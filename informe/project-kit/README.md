# Kit mínimo para el Project de ChatGPT

> ✎ **2026-09-18 — KIT HISTÓRICO.** Cumplió su función: el informe está completo
> (`../entregable/desarrollando/E-OVRT-VDP_Informe_Final_2026-09-16_v0.1.docx`). **No se regenera ni
> se vuelve a cargar**; los `.docx` de sección que menciona abajo ya están en
> `../entregable/desarrollando/archivado/`. El generador (`herramientas/generar_project_kit.py`) y sus
> tests se conservan por si hiciera falta armar un kit para las correcciones del jurado, con el informe
> final como único `.docx` de referencia.

Este directorio contiene el paquete versionado para desarrollar el informe final en
ChatGPT Web. Reemplaza al kit externo aplanado de 95 archivos. Los documentos generados
son derivados: las fuentes de verdad siguen siendo este repositorio y los índices de
`e-ovrt_experimental-setup/results/`.

## Qué se carga

*(✎ 2026-08-16 — el knowledge pasó de dos a **cuatro archivos**: se suman los dos DOCX
del entregable, por decisión del usuario; ver `operacion/122` §6-ter.)*

*(✎ 2026-08-17 — el archivo de etapa dejó de tener nombre único: cada etapa genera
`01-etapa-<N>-activa.md`, así que regenerar una no pisa el paquete de otra. Se puede
tener las siete escritas en disco al mismo tiempo; lo que sigue siendo cuatro es lo que
se **sube al Project** — un archivo de etapa por vez.)*

El knowledge del Project usa **cuatro archivos**:

1. `00-contexto-base.md`: reglas, estado técnico vigente, limitaciones y cifras citables.
   Es el mismo para las siete etapas.
2. `01-etapa-<N>-activa.md` (`N` = 0…6): texto e insumos de una sola etapa del informe.
   Subí solo el de la etapa que estás trabajando.
3. **El `.docx` maestro como autoridad de formato, estilos y estructura.** ✎ **2026-09-08 —
   cambió cuál es, y el que este README nombraba ya no está en esa ruta.** Hasta el 09-07 era
   `E-OVRT-VDP_v1.1_05062026-sin-etapa3.docx`, que se archivó junto con las demás variantes
   superadas y hoy vive en `informe/entregable/archivado/` con su paréntesis. **El vigente es
   `informe/entregable/archivado/E-OVRT-VDP_v1.1_05062026-sin-indice.docx`**, el export del
   09-08: es el informe completo y el destino de la integración. Pesa 12 MB; si la carga lo
   rechaza por tamaño, subí la variante archivada, que pesa 2,3 MB y sirve igual como autoridad de
   formato.

   ⚠ Al usarlo hay que saber que **sus §15, §16, §17.1 y §17.3 son las versiones viejas**,
   superadas por los textos que el propio paquete de etapa ya trae. Se sube por su formato y su
   estructura, no por su contenido de esas cuatro secciones.
4. El `.docx` **vigente** de la sección en trabajo, que vive en
   `informe/entregable/desarrollando/` (✎ 2026-08-28 — tabla al día; la versión anterior de
   este README nombraba `E-OVRT-VDP_Seccion_17.3_Diseno_Arquitectonico_v1.1.docx` y
   `E-OVRT-VDP_Seccion_17.4_Implementacion_v1.2.docx`, que **ya no existen en disco**;
   `operacion/130` §5 / `docs-set.md` #3):

   | Etapa | `.docx` vigente en `desarrollando/` (✎ 2026-09-08) | Estado |
   |---:|---|---|
   | 1 | `E-OVRT-VDP_Secciones_15_y_16_Estado_del_Arte_y_Marco_Teorico_v1.4.docx` | pase 5 aceptado; **en revisión de los colegas** (9 comentarios, 1 sugerencia sin resolver) |
   | 2 | `E-OVRT-VDP_Seccion_17.1_Consolidacion_Metodologica_v1.21.docx` | **CERRADA**, limpia |
   | 3 | `E-OVRT-VDP_Seccion_17.3_Diseno_Arquitectonico_v1.12.docx` | **CERRADA**, limpia |
   | 4 | `E-OVRT-VDP_Seccion_17.4_Implementacion_v1.15.docx` | **CERRADA**; 3 comentarios abiertos, sin marcas |
   | 5 | `E-OVRT-VDP_Seccion_17.5_Evaluacion_y_Validacion_v1.5.docx` | **CERRADA**, limpia. ⚠ el archivo dice v1.5 pero su contenido es el de la v1.9 |
   | 0 · 6 | — | sin documento de trabajo propio: la Etapa 6 escribe §17.6/§18/§19 y el paquete `01-etapa-6-activa.md` ya trae los cinco textos cerrados; el cuarto archivo no aplica |

   ⚠ El maestro tiene dos exports en disco y traen el mismo contenido: el del 09-08, en
   `desarrollando/`, y el del 08-16, en `entregable/archivado/`. Se distinguen en un detalle que
   importa para cualquier herramienta que los procese: **el nuevo nombra sus estilos de título
   `Ttulo1`…`Ttulo5` y el viejo `Heading1`…`Heading5`**, porque Google Docs los nombra según el
   idioma de la interfaz.

   Las versiones anteriores de cada sección están en `desarrollando/archivado/` y **no se suben**.
   El histórico `E-OVRT-VDP_Etapa_3_Diseno_Arquitectonico.docx` (16-08, PREVIO al pase 1) quedó
   superado y **no se sube**.

5. **`informe/figuras/GUIA-DE-FIGURAS.md`** — el quinto archivo, ✎ **nuevo el 2026-09-08**. Se sube
   **sólo cuando la etapa tiene que producir o rehacer figuras**. Define un sistema visual único
   para las seis figuras del informe (superficie, paleta, tipografía, geometría, flechas, tamaño y
   exportación) y después especifica cada una: qué debe mostrar, con qué rótulos exactos y con qué
   trampas. **Regla que trae y conviene no saltear: las figuras se piden como código vectorial
   —SVG o un script de graficación—, nunca como imagen de un modelo de imagen**, que deforma el
   texto de los rótulos. Trae además una corrección de fondo verificada contra el código: la
   máquina de estados de la Figura 4.3 dibuja hoy dos transiciones que el sistema no hace.

El contexto base y el DOCX de formato son estables entre etapas. `INSTRUCCIONES-PROJECT.md`
se pega en **Project settings → Instructions**. No se carga como archivo. `README.md`,
el generador y sus pruebas tampoco se suben.

### Qué subir para la Etapa 6, que es la activa (✎ 2026-09-08)

```
1. informe/project-kit/00-contexto-base.md
2. informe/project-kit/01-etapa-6-activa.md
3. informe/entregable/archivado/E-OVRT-VDP_v1.1_05062026-sin-indice.docx
4. informe/figuras/GUIA-DE-FIGURAS.md          ← sólo si además se van a producir figuras
```

Son cuatro porque la Etapa 6 **no tiene documento de trabajo propio**: escribe §17.6, §18 y §19
directamente sobre los marcadores del maestro, y los cinco textos cerrados que necesita para
apoyarse ya viajan dentro de `01-etapa-6-activa.md`.

## Primera carga

**Estado que define el orden (✎ 2026-09-08; antes 2026-08-28 — fuente `informe/entregable/00-lo-que-resta.md`):**

| Sección | Estado | Trabajo que queda |
|---|---|---|
| §15 · §16 | **v1.4** — cinco pases E1 + revisión del colega + pase 5, aceptado el 09-08 | cerrar la revisión de los colegas en Google Docs (9 comentarios) · integrar al maestro |
| §17.1 | **v1.21 CERRADA** — seis pases + reestructuración + pases 5/5d/5e aceptados el 09-08 | integrar |
| §17.3 | **v1.12 CERRADA** — cuatro pases + pases 5/5d aceptados el 09-08 | agregar el título «17.3» al integrar |
| §17.4 | **v1.15 CERRADA** — pases 5/5b/5c/5d/5e aceptados el 09-08 | integrar · la ficha por video del lote depende de C1 |
| §17.5 | **CERRADA** — pases 5/5b/5d aceptados el 09-08 (archivo «v1.5», contenido de la v1.9) | integrar |
| §17.6 · §19 | vacías | redactar desde cero — **Etapa 6, AHORA** |
| §18 | vacía | redactar sobre §17.5 cerrada: interpreta lo que ella reporta |
| §11–§14 | escritas | correcciones de prosa (Etapa 0) — **al final**, por decisión del usuario |

**Cada sección se trabaja en su propio documento** (decisión del usuario, 2026-08-23): los
`.docx` de `entregable/desarrollando/` son la versión de trabajo de §17.3, §17.4 y §17.5, y
la integración al maestro se resuelve **después**, cuando cada una cierre individualmente.
Por eso el texto base de cada etapa es su extracción (`90` / `90b` / `90c`) y **no** el
placeholder del maestro: el maestro todavía tiene §17.3/§17.4 en su versión previa y §17.5
vacía.

⚠ **Los tres pases de corrección ya están aplicados. NO se re-aplican**: entran al kit como
criterio de lectura (sus decisiones D1–D4, D-P2-1…6 y D-P3-1…6 siguen rigiendo), no como
lista de tareas. Re-aplicarlos sobre texto ya corregido es exactamente la falla de
integración que costó una pasada completa el 2026-08-23.

**Orden de trabajo vigente (✎ 2026-09-08): Etapa 6 AHORA** (§17.6, §18 y §19: las cinco
secciones del desarrollo cerraron el 09-08), después la **integración al maestro** y por último
la **Etapa 0** (§11–§14). *(Antes, desde el 08-28: 2 → 6 → 0.)* El paquete de la Etapa 6 lleva
dentro los cinco textos cerrados (`90c` y `90b` completos; las conclusiones parciales de §16,
§17.1 y §17.3; §12–§13 del informe v1.1), así que §18 se escribe leyendo, no recordando.

```bash
python3 herramientas/generar_project_kit.py --etapa 6
python3 herramientas/generar_project_kit.py --etapa 6 --check
```

Después:

1. Pegar `INSTRUCCIONES-PROJECT.md` en las instrucciones del Project.
2. Subir los archivos del knowledge: `00-contexto-base.md`, el `01-etapa-<N>-activa.md` de
   la etapa, `entregable/E-OVRT-VDP_v1.1_05062026-sin-etapa3.docx` (formato) y, si la etapa
   tiene documento de trabajo, ese `.docx` de `entregable/desarrollando/`.
3. Abrir un chat nuevo para la sección que se va a trabajar.

## Cambiar de etapa

Como cada etapa tiene su propio nombre de archivo, generar una no borra ni pisa la de
otra — las siete pueden convivir en `informe/project-kit/`. Lo que hay que mover es lo
que está **subido al Project**: eliminar ahí el `01-etapa-<N>-activa.md` anterior y
subir el de la nueva etapa. Si el contexto base también cambió (columna "Comando" abajo
regenera los dos archivos siempre), reemplazarlo también.

| Etapa | Secciones | Archivo | Comando |
|---:|---|---|---|
| 0 | §11–§14 | `01-etapa-0-activa.md` | `python3 herramientas/generar_project_kit.py --etapa 0` |
| 1 | §15, §16 y Anexo A | `01-etapa-1-activa.md` | `python3 herramientas/generar_project_kit.py --etapa 1` |
| 2 | §17.1 y Anexos C/D | `01-etapa-2-activa.md` | `python3 herramientas/generar_project_kit.py --etapa 2` |
| 3 | §17.3 | `01-etapa-3-activa.md` | `python3 herramientas/generar_project_kit.py --etapa 3` |
| 4 | §17.4 | `01-etapa-4-activa.md` | `python3 herramientas/generar_project_kit.py --etapa 4` |
| 5 | §17.5 | `01-etapa-5-activa.md` | `python3 herramientas/generar_project_kit.py --etapa 5` |
| 6 | §17.6, §18 y §19 | `01-etapa-6-activa.md` | `python3 herramientas/generar_project_kit.py --etapa 6` |

Tras generar, ejecutar el mismo comando con `--check`, por ejemplo:

```bash
python3 herramientas/generar_project_kit.py --etapa 5 --check
```

Para regenerar las siete etapas de una sola vez (por ejemplo, después de que cambió una
fuente que las siete comparten, como el contexto base):

```bash
python3 herramientas/generar_project_kit.py --etapa all
python3 herramientas/generar_project_kit.py --etapa all --check
```

## Reglas de mantenimiento

- No editar `00-contexto-base.md` ni ningún `01-etapa-<N>-activa.md` a mano.
- Cambiar primero la fuente canónica y regenerar después.
- Cada bloque generado registra ruta, selección y SHA-256 de la fuente incorporada.
- `--check` falla ante deriva, fuentes ausentes, enlaces relativos o límites de tamaño.
- Límites internos: 500 KiB para el contexto y 750 KiB para cada etapa.
- **`INSTRUCCIONES-PROJECT.md` no puede pasar de 8.000 caracteres**: es el tope del
  cuadro de Project settings y al pegar no avisa — lo que sobra se pierde en silencio, y
  lo último del archivo es justamente el control final. El test de contrato lo verifica.
  Tampoco congela estado volátil: qué está cerrado y qué abierto lo fija el inventario
  del contexto base, que sí se regenera.
- Al cerrar una sección en Google Docs, reextraer su texto antes de usarlo como base de
  otra sesión, según `informe/ajustes/08-manual-de-aplicacion.md`.

## Verificación del generador

```bash
python3 -m unittest herramientas.tests.test_generar_project_kit -v
```

El kit externo `../informe-project-kit/` fue eliminado. Su manifiesto anterior se conserva
solo como registro histórico en `informe/ajustes/gobierno/98-*`.
