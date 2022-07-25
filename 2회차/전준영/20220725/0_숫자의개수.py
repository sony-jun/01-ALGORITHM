# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open(r"2회차\전준영\20220725\0_숫자의개수.txt",'r',encoding='utf-8')
int_array=[0,0,0,0,0,0,0,0,0,0]
result=1
for i in sys.stdin:
    result*=int(i)
while(result):
    int_array[result%10]+=1
    result=result//10
for k in range(10):
    print(int_array[k])