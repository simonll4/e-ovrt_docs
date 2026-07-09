# Spec 43 — Clip bench con GT temporal

- **Fecha:** 2026-07-09
- **Estado:** Escrito y congelado — **EJECUCIÓN DIFERIDA (ADR-010):** se dispara
  al **cierre del spec 44 (experimental-setup)** — corridas y configs trazables +
  runner + reporte operativos; el spec 45 (distribución) NO es prerequisito.
  Mientras tanto corren en paralelo: el **armado del material crudo del dataset
  (videos), ya en proceso**, la coordinación de videos Intel (bloque B) y los
  consentimientos. Lo diferido es la ejecución formal (GT, anotación, validación,
  registry), no la recolección.
- **Repo dueño:** `e-ovrt_datasets`
- **Decisiones que implementa:** ADR-002 (GT a nivel escena-condición + identidad
  mínima solo en clips G1-demo), ADR-006 (estados de aplicabilidad en la
  evaluación). Insumos: doc 07 H2/H4/H8, doc 08 (§1.3 marco legal, §2.2 métricas
  y t0, §5.1 Tabla C.2), doc 12 §5 (Fase 2 de D1), doc 09 (videos V1–V3),
  Tabla D.4 (umbrales por severidad).
- **Qué desbloquea:** R3 (cadena completa con métricas temporales), Fase 2 del
  experimento D1, comparación DBE↔EBE con fuente idéntica (H4), demo G1 (ADR-002).
- **Prioridad:** se ejecuta inmediatamente después del spec 44 (ADR-010,
  precisión 07-09). La Fase 1 de D1 (BENCH, imágenes) NO depende de este spec.

## 1. Objetivo y alcance

Producir un banco de **8–15 clips de 10–60 s** con **ground truth temporal de
episodios** para CR-01/CR-02, que permita a `evaluate-alerts` calcular
precision/recall/F1 de alertas, `t_alert-system`, TTFD y SDR contra los umbrales de
la Tabla D.4 — sin código nuevo de evaluación más allá de la adaptación del spec 41.

**Fuera de alcance:** GT de identidades / métricas MOT (E-10), condiciones
CR-03…06 (E-01/E-02), anotación de bboxes por frame (la detección ya se evalúa en
BENCH v2; este banco evalúa **alertas**, no detecciones).

## 2. Composición del banco

| Bloque | Fuente | Cantidad | Rol |
|---|---|---|---|
| A — Escenificado | Grabación propia guionada (persona real con/sin EPP) | 8–10 clips | Núcleo del banco. Es el **Escenario B oficial del informe** (Tabla 20: "espacio de obra simulado… con y sin infracción deliberada"), no un atajo. GT exacto por diseño del guion. |
| B — Obra real | 2–3 clips de los videos Intel (`video1`…`video5`, entorno del compañero, doc 01 §12.3) o CC con licencia clara | 2–3 clips | Validez externa: episodios no guionados. GT por anotación (doble anotador). |
| C — Defensa (misma sesión que A) | Guiones V1 (cadena completa), V2 (clase nueva por config), V3 (cumplimiento → no-alerta) del doc 09 | 3 clips | Se graban en la misma sesión con el mismo setup — V3 además ES un clip negativo del banco. |

**Acción de coordinación (bloquea el Bloque B, no el A):** obtener los videos Intel
del compañero y registrar la licencia del dataset en `license_registry.md`
(trámite gestionable durante el tramo plataforma, ADR-010). Si no están para
cuando arranque la ejecución, el banco arranca solo con A+C (válido: n≥8).

## 3. Guion de grabación (Bloque A) — matriz de escenarios

Cada clip implementa **un escenario único** con timeline guionado. La matriz cruza
los casos de patrón con las variables de sensibilidad de la **Tabla C.2** (así la
grabación es, a la vez, la campaña EBE del informe):

### 3.1 Casos de patrón (qué pasa en el clip)

