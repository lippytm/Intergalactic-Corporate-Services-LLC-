# Repository Portfolio — Ecosystem v0.1

This document is the first canonical portfolio map for the Intergalactic Corporate Services LLC GitHub ecosystem.

## Portfolio principles

1. **One corporate backbone.** `Intergalactic-Corporate-Services-LLC-` is the umbrella governance and architecture repository.
2. **One Control Tower.** `lippytm-lippytm.ai-tower-control-ai` is the operational AI Copilot / orchestration application unless superseded by an approved architecture decision.
3. **Specialized repositories remain specialized.** Hermes, Clone, Prompt #11, bot families, Web3, publishing, and other domain repositories feed capabilities into the shared system rather than duplicating the whole platform.
4. **No destructive consolidation.** Overlap is documented first; repositories are not deleted, renamed, or merged without explicit human approval and migration evidence.
5. **Every active repository needs a user problem, measurable outcome, QA gate, lifecycle state, and—where applicable—a revenue hypothesis.

## Classification model

- **Core Platform** — shared orchestration, governance, runtime, identity, schemas, or control-plane capabilities.
- **Adapter** — connector or integration layer for an external system/provider.
- **Application** — end-user or operator-facing product built on the core platform.
- **Product / IP** — publishing, media, curriculum, characters, research, or commercial content assets.
- **Experiment / R&D** — exploratory technology or concepts not yet production-certified.
- **Infrastructure** — hosting, deployment, automation, CI/CD, observability, data services.
- **Archive Candidate** — superseded or redundant repository pending evidence-based retirement review.

## Canonical core map

| Repository | Proposed role | Classification | Current evidence | Next action |
|---|---|---|---|---|
| `lippytm/Intergalactic-Corporate-Services-LLC-` | Corporate umbrella, governance, architecture, common contracts | Core Platform | README already defines Clone identities, Hermes, Fabric, Swarms, approvals, audit-ready results | Keep as canonical governance root |
| `lippytm/lippytm-lippytm.ai-tower-control-ai` | AI Copilot / Control Tower runtime and connector hub | Core Platform + Application | Existing Express server includes connectors, swarm lifecycle, auth, data sync, CI/CD | Align with common task/agent/workflow/audit contracts |
| `lippytm/Hermes-AI-Hermes` | Hermes routing/orchestration specialization | Core Platform / R&D | Current README states Hermes should serve all repositories | Define router contract, capability registry, risk-aware eligibility |
| `lippytm/AI-Clone-of-Charles-Earl-Lipshay-lippytm-lippytm.AI-lippytmai-` | Clone identity and specialist-agent R&D | Core Platform / R&D | Repository exists but README is currently only a title | Add clone profile schema, consent, permissions, provenance, limits |
| `lippytm/AI-Autonomous-Systems-for-all-of-my-lippytm.ai-Repositories-Research-and-Development-integration-` | Cross-repository automation/integration research | Infrastructure / R&D | README describes autonomous integration across repositories | Convert ideas into bounded automation contracts and approval gates |
| `lippytm/Prompt-11-` | Product/workflow/QA knowledge system | Product / IP + Core Knowledge | Mature governance, RiskGate, continuation, evidence, ledger, publishing, learning architecture already documented | Expose reusable schemas/workflows to Tower Control rather than duplicating them |

## First application families

| Repository family | Role in ecosystem | Classification | Initial business/use outcome |
|---|---|---|---|
| `Chatlippytm.ai.Bots` | Chat-based agents and assistants | Application | Reusable customer-facing or internal assistants |
| `Clawlippytm.Bots`, `Clawlippytm.ai.Bots`, `OpenClaw-lippytm.AI-`, `MyClaw.lippytm.AI-` | Agent/action automation family | Application / R&D | Safe action-taking agents with bounded permissions |
| `Web3AI` | Web3/blockchain research and applications | Application / R&D | Research, education, analytics, provenance, product concepts |
| `AI-Time-Machines`, `Time-Machines-Builders-` | Time-machine themed research/education/IP | Product / IP + R&D | Educational/creative products and simulations |
| `The-Encyclopedia-of-Everything-Applied-ChatAIBots` | Encyclopedia + AI bot delivery | Product / IP + Application | Structured educational/entertainment product line |
| `Evolutionary-Evolutions-Social-Multimedia-Networks-Agency-` | Social/content distribution | Application | Content operations and audience growth |
| `AI-Intergalactic-Zoological-Social-Multimedia-Agency-Networks-` | Creative social/media IP system | Product / IP + Application | Media/community experiments |
| `lippytmai.getbizfunds.com-` | Funding/business-development web presence | Application | Funding funnel and business-plan support |
| `lippytmai.zo.computer-` | Zo-hosted runtime/workspace integration | Infrastructure / Application | Portable execution and business continuity |

## Platform contracts to standardize next

### `RepositoryProfile`
Minimum fields:
- repository id and full name
- canonical role
- classification
- business domain
- lifecycle state
- visibility
- default branch
- owners / responsible agent
- deployment target
- dependencies
- data sensitivity class
- revenue role / hypothesis
- quality state
- last reviewed timestamp

### `AgentProfile`
Minimum fields:
- stable agent id
- name and role
- capabilities
- allowed repositories
- allowed tools/actions
- prohibited actions
- risk ceiling
- required approval classes
- budget / usage limits
- provenance and model/provider metadata
- lifecycle state

### `Task`
Minimum fields:
- task id
- objective
- repository scope
- required capabilities
- input references
- risk class
- approval requirements
- expected output contract
- budget / time limits
- provenance context

### `TaskResult`
Minimum fields:
- task id
- executing agent
- status
- evidence/references
- changed resources
- test/validation results
- cost/usage metadata
- reason / decision record
- follow-up actions
- human approval state

### `AuditEvent`
Minimum fields:
- event id
- timestamp
- actor/agent
- action
- target
- before/after references
- risk class
- approval evidence
- outcome
- trace/correlation id

## Ecosystem v0.1 priority sequence

1. Complete portfolio inventory for every accessible repository.
2. Assign one classification and lifecycle state to each repo.
3. Mark the six core repositories above as the first integration boundary.
4. Define shared JSON schemas for `RepositoryProfile`, `AgentProfile`, `Task`, `TaskResult`, `Approval`, `Workflow`, and `AuditEvent`.
5. Add a repository scanner to Tower Control that emits `RepositoryProfile` records.
6. Add a Hermes routing proof-of-concept using capabilities + risk ceiling + repository scope.
7. Register three initial agents: Portfolio Chief of Staff, GitHub DevOps, and QA/Security.
8. Run one bounded three-agent swarm against a low-risk repository-health task.
9. Record all decisions/results as audit events.
10. Require human approval before merges, destructive changes, external publication, financial actions, credential use, or sensitive-data operations.

## Initial KPIs

- % of repositories inventoried
- % with classification and lifecycle state
- % with README / purpose / owner / QA state documented
- number of duplicate capability areas identified
- number of shared contracts implemented
- number of automated health checks passing
- number of audited agent tasks completed
- AI cost per successful task
- cycle time from issue to verified result
- revenue experiments launched and validated

## Revenue-growth rule

Do not equate repository count or generated code volume with growth. A repository contributes to business growth only when it is connected to a real user/customer problem, has a measurable outcome, meets its QA/security gate, and has a delivery or monetization path where appropriate.

## Current decision

For Ecosystem v0.1, the corporate repository is the governance root and Tower Control is the preferred operational control plane. Hermes, Clone, Prompt #11, and autonomous-integration repositories are capability sources feeding that control plane. This remains an architectural decision subject to review through a pull request before it becomes part of `main`.
