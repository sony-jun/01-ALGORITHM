# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

a, b = input().split()

a_rev = int(a[::-1])
b_rev = int(b[::-1])

if a_rev > b_rev:
    print(a_rev)
if a_rev < b_rev:
    print(b_rev)