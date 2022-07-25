# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")
n = int(input())
for _ in range(n):
    s = input()
    sum_val = 0
    cnt = 0
    for i in s:
        if i == 'O':
            cnt += 1
            sum_val += cnt
        else:
            cnt = 0
    print(sum_val)

