# 68 — Manual de arranque de la plataforma (live / EBE)

**Fecha:** 2026-07-24. **Propósito:** checklist operativo para levantar la plataforma
completa y dejar lista una corrida en vivo, de cámara a evaluación de alertas.
Fuentes: docs 37 (bus/live), 38 (servicio control-plane), 67 (EBE verificado).

## 0. Precondiciones

- Disco: ≥ 20 GB libres en el destino de grabación/runs.
- **Cada servicio se levanta desde la raíz de su propio repo** (si no, los `runs/`
  quedan fuera de lugar).
- Modelo campeón para live: `grounding-dino/gdino-tiny-560` (doc 64).
- Prompt set congelado: `cr01_cr02_v2_short` (frozen, sha256 en el YAML).
- Pattern set: **`cr01_cr02_v2` siempre, nunca `v1`** (v1 desalinea umbrales con
  `derive_clip_gt` → falsos `missed`, F-DR9).

## 1. Arranque de servicios (en este orden)

```bash
# 1) media-plane (:8080) — el modelo carga UNA vez al startup
cd ~/projects/e-ovrt_media-plane
EOVRT_MODEL_REF=grounding-dino/gdino-tiny-560 make serve
make smoke        # /healthz + /readyz deben responder ok/ready

# 2) control-plane (:8081) — sin modelo, readyz siempre ready
cd ~/projects/e-ovrt_control-plane
.venv/bin/eovrt-control serve --port 8081

# 3) webconsole — BFF (:8090) y frontend (:5173)
cd ~/projects/e-ovrt_experimental-setup/webconsole/backend
.venv/bin/uvicorn eovrt_webconsole.app:create_app --factory --port 8090
cd ../frontend && npm run dev
```

Tras cambios de frontend: Ctrl+Shift+R en el navegador. Entrar por `/`
(deep-links directos dan 404 en dev).

## 2. Cámaras

| Cámara | IP | Nota |
|---|---|---|
| RTSP DVR (EZVIZ) | **169.254.31.140** | estática en su **interfaz Ethernet**; medido 1920×1080, ~18 fps |
| OAK-D Pro PoE | **169.254.31.137** | estática en bootloader; preset `fps: 30` → ~22 fps; tarda ~9 s en conectar |

### 2.1 Red directa (sin router) — configuración del rodaje

Montaje: **switch PoE** entre la PC y las cámaras. El switch cumple dos funciones y las
dos son necesarias: **alimenta la OAK-D** (es PoE 802.3af — el puerto Ethernet de la PC
no entrega corriente, con un cable común la cámara ni enciende) y **reparte** el único
puerto Ethernet físico de la PC entre los dos dispositivos.

**Las dos cámaras tienen IP estática en el rango link-local `169.254.0.0/16`**
(configuradas 2026-07-25). La elección es deliberada: **es el mismo rango que Windows se
autoasigna cuando no hay DHCP**, así que con el cable directo puesto, la PC y las cámaras
quedan en la misma subred **sin configurar absolutamente nada**:

- **No hace falta fijar IP a mano** en la interfaz Ethernet (requeriría permisos de
  administrador, que WSL no tiene).
- **No hace falta apagar el Wi-Fi**: al no compartir subred con la LAN doméstica/de obra,
  no hay ruteo ambiguo. **El Wi-Fi sigue dando internet en paralelo** (verificado).
- **No puede colisionar** con la red del lugar del rodaje, sea cual sea.

Si la IP que Windows se autoasigna coincidiera con la de una cámara, el propio protocolo
APIPA (RFC 3927) lo detecta por ARP y elige otra: verificado en la práctica el 07-25,
Windows tomó `169.254.235.239` sin intervención.

**Historial de IPs** (por si algo no responde y hay que rastrearlo): OAK-D `192.168.1.50`
(DHCP) → `192.168.1.50` (estática) → **`169.254.31.137`**. DVR: `192.168.1.5` (DHCP) →
`192.168.1.51` (estática) → **`169.254.31.140`**. Backups del bootloader de la OAK-D en
`e-ovrt_experimental-setup/cameras/oakd_bootloader_backup_*.json`.

