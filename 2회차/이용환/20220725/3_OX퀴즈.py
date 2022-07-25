# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")
T = int(input())
for i in range(T):
    Text = input()
    result = 0
    cnt = 0
    for j in Text:
        if j == 'O':
            cnt += 1
            result += cnt
        else:
            cnt = 0
    print(result)