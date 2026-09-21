"""Built-in clone registry for governed Hermes routing."""

from .models import AgentProfile, Task

BUILTIN_AGENT_SPECS = (
    (
        "ai-jarvis-assistant",
        "assistant",
        {"assistant", "intake", "research", "triage"},
    ),
    (
        "engineer-manager",
        "engineering_management",
        {"delivery", "engineering", "planning", "review"},
    ),
    (
        "communications-manager",
        "communications_management",
        {"communications", "messaging", "outreach", "publishing"},
    ),
)


def _bound_handler(agent_name: str, role: str):
    def handle(task: Task) -> dict[str, object]:
        return {
            "agent": agent_name,
            "role": role,
            "task_kind": task.kind,
            "payload": task.payload,
        }

    return handle


def build_builtin_registry() -> dict[str, AgentProfile]:
    """Return the default clone profiles shipped with the foundation."""
    return {
        name: AgentProfile(name, role, set(capabilities), _bound_handler(name, role))
        for name, role, capabilities in BUILTIN_AGENT_SPECS
    }


def list_builtin_agents() -> tuple[AgentProfile, ...]:
    """Return the built-in profiles in registration order."""
    return tuple(build_builtin_registry().values())
