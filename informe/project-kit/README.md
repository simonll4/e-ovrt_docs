# Kit mínimo para el Project de ChatGPT

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
3. `informe/entregable/E-OVRT-VDP_v1.1_05062026-sin-etapa3.docx`: el informe base —
   autoridad de formato, estilos y estructura; su §17.3 está vaciada a propósito.
4. El `.docx` **vigente** de la sección en trabajo (✎ 2026-08-22 — hoy viven en
   `informe/entregable/desarrollando/`): para la etapa 3,
   `E-OVRT-VDP_Seccion_17.3_Diseno_Arquitectonico_v1.1.docx`; para la etapa 4,
   `E-OVRT-VDP_Seccion_17.4_Implementacion_v1.2.docx` — ambos con el pase 1 ya aplicado.
   Para las demás etapas este cuarto archivo no aplica (salvo que la etapa tenga sección
   propia cerrada). El histórico `E-OVRT-VDP_Etapa_3_Diseno_Arquitectonico.docx`
   (16-08, PREVIO al pase 1) quedó superado y **no se sube**; tampoco se sube nunca el
   `E-OVRT-VDP_v1.1_05062026-sin-indice.docx` completo (su §17.3 embebida está
   desactualizada).

El contexto base y el DOCX de formato son estables entre etapas. `INSTRUCCIONES-PROJECT.md`
se pega en **Project settings → Instructions**. No se carga como archivo. `README.md`,
el generador y sus pruebas tampoco se suben.

## Primera carga

**Estado que define el orden (✎ 2026-08-23):**

| Sección | Estado | Trabajo que queda |
|---|---|---|
| §17.3 | **v1.4** — tres pases aplicados y verificados | revisión del autor · figuras · integrar al maestro |
| §17.4 | **v1.5** — tres pases aplicados y verificados | revisión del autor · URLs del lote · integrar al maestro |
| §17.5 | **v1.3** — redactada bajo D-P3-6 y verificada | revisión del autor · figuras · integrar al maestro |
| §17.6 · §19 | vacías | redactar desde cero |
| §18 | vacía | redactar **después** de cerrar §17.5: interpreta lo que ella reporta |
| §15 · §16 · §17.1 · §11–§14 | escritas | correcciones de prosa y poda — **al final**, por decisión del usuario |

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

**Orden recomendado de lo que queda: 6 → 1 → 2 → 0**, con §17.6 y §19 antes que §18.

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
