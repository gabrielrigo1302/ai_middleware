import logging
from settings import settings
from src.types.enums.log_enums import LogLevelEnum

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def log_debug(logLevel: LogLevelEnum, location: str, message: str):
    if settings.DEBUG is False:
        return

    elif logLevel == LogLevelEnum.info:
        logger.info("Requisição acessou: " + location + ". " + message)

    elif logLevel == LogLevelEnum.warning:
        logger.warning("Atenção: " + location + ". " + message)

    elif logLevel == LogLevelEnum.error:
        logger.error("Erro ocorrido na : " + location + ". " + message)
