import sys
input=sys.stdin.readline
def fun(array,i,k,M,N):
    stack=[]
    vec=[[0,1],[1,0],[-1,0],[0,-1],[1,1],[-1,1],[-1,-1],[1,-1]]
    stack.append([i,k])
    while stack:
        temp=stack.pop()
        for i in range(8):
            if(0<=temp[0]+vec[i][0]<M and 0<=temp[1]+vec[i][1]<N and array[temp[0]+vec[i][0]][temp[1]+vec[i][1]]==1):
                stack.append([temp[0]+vec[i][0],temp[1]+vec[i][1]])
                array[temp[0]+vec[i][0]][temp[1]+vec[i][1]]=0
    return 1
M=1
N=1
answer=[]
M,N=map(int,input().split())
while M!=0 and N!=0:
    array=[]
    cnt=0
    for i in range(N):
        array.append(list(map(int,input().split())))
    for i in range(N):
        for k in range(M):
            if(array[i][k]==1):
                fun(array,i,k,N,M)
                cnt+=1
    answer.append(cnt)
    M,N=map(int,input().split())
for i in answer:
    print(i)