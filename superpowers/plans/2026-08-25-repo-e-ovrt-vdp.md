# Repo público `e-ovrt-vdp` — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Dejar listo en disco el repositorio público de documentación `/home/simonll4/projects/e-ovrt-vdp/` — portada, idea general de la plataforma en 5 documentos, resultados enlazados, fichas de los 5 repos, figuras, capturas de la consola, verificación de suites y checklist de publicación — con un guardián automático que impide referencias internas, enlaces rotos y cifras sin fuente.

**Architecture:** Un repo Markdown puro renderizado por GitHub (sin tooling de sitio), organizado en `informe/`, `plataforma/`, `resultados/`, `repositorios/`, `evidencia/` y `herramientas/`. El único código es `herramientas/verificar.py` (stdlib, con pytest), que se escribe primero y por el que pasa cada texto antes de darse por escrito. El contenido se **reescribe** para un lector externo a partir del set interno de `docs/`; nunca se copia.

**Tech Stack:** Markdown (GitHub Flavored), Python 3 stdlib + pytest (`/home/simonll4/projects/e-ovrt_experimental-setup/.venv/bin/python`, pytest 9.1.1), git, chromium headless (`~/.cache/ms-playwright/chromium-1228/chrome-linux64/chrome`), los venvs existentes de los 5 repos para correr sus suites.

**Spec:** `docs/superpowers/specs/2026-08-25-repo-e-ovrt-vdp-design.md`

## Global Constraints

- **NUNCA `git commit` ni `git push` ni crear remotes** (regla del usuario, `CLAUDE.md` del workspace). Cada tarea termina con `git status` mostrando los archivos nuevos; el usuario commitea cuando quiera. Por eso este plan **no tiene pasos de commit**.
- El repo vive en `/home/simonll4/projects/e-ovrt-vdp/` (hermano de los demás). Abreviatura en este plan: `$REPO`.
- **Autocontención hacia afuera** (spec §3 regla 1): en ningún `.md` del repo pueden aparecer `../docs/`, `docs/operacion`, `docs/nucleo`, `docs/decisiones`, `docs/informe`, `docs/sintesis`, `docs/specs`, `operacion/N`, `nucleo/N`, `ADR-N`, `F-N`, `D-N`, `AJ-N`, `R-NN`, `PODA-`, `T-FT-`, `[[PENDIENTE`, `[[FIGURA`, `[[CIFRA`, `/home/`. Lo verifica `herramientas/verificar.py`.
- **Cifras sólo enlazadas** (regla 2): toda fila con cifra en `resultados/README.md` enlaza a `https://github.com/simonll4/e-ovrt_experimental-setup/blob/HEAD/results/…` o `…/blob/HEAD/finetuning/…`.
- **Sin binarios pesados** (regla 3): se commitean figuras PNG/SVG, capturas PNG (~200 KB c/u) y el PDF del informe. Nada de videos, `.docx`, datasets, pesos, `runs/`.
- **Vocabulario del informe** (regla 4): CR-01 / CR-02, DBE / EBE, `media.detection.v1`, `bus.envelope.v1`, `bench_v3`, L1–L8, E-DIR / E-IND / E-HYB, `gdino-tiny-560`. Marco: los números son EL DATO de una combinación bajo un protocolo, no aprobado/fallado; nunca argumentar "OVD detecta mejor".
- Idioma: castellano; un párrafo de abstract en inglés en el README.
- URLs base de los repos (copiar exactas):
  - `https://github.com/Pandulc/e-ovrt_datasets`
  - `https://github.com/simonll4/e-ovrt_media-plane`
  - `https://github.com/Pandulc/e-ovrt_control-plane`
  - `https://github.com/simonll4/e-ovrt_experimental-setup`
  - `https://github.com/simonll4/e-ovrt_alert-distribution`
  - Paraguas: `https://github.com/simonll4/e-ovrt-vdp`
  - Base de resultados: `https://github.com/simonll4/e-ovrt_experimental-setup/blob/HEAD/results/` (abreviado `$RES` en este plan; en los archivos va la URL completa).
- Comando del guardián (se usa en casi todas las tareas): `cd $REPO && python3 herramientas/verificar.py` → debe imprimir `OK: 0 violaciones` y salir con 0.
- Fuentes internas para redactar (sólo lectura, nunca se citan ni se copian): `docs/sintesis/resultados-y-conclusiones.md`, `docs/nucleo/14-mapa-de-la-cadena.md`, `docs/nucleo/19-cierre-arquitectura-ciclo-de-vida-alerta.md`, `docs/specs/40…45`, `docs/informe/entregable/90-etapa3-texto-extraido.md` (§17.3), `90b` (§17.4), `90c` (§17.5), `docs/informe/figuras/README.md`, `e-ovrt_experimental-setup/results/index.md` y sus 4 índices, `e-ovrt_experimental-setup/infra/platform/README.md`, los `README.md` y `CLAUDE.md` de cada repo.

---

## Mapa de archivos

| Archivo | Responsabilidad | Tarea |
|---|---|---|
| `$REPO/.gitignore`, `LICENSE`, `CITATION.cff`, `CONTRIBUTING.md`, `PUBLICAR.md` | identidad, reglas, checklist del usuario | 1 |
| `$REPO/herramientas/verificar.py` | guardián: patrones prohibidos, enlaces, imágenes, cifras enlazadas; CLI | 2, 3, 4 |
| `$REPO/herramientas/tests/test_verificar.py` | tests del guardián con fixtures en `tmp_path` | 2, 3, 4 |
| `$REPO/README.md` | portada | 5 |
| `$REPO/plataforma/01-problema-y-enfoque.md`, `02-arquitectura.md` | la idea y la arquitectura | 6 |
| `$REPO/plataforma/03-flujo-de-una-alerta.md`, `04-escenarios-dbe-ebe.md` | el ciclo de vida de una alerta y los dos escenarios | 7 |
| `$REPO/plataforma/05-metodo-experimental.md` | bancos, GT, protocolo | 8 |
| `$REPO/repositorios/README.md` | fichas + tabla de versiones citadas | 9 |
| `$REPO/resultados/README.md` | la respuesta, cifras enlazadas, L1–L8 | 10 |
| `$REPO/evidencia/figuras/*` | fig-a…fig-f + generadores + README | 11 |
| `$REPO/evidencia/material-de-video.md` | procedencia del banco de clips | 12 |
| `$REPO/evidencia/consola/*` | capturas de la webconsole + README | 13 |
| `$REPO/evidencia/verificacion.md` | suites corridas hoy | 14 |
| `$REPO/informe/README.md` | qué versión, TOC, dónde va el PDF | 15 |
| `/home/simonll4/projects/CLAUDE.md` | registrar el nuevo hermano | 16 |

---

### Task 1: Esqueleto del repo, licencia, citación, reglas y checklist

**Files:**
- Create: `$REPO/.gitignore`, `$REPO/LICENSE`, `$REPO/CITATION.cff`, `$REPO/CONTRIBUTING.md`, `$REPO/PUBLICAR.md`
- Create (vacíos, para que las carpetas existan): `$REPO/informe/.gitkeep`, `$REPO/evidencia/consola/.gitkeep`

**Interfaces:**
- Produces: la estructura de carpetas que todas las tareas siguientes asumen; `CONTRIBUTING.md` es el texto de referencia de las 4 reglas; `PUBLICAR.md` es el único archivo exento del guardián.

- [ ] **Step 1: Crear la carpeta y el repo git local**

```bash
mkdir -p /home/simonll4/projects/e-ovrt-vdp/{informe,plataforma,resultados,repositorios,evidencia/figuras/scripts,evidencia/consola,herramientas/tests}
cd /home/simonll4/projects/e-ovrt-vdp && git init -b main
touch informe/.gitkeep evidencia/consola/.gitkeep
```

- [ ] **Step 2: `.gitignore`**

```gitignore
__pycache__/
.pytest_cache/
*.pyc
.venv/
# nunca binarios pesados (spec §3 regla 3)
*.mp4
*.mov
*.docx
*.pt
*.pth
```

- [ ] **Step 3: `LICENSE` (CC BY 4.0, texto legal completo)**

```bash
cd /home/simonll4/projects/e-ovrt-vdp
curl -fsSL https://creativecommons.org/licenses/by/4.0/legalcode.txt -o LICENSE && head -3 LICENSE
```

Esperado: la primera línea contiene `Attribution 4.0 International`. Si no hay red, escribir este `LICENSE` mínimo y anotar en `PUBLICAR.md` (paso 1) que hay que reemplazarlo por el texto legal completo antes de publicar:

```text
E-OVRT-VDP — documentación, figuras e informe
© 2026 Matías Lautaro Carrizo, Gabriel Agustín Guillaumet, Simon Llamosas

Este trabajo está licenciado bajo Creative Commons Attribution 4.0 International (CC BY 4.0).
Texto legal: https://creativecommons.org/licenses/by/4.0/legalcode
El código fuente de la plataforma vive en repositorios separados con su propia licencia.
```

- [ ] **Step 4: `CITATION.cff`**

```yaml
cff-version: 1.2.0
message: "Si usás este trabajo, citá el informe y el repositorio."
type: software
title: "E-OVRT-VDP — Plataforma experimental de detección open-vocabulary en video en tiempo real para monitoreo asistivo de riesgos en construcción"
authors:
  - family-names: Carrizo
    given-names: Matías Lautaro
  - family-names: Guillaumet
    given-names: Gabriel Agustín
  - family-names: Llamosas
    given-names: Simon
contact:
  - family-names: Llamosas
    given-names: Simon
repository-code: "https://github.com/simonll4/e-ovrt-vdp"
url: "https://github.com/simonll4/e-ovrt-vdp"
license: CC-BY-4.0
date-released: "2026-09-01"
version: "1.0"
keywords:
  - open-vocabulary detection
  - construction safety
  - PPE
  - Grounding DINO
  - real-time video
abstract: "Proyecto Integrador de Ingeniería en Informática (IUA Córdoba, Facultad de Ingeniería, 2026). Tutor: Mariano García Mattio. Plataforma experimental que aplica detección open-vocabulary sin entrenamiento a la detección asistiva de riesgos en obra (CR-01 sin casco, CR-02 sin chaleco), con motor de patrones temporal, bus de eventos, distribución MQTT y una consola para experimentos reproducibles; incluye la medición completa sobre bancos con referencia humana."
```

Nota: `date-released` y `version` se ajustan en `PUBLICAR.md` paso 8 al crear el Release.

- [ ] **Step 5: `CONTRIBUTING.md` — las cuatro reglas**

```markdown
# Cómo se escribe en este repositorio

Este repo es la cara pública del proyecto y **la única referencia externa que cita el informe**.
Lo lee gente que no participó del trabajo. Cuatro reglas, todas verificables con
`python3 herramientas/verificar.py`:

1. **Autocontenido hacia afuera.** No se referencia ningún documento de trabajo interno del
   equipo (bitácoras, registros de decisión, fichas de corrección, identificadores de
   hallazgos, rutas de una máquina). Sólo se cita: este repo, los cinco repos públicos de
   código, el informe y la bibliografía. Para un lector externo, cualquier otra cosa es un
   enlace muerto.
2. **Ninguna cifra sin fuente enlazada.** Cada número de resultado enlaza a la página de
   `results/` (o `finetuning/`) de `e-ovrt_experimental-setup` de donde sale, con `n` y
   material. Este repo muestra cifras; no las produce.
3. **Sin binarios pesados.** Sí: figuras PNG/SVG, capturas de la consola, el PDF del informe.
   No: videos, documentos de trabajo `.docx`, datasets, pesos de modelos, corridas.
4. **El vocabulario es el del informe.** CR-01 / CR-02, DBE / EBE, `media.detection.v1`,
   `bus.envelope.v1`, `bench_v3`, limitaciones L1–L8, E-DIR / E-IND / E-HYB,
   `gdino-tiny-560`. Sin sinónimos internos.

Marco de lectura para todo lo que muestre resultados: **los números son el dato de una
combinación bajo un protocolo, no un aprobado/fallado**. Un NO-GO pre-registrado es un
resultado y se muestra como tal.

Excepción única al guardián: `PUBLICAR.md` (checklist interno de publicación, se borra al
publicar). Una línea puntual se exime con el marcador `<!-- verificar:permitir -->` al final.
```

