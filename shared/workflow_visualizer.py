def build_workflow_definition():

    return """
RequirementAgent
        ↓
ServiceAgent
        ↓
ArchitectureAgent
       ↙      ↘
ReviewAgent  SecurityAgent
       ↘      ↙
        CostAgent
            ↓
      ConsensusAgent
"""