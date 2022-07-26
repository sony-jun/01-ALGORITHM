# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

T = int(input()) #문자를 받는다 

for n in range(1,T+1): #문자의 길이만큼 만복하도록 
    answer = input() #O.X만 존재
    score = 0
    result = 0
    for c in answer: #문자열
        if c == 'O':
            score += 1
            result +=score
        else:
            score = 0
    
    print(result)