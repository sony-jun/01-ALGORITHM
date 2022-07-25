# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

a, b = map(str, input().split())

new_a= int(a[::-1])
new_b= int(b[::-1])

print(max(new_a, new_b))