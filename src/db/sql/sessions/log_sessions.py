from sqlalchemy.orm import Session
from src.db.sql.dtos.Log import Log

async def add_log (new_log: Log, db: Session) -> Log:
    db.add(new_log)
    db.commit()
    db.refresh(new_log)

    return new_log

async def get_logs(db: Session) -> list[Log]:
    return db.query(Log).all()