from typing import List
from sqlalchemy.orm import Session
from src.types.classes.log_classes import Log
from src.db.sql.sessions.log_sessions import get_logs as get_logs_from_db


async def get_logs(db: Session) -> List[Log]:
    return await get_logs_from_db(db)
