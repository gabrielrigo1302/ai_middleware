from src.orchestrator import orchestrator
from src.types.classes.agent_classes import AgentInput
from src.types.classes.agent_classes import AgentIntenticEnum
from src.main.services.log_services.post_log import create_log
from src.main.services.text_services.get_rag_text_query import get_rag_text_query
from sqlalchemy.orm import Session

from src.types.classes.log_classes import Log


async def ask_agent_service(input: AgentInput, db: Session):
    # Entender a Intenção do prompt
    intentResponse = await analyze_agent_intent(input)

    intents = intentResponse.strip('[]').replace('"', '').split(', ')
    # Tomada de decisão baseada na intenção

    print(intents)
    
    reasons = [""]
    for intent in intents:
        reason = await reasoner_agent_intent(AgentIntenticEnum(intent.strip()), input, db)
        reasons.append(reason)

    # Responder ao usuário
    return reasons


async def analyze_agent_intent(input: AgentInput) -> str:
    system_prompt = f"""
        Você é um assistente que analisa a intenção de prompts de usuários e
        classifica-os em uma ou mais das seguintes categorias: 
            - {AgentIntenticEnum.create_log.value}: caso peça para criar um log de sistema; 
            - {AgentIntenticEnum.generic_ask.value}: caso seja uma pergunta genérica que não se encaixa nas outras categorias; 
            - {AgentIntenticEnum.send_email.value}: caso peça para enviar um e-mail;
            - {AgentIntenticEnum.own_application.value}: caso pergunte sobre a própria aplicação, projeto e similares.;  
        retorne um array de uma ou mais das intenções classificadas.
    """
    response = await orchestrator.text_to_text_orchestration(
        system_prompt, input.prompt
    )

    return response

async def reasoner_agent_intent(intent: AgentIntenticEnum, input: AgentInput, db: Session) -> str:
    response = ""
    match intent:
        case AgentIntenticEnum.generic_ask:
            system_prompt = "Você é um assistente inteligente que responde perguntas de usuários de forma clara e objetiva."
            response = await orchestrator.text_to_text_orchestration(
                system_prompt, input.prompt
            )
        case AgentIntenticEnum.create_log: 
            new_log = Log(
                user_id=1,
                tenant_id=1,
                date="2025-11-18T12:00:00Z",
                region="us-east-1",
                method="POST",
                endpoint="/agent/chat/intentic",
                status_code=200,
                response_time=150,
                response="Log criado com sucesso.",
                error_message="",
                model="mistral-small-latest",
                prompt=input.prompt,
            )
            await create_log(new_log, db)
            response = "Log criado com sucesso."
        case AgentIntenticEnum.send_email:
            system_prompt = "Você é um assistente inteligente que monta mensagens de email e apenas mensagens de email. Você não responde nada além da criação de emails"
            response = await orchestrator.text_to_text_orchestration(
                system_prompt, input.prompt
            )
        case AgentIntenticEnum.own_application:
            response = await get_rag_text_query(
                input.prompt
            )

            response = response['resposta']
        case _:
            response = "Intenção não reconhecida."
    

    return response
