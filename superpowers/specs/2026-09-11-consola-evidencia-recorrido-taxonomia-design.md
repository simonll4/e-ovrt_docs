# Consola: el recorrido de evidencia y la taxonomía de clases

**Fecha:** 2026-09-11
**Repo:** `e-ovrt_experimental-setup` · rama `feature/webconsole-adopcion-front-design`
**Mockups:** https://claude.ai/code/artifact/28eb5e84-c842-4d97-9df3-ee8c29fa66f2
**Antecedente:** tramo 6 (archivado por evidencia) y tramo 7 (sección `/evidencia`), commits `ee5a834` y `b0c95c6`

---

## 1. El problema, medido

La pantalla `/evidencia` existe desde el tramo 7 y no cumple su función. El usuario no
puede decir, mirándola, qué se usó en los resultados ni qué los justifica. Medido sobre
la consola corriendo en `:8090`:

| Síntoma | Medición |
|---|---|
| Sopa de slugs | Los **35** `titulo:` de `results/evidence-vista/titulos.yaml` están **vacíos**, así que cada fila cae a la etiqueta derivada (`r4 gdinotiny560 v2short subject s15`) |
| El número equivocado al frente | La única cifra de la entrada es **Corridas** (544 en una fila) y «928 relaciones registradas» — plomería del CSV |
| Cero métricas | `clip_bench/t1`, la línea de base del Nivel B, no muestra F1, recall ni precision: muestra **68 IDs de corrida** con la misma nota de 4 líneas repetida **12 veces** en pantalla |
| Eje de organización | La carpeta del archivo (`bench_imagenes` / `bench_nivel_a` / `clip_bench` / `realtime`), no el argumento. El «recorrido del argumento en cuatro números» de `results/index.md` y los tres `results/ejes/` no existen en la consola |
| La distinción que falta | **17 de 35** resultados tienen `campaign.yaml` + `metrics.json` en `results/`; los otros **18** son mediciones de respaldo con artefacto fuera del repo. Ese 17/18 es exactamente «lo que el informe reporta» contra «lo que lo respalda», y es invisible |

Y el pedido se extendió a Corridas y Experimentos:

| Pantalla | Hoy | Con el binario `evidencia`/`archivadas` que ya existe |
|---|---|---|
| **Corridas** | 472 corridas | 420 / 52 — **el filtro casi no ayuda** |
| **Experimentos** | 459 ejecuciones, 11 manifiestos | La vista Evidencia ya deja **1 manifiesto** real, pero lumpa «**456 ejecuciones archivadas**» en un solo número que mezcla 445 smokes con 11 ensayos |

**Lo que lo hace tratable:** todo lo que falta ya está en disco, al lado de lo que la
página lee. `campaign.yaml` trae una descripción en castellano y la combinación declarada
(modelo, prompt set, pattern set, granularidad, DBE/EBE, stride); `metrics.json` trae las
cifras y su desglose. La propiedad de que `/evidencia` funcione **con los tres planos
apagados** se conserva: nada de esto consulta un servicio.

---

## 2. Decisiones firmadas por el usuario

| # | Decisión | Alternativas descartadas |
|---|---|---|
| **D-1** | **Un recorrido en capas**, no un modo de defensa separado del inventario. La entrada es el argumento en cuatro números; la profundidad se abre al clickear | Dos modos (Defensa proyectable + Inventario); entrada por los tres ejes de lectura |
| **D-2** | **La capa editorial la redacta Claude y la edita el usuario**, sacada del `description` de cada `campaign.yaml` y de la redacción de `results/index.md` | Derivación mecánica sin texto redactado; que el usuario escriba las 35 desde cero |
| **D-3** | **Tres niveles de profundidad**: resultado → desglose (condición / escenario / clip) → corrida. El desglose honra la limitación **L5** (nunca sólo el agregado) | Dos niveles sin desglose; cuatro niveles con el artefacto JSON crudo |
| **D-4** | **Una sola taxonomía de cinco clases** para Evidencia, Corridas y Experimentos, definida sobre los **21 roles** del registro, no sobre las 1.436 corridas | El binario actual; clasificar corrida por corrida |

