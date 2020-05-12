username = input("Введите имя пользователя: ")
password = input("Введите пароль: ")

password_correct = False

while len(password) < 8 or username.lower() in password.lower():
# while not password_correct:
    if len(password) < 8:
        print("Пароль слишком короткий")
    elif username.lower() in password.lower():
        print("Имя пользователя в пароле")
    elif len(set('@$!%^') & set(password)) == 0:
        print("В пароле должен быть хотя один символ из @$!%^")
    else:
        password_correct = True
        continue
    password = input("Введите пароль еще раз: ")


while not password_correct:
    user_in_password = username.lower() in password.lower()
    spec_sym_in_password = len(set('@$!%^') & set(password)) == 0

    if len(password) < 8 or user_in_password or spec_sym_in_password:
        print('неправильный пароль')
        password = input("Введите пароль еще раз: ")
    else:
        password_correct = True

print(f"Пароль для пользователя {username} установлен")

print('#'*40)

