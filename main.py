from fastapi import FastAPI

from back.admin.directions.models import *
from back.admin.directions import directions as directions

from back.auth import auth
from back.auth.models import *
app = FastAPI()


@app.get("/")
async def root():
    return "Главная страница сайта пока не создана"


@app.post("/directions/createDirections/")
async def createDirections(newDirections: NewDirection):
    return directions.createDirections(newDirections.title, newDirections.date, newDirections.cost)

@app.get("/finance/")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/operatorsTransports")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/tours/")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.post("/auth/create")
async def createUsers(newClient: NewClient):
    return auth.createUsers(newClient.login, newClient.password, newClient.lastname, newClient.name, newClient.patronymic)

@app.post("/auth/checkAuth")
async def checkAuth(checkAuth: checkAuth):
    return auth.checkAuth(checkAuth.login, checkAuth.password)

@app.post("/auth/del")
async def delUsers(checkAuth: checkAuth):
    return auth.delUsers(id)