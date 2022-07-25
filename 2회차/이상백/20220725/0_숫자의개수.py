# https://www.acmicpc.net/problem/2577
# import sys

# sys.stdin = open("0_숫자의개수.txt", "r")

A = int(input())
B = int(input())
C = int(input())

result = list(str(A * B * C))

for mul in range(0, 10):
    print(result.count(str(mul)))