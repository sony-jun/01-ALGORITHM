import sys
input=sys.stdin.readline
line=list(map(int,input().split()))
metrix=[list(map(int,input().split())) for _ in range(line[0])]
input0=int(input())
answer=[]
temp=[[0]*line[1] for __ in range(line[0])]
cnt=0
for i in metrix:
    cnt0=0
    for k in i:
        if(cnt0>0):
            temp[cnt][cnt0]=temp[cnt][cnt0-1]+k
        else:
            temp[cnt][cnt0]=k
        cnt0+=1
    cnt+=1
for __ in range(input0):
    temp1=list(map(int,input().split()))
    temp2=0
    for k0 in range(temp1[0]-1,temp1[2]):
        temp2+=temp[k0][temp1[3]-1]
        temp2-=temp[k0][temp1[1]-1]
        temp2+=metrix[k0][temp1[1]-1]
    answer.append(temp2)
for an in answer:
    print(an)
print(temp)
#import sys
#input=sys.stdin.readline
#line=list(map(int,input().split()))
#metrix=[list(map(int,input().split())) for _ in range(line[0])]
#input0=int(input())
#answer=[0]*input0
#for i in range(input0):
#    temp=list(map(int,input().split()))
#    for k in range(temp[0]-1,temp[2]):
#        for j in range(temp[1]-1,temp[3]):
#            answer[i]+=metrix[k][j]
#for an in answer:
#    print(an)