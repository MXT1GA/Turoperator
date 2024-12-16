from db import db_api as db

def createOperatorTransports(title, cost):
    return db.createOperatorTransports(title, cost)
def listOperatorsTransport():
    return db.listOperatorsTransport()
