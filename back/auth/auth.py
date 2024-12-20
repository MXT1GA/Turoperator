from back.db import db_api as db

def checkAuth(lg, password):
    return db.checkAuth(lg, password)