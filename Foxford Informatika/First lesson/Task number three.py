x = int(input())
ans = 1
a = x // 1000
b = x // 100 % 10
c = x // 10 % 10
ans = a * b * c 
print(ans)
