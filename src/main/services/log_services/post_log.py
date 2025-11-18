from src.types.classes.log_classes import Log
from src.db.sql.sessions.log_sessions import add_log
from sqlalchemy.orm import Session


async def create_log(log: Log, db: Session) -> Log:
    await add_log(log, db)
    # Return the created ORM object (id should be populated after commit)
    return log
