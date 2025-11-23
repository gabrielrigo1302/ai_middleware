from typing import Any, Dict, List
from src.main.services import text_services


async def get_summarized_text_controller(text: str) -> str:
    return await text_services.get_summarized_text_service(text)


async def get_text_embedding_controller(content: List[str]) -> List[float]:
    return await text_services.get_text_embedding_service(content)


async def post_rag_text_add_document() -> str:
    return await text_services.post_rag_text_add_document_service()


async def get_rag_text_query(question: str) -> Dict[str, Any]:
    return await text_services.get_rag_text_query_service(question)
