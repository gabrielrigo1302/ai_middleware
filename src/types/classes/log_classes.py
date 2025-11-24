from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from src.db.sql import Base


class LogClass(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True)
    ## Quem?
    user_id = Column(Integer)
    tenant_id = Column(String)
    ## Quando?
    date = Column(String)
    ## Onde?
    region = Column(String)
    ## O que?
    method = Column(String)
    endpoint = Column(String)
    status_code = Column(Integer)
    response_time = Column(Integer)  # em milissegundos
    response = Column(String)
    error_message = Column(String)
    model = Column(String)
    prompt = Column(String)


class LogInputClass(BaseModel):
    user_id: int
    tenant_id: str
    date: str
    region: str
    method: str
    endpoint: str
    status_code: int
    response_time: int
    response: str
    error_message: str
    model: str
    prompt: str


class LogOutputClass(LogInputClass):
    id: int

    class Config:
        from_attributes = True
