"""Built-in clone profiles for common Intergalactic Services roles."""

from .models import AgentProfile, Task


def _jarvis_handler(task: Task) -> dict[str, object]:
    return {
        "assistant": "AI Jarvis assistant",
        "role": "Engineer Manager and Communications Engineer and Manager",
        "task": task.kind,
        "payload": task.payload,
    }


def jarvis_assistant() -> AgentProfile:
    return AgentProfile(
        "ai-jarvis-assistant",
        "Engineer Manager and Communications Engineer and Manager",
        {
            "engineering_management",
            "communications_engineering",
            "communications_management",
        },
        _jarvis_handler,
    )


def default_agents() -> tuple[AgentProfile, ...]:
    return (jarvis_assistant(),)
