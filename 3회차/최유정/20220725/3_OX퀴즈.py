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
            result = result+1+o_cnt  #o_count +=1 연속된 0의 개수 1증가
            o_cnt+=1 #result=o_count + result로 하면 1안더해도됨
        else:
            o_cnt=0
           
    print(result)