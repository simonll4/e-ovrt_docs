"""Humo EBE live tras los cambios del control-plane (2026-08-04) — SIN pasos manuales.

Dos objetivos, en orden de importancia:

  A) **REGRESION del camino live.** La ultima corrida live real fue el 2026-07-25.
     Desde entonces el control-plane cambio el evaluador (`c1cbb56`) y sobre todo el
     **despacho por estrategia dentro de `pattern_engine.process()`**, que es el camino
     caliente de live Y de replay; mas `prepare_run` (desambiguacion de directorios) y
     el decorador de fuente. Nada de eso se ejercito en vivo. Esto corre con el pattern
     set DESPLEGADO (`cr01_cr02_v2`, strategy eind por default): si el 1:1 sigue verde,
     la regresion esta descartada.

  B) **G1 en vivo** (`cr01_cr02_v2_subject` + `input.track_persons: true`): cierra el
     residuo declarado en el doc 90 D-90.3 — la afirmacion "la identidad sirve tambien
     en EBE" hoy esta cubierta solo por tests unitarios.

Orden EBE NO NEGOCIABLE (spec 40 SS3.2 regla 1, doc 82 trampa): control PRIMERO
(POST :8081/api/runs, cuyo 201 implica que ya esta suscripto) y DESPUES media
(POST :8080/api/runs con bus.enabled). PUB/SUB pierde lo publicado antes de la
suscripcion.

Uso:
  # 1) media-plane arriba desde SU repo con el campeon:
  #    EOVRT_MODEL_REF=grounding-dino/gdino-tiny-560 .venv/bin/uvicorn --factory \
  #      eovrt_media.service.app:create_app --port 8080
  # 2) control-plane arriba desde SU repo:
  #    .venv/bin/eovrt-control serve --port 8081
  # 3) este script:
  python3 91-smoke-ebe-post-cambios.py --fase A --camera rtsp --seconds 45
  python3 91-smoke-ebe-post-cambios.py --fase B --camera rtsp --seconds 45
"""
import argparse, json, os, sys, time, urllib.request
from pathlib import Path

CONTROL = "http://127.0.0.1:8081"
MEDIA = "http://127.0.0.1:8080"
CP = Path("/home/simonll4/projects/e-ovrt_control-plane")

# ✎ 2026-08-10: la URL traía la credencial del DVR en texto plano (se coló al
# commitear; el resto de las cámaras van gitignoradas justamente por esto). Redactada
# antes de publicar el repo — se toma de EZVIZ_RTSP_URL, mismo nombre que
# operacion/30-runbook-local.md, formato `rtsp://usuario:clave@ip:554/stream`.
EZVIZ_RTSP_URL = os.environ.get("EZVIZ_RTSP_URL")

CAMERAS = {
    # cameras/rtsp_dvr_1.yaml y oak_d_lab.yaml (gitignorados: credenciales en claro)
    "rtsp": {"plugin": "rtsp",
             "config": {"url": EZVIZ_RTSP_URL,
                        "source_id": "smoke_ebe"}},
    # La clave es `url` (no `ip`): 1:1 con cameras/oak_d_lab.yaml. Con `ip` el
    # servicio devuelve 422 "Campos desconocidos en ingest.config".
    "oakd": {"plugin": "oak_d", "config": {"url": "169.254.31.137", "fps": 30,
                                           "source_id": "smoke_ebe"}},
}

# Prompt set congelado cr01_cr02_v2_short (frozen_sha256 df81fd48...).
PROMPTS = {
    "set_inline": {"id": "cr01_cr02_v2_short", "classes": [
        {"id": "person", "phrasings": {"default": ["person"]}},
        {"id": "helmet", "phrasings": {"default": ["helmet"]}},
        {"id": "vest", "phrasings": {"default": ["vest"]}},
    ]},
    "active_ids": ["person", "helmet", "vest"],
}

