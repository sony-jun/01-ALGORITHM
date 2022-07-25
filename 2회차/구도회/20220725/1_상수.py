# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

a,b = input().split()

if int(a[3::-1]) < int(b[3::-1]):
    print(b[3::-1])
else:
    print(a[3::-1])