Pasos en la PC, antes de conectar:

1. **Conectar el cable** PC → switch PoE → cámaras. Nada más.
2. Esperar a que la interfaz `Ethernet` tome IP en `169.254.x.x` (unos segundos; Windows
   la asigna solo al no encontrar DHCP).
3. **Bajar las VPN**: NordLynx, WireGuard (`sllamosas_*`) y ZeroTier pueden capturar rutas.
4. Verificar: `ping 169.254.31.137` (OAK-D) y `ping 169.254.31.140` (DVR).
5. **Si Windows llega a la cámara pero WSL no**, es la caché de red de WSL tras el cambio
   de interfaz: `wsl --shutdown` desde PowerShell y reabrir la terminal. Después de eso
   hay que **volver a levantar los tres servicios** (§1). Hacer este paso ANTES de
   arrancar los servicios, no en medio del rodaje.

> **✎ 2026-08-05 — el paso 5 NO alcanza si WSL está en modo NAT (doc 91).** El
> `wsl --shutdown` limpia caché de rutas, pero **no cambia el modo de red**. En NAT (el
> default) WSL solo ve su subred `172.22.0.0/20` y **nunca** va a alcanzar el
> link-local `169.254.0.0/16`, por más reinicios que se hagan.
>
> **Diagnóstico correcto — el `ping` MIENTE:** en NAT, la OAK-D "responde" al ping pero
> la respuesta viene `via 172.22.0.1` con **`ttl=63`** (es el gateway de Windows, no la
> cámara) y sus puertos dan *Connection refused*. Verificar siempre con
> `ip route get 169.254.31.137` (debe salir `dev eth1`, **sin** `via`), `ttl=64` en el
> ping, y para la OAK-D el chequeo definitivo:
> ```bash
> cd e-ovrt_media-plane && .venv/bin/python -c "
> import depthai as dai
> with dai.Device(dai.DeviceInfo('169.254.31.137')) as d: print(d.getDeviceName(), d.getMxId())"
> ```
>
> **Fix:** en `C:\Users\<user>\.wslconfig` poner `[wsl2]` + `networkingMode=mirrored` y
> `wsl --shutdown`. WSL levanta `eth1` con `169.254.x.x` y rutea directo. Requiere
> WSL ≥ 2.0.0 y Windows 11 22H2+. **Caveat:** el modo espejo cambia la red de WSL
> globalmente; el punto de fricción conocido es Docker (`infra/twonode/`). Se revierte
> vaciando el archivo y repitiendo el shutdown. Si el archivo aparece **vacío (0 bytes)**
> es probablemente una regresión de entorno: el 2026-07-25 el live funcionó con estas
> mismas IPs, así que el modo espejo estaba puesto.

> **Trampa del DVR (mordió el 07-25):** el DVR EZVIZ tiene **interfaces Wi-Fi y Ethernet
> con configuración de red separada**. Si se edita la IP en la pantalla equivocada, el
> equipo sigue respondiendo en su IP vieja **por Wi-Fi** — lo que parece "la config no se
> guardó" o "revirtió sola", cuando en realidad el puerto Ethernet nunca se tocó. La IP
> del preset es la de la **interfaz Ethernet**, que es la que va al switch PoE. Su UI web
> está cerrada: solo expone `554` (RTSP) y `8000` (SDK), la config se hace desde el menú
> local del equipo (monitor + mouse).

- `ping` a ambas antes de arrancar. **Si falla el primero, reintentar** (la interfaz
  tarda en levantar; pasó el 2026-07-25 y dio un falso negativo).
- **Desde WSL, el descubrimiento por broadcast de DepthAI no funciona** (el UDP no
  cruza el NAT): `getAllAvailableDevices()` devuelve vacío aunque la cámara esté
  perfecta. **Siempre por IP explícita**, que es lo que hace el preset. No buscarla.
