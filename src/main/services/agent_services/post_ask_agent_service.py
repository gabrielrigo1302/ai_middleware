from src.orchestrator import text_to_text_orchestration
from src.types.classes import AgentInputClass, LogClass
from src.types.enums import AgentIntenticEnum
from src.main.services.log_services import post_log_service
from src.main.services.text_services import get_rag_text_query_service
from sqlalchemy.orm import Session


async def post_ask_agent_service(input: AgentInputClass, db: Session):
    # Entender a Intenção do prompt
    intentResponse = await analyze_agent_intent(input)

    # intents = intentResponse.strip('[]').replace('"', '').split(', ')
    # Tomada de decisão baseada na intenção

    # print(intents)

    reasons = [""]
    # for intent in intents:
    reason = await reasoner_agent_intent(AgentIntenticEnum(intentResponse), input, db)
    reasons.append(reason)

    # Responder ao usuário
    return reasons


async def analyze_agent_intent(input: AgentInputClass) -> str:
    system_prompt = f"""
        Você é um assistente que analisa a intenção de prompts de usuários e
        classifica-os em uma seguintes categorias: 
            - {AgentIntenticEnum.create_log.value}: caso peça para criar um log de sistema; 
            - {AgentIntenticEnum.generic_ask.value}: caso seja uma pergunta genérica que não se encaixa nas outras categorias; 
            - {AgentIntenticEnum.send_email.value}: caso peça para enviar um e-mail;
            - {AgentIntenticEnum.own_application.value}: caso pergunte sobre a própria aplicação, projeto e similares.;  
        retorne uma das intenções classificadas.
    """
    response = await text_to_text_orchestration(system_prompt, input.prompt)

    print("response === ", response)

    return response


async def reasoner_agent_intent(
    intent: AgentIntenticEnum, input: AgentInputClass, db: Session
) -> str:
    response = ""
    match intent:
        case AgentIntenticEnum.generic_ask:
            system_prompt = "Você é um assistente inteligente que responde perguntas de usuários de forma clara e objetiva."
            response = await text_to_text_orchestration(system_prompt, input.prompt)
        case AgentIntenticEnum.create_log:
            system_prompt = """
                Você é um assistente inteligente que cria um objeto para registro de log. 
                Utilize as informações fornecidas para montar a estrutura. 
                A estrutura do log é um dict como o seguinte:
                {
                    "tenant_id": int (id da tenant informada no input),
                    "region": str (ex: "us-east-1"),
                    "response_time": int (tempo que a resposta levou para ser gerada em ms),
                    "response": str (mensagem de resposta do log),
                    "model": str (nome do modelo utilizado),
                    "prompt": str (prompt utilizado)
                }
                """

            log_dict = await text_to_text_orchestration(system_prompt, input.prompt)

            if isinstance(log_dict, str):
                import ast

                try:
                    log_dict = ast.literal_eval(log_dict)
                except Exception:
                    log_dict = {}

            new_log = LogClass(
                user_id=1,
                tenant_id=log_dict.get("tenant_id", 1),
                date="2025-11-18T12:00:00Z",
                region=log_dict.get("region", "us-east-1"),
                method="POST",
                endpoint="/agent/chat/intentic",
                status_code=200,
                response_time=log_dict.get("response_time", 150),
                response=log_dict.get("response", "Log criado com sucesso."),
                error_message="",
                model=log_dict.get("model", "mistral-small-latest"),
                prompt=log_dict.get("prompt", input.prompt),
            )

            await post_log_service(new_log, db)
            response = "Log criado com sucesso."
        case AgentIntenticEnum.send_email:
            system_prompt = "Você é um assistente inteligente que monta mensagens de email e apenas mensagens de email. Você não responde nada além da criação de emails"
            response = await text_to_text_orchestration(system_prompt, input.prompt)
        case AgentIntenticEnum.own_application:
            response = await get_rag_text_query_service(input.prompt)

            system_prompt = f"""
                Você é um assistente inteligente que responde perguntas sobre a aplicação de IA Middleware. 
                Utilize as informações fornecidas para responder de forma clara e objetiva. 
                A sua resposta deve sempre responder a pergunta, bem como trazer o documento de onde foi referenciada e a similaridade da pesquisa vetorial que trouxe esse arquivo. 
                - As informações de contextualização: {response["content"]};
                - ID do documento de onde veio as informações: {response["chunk_id"]}; 
                - Similaridade da pesquisa vetorial: {response["similarity"]}."""

            response = await text_to_text_orchestration(system_prompt, input.prompt)
        case _:
            response = "Intenção não reconhecida."

    return response
