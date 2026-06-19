from pathlib import Path

from shared.state import ArchitectureState
from shared.models import ConsensusResponse
from shared.foundry_client import client


class ConsensusAgent:

    def execute(self, state: ArchitectureState):

        prompt = Path(
            "prompts/consensus_agent_prompt.txt"
        ).read_text()

        response = client.responses.parse(
            model="gpt-4o",
            input=f"""
            {prompt}

            Review Comments:
            {state.review_comments}

            Security Findings:
            {state.security_findings}

            Cost Recommendations:
            {state.cost_recommendations}
            """,
            text_format=ConsensusResponse
        )

        result = response.output_parsed

        state.agreements = result.agreements
        state.conflicts = result.conflicts
        state.final_confidence = result.final_confidence

        return state