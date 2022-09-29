T=int(input())
array0=[]
for i in range(1,T+1):
    array0.append(i)
while(len(array0)):
    num=array0.pop(0)
    print(num,end=" ")
    if(len(array0)):
        num=array0.pop(0)
        array0.append(num)
    else:
        break
