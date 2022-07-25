# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")
num1 = int(input())
num2 = int(input())
num3 = int(input())
# 각자리별숫자를 문자취급하고 리스토로 나열하였다.
num = list(str(num1*num2*num3))
# 0~9까지 각각 세서 나오게 한다.
for i in range(10):
    print(num.count(str(i)))
print(num)

