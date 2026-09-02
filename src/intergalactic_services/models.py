"""Core domain models for clones, tasks, and governed results."""

from collections.abc import Callable
from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any


class RiskClass(StrEnum):
    READ_ONLY = "read_only"
    EXTERNAL_WRITE = "external_write"
    FINANCIAL = "financial"
    SENSITIVE_DATA = "sensitive_data"
    DESTRUCTIVE = "destructive"


@dataclass(frozen=True)
class Task:
    task_id: str
    kind: str
    payload: dict[str, Any] = field(default_factory=dict)
    risk: RiskClass = RiskClass.READ_ONLY
    approved_by: str | None = None


@dataclass(frozen=True)
class TaskResult:
    task_id: str
    status: str
    agent: str | None
    reason: str
    output: Any = None


Handler = Callable[[Task], Any]


@dataclass
class AgentProfile:
    name: str
    role: str
    capabilities: set[str]
    handler: Handler
    enabled: bool = True
