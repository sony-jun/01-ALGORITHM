from collections import deque

n = int(input())
queue = (deque(range(1, n+1)))
card_list = []
while queue:
    a = queue.popleft()
    card_list.append(a)
    if queue:
        a = queue.popleft()
        queue.append(a)
print(card_list)


