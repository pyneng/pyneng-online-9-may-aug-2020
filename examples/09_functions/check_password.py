# -*- coding: utf-8 -*-
from pprint import pprint

def check_passwd(username, password, min_passwd_len=8, spec_sym=None):
    #print(f"PARAMS: {username:10} {password:20} {min_passwd_len}")
    if len(password) < min_passwd_len:
        message = "Пароль слишком короткий"
        return False, message
    elif username.lower() in password.lower():
        message = "Пароль содержит имя пользователя"
        return False, message
    elif spec_sym and not set(spec_sym) & set(password):
        message = f"Пароль должен содержать один из символов {spec_sym}"
        return False, message
    else:
        message = "Пароль для пользователя {} установлен".format(username)
        return True, message


def select_correct_passwd(check_data):
    correct_password = []
    incorrect_password = []

    for data in check_data:
        user, passwd = data
        check, message = check_passwd(user, password=passwd, spec_sym="@$#!")
        if check:
            correct_password.append([user, passwd])
        else:
            incorrect_password.append([user, passwd])
    return correct_password, incorrect_password


data= [
    ["user10", "sdldfj"],
    ["user20", "sdf####klfdj"],
    ["user30", "ssdkfjsus#%er3df"],
]
yes, no = select_correct_passwd(data)
pprint(yes)
pprint(no)
