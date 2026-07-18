# Cómo continuar — guía paso a paso (estado al 2026-07-11)

- **Fecha:** 2026-07-11
- **Qué es:** el mapa para retomar el proyecto. Qué está construido y probado, qué
  falta, y el **orden concreto** de los próximos pasos con los comandos reales.
  Si volvés después de un tiempo y no te acordás de nada, **leé este doc y el 50**.
- **Estado de commits (✎ refrescado 2026-07-18, doc 56 §1/§5):** HEADs actuales
  `e-ovrt_datasets@42cfff37` (en sync), `e-ovrt_media-plane@eddeb89` (**ahead 2**),
  `e-ovrt_control-plane@a53e95e` (**ahead 1**), `e-ovrt_experimental-setup@cb72425`
  (**ahead 15**). Hay 18 commits sin pushear y 4 working trees con trabajo terminado
  sin commitear — inventario exacto en el doc 56 §5. El repo `docs` sigue **local sin
  remote** (decisión tuya del 07-09).
- **✎ 2026-07-18:** desde que se escribió esta guía la plataforma sumó: OAK-D +
  prefilter EN-2, ledger de descartes, progreso parcial de patrones, consola
  rediseñada con **vista correlacionada media↔control**, borrado orquestado de runs,
  y la ventana **Cámaras** con preview en vivo (posicionar cámara + probar prompts
  sin corrida). Nada de eso cambia los PASOS 1–5 de esta guía, que siguen vigentes.
  La foto completa está en
  [`operacion/56`](56-relevamiento-plataforma-2026-07-18.md).

---

## 1. Dónde estamos, en una frase

**La plataforma está completa y probada de punta a punta.** Podés meterle un video,
que detecte, que genere alertas y que te dé las 5 métricas de la tesis. Lo único
que le falta al proyecto es **el dato**: los clips de video reales, grabados y
anotados por vos.

Hoy hay **un solo clip** en el banco (`cb_b01_p7`, obra real, ~10 operarios) con un
**GT preliminar** que generé yo por revisión visual. Sirve para que la plataforma
arranque y para probar, **no para los números de la tesis**.

---

## 2. Lo que YA ESTÁ HECHO (no re-implementar nada de esto)

### 2.1 La plataforma (los dos planos + el orquestador)

| Pieza | Estado | Dónde |
|---|---|---|
| **Media-plane**: servicio HTTP de inferencia OVD, fuentes (video/imágenes/RTSP), bus ZeroMQ, instrumentación G2A | ✅ probado E2E | `e-ovrt_media-plane` |
| **Control-plane**: servicio HTTP, motor de patrones CR-01/CR-02, pattern set oficial `cr01_cr02_v2`, publisher de alertas | ✅ probado E2E | `e-ovrt_control-plane` |
| **`evaluate-alerts`**: emite **las 5 métricas** del spec 43 §10 (P/R/F1, t_alert-system, **TTFD**, **SDR**) | ✅ probado con datos reales | `evaluation/temporal.py` |
| **Experimental-setup**: runner reproducible que orquesta los dos planos, consolida artefactos (ADR-014) y genera `report.json` | ✅ probado contra servicios reales | `e-ovrt_experimental-setup` |
| **Webconsole**: backend + frontend React (lista de experimentos, disparo, alertas, reporte) | ✅ | `webconsole/` |
| **EBE two-node** (Docker, dos nodos) | ✅ (Fase 2) | `infra/twonode/` |

### 2.2 El laboratorio de GT de video (`video-gt-lab`)

El pipeline que convierte un video crudo en ground truth temporal:

```
video → prepare_clip.sh → preannotate_video → CVAT (vos) → derive_clip_gt.py
        (CFR + sha256)    (GDINO-base+track)   corregís    (episodios CR-01/CR-02)
                                                              ↓
                                            validate_clip_gt.py + promote_clip.py
                                                    (valida)      (al banco)
```

**Todo funciona y está probado.** El detalle está en `operacion/54` y en el spec del
laboratorio (`e-ovrt_datasets/docs/superpowers/specs/2026-07-11-video-gt-lab-design.md`).

Cosas importantes que ya resolvimos y **no tenés que pensar**:

- La **incertidumbre nunca fabrica una infracción**: si el detector no vio a alguien,
  o vos dejás un atributo en `unknown`, el GT no afirma nada (no inventa un "sin casco").
- El **`source_id = clip_id`** es la convención que hace que las alertas matcheen con el
  GT. La corrida del bench configura su fuente con el `clip_id` — el runner lo hace solo.
- Los **umbrales oficiales son 4000/7000 ms** (CR-01 / CR-02, Tabla D.4). Son el default
  en todos lados; no los toques salvo que cambies el pattern set.

### 2.3 El primer clip del banco y el primer benchmark

`datasets/processed/clip_bench/` tiene `cb_b01_p7` en estado **`gt_preliminary`**.

Primer benchmark real (GDINO-tiny, DBE, contra ese GT preliminar):

