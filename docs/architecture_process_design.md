# Architecture Process Design

## Objective

Replace the custom ArchitectureOrchestrator with a Semantic Kernel Process-based workflow.

---

## Current Flow

RequirementAgent
↓
ServiceAgent
↓
ArchitectureAgent
↓
ReviewAgent
↓
SecurityAgent
↓
CostAgent
↓
ConsensusAgent

---

## Future Process

ArchitectureProcess

RequirementStep
↓
RequirementPlugin.extract_requirements()

ServiceStep
↓
ServicePlugin.recommend_services()

ArchitectureStep
↓
ArchitecturePlugin.generate_architecture()

ReviewStep
↓
ReviewPlugin.review_architecture()

SecurityStep
↓
SecurityPlugin.analyze_security()

CostStep
↓
CostPlugin.analyze_cost()

ConsensusStep
↓
ConsensusPlugin.evaluate_consensus()

---

## Process Context

The Process Context will replace ArchitectureState.

Context Properties:

* user_requirement
* functional_requirements
* non_functional_requirements
* recommended_services
* architecture_design
* review_comments
* security_findings
* cost_recommendations
* agreements
* conflicts
* final_confidence

---

## Future Human Review

ConsensusStep
↓
Conflict Detection
↓
Human Approval
↓
Final Recommendation

---

## Expected Benefits

* Native Semantic Kernel workflow orchestration
* Better Azure ecosystem alignment
* Easier integration with Azure AI Foundry
* Step-level observability
* Process-level state management
* Agent-to-Process migration path
