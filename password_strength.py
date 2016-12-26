import os
import re


def load_password_blacklist(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath) as data:
        password_object = data.read()
    password_blacklist = re.findall(r'\w+', password_object)
    return password_blacklist


def get_password_strength(password):
    if len(password) < 6:
        return 1
    else:
        password_strength = 1
        if len(password) > 9:  
            password_strength += 1
        if len(password) > 12:  
            password_strength += 1
        if len(password) > 15:  
            password_strength += 1
        if (password.lower() or password.upper()) != password: 
            password_strength += 1
        if password not in load_password_blacklist(filepath):
            password_strength += 2
        if re.findall(r'[\d]', password): 
            password_strength += 1
        if re.findall(r'[!@#$%^&*-=+}{]', password):
            password_strength += 1
        previous = ''
        for symbol in password:
            if symbol == previous:
                return password_strength
            else:
                previous = symbol
        password_strength += 1
        return password_strength


if __name__ == '__main__':
    password = input("Enter a password to get it's strength: ")
    filepath = input('Enter blacklist name/path: ')
    password_strength = str(get_password_strength(password))
    print('Your password scored', password_strength, 'out of 10')
