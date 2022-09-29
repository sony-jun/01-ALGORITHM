# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")


a,b = map(str,sys.stdin.readline().split())

a = a[::-1]
b = b[::-1]
a = int(a)
b = int(b)

if a > b:
    print(a)
elif a < b:
    print(b)