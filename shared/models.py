from pydantic import BaseModel
from typing import List


class RequirementResponse(BaseModel):
    functional_requirements: List[str]
    non_functional_requirements: List[str]

class AzureServiceRecommendation(BaseModel):
    service_name: str
    reason: str
    confidence: str


class ServiceRecommendationResponse(BaseModel):
    recommended_services: List[AzureServiceRecommendation]

class ArchitectureResponse(BaseModel):
    architecture_design: str

class ArchitectureReviewResponse(BaseModel):
    review_comments: List[str]

class SecurityReviewResponse(BaseModel):
    security_findings: List[str]