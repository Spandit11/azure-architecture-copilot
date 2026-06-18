from pydantic import BaseModel


class AgentLog(BaseModel):
    agent_name: str
    status: str
    message: str