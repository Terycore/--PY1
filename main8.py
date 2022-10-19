money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
proc = 0
ras = 0
dox = 0
month = 0

# TODO Оформить решение
while money_capital >= spend:
    dox += salary
    ras = ras + spend + proc
    proc = ras * increase
    money_capital = money_capital + dox - ras
    month = month + 1

print(month)
