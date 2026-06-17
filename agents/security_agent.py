from pathlib import Path

from shared.state import ArchitectureState
from shared.models import SecurityReviewResponse
from shared.foundry_client import client


class SecurityAgent:

    def execute(self, state: ArchitectureState):

        prompt = Path(
            "prompts/security_agent_prompt.txt"
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
            text_format=SecurityReviewResponse
        )

        result = response.output_parsed

        state.security_findings = (
            result.security_findings
        )

        return state