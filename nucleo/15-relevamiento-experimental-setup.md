# 15 — Relevamiento: `e-ovrt_experimental-setup`

- **Fecha de relevamiento:** 2026-08-10
- **Método:** relevado **contra git y código**. Los comandos de §2 y la suite de §7 se
  ejecutaron en esta máquina.
- **Regla de este documento:** **no publica ninguna cifra de resultado.** Este repo
  *contiene* los índices de resultados (§5.4); las cifras se citan desde ahí, nunca desde
  acá.

---

## 1. Qué es, y qué no es

**El centro operativo del proyecto, y no es un plano.** Desde acá se dispara todo lo demás.
Reúne cuatro cosas:

1. Los **catálogos de experimento** — conjuntos de prompts y manifiestos de corrida.
2. La **webconsole** — React + BFF FastAPI, la superficie de gestión primaria (ADR-009).
3. Los **resultados citables** — los cuatro índices de `results/`, que son **la fuente
   canónica de toda cifra del proyecto**.
4. El material de la defensa y el despliegue dockerizado de dos nodos.

**Es cliente HTTP de los dos planos, y nunca consume el bus ZeroMQ directamente.** Esa es
la costura que permite que los planos vivan en máquinas distintas sin que la consola se
entere.

**Qué NO hace:** no detecta, no evalúa patrones, no distribuye alertas. Orquesta,
configura, recolecta y muestra.

## 2. Cómo se ejecuta

```bash
cd e-ovrt_experimental-setup/webconsole

# BFF (backend)
cd backend && python3.11 -m venv .venv && source .venv/bin/activate && pip install -e ".[dev]"
.venv/bin/python -m pytest -q          # 586 passed (2026-08-10)

# Frontend
cd ../frontend && npm install && npm run dev    # vite
npm test                                        # vitest run
```

Los dos planos tienen que estar levantados (`:8080` media, `:8081` control) para que la
consola haga algo útil.

## 3. Estructura

```
e-ovrt_experimental-setup/
├── prompts/          # conjuntos de prompts — los catálogos de vocabulario
├── experiments/      # manifiestos de corrida, por referencia
├── results/          # LOS ÍNDICES CITABLES (§5.4)
├── webconsole/
│   ├── backend/      # BFF FastAPI (§4)
│   ├── frontend/     # React + Vite
│   ├── tools/        # record_oakd.py
│   └── Makefile
├── defensa/          # armar_videos.py, overlay_render.py, montaje_lado_a_lado.py
├── infra/            # despliegue dockerizado two-node (Fase 2c)
├── cameras/          # presets RTSP/OAK-D — GITIGNORADO (credenciales en claro)
├── runs/             # resultados consolidados por experimento — gitignorado
└── docs/
```

### 3.1 El BFF por dentro

`webconsole/backend/src/eovrt_webconsole/`:

| Módulo | Responsabilidad |
|---|---|
| `app.py`, `routers/` | La superficie HTTP |
| `orchestrator.py` | Dispara y coordina corridas en los dos planos |
| `run_backend.py` | **La costura multi-nodo**: abstrae dónde vive cada plano |
| `experiment_deriver.py`, `experiment/` | Deriva la corrida concreta desde el manifiesto |
| `manifest_writer.py` | Materializa el manifiesto efectivo de la corrida |
| `preflight.py` | Chequeos previos al disparo |
| `prompt_store.py`, `repo_catalog.py` | Acceso a los catálogos versionados |
| `clips/`, `recording/` | Grabación y recorte de clips desde la consola |
| `camera_store.py` | Presets de cámara |
| `redact.py` | Redacción de secretos en trazas |
| `trace.py`, `translation.py`, `settings.py` | Trazabilidad, i18n, configuración |

## 4. Contratos y acople

**No define contratos propios de evento.** Consume los de los dos planos por HTTP y
produce dos artefactos propios:

- **Manifiesto de experimento** con `experiment_id` (ADR-004): la corrida paraguas que
  agrupa lo que pasó en ambos planos.
- **Layout consolidado de artefactos** (ADR-014): `runs/<experiment_id>/` con **híbrido
  selectivo** — copia lo liviano (configs, summaries, metrics, alerts, report) y
  **referencia por `run_id`** los `detections.jsonl` pesados, cuya fuente de verdad sigue
  siendo el `runs/` del plano que los produjo.

**El orden de disparo en live no es negociable** (PUB/SUB pierde lo anterior a la
suscripción): primero el control-plane con `mode: live`, después el media-plane con
`bus.enabled: true`. Ver `18` §6.

## 5. Catálogos y resultados

### 5.1 Prompts (`prompts/`)

`cr01_cr02_v2_short.yaml` (**el congelado**, usado en el rodaje y en el bench),
`cr01_cr02_bench_v2.yaml`, `cr01_cr02_v2_safety_vest.yaml`, `eind_v1.yaml`, `edir_v1.yaml`,
`clase_nueva_v1.yaml` (el del piloto de clase nueva), más `_archive/`.
*(✎ 2026-08-19: el benchmark de imágenes vigente es **`bench_v3`**, doc 64 — lo
`bench_v2` de este inventario es histórico.)*

