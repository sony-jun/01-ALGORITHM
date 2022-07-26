
import sys
sys.stdin = open("27_최대공약수와최소공배수.txt", "r")

a, b = map(int, input().split())

# #a, b 중에 큰 수와 작은 수를 구분
# if a >= b:
#     large = a
#     small = b
# else:
#     laege = b
#     small = a

# #큰 수를 range(2, 작은 수)로 반복하며 나누어 떨어지는 수가 공약수
# result = []

# for num in range(2, small + 1):
#     if large % num == 0 and small % num == 0:
#         result.append(num)

# #그 중에 가장 큰 것이 최대공약수
# gcd_ = max(result)
# print(gcd_)


## 유클리드 호제법: 최대 공약수 풀이2
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

gcd_ = gcd(a, b)
print(gcd_)


#최소공배수는 a * b / 최대 공약수
lcm = a * b // gcd_
print(lcm)