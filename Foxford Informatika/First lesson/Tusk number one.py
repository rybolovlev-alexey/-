num = int(input())
summa = 0
a = num % 10
b = num // 10 % 10
c = num // 100 % 10
summa = a + b + c
print(summa)
