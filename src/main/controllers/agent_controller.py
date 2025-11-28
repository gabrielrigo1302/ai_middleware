from src.types.classes.agent_classes import AgentIntenticInputClass, AgentInputClass
from src.main.services.agent_services import (
    post_ask_agent_service,
    post_ask_agent_intentic_service,
)
from sqlalchemy.orm import Session


async def post_ask_agent_controller(input: AgentInputClass, db: Session):
    return await post_ask_agent_service(input, db)


async def post_ask_agent_intentic_controller(input: AgentIntenticInputClass):
    return await post_ask_agent_intentic_service(input)
