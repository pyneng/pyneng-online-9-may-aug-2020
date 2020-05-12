from check_password_example import check_password

def test_check_password_func():
    assert check_password('user', '12345678') == True, "Для пользователя user пароль 12345678 должен быть правильным"
    assert check_password('user', '12345678', password_length=10) == False
    assert check_password('user', '12345678user') == False
