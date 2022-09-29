T=int(input())
answer=[]
for i in range(T):
    T1=int(input())
    array0=list(map(int,input().split()))
    av=0
    people=0
    for k in array0:
        av+=k
    av=av/T1
    for m in array0:
        if(m<=av):
            people+=1
    answer.append(people)
for j in range(0,T):
    print(f"#"+str(j+1),answer[j])