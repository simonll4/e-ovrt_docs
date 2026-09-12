# Recorrido de evidencia y taxonomía de clases — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Que `/evidencia` entre por el argumento del informe en vez de por la carpeta del archivo, y que Evidencia, Corridas y Experimentos clasifiquen todo con la misma taxonomía de cinco clases.

**Architecture:** Una capa editorial en YAML (mutable, fuera del archivo congelado) define los títulos, los cuatro pasos del recorrido y la clase de cada uno de los 21 roles del registro. El backend lee esa capa más los `metrics.json` que ya están en `results/`, con un adaptador por esquema de métricas. El frontend rearma `/evidencia` en tres niveles y agrega filtros de clase a Corridas y Experimentos. Nada de esto consulta a los servicios.

**Tech Stack:** Python 3.11+ / FastAPI / pytest (backend) · React 18 + TanStack Query + TanStack Table / Vitest + Testing Library (frontend) · PyYAML

**Spec:** `docs/superpowers/specs/2026-09-11-consola-evidencia-recorrido-taxonomia-design.md`

**Mockups (la fuente del markup):** `e-ovrt_experimental-setup/docs/rediseno-consola/mockups-evidencia/` — cinco archivos `.dc.html`, uno por pantalla. Son HTML completo y legible: **abrir el que corresponde antes de escribir cada componente y copiar de ahí la anatomía exacta** (jerarquía, columnas, textos). Los hex están inlineados porque un artboard no puede importar `tokens.css`; al portar, **usar siempre las variables CSS**, nunca los literales. Versión navegable: https://claude.ai/code/artifact/28eb5e84-c842-4d97-9df3-ee8c29fa66f2

## Global Constraints

- **Repo:** `e-ovrt_experimental-setup`, rama `feature/webconsole-adopcion-front-design`. Todos los comandos corren desde `webconsole/backend` o `webconsole/frontend` salvo que se diga otra cosa.
- **Venv del backend:** `webconsole/backend` usa su propio venv. Comando de tests: `cd webconsole/backend && python -m pytest -q`.
- **Frontend:** `cd webconsole/frontend && npm test`.
- **NUNCA commitear sin que el usuario lo pida en ese turno.** Los pasos "Commit" de este plan se ejecutan **sólo** si el usuario lo autorizó explícitamente; si no, se deja el árbol sucio y se le avisa. Nunca agregar `Co-Authored-By`.
- **El contrato congelado (`webconsole/frontend/src/__tests__/contrato/`) no se toca y debe dar 10/10** contra el árbol nuevo. Es el gate de cada tarea que toque frontend.
- **`ExperimentsPage` está montada por el contrato** (`experimentos-distribucion.contrato.test.tsx`) y el arnés falla ante cualquier ruta HTTP imprevista, incluso absorbida en un `catch`. Desde esa pantalla: **cero endpoints nuevos**; los datos nuevos viajan en **cabeceras `X-`** de `/api/experiments/manifests`, y todo campo nuevo es **opcional** con render correcto cuando falta.
- **`RunsPage` NO está cubierta** por el contrato (monta `RunDetailPage`, `ComposePage`, `ComparePage`): ahí sí se pueden agregar rutas.
- **No se toca** `results/evidence-runs/` (archivo congelado con `files.sha256`), `results/evidence-runs.yaml`, ni los cuatro CSV de `collections/`.
- **El default de la API sigue siendo `vista=todas`.** El parámetro `clase` se agrega **junto a** `vista`, nunca en su lugar.
- **Cifras:** una cifra mostrada es **leída** de un `metrics.json` en `results/`, o **citada** con una `fuente` donde aparece **literalmente**. No hay tercera opción. Las citadas se marcan en la UI.
- **Limitación L5:** nunca mostrar un agregado sin su desglose por estrato/escenario.
- **Estados `not_applicable`:** lo que no tiene dato se declara, no se dibuja como cero.

---

## Estructura de archivos

**Se crean:**

| Archivo | Responsabilidad |
|---|---|
| `results/evidence-vista/clasificacion.yaml` | Los 21 roles → 5 clases + excepciones por slug/id |
| `results/evidence-vista/recorrido.yaml` | Los 4 pasos, sus cifras y el reparto de los 35 `result_id` |
| `webconsole/backend/src/eovrt_webconsole/evidence_metrics.py` | Los 4 adaptadores de `metrics.json` y su despacho |
| `webconsole/backend/tests/test_evidence_clases.py` | Tests 1 y 2 (cobertura de roles, partición del recorrido) |
| `webconsole/backend/tests/test_evidence_metrics.py` | Tests 3 y 4 (cifra citada contra fuente, despacho) |
| `webconsole/frontend/src/pages/evidencia/Entrada.tsx` | Nivel 0: el recorrido en cuatro números |
| `webconsole/frontend/src/pages/evidencia/Paso.tsx` | Nivel 1: los resultados de un número |
| `webconsole/frontend/src/pages/evidencia/Resultado.tsx` | Nivel 2: reclamo, cifras, desglose, procedencia, corridas |
| `webconsole/frontend/src/pages/evidencia/Desglose.tsx` | La tabla con barra de una sola tinta (condición / escenario / clip) |
| `webconsole/frontend/src/components/ClaseChips.tsx` | Los chips de clase, compartidos por Corridas y Experimentos |

**Se modifican:**

| Archivo | Cambio |
|---|---|
| `backend/src/eovrt_webconsole/evidence.py` | Vocabulario de clases, carga de `clasificacion.yaml`, `clase_de()` |
| `backend/src/eovrt_webconsole/evidence_archive.py` | Carga de `recorrido.yaml` y del `reclamo`; índice con forma de recorrido; desglose en `result()` |
| `backend/src/eovrt_webconsole/routers/evidencia.py` | `/paso` nuevo; `/resultado` con desglose |
| `backend/src/eovrt_webconsole/routers/runs.py` | Parámetros `clase` y `result_id`; ruta `/api/runs/grupos` |
| `backend/src/eovrt_webconsole/routers/experiments.py` | `clase` por manifiesto + cabeceras `X-Platform-Test-*` |
| `frontend/src/pages/EvidencePage.tsx` | Pasa a ser el router de los cuatro niveles |
| `frontend/src/pages/RunsPage.tsx` | Chips de clase + tabla agrupada |
| `frontend/src/pages/ExperimentsPage.tsx` | Chips de clase + bloque de pruebas de plataforma |
| `frontend/src/components/EvidenceViewControl.tsx` | El segmentado de 3 se reemplaza por `ClaseChips` |
| `frontend/src/types.ts`, `frontend/src/api/endpoints.ts`, `frontend/src/styles/ui.css`, `frontend/src/App.tsx` | Tipos, cliente, estilos, rutas |
| `results/evidence-vista/titulos.yaml` | 35 `titulo` y 35 `reclamo` redactados |

---

## Task 1: Vocabulario de clases y `clasificacion.yaml`

**Files:**
- Create: `results/evidence-vista/clasificacion.yaml`
- Modify: `webconsole/backend/src/eovrt_webconsole/evidence.py`
- Test: `webconsole/backend/tests/test_evidence_clases.py`

**Interfaces:**
- Consumes: `EvidenceRegistry._rows` y `EvidenceRegistry.config_dir`, que ya existen.
- Produces:
  - `CLASES: tuple[str, ...] = ("resultado", "instrumento", "ensayo", "plataforma", "sin_clasificar")`
  - `EvidenceRegistry.clase_de_rol(rol: str) -> str`
  - `EvidenceRegistry.clase_de(run_id: str) -> str` — la primera clase presente en el orden de `CLASES` entre los roles de esa corrida; `"sin_clasificar"` si no está en el registro.
  - `EvidenceRegistry.roles_sin_clasificar() -> list[str]`

- [ ] **Step 1: Escribir `clasificacion.yaml`**

Crear `results/evidence-vista/clasificacion.yaml`:

```yaml
# La clase de cada rol del registro. Son 21 roles para 1.436 corridas: se
# clasifica el rol, no la corrida, y se propaga solo.
#
# El test `test_todo_rol_tiene_clase` falla si aparece un rol nuevo sin
# clasificar. Eso es deliberado: preferimos romper el build antes que mostrar
# una corrida nueva como "Resultado" por descarte.
roles:
  resultado:
    - campaign_media
    - campaign_control
    - control_replay_empirico
    - distribucion_live
    - benchmark_realtime
    - nivel_a_primaria
    - nivel_a_replica
    - seleccion_modelos
    - rodaje_ebe_final
    - contraste_resolucion
    - benchmark_modelos
    - confirmacion_estratos
    - extensibilidad_y_contraste_negativo
  instrumento:
    - claqueta_y_guards_negativos
    - control_live_y_replay
    - instrumentacion_g2a
    - bloques_ab
  ensayo:
    - ensayo_ebe_1a1
    - smoke_ebe_post_cambios
    - media_live_e2e
    - validacion_integrada_distribucion
  plataforma: []

# Excepciones para lo que NO tiene rol en el registro. El default de todo lo
# demás es `sin_clasificar`: nada sube de clase por heurística de nombre.
excepciones:
  plataforma:
    - orq_1
    - orq_2a
    - orq_alerts
    - orq_alerts_502
    - gate_orq
```

- [ ] **Step 2: Escribir el test que falla**

Crear `webconsole/backend/tests/test_evidence_clases.py`:

```python
"""La taxonomía se define sobre los roles del registro, no sobre las corridas."""
import csv
import glob
from pathlib import Path

import pytest
import yaml

from eovrt_webconsole.evidence import CLASES, EvidenceRegistry

REPO = Path(__file__).resolve().parents[3]
VISTA = REPO / 'results/evidence-vista'


def roles_del_registro() -> set[str]:
    roles = set()
    for path in glob.glob(str(REPO / 'results/evidence-runs/collections/*.csv')):
        with open(path, newline='', encoding='utf-8') as src:
            roles.update(row['role'] for row in csv.DictReader(src))
    return roles


def test_todo_rol_tiene_exactamente_una_clase():
    """Un rol nuevo sin clasificar FALLA. Es el chequeo anti-envejecimiento."""
    data = yaml.safe_load((VISTA / 'clasificacion.yaml').read_text(encoding='utf-8'))
    declarados = [rol for clase in data['roles'].values() for rol in clase]
    assert len(declarados) == len(set(declarados)), 'un rol declarado en dos clases'
    faltan = roles_del_registro() - set(declarados)
    assert not faltan, f'roles sin clase en clasificacion.yaml: {sorted(faltan)}'


def test_las_clases_declaradas_son_las_del_vocabulario():
    data = yaml.safe_load((VISTA / 'clasificacion.yaml').read_text(encoding='utf-8'))
    assert set(data['roles']) <= set(CLASES)
    assert set(data.get('excepciones', {})) <= set(CLASES)


def test_clase_de_run_toma_la_mas_fuerte(tmp_path):
    """Una corrida con dos roles se clasifica por el más fuerte, no por el primero."""
    registry = _registro(tmp_path, [
        ('resultado_role', 'campaign_media', 'm1'),
        ('instrumento_role', 'bloques_ab', 'm1'),
    ])
    assert registry.clase_de('m1') == 'resultado'


def test_run_fuera_del_registro_es_sin_clasificar(tmp_path):
    registry = _registro(tmp_path, [('x', 'campaign_media', 'm1')])
    assert registry.clase_de('desconocida') == 'sin_clasificar'


def _registro(tmp_path: Path, filas) -> EvidenceRegistry:
    from eovrt_webconsole.evidence import CSV_FILES
    archive = tmp_path / 'evidence-runs'
    (archive / 'collections').mkdir(parents=True)
    campos = ['collection', 'result_id', 'role', 'plane', 'run_id', 'status',
              'source_ref', 'artifact_path']
    for nombre in CSV_FILES:
        with (archive / 'collections' / nombre).open('w', newline='') as dst:
            writer = csv.writer(dst)
            writer.writerow(campos)
            if nombre == 'shared.csv':
                for result_id, rol, run_id in filas:
                    writer.writerow(['shared', result_id, rol, 'media-plane', run_id,
                                     'copied', 'x.json', 'artifacts/x'])
    config = tmp_path / 'evidence-vista'
    config.mkdir()
    (config / 'clasificacion.yaml').write_text(
        (VISTA / 'clasificacion.yaml').read_text(encoding='utf-8'), encoding='utf-8')
    return EvidenceRegistry(archive, config)
```

