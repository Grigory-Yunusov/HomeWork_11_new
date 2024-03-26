# В Інтернет-магазині зроблено 4 покупки: на $34.34, $12.01, $17.42, $4.93.
# Зі скількох доларів і центів складатиметься підсумкова сума.
price1 = 34.34
price2 = 12.01
price3 = 17.42
price4 = 4.93

cost = price1 + price2 + price3 + price4
dollar = int(cost)
# cent = float(cost - dollar)
cent = int((cost - int(cost)) * 100)
print(f'Sum: {cost}')
print(f'Dollar: {dollar}')
print(f'Cent: {cent}')
