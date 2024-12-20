import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('db_turooperator.db')
cursor = connection.cursor()

# Создаем таблицу Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS Tours (
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
directions TEXT NOT NULL,
cost INTEGER NOT NULL,
date TEXT NOT NULL,
available BOOLEAN NOT NULL,
operatorsTransports TEXT NOT NULL,
howManyPeople INTEGER NOT NULL,
FOREIGN KEY (directions) REFERENCES directions (id),
FOREIGN KEY (operatorsTransports) REFERENCES OperatorsTransports (id)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Directions (
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
date TEXT NOT NULL,
cost INTEGER NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS OperatorsTransports (
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
cost INTEGER NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS SelledTours (
id INTEGER PRIMARY KEY AUTOINCREMENT,
tour INTEGER NOT NULL,
cost INTEGER NOT NULL,
profits INTEGER NOT NULL,
Revenue INTEGER NOT NULL,
month TEXT NOT NULL,
tax INTEGER NOT NULL,
FOREIGN KEY (tour) REFERENCES OperatorsTransports (Tours)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
login TEXT NOT NULL,
password TEXT NOT NULL,
lastname INTEGER NOT NULL,
name TEXT NOT NULL,
patronymic TEXT NOT NULL
)
''')

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()
