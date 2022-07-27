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
mi=1
ma=1
for i in range(1,10001):
    if a%i==0 and b%i==0:
        a//=i
        b//=i
        mi*=i
        ma*=i
        break
    
print(mi)
print(mi*a*b)