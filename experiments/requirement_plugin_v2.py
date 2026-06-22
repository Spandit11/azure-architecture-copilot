from pathlib import Path

from semantic_kernel.functions import (
    kernel_function
)

from shared.foundry_client import client
from shared.models import RequirementResponse


class RequirementPlugin:

    @kernel_function(
        description="Extract functional and non-functional requirements"
    )
    def extract_requirements(
        self,
        user_requirement: str
    ) -> RequirementResponse:

        prompt = Path(
            "prompts/requirement_agent_prompt.txt"
        ).read_text()

        response = client.responses.parse(
            model="gpt-4o",
            input=f"""
            {prompt}

            User Requirement:
            {user_requirement}
            """,
            text_format=RequirementResponse
        )

        result = response.output_parsed

        return result