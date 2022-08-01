
from collections import deque


N=int (input())
a=deque(range(1,N+1))
while len(a)>1:
    print(a.popleft(), end=" ")
    a.append(a.popleft())
print(a[0])