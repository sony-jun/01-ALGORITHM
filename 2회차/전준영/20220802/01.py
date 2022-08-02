import sys
import heapq
class anj:
    def __init__(self,num0):
        self.abs_num=abs(num0)
        self.num=num0
    def __lt__(self,other):
        if(self.abs_num<other.abs_num):
            return 1
        elif(self.abs_num==other.abs_num):
            if(self.num<other.num):
                return 1
            else:
                return 0
        else:
            return 0
input=sys.stdin.readline
array0=[]
heapq.heapify(array0)
answer=[]
N=int(input())
for i in range(N):
    input0=int(input())
    if(input0==0):
        if(len(array0)):
            answer.append(heapq.heappop(array0).num)
        else:
            answer.append(0)
    else:
        heapq.heappush(array0,anj(input0))
for k in answer:
    print(k)