- Presets en `e-ovrt_experimental-setup/cameras/*.yaml` (gitignorado: credenciales
  RTSP en claro). El `{plugin, config}` del preset mapea 1:1 al bloque `ingest`.
- Encuadre: usar el preview de la consola (`/cameras`). Preview y run son
  mutuamente excluyentes (409 `preview_active` / `run_active`).

## 3. Lanzar la corrida live (EBE) — orden NO negociable

Desde la consola (`/experiments`, manifiesto con `runs.control.mode: live`) o a mano:

1. **Control-plane PRIMERO**: `POST :8081/api/runs` con
   `{"mode": "live", "config": {…, input.type: bus}}`. El 201 implica que el
   `BusSource` ya está suscripto (construirlo ES suscribirse). Config de
   referencia: `e-ovrt_control-plane/configs/live_ebe_cr01_cr02.yaml`.
2. **Confirmar suscripción**: `GET :8081/api/runs/current` → `subscribed: true`.
   Si no, abortar sin tocar el media-plane (PUB/SUB descarta en silencio lo
   publicado antes del SUBSCRIBE).
3. **Media-plane DESPUÉS**: `POST :8080/api/runs` con `bus: {enabled: true}`,
   `ingest` del preset de cámara, `prompts` = `cr01_cr02_v2_short`, y
   `ingest.config.source_id = <clip_id>` (contrato con el GT).
4. **Cierre 1:1**: al frenar el run de media (`POST :8080/api/runs/{id}/stop` o
   fin de fuente), emite `run.lifecycle.v1/run_finished` y el control cierra solo
   (fallback: polling o `idle_timeout_s: 300`).

**Antes de desarmar la escena**: verificar en el `summary.json` del control
`bus_dropped_events == 0` y que la alerta esperada se emitió.

## 4. Artefactos

- Media: `e-ovrt_media-plane/runs/<id>/` — `detections.jsonl` (verdad del bus),
  `metrics.jsonl`, `summary.json`, `dropped_units.jsonl`.
- Control: `e-ovrt_control-plane/runs/<id>/` — `alerts.jsonl`, `alerts.csv`,
  `pattern_events.jsonl`, `pattern_progress.jsonl`, `effective_config.yaml`,
  `summary.json` (`media_run_id`, `scenario: EBE`, `bus_dropped_events`, `degraded`).

## 5. Evaluación de alertas (offline, tras la corrida)

```bash
cd ~/projects/e-ovrt_control-plane
.venv/bin/eovrt-control evaluate-alerts \
    runs/<control_run>/alerts.jsonl <ground_truth.json> \
    -o temporal_evaluation.json \
    --detections ../e-ovrt_media-plane/runs/<media_run>/detections.jsonl \
    --patterns configs/patterns/cr01_cr02_v2.yaml
```

- `--detections`/`--patterns` habilitan SDR y TTFD; sin ellos solo P/R/FAR-hora.
- `--patterns` recibe el **YAML de patrones**, nunca `pattern_events.jsonl`.
- GT v2 = episodios en ms de `derive_clip_gt` (video-gt-lab); el matching casa
  por `source_id == clip_id`. Estado actual del banco: `gt_preliminary`.

## 6. Trampas conocidas (todas ya mordieron)

1. Invertir el orden de los POST pierde eventos iniciales sin error visible.
2. Pattern set v1 → falsos `missed` silenciosos. Siempre v2.
3. Nunca cerrar un socket ZeroMQ desde otro hilo con `recv_multipart` en vuelo
   (SIGABRT); usar `request_stop()`.
4. Servicios levantados fuera de la raíz de su repo → artefactos perdidos.
5. `--patterns` con el JSONL de eventos revienta la evaluación.
6. OAK-D viene de fábrica con IP estática 169.254.1.222 (no DHCP).
7. **`warmup_frames` es por-run y su default es `0`** (`schemas.py:218`): NO viene
   del preset de cámara — el preset trae solo `{plugin, config}` de la cámara, y el
   campo se escribe a mano en el paso 1 de "Nueva corrida". **Si se deja vacío, los
   primeros frames de la OAK-D (exposición sin converger, cuadro oscuro) entran al
   pipeline** y contaminan el arranque de la toma. Valor de referencia: **20** (a los
   ~13 fps reales de la OAK-D ≈ 1,5 s). Solo aplica a fuentes vivas: ponerlo en una
   fuente `video_file` es error de validación, no se ignora en silencio.
