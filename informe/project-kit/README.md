# Kit mínimo para el Project de ChatGPT

Este directorio contiene el paquete versionado para desarrollar el informe final en
ChatGPT Web. Reemplaza al kit externo aplanado de 95 archivos. Los documentos generados
son derivados: las fuentes de verdad siguen siendo este repositorio y los índices de
`e-ovrt_experimental-setup/results/`.

## Qué se carga

*(✎ 2026-08-16 — el knowledge pasó de dos a **cuatro archivos**: se suman los dos DOCX
del entregable, por decisión del usuario; ver `operacion/122` §6-ter.)*

El knowledge del Project usa **cuatro archivos**:

1. `00-contexto-base.md`: reglas, estado técnico vigente, limitaciones y cifras citables.
2. `01-etapa-activa.md`: texto e insumos de una sola etapa del informe.
3. `informe/entregable/E-OVRT-VDP_v1.1_05062026-sin-etapa3.docx`: el informe base —
   autoridad de formato, estilos y estructura; su §17.3 está vaciada a propósito.
4. `informe/entregable/E-OVRT-VDP_Etapa_3_Diseno_Arquitectonico.docx`: la §17.3
   **vigente** (la embebida en el v1.1 completo quedó desactualizada — nunca subir el
   `E-OVRT-VDP_v1.1_05062026-sin-indice.docx` completo por esa razón).

Los dos `.md` cambian por etapa; los dos DOCX son estables. `INSTRUCCIONES-PROJECT.md`
se pega en **Project settings → Instructions**. No se carga como archivo. `README.md`,
el generador y sus pruebas tampoco se suben.

## Primera carga

*(✎ 2026-08-16 — antes acá se recomendaba arrancar por la etapa 1, porque construye la
vara bibliográfica que necesita §17.5. **Esa vara ya está redactada** —el borrador
`entregable/borradores/vara-15.md`, que además viaja dentro de los paquetes de las
etapas 1 y 5—, así que el camino crítico se corrió a los capítulos nuevos.)*

La etapa inicial recomendada es la **4**: el §17.4 tiene borrador completo y es el más
barato de cerrar. El orden del manual (`informe/ajustes/08` §3) para este carril es
**4 → 5 → 6**, y recién después las correcciones de prosa (etapa 3 por el usuario;
etapas 1, 2 y 0 por los colegas).

```bash
python3 herramientas/generar_project_kit.py --etapa 4
python3 herramientas/generar_project_kit.py --etapa 4 --check
```

Después:

1. Pegar `INSTRUCCIONES-PROJECT.md` en las instrucciones del Project.
2. Subir los cuatro archivos del knowledge (los dos `.md` de este directorio y los dos
   DOCX de `informe/entregable/`).
3. Abrir un chat nuevo para la sección que se va a trabajar.

## Cambiar de etapa

Eliminar del Project únicamente el `01-etapa-activa.md` anterior, generar el nuevo y
subirlo con el mismo nombre. El contexto base y los dos DOCX permanecen cargados.

| Etapa | Secciones | Comando |
|---:|---|---|
| 0 | §11–§14 | `python3 herramientas/generar_project_kit.py --etapa 0` |
| 1 | §15, §16 y Anexo A | `python3 herramientas/generar_project_kit.py --etapa 1` |
| 2 | §17.1 y Anexos C/D | `python3 herramientas/generar_project_kit.py --etapa 2` |
| 3 | §17.3 | `python3 herramientas/generar_project_kit.py --etapa 3` |
| 4 | §17.4 | `python3 herramientas/generar_project_kit.py --etapa 4` |
| 5 | §17.5 | `python3 herramientas/generar_project_kit.py --etapa 5` |
| 6 | §17.6, §18 y §19 | `python3 herramientas/generar_project_kit.py --etapa 6` |

Tras generar, ejecutar el mismo comando con `--check`, por ejemplo:

```bash
python3 herramientas/generar_project_kit.py --etapa 5 --check
```

## Reglas de mantenimiento

- No editar `00-contexto-base.md` ni `01-etapa-activa.md` a mano.
- Cambiar primero la fuente canónica y regenerar después.
- Cada bloque generado registra ruta, selección y SHA-256 de la fuente incorporada.
- `--check` falla ante deriva, fuentes ausentes, enlaces relativos o límites de tamaño.
- Límites internos: 500 KiB para el contexto y 750 KiB para la etapa.
- Al cerrar una sección en Google Docs, reextraer su texto antes de usarlo como base de
  otra sesión, según `informe/ajustes/08-manual-de-aplicacion.md`.

## Verificación del generador

```bash
python3 -m unittest herramientas.tests.test_generar_project_kit -v
```

El kit externo `../informe-project-kit/` fue eliminado. Su manifiesto anterior se conserva
solo como registro histórico en `informe/ajustes/gobierno/98-*`.
