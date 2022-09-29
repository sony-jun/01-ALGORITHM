# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

T = int(input())

for tt in range(T):
    count = 0
    score = 0
    str = input()
    for i in str:
        if i == 'O':
            count += 1
            score += count
        elif i == 'X':
            count = 0
    print(score)