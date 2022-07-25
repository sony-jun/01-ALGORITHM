# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

T = int(input())

for i in range(T):
    QUIZ = input()
    cnt = 0 
    total = 0
    for j in QUIZ:
        if j == 'O':
            cnt += 1
            total += cnt
        else:
            cnt = 0
    print(total)