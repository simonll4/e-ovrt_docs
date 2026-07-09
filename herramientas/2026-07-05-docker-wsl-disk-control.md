# Docker/WSL Disk Control Mechanism — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a 3-layer mechanism that stops Docker/WSL from exhausting the Windows `C:` disk — a prevention config, a fast in-WSL cleanup script, and an occasional out-of-WSL VHDX compaction script.

**Architecture:** Three independent scripts split by *where they run*. `docker-clean.sh` (WSL, no admin) reclaims space inside the VHDX. `setup-prevention.sh` (WSL) idempotently ensures the build-cache cap in `daemon.json`. `compact-vhdx.ps1` (Windows, admin) runs outside WSL because it must shut WSL down to shrink the VHDX files back into `C:`.

**Tech Stack:** Bash, `jq` (1.8, present), Docker CLI 29.6.1, PowerShell 5+, `diskpart`.

## Global Constraints

- **Never `git commit`.** The workspace root (`/home/simonll4/projects`) is **not** a git repo. These are workspace-level host-ops tools and follow the existing `scripts/` precedent (`download_videos.sh` lives there uncommitted). Leave files in place; do not commit to either child repo. (CLAUDE.md rule + no repo to commit to.)
- **Never use `docker system prune -a` by default.** Tagged images (`eovrt/media-plane:latest` ~13.2GB, `eovrt/console:latest`) must survive cleanup unless the user passes `--all` explicitly.
- **Never shut Docker/WSL down while containers run.** `compact-vhdx.ps1` must abort if `docker ps -q` is non-empty.
- All scripts use `set -euo pipefail` (bash) / `$ErrorActionPreference='Stop'` (PowerShell), and print a before/after space report.
- Discover paths at runtime; do not hardcode the user profile beyond documented fallbacks.

### Known environment (verified 2026-07-05)

- WSL distro name: `Ubuntu`. Its VHDX: `<Lxss BasePath>\ext4.vhdx` (currently `C:\Users\giuli\AppData\Local\wsl\{b1ad7718-930e-497f-a0c2-0b9afc6ca408}\ext4.vhdx`, 82.7GB).
- Docker VHDX: `%LOCALAPPDATA%\Docker\wsl\disk\docker_data.vhdx` (57.9GB).
- `daemon.json`: `%USERPROFILE%\.docker\daemon.json` → from WSL `/mnt/c/Users/giuli/.docker/daemon.json`. **Already contains** `builder.gc.defaultKeepStorage: "20GB"`, `enabled: true`.
- Reclaimable now: build cache 13.83GB. Tagged images: 13.59GB (keep).

---

## File Structure

```
scripts/
├── docker/
│   ├── docker-clean.sh        # Task 1 — WSL, no admin (Layer 2)
│   └── setup-prevention.sh    # Task 2 — WSL, verify/patch daemon.json (Layer 1)
└── windows/
    └── compact-vhdx.ps1       # Task 3 — Windows admin, outside WSL (Layer 3)
README-disk-control.md         # Task 4 — one-page operator guide
```

---

### Task 1: `docker-clean.sh` — in-WSL cleanup (Layer 2)

**Files:**
- Create: `scripts/docker/docker-clean.sh`

**Interfaces:**
- Consumes: nothing.
- Produces: an executable that reclaims Docker build cache + dangling images + stopped containers, keeping tagged images. Exit 0 on success, non-zero if daemon unreachable.

- [ ] **Step 1: Write the script**

```bash
#!/usr/bin/env bash
# docker-clean.sh — Layer 2: reclaim space INSIDE the WSL/Docker VHDX.
# Fast, no admin, keeps tagged images. Run after a build session.
# Usage: ./docker-clean.sh [--all]
#   --all  also remove tagged images unused by running containers (docker system prune -a)
set -euo pipefail

RED='\033[0;31m'; GREEN='\033[0;32m'; CYAN='\033[0;36m'; BOLD='\033[1m'; RESET='\033[0m'
ALL=0
[[ "${1:-}" == "--all" ]] && ALL=1

if ! docker info >/dev/null 2>&1; then
  echo -e "${RED}[ERROR]${RESET} Docker daemon no responde. Iniciá Docker Desktop y reintentá." >&2
  exit 1
fi

echo -e "${BOLD}${CYAN}== Estado inicial ==${RESET}"
docker system df

if [[ $ALL -eq 1 ]]; then
  echo -e "\n${BOLD}${CYAN}== Limpieza AGRESIVA (--all): borra imágenes tagueadas no usadas ==${RESET}"
  docker system prune -a -f
else
  echo -e "\n${BOLD}${CYAN}== Limpieza (conserva imágenes tagueadas) ==${RESET}"
  docker builder prune -f
  docker image prune -f
  docker container prune -f
fi

echo -e "\n${BOLD}${CYAN}== Estado final ==${RESET}"
docker system df
echo -e "\n${GREEN}[OK]${RESET} Espacio liberado dentro del VHDX. Para devolverlo a C:, corré compact-vhdx.ps1 desde Windows."
```

