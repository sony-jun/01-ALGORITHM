# 문제 : 두 수의 최대공약수, 최소공배수 구하기
# 공약수란, 두 수 사이의 공통으로 존재하는 약수 💡
# 공배수란, 두 수의 공통적인 배수 💡

import math

a, b = map(int, input().split())

print(math.gcd(a, b))  # 최대공약수
print(math.lcm(a, b))  # 최소공배수
