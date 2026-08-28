# Etapa 2 — pase 2: verificación de la entrega v1.2 y cierre en v1.3 (2026-08-28, noche)

> **Qué es.** La revisión "de pie a cabeza" de la entrega de ChatGPT sobre §17.1
> (`E-OVRT-VDP_Seccion_17.1_Consolidacion_Metodologica_v1.2.docx`, 16:07) contra el texto base
> `90f` v1.0 y contra el pase [`correcciones-etapa-2.md`](correcciones-etapa-2.md). Resultado: **el
> contenido está bien y completo**; tres defectos de **forma** se repararon de manera determinista
> sobre el XML y el resultado es la **v1.3**, que pasa a ser el documento vigente de la etapa. La
> v1.0 (base) y la v1.2 (entrega) quedaron en `archivado/`.
>
> **Estado: APLICADO Y VERIFICADO. No hay trabajo de redacción pendiente sobre §17.1.** Lo que queda de
> la etapa es externo al `.docx` (§5).

---

## 1. Verificación mecánica

| Chequeo | v1.2 (entrega) | v1.3 (final) |
|---|---|---|
| `verificar_entregable.py --seccion 17.1` | **OK** (28.499 palabras · 118 títulos · `[[PENDIENTE]]`×1) | **OK** (28.534 · 118 · ×1) |
| Estilos de título | `Heading1` 1 · `Heading2` 1 · `Heading3` 11 · `Heading4` 41 · `Heading5` 65 — **§17.1.1 corregido** (E2-01) | ídem |
| Numeración | sin huecos; §17.1.10 (proyección) eliminada y §17.1.11/12 → §17.1.10/11 (E2-24) | ídem |
| Ecuaciones OMML | **85** (todas conservadas) | 85 |
| Runs que partan palabras con cambio de formato | **0** | 0 |
| Comentarios / cambios controlados | ninguno (la entrega vino sin cambios controlados; el diff se hizo contra `90f`) | — |
| Andamiaje (`AJ-`/`E2-`/`D-E2`/`R-`/rutas/ADR) | **0** (sólo los `P-E1-xx`, permitidos) | 0 |
| Cifras propias (no-anacronismo) | **0** — los únicos números nuevos son tamaños de dataset (SHEL5K 5.000, CHV 1.330), que son hechos de las fuentes | 0 |
| Marcadores | 1: el espejo de la AAIP (E2-25) | 1 |
| Referencias | avisos iguales a la v1.0 (Liu 2023/2024 · Wang 2021/2025: autores homónimos, no error) | ídem |

**Diff v1.0 → v1.2 (párrafos normalizados):** 667 → 629 párrafos · **59 nuevos** (1.948 palabras) ·
**97 eliminados** (5.402) · **113 modificados** (35 de ellos sólo terminología F5). Palabras:
32.669 → 28.499 (−12,8 %). Por sección: §17.1.6.2 **4.856 → 1.375** (PODA-12) · §17.1.10 eliminada
(PODA-13, 647 → párrafo puente) · §17.1.4 **3.138 → 2.666** (PODA-14, parcial: −472 contra ~1.000
esperadas; el detalle removido remite a las Tablas B.1–B.7, cuya correspondencia se verificó: B.1
CPN · B.2 EN/OAK-D · B.3 stack CPN · B.4 TN · B.5 stack TN · B.6 parámetros · B.7 topología) ·
§17.1.5 9.317 → 9.483 y §17.1.7 6.514 → 6.792 (**sólo inserciones**, guardrail respetado).
**Intactas** (filas idénticas): Tablas 24, 28, 36 y 37. **Intactos** (sólo el título a tipo frase):
§17.1.6.3 MOT17/OVT-B y §17.1.7.4.2 métricas MOT (D-E2-6).

## 2. Unidad por unidad

