from pathlib import Path

from shared.state import ArchitectureState
from shared.models import ArchitectureResponse
from shared.foundry_client import client


class ArchitectureAgent:

    def execute(self, state: ArchitectureState):

        prompt = Path(
            "prompts/architecture_agent_prompt.txt"
        ).read_text()

        response = client.responses.parse(
            model="gpt-4o",
            input=f"""
            {prompt}

            Functional Requirements:
            {state.functional_requirements}

            Non Functional Requirements:
            {state.non_functional_requirements}

            Recommended Services:
            {state.recommended_services}
            """,
            text_format=ArchitectureResponse
        )

        result = response.output_parsed

        state.architecture_design = (
            result.architecture_design
        )

        return state