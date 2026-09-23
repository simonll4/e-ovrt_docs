# 132 — El paquete de evidencia para el jurado (2026-09-23)

**Por qué existe este doc.** `operacion/126` fijó el criterio de qué respaldar, pero su
ejecución era un espejo por `rsync` a un directorio de staging, pensado para backup y no
para que alguien lo mire. Cuando el pedido pasó a ser **darle acceso al jurado —y a quien
lo solicite— para que vea resultados, evidencia y videos**, el artefacto dejó de ser un
backup y pasó a ser un entregable con audiencia. Este doc registra qué se entregó, la
decisión de diseño que lo hizo chico, y **un hallazgo de licencias que estuvo a un paso de
poner al informe en contradicción consigo mismo delante del jurado**.

**Estado: cerrado.** El paquete está armado y verificado; falta que el usuario lo suba a
Drive y lo configure en modo «Restringido».

---

## 1. Qué se entregó

En `C:\Users\giuli\E-OVRT-VDP-evidencia\` (desde WSL, `/mnt/c/Users/giuli/...`), armado por
**`scripts/empaquetar_evidencia.py`** — stdlib pura, sin dependencias, con `--simular`,
`--solo <colección>` y `--forzar`.

| Carpeta | Peso | Destino |
|---|---|---|
| `Evidencia-compartida/` | **4,8 GB** | Drive en modo **«Restringido»**: el enlace muestra *Solicitar acceso* y el usuario autoriza uno por uno. Sirve igual para el jurado que para un interesado que escriba |
| `Respaldo-privado/` | **7,3 GB** | **No se comparte con nadie.** Backup propio |
| `MANIFIESTO.txt` | — | sha256, peso y cantidad de archivos de cada paquete |

**Compartida** — lo mirable va **suelto** y lo voluminoso en zip. La distinción no es
cosmética: Drive reproduce un `.mp4` en el navegador, pero un `.mp4` dentro de un `.zip` no
se puede ver, y ver la plataforma funcionando es todo el punto de la carpeta.

- `1-ver-la-plataforma-funcionando/` — los 5 videos de defensa **sueltos** (105 MB) con
  `00-que-es-cada-video.txt`.
- `2-banco-de-video-y-su-GT/` — los **34 clips del rodaje propio sueltos** (1,00 GB), el GT
  humano en zip, y `00-DE-DONDE-SALE-CADA-CLIP.txt` (ver §3).
- `3-artefactos-de-resultados/` — 11.503 archivos, 74 MB: el artefacto detrás de cada cifra.
- `4-fine-tuning/` — checkpoints de Mendieta (1,92 GB) y las evaluaciones del NO-GO (1,53 GB).
- `5-datos-de-campana/` — 11.326 archivos, 161 MB.

**Privada** — rodaje crudo (5,46 GB), anotación (1,06 GB), lote de internet (710 MB), clip
retirado `cb_b01_p7` (18 MB), y **la raíz del workspace** (31 KB): `CLAUDE.md`, `AGENTS.md`
y `scripts/`, que es el agujero declarado en `126` §2.1 y que el script anterior no copiaba.

## 2. La decisión que lo hizo chico: GitHub navega, Drive deposita

El paquete iba a pesar 13 GB en la primera versión y terminó siendo mucho menos trabajo,
porque **buena parte de la evidencia ya está versionada y online**:

| Ya en GitHub, no se empaqueta | Sólo esto necesita el paquete |
|---|---|
| los 12 `.md` y las métricas de `results/` (511 archivos) | los artefactos `.gz` de `results/` |
| `bench_v3` y sus estratos (10/10) | los 5 videos de defensa (gitignorados) |
| el GT de `clip_bench` (261/261) | los clips del rodaje |
| `docs/informe` completo (231/231) | checkpoints, corridas de FT, datos de campaña |

`results/` es un sitio markdown autocontenido: índice, cuatro sub-índices y ejes, con
enlaces relativos que no salen de la carpeta. GitHub ya lo renderiza. **La capa de
navegación no había que construirla, había que enlazarla.**

Por eso la entrada del jurado **no** es la carpeta de Drive sino una página del repositorio
público que reproduce los cuatro pasos de `results/evidence-vista/recorrido.yaml` —cada uno
con su claim, su cifra y su fuente— y enlaza a Drive para lo pesado. Esa página queda
pendiente: necesita el enlace de Drive, que todavía no existe.

## 3. El hallazgo: los clips del lote de internet no pueden ir

Al revisar el primer armado apareció que la carpeta compartida contenía **los 13 clips
`v*` del lote de internet** (@HospitalConstruction) y `cb_b01_p7`. Son dos problemas
distintos y conviene no mezclarlos.

**El lote de internet.** El usuario propuso incluirlos citando la lista de reproducción, con
el argumento —razonable— de que con la fuente a la vista no se rompe ninguna regla. La
revisión del texto del informe mostró otra cosa: **la v0.1 afirma cuatro veces que ese
material no se redistribuye.**

- §17.5 — *"Los videos maestros del lote se obtuvieron de la lista de reproducción pública
  de YouTube ... y **no se redistribuyen**."*
- Tabla F.1 — *"Licencia estándar de YouTube, no Creative Commons. Uso académico y
  evaluativo declarado por el proyecto, **con cita y sin redistribución**."*
- Anexo F — *"esa declaración no equivale a una licencia de libre reutilización ni a una
  conclusión jurídica sobre permisos."*
- Y el encuadre general — *"**que un video sea públicamente visible no acredita autorización
  para redistribuirlo**."*

La regla no era externa: **era del proyecto, escrita en el documento que el jurado lee.**
Compartir los clips habría puesto al jurado delante de un informe que dice "sin
redistribución" y una carpeta que los distribuye. Decisión del usuario: **se sacan**, y la
atribución se hace igual de visible.

`00-DE-DONDE-SALE-CADA-CLIP.txt` queda entonces con el canal y la
[lista de reproducción](https://www.youtube.com/playlist?list=PLVG3-xIaXtKzAC9JJnZJUY4aBCg0BNPKV),
y explica que la ausencia es decisión declarada y no un faltante: **de esos 13 clips sí
están el GT humano, las anotaciones y todas las métricas**, así que ninguna cifra del banco
pierde verificabilidad; lo único que falta es el archivo de video, que se baja del enlace.

**`cb_b01_p7` es otro caso.** Su retiro del banco (2026-08-03) tiene como motivo #1
consentimiento sin registrar sobre ~10-12 operarios que **no son del proyecto**, más GT
generado por IA. **La atribución no toca ninguno de los dos motivos**, así que no vuelve
por esta vía. Queda en el respaldo privado, en su propio zip.

**Consecuencia registrada en `datasets/registry/license_registry.md`:** la condición de no
redistribución **ya no se cumple sola**. Antes bastaba el gitignore, porque el repositorio
era el único canal de salida; ahora hay un segundo —el paquete— donde hay que excluirlos a
mano. La fila del lote lo dice, y advierte que **quien agregue un canal de distribución
nuevo tiene que replicar la exclusión ahí**. Se agregó además una nota de que el texto
publicado en el informe no se toca: si alguna vez se decidiera lo contrario, no alcanza con
editar el registro — hay que corregir el informe en §17.5, Anexo F y Tabla F.1.

## 4. La trampa de disco: `df -h /` miente en WSL

La corrida anterior del script viejo (12-sep) **se había interrumpido por falta de espacio**,
y el motivo no se ve desde adentro de WSL:

- `df -h /` informa el ext4 **virtual** — decía 857 GB libres.
- El techo real es **`C:`**, porque el `ext4.vhdx` crece sobre él. Tenía **34 GB**.
- Y **borrar adentro de WSL no le devuelve espacio a `C:`**: el VHDX no se achica solo.

Por eso el paquete se escribe **a `/mnt/c`**, donde borrar sí libera, y por eso el staging
`_evidencia-drive/` de 28 GB —que era copia pura de cosas todas presentes en el workspace—
**se borró**: liberó 27 GB de ext4 para que las escrituras futuras reusen ese hueco en vez
de seguir inflando el VHDX. **Regla operativa: mirar `df -h /mnt/c`, nunca `df -h /`.**

El script incorpora dos defensas que salen de acá: una **guardia de colchón** que aborta
limpio si escribir dejaría menos de 8 GB libres en `C:` (y que mide el trabajo **pendiente**,
no el inventario, para no pedir espacio por lo que ya está escrito), y la escritura a
`.parcial` con `rename` al terminar, de modo que **una interrupción no puede dejar un
archivo a medias que parezca completo** — que es exactamente lo que había pasado.

## 5. Verificación

Las 12 colecciones cierran con `unzip -t` más conteo de entradas contra el origen, y sha256
al manifiesto. Comprobaciones independientes del resultado:

- **0 archivos** del lote de internet o de `cb_b01_p7` en la carpeta compartida, ni sueltos
  ni dentro de ninguno de los 5 zips.
- **0 rutas** de credenciales (`cameras/`, `.env`) en ningún paquete: el script las excluye
  por nombre, además de las exclusiones de entorno y caché.
- **0 archivos** `.parcial` remanentes.
- Los 17 orígenes del staging seguían presentes en el workspace antes de borrarlo.

## 6. Lo que queda

1. **Subir** `Evidencia-compartida/` a Drive y ponerla en «Restringido». `Respaldo-privado/`
   va al Drive personal y no se comparte.
2. **La página del repositorio público** con el recorrido de cuatro pasos, el enlace a Drive
   con la nota de solicitar acceso, y la cita de la lista de reproducción —que en una página
   pública tiene más sentido que dentro de una carpeta restringida.
3. `126` queda como **criterio**; este doc es la **ejecución**. Sus tamaños por capa son del
   19-ago y quedaron cortos (ver la nota ✎ en `126` §2).
