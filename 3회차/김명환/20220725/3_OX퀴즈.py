# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")
N = int(input())

for i in range(N):
    test_case = input()
    score = 0 
    total_score = 0
    for j in range(len(test_case)):
        if test_case[j]=='O':
            score +=1
            total_score += score
        else:
            score = 0
    print(total_score)
