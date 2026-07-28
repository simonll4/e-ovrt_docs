# 74 — Protocolo de higiene antes de medir fps/latencia en tiempo real

- **Última actualización:** 2026-07-28
- **Propósito:** evitar que una medición de fps/latencia en vivo (campaña de benchmark,
  demo, rodaje) quede contaminada por el estado del host, no por el código o el modelo.
- **Basado en:** `docs/operacion/73` §8–§9 (F-RT4). Con el host "cargado" (WSL con horas
  de uptime + control-plane + BFF + navegador corriendo) la misma configuración midió
  **2,6× más lenta** (550 ms vs 210 ms p50) que con el host recién reiniciado. La causa
  exacta no está aislada — está descartado que sea térmico, duty cycle de GPU, contexto
  CUDA frío/caliente o inquilinos por-run — pero el **remedio operativo sí está
  verificado**: reiniciar y no correr de más recupera el régimen rápido de forma
  reproducible (10/10 corridas limpias en la sesión que lo estableció).

**Costo:** ~5 minutos (reinicio de WSL) + 1 minuto (corrida de verificación). Hacerlo
siempre que el resultado de la medición vaya a citarse o compararse contra otra corrida.

## Cuándo aplicarlo

- Antes de cualquier campaña de benchmark de fps/latencia (A/B de código, comparación de
  modelos, medición de palancas de rendimiento).
- Antes de una demo o rodaje en vivo donde el fps importa.
- **No hace falta** para DBE offline (procesa a la velocidad que dé, no mide sobre reloj
  de pared) ni para verificar corrección funcional (detecciones, alertas).

## Checklist

### 1. Reiniciar WSL

Desde PowerShell/CMD en Windows (no se puede hacer desde dentro de WSL):

```powershell
wsl --shutdown
```

Volvé a abrir la terminal WSL. Esto descarta el estado acumulado del kernel de Linux y
cualquier proceso huérfano de sesiones previas. (El contexto CUDA en sí está descartado
como variable — trampa 3 abajo — pero el estado global del host no, y el reinicio es la
única forma verificada de resetearlo.)

### 2. Levantar solo lo necesario

No arranques `control-plane`, el `BFF`/webconsole ni un navegador si la medición es solo
del media-plane. Cada proceso extra es un competidor por CPU/GIL potencial, aunque la
ablación de inquilinos (doc 73 §8.1) los haya medido como costo plano en aislamiento —
**no se testeó su efecto combinado con horas de uptime**, así que la higiene barata es no
arriesgar:

```bash
cd e-ovrt_media-plane
source .venv/bin/activate
EOVRT_MODEL_REF=grounding-dino/gdino-tiny-560 make serve   # solo esto
```

Esperá a que `/readyz` conteste `{"status":"ready",...}` antes de seguir.

### 3. Corrida de verificación (obligatoria, ~1 minuto)

Lanzá una corrida corta contra la fuente real que vas a usar y mirá `latency_inference_ms`
en `metrics.jsonl`:

```bash
curl -X POST http://localhost:8080/api/runs \
  -H "Content-Type: application/json" \
  -d '{
        "ingest": {"plugin": "oak_d", "config": {"url": "169.254.31.137", "fps": 30, "resolution": "1080p", "warmup_frames": 20}},
        "prompts": {
          "set_inline": {"id": "verificacion", "classes": [{"id": "person", "phrasings": {"default": ["person"]}}]},
          "active_ids": ["person"]
        },
        "run": {"save_previews": false, "name": "verificacion_higiene"}
      }'
# copiar el run_id de la respuesta, esperar ~60s, y:
curl -X POST http://localhost:8080/api/runs/<run_id>/stop
```

```bash
python3 -c "
import json, statistics
vals = []
for line in open('runs/<run_id>/metrics.jsonl'):
    try:
        r = json.loads(line)
    except json.JSONDecodeError:
        continue
    if r.get('latency_inference_ms') is not None:
        vals.append(r['latency_inference_ms'])
p50 = statistics.median(vals)
print(f'p50={p50:.0f} ms  n={len(vals)}  ->', 'OK regimen rapido' if p50 < 300 else 'SOSPECHOSO, ver abajo')
"
```

**Umbral: p50 < 300 ms** con `gdino-tiny-560` @ OAK-D 1080p (referencia: régimen rápido
verificado en 194–236 ms; régimen lento en 420–560 ms — el umbral de 300 separa ambos con
margen). Para otro modelo/fuente, correr esta misma verificación una vez en condiciones
sabidas-buenas y fijar el propio umbral.

### 4. Si falla el umbral

**No sigas con la medición.** El resultado no va a ser comparable contra nada hecho en
régimen rápido. Antes de reintentar:

- Confirmá que el reinicio de WSL realmente ocurrió (no alcanza con matar el proceso del
  servicio; es el estado del kernel/WSL lo que importa, no solo el proceso).
- Revisá que no haya quedado ningún proceso pesado corriendo (`ps aux`, `nvidia-smi`
  mostrando otro consumidor de GPU).
- Si el umbral sigue sin cumplirse con host limpio, es una observación nueva de F-RT4 —
  documentarla en `docs/operacion/73`, no descartarla en silencio.

## Trampas conocidas (no repetir)

- **`py-spy` en WSL infla la latencia medida ~2× mientras perfila**, y su flag `-d` es un
  objetivo de *muestras*, no de segundos — puede tardar minutos en juntar lo pedido. Nunca
  usarlo para medir latencia en la misma corrida que perfila; solo sirve para la estructura
  relativa del flamegraph después. Detalle: doc 73 §9.1.
- **Nunca alimentar `normalize_spatial`/`prepare_model_input` con el frame crudo de 1080p**
  en un test aislado — el pipeline real le pasa el payload ya redimensionado por el
  productor. Error de método documentado en doc 73 §8.4, infla la línea base ~2,7×.
- **El régimen lento no se reproduce por antigüedad de proceso ni por contexto CUDA
  frío/caliente** — se probaron ambos y no separan (doc 73 §9.3). No perder tiempo
  intentando forzarlo por esa vía; si hace falta reproducirlo para seguir investigando
  F-RT4, la variable a manipular es el estado global del host (uptime + procesos
  concurrentes), no el proceso del media-plane en sí.
