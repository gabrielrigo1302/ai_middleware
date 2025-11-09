from .binders.mistral_binder import mistral_text_to_text_binder


async def text_to_text_orchestration(text: str) -> str:
    return await mistral_text_to_text_binder(text)
