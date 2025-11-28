from typing import Any, Dict
from fastapi import APIRouter, status
from src.types.classes.text_classes import TextInputClass
from src.main.controllers.text_controller import (
    get_rag_text_query_controller,
    get_summarized_text_controller,
    post_rag_text_add_document_controller,
)


router = APIRouter(prefix="/text", tags=["text"])


@router.post("/summarize", status_code=status.HTTP_200_OK)
async def get_summarized_text(body: TextInputClass) -> str:
    return await get_summarized_text_controller(body.text)


@router.post("/enterprise-rag/add-document", status_code=status.HTTP_200_OK)
async def post_rag_text_add_document() -> str:
    return await post_rag_text_add_document_controller()


@router.post("/enterprise-rag/query", status_code=status.HTTP_200_OK)
async def get_rag_text_query(body: TextInputClass) -> Dict[str, Any]:
    return await get_rag_text_query_controller(body.text)
