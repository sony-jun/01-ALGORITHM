# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

A, B = input().split()
reversed_A = int(A[::-1])
reversed_B = int(B[::-1])
if reversed_A > reversed_B:
    print(reversed_A)
else:
    print(reversed_B)