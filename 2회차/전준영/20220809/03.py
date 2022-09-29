import sys
input=sys.stdin.readline
N=int(input())
M=int(input())
arr=[[] for _ in range(N+1)]
array=[]
for _ in range(M):
    a,b=map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
answer=[0]*(N+1)
answer[1]=1
que=[]
for i in arr[1]:
    que.append(i)
cnt=0
while len(que):
    m=que.pop(0)
    if(answer[m]==0):
        cnt+=1
        answer[m]=1
        for k in arr[m]:
            que.append(k)
print(cnt)
