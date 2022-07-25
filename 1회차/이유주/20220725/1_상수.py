# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

A, B = input().split()
rev_A = int(str(A)[::-1])
rev_B = int(str(B)[::-1])
if rev_A > rev_B:
    print(rev_A)
else: 
    print(rev_B)