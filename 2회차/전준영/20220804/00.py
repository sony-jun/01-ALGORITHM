import sys
input=sys.stdin.readline
N=int(input())
metrix=[input() for _ in range(N)]
cnt0=0
cnt1=0
array=[0]*len(metrix[0])
for i in metrix:
    temp=0
    column=0
    for k in i:
        if(k=='.'):
            if(temp>-1):
                temp+=1
                if(temp>1):
                    cnt0+=1
                    temp=-1
            if(array[column]>-1):
                array[column]+=1
                if(array[column]>1):
                    cnt1+=1
                    array[column]=-1
        else:
            temp=0
            array[column]=0
        column+=1
print(cnt0,cnt1)
