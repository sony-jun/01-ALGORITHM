# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")
# cnt=+1을 반복문에 넣고 x가 나오면 리셋되게 하자, 
T=int(input())

for i in range(T):
    problem=input()
    score=0
    cnt=0
    for p in problem:
        if p=='O':
            cnt+=1
            score+=cnt
        else: cnt=0
    print(score)       
            
