T=int(input())
answer=[]
for i in range(T):
    array0=list(map(int,input().split()))
    dict0={}
    for k in array0:
        if(k not in dict0):
            dict0[k]=1
        else:
            dict0[k]+=1
    for m in dict0:
        if(dict0[m]%2==1):
            answer.append(m)
for j in range(0,T):
    print(f"#"+str(j+1),answer[j])