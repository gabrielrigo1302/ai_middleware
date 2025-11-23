from typing import List
from src.orchestrator.providers import mistral_provider


async def mistral_text_to_text_adapter(system_prompt: str, prompt: str) -> str:
    return await mistral_provider.mistral_text_to_text_provider(system_prompt, prompt)


async def mistral_text_embedding_adapter(content: List[str]) -> List[float]:
    return await mistral_provider.mistral_text_embedding_provider(content)
