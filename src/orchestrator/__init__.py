from typing import Any, Callable, List
from src.orchestrator.orchestrator import (
    text_to_text_orchestration,
    text_embedding_documents_orchestration,
    text_embedding_query_orchestration,
)

__all__ = [
    "text_to_text_orchestration",
    "text_embedding_query_orchestration",
    "text_embedding_documents_orchestration",
]

orchestrator: List[Callable[..., Any]] = [
    text_to_text_orchestration,
    text_embedding_documents_orchestration,
    text_embedding_query_orchestration,
]
