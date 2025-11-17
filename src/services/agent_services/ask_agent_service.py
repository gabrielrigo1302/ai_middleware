from src.orchestrator import orchestrator
from src.types.classes.agent_classes import AgentInput
from src.types.classes.agent_classes import AgentIntenticEnum


async def ask_agent_service(input: AgentInput):
    # Entender a Intenção do prompt
    intent = await analyze_agent_intent(input)
    # Tomada de decisão baseada na intenção
    # Executar ações apropriadas
    # Responder ao usuário
    return intent


async def analyze_agent_intent(input: AgentInput) -> str:
    system_prompt = f"""
        Você é um assistente que analisa a intenção de prompts de usuários e
        classifica-os nas seguintes categorias: 
            - {AgentIntenticEnum.create_log}; 
            - {AgentIntenticEnum.generic_ask}; 
            - {AgentIntenticEnum.send_email}; 
        Emplique o porque da decisão tomada.
    """
    response = await orchestrator.text_to_text_orchestration(
        system_prompt, input.prompt
    )

    return response
