# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("00_숫자의개수.txt", "r")

A = int(input())
B = int(input())
C = int(input())

mult = str(A * B * C)
for i in range(10):
    print(mult.count(str(i)))