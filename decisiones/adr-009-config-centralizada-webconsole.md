# ADR-009 — Configuración centralizada en experimental-setup y webconsole como superficie de gestión

- **Fecha:** 2026-07-09
- **Estado:** Aceptada
- **Decisión que atiende:** nueva (decisión del usuario). Amplía ADR-004 y ADR-008;
  se registra en el alcance (doc 10, ítem 11).
- **Decisor:** usuario, 2026-07-09

## Decisión

1. **Toda la configuración experimental se centraliza en `e-ovrt_experimental-setup`**
   (versionada en ese repo): manifiestos paraguas, run configs del media-plane, run
   configs / pattern sets del control-plane, prompt sets (`eind_v1`, `edir_v1`),
   tuning. Los servicios **reciben la config al disparar la corrida** (payload o
   referencia vía API) y siguen persistiendo su `effective_config` en los artefactos
   de la corrida — la trazabilidad "alerta → configuración" no cambia de mecanismo.
2. **Qué NO se centraliza:** la config operacional de cada servicio (puertos, env,
   `EOVRT_MODEL_REF`, deployment/compose) y los catálogos por id que cada plano ya
   expone (regla previa: el media-plane conserva contrato + catálogos). La frontera
   es: *lo que varía entre corridas/experimentos vive en experimental-setup; lo que
   define el despliegue vive con el servicio*.
3. **La webconsole es la superficie de gestión primaria de la plataforma**: crear/
   editar/seleccionar configs de experimento, disparar corridas en ambos planos
   (clientes HTTP de media-plane y control-plane, ADR-008), monitorear estado, ver
   alertas (ADR-005) y agrupar por `experiment_id`. Esto exige una **mejora de UI y
   reorganización UX** (navegación por experimento como eje, no por servicio).
4. El **runner CLI (ADR-004) se conserva** como camino headless y reproducible para
   campañas (R1–R4 congeladas se corren por runner, no a mano por UI). Webconsole y
   runner usan **las mismas APIs y las mismas configs** — cero lógica duplicada.

## Alternativas consideradas

- **Configs en cada repo + manifiesto que solo referencia** (ADR-004 original):
  funciona, pero fragmenta la edición en tres repos y hace imposible una UI de
  gestión coherente sin acoplarla a los filesystems de cada repo.
- **Webconsole como orquestador con estado propio:** sigue descartada (doc 07 D4.1)
  — la consola gestiona y dispara, pero el estado de corrida vive en los servicios y
  los artefactos, y la campaña reproducible es del runner.

## Fundamento

- Un solo lugar versionado para "qué se corre" es la materialización práctica del
  `RunConfig` de Etapa 3 (§17.3.6) sin config monolítica: el manifiesto y sus partes
  viven juntos, los servicios siguen siendo config-driven.
- Coherente con la regla previa del proyecto: experimental-setup ya era el dueño de
  la declaración de experimentos (prompts + run configs); esto la completa con las
  configs del control-plane.
- La demo de la defensa (R4) gana: una sola pantalla gestiona la plataforma entera.

## Impacto

- **experimental-setup (spec 44):** estructura de carpetas de configs por
  experimento; API de la webconsole para CRUD de configs + disparo; rediseño
  UI/UX (navegación por experimento; media-plane y control-plane como recursos).
- **control-plane (spec 41):** el servicio mínimo (ADR-008) acepta config por
  payload/referencia, no solo path local.
- **media-plane (spec 42):** verificar que `POST /api/runs` acepte la config
  completa por payload (hoy referencia catálogos por id — se conserva).
- **Alcance (doc 10, ítem 11):** la mejora UX es lo primero sacrificable del
  proyecto; la centralización de configs no se sacrifica (la usa también el runner).

## Referencias

ADR-004, ADR-005, ADR-008; doc 07 D4.1; §17.3.6 (RunConfig); memoria del módulo
experimental-setup (2026-07-01).
