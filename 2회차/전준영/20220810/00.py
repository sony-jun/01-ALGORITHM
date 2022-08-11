import sys
input=sys.stdin.readline
N,M=map(int,input().split())
array=[[] for _ in range(N+1)]
answer=[0]*(N+1)
for _ in range(M):
    a,b=map(int,input().split())
    array[a].append([a,b])
    array[b].append([b,a])
stack=[]
cnt=0
bo=1
while bo:
    bo=0
    for i in range(1,len(answer)):
        if(answer[i]==0):
            bo=1
            cnt+=1
            stack.append(array[i])
            answer[i]=cnt
            break
    while stack:
        temp=stack.pop()
        for i in temp:
            if(answer[i[0]]!=0 and answer[i[1]]==0):
                answer[i[1]]=answer[i[0]]
                stack.append(array[i[1]])
print(cnt)