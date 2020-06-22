from check_password_db import select_correct_passwd
from pprint import pprint

data = [
    ["user1", "password1"],
    ["user2", "passw2r31"],
    ["user3", "passwo2d1"],
    ["user4", "password3"],
]


def log_passwords_to_file(filename, user_passwd_list):
    correct, wrong = select_correct_passwd(data)
    with open(filename, "w") as f:
        f.write("### Правильные пароли:\n")
        for user, passwd in correct:
            f.write(f"{user},{passwd}\n")
        f.write("### Неправильные пароли:\n")
        for user, passwd in wrong:
            f.write(f"{user},{passwd}\n")


if __name__ == "__main__":
    log_passwords_to_file("password_check_log.txt", data)

