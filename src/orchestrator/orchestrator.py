from typing import List
from .adapters import mistral_adapter


async def text_to_text_orchestration(system_prompt: str, prompt: str) -> str:
    return await mistral_adapter.mistral_text_to_text_adapter(system_prompt, prompt)


async def text_embedding_orchestration(content: List[str]) -> List[float]:
    return await mistral_adapter.mistral_text_embedding_adapter(content)