Decisiones de diseño tomadas al dibujar, sujetas a revocación:

- **D-5** — **`bloques_ab` (23 corridas, el spike de fps F-RT5) va a Instrumento, no a
  Resultado.** Mejoró la plataforma un 18 %, pero el informe no cita una cifra suya como
  resultado del sistema de detección. Si el informe la cita, es Resultado.
- **D-6** — **`control_replay_empirico` (544 corridas) va a Resultado**: es el eje de
  densidad, el número 4 del argumento.
- **D-7** — **La entrada no muestra conteos de corridas por paso.** Los cuatro pasos suman
  1.717 porque 43 corridas pertenecen a dos resultados, mientras el total único es 1.436;
  mostrar ambos invita a restar. Además es justo el número que este rediseño deja de poner
  al frente.
- **D-8** — **La taxonomía no se codifica con color.** Cinco clases con cinco tonos
  chocarían con los tonos de estado reservados de la consola (`--live`, `--ok`, `--wn`,
  `--er`) y el violeta ahí es acción, no condición (regla escrita en `palette.ts`). La
  clase se lee por etiqueta y posición.

---

## 3. La taxonomía

Cinco clases, cada una con un **test operativo** para que la asignación no sea opinión:

| Clase | El test que la define | Roles |
|---|---|---|
| **Resultado** | *El informe cita una cifra suya.* Tiene fila en uno de los 4 índices de `results/` y la verifica `96-verificar-indices.py` | `campaign_media`, `campaign_control`, `control_replay_empirico`, `distribucion_live`, `benchmark_realtime`, `nivel_a_primaria`, `nivel_a_replica`, `seleccion_modelos`, `rodaje_ebe_final`, `contraste_resolucion`, `benchmark_modelos`, `confirmacion_estratos`, `extensibilidad_y_contraste_negativo` |
| **Instrumento** | *Mide o valida el aparato de medición, no el fenómeno.* Sostiene la credibilidad de un resultado sin ser uno | `claqueta_y_guards_negativos`, `control_live_y_replay`, `instrumentacion_g2a`, `bloques_ab` |
| **Ensayo** | *Existió para llegar al resultado:* preparación, ajuste, verificación post-cambio | `ensayo_ebe_1a1`, `smoke_ebe_post_cambios`, `media_live_e2e`, `validacion_integrada_distribucion` |
| **Prueba de plataforma** | *La máquina probándose a sí misma.* No es experimento en ningún sentido | Ningún rol del registro. Se asigna **sólo por excepción explícita** en `clasificacion.yaml`: los 5 slugs del orquestador (445 ejecuciones) y, si el usuario lo decide, corridas como `talert_camera_smoke` o `health` |
| **Sin clasificar** | Fuera del registro y sin excepción | Las **52** corridas de `/runs` que no figuran en ningún CSV. **Es el default**: nada cae acá por descarte silencioso ni sube a otra clase por heurística de nombre. Se muestran con su desglose crudo (48 exploratorias · 4 fallidas o interrumpidas) y se promueven de a una editando el YAML |

**Conteos reales al 2026-09-11** (`clase_de` = la primera clase presente en el orden
Resultado → Instrumento → Ensayo, porque una corrida puede cumplir dos roles):

- Registro completo, 1.436 corridas: **Resultado 1.402 · Instrumento 23 · Ensayo 11**
- Pantalla Corridas, 472 del media-plane: **Resultado 412 · Instrumento 4 · Ensayo 4 · fuera del registro 52** (43 `succeeded`, 5 `stopped`, 3 `failed`, 1 `interrupted`)
- Pantalla Experimentos, 459 ejecuciones: **Resultado 3 · Ensayo 11 · Prueba de plataforma 445** (`orq_1` 90, `orq_2a` 90, `orq_alerts_502` 89, `orq_alerts` 89, `gate_orq` 87)

