# https://www.acmicpc.net/problem/8958
import sys

import sys
sys.stdin = open(r"2회차\전준영\20220725\3_OX퀴즈.txt",'r',encoding='utf-8')
score=0
temp=0
size=sys.stdin.readline()
for i in sys.stdin:
    score=0
    for k in i:
        if(k=='O'):
            temp+=1
            score+=temp
        else:
            temp=0
    print(score)
