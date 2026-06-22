from pathlib import Path

from semantic_kernel.functions import (
    kernel_function
)

from shared.models import (
    ServiceRecommendationResponse
)
from shared.foundry_client import client


class ServicePlugin:

    @kernel_function(
        description="Recommend Azure services based on requirements"
    )
    def recommend_services(
        self,
        functional_requirements: list[str],
        non_functional_requirements: list[str]
    ) -> ServiceRecommendationResponse:

        prompt = Path(
            "prompts/service_agent_prompt.txt"
        ).read_text()

        response = client.responses.parse(
            model="gpt-4o",
            input=f"""
            {prompt}

            Functional Requirements:
            {functional_requirements}

            Non Functional Requirements:
            {non_functional_requirements}
            """,
            text_format=ServiceRecommendationResponse
        )

        result = response.output_parsed

        return result