**Por qué sobre los roles y no sobre las corridas:** son 21 decisiones revisables en una
sentada contra 1.436, y se propagan solas a cada corrida nueva.

---

## 4. La arquitectura de información

### 4.1 `/evidencia` — tres capas más una

```
/evidencia                    El argumento en cuatro números
  ├─ 1 · Qué ve el detector sin entrenar      mAP50 0,551        5 resultados
  ├─ 2 · Cómo expresar la condición           precision 0,146    5 resultados
  ├─ 3 · Qué agrega la plataforma             F1 0,789 → 0,930   7 resultados
  ├─ 4 · Qué sobrevive al tiempo real         4/4 densidades    13 resultados
  ├─ Respaldo instrumental                                       5 mediciones
  ├─ Por material (los 4 índices de results/)
  └─ Ejes de lectura (enlace a results/ejes/, NO se reimplementa)

/evidencia/paso?n=3           Los resultados de un número, con el hallazgo del paso
/evidencia/resultado?id=…     Reclamo · cifras · DESGLOSE · procedencia · corridas plegadas
/evidencia/run?plane=…        La corrida y su summary congelado (ya existe)
```

La partición de los 35 resultados es **total y disyunta**: 5 + 5 + 7 + 13 = 30 en el
recorrido, + 5 en respaldo instrumental = 35.

Los tres `results/ejes/` se **enlazan**, no se reimplementan: ya son documentos escritos y
duplicarlos crearía una segunda fuente de verdad.

### 4.2 Corridas

El filtro de clase deja 412 de 472: **casi no baja**. El arreglo real es la granularidad —
**las 472 corridas son 32 grupos por resultado**. La pantalla arranca agrupada, cada grupo
con su título redactado, su cifra de cabecera, su paso del recorrido y su clase; el grupo
se despliega a las corridas individuales.

### 4.3 Experimentos

Lo que ya funciona (la vista Evidencia con 1 manifiesto) se conserva. Cambia:
el lump «456 ejecuciones archivadas» se parte por clase, y las **445 ejecuciones sin
manifiesto** pasan a un bloque propio que dice qué son (la suite de tests escribe 5 por
corrida completa) y **cita la proporción, 97 % de 459, nunca el absoluto** — porque el
total crece solo.

---

## 5. La capa editorial

Cuatro archivos en `results/evidence-vista/` — **mutable, fuera del archivo congelado**,
por la razón ya escrita en `evidence.py`: los edita una persona y `results/evidence-runs/`
tiene integridad por hash (`files.sha256`).

| Archivo | Estado | Contenido |
|---|---|---|
| `consola.yaml` | existe | Excepciones de visibilidad. Sin cambios |
| `titulos.yaml` | **se extiende** | Por `result_id`: `titulo` (ya existe, hoy vacío) y **`reclamo`** nuevo — la frase de una línea que dice qué demuestra |
| `clasificacion.yaml` | **nuevo** | Los 21 roles → las 5 clases, más las excepciones por slug o por id para lo que está fuera del registro |
| `recorrido.yaml` | **nuevo** | Los 4 pasos (`n`, `titulo`, `claim`, `cifra`, `fuente`) y la lista ordenada de `result_id` de cada uno, más `respaldo_instrumental` |

Forma de `recorrido.yaml`:

```yaml
pasos:
  - n: 3
    titulo: Qué agrega la plataforma sobre la detección cruda
    claim: >
      La histéresis rescata percepción intermitente, pero es palanca de doble filo.
      La capa que más agrega es la identidad: el F1 sube con las detecciones bit a
      bit idénticas.
    cifra: "0,789 → 0,930"
    cifra_label: "F1, escena → sujeto"
    fuente: null          # null = leída de metrics.json; si no, la ruta que la cita
    resultados:
      - clip_bench/t1_gdinotiny560_v2short_scene
      - clip_bench/g1_gdinotiny560_v2short_subject
      # …
respaldo_instrumental:
  - realtime/claqueta_reloj_externo
  # …
```