- [ ] **Step 2: Make executable**

Run: `chmod +x scripts/docker/docker-clean.sh`

- [ ] **Step 3: Verify daemon-down guard (dry check of logic)**

Run: `bash -n scripts/docker/docker-clean.sh && echo SYNTAX_OK`
Expected: `SYNTAX_OK`

- [ ] **Step 4: Real run — verify tagged images survive**

Run: `scripts/docker/docker-clean.sh`
Expected: exits 0; final `docker system df` shows Build Cache reclaimable ~0GB; `docker images eovrt/media-plane` still lists the tagged image afterward.

- [ ] **Step 5: Confirm survival explicitly**

Run: `docker images --format '{{.Repository}}:{{.Tag}}' | grep eovrt`
Expected: `eovrt/media-plane:latest` (and `eovrt/console:latest` if present) still listed.

---

### Task 2: `setup-prevention.sh` — idempotent cache-cap verification (Layer 1)

**Files:**
- Create: `scripts/docker/setup-prevention.sh`

**Interfaces:**
- Consumes: nothing.
- Produces: ensures `daemon.json` has `builder.gc.enabled=true` and `defaultKeepStorage="20GB"`; backs up before any write; prints the manual Docker Desktop UI step (disk image size cap) that can't be automated from WSL.

**Note:** the cap is already present in the current `daemon.json`. This script must be **idempotent**: detect the existing correct value and make no change, so it doubles as a verifier if the config is ever reset.

- [ ] **Step 1: Write the script**

```bash
#!/usr/bin/env bash
# setup-prevention.sh — Layer 1: ensure Docker build-cache cap so cache can't grow unbounded.
# Idempotent: if the cap already matches, changes nothing. Backs up daemon.json before writing.
set -euo pipefail

GREEN='\033[0;32m'; YELLOW='\033[1;33m'; CYAN='\033[0;36m'; BOLD='\033[1m'; RESET='\033[0m'
DAEMON="/mnt/c/Users/giuli/.docker/daemon.json"
KEEP="20GB"

command -v jq >/dev/null || { echo "jq requerido"; exit 1; }

if [[ ! -f "$DAEMON" ]]; then
  echo -e "${YELLOW}[WARN]${RESET} No existe $DAEMON; creándolo."
  echo '{}' > "$DAEMON"
fi

cur_enabled=$(jq -r '.builder.gc.enabled // empty' "$DAEMON")
cur_keep=$(jq -r '.builder.gc.defaultKeepStorage // empty' "$DAEMON")

if [[ "$cur_enabled" == "true" && "$cur_keep" == "$KEEP" ]]; then
  echo -e "${GREEN}[OK]${RESET} Cap de build cache ya configurado ($KEEP). Sin cambios."
else
  cp "$DAEMON" "${DAEMON}.bak"
  tmp=$(mktemp)
  jq --arg keep "$KEEP" '.builder.gc.enabled = true | .builder.gc.defaultKeepStorage = $keep' "$DAEMON" > "$tmp"
  jq empty "$tmp"  # validate
  mv "$tmp" "$DAEMON"
  echo -e "${GREEN}[OK]${RESET} Cap aplicado ($KEEP). Backup en ${DAEMON}.bak. Reiniciá Docker Desktop para que tome efecto."
fi

echo -e "\n${BOLD}${CYAN}== Paso manual (no automatizable desde WSL) ==${RESET}"
echo "Docker Desktop → Settings → Resources → Disk image size: fijá un tope de ~100GB como red de seguridad."
```

- [ ] **Step 2: Make executable + syntax check**

Run: `chmod +x scripts/docker/setup-prevention.sh && bash -n scripts/docker/setup-prevention.sh && echo SYNTAX_OK`
Expected: `SYNTAX_OK`

