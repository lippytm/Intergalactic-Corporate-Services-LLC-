from intergalactic_services import (
    AgentProfile,
    HermesOrchestrator,
    RiskClass,
    Task,
    build_builtin_registry,
    list_builtin_agents,
)


def echo(task: Task) -> dict:
    return {"received": task.payload}


def test_routes_read_only_task() -> None:
    agent = AgentProfile("research-clone", "research", {"research"}, echo)
    result = HermesOrchestrator([agent]).dispatch(
        Task("task-1", "research", {"topic": "market"})
    )
    assert result.status == "completed"
    assert result.agent == "research-clone"
    assert result.output == {"received": {"topic": "market"}}


def test_blocks_external_write_without_human_approval() -> None:
    agent = AgentProfile("publisher-clone", "publishing", {"publish"}, echo)
    result = HermesOrchestrator([agent]).dispatch(
        Task("task-2", "publish", risk=RiskClass.EXTERNAL_WRITE)
    )
    assert result.status == "blocked"
    assert result.agent is None


def test_allows_approved_external_write() -> None:
    agent = AgentProfile("publisher-clone", "publishing", {"publish"}, echo)
    result = HermesOrchestrator([agent]).dispatch(
        Task(
            "task-3",
            "publish",
            risk=RiskClass.EXTERNAL_WRITE,
            approved_by="owner",
        )
    )
    assert result.status == "completed"


def test_reports_unroutable_capability() -> None:
    result = HermesOrchestrator().dispatch(Task("task-4", "unknown"))
    assert result.status == "unroutable"


def test_rejects_duplicate_agent_names() -> None:
    agent = AgentProfile("clone", "general", {"research"}, echo)
    orchestrator = HermesOrchestrator([agent])
    try:
        orchestrator.register(agent)
    except ValueError as exc:
        assert "already registered" in str(exc)
    else:
        raise AssertionError("duplicate registration should fail")


def test_builtin_registry_includes_requested_profiles() -> None:
    registry = build_builtin_registry()
    assert set(registry) == {
        "ai-jarvis-assistant",
        "communications-manager",
        "engineer-manager",
    }
    assert registry["ai-jarvis-assistant"].capabilities >= {"assistant", "research"}
    assert registry["engineer-manager"].capabilities >= {"engineering", "review"}
    assert registry["communications-manager"].capabilities >= {
        "communications",
        "publishing",
    }


def test_builtin_agents_route_supported_work() -> None:
    result = HermesOrchestrator(list_builtin_agents()).dispatch(
        Task("task-5", "communications", {"channel": "email"})
    )
    assert result.status == "completed"
    assert result.agent == "communications-manager"
    assert result.output == {
        "agent": "communications-manager",
        "role": "communications_management",
        "task_kind": "communications",
        "payload": {"channel": "email"},
    }
