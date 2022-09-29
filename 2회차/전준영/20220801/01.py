import sys
input=sys.stdin.readline
temp0=list(map(int,input().split()))
N=temp0[0]
M=temp0[1]
array0=[]
for i in range(M):
    n=int(input())
    array0.append(list(map(int,input().split())))
cnt=1
for j in array0:
    temp=0
    for k in j[::-1]:
        if(k<temp):
            cnt=0
        temp=k
if(cnt==0):
    print("No")
else:
    print("Yes")
