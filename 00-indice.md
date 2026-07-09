# Índice de lectura — Documentación de la plataforma E-OVRT-VDP

- **Última actualización:** 2026-07-09
- **Propósito:** guía de lectura ordenada del set de documentos generados durante el
  relevamiento del control-plane, la revisión de Etapa 3 y la definición del norte
  hacia la defensa (~fines de septiembre 2026).

> ⚠️ **`projects/docs/` NO está bajo control de versiones. No se commitea. No es un repo git.**
>
> El workspace `projects/` completo **no es un repositorio git** (así lo declara
> `projects/CLAUDE.md`). Los dos repos reales de la plataforma son sus hermanos
> `e-ovrt_media-plane/` y `e-ovrt_experimental-setup/` — `docs/` no vive dentro de
> ninguno de los dos, así que ningún `git add`/`commit` desde ahí la alcanza.
>
> Hay un `.git/` en la raíz de `projects/`, pero es un cascarón vacío (solo
> `.git/info/exclude`, sin `HEAD` ni `objects` ni `refs` — `git status`/`git log` fallan
> con "not a git repository"). **No lo tomes como señal de que hay versionado real**; es
> justamente el hueco H10 (doc 07): *"la documentación de `projects/docs/` no está
> versionada... existe un `.git` vacío en la raíz — inconsistencia en sí misma"*.
>
> **Consecuencia práctica:** todo lo que se escribe en `docs/` (este índice incluido) es
> perdible — no hay historial, no hay backup, no hay forma de deshacer un `rm`. Está
> pendiente que el usuario decida (a) versionarla en un repo propio o (b) moverla al
> repo del informe/TFG. Hasta entonces, **no ejecutar `git init`, `git add` ni
> `git commit` en `projects/` ni en `docs/`** sin que el usuario lo pida explícitamente
> en ese turno — regla general del workspace (`CLAUDE.md` §"Git conventions"), reforzada
> acá porque `docs/` es, de las dos, la parte con más riesgo de pérdida silenciosa.

## Cómo está organizado

El **número del documento es su identidad** y no cambia: en todo el set se referencian
entre sí como "doc 04", "doc 07", etc. Las carpetas agrupan por **rol**, no por tema:

| Carpeta | Qué contiene | Estabilidad |
|---|---|---|
| `informe/` | **El TFG en sí** (`.docx`) y su texto extraído (serie 90-). Es nuestro entregable, no una fuente externa. | Viva — se reescribe al final |
| `nucleo/` | 01–11. La narrativa principal, en orden de lectura. | Viva — se corrige y amplía |
| `contingencia/` | Serie 20-. Trabajo **fuera del plan**, por si sobra tiempo. No reabre exclusiones. | Congelada salvo que se active |
| `operacion/` | Serie 30-. Runbooks y mediciones sobre el host local. `operacion/datos/` guarda evidencia cruda (JSON, scripts). | Viva — se re-mide |
| `herramientas/` | Diseño y plan de utilidades del entorno de desarrollo. No es documentación de la plataforma. | Independiente |

**Cómo se relacionan `informe/` y `nucleo/`.** No hay una carpeta que sea "la verdad" y
otra que la comente. El informe **está en desarrollo** y el núcleo lo critica y lo corrige
a la luz de la implementación y los experimentos (doc 02 revisa Etapa 3; doc 08 se alinea
con §17.1 y lista las desalineaciones a arreglar **en ambos lados**). El propio doc 08 lo
dice: *el informe no es fuente de verdad cerrada, pero es el protocolo contra el que la
plataforma y nuestros documentos deben leerse.* El flujo es bidireccional:

```
   informe/  ──"protocolo, definiciones, metodología"──►  nucleo/
        ▲                                                    │
        └──"redlines, erratas, resultados, decisiones"───────┘
              (se aplican casi al final del proyecto)
```

Corolario práctico: **una crítica del núcleo no se pierde**, se agenda como redline sobre
el `.docx`. Y un cambio del informe puede invalidar un doc del núcleo. Ninguno manda solo.

> Recordatorio: **`docs/` no está bajo git** — ver el aviso al principio de este índice
> y el hueco H10 en `nucleo/07-auditoria-decisiones-y-huecos.md`.

## Orden de lectura recomendado

### `nucleo/` — la narrativa principal

