from shared import state
from shared.state import ArchitectureState

from agents.requirement_agent_v2 import RequirementAgentV2
from agents.service_agent import ServiceAgent
from agents.architecture_agent import ArchitectureAgent
from agents.review_agent import ReviewAgent
from agents.security_agent import SecurityAgent
from agents.cost_agent import CostAgent


class ArchitectureOrchestrator:

    def execute(self, user_requirement: str):

        state = ArchitectureState()

        state.user_requirement = user_requirement

        state.workflow_status = "RUNNING"  

        print("Running Requirement Agent...")
        state = RequirementAgentV2().execute(state)
        state.agent_logs.append(
            {
                "agent_name": "RequirementAgentV2",
                "status": "SUCCESS",
                "message": "Completed successfully"
            }
        )

        print("Running Service Agent...")
        state = ServiceAgent().execute(state)
        state.agent_logs.append(
            {
                "agent_name": "ServiceAgent",
                "status": "SUCCESS",
                "message": "Completed successfully"
            }
        )

        print("Running Architecture Agent...")
        state = ArchitectureAgent().execute(state)   
        state.agent_logs.append(
            {
                "agent_name": "ArchitectureAgent",
                "status": "SUCCESS",
                "message": "Completed successfully"
            }
        ) 

        try:
            print("Running Review Agent...")
            state = ReviewAgent().execute(state)
            state.agent_logs.append(
                {
                    "agent_name": "ReviewAgent",
                    "status": "SUCCESS",
                    "message": "Completed successfully"
                }
            )

        except Exception as ex:
            state.agent_errors.append(
                f"ReviewAgent: {str(ex)}"
            )
            state.agent_logs.append(
                {
                    "agent_name": "ReviewAgent",
                    "status": "FAILED",
                    "message": str(ex)
                }
            )
            print(f"Review Agent Failed: {str(ex)}")
        try:
            print("Running Security Agent...")
            state = SecurityAgent().execute(state)
            state.agent_logs.append(
                {
                    "agent_name": "SecurityAgent",
                    "status": "SUCCESS",
                    "message": "Completed successfully"
                }
            )

        except Exception as ex:
            state.agent_errors.append(
                f"SecurityAgent: {str(ex)}"
            )
            state.agent_logs.append(
                {
                    "agent_name": "SecurityAgent",
                    "status": "FAILED",
                    "message": str(ex)
                }
            )
            print(f"Security Agent Failed: {str(ex)}")

        try:
            
            print("Running Cost Agent...")
            state = CostAgent().execute(state)
            state.agent_logs.append(
                {
                    "agent_name": "CostAgent",
                    "status": "SUCCESS",
                    "message": "Completed successfully"
                }
            )

        except Exception as ex:
            state.agent_errors.append(
                f"CostAgent: {str(ex)}"
            )
            state.agent_logs.append(
                {
                    "agent_name": "CostAgent",
                    "status": "FAILED",
                    "message": str(ex)
                }
            )
            print(f"Cost Agent Failed: {str(ex)}")
            
        if len(state.agent_errors) == 0:
            state.workflow_status = "SUCCESS"
        else:
            state.workflow_status = "PARTIAL_SUCCESS"
        return state