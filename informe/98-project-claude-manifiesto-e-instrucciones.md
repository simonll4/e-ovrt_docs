# 98 — Project de claude.ai: manifiesto de archivos e instrucciones

- **Fecha:** 2026-07-18
- **Propósito:** definir qué archivos del set se suben al knowledge del Project de
  claude.ai para redactar el informe final, y las instrucciones (custom instructions)
  del Project, listas para pegar. El paquete físico se genera en
  `~/projects/informe-project-kit/` (copias planas, regenerables desde este manifiesto).

---

## 1. Manifiesto de archivos

Los nombres se aplanan con prefijo de carpeta (`operacion-56-...md`) porque el
knowledge del Project no tiene carpetas.

### Nivel 1 — obligatorios (el corazón del Project)

| Archivo | Rol en la redacción |
|---|---|
| `13-glosario-y-convenciones-de-lectura.md` | Siglas + jerarquía de verdad. **El asistente debe leerlo primero.** |
| `informe/97-brief-de-redaccion.md` | Las reglas de redacción (registro, fuentes, honestidad). |
| `operacion/56-relevamiento-plataforma-2026-07-18.md` | El estado actual verificado de la plataforma. |
| `informe/92-anexo-concrecion-tecnica.md` | La fuente única de cifras, contratos y APIs (ruta:línea). |
| `informe/93-redlines-etapa3.md` | El tablero de trabajo: los 24 redlines con casillas. |
| `informe/94-secciones-nuevas-etapa3.md` | Texto ya redactado en registro de informe (modelo de estilo). |
| `informe/91-relevamiento-etapa3-vs-implementacion.md` | Qué contradice/falta en el capítulo, con plan A–D. |
| `informe/95-auditoria-y-plan-de-cierre.md` | Plan de cierre, orden de sacrificio, reglas anti-error. |
| `informe/90-etapa3-texto-extraido.md` | La Etapa 3 **vigente** (texto a corregir). |
| `informe/96b-informe-v11-17-1-consolidacion-metodologica.md` | El protocolo (§17.1) contra el que todo se lee. |
| `informe/96a-informe-v11-frontmatter-intro-objetivos-plan.md` | Intro, objetivos, etapas: el marco del documento. |
| `nucleo/10-registro-alcance-y-exclusiones.md` | El alcance cerrado y las exclusiones E-01…E-13. |
| `decisiones/README.md` + los 14 ADRs | Las decisiones formalizadas y sus porqués. |
| `decisiones/estado-de-implementacion-adrs.md` | **El cierre decisión→implementación**: cómo quedó implementado cada ADR, vista por tema y condicionales resueltos. Leer SIEMPRE junto a los ADRs. |

### Nivel 2 — recomendados (contexto de diseño y defensa)

| Archivo | Rol |
|---|---|
| `nucleo/02-revision-critica-etapa3-y-norte.md` | El norte, R1–R4, plan de 12 semanas. |
| `nucleo/03-spec-plataforma-dos-caminos.md` | Documento rector de las dimensiones D1–D6. |
| `nucleo/04-diseno-comparativo-estrategias-edir-eind.md` | Pre-registro del experimento D1. |
| `nucleo/08-alineacion-consolidacion-metodologica.md` | Cómo el set se alinea con la §17.1. |
| `nucleo/09-justificacion-ovd-y-defensa.md` | Los 5 argumentos, Q&A hostil, cierre del informe. |
| `nucleo/12-diseno-prompts-y-fusion-ehyb.md` | Prompt sets, comparabilidad, fusión E-HYB, pista doble. |
| `specs/40…45 + README` | Lo especificado por módulo (leer como "lo pedido"; el 56 dice lo construido). |
| `operacion/54-video-gt-lab-y-contrato-gt.md` | El laboratorio de GT y el contrato `clip_gt.v2`. |
| `operacion/55-como-continuar.md` | Los pasos pendientes con comandos. |
| `operacion/57-validacion-metodologica-externa-duracion-clips.md` | Validación de la duración de clips contra i-LIDS/TRECVID: duración bimodal, plantillas de grabación, gaps accionables. Leer antes de escribir la sección de metodología de grabación del banco. |
| `informe/96e-informe-v11-cierre-anexos-referencias.md` | Anexos y referencias del documento. |

