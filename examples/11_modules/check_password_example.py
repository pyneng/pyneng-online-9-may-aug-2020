"""
Функции для работы с оборудованием
"""
import os

def _internal_function():
    pass


def check_password(username, password, password_length=8,
                   check_username=True, spec_sym=True):
    #print(f'username = {username}, password = {password}, length = {password_length}')
    print(os.listdir('.'))
    if len(password) < password_length:
        print("Пароль слишком короткий")
        return False
    elif check_username and username in password:
        print("Пароль содержит имя пользователя")
        return False
    else:
        print(f"Пароль для пользователя {username} установлен")
        return True


def create_user(db, **kwargs): # ключевые аргументы переменной длины
    username = input("Введите имя пользователя: ")
    while True:
        password = input("Введите пароль: ")
        check = check_password(username, password, **kwargs) # распаковка словаря в ключевые аргументы
        if check:
            break
    with open(db, 'a') as f:
        f.write(f"{username},{password}\n")


if __name__ == "__main__":
    create_user('passwords.txt', password_length=10)
