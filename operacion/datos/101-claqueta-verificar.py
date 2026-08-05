"""Humo claqueta (doc 101 §5) — VERIFICACIÓN sobre los artefactos.

Lee `101-claqueta-captura.json` (el instante del beep en wallclock) y los
artefactos de la corrida (media `metrics.jsonl`/`detections.jsonl` + control
`alerts.jsonl`) y computa, cada pata con su INSTRUMENTO declarado:

  A) ANCLA EXTERNA — |capture_wallclock del frame más cercano − beep|. Es la
     única pata que cruza al mundo físico: valida que `capture_wallclock_ms`
     sea tiempo real y no un reloj a la deriva. Doc 67 §G2 midió 222 ms a mano.

  B) ONSET OBSERVADO vs PRIMERA EVIDENCIA DEL MOTOR — el primer frame con
     `person` después del beep (lo que se ve) contra el `first_evidence_unit_id`
     que el control-plane registró (su contabilidad). Que coincidan es lo que
     hace no-trivial la descomposición.

  C) POLÍTICA — `alert_registered_ms − first_evidence_ms` ≈ `confirm_after_ms`
     (4.000 ms para CR-01 en cr01_cr02_v2). Doc 71 midió 4,1–4,6 s en vivo.

  D) COHERENCIA DE RELOJES ENTRE PROCESOS — `alert_registered_ms` es el reloj
     monotónico del CONTROL-plane y `capture_monotonic_ns` el del MEDIA-plane.
     La identidad del spec 40 §5.2.2 asume que comparten base (mismo host).
     Se verifica: la diferencia para el frame de la alerta debe ser positiva y
     del orden de G2A + bus (decenas/centenas de ms), no negativa ni absurda.

  E) IDENTIDAD `t_alert-system = TTFD + t_capture→alert`, con TTFD medido
     contra el reloj EXTERNO (el beep) y `t_capture→alert` medido por
     instrumentación interna cruzando los dos procesos. Se reporta el residual
     y qué parte es algebraica y qué parte es medida.

Uso: python3 101-claqueta-verificar.py [--captura ARCHIVO]
"""

import argparse
import json
import sys
from pathlib import Path

DATOS = Path(__file__).parent
CONFIRM_CR01_MS = 4000.0     # cr01_cr02_v2 (nunca v1)
CONFIRM_CR02_MS = 7000.0
CONF_MIN = 0.25              # postprocess.min_confidence del servicio


