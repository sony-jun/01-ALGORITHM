# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

n = int(input())

for i in range(n):
    cnt = 0
    score_lst = []
    text_lst = input()
    for text in text_lst:
        if text == 'O':
            cnt += 1
            score_lst.append(cnt)
        else:
            cnt = 0
    print(sum(score_lst))