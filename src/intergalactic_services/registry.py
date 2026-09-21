"""Built-in clone profiles for common engineering and communications workflows."""

from .models import AgentProfile, Handler


def builtin_clone_profiles(handler: Handler) -> tuple[AgentProfile, ...]:
    """Return the built-in AI Jarvis Assistant clone profiles."""

    return (
        AgentProfile(
            name="ai-jarvis-assistant-engineer-manager",
            role="engineering_management",
            capabilities={"engineering_management", "technical_planning", "delivery_review"},
            handler=handler,
        ),
        AgentProfile(
            name="communications-engineer-manager",
            role="communications_management",
            capabilities={"communications_management", "stakeholder_updates", "publish"},
            handler=handler,
        ),
    )


def builtin_clone_registry(handler: Handler) -> dict[str, AgentProfile]:
    """Return built-in clone profiles keyed by agent name."""

    return {profile.name: profile for profile in builtin_clone_profiles(handler)}
