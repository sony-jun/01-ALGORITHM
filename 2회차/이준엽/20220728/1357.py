x, y = map(int,input().split())

xrev = int(str(x)[::-1])
yrev = int(str(y)[::-1])
result = int(str(xrev+yrev)[::-1])
print(result)