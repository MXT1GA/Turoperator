from back.db import db_api as db


def createDirections(title, date, cost):
    return db.createDirections(title, date, cost)
def listDirections():
    return db.listDirections()
