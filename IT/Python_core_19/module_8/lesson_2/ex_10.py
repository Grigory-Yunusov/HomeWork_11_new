"""
defaultdict: Зручно, якщо ми розбиваємо на різні списки набори телефонних операторів
"""

from collections import defaultdict

phone_numbers = ['0509993636', '0679993636', '0959993636', '0969993636', '0509993637', '0639993636', '0509993632',
                 '0339993632']

phone_operator_numbers = defaultdict(list)
for phone in phone_numbers:
    if phone.startswith('050') or phone.startswith('095'):
        phone_operator_numbers['Vodafone'].append(phone)
    elif phone.startswith('067') or phone.startswith('096'):
        phone_operator_numbers['Kyivstar'].append(phone)
    elif phone.startswith('063') or phone.startswith('093'):
        phone_operator_numbers['Lifeceil'].append(phone)
    else:
        phone_operator_numbers['Unknown'].append(phone)
print(phone_operator_numbers)
