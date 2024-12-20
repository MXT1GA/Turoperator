import requests
import json

# Замените на ваш фактический URL API
API_URL = "http://127.0.0.1:8000"  


def register():
    """Регистрация нового пользователя."""
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    lastname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")

    data = {
        "login": login,
        "password": password,
        "lastname": lastname,
        "name": name,
        "patronymic": patronymic
    }

    try:
        response = requests.post(f"{API_URL}/auth/create", json=data)
        response.raise_for_status() # Поднимает исключение для не-2xx статусов
        print("Регистрация успешна!")
        print(response.json()) # Выводим ответ сервера
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при регистрации: {e}")


def login():
    """Вход в существующий профиль."""
    login = input("Введите логин: ")
    password = input("Введите пароль: ")

    data = {
        "login": login,
        "password": password
    }

    try:
        response = requests.post(f"{API_URL}/auth/checkAuth", json=data)
        response.raise_for_status()
        if response.json() == True: print("\n\nВход успешен!")
        else:
            print(f"Ошибка при входе: Неверный пароль или логин")
            print(response.json()) # Выводим ответ сервера
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при входе: {e}")


if __name__ == "__main__":
    while True:
        print("\nВыберите действие:")
        print("1. Регистрация")
        print("2. Вход")
        print("3. Выход")

        choice = input("Ваш выбор: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            break
        else:
            print("Неверный выбор.")

