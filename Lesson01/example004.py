n = int(input("Введите положительное число"))
ext = -1
while n > 10:
    l = n % 10
    n //=  10
    if l > ext:
        ext = l
print(ext)