# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

T = int(input()) 

for n in range(1,T+1):
    answer = input() #O.X만 존재
    score = 0
    result = 0
    for c in answer:
        if c == 'O':
            score += 1
            result +=score
        else:
            score = 0
    print(result)