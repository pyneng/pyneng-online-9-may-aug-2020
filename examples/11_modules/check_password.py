# -*- coding: utf-8 -*-


def check_passwd(
    username,
    password,
    min_passwd_len=8,
    check_spec_sym=False,
    default_spec_sym="@#$%",
    numbers=False,
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
    elif check_spec_sym and not set(default_spec_sym) & set(password):
        message = f"Пароль должен содержать один из символов {spec_sym}"
        return False, message
    else:
        message = "Пароль для пользователя {} установлен".format(username)
        return True, message
