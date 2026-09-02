"""Human-control policies applied before task dispatch."""

from dataclasses import dataclass, field

from .models import RiskClass, Task


@dataclass
class GovernancePolicy:
    approval_required: set[RiskClass] = field(
        default_factory=lambda: {
            RiskClass.EXTERNAL_WRITE,
            RiskClass.FINANCIAL,
            RiskClass.SENSITIVE_DATA,
            RiskClass.DESTRUCTIVE,
        }
    )

    def evaluate(self, task: Task) -> tuple[bool, str]:
        if task.risk in self.approval_required and not task.approved_by:
            return False, f"Human approval required for risk class: {task.risk.value}"
        return True, "Policy checks passed"
