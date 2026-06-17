from pathlib import Path

from shared.state import ArchitectureState
from shared.models import ArchitectureReviewResponse
from shared.foundry_client import client


class ReviewAgent:

    def execute(self, state: ArchitectureState):

        prompt = Path(
            "prompts/review_agent_prompt.txt"
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
            text_format=ArchitectureReviewResponse
        )

        result = response.output_parsed

        state.review_comments = result.review_comments

        return state