- [ ] **Step 3: Real run — expect idempotent no-op**

Run: `scripts/docker/setup-prevention.sh`
Expected: prints `Cap de build cache ya configurado (20GB). Sin cambios.` (because the value is already present); no `.bak` file created.

- [ ] **Step 4: Verify daemon.json untouched**

Run: `jq '.builder.gc' /mnt/c/Users/giuli/.docker/daemon.json`
Expected: `{ "defaultKeepStorage": "20GB", "enabled": true }`, and `ls /mnt/c/Users/giuli/.docker/daemon.json.bak` returns "No such file" (no needless backup).

---

### Task 3: `compact-vhdx.ps1` — out-of-WSL VHDX compaction (Layer 3)

**Files:**
- Create: `scripts/windows/compact-vhdx.ps1`

**Interfaces:**
- Consumes: nothing.
- Produces: a PowerShell script that (self-elevates), aborts if containers run, shuts down Docker + WSL, `diskpart compact vdisk` on both VHDX files (discovered at runtime), restarts Docker, and reports space recovered. **Cannot run from `\\wsl.localhost\...`** — must be copied to a Windows-local path (Task 4 documents this).

- [ ] **Step 1: Write the script**

```powershell
# compact-vhdx.ps1 — Layer 3: shrink WSL/Docker VHDX files back into C:.
# Must run OUTSIDE WSL (it shuts WSL down). Requires admin.
$ErrorActionPreference = 'Stop'

# Self-elevate
if (-not ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Start-Process powershell.exe "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`"" -Verb RunAs
    exit
}

function Get-SizeGB($p) { if (Test-Path $p) { [math]::Round((Get-Item $p).Length/1GB,2) } else { $null } }

# Discover VHDX paths at runtime
$lxss = Get-ChildItem HKCU:\Software\Microsoft\Windows\CurrentVersion\Lxss |
        ForEach-Object { Get-ItemProperty $_.PSPath } |
        Where-Object { $_.DistributionName -eq 'Ubuntu' } | Select-Object -First 1
$ubuntuVhdx = Join-Path ($lxss.BasePath -replace '^\\\\\?\\','') 'ext4.vhdx'
$dockerVhdx = Join-Path $env:LOCALAPPDATA 'Docker\wsl\disk\docker_data.vhdx'
$targets = @($dockerVhdx, $ubuntuVhdx) | Where-Object { Test-Path $_ }

Write-Host "== VHDX objetivo (antes) ==" -ForegroundColor Cyan
$targets | ForEach-Object { Write-Host ("  {0,-8} GB  {1}" -f (Get-SizeGB $_), $_) }
$cFreeBefore = [math]::Round((Get-PSDrive C).Free/1GB,1)

# Guardrail: abort if containers are running
$running = & wsl.exe -d docker-desktop docker ps -q 2>$null
if ($running) { Write-Host "[ABORT] Hay contenedores corriendo. Pará todo antes de compactar." -ForegroundColor Red; Read-Host "Enter para salir"; exit 1 }

Write-Host "`nCerrando Docker Desktop y WSL (esto cierra tu sesión WSL)..." -ForegroundColor Yellow
Get-Process 'Docker Desktop' -ErrorAction SilentlyContinue | Stop-Process -Force
Start-Sleep 3
wsl.exe --shutdown
Start-Sleep 5

foreach ($vhdx in $targets) {
    Write-Host "`nCompactando $vhdx ..." -ForegroundColor Cyan
    $script = @"
select vdisk file="$vhdx"
attach vdisk readonly
compact vdisk
detach vdisk
exit
"@
    $tmp = [System.IO.Path]::GetTempFileName()
    Set-Content -Path $tmp -Value $script -Encoding ASCII
    try { diskpart /s $tmp | Out-Host } catch { Write-Host "[WARN] diskpart falló en $vhdx, sigo con el resto." -ForegroundColor Yellow }
    Remove-Item $tmp -Force
}

Write-Host "`n== VHDX objetivo (después) ==" -ForegroundColor Cyan
$targets | ForEach-Object { Write-Host ("  {0,-8} GB  {1}" -f (Get-SizeGB $_), $_) }
$cFreeAfter = [math]::Round((Get-PSDrive C).Free/1GB,1)
Write-Host ("`nC: libre: {0} GB -> {1} GB (recuperado ~{2} GB)" -f $cFreeBefore, $cFreeAfter, [math]::Round($cFreeAfter-$cFreeBefore,1)) -ForegroundColor Green

