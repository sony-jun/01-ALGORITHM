X, Y = map(int, input().split())

x = int(str(X)[::-1])
y = int(str(Y)[::-1])

print(int(str(x + y)[::-1]))