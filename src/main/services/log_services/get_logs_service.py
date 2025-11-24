from typing import List
from sqlalchemy.orm import Session
from src.types.classes import LogClass
from src.db.sql.sessions import get_all_logs_session


async def get_all_logs_service(db: Session) -> List[LogClass]:
    return await get_all_logs_session(db)
