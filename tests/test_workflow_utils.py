from shared.workflow_utils import (
    can_execute
)

completed_agents = [
    "RequirementAgent",
    "ServiceAgent",
    "ArchitectureAgent",
    "ReviewAgent"
]

print(
    can_execute(
        "CostAgent",
        completed_agents
    )
)