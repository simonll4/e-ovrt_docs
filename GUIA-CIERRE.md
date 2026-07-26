# Guía de cierre — tu checklist hasta la defensa

Documento vivo, **sin número** (no forma parte de la serie `operacion/NN-`), pensado para
que lo abras, vayas tachando, y cada ítem te mande al documento con el detalle completo para
ejecutarlo. Última actualización: 2026-07-25.

**Cómo usarlo:** marcá `[x]` a medida que cerrás cada punto. El orden de la lista es el orden
recomendado (hay dependencias reales entre algunos ítems, marcadas donde corresponde). Si en
algún momento perdés el hilo de todo el proyecto, `docs/00-indice.md` es el índice completo y
`docs/operacion/62-plan-maestro-experimentos.md` es el plan metodológico entero.

---

## Ya está todo cerrado (nada que hacer acá)

No hace falta tocar nada de esto — está verificado (auditoría de cierre 2026-07-23, más lo
cerrado el 07-24), pero si querés el detalle de cómo se llegó, cada ítem linkea a su doc:

- ✅ **Modelo elegido**: `grounding-dino/gdino-tiny-560`, con criterio pre-registrado y
  confirmado en 2 benchs independientes → `docs/operacion/64-resultados-s1-s2-seleccion-modelos.md`
- ✅ **Bench de imágenes ampliado y congelado**: 6.477 imgs, 3 fuentes → `docs/operacion/66-plan-ampliacion-bench-imagenes.md`
- ✅ **Config del rodaje y del carril live**: prompts congelados, pattern set correcto → `docs/operacion/59-guion-grabacion-bloque-a.md` §9
- ✅ **EBE (corrida live) probada de punta a punta** con el modelo elegido → `docs/operacion/65-l0-ensayo-ebe-tramo1.md`
- ✅ **Plataforma de medición completa** (persistencia, métricas, matching, FAR) → `docs/operacion/62-plan-maestro-experimentos.md` §1-2
- ✅ **Ensayo con cámaras (G2)**: circuito completo probado con la OAK-D real —
  toma A (consola→clip) OK, toma B (live 1:1) con alerta CR-01 real y
  `bus_dropped_events: 0`, claqueta anclada a 222 ms tras corregir la regla del `starting`,
  tiempos de setup medidos (~15 s overhead mecánico/toma live) → `docs/operacion/67-preparacion-rodaje-y-ebe.md` sección G2
- ✅ **Manual de arranque de la plataforma** (2026-07-24): un solo documento para levantar
  todo el día del rodaje — orden de servicios, cámaras, orden EBE no negociable, artefactos,
  evaluación y las 6 trampas conocidas → `docs/operacion/68-manual-arranque-plataforma.md`
- ✅ **Consola lista para operar el rodaje** (2026-07-24): la pantalla "Nueva corrida" quedó
  en 3 pasos (Fuente / Prompts / Lanzar), las fuentes live eligen **preset de cámara guardado**,
  hay **preflight de plataforma** que deshabilita *Lanzar* si un plano está caído (con el motivo
  a la vista, y gate 503 en el backend — antes un control-plane caído moría en silencio dentro
  del runner), campo **`warmup_frames`** para descartar los primeros frames de la OAK-D hasta
  que asiente la exposición, y **nombre opcional de corrida** (usalo con el nombre de la escena:
  `P1-toma2-live` — así la hoja de registro se lee sola en la lista de runs)

---

## Verificación pre-rodaje (2026-07-25, plataforma levantada de cero)

Se levantó la plataforma completa desde cero y se corrió el circuito EBE de punta a punta
**con el modelo campeón y la config oficial del rodaje**, usando el video del ensayo G2 en
lugar de la cámara. **Resultado: verde.**

