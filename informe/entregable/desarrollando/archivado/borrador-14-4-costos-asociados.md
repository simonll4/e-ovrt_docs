# Borrador — §14.4 Costos asociados al proyecto

- **Fecha:** 2026-09-11 · **Estado:** borrador v0.1 para revisión del usuario
- **Destino:** reemplaza `[Se completará más adelante.]` en §14.4 del maestro
- **Formato:** prosa y lista, **sin tabla numerada** (una tabla acá corre la numeración de §15/§16)
- **Respaldo de cifras:** `docs/operacion/datos/costos-proyecto-2026-09-11.csv`
- **Pendientes marcados `[confirmar …]`:** ver §Notas editoriales al final

---

### 14.4. Costos asociados al proyecto

El proyecto se autofinancia con recursos de los integrantes y no requiere desembolsos significativos. Esa característica no es casual sino una consecuencia de tres decisiones de diseño. La plataforma se despliega en forma local sobre equipamiento propio, el cómputo intensivo de ajuste fino se deriva a un clúster institucional y toda la cadena de software se construye con componentes de código abierto y conjuntos de datos publicados bajo licencias abiertas.

Los gastos previstos para la realización del trabajo, agrupados según las categorías que fija el formato institucional, son los siguientes.

- **Movilidad.** Un único traslado del equipo a las instalaciones de la empresa Steel Brox S.R.L., en la ciudad de Córdoba `[confirmar sede]`, para la jornada de captura de video con escenas guionadas. Las reuniones de tutoría no generan traslados adicionales.
- **Alquiler de servidores o VPS.** No se contrata. Los tres servicios de la plataforma corren en un mismo equipo local y el entrenamiento de modelos se ejecuta en el clúster Mendieta del Centro de Computación de Alto Desempeño de la Universidad Nacional de Córdoba, cuyo acceso es institucional y sin cargo.
- **Licencias de software.** Sin costo. El conjunto de herramientas de desarrollo, inferencia y despliegue es íntegramente de código abierto, y los conjuntos de datos se usan bajo licencias abiertas con atribución.
- **Suscripciones.** No se contratan servicios pagos. El control de versiones y el resguardo de la evidencia experimental usan los planes gratuitos de GitHub y Google Drive. `[confirmar: ¿hubo planes pagos de asistentes de código con IA u otros servicios?]`
- **Impresiones.** Sin costo. El informe y sus anexos se entregan en formato digital.
- **Consumibles del trabajo de campo.** Sin costo. El casco y el chaleco reflectivo empleados como utilería son prestados por la misma empresa que facilita el espacio de grabación, y la cámara de borde es prestada por el tutor.

En consecuencia, el gasto efectivo previsto se reduce al combustible del traslado mencionado. La evaluación económica completa del proyecto, que valoriza además las horas de trabajo, el equipamiento aportado y el cómputo institucional, se desarrolla en la sección 17.2.

---

## Notas editoriales (no van al informe)

**Pendientes del usuario**
1. `[confirmar sede]` — el local de Steel Brox visitado (la empresa tiene sedes en Córdoba Capital, Santa María de Punilla y Valle Hermoso). Si fue fuera de la ciudad, corregir "en la ciudad de Córdoba".
2. Monto del traslado (combustible o pasajes). Sin ese dato, §17.2 deja el total de gasto efectivo como `[monto]`.
3. Suscripciones — asumí **ninguna paga**. Si se usaron planes pagos de asistentes de IA (Claude, ChatGPT, Codex, Copilot) u otro servicio, el formato los pide explícitamente en esta categoría y hay que agregar la línea con el monto.

**Coherencia con otras secciones**
- La frase "tres servicios de la plataforma" es consistente con §17.3/§17.4 (medios, control, distribución).
- "Cámara de borde prestada por el tutor" — en Anexo B (Tabla B.2) figura como "Edge Node candidato"; no hay contradicción.
- Las cifras (semanas, horas, montos) **no aparecen acá a propósito**: viven en §17.2 para no duplicar.

**Reglas verificadas**
- Sin referencias a documentación local (autocontención). Sin ":" ni ";" en prosa. Voz en presente para lo que existe.
