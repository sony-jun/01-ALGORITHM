# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

A=int(input())
B=int(input())
C=int(input())

result = list(str(A * B * C)) # 곱한 값을 문자열로 바꾼 뒤 list의 요소로 넣는다

for i in range(10):
    print(result.count(str(i))) 