from typing import List
from sqlalchemy.orm import Session
from src.types.classes.log_classes import Log
from src.db.sql.sessions.log_sessions import get_all_logs_session


async def get_all_logs_service(db: Session) -> List[Log]:
    return await get_all_logs_session(db)
