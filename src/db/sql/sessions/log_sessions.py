from typing import List
from sqlalchemy.orm import Session
from src.types.classes.log_classes import Log


async def add_log(new_log: Log, db: Session) -> Log:
    db.add(new_log)
    db.commit()
    db.refresh(new_log)

    return new_log


async def get_logs(db: Session) -> List[Log]:
    return db.query(Log).all()
