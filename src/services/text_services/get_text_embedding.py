from typing import List
from src.orchestrator import orchestrator

async def get_text_embedding(content: List[str]) -> List[float]:
    return await orchestrator.text_embedding_orchestration(content)
