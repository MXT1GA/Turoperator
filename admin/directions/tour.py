
from db import db_api as db
def create_tour(title, cost, date, available, howManyPeople):
    return db.create_tour(title, cost, date, available, howManyPeople)
def amountPeoples(id):
    return db.amountPeoples(id)
def costTour(id):
    return db.costTour(id)