- [ ] **Step 3: Correr el test para verificar que falla**

Run: `cd webconsole/backend && python -m pytest tests/test_evidence_clases.py -q`
Expected: FAIL con `ImportError: cannot import name 'CLASES'`.

- [ ] **Step 4: Implementar en `evidence.py`**

Agregar arriba, junto a `Vista`:

```python
CLASES: tuple[str, ...] = ("resultado", "instrumento", "ensayo", "plataforma", "sin_clasificar")
```

Dentro de `EvidenceRegistry.__init__`, después del bloque que carga `consola.yaml`:

```python
        # La clase se declara por ROL, no por corrida: 21 decisiones en vez de
        # 1.436, y una corrida nueva hereda la clase de su rol sin tocar nada.
        self._clase_de_rol: dict[str, str] = {}
        self._clase_forzada: dict[str, str] = {}
        clasificacion = self.config_dir / "clasificacion.yaml"
        if clasificacion.is_file():
            data = yaml.safe_load(clasificacion.read_text(encoding="utf-8")) or {}
            for clase, roles in (data.get("roles") or {}).items():
                if clase not in CLASES:
                    raise ValueError(f"clasificacion.yaml: clase desconocida {clase}")
                for rol in roles:
                    if rol in self._clase_de_rol:
                        raise ValueError(f"clasificacion.yaml: {rol} declarado dos veces")
                    self._clase_de_rol[rol] = clase
            for clase, entradas in (data.get("excepciones") or {}).items():
                if clase not in CLASES:
                    raise ValueError(f"clasificacion.yaml: clase desconocida {clase}")
                for entrada in entradas:
                    self._clase_forzada[entrada] = clase
```

Y los métodos, después de `es_evidencia`:

```python
    def clase_de_rol(self, rol: str) -> str:
        return self._clase_de_rol.get(rol, "sin_clasificar")

    def clase_de(self, run_id: str) -> str:
        """La clase MÁS FUERTE entre los roles de la corrida.

        Una corrida puede cumplir dos roles (es evidencia de dos resultados). El
        orden de `CLASES` es la precedencia: si algo es Resultado en algún lado,
        es Resultado.
        """
        if run_id in self._clase_forzada:
            return self._clase_forzada[run_id]
        clases = {self.clase_de_rol(row["role"]) for row in self._rows.get(run_id, [])}
        return next((c for c in CLASES if c in clases), "sin_clasificar")

    def roles_sin_clasificar(self) -> list[str]:
        return sorted({row["role"] for rows in self._rows.values() for row in rows
                       if row["role"] not in self._clase_de_rol})
```

- [ ] **Step 5: Correr los tests para verificar que pasan**

Run: `cd webconsole/backend && python -m pytest tests/test_evidence_clases.py -q`
Expected: PASS, 4 tests.

- [ ] **Step 6: Correr la suite del backend entera**

Run: `cd webconsole/backend && python -m pytest -q`
Expected: los 813+ que ya pasaban, más los 4 nuevos. Cero fallas.

- [ ] **Step 7: Commit — SÓLO si el usuario lo pidió en este turno**

```bash
git add results/evidence-vista/clasificacion.yaml \
        webconsole/backend/src/eovrt_webconsole/evidence.py \
        webconsole/backend/tests/test_evidence_clases.py
git commit -m "feat(webconsole): taxonomía de clases sobre los roles del registro"
```

---

## Task 2: La capa editorial — `recorrido.yaml` y los 35 títulos

**Files:**
- Create: `results/evidence-vista/recorrido.yaml`
- Modify: `results/evidence-vista/titulos.yaml`
- Test: `webconsole/backend/tests/test_evidence_clases.py` (se agregan tests)

**Interfaces:**
- Consumes: los 35 `result_id` que produce `EvidenceRegistry.resultados()`.
- Produces: el archivo `recorrido.yaml` con la forma que Task 4 lee.

- [ ] **Step 1: Escribir `recorrido.yaml`**

Crear `results/evidence-vista/recorrido.yaml`. **Toda cifra es leída (`leer:`) o citada
(`cifra:` + `fuente:`); nunca las dos ni ninguna.**

```yaml
# El recorrido del argumento del informe. La partición de los 35 result_id entre
# los cuatro pasos y `respaldo_instrumental` es TOTAL y DISYUNTA: el test
# `test_recorrido_particiona_los_resultados` falla si alguno queda afuera o en dos.
pasos:
  - n: 1
    titulo: Qué ve el detector sin entrenar
    claim: >
      El campeón zero-shot sobre 6.477 imágenes de tres fuentes independientes.
      La asimetría es estructural: person y helmet sólidas, vest débil,
      bare_head fuerte sólo en el especialista.
    cifra: "0,551"
    cifra_label: mAP50, bench_v3 completo
    cifra_nota: gdino-tiny-560 · 560 / 0,30
    fuente: results/bench_imagenes/index.md
    resultados:
      - bench_imagenes/seleccion_s1
      - bench_imagenes/confirmacion_b5
      - bench_imagenes/gdino560
      - bench_imagenes/modelos_crudos
      - bench_imagenes/clase_nueva

  - n: 2
    titulo: Cómo conviene expresar la condición
    claim: >
      Evidencia positiva más inferencia (E-IND) le gana a los prompts directos de
      ausencia (E-DIR) en los dos niveles. A Nivel B decide el criterio
      pre-registrado: el veto de precisión descarta E-DIR como núcleo. Lo que
      manda es la formulación, no el mecanismo.
    cifra_label: precision de E-DIR (veto < 0,5)
    cifra_nota: contra 0,757 de E-IND
    leer:
      - result_id: clip_bench/d1_gdinotiny560_edirpair_scene
        campo: precision_micro
    resultados:
      - bench_nivel_a/d1_gdinotiny560_edir_vs_eind
      - bench_nivel_a/edir_vs_eind
      - bench_nivel_a/replica_base560
      - bench_nivel_a/na1_gdinotiny560_v2short_video
      - clip_bench/d1_gdinotiny560_edirpair_scene

  - n: 3
    titulo: Qué agrega la plataforma sobre la detección cruda
    claim: >
      La histéresis rescata percepción intermitente, pero es palanca de doble
      filo. La capa que más agrega es la identidad: el F1 sube con las
      detecciones bit a bit idénticas. El margen no estaba en el modelo.
    cifra_label: F1, escena → sujeto
    cifra_nota: mismas detecciones
    leer:
      - result_id: clip_bench/t1_gdinotiny560_v2short_scene
        campo: f1_micro
      - result_id: clip_bench/g1_gdinotiny560_v2short_subject
        campo: f1_micro
    resultados:
      - clip_bench/t1_gdinotiny560_v2short_scene
      - clip_bench/g1_gdinotiny560_v2short_subject
      - clip_bench/t2_gdinobase560_v2short_scene
      - clip_bench/b1_gdinobase560_barehead_scene
      - clip_bench/h1_gdinotiny560_hybor_scene
      - clip_bench/i1_gdinotiny560_v2short_scene_internet
      - clip_bench/i2_gdinotiny560_v2short_subject_internet

  - n: 4
    titulo: Qué sobrevive al tiempo real
    claim: >
      La ganancia de la identidad excluye el cero en las cuatro densidades
      medidas, y conserva la dirección bajo el descarte irregular del camino en
      vivo. Es la única palanca del banco significativa bajo esa restricción.
    # La cifra es el par a stride 7, LEÍDO. El "4/4" vive en el claim, que es
    # prosa editorial: no se muestra como cifra porque el índice lo escribe con
    # letras ("las cuatro densidades") y no pasaría la verificación literal.
    cifra_label: F1 escena → sujeto, stride 7
    cifra_nota: la ganancia sobrevive al decimado
    leer:
      - result_id: clip_bench/r1_gdinotiny560_v2short_scene_s7
        campo: f1_micro
      - result_id: clip_bench/r2_gdinotiny560_v2short_subject_s7
        campo: f1_micro
    resultados:
      - clip_bench/r1_gdinotiny560_v2short_scene_s7
      - clip_bench/r2_gdinotiny560_v2short_subject_s7
      - clip_bench/r3_gdinotiny560_v2short_scene_s15
      - clip_bench/r4_gdinotiny560_v2short_subject_s15
      - clip_bench/r5_gdinotiny560_v2short_scene_s26
      - clip_bench/r6_gdinotiny560_v2short_subject_s26
      - realtime/decimado_empirico
      - realtime/descarte_irregular
      - realtime/matriz_modelo_fuente
      - realtime/t_alert_notification
      - realtime/rodaje_seis_corridas
      - realtime/g2a_single_host
      - realtime/gdino560

respaldo_instrumental:
  titulo: Respaldo instrumental
  claim: >
    Lo que valida el aparato de medición, no el fenómeno: la claqueta con reloj
    externo, la paridad vivo contra archivo del bus, la instrumentación del G2A.
  resultados:
    - realtime/claqueta_reloj_externo
    - realtime/bus_live_paridad
    - realtime/frt5_roundtrip_pil
    - realtime/regresion_g1_live
    - realtime/l0
```

- [ ] **Step 2: Reescribir `titulos.yaml` con los 35 títulos y reclamos**

Reemplazar el contenido de `results/evidence-vista/titulos.yaml` (mantiene la clave
`resultados` y el campo `etiqueta`; se llenan `titulo` y se agrega `reclamo`):

