from typing import List
from sqlalchemy.orm import Session
from src.types.classes.log_classes import LogClass, LogInputClass, LogOutputClass
from src.main.services.log_services import (
    get_all_logs_service, 
    post_log_service
)


async def get_all_logs_controller(db: Session) -> List[LogClass]:
    return await get_all_logs_service(db)


async def post_log_controller(log: LogInputClass, db: Session) -> LogOutputClass:
    new_log = LogClass(
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
