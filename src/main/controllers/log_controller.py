from typing import List
from sqlalchemy.orm import Session
from src.types.classes.log_classes import LogClass
from src.main.services.log_services import get_all_logs_service


async def get_all_logs_controller(db: Session) -> List[LogClass]:
    return await get_all_logs_service(db)
