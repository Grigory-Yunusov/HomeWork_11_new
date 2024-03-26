# Перевірити чи в 3-х значному числі всі цифри різні? І чи є тільки 2 однакових числа?
num = input("Number: ")

if len(num) != 3:
    print('Please enter 3 digits')
else:
    n1 = int(num[0])
    n2 = int(num[1])
    n3 = int(num[2])

    if n1 != n3 and n2 != n3 and n1 != n2:
        print('Усі цифри різні')

    elif (n1 == n3 or n2 == n3 or n2 == n1) and not (n1 == n2 and n1 == n3):
        print('Є тільки дві однакові цифри')