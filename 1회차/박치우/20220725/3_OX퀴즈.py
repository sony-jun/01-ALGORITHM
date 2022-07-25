# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")


n = int(input())
for i in range(n):
    quiz = input()
    score = 0
    s_score = 0
    for j in quiz:
        if j == 'O':
            s_score +=1
            score += s_score
        else :
            s_score = 0
    print(score)
    

            