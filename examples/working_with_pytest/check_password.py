# -*- coding: utf-8 -*-

def check_passwd(username, password, min_len=10):
    if len(password) < min_len:
        return False
    elif username.lower() in password.lower():
        return False
    else:
        return True


def test_check_passwd():
    assert check_passwd("user1", "546") == False
    assert check_passwd("user2", "dfgjuser2dfkglj546") == False
    assert check_passwd("user1", "5dsa;fk;sdfk46") == True


def test_check_passwd_min_len():
    assert check_passwd("user1", "546", min_len=2) == True
    assert check_passwd("user1", "546", min_len=7) == False
    assert check_passwd("user1", "546") == False
