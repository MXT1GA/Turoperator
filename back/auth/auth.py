from back.db import db_api as db

def checkAuth(lg, password) -> bool:
    return db.checkAuth(lg, password)

def createUsers():
    pass