import sys
input=sys.stdin.readline
N=int(input())
array=[list(map(int,input().split())) for _ in range(N)]
answer=[0]*N
temp0=[[0]*101 for __ in range(3)]
cnt=0
for i in array:
    cnt=0
    for k in i:
        temp0[cnt][k]+=1
        cnt+=1
cnt=0
cnt0=0
for j in array:
    cnt=0
    for l in j:
        if(temp0[cnt][l]==1):
            answer[cnt0]+=l
        cnt+=1
    cnt0+=1
for an in answer:
    print(an)