| Unidad | Estado | Evidencia en la v1.2 |
|---|---|---|
| E2-01 §17.1.1 estilo | ✅ | `Heading3`, sin tabulador |
| E2-02 16.7.6 → 16.7.3 | ✅ | §17.1.6.1.1, única aparición |
| E2-03 SO del CPN | ✅ | "El entorno de ejecución adoptado es Linux mediante WSL2 sobre el equipo descrito y contenedores Linux…"; `Windows` 4 → 0 (también en §17.1.4.6/.7) |
| E2-04 fuente EBE | ✅ | §17.1.4.2.3 reescrita (dos fuentes integrables; RTSP priorizada por disponibilidad; OAK-D posterior; ninguna presupone inferencia en borde); §17.1.4.2.4 retitulada *"Criterio de prioridad y fuente RTSP sintética"* |
| E2-05 resolución por perfil | ✅ | §17.1.4.5.1 |
| E2-06 PODA-14 | ◐ | −472 palabras; remisiones a B.1–B.7 correctas; sin "altas al Anexo B" (nada quedó sin destino) |
| E2-07 valores de persistencia | ✅ | frase exacta del texto guía al final de §17.1.5.3.3; Tabla 24 intacta; sin "efectivos" |
| E2-08 histéresis / episodio nuevo | ✅ | §17.1.5.3.4 |
| E2-09 bautismo E-DIR/E-IND/E-HYB | ✅ | glosa en §17.1.5.4.2; **primera y única aparición** de los tres códigos |
| E2-10 AJ-2.04 | ⊘ | sin cambios, como pedía |
| E2-11 piso muestral / bootstrap | ✅ | §17.1.5.4.5 Fase 1 |
| E2-12 criterio de aplicabilidad de la doble anotación | ✅ | §17.1.5.4.5 Fase 1 |
| E2-13 Tabla C.1 + acta · confianza media de TP · por entidad | ✅ | §17.1.5.4.4 y Fase 4 |
| E2-14 PODA-12 / Tabla 26 | ✅ | 4 retenidos (SHEL5K · CHV "sin licencia formal; cita obligatoria" · construction site safety · ppe siabar), Tabla 27 = descartados con causa en una línea, Tabla 29 aptitud de los 4, §17.1.6.4.1 licencias como el registro; Nota: "la retención expresa aptitud como candidato y no asignación efectiva" |
| E2-15 rango 500–2.000 | ⊘ ✅ | la regla se conserva en §17.1.6.2.4 ("justificarse si se apartan") |
| E2-16 MOT intacto | ✅ | ver §1 |
| E2-17 nota Tabla 36 | ✅ | "La secuencia expresa dependencias entre fases, no un calendario…" |
| E2-18 nivel "estado observable por persona" (AJ-2.13) | ✅ | párrafo de apertura de §17.1.7.3.1 |
| E2-19 diccionario / reparto | ✅ | frase nueva en §17.1.7.2 fijando `t_alert-system` y `t_alert-notification` (como texto, no como ecuación — ver §4) |
| E2-20 Tabla 35 | ✅ | conservada en §17.1.7.7.6 (el Anexo D se resuelve en `90g`) |
| E2-21 instrumentación | ⊘ | sin cambios de fondo; F5 en §17.1.7.8.1 |
| E2-22 aplicabilidad · regla de conteo · reglas de lectura | ✅ | §17.1.7.8.2 y §17.1.7.8.3 (por estrato y escenario · negativos fuera de P/R/F1 · SDR misma cadencia · latencia y episodios evaluables) |
| E2-23 ajuste fino como jornada | ✅ | párrafo en §17.1.9.2 ("criterios prerregistrados… de datos y de protocolo, no de disponibilidad de cómputo"); "presupuesto de tiempo/cronograma/plazo" 0 apariciones; §17.1.4.6 "sin convertir cómputo en criterio metodológico" |
| E2-24 PODA-13 párrafo puente | ✅ (reubicado, E2-29) | ver §3 |
| E2-25 marcador AAIP | ✅ (anclado, E2-28) | ver §3 |
| E2-26 AJ-2.02 | ⊘ | sin cambios, como pedía |
| Pase de formato F1–F6 | ✅ salvo F2/F3 (E2-27) | F1 títulos tipo frase ✓ · F4 puntos dentro de la negrita ✓ · F5 `cuadro` 4 → 44, `fotograma` 9 → 0, `tracking` 15 → 3 (`tracking-by-detection`, `TrackingNet`, *Multiple Object Tracking*), `end-to-end/E2E` 1 → 0 ✓ · F6 ✓ |

## 3. Tres defectos de forma, reparados sobre el XML → v1.3

| ID | Defecto en la v1.2 | Reparación (determinista, `document.xml`, validado con `ElementTree`) |
|---|---|---|
| **E2-27** | Los 23 rótulos `Tabla N` y las 21 notas venían en **negrita + itálica** (`***Tabla N***`, `***Nota***.`), contra la convención ya fijada en §15–§16 v1.0 y §17.5 v1.3 (`**Tabla N**` en negrita · `*Nota.*` en itálica; regla F2/F3 del pase 5 de la Etapa 1) | quitar `<w:i/>` de los runs de los 23 rótulos; quitar `<w:b/>` de los runs "Nota" y "." de las 21 notas. Resultado: 23 `**Tabla N**` · 21 `*Nota.*` |
| **E2-28** | El marcador `[[PENDIENTE: … aplicabilidad de esta inscripción …]]` quedó debajo de un párrafo que **no menciona ninguna inscripción** (habla de minimización y del régimen de datos personales): "esta inscripción" no tenía antecedente | se agregó al final del párrafo previo: *"Ese régimen prevé, además, la inscripción de las bases de datos con datos personales ante la autoridad de aplicación (AAIP); su aplicabilidad al material experimental del proyecto y el recaudo adoptado se documentan a continuación."* (+35 palabras). El marcador **no se tocó** y sigue viajando |
| **E2-29** | El párrafo puente de PODA-13 (*"Esta consolidación distribuye sus salidas hacia las instancias siguientes…"*) quedó **dentro de §17.1.9.2** (*Candidatos de comparación*), después de la nota de la Tabla 37 — fuera de tema | movido tal cual a **§17.1.11.2** (*Articulación con las instancias de diseño e implementación*), como segundo párrafo: es exactamente el tema de esa subsección y complementa su primer párrafo con qué toma cada instancia |

