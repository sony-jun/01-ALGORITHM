# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

T = int(input())

for i in range(1, T + 1):
    OX_List = list(input())
    score = 0 #초기화
    total = 0

    for i in OX_List:
        if i == 'O':
            score += 1 #O일 경우 점수 1씩 증가시킴
        else:
            score = 0 #X일 경우 0으로 초기화
        total += score #최종 결과 합 total에 넘기고 다음 입력으로 넘어감
    print(total)