FASES = {
    "A": {"patterns": "patterns/cr01_cr02_v2.yaml", "track_persons": False,
          "que": "REGRESION del camino live con el pattern set desplegado"},
    "B": {"patterns": "patterns/cr01_cr02_v2_subject.yaml", "track_persons": True,
          "que": "G1 EN VIVO (identidad por sujeto sobre el bus)"},
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


def _precondiciones(camera):
    problemas = []
    for nombre, base in (("media-plane :8080", MEDIA), ("control-plane :8081", CONTROL)):
        try:
            _get(base, "/healthz")
        except Exception as e:
            problemas.append(f"{nombre} no responde ({type(e).__name__})")
    if camera == "rtsp" and not EZVIZ_RTSP_URL:
        problemas.append("falta EZVIZ_RTSP_URL en el entorno (ver comentario junto a CAMERAS)")
    return problemas


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fase", choices=["A", "B"], required=True)
    ap.add_argument("--camera", choices=list(CAMERAS), default="rtsp")
    ap.add_argument("--seconds", type=int, default=45)
    a = ap.parse_args()
    fase = FASES[a.fase]

    print(f"=== FASE {a.fase}: {fase['que']}")
    problemas = _precondiciones(a.camera)
    if problemas:
        print("PRECONDICIONES NO CUMPLIDAS:")
        for p in problemas:
            print(f"  - {p}")
        print("Levantar cada servicio DESDE LA RAIZ DE SU REPO (doc 82 trampa 5).")
        return 2

    # --- 1) CONTROL PRIMERO: el 201 implica suscripcion (regla 1)
    cfg = CP / "configs" / f"smoke_ebe_{a.fase.lower()}.yaml"
    cfg.write_text(
        "run:\n  scenario: EBE\n"
        f"  name: smoke_ebe_{a.fase.lower()}\n"
        f'  description: "Humo EBE fase {a.fase} — {fase["que"]}"\n'
        "input:\n  type: bus\n"
        f"  track_persons: {str(fase['track_persons']).lower()}\n"
        "  bus:\n    endpoint: tcp://127.0.0.1:5557\n"
        "    topics:\n      - media.detection.v1.\n      - run.lifecycle.v1.\n"
        "    hwm: 1000\n    recv_timeout_ms: 1000\n    idle_timeout_s: 120\n"
        "    finish:\n      signal: run_lifecycle\n      poll_url: null\n"
        "      poll_interval_s: 5\n"
        f"patterns:\n  file: {fase['patterns']}\n"
        "  active_ids:\n    - CR-01\n    - CR-02\n"
        "outputs:\n  base_dir: ../runs\n")
    print(f"[1/4] control-plane: POST /api/runs (mode=live) con {cfg.name} ...")
    r = _post(CONTROL, "/api/runs", {"config_path": str(cfg), "mode": "live"})
    control_run_id = r.get("control_run_id") or r.get("run_id") or r.get("id")
    print(f"      201 -> control_run_id={control_run_id}  (suscripto)")

    # --- 2) MEDIA DESPUES, con el bus habilitado
    print(f"[2/4] media-plane: POST /api/runs con bus.enabled (camara {a.camera}) ...")
    media = _post(MEDIA, "/api/runs", {
        "ingest": CAMERAS[a.camera],
        "prompts": PROMPTS,
        "bus": {"enabled": True},
        "run": {"name": f"smoke_ebe_{a.fase.lower()}", "save_previews": False},
    })
    media_run_id = media.get("run_id") or media.get("id")
    print(f"      media_run_id={media_run_id}")

    # --- 3) dejar correr
    print(f"[3/4] corriendo {a.seconds}s — PONETE EN CUADRO SIN CASCO ~10 s seguidos "
          f"para disparar CR-01 (persistencia 4 s)")
    t0 = time.time()
    while time.time() - t0 < a.seconds:
        time.sleep(5)
        try:
            cur = _get(CONTROL, "/api/runs/current")
            print(f"      t={time.time()-t0:>3.0f}s  unidades={cur.get('units_processed')} "
                  f"alertas={cur.get('alerts_count')} drops={cur.get('bus_dropped_events')}",
                  flush=True)
        except Exception:
            pass
    try:
        _post(MEDIA, f"/api/runs/{media_run_id}/stop", {})
    except Exception as e:
        print(f"      (stop del media devolvio {type(e).__name__}; sigue)")

    # --- 4) veredicto
    print("[4/4] esperando cierre 1:1 (run.lifecycle -> el control cierra solo) ...")
    time.sleep(12)
    # `outputs.base_dir: ../runs` resuelve RELATIVO AL ARCHIVO DE CONFIG (que vive en
    # e-ovrt_control-plane/configs/), no al cwd: el directorio es <repo>/runs.
    runs_dir = CP / "runs"
    candidatos = sorted([p for p in runs_dir.glob(f"smoke_ebe_{a.fase.lower()}*") if p.is_dir()],
                        key=lambda p: p.stat().st_mtime)
    if not candidatos:
        print("VEREDICTO: NO se creo directorio de control run — revisar logs")
        return 1
    run_dir = candidatos[-1]
    summary = json.loads((run_dir / "summary.json").read_text())
    alertas = [json.loads(x) for x in (run_dir / "alerts.jsonl").read_text().splitlines()
               if x.strip()] if (run_dir / "alerts.jsonl").exists() else []

    print(f"\n=== VEREDICTO FASE {a.fase} ===")
    print(f"  control run dir : {run_dir.name}")
    print(f"  unidades        : {summary.get('units_processed')}")
    print(f"  bus_dropped     : {summary.get('bus_dropped_events')}  (ADR-003: debe ser 0)")
    print(f"  degradado       : {summary.get('degraded')} {summary.get('degradation_causes')}")
    print(f"  alertas         : {len(alertas)}")
    for al in alertas[:5]:
        print(f"     - {al.get('condition_id')} subject_key={al.get('subject_key')!r}")

    ok = (summary.get("units_processed") or 0) > 0 and not summary.get("bus_dropped_events")
    if a.fase == "B":
        # El invariante de G1: la clave de estado debe traer track_id, no ser de escena.
        con_track = [al for al in alertas if (al.get("subject_key") or "").count(":") >= 2]
        causas = summary.get("degradation_causes") or []
        print(f"  claves con track_id: {len(con_track)}/{len(alertas)}")
        if "no_track_id" in causas:
            print("  *** no_track_id EN LAS CAUSAS: el motor degrado a escena -> "
                  "esto midio G0, no G1")
            ok = False
        elif alertas and not con_track:
            print("  *** ninguna alerta trae track_id en subject_key -> revisar")
            ok = False
    print(f"\n  {'VERDE' if ok else 'ROJO'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
