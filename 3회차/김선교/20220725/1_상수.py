# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

a, b = input().split()
a = int(str(a)[::-1])
b = int(str(b)[::-1])
print(a if a > b else b)