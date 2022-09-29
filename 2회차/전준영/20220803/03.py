import sys
input=sys.stdin.readline
metrix=[input() for _ in range(8)]
cnt=0
answer=0
for i in metrix:
    cnt0=0
    for k in i:
        if(cnt%2==0):
            if(cnt0%2==0 and k=='F'):
                answer+=1
        else:
            if(cnt0%2==1 and k=='F'):
                answer+=1
        cnt0+=1
    cnt+=1
print(answer)