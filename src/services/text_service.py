from ..orchestrator.orchestrator import text_to_text_orchestration


async def get_summarized_text(text: str) -> str:
    return await text_to_text_orchestration(text)
