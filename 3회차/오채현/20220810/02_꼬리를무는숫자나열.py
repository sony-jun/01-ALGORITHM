a, b = map(int, input().split())

w = 0
h = 0

a = a - 1
b = b - 1

w = abs((a // 4) - (b // 4))
h = abs((a % 4) - (b % 4))

print(w + h)