Diff v1.2 → v1.3 verificado por extracción: **sólo** esos tres cambios (un párrafo movido, una frase
agregada, formato de 44 rótulos). Verificador OK.

## 4. Residuales que NO se corrigen acá (anotados)

1. **PODA-14 parcial** (−472 palabras de ~1.000 estimadas). Lo removido quedó cubierto por B.1–B.7;
   no se fuerza más recorte: el guardrail es no cortar por cuota.
2. **`t_alert-system` / `t_alert-notification` en §17.1.7.2** están escritos como texto (con
   subíndice tipográfico) mientras en el resto del capítulo la sigla es un objeto de ecuación. Es
   legible (justo lo que pedía el pase 3 §I) y no se unifica: convertirlo a OMML a mano es más
   riesgoso que el beneficio. Se revisa en la integración final junto con los rótulos de nota del
   maestro.
3. Tabla 26: las filas de `construction site safety` y `ppe siabar` dicen *"Versión registrada"* en
   la columna de volumen. Es correcto pero pobre; si el equipo quiere el volumen, son hechos de
   las fuentes (2.799 y 1.607 imágenes) y pueden agregarse sin violar el no-anacronismo.
4. Los nombres de dataset se escriben con espacios (*construction site safety*, *ppe siabar*) y no
   como identificadores (`construction_site_safety`). §17.4/§17.5 deben usar la misma forma — se
   verifica en la integración.

## 5. Delta de referencias (para las Referencias globales del equipo)

**Bajas** por PODA-12/13/14 (ya no se citan en §17.1; **antes de sacarlas del listado global hay
que confirmar que ninguna otra sección las cite**): Ahmad y Rahimi, 2025 (SH17) · An et al., 2021
(MOCS) · Buslaev et al., 2020 (Albumentations) · Dalvi et al., 2025 (Construction-PPE) · Duan et
al., 2022 (SODA) · Ley 25.326, 2000 (sigue citada como *Argentina, 2000*) · Long y Li, 2023 · Mallick,
2025 · NJVisionPower, 2019 (SHWD) · Nath et al., 2020 y CIBER Lab, 2020 (Pictor-PPE) · Wu et al.,
2019 (GDUT-HWD). **Altas:** ninguna.

## 6. Lo que queda de la Etapa 2 — fuera del `.docx`

| Qué | Dónde | Estado |
|---|---|---|
| `90g-etapa2-anexos-c-y-d.md`: Anexos C y D corregidos (candidatos vs retenidos sin `chv` como entrenado; `bench_obra` no es dataset; Tabla C.1 fuente del prompt set; Anexo D → filas extra + remisión a Tabla 35) | texto base `96e` §19.3–19.4 | **pendiente** (D-E2-1) |
| Recortar la glosa de §17.3.6.4 a la remisión (dependencia inversa de E3-42) | §17.3 v1.4 → v1.5 | handoff Etapa 3 |
| Orden de disparo real (control → distribución → medios) y desviación 500–2.000 → 2.946 con causa | §17.4 v1.6 | handoff Etapa 4 |
| Declarar lo no ejercido del protocolo (templates, vocabulario cruzado, español, kappa/L2, MOT, confianza media de TP), `n=5.313` fechado, caveat del umbral tiny 800/560, `t_alert-system` = promedio | §17.5 v1.3 | handoff Etapa 5 |
| D-E1-11 (AAIP) | equipo | marcador viaja en §16.6.2.2 y §17.1.10.1 |

## 7. Cómo se re-verifica

```
python3 herramientas/verificar_entregable.py informe/entregable/desarrollando/E-OVRT-VDP_Seccion_17.1_Consolidacion_Metodologica_v1.3.docx --seccion 17.1
python3 herramientas/extraer_informe.py <v1.3> --out /tmp/v13.md ; python3 herramientas/extraer_informe.py desarrollando/archivado/<v1.2> --out /tmp/v12.md
diff <(sed -E 's/[*]+//g' /tmp/v12.md) <(sed -E 's/[*]+//g' /tmp/v13.md)      # sólo E2-28 y E2-29
grep -oE '^\**Tabla [0-9]+\**' /tmp/v13.md | sort | uniq -c ; grep -oE '^\**\*?Nota\*?\**\.?\**\*?' /tmp/v13.md | sort | uniq -c
grep -cE 'E-DIR|16\.7\.3|4\.000|estado observable por persona|bootstrap|re-alerta' /tmp/v13.md
```
