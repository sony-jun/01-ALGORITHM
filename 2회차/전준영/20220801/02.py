answer=[]
T=int(input())
for i in range(T):
    str0=input()
    cnt=0
    bo=1
    for k in str0:
        if(k=='('):
            cnt+=1
        else:
            cnt-=1
        if(cnt<0):
            bo=0
            break
    if(bo==1 and cnt==0):
        answer.append("YES")
    else:
        answer.append("NO")
for k in answer:
    print(k)