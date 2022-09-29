# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

A = int(input())
B = int(input())
C = int(input())

Moa = list(str(A * B * C)) #(['1', '7', '0', '3', '7', '3', '0', '0'])
for i in range(0, 10):
    print(Moa.count(str(i)))