### Nivel 3 — opcionales (subir solo si el capítulo lo requiere)

| Archivo | Cuándo |
|---|---|
| `informe/96c-informe-v11-estado-del-arte.md` (21k palabras) | Solo al retocar §15 o citar modelos. |
| `informe/96d-informe-v11-marco-teorico.md` (32k palabras) | Solo al retocar §16 o alinear terminología teórica. |
| `operacion/31-benchmark-modelos-host-local.md` | Al redactar la selección de modelos. |
| `operacion/37/38/39/51/52/53` | Al redactar la sección de verificación E2E con detalle. |
| `nucleo/01/05/06/07/11`, `contingencia/20` | Consulta puntual; en general el 56/92 los resumen. |

**No subir:** los `.docx` (pesados y mal indexables — su texto ya está en 90/96),
`operacion/datos/*` (JSON crudo; las cifras citables ya están en 92/97),
`herramientas/`, docs históricos 32/36/50.

## 2. Instrucciones del Project (pegar en "Custom instructions")

```
Sos el asistente de redacción del informe final (TFG) del proyecto E-OVRT-VDP:
una plataforma experimental de detección open-vocabulary de riesgos de seguridad
en construcción. El knowledge contiene la documentación completa del proyecto.

REGLAS DE LECTURA (obligatorias):
1. Leé primero "13-glosario-y-convenciones-de-lectura" (siglas y jerarquía de
   verdad) y "97-brief-de-redaccion" (reglas de redacción). Todo lo que escribas
   debe cumplirlas.
2. Jerarquía de verdad sobre el estado de la plataforma: doc 56 > banners "✎" de
   cualquier doc > doc 92 (cifras/contratos) > el resto. Los docs con banner son
   fotos históricas: NUNCA cites su cuerpo como estado actual.
3. Cifras: solo las del doc 92 o del doc 56 §9. Si un número no está ahí, decí
   que no hay artefacto y no lo uses. Nunca inventes números, rutas ni nombres
   de campos.
4. Las métricas del clip bench provienen de un GT preliminar sin pasada humana:
   presentalas siempre como verificación de mecánica, jamás como resultado final.
5. Las decisiones ADR-001…014 están cerradas: se declaran y justifican, no se
   re-litigan. La tesis NO es "OVD detecta mejor" (ver doc 09): es la plataforma
   que mide qué se logra especificando condiciones en lenguaje, sin entrenar.

CÓMO TRABAJAR:
- El texto del informe vive en Google Docs; acá se produce texto listo para
  pegar, en registro formal impersonal (modelo: doc 94), en español.
- Para cada sección: buscá el redline correspondiente en el doc 93, la evidencia
  en el 92/56, y el borrador previo en el 94. Entregá el texto final + qué
  redline queda saldado (R-NN).
- Terminología y nombres de artefactos exactamente como en el glosario; los
  identificadores técnicos en monoespaciado y sin traducir.
- Lo no implementado se declara honestamente (doc 91 §7); las métricas que no
  aplican usan los estados de aplicabilidad del ADR-006/013.
- Si encontrás una contradicción entre documentos, señalala y resolvela por la
  jerarquía del punto 2; si no se puede, dejala registrada como pendiente.
```

## 3. Flujo de trabajo sugerido en el chat

1. **Sesión inicial:** pedir al asistente un plan de redacción a partir del doc 95
   (plan de cierre) + doc 93 (tablero de redlines), priorizado por bloques A–D.
2. **Por sección:** "redactá la sección que salda R-NN" → pegar en Google Docs →
   marcar la casilla en el doc 93 local.
3. **Al llegar resultados nuevos** (pasada humana del GT, corridas del banco): se
   actualiza el doc 92 y se re-sube al Project esa única pieza; el resto no cambia.
4. **Regenerar el paquete** tras cambios en `docs/`: copiar según el manifiesto §1
   (o pedir a Claude Code que lo regenere).
