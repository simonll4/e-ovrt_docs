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

### ✅ GATES CERRADOS (2026-07-23, misma sesión que abrió este doc)

**G1 — Prompt set del rodaje: CERRADO.** `cr01_cr02_v2_short` (person/helmet/vest, etiquetas
cortas) quedó **`status: frozen`** con `frozen_sha256` en
`e-ovrt_experimental-setup/prompts/cr01_cr02_v2_short.yaml`, commiteado y pusheado
(`3d7dad5`). Es el set oficial de las corridas del rodaje (tomas A DBE y B live) y de toda
evaluación de bench de imágenes. Nota medida (doc 65): el caption de 3 clases suma ~60 ms de
g2a vs person-only — ya contemplado en el presupuesto.

**G3 — Guion de escenas revisado: CERRADO.** `59-guion-grabacion-bloque-a.md` §9 agregado:
config oficial (modelo campeón + prompts congelados + pattern set v2), regla dura del
`starting` (F-DR6), "cantar el evento" en voz alta, reglas de seguridad de escena (piso,
lejos de maquinaria, EPP real disponible, consentimientos antes de grabar), y las trampas
operativas del día (servicios desde su repo, orden EBE, etc.).

**G4 — Higiene de repos: CERRADA.** Los 5 repos (`datasets`, `media-plane`, `control-plane`,
`experimental-setup`, `docs`) están commiteados; los 4 con remote están pusheados
(`docs` no tiene remote por decisión vigente). Working trees limpios verificados
2026-07-23 — no hay material irrepetible en riesgo por árboles sucios.

### ⏳ GATE ABIERTO antes de declarar "todo ok"

**G2 — L0 tramo 2: ensayo mecánico de doble toma (necesita al usuario, ~1 h con cámaras).**
Único gate pendiente — todos los demás (config, guion, higiene de repos) ya están resueltos.
1. Toma A: grabar desde la consola → `prepare_clip.sh` → clip listo (circuito completo).
2. Toma B: corrida live 1:1 inmediata (misma escena).
3. Claqueta de prueba (palmada + hora anotada) → decidir si el stretch `t_alert = TTFD +
   t_capture→alert` entra al rodaje.
4. Medir tiempos de setup por escena → dimensionar la jornada del doc 59.

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

## Secuencia (actualizada 2026-07-23: G1/G3/G4 cerrados)

1. ~~Claude, ya: G1 + B1/B2 del doc 66~~ — **HECHO** (G1 congelado; B1 descartado en
   auditoría, B2/B4/B5 completados con `bench_v3`, doc 66).
2. **Usuario + Claude, próxima sesión con cámaras (~1 h)**: **G2** (ensayo doble toma) +
   recorrer G5. Único paso que falta.
3. ~~Usuario: G4~~ — **HECHO** (los 5 repos commiteados y pusheados).
4. **Día del rodaje**: ejecutar G5; Claude opera los planos y el inventario en vivo.

Del lado del usuario sigue pendiente (fuera del alcance de estos gates): consentimientos
firmados, coordinación de colegas y EPP físico, pasada humana CVAT de los videos de internet,
acta `edir_v1`.
