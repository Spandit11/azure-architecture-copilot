from shared.state import ArchitectureState

from agents.requirement_agent_v2 import RequirementAgentV2
from agents.service_agent import ServiceAgent
from agents.architecture_agent import ArchitectureAgent
from agents.review_agent import ReviewAgent
from agents.security_agent import SecurityAgent
from agents.cost_agent import CostAgent
state = ArchitectureState()

state.user_requirement = """
Build a scalable healthcare claims processing
platform with document upload and AI extraction.
"""

state = RequirementAgentV2().execute(state)

state = ServiceAgent().execute(state)

state = ArchitectureAgent().execute(state)

state = ReviewAgent().execute(state)

state = SecurityAgent().execute(state)

state = CostAgent().execute(state)

print("\nSecurity Findings:\n")

for finding in state.security_findings:
    print("-", finding)

print("\nCost Recommendations:\n")

for recommendation in state.cost_recommendations:
    print("-", recommendation)