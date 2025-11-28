from typing import Any, Dict
from src.main.services.text_services import (
    get_summarized_text_service,
    post_rag_text_add_document_service,
    get_rag_text_query_service,
)


async def get_summarized_text_controller(text: str) -> str:
    return await get_summarized_text_service(text)


async def post_rag_text_add_document_controller() -> str:
    return await post_rag_text_add_document_service()


async def get_rag_text_query_controller(question: str) -> Dict[str, Any]:
    return await get_rag_text_query_service(question)
