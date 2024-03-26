# Знайти у рядку номер першого входження символу 'a'
string = input("Введіть строку: ")

count = 0
# hello and
for char in string:
    if char == '':
        break
    count += 1

print(f"a: {count}")
