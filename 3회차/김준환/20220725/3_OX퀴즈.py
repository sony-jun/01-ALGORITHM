# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

n = int(input())

for i in range(n):                   # n번 반복
    cnt = 0
    score_lst = []                   # 점수 기록 리스트
    text_lst = input()               # 입력 
    for text in text_lst:
        if text == 'O':
            cnt += 1
            score_lst.append(cnt)
        else:
            cnt = 0
    print(sum(score_lst))