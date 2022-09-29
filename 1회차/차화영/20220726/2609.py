# https://www.acmicpc.net/problem/2609
import sys

sys.stdin = open("2609.txt")
a, b = map(int, input().split())

# 유클리드 호제법
# gcd(최대공약수), lcm(최소공배수)
# gcd(a, b) = gcd(b, a % b)
# 만일 a % b가 0이면 gcd는 b이다.
# 그렇지 않으면 gcd(b, a% b)

# 최대공약수
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
# 최소공배수
def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))