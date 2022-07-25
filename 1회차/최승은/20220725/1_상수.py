# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")
a, b = input().split()

c = a[::-1]
d = b[::-1]

if c > d:
    print(c)
else:
    print(d)
