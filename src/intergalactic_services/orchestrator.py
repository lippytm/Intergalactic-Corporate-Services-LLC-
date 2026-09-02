"""Hermes routing and governed swarm dispatch."""

from collections.abc import Iterable

from .models import AgentProfile, Task, TaskResult
from .policies import GovernancePolicy


class HermesOrchestrator:
    def __init__(
        self,
        agents: Iterable[AgentProfile] = (),
        policy: GovernancePolicy | None = None,
    ) -> None:
        self._agents: dict[str, AgentProfile] = {}
        self.policy = policy or GovernancePolicy()
        for agent in agents:
            self.register(agent)

    def register(self, agent: AgentProfile) -> None:
        if agent.name in self._agents:
            raise ValueError(f"Agent already registered: {agent.name}")
        self._agents[agent.name] = agent

    def dispatch(self, task: Task) -> TaskResult:
        allowed, reason = self.policy.evaluate(task)
        if not allowed:
            return TaskResult(task.task_id, "blocked", None, reason)

        candidates = [
            agent
            for agent in self._agents.values()
            if agent.enabled and task.kind in agent.capabilities
        ]
        if not candidates:
            return TaskResult(
                task.task_id,
                "unroutable",
                None,
                f"No enabled agent supports capability: {task.kind}",
            )

        agent = min(candidates, key=lambda item: item.name)
        try:
            output = agent.handler(task)
        except Exception as exc:  # noqa: BLE001 - boundary converts failures to audit results
            return TaskResult(task.task_id, "error", agent.name, str(exc))
        return TaskResult(task.task_id, "completed", agent.name, reason, output)
