from ..services import text_service


async def get_summarized_text_controller(text: str) -> str:
    return await text_service.get_summarized_text(text)
