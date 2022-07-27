
from re import I
import sys
sys.stdin = open("7568.txt", "r")

N=int(input())

a=[]
b=''
for i in range(1,N+1):
    x,y=map(int,(input()).split())
    a= round(x+y/2,-1)#키와 몸무게 평균 일자리까지 반올림
    if a[0] ==150.0:
        b=2
    elif a[1] ==150.0:
        b=2
    elif a[2] ==180.0:
        b=1
    elif a[3] ==150.0:
        b=2
    elif a[4] ==120.0:
        b=3

        #딕셔너리 