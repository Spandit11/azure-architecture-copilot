from dataclasses import dataclass, field
from typing import List


@dataclass
class ArchitectureState:

    user_requirement: str = ""

    functional_requirements: List[str] = field(default_factory=list)

    non_functional_requirements: List[str] = field(default_factory=list)

    recommended_services: List[dict] = field(default_factory=list)

    architecture_design: str = ""

    security_findings: List[str] = field(default_factory=list)

    cost_recommendations: List[str] = field(default_factory=list)

    review_comments: List[str] = field(default_factory=list)

    diagram_definition: str = ""

    agent_logs: list = field(default_factory=list)
    agent_errors: list = field(default_factory=list)

    workflow_status: str = "NOT_STARTED"

    consensus_score: str = ""
    requires_human_review: bool = False

    agreements: list = field(default_factory=list)
    conflicts: list = field(default_factory=list)
    final_confidence: str = ""