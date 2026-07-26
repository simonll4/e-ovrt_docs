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
| OAK-D | IP fija **169.254.31.137** (link-local desde 07-25; era `192.168.1.50`), connect ~9 s conocido, preset `fps: 30` (~13 fps reales con luz de laboratorio, ~22 medidos 07-25), prefilter EN-2 APAGADO en evaluativo (D-61.2) |
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

### ✅ GATE CERRADO (2026-07-23, ensayo con cámaras reales)

**G2 — L0 tramo 2: ensayo mecánico de doble toma. CERRADO.** Los 4 pasos, con la OAK-D real
(192.168.1.50) y la EZVIZ verificada por ping:
1. **Toma A**: grabada desde la consola (`P1-a-take2.mp4`, 40.4 s) → `prepare_clip.sh` →
   `ensayo-g2-tomaA.mp4` (1920x1080, 30 fps CFR, 1212 frames). Circuito completo OK.
2. **Toma B**: corrida live 1:1 con `gdino-tiny-560` + `cr01_cr02_v2_short` sobre OAK-D. Orden
   control-first respetado, `subscribed:true` confirmado antes de disparar media. Alerta CR-01
   real emitida (persona sin casco, severidad `high`), `bus_dropped_events: 0`, cierre 1:1
   (`succeeded`/`stopped`) referenciando el mismo `media_run_id`.
3. **Claqueta de prueba**: primer intento **falló** — la palmada llegó 4.5 s antes de que la
   OAK-D entregara el primer frame (conexión ~9 s), confirmando en carne propia por qué existe
   la regla dura del `starting` (F-DR6, doc 59 §9: nadie actúa hasta que la fuente salga de
   "starting"). Repetido esperando la conexión: la palmada quedó anclada a **222 ms** del
   `capture_wallclock_ms` del frame más cercano — confirma que `t_alert = TTFD +
   t_capture→alert` es reconstruible con un ancla externa (una claqueta física real en el
   rodaje da precisión sub-frame, mejor que el margen de chat de este ensayo).
**Hallazgo de vestuario y sobre-marca `vest` (F-G2.1, con corrida de verificación):** la
campera deportiva del usuario (oscura con franjas amarillas) se detectó como `vest` conf
~0.54 en el **98-100% de los frames** de las tres primeras corridas — CR-02 completamente
suprimida (solo CR-01 disparó). Corrida de verificación **sin la campera** (ropa lisa,
`run_20260723_215516…0d0abb`, 585 unidades): el modelo siguió alucinando `vest` débil
(~0.31) sobre el torso liso durante ~4 min — por encima del umbral de evidencia del motor
(`min_absent_class_confidence: 0.25`), así que el episodio CR-02 siguió sin abrir; cuando la
alucinación cesó (frames 2217+), el episodio abrió, sostuvo los 7000 ms y **CR-02 confirmó**
(`medium`, score 0.56) — las dos alertas (CR-01 + CR-02) en el mismo run, `bus_dropped: 0`.
Lecturas: (a) **el circuito CR-02 live funciona de punta a punta**; (b) la sobre-marca de
`vest` es un fenómeno real del modelo (escena doméstica nocturna, fuera de dominio) que
retrasa o suprime CR-02 — es exactamente lo que las Fases T/P van a caracterizar con
material real, y un caso documentable de falso cumplimiento (P9). **Regla para el rodaje:**
el estado "sin chaleco" se actúa con ropa lisa sin franjas ni colores hi-vis (para que CR-02
sea medible), y se guarda además una toma deliberada con ropa a franjas como caso P9
documentado. Los `helmet` FPs fueron esporádicos (13/463, 11/93) y la persistencia de
4000 ms los filtró: CR-01 confirmó en todas las corridas.

