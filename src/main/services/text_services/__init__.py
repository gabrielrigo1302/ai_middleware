from typing import Any, Callable, List

from .get_rag_text_query import get_rag_text_query
from .get_summarized_text import get_summarized_text
from .get_text_embedding import get_text_embedding
from .post_rag_text_add_document import post_rag_text_add_document

__all__ = [
    "get_rag_text_query",
    "get_summarized_text",
    "get_text_embedding",
    "post_rag_text_add_document",
]

# Expose as a list for frameworks that iterate over service callables
text_service: List[Callable[..., Any]] = [
    get_rag_text_query,
    get_summarized_text,
    get_text_embedding,
    post_rag_text_add_document,
]
