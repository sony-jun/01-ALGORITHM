# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

A, B = input().split()
rA, rB = A[::-1], B[::-1]
if rA > rB:
    print(rA)
elif rA < rB:
    print(rB)