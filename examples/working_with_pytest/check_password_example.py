def check_password(username, password, password_length=8,
                   check_username=True, spec_sym=True):
    if len(password) < password_length:
        return False
    elif check_username and username in password:
        return False
    else:
        return True

