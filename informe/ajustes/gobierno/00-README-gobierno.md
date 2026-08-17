# `gobierno/` — cómo se redacta, no qué se corrige

Los cuatro documentos de esta carpeta **no son ajustes a una sección**: son las reglas y
los materiales que gobiernan el acto de redactar. Van juntos porque se aplican a todas las
etapas por igual.

| Doc | Qué es | Cuándo abrirlo |
|---|---|---|
| **`97-brief-de-redaccion.md`** | Registro y estilo · **jerarquía de fuentes** · **reglas de honestidad experimental (no negociables)** · mecánica de trabajo | **Antes de escribir la primera línea.** Su §3 es lo más importante del set para no sobrevender. |
| **`99-materiales-de-cierre.md`** | **Inventario T-68…T-84 y FIG-A…FIG-F** con su artefacto de origen · anexo de reproducibilidad (sha256 + comandos) · licencias, consentimientos y citas · **limitaciones L1–L8** · hallazgos abiertos | Al armar cualquier tabla o figura de resultados. Es el documento más referenciado del set. |
| **`98-project-claude-manifiesto-e-instrucciones.md`** | Manifiesto histórico del kit aplanado de 95 archivos, **reemplazado el 2026-08-12** | Solo para trazabilidad de la estrategia anterior. |
| **`informe/project-kit/README.md`** | Kit mínimo versionado para ChatGPT: contexto base + etapa activa, instrucciones y generador verificable | Al montar el Project o cambiar de etapa. |
| **`95-auditoria-y-plan-de-cierre.md`** | La auditoría adversarial de los docs 91–94 (produjo la v2 de los redlines y agregó R-25/R-26) | Consulta histórica. ⚠️ **Su §5 es un plan PRE-rodaje y quedó viejo: solo vive §5.5.** |

---

## Dos advertencias que valen para toda la carpeta

1. **`97` §5 quedó derogado como fuente de números.** Era una tabla de referencia rápida y
   se desactualizó. Las cifras salen de los cuatro índices de
   `e-ovrt_experimental-setup/results/`. Lo mismo aplica a `informe/92` §10,
   `operacion/92` y `operacion/56`.
2. **Un documento con banner ⚠️ o ✎ manda por el banner, no por el cuerpo.** Es la
   convención del set entero (`13-glosario` §1), y en esta carpeta importa especialmente:
   el `95` es un documento vigente solo en una de sus secciones.

## Si mové algo de acá

El flujo vigente está en [`informe/project-kit/README.md`](../../project-kit/README.md).
ChatGPT mantiene cuatro archivos en el knowledge (✎ 2026-08-16): los dos que el
generador compone desde las fuentes canónicas (contexto y etapa) más los dos DOCX del
entregable (informe sin §17.3 + Etapa 3 vigente). El antiguo `informe-project-kit/`,
externo al repo, fue eliminado.
