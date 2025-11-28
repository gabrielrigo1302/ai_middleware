from typing import Any, Callable, List
from src.orchestrator.providers.mistral_provider import (
    mistral_text_embedding_provider,
    mistral_text_to_text_provider,
)

__all__ = [
    "mistral_text_embedding_provider",
    "mistral_text_to_text_provider",
]

orchestrator_provider: List[Callable[..., Any]] = [
    mistral_text_to_text_provider,
    mistral_text_embedding_provider,
]
