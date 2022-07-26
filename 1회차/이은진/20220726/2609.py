A, B = map(int, input().split())
for i in range(min(A, B), 0, -1):
    if (A % i == 0) and (B % i == 0):
        gcd = i
        break
lcd = (A * B) // gcd
print(gcd)
print(lcd)