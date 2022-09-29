from collections import deque


N , M = map(int, input().split())

total = []
new_number = []


for a in range(M):
    number = int(input())
    stack = deque(map(int, input().split()))
    total.append(stack)

for a in range(N-M):
  for b in total:
    if len(b) > 0:
        new_number.append(b.pop())
        n = len(new_number)
        

  if sum(new_number) != n*(n+1)/2:
    print('No')
    break

if sum(new_number) == n*(n+1)/2:
    print('Yes')

    
     
        




