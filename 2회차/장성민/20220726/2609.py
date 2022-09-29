a, b = map(int, input().split())

# 최대공약수 -> 유클리드 호제법
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

# 최소공배수 -> a와 b의 곱을 a와 b의 최대 공약수로 나눈 것
def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))