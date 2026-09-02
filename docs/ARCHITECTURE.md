# Architecture

## Operating model

1. An application submits a typed `Task`.
2. Governance evaluates its risk class and approval evidence.
3. Hermes selects an enabled clone with the required capability.
4. The selected handler performs one bounded operation.
5. A structured `TaskResult` records status, agent, reason, and output.

## Layers

- **Application adapters:** future web, CRM, publishing, finance, GitHub, and communications interfaces.
- **Hermes:** deterministic task routing and capability matching.
- **Fabric:** reusable workflows composed from bounded tasks.
- **Swarm:** specialist clone profiles coordinated through Hermes.
- **Governance:** approval, identity, privacy, budget, and audit policies.
- **Infrastructure:** queues, storage, observability, secrets, and deployment.

Integrations must depend on adapter interfaces instead of embedding provider-specific logic in core orchestration.
