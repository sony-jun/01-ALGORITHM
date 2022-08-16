import sys
from copy import deepcopy
from collections import deque
input=sys.stdin.readline
class coordinate:
    def __init__(self,idx):
        self.idx=deepcopy(idx)
        self.cnt=1
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
queue=deque()
min=M*N
cnt=1
temp2=[0,0]
queue.append(coordinate([0,0]))
cnt=1
visited=[[False]*M for _ in range(N)]
visited[0][0]=True
t=0
while t!=1:
    temp=queue.popleft()
    for i in vector:
        temp1=deepcopy(temp)
        temp2[0]=temp1.idx[0]+i[0]
        temp2[1]=temp1.idx[1]+i[1]
        if(0<=temp2[0]<N and 0<=temp2[1]<M and arr[temp2[0]][temp2[1]] and not visited[temp2[0]][temp2[1]]):
            if(temp2[0]==N-1 and temp2[1]==M-1):
                t=1
                min=temp1.cnt+1
                break
            else:
                temp1.idx[0]=temp2[0]
                temp1.idx[1]=temp2[1]
                temp1.cnt+=1
                visited[temp2[0]][temp2[1]]=True
                queue.append(temp1)
print(min)
