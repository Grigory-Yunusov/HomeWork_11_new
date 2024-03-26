# Перевірити чи 3-х значне число паліндром
#  101, 202, 535, etc.

num = int(input("Number: "))

n1 = num // 100
n2 = num % 10

if n1 == n2:
    print('Yes')
else:
    print('No')