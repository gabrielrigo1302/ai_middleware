from typing import Any, Callable, List

from src.main.services.agent_services.post_ask_agent_intentic_service import (
    post_ask_agent_intentic_service,
)

from src.main.services.agent_services.post_ask_agent_service import (
    post_ask_agent_service,
)

__all__ = ["post_ask_agent_intentic_service", "post_ask_agent_service"]

agent_services: List[Callable[..., Any]] = [
    post_ask_agent_intentic_service,
    post_ask_agent_service,
]
