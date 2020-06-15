# -*- coding: utf-8 -*-
from pprint import pprint


def check_passwd(
    username, password, min_passwd_len=8, spec_sym=None, numbers=False
):
    if len(password) < min_passwd_len:
        message = "Пароль слишком короткий"
        return False, message
    elif username.lower() in password.lower():
        message = "Пароль содержит имя пользователя"
        return False, message
    elif numbers and not set("0123456789") & set(password):
        message = f"Пароль должен содержать хотя бы одно число"
        return False, message
    elif spec_sym and not set(spec_sym) & set(password):
        message = f"Пароль должен содержать один из символов {spec_sym}"
        return False, message
    else:
        message = "Пароль для пользователя {} установлен".format(username)
        return True, message


# ключевые аргументы переменной длины
def select_correct_passwd(check_data, **kwargs):
    correct_password = []
    incorrect_password = []

    for data in check_data:
        user, passwd = data
        # распаковка словаря в ключевые аргументы
        check, message = check_passwd(user, password=passwd, **kwargs)
        if check:
            correct_password.append([user, passwd])
        else:
            incorrect_password.append([user, passwd])
    return correct_password, incorrect_password


data = [
    ["user10", "sdldfj"],
    ["user20", "sdf####klfdj"],
    ["user30", "ssdkfjsus#%er3df"],
]
yes, no = select_correct_passwd(data, spec_sym="@#$", numbers=True)
pprint(yes)
pprint(no)
