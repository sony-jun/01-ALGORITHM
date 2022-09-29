T=int(input())
answer=[]
for i in range(T):
    sample=input()
    sample=sample[::-1]
    nsample=""
    for k in sample:
        if(k=='p'):
            nsample+='q'
        elif(k=='q'):
             nsample+='p'
        elif(k=='d'):
              nsample+='b'
        elif(k=='b'):
            nsample+='d'
    answer.append(nsample)
for j in range(0,T):
    print("#"+str(j+1),answer[j])