from typing import Any, Callable, List

from src.orchestrator.adapters.mistral_adapter import (
    mistral_text_to_text_adapter,
    mistral_text_embedding_adapter,
)

from src.orchestrator.adapters.huggy_face_adapter import (
    huggy_face_text_embedding_query_adapter,
    huggy_face_text_embedding_documents_adapter,
)

__all__ = [
    "mistral_text_to_text_adapter",
    "mistral_text_embedding_adapter",
    "huggy_face_text_embedding_query_adapter",
    "huggy_face_text_embedding_documents_adapter"
]

text_adapter: List[Callable[..., Any]] = [
    mistral_text_to_text_adapter,
    mistral_text_embedding_adapter,
    huggy_face_text_embedding_query_adapter,
    huggy_face_text_embedding_documents_adapter,
]
