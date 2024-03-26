# Написати програму яку буде вираховувати вартість товару з врахуванням знижки

def real_cost(base, discount=0):
    return base * (1 - discount)


print(real_cost(15))
print(real_cost(100, 0.20))
print(real_cost(15, 0.05))