def check_password(username, password, password_length=8,
                   check_username=True, spec_sym=True):
    #print(f'username = {username}, password = {password}, length = {password_length}')
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


create_user('passwords.txt', password_length=10, spec_sym=True)

'''
In [181]: create_user('passwords.txt')
Введите имя пользователя: bob
Введите пароль: sdf
username = bob, password = sdf, length = 8
Пароль слишком короткий
Введите пароль: aldkfjlskjflsabob
username = bob, password = aldkfjlskjflsabob, length = 8
Пароль содержит имя пользователя
Введите пароль: l;fsadkflsa;djfl
username = bob, password = l;fsadkflsa;djfl, length = 8
Пароль для пользователя bob установлен

In [182]: cat passwords.txt
username,password
bob,l;fsadkflsa;djfl
'''
