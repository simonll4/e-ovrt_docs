# `nucleo/historicos/` — documentos no actualizados a lo implementado

**Criterio de esta carpeta (decisión del usuario, 2026-08-10):** es histórico **todo lo que
no esté actualizado a lo implementado o a los resultados actuales**.

No significa "equivocado" ni "sin valor". Significa que **describe una etapa previa** y que
no se puede usar como estado del sistema. Varios de estos documentos son la mejor evidencia
de cómo se decidió algo, y dos de ellos valen precisamente porque **no** se actualizaron
(§2).

**Regla de lectura:** si un documento de acá tiene banner ✎ o ⚠️, **manda el banner, no el
cuerpo**.

**Los archivos no se renumeran ni se renombran.** Conservan su número original porque el
set tiene miles de referencias por número. Lo único que cambió es la carpeta.

---

## 1. Qué hay acá

Ninguno tiene actualización posterior al **2026-07-13**; el tramo experimental completo
(rodaje, campañas, Fase L, lote de internet) es posterior y no está reflejado en ellos.

| Doc | Qué es | Última actualización | Dónde está el estado vigente |
|---|---|---|---|
| `01` | Relevamiento del control-plane | 2026-07-09 | **`../18`** |
| `02` | Revisión crítica de Etapa 3 y norte propuesto | 2026-07-09 | `../../operacion/95` (estado) · `../../operacion/98` (conclusiones) |
| `03` | Spec integrador: la plataforma por los dos caminos | 2026-07-09 | **`../14`** (mapa) · `../../operacion/97` |
| `04` | Diseño comparativo E-DIR vs E-IND (D1) | — | **Congelado a propósito** (§2) · resultados en `results/clip_bench/` |
| `05` | Integración media→control por bus de eventos | — | **`../17`** §6 y **`../18`** §6 · `../../operacion/37` |
| `06` | Diseño del módulo de distribución de alertas | — | **`../19`** es la entrada vigente; este sigue siendo el diseño completo (§2) |
| `07` | Auditoría de decisiones, contraargumentos y huecos | — | Los huecos se cerraron en `../../decisiones/` |
| `08` | Alineación con la Consolidación Metodológica (§17.1) | 2026-07-09 | `../../informe/ajustes/02-etapa-2-consolidacion-metodologica.md` |
| `09` | Justificación de OVD y estrategia de defensa (A1–A5) | 2026-07-09 | **Ver la advertencia de §3** |
| `11` | Relevamiento del media-plane | 2026-07-18 (banner) | **`../17`** |
| `12` | Diseño de prompts y fusión E-HYB | — | **Congelado a propósito** (§2) · resultados en `results/clip_bench/` |

## 2. Tres que valen por no haberse actualizado

- **`04` y `12`** son el **diseño pre-registrado del experimento D1**: se congelaron antes
  de correrlo. Su valor metodológico es exactamente ese — actualizarlos con los resultados
  destruiría la prueba de que las hipótesis se fijaron de antemano. **No se tocan.**
- **`06`** es el diseño completo del módulo de distribución (20 secciones: ledger, retry,
  dead-letter, canales, paridad DBE/EBE). El módulo **no está implementado**, así que el
  diseño no puede "actualizarse a lo implementado". Está acá porque la entrada vigente es
  **`../19`**, que lo consolida y lo cita; su §4 (ubicación del módulo) quedó superado por
  ADR-005.

## 3. Advertencia sobre el `09`

**`09` es el argumento central de la tesis** —los cinco argumentos A1–A5 de por qué OVD— y
su última actualización es del 2026-07-09. Está acá por el criterio, y **eso es en sí un
hallazgo**: el documento que sostiene la defensa **no incorpora los números que después se
midieron**. El caso más claro es **A1** (costo de agregar una condición nueva), que se midió
en `../../operacion/94` el 2026-08-05 y que este documento todavía plantea en términos de
expectativa.

**Antes de usar `09` para redactar la defensa, contrastarlo contra `../../operacion/98`**
(conclusiones AF-1…AF-11) y contra los índices de `results/`. Amerita un sucesor vigente en
la raíz de `nucleo/`.

## 4. Qué quedó en la raíz de `nucleo/`

`10` (registro de alcance, actualizado 2026-08-10) y la serie de relevamientos por servicio
**`14`–`19`** (relevada contra código el 2026-08-10).
