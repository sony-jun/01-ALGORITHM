# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

# 세 개의 자연수 A, B, C
# A * B * C 에서 0 - 9 까지의 숫자가 각각 몇 번씩 쓰였는가

A = int(input())
B = int(input())
C = int(input())

ABC = A * B * C

# ABC를 문자열로 바꿈
str_ABC = str(ABC)

# 0 - 9까지의 각 값을 순회하기 위함
for i in range(10):
    print(str_ABC.count(str(i)))