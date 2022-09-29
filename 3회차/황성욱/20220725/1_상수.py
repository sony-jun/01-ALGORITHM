# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

a, b = map(str,input().split())
a_re = a[::-1]
b_re = b[::-1]

if int(a_re) > int(b_re):
    print(a_re)
else:
    print(b_re)