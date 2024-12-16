from db import db_api as db

def createDirections():
    return db.createDirections(title, date, cost)
def listDirections():
    return db.listDirections()
