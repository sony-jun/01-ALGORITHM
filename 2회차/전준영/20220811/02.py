import sys
input=sys.stdin.readline
N,M=map(int,input().split())
metrix=[list(map(int,input().split())) for _ in range(N)]
max=0
cnt=0
vector=[[1,0],[0,1],[-1,0],[0,-1]]
stack=[]
for i in range(N):
    for k in range(M):
        if(metrix[i][k]):#그림을 발견함
            cnt+=1
            cnt0=1
            stack=[[i,k]]
            metrix[i][k]=0
            while stack:
                temp=stack.pop()
                for j in range(len(vector)):#전후좌우로 탐색
                    temp1=[]
                    temp1.append(temp[0]+vector[j][0])
                    temp1.append(temp[1]+vector[j][1])
                    if(0<=temp1[0]<N and 0<=temp1[1]<M and metrix[temp1[0]][temp1[1]]==1):
                        stack.append(temp1)
                        metrix[temp1[0]][temp1[1]]=0
                        cnt0+=1
            if(cnt0>max):
                max=cnt0
print(cnt)
print(max)
            