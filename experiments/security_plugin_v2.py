from pathlib import Path

from semantic_kernel.functions import (
    kernel_function
)

from shared.models import (
    SecurityReviewResponse
)
from shared.foundry_client import client


class SecurityPlugin:

    @kernel_function(
        description="Analyze architecture security and provide findings"
    )
    def analyze_security(
        self,
        architecture_design: str,
        recommended_services: list[dict]
    ) -> SecurityReviewResponse:

        prompt = Path(
            "prompts/security_agent_prompt.txt"
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
            text_format=SecurityReviewResponse
        )

        result = response.output_parsed

        return result