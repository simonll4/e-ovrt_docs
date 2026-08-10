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

> ✎ **ACTUALIZADO 2026-08-05.** Este manifiesto había quedado atrás del tramo
> experimental en tres puntos que importan, todos corregidos abajo: mandaba subir
> `operacion/56` (reemplazado por `operacion/97`), declaraba `informe/92` como **"la
> fuente única de cifras"** (derogado: las cifras salen de los cuatro índices de
> `results/`, ver doc 97 §2.1) y decía **24 redlines** cuando son **26** — R-25 y R-26 se
> agregaron después, y el propio doc 93 marca a R-26 como *"la más valiosa"*. Con el número viejo, un
> redactor se saltaba los dos mejores redlines sin enterarse.

> ✎ **ACTUALIZADO OTRA VEZ, 2026-08-10 — faltaba TODO el tramo de video.** Este manifiesto
> no listaba `docs/sintesis/` (donde vive la narrativa vigente y la escala AF) ni los docs
> `operacion/102`–`113` (el lote de internet, la revisión ciega del GT y el cierre).
> Agregados abajo. Y ojo con dos entradas de esta tabla: el **glosario** y el **brief**
> siguen siendo obligatorios, pero **los dos llevan hoy banners de corrección** — hay que
> leer esos banners, no solo el cuerpo.

| Archivo | Rol en la redacción |
|---|---|
| **`GUIA-REDACTORES.md`** | ✎ **AGREGADO 2026-08-10. La puerta de entrada del redactor externo** — el proyecto en 5 minutos, orden de lectura, qué NO abrir, cómo citar una cifra y las 5 trampas. **Leerlo ANTES que todo lo demás.** |
| **`sintesis/resultados-y-conclusiones.md`** | ✎ **AGREGADO 2026-08-10. La narrativa vigente de punta a punta**, con el estrato B integrado (§4.1 y §5.1) y la escala **AF-1…AF-11** con su columna de fuerza. **Es el documento por el que conviene empezar a leer.** |
| **`sintesis/fundamentos-teoricos.md`** | ✎ **AGREGADO 2026-08-10.** La teoría sin cifras: qué es OVD, los tres niveles de medición, por qué el diseño es el que es. **Lo más pedagógico del set** para alguien que no participó. |
| **`sintesis/inventario-de-metricas.md`** | ✎ **AGREGADO 2026-08-10.** Qué calcula la plataforma y en qué nivel. |
| **`operacion/109`, `111`, `112`, `113`** | ✎ **AGREGADOS 2026-08-10.** El tramo de video: fuente única del material (109), cierre del lote (111), balance crítico (112) y **la revisión ciega del GT + el cierre de brechas (113)**. Sin estos, el capítulo no puede contar el estrato B. |
| `13-glosario-y-convenciones-de-lectura.md` | Siglas + jerarquía de verdad + **§4.1/4.2/4.3: los códigos (`F-NN.N`, `D-NNN.N`, AF, L), los IDs de campaña y las tres colisiones de símbolos**. **Leerlo primero**, y prestar atención a sus banners ✎ de corrección. |
| `informe/97-brief-de-redaccion.md` | Las reglas de redacción (registro, fuentes, honestidad). ⚠️ **Su §5 quedó SUPERSEDIDA** (banco de 34, FAR/hora, lote sin GT): tiene banner de cabecera con la tabla de qué cambió. **Las cifras salen de `results/`, no de §5.** |
| **`results/index.md` + los 4 índices** (`bench_imagenes/`, `bench_nivel_a/`, `clip_bench/`, `realtime/`) | ✎ **La fuente de cifras del capítulo**, verificada mecánicamente con `96-verificar-indices.py`. Si un número no está acá, no existe para el informe. |
| **`operacion/97-relevamiento-plataforma-2026-08-05.md`** | ✎ El estado verificado de la plataforma (**reemplaza al 56**). |
| **`operacion/98-conclusiones-transversales.md`** | ✎ Las 4 conclusiones + la escala de afirmación **AF-1…AF-11** + las limitaciones. |
| **`informe/99-materiales-de-cierre.md`** | ✎ Inventario de figuras/tablas con su artefacto, anexo de reproducibilidad, licencias y citas obligatorias, limitaciones L1–L8, ADRs y el catálogo de mecanismos. |
| `informe/92-anexo-concrecion-tecnica.md` | Contratos, APIs y rutas:línea. ⚠ **Ya NO es fuente de cifras** (derogado, doc 97 §2.1): para números, los índices de `results/`. |
| `informe/93-redlines-etapa3.md` | El tablero de trabajo: los **26** redlines (R-01…R-26) con casillas. |
| `informe/94-secciones-nuevas-etapa3.md` | Texto ya redactado en registro de informe (modelo de estilo). |
| `informe/91-relevamiento-etapa3-vs-implementacion.md` | Qué contradice/falta en el capítulo, con plan A–D. |
| `informe/95-auditoria-y-plan-de-cierre.md` | Plan de cierre, orden de sacrificio, reglas anti-error. |
| `informe/90-etapa3-texto-extraido.md` | La Etapa 3 **vigente** (texto a corregir). |
| `informe/96b-informe-v11-17-1-consolidacion-metodologica.md` | El protocolo (§17.1) contra el que todo se lee. |
| `informe/96a-informe-v11-frontmatter-intro-objetivos-plan.md` | Intro, objetivos, etapas: el marco del documento. |
| `nucleo/10-registro-alcance-y-exclusiones.md` | El alcance cerrado y las exclusiones E-01…E-13. |
| `decisiones/README.md` + los **15** ADRs (✎ 2026-08-06: *decía "14"* — sin el ADR-015 no subía justamente el cierre de alcance) | Las decisiones formalizadas y sus porqués, incluido **ADR-015** (cierre de alcance: MQTT no implementada, G1 capacidad medida, R-13/R-21 desbloqueados). |
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
| `specs/40…45 + README` | Lo especificado por módulo (leer como "lo pedido"; ✎ el que dice lo construido es `operacion/97`). |
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
| `nucleo/01/05/06/07/11`, `contingencia/20` | Consulta puntual; ✎ en general `operacion/97` + `informe/92` los resumen. |

