from intergalactic_services import (
    AgentProfile,
    HermesOrchestrator,
    RiskClass,
    Task,
    builtin_clone_profiles,
    builtin_clone_registry,
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


def test_builtin_clone_registry_exposes_manager_profiles() -> None:
    registry = builtin_clone_registry(echo)
    assert set(registry) == {
        "ai-jarvis-assistant-engineer-manager",
        "communications-engineer-manager",
    }
    assert registry["ai-jarvis-assistant-engineer-manager"] == AgentProfile(
        "ai-jarvis-assistant-engineer-manager",
        "engineering_management",
        {"engineering_management", "technical_planning", "delivery_review"},
        echo,
    )
    assert registry["communications-engineer-manager"] == AgentProfile(
        "communications-engineer-manager",
        "communications_management",
        {"communications_management", "stakeholder_updates", "publish"},
        echo,
    )


def test_builtin_clone_profiles_returns_expected_sequence() -> None:
    assert builtin_clone_profiles(echo) == (
        AgentProfile(
            "ai-jarvis-assistant-engineer-manager",
            "engineering_management",
            {"engineering_management", "technical_planning", "delivery_review"},
            echo,
        ),
        AgentProfile(
            "communications-engineer-manager",
            "communications_management",
            {"communications_management", "stakeholder_updates", "publish"},
            echo,
        ),
    )


def test_builtin_engineering_manager_routes_engineering_work() -> None:
    engineering_manager, _ = builtin_clone_profiles(echo)
    for task_id, kind in (
        ("task-5", "engineering_management"),
        ("task-6", "technical_planning"),
        ("task-7", "delivery_review"),
    ):
        result = HermesOrchestrator([engineering_manager]).dispatch(
            Task(task_id, kind, {"initiative": "launch"})
        )
        assert result.status == "completed"
        assert result.agent == "ai-jarvis-assistant-engineer-manager"


def test_builtin_communications_manager_routes_publish_work() -> None:
    _, communications_manager = builtin_clone_profiles(echo)
    for task_id, kind in (
        ("task-8", "communications_management"),
        ("task-9", "stakeholder_updates"),
        ("task-10", "publish"),
    ):
        result = HermesOrchestrator([communications_manager]).dispatch(
            Task(task_id, kind, {"channel": "newsletter"})
        )
        assert result.status == "completed"
        assert result.agent == "communications-engineer-manager"
