from typing import Any, Callable, List
from src.db.sql.engine import Base

__all__ = [
    "Base"
]

sql: List[Callable[..., Any]] = [
    Base
]