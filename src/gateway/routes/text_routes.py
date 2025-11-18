from typing import Any, Dict, List
from fastapi import APIRouter, status
from src.types.classes.text_classes import TextInput
from src.main.controllers import text_controller

router = APIRouter(prefix="/text", tags=["text"])


@router.post("/summarize", status_code=status.HTTP_200_OK)
async def get_summarized_text(body: TextInput) -> str:
    return await text_controller.get_summarized_text_controller(body.text)


@router.post("/embedding", status_code=status.HTTP_200_OK)
async def get_text_embedding(body: TextInput) -> List[float]:
    return await text_controller.get_text_embedding_controller([body.text])


@router.post("/enterprise-rag/add-document", status_code=status.HTTP_200_OK)
async def post_rag_text_add_document() -> str:
    return await text_controller.post_rag_text_add_document()


@router.post("/enterprise-rag/query", status_code=status.HTTP_200_OK)
async def get_rag_text_query(body: TextInput) -> Dict[str, Any]:
    return await text_controller.get_rag_text_query(body.text)
