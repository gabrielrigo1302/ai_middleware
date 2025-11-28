from typing import List
from src.orchestrator import text_embedding_documents_orchestration


async def get_text_embedding_documents_service(content: List[str]) -> List[List[float]]:
    return await text_embedding_documents_orchestration(content)
