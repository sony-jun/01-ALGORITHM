# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

T = int(input())

for i in range(1, T + 1):
    OX_List = list(input())
    score = 0
    total = 0

    for i in OX_List:
        if i == 'O':
            score += 1
        else:
            score = 0
        total += score
    print(total)
