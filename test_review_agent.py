from shared.state import ArchitectureState

from agents.requirement_agent_v2 import RequirementAgentV2
from agents.service_agent import ServiceAgent
from agents.architecture_agent import ArchitectureAgent
from agents.review_agent import ReviewAgent

state = ArchitectureState()

state.user_requirement = """
Build a scalable healthcare claims processing
platform with document upload and AI extraction.
"""

state = RequirementAgentV2().execute(state)

state = ServiceAgent().execute(state)

state = ArchitectureAgent().execute(state)

state = ReviewAgent().execute(state)

print("\nReview Comments:\n")

for comment in state.review_comments:
    print("-", comment)