| Verificado | Resultado |
|---|---|
| media-plane `:8080` | `ready`, `grounding-dino/gdino-tiny-560` en **CUDA**, half precision |
| control-plane `:8081` | `ready` |
| BFF `:8090` + SPA | `/api/health` ok, SPA servida, `npm run build` limpio (tsc sin errores) |
| **Preflight de la consola** | `ready: true`, `blockers: []` — el gate nuevo funciona |
| **Circuito EBE completo** | control→media, `subscribed: true`, **cierre 1:1 `succeeded`/`succeeded`** |
| Paridad de unidades | **2423 = 2423** en ambos planos |
| `bus_dropped_events` | **0**, `degraded: false` |
| Config efectiva | prompt set `cr01_cr02_v2_short`, pattern set `cr01_cr02_v2` ✅ |
| Alerta | **1 × CR-01** con evidencia (`missing_class: helmet`) |
| Artefactos | los 8 del media + los 7 del control, completos |
| `idle_timeout_s` del bus | cierra a los **300 s exactos** (`BusIdleTimeout`), medido |
| Disco | 901 GB libres |

**Dos cosas nuevas quedaron documentadas como trampas** (doc 68 §6, nuevas 7 y 8), porque
las dos pueden morder en pleno rodaje:

- **`warmup_frames` está vacío por default y NO viene del preset de cámara.** Es un ajuste
  **por-run** con default `0`. Si se deja en blanco, los primeros frames oscuros de la OAK-D
  entran al pipeline. **Poner `20` en cada corrida live** (ya está en el paso 5 del
  checklist A→B del guion 59 §7).
- **Un run live del control no se puede cancelar por API** (no hay stop; `DELETE` sobre un
  run activo da 409). Si el control ya está disparado y el media no arrancó, **reusar el
  `active_run_id`** — que es justo lo que el guion ya manda. La alternativa es esperar
  5 minutos o reiniciar el servicio: en rodaje, nunca.

### Segunda pasada: EBE **live con la OAK-D real** (misma noche)

No hizo falta esperar al sitio — la cámara está en la LAN y se verificó el circuito completo
**con hardware real**, siguiendo literal los pasos 4→9 del checklist A→B del guion:

| Paso del checklist | Resultado |
|---|---|
| Conexión DepthAI directa a `192.168.1.50` | **8,1 s**, 1920×1080, ~22 fps en crudo (coincide con los ~9 s documentados) |
| 4 — control primero | `201`, `subscribed: true` |
| 5 — media después, `warmup_frames: 20` | `201`, preset `oak_d_lab` mapeado 1:1 a `ingest` |
| 6 — regla del primer frame | `units_processed > 0` a **t+11 s** |
| 8 — `POST /api/runs/{id}/stop` | **`202`**, terminal en AMBOS planos en **2 s** (media `stopped`, control `succeeded`) |
| 9 — `bus_dropped_events` | **0**, `degraded: false` |
| 9 — paridad 1:1 | **73 = 73** unidades |
| 9 — alertas | **2 emitidas**, pattern set `cr01_cr02_v2` |

> **Nota de luz:** la corrida dio **~1,6 fps** contra los ~3,3 fps del doc 65 — se hizo de
> noche, con poca luz, y la OAK-D alarga la exposición. Las alertas salieron igual (a 1,6 fps
> la ventana de 4000 ms todavía tiene ~6 frames), pero **el margen se achica**: si el día del
> rodaje hay poca luz, vale iluminar la escena antes que tocar umbrales.

> **Descubrimiento por broadcast NO funciona desde WSL** (el UDP no cruza el NAT):
> `getAllAvailableDevices()` devuelve vacío. **Hay que conectar por IP explícita**, que es
> exactamente lo que hace el preset `oak_d_lab`. No es un problema — pero si alguien intenta
> "buscar la cámara" en vez de usar el preset, no la va a encontrar.
> Si el primer `ping` falla, reintentar: la interfaz tarda en despertar (pasó acá).
> *(Las IPs de esta pasada y la siguiente quedaron superadas por la cuarta — ver abajo.)*

