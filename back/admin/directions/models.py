from pydantic import BaseModel

class NewDirection(BaseModel):
    title: str
    date: str
    cost: int