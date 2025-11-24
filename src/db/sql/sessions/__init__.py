from typing import Any, Callable, List

from src.db.sql.sessions.log_sessions import (
    get_all_logs_session,
    post_log_session
)

__all__ = [
    "get_all_logs_session",
    "post_log_session"
]

sessions: List[Callable[..., Any]] = [
    get_all_logs_session,
    post_log_session
]