---

## 6. Cifras: leída contra citada

La regla que impide que la consola se convierta en un lugar donde aparece un número que
ningún verificador chequea — el modo de falla que este proyecto ya sufrió una vez
(«el número estrella del TFG no tenía respaldo en el repo», `informe/ajustes/gobierno/95` §2.1).

- **Cifra leída** — la consola la lee de `results/<result_id>/metrics.json` **al
  renderizar**. No puede desviarse. 17 de 35 resultados.
- **Cifra citada** — escrita a mano en la capa editorial, **con su `fuente`**. 18 de 35, más
  el número 1 del recorrido (`mAP50 0,551`, que vive en `results/bench_imagenes/index.md` y
  no tiene `metrics.json` en este repo). **Se marca en pantalla** (subrayado punteado) y
  muestra su fuente: nunca se disfraza de leída.

### 6.1 Adaptadores por esquema

Los `metrics.json` **no comparten forma**. Cuatro adaptadores en el backend, cada uno
declarando qué campos lee:

| Esquema | Resultados | Cabecera | Desglose |
|---|---|---|---|
| `clip_campaign_metrics.v1` | las 14 de `clip_bench` | `f1_micro`, `recall_micro`, `precision_micro` | `by_condition`, `by_scenario`, `by_clip`, `negatives` |
| `clip_person_state.v1` | `bench_nivel_a/na1` | `agregado` CR-01 / CR-02 | `por_clip` |
| sin `schema_version` | `bench_nivel_a/d1_gdinotiny560_edir_vs_eind` | `gate` | `strata`, `complementarity` |
| propio | `realtime/t_alert_notification` | p95 | fases |

**Trampa:** el `metrics.json` de `bench_nivel_a/d1_…` **no tiene `schema_version`**. El
despacho es: por `schema_version` cuando está; si no, por sonda de forma; y una forma
desconocida **degrada a «sin cabecera leída»**, nunca adivina.

---

## 7. El contrato congelado: la restricción dura

`webconsole/frontend/src/__tests__/contrato/` **debe seguir dando 10/10 sin tocarse**. Eso
acota el diseño de dos maneras verificadas:

1. **Ninguno de los cuatro archivos del contrato menciona `/evidencia`** → la pantalla se
   puede rediseñar entera, con rutas y endpoints nuevos, sin riesgo.
2. **`ExperimentsPage` SÍ está montada por el contrato**
   (`experimentos-distribucion.contrato.test.tsx`), y el arnés de `soporte.tsx` **falla
   ante cualquier ruta HTTP imprevista, incluso si la pantalla la absorbe en un `catch`**.

De (2) salen dos reglas no negociables:

- La clase y el bloque de los 445 smokes **viajan en la respuesta de
  `/api/experiments/manifests` que ya existe**. Ningún endpoint nuevo desde esa pantalla.
- Los campos nuevos son **opcionales**, y la pantalla **renderiza correctamente cuando
  faltan** — la fixture `manifiestos` del contrato no los trae.

`RunsPage` no está cubierta (el contrato monta `RunDetailPage`, `ComposePage` y
`ComparePage`), pero se le aplica la misma disciplina.

El default de la API sigue siendo `vista=todas`: **quien elige la vista es la pantalla**. El
parámetro `clase` se agrega **junto a** `vista`, no en su lugar.

---

## 8. Alcance

**Backend** (`webconsole/backend/src/eovrt_webconsole/`)
- `evidence.py` — vocabulario de clases, carga de `clasificacion.yaml`, `clase_de(run_id)`
- `evidence_archive.py` — adaptadores de métricas, carga de `recorrido.yaml` y del
  `reclamo`, nueva forma del índice
- `routers/evidencia.py` — `/api/evidencia` (el recorrido), `/api/evidencia/paso`,
  y `/resultado` extendido con desglose
- `routers/runs.py` — parámetro `clase`, agrupación por resultado
- `routers/experiments.py` — `clase` y el agregado `sin_manifiesto`, **ambos opcionales**

