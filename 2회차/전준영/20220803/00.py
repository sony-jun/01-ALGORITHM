import sys
input=sys.stdin.readline
line=list(map(int,input().split()))
array=[input() for _ in range(line[0])]
temp=[0]*line[1]
cnt=0
for i in array:
    bo=0
    cnt0=0
    for k in i:
        if(k=='X'and bo==0):
            cnt+=1
            bo=1
            temp[cnt0]=1
        elif(k=='X'):
            temp[cnt0]=1
        cnt0+=1
cnt0=0
for j in temp:
    if(j==1):
        cnt0+=1
answer=max(line[0]-cnt,line[1]-cnt0)
print(answer)