- [ ] **Step 6: `PUBLICAR.md` — checklist del usuario**

```markdown
# PUBLICAR.md — checklist de publicación (para el autor; borrar al terminar)

Todo lo de acá lo ejecuta el autor: git, GitHub, licencias y el PDF. Nada lo hace un agente.

1. [ ] **Licencias.** Decidir con los coautores: paraguas CC BY 4.0 (ya en `LICENSE`; si es la
       versión corta, reemplazar por el texto legal de
       https://creativecommons.org/licenses/by/4.0/legalcode.txt) y MIT para los 5 repos de
       código. Agregar `LICENSE` a cada repo de código.
2. [ ] **Barrido de secretos** en la historia de los 5 repos antes de hacerlos públicos.
       Verificado el 2026-08-25: `cameras/` nunca fue commiteado; el `.env` histórico de
       `infra/platform` sólo contenía `EOVRT_WORKSPACE` y `COMPOSE_PROFILES`. Como constancia,
       correr en cada repo: `git log -p --all | grep -n -i -E 'password|api_key|secret|rtsp://[^*]' | head`
       (o `gitleaks detect` si está instalado).
3. [ ] **Coherencia de READMEs.** El primer párrafo del `README.md` de cada repo dice lo mismo
       que su ficha en `repositorios/README.md`.
4. [ ] **Rama por defecto.** Los enlaces de este repo usan `blob/HEAD/` (= rama por defecto en
       GitHub). Antes de publicar, la rama por defecto de `e-ovrt_experimental-setup` tiene que
       contener `results/` y `finetuning/manifests/` tal como se enlazan.
5. [ ] **Crear el repo** `simonll4/e-ovrt-vdp` en GitHub, público. Descripción:
       *Plataforma experimental de detección open-vocabulary en video en tiempo real para
       monitoreo asistivo de riesgos en construcción — Proyecto Integrador, Ingeniería en
       Informática, IUA Córdoba (2026).* Topics: `open-vocabulary-detection`,
       `construction-safety`, `grounding-dino`, `computer-vision`, `thesis`, `zeromq`, `mqtt`.
       Luego: `git remote add origin git@github.com:simonll4/e-ovrt-vdp.git && git push -u origin main`.
6. [ ] **Hacer públicos** los 5 repos de código.
7. [ ] **Informe.** Cuando cierre el maestro: exportar PDF → `informe/E-OVRT-VDP-informe.pdf`;
       actualizar versión, fecha y tabla de contenidos en `informe/README.md`.
8. [ ] **Congelar.** En cada repo de código: `git tag -a informe-2026 -m "Versión citada en el informe" <commit> && git push origin informe-2026`.
       Completar la tabla de versiones de `repositorios/README.md` (tag, commit corto, fecha).
       Opcional, para permanencia: `grep -rl 'blob/HEAD/' --include='*.md' . | xargs sed -i 's#blob/HEAD/#blob/informe-2026/#g'`
       y volver a correr `python3 herramientas/verificar.py`. En `CITATION.cff` ajustar
       `date-released` y `version`. Crear el Release `v1.0` con el PDF adjunto.
9. [ ] **Citar.** Poner `https://github.com/simonll4/e-ovrt-vdp` en la sección de entrega /
       anexos del informe.
10. [ ] Borrar este archivo.
```

- [ ] **Step 7: Verificar el esqueleto**

```bash
cd /home/simonll4/projects/e-ovrt-vdp && find . -path ./.git -prune -o -type f -print | sort && git status --short | head
```

Esperado: `./.gitignore ./CITATION.cff ./CONTRIBUTING.md ./LICENSE ./PUBLICAR.md ./evidencia/consola/.gitkeep ./informe/.gitkeep`; `git status` los lista como untracked. **No commitear.**

---

### Task 2: `verificar.py` — regla (a) patrones prohibidos

**Files:**
- Create: `$REPO/herramientas/verificar.py`
- Create: `$REPO/herramientas/tests/test_verificar.py`
- Create: `$REPO/herramientas/__init__.py`, `$REPO/herramientas/tests/__init__.py` (vacíos)

**Interfaces:**
- Produces:
  - `PATRONES_PROHIBIDOS: list[tuple[str, str]]` — (regex, descripción).
  - `PERMITIR = "<!-- verificar:permitir -->"`.
  - `EXCLUIR = {"PUBLICAR.md"}`.
  - `archivos_md(raiz: Path) -> list[Path]` — todos los `.md` bajo `raiz`, sin `.git/`, sin `EXCLUIR`, ordenados.
  - `revisar_patrones(raiz: Path) -> list[dict]` — cada violación es `{"archivo": str (relativo a raiz), "linea": int, "regla": str, "texto": str}`.
- Tests corren con: `cd $REPO && /home/simonll4/projects/e-ovrt_experimental-setup/.venv/bin/python -m pytest herramientas/tests -q`

- [ ] **Step 1: Escribir los tests de la regla (a)**

`$REPO/herramientas/tests/test_verificar.py`:

```python
from pathlib import Path

import pytest

from herramientas import verificar


def _repo(tmp_path: Path, archivos: dict[str, str]) -> Path:
    for rel, contenido in archivos.items():
        p = tmp_path / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(contenido, encoding="utf-8")
    return tmp_path


def test_archivos_md_excluye_publicar_y_git(tmp_path):
    raiz = _repo(tmp_path, {
        "README.md": "# hola\n",
        "PUBLICAR.md": "operacion/128\n",
        ".git/x.md": "operacion/1\n",
        "plataforma/01.md": "texto\n",
    })
    nombres = [p.relative_to(raiz).as_posix() for p in verificar.archivos_md(raiz)]
    assert nombres == ["README.md", "plataforma/01.md"]


@pytest.mark.parametrize("linea", [
    "ver ../docs/informe/x.md",
    "según docs/operacion/128",
    "consta en operacion/97 §1",
    "nucleo/14 lo describe",
    "decidido en ADR-011",
    "hallazgo F-96.4",
    "decisión D-113.1",
    "ficha AJ-4.02",
    "redline R-13",
    "PODA-03",
    "tarea T-FT-016",
    "[[PENDIENTE: url]]",
    "[[FIGURA B]]",
    "[[CIFRA]]",
    "en /home/simonll4/projects/x",
])
def test_detecta_cada_patron_prohibido(tmp_path, linea):
    raiz = _repo(tmp_path, {"a.md": f"ok\n{linea}\n"})
    v = verificar.revisar_patrones(raiz)
    assert len(v) == 1
    assert v[0]["archivo"] == "a.md"
    assert v[0]["linea"] == 2
    assert v[0]["texto"] == linea


@pytest.mark.parametrize("linea", [
    "la carpeta docs/ de e-ovrt_experimental-setup",
    "condición CR-01 y CR-02",
    "campaña D1 y estrato B",
    "limitación L1",
    "prompt E-DIR y E-IND",
    "Figura E",
    "contrato media.detection.v1",
])
def test_no_marca_vocabulario_legitimo(tmp_path, linea):
    raiz = _repo(tmp_path, {"a.md": linea + "\n"})
    assert verificar.revisar_patrones(raiz) == []


def test_marcador_permitir_exime_la_linea(tmp_path):
    raiz = _repo(tmp_path, {"a.md": "ver operacion/128 <!-- verificar:permitir -->\n"})
    assert verificar.revisar_patrones(raiz) == []


def test_publicar_md_esta_exento(tmp_path):
    raiz = _repo(tmp_path, {"PUBLICAR.md": "operacion/128 y /home/x\n"})
    assert verificar.revisar_patrones(raiz) == []
