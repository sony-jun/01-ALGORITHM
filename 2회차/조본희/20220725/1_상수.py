# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt", "r")

A, B = map(str, input().split())

A = A[::-1]
B = B[::-1]

if int(A) > int(B):
    print(A)
else:
    print(B)