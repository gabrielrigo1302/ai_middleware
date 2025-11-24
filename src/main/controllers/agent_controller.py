from src.types.classes.agent_classes import AgentIntenticInputClass, AgentInputClass
from src.main.services.agent_services import (
    ask_agent_service, 
    ask_agent_intentic_service
)
from sqlalchemy.orm import Session


async def ask_agent_prompt_controller(input: AgentInputClass, db: Session):
    return await ask_agent_service(input, db)


async def ask_agent_intentic_prompt_controller(input: AgentIntenticInputClass):
    return await ask_agent_intentic_service(input)
