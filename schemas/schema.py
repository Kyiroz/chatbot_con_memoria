from pydantic import BaseModel
class Bot(BaseModel):
    pregunta: str
    USERID: int