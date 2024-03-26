# Реалізувати рекурсивний прохід по дереву дирекорій.
# І потрібно вивести всі папки і файли які зберігаються в середині.
from pathlib import Path
import sys

p = Path(sys.argv[1])

# def parse_folder(path: Path):
#     for el in path.iterdir():
#         if el.is_dir():
#             print(f'Parse_folder: This is folder - {el.name}')
#         else:
#             print(f'Parse_folder: This is file - {el.name}')


def parse_folder_recursion(path: Path):
    for element in path.iterdir():
        if element.is_dir():
            print(f'Parse_folder: This is folder - {element.name}')
            parse_folder_recursion(element)
        else:
            print(f'Parse_folder: This is file - {element.name}')


if __name__ == "__main__":
    parse_folder_recursion(p)


