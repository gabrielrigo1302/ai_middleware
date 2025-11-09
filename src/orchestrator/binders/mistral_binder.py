from ..providers.mistral_provider import mistral_text_to_text_provider


async def mistral_text_to_text_binder(text: str) -> str:
    return await mistral_text_to_text_provider(text)
