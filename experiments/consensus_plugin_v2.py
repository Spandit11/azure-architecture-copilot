from pathlib import Path

from semantic_kernel.functions import (
    kernel_function
)

from shared.models import (
    ConsensusResponse
)
from shared.foundry_client import client


class ConsensusPlugin:

    @kernel_function(
        description="Evaluate consensus across review, security and cost findings"
    )
    def evaluate_consensus(
        self,
        review_comments: list[str],
        security_findings: list[str],
        cost_recommendations: list[str]
    ) -> ConsensusResponse:

        prompt = Path(
            "prompts/consensus_agent_prompt.txt"
        ).read_text()

        response = client.responses.parse(
            model="gpt-4o",
            input=f"""
            {prompt}

            Review Comments:
            {review_comments}

            Security Findings:
            {security_findings}

            Cost Recommendations:
            {cost_recommendations}
            """,
            text_format=ConsensusResponse
        )

        result = response.output_parsed

        return result