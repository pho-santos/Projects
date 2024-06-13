import getpass

def password_validator(password):
    if password.isnumeric() and len(password) < 8:
        pass_str = 1
        print('Your password is very weak.')
    elif password.isalpha() and len(password) < 8:
        pass_str = 2
        print('Your password is weak.')
    elif any(c.isdigit() for c in password) and any(c.isalpha() for c in password) and not any(not c.isalnum() for c in password) and len(password) >= 8 :
        pass_str = 4
        print('Your password is strong.')
    elif password.isalnum() and len(password) >= 8:
        pass_str = 3
        print('Your password has medium strength.')
    elif any(c.isdigit() for c in password) and any(c.isalpha() for c in password) and any(not c.isalnum() for c in password) and len(password) >= 8:
        pass_str = 5
        print('Your password is very strong!')
    else:
        pass_str = 3
        print('Your password has medium strength.')
    return pass_str

recomendations = [
    'Use letters, numbers and special characters;',
    'Have at least 8 characters.'
]

print(f'Hello! We are going to validate the strength of your password, please follow these rules:\n {recomendations}')
password = getpass.getpass('Please, input your password \n')
pass_str = password_validator(password)