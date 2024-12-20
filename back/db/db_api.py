import sqlite3

def createOperatorTransports(title, cost):
    try:
        connection = sqlite3.connect('db_turooperator.db')
        cursor = connection.cursor()
        cursor.execute('''
        INSERT INTO OperatorsTransports (title, cost)
        VALUES (?, ?)
        ''', (title, cost))
        connection.commit()
        connection.close()
        return True
    except Exception as e:
        print(e)
        return False

def listOperatorsTransport():
    try:
        connection = sqlite3.connect('db_turooperator.db')
        cursor = connection.cursor()
        cursor.execute('''
        SELECT * FROM OperatorsTransports
    ''')
        results = cursor.fetchall()
        connection.commit()
        connection.close()
        return results
    except Exception as e:
        print(e)
        return False

def createDirections(title, date, cost):
    try:
        connection = sqlite3.connect('db_turooperator.db')
        cursor = connection.cursor()
        cursor.execute('''
        INSERT INTO Directions (title, date, cost)
        VALUES (?, ?, ?)
        ''', (title, date, cost))
        connection.commit()
        connection.close()
        return True
    except Exception as e:
        print(e)
        return False

def listDirections():
    try:
        connection = sqlite3.connect('db_turooperator.db')
        cursor = connection.cursor()
        cursor.execute('''
        SELECT * FROM Directions
    ''')
        results = cursor.fetchall()
        connection.commit()
        connection.close()
        return results
    except Exception as e:
        print(e)
        return False

def create_tour(title, cost, date, available, howManyPeople):
    try:
        connection = sqlite3.connect('db_turooperator.db')
        cursor = connection.cursor()
        cursor.execute('''
        INSERT INTO Tours (title, cost, date, available, howManyPeople)
        VALUES (?, ?, ?, ?, ?)
        ''', (title, cost, date, available, howManyPeople))
        connection.commit()
        connection.close()
        return True
    except Exception as e:
        print(e)
        return False

def amountPeoples(id):
    try:
        connection = sqlite3.connect('db_turooperator.db')
        cursor = connection.cursor()

        cursor.execute('''
        SELECT title, howManyPeople FROM Tours WHERE id = ?
    ''', (id))
        results = cursor.fetchall()
        connection.commit()
        connection.close()
        return results
    except Exception as e:
        print(e)
        return False

def costTour(id):
    try:
        connection = sqlite3.connect('db_turooperator.db')
        cursor = connection.cursor()
        cursor.execute('''
        SELECT title, cost FROM Tours WHERE id = ?
        ''', (id))
        results = cursor.fetchall()
        connection.commit()
        connection.close()
        return results
    except Exception as e:
        print(e)
        return False

#==============================АВТОРИЗАЦИЯ==============================

def checkAuth(lg, password):
    try:
        connection = sqlite3.connect('db_turooperator.db')
        cursor = connection.cursor()
        cursor.execute('''
        SELECT * FROM Clients WHERE login = ? AND password = ?
        ''', (lg, password))
        results = cursor.fetchall()
        connection.commit()
        connection.close()
        if len(results) > 0: return True
    except Exception as e:
        print(e)
        return False
#==============================ФИНАНСЫ==============================

def getSelledTours(): #Проданные туры
    try:
        connection = sqlite3.connect('db_turooperator.db')
        cursor = connection.cursor()
        cursor.execute('''
        SELECT * FROM SelledTours
                ''')
        results = cursor.fetchall()
        connection.commit()
        connection.close()
        return results
    except Exception as e:
        print(e)
        return False

def getTour(id): #Данные проданного тура
    try:
        connection = sqlite3.connect('db_turooperator.db')
        cursor = connection.cursor()
        cursor.execute('''
        SELECT * FROM Tours WHERE id = ?
                        ''', (id))
        results = cursor.fetchall()
        connection.commit()
        connection.close()
        return results
    except Exception as e:
        print(e)
        return False

def getMounthFinance(month): #Отчет за месяц
    try:
        connection = sqlite3.connect('db_turooperator.db')
        cursor = connection.cursor()
        cursor.execute('''
        SELECT * FROM SelledTours WHERE month = ?
                        ''', (month))
        results = cursor.fetchall()
        connection.commit()
        connection.close()
        return results
    except Exception as e:
        print(e)
        return False

def getFinanceTour(id): #подробный Финансовый отчет тура
    try:
        connection = sqlite3.connect('db_turooperator.db')
        cursor = connection.cursor()
        cursor.execute('''
        SELECT * FROM SelledTours WHERE id = ?
                        ''', (id))
        results = cursor.fetchall()
        connection.commit()
        connection.close()
        return results
    except Exception as e:
        print(e)
        return False
