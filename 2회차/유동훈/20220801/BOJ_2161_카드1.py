# https://www.acmicpc.net/problem/2161
# 카드1

# 풀이
from collections import deque

N = int(input())
queue = deque(list(range(1, N+1)))

for i in range(N):
    print(queue.popleft(), end=' ')
    queue.rotate(-1)

