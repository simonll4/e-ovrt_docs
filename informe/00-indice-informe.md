# `informe/` — el entregable y sus ajustes

> **Reorganizada el 2026-08-10.** Antes esta carpeta era un solo montón de 17 archivos
> numerados 90–99 donde convivían el informe, el capítulo de Etapa 3, los redlines y el
> kit de redacción. Ahora está partida en **dos**, según la pregunta que uno viene a
> hacerle:

| Si venís a… | Entrá por |
|---|---|
| **leer el informe tal como está hoy** (o el capítulo de Etapa 3) | [`entregable/`](entregable/00-el-informe-hoy.md) |
| **saber qué hay que cambiarle, etapa por etapa** | [`ajustes/00-mapa-de-ajustes.md`](ajustes/00-mapa-de-ajustes.md) ← **el punto de entrada** |
| **ponerte a aplicarlo** (dónde escribís, en qué orden, qué te toca, qué falta producir) | ✎ [`ajustes/08-manual-de-aplicacion.md`](ajustes/08-manual-de-aplicacion.md) ← **el documento del día 1** |
| **trabajarlo en un Project de ChatGPT** | [`informe/project-kit/README.md`](project-kit/README.md) ← **cuatro archivos de knowledge: dos generados por etapa + los dos DOCX del entregable** (✎ 2026-08-16) (✎ 2026-08-28: = el **base de formato** `…sin-etapa3.docx` + el **`.docx` vigente de la sección en trabajo**, en `entregable/desarrollando/`) |

> ✎ **2026-08-28 — estado del informe (fuente `entregable/00-el-informe-hoy.md`):** **Etapa 1
> CERRADA** (§15+§16 **v1.0**, 08-28) · **Etapa 2 (§17.1) en curso** tras `operacion/130` ·
> §17.3 **v1.4** · §17.4 **v1.6** · §17.5 **v1.3** redactadas con sus pases aplicados y
> verificadas, todas en `entregable/desarrollando/` · vacías: **§17.6, §18, §19**. El árbol de
> abajo es el del 08-10: hoy `entregable/` tiene además `desarrollando/` (los `.docx` de trabajo
> + `archivado/`), `borradores/`, los textos extraídos `90b`–`90f` y `resumen-cambios-etapa-1.md`;
> `ajustes/` tiene además `09-pase-de-tablas-y-lectura-de-cierre.md`; `herramientas/` tiene
> `extraer_informe.py` y `verificar_entregable.py`.
>
> ✎ **2026-09-07 — vencido lo de arriba; el árbol de abajo ya está actualizado.** Estado real:
> las cinco secciones tienen entrega con sugerencias del pase 5 (§15/16 **v1.3** · §17.1 **v1.17** ·
> §17.3 **v1.9** · §17.4 **v1.9** · §17.5 **v1.6**), a la espera de que el usuario las revise en Google
> Docs; siguen vacías **§17.6, §18 y §19**. Lo superado se archivó ese mismo día, cada carpeta con su
> `00-que-hay-aca.md`. La fuente sigue siendo `entregable/00-el-informe-hoy.md` y los pendientes,
> `entregable/00-lo-que-resta.md`.
>
> ✎ **2026-09-18 — EL INFORME ESTÁ COMPLETO; todo lo de arriba es historia.** El documento
> desarrollado entero es **`entregable/desarrollando/E-OVRT-VDP_Informe_Final_2026-09-16_v0.1.docx`**
> (portada + §2–§19 + Anexos A–F + Referencias; 82k palabras; 73 tablas; 8 figuras; sin comentarios
> ni cambios rastreados). Su foto de texto: **`entregable/90-informe-final-2026-09-16-v0.1-texto-extraido.md`**.
> Los `.docx` por sección, el maestro v1.1, las actas, los mapas de secciones y las fotos por sección
> fueron a `entregable/desarrollando/archivado/` y `entregable/archivado/`. **`ajustes/` y `project-kit/`
> quedan históricos**: el pase de redacción que gobernaban terminó; se conservan porque el set los cita
> por número y ruta. Lo que resta es formal y está en `entregable/00-lo-que-resta.md` (foto 2026-09-18).

---

## Estructura

