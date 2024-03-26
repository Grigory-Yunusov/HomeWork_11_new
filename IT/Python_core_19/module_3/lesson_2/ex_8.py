# Потрібно написати функцію для вгадування числа
# 0 ... n
from random import randint


def game(n):
    count = 0
    goal = randint(0, n)
    while True:
        try:
            answer = int(input(f'Вгадайте задумане число від 0 до {n}: '))
            count += 1
        except Exception:
            print("It's not number")
        if answer > goal:
            print("Ваше число більше за задумане")
        elif answer < goal:
            print("Ваше число менше за задумане")
        else:
            print(f'Ви вгадали число за {count} кроків')
            break

game(10)