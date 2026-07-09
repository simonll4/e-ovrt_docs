# ADR-008 — Control-plane como servicio mínimo (deja de ser solo CLI)

- **Fecha:** 2026-07-09
- **Estado:** Aceptada
- **Decisión que atiende:** nueva (nota del usuario sobre doc 04; no estaba en el
  tablero D1–D6). **Modifica el alcance cerrado del doc 10 — excepción registrada.**
- **Decisor:** usuario, 2026-07-09

## Decisión

El control-plane suma un **servicio mínimo** (FastAPI, mismo patrón que el
media-plane) por encima del runtime live que ya estaba planificado (semanas 5–6):

- `POST` para disparar una corrida (replay o live/bus) desde una config referenciada,
- `GET` de estado de la corrida activa (un run activo por vez, como el media-plane),
- `GET` de la config efectiva.

**Explícitamente fuera:** gestión de modelos (no aplica — el plano no infiere),
sesiones, concurrencia de corridas, autenticación, retención — todo sigue amparado
por E-12 (prototipo experimental, sin hardening). La CLI (`replay`,
`validate-config`, `evaluate-alerts`) se conserva para uso offline y tests.

**Consecuencia para la webconsole:** pasa a ser **cliente de ambos planos** —
configura/dispara/observa el control-plane igual que hace con el media-plane, y
aloja la vista de alertas (ADR-005). El runner CLI (ADR-004) orquesta por HTTP a
los dos servicios.

## Alternativas consideradas

- **Runner CLI + proceso lanzado por script** (contención original de la auditoría,
  doc 07 D4.1): suficiente para la tesis, pero deja al control-plane como el único
  componente no operable desde la consola y duplica formas de ejecución en la demo.

## Fundamento

1. **Simetría arquitectónica**: los dos planos como servicios config-driven, la
   consola como cliente — simplifica la narrativa de plataforma y la demo EBE (R4).
2. El costo marginal es bajo (~1–2 días) porque el runtime live ya requería un
   proceso de larga vida suscripto al bus; el servicio es una cáscara HTTP sobre eso.
3. Habilita la configuración del control-plane desde la webconsole (pedido del
   usuario) sin que la consola orqueste (ADR-004).

## Registro en el alcance (doc 10)

Se agrega a la lista de "SÍ se implementa" como parte del ítem del bus/runtime
live, con esta regla: si la agenda aprieta, **se sacrifica la cáscara HTTP y queda
el runner CLI** (el runtime live no es sacrificable — lo exige EBE). E-12 no se
reabre: el servicio mínimo excluye todas las capacidades de producto que E-12 lista.

## Referencias

Doc 01 §2 (estado CLI), doc 04 (nota origen), doc 07 D4, doc 10 §2/E-12,
ADR-004, ADR-005.
