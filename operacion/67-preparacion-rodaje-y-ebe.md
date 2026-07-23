# 67 — Preparación del rodaje + EBE: estado y gates para el "todo ok" (2026-07-23)

El usuario grabará con colegas apenas esté todo listo, con corridas EBE en la sesión. Este
doc consolida QUÉ está verificado, QUÉ falta, y los gates que definen "listo". Fuentes:
doc 59 (shot-list canónico), 58 §C.5 (protocolo doble toma), 61/64/65 (mejoras+campeón+L0),
memoria del dry-run (F-DR2..10).

## Estado por componente

### ✅ VERIFICADO (no re-verificar, solo no romper)

| Componente | Evidencia |
|---|---|
| Grabación RTSP/OAK-D desde la consola | F-DR2..10 arreglados con TDD y verificados en hardware 07-22 (timestamps wallclock, warmup OAK-D, estado `starting` "no actúes todavía", `-an`, re-sync tras 409, selector de cámara) |
| Pipeline live sin drops de arranque | pre-flight `prepare_run` (doc 61 adenda), verificado live en L0 (frame0 711 ms sin cascada) |
| EBE 1:1 dos planos punta a punta | L0 tramo 1 (doc 65): control-first `subscribed:true`, 30/30, `bus_dropped=0`, `cr01_cr02_v2`, alerta CR-01 real emitida |
| Config live del control-plane | `configs/live_ebe_cr01_cr02.yaml` con pattern set **v2** (F-DR9) |
| OAK-D | IP fija 192.168.1.50, connect ~9 s conocido, preset `fps: 30` (~13 fps reales), prefilter EN-2 APAGADO en evaluativo (D-61.2) |
| Modelo del carril live | **`grounding-dino/gdino-tiny-560`** — campeón S2 validado en BENCH (doc 64) y en live (docs 61/65) |
| Suites | media 636 / control 246+ / datasets 119 / webconsole verde al 07-23 |

### ⏳ GATES ABIERTOS antes de declarar "todo ok"

**G1 — Decisión de prompts del rodaje (la única decisión de config pendiente).**
El L0 corrió con prompts inline ad-hoc. Para el rodaje hay que fijar EL prompt set oficial
de las corridas (DBE y live) desde el catálogo del experimental-setup — candidato natural:
el linaje `cr01_cr02_v2` (person/helmet/vest con fraseos por backend) — y **congelarlo antes
del rodaje** (además lo exige el plan de ampliación del bench, doc 66). Nota medida (doc 65):
el caption de 3 clases suma ~60 ms de g2a vs person-only — ya contemplado.

**G2 — L0 tramo 2: ensayo mecánico de doble toma (necesita al usuario, ~1 h con cámaras).**
1. Toma A: grabar desde la consola → `prepare_clip.sh` → clip listo (circuito completo).
2. Toma B: corrida live 1:1 inmediata (misma escena).
3. Claqueta de prueba (palmada + hora anotada) → decidir si el stretch `t_alert = TTFD +
   t_capture→alert` entra al rodaje.
4. Medir tiempos de setup por escena → dimensionar la jornada del doc 59.

**G3 — Guion de escenas revisado (tramo 3 del doc 60 §8, pendiente desde el dry-run).**
Revisar `59-guion-grabacion-bloque-a.md` con los aprendizajes de tramos 1-2 e incorporar:
- **"Cantar el evento en voz alta"** (doc 60 §9) al iniciar/terminar cada infracción actuada.
- Regla dura del F-DR6: **nadie actúa hasta que la UI salga de `starting`** (la OAK-D tarda
  9 s en conectar; el REC prematuro costó una toma en el dry-run).
- Escenas live mínimas: 1×P1, 1×P2, 1×P3 (P3 = demo de persistencia). P2×3 tomas (vest).
- **Seguridad de escena (pedido explícito):** infracciones SIEMPRE actuadas a nivel de piso
  — nada de altura real ni cerca de maquinaria operando; EPP real disponible para el "estado
  cumplidor"; zona despejada; consentimientos firmados ANTES de grabar (lado usuario).

**G4 — Higiene de repos ANTES del rodaje (riesgo real).**
Hay trabajo sin commitear en 5 repos (mejoras doc 61, prepare_run, catálogos 560, curación
bench, docs 62-67) + commits sin pushear previos. **Grabar material irrepetible sobre árboles
sucios es riesgo innecesario**: decidir commit (y push si corresponde) ANTES de la jornada —
decisión del usuario, regla de no-commit-sin-pedido vigente.

**G5 — Checklist del día (recorrerla en G2, ejecutarla el día):**
1. Disco: ≥20 GB libres en el destino de `datasets-videos/raw/` (y ojo tmpfs de `/tmp`).
2. Servicios **desde la raíz de su repo** (trampa doc 65: artefactos fuera de lugar).
3. `EOVRT_MODEL_REF=grounding-dino/gdino-tiny-560`; smoke `/healthz`+`/readyz`.
4. Orden EBE: control-plane primero (`subscribed:true`), media después; terminal `succeeded`;
   409 al reintentar = reusar el run activo.
5. Consola: Ctrl+Shift+R tras cualquier cambio de frontend; entrar por `/` (deep-link 404).
6. Cámaras: ping a 192.168.1.5 y .50; EZVIZ tope 15 fps (no hay más); preset OAK-D fps 30.
7. Por escena: grabar toma A (esperar fin de `starting` → actuar → cantar el evento) → toma
   B live 1:1 → verificar `bus_dropped_events=0` antes de desarmar la escena.
8. Al cierre: inventario de tomas vs shot-list ANTES de que los colegas se vayan (el doc 59
   §6 define el mínimo por escenario — es más barato repetir en el momento).

## Secuencia propuesta

1. **Claude, ya**: G1 (proponer el prompt set congelado para tu OK) + B1/B2 del doc 66 en
   paralelo (no bloquea nada del rodaje).
2. **Usuario + Claude, próxima sesión con cámaras (~1 h)**: G2 (ensayo doble toma) + G3
   (revisión del guion juntos) + recorrer G5.
3. **Usuario**: G4 (decisión de commits), consentimientos, coordinación de colegas y EPP.
4. **Día del rodaje**: ejecutar G5; Claude opera los planos y el inventario en vivo.
