from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from src.types.classes import AgentIntenticInputClass, AgentInputClass
from src.main.controllers.agent_controller import  ask_agent_intentic_prompt_controller, ask_agent_prompt_controller
from src.db.sql.engine import get_db

router = APIRouter(prefix="/agent", tags=["agent"])


@router.post("/chat", status_code=status.HTTP_200_OK, response_model=dict)
async def post_ask_agent(input: AgentInputClass, db: Session = Depends(get_db)):
    response = await ask_agent_prompt_controller(input, db)
    return {"message": response}


@router.post("/chat/intentic", status_code=status.HTTP_200_OK, response_model=dict)
async def post_ask_agent_intentic(input: AgentIntenticInputClass):
    await ask_agent_intentic_prompt_controller(input)
    return {"message": "Agent chat endpoint"}
