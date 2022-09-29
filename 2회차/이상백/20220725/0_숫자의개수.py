# https://www.acmicpc.net/problem/2577
# import sys

# sys.stdin = open("0_숫자의개수.txt", "r")

A = int(input())
B = int(input())
C = int(input())

result = list(str(A * B * C))

for mul in range(0, 10):
    print(result.count(str(mul)))
# 숫자 하나당 0부터9까지 돌면서 겹치는 수가 있으면 해당 수에 카운트