```

- [ ] **Step 2: Correr los tests y ver que fallan**

```bash
cd /home/simonll4/projects/e-ovrt-vdp && touch herramientas/__init__.py herramientas/tests/__init__.py
/home/simonll4/projects/e-ovrt_experimental-setup/.venv/bin/python -m pytest herramientas/tests -q 2>&1 | tail -3
```

Esperado: `ModuleNotFoundError: No module named 'herramientas.verificar'` (o `ImportError`).

- [ ] **Step 3: Implementar la regla (a)**

`$REPO/herramientas/verificar.py`:

```python
#!/usr/bin/env python3
"""Guardián de las reglas de contenido del repo e-ovrt-vdp.

Reglas (ver CONTRIBUTING.md):
  (a) ningún patrón de referencia interna en los .md;
  (b) todo enlace relativo resuelve a un archivo/carpeta del repo;
  (c) toda fila con cifra en resultados/README.md enlaza a results/ o finetuning/;
  (d) toda imagen referenciada existe.
Uso: python3 herramientas/verificar.py [--raiz DIR] [--json]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

PATRONES_PROHIBIDOS: list[tuple[str, str]] = [
    (r"\.\./docs/", "ruta al set documental interno"),
    (r"\bdocs/(operacion|nucleo|decisiones|informe|sintesis|specs)\b", "ruta al set documental interno"),
    (r"\boperacion/\d", "referencia a bitácora interna"),
    (r"\bnucleo/\d", "referencia a documento interno de núcleo"),
    (r"\bADR-\d", "referencia a registro de decisión interno"),
    (r"\bF-\d", "identificador interno de hallazgo"),
    (r"\bD-\d", "identificador interno de decisión"),
    (r"\bAJ-\d", "ficha interna de ajuste"),
    (r"\bR-\d\d", "redline interno"),
    (r"\bPODA-", "ficha interna de poda"),
    (r"\bT-FT-", "identificador interno de tarea"),
    (r"\[\[PENDIENTE", "marcador de borrador"),
    (r"\[\[FIGURA", "marcador de borrador"),
    (r"\[\[CIFRA", "marcador de borrador"),
    (r"/home/", "ruta absoluta de una máquina"),
]
_COMPILADOS = [(re.compile(rx), desc) for rx, desc in PATRONES_PROHIBIDOS]

PERMITIR = "<!-- verificar:permitir -->"
EXCLUIR = {"PUBLICAR.md"}


def archivos_md(raiz: Path) -> list[Path]:
    out = []
    for p in sorted(raiz.rglob("*.md")):
        if ".git" in p.relative_to(raiz).parts:
            continue
        if p.name in EXCLUIR:
            continue
        out.append(p)
    return out


def _violacion(raiz: Path, archivo: Path, linea: int, regla: str, texto: str) -> dict:
    return {
        "archivo": archivo.relative_to(raiz).as_posix(),
        "linea": linea,
        "regla": regla,
        "texto": texto.rstrip("\n"),
    }


def revisar_patrones(raiz: Path) -> list[dict]:
    violaciones = []
    for archivo in archivos_md(raiz):
        for n, linea in enumerate(archivo.read_text(encoding="utf-8").splitlines(), start=1):
            if PERMITIR in linea:
                continue
            for rx, desc in _COMPILADOS:
                if rx.search(linea):
                    # una violación por línea: el primer patrón que matchea alcanza para señalarla
                    violaciones.append(_violacion(raiz, archivo, n, f"(a) {desc}: {rx.pattern}", linea))
                    break
    return violaciones
```

- [ ] **Step 4: Correr los tests y ver que pasan**

```bash
cd /home/simonll4/projects/e-ovrt-vdp && /home/simonll4/projects/e-ovrt_experimental-setup/.venv/bin/python -m pytest herramientas/tests -q 2>&1 | tail -3
```

Esperado: `25 passed` (1 + 15 + 7 + 1 + 1 = 25).

---

### Task 3: `verificar.py` — reglas (b) enlaces relativos y (d) imágenes

**Files:**
- Modify: `$REPO/herramientas/verificar.py` (agregar debajo de `revisar_patrones`)
- Modify: `$REPO/herramientas/tests/test_verificar.py` (agregar al final)

**Interfaces:**
- Consumes: `archivos_md`, `_violacion` de la Tarea 2.
- Produces:
  - `ENLACE = re.compile(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")` — captura el destino de `[texto](destino)` y `![alt](destino)`.
  - `revisar_enlaces(raiz: Path) -> list[dict]` — regla (b): destinos relativos que no existen.
  - `revisar_imagenes(raiz: Path) -> list[dict]` — regla (d): destinos de `![…](…)` relativos que no existen.

- [ ] **Step 1: Tests de (b) y (d)**

Agregar a `test_verificar.py`:

```python
def test_enlace_relativo_existente_pasa(tmp_path):
    raiz = _repo(tmp_path, {
        "README.md": "ver [la guía](plataforma/01.md) y [ancla](plataforma/01.md#seccion) y [carpeta](evidencia/)\n",
        "plataforma/01.md": "# x\n",
        "evidencia/.gitkeep": "",
    })
    assert verificar.revisar_enlaces(raiz) == []


def test_enlace_relativo_roto_falla(tmp_path):
    raiz = _repo(tmp_path, {"README.md": "ver [x](no/existe.md)\n"})
    v = verificar.revisar_enlaces(raiz)
    assert len(v) == 1 and v[0]["linea"] == 1 and "no/existe.md" in v[0]["regla"]


def test_enlaces_externos_mailto_y_anclas_se_ignoran(tmp_path):
    raiz = _repo(tmp_path, {
        "README.md": "[a](https://github.com/x) [b](http://x) [c](mailto:x@y) [d](#local)\n",
    })
    assert verificar.revisar_enlaces(raiz) == []


def test_enlace_relativo_al_padre_del_archivo(tmp_path):
    raiz = _repo(tmp_path, {
        "plataforma/02.md": "![fig](../evidencia/figuras/fig-a.png)\n",
        "evidencia/figuras/fig-a.png": "png",
    })
    assert verificar.revisar_enlaces(raiz) == []
    assert verificar.revisar_imagenes(raiz) == []


def test_imagen_inexistente_falla(tmp_path):
    raiz = _repo(tmp_path, {"a.md": "![fig](figuras/nada.png)\n"})
    v = verificar.revisar_imagenes(raiz)
    assert len(v) == 1 and v[0]["regla"].startswith("(d)")
```

- [ ] **Step 2: Correr y ver fallar**

```bash
cd /home/simonll4/projects/e-ovrt-vdp && /home/simonll4/projects/e-ovrt_experimental-setup/.venv/bin/python -m pytest herramientas/tests -q 2>&1 | tail -3
```

Esperado: 5 fallos con `AttributeError: module 'herramientas.verificar' has no attribute 'revisar_enlaces'`.

- [ ] **Step 3: Implementar (b) y (d)**

Agregar a `verificar.py` después de `revisar_patrones`:

```python
ENLACE = re.compile(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
IMAGEN = re.compile(r"!\[[^\]]*\]\(([^)\s]+)")
_EXTERNO = ("http://", "https://", "mailto:")


def _destinos_relativos(linea: str, rx: re.Pattern) -> list[str]:
    out = []
    for destino in rx.findall(linea):
        if destino.startswith(_EXTERNO) or destino.startswith("#"):
            continue
        out.append(destino.split("#", 1)[0])
    return out


def _revisar_destinos(raiz: Path, rx: re.Pattern, etiqueta: str) -> list[dict]:
    violaciones = []
    for archivo in archivos_md(raiz):
        for n, linea in enumerate(archivo.read_text(encoding="utf-8").splitlines(), start=1):
            for destino in _destinos_relativos(linea, rx):
                if not (archivo.parent / destino).exists():
                    violaciones.append(_violacion(raiz, archivo, n, f"{etiqueta} destino inexistente: {destino}", linea))
    return violaciones


def revisar_enlaces(raiz: Path) -> list[dict]:
    return _revisar_destinos(raiz, ENLACE, "(b)")


def revisar_imagenes(raiz: Path) -> list[dict]:
    return _revisar_destinos(raiz, IMAGEN, "(d)")
```

- [ ] **Step 4: Correr y ver pasar**

```bash
cd /home/simonll4/projects/e-ovrt-vdp && /home/simonll4/projects/e-ovrt_experimental-setup/.venv/bin/python -m pytest herramientas/tests -q 2>&1 | tail -3
```

Esperado: `30 passed`.

---

### Task 4: `verificar.py` — regla (c) cifras enlazadas, `revisar_todo` y CLI

**Files:**
- Modify: `$REPO/herramientas/verificar.py`
- Modify: `$REPO/herramientas/tests/test_verificar.py`

**Interfaces:**
- Produces:
  - `CIFRA = re.compile(r"\d+,\d+|\bp95\b|\bn\s*=\s*\d")`.
  - `ENLACE_FUENTE = re.compile(r"https://github\.com/simonll4/e-ovrt_experimental-setup/blob/[^/\s)]+/(results|finetuning)/")`.
  - `ARCHIVO_CIFRAS = Path("resultados/README.md")`.
  - `revisar_cifras(raiz: Path) -> list[dict]` — regla (c) sólo sobre `resultados/README.md`; una fila de tabla es "de encabezado" si la siguiente línea no vacía empieza con `|` seguido de `-` o `:`; las filas de encabezado y las separadoras se ignoran.
  - `revisar_todo(raiz: Path) -> list[dict]` — concatena (a), (b), (c), (d).
  - `main(argv: list[str] | None = None) -> int` — imprime `archivo:línea: regla — texto` por violación y `OK: 0 violaciones` si no hay; `--json` imprime la lista; `--raiz` (default: carpeta padre de `herramientas/`); exit 1 si hay violaciones.

- [ ] **Step 1: Tests de (c), `revisar_todo` y CLI**

Agregar a `test_verificar.py`:

```python
RES = "https://github.com/simonll4/e-ovrt_experimental-setup/blob/HEAD/results/clip_bench/index.md"
FT = "https://github.com/simonll4/e-ovrt_experimental-setup/blob/HEAD/finetuning/manifests/x.json"


def test_fila_con_cifra_y_enlace_a_results_pasa(tmp_path):
    raiz = _repo(tmp_path, {"resultados/README.md":
        "| Qué | Cifra | Fuente |\n|---|---|---|\n"
        f"| G1 | F1 **0,930** (n=34) | [clip_bench]({RES}) |\n"
        f"| FT | bare_head 0,0909 | [manifest]({FT}) |\n"})
    assert verificar.revisar_cifras(raiz) == []


def test_fila_con_cifra_sin_enlace_falla(tmp_path):
    raiz = _repo(tmp_path, {"resultados/README.md":
        "| Qué | Cifra |\n|---|---|\n| G1 | F1 0,930 |\n| p95 | 64,534 ms |\n"})
    v = verificar.revisar_cifras(raiz)
    assert [x["linea"] for x in v] == [3, 4]
    assert all(x["regla"].startswith("(c)") for x in v)


def test_encabezado_con_p95_o_n_no_se_marca(tmp_path):
    raiz = _repo(tmp_path, {"resultados/README.md":
        "| Tramo | p95 | n= |\n|---|---|---|\n"
        f"| distribución | 64,534 ms | [x]({RES}) |\n"})
    assert verificar.revisar_cifras(raiz) == []


def test_cifras_solo_aplica_a_resultados(tmp_path):
    raiz = _repo(tmp_path, {"plataforma/02.md": "| a | 0,5 |\n|---|---|\n| b | 0,930 |\n"})
    assert verificar.revisar_cifras(raiz) == []


def test_enlace_a_otro_repo_no_cuenta_como_fuente(tmp_path):
    raiz = _repo(tmp_path, {"resultados/README.md":
        "| a | b |\n|---|---|\n| G1 | 0,930 [x](https://github.com/simonll4/e-ovrt_media-plane) |\n"})
    assert len(verificar.revisar_cifras(raiz)) == 1


def test_revisar_todo_concatena(tmp_path):
    raiz = _repo(tmp_path, {
        "a.md": "operacion/1 y [x](no.md) y ![f](no.png)\n",
        "resultados/README.md": "| a | b |\n|---|---|\n| c | 0,5 |\n",
    })
    reglas = sorted(v["regla"][:3] for v in verificar.revisar_todo(raiz))
    assert reglas == ["(a)", "(b)", "(b)", "(c)", "(d)"]


def test_main_exit_code_y_salida(tmp_path, capsys):
    raiz = _repo(tmp_path, {"a.md": "limpio\n"})
    assert verificar.main(["--raiz", str(raiz)]) == 0
    assert "OK: 0 violaciones" in capsys.readouterr().out
    raiz2 = _repo(tmp_path / "otro", {"a.md": "operacion/1\n"})
    assert verificar.main(["--raiz", str(raiz2)]) == 1
    assert "a.md:1:" in capsys.readouterr().out


def test_main_json(tmp_path, capsys):
    raiz = _repo(tmp_path, {"a.md": "ADR-011\n"})
    assert verificar.main(["--raiz", str(raiz), "--json"]) == 1
    datos = json.loads(capsys.readouterr().out)
    assert datos[0]["archivo"] == "a.md" and datos[0]["linea"] == 1
```

Agregar `import json` al inicio del archivo de tests.

- [ ] **Step 2: Correr y ver fallar**

```bash
cd /home/simonll4/projects/e-ovrt-vdp && /home/simonll4/projects/e-ovrt_experimental-setup/.venv/bin/python -m pytest herramientas/tests -q 2>&1 | tail -3
```

Esperado: 8 fallos por `AttributeError` (`revisar_cifras`, `revisar_todo`, `main`).

- [ ] **Step 3: Implementar (c), `revisar_todo` y `main`**

Agregar al final de `verificar.py`:

```python
CIFRA = re.compile(r"\d+,\d+|\bp95\b|\bn\s*=\s*\d")
ENLACE_FUENTE = re.compile(
    r"https://github\.com/simonll4/e-ovrt_experimental-setup/blob/[^/\s)]+/(results|finetuning)/"
)
ARCHIVO_CIFRAS = Path("resultados/README.md")
_SEPARADOR = re.compile(r"^\|\s*[-:]")


def _es_encabezado(lineas: list[str], i: int) -> bool:
    for siguiente in lineas[i + 1:]:
        if siguiente.strip():
            return bool(_SEPARADOR.match(siguiente))
    return False


def revisar_cifras(raiz: Path) -> list[dict]:
    archivo = raiz / ARCHIVO_CIFRAS
    if not archivo.exists():
        return []
    lineas = archivo.read_text(encoding="utf-8").splitlines()
    violaciones = []
    for i, linea in enumerate(lineas):
        if not linea.lstrip().startswith("|") or _SEPARADOR.match(linea) or _es_encabezado(lineas, i):
            continue
        if CIFRA.search(linea) and not ENLACE_FUENTE.search(linea):
            violaciones.append(_violacion(raiz, archivo, i + 1, "(c) fila con cifra sin enlace a results/ o finetuning/", linea))
    return violaciones


def revisar_todo(raiz: Path) -> list[dict]:
    return revisar_patrones(raiz) + revisar_enlaces(raiz) + revisar_cifras(raiz) + revisar_imagenes(raiz)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--raiz", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--json", action="store_true", help="salida JSON")
    args = parser.parse_args(argv)
    violaciones = revisar_todo(args.raiz.resolve())
    if args.json:
        print(json.dumps(violaciones, ensure_ascii=False, indent=2))
    elif violaciones:
        for v in violaciones:
            print(f"{v['archivo']}:{v['linea']}: {v['regla']} — {v['texto']}")
        print(f"{len(violaciones)} violaciones")
    else:
        print("OK: 0 violaciones")
    return 1 if violaciones else 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Correr tests y el guardián sobre el repo real**

```bash
cd /home/simonll4/projects/e-ovrt-vdp && /home/simonll4/projects/e-ovrt_experimental-setup/.venv/bin/python -m pytest herramientas/tests -q 2>&1 | tail -3
python3 herramientas/verificar.py
```

Esperado: `38 passed`; y `OK: 0 violaciones` (`CONTRIBUTING.md` no contiene ningún patrón; `PUBLICAR.md` está exento).

---

### Task 5: `README.md` — la portada

**Files:**
- Create: `$REPO/README.md`

**Interfaces:**
- Consumes: la figura A existirá en `evidencia/figuras/fig-a-vista-de-procesos.png` (Tarea 11). Hasta esa tarea, el guardián marcará la imagen como inexistente: **es esperable** y se resuelve en la Tarea 11. Todos los demás enlaces relativos apuntan a archivos que las Tareas 6–15 crean; correr el guardián al final de cada tarea y esperar que las violaciones (b)/(d) restantes correspondan sólo a archivos de tareas aún no hechas.
- Produces: la portada; los nombres de archivo que enlaza fijan los nombres del resto del repo.

- [ ] **Step 1: Escribir `README.md`** con esta estructura y contenido (redactar en prosa propia; no copiar del set interno):

```markdown
# E-OVRT-VDP — Plataforma experimental de detección open-vocabulary en video en tiempo real para monitoreo asistivo de riesgos en construcción

Proyecto Integrador · Ingeniería en Informática · IUA Córdoba, Facultad de Ingeniería · 2026
Autores: Matías Lautaro Carrizo · Gabriel Agustín Guillaumet · Simon Llamosas — Tutor: Mariano García Mattio

> **Abstract.** [6–8 líneas en inglés: an experimental platform that applies open-vocabulary
> detection *without training* to assistive detection of construction-site risks — two
> conditions, CR-01 (no helmet) and CR-02 (no vest) — expressed in natural language; a
> temporal pattern engine with per-subject identity, a versioned event bus, MQTT QoS 1
> distribution and a console for reproducible experiments; measured on an image benchmark of
> 6,477 images from 3 sources and a clip bench of 47 clips with human temporal ground truth,
> both offline and under real-time constraints.]

## La pregunta, y la respuesta en una línea
[La pregunta del trabajo: qué rendimiento se obtiene hoy, en construcción civil, con
detección open-vocabulary sin entrenar, expresando las condiciones de riesgo en lenguaje —
y qué aporta la plataforma alrededor del modelo.]
[Respuesta: la detección zero-shot alcanza para sostener CR-01 y no para CR-02; la
plataforma alrededor del modelo cambia el resultado más que cualquier elección de modelo o
de prompt — con las mismas detecciones bit a bit, pasar de granularidad de escena a sujeto
lleva el F1 de alertas de 0,789 a 0,930 — y esa ganancia sobrevive a la restricción de
tiempo real. Enlazar a `resultados/README.md` para las cifras con fuente.]

## Qué es la plataforma, en una figura
![Vista de procesos de la plataforma](evidencia/figuras/fig-a-vista-de-procesos.png)
[2–3 líneas: tres servicios HTTP config-driven —medios `:8080`, control `:8081`,
distribución `:8082`—, un bus de eventos versionados y una consola que orquesta
experimentos reproducibles. Enlazar a `plataforma/02-arquitectura.md`.]

## Cómo leer este repositorio
| Si querés… | Leé |
|---|---|
| el informe completo | [`informe/`](informe/README.md) |
| entender la idea y la arquitectura en 20 minutos | [`plataforma/`](plataforma/01-problema-y-enfoque.md) — 5 documentos cortos, en orden |
| ver los resultados con su fuente | [`resultados/`](resultados/README.md) |
| ir al código | [`repositorios/`](repositorios/README.md) |
| ver la plataforma funcionando | [`evidencia/consola/`](evidencia/consola/README.md) y las [figuras](evidencia/figuras/README.md) |

## Los cinco repositorios de código
| Repositorio | Qué es | Puerto / rol |
|---|---|---|
| [e-ovrt_media-plane](https://github.com/simonll4/e-ovrt_media-plane) | servicio de inferencia open-vocabulary (FastAPI); publica `media.detection.v1` | `:8080` |
| [e-ovrt_control-plane](https://github.com/Pandulc/e-ovrt_control-plane) | motor de patrones de riesgo CR-01 / CR-02 con persistencia temporal e identidad por sujeto | `:8081` |
| [e-ovrt_alert-distribution](https://github.com/simonll4/e-ovrt_alert-distribution) | distribución de alertas confirmadas por MQTT QoS 1 con idempotencia | `:8082` |
| [e-ovrt_experimental-setup](https://github.com/simonll4/e-ovrt_experimental-setup) | prompts, manifiestos de experimento, **resultados**, consola web, deploy integral, fine-tuning | consola `:8090` |
| [e-ovrt_datasets](https://github.com/Pandulc/e-ovrt_datasets) | adquisición, conversión y curación de datasets; el banco de imágenes `bench_v3` | — |

## Cómo citar
[Una línea: ver `CITATION.cff` (GitHub ofrece "Cite this repository"). Licencia CC BY 4.0 para
este repo; los repos de código tienen la suya.]
```

- [ ] **Step 2: Guardián**

```bash
cd /home/simonll4/projects/e-ovrt-vdp && python3 herramientas/verificar.py
```

Esperado: sólo violaciones (b)/(d) por archivos que todavía no existen (`evidencia/figuras/fig-a-…png`, `informe/README.md`, `plataforma/01-…`, `resultados/README.md`, `repositorios/README.md`, `evidencia/consola/README.md`, `evidencia/figuras/README.md`). **Cero violaciones (a).** Si aparece alguna (a), corregir el texto.

---

### Task 6: `plataforma/01-problema-y-enfoque.md` y `02-arquitectura.md`

**Files:**
- Create: `$REPO/plataforma/01-problema-y-enfoque.md`
- Create: `$REPO/plataforma/02-arquitectura.md`

**Interfaces:**
- Consumes: figura A (`../evidencia/figuras/fig-a-vista-de-procesos.png`, Tarea 11).
- Produces: los dos primeros documentos de la serie; cada uno termina con "Siguiente: [`0N-…`](0N-….md)".

- [ ] **Step 1: Leer las fuentes internas** (sólo para redactar): `docs/informe/entregable/96a-informe-v11-frontmatter-intro-objetivos-plan.md` (introducción y objetivos), `docs/nucleo/09-*` (defensa de OVD — regla: **nunca "OVD detecta mejor"**), `docs/nucleo/14-mapa-de-la-cadena.md`, `docs/specs/40-plataforma-etapa4-integrador.md`, `docs/informe/entregable/90b-etapa4-texto-extraido.md` §17.4.1–17.4.3, `e-ovrt_experimental-setup/infra/platform/README.md`.

- [ ] **Step 2: Escribir `01-problema-y-enfoque.md`** (~1 página) con estas secciones y afirmaciones:

```markdown
# 1 · El problema y el enfoque
## El riesgo que se mira
- Obra de construcción; equipo de protección personal (EPP) como condición observable.
- Dos condiciones de riesgo: **CR-01, persona sin casco** y **CR-02, persona sin chaleco**.
  Se eligen porque son observables en video, frecuentes y con consecuencias distintas
  (CR-01 severidad alta, CR-02 media).
## Por qué detección open-vocabulary sin entrenar
- Un detector open-vocabulary recibe la clase en lenguaje natural ("person", "helmet",
  "vest", "bare head") y no requiere un dataset etiquetado por obra.
- La apuesta del trabajo NO es que detecte mejor que un modelo entrenado: es medir qué
  rendimiento da hoy sin entrenar y qué agrega la plataforma alrededor.
## La hipótesis de plataforma
- Una detección por frame no es una alerta. Entre ambas hay: evidencia por sujeto,
  persistencia temporal, confirmación, política de notificación. Ese tramo es la
  plataforma, y es lo que se diseña, construye y mide.
## Qué se mide
- Nivel de percepción (imágenes), nivel de plataforma (alertas contra referencia humana en
  clips) y operación en vivo (bus, latencia, throughput). Ver `05-metodo-experimental.md`.
Siguiente: [`02-arquitectura.md`](02-arquitectura.md)
```

- [ ] **Step 3: Escribir `02-arquitectura.md`** (~1,5 páginas):

```markdown
# 2 · Arquitectura
![Vista de procesos](../evidencia/figuras/fig-a-vista-de-procesos.png)
## Tres servicios HTTP config-driven y una consola
| Servicio | Puerto | Hace | No hace |
|---|---|---|---|
| Plano de medios (`e-ovrt_media-plane`) | `:8080` | ingesta (carpeta de imágenes, video, RTSP, OAK-D), inferencia open-vocabulary, publica eventos `media.detection.v1` | patrones, alertas, UI |
| Plano de control (`e-ovrt_control-plane`) | `:8081` | consume detecciones, evalúa CR-01/CR-02 con persistencia temporal e identidad por sujeto, emite alertas confirmadas | notificación externa, UI |
| Distribución (`e-ovrt_alert-distribution`) | `:8082` | consume alertas confirmadas, política de notificación, entrega MQTT QoS 1 idempotente | recalcular severidad |
| Consola web (`e-ovrt_experimental-setup/webconsole`) | `:8090` | cliente HTTP de los tres; define, lanza y compara experimentos reproducibles | consumir el bus |
- Config-driven: YAML sin rutas ni umbrales hardcodeados; cada servicio expone `POST /api/runs`,
  `GET /healthz`, `GET /readyz`; el modelo se carga una vez al arrancar.
## Contratos versionados
- `media.detection.v1` (detección por frame, con `track_id` opcional), `bus.envelope.v1`
  (sobre del bus: `seq`, `run_id`, timestamps), eventos de patrón y alerta del control,
  `run.lifecycle.v1` (inicio/fin de corrida). Compatibilidad hacia adelante: el emisor omite
  nulos, el consumidor tolera campos extra.
## Dos formas de acoplarse
- Por archivo (`detections.jsonl` → relectura) y por bus ZeroMQ PUB/SUB + msgpack. El JSONL
  es la verdad en ambas: toda corrida en vivo es re-evaluable offline con artefactos idénticos.
  Detalle en `04-escenarios-dbe-ebe.md`.
## Deploy integral
- Un `docker compose` con 13 servicios (consola, control, distribución, broker MQTT y una
  flota de instancias del plano de medios por modelo, encendidas desde la consola).
  Paridad de rutas: los tres servicios montan el workspace en la misma ruta absoluta que el
  host, porque los contratos intercambian rutas por filesystem compartido.
  Fuente: `infra/platform/` en `e-ovrt_experimental-setup` (enlace).
Siguiente: [`03-flujo-de-una-alerta.md`](03-flujo-de-una-alerta.md)
```

- [ ] **Step 4: Guardián**

```bash
cd /home/simonll4/projects/e-ovrt-vdp && python3 herramientas/verificar.py | grep -v -E 'fig-a-vista|informe/README|resultados/README|repositorios/README|consola/README|figuras/README|03-flujo|04-escenarios|05-metodo' ; echo "exit=$?"
```

Esperado: ninguna línea de violación fuera de las esperadas por tareas futuras (el `grep -v` las filtra); en particular **ninguna (a)**.

---

### Task 7: `plataforma/03-flujo-de-una-alerta.md` y `04-escenarios-dbe-ebe.md`

**Files:**
- Create: `$REPO/plataforma/03-flujo-de-una-alerta.md`
- Create: `$REPO/plataforma/04-escenarios-dbe-ebe.md`

**Interfaces:**
- Consumes: figuras E y C (`../evidencia/figuras/fig-e-maquina-de-estados.png`, `../evidencia/figuras/fig-c-alerta-confirmada.png`, Tarea 11).

- [ ] **Step 1: Leer fuentes internas**: `docs/nucleo/19-cierre-arquitectura-ciclo-de-vida-alerta.md`, `docs/informe/entregable/90-etapa3-texto-extraido.md` §17.3.8 (máquina de estados), `docs/informe/figuras/README.md` (las 3 advertencias), `e-ovrt_experimental-setup/results/realtime/index.md` §1–§3, `e-ovrt_experimental-setup/results/index.md` § "La cadena temporal completa se cita POR TRAMOS".

- [ ] **Step 2: Escribir `03-flujo-de-una-alerta.md`**:

```markdown
# 3 · De una detección a una alerta notificada
![Máquina de estados del patrón](../evidencia/figuras/fig-e-maquina-de-estados.png)
## Los pasos
1. **Detección** por frame (`media.detection.v1`): cajas `person`, `helmet`, `vest` y,
   opcionalmente, `bare_head`.
2. **Evidencia por sujeto**: la condición se evalúa por persona; la identidad (`track_id`)
   la agrega el plano de control como decorador de la fuente, igual en offline y en vivo.
   Dos granularidades medidas: **escena** (una condición por frame) y **sujeto** (una por persona).
3. **Formulación de la condición**: evidencia positiva + inferencia (E-IND: "hay persona y no
   hay casco asociado") frente a prompts directos de ausencia (E-DIR: "bare head"). La
   plataforma soporta ambas y una fusión (E-HYB); cuál rinde, en `resultados/`.
4. **Persistencia y confirmación**: un patrón pasa por **cinco estados** — inactivo,
   candidato, confirmado, en enfriamiento, y reapertura a candidato — con
   `confirm_after_ms` 4.000 (CR-01) y 7.000 (CR-02). Advertencia de lectura: la máquina
   tiene cinco estados y reabre a candidato, no vuelve a inactivo.
5. **Alerta confirmada** → bus de alertas `:5558` → **distribución** MQTT QoS 1 con
   idempotencia por (`notification_id`, canal) y `alert_id` determinístico (UUID5), para
   que una re-entrega nunca duplique. Advertencia de lectura: la distribución está **en
   línea, continua** con el resto de la cadena (no es un lote posterior).
## Qué se ve
![Alerta confirmada sobre el video](../evidencia/figuras/fig-c-alerta-confirmada.png)
[2 líneas: fotograma con la caja del sujeto y el rótulo de la alerta confirmada.]
Siguiente: [`04-escenarios-dbe-ebe.md`](04-escenarios-dbe-ebe.md)
```

- [ ] **Step 3: Escribir `04-escenarios-dbe-ebe.md`**:

```markdown
# 4 · Dos escenarios: offline (DBE) y en vivo (EBE)
## DBE — acople por archivo
- El plano de medios escribe `runs/<id>/detections.jsonl`; el control lo relee. El
  repositorio de artefactos es la fuente de verdad; permite re-evaluar cualquier corrida.
## EBE — acople por bus
- ZeroMQ PUB/SUB + msgpack, sobre `bus.envelope.v1` con `seq`. Los huecos de `seq` se
  cuentan (`bus_dropped_events`) y degradan la corrida; nunca se silencian.
- **Orden de arranque inverso al flujo de datos**: primero se suscribe la distribución,
  después el control, y por último se dispara el plano de medios — PUB/SUB pierde lo que se
  publicó antes de la suscripción. Advertencia de lectura para la figura A.
## Hardware real
- Cámara OAK-D Pro PoE (IP fija, SDK DepthAI, con preselección liviana on-device opcional) y
  cámaras RTSP. La consola graba y recorta clips desde el vivo.
## Cómo se cita el tiempo (sin sumar percentiles)
| Tramo | Qué mide |
|---|---|
| `capture_to_host` | fotón → dequeue en el host |
| G2A | dequeue → alerta, por frame |
| `t_alert-system` | inicio anotado del episodio → alerta; dominado por la persistencia deliberada (4–7 s) |
| `t_alert-notification` | bus de alertas → PUBACK MQTT |
- Cada tramo tiene su reloj, su dueño y su cifra; los p95 **no son aditivos**. Las cifras,
  con `n`, en `resultados/`.
Siguiente: [`05-metodo-experimental.md`](05-metodo-experimental.md)
```

- [ ] **Step 4: Guardián** (mismo comando y criterio que Tarea 6, Step 4).

---

### Task 8: `plataforma/05-metodo-experimental.md`

**Files:**
- Create: `$REPO/plataforma/05-metodo-experimental.md`

- [ ] **Step 1: Leer fuentes internas**: `e-ovrt_datasets/datasets/registry/bench_v3.md`, `e-ovrt_experimental-setup/results/index.md` (§ "Reglas de lectura", § "Limitaciones declaradas", § "Licencias de los pesos"), `results/clip_bench/index.md` (cabecera: banco 47, 32/15, 37 episodios; § estrato B), `docs/informe/entregable/90c-etapa5-texto-extraido.md` §17.5 (bloques por pregunta de medición).

- [ ] **Step 2: Escribir el documento**:

```markdown
# 5 · Método experimental
## Tres niveles de medición
| Nivel | Material | Pregunta |
|---|---|---|
| Percepción (imágenes) | `bench_v3` | qué ve el detector sin entrenar; costo de una clase nueva |
| Percepción por sujeto (Nivel A) | `bench_v3` + clips | estado "sin EPP" por persona; E-DIR vs E-IND |
| Plataforma (Nivel B) | banco de clips con referencia humana | alertas contra episodios anotados |
| Operación (EBE) | corridas en vivo | integridad del bus, latencia, throughput, calidad bajo tiempo real |
## `bench_v3` — 6.477 imágenes, 3 fuentes independientes
- `bench_obra` (147, núcleo curado con pasada visual; CC BY 4.0), `chv` (1.330; uso académico
  con cita, sin redistribución — limitación L7), `shel5k` (5.000; CC BY 4.0; `bare_head`
  nativo). Cada imagen lleva su estrato; **se reporta por estrato y agregado, nunca sólo el
  agregado**. Manifiesto con sha256 por fuente; regenerable byte a byte desde las fuentes.
## Banco de clips con referencia temporal humana
- **47 clips**: 34 de un rodaje propio en obra (guionado, hardware real, GT anotado en CVAT en
  dos pasadas) + **13 de internet** (obra real no guionada). 32 positivos / 15 negativos /
  37 episodios. El GT es humano ⇒ su calidad es un resultado: una revisión ciega tumbó 5 de 7
  declaraciones de episodio del lote de internet. Procedencia en `evidencia/material-de-video.md`.
## Campañas por pregunta de medición
- Una campaña = una combinación (modelo × prompt set × granularidad × densidad) bajo un
  protocolo. Criterios de veredicto **fijados antes de correr** (pre-registro); un NO-GO es
  un resultado.
- Ejes: selección de modelo · formulación (E-DIR / E-IND / E-HYB) · granularidad (escena /
  sujeto) · densidad de evidencia (30 → 4,29 → 2,00 → 1,15 fps) · obra real no guionada ·
  distribución · fine-tuning acotado (jornada con protocolo, en clúster, gates de ganancia,
  retención y open-vocabulary).
## Reglas de lectura
- Toda cifra con material y `n`; escenarios desbalanceados ⇒ reportar por escenario y
  estrato (L5); FAR/hora se publica como conteo crudo y no sostiene cota (L1).
## Licencias de los modelos
- Grounding DINO: Apache-2.0. YOLOE: AGPL-3.0, usado como contraste medido y descartado con
  causa. No se redistribuyen pesos.
Ver los resultados: [`../resultados/README.md`](../resultados/README.md)
```

- [ ] **Step 3: Guardián** (mismo criterio).

---

### Task 9: `repositorios/README.md` — fichas y tabla de versiones citadas

**Files:**
- Create: `$REPO/repositorios/README.md`

- [ ] **Step 1: Tomar la foto actual de cada repo** (para la columna "rama de trabajo" y el commit provisional):

```bash
cd /home/simonll4/projects && for r in e-ovrt_datasets e-ovrt_media-plane e-ovrt_control-plane e-ovrt_experimental-setup e-ovrt_alert-distribution; do (cd $r && echo "$r | $(git branch --show-current) | $(git log -1 --format='%h | %cs')"); done
```

- [ ] **Step 2: Escribir el documento**:

```markdown
# Los cinco repositorios de código
Son repos independientes que se clonan **como hermanos en una misma carpeta**: varias
configuraciones usan rutas relativas entre ellos (`../e-ovrt_datasets/...`).

## Fichas
### e-ovrt_media-plane — plano de medios
- https://github.com/simonll4/e-ovrt_media-plane
- Servicio de inferencia open-vocabulary (FastAPI, HTTP/WS). Ingesta de carpeta de imágenes,
  video, RTSP y OAK-D; el modelo se carga una vez (`EOVRT_MODEL_REF`); una corrida activa a la
  vez; publica `media.detection.v1` por archivo o por bus.
- Correr: `python3.12 -m venv .venv && source .venv/bin/activate && pip install -e ".[gpu,dev]"` ·
  `make download-models` · `EOVRT_MODEL_REF=mock make serve` (`:8080`).
- Tests: `make test`.
### e-ovrt_control-plane — plano de control
- https://github.com/Pandulc/e-ovrt_control-plane
- Motor de patrones CR-01 / CR-02 sobre `media.detection.v1`: identidad por sujeto,
  estrategias de evidencia (E-IND, E-DIR, fusiones), persistencia temporal, alertas
  confirmadas al bus `:5558`; evaluador de alertas contra referencia temporal.
- Correr: `python3.11 -m venv .venv && pip install -e ".[dev]"` · `eovrt-control serve --port 8081`;
  `eovrt-control replay --config <cfg>` para el camino offline.
- Tests: `python3 -m pytest tests/ -q --ignore=tests/labs`.
### e-ovrt_alert-distribution — distribución de alertas
- https://github.com/simonll4/e-ovrt_alert-distribution
- Consumidor de alertas confirmadas; política de notificación; entrega MQTT QoS 1 con
  registro idempotente. Servicio HTTP `:8082` (`eovrt-distribute serve`) y CLI `replay`/`live`.
  Python 3.11.
- Tests: `.venv/bin/python -m pytest -q`.
### e-ovrt_experimental-setup — experimentos, resultados y consola
- https://github.com/simonll4/e-ovrt_experimental-setup
- `prompts/` (prompt sets, incluido el congelado para el rodaje y el bench), `experiments/`
  (manifiestos), **`results/` (los cuatro índices de cifras del proyecto)**, `webconsole/`
  (React + FastAPI BFF, `:8090`), `infra/platform/` (compose integral de 13 servicios),
  `finetuning/` (recetas Slurm/Apptainer y manifiestos de la jornada de fine-tuning),
  `defensa/` (renderer de videos).
- Correr la consola: `cd webconsole && make install && make serve` (requiere el plano de
  medios arriba).
- Tests: `.venv/bin/python -m pytest tests/` · `finetuning/tests/` ·
  `cd webconsole/backend && ../../.venv/bin/python -m pytest` · `cd webconsole/frontend && npm test`.
### e-ovrt_datasets — datos
- https://github.com/Pandulc/e-ovrt_datasets
- Descarga, validación y conversión (COCO/YOLO/ODVG) a la vista canónica `canonical_v2`
  (`person`, `helmet`, `vest`, `bare_head`); construcción y verificación byte a byte del
  banco `bench_v3`; registro de licencias y procedencia. Las imágenes crudas no se versionan.
- Tests: `python3 -m pytest datasets/tests/ -q`.

## Versiones citadas en el informe
Se completa al congelar (tag `informe-2026` en cada repo).
| Repositorio | Rama de trabajo | Tag | Commit | Fecha |
|---|---|---|---|---|
| e-ovrt_media-plane | `feature/inference-service` | `informe-2026` | *(al congelar)* | |
| e-ovrt_control-plane | `feature/control-service` | `informe-2026` | | |
| e-ovrt_alert-distribution | `main` | `informe-2026` | | |
| e-ovrt_experimental-setup | `feature/webconsole-consola-tesis` | `informe-2026` | | |
| e-ovrt_datasets | `feature/datasets-v2-setup` | `informe-2026` | | |
```

- [ ] **Step 3: Guardián** (mismo criterio; este archivo no tiene figuras ni cifras).

---

### Task 10: `resultados/README.md` — la respuesta con cifras enlazadas

**Files:**
- Create: `$REPO/resultados/README.md`

**Interfaces:**
- Consumes: figuras B y F (`../evidencia/figuras/fig-b-calidad-vs-densidad.png`, `fig-f-frontera-juzgabilidad.png`, Tarea 11). Regla (c) del guardián: **toda fila con cifra lleva enlace** a `$RES…` o a `…/blob/HEAD/finetuning/…`.

- [ ] **Step 1: Verificar las cifras contra los índices antes de escribirlas** (interno, no se cita):

```bash
cd /home/simonll4/projects/docs && python3 operacion/datos/96-verificar-indices.py 2>&1 | tail -2
cd /home/simonll4/projects/e-ovrt_experimental-setup && git ls-files finetuning/manifests | grep -E 'go_no_go|promotion' ; ls finetuning/manifests | grep -E '^t1_.*(go_no_go|promotion|verdict)'
```

Esperado: "Todo verificado". Anotar qué manifiestos de fine-tuning están **trackeados**: los enlaces de la fila de fine-tuning sólo pueden apuntar a archivos trackeados (`t2_go_no_go_1167982.json` como mínimo). Si existe un manifiesto de veredicto de T1 trackeado, enlazarlo; si no, la fila de T1 cita "NO-GO pre-registrado" enlazando al `finetuning/README.md`.

- [ ] **Step 2: Escribir el documento**. Estructura por pregunta de medición; cada fila de cifras con su enlace (URL completa, no abreviada). Usar exactamente estas cifras:

```markdown
# Resultados
Cada cifra enlaza a la página de resultados de donde sale, con su `n` y su material. Los
números son el dato de una combinación bajo un protocolo, no un aprobado/fallado.

## La respuesta en cuatro números
| # | Pregunta | Dato | Fuente |
|---|---|---|---|
| 1 | Qué ve el detector sin entrenar | `gdino-tiny-560`: mAP50 **0,551** sobre 6.477 imágenes de 3 fuentes; `person`/`helmet` sólidas, `vest` débil, `bare_head` sólo en el especialista | [bench_imagenes](https://github.com/simonll4/e-ovrt_experimental-setup/blob/HEAD/results/bench_imagenes/index.md) |
| 2 | Cómo expresar la condición | E-IND supera a E-DIR en los dos niveles; a Nivel B la precisión de E-DIR **0,146** (< 0,5) la descarta como núcleo | [bench_nivel_a](…/results/bench_nivel_a/index.md) · [clip_bench](…/results/clip_bench/index.md) |
| 3 | Qué agrega la plataforma | Con las mismas detecciones bit a bit, escena → sujeto lleva el F1 de alertas de **0,789 a 0,930** | [clip_bench](…/results/clip_bench/index.md) |
| 4 | Qué sobrevive al tiempo real | La ganancia de la identidad **excluye el cero en las cuatro densidades** medidas (30 → 1,15 fps) | [realtime](…/results/realtime/index.md) |

## 1. Selección de modelo (`bench_v3`, 6.477 imágenes)
| Modelo | mAP50 `bench_v3` | mAP50 núcleo `bench_obra` (147) | recall CR-01 (n=5.313) | latencia | Fuente |
| `gdino-tiny-560` (campeón) | **0,551** | **0,503** | 0,308 | **129 ms** | link |
| `gdino-base-560` (especialista CR-02/`bare_head`) | 0,525 | 0,474 | **0,599** | 146 ms | link |
- Por estrato, campeón: `shel5k` (n=5.000) person 0,770 · helmet 0,707 · bare_head 0,133;
  `chv` (n=1.330) vest 0,553. La asimetría por clase es estructural. [fila con link]
- Resolución 560 vs 800: −24 % de latencia con igual o mejor mAP. [link]

## 2. Formulación: E-IND vs E-DIR vs E-HYB
| Nivel | Combinación | F1 | Fuente |
| A, CR-01 `bench_obra` (n=28) | E-IND | 0,408 | bench_nivel_a |
| A, CR-01 `shel5k` (n=2.487) | E-IND | 0,546 | bench_nivel_a |
| A, CR-02 `bench_obra` (n=82) | E-IND | 0,479 | bench_nivel_a |
| B, clips (34 evaluables) | T1 E-IND escena | **0,789** (recall 0,824 · precisión 0,757) | clip_bench |
| B, clips | D1 E-DIR escena | 0,160 (precisión 0,146 → veto pre-registrado) | clip_bench |
| B, clips | H1 E-HYB-or escena | 0,296 (la predicción pre-registrada de mejora se refutó) | clip_bench |

## 3. Granularidad: escena vs sujeto (la palanca que más agrega)
| Campaña | Granularidad | Recall | Precisión | F1 | FP en 4 negativos | Fuente |
| T1 | escena | 0,824 | 0,757 | 0,789 | 0 | clip_bench |
| **G1** | **sujeto** | **0,971** | **0,892** | **0,930** | 0 | clip_bench |
- Única variable: la granularidad (SDR y TTFD idénticos). Δ F1 **+0,141**, IC [+0,032; +0,258]. [link]
- La histéresis rescata percepción intermitente (CR-02 llega a recall 1,000 con SDR 0,281) pero es palanca de doble filo. [link]

## 4. El costo del tiempo real (densidad de evidencia)
![Calidad vs densidad](../evidencia/figuras/fig-b-calidad-vs-densidad.png)
| fps evaluados | Escena F1 | Sujeto F1 | Fuente |
| 30,00 (referencia) | 0,789 (T1) | 0,930 (G1) | clip_bench |
| 4,29 (techo live) | 0,794 (R1) | 0,866 (R2) | clip_bench |
| 2,00 (lo que corrió el rodaje) | 0,738 (R3) | 0,875 (R4) | clip_bench |
| 1,15 (peor caso) | 0,646 (R5) | 0,742 (R6) | clip_bench |
- En vivo: `bus_dropped_events = 0` en las 6 corridas del rodaje; fps del plano de medios
  3,75 → 4,42 (+18 %) con la palanca de pre-flight; G2A 630–890 ms con GDINO en vivo;
  `capture_to_host` 202–217 ms. [filas con link a realtime]

## 5. Obra real no guionada (13 clips de internet)
![Frontera de juzgabilidad](../evidencia/figuras/fig-f-frontera-juzgabilidad.png)
| | Escena | Sujeto | Fuente |
| F1 (2 episodios evaluables) | 0,333 | 0,190 | clip_bench |
| FP sobre 11 negativos | 26 | 323 | clip_bench |
| FAR/hora (0,1027 h de soak) | 29,2 | 1.850,8 | clip_bench |
- Con n=2 no hay ranking posible entre granularidades; lo robusto es la asimetría de FP (12×).
  La revisión ciega del GT tumbó 5 de 7 declaraciones de episodio: la calidad del GT es un
  resultado. La figura F muestra la frontera de juzgabilidad (escala × iluminación × oclusión).

## 6. Distribución de alertas
| Tramo | p95 | n | Fuente |
| bus de alertas → PUBACK MQTT QoS 1 | **64,534 ms** | 460 | [t_alert_notification](…/results/realtime/t_alert_notification/README.md) |
| régimen sostenido (2.ª+ entrega por corrida) | 102,025 ms | 104 | idem |
| primeras entregas | 49,869 ms | 356 | idem |
- La distribución no es el cuello: un orden de magnitud por debajo del G2A en vivo y dos por
  debajo de la persistencia deliberada del patrón (4–7 s).

## 7. Fine-tuning acotado (YOLOE-26s, jornada con protocolo pre-registrado)
| Brazo | Veredicto | Dato | Fuente |
| T1 | NO-GO pre-registrado | [según manifiesto trackeado o "gates no alcanzados"] | finetuning |
| T2 | NO-GO pre-registrado | ganancia `bare_head` 0 → 0,0909 (sólo `shel5k`) **pasa**; retención in-domain **falla** (person −49,7 %); open-vocabulary **falla** (COCO −71,3 %) | [t2_go_no_go](https://github.com/simonll4/e-ovrt_experimental-setup/blob/HEAD/finetuning/manifests/t2_go_no_go_1167982.json) |
- Lectura: el fallo no es de capacidad sino estructural (2.946 imágenes frente a 10,35 M
  parámetros). T1 gana por recall CR-01 y T2 por AP: no es una métrica única. El checkpoint
  no se adoptó.

## Limitaciones declaradas (L1–L8)
[Una fila por limitación, texto de una línea, con enlace a results/index.md § Limitaciones:]
L1 FAR/hora como conteo crudo, no sostiene cota (0,27 h de negativo; harían falta 3 h) ·
L2 sin doble anotación ni kappa (decisión declarada) · L3 bordes del GT adjudicados en 6 clips
por oclusión · L4 medición en obra real acotada: caracteriza dónde el sistema deja de ser
evaluable, no lo valida sobre obra real · L5 escenarios desbalanceados ⇒ reportar por
escenario y estrato · L6 tracker sin métricas MOT; en multitud real fragmenta identidades
(182 con FP frente a 127 personas) · L7 licencia parcial de `chv` (20,5 % del bench) ·
L8 CR-02 a Nivel A no cerrada (un estrato, IC solapados).
```

Reemplazar cada `…` y `link`/`idem`/`clip_bench`/`bench_nivel_a`/`finetuning` por la URL completa correspondiente (`https://github.com/simonll4/e-ovrt_experimental-setup/blob/HEAD/results/<índice>/index.md`, o `…/finetuning/README.md`).

- [ ] **Step 3: Guardián — acá la regla (c) tiene que dar cero**

```bash
cd /home/simonll4/projects/e-ovrt-vdp && python3 herramientas/verificar.py | grep -E '^resultados/' ; echo "---"; python3 herramientas/verificar.py | grep -c '(c)'
```

Esperado: ninguna línea `(a)` ni `(c)` en `resultados/`; el conteo de `(c)` es `0`. Las únicas violaciones tolerables son `(d)` por las figuras B y F hasta la Tarea 11.

---

### Task 11: `evidencia/figuras/` — las seis figuras, generadores y README

**Files:**
- Create: `$REPO/evidencia/figuras/{fig-a-vista-de-procesos,fig-b-calidad-vs-densidad,fig-e-maquina-de-estados,fig-f-frontera-juzgabilidad}.{png,svg}`, `fig-c-alerta-confirmada.png`, `fig-c-alerta-confirmada-completa.png`
- Create: `$REPO/evidencia/figuras/scripts/{estilo,fig_a_vista_de_procesos,fig_b_calidad_vs_densidad,fig_e_maquina_de_estados,fig_f_frontera_juzgabilidad}.py`
- Create: `$REPO/evidencia/figuras/README.md`

- [ ] **Step 1: Copiar figuras y generadores**

```bash
SRC=/home/simonll4/projects/docs/informe/figuras; DST=/home/simonll4/projects/e-ovrt-vdp/evidencia/figuras
cp $SRC/fig-*.png $SRC/fig-*.svg $DST/
cp $SRC/scripts/*.py $DST/scripts/
ls -la $DST $DST/scripts && du -sh $DST
```

Esperado: 10 imágenes + 5 scripts; total ≈ 3,5 MB.

- [ ] **Step 2: Limpiar referencias internas en los generadores**

```bash
cd /home/simonll4/projects/e-ovrt-vdp/evidencia/figuras/scripts && grep -n -E 'operacion/|nucleo/|ADR-|\bF-[0-9]|\bD-[0-9]|/home/|\.\./\.\./' *.py
```

Por cada línea encontrada: si es un comentario o docstring, reescribirlo sin la referencia (p. ej. "cifras tomadas de results/clip_bench/{t1,g1,r1…r6}/metrics.json"); si es una **ruta de lectura de datos** (`../../../../e-ovrt_experimental-setup/results/...`), reemplazarla por una variable `RESULTS = Path(os.environ.get("EOVRT_RESULTS", "../../../../e-ovrt_experimental-setup/results"))` y documentar en el README que se corre con el repo hermano clonado al lado. Volver a correr el `grep`: sin salida. (El guardián no revisa `.py`, pero la regla 1 aplica igual.)

- [ ] **Step 3: Escribir `README.md` de figuras**

```markdown
# Figuras
Las figuras del informe, en PNG a 300 dpi (ancho de diseño 16 cm) y SVG. Cuatro se generan
desde los datos publicados con los scripts de `scripts/`; la C es un fotograma.

| Figura | Archivo | Qué muestra | De dónde sale |
|---|---|---|---|
| A | `fig-a-vista-de-procesos` | los procesos de la plataforma y sus interfaces | especificación de la arquitectura |
| B | `fig-b-calidad-vs-densidad` | F1 de alertas vs densidad de evidencia, escena y sujeto | `results/clip_bench/{t1,g1,r1…r6}/metrics.json`; el script falla si la cifra no coincide |
| C | `fig-c-alerta-confirmada` (+ `-completa`) | fotograma con la alerta confirmada dibujada | render del video de defensa del clip `a_p1_c04`, t = 8,5 s |
| E | `fig-e-maquina-de-estados` | la máquina de cinco estados del patrón | contrato de eventos de patrón del plano de control |
| F | `fig-f-frontera-juzgabilidad` | asociación de chaleco por banda de altura (A) y Nivel A por clip (B) | campañas del lote de internet |

## Tres advertencias de lectura
1. **La distribución está en línea, continua** con la cadena; no es un proceso por lotes.
2. **El orden de arranque es inverso al flujo de datos**: distribución → control → medios.
3. **La máquina de estados tiene cinco estados y reabre a candidato**, no vuelve a inactivo.

## Regenerar
```bash
cd evidencia/figuras/scripts
python3 fig_a_vista_de_procesos.py && python3 fig_b_calidad_vs_densidad.py && python3 fig_e_maquina_de_estados.py && python3 fig_f_frontera_juzgabilidad.py
```
Requiere `matplotlib` y, para la B y la F, el repo `e-ovrt_experimental-setup` clonado como
hermano (o `EOVRT_RESULTS` apuntando a su carpeta `results/`). `estilo.py` concentra paleta y
tipografía: tocarlo cambia las cuatro a la vez.
```

- [ ] **Step 4: Guardián completo** — ahora las (d) de figuras desaparecen:

```bash
cd /home/simonll4/projects/e-ovrt-vdp && python3 herramientas/verificar.py
```

Esperado: sólo violaciones (b) por `informe/README.md`, `evidencia/consola/README.md`, `evidencia/material-de-video.md`, `evidencia/verificacion.md` (tareas 12–15). Ninguna (a), (c) ni (d).

---

### Task 12: `evidencia/material-de-video.md` — procedencia del banco de clips

**Files:**
- Create: `$REPO/evidencia/material-de-video.md`

- [ ] **Step 1: Extraer la tabla de los 13 clips de internet desde los `clip.yaml`** (la lista vigente del estrato B es: `v01_c01 v01_c02 v02_c01 v03_c01 v03_c02 v04_c01 v04_c02 v04_c03 v05_c01 v06_c01 v07_c01 v09_c01 v10_c01`; `v08_c01` está excluido del banco con causa):

```bash
cd /home/simonll4/projects/e-ovrt_datasets/datasets-videos && python3 - <<'EOF'
import yaml
ids = "v01_c01 v01_c02 v02_c01 v03_c01 v03_c02 v04_c01 v04_c02 v04_c03 v05_c01 v06_c01 v07_c01 v09_c01 v10_c01".split()
print("| Clip | Escenario | Fuente | Video de origen | Términos |")
print("|---|---|---|---|---|")
for i in ids:
    d = yaml.safe_load(open(f"{i}.clip.yaml"))
    lic = d.get("license", {}) or {}
    print(f"| `{i}` | {d.get('scenario','')} | {lic.get('source','')} | {lic.get('video_url','')} | {lic.get('terms','')} |")
EOF
```

Si `yaml` no está en el `python3` del sistema, usar `/home/simonll4/projects/e-ovrt_experimental-setup/.venv/bin/python`. Revisar que las 13 filas tengan URL; si alguna está vacía, dejar la celda como `*(sin URL registrada)*` y agregar una fila a `PUBLICAR.md` para completarla.

- [ ] **Step 2: Escribir el documento**

```markdown
# Material de video: qué se usó y qué se publica
**No se publica ningún video en este repositorio.** El material de obra propia no se
redistribuye; el de internet se referencia a su origen.

## Rodaje propio (34 clips, no publicados)
- Obra real, bloque guionado con hardware real (cámara OAK-D Pro PoE y RTSP), grabado y
  recortado desde la consola. Referencia temporal humana anotada en CVAT en dos pasadas;
  34 clips, 34 episodios evaluables. Sus métricas están en `results/clip_bench/`
  (enlace). Los fotogramas que aparecen en las figuras (C) provienen de este rodaje.

## Lote de internet (13 clips, referenciados por URL)
- Obra real **no guionada**, diurna en su mayoría (un clip nocturno), un clip largo de
  "soak" (0,1027 h) para el control de falsos positivos. Cada clip se recortó de un video
  público; acá va su origen. Los términos de uso son los del canal; no se redistribuye el
  material.
[TABLA del Step 1]
- `v08_c01` se relevó pero quedó **excluido del banco con causa** y no se publica.

## Cómo se anotó la referencia
- Nivel B: episodios (inicio/fin) de CR-01 y CR-02 por clip; bordes adjudicados por oclusión
  en 6 clips (L3); sin doble anotación (L2). Una revisión ciega posterior del lote de internet
  cambió 5 de 7 declaraciones de episodio: donde el estado no era observable, la anotación
  pasó a "desconocido". Ese resultado está en `results/clip_bench/` (enlace).
```

- [ ] **Step 3: Guardián** (mismo criterio; ninguna (a)).

---

### Task 13: `evidencia/consola/` — capturas de la webconsole

**Files:**
- Create: `$REPO/evidencia/consola/{01-plataforma,02-componer-corrida,03-corridas,04-detalle-de-corrida,05-experimentos,06-detalle-de-experimento,07-comparar,08-prompt-sets}.png`
- Create: `$REPO/evidencia/consola/README.md`
- Delete: `$REPO/evidencia/consola/.gitkeep`

**Interfaces:**
- Consumes: los cuatro servicios levantados en local con el modelo mock (sin GPU). Todo lo que se arranca acá **se apaga al final** de la tarea. Logs y PNG intermedios en el scratchpad de la sesión (no en `/tmp`).

- [ ] **Step 1: Levantar los servicios en background** (cada uno en su repo, con su venv):

```bash
S=$CLAUDE_SCRATCHPAD_DIR   # usar la ruta del scratchpad de la sesión; crear $S/consola
mkdir -p $S/consola
cd /home/simonll4/projects/e-ovrt_media-plane && EOVRT_MODEL_REF=mock nohup .venv/bin/uvicorn --factory eovrt_media.service.app:create_app --host 127.0.0.1 --port 8080 > $S/consola/media.log 2>&1 &
cd /home/simonll4/projects/e-ovrt_control-plane && nohup .venv/bin/eovrt-control serve --port 8081 > $S/consola/control.log 2>&1 &
cd /home/simonll4/projects/e-ovrt_alert-distribution && nohup .venv/bin/eovrt-distribute serve --host 127.0.0.1 --port 8082 > $S/consola/dist.log 2>&1 &
cd /home/simonll4/projects/e-ovrt_experimental-setup/webconsole && nohup make serve > $S/consola/console.log 2>&1 &
sleep 40; for p in 8080 8081 8082; do curl -sf http://127.0.0.1:$p/readyz >/dev/null && echo "$p ready" || echo "$p NOT ready"; done; curl -sf http://127.0.0.1:8090/api/health && echo && curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1:8090/platform
```

Esperado: `8080 ready`, `8081 ready`, `8082 ready`, el JSON de health de la consola y `200` para `/platform`. Si `/platform` da 404, la SPA no hace fallback por ruta: capturar entonces `http://127.0.0.1:8090/#/platform` o navegar desde `/` (probar ambos y usar el que renderice la página). Si la consola tarda (build de Vite), esperar 60 s más y reintentar.

- [ ] **Step 2: Elegir un experimento y una corrida existentes para las páginas de detalle**

```bash
curl -s http://127.0.0.1:8090/api/experiments | python3 -c 'import json,sys; d=json.load(sys.stdin); items=d if isinstance(d,list) else d.get("items",d.get("experiments",[])); print(len(items)); print(items[0].get("id") if items else "NONE")'
curl -s http://127.0.0.1:8080/api/runs | python3 -c 'import json,sys; d=json.load(sys.stdin); items=d if isinstance(d,list) else d.get("items",d.get("runs",[])); print(len(items)); print(items[0].get("id") if items else "NONE")'
```

Anotar `EXP_ID` y `RUN_ID`. Si alguna lista está vacía, capturar la página de listado igual (muestra el estado vacío real) y omitir la de detalle correspondiente, documentándolo en el README.

- [ ] **Step 3: Capturar con chromium headless** (1440×900, esperar 6 s de render por página):

```bash
CHROME=/home/simonll4/.cache/ms-playwright/chromium-1228/chrome-linux64/chrome
OUT=/home/simonll4/projects/e-ovrt-vdp/evidencia/consola
shot() { "$CHROME" --headless=new --disable-gpu --no-sandbox --hide-scrollbars --window-size=1440,900 --virtual-time-budget=6000 --screenshot="$OUT/$1.png" "http://127.0.0.1:8090$2" 2>/dev/null && echo "ok $1"; }
shot 01-plataforma /platform
shot 02-componer-corrida /compose
shot 03-corridas /
shot 04-detalle-de-corrida "/runs/$RUN_ID"
shot 05-experimentos /experiments
shot 06-detalle-de-experimento "/experiments/$EXP_ID"
shot 07-comparar /compare
shot 08-prompt-sets /prompts
ls -la $OUT/*.png && du -sh $OUT
```

Esperado: 8 PNG (o 6–7 si no había detalle), cada uno < 500 KB. Abrir 2 o 3 con el Read tool para confirmar que no son pantallas en blanco ni de error. Si un PNG salió en blanco, repetir esa captura con `--virtual-time-budget=15000`.

- [ ] **Step 4: Apagar todo**

```bash
pkill -f 'eovrt_media.service.app' ; pkill -f 'eovrt-control serve' ; pkill -f 'eovrt-distribute serve' ; pkill -f 'eovrt_webconsole.app'
sleep 2; for p in 8080 8081 8082 8090; do curl -s -o /dev/null http://127.0.0.1:$p/ && echo "$p STILL UP" || echo "$p down"; done
rm /home/simonll4/projects/e-ovrt-vdp/evidencia/consola/.gitkeep
```

Esperado: los cuatro `down`.

- [ ] **Step 5: `README.md` de la carpeta**

```markdown
# La consola web
Capturas de la consola (`e-ovrt_experimental-setup/webconsole`, React + FastAPI) tomadas con
la plataforma completa levantada en local con el modelo `mock` (sin GPU). Los datos que se
ven son las corridas y experimentos reales del repositorio.

| Captura | Pantalla | Qué muestra |
|---|---|---|
| `01-plataforma.png` | Plataforma | estado de los tres servicios y de la flota de instancias del plano de medios; desde acá se encienden los modelos |
| `02-componer-corrida.png` | Componer | armado de una corrida: fuente, modelo, prompt set, control, distribución |
| `03-corridas.png` | Corridas | historial de corridas del plano de medios |
| `04-detalle-de-corrida.png` | Detalle de corrida | métricas, artefactos y línea de tiempo de una corrida |
| `05-experimentos.png` | Experimentos | manifiestos de experimento por referencia y su estado |
| `06-detalle-de-experimento.png` | Detalle de experimento | los tres planos de una corrida de experimento: medios, control, distribución |
| `07-comparar.png` | Comparar | comparación de corridas/campañas |
| `08-prompt-sets.png` | Prompt sets | ciclo de vida de los prompt sets: alta, edición, congelamiento |
```

Ajustar la tabla a lo capturado realmente (quitar filas si se omitió un detalle).

- [ ] **Step 6: Guardián** (ninguna (a); las imágenes no se referencian desde `.md` con `![…]`, así que (d) no aplica; sólo quedan (b) de tareas 14–15).

---

### Task 14: `evidencia/verificacion.md` — suites corridas hoy

**Files:**
- Create: `$REPO/evidencia/verificacion.md`

- [ ] **Step 1: Correr las suites, una por una, guardando la última línea de cada una** (salida completa al scratchpad):

```bash
S=$CLAUDE_SCRATCHPAD_DIR/suites; mkdir -p $S; cd /home/simonll4/projects
( cd e-ovrt_datasets && python3 -m pytest datasets/tests/ -q > $S/datasets.log 2>&1 || ../e-ovrt_experimental-setup/.venv/bin/python -m pytest datasets/tests/ -q > $S/datasets.log 2>&1 ); tail -1 $S/datasets.log
( cd e-ovrt_media-plane && .venv/bin/python -m pytest -q > $S/media.log 2>&1 ); tail -1 $S/media.log
( cd e-ovrt_control-plane && .venv/bin/python -m pytest tests/ -q --ignore=tests/labs > $S/control.log 2>&1 ); tail -1 $S/control.log
( cd e-ovrt_alert-distribution && .venv/bin/python -m pytest -q > $S/dist.log 2>&1 ); tail -1 $S/dist.log
( cd e-ovrt_experimental-setup && .venv/bin/python -m pytest tests/ -q > $S/exp.log 2>&1 ); tail -1 $S/exp.log
( cd e-ovrt_experimental-setup && .venv/bin/python -m pytest finetuning/tests/ -q > $S/ft.log 2>&1 ); tail -1 $S/ft.log
( cd e-ovrt_experimental-setup/webconsole/backend && ../../.venv/bin/python -m pytest -q > $S/bff.log 2>&1 ); tail -1 $S/bff.log
( cd e-ovrt_experimental-setup/webconsole/frontend && npm test > $S/front.log 2>&1 ); grep -E 'Tests|passed|failed' $S/front.log | tail -2
```

Referencia histórica (no citar como actual): plataforma 2.203 tests al 2026-08-15, BFF 643, experimental-setup 88, finetuning 46. Si una suite falla, **se reporta tal cual** con la línea de fallo; no se maquilla ni se omite.

- [ ] **Step 2: Escribir el documento con lo que salió**

```markdown
# Verificación: las suites de los cinco repos
Corridas el **2026-MM-DD** en el workspace de desarrollo, con los comandos exactos de abajo.
No son cifras copiadas de una foto anterior.

| Repo / módulo | Comando | Resultado |
|---|---|---|
| e-ovrt_datasets | `python3 -m pytest datasets/tests/ -q` | *(última línea)* |
| e-ovrt_media-plane | `.venv/bin/python -m pytest -q` | |
| e-ovrt_control-plane | `.venv/bin/python -m pytest tests/ -q --ignore=tests/labs` | |
| e-ovrt_alert-distribution | `.venv/bin/python -m pytest -q` (la integración MQTT real queda deseleccionada por defecto) | |
| e-ovrt_experimental-setup — runner | `.venv/bin/python -m pytest tests/ -q` | |
| e-ovrt_experimental-setup — fine-tuning | `.venv/bin/python -m pytest finetuning/tests/ -q` | |
| webconsole — backend (BFF) | `cd webconsole/backend && ../../.venv/bin/python -m pytest -q` | |
| webconsole — frontend | `cd webconsole/frontend && npm test` | |
| **Total** | | **N tests** |

Además, este repo se verifica con `python3 herramientas/verificar.py` (reglas de contenido) y
`python -m pytest herramientas/tests -q` (38 tests del guardián).
```

- [ ] **Step 3: Guardián** (ninguna (a)).

---

### Task 15: `informe/README.md`

**Files:**
- Create: `$REPO/informe/README.md`
- Delete: `$REPO/informe/.gitkeep`

- [ ] **Step 1: Escribir el documento** (el PDF lo aporta el autor cuando cierre el maestro; hasta entonces el README lo dice):

```markdown
# El informe
**Archivo:** `E-OVRT-VDP-informe.pdf` — *(se incorpora con la versión final; hoy el informe
está en integración de sus últimas secciones)*.

Título: *Plataforma experimental de detección open-vocabulary en video en tiempo real para
monitoreo asistivo de riesgos en construcción*. Proyecto Integrador, Ingeniería en
Informática, IUA Córdoba — Facultad de Ingeniería, 2026. Autores: Matías Lautaro Carrizo,
Gabriel Agustín Guillaumet, Simon Llamosas. Tutor: Mariano García Mattio.

## Estructura
| § | Capítulo |
|---|---|
| 12 | Introducción |
| 13 | Objetivo del proyecto |
| 14 | Plan de trabajo |
| 15 | Estado del arte |
| 16 | Marco teórico |
| 17 | Desarrollo del producto — 17.1 Consolidación metodológica del protocolo experimental · 17.3 Diseño arquitectónico · 17.4 Implementación del prototipo experimental · 17.5 Evaluación y validación del prototipo · 17.6 Documentación y cierre |
| 18 | Cierre del proyecto |
| 19 | Anexos |

Este repositorio es el complemento del informe: lo que el informe describe, acá se ve
(figuras, capturas, resultados con su fuente) y se puede seguir hasta el código.
```

Al llegar el PDF (PUBLICAR.md paso 7): reemplazar la primera línea por la versión y fecha, y completar la tabla con los títulos exactos de todas las secciones del PDF.

- [ ] **Step 2: Guardián completo — tiene que dar cero**

```bash
cd /home/simonll4/projects/e-ovrt-vdp && rm -f informe/.gitkeep && python3 herramientas/verificar.py && /home/simonll4/projects/e-ovrt_experimental-setup/.venv/bin/python -m pytest herramientas/tests -q | tail -1
```

Esperado: `OK: 0 violaciones` y `38 passed`.

---

### Task 16: Registrar el nuevo hermano en el `CLAUDE.md` del workspace y cierre

**Files:**
- Modify: `/home/simonll4/projects/CLAUDE.md` — sección "Workspace layout", después del ítem de `docs/`.

- [ ] **Step 1: Agregar el ítem**

```markdown
- `e-ovrt-vdp/` — el **repositorio público de documentación** (vitrina de la tesis; la única
  referencia externa que cita el informe). Markdown puro; `docs/` NO se publica ni se
  referencia desde ahí. Antes de tocar cualquier `.md` suyo, leer su `CONTRIBUTING.md`;
  después, correr `python3 herramientas/verificar.py` (cero violaciones). Remote y publicación
  los maneja el usuario (`PUBLICAR.md`). Diseño: `docs/superpowers/specs/2026-08-25-repo-e-ovrt-vdp-design.md`.
```

- [ ] **Step 2: Foto final del repo para el usuario**

```bash
cd /home/simonll4/projects/e-ovrt-vdp && find . -path ./.git -prune -o -type f -print | sort && du -sh --exclude=.git . && git status --short | wc -l && python3 herramientas/verificar.py
```

Esperado: ~40 archivos (5 raíz + 1 informe + 5 plataforma + 1 resultados + 1 repositorios + 16 figuras/scripts + 9 consola + 2 evidencia + 4 herramientas); tamaño < 8 MB; `OK: 0 violaciones`. **Sin commits**: reportar al usuario que el repo está listo para que lo commitee y siga `PUBLICAR.md`.

---

## Self-review (hecho al escribir el plan)

- **Cobertura de la spec:** §2 identidad → T1 (LICENSE, CITATION, PUBLICAR con descripción/topics); §3 reglas → T1 (CONTRIBUTING) + T2–T4 (guardián); §4 estructura → T1 + mapa de archivos; §5 contenido de las 13 piezas → T5–T15 (README, 01–05, resultados, repositorios, figuras/README, consola/README, material-de-video, verificacion, informe/README); §6 evidencia → T11 (figuras), T13 (capturas), T12 (videos = ninguno, por URL), T15 (informe); §7 guardián con las 4 reglas, marcador y `--json` → T2–T4; §8 versiones/citación → T9 (tabla) + T1 (PUBLICAR pasos 8–9, CITATION); §9 orden → tareas en ese orden; §10 checklist → T1; §11 fuera de alcance → sin tareas de commit/push/merge/docx/V2; §12 criterios → T15/T16 (guardián en cero), T14 (suites con fecha), T10 (cifras con enlace).
- **Placeholders:** los corchetes `[…]` en los outlines de texto indican prosa a redactar con el contenido indicado en la misma línea; las cifras y URLs están dadas. Las celdas "*(al congelar)*" de la tabla de versiones y "*(se incorpora con la versión final)*" del informe son estados reales declarados, no huecos del plan.
- **Consistencia de nombres:** `archivos_md`, `revisar_patrones`, `revisar_enlaces`, `revisar_imagenes`, `revisar_cifras`, `revisar_todo`, `main`, `PERMITIR`, `EXCLUIR`, `ENLACE_FUENTE`, `ARCHIVO_CIFRAS` se usan igual en T2–T4 y en los tests; los nombres de archivo de figuras y capturas coinciden entre T5/T6/T7/T10/T11/T13.