| Caso | Descripción | GT esperado | Clips |
|---|---|---|---|
| P1 — CR-01 persistente | Persona sin casco > ventana de confirmación (≥ 8 s continuos) | 1 episodio CR-01 | 2 |
| P2 — CR-02 persistente | Persona sin chaleco > ventana (≥ 12 s) | 1 episodio CR-02 | 2 |
| P3 — Transitorio no alertable | Sin EPP durante < persistencia mínima (2 s), se lo pone | 0 alertas (episodio sub-umbral anotado como negativo con causa) | 1 |
| P4 — Resolución | Sin casco ≥ 8 s → se lo pone y permanece en cuadro ≥ 10 s | 1 episodio CR-01 con `end_ms` (cierra por resolve) | 1 |
| P5 — Cumplimiento total (= V3) | EPP completo todo el clip | 0 episodios (`negative: true`) | 1 |
| P6 — Doble condición | Sin casco y sin chaleco simultáneos | 1 episodio CR-01 + 1 CR-02 solapados | 1 |
| P7 — Multi-persona (G1-demo) | 2–3 personas, una sin EPP, con cruces/solapamiento | episodios `level: subject` (ver §4.3) | 2–3 |
| P8 — Entrada/salida | El infractor sale de cuadro y vuelve | 2 episodios de la misma condición (corte por ausencia) | 1 |

### 3.2 Variables de sensibilidad (Tabla C.2 — variar entre clips, no dentro)

- **Resolución:** 1280×720 base (1080p solo como variante en 1–2 clips).
- **Distancia cámara–sujeto:** banda 5–10 m (mayoría) y banda 10–20 m (2 clips).
- **Iluminación:** controlada/interior y natural/exterior (mínimo 2 clips exterior).
- **Oclusión:** baja (mayoría) y media (los clips P7; severa no exigible).
- Cámara **fija** (trípode), sin zoom ni paneo — condición del EBE del informe.
- FPS de grabación: el nativo del dispositivo (declararlo); el rate-gate del
  media-plane decide el FPS efectivo por corrida, no la grabación.

### 3.3 Regla de oro del guion

El operador registra el **timeline planificado por escena** (tabla: t inicio, t fin,
acción) ANTES de grabar, y el anotador marca los tiempos **reales** contra el video
después. El GT sale del video, no del plan — el plan solo garantiza que los casos
ocurran.

## 4. Formato de GT temporal v2 (`clip_gt.v2`)

Extiende el `ground_truth.json` existente del control-plane (hoy: alertas esperadas
por `subject_key` con frames esperados — fixture `cr01_cr02_temporal`). El v2 pasa a
**episodios a nivel escena-condición** (G0, ADR-002) con tiempos en ms:

```json
{
  "schema_version": "clip_gt.v2",
  "clip_id": "cb_a01_p1_cr01",
  "source_file": "clips/cb_a01_p1_cr01.mp4",
  "block": "A",
  "scenario": "P1",
  "fps_nominal": 30,
  "duration_ms": 32000,
  "recording": { "resolution": "1280x720", "distance_band_m": "5-10",
                 "lighting": "natural", "occlusion": "low" },
  "negative": false,
  "episodes": [
    {
      "id": "ep1",
      "condition_id": "CR-01",
      "level": "scene",
      "start_ms": 4200,
      "end_ms": 21500,
      "subjects_in_evidence": 1,
      "notes": "se quita el casco en t=4.2s, lo recupera en t=21.5s"
    }
  ],
  "sub_threshold_events": [
    { "condition_id": "CR-01", "start_ms": 26000, "end_ms": 27500,
      "reason": "transitorio < persistencia mínima — NO debe alertar" }
  ],
  "annotation": {
    "annotator": "a1", "double_annotated": true,
    "second_annotator": "a2", "kappa": null,
    "start_end_tolerance_ms": 500
  }
}
```

### 4.1 Semántica de los campos críticos

- **`start_ms` = inicio anotado del evento** — es el **t0 oficial** de
  `t_alert-system` y TTFD (doc 08 §2.2: "inicio anotado", NO primera detección).
  El `t1` de TTFD se toma en el **instante de captura** del frame de primera
  evidencia (spec 40 §5.2.2): con esa convención vale exactamente
  `t_alert-system = TTFD + t_capture→alert`, y la primera corrida con GT debe
  **verificar numéricamente esa identidad** como control de consistencia entre el
  tramo plataforma y el tramo de evaluación.
- **`end_ms`**: fin observable de la condición (se pone el EPP o sale de cuadro).
- **Criterio de matching alerta↔episodio** (lo consume el evaluador, spec 41): una
  alerta matchea si su `condition_id` coincide y su timestamp cae en
  `[start_ms + persistencia_min, start_ms + t_alert_max]`, con `persistencia_min` y
  `t_alert_max` tomados del pattern set/Tabla D.4 vigentes en la corrida (PR-01:
  3 s / 10 s; PR-02: 5 s / 20 s). Alertas fuera de todo episodio → `unexpected`
  (FP); episodios sin alerta → `missed`. **Alertas adicionales dentro del mismo
  episodio → `re_alerts` (ADR-011):** el motor emite en cada confirmación del
  patrón y la supresión de re-notificación es del tramo de distribución, así que
  las re-alertas se reportan como métrica de estabilidad de la percepción, no se
  penalizan como falsos positivos.
