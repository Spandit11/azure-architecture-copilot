from shared.state import ArchitectureState

from agents.consensus_agent import ConsensusAgent

state = ArchitectureState()

state.review_comments = [
    "Use Azure Key Vault",
    "Enable Monitoring"
]

state.security_findings = [
    "Use Azure Key Vault",
    "Enable Monitoring"
]

state.cost_recommendations = [
    "Review AKS costs"
]

state = ConsensusAgent().execute(state)

print("\nAgreements:\n")
print(state.agreements)

print("\nConflicts:\n")
print(state.conflicts)

print("\nFinal Confidence:\n")
print(state.final_confidence)