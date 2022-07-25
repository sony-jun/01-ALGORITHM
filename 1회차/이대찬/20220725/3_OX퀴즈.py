# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

case = input() 
result = []
for i in sys.stdin:
    sum  = 0
    tmp =0
    t = 0
    for n in i:
        if n == 'O':
            t +=1
            tmp += t
        else:
            sum += tmp
            tmp = 0
            t = 0
    result.append(sum)

for i in result:
    print(i)
 
        
            
        
 