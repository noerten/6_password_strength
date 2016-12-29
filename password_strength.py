import os
import re


def load_password_blacklist(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath) as data:
        password_object = data.read()
    password_blacklist = re.findall(r'\w+', password_object)
    return password_blacklist


def get_length_strength(password):
    length_strength = 0
    for i in range(0, 17, 4):
        if len(password) > i:
            length_strength += 1
    return length_strength


def get_case_strength(password):
    return bool((password.lower() or password.upper()) != password)


def get_blacklist_strength(password):
    return bool(password not in load_password_blacklist(filepath))


def get_digital_strength(password):
    return bool(re.findall(r'[\d]', password))


def get_special_symbol_strength(password):
    return bool(re.findall(r'[!@#$%^&*-=+}{]', password))


def get_repeating_strength(password):
    previous = ''
    for symbol in password:
        if symbol == previous:
            return 0
        else:
            previous = symbol
    return 1


def get_password_strength(password):
    length_strength = get_length_strength(password)
    case_strength = get_case_strength(password)
    blacklist_strength = get_blacklist_strength(password)
    digital_strength = get_digital_strength(password)
    special_symbol_strength = get_special_symbol_strength(password)
    repeating_strength = get_repeating_strength(password)
    return sum([length_strength, case_strength, blacklist_strength,
               digital_strength, special_symbol_strength, repeating_strength])


if __name__ == '__main__':
    password = input("Enter a password to get it's strength: ")
    filepath = input('Enter blacklist name/path: ')
    password_strength = str(get_password_strength(password))
    print('Your password scored', password_strength, 'out of 10')
