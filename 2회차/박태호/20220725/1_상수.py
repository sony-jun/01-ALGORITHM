# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

a, b = map(int, input().split())

new_a = str(a)[::-1] #437
new_b = str(b)[::-1] #398

if new_a > new_b:
    print(new_a)

else:
    print(new_b)