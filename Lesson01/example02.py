ss = int(input("Введите колличество секунд"))
ss = ss % (24 * 3600)
hh = ss // 3600
ss %= 3600
mm = ss // 60
ss %= 60
print(f"{hh}:{mm}:{ss}")