### Tercera pasada: preparación de la red directa del rodaje (2026-07-25)

Mañana las cámaras van por **cable directo a la PC vía switch PoE**, sin router. Eso
destapó un bloqueante que habría costado la mañana:

- **La OAK-D estaba en modo DHCP** (`isStaticIPV4: false`): el `192.168.1.50` se lo daba
  el router. Sin router no habría tomado IP, habría caído a APIPA y el preset habría
  fallado. **Corregido**: se flasheó la estática con los **mismos valores**
  (`192.168.1.50 / 255.255.255.0 / gw 192.168.1.1`), `isStaticIPV4: true` verificado
  releyendo la config tras el reinicio, y **se revalidó el EBE live completo** después
  del flash (72=72 unidades, `bus_dropped_events: 0`, 2 alertas). Backup de la config
  previa en `cameras/oakd_bootloader_backup_pre_static_20260725.json`.
- **El switch PoE no es opcional**: la OAK-D es PoE 802.3af y el puerto Ethernet de la PC
  no entrega corriente. Además la PC tiene **un solo** puerto físico, así que el switch
  también es lo que permite colgar las dos cámaras.
- **El DVR EZVIZ pasó a `192.168.1.51` estática** (lo configuraste desde su menú; su UI
  web está cerrada, solo expone `554` y `8000`). Verificado: responde al ping, RTSP
  1920×1080 a **~18 fps** (mejor que los ~15 que decía la doc), la vieja `.5` quedó libre
  y **no hay IP duplicada**. Se actualizó el preset `rtsp_dvr_1.yaml` y **se revalidó el
  EBE completo con esa fuente**: 115=115 unidades, `bus_dropped_events: 0`, 2 alertas.

### Cuarta pasada: link-local — la red del rodaje queda con **cero configuración** (07-25)

La solución anterior (subred `192.168.1.0/24` en el cable) funcionaba pero exigía **dos
comandos como administrador y apagar el Wi-Fi** cada vez. Se reemplazó por algo mejor:
**ambas cámaras pasaron a IP estática dentro de `169.254.0.0/16`** — el mismo rango que
Windows se autoasigna cuando no encuentra DHCP.

| | IP final | Verificado |
|---|---|---|
| OAK-D Pro PoE | **169.254.31.137** | bootloader `isStaticIPV4: true`; DepthAI conecta en 9,0 s; 1920×1080 @ ~21,8 fps |
| DVR EZVIZ (RTSP) | **169.254.31.140** | ping + `554`/`8000` abiertos; RTSP 1920×1080 @ ~18 fps |

Con el cable puesto, **no hay que configurar nada**: Windows tomó `169.254.235.239` solo
(distinta de las cámaras — el propio APIPA/RFC 3927 detecta el conflicto por ARP y elige
otra), **el Wi-Fi sigue arriba con internet en paralelo**, y no hay forma de que colisione
con la red del lugar del rodaje. Sin permisos de administrador, sin interfaces apagadas.

**La cámara RTSP quedó validada para el rodaje completo, no solo para el circuito EBE:**

| Verificación | Resultado |
|---|---|
| EBE live 30 s | **158 = 158** unidades, `bus_dropped_events: 0`, 1 alerta, cierre 1:1 |
| **EBE live 90 s** (estabilidad, duración de toma real) | **437 = 437** unidades, **0 drops**, 2 alertas |
| **Grabación toma A** (`POST /api/recordings`) | 1920×1080, `truncated: false`, **`suspected_substream: false`** ← la trampa del guion §8 |
| Sidecar `.rec.json` | completo: `measured.fps/resolution`, `started_wallclock_ms`, **sha256**, y **sin credenciales RTSP en claro** |
| MP4 resultante | 217 frames legibles, 1080p |
| Preview de encuadre | `201` → `streaming` → `204` limpio |

