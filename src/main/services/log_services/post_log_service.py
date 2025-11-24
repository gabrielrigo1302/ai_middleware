from src.types.classes import LogClass
from src.db.sql.sessions import post_log_session
from sqlalchemy.orm import Session


async def post_log_service(log: LogClass, db: Session) -> LogClass:
    await post_log_session(log, db)
    # Return the created ORM object (id should be populated after commit)
    return log
