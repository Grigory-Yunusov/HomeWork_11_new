# У банк поклали 100 доларів під 5 % річних.
# Скласти програму обчислення кількості грошей на рахунку через 10 років. (складні щомісячні відсотки)

deposit = 100
percent = 0.05
T = 10

for year in range(1, T + 1):
    new_deposit = deposit * (1 + percent / 12) ** 12
    deposit = new_deposit
print(deposit)
# 164.700949769028
# 164.700949769028
# print(deposit * (1 + percent / 12) ** (12 * 10))
