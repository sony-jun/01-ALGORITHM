from collections import deque

n = int(input())
milk = list(map(int,input().split()))
origin = deque([0,1,2])
cnt=0
for i in milk:
    if i == origin[0]:
        cnt+=1
        origin.append(origin.popleft())
    else:
        continue
print(cnt)