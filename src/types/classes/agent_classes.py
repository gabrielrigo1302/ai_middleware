from pydantic import BaseModel
from src.types.enums import AgentIntenticEnum


class AgentIntenticInputClass(BaseModel):
    prompt: str
    intent: AgentIntenticEnum


class AgentInputClass(BaseModel):
    prompt: str
