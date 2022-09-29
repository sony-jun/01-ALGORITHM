# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("20220725/1_상수.txt")

A, B = input().split()

re_A = A[::-1]
re_B = B[::-1]

if int(re_A) > int(re_B):
    print(re_A)
else:
    print(re_B)