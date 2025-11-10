from typing import List
from .adapters import mistral_adapter

async def text_to_text_orchestration(text: str) -> str:
    return await mistral_adapter.mistral_text_to_text_adapter(text)

async def text_embedding_orchestration(content: List[str]) -> List[float]:
    return await mistral_adapter.mistral_text_embedding_adapter(content)