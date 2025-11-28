from typing import Any, Callable, List

from src.main.services.log_services.post_log_service import post_log_service

from src.main.services.log_services.get_logs_service import get_all_logs_service

__all__ = ["post_log_service", "get_all_logs_service"]

log_services: List[Callable[..., Any]] = [post_log_service, get_all_logs_service]
