from pathlib import Path

from shared.state import ArchitectureState
from shared.models import CostReviewResponse
from shared.foundry_client import client


class CostAgent:

    def execute(self, state: ArchitectureState):

        prompt = Path(
            "prompts/cost_agent_prompt.txt"
        ).read_text()

        response = client.responses.parse(
            model="gpt-4o",
            input=f"""
            {prompt}

            Architecture Design:
            {state.architecture_design}

            Recommended Services:
            {state.recommended_services}
            """,
            text_format=CostReviewResponse
        )

        result = response.output_parsed

        state.cost_recommendations = (
            result.cost_recommendations
        )

        return state