from pathlib import Path

from shared.state import ArchitectureState
from shared.foundry_client import client
from shared.models import RequirementResponse


class RequirementAgentV2:

    def execute(self, state: ArchitectureState):

        prompt = Path(
            "prompts/requirement_agent_prompt.txt"
        ).read_text()

        response = client.responses.parse(
            model="gpt-4o",
            input=f"""
            {prompt}

            User Requirement:
            {state.user_requirement}
            """,
            text_format=RequirementResponse
        )

        result = response.output_parsed

        state.functional_requirements = (
            result.functional_requirements
        )

        state.non_functional_requirements = (
            result.non_functional_requirements
        )

        return state