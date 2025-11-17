from typing import List
from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from src.types.classes.log_classes import LogOutput, LogInput
from src.db.sql.engine import get_db
from src.controllers import log_controller

router = APIRouter(prefix="/log", tags=["log"])


@router.get("/all", status_code=status.HTTP_200_OK, response_model=List[LogOutput])
async def get_all_logs(db: Session = Depends(get_db)):
    logs = await log_controller.get_logs(db)
    return logs


@router.post("", status_code=status.HTTP_201_CREATED, response_model=LogOutput)
async def post_log(log: LogInput, db: Session = Depends(get_db)):
    return await log_controller.post_log(log, db)
