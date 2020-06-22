from pprint import pprint
import netmiko
from check_password import check_passwd


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

if __name__ == "__main__":
    data = [
        ["user10", "sdldfj"],
        ["user20", "aaaaaaaaaaaaaaaaa#"],
        ["user30", "aaaaaaaaaaaa#3"],
    ]
    yes, no = select_correct_passwd(data, check_spec_sym=True)
    print("Правильные", yes)
    print("Неправильные", no)
