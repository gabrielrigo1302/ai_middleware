from typing import Any, Callable, List
from src.types.classes.agent_classes import AgentInputClass, AgentIntenticInputClass
from src.types.classes.log_classes import LogClass, LogInputClass, LogOutputClass
from src.types.classes.text_classes import TextInputClass

__all__ = [
    "AgentInputClass",
    "AgentIntenticInputClass",
    "LogClass",
    "LogInputClass",
    "LogOutputClass",
    "TextInputClass",
]

agent_classes: List[Callable[..., Any]] = [
    AgentInputClass,
    AgentIntenticInputClass,
    LogClass,
    LogInputClass,
    LogOutputClass,
    TextInputClass,
]
