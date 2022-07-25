# https://www.acmicpc.net/problem/2577
from re import T
import sys

sys.stdin = open("0_숫자의개수.txt")

a,b,c = map(int,sys.stdin)

t = a*b*c
result = {}
for i in range(0,10):
    result[str(i)] = 0
    
for i in str(t):
    if i in result:
         result[i] = result[i] + 1
     
for i in result:
    print(result[i])





