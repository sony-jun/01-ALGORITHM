# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")
T=int(input())

for t in range(T):
    inputstr = input()

   
    result=0
    o_cnt=0

    for i in inputstr:
    
        if i == 'O':
            result = result+1+o_cnt
            o_cnt+=1
        else:
            o_cnt=0
           
    print(result)