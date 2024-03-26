"""
Запис у файл байтових рядків. Робота з різними кодуваннями
"""

from pathlib import Path
text = 'Привіт потік GoIT 19!'
print(text.encode())
print(text.encode('utf-16'))
print(text.encode('cp1251'))
a = b'\xcf\xf0\xe8\xe2\xb3\xf2 \xef\xee\xf2\xb3\xea GoIT 19!'
print(a.decode('cp1251'))
folder = Path('Hello')
with open(folder / 'utf-8.txt', 'wb') as f:
    f.write(text.encode())
with open(folder / 'utf-16.txt', 'wb') as f:
    f.write(text.encode('utf-16'))
with open(folder / 'cp1251.txt', 'wb') as f:
    f.write(text.encode('cp1251'))


with open(folder / 'utf-8.txt', 'rb') as f:
    print(f.read().decode())
with open(folder / 'utf-16.txt', 'rb') as f:
    print(f.read().decode('utf-16'))
with open(folder / 'cp1251.txt', 'rb') as f:
    print(f.read().decode('cp1251'))