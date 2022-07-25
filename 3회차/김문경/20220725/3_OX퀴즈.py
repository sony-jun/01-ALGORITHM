# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

T = int(input())
for case in range(1, T + 1):
    word = input()
    cnt = 0
    result = 0
    for i in word:
        cnt += 1
        if i == 'O':
            result += cnt
        else:
            cnt = 0
    print(result)