```yaml
# Los títulos y reclamos que ve el tribunal. Redactados desde el `description` de
# cada campaign.yaml y desde results/index.md. Editables sin tocar código.
resultados:
  - result_id: bench_imagenes/modelos_crudos
    etiqueta: "modelos crudos"
    titulo: Los seis modelos crudos, sin adaptar
    reclamo: El punto de partida, antes de elegir nada.
  - result_id: bench_imagenes/seleccion_s1
    etiqueta: "seleccion s1"
    titulo: La selección del campeón (S1)
    reclamo: Veinte combinaciones sobre bench_v3; gana gdino-tiny-560, robusto a la fuente.
  - result_id: bench_imagenes/confirmacion_b5
    etiqueta: "confirmacion b5"
    titulo: Confirmación por estratos (B5)
    reclamo: El campeón sostiene el resultado en cada una de las tres fuentes por separado.
  - result_id: bench_imagenes/gdino560
    etiqueta: "gdino560"
    titulo: El contraste de resolución, 560 contra 800
    reclamo: 560 baja la latencia un 24 % con mAP igual o mejor.
  - result_id: bench_imagenes/clase_nueva
    etiqueta: "clase nueva"
    titulo: El costo de agregar una clase nueva
    reclamo: Cuánto cuesta extender el vocabulario sin reentrenar.
  - result_id: bench_nivel_a/d1_gdinotiny560_edir_vs_eind
    etiqueta: "d1 gdinotiny560 edir vs eind"
    titulo: E-DIR contra E-IND por sujeto (D1)
    reclamo: La comparación pre-registrada entre las dos formulaciones, a nivel de persona.
  - result_id: bench_nivel_a/edir_vs_eind
    etiqueta: "edir vs eind"
    titulo: E-DIR contra E-IND, la fuente estructurada
    reclamo: El artefacto de medición del que sale la comparación de formulaciones.
  - result_id: bench_nivel_a/replica_base560
    etiqueta: "replica base560"
    titulo: La réplica con base-560
    reclamo: La misma comparación con el modelo grande, para separar formulación de capacidad.
  - result_id: bench_nivel_a/na1_gdinotiny560_v2short_video
    etiqueta: "na1 gdinotiny560 v2short video"
    titulo: Estado por persona sobre video (NA1)
    reclamo: Nivel A sobre los clips: el derrumbe de precision al salir de las imágenes.
  - result_id: clip_bench/t1_gdinotiny560_v2short_scene
    etiqueta: "t1 gdinotiny560 v2short scene"
    titulo: Línea de base del Nivel B
    reclamo: Primera campaña sobre GT temporal humano. Toda campaña posterior se compara contra ésta.
  - result_id: clip_bench/g1_gdinotiny560_v2short_subject
    etiqueta: "g1 gdinotiny560 v2short subject"
    titulo: La identidad por sujeto
    reclamo: El F1 sube de 0,789 a 0,930 con las detecciones bit a bit idénticas.
  - result_id: clip_bench/t2_gdinobase560_v2short_scene
    etiqueta: "t2 gdinobase560 v2short scene"
    titulo: Contraste de modelo, base-560
    reclamo: El modelo grande sobre el mismo banco: no alcanza a la identidad.
  - result_id: clip_bench/b1_gdinobase560_barehead_scene
    etiqueta: "b1 gdinobase560 barehead scene"
    titulo: El especialista de bare_head
    reclamo: El prompt set de banco con el modelo base: gana SDR y pierde precision.
  - result_id: clip_bench/h1_gdinotiny560_hybor_scene
    etiqueta: "h1 gdinotiny560 hybor scene"
    titulo: La histéresis, palanca de doble filo
    reclamo: Rescata percepción intermitente y multiplica los falsos positivos.
  - result_id: clip_bench/d1_gdinotiny560_edirpair_scene
    etiqueta: "d1 gdinotiny560 edirpair scene"
    titulo: Los prompts directos de ausencia (E-DIR)
    reclamo: Precision 0,146: el veto pre-registrado la descarta como núcleo.
  - result_id: clip_bench/i1_gdinotiny560_v2short_scene_internet
    etiqueta: "i1 gdinotiny560 v2short scene internet"
    titulo: Obra real no guionada, por escena
    reclamo: Dos episodios evaluables. Acotado por la limitación L4.
  - result_id: clip_bench/i2_gdinotiny560_v2short_subject_internet
    etiqueta: "i2 gdinotiny560 v2short subject internet"
    titulo: Obra real no guionada, por sujeto
    reclamo: La fragmentación de identidades en multitud, medida.
  - result_id: clip_bench/r1_gdinotiny560_v2short_scene_s7
    etiqueta: "r1 gdinotiny560 v2short scene s7"
    titulo: Densidad stride 7, por escena
    reclamo: Un frame de cada siete; el banco sigue evaluable.
  - result_id: clip_bench/r2_gdinotiny560_v2short_subject_s7
    etiqueta: "r2 gdinotiny560 v2short subject s7"
    titulo: Densidad stride 7, por sujeto
    reclamo: La ganancia de la identidad sobrevive al primer nivel de decimado.
  - result_id: clip_bench/r3_gdinotiny560_v2short_scene_s15
    etiqueta: "r3 gdinotiny560 v2short scene s15"
    titulo: Densidad stride 15, por escena
    reclamo: Un frame de cada quince.
  - result_id: clip_bench/r4_gdinotiny560_v2short_subject_s15
    etiqueta: "r4 gdinotiny560 v2short subject s15"
    titulo: Densidad stride 15, por sujeto
    reclamo: La ganancia se conserva a la mitad de la densidad.
  - result_id: clip_bench/r5_gdinotiny560_v2short_scene_s26
    etiqueta: "r5 gdinotiny560 v2short scene s26"
    titulo: Densidad stride 26, por escena
    reclamo: El ancla del techo live de hoy.
  - result_id: clip_bench/r6_gdinotiny560_v2short_subject_s26
    etiqueta: "r6 gdinotiny560 v2short subject s26"
    titulo: Densidad stride 26, por sujeto
    reclamo: La cuarta densidad: la ganancia sigue excluyendo el cero.
  - result_id: realtime/decimado_empirico
    etiqueta: "decimado empirico"
    titulo: El decimado empírico
    reclamo: Las mismas detecciones decimadas, para separar el efecto del instrumento.
  - result_id: realtime/descarte_irregular
    etiqueta: "descarte irregular"
    titulo: El descarte irregular del camino en vivo
    reclamo: La ganancia de la identidad conserva el signo bajo el descarte real.
  - result_id: realtime/matriz_modelo_fuente
    etiqueta: "matriz modelo fuente"
    titulo: La matriz modelo por fuente en vivo
    reclamo: Qué combinación sostiene el vivo y a qué fps.
  - result_id: realtime/t_alert_notification
    etiqueta: "t alert notification"
    titulo: Del bus de alertas al PUBACK MQTT
    reclamo: La distribución no es el cuello: un orden de magnitud menos que el G2A.
  - result_id: realtime/rodaje_seis_corridas
    etiqueta: "rodaje seis corridas"
    titulo: Las seis corridas del rodaje en vivo
    reclamo: La plataforma completa, de cámara a alerta, con hardware real.
  - result_id: realtime/g2a_single_host
    etiqueta: "g2a single host"
    titulo: El G2A en un solo host
    reclamo: Captura a alerta por frame, sin red de por medio.
  - result_id: realtime/gdino560
    etiqueta: "gdino560"
    titulo: 560 en tiempo real
    reclamo: Lo que la resolución del campeón cuesta en el camino vivo.
  - result_id: realtime/claqueta_reloj_externo
    etiqueta: "claqueta reloj externo"
    titulo: La claqueta con reloj externo
    reclamo: El G2A se mide desde el dequeue, no desde el fotón. Valida el reloj.
  - result_id: realtime/bus_live_paridad
    etiqueta: "bus live paridad"
    titulo: Paridad vivo contra archivo del bus
    reclamo: Toda corrida live es re-evaluable offline y produce artefactos idénticos.
  - result_id: realtime/frt5_roundtrip_pil
    etiqueta: "frt5 roundtrip pil"
    titulo: El round-trip PIL (F-RT5)
    reclamo: De dónde salían los fps perdidos en la ingesta.
  - result_id: realtime/regresion_g1_live
    etiqueta: "regresion g1 live"
    titulo: Regresión de G1 en vivo
    reclamo: Verificación de que la identidad no se rompió en el camino vivo.
  - result_id: realtime/l0
    etiqueta: "l0"
    titulo: El ensayo previo al rodaje (L0)
    reclamo: La corrida de preparación que habilitó el día de rodaje.
```

- [ ] **Step 3: Escribir los tests que fallan**

Agregar a `webconsole/backend/tests/test_evidence_clases.py`:

```python
def _recorrido() -> dict:
    return yaml.safe_load((VISTA / 'recorrido.yaml').read_text(encoding='utf-8'))


def _resultados_del_registro() -> set[str]:
    ids = set()
    for path in glob.glob(str(REPO / 'results/evidence-runs/collections/*.csv')):
        with open(path, newline='', encoding='utf-8') as src:
            ids.update(row['result_id'] for row in csv.DictReader(src))
    return ids


def test_recorrido_particiona_los_resultados():
    """Total y disyunta: ninguno invisible, ninguno contado dos veces."""
    data = _recorrido()
    asignados = [r for paso in data['pasos'] for r in paso['resultados']]
    asignados += data['respaldo_instrumental']['resultados']
    assert len(asignados) == len(set(asignados)), 'un result_id en dos pasos'
    assert set(asignados) == _resultados_del_registro()


def test_titulos_cubren_los_resultados():
    data = yaml.safe_load((VISTA / 'titulos.yaml').read_text(encoding='utf-8'))
    filas = {row['result_id']: row for row in data['resultados']}
    assert set(filas) == _resultados_del_registro()
    sin_titulo = [k for k, v in filas.items() if not v.get('titulo')]
    assert not sin_titulo, f'resultados sin titulo redactado: {sin_titulo}'
    sin_reclamo = [k for k, v in filas.items() if not v.get('reclamo')]
    assert not sin_reclamo, f'resultados sin reclamo: {sin_reclamo}'


@pytest.mark.parametrize('paso', _recorrido()['pasos'], ids=lambda p: str(p['n']))
def test_cada_paso_declara_su_cifra_de_una_sola_forma(paso):
    """Leída o citada, nunca las dos ni ninguna."""
    citada = 'cifra' in paso
    leida = 'leer' in paso
    assert citada != leida, f"paso {paso['n']}: cifra y leer son excluyentes"
    if citada:
        assert paso.get('fuente'), f"paso {paso['n']}: una cifra citada necesita fuente"


@pytest.mark.parametrize('paso', [p for p in _recorrido()['pasos'] if 'cifra' in p],
                         ids=lambda p: str(p['n']))
def test_cifra_citada_aparece_literal_en_su_fuente(paso):
    """El chequeo (b) de 96-verificar-indices.py, aplicado a la consola.

    Sin esto la consola es un lugar donde puede aparecer, frente al tribunal, un
    número que ningún verificador chequea.
    """
    fuente = REPO / paso['fuente']
    assert fuente.is_file(), f"fuente inexistente: {paso['fuente']}"
    assert paso['cifra'] in fuente.read_text(encoding='utf-8'), (
        f"la cifra {paso['cifra']!r} del paso {paso['n']} no aparece en {paso['fuente']}")
```

- [ ] **Step 4: Correr los tests**

Run: `cd webconsole/backend && python -m pytest tests/test_evidence_clases.py -q`
Expected: PASS. Si `test_recorrido_particiona_los_resultados` falla, el mensaje nombra
exactamente qué `result_id` sobra o falta — corregir `recorrido.yaml`, nunca el test.

- [ ] **Step 5: Commit — SÓLO si el usuario lo pidió**

```bash
git add results/evidence-vista/recorrido.yaml results/evidence-vista/titulos.yaml \
        webconsole/backend/tests/test_evidence_clases.py
git commit -m "feat(webconsole): capa editorial del recorrido y los 35 títulos"
```

---

