from pydantic import BaseModel


class AgentResult(BaseModel):
    success: bool
    error_message: str | None = None