from typing import List
from src.orchestrator.adapters.huggy_face_adapter import (
    huggy_face_text_embedding_documents_adapter,
    huggy_face_text_embedding_query_adapter,
)
from src.orchestrator.adapters.mistral_adapter import mistral_text_to_text_adapter


async def text_to_text_orchestration(system_prompt: str, prompt: str) -> str:
    return await mistral_text_to_text_adapter(system_prompt, prompt)


async def text_embedding_documents_orchestration(
    content: List[str],
) -> List[List[float]]:
    return await huggy_face_text_embedding_documents_adapter(content)


async def text_embedding_query_orchestration(content: str) -> List[float]:
    return await huggy_face_text_embedding_query_adapter(content)
