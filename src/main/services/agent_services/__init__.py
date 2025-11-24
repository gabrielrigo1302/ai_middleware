from typing import Any, Callable, List

from src.main.services.agent_services.ask_agent_intentic_service import (
    ask_agent_intentic_service
)

from src.main.services.agent_services.ask_agent_service import (
    ask_agent_service
)

__all__ = [
    "ask_agent_intentic_service",
    "ask_agent_service"
]

agent_services: List[Callable[..., Any]]  = [
    ask_agent_intentic_service,
    ask_agent_service
]