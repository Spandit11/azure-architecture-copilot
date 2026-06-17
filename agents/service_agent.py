from pathlib import Path

from shared.state import ArchitectureState
from shared.models import ServiceRecommendationResponse
from shared.foundry_client import client


class ServiceAgent:

    def execute(self, state: ArchitectureState):

        prompt = Path(
            "prompts/service_agent_prompt.txt"
        ).read_text()

        response = client.responses.parse(
            model="gpt-4o",
            input=f"""
            {prompt}

            Functional Requirements:
            {state.functional_requirements}

            Non Functional Requirements:
            {state.non_functional_requirements}
            """,
            text_format=ServiceRecommendationResponse
        )

        result = response.output_parsed

        state.recommended_services = [
        {
            "service_name": service.service_name,
            "reason": service.reason,
            "confidence": service.confidence
        }
        for service in result.recommended_services
        ]
        return state