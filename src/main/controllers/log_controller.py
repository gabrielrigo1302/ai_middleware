from typing import List
from sqlalchemy.orm import Session
from src.types.classes.log_classes import Log, LogInput, LogOutput
from src.main.services.log_services.get_logs import get_all_logs_service
from src.main.services.log_services.post_log import post_log_service


async def get_all_logs_controller(db: Session) -> List[Log]:
    return await get_all_logs_service(db)


async def post_log_controller(log: LogInput, db: Session) -> LogOutput:
    new_log = Log(
        user_id=log.user_id,
        tenant_id=log.tenant_id,
        date=log.date,
        region=log.region,
        method=log.method,
        endpoint=log.endpoint,
        status_code=log.status_code,
        response_time=log.response_time,
        response=log.response,
        error_message=log.error_message,
        model=log.model,
        prompt=log.prompt,
    )

    return await post_log_service(new_log, db)
