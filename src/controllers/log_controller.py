from typing import List
from sqlalchemy.orm import Session
from src.types.classes.log_classes import Log, LogInput, LogOutput
from src.services.log_services.get_logs import get_logs as fetch_logs
from src.services.log_services.post_log import create_log


async def get_logs(db: Session) -> List[Log]:
    return await fetch_logs(db)


async def post_log(log: LogInput, db: Session) -> LogOutput:
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

    return await create_log(new_log, db)
