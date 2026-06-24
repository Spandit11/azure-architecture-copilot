from pathlib import Path

from semantic_kernel.functions import (
    kernel_function
)

from shared.models import (
    ArchitectureReviewResponse
)
from shared.foundry_client import client


class ReviewPlugin:

    @kernel_function(
        description="Review architecture design and provide recommendations"
    )
    def review_architecture(
        self,
        architecture_design: str,
        recommended_services: list[dict]
    ) -> ArchitectureReviewResponse:

        prompt = Path(
            "prompts/review_agent_prompt.txt"
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
            text_format=ArchitectureReviewResponse
        )

        result = response.output_parsed

        return result