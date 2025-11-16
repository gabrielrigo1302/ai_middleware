from typing import List
from sqlalchemy.orm import Session
from src.db.sql.dtos.Log import Log, LogOutput
from src.services.log_services.get_logs import get_logs as fetch_logs
from src.services.log_services.post_log import create_log


async def get_logs(db: Session) -> List[Log]:
    logs = await fetch_logs(db)
    # Convert ORM objects to Pydantic models for a clean JSON response
    return logs


async def post_log(log: Log, db: Session) -> LogOutput:
    return await create_log(log, db)
