from src.orchestrator import text_to_text_orchestration


async def get_summarized_text_service(prompt: str) -> str:
    system_prompt = "Você é um assistente que resume textos de forma clara e concisa."

    return await text_to_text_orchestration(system_prompt, prompt)
