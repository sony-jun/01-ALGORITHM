a, b = map(int, input().split())

c = 4 if a % 4 == 0 else a % 4
d = 4 if b % 4 == 0 else b % 4

e = a // 4 if a % 4 == 0 else a // 4 + 1
f = b // 4 if b % 4 == 0 else b // 4 + 1

if c == d:
    print(abs(e-f))
elif c > d:
    print(abs(e-f) + abs(c - d))
else:
    print(abs(e-f) + abs(d - c))