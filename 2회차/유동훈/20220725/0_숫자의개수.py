# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

A = int(input())
B = int(input())
C = int(input())

mul = list(str(A * B * C))

numbers = {}
for i in range(10):
    numbers[i] = 0
for j in mul:
    numbers[int(j)] += 1
for i in range(10):
    print(numbers[i])