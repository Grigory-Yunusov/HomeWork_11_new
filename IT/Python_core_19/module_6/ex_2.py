"""
Добавити запис в існуючий файл
"""

file = open('test.txt', 'r', encoding='utf-8')
file.write('Happy!!!')
file.close()
