from pydantic import BaseModel

class SummarizeRequest(BaseModel):
    conversation_id: str
    max_tokens: int = 1024

class SummarizeResponse(BaseModel):
    summary: str