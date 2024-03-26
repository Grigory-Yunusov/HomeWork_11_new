"""
Основні можливості pathlib
"""

from pathlib import Path
current_path = Path()
print(current_path)
print(current_path.cwd())
file = current_path / 'bin' / 'image' / 'test.png'
print(file)
file = current_path.joinpath('bin', 'image', 'test.drawio.svg')
print(file)

print(file.parts)

print(file.name)
print(file.name.split('.')[2])

print(file.parent)
print(file.suffix)
print(file.suffixes)