**No subir:** los `.docx` (pesados y mal indexables — su texto ya está en 90/96),
`operacion/datos/*` (JSON crudo; ✎ las cifras citables ya están en los índices de
`results/` y en el doc 97 §5), `herramientas/`, docs históricos 32/36/50/56.

## 2. Instrucciones del Project (pegar en "Custom instructions")

```
Sos el asistente de redacción del informe final (TFG) del proyecto E-OVRT-VDP:
una plataforma experimental de detección open-vocabulary de riesgos de seguridad
en construcción. El knowledge contiene la documentación completa del proyecto.

REGLAS DE LECTURA (obligatorias):
1. Leé primero "13-glosario-y-convenciones-de-lectura" (siglas y jerarquía de
   verdad) y "97-brief-de-redaccion" (reglas de redacción). Todo lo que escribas
   debe cumplirlas.
2. Jerarquía de verdad sobre el estado de la plataforma: doc "operacion-97" >
   banners "✎" de cualquier doc > el resto. Los docs con banner son fotos
   históricas: NUNCA cites su cuerpo como estado actual. El doc 56 quedó
   REEMPLAZADO por el 97; el plan del doc 95 §5 es histórico pre-rodaje.
3. Cifras: SOLO de los cuatro índices de "results/" (bench_imagenes,
   bench_nivel_a, clip_bench, realtime), que están verificados mecánicamente
   contra los metrics.json; el doc 97 §5 es un atajo de esos mismos números y
   siempre se chequea contra el índice antes de citar. El doc 92 sirve para
   contratos, APIs y rutas:línea, NO para cifras. Si un número no está en un
   índice, decí que no hay artefacto y no lo uses. Nunca inventes números,
   rutas ni nombres de campos.
4. TODO el GT de video es HUMANO y "gt_ready": sus métricas SE REPORTAN COMO
   RESULTADO. La regla vieja de presentarlas como "verificación de mecánica"
   está DEROGADA y no aplica ya a NINGÚN material.
   El banco tiene 47 clips = 32 positivos / 15 negativos / 37 episodios, en dos
   bloques: A = rodaje guionado (34 clips, 35 episodios) y B = lote de internet
   (13 clips, obra real no guionada). El estrato B se reporta como fila aparte,
   NUNCA fusionado al agregado del rodaje.
   Al citar un denominador, decí de qué bloque hablás: "34 episodios evaluables
   sobre 35" es el del RODAJE (1 censurado), no el del banco.
   El estrato B tiene solo 2 episodios evaluables tras una revisión ciega del GT
   que encontró que 5 de las 7 declaraciones del lote eran errores de anotación.
   Con n=2 NO se rankean granularidades: "scene 0,333 le gana a subject 0,190" es
   ruido. Lo robusto de ese estrato es la asimetría de FP: 26 vs 323 en 11
   negativos.
5. Reglas de lectura que no se pueden violar: los clips negativos NO entran a
   precision/recall/F1 (su métrica son los FP); se reporta siempre por estrato y
   por escenario, nunca solo el agregado; el SDR no se compara entre cadencias;
   los "re_alerts" no son falsos positivos; y FAR/hora se reporta pero NO sostiene
   una cota: se cita como "3 y 190 FP en 6:09,6 del único clip soak", con la tasa
   horaria (29,2 y 1.850,8) como derivada, nunca desnuda ni como "<=N FA/hora".
6. Las decisiones ADR-001…015 están cerradas: se declaran y justifican, no se
   re-litigan (ADR-015 además cierra la puerta: ninguna capacidad nueva hasta la
   defensa, MQTT declarada no implementada). Ojo: hay DOS series de ADR —
   ADR-001…015 del proyecto y ADR-0001…0013 internos del control-plane; al citar,
   decí la serie (convención en el glosario, doc 13).
   La tesis NO es "OVD detecta mejor" (ver doc 09): es la plataforma
   que mide qué se logra especificando condiciones en lenguaje, sin entrenar.

CÓMO TRABAJAR:
- El texto del informe vive en Google Docs; acá se produce texto listo para
  pegar, en registro formal impersonal (modelo: doc 94), en español.
- Para cada sección: buscá el redline correspondiente en el doc 93 (son 26,
  R-01…R-26), la evidencia en los índices de "results/" + operacion-97, y el
  borrador previo en el 94. Entregá el texto final + qué redline queda saldado
  (R-NN). Para figuras, tablas, reproducibilidad, licencias/citas, limitaciones
  y mecanismos hay un documento dedicado: "informe-99-materiales-de-cierre".
- Terminología y nombres de artefactos exactamente como en el glosario; los
  identificadores técnicos en monoespaciado y sin traducir.
- Lo no implementado se declara honestamente desde "operacion-98" §6 y los
  índices de "results/" (NO desde el doc 91 §7, que es anterior al tramo
  experimental); las métricas que no aplican usan los estados de aplicabilidad
  del ADR-006/013.
- Si encontrás una contradicción entre documentos, señalala y resolvela por la
  jerarquía del punto 2; si no se puede, dejala registrada como pendiente.
```

