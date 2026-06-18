from agents.requirement_agent_v2 import RequirementAgentV2
from shared.state import ArchitectureState

state = ArchitectureState()

state.user_requirement = """
Build a scalable healthcare claims processing
platform with document upload and AI extraction.
"""

agent = RequirementAgentV2()

updated_state = agent.execute(state)

print(updated_state)