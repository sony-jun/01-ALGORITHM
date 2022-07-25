# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

t = int(input())
for test_case in range(1, t+1):
    l = list(input()) #입력된 값을 리스트로 만들기
    score = 0 #점수
    reset = 0 #O면 1씩 플러스하면서 점수에 추가하고 x면 0으로 초기화 시키는 값
    for r in l:
        if r == 'O': #O일 경우에
            reset += 1 #계속 1씩 추가하고
            score += reset #score에 더하기
        else:
            reset = 0 #X일 경우에 0으로
    print(score)