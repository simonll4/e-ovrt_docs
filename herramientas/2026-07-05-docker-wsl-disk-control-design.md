# Mecanismo de control de disco Docker en WSL2 — Diseño

**Fecha:** 2026-07-05
**Ámbito:** workspace `e-ovrt` (host Windows + WSL2 Ubuntu + Docker Desktop)
**Estado:** aprobado, pendiente de implementación

## Problema

Los builds e imágenes de Docker acumulados agotan el espacio del disco `C:` del host
Windows. El VHDX de Docker (`docker_data.vhdx`) y el VHDX de la distro Ubuntu
(`ext4.vhdx`) crecen de forma monótona: aunque se borren imágenes y cache dentro de
WSL, los archivos VHDX en `C:` **no se achican solos** (los VHDX son dynamic-expanding:
crecen pero nunca se contraen sin compactación explícita).

Estado observado el 2026-07-05:
- `C:` — 409 GB usados / 40 GB libres (92%).
- `docker_data.vhdx` — 57.9 GB.
- `ext4.vhdx` (Ubuntu) — 82.7 GB.
- Docker build cache — 14.23 GB (13.83 GB reclamables), sobre 13.59 GB de imágenes.

La causa raíz es doble: (1) el build cache crece sin límite entre sesiones, y (2) el
espacio liberado dentro del VHDX no vuelve al host hasta compactar.

## Restricción de arquitectura

**Compactar un VHDX exige apagar la VM que lo monta** (`wsl --shutdown` + cerrar Docker
Desktop). Por lo tanto la compactación **no puede ejecutarse desde dentro de WSL** — un
script que corre en WSL no puede apagar su propio sistema de archivos a mitad de camino.
Esto obliga a separar el mecanismo en capas por dónde se ejecutan.

## Diseño: 3 capas

### Capa 1 — Prevención (configuración una sola vez)

Evita que el problema se acumule.

1. **Cap del build cache** vía `daemon.json` de Docker Desktop:
   ```json
   {
     "builder": {
       "gc": {
         "enabled": true,
         "defaultKeepStorage": "20GB"
       }
     }
   }
   ```
   Docker poda automáticamente el build cache al superar 20 GB, conservando las capas
   más recientes/usadas. Se elige 20 GB (no menos) porque el build multi-variante de
   media-plane usa ~14 GB de cache legítimo; un cap menor forzaría re-descargar
   torch/CUDA en cada build.

2. **Límite del disco virtual de Docker** en Docker Desktop → Settings → Resources →
   Disk image size: fijar un tope duro de ~100 GB (hoy suele estar en el máximo). Actúa
   como red de seguridad: Docker no puede crecer más allá de ese límite.

Ambos cambios son manuales-guiados: el instalador (`setup-prevention.sh`) genera/parcha
`daemon.json` y documenta el paso de UI que no es automatizable desde WSL.

### Capa 2 — Limpieza frecuente: `scripts/docker/docker-clean.sh` (corre en WSL)

Se ejecuta después de una sesión de builds. No requiere admin ni apagar nada.

Acciones, en orden:
1. Verificar que el daemon Docker responde (`docker info`); abortar con mensaje claro si
   no.
2. Reportar estado inicial (`docker system df`).
3. `docker builder prune -f` — borra todo el build cache no usado.
4. `docker image prune -f` — borra imágenes dangling (`<none>`).
5. `docker container prune -f` — borra contenedores parados.
6. Reportar estado final y espacio liberado.

**Conserva imágenes tagueadas** (`eovrt/media-plane:latest`, `eovrt/console:latest`):
nunca usa `-a`. Así no se re-buildea ~20 min después de cada limpieza.

Libera espacio *dentro* del VHDX. El archivo en `C:` deja de crecer pero todavía no se
achica — eso es trabajo de la Capa 3.

Flag opcional `--all`: escala a `docker system prune -a -f` (borra también imágenes
tagueadas no usadas por contenedores corriendo) para cuando se quiere recuperación
máxima. No es el default.

### Capa 3 — Compactación ocasional: `scripts/windows/compact-vhdx.ps1` (corre en Windows, admin)