$dd = Join-Path $env:ProgramFiles 'Docker\Docker\Docker Desktop.exe'
if (Test-Path $dd) { Start-Process $dd }
Read-Host "Listo. Enter para cerrar"
```

- [ ] **Step 2: Syntax check (parse only, no run)**

Run: `powershell.exe -NoProfile -Command "\$null = [System.Management.Automation.PSParser]::Tokenize((Get-Content -Raw '\\\\wsl.localhost\\Ubuntu\\home\\simonll4\\projects\\scripts\\windows\\compact-vhdx.ps1'), [ref]\$null); echo PARSE_OK"`
Expected: `PARSE_OK`

- [ ] **Step 3: Supervised real run** (only when `C:` is tight and no containers run)

First stop everything: `cd /home/simonll4/projects/e-ovrt_media-plane/infra && docker compose down` (or ensure `docker ps -q` is empty).
Then, from Windows (after Task 4's copy step), right-click `compact-vhdx.ps1` → Run with PowerShell.
Expected: UAC prompt → "antes" sizes → shutdown → two diskpart compactions → "después" sizes smaller → C: free increased by ~60–75GB → Docker Desktop restarts.

- [ ] **Step 4: Verify recovery**

Run (back in WSL after Docker restarts): `df -h /mnt/c`
Expected: `Avail` on `/mnt/c` grew substantially vs the 40GB baseline.

---

### Task 4: Operator guide

**Files:**
- Create: `scripts/README-disk-control.md`

- [ ] **Step 1: Write the guide**

```markdown
# Control de disco Docker/WSL

Tres capas para que Docker no llene `C:`.

## Capa 1 — Prevención (una vez)
    scripts/docker/setup-prevention.sh
Verifica/fija el cap de build cache (20GB) en daemon.json. Luego, manual:
Docker Desktop → Settings → Resources → Disk image size → ~100GB.

## Capa 2 — Limpieza rápida (después de buildear, en WSL)
    scripts/docker/docker-clean.sh          # conserva imágenes eovrt/*
    scripts/docker/docker-clean.sh --all    # borra también imágenes tagueadas no usadas
Libera espacio dentro del VHDX. No achica C: todavía.

## Capa 3 — Compactar (cuando C: esté justo, desde Windows como admin)
NO se puede correr desde \\wsl.localhost — apaga WSL a mitad.
1. Copiá una vez:  scripts/windows/compact-vhdx.ps1  ->  C:\Users\giuli\eovrt-tools\
2. Pará contenedores (docker compose down).
3. Click derecho el .ps1 -> Run with PowerShell (pide UAC).
Devuelve ~60-75GB a C:.

## Umbral sugerido
Corré la Capa 3 cuando `df -h /mnt/c` muestre <30GB libres.
```

- [ ] **Step 2: Copy the PowerShell script to a Windows-local path (one-time install)**

Run: `mkdir -p /mnt/c/Users/giuli/eovrt-tools && cp scripts/windows/compact-vhdx.ps1 /mnt/c/Users/giuli/eovrt-tools/ && ls -la /mnt/c/Users/giuli/eovrt-tools/`
Expected: `compact-vhdx.ps1` listed under the Windows-local tools dir (from where it can self-elevate and shut WSL down safely).

---

## Self-Review

**Spec coverage:** Layer 1 → Task 2 (+manual UI step documented). Layer 2 → Task 1 (with `--all` flag). Layer 3 → Task 3. Error handling (daemon guard, running-container abort, per-VHDX continue-on-fail, daemon.json backup+validate) → covered in Tasks 1–3. Testing (real reclaimable-cache run, idempotent no-op, supervised compaction) → covered. Operator doc + install copy → Task 4. No gaps.

**Placeholder scan:** no TBD/TODO; all code is complete and runnable; paths are concrete.

**Type/name consistency:** `daemon.json` path, distro name `Ubuntu`, VHDX discovery, and `20GB` keep value are consistent across Tasks 2–3 and the spec.

**Discovered during planning:** the `builder.gc` cap is *already* in `daemon.json` (from the 2026-07-05 cleanup), so Task 2 is expected to be a no-op — it exists as a verifier/restorer, which is the correct idempotent behavior.
