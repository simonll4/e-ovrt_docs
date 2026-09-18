# Herramientas de pases ya cerrados

Guiones de aplicación y verificación de pases que el usuario ya aceptó. Se conservan porque son la
constancia ejecutable de qué cambió cada pase: el enunciado de cada corrección vive en el código,
junto al texto que insertó o borró.

| Guion | Pase |
|---|---|
| `aplicar_pase6.py` · `verificar_anclas_pase6.py` | §17.1, pase 6 (desacople normativo, 2026-09-01) |
| `aplicar_v112_17_1.py` … `aplicar_v115_17_1.py` | §17.1, ciclo de reestructuración v1.12 a v1.15 (2026-09-03) |
| `aplicar_v16_17_3.py` · `verificar_v16_17_3.py` | §17.3, pase 4 (2026-09-03) |
| `aplicar_v17_17_4.py` · `aplicar_v14_17_5.py` · `verificar_pase_17_4_17_5.py` | §17.4 y §17.5, pase 4 (2026-09-04) |

Todos reescribían el párrafo entero en cada edición. El motor que los reemplaza,
`herramientas/pase_docx.py`, hace edición **quirúrgica**: marca como borrado sólo el tramo que
cambia. `aplicar_v17_17_4.py` es su antecedente directo y de ahí salieron los primeros helpers.

**Lo que sigue vivo en `herramientas/`:** `extraer_informe.py` (regla D-C), `verificar_entregable.py`,
`generar_project_kit.py`, `indice_xml.py`, y la cadena del pase 5 —`pase_docx.py`,
`rechazar_cambios.py`, `verificar_paquete.py` y los cinco `pase5_*.py`—.

## Archivado del 2026-09-18: los guiones de los pases 5 → Etapa 6 y Etapa 0

El informe final está completo (`informe/entregable/desarrollando/E-OVRT-VDP_Informe_Final_2026-09-16_v0.1.docx`),
así que los guiones de un pase concreto ya ejecutado pasaron acá, por el mismo criterio que los de arriba:

| Guion | Pase |
|---|---|
| `pase5_15_16.py` · `pase5_17_1.py` · `pase5_17_3.py` · `pase5_17_4.py` · `pase5_17_5.py` | Pase 5 sobre las cinco secciones (2026-09-06/07) |
| `pase5b_config_entrenamiento.py` · `pase5c_tabla59.py` · `pase5d_revision.py` · `pase5e_cierre.py` | Incrementales 5b/5c/5d (09-07) y 5e (09-08) |
| `pase_etapa6_cierre.py` · `pase_etapa6_v13.py` · `pase_etapa6_v15_consola.py` | Etapa 6: v1.0→v1.1, v1.2→v1.3, v1.4→v1.5 (09-09 → 09-13) |
| `pase_secciones_iniciales_v11.py` | Etapa 0 (§2–§14) v1.0→v1.1 (09-12) |
| `generar_docx_costos.py` | §14.4/§17.2 desde los borradores markdown (09-11); único uso |

Todos importan `pase_docx` desde `herramientas/` y leen sus bases desde `informe/entregable/desarrollando/archivado/`
(rutas hardcodeadas). Para repetir uno: `cd docs && PYTHONPATH=herramientas python3 herramientas/archivado/<guion>.py`
— y verificar que las rutas de entrada apunten a las bases archivadas.

**Lo que sigue vivo en `herramientas/` (2026-09-18):** `extraer_informe.py` (regla D-C: re-extraer cada bajada del
informe), `verificar_entregable.py`, `generar_project_kit.py` (kit histórico; se conserva por si hay correcciones del
jurado), `indice_xml.py`, `verificar_paquete.py`, `pase_docx.py` (motor de edición quirúrgica), `rechazar_cambios.py`
y `reparar_enlaces.py`.
