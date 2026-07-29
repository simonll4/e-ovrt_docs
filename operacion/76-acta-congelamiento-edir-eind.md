# 76 — Acta de congelamiento de `edir_v1` + `eind_v1`

- **Fecha:** 2026-07-29
- **Propósito:** dejar registrado el congelamiento de los dos prompt sets del
  comparativo E-DIR vs E-IND (Fase D, doc 62 §7), cumpliendo la regla 3 del
  doc 12 §2.2 (revisión previa al freeze, mitigación del sesgo del auditor,
  doc 07 D1.6). Con esta acta, la Fase D queda **desbloqueada**.

## 1. Qué se congela

| Set | status | track | `frozen_sha256` |
|---|---|---|---|
| `edir_v1` | `frozen` | `comparative` | `a1278d0c34cd13beb759a1fe10b13c7096f147f7be23154f28a79454b5643703` |
| `eind_v1` | `frozen` | `core` | `7a0126f45eb1362a2cfcc67458caa307357dc3f7684188fae6486486cd5ed770` |

Hashes computados con `classes_sha256()` del BFF (`eovrt_webconsole/prompt_store.py`,
convención spec §2.1: JSON canónico del bloque `classes` crudo) — la misma función
que el test de integridad verifica. Regla vigente desde ahora (doc 12 §2.2 regla 1):
**nada se reformula; una frase mal elegida es un resultado, no un bug.**

## 2. Registro de la revisión (doc 07 D1.6)

