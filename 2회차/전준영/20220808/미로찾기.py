import sys
from collections import deque
input=sys.stdin.readline
class coordinate:
    def __init__(self,idx,arr,N,M,cnt):
        self.idx=[]
        self.idx.append(idx[0])
        self.idx.append(idx[1])
        self.arr=[]
        for i in arr:
            ar0=[]
            for k in i:
                ar0.append(k)
            self.arr.append(ar0)
        self.cnt=cnt
vector=[[1,0],[0,1],[-1,0],[0,-1]]
N,M=map(int,input().split())
arr=[]
for _ in range(N):
    tt=input()
    ttt=[]
    for i in tt:
        if(i!='\n'):
            ttt.append(int(i))
    arr.append(ttt)
stack=[]
stack.append(coordinate([0,0],arr,N,M,1))
temp1=[]
t=0
cnt=0
min=M*N
while stack:
    temp=stack.pop()
    temp.arr[temp.idx[0]][temp.idx[1]]=0
    bo=0
    for i in vector:
        temp1.clear()
        temp1.append(temp.idx[0]+i[0])
        temp1.append(temp.idx[1]+i[1])
        if(0<=temp1[0]<N and 0<=temp1[1]<M and temp.arr[temp1[0]][temp1[1]]==1):
            temp.cnt+=1
            if(temp1[0]==N-1 and temp1[1]==M-1):
                if(min>temp.cnt):
                    min=temp.cnt
            else:
                stack.append(coordinate(temp1,temp.arr,N,M,temp.cnt))
            bo+=1
print(min)
