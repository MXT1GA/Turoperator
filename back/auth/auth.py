from back.db import db_api as db

def checkAuth(lg, password) -> bool:
    return db.checkAuth(lg, password)

def createUsers(lg, password, lastname, name, patronymic):
    return db.createUsers(lg, password, lastname, name, patronymic)

def delUsers(id):
    return db.delUsers(id)