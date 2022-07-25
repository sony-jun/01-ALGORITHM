# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("20220725/0_숫자의개수.txt")

A = int(input())
B = int(input())
C = int(input())

result = str(A * B * C)

for i in range(10):
    print(result.count(str(i)))