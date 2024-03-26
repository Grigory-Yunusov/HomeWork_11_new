# Знайдемо індекс останнього входження символу 'а'
string = input('String: ')

count = 0
index = -1
for ch in string:
    if ch == 'a':
        index = count
    count += 1

print(f'The latest a is: {index}')



