from fastapi import APIRouter, status
from .classes.text_routes_classes import TextInput
from ..controllers import text_controller

router = APIRouter(prefix="/text", tags=["text"])

@router.post("/summarize", status_code=status.HTTP_200_OK)
async def get_summarized_text(body: TextInput) -> str:
    return await text_controller.get_summarized_text_controller(body.text)
