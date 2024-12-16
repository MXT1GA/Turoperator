from db import db_api as db

def getSelledTours(): #Проданные туры
    db.getSelledTours()
def getTour(): #Данные проданного тура
    db.getTour()
def getMounthFinance(): #Отчет за месяц
    db.getMounthFinance()
def getFinanceTour(): #подробный Финансовый отчет тура
    db.getFinanceTour()
