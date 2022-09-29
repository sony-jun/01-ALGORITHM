# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")
T = int(input())
for i in range(T):
    score = 0
    case = input()
    in_a_row = 0
    for i in case:
        if i == 'O':
            in_a_row += 1
            score += in_a_row
        else:
            in_a_row = 0
    print(score)