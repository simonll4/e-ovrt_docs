# 91 — Humo EBE en vivo tras los cambios: regresión + G1 en vivo

- **Fecha:** 2026-08-05 (madrugada, con hardware real).
- **Qué es:** dos humos EBE en vivo con la OAK-D. **(A)** regresión del camino live tras
  todos los cambios del control-plane de la jornada 83–90 — la última corrida live real
  había sido el **2026-07-25**. **(B)** G1 (identidad por sujeto) en vivo, que cierra el
  residuo declarado en el doc 90 D-90.3.
- **Estado:** **ambas VERDES.**

## 1. Por qué la regresión era el riesgo principal, no el residuo

Desde la última corrida live, el control-plane cambió en el **camino caliente**:
`c1cbb56` (3 fixes del evaluador) y sobre todo `5327080`, que metió el **despacho por
estrategia dentro de `pattern_engine.process()`** — usado por replay **y** por live. Más
lo de esta jornada sin commitear: el decorador de fuente, el fix de `prepare_run` y el
despacho del derivador de SDR/TTFD. Todo eso estaba cubierto por 312 tests unitarios,
pero **la integración EBE (bus, suscripción, threading del servicio, semántica 1:1) no
se había ejercitado**. Es exactamente el tipo de cosa que se rompe en silencio.

## 2. Resultado

| | Fase A (regresión, `cr01_cr02_v2`) | Fase B (G1, `cr01_cr02_v2_subject`) |
|---|---|---|
| Unidades | 150 | 160 |
| `units_failed` / `errors_count` | 0 / 0 | 0 / 0 |
| **`bus_dropped_events`** | **0** | **0** |
| Degradado | `False`, sin causas | `False`, sin causas |
| Alertas | 2 (CR-01 + CR-02) | 2 (CR-01 + CR-02) |
| **`subject_key`** | `CR-01:smoke_ebe` | **`CR-01:smoke_ebe:subject_001`** |

**El contraste de la última fila es toda la evidencia de G1 en vivo**: bajo escena la
clave es `pattern:source`; bajo sujeto incorpora el `track_id` que el decorador de
fuente produce **sobre el bus**, sin que el media-plane emita nada nuevo. Y el invariante
que hacía falta descartar: **`no_track_id` NO aparece** en las causas de degradación —
si apareciera, el motor habría degradado a escena y la fase B habría medido G0 creyendo
medir G1.

Con esto, la afirmación de la adenda de ADR-002 —*"cubre DBE y EBE/live por igual"*—
deja de estar sostenida solo por tests unitarios.

## 3. Lo que costó llegar: la red de WSL (trampa nueva, y grande)

**Ninguna cámara era alcanzable desde WSL**, y el modo en que fallaba era engañoso:

- El DVR RTSP (`169.254.31.140`) daba `No route to host` — inequívoco.
- La OAK-D (`169.254.31.137`) **respondía al ping** — y era **falso**: la respuesta venía
  `via 172.22.0.1` (el gateway NAT de WSL) con `ttl=63`, y sus puertos daban
  *Connection refused*. Quien contestaba era Windows, no la cámara. **Quedarse en el
  ping habría hecho arrancar la campaña contra una cámara inexistente.**

**Causa raíz:** `C:\Users\<user>\.wslconfig` estaba **vacío (0 bytes)** ⇒ WSL en modo
**NAT**, donde solo ve su subred `172.22.0.0/20` y **no puede alcanzar el rango
link-local `169.254.0.0/16`** en el que viven las dos cámaras (doc 68 §2.1).

**El paso 5 del doc 68 no alcanza.** Ese paso dice que si Windows llega y WSL no, es
caché de red y se arregla con `wsl --shutdown`. **Se ejecutó y no cambió nada**: el
shutdown limpia caché de rutas, pero **no cambia el modo de red**. En NAT, WSL nunca va
a ver el link-local, por más reinicios que se hagan.

**Fix:** `networkingMode=mirrored` en `.wslconfig` + `wsl --shutdown`. Tras eso WSL
levanta `eth1` con `169.254.235.239/16` —la misma IP que el doc 68 registra que Windows
se autoasigna— y la ruta a la cámara va **directa por `eth1`, sin gateway**. Verificación
correcta: `ping` con **`ttl=64`** (2,37 ms) y `dai.Device('169.254.31.137')` devolviendo
`OAK-D-PRO-POE`, mxid `194430105168741300`.

Requiere WSL ≥ 2.0.0 (acá 2.7.3) y Windows 11 22H2+ (acá 24H2). **Caveat declarado:** el
modo espejo cambia la red de WSL globalmente; el punto de fricción conocido es Docker
(binding de puertos y `localhost`), y este proyecto tiene `infra/twonode/`. Se revierte
vaciando el archivo y repitiendo el shutdown.

**Casi seguro es una regresión de entorno, no algo nuevo:** el 2026-07-25 las corridas
live funcionaron desde WSL con estas mismas IPs link-local, así que el `.wslconfig`
tenía el modo espejo y en algún momento quedó truncado a 0 bytes.

## 4. Verificación de cámara antes de gastar la sesión

Antes de los humos se hizo una corrida corta de 18 s solo de captura: **31 unidades, 78
detecciones (60 `person` + 18 `helmet`)** y se miró un preview real
(`datos/91-smoke-ebe-evidencia/encuadre_camara.jpg`): sujeto detectado con
**`person 0.89`**, bien encuadrado. Se observó un **`helmet 0.31` espurio** en el borde
inferior del cuadro — irrelevante para CR-01 porque cae **fuera de la región
`upper_body`** (que llega al 45% de la altura de la persona), y en efecto CR-01
confirmó en ambas fases.

## 5. Dos bugs de tooling corregidos en el camino

Ninguno es de la plataforma, pero los dos habrían dado veredictos falsos:

1. **`ingest.config` de la OAK-D usa `url`, no `ip`.** Con `ip` el servicio devuelve
   **422** con la lista de campos válidos (buen mensaje). El preset
   `cameras/oak_d_lab.yaml` ya lo tenía bien: el error fue no mapear 1:1 desde el preset,
   que es justo lo que el doc 68 dice que hay que hacer.
2. **`outputs.base_dir: ../runs` resuelve relativo al ARCHIVO DE CONFIG**, no al cwd. El
   script buscaba el directorio de la corrida en `projects/runs/` y reportó
   *"NO se creó directorio de control run"* cuando la fase A **había funcionado
   perfecto**. Un veredicto rojo sobre una corrida verde.

## 6. Qué queda

El residuo de D-90.3 está **cerrado**: G1 funciona en vivo, con evidencia, no solo en
DBE. La adenda de ADR-002 puede ratificarse con esto a la vista.

Evidencia cruda: `datos/91-smoke-ebe-evidencia/` (summaries y alerts de ambas fases,
preview del encuadre). Scripts: `datos/91-arrancar-servicios.sh` (levanta ambos
servicios cada uno desde la raíz de su repo y espera ready) y
`datos/91-smoke-ebe-post-cambios.py` (orden EBE no negociable: control primero, cuyo 201
implica suscripción, y media después con `bus.enabled`).
