"""Built-in clone profiles for common engineering and communications workflows."""

from collections.abc import Mapping
from dataclasses import dataclass
from types import MappingProxyType

from .models import AgentProfile, Handler


@dataclass(frozen=True)
class BuiltinCloneSpec:
    name: str
    role: str
    capabilities: frozenset[str]


BUILTIN_CLONE_SPECS = (
    BuiltinCloneSpec(
        name="ai-jarvis-assistant-engineer-manager",
        role="engineering_management",
        capabilities=frozenset(
            {"engineering_management", "technical_planning", "delivery_review"}
        ),
    ),
    BuiltinCloneSpec(
        name="ai-jarvis-assistant-communications-engineer-manager",
        role="communications_management",
        capabilities=frozenset(
            {"communications_management", "stakeholder_updates", "publish"}
        ),
    ),
)


def builtin_clone_profiles(handler: Handler) -> tuple[AgentProfile, ...]:
    """Return the built-in engineering and communications manager profiles."""

    return tuple(
        AgentProfile(
            name=spec.name,
            role=spec.role,
            capabilities=set(spec.capabilities),
            handler=handler,
        )
        for spec in BUILTIN_CLONE_SPECS
    )


def builtin_clone_registry(handler: Handler) -> Mapping[str, AgentProfile]:
    """Return a read-only mapping of built-in clone profiles keyed by agent name."""

    return MappingProxyType(
        {profile.name: profile for profile in builtin_clone_profiles(handler)}
    )
