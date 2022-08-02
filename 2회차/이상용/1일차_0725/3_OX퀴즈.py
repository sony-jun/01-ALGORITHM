# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

T = int(input())
for i in range(T):
    a = input()
    score = 0
    sumScore = 0
    for j in a:
        if j == 'O':
            score += 1 # 연속된 0의 개수 증가
        else:
            score = 0 # 연속된 0의 개수 초기화
        sumScore += score
    print(sumScore)