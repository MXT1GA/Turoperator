from fastapi import FastAPI

from back.admin.directions import directions
from back.admin.directions.models import *
from back.admin.directions import directions as directions
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
