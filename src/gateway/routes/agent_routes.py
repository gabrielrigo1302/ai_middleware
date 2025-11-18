from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from src.types.classes.agent_classes import AgentIntenticInput, AgentInput
from src.main.controllers import agent_controller
from src.db.sql.engine import get_db

router = APIRouter(prefix="/agent", tags=["agent"])


@router.post("/chat", status_code=status.HTTP_200_OK, response_model=dict)
async def post_ask_agent(input: AgentInput, db: Session = Depends(get_db)):
    response = await agent_controller.ask_agent_prompt_controller(input, db)
    return {"message": response}


@router.post("/chat/intentic", status_code=status.HTTP_200_OK, response_model=dict)
async def post_ask_agent_intentic(input: AgentIntenticInput):
    await agent_controller.ask_agent_intentic_prompt_controller(input)
    return {"message": "Agent chat endpoint"}
