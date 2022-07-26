import math

a, b = map(int, input().split())

print(math.gcd(a, b))
print(math.lcm(a, b))

def gcd_1(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm_1(a, b):
    return a * b // gcd_1(a, b)

print("유클리드호제법 GCM:",gcd_1(a,b))
print("유클리드호제법 LCM:",lcm_1(a,b))