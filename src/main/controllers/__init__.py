from typing import Any, Callable, List

from src.main.controllers.text_controller import (
    get_rag_text_query_controller,
    get_summarized_text_controller,
    get_text_embedding_controller,
    post_rag_text_add_document_controller
)

from src.main.controllers.agent_controller import (
    ask_agent_intentic_prompt_controller,
    ask_agent_prompt_controller
)

from src.main.controllers.log_controller import (
    get_all_logs_controller,
    post_log_controller
)

__all__ = [
    "get_rag_text_query_controller",
    "get_summarized_text_controller",
    "get_text_embedding_controller",
    "post_rag_text_add_document_controller",
    "ask_agent_intentic_prompt_controller",
    "ask_agent_prompt_controller",
    "get_all_logs_controller",
    "post_log_controller"
]

text_controller: List[Callable[..., Any]] = [
    get_rag_text_query_controller,
    get_summarized_text_controller,
    get_text_embedding_controller,
    post_rag_text_add_document_controller,
    ask_agent_prompt_controller,
    ask_agent_intentic_prompt_controller,
    get_all_logs_controller,
    post_log_controller
]