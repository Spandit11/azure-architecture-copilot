from pathlib import Path

from semantic_kernel.functions import (
    kernel_function
)

from shared.models import (
    CostReviewResponse
)
from shared.foundry_client import client


class CostPlugin:

    @kernel_function(
        description="Analyze architecture costs and provide recommendations"
    )
    def analyze_cost(
        self,
        architecture_design: str,
        recommended_services: list[dict]
    ) -> CostReviewResponse:

        prompt = Path(
            "prompts/cost_agent_prompt.txt"
        ).read_text()

        response = client.responses.parse(
            model="gpt-4o",
            input=f"""
            {prompt}

            Architecture Design:
            {architecture_design}

            Recommended Services:
            {recommended_services}
            """,
            text_format=CostReviewResponse
        )

        result = response.output_parsed

        return result