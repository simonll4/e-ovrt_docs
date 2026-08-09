# 94 — Mini-piloto de clase nueva: el número de A1, medido

- **Fecha:** 2026-08-05.
- **Qué es:** el complemento de la Fase D que el doc 62 §7 dejó anotado y que el
  relevamiento del doc 93 encontró **fuera de todo tablero**. Mide lo que `nucleo/09`
  A1 exige medir textualmente — *"este número — condición nueva: 0 entrenamientos,
  ~20 líneas de configuración, minutos — debe medirse y reportarse como resultado, no
  solo afirmarse"* — y que **no estaba medido en ninguna parte**: toda la evidencia
  del trabajo era sobre CR-01/CR-02, el catálogo que ya existía.
- **Estado:** ejecutado completo. ~~Sin commitear.~~ (✎ commiteado al cierre del
  2026-08-05.)

## 1. El número de A1

| Costo de agregar clases que la plataforma JAMÁS configuró | Medido |
|---|---|
| Entrenamientos | **0** |
| Artefacto de configuración | **1 archivo, 48 líneas** (`prompts/clase_nueva_v1.yaml`, 5 clases nuevas) |
| Tiempo de pared del piloto completo | **9 minutos** (config + 5 corridas + scoring con GT real + verificación de mecanismo) |
| GT nuevo anotado | **0** (se reutilizó GT existente que `canonical_v2` nunca usó) |

## 2. Diseño (y por qué no fue como estaba anotado)

El plan decía "MOCS de clase nueva". Al inspeccionar, **la copia de MOCS en `raw/`
(export de Roboflow) solo anota `Worker`** — sin GT de maquinaria, imposible un AP de
clase nueva ahí. Pero el raw de `construction_site_safety` **sí anota `machinery` y
`vehicle`** (99 + 76 cajas sobre las 147 imágenes del núcleo curado), clases que
`canonical_v2` nunca arrastró — el mismo patrón que el GT de CR-02 (doc 83 F-83.3).
El piloto quedó en dos partes:

- **(a) Cuantitativa, sobre el bench congelado:** caption = catálogo desplegado +
  `machinery` + `vehicle`, scoring AP@0.5 contra el GT humano del raw en las 147
  curadas.
- **(b) Amplitud de vocabulario, sobre MOCS (151 imgs):** caption = `person` +
  `excavator` + `dump truck` + `tower crane`; `person`-vs-`Worker` da un **ancla
  cuantitativa cross-dataset** (507 cajas GT) y las máquinas, evidencia visual.

## 3. Resultados

### La clase nueva funciona — con número real

| Medición | Valor | n |
|---|---|---|
| **`machinery` AP@0.5, zero-shot, jamás configurada** | **0,662** | 99 cajas GT |
| `person` vs `Worker` en MOCS (cross-dataset, ancla) | 0,610 | 507 cajas GT |
| `excavator` con det ≥0,5 en MOCS | 62/151 imgs | sin GT (visual) |
| `tower_crane` con det ≥0,5 | 34/151 imgs | sin GT (visual) |
| `dump_truck` con det ≥0,5 | 4/151 imgs | sin GT (visual) |

Para calibrar el 0,662: **supera el mAP50 agregado del campeón sobre el mismo núcleo
curado con las clases configuradas** (0,447–0,503, doc 64). Una clase escrita en el
prompt cinco minutos antes rinde al nivel de las que estructuraron todo el proyecto.
Evidencia visual en `datos/94-piloto-clase-nueva/evidencia/`: `excavator 0.84` sobre
una excavadora real, `tower_crane 0.61` sobre las grúas.

### F-94.1 — La palabra tiene que alinear con la taxonomía del despliegue (el hallazgo honesto)

`vehicle` falló, y el mecanismo es más interesante que el número:

1. **En el caption junto a `machinery`: 0 detecciones.** Inanición total por
   competencia intra-caption entre clases semánticamente solapadas — el caso extremo
   de F-88.1 (allí una palabra costaba 0,082 de F1; acá una clase solapada borra a la
   otra).
2. **Aislada: 118 detecciones, AP 0,026.** Las cajas existen pero no caen donde este
   GT dice `vehicle`: **el 67% cae sobre lo que el GT llama `machinery`** (verificado
   caja por caja). El modelo entiende "vehicle" como algo que incluye la maquinaria;
   esta taxonomía los separa. No es que no vea — es que **la palabra significa otra
   cosa en este dataset**.

La lectura para A1 es la versión honesta y más fuerte del argumento: agregar la clase
cuesta minutos, **y validar que la palabra signifique lo que tu despliegue quiere
decir es parte del flujo** — y eso también cuesta minutos, porque el bench de la
plataforma lo expone al instante (descubrir y explicar la falla de `vehicle` costó
~3 minutos de scoring). Con detector cerrado, ese mismo error se descubre después de
una campaña de anotación y entrenamiento.

## 4. Qué afirma esto para la defensa (A1) y qué no

**Afirma:** el ciclo "condición nueva" completo — escribir la clase, correr, tener un
AP contra GT — se ejecutó en 9 minutos con 0 entrenamientos, y la clase nueva rindió
al nivel de las configuradas. El costo marginal de la condición N+1 es configuración,
medido.

**No afirma:** que cualquier palabra funcione (F-94.1 muestra el contraejemplo y su
mecanismo — coherente con F-88.3: el vocabulario importa), ni una condición de
*riesgo* nueva de punta a punta (eso requiere además el pattern set — cuyo costo ya
quedó medido tres veces esta semana: `cr01_cr02_edir_v1`, `hyb_or_v1`, `v2_subject`,
cada uno ~70 líneas y minutos).

## 5. Evidencia

`datos/94-piloto-clase-nueva/`: `resultados.json` (corridas, scores, procedencia de
runs), `evidencia/` (3 previews de MOCS). Prompt set: `prompts/clase_nueva_v1.yaml`
(experimental-setup, `exploratory`). Runner: `datos/94-piloto-clase-nueva.py`.