## 3. Flujo de trabajo sugerido en el chat

0. ✅ **PUERTA ABIERTA — 2026-08-10.** ~~*Puerta de secuencia (orden del usuario
   2026-08-05, `informe/99` §7): la redacción de §17.x no arranca hasta que estén (1) los
   runs/evals del lote de internet (estrato B) y (2) los videos V1–V3.*~~ **(1) está
   hecho** —el lote cerró con GT humano y sus campañas corrieron y se re-evaluaron—, y
   **(2) pasó a carril paralelo** porque no bloquea escribir. **La redacción es el carril
   principal.**
   ✅ ~~Lo que sí falta antes de usar este manifiesto: regenerar el
   `informe-project-kit/`~~ — **regenerado el 2026-08-10 según este manifiesto §1**
   (el paquete del 2026-07-18 quedó descartado; el vigente incluye `sintesis/`, la
   `GUIA-REDACTORES`, los índices de `results/`, el tramo de video 109–113 y los 15
   ADRs con el 015).
1. **Sesión inicial:** pedir al asistente un plan de redacción a partir del doc 93
   (tablero de 26 redlines) + `informe/99` (inventario de figuras/tablas), priorizado
   por bloques A–D. ✎ **No** desde el doc 95 §5: ese cronograma es histórico pre-rodaje
   (sí sirve su §5.5, el orden de sacrificio — **salvo su ítem 1, derogado**: G1 se
   implementó y midió, ADR-015 E-03).
2. **Por sección:** "redactá la sección que salda R-NN" → pegar en Google Docs →
   marcar la casilla en el doc 93 local.
3. **Al llegar resultados nuevos** (el GT del lote de internet, corridas nuevas): se
   actualizan **los índices de `results/`**, se corre
   `operacion/datos/96-verificar-indices.py` y se re-suben esas piezas; el resto no
   cambia.
4. **Regenerar el paquete** tras cambios en `docs/`: copiar según el manifiesto §1
   (o pedir a Claude Code que lo regenere).
