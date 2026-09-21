from intergalactic_services import (
    AgentProfile,
    HermesOrchestrator,
    RiskClass,
    Task,
    default_agents,
    jarvis_assistant,
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


def test_jarvis_assistant_declares_expected_roles() -> None:
    agent = jarvis_assistant()
    assert agent.name == "ai-jarvis-assistant"
    assert agent.role == "Engineer Manager and Communications Engineer and Manager"
    assert agent.capabilities == {
        "engineering_management",
        "communications_engineering",
        "communications_management",
    }


def test_default_agents_include_jarvis() -> None:
    agents = default_agents()
    assert len(agents) == 1
    assert agents[0].name == "ai-jarvis-assistant"


def test_routes_engineering_management_task_to_jarvis() -> None:
    result = HermesOrchestrator(default_agents()).dispatch(
        Task("task-5", "engineering_management", {"team": "platform"})
    )
    assert result.status == "completed"
    assert result.agent == "ai-jarvis-assistant"
    assert result.output == {
        "assistant": "AI Jarvis assistant",
        "role": "Engineer Manager and Communications Engineer and Manager",
        "task": "engineering_management",
        "payload": {"team": "platform"},
    }