**Los prompts viven acá y no en el media-plane** a propósito: el plano conserva el contrato
y los catálogos por id, y el vocabulario se cambia sin tocarlo.

### 5.2 Experimentos (`experiments/`)

Un directorio por experimento con su manifiesto: `bench_v2`, `diag_riesgo_activo`,
`ebe_oakd_live`, `ebe_p1_live`, `ebe_p2_live`, `ebe_p3_live`, entre otros. Los manifiestos
son **por referencia**: nombran catálogos versionados, no copian valores.
*(✎ 2026-08-19: ídem §5.1 — `bench_v2` acá es inventario histórico; el bench de
imágenes vigente es `bench_v3`, doc 64.)*

### 5.3 Cámaras e infraestructura

`cameras/` está **gitignorado** porque guarda credenciales RTSP en claro. `infra/` tiene el
despliegue dockerizado de dos nodos: imágenes separadas para borde y GPU, verificado en la
Fase 2c. La decisión registrada es **dockerizar solo el escenario de dos nodos**.

### 5.4 `results/` — la fuente canónica de las cifras

**Cuatro índices**, y son la referencia citable de todo el proyecto:

| Índice | Qué cubre |
|---|---|
| `results/bench_imagenes/` | Evaluación sobre el banco de imágenes |
| `results/bench_nivel_a/` | Nivel A (estado por persona) |
| `results/clip_bench/` | Nivel B sobre el banco de clips |
| `results/realtime/` | Fase L, costo del tiempo real |
| `results/index.md` | Entrada, más **las limitaciones declaradas L1–L8** |

Cada campaña citable lleva `campaign.yaml`, `metrics`, `evals` y `provenance`. La
separación es estricta: lo que está en `results/` **es citable**; lo exploratorio vive en
`docs/operacion/datos/` y **nunca se cita como resultado**.

> **La regla que gobierna todo el informe: las cifras salen de estos índices, nunca de
> tablas-atajo ni de documentos de síntesis.** Se verifican con
> `docs/operacion/datos/96-verificar-indices.py`.

> **Al citar `L1` escribir "limitación L1"** — la Fase L usa `L0`/`L1` para sus hitos y se
> confunden.

## 6. La webconsole

Superficie de gestión primaria (ADR-009): dispara corridas en ambos planos, muestra estado
y progreso parcial de patrones, expone alertas y artefactos, gestiona presets de cámara, y
graba y recorta clips.

**El runner CLI se conserva como el camino reproducible**: la consola es la superficie
cómoda, el runner es el que se cita en una tesis.

## 7. Estado de implementación y límites

**Construido:** el BFF con la costura multi-nodo · el frontend · la orquestación de
corridas en ambos planos · grabación y recorte de clips con hardware real · el layout
consolidado de artefactos · los cuatro índices de resultados · el renderer de videos de la
defensa · el despliegue de dos nodos. Suite del BFF: **586 passed**.

**Lo que no está:**

- **El video V2 de la defensa.** Tres de los cuatro están listos; V2 sigue pendiente. El
  intento con `gloves` fue **descartado por falso** — las detecciones caían sobre el casco
  amarillo.
- **`cameras/` sin versionar**, por credenciales. Quien clone no tiene los presets.
- **Los `.mp4` renderizados de la defensa** están gitignorados: se regeneran con
  `armar_videos.py`.

**Runs no citados:** al 2026-08-10, de 167 en `runs/` hay 166 que no cita ningún documento
ni índice. Son wrappers de orquestación (`exp_*_orq_alerts`, `exp_*_diag_riesgo_activo`) y
pesan en total pocos MiB. `runs/` está gitignoreado; el repo versionado son 877 archivos.

## 8. Trampas conocidas

1. **El orden de disparo en live** — control primero, media después. Al revés se pierden
   eventos y la corrida queda degradada.
2. **`outputs.base_dir` resuelve relativo al archivo de config**, no al CWD.
3. **Colisión de directorios de run** con id autogenerado dentro del mismo segundo.
4. **La corrida live del control no es cancelable** desde la consola.
5. **`--to` de `prepare_clip.sh` es relativo**, y un `datasets_videos_dir` custom lo rompe.
6. **Un error de la OAK-D tapa la causa real** en el mensaje que llega a la consola.
7. **Las cifras nunca se leen de un documento de síntesis** — siempre de `results/`.

## Referencias

`14` (mapa de la cadena) · `17` y `18` (los dos planos que orquesta) ·
`specs/44-experimental-setup.md` · ADR-004 (corrida paraguas), ADR-008 y ADR-009
(servicio y consola), ADR-014 (layout de artefactos) · `operacion/97` (capacidades) ·
`operacion/53` (runner y reporte) · `operacion/69` (guion de campo del rodaje).
