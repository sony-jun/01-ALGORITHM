import sys
input=sys.stdin.readline
answer=[]
N=int(input())
for i in range(N):
    temp=list(map(int,input().split()))
    if(temp[1]-temp[2]>temp[0]):
        answer.append("advertise")
    elif(temp[1]-temp[2]==temp[0]):
        answer.append("does not matter")
    else:
        answer.append("do not advertise")
for k in answer:
    print(k)