4. **Tiempos de setup por escena** (medidos, no estimados):
   - control→`subscribed:true`: <1 s
   - media→primer frame OAK-D (conexión): **8.3 s** (consistente con el ~9 s de doc 61)
   - ventana mínima de actuación para confirmar CR-01: ≥4 s sostenidos (`confirm_after_ms`)
   - `stop()`→ambos planos en terminal: 6.4 s
   - **overhead mecánico fijo por toma live: ~15 s** (fuera del tiempo de actuación) — con
     ~12-15 episodios del shot-list son ~3-4 min acumulados en el día, manejable.

**G5 — Checklist del día**, recorrida en este ensayo (disco 901 GB libres, servicios
levantados cada uno desde la raíz de su repo, orden EBE control-primero verificado dos veces,
consola up en `:5173`/BFF `:8090`, ambas cámaras responden ping) — falta ejecutarla completa
recién **el día del rodaje** (ítems 7-8 son por escena/al cierre, no aplican a un ensayo sin
actores):
1. Disco: ≥20 GB libres en el destino de `datasets-videos/raw/` (y ojo tmpfs de `/tmp`).
2. Servicios **desde la raíz de su repo** (trampa doc 65: artefactos fuera de lugar).
3. `EOVRT_MODEL_REF=grounding-dino/gdino-tiny-560`; smoke `/healthz`+`/readyz`.
4. Orden EBE: control-plane primero (`subscribed:true`), media después; terminal `succeeded`;
   409 al reintentar = reusar el run activo.
5. Consola: Ctrl+Shift+R tras cualquier cambio de frontend; entrar por `/` (deep-link 404).
6. Cámaras: ping a **169.254.31.137** (OAK-D) y **169.254.31.140** (EZVIZ) — ambas con IP
   estática **link-local** desde 07-25. Con el cable directo PC→switch PoE **no hay que
   configurar nada** en la PC (Windows se autoasigna una IP del mismo `/16`) ni apagar el
   Wi-Fi. EZVIZ ~18 fps medidos; preset OAK-D fps 30 → ~22 fps. Detalle y trampas
   (interfaces Wi-Fi/Ethernet separadas del DVR): doc 68 §2.1.
7. Por escena: grabar toma A (esperar fin de `starting` → actuar → cantar el evento) → toma
   B live 1:1 → **antes de desarmar la escena, verificar DOS cosas en el estado del
   control-plane**: `bus_dropped_events=0` **y que la alerta esperada del escenario se
   emitió** (`alerts_count` se ve en caliente en `GET /api/runs/{id}`). Motivo (F-G2.1): la
   sobre-marca de `vest` puede suprimir CR-02 en silencio — una escena P2 live sin su alerta
   CR-02 es una corrida perdida que solo es barata de repetir en el momento. Si la alerta no
   salió: revisar vestuario (¿algo con franjas/colores hi-vis en cuadro?) y repetir la toma.
8. Al cierre: inventario de tomas vs shot-list ANTES de que los colegas se vayan (el doc 59
   §6 define el mínimo por escenario — es más barato repetir en el momento).

## Secuencia (actualizada 2026-07-23: G1-G5 cerrados, solo falta el rodaje en sí)

1. ~~Claude, ya: G1 + B1/B2 del doc 66~~ — **HECHO** (G1 congelado; B1 descartado en
   auditoría, B2/B4/B5 completados con `bench_v3`, doc 66).
2. ~~Usuario + Claude, sesión con cámaras (~1 h)~~ — **HECHO** (G2 ensayo doble toma + G5
   recorrida, misma noche).
3. ~~Usuario: G4~~ — **HECHO** (los 5 repos commiteados y pusheados).
4. **Día del rodaje**: ejecutar G5 completa (ítems 7-8, por escena y al cierre); Claude opera
   los planos y el inventario en vivo. Sin gates técnicos pendientes — lo que falta es
   administrativo (consentimientos, colegas, EPP) y del lado del rodaje mismo.

Del lado del usuario sigue pendiente (fuera del alcance de estos gates): consentimientos
firmados, coordinación de colegas y EPP físico, pasada humana CVAT de los videos de internet,
acta `edir_v1`.
