import sys
class bulk:
    def __init__(self,ls):
        self.weight=ls[0]
        self.height=ls[1]
        self.rank=1
    def __lt__(self,other):
        if self.weight<other.weight and self.height<other.height:
            return True
        else:
            return False
array0=[]
N=int(input())
for i in range(N):
    temp0=input()
    obj=bulk(list(map(int,temp0.split())))
    array0.append(obj)
for k in array0:
    for m in array0:
        if(k<m):
            k.rank+=1
for d in array0:
    print(d.rank,end=" ")