# 덱을 이용한 풀이
from collections import deque

N = int(input())
deque_ = deque(range(1, N + 1))

while len(deque_) > 1:
    print(deque_.popleft(), end = ' ')
    deque_.append(deque_.popleft())

print(deque_[0])


# # 큐를 이용한 풀이
# N = int(input())
# queue = list(range(1, N + 1))

# while len(queue) > 1:
#     print(queue.pop(0), end = ' ')
#     queue.append(queue.pop(0))

# print(queue[0])



