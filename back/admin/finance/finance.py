from back.db import db_api as db

def getSelledTours(): #Проданные туры
    db.getSelledTours()
def getTour(id): #Данные проданного тура
    db.getTour(id)
def getMounthFinance(month): #Отчет за месяц
    db.getMounthFinance()
def getFinanceTour(id): #подробный Финансовый отчет тура
    db.getFinanceTour(id)
