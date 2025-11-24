from typing import List
from src.orchestrator import text_embedding_orchestration


async def get_text_embedding_service(content: List[str]) -> List[float]:
    return await text_embedding_orchestration(content)