| Métrica | Valor | Qué significa |
|---|---|---|
| recall | **1.0** | detectó la infracción real (el operador del compactador, sin casco) |
| precision | **0.5** | 1 alerta correcta + **1 falso positivo genuino**: el modelo perdió el chaleco de alguien y alertó CR-02 de más |
| t_alert-system | 4000 ms | confirmó justo en la ventana de persistencia |
| TTFD / SDR | 0 ms / 0.999 | detección inmediata y sostenida |

**Ese falso positivo es un hallazgo sobre el modelo, no un bug** — es exactamente el
tipo de resultado que la plataforma existe para medir.

---

## 3. Lo que FALTA

| # | Falta | Quién | ¿Bloquea? |
|---|---|---|---|
| 1 | **Pasada humana en CVAT** del clip que ya está (reemplaza mi GT preliminar) | vos | los números reportables |
| 2 | **Grabar el banco A+C** (guiones P1–P8 + V1–V3) + consentimientos | vos | R3 / D1-Fase2 |
| 3 | **Bloque B**: videos Intel del compañero + licencia | vos (trámite) | nada (opcional, n≥8 alcanza con A+C) |
| 4 | **Spec 45** — distribución de alertas por MQTT (repo nuevo) | Claude | nada (lo dejaste para el final) |
| 5 | **Evaluadores D1** (E-IND vs E-DIR) | Claude | **bloqueado por el acta `edir_v1`** (la tenés que firmar vos) |
| 6 | **EBE-desde-clip** (comparación DBE↔EBE con fuente idéntica, H4) | Claude | nada (brecha de diseño documentada: falta el ancla wallclock↔media) |
| 7 | Tracker / `track_id` (spec 42 §3) | Claude | métricas G1 (no son del núcleo). OAK-D: ✅ integrada 2026-07-13 (fuente `oak_d` del media-plane, verificada E2E con hardware) |

---

## 4. EL PASO A PASO — qué hacer, en orden

### PASO 1 — Probar CVAT con el clip que ya está *(medio día, tu otra PC)*

Es lo primero porque **valida la herramienta antes de que grabes nada**. Si CVAT no
importa bien el XML, mejor saberlo ahora que con 15 clips grabados.

1. **Cloná el repo `e-ovrt_datasets`** en la PC donde vas a correr CVAT.
   Ya viene todo el material de trabajo (XML de pre-anotación, labels, metadata, guía).
2. **Bajate el video de Drive**: `cb_b01_p7.mp4` → ponelo en
   `datasets/raw/clip_bench/clips/`. (Los `.mp4` no están en git, por tu decisión.)
   El `sha256` está en `datasets/processed/clip_bench/meta/cb_b01_p7.info.json` si
   querés verificar que es el correcto.
3. **Seguí la guía**: `datasets-videos/GUIA-CVAT.md`. Incluye **cómo levantar CVAT en
   Linux con Docker** (instalación, usuario admin, operación diaria) y el protocolo de
   corrección.
4. **Hacé primero el roundtrip del paso 6 de la guía**: importás el XML, lo exportás
   **sin editar nada**, y comparás. Si da `ROUNDTRIP OK`, la herramienta está validada.
   Si no, guardá los archivos y avisame.

> **Qué vas a corregir:** ~38 tracks. Lo que más trabajo da es **unir tracks
> fragmentados** (ByteTrack corta cuando la maquinaria tapa a alguien). Los atributos
> ya vienen bastante bien. Presupuesto realista: 30–60 min para este clip
> (es multitud; los clips escenificados van a ser mucho más rápidos).

### PASO 2 — Reemplazar mi GT preliminar por el tuyo *(30 min, en la PC con GPU)*

Cuando exportes el XML corregido de CVAT:

```bash
cd e-ovrt_datasets
# 1) poné el XML exportado acá:
#    datasets-videos/corrected/cb_b01_p7.xml

# 2) derivá el GT (los umbrales oficiales 4000/7000 son el default)
python3 datasets/scripts/videogt/derive_clip_gt.py \
    --xml datasets-videos/corrected/cb_b01_p7.xml \
    --clip-yaml datasets-videos/cb_b01_p7.clip.yaml \
    --info datasets-videos/clips/cb_b01_p7.info.json \
    --out datasets-videos/gt/cb_b01_p7.json

# 3) MIRÁ EL TIMELINE que imprime, contra el video. Es la regla de oro:
#    el GT sale del video, el script solo hace la aritmética.

# 4) validá
python3 datasets/scripts/bench/validate_clip_gt.py --gt-dir datasets-videos/gt

# 5) promové al banco (ahora sí, gt_ready)
python3 datasets/scripts/bench/promote_clip.py --clip-id cb_b01_p7 --state gt_ready
```

Antes de derivar, editá `datasets-videos/cb_b01_p7.clip.yaml` y cambiá
`annotator: claude-vision-preliminary` por tu nombre. Ese `clip.yaml` es la metadata
del clip (bloque, escenario, nivel, condiciones de grabación).

### PASO 3 — Correr el benchmark con TU GT *(15 min)*

Ya está todo automatizado por el runner. La forma corta (manual, la que probé):

