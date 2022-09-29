# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

T = int(input())

for i in range(1,T+1):
    result = list(input())
    score=0
    sum_score=0
    for ox in result:
        if ox == 'O':
            score+=1
            sum_score+=score
        else:
            score = 0
    print(sum_score)