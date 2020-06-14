# -*- coding: utf-8 -*-
from pprint import pprint


def select_correct_passwd(check_data):
    correct_password = []
    incorrect_password = []

    for data in check_data:
        user, passwd = data
        if len(password) < min_passwd_len:
            incorrect_password.append([user, passwd])
        elif username.lower() in password.lower():
            incorrect_password.append([user, passwd])
        elif spec_sym and not set(spec_sym) & set(password):
            incorrect_password.append([user, passwd])
        else:
            correct_password.append([user, passwd])
    return correct_password, incorrect_password


data_to_check = [
    ["user10", "sdldfj"],
    ["user20", "sdf####klfdj"],
    ["user30", "ssdkfjsus#%er3df"],
]
yes, no = select_correct_passwd(data_to_check)
pprint(yes)
pprint(no)
