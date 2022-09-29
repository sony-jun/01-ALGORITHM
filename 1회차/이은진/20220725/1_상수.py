# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

a, b = input().split()
re_a, re_b = int(a[::-1]), int(b[::-1])
if re_a > re_b:
    print(re_a)
else:
    print(re_b)