```
informe/
├── 00-indice-informe.md                      ← estás acá
│
├── entregable/                               ← EL INFORME, como está hoy
│   ├── 00-el-informe-hoy.md                  ← tablero por jornada (✎ 09-18: informe completo)
│   ├── 00-lo-que-resta.md                    ← el índice de pendientes, con dueño y bloqueo
│   ├── 90-informe-final-2026-09-16-v0.1-texto-extraido.md   ← LA FOTO DEL INFORME COMPLETO
│   ├── desarrollando/
│   │   ├── E-OVRT-VDP_Informe_Final_2026-09-16_v0.1.docx     ← EL INFORME FINAL (v0.1, 09-16)
│   │   ├── revision-informe-final-v0.6-2026-09-15.md         ← revisión externa de la v0.6
│   │   └── archivado/                        .docx por sección, maestro v1.1, actas, mapas, análisis
│   └── archivado/                            fotos por sección 90/90b–90g/96a–96e, standalone de Etapa 3, borradores
│
├── ajustes/                                  ← HISTÓRICO (✎ 09-18): el pase de redacción que gobernó terminó
    ├── 00-mapa-de-ajustes.md                 ← el mapa: etapa 1 → 6, en una tabla
    ├── 01-etapa-1-fundamentacion-teorica.md      inv. bibliográfica → §15 · §16 · Anexo A
    ├── 02-etapa-2-consolidacion-metodologica.md  análisis metodológico → §17.1 · Anexos C/D
    ├── 03-etapa-3-diseno-arquitectonico.md       diseño → §17.3 (enruta las 26 redlines)
    ├── 04-etapa-4-implementacion.md              implementación MVP → §17.4 (vacía → ✎ 08-28: v1.6 redactada)
    ├── 05-etapa-5-evaluacion-y-validacion.md     evaluación → §17.5 (vacía → ✎ 08-28: v1.3 redactada)
    ├── 06-etapa-6-documentacion-y-cierre.md      cierre → §17.6 (vacía) · §18 · §19
    ├── 07-critica-extension-y-poda.md            transversal: qué ELIMINAR (18 PODA-nn, ~27%)
    ├── 08-manual-de-aplicacion.md                ← CÓMO se aplica todo: orden, reparto, tablero
    ├── material-etapa-3/   91 · 92 · 92b · 93 · 94
│   └── gobierno/           95 · 97 · 98 · 99
│
└── project-kit/                              ← KIT PARA CHATGPT — HISTÓRICO (✎ 09-18), no se regenera
    ├── README.md                              uso y cambio de etapa
    ├── INSTRUCCIONES-PROJECT.md              se pega en Project settings
    ├── 00-contexto-base.md                    primer archivo del knowledge
    └── 01-etapa-N-activa.md                  segundo archivo; uno por etapa (0-6), no se pisan
```

---

## Lo que cambió, y lo que no

**Cambió:** la ubicación de los 17 archivos. Todos siguen existiendo, con el mismo
nombre y el mismo número; lo que ganaron es una carpeta.

**No cambió:** la numeración. Se sigue diciendo **"el doc 93"**, **"informe/99"**,
**"el 92b"**. Los números son la identidad de estos documentos y hay referencias por
número repartidas por todo el set — moverlos de carpeta es seguro, renumerarlos no.

| Antes | Ahora |
|---|---|
| `informe/90`, `96a`–`96e`, los dos `.docx` | `informe/entregable/…` |
| `informe/91`, `92`, `92b`, `93`, `94` | `informe/ajustes/material-etapa-3/…` |
| `informe/95`, `97`, `98`, `99` | `informe/ajustes/gobierno/…` |

**Nuevo:** los siete documentos de `ajustes/` (`00`–`06`) y los tres índices de carpeta.
El `00-mapa-de-ajustes.md` es el único documento del proyecto que ordena **todos** los
ajustes del informe por etapa; antes estaban repartidos entre `93` (solo Etapa 3),
`nucleo/08`, `sintesis/resultados-y-conclusiones.md` §7 y `gobierno/99`.

---

## Las tres cosas que conviene saber antes de tocar el informe

1. **Las seis etapas del Gantt (§14.3, Figura 1) son la guía de desarrollo**, y cada una
   tiene su sección: 1 investigación bibliográfica → §15/§16 · 2 análisis metodológico →
   §17.1 · 3 diseño → §17.3 · 4 implementación → §17.4 · 5 evaluación y validación →
   §17.5 · 6 documentación y defensa → §17.6/§18/§19. **El Gantt numera 0–5 y el §14.2
   numera 1–6**: misma secuencia, corrida en uno. La tabla completa está en
   [`ajustes/00-mapa-de-ajustes.md`](ajustes/00-mapa-de-ajustes.md) §0.
2. **§17.4 y §17.5 están vacías.** Etapas 1–3 son corrección de texto existente; etapas
   4 y 5 son redacción desde cero, y son el camino crítico. (✎ 2026-08-28: **vencido** — §17.4
   v1.6 y §17.5 v1.3 están redactadas en `entregable/desarrollando/`; vacías quedan §17.6, §18 y
   §19. El camino crítico hoy es la Etapa 2 (§17.1) y después el cierre.) (✎ 2026-09-18: **todo
   redactado e integrado** en el Informe Final v0.1; ninguna sección está vacía.)
3. **Las cifras salen solo de los cuatro índices de
   `e-ovrt_experimental-setup/results/`.** Varias tablas-atajo que parecen citables
   quedaron derogadas (`informe/92` §10, `gobierno/97` §5, `operacion/92`, `operacion/56`).

## Si sos parte del equipo que redacta y no participaste del trabajo experimental

Empezá por **`docs/GUIA-REDACTORES.md`**, no por acá. Esta carpeta es el material; la
guía es el orden de lectura y las trampas.