> **Trampa nueva del DVR, y costó rato encontrarla** (doc 68 §2.1): tiene **interfaces
> Wi-Fi y Ethernet con config de red separada**. Al editar la IP en la pantalla equivocada,
> el equipo seguía respondiendo en su IP vieja **por Wi-Fi**, lo que se leía como "la
> config revirtió sola". El preset apunta a la IP de la **interfaz Ethernet**, que es la
> que va al switch PoE.

**Las dos cámaras quedan con IP estática link-local y ambas revalidadas de punta a punta.
No queda nada de red por configurar mañana: se conecta el cable y funciona.**

> Único punto sin probar: las **dos cámaras conectadas al switch simultáneamente** (se
> probaron de a una, intercambiando el cable). No hay motivo para que falle —IPs distintas
> en la misma subred— pero conviene hacer el `ping` a ambas apenas se arme el montaje.

Procedimiento completo de la PC (IP fija, Wi-Fi off, VPNs abajo): **doc 68 §2.1**.

**Se reconfirmó F-G2.1 con material real**: en la corrida de smoke, `vest` se marcó **2430
veces contra 2425 de `person`** — casi un chaleco por frame, más que personas en cuadro.
La sobre-marca de `vest` está viva y es la causa de que **CR-02 pueda no alertar en P2**.
Es exactamente el chequeo del paso 9 del checklist.

---

## Lo que falta — en orden

### 1. [ ] Pasada humana en CVAT — los 14 videos de internet

**Qué es:** corregir el GT preliminar de los videos que ya tenemos descargados. Esto
**desbloquea la Fase T sola**, sin esperar al rodaje — es lo más barato que podés hacer para
destrabar evaluación real.

**Detalle completo (paso a paso, con comandos):**
`docs/operacion/55-como-continuar.md`, **PASO 1** (probar CVAT con el clip que ya está, medio
día) y **PASO 2** (reemplazar el GT preliminar por el tuyo).
Guía técnica de la herramienta: `e-ovrt_datasets/datasets-videos/GUIA-CVAT.md` (cómo levantar
CVAT con Docker, protocolo de corrección) y el complemento conceptual
`e-ovrt_datasets/datasets-videos/docs/etiquetado-cvat.md` (qué significa cada track/atributo).

---

### 2. [ ] Consentimientos + coordinar colegas + EPP físico

**Qué es:** lo administrativo del rodaje — consentimientos firmados **antes** de grabar (no
después), coordinar quién actúa, y tener casco/chaleco reales disponibles para las tomas
"cumplidoras".

**Detalle completo:** `docs/operacion/59-guion-grabacion-bloque-a.md` (el guion entero da el
contexto de qué se graba y por qué).

---

### 3. [ ] Ejecutar el rodaje (día completo, con tus colegas)

**Qué es:** la jornada de grabación en sí — el shot-list completo (P1 a P9), con la config ya
cerrada y las corridas EBE live embebidas. Cada escena se hace **dos veces, en orden fijo
A→B**: la **toma A grabada** es el material re-corrible (sobre ella corre después todo lo
offline, infinitas veces) y la **toma B live** produce las métricas que solo existen en vivo
(`t_capture→alert`, salud del bus) y **no se pueden regenerar** — por eso una toma B que sale
mal se repite en el momento.

**Detalle completo:** `docs/operacion/69-guion-operativo-rodaje.md` — **es el único
documento que hace falta llevar a la obra.** Está escrito para el equipo real (3 personas,
2 cascos, 2 chalecos, 1–2 personas en cuadro) y es autocontenido: roles, inventario,
arranque de la plataforma, las 5 reglas de oro, el procedimiento toma A / toma B, el
shot-list reordenado en 4 bloques por vestuario, las verificaciones antes de desarmar cada
escena, la hoja de registro, una tabla de troubleshooting y el checklist de cierre.

Los otros tres quedan como respaldo, no hace falta abrirlos durante la jornada:
`68-manual-arranque-plataforma.md` (detalle técnico del arranque y las 8 trampas),
`59-guion-grabacion-bloque-a.md` (por qué existe cada escena y de dónde salen las
duraciones) y `67-preparacion-rodaje-y-ebe.md` §G5 (estado de los gates).

