from typing import List
from sqlalchemy.orm import Session
from src.types.classes.log_classes import LogClass


async def post_log_session(new_log: LogClass, db: Session) -> LogClass:
    db.add(new_log)
    db.commit()
    db.refresh(new_log)

    return new_log


async def get_all_logs_session(db: Session) -> List[LogClass]:
    return db.query(LogClass).all()
