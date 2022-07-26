# 유클리드 호제법 - 반복문
a, b = map(int, input().split())

def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x

def lcm(x,y):
    return x * y // (gcd(x, y))

print(gcd(a, b), lcm(a, b))