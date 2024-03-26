"""
Більше можливостей pathlib
"""
from pathlib import Path

current_dir = Path('.')
print(current_dir)
# current_dir = current_dir / 'Temp'
file = current_dir / 'bin' / 'image' / 'test.png'
# print(file.exists())

for element in current_dir.glob('**/*.png'):
# for element in current_dir.glob('*.txt'):
    print(element)

tmp = Path('empty.txt')
if tmp.exists():
    tmp.unlink()

