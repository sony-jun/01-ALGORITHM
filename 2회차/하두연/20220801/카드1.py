# 백준 2161 카드1 


from collections import deque
import queue


n = int(input())
queue = deque(range(1, n+1))

while len(queue) > 1:
    print(queue.popleft(), end = " ")
    queue.append(queue.popleft())

print(queue[0])