# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

A, B = map(str, input().split())


SA = A[::-1]
SB = B[::-1]

if SA > SB:
    print(SA)
else:
    print(SB)
