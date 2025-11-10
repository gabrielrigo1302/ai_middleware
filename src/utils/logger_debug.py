import logging
from enum import Enum
from settings import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LogLevel(str, Enum):
    info = "info"
    warning = "warning"
    error = "error"

def log_debug(logLevel: LogLevel, location: str, message: str):
    if settings.DEBUG is False:
        return
    
    elif logLevel == LogLevel.info:
        logger.info("Requisição acessou: " + location + ". " + message)

    elif logLevel == LogLevel.warning:
        logger.warning("Atenção: " + location + ". " + message)

    elif logLevel == LogLevel.error:
        logger.error("Erro ocorrido na : " + location + ". " + message)