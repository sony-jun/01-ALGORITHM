# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")


T = int(input())
for i in range(1, T+1) :
    a, b = list(input().split())
    a = a[::-1]
    b = b[::-1]
    print(max(a, b))
