salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
proc = 0
need_money = 0  # количество денег, чтобы прожить 10 месяцев
ras = 0
dox = 0

# TODO Оформить решение
for month in range(0, 10):
    dox += salary
    ras = ras + spend + proc
    proc = ras * increase

need_money = ras-dox
print(round(need_money))
