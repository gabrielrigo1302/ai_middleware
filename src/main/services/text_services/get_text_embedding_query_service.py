from typing import List
from src.orchestrator import text_embedding_query_orchestration


async def get_text_embedding_query_service(content: str) -> List[float]:
    return await text_embedding_query_orchestration(content)
