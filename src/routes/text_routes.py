from fastapi import APIRouter
from ..controllers import text_controller

router = APIRouter(prefix="/text", tags=["text"])

@router.get("/summarize")
def get_summarized_text():
    return text_controller.get_summarized_text_controller('teste')