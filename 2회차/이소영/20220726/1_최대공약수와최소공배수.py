# 최대공약수GCD는 두 수의 곱을 최소공배수LCM로 나눈 값 // 과 같다

# # 1. 하나씩 나눠서 리스트에 넣으려다 실패
# A, B = map(int, input().split())
# n = 2
# m = 2
# list1 = []
# list2 = []

# # 두 수를 나눠서 나머지가 0인 몫 n, m을 리스트에 넣는다

# while A >= n and B >= n:
#     if A % n == 0 and B % n == 0:
#         list1.append(n)
#     else:
#         n += 1

#  while A >= m and B >= m:
#     if A / n % m == 0 and B / n % m == 0:
#         list2.append(m)
#     else:
#         m += 1

# n * m * list2[0] * list2[1] 가 최소공배수, list[1] 가 최대공약수?


# 2. gcd, lcm 함수
a, b = map(int, input().split())

# 최대공약수 gcd 구하기
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

# 최소공배수 lcm 구하기 
def lcm(a, b):
    for i in range(max(a, b), (a * b) + 1):
        if i % a == 0 and i % b == 0:
            return i

print(gcd(a, b))
print(lcm(a, b))


# 3. 파이썬 내장 함수 (라이브러리)
# import math

# a, b = map(int, input().split())

# print(math.gcd(a, b))
# print(math.lcm(a, b))