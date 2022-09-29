N = int(input())

# drop = []
# left = [i for i in range(N, 0, -1)]

# for _ in range(N - 1):
#     drop_card = left.pop()
#     drop.append(drop_card)

#     next_card = left.pop()
#     left.insert(0, next_card)

# for i in drop:
#     print(i, end=' ')

# print(left[0])

# 아래는 다른 분의 코드를 참조했다.
from collections import deque

a = []
b = deque(list(range(1, N + 1)))

while len(b) != 1:
    a.append(b.popleft())
    b.append(b.popleft())

print(*a, *b)