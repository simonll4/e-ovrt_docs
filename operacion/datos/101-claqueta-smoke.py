"""Humo claqueta (doc 101 §5) — CAPTURA. La verificación va aparte.

Objetivo: anclar el reloj de pared REAL a los timestamps del pipeline live, para
verificar la identidad `t_alert-system = TTFD + t_capture→alert`
(spec 40 §5.2.2), el stretch que el doc 58 declaró diferible y cuyo ancla el
doc 67 §G2 ensayó (palmada ↔ `capture_wallclock_ms`: 222 ms).

Este script SOLO captura: orquesta la corrida EBE, canta la cuenta regresiva y
registra el instante del beep en wallclock. El análisis lo hace
`101-claqueta-verificar.py` sobre los artefactos, así que se puede iterar la
verificación sin volver a filmar.

NO requiere EPP ni gente: CR-01 se dispara por AUSENCIA de casco, así que basta
una persona a cabeza descubierta.

Orden EBE no negociable (spec 40 §3.2 regla 1): control PRIMERO (el 201 implica
que ya está suscripto), media DESPUÉS con `bus.enabled`. PUB/SUB pierde lo
publicado antes de la suscripción.

Uso:  bash 91-arrancar-servicios.sh      # ambos planos, campeón gdino-tiny-560
      python3 101-claqueta-smoke.py      # este script
"""

import argparse
import json
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

PWSH = "/mnt/c/Windows/System32/WindowsPowerShell/v1.0/powershell.exe"

CONTROL = "http://127.0.0.1:8081"
MEDIA = "http://127.0.0.1:8080"
CP = Path("/home/simonll4/projects/e-ovrt_control-plane")
MP = Path("/home/simonll4/projects/e-ovrt_media-plane")
CAPTURA = Path(__file__).parent / "101-claqueta-captura.json"

PROMPTS = {
    "set_inline": {"id": "cr01_cr02_v2_short", "classes": [
        {"id": "person", "phrasings": {"default": ["person"]}},
        {"id": "helmet", "phrasings": {"default": ["helmet"]}},
        {"id": "vest", "phrasings": {"default": ["vest"]}},
    ]},
    "active_ids": ["person", "helmet", "vest"],
}


def _post(base, path, body):
    req = urllib.request.Request(base + path, method="POST",
                                 data=json.dumps(body).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())


def _get(base, path):
    with urllib.request.urlopen(base + path, timeout=30) as r:
        return json.loads(r.read())


