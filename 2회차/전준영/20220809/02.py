import sys
input=sys.stdin.readline
N,M=map(int,input().split())
vx=[0,0,1,1]
vy=[0,1,0,1]
arr=[]
answer=[0]*5
for _ in range(N):
    arr.append(input())
for i in range(N):
    for k in range(M):
        cnt=0
        bo=1
        if(arr[i][k]!='#'):
            if(i+1<N and k+1<M):
                for j in range(4):
                    if(arr[i+vx[j]][k+vy[j]]=='#'):
                        bo=0
                    elif(arr[i+vx[j]][k+vy[j]]=='X'):
                        cnt+=1
                if(bo==1):
                    answer[cnt]+=1
for a in answer:
    print(a)