## Task 3: Adaptadores de `metrics.json`

**Files:**
- Create: `webconsole/backend/src/eovrt_webconsole/evidence_metrics.py`
- Test: `webconsole/backend/tests/test_evidence_metrics.py`

**Interfaces:**
- Produces:
  - `Cabecera = TypedDict("Cabecera", {"label": str, "valor": float | None, "texto": str})`
  - `leer_metricas(path: Path) -> dict | None` — `None` si no hay archivo o la forma es desconocida.
  - La forma devuelta: `{"esquema": str, "cabecera": list[dict], "desgloses": list[dict]}`, donde cada desglose es `{"id": str, "titulo": str, "nota": str | None, "columnas": list[str], "filas": list[dict]}`.
  - `campo_de(path: Path, campo: str) -> float | None` — para las cifras `leer:` del recorrido.

- [ ] **Step 1: Escribir el test que falla**

Crear `webconsole/backend/tests/test_evidence_metrics.py`:

```python
"""Los metrics.json NO comparten forma: un adaptador por esquema, y lo desconocido degrada."""
import json
from pathlib import Path

import pytest

from eovrt_webconsole.evidence_metrics import campo_de, leer_metricas

REPO = Path(__file__).resolve().parents[3]
CAMPANAS = sorted(p.parent for p in (REPO / 'results').glob('*/*/metrics.json'))


def test_hay_17_campanas_con_artefacto():
    """Si aparece una campaña nueva, este test lo dice antes que la pantalla."""
    assert len(CAMPANAS) == 17


@pytest.mark.parametrize('directorio', CAMPANAS, ids=lambda p: p.name)
def test_toda_campana_despacha_a_un_adaptador(directorio):
    datos = leer_metricas(directorio / 'metrics.json')
    assert datos is not None, f'esquema no reconocido en {directorio.name}'
    assert datos['cabecera'], 'un adaptador sin cabecera no sirve de nada'


def test_clip_campaign_lee_cabecera_y_desgloses():
    datos = leer_metricas(
        REPO / 'results/clip_bench/t1_gdinotiny560_v2short_scene/metrics.json')
    assert datos['esquema'] == 'clip_campaign_metrics.v1'
    cabecera = {c['label']: c['valor'] for c in datos['cabecera']}
    assert cabecera['F1 micro'] == pytest.approx(0.788732, abs=1e-6)
    ids = [d['id'] for d in datos['desgloses']]
    assert ids == ['condicion', 'escenario', 'clip', 'negativos']


def test_escenario_sin_episodios_evaluables_no_vale_cero():
    """P3 y P5 se declaran, no se cuentan como recall 0 (ADR-006/013)."""
    datos = leer_metricas(
        REPO / 'results/clip_bench/t1_gdinotiny560_v2short_scene/metrics.json')
    escenarios = next(d for d in datos['desgloses'] if d['id'] == 'escenario')
    p3 = next(f for f in escenarios['filas'] if f['nombre'] == 'P3')
    assert p3['recall'] is None
    assert p3['no_aplica'] == 'sin episodios evaluables'


def test_esquema_desconocido_degrada_a_none(tmp_path):
    path = tmp_path / 'metrics.json'
    path.write_text(json.dumps({'schema_version': 'inventado.v9', 'x': 1}))
    assert leer_metricas(path) is None


def test_campo_de_lee_una_metrica_puntual():
    valor = campo_de(
        REPO / 'results/clip_bench/g1_gdinotiny560_v2short_subject/metrics.json',
        'f1_micro')
    assert valor == pytest.approx(0.929577, abs=1e-6)
```

- [ ] **Step 2: Correr para verificar que falla**

Run: `cd webconsole/backend && python -m pytest tests/test_evidence_metrics.py -q`
Expected: FAIL con `ModuleNotFoundError: No module named 'eovrt_webconsole.evidence_metrics'`.

- [ ] **Step 3: Implementar `evidence_metrics.py`**

```python
"""Adaptadores de metrics.json. Los cuatro esquemas NO comparten forma.

El despacho es por `schema_version` cuando está; si no, por sonda de forma. Una
forma desconocida devuelve None: la pantalla muestra el resultado sin cabecera
leída antes que adivinar una métrica.
"""
from __future__ import annotations

import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


def _cargar(path: Path) -> dict | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        logger.warning("metrics.json ilegible en %s: %s", path, exc)
        return None


def campo_de(path: Path, campo: str) -> float | None:
    """Una métrica puntual, para las cifras `leer:` del recorrido."""
    data = _cargar(path)
    if not isinstance(data, dict):
        return None
    for contenedor in (data.get("positives"), data):
        if isinstance(contenedor, dict) and isinstance(contenedor.get(campo), (int, float)):
            return float(contenedor[campo])
    return None


def _clip_campaign(data: dict) -> dict:
    pos, neg = data.get("positives", {}), data.get("negatives", {})
    cabecera = [
        {"label": "F1 micro", "valor": pos.get("f1_micro")},
        {"label": "recall micro", "valor": pos.get("recall_micro")},
        {"label": "precision micro", "valor": pos.get("precision_micro")},
        {"label": "episodios evaluables", "valor": pos.get("episodes_evaluable"),
         "entero": True, "nota": f"de {pos.get('episodes_total')}"},
        {"label": "falsos positivos", "valor": pos.get("false_positives"), "entero": True},
    ]
    condicion = {
        "id": "condicion", "titulo": "Por condición de riesgo",
        "nota": "El t_alert está dominado por la persistencia del patrón, no por el transporte.",
        "columnas": ["Condición", "Episodios", "SDR", "t_alert"],
        "filas": [{"nombre": k, "episodios": v.get("episodes"), "sdr": v.get("sdr"),
                   "t_alert_ms": v.get("t_alert_system_ms"), "fp": v.get("false_positives"),
                   "no_aplica": None}
                  for k, v in sorted(data.get("by_condition", {}).items())],
    }
    escenario = {
        "id": "escenario", "titulo": "Por escenario",
        "nota": "Nunca sólo el agregado — limitación L5.",
        "columnas": ["Escenario", "Clips", "Episodios", "recall", "FP", "SDR"],
        "filas": [{"nombre": k, "clips": v.get("clips"),
                   "episodios": v.get("episodes_evaluable"), "recall": v.get("recall"),
                   "fp": v.get("false_positives"), "sdr": v.get("sdr"),
                   # Lo que no tiene dato se DECLARA, no se dibuja como cero.
                   "no_aplica": None if v.get("recall") is not None
                   else "sin episodios evaluables"}
                  for k, v in sorted(data.get("by_scenario", {}).items())],
    }
    clip = {
        "id": "clip", "titulo": "Por clip", "nota": None,
        "columnas": ["Clip", "Escenario", "Esperados", "Detectados", "recall", "t_alert"],
        "filas": [{"nombre": c.get("clip_id"), "escenario": c.get("scenario"),
                   "esperados": c.get("expected"), "detectados": c.get("matched"),
                   "recall": c.get("recall"), "t_alert_ms": c.get("t_alert_system_ms"),
                   "no_aplica": None if c.get("applicability") == "computed"
                   else c.get("applicability_cause")}
                  for c in data.get("by_clip", [])],
    }
    negativos = {
        "id": "negativos", "titulo": "Control de negativos",
        "nota": "Los negativos no entran a precision, recall ni F1: su métrica son los FP.",
        "columnas": ["Clips", "FP", "Tiempo observado"],
        "filas": [{"nombre": "negativos", "clips": neg.get("clips"),
                   "fp": neg.get("false_positives"),
                   "observado_ms": neg.get("observed_ms"), "no_aplica": None}],
    }
    return {"esquema": "clip_campaign_metrics.v1", "cabecera": cabecera,
            "desgloses": [condicion, escenario, clip, negativos]}


def _clip_person_state(data: dict) -> dict:
    agregado = data.get("agregado", {})
    cabecera = [{"label": f"{cond} F1", "valor": v.get("f1")}
                for cond, v in sorted(agregado.items())]
    return {
        "esquema": "clip_person_state.v1", "cabecera": cabecera,
        "desgloses": [{
            "id": "clip", "titulo": "Por clip",
            "nota": "person-frames con atributo unknown excluidas del denominador.",
            "columnas": ["Clip", "Condición", "F1"],
            "filas": [{"nombre": str(c.get("clip_id")), "f1": c.get("f1"),
                       "no_aplica": None} for c in data.get("por_clip", [])],
        }],
    }


def _nivel_a_gate(data: dict) -> dict:
    gate = data.get("gate", {})
    return {
        "esquema": "nivel_a_gate", "cabecera": [
            {"label": k, "valor": v.get("delta"), "nota": "delta"} for k, v in sorted(gate.items())
        ],
        "desgloses": [{
            "id": "estrato", "titulo": "Por estrato",
            "nota": "Comparación pre-registrada entre formulaciones.",
            "columnas": ["Estrato / condición", "Complementariedad"],
            "filas": [{"nombre": k, "valores": v, "no_aplica": None}
                      for k, v in sorted(data.get("complementarity", {}).items())],
        }],
    }


def leer_metricas(path: Path) -> dict | None:
    data = _cargar(path)
    if not isinstance(data, dict):
        return None
    esquema = data.get("schema_version")
    if esquema == "clip_campaign_metrics.v1":
        return _clip_campaign(data)
    if esquema == "clip_person_state.v1":
        return _clip_person_state(data)
    # Sonda de forma: bench_nivel_a/d1 no declara schema_version. No adivinamos
    # por nombre de archivo: exigimos las dos claves que sólo tiene ese esquema.
    if esquema is None and "gate" in data and "complementarity" in data:
        return _nivel_a_gate(data)
    if esquema is None and "fases" in data:
        return {"esquema": "t_alert_notification", "cabecera": [
            {"label": "p95", "valor": data.get("p95_ms"), "nota": "ms"},
        ], "desgloses": [{
            "id": "fase", "titulo": "Por fase", "nota": None,
            "columnas": ["Fase", "n", "p95"],
            "filas": [{"nombre": k, "valores": v, "no_aplica": None}
                      for k, v in sorted(data.get("fases", {}).items())],
        }]}
    logger.warning("esquema de métricas no reconocido en %s: %r", path, esquema)
    return None
```

- [ ] **Step 4: Correr los tests**

Run: `cd webconsole/backend && python -m pytest tests/test_evidence_metrics.py -q`
Expected: PASS.

**Si `test_toda_campana_despacha_a_un_adaptador` falla para
`realtime/t_alert_notification`**, es porque la sonda `"fases" in data` no coincide con su
forma real. Abrir `results/realtime/t_alert_notification/metrics.json`, leer sus claves de
primer nivel, y ajustar **la sonda y el adaptador** a la forma real — nunca relajar el test
a `is not None or True`.

- [ ] **Step 5: Commit — SÓLO si el usuario lo pidió**

```bash
git add webconsole/backend/src/eovrt_webconsole/evidence_metrics.py \
        webconsole/backend/tests/test_evidence_metrics.py
git commit -m "feat(webconsole): adaptadores de metrics.json por esquema"
```

---

## Task 4: La API del recorrido

**Files:**
- Modify: `webconsole/backend/src/eovrt_webconsole/evidence_archive.py`
- Modify: `webconsole/backend/src/eovrt_webconsole/routers/evidencia.py`
- Test: `webconsole/backend/tests/test_evidence_archive.py`

