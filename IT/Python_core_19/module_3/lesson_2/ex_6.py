# Написати калькулятор
# 3, 4, '+' -> 7
# 3, 4, '*' -> 12
# 3, 4, '-' -> Функція не підтримує дану операцію
def calc(operation: str):
    result = None  # -
    if operation == "+":
        result = 0
    elif operation == "*":
        result = 1
    else:
        return "Функція не підтримує дану операцію"

    value = input('Please enter the value: ')

    while True:
        if value == '':
            break
        if operation == "+":
            result += int(value)
        elif operation == "*":
            result *= int(value)
        value = input('Please enter the value: ')
    return result


result = calc("*")
print(result)
