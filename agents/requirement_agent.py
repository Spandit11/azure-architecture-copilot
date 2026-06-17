import json
from pathlib import Path
from unittest import result

from shared.state import ArchitectureState
from shared.foundry_client import client


class RequirementAgent:

    def execute(self, state: ArchitectureState):

        prompt = Path(
            "prompts/requirement_agent_prompt.txt"
        ).read_text()

        response = client.responses.create(
            model="gpt-4o",
            input=f"""
            {prompt}

            User Requirement:
            {state.user_requirement}
            """
        )

        result = response.output_text

        result = result.replace("```json", "")
        result = result.replace("```", "")
        result = result.strip()

        parsed = json.loads(result)

        state.functional_requirements = parsed.get(
            "functional_requirements",
            []
        )

        state.non_functional_requirements = parsed.get(
            "non_functional_requirements",
            []
        )

        return state