answer=[]
for m in range(10): 
    T=int(input())
    array0=list(map(int,input().split()))
    a=int(input())
    array1=list(input().split())
    bo=0
    temp0=0
    temp1=0
    temp2=[]
    for i in array1:
        if(i=='I'):
            bo=1
        elif(bo==1):
            temp0=int(i)
            bo+=1
        elif(bo==2):
            temp1=int(i)
            temp2.clear()
            bo+=1
        elif(bo==3):
            temp2.append(int(i))
            temp1-=1
            if(temp1==0):
                temp00=array0[0:temp0]
                temp01=array0[temp0:]
                array0.clear()
                for i0 in temp00:
                    array0.append(i0)
                for i1 in temp2:
                    array0.append(i1)
                for i2 in temp01:
                    array0.append(i2)
    answer.append(array0)
for j in range(0,10):
    print("#"+str(j+1),end=' ')
    for k in range(0,10):
        print(answer[j][k],end=' ')
    print()
