from enum import Enum


class LogLevelEnum(str, Enum):
    info = "info"
    warning = "warning"
    error = "error"
