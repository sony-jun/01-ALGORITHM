# # queue
# from collections import deque
n = int(input())
# card = deque([i for i in range(1,n+1)])
# drop = deque([])
card = [i for i in range(1,n+1)]
drop = []

for i in range(1,n):
    # print(drop,card)
    drop.append(card.popleft())
    card.append(card.popleft())
    # print(drop,card)
lst = list(drop+card)
lst = list(map(str,lst))

print(' '.join(lst))