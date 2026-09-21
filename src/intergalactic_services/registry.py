"""Built-in clone profiles for common Intergalactic Services roles."""

from .models import AgentProfile, Task

JARVIS_NAME = "ai-jarvis-assistant"
JARVIS_ROLE = "Engineer Manager and Communications Engineer and Manager"


def _jarvis_handler(task: Task) -> dict[str, object]:
    return {
        "assistant": "AI Jarvis assistant",
        "role": JARVIS_ROLE,
        "task": task.kind,
        "payload": task.payload,
    }


def jarvis_assistant() -> AgentProfile:
    return AgentProfile(
        JARVIS_NAME,
        JARVIS_ROLE,
        {
            "engineering_management",
            "communications_engineering",
            "communications_management",
        },
        _jarvis_handler,
    )


def default_agents() -> tuple[AgentProfile, ...]:
    return (jarvis_assistant(),)