> **Antes de desarmar cada escena, dos verificaciones, no una**: `bus_dropped_events = 0`
> **y** que la alerta esperada se emitió (P1 → CR-01 a ~4 s; P2 → CR-02 a ~7 s; **P3 → ninguna**).
> Motivo F-G2.1: la sobre-marca de `vest` puede suprimir CR-02 en silencio — si P2 no alertó,
> revisá el vestuario (¿franjas o colores hi-vis en cuadro?) y repetí la toma B ahí mismo.

> Depende de 1 y 2 de esta lista.

---

### 4. [ ] Acta `edir_v1` (ahora es solo revisar y aprobar, ~10 min)

**Qué es:** congelar los prompt sets del experimento E-DIR vs E-IND (Fase D). **El borrador
ya existe** (2026-07-24): `e-ovrt_experimental-setup/prompts/edir_v1.yaml`, construido
literal desde la tabla de ejes del doc 12 §2.2 (negación, especificidad, estado observable,
template diagnóstico — 8 formulaciones, validado contra el schema del media-plane). Tu acta:
leer las 8 frases, ajustar si alguna te parece débil, y aprobar — con eso se pasan a
`status: frozen` (+sha256) **junto con `eind_v1`** (mismo acta, hoy `frozen_pending_review`).
La revisión tuya es requisito metodológico (doc 07 D1.6: mitigación del sesgo del auditor),
no una formalidad. No bloquea nada más — las Fases T y P corren sin esto.

**Detalle completo:** `docs/nucleo/12-diseno-prompts-y-fusion-ehyb.md` §2.2 (construcción y
reglas) y `docs/nucleo/04-diseno-comparativo-estrategias-edir-eind.md` §8 (criterios de
decisión pre-registrados).

---

### 5. [ ] GT en CVAT del material del rodaje (después de grabar)

**Qué es:** la misma tarea que el punto 1, pero sobre las tomas del rodaje propio en vez de
los videos de internet. Con equipo de 3, doble anotación en una porción para medir acuerdo.

**Detalle completo:** `docs/operacion/58-plan-cierre-implementacion-experimentacion.md` §B.3.

---

## Después de esto, lo hago yo (sin que haga falta que intervengas)

Con el punto 1 (CVAT internet) ya alcanza para arrancar la Fase T. El resto de la cadena:

**T** (banco temporal) → **P** (validación de la plataforma) → **D** (E-DIR vs E-IND, si ya
está el punto 4) → análisis de errores → reporte de cierre.

Metodología completa de estas fases: `docs/operacion/62-plan-maestro-experimentos.md` §4-8.
Estado y deuda de implementación pendiente (no bloquea nada, la voy tomando en tiempo
libre): mismo doc, §9.

---

## Mapa rápido si te perdiste

| Necesitás | Doc |
|---|---|
| El panorama completo del proyecto de tesis | `docs/operacion/62-plan-maestro-experimentos.md` |
| Por qué elegimos este modelo | `docs/operacion/64-resultados-s1-s2-seleccion-modelos.md` |
| Cómo quedó armado el bench de imágenes | `docs/operacion/66-plan-ampliacion-bench-imagenes.md` |
| Levantar la plataforma live de cero (servicios, cámaras, orden EBE) | `docs/operacion/68-manual-arranque-plataforma.md` |
| Ejecutar el rodaje paso a paso | `docs/operacion/59-guion-grabacion-bloque-a.md` |
| Checklist operativo del día (disco, servicios, EBE) | `docs/operacion/67-preparacion-rodaje-y-ebe.md` |
| Usar CVAT (herramienta y protocolo) | `e-ovrt_datasets/datasets-videos/GUIA-CVAT.md` |
| Cualquier otra cosa / índice completo | `docs/00-indice.md` |
