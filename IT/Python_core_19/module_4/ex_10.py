# Знайти індекс колонки для excel таблиці
from string import ascii_uppercase


def find_column_index(column_name: str) -> int:
    """
    >>> find_column_index('AA')
    27
    >>> find_column_index('ABA')
    729
    >>> find_column_index('AAA')
    703
    """
    letter_map = {}
    for index, letter in enumerate(ascii_uppercase, 1):
        letter_map[letter] = index  # {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
    if len(column_name) > 1:
        sum = 0
        reverse_column_name = column_name[::-1]
        for index, letter in enumerate(reverse_column_name):
            sum += 26 ** index * letter_map[letter]
        return sum
    return letter_map.get(column_name)

print(find_column_index('AAA'))
