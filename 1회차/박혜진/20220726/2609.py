# 풀이 1
a, b = map(int, input().split())

def gcd(a, b) :
    while b != 0 :
        a, b = b, a % b
    
    return a

def lcm(a, b) :
    
    return a * b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))

# 풀이 2
import math

print(math.gcd(a, b)) # 최대공약수
print(math.lcm(a, b)) # 최소공배수