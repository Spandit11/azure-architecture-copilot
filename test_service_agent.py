from agents.requirement_agent_v2 import RequirementAgentV2
from agents.service_agent import ServiceAgent
from shared.state import ArchitectureState

state = ArchitectureState()

state.user_requirement = """
Build a scalable healthcare claims processing
platform with document upload and AI extraction.
"""

requirement_agent = RequirementAgentV2()
state = requirement_agent.execute(state)

service_agent = ServiceAgent()
state = service_agent.execute(state)

print("\nRecommended Azure Services:\n")

for service in state.recommended_services:
    print(service)