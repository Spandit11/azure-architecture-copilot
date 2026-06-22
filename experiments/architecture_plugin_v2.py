from pathlib import Path

from semantic_kernel.functions import (
    kernel_function
)

from shared.models import ArchitectureResponse
from shared.foundry_client import client


class ArchitecturePlugin:

    @kernel_function(
        description="Generate Azure architecture design"
    )
    def generate_architecture(
        self,
        functional_requirements: list[str],
        non_functional_requirements: list[str],
        recommended_services: list[dict]
    ) -> ArchitectureResponse:

        prompt = Path(
            "prompts/architecture_agent_prompt.txt"
        ).read_text()

        response = client.responses.parse(
            model="gpt-4o",
            input=f"""
            {prompt}

            Functional Requirements:
            {functional_requirements}

            Non Functional Requirements:
            {non_functional_requirements}

            Recommended Services:
            {recommended_services}
            """,
            text_format=ArchitectureResponse
        )

        result = response.output_parsed

        return result