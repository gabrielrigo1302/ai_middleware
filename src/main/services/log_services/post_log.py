from src.types.classes.log_classes import Log
from src.db.sql.sessions.log_sessions import post_log_session
from sqlalchemy.orm import Session


async def post_log_service(log: Log, db: Session) -> Log:
    await post_log_session(log, db)
    # Return the created ORM object (id should be populated after commit)
    return log
