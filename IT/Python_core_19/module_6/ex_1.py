"""
Читання та запис у файл.
"""
file = open('test.txt', 'w', encoding='utf-8')
file.write('Hello Test\n')
file.write('Hello Ukraine\n')
file.writelines(['Hi Vova\n', 'Hi Olga\n', 'Hi Iryna\n'])
file.close()

file = open('test.txt', 'r', encoding='utf-8')
# result = file.read()
# result = file.readline()
result = file.readlines()
print(result)
file.close()
