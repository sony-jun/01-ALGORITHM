# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

t = int(input())

for tc in range(1, t + 1):
    ox = input()
    result = 0
    cnt = 1

    for i in ox:
        if i == 'O':
            result += cnt
            cnt += 1
        else:
            cnt = 1

    print(result)
