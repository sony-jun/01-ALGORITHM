T=int(input())
answer=[]
for i in range(T):
    a=input()
    array0=list(map(int,input().split()))
    dict0=[0]
    for m in range(100):
        dict0.append(0)
    max=0
    max_num=0
    for k in array0:
        dict0[k]+=1
        if(max<dict0[k]):
            max=dict0[k]
            max_num=k
        elif(max==dict0[k]):
            if(max_num<k):
                max_num=k
    answer.append(max_num)
for j in range(0,T):
    print(f"#"+str(j+1),answer[j])