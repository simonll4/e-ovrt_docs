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

> ✎ **2026-08-19 — pase de cierre de §17.3/§17.4 en curso.** Las versiones de trabajo
> VIGENTES de ambas secciones son los `.docx` v0.1 de [`desarrollando/`](desarrollando/)
> (con los comentarios del autor), y las correcciones firmadas para cerrarlas están en
> [`desarrollando/correcciones-etapa-3-4.md`](desarrollando/correcciones-etapa-3-4.md).
> El standalone `E-OVRT-VDP_Etapa_3_Diseno_Arquitectonico.docx` (16-08) queda como
> versión PREVIA de §17.3. Al cerrar cada sección en el maestro: re-extraer su `.md` y
> fechar acá (regla D-C).

## El texto extraído

| Archivo | Qué contiene | Etapa del plan |
|---|---|---|
| `96a-informe-v11-frontmatter-intro-objetivos-plan.md` | frontmatter, §11 Glosario, §12 Introducción, §13 Objetivos, §14 Plan de trabajo (**§14.2 define las etapas**) | transversal |
| `96c-informe-v11-estado-del-arte.md` | **§15 Estado del Arte** | **1** |
| `96d-informe-v11-marco-teorico.md` | **§16 Marco Teórico** | **1** |
| `96b-informe-v11-17-1-consolidacion-metodologica.md` | **§17.1 Consolidación Metodológica** + §17.2 Costos | **2** |
| `90-etapa3-texto-extraido.md` | **§17.3 Diseño arquitectónico**, §17.3.1 a §17.3.18 | **3** |
| `96e-informe-v11-cierre-anexos-referencias.md` | §17.4–§17.6 (**los tres placeholders**), §18 Cierre, §19 Anexos A–D, Referencias | 4, 5, 6 |

---

## Lo que está vacío, y es lo que importa

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
