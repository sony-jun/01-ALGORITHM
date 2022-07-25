# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

t = int(input())

for i in range(t):
    s = list(input())
    cnt = 0
    result = 0
    for j in s:
        if j == 'O':
            cnt += 1
            result += cnt
        else:
            cnt = 0
    print(result)