def leer_jsonl(p: Path):
    if not p.exists():
        return []
    return [json.loads(x) for x in p.read_text().splitlines() if x.strip()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--captura", default=str(DATOS / "101-claqueta-captura.json"))
    a = ap.parse_args()

    cap_p = Path(a.captura)
    if not cap_p.exists():
        print(f"No existe {cap_p} — correr primero 101-claqueta-smoke.py")
        return 2
    cap = json.loads(cap_p.read_text())
    beep = cap["beep_wallclock_ms"]
    mrun = Path(cap["media_run_dir"])
    crun = Path(cap["control_run_dir"]) if cap.get("control_run_dir") else None

    metrics = [m for m in leer_jsonl(mrun / "metrics.jsonl")
               if m.get("event_type") == "metric_sample"]
    dets = leer_jsonl(mrun / "detections.jsonl")
    alertas = leer_jsonl(crun / "alerts.jsonl") if crun else []
    if not metrics:
        print(f"Sin metrics.jsonl utilizable en {mrun}")
        return 1

    por_unidad = {m["unit_id"]: m for m in metrics}
    dets_por_unidad = {d["unit_id"]: d for d in dets}

    print("=" * 72)
    print("HUMO CLAQUETA — VERIFICACIÓN (doc 101 §5)")
    print("=" * 72)
    print(f"  media run   : {mrun.name}")
    print(f"  control run : {crun.name if crun else '(no encontrado)'}")
    print(f"  unidades    : {len(metrics)} procesadas, {len(dets)} con detecciones")
    print(f"  beep        : {beep:.0f} ms (wallclock del script)")

    # ---------- A) ANCLA EXTERNA ----------
    # ---------- GUARD DE CONTAMINACIÓN (F-101.6) ----------
    # Sin esto, una corrida con el device crasheando se reporta como medición
    # limpia: los números SALEN, son plausibles y están mal. Pasó en la primera
    # toma del 2026-08-05 (dos huecos de ~40 s por ciclos de crash-reconexión;
    # el CR-01 "confirmó a 7.828 ms" contra una política de 4.000 y eso medía el
    # stall, no la política). El ping ICMP daba 0% de pérdida al mismo tiempo:
    # la pila de red del PoE contesta con la aplicación muerta.
    cad = [b["capture_wallclock_ms"] - x["capture_wallclock_ms"]
           for x, b in zip(metrics, metrics[1:])
           if b["capture_wallclock_ms"] > x["capture_wallclock_ms"]]
    problemas = []
    if cad:
        med_gap = sorted(cad)[len(cad) // 2]
        if max(cad) > max(5 * med_gap, 3000):
            problemas.append(
                f"hueco máximo {max(cad) / 1000:.1f} s contra una mediana de "
                f"{med_gap:.0f} ms → el pipeline se frenó (firma de "
                f"crash-reconexión del device)")
    # Un capture_to_host ALTO pero CONSTANTE es régimen estacionario de la fuente
    # (medido 2026-08-05: 1.660 ms de cola con huecos regulares de 281 ms) y no
    # invalida nada — se declara. Lo que sí contamina es que CREZCA: eso es el host
    # drenando un backlog, o sea que los frames no son contemporáneos entre sí.
    stale = sorted(m.get("capture_to_host_ms") or 0 for m in metrics)
    if stale:
        med_s = stale[len(stale) // 2]
        if max(stale) > 3 * med_s + 1000:
            problemas.append(
                f"capture_to_host CRECIENTE: mediana {med_s:.0f} ms, máx "
                f"{max(stale):.0f} ms → el host drenó un backlog (frames no "
                f"contemporáneos)")
    if problemas:
        print("\n" + "!" * 72)
        print("CORRIDA CONTAMINADA — NO se reportan métricas temporales de acá:")
        for p in problemas:
            print(f"  · {p}")
        print("\n  Verificar en el log del servicio "
              "(/tmp/eovrt-smoke-logs/media.log) las líneas:")
        print('    "ping was missed, closing the device connection"')
        print('    "Device likely crashed but did not reboot in time"')
        print('    "OAK-D no disponible (intento N/12)"')
        print("\n  REMEDIO: power-cycle de la OAK-D (desenchufar el PoE ~10 s). El "
              "ping ICMP\n  NO sirve para descartar esto — la pila de red del PoE "
              "responde con la\n  aplicación del device caída. Repetir la toma "
              "después del power-cycle.")
        print("!" * 72)
        return 3

    print("\n--- A) ANCLA EXTERNA (la pata que cruza al mundo físico) ---")
    if cap.get("modo") == "sin_cue":
        print("  (MODO SIN CUE: el sujeto ya estaba en cuadro y no hubo evento "
              "físico anclado.\n   Las patas A y B NO son ancla en esta corrida; "
              "se informan solo como contexto.)")
    cerca = sorted(metrics, key=lambda m: abs(m["capture_wallclock_ms"] - beep))
    mejor = cerca[0]
    d_ancla = mejor["capture_wallclock_ms"] - beep
    print(f"  frame más cercano al beep : {mejor['unit_id']}  "
          f"(Δ {d_ancla:+.0f} ms)")
    print(f"  doc 67 §G2 midió 222 ms a mano; esta corrida: {abs(d_ancla):.0f} ms")
    ventana = sorted([m for m in metrics
                      if abs(m["capture_wallclock_ms"] - beep) <= 1200],
                     key=lambda m: m["capture_wallclock_ms"])
    print(f"  frames a ±1,2 s del beep  : "
          f"{[m['unit_id'] for m in ventana]}")
    print(f"  → confirmar la palmada visualmente en {mrun / 'previews'}")
    if cad:
        med = sorted(cad)[len(cad) // 2]
        prom = sum(cad) / len(cad)
        sd = (sum((c - prom) ** 2 for c in cad) / len(cad)) ** 0.5
        print(f"  cadencia de esta corrida  : media {prom:.0f} ms "
              f"({30 / (prom / 33.333):.2f} fps eq), mediana {med:.0f} ms, "
              f"CV {sd / prom:.3f}")
        print(f"  (F-101.1 midió CV 0,22 en los humos del 08-05 — este es un "
              f"punto más de la misma distribución)")

    # ---------- B) ONSET OBSERVADO ----------
    print("\n--- B) ONSET OBSERVADO vs PRIMERA EVIDENCIA DEL MOTOR ---")

    def tiene_persona(unit_id):
        d = dets_por_unidad.get(unit_id)
        return bool(d) and any(x["label"] == "person" and x["confidence"] >= CONF_MIN
                               for x in d.get("detections") or [])

    # GUARD DE TRANSICIÓN: sin cuadro vacío antes del tono no hay onset que anclar.
    # Pasó en la toma de las 17:26 — datos impecables (CV 0,018) y ancla inservible
    # porque el sujeto nunca salió de cuadro (`first_evidence` = frame_000000).
    if cap.get("modo") != "sin_cue":
        previos = [m for m in metrics
                   if beep - 4000 <= m["capture_wallclock_ms"] <= beep - 200]
        ocupados = [m["unit_id"] for m in previos if tiene_persona(m["unit_id"])]
        if not previos:
            print("  ⚠ sin frames en la ventana previa al tono: no se puede "
                  "verificar la transición")
        elif ocupados:
            print(f"  ❌ GUARD DE TRANSICIÓN: había `person` en {len(ocupados)}/"
                  f"{len(previos)} frames de la ventana previa al tono "
                  f"({ocupados[:4]}).")
            print("     El sujeto NO salió de cuadro ⇒ lo que sigue no es un onset "
                  "y el ancla NO es válida.")
            print("     Repetir la toma: el script espera el cuadro vacío "
                  "confirmado por datos antes de armar el tono.")
            return 4
        else:
            print(f"  ✅ transición verificada: {len(previos)} frames sin `person` "
                  f"en la ventana previa al tono")

    post = [m for m in sorted(metrics, key=lambda m: m["capture_wallclock_ms"])
            if m["capture_wallclock_ms"] >= beep - 400]
    onset = next((m for m in post if tiene_persona(m["unit_id"])), None)
    if onset:
        ttfd_ext = onset["capture_wallclock_ms"] - beep
        print(f"  1er frame con `person` ≥{CONF_MIN} : {onset['unit_id']}  "
              f"→ TTFD externo = {ttfd_ext:+.0f} ms desde el beep")
        # PREDICCIÓN FALSABLE (lectura del código de OakDSource, 2026-08-05):
        #   capture_to_host_ms = dai.Clock.now() − msg.getTimestamp()  (edad real
        #   del frame al salir de la cola; timesync PoE <0,5 ms)
        #   capture_wallclock_ms = time.time() en ESE mismo momento (dequeue)
        # ⇒ el wallclock de captura del FOTÓN = capture_wallclock − capture_to_host.
        # Si el sujeto entra a cuadro en el tono, entonces
        #   TTFD_externo − capture_to_host = reacción humana,
        # que tiene que ser un número chico y POSITIVO (~200-400 ms). Si
        # capture_to_host fuera un instrumento mentiroso, esto sale negativo o
        # absurdo. Es la única forma de validar ese campo contra el mundo físico.
        c2h = onset.get("capture_to_host_ms")
        if c2h is not None and cap.get("modo") != "sin_cue":
            reaccion = ttfd_ext - c2h
            print(f"     capture_to_host de ese frame       = {c2h:8.0f} ms "
                  f"(edad del frame al salir de la cola)")
            print(f"     ⇒ captura del FOTÓN vs tono        = "
                  f"{reaccion:+8.0f} ms  = reacción humana + cuantización de frame")
            ok_pred = -100 <= reaccion <= 1500
            print(f"     {'✅' if ok_pred else '❌'} predicción "
                  f"{'cumplida' if ok_pred else 'NO cumplida'}: se esperaba un valor "
                  f"chico y positivo (0-1.500 ms).")
            print(f"     Corolario para el informe: el presupuesto G2A (50-250 ms) "
                  f"se mide desde el\n     DEQUEUE, no desde el fotón. La latencia "
                  f"vidrio→resultado suma capture_to_host:\n     "
                  f"{c2h:.0f} + G2A. Ya está instrumentado por frame, así que es "
                  f"declarable, no un hueco.")
    else:
        ttfd_ext = None
        print("  *** ningún frame con `person` después del beep — revisar encuadre")

    if not alertas:
        print("\n  *** NO HUBO ALERTAS. Sin alerta no se puede verificar C/D/E.")
        print("      Diagnóstico posible: `helmet` falso sostenido sobre la cabeza "
              "(F-RT1 es el análogo para vest), o menos de 4 s de evidencia "
              "continua, o persona fuera del encuadre útil.")
        _diagnostico(dets, beep, por_unidad)
        return 1

    # Elegir la alerta ANCLADA: la que abre su primera evidencia DESPUÉS del tono.
    # Sin esto se analiza la alerta equivocada. Medido 2026-08-05: si la corrida
    # arranca con el sujeto en cuadro, se abre un episodio que **no se cierra al
    # salir de cuadro** — con nadie en cuadro no hay evidencia de cumplimiento, así
    # que `resolve_after_ms` no corre — y la reentrada NO genera un episodio nuevo.
    # Por eso la toma anclada tiene que empezar con el cuadro ya vacío.
    if cap.get("modo") != "sin_cue":
        ancladas = [al for al in alertas
                    if (por_unidad.get(al.get("first_evidence_unit_id")) or {})
                    .get("capture_wallclock_ms", 0) > beep]
        if not ancladas:
            print(f"\n  ❌ GUARD: ninguna de las {len(alertas)} alertas tiene su "
                  f"primera evidencia después del tono.")
            print("     La corrida arrancó con el sujeto en cuadro: el episodio "
                  "preexistente no se cierra\n     al salir de cuadro (sin sujeto no "
                  "hay evidencia de cumplimiento) y la reentrada no\n     abre uno "
                  "nuevo. Repetir con el cuadro VACÍO desde antes de arrancar.")
            return 5
        print(f"\n  ✅ {len(ancladas)}/{len(alertas)} alerta(s) ancladas al tono")
        alertas = ancladas

    for al in alertas:
        cond = al.get("condition_id")
        umbral = CONFIRM_CR01_MS if cond == "CR-01" else CONFIRM_CR02_MS
        print(f"\n{'=' * 72}\nALERTA {cond}  (subject_key={al.get('subject_key')!r}, "
              f"severidad={al.get('severity')})")
        fe_uid = al.get("first_evidence_unit_id")
        al_uid = al.get("unit_id")
        m_fe, m_al = por_unidad.get(fe_uid), por_unidad.get(al_uid)
        print(f"  1ª evidencia del motor : {fe_uid}"
              f"{'' if m_fe else '  (NO está en metrics — ojo)'}")
        print(f"  frame de confirmación  : {al_uid}"
              f"{'' if m_al else '  (NO está en metrics — ojo)'}")
        if onset and fe_uid == onset["unit_id"]:
            print("  → COINCIDE con el onset observado: la contabilidad del motor "
                  "es lo que se ve")
        elif onset and m_fe:
            print(f"  → difiere del onset observado por "
                  f"{m_fe['capture_wallclock_ms'] - onset['capture_wallclock_ms']:+.0f} ms")

        # ---------- C) POLÍTICA ----------
        d_pol = al["alert_registered_ms"] - al["first_evidence_ms"]
        ref = ("doc 71 midió 4.100–4.600 ms en vivo" if cond == "CR-01"
               else "el índice realtime §5 reporta 7.100 ms y superiores en vivo")
        print(f"\n  C) POLÍTICA: alert_registered − first_evidence = {d_pol:.0f} ms "
              f"(confirm_after_ms = {umbral:.0f})")
        print(f"     exceso sobre la política: {d_pol - umbral:+.0f} ms — {ref} "
              f"para {cond}")

        if not (m_fe and m_al):
            print("     (sin métricas de esos frames no se puede seguir con D/E)")
            continue

        # ---------- D) COHERENCIA DE RELOJES ENTRE PROCESOS ----------
        cap_mono_al = m_al["capture_monotonic_ns"] / 1e6
        cap_mono_fe = m_fe["capture_monotonic_ns"] / 1e6
        gap_proc = al["alert_registered_ms"] - cap_mono_al
        print(f"\n  D) RELOJES ENTRE PROCESOS: alert_registered (control) − "
              f"capture_monotonic (media) = {gap_proc:+.0f} ms")
        print(f"     G2A de ese frame (media): {m_al.get('g2a_ms', float('nan')):.0f} ms"
              f"  → resto atribuible a bus + motor: "
              f"{gap_proc - (m_al.get('g2a_ms') or 0):+.0f} ms")
        coherente = 0 < gap_proc < 5000
        print(f"     {'✅ comparten base monotónica' if coherente else '❌ NO comparten base — la identidad del spec no aplica'}")

        # ---------- E) IDENTIDAD ----------
        t_cap_alert = al["alert_registered_ms"] - cap_mono_fe
        # wallclock de registro de la alerta, vía el mapeo del media-plane
        al_wall = m_al["capture_wallclock_ms"] + (al["alert_registered_ms"] - cap_mono_al)
        t_sys = al_wall - beep
        ttfd_motor = m_fe["capture_wallclock_ms"] - beep
        suma = ttfd_motor + t_cap_alert
        print(f"\n  E) IDENTIDAD t_alert-system = TTFD + t_capture→alert")
        print(f"     TTFD              (reloj EXTERNO: beep → captura 1ª ev.) = "
              f"{ttfd_motor:8.0f} ms")
        print(f"     t_capture→alert   (interno, cruza media↔control)         = "
              f"{t_cap_alert:8.0f} ms")
        print(f"     suma                                                     = "
              f"{suma:8.0f} ms")
        print(f"     t_alert-system    (reloj EXTERNO: beep → alerta)         = "
              f"{t_sys:8.0f} ms")
        print(f"     residual                                                 = "
              f"{t_sys - suma:+8.0f} ms")
        print(f"     Nota de honestidad: el residual es algebraicamente 0 por el "
              f"mapeo\n     wallclock↔monotónico; lo que las patas A-D verifican de forma "
              f"INDEPENDIENTE es\n     que el ancla externa cierre ({abs(d_ancla):.0f} ms), que la 1ª "
              f"evidencia del motor sea\n     lo observable, que la política cierre y que los "
              f"relojes de los dos procesos\n     compartan base.")
        if ttfd_ext is not None:
            print(f"     t_alert-system contra el onset OBSERVADO "
                  f"(no el del motor) = {al_wall - (beep + ttfd_ext):.0f} ms")

    out = DATOS / "101-claqueta-verificacion.json"
    out.write_text(json.dumps({
        "media_run": mrun.name, "control_run": crun.name if crun else None,
        "beep_wallclock_ms": beep,
        "ancla_ms": d_ancla, "frame_ancla": mejor["unit_id"],
        "ttfd_externo_ms": ttfd_ext,
        "cadencia_media_ms": (sum(cad) / len(cad)) if cad else None,
        "alertas": [{
            "condition_id": al.get("condition_id"),
            "subject_key": al.get("subject_key"),
            "politica_ms": al["alert_registered_ms"] - al["first_evidence_ms"],
            "first_evidence_unit_id": al.get("first_evidence_unit_id"),
            "unit_id": al.get("unit_id"),
        } for al in alertas],
    }, indent=1, ensure_ascii=False))
    print(f"\n-> {out}")
    return 0


def _diagnostico(dets, beep, por_unidad):
    """Si no hubo alerta: ¿qué vio el modelo? (el patrón de F-RT1/F-RT2)."""
    n_p = n_h = n_v = 0
    for d in dets:
        labels = {x["label"] for x in d.get("detections") or []
                  if x["confidence"] >= CONF_MIN}
        n_p += "person" in labels
        n_h += "helmet" in labels
        n_v += "vest" in labels
    print(f"      frames con person={n_p}, helmet={n_h}, vest={n_v} "
          f"(de {len(dets)})")
    print("      Si helmet ≈ person, el modelo 'vio' un casco inexistente y "
          "suprimió CR-01.")


if __name__ == "__main__":
    sys.exit(main())
