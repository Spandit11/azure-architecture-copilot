AGENT_DEPENDENCIES = {
    "RequirementAgent": [],
    "ServiceAgent": ["RequirementAgent"],
    "ArchitectureAgent": ["ServiceAgent"],
    "ReviewAgent": ["ArchitectureAgent"],
    "SecurityAgent": ["ArchitectureAgent"],
    "CostAgent": ["ReviewAgent", "SecurityAgent"],
    "ConsensusAgent": ["CostAgent"]
}