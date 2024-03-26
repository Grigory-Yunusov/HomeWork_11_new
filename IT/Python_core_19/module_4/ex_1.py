# У нас є строка: a = "lsj94ks6d231* !9#".
# Потрібно створити список в якому будуть тільки цифри
a = "lsj94k4s6d231* !9#"
result_list = []
for el in a:
    if '0' <= el <= '9':
        result_list.append(el)

print(result_list)
result_tuple = tuple(result_list)
print(result_tuple)
result_dict = {}
for element in result_list:
    result_dict[element] = int(element)
print(result_dict)
result_set = set(result_list)
print(result_set)