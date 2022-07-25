# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

a, b =input().split()
a = a[::-1]
b = b[::-1]
if a > b:
    print(a)
else:
    print(b)