**Interfaces:**
- Consumes: `leer_metricas` y `campo_de` de Task 3; `recorrido.yaml` y `titulos.yaml` de Task 2; `EvidenceRegistry.clase_de` de Task 1.
- Produces:
  - `GET /api/evidencia` → `{available, message, pasos: [...], respaldo: {...}, indices: [...]}`
  - `GET /api/evidencia/paso?n=3` → `{available, message, paso: {...}, resultados: [...]}`
  - `GET /api/evidencia/resultado?id=…` → lo que ya devolvía **más** `metricas` (la salida de `leer_metricas`) y `reclamo`.
  - `EvidenceArchive.recorrido() -> dict`, `EvidenceArchive.paso(n: int) -> dict`

- [ ] **Step 1: Escribir el test que falla**

Agregar a `webconsole/backend/tests/test_evidence_archive.py` (usa el fixture
`archive_client` que ya existe en ese archivo):

```python
def test_index_devuelve_el_recorrido_no_las_colecciones(archive_client):
    client, _ = archive_client
    data = client.get('/api/evidencia').json()
    assert [p['n'] for p in data['pasos']] == [1, 2, 3, 4]
    assert data['pasos'][0]['titulo']
    assert data['respaldo']['resultados'] is not None
    # Los cuatro índices por material siguen alcanzables, como acceso secundario.
    assert data['indices']


def test_paso_lista_sus_resultados_con_titulo_y_reclamo(archive_client):
    client, _ = archive_client
    data = client.get('/api/evidencia/paso?n=3').json()
    assert data['paso']['n'] == 3
    for fila in data['resultados']:
        assert fila['titulo'], 'un resultado sin título redactado llegó a la API'
        assert 'reclamo' in fila


def test_paso_inexistente_es_404(archive_client):
    client, _ = archive_client
    assert client.get('/api/evidencia/paso?n=9').status_code == 404


def test_resultado_trae_el_desglose(archive_client):
    client, _ = archive_client
    data = client.get('/api/evidencia/resultado?id=clip_bench/campaign').json()
    # La fixture no tiene metrics.json: la clave existe y vale None, y la
    # pantalla tiene que renderizar igual. Es el mismo contrato que en disco.
    assert 'metricas' in data['result']
    assert data['result']['metricas'] is None


def test_cifra_del_paso_leida_marca_su_origen(archive_client):
    client, _ = archive_client
    data = client.get('/api/evidencia').json()
    for paso in data['pasos']:
        assert paso['cifra_origen'] in {'leida', 'citada'}
        if paso['cifra_origen'] == 'citada':
            assert paso['fuente']
```

- [ ] **Step 2: Correr para verificar que falla**

Run: `cd webconsole/backend && python -m pytest tests/test_evidence_archive.py -q`
Expected: FAIL — `KeyError: 'pasos'`.

- [ ] **Step 3: Implementar en `evidence_archive.py`**

En `__init__`, después del bloque que carga `titulos.yaml`, reemplazar la carga de títulos
por una que traiga también el reclamo, y sumar el recorrido:

```python
        self.titles: dict[str, str | None] = {}
        self.reclamos: dict[str, str | None] = {}
        titles_path = registry.config_dir / "titulos.yaml"
        if titles_path.is_file():
            for row in (yaml.safe_load(titles_path.read_text()) or {}).get("resultados", []):
                self.titles[row["result_id"]] = row.get("titulo")
                self.reclamos[row["result_id"]] = row.get("reclamo")
        self.recorrido_cfg: dict = {}
        recorrido_path = registry.config_dir / "recorrido.yaml"
        if recorrido_path.is_file():
            self.recorrido_cfg = yaml.safe_load(recorrido_path.read_text()) or {}
```

Agregar los métodos:

```python
    def _cifra(self, paso: dict) -> dict:
        """Leída del metrics.json, o citada con su fuente. Nunca otra cosa."""
        if paso.get("leer"):
            valores = [campo_de(self.root / f"results/{item['result_id']}/metrics.json",
                                item["campo"]) for item in paso["leer"]]
            texto = " → ".join(f"{v:.3f}".replace(".", ",") if v is not None else "—"
                               for v in valores)
            return {"cifra": texto, "cifra_origen": "leida", "fuente": None}
        return {"cifra": paso.get("cifra"), "cifra_origen": "citada",
                "fuente": paso.get("fuente")}

    def recorrido(self) -> dict:
        state = self.availability()
        if not state["available"]:
            return {**state, "pasos": [], "respaldo": None, "indices": []}
        pasos = [{
            "n": paso["n"], "titulo": paso["titulo"], "claim": paso["claim"],
            "cifra_label": paso.get("cifra_label"), "cifra_nota": paso.get("cifra_nota"),
            "n_resultados": len(paso["resultados"]),
            "indices": sorted({r.split("/", 1)[0] for r in paso["resultados"]}),
            **self._cifra(paso),
        } for paso in self.recorrido_cfg.get("pasos", [])]
        respaldo = self.recorrido_cfg.get("respaldo_instrumental", {})
        indices: dict[str, int] = defaultdict(int)
        for result_id in self.by_result:
            indices[result_id.split("/", 1)[0]] += 1
        return {**state, "pasos": pasos, "respaldo": {
            "titulo": respaldo.get("titulo"), "claim": respaldo.get("claim"),
            "n_resultados": len(respaldo.get("resultados", [])),
        }, "indices": [{"id": k, "n_results": v} for k, v in sorted(indices.items())]}

    def paso(self, n: int) -> dict:
        state = self.availability()
        paso = next((p for p in self.recorrido_cfg.get("pasos", []) if p["n"] == n), None)
        if paso is None:
            raise KeyError(n)
        if not state["available"]:
            return {**state, "paso": None, "resultados": []}
        return {**state, "paso": {
            "n": paso["n"], "titulo": paso["titulo"], "claim": paso["claim"],
            "cifra_label": paso.get("cifra_label"), "cifra_nota": paso.get("cifra_nota"),
            **self._cifra(paso),
        }, "resultados": [self.result_info(r) for r in paso["resultados"]
                          if r in self.by_result]}
```

En `result_info`, sumar el reclamo y las métricas leídas:

```python
            "reclamo": self.reclamos.get(result_id) or None,
            "metricas": leer_metricas(self.root / f"results/{result_id}/metrics.json"),
```

Imports nuevos al tope del archivo:

```python
from eovrt_webconsole.evidence_metrics import campo_de, leer_metricas
```

- [ ] **Step 4: Implementar las rutas en `routers/evidencia.py`**

Reemplazar `index` y agregar `paso`:

```python
@router.get("")
def index(request: Request) -> dict:
    return request.app.state.evidence_archive.recorrido()


@router.get("/paso")
def paso(request: Request, n: Annotated[int, Query(ge=1)]) -> dict:
    try:
        return request.app.state.evidence_archive.paso(n)
    except KeyError as exc:
        raise HTTPException(404, "Ese paso del recorrido no existe") from exc
```

- [ ] **Step 5: Correr los tests**

Run: `cd webconsole/backend && python -m pytest tests/test_evidence_archive.py tests/test_evidence.py -q`
Expected: PASS. Los tests viejos que asumían `collections` en `/api/evidencia` van a fallar:
**actualizarlos a la forma nueva**, no restaurar la vieja.

- [ ] **Step 6: Suite completa del backend**

Run: `cd webconsole/backend && python -m pytest -q`
Expected: cero fallas.

- [ ] **Step 7: Commit — SÓLO si el usuario lo pidió**

```bash
git add webconsole/backend/src/eovrt_webconsole/evidence_archive.py \
        webconsole/backend/src/eovrt_webconsole/routers/evidencia.py \
        webconsole/backend/tests/
git commit -m "feat(webconsole): API del recorrido de evidencia"
```

---

## Task 5: La entrada y el paso (frontend)

**Files:**
- Create: `webconsole/frontend/src/pages/evidencia/Entrada.tsx`, `webconsole/frontend/src/pages/evidencia/Paso.tsx`
- Modify: `webconsole/frontend/src/pages/EvidencePage.tsx`, `types.ts`, `api/endpoints.ts`, `App.tsx`, `styles/ui.css`
- Test: `webconsole/frontend/src/__tests__/EvidencePage.test.tsx`

**Interfaces:**
- Consumes: `GET /api/evidencia` y `GET /api/evidencia/paso?n=` de Task 4.
- Produces:
  - `types.ts`: `EvidenceStep`, `EvidenceRecorrido`, `EvidenceStepPage`
  - `endpoints.ts`: `getEvidenceRecorrido()`, `getEvidenceStep(n: number)`
  - Ruta `/evidencia/paso?n=3`

- [ ] **Step 1: Escribir el test que falla**

Agregar a `webconsole/frontend/src/__tests__/EvidencePage.test.tsx` (extender el `fetch`
stub del `beforeEach` con las dos rutas nuevas, siguiendo el patrón que ya usa):

```tsx
it('la entrada muestra los cuatro números del argumento, no las colecciones', async () => {
  render(<MemoryRouter initialEntries={['/evidencia']}><App /></MemoryRouter>)
  expect(await screen.findByText('Qué agrega la plataforma sobre la detección cruda')).toBeTruthy()
  expect(screen.getByText('0,789 → 0,930')).toBeTruthy()
  // El conteo de corridas NO es la cifra de cabecera de la entrada.
  expect(screen.queryByText(/relaciones registradas/)).toBeNull()
})

it('una cifra citada se marca y dice su fuente', async () => {
  render(<MemoryRouter initialEntries={['/evidencia']}><App /></MemoryRouter>)
  const citada = await screen.findByTitle('results/bench_imagenes/index.md')
  expect(citada.textContent).toContain('0,551')
})

it('clickear un número abre sus resultados con título redactado', async () => {
  render(<MemoryRouter initialEntries={['/evidencia/paso?n=3']}><App /></MemoryRouter>)
  expect(await screen.findByText('Línea de base del Nivel B')).toBeTruthy()
  expect(screen.getByText(/toda campaña posterior se compara contra ésta/i)).toBeTruthy()
})
```

- [ ] **Step 2: Correr para verificar que falla**

Run: `cd webconsole/frontend && npm test -- EvidencePage`
Expected: FAIL — los textos no existen.

- [ ] **Step 3: Agregar los tipos**

En `webconsole/frontend/src/types.ts`, junto a `EvidenceResult`:

```ts
export interface EvidenceStep {
  n: number
  titulo: string
  claim: string
  cifra: string | null
  cifra_label: string | null
  cifra_nota: string | null
  cifra_origen: 'leida' | 'citada'
  fuente: string | null
  n_resultados: number
  indices: string[]
}
export interface EvidenceRecorrido extends ArchiveState {
  pasos: EvidenceStep[]
  respaldo: { titulo: string; claim: string; n_resultados: number } | null
  indices: Array<{ id: string; n_results: number }>
}
export interface EvidenceStepPage extends ArchiveState {
  paso: EvidenceStep | null
  resultados: EvidenceResult[]
}
```

Y extender `EvidenceResult` con los dos campos nuevos:

```ts
  reclamo: string | null
  metricas: EvidenceMetrics | null
```

