# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

a, b= input().split()

print(max(int(a[::-1]), int(b[::-1])))