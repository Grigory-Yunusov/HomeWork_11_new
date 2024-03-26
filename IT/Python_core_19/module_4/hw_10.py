from random import randint


def get_random_password():
    result = ''
    count = 0
    while count < 8:
        result += chr(randint(40, 126))
        count += 1
    return result