Para cuando `C:` se pone crítico (~semanal, o cuando el espacio libre baje de un
umbral). Devuelve al host el espacio ya liberado por la Capa 2.

Acciones:
1. Auto-elevarse (UAC) si no corre como admin.
2. Listar tamaño actual de los VHDX objetivo.
3. **Guardarraíl:** si hay contenedores corriendo (`docker ps -q` no vacío), abortar —
   no apagar Docker en medio de un build/run.
4. Cerrar Docker Desktop y `wsl --shutdown` (avisa antes: cierra la sesión WSL activa).
5. `diskpart` con `compact vdisk` sobre:
   - `docker_data.vhdx` (Docker)
   - `ext4.vhdx` de la distro Ubuntu (donde quedaron los ~75 GB muertos)
   Si diskpart falla en un VHDX, continúa con el otro y reporta el fallo.
6. Reiniciar Docker Desktop.
7. Reportar tamaño final de los VHDX y espacio recuperado en `C:`.

Las rutas de los VHDX se descubren en tiempo de ejecución (no hardcodeadas): el `.vhdx`
de la distro vía la ruta registrada de WSL, y `docker_data.vhdx` en la ruta estándar de
Docker Desktop.

**Ubicación y ejecución:** el script vive versionado en `scripts/windows/` dentro del
workspace, pero **no puede ejecutarse desde `\\wsl.localhost\...`** porque apaga WSL a
mitad de camino. El instalador lo copia a una ruta local de Windows
(`C:\Users\<user>\eovrt-tools\`) y documenta cómo invocarlo (click derecho → Run with
PowerShell, o acceso directo).

## Componentes y su relación

```
scripts/
├── docker/
│   ├── docker-clean.sh        # Capa 2 — WSL, sin admin
│   └── setup-prevention.sh    # Capa 1 — parcha daemon.json, guía UI
└── windows/
    └── compact-vhdx.ps1       # Capa 3 — Windows admin, fuera de WSL
```

Cada script tiene un propósito único e independiente:
- `docker-clean.sh`: reclama espacio dentro del VHDX. Entrada: ninguna. Salida:
  reporte df. Depende de: daemon Docker.
- `setup-prevention.sh`: aplica configuración de prevención una vez. Depende de: acceso
  de escritura a `daemon.json`.
- `compact-vhdx.ps1`: contrae los VHDX al host. Depende de: privilegios admin, Docker
  detenible.

No comparten estado; se comunican solo con el sistema (Docker daemon, filesystem).

## Manejo de errores

- `docker-clean.sh`: si el daemon no responde, aborta con instrucción de arrancar Docker
  Desktop; nunca toca contenedores corriendo (usa `prune`, no `rm` forzado).
- `compact-vhdx.ps1`: aborta si hay contenedores activos antes de apagar; si un
  `diskpart compact` falla, continúa con el siguiente VHDX; reporta cada resultado.
- `setup-prevention.sh`: respalda `daemon.json` antes de parchear; valida el JSON
  resultante.

## Testing

- `docker-clean.sh`: corrida real contra el estado actual (13.83 GB reclamables como
  fixture natural), verificando que las imágenes `eovrt/*` sobreviven y que
  `docker system df` reporta el cache en ~0 después.
- `compact-vhdx.ps1`: corrida real supervisada (única forma de validar compactación);
  se verifica midiendo los VHDX en `C:` antes/después.
- `setup-prevention.sh`: verificar que `daemon.json` queda con JSON válido y que Docker
  reinicia sin error tras aplicar el cap.

## Resultado esperado

- Inmediato (Capa 2): ~14 GB liberados dentro del VHDX.
- Al compactar (Capa 3): ~60–75 GB devueltos a `C:`.
- Continuo (Capa 1): el build cache deja de crecer sin control; el problema no
  reaparece.

## Fuera de alcance (YAGNI)

- Tarea programada / automatización en background (el usuario eligió comando manual).
- Monitoreo continuo con alertas de umbral.
- Mover los VHDX a otro disco (`D:`/`/dev/sdd`) — posible mejora futura, no requerida
  ahora.
