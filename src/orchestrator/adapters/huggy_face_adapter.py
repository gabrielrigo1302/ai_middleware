from typing import List
from src.orchestrator.providers.huggy_face_provider import (
    huggy_face_text_embedding_documents_provider,
    huggy_face_text_embedding_query_provider,
)


async def huggy_face_text_embedding_documents_adapter(
    content: List[str],
) -> List[List[float]]:
    return await huggy_face_text_embedding_documents_provider(content)


async def huggy_face_text_embedding_query_adapter(content: str) -> List[float]:
    return await huggy_face_text_embedding_query_provider(content)