def _voz(texto: str, esperar: bool = False):
    """Habla por los parlantes del host Windows (interop WSL).

    Resuelve el problema real de este humo: el operador está frente a la cámara y
    NO ve la terminal del agente, así que una cuenta regresiva impresa no le llega.
    El audio sí.
    """
    ps = ("$ErrorActionPreference='SilentlyContinue';"
          "Add-Type -AssemblyName System.Speech;"
          "$s=New-Object System.Speech.Synthesis.SpeechSynthesizer;"
          f"$s.Speak('{texto}')")
    p = subprocess.Popen([PWSH, "-NoProfile", "-Command", ps],
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if esperar:
        p.wait()
    return p


def _cue_preciso(target_ms: float, texto_previo: str):
    """Programa el TONO del ancla para un instante ABSOLUTO y devuelve el proceso.

    Por qué así y no `speak(); beep()`: arrancar powershell.exe cuesta cientos de
    ms y hablar dura un tiempo variable, así que tomar el wallclock en Python
    alrededor de esas llamadas corrompería justo lo único que este humo mide.
    Acá PowerShell espera hasta un instante absoluto, y **devuelve por stdout el
    wallclock real en que sonó el tono**: ese valor es el ancla, no una estimación.
    """
    ps = (
        "$ErrorActionPreference='SilentlyContinue';"
        "Add-Type -AssemblyName System.Speech;"
        "$s=New-Object System.Speech.Synthesis.SpeechSynthesizer;"
        f"$s.Speak('{texto_previo}');"
        f"$t=[DateTimeOffset]::FromUnixTimeMilliseconds({int(target_ms)}).UtcDateTime;"
        "while([DateTime]::UtcNow -lt $t){Start-Sleep -Milliseconds 2};"
        "$b=[DateTimeOffset]::UtcNow.ToUnixTimeMilliseconds();"
        "[console]::beep(1100,350);"
        "Write-Output $b"
    )
    return subprocess.Popen([PWSH, "-NoProfile", "-Command", ps],
                            stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                            text=True)


def _frames(media_run_id):
    """[(wallclock_ms, hay_persona)] de la corrida, desde detections.jsonl."""
    det = MP / "runs" / media_run_id / "detections.jsonl"
    if not det.exists():
        return []
    out = []
    with det.open() as fh:
        for line in fh:
            if not line.strip():
                continue
            e = json.loads(line)
            hay = any(d["label"] == "person" and d["confidence"] >= 0.25
                      for d in e.get("detections") or [])
            out.append((e["source"]["timestamp_ms"], hay))
    return out


def _esperar_cuadro_vacio(media_run_id, vacio_s=5.0, timeout_s=100.0):
    """Espera a que LOS DATOS confirmen que no hay nadie en cuadro.

    Por qué es imprescindible: en la toma de las 17:26 el operador no salió de
    cuadro (no oyó el aviso), `first_evidence` quedó en `frame_000000` y CR-01
    confirmó 19 s ANTES del tono. Los datos eran de calidad excelente (CV 0,018) y
    la toma igual no servía: sin transición no hay onset que anclar. Pedirlo por
    voz y suponer que pasó es exactamente el error que este proyecto evita con
    guards.

    `vacio_s` debe superar `resolve_after_ms` de CR-01 (2.000 ms) para que el
    episodio viejo se cierre y la reentrada abra uno NUEVO.
    """
    t0 = time.time()
    ultimo_aviso = 0.0
    while time.time() - t0 < timeout_s:
        fr = _frames(media_run_id)
        if fr:
            con_persona = [ts for ts, hay in fr if hay]
            ultimo_ts = fr[-1][0]
            vacio_ms = (ultimo_ts - max(con_persona)) if con_persona else None
            if vacio_ms is None or vacio_ms >= vacio_s * 1000:
                real = vacio_s if vacio_ms is None else vacio_ms / 1000
                print(f"      cuadro vacío CONFIRMADO por datos "
                      f"({real:.1f} s sin `person`)", flush=True)
                return True
        if time.time() - ultimo_aviso > 9:
            _voz("Sali de cuadro por completo, por favor.")
            ultimo_aviso = time.time()
            print("      esperando cuadro vacío ...", flush=True)
        time.sleep(1.5)
    print("      ⚠ TIMEOUT esperando cuadro vacío — se aborta para no gastar la "
          "toma", flush=True)
    _voz("No detecte el cuadro vacio. Se aborta la toma.")
    return False


def _unidades(media_run_id):
    """Unidades ya procesadas, EN VIVO.

    TRAMPA F-101.7 (medida 2026-08-05): mid-run `GET /api/runs/{id}` del media-plane
    devuelve solo `{run_id, name, status, started_at, model, live}` — NO trae
    `units_processed`; ese campo aparece recién en el `summary` al cerrar. Una
    espera que lo lea de ahí concluye "la cámara no entregó frames" con la
    cámara funcionando perfecto (102 unidades en el probe que lo destapó).
    La señal correcta y directa es el `detections.jsonl`, que se escribe
    incrementalmente.
    """
    det = MP / "runs" / media_run_id / "detections.jsonl"
    if det.exists():
        with det.open() as fh:
            return sum(1 for line in fh if line.strip())
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seconds", type=int, default=35,
                    help="segundos de corrida DESPUÉS del beep")
    ap.add_argument("--en-cuadro", type=int, default=15,
                    help="segundos que hay que quedarse en cuadro")
    ap.add_argument("--camera-url", default="169.254.31.137")
    ap.add_argument("--sin-cue", action="store_true",
                    help="el sujeto YA está en cuadro: no hay cuenta regresiva ni "
                         "ancla humana. Se miden política, relojes e integridad, "
                         "no el offset físico→estampa.")
    a = ap.parse_args()

    for nombre, base in (("media :8080", MEDIA), ("control :8081", CONTROL)):
        try:
            _get(base, "/healthz")
        except Exception as e:
            print(f"PRECONDICIÓN NO CUMPLIDA: {nombre} no responde "
                  f"({type(e).__name__}).\n  Levantar con: bash "
                  f"{Path(__file__).parent / '91-arrancar-servicios.sh'}")
            return 2

    # --- 1) CONTROL PRIMERO: el 201 implica suscripción activa
    cfg = CP / "configs" / "smoke_claqueta.yaml"
    cfg.write_text(
        "run:\n  scenario: EBE\n  name: smoke_claqueta\n"
        '  description: "Humo claqueta doc 101 — ancla wallclock e identidad t_alert"\n'
        "input:\n  type: bus\n  track_persons: false\n"
        "  bus:\n    endpoint: tcp://127.0.0.1:5557\n"
        "    topics:\n      - media.detection.v1.\n      - run.lifecycle.v1.\n"
        "    hwm: 1000\n    recv_timeout_ms: 1000\n    idle_timeout_s: 120\n"
        "    finish:\n      signal: run_lifecycle\n      poll_url: null\n"
        "      poll_interval_s: 5\n"
        "patterns:\n  file: patterns/cr01_cr02_v2.yaml\n"
        "  active_ids:\n    - CR-01\n    - CR-02\n"
        "outputs:\n  base_dir: ../runs\n")
    r = _post(CONTROL, "/api/runs", {"config_path": str(cfg), "mode": "live"})
    control_run_id = r.get("control_run_id") or r.get("run_id") or r.get("id")
    print(f"[1/5] control-plane suscripto — run {control_run_id}")

    # El aviso va ANTES de arrancar el media: la corrida tiene que empezar con el
    # cuadro VACÍO. Si arranca con el sujeto adentro se abre un episodio que no se
    # cierra al salir (sin sujeto no hay evidencia de cumplimiento) y la reentrada
    # en el tono no genera la alerta anclada. Los ~9 s de conexión de la OAK-D son
    # justamente la ventana para salir.
    if not a.sin_cue:
        _voz("Sali de cuadro AHORA y quedate afuera hasta el tono.", esperar=True)

    # --- 2) MEDIA DESPUÉS, con bus y previews (registro visual de la palmada)
    media = _post(MEDIA, "/api/runs", {
        "ingest": {"plugin": "oak_d",
                   "config": {"url": a.camera_url, "fps": 30,
                              "source_id": "smoke_claqueta"}},
        "prompts": PROMPTS,
        "bus": {"enabled": True},
        "run": {"name": "smoke_claqueta", "save_previews": True},
    })
    media_run_id = media.get("run_id") or media.get("id")
    print(f"[2/5] media-plane disparado — run {media_run_id}")
    print("      conectando la OAK-D (~9 s; F-DR6: NADIE actúa hasta que entregue "
          "frames)...")

    # --- 3) esperar a que la fuente salga de "starting"
    for _ in range(45):
        time.sleep(2)
        try:
            if _unidades(media_run_id) >= 5:
                break
        except Exception:
            pass
    else:
        print("La cámara no entregó frames. Revisar red mirrored (doc 68 / "
              "`ip route get` sin `via`). Abortando.")
        return 1

    if a.sin_cue:
        beep_ms = time.time() * 1000.0
        beep_mono_ms = time.monotonic() * 1000.0
        print(f"\n[3/5] MODO SIN CUE — el sujeto ya está en cuadro. Corriendo "
              f"{a.seconds} s.")
        print("      (sin ancla humana: no se mide el offset físico→estampa; sí la "
              "política,\n       la coherencia de relojes entre procesos y la "
              "integridad del acople.)")
        time.sleep(a.seconds)
        return _cerrar(a, media_run_id, control_run_id, beep_ms, beep_mono_ms)

    print("\n[3/5] CÁMARA ENTREGANDO FRAMES — guiando al operador POR AUDIO.")
    if not _esperar_cuadro_vacio(media_run_id):
        try:
            _post(MEDIA, f"/api/runs/{media_run_id}/stop", {})
        except Exception:
            pass
        return 1

    # El ancla: tono en un instante absoluto, y PowerShell devuelve el wallclock
    # real en que sonó (ver _cue_preciso).
    # OJO con el texto: una cuenta regresiva hablada INVITA a anticipar. En la toma
    # de las 17:26 el operador entró 1,1 s ANTES del tono reaccionando al "tres, dos,
    # uno" (4 de los 13 frames previos ya tenían `person`), y el guard de transición
    # la rechazó. Sin cuenta: solo la instrucción, silencio, y el tono.
    target_ms = (time.time() + 12.0) * 1000.0
    # "Lo más rápido posible" no es capricho: la pata A discrimina el instrumento
    # solo si la reacción humana es CHICA frente al capture_to_host (~1.600 ms).
    # Con la reacción de 3,1 s de la toma anterior, el número es compatible con las
    # dos hipótesis y no prueba nada.
    cue = _cue_preciso(
        target_ms,
        "No entres ahora. Espera el tono. Cuando suene, entra a cuadro lo mas "
        "rapido que puedas, de un solo paso.")
    print(f"      tono programado para {target_ms:.0f} ms; esperando ...",
          flush=True)
    beep_mono_ms = time.monotonic() * 1000.0 + (target_ms - time.time() * 1000.0)
    time.sleep(max(0.0, target_ms / 1000.0 - time.time()) + 0.4)

    beep_ms = target_ms
    try:
        out, _ = cue.communicate(timeout=10)
        real = float((out or "").strip().splitlines()[-1])
        deriva = real - target_ms
        beep_ms = real            # el ancla es el instante MEDIDO, no el programado
        print(f"      TONO sonó a {real:.0f} ms (deriva vs programado "
              f"{deriva:+.0f} ms)")
        if abs(deriva) > 500:
            print("      ⚠ deriva alta: el habla previa se pasó del target. El "
                  "ancla usa el instante medido, así que sigue siendo válido.")
    except Exception as e:
        print(f"      ⚠ no se pudo leer el instante real del tono ({type(e).__name__}); "
              f"se usa el programado")

    _voz(f"Quedate quieto {a.en_cuadro} segundos.")
    time.sleep(max(0, a.en_cuadro - 1))
    _voz("Ya podes salir de cuadro.")
    time.sleep(max(0, a.seconds - a.en_cuadro))

    return _cerrar(a, media_run_id, control_run_id, beep_ms, beep_mono_ms)


