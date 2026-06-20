from shared.agent_dependency_graph import (
    AGENT_DEPENDENCIES
)


def can_execute(
    agent_name: str,
    completed_agents: list[str]
):

    dependencies = AGENT_DEPENDENCIES.get(
        agent_name,
        []
    )

    return all(
        dependency in completed_agents
        for dependency in dependencies
    )