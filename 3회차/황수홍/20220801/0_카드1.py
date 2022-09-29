from collections import deque

n = int(input())
cards = deque(list(range(1,n+1)))
list = []

while cards:
    card = cards.popleft()
    list.append(card)
    if cards:
        card = cards.popleft()
        cards.append(card)
print(' '.join(map(str,list)))