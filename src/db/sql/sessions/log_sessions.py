from typing import List
from sqlalchemy.orm import Session
from src.types.classes.log_classes import Log


async def post_log_session(new_log: Log, db: Session) -> Log:
    db.add(new_log)
    db.commit()
    db.refresh(new_log)

    return new_log


async def get_all_logs_session(db: Session) -> List[Log]:
    return db.query(Log).all()
