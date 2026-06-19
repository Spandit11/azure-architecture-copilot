from orchestrators.architecture_orchestrator import (
    ArchitectureOrchestrator
)

orchestrator = ArchitectureOrchestrator()

state = orchestrator.execute(
    """
    Build a scalable healthcare claims
    processing platform with document upload
    and AI extraction.
    """
)

print("\n=================================")
print("ARCHITECTURE COMPLETE")
print("=================================")

print("\nServices:\n")
print(state.recommended_services)

print("\nReview Comments:\n")
print(state.review_comments)

print("\nSecurity Findings:\n")
print(state.security_findings)

print("\nCost Recommendations:\n")
print(state.cost_recommendations)
print("\nWorkflow Status:")
print(state.workflow_status)

print("\nAgent Logs:")
for log in state.agent_logs:
    print(log)

print("\nAgent Errors:")
if len(state.agent_errors) == 0:
    print("None")
else:
    for error in state.agent_errors:
        print(error)
print("\nConsensus Score:")
print(state.consensus_score)

print("\nRequires Human Review:")
print(state.requires_human_review)
print("\nAgreements:\n")
print(state.agreements)

print("\nConflicts:\n")
print(state.conflicts)

print("\nFinal Confidence:\n")
print(state.final_confidence)