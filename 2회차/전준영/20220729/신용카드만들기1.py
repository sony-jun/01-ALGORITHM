T=int(input())
answer=[]
for i in range(T):
    cnt=0
    sum=0 
    Tk=list(map(int,input().split()))
    for k in Tk:
        if(cnt%2==0):
            sum+=2*(k)
        else:
            sum+=k
        cnt+=1
    temp=sum%10
    if(temp==0):
        answer.append(temp)
    else:
        answer.append(10-temp)
for j in range(0,T):
    print(f"#"+str(j+1),answer[j])