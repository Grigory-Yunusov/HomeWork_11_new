"""
Метод: compile
Ми використаємо функцію compile щоб скомпілювати попередньо визначений патерн.
Потрібно, якщо використовуємо його часто в різних місцях програми.
"""

import re

string = "Нільс Бор народився в родині професора фізіології Копенгагенського університету Християна Бора (1858-1911), " \
         "й Еллен Адлер (1860--1930). Батьки Бора одружилися 1881 року. Батька Нільса Бора двічі висували кандидатом " \
         "на Нобелівську премію з фізіології або медицини[6]. Мати була донькою впливового та вельми заможного " \
         "єврейського банкіра і парламентаря-ліберала Давида Баруха Адлера[da] (1826--1878) і Дженні Рафаел (1830--1902) " \
         "із британської єврейської банкірської династії Raphael Raphael & sons."

# Знайти всі слова з великої літери
pattern = re.compile(r'[А-ЯA-Z]\w*')
result = pattern.findall(string)
print(result)

# Знайти всі слова
pattern = re.compile(r'\w+')
result = pattern.findall(string)
print(result)

# Знайти слово на початку строки
pattern = re.compile(r'^[А-ЯA-Z]\w*')
result = pattern.findall(string)
print(result)

# Знайти слово в кінці строки
pattern = re.compile(r'\w+\.$')
result = pattern.findall(string)
print(result)