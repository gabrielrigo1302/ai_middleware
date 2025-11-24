from pydantic import BaseModel


class TextInputClass(BaseModel):
    text: str