def _cerrar(a, media_run_id, control_run_id, beep_ms, beep_mono_ms):
    try:
        _post(MEDIA, f"/api/runs/{media_run_id}/stop", {})
    except Exception:
        pass
    print("[4/5] corte — esperando el cierre del control ...")

    # TRAMPA MEDIDA (2026-08-05, F-101.5): la fuente OAK-D no cierra de forma
    # cooperativa — el productor no manda END ("ventana de drenaje agotada") y el
    # hilo monitor de depthai puede cerrar el device y tirar un std::system_error
    # desde un hilo NO-Python => std::terminate => SIGABRT: el proceso del
    # media-plane MUERE. Misma familia que la trampa de ZeroMQ (docs 37/68), otro
    # culpable. Los artefactos NO se pierden: `detections.jsonl` y `metrics.jsonl`
    # se escriben incrementalmente y `alerts.jsonl` lo escribe el control-plane,
    # que sobrevive. Por eso esta espera no exige que el media siga vivo.
    cerrado = False
    for _ in range(15):
        time.sleep(2)
        cand = sorted([p for p in (CP / "runs").glob("smoke_claqueta*") if p.is_dir()],
                      key=lambda p: p.stat().st_mtime)
        if cand and (cand[-1] / "summary.json").exists():
            cerrado = True
            break
    media_vivo = True
    try:
        _get(MEDIA, "/healthz")
    except Exception:
        media_vivo = False
    cand = sorted([p for p in (CP / "runs").glob("smoke_claqueta*") if p.is_dir()],
                  key=lambda p: p.stat().st_mtime)
    control_dir = str(cand[-1]) if cand else None
    if not media_vivo:
        print("      ⚠ el media-plane murió al cerrar la fuente OAK-D (F-101.5). "
              "Los artefactos SIRVEN igual:")
        print("        detections/metrics se escriben incrementalmente y las "
              "alertas las escribe el control.")
    if not cerrado:
        print("      ⚠ el control todavía no escribió summary.json (esperará su "
              "idle_timeout de 120 s).")
        print("        La verificación no lo necesita: usa alerts.jsonl.")

    CAPTURA.write_text(json.dumps({
        "fecha": "2026-08-05",
        "beep_wallclock_ms": beep_ms,
        "beep_monotonic_ms": beep_mono_ms,
        "media_run_id": media_run_id,
        "control_run_id": control_run_id,
        "control_run_dir": control_dir,
        "media_run_dir": str(MP / "runs" / media_run_id),
        "en_cuadro_s": a.en_cuadro,
        "modo": "sin_cue" if a.sin_cue else "con_ancla_humana",
        "nota": (
            "MODO SIN CUE: el sujeto ya estaba en cuadro. `beep_wallclock_ms` es "
            "solo el instante de referencia del arranque, NO un ancla física — la "
            "pata A (offset mundo físico→estampa) NO se mide en esta corrida; se "
            "miden política, coherencia de relojes entre procesos e integridad."
            if a.sin_cue else
            "El beep es el instante conocido en wallclock. La entrada a cuadro debe "
            "coincidir con él; la reacción humana (~200-300 ms, doc 67 midió 222 ms) "
            "es el límite de precisión del ancla y se declara."),
    }, indent=1, ensure_ascii=False))

    print(f"\n[5/5] CAPTURA LISTA -> {CAPTURA.name}")
    print(f"      media  : {MP / 'runs' / media_run_id}")
    print(f"      control: {control_dir}")
    print("\n      Verificar con: python3 101-claqueta-verificar.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
