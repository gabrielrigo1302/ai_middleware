from typing import List
from ..providers import mistral_provider

async def mistral_text_to_text_adapter(text: str) -> str:
    return await mistral_provider.mistral_text_to_text_provider(text)

async def mistral_text_embedding_adapter(content: List[str]) -> List[float]:
    return await mistral_provider.mistral_text_embedding_provider(content)