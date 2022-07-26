# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")


T = int(input())
for i in range(T):
    answer = input().split('X')
    score = 0
    for j in range(len(answer)):
        cnt = 1
        for k in range(len(answer[j])):
            score += cnt
            cnt += 1
    print(score)