# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")
a,b = input().split()
if a[::-1]>b[::-1]:
    print(a[::-1])
else:
    print(b[::-1])