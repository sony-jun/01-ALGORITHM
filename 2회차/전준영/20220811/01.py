import sys
from collections import deque
input=sys.stdin.readline
vector=[[1,0],[0,1],[-1,0],[0,-1]]
M,N=map(int,input().split())
vecidx=0
idx=[0,0]
arr=[]
answer=0
for i in range(N):
    arr.clear()
    arr=input().split()
    arr[1]=arr[1]
    arr[1]=int(arr[1])
    if(arr[0]=="MOVE"):
        idx[0]+=vector[vecidx][0]*arr[1]
        idx[1]+=vector[vecidx][1]*arr[1]
    elif(arr[0]=="TURN"):
        if(arr[1]==0):
            vecidx+=1
            vecidx=vecidx%4
        else:
            vecidx-=1
            vecidx=vecidx%4
    if(idx[0]>M or idx[1]>M or idx[0]<0 or idx[1]<0):
        answer=-1
if(answer==-1):
    print(answer)
else:
    print(idx[0],idx[1])