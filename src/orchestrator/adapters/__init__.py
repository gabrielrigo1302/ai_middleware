from typing import Any, Callable, List

from src.orchestrator.adapters.mistral_adapter import (
    mistral_text_to_text_adapter,
    mistral_text_embedding_adapter,
)

__all__ = [
    "mistral_text_to_text_adapter",
    "mistral_text_embedding_adapter",
]

text_adapter: List[Callable[..., Any]] = [
    mistral_text_to_text_adapter,
    mistral_text_embedding_adapter,
]