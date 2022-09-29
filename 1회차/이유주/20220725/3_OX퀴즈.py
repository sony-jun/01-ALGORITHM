# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

T = int(input())
for x in range(T):
    n = input()
    score = 0
    count = 0
    for i in n:
        if i == 'O':
            count += 1
        else:
            count = 0
        score += count
    print(score)