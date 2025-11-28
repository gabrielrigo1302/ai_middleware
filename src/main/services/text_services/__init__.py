from typing import Any, Callable, List

from src.main.services.text_services.get_rag_text_query_service import (
    get_rag_text_query_service,
)
from src.main.services.text_services.get_summarized_text_service import (
    get_summarized_text_service,
)
from src.main.services.text_services.get_text_embedding_documents_service import (
    get_text_embedding_documents_service,
)
from src.main.services.text_services.post_rag_text_add_document_service import (
    post_rag_text_add_document_service,
)
from src.main.services.text_services.get_text_embedding_query_service import (
    get_text_embedding_query_service,
)

__all__ = [
    "get_rag_text_query_service",
    "get_summarized_text_service",
    "get_text_embedding_documents_service",
    "get_text_embedding_query_service",
    "post_rag_text_add_document_service",
]

# Expose as a list for frameworks that iterate over service callables
text_service: List[Callable[..., Any]] = [
    get_rag_text_query_service,
    get_summarized_text_service,
    get_text_embedding_documents_service,
    get_text_embedding_query_service,
    post_rag_text_add_document_service,
]
