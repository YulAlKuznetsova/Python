revenue = int(input("Введите сумму выручки"))
costs = int(input("Введите сумму издержек"))
if revenue > costs:
    profit = revenue - costs
    print("Фирма работает в прибыль")
    profitability = profit / revenue
    print("Рентабельность фирмы =", profitability)
    quantity = int(input("Введите количесвто сотрудников"))
    profit1 = profit / quantity
    print("Прибыль на одного сотрудника =", profit1)
else:
    print("Фирма работает в убыток")
