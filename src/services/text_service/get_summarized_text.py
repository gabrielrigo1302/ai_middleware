from src.orchestrator import orchestrator

async def get_summarized_text(text: str) -> str:
    return await orchestrator.text_to_text_orchestration(text)
