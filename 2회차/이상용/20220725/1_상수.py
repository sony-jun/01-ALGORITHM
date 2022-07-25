# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")
l = sys.stdin.readline()

# 입력된 숫자를 뒤집고
num1 = l[0:3][::-1]
num2 = l[4:7][::-1]

# 뒤집은 두 수를 비교 하여 큰 수를 출력하기
print(max(num1, num2))

# 일반적인 입력으로 진행할 떄 ver
# a, b = input().split()
# a = int(a[::-1])
# b = int(b[::-1])
# if a > b:
#   print(a)
# else:
#   print(b)

# 완전 간소화 ver
# a, b = input().split()
# print(max(a[::-1], b[::-1]))