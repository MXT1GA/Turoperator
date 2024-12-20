from pydantic import BaseModel

class NewClient(BaseModel):
    login: str
    password: str
    lastname: str
    name: str
    patronymic: str

class checkAuth(BaseModel):
    login: str
    password: str