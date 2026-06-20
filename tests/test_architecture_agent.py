from agents.requirement_agent_v2 import RequirementAgentV2
from agents.service_agent import ServiceAgent
from agents.architecture_agent import ArchitectureAgent

from shared.state import ArchitectureState
from shared.workflow_visualizer import build_workflow_definition

state = ArchitectureState()

state.user_requirement = """
Build a scalable healthcare claims processing
platform with document upload and AI extraction.
"""

state = RequirementAgentV2().execute(state)

state = ServiceAgent().execute(state)

state = ArchitectureAgent().execute(state)

print(state.architecture_design)
 
print("\nWorkflow Definition:\n")
print(state.workflow_definition)
state.workflow_definition = build_workflow_definition()