from pydantic import BaseModel
from src.types.enums.agent_enums import AgentIntenticEnum


class AgentIntenticInput(BaseModel):
    prompt: str
    intent: AgentIntenticEnum


class AgentInput(BaseModel):
    prompt: str
