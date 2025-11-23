from src.orchestrator import orchestrator


async def get_summarized_text_service(prompt: str) -> str:
    system_prompt = "Você é um assistente que resume textos de forma clara e concisa."

    return await orchestrator.text_to_text_orchestration(system_prompt, prompt)
