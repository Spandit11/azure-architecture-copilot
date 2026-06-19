from shared import state


class ConsensusEngine:

    @staticmethod
    def evaluate(state):

        if state.workflow_status == "FAILED":

            state.consensus_score = "Low"
            state.requires_human_review = True

            return state

        if len(state.agent_errors) > 0:

            state.consensus_score = "Medium"
            state.requires_human_review = False

            return state

        state.consensus_score = "High"
        state.requires_human_review = False

        if len(state.conflicts) > 0:

            state.requires_human_review = True
        return state