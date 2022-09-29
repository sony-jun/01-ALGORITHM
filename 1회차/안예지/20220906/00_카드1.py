# 2161

from collections import deque

cards = list(range(1, int(input()) + 1))
# print(cards)

cards = deque(cards)
# print(cards)

while len(cards) != 1:
  print(cards.popleft(), end=" ")
  print('=', cards)
  cards.append(cards.popleft())
  
print(*cards)