```ts
export interface EvidenceMetricRow {
  nombre: string
  no_aplica: string | null
  [campo: string]: unknown
}
export interface EvidenceMetrics {
  esquema: string
  cabecera: Array<{ label: string; valor: number | null; nota?: string; entero?: boolean }>
  desgloses: Array<{
    id: string; titulo: string; nota: string | null
    columnas: string[]; filas: EvidenceMetricRow[]
  }>
}
```

- [ ] **Step 4: Agregar el cliente**

En `webconsole/frontend/src/api/endpoints.ts`, reemplazar `getEvidenceIndex`:

```ts
export const getEvidenceRecorrido = () => request<EvidenceRecorrido>('/api/evidencia')
export const getEvidenceStep = (n: number) =>
  request<EvidenceStepPage>(`/api/evidencia/paso?${new URLSearchParams({ n: String(n) })}`)
```

- [ ] **Step 5: Escribir `Entrada.tsx`**

El markup exacto está en el artboard `Main.dc.html` del canvas de diseño
(https://claude.ai/code/artifact/28eb5e84-c842-4d97-9df3-ee8c29fa66f2). Portarlo a JSX
usando los componentes de `components/ui` y clases nuevas en `ui.css`:

```tsx
import { Link } from 'react-router-dom'
import { useQuery } from '@tanstack/react-query'
import { getEvidenceRecorrido } from '../../api'
import { EmptyState, ErrorBanner, PageHeader } from '../../components/ui'

export default function Entrada() {
  const q = useQuery({ queryKey: ['evidencia', 'recorrido'], queryFn: getEvidenceRecorrido })
  if (q.isPending) return <EmptyState>Leyendo archivo de evidencia…</EmptyState>
  if (q.error) return <ErrorBanner>No se pudo leer el archivo de evidencia.</ErrorBanner>
  if (q.data.available === false) return <>
    <PageHeader title="Evidencia" />
    <EmptyState hint={q.data.message}>Archivo de evidencia no disponible</EmptyState>
  </>
  const total = q.data.pasos.reduce((n, p) => n + p.n_resultados, 0)
  return <div className="eo-evidence">
    <PageHeader title="Evidencia" meta={`${total} resultados reportados · lectura del archivo curado`} />
    <p className="eo-note">El recorrido del argumento del informe. Cada número abre los
      resultados que lo sostienen; cada resultado, su desglose y las corridas que lo respaldan.</p>
    <div className="eo-steps">
      {q.data.pasos.map((paso) => (
        <Link key={paso.n} className="eo-step" to={`/evidencia/paso?n=${paso.n}`}>
          <div className="eo-step__n">{paso.n}</div>
          <div>
            <div className="eo-step__t">{paso.titulo}</div>
            <p className="eo-step__c">{paso.claim}</p>
            <div className="eo-step__m">{paso.n_resultados} resultados · {paso.indices.join(' + ')}/</div>
          </div>
          <div className="eo-fig">
            <div className="eo-fig__l">{paso.cifra_label}</div>
            <div
              className={paso.cifra_origen === 'citada' ? 'eo-fig__v eo-cifra--cit' : 'eo-fig__v'}
              title={paso.fuente ?? undefined}
            >{paso.cifra}</div>
            <div className="eo-fig__u">{paso.cifra_nota}</div>
          </div>
        </Link>
      ))}
    </div>

    <div className="eo-side3">
      <Link className="eo-mini" to="/evidencia/respaldo">
        <div className="eo-mini__h">{q.data.respaldo?.titulo}</div>
        <p className="eo-mini__d">{q.data.respaldo?.claim}</p>
        <div className="eo-mini__n">{q.data.respaldo?.n_resultados} mediciones</div>
      </Link>
      <Link className="eo-mini" to="/evidencia/material">
        <div className="eo-mini__h">Por material</div>
        <p className="eo-mini__d">La organización canónica de <b>results/</b>, que es la
          fuente de las cifras: imágenes, Nivel A por sujeto, banco de clips y tiempo real.</p>
        <div className="eo-mini__n">{q.data.indices.length} índices · {total} resultados</div>
      </Link>
      {/* Los tres ejes se ENLAZAN, no se reimplementan: ya son documentos escritos
          y duplicarlos crearía una segunda fuente de verdad. */}
      <a className="eo-mini" href="https://github.com/simonll4/e-ovrt_experimental-setup/tree/main/results/ejes"
         target="_blank" rel="noreferrer">
        <div className="eo-mini__h">Ejes de lectura</div>
        <p className="eo-mini__d">La misma evidencia cortada por otros ejes, sin agregar
          mediciones: offline contra vivo, el día de rodaje, y zero-shot contra la jornada de ajuste.</p>
        <div className="eo-mini__n">3 vistas · results/ejes/</div>
      </a>
    </div>

    <p className="eo-cap">Las cifras se leen del <b>metrics.json</b> de cada campaña al
      abrirla; las que no tienen artefacto en este repositorio se muestran citadas, con la
      fuente al lado. Nada de esto consulta a los servicios.</p>
  </div>
}
```

- [ ] **Step 6: Escribir `Paso.tsx`**

Abrir `docs/rediseno-consola/mockups-evidencia/Paso.dc.html` y copiar de ahí la anatomía.
La tarjeta «El hallazgo del paso» sale de `paso.cifra` / `cifra_label` / `cifra_nota`; la
tabla, de `resultados`:

```tsx
import { Link, useSearchParams } from 'react-router-dom'
import { useQuery } from '@tanstack/react-query'
import { getEvidenceStep } from '../../api'
import { Card, EmptyState, ErrorBanner, PageHeader, Table } from '../../components/ui'

const fmt = (v: number | null | undefined, dec = 3) =>
  typeof v === 'number' ? v.toFixed(dec).replace('.', ',') : '—'

export default function Paso() {
  const [params] = useSearchParams()
  const n = Number(params.get('n') ?? '1')
  const q = useQuery({ queryKey: ['evidencia', 'paso', n], queryFn: () => getEvidenceStep(n) })
  if (q.isPending) return <EmptyState>Leyendo archivo de evidencia…</EmptyState>
  if (q.error) return <ErrorBanner>Ese paso del recorrido no existe.</ErrorBanner>
  const paso = q.data.paso
  if (!paso) return <EmptyState hint={q.data.message}>Archivo de evidencia no disponible</EmptyState>
  return <div className="eo-evidence">
    <PageHeader title={paso.titulo} meta={`paso ${paso.n} de 4 · ${q.data.resultados.length} resultados`} />
    <p className="eo-note">{paso.claim}</p>
    <Card title="El hallazgo del paso" meta={paso.cifra_nota ?? undefined}>
      <div className="eo-stats-row">
        <div className="eo-stat eo-stat--on">
          <span className="eo-stat__label">{paso.cifra_label}</span>
          <span className={paso.cifra_origen === 'citada' ? 'eo-stat__value eo-cifra--cit' : 'eo-stat__value'}
                title={paso.fuente ?? undefined}>{paso.cifra}</span>
        </div>
      </div>
    </Card>
    <Card title="Los resultados de este paso" flush>
      <Table aria-label={`Resultados del paso ${paso.n}`}>
        <thead><tr>
          <th>Resultado</th><th>Cifra de cabecera</th><th>Combinación declarada</th>
          <th className="eo-num">Respaldo</th>
        </tr></thead>
        <tbody>
          {q.data.resultados.map((r) => (
            <tr key={r.result_id}>
              <td>
                <div className="eo-rowname">
                  <Link to={`/evidencia/resultado?id=${encodeURIComponent(r.result_id)}`}>
                    <b>{r.titulo || r.etiqueta}</b>
                  </Link>
                  <span className="eo-mono">{r.result_id}</span>
                </div>
              </td>
              <td className="eo-cifra">
                {r.metricas?.cabecera[0]
                  ? <><i>{r.metricas.cabecera[0].label}</i>{fmt(r.metricas.cabecera[0].valor)}</>
                  : <span className="eo-na">sin artefacto en este repositorio</span>}
              </td>
              <td className="eo-comb">{r.reclamo}</td>
              <td className="eo-num eo-mono">{r.n_runs} corridas</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </Card>
  </div>
}
```

Agregar las rutas `/evidencia/respaldo` y `/evidencia/material` a `App.tsx` junto con
`/evidencia/paso`; ambas reusan `Paso.tsx` leyendo `respaldo_instrumental` y los índices
por material respectivamente.

- [ ] **Step 7: Reconectar `EvidencePage.tsx` y `App.tsx`**

`EvidencePage.tsx` pasa a despachar por `pathname` entre `Entrada`, `Paso`, `Resultado`
(Task 6) y el nivel de corrida que ya existe. En `App.tsx` agregar:

```tsx
<Route path="/evidencia/paso" element={<EvidencePage />} />
```

- [ ] **Step 8: Agregar los estilos a `ui.css`**

Portar los bloques `.eo-steps`, `.eo-step`, `.eo-fig`, `.eo-side3`, `.eo-mini` y
`.eo-cifra--cit` del artboard, **usando las variables de `tokens.css`**, no los hex
literales del mockup (el mockup los inlineó porque un artboard no puede importar el
stylesheet real).

- [ ] **Step 9: Correr los tests del frontend**

Run: `cd webconsole/frontend && npm test -- EvidencePage`
Expected: PASS.

- [ ] **Step 10: El gate del contrato**

Run: `cd webconsole/frontend && npm test -- contrato`
Expected: **10/10**, sin haber tocado ningún archivo de `__tests__/contrato/`.

- [ ] **Step 11: Commit — SÓLO si el usuario lo pidió**

```bash
git add webconsole/frontend/src
git commit -m "feat(webconsole): entrada del recorrido y pantalla de paso"
```

---

## Task 6: El resultado con su desglose

**Files:**
- Create: `webconsole/frontend/src/pages/evidencia/Resultado.tsx`, `webconsole/frontend/src/pages/evidencia/Desglose.tsx`
- Modify: `webconsole/frontend/src/styles/ui.css`
- Test: `webconsole/frontend/src/__tests__/EvidenceView.test.tsx`

**Interfaces:**
- Consumes: `EvidenceMetrics` de Task 5; `GET /api/evidencia/resultado` de Task 4.
- Produces: `<Desglose desglose={d} />`, reutilizable por los cuatro desgloses.

- [ ] **Step 1: Escribir el test que falla**

En `webconsole/frontend/src/__tests__/EvidenceView.test.tsx`:

```tsx
it('muestra el agregado Y el desglose, nunca sólo el agregado', async () => {
  render(<MemoryRouter initialEntries={['/evidencia/resultado?id=clip_bench/campaign']}>
    <App /></MemoryRouter>)
  expect(await screen.findByText('0,789')).toBeTruthy()       // agregado
  expect(screen.getByText('Por escenario')).toBeTruthy()      // desglose (L5)
  expect(screen.getByText('Por condición de riesgo')).toBeTruthy()
})

it('un escenario sin episodios evaluables se declara, no se dibuja como cero', async () => {
  render(<MemoryRouter initialEntries={['/evidencia/resultado?id=clip_bench/campaign']}>
    <App /></MemoryRouter>)
  const fila = await screen.findByRole('row', { name: /P3/ })
  expect(within(fila).getByText('sin episodios evaluables')).toBeTruthy()
  expect(within(fila).queryByText('0,000')).toBeNull()
  // Y no hay barra: lo que no tiene dato no se dibuja. `within()` devuelve
  // consultas, no un contenedor — se consulta el elemento de la fila directo.
  expect(fila.querySelector('.eo-bar')).toBeNull()
})

it('agrupa el motivo repetido de las corridas en vez de repetirlo por fila', async () => {
  render(<MemoryRouter initialEntries={['/evidencia/resultado?id=clip_bench/campaign']}>
    <App /></MemoryRouter>)
  const motivo = await screen.findAllByText(/vivían en un scratchpad ausente/)
  expect(motivo).toHaveLength(1)
})
```

- [ ] **Step 2: Correr para verificar que falla**

Run: `cd webconsole/frontend && npm test -- EvidenceView`
Expected: FAIL.

- [ ] **Step 3: Escribir `Desglose.tsx`**

```tsx
import { Card, Table } from '../../components/ui'
import type { EvidenceMetrics } from '../../types'

const fmt = (v: unknown, dec = 3) =>
  typeof v === 'number' ? v.toFixed(dec).replace('.', ',') : '—'

/** Barra de UNA sola tinta: esto es magnitud, no identidad. El valor va en tinta
 *  de texto; el color vive en la marca. Lo que no tiene dato no se dibuja. */
function Barra({ valor }: { valor: number | null }) {
  if (valor == null) return null
  return <span className="eo-track">
    <i className="eo-bar" style={{ width: `${Math.max(0, Math.min(1, valor)) * 100}%` }} />
  </span>
}

export default function Desglose({ desglose }: { desglose: EvidenceMetrics['desgloses'][number] }) {
  return <Card title={desglose.titulo} flush>
    <Table aria-label={desglose.titulo}>
      <thead><tr>{desglose.columnas.map((c) => <th key={c}>{c}</th>)}</tr></thead>
      <tbody>
        {desglose.filas.map((fila) => (
          <tr key={fila.nombre}>
            <td className="eo-mono">{fila.nombre}</td>
            {fila.no_aplica
              ? <td colSpan={desglose.columnas.length - 1} className="eo-na">{fila.no_aplica}</td>
              : <>
                  <td className="eo-num">{String(fila.clips ?? fila.episodios ?? '—')}</td>
                  <td>
                    <div className="eo-barcell">
                      <span className="eo-barval">{fmt(fila.recall)}</span>
                      <Barra valor={typeof fila.recall === 'number' ? fila.recall : null} />
                    </div>
                  </td>
                  <td className="eo-num">{String(fila.fp ?? '—')}</td>
                  <td className="eo-num">{fmt(fila.sdr)}</td>
                </>}
          </tr>
        ))}
      </tbody>
    </Table>
    {desglose.nota && <p className="eo-cap">{desglose.nota}</p>}
  </Card>
}
```

- [ ] **Step 4: Escribir `Resultado.tsx`**

Portar el artboard `Resultado.dc.html`: `PageHeader` con título y badge de clase, el
reclamo, la fila de `StatTile` con `metricas.cabecera`, los desgloses en dos columnas, la
tarjeta de Procedencia, y la de **Corridas plegadas** — que agrupa las filas por `reason`
y muestra cada motivo **una sola vez** con su conteo, detrás de un `<details>`.

- [ ] **Step 5: Correr los tests**

Run: `cd webconsole/frontend && npm test -- EvidenceView`
Expected: PASS.

- [ ] **Step 6: El gate del contrato**

Run: `cd webconsole/frontend && npm test -- contrato`
Expected: 10/10.

- [ ] **Step 7: Commit — SÓLO si el usuario lo pidió**

```bash
git add webconsole/frontend/src
git commit -m "feat(webconsole): resultado con desglose por escenario y condición"
```

---

## Task 7: Corridas — clase y agrupación por resultado

**Files:**
- Modify: `webconsole/backend/src/eovrt_webconsole/routers/runs.py`
- Create: `webconsole/frontend/src/components/ClaseChips.tsx`
- Modify: `webconsole/frontend/src/pages/RunsPage.tsx`, `types.ts`, `api/endpoints.ts`
- Test: `webconsole/backend/tests/test_runs_clases.py`, `webconsole/frontend/src/__tests__/RunsClases.test.tsx`

**Interfaces:**
- Consumes: `EvidenceRegistry.clase_de` de Task 1; los títulos de Task 2.
- Produces:
  - `GET /api/runs?clase=resultado` y `GET /api/runs?result_id=clip_bench/t1_…`
  - `GET /api/runs/grupos` → `[{result_id, titulo, cifra, paso, clase, n_runs, last_run_at}]`
  - `<ClaseChips valor={clase} onChange={…} conteos={…} />`

**Por qué una ruta nueva acá sí:** `RunsPage` no está montada por el contrato congelado
(monta `RunDetailPage`, `ComposePage` y `ComparePage`). Verificarlo antes de agregarla:
`grep -rn "RunsPage" webconsole/frontend/src/__tests__/contrato/` debe no devolver nada.

- [ ] **Step 1: Escribir el test del backend**

Crear `webconsole/backend/tests/test_runs_clases.py`:

```python
def test_listado_filtra_por_clase(runs_client):
    client = runs_client
    todas = client.get('/api/runs?vista=todas&page_size=200').json()
    resultado = client.get('/api/runs?clase=resultado&page_size=200').json()
    assert len(resultado) < len(todas)
    assert all(r['evidence']['clase'] == 'resultado' for r in resultado)


def test_cada_corrida_trae_su_clase(runs_client):
    filas = runs_client.get('/api/runs?vista=todas&page_size=5').json()
    assert all('clase' in r['evidence'] for r in filas)


def test_grupos_colapsan_las_corridas_por_resultado(runs_client):
    grupos = runs_client.get('/api/runs/grupos').json()
    assert len(grupos) < 60, 'la gracia es colapsar cientos de filas en decenas'
    assert all({'result_id', 'titulo', 'clase', 'n_runs'} <= set(g) for g in grupos)


def test_corridas_fuera_del_registro_caen_en_un_grupo_propio(runs_client):
    grupos = runs_client.get('/api/runs/grupos').json()
    suelto = [g for g in grupos if g['clase'] == 'sin_clasificar']
    assert len(suelto) == 1
    assert suelto[0]['result_id'] is None
```

- [ ] **Step 2: Correr para verificar que falla**

Run: `cd webconsole/backend && python -m pytest tests/test_runs_clases.py -q`
Expected: FAIL — `clase` no existe en `evidence`.

- [ ] **Step 3: Implementar en `runs.py`**

En `EvidenceRegistry.describe` (en `evidence.py`) sumar la clase al dict que ya devuelve:

```python
            "clase": next((c for c in CLASES if c in {
                self.clase_de(run_id) for run_id in run_ids}), "sin_clasificar"),
```

En `list_runs`, después de la línea de `coincide_vista`:

```python
    if clase:
        base = [r for r in base if evidence[r["run_id"]]["clase"] == clase]
    if result_id:
        base = [r for r in base if result_id in evidence[r["run_id"]]["result_ids"]]
```

y sumar los dos parámetros a la firma:

```python
    clase: str | None = Query(default=None, description="resultado | instrumento | ensayo | plataforma | sin_clasificar"),
    result_id: str | None = Query(default=None),
```

Agregar la ruta de grupos:

```python
@router.get("/grupos")
async def list_grupos(request: Request, clase: str | None = None) -> list[dict]:
    """Las 472 corridas son ~32 grupos. El filtro de clase casi no baja el
    listado (412 de 472): lo que lo hace legible es la granularidad."""
    backend = request.app.state.backend
    registry = request.app.state.evidence
    archive = request.app.state.evidence_archive
    try:
        base = await backend.list_runs()
    except ServiceUnavailable as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc
    grupos: dict[str | None, dict] = {}
    for fila in base:
        descripcion = registry.describe([fila["run_id"]])
        claves = descripcion["result_ids"] or [None]
        for clave in claves:
            grupo = grupos.setdefault(clave, {
                "result_id": clave,
                "titulo": archive.titles.get(clave) if clave else "Fuera del registro de evidencia",
                "clase": descripcion["clase"],
                "n_runs": 0,
                "last_run_at": None,
            })
            grupo["n_runs"] += 1
            creado = fila.get("created_at")
            if creado and (grupo["last_run_at"] is None or creado > grupo["last_run_at"]):
                grupo["last_run_at"] = creado
    filas = list(grupos.values())
    if clase:
        filas = [g for g in filas if g["clase"] == clase]
    return sorted(filas, key=lambda g: (g["last_run_at"] or ""), reverse=True)
```

- [ ] **Step 4: Correr los tests del backend**

Run: `cd webconsole/backend && python -m pytest tests/test_runs_clases.py -q`
Expected: PASS.

- [ ] **Step 5: Escribir `ClaseChips.tsx`**

```tsx
import type { Clase } from '../types'

const ETIQUETA: Record<Clase, string> = {
  resultado: 'Resultado', instrumento: 'Instrumento', ensayo: 'Ensayo',
  plataforma: 'Prueba de plataforma', sin_clasificar: 'Fuera del registro',
}

/** La clase se lee por etiqueta y posición, NO por color: cinco tonos chocarían
 *  con los tonos de estado reservados, y el violeta acá es acción. */
export default function ClaseChips({ valor, onChange, conteos }: {
  valor: Clase | null
  onChange: (c: Clase | null) => void
  conteos: Partial<Record<Clase, number>>
}) {
  return <div className="eo-chips" role="group" aria-label="Filtrar por clase">
    {(Object.keys(ETIQUETA) as Clase[]).filter((c) => conteos[c]).map((c) => (
      <button key={c} type="button" aria-pressed={valor === c}
        className={valor === c ? 'eo-chip eo-chip--on' : 'eo-chip'}
        onClick={() => onChange(valor === c ? null : c)}>
        {ETIQUETA[c]} <b>{conteos[c]}</b>
      </button>
    ))}
  </div>
}
```

- [ ] **Step 6: Cablear `RunsPage.tsx`**

Reemplazar `<EvidenceViewControl>` por `<ClaseChips>`, agregar el toggle «Agrupar por
resultado» (default **encendido**), y cuando está encendido renderizar los grupos de
`/api/runs/grupos`; al expandir un grupo, pedir `/api/runs?result_id=<id>`.

- [ ] **Step 7: Escribir el test del frontend**

Crear `webconsole/frontend/src/__tests__/RunsClases.test.tsx`:

```tsx
import { beforeEach, expect, it, vi } from 'vitest'
import { MemoryRouter } from 'react-router-dom'
import { fireEvent, render, screen } from '../test-utils'
import App from '../App'

let urls: URL[]
beforeEach(() => {
  urls = []
  vi.stubGlobal('fetch', vi.fn(async (input: RequestInfo | URL) => {
    const url = new URL(String(input), 'http://localhost'); urls.push(url)
    if (url.pathname === '/api/runs/grupos') return new Response(JSON.stringify([
      { result_id: 'clip_bench/t1', titulo: 'Línea de base del Nivel B',
        clase: 'resultado', n_runs: 34, last_run_at: '2026-08-03T22:33:23Z' },
      { result_id: 'realtime/claqueta_reloj_externo', titulo: 'La claqueta con reloj externo',
        clase: 'instrumento', n_runs: 4, last_run_at: '2026-08-05T10:00:00Z' },
    ]))
    if (url.pathname === '/api/runs') return new Response(JSON.stringify([]))
    return new Response('{}')
  }))
})

it('arranca agrupada por resultado: pide los grupos, no las 472 filas', async () => {
  render(<MemoryRouter initialEntries={['/runs']}><App /></MemoryRouter>)
  expect(await screen.findByText('Línea de base del Nivel B')).toBeTruthy()
  expect(urls.some((u) => u.pathname === '/api/runs/grupos')).toBe(true)
})

it('el chip de clase filtra del lado del servidor', async () => {
  render(<MemoryRouter initialEntries={['/runs']}><App /></MemoryRouter>)
  fireEvent.click(await screen.findByRole('button', { name: /Instrumento/ }))
  await screen.findByText('La claqueta con reloj externo')
  expect(urls.some((u) => u.searchParams.get('clase') === 'instrumento')).toBe(true)
})

it('expandir un grupo pide sólo las corridas de ese resultado', async () => {
  render(<MemoryRouter initialEntries={['/runs']}><App /></MemoryRouter>)
  fireEvent.click(await screen.findByText('Línea de base del Nivel B'))
  await vi.waitFor(() => expect(
    urls.some((u) => u.searchParams.get('result_id') === 'clip_bench/t1')).toBe(true))
})
```

- [ ] **Step 8: Correr todo el frontend y el gate**

Run: `cd webconsole/frontend && npm test`
Expected: los 467+ que pasaban, más los nuevos. **Contrato 10/10.**

- [ ] **Step 9: Commit — SÓLO si el usuario lo pidió**

```bash
git add webconsole/backend/src webconsole/backend/tests webconsole/frontend/src
git commit -m "feat(webconsole): Corridas por clase y agrupadas por resultado"
```

---

## Task 8: Experimentos — clase y las pruebas de plataforma

**Files:**
- Modify: `webconsole/backend/src/eovrt_webconsole/routers/experiments.py`
- Modify: `webconsole/frontend/src/pages/ExperimentsPage.tsx`, `types.ts`, `api/endpoints.ts`
- Test: `webconsole/backend/tests/test_experiments_clases.py`, `webconsole/frontend/src/__tests__/ExperimentsEvidence.test.tsx`

**Interfaces:**
- Consumes: `EvidenceRegistry.clase_de` y las excepciones de `clasificacion.yaml` (Task 1).
- Produces:
  - `EvidenceRegistry.clase_de_slug(slug: str, default: str) -> str` — nuevo método en `evidence.py`: la excepción explícita del slug, o el `default` que pasa el llamador.
  - Campo **opcional** `evidence.clase` en cada fila de `/api/experiments/manifests`.
  - Cabecera `X-Platform-Test-Count: 445`
  - Cabecera `X-Platform-Test-Slugs: orq_1=90,orq_2a=90,orq_alerts_502=89,orq_alerts=89,gate_orq=87`

**⚠ La restricción que manda acá:** `ExperimentsPage` está montada por
`experimentos-distribucion.contrato.test.tsx`, y `soporte.tsx` **falla ante cualquier ruta
imprevista**. Por eso: **cero rutas nuevas** desde esta pantalla, los datos viajan en
cabeceras (el patrón que este endpoint ya usa con `X-Archived-Executions-Count`), y la
pantalla **tiene que renderizar bien cuando las cabeceras no están** — la fixture del
contrato no las manda.

- [ ] **Step 1: Escribir el test del backend**

Crear `webconsole/backend/tests/test_experiments_clases.py`:

```python
def test_manifiestos_traen_su_clase(manifests_client):
    filas = manifests_client.get('/api/experiments/manifests?vista=todas').json()
    assert all('clase' in f['evidence'] for f in filas)


def test_cabecera_cuenta_las_pruebas_de_plataforma(manifests_client):
    respuesta = manifests_client.get('/api/experiments/manifests?vista=todas')
    assert int(respuesta.headers['X-Platform-Test-Count']) > 0


def test_cabecera_desglosa_los_slugs(manifests_client):
    respuesta = manifests_client.get('/api/experiments/manifests?vista=todas')
    desglose = dict(
        par.split('=') for par in respuesta.headers['X-Platform-Test-Slugs'].split(','))
    assert all(v.isdigit() for v in desglose.values())


def test_la_respuesta_sigue_siendo_una_lista(manifests_client):
    """Cambiar la forma a objeto rompería el contrato congelado."""
    assert isinstance(manifests_client.get('/api/experiments/manifests').json(), list)
```

- [ ] **Step 2: Correr para verificar que falla**

Run: `cd webconsole/backend && python -m pytest tests/test_experiments_clases.py -q`
Expected: FAIL — `KeyError: 'X-Platform-Test-Count'`.

- [ ] **Step 3: Implementar en `experiments.py`**

Dentro de `list_manifests`, junto a las cabeceras que ya se setean:

```python
    # Las ejecuciones sin manifiesto son la máquina probándose: 5 slugs que
    # escribe la suite de tests. Viajan en cabeceras, NO en un endpoint nuevo,
    # porque esta pantalla está montada por el contrato congelado y su arnés
    # falla ante cualquier ruta imprevista.
    plataforma = Counter(
        e["slug"] for e in classification
        if registry.clase_de_slug(e["slug"], "") == "plataforma"
    )
    response.headers["X-Platform-Test-Count"] = str(sum(plataforma.values()))
    response.headers["X-Platform-Test-Slugs"] = ",".join(
        f"{slug}={n}" for slug, n in plataforma.most_common())
```

Requiere `from collections import Counter` al tope de `experiments.py` si todavía no está.

Y en `evidence.py`, el ayudante que resuelve la excepción por slug — con `default`
explícito, para no leer el diccionario privado desde el router:

```python
    def clase_de_slug(self, slug: str, default: str = "sin_clasificar") -> str:
        """La excepción explícita del slug, o lo que decida el llamador.

        Los slugs no tienen rol en el registro (no producen corridas de
        evidencia), así que su clase sale sólo de `clasificacion.yaml`.
        """
        return self._clase_forzada.get(slug, default)
```

En la construcción de `evidence` de cada fila, sumar:

```python
        evidence["clase"] = registry.clase_de_slug(
            manifest.slug, "resultado" if evidence["is_evidence"] else "ensayo")
```

- [ ] **Step 4: Correr los tests del backend**

Run: `cd webconsole/backend && python -m pytest tests/test_experiments_clases.py -q`
Expected: PASS.

- [ ] **Step 5: Escribir el test del frontend, incluido el caso sin cabeceras**

En `webconsole/frontend/src/__tests__/ExperimentsEvidence.test.tsx`:

```tsx
it('muestra las pruebas de plataforma como un bloque, no como un lump archivado', async () => {
  render(<MemoryRouter initialEntries={['/experiments']}><App /></MemoryRouter>)
  expect(await screen.findByText('445')).toBeTruthy()
  expect(screen.getByText(/la máquina probándose/i)).toBeTruthy()
  expect(screen.getByText('orq_1 · 90')).toBeTruthy()
})

it('renderiza bien cuando las cabeceras no están (la fixture del contrato no las manda)', async () => {
  sinCabeceras = true
  render(<MemoryRouter initialEntries={['/experiments']}><App /></MemoryRouter>)
  expect(await screen.findByText('Manifiestos')).toBeTruthy()
  expect(screen.queryByText(/pruebas de plataforma/i)).toBeNull()
})
```

- [ ] **Step 6: Cablear `ExperimentsPage.tsx`**

Leer las dos cabeceras con el `onResponse` que `request<T>` ya acepta, guardarlas en el
meta del listado, y renderizar el bloque **sólo si `X-Platform-Test-Count` está presente y
es > 0**. Reemplazar el `EvidenceViewControl` por `ClaseChips`.

- [ ] **Step 7: El gate del contrato — el paso que más importa de esta tarea**

Run: `cd webconsole/frontend && npm test -- contrato`
Expected: **10/10**. Si falla con una ruta imprevista, la causa es una petición nueva desde
`ExperimentsPage`: sacarla, no stubbearla en el contrato.

- [ ] **Step 8: Suites completas**

Run: `cd webconsole/backend && python -m pytest -q && cd ../frontend && npm test`
Expected: cero fallas.

- [ ] **Step 9: Commit — SÓLO si el usuario lo pidió**

```bash
git add webconsole/backend/src webconsole/backend/tests webconsole/frontend/src
git commit -m "feat(webconsole): Experimentos por clase y bloque de pruebas de plataforma"
```

---

## Task 9: Verificación integral

**Files:** ninguno nuevo. Esta tarea sólo corre y mira.

- [ ] **Step 1: Las tres suites**

```bash
cd webconsole/backend && python -m pytest -q
cd ../frontend && npm test
cd ../../ && .venv/bin/python -m pytest tests/
```
Expected: cero fallas en las tres.

- [ ] **Step 2: El contrato congelado, explícito**

Run: `cd webconsole/frontend && npm test -- contrato`
Expected: 10/10.
Run: `git status --short webconsole/frontend/src/__tests__/contrato/`
Expected: **vacío**. Un archivo modificado ahí invalida el gate entero.

- [ ] **Step 3: Levantar la consola y mirarla**

```bash
cd e-ovrt_experimental-setup/infra/platform && docker compose up -d
```

Abrir `http://localhost:8090/#/evidencia`, `#/evidencia/paso?n=3`,
`#/evidencia/resultado?id=clip_bench/t1_gdinotiny560_v2short_scene`, `#/runs`,
`#/experiments`.

- [ ] **Step 4: Verificar la propiedad que no puede perderse**

```bash
docker compose stop media-plane control-plane alert-distribution
```
Abrir `http://localhost:8090/#/evidencia` y recorrer los tres niveles.
Expected: **funciona completo con los tres planos apagados**. Si algún nivel muestra error
o vacío, hay una llamada a un servicio que no debería existir.

- [ ] **Step 5: Verificar contra las cifras en disco**

```bash
cd e-ovrt_experimental-setup && python3 -c "
import json
d = json.load(open('results/clip_bench/t1_gdinotiny560_v2short_scene/metrics.json'))
print('F1 en disco:', round(d['positives']['f1_micro'], 3))"
```
Expected: `0.789`, y la pantalla del resultado muestra **0,789**. Si difieren, la pantalla
está calculando en vez de leer.

- [ ] **Step 6: Informe al usuario**

Reportar: las tres suites con sus números, el contrato 10/10 sin tocar, la verificación con
los planos apagados, y la lista de lo que quedó pendiente de su decisión (los tres
hallazgos abiertos de la §11 del spec).

---

## Hallazgos que este plan NO resuelve

Están en la §11 del spec y se dejan como están, deliberadamente:

1. **`bench_nivel_a` muestra 4 resultados donde `results/index.md` declara 2 campañas.**
   `edir_vs_eind` y `replica_base560` conviven con `d1_gdinotiny560_edir_vs_eind`. Tocar eso
   es tocar la procedencia: se reporta, no se corrige por iniciativa propia.
2. **El badge del sidebar de Experimentos dice 11 mientras la pantalla muestra 1.**
3. **La pantalla dice «1 manifiestos».**

Si el usuario los quiere arreglar, son un plan aparte — el (1) especialmente, porque toca
`evidence-runs.yaml`, que este plan declara intocable.
