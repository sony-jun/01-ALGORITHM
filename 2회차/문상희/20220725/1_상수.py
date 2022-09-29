# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

A, B = map(str, input().split())
if int(A[::-1]) > int(B[::-1]):
    print(A[::-1])
else:
    print(B[::-1])
