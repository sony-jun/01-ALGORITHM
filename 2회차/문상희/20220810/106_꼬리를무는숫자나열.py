a, b = map(int, input().split())
a -= 1
b -= 1
line = abs(a//4 - b//4)
stripe = abs(a%4 - b%4)
cnt = line + stripe
print(cnt)