a = int(input("Введите количество киллометров"))
b = int(input("Цель (в км)"))
day = 1
while a < b:
    a = a + (a / 10)
    day += 1
print("На", day, "Вы достигнете цели")
