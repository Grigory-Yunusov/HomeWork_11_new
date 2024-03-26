# Порахувати суму всіх аргументів

def sum(start, *args):
    sum = start
    for element in args:
        sum += element
    return sum

result = sum(2, 3, 5, 1)
print(result)

# print(sum([2, 3, 5, 1]))