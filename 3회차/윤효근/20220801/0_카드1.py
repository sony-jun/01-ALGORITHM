from collections import deque
import sys

sys.stdin = open("0_카드1.txt")
n = int(input())
d = deque(list(range(1,n+1)))
result=[]
while d:
    result.append(d.popleft())
    if d:
        d.append(d.popleft())

print(result)