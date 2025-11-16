from sqlalchemy.orm import Session
from src.db.sql.dtos.Log import Log
from src.db.sql.sessions.log_sessions import get_logs as get_logs_from_db

async def get_logs(db: Session) -> list[Log]:
    return await get_logs_from_db(db)