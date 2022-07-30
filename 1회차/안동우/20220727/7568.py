
import sys
sys.stdin = open("7568.txt", "r")

N=int(input())
a=""
b=[]

for i in range(1,N+1):
    x,y=map(int,(input()).split())
    a=str(round(x+y/2,-1))#키와 몸무게 평균 일자리까지 반올림
    # A,B,C,D,F=map(int,(input()).split())
    print(a)
    