8. **Un run live del control NO se puede cancelar por API.** No hay endpoint de
   stop/cancel: `DELETE /api/runs/{id}` sobre un run activo devuelve **409** y
   `shutdown()` solo corre al apagar el servicio. Si se disparó el control (paso 1) y
   el media nunca arrancó, quedan **dos salidas**: (a) la del guion — **reusar el
   `active_run_id`** y disparar el media contra ese run (es lo normal y lo barato: el
   SUB ya está suscripto); (b) si hay que cambiar la config del control, esperar el
   **`idle_timeout_s` = 300 s** (verificado 2026-07-25: cierra a los 300 s exactos con
   `BusIdleTimeout`) o reiniciar el control-plane. **En el rodaje, siempre (a).**

### Trampas nuevas del día de rodaje (2026-07-25 — todas mordieron; detalle: doc 71 §3)

9. **"Nueva corrida" (Composición) lanza SOLO el plano de medios** — su payload ni
   tiene campo `bus`; el control-plane nunca ve los eventos y la corrida sale **sin
   ninguna alerta, sin error visible**. Costó dos pruebas (r1, rt1) antes de
   detectarse. Toda corrida de plataforma completa va por **Experimentos** (el runner
   hace control-first + `SubscriptionNotConfirmed`). La UI ahora tiene
   **`+ Nuevo experimento`** en el sidebar para crear la config sin editar YAML.
10. **El BFF en :8090 sirve el `dist/` del frontend si existe** — un build viejo tapa
    todos los cambios de UI aunque el dev server (:5173/:5199) esté al día, y ni el
    modo incógnito lo salva. Regla: **cambio de frontend ⇒ `npm run build`** antes de
    mirar por :8090. El BFF tampoco recarga Python solo: cambio de backend ⇒
    reiniciar el proceso uvicorn.
11. **Detener una corrida da `stopped`, y la consolidación NO corre con `stopped`.**
    El fix del 2026-07-25 hizo que `stopped` sea terminal para el runner (antes el
    experimento quedaba "corriendo" 300 s y bloqueaba el próximo lanzamiento con "hay
    un experimento en curso"), pero `ok` exige `succeeded` en ambos planos: una toma
    live cortada a mano **no genera dir consolidado ni report paraguas** — los datos
    quedan completos en los `runs/` de cada plano. Decisión pendiente si un `stopped`
    limpio debería consolidar.
12. **El modelo es del proceso, no del run** (`EOVRT_MODEL_REF` al arrancar el
    media-plane). Cambiar de modelo = bajar y relevantar el servicio. Tras la
    comparación GDINO/YOLOE del 2026-07-25 el media-plane quedó apagado con
    `yoloe/yoloe-26x`: **al relevantar, volver a
    `EOVRT_MODEL_REF=grounding-dino/gdino-tiny-560`** (campeón, doc 64).
13. **La card Alertas del detalle de experimento carga UNA vez y no se refresca** —
    mirarla durante la corrida muestra "Sin alertas." o `error 404` aunque la alerta
    ya haya saltado. El estado en vivo real es el **banner de riesgo activo** (rojo,
    arriba, se enciende al confirmar y se apaga al resolver — nuevo 2026-07-25);
    para la tabla de alertas, **recargar la página** cuando ambos planos estén
    terminales.
14. **`pytest` del backend de la consola deja basura en `experimental-setup/runs/`**
    (dirs `exp_*_orq_*` / `gate_orq` de la suite de orquestación, ~5 por corrida de
    suite). No romper la cabeza buscando qué experimento fue: si el slug es `orq_*`,
    es un test. Pendiente aislar la suite y limpiar (~74 dirs del 2026-07-25).
