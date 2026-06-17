from agents.requirement_agent import RequirementAgent
from shared.state import ArchitectureState

state = ArchitectureState()

state.user_requirement = """
Build a scalable healthcare claims processing
platform with document upload and AI extraction.
"""

agent = RequirementAgent()

updated_state = agent.execute(state)

print("\nFunctional Requirements:\n")
print(updated_state.functional_requirements)

print("\nNon Functional Requirements:\n")
print(updated_state.non_functional_requirements)