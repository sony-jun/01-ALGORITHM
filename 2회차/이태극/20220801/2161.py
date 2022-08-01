from collections import deque
q=[]
a=[]
n=int(input())
for i in range(n):
    q.append(i+1)
dq=deque(q)
for i in range(n-1):
    c=dq.popleft()  
    a.append(c) #버리는 순서대로 추가 
    b=dq[0]     
    dq.append(b)
    dq.popleft()
     
#for i in range(len(q),0,-1):
#print(dq)
for i in a:
    print(i,end=" ")
print(dq[0])