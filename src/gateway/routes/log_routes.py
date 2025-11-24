from typing import List
from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from src.types.classes import LogOutputClass, LogInputClass
from src.db.sql.engine import get_db
from src.main.controllers.log_controller import get_all_logs_controller, post_log_controller

router = APIRouter(prefix="/log", tags=["log"])


@router.get("/all", status_code=status.HTTP_200_OK, response_model=List[LogOutputClass])
async def get_all_logs(db: Session = Depends(get_db)):
    logs = await get_all_logs_controller(db)
    return logs


@router.post("", status_code=status.HTTP_201_CREATED, response_model=LogOutputClass)
async def post_log(log: LogInputClass, db: Session = Depends(get_db)):
    return await post_log_controller(log, db)
