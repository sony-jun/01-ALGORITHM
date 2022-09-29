a, b, c = map(int, input().split())

if a == b == c:
    result = 10000 + a * 1000
elif a == b:
    result = 1000 + a * 100
elif b == c:
    result = 1000 + b * 100
elif c == a:
    result = 1000 + c * 100
else:
    result = 100 * max(a, b, c)

print(result)