| # | Documento | Qué responde | Tipo |
|---|---|---|---|
| 01 | `nucleo/01-relevamiento-control-plane.md` | ¿Qué es y cómo funciona el repo `e-ovrt_control-plane`? Arquitectura, contratos, motor de patrones, punto débil de identidad. **§12: actualización 2026-07-09 con la rama `mati`** (motor mejorado: matching 1:1, pose, cooldown; paquete `eovrt_labs` con generador + tracker IoU + backend supervisado yolo-ppe; **§12.3: toolchain de calibración y los dos experimentos reales ya corridos** — video Intel 06-26 y video5+gdino 07-07). | Relevamiento |
| 02 | `nucleo/02-revision-critica-etapa3-y-norte.md` | ¿Qué dice la Etapa 3 del TFG, qué está bien, qué falta decidir, y cuál es el norte? Estado real vs backlog, recorte must/won't, 4 resultados defendibles (R1–R4), plan de 12 semanas. | Crítica + plan |
| 03 | `nucleo/03-spec-plataforma-dos-caminos.md` | ¿En qué difiere exactamente "lo implementado" de "lo que plantea el doc" y cómo se decide cada punto? Las 6 dimensiones (D1–D6), tablero de decisiones vivo, secuencia de inclinación de la implementación. **Documento rector.** | Spec integrador |
| 04 | `nucleo/04-diseno-comparativo-estrategias-edir-eind.md` | ¿Cómo se decide D1 (la única dimensión empírica)? Desarrollo documental de E-IND, E-DIR (neg/obs) y E-HYB; protocolo pre-registrado en 2 fases con gates y criterios fijados antes de correr. | Pre-registro experimental |
| 05 | `nucleo/05-integracion-media-control-bus-eventos.md` | ¿Cómo se conectan los planos con un bus de eventos (D3)? Costuras en cada repo, envelope, ZeroMQ vs broker, fases A/B/C. | Diseño técnico |
| 06 | `nucleo/06-diseno-distribucion-alertas.md` | ¿Cómo se distribuyen las alertas confirmadas (D5)? Diseño completo del 2026-07-04 — **se implementa recortado** según D5 del doc 03 (canal MQTT + ledger; dashboard absorbido por la webconsole). | Diseño técnico (pre-existente, a recortar) |
| 07 | `nucleo/07-auditoria-decisiones-y-huecos.md` | ¿Qué puede estar mal en todo lo anterior? Crítica decisión por decisión (D1–D6 + decisiones implícitas), huecos detectados con su corrección, y contingencias. | Auditoría |
| 08 | `nucleo/08-alineacion-consolidacion-metodologica.md` | ¿Cómo se alinea todo el set con la Consolidación Metodológica del informe (§17.1)? Validaciones textuales (D1 mandado por el protocolo de prompts, G0, clip bench=EBE oficial), desalineaciones a corregir (severidades/ventanas PR-01/PR-02, nombres y umbrales de métricas, ejes de prompts faltantes) y acciones. | Alineación |
| 09 | `nucleo/09-justificacion-ovd-y-defensa.md` | ¿Por qué OVD si un modelo cerrado detecta cascos mejor? Reencuadre de la tesis, 5 argumentos de defensa, Q&A hostil, estructura del cierre del informe, y qué mostrar en la presentación (4 números, videos V1–V4, overlay renderer, gestión de riesgo de demo). | Defensa |
| 10 | `nucleo/10-registro-alcance-y-exclusiones.md` | Cierre formal del alcance: la lista cerrada de lo que SÍ se implementa (núcleo validable + EBE ya construido + distribución mínima) y el registro E-01…E-13 de todo lo excluido, cada uno con estado, regla del informe que lo ampara, rastro documental y frase de declaración. **Documento rector del alcance.** | Alcance |
| 11 | `nucleo/11-relevamiento-media-plane.md` | Relevamiento completo del media-plane (estado 2026-07-09): API, módulos, flujos single-host/two-node, historia de ramas, y las novedades sin commitear (visibilidad two-node en webconsole validada E2E). Hallazgo: `VideoAnnotationWriter` ya cubre media pieza del overlay renderer del doc 09. | Relevamiento |

**Lectura mínima si hay poco tiempo:** 02 (norte) → 03 (decisiones) → 07 (riesgos) → 08 (alineación con el informe) → 09 (defensa).

### `contingencia/` — fuera del plan

| # | Documento | Qué responde |
|---|---|---|
| 20 | `contingencia/20-investigacion-finetuning-condicionada-e04.md` | Investigación completa de fine-tuning de GDINO (MM-GDINO/ODVG) y YOLOE sobre nuestros datos, por si sobra tiempo: inventario de lo ya listo, presupuestos GPU, escalera T1–T3 con criterios go/no-go pre-registrados, y una corrección de cita del paper Abdalwhab para el informe. **No reabre E-04.** |

### `operacion/` — runbooks y mediciones del host local

| # | Documento | Qué responde |
|---|---|---|
| 30 | `operacion/30-runbook-local.md` | Cómo levantar media-plane + webconsole en local sin Docker, con hot-reload, para iterar rápido: comandos por terminal, refs de modelo, lanzar una corrida RTSP, y las trampas conocidas (`dist/` viejo servido en silencio, run "succeeded" con cámara caída). |
| 31 | `operacion/31-benchmark-modelos-host-local.md` | Benchmark de las 6 variantes GDINO/YOLOE: BENCH v2 val con GT (mAP@0.5, AP por clase, recall CR-01) + cámara RTSP en vivo (keep-up, latencia, VRAM). **Hallazgo clave: YOLOE es ciego a `bare_head` (recall CR-01 ≈ 0), y el mAP oculta que GDINO-base gana en CR-01 y `vest` pese a perder en mAP.** |

Evidencia cruda del doc 31, para que los números sean auditables y re-generables:

| Archivo | Qué es |
|---|---|
| `operacion/datos/31-benchmark-modelos-host-local.datos.json` | Salida cruda de las 12 corridas (6 modelos × 2 suites), con `run_id`, latencias y evaluación. |
| `operacion/datos/31-benchmark-modelos-host-local.driver.py` | Script que las reproduce: levanta y baja un servicio por modelo. |

### `informe/` — el TFG, en desarrollo

Nuestro entregable. **No es fuente de verdad cerrada**: se lo critica desde `nucleo/` y se
lo reescribe al final, cuando estén tomadas las decisiones (D1–D6) y corridos los
experimentos. Los redlines pendientes viven en los docs 02 (§4.8, erratas) y 08 (§2,
desalineaciones).

| # | Documento | Qué es |
|---|---|---|
| — | `informe/E-OVRT-VDP_v1.1_05062026-sin-indice.docx` | El informe completo del TFG (Etapas 1–2 + consolidación metodológica §17.1 + Etapa 3 previa). Aporta el protocolo metodológico contra el que se leen los docs 01–11. |
| — | `informe/E-OVRT-VDP_Etapa_3_Diseno_Arquitectonico.docx` | El capítulo 17.3 standalone (versión más reciente de Etapa 3). Insumo del doc 02, que lo revisa críticamente. |
| 90 | `informe/90-etapa3-texto-extraido.md` | Texto plano de Etapa 3, **solo para búsqueda y cita rápida**. Es una extracción derivada: al editar, se edita el `.docx`, no este archivo. |

### `herramientas/` — entorno de desarrollo

| Documento | Qué es |
|---|---|
| `herramientas/2026-07-05-docker-wsl-disk-control-design.md` | Diseño del mecanismo de 3 capas para que Docker/WSL2 no agote el disco `C:`. |
| `herramientas/2026-07-05-docker-wsl-disk-control.md` | Plan de implementación del mismo. Los scripts viven en `projects/scripts/`. |

## Estado del tablero de decisiones (espejo de 03 §9 — actualizar allí primero)

| # | Dimensión | Estado | Resolución |
|---|---|---|---|
| D1 | Estrategia del núcleo (E-IND / E-DIR / E-HYB) | Abierta | Experimento pre-registrado (doc 04), cierre fin de semana 4 |
| D2 | Granularidad del patrón (G0 escena / G1 sujeto) | Abierta | ADR semana 1 — recomendación: G0 núcleo, G1 condicionada |
| D3 | Bus media→control | Abierta | ADR semana 1 — recomendación: ZeroMQ PUB/SUB, broker diferido |
| D4 | Config paraguas / experiment_id | Abierta | ADR semana 1 — recomendación: manifiesto en experimental-setup |
| D5 | Distribución de alertas + canal | **Decidida: MQTT** (2026-07-06) | Falta formalizar ADR |
| D6 | Reporte consolidado + métricas | Abierta | ADR semana 2 — recomendación: adoptar Camino B (Etapa 3) |

**Insumo nuevo para D1:** el doc 31 muestra que YOLOE no puede sostener CR-01 tal como está
definida (`bare_head`). Si CR-01 sigue anclada a esa clase, YOLOE sale del espacio de
búsqueda antes de correr el experimento del doc 04.

## Trabajo común que no depende de ninguna decisión (arranca ya)

1. Corrida DBE end-to-end real (media-plane → control-plane sobre detecciones reales).
2. Clip bench con GT temporal — mayor lead time de todo el plan (ver hueco H2 en doc 07).
3. Calibración de umbrales/regiones con datos reales.
4. Erratas del .docx de Etapa 3 (doc 02 §4.8).