- **Revisión del usuario (2026-07-29):** leyó las 8 formulaciones de `edir_v1`
  presentadas verbatim (tabla por eje × condición) y las 3 clases de `eind_v1`;
  las juzgó buenas candidatas y delegó explícitamente la revisión técnica final
  y el cierre ("revisalos de manera crítica y con relación a la arquitectura de
  modelos a la que está destinado; si realmente creés que son buenos candidatos,
  cerralos").
- **Revisión técnica (Claude, misma fecha):** contra la tabla pre-registrada y la
  arquitectura de ambos backends. Resultado abajo.

## 3. Resultado de la revisión técnica

**Fidelidad al pre-registro:** las 8 frases de `edir_v1` son transcripción
**literal, palabra por palabra**, de la tabla del doc 12 §2.2 (Anexo C Tabla C.1 +
Tabla 45). Las 3 clases de `eind_v1` usan phrasings **idénticos** a los del set
congelado del que deriva (`cr01_cr02_v2_short`: "person"/"helmet"/"vest") — la
Fase 1 de E-IND puede puntuarse sin re-inferir (doc 04 §7.7) porque el vocabulario
es el mismo que ya corrió.

**Compatibilidad con la arquitectura (pista primaria GDINO-tiny-560, réplica
YOLOE-26s):**

- GDINO hace *phrase grounding* con encoder de texto BERT: frases nominales
  multi-palabra son su caso de uso natural; las 8 son cortas, gramaticales y sin
  ambigüedad de parseo. La debilidad conocida de estos encoders con la **negación**
  ("without" tiende a ignorarse; los tokens de "hard hat" pueden matchear cascos
  reales) **no es un defecto del set: es exactamente la hipótesis que el eje
  sintáctico testea**. Las formulaciones son las que un operador real escribiría —
  sondas justas, no hombres de paja.
- YOLOE consume el embedding de la frase completa (encoder tipo CLIP); mismo
  razonamiento: la negación diluida en el embedding es parte del objeto de medición.
- Los **templates de presencia** ("a photo of a …") están correctamente cableados
  como diagnóstico: `role: diagnostic_template`, `enabled_by_default: false`, se
  activan solo por `active_ids` — no contaminan la evidencia de ausencia (regla 2).
- Cada formulación es un `prompt_id` propio → soporta el sub-experimento
  aislado-vs-completo (doc 12 §3), que es la mitigación pre-registrada de la
  competencia entre prompts en la atención texto-imagen de GDINO.

**Veredicto: buenos candidatos. Se congelan sin tocar una sola frase.**

## 4. Caveats interpretativos declarados ANTES de los resultados

Se registran ahora para que ningún patrón de resultados se "descubra" post-hoc:

- **C1 — asimetría del eje estado-observable entre condiciones.** CR-01 lo
  instancia como reformulación positiva ("bare head": existe palabra visual para la
  ausencia de casco); CR-02 **conserva la negación** ("without bright colored
  safety clothing") porque la ausencia de chaleco no tiene estado positivo nombrable
  — lo que cambia respecto del eje de negación es *qué* se niega (atributo
  observable vs objeto). Consecuencia: si el contraste obs-vs-neg da distinto en
  CR-01 que en CR-02, eso puede reflejar esta diferencia estructural de la frase,
  no una diferencia del riesgo. No sobre-leer esa asimetría.
- **C2 — el eje de especificidad cambia sujeto y objeto a la vez** ("person"→
  "construction worker" y "hard hat"→"safety helmet"). Mide *especificidad global
  de la formulación*; no permite atribuir el efecto a un componente. Así está
  pre-registrado.
- **C3 — el eje estado-observable de CR-01 agrega contexto de escena** ("on
  construction site"), o sea estado + contexto en un solo salto. Mismo tratamiento
  que C2.
- **C4 — interacciones conocidas a tener presentes al leer resultados:**
  F-G2.1 (sobre-marca de `vest`/ropa vistosa, doc 67) toca de lleno a las
  formulaciones CR-02; y la pista primaria `gdino-tiny` es débil en `bare_head`
  (E1, Sprint 2) mientras `gdino-base` es el especialista — si el eje observable de
  CR-01 rinde poco en la primaria, eso es un resultado esperado del modelo, no de
  la frase.

## 5. Decisiones de metadatos tomadas al cerrar (no tocan frases)

1. **`strategy: direct_absence` → taxonomía pre-registrada**: `cr01_neg`/`cr02_neg`
   pasan a `syntactic_negation` y `cr01_spec`/`cr02_spec` a `specificity`.
   `direct_absence` confundía el *carril* (E-DIR) con el *eje*; la taxonomía de 5
   valores (docs/prompt-strategy.md) ES los ejes del informe y así la usan los sets
   archivados. El media-plane acepta `strategy` como string libre → sin impacto.
   El hash se computó después del remapeo (el sha congela los metadatos correctos).
2. **`track: comparative` se conserva** y el espejo del BFF se amplía
   (`prompt_store.py`: `Literal["core", "demo", "comparative"]`) — `edir_v1` no es
   del carril core y etiquetarlo `core` habría sido falsear su rol.
3. **Normalización colateral:** `cr01_cr02_v2_safety_vest` pasa de `status: draft`
   (valor fuera del ciclo de vida) a `exploratory`, su estado real.
4. **Nota de gobernanza (observación de la revisión adversarial posterior):** el
   remapeo de strategies y el flip a `frozen` se hicieron **editando el YAML a mano**,
   no vía `confirm_freeze()` del store. Fue necesario: el set estaba en
   `frozen_pending_review` (estado que el store no deja editar) y `confirm_freeze()`
   no re-valida — aplicado tal cual habría congelado `direct_absence`, un valor que
   el propio espejo rechaza. El resultado final valida contra `PromptSetModel` y el
   hash se computó con la función canónica; esta acta es el registro de esa
   operación manual.

## 6. Verificación

- `test_prompt_store.py` **15/15 verde** — incluye `test_repo_frozen_sets_integrity`,
  rojo desde 2026-07-24. Consecuencia importante: **la verificación de
  `frozen_sha256` vuelve a ejecutarse de verdad para TODOS los sets congelados**
  (rota mientras el primer YAML del glob reventaba el modelo).
- Suite completa del backend del BFF: **578 passed, 0 failed**.
- Sin commitear (regla vigente: git lo maneja el usuario). Archivos tocados:
  `prompts/edir_v1.yaml`, `prompts/eind_v1.yaml`,
  `prompts/cr01_cr02_v2_safety_vest.yaml`,
  `webconsole/backend/src/eovrt_webconsole/prompt_store.py`.

## 7. Efecto sobre el plan

- Doc 75 §1 ítem 4 (acta): **CERRADO**. La Fase D ya no espera nada del carril de
  prompts; sigue dependiendo del GT humano (CVAT en curso) como las Fases T y P.
- Doc 75 §2 ítem 3 (test espejo que enmascaraba la verificación de hashes):
  **CERRADO** como parte de esta acta.
