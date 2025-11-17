from src.types.classes.agent_classes import AgentIntenticInput, AgentInput
from src.services.agent_services import ask_agent_intentic_service
from src.services.agent_services import ask_agent_service


async def ask_agent_prompt_controller(input: AgentInput):
    return await ask_agent_service.ask_agent_service(input)


async def ask_agent_intentic_prompt_controller(input: AgentIntenticInput):
    return await ask_agent_intentic_service.ask_agent_intentic_service(input)