**Frontend** (`webconsole/frontend/src/`)
- `pages/EvidencePage.tsx` — se parte en los cuatro niveles (hoy son 133 líneas con tres
  niveles en un solo componente; crece lo suficiente como para separarlos)
- `pages/RunsPage.tsx`, `pages/ExperimentsPage.tsx` — chips de clase, agrupación, bloque
  de smokes
- `components/EvidenceViewControl.tsx` — el segmentado de 3 pasa a chips de clase
- `types.ts`, `api/endpoints.ts`, `styles/ui.css`

**Configuración** — `clasificacion.yaml` y `recorrido.yaml` nuevos; `titulos.yaml` extendido
con los 35 títulos y reclamos redactados.

---

## 9. Tests

**Nuevos, todos con el patrón anti-envejecimiento del chequeo (c) de
`96-verificar-indices.py` — fallar en vez de esconder:**

1. **Cobertura de roles** — todo rol presente en los CSV está en **exactamente una** clase.
   Un rol nuevo sin clasificar **falla**.
2. **Partición del recorrido** — los 35 `result_id` se reparten en exactamente un paso o en
   respaldo instrumental. **Total y disyunta**: ninguno invisible, ninguno contado dos veces.
3. **Cifra citada contra su fuente** — toda `cifra` con `fuente` aparece **literalmente** en
   el archivo que nombra. Es el chequeo (b) de `96-verificar-indices.py` aplicado a la consola.
4. **Despacho de adaptadores** — los 17 resultados con `metrics.json` despachan a un
   adaptador. Una campaña nueva con esquema desconocido **falla**.
5. **Render** — la entrada, un paso, un resultado con desglose, y los estados
   `not_applicable` (P3/P5 se declaran, no se cuentan como cero).

**Se actualizan:** `EvidencePage.test.tsx`, `EvidenceView.test.tsx`,
`ExperimentsEvidence.test.tsx`, `test_evidence.py`, `test_evidence_archive.py`.

**El gate:** `webconsole/frontend/src/__tests__/contrato/` 10/10 **sin tocarse**, contra el
árbol nuevo. Más las suites completas: backend 813+, frontend 467+.

---

## 10. Qué NO se toca

- `results/evidence-runs/` — el archivo congelado, su `files.sha256` y los cuatro CSV
- `results/evidence-runs.yaml` — el manifiesto de procedencia
- Los cuatro índices de `results/` — siguen siendo la fuente de las cifras
- El contrato congelado — ni un archivo
- El default `vista=todas` de la API
- La propiedad de que `/evidencia` no consulte ningún servicio

---

## 11. Hallazgos abiertos, que este trabajo no resuelve

- **`bench_nivel_a` muestra 4 resultados donde `results/index.md` declara 2 campañas.**
  `edir_vs_eind` y `replica_base560` (fuentes estructuradas) conviven con
  `d1_gdinotiny560_edir_vs_eind` (campaña). Puede ser la misma medición contada dos veces.
  **Se reporta, no se corrige por iniciativa propia**: tocar eso es tocar la procedencia.
- **El badge del sidebar de Experimentos dice 11 mientras la pantalla muestra 1.**
- **La pantalla dice «1 manifiestos».**

---

## 12. Riesgos

| Riesgo | Mitigación |
|---|---|
| Un número redactado a mano termina frente al tribunal sin verificar | Test 3: toda cifra citada aparece literalmente en su fuente declarada |
| El texto editorial dice algo que el informe no dice | Los títulos y reclamos salen del `description` de `campaign.yaml` y de `results/index.md`; el usuario los edita en YAML sin tocar código |
| La pantalla envejece en silencio cuando aparece una campaña nueva | Tests 1, 2 y 4 fallan en vez de esconder |
| Romper el contrato congelado desde Experimentos | Campos opcionales, cero rutas nuevas desde esa pantalla, y el contrato se corre antes y después |
| Mostrar el agregado sin desglose | El desglose es parte de la capa 2, no un opcional (limitación L5) |