- **`sub_threshold_events`**: eventos reales pero no alertables — permiten
  distinguir "FP verdadero" de "alerta a evento sub-umbral" en el análisis de
  errores (insumo directo del capítulo R3).
- **SDR** se calcula sobre `[start_ms, end_ms]`: proporción del intervalo anotado
  con detección positiva sostenida (definición §17.1.7 / doc 08 §2.2).

### 4.2 Anotación y calidad

- **Doble anotación ≥20% de los clips** (mínimo 3, incluyendo 1 del Bloque B) con
  **kappa de Cohen** sobre presencia/condición por ventana de 1 s, y desacuerdo de
  bordes reportado como |Δstart| y |Δend| medianos. Tolerancia declarada
  `start_end_tolerance_ms: 500` (medio segundo: la incertidumbre humana de "cuándo
  terminó de sacarse el casco").
- Los clips escenificados también entran al sorteo de doble anotación: el guion no
  reemplaza la verificación de tiempos reales.
- El kappa y las tolerancias van al reporte consolidado (ADR-006) como metadatos de
  calidad del GT.

### 4.3 Clips G1-demo (ADR-002)

En los 2–3 clips P7, los episodios llevan `level: "subject"` y un campo adicional
`subject_label` local al clip (`"persona_A"`, `"persona_B"`) con una línea de
descripción física para el anotador. **No es GT MOT**: no hay trayectorias ni ids
por frame — solo "qué persona protagoniza el episodio", suficiente para comparar
episodios G0 vs G1 cualitativamente y contar fragmentaciones evidentes. E-10 sigue
"no aplicable" y así se declara.

## 5. Layout en el repo datasets y versionado

```
e-ovrt_datasets/datasets/
├── raw/clip_bench/                    # git-IGNORED (política de raw media)
│   ├── clips/*.mp4                    # los clips finales recortados
│   └── sessions/                      # material bruto de grabación
├── processed/clip_bench/
│   ├── gt/*.json                      # clip_gt.v2 — SE COMMITEA
│   └── manifest.yaml                  # SE COMMITEA: clip_id → archivo, sha256,
│                                      #   duración, escenario, bloque, estado GT
└── registry/                          # SE COMMITEA
    ├── license_registry.md            # + categoría "clips temporales" (H8):
    │                                  #   consentimientos A/C, licencia Intel B
    └── datasets_metadata.yaml         # + entrada clip_bench
```

- **Script nuevo** `datasets/scripts/bench/validate_clip_gt.py`: valida schema
  v2, consistencia interna (episodios dentro de `duration_ms`, sin solape de la
  misma condición, `negative` ⇔ sin episodios), y cruza `manifest.yaml` contra los
  archivos y checksums. Con test en `datasets/tests/` sobre fixture sintético
  (sin media real, como el resto del repo).
- Los `.mp4` no se commitean; el `manifest.yaml` con sha256 hace reproducible la
  verificación de qué versión del clip corresponde a qué GT.

## 6. Empaquetado DBE ↔ EBE (fuente idéntica, H4)

- **DBE:** el clip como archivo — consumido por `VideoFileSource` del media-plane
  (R3/R4) y por `eovrt-labs generate-detections` para los replays de la Fase 2 de
  D1 (doc 04 §8.6).
- **EBE:** el mismo archivo servido como stream en vivo:
  `mediamtx` + `ffmpeg -re -stream_loop` (receta en el runbook de operación,
  serie 30). La Tabla 55 del informe admite explícitamente "archivo simulado como
  stream". La cámara IP real (contingencia oficial, doc 08 §2.6) se usa para la
  demo en vivo; el RTSP-desde-clip da la **comparación DBE-vs-EBE con fuente
  idéntica** — resultado extra de robustez, gratis.
- El manifiesto de corrida (ADR-004/spec 44) referencia `clip_id`; el reporte
  consolidado liga `experiment_id → clip_id → gt/*.json` — trazabilidad completa
  de cada número de R3 hasta el clip y su GT.

## 7. Marco legal (bloqueante de la grabación, no del diseño)

- **Consentimiento libre, expreso e informado por escrito** de cada persona
  grabada (Ley 25.326, Disposición 10/2015 — doc 08 §1.3), archivado y referenciado
  en `license_registry.md` (sin datos personales en el repo).
- Minimización (DA-08/09): los clips son material controlado para evaluación y
  comunicación académica; sin captura automática en runtime (E-11 intacta).
- Bloque B: registrar la licencia del dataset Intel antes de usar los videos en
  resultados reportables.

## 8. Procedimiento de ejecución (orden)

1. Congelar este spec + guiones por clip (tabla de escenas de §3.3). *(½ día)*
2. Consentimientos firmados + checklist de grabación (EPP disponibles: casco,
   chaleco alta visibilidad; trípode; locación interior y exterior). *(½ día)*
3. Sesión de grabación A+C (un día de grabación bien guionado alcanza). *(1 día)*
4. Volcado, recorte, `manifest.yaml` con checksums. *(½ día)*
5. Anotación de GT contra video + doble anotación del 20% + kappa. *(1–1½ días)*
6. `validate_clip_gt.py` en verde sobre todo el banco. *(incluido en 5)*
7. Registry (licencias, consentimientos, metadata). *(½ día)*
8. **Smoke end-to-end:** 1 clip → `generate-detections` (labs, gdino, tuning
   congelado) → replay control-plane (pattern set v2) → `evaluate-alerts` con GT
   v2 → P/R/F1 + latencias emitidas. *(½ día — requiere el evaluador v2 del
   spec 41; si aún no está, el smoke corre con el matching v1 sobre un clip P1 y
   se marca la brecha)*
9. Bloque B cuando lleguen los videos Intel (anotación + registry). *(paralelo)*

Total estimado: **~1 semana calendario**, paralelizable con todo lo demás
(coincide con el presupuesto del doc 02 §4.5).

## 9. Criterios de terminado (evidencia, no código — doc 02 §2.6)

- [ ] ≥ 8 clips en `manifest.yaml` con GT `clip_gt.v2` válido (`validate_clip_gt.py`
      en verde), cubriendo: ≥2 P1, ≥2 P2, ≥1 negativo (P5), ≥1 transitorio (P3),
      ≥1 resolución (P4), ≥2 multi-persona (P7 con `level: subject`).
- [ ] Ambas bandas de distancia y ambas iluminaciones representadas (Tabla C.2).
- [ ] Kappa de la doble anotación reportado (≥20% de los clips) + |Δstart|/|Δend|.
- [ ] Consentimientos y licencias en `license_registry.md`; sha256 en manifest.
- [ ] Smoke end-to-end del §8.8 ejecutado con artefactos persistidos en `runs/`.
- [ ] Los 3 clips V1–V3 de la defensa grabados (aunque su edición final sea del
      overlay renderer, doc 10 ítem 7).

## 10. Métricas que habilita (mapeo al diccionario del spec 40)

| Métrica | t0 | t1 | Contra qué se lee |
|---|---|---|---|
| `t_alert-system` | `start_ms` del episodio (inicio anotado) | alerta confirmada registrada | Tabla D.4: PR-01 (alta) 5–10 s; PR-02 (media) 10–20 s |
| TTFD | `start_ms` | primera detección positiva válida (criterio declarado por estrategia) | PR-01 < 3 s; PR-02 < 10 s |
| SDR | — | proporción de `[start_ms, end_ms]` con detección sostenida | PR-01 ≥ 0.60; PR-02 ≥ 0.70 |
| P/R/F1 de alertas | matching del §4.1 | — | criterios de decisión D1 (doc 04 §8: veto precision < 0.5) |
| Re-alertas por episodio (ADR-011) / inesperadas / sub-umbral alertadas | §4.1 | — | análisis de errores R3 |

Toda métrica no computable en una corrida se reporta con su estado de
aplicabilidad + causa (ADR-006), nunca se omite.

## 11. Interfaces con otros specs

- **Spec 41 (control-plane):** `evaluate-alerts` debe consumir `clip_gt.v2`
  (episodios escena-condición + tolerancias + sub-umbral) además del formato v1
  del fixture sintético — el gate de regresión F1=1.0 sobre el fixture se conserva.
- **Spec 44 (experimental-setup):** el manifiesto de corrida referencia `clip_id`;
  las campañas de la Fase 2 de D1 iteran sobre el manifest del banco.
- **Spec 40 (integrador):** las definiciones de §10 se transcriben al diccionario
  de métricas (única fuente: §17.1.7 + Tabla D.4 — este spec no las redefine).