```bash
# a) levantá el media-plane con el modelo que quieras evaluar
cd e-ovrt_media-plane
EOVRT_MODEL_REF=grounding-dino/gdino-tiny .venv/bin/python -m uvicorn \
    --factory eovrt_media.service.app:create_app --port 8080

# b) disparás la corrida (POST /api/runs) con:
#      ingest.plugin = video_file
#      ingest.config.path = .../clips/cb_b01_p7.mp4
#      ingest.config.source_id = "cb_b01_p7"     <-- CLAVE: sin esto no matchea el GT
#      prompts.set_inline = person/helmet/vest

# c) replay del control-plane con el pattern set oficial
cd ../e-ovrt_control-plane
.venv/bin/python -m eovrt_control.cli replay <config.yaml>
#   (input.type: media_jsonl, path al detections.jsonl del media-plane;
#    patterns.file: configs/patterns/cr01_cr02_v2.yaml)

# d) las 5 métricas
.venv/bin/python -m eovrt_control.cli evaluate-alerts \
    <runs/.../alerts.jsonl> \
    ../e-ovrt_datasets/datasets/processed/clip_bench/gt/cb_b01_p7.json \
    --detections <runs/.../detections.jsonl> \
    --patterns configs/patterns/cr01_cr02_v2.yaml \
    --output evaluation.json
```

**La forma larga (recomendada para las campañas):** usar el **runner del
experimental-setup**, que hace todo esto solo a partir de un manifiesto con
`clip_id` + `ground_truth`, consolida los artefactos y te genera el `report.json`
con las métricas y la trazabilidad. Está probado contra servicios reales.

### PASO 4 — Grabar el banco *(la parte grande — 1 semana calendario)*

Esto es lo que desbloquea los resultados de la tesis (R3, Fase 2 de D1).
El guion completo está en **`specs/43-clip-bench-gt-temporal.md` §3**. Resumen:

1. **Consentimientos por escrito** de cada persona grabada (Ley 25.326) — *bloqueante
   legal, no lo saltees*. Archivalos y registralos en `license_registry.md`.
2. **8–10 clips escenificados (Bloque A)** de 10–60 s, cámara fija en trípode, con la
   matriz de escenarios: P1 (sin casco persistente), P2 (sin chaleco), P3 (transitorio
   que NO debe alertar), P4 (se pone el casco), P5 (cumplimiento total = negativo),
   P6 (doble condición), P7 (multi-persona), P8 (sale y vuelve).
3. **3 clips de la defensa (Bloque C)**: V1 (cadena completa), V2 (clase nueva por
   config), V3 (cumplimiento → no-alerta). Se graban en la misma sesión.
4. Variá entre clips: distancia (5–10 m y 10–20 m), iluminación (interior y exterior).
5. **Anotá cada clip** con el pipeline (pasos 1–2 de esta guía). Presupuesto real:
   5–10 min por clip escenificado.
6. **Doble anotación del ≥20%** de los clips (kappa) — `compare_annotations.py`.

### PASO 5 — Los resultados de la tesis

Con el banco anotado, corrés las campañas y salen los números de R3. A partir de acá
el trabajo vuelve a ser mío (implementar lo que falte, correr las campañas, generar
el reporte consolidado).

---

## 5. Cosas que me podés pedir mientras tanto (no dependen de vos)

- **Spec 45 — distribución de alertas por MQTT** (repo nuevo). Lo dejaste "para lo
  último"; se puede hacer cuando quieras.
- **EBE-desde-clip**: resolver el ancla de sincronización wallclock↔media para poder
  comparar DBE vs EBE con la misma fuente (H4). Hoy es una brecha de diseño conocida.
- **Deuda técnica registrada**: matching bipartito en el evaluador (el greedy puede
  deprimir recall en clips P8 con ≥2 alertas), el caveat del `PATH` del subprocess
  `eovrt-control` en el runner, y el tracker/`track_id` (spec 42 §3).
- **El overlay renderer** para los videos de la defensa (doc 09).

**Lo que NO se puede hacer sin vos:** los evaluadores D1 (E-IND vs E-DIR) están
bloqueados por el **acta `edir_v1`** — es una decisión de diseño experimental que
tenés que firmar (doc 12 §2.2).

---

## 6. Referencias rápidas

| Necesito… | Leer |
|---|---|
| Estado general del tramo plataforma | `operacion/50` (+ sus banners) |
| Qué es el laboratorio de GT y cómo funciona | `operacion/54` |
| Cómo usar CVAT (incluye instalación) | `e-ovrt_datasets/datasets-videos/GUIA-CVAT.md` |
| El pipeline de GT en detalle | `e-ovrt_datasets/docs/superpowers/specs/2026-07-11-video-gt-lab-design.md` |
| Cómo se compone el banco de clips (guiones) | `specs/43-clip-bench-gt-temporal.md` §3 |
| Las métricas y sus definiciones | `specs/43` §10 y `specs/40` §17.1.7 |
| Las decisiones ya cerradas (no re-litigar) | `decisiones/adr-001…014` |
| Qué está excluido del alcance | `nucleo/10-registro-alcance